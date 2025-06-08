# SNMP MIB module (ZYXEL-MGS360024F-FUNCTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-MGS360024F-FUNCTION-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:45:43 2025
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

zyxel = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1)
)
_AccessSwitch_ObjectIdentity = ObjectIdentity
accessSwitch = _AccessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5)
)
_EsSeries_ObjectIdentity = ObjectIdentity
esSeries = _EsSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8)
)
_Mgs360024fProductId_ObjectIdentity = ObjectIdentity
mgs360024fProductId = _Mgs360024fProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76)
)
_Mgs360024fSystem_ObjectIdentity = ObjectIdentity
mgs360024fSystem = _Mgs360024fSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1)
)
_Mgs360024fSystemInformation_ObjectIdentity = ObjectIdentity
mgs360024fSystemInformation = _Mgs360024fSystemInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1)
)
_Mgs360024fModelName_Type = DisplayString
_Mgs360024fModelName_Object = MibScalar
mgs360024fModelName = _Mgs360024fModelName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 1),
    _Mgs360024fModelName_Type()
)
mgs360024fModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fModelName.setStatus("current")
_Mgs360024fBIOSVersion_Type = DisplayString
_Mgs360024fBIOSVersion_Object = MibScalar
mgs360024fBIOSVersion = _Mgs360024fBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 2),
    _Mgs360024fBIOSVersion_Type()
)
mgs360024fBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fBIOSVersion.setStatus("current")
_Mgs360024fFirmwareVersion_Type = DisplayString
_Mgs360024fFirmwareVersion_Object = MibScalar
mgs360024fFirmwareVersion = _Mgs360024fFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 3),
    _Mgs360024fFirmwareVersion_Type()
)
mgs360024fFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fFirmwareVersion.setStatus("current")
_Mgs360024fHardwareMechanicalVersion_Type = DisplayString
_Mgs360024fHardwareMechanicalVersion_Object = MibScalar
mgs360024fHardwareMechanicalVersion = _Mgs360024fHardwareMechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 4),
    _Mgs360024fHardwareMechanicalVersion_Type()
)
mgs360024fHardwareMechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fHardwareMechanicalVersion.setStatus("current")
_Mgs360024fSeriesNumber_Type = DisplayString
_Mgs360024fSeriesNumber_Object = MibScalar
mgs360024fSeriesNumber = _Mgs360024fSeriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 5),
    _Mgs360024fSeriesNumber_Type()
)
mgs360024fSeriesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSeriesNumber.setStatus("current")
_Mgs360024fHostMACAddress_Type = MacAddress
_Mgs360024fHostMACAddress_Object = MibScalar
mgs360024fHostMACAddress = _Mgs360024fHostMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 6),
    _Mgs360024fHostMACAddress_Type()
)
mgs360024fHostMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fHostMACAddress.setStatus("current")
_Mgs360024fConsoleBaudrate_Type = DisplayString
_Mgs360024fConsoleBaudrate_Object = MibScalar
mgs360024fConsoleBaudrate = _Mgs360024fConsoleBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 7),
    _Mgs360024fConsoleBaudrate_Type()
)
mgs360024fConsoleBaudrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fConsoleBaudrate.setStatus("current")
_Mgs360024fRAMSize_Type = DisplayString
_Mgs360024fRAMSize_Object = MibScalar
mgs360024fRAMSize = _Mgs360024fRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 8),
    _Mgs360024fRAMSize_Type()
)
mgs360024fRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fRAMSize.setStatus("current")
_Mgs360024fFlashSize_Type = DisplayString
_Mgs360024fFlashSize_Object = MibScalar
mgs360024fFlashSize = _Mgs360024fFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 9),
    _Mgs360024fFlashSize_Type()
)
mgs360024fFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fFlashSize.setStatus("current")
_Mgs360024fBridgeFBDSize_Type = DisplayString
_Mgs360024fBridgeFBDSize_Object = MibScalar
mgs360024fBridgeFBDSize = _Mgs360024fBridgeFBDSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 10),
    _Mgs360024fBridgeFBDSize_Type()
)
mgs360024fBridgeFBDSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fBridgeFBDSize.setStatus("current")
_Mgs360024fTransmitQueue_Type = DisplayString
_Mgs360024fTransmitQueue_Object = MibScalar
mgs360024fTransmitQueue = _Mgs360024fTransmitQueue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 11),
    _Mgs360024fTransmitQueue_Type()
)
mgs360024fTransmitQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fTransmitQueue.setStatus("current")
_Mgs360024fMaximumFrameSize_Type = DisplayString
_Mgs360024fMaximumFrameSize_Object = MibScalar
mgs360024fMaximumFrameSize = _Mgs360024fMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 12),
    _Mgs360024fMaximumFrameSize_Type()
)
mgs360024fMaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMaximumFrameSize.setStatus("current")
_Mgs360024fCPULoad_Type = DisplayString
_Mgs360024fCPULoad_Object = MibScalar
mgs360024fCPULoad = _Mgs360024fCPULoad_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 13),
    _Mgs360024fCPULoad_Type()
)
mgs360024fCPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fCPULoad.setStatus("current")
_Mgs360024fFanSpeed_Type = DisplayString
_Mgs360024fFanSpeed_Object = MibScalar
mgs360024fFanSpeed = _Mgs360024fFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 14),
    _Mgs360024fFanSpeed_Type()
)
mgs360024fFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fFanSpeed.setStatus("current")
_Mgs360024fPowers_Type = DisplayString
_Mgs360024fPowers_Object = MibScalar
mgs360024fPowers = _Mgs360024fPowers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 15),
    _Mgs360024fPowers_Type()
)
mgs360024fPowers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPowers.setStatus("current")
_Mgs360024fTemperature1_Type = DisplayString
_Mgs360024fTemperature1_Object = MibScalar
mgs360024fTemperature1 = _Mgs360024fTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 16),
    _Mgs360024fTemperature1_Type()
)
mgs360024fTemperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fTemperature1.setStatus("current")
_Mgs360024fTemperature2_Type = DisplayString
_Mgs360024fTemperature2_Object = MibScalar
mgs360024fTemperature2 = _Mgs360024fTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 17),
    _Mgs360024fTemperature2_Type()
)
mgs360024fTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fTemperature2.setStatus("current")
_Mgs360024fTemperature3_Type = DisplayString
_Mgs360024fTemperature3_Object = MibScalar
mgs360024fTemperature3 = _Mgs360024fTemperature3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 18),
    _Mgs360024fTemperature3_Type()
)
mgs360024fTemperature3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fTemperature3.setStatus("current")
_Mgs360024fTemperature4_Type = DisplayString
_Mgs360024fTemperature4_Object = MibScalar
mgs360024fTemperature4 = _Mgs360024fTemperature4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 1, 19),
    _Mgs360024fTemperature4_Type()
)
mgs360024fTemperature4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fTemperature4.setStatus("current")
_Mgs360024fSystemTime_ObjectIdentity = ObjectIdentity
mgs360024fSystemTime = _Mgs360024fSystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2)
)
_Mgs360024fSystemTimeManual_ObjectIdentity = ObjectIdentity
mgs360024fSystemTimeManual = _Mgs360024fSystemTimeManual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 1)
)


class _Mgs360024fSystemTimeManualClockSource_Type(Integer32):
    """Custom type mgs360024fSystemTimeManualClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fSystemTimeManualClockSource_Type.__name__ = "Integer32"
_Mgs360024fSystemTimeManualClockSource_Object = MibScalar
mgs360024fSystemTimeManualClockSource = _Mgs360024fSystemTimeManualClockSource_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 1, 1),
    _Mgs360024fSystemTimeManualClockSource_Type()
)
mgs360024fSystemTimeManualClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeManualClockSource.setStatus("current")
_Mgs360024fSystemTimeManualLocaltime_Type = DisplayString
_Mgs360024fSystemTimeManualLocaltime_Object = MibScalar
mgs360024fSystemTimeManualLocaltime = _Mgs360024fSystemTimeManualLocaltime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 1, 2),
    _Mgs360024fSystemTimeManualLocaltime_Type()
)
mgs360024fSystemTimeManualLocaltime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeManualLocaltime.setStatus("current")


class _Mgs360024fSystemTimeManualTimeZoneOffset_Type(Integer32):
    """Custom type mgs360024fSystemTimeManualTimeZoneOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 780),
    )


_Mgs360024fSystemTimeManualTimeZoneOffset_Type.__name__ = "Integer32"
_Mgs360024fSystemTimeManualTimeZoneOffset_Object = MibScalar
mgs360024fSystemTimeManualTimeZoneOffset = _Mgs360024fSystemTimeManualTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 1, 3),
    _Mgs360024fSystemTimeManualTimeZoneOffset_Type()
)
mgs360024fSystemTimeManualTimeZoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeManualTimeZoneOffset.setStatus("current")


class _Mgs360024fSystemTimeManualDaylightSavings_Type(Integer32):
    """Custom type mgs360024fSystemTimeManualDaylightSavings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fSystemTimeManualDaylightSavings_Type.__name__ = "Integer32"
_Mgs360024fSystemTimeManualDaylightSavings_Object = MibScalar
mgs360024fSystemTimeManualDaylightSavings = _Mgs360024fSystemTimeManualDaylightSavings_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 1, 4),
    _Mgs360024fSystemTimeManualDaylightSavings_Type()
)
mgs360024fSystemTimeManualDaylightSavings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeManualDaylightSavings.setStatus("current")


class _Mgs360024fSystemTimeManualTimeSetOffset_Type(Integer32):
    """Custom type mgs360024fSystemTimeManualTimeSetOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Mgs360024fSystemTimeManualTimeSetOffset_Type.__name__ = "Integer32"
_Mgs360024fSystemTimeManualTimeSetOffset_Object = MibScalar
mgs360024fSystemTimeManualTimeSetOffset = _Mgs360024fSystemTimeManualTimeSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 1, 5),
    _Mgs360024fSystemTimeManualTimeSetOffset_Type()
)
mgs360024fSystemTimeManualTimeSetOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeManualTimeSetOffset.setStatus("current")


class _Mgs360024fSystemTimeManualDaylightSavingsType_Type(Integer32):
    """Custom type mgs360024fSystemTimeManualDaylightSavingsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fSystemTimeManualDaylightSavingsType_Type.__name__ = "Integer32"
_Mgs360024fSystemTimeManualDaylightSavingsType_Object = MibScalar
mgs360024fSystemTimeManualDaylightSavingsType = _Mgs360024fSystemTimeManualDaylightSavingsType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 1, 6),
    _Mgs360024fSystemTimeManualDaylightSavingsType_Type()
)
mgs360024fSystemTimeManualDaylightSavingsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeManualDaylightSavingsType.setStatus("current")
_Mgs360024fSystemTimeManualDaylightSavingsBydatesFrom_Type = DisplayString
_Mgs360024fSystemTimeManualDaylightSavingsBydatesFrom_Object = MibScalar
mgs360024fSystemTimeManualDaylightSavingsBydatesFrom = _Mgs360024fSystemTimeManualDaylightSavingsBydatesFrom_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 1, 7),
    _Mgs360024fSystemTimeManualDaylightSavingsBydatesFrom_Type()
)
mgs360024fSystemTimeManualDaylightSavingsBydatesFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeManualDaylightSavingsBydatesFrom.setStatus("current")
_Mgs360024fSystemTimeManualDaylightSavingsBydatesTo_Type = DisplayString
_Mgs360024fSystemTimeManualDaylightSavingsBydatesTo_Object = MibScalar
mgs360024fSystemTimeManualDaylightSavingsBydatesTo = _Mgs360024fSystemTimeManualDaylightSavingsBydatesTo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 1, 8),
    _Mgs360024fSystemTimeManualDaylightSavingsBydatesTo_Type()
)
mgs360024fSystemTimeManualDaylightSavingsBydatesTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeManualDaylightSavingsBydatesTo.setStatus("current")


class _Mgs360024fSystemTimeManualDaylightSavingsRecurringDayFrom_Type(Integer32):
    """Custom type mgs360024fSystemTimeManualDaylightSavingsRecurringDayFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Mgs360024fSystemTimeManualDaylightSavingsRecurringDayFrom_Type.__name__ = "Integer32"
_Mgs360024fSystemTimeManualDaylightSavingsRecurringDayFrom_Object = MibScalar
mgs360024fSystemTimeManualDaylightSavingsRecurringDayFrom = _Mgs360024fSystemTimeManualDaylightSavingsRecurringDayFrom_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 1, 9),
    _Mgs360024fSystemTimeManualDaylightSavingsRecurringDayFrom_Type()
)
mgs360024fSystemTimeManualDaylightSavingsRecurringDayFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeManualDaylightSavingsRecurringDayFrom.setStatus("current")


class _Mgs360024fSystemTimeManualDaylightSavingsRecurringWeekFrom_Type(Integer32):
    """Custom type mgs360024fSystemTimeManualDaylightSavingsRecurringWeekFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Mgs360024fSystemTimeManualDaylightSavingsRecurringWeekFrom_Type.__name__ = "Integer32"
_Mgs360024fSystemTimeManualDaylightSavingsRecurringWeekFrom_Object = MibScalar
mgs360024fSystemTimeManualDaylightSavingsRecurringWeekFrom = _Mgs360024fSystemTimeManualDaylightSavingsRecurringWeekFrom_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 1, 10),
    _Mgs360024fSystemTimeManualDaylightSavingsRecurringWeekFrom_Type()
)
mgs360024fSystemTimeManualDaylightSavingsRecurringWeekFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeManualDaylightSavingsRecurringWeekFrom.setStatus("current")


class _Mgs360024fSystemTimeManualDaylightSavingsRecurringMonthFrom_Type(Integer32):
    """Custom type mgs360024fSystemTimeManualDaylightSavingsRecurringMonthFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_Mgs360024fSystemTimeManualDaylightSavingsRecurringMonthFrom_Type.__name__ = "Integer32"
_Mgs360024fSystemTimeManualDaylightSavingsRecurringMonthFrom_Object = MibScalar
mgs360024fSystemTimeManualDaylightSavingsRecurringMonthFrom = _Mgs360024fSystemTimeManualDaylightSavingsRecurringMonthFrom_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 1, 11),
    _Mgs360024fSystemTimeManualDaylightSavingsRecurringMonthFrom_Type()
)
mgs360024fSystemTimeManualDaylightSavingsRecurringMonthFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeManualDaylightSavingsRecurringMonthFrom.setStatus("current")
_Mgs360024fSystemTimeManualDaylightSavingsRecurringTimeFrom_Type = DisplayString
_Mgs360024fSystemTimeManualDaylightSavingsRecurringTimeFrom_Object = MibScalar
mgs360024fSystemTimeManualDaylightSavingsRecurringTimeFrom = _Mgs360024fSystemTimeManualDaylightSavingsRecurringTimeFrom_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 1, 12),
    _Mgs360024fSystemTimeManualDaylightSavingsRecurringTimeFrom_Type()
)
mgs360024fSystemTimeManualDaylightSavingsRecurringTimeFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeManualDaylightSavingsRecurringTimeFrom.setStatus("current")


class _Mgs360024fSystemTimeManualDaylightSavingsRecurringDayTo_Type(Integer32):
    """Custom type mgs360024fSystemTimeManualDaylightSavingsRecurringDayTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Mgs360024fSystemTimeManualDaylightSavingsRecurringDayTo_Type.__name__ = "Integer32"
_Mgs360024fSystemTimeManualDaylightSavingsRecurringDayTo_Object = MibScalar
mgs360024fSystemTimeManualDaylightSavingsRecurringDayTo = _Mgs360024fSystemTimeManualDaylightSavingsRecurringDayTo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 1, 13),
    _Mgs360024fSystemTimeManualDaylightSavingsRecurringDayTo_Type()
)
mgs360024fSystemTimeManualDaylightSavingsRecurringDayTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeManualDaylightSavingsRecurringDayTo.setStatus("current")


class _Mgs360024fSystemTimeManualDaylightSavingsRecurringWeekTo_Type(Integer32):
    """Custom type mgs360024fSystemTimeManualDaylightSavingsRecurringWeekTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Mgs360024fSystemTimeManualDaylightSavingsRecurringWeekTo_Type.__name__ = "Integer32"
_Mgs360024fSystemTimeManualDaylightSavingsRecurringWeekTo_Object = MibScalar
mgs360024fSystemTimeManualDaylightSavingsRecurringWeekTo = _Mgs360024fSystemTimeManualDaylightSavingsRecurringWeekTo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 1, 14),
    _Mgs360024fSystemTimeManualDaylightSavingsRecurringWeekTo_Type()
)
mgs360024fSystemTimeManualDaylightSavingsRecurringWeekTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeManualDaylightSavingsRecurringWeekTo.setStatus("current")


class _Mgs360024fSystemTimeManualDaylightSavingsRecurringMonthTo_Type(Integer32):
    """Custom type mgs360024fSystemTimeManualDaylightSavingsRecurringMonthTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_Mgs360024fSystemTimeManualDaylightSavingsRecurringMonthTo_Type.__name__ = "Integer32"
_Mgs360024fSystemTimeManualDaylightSavingsRecurringMonthTo_Object = MibScalar
mgs360024fSystemTimeManualDaylightSavingsRecurringMonthTo = _Mgs360024fSystemTimeManualDaylightSavingsRecurringMonthTo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 1, 15),
    _Mgs360024fSystemTimeManualDaylightSavingsRecurringMonthTo_Type()
)
mgs360024fSystemTimeManualDaylightSavingsRecurringMonthTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeManualDaylightSavingsRecurringMonthTo.setStatus("current")
_Mgs360024fSystemTimeManualDaylightSavingsRecurringTimeTo_Type = DisplayString
_Mgs360024fSystemTimeManualDaylightSavingsRecurringTimeTo_Object = MibScalar
mgs360024fSystemTimeManualDaylightSavingsRecurringTimeTo = _Mgs360024fSystemTimeManualDaylightSavingsRecurringTimeTo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 1, 16),
    _Mgs360024fSystemTimeManualDaylightSavingsRecurringTimeTo_Type()
)
mgs360024fSystemTimeManualDaylightSavingsRecurringTimeTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeManualDaylightSavingsRecurringTimeTo.setStatus("current")
_Mgs360024fSystemTimeNTP_ObjectIdentity = ObjectIdentity
mgs360024fSystemTimeNTP = _Mgs360024fSystemTimeNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 2)
)
_Mgs360024fSystemTimeNTPTable_Object = MibTable
mgs360024fSystemTimeNTPTable = _Mgs360024fSystemTimeNTPTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mgs360024fSystemTimeNTPTable.setStatus("current")
_Mgs360024fSystemTimeNTPEntry_Object = MibTableRow
mgs360024fSystemTimeNTPEntry = _Mgs360024fSystemTimeNTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 2, 1, 1)
)
mgs360024fSystemTimeNTPEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fSystemTimeNTPIndex"),
)
if mibBuilder.loadTexts:
    mgs360024fSystemTimeNTPEntry.setStatus("current")


class _Mgs360024fSystemTimeNTPIndex_Type(Integer32):
    """Custom type mgs360024fSystemTimeNTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Mgs360024fSystemTimeNTPIndex_Type.__name__ = "Integer32"
_Mgs360024fSystemTimeNTPIndex_Object = MibTableColumn
mgs360024fSystemTimeNTPIndex = _Mgs360024fSystemTimeNTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 2, 1, 1, 1),
    _Mgs360024fSystemTimeNTPIndex_Type()
)
mgs360024fSystemTimeNTPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeNTPIndex.setStatus("current")


class _Mgs360024fSystemTimeNTPServerIPType_Type(Integer32):
    """Custom type mgs360024fSystemTimeNTPServerIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fSystemTimeNTPServerIPType_Type.__name__ = "Integer32"
_Mgs360024fSystemTimeNTPServerIPType_Object = MibTableColumn
mgs360024fSystemTimeNTPServerIPType = _Mgs360024fSystemTimeNTPServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 2, 1, 1, 2),
    _Mgs360024fSystemTimeNTPServerIPType_Type()
)
mgs360024fSystemTimeNTPServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeNTPServerIPType.setStatus("current")
_Mgs360024fSystemTimeNTPServer_Type = DisplayString
_Mgs360024fSystemTimeNTPServer_Object = MibTableColumn
mgs360024fSystemTimeNTPServer = _Mgs360024fSystemTimeNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 2, 1, 1, 3),
    _Mgs360024fSystemTimeNTPServer_Type()
)
mgs360024fSystemTimeNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeNTPServer.setStatus("current")


class _Mgs360024fSystemTimeNTPCurrentMode_Type(Integer32):
    """Custom type mgs360024fSystemTimeNTPCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Mgs360024fSystemTimeNTPCurrentMode_Type.__name__ = "Integer32"
_Mgs360024fSystemTimeNTPCurrentMode_Object = MibTableColumn
mgs360024fSystemTimeNTPCurrentMode = _Mgs360024fSystemTimeNTPCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 2, 2, 1, 1, 4),
    _Mgs360024fSystemTimeNTPCurrentMode_Type()
)
mgs360024fSystemTimeNTPCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemTimeNTPCurrentMode.setStatus("current")
_Mgs360024fSystemAccount_ObjectIdentity = ObjectIdentity
mgs360024fSystemAccount = _Mgs360024fSystemAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3)
)
_Mgs360024fSystemAccountUsers_ObjectIdentity = ObjectIdentity
mgs360024fSystemAccountUsers = _Mgs360024fSystemAccountUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 1)
)


class _Mgs360024fSystemAccountUserCreate_Type(Integer32):
    """Custom type mgs360024fSystemAccountUserCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fSystemAccountUserCreate_Type.__name__ = "Integer32"
_Mgs360024fSystemAccountUserCreate_Object = MibScalar
mgs360024fSystemAccountUserCreate = _Mgs360024fSystemAccountUserCreate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 1, 1),
    _Mgs360024fSystemAccountUserCreate_Type()
)
mgs360024fSystemAccountUserCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemAccountUserCreate.setStatus("current")
_Mgs360024fSystemAccountUsersTable_Object = MibTable
mgs360024fSystemAccountUsersTable = _Mgs360024fSystemAccountUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    mgs360024fSystemAccountUsersTable.setStatus("current")
_Mgs360024fSystemAccountUsersEntry_Object = MibTableRow
mgs360024fSystemAccountUsersEntry = _Mgs360024fSystemAccountUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 1, 2, 1)
)
mgs360024fSystemAccountUsersEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fUserIndex"),
)
if mibBuilder.loadTexts:
    mgs360024fSystemAccountUsersEntry.setStatus("current")


class _Mgs360024fUserIndex_Type(Integer32):
    """Custom type mgs360024fUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Mgs360024fUserIndex_Type.__name__ = "Integer32"
_Mgs360024fUserIndex_Object = MibTableColumn
mgs360024fUserIndex = _Mgs360024fUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 1, 2, 1, 1),
    _Mgs360024fUserIndex_Type()
)
mgs360024fUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fUserIndex.setStatus("current")


class _Mgs360024fUserName_Type(DisplayString):
    """Custom type mgs360024fUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Mgs360024fUserName_Type.__name__ = "DisplayString"
_Mgs360024fUserName_Object = MibTableColumn
mgs360024fUserName = _Mgs360024fUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 1, 2, 1, 2),
    _Mgs360024fUserName_Type()
)
mgs360024fUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fUserName.setStatus("current")


class _Mgs360024fPassword_Type(DisplayString):
    """Custom type mgs360024fPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Mgs360024fPassword_Type.__name__ = "DisplayString"
_Mgs360024fPassword_Object = MibTableColumn
mgs360024fPassword = _Mgs360024fPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 1, 2, 1, 3),
    _Mgs360024fPassword_Type()
)
mgs360024fPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPassword.setStatus("current")


class _Mgs360024fUserPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fUserPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fUserPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fUserPrivilegeLevel_Object = MibTableColumn
mgs360024fUserPrivilegeLevel = _Mgs360024fUserPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 1, 2, 1, 4),
    _Mgs360024fUserPrivilegeLevel_Type()
)
mgs360024fUserPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fUserPrivilegeLevel.setStatus("current")


class _Mgs360024fAccountUserRowStatus_Type(Integer32):
    """Custom type mgs360024fAccountUserRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Mgs360024fAccountUserRowStatus_Type.__name__ = "Integer32"
_Mgs360024fAccountUserRowStatus_Object = MibTableColumn
mgs360024fAccountUserRowStatus = _Mgs360024fAccountUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 1, 2, 1, 5),
    _Mgs360024fAccountUserRowStatus_Type()
)
mgs360024fAccountUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fAccountUserRowStatus.setStatus("current")
_Mgs360024fSystemAccountPrivilegeLevel_ObjectIdentity = ObjectIdentity
mgs360024fSystemAccountPrivilegeLevel = _Mgs360024fSystemAccountPrivilegeLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2)
)


class _Mgs360024fAccountPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fAccountPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fAccountPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fAccountPrivilegeLevel_Object = MibScalar
mgs360024fAccountPrivilegeLevel = _Mgs360024fAccountPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 1),
    _Mgs360024fAccountPrivilegeLevel_Type()
)
mgs360024fAccountPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fAccountPrivilegeLevel.setStatus("current")


class _Mgs360024fAggregationPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fAggregationPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fAggregationPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fAggregationPrivilegeLevel_Object = MibScalar
mgs360024fAggregationPrivilegeLevel = _Mgs360024fAggregationPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 2),
    _Mgs360024fAggregationPrivilegeLevel_Type()
)
mgs360024fAggregationPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fAggregationPrivilegeLevel.setStatus("current")


class _Mgs360024fDiagnosticsPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fDiagnosticsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fDiagnosticsPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fDiagnosticsPrivilegeLevel_Object = MibScalar
mgs360024fDiagnosticsPrivilegeLevel = _Mgs360024fDiagnosticsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 3),
    _Mgs360024fDiagnosticsPrivilegeLevel_Type()
)
mgs360024fDiagnosticsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fDiagnosticsPrivilegeLevel.setStatus("current")


class _Mgs360024fEPSPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fEPSPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fEPSPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fEPSPrivilegeLevel_Object = MibScalar
mgs360024fEPSPrivilegeLevel = _Mgs360024fEPSPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 5),
    _Mgs360024fEPSPrivilegeLevel_Type()
)
mgs360024fEPSPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fEPSPrivilegeLevel.setStatus("current")


class _Mgs360024fERPSPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fERPSPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fERPSPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fERPSPrivilegeLevel_Object = MibScalar
mgs360024fERPSPrivilegeLevel = _Mgs360024fERPSPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 6),
    _Mgs360024fERPSPrivilegeLevel_Type()
)
mgs360024fERPSPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSPrivilegeLevel.setStatus("current")


class _Mgs360024fETHLinkOAMPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fETHLinkOAMPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fETHLinkOAMPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fETHLinkOAMPrivilegeLevel_Object = MibScalar
mgs360024fETHLinkOAMPrivilegeLevel = _Mgs360024fETHLinkOAMPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 7),
    _Mgs360024fETHLinkOAMPrivilegeLevel_Type()
)
mgs360024fETHLinkOAMPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fETHLinkOAMPrivilegeLevel.setStatus("current")


class _Mgs360024fEVCPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fEVCPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fEVCPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fEVCPrivilegeLevel_Object = MibScalar
mgs360024fEVCPrivilegeLevel = _Mgs360024fEVCPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 8),
    _Mgs360024fEVCPrivilegeLevel_Type()
)
mgs360024fEVCPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fEVCPrivilegeLevel.setStatus("current")


class _Mgs360024fGARPPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fGARPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fGARPPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fGARPPrivilegeLevel_Object = MibScalar
mgs360024fGARPPrivilegeLevel = _Mgs360024fGARPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 10),
    _Mgs360024fGARPPrivilegeLevel_Type()
)
mgs360024fGARPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fGARPPrivilegeLevel.setStatus("current")


class _Mgs360024fGVRPPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fGVRPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fGVRPPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fGVRPPrivilegeLevel_Object = MibScalar
mgs360024fGVRPPrivilegeLevel = _Mgs360024fGVRPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 11),
    _Mgs360024fGVRPPrivilegeLevel_Type()
)
mgs360024fGVRPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fGVRPPrivilegeLevel.setStatus("current")


class _Mgs360024fIPPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fIPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fIPPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fIPPrivilegeLevel_Object = MibScalar
mgs360024fIPPrivilegeLevel = _Mgs360024fIPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 12),
    _Mgs360024fIPPrivilegeLevel_Type()
)
mgs360024fIPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIPPrivilegeLevel.setStatus("current")


class _Mgs360024fIPMCSnoopingPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fIPMCSnoopingPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fIPMCSnoopingPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fIPMCSnoopingPrivilegeLevel_Object = MibScalar
mgs360024fIPMCSnoopingPrivilegeLevel = _Mgs360024fIPMCSnoopingPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 13),
    _Mgs360024fIPMCSnoopingPrivilegeLevel_Type()
)
mgs360024fIPMCSnoopingPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIPMCSnoopingPrivilegeLevel.setStatus("current")


class _Mgs360024fLACPPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fLACPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fLACPPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fLACPPrivilegeLevel_Object = MibScalar
mgs360024fLACPPrivilegeLevel = _Mgs360024fLACPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 14),
    _Mgs360024fLACPPrivilegeLevel_Type()
)
mgs360024fLACPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fLACPPrivilegeLevel.setStatus("current")


class _Mgs360024fLLDPPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fLLDPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fLLDPPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fLLDPPrivilegeLevel_Object = MibScalar
mgs360024fLLDPPrivilegeLevel = _Mgs360024fLLDPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 15),
    _Mgs360024fLLDPPrivilegeLevel_Type()
)
mgs360024fLLDPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fLLDPPrivilegeLevel.setStatus("current")


class _Mgs360024fLLDPMEDPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fLLDPMEDPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fLLDPMEDPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fLLDPMEDPrivilegeLevel_Object = MibScalar
mgs360024fLLDPMEDPrivilegeLevel = _Mgs360024fLLDPMEDPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 16),
    _Mgs360024fLLDPMEDPrivilegeLevel_Type()
)
mgs360024fLLDPMEDPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fLLDPMEDPrivilegeLevel.setStatus("current")


class _Mgs360024fLoopProtectPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fLoopProtectPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fLoopProtectPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fLoopProtectPrivilegeLevel_Object = MibScalar
mgs360024fLoopProtectPrivilegeLevel = _Mgs360024fLoopProtectPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 17),
    _Mgs360024fLoopProtectPrivilegeLevel_Type()
)
mgs360024fLoopProtectPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fLoopProtectPrivilegeLevel.setStatus("current")


class _Mgs360024fMACTablePrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fMACTablePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fMACTablePrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fMACTablePrivilegeLevel_Object = MibScalar
mgs360024fMACTablePrivilegeLevel = _Mgs360024fMACTablePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 18),
    _Mgs360024fMACTablePrivilegeLevel_Type()
)
mgs360024fMACTablePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMACTablePrivilegeLevel.setStatus("current")


class _Mgs360024fMEPPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fMEPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fMEPPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fMEPPrivilegeLevel_Object = MibScalar
mgs360024fMEPPrivilegeLevel = _Mgs360024fMEPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 20),
    _Mgs360024fMEPPrivilegeLevel_Type()
)
mgs360024fMEPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMEPPrivilegeLevel.setStatus("current")


class _Mgs360024fMRSTPPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fMRSTPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fMRSTPPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fMRSTPPrivilegeLevel_Object = MibScalar
mgs360024fMRSTPPrivilegeLevel = _Mgs360024fMRSTPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 21),
    _Mgs360024fMRSTPPrivilegeLevel_Type()
)
mgs360024fMRSTPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMRSTPPrivilegeLevel.setStatus("current")


class _Mgs360024fMVRPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fMVRPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fMVRPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fMVRPrivilegeLevel_Object = MibScalar
mgs360024fMVRPrivilegeLevel = _Mgs360024fMVRPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 22),
    _Mgs360024fMVRPrivilegeLevel_Type()
)
mgs360024fMVRPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMVRPrivilegeLevel.setStatus("current")


class _Mgs360024fMaintenancePrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fMaintenancePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fMaintenancePrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fMaintenancePrivilegeLevel_Object = MibScalar
mgs360024fMaintenancePrivilegeLevel = _Mgs360024fMaintenancePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 24),
    _Mgs360024fMaintenancePrivilegeLevel_Type()
)
mgs360024fMaintenancePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMaintenancePrivilegeLevel.setStatus("current")


class _Mgs360024fMirroringPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fMirroringPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fMirroringPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fMirroringPrivilegeLevel_Object = MibScalar
mgs360024fMirroringPrivilegeLevel = _Mgs360024fMirroringPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 25),
    _Mgs360024fMirroringPrivilegeLevel_Type()
)
mgs360024fMirroringPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMirroringPrivilegeLevel.setStatus("current")


class _Mgs360024fPTPPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fPTPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fPTPPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fPTPPrivilegeLevel_Object = MibScalar
mgs360024fPTPPrivilegeLevel = _Mgs360024fPTPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 26),
    _Mgs360024fPTPPrivilegeLevel_Type()
)
mgs360024fPTPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPTPPrivilegeLevel.setStatus("current")


class _Mgs360024fPortsPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fPortsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fPortsPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fPortsPrivilegeLevel_Object = MibScalar
mgs360024fPortsPrivilegeLevel = _Mgs360024fPortsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 27),
    _Mgs360024fPortsPrivilegeLevel_Type()
)
mgs360024fPortsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPortsPrivilegeLevel.setStatus("current")


class _Mgs360024fPrivateVLANsPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fPrivateVLANsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fPrivateVLANsPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fPrivateVLANsPrivilegeLevel_Object = MibScalar
mgs360024fPrivateVLANsPrivilegeLevel = _Mgs360024fPrivateVLANsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 28),
    _Mgs360024fPrivateVLANsPrivilegeLevel_Type()
)
mgs360024fPrivateVLANsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPrivateVLANsPrivilegeLevel.setStatus("current")


class _Mgs360024fQoSPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fQoSPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fQoSPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fQoSPrivilegeLevel_Object = MibScalar
mgs360024fQoSPrivilegeLevel = _Mgs360024fQoSPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 29),
    _Mgs360024fQoSPrivilegeLevel_Type()
)
mgs360024fQoSPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fQoSPrivilegeLevel.setStatus("current")


class _Mgs360024fSMTPPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fSMTPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fSMTPPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fSMTPPrivilegeLevel_Object = MibScalar
mgs360024fSMTPPrivilegeLevel = _Mgs360024fSMTPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 31),
    _Mgs360024fSMTPPrivilegeLevel_Type()
)
mgs360024fSMTPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSMTPPrivilegeLevel.setStatus("current")


class _Mgs360024fSNMPPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fSNMPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fSNMPPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fSNMPPrivilegeLevel_Object = MibScalar
mgs360024fSNMPPrivilegeLevel = _Mgs360024fSNMPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 32),
    _Mgs360024fSNMPPrivilegeLevel_Type()
)
mgs360024fSNMPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSNMPPrivilegeLevel.setStatus("current")


class _Mgs360024fSecurityPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fSecurityPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fSecurityPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fSecurityPrivilegeLevel_Object = MibScalar
mgs360024fSecurityPrivilegeLevel = _Mgs360024fSecurityPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 33),
    _Mgs360024fSecurityPrivilegeLevel_Type()
)
mgs360024fSecurityPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSecurityPrivilegeLevel.setStatus("current")


class _Mgs360024fSpanningTreePrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fSpanningTreePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fSpanningTreePrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fSpanningTreePrivilegeLevel_Object = MibScalar
mgs360024fSpanningTreePrivilegeLevel = _Mgs360024fSpanningTreePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 35),
    _Mgs360024fSpanningTreePrivilegeLevel_Type()
)
mgs360024fSpanningTreePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSpanningTreePrivilegeLevel.setStatus("current")


class _Mgs360024fSystemPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fSystemPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fSystemPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fSystemPrivilegeLevel_Object = MibScalar
mgs360024fSystemPrivilegeLevel = _Mgs360024fSystemPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 36),
    _Mgs360024fSystemPrivilegeLevel_Type()
)
mgs360024fSystemPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSystemPrivilegeLevel.setStatus("current")


class _Mgs360024fTrapEventPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fTrapEventPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fTrapEventPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fTrapEventPrivilegeLevel_Object = MibScalar
mgs360024fTrapEventPrivilegeLevel = _Mgs360024fTrapEventPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 37),
    _Mgs360024fTrapEventPrivilegeLevel_Type()
)
mgs360024fTrapEventPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventPrivilegeLevel.setStatus("current")


class _Mgs360024fVCLPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fVCLPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fVCLPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fVCLPrivilegeLevel_Object = MibScalar
mgs360024fVCLPrivilegeLevel = _Mgs360024fVCLPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 39),
    _Mgs360024fVCLPrivilegeLevel_Type()
)
mgs360024fVCLPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fVCLPrivilegeLevel.setStatus("current")


class _Mgs360024fVLANTranslationPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fVLANTranslationPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fVLANTranslationPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fVLANTranslationPrivilegeLevel_Object = MibScalar
mgs360024fVLANTranslationPrivilegeLevel = _Mgs360024fVLANTranslationPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 40),
    _Mgs360024fVLANTranslationPrivilegeLevel_Type()
)
mgs360024fVLANTranslationPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fVLANTranslationPrivilegeLevel.setStatus("current")


class _Mgs360024fVLANsPrivilegeLevel_Type(Integer32):
    """Custom type mgs360024fVLANsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Mgs360024fVLANsPrivilegeLevel_Type.__name__ = "Integer32"
_Mgs360024fVLANsPrivilegeLevel_Object = MibScalar
mgs360024fVLANsPrivilegeLevel = _Mgs360024fVLANsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 3, 2, 41),
    _Mgs360024fVLANsPrivilegeLevel_Type()
)
mgs360024fVLANsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fVLANsPrivilegeLevel.setStatus("current")
_Mgs360024fIP_ObjectIdentity = ObjectIdentity
mgs360024fIP = _Mgs360024fIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4)
)
_Mgs360024fIPv4_ObjectIdentity = ObjectIdentity
mgs360024fIPv4 = _Mgs360024fIPv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 1)
)
_Mgs360024fIPv4Configured_ObjectIdentity = ObjectIdentity
mgs360024fIPv4Configured = _Mgs360024fIPv4Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 1, 1)
)


class _Mgs360024fIpv4DHCPClient_Type(Integer32):
    """Custom type mgs360024fIpv4DHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fIpv4DHCPClient_Type.__name__ = "Integer32"
_Mgs360024fIpv4DHCPClient_Object = MibScalar
mgs360024fIpv4DHCPClient = _Mgs360024fIpv4DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 1, 1, 1),
    _Mgs360024fIpv4DHCPClient_Type()
)
mgs360024fIpv4DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIpv4DHCPClient.setStatus("current")
_Mgs360024fIPv4Address_Type = IpAddress
_Mgs360024fIPv4Address_Object = MibScalar
mgs360024fIPv4Address = _Mgs360024fIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 1, 1, 2),
    _Mgs360024fIPv4Address_Type()
)
mgs360024fIPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIPv4Address.setStatus("current")
_Mgs360024fIPv4Mask_Type = IpAddress
_Mgs360024fIPv4Mask_Object = MibScalar
mgs360024fIPv4Mask = _Mgs360024fIPv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 1, 1, 3),
    _Mgs360024fIPv4Mask_Type()
)
mgs360024fIPv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIPv4Mask.setStatus("current")
_Mgs360024fIPv4Router_Type = IpAddress
_Mgs360024fIPv4Router_Object = MibScalar
mgs360024fIPv4Router = _Mgs360024fIPv4Router_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 1, 1, 4),
    _Mgs360024fIPv4Router_Type()
)
mgs360024fIPv4Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIPv4Router.setStatus("current")


class _Mgs360024fIPv4VLANId_Type(Integer32):
    """Custom type mgs360024fIPv4VLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Mgs360024fIPv4VLANId_Type.__name__ = "Integer32"
_Mgs360024fIPv4VLANId_Object = MibScalar
mgs360024fIPv4VLANId = _Mgs360024fIPv4VLANId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 1, 1, 5),
    _Mgs360024fIPv4VLANId_Type()
)
mgs360024fIPv4VLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIPv4VLANId.setStatus("current")
_Mgs360024fIPv4DNSServer_Type = IpAddress
_Mgs360024fIPv4DNSServer_Object = MibScalar
mgs360024fIPv4DNSServer = _Mgs360024fIPv4DNSServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 1, 1, 6),
    _Mgs360024fIPv4DNSServer_Type()
)
mgs360024fIPv4DNSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIPv4DNSServer.setStatus("current")


class _Mgs360024fIPv4DNSProxy_Type(Integer32):
    """Custom type mgs360024fIPv4DNSProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fIPv4DNSProxy_Type.__name__ = "Integer32"
_Mgs360024fIPv4DNSProxy_Object = MibScalar
mgs360024fIPv4DNSProxy = _Mgs360024fIPv4DNSProxy_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 1, 1, 7),
    _Mgs360024fIPv4DNSProxy_Type()
)
mgs360024fIPv4DNSProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIPv4DNSProxy.setStatus("current")
_Mgs360024fIPv4Current_ObjectIdentity = ObjectIdentity
mgs360024fIPv4Current = _Mgs360024fIPv4Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 1, 2)
)


class _Mgs360024fIpv4CurrentDHCPClient_Type(Integer32):
    """Custom type mgs360024fIpv4CurrentDHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fIpv4CurrentDHCPClient_Type.__name__ = "Integer32"
_Mgs360024fIpv4CurrentDHCPClient_Object = MibScalar
mgs360024fIpv4CurrentDHCPClient = _Mgs360024fIpv4CurrentDHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 1, 2, 1),
    _Mgs360024fIpv4CurrentDHCPClient_Type()
)
mgs360024fIpv4CurrentDHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIpv4CurrentDHCPClient.setStatus("current")
_Mgs360024fIPv4CurrentAddress_Type = IpAddress
_Mgs360024fIPv4CurrentAddress_Object = MibScalar
mgs360024fIPv4CurrentAddress = _Mgs360024fIPv4CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 1, 2, 2),
    _Mgs360024fIPv4CurrentAddress_Type()
)
mgs360024fIPv4CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fIPv4CurrentAddress.setStatus("current")
_Mgs360024fIPv4CurrentMask_Type = IpAddress
_Mgs360024fIPv4CurrentMask_Object = MibScalar
mgs360024fIPv4CurrentMask = _Mgs360024fIPv4CurrentMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 1, 2, 3),
    _Mgs360024fIPv4CurrentMask_Type()
)
mgs360024fIPv4CurrentMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fIPv4CurrentMask.setStatus("current")
_Mgs360024fIPv4CurrentRouter_Type = IpAddress
_Mgs360024fIPv4CurrentRouter_Object = MibScalar
mgs360024fIPv4CurrentRouter = _Mgs360024fIPv4CurrentRouter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 1, 2, 4),
    _Mgs360024fIPv4CurrentRouter_Type()
)
mgs360024fIPv4CurrentRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fIPv4CurrentRouter.setStatus("current")


class _Mgs360024fIPv4CurrentVLANId_Type(Integer32):
    """Custom type mgs360024fIPv4CurrentVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Mgs360024fIPv4CurrentVLANId_Type.__name__ = "Integer32"
_Mgs360024fIPv4CurrentVLANId_Object = MibScalar
mgs360024fIPv4CurrentVLANId = _Mgs360024fIPv4CurrentVLANId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 1, 2, 5),
    _Mgs360024fIPv4CurrentVLANId_Type()
)
mgs360024fIPv4CurrentVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fIPv4CurrentVLANId.setStatus("current")
_Mgs360024fIPv4CurrentDNSServer_Type = IpAddress
_Mgs360024fIPv4CurrentDNSServer_Object = MibScalar
mgs360024fIPv4CurrentDNSServer = _Mgs360024fIPv4CurrentDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 1, 2, 6),
    _Mgs360024fIPv4CurrentDNSServer_Type()
)
mgs360024fIPv4CurrentDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fIPv4CurrentDNSServer.setStatus("current")
_Mgs360024fIPv6_ObjectIdentity = ObjectIdentity
mgs360024fIPv6 = _Mgs360024fIPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 2)
)
_Mgs360024fIPv6Configured_ObjectIdentity = ObjectIdentity
mgs360024fIPv6Configured = _Mgs360024fIPv6Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 2, 1)
)


class _Mgs360024fIpv6AutoConfiguration_Type(Integer32):
    """Custom type mgs360024fIpv6AutoConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fIpv6AutoConfiguration_Type.__name__ = "Integer32"
_Mgs360024fIpv6AutoConfiguration_Object = MibScalar
mgs360024fIpv6AutoConfiguration = _Mgs360024fIpv6AutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 2, 1, 1),
    _Mgs360024fIpv6AutoConfiguration_Type()
)
mgs360024fIpv6AutoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIpv6AutoConfiguration.setStatus("current")


class _Mgs360024fIpv6Address_Type(DisplayString):
    """Custom type mgs360024fIpv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Mgs360024fIpv6Address_Type.__name__ = "DisplayString"
_Mgs360024fIpv6Address_Object = MibScalar
mgs360024fIpv6Address = _Mgs360024fIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 2, 1, 2),
    _Mgs360024fIpv6Address_Type()
)
mgs360024fIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIpv6Address.setStatus("current")


class _Mgs360024fIpv6Prefix_Type(Integer32):
    """Custom type mgs360024fIpv6Prefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Mgs360024fIpv6Prefix_Type.__name__ = "Integer32"
_Mgs360024fIpv6Prefix_Object = MibScalar
mgs360024fIpv6Prefix = _Mgs360024fIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 2, 1, 3),
    _Mgs360024fIpv6Prefix_Type()
)
mgs360024fIpv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIpv6Prefix.setStatus("current")


class _Mgs360024fIpv6Router_Type(DisplayString):
    """Custom type mgs360024fIpv6Router based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Mgs360024fIpv6Router_Type.__name__ = "DisplayString"
_Mgs360024fIpv6Router_Object = MibScalar
mgs360024fIpv6Router = _Mgs360024fIpv6Router_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 2, 1, 4),
    _Mgs360024fIpv6Router_Type()
)
mgs360024fIpv6Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIpv6Router.setStatus("current")
_Mgs360024fIPv6Current_ObjectIdentity = ObjectIdentity
mgs360024fIPv6Current = _Mgs360024fIPv6Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 2, 2)
)


class _Mgs360024fIpv6CurrentAutoConfiguration_Type(Integer32):
    """Custom type mgs360024fIpv6CurrentAutoConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fIpv6CurrentAutoConfiguration_Type.__name__ = "Integer32"
_Mgs360024fIpv6CurrentAutoConfiguration_Object = MibScalar
mgs360024fIpv6CurrentAutoConfiguration = _Mgs360024fIpv6CurrentAutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 2, 2, 1),
    _Mgs360024fIpv6CurrentAutoConfiguration_Type()
)
mgs360024fIpv6CurrentAutoConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fIpv6CurrentAutoConfiguration.setStatus("current")


class _Mgs360024fIpv6CurrentAddress_Type(DisplayString):
    """Custom type mgs360024fIpv6CurrentAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Mgs360024fIpv6CurrentAddress_Type.__name__ = "DisplayString"
_Mgs360024fIpv6CurrentAddress_Object = MibScalar
mgs360024fIpv6CurrentAddress = _Mgs360024fIpv6CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 2, 2, 2),
    _Mgs360024fIpv6CurrentAddress_Type()
)
mgs360024fIpv6CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fIpv6CurrentAddress.setStatus("current")


class _Mgs360024fIpv6CurrentLinkLocalAddress_Type(DisplayString):
    """Custom type mgs360024fIpv6CurrentLinkLocalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Mgs360024fIpv6CurrentLinkLocalAddress_Type.__name__ = "DisplayString"
_Mgs360024fIpv6CurrentLinkLocalAddress_Object = MibScalar
mgs360024fIpv6CurrentLinkLocalAddress = _Mgs360024fIpv6CurrentLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 2, 2, 3),
    _Mgs360024fIpv6CurrentLinkLocalAddress_Type()
)
mgs360024fIpv6CurrentLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fIpv6CurrentLinkLocalAddress.setStatus("current")


class _Mgs360024fIpv6CurrentPrefix_Type(Integer32):
    """Custom type mgs360024fIpv6CurrentPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Mgs360024fIpv6CurrentPrefix_Type.__name__ = "Integer32"
_Mgs360024fIpv6CurrentPrefix_Object = MibScalar
mgs360024fIpv6CurrentPrefix = _Mgs360024fIpv6CurrentPrefix_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 2, 2, 4),
    _Mgs360024fIpv6CurrentPrefix_Type()
)
mgs360024fIpv6CurrentPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fIpv6CurrentPrefix.setStatus("current")


class _Mgs360024fIpv6CurrentRouter_Type(DisplayString):
    """Custom type mgs360024fIpv6CurrentRouter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Mgs360024fIpv6CurrentRouter_Type.__name__ = "DisplayString"
_Mgs360024fIpv6CurrentRouter_Object = MibScalar
mgs360024fIpv6CurrentRouter = _Mgs360024fIpv6CurrentRouter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 4, 2, 2, 5),
    _Mgs360024fIpv6CurrentRouter_Type()
)
mgs360024fIpv6CurrentRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fIpv6CurrentRouter.setStatus("current")
_Mgs360024fSyslog_ObjectIdentity = ObjectIdentity
mgs360024fSyslog = _Mgs360024fSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 5)
)
_Mgs360024fSyslogConf_ObjectIdentity = ObjectIdentity
mgs360024fSyslogConf = _Mgs360024fSyslogConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 5, 1)
)


class _Mgs360024fServerMode_Type(Integer32):
    """Custom type mgs360024fServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fServerMode_Type.__name__ = "Integer32"
_Mgs360024fServerMode_Object = MibScalar
mgs360024fServerMode = _Mgs360024fServerMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 5, 1, 1),
    _Mgs360024fServerMode_Type()
)
mgs360024fServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fServerMode.setStatus("current")
_Mgs360024fServerAddress1_Type = IpAddress
_Mgs360024fServerAddress1_Object = MibScalar
mgs360024fServerAddress1 = _Mgs360024fServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 5, 1, 2),
    _Mgs360024fServerAddress1_Type()
)
mgs360024fServerAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fServerAddress1.setStatus("current")
_Mgs360024fServerAddress2_Type = IpAddress
_Mgs360024fServerAddress2_Object = MibScalar
mgs360024fServerAddress2 = _Mgs360024fServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 5, 1, 3),
    _Mgs360024fServerAddress2_Type()
)
mgs360024fServerAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fServerAddress2.setStatus("current")


class _Mgs360024fSyslogLevel_Type(Integer32):
    """Custom type mgs360024fSyslogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fSyslogLevel_Type.__name__ = "Integer32"
_Mgs360024fSyslogLevel_Object = MibScalar
mgs360024fSyslogLevel = _Mgs360024fSyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 5, 1, 4),
    _Mgs360024fSyslogLevel_Type()
)
mgs360024fSyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSyslogLevel.setStatus("current")
_Mgs360024fSyslogDetailedInfo_ObjectIdentity = ObjectIdentity
mgs360024fSyslogDetailedInfo = _Mgs360024fSyslogDetailedInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 5, 2)
)


class _Mgs360024fSyslogDetailedInfoClear_Type(Integer32):
    """Custom type mgs360024fSyslogDetailedInfoClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fSyslogDetailedInfoClear_Type.__name__ = "Integer32"
_Mgs360024fSyslogDetailedInfoClear_Object = MibScalar
mgs360024fSyslogDetailedInfoClear = _Mgs360024fSyslogDetailedInfoClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 5, 2, 1),
    _Mgs360024fSyslogDetailedInfoClear_Type()
)
mgs360024fSyslogDetailedInfoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSyslogDetailedInfoClear.setStatus("current")
_Mgs360024fSyslogDetailedInfoTable_Object = MibTable
mgs360024fSyslogDetailedInfoTable = _Mgs360024fSyslogDetailedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    mgs360024fSyslogDetailedInfoTable.setStatus("current")
_Mgs360024fSyslogDetailedInfoEntry_Object = MibTableRow
mgs360024fSyslogDetailedInfoEntry = _Mgs360024fSyslogDetailedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 5, 2, 2, 1)
)
mgs360024fSyslogDetailedInfoEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fSyslogDetailedInfoIndex"),
)
if mibBuilder.loadTexts:
    mgs360024fSyslogDetailedInfoEntry.setStatus("current")


class _Mgs360024fSyslogDetailedInfoIndex_Type(Integer32):
    """Custom type mgs360024fSyslogDetailedInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Mgs360024fSyslogDetailedInfoIndex_Type.__name__ = "Integer32"
_Mgs360024fSyslogDetailedInfoIndex_Object = MibTableColumn
mgs360024fSyslogDetailedInfoIndex = _Mgs360024fSyslogDetailedInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 5, 2, 2, 1, 1),
    _Mgs360024fSyslogDetailedInfoIndex_Type()
)
mgs360024fSyslogDetailedInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fSyslogDetailedInfoIndex.setStatus("current")
_Mgs360024fSyslogDetailedInfoLevel_Type = DisplayString
_Mgs360024fSyslogDetailedInfoLevel_Object = MibTableColumn
mgs360024fSyslogDetailedInfoLevel = _Mgs360024fSyslogDetailedInfoLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 5, 2, 2, 1, 2),
    _Mgs360024fSyslogDetailedInfoLevel_Type()
)
mgs360024fSyslogDetailedInfoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSyslogDetailedInfoLevel.setStatus("current")


class _Mgs360024fSyslogDetailedInfoTime_Type(DisplayString):
    """Custom type mgs360024fSyslogDetailedInfoTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Mgs360024fSyslogDetailedInfoTime_Type.__name__ = "DisplayString"
_Mgs360024fSyslogDetailedInfoTime_Object = MibTableColumn
mgs360024fSyslogDetailedInfoTime = _Mgs360024fSyslogDetailedInfoTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 5, 2, 2, 1, 3),
    _Mgs360024fSyslogDetailedInfoTime_Type()
)
mgs360024fSyslogDetailedInfoTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSyslogDetailedInfoTime.setStatus("current")
_Mgs360024fSyslogDetailedInfoMessage_Type = DisplayString
_Mgs360024fSyslogDetailedInfoMessage_Object = MibTableColumn
mgs360024fSyslogDetailedInfoMessage = _Mgs360024fSyslogDetailedInfoMessage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 5, 2, 2, 1, 4),
    _Mgs360024fSyslogDetailedInfoMessage_Type()
)
mgs360024fSyslogDetailedInfoMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSyslogDetailedInfoMessage.setStatus("current")
_Mgs360024fSnmp_ObjectIdentity = ObjectIdentity
mgs360024fSnmp = _Mgs360024fSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6)
)
_Mgs360024fSnmpConf_ObjectIdentity = ObjectIdentity
mgs360024fSnmpConf = _Mgs360024fSnmpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1)
)
_Mgs360024fGetCommunity_Type = DisplayString
_Mgs360024fGetCommunity_Object = MibScalar
mgs360024fGetCommunity = _Mgs360024fGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1, 1),
    _Mgs360024fGetCommunity_Type()
)
mgs360024fGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fGetCommunity.setStatus("current")


class _Mgs360024fSetCommunityMode_Type(Integer32):
    """Custom type mgs360024fSetCommunityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fSetCommunityMode_Type.__name__ = "Integer32"
_Mgs360024fSetCommunityMode_Object = MibScalar
mgs360024fSetCommunityMode = _Mgs360024fSetCommunityMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1, 2),
    _Mgs360024fSetCommunityMode_Type()
)
mgs360024fSetCommunityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSetCommunityMode.setStatus("current")
_Mgs360024fSetCommunity_Type = DisplayString
_Mgs360024fSetCommunity_Object = MibScalar
mgs360024fSetCommunity = _Mgs360024fSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1, 3),
    _Mgs360024fSetCommunity_Type()
)
mgs360024fSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSetCommunity.setStatus("current")
_Mgs360024fTrapHostConfTable_Object = MibTable
mgs360024fTrapHostConfTable = _Mgs360024fTrapHostConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1, 4)
)
if mibBuilder.loadTexts:
    mgs360024fTrapHostConfTable.setStatus("current")
_Mgs360024fTrapHostConfEntry_Object = MibTableRow
mgs360024fTrapHostConfEntry = _Mgs360024fTrapHostConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1, 4, 1)
)
mgs360024fTrapHostConfEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fTrapHostConfIndex"),
)
if mibBuilder.loadTexts:
    mgs360024fTrapHostConfEntry.setStatus("current")


class _Mgs360024fTrapHostConfIndex_Type(Integer32):
    """Custom type mgs360024fTrapHostConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Mgs360024fTrapHostConfIndex_Type.__name__ = "Integer32"
_Mgs360024fTrapHostConfIndex_Object = MibTableColumn
mgs360024fTrapHostConfIndex = _Mgs360024fTrapHostConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1, 4, 1, 1),
    _Mgs360024fTrapHostConfIndex_Type()
)
mgs360024fTrapHostConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fTrapHostConfIndex.setStatus("current")


class _Mgs360024fTrapHostConfVersion_Type(Integer32):
    """Custom type mgs360024fTrapHostConfVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3),
    )


_Mgs360024fTrapHostConfVersion_Type.__name__ = "Integer32"
_Mgs360024fTrapHostConfVersion_Object = MibTableColumn
mgs360024fTrapHostConfVersion = _Mgs360024fTrapHostConfVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1, 4, 1, 2),
    _Mgs360024fTrapHostConfVersion_Type()
)
mgs360024fTrapHostConfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapHostConfVersion.setStatus("current")


class _Mgs360024fTrapHostConfIPType_Type(Integer32):
    """Custom type mgs360024fTrapHostConfIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(6, 6),
    )


_Mgs360024fTrapHostConfIPType_Type.__name__ = "Integer32"
_Mgs360024fTrapHostConfIPType_Object = MibTableColumn
mgs360024fTrapHostConfIPType = _Mgs360024fTrapHostConfIPType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1, 4, 1, 3),
    _Mgs360024fTrapHostConfIPType_Type()
)
mgs360024fTrapHostConfIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapHostConfIPType.setStatus("current")
_Mgs360024fTrapHostConfIP_Type = DisplayString
_Mgs360024fTrapHostConfIP_Object = MibTableColumn
mgs360024fTrapHostConfIP = _Mgs360024fTrapHostConfIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1, 4, 1, 4),
    _Mgs360024fTrapHostConfIP_Type()
)
mgs360024fTrapHostConfIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapHostConfIP.setStatus("current")


class _Mgs360024fTrapHostConfPort_Type(Integer32):
    """Custom type mgs360024fTrapHostConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Mgs360024fTrapHostConfPort_Type.__name__ = "Integer32"
_Mgs360024fTrapHostConfPort_Object = MibTableColumn
mgs360024fTrapHostConfPort = _Mgs360024fTrapHostConfPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1, 4, 1, 5),
    _Mgs360024fTrapHostConfPort_Type()
)
mgs360024fTrapHostConfPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapHostConfPort.setStatus("current")


class _Mgs360024fTrapHostConfCommunity_Type(DisplayString):
    """Custom type mgs360024fTrapHostConfCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Mgs360024fTrapHostConfCommunity_Type.__name__ = "DisplayString"
_Mgs360024fTrapHostConfCommunity_Object = MibTableColumn
mgs360024fTrapHostConfCommunity = _Mgs360024fTrapHostConfCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1, 4, 1, 6),
    _Mgs360024fTrapHostConfCommunity_Type()
)
mgs360024fTrapHostConfCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapHostConfCommunity.setStatus("current")


class _Mgs360024fTrapHostConfSeverityLevel_Type(Integer32):
    """Custom type mgs360024fTrapHostConfSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapHostConfSeverityLevel_Type.__name__ = "Integer32"
_Mgs360024fTrapHostConfSeverityLevel_Object = MibTableColumn
mgs360024fTrapHostConfSeverityLevel = _Mgs360024fTrapHostConfSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1, 4, 1, 7),
    _Mgs360024fTrapHostConfSeverityLevel_Type()
)
mgs360024fTrapHostConfSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapHostConfSeverityLevel.setStatus("current")


class _Mgs360024fTrapHostConfSecurityLevel_Type(Integer32):
    """Custom type mgs360024fTrapHostConfSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Mgs360024fTrapHostConfSecurityLevel_Type.__name__ = "Integer32"
_Mgs360024fTrapHostConfSecurityLevel_Object = MibTableColumn
mgs360024fTrapHostConfSecurityLevel = _Mgs360024fTrapHostConfSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1, 4, 1, 8),
    _Mgs360024fTrapHostConfSecurityLevel_Type()
)
mgs360024fTrapHostConfSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapHostConfSecurityLevel.setStatus("current")


class _Mgs360024fTrapHostConfAuthPtc_Type(Integer32):
    """Custom type mgs360024fTrapHostConfAuthPtc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Mgs360024fTrapHostConfAuthPtc_Type.__name__ = "Integer32"
_Mgs360024fTrapHostConfAuthPtc_Object = MibTableColumn
mgs360024fTrapHostConfAuthPtc = _Mgs360024fTrapHostConfAuthPtc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1, 4, 1, 9),
    _Mgs360024fTrapHostConfAuthPtc_Type()
)
mgs360024fTrapHostConfAuthPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapHostConfAuthPtc.setStatus("current")
_Mgs360024fTrapHostConfAuthPassword_Type = DisplayString
_Mgs360024fTrapHostConfAuthPassword_Object = MibTableColumn
mgs360024fTrapHostConfAuthPassword = _Mgs360024fTrapHostConfAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1, 4, 1, 10),
    _Mgs360024fTrapHostConfAuthPassword_Type()
)
mgs360024fTrapHostConfAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapHostConfAuthPassword.setStatus("current")


class _Mgs360024fTrapHostConfPrivPtc_Type(Integer32):
    """Custom type mgs360024fTrapHostConfPrivPtc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fTrapHostConfPrivPtc_Type.__name__ = "Integer32"
_Mgs360024fTrapHostConfPrivPtc_Object = MibTableColumn
mgs360024fTrapHostConfPrivPtc = _Mgs360024fTrapHostConfPrivPtc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1, 4, 1, 11),
    _Mgs360024fTrapHostConfPrivPtc_Type()
)
mgs360024fTrapHostConfPrivPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapHostConfPrivPtc.setStatus("current")
_Mgs360024fTrapHostConfPrivPassword_Type = DisplayString
_Mgs360024fTrapHostConfPrivPassword_Object = MibTableColumn
mgs360024fTrapHostConfPrivPassword = _Mgs360024fTrapHostConfPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1, 4, 1, 12),
    _Mgs360024fTrapHostConfPrivPassword_Type()
)
mgs360024fTrapHostConfPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapHostConfPrivPassword.setStatus("current")


class _Mgs360024fTrapHostConfCurrentMode_Type(Integer32):
    """Custom type mgs360024fTrapHostConfCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mgs360024fTrapHostConfCurrentMode_Type.__name__ = "Integer32"
_Mgs360024fTrapHostConfCurrentMode_Object = MibTableColumn
mgs360024fTrapHostConfCurrentMode = _Mgs360024fTrapHostConfCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 1, 6, 1, 4, 1, 13),
    _Mgs360024fTrapHostConfCurrentMode_Type()
)
mgs360024fTrapHostConfCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapHostConfCurrentMode.setStatus("current")
_Mgs360024fConfiguration_ObjectIdentity = ObjectIdentity
mgs360024fConfiguration = _Mgs360024fConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2)
)
_Mgs360024fPort_ObjectIdentity = ObjectIdentity
mgs360024fPort = _Mgs360024fPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1)
)
_Mgs360024fPortConfigurationTable_Object = MibTable
mgs360024fPortConfigurationTable = _Mgs360024fPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mgs360024fPortConfigurationTable.setStatus("current")
_Mgs360024fPortConfigurationEntry_Object = MibTableRow
mgs360024fPortConfigurationEntry = _Mgs360024fPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 1, 1)
)
mgs360024fPortConfigurationEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fPortConfPort"),
)
if mibBuilder.loadTexts:
    mgs360024fPortConfigurationEntry.setStatus("current")


class _Mgs360024fPortConfPort_Type(Integer32):
    """Custom type mgs360024fPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fPortConfPort_Type.__name__ = "Integer32"
_Mgs360024fPortConfPort_Object = MibTableColumn
mgs360024fPortConfPort = _Mgs360024fPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 1, 1, 1),
    _Mgs360024fPortConfPort_Type()
)
mgs360024fPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fPortConfPort.setStatus("current")


class _Mgs360024fPortConfPortMedia_Type(DisplayString):
    """Custom type mgs360024fPortConfPortMedia based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_Mgs360024fPortConfPortMedia_Type.__name__ = "DisplayString"
_Mgs360024fPortConfPortMedia_Object = MibTableColumn
mgs360024fPortConfPortMedia = _Mgs360024fPortConfPortMedia_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 1, 1, 2),
    _Mgs360024fPortConfPortMedia_Type()
)
mgs360024fPortConfPortMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortConfPortMedia.setStatus("current")


class _Mgs360024fPortConfLink_Type(DisplayString):
    """Custom type mgs360024fPortConfLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_Mgs360024fPortConfLink_Type.__name__ = "DisplayString"
_Mgs360024fPortConfLink_Object = MibTableColumn
mgs360024fPortConfLink = _Mgs360024fPortConfLink_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 1, 1, 3),
    _Mgs360024fPortConfLink_Type()
)
mgs360024fPortConfLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortConfLink.setStatus("current")


class _Mgs360024fPortConfCurrentSpeed_Type(DisplayString):
    """Custom type mgs360024fPortConfCurrentSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 12),
    )


_Mgs360024fPortConfCurrentSpeed_Type.__name__ = "DisplayString"
_Mgs360024fPortConfCurrentSpeed_Object = MibTableColumn
mgs360024fPortConfCurrentSpeed = _Mgs360024fPortConfCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 1, 1, 4),
    _Mgs360024fPortConfCurrentSpeed_Type()
)
mgs360024fPortConfCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortConfCurrentSpeed.setStatus("current")


class _Mgs360024fPortConfSpeed_Type(Integer32):
    """Custom type mgs360024fPortConfSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_Mgs360024fPortConfSpeed_Type.__name__ = "Integer32"
_Mgs360024fPortConfSpeed_Object = MibTableColumn
mgs360024fPortConfSpeed = _Mgs360024fPortConfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 1, 1, 5),
    _Mgs360024fPortConfSpeed_Type()
)
mgs360024fPortConfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPortConfSpeed.setStatus("current")


class _Mgs360024fPortConfCurrentFlowControlRx_Type(Integer32):
    """Custom type mgs360024fPortConfCurrentFlowControlRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fPortConfCurrentFlowControlRx_Type.__name__ = "Integer32"
_Mgs360024fPortConfCurrentFlowControlRx_Object = MibTableColumn
mgs360024fPortConfCurrentFlowControlRx = _Mgs360024fPortConfCurrentFlowControlRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 1, 1, 6),
    _Mgs360024fPortConfCurrentFlowControlRx_Type()
)
mgs360024fPortConfCurrentFlowControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortConfCurrentFlowControlRx.setStatus("current")


class _Mgs360024fPortConfCurrentFlowControlTx_Type(Integer32):
    """Custom type mgs360024fPortConfCurrentFlowControlTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fPortConfCurrentFlowControlTx_Type.__name__ = "Integer32"
_Mgs360024fPortConfCurrentFlowControlTx_Object = MibTableColumn
mgs360024fPortConfCurrentFlowControlTx = _Mgs360024fPortConfCurrentFlowControlTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 1, 1, 7),
    _Mgs360024fPortConfCurrentFlowControlTx_Type()
)
mgs360024fPortConfCurrentFlowControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortConfCurrentFlowControlTx.setStatus("current")


class _Mgs360024fPortConfFlowControl_Type(Integer32):
    """Custom type mgs360024fPortConfFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fPortConfFlowControl_Type.__name__ = "Integer32"
_Mgs360024fPortConfFlowControl_Object = MibTableColumn
mgs360024fPortConfFlowControl = _Mgs360024fPortConfFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 1, 1, 8),
    _Mgs360024fPortConfFlowControl_Type()
)
mgs360024fPortConfFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPortConfFlowControl.setStatus("current")


class _Mgs360024fPortConfMaxFrameSize_Type(Integer32):
    """Custom type mgs360024fPortConfMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_Mgs360024fPortConfMaxFrameSize_Type.__name__ = "Integer32"
_Mgs360024fPortConfMaxFrameSize_Object = MibTableColumn
mgs360024fPortConfMaxFrameSize = _Mgs360024fPortConfMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 1, 1, 9),
    _Mgs360024fPortConfMaxFrameSize_Type()
)
mgs360024fPortConfMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPortConfMaxFrameSize.setStatus("current")


class _Mgs360024fPortConfExcessiveCollisionMode_Type(Integer32):
    """Custom type mgs360024fPortConfExcessiveCollisionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fPortConfExcessiveCollisionMode_Type.__name__ = "Integer32"
_Mgs360024fPortConfExcessiveCollisionMode_Object = MibTableColumn
mgs360024fPortConfExcessiveCollisionMode = _Mgs360024fPortConfExcessiveCollisionMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 1, 1, 10),
    _Mgs360024fPortConfExcessiveCollisionMode_Type()
)
mgs360024fPortConfExcessiveCollisionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPortConfExcessiveCollisionMode.setStatus("current")


class _Mgs360024fPortConfPowerControl_Type(Integer32):
    """Custom type mgs360024fPortConfPowerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Mgs360024fPortConfPowerControl_Type.__name__ = "Integer32"
_Mgs360024fPortConfPowerControl_Object = MibTableColumn
mgs360024fPortConfPowerControl = _Mgs360024fPortConfPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 1, 1, 11),
    _Mgs360024fPortConfPowerControl_Type()
)
mgs360024fPortConfPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPortConfPowerControl.setStatus("current")
_Mgs360024fPortConfDescription_Type = DisplayString
_Mgs360024fPortConfDescription_Object = MibTableColumn
mgs360024fPortConfDescription = _Mgs360024fPortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 1, 1, 12),
    _Mgs360024fPortConfDescription_Type()
)
mgs360024fPortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPortConfDescription.setStatus("current")
_Mgs360024fPortTrafficStatisticsTable_Object = MibTable
mgs360024fPortTrafficStatisticsTable = _Mgs360024fPortTrafficStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mgs360024fPortTrafficStatisticsTable.setStatus("current")
_Mgs360024fPortTrafficStatisticsEntry_Object = MibTableRow
mgs360024fPortTrafficStatisticsEntry = _Mgs360024fPortTrafficStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1)
)
mgs360024fPortTrafficStatisticsEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fPortTrafficStatisticsPort"),
)
if mibBuilder.loadTexts:
    mgs360024fPortTrafficStatisticsEntry.setStatus("current")


class _Mgs360024fPortTrafficStatisticsPort_Type(Integer32):
    """Custom type mgs360024fPortTrafficStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fPortTrafficStatisticsPort_Type.__name__ = "Integer32"
_Mgs360024fPortTrafficStatisticsPort_Object = MibTableColumn
mgs360024fPortTrafficStatisticsPort = _Mgs360024fPortTrafficStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 1),
    _Mgs360024fPortTrafficStatisticsPort_Type()
)
mgs360024fPortTrafficStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficStatisticsPort.setStatus("current")


class _Mgs360024fPortTrafficStatisticsClear_Type(Integer32):
    """Custom type mgs360024fPortTrafficStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fPortTrafficStatisticsClear_Type.__name__ = "Integer32"
_Mgs360024fPortTrafficStatisticsClear_Object = MibTableColumn
mgs360024fPortTrafficStatisticsClear = _Mgs360024fPortTrafficStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 2),
    _Mgs360024fPortTrafficStatisticsClear_Type()
)
mgs360024fPortTrafficStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficStatisticsClear.setStatus("current")
_Mgs360024fPortTrafficRxPackets_Type = Counter64
_Mgs360024fPortTrafficRxPackets_Object = MibTableColumn
mgs360024fPortTrafficRxPackets = _Mgs360024fPortTrafficRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 3),
    _Mgs360024fPortTrafficRxPackets_Type()
)
mgs360024fPortTrafficRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxPackets.setStatus("current")
_Mgs360024fPortTrafficRxOctets_Type = Counter64
_Mgs360024fPortTrafficRxOctets_Object = MibTableColumn
mgs360024fPortTrafficRxOctets = _Mgs360024fPortTrafficRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 4),
    _Mgs360024fPortTrafficRxOctets_Type()
)
mgs360024fPortTrafficRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxOctets.setStatus("current")
_Mgs360024fPortTrafficRxUnicast_Type = Counter64
_Mgs360024fPortTrafficRxUnicast_Object = MibTableColumn
mgs360024fPortTrafficRxUnicast = _Mgs360024fPortTrafficRxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 5),
    _Mgs360024fPortTrafficRxUnicast_Type()
)
mgs360024fPortTrafficRxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxUnicast.setStatus("current")
_Mgs360024fPortTrafficRxMulticast_Type = Counter64
_Mgs360024fPortTrafficRxMulticast_Object = MibTableColumn
mgs360024fPortTrafficRxMulticast = _Mgs360024fPortTrafficRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 6),
    _Mgs360024fPortTrafficRxMulticast_Type()
)
mgs360024fPortTrafficRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxMulticast.setStatus("current")
_Mgs360024fPortTrafficRxBroadcast_Type = Counter64
_Mgs360024fPortTrafficRxBroadcast_Object = MibTableColumn
mgs360024fPortTrafficRxBroadcast = _Mgs360024fPortTrafficRxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 7),
    _Mgs360024fPortTrafficRxBroadcast_Type()
)
mgs360024fPortTrafficRxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxBroadcast.setStatus("current")
_Mgs360024fPortTrafficRxPause_Type = Counter64
_Mgs360024fPortTrafficRxPause_Object = MibTableColumn
mgs360024fPortTrafficRxPause = _Mgs360024fPortTrafficRxPause_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 8),
    _Mgs360024fPortTrafficRxPause_Type()
)
mgs360024fPortTrafficRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxPause.setStatus("current")
_Mgs360024fPortTrafficRx64Bytes_Type = Counter64
_Mgs360024fPortTrafficRx64Bytes_Object = MibTableColumn
mgs360024fPortTrafficRx64Bytes = _Mgs360024fPortTrafficRx64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 9),
    _Mgs360024fPortTrafficRx64Bytes_Type()
)
mgs360024fPortTrafficRx64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRx64Bytes.setStatus("current")
_Mgs360024fPortTrafficRx65to127Bytes_Type = Counter64
_Mgs360024fPortTrafficRx65to127Bytes_Object = MibTableColumn
mgs360024fPortTrafficRx65to127Bytes = _Mgs360024fPortTrafficRx65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 10),
    _Mgs360024fPortTrafficRx65to127Bytes_Type()
)
mgs360024fPortTrafficRx65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRx65to127Bytes.setStatus("current")
_Mgs360024fPortTrafficRx128to255Bytes_Type = Counter64
_Mgs360024fPortTrafficRx128to255Bytes_Object = MibTableColumn
mgs360024fPortTrafficRx128to255Bytes = _Mgs360024fPortTrafficRx128to255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 11),
    _Mgs360024fPortTrafficRx128to255Bytes_Type()
)
mgs360024fPortTrafficRx128to255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRx128to255Bytes.setStatus("current")
_Mgs360024fPortTrafficRx256to511Bytes_Type = Counter64
_Mgs360024fPortTrafficRx256to511Bytes_Object = MibTableColumn
mgs360024fPortTrafficRx256to511Bytes = _Mgs360024fPortTrafficRx256to511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 12),
    _Mgs360024fPortTrafficRx256to511Bytes_Type()
)
mgs360024fPortTrafficRx256to511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRx256to511Bytes.setStatus("current")
_Mgs360024fPortTrafficRx512to1023Bytes_Type = Counter64
_Mgs360024fPortTrafficRx512to1023Bytes_Object = MibTableColumn
mgs360024fPortTrafficRx512to1023Bytes = _Mgs360024fPortTrafficRx512to1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 13),
    _Mgs360024fPortTrafficRx512to1023Bytes_Type()
)
mgs360024fPortTrafficRx512to1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRx512to1023Bytes.setStatus("current")
_Mgs360024fPortTrafficRx1024to1526Bytes_Type = Counter64
_Mgs360024fPortTrafficRx1024to1526Bytes_Object = MibTableColumn
mgs360024fPortTrafficRx1024to1526Bytes = _Mgs360024fPortTrafficRx1024to1526Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 14),
    _Mgs360024fPortTrafficRx1024to1526Bytes_Type()
)
mgs360024fPortTrafficRx1024to1526Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRx1024to1526Bytes.setStatus("current")
_Mgs360024fPortTrafficRxExceecd1527Bytes_Type = Counter64
_Mgs360024fPortTrafficRxExceecd1527Bytes_Object = MibTableColumn
mgs360024fPortTrafficRxExceecd1527Bytes = _Mgs360024fPortTrafficRxExceecd1527Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 15),
    _Mgs360024fPortTrafficRxExceecd1527Bytes_Type()
)
mgs360024fPortTrafficRxExceecd1527Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxExceecd1527Bytes.setStatus("current")
_Mgs360024fPortTrafficRxQ0_Type = Counter64
_Mgs360024fPortTrafficRxQ0_Object = MibTableColumn
mgs360024fPortTrafficRxQ0 = _Mgs360024fPortTrafficRxQ0_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 16),
    _Mgs360024fPortTrafficRxQ0_Type()
)
mgs360024fPortTrafficRxQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxQ0.setStatus("current")
_Mgs360024fPortTrafficRxQ1_Type = Counter64
_Mgs360024fPortTrafficRxQ1_Object = MibTableColumn
mgs360024fPortTrafficRxQ1 = _Mgs360024fPortTrafficRxQ1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 17),
    _Mgs360024fPortTrafficRxQ1_Type()
)
mgs360024fPortTrafficRxQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxQ1.setStatus("current")
_Mgs360024fPortTrafficRxQ2_Type = Counter64
_Mgs360024fPortTrafficRxQ2_Object = MibTableColumn
mgs360024fPortTrafficRxQ2 = _Mgs360024fPortTrafficRxQ2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 18),
    _Mgs360024fPortTrafficRxQ2_Type()
)
mgs360024fPortTrafficRxQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxQ2.setStatus("current")
_Mgs360024fPortTrafficRxQ3_Type = Counter64
_Mgs360024fPortTrafficRxQ3_Object = MibTableColumn
mgs360024fPortTrafficRxQ3 = _Mgs360024fPortTrafficRxQ3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 19),
    _Mgs360024fPortTrafficRxQ3_Type()
)
mgs360024fPortTrafficRxQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxQ3.setStatus("current")
_Mgs360024fPortTrafficRxQ4_Type = Counter64
_Mgs360024fPortTrafficRxQ4_Object = MibTableColumn
mgs360024fPortTrafficRxQ4 = _Mgs360024fPortTrafficRxQ4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 20),
    _Mgs360024fPortTrafficRxQ4_Type()
)
mgs360024fPortTrafficRxQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxQ4.setStatus("current")
_Mgs360024fPortTrafficRxQ5_Type = Counter64
_Mgs360024fPortTrafficRxQ5_Object = MibTableColumn
mgs360024fPortTrafficRxQ5 = _Mgs360024fPortTrafficRxQ5_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 21),
    _Mgs360024fPortTrafficRxQ5_Type()
)
mgs360024fPortTrafficRxQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxQ5.setStatus("current")
_Mgs360024fPortTrafficRxQ6_Type = Counter64
_Mgs360024fPortTrafficRxQ6_Object = MibTableColumn
mgs360024fPortTrafficRxQ6 = _Mgs360024fPortTrafficRxQ6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 22),
    _Mgs360024fPortTrafficRxQ6_Type()
)
mgs360024fPortTrafficRxQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxQ6.setStatus("current")
_Mgs360024fPortTrafficRxQ7_Type = Counter64
_Mgs360024fPortTrafficRxQ7_Object = MibTableColumn
mgs360024fPortTrafficRxQ7 = _Mgs360024fPortTrafficRxQ7_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 23),
    _Mgs360024fPortTrafficRxQ7_Type()
)
mgs360024fPortTrafficRxQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxQ7.setStatus("current")
_Mgs360024fPortTrafficRxDrops_Type = Counter64
_Mgs360024fPortTrafficRxDrops_Object = MibTableColumn
mgs360024fPortTrafficRxDrops = _Mgs360024fPortTrafficRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 24),
    _Mgs360024fPortTrafficRxDrops_Type()
)
mgs360024fPortTrafficRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxDrops.setStatus("current")
_Mgs360024fPortTrafficRxCRCorAlignment_Type = Counter64
_Mgs360024fPortTrafficRxCRCorAlignment_Object = MibTableColumn
mgs360024fPortTrafficRxCRCorAlignment = _Mgs360024fPortTrafficRxCRCorAlignment_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 25),
    _Mgs360024fPortTrafficRxCRCorAlignment_Type()
)
mgs360024fPortTrafficRxCRCorAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxCRCorAlignment.setStatus("current")
_Mgs360024fPortTrafficRxUndersize_Type = Counter64
_Mgs360024fPortTrafficRxUndersize_Object = MibTableColumn
mgs360024fPortTrafficRxUndersize = _Mgs360024fPortTrafficRxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 26),
    _Mgs360024fPortTrafficRxUndersize_Type()
)
mgs360024fPortTrafficRxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxUndersize.setStatus("current")
_Mgs360024fPortTrafficRxOversize_Type = Counter64
_Mgs360024fPortTrafficRxOversize_Object = MibTableColumn
mgs360024fPortTrafficRxOversize = _Mgs360024fPortTrafficRxOversize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 27),
    _Mgs360024fPortTrafficRxOversize_Type()
)
mgs360024fPortTrafficRxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxOversize.setStatus("current")
_Mgs360024fPortTrafficRxFragments_Type = Counter64
_Mgs360024fPortTrafficRxFragments_Object = MibTableColumn
mgs360024fPortTrafficRxFragments = _Mgs360024fPortTrafficRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 28),
    _Mgs360024fPortTrafficRxFragments_Type()
)
mgs360024fPortTrafficRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxFragments.setStatus("current")
_Mgs360024fPortTrafficRxJabber_Type = Counter64
_Mgs360024fPortTrafficRxJabber_Object = MibTableColumn
mgs360024fPortTrafficRxJabber = _Mgs360024fPortTrafficRxJabber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 29),
    _Mgs360024fPortTrafficRxJabber_Type()
)
mgs360024fPortTrafficRxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxJabber.setStatus("current")
_Mgs360024fPortTrafficRxFiltered_Type = Counter64
_Mgs360024fPortTrafficRxFiltered_Object = MibTableColumn
mgs360024fPortTrafficRxFiltered = _Mgs360024fPortTrafficRxFiltered_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 30),
    _Mgs360024fPortTrafficRxFiltered_Type()
)
mgs360024fPortTrafficRxFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficRxFiltered.setStatus("current")
_Mgs360024fPortTrafficTxPackets_Type = Counter64
_Mgs360024fPortTrafficTxPackets_Object = MibTableColumn
mgs360024fPortTrafficTxPackets = _Mgs360024fPortTrafficTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 31),
    _Mgs360024fPortTrafficTxPackets_Type()
)
mgs360024fPortTrafficTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTxPackets.setStatus("current")
_Mgs360024fPortTrafficTxOctets_Type = Counter64
_Mgs360024fPortTrafficTxOctets_Object = MibTableColumn
mgs360024fPortTrafficTxOctets = _Mgs360024fPortTrafficTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 32),
    _Mgs360024fPortTrafficTxOctets_Type()
)
mgs360024fPortTrafficTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTxOctets.setStatus("current")
_Mgs360024fPortTrafficTxUnicast_Type = Counter64
_Mgs360024fPortTrafficTxUnicast_Object = MibTableColumn
mgs360024fPortTrafficTxUnicast = _Mgs360024fPortTrafficTxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 33),
    _Mgs360024fPortTrafficTxUnicast_Type()
)
mgs360024fPortTrafficTxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTxUnicast.setStatus("current")
_Mgs360024fPortTrafficTxMulticast_Type = Counter64
_Mgs360024fPortTrafficTxMulticast_Object = MibTableColumn
mgs360024fPortTrafficTxMulticast = _Mgs360024fPortTrafficTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 34),
    _Mgs360024fPortTrafficTxMulticast_Type()
)
mgs360024fPortTrafficTxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTxMulticast.setStatus("current")
_Mgs360024fPortTrafficTxBroadcast_Type = Counter64
_Mgs360024fPortTrafficTxBroadcast_Object = MibTableColumn
mgs360024fPortTrafficTxBroadcast = _Mgs360024fPortTrafficTxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 35),
    _Mgs360024fPortTrafficTxBroadcast_Type()
)
mgs360024fPortTrafficTxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTxBroadcast.setStatus("current")
_Mgs360024fPortTrafficTxPause_Type = Counter64
_Mgs360024fPortTrafficTxPause_Object = MibTableColumn
mgs360024fPortTrafficTxPause = _Mgs360024fPortTrafficTxPause_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 36),
    _Mgs360024fPortTrafficTxPause_Type()
)
mgs360024fPortTrafficTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTxPause.setStatus("current")
_Mgs360024fPortTrafficTx64Bytes_Type = Counter64
_Mgs360024fPortTrafficTx64Bytes_Object = MibTableColumn
mgs360024fPortTrafficTx64Bytes = _Mgs360024fPortTrafficTx64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 37),
    _Mgs360024fPortTrafficTx64Bytes_Type()
)
mgs360024fPortTrafficTx64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTx64Bytes.setStatus("current")
_Mgs360024fPortTrafficTx65to127Bytes_Type = Counter64
_Mgs360024fPortTrafficTx65to127Bytes_Object = MibTableColumn
mgs360024fPortTrafficTx65to127Bytes = _Mgs360024fPortTrafficTx65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 38),
    _Mgs360024fPortTrafficTx65to127Bytes_Type()
)
mgs360024fPortTrafficTx65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTx65to127Bytes.setStatus("current")
_Mgs360024fPortTrafficTx128to255Bytes_Type = Counter64
_Mgs360024fPortTrafficTx128to255Bytes_Object = MibTableColumn
mgs360024fPortTrafficTx128to255Bytes = _Mgs360024fPortTrafficTx128to255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 39),
    _Mgs360024fPortTrafficTx128to255Bytes_Type()
)
mgs360024fPortTrafficTx128to255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTx128to255Bytes.setStatus("current")
_Mgs360024fPortTrafficTx256to511Bytes_Type = Counter64
_Mgs360024fPortTrafficTx256to511Bytes_Object = MibTableColumn
mgs360024fPortTrafficTx256to511Bytes = _Mgs360024fPortTrafficTx256to511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 40),
    _Mgs360024fPortTrafficTx256to511Bytes_Type()
)
mgs360024fPortTrafficTx256to511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTx256to511Bytes.setStatus("current")
_Mgs360024fPortTrafficTx512to1023Bytes_Type = Counter64
_Mgs360024fPortTrafficTx512to1023Bytes_Object = MibTableColumn
mgs360024fPortTrafficTx512to1023Bytes = _Mgs360024fPortTrafficTx512to1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 41),
    _Mgs360024fPortTrafficTx512to1023Bytes_Type()
)
mgs360024fPortTrafficTx512to1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTx512to1023Bytes.setStatus("current")
_Mgs360024fPortTrafficTx1024to1526Bytes_Type = Counter64
_Mgs360024fPortTrafficTx1024to1526Bytes_Object = MibTableColumn
mgs360024fPortTrafficTx1024to1526Bytes = _Mgs360024fPortTrafficTx1024to1526Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 42),
    _Mgs360024fPortTrafficTx1024to1526Bytes_Type()
)
mgs360024fPortTrafficTx1024to1526Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTx1024to1526Bytes.setStatus("current")
_Mgs360024fPortTrafficTxExceecd1527Bytes_Type = Counter64
_Mgs360024fPortTrafficTxExceecd1527Bytes_Object = MibTableColumn
mgs360024fPortTrafficTxExceecd1527Bytes = _Mgs360024fPortTrafficTxExceecd1527Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 43),
    _Mgs360024fPortTrafficTxExceecd1527Bytes_Type()
)
mgs360024fPortTrafficTxExceecd1527Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTxExceecd1527Bytes.setStatus("current")
_Mgs360024fPortTrafficTxQ0_Type = Counter64
_Mgs360024fPortTrafficTxQ0_Object = MibTableColumn
mgs360024fPortTrafficTxQ0 = _Mgs360024fPortTrafficTxQ0_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 44),
    _Mgs360024fPortTrafficTxQ0_Type()
)
mgs360024fPortTrafficTxQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTxQ0.setStatus("current")
_Mgs360024fPortTrafficTxQ1_Type = Counter64
_Mgs360024fPortTrafficTxQ1_Object = MibTableColumn
mgs360024fPortTrafficTxQ1 = _Mgs360024fPortTrafficTxQ1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 45),
    _Mgs360024fPortTrafficTxQ1_Type()
)
mgs360024fPortTrafficTxQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTxQ1.setStatus("current")
_Mgs360024fPortTrafficTxQ2_Type = Counter64
_Mgs360024fPortTrafficTxQ2_Object = MibTableColumn
mgs360024fPortTrafficTxQ2 = _Mgs360024fPortTrafficTxQ2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 46),
    _Mgs360024fPortTrafficTxQ2_Type()
)
mgs360024fPortTrafficTxQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTxQ2.setStatus("current")
_Mgs360024fPortTrafficTxQ3_Type = Counter64
_Mgs360024fPortTrafficTxQ3_Object = MibTableColumn
mgs360024fPortTrafficTxQ3 = _Mgs360024fPortTrafficTxQ3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 47),
    _Mgs360024fPortTrafficTxQ3_Type()
)
mgs360024fPortTrafficTxQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTxQ3.setStatus("current")
_Mgs360024fPortTrafficTxQ4_Type = Counter64
_Mgs360024fPortTrafficTxQ4_Object = MibTableColumn
mgs360024fPortTrafficTxQ4 = _Mgs360024fPortTrafficTxQ4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 48),
    _Mgs360024fPortTrafficTxQ4_Type()
)
mgs360024fPortTrafficTxQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTxQ4.setStatus("current")
_Mgs360024fPortTrafficTxQ5_Type = Counter64
_Mgs360024fPortTrafficTxQ5_Object = MibTableColumn
mgs360024fPortTrafficTxQ5 = _Mgs360024fPortTrafficTxQ5_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 49),
    _Mgs360024fPortTrafficTxQ5_Type()
)
mgs360024fPortTrafficTxQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTxQ5.setStatus("current")
_Mgs360024fPortTrafficTxQ6_Type = Counter64
_Mgs360024fPortTrafficTxQ6_Object = MibTableColumn
mgs360024fPortTrafficTxQ6 = _Mgs360024fPortTrafficTxQ6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 50),
    _Mgs360024fPortTrafficTxQ6_Type()
)
mgs360024fPortTrafficTxQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTxQ6.setStatus("current")
_Mgs360024fPortTrafficTxQ7_Type = Counter64
_Mgs360024fPortTrafficTxQ7_Object = MibTableColumn
mgs360024fPortTrafficTxQ7 = _Mgs360024fPortTrafficTxQ7_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 51),
    _Mgs360024fPortTrafficTxQ7_Type()
)
mgs360024fPortTrafficTxQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTxQ7.setStatus("current")
_Mgs360024fPortTrafficTxDrops_Type = Counter64
_Mgs360024fPortTrafficTxDrops_Object = MibTableColumn
mgs360024fPortTrafficTxDrops = _Mgs360024fPortTrafficTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 52),
    _Mgs360024fPortTrafficTxDrops_Type()
)
mgs360024fPortTrafficTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTxDrops.setStatus("current")
_Mgs360024fPortTrafficTxLateOrExcColl_Type = Counter64
_Mgs360024fPortTrafficTxLateOrExcColl_Object = MibTableColumn
mgs360024fPortTrafficTxLateOrExcColl = _Mgs360024fPortTrafficTxLateOrExcColl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 2, 1, 53),
    _Mgs360024fPortTrafficTxLateOrExcColl_Type()
)
mgs360024fPortTrafficTxLateOrExcColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortTrafficTxLateOrExcColl.setStatus("current")
_Mgs360024fPortQoSStatistics_ObjectIdentity = ObjectIdentity
mgs360024fPortQoSStatistics = _Mgs360024fPortQoSStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3)
)


class _Mgs360024fPortQoSStatisticsClear_Type(Integer32):
    """Custom type mgs360024fPortQoSStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fPortQoSStatisticsClear_Type.__name__ = "Integer32"
_Mgs360024fPortQoSStatisticsClear_Object = MibScalar
mgs360024fPortQoSStatisticsClear = _Mgs360024fPortQoSStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 1),
    _Mgs360024fPortQoSStatisticsClear_Type()
)
mgs360024fPortQoSStatisticsClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortQoSStatisticsClear.setStatus("current")
_Mgs360024fPortQoSStatisticsTable_Object = MibTable
mgs360024fPortQoSStatisticsTable = _Mgs360024fPortQoSStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    mgs360024fPortQoSStatisticsTable.setStatus("current")
_Mgs360024fPortQoSStatisticsEntry_Object = MibTableRow
mgs360024fPortQoSStatisticsEntry = _Mgs360024fPortQoSStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2, 1)
)
mgs360024fPortQoSStatisticsEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fPortQoSStatisticsPort"),
)
if mibBuilder.loadTexts:
    mgs360024fPortQoSStatisticsEntry.setStatus("current")


class _Mgs360024fPortQoSStatisticsPort_Type(Integer32):
    """Custom type mgs360024fPortQoSStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fPortQoSStatisticsPort_Type.__name__ = "Integer32"
_Mgs360024fPortQoSStatisticsPort_Object = MibTableColumn
mgs360024fPortQoSStatisticsPort = _Mgs360024fPortQoSStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2, 1, 1),
    _Mgs360024fPortQoSStatisticsPort_Type()
)
mgs360024fPortQoSStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fPortQoSStatisticsPort.setStatus("current")
_Mgs360024fPortQoSQ0Rx_Type = Counter64
_Mgs360024fPortQoSQ0Rx_Object = MibTableColumn
mgs360024fPortQoSQ0Rx = _Mgs360024fPortQoSQ0Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2, 1, 2),
    _Mgs360024fPortQoSQ0Rx_Type()
)
mgs360024fPortQoSQ0Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortQoSQ0Rx.setStatus("current")
_Mgs360024fPortQoSQ0Tx_Type = Counter64
_Mgs360024fPortQoSQ0Tx_Object = MibTableColumn
mgs360024fPortQoSQ0Tx = _Mgs360024fPortQoSQ0Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2, 1, 3),
    _Mgs360024fPortQoSQ0Tx_Type()
)
mgs360024fPortQoSQ0Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortQoSQ0Tx.setStatus("current")
_Mgs360024fPortQoSQ1Rx_Type = Counter64
_Mgs360024fPortQoSQ1Rx_Object = MibTableColumn
mgs360024fPortQoSQ1Rx = _Mgs360024fPortQoSQ1Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2, 1, 4),
    _Mgs360024fPortQoSQ1Rx_Type()
)
mgs360024fPortQoSQ1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortQoSQ1Rx.setStatus("current")
_Mgs360024fPortQoSQ1Tx_Type = Counter64
_Mgs360024fPortQoSQ1Tx_Object = MibTableColumn
mgs360024fPortQoSQ1Tx = _Mgs360024fPortQoSQ1Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2, 1, 5),
    _Mgs360024fPortQoSQ1Tx_Type()
)
mgs360024fPortQoSQ1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortQoSQ1Tx.setStatus("current")
_Mgs360024fPortQoSQ2Rx_Type = Counter64
_Mgs360024fPortQoSQ2Rx_Object = MibTableColumn
mgs360024fPortQoSQ2Rx = _Mgs360024fPortQoSQ2Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2, 1, 6),
    _Mgs360024fPortQoSQ2Rx_Type()
)
mgs360024fPortQoSQ2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortQoSQ2Rx.setStatus("current")
_Mgs360024fPortQoSQ2Tx_Type = Counter64
_Mgs360024fPortQoSQ2Tx_Object = MibTableColumn
mgs360024fPortQoSQ2Tx = _Mgs360024fPortQoSQ2Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2, 1, 7),
    _Mgs360024fPortQoSQ2Tx_Type()
)
mgs360024fPortQoSQ2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortQoSQ2Tx.setStatus("current")
_Mgs360024fPortQoSQ3Rx_Type = Counter64
_Mgs360024fPortQoSQ3Rx_Object = MibTableColumn
mgs360024fPortQoSQ3Rx = _Mgs360024fPortQoSQ3Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2, 1, 8),
    _Mgs360024fPortQoSQ3Rx_Type()
)
mgs360024fPortQoSQ3Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortQoSQ3Rx.setStatus("current")
_Mgs360024fPortQoSQ3Tx_Type = Counter64
_Mgs360024fPortQoSQ3Tx_Object = MibTableColumn
mgs360024fPortQoSQ3Tx = _Mgs360024fPortQoSQ3Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2, 1, 9),
    _Mgs360024fPortQoSQ3Tx_Type()
)
mgs360024fPortQoSQ3Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortQoSQ3Tx.setStatus("current")
_Mgs360024fPortQoSQ4Rx_Type = Counter64
_Mgs360024fPortQoSQ4Rx_Object = MibTableColumn
mgs360024fPortQoSQ4Rx = _Mgs360024fPortQoSQ4Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2, 1, 10),
    _Mgs360024fPortQoSQ4Rx_Type()
)
mgs360024fPortQoSQ4Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortQoSQ4Rx.setStatus("current")
_Mgs360024fPortQoSQ4Tx_Type = Counter64
_Mgs360024fPortQoSQ4Tx_Object = MibTableColumn
mgs360024fPortQoSQ4Tx = _Mgs360024fPortQoSQ4Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2, 1, 11),
    _Mgs360024fPortQoSQ4Tx_Type()
)
mgs360024fPortQoSQ4Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortQoSQ4Tx.setStatus("current")
_Mgs360024fPortQoSQ5Rx_Type = Counter64
_Mgs360024fPortQoSQ5Rx_Object = MibTableColumn
mgs360024fPortQoSQ5Rx = _Mgs360024fPortQoSQ5Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2, 1, 12),
    _Mgs360024fPortQoSQ5Rx_Type()
)
mgs360024fPortQoSQ5Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortQoSQ5Rx.setStatus("current")
_Mgs360024fPortQoSQ5Tx_Type = Counter64
_Mgs360024fPortQoSQ5Tx_Object = MibTableColumn
mgs360024fPortQoSQ5Tx = _Mgs360024fPortQoSQ5Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2, 1, 13),
    _Mgs360024fPortQoSQ5Tx_Type()
)
mgs360024fPortQoSQ5Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortQoSQ5Tx.setStatus("current")
_Mgs360024fPortQoSQ6Rx_Type = Counter64
_Mgs360024fPortQoSQ6Rx_Object = MibTableColumn
mgs360024fPortQoSQ6Rx = _Mgs360024fPortQoSQ6Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2, 1, 14),
    _Mgs360024fPortQoSQ6Rx_Type()
)
mgs360024fPortQoSQ6Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortQoSQ6Rx.setStatus("current")
_Mgs360024fPortQoSQ6Tx_Type = Counter64
_Mgs360024fPortQoSQ6Tx_Object = MibTableColumn
mgs360024fPortQoSQ6Tx = _Mgs360024fPortQoSQ6Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2, 1, 15),
    _Mgs360024fPortQoSQ6Tx_Type()
)
mgs360024fPortQoSQ6Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortQoSQ6Tx.setStatus("current")
_Mgs360024fPortQoSQ7Rx_Type = Counter64
_Mgs360024fPortQoSQ7Rx_Object = MibTableColumn
mgs360024fPortQoSQ7Rx = _Mgs360024fPortQoSQ7Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2, 1, 16),
    _Mgs360024fPortQoSQ7Rx_Type()
)
mgs360024fPortQoSQ7Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortQoSQ7Rx.setStatus("current")
_Mgs360024fPortQoSQ7Tx_Type = Counter64
_Mgs360024fPortQoSQ7Tx_Object = MibTableColumn
mgs360024fPortQoSQ7Tx = _Mgs360024fPortQoSQ7Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 3, 2, 1, 17),
    _Mgs360024fPortQoSQ7Tx_Type()
)
mgs360024fPortQoSQ7Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortQoSQ7Tx.setStatus("current")
_Mgs360024fSFPInfoTable_Object = MibTable
mgs360024fSFPInfoTable = _Mgs360024fSFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4)
)
if mibBuilder.loadTexts:
    mgs360024fSFPInfoTable.setStatus("current")
_Mgs360024fSFPInfoEntry_Object = MibTableRow
mgs360024fSFPInfoEntry = _Mgs360024fSFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4, 1)
)
mgs360024fSFPInfoEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fSFPInfoIndex"),
)
if mibBuilder.loadTexts:
    mgs360024fSFPInfoEntry.setStatus("current")


class _Mgs360024fSFPInfoIndex_Type(Integer32):
    """Custom type mgs360024fSFPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fSFPInfoIndex_Type.__name__ = "Integer32"
_Mgs360024fSFPInfoIndex_Object = MibTableColumn
mgs360024fSFPInfoIndex = _Mgs360024fSFPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4, 1, 1),
    _Mgs360024fSFPInfoIndex_Type()
)
mgs360024fSFPInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fSFPInfoIndex.setStatus("current")
_Mgs360024fSFPInfoPort_Type = DisplayString
_Mgs360024fSFPInfoPort_Object = MibTableColumn
mgs360024fSFPInfoPort = _Mgs360024fSFPInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4, 1, 2),
    _Mgs360024fSFPInfoPort_Type()
)
mgs360024fSFPInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSFPInfoPort.setStatus("current")
_Mgs360024fSFPConnectorType_Type = DisplayString
_Mgs360024fSFPConnectorType_Object = MibTableColumn
mgs360024fSFPConnectorType = _Mgs360024fSFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4, 1, 3),
    _Mgs360024fSFPConnectorType_Type()
)
mgs360024fSFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSFPConnectorType.setStatus("current")
_Mgs360024fSFPFiberType_Type = DisplayString
_Mgs360024fSFPFiberType_Object = MibTableColumn
mgs360024fSFPFiberType = _Mgs360024fSFPFiberType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4, 1, 4),
    _Mgs360024fSFPFiberType_Type()
)
mgs360024fSFPFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSFPFiberType.setStatus("current")
_Mgs360024fSFPTxCentralWavelength_Type = DisplayString
_Mgs360024fSFPTxCentralWavelength_Object = MibTableColumn
mgs360024fSFPTxCentralWavelength = _Mgs360024fSFPTxCentralWavelength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4, 1, 5),
    _Mgs360024fSFPTxCentralWavelength_Type()
)
mgs360024fSFPTxCentralWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSFPTxCentralWavelength.setStatus("current")
_Mgs360024fSFPBaudRate_Type = DisplayString
_Mgs360024fSFPBaudRate_Object = MibTableColumn
mgs360024fSFPBaudRate = _Mgs360024fSFPBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4, 1, 6),
    _Mgs360024fSFPBaudRate_Type()
)
mgs360024fSFPBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSFPBaudRate.setStatus("current")
_Mgs360024fSFPVendorOUI_Type = DisplayString
_Mgs360024fSFPVendorOUI_Object = MibTableColumn
mgs360024fSFPVendorOUI = _Mgs360024fSFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4, 1, 7),
    _Mgs360024fSFPVendorOUI_Type()
)
mgs360024fSFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSFPVendorOUI.setStatus("current")
_Mgs360024fSFPVendorName_Type = DisplayString
_Mgs360024fSFPVendorName_Object = MibTableColumn
mgs360024fSFPVendorName = _Mgs360024fSFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4, 1, 8),
    _Mgs360024fSFPVendorName_Type()
)
mgs360024fSFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSFPVendorName.setStatus("current")
_Mgs360024fSFPVendorPN_Type = DisplayString
_Mgs360024fSFPVendorPN_Object = MibTableColumn
mgs360024fSFPVendorPN = _Mgs360024fSFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4, 1, 9),
    _Mgs360024fSFPVendorPN_Type()
)
mgs360024fSFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSFPVendorPN.setStatus("current")
_Mgs360024fSFPVendorRev_Type = DisplayString
_Mgs360024fSFPVendorRev_Object = MibTableColumn
mgs360024fSFPVendorRev = _Mgs360024fSFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4, 1, 10),
    _Mgs360024fSFPVendorRev_Type()
)
mgs360024fSFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSFPVendorRev.setStatus("current")
_Mgs360024fSFPVendorSN_Type = DisplayString
_Mgs360024fSFPVendorSN_Object = MibTableColumn
mgs360024fSFPVendorSN = _Mgs360024fSFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4, 1, 11),
    _Mgs360024fSFPVendorSN_Type()
)
mgs360024fSFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSFPVendorSN.setStatus("current")
_Mgs360024fSFPDateCode_Type = DisplayString
_Mgs360024fSFPDateCode_Object = MibTableColumn
mgs360024fSFPDateCode = _Mgs360024fSFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4, 1, 12),
    _Mgs360024fSFPDateCode_Type()
)
mgs360024fSFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSFPDateCode.setStatus("current")
_Mgs360024fSFPTemperature_Type = DisplayString
_Mgs360024fSFPTemperature_Object = MibTableColumn
mgs360024fSFPTemperature = _Mgs360024fSFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4, 1, 13),
    _Mgs360024fSFPTemperature_Type()
)
mgs360024fSFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSFPTemperature.setStatus("current")
_Mgs360024fSFPVcc_Type = DisplayString
_Mgs360024fSFPVcc_Object = MibTableColumn
mgs360024fSFPVcc = _Mgs360024fSFPVcc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4, 1, 14),
    _Mgs360024fSFPVcc_Type()
)
mgs360024fSFPVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSFPVcc.setStatus("current")
_Mgs360024fSFPMon1Bias_Type = DisplayString
_Mgs360024fSFPMon1Bias_Object = MibTableColumn
mgs360024fSFPMon1Bias = _Mgs360024fSFPMon1Bias_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4, 1, 15),
    _Mgs360024fSFPMon1Bias_Type()
)
mgs360024fSFPMon1Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSFPMon1Bias.setStatus("current")
_Mgs360024fSFPMon2TxPWR_Type = DisplayString
_Mgs360024fSFPMon2TxPWR_Object = MibTableColumn
mgs360024fSFPMon2TxPWR = _Mgs360024fSFPMon2TxPWR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4, 1, 16),
    _Mgs360024fSFPMon2TxPWR_Type()
)
mgs360024fSFPMon2TxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSFPMon2TxPWR.setStatus("current")
_Mgs360024fSFPMon3RxPWR_Type = DisplayString
_Mgs360024fSFPMon3RxPWR_Object = MibTableColumn
mgs360024fSFPMon3RxPWR = _Mgs360024fSFPMon3RxPWR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 1, 4, 1, 17),
    _Mgs360024fSFPMon3RxPWR_Type()
)
mgs360024fSFPMon3RxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSFPMon3RxPWR.setStatus("current")
_Mgs360024fGARP_ObjectIdentity = ObjectIdentity
mgs360024fGARP = _Mgs360024fGARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 3)
)
_Mgs360024fGARPConfTable_Object = MibTable
mgs360024fGARPConfTable = _Mgs360024fGARPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mgs360024fGARPConfTable.setStatus("current")
_Mgs360024fGARPConfEntry_Object = MibTableRow
mgs360024fGARPConfEntry = _Mgs360024fGARPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 3, 1, 1)
)
mgs360024fGARPConfEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fGARPConfPort"),
)
if mibBuilder.loadTexts:
    mgs360024fGARPConfEntry.setStatus("current")


class _Mgs360024fGARPConfPort_Type(Integer32):
    """Custom type mgs360024fGARPConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fGARPConfPort_Type.__name__ = "Integer32"
_Mgs360024fGARPConfPort_Object = MibTableColumn
mgs360024fGARPConfPort = _Mgs360024fGARPConfPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 3, 1, 1, 1),
    _Mgs360024fGARPConfPort_Type()
)
mgs360024fGARPConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fGARPConfPort.setStatus("current")


class _Mgs360024fGARPJoinTimer_Type(Integer32):
    """Custom type mgs360024fGARPJoinTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_Mgs360024fGARPJoinTimer_Type.__name__ = "Integer32"
_Mgs360024fGARPJoinTimer_Object = MibTableColumn
mgs360024fGARPJoinTimer = _Mgs360024fGARPJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 3, 1, 1, 2),
    _Mgs360024fGARPJoinTimer_Type()
)
mgs360024fGARPJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fGARPJoinTimer.setStatus("current")


class _Mgs360024fGARPLeaveTimer_Type(Integer32):
    """Custom type mgs360024fGARPLeaveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 3000),
    )


_Mgs360024fGARPLeaveTimer_Type.__name__ = "Integer32"
_Mgs360024fGARPLeaveTimer_Object = MibTableColumn
mgs360024fGARPLeaveTimer = _Mgs360024fGARPLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 3, 1, 1, 3),
    _Mgs360024fGARPLeaveTimer_Type()
)
mgs360024fGARPLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fGARPLeaveTimer.setStatus("current")


class _Mgs360024fGARPLeaveAllTimer_Type(Integer32):
    """Custom type mgs360024fGARPLeaveAllTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 50000),
    )


_Mgs360024fGARPLeaveAllTimer_Type.__name__ = "Integer32"
_Mgs360024fGARPLeaveAllTimer_Object = MibTableColumn
mgs360024fGARPLeaveAllTimer = _Mgs360024fGARPLeaveAllTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 3, 1, 1, 4),
    _Mgs360024fGARPLeaveAllTimer_Type()
)
mgs360024fGARPLeaveAllTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fGARPLeaveAllTimer.setStatus("current")


class _Mgs360024fGARPApplicantion_Type(Integer32):
    """Custom type mgs360024fGARPApplicantion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fGARPApplicantion_Type.__name__ = "Integer32"
_Mgs360024fGARPApplicantion_Object = MibTableColumn
mgs360024fGARPApplicantion = _Mgs360024fGARPApplicantion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 3, 1, 1, 5),
    _Mgs360024fGARPApplicantion_Type()
)
mgs360024fGARPApplicantion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fGARPApplicantion.setStatus("current")


class _Mgs360024fGARPAttributeType_Type(Integer32):
    """Custom type mgs360024fGARPAttributeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fGARPAttributeType_Type.__name__ = "Integer32"
_Mgs360024fGARPAttributeType_Object = MibTableColumn
mgs360024fGARPAttributeType = _Mgs360024fGARPAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 3, 1, 1, 6),
    _Mgs360024fGARPAttributeType_Type()
)
mgs360024fGARPAttributeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fGARPAttributeType.setStatus("current")


class _Mgs360024fGARPApplicant_Type(Integer32):
    """Custom type mgs360024fGARPApplicant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fGARPApplicant_Type.__name__ = "Integer32"
_Mgs360024fGARPApplicant_Object = MibTableColumn
mgs360024fGARPApplicant = _Mgs360024fGARPApplicant_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 3, 1, 1, 7),
    _Mgs360024fGARPApplicant_Type()
)
mgs360024fGARPApplicant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fGARPApplicant.setStatus("current")
_Mgs360024fGARPStatisticsTable_Object = MibTable
mgs360024fGARPStatisticsTable = _Mgs360024fGARPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 3, 2)
)
if mibBuilder.loadTexts:
    mgs360024fGARPStatisticsTable.setStatus("current")
_Mgs360024fGARPStatisticsEntry_Object = MibTableRow
mgs360024fGARPStatisticsEntry = _Mgs360024fGARPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 3, 2, 1)
)
mgs360024fGARPStatisticsEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fGARPStatisticsPort"),
)
if mibBuilder.loadTexts:
    mgs360024fGARPStatisticsEntry.setStatus("current")


class _Mgs360024fGARPStatisticsPort_Type(Integer32):
    """Custom type mgs360024fGARPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fGARPStatisticsPort_Type.__name__ = "Integer32"
_Mgs360024fGARPStatisticsPort_Object = MibTableColumn
mgs360024fGARPStatisticsPort = _Mgs360024fGARPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 3, 2, 1, 1),
    _Mgs360024fGARPStatisticsPort_Type()
)
mgs360024fGARPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fGARPStatisticsPort.setStatus("current")
_Mgs360024fGARPStatisticsPeerMAC_Type = DisplayString
_Mgs360024fGARPStatisticsPeerMAC_Object = MibTableColumn
mgs360024fGARPStatisticsPeerMAC = _Mgs360024fGARPStatisticsPeerMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 3, 2, 1, 2),
    _Mgs360024fGARPStatisticsPeerMAC_Type()
)
mgs360024fGARPStatisticsPeerMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fGARPStatisticsPeerMAC.setStatus("current")
_Mgs360024fGARPStatisticsFailedCount_Type = Counter32
_Mgs360024fGARPStatisticsFailedCount_Object = MibTableColumn
mgs360024fGARPStatisticsFailedCount = _Mgs360024fGARPStatisticsFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 3, 2, 1, 3),
    _Mgs360024fGARPStatisticsFailedCount_Type()
)
mgs360024fGARPStatisticsFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fGARPStatisticsFailedCount.setStatus("current")
_Mgs360024fGVRP_ObjectIdentity = ObjectIdentity
mgs360024fGVRP = _Mgs360024fGVRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 4)
)
_Mgs360024fGVRPConf_ObjectIdentity = ObjectIdentity
mgs360024fGVRPConf = _Mgs360024fGVRPConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 4, 1)
)


class _Mgs360024fGVRPMode_Type(Integer32):
    """Custom type mgs360024fGVRPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fGVRPMode_Type.__name__ = "Integer32"
_Mgs360024fGVRPMode_Object = MibScalar
mgs360024fGVRPMode = _Mgs360024fGVRPMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 4, 1, 1),
    _Mgs360024fGVRPMode_Type()
)
mgs360024fGVRPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fGVRPMode.setStatus("current")
_Mgs360024fGVRPConfTable_Object = MibTable
mgs360024fGVRPConfTable = _Mgs360024fGVRPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    mgs360024fGVRPConfTable.setStatus("current")
_Mgs360024fGVRPConfEntry_Object = MibTableRow
mgs360024fGVRPConfEntry = _Mgs360024fGVRPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 4, 1, 2, 1)
)
mgs360024fGVRPConfEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fGVRPConfPort"),
)
if mibBuilder.loadTexts:
    mgs360024fGVRPConfEntry.setStatus("current")


class _Mgs360024fGVRPConfPort_Type(Integer32):
    """Custom type mgs360024fGVRPConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fGVRPConfPort_Type.__name__ = "Integer32"
_Mgs360024fGVRPConfPort_Object = MibTableColumn
mgs360024fGVRPConfPort = _Mgs360024fGVRPConfPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 4, 1, 2, 1, 1),
    _Mgs360024fGVRPConfPort_Type()
)
mgs360024fGVRPConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fGVRPConfPort.setStatus("current")


class _Mgs360024fGVRPConfPortMode_Type(Integer32):
    """Custom type mgs360024fGVRPConfPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fGVRPConfPortMode_Type.__name__ = "Integer32"
_Mgs360024fGVRPConfPortMode_Object = MibTableColumn
mgs360024fGVRPConfPortMode = _Mgs360024fGVRPConfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 4, 1, 2, 1, 2),
    _Mgs360024fGVRPConfPortMode_Type()
)
mgs360024fGVRPConfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fGVRPConfPortMode.setStatus("current")


class _Mgs360024fGVRPConfPortRRole_Type(Integer32):
    """Custom type mgs360024fGVRPConfPortRRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fGVRPConfPortRRole_Type.__name__ = "Integer32"
_Mgs360024fGVRPConfPortRRole_Object = MibTableColumn
mgs360024fGVRPConfPortRRole = _Mgs360024fGVRPConfPortRRole_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 4, 1, 2, 1, 3),
    _Mgs360024fGVRPConfPortRRole_Type()
)
mgs360024fGVRPConfPortRRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fGVRPConfPortRRole.setStatus("current")
_Mgs360024fGVRPStatisticsTable_Object = MibTable
mgs360024fGVRPStatisticsTable = _Mgs360024fGVRPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 4, 2)
)
if mibBuilder.loadTexts:
    mgs360024fGVRPStatisticsTable.setStatus("current")
_Mgs360024fGVRPStatisticsEntry_Object = MibTableRow
mgs360024fGVRPStatisticsEntry = _Mgs360024fGVRPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 4, 2, 1)
)
mgs360024fGVRPStatisticsEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fGVRPStatisticsPort"),
)
if mibBuilder.loadTexts:
    mgs360024fGVRPStatisticsEntry.setStatus("current")


class _Mgs360024fGVRPStatisticsPort_Type(Integer32):
    """Custom type mgs360024fGVRPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fGVRPStatisticsPort_Type.__name__ = "Integer32"
_Mgs360024fGVRPStatisticsPort_Object = MibTableColumn
mgs360024fGVRPStatisticsPort = _Mgs360024fGVRPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 4, 2, 1, 1),
    _Mgs360024fGVRPStatisticsPort_Type()
)
mgs360024fGVRPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fGVRPStatisticsPort.setStatus("current")
_Mgs360024fGVRPStatisticsJoinTxCnt_Type = Counter32
_Mgs360024fGVRPStatisticsJoinTxCnt_Object = MibTableColumn
mgs360024fGVRPStatisticsJoinTxCnt = _Mgs360024fGVRPStatisticsJoinTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 4, 2, 1, 2),
    _Mgs360024fGVRPStatisticsJoinTxCnt_Type()
)
mgs360024fGVRPStatisticsJoinTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fGVRPStatisticsJoinTxCnt.setStatus("current")
_Mgs360024fGVRPStatisticsLeaveTxCnt_Type = Counter32
_Mgs360024fGVRPStatisticsLeaveTxCnt_Object = MibTableColumn
mgs360024fGVRPStatisticsLeaveTxCnt = _Mgs360024fGVRPStatisticsLeaveTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 4, 2, 1, 3),
    _Mgs360024fGVRPStatisticsLeaveTxCnt_Type()
)
mgs360024fGVRPStatisticsLeaveTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fGVRPStatisticsLeaveTxCnt.setStatus("current")
_Mgs360024fThermalProtection_ObjectIdentity = ObjectIdentity
mgs360024fThermalProtection = _Mgs360024fThermalProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 5)
)


class _Mgs360024fPriority0Temperature_Type(Integer32):
    """Custom type mgs360024fPriority0Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Mgs360024fPriority0Temperature_Type.__name__ = "Integer32"
_Mgs360024fPriority0Temperature_Object = MibScalar
mgs360024fPriority0Temperature = _Mgs360024fPriority0Temperature_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 5, 1),
    _Mgs360024fPriority0Temperature_Type()
)
mgs360024fPriority0Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPriority0Temperature.setStatus("current")


class _Mgs360024fPriority1Temperature_Type(Integer32):
    """Custom type mgs360024fPriority1Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Mgs360024fPriority1Temperature_Type.__name__ = "Integer32"
_Mgs360024fPriority1Temperature_Object = MibScalar
mgs360024fPriority1Temperature = _Mgs360024fPriority1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 5, 2),
    _Mgs360024fPriority1Temperature_Type()
)
mgs360024fPriority1Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPriority1Temperature.setStatus("current")


class _Mgs360024fPriority2Temperature_Type(Integer32):
    """Custom type mgs360024fPriority2Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Mgs360024fPriority2Temperature_Type.__name__ = "Integer32"
_Mgs360024fPriority2Temperature_Object = MibScalar
mgs360024fPriority2Temperature = _Mgs360024fPriority2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 5, 3),
    _Mgs360024fPriority2Temperature_Type()
)
mgs360024fPriority2Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPriority2Temperature.setStatus("current")


class _Mgs360024fPriority3Temperature_Type(Integer32):
    """Custom type mgs360024fPriority3Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Mgs360024fPriority3Temperature_Type.__name__ = "Integer32"
_Mgs360024fPriority3Temperature_Object = MibScalar
mgs360024fPriority3Temperature = _Mgs360024fPriority3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 5, 4),
    _Mgs360024fPriority3Temperature_Type()
)
mgs360024fPriority3Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPriority3Temperature.setStatus("current")
_Mgs360024fThermalProtectionTable_Object = MibTable
mgs360024fThermalProtectionTable = _Mgs360024fThermalProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 5, 5)
)
if mibBuilder.loadTexts:
    mgs360024fThermalProtectionTable.setStatus("current")
_Mgs360024fThermalProtectionEntry_Object = MibTableRow
mgs360024fThermalProtectionEntry = _Mgs360024fThermalProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 5, 5, 1)
)
mgs360024fThermalProtectionEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fThermalProtectionPort"),
)
if mibBuilder.loadTexts:
    mgs360024fThermalProtectionEntry.setStatus("current")


class _Mgs360024fThermalProtectionPort_Type(Integer32):
    """Custom type mgs360024fThermalProtectionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fThermalProtectionPort_Type.__name__ = "Integer32"
_Mgs360024fThermalProtectionPort_Object = MibTableColumn
mgs360024fThermalProtectionPort = _Mgs360024fThermalProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 5, 5, 1, 1),
    _Mgs360024fThermalProtectionPort_Type()
)
mgs360024fThermalProtectionPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fThermalProtectionPort.setStatus("current")


class _Mgs360024fThermalProtectionPortTemperature_Type(Integer32):
    """Custom type mgs360024fThermalProtectionPortTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Mgs360024fThermalProtectionPortTemperature_Type.__name__ = "Integer32"
_Mgs360024fThermalProtectionPortTemperature_Object = MibTableColumn
mgs360024fThermalProtectionPortTemperature = _Mgs360024fThermalProtectionPortTemperature_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 5, 5, 1, 2),
    _Mgs360024fThermalProtectionPortTemperature_Type()
)
mgs360024fThermalProtectionPortTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fThermalProtectionPortTemperature.setStatus("current")


class _Mgs360024fThermalProtectionPortPriority_Type(Integer32):
    """Custom type mgs360024fThermalProtectionPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Mgs360024fThermalProtectionPortPriority_Type.__name__ = "Integer32"
_Mgs360024fThermalProtectionPortPriority_Object = MibTableColumn
mgs360024fThermalProtectionPortPriority = _Mgs360024fThermalProtectionPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 5, 5, 1, 3),
    _Mgs360024fThermalProtectionPortPriority_Type()
)
mgs360024fThermalProtectionPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fThermalProtectionPortPriority.setStatus("current")
_Mgs360024fThermalProtectionPortStatus_Type = DisplayString
_Mgs360024fThermalProtectionPortStatus_Object = MibTableColumn
mgs360024fThermalProtectionPortStatus = _Mgs360024fThermalProtectionPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 5, 5, 1, 4),
    _Mgs360024fThermalProtectionPortStatus_Type()
)
mgs360024fThermalProtectionPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fThermalProtectionPortStatus.setStatus("current")
_Mgs360024fMirroring_ObjectIdentity = ObjectIdentity
mgs360024fMirroring = _Mgs360024fMirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 6)
)


class _Mgs360024fPortToMirrorOn_Type(Integer32):
    """Custom type mgs360024fPortToMirrorOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Mgs360024fPortToMirrorOn_Type.__name__ = "Integer32"
_Mgs360024fPortToMirrorOn_Object = MibScalar
mgs360024fPortToMirrorOn = _Mgs360024fPortToMirrorOn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 6, 1),
    _Mgs360024fPortToMirrorOn_Type()
)
mgs360024fPortToMirrorOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPortToMirrorOn.setStatus("current")
_Mgs360024fMirrorTable_Object = MibTable
mgs360024fMirrorTable = _Mgs360024fMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 6, 2)
)
if mibBuilder.loadTexts:
    mgs360024fMirrorTable.setStatus("current")
_Mgs360024fMirrorEntry_Object = MibTableRow
mgs360024fMirrorEntry = _Mgs360024fMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 6, 2, 1)
)
mgs360024fMirrorEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fMirrorPort"),
)
if mibBuilder.loadTexts:
    mgs360024fMirrorEntry.setStatus("current")


class _Mgs360024fMirrorPort_Type(Integer32):
    """Custom type mgs360024fMirrorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fMirrorPort_Type.__name__ = "Integer32"
_Mgs360024fMirrorPort_Object = MibTableColumn
mgs360024fMirrorPort = _Mgs360024fMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 6, 2, 1, 1),
    _Mgs360024fMirrorPort_Type()
)
mgs360024fMirrorPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fMirrorPort.setStatus("current")


class _Mgs360024fMirrorMode_Type(Integer32):
    """Custom type mgs360024fMirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Mgs360024fMirrorMode_Type.__name__ = "Integer32"
_Mgs360024fMirrorMode_Object = MibTableColumn
mgs360024fMirrorMode = _Mgs360024fMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 6, 2, 1, 2),
    _Mgs360024fMirrorMode_Type()
)
mgs360024fMirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMirrorMode.setStatus("current")
_Mgs360024fTrapEventSeverity_ObjectIdentity = ObjectIdentity
mgs360024fTrapEventSeverity = _Mgs360024fTrapEventSeverity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7)
)


class _Mgs360024fTrapEventSeverityACL_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityACL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityACL_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityACL_Object = MibScalar
mgs360024fTrapEventSeverityACL = _Mgs360024fTrapEventSeverityACL_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 1),
    _Mgs360024fTrapEventSeverityACL_Type()
)
mgs360024fTrapEventSeverityACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityACL.setStatus("current")


class _Mgs360024fTrapEventSeverityACLLog_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityACLLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityACLLog_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityACLLog_Object = MibScalar
mgs360024fTrapEventSeverityACLLog = _Mgs360024fTrapEventSeverityACLLog_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 2),
    _Mgs360024fTrapEventSeverityACLLog_Type()
)
mgs360024fTrapEventSeverityACLLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityACLLog.setStatus("current")


class _Mgs360024fTrapEventSeverityAccessMgmt_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityAccessMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityAccessMgmt_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityAccessMgmt_Object = MibScalar
mgs360024fTrapEventSeverityAccessMgmt = _Mgs360024fTrapEventSeverityAccessMgmt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 3),
    _Mgs360024fTrapEventSeverityAccessMgmt_Type()
)
mgs360024fTrapEventSeverityAccessMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityAccessMgmt.setStatus("current")


class _Mgs360024fTrapEventSeverityAuthFailed_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityAuthFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityAuthFailed_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityAuthFailed_Object = MibScalar
mgs360024fTrapEventSeverityAuthFailed = _Mgs360024fTrapEventSeverityAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 4),
    _Mgs360024fTrapEventSeverityAuthFailed_Type()
)
mgs360024fTrapEventSeverityAuthFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityAuthFailed.setStatus("current")


class _Mgs360024fTrapEventSeverityColdStart_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityColdStart_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityColdStart_Object = MibScalar
mgs360024fTrapEventSeverityColdStart = _Mgs360024fTrapEventSeverityColdStart_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 5),
    _Mgs360024fTrapEventSeverityColdStart_Type()
)
mgs360024fTrapEventSeverityColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityColdStart.setStatus("current")


class _Mgs360024fTrapEventSeverityConfigInfo_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityConfigInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityConfigInfo_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityConfigInfo_Object = MibScalar
mgs360024fTrapEventSeverityConfigInfo = _Mgs360024fTrapEventSeverityConfigInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 6),
    _Mgs360024fTrapEventSeverityConfigInfo_Type()
)
mgs360024fTrapEventSeverityConfigInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityConfigInfo.setStatus("current")


class _Mgs360024fTrapEventSeverityFirmwareUpgrade_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityFirmwareUpgrade_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityFirmwareUpgrade_Object = MibScalar
mgs360024fTrapEventSeverityFirmwareUpgrade = _Mgs360024fTrapEventSeverityFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 7),
    _Mgs360024fTrapEventSeverityFirmwareUpgrade_Type()
)
mgs360024fTrapEventSeverityFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityFirmwareUpgrade.setStatus("current")


class _Mgs360024fTrapEventSeverityImportExport_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityImportExport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityImportExport_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityImportExport_Object = MibScalar
mgs360024fTrapEventSeverityImportExport = _Mgs360024fTrapEventSeverityImportExport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 8),
    _Mgs360024fTrapEventSeverityImportExport_Type()
)
mgs360024fTrapEventSeverityImportExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityImportExport.setStatus("current")


class _Mgs360024fTrapEventSeverityLACP_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityLACP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityLACP_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityLACP_Object = MibScalar
mgs360024fTrapEventSeverityLACP = _Mgs360024fTrapEventSeverityLACP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 9),
    _Mgs360024fTrapEventSeverityLACP_Type()
)
mgs360024fTrapEventSeverityLACP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityLACP.setStatus("current")


class _Mgs360024fTrapEventSeverityLinkStatus_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityLinkStatus_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityLinkStatus_Object = MibScalar
mgs360024fTrapEventSeverityLinkStatus = _Mgs360024fTrapEventSeverityLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 10),
    _Mgs360024fTrapEventSeverityLinkStatus_Type()
)
mgs360024fTrapEventSeverityLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityLinkStatus.setStatus("current")


class _Mgs360024fTrapEventSeverityLogin_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityLogin_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityLogin_Object = MibScalar
mgs360024fTrapEventSeverityLogin = _Mgs360024fTrapEventSeverityLogin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 11),
    _Mgs360024fTrapEventSeverityLogin_Type()
)
mgs360024fTrapEventSeverityLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityLogin.setStatus("current")


class _Mgs360024fTrapEventSeverityLogout_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityLogout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityLogout_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityLogout_Object = MibScalar
mgs360024fTrapEventSeverityLogout = _Mgs360024fTrapEventSeverityLogout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 12),
    _Mgs360024fTrapEventSeverityLogout_Type()
)
mgs360024fTrapEventSeverityLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityLogout.setStatus("current")


class _Mgs360024fTrapEventSeverityLoopProtect_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityLoopProtect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityLoopProtect_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityLoopProtect_Object = MibScalar
mgs360024fTrapEventSeverityLoopProtect = _Mgs360024fTrapEventSeverityLoopProtect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 13),
    _Mgs360024fTrapEventSeverityLoopProtect_Type()
)
mgs360024fTrapEventSeverityLoopProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityLoopProtect.setStatus("current")


class _Mgs360024fTrapEventSeverityMgmtIPChange_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityMgmtIPChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityMgmtIPChange_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityMgmtIPChange_Object = MibScalar
mgs360024fTrapEventSeverityMgmtIPChange = _Mgs360024fTrapEventSeverityMgmtIPChange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 14),
    _Mgs360024fTrapEventSeverityMgmtIPChange_Type()
)
mgs360024fTrapEventSeverityMgmtIPChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityMgmtIPChange.setStatus("current")


class _Mgs360024fTrapEventSeverityModuleChange_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityModuleChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityModuleChange_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityModuleChange_Object = MibScalar
mgs360024fTrapEventSeverityModuleChange = _Mgs360024fTrapEventSeverityModuleChange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 15),
    _Mgs360024fTrapEventSeverityModuleChange_Type()
)
mgs360024fTrapEventSeverityModuleChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityModuleChange.setStatus("current")


class _Mgs360024fTrapEventSeverityNAS_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityNAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityNAS_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityNAS_Object = MibScalar
mgs360024fTrapEventSeverityNAS = _Mgs360024fTrapEventSeverityNAS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 16),
    _Mgs360024fTrapEventSeverityNAS_Type()
)
mgs360024fTrapEventSeverityNAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityNAS.setStatus("current")


class _Mgs360024fTrapEventSeverityPasswdChange_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityPasswdChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityPasswdChange_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityPasswdChange_Object = MibScalar
mgs360024fTrapEventSeverityPasswdChange = _Mgs360024fTrapEventSeverityPasswdChange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 17),
    _Mgs360024fTrapEventSeverityPasswdChange_Type()
)
mgs360024fTrapEventSeverityPasswdChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityPasswdChange.setStatus("current")


class _Mgs360024fTrapEventSeverityPortSecurity_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityPortSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityPortSecurity_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityPortSecurity_Object = MibScalar
mgs360024fTrapEventSeverityPortSecurity = _Mgs360024fTrapEventSeverityPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 18),
    _Mgs360024fTrapEventSeverityPortSecurity_Type()
)
mgs360024fTrapEventSeverityPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityPortSecurity.setStatus("current")


class _Mgs360024fTrapEventSeverityThermalProtect_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityThermalProtect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityThermalProtect_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityThermalProtect_Object = MibScalar
mgs360024fTrapEventSeverityThermalProtect = _Mgs360024fTrapEventSeverityThermalProtect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 19),
    _Mgs360024fTrapEventSeverityThermalProtect_Type()
)
mgs360024fTrapEventSeverityThermalProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityThermalProtect.setStatus("current")


class _Mgs360024fTrapEventSeverityVLAN_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityVLAN_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityVLAN_Object = MibScalar
mgs360024fTrapEventSeverityVLAN = _Mgs360024fTrapEventSeverityVLAN_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 20),
    _Mgs360024fTrapEventSeverityVLAN_Type()
)
mgs360024fTrapEventSeverityVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityVLAN.setStatus("current")


class _Mgs360024fTrapEventSeverityWarmStart_Type(Integer32):
    """Custom type mgs360024fTrapEventSeverityWarmStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fTrapEventSeverityWarmStart_Type.__name__ = "Integer32"
_Mgs360024fTrapEventSeverityWarmStart_Object = MibScalar
mgs360024fTrapEventSeverityWarmStart = _Mgs360024fTrapEventSeverityWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 7, 21),
    _Mgs360024fTrapEventSeverityWarmStart_Type()
)
mgs360024fTrapEventSeverityWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTrapEventSeverityWarmStart.setStatus("current")
_Mgs360024fSMTP_ObjectIdentity = ObjectIdentity
mgs360024fSMTP = _Mgs360024fSMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 8)
)
_Mgs360024fSMTPMailServer_Type = DisplayString
_Mgs360024fSMTPMailServer_Object = MibScalar
mgs360024fSMTPMailServer = _Mgs360024fSMTPMailServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 8, 1),
    _Mgs360024fSMTPMailServer_Type()
)
mgs360024fSMTPMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSMTPMailServer.setStatus("current")
_Mgs360024fSMTPUserName_Type = DisplayString
_Mgs360024fSMTPUserName_Object = MibScalar
mgs360024fSMTPUserName = _Mgs360024fSMTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 8, 2),
    _Mgs360024fSMTPUserName_Type()
)
mgs360024fSMTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSMTPUserName.setStatus("current")
_Mgs360024fSMTPPassword_Type = DisplayString
_Mgs360024fSMTPPassword_Object = MibScalar
mgs360024fSMTPPassword = _Mgs360024fSMTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 8, 3),
    _Mgs360024fSMTPPassword_Type()
)
mgs360024fSMTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSMTPPassword.setStatus("current")


class _Mgs360024fSMTPServeriryLevel_Type(Integer32):
    """Custom type mgs360024fSMTPServeriryLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mgs360024fSMTPServeriryLevel_Type.__name__ = "Integer32"
_Mgs360024fSMTPServeriryLevel_Object = MibScalar
mgs360024fSMTPServeriryLevel = _Mgs360024fSMTPServeriryLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 8, 4),
    _Mgs360024fSMTPServeriryLevel_Type()
)
mgs360024fSMTPServeriryLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSMTPServeriryLevel.setStatus("current")
_Mgs360024fSMTPSender_Type = DisplayString
_Mgs360024fSMTPSender_Object = MibScalar
mgs360024fSMTPSender = _Mgs360024fSMTPSender_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 8, 5),
    _Mgs360024fSMTPSender_Type()
)
mgs360024fSMTPSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSMTPSender.setStatus("current")
_Mgs360024fSMTPReturnPath_Type = DisplayString
_Mgs360024fSMTPReturnPath_Object = MibScalar
mgs360024fSMTPReturnPath = _Mgs360024fSMTPReturnPath_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 8, 6),
    _Mgs360024fSMTPReturnPath_Type()
)
mgs360024fSMTPReturnPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSMTPReturnPath.setStatus("current")
_Mgs360024fSMTPEmailAddress1_Type = DisplayString
_Mgs360024fSMTPEmailAddress1_Object = MibScalar
mgs360024fSMTPEmailAddress1 = _Mgs360024fSMTPEmailAddress1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 8, 7),
    _Mgs360024fSMTPEmailAddress1_Type()
)
mgs360024fSMTPEmailAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSMTPEmailAddress1.setStatus("current")
_Mgs360024fSMTPEmailAddress2_Type = DisplayString
_Mgs360024fSMTPEmailAddress2_Object = MibScalar
mgs360024fSMTPEmailAddress2 = _Mgs360024fSMTPEmailAddress2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 8, 8),
    _Mgs360024fSMTPEmailAddress2_Type()
)
mgs360024fSMTPEmailAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSMTPEmailAddress2.setStatus("current")
_Mgs360024fSMTPEmailAddress3_Type = DisplayString
_Mgs360024fSMTPEmailAddress3_Object = MibScalar
mgs360024fSMTPEmailAddress3 = _Mgs360024fSMTPEmailAddress3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 8, 9),
    _Mgs360024fSMTPEmailAddress3_Type()
)
mgs360024fSMTPEmailAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSMTPEmailAddress3.setStatus("current")
_Mgs360024fSMTPEmailAddress4_Type = DisplayString
_Mgs360024fSMTPEmailAddress4_Object = MibScalar
mgs360024fSMTPEmailAddress4 = _Mgs360024fSMTPEmailAddress4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 8, 10),
    _Mgs360024fSMTPEmailAddress4_Type()
)
mgs360024fSMTPEmailAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSMTPEmailAddress4.setStatus("current")
_Mgs360024fSMTPEmailAddress5_Type = DisplayString
_Mgs360024fSMTPEmailAddress5_Object = MibScalar
mgs360024fSMTPEmailAddress5 = _Mgs360024fSMTPEmailAddress5_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 8, 11),
    _Mgs360024fSMTPEmailAddress5_Type()
)
mgs360024fSMTPEmailAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSMTPEmailAddress5.setStatus("current")
_Mgs360024fSMTPEmailAddress6_Type = DisplayString
_Mgs360024fSMTPEmailAddress6_Object = MibScalar
mgs360024fSMTPEmailAddress6 = _Mgs360024fSMTPEmailAddress6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 8, 12),
    _Mgs360024fSMTPEmailAddress6_Type()
)
mgs360024fSMTPEmailAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSMTPEmailAddress6.setStatus("current")
_Mgs360024fACL_ObjectIdentity = ObjectIdentity
mgs360024fACL = _Mgs360024fACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9)
)
_Mgs360024fACLPortsConfTable_Object = MibTable
mgs360024fACLPortsConfTable = _Mgs360024fACLPortsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 1)
)
if mibBuilder.loadTexts:
    mgs360024fACLPortsConfTable.setStatus("current")
_Mgs360024fACLPortsConfEntry_Object = MibTableRow
mgs360024fACLPortsConfEntry = _Mgs360024fACLPortsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 1, 1)
)
mgs360024fACLPortsConfEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fACLPortsConfPort"),
)
if mibBuilder.loadTexts:
    mgs360024fACLPortsConfEntry.setStatus("current")


class _Mgs360024fACLPortsConfPort_Type(Integer32):
    """Custom type mgs360024fACLPortsConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fACLPortsConfPort_Type.__name__ = "Integer32"
_Mgs360024fACLPortsConfPort_Object = MibTableColumn
mgs360024fACLPortsConfPort = _Mgs360024fACLPortsConfPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 1, 1, 1),
    _Mgs360024fACLPortsConfPort_Type()
)
mgs360024fACLPortsConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fACLPortsConfPort.setStatus("current")


class _Mgs360024fACLPortsConfPolicyID_Type(Integer32):
    """Custom type mgs360024fACLPortsConfPolicyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Mgs360024fACLPortsConfPolicyID_Type.__name__ = "Integer32"
_Mgs360024fACLPortsConfPolicyID_Object = MibTableColumn
mgs360024fACLPortsConfPolicyID = _Mgs360024fACLPortsConfPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 1, 1, 2),
    _Mgs360024fACLPortsConfPolicyID_Type()
)
mgs360024fACLPortsConfPolicyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLPortsConfPolicyID.setStatus("current")


class _Mgs360024fACLPortsConfAction_Type(Integer32):
    """Custom type mgs360024fACLPortsConfAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fACLPortsConfAction_Type.__name__ = "Integer32"
_Mgs360024fACLPortsConfAction_Object = MibTableColumn
mgs360024fACLPortsConfAction = _Mgs360024fACLPortsConfAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 1, 1, 3),
    _Mgs360024fACLPortsConfAction_Type()
)
mgs360024fACLPortsConfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLPortsConfAction.setStatus("current")


class _Mgs360024fACLPortsConfRateLimiterID_Type(Integer32):
    """Custom type mgs360024fACLPortsConfRateLimiterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Mgs360024fACLPortsConfRateLimiterID_Type.__name__ = "Integer32"
_Mgs360024fACLPortsConfRateLimiterID_Object = MibTableColumn
mgs360024fACLPortsConfRateLimiterID = _Mgs360024fACLPortsConfRateLimiterID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 1, 1, 4),
    _Mgs360024fACLPortsConfRateLimiterID_Type()
)
mgs360024fACLPortsConfRateLimiterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLPortsConfRateLimiterID.setStatus("current")


class _Mgs360024fACLPortsConfPortRedirect_Type(Integer32):
    """Custom type mgs360024fACLPortsConfPortRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Mgs360024fACLPortsConfPortRedirect_Type.__name__ = "Integer32"
_Mgs360024fACLPortsConfPortRedirect_Object = MibTableColumn
mgs360024fACLPortsConfPortRedirect = _Mgs360024fACLPortsConfPortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 1, 1, 5),
    _Mgs360024fACLPortsConfPortRedirect_Type()
)
mgs360024fACLPortsConfPortRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLPortsConfPortRedirect.setStatus("current")


class _Mgs360024fACLPortsConfLogging_Type(Integer32):
    """Custom type mgs360024fACLPortsConfLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fACLPortsConfLogging_Type.__name__ = "Integer32"
_Mgs360024fACLPortsConfLogging_Object = MibTableColumn
mgs360024fACLPortsConfLogging = _Mgs360024fACLPortsConfLogging_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 1, 1, 7),
    _Mgs360024fACLPortsConfLogging_Type()
)
mgs360024fACLPortsConfLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLPortsConfLogging.setStatus("current")


class _Mgs360024fACLPortsConfShutdown_Type(Integer32):
    """Custom type mgs360024fACLPortsConfShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fACLPortsConfShutdown_Type.__name__ = "Integer32"
_Mgs360024fACLPortsConfShutdown_Object = MibTableColumn
mgs360024fACLPortsConfShutdown = _Mgs360024fACLPortsConfShutdown_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 1, 1, 8),
    _Mgs360024fACLPortsConfShutdown_Type()
)
mgs360024fACLPortsConfShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLPortsConfShutdown.setStatus("current")


class _Mgs360024fACLPortsConfState_Type(Integer32):
    """Custom type mgs360024fACLPortsConfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fACLPortsConfState_Type.__name__ = "Integer32"
_Mgs360024fACLPortsConfState_Object = MibTableColumn
mgs360024fACLPortsConfState = _Mgs360024fACLPortsConfState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 1, 1, 9),
    _Mgs360024fACLPortsConfState_Type()
)
mgs360024fACLPortsConfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLPortsConfState.setStatus("current")
_Mgs360024fACLPortsConfCounter_Type = Counter32
_Mgs360024fACLPortsConfCounter_Object = MibTableColumn
mgs360024fACLPortsConfCounter = _Mgs360024fACLPortsConfCounter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 1, 1, 10),
    _Mgs360024fACLPortsConfCounter_Type()
)
mgs360024fACLPortsConfCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fACLPortsConfCounter.setStatus("current")
_Mgs360024fACLRateLimiterTable_Object = MibTable
mgs360024fACLRateLimiterTable = _Mgs360024fACLRateLimiterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 2)
)
if mibBuilder.loadTexts:
    mgs360024fACLRateLimiterTable.setStatus("current")
_Mgs360024fACLRateLimiterEntry_Object = MibTableRow
mgs360024fACLRateLimiterEntry = _Mgs360024fACLRateLimiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 2, 1)
)
mgs360024fACLRateLimiterEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fACLRateLimiterID"),
)
if mibBuilder.loadTexts:
    mgs360024fACLRateLimiterEntry.setStatus("current")


class _Mgs360024fACLRateLimiterID_Type(Integer32):
    """Custom type mgs360024fACLRateLimiterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Mgs360024fACLRateLimiterID_Type.__name__ = "Integer32"
_Mgs360024fACLRateLimiterID_Object = MibTableColumn
mgs360024fACLRateLimiterID = _Mgs360024fACLRateLimiterID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 2, 1, 1),
    _Mgs360024fACLRateLimiterID_Type()
)
mgs360024fACLRateLimiterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fACLRateLimiterID.setStatus("current")


class _Mgs360024fACLRateLimiterRate_Type(Integer32):
    """Custom type mgs360024fACLRateLimiterRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3276700),
    )


_Mgs360024fACLRateLimiterRate_Type.__name__ = "Integer32"
_Mgs360024fACLRateLimiterRate_Object = MibTableColumn
mgs360024fACLRateLimiterRate = _Mgs360024fACLRateLimiterRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 2, 1, 3),
    _Mgs360024fACLRateLimiterRate_Type()
)
mgs360024fACLRateLimiterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLRateLimiterRate.setStatus("current")
_Mgs360024fACLACE_ObjectIdentity = ObjectIdentity
mgs360024fACLACE = _Mgs360024fACLACE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3)
)


class _Mgs360024fACLACECreate_Type(Integer32):
    """Custom type mgs360024fACLACECreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fACLACECreate_Type.__name__ = "Integer32"
_Mgs360024fACLACECreate_Object = MibScalar
mgs360024fACLACECreate = _Mgs360024fACLACECreate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 1),
    _Mgs360024fACLACECreate_Type()
)
mgs360024fACLACECreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACECreate.setStatus("current")
_Mgs360024fACLACETable_Object = MibTable
mgs360024fACLACETable = _Mgs360024fACLACETable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2)
)
if mibBuilder.loadTexts:
    mgs360024fACLACETable.setStatus("current")
_Mgs360024fACLACEEntry_Object = MibTableRow
mgs360024fACLACEEntry = _Mgs360024fACLACEEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1)
)
mgs360024fACLACEEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fACLACEIndex"),
)
if mibBuilder.loadTexts:
    mgs360024fACLACEEntry.setStatus("current")


class _Mgs360024fACLACEIndex_Type(Integer32):
    """Custom type mgs360024fACLACEIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Mgs360024fACLACEIndex_Type.__name__ = "Integer32"
_Mgs360024fACLACEIndex_Object = MibTableColumn
mgs360024fACLACEIndex = _Mgs360024fACLACEIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 1),
    _Mgs360024fACLACEIndex_Type()
)
mgs360024fACLACEIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fACLACEIndex.setStatus("current")


class _Mgs360024fACLACEID_Type(Integer32):
    """Custom type mgs360024fACLACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Mgs360024fACLACEID_Type.__name__ = "Integer32"
_Mgs360024fACLACEID_Object = MibTableColumn
mgs360024fACLACEID = _Mgs360024fACLACEID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 2),
    _Mgs360024fACLACEID_Type()
)
mgs360024fACLACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEID.setStatus("current")


class _Mgs360024fACLACENextID_Type(Integer32):
    """Custom type mgs360024fACLACENextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Mgs360024fACLACENextID_Type.__name__ = "Integer32"
_Mgs360024fACLACENextID_Object = MibTableColumn
mgs360024fACLACENextID = _Mgs360024fACLACENextID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 3),
    _Mgs360024fACLACENextID_Type()
)
mgs360024fACLACENextID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACENextID.setStatus("current")
_Mgs360024fACLACEIngressPort_Type = DisplayString
_Mgs360024fACLACEIngressPort_Object = MibTableColumn
mgs360024fACLACEIngressPort = _Mgs360024fACLACEIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 4),
    _Mgs360024fACLACEIngressPort_Type()
)
mgs360024fACLACEIngressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEIngressPort.setStatus("current")


class _Mgs360024fACLACEPortPolicyNumber_Type(Integer32):
    """Custom type mgs360024fACLACEPortPolicyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Mgs360024fACLACEPortPolicyNumber_Type.__name__ = "Integer32"
_Mgs360024fACLACEPortPolicyNumber_Object = MibTableColumn
mgs360024fACLACEPortPolicyNumber = _Mgs360024fACLACEPortPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 5),
    _Mgs360024fACLACEPortPolicyNumber_Type()
)
mgs360024fACLACEPortPolicyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEPortPolicyNumber.setStatus("current")


class _Mgs360024fACLACEPortPolicyBitmask_Type(Integer32):
    """Custom type mgs360024fACLACEPortPolicyBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Mgs360024fACLACEPortPolicyBitmask_Type.__name__ = "Integer32"
_Mgs360024fACLACEPortPolicyBitmask_Object = MibTableColumn
mgs360024fACLACEPortPolicyBitmask = _Mgs360024fACLACEPortPolicyBitmask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 6),
    _Mgs360024fACLACEPortPolicyBitmask_Type()
)
mgs360024fACLACEPortPolicyBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEPortPolicyBitmask.setStatus("current")


class _Mgs360024fACLACEFrameType_Type(Integer32):
    """Custom type mgs360024fACLACEFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Mgs360024fACLACEFrameType_Type.__name__ = "Integer32"
_Mgs360024fACLACEFrameType_Object = MibTableColumn
mgs360024fACLACEFrameType = _Mgs360024fACLACEFrameType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 7),
    _Mgs360024fACLACEFrameType_Type()
)
mgs360024fACLACEFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEFrameType.setStatus("current")


class _Mgs360024fACLACEAction_Type(Integer32):
    """Custom type mgs360024fACLACEAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fACLACEAction_Type.__name__ = "Integer32"
_Mgs360024fACLACEAction_Object = MibTableColumn
mgs360024fACLACEAction = _Mgs360024fACLACEAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 8),
    _Mgs360024fACLACEAction_Type()
)
mgs360024fACLACEAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEAction.setStatus("current")
_Mgs360024fACLACEDenyPortRedirect_Type = DisplayString
_Mgs360024fACLACEDenyPortRedirect_Object = MibTableColumn
mgs360024fACLACEDenyPortRedirect = _Mgs360024fACLACEDenyPortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 9),
    _Mgs360024fACLACEDenyPortRedirect_Type()
)
mgs360024fACLACEDenyPortRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEDenyPortRedirect.setStatus("current")


class _Mgs360024fACLACELogging_Type(Integer32):
    """Custom type mgs360024fACLACELogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fACLACELogging_Type.__name__ = "Integer32"
_Mgs360024fACLACELogging_Object = MibTableColumn
mgs360024fACLACELogging = _Mgs360024fACLACELogging_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 10),
    _Mgs360024fACLACELogging_Type()
)
mgs360024fACLACELogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACELogging.setStatus("current")


class _Mgs360024fACLACERateLimiter_Type(Integer32):
    """Custom type mgs360024fACLACERateLimiter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Mgs360024fACLACERateLimiter_Type.__name__ = "Integer32"
_Mgs360024fACLACERateLimiter_Object = MibTableColumn
mgs360024fACLACERateLimiter = _Mgs360024fACLACERateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 12),
    _Mgs360024fACLACERateLimiter_Type()
)
mgs360024fACLACERateLimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACERateLimiter.setStatus("current")


class _Mgs360024fACLACEShutdown_Type(Integer32):
    """Custom type mgs360024fACLACEShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fACLACEShutdown_Type.__name__ = "Integer32"
_Mgs360024fACLACEShutdown_Object = MibTableColumn
mgs360024fACLACEShutdown = _Mgs360024fACLACEShutdown_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 13),
    _Mgs360024fACLACEShutdown_Type()
)
mgs360024fACLACEShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEShutdown.setStatus("current")


class _Mgs360024fACLACEVLANTagPriority_Type(Integer32):
    """Custom type mgs360024fACLACEVLANTagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Mgs360024fACLACEVLANTagPriority_Type.__name__ = "Integer32"
_Mgs360024fACLACEVLANTagPriority_Object = MibTableColumn
mgs360024fACLACEVLANTagPriority = _Mgs360024fACLACEVLANTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 15),
    _Mgs360024fACLACEVLANTagPriority_Type()
)
mgs360024fACLACEVLANTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEVLANTagPriority.setStatus("current")


class _Mgs360024fACLACEVLANVID_Type(Integer32):
    """Custom type mgs360024fACLACEVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Mgs360024fACLACEVLANVID_Type.__name__ = "Integer32"
_Mgs360024fACLACEVLANVID_Object = MibTableColumn
mgs360024fACLACEVLANVID = _Mgs360024fACLACEVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 16),
    _Mgs360024fACLACEVLANVID_Type()
)
mgs360024fACLACEVLANVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEVLANVID.setStatus("current")


class _Mgs360024fACLACEEtherType_Type(Integer32):
    """Custom type mgs360024fACLACEEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Mgs360024fACLACEEtherType_Type.__name__ = "Integer32"
_Mgs360024fACLACEEtherType_Object = MibTableColumn
mgs360024fACLACEEtherType = _Mgs360024fACLACEEtherType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 17),
    _Mgs360024fACLACEEtherType_Type()
)
mgs360024fACLACEEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEEtherType.setStatus("current")
_Mgs360024fACLACESMAC_Type = DisplayString
_Mgs360024fACLACESMAC_Object = MibTableColumn
mgs360024fACLACESMAC = _Mgs360024fACLACESMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 18),
    _Mgs360024fACLACESMAC_Type()
)
mgs360024fACLACESMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACESMAC.setStatus("current")


class _Mgs360024fACLACEDMACType_Type(Integer32):
    """Custom type mgs360024fACLACEDMACType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Mgs360024fACLACEDMACType_Type.__name__ = "Integer32"
_Mgs360024fACLACEDMACType_Object = MibTableColumn
mgs360024fACLACEDMACType = _Mgs360024fACLACEDMACType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 19),
    _Mgs360024fACLACEDMACType_Type()
)
mgs360024fACLACEDMACType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEDMACType.setStatus("current")
_Mgs360024fACLACEDMAC_Type = DisplayString
_Mgs360024fACLACEDMAC_Object = MibTableColumn
mgs360024fACLACEDMAC = _Mgs360024fACLACEDMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 20),
    _Mgs360024fACLACEDMAC_Type()
)
mgs360024fACLACEDMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEDMAC.setStatus("current")


class _Mgs360024fACLACEArpOpcode_Type(Integer32):
    """Custom type mgs360024fACLACEArpOpcode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Mgs360024fACLACEArpOpcode_Type.__name__ = "Integer32"
_Mgs360024fACLACEArpOpcode_Object = MibTableColumn
mgs360024fACLACEArpOpcode = _Mgs360024fACLACEArpOpcode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 21),
    _Mgs360024fACLACEArpOpcode_Type()
)
mgs360024fACLACEArpOpcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEArpOpcode.setStatus("current")


class _Mgs360024fACLACEArpFlagsRequestReply_Type(Integer32):
    """Custom type mgs360024fACLACEArpFlagsRequestReply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mgs360024fACLACEArpFlagsRequestReply_Type.__name__ = "Integer32"
_Mgs360024fACLACEArpFlagsRequestReply_Object = MibTableColumn
mgs360024fACLACEArpFlagsRequestReply = _Mgs360024fACLACEArpFlagsRequestReply_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 22),
    _Mgs360024fACLACEArpFlagsRequestReply_Type()
)
mgs360024fACLACEArpFlagsRequestReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEArpFlagsRequestReply.setStatus("current")


class _Mgs360024fACLACEArpFlagsArpSmac_Type(Integer32):
    """Custom type mgs360024fACLACEArpFlagsArpSmac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mgs360024fACLACEArpFlagsArpSmac_Type.__name__ = "Integer32"
_Mgs360024fACLACEArpFlagsArpSmac_Object = MibTableColumn
mgs360024fACLACEArpFlagsArpSmac = _Mgs360024fACLACEArpFlagsArpSmac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 23),
    _Mgs360024fACLACEArpFlagsArpSmac_Type()
)
mgs360024fACLACEArpFlagsArpSmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEArpFlagsArpSmac.setStatus("current")


class _Mgs360024fACLACEArpFlagsRarpDmac_Type(Integer32):
    """Custom type mgs360024fACLACEArpFlagsRarpDmac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mgs360024fACLACEArpFlagsRarpDmac_Type.__name__ = "Integer32"
_Mgs360024fACLACEArpFlagsRarpDmac_Object = MibTableColumn
mgs360024fACLACEArpFlagsRarpDmac = _Mgs360024fACLACEArpFlagsRarpDmac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 24),
    _Mgs360024fACLACEArpFlagsRarpDmac_Type()
)
mgs360024fACLACEArpFlagsRarpDmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEArpFlagsRarpDmac.setStatus("current")


class _Mgs360024fACLACEArpFlagsLength_Type(Integer32):
    """Custom type mgs360024fACLACEArpFlagsLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mgs360024fACLACEArpFlagsLength_Type.__name__ = "Integer32"
_Mgs360024fACLACEArpFlagsLength_Object = MibTableColumn
mgs360024fACLACEArpFlagsLength = _Mgs360024fACLACEArpFlagsLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 25),
    _Mgs360024fACLACEArpFlagsLength_Type()
)
mgs360024fACLACEArpFlagsLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEArpFlagsLength.setStatus("current")


class _Mgs360024fACLACEArpFlagsIp_Type(Integer32):
    """Custom type mgs360024fACLACEArpFlagsIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mgs360024fACLACEArpFlagsIp_Type.__name__ = "Integer32"
_Mgs360024fACLACEArpFlagsIp_Object = MibTableColumn
mgs360024fACLACEArpFlagsIp = _Mgs360024fACLACEArpFlagsIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 26),
    _Mgs360024fACLACEArpFlagsIp_Type()
)
mgs360024fACLACEArpFlagsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEArpFlagsIp.setStatus("current")


class _Mgs360024fACLACEArpFlagsEthernet_Type(Integer32):
    """Custom type mgs360024fACLACEArpFlagsEthernet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mgs360024fACLACEArpFlagsEthernet_Type.__name__ = "Integer32"
_Mgs360024fACLACEArpFlagsEthernet_Object = MibTableColumn
mgs360024fACLACEArpFlagsEthernet = _Mgs360024fACLACEArpFlagsEthernet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 27),
    _Mgs360024fACLACEArpFlagsEthernet_Type()
)
mgs360024fACLACEArpFlagsEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEArpFlagsEthernet.setStatus("current")


class _Mgs360024fACLACESIPType_Type(Integer32):
    """Custom type mgs360024fACLACESIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fACLACESIPType_Type.__name__ = "Integer32"
_Mgs360024fACLACESIPType_Object = MibTableColumn
mgs360024fACLACESIPType = _Mgs360024fACLACESIPType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 28),
    _Mgs360024fACLACESIPType_Type()
)
mgs360024fACLACESIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACESIPType.setStatus("current")
_Mgs360024fACLACESIPIPAddress_Type = IpAddress
_Mgs360024fACLACESIPIPAddress_Object = MibTableColumn
mgs360024fACLACESIPIPAddress = _Mgs360024fACLACESIPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 29),
    _Mgs360024fACLACESIPIPAddress_Type()
)
mgs360024fACLACESIPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACESIPIPAddress.setStatus("current")


class _Mgs360024fACLACESIPNetworkPrefix_Type(Integer32):
    """Custom type mgs360024fACLACESIPNetworkPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgs360024fACLACESIPNetworkPrefix_Type.__name__ = "Integer32"
_Mgs360024fACLACESIPNetworkPrefix_Object = MibTableColumn
mgs360024fACLACESIPNetworkPrefix = _Mgs360024fACLACESIPNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 30),
    _Mgs360024fACLACESIPNetworkPrefix_Type()
)
mgs360024fACLACESIPNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACESIPNetworkPrefix.setStatus("current")


class _Mgs360024fACLACEDIPType_Type(Integer32):
    """Custom type mgs360024fACLACEDIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fACLACEDIPType_Type.__name__ = "Integer32"
_Mgs360024fACLACEDIPType_Object = MibTableColumn
mgs360024fACLACEDIPType = _Mgs360024fACLACEDIPType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 32),
    _Mgs360024fACLACEDIPType_Type()
)
mgs360024fACLACEDIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEDIPType.setStatus("current")
_Mgs360024fACLACEDIPIPAddress_Type = IpAddress
_Mgs360024fACLACEDIPIPAddress_Object = MibTableColumn
mgs360024fACLACEDIPIPAddress = _Mgs360024fACLACEDIPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 33),
    _Mgs360024fACLACEDIPIPAddress_Type()
)
mgs360024fACLACEDIPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEDIPIPAddress.setStatus("current")


class _Mgs360024fACLACEDIPNetworkPrefix_Type(Integer32):
    """Custom type mgs360024fACLACEDIPNetworkPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgs360024fACLACEDIPNetworkPrefix_Type.__name__ = "Integer32"
_Mgs360024fACLACEDIPNetworkPrefix_Object = MibTableColumn
mgs360024fACLACEDIPNetworkPrefix = _Mgs360024fACLACEDIPNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 34),
    _Mgs360024fACLACEDIPNetworkPrefix_Type()
)
mgs360024fACLACEDIPNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEDIPNetworkPrefix.setStatus("current")


class _Mgs360024fACLACEIPProtocol_Type(Integer32):
    """Custom type mgs360024fACLACEIPProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Mgs360024fACLACEIPProtocol_Type.__name__ = "Integer32"
_Mgs360024fACLACEIPProtocol_Object = MibTableColumn
mgs360024fACLACEIPProtocol = _Mgs360024fACLACEIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 36),
    _Mgs360024fACLACEIPProtocol_Type()
)
mgs360024fACLACEIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEIPProtocol.setStatus("current")


class _Mgs360024fACLACEIPFlagsTTL_Type(Integer32):
    """Custom type mgs360024fACLACEIPFlagsTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mgs360024fACLACEIPFlagsTTL_Type.__name__ = "Integer32"
_Mgs360024fACLACEIPFlagsTTL_Object = MibTableColumn
mgs360024fACLACEIPFlagsTTL = _Mgs360024fACLACEIPFlagsTTL_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 37),
    _Mgs360024fACLACEIPFlagsTTL_Type()
)
mgs360024fACLACEIPFlagsTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEIPFlagsTTL.setStatus("current")


class _Mgs360024fACLACEIPFlagsOptions_Type(Integer32):
    """Custom type mgs360024fACLACEIPFlagsOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mgs360024fACLACEIPFlagsOptions_Type.__name__ = "Integer32"
_Mgs360024fACLACEIPFlagsOptions_Object = MibTableColumn
mgs360024fACLACEIPFlagsOptions = _Mgs360024fACLACEIPFlagsOptions_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 38),
    _Mgs360024fACLACEIPFlagsOptions_Type()
)
mgs360024fACLACEIPFlagsOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEIPFlagsOptions.setStatus("current")


class _Mgs360024fACLACEIPFlagsFragment_Type(Integer32):
    """Custom type mgs360024fACLACEIPFlagsFragment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mgs360024fACLACEIPFlagsFragment_Type.__name__ = "Integer32"
_Mgs360024fACLACEIPFlagsFragment_Object = MibTableColumn
mgs360024fACLACEIPFlagsFragment = _Mgs360024fACLACEIPFlagsFragment_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 39),
    _Mgs360024fACLACEIPFlagsFragment_Type()
)
mgs360024fACLACEIPFlagsFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEIPFlagsFragment.setStatus("current")


class _Mgs360024fACLACEICMPType_Type(Integer32):
    """Custom type mgs360024fACLACEICMPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Mgs360024fACLACEICMPType_Type.__name__ = "Integer32"
_Mgs360024fACLACEICMPType_Object = MibTableColumn
mgs360024fACLACEICMPType = _Mgs360024fACLACEICMPType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 40),
    _Mgs360024fACLACEICMPType_Type()
)
mgs360024fACLACEICMPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEICMPType.setStatus("current")


class _Mgs360024fACLACEICMPCode_Type(Integer32):
    """Custom type mgs360024fACLACEICMPCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Mgs360024fACLACEICMPCode_Type.__name__ = "Integer32"
_Mgs360024fACLACEICMPCode_Object = MibTableColumn
mgs360024fACLACEICMPCode = _Mgs360024fACLACEICMPCode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 41),
    _Mgs360024fACLACEICMPCode_Type()
)
mgs360024fACLACEICMPCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEICMPCode.setStatus("current")


class _Mgs360024fACLACESourcePortMin_Type(Integer32):
    """Custom type mgs360024fACLACESourcePortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Mgs360024fACLACESourcePortMin_Type.__name__ = "Integer32"
_Mgs360024fACLACESourcePortMin_Object = MibTableColumn
mgs360024fACLACESourcePortMin = _Mgs360024fACLACESourcePortMin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 42),
    _Mgs360024fACLACESourcePortMin_Type()
)
mgs360024fACLACESourcePortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACESourcePortMin.setStatus("current")


class _Mgs360024fACLACESourcePortMax_Type(Integer32):
    """Custom type mgs360024fACLACESourcePortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Mgs360024fACLACESourcePortMax_Type.__name__ = "Integer32"
_Mgs360024fACLACESourcePortMax_Object = MibTableColumn
mgs360024fACLACESourcePortMax = _Mgs360024fACLACESourcePortMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 43),
    _Mgs360024fACLACESourcePortMax_Type()
)
mgs360024fACLACESourcePortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACESourcePortMax.setStatus("current")


class _Mgs360024fACLACEDestPortMin_Type(Integer32):
    """Custom type mgs360024fACLACEDestPortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Mgs360024fACLACEDestPortMin_Type.__name__ = "Integer32"
_Mgs360024fACLACEDestPortMin_Object = MibTableColumn
mgs360024fACLACEDestPortMin = _Mgs360024fACLACEDestPortMin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 44),
    _Mgs360024fACLACEDestPortMin_Type()
)
mgs360024fACLACEDestPortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEDestPortMin.setStatus("current")


class _Mgs360024fACLACEDestPortMax_Type(Integer32):
    """Custom type mgs360024fACLACEDestPortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Mgs360024fACLACEDestPortMax_Type.__name__ = "Integer32"
_Mgs360024fACLACEDestPortMax_Object = MibTableColumn
mgs360024fACLACEDestPortMax = _Mgs360024fACLACEDestPortMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 45),
    _Mgs360024fACLACEDestPortMax_Type()
)
mgs360024fACLACEDestPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEDestPortMax.setStatus("current")


class _Mgs360024fACLACETCPFlagsFin_Type(Integer32):
    """Custom type mgs360024fACLACETCPFlagsFin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mgs360024fACLACETCPFlagsFin_Type.__name__ = "Integer32"
_Mgs360024fACLACETCPFlagsFin_Object = MibTableColumn
mgs360024fACLACETCPFlagsFin = _Mgs360024fACLACETCPFlagsFin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 46),
    _Mgs360024fACLACETCPFlagsFin_Type()
)
mgs360024fACLACETCPFlagsFin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACETCPFlagsFin.setStatus("current")


class _Mgs360024fACLACETCPFlagsSyn_Type(Integer32):
    """Custom type mgs360024fACLACETCPFlagsSyn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mgs360024fACLACETCPFlagsSyn_Type.__name__ = "Integer32"
_Mgs360024fACLACETCPFlagsSyn_Object = MibTableColumn
mgs360024fACLACETCPFlagsSyn = _Mgs360024fACLACETCPFlagsSyn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 47),
    _Mgs360024fACLACETCPFlagsSyn_Type()
)
mgs360024fACLACETCPFlagsSyn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACETCPFlagsSyn.setStatus("current")


class _Mgs360024fACLACETCPFlagsRst_Type(Integer32):
    """Custom type mgs360024fACLACETCPFlagsRst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mgs360024fACLACETCPFlagsRst_Type.__name__ = "Integer32"
_Mgs360024fACLACETCPFlagsRst_Object = MibTableColumn
mgs360024fACLACETCPFlagsRst = _Mgs360024fACLACETCPFlagsRst_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 48),
    _Mgs360024fACLACETCPFlagsRst_Type()
)
mgs360024fACLACETCPFlagsRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACETCPFlagsRst.setStatus("current")


class _Mgs360024fACLACETCPFlagsPsh_Type(Integer32):
    """Custom type mgs360024fACLACETCPFlagsPsh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mgs360024fACLACETCPFlagsPsh_Type.__name__ = "Integer32"
_Mgs360024fACLACETCPFlagsPsh_Object = MibTableColumn
mgs360024fACLACETCPFlagsPsh = _Mgs360024fACLACETCPFlagsPsh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 49),
    _Mgs360024fACLACETCPFlagsPsh_Type()
)
mgs360024fACLACETCPFlagsPsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACETCPFlagsPsh.setStatus("current")


class _Mgs360024fACLACETCPFlagsAck_Type(Integer32):
    """Custom type mgs360024fACLACETCPFlagsAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mgs360024fACLACETCPFlagsAck_Type.__name__ = "Integer32"
_Mgs360024fACLACETCPFlagsAck_Object = MibTableColumn
mgs360024fACLACETCPFlagsAck = _Mgs360024fACLACETCPFlagsAck_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 50),
    _Mgs360024fACLACETCPFlagsAck_Type()
)
mgs360024fACLACETCPFlagsAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACETCPFlagsAck.setStatus("current")


class _Mgs360024fACLACETCPFlagsUrg_Type(Integer32):
    """Custom type mgs360024fACLACETCPFlagsUrg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mgs360024fACLACETCPFlagsUrg_Type.__name__ = "Integer32"
_Mgs360024fACLACETCPFlagsUrg_Object = MibTableColumn
mgs360024fACLACETCPFlagsUrg = _Mgs360024fACLACETCPFlagsUrg_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 51),
    _Mgs360024fACLACETCPFlagsUrg_Type()
)
mgs360024fACLACETCPFlagsUrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACETCPFlagsUrg.setStatus("current")


class _Mgs360024fACLACERowStatus_Type(Integer32):
    """Custom type mgs360024fACLACERowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Mgs360024fACLACERowStatus_Type.__name__ = "Integer32"
_Mgs360024fACLACERowStatus_Object = MibTableColumn
mgs360024fACLACERowStatus = _Mgs360024fACLACERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 2, 1, 66),
    _Mgs360024fACLACERowStatus_Type()
)
mgs360024fACLACERowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACERowStatus.setStatus("current")


class _Mgs360024fACLACEClear_Type(Integer32):
    """Custom type mgs360024fACLACEClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fACLACEClear_Type.__name__ = "Integer32"
_Mgs360024fACLACEClear_Object = MibScalar
mgs360024fACLACEClear = _Mgs360024fACLACEClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 3),
    _Mgs360024fACLACEClear_Type()
)
mgs360024fACLACEClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEClear.setStatus("current")


class _Mgs360024fACLACEMoveACEID_Type(Integer32):
    """Custom type mgs360024fACLACEMoveACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Mgs360024fACLACEMoveACEID_Type.__name__ = "Integer32"
_Mgs360024fACLACEMoveACEID_Object = MibScalar
mgs360024fACLACEMoveACEID = _Mgs360024fACLACEMoveACEID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 4),
    _Mgs360024fACLACEMoveACEID_Type()
)
mgs360024fACLACEMoveACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEMoveACEID.setStatus("current")


class _Mgs360024fACLACEMoveNextACEID_Type(Integer32):
    """Custom type mgs360024fACLACEMoveNextACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Mgs360024fACLACEMoveNextACEID_Type.__name__ = "Integer32"
_Mgs360024fACLACEMoveNextACEID_Object = MibScalar
mgs360024fACLACEMoveNextACEID = _Mgs360024fACLACEMoveNextACEID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 5),
    _Mgs360024fACLACEMoveNextACEID_Type()
)
mgs360024fACLACEMoveNextACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fACLACEMoveNextACEID.setStatus("current")
_Mgs360024fACLACEStatusTable_Object = MibTable
mgs360024fACLACEStatusTable = _Mgs360024fACLACEStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 6)
)
if mibBuilder.loadTexts:
    mgs360024fACLACEStatusTable.setStatus("current")
_Mgs360024fACLACEStatusEntry_Object = MibTableRow
mgs360024fACLACEStatusEntry = _Mgs360024fACLACEStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 6, 1)
)
mgs360024fACLACEStatusEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fACLACEStatusIndex"),
)
if mibBuilder.loadTexts:
    mgs360024fACLACEStatusEntry.setStatus("current")


class _Mgs360024fACLACEStatusIndex_Type(Integer32):
    """Custom type mgs360024fACLACEStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Mgs360024fACLACEStatusIndex_Type.__name__ = "Integer32"
_Mgs360024fACLACEStatusIndex_Object = MibTableColumn
mgs360024fACLACEStatusIndex = _Mgs360024fACLACEStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 6, 1, 1),
    _Mgs360024fACLACEStatusIndex_Type()
)
mgs360024fACLACEStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fACLACEStatusIndex.setStatus("current")
_Mgs360024fACLACEStatusUser_Type = DisplayString
_Mgs360024fACLACEStatusUser_Object = MibTableColumn
mgs360024fACLACEStatusUser = _Mgs360024fACLACEStatusUser_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 6, 1, 2),
    _Mgs360024fACLACEStatusUser_Type()
)
mgs360024fACLACEStatusUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fACLACEStatusUser.setStatus("current")


class _Mgs360024fACLACEStatusID_Type(Integer32):
    """Custom type mgs360024fACLACEStatusID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Mgs360024fACLACEStatusID_Type.__name__ = "Integer32"
_Mgs360024fACLACEStatusID_Object = MibTableColumn
mgs360024fACLACEStatusID = _Mgs360024fACLACEStatusID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 6, 1, 3),
    _Mgs360024fACLACEStatusID_Type()
)
mgs360024fACLACEStatusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fACLACEStatusID.setStatus("current")
_Mgs360024fACLACEStatusIngressPort_Type = DisplayString
_Mgs360024fACLACEStatusIngressPort_Object = MibTableColumn
mgs360024fACLACEStatusIngressPort = _Mgs360024fACLACEStatusIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 6, 1, 4),
    _Mgs360024fACLACEStatusIngressPort_Type()
)
mgs360024fACLACEStatusIngressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fACLACEStatusIngressPort.setStatus("current")
_Mgs360024fACLACEStatusFrameType_Type = DisplayString
_Mgs360024fACLACEStatusFrameType_Object = MibTableColumn
mgs360024fACLACEStatusFrameType = _Mgs360024fACLACEStatusFrameType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 6, 1, 5),
    _Mgs360024fACLACEStatusFrameType_Type()
)
mgs360024fACLACEStatusFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fACLACEStatusFrameType.setStatus("current")
_Mgs360024fACLACEStatusAction_Type = DisplayString
_Mgs360024fACLACEStatusAction_Object = MibTableColumn
mgs360024fACLACEStatusAction = _Mgs360024fACLACEStatusAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 6, 1, 6),
    _Mgs360024fACLACEStatusAction_Type()
)
mgs360024fACLACEStatusAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fACLACEStatusAction.setStatus("current")
_Mgs360024fACLACEStatusRateLimiter_Type = DisplayString
_Mgs360024fACLACEStatusRateLimiter_Object = MibTableColumn
mgs360024fACLACEStatusRateLimiter = _Mgs360024fACLACEStatusRateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 6, 1, 7),
    _Mgs360024fACLACEStatusRateLimiter_Type()
)
mgs360024fACLACEStatusRateLimiter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fACLACEStatusRateLimiter.setStatus("current")
_Mgs360024fACLACEStatusPortCopy_Type = DisplayString
_Mgs360024fACLACEStatusPortCopy_Object = MibTableColumn
mgs360024fACLACEStatusPortCopy = _Mgs360024fACLACEStatusPortCopy_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 6, 1, 8),
    _Mgs360024fACLACEStatusPortCopy_Type()
)
mgs360024fACLACEStatusPortCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fACLACEStatusPortCopy.setStatus("current")
_Mgs360024fACLACEStatusMirror_Type = DisplayString
_Mgs360024fACLACEStatusMirror_Object = MibTableColumn
mgs360024fACLACEStatusMirror = _Mgs360024fACLACEStatusMirror_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 6, 1, 9),
    _Mgs360024fACLACEStatusMirror_Type()
)
mgs360024fACLACEStatusMirror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fACLACEStatusMirror.setStatus("current")
_Mgs360024fACLACEStatusCPU_Type = DisplayString
_Mgs360024fACLACEStatusCPU_Object = MibTableColumn
mgs360024fACLACEStatusCPU = _Mgs360024fACLACEStatusCPU_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 6, 1, 10),
    _Mgs360024fACLACEStatusCPU_Type()
)
mgs360024fACLACEStatusCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fACLACEStatusCPU.setStatus("current")
_Mgs360024fACLACEStatusCounter_Type = Counter32
_Mgs360024fACLACEStatusCounter_Object = MibTableColumn
mgs360024fACLACEStatusCounter = _Mgs360024fACLACEStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 6, 1, 11),
    _Mgs360024fACLACEStatusCounter_Type()
)
mgs360024fACLACEStatusCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fACLACEStatusCounter.setStatus("current")
_Mgs360024fACLACEStatusConflict_Type = DisplayString
_Mgs360024fACLACEStatusConflict_Object = MibTableColumn
mgs360024fACLACEStatusConflict = _Mgs360024fACLACEStatusConflict_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 9, 3, 6, 1, 12),
    _Mgs360024fACLACEStatusConflict_Type()
)
mgs360024fACLACEStatusConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fACLACEStatusConflict.setStatus("current")
_Mgs360024fERPS_ObjectIdentity = ObjectIdentity
mgs360024fERPS = _Mgs360024fERPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10)
)
_Mgs360024fERPSConf_ObjectIdentity = ObjectIdentity
mgs360024fERPSConf = _Mgs360024fERPSConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1)
)


class _Mgs360024fERPSConfCreate_Type(Integer32):
    """Custom type mgs360024fERPSConfCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fERPSConfCreate_Type.__name__ = "Integer32"
_Mgs360024fERPSConfCreate_Object = MibScalar
mgs360024fERPSConfCreate = _Mgs360024fERPSConfCreate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 1),
    _Mgs360024fERPSConfCreate_Type()
)
mgs360024fERPSConfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSConfCreate.setStatus("current")
_Mgs360024fERPSConfTable_Object = MibTable
mgs360024fERPSConfTable = _Mgs360024fERPSConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2)
)
if mibBuilder.loadTexts:
    mgs360024fERPSConfTable.setStatus("current")
_Mgs360024fERPSConfEntry_Object = MibTableRow
mgs360024fERPSConfEntry = _Mgs360024fERPSConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1)
)
mgs360024fERPSConfEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fERPSConfIndex"),
)
if mibBuilder.loadTexts:
    mgs360024fERPSConfEntry.setStatus("current")


class _Mgs360024fERPSConfIndex_Type(Integer32):
    """Custom type mgs360024fERPSConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Mgs360024fERPSConfIndex_Type.__name__ = "Integer32"
_Mgs360024fERPSConfIndex_Object = MibTableColumn
mgs360024fERPSConfIndex = _Mgs360024fERPSConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 1),
    _Mgs360024fERPSConfIndex_Type()
)
mgs360024fERPSConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fERPSConfIndex.setStatus("current")


class _Mgs360024fERPSConfERPSID_Type(Integer32):
    """Custom type mgs360024fERPSConfERPSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Mgs360024fERPSConfERPSID_Type.__name__ = "Integer32"
_Mgs360024fERPSConfERPSID_Object = MibTableColumn
mgs360024fERPSConfERPSID = _Mgs360024fERPSConfERPSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 2),
    _Mgs360024fERPSConfERPSID_Type()
)
mgs360024fERPSConfERPSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSConfERPSID.setStatus("current")


class _Mgs360024fERPSConfPort0_Type(Integer32):
    """Custom type mgs360024fERPSConfPort0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Mgs360024fERPSConfPort0_Type.__name__ = "Integer32"
_Mgs360024fERPSConfPort0_Object = MibTableColumn
mgs360024fERPSConfPort0 = _Mgs360024fERPSConfPort0_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 3),
    _Mgs360024fERPSConfPort0_Type()
)
mgs360024fERPSConfPort0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSConfPort0.setStatus("current")


class _Mgs360024fERPSConfPort1_Type(Integer32):
    """Custom type mgs360024fERPSConfPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 26),
    )


_Mgs360024fERPSConfPort1_Type.__name__ = "Integer32"
_Mgs360024fERPSConfPort1_Object = MibTableColumn
mgs360024fERPSConfPort1 = _Mgs360024fERPSConfPort1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 4),
    _Mgs360024fERPSConfPort1_Type()
)
mgs360024fERPSConfPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSConfPort1.setStatus("current")


class _Mgs360024fERPSConfPort0SFMEP_Type(Integer32):
    """Custom type mgs360024fERPSConfPort0SFMEP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgs360024fERPSConfPort0SFMEP_Type.__name__ = "Integer32"
_Mgs360024fERPSConfPort0SFMEP_Object = MibTableColumn
mgs360024fERPSConfPort0SFMEP = _Mgs360024fERPSConfPort0SFMEP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 5),
    _Mgs360024fERPSConfPort0SFMEP_Type()
)
mgs360024fERPSConfPort0SFMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSConfPort0SFMEP.setStatus("current")


class _Mgs360024fERPSConfPort1SFMEP_Type(Integer32):
    """Custom type mgs360024fERPSConfPort1SFMEP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Mgs360024fERPSConfPort1SFMEP_Type.__name__ = "Integer32"
_Mgs360024fERPSConfPort1SFMEP_Object = MibTableColumn
mgs360024fERPSConfPort1SFMEP = _Mgs360024fERPSConfPort1SFMEP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 6),
    _Mgs360024fERPSConfPort1SFMEP_Type()
)
mgs360024fERPSConfPort1SFMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSConfPort1SFMEP.setStatus("current")


class _Mgs360024fERPSConfPort0APSMEP_Type(Integer32):
    """Custom type mgs360024fERPSConfPort0APSMEP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgs360024fERPSConfPort0APSMEP_Type.__name__ = "Integer32"
_Mgs360024fERPSConfPort0APSMEP_Object = MibTableColumn
mgs360024fERPSConfPort0APSMEP = _Mgs360024fERPSConfPort0APSMEP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 7),
    _Mgs360024fERPSConfPort0APSMEP_Type()
)
mgs360024fERPSConfPort0APSMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSConfPort0APSMEP.setStatus("current")


class _Mgs360024fERPSConfPort1APSMEP_Type(Integer32):
    """Custom type mgs360024fERPSConfPort1APSMEP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Mgs360024fERPSConfPort1APSMEP_Type.__name__ = "Integer32"
_Mgs360024fERPSConfPort1APSMEP_Object = MibTableColumn
mgs360024fERPSConfPort1APSMEP = _Mgs360024fERPSConfPort1APSMEP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 8),
    _Mgs360024fERPSConfPort1APSMEP_Type()
)
mgs360024fERPSConfPort1APSMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSConfPort1APSMEP.setStatus("current")


class _Mgs360024fERPSConfRingType_Type(Integer32):
    """Custom type mgs360024fERPSConfRingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fERPSConfRingType_Type.__name__ = "Integer32"
_Mgs360024fERPSConfRingType_Object = MibTableColumn
mgs360024fERPSConfRingType = _Mgs360024fERPSConfRingType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 9),
    _Mgs360024fERPSConfRingType_Type()
)
mgs360024fERPSConfRingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSConfRingType.setStatus("current")


class _Mgs360024fERPSConfInterconnectedNode_Type(Integer32):
    """Custom type mgs360024fERPSConfInterconnectedNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fERPSConfInterconnectedNode_Type.__name__ = "Integer32"
_Mgs360024fERPSConfInterconnectedNode_Object = MibTableColumn
mgs360024fERPSConfInterconnectedNode = _Mgs360024fERPSConfInterconnectedNode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 10),
    _Mgs360024fERPSConfInterconnectedNode_Type()
)
mgs360024fERPSConfInterconnectedNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSConfInterconnectedNode.setStatus("current")


class _Mgs360024fERPSConfVirtualChannel_Type(Integer32):
    """Custom type mgs360024fERPSConfVirtualChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fERPSConfVirtualChannel_Type.__name__ = "Integer32"
_Mgs360024fERPSConfVirtualChannel_Object = MibTableColumn
mgs360024fERPSConfVirtualChannel = _Mgs360024fERPSConfVirtualChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 11),
    _Mgs360024fERPSConfVirtualChannel_Type()
)
mgs360024fERPSConfVirtualChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSConfVirtualChannel.setStatus("current")


class _Mgs360024fERPSConfMajorRingID_Type(Integer32):
    """Custom type mgs360024fERPSConfMajorRingID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Mgs360024fERPSConfMajorRingID_Type.__name__ = "Integer32"
_Mgs360024fERPSConfMajorRingID_Object = MibTableColumn
mgs360024fERPSConfMajorRingID = _Mgs360024fERPSConfMajorRingID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 12),
    _Mgs360024fERPSConfMajorRingID_Type()
)
mgs360024fERPSConfMajorRingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fERPSConfMajorRingID.setStatus("current")


class _Mgs360024fERPSConfAlarm_Type(DisplayString):
    """Custom type mgs360024fERPSConfAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Mgs360024fERPSConfAlarm_Type.__name__ = "DisplayString"
_Mgs360024fERPSConfAlarm_Object = MibTableColumn
mgs360024fERPSConfAlarm = _Mgs360024fERPSConfAlarm_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 13),
    _Mgs360024fERPSConfAlarm_Type()
)
mgs360024fERPSConfAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fERPSConfAlarm.setStatus("current")


class _Mgs360024fERPSInstanceConfConfigured_Type(DisplayString):
    """Custom type mgs360024fERPSInstanceConfConfigured based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Mgs360024fERPSInstanceConfConfigured_Type.__name__ = "DisplayString"
_Mgs360024fERPSInstanceConfConfigured_Object = MibTableColumn
mgs360024fERPSInstanceConfConfigured = _Mgs360024fERPSInstanceConfConfigured_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 14),
    _Mgs360024fERPSInstanceConfConfigured_Type()
)
mgs360024fERPSInstanceConfConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fERPSInstanceConfConfigured.setStatus("current")


class _Mgs360024fERPSInstanceConfGuardTime_Type(Integer32):
    """Custom type mgs360024fERPSInstanceConfGuardTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_Mgs360024fERPSInstanceConfGuardTime_Type.__name__ = "Integer32"
_Mgs360024fERPSInstanceConfGuardTime_Object = MibTableColumn
mgs360024fERPSInstanceConfGuardTime = _Mgs360024fERPSInstanceConfGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 15),
    _Mgs360024fERPSInstanceConfGuardTime_Type()
)
mgs360024fERPSInstanceConfGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSInstanceConfGuardTime.setStatus("current")


class _Mgs360024fERPSInstanceConfWTRTime_Type(Integer32):
    """Custom type mgs360024fERPSInstanceConfWTRTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Mgs360024fERPSInstanceConfWTRTime_Type.__name__ = "Integer32"
_Mgs360024fERPSInstanceConfWTRTime_Object = MibTableColumn
mgs360024fERPSInstanceConfWTRTime = _Mgs360024fERPSInstanceConfWTRTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 16),
    _Mgs360024fERPSInstanceConfWTRTime_Type()
)
mgs360024fERPSInstanceConfWTRTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSInstanceConfWTRTime.setStatus("current")


class _Mgs360024fERPSInstanceConfHoldOffTime_Type(Integer32):
    """Custom type mgs360024fERPSInstanceConfHoldOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Mgs360024fERPSInstanceConfHoldOffTime_Type.__name__ = "Integer32"
_Mgs360024fERPSInstanceConfHoldOffTime_Object = MibTableColumn
mgs360024fERPSInstanceConfHoldOffTime = _Mgs360024fERPSInstanceConfHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 17),
    _Mgs360024fERPSInstanceConfHoldOffTime_Type()
)
mgs360024fERPSInstanceConfHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSInstanceConfHoldOffTime.setStatus("current")


class _Mgs360024fERPSInstanceConfVersion_Type(Integer32):
    """Custom type mgs360024fERPSInstanceConfVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fERPSInstanceConfVersion_Type.__name__ = "Integer32"
_Mgs360024fERPSInstanceConfVersion_Object = MibTableColumn
mgs360024fERPSInstanceConfVersion = _Mgs360024fERPSInstanceConfVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 18),
    _Mgs360024fERPSInstanceConfVersion_Type()
)
mgs360024fERPSInstanceConfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSInstanceConfVersion.setStatus("current")


class _Mgs360024fERPSInstanceConfRevertive_Type(Integer32):
    """Custom type mgs360024fERPSInstanceConfRevertive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fERPSInstanceConfRevertive_Type.__name__ = "Integer32"
_Mgs360024fERPSInstanceConfRevertive_Object = MibTableColumn
mgs360024fERPSInstanceConfRevertive = _Mgs360024fERPSInstanceConfRevertive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 19),
    _Mgs360024fERPSInstanceConfRevertive_Type()
)
mgs360024fERPSInstanceConfRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSInstanceConfRevertive.setStatus("current")


class _Mgs360024fERPSInstanceConfVLANconfig_Type(DisplayString):
    """Custom type mgs360024fERPSInstanceConfVLANconfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Mgs360024fERPSInstanceConfVLANconfig_Type.__name__ = "DisplayString"
_Mgs360024fERPSInstanceConfVLANconfig_Object = MibTableColumn
mgs360024fERPSInstanceConfVLANconfig = _Mgs360024fERPSInstanceConfVLANconfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 20),
    _Mgs360024fERPSInstanceConfVLANconfig_Type()
)
mgs360024fERPSInstanceConfVLANconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSInstanceConfVLANconfig.setStatus("current")


class _Mgs360024fERPSConfRowStatus_Type(Integer32):
    """Custom type mgs360024fERPSConfRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Mgs360024fERPSConfRowStatus_Type.__name__ = "Integer32"
_Mgs360024fERPSConfRowStatus_Object = MibTableColumn
mgs360024fERPSConfRowStatus = _Mgs360024fERPSConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 10, 1, 2, 1, 21),
    _Mgs360024fERPSConfRowStatus_Type()
)
mgs360024fERPSConfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fERPSConfRowStatus.setStatus("current")
_Mgs360024fMRSTP_ObjectIdentity = ObjectIdentity
mgs360024fMRSTP = _Mgs360024fMRSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11)
)
_Mgs360024fMRSTPInstance_ObjectIdentity = ObjectIdentity
mgs360024fMRSTPInstance = _Mgs360024fMRSTPInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1)
)
_Mgs360024fMRSTPInstanceConf_ObjectIdentity = ObjectIdentity
mgs360024fMRSTPInstanceConf = _Mgs360024fMRSTPInstanceConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 1)
)


class _Mgs360024fMRSTPInstanceConfGlobalState_Type(Integer32):
    """Custom type mgs360024fMRSTPInstanceConfGlobalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fMRSTPInstanceConfGlobalState_Type.__name__ = "Integer32"
_Mgs360024fMRSTPInstanceConfGlobalState_Object = MibScalar
mgs360024fMRSTPInstanceConfGlobalState = _Mgs360024fMRSTPInstanceConfGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 1, 1),
    _Mgs360024fMRSTPInstanceConfGlobalState_Type()
)
mgs360024fMRSTPInstanceConfGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceConfGlobalState.setStatus("current")
_Mgs360024fMRSTPInstanceConfigurationTable_Object = MibTable
mgs360024fMRSTPInstanceConfigurationTable = _Mgs360024fMRSTPInstanceConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceConfigurationTable.setStatus("current")
_Mgs360024fMRSTPInstanceConfigurationEntry_Object = MibTableRow
mgs360024fMRSTPInstanceConfigurationEntry = _Mgs360024fMRSTPInstanceConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 1, 2, 1)
)
mgs360024fMRSTPInstanceConfigurationEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fMRSTPInstanceConfigurationInstance"),
)
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceConfigurationEntry.setStatus("current")


class _Mgs360024fMRSTPInstanceConfigurationInstance_Type(Integer32):
    """Custom type mgs360024fMRSTPInstanceConfigurationInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Mgs360024fMRSTPInstanceConfigurationInstance_Type.__name__ = "Integer32"
_Mgs360024fMRSTPInstanceConfigurationInstance_Object = MibTableColumn
mgs360024fMRSTPInstanceConfigurationInstance = _Mgs360024fMRSTPInstanceConfigurationInstance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 1, 2, 1, 1),
    _Mgs360024fMRSTPInstanceConfigurationInstance_Type()
)
mgs360024fMRSTPInstanceConfigurationInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceConfigurationInstance.setStatus("current")


class _Mgs360024fMRSTPInstanceConfigurationState_Type(Integer32):
    """Custom type mgs360024fMRSTPInstanceConfigurationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fMRSTPInstanceConfigurationState_Type.__name__ = "Integer32"
_Mgs360024fMRSTPInstanceConfigurationState_Object = MibTableColumn
mgs360024fMRSTPInstanceConfigurationState = _Mgs360024fMRSTPInstanceConfigurationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 1, 2, 1, 2),
    _Mgs360024fMRSTPInstanceConfigurationState_Type()
)
mgs360024fMRSTPInstanceConfigurationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceConfigurationState.setStatus("current")


class _Mgs360024fMRSTPInstanceConfigurationVersion_Type(Integer32):
    """Custom type mgs360024fMRSTPInstanceConfigurationVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fMRSTPInstanceConfigurationVersion_Type.__name__ = "Integer32"
_Mgs360024fMRSTPInstanceConfigurationVersion_Object = MibTableColumn
mgs360024fMRSTPInstanceConfigurationVersion = _Mgs360024fMRSTPInstanceConfigurationVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 1, 2, 1, 3),
    _Mgs360024fMRSTPInstanceConfigurationVersion_Type()
)
mgs360024fMRSTPInstanceConfigurationVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceConfigurationVersion.setStatus("current")


class _Mgs360024fMRSTPInstanceConfigurationPriority_Type(Integer32):
    """Custom type mgs360024fMRSTPInstanceConfigurationPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Mgs360024fMRSTPInstanceConfigurationPriority_Type.__name__ = "Integer32"
_Mgs360024fMRSTPInstanceConfigurationPriority_Object = MibTableColumn
mgs360024fMRSTPInstanceConfigurationPriority = _Mgs360024fMRSTPInstanceConfigurationPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 1, 2, 1, 4),
    _Mgs360024fMRSTPInstanceConfigurationPriority_Type()
)
mgs360024fMRSTPInstanceConfigurationPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceConfigurationPriority.setStatus("current")


class _Mgs360024fMRSTPInstanceConfigurationHelloTime_Type(Integer32):
    """Custom type mgs360024fMRSTPInstanceConfigurationHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Mgs360024fMRSTPInstanceConfigurationHelloTime_Type.__name__ = "Integer32"
_Mgs360024fMRSTPInstanceConfigurationHelloTime_Object = MibTableColumn
mgs360024fMRSTPInstanceConfigurationHelloTime = _Mgs360024fMRSTPInstanceConfigurationHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 1, 2, 1, 5),
    _Mgs360024fMRSTPInstanceConfigurationHelloTime_Type()
)
mgs360024fMRSTPInstanceConfigurationHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceConfigurationHelloTime.setStatus("current")


class _Mgs360024fMRSTPInstanceConfigurationMaxAge_Type(Integer32):
    """Custom type mgs360024fMRSTPInstanceConfigurationMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Mgs360024fMRSTPInstanceConfigurationMaxAge_Type.__name__ = "Integer32"
_Mgs360024fMRSTPInstanceConfigurationMaxAge_Object = MibTableColumn
mgs360024fMRSTPInstanceConfigurationMaxAge = _Mgs360024fMRSTPInstanceConfigurationMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 1, 2, 1, 6),
    _Mgs360024fMRSTPInstanceConfigurationMaxAge_Type()
)
mgs360024fMRSTPInstanceConfigurationMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceConfigurationMaxAge.setStatus("current")


class _Mgs360024fMRSTPInstanceConfigurationFWDelay_Type(Integer32):
    """Custom type mgs360024fMRSTPInstanceConfigurationFWDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_Mgs360024fMRSTPInstanceConfigurationFWDelay_Type.__name__ = "Integer32"
_Mgs360024fMRSTPInstanceConfigurationFWDelay_Object = MibTableColumn
mgs360024fMRSTPInstanceConfigurationFWDelay = _Mgs360024fMRSTPInstanceConfigurationFWDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 1, 2, 1, 7),
    _Mgs360024fMRSTPInstanceConfigurationFWDelay_Type()
)
mgs360024fMRSTPInstanceConfigurationFWDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceConfigurationFWDelay.setStatus("current")
_Mgs360024fMRSTPInstanceStatus_ObjectIdentity = ObjectIdentity
mgs360024fMRSTPInstanceStatus = _Mgs360024fMRSTPInstanceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 2)
)
_Mgs360024fMRSTPInstanceStatusTable_Object = MibTable
mgs360024fMRSTPInstanceStatusTable = _Mgs360024fMRSTPInstanceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceStatusTable.setStatus("current")
_Mgs360024fMRSTPInstanceStatusEntry_Object = MibTableRow
mgs360024fMRSTPInstanceStatusEntry = _Mgs360024fMRSTPInstanceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 2, 1, 1)
)
mgs360024fMRSTPInstanceStatusEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fMRSTPInstanceStatusInstance"),
)
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceStatusEntry.setStatus("current")


class _Mgs360024fMRSTPInstanceStatusInstance_Type(Integer32):
    """Custom type mgs360024fMRSTPInstanceStatusInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Mgs360024fMRSTPInstanceStatusInstance_Type.__name__ = "Integer32"
_Mgs360024fMRSTPInstanceStatusInstance_Object = MibTableColumn
mgs360024fMRSTPInstanceStatusInstance = _Mgs360024fMRSTPInstanceStatusInstance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 2, 1, 1, 1),
    _Mgs360024fMRSTPInstanceStatusInstance_Type()
)
mgs360024fMRSTPInstanceStatusInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceStatusInstance.setStatus("current")


class _Mgs360024fMRSTPInstanceStatusGlobalState_Type(Integer32):
    """Custom type mgs360024fMRSTPInstanceStatusGlobalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fMRSTPInstanceStatusGlobalState_Type.__name__ = "Integer32"
_Mgs360024fMRSTPInstanceStatusGlobalState_Object = MibTableColumn
mgs360024fMRSTPInstanceStatusGlobalState = _Mgs360024fMRSTPInstanceStatusGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 2, 1, 1, 2),
    _Mgs360024fMRSTPInstanceStatusGlobalState_Type()
)
mgs360024fMRSTPInstanceStatusGlobalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceStatusGlobalState.setStatus("current")


class _Mgs360024fMRSTPInstanceStatusInstanceConfigState_Type(Integer32):
    """Custom type mgs360024fMRSTPInstanceStatusInstanceConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fMRSTPInstanceStatusInstanceConfigState_Type.__name__ = "Integer32"
_Mgs360024fMRSTPInstanceStatusInstanceConfigState_Object = MibTableColumn
mgs360024fMRSTPInstanceStatusInstanceConfigState = _Mgs360024fMRSTPInstanceStatusInstanceConfigState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 2, 1, 1, 3),
    _Mgs360024fMRSTPInstanceStatusInstanceConfigState_Type()
)
mgs360024fMRSTPInstanceStatusInstanceConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceStatusInstanceConfigState.setStatus("current")


class _Mgs360024fMRSTPInstanceStatusInstanceCurrentState_Type(Integer32):
    """Custom type mgs360024fMRSTPInstanceStatusInstanceCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fMRSTPInstanceStatusInstanceCurrentState_Type.__name__ = "Integer32"
_Mgs360024fMRSTPInstanceStatusInstanceCurrentState_Object = MibTableColumn
mgs360024fMRSTPInstanceStatusInstanceCurrentState = _Mgs360024fMRSTPInstanceStatusInstanceCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 2, 1, 1, 4),
    _Mgs360024fMRSTPInstanceStatusInstanceCurrentState_Type()
)
mgs360024fMRSTPInstanceStatusInstanceCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceStatusInstanceCurrentState.setStatus("current")
_Mgs360024fMRSTPInstanceStatusBridgeID_Type = MacAddress
_Mgs360024fMRSTPInstanceStatusBridgeID_Object = MibTableColumn
mgs360024fMRSTPInstanceStatusBridgeID = _Mgs360024fMRSTPInstanceStatusBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 2, 1, 1, 5),
    _Mgs360024fMRSTPInstanceStatusBridgeID_Type()
)
mgs360024fMRSTPInstanceStatusBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceStatusBridgeID.setStatus("current")


class _Mgs360024fMRSTPInstanceStatusBridgePrioriry_Type(Integer32):
    """Custom type mgs360024fMRSTPInstanceStatusBridgePrioriry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Mgs360024fMRSTPInstanceStatusBridgePrioriry_Type.__name__ = "Integer32"
_Mgs360024fMRSTPInstanceStatusBridgePrioriry_Object = MibTableColumn
mgs360024fMRSTPInstanceStatusBridgePrioriry = _Mgs360024fMRSTPInstanceStatusBridgePrioriry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 2, 1, 1, 6),
    _Mgs360024fMRSTPInstanceStatusBridgePrioriry_Type()
)
mgs360024fMRSTPInstanceStatusBridgePrioriry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceStatusBridgePrioriry.setStatus("current")
_Mgs360024fMRSTPInstanceStatusRootID_Type = MacAddress
_Mgs360024fMRSTPInstanceStatusRootID_Object = MibTableColumn
mgs360024fMRSTPInstanceStatusRootID = _Mgs360024fMRSTPInstanceStatusRootID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 2, 1, 1, 7),
    _Mgs360024fMRSTPInstanceStatusRootID_Type()
)
mgs360024fMRSTPInstanceStatusRootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceStatusRootID.setStatus("current")


class _Mgs360024fMRSTPInstanceStatusRootPriority_Type(Integer32):
    """Custom type mgs360024fMRSTPInstanceStatusRootPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Mgs360024fMRSTPInstanceStatusRootPriority_Type.__name__ = "Integer32"
_Mgs360024fMRSTPInstanceStatusRootPriority_Object = MibTableColumn
mgs360024fMRSTPInstanceStatusRootPriority = _Mgs360024fMRSTPInstanceStatusRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 2, 1, 1, 8),
    _Mgs360024fMRSTPInstanceStatusRootPriority_Type()
)
mgs360024fMRSTPInstanceStatusRootPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceStatusRootPriority.setStatus("current")
_Mgs360024fMRSTPInstanceStatusRootPort_Type = Integer32
_Mgs360024fMRSTPInstanceStatusRootPort_Object = MibTableColumn
mgs360024fMRSTPInstanceStatusRootPort = _Mgs360024fMRSTPInstanceStatusRootPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 2, 1, 1, 9),
    _Mgs360024fMRSTPInstanceStatusRootPort_Type()
)
mgs360024fMRSTPInstanceStatusRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceStatusRootPort.setStatus("current")
_Mgs360024fMRSTPInstanceStatusRootPathCost_Type = Integer32
_Mgs360024fMRSTPInstanceStatusRootPathCost_Object = MibTableColumn
mgs360024fMRSTPInstanceStatusRootPathCost = _Mgs360024fMRSTPInstanceStatusRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 2, 1, 1, 10),
    _Mgs360024fMRSTPInstanceStatusRootPathCost_Type()
)
mgs360024fMRSTPInstanceStatusRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceStatusRootPathCost.setStatus("current")


class _Mgs360024fMRSTPInstanceStatusCurrentMaxAge_Type(Integer32):
    """Custom type mgs360024fMRSTPInstanceStatusCurrentMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Mgs360024fMRSTPInstanceStatusCurrentMaxAge_Type.__name__ = "Integer32"
_Mgs360024fMRSTPInstanceStatusCurrentMaxAge_Object = MibTableColumn
mgs360024fMRSTPInstanceStatusCurrentMaxAge = _Mgs360024fMRSTPInstanceStatusCurrentMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 2, 1, 1, 11),
    _Mgs360024fMRSTPInstanceStatusCurrentMaxAge_Type()
)
mgs360024fMRSTPInstanceStatusCurrentMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceStatusCurrentMaxAge.setStatus("current")


class _Mgs360024fMRSTPInstanceStatusCurrentForwardDelay_Type(Integer32):
    """Custom type mgs360024fMRSTPInstanceStatusCurrentForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_Mgs360024fMRSTPInstanceStatusCurrentForwardDelay_Type.__name__ = "Integer32"
_Mgs360024fMRSTPInstanceStatusCurrentForwardDelay_Object = MibTableColumn
mgs360024fMRSTPInstanceStatusCurrentForwardDelay = _Mgs360024fMRSTPInstanceStatusCurrentForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 2, 1, 1, 12),
    _Mgs360024fMRSTPInstanceStatusCurrentForwardDelay_Type()
)
mgs360024fMRSTPInstanceStatusCurrentForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceStatusCurrentForwardDelay.setStatus("current")


class _Mgs360024fMRSTPInstanceStatusHelloTime_Type(Integer32):
    """Custom type mgs360024fMRSTPInstanceStatusHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Mgs360024fMRSTPInstanceStatusHelloTime_Type.__name__ = "Integer32"
_Mgs360024fMRSTPInstanceStatusHelloTime_Object = MibTableColumn
mgs360024fMRSTPInstanceStatusHelloTime = _Mgs360024fMRSTPInstanceStatusHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 2, 1, 1, 13),
    _Mgs360024fMRSTPInstanceStatusHelloTime_Type()
)
mgs360024fMRSTPInstanceStatusHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceStatusHelloTime.setStatus("current")
_Mgs360024fMRSTPInstanceStatusTopologyChangeCount_Type = Integer32
_Mgs360024fMRSTPInstanceStatusTopologyChangeCount_Object = MibTableColumn
mgs360024fMRSTPInstanceStatusTopologyChangeCount = _Mgs360024fMRSTPInstanceStatusTopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 2, 1, 1, 14),
    _Mgs360024fMRSTPInstanceStatusTopologyChangeCount_Type()
)
mgs360024fMRSTPInstanceStatusTopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceStatusTopologyChangeCount.setStatus("current")
_Mgs360024fMRSTPInstanceStatusTimeSinceLastTopologyChange_Type = Integer32
_Mgs360024fMRSTPInstanceStatusTimeSinceLastTopologyChange_Object = MibTableColumn
mgs360024fMRSTPInstanceStatusTimeSinceLastTopologyChange = _Mgs360024fMRSTPInstanceStatusTimeSinceLastTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 1, 2, 1, 1, 15),
    _Mgs360024fMRSTPInstanceStatusTimeSinceLastTopologyChange_Type()
)
mgs360024fMRSTPInstanceStatusTimeSinceLastTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPInstanceStatusTimeSinceLastTopologyChange.setStatus("current")
_Mgs360024fMRSTPPort_ObjectIdentity = ObjectIdentity
mgs360024fMRSTPPort = _Mgs360024fMRSTPPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2)
)
_Mgs360024fMRSTPPortConfiguration_ObjectIdentity = ObjectIdentity
mgs360024fMRSTPPortConfiguration = _Mgs360024fMRSTPPortConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 1)
)
_Mgs360024fMRSTPPortConfigurationTable_Object = MibTable
mgs360024fMRSTPPortConfigurationTable = _Mgs360024fMRSTPPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortConfigurationTable.setStatus("current")
_Mgs360024fMRSTPPortConfigurationEntry_Object = MibTableRow
mgs360024fMRSTPPortConfigurationEntry = _Mgs360024fMRSTPPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 1, 1, 1)
)
mgs360024fMRSTPPortConfigurationEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fMRSTPPortConfigurationPort"),
)
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortConfigurationEntry.setStatus("current")


class _Mgs360024fMRSTPPortConfigurationPort_Type(Integer32):
    """Custom type mgs360024fMRSTPPortConfigurationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fMRSTPPortConfigurationPort_Type.__name__ = "Integer32"
_Mgs360024fMRSTPPortConfigurationPort_Object = MibTableColumn
mgs360024fMRSTPPortConfigurationPort = _Mgs360024fMRSTPPortConfigurationPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 1, 1, 1, 1),
    _Mgs360024fMRSTPPortConfigurationPort_Type()
)
mgs360024fMRSTPPortConfigurationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortConfigurationPort.setStatus("current")


class _Mgs360024fMRSTPPortConfigurationInstance_Type(Integer32):
    """Custom type mgs360024fMRSTPPortConfigurationInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Mgs360024fMRSTPPortConfigurationInstance_Type.__name__ = "Integer32"
_Mgs360024fMRSTPPortConfigurationInstance_Object = MibTableColumn
mgs360024fMRSTPPortConfigurationInstance = _Mgs360024fMRSTPPortConfigurationInstance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 1, 1, 1, 2),
    _Mgs360024fMRSTPPortConfigurationInstance_Type()
)
mgs360024fMRSTPPortConfigurationInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortConfigurationInstance.setStatus("current")


class _Mgs360024fMRSTPPortConfigurationPathCost_Type(Integer32):
    """Custom type mgs360024fMRSTPPortConfigurationPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Mgs360024fMRSTPPortConfigurationPathCost_Type.__name__ = "Integer32"
_Mgs360024fMRSTPPortConfigurationPathCost_Object = MibTableColumn
mgs360024fMRSTPPortConfigurationPathCost = _Mgs360024fMRSTPPortConfigurationPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 1, 1, 1, 3),
    _Mgs360024fMRSTPPortConfigurationPathCost_Type()
)
mgs360024fMRSTPPortConfigurationPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortConfigurationPathCost.setStatus("current")


class _Mgs360024fMRSTPPortConfigurationPriority_Type(Integer32):
    """Custom type mgs360024fMRSTPPortConfigurationPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Mgs360024fMRSTPPortConfigurationPriority_Type.__name__ = "Integer32"
_Mgs360024fMRSTPPortConfigurationPriority_Object = MibTableColumn
mgs360024fMRSTPPortConfigurationPriority = _Mgs360024fMRSTPPortConfigurationPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 1, 1, 1, 4),
    _Mgs360024fMRSTPPortConfigurationPriority_Type()
)
mgs360024fMRSTPPortConfigurationPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortConfigurationPriority.setStatus("current")


class _Mgs360024fMRSTPPortConfigurationAdminEdge_Type(Integer32):
    """Custom type mgs360024fMRSTPPortConfigurationAdminEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fMRSTPPortConfigurationAdminEdge_Type.__name__ = "Integer32"
_Mgs360024fMRSTPPortConfigurationAdminEdge_Object = MibTableColumn
mgs360024fMRSTPPortConfigurationAdminEdge = _Mgs360024fMRSTPPortConfigurationAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 1, 1, 1, 5),
    _Mgs360024fMRSTPPortConfigurationAdminEdge_Type()
)
mgs360024fMRSTPPortConfigurationAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortConfigurationAdminEdge.setStatus("current")


class _Mgs360024fMRSTPPortConfigurationAdminP2P_Type(Integer32):
    """Custom type mgs360024fMRSTPPortConfigurationAdminP2P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mgs360024fMRSTPPortConfigurationAdminP2P_Type.__name__ = "Integer32"
_Mgs360024fMRSTPPortConfigurationAdminP2P_Object = MibTableColumn
mgs360024fMRSTPPortConfigurationAdminP2P = _Mgs360024fMRSTPPortConfigurationAdminP2P_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 1, 1, 1, 6),
    _Mgs360024fMRSTPPortConfigurationAdminP2P_Type()
)
mgs360024fMRSTPPortConfigurationAdminP2P.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortConfigurationAdminP2P.setStatus("current")


class _Mgs360024fMRSTPPortConfigurationMigrateCheck_Type(Integer32):
    """Custom type mgs360024fMRSTPPortConfigurationMigrateCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fMRSTPPortConfigurationMigrateCheck_Type.__name__ = "Integer32"
_Mgs360024fMRSTPPortConfigurationMigrateCheck_Object = MibTableColumn
mgs360024fMRSTPPortConfigurationMigrateCheck = _Mgs360024fMRSTPPortConfigurationMigrateCheck_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 1, 1, 1, 7),
    _Mgs360024fMRSTPPortConfigurationMigrateCheck_Type()
)
mgs360024fMRSTPPortConfigurationMigrateCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortConfigurationMigrateCheck.setStatus("current")
_Mgs360024fMRSTPPortStatus_ObjectIdentity = ObjectIdentity
mgs360024fMRSTPPortStatus = _Mgs360024fMRSTPPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 2)
)
_Mgs360024fMRSTPPortStatusTable_Object = MibTable
mgs360024fMRSTPPortStatusTable = _Mgs360024fMRSTPPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortStatusTable.setStatus("current")
_Mgs360024fMRSTPPortStatusEntry_Object = MibTableRow
mgs360024fMRSTPPortStatusEntry = _Mgs360024fMRSTPPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 2, 1, 1)
)
mgs360024fMRSTPPortStatusEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fMRSTPPortStatusPort"),
)
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortStatusEntry.setStatus("current")


class _Mgs360024fMRSTPPortStatusPort_Type(Integer32):
    """Custom type mgs360024fMRSTPPortStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fMRSTPPortStatusPort_Type.__name__ = "Integer32"
_Mgs360024fMRSTPPortStatusPort_Object = MibTableColumn
mgs360024fMRSTPPortStatusPort = _Mgs360024fMRSTPPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 2, 1, 1, 1),
    _Mgs360024fMRSTPPortStatusPort_Type()
)
mgs360024fMRSTPPortStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortStatusPort.setStatus("current")
_Mgs360024fMRSTPPortStatusInstance_Type = DisplayString
_Mgs360024fMRSTPPortStatusInstance_Object = MibTableColumn
mgs360024fMRSTPPortStatusInstance = _Mgs360024fMRSTPPortStatusInstance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 2, 1, 1, 2),
    _Mgs360024fMRSTPPortStatusInstance_Type()
)
mgs360024fMRSTPPortStatusInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortStatusInstance.setStatus("current")
_Mgs360024fMRSTPPortStatusState_Type = DisplayString
_Mgs360024fMRSTPPortStatusState_Object = MibTableColumn
mgs360024fMRSTPPortStatusState = _Mgs360024fMRSTPPortStatusState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 2, 1, 1, 3),
    _Mgs360024fMRSTPPortStatusState_Type()
)
mgs360024fMRSTPPortStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortStatusState.setStatus("current")
_Mgs360024fMRSTPPortStatusRole_Type = DisplayString
_Mgs360024fMRSTPPortStatusRole_Object = MibTableColumn
mgs360024fMRSTPPortStatusRole = _Mgs360024fMRSTPPortStatusRole_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 2, 1, 1, 4),
    _Mgs360024fMRSTPPortStatusRole_Type()
)
mgs360024fMRSTPPortStatusRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortStatusRole.setStatus("current")


class _Mgs360024fMRSTPPortStatusPathCost_Type(Integer32):
    """Custom type mgs360024fMRSTPPortStatusPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Mgs360024fMRSTPPortStatusPathCost_Type.__name__ = "Integer32"
_Mgs360024fMRSTPPortStatusPathCost_Object = MibTableColumn
mgs360024fMRSTPPortStatusPathCost = _Mgs360024fMRSTPPortStatusPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 2, 1, 1, 5),
    _Mgs360024fMRSTPPortStatusPathCost_Type()
)
mgs360024fMRSTPPortStatusPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortStatusPathCost.setStatus("current")


class _Mgs360024fMRSTPPortStatusPathCostConfig_Type(Integer32):
    """Custom type mgs360024fMRSTPPortStatusPathCostConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Mgs360024fMRSTPPortStatusPathCostConfig_Type.__name__ = "Integer32"
_Mgs360024fMRSTPPortStatusPathCostConfig_Object = MibTableColumn
mgs360024fMRSTPPortStatusPathCostConfig = _Mgs360024fMRSTPPortStatusPathCostConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 2, 1, 1, 6),
    _Mgs360024fMRSTPPortStatusPathCostConfig_Type()
)
mgs360024fMRSTPPortStatusPathCostConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortStatusPathCostConfig.setStatus("current")


class _Mgs360024fMRSTPPortStatusPriority_Type(Integer32):
    """Custom type mgs360024fMRSTPPortStatusPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Mgs360024fMRSTPPortStatusPriority_Type.__name__ = "Integer32"
_Mgs360024fMRSTPPortStatusPriority_Object = MibTableColumn
mgs360024fMRSTPPortStatusPriority = _Mgs360024fMRSTPPortStatusPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 2, 1, 1, 7),
    _Mgs360024fMRSTPPortStatusPriority_Type()
)
mgs360024fMRSTPPortStatusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortStatusPriority.setStatus("current")
_Mgs360024fMRSTPPortStatusAdminEdge_Type = DisplayString
_Mgs360024fMRSTPPortStatusAdminEdge_Object = MibTableColumn
mgs360024fMRSTPPortStatusAdminEdge = _Mgs360024fMRSTPPortStatusAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 2, 1, 1, 8),
    _Mgs360024fMRSTPPortStatusAdminEdge_Type()
)
mgs360024fMRSTPPortStatusAdminEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortStatusAdminEdge.setStatus("current")
_Mgs360024fMRSTPPortStatusAdminP2P_Type = DisplayString
_Mgs360024fMRSTPPortStatusAdminP2P_Object = MibTableColumn
mgs360024fMRSTPPortStatusAdminP2P = _Mgs360024fMRSTPPortStatusAdminP2P_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 2, 11, 2, 2, 1, 1, 9),
    _Mgs360024fMRSTPPortStatusAdminP2P_Type()
)
mgs360024fMRSTPPortStatusAdminP2P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fMRSTPPortStatusAdminP2P.setStatus("current")
_Mgs360024fSecurity_ObjectIdentity = ObjectIdentity
mgs360024fSecurity = _Mgs360024fSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3)
)
_Mgs360024fIPSourceGuard_ObjectIdentity = ObjectIdentity
mgs360024fIPSourceGuard = _Mgs360024fIPSourceGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1)
)
_Mgs360024fIPSourceGuardConf_ObjectIdentity = ObjectIdentity
mgs360024fIPSourceGuardConf = _Mgs360024fIPSourceGuardConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 1)
)


class _Mgs360024fIPSourceGuardMode_Type(Integer32):
    """Custom type mgs360024fIPSourceGuardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fIPSourceGuardMode_Type.__name__ = "Integer32"
_Mgs360024fIPSourceGuardMode_Object = MibScalar
mgs360024fIPSourceGuardMode = _Mgs360024fIPSourceGuardMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 1, 1),
    _Mgs360024fIPSourceGuardMode_Type()
)
mgs360024fIPSourceGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardMode.setStatus("current")
_Mgs360024fIPSourceGuardPortConfigTable_Object = MibTable
mgs360024fIPSourceGuardPortConfigTable = _Mgs360024fIPSourceGuardPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardPortConfigTable.setStatus("current")
_Mgs360024fIPSourceGuardPortConfigEntry_Object = MibTableRow
mgs360024fIPSourceGuardPortConfigEntry = _Mgs360024fIPSourceGuardPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 1, 2, 1)
)
mgs360024fIPSourceGuardPortConfigEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fIPSourceGuardPortConfigPort"),
)
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardPortConfigEntry.setStatus("current")


class _Mgs360024fIPSourceGuardPortConfigPort_Type(Integer32):
    """Custom type mgs360024fIPSourceGuardPortConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fIPSourceGuardPortConfigPort_Type.__name__ = "Integer32"
_Mgs360024fIPSourceGuardPortConfigPort_Object = MibTableColumn
mgs360024fIPSourceGuardPortConfigPort = _Mgs360024fIPSourceGuardPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 1, 2, 1, 1),
    _Mgs360024fIPSourceGuardPortConfigPort_Type()
)
mgs360024fIPSourceGuardPortConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardPortConfigPort.setStatus("current")


class _Mgs360024fIPSourceGuardPortConfigMode_Type(Integer32):
    """Custom type mgs360024fIPSourceGuardPortConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fIPSourceGuardPortConfigMode_Type.__name__ = "Integer32"
_Mgs360024fIPSourceGuardPortConfigMode_Object = MibTableColumn
mgs360024fIPSourceGuardPortConfigMode = _Mgs360024fIPSourceGuardPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 1, 2, 1, 2),
    _Mgs360024fIPSourceGuardPortConfigMode_Type()
)
mgs360024fIPSourceGuardPortConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardPortConfigMode.setStatus("current")


class _Mgs360024fIPSourceGuardPortMaxDynamicClients_Type(Integer32):
    """Custom type mgs360024fIPSourceGuardPortMaxDynamicClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(99, 99),
    )


_Mgs360024fIPSourceGuardPortMaxDynamicClients_Type.__name__ = "Integer32"
_Mgs360024fIPSourceGuardPortMaxDynamicClients_Object = MibTableColumn
mgs360024fIPSourceGuardPortMaxDynamicClients = _Mgs360024fIPSourceGuardPortMaxDynamicClients_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 1, 2, 1, 3),
    _Mgs360024fIPSourceGuardPortMaxDynamicClients_Type()
)
mgs360024fIPSourceGuardPortMaxDynamicClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardPortMaxDynamicClients.setStatus("current")
_Mgs360024fIPSourceGuardStatic_ObjectIdentity = ObjectIdentity
mgs360024fIPSourceGuardStatic = _Mgs360024fIPSourceGuardStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 2)
)


class _Mgs360024fIPSourceGuardStaticCreate_Type(Integer32):
    """Custom type mgs360024fIPSourceGuardStaticCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fIPSourceGuardStaticCreate_Type.__name__ = "Integer32"
_Mgs360024fIPSourceGuardStaticCreate_Object = MibScalar
mgs360024fIPSourceGuardStaticCreate = _Mgs360024fIPSourceGuardStaticCreate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 2, 1),
    _Mgs360024fIPSourceGuardStaticCreate_Type()
)
mgs360024fIPSourceGuardStaticCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardStaticCreate.setStatus("current")
_Mgs360024fIPSourceGuardStaticTable_Object = MibTable
mgs360024fIPSourceGuardStaticTable = _Mgs360024fIPSourceGuardStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardStaticTable.setStatus("current")
_Mgs360024fIPSourceGuardStaticEntry_Object = MibTableRow
mgs360024fIPSourceGuardStaticEntry = _Mgs360024fIPSourceGuardStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 2, 2, 1)
)
mgs360024fIPSourceGuardStaticEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fIPSourceGuardStaticIndex"),
)
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardStaticEntry.setStatus("current")


class _Mgs360024fIPSourceGuardStaticIndex_Type(Integer32):
    """Custom type mgs360024fIPSourceGuardStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_Mgs360024fIPSourceGuardStaticIndex_Type.__name__ = "Integer32"
_Mgs360024fIPSourceGuardStaticIndex_Object = MibTableColumn
mgs360024fIPSourceGuardStaticIndex = _Mgs360024fIPSourceGuardStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 2, 2, 1, 1),
    _Mgs360024fIPSourceGuardStaticIndex_Type()
)
mgs360024fIPSourceGuardStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardStaticIndex.setStatus("current")


class _Mgs360024fIPSourceGuardStaticPort_Type(Integer32):
    """Custom type mgs360024fIPSourceGuardStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fIPSourceGuardStaticPort_Type.__name__ = "Integer32"
_Mgs360024fIPSourceGuardStaticPort_Object = MibTableColumn
mgs360024fIPSourceGuardStaticPort = _Mgs360024fIPSourceGuardStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 2, 2, 1, 2),
    _Mgs360024fIPSourceGuardStaticPort_Type()
)
mgs360024fIPSourceGuardStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardStaticPort.setStatus("current")


class _Mgs360024fIPSourceGuardStaticVLANId_Type(Integer32):
    """Custom type mgs360024fIPSourceGuardStaticVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Mgs360024fIPSourceGuardStaticVLANId_Type.__name__ = "Integer32"
_Mgs360024fIPSourceGuardStaticVLANId_Object = MibTableColumn
mgs360024fIPSourceGuardStaticVLANId = _Mgs360024fIPSourceGuardStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 2, 2, 1, 3),
    _Mgs360024fIPSourceGuardStaticVLANId_Type()
)
mgs360024fIPSourceGuardStaticVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardStaticVLANId.setStatus("current")
_Mgs360024fIPSourceGuardStaticIPAddress_Type = IpAddress
_Mgs360024fIPSourceGuardStaticIPAddress_Object = MibTableColumn
mgs360024fIPSourceGuardStaticIPAddress = _Mgs360024fIPSourceGuardStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 2, 2, 1, 4),
    _Mgs360024fIPSourceGuardStaticIPAddress_Type()
)
mgs360024fIPSourceGuardStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardStaticIPAddress.setStatus("current")
_Mgs360024fIPSourceGuardStaticMACAddress_Type = MacAddress
_Mgs360024fIPSourceGuardStaticMACAddress_Object = MibTableColumn
mgs360024fIPSourceGuardStaticMACAddress = _Mgs360024fIPSourceGuardStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 2, 2, 1, 5),
    _Mgs360024fIPSourceGuardStaticMACAddress_Type()
)
mgs360024fIPSourceGuardStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardStaticMACAddress.setStatus("current")


class _Mgs360024fIPSourceGuardStaticRowStatus_Type(Integer32):
    """Custom type mgs360024fIPSourceGuardStaticRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Mgs360024fIPSourceGuardStaticRowStatus_Type.__name__ = "Integer32"
_Mgs360024fIPSourceGuardStaticRowStatus_Object = MibTableColumn
mgs360024fIPSourceGuardStaticRowStatus = _Mgs360024fIPSourceGuardStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 2, 2, 1, 6),
    _Mgs360024fIPSourceGuardStaticRowStatus_Type()
)
mgs360024fIPSourceGuardStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardStaticRowStatus.setStatus("current")
_Mgs360024fIPSourceGuardDynamicTable_Object = MibTable
mgs360024fIPSourceGuardDynamicTable = _Mgs360024fIPSourceGuardDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 3)
)
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardDynamicTable.setStatus("current")
_Mgs360024fIPSourceGuardDynamicEntry_Object = MibTableRow
mgs360024fIPSourceGuardDynamicEntry = _Mgs360024fIPSourceGuardDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 3, 1)
)
mgs360024fIPSourceGuardDynamicEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fIPSourceGuardDynamicIndex"),
)
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardDynamicEntry.setStatus("current")


class _Mgs360024fIPSourceGuardDynamicIndex_Type(Integer32):
    """Custom type mgs360024fIPSourceGuardDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fIPSourceGuardDynamicIndex_Type.__name__ = "Integer32"
_Mgs360024fIPSourceGuardDynamicIndex_Object = MibTableColumn
mgs360024fIPSourceGuardDynamicIndex = _Mgs360024fIPSourceGuardDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 3, 1, 1),
    _Mgs360024fIPSourceGuardDynamicIndex_Type()
)
mgs360024fIPSourceGuardDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardDynamicIndex.setStatus("current")


class _Mgs360024fIPSourceGuardDynamicPort_Type(Integer32):
    """Custom type mgs360024fIPSourceGuardDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Mgs360024fIPSourceGuardDynamicPort_Type.__name__ = "Integer32"
_Mgs360024fIPSourceGuardDynamicPort_Object = MibTableColumn
mgs360024fIPSourceGuardDynamicPort = _Mgs360024fIPSourceGuardDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 3, 1, 2),
    _Mgs360024fIPSourceGuardDynamicPort_Type()
)
mgs360024fIPSourceGuardDynamicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardDynamicPort.setStatus("current")


class _Mgs360024fIPSourceGuardDynamicVLANId_Type(Integer32):
    """Custom type mgs360024fIPSourceGuardDynamicVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Mgs360024fIPSourceGuardDynamicVLANId_Type.__name__ = "Integer32"
_Mgs360024fIPSourceGuardDynamicVLANId_Object = MibTableColumn
mgs360024fIPSourceGuardDynamicVLANId = _Mgs360024fIPSourceGuardDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 3, 1, 3),
    _Mgs360024fIPSourceGuardDynamicVLANId_Type()
)
mgs360024fIPSourceGuardDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardDynamicVLANId.setStatus("current")
_Mgs360024fIPSourceGuardDynamicIPAddress_Type = IpAddress
_Mgs360024fIPSourceGuardDynamicIPAddress_Object = MibTableColumn
mgs360024fIPSourceGuardDynamicIPAddress = _Mgs360024fIPSourceGuardDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 3, 1, 4),
    _Mgs360024fIPSourceGuardDynamicIPAddress_Type()
)
mgs360024fIPSourceGuardDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardDynamicIPAddress.setStatus("current")
_Mgs360024fIPSourceGuardDynamicMACAddress_Type = MacAddress
_Mgs360024fIPSourceGuardDynamicMACAddress_Object = MibTableColumn
mgs360024fIPSourceGuardDynamicMACAddress = _Mgs360024fIPSourceGuardDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 1, 3, 1, 5),
    _Mgs360024fIPSourceGuardDynamicMACAddress_Type()
)
mgs360024fIPSourceGuardDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fIPSourceGuardDynamicMACAddress.setStatus("current")
_Mgs360024fARPInspection_ObjectIdentity = ObjectIdentity
mgs360024fARPInspection = _Mgs360024fARPInspection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2)
)
_Mgs360024fARPInspectionConf_ObjectIdentity = ObjectIdentity
mgs360024fARPInspectionConf = _Mgs360024fARPInspectionConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 1)
)


class _Mgs360024fARPInspectionConfMode_Type(Integer32):
    """Custom type mgs360024fARPInspectionConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fARPInspectionConfMode_Type.__name__ = "Integer32"
_Mgs360024fARPInspectionConfMode_Object = MibScalar
mgs360024fARPInspectionConfMode = _Mgs360024fARPInspectionConfMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 1, 1),
    _Mgs360024fARPInspectionConfMode_Type()
)
mgs360024fARPInspectionConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fARPInspectionConfMode.setStatus("current")
_Mgs360024fARPInspectionConfTable_Object = MibTable
mgs360024fARPInspectionConfTable = _Mgs360024fARPInspectionConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mgs360024fARPInspectionConfTable.setStatus("current")
_Mgs360024fARPInspectionConfEntry_Object = MibTableRow
mgs360024fARPInspectionConfEntry = _Mgs360024fARPInspectionConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 1, 2, 1)
)
mgs360024fARPInspectionConfEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fARPInspectionConfPortIndex"),
)
if mibBuilder.loadTexts:
    mgs360024fARPInspectionConfEntry.setStatus("current")


class _Mgs360024fARPInspectionConfPortIndex_Type(Integer32):
    """Custom type mgs360024fARPInspectionConfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fARPInspectionConfPortIndex_Type.__name__ = "Integer32"
_Mgs360024fARPInspectionConfPortIndex_Object = MibTableColumn
mgs360024fARPInspectionConfPortIndex = _Mgs360024fARPInspectionConfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 1, 2, 1, 1),
    _Mgs360024fARPInspectionConfPortIndex_Type()
)
mgs360024fARPInspectionConfPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fARPInspectionConfPortIndex.setStatus("current")


class _Mgs360024fARPInspectionConfPortMode_Type(Integer32):
    """Custom type mgs360024fARPInspectionConfPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fARPInspectionConfPortMode_Type.__name__ = "Integer32"
_Mgs360024fARPInspectionConfPortMode_Object = MibTableColumn
mgs360024fARPInspectionConfPortMode = _Mgs360024fARPInspectionConfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 1, 2, 1, 2),
    _Mgs360024fARPInspectionConfPortMode_Type()
)
mgs360024fARPInspectionConfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fARPInspectionConfPortMode.setStatus("current")
_Mgs360024fARPInspectionStatic_ObjectIdentity = ObjectIdentity
mgs360024fARPInspectionStatic = _Mgs360024fARPInspectionStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 2)
)


class _Mgs360024fARPInspectionStaticCreate_Type(Integer32):
    """Custom type mgs360024fARPInspectionStaticCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fARPInspectionStaticCreate_Type.__name__ = "Integer32"
_Mgs360024fARPInspectionStaticCreate_Object = MibScalar
mgs360024fARPInspectionStaticCreate = _Mgs360024fARPInspectionStaticCreate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 2, 1),
    _Mgs360024fARPInspectionStaticCreate_Type()
)
mgs360024fARPInspectionStaticCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fARPInspectionStaticCreate.setStatus("current")
_Mgs360024fARPInspectionStaticTable_Object = MibTable
mgs360024fARPInspectionStaticTable = _Mgs360024fARPInspectionStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    mgs360024fARPInspectionStaticTable.setStatus("current")
_Mgs360024fARPInspectionStaticEntry_Object = MibTableRow
mgs360024fARPInspectionStaticEntry = _Mgs360024fARPInspectionStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 2, 2, 1)
)
mgs360024fARPInspectionStaticEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fARPInspectionStaticIndex"),
)
if mibBuilder.loadTexts:
    mgs360024fARPInspectionStaticEntry.setStatus("current")


class _Mgs360024fARPInspectionStaticIndex_Type(Integer32):
    """Custom type mgs360024fARPInspectionStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fARPInspectionStaticIndex_Type.__name__ = "Integer32"
_Mgs360024fARPInspectionStaticIndex_Object = MibTableColumn
mgs360024fARPInspectionStaticIndex = _Mgs360024fARPInspectionStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 2, 2, 1, 1),
    _Mgs360024fARPInspectionStaticIndex_Type()
)
mgs360024fARPInspectionStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fARPInspectionStaticIndex.setStatus("current")


class _Mgs360024fARPInspectionStaticPort_Type(Integer32):
    """Custom type mgs360024fARPInspectionStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fARPInspectionStaticPort_Type.__name__ = "Integer32"
_Mgs360024fARPInspectionStaticPort_Object = MibTableColumn
mgs360024fARPInspectionStaticPort = _Mgs360024fARPInspectionStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 2, 2, 1, 2),
    _Mgs360024fARPInspectionStaticPort_Type()
)
mgs360024fARPInspectionStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fARPInspectionStaticPort.setStatus("current")


class _Mgs360024fARPInspectionStaticVLANId_Type(Integer32):
    """Custom type mgs360024fARPInspectionStaticVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Mgs360024fARPInspectionStaticVLANId_Type.__name__ = "Integer32"
_Mgs360024fARPInspectionStaticVLANId_Object = MibTableColumn
mgs360024fARPInspectionStaticVLANId = _Mgs360024fARPInspectionStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 2, 2, 1, 3),
    _Mgs360024fARPInspectionStaticVLANId_Type()
)
mgs360024fARPInspectionStaticVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fARPInspectionStaticVLANId.setStatus("current")
_Mgs360024fARPInspectionStaticIPAddress_Type = IpAddress
_Mgs360024fARPInspectionStaticIPAddress_Object = MibTableColumn
mgs360024fARPInspectionStaticIPAddress = _Mgs360024fARPInspectionStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 2, 2, 1, 4),
    _Mgs360024fARPInspectionStaticIPAddress_Type()
)
mgs360024fARPInspectionStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fARPInspectionStaticIPAddress.setStatus("current")
_Mgs360024fARPInspectionStaticMACAddress_Type = MacAddress
_Mgs360024fARPInspectionStaticMACAddress_Object = MibTableColumn
mgs360024fARPInspectionStaticMACAddress = _Mgs360024fARPInspectionStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 2, 2, 1, 5),
    _Mgs360024fARPInspectionStaticMACAddress_Type()
)
mgs360024fARPInspectionStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fARPInspectionStaticMACAddress.setStatus("current")


class _Mgs360024fARPInspectionStaticRowStatus_Type(Integer32):
    """Custom type mgs360024fARPInspectionStaticRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Mgs360024fARPInspectionStaticRowStatus_Type.__name__ = "Integer32"
_Mgs360024fARPInspectionStaticRowStatus_Object = MibTableColumn
mgs360024fARPInspectionStaticRowStatus = _Mgs360024fARPInspectionStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 2, 2, 1, 6),
    _Mgs360024fARPInspectionStaticRowStatus_Type()
)
mgs360024fARPInspectionStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fARPInspectionStaticRowStatus.setStatus("current")
_Mgs360024fARPInspectionDynamicTable_Object = MibTable
mgs360024fARPInspectionDynamicTable = _Mgs360024fARPInspectionDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 3)
)
if mibBuilder.loadTexts:
    mgs360024fARPInspectionDynamicTable.setStatus("current")
_Mgs360024fARPInspectionDynamicEntry_Object = MibTableRow
mgs360024fARPInspectionDynamicEntry = _Mgs360024fARPInspectionDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 3, 1)
)
mgs360024fARPInspectionDynamicEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fARPInspectionDynamicIndex"),
)
if mibBuilder.loadTexts:
    mgs360024fARPInspectionDynamicEntry.setStatus("current")


class _Mgs360024fARPInspectionDynamicIndex_Type(Integer32):
    """Custom type mgs360024fARPInspectionDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fARPInspectionDynamicIndex_Type.__name__ = "Integer32"
_Mgs360024fARPInspectionDynamicIndex_Object = MibTableColumn
mgs360024fARPInspectionDynamicIndex = _Mgs360024fARPInspectionDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 3, 1, 1),
    _Mgs360024fARPInspectionDynamicIndex_Type()
)
mgs360024fARPInspectionDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fARPInspectionDynamicIndex.setStatus("current")


class _Mgs360024fARPInspectionDynamicPort_Type(Integer32):
    """Custom type mgs360024fARPInspectionDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fARPInspectionDynamicPort_Type.__name__ = "Integer32"
_Mgs360024fARPInspectionDynamicPort_Object = MibTableColumn
mgs360024fARPInspectionDynamicPort = _Mgs360024fARPInspectionDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 3, 1, 2),
    _Mgs360024fARPInspectionDynamicPort_Type()
)
mgs360024fARPInspectionDynamicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fARPInspectionDynamicPort.setStatus("current")


class _Mgs360024fARPInspectionDynamicVLANId_Type(Integer32):
    """Custom type mgs360024fARPInspectionDynamicVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Mgs360024fARPInspectionDynamicVLANId_Type.__name__ = "Integer32"
_Mgs360024fARPInspectionDynamicVLANId_Object = MibTableColumn
mgs360024fARPInspectionDynamicVLANId = _Mgs360024fARPInspectionDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 3, 1, 3),
    _Mgs360024fARPInspectionDynamicVLANId_Type()
)
mgs360024fARPInspectionDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fARPInspectionDynamicVLANId.setStatus("current")
_Mgs360024fARPInspectionDynamicIPAddress_Type = IpAddress
_Mgs360024fARPInspectionDynamicIPAddress_Object = MibTableColumn
mgs360024fARPInspectionDynamicIPAddress = _Mgs360024fARPInspectionDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 3, 1, 4),
    _Mgs360024fARPInspectionDynamicIPAddress_Type()
)
mgs360024fARPInspectionDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fARPInspectionDynamicIPAddress.setStatus("current")
_Mgs360024fARPInspectionDynamicMACAddress_Type = MacAddress
_Mgs360024fARPInspectionDynamicMACAddress_Object = MibTableColumn
mgs360024fARPInspectionDynamicMACAddress = _Mgs360024fARPInspectionDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 2, 3, 1, 5),
    _Mgs360024fARPInspectionDynamicMACAddress_Type()
)
mgs360024fARPInspectionDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fARPInspectionDynamicMACAddress.setStatus("current")
_Mgs360024fDHCPSnooping_ObjectIdentity = ObjectIdentity
mgs360024fDHCPSnooping = _Mgs360024fDHCPSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3)
)
_Mgs360024fDHCPSnoopingConf_ObjectIdentity = ObjectIdentity
mgs360024fDHCPSnoopingConf = _Mgs360024fDHCPSnoopingConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 1)
)


class _Mgs360024fDHCPSnoopingMode_Type(Integer32):
    """Custom type mgs360024fDHCPSnoopingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fDHCPSnoopingMode_Type.__name__ = "Integer32"
_Mgs360024fDHCPSnoopingMode_Object = MibScalar
mgs360024fDHCPSnoopingMode = _Mgs360024fDHCPSnoopingMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 1, 1),
    _Mgs360024fDHCPSnoopingMode_Type()
)
mgs360024fDHCPSnoopingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingMode.setStatus("current")
_Mgs360024fDHCPSnoopingPortModeConfigurationTable_Object = MibTable
mgs360024fDHCPSnoopingPortModeConfigurationTable = _Mgs360024fDHCPSnoopingPortModeConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingPortModeConfigurationTable.setStatus("current")
_Mgs360024fDHCPSnoopingPortModeConfigurationEntry_Object = MibTableRow
mgs360024fDHCPSnoopingPortModeConfigurationEntry = _Mgs360024fDHCPSnoopingPortModeConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 1, 2, 1)
)
mgs360024fDHCPSnoopingPortModeConfigurationEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fDHCPSnoopingPortModeConfigurationPort"),
)
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingPortModeConfigurationEntry.setStatus("current")


class _Mgs360024fDHCPSnoopingPortModeConfigurationPort_Type(Integer32):
    """Custom type mgs360024fDHCPSnoopingPortModeConfigurationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fDHCPSnoopingPortModeConfigurationPort_Type.__name__ = "Integer32"
_Mgs360024fDHCPSnoopingPortModeConfigurationPort_Object = MibTableColumn
mgs360024fDHCPSnoopingPortModeConfigurationPort = _Mgs360024fDHCPSnoopingPortModeConfigurationPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 1, 2, 1, 1),
    _Mgs360024fDHCPSnoopingPortModeConfigurationPort_Type()
)
mgs360024fDHCPSnoopingPortModeConfigurationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingPortModeConfigurationPort.setStatus("current")


class _Mgs360024fDHCPSnoopingPortModeConfigurationMode_Type(Integer32):
    """Custom type mgs360024fDHCPSnoopingPortModeConfigurationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fDHCPSnoopingPortModeConfigurationMode_Type.__name__ = "Integer32"
_Mgs360024fDHCPSnoopingPortModeConfigurationMode_Object = MibTableColumn
mgs360024fDHCPSnoopingPortModeConfigurationMode = _Mgs360024fDHCPSnoopingPortModeConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 1, 2, 1, 2),
    _Mgs360024fDHCPSnoopingPortModeConfigurationMode_Type()
)
mgs360024fDHCPSnoopingPortModeConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingPortModeConfigurationMode.setStatus("current")
_Mgs360024fDHCPSnoopingStatisticsTable_Object = MibTable
mgs360024fDHCPSnoopingStatisticsTable = _Mgs360024fDHCPSnoopingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2)
)
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingStatisticsTable.setStatus("current")
_Mgs360024fDHCPSnoopingStatisticsEntry_Object = MibTableRow
mgs360024fDHCPSnoopingStatisticsEntry = _Mgs360024fDHCPSnoopingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1)
)
mgs360024fDHCPSnoopingStatisticsEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fDHCPSnoopingStatisticsPort"),
)
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingStatisticsEntry.setStatus("current")


class _Mgs360024fDHCPSnoopingStatisticsPort_Type(Integer32):
    """Custom type mgs360024fDHCPSnoopingStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fDHCPSnoopingStatisticsPort_Type.__name__ = "Integer32"
_Mgs360024fDHCPSnoopingStatisticsPort_Object = MibTableColumn
mgs360024fDHCPSnoopingStatisticsPort = _Mgs360024fDHCPSnoopingStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 1),
    _Mgs360024fDHCPSnoopingStatisticsPort_Type()
)
mgs360024fDHCPSnoopingStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingStatisticsPort.setStatus("current")


class _Mgs360024fDHCPSnoopingStatisticsClear_Type(Integer32):
    """Custom type mgs360024fDHCPSnoopingStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fDHCPSnoopingStatisticsClear_Type.__name__ = "Integer32"
_Mgs360024fDHCPSnoopingStatisticsClear_Object = MibTableColumn
mgs360024fDHCPSnoopingStatisticsClear = _Mgs360024fDHCPSnoopingStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 2),
    _Mgs360024fDHCPSnoopingStatisticsClear_Type()
)
mgs360024fDHCPSnoopingStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingStatisticsClear.setStatus("current")
_Mgs360024fDHCPSnoopingRxDiscover_Type = Counter32
_Mgs360024fDHCPSnoopingRxDiscover_Object = MibTableColumn
mgs360024fDHCPSnoopingRxDiscover = _Mgs360024fDHCPSnoopingRxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 3),
    _Mgs360024fDHCPSnoopingRxDiscover_Type()
)
mgs360024fDHCPSnoopingRxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingRxDiscover.setStatus("current")
_Mgs360024fDHCPSnoopingRxOffer_Type = Counter32
_Mgs360024fDHCPSnoopingRxOffer_Object = MibTableColumn
mgs360024fDHCPSnoopingRxOffer = _Mgs360024fDHCPSnoopingRxOffer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 4),
    _Mgs360024fDHCPSnoopingRxOffer_Type()
)
mgs360024fDHCPSnoopingRxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingRxOffer.setStatus("current")
_Mgs360024fDHCPSnoopingRxRequest_Type = Counter32
_Mgs360024fDHCPSnoopingRxRequest_Object = MibTableColumn
mgs360024fDHCPSnoopingRxRequest = _Mgs360024fDHCPSnoopingRxRequest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 5),
    _Mgs360024fDHCPSnoopingRxRequest_Type()
)
mgs360024fDHCPSnoopingRxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingRxRequest.setStatus("current")
_Mgs360024fDHCPSnoopingRxDecline_Type = Counter32
_Mgs360024fDHCPSnoopingRxDecline_Object = MibTableColumn
mgs360024fDHCPSnoopingRxDecline = _Mgs360024fDHCPSnoopingRxDecline_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 6),
    _Mgs360024fDHCPSnoopingRxDecline_Type()
)
mgs360024fDHCPSnoopingRxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingRxDecline.setStatus("current")
_Mgs360024fDHCPSnoopingRxACK_Type = Counter32
_Mgs360024fDHCPSnoopingRxACK_Object = MibTableColumn
mgs360024fDHCPSnoopingRxACK = _Mgs360024fDHCPSnoopingRxACK_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 7),
    _Mgs360024fDHCPSnoopingRxACK_Type()
)
mgs360024fDHCPSnoopingRxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingRxACK.setStatus("current")
_Mgs360024fDHCPSnoopingRxNAK_Type = Counter32
_Mgs360024fDHCPSnoopingRxNAK_Object = MibTableColumn
mgs360024fDHCPSnoopingRxNAK = _Mgs360024fDHCPSnoopingRxNAK_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 8),
    _Mgs360024fDHCPSnoopingRxNAK_Type()
)
mgs360024fDHCPSnoopingRxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingRxNAK.setStatus("current")
_Mgs360024fDHCPSnoopingRxRelease_Type = Counter32
_Mgs360024fDHCPSnoopingRxRelease_Object = MibTableColumn
mgs360024fDHCPSnoopingRxRelease = _Mgs360024fDHCPSnoopingRxRelease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 9),
    _Mgs360024fDHCPSnoopingRxRelease_Type()
)
mgs360024fDHCPSnoopingRxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingRxRelease.setStatus("current")
_Mgs360024fDHCPSnoopingRxInform_Type = Counter32
_Mgs360024fDHCPSnoopingRxInform_Object = MibTableColumn
mgs360024fDHCPSnoopingRxInform = _Mgs360024fDHCPSnoopingRxInform_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 10),
    _Mgs360024fDHCPSnoopingRxInform_Type()
)
mgs360024fDHCPSnoopingRxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingRxInform.setStatus("current")
_Mgs360024fDHCPSnoopingRxLeaseQuery_Type = Counter32
_Mgs360024fDHCPSnoopingRxLeaseQuery_Object = MibTableColumn
mgs360024fDHCPSnoopingRxLeaseQuery = _Mgs360024fDHCPSnoopingRxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 11),
    _Mgs360024fDHCPSnoopingRxLeaseQuery_Type()
)
mgs360024fDHCPSnoopingRxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingRxLeaseQuery.setStatus("current")
_Mgs360024fDHCPSnoopingRxLeaseUnassigned_Type = Counter32
_Mgs360024fDHCPSnoopingRxLeaseUnassigned_Object = MibTableColumn
mgs360024fDHCPSnoopingRxLeaseUnassigned = _Mgs360024fDHCPSnoopingRxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 12),
    _Mgs360024fDHCPSnoopingRxLeaseUnassigned_Type()
)
mgs360024fDHCPSnoopingRxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingRxLeaseUnassigned.setStatus("current")
_Mgs360024fDHCPSnoopingRxLeaseUnknown_Type = Counter32
_Mgs360024fDHCPSnoopingRxLeaseUnknown_Object = MibTableColumn
mgs360024fDHCPSnoopingRxLeaseUnknown = _Mgs360024fDHCPSnoopingRxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 13),
    _Mgs360024fDHCPSnoopingRxLeaseUnknown_Type()
)
mgs360024fDHCPSnoopingRxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingRxLeaseUnknown.setStatus("current")
_Mgs360024fDHCPSnoopingRxLeaseActive_Type = Counter32
_Mgs360024fDHCPSnoopingRxLeaseActive_Object = MibTableColumn
mgs360024fDHCPSnoopingRxLeaseActive = _Mgs360024fDHCPSnoopingRxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 14),
    _Mgs360024fDHCPSnoopingRxLeaseActive_Type()
)
mgs360024fDHCPSnoopingRxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingRxLeaseActive.setStatus("current")
_Mgs360024fDHCPSnoopingTxDiscover_Type = Counter32
_Mgs360024fDHCPSnoopingTxDiscover_Object = MibTableColumn
mgs360024fDHCPSnoopingTxDiscover = _Mgs360024fDHCPSnoopingTxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 15),
    _Mgs360024fDHCPSnoopingTxDiscover_Type()
)
mgs360024fDHCPSnoopingTxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingTxDiscover.setStatus("current")
_Mgs360024fDHCPSnoopingTxOffer_Type = Counter32
_Mgs360024fDHCPSnoopingTxOffer_Object = MibTableColumn
mgs360024fDHCPSnoopingTxOffer = _Mgs360024fDHCPSnoopingTxOffer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 16),
    _Mgs360024fDHCPSnoopingTxOffer_Type()
)
mgs360024fDHCPSnoopingTxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingTxOffer.setStatus("current")
_Mgs360024fDHCPSnoopingTxRequest_Type = Counter32
_Mgs360024fDHCPSnoopingTxRequest_Object = MibTableColumn
mgs360024fDHCPSnoopingTxRequest = _Mgs360024fDHCPSnoopingTxRequest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 17),
    _Mgs360024fDHCPSnoopingTxRequest_Type()
)
mgs360024fDHCPSnoopingTxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingTxRequest.setStatus("current")
_Mgs360024fDHCPSnoopingTxDecline_Type = Counter32
_Mgs360024fDHCPSnoopingTxDecline_Object = MibTableColumn
mgs360024fDHCPSnoopingTxDecline = _Mgs360024fDHCPSnoopingTxDecline_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 18),
    _Mgs360024fDHCPSnoopingTxDecline_Type()
)
mgs360024fDHCPSnoopingTxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingTxDecline.setStatus("current")
_Mgs360024fDHCPSnoopingTxACK_Type = Counter32
_Mgs360024fDHCPSnoopingTxACK_Object = MibTableColumn
mgs360024fDHCPSnoopingTxACK = _Mgs360024fDHCPSnoopingTxACK_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 19),
    _Mgs360024fDHCPSnoopingTxACK_Type()
)
mgs360024fDHCPSnoopingTxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingTxACK.setStatus("current")
_Mgs360024fDHCPSnoopingTxNAK_Type = Counter32
_Mgs360024fDHCPSnoopingTxNAK_Object = MibTableColumn
mgs360024fDHCPSnoopingTxNAK = _Mgs360024fDHCPSnoopingTxNAK_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 20),
    _Mgs360024fDHCPSnoopingTxNAK_Type()
)
mgs360024fDHCPSnoopingTxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingTxNAK.setStatus("current")
_Mgs360024fDHCPSnoopingTxRelease_Type = Counter32
_Mgs360024fDHCPSnoopingTxRelease_Object = MibTableColumn
mgs360024fDHCPSnoopingTxRelease = _Mgs360024fDHCPSnoopingTxRelease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 21),
    _Mgs360024fDHCPSnoopingTxRelease_Type()
)
mgs360024fDHCPSnoopingTxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingTxRelease.setStatus("current")
_Mgs360024fDHCPSnoopingTxInform_Type = Counter32
_Mgs360024fDHCPSnoopingTxInform_Object = MibTableColumn
mgs360024fDHCPSnoopingTxInform = _Mgs360024fDHCPSnoopingTxInform_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 22),
    _Mgs360024fDHCPSnoopingTxInform_Type()
)
mgs360024fDHCPSnoopingTxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingTxInform.setStatus("current")
_Mgs360024fDHCPSnoopingTxLeaseQuery_Type = Counter32
_Mgs360024fDHCPSnoopingTxLeaseQuery_Object = MibTableColumn
mgs360024fDHCPSnoopingTxLeaseQuery = _Mgs360024fDHCPSnoopingTxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 23),
    _Mgs360024fDHCPSnoopingTxLeaseQuery_Type()
)
mgs360024fDHCPSnoopingTxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingTxLeaseQuery.setStatus("current")
_Mgs360024fDHCPSnoopingTxLeaseUnassigned_Type = Counter32
_Mgs360024fDHCPSnoopingTxLeaseUnassigned_Object = MibTableColumn
mgs360024fDHCPSnoopingTxLeaseUnassigned = _Mgs360024fDHCPSnoopingTxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 24),
    _Mgs360024fDHCPSnoopingTxLeaseUnassigned_Type()
)
mgs360024fDHCPSnoopingTxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingTxLeaseUnassigned.setStatus("current")
_Mgs360024fDHCPSnoopingTxLeaseUnknown_Type = Counter32
_Mgs360024fDHCPSnoopingTxLeaseUnknown_Object = MibTableColumn
mgs360024fDHCPSnoopingTxLeaseUnknown = _Mgs360024fDHCPSnoopingTxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 25),
    _Mgs360024fDHCPSnoopingTxLeaseUnknown_Type()
)
mgs360024fDHCPSnoopingTxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingTxLeaseUnknown.setStatus("current")
_Mgs360024fDHCPSnoopingTxLeaseActive_Type = Counter32
_Mgs360024fDHCPSnoopingTxLeaseActive_Object = MibTableColumn
mgs360024fDHCPSnoopingTxLeaseActive = _Mgs360024fDHCPSnoopingTxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 3, 2, 1, 26),
    _Mgs360024fDHCPSnoopingTxLeaseActive_Type()
)
mgs360024fDHCPSnoopingTxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fDHCPSnoopingTxLeaseActive.setStatus("current")
_Mgs360024fDHCPRelay_ObjectIdentity = ObjectIdentity
mgs360024fDHCPRelay = _Mgs360024fDHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4)
)
_Mgs360024fDHCPRelayConfiguration_ObjectIdentity = ObjectIdentity
mgs360024fDHCPRelayConfiguration = _Mgs360024fDHCPRelayConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 1)
)


class _Mgs360024fDHCPRelayMode_Type(Integer32):
    """Custom type mgs360024fDHCPRelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fDHCPRelayMode_Type.__name__ = "Integer32"
_Mgs360024fDHCPRelayMode_Object = MibScalar
mgs360024fDHCPRelayMode = _Mgs360024fDHCPRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 1, 1),
    _Mgs360024fDHCPRelayMode_Type()
)
mgs360024fDHCPRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fDHCPRelayMode.setStatus("current")
_Mgs360024fDHCPRelayServer_Type = IpAddress
_Mgs360024fDHCPRelayServer_Object = MibScalar
mgs360024fDHCPRelayServer = _Mgs360024fDHCPRelayServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 1, 2),
    _Mgs360024fDHCPRelayServer_Type()
)
mgs360024fDHCPRelayServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fDHCPRelayServer.setStatus("current")


class _Mgs360024fDHCPRelayInformationMode_Type(Integer32):
    """Custom type mgs360024fDHCPRelayInformationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fDHCPRelayInformationMode_Type.__name__ = "Integer32"
_Mgs360024fDHCPRelayInformationMode_Object = MibScalar
mgs360024fDHCPRelayInformationMode = _Mgs360024fDHCPRelayInformationMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 1, 3),
    _Mgs360024fDHCPRelayInformationMode_Type()
)
mgs360024fDHCPRelayInformationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fDHCPRelayInformationMode.setStatus("current")


class _Mgs360024fDHCPRelayInformationPolicy_Type(Integer32):
    """Custom type mgs360024fDHCPRelayInformationPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mgs360024fDHCPRelayInformationPolicy_Type.__name__ = "Integer32"
_Mgs360024fDHCPRelayInformationPolicy_Object = MibScalar
mgs360024fDHCPRelayInformationPolicy = _Mgs360024fDHCPRelayInformationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 1, 4),
    _Mgs360024fDHCPRelayInformationPolicy_Type()
)
mgs360024fDHCPRelayInformationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fDHCPRelayInformationPolicy.setStatus("current")
_Mgs360024fDHCPRelayStatistics_ObjectIdentity = ObjectIdentity
mgs360024fDHCPRelayStatistics = _Mgs360024fDHCPRelayStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 2)
)
_Mgs360024fDHCPRelayServerStatistics_ObjectIdentity = ObjectIdentity
mgs360024fDHCPRelayServerStatistics = _Mgs360024fDHCPRelayServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 2, 1)
)
_Mgs360024fServerStatTransmitToServer_Type = Counter32
_Mgs360024fServerStatTransmitToServer_Object = MibScalar
mgs360024fServerStatTransmitToServer = _Mgs360024fServerStatTransmitToServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 2, 1, 1),
    _Mgs360024fServerStatTransmitToServer_Type()
)
mgs360024fServerStatTransmitToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fServerStatTransmitToServer.setStatus("current")
_Mgs360024fServerStatTransmitError_Type = Counter32
_Mgs360024fServerStatTransmitError_Object = MibScalar
mgs360024fServerStatTransmitError = _Mgs360024fServerStatTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 2, 1, 2),
    _Mgs360024fServerStatTransmitError_Type()
)
mgs360024fServerStatTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fServerStatTransmitError.setStatus("current")
_Mgs360024fServerStatReceiveFromServer_Type = Counter32
_Mgs360024fServerStatReceiveFromServer_Object = MibScalar
mgs360024fServerStatReceiveFromServer = _Mgs360024fServerStatReceiveFromServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 2, 1, 3),
    _Mgs360024fServerStatReceiveFromServer_Type()
)
mgs360024fServerStatReceiveFromServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fServerStatReceiveFromServer.setStatus("current")
_Mgs360024fServerStatReceiveMissingAgentOption_Type = Counter32
_Mgs360024fServerStatReceiveMissingAgentOption_Object = MibScalar
mgs360024fServerStatReceiveMissingAgentOption = _Mgs360024fServerStatReceiveMissingAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 2, 1, 4),
    _Mgs360024fServerStatReceiveMissingAgentOption_Type()
)
mgs360024fServerStatReceiveMissingAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fServerStatReceiveMissingAgentOption.setStatus("current")
_Mgs360024fServerStatReceiveMissingCircuitID_Type = Counter32
_Mgs360024fServerStatReceiveMissingCircuitID_Object = MibScalar
mgs360024fServerStatReceiveMissingCircuitID = _Mgs360024fServerStatReceiveMissingCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 2, 1, 5),
    _Mgs360024fServerStatReceiveMissingCircuitID_Type()
)
mgs360024fServerStatReceiveMissingCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fServerStatReceiveMissingCircuitID.setStatus("current")
_Mgs360024fServerStatReceiveMissingRemoteID_Type = Counter32
_Mgs360024fServerStatReceiveMissingRemoteID_Object = MibScalar
mgs360024fServerStatReceiveMissingRemoteID = _Mgs360024fServerStatReceiveMissingRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 2, 1, 6),
    _Mgs360024fServerStatReceiveMissingRemoteID_Type()
)
mgs360024fServerStatReceiveMissingRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fServerStatReceiveMissingRemoteID.setStatus("current")
_Mgs360024fServerStatReceiveBadCircuitID_Type = Counter32
_Mgs360024fServerStatReceiveBadCircuitID_Object = MibScalar
mgs360024fServerStatReceiveBadCircuitID = _Mgs360024fServerStatReceiveBadCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 2, 1, 7),
    _Mgs360024fServerStatReceiveBadCircuitID_Type()
)
mgs360024fServerStatReceiveBadCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fServerStatReceiveBadCircuitID.setStatus("current")
_Mgs360024fServerStatReceiveBadRemoteID_Type = Counter32
_Mgs360024fServerStatReceiveBadRemoteID_Object = MibScalar
mgs360024fServerStatReceiveBadRemoteID = _Mgs360024fServerStatReceiveBadRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 2, 1, 8),
    _Mgs360024fServerStatReceiveBadRemoteID_Type()
)
mgs360024fServerStatReceiveBadRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fServerStatReceiveBadRemoteID.setStatus("current")
_Mgs360024fDHCPRelayClientStatistics_ObjectIdentity = ObjectIdentity
mgs360024fDHCPRelayClientStatistics = _Mgs360024fDHCPRelayClientStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 2, 2)
)
_Mgs360024fClientStatTransmitToClient_Type = Counter32
_Mgs360024fClientStatTransmitToClient_Object = MibScalar
mgs360024fClientStatTransmitToClient = _Mgs360024fClientStatTransmitToClient_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 2, 2, 1),
    _Mgs360024fClientStatTransmitToClient_Type()
)
mgs360024fClientStatTransmitToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fClientStatTransmitToClient.setStatus("current")
_Mgs360024fClientStatTransmitError_Type = Counter32
_Mgs360024fClientStatTransmitError_Object = MibScalar
mgs360024fClientStatTransmitError = _Mgs360024fClientStatTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 2, 2, 2),
    _Mgs360024fClientStatTransmitError_Type()
)
mgs360024fClientStatTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fClientStatTransmitError.setStatus("current")
_Mgs360024fClientStatReceivefromClient_Type = Counter32
_Mgs360024fClientStatReceivefromClient_Object = MibScalar
mgs360024fClientStatReceivefromClient = _Mgs360024fClientStatReceivefromClient_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 2, 2, 3),
    _Mgs360024fClientStatReceivefromClient_Type()
)
mgs360024fClientStatReceivefromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fClientStatReceivefromClient.setStatus("current")
_Mgs360024fClientStatReceiveAgentOption_Type = Counter32
_Mgs360024fClientStatReceiveAgentOption_Object = MibScalar
mgs360024fClientStatReceiveAgentOption = _Mgs360024fClientStatReceiveAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 2, 2, 4),
    _Mgs360024fClientStatReceiveAgentOption_Type()
)
mgs360024fClientStatReceiveAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fClientStatReceiveAgentOption.setStatus("current")
_Mgs360024fClientStatReplaceAgentOption_Type = Counter32
_Mgs360024fClientStatReplaceAgentOption_Object = MibScalar
mgs360024fClientStatReplaceAgentOption = _Mgs360024fClientStatReplaceAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 2, 2, 5),
    _Mgs360024fClientStatReplaceAgentOption_Type()
)
mgs360024fClientStatReplaceAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fClientStatReplaceAgentOption.setStatus("current")
_Mgs360024fClientStatKeepAgentOption_Type = Counter32
_Mgs360024fClientStatKeepAgentOption_Object = MibScalar
mgs360024fClientStatKeepAgentOption = _Mgs360024fClientStatKeepAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 2, 2, 6),
    _Mgs360024fClientStatKeepAgentOption_Type()
)
mgs360024fClientStatKeepAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fClientStatKeepAgentOption.setStatus("current")
_Mgs360024fClientStatDropAgentOption_Type = Counter32
_Mgs360024fClientStatDropAgentOption_Object = MibScalar
mgs360024fClientStatDropAgentOption = _Mgs360024fClientStatDropAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 4, 2, 2, 7),
    _Mgs360024fClientStatDropAgentOption_Type()
)
mgs360024fClientStatDropAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fClientStatDropAgentOption.setStatus("current")
_Mgs360024fPortSecurity_ObjectIdentity = ObjectIdentity
mgs360024fPortSecurity = _Mgs360024fPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5)
)
_Mgs360024fPortSecLimitCtrl_ObjectIdentity = ObjectIdentity
mgs360024fPortSecLimitCtrl = _Mgs360024fPortSecLimitCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 1)
)
_Mgs360024fPortSecLimitCtrlSystemConf_ObjectIdentity = ObjectIdentity
mgs360024fPortSecLimitCtrlSystemConf = _Mgs360024fPortSecLimitCtrlSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 1, 1)
)


class _Mgs360024fPortSecurityMode_Type(Integer32):
    """Custom type mgs360024fPortSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fPortSecurityMode_Type.__name__ = "Integer32"
_Mgs360024fPortSecurityMode_Object = MibScalar
mgs360024fPortSecurityMode = _Mgs360024fPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 1, 1, 1),
    _Mgs360024fPortSecurityMode_Type()
)
mgs360024fPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPortSecurityMode.setStatus("current")


class _Mgs360024fPortSecurityAging_Type(Integer32):
    """Custom type mgs360024fPortSecurityAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fPortSecurityAging_Type.__name__ = "Integer32"
_Mgs360024fPortSecurityAging_Object = MibScalar
mgs360024fPortSecurityAging = _Mgs360024fPortSecurityAging_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 1, 1, 2),
    _Mgs360024fPortSecurityAging_Type()
)
mgs360024fPortSecurityAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPortSecurityAging.setStatus("current")


class _Mgs360024fPortSecurityAgingPeriod_Type(Integer32):
    """Custom type mgs360024fPortSecurityAgingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000000),
    )


_Mgs360024fPortSecurityAgingPeriod_Type.__name__ = "Integer32"
_Mgs360024fPortSecurityAgingPeriod_Object = MibScalar
mgs360024fPortSecurityAgingPeriod = _Mgs360024fPortSecurityAgingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 1, 1, 3),
    _Mgs360024fPortSecurityAgingPeriod_Type()
)
mgs360024fPortSecurityAgingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPortSecurityAgingPeriod.setStatus("current")
_Mgs360024fPortSecLimitCtrlTable_Object = MibTable
mgs360024fPortSecLimitCtrlTable = _Mgs360024fPortSecLimitCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    mgs360024fPortSecLimitCtrlTable.setStatus("current")
_Mgs360024fPortSecLimitCtrlEntry_Object = MibTableRow
mgs360024fPortSecLimitCtrlEntry = _Mgs360024fPortSecLimitCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 1, 2, 1)
)
mgs360024fPortSecLimitCtrlEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fPortSecLimitCtrlPort"),
)
if mibBuilder.loadTexts:
    mgs360024fPortSecLimitCtrlEntry.setStatus("current")


class _Mgs360024fPortSecLimitCtrlPort_Type(Integer32):
    """Custom type mgs360024fPortSecLimitCtrlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fPortSecLimitCtrlPort_Type.__name__ = "Integer32"
_Mgs360024fPortSecLimitCtrlPort_Object = MibTableColumn
mgs360024fPortSecLimitCtrlPort = _Mgs360024fPortSecLimitCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 1, 2, 1, 1),
    _Mgs360024fPortSecLimitCtrlPort_Type()
)
mgs360024fPortSecLimitCtrlPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fPortSecLimitCtrlPort.setStatus("current")


class _Mgs360024fPortSecLimitCtrlPortMode_Type(Integer32):
    """Custom type mgs360024fPortSecLimitCtrlPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fPortSecLimitCtrlPortMode_Type.__name__ = "Integer32"
_Mgs360024fPortSecLimitCtrlPortMode_Object = MibTableColumn
mgs360024fPortSecLimitCtrlPortMode = _Mgs360024fPortSecLimitCtrlPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 1, 2, 1, 2),
    _Mgs360024fPortSecLimitCtrlPortMode_Type()
)
mgs360024fPortSecLimitCtrlPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPortSecLimitCtrlPortMode.setStatus("current")


class _Mgs360024fPortSecLimitCtrlPortLimit_Type(Integer32):
    """Custom type mgs360024fPortSecLimitCtrlPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Mgs360024fPortSecLimitCtrlPortLimit_Type.__name__ = "Integer32"
_Mgs360024fPortSecLimitCtrlPortLimit_Object = MibTableColumn
mgs360024fPortSecLimitCtrlPortLimit = _Mgs360024fPortSecLimitCtrlPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 1, 2, 1, 3),
    _Mgs360024fPortSecLimitCtrlPortLimit_Type()
)
mgs360024fPortSecLimitCtrlPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPortSecLimitCtrlPortLimit.setStatus("current")


class _Mgs360024fPortSecLimitCtrlPortAction_Type(Integer32):
    """Custom type mgs360024fPortSecLimitCtrlPortAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Mgs360024fPortSecLimitCtrlPortAction_Type.__name__ = "Integer32"
_Mgs360024fPortSecLimitCtrlPortAction_Object = MibTableColumn
mgs360024fPortSecLimitCtrlPortAction = _Mgs360024fPortSecLimitCtrlPortAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 1, 2, 1, 4),
    _Mgs360024fPortSecLimitCtrlPortAction_Type()
)
mgs360024fPortSecLimitCtrlPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPortSecLimitCtrlPortAction.setStatus("current")
_Mgs360024fPortSecLimitCtrlPortState_Type = DisplayString
_Mgs360024fPortSecLimitCtrlPortState_Object = MibTableColumn
mgs360024fPortSecLimitCtrlPortState = _Mgs360024fPortSecLimitCtrlPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 1, 2, 1, 5),
    _Mgs360024fPortSecLimitCtrlPortState_Type()
)
mgs360024fPortSecLimitCtrlPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortSecLimitCtrlPortState.setStatus("current")


class _Mgs360024fPortSecLimitCtrlPortReOpen_Type(Integer32):
    """Custom type mgs360024fPortSecLimitCtrlPortReOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fPortSecLimitCtrlPortReOpen_Type.__name__ = "Integer32"
_Mgs360024fPortSecLimitCtrlPortReOpen_Object = MibTableColumn
mgs360024fPortSecLimitCtrlPortReOpen = _Mgs360024fPortSecLimitCtrlPortReOpen_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 1, 2, 1, 6),
    _Mgs360024fPortSecLimitCtrlPortReOpen_Type()
)
mgs360024fPortSecLimitCtrlPortReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPortSecLimitCtrlPortReOpen.setStatus("current")
_Mgs360024fPortSecSwitchStatusTable_Object = MibTable
mgs360024fPortSecSwitchStatusTable = _Mgs360024fPortSecSwitchStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 2)
)
if mibBuilder.loadTexts:
    mgs360024fPortSecSwitchStatusTable.setStatus("current")
_Mgs360024fPortSecSwitchStatusEntry_Object = MibTableRow
mgs360024fPortSecSwitchStatusEntry = _Mgs360024fPortSecSwitchStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 2, 1)
)
mgs360024fPortSecSwitchStatusEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fPortSecSwitchStatusPort"),
)
if mibBuilder.loadTexts:
    mgs360024fPortSecSwitchStatusEntry.setStatus("current")


class _Mgs360024fPortSecSwitchStatusPort_Type(Integer32):
    """Custom type mgs360024fPortSecSwitchStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fPortSecSwitchStatusPort_Type.__name__ = "Integer32"
_Mgs360024fPortSecSwitchStatusPort_Object = MibTableColumn
mgs360024fPortSecSwitchStatusPort = _Mgs360024fPortSecSwitchStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 2, 1, 1),
    _Mgs360024fPortSecSwitchStatusPort_Type()
)
mgs360024fPortSecSwitchStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fPortSecSwitchStatusPort.setStatus("current")
_Mgs360024fPortSecSwitchStatusUsers_Type = DisplayString
_Mgs360024fPortSecSwitchStatusUsers_Object = MibTableColumn
mgs360024fPortSecSwitchStatusUsers = _Mgs360024fPortSecSwitchStatusUsers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 2, 1, 2),
    _Mgs360024fPortSecSwitchStatusUsers_Type()
)
mgs360024fPortSecSwitchStatusUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortSecSwitchStatusUsers.setStatus("current")
_Mgs360024fPortSecSwitchStatusState_Type = DisplayString
_Mgs360024fPortSecSwitchStatusState_Object = MibTableColumn
mgs360024fPortSecSwitchStatusState = _Mgs360024fPortSecSwitchStatusState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 2, 1, 3),
    _Mgs360024fPortSecSwitchStatusState_Type()
)
mgs360024fPortSecSwitchStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortSecSwitchStatusState.setStatus("current")


class _Mgs360024fPortSecSwitchStatusMACCountCurrent_Type(Integer32):
    """Custom type mgs360024fPortSecSwitchStatusMACCountCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fPortSecSwitchStatusMACCountCurrent_Type.__name__ = "Integer32"
_Mgs360024fPortSecSwitchStatusMACCountCurrent_Object = MibTableColumn
mgs360024fPortSecSwitchStatusMACCountCurrent = _Mgs360024fPortSecSwitchStatusMACCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 2, 1, 4),
    _Mgs360024fPortSecSwitchStatusMACCountCurrent_Type()
)
mgs360024fPortSecSwitchStatusMACCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortSecSwitchStatusMACCountCurrent.setStatus("current")


class _Mgs360024fPortSecSwitchStatusMACCountLimit_Type(Integer32):
    """Custom type mgs360024fPortSecSwitchStatusMACCountLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fPortSecSwitchStatusMACCountLimit_Type.__name__ = "Integer32"
_Mgs360024fPortSecSwitchStatusMACCountLimit_Object = MibTableColumn
mgs360024fPortSecSwitchStatusMACCountLimit = _Mgs360024fPortSecSwitchStatusMACCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 2, 1, 5),
    _Mgs360024fPortSecSwitchStatusMACCountLimit_Type()
)
mgs360024fPortSecSwitchStatusMACCountLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortSecSwitchStatusMACCountLimit.setStatus("current")
_Mgs360024fPortSecPortStatus_ObjectIdentity = ObjectIdentity
mgs360024fPortSecPortStatus = _Mgs360024fPortSecPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 3)
)


class _Mgs360024fPortSecPortStatusPort_Type(Integer32):
    """Custom type mgs360024fPortSecPortStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fPortSecPortStatusPort_Type.__name__ = "Integer32"
_Mgs360024fPortSecPortStatusPort_Object = MibScalar
mgs360024fPortSecPortStatusPort = _Mgs360024fPortSecPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 3, 1),
    _Mgs360024fPortSecPortStatusPort_Type()
)
mgs360024fPortSecPortStatusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPortSecPortStatusPort.setStatus("current")
_Mgs360024fPortSecPortStatusTable_Object = MibTable
mgs360024fPortSecPortStatusTable = _Mgs360024fPortSecPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 3, 2)
)
if mibBuilder.loadTexts:
    mgs360024fPortSecPortStatusTable.setStatus("current")
_Mgs360024fPortSecPortStatusEntry_Object = MibTableRow
mgs360024fPortSecPortStatusEntry = _Mgs360024fPortSecPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 3, 2, 1)
)
mgs360024fPortSecPortStatusEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fPortSecPortStatusIndex"),
)
if mibBuilder.loadTexts:
    mgs360024fPortSecPortStatusEntry.setStatus("current")


class _Mgs360024fPortSecPortStatusIndex_Type(Integer32):
    """Custom type mgs360024fPortSecPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fPortSecPortStatusIndex_Type.__name__ = "Integer32"
_Mgs360024fPortSecPortStatusIndex_Object = MibTableColumn
mgs360024fPortSecPortStatusIndex = _Mgs360024fPortSecPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 3, 2, 1, 1),
    _Mgs360024fPortSecPortStatusIndex_Type()
)
mgs360024fPortSecPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fPortSecPortStatusIndex.setStatus("current")
_Mgs360024fPortSecPortStatusMACAddress_Type = MacAddress
_Mgs360024fPortSecPortStatusMACAddress_Object = MibTableColumn
mgs360024fPortSecPortStatusMACAddress = _Mgs360024fPortSecPortStatusMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 3, 2, 1, 2),
    _Mgs360024fPortSecPortStatusMACAddress_Type()
)
mgs360024fPortSecPortStatusMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortSecPortStatusMACAddress.setStatus("current")


class _Mgs360024fPortSecPortStatusVLANId_Type(Integer32):
    """Custom type mgs360024fPortSecPortStatusVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Mgs360024fPortSecPortStatusVLANId_Type.__name__ = "Integer32"
_Mgs360024fPortSecPortStatusVLANId_Object = MibTableColumn
mgs360024fPortSecPortStatusVLANId = _Mgs360024fPortSecPortStatusVLANId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 3, 2, 1, 3),
    _Mgs360024fPortSecPortStatusVLANId_Type()
)
mgs360024fPortSecPortStatusVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortSecPortStatusVLANId.setStatus("current")
_Mgs360024fPortSecPortStatusState_Type = DisplayString
_Mgs360024fPortSecPortStatusState_Object = MibTableColumn
mgs360024fPortSecPortStatusState = _Mgs360024fPortSecPortStatusState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 3, 2, 1, 4),
    _Mgs360024fPortSecPortStatusState_Type()
)
mgs360024fPortSecPortStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortSecPortStatusState.setStatus("current")
_Mgs360024fPortSecPortStatusTimeOfAddition_Type = DisplayString
_Mgs360024fPortSecPortStatusTimeOfAddition_Object = MibTableColumn
mgs360024fPortSecPortStatusTimeOfAddition = _Mgs360024fPortSecPortStatusTimeOfAddition_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 3, 2, 1, 5),
    _Mgs360024fPortSecPortStatusTimeOfAddition_Type()
)
mgs360024fPortSecPortStatusTimeOfAddition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortSecPortStatusTimeOfAddition.setStatus("current")
_Mgs360024fPortSecPortStatusAgeAndHold_Type = DisplayString
_Mgs360024fPortSecPortStatusAgeAndHold_Object = MibTableColumn
mgs360024fPortSecPortStatusAgeAndHold = _Mgs360024fPortSecPortStatusAgeAndHold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 5, 3, 2, 1, 6),
    _Mgs360024fPortSecPortStatusAgeAndHold_Type()
)
mgs360024fPortSecPortStatusAgeAndHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPortSecPortStatusAgeAndHold.setStatus("current")
_Mgs360024fAccessManagement_ObjectIdentity = ObjectIdentity
mgs360024fAccessManagement = _Mgs360024fAccessManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6)
)
_Mgs360024fAccessMgtConf_ObjectIdentity = ObjectIdentity
mgs360024fAccessMgtConf = _Mgs360024fAccessMgtConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 1)
)


class _Mgs360024fAccessMgtConfMode_Type(Integer32):
    """Custom type mgs360024fAccessMgtConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fAccessMgtConfMode_Type.__name__ = "Integer32"
_Mgs360024fAccessMgtConfMode_Object = MibScalar
mgs360024fAccessMgtConfMode = _Mgs360024fAccessMgtConfMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 1, 1),
    _Mgs360024fAccessMgtConfMode_Type()
)
mgs360024fAccessMgtConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fAccessMgtConfMode.setStatus("current")


class _Mgs360024fAccessMgtConfCreate_Type(Integer32):
    """Custom type mgs360024fAccessMgtConfCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fAccessMgtConfCreate_Type.__name__ = "Integer32"
_Mgs360024fAccessMgtConfCreate_Object = MibScalar
mgs360024fAccessMgtConfCreate = _Mgs360024fAccessMgtConfCreate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 1, 2),
    _Mgs360024fAccessMgtConfCreate_Type()
)
mgs360024fAccessMgtConfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fAccessMgtConfCreate.setStatus("current")
_Mgs360024fAccessMgtConfTable_Object = MibTable
mgs360024fAccessMgtConfTable = _Mgs360024fAccessMgtConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 1, 3)
)
if mibBuilder.loadTexts:
    mgs360024fAccessMgtConfTable.setStatus("current")
_Mgs360024fAccessMgtConfEntry_Object = MibTableRow
mgs360024fAccessMgtConfEntry = _Mgs360024fAccessMgtConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 1, 3, 1)
)
mgs360024fAccessMgtConfEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fAccessMgtIndex"),
)
if mibBuilder.loadTexts:
    mgs360024fAccessMgtConfEntry.setStatus("current")


class _Mgs360024fAccessMgtIndex_Type(Integer32):
    """Custom type mgs360024fAccessMgtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Mgs360024fAccessMgtIndex_Type.__name__ = "Integer32"
_Mgs360024fAccessMgtIndex_Object = MibTableColumn
mgs360024fAccessMgtIndex = _Mgs360024fAccessMgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 1, 3, 1, 1),
    _Mgs360024fAccessMgtIndex_Type()
)
mgs360024fAccessMgtIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fAccessMgtIndex.setStatus("current")


class _Mgs360024fAccessMgtAddresstype_Type(Integer32):
    """Custom type mgs360024fAccessMgtAddresstype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fAccessMgtAddresstype_Type.__name__ = "Integer32"
_Mgs360024fAccessMgtAddresstype_Object = MibTableColumn
mgs360024fAccessMgtAddresstype = _Mgs360024fAccessMgtAddresstype_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 1, 3, 1, 2),
    _Mgs360024fAccessMgtAddresstype_Type()
)
mgs360024fAccessMgtAddresstype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fAccessMgtAddresstype.setStatus("current")
_Mgs360024fAccessMgtStartIpAddress_Type = DisplayString
_Mgs360024fAccessMgtStartIpAddress_Object = MibTableColumn
mgs360024fAccessMgtStartIpAddress = _Mgs360024fAccessMgtStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 1, 3, 1, 3),
    _Mgs360024fAccessMgtStartIpAddress_Type()
)
mgs360024fAccessMgtStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fAccessMgtStartIpAddress.setStatus("current")
_Mgs360024fAccessMgtEndIpAddress_Type = DisplayString
_Mgs360024fAccessMgtEndIpAddress_Object = MibTableColumn
mgs360024fAccessMgtEndIpAddress = _Mgs360024fAccessMgtEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 1, 3, 1, 4),
    _Mgs360024fAccessMgtEndIpAddress_Type()
)
mgs360024fAccessMgtEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fAccessMgtEndIpAddress.setStatus("current")


class _Mgs360024fAccessMgtHttpHttps_Type(Integer32):
    """Custom type mgs360024fAccessMgtHttpHttps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fAccessMgtHttpHttps_Type.__name__ = "Integer32"
_Mgs360024fAccessMgtHttpHttps_Object = MibTableColumn
mgs360024fAccessMgtHttpHttps = _Mgs360024fAccessMgtHttpHttps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 1, 3, 1, 5),
    _Mgs360024fAccessMgtHttpHttps_Type()
)
mgs360024fAccessMgtHttpHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fAccessMgtHttpHttps.setStatus("current")


class _Mgs360024fAccessMgtSNMP_Type(Integer32):
    """Custom type mgs360024fAccessMgtSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fAccessMgtSNMP_Type.__name__ = "Integer32"
_Mgs360024fAccessMgtSNMP_Object = MibTableColumn
mgs360024fAccessMgtSNMP = _Mgs360024fAccessMgtSNMP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 1, 3, 1, 6),
    _Mgs360024fAccessMgtSNMP_Type()
)
mgs360024fAccessMgtSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fAccessMgtSNMP.setStatus("current")


class _Mgs360024fAccessMgtTelnetSSH_Type(Integer32):
    """Custom type mgs360024fAccessMgtTelnetSSH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fAccessMgtTelnetSSH_Type.__name__ = "Integer32"
_Mgs360024fAccessMgtTelnetSSH_Object = MibTableColumn
mgs360024fAccessMgtTelnetSSH = _Mgs360024fAccessMgtTelnetSSH_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 1, 3, 1, 7),
    _Mgs360024fAccessMgtTelnetSSH_Type()
)
mgs360024fAccessMgtTelnetSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fAccessMgtTelnetSSH.setStatus("current")


class _Mgs360024fAccessMgtRowStatus_Type(Integer32):
    """Custom type mgs360024fAccessMgtRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Mgs360024fAccessMgtRowStatus_Type.__name__ = "Integer32"
_Mgs360024fAccessMgtRowStatus_Object = MibTableColumn
mgs360024fAccessMgtRowStatus = _Mgs360024fAccessMgtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 1, 3, 1, 8),
    _Mgs360024fAccessMgtRowStatus_Type()
)
mgs360024fAccessMgtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fAccessMgtRowStatus.setStatus("current")
_Mgs360024fAccessMgtStatistics_ObjectIdentity = ObjectIdentity
mgs360024fAccessMgtStatistics = _Mgs360024fAccessMgtStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 2)
)
_Mgs360024fHttpReceivedPkts_Type = Counter32
_Mgs360024fHttpReceivedPkts_Object = MibScalar
mgs360024fHttpReceivedPkts = _Mgs360024fHttpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 2, 1),
    _Mgs360024fHttpReceivedPkts_Type()
)
mgs360024fHttpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fHttpReceivedPkts.setStatus("current")
_Mgs360024fHttpAllowedPkts_Type = Counter32
_Mgs360024fHttpAllowedPkts_Object = MibScalar
mgs360024fHttpAllowedPkts = _Mgs360024fHttpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 2, 2),
    _Mgs360024fHttpAllowedPkts_Type()
)
mgs360024fHttpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fHttpAllowedPkts.setStatus("current")
_Mgs360024fHttpDiscardedPkts_Type = Counter32
_Mgs360024fHttpDiscardedPkts_Object = MibScalar
mgs360024fHttpDiscardedPkts = _Mgs360024fHttpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 2, 3),
    _Mgs360024fHttpDiscardedPkts_Type()
)
mgs360024fHttpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fHttpDiscardedPkts.setStatus("current")
_Mgs360024fHttpsReceivedPkts_Type = Counter32
_Mgs360024fHttpsReceivedPkts_Object = MibScalar
mgs360024fHttpsReceivedPkts = _Mgs360024fHttpsReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 2, 4),
    _Mgs360024fHttpsReceivedPkts_Type()
)
mgs360024fHttpsReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fHttpsReceivedPkts.setStatus("current")
_Mgs360024fHttpsAllowedPkts_Type = Counter32
_Mgs360024fHttpsAllowedPkts_Object = MibScalar
mgs360024fHttpsAllowedPkts = _Mgs360024fHttpsAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 2, 5),
    _Mgs360024fHttpsAllowedPkts_Type()
)
mgs360024fHttpsAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fHttpsAllowedPkts.setStatus("current")
_Mgs360024fHttpsDiscardedPkts_Type = Counter32
_Mgs360024fHttpsDiscardedPkts_Object = MibScalar
mgs360024fHttpsDiscardedPkts = _Mgs360024fHttpsDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 2, 6),
    _Mgs360024fHttpsDiscardedPkts_Type()
)
mgs360024fHttpsDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fHttpsDiscardedPkts.setStatus("current")
_Mgs360024fSnmpReceivedPkts_Type = Counter32
_Mgs360024fSnmpReceivedPkts_Object = MibScalar
mgs360024fSnmpReceivedPkts = _Mgs360024fSnmpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 2, 7),
    _Mgs360024fSnmpReceivedPkts_Type()
)
mgs360024fSnmpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSnmpReceivedPkts.setStatus("current")
_Mgs360024fSnmpAllowedPkts_Type = Counter32
_Mgs360024fSnmpAllowedPkts_Object = MibScalar
mgs360024fSnmpAllowedPkts = _Mgs360024fSnmpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 2, 8),
    _Mgs360024fSnmpAllowedPkts_Type()
)
mgs360024fSnmpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSnmpAllowedPkts.setStatus("current")
_Mgs360024fSnmpDiscardedPkts_Type = Counter32
_Mgs360024fSnmpDiscardedPkts_Object = MibScalar
mgs360024fSnmpDiscardedPkts = _Mgs360024fSnmpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 2, 9),
    _Mgs360024fSnmpDiscardedPkts_Type()
)
mgs360024fSnmpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSnmpDiscardedPkts.setStatus("current")
_Mgs360024fTelnetReceivedPkts_Type = Counter32
_Mgs360024fTelnetReceivedPkts_Object = MibScalar
mgs360024fTelnetReceivedPkts = _Mgs360024fTelnetReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 2, 10),
    _Mgs360024fTelnetReceivedPkts_Type()
)
mgs360024fTelnetReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fTelnetReceivedPkts.setStatus("current")
_Mgs360024fTelnetAllowedPkts_Type = Counter32
_Mgs360024fTelnetAllowedPkts_Object = MibScalar
mgs360024fTelnetAllowedPkts = _Mgs360024fTelnetAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 2, 11),
    _Mgs360024fTelnetAllowedPkts_Type()
)
mgs360024fTelnetAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fTelnetAllowedPkts.setStatus("current")
_Mgs360024fTelnetDiscardedPkts_Type = Counter32
_Mgs360024fTelnetDiscardedPkts_Object = MibScalar
mgs360024fTelnetDiscardedPkts = _Mgs360024fTelnetDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 2, 12),
    _Mgs360024fTelnetDiscardedPkts_Type()
)
mgs360024fTelnetDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fTelnetDiscardedPkts.setStatus("current")
_Mgs360024fSSHReceivedPkts_Type = Counter32
_Mgs360024fSSHReceivedPkts_Object = MibScalar
mgs360024fSSHReceivedPkts = _Mgs360024fSSHReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 2, 13),
    _Mgs360024fSSHReceivedPkts_Type()
)
mgs360024fSSHReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSSHReceivedPkts.setStatus("current")
_Mgs360024fSSHAllowedPkts_Type = Counter32
_Mgs360024fSSHAllowedPkts_Object = MibScalar
mgs360024fSSHAllowedPkts = _Mgs360024fSSHAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 2, 14),
    _Mgs360024fSSHAllowedPkts_Type()
)
mgs360024fSSHAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSSHAllowedPkts.setStatus("current")
_Mgs360024fSSHDiscardedPkts_Type = Counter32
_Mgs360024fSSHDiscardedPkts_Object = MibScalar
mgs360024fSSHDiscardedPkts = _Mgs360024fSSHDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 2, 15),
    _Mgs360024fSSHDiscardedPkts_Type()
)
mgs360024fSSHDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fSSHDiscardedPkts.setStatus("current")


class _Mgs360024fAccessMgtStatisticsClearAll_Type(Integer32):
    """Custom type mgs360024fAccessMgtStatisticsClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fAccessMgtStatisticsClearAll_Type.__name__ = "Integer32"
_Mgs360024fAccessMgtStatisticsClearAll_Object = MibScalar
mgs360024fAccessMgtStatisticsClearAll = _Mgs360024fAccessMgtStatisticsClearAll_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 6, 2, 16),
    _Mgs360024fAccessMgtStatisticsClearAll_Type()
)
mgs360024fAccessMgtStatisticsClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fAccessMgtStatisticsClearAll.setStatus("current")
_Mgs360024fSSH_ObjectIdentity = ObjectIdentity
mgs360024fSSH = _Mgs360024fSSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 7)
)


class _Mgs360024fSSHMode_Type(Integer32):
    """Custom type mgs360024fSSHMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fSSHMode_Type.__name__ = "Integer32"
_Mgs360024fSSHMode_Object = MibScalar
mgs360024fSSHMode = _Mgs360024fSSHMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 7, 1),
    _Mgs360024fSSHMode_Type()
)
mgs360024fSSHMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSSHMode.setStatus("current")
_Mgs360024fHTTPS_ObjectIdentity = ObjectIdentity
mgs360024fHTTPS = _Mgs360024fHTTPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 8)
)


class _Mgs360024fHTTPSMode_Type(Integer32):
    """Custom type mgs360024fHTTPSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fHTTPSMode_Type.__name__ = "Integer32"
_Mgs360024fHTTPSMode_Object = MibScalar
mgs360024fHTTPSMode = _Mgs360024fHTTPSMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 8, 1),
    _Mgs360024fHTTPSMode_Type()
)
mgs360024fHTTPSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fHTTPSMode.setStatus("current")


class _Mgs360024fHTTPSAutoRedirect_Type(Integer32):
    """Custom type mgs360024fHTTPSAutoRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fHTTPSAutoRedirect_Type.__name__ = "Integer32"
_Mgs360024fHTTPSAutoRedirect_Object = MibScalar
mgs360024fHTTPSAutoRedirect = _Mgs360024fHTTPSAutoRedirect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 8, 2),
    _Mgs360024fHTTPSAutoRedirect_Type()
)
mgs360024fHTTPSAutoRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fHTTPSAutoRedirect.setStatus("current")
_Mgs360024fAuthMethod_ObjectIdentity = ObjectIdentity
mgs360024fAuthMethod = _Mgs360024fAuthMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 9)
)


class _Mgs360024fConsoleAuthMethod_Type(Integer32):
    """Custom type mgs360024fConsoleAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Mgs360024fConsoleAuthMethod_Type.__name__ = "Integer32"
_Mgs360024fConsoleAuthMethod_Object = MibScalar
mgs360024fConsoleAuthMethod = _Mgs360024fConsoleAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 9, 1),
    _Mgs360024fConsoleAuthMethod_Type()
)
mgs360024fConsoleAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fConsoleAuthMethod.setStatus("current")


class _Mgs360024fConsoleFallback_Type(Integer32):
    """Custom type mgs360024fConsoleFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fConsoleFallback_Type.__name__ = "Integer32"
_Mgs360024fConsoleFallback_Object = MibScalar
mgs360024fConsoleFallback = _Mgs360024fConsoleFallback_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 9, 2),
    _Mgs360024fConsoleFallback_Type()
)
mgs360024fConsoleFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fConsoleFallback.setStatus("current")


class _Mgs360024fTelnetAuthMethod_Type(Integer32):
    """Custom type mgs360024fTelnetAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Mgs360024fTelnetAuthMethod_Type.__name__ = "Integer32"
_Mgs360024fTelnetAuthMethod_Object = MibScalar
mgs360024fTelnetAuthMethod = _Mgs360024fTelnetAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 9, 3),
    _Mgs360024fTelnetAuthMethod_Type()
)
mgs360024fTelnetAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTelnetAuthMethod.setStatus("current")


class _Mgs360024fTelnetFallback_Type(Integer32):
    """Custom type mgs360024fTelnetFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fTelnetFallback_Type.__name__ = "Integer32"
_Mgs360024fTelnetFallback_Object = MibScalar
mgs360024fTelnetFallback = _Mgs360024fTelnetFallback_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 9, 4),
    _Mgs360024fTelnetFallback_Type()
)
mgs360024fTelnetFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fTelnetFallback.setStatus("current")


class _Mgs360024fSshAuthMethod_Type(Integer32):
    """Custom type mgs360024fSshAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Mgs360024fSshAuthMethod_Type.__name__ = "Integer32"
_Mgs360024fSshAuthMethod_Object = MibScalar
mgs360024fSshAuthMethod = _Mgs360024fSshAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 9, 5),
    _Mgs360024fSshAuthMethod_Type()
)
mgs360024fSshAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSshAuthMethod.setStatus("current")


class _Mgs360024fSshFallback_Type(Integer32):
    """Custom type mgs360024fSshFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fSshFallback_Type.__name__ = "Integer32"
_Mgs360024fSshFallback_Object = MibScalar
mgs360024fSshFallback = _Mgs360024fSshFallback_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 9, 6),
    _Mgs360024fSshFallback_Type()
)
mgs360024fSshFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSshFallback.setStatus("current")


class _Mgs360024fWebAuthMethod_Type(Integer32):
    """Custom type mgs360024fWebAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Mgs360024fWebAuthMethod_Type.__name__ = "Integer32"
_Mgs360024fWebAuthMethod_Object = MibScalar
mgs360024fWebAuthMethod = _Mgs360024fWebAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 9, 7),
    _Mgs360024fWebAuthMethod_Type()
)
mgs360024fWebAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fWebAuthMethod.setStatus("current")


class _Mgs360024fWebFallback_Type(Integer32):
    """Custom type mgs360024fWebFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fWebFallback_Type.__name__ = "Integer32"
_Mgs360024fWebFallback_Object = MibScalar
mgs360024fWebFallback = _Mgs360024fWebFallback_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 3, 9, 8),
    _Mgs360024fWebFallback_Type()
)
mgs360024fWebFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fWebFallback.setStatus("current")
_Mgs360024fMaintenance_ObjectIdentity = ObjectIdentity
mgs360024fMaintenance = _Mgs360024fMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4)
)


class _Mgs360024fRestartDevice_Type(Integer32):
    """Custom type mgs360024fRestartDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fRestartDevice_Type.__name__ = "Integer32"
_Mgs360024fRestartDevice_Object = MibScalar
mgs360024fRestartDevice = _Mgs360024fRestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 1),
    _Mgs360024fRestartDevice_Type()
)
mgs360024fRestartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fRestartDevice.setStatus("current")
_Mgs360024fFirmware_ObjectIdentity = ObjectIdentity
mgs360024fFirmware = _Mgs360024fFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 2)
)
_Mgs360024fFirmwareIpAddress_Type = IpAddress
_Mgs360024fFirmwareIpAddress_Object = MibScalar
mgs360024fFirmwareIpAddress = _Mgs360024fFirmwareIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 2, 1),
    _Mgs360024fFirmwareIpAddress_Type()
)
mgs360024fFirmwareIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fFirmwareIpAddress.setStatus("current")
_Mgs360024fFirmwareFileName_Type = DisplayString
_Mgs360024fFirmwareFileName_Object = MibScalar
mgs360024fFirmwareFileName = _Mgs360024fFirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 2, 2),
    _Mgs360024fFirmwareFileName_Type()
)
mgs360024fFirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fFirmwareFileName.setStatus("current")


class _Mgs360024fDoFirmwareUpgrade_Type(Integer32):
    """Custom type mgs360024fDoFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fDoFirmwareUpgrade_Type.__name__ = "Integer32"
_Mgs360024fDoFirmwareUpgrade_Object = MibScalar
mgs360024fDoFirmwareUpgrade = _Mgs360024fDoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 2, 3),
    _Mgs360024fDoFirmwareUpgrade_Type()
)
mgs360024fDoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fDoFirmwareUpgrade.setStatus("current")
_Mgs360024fSaveOrRestore_ObjectIdentity = ObjectIdentity
mgs360024fSaveOrRestore = _Mgs360024fSaveOrRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 3)
)


class _Mgs360024fFactoryDefaults_Type(Integer32):
    """Custom type mgs360024fFactoryDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fFactoryDefaults_Type.__name__ = "Integer32"
_Mgs360024fFactoryDefaults_Object = MibScalar
mgs360024fFactoryDefaults = _Mgs360024fFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 3, 1),
    _Mgs360024fFactoryDefaults_Type()
)
mgs360024fFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fFactoryDefaults.setStatus("current")


class _Mgs360024fSaveStart_Type(Integer32):
    """Custom type mgs360024fSaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fSaveStart_Type.__name__ = "Integer32"
_Mgs360024fSaveStart_Object = MibScalar
mgs360024fSaveStart = _Mgs360024fSaveStart_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 3, 2),
    _Mgs360024fSaveStart_Type()
)
mgs360024fSaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSaveStart.setStatus("current")


class _Mgs360024fSaveUser_Type(Integer32):
    """Custom type mgs360024fSaveUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fSaveUser_Type.__name__ = "Integer32"
_Mgs360024fSaveUser_Object = MibScalar
mgs360024fSaveUser = _Mgs360024fSaveUser_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 3, 3),
    _Mgs360024fSaveUser_Type()
)
mgs360024fSaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fSaveUser.setStatus("current")


class _Mgs360024fRestoreUser_Type(Integer32):
    """Custom type mgs360024fRestoreUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fRestoreUser_Type.__name__ = "Integer32"
_Mgs360024fRestoreUser_Object = MibScalar
mgs360024fRestoreUser = _Mgs360024fRestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 3, 4),
    _Mgs360024fRestoreUser_Type()
)
mgs360024fRestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fRestoreUser.setStatus("current")
_Mgs360024fExportOrImport_ObjectIdentity = ObjectIdentity
mgs360024fExportOrImport = _Mgs360024fExportOrImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 4)
)
_Mgs360024fExportIpAddress_Type = IpAddress
_Mgs360024fExportIpAddress_Object = MibScalar
mgs360024fExportIpAddress = _Mgs360024fExportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 4, 1),
    _Mgs360024fExportIpAddress_Type()
)
mgs360024fExportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fExportIpAddress.setStatus("current")
_Mgs360024fExportConfigName_Type = DisplayString
_Mgs360024fExportConfigName_Object = MibScalar
mgs360024fExportConfigName = _Mgs360024fExportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 4, 2),
    _Mgs360024fExportConfigName_Type()
)
mgs360024fExportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fExportConfigName.setStatus("current")


class _Mgs360024fDoExportConfig_Type(Integer32):
    """Custom type mgs360024fDoExportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fDoExportConfig_Type.__name__ = "Integer32"
_Mgs360024fDoExportConfig_Object = MibScalar
mgs360024fDoExportConfig = _Mgs360024fDoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 4, 3),
    _Mgs360024fDoExportConfig_Type()
)
mgs360024fDoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fDoExportConfig.setStatus("current")
_Mgs360024fImportIpAddress_Type = IpAddress
_Mgs360024fImportIpAddress_Object = MibScalar
mgs360024fImportIpAddress = _Mgs360024fImportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 4, 4),
    _Mgs360024fImportIpAddress_Type()
)
mgs360024fImportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fImportIpAddress.setStatus("current")
_Mgs360024fImportConfigName_Type = DisplayString
_Mgs360024fImportConfigName_Object = MibScalar
mgs360024fImportConfigName = _Mgs360024fImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 4, 5),
    _Mgs360024fImportConfigName_Type()
)
mgs360024fImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fImportConfigName.setStatus("current")


class _Mgs360024fDoImportConfig_Type(Integer32):
    """Custom type mgs360024fDoImportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fDoImportConfig_Type.__name__ = "Integer32"
_Mgs360024fDoImportConfig_Object = MibScalar
mgs360024fDoImportConfig = _Mgs360024fDoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 4, 6),
    _Mgs360024fDoImportConfig_Type()
)
mgs360024fDoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fDoImportConfig.setStatus("current")
_Mgs360024fDiagnostics_ObjectIdentity = ObjectIdentity
mgs360024fDiagnostics = _Mgs360024fDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5)
)
_Mgs360024fPingIpAddress_Type = IpAddress
_Mgs360024fPingIpAddress_Object = MibScalar
mgs360024fPingIpAddress = _Mgs360024fPingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 1),
    _Mgs360024fPingIpAddress_Type()
)
mgs360024fPingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPingIpAddress.setStatus("current")


class _Mgs360024fPingSize_Type(Integer32):
    """Custom type mgs360024fPingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Mgs360024fPingSize_Type.__name__ = "Integer32"
_Mgs360024fPingSize_Object = MibScalar
mgs360024fPingSize = _Mgs360024fPingSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 2),
    _Mgs360024fPingSize_Type()
)
mgs360024fPingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPingSize.setStatus("current")


class _Mgs360024fDoPingConfig_Type(Integer32):
    """Custom type mgs360024fDoPingConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fDoPingConfig_Type.__name__ = "Integer32"
_Mgs360024fDoPingConfig_Object = MibScalar
mgs360024fDoPingConfig = _Mgs360024fDoPingConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 3),
    _Mgs360024fDoPingConfig_Type()
)
mgs360024fDoPingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fDoPingConfig.setStatus("current")
_Mgs360024fPingResult_Type = DisplayString
_Mgs360024fPingResult_Object = MibScalar
mgs360024fPingResult = _Mgs360024fPingResult_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 4),
    _Mgs360024fPingResult_Type()
)
mgs360024fPingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPingResult.setStatus("current")
_Mgs360024fPing6IpAddress_Type = DisplayString
_Mgs360024fPing6IpAddress_Object = MibScalar
mgs360024fPing6IpAddress = _Mgs360024fPing6IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 5),
    _Mgs360024fPing6IpAddress_Type()
)
mgs360024fPing6IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPing6IpAddress.setStatus("current")


class _Mgs360024fPing6Size_Type(Integer32):
    """Custom type mgs360024fPing6Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Mgs360024fPing6Size_Type.__name__ = "Integer32"
_Mgs360024fPing6Size_Object = MibScalar
mgs360024fPing6Size = _Mgs360024fPing6Size_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 6),
    _Mgs360024fPing6Size_Type()
)
mgs360024fPing6Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fPing6Size.setStatus("current")


class _Mgs360024fDoPing6Config_Type(Integer32):
    """Custom type mgs360024fDoPing6Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Mgs360024fDoPing6Config_Type.__name__ = "Integer32"
_Mgs360024fDoPing6Config_Object = MibScalar
mgs360024fDoPing6Config = _Mgs360024fDoPing6Config_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 7),
    _Mgs360024fDoPing6Config_Type()
)
mgs360024fDoPing6Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fDoPing6Config.setStatus("current")
_Mgs360024fPing6Result_Type = DisplayString
_Mgs360024fPing6Result_Object = MibScalar
mgs360024fPing6Result = _Mgs360024fPing6Result_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 8),
    _Mgs360024fPing6Result_Type()
)
mgs360024fPing6Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fPing6Result.setStatus("current")
_Mgs360024fVeriPHY_ObjectIdentity = ObjectIdentity
mgs360024fVeriPHY = _Mgs360024fVeriPHY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 9)
)


class _Mgs360024fVeriPHYTest_Type(Integer32):
    """Custom type mgs360024fVeriPHYTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fVeriPHYTest_Type.__name__ = "Integer32"
_Mgs360024fVeriPHYTest_Object = MibScalar
mgs360024fVeriPHYTest = _Mgs360024fVeriPHYTest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 9, 1),
    _Mgs360024fVeriPHYTest_Type()
)
mgs360024fVeriPHYTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgs360024fVeriPHYTest.setStatus("current")
_Mgs360024fVeriPHYTable_Object = MibTable
mgs360024fVeriPHYTable = _Mgs360024fVeriPHYTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 9, 2)
)
if mibBuilder.loadTexts:
    mgs360024fVeriPHYTable.setStatus("current")
_Mgs360024fVeriPHYEntry_Object = MibTableRow
mgs360024fVeriPHYEntry = _Mgs360024fVeriPHYEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 9, 2, 1)
)
mgs360024fVeriPHYEntry.setIndexNames(
    (0, "ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fVeriPHYPort"),
)
if mibBuilder.loadTexts:
    mgs360024fVeriPHYEntry.setStatus("current")


class _Mgs360024fVeriPHYPort_Type(Integer32):
    """Custom type mgs360024fVeriPHYPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Mgs360024fVeriPHYPort_Type.__name__ = "Integer32"
_Mgs360024fVeriPHYPort_Object = MibTableColumn
mgs360024fVeriPHYPort = _Mgs360024fVeriPHYPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 9, 2, 1, 1),
    _Mgs360024fVeriPHYPort_Type()
)
mgs360024fVeriPHYPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgs360024fVeriPHYPort.setStatus("current")
_Mgs360024fVeriPHYPairA_Type = DisplayString
_Mgs360024fVeriPHYPairA_Object = MibTableColumn
mgs360024fVeriPHYPairA = _Mgs360024fVeriPHYPairA_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 9, 2, 1, 2),
    _Mgs360024fVeriPHYPairA_Type()
)
mgs360024fVeriPHYPairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fVeriPHYPairA.setStatus("current")
_Mgs360024fVeriPHYLengthA_Type = DisplayString
_Mgs360024fVeriPHYLengthA_Object = MibTableColumn
mgs360024fVeriPHYLengthA = _Mgs360024fVeriPHYLengthA_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 9, 2, 1, 3),
    _Mgs360024fVeriPHYLengthA_Type()
)
mgs360024fVeriPHYLengthA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fVeriPHYLengthA.setStatus("current")
_Mgs360024fVeriPHYPairB_Type = DisplayString
_Mgs360024fVeriPHYPairB_Object = MibTableColumn
mgs360024fVeriPHYPairB = _Mgs360024fVeriPHYPairB_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 9, 2, 1, 4),
    _Mgs360024fVeriPHYPairB_Type()
)
mgs360024fVeriPHYPairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fVeriPHYPairB.setStatus("current")
_Mgs360024fVeriPHYLengthB_Type = DisplayString
_Mgs360024fVeriPHYLengthB_Object = MibTableColumn
mgs360024fVeriPHYLengthB = _Mgs360024fVeriPHYLengthB_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 9, 2, 1, 5),
    _Mgs360024fVeriPHYLengthB_Type()
)
mgs360024fVeriPHYLengthB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fVeriPHYLengthB.setStatus("current")
_Mgs360024fVeriPHYPairC_Type = DisplayString
_Mgs360024fVeriPHYPairC_Object = MibTableColumn
mgs360024fVeriPHYPairC = _Mgs360024fVeriPHYPairC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 9, 2, 1, 6),
    _Mgs360024fVeriPHYPairC_Type()
)
mgs360024fVeriPHYPairC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fVeriPHYPairC.setStatus("current")
_Mgs360024fVeriPHYLengthC_Type = DisplayString
_Mgs360024fVeriPHYLengthC_Object = MibTableColumn
mgs360024fVeriPHYLengthC = _Mgs360024fVeriPHYLengthC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 9, 2, 1, 7),
    _Mgs360024fVeriPHYLengthC_Type()
)
mgs360024fVeriPHYLengthC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fVeriPHYLengthC.setStatus("current")
_Mgs360024fVeriPHYPairD_Type = DisplayString
_Mgs360024fVeriPHYPairD_Object = MibTableColumn
mgs360024fVeriPHYPairD = _Mgs360024fVeriPHYPairD_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 9, 2, 1, 8),
    _Mgs360024fVeriPHYPairD_Type()
)
mgs360024fVeriPHYPairD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fVeriPHYPairD.setStatus("current")
_Mgs360024fVeriPHYLengthD_Type = DisplayString
_Mgs360024fVeriPHYLengthD_Object = MibTableColumn
mgs360024fVeriPHYLengthD = _Mgs360024fVeriPHYLengthD_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 4, 5, 9, 2, 1, 9),
    _Mgs360024fVeriPHYLengthD_Type()
)
mgs360024fVeriPHYLengthD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fVeriPHYLengthD.setStatus("current")
_Mgs360024fTrap_ObjectIdentity = ObjectIdentity
mgs360024fTrap = _Mgs360024fTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 5)
)
_Mgs360024fTrapEvent_ObjectIdentity = ObjectIdentity
mgs360024fTrapEvent = _Mgs360024fTrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 5, 1)
)
_Mgs360024fTrapVariable_ObjectIdentity = ObjectIdentity
mgs360024fTrapVariable = _Mgs360024fTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 5, 2)
)
_Mgs360024fInformation_Type = DisplayString
_Mgs360024fInformation_Object = MibScalar
mgs360024fInformation = _Mgs360024fInformation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 5, 2, 1),
    _Mgs360024fInformation_Type()
)
mgs360024fInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgs360024fInformation.setStatus("current")

# Managed Objects groups


# Notification objects

mgs360024fEmergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 5, 1, 1)
)
mgs360024fEmergency.setObjects(
    ("ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fInformation")
)
if mibBuilder.loadTexts:
    mgs360024fEmergency.setStatus(
        "current"
    )

mgs360024fAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 5, 1, 2)
)
mgs360024fAlert.setObjects(
    ("ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fInformation")
)
if mibBuilder.loadTexts:
    mgs360024fAlert.setStatus(
        "current"
    )

mgs360024fCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 5, 1, 3)
)
mgs360024fCritical.setObjects(
    ("ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fInformation")
)
if mibBuilder.loadTexts:
    mgs360024fCritical.setStatus(
        "current"
    )

mgs360024fError = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 5, 1, 4)
)
mgs360024fError.setObjects(
    ("ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fInformation")
)
if mibBuilder.loadTexts:
    mgs360024fError.setStatus(
        "current"
    )

mgs360024fWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 5, 1, 5)
)
mgs360024fWarning.setObjects(
    ("ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fInformation")
)
if mibBuilder.loadTexts:
    mgs360024fWarning.setStatus(
        "current"
    )

mgs360024fNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 5, 1, 6)
)
mgs360024fNotice.setObjects(
    ("ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fInformation")
)
if mibBuilder.loadTexts:
    mgs360024fNotice.setStatus(
        "current"
    )

mgs360024fInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 5, 1, 7)
)
mgs360024fInformational.setObjects(
    ("ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fInformation")
)
if mibBuilder.loadTexts:
    mgs360024fInformational.setStatus(
        "current"
    )

mgs360024fDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 76, 5, 1, 8)
)
mgs360024fDebug.setObjects(
    ("ZYXEL-MGS360024F-FUNCTION-MIB", "mgs360024fInformation")
)
if mibBuilder.loadTexts:
    mgs360024fDebug.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-MGS360024F-FUNCTION-MIB",
    **{"zyxel": zyxel,
       "products": products,
       "accessSwitch": accessSwitch,
       "esSeries": esSeries,
       "mgs360024fProductId": mgs360024fProductId,
       "mgs360024fSystem": mgs360024fSystem,
       "mgs360024fSystemInformation": mgs360024fSystemInformation,
       "mgs360024fModelName": mgs360024fModelName,
       "mgs360024fBIOSVersion": mgs360024fBIOSVersion,
       "mgs360024fFirmwareVersion": mgs360024fFirmwareVersion,
       "mgs360024fHardwareMechanicalVersion": mgs360024fHardwareMechanicalVersion,
       "mgs360024fSeriesNumber": mgs360024fSeriesNumber,
       "mgs360024fHostMACAddress": mgs360024fHostMACAddress,
       "mgs360024fConsoleBaudrate": mgs360024fConsoleBaudrate,
       "mgs360024fRAMSize": mgs360024fRAMSize,
       "mgs360024fFlashSize": mgs360024fFlashSize,
       "mgs360024fBridgeFBDSize": mgs360024fBridgeFBDSize,
       "mgs360024fTransmitQueue": mgs360024fTransmitQueue,
       "mgs360024fMaximumFrameSize": mgs360024fMaximumFrameSize,
       "mgs360024fCPULoad": mgs360024fCPULoad,
       "mgs360024fFanSpeed": mgs360024fFanSpeed,
       "mgs360024fPowers": mgs360024fPowers,
       "mgs360024fTemperature1": mgs360024fTemperature1,
       "mgs360024fTemperature2": mgs360024fTemperature2,
       "mgs360024fTemperature3": mgs360024fTemperature3,
       "mgs360024fTemperature4": mgs360024fTemperature4,
       "mgs360024fSystemTime": mgs360024fSystemTime,
       "mgs360024fSystemTimeManual": mgs360024fSystemTimeManual,
       "mgs360024fSystemTimeManualClockSource": mgs360024fSystemTimeManualClockSource,
       "mgs360024fSystemTimeManualLocaltime": mgs360024fSystemTimeManualLocaltime,
       "mgs360024fSystemTimeManualTimeZoneOffset": mgs360024fSystemTimeManualTimeZoneOffset,
       "mgs360024fSystemTimeManualDaylightSavings": mgs360024fSystemTimeManualDaylightSavings,
       "mgs360024fSystemTimeManualTimeSetOffset": mgs360024fSystemTimeManualTimeSetOffset,
       "mgs360024fSystemTimeManualDaylightSavingsType": mgs360024fSystemTimeManualDaylightSavingsType,
       "mgs360024fSystemTimeManualDaylightSavingsBydatesFrom": mgs360024fSystemTimeManualDaylightSavingsBydatesFrom,
       "mgs360024fSystemTimeManualDaylightSavingsBydatesTo": mgs360024fSystemTimeManualDaylightSavingsBydatesTo,
       "mgs360024fSystemTimeManualDaylightSavingsRecurringDayFrom": mgs360024fSystemTimeManualDaylightSavingsRecurringDayFrom,
       "mgs360024fSystemTimeManualDaylightSavingsRecurringWeekFrom": mgs360024fSystemTimeManualDaylightSavingsRecurringWeekFrom,
       "mgs360024fSystemTimeManualDaylightSavingsRecurringMonthFrom": mgs360024fSystemTimeManualDaylightSavingsRecurringMonthFrom,
       "mgs360024fSystemTimeManualDaylightSavingsRecurringTimeFrom": mgs360024fSystemTimeManualDaylightSavingsRecurringTimeFrom,
       "mgs360024fSystemTimeManualDaylightSavingsRecurringDayTo": mgs360024fSystemTimeManualDaylightSavingsRecurringDayTo,
       "mgs360024fSystemTimeManualDaylightSavingsRecurringWeekTo": mgs360024fSystemTimeManualDaylightSavingsRecurringWeekTo,
       "mgs360024fSystemTimeManualDaylightSavingsRecurringMonthTo": mgs360024fSystemTimeManualDaylightSavingsRecurringMonthTo,
       "mgs360024fSystemTimeManualDaylightSavingsRecurringTimeTo": mgs360024fSystemTimeManualDaylightSavingsRecurringTimeTo,
       "mgs360024fSystemTimeNTP": mgs360024fSystemTimeNTP,
       "mgs360024fSystemTimeNTPTable": mgs360024fSystemTimeNTPTable,
       "mgs360024fSystemTimeNTPEntry": mgs360024fSystemTimeNTPEntry,
       "mgs360024fSystemTimeNTPIndex": mgs360024fSystemTimeNTPIndex,
       "mgs360024fSystemTimeNTPServerIPType": mgs360024fSystemTimeNTPServerIPType,
       "mgs360024fSystemTimeNTPServer": mgs360024fSystemTimeNTPServer,
       "mgs360024fSystemTimeNTPCurrentMode": mgs360024fSystemTimeNTPCurrentMode,
       "mgs360024fSystemAccount": mgs360024fSystemAccount,
       "mgs360024fSystemAccountUsers": mgs360024fSystemAccountUsers,
       "mgs360024fSystemAccountUserCreate": mgs360024fSystemAccountUserCreate,
       "mgs360024fSystemAccountUsersTable": mgs360024fSystemAccountUsersTable,
       "mgs360024fSystemAccountUsersEntry": mgs360024fSystemAccountUsersEntry,
       "mgs360024fUserIndex": mgs360024fUserIndex,
       "mgs360024fUserName": mgs360024fUserName,
       "mgs360024fPassword": mgs360024fPassword,
       "mgs360024fUserPrivilegeLevel": mgs360024fUserPrivilegeLevel,
       "mgs360024fAccountUserRowStatus": mgs360024fAccountUserRowStatus,
       "mgs360024fSystemAccountPrivilegeLevel": mgs360024fSystemAccountPrivilegeLevel,
       "mgs360024fAccountPrivilegeLevel": mgs360024fAccountPrivilegeLevel,
       "mgs360024fAggregationPrivilegeLevel": mgs360024fAggregationPrivilegeLevel,
       "mgs360024fDiagnosticsPrivilegeLevel": mgs360024fDiagnosticsPrivilegeLevel,
       "mgs360024fEPSPrivilegeLevel": mgs360024fEPSPrivilegeLevel,
       "mgs360024fERPSPrivilegeLevel": mgs360024fERPSPrivilegeLevel,
       "mgs360024fETHLinkOAMPrivilegeLevel": mgs360024fETHLinkOAMPrivilegeLevel,
       "mgs360024fEVCPrivilegeLevel": mgs360024fEVCPrivilegeLevel,
       "mgs360024fGARPPrivilegeLevel": mgs360024fGARPPrivilegeLevel,
       "mgs360024fGVRPPrivilegeLevel": mgs360024fGVRPPrivilegeLevel,
       "mgs360024fIPPrivilegeLevel": mgs360024fIPPrivilegeLevel,
       "mgs360024fIPMCSnoopingPrivilegeLevel": mgs360024fIPMCSnoopingPrivilegeLevel,
       "mgs360024fLACPPrivilegeLevel": mgs360024fLACPPrivilegeLevel,
       "mgs360024fLLDPPrivilegeLevel": mgs360024fLLDPPrivilegeLevel,
       "mgs360024fLLDPMEDPrivilegeLevel": mgs360024fLLDPMEDPrivilegeLevel,
       "mgs360024fLoopProtectPrivilegeLevel": mgs360024fLoopProtectPrivilegeLevel,
       "mgs360024fMACTablePrivilegeLevel": mgs360024fMACTablePrivilegeLevel,
       "mgs360024fMEPPrivilegeLevel": mgs360024fMEPPrivilegeLevel,
       "mgs360024fMRSTPPrivilegeLevel": mgs360024fMRSTPPrivilegeLevel,
       "mgs360024fMVRPrivilegeLevel": mgs360024fMVRPrivilegeLevel,
       "mgs360024fMaintenancePrivilegeLevel": mgs360024fMaintenancePrivilegeLevel,
       "mgs360024fMirroringPrivilegeLevel": mgs360024fMirroringPrivilegeLevel,
       "mgs360024fPTPPrivilegeLevel": mgs360024fPTPPrivilegeLevel,
       "mgs360024fPortsPrivilegeLevel": mgs360024fPortsPrivilegeLevel,
       "mgs360024fPrivateVLANsPrivilegeLevel": mgs360024fPrivateVLANsPrivilegeLevel,
       "mgs360024fQoSPrivilegeLevel": mgs360024fQoSPrivilegeLevel,
       "mgs360024fSMTPPrivilegeLevel": mgs360024fSMTPPrivilegeLevel,
       "mgs360024fSNMPPrivilegeLevel": mgs360024fSNMPPrivilegeLevel,
       "mgs360024fSecurityPrivilegeLevel": mgs360024fSecurityPrivilegeLevel,
       "mgs360024fSpanningTreePrivilegeLevel": mgs360024fSpanningTreePrivilegeLevel,
       "mgs360024fSystemPrivilegeLevel": mgs360024fSystemPrivilegeLevel,
       "mgs360024fTrapEventPrivilegeLevel": mgs360024fTrapEventPrivilegeLevel,
       "mgs360024fVCLPrivilegeLevel": mgs360024fVCLPrivilegeLevel,
       "mgs360024fVLANTranslationPrivilegeLevel": mgs360024fVLANTranslationPrivilegeLevel,
       "mgs360024fVLANsPrivilegeLevel": mgs360024fVLANsPrivilegeLevel,
       "mgs360024fIP": mgs360024fIP,
       "mgs360024fIPv4": mgs360024fIPv4,
       "mgs360024fIPv4Configured": mgs360024fIPv4Configured,
       "mgs360024fIpv4DHCPClient": mgs360024fIpv4DHCPClient,
       "mgs360024fIPv4Address": mgs360024fIPv4Address,
       "mgs360024fIPv4Mask": mgs360024fIPv4Mask,
       "mgs360024fIPv4Router": mgs360024fIPv4Router,
       "mgs360024fIPv4VLANId": mgs360024fIPv4VLANId,
       "mgs360024fIPv4DNSServer": mgs360024fIPv4DNSServer,
       "mgs360024fIPv4DNSProxy": mgs360024fIPv4DNSProxy,
       "mgs360024fIPv4Current": mgs360024fIPv4Current,
       "mgs360024fIpv4CurrentDHCPClient": mgs360024fIpv4CurrentDHCPClient,
       "mgs360024fIPv4CurrentAddress": mgs360024fIPv4CurrentAddress,
       "mgs360024fIPv4CurrentMask": mgs360024fIPv4CurrentMask,
       "mgs360024fIPv4CurrentRouter": mgs360024fIPv4CurrentRouter,
       "mgs360024fIPv4CurrentVLANId": mgs360024fIPv4CurrentVLANId,
       "mgs360024fIPv4CurrentDNSServer": mgs360024fIPv4CurrentDNSServer,
       "mgs360024fIPv6": mgs360024fIPv6,
       "mgs360024fIPv6Configured": mgs360024fIPv6Configured,
       "mgs360024fIpv6AutoConfiguration": mgs360024fIpv6AutoConfiguration,
       "mgs360024fIpv6Address": mgs360024fIpv6Address,
       "mgs360024fIpv6Prefix": mgs360024fIpv6Prefix,
       "mgs360024fIpv6Router": mgs360024fIpv6Router,
       "mgs360024fIPv6Current": mgs360024fIPv6Current,
       "mgs360024fIpv6CurrentAutoConfiguration": mgs360024fIpv6CurrentAutoConfiguration,
       "mgs360024fIpv6CurrentAddress": mgs360024fIpv6CurrentAddress,
       "mgs360024fIpv6CurrentLinkLocalAddress": mgs360024fIpv6CurrentLinkLocalAddress,
       "mgs360024fIpv6CurrentPrefix": mgs360024fIpv6CurrentPrefix,
       "mgs360024fIpv6CurrentRouter": mgs360024fIpv6CurrentRouter,
       "mgs360024fSyslog": mgs360024fSyslog,
       "mgs360024fSyslogConf": mgs360024fSyslogConf,
       "mgs360024fServerMode": mgs360024fServerMode,
       "mgs360024fServerAddress1": mgs360024fServerAddress1,
       "mgs360024fServerAddress2": mgs360024fServerAddress2,
       "mgs360024fSyslogLevel": mgs360024fSyslogLevel,
       "mgs360024fSyslogDetailedInfo": mgs360024fSyslogDetailedInfo,
       "mgs360024fSyslogDetailedInfoClear": mgs360024fSyslogDetailedInfoClear,
       "mgs360024fSyslogDetailedInfoTable": mgs360024fSyslogDetailedInfoTable,
       "mgs360024fSyslogDetailedInfoEntry": mgs360024fSyslogDetailedInfoEntry,
       "mgs360024fSyslogDetailedInfoIndex": mgs360024fSyslogDetailedInfoIndex,
       "mgs360024fSyslogDetailedInfoLevel": mgs360024fSyslogDetailedInfoLevel,
       "mgs360024fSyslogDetailedInfoTime": mgs360024fSyslogDetailedInfoTime,
       "mgs360024fSyslogDetailedInfoMessage": mgs360024fSyslogDetailedInfoMessage,
       "mgs360024fSnmp": mgs360024fSnmp,
       "mgs360024fSnmpConf": mgs360024fSnmpConf,
       "mgs360024fGetCommunity": mgs360024fGetCommunity,
       "mgs360024fSetCommunityMode": mgs360024fSetCommunityMode,
       "mgs360024fSetCommunity": mgs360024fSetCommunity,
       "mgs360024fTrapHostConfTable": mgs360024fTrapHostConfTable,
       "mgs360024fTrapHostConfEntry": mgs360024fTrapHostConfEntry,
       "mgs360024fTrapHostConfIndex": mgs360024fTrapHostConfIndex,
       "mgs360024fTrapHostConfVersion": mgs360024fTrapHostConfVersion,
       "mgs360024fTrapHostConfIPType": mgs360024fTrapHostConfIPType,
       "mgs360024fTrapHostConfIP": mgs360024fTrapHostConfIP,
       "mgs360024fTrapHostConfPort": mgs360024fTrapHostConfPort,
       "mgs360024fTrapHostConfCommunity": mgs360024fTrapHostConfCommunity,
       "mgs360024fTrapHostConfSeverityLevel": mgs360024fTrapHostConfSeverityLevel,
       "mgs360024fTrapHostConfSecurityLevel": mgs360024fTrapHostConfSecurityLevel,
       "mgs360024fTrapHostConfAuthPtc": mgs360024fTrapHostConfAuthPtc,
       "mgs360024fTrapHostConfAuthPassword": mgs360024fTrapHostConfAuthPassword,
       "mgs360024fTrapHostConfPrivPtc": mgs360024fTrapHostConfPrivPtc,
       "mgs360024fTrapHostConfPrivPassword": mgs360024fTrapHostConfPrivPassword,
       "mgs360024fTrapHostConfCurrentMode": mgs360024fTrapHostConfCurrentMode,
       "mgs360024fConfiguration": mgs360024fConfiguration,
       "mgs360024fPort": mgs360024fPort,
       "mgs360024fPortConfigurationTable": mgs360024fPortConfigurationTable,
       "mgs360024fPortConfigurationEntry": mgs360024fPortConfigurationEntry,
       "mgs360024fPortConfPort": mgs360024fPortConfPort,
       "mgs360024fPortConfPortMedia": mgs360024fPortConfPortMedia,
       "mgs360024fPortConfLink": mgs360024fPortConfLink,
       "mgs360024fPortConfCurrentSpeed": mgs360024fPortConfCurrentSpeed,
       "mgs360024fPortConfSpeed": mgs360024fPortConfSpeed,
       "mgs360024fPortConfCurrentFlowControlRx": mgs360024fPortConfCurrentFlowControlRx,
       "mgs360024fPortConfCurrentFlowControlTx": mgs360024fPortConfCurrentFlowControlTx,
       "mgs360024fPortConfFlowControl": mgs360024fPortConfFlowControl,
       "mgs360024fPortConfMaxFrameSize": mgs360024fPortConfMaxFrameSize,
       "mgs360024fPortConfExcessiveCollisionMode": mgs360024fPortConfExcessiveCollisionMode,
       "mgs360024fPortConfPowerControl": mgs360024fPortConfPowerControl,
       "mgs360024fPortConfDescription": mgs360024fPortConfDescription,
       "mgs360024fPortTrafficStatisticsTable": mgs360024fPortTrafficStatisticsTable,
       "mgs360024fPortTrafficStatisticsEntry": mgs360024fPortTrafficStatisticsEntry,
       "mgs360024fPortTrafficStatisticsPort": mgs360024fPortTrafficStatisticsPort,
       "mgs360024fPortTrafficStatisticsClear": mgs360024fPortTrafficStatisticsClear,
       "mgs360024fPortTrafficRxPackets": mgs360024fPortTrafficRxPackets,
       "mgs360024fPortTrafficRxOctets": mgs360024fPortTrafficRxOctets,
       "mgs360024fPortTrafficRxUnicast": mgs360024fPortTrafficRxUnicast,
       "mgs360024fPortTrafficRxMulticast": mgs360024fPortTrafficRxMulticast,
       "mgs360024fPortTrafficRxBroadcast": mgs360024fPortTrafficRxBroadcast,
       "mgs360024fPortTrafficRxPause": mgs360024fPortTrafficRxPause,
       "mgs360024fPortTrafficRx64Bytes": mgs360024fPortTrafficRx64Bytes,
       "mgs360024fPortTrafficRx65to127Bytes": mgs360024fPortTrafficRx65to127Bytes,
       "mgs360024fPortTrafficRx128to255Bytes": mgs360024fPortTrafficRx128to255Bytes,
       "mgs360024fPortTrafficRx256to511Bytes": mgs360024fPortTrafficRx256to511Bytes,
       "mgs360024fPortTrafficRx512to1023Bytes": mgs360024fPortTrafficRx512to1023Bytes,
       "mgs360024fPortTrafficRx1024to1526Bytes": mgs360024fPortTrafficRx1024to1526Bytes,
       "mgs360024fPortTrafficRxExceecd1527Bytes": mgs360024fPortTrafficRxExceecd1527Bytes,
       "mgs360024fPortTrafficRxQ0": mgs360024fPortTrafficRxQ0,
       "mgs360024fPortTrafficRxQ1": mgs360024fPortTrafficRxQ1,
       "mgs360024fPortTrafficRxQ2": mgs360024fPortTrafficRxQ2,
       "mgs360024fPortTrafficRxQ3": mgs360024fPortTrafficRxQ3,
       "mgs360024fPortTrafficRxQ4": mgs360024fPortTrafficRxQ4,
       "mgs360024fPortTrafficRxQ5": mgs360024fPortTrafficRxQ5,
       "mgs360024fPortTrafficRxQ6": mgs360024fPortTrafficRxQ6,
       "mgs360024fPortTrafficRxQ7": mgs360024fPortTrafficRxQ7,
       "mgs360024fPortTrafficRxDrops": mgs360024fPortTrafficRxDrops,
       "mgs360024fPortTrafficRxCRCorAlignment": mgs360024fPortTrafficRxCRCorAlignment,
       "mgs360024fPortTrafficRxUndersize": mgs360024fPortTrafficRxUndersize,
       "mgs360024fPortTrafficRxOversize": mgs360024fPortTrafficRxOversize,
       "mgs360024fPortTrafficRxFragments": mgs360024fPortTrafficRxFragments,
       "mgs360024fPortTrafficRxJabber": mgs360024fPortTrafficRxJabber,
       "mgs360024fPortTrafficRxFiltered": mgs360024fPortTrafficRxFiltered,
       "mgs360024fPortTrafficTxPackets": mgs360024fPortTrafficTxPackets,
       "mgs360024fPortTrafficTxOctets": mgs360024fPortTrafficTxOctets,
       "mgs360024fPortTrafficTxUnicast": mgs360024fPortTrafficTxUnicast,
       "mgs360024fPortTrafficTxMulticast": mgs360024fPortTrafficTxMulticast,
       "mgs360024fPortTrafficTxBroadcast": mgs360024fPortTrafficTxBroadcast,
       "mgs360024fPortTrafficTxPause": mgs360024fPortTrafficTxPause,
       "mgs360024fPortTrafficTx64Bytes": mgs360024fPortTrafficTx64Bytes,
       "mgs360024fPortTrafficTx65to127Bytes": mgs360024fPortTrafficTx65to127Bytes,
       "mgs360024fPortTrafficTx128to255Bytes": mgs360024fPortTrafficTx128to255Bytes,
       "mgs360024fPortTrafficTx256to511Bytes": mgs360024fPortTrafficTx256to511Bytes,
       "mgs360024fPortTrafficTx512to1023Bytes": mgs360024fPortTrafficTx512to1023Bytes,
       "mgs360024fPortTrafficTx1024to1526Bytes": mgs360024fPortTrafficTx1024to1526Bytes,
       "mgs360024fPortTrafficTxExceecd1527Bytes": mgs360024fPortTrafficTxExceecd1527Bytes,
       "mgs360024fPortTrafficTxQ0": mgs360024fPortTrafficTxQ0,
       "mgs360024fPortTrafficTxQ1": mgs360024fPortTrafficTxQ1,
       "mgs360024fPortTrafficTxQ2": mgs360024fPortTrafficTxQ2,
       "mgs360024fPortTrafficTxQ3": mgs360024fPortTrafficTxQ3,
       "mgs360024fPortTrafficTxQ4": mgs360024fPortTrafficTxQ4,
       "mgs360024fPortTrafficTxQ5": mgs360024fPortTrafficTxQ5,
       "mgs360024fPortTrafficTxQ6": mgs360024fPortTrafficTxQ6,
       "mgs360024fPortTrafficTxQ7": mgs360024fPortTrafficTxQ7,
       "mgs360024fPortTrafficTxDrops": mgs360024fPortTrafficTxDrops,
       "mgs360024fPortTrafficTxLateOrExcColl": mgs360024fPortTrafficTxLateOrExcColl,
       "mgs360024fPortQoSStatistics": mgs360024fPortQoSStatistics,
       "mgs360024fPortQoSStatisticsClear": mgs360024fPortQoSStatisticsClear,
       "mgs360024fPortQoSStatisticsTable": mgs360024fPortQoSStatisticsTable,
       "mgs360024fPortQoSStatisticsEntry": mgs360024fPortQoSStatisticsEntry,
       "mgs360024fPortQoSStatisticsPort": mgs360024fPortQoSStatisticsPort,
       "mgs360024fPortQoSQ0Rx": mgs360024fPortQoSQ0Rx,
       "mgs360024fPortQoSQ0Tx": mgs360024fPortQoSQ0Tx,
       "mgs360024fPortQoSQ1Rx": mgs360024fPortQoSQ1Rx,
       "mgs360024fPortQoSQ1Tx": mgs360024fPortQoSQ1Tx,
       "mgs360024fPortQoSQ2Rx": mgs360024fPortQoSQ2Rx,
       "mgs360024fPortQoSQ2Tx": mgs360024fPortQoSQ2Tx,
       "mgs360024fPortQoSQ3Rx": mgs360024fPortQoSQ3Rx,
       "mgs360024fPortQoSQ3Tx": mgs360024fPortQoSQ3Tx,
       "mgs360024fPortQoSQ4Rx": mgs360024fPortQoSQ4Rx,
       "mgs360024fPortQoSQ4Tx": mgs360024fPortQoSQ4Tx,
       "mgs360024fPortQoSQ5Rx": mgs360024fPortQoSQ5Rx,
       "mgs360024fPortQoSQ5Tx": mgs360024fPortQoSQ5Tx,
       "mgs360024fPortQoSQ6Rx": mgs360024fPortQoSQ6Rx,
       "mgs360024fPortQoSQ6Tx": mgs360024fPortQoSQ6Tx,
       "mgs360024fPortQoSQ7Rx": mgs360024fPortQoSQ7Rx,
       "mgs360024fPortQoSQ7Tx": mgs360024fPortQoSQ7Tx,
       "mgs360024fSFPInfoTable": mgs360024fSFPInfoTable,
       "mgs360024fSFPInfoEntry": mgs360024fSFPInfoEntry,
       "mgs360024fSFPInfoIndex": mgs360024fSFPInfoIndex,
       "mgs360024fSFPInfoPort": mgs360024fSFPInfoPort,
       "mgs360024fSFPConnectorType": mgs360024fSFPConnectorType,
       "mgs360024fSFPFiberType": mgs360024fSFPFiberType,
       "mgs360024fSFPTxCentralWavelength": mgs360024fSFPTxCentralWavelength,
       "mgs360024fSFPBaudRate": mgs360024fSFPBaudRate,
       "mgs360024fSFPVendorOUI": mgs360024fSFPVendorOUI,
       "mgs360024fSFPVendorName": mgs360024fSFPVendorName,
       "mgs360024fSFPVendorPN": mgs360024fSFPVendorPN,
       "mgs360024fSFPVendorRev": mgs360024fSFPVendorRev,
       "mgs360024fSFPVendorSN": mgs360024fSFPVendorSN,
       "mgs360024fSFPDateCode": mgs360024fSFPDateCode,
       "mgs360024fSFPTemperature": mgs360024fSFPTemperature,
       "mgs360024fSFPVcc": mgs360024fSFPVcc,
       "mgs360024fSFPMon1Bias": mgs360024fSFPMon1Bias,
       "mgs360024fSFPMon2TxPWR": mgs360024fSFPMon2TxPWR,
       "mgs360024fSFPMon3RxPWR": mgs360024fSFPMon3RxPWR,
       "mgs360024fGARP": mgs360024fGARP,
       "mgs360024fGARPConfTable": mgs360024fGARPConfTable,
       "mgs360024fGARPConfEntry": mgs360024fGARPConfEntry,
       "mgs360024fGARPConfPort": mgs360024fGARPConfPort,
       "mgs360024fGARPJoinTimer": mgs360024fGARPJoinTimer,
       "mgs360024fGARPLeaveTimer": mgs360024fGARPLeaveTimer,
       "mgs360024fGARPLeaveAllTimer": mgs360024fGARPLeaveAllTimer,
       "mgs360024fGARPApplicantion": mgs360024fGARPApplicantion,
       "mgs360024fGARPAttributeType": mgs360024fGARPAttributeType,
       "mgs360024fGARPApplicant": mgs360024fGARPApplicant,
       "mgs360024fGARPStatisticsTable": mgs360024fGARPStatisticsTable,
       "mgs360024fGARPStatisticsEntry": mgs360024fGARPStatisticsEntry,
       "mgs360024fGARPStatisticsPort": mgs360024fGARPStatisticsPort,
       "mgs360024fGARPStatisticsPeerMAC": mgs360024fGARPStatisticsPeerMAC,
       "mgs360024fGARPStatisticsFailedCount": mgs360024fGARPStatisticsFailedCount,
       "mgs360024fGVRP": mgs360024fGVRP,
       "mgs360024fGVRPConf": mgs360024fGVRPConf,
       "mgs360024fGVRPMode": mgs360024fGVRPMode,
       "mgs360024fGVRPConfTable": mgs360024fGVRPConfTable,
       "mgs360024fGVRPConfEntry": mgs360024fGVRPConfEntry,
       "mgs360024fGVRPConfPort": mgs360024fGVRPConfPort,
       "mgs360024fGVRPConfPortMode": mgs360024fGVRPConfPortMode,
       "mgs360024fGVRPConfPortRRole": mgs360024fGVRPConfPortRRole,
       "mgs360024fGVRPStatisticsTable": mgs360024fGVRPStatisticsTable,
       "mgs360024fGVRPStatisticsEntry": mgs360024fGVRPStatisticsEntry,
       "mgs360024fGVRPStatisticsPort": mgs360024fGVRPStatisticsPort,
       "mgs360024fGVRPStatisticsJoinTxCnt": mgs360024fGVRPStatisticsJoinTxCnt,
       "mgs360024fGVRPStatisticsLeaveTxCnt": mgs360024fGVRPStatisticsLeaveTxCnt,
       "mgs360024fThermalProtection": mgs360024fThermalProtection,
       "mgs360024fPriority0Temperature": mgs360024fPriority0Temperature,
       "mgs360024fPriority1Temperature": mgs360024fPriority1Temperature,
       "mgs360024fPriority2Temperature": mgs360024fPriority2Temperature,
       "mgs360024fPriority3Temperature": mgs360024fPriority3Temperature,
       "mgs360024fThermalProtectionTable": mgs360024fThermalProtectionTable,
       "mgs360024fThermalProtectionEntry": mgs360024fThermalProtectionEntry,
       "mgs360024fThermalProtectionPort": mgs360024fThermalProtectionPort,
       "mgs360024fThermalProtectionPortTemperature": mgs360024fThermalProtectionPortTemperature,
       "mgs360024fThermalProtectionPortPriority": mgs360024fThermalProtectionPortPriority,
       "mgs360024fThermalProtectionPortStatus": mgs360024fThermalProtectionPortStatus,
       "mgs360024fMirroring": mgs360024fMirroring,
       "mgs360024fPortToMirrorOn": mgs360024fPortToMirrorOn,
       "mgs360024fMirrorTable": mgs360024fMirrorTable,
       "mgs360024fMirrorEntry": mgs360024fMirrorEntry,
       "mgs360024fMirrorPort": mgs360024fMirrorPort,
       "mgs360024fMirrorMode": mgs360024fMirrorMode,
       "mgs360024fTrapEventSeverity": mgs360024fTrapEventSeverity,
       "mgs360024fTrapEventSeverityACL": mgs360024fTrapEventSeverityACL,
       "mgs360024fTrapEventSeverityACLLog": mgs360024fTrapEventSeverityACLLog,
       "mgs360024fTrapEventSeverityAccessMgmt": mgs360024fTrapEventSeverityAccessMgmt,
       "mgs360024fTrapEventSeverityAuthFailed": mgs360024fTrapEventSeverityAuthFailed,
       "mgs360024fTrapEventSeverityColdStart": mgs360024fTrapEventSeverityColdStart,
       "mgs360024fTrapEventSeverityConfigInfo": mgs360024fTrapEventSeverityConfigInfo,
       "mgs360024fTrapEventSeverityFirmwareUpgrade": mgs360024fTrapEventSeverityFirmwareUpgrade,
       "mgs360024fTrapEventSeverityImportExport": mgs360024fTrapEventSeverityImportExport,
       "mgs360024fTrapEventSeverityLACP": mgs360024fTrapEventSeverityLACP,
       "mgs360024fTrapEventSeverityLinkStatus": mgs360024fTrapEventSeverityLinkStatus,
       "mgs360024fTrapEventSeverityLogin": mgs360024fTrapEventSeverityLogin,
       "mgs360024fTrapEventSeverityLogout": mgs360024fTrapEventSeverityLogout,
       "mgs360024fTrapEventSeverityLoopProtect": mgs360024fTrapEventSeverityLoopProtect,
       "mgs360024fTrapEventSeverityMgmtIPChange": mgs360024fTrapEventSeverityMgmtIPChange,
       "mgs360024fTrapEventSeverityModuleChange": mgs360024fTrapEventSeverityModuleChange,
       "mgs360024fTrapEventSeverityNAS": mgs360024fTrapEventSeverityNAS,
       "mgs360024fTrapEventSeverityPasswdChange": mgs360024fTrapEventSeverityPasswdChange,
       "mgs360024fTrapEventSeverityPortSecurity": mgs360024fTrapEventSeverityPortSecurity,
       "mgs360024fTrapEventSeverityThermalProtect": mgs360024fTrapEventSeverityThermalProtect,
       "mgs360024fTrapEventSeverityVLAN": mgs360024fTrapEventSeverityVLAN,
       "mgs360024fTrapEventSeverityWarmStart": mgs360024fTrapEventSeverityWarmStart,
       "mgs360024fSMTP": mgs360024fSMTP,
       "mgs360024fSMTPMailServer": mgs360024fSMTPMailServer,
       "mgs360024fSMTPUserName": mgs360024fSMTPUserName,
       "mgs360024fSMTPPassword": mgs360024fSMTPPassword,
       "mgs360024fSMTPServeriryLevel": mgs360024fSMTPServeriryLevel,
       "mgs360024fSMTPSender": mgs360024fSMTPSender,
       "mgs360024fSMTPReturnPath": mgs360024fSMTPReturnPath,
       "mgs360024fSMTPEmailAddress1": mgs360024fSMTPEmailAddress1,
       "mgs360024fSMTPEmailAddress2": mgs360024fSMTPEmailAddress2,
       "mgs360024fSMTPEmailAddress3": mgs360024fSMTPEmailAddress3,
       "mgs360024fSMTPEmailAddress4": mgs360024fSMTPEmailAddress4,
       "mgs360024fSMTPEmailAddress5": mgs360024fSMTPEmailAddress5,
       "mgs360024fSMTPEmailAddress6": mgs360024fSMTPEmailAddress6,
       "mgs360024fACL": mgs360024fACL,
       "mgs360024fACLPortsConfTable": mgs360024fACLPortsConfTable,
       "mgs360024fACLPortsConfEntry": mgs360024fACLPortsConfEntry,
       "mgs360024fACLPortsConfPort": mgs360024fACLPortsConfPort,
       "mgs360024fACLPortsConfPolicyID": mgs360024fACLPortsConfPolicyID,
       "mgs360024fACLPortsConfAction": mgs360024fACLPortsConfAction,
       "mgs360024fACLPortsConfRateLimiterID": mgs360024fACLPortsConfRateLimiterID,
       "mgs360024fACLPortsConfPortRedirect": mgs360024fACLPortsConfPortRedirect,
       "mgs360024fACLPortsConfLogging": mgs360024fACLPortsConfLogging,
       "mgs360024fACLPortsConfShutdown": mgs360024fACLPortsConfShutdown,
       "mgs360024fACLPortsConfState": mgs360024fACLPortsConfState,
       "mgs360024fACLPortsConfCounter": mgs360024fACLPortsConfCounter,
       "mgs360024fACLRateLimiterTable": mgs360024fACLRateLimiterTable,
       "mgs360024fACLRateLimiterEntry": mgs360024fACLRateLimiterEntry,
       "mgs360024fACLRateLimiterID": mgs360024fACLRateLimiterID,
       "mgs360024fACLRateLimiterRate": mgs360024fACLRateLimiterRate,
       "mgs360024fACLACE": mgs360024fACLACE,
       "mgs360024fACLACECreate": mgs360024fACLACECreate,
       "mgs360024fACLACETable": mgs360024fACLACETable,
       "mgs360024fACLACEEntry": mgs360024fACLACEEntry,
       "mgs360024fACLACEIndex": mgs360024fACLACEIndex,
       "mgs360024fACLACEID": mgs360024fACLACEID,
       "mgs360024fACLACENextID": mgs360024fACLACENextID,
       "mgs360024fACLACEIngressPort": mgs360024fACLACEIngressPort,
       "mgs360024fACLACEPortPolicyNumber": mgs360024fACLACEPortPolicyNumber,
       "mgs360024fACLACEPortPolicyBitmask": mgs360024fACLACEPortPolicyBitmask,
       "mgs360024fACLACEFrameType": mgs360024fACLACEFrameType,
       "mgs360024fACLACEAction": mgs360024fACLACEAction,
       "mgs360024fACLACEDenyPortRedirect": mgs360024fACLACEDenyPortRedirect,
       "mgs360024fACLACELogging": mgs360024fACLACELogging,
       "mgs360024fACLACERateLimiter": mgs360024fACLACERateLimiter,
       "mgs360024fACLACEShutdown": mgs360024fACLACEShutdown,
       "mgs360024fACLACEVLANTagPriority": mgs360024fACLACEVLANTagPriority,
       "mgs360024fACLACEVLANVID": mgs360024fACLACEVLANVID,
       "mgs360024fACLACEEtherType": mgs360024fACLACEEtherType,
       "mgs360024fACLACESMAC": mgs360024fACLACESMAC,
       "mgs360024fACLACEDMACType": mgs360024fACLACEDMACType,
       "mgs360024fACLACEDMAC": mgs360024fACLACEDMAC,
       "mgs360024fACLACEArpOpcode": mgs360024fACLACEArpOpcode,
       "mgs360024fACLACEArpFlagsRequestReply": mgs360024fACLACEArpFlagsRequestReply,
       "mgs360024fACLACEArpFlagsArpSmac": mgs360024fACLACEArpFlagsArpSmac,
       "mgs360024fACLACEArpFlagsRarpDmac": mgs360024fACLACEArpFlagsRarpDmac,
       "mgs360024fACLACEArpFlagsLength": mgs360024fACLACEArpFlagsLength,
       "mgs360024fACLACEArpFlagsIp": mgs360024fACLACEArpFlagsIp,
       "mgs360024fACLACEArpFlagsEthernet": mgs360024fACLACEArpFlagsEthernet,
       "mgs360024fACLACESIPType": mgs360024fACLACESIPType,
       "mgs360024fACLACESIPIPAddress": mgs360024fACLACESIPIPAddress,
       "mgs360024fACLACESIPNetworkPrefix": mgs360024fACLACESIPNetworkPrefix,
       "mgs360024fACLACEDIPType": mgs360024fACLACEDIPType,
       "mgs360024fACLACEDIPIPAddress": mgs360024fACLACEDIPIPAddress,
       "mgs360024fACLACEDIPNetworkPrefix": mgs360024fACLACEDIPNetworkPrefix,
       "mgs360024fACLACEIPProtocol": mgs360024fACLACEIPProtocol,
       "mgs360024fACLACEIPFlagsTTL": mgs360024fACLACEIPFlagsTTL,
       "mgs360024fACLACEIPFlagsOptions": mgs360024fACLACEIPFlagsOptions,
       "mgs360024fACLACEIPFlagsFragment": mgs360024fACLACEIPFlagsFragment,
       "mgs360024fACLACEICMPType": mgs360024fACLACEICMPType,
       "mgs360024fACLACEICMPCode": mgs360024fACLACEICMPCode,
       "mgs360024fACLACESourcePortMin": mgs360024fACLACESourcePortMin,
       "mgs360024fACLACESourcePortMax": mgs360024fACLACESourcePortMax,
       "mgs360024fACLACEDestPortMin": mgs360024fACLACEDestPortMin,
       "mgs360024fACLACEDestPortMax": mgs360024fACLACEDestPortMax,
       "mgs360024fACLACETCPFlagsFin": mgs360024fACLACETCPFlagsFin,
       "mgs360024fACLACETCPFlagsSyn": mgs360024fACLACETCPFlagsSyn,
       "mgs360024fACLACETCPFlagsRst": mgs360024fACLACETCPFlagsRst,
       "mgs360024fACLACETCPFlagsPsh": mgs360024fACLACETCPFlagsPsh,
       "mgs360024fACLACETCPFlagsAck": mgs360024fACLACETCPFlagsAck,
       "mgs360024fACLACETCPFlagsUrg": mgs360024fACLACETCPFlagsUrg,
       "mgs360024fACLACERowStatus": mgs360024fACLACERowStatus,
       "mgs360024fACLACEClear": mgs360024fACLACEClear,
       "mgs360024fACLACEMoveACEID": mgs360024fACLACEMoveACEID,
       "mgs360024fACLACEMoveNextACEID": mgs360024fACLACEMoveNextACEID,
       "mgs360024fACLACEStatusTable": mgs360024fACLACEStatusTable,
       "mgs360024fACLACEStatusEntry": mgs360024fACLACEStatusEntry,
       "mgs360024fACLACEStatusIndex": mgs360024fACLACEStatusIndex,
       "mgs360024fACLACEStatusUser": mgs360024fACLACEStatusUser,
       "mgs360024fACLACEStatusID": mgs360024fACLACEStatusID,
       "mgs360024fACLACEStatusIngressPort": mgs360024fACLACEStatusIngressPort,
       "mgs360024fACLACEStatusFrameType": mgs360024fACLACEStatusFrameType,
       "mgs360024fACLACEStatusAction": mgs360024fACLACEStatusAction,
       "mgs360024fACLACEStatusRateLimiter": mgs360024fACLACEStatusRateLimiter,
       "mgs360024fACLACEStatusPortCopy": mgs360024fACLACEStatusPortCopy,
       "mgs360024fACLACEStatusMirror": mgs360024fACLACEStatusMirror,
       "mgs360024fACLACEStatusCPU": mgs360024fACLACEStatusCPU,
       "mgs360024fACLACEStatusCounter": mgs360024fACLACEStatusCounter,
       "mgs360024fACLACEStatusConflict": mgs360024fACLACEStatusConflict,
       "mgs360024fERPS": mgs360024fERPS,
       "mgs360024fERPSConf": mgs360024fERPSConf,
       "mgs360024fERPSConfCreate": mgs360024fERPSConfCreate,
       "mgs360024fERPSConfTable": mgs360024fERPSConfTable,
       "mgs360024fERPSConfEntry": mgs360024fERPSConfEntry,
       "mgs360024fERPSConfIndex": mgs360024fERPSConfIndex,
       "mgs360024fERPSConfERPSID": mgs360024fERPSConfERPSID,
       "mgs360024fERPSConfPort0": mgs360024fERPSConfPort0,
       "mgs360024fERPSConfPort1": mgs360024fERPSConfPort1,
       "mgs360024fERPSConfPort0SFMEP": mgs360024fERPSConfPort0SFMEP,
       "mgs360024fERPSConfPort1SFMEP": mgs360024fERPSConfPort1SFMEP,
       "mgs360024fERPSConfPort0APSMEP": mgs360024fERPSConfPort0APSMEP,
       "mgs360024fERPSConfPort1APSMEP": mgs360024fERPSConfPort1APSMEP,
       "mgs360024fERPSConfRingType": mgs360024fERPSConfRingType,
       "mgs360024fERPSConfInterconnectedNode": mgs360024fERPSConfInterconnectedNode,
       "mgs360024fERPSConfVirtualChannel": mgs360024fERPSConfVirtualChannel,
       "mgs360024fERPSConfMajorRingID": mgs360024fERPSConfMajorRingID,
       "mgs360024fERPSConfAlarm": mgs360024fERPSConfAlarm,
       "mgs360024fERPSInstanceConfConfigured": mgs360024fERPSInstanceConfConfigured,
       "mgs360024fERPSInstanceConfGuardTime": mgs360024fERPSInstanceConfGuardTime,
       "mgs360024fERPSInstanceConfWTRTime": mgs360024fERPSInstanceConfWTRTime,
       "mgs360024fERPSInstanceConfHoldOffTime": mgs360024fERPSInstanceConfHoldOffTime,
       "mgs360024fERPSInstanceConfVersion": mgs360024fERPSInstanceConfVersion,
       "mgs360024fERPSInstanceConfRevertive": mgs360024fERPSInstanceConfRevertive,
       "mgs360024fERPSInstanceConfVLANconfig": mgs360024fERPSInstanceConfVLANconfig,
       "mgs360024fERPSConfRowStatus": mgs360024fERPSConfRowStatus,
       "mgs360024fMRSTP": mgs360024fMRSTP,
       "mgs360024fMRSTPInstance": mgs360024fMRSTPInstance,
       "mgs360024fMRSTPInstanceConf": mgs360024fMRSTPInstanceConf,
       "mgs360024fMRSTPInstanceConfGlobalState": mgs360024fMRSTPInstanceConfGlobalState,
       "mgs360024fMRSTPInstanceConfigurationTable": mgs360024fMRSTPInstanceConfigurationTable,
       "mgs360024fMRSTPInstanceConfigurationEntry": mgs360024fMRSTPInstanceConfigurationEntry,
       "mgs360024fMRSTPInstanceConfigurationInstance": mgs360024fMRSTPInstanceConfigurationInstance,
       "mgs360024fMRSTPInstanceConfigurationState": mgs360024fMRSTPInstanceConfigurationState,
       "mgs360024fMRSTPInstanceConfigurationVersion": mgs360024fMRSTPInstanceConfigurationVersion,
       "mgs360024fMRSTPInstanceConfigurationPriority": mgs360024fMRSTPInstanceConfigurationPriority,
       "mgs360024fMRSTPInstanceConfigurationHelloTime": mgs360024fMRSTPInstanceConfigurationHelloTime,
       "mgs360024fMRSTPInstanceConfigurationMaxAge": mgs360024fMRSTPInstanceConfigurationMaxAge,
       "mgs360024fMRSTPInstanceConfigurationFWDelay": mgs360024fMRSTPInstanceConfigurationFWDelay,
       "mgs360024fMRSTPInstanceStatus": mgs360024fMRSTPInstanceStatus,
       "mgs360024fMRSTPInstanceStatusTable": mgs360024fMRSTPInstanceStatusTable,
       "mgs360024fMRSTPInstanceStatusEntry": mgs360024fMRSTPInstanceStatusEntry,
       "mgs360024fMRSTPInstanceStatusInstance": mgs360024fMRSTPInstanceStatusInstance,
       "mgs360024fMRSTPInstanceStatusGlobalState": mgs360024fMRSTPInstanceStatusGlobalState,
       "mgs360024fMRSTPInstanceStatusInstanceConfigState": mgs360024fMRSTPInstanceStatusInstanceConfigState,
       "mgs360024fMRSTPInstanceStatusInstanceCurrentState": mgs360024fMRSTPInstanceStatusInstanceCurrentState,
       "mgs360024fMRSTPInstanceStatusBridgeID": mgs360024fMRSTPInstanceStatusBridgeID,
       "mgs360024fMRSTPInstanceStatusBridgePrioriry": mgs360024fMRSTPInstanceStatusBridgePrioriry,
       "mgs360024fMRSTPInstanceStatusRootID": mgs360024fMRSTPInstanceStatusRootID,
       "mgs360024fMRSTPInstanceStatusRootPriority": mgs360024fMRSTPInstanceStatusRootPriority,
       "mgs360024fMRSTPInstanceStatusRootPort": mgs360024fMRSTPInstanceStatusRootPort,
       "mgs360024fMRSTPInstanceStatusRootPathCost": mgs360024fMRSTPInstanceStatusRootPathCost,
       "mgs360024fMRSTPInstanceStatusCurrentMaxAge": mgs360024fMRSTPInstanceStatusCurrentMaxAge,
       "mgs360024fMRSTPInstanceStatusCurrentForwardDelay": mgs360024fMRSTPInstanceStatusCurrentForwardDelay,
       "mgs360024fMRSTPInstanceStatusHelloTime": mgs360024fMRSTPInstanceStatusHelloTime,
       "mgs360024fMRSTPInstanceStatusTopologyChangeCount": mgs360024fMRSTPInstanceStatusTopologyChangeCount,
       "mgs360024fMRSTPInstanceStatusTimeSinceLastTopologyChange": mgs360024fMRSTPInstanceStatusTimeSinceLastTopologyChange,
       "mgs360024fMRSTPPort": mgs360024fMRSTPPort,
       "mgs360024fMRSTPPortConfiguration": mgs360024fMRSTPPortConfiguration,
       "mgs360024fMRSTPPortConfigurationTable": mgs360024fMRSTPPortConfigurationTable,
       "mgs360024fMRSTPPortConfigurationEntry": mgs360024fMRSTPPortConfigurationEntry,
       "mgs360024fMRSTPPortConfigurationPort": mgs360024fMRSTPPortConfigurationPort,
       "mgs360024fMRSTPPortConfigurationInstance": mgs360024fMRSTPPortConfigurationInstance,
       "mgs360024fMRSTPPortConfigurationPathCost": mgs360024fMRSTPPortConfigurationPathCost,
       "mgs360024fMRSTPPortConfigurationPriority": mgs360024fMRSTPPortConfigurationPriority,
       "mgs360024fMRSTPPortConfigurationAdminEdge": mgs360024fMRSTPPortConfigurationAdminEdge,
       "mgs360024fMRSTPPortConfigurationAdminP2P": mgs360024fMRSTPPortConfigurationAdminP2P,
       "mgs360024fMRSTPPortConfigurationMigrateCheck": mgs360024fMRSTPPortConfigurationMigrateCheck,
       "mgs360024fMRSTPPortStatus": mgs360024fMRSTPPortStatus,
       "mgs360024fMRSTPPortStatusTable": mgs360024fMRSTPPortStatusTable,
       "mgs360024fMRSTPPortStatusEntry": mgs360024fMRSTPPortStatusEntry,
       "mgs360024fMRSTPPortStatusPort": mgs360024fMRSTPPortStatusPort,
       "mgs360024fMRSTPPortStatusInstance": mgs360024fMRSTPPortStatusInstance,
       "mgs360024fMRSTPPortStatusState": mgs360024fMRSTPPortStatusState,
       "mgs360024fMRSTPPortStatusRole": mgs360024fMRSTPPortStatusRole,
       "mgs360024fMRSTPPortStatusPathCost": mgs360024fMRSTPPortStatusPathCost,
       "mgs360024fMRSTPPortStatusPathCostConfig": mgs360024fMRSTPPortStatusPathCostConfig,
       "mgs360024fMRSTPPortStatusPriority": mgs360024fMRSTPPortStatusPriority,
       "mgs360024fMRSTPPortStatusAdminEdge": mgs360024fMRSTPPortStatusAdminEdge,
       "mgs360024fMRSTPPortStatusAdminP2P": mgs360024fMRSTPPortStatusAdminP2P,
       "mgs360024fSecurity": mgs360024fSecurity,
       "mgs360024fIPSourceGuard": mgs360024fIPSourceGuard,
       "mgs360024fIPSourceGuardConf": mgs360024fIPSourceGuardConf,
       "mgs360024fIPSourceGuardMode": mgs360024fIPSourceGuardMode,
       "mgs360024fIPSourceGuardPortConfigTable": mgs360024fIPSourceGuardPortConfigTable,
       "mgs360024fIPSourceGuardPortConfigEntry": mgs360024fIPSourceGuardPortConfigEntry,
       "mgs360024fIPSourceGuardPortConfigPort": mgs360024fIPSourceGuardPortConfigPort,
       "mgs360024fIPSourceGuardPortConfigMode": mgs360024fIPSourceGuardPortConfigMode,
       "mgs360024fIPSourceGuardPortMaxDynamicClients": mgs360024fIPSourceGuardPortMaxDynamicClients,
       "mgs360024fIPSourceGuardStatic": mgs360024fIPSourceGuardStatic,
       "mgs360024fIPSourceGuardStaticCreate": mgs360024fIPSourceGuardStaticCreate,
       "mgs360024fIPSourceGuardStaticTable": mgs360024fIPSourceGuardStaticTable,
       "mgs360024fIPSourceGuardStaticEntry": mgs360024fIPSourceGuardStaticEntry,
       "mgs360024fIPSourceGuardStaticIndex": mgs360024fIPSourceGuardStaticIndex,
       "mgs360024fIPSourceGuardStaticPort": mgs360024fIPSourceGuardStaticPort,
       "mgs360024fIPSourceGuardStaticVLANId": mgs360024fIPSourceGuardStaticVLANId,
       "mgs360024fIPSourceGuardStaticIPAddress": mgs360024fIPSourceGuardStaticIPAddress,
       "mgs360024fIPSourceGuardStaticMACAddress": mgs360024fIPSourceGuardStaticMACAddress,
       "mgs360024fIPSourceGuardStaticRowStatus": mgs360024fIPSourceGuardStaticRowStatus,
       "mgs360024fIPSourceGuardDynamicTable": mgs360024fIPSourceGuardDynamicTable,
       "mgs360024fIPSourceGuardDynamicEntry": mgs360024fIPSourceGuardDynamicEntry,
       "mgs360024fIPSourceGuardDynamicIndex": mgs360024fIPSourceGuardDynamicIndex,
       "mgs360024fIPSourceGuardDynamicPort": mgs360024fIPSourceGuardDynamicPort,
       "mgs360024fIPSourceGuardDynamicVLANId": mgs360024fIPSourceGuardDynamicVLANId,
       "mgs360024fIPSourceGuardDynamicIPAddress": mgs360024fIPSourceGuardDynamicIPAddress,
       "mgs360024fIPSourceGuardDynamicMACAddress": mgs360024fIPSourceGuardDynamicMACAddress,
       "mgs360024fARPInspection": mgs360024fARPInspection,
       "mgs360024fARPInspectionConf": mgs360024fARPInspectionConf,
       "mgs360024fARPInspectionConfMode": mgs360024fARPInspectionConfMode,
       "mgs360024fARPInspectionConfTable": mgs360024fARPInspectionConfTable,
       "mgs360024fARPInspectionConfEntry": mgs360024fARPInspectionConfEntry,
       "mgs360024fARPInspectionConfPortIndex": mgs360024fARPInspectionConfPortIndex,
       "mgs360024fARPInspectionConfPortMode": mgs360024fARPInspectionConfPortMode,
       "mgs360024fARPInspectionStatic": mgs360024fARPInspectionStatic,
       "mgs360024fARPInspectionStaticCreate": mgs360024fARPInspectionStaticCreate,
       "mgs360024fARPInspectionStaticTable": mgs360024fARPInspectionStaticTable,
       "mgs360024fARPInspectionStaticEntry": mgs360024fARPInspectionStaticEntry,
       "mgs360024fARPInspectionStaticIndex": mgs360024fARPInspectionStaticIndex,
       "mgs360024fARPInspectionStaticPort": mgs360024fARPInspectionStaticPort,
       "mgs360024fARPInspectionStaticVLANId": mgs360024fARPInspectionStaticVLANId,
       "mgs360024fARPInspectionStaticIPAddress": mgs360024fARPInspectionStaticIPAddress,
       "mgs360024fARPInspectionStaticMACAddress": mgs360024fARPInspectionStaticMACAddress,
       "mgs360024fARPInspectionStaticRowStatus": mgs360024fARPInspectionStaticRowStatus,
       "mgs360024fARPInspectionDynamicTable": mgs360024fARPInspectionDynamicTable,
       "mgs360024fARPInspectionDynamicEntry": mgs360024fARPInspectionDynamicEntry,
       "mgs360024fARPInspectionDynamicIndex": mgs360024fARPInspectionDynamicIndex,
       "mgs360024fARPInspectionDynamicPort": mgs360024fARPInspectionDynamicPort,
       "mgs360024fARPInspectionDynamicVLANId": mgs360024fARPInspectionDynamicVLANId,
       "mgs360024fARPInspectionDynamicIPAddress": mgs360024fARPInspectionDynamicIPAddress,
       "mgs360024fARPInspectionDynamicMACAddress": mgs360024fARPInspectionDynamicMACAddress,
       "mgs360024fDHCPSnooping": mgs360024fDHCPSnooping,
       "mgs360024fDHCPSnoopingConf": mgs360024fDHCPSnoopingConf,
       "mgs360024fDHCPSnoopingMode": mgs360024fDHCPSnoopingMode,
       "mgs360024fDHCPSnoopingPortModeConfigurationTable": mgs360024fDHCPSnoopingPortModeConfigurationTable,
       "mgs360024fDHCPSnoopingPortModeConfigurationEntry": mgs360024fDHCPSnoopingPortModeConfigurationEntry,
       "mgs360024fDHCPSnoopingPortModeConfigurationPort": mgs360024fDHCPSnoopingPortModeConfigurationPort,
       "mgs360024fDHCPSnoopingPortModeConfigurationMode": mgs360024fDHCPSnoopingPortModeConfigurationMode,
       "mgs360024fDHCPSnoopingStatisticsTable": mgs360024fDHCPSnoopingStatisticsTable,
       "mgs360024fDHCPSnoopingStatisticsEntry": mgs360024fDHCPSnoopingStatisticsEntry,
       "mgs360024fDHCPSnoopingStatisticsPort": mgs360024fDHCPSnoopingStatisticsPort,
       "mgs360024fDHCPSnoopingStatisticsClear": mgs360024fDHCPSnoopingStatisticsClear,
       "mgs360024fDHCPSnoopingRxDiscover": mgs360024fDHCPSnoopingRxDiscover,
       "mgs360024fDHCPSnoopingRxOffer": mgs360024fDHCPSnoopingRxOffer,
       "mgs360024fDHCPSnoopingRxRequest": mgs360024fDHCPSnoopingRxRequest,
       "mgs360024fDHCPSnoopingRxDecline": mgs360024fDHCPSnoopingRxDecline,
       "mgs360024fDHCPSnoopingRxACK": mgs360024fDHCPSnoopingRxACK,
       "mgs360024fDHCPSnoopingRxNAK": mgs360024fDHCPSnoopingRxNAK,
       "mgs360024fDHCPSnoopingRxRelease": mgs360024fDHCPSnoopingRxRelease,
       "mgs360024fDHCPSnoopingRxInform": mgs360024fDHCPSnoopingRxInform,
       "mgs360024fDHCPSnoopingRxLeaseQuery": mgs360024fDHCPSnoopingRxLeaseQuery,
       "mgs360024fDHCPSnoopingRxLeaseUnassigned": mgs360024fDHCPSnoopingRxLeaseUnassigned,
       "mgs360024fDHCPSnoopingRxLeaseUnknown": mgs360024fDHCPSnoopingRxLeaseUnknown,
       "mgs360024fDHCPSnoopingRxLeaseActive": mgs360024fDHCPSnoopingRxLeaseActive,
       "mgs360024fDHCPSnoopingTxDiscover": mgs360024fDHCPSnoopingTxDiscover,
       "mgs360024fDHCPSnoopingTxOffer": mgs360024fDHCPSnoopingTxOffer,
       "mgs360024fDHCPSnoopingTxRequest": mgs360024fDHCPSnoopingTxRequest,
       "mgs360024fDHCPSnoopingTxDecline": mgs360024fDHCPSnoopingTxDecline,
       "mgs360024fDHCPSnoopingTxACK": mgs360024fDHCPSnoopingTxACK,
       "mgs360024fDHCPSnoopingTxNAK": mgs360024fDHCPSnoopingTxNAK,
       "mgs360024fDHCPSnoopingTxRelease": mgs360024fDHCPSnoopingTxRelease,
       "mgs360024fDHCPSnoopingTxInform": mgs360024fDHCPSnoopingTxInform,
       "mgs360024fDHCPSnoopingTxLeaseQuery": mgs360024fDHCPSnoopingTxLeaseQuery,
       "mgs360024fDHCPSnoopingTxLeaseUnassigned": mgs360024fDHCPSnoopingTxLeaseUnassigned,
       "mgs360024fDHCPSnoopingTxLeaseUnknown": mgs360024fDHCPSnoopingTxLeaseUnknown,
       "mgs360024fDHCPSnoopingTxLeaseActive": mgs360024fDHCPSnoopingTxLeaseActive,
       "mgs360024fDHCPRelay": mgs360024fDHCPRelay,
       "mgs360024fDHCPRelayConfiguration": mgs360024fDHCPRelayConfiguration,
       "mgs360024fDHCPRelayMode": mgs360024fDHCPRelayMode,
       "mgs360024fDHCPRelayServer": mgs360024fDHCPRelayServer,
       "mgs360024fDHCPRelayInformationMode": mgs360024fDHCPRelayInformationMode,
       "mgs360024fDHCPRelayInformationPolicy": mgs360024fDHCPRelayInformationPolicy,
       "mgs360024fDHCPRelayStatistics": mgs360024fDHCPRelayStatistics,
       "mgs360024fDHCPRelayServerStatistics": mgs360024fDHCPRelayServerStatistics,
       "mgs360024fServerStatTransmitToServer": mgs360024fServerStatTransmitToServer,
       "mgs360024fServerStatTransmitError": mgs360024fServerStatTransmitError,
       "mgs360024fServerStatReceiveFromServer": mgs360024fServerStatReceiveFromServer,
       "mgs360024fServerStatReceiveMissingAgentOption": mgs360024fServerStatReceiveMissingAgentOption,
       "mgs360024fServerStatReceiveMissingCircuitID": mgs360024fServerStatReceiveMissingCircuitID,
       "mgs360024fServerStatReceiveMissingRemoteID": mgs360024fServerStatReceiveMissingRemoteID,
       "mgs360024fServerStatReceiveBadCircuitID": mgs360024fServerStatReceiveBadCircuitID,
       "mgs360024fServerStatReceiveBadRemoteID": mgs360024fServerStatReceiveBadRemoteID,
       "mgs360024fDHCPRelayClientStatistics": mgs360024fDHCPRelayClientStatistics,
       "mgs360024fClientStatTransmitToClient": mgs360024fClientStatTransmitToClient,
       "mgs360024fClientStatTransmitError": mgs360024fClientStatTransmitError,
       "mgs360024fClientStatReceivefromClient": mgs360024fClientStatReceivefromClient,
       "mgs360024fClientStatReceiveAgentOption": mgs360024fClientStatReceiveAgentOption,
       "mgs360024fClientStatReplaceAgentOption": mgs360024fClientStatReplaceAgentOption,
       "mgs360024fClientStatKeepAgentOption": mgs360024fClientStatKeepAgentOption,
       "mgs360024fClientStatDropAgentOption": mgs360024fClientStatDropAgentOption,
       "mgs360024fPortSecurity": mgs360024fPortSecurity,
       "mgs360024fPortSecLimitCtrl": mgs360024fPortSecLimitCtrl,
       "mgs360024fPortSecLimitCtrlSystemConf": mgs360024fPortSecLimitCtrlSystemConf,
       "mgs360024fPortSecurityMode": mgs360024fPortSecurityMode,
       "mgs360024fPortSecurityAging": mgs360024fPortSecurityAging,
       "mgs360024fPortSecurityAgingPeriod": mgs360024fPortSecurityAgingPeriod,
       "mgs360024fPortSecLimitCtrlTable": mgs360024fPortSecLimitCtrlTable,
       "mgs360024fPortSecLimitCtrlEntry": mgs360024fPortSecLimitCtrlEntry,
       "mgs360024fPortSecLimitCtrlPort": mgs360024fPortSecLimitCtrlPort,
       "mgs360024fPortSecLimitCtrlPortMode": mgs360024fPortSecLimitCtrlPortMode,
       "mgs360024fPortSecLimitCtrlPortLimit": mgs360024fPortSecLimitCtrlPortLimit,
       "mgs360024fPortSecLimitCtrlPortAction": mgs360024fPortSecLimitCtrlPortAction,
       "mgs360024fPortSecLimitCtrlPortState": mgs360024fPortSecLimitCtrlPortState,
       "mgs360024fPortSecLimitCtrlPortReOpen": mgs360024fPortSecLimitCtrlPortReOpen,
       "mgs360024fPortSecSwitchStatusTable": mgs360024fPortSecSwitchStatusTable,
       "mgs360024fPortSecSwitchStatusEntry": mgs360024fPortSecSwitchStatusEntry,
       "mgs360024fPortSecSwitchStatusPort": mgs360024fPortSecSwitchStatusPort,
       "mgs360024fPortSecSwitchStatusUsers": mgs360024fPortSecSwitchStatusUsers,
       "mgs360024fPortSecSwitchStatusState": mgs360024fPortSecSwitchStatusState,
       "mgs360024fPortSecSwitchStatusMACCountCurrent": mgs360024fPortSecSwitchStatusMACCountCurrent,
       "mgs360024fPortSecSwitchStatusMACCountLimit": mgs360024fPortSecSwitchStatusMACCountLimit,
       "mgs360024fPortSecPortStatus": mgs360024fPortSecPortStatus,
       "mgs360024fPortSecPortStatusPort": mgs360024fPortSecPortStatusPort,
       "mgs360024fPortSecPortStatusTable": mgs360024fPortSecPortStatusTable,
       "mgs360024fPortSecPortStatusEntry": mgs360024fPortSecPortStatusEntry,
       "mgs360024fPortSecPortStatusIndex": mgs360024fPortSecPortStatusIndex,
       "mgs360024fPortSecPortStatusMACAddress": mgs360024fPortSecPortStatusMACAddress,
       "mgs360024fPortSecPortStatusVLANId": mgs360024fPortSecPortStatusVLANId,
       "mgs360024fPortSecPortStatusState": mgs360024fPortSecPortStatusState,
       "mgs360024fPortSecPortStatusTimeOfAddition": mgs360024fPortSecPortStatusTimeOfAddition,
       "mgs360024fPortSecPortStatusAgeAndHold": mgs360024fPortSecPortStatusAgeAndHold,
       "mgs360024fAccessManagement": mgs360024fAccessManagement,
       "mgs360024fAccessMgtConf": mgs360024fAccessMgtConf,
       "mgs360024fAccessMgtConfMode": mgs360024fAccessMgtConfMode,
       "mgs360024fAccessMgtConfCreate": mgs360024fAccessMgtConfCreate,
       "mgs360024fAccessMgtConfTable": mgs360024fAccessMgtConfTable,
       "mgs360024fAccessMgtConfEntry": mgs360024fAccessMgtConfEntry,
       "mgs360024fAccessMgtIndex": mgs360024fAccessMgtIndex,
       "mgs360024fAccessMgtAddresstype": mgs360024fAccessMgtAddresstype,
       "mgs360024fAccessMgtStartIpAddress": mgs360024fAccessMgtStartIpAddress,
       "mgs360024fAccessMgtEndIpAddress": mgs360024fAccessMgtEndIpAddress,
       "mgs360024fAccessMgtHttpHttps": mgs360024fAccessMgtHttpHttps,
       "mgs360024fAccessMgtSNMP": mgs360024fAccessMgtSNMP,
       "mgs360024fAccessMgtTelnetSSH": mgs360024fAccessMgtTelnetSSH,
       "mgs360024fAccessMgtRowStatus": mgs360024fAccessMgtRowStatus,
       "mgs360024fAccessMgtStatistics": mgs360024fAccessMgtStatistics,
       "mgs360024fHttpReceivedPkts": mgs360024fHttpReceivedPkts,
       "mgs360024fHttpAllowedPkts": mgs360024fHttpAllowedPkts,
       "mgs360024fHttpDiscardedPkts": mgs360024fHttpDiscardedPkts,
       "mgs360024fHttpsReceivedPkts": mgs360024fHttpsReceivedPkts,
       "mgs360024fHttpsAllowedPkts": mgs360024fHttpsAllowedPkts,
       "mgs360024fHttpsDiscardedPkts": mgs360024fHttpsDiscardedPkts,
       "mgs360024fSnmpReceivedPkts": mgs360024fSnmpReceivedPkts,
       "mgs360024fSnmpAllowedPkts": mgs360024fSnmpAllowedPkts,
       "mgs360024fSnmpDiscardedPkts": mgs360024fSnmpDiscardedPkts,
       "mgs360024fTelnetReceivedPkts": mgs360024fTelnetReceivedPkts,
       "mgs360024fTelnetAllowedPkts": mgs360024fTelnetAllowedPkts,
       "mgs360024fTelnetDiscardedPkts": mgs360024fTelnetDiscardedPkts,
       "mgs360024fSSHReceivedPkts": mgs360024fSSHReceivedPkts,
       "mgs360024fSSHAllowedPkts": mgs360024fSSHAllowedPkts,
       "mgs360024fSSHDiscardedPkts": mgs360024fSSHDiscardedPkts,
       "mgs360024fAccessMgtStatisticsClearAll": mgs360024fAccessMgtStatisticsClearAll,
       "mgs360024fSSH": mgs360024fSSH,
       "mgs360024fSSHMode": mgs360024fSSHMode,
       "mgs360024fHTTPS": mgs360024fHTTPS,
       "mgs360024fHTTPSMode": mgs360024fHTTPSMode,
       "mgs360024fHTTPSAutoRedirect": mgs360024fHTTPSAutoRedirect,
       "mgs360024fAuthMethod": mgs360024fAuthMethod,
       "mgs360024fConsoleAuthMethod": mgs360024fConsoleAuthMethod,
       "mgs360024fConsoleFallback": mgs360024fConsoleFallback,
       "mgs360024fTelnetAuthMethod": mgs360024fTelnetAuthMethod,
       "mgs360024fTelnetFallback": mgs360024fTelnetFallback,
       "mgs360024fSshAuthMethod": mgs360024fSshAuthMethod,
       "mgs360024fSshFallback": mgs360024fSshFallback,
       "mgs360024fWebAuthMethod": mgs360024fWebAuthMethod,
       "mgs360024fWebFallback": mgs360024fWebFallback,
       "mgs360024fMaintenance": mgs360024fMaintenance,
       "mgs360024fRestartDevice": mgs360024fRestartDevice,
       "mgs360024fFirmware": mgs360024fFirmware,
       "mgs360024fFirmwareIpAddress": mgs360024fFirmwareIpAddress,
       "mgs360024fFirmwareFileName": mgs360024fFirmwareFileName,
       "mgs360024fDoFirmwareUpgrade": mgs360024fDoFirmwareUpgrade,
       "mgs360024fSaveOrRestore": mgs360024fSaveOrRestore,
       "mgs360024fFactoryDefaults": mgs360024fFactoryDefaults,
       "mgs360024fSaveStart": mgs360024fSaveStart,
       "mgs360024fSaveUser": mgs360024fSaveUser,
       "mgs360024fRestoreUser": mgs360024fRestoreUser,
       "mgs360024fExportOrImport": mgs360024fExportOrImport,
       "mgs360024fExportIpAddress": mgs360024fExportIpAddress,
       "mgs360024fExportConfigName": mgs360024fExportConfigName,
       "mgs360024fDoExportConfig": mgs360024fDoExportConfig,
       "mgs360024fImportIpAddress": mgs360024fImportIpAddress,
       "mgs360024fImportConfigName": mgs360024fImportConfigName,
       "mgs360024fDoImportConfig": mgs360024fDoImportConfig,
       "mgs360024fDiagnostics": mgs360024fDiagnostics,
       "mgs360024fPingIpAddress": mgs360024fPingIpAddress,
       "mgs360024fPingSize": mgs360024fPingSize,
       "mgs360024fDoPingConfig": mgs360024fDoPingConfig,
       "mgs360024fPingResult": mgs360024fPingResult,
       "mgs360024fPing6IpAddress": mgs360024fPing6IpAddress,
       "mgs360024fPing6Size": mgs360024fPing6Size,
       "mgs360024fDoPing6Config": mgs360024fDoPing6Config,
       "mgs360024fPing6Result": mgs360024fPing6Result,
       "mgs360024fVeriPHY": mgs360024fVeriPHY,
       "mgs360024fVeriPHYTest": mgs360024fVeriPHYTest,
       "mgs360024fVeriPHYTable": mgs360024fVeriPHYTable,
       "mgs360024fVeriPHYEntry": mgs360024fVeriPHYEntry,
       "mgs360024fVeriPHYPort": mgs360024fVeriPHYPort,
       "mgs360024fVeriPHYPairA": mgs360024fVeriPHYPairA,
       "mgs360024fVeriPHYLengthA": mgs360024fVeriPHYLengthA,
       "mgs360024fVeriPHYPairB": mgs360024fVeriPHYPairB,
       "mgs360024fVeriPHYLengthB": mgs360024fVeriPHYLengthB,
       "mgs360024fVeriPHYPairC": mgs360024fVeriPHYPairC,
       "mgs360024fVeriPHYLengthC": mgs360024fVeriPHYLengthC,
       "mgs360024fVeriPHYPairD": mgs360024fVeriPHYPairD,
       "mgs360024fVeriPHYLengthD": mgs360024fVeriPHYLengthD,
       "mgs360024fTrap": mgs360024fTrap,
       "mgs360024fTrapEvent": mgs360024fTrapEvent,
       "mgs360024fEmergency": mgs360024fEmergency,
       "mgs360024fAlert": mgs360024fAlert,
       "mgs360024fCritical": mgs360024fCritical,
       "mgs360024fError": mgs360024fError,
       "mgs360024fWarning": mgs360024fWarning,
       "mgs360024fNotice": mgs360024fNotice,
       "mgs360024fInformational": mgs360024fInformational,
       "mgs360024fDebug": mgs360024fDebug,
       "mgs360024fTrapVariable": mgs360024fTrapVariable,
       "mgs360024fInformation": mgs360024fInformation}
)
