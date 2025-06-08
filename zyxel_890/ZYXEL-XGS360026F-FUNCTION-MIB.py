# SNMP MIB module (ZYXEL-XGS360026F-FUNCTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-XGS360026F-FUNCTION-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:33:26 2025
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
_Xgs360026fProductId_ObjectIdentity = ObjectIdentity
xgs360026fProductId = _Xgs360026fProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77)
)
_Xgs360026fSystem_ObjectIdentity = ObjectIdentity
xgs360026fSystem = _Xgs360026fSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1)
)
_Xgs360026fSystemInformation_ObjectIdentity = ObjectIdentity
xgs360026fSystemInformation = _Xgs360026fSystemInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1)
)
_Xgs360026fModelName_Type = DisplayString
_Xgs360026fModelName_Object = MibScalar
xgs360026fModelName = _Xgs360026fModelName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 1),
    _Xgs360026fModelName_Type()
)
xgs360026fModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fModelName.setStatus("current")
_Xgs360026fBIOSVersion_Type = DisplayString
_Xgs360026fBIOSVersion_Object = MibScalar
xgs360026fBIOSVersion = _Xgs360026fBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 2),
    _Xgs360026fBIOSVersion_Type()
)
xgs360026fBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fBIOSVersion.setStatus("current")
_Xgs360026fFirmwareVersion_Type = DisplayString
_Xgs360026fFirmwareVersion_Object = MibScalar
xgs360026fFirmwareVersion = _Xgs360026fFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 3),
    _Xgs360026fFirmwareVersion_Type()
)
xgs360026fFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fFirmwareVersion.setStatus("current")
_Xgs360026fHardwareMechanicalVersion_Type = DisplayString
_Xgs360026fHardwareMechanicalVersion_Object = MibScalar
xgs360026fHardwareMechanicalVersion = _Xgs360026fHardwareMechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 4),
    _Xgs360026fHardwareMechanicalVersion_Type()
)
xgs360026fHardwareMechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fHardwareMechanicalVersion.setStatus("current")
_Xgs360026fSeriesNumber_Type = DisplayString
_Xgs360026fSeriesNumber_Object = MibScalar
xgs360026fSeriesNumber = _Xgs360026fSeriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 5),
    _Xgs360026fSeriesNumber_Type()
)
xgs360026fSeriesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSeriesNumber.setStatus("current")
_Xgs360026fHostMACAddress_Type = MacAddress
_Xgs360026fHostMACAddress_Object = MibScalar
xgs360026fHostMACAddress = _Xgs360026fHostMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 6),
    _Xgs360026fHostMACAddress_Type()
)
xgs360026fHostMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fHostMACAddress.setStatus("current")
_Xgs360026fConsoleBaudrate_Type = DisplayString
_Xgs360026fConsoleBaudrate_Object = MibScalar
xgs360026fConsoleBaudrate = _Xgs360026fConsoleBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 7),
    _Xgs360026fConsoleBaudrate_Type()
)
xgs360026fConsoleBaudrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fConsoleBaudrate.setStatus("current")
_Xgs360026fRAMSize_Type = DisplayString
_Xgs360026fRAMSize_Object = MibScalar
xgs360026fRAMSize = _Xgs360026fRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 8),
    _Xgs360026fRAMSize_Type()
)
xgs360026fRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fRAMSize.setStatus("current")
_Xgs360026fFlashSize_Type = DisplayString
_Xgs360026fFlashSize_Object = MibScalar
xgs360026fFlashSize = _Xgs360026fFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 9),
    _Xgs360026fFlashSize_Type()
)
xgs360026fFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fFlashSize.setStatus("current")
_Xgs360026fBridgeFBDSize_Type = DisplayString
_Xgs360026fBridgeFBDSize_Object = MibScalar
xgs360026fBridgeFBDSize = _Xgs360026fBridgeFBDSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 10),
    _Xgs360026fBridgeFBDSize_Type()
)
xgs360026fBridgeFBDSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fBridgeFBDSize.setStatus("current")
_Xgs360026fTransmitQueue_Type = DisplayString
_Xgs360026fTransmitQueue_Object = MibScalar
xgs360026fTransmitQueue = _Xgs360026fTransmitQueue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 11),
    _Xgs360026fTransmitQueue_Type()
)
xgs360026fTransmitQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fTransmitQueue.setStatus("current")
_Xgs360026fMaximumFrameSize_Type = DisplayString
_Xgs360026fMaximumFrameSize_Object = MibScalar
xgs360026fMaximumFrameSize = _Xgs360026fMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 12),
    _Xgs360026fMaximumFrameSize_Type()
)
xgs360026fMaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMaximumFrameSize.setStatus("current")
_Xgs360026fCPULoad_Type = DisplayString
_Xgs360026fCPULoad_Object = MibScalar
xgs360026fCPULoad = _Xgs360026fCPULoad_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 13),
    _Xgs360026fCPULoad_Type()
)
xgs360026fCPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fCPULoad.setStatus("current")
_Xgs360026fFanSpeed_Type = DisplayString
_Xgs360026fFanSpeed_Object = MibScalar
xgs360026fFanSpeed = _Xgs360026fFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 14),
    _Xgs360026fFanSpeed_Type()
)
xgs360026fFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fFanSpeed.setStatus("current")
_Xgs360026fPowers_Type = DisplayString
_Xgs360026fPowers_Object = MibScalar
xgs360026fPowers = _Xgs360026fPowers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 15),
    _Xgs360026fPowers_Type()
)
xgs360026fPowers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPowers.setStatus("current")
_Xgs360026fTemperature1_Type = DisplayString
_Xgs360026fTemperature1_Object = MibScalar
xgs360026fTemperature1 = _Xgs360026fTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 16),
    _Xgs360026fTemperature1_Type()
)
xgs360026fTemperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fTemperature1.setStatus("current")
_Xgs360026fTemperature2_Type = DisplayString
_Xgs360026fTemperature2_Object = MibScalar
xgs360026fTemperature2 = _Xgs360026fTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 17),
    _Xgs360026fTemperature2_Type()
)
xgs360026fTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fTemperature2.setStatus("current")
_Xgs360026fTemperature3_Type = DisplayString
_Xgs360026fTemperature3_Object = MibScalar
xgs360026fTemperature3 = _Xgs360026fTemperature3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 18),
    _Xgs360026fTemperature3_Type()
)
xgs360026fTemperature3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fTemperature3.setStatus("current")
_Xgs360026fTemperature4_Type = DisplayString
_Xgs360026fTemperature4_Object = MibScalar
xgs360026fTemperature4 = _Xgs360026fTemperature4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 1, 19),
    _Xgs360026fTemperature4_Type()
)
xgs360026fTemperature4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fTemperature4.setStatus("current")
_Xgs360026fSystemTime_ObjectIdentity = ObjectIdentity
xgs360026fSystemTime = _Xgs360026fSystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2)
)
_Xgs360026fSystemTimeManual_ObjectIdentity = ObjectIdentity
xgs360026fSystemTimeManual = _Xgs360026fSystemTimeManual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 1)
)


class _Xgs360026fSystemTimeManualClockSource_Type(Integer32):
    """Custom type xgs360026fSystemTimeManualClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fSystemTimeManualClockSource_Type.__name__ = "Integer32"
_Xgs360026fSystemTimeManualClockSource_Object = MibScalar
xgs360026fSystemTimeManualClockSource = _Xgs360026fSystemTimeManualClockSource_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 1, 1),
    _Xgs360026fSystemTimeManualClockSource_Type()
)
xgs360026fSystemTimeManualClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeManualClockSource.setStatus("current")
_Xgs360026fSystemTimeManualLocaltime_Type = DisplayString
_Xgs360026fSystemTimeManualLocaltime_Object = MibScalar
xgs360026fSystemTimeManualLocaltime = _Xgs360026fSystemTimeManualLocaltime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 1, 2),
    _Xgs360026fSystemTimeManualLocaltime_Type()
)
xgs360026fSystemTimeManualLocaltime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeManualLocaltime.setStatus("current")


class _Xgs360026fSystemTimeManualTimeZoneOffset_Type(Integer32):
    """Custom type xgs360026fSystemTimeManualTimeZoneOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 780),
    )


_Xgs360026fSystemTimeManualTimeZoneOffset_Type.__name__ = "Integer32"
_Xgs360026fSystemTimeManualTimeZoneOffset_Object = MibScalar
xgs360026fSystemTimeManualTimeZoneOffset = _Xgs360026fSystemTimeManualTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 1, 3),
    _Xgs360026fSystemTimeManualTimeZoneOffset_Type()
)
xgs360026fSystemTimeManualTimeZoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeManualTimeZoneOffset.setStatus("current")


class _Xgs360026fSystemTimeManualDaylightSavings_Type(Integer32):
    """Custom type xgs360026fSystemTimeManualDaylightSavings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fSystemTimeManualDaylightSavings_Type.__name__ = "Integer32"
_Xgs360026fSystemTimeManualDaylightSavings_Object = MibScalar
xgs360026fSystemTimeManualDaylightSavings = _Xgs360026fSystemTimeManualDaylightSavings_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 1, 4),
    _Xgs360026fSystemTimeManualDaylightSavings_Type()
)
xgs360026fSystemTimeManualDaylightSavings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeManualDaylightSavings.setStatus("current")


class _Xgs360026fSystemTimeManualTimeSetOffset_Type(Integer32):
    """Custom type xgs360026fSystemTimeManualTimeSetOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Xgs360026fSystemTimeManualTimeSetOffset_Type.__name__ = "Integer32"
_Xgs360026fSystemTimeManualTimeSetOffset_Object = MibScalar
xgs360026fSystemTimeManualTimeSetOffset = _Xgs360026fSystemTimeManualTimeSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 1, 5),
    _Xgs360026fSystemTimeManualTimeSetOffset_Type()
)
xgs360026fSystemTimeManualTimeSetOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeManualTimeSetOffset.setStatus("current")


class _Xgs360026fSystemTimeManualDaylightSavingsType_Type(Integer32):
    """Custom type xgs360026fSystemTimeManualDaylightSavingsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fSystemTimeManualDaylightSavingsType_Type.__name__ = "Integer32"
_Xgs360026fSystemTimeManualDaylightSavingsType_Object = MibScalar
xgs360026fSystemTimeManualDaylightSavingsType = _Xgs360026fSystemTimeManualDaylightSavingsType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 1, 6),
    _Xgs360026fSystemTimeManualDaylightSavingsType_Type()
)
xgs360026fSystemTimeManualDaylightSavingsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeManualDaylightSavingsType.setStatus("current")
_Xgs360026fSystemTimeManualDaylightSavingsBydatesFrom_Type = DisplayString
_Xgs360026fSystemTimeManualDaylightSavingsBydatesFrom_Object = MibScalar
xgs360026fSystemTimeManualDaylightSavingsBydatesFrom = _Xgs360026fSystemTimeManualDaylightSavingsBydatesFrom_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 1, 7),
    _Xgs360026fSystemTimeManualDaylightSavingsBydatesFrom_Type()
)
xgs360026fSystemTimeManualDaylightSavingsBydatesFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeManualDaylightSavingsBydatesFrom.setStatus("current")
_Xgs360026fSystemTimeManualDaylightSavingsBydatesTo_Type = DisplayString
_Xgs360026fSystemTimeManualDaylightSavingsBydatesTo_Object = MibScalar
xgs360026fSystemTimeManualDaylightSavingsBydatesTo = _Xgs360026fSystemTimeManualDaylightSavingsBydatesTo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 1, 8),
    _Xgs360026fSystemTimeManualDaylightSavingsBydatesTo_Type()
)
xgs360026fSystemTimeManualDaylightSavingsBydatesTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeManualDaylightSavingsBydatesTo.setStatus("current")


class _Xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom_Type(Integer32):
    """Custom type xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom_Type.__name__ = "Integer32"
_Xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom_Object = MibScalar
xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom = _Xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 1, 9),
    _Xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom_Type()
)
xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom.setStatus("current")


class _Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom_Type(Integer32):
    """Custom type xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom_Type.__name__ = "Integer32"
_Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom_Object = MibScalar
xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom = _Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 1, 10),
    _Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom_Type()
)
xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom.setStatus("current")


class _Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom_Type(Integer32):
    """Custom type xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom_Type.__name__ = "Integer32"
_Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom_Object = MibScalar
xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom = _Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 1, 11),
    _Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom_Type()
)
xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom.setStatus("current")
_Xgs360026fSystemTimeManualDaylightSavingsRecurringTimeFrom_Type = DisplayString
_Xgs360026fSystemTimeManualDaylightSavingsRecurringTimeFrom_Object = MibScalar
xgs360026fSystemTimeManualDaylightSavingsRecurringTimeFrom = _Xgs360026fSystemTimeManualDaylightSavingsRecurringTimeFrom_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 1, 12),
    _Xgs360026fSystemTimeManualDaylightSavingsRecurringTimeFrom_Type()
)
xgs360026fSystemTimeManualDaylightSavingsRecurringTimeFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeManualDaylightSavingsRecurringTimeFrom.setStatus("current")


class _Xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo_Type(Integer32):
    """Custom type xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo_Type.__name__ = "Integer32"
_Xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo_Object = MibScalar
xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo = _Xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 1, 13),
    _Xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo_Type()
)
xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo.setStatus("current")


class _Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo_Type(Integer32):
    """Custom type xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo_Type.__name__ = "Integer32"
_Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo_Object = MibScalar
xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo = _Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 1, 14),
    _Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo_Type()
)
xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo.setStatus("current")


class _Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo_Type(Integer32):
    """Custom type xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo_Type.__name__ = "Integer32"
_Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo_Object = MibScalar
xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo = _Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 1, 15),
    _Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo_Type()
)
xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo.setStatus("current")
_Xgs360026fSystemTimeManualDaylightSavingsRecurringTimeTo_Type = DisplayString
_Xgs360026fSystemTimeManualDaylightSavingsRecurringTimeTo_Object = MibScalar
xgs360026fSystemTimeManualDaylightSavingsRecurringTimeTo = _Xgs360026fSystemTimeManualDaylightSavingsRecurringTimeTo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 1, 16),
    _Xgs360026fSystemTimeManualDaylightSavingsRecurringTimeTo_Type()
)
xgs360026fSystemTimeManualDaylightSavingsRecurringTimeTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeManualDaylightSavingsRecurringTimeTo.setStatus("current")
_Xgs360026fSystemTimeNTP_ObjectIdentity = ObjectIdentity
xgs360026fSystemTimeNTP = _Xgs360026fSystemTimeNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 2)
)
_Xgs360026fSystemTimeNTPTable_Object = MibTable
xgs360026fSystemTimeNTPTable = _Xgs360026fSystemTimeNTPTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    xgs360026fSystemTimeNTPTable.setStatus("current")
_Xgs360026fSystemTimeNTPEntry_Object = MibTableRow
xgs360026fSystemTimeNTPEntry = _Xgs360026fSystemTimeNTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 2, 1, 1)
)
xgs360026fSystemTimeNTPEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fSystemTimeNTPIndex"),
)
if mibBuilder.loadTexts:
    xgs360026fSystemTimeNTPEntry.setStatus("current")


class _Xgs360026fSystemTimeNTPIndex_Type(Integer32):
    """Custom type xgs360026fSystemTimeNTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Xgs360026fSystemTimeNTPIndex_Type.__name__ = "Integer32"
_Xgs360026fSystemTimeNTPIndex_Object = MibTableColumn
xgs360026fSystemTimeNTPIndex = _Xgs360026fSystemTimeNTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 2, 1, 1, 1),
    _Xgs360026fSystemTimeNTPIndex_Type()
)
xgs360026fSystemTimeNTPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeNTPIndex.setStatus("current")


class _Xgs360026fSystemTimeNTPServerIPType_Type(Integer32):
    """Custom type xgs360026fSystemTimeNTPServerIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fSystemTimeNTPServerIPType_Type.__name__ = "Integer32"
_Xgs360026fSystemTimeNTPServerIPType_Object = MibTableColumn
xgs360026fSystemTimeNTPServerIPType = _Xgs360026fSystemTimeNTPServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 2, 1, 1, 2),
    _Xgs360026fSystemTimeNTPServerIPType_Type()
)
xgs360026fSystemTimeNTPServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeNTPServerIPType.setStatus("current")
_Xgs360026fSystemTimeNTPServer_Type = DisplayString
_Xgs360026fSystemTimeNTPServer_Object = MibTableColumn
xgs360026fSystemTimeNTPServer = _Xgs360026fSystemTimeNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 2, 1, 1, 3),
    _Xgs360026fSystemTimeNTPServer_Type()
)
xgs360026fSystemTimeNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeNTPServer.setStatus("current")


class _Xgs360026fSystemTimeNTPCurrentMode_Type(Integer32):
    """Custom type xgs360026fSystemTimeNTPCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Xgs360026fSystemTimeNTPCurrentMode_Type.__name__ = "Integer32"
_Xgs360026fSystemTimeNTPCurrentMode_Object = MibTableColumn
xgs360026fSystemTimeNTPCurrentMode = _Xgs360026fSystemTimeNTPCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 2, 2, 1, 1, 4),
    _Xgs360026fSystemTimeNTPCurrentMode_Type()
)
xgs360026fSystemTimeNTPCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemTimeNTPCurrentMode.setStatus("current")
_Xgs360026fSystemAccount_ObjectIdentity = ObjectIdentity
xgs360026fSystemAccount = _Xgs360026fSystemAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3)
)
_Xgs360026fSystemAccountUsers_ObjectIdentity = ObjectIdentity
xgs360026fSystemAccountUsers = _Xgs360026fSystemAccountUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 1)
)


class _Xgs360026fSystemAccountUserCreate_Type(Integer32):
    """Custom type xgs360026fSystemAccountUserCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fSystemAccountUserCreate_Type.__name__ = "Integer32"
_Xgs360026fSystemAccountUserCreate_Object = MibScalar
xgs360026fSystemAccountUserCreate = _Xgs360026fSystemAccountUserCreate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 1, 1),
    _Xgs360026fSystemAccountUserCreate_Type()
)
xgs360026fSystemAccountUserCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemAccountUserCreate.setStatus("current")
_Xgs360026fSystemAccountUsersTable_Object = MibTable
xgs360026fSystemAccountUsersTable = _Xgs360026fSystemAccountUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    xgs360026fSystemAccountUsersTable.setStatus("current")
_Xgs360026fSystemAccountUsersEntry_Object = MibTableRow
xgs360026fSystemAccountUsersEntry = _Xgs360026fSystemAccountUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 1, 2, 1)
)
xgs360026fSystemAccountUsersEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fUserIndex"),
)
if mibBuilder.loadTexts:
    xgs360026fSystemAccountUsersEntry.setStatus("current")


class _Xgs360026fUserIndex_Type(Integer32):
    """Custom type xgs360026fUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Xgs360026fUserIndex_Type.__name__ = "Integer32"
_Xgs360026fUserIndex_Object = MibTableColumn
xgs360026fUserIndex = _Xgs360026fUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 1, 2, 1, 1),
    _Xgs360026fUserIndex_Type()
)
xgs360026fUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fUserIndex.setStatus("current")


class _Xgs360026fUserName_Type(DisplayString):
    """Custom type xgs360026fUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xgs360026fUserName_Type.__name__ = "DisplayString"
_Xgs360026fUserName_Object = MibTableColumn
xgs360026fUserName = _Xgs360026fUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 1, 2, 1, 2),
    _Xgs360026fUserName_Type()
)
xgs360026fUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fUserName.setStatus("current")


class _Xgs360026fPassword_Type(DisplayString):
    """Custom type xgs360026fPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xgs360026fPassword_Type.__name__ = "DisplayString"
_Xgs360026fPassword_Object = MibTableColumn
xgs360026fPassword = _Xgs360026fPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 1, 2, 1, 3),
    _Xgs360026fPassword_Type()
)
xgs360026fPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPassword.setStatus("current")


class _Xgs360026fUserPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fUserPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fUserPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fUserPrivilegeLevel_Object = MibTableColumn
xgs360026fUserPrivilegeLevel = _Xgs360026fUserPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 1, 2, 1, 4),
    _Xgs360026fUserPrivilegeLevel_Type()
)
xgs360026fUserPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fUserPrivilegeLevel.setStatus("current")


class _Xgs360026fAccountUserRowStatus_Type(Integer32):
    """Custom type xgs360026fAccountUserRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Xgs360026fAccountUserRowStatus_Type.__name__ = "Integer32"
_Xgs360026fAccountUserRowStatus_Object = MibTableColumn
xgs360026fAccountUserRowStatus = _Xgs360026fAccountUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 1, 2, 1, 5),
    _Xgs360026fAccountUserRowStatus_Type()
)
xgs360026fAccountUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fAccountUserRowStatus.setStatus("current")
_Xgs360026fSystemAccountPrivilegeLevel_ObjectIdentity = ObjectIdentity
xgs360026fSystemAccountPrivilegeLevel = _Xgs360026fSystemAccountPrivilegeLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2)
)


class _Xgs360026fAccountPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fAccountPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fAccountPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fAccountPrivilegeLevel_Object = MibScalar
xgs360026fAccountPrivilegeLevel = _Xgs360026fAccountPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 1),
    _Xgs360026fAccountPrivilegeLevel_Type()
)
xgs360026fAccountPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fAccountPrivilegeLevel.setStatus("current")


class _Xgs360026fAggregationPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fAggregationPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fAggregationPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fAggregationPrivilegeLevel_Object = MibScalar
xgs360026fAggregationPrivilegeLevel = _Xgs360026fAggregationPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 2),
    _Xgs360026fAggregationPrivilegeLevel_Type()
)
xgs360026fAggregationPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fAggregationPrivilegeLevel.setStatus("current")


class _Xgs360026fDiagnosticsPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fDiagnosticsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fDiagnosticsPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fDiagnosticsPrivilegeLevel_Object = MibScalar
xgs360026fDiagnosticsPrivilegeLevel = _Xgs360026fDiagnosticsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 3),
    _Xgs360026fDiagnosticsPrivilegeLevel_Type()
)
xgs360026fDiagnosticsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fDiagnosticsPrivilegeLevel.setStatus("current")


class _Xgs360026fEPSPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fEPSPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fEPSPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fEPSPrivilegeLevel_Object = MibScalar
xgs360026fEPSPrivilegeLevel = _Xgs360026fEPSPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 5),
    _Xgs360026fEPSPrivilegeLevel_Type()
)
xgs360026fEPSPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fEPSPrivilegeLevel.setStatus("current")


class _Xgs360026fERPSPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fERPSPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fERPSPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fERPSPrivilegeLevel_Object = MibScalar
xgs360026fERPSPrivilegeLevel = _Xgs360026fERPSPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 6),
    _Xgs360026fERPSPrivilegeLevel_Type()
)
xgs360026fERPSPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSPrivilegeLevel.setStatus("current")


class _Xgs360026fETHLinkOAMPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fETHLinkOAMPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fETHLinkOAMPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fETHLinkOAMPrivilegeLevel_Object = MibScalar
xgs360026fETHLinkOAMPrivilegeLevel = _Xgs360026fETHLinkOAMPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 7),
    _Xgs360026fETHLinkOAMPrivilegeLevel_Type()
)
xgs360026fETHLinkOAMPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fETHLinkOAMPrivilegeLevel.setStatus("current")


class _Xgs360026fEVCPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fEVCPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fEVCPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fEVCPrivilegeLevel_Object = MibScalar
xgs360026fEVCPrivilegeLevel = _Xgs360026fEVCPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 8),
    _Xgs360026fEVCPrivilegeLevel_Type()
)
xgs360026fEVCPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fEVCPrivilegeLevel.setStatus("current")


class _Xgs360026fGARPPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fGARPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fGARPPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fGARPPrivilegeLevel_Object = MibScalar
xgs360026fGARPPrivilegeLevel = _Xgs360026fGARPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 10),
    _Xgs360026fGARPPrivilegeLevel_Type()
)
xgs360026fGARPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fGARPPrivilegeLevel.setStatus("current")


class _Xgs360026fGVRPPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fGVRPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fGVRPPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fGVRPPrivilegeLevel_Object = MibScalar
xgs360026fGVRPPrivilegeLevel = _Xgs360026fGVRPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 11),
    _Xgs360026fGVRPPrivilegeLevel_Type()
)
xgs360026fGVRPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fGVRPPrivilegeLevel.setStatus("current")


class _Xgs360026fIPPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fIPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fIPPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fIPPrivilegeLevel_Object = MibScalar
xgs360026fIPPrivilegeLevel = _Xgs360026fIPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 12),
    _Xgs360026fIPPrivilegeLevel_Type()
)
xgs360026fIPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIPPrivilegeLevel.setStatus("current")


class _Xgs360026fIPMCSnoopingPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fIPMCSnoopingPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fIPMCSnoopingPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fIPMCSnoopingPrivilegeLevel_Object = MibScalar
xgs360026fIPMCSnoopingPrivilegeLevel = _Xgs360026fIPMCSnoopingPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 13),
    _Xgs360026fIPMCSnoopingPrivilegeLevel_Type()
)
xgs360026fIPMCSnoopingPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIPMCSnoopingPrivilegeLevel.setStatus("current")


class _Xgs360026fLACPPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fLACPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fLACPPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fLACPPrivilegeLevel_Object = MibScalar
xgs360026fLACPPrivilegeLevel = _Xgs360026fLACPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 14),
    _Xgs360026fLACPPrivilegeLevel_Type()
)
xgs360026fLACPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fLACPPrivilegeLevel.setStatus("current")


class _Xgs360026fLLDPPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fLLDPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fLLDPPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fLLDPPrivilegeLevel_Object = MibScalar
xgs360026fLLDPPrivilegeLevel = _Xgs360026fLLDPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 15),
    _Xgs360026fLLDPPrivilegeLevel_Type()
)
xgs360026fLLDPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fLLDPPrivilegeLevel.setStatus("current")


class _Xgs360026fLLDPMEDPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fLLDPMEDPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fLLDPMEDPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fLLDPMEDPrivilegeLevel_Object = MibScalar
xgs360026fLLDPMEDPrivilegeLevel = _Xgs360026fLLDPMEDPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 16),
    _Xgs360026fLLDPMEDPrivilegeLevel_Type()
)
xgs360026fLLDPMEDPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fLLDPMEDPrivilegeLevel.setStatus("current")


class _Xgs360026fLoopProtectPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fLoopProtectPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fLoopProtectPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fLoopProtectPrivilegeLevel_Object = MibScalar
xgs360026fLoopProtectPrivilegeLevel = _Xgs360026fLoopProtectPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 17),
    _Xgs360026fLoopProtectPrivilegeLevel_Type()
)
xgs360026fLoopProtectPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fLoopProtectPrivilegeLevel.setStatus("current")


class _Xgs360026fMACTablePrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fMACTablePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fMACTablePrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fMACTablePrivilegeLevel_Object = MibScalar
xgs360026fMACTablePrivilegeLevel = _Xgs360026fMACTablePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 18),
    _Xgs360026fMACTablePrivilegeLevel_Type()
)
xgs360026fMACTablePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMACTablePrivilegeLevel.setStatus("current")


class _Xgs360026fMEPPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fMEPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fMEPPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fMEPPrivilegeLevel_Object = MibScalar
xgs360026fMEPPrivilegeLevel = _Xgs360026fMEPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 20),
    _Xgs360026fMEPPrivilegeLevel_Type()
)
xgs360026fMEPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMEPPrivilegeLevel.setStatus("current")


class _Xgs360026fMRSTPPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fMRSTPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fMRSTPPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fMRSTPPrivilegeLevel_Object = MibScalar
xgs360026fMRSTPPrivilegeLevel = _Xgs360026fMRSTPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 21),
    _Xgs360026fMRSTPPrivilegeLevel_Type()
)
xgs360026fMRSTPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMRSTPPrivilegeLevel.setStatus("current")


class _Xgs360026fMVRPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fMVRPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fMVRPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fMVRPrivilegeLevel_Object = MibScalar
xgs360026fMVRPrivilegeLevel = _Xgs360026fMVRPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 22),
    _Xgs360026fMVRPrivilegeLevel_Type()
)
xgs360026fMVRPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMVRPrivilegeLevel.setStatus("current")


class _Xgs360026fMaintenancePrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fMaintenancePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fMaintenancePrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fMaintenancePrivilegeLevel_Object = MibScalar
xgs360026fMaintenancePrivilegeLevel = _Xgs360026fMaintenancePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 24),
    _Xgs360026fMaintenancePrivilegeLevel_Type()
)
xgs360026fMaintenancePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMaintenancePrivilegeLevel.setStatus("current")


class _Xgs360026fMirroringPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fMirroringPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fMirroringPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fMirroringPrivilegeLevel_Object = MibScalar
xgs360026fMirroringPrivilegeLevel = _Xgs360026fMirroringPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 25),
    _Xgs360026fMirroringPrivilegeLevel_Type()
)
xgs360026fMirroringPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMirroringPrivilegeLevel.setStatus("current")


class _Xgs360026fPTPPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fPTPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fPTPPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fPTPPrivilegeLevel_Object = MibScalar
xgs360026fPTPPrivilegeLevel = _Xgs360026fPTPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 26),
    _Xgs360026fPTPPrivilegeLevel_Type()
)
xgs360026fPTPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPTPPrivilegeLevel.setStatus("current")


class _Xgs360026fPortsPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fPortsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fPortsPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fPortsPrivilegeLevel_Object = MibScalar
xgs360026fPortsPrivilegeLevel = _Xgs360026fPortsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 27),
    _Xgs360026fPortsPrivilegeLevel_Type()
)
xgs360026fPortsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPortsPrivilegeLevel.setStatus("current")


class _Xgs360026fPrivateVLANsPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fPrivateVLANsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fPrivateVLANsPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fPrivateVLANsPrivilegeLevel_Object = MibScalar
xgs360026fPrivateVLANsPrivilegeLevel = _Xgs360026fPrivateVLANsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 28),
    _Xgs360026fPrivateVLANsPrivilegeLevel_Type()
)
xgs360026fPrivateVLANsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPrivateVLANsPrivilegeLevel.setStatus("current")


class _Xgs360026fQoSPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fQoSPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fQoSPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fQoSPrivilegeLevel_Object = MibScalar
xgs360026fQoSPrivilegeLevel = _Xgs360026fQoSPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 29),
    _Xgs360026fQoSPrivilegeLevel_Type()
)
xgs360026fQoSPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fQoSPrivilegeLevel.setStatus("current")


class _Xgs360026fSMTPPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fSMTPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fSMTPPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fSMTPPrivilegeLevel_Object = MibScalar
xgs360026fSMTPPrivilegeLevel = _Xgs360026fSMTPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 31),
    _Xgs360026fSMTPPrivilegeLevel_Type()
)
xgs360026fSMTPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSMTPPrivilegeLevel.setStatus("current")


class _Xgs360026fSNMPPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fSNMPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fSNMPPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fSNMPPrivilegeLevel_Object = MibScalar
xgs360026fSNMPPrivilegeLevel = _Xgs360026fSNMPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 32),
    _Xgs360026fSNMPPrivilegeLevel_Type()
)
xgs360026fSNMPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSNMPPrivilegeLevel.setStatus("current")


class _Xgs360026fSecurityPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fSecurityPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fSecurityPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fSecurityPrivilegeLevel_Object = MibScalar
xgs360026fSecurityPrivilegeLevel = _Xgs360026fSecurityPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 33),
    _Xgs360026fSecurityPrivilegeLevel_Type()
)
xgs360026fSecurityPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSecurityPrivilegeLevel.setStatus("current")


class _Xgs360026fSpanningTreePrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fSpanningTreePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fSpanningTreePrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fSpanningTreePrivilegeLevel_Object = MibScalar
xgs360026fSpanningTreePrivilegeLevel = _Xgs360026fSpanningTreePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 35),
    _Xgs360026fSpanningTreePrivilegeLevel_Type()
)
xgs360026fSpanningTreePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSpanningTreePrivilegeLevel.setStatus("current")


class _Xgs360026fSystemPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fSystemPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fSystemPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fSystemPrivilegeLevel_Object = MibScalar
xgs360026fSystemPrivilegeLevel = _Xgs360026fSystemPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 36),
    _Xgs360026fSystemPrivilegeLevel_Type()
)
xgs360026fSystemPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSystemPrivilegeLevel.setStatus("current")


class _Xgs360026fTrapEventPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fTrapEventPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fTrapEventPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fTrapEventPrivilegeLevel_Object = MibScalar
xgs360026fTrapEventPrivilegeLevel = _Xgs360026fTrapEventPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 37),
    _Xgs360026fTrapEventPrivilegeLevel_Type()
)
xgs360026fTrapEventPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventPrivilegeLevel.setStatus("current")


class _Xgs360026fVCLPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fVCLPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fVCLPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fVCLPrivilegeLevel_Object = MibScalar
xgs360026fVCLPrivilegeLevel = _Xgs360026fVCLPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 39),
    _Xgs360026fVCLPrivilegeLevel_Type()
)
xgs360026fVCLPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fVCLPrivilegeLevel.setStatus("current")


class _Xgs360026fVLANTranslationPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fVLANTranslationPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fVLANTranslationPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fVLANTranslationPrivilegeLevel_Object = MibScalar
xgs360026fVLANTranslationPrivilegeLevel = _Xgs360026fVLANTranslationPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 40),
    _Xgs360026fVLANTranslationPrivilegeLevel_Type()
)
xgs360026fVLANTranslationPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fVLANTranslationPrivilegeLevel.setStatus("current")


class _Xgs360026fVLANsPrivilegeLevel_Type(Integer32):
    """Custom type xgs360026fVLANsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Xgs360026fVLANsPrivilegeLevel_Type.__name__ = "Integer32"
_Xgs360026fVLANsPrivilegeLevel_Object = MibScalar
xgs360026fVLANsPrivilegeLevel = _Xgs360026fVLANsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 3, 2, 41),
    _Xgs360026fVLANsPrivilegeLevel_Type()
)
xgs360026fVLANsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fVLANsPrivilegeLevel.setStatus("current")
_Xgs360026fIP_ObjectIdentity = ObjectIdentity
xgs360026fIP = _Xgs360026fIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4)
)
_Xgs360026fIPv4_ObjectIdentity = ObjectIdentity
xgs360026fIPv4 = _Xgs360026fIPv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 1)
)
_Xgs360026fIPv4Configured_ObjectIdentity = ObjectIdentity
xgs360026fIPv4Configured = _Xgs360026fIPv4Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 1, 1)
)


class _Xgs360026fIpv4DHCPClient_Type(Integer32):
    """Custom type xgs360026fIpv4DHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fIpv4DHCPClient_Type.__name__ = "Integer32"
_Xgs360026fIpv4DHCPClient_Object = MibScalar
xgs360026fIpv4DHCPClient = _Xgs360026fIpv4DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 1, 1, 1),
    _Xgs360026fIpv4DHCPClient_Type()
)
xgs360026fIpv4DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIpv4DHCPClient.setStatus("current")
_Xgs360026fIPv4Address_Type = IpAddress
_Xgs360026fIPv4Address_Object = MibScalar
xgs360026fIPv4Address = _Xgs360026fIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 1, 1, 2),
    _Xgs360026fIPv4Address_Type()
)
xgs360026fIPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIPv4Address.setStatus("current")
_Xgs360026fIPv4Mask_Type = IpAddress
_Xgs360026fIPv4Mask_Object = MibScalar
xgs360026fIPv4Mask = _Xgs360026fIPv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 1, 1, 3),
    _Xgs360026fIPv4Mask_Type()
)
xgs360026fIPv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIPv4Mask.setStatus("current")
_Xgs360026fIPv4Router_Type = IpAddress
_Xgs360026fIPv4Router_Object = MibScalar
xgs360026fIPv4Router = _Xgs360026fIPv4Router_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 1, 1, 4),
    _Xgs360026fIPv4Router_Type()
)
xgs360026fIPv4Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIPv4Router.setStatus("current")


class _Xgs360026fIPv4VLANId_Type(Integer32):
    """Custom type xgs360026fIPv4VLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Xgs360026fIPv4VLANId_Type.__name__ = "Integer32"
_Xgs360026fIPv4VLANId_Object = MibScalar
xgs360026fIPv4VLANId = _Xgs360026fIPv4VLANId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 1, 1, 5),
    _Xgs360026fIPv4VLANId_Type()
)
xgs360026fIPv4VLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIPv4VLANId.setStatus("current")
_Xgs360026fIPv4DNSServer_Type = IpAddress
_Xgs360026fIPv4DNSServer_Object = MibScalar
xgs360026fIPv4DNSServer = _Xgs360026fIPv4DNSServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 1, 1, 6),
    _Xgs360026fIPv4DNSServer_Type()
)
xgs360026fIPv4DNSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIPv4DNSServer.setStatus("current")


class _Xgs360026fIPv4DNSProxy_Type(Integer32):
    """Custom type xgs360026fIPv4DNSProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fIPv4DNSProxy_Type.__name__ = "Integer32"
_Xgs360026fIPv4DNSProxy_Object = MibScalar
xgs360026fIPv4DNSProxy = _Xgs360026fIPv4DNSProxy_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 1, 1, 7),
    _Xgs360026fIPv4DNSProxy_Type()
)
xgs360026fIPv4DNSProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIPv4DNSProxy.setStatus("current")
_Xgs360026fIPv4Current_ObjectIdentity = ObjectIdentity
xgs360026fIPv4Current = _Xgs360026fIPv4Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 1, 2)
)


class _Xgs360026fIpv4CurrentDHCPClient_Type(Integer32):
    """Custom type xgs360026fIpv4CurrentDHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fIpv4CurrentDHCPClient_Type.__name__ = "Integer32"
_Xgs360026fIpv4CurrentDHCPClient_Object = MibScalar
xgs360026fIpv4CurrentDHCPClient = _Xgs360026fIpv4CurrentDHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 1, 2, 1),
    _Xgs360026fIpv4CurrentDHCPClient_Type()
)
xgs360026fIpv4CurrentDHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIpv4CurrentDHCPClient.setStatus("current")
_Xgs360026fIPv4CurrentAddress_Type = IpAddress
_Xgs360026fIPv4CurrentAddress_Object = MibScalar
xgs360026fIPv4CurrentAddress = _Xgs360026fIPv4CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 1, 2, 2),
    _Xgs360026fIPv4CurrentAddress_Type()
)
xgs360026fIPv4CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fIPv4CurrentAddress.setStatus("current")
_Xgs360026fIPv4CurrentMask_Type = IpAddress
_Xgs360026fIPv4CurrentMask_Object = MibScalar
xgs360026fIPv4CurrentMask = _Xgs360026fIPv4CurrentMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 1, 2, 3),
    _Xgs360026fIPv4CurrentMask_Type()
)
xgs360026fIPv4CurrentMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fIPv4CurrentMask.setStatus("current")
_Xgs360026fIPv4CurrentRouter_Type = IpAddress
_Xgs360026fIPv4CurrentRouter_Object = MibScalar
xgs360026fIPv4CurrentRouter = _Xgs360026fIPv4CurrentRouter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 1, 2, 4),
    _Xgs360026fIPv4CurrentRouter_Type()
)
xgs360026fIPv4CurrentRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fIPv4CurrentRouter.setStatus("current")


class _Xgs360026fIPv4CurrentVLANId_Type(Integer32):
    """Custom type xgs360026fIPv4CurrentVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Xgs360026fIPv4CurrentVLANId_Type.__name__ = "Integer32"
_Xgs360026fIPv4CurrentVLANId_Object = MibScalar
xgs360026fIPv4CurrentVLANId = _Xgs360026fIPv4CurrentVLANId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 1, 2, 5),
    _Xgs360026fIPv4CurrentVLANId_Type()
)
xgs360026fIPv4CurrentVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fIPv4CurrentVLANId.setStatus("current")
_Xgs360026fIPv4CurrentDNSServer_Type = IpAddress
_Xgs360026fIPv4CurrentDNSServer_Object = MibScalar
xgs360026fIPv4CurrentDNSServer = _Xgs360026fIPv4CurrentDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 1, 2, 6),
    _Xgs360026fIPv4CurrentDNSServer_Type()
)
xgs360026fIPv4CurrentDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fIPv4CurrentDNSServer.setStatus("current")
_Xgs360026fIPv6_ObjectIdentity = ObjectIdentity
xgs360026fIPv6 = _Xgs360026fIPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 2)
)
_Xgs360026fIPv6Configured_ObjectIdentity = ObjectIdentity
xgs360026fIPv6Configured = _Xgs360026fIPv6Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 2, 1)
)


class _Xgs360026fIpv6AutoConfiguration_Type(Integer32):
    """Custom type xgs360026fIpv6AutoConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fIpv6AutoConfiguration_Type.__name__ = "Integer32"
_Xgs360026fIpv6AutoConfiguration_Object = MibScalar
xgs360026fIpv6AutoConfiguration = _Xgs360026fIpv6AutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 2, 1, 1),
    _Xgs360026fIpv6AutoConfiguration_Type()
)
xgs360026fIpv6AutoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIpv6AutoConfiguration.setStatus("current")


class _Xgs360026fIpv6Address_Type(DisplayString):
    """Custom type xgs360026fIpv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Xgs360026fIpv6Address_Type.__name__ = "DisplayString"
_Xgs360026fIpv6Address_Object = MibScalar
xgs360026fIpv6Address = _Xgs360026fIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 2, 1, 2),
    _Xgs360026fIpv6Address_Type()
)
xgs360026fIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIpv6Address.setStatus("current")


class _Xgs360026fIpv6Prefix_Type(Integer32):
    """Custom type xgs360026fIpv6Prefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Xgs360026fIpv6Prefix_Type.__name__ = "Integer32"
_Xgs360026fIpv6Prefix_Object = MibScalar
xgs360026fIpv6Prefix = _Xgs360026fIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 2, 1, 3),
    _Xgs360026fIpv6Prefix_Type()
)
xgs360026fIpv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIpv6Prefix.setStatus("current")


class _Xgs360026fIpv6Router_Type(DisplayString):
    """Custom type xgs360026fIpv6Router based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Xgs360026fIpv6Router_Type.__name__ = "DisplayString"
_Xgs360026fIpv6Router_Object = MibScalar
xgs360026fIpv6Router = _Xgs360026fIpv6Router_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 2, 1, 4),
    _Xgs360026fIpv6Router_Type()
)
xgs360026fIpv6Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIpv6Router.setStatus("current")
_Xgs360026fIPv6Current_ObjectIdentity = ObjectIdentity
xgs360026fIPv6Current = _Xgs360026fIPv6Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 2, 2)
)


class _Xgs360026fIpv6CurrentAutoConfiguration_Type(Integer32):
    """Custom type xgs360026fIpv6CurrentAutoConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fIpv6CurrentAutoConfiguration_Type.__name__ = "Integer32"
_Xgs360026fIpv6CurrentAutoConfiguration_Object = MibScalar
xgs360026fIpv6CurrentAutoConfiguration = _Xgs360026fIpv6CurrentAutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 2, 2, 1),
    _Xgs360026fIpv6CurrentAutoConfiguration_Type()
)
xgs360026fIpv6CurrentAutoConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fIpv6CurrentAutoConfiguration.setStatus("current")


class _Xgs360026fIpv6CurrentAddress_Type(DisplayString):
    """Custom type xgs360026fIpv6CurrentAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Xgs360026fIpv6CurrentAddress_Type.__name__ = "DisplayString"
_Xgs360026fIpv6CurrentAddress_Object = MibScalar
xgs360026fIpv6CurrentAddress = _Xgs360026fIpv6CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 2, 2, 2),
    _Xgs360026fIpv6CurrentAddress_Type()
)
xgs360026fIpv6CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fIpv6CurrentAddress.setStatus("current")


class _Xgs360026fIpv6CurrentLinkLocalAddress_Type(DisplayString):
    """Custom type xgs360026fIpv6CurrentLinkLocalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Xgs360026fIpv6CurrentLinkLocalAddress_Type.__name__ = "DisplayString"
_Xgs360026fIpv6CurrentLinkLocalAddress_Object = MibScalar
xgs360026fIpv6CurrentLinkLocalAddress = _Xgs360026fIpv6CurrentLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 2, 2, 3),
    _Xgs360026fIpv6CurrentLinkLocalAddress_Type()
)
xgs360026fIpv6CurrentLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fIpv6CurrentLinkLocalAddress.setStatus("current")


class _Xgs360026fIpv6CurrentPrefix_Type(Integer32):
    """Custom type xgs360026fIpv6CurrentPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Xgs360026fIpv6CurrentPrefix_Type.__name__ = "Integer32"
_Xgs360026fIpv6CurrentPrefix_Object = MibScalar
xgs360026fIpv6CurrentPrefix = _Xgs360026fIpv6CurrentPrefix_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 2, 2, 4),
    _Xgs360026fIpv6CurrentPrefix_Type()
)
xgs360026fIpv6CurrentPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fIpv6CurrentPrefix.setStatus("current")


class _Xgs360026fIpv6CurrentRouter_Type(DisplayString):
    """Custom type xgs360026fIpv6CurrentRouter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Xgs360026fIpv6CurrentRouter_Type.__name__ = "DisplayString"
_Xgs360026fIpv6CurrentRouter_Object = MibScalar
xgs360026fIpv6CurrentRouter = _Xgs360026fIpv6CurrentRouter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 4, 2, 2, 5),
    _Xgs360026fIpv6CurrentRouter_Type()
)
xgs360026fIpv6CurrentRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fIpv6CurrentRouter.setStatus("current")
_Xgs360026fSyslog_ObjectIdentity = ObjectIdentity
xgs360026fSyslog = _Xgs360026fSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 5)
)
_Xgs360026fSyslogConf_ObjectIdentity = ObjectIdentity
xgs360026fSyslogConf = _Xgs360026fSyslogConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 5, 1)
)


class _Xgs360026fServerMode_Type(Integer32):
    """Custom type xgs360026fServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fServerMode_Type.__name__ = "Integer32"
_Xgs360026fServerMode_Object = MibScalar
xgs360026fServerMode = _Xgs360026fServerMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 5, 1, 1),
    _Xgs360026fServerMode_Type()
)
xgs360026fServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fServerMode.setStatus("current")
_Xgs360026fServerAddress1_Type = IpAddress
_Xgs360026fServerAddress1_Object = MibScalar
xgs360026fServerAddress1 = _Xgs360026fServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 5, 1, 2),
    _Xgs360026fServerAddress1_Type()
)
xgs360026fServerAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fServerAddress1.setStatus("current")
_Xgs360026fServerAddress2_Type = IpAddress
_Xgs360026fServerAddress2_Object = MibScalar
xgs360026fServerAddress2 = _Xgs360026fServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 5, 1, 3),
    _Xgs360026fServerAddress2_Type()
)
xgs360026fServerAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fServerAddress2.setStatus("current")


class _Xgs360026fSyslogLevel_Type(Integer32):
    """Custom type xgs360026fSyslogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fSyslogLevel_Type.__name__ = "Integer32"
_Xgs360026fSyslogLevel_Object = MibScalar
xgs360026fSyslogLevel = _Xgs360026fSyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 5, 1, 4),
    _Xgs360026fSyslogLevel_Type()
)
xgs360026fSyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSyslogLevel.setStatus("current")
_Xgs360026fSyslogDetailedInfo_ObjectIdentity = ObjectIdentity
xgs360026fSyslogDetailedInfo = _Xgs360026fSyslogDetailedInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 5, 2)
)


class _Xgs360026fSyslogDetailedInfoClear_Type(Integer32):
    """Custom type xgs360026fSyslogDetailedInfoClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fSyslogDetailedInfoClear_Type.__name__ = "Integer32"
_Xgs360026fSyslogDetailedInfoClear_Object = MibScalar
xgs360026fSyslogDetailedInfoClear = _Xgs360026fSyslogDetailedInfoClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 5, 2, 1),
    _Xgs360026fSyslogDetailedInfoClear_Type()
)
xgs360026fSyslogDetailedInfoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSyslogDetailedInfoClear.setStatus("current")
_Xgs360026fSyslogDetailedInfoTable_Object = MibTable
xgs360026fSyslogDetailedInfoTable = _Xgs360026fSyslogDetailedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    xgs360026fSyslogDetailedInfoTable.setStatus("current")
_Xgs360026fSyslogDetailedInfoEntry_Object = MibTableRow
xgs360026fSyslogDetailedInfoEntry = _Xgs360026fSyslogDetailedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 5, 2, 2, 1)
)
xgs360026fSyslogDetailedInfoEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fSyslogDetailedInfoIndex"),
)
if mibBuilder.loadTexts:
    xgs360026fSyslogDetailedInfoEntry.setStatus("current")


class _Xgs360026fSyslogDetailedInfoIndex_Type(Integer32):
    """Custom type xgs360026fSyslogDetailedInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Xgs360026fSyslogDetailedInfoIndex_Type.__name__ = "Integer32"
_Xgs360026fSyslogDetailedInfoIndex_Object = MibTableColumn
xgs360026fSyslogDetailedInfoIndex = _Xgs360026fSyslogDetailedInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 5, 2, 2, 1, 1),
    _Xgs360026fSyslogDetailedInfoIndex_Type()
)
xgs360026fSyslogDetailedInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fSyslogDetailedInfoIndex.setStatus("current")
_Xgs360026fSyslogDetailedInfoLevel_Type = DisplayString
_Xgs360026fSyslogDetailedInfoLevel_Object = MibTableColumn
xgs360026fSyslogDetailedInfoLevel = _Xgs360026fSyslogDetailedInfoLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 5, 2, 2, 1, 2),
    _Xgs360026fSyslogDetailedInfoLevel_Type()
)
xgs360026fSyslogDetailedInfoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSyslogDetailedInfoLevel.setStatus("current")


class _Xgs360026fSyslogDetailedInfoTime_Type(DisplayString):
    """Custom type xgs360026fSyslogDetailedInfoTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Xgs360026fSyslogDetailedInfoTime_Type.__name__ = "DisplayString"
_Xgs360026fSyslogDetailedInfoTime_Object = MibTableColumn
xgs360026fSyslogDetailedInfoTime = _Xgs360026fSyslogDetailedInfoTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 5, 2, 2, 1, 3),
    _Xgs360026fSyslogDetailedInfoTime_Type()
)
xgs360026fSyslogDetailedInfoTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSyslogDetailedInfoTime.setStatus("current")
_Xgs360026fSyslogDetailedInfoMessage_Type = DisplayString
_Xgs360026fSyslogDetailedInfoMessage_Object = MibTableColumn
xgs360026fSyslogDetailedInfoMessage = _Xgs360026fSyslogDetailedInfoMessage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 5, 2, 2, 1, 4),
    _Xgs360026fSyslogDetailedInfoMessage_Type()
)
xgs360026fSyslogDetailedInfoMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSyslogDetailedInfoMessage.setStatus("current")
_Xgs360026fSnmp_ObjectIdentity = ObjectIdentity
xgs360026fSnmp = _Xgs360026fSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6)
)
_Xgs360026fSnmpConf_ObjectIdentity = ObjectIdentity
xgs360026fSnmpConf = _Xgs360026fSnmpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1)
)
_Xgs360026fGetCommunity_Type = DisplayString
_Xgs360026fGetCommunity_Object = MibScalar
xgs360026fGetCommunity = _Xgs360026fGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1, 1),
    _Xgs360026fGetCommunity_Type()
)
xgs360026fGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fGetCommunity.setStatus("current")


class _Xgs360026fSetCommunityMode_Type(Integer32):
    """Custom type xgs360026fSetCommunityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fSetCommunityMode_Type.__name__ = "Integer32"
_Xgs360026fSetCommunityMode_Object = MibScalar
xgs360026fSetCommunityMode = _Xgs360026fSetCommunityMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1, 2),
    _Xgs360026fSetCommunityMode_Type()
)
xgs360026fSetCommunityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSetCommunityMode.setStatus("current")
_Xgs360026fSetCommunity_Type = DisplayString
_Xgs360026fSetCommunity_Object = MibScalar
xgs360026fSetCommunity = _Xgs360026fSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1, 3),
    _Xgs360026fSetCommunity_Type()
)
xgs360026fSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSetCommunity.setStatus("current")
_Xgs360026fTrapHostConfTable_Object = MibTable
xgs360026fTrapHostConfTable = _Xgs360026fTrapHostConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1, 4)
)
if mibBuilder.loadTexts:
    xgs360026fTrapHostConfTable.setStatus("current")
_Xgs360026fTrapHostConfEntry_Object = MibTableRow
xgs360026fTrapHostConfEntry = _Xgs360026fTrapHostConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1, 4, 1)
)
xgs360026fTrapHostConfEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fTrapHostConfIndex"),
)
if mibBuilder.loadTexts:
    xgs360026fTrapHostConfEntry.setStatus("current")


class _Xgs360026fTrapHostConfIndex_Type(Integer32):
    """Custom type xgs360026fTrapHostConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Xgs360026fTrapHostConfIndex_Type.__name__ = "Integer32"
_Xgs360026fTrapHostConfIndex_Object = MibTableColumn
xgs360026fTrapHostConfIndex = _Xgs360026fTrapHostConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1, 4, 1, 1),
    _Xgs360026fTrapHostConfIndex_Type()
)
xgs360026fTrapHostConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fTrapHostConfIndex.setStatus("current")


class _Xgs360026fTrapHostConfVersion_Type(Integer32):
    """Custom type xgs360026fTrapHostConfVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3),
    )


_Xgs360026fTrapHostConfVersion_Type.__name__ = "Integer32"
_Xgs360026fTrapHostConfVersion_Object = MibTableColumn
xgs360026fTrapHostConfVersion = _Xgs360026fTrapHostConfVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1, 4, 1, 2),
    _Xgs360026fTrapHostConfVersion_Type()
)
xgs360026fTrapHostConfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapHostConfVersion.setStatus("current")


class _Xgs360026fTrapHostConfIPType_Type(Integer32):
    """Custom type xgs360026fTrapHostConfIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(6, 6),
    )


_Xgs360026fTrapHostConfIPType_Type.__name__ = "Integer32"
_Xgs360026fTrapHostConfIPType_Object = MibTableColumn
xgs360026fTrapHostConfIPType = _Xgs360026fTrapHostConfIPType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1, 4, 1, 3),
    _Xgs360026fTrapHostConfIPType_Type()
)
xgs360026fTrapHostConfIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapHostConfIPType.setStatus("current")
_Xgs360026fTrapHostConfIP_Type = DisplayString
_Xgs360026fTrapHostConfIP_Object = MibTableColumn
xgs360026fTrapHostConfIP = _Xgs360026fTrapHostConfIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1, 4, 1, 4),
    _Xgs360026fTrapHostConfIP_Type()
)
xgs360026fTrapHostConfIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapHostConfIP.setStatus("current")


class _Xgs360026fTrapHostConfPort_Type(Integer32):
    """Custom type xgs360026fTrapHostConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Xgs360026fTrapHostConfPort_Type.__name__ = "Integer32"
_Xgs360026fTrapHostConfPort_Object = MibTableColumn
xgs360026fTrapHostConfPort = _Xgs360026fTrapHostConfPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1, 4, 1, 5),
    _Xgs360026fTrapHostConfPort_Type()
)
xgs360026fTrapHostConfPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapHostConfPort.setStatus("current")


class _Xgs360026fTrapHostConfCommunity_Type(DisplayString):
    """Custom type xgs360026fTrapHostConfCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xgs360026fTrapHostConfCommunity_Type.__name__ = "DisplayString"
_Xgs360026fTrapHostConfCommunity_Object = MibTableColumn
xgs360026fTrapHostConfCommunity = _Xgs360026fTrapHostConfCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1, 4, 1, 6),
    _Xgs360026fTrapHostConfCommunity_Type()
)
xgs360026fTrapHostConfCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapHostConfCommunity.setStatus("current")


class _Xgs360026fTrapHostConfSeverityLevel_Type(Integer32):
    """Custom type xgs360026fTrapHostConfSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapHostConfSeverityLevel_Type.__name__ = "Integer32"
_Xgs360026fTrapHostConfSeverityLevel_Object = MibTableColumn
xgs360026fTrapHostConfSeverityLevel = _Xgs360026fTrapHostConfSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1, 4, 1, 7),
    _Xgs360026fTrapHostConfSeverityLevel_Type()
)
xgs360026fTrapHostConfSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapHostConfSeverityLevel.setStatus("current")


class _Xgs360026fTrapHostConfSecurityLevel_Type(Integer32):
    """Custom type xgs360026fTrapHostConfSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Xgs360026fTrapHostConfSecurityLevel_Type.__name__ = "Integer32"
_Xgs360026fTrapHostConfSecurityLevel_Object = MibTableColumn
xgs360026fTrapHostConfSecurityLevel = _Xgs360026fTrapHostConfSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1, 4, 1, 8),
    _Xgs360026fTrapHostConfSecurityLevel_Type()
)
xgs360026fTrapHostConfSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapHostConfSecurityLevel.setStatus("current")


class _Xgs360026fTrapHostConfAuthPtc_Type(Integer32):
    """Custom type xgs360026fTrapHostConfAuthPtc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Xgs360026fTrapHostConfAuthPtc_Type.__name__ = "Integer32"
_Xgs360026fTrapHostConfAuthPtc_Object = MibTableColumn
xgs360026fTrapHostConfAuthPtc = _Xgs360026fTrapHostConfAuthPtc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1, 4, 1, 9),
    _Xgs360026fTrapHostConfAuthPtc_Type()
)
xgs360026fTrapHostConfAuthPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapHostConfAuthPtc.setStatus("current")
_Xgs360026fTrapHostConfAuthPassword_Type = DisplayString
_Xgs360026fTrapHostConfAuthPassword_Object = MibTableColumn
xgs360026fTrapHostConfAuthPassword = _Xgs360026fTrapHostConfAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1, 4, 1, 10),
    _Xgs360026fTrapHostConfAuthPassword_Type()
)
xgs360026fTrapHostConfAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapHostConfAuthPassword.setStatus("current")


class _Xgs360026fTrapHostConfPrivPtc_Type(Integer32):
    """Custom type xgs360026fTrapHostConfPrivPtc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fTrapHostConfPrivPtc_Type.__name__ = "Integer32"
_Xgs360026fTrapHostConfPrivPtc_Object = MibTableColumn
xgs360026fTrapHostConfPrivPtc = _Xgs360026fTrapHostConfPrivPtc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1, 4, 1, 11),
    _Xgs360026fTrapHostConfPrivPtc_Type()
)
xgs360026fTrapHostConfPrivPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapHostConfPrivPtc.setStatus("current")
_Xgs360026fTrapHostConfPrivPassword_Type = DisplayString
_Xgs360026fTrapHostConfPrivPassword_Object = MibTableColumn
xgs360026fTrapHostConfPrivPassword = _Xgs360026fTrapHostConfPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1, 4, 1, 12),
    _Xgs360026fTrapHostConfPrivPassword_Type()
)
xgs360026fTrapHostConfPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapHostConfPrivPassword.setStatus("current")


class _Xgs360026fTrapHostConfCurrentMode_Type(Integer32):
    """Custom type xgs360026fTrapHostConfCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Xgs360026fTrapHostConfCurrentMode_Type.__name__ = "Integer32"
_Xgs360026fTrapHostConfCurrentMode_Object = MibTableColumn
xgs360026fTrapHostConfCurrentMode = _Xgs360026fTrapHostConfCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 1, 6, 1, 4, 1, 13),
    _Xgs360026fTrapHostConfCurrentMode_Type()
)
xgs360026fTrapHostConfCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapHostConfCurrentMode.setStatus("current")
_Xgs360026fConfiguration_ObjectIdentity = ObjectIdentity
xgs360026fConfiguration = _Xgs360026fConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2)
)
_Xgs360026fPort_ObjectIdentity = ObjectIdentity
xgs360026fPort = _Xgs360026fPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1)
)
_Xgs360026fPortConfigurationTable_Object = MibTable
xgs360026fPortConfigurationTable = _Xgs360026fPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xgs360026fPortConfigurationTable.setStatus("current")
_Xgs360026fPortConfigurationEntry_Object = MibTableRow
xgs360026fPortConfigurationEntry = _Xgs360026fPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 1, 1)
)
xgs360026fPortConfigurationEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fPortConfPort"),
)
if mibBuilder.loadTexts:
    xgs360026fPortConfigurationEntry.setStatus("current")


class _Xgs360026fPortConfPort_Type(Integer32):
    """Custom type xgs360026fPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fPortConfPort_Type.__name__ = "Integer32"
_Xgs360026fPortConfPort_Object = MibTableColumn
xgs360026fPortConfPort = _Xgs360026fPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 1, 1, 1),
    _Xgs360026fPortConfPort_Type()
)
xgs360026fPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fPortConfPort.setStatus("current")


class _Xgs360026fPortConfPortMedia_Type(DisplayString):
    """Custom type xgs360026fPortConfPortMedia based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_Xgs360026fPortConfPortMedia_Type.__name__ = "DisplayString"
_Xgs360026fPortConfPortMedia_Object = MibTableColumn
xgs360026fPortConfPortMedia = _Xgs360026fPortConfPortMedia_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 1, 1, 2),
    _Xgs360026fPortConfPortMedia_Type()
)
xgs360026fPortConfPortMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortConfPortMedia.setStatus("current")


class _Xgs360026fPortConfLink_Type(DisplayString):
    """Custom type xgs360026fPortConfLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_Xgs360026fPortConfLink_Type.__name__ = "DisplayString"
_Xgs360026fPortConfLink_Object = MibTableColumn
xgs360026fPortConfLink = _Xgs360026fPortConfLink_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 1, 1, 3),
    _Xgs360026fPortConfLink_Type()
)
xgs360026fPortConfLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortConfLink.setStatus("current")


class _Xgs360026fPortConfCurrentSpeed_Type(DisplayString):
    """Custom type xgs360026fPortConfCurrentSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 12),
    )


_Xgs360026fPortConfCurrentSpeed_Type.__name__ = "DisplayString"
_Xgs360026fPortConfCurrentSpeed_Object = MibTableColumn
xgs360026fPortConfCurrentSpeed = _Xgs360026fPortConfCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 1, 1, 4),
    _Xgs360026fPortConfCurrentSpeed_Type()
)
xgs360026fPortConfCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortConfCurrentSpeed.setStatus("current")


class _Xgs360026fPortConfSpeed_Type(Integer32):
    """Custom type xgs360026fPortConfSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_Xgs360026fPortConfSpeed_Type.__name__ = "Integer32"
_Xgs360026fPortConfSpeed_Object = MibTableColumn
xgs360026fPortConfSpeed = _Xgs360026fPortConfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 1, 1, 5),
    _Xgs360026fPortConfSpeed_Type()
)
xgs360026fPortConfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPortConfSpeed.setStatus("current")


class _Xgs360026fPortConfCurrentFlowControlRx_Type(Integer32):
    """Custom type xgs360026fPortConfCurrentFlowControlRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fPortConfCurrentFlowControlRx_Type.__name__ = "Integer32"
_Xgs360026fPortConfCurrentFlowControlRx_Object = MibTableColumn
xgs360026fPortConfCurrentFlowControlRx = _Xgs360026fPortConfCurrentFlowControlRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 1, 1, 6),
    _Xgs360026fPortConfCurrentFlowControlRx_Type()
)
xgs360026fPortConfCurrentFlowControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortConfCurrentFlowControlRx.setStatus("current")


class _Xgs360026fPortConfCurrentFlowControlTx_Type(Integer32):
    """Custom type xgs360026fPortConfCurrentFlowControlTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fPortConfCurrentFlowControlTx_Type.__name__ = "Integer32"
_Xgs360026fPortConfCurrentFlowControlTx_Object = MibTableColumn
xgs360026fPortConfCurrentFlowControlTx = _Xgs360026fPortConfCurrentFlowControlTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 1, 1, 7),
    _Xgs360026fPortConfCurrentFlowControlTx_Type()
)
xgs360026fPortConfCurrentFlowControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortConfCurrentFlowControlTx.setStatus("current")


class _Xgs360026fPortConfFlowControl_Type(Integer32):
    """Custom type xgs360026fPortConfFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fPortConfFlowControl_Type.__name__ = "Integer32"
_Xgs360026fPortConfFlowControl_Object = MibTableColumn
xgs360026fPortConfFlowControl = _Xgs360026fPortConfFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 1, 1, 8),
    _Xgs360026fPortConfFlowControl_Type()
)
xgs360026fPortConfFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPortConfFlowControl.setStatus("current")


class _Xgs360026fPortConfMaxFrameSize_Type(Integer32):
    """Custom type xgs360026fPortConfMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_Xgs360026fPortConfMaxFrameSize_Type.__name__ = "Integer32"
_Xgs360026fPortConfMaxFrameSize_Object = MibTableColumn
xgs360026fPortConfMaxFrameSize = _Xgs360026fPortConfMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 1, 1, 9),
    _Xgs360026fPortConfMaxFrameSize_Type()
)
xgs360026fPortConfMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPortConfMaxFrameSize.setStatus("current")


class _Xgs360026fPortConfExcessiveCollisionMode_Type(Integer32):
    """Custom type xgs360026fPortConfExcessiveCollisionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fPortConfExcessiveCollisionMode_Type.__name__ = "Integer32"
_Xgs360026fPortConfExcessiveCollisionMode_Object = MibTableColumn
xgs360026fPortConfExcessiveCollisionMode = _Xgs360026fPortConfExcessiveCollisionMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 1, 1, 10),
    _Xgs360026fPortConfExcessiveCollisionMode_Type()
)
xgs360026fPortConfExcessiveCollisionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPortConfExcessiveCollisionMode.setStatus("current")


class _Xgs360026fPortConfPowerControl_Type(Integer32):
    """Custom type xgs360026fPortConfPowerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Xgs360026fPortConfPowerControl_Type.__name__ = "Integer32"
_Xgs360026fPortConfPowerControl_Object = MibTableColumn
xgs360026fPortConfPowerControl = _Xgs360026fPortConfPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 1, 1, 11),
    _Xgs360026fPortConfPowerControl_Type()
)
xgs360026fPortConfPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPortConfPowerControl.setStatus("current")
_Xgs360026fPortConfDescription_Type = DisplayString
_Xgs360026fPortConfDescription_Object = MibTableColumn
xgs360026fPortConfDescription = _Xgs360026fPortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 1, 1, 12),
    _Xgs360026fPortConfDescription_Type()
)
xgs360026fPortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPortConfDescription.setStatus("current")
_Xgs360026fPortTrafficStatisticsTable_Object = MibTable
xgs360026fPortTrafficStatisticsTable = _Xgs360026fPortTrafficStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2)
)
if mibBuilder.loadTexts:
    xgs360026fPortTrafficStatisticsTable.setStatus("current")
_Xgs360026fPortTrafficStatisticsEntry_Object = MibTableRow
xgs360026fPortTrafficStatisticsEntry = _Xgs360026fPortTrafficStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1)
)
xgs360026fPortTrafficStatisticsEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fPortTrafficStatisticsPort"),
)
if mibBuilder.loadTexts:
    xgs360026fPortTrafficStatisticsEntry.setStatus("current")


class _Xgs360026fPortTrafficStatisticsPort_Type(Integer32):
    """Custom type xgs360026fPortTrafficStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fPortTrafficStatisticsPort_Type.__name__ = "Integer32"
_Xgs360026fPortTrafficStatisticsPort_Object = MibTableColumn
xgs360026fPortTrafficStatisticsPort = _Xgs360026fPortTrafficStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 1),
    _Xgs360026fPortTrafficStatisticsPort_Type()
)
xgs360026fPortTrafficStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficStatisticsPort.setStatus("current")


class _Xgs360026fPortTrafficStatisticsClear_Type(Integer32):
    """Custom type xgs360026fPortTrafficStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fPortTrafficStatisticsClear_Type.__name__ = "Integer32"
_Xgs360026fPortTrafficStatisticsClear_Object = MibTableColumn
xgs360026fPortTrafficStatisticsClear = _Xgs360026fPortTrafficStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 2),
    _Xgs360026fPortTrafficStatisticsClear_Type()
)
xgs360026fPortTrafficStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficStatisticsClear.setStatus("current")
_Xgs360026fPortTrafficRxPackets_Type = Counter64
_Xgs360026fPortTrafficRxPackets_Object = MibTableColumn
xgs360026fPortTrafficRxPackets = _Xgs360026fPortTrafficRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 3),
    _Xgs360026fPortTrafficRxPackets_Type()
)
xgs360026fPortTrafficRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxPackets.setStatus("current")
_Xgs360026fPortTrafficRxOctets_Type = Counter64
_Xgs360026fPortTrafficRxOctets_Object = MibTableColumn
xgs360026fPortTrafficRxOctets = _Xgs360026fPortTrafficRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 4),
    _Xgs360026fPortTrafficRxOctets_Type()
)
xgs360026fPortTrafficRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxOctets.setStatus("current")
_Xgs360026fPortTrafficRxUnicast_Type = Counter64
_Xgs360026fPortTrafficRxUnicast_Object = MibTableColumn
xgs360026fPortTrafficRxUnicast = _Xgs360026fPortTrafficRxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 5),
    _Xgs360026fPortTrafficRxUnicast_Type()
)
xgs360026fPortTrafficRxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxUnicast.setStatus("current")
_Xgs360026fPortTrafficRxMulticast_Type = Counter64
_Xgs360026fPortTrafficRxMulticast_Object = MibTableColumn
xgs360026fPortTrafficRxMulticast = _Xgs360026fPortTrafficRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 6),
    _Xgs360026fPortTrafficRxMulticast_Type()
)
xgs360026fPortTrafficRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxMulticast.setStatus("current")
_Xgs360026fPortTrafficRxBroadcast_Type = Counter64
_Xgs360026fPortTrafficRxBroadcast_Object = MibTableColumn
xgs360026fPortTrafficRxBroadcast = _Xgs360026fPortTrafficRxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 7),
    _Xgs360026fPortTrafficRxBroadcast_Type()
)
xgs360026fPortTrafficRxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxBroadcast.setStatus("current")
_Xgs360026fPortTrafficRxPause_Type = Counter64
_Xgs360026fPortTrafficRxPause_Object = MibTableColumn
xgs360026fPortTrafficRxPause = _Xgs360026fPortTrafficRxPause_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 8),
    _Xgs360026fPortTrafficRxPause_Type()
)
xgs360026fPortTrafficRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxPause.setStatus("current")
_Xgs360026fPortTrafficRx64Bytes_Type = Counter64
_Xgs360026fPortTrafficRx64Bytes_Object = MibTableColumn
xgs360026fPortTrafficRx64Bytes = _Xgs360026fPortTrafficRx64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 9),
    _Xgs360026fPortTrafficRx64Bytes_Type()
)
xgs360026fPortTrafficRx64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRx64Bytes.setStatus("current")
_Xgs360026fPortTrafficRx65to127Bytes_Type = Counter64
_Xgs360026fPortTrafficRx65to127Bytes_Object = MibTableColumn
xgs360026fPortTrafficRx65to127Bytes = _Xgs360026fPortTrafficRx65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 10),
    _Xgs360026fPortTrafficRx65to127Bytes_Type()
)
xgs360026fPortTrafficRx65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRx65to127Bytes.setStatus("current")
_Xgs360026fPortTrafficRx128to255Bytes_Type = Counter64
_Xgs360026fPortTrafficRx128to255Bytes_Object = MibTableColumn
xgs360026fPortTrafficRx128to255Bytes = _Xgs360026fPortTrafficRx128to255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 11),
    _Xgs360026fPortTrafficRx128to255Bytes_Type()
)
xgs360026fPortTrafficRx128to255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRx128to255Bytes.setStatus("current")
_Xgs360026fPortTrafficRx256to511Bytes_Type = Counter64
_Xgs360026fPortTrafficRx256to511Bytes_Object = MibTableColumn
xgs360026fPortTrafficRx256to511Bytes = _Xgs360026fPortTrafficRx256to511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 12),
    _Xgs360026fPortTrafficRx256to511Bytes_Type()
)
xgs360026fPortTrafficRx256to511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRx256to511Bytes.setStatus("current")
_Xgs360026fPortTrafficRx512to1023Bytes_Type = Counter64
_Xgs360026fPortTrafficRx512to1023Bytes_Object = MibTableColumn
xgs360026fPortTrafficRx512to1023Bytes = _Xgs360026fPortTrafficRx512to1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 13),
    _Xgs360026fPortTrafficRx512to1023Bytes_Type()
)
xgs360026fPortTrafficRx512to1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRx512to1023Bytes.setStatus("current")
_Xgs360026fPortTrafficRx1024to1526Bytes_Type = Counter64
_Xgs360026fPortTrafficRx1024to1526Bytes_Object = MibTableColumn
xgs360026fPortTrafficRx1024to1526Bytes = _Xgs360026fPortTrafficRx1024to1526Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 14),
    _Xgs360026fPortTrafficRx1024to1526Bytes_Type()
)
xgs360026fPortTrafficRx1024to1526Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRx1024to1526Bytes.setStatus("current")
_Xgs360026fPortTrafficRxExceecd1527Bytes_Type = Counter64
_Xgs360026fPortTrafficRxExceecd1527Bytes_Object = MibTableColumn
xgs360026fPortTrafficRxExceecd1527Bytes = _Xgs360026fPortTrafficRxExceecd1527Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 15),
    _Xgs360026fPortTrafficRxExceecd1527Bytes_Type()
)
xgs360026fPortTrafficRxExceecd1527Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxExceecd1527Bytes.setStatus("current")
_Xgs360026fPortTrafficRxQ0_Type = Counter64
_Xgs360026fPortTrafficRxQ0_Object = MibTableColumn
xgs360026fPortTrafficRxQ0 = _Xgs360026fPortTrafficRxQ0_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 16),
    _Xgs360026fPortTrafficRxQ0_Type()
)
xgs360026fPortTrafficRxQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxQ0.setStatus("current")
_Xgs360026fPortTrafficRxQ1_Type = Counter64
_Xgs360026fPortTrafficRxQ1_Object = MibTableColumn
xgs360026fPortTrafficRxQ1 = _Xgs360026fPortTrafficRxQ1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 17),
    _Xgs360026fPortTrafficRxQ1_Type()
)
xgs360026fPortTrafficRxQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxQ1.setStatus("current")
_Xgs360026fPortTrafficRxQ2_Type = Counter64
_Xgs360026fPortTrafficRxQ2_Object = MibTableColumn
xgs360026fPortTrafficRxQ2 = _Xgs360026fPortTrafficRxQ2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 18),
    _Xgs360026fPortTrafficRxQ2_Type()
)
xgs360026fPortTrafficRxQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxQ2.setStatus("current")
_Xgs360026fPortTrafficRxQ3_Type = Counter64
_Xgs360026fPortTrafficRxQ3_Object = MibTableColumn
xgs360026fPortTrafficRxQ3 = _Xgs360026fPortTrafficRxQ3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 19),
    _Xgs360026fPortTrafficRxQ3_Type()
)
xgs360026fPortTrafficRxQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxQ3.setStatus("current")
_Xgs360026fPortTrafficRxQ4_Type = Counter64
_Xgs360026fPortTrafficRxQ4_Object = MibTableColumn
xgs360026fPortTrafficRxQ4 = _Xgs360026fPortTrafficRxQ4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 20),
    _Xgs360026fPortTrafficRxQ4_Type()
)
xgs360026fPortTrafficRxQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxQ4.setStatus("current")
_Xgs360026fPortTrafficRxQ5_Type = Counter64
_Xgs360026fPortTrafficRxQ5_Object = MibTableColumn
xgs360026fPortTrafficRxQ5 = _Xgs360026fPortTrafficRxQ5_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 21),
    _Xgs360026fPortTrafficRxQ5_Type()
)
xgs360026fPortTrafficRxQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxQ5.setStatus("current")
_Xgs360026fPortTrafficRxQ6_Type = Counter64
_Xgs360026fPortTrafficRxQ6_Object = MibTableColumn
xgs360026fPortTrafficRxQ6 = _Xgs360026fPortTrafficRxQ6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 22),
    _Xgs360026fPortTrafficRxQ6_Type()
)
xgs360026fPortTrafficRxQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxQ6.setStatus("current")
_Xgs360026fPortTrafficRxQ7_Type = Counter64
_Xgs360026fPortTrafficRxQ7_Object = MibTableColumn
xgs360026fPortTrafficRxQ7 = _Xgs360026fPortTrafficRxQ7_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 23),
    _Xgs360026fPortTrafficRxQ7_Type()
)
xgs360026fPortTrafficRxQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxQ7.setStatus("current")
_Xgs360026fPortTrafficRxDrops_Type = Counter64
_Xgs360026fPortTrafficRxDrops_Object = MibTableColumn
xgs360026fPortTrafficRxDrops = _Xgs360026fPortTrafficRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 24),
    _Xgs360026fPortTrafficRxDrops_Type()
)
xgs360026fPortTrafficRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxDrops.setStatus("current")
_Xgs360026fPortTrafficRxCRCorAlignment_Type = Counter64
_Xgs360026fPortTrafficRxCRCorAlignment_Object = MibTableColumn
xgs360026fPortTrafficRxCRCorAlignment = _Xgs360026fPortTrafficRxCRCorAlignment_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 25),
    _Xgs360026fPortTrafficRxCRCorAlignment_Type()
)
xgs360026fPortTrafficRxCRCorAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxCRCorAlignment.setStatus("current")
_Xgs360026fPortTrafficRxUndersize_Type = Counter64
_Xgs360026fPortTrafficRxUndersize_Object = MibTableColumn
xgs360026fPortTrafficRxUndersize = _Xgs360026fPortTrafficRxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 26),
    _Xgs360026fPortTrafficRxUndersize_Type()
)
xgs360026fPortTrafficRxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxUndersize.setStatus("current")
_Xgs360026fPortTrafficRxOversize_Type = Counter64
_Xgs360026fPortTrafficRxOversize_Object = MibTableColumn
xgs360026fPortTrafficRxOversize = _Xgs360026fPortTrafficRxOversize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 27),
    _Xgs360026fPortTrafficRxOversize_Type()
)
xgs360026fPortTrafficRxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxOversize.setStatus("current")
_Xgs360026fPortTrafficRxFragments_Type = Counter64
_Xgs360026fPortTrafficRxFragments_Object = MibTableColumn
xgs360026fPortTrafficRxFragments = _Xgs360026fPortTrafficRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 28),
    _Xgs360026fPortTrafficRxFragments_Type()
)
xgs360026fPortTrafficRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxFragments.setStatus("current")
_Xgs360026fPortTrafficRxJabber_Type = Counter64
_Xgs360026fPortTrafficRxJabber_Object = MibTableColumn
xgs360026fPortTrafficRxJabber = _Xgs360026fPortTrafficRxJabber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 29),
    _Xgs360026fPortTrafficRxJabber_Type()
)
xgs360026fPortTrafficRxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxJabber.setStatus("current")
_Xgs360026fPortTrafficRxFiltered_Type = Counter64
_Xgs360026fPortTrafficRxFiltered_Object = MibTableColumn
xgs360026fPortTrafficRxFiltered = _Xgs360026fPortTrafficRxFiltered_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 30),
    _Xgs360026fPortTrafficRxFiltered_Type()
)
xgs360026fPortTrafficRxFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficRxFiltered.setStatus("current")
_Xgs360026fPortTrafficTxPackets_Type = Counter64
_Xgs360026fPortTrafficTxPackets_Object = MibTableColumn
xgs360026fPortTrafficTxPackets = _Xgs360026fPortTrafficTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 31),
    _Xgs360026fPortTrafficTxPackets_Type()
)
xgs360026fPortTrafficTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTxPackets.setStatus("current")
_Xgs360026fPortTrafficTxOctets_Type = Counter64
_Xgs360026fPortTrafficTxOctets_Object = MibTableColumn
xgs360026fPortTrafficTxOctets = _Xgs360026fPortTrafficTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 32),
    _Xgs360026fPortTrafficTxOctets_Type()
)
xgs360026fPortTrafficTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTxOctets.setStatus("current")
_Xgs360026fPortTrafficTxUnicast_Type = Counter64
_Xgs360026fPortTrafficTxUnicast_Object = MibTableColumn
xgs360026fPortTrafficTxUnicast = _Xgs360026fPortTrafficTxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 33),
    _Xgs360026fPortTrafficTxUnicast_Type()
)
xgs360026fPortTrafficTxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTxUnicast.setStatus("current")
_Xgs360026fPortTrafficTxMulticast_Type = Counter64
_Xgs360026fPortTrafficTxMulticast_Object = MibTableColumn
xgs360026fPortTrafficTxMulticast = _Xgs360026fPortTrafficTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 34),
    _Xgs360026fPortTrafficTxMulticast_Type()
)
xgs360026fPortTrafficTxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTxMulticast.setStatus("current")
_Xgs360026fPortTrafficTxBroadcast_Type = Counter64
_Xgs360026fPortTrafficTxBroadcast_Object = MibTableColumn
xgs360026fPortTrafficTxBroadcast = _Xgs360026fPortTrafficTxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 35),
    _Xgs360026fPortTrafficTxBroadcast_Type()
)
xgs360026fPortTrafficTxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTxBroadcast.setStatus("current")
_Xgs360026fPortTrafficTxPause_Type = Counter64
_Xgs360026fPortTrafficTxPause_Object = MibTableColumn
xgs360026fPortTrafficTxPause = _Xgs360026fPortTrafficTxPause_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 36),
    _Xgs360026fPortTrafficTxPause_Type()
)
xgs360026fPortTrafficTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTxPause.setStatus("current")
_Xgs360026fPortTrafficTx64Bytes_Type = Counter64
_Xgs360026fPortTrafficTx64Bytes_Object = MibTableColumn
xgs360026fPortTrafficTx64Bytes = _Xgs360026fPortTrafficTx64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 37),
    _Xgs360026fPortTrafficTx64Bytes_Type()
)
xgs360026fPortTrafficTx64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTx64Bytes.setStatus("current")
_Xgs360026fPortTrafficTx65to127Bytes_Type = Counter64
_Xgs360026fPortTrafficTx65to127Bytes_Object = MibTableColumn
xgs360026fPortTrafficTx65to127Bytes = _Xgs360026fPortTrafficTx65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 38),
    _Xgs360026fPortTrafficTx65to127Bytes_Type()
)
xgs360026fPortTrafficTx65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTx65to127Bytes.setStatus("current")
_Xgs360026fPortTrafficTx128to255Bytes_Type = Counter64
_Xgs360026fPortTrafficTx128to255Bytes_Object = MibTableColumn
xgs360026fPortTrafficTx128to255Bytes = _Xgs360026fPortTrafficTx128to255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 39),
    _Xgs360026fPortTrafficTx128to255Bytes_Type()
)
xgs360026fPortTrafficTx128to255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTx128to255Bytes.setStatus("current")
_Xgs360026fPortTrafficTx256to511Bytes_Type = Counter64
_Xgs360026fPortTrafficTx256to511Bytes_Object = MibTableColumn
xgs360026fPortTrafficTx256to511Bytes = _Xgs360026fPortTrafficTx256to511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 40),
    _Xgs360026fPortTrafficTx256to511Bytes_Type()
)
xgs360026fPortTrafficTx256to511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTx256to511Bytes.setStatus("current")
_Xgs360026fPortTrafficTx512to1023Bytes_Type = Counter64
_Xgs360026fPortTrafficTx512to1023Bytes_Object = MibTableColumn
xgs360026fPortTrafficTx512to1023Bytes = _Xgs360026fPortTrafficTx512to1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 41),
    _Xgs360026fPortTrafficTx512to1023Bytes_Type()
)
xgs360026fPortTrafficTx512to1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTx512to1023Bytes.setStatus("current")
_Xgs360026fPortTrafficTx1024to1526Bytes_Type = Counter64
_Xgs360026fPortTrafficTx1024to1526Bytes_Object = MibTableColumn
xgs360026fPortTrafficTx1024to1526Bytes = _Xgs360026fPortTrafficTx1024to1526Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 42),
    _Xgs360026fPortTrafficTx1024to1526Bytes_Type()
)
xgs360026fPortTrafficTx1024to1526Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTx1024to1526Bytes.setStatus("current")
_Xgs360026fPortTrafficTxExceecd1527Bytes_Type = Counter64
_Xgs360026fPortTrafficTxExceecd1527Bytes_Object = MibTableColumn
xgs360026fPortTrafficTxExceecd1527Bytes = _Xgs360026fPortTrafficTxExceecd1527Bytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 43),
    _Xgs360026fPortTrafficTxExceecd1527Bytes_Type()
)
xgs360026fPortTrafficTxExceecd1527Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTxExceecd1527Bytes.setStatus("current")
_Xgs360026fPortTrafficTxQ0_Type = Counter64
_Xgs360026fPortTrafficTxQ0_Object = MibTableColumn
xgs360026fPortTrafficTxQ0 = _Xgs360026fPortTrafficTxQ0_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 44),
    _Xgs360026fPortTrafficTxQ0_Type()
)
xgs360026fPortTrafficTxQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTxQ0.setStatus("current")
_Xgs360026fPortTrafficTxQ1_Type = Counter64
_Xgs360026fPortTrafficTxQ1_Object = MibTableColumn
xgs360026fPortTrafficTxQ1 = _Xgs360026fPortTrafficTxQ1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 45),
    _Xgs360026fPortTrafficTxQ1_Type()
)
xgs360026fPortTrafficTxQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTxQ1.setStatus("current")
_Xgs360026fPortTrafficTxQ2_Type = Counter64
_Xgs360026fPortTrafficTxQ2_Object = MibTableColumn
xgs360026fPortTrafficTxQ2 = _Xgs360026fPortTrafficTxQ2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 46),
    _Xgs360026fPortTrafficTxQ2_Type()
)
xgs360026fPortTrafficTxQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTxQ2.setStatus("current")
_Xgs360026fPortTrafficTxQ3_Type = Counter64
_Xgs360026fPortTrafficTxQ3_Object = MibTableColumn
xgs360026fPortTrafficTxQ3 = _Xgs360026fPortTrafficTxQ3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 47),
    _Xgs360026fPortTrafficTxQ3_Type()
)
xgs360026fPortTrafficTxQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTxQ3.setStatus("current")
_Xgs360026fPortTrafficTxQ4_Type = Counter64
_Xgs360026fPortTrafficTxQ4_Object = MibTableColumn
xgs360026fPortTrafficTxQ4 = _Xgs360026fPortTrafficTxQ4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 48),
    _Xgs360026fPortTrafficTxQ4_Type()
)
xgs360026fPortTrafficTxQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTxQ4.setStatus("current")
_Xgs360026fPortTrafficTxQ5_Type = Counter64
_Xgs360026fPortTrafficTxQ5_Object = MibTableColumn
xgs360026fPortTrafficTxQ5 = _Xgs360026fPortTrafficTxQ5_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 49),
    _Xgs360026fPortTrafficTxQ5_Type()
)
xgs360026fPortTrafficTxQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTxQ5.setStatus("current")
_Xgs360026fPortTrafficTxQ6_Type = Counter64
_Xgs360026fPortTrafficTxQ6_Object = MibTableColumn
xgs360026fPortTrafficTxQ6 = _Xgs360026fPortTrafficTxQ6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 50),
    _Xgs360026fPortTrafficTxQ6_Type()
)
xgs360026fPortTrafficTxQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTxQ6.setStatus("current")
_Xgs360026fPortTrafficTxQ7_Type = Counter64
_Xgs360026fPortTrafficTxQ7_Object = MibTableColumn
xgs360026fPortTrafficTxQ7 = _Xgs360026fPortTrafficTxQ7_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 51),
    _Xgs360026fPortTrafficTxQ7_Type()
)
xgs360026fPortTrafficTxQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTxQ7.setStatus("current")
_Xgs360026fPortTrafficTxDrops_Type = Counter64
_Xgs360026fPortTrafficTxDrops_Object = MibTableColumn
xgs360026fPortTrafficTxDrops = _Xgs360026fPortTrafficTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 52),
    _Xgs360026fPortTrafficTxDrops_Type()
)
xgs360026fPortTrafficTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTxDrops.setStatus("current")
_Xgs360026fPortTrafficTxLateOrExcColl_Type = Counter64
_Xgs360026fPortTrafficTxLateOrExcColl_Object = MibTableColumn
xgs360026fPortTrafficTxLateOrExcColl = _Xgs360026fPortTrafficTxLateOrExcColl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 2, 1, 53),
    _Xgs360026fPortTrafficTxLateOrExcColl_Type()
)
xgs360026fPortTrafficTxLateOrExcColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortTrafficTxLateOrExcColl.setStatus("current")
_Xgs360026fPortQoSStatistics_ObjectIdentity = ObjectIdentity
xgs360026fPortQoSStatistics = _Xgs360026fPortQoSStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3)
)


class _Xgs360026fPortQoSStatisticsClear_Type(Integer32):
    """Custom type xgs360026fPortQoSStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fPortQoSStatisticsClear_Type.__name__ = "Integer32"
_Xgs360026fPortQoSStatisticsClear_Object = MibScalar
xgs360026fPortQoSStatisticsClear = _Xgs360026fPortQoSStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 1),
    _Xgs360026fPortQoSStatisticsClear_Type()
)
xgs360026fPortQoSStatisticsClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortQoSStatisticsClear.setStatus("current")
_Xgs360026fPortQoSStatisticsTable_Object = MibTable
xgs360026fPortQoSStatisticsTable = _Xgs360026fPortQoSStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    xgs360026fPortQoSStatisticsTable.setStatus("current")
_Xgs360026fPortQoSStatisticsEntry_Object = MibTableRow
xgs360026fPortQoSStatisticsEntry = _Xgs360026fPortQoSStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2, 1)
)
xgs360026fPortQoSStatisticsEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fPortQoSStatisticsPort"),
)
if mibBuilder.loadTexts:
    xgs360026fPortQoSStatisticsEntry.setStatus("current")


class _Xgs360026fPortQoSStatisticsPort_Type(Integer32):
    """Custom type xgs360026fPortQoSStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fPortQoSStatisticsPort_Type.__name__ = "Integer32"
_Xgs360026fPortQoSStatisticsPort_Object = MibTableColumn
xgs360026fPortQoSStatisticsPort = _Xgs360026fPortQoSStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2, 1, 1),
    _Xgs360026fPortQoSStatisticsPort_Type()
)
xgs360026fPortQoSStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fPortQoSStatisticsPort.setStatus("current")
_Xgs360026fPortQoSQ0Rx_Type = Counter64
_Xgs360026fPortQoSQ0Rx_Object = MibTableColumn
xgs360026fPortQoSQ0Rx = _Xgs360026fPortQoSQ0Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2, 1, 2),
    _Xgs360026fPortQoSQ0Rx_Type()
)
xgs360026fPortQoSQ0Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortQoSQ0Rx.setStatus("current")
_Xgs360026fPortQoSQ0Tx_Type = Counter64
_Xgs360026fPortQoSQ0Tx_Object = MibTableColumn
xgs360026fPortQoSQ0Tx = _Xgs360026fPortQoSQ0Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2, 1, 3),
    _Xgs360026fPortQoSQ0Tx_Type()
)
xgs360026fPortQoSQ0Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortQoSQ0Tx.setStatus("current")
_Xgs360026fPortQoSQ1Rx_Type = Counter64
_Xgs360026fPortQoSQ1Rx_Object = MibTableColumn
xgs360026fPortQoSQ1Rx = _Xgs360026fPortQoSQ1Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2, 1, 4),
    _Xgs360026fPortQoSQ1Rx_Type()
)
xgs360026fPortQoSQ1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortQoSQ1Rx.setStatus("current")
_Xgs360026fPortQoSQ1Tx_Type = Counter64
_Xgs360026fPortQoSQ1Tx_Object = MibTableColumn
xgs360026fPortQoSQ1Tx = _Xgs360026fPortQoSQ1Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2, 1, 5),
    _Xgs360026fPortQoSQ1Tx_Type()
)
xgs360026fPortQoSQ1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortQoSQ1Tx.setStatus("current")
_Xgs360026fPortQoSQ2Rx_Type = Counter64
_Xgs360026fPortQoSQ2Rx_Object = MibTableColumn
xgs360026fPortQoSQ2Rx = _Xgs360026fPortQoSQ2Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2, 1, 6),
    _Xgs360026fPortQoSQ2Rx_Type()
)
xgs360026fPortQoSQ2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortQoSQ2Rx.setStatus("current")
_Xgs360026fPortQoSQ2Tx_Type = Counter64
_Xgs360026fPortQoSQ2Tx_Object = MibTableColumn
xgs360026fPortQoSQ2Tx = _Xgs360026fPortQoSQ2Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2, 1, 7),
    _Xgs360026fPortQoSQ2Tx_Type()
)
xgs360026fPortQoSQ2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortQoSQ2Tx.setStatus("current")
_Xgs360026fPortQoSQ3Rx_Type = Counter64
_Xgs360026fPortQoSQ3Rx_Object = MibTableColumn
xgs360026fPortQoSQ3Rx = _Xgs360026fPortQoSQ3Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2, 1, 8),
    _Xgs360026fPortQoSQ3Rx_Type()
)
xgs360026fPortQoSQ3Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortQoSQ3Rx.setStatus("current")
_Xgs360026fPortQoSQ3Tx_Type = Counter64
_Xgs360026fPortQoSQ3Tx_Object = MibTableColumn
xgs360026fPortQoSQ3Tx = _Xgs360026fPortQoSQ3Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2, 1, 9),
    _Xgs360026fPortQoSQ3Tx_Type()
)
xgs360026fPortQoSQ3Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortQoSQ3Tx.setStatus("current")
_Xgs360026fPortQoSQ4Rx_Type = Counter64
_Xgs360026fPortQoSQ4Rx_Object = MibTableColumn
xgs360026fPortQoSQ4Rx = _Xgs360026fPortQoSQ4Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2, 1, 10),
    _Xgs360026fPortQoSQ4Rx_Type()
)
xgs360026fPortQoSQ4Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortQoSQ4Rx.setStatus("current")
_Xgs360026fPortQoSQ4Tx_Type = Counter64
_Xgs360026fPortQoSQ4Tx_Object = MibTableColumn
xgs360026fPortQoSQ4Tx = _Xgs360026fPortQoSQ4Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2, 1, 11),
    _Xgs360026fPortQoSQ4Tx_Type()
)
xgs360026fPortQoSQ4Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortQoSQ4Tx.setStatus("current")
_Xgs360026fPortQoSQ5Rx_Type = Counter64
_Xgs360026fPortQoSQ5Rx_Object = MibTableColumn
xgs360026fPortQoSQ5Rx = _Xgs360026fPortQoSQ5Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2, 1, 12),
    _Xgs360026fPortQoSQ5Rx_Type()
)
xgs360026fPortQoSQ5Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortQoSQ5Rx.setStatus("current")
_Xgs360026fPortQoSQ5Tx_Type = Counter64
_Xgs360026fPortQoSQ5Tx_Object = MibTableColumn
xgs360026fPortQoSQ5Tx = _Xgs360026fPortQoSQ5Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2, 1, 13),
    _Xgs360026fPortQoSQ5Tx_Type()
)
xgs360026fPortQoSQ5Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortQoSQ5Tx.setStatus("current")
_Xgs360026fPortQoSQ6Rx_Type = Counter64
_Xgs360026fPortQoSQ6Rx_Object = MibTableColumn
xgs360026fPortQoSQ6Rx = _Xgs360026fPortQoSQ6Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2, 1, 14),
    _Xgs360026fPortQoSQ6Rx_Type()
)
xgs360026fPortQoSQ6Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortQoSQ6Rx.setStatus("current")
_Xgs360026fPortQoSQ6Tx_Type = Counter64
_Xgs360026fPortQoSQ6Tx_Object = MibTableColumn
xgs360026fPortQoSQ6Tx = _Xgs360026fPortQoSQ6Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2, 1, 15),
    _Xgs360026fPortQoSQ6Tx_Type()
)
xgs360026fPortQoSQ6Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortQoSQ6Tx.setStatus("current")
_Xgs360026fPortQoSQ7Rx_Type = Counter64
_Xgs360026fPortQoSQ7Rx_Object = MibTableColumn
xgs360026fPortQoSQ7Rx = _Xgs360026fPortQoSQ7Rx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2, 1, 16),
    _Xgs360026fPortQoSQ7Rx_Type()
)
xgs360026fPortQoSQ7Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortQoSQ7Rx.setStatus("current")
_Xgs360026fPortQoSQ7Tx_Type = Counter64
_Xgs360026fPortQoSQ7Tx_Object = MibTableColumn
xgs360026fPortQoSQ7Tx = _Xgs360026fPortQoSQ7Tx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 3, 2, 1, 17),
    _Xgs360026fPortQoSQ7Tx_Type()
)
xgs360026fPortQoSQ7Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortQoSQ7Tx.setStatus("current")
_Xgs360026fSFPInfoTable_Object = MibTable
xgs360026fSFPInfoTable = _Xgs360026fSFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4)
)
if mibBuilder.loadTexts:
    xgs360026fSFPInfoTable.setStatus("current")
_Xgs360026fSFPInfoEntry_Object = MibTableRow
xgs360026fSFPInfoEntry = _Xgs360026fSFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4, 1)
)
xgs360026fSFPInfoEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fSFPInfoIndex"),
)
if mibBuilder.loadTexts:
    xgs360026fSFPInfoEntry.setStatus("current")


class _Xgs360026fSFPInfoIndex_Type(Integer32):
    """Custom type xgs360026fSFPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fSFPInfoIndex_Type.__name__ = "Integer32"
_Xgs360026fSFPInfoIndex_Object = MibTableColumn
xgs360026fSFPInfoIndex = _Xgs360026fSFPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4, 1, 1),
    _Xgs360026fSFPInfoIndex_Type()
)
xgs360026fSFPInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fSFPInfoIndex.setStatus("current")
_Xgs360026fSFPInfoPort_Type = DisplayString
_Xgs360026fSFPInfoPort_Object = MibTableColumn
xgs360026fSFPInfoPort = _Xgs360026fSFPInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4, 1, 2),
    _Xgs360026fSFPInfoPort_Type()
)
xgs360026fSFPInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSFPInfoPort.setStatus("current")
_Xgs360026fSFPConnectorType_Type = DisplayString
_Xgs360026fSFPConnectorType_Object = MibTableColumn
xgs360026fSFPConnectorType = _Xgs360026fSFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4, 1, 3),
    _Xgs360026fSFPConnectorType_Type()
)
xgs360026fSFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSFPConnectorType.setStatus("current")
_Xgs360026fSFPFiberType_Type = DisplayString
_Xgs360026fSFPFiberType_Object = MibTableColumn
xgs360026fSFPFiberType = _Xgs360026fSFPFiberType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4, 1, 4),
    _Xgs360026fSFPFiberType_Type()
)
xgs360026fSFPFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSFPFiberType.setStatus("current")
_Xgs360026fSFPTxCentralWavelength_Type = DisplayString
_Xgs360026fSFPTxCentralWavelength_Object = MibTableColumn
xgs360026fSFPTxCentralWavelength = _Xgs360026fSFPTxCentralWavelength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4, 1, 5),
    _Xgs360026fSFPTxCentralWavelength_Type()
)
xgs360026fSFPTxCentralWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSFPTxCentralWavelength.setStatus("current")
_Xgs360026fSFPBaudRate_Type = DisplayString
_Xgs360026fSFPBaudRate_Object = MibTableColumn
xgs360026fSFPBaudRate = _Xgs360026fSFPBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4, 1, 6),
    _Xgs360026fSFPBaudRate_Type()
)
xgs360026fSFPBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSFPBaudRate.setStatus("current")
_Xgs360026fSFPVendorOUI_Type = DisplayString
_Xgs360026fSFPVendorOUI_Object = MibTableColumn
xgs360026fSFPVendorOUI = _Xgs360026fSFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4, 1, 7),
    _Xgs360026fSFPVendorOUI_Type()
)
xgs360026fSFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSFPVendorOUI.setStatus("current")
_Xgs360026fSFPVendorName_Type = DisplayString
_Xgs360026fSFPVendorName_Object = MibTableColumn
xgs360026fSFPVendorName = _Xgs360026fSFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4, 1, 8),
    _Xgs360026fSFPVendorName_Type()
)
xgs360026fSFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSFPVendorName.setStatus("current")
_Xgs360026fSFPVendorPN_Type = DisplayString
_Xgs360026fSFPVendorPN_Object = MibTableColumn
xgs360026fSFPVendorPN = _Xgs360026fSFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4, 1, 9),
    _Xgs360026fSFPVendorPN_Type()
)
xgs360026fSFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSFPVendorPN.setStatus("current")
_Xgs360026fSFPVendorRev_Type = DisplayString
_Xgs360026fSFPVendorRev_Object = MibTableColumn
xgs360026fSFPVendorRev = _Xgs360026fSFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4, 1, 10),
    _Xgs360026fSFPVendorRev_Type()
)
xgs360026fSFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSFPVendorRev.setStatus("current")
_Xgs360026fSFPVendorSN_Type = DisplayString
_Xgs360026fSFPVendorSN_Object = MibTableColumn
xgs360026fSFPVendorSN = _Xgs360026fSFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4, 1, 11),
    _Xgs360026fSFPVendorSN_Type()
)
xgs360026fSFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSFPVendorSN.setStatus("current")
_Xgs360026fSFPDateCode_Type = DisplayString
_Xgs360026fSFPDateCode_Object = MibTableColumn
xgs360026fSFPDateCode = _Xgs360026fSFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4, 1, 12),
    _Xgs360026fSFPDateCode_Type()
)
xgs360026fSFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSFPDateCode.setStatus("current")
_Xgs360026fSFPTemperature_Type = DisplayString
_Xgs360026fSFPTemperature_Object = MibTableColumn
xgs360026fSFPTemperature = _Xgs360026fSFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4, 1, 13),
    _Xgs360026fSFPTemperature_Type()
)
xgs360026fSFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSFPTemperature.setStatus("current")
_Xgs360026fSFPVcc_Type = DisplayString
_Xgs360026fSFPVcc_Object = MibTableColumn
xgs360026fSFPVcc = _Xgs360026fSFPVcc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4, 1, 14),
    _Xgs360026fSFPVcc_Type()
)
xgs360026fSFPVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSFPVcc.setStatus("current")
_Xgs360026fSFPMon1Bias_Type = DisplayString
_Xgs360026fSFPMon1Bias_Object = MibTableColumn
xgs360026fSFPMon1Bias = _Xgs360026fSFPMon1Bias_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4, 1, 15),
    _Xgs360026fSFPMon1Bias_Type()
)
xgs360026fSFPMon1Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSFPMon1Bias.setStatus("current")
_Xgs360026fSFPMon2TxPWR_Type = DisplayString
_Xgs360026fSFPMon2TxPWR_Object = MibTableColumn
xgs360026fSFPMon2TxPWR = _Xgs360026fSFPMon2TxPWR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4, 1, 16),
    _Xgs360026fSFPMon2TxPWR_Type()
)
xgs360026fSFPMon2TxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSFPMon2TxPWR.setStatus("current")
_Xgs360026fSFPMon3RxPWR_Type = DisplayString
_Xgs360026fSFPMon3RxPWR_Object = MibTableColumn
xgs360026fSFPMon3RxPWR = _Xgs360026fSFPMon3RxPWR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 1, 4, 1, 17),
    _Xgs360026fSFPMon3RxPWR_Type()
)
xgs360026fSFPMon3RxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSFPMon3RxPWR.setStatus("current")
_Xgs360026fGARP_ObjectIdentity = ObjectIdentity
xgs360026fGARP = _Xgs360026fGARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 3)
)
_Xgs360026fGARPConfTable_Object = MibTable
xgs360026fGARPConfTable = _Xgs360026fGARPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 3, 1)
)
if mibBuilder.loadTexts:
    xgs360026fGARPConfTable.setStatus("current")
_Xgs360026fGARPConfEntry_Object = MibTableRow
xgs360026fGARPConfEntry = _Xgs360026fGARPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 3, 1, 1)
)
xgs360026fGARPConfEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fGARPConfPort"),
)
if mibBuilder.loadTexts:
    xgs360026fGARPConfEntry.setStatus("current")


class _Xgs360026fGARPConfPort_Type(Integer32):
    """Custom type xgs360026fGARPConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fGARPConfPort_Type.__name__ = "Integer32"
_Xgs360026fGARPConfPort_Object = MibTableColumn
xgs360026fGARPConfPort = _Xgs360026fGARPConfPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 3, 1, 1, 1),
    _Xgs360026fGARPConfPort_Type()
)
xgs360026fGARPConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fGARPConfPort.setStatus("current")


class _Xgs360026fGARPJoinTimer_Type(Integer32):
    """Custom type xgs360026fGARPJoinTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_Xgs360026fGARPJoinTimer_Type.__name__ = "Integer32"
_Xgs360026fGARPJoinTimer_Object = MibTableColumn
xgs360026fGARPJoinTimer = _Xgs360026fGARPJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 3, 1, 1, 2),
    _Xgs360026fGARPJoinTimer_Type()
)
xgs360026fGARPJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fGARPJoinTimer.setStatus("current")


class _Xgs360026fGARPLeaveTimer_Type(Integer32):
    """Custom type xgs360026fGARPLeaveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 3000),
    )


_Xgs360026fGARPLeaveTimer_Type.__name__ = "Integer32"
_Xgs360026fGARPLeaveTimer_Object = MibTableColumn
xgs360026fGARPLeaveTimer = _Xgs360026fGARPLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 3, 1, 1, 3),
    _Xgs360026fGARPLeaveTimer_Type()
)
xgs360026fGARPLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fGARPLeaveTimer.setStatus("current")


class _Xgs360026fGARPLeaveAllTimer_Type(Integer32):
    """Custom type xgs360026fGARPLeaveAllTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 50000),
    )


_Xgs360026fGARPLeaveAllTimer_Type.__name__ = "Integer32"
_Xgs360026fGARPLeaveAllTimer_Object = MibTableColumn
xgs360026fGARPLeaveAllTimer = _Xgs360026fGARPLeaveAllTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 3, 1, 1, 4),
    _Xgs360026fGARPLeaveAllTimer_Type()
)
xgs360026fGARPLeaveAllTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fGARPLeaveAllTimer.setStatus("current")


class _Xgs360026fGARPApplicantion_Type(Integer32):
    """Custom type xgs360026fGARPApplicantion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fGARPApplicantion_Type.__name__ = "Integer32"
_Xgs360026fGARPApplicantion_Object = MibTableColumn
xgs360026fGARPApplicantion = _Xgs360026fGARPApplicantion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 3, 1, 1, 5),
    _Xgs360026fGARPApplicantion_Type()
)
xgs360026fGARPApplicantion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fGARPApplicantion.setStatus("current")


class _Xgs360026fGARPAttributeType_Type(Integer32):
    """Custom type xgs360026fGARPAttributeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fGARPAttributeType_Type.__name__ = "Integer32"
_Xgs360026fGARPAttributeType_Object = MibTableColumn
xgs360026fGARPAttributeType = _Xgs360026fGARPAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 3, 1, 1, 6),
    _Xgs360026fGARPAttributeType_Type()
)
xgs360026fGARPAttributeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fGARPAttributeType.setStatus("current")


class _Xgs360026fGARPApplicant_Type(Integer32):
    """Custom type xgs360026fGARPApplicant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fGARPApplicant_Type.__name__ = "Integer32"
_Xgs360026fGARPApplicant_Object = MibTableColumn
xgs360026fGARPApplicant = _Xgs360026fGARPApplicant_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 3, 1, 1, 7),
    _Xgs360026fGARPApplicant_Type()
)
xgs360026fGARPApplicant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fGARPApplicant.setStatus("current")
_Xgs360026fGARPStatisticsTable_Object = MibTable
xgs360026fGARPStatisticsTable = _Xgs360026fGARPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 3, 2)
)
if mibBuilder.loadTexts:
    xgs360026fGARPStatisticsTable.setStatus("current")
_Xgs360026fGARPStatisticsEntry_Object = MibTableRow
xgs360026fGARPStatisticsEntry = _Xgs360026fGARPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 3, 2, 1)
)
xgs360026fGARPStatisticsEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fGARPStatisticsPort"),
)
if mibBuilder.loadTexts:
    xgs360026fGARPStatisticsEntry.setStatus("current")


class _Xgs360026fGARPStatisticsPort_Type(Integer32):
    """Custom type xgs360026fGARPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fGARPStatisticsPort_Type.__name__ = "Integer32"
_Xgs360026fGARPStatisticsPort_Object = MibTableColumn
xgs360026fGARPStatisticsPort = _Xgs360026fGARPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 3, 2, 1, 1),
    _Xgs360026fGARPStatisticsPort_Type()
)
xgs360026fGARPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fGARPStatisticsPort.setStatus("current")
_Xgs360026fGARPStatisticsPeerMAC_Type = DisplayString
_Xgs360026fGARPStatisticsPeerMAC_Object = MibTableColumn
xgs360026fGARPStatisticsPeerMAC = _Xgs360026fGARPStatisticsPeerMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 3, 2, 1, 2),
    _Xgs360026fGARPStatisticsPeerMAC_Type()
)
xgs360026fGARPStatisticsPeerMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fGARPStatisticsPeerMAC.setStatus("current")
_Xgs360026fGARPStatisticsFailedCount_Type = Counter32
_Xgs360026fGARPStatisticsFailedCount_Object = MibTableColumn
xgs360026fGARPStatisticsFailedCount = _Xgs360026fGARPStatisticsFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 3, 2, 1, 3),
    _Xgs360026fGARPStatisticsFailedCount_Type()
)
xgs360026fGARPStatisticsFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fGARPStatisticsFailedCount.setStatus("current")
_Xgs360026fGVRP_ObjectIdentity = ObjectIdentity
xgs360026fGVRP = _Xgs360026fGVRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 4)
)
_Xgs360026fGVRPConf_ObjectIdentity = ObjectIdentity
xgs360026fGVRPConf = _Xgs360026fGVRPConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 4, 1)
)


class _Xgs360026fGVRPMode_Type(Integer32):
    """Custom type xgs360026fGVRPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fGVRPMode_Type.__name__ = "Integer32"
_Xgs360026fGVRPMode_Object = MibScalar
xgs360026fGVRPMode = _Xgs360026fGVRPMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 4, 1, 1),
    _Xgs360026fGVRPMode_Type()
)
xgs360026fGVRPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fGVRPMode.setStatus("current")
_Xgs360026fGVRPConfTable_Object = MibTable
xgs360026fGVRPConfTable = _Xgs360026fGVRPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    xgs360026fGVRPConfTable.setStatus("current")
_Xgs360026fGVRPConfEntry_Object = MibTableRow
xgs360026fGVRPConfEntry = _Xgs360026fGVRPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 4, 1, 2, 1)
)
xgs360026fGVRPConfEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fGVRPConfPort"),
)
if mibBuilder.loadTexts:
    xgs360026fGVRPConfEntry.setStatus("current")


class _Xgs360026fGVRPConfPort_Type(Integer32):
    """Custom type xgs360026fGVRPConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fGVRPConfPort_Type.__name__ = "Integer32"
_Xgs360026fGVRPConfPort_Object = MibTableColumn
xgs360026fGVRPConfPort = _Xgs360026fGVRPConfPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 4, 1, 2, 1, 1),
    _Xgs360026fGVRPConfPort_Type()
)
xgs360026fGVRPConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fGVRPConfPort.setStatus("current")


class _Xgs360026fGVRPConfPortMode_Type(Integer32):
    """Custom type xgs360026fGVRPConfPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fGVRPConfPortMode_Type.__name__ = "Integer32"
_Xgs360026fGVRPConfPortMode_Object = MibTableColumn
xgs360026fGVRPConfPortMode = _Xgs360026fGVRPConfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 4, 1, 2, 1, 2),
    _Xgs360026fGVRPConfPortMode_Type()
)
xgs360026fGVRPConfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fGVRPConfPortMode.setStatus("current")


class _Xgs360026fGVRPConfPortRRole_Type(Integer32):
    """Custom type xgs360026fGVRPConfPortRRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fGVRPConfPortRRole_Type.__name__ = "Integer32"
_Xgs360026fGVRPConfPortRRole_Object = MibTableColumn
xgs360026fGVRPConfPortRRole = _Xgs360026fGVRPConfPortRRole_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 4, 1, 2, 1, 3),
    _Xgs360026fGVRPConfPortRRole_Type()
)
xgs360026fGVRPConfPortRRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fGVRPConfPortRRole.setStatus("current")
_Xgs360026fGVRPStatisticsTable_Object = MibTable
xgs360026fGVRPStatisticsTable = _Xgs360026fGVRPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 4, 2)
)
if mibBuilder.loadTexts:
    xgs360026fGVRPStatisticsTable.setStatus("current")
_Xgs360026fGVRPStatisticsEntry_Object = MibTableRow
xgs360026fGVRPStatisticsEntry = _Xgs360026fGVRPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 4, 2, 1)
)
xgs360026fGVRPStatisticsEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fGVRPStatisticsPort"),
)
if mibBuilder.loadTexts:
    xgs360026fGVRPStatisticsEntry.setStatus("current")


class _Xgs360026fGVRPStatisticsPort_Type(Integer32):
    """Custom type xgs360026fGVRPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fGVRPStatisticsPort_Type.__name__ = "Integer32"
_Xgs360026fGVRPStatisticsPort_Object = MibTableColumn
xgs360026fGVRPStatisticsPort = _Xgs360026fGVRPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 4, 2, 1, 1),
    _Xgs360026fGVRPStatisticsPort_Type()
)
xgs360026fGVRPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fGVRPStatisticsPort.setStatus("current")
_Xgs360026fGVRPStatisticsJoinTxCnt_Type = Counter32
_Xgs360026fGVRPStatisticsJoinTxCnt_Object = MibTableColumn
xgs360026fGVRPStatisticsJoinTxCnt = _Xgs360026fGVRPStatisticsJoinTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 4, 2, 1, 2),
    _Xgs360026fGVRPStatisticsJoinTxCnt_Type()
)
xgs360026fGVRPStatisticsJoinTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fGVRPStatisticsJoinTxCnt.setStatus("current")
_Xgs360026fGVRPStatisticsLeaveTxCnt_Type = Counter32
_Xgs360026fGVRPStatisticsLeaveTxCnt_Object = MibTableColumn
xgs360026fGVRPStatisticsLeaveTxCnt = _Xgs360026fGVRPStatisticsLeaveTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 4, 2, 1, 3),
    _Xgs360026fGVRPStatisticsLeaveTxCnt_Type()
)
xgs360026fGVRPStatisticsLeaveTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fGVRPStatisticsLeaveTxCnt.setStatus("current")
_Xgs360026fThermalProtection_ObjectIdentity = ObjectIdentity
xgs360026fThermalProtection = _Xgs360026fThermalProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 5)
)


class _Xgs360026fPriority0Temperature_Type(Integer32):
    """Custom type xgs360026fPriority0Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xgs360026fPriority0Temperature_Type.__name__ = "Integer32"
_Xgs360026fPriority0Temperature_Object = MibScalar
xgs360026fPriority0Temperature = _Xgs360026fPriority0Temperature_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 5, 1),
    _Xgs360026fPriority0Temperature_Type()
)
xgs360026fPriority0Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPriority0Temperature.setStatus("current")


class _Xgs360026fPriority1Temperature_Type(Integer32):
    """Custom type xgs360026fPriority1Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xgs360026fPriority1Temperature_Type.__name__ = "Integer32"
_Xgs360026fPriority1Temperature_Object = MibScalar
xgs360026fPriority1Temperature = _Xgs360026fPriority1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 5, 2),
    _Xgs360026fPriority1Temperature_Type()
)
xgs360026fPriority1Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPriority1Temperature.setStatus("current")


class _Xgs360026fPriority2Temperature_Type(Integer32):
    """Custom type xgs360026fPriority2Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xgs360026fPriority2Temperature_Type.__name__ = "Integer32"
_Xgs360026fPriority2Temperature_Object = MibScalar
xgs360026fPriority2Temperature = _Xgs360026fPriority2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 5, 3),
    _Xgs360026fPriority2Temperature_Type()
)
xgs360026fPriority2Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPriority2Temperature.setStatus("current")


class _Xgs360026fPriority3Temperature_Type(Integer32):
    """Custom type xgs360026fPriority3Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xgs360026fPriority3Temperature_Type.__name__ = "Integer32"
_Xgs360026fPriority3Temperature_Object = MibScalar
xgs360026fPriority3Temperature = _Xgs360026fPriority3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 5, 4),
    _Xgs360026fPriority3Temperature_Type()
)
xgs360026fPriority3Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPriority3Temperature.setStatus("current")
_Xgs360026fThermalProtectionTable_Object = MibTable
xgs360026fThermalProtectionTable = _Xgs360026fThermalProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 5, 5)
)
if mibBuilder.loadTexts:
    xgs360026fThermalProtectionTable.setStatus("current")
_Xgs360026fThermalProtectionEntry_Object = MibTableRow
xgs360026fThermalProtectionEntry = _Xgs360026fThermalProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 5, 5, 1)
)
xgs360026fThermalProtectionEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fThermalProtectionPort"),
)
if mibBuilder.loadTexts:
    xgs360026fThermalProtectionEntry.setStatus("current")


class _Xgs360026fThermalProtectionPort_Type(Integer32):
    """Custom type xgs360026fThermalProtectionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fThermalProtectionPort_Type.__name__ = "Integer32"
_Xgs360026fThermalProtectionPort_Object = MibTableColumn
xgs360026fThermalProtectionPort = _Xgs360026fThermalProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 5, 5, 1, 1),
    _Xgs360026fThermalProtectionPort_Type()
)
xgs360026fThermalProtectionPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fThermalProtectionPort.setStatus("current")


class _Xgs360026fThermalProtectionPortTemperature_Type(Integer32):
    """Custom type xgs360026fThermalProtectionPortTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xgs360026fThermalProtectionPortTemperature_Type.__name__ = "Integer32"
_Xgs360026fThermalProtectionPortTemperature_Object = MibTableColumn
xgs360026fThermalProtectionPortTemperature = _Xgs360026fThermalProtectionPortTemperature_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 5, 5, 1, 2),
    _Xgs360026fThermalProtectionPortTemperature_Type()
)
xgs360026fThermalProtectionPortTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fThermalProtectionPortTemperature.setStatus("current")


class _Xgs360026fThermalProtectionPortPriority_Type(Integer32):
    """Custom type xgs360026fThermalProtectionPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Xgs360026fThermalProtectionPortPriority_Type.__name__ = "Integer32"
_Xgs360026fThermalProtectionPortPriority_Object = MibTableColumn
xgs360026fThermalProtectionPortPriority = _Xgs360026fThermalProtectionPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 5, 5, 1, 3),
    _Xgs360026fThermalProtectionPortPriority_Type()
)
xgs360026fThermalProtectionPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fThermalProtectionPortPriority.setStatus("current")
_Xgs360026fThermalProtectionPortStatus_Type = DisplayString
_Xgs360026fThermalProtectionPortStatus_Object = MibTableColumn
xgs360026fThermalProtectionPortStatus = _Xgs360026fThermalProtectionPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 5, 5, 1, 4),
    _Xgs360026fThermalProtectionPortStatus_Type()
)
xgs360026fThermalProtectionPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fThermalProtectionPortStatus.setStatus("current")
_Xgs360026fMirroring_ObjectIdentity = ObjectIdentity
xgs360026fMirroring = _Xgs360026fMirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 6)
)


class _Xgs360026fPortToMirrorOn_Type(Integer32):
    """Custom type xgs360026fPortToMirrorOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Xgs360026fPortToMirrorOn_Type.__name__ = "Integer32"
_Xgs360026fPortToMirrorOn_Object = MibScalar
xgs360026fPortToMirrorOn = _Xgs360026fPortToMirrorOn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 6, 1),
    _Xgs360026fPortToMirrorOn_Type()
)
xgs360026fPortToMirrorOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPortToMirrorOn.setStatus("current")
_Xgs360026fMirrorTable_Object = MibTable
xgs360026fMirrorTable = _Xgs360026fMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 6, 2)
)
if mibBuilder.loadTexts:
    xgs360026fMirrorTable.setStatus("current")
_Xgs360026fMirrorEntry_Object = MibTableRow
xgs360026fMirrorEntry = _Xgs360026fMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 6, 2, 1)
)
xgs360026fMirrorEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fMirrorPort"),
)
if mibBuilder.loadTexts:
    xgs360026fMirrorEntry.setStatus("current")


class _Xgs360026fMirrorPort_Type(Integer32):
    """Custom type xgs360026fMirrorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fMirrorPort_Type.__name__ = "Integer32"
_Xgs360026fMirrorPort_Object = MibTableColumn
xgs360026fMirrorPort = _Xgs360026fMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 6, 2, 1, 1),
    _Xgs360026fMirrorPort_Type()
)
xgs360026fMirrorPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fMirrorPort.setStatus("current")


class _Xgs360026fMirrorMode_Type(Integer32):
    """Custom type xgs360026fMirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Xgs360026fMirrorMode_Type.__name__ = "Integer32"
_Xgs360026fMirrorMode_Object = MibTableColumn
xgs360026fMirrorMode = _Xgs360026fMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 6, 2, 1, 2),
    _Xgs360026fMirrorMode_Type()
)
xgs360026fMirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMirrorMode.setStatus("current")
_Xgs360026fTrapEventSeverity_ObjectIdentity = ObjectIdentity
xgs360026fTrapEventSeverity = _Xgs360026fTrapEventSeverity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7)
)


class _Xgs360026fTrapEventSeverityACL_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityACL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityACL_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityACL_Object = MibScalar
xgs360026fTrapEventSeverityACL = _Xgs360026fTrapEventSeverityACL_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 1),
    _Xgs360026fTrapEventSeverityACL_Type()
)
xgs360026fTrapEventSeverityACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityACL.setStatus("current")


class _Xgs360026fTrapEventSeverityACLLog_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityACLLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityACLLog_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityACLLog_Object = MibScalar
xgs360026fTrapEventSeverityACLLog = _Xgs360026fTrapEventSeverityACLLog_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 2),
    _Xgs360026fTrapEventSeverityACLLog_Type()
)
xgs360026fTrapEventSeverityACLLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityACLLog.setStatus("current")


class _Xgs360026fTrapEventSeverityAccessMgmt_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityAccessMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityAccessMgmt_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityAccessMgmt_Object = MibScalar
xgs360026fTrapEventSeverityAccessMgmt = _Xgs360026fTrapEventSeverityAccessMgmt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 3),
    _Xgs360026fTrapEventSeverityAccessMgmt_Type()
)
xgs360026fTrapEventSeverityAccessMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityAccessMgmt.setStatus("current")


class _Xgs360026fTrapEventSeverityAuthFailed_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityAuthFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityAuthFailed_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityAuthFailed_Object = MibScalar
xgs360026fTrapEventSeverityAuthFailed = _Xgs360026fTrapEventSeverityAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 4),
    _Xgs360026fTrapEventSeverityAuthFailed_Type()
)
xgs360026fTrapEventSeverityAuthFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityAuthFailed.setStatus("current")


class _Xgs360026fTrapEventSeverityColdStart_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityColdStart_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityColdStart_Object = MibScalar
xgs360026fTrapEventSeverityColdStart = _Xgs360026fTrapEventSeverityColdStart_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 5),
    _Xgs360026fTrapEventSeverityColdStart_Type()
)
xgs360026fTrapEventSeverityColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityColdStart.setStatus("current")


class _Xgs360026fTrapEventSeverityConfigInfo_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityConfigInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityConfigInfo_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityConfigInfo_Object = MibScalar
xgs360026fTrapEventSeverityConfigInfo = _Xgs360026fTrapEventSeverityConfigInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 6),
    _Xgs360026fTrapEventSeverityConfigInfo_Type()
)
xgs360026fTrapEventSeverityConfigInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityConfigInfo.setStatus("current")


class _Xgs360026fTrapEventSeverityFirmwareUpgrade_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityFirmwareUpgrade_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityFirmwareUpgrade_Object = MibScalar
xgs360026fTrapEventSeverityFirmwareUpgrade = _Xgs360026fTrapEventSeverityFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 7),
    _Xgs360026fTrapEventSeverityFirmwareUpgrade_Type()
)
xgs360026fTrapEventSeverityFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityFirmwareUpgrade.setStatus("current")


class _Xgs360026fTrapEventSeverityImportExport_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityImportExport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityImportExport_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityImportExport_Object = MibScalar
xgs360026fTrapEventSeverityImportExport = _Xgs360026fTrapEventSeverityImportExport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 8),
    _Xgs360026fTrapEventSeverityImportExport_Type()
)
xgs360026fTrapEventSeverityImportExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityImportExport.setStatus("current")


class _Xgs360026fTrapEventSeverityLACP_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityLACP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityLACP_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityLACP_Object = MibScalar
xgs360026fTrapEventSeverityLACP = _Xgs360026fTrapEventSeverityLACP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 9),
    _Xgs360026fTrapEventSeverityLACP_Type()
)
xgs360026fTrapEventSeverityLACP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityLACP.setStatus("current")


class _Xgs360026fTrapEventSeverityLinkStatus_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityLinkStatus_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityLinkStatus_Object = MibScalar
xgs360026fTrapEventSeverityLinkStatus = _Xgs360026fTrapEventSeverityLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 10),
    _Xgs360026fTrapEventSeverityLinkStatus_Type()
)
xgs360026fTrapEventSeverityLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityLinkStatus.setStatus("current")


class _Xgs360026fTrapEventSeverityLogin_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityLogin_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityLogin_Object = MibScalar
xgs360026fTrapEventSeverityLogin = _Xgs360026fTrapEventSeverityLogin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 11),
    _Xgs360026fTrapEventSeverityLogin_Type()
)
xgs360026fTrapEventSeverityLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityLogin.setStatus("current")


class _Xgs360026fTrapEventSeverityLogout_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityLogout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityLogout_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityLogout_Object = MibScalar
xgs360026fTrapEventSeverityLogout = _Xgs360026fTrapEventSeverityLogout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 12),
    _Xgs360026fTrapEventSeverityLogout_Type()
)
xgs360026fTrapEventSeverityLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityLogout.setStatus("current")


class _Xgs360026fTrapEventSeverityLoopProtect_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityLoopProtect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityLoopProtect_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityLoopProtect_Object = MibScalar
xgs360026fTrapEventSeverityLoopProtect = _Xgs360026fTrapEventSeverityLoopProtect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 13),
    _Xgs360026fTrapEventSeverityLoopProtect_Type()
)
xgs360026fTrapEventSeverityLoopProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityLoopProtect.setStatus("current")


class _Xgs360026fTrapEventSeverityMgmtIPChange_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityMgmtIPChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityMgmtIPChange_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityMgmtIPChange_Object = MibScalar
xgs360026fTrapEventSeverityMgmtIPChange = _Xgs360026fTrapEventSeverityMgmtIPChange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 14),
    _Xgs360026fTrapEventSeverityMgmtIPChange_Type()
)
xgs360026fTrapEventSeverityMgmtIPChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityMgmtIPChange.setStatus("current")


class _Xgs360026fTrapEventSeverityModuleChange_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityModuleChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityModuleChange_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityModuleChange_Object = MibScalar
xgs360026fTrapEventSeverityModuleChange = _Xgs360026fTrapEventSeverityModuleChange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 15),
    _Xgs360026fTrapEventSeverityModuleChange_Type()
)
xgs360026fTrapEventSeverityModuleChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityModuleChange.setStatus("current")


class _Xgs360026fTrapEventSeverityNAS_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityNAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityNAS_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityNAS_Object = MibScalar
xgs360026fTrapEventSeverityNAS = _Xgs360026fTrapEventSeverityNAS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 16),
    _Xgs360026fTrapEventSeverityNAS_Type()
)
xgs360026fTrapEventSeverityNAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityNAS.setStatus("current")


class _Xgs360026fTrapEventSeverityPasswdChange_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityPasswdChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityPasswdChange_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityPasswdChange_Object = MibScalar
xgs360026fTrapEventSeverityPasswdChange = _Xgs360026fTrapEventSeverityPasswdChange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 17),
    _Xgs360026fTrapEventSeverityPasswdChange_Type()
)
xgs360026fTrapEventSeverityPasswdChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityPasswdChange.setStatus("current")


class _Xgs360026fTrapEventSeverityPortSecurity_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityPortSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityPortSecurity_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityPortSecurity_Object = MibScalar
xgs360026fTrapEventSeverityPortSecurity = _Xgs360026fTrapEventSeverityPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 18),
    _Xgs360026fTrapEventSeverityPortSecurity_Type()
)
xgs360026fTrapEventSeverityPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityPortSecurity.setStatus("current")


class _Xgs360026fTrapEventSeverityThermalProtect_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityThermalProtect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityThermalProtect_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityThermalProtect_Object = MibScalar
xgs360026fTrapEventSeverityThermalProtect = _Xgs360026fTrapEventSeverityThermalProtect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 19),
    _Xgs360026fTrapEventSeverityThermalProtect_Type()
)
xgs360026fTrapEventSeverityThermalProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityThermalProtect.setStatus("current")


class _Xgs360026fTrapEventSeverityVLAN_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityVLAN_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityVLAN_Object = MibScalar
xgs360026fTrapEventSeverityVLAN = _Xgs360026fTrapEventSeverityVLAN_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 20),
    _Xgs360026fTrapEventSeverityVLAN_Type()
)
xgs360026fTrapEventSeverityVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityVLAN.setStatus("current")


class _Xgs360026fTrapEventSeverityWarmStart_Type(Integer32):
    """Custom type xgs360026fTrapEventSeverityWarmStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fTrapEventSeverityWarmStart_Type.__name__ = "Integer32"
_Xgs360026fTrapEventSeverityWarmStart_Object = MibScalar
xgs360026fTrapEventSeverityWarmStart = _Xgs360026fTrapEventSeverityWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 7, 21),
    _Xgs360026fTrapEventSeverityWarmStart_Type()
)
xgs360026fTrapEventSeverityWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTrapEventSeverityWarmStart.setStatus("current")
_Xgs360026fSMTP_ObjectIdentity = ObjectIdentity
xgs360026fSMTP = _Xgs360026fSMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 8)
)
_Xgs360026fSMTPMailServer_Type = DisplayString
_Xgs360026fSMTPMailServer_Object = MibScalar
xgs360026fSMTPMailServer = _Xgs360026fSMTPMailServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 8, 1),
    _Xgs360026fSMTPMailServer_Type()
)
xgs360026fSMTPMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSMTPMailServer.setStatus("current")
_Xgs360026fSMTPUserName_Type = DisplayString
_Xgs360026fSMTPUserName_Object = MibScalar
xgs360026fSMTPUserName = _Xgs360026fSMTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 8, 2),
    _Xgs360026fSMTPUserName_Type()
)
xgs360026fSMTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSMTPUserName.setStatus("current")
_Xgs360026fSMTPPassword_Type = DisplayString
_Xgs360026fSMTPPassword_Object = MibScalar
xgs360026fSMTPPassword = _Xgs360026fSMTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 8, 3),
    _Xgs360026fSMTPPassword_Type()
)
xgs360026fSMTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSMTPPassword.setStatus("current")


class _Xgs360026fSMTPServeriryLevel_Type(Integer32):
    """Custom type xgs360026fSMTPServeriryLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xgs360026fSMTPServeriryLevel_Type.__name__ = "Integer32"
_Xgs360026fSMTPServeriryLevel_Object = MibScalar
xgs360026fSMTPServeriryLevel = _Xgs360026fSMTPServeriryLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 8, 4),
    _Xgs360026fSMTPServeriryLevel_Type()
)
xgs360026fSMTPServeriryLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSMTPServeriryLevel.setStatus("current")
_Xgs360026fSMTPSender_Type = DisplayString
_Xgs360026fSMTPSender_Object = MibScalar
xgs360026fSMTPSender = _Xgs360026fSMTPSender_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 8, 5),
    _Xgs360026fSMTPSender_Type()
)
xgs360026fSMTPSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSMTPSender.setStatus("current")
_Xgs360026fSMTPReturnPath_Type = DisplayString
_Xgs360026fSMTPReturnPath_Object = MibScalar
xgs360026fSMTPReturnPath = _Xgs360026fSMTPReturnPath_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 8, 6),
    _Xgs360026fSMTPReturnPath_Type()
)
xgs360026fSMTPReturnPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSMTPReturnPath.setStatus("current")
_Xgs360026fSMTPEmailAddress1_Type = DisplayString
_Xgs360026fSMTPEmailAddress1_Object = MibScalar
xgs360026fSMTPEmailAddress1 = _Xgs360026fSMTPEmailAddress1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 8, 7),
    _Xgs360026fSMTPEmailAddress1_Type()
)
xgs360026fSMTPEmailAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSMTPEmailAddress1.setStatus("current")
_Xgs360026fSMTPEmailAddress2_Type = DisplayString
_Xgs360026fSMTPEmailAddress2_Object = MibScalar
xgs360026fSMTPEmailAddress2 = _Xgs360026fSMTPEmailAddress2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 8, 8),
    _Xgs360026fSMTPEmailAddress2_Type()
)
xgs360026fSMTPEmailAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSMTPEmailAddress2.setStatus("current")
_Xgs360026fSMTPEmailAddress3_Type = DisplayString
_Xgs360026fSMTPEmailAddress3_Object = MibScalar
xgs360026fSMTPEmailAddress3 = _Xgs360026fSMTPEmailAddress3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 8, 9),
    _Xgs360026fSMTPEmailAddress3_Type()
)
xgs360026fSMTPEmailAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSMTPEmailAddress3.setStatus("current")
_Xgs360026fSMTPEmailAddress4_Type = DisplayString
_Xgs360026fSMTPEmailAddress4_Object = MibScalar
xgs360026fSMTPEmailAddress4 = _Xgs360026fSMTPEmailAddress4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 8, 10),
    _Xgs360026fSMTPEmailAddress4_Type()
)
xgs360026fSMTPEmailAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSMTPEmailAddress4.setStatus("current")
_Xgs360026fSMTPEmailAddress5_Type = DisplayString
_Xgs360026fSMTPEmailAddress5_Object = MibScalar
xgs360026fSMTPEmailAddress5 = _Xgs360026fSMTPEmailAddress5_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 8, 11),
    _Xgs360026fSMTPEmailAddress5_Type()
)
xgs360026fSMTPEmailAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSMTPEmailAddress5.setStatus("current")
_Xgs360026fSMTPEmailAddress6_Type = DisplayString
_Xgs360026fSMTPEmailAddress6_Object = MibScalar
xgs360026fSMTPEmailAddress6 = _Xgs360026fSMTPEmailAddress6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 8, 12),
    _Xgs360026fSMTPEmailAddress6_Type()
)
xgs360026fSMTPEmailAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSMTPEmailAddress6.setStatus("current")
_Xgs360026fACL_ObjectIdentity = ObjectIdentity
xgs360026fACL = _Xgs360026fACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9)
)
_Xgs360026fACLPortsConfTable_Object = MibTable
xgs360026fACLPortsConfTable = _Xgs360026fACLPortsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 1)
)
if mibBuilder.loadTexts:
    xgs360026fACLPortsConfTable.setStatus("current")
_Xgs360026fACLPortsConfEntry_Object = MibTableRow
xgs360026fACLPortsConfEntry = _Xgs360026fACLPortsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 1, 1)
)
xgs360026fACLPortsConfEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fACLPortsConfPort"),
)
if mibBuilder.loadTexts:
    xgs360026fACLPortsConfEntry.setStatus("current")


class _Xgs360026fACLPortsConfPort_Type(Integer32):
    """Custom type xgs360026fACLPortsConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fACLPortsConfPort_Type.__name__ = "Integer32"
_Xgs360026fACLPortsConfPort_Object = MibTableColumn
xgs360026fACLPortsConfPort = _Xgs360026fACLPortsConfPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 1, 1, 1),
    _Xgs360026fACLPortsConfPort_Type()
)
xgs360026fACLPortsConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fACLPortsConfPort.setStatus("current")


class _Xgs360026fACLPortsConfPolicyID_Type(Integer32):
    """Custom type xgs360026fACLPortsConfPolicyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xgs360026fACLPortsConfPolicyID_Type.__name__ = "Integer32"
_Xgs360026fACLPortsConfPolicyID_Object = MibTableColumn
xgs360026fACLPortsConfPolicyID = _Xgs360026fACLPortsConfPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 1, 1, 2),
    _Xgs360026fACLPortsConfPolicyID_Type()
)
xgs360026fACLPortsConfPolicyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLPortsConfPolicyID.setStatus("current")


class _Xgs360026fACLPortsConfAction_Type(Integer32):
    """Custom type xgs360026fACLPortsConfAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fACLPortsConfAction_Type.__name__ = "Integer32"
_Xgs360026fACLPortsConfAction_Object = MibTableColumn
xgs360026fACLPortsConfAction = _Xgs360026fACLPortsConfAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 1, 1, 3),
    _Xgs360026fACLPortsConfAction_Type()
)
xgs360026fACLPortsConfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLPortsConfAction.setStatus("current")


class _Xgs360026fACLPortsConfRateLimiterID_Type(Integer32):
    """Custom type xgs360026fACLPortsConfRateLimiterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Xgs360026fACLPortsConfRateLimiterID_Type.__name__ = "Integer32"
_Xgs360026fACLPortsConfRateLimiterID_Object = MibTableColumn
xgs360026fACLPortsConfRateLimiterID = _Xgs360026fACLPortsConfRateLimiterID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 1, 1, 4),
    _Xgs360026fACLPortsConfRateLimiterID_Type()
)
xgs360026fACLPortsConfRateLimiterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLPortsConfRateLimiterID.setStatus("current")


class _Xgs360026fACLPortsConfPortRedirect_Type(Integer32):
    """Custom type xgs360026fACLPortsConfPortRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Xgs360026fACLPortsConfPortRedirect_Type.__name__ = "Integer32"
_Xgs360026fACLPortsConfPortRedirect_Object = MibTableColumn
xgs360026fACLPortsConfPortRedirect = _Xgs360026fACLPortsConfPortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 1, 1, 5),
    _Xgs360026fACLPortsConfPortRedirect_Type()
)
xgs360026fACLPortsConfPortRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLPortsConfPortRedirect.setStatus("current")


class _Xgs360026fACLPortsConfLogging_Type(Integer32):
    """Custom type xgs360026fACLPortsConfLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fACLPortsConfLogging_Type.__name__ = "Integer32"
_Xgs360026fACLPortsConfLogging_Object = MibTableColumn
xgs360026fACLPortsConfLogging = _Xgs360026fACLPortsConfLogging_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 1, 1, 7),
    _Xgs360026fACLPortsConfLogging_Type()
)
xgs360026fACLPortsConfLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLPortsConfLogging.setStatus("current")


class _Xgs360026fACLPortsConfShutdown_Type(Integer32):
    """Custom type xgs360026fACLPortsConfShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fACLPortsConfShutdown_Type.__name__ = "Integer32"
_Xgs360026fACLPortsConfShutdown_Object = MibTableColumn
xgs360026fACLPortsConfShutdown = _Xgs360026fACLPortsConfShutdown_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 1, 1, 8),
    _Xgs360026fACLPortsConfShutdown_Type()
)
xgs360026fACLPortsConfShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLPortsConfShutdown.setStatus("current")


class _Xgs360026fACLPortsConfState_Type(Integer32):
    """Custom type xgs360026fACLPortsConfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fACLPortsConfState_Type.__name__ = "Integer32"
_Xgs360026fACLPortsConfState_Object = MibTableColumn
xgs360026fACLPortsConfState = _Xgs360026fACLPortsConfState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 1, 1, 9),
    _Xgs360026fACLPortsConfState_Type()
)
xgs360026fACLPortsConfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLPortsConfState.setStatus("current")
_Xgs360026fACLPortsConfCounter_Type = Counter32
_Xgs360026fACLPortsConfCounter_Object = MibTableColumn
xgs360026fACLPortsConfCounter = _Xgs360026fACLPortsConfCounter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 1, 1, 10),
    _Xgs360026fACLPortsConfCounter_Type()
)
xgs360026fACLPortsConfCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fACLPortsConfCounter.setStatus("current")
_Xgs360026fACLRateLimiterTable_Object = MibTable
xgs360026fACLRateLimiterTable = _Xgs360026fACLRateLimiterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 2)
)
if mibBuilder.loadTexts:
    xgs360026fACLRateLimiterTable.setStatus("current")
_Xgs360026fACLRateLimiterEntry_Object = MibTableRow
xgs360026fACLRateLimiterEntry = _Xgs360026fACLRateLimiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 2, 1)
)
xgs360026fACLRateLimiterEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fACLRateLimiterID"),
)
if mibBuilder.loadTexts:
    xgs360026fACLRateLimiterEntry.setStatus("current")


class _Xgs360026fACLRateLimiterID_Type(Integer32):
    """Custom type xgs360026fACLRateLimiterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Xgs360026fACLRateLimiterID_Type.__name__ = "Integer32"
_Xgs360026fACLRateLimiterID_Object = MibTableColumn
xgs360026fACLRateLimiterID = _Xgs360026fACLRateLimiterID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 2, 1, 1),
    _Xgs360026fACLRateLimiterID_Type()
)
xgs360026fACLRateLimiterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fACLRateLimiterID.setStatus("current")


class _Xgs360026fACLRateLimiterRate_Type(Integer32):
    """Custom type xgs360026fACLRateLimiterRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3276700),
    )


_Xgs360026fACLRateLimiterRate_Type.__name__ = "Integer32"
_Xgs360026fACLRateLimiterRate_Object = MibTableColumn
xgs360026fACLRateLimiterRate = _Xgs360026fACLRateLimiterRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 2, 1, 3),
    _Xgs360026fACLRateLimiterRate_Type()
)
xgs360026fACLRateLimiterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLRateLimiterRate.setStatus("current")
_Xgs360026fACLACE_ObjectIdentity = ObjectIdentity
xgs360026fACLACE = _Xgs360026fACLACE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3)
)


class _Xgs360026fACLACECreate_Type(Integer32):
    """Custom type xgs360026fACLACECreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fACLACECreate_Type.__name__ = "Integer32"
_Xgs360026fACLACECreate_Object = MibScalar
xgs360026fACLACECreate = _Xgs360026fACLACECreate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 1),
    _Xgs360026fACLACECreate_Type()
)
xgs360026fACLACECreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACECreate.setStatus("current")
_Xgs360026fACLACETable_Object = MibTable
xgs360026fACLACETable = _Xgs360026fACLACETable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2)
)
if mibBuilder.loadTexts:
    xgs360026fACLACETable.setStatus("current")
_Xgs360026fACLACEEntry_Object = MibTableRow
xgs360026fACLACEEntry = _Xgs360026fACLACEEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1)
)
xgs360026fACLACEEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fACLACEIndex"),
)
if mibBuilder.loadTexts:
    xgs360026fACLACEEntry.setStatus("current")


class _Xgs360026fACLACEIndex_Type(Integer32):
    """Custom type xgs360026fACLACEIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Xgs360026fACLACEIndex_Type.__name__ = "Integer32"
_Xgs360026fACLACEIndex_Object = MibTableColumn
xgs360026fACLACEIndex = _Xgs360026fACLACEIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 1),
    _Xgs360026fACLACEIndex_Type()
)
xgs360026fACLACEIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fACLACEIndex.setStatus("current")


class _Xgs360026fACLACEID_Type(Integer32):
    """Custom type xgs360026fACLACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Xgs360026fACLACEID_Type.__name__ = "Integer32"
_Xgs360026fACLACEID_Object = MibTableColumn
xgs360026fACLACEID = _Xgs360026fACLACEID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 2),
    _Xgs360026fACLACEID_Type()
)
xgs360026fACLACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEID.setStatus("current")


class _Xgs360026fACLACENextID_Type(Integer32):
    """Custom type xgs360026fACLACENextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Xgs360026fACLACENextID_Type.__name__ = "Integer32"
_Xgs360026fACLACENextID_Object = MibTableColumn
xgs360026fACLACENextID = _Xgs360026fACLACENextID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 3),
    _Xgs360026fACLACENextID_Type()
)
xgs360026fACLACENextID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACENextID.setStatus("current")
_Xgs360026fACLACEIngressPort_Type = DisplayString
_Xgs360026fACLACEIngressPort_Object = MibTableColumn
xgs360026fACLACEIngressPort = _Xgs360026fACLACEIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 4),
    _Xgs360026fACLACEIngressPort_Type()
)
xgs360026fACLACEIngressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEIngressPort.setStatus("current")


class _Xgs360026fACLACEPortPolicyNumber_Type(Integer32):
    """Custom type xgs360026fACLACEPortPolicyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xgs360026fACLACEPortPolicyNumber_Type.__name__ = "Integer32"
_Xgs360026fACLACEPortPolicyNumber_Object = MibTableColumn
xgs360026fACLACEPortPolicyNumber = _Xgs360026fACLACEPortPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 5),
    _Xgs360026fACLACEPortPolicyNumber_Type()
)
xgs360026fACLACEPortPolicyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEPortPolicyNumber.setStatus("current")


class _Xgs360026fACLACEPortPolicyBitmask_Type(Integer32):
    """Custom type xgs360026fACLACEPortPolicyBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xgs360026fACLACEPortPolicyBitmask_Type.__name__ = "Integer32"
_Xgs360026fACLACEPortPolicyBitmask_Object = MibTableColumn
xgs360026fACLACEPortPolicyBitmask = _Xgs360026fACLACEPortPolicyBitmask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 6),
    _Xgs360026fACLACEPortPolicyBitmask_Type()
)
xgs360026fACLACEPortPolicyBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEPortPolicyBitmask.setStatus("current")


class _Xgs360026fACLACEFrameType_Type(Integer32):
    """Custom type xgs360026fACLACEFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Xgs360026fACLACEFrameType_Type.__name__ = "Integer32"
_Xgs360026fACLACEFrameType_Object = MibTableColumn
xgs360026fACLACEFrameType = _Xgs360026fACLACEFrameType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 7),
    _Xgs360026fACLACEFrameType_Type()
)
xgs360026fACLACEFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEFrameType.setStatus("current")


class _Xgs360026fACLACEAction_Type(Integer32):
    """Custom type xgs360026fACLACEAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fACLACEAction_Type.__name__ = "Integer32"
_Xgs360026fACLACEAction_Object = MibTableColumn
xgs360026fACLACEAction = _Xgs360026fACLACEAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 8),
    _Xgs360026fACLACEAction_Type()
)
xgs360026fACLACEAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEAction.setStatus("current")
_Xgs360026fACLACEDenyPortRedirect_Type = DisplayString
_Xgs360026fACLACEDenyPortRedirect_Object = MibTableColumn
xgs360026fACLACEDenyPortRedirect = _Xgs360026fACLACEDenyPortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 9),
    _Xgs360026fACLACEDenyPortRedirect_Type()
)
xgs360026fACLACEDenyPortRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEDenyPortRedirect.setStatus("current")


class _Xgs360026fACLACELogging_Type(Integer32):
    """Custom type xgs360026fACLACELogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fACLACELogging_Type.__name__ = "Integer32"
_Xgs360026fACLACELogging_Object = MibTableColumn
xgs360026fACLACELogging = _Xgs360026fACLACELogging_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 10),
    _Xgs360026fACLACELogging_Type()
)
xgs360026fACLACELogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACELogging.setStatus("current")


class _Xgs360026fACLACERateLimiter_Type(Integer32):
    """Custom type xgs360026fACLACERateLimiter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Xgs360026fACLACERateLimiter_Type.__name__ = "Integer32"
_Xgs360026fACLACERateLimiter_Object = MibTableColumn
xgs360026fACLACERateLimiter = _Xgs360026fACLACERateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 12),
    _Xgs360026fACLACERateLimiter_Type()
)
xgs360026fACLACERateLimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACERateLimiter.setStatus("current")


class _Xgs360026fACLACEShutdown_Type(Integer32):
    """Custom type xgs360026fACLACEShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fACLACEShutdown_Type.__name__ = "Integer32"
_Xgs360026fACLACEShutdown_Object = MibTableColumn
xgs360026fACLACEShutdown = _Xgs360026fACLACEShutdown_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 13),
    _Xgs360026fACLACEShutdown_Type()
)
xgs360026fACLACEShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEShutdown.setStatus("current")


class _Xgs360026fACLACEVLANTagPriority_Type(Integer32):
    """Custom type xgs360026fACLACEVLANTagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Xgs360026fACLACEVLANTagPriority_Type.__name__ = "Integer32"
_Xgs360026fACLACEVLANTagPriority_Object = MibTableColumn
xgs360026fACLACEVLANTagPriority = _Xgs360026fACLACEVLANTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 15),
    _Xgs360026fACLACEVLANTagPriority_Type()
)
xgs360026fACLACEVLANTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEVLANTagPriority.setStatus("current")


class _Xgs360026fACLACEVLANVID_Type(Integer32):
    """Custom type xgs360026fACLACEVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Xgs360026fACLACEVLANVID_Type.__name__ = "Integer32"
_Xgs360026fACLACEVLANVID_Object = MibTableColumn
xgs360026fACLACEVLANVID = _Xgs360026fACLACEVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 16),
    _Xgs360026fACLACEVLANVID_Type()
)
xgs360026fACLACEVLANVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEVLANVID.setStatus("current")


class _Xgs360026fACLACEEtherType_Type(Integer32):
    """Custom type xgs360026fACLACEEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Xgs360026fACLACEEtherType_Type.__name__ = "Integer32"
_Xgs360026fACLACEEtherType_Object = MibTableColumn
xgs360026fACLACEEtherType = _Xgs360026fACLACEEtherType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 17),
    _Xgs360026fACLACEEtherType_Type()
)
xgs360026fACLACEEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEEtherType.setStatus("current")
_Xgs360026fACLACESMAC_Type = DisplayString
_Xgs360026fACLACESMAC_Object = MibTableColumn
xgs360026fACLACESMAC = _Xgs360026fACLACESMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 18),
    _Xgs360026fACLACESMAC_Type()
)
xgs360026fACLACESMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACESMAC.setStatus("current")


class _Xgs360026fACLACEDMACType_Type(Integer32):
    """Custom type xgs360026fACLACEDMACType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Xgs360026fACLACEDMACType_Type.__name__ = "Integer32"
_Xgs360026fACLACEDMACType_Object = MibTableColumn
xgs360026fACLACEDMACType = _Xgs360026fACLACEDMACType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 19),
    _Xgs360026fACLACEDMACType_Type()
)
xgs360026fACLACEDMACType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEDMACType.setStatus("current")
_Xgs360026fACLACEDMAC_Type = DisplayString
_Xgs360026fACLACEDMAC_Object = MibTableColumn
xgs360026fACLACEDMAC = _Xgs360026fACLACEDMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 20),
    _Xgs360026fACLACEDMAC_Type()
)
xgs360026fACLACEDMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEDMAC.setStatus("current")


class _Xgs360026fACLACEArpOpcode_Type(Integer32):
    """Custom type xgs360026fACLACEArpOpcode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Xgs360026fACLACEArpOpcode_Type.__name__ = "Integer32"
_Xgs360026fACLACEArpOpcode_Object = MibTableColumn
xgs360026fACLACEArpOpcode = _Xgs360026fACLACEArpOpcode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 21),
    _Xgs360026fACLACEArpOpcode_Type()
)
xgs360026fACLACEArpOpcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEArpOpcode.setStatus("current")


class _Xgs360026fACLACEArpFlagsRequestReply_Type(Integer32):
    """Custom type xgs360026fACLACEArpFlagsRequestReply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Xgs360026fACLACEArpFlagsRequestReply_Type.__name__ = "Integer32"
_Xgs360026fACLACEArpFlagsRequestReply_Object = MibTableColumn
xgs360026fACLACEArpFlagsRequestReply = _Xgs360026fACLACEArpFlagsRequestReply_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 22),
    _Xgs360026fACLACEArpFlagsRequestReply_Type()
)
xgs360026fACLACEArpFlagsRequestReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEArpFlagsRequestReply.setStatus("current")


class _Xgs360026fACLACEArpFlagsArpSmac_Type(Integer32):
    """Custom type xgs360026fACLACEArpFlagsArpSmac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Xgs360026fACLACEArpFlagsArpSmac_Type.__name__ = "Integer32"
_Xgs360026fACLACEArpFlagsArpSmac_Object = MibTableColumn
xgs360026fACLACEArpFlagsArpSmac = _Xgs360026fACLACEArpFlagsArpSmac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 23),
    _Xgs360026fACLACEArpFlagsArpSmac_Type()
)
xgs360026fACLACEArpFlagsArpSmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEArpFlagsArpSmac.setStatus("current")


class _Xgs360026fACLACEArpFlagsRarpDmac_Type(Integer32):
    """Custom type xgs360026fACLACEArpFlagsRarpDmac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Xgs360026fACLACEArpFlagsRarpDmac_Type.__name__ = "Integer32"
_Xgs360026fACLACEArpFlagsRarpDmac_Object = MibTableColumn
xgs360026fACLACEArpFlagsRarpDmac = _Xgs360026fACLACEArpFlagsRarpDmac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 24),
    _Xgs360026fACLACEArpFlagsRarpDmac_Type()
)
xgs360026fACLACEArpFlagsRarpDmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEArpFlagsRarpDmac.setStatus("current")


class _Xgs360026fACLACEArpFlagsLength_Type(Integer32):
    """Custom type xgs360026fACLACEArpFlagsLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Xgs360026fACLACEArpFlagsLength_Type.__name__ = "Integer32"
_Xgs360026fACLACEArpFlagsLength_Object = MibTableColumn
xgs360026fACLACEArpFlagsLength = _Xgs360026fACLACEArpFlagsLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 25),
    _Xgs360026fACLACEArpFlagsLength_Type()
)
xgs360026fACLACEArpFlagsLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEArpFlagsLength.setStatus("current")


class _Xgs360026fACLACEArpFlagsIp_Type(Integer32):
    """Custom type xgs360026fACLACEArpFlagsIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Xgs360026fACLACEArpFlagsIp_Type.__name__ = "Integer32"
_Xgs360026fACLACEArpFlagsIp_Object = MibTableColumn
xgs360026fACLACEArpFlagsIp = _Xgs360026fACLACEArpFlagsIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 26),
    _Xgs360026fACLACEArpFlagsIp_Type()
)
xgs360026fACLACEArpFlagsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEArpFlagsIp.setStatus("current")


class _Xgs360026fACLACEArpFlagsEthernet_Type(Integer32):
    """Custom type xgs360026fACLACEArpFlagsEthernet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Xgs360026fACLACEArpFlagsEthernet_Type.__name__ = "Integer32"
_Xgs360026fACLACEArpFlagsEthernet_Object = MibTableColumn
xgs360026fACLACEArpFlagsEthernet = _Xgs360026fACLACEArpFlagsEthernet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 27),
    _Xgs360026fACLACEArpFlagsEthernet_Type()
)
xgs360026fACLACEArpFlagsEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEArpFlagsEthernet.setStatus("current")


class _Xgs360026fACLACESIPType_Type(Integer32):
    """Custom type xgs360026fACLACESIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fACLACESIPType_Type.__name__ = "Integer32"
_Xgs360026fACLACESIPType_Object = MibTableColumn
xgs360026fACLACESIPType = _Xgs360026fACLACESIPType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 28),
    _Xgs360026fACLACESIPType_Type()
)
xgs360026fACLACESIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACESIPType.setStatus("current")
_Xgs360026fACLACESIPIPAddress_Type = IpAddress
_Xgs360026fACLACESIPIPAddress_Object = MibTableColumn
xgs360026fACLACESIPIPAddress = _Xgs360026fACLACESIPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 29),
    _Xgs360026fACLACESIPIPAddress_Type()
)
xgs360026fACLACESIPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACESIPIPAddress.setStatus("current")


class _Xgs360026fACLACESIPNetworkPrefix_Type(Integer32):
    """Custom type xgs360026fACLACESIPNetworkPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Xgs360026fACLACESIPNetworkPrefix_Type.__name__ = "Integer32"
_Xgs360026fACLACESIPNetworkPrefix_Object = MibTableColumn
xgs360026fACLACESIPNetworkPrefix = _Xgs360026fACLACESIPNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 30),
    _Xgs360026fACLACESIPNetworkPrefix_Type()
)
xgs360026fACLACESIPNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACESIPNetworkPrefix.setStatus("current")


class _Xgs360026fACLACEDIPType_Type(Integer32):
    """Custom type xgs360026fACLACEDIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fACLACEDIPType_Type.__name__ = "Integer32"
_Xgs360026fACLACEDIPType_Object = MibTableColumn
xgs360026fACLACEDIPType = _Xgs360026fACLACEDIPType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 32),
    _Xgs360026fACLACEDIPType_Type()
)
xgs360026fACLACEDIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEDIPType.setStatus("current")
_Xgs360026fACLACEDIPIPAddress_Type = IpAddress
_Xgs360026fACLACEDIPIPAddress_Object = MibTableColumn
xgs360026fACLACEDIPIPAddress = _Xgs360026fACLACEDIPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 33),
    _Xgs360026fACLACEDIPIPAddress_Type()
)
xgs360026fACLACEDIPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEDIPIPAddress.setStatus("current")


class _Xgs360026fACLACEDIPNetworkPrefix_Type(Integer32):
    """Custom type xgs360026fACLACEDIPNetworkPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Xgs360026fACLACEDIPNetworkPrefix_Type.__name__ = "Integer32"
_Xgs360026fACLACEDIPNetworkPrefix_Object = MibTableColumn
xgs360026fACLACEDIPNetworkPrefix = _Xgs360026fACLACEDIPNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 34),
    _Xgs360026fACLACEDIPNetworkPrefix_Type()
)
xgs360026fACLACEDIPNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEDIPNetworkPrefix.setStatus("current")


class _Xgs360026fACLACEIPProtocol_Type(Integer32):
    """Custom type xgs360026fACLACEIPProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Xgs360026fACLACEIPProtocol_Type.__name__ = "Integer32"
_Xgs360026fACLACEIPProtocol_Object = MibTableColumn
xgs360026fACLACEIPProtocol = _Xgs360026fACLACEIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 36),
    _Xgs360026fACLACEIPProtocol_Type()
)
xgs360026fACLACEIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEIPProtocol.setStatus("current")


class _Xgs360026fACLACEIPFlagsTTL_Type(Integer32):
    """Custom type xgs360026fACLACEIPFlagsTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Xgs360026fACLACEIPFlagsTTL_Type.__name__ = "Integer32"
_Xgs360026fACLACEIPFlagsTTL_Object = MibTableColumn
xgs360026fACLACEIPFlagsTTL = _Xgs360026fACLACEIPFlagsTTL_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 37),
    _Xgs360026fACLACEIPFlagsTTL_Type()
)
xgs360026fACLACEIPFlagsTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEIPFlagsTTL.setStatus("current")


class _Xgs360026fACLACEIPFlagsOptions_Type(Integer32):
    """Custom type xgs360026fACLACEIPFlagsOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Xgs360026fACLACEIPFlagsOptions_Type.__name__ = "Integer32"
_Xgs360026fACLACEIPFlagsOptions_Object = MibTableColumn
xgs360026fACLACEIPFlagsOptions = _Xgs360026fACLACEIPFlagsOptions_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 38),
    _Xgs360026fACLACEIPFlagsOptions_Type()
)
xgs360026fACLACEIPFlagsOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEIPFlagsOptions.setStatus("current")


class _Xgs360026fACLACEIPFlagsFragment_Type(Integer32):
    """Custom type xgs360026fACLACEIPFlagsFragment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Xgs360026fACLACEIPFlagsFragment_Type.__name__ = "Integer32"
_Xgs360026fACLACEIPFlagsFragment_Object = MibTableColumn
xgs360026fACLACEIPFlagsFragment = _Xgs360026fACLACEIPFlagsFragment_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 39),
    _Xgs360026fACLACEIPFlagsFragment_Type()
)
xgs360026fACLACEIPFlagsFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEIPFlagsFragment.setStatus("current")


class _Xgs360026fACLACEICMPType_Type(Integer32):
    """Custom type xgs360026fACLACEICMPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Xgs360026fACLACEICMPType_Type.__name__ = "Integer32"
_Xgs360026fACLACEICMPType_Object = MibTableColumn
xgs360026fACLACEICMPType = _Xgs360026fACLACEICMPType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 40),
    _Xgs360026fACLACEICMPType_Type()
)
xgs360026fACLACEICMPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEICMPType.setStatus("current")


class _Xgs360026fACLACEICMPCode_Type(Integer32):
    """Custom type xgs360026fACLACEICMPCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Xgs360026fACLACEICMPCode_Type.__name__ = "Integer32"
_Xgs360026fACLACEICMPCode_Object = MibTableColumn
xgs360026fACLACEICMPCode = _Xgs360026fACLACEICMPCode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 41),
    _Xgs360026fACLACEICMPCode_Type()
)
xgs360026fACLACEICMPCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEICMPCode.setStatus("current")


class _Xgs360026fACLACESourcePortMin_Type(Integer32):
    """Custom type xgs360026fACLACESourcePortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Xgs360026fACLACESourcePortMin_Type.__name__ = "Integer32"
_Xgs360026fACLACESourcePortMin_Object = MibTableColumn
xgs360026fACLACESourcePortMin = _Xgs360026fACLACESourcePortMin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 42),
    _Xgs360026fACLACESourcePortMin_Type()
)
xgs360026fACLACESourcePortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACESourcePortMin.setStatus("current")


class _Xgs360026fACLACESourcePortMax_Type(Integer32):
    """Custom type xgs360026fACLACESourcePortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Xgs360026fACLACESourcePortMax_Type.__name__ = "Integer32"
_Xgs360026fACLACESourcePortMax_Object = MibTableColumn
xgs360026fACLACESourcePortMax = _Xgs360026fACLACESourcePortMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 43),
    _Xgs360026fACLACESourcePortMax_Type()
)
xgs360026fACLACESourcePortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACESourcePortMax.setStatus("current")


class _Xgs360026fACLACEDestPortMin_Type(Integer32):
    """Custom type xgs360026fACLACEDestPortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Xgs360026fACLACEDestPortMin_Type.__name__ = "Integer32"
_Xgs360026fACLACEDestPortMin_Object = MibTableColumn
xgs360026fACLACEDestPortMin = _Xgs360026fACLACEDestPortMin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 44),
    _Xgs360026fACLACEDestPortMin_Type()
)
xgs360026fACLACEDestPortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEDestPortMin.setStatus("current")


class _Xgs360026fACLACEDestPortMax_Type(Integer32):
    """Custom type xgs360026fACLACEDestPortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Xgs360026fACLACEDestPortMax_Type.__name__ = "Integer32"
_Xgs360026fACLACEDestPortMax_Object = MibTableColumn
xgs360026fACLACEDestPortMax = _Xgs360026fACLACEDestPortMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 45),
    _Xgs360026fACLACEDestPortMax_Type()
)
xgs360026fACLACEDestPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEDestPortMax.setStatus("current")


class _Xgs360026fACLACETCPFlagsFin_Type(Integer32):
    """Custom type xgs360026fACLACETCPFlagsFin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Xgs360026fACLACETCPFlagsFin_Type.__name__ = "Integer32"
_Xgs360026fACLACETCPFlagsFin_Object = MibTableColumn
xgs360026fACLACETCPFlagsFin = _Xgs360026fACLACETCPFlagsFin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 46),
    _Xgs360026fACLACETCPFlagsFin_Type()
)
xgs360026fACLACETCPFlagsFin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACETCPFlagsFin.setStatus("current")


class _Xgs360026fACLACETCPFlagsSyn_Type(Integer32):
    """Custom type xgs360026fACLACETCPFlagsSyn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Xgs360026fACLACETCPFlagsSyn_Type.__name__ = "Integer32"
_Xgs360026fACLACETCPFlagsSyn_Object = MibTableColumn
xgs360026fACLACETCPFlagsSyn = _Xgs360026fACLACETCPFlagsSyn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 47),
    _Xgs360026fACLACETCPFlagsSyn_Type()
)
xgs360026fACLACETCPFlagsSyn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACETCPFlagsSyn.setStatus("current")


class _Xgs360026fACLACETCPFlagsRst_Type(Integer32):
    """Custom type xgs360026fACLACETCPFlagsRst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Xgs360026fACLACETCPFlagsRst_Type.__name__ = "Integer32"
_Xgs360026fACLACETCPFlagsRst_Object = MibTableColumn
xgs360026fACLACETCPFlagsRst = _Xgs360026fACLACETCPFlagsRst_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 48),
    _Xgs360026fACLACETCPFlagsRst_Type()
)
xgs360026fACLACETCPFlagsRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACETCPFlagsRst.setStatus("current")


class _Xgs360026fACLACETCPFlagsPsh_Type(Integer32):
    """Custom type xgs360026fACLACETCPFlagsPsh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Xgs360026fACLACETCPFlagsPsh_Type.__name__ = "Integer32"
_Xgs360026fACLACETCPFlagsPsh_Object = MibTableColumn
xgs360026fACLACETCPFlagsPsh = _Xgs360026fACLACETCPFlagsPsh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 49),
    _Xgs360026fACLACETCPFlagsPsh_Type()
)
xgs360026fACLACETCPFlagsPsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACETCPFlagsPsh.setStatus("current")


class _Xgs360026fACLACETCPFlagsAck_Type(Integer32):
    """Custom type xgs360026fACLACETCPFlagsAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Xgs360026fACLACETCPFlagsAck_Type.__name__ = "Integer32"
_Xgs360026fACLACETCPFlagsAck_Object = MibTableColumn
xgs360026fACLACETCPFlagsAck = _Xgs360026fACLACETCPFlagsAck_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 50),
    _Xgs360026fACLACETCPFlagsAck_Type()
)
xgs360026fACLACETCPFlagsAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACETCPFlagsAck.setStatus("current")


class _Xgs360026fACLACETCPFlagsUrg_Type(Integer32):
    """Custom type xgs360026fACLACETCPFlagsUrg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Xgs360026fACLACETCPFlagsUrg_Type.__name__ = "Integer32"
_Xgs360026fACLACETCPFlagsUrg_Object = MibTableColumn
xgs360026fACLACETCPFlagsUrg = _Xgs360026fACLACETCPFlagsUrg_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 51),
    _Xgs360026fACLACETCPFlagsUrg_Type()
)
xgs360026fACLACETCPFlagsUrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACETCPFlagsUrg.setStatus("current")


class _Xgs360026fACLACERowStatus_Type(Integer32):
    """Custom type xgs360026fACLACERowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Xgs360026fACLACERowStatus_Type.__name__ = "Integer32"
_Xgs360026fACLACERowStatus_Object = MibTableColumn
xgs360026fACLACERowStatus = _Xgs360026fACLACERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 2, 1, 66),
    _Xgs360026fACLACERowStatus_Type()
)
xgs360026fACLACERowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACERowStatus.setStatus("current")


class _Xgs360026fACLACEClear_Type(Integer32):
    """Custom type xgs360026fACLACEClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fACLACEClear_Type.__name__ = "Integer32"
_Xgs360026fACLACEClear_Object = MibScalar
xgs360026fACLACEClear = _Xgs360026fACLACEClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 3),
    _Xgs360026fACLACEClear_Type()
)
xgs360026fACLACEClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEClear.setStatus("current")


class _Xgs360026fACLACEMoveACEID_Type(Integer32):
    """Custom type xgs360026fACLACEMoveACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Xgs360026fACLACEMoveACEID_Type.__name__ = "Integer32"
_Xgs360026fACLACEMoveACEID_Object = MibScalar
xgs360026fACLACEMoveACEID = _Xgs360026fACLACEMoveACEID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 4),
    _Xgs360026fACLACEMoveACEID_Type()
)
xgs360026fACLACEMoveACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEMoveACEID.setStatus("current")


class _Xgs360026fACLACEMoveNextACEID_Type(Integer32):
    """Custom type xgs360026fACLACEMoveNextACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Xgs360026fACLACEMoveNextACEID_Type.__name__ = "Integer32"
_Xgs360026fACLACEMoveNextACEID_Object = MibScalar
xgs360026fACLACEMoveNextACEID = _Xgs360026fACLACEMoveNextACEID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 5),
    _Xgs360026fACLACEMoveNextACEID_Type()
)
xgs360026fACLACEMoveNextACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fACLACEMoveNextACEID.setStatus("current")
_Xgs360026fACLACEStatusTable_Object = MibTable
xgs360026fACLACEStatusTable = _Xgs360026fACLACEStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 6)
)
if mibBuilder.loadTexts:
    xgs360026fACLACEStatusTable.setStatus("current")
_Xgs360026fACLACEStatusEntry_Object = MibTableRow
xgs360026fACLACEStatusEntry = _Xgs360026fACLACEStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 6, 1)
)
xgs360026fACLACEStatusEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fACLACEStatusIndex"),
)
if mibBuilder.loadTexts:
    xgs360026fACLACEStatusEntry.setStatus("current")


class _Xgs360026fACLACEStatusIndex_Type(Integer32):
    """Custom type xgs360026fACLACEStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Xgs360026fACLACEStatusIndex_Type.__name__ = "Integer32"
_Xgs360026fACLACEStatusIndex_Object = MibTableColumn
xgs360026fACLACEStatusIndex = _Xgs360026fACLACEStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 6, 1, 1),
    _Xgs360026fACLACEStatusIndex_Type()
)
xgs360026fACLACEStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fACLACEStatusIndex.setStatus("current")
_Xgs360026fACLACEStatusUser_Type = DisplayString
_Xgs360026fACLACEStatusUser_Object = MibTableColumn
xgs360026fACLACEStatusUser = _Xgs360026fACLACEStatusUser_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 6, 1, 2),
    _Xgs360026fACLACEStatusUser_Type()
)
xgs360026fACLACEStatusUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fACLACEStatusUser.setStatus("current")


class _Xgs360026fACLACEStatusID_Type(Integer32):
    """Custom type xgs360026fACLACEStatusID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Xgs360026fACLACEStatusID_Type.__name__ = "Integer32"
_Xgs360026fACLACEStatusID_Object = MibTableColumn
xgs360026fACLACEStatusID = _Xgs360026fACLACEStatusID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 6, 1, 3),
    _Xgs360026fACLACEStatusID_Type()
)
xgs360026fACLACEStatusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fACLACEStatusID.setStatus("current")
_Xgs360026fACLACEStatusIngressPort_Type = DisplayString
_Xgs360026fACLACEStatusIngressPort_Object = MibTableColumn
xgs360026fACLACEStatusIngressPort = _Xgs360026fACLACEStatusIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 6, 1, 4),
    _Xgs360026fACLACEStatusIngressPort_Type()
)
xgs360026fACLACEStatusIngressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fACLACEStatusIngressPort.setStatus("current")
_Xgs360026fACLACEStatusFrameType_Type = DisplayString
_Xgs360026fACLACEStatusFrameType_Object = MibTableColumn
xgs360026fACLACEStatusFrameType = _Xgs360026fACLACEStatusFrameType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 6, 1, 5),
    _Xgs360026fACLACEStatusFrameType_Type()
)
xgs360026fACLACEStatusFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fACLACEStatusFrameType.setStatus("current")
_Xgs360026fACLACEStatusAction_Type = DisplayString
_Xgs360026fACLACEStatusAction_Object = MibTableColumn
xgs360026fACLACEStatusAction = _Xgs360026fACLACEStatusAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 6, 1, 6),
    _Xgs360026fACLACEStatusAction_Type()
)
xgs360026fACLACEStatusAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fACLACEStatusAction.setStatus("current")
_Xgs360026fACLACEStatusRateLimiter_Type = DisplayString
_Xgs360026fACLACEStatusRateLimiter_Object = MibTableColumn
xgs360026fACLACEStatusRateLimiter = _Xgs360026fACLACEStatusRateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 6, 1, 7),
    _Xgs360026fACLACEStatusRateLimiter_Type()
)
xgs360026fACLACEStatusRateLimiter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fACLACEStatusRateLimiter.setStatus("current")
_Xgs360026fACLACEStatusPortCopy_Type = DisplayString
_Xgs360026fACLACEStatusPortCopy_Object = MibTableColumn
xgs360026fACLACEStatusPortCopy = _Xgs360026fACLACEStatusPortCopy_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 6, 1, 8),
    _Xgs360026fACLACEStatusPortCopy_Type()
)
xgs360026fACLACEStatusPortCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fACLACEStatusPortCopy.setStatus("current")
_Xgs360026fACLACEStatusMirror_Type = DisplayString
_Xgs360026fACLACEStatusMirror_Object = MibTableColumn
xgs360026fACLACEStatusMirror = _Xgs360026fACLACEStatusMirror_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 6, 1, 9),
    _Xgs360026fACLACEStatusMirror_Type()
)
xgs360026fACLACEStatusMirror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fACLACEStatusMirror.setStatus("current")
_Xgs360026fACLACEStatusCPU_Type = DisplayString
_Xgs360026fACLACEStatusCPU_Object = MibTableColumn
xgs360026fACLACEStatusCPU = _Xgs360026fACLACEStatusCPU_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 6, 1, 10),
    _Xgs360026fACLACEStatusCPU_Type()
)
xgs360026fACLACEStatusCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fACLACEStatusCPU.setStatus("current")
_Xgs360026fACLACEStatusCounter_Type = Counter32
_Xgs360026fACLACEStatusCounter_Object = MibTableColumn
xgs360026fACLACEStatusCounter = _Xgs360026fACLACEStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 6, 1, 11),
    _Xgs360026fACLACEStatusCounter_Type()
)
xgs360026fACLACEStatusCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fACLACEStatusCounter.setStatus("current")
_Xgs360026fACLACEStatusConflict_Type = DisplayString
_Xgs360026fACLACEStatusConflict_Object = MibTableColumn
xgs360026fACLACEStatusConflict = _Xgs360026fACLACEStatusConflict_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 9, 3, 6, 1, 12),
    _Xgs360026fACLACEStatusConflict_Type()
)
xgs360026fACLACEStatusConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fACLACEStatusConflict.setStatus("current")
_Xgs360026fERPS_ObjectIdentity = ObjectIdentity
xgs360026fERPS = _Xgs360026fERPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10)
)
_Xgs360026fERPSConf_ObjectIdentity = ObjectIdentity
xgs360026fERPSConf = _Xgs360026fERPSConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1)
)


class _Xgs360026fERPSConfCreate_Type(Integer32):
    """Custom type xgs360026fERPSConfCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fERPSConfCreate_Type.__name__ = "Integer32"
_Xgs360026fERPSConfCreate_Object = MibScalar
xgs360026fERPSConfCreate = _Xgs360026fERPSConfCreate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 1),
    _Xgs360026fERPSConfCreate_Type()
)
xgs360026fERPSConfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSConfCreate.setStatus("current")
_Xgs360026fERPSConfTable_Object = MibTable
xgs360026fERPSConfTable = _Xgs360026fERPSConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2)
)
if mibBuilder.loadTexts:
    xgs360026fERPSConfTable.setStatus("current")
_Xgs360026fERPSConfEntry_Object = MibTableRow
xgs360026fERPSConfEntry = _Xgs360026fERPSConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1)
)
xgs360026fERPSConfEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fERPSConfIndex"),
)
if mibBuilder.loadTexts:
    xgs360026fERPSConfEntry.setStatus("current")


class _Xgs360026fERPSConfIndex_Type(Integer32):
    """Custom type xgs360026fERPSConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Xgs360026fERPSConfIndex_Type.__name__ = "Integer32"
_Xgs360026fERPSConfIndex_Object = MibTableColumn
xgs360026fERPSConfIndex = _Xgs360026fERPSConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 1),
    _Xgs360026fERPSConfIndex_Type()
)
xgs360026fERPSConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fERPSConfIndex.setStatus("current")


class _Xgs360026fERPSConfERPSID_Type(Integer32):
    """Custom type xgs360026fERPSConfERPSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Xgs360026fERPSConfERPSID_Type.__name__ = "Integer32"
_Xgs360026fERPSConfERPSID_Object = MibTableColumn
xgs360026fERPSConfERPSID = _Xgs360026fERPSConfERPSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 2),
    _Xgs360026fERPSConfERPSID_Type()
)
xgs360026fERPSConfERPSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSConfERPSID.setStatus("current")


class _Xgs360026fERPSConfPort0_Type(Integer32):
    """Custom type xgs360026fERPSConfPort0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Xgs360026fERPSConfPort0_Type.__name__ = "Integer32"
_Xgs360026fERPSConfPort0_Object = MibTableColumn
xgs360026fERPSConfPort0 = _Xgs360026fERPSConfPort0_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 3),
    _Xgs360026fERPSConfPort0_Type()
)
xgs360026fERPSConfPort0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSConfPort0.setStatus("current")


class _Xgs360026fERPSConfPort1_Type(Integer32):
    """Custom type xgs360026fERPSConfPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 26),
    )


_Xgs360026fERPSConfPort1_Type.__name__ = "Integer32"
_Xgs360026fERPSConfPort1_Object = MibTableColumn
xgs360026fERPSConfPort1 = _Xgs360026fERPSConfPort1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 4),
    _Xgs360026fERPSConfPort1_Type()
)
xgs360026fERPSConfPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSConfPort1.setStatus("current")


class _Xgs360026fERPSConfPort0SFMEP_Type(Integer32):
    """Custom type xgs360026fERPSConfPort0SFMEP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Xgs360026fERPSConfPort0SFMEP_Type.__name__ = "Integer32"
_Xgs360026fERPSConfPort0SFMEP_Object = MibTableColumn
xgs360026fERPSConfPort0SFMEP = _Xgs360026fERPSConfPort0SFMEP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 5),
    _Xgs360026fERPSConfPort0SFMEP_Type()
)
xgs360026fERPSConfPort0SFMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSConfPort0SFMEP.setStatus("current")


class _Xgs360026fERPSConfPort1SFMEP_Type(Integer32):
    """Custom type xgs360026fERPSConfPort1SFMEP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Xgs360026fERPSConfPort1SFMEP_Type.__name__ = "Integer32"
_Xgs360026fERPSConfPort1SFMEP_Object = MibTableColumn
xgs360026fERPSConfPort1SFMEP = _Xgs360026fERPSConfPort1SFMEP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 6),
    _Xgs360026fERPSConfPort1SFMEP_Type()
)
xgs360026fERPSConfPort1SFMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSConfPort1SFMEP.setStatus("current")


class _Xgs360026fERPSConfPort0APSMEP_Type(Integer32):
    """Custom type xgs360026fERPSConfPort0APSMEP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Xgs360026fERPSConfPort0APSMEP_Type.__name__ = "Integer32"
_Xgs360026fERPSConfPort0APSMEP_Object = MibTableColumn
xgs360026fERPSConfPort0APSMEP = _Xgs360026fERPSConfPort0APSMEP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 7),
    _Xgs360026fERPSConfPort0APSMEP_Type()
)
xgs360026fERPSConfPort0APSMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSConfPort0APSMEP.setStatus("current")


class _Xgs360026fERPSConfPort1APSMEP_Type(Integer32):
    """Custom type xgs360026fERPSConfPort1APSMEP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Xgs360026fERPSConfPort1APSMEP_Type.__name__ = "Integer32"
_Xgs360026fERPSConfPort1APSMEP_Object = MibTableColumn
xgs360026fERPSConfPort1APSMEP = _Xgs360026fERPSConfPort1APSMEP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 8),
    _Xgs360026fERPSConfPort1APSMEP_Type()
)
xgs360026fERPSConfPort1APSMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSConfPort1APSMEP.setStatus("current")


class _Xgs360026fERPSConfRingType_Type(Integer32):
    """Custom type xgs360026fERPSConfRingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fERPSConfRingType_Type.__name__ = "Integer32"
_Xgs360026fERPSConfRingType_Object = MibTableColumn
xgs360026fERPSConfRingType = _Xgs360026fERPSConfRingType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 9),
    _Xgs360026fERPSConfRingType_Type()
)
xgs360026fERPSConfRingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSConfRingType.setStatus("current")


class _Xgs360026fERPSConfInterconnectedNode_Type(Integer32):
    """Custom type xgs360026fERPSConfInterconnectedNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fERPSConfInterconnectedNode_Type.__name__ = "Integer32"
_Xgs360026fERPSConfInterconnectedNode_Object = MibTableColumn
xgs360026fERPSConfInterconnectedNode = _Xgs360026fERPSConfInterconnectedNode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 10),
    _Xgs360026fERPSConfInterconnectedNode_Type()
)
xgs360026fERPSConfInterconnectedNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSConfInterconnectedNode.setStatus("current")


class _Xgs360026fERPSConfVirtualChannel_Type(Integer32):
    """Custom type xgs360026fERPSConfVirtualChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fERPSConfVirtualChannel_Type.__name__ = "Integer32"
_Xgs360026fERPSConfVirtualChannel_Object = MibTableColumn
xgs360026fERPSConfVirtualChannel = _Xgs360026fERPSConfVirtualChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 11),
    _Xgs360026fERPSConfVirtualChannel_Type()
)
xgs360026fERPSConfVirtualChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSConfVirtualChannel.setStatus("current")


class _Xgs360026fERPSConfMajorRingID_Type(Integer32):
    """Custom type xgs360026fERPSConfMajorRingID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Xgs360026fERPSConfMajorRingID_Type.__name__ = "Integer32"
_Xgs360026fERPSConfMajorRingID_Object = MibTableColumn
xgs360026fERPSConfMajorRingID = _Xgs360026fERPSConfMajorRingID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 12),
    _Xgs360026fERPSConfMajorRingID_Type()
)
xgs360026fERPSConfMajorRingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fERPSConfMajorRingID.setStatus("current")


class _Xgs360026fERPSConfAlarm_Type(DisplayString):
    """Custom type xgs360026fERPSConfAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xgs360026fERPSConfAlarm_Type.__name__ = "DisplayString"
_Xgs360026fERPSConfAlarm_Object = MibTableColumn
xgs360026fERPSConfAlarm = _Xgs360026fERPSConfAlarm_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 13),
    _Xgs360026fERPSConfAlarm_Type()
)
xgs360026fERPSConfAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fERPSConfAlarm.setStatus("current")


class _Xgs360026fERPSInstanceConfConfigured_Type(DisplayString):
    """Custom type xgs360026fERPSInstanceConfConfigured based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xgs360026fERPSInstanceConfConfigured_Type.__name__ = "DisplayString"
_Xgs360026fERPSInstanceConfConfigured_Object = MibTableColumn
xgs360026fERPSInstanceConfConfigured = _Xgs360026fERPSInstanceConfConfigured_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 14),
    _Xgs360026fERPSInstanceConfConfigured_Type()
)
xgs360026fERPSInstanceConfConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fERPSInstanceConfConfigured.setStatus("current")


class _Xgs360026fERPSInstanceConfGuardTime_Type(Integer32):
    """Custom type xgs360026fERPSInstanceConfGuardTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_Xgs360026fERPSInstanceConfGuardTime_Type.__name__ = "Integer32"
_Xgs360026fERPSInstanceConfGuardTime_Object = MibTableColumn
xgs360026fERPSInstanceConfGuardTime = _Xgs360026fERPSInstanceConfGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 15),
    _Xgs360026fERPSInstanceConfGuardTime_Type()
)
xgs360026fERPSInstanceConfGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSInstanceConfGuardTime.setStatus("current")


class _Xgs360026fERPSInstanceConfWTRTime_Type(Integer32):
    """Custom type xgs360026fERPSInstanceConfWTRTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Xgs360026fERPSInstanceConfWTRTime_Type.__name__ = "Integer32"
_Xgs360026fERPSInstanceConfWTRTime_Object = MibTableColumn
xgs360026fERPSInstanceConfWTRTime = _Xgs360026fERPSInstanceConfWTRTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 16),
    _Xgs360026fERPSInstanceConfWTRTime_Type()
)
xgs360026fERPSInstanceConfWTRTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSInstanceConfWTRTime.setStatus("current")


class _Xgs360026fERPSInstanceConfHoldOffTime_Type(Integer32):
    """Custom type xgs360026fERPSInstanceConfHoldOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Xgs360026fERPSInstanceConfHoldOffTime_Type.__name__ = "Integer32"
_Xgs360026fERPSInstanceConfHoldOffTime_Object = MibTableColumn
xgs360026fERPSInstanceConfHoldOffTime = _Xgs360026fERPSInstanceConfHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 17),
    _Xgs360026fERPSInstanceConfHoldOffTime_Type()
)
xgs360026fERPSInstanceConfHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSInstanceConfHoldOffTime.setStatus("current")


class _Xgs360026fERPSInstanceConfVersion_Type(Integer32):
    """Custom type xgs360026fERPSInstanceConfVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fERPSInstanceConfVersion_Type.__name__ = "Integer32"
_Xgs360026fERPSInstanceConfVersion_Object = MibTableColumn
xgs360026fERPSInstanceConfVersion = _Xgs360026fERPSInstanceConfVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 18),
    _Xgs360026fERPSInstanceConfVersion_Type()
)
xgs360026fERPSInstanceConfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSInstanceConfVersion.setStatus("current")


class _Xgs360026fERPSInstanceConfRevertive_Type(Integer32):
    """Custom type xgs360026fERPSInstanceConfRevertive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fERPSInstanceConfRevertive_Type.__name__ = "Integer32"
_Xgs360026fERPSInstanceConfRevertive_Object = MibTableColumn
xgs360026fERPSInstanceConfRevertive = _Xgs360026fERPSInstanceConfRevertive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 19),
    _Xgs360026fERPSInstanceConfRevertive_Type()
)
xgs360026fERPSInstanceConfRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSInstanceConfRevertive.setStatus("current")


class _Xgs360026fERPSInstanceConfVLANconfig_Type(DisplayString):
    """Custom type xgs360026fERPSInstanceConfVLANconfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Xgs360026fERPSInstanceConfVLANconfig_Type.__name__ = "DisplayString"
_Xgs360026fERPSInstanceConfVLANconfig_Object = MibTableColumn
xgs360026fERPSInstanceConfVLANconfig = _Xgs360026fERPSInstanceConfVLANconfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 20),
    _Xgs360026fERPSInstanceConfVLANconfig_Type()
)
xgs360026fERPSInstanceConfVLANconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSInstanceConfVLANconfig.setStatus("current")


class _Xgs360026fERPSConfRowStatus_Type(Integer32):
    """Custom type xgs360026fERPSConfRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Xgs360026fERPSConfRowStatus_Type.__name__ = "Integer32"
_Xgs360026fERPSConfRowStatus_Object = MibTableColumn
xgs360026fERPSConfRowStatus = _Xgs360026fERPSConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 10, 1, 2, 1, 21),
    _Xgs360026fERPSConfRowStatus_Type()
)
xgs360026fERPSConfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fERPSConfRowStatus.setStatus("current")
_Xgs360026fMRSTP_ObjectIdentity = ObjectIdentity
xgs360026fMRSTP = _Xgs360026fMRSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11)
)
_Xgs360026fMRSTPInstance_ObjectIdentity = ObjectIdentity
xgs360026fMRSTPInstance = _Xgs360026fMRSTPInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1)
)
_Xgs360026fMRSTPInstanceConf_ObjectIdentity = ObjectIdentity
xgs360026fMRSTPInstanceConf = _Xgs360026fMRSTPInstanceConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 1)
)


class _Xgs360026fMRSTPInstanceConfGlobalState_Type(Integer32):
    """Custom type xgs360026fMRSTPInstanceConfGlobalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fMRSTPInstanceConfGlobalState_Type.__name__ = "Integer32"
_Xgs360026fMRSTPInstanceConfGlobalState_Object = MibScalar
xgs360026fMRSTPInstanceConfGlobalState = _Xgs360026fMRSTPInstanceConfGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 1, 1),
    _Xgs360026fMRSTPInstanceConfGlobalState_Type()
)
xgs360026fMRSTPInstanceConfGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceConfGlobalState.setStatus("current")
_Xgs360026fMRSTPInstanceConfigurationTable_Object = MibTable
xgs360026fMRSTPInstanceConfigurationTable = _Xgs360026fMRSTPInstanceConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 1, 2)
)
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceConfigurationTable.setStatus("current")
_Xgs360026fMRSTPInstanceConfigurationEntry_Object = MibTableRow
xgs360026fMRSTPInstanceConfigurationEntry = _Xgs360026fMRSTPInstanceConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 1, 2, 1)
)
xgs360026fMRSTPInstanceConfigurationEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fMRSTPInstanceConfigurationInstance"),
)
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceConfigurationEntry.setStatus("current")


class _Xgs360026fMRSTPInstanceConfigurationInstance_Type(Integer32):
    """Custom type xgs360026fMRSTPInstanceConfigurationInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Xgs360026fMRSTPInstanceConfigurationInstance_Type.__name__ = "Integer32"
_Xgs360026fMRSTPInstanceConfigurationInstance_Object = MibTableColumn
xgs360026fMRSTPInstanceConfigurationInstance = _Xgs360026fMRSTPInstanceConfigurationInstance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 1, 2, 1, 1),
    _Xgs360026fMRSTPInstanceConfigurationInstance_Type()
)
xgs360026fMRSTPInstanceConfigurationInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceConfigurationInstance.setStatus("current")


class _Xgs360026fMRSTPInstanceConfigurationState_Type(Integer32):
    """Custom type xgs360026fMRSTPInstanceConfigurationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fMRSTPInstanceConfigurationState_Type.__name__ = "Integer32"
_Xgs360026fMRSTPInstanceConfigurationState_Object = MibTableColumn
xgs360026fMRSTPInstanceConfigurationState = _Xgs360026fMRSTPInstanceConfigurationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 1, 2, 1, 2),
    _Xgs360026fMRSTPInstanceConfigurationState_Type()
)
xgs360026fMRSTPInstanceConfigurationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceConfigurationState.setStatus("current")


class _Xgs360026fMRSTPInstanceConfigurationVersion_Type(Integer32):
    """Custom type xgs360026fMRSTPInstanceConfigurationVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fMRSTPInstanceConfigurationVersion_Type.__name__ = "Integer32"
_Xgs360026fMRSTPInstanceConfigurationVersion_Object = MibTableColumn
xgs360026fMRSTPInstanceConfigurationVersion = _Xgs360026fMRSTPInstanceConfigurationVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 1, 2, 1, 3),
    _Xgs360026fMRSTPInstanceConfigurationVersion_Type()
)
xgs360026fMRSTPInstanceConfigurationVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceConfigurationVersion.setStatus("current")


class _Xgs360026fMRSTPInstanceConfigurationPriority_Type(Integer32):
    """Custom type xgs360026fMRSTPInstanceConfigurationPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Xgs360026fMRSTPInstanceConfigurationPriority_Type.__name__ = "Integer32"
_Xgs360026fMRSTPInstanceConfigurationPriority_Object = MibTableColumn
xgs360026fMRSTPInstanceConfigurationPriority = _Xgs360026fMRSTPInstanceConfigurationPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 1, 2, 1, 4),
    _Xgs360026fMRSTPInstanceConfigurationPriority_Type()
)
xgs360026fMRSTPInstanceConfigurationPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceConfigurationPriority.setStatus("current")


class _Xgs360026fMRSTPInstanceConfigurationHelloTime_Type(Integer32):
    """Custom type xgs360026fMRSTPInstanceConfigurationHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Xgs360026fMRSTPInstanceConfigurationHelloTime_Type.__name__ = "Integer32"
_Xgs360026fMRSTPInstanceConfigurationHelloTime_Object = MibTableColumn
xgs360026fMRSTPInstanceConfigurationHelloTime = _Xgs360026fMRSTPInstanceConfigurationHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 1, 2, 1, 5),
    _Xgs360026fMRSTPInstanceConfigurationHelloTime_Type()
)
xgs360026fMRSTPInstanceConfigurationHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceConfigurationHelloTime.setStatus("current")


class _Xgs360026fMRSTPInstanceConfigurationMaxAge_Type(Integer32):
    """Custom type xgs360026fMRSTPInstanceConfigurationMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Xgs360026fMRSTPInstanceConfigurationMaxAge_Type.__name__ = "Integer32"
_Xgs360026fMRSTPInstanceConfigurationMaxAge_Object = MibTableColumn
xgs360026fMRSTPInstanceConfigurationMaxAge = _Xgs360026fMRSTPInstanceConfigurationMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 1, 2, 1, 6),
    _Xgs360026fMRSTPInstanceConfigurationMaxAge_Type()
)
xgs360026fMRSTPInstanceConfigurationMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceConfigurationMaxAge.setStatus("current")


class _Xgs360026fMRSTPInstanceConfigurationFWDelay_Type(Integer32):
    """Custom type xgs360026fMRSTPInstanceConfigurationFWDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_Xgs360026fMRSTPInstanceConfigurationFWDelay_Type.__name__ = "Integer32"
_Xgs360026fMRSTPInstanceConfigurationFWDelay_Object = MibTableColumn
xgs360026fMRSTPInstanceConfigurationFWDelay = _Xgs360026fMRSTPInstanceConfigurationFWDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 1, 2, 1, 7),
    _Xgs360026fMRSTPInstanceConfigurationFWDelay_Type()
)
xgs360026fMRSTPInstanceConfigurationFWDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceConfigurationFWDelay.setStatus("current")
_Xgs360026fMRSTPInstanceStatus_ObjectIdentity = ObjectIdentity
xgs360026fMRSTPInstanceStatus = _Xgs360026fMRSTPInstanceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 2)
)
_Xgs360026fMRSTPInstanceStatusTable_Object = MibTable
xgs360026fMRSTPInstanceStatusTable = _Xgs360026fMRSTPInstanceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceStatusTable.setStatus("current")
_Xgs360026fMRSTPInstanceStatusEntry_Object = MibTableRow
xgs360026fMRSTPInstanceStatusEntry = _Xgs360026fMRSTPInstanceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 2, 1, 1)
)
xgs360026fMRSTPInstanceStatusEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fMRSTPInstanceStatusInstance"),
)
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceStatusEntry.setStatus("current")


class _Xgs360026fMRSTPInstanceStatusInstance_Type(Integer32):
    """Custom type xgs360026fMRSTPInstanceStatusInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Xgs360026fMRSTPInstanceStatusInstance_Type.__name__ = "Integer32"
_Xgs360026fMRSTPInstanceStatusInstance_Object = MibTableColumn
xgs360026fMRSTPInstanceStatusInstance = _Xgs360026fMRSTPInstanceStatusInstance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 2, 1, 1, 1),
    _Xgs360026fMRSTPInstanceStatusInstance_Type()
)
xgs360026fMRSTPInstanceStatusInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceStatusInstance.setStatus("current")


class _Xgs360026fMRSTPInstanceStatusGlobalState_Type(Integer32):
    """Custom type xgs360026fMRSTPInstanceStatusGlobalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fMRSTPInstanceStatusGlobalState_Type.__name__ = "Integer32"
_Xgs360026fMRSTPInstanceStatusGlobalState_Object = MibTableColumn
xgs360026fMRSTPInstanceStatusGlobalState = _Xgs360026fMRSTPInstanceStatusGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 2, 1, 1, 2),
    _Xgs360026fMRSTPInstanceStatusGlobalState_Type()
)
xgs360026fMRSTPInstanceStatusGlobalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceStatusGlobalState.setStatus("current")


class _Xgs360026fMRSTPInstanceStatusInstanceConfigState_Type(Integer32):
    """Custom type xgs360026fMRSTPInstanceStatusInstanceConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fMRSTPInstanceStatusInstanceConfigState_Type.__name__ = "Integer32"
_Xgs360026fMRSTPInstanceStatusInstanceConfigState_Object = MibTableColumn
xgs360026fMRSTPInstanceStatusInstanceConfigState = _Xgs360026fMRSTPInstanceStatusInstanceConfigState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 2, 1, 1, 3),
    _Xgs360026fMRSTPInstanceStatusInstanceConfigState_Type()
)
xgs360026fMRSTPInstanceStatusInstanceConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceStatusInstanceConfigState.setStatus("current")


class _Xgs360026fMRSTPInstanceStatusInstanceCurrentState_Type(Integer32):
    """Custom type xgs360026fMRSTPInstanceStatusInstanceCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fMRSTPInstanceStatusInstanceCurrentState_Type.__name__ = "Integer32"
_Xgs360026fMRSTPInstanceStatusInstanceCurrentState_Object = MibTableColumn
xgs360026fMRSTPInstanceStatusInstanceCurrentState = _Xgs360026fMRSTPInstanceStatusInstanceCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 2, 1, 1, 4),
    _Xgs360026fMRSTPInstanceStatusInstanceCurrentState_Type()
)
xgs360026fMRSTPInstanceStatusInstanceCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceStatusInstanceCurrentState.setStatus("current")
_Xgs360026fMRSTPInstanceStatusBridgeID_Type = MacAddress
_Xgs360026fMRSTPInstanceStatusBridgeID_Object = MibTableColumn
xgs360026fMRSTPInstanceStatusBridgeID = _Xgs360026fMRSTPInstanceStatusBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 2, 1, 1, 5),
    _Xgs360026fMRSTPInstanceStatusBridgeID_Type()
)
xgs360026fMRSTPInstanceStatusBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceStatusBridgeID.setStatus("current")


class _Xgs360026fMRSTPInstanceStatusBridgePrioriry_Type(Integer32):
    """Custom type xgs360026fMRSTPInstanceStatusBridgePrioriry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Xgs360026fMRSTPInstanceStatusBridgePrioriry_Type.__name__ = "Integer32"
_Xgs360026fMRSTPInstanceStatusBridgePrioriry_Object = MibTableColumn
xgs360026fMRSTPInstanceStatusBridgePrioriry = _Xgs360026fMRSTPInstanceStatusBridgePrioriry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 2, 1, 1, 6),
    _Xgs360026fMRSTPInstanceStatusBridgePrioriry_Type()
)
xgs360026fMRSTPInstanceStatusBridgePrioriry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceStatusBridgePrioriry.setStatus("current")
_Xgs360026fMRSTPInstanceStatusRootID_Type = MacAddress
_Xgs360026fMRSTPInstanceStatusRootID_Object = MibTableColumn
xgs360026fMRSTPInstanceStatusRootID = _Xgs360026fMRSTPInstanceStatusRootID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 2, 1, 1, 7),
    _Xgs360026fMRSTPInstanceStatusRootID_Type()
)
xgs360026fMRSTPInstanceStatusRootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceStatusRootID.setStatus("current")


class _Xgs360026fMRSTPInstanceStatusRootPriority_Type(Integer32):
    """Custom type xgs360026fMRSTPInstanceStatusRootPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Xgs360026fMRSTPInstanceStatusRootPriority_Type.__name__ = "Integer32"
_Xgs360026fMRSTPInstanceStatusRootPriority_Object = MibTableColumn
xgs360026fMRSTPInstanceStatusRootPriority = _Xgs360026fMRSTPInstanceStatusRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 2, 1, 1, 8),
    _Xgs360026fMRSTPInstanceStatusRootPriority_Type()
)
xgs360026fMRSTPInstanceStatusRootPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceStatusRootPriority.setStatus("current")
_Xgs360026fMRSTPInstanceStatusRootPort_Type = Integer32
_Xgs360026fMRSTPInstanceStatusRootPort_Object = MibTableColumn
xgs360026fMRSTPInstanceStatusRootPort = _Xgs360026fMRSTPInstanceStatusRootPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 2, 1, 1, 9),
    _Xgs360026fMRSTPInstanceStatusRootPort_Type()
)
xgs360026fMRSTPInstanceStatusRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceStatusRootPort.setStatus("current")
_Xgs360026fMRSTPInstanceStatusRootPathCost_Type = Integer32
_Xgs360026fMRSTPInstanceStatusRootPathCost_Object = MibTableColumn
xgs360026fMRSTPInstanceStatusRootPathCost = _Xgs360026fMRSTPInstanceStatusRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 2, 1, 1, 10),
    _Xgs360026fMRSTPInstanceStatusRootPathCost_Type()
)
xgs360026fMRSTPInstanceStatusRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceStatusRootPathCost.setStatus("current")


class _Xgs360026fMRSTPInstanceStatusCurrentMaxAge_Type(Integer32):
    """Custom type xgs360026fMRSTPInstanceStatusCurrentMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Xgs360026fMRSTPInstanceStatusCurrentMaxAge_Type.__name__ = "Integer32"
_Xgs360026fMRSTPInstanceStatusCurrentMaxAge_Object = MibTableColumn
xgs360026fMRSTPInstanceStatusCurrentMaxAge = _Xgs360026fMRSTPInstanceStatusCurrentMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 2, 1, 1, 11),
    _Xgs360026fMRSTPInstanceStatusCurrentMaxAge_Type()
)
xgs360026fMRSTPInstanceStatusCurrentMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceStatusCurrentMaxAge.setStatus("current")


class _Xgs360026fMRSTPInstanceStatusCurrentForwardDelay_Type(Integer32):
    """Custom type xgs360026fMRSTPInstanceStatusCurrentForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_Xgs360026fMRSTPInstanceStatusCurrentForwardDelay_Type.__name__ = "Integer32"
_Xgs360026fMRSTPInstanceStatusCurrentForwardDelay_Object = MibTableColumn
xgs360026fMRSTPInstanceStatusCurrentForwardDelay = _Xgs360026fMRSTPInstanceStatusCurrentForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 2, 1, 1, 12),
    _Xgs360026fMRSTPInstanceStatusCurrentForwardDelay_Type()
)
xgs360026fMRSTPInstanceStatusCurrentForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceStatusCurrentForwardDelay.setStatus("current")


class _Xgs360026fMRSTPInstanceStatusHelloTime_Type(Integer32):
    """Custom type xgs360026fMRSTPInstanceStatusHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Xgs360026fMRSTPInstanceStatusHelloTime_Type.__name__ = "Integer32"
_Xgs360026fMRSTPInstanceStatusHelloTime_Object = MibTableColumn
xgs360026fMRSTPInstanceStatusHelloTime = _Xgs360026fMRSTPInstanceStatusHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 2, 1, 1, 13),
    _Xgs360026fMRSTPInstanceStatusHelloTime_Type()
)
xgs360026fMRSTPInstanceStatusHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceStatusHelloTime.setStatus("current")
_Xgs360026fMRSTPInstanceStatusTopologyChangeCount_Type = Integer32
_Xgs360026fMRSTPInstanceStatusTopologyChangeCount_Object = MibTableColumn
xgs360026fMRSTPInstanceStatusTopologyChangeCount = _Xgs360026fMRSTPInstanceStatusTopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 2, 1, 1, 14),
    _Xgs360026fMRSTPInstanceStatusTopologyChangeCount_Type()
)
xgs360026fMRSTPInstanceStatusTopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceStatusTopologyChangeCount.setStatus("current")
_Xgs360026fMRSTPInstanceStatusTimeSinceLastTopologyChange_Type = Integer32
_Xgs360026fMRSTPInstanceStatusTimeSinceLastTopologyChange_Object = MibTableColumn
xgs360026fMRSTPInstanceStatusTimeSinceLastTopologyChange = _Xgs360026fMRSTPInstanceStatusTimeSinceLastTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 1, 2, 1, 1, 15),
    _Xgs360026fMRSTPInstanceStatusTimeSinceLastTopologyChange_Type()
)
xgs360026fMRSTPInstanceStatusTimeSinceLastTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPInstanceStatusTimeSinceLastTopologyChange.setStatus("current")
_Xgs360026fMRSTPPort_ObjectIdentity = ObjectIdentity
xgs360026fMRSTPPort = _Xgs360026fMRSTPPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2)
)
_Xgs360026fMRSTPPortConfiguration_ObjectIdentity = ObjectIdentity
xgs360026fMRSTPPortConfiguration = _Xgs360026fMRSTPPortConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 1)
)
_Xgs360026fMRSTPPortConfigurationTable_Object = MibTable
xgs360026fMRSTPPortConfigurationTable = _Xgs360026fMRSTPPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortConfigurationTable.setStatus("current")
_Xgs360026fMRSTPPortConfigurationEntry_Object = MibTableRow
xgs360026fMRSTPPortConfigurationEntry = _Xgs360026fMRSTPPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 1, 1, 1)
)
xgs360026fMRSTPPortConfigurationEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fMRSTPPortConfigurationPort"),
)
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortConfigurationEntry.setStatus("current")


class _Xgs360026fMRSTPPortConfigurationPort_Type(Integer32):
    """Custom type xgs360026fMRSTPPortConfigurationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fMRSTPPortConfigurationPort_Type.__name__ = "Integer32"
_Xgs360026fMRSTPPortConfigurationPort_Object = MibTableColumn
xgs360026fMRSTPPortConfigurationPort = _Xgs360026fMRSTPPortConfigurationPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 1, 1, 1, 1),
    _Xgs360026fMRSTPPortConfigurationPort_Type()
)
xgs360026fMRSTPPortConfigurationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortConfigurationPort.setStatus("current")


class _Xgs360026fMRSTPPortConfigurationInstance_Type(Integer32):
    """Custom type xgs360026fMRSTPPortConfigurationInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Xgs360026fMRSTPPortConfigurationInstance_Type.__name__ = "Integer32"
_Xgs360026fMRSTPPortConfigurationInstance_Object = MibTableColumn
xgs360026fMRSTPPortConfigurationInstance = _Xgs360026fMRSTPPortConfigurationInstance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 1, 1, 1, 2),
    _Xgs360026fMRSTPPortConfigurationInstance_Type()
)
xgs360026fMRSTPPortConfigurationInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortConfigurationInstance.setStatus("current")


class _Xgs360026fMRSTPPortConfigurationPathCost_Type(Integer32):
    """Custom type xgs360026fMRSTPPortConfigurationPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Xgs360026fMRSTPPortConfigurationPathCost_Type.__name__ = "Integer32"
_Xgs360026fMRSTPPortConfigurationPathCost_Object = MibTableColumn
xgs360026fMRSTPPortConfigurationPathCost = _Xgs360026fMRSTPPortConfigurationPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 1, 1, 1, 3),
    _Xgs360026fMRSTPPortConfigurationPathCost_Type()
)
xgs360026fMRSTPPortConfigurationPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortConfigurationPathCost.setStatus("current")


class _Xgs360026fMRSTPPortConfigurationPriority_Type(Integer32):
    """Custom type xgs360026fMRSTPPortConfigurationPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Xgs360026fMRSTPPortConfigurationPriority_Type.__name__ = "Integer32"
_Xgs360026fMRSTPPortConfigurationPriority_Object = MibTableColumn
xgs360026fMRSTPPortConfigurationPriority = _Xgs360026fMRSTPPortConfigurationPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 1, 1, 1, 4),
    _Xgs360026fMRSTPPortConfigurationPriority_Type()
)
xgs360026fMRSTPPortConfigurationPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortConfigurationPriority.setStatus("current")


class _Xgs360026fMRSTPPortConfigurationAdminEdge_Type(Integer32):
    """Custom type xgs360026fMRSTPPortConfigurationAdminEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fMRSTPPortConfigurationAdminEdge_Type.__name__ = "Integer32"
_Xgs360026fMRSTPPortConfigurationAdminEdge_Object = MibTableColumn
xgs360026fMRSTPPortConfigurationAdminEdge = _Xgs360026fMRSTPPortConfigurationAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 1, 1, 1, 5),
    _Xgs360026fMRSTPPortConfigurationAdminEdge_Type()
)
xgs360026fMRSTPPortConfigurationAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortConfigurationAdminEdge.setStatus("current")


class _Xgs360026fMRSTPPortConfigurationAdminP2P_Type(Integer32):
    """Custom type xgs360026fMRSTPPortConfigurationAdminP2P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Xgs360026fMRSTPPortConfigurationAdminP2P_Type.__name__ = "Integer32"
_Xgs360026fMRSTPPortConfigurationAdminP2P_Object = MibTableColumn
xgs360026fMRSTPPortConfigurationAdminP2P = _Xgs360026fMRSTPPortConfigurationAdminP2P_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 1, 1, 1, 6),
    _Xgs360026fMRSTPPortConfigurationAdminP2P_Type()
)
xgs360026fMRSTPPortConfigurationAdminP2P.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortConfigurationAdminP2P.setStatus("current")


class _Xgs360026fMRSTPPortConfigurationMigrateCheck_Type(Integer32):
    """Custom type xgs360026fMRSTPPortConfigurationMigrateCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fMRSTPPortConfigurationMigrateCheck_Type.__name__ = "Integer32"
_Xgs360026fMRSTPPortConfigurationMigrateCheck_Object = MibTableColumn
xgs360026fMRSTPPortConfigurationMigrateCheck = _Xgs360026fMRSTPPortConfigurationMigrateCheck_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 1, 1, 1, 7),
    _Xgs360026fMRSTPPortConfigurationMigrateCheck_Type()
)
xgs360026fMRSTPPortConfigurationMigrateCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortConfigurationMigrateCheck.setStatus("current")
_Xgs360026fMRSTPPortStatus_ObjectIdentity = ObjectIdentity
xgs360026fMRSTPPortStatus = _Xgs360026fMRSTPPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 2)
)
_Xgs360026fMRSTPPortStatusTable_Object = MibTable
xgs360026fMRSTPPortStatusTable = _Xgs360026fMRSTPPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 2, 1)
)
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortStatusTable.setStatus("current")
_Xgs360026fMRSTPPortStatusEntry_Object = MibTableRow
xgs360026fMRSTPPortStatusEntry = _Xgs360026fMRSTPPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 2, 1, 1)
)
xgs360026fMRSTPPortStatusEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fMRSTPPortStatusPort"),
)
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortStatusEntry.setStatus("current")


class _Xgs360026fMRSTPPortStatusPort_Type(Integer32):
    """Custom type xgs360026fMRSTPPortStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fMRSTPPortStatusPort_Type.__name__ = "Integer32"
_Xgs360026fMRSTPPortStatusPort_Object = MibTableColumn
xgs360026fMRSTPPortStatusPort = _Xgs360026fMRSTPPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 2, 1, 1, 1),
    _Xgs360026fMRSTPPortStatusPort_Type()
)
xgs360026fMRSTPPortStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortStatusPort.setStatus("current")
_Xgs360026fMRSTPPortStatusInstance_Type = DisplayString
_Xgs360026fMRSTPPortStatusInstance_Object = MibTableColumn
xgs360026fMRSTPPortStatusInstance = _Xgs360026fMRSTPPortStatusInstance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 2, 1, 1, 2),
    _Xgs360026fMRSTPPortStatusInstance_Type()
)
xgs360026fMRSTPPortStatusInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortStatusInstance.setStatus("current")
_Xgs360026fMRSTPPortStatusState_Type = DisplayString
_Xgs360026fMRSTPPortStatusState_Object = MibTableColumn
xgs360026fMRSTPPortStatusState = _Xgs360026fMRSTPPortStatusState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 2, 1, 1, 3),
    _Xgs360026fMRSTPPortStatusState_Type()
)
xgs360026fMRSTPPortStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortStatusState.setStatus("current")
_Xgs360026fMRSTPPortStatusRole_Type = DisplayString
_Xgs360026fMRSTPPortStatusRole_Object = MibTableColumn
xgs360026fMRSTPPortStatusRole = _Xgs360026fMRSTPPortStatusRole_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 2, 1, 1, 4),
    _Xgs360026fMRSTPPortStatusRole_Type()
)
xgs360026fMRSTPPortStatusRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortStatusRole.setStatus("current")


class _Xgs360026fMRSTPPortStatusPathCost_Type(Integer32):
    """Custom type xgs360026fMRSTPPortStatusPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Xgs360026fMRSTPPortStatusPathCost_Type.__name__ = "Integer32"
_Xgs360026fMRSTPPortStatusPathCost_Object = MibTableColumn
xgs360026fMRSTPPortStatusPathCost = _Xgs360026fMRSTPPortStatusPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 2, 1, 1, 5),
    _Xgs360026fMRSTPPortStatusPathCost_Type()
)
xgs360026fMRSTPPortStatusPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortStatusPathCost.setStatus("current")


class _Xgs360026fMRSTPPortStatusPathCostConfig_Type(Integer32):
    """Custom type xgs360026fMRSTPPortStatusPathCostConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Xgs360026fMRSTPPortStatusPathCostConfig_Type.__name__ = "Integer32"
_Xgs360026fMRSTPPortStatusPathCostConfig_Object = MibTableColumn
xgs360026fMRSTPPortStatusPathCostConfig = _Xgs360026fMRSTPPortStatusPathCostConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 2, 1, 1, 6),
    _Xgs360026fMRSTPPortStatusPathCostConfig_Type()
)
xgs360026fMRSTPPortStatusPathCostConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortStatusPathCostConfig.setStatus("current")


class _Xgs360026fMRSTPPortStatusPriority_Type(Integer32):
    """Custom type xgs360026fMRSTPPortStatusPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Xgs360026fMRSTPPortStatusPriority_Type.__name__ = "Integer32"
_Xgs360026fMRSTPPortStatusPriority_Object = MibTableColumn
xgs360026fMRSTPPortStatusPriority = _Xgs360026fMRSTPPortStatusPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 2, 1, 1, 7),
    _Xgs360026fMRSTPPortStatusPriority_Type()
)
xgs360026fMRSTPPortStatusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortStatusPriority.setStatus("current")
_Xgs360026fMRSTPPortStatusAdminEdge_Type = DisplayString
_Xgs360026fMRSTPPortStatusAdminEdge_Object = MibTableColumn
xgs360026fMRSTPPortStatusAdminEdge = _Xgs360026fMRSTPPortStatusAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 2, 1, 1, 8),
    _Xgs360026fMRSTPPortStatusAdminEdge_Type()
)
xgs360026fMRSTPPortStatusAdminEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortStatusAdminEdge.setStatus("current")
_Xgs360026fMRSTPPortStatusAdminP2P_Type = DisplayString
_Xgs360026fMRSTPPortStatusAdminP2P_Object = MibTableColumn
xgs360026fMRSTPPortStatusAdminP2P = _Xgs360026fMRSTPPortStatusAdminP2P_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 2, 11, 2, 2, 1, 1, 9),
    _Xgs360026fMRSTPPortStatusAdminP2P_Type()
)
xgs360026fMRSTPPortStatusAdminP2P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fMRSTPPortStatusAdminP2P.setStatus("current")
_Xgs360026fSecurity_ObjectIdentity = ObjectIdentity
xgs360026fSecurity = _Xgs360026fSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3)
)
_Xgs360026fIPSourceGuard_ObjectIdentity = ObjectIdentity
xgs360026fIPSourceGuard = _Xgs360026fIPSourceGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1)
)
_Xgs360026fIPSourceGuardConf_ObjectIdentity = ObjectIdentity
xgs360026fIPSourceGuardConf = _Xgs360026fIPSourceGuardConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 1)
)


class _Xgs360026fIPSourceGuardMode_Type(Integer32):
    """Custom type xgs360026fIPSourceGuardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fIPSourceGuardMode_Type.__name__ = "Integer32"
_Xgs360026fIPSourceGuardMode_Object = MibScalar
xgs360026fIPSourceGuardMode = _Xgs360026fIPSourceGuardMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 1, 1),
    _Xgs360026fIPSourceGuardMode_Type()
)
xgs360026fIPSourceGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardMode.setStatus("current")
_Xgs360026fIPSourceGuardPortConfigTable_Object = MibTable
xgs360026fIPSourceGuardPortConfigTable = _Xgs360026fIPSourceGuardPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardPortConfigTable.setStatus("current")
_Xgs360026fIPSourceGuardPortConfigEntry_Object = MibTableRow
xgs360026fIPSourceGuardPortConfigEntry = _Xgs360026fIPSourceGuardPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 1, 2, 1)
)
xgs360026fIPSourceGuardPortConfigEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fIPSourceGuardPortConfigPort"),
)
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardPortConfigEntry.setStatus("current")


class _Xgs360026fIPSourceGuardPortConfigPort_Type(Integer32):
    """Custom type xgs360026fIPSourceGuardPortConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fIPSourceGuardPortConfigPort_Type.__name__ = "Integer32"
_Xgs360026fIPSourceGuardPortConfigPort_Object = MibTableColumn
xgs360026fIPSourceGuardPortConfigPort = _Xgs360026fIPSourceGuardPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 1, 2, 1, 1),
    _Xgs360026fIPSourceGuardPortConfigPort_Type()
)
xgs360026fIPSourceGuardPortConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardPortConfigPort.setStatus("current")


class _Xgs360026fIPSourceGuardPortConfigMode_Type(Integer32):
    """Custom type xgs360026fIPSourceGuardPortConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fIPSourceGuardPortConfigMode_Type.__name__ = "Integer32"
_Xgs360026fIPSourceGuardPortConfigMode_Object = MibTableColumn
xgs360026fIPSourceGuardPortConfigMode = _Xgs360026fIPSourceGuardPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 1, 2, 1, 2),
    _Xgs360026fIPSourceGuardPortConfigMode_Type()
)
xgs360026fIPSourceGuardPortConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardPortConfigMode.setStatus("current")


class _Xgs360026fIPSourceGuardPortMaxDynamicClients_Type(Integer32):
    """Custom type xgs360026fIPSourceGuardPortMaxDynamicClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(99, 99),
    )


_Xgs360026fIPSourceGuardPortMaxDynamicClients_Type.__name__ = "Integer32"
_Xgs360026fIPSourceGuardPortMaxDynamicClients_Object = MibTableColumn
xgs360026fIPSourceGuardPortMaxDynamicClients = _Xgs360026fIPSourceGuardPortMaxDynamicClients_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 1, 2, 1, 3),
    _Xgs360026fIPSourceGuardPortMaxDynamicClients_Type()
)
xgs360026fIPSourceGuardPortMaxDynamicClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardPortMaxDynamicClients.setStatus("current")
_Xgs360026fIPSourceGuardStatic_ObjectIdentity = ObjectIdentity
xgs360026fIPSourceGuardStatic = _Xgs360026fIPSourceGuardStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 2)
)


class _Xgs360026fIPSourceGuardStaticCreate_Type(Integer32):
    """Custom type xgs360026fIPSourceGuardStaticCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fIPSourceGuardStaticCreate_Type.__name__ = "Integer32"
_Xgs360026fIPSourceGuardStaticCreate_Object = MibScalar
xgs360026fIPSourceGuardStaticCreate = _Xgs360026fIPSourceGuardStaticCreate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 2, 1),
    _Xgs360026fIPSourceGuardStaticCreate_Type()
)
xgs360026fIPSourceGuardStaticCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardStaticCreate.setStatus("current")
_Xgs360026fIPSourceGuardStaticTable_Object = MibTable
xgs360026fIPSourceGuardStaticTable = _Xgs360026fIPSourceGuardStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardStaticTable.setStatus("current")
_Xgs360026fIPSourceGuardStaticEntry_Object = MibTableRow
xgs360026fIPSourceGuardStaticEntry = _Xgs360026fIPSourceGuardStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 2, 2, 1)
)
xgs360026fIPSourceGuardStaticEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fIPSourceGuardStaticIndex"),
)
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardStaticEntry.setStatus("current")


class _Xgs360026fIPSourceGuardStaticIndex_Type(Integer32):
    """Custom type xgs360026fIPSourceGuardStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_Xgs360026fIPSourceGuardStaticIndex_Type.__name__ = "Integer32"
_Xgs360026fIPSourceGuardStaticIndex_Object = MibTableColumn
xgs360026fIPSourceGuardStaticIndex = _Xgs360026fIPSourceGuardStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 2, 2, 1, 1),
    _Xgs360026fIPSourceGuardStaticIndex_Type()
)
xgs360026fIPSourceGuardStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardStaticIndex.setStatus("current")


class _Xgs360026fIPSourceGuardStaticPort_Type(Integer32):
    """Custom type xgs360026fIPSourceGuardStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fIPSourceGuardStaticPort_Type.__name__ = "Integer32"
_Xgs360026fIPSourceGuardStaticPort_Object = MibTableColumn
xgs360026fIPSourceGuardStaticPort = _Xgs360026fIPSourceGuardStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 2, 2, 1, 2),
    _Xgs360026fIPSourceGuardStaticPort_Type()
)
xgs360026fIPSourceGuardStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardStaticPort.setStatus("current")


class _Xgs360026fIPSourceGuardStaticVLANId_Type(Integer32):
    """Custom type xgs360026fIPSourceGuardStaticVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Xgs360026fIPSourceGuardStaticVLANId_Type.__name__ = "Integer32"
_Xgs360026fIPSourceGuardStaticVLANId_Object = MibTableColumn
xgs360026fIPSourceGuardStaticVLANId = _Xgs360026fIPSourceGuardStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 2, 2, 1, 3),
    _Xgs360026fIPSourceGuardStaticVLANId_Type()
)
xgs360026fIPSourceGuardStaticVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardStaticVLANId.setStatus("current")
_Xgs360026fIPSourceGuardStaticIPAddress_Type = IpAddress
_Xgs360026fIPSourceGuardStaticIPAddress_Object = MibTableColumn
xgs360026fIPSourceGuardStaticIPAddress = _Xgs360026fIPSourceGuardStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 2, 2, 1, 4),
    _Xgs360026fIPSourceGuardStaticIPAddress_Type()
)
xgs360026fIPSourceGuardStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardStaticIPAddress.setStatus("current")
_Xgs360026fIPSourceGuardStaticMACAddress_Type = MacAddress
_Xgs360026fIPSourceGuardStaticMACAddress_Object = MibTableColumn
xgs360026fIPSourceGuardStaticMACAddress = _Xgs360026fIPSourceGuardStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 2, 2, 1, 5),
    _Xgs360026fIPSourceGuardStaticMACAddress_Type()
)
xgs360026fIPSourceGuardStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardStaticMACAddress.setStatus("current")


class _Xgs360026fIPSourceGuardStaticRowStatus_Type(Integer32):
    """Custom type xgs360026fIPSourceGuardStaticRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Xgs360026fIPSourceGuardStaticRowStatus_Type.__name__ = "Integer32"
_Xgs360026fIPSourceGuardStaticRowStatus_Object = MibTableColumn
xgs360026fIPSourceGuardStaticRowStatus = _Xgs360026fIPSourceGuardStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 2, 2, 1, 6),
    _Xgs360026fIPSourceGuardStaticRowStatus_Type()
)
xgs360026fIPSourceGuardStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardStaticRowStatus.setStatus("current")
_Xgs360026fIPSourceGuardDynamicTable_Object = MibTable
xgs360026fIPSourceGuardDynamicTable = _Xgs360026fIPSourceGuardDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 3)
)
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardDynamicTable.setStatus("current")
_Xgs360026fIPSourceGuardDynamicEntry_Object = MibTableRow
xgs360026fIPSourceGuardDynamicEntry = _Xgs360026fIPSourceGuardDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 3, 1)
)
xgs360026fIPSourceGuardDynamicEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fIPSourceGuardDynamicIndex"),
)
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardDynamicEntry.setStatus("current")


class _Xgs360026fIPSourceGuardDynamicIndex_Type(Integer32):
    """Custom type xgs360026fIPSourceGuardDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fIPSourceGuardDynamicIndex_Type.__name__ = "Integer32"
_Xgs360026fIPSourceGuardDynamicIndex_Object = MibTableColumn
xgs360026fIPSourceGuardDynamicIndex = _Xgs360026fIPSourceGuardDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 3, 1, 1),
    _Xgs360026fIPSourceGuardDynamicIndex_Type()
)
xgs360026fIPSourceGuardDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardDynamicIndex.setStatus("current")


class _Xgs360026fIPSourceGuardDynamicPort_Type(Integer32):
    """Custom type xgs360026fIPSourceGuardDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Xgs360026fIPSourceGuardDynamicPort_Type.__name__ = "Integer32"
_Xgs360026fIPSourceGuardDynamicPort_Object = MibTableColumn
xgs360026fIPSourceGuardDynamicPort = _Xgs360026fIPSourceGuardDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 3, 1, 2),
    _Xgs360026fIPSourceGuardDynamicPort_Type()
)
xgs360026fIPSourceGuardDynamicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardDynamicPort.setStatus("current")


class _Xgs360026fIPSourceGuardDynamicVLANId_Type(Integer32):
    """Custom type xgs360026fIPSourceGuardDynamicVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Xgs360026fIPSourceGuardDynamicVLANId_Type.__name__ = "Integer32"
_Xgs360026fIPSourceGuardDynamicVLANId_Object = MibTableColumn
xgs360026fIPSourceGuardDynamicVLANId = _Xgs360026fIPSourceGuardDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 3, 1, 3),
    _Xgs360026fIPSourceGuardDynamicVLANId_Type()
)
xgs360026fIPSourceGuardDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardDynamicVLANId.setStatus("current")
_Xgs360026fIPSourceGuardDynamicIPAddress_Type = IpAddress
_Xgs360026fIPSourceGuardDynamicIPAddress_Object = MibTableColumn
xgs360026fIPSourceGuardDynamicIPAddress = _Xgs360026fIPSourceGuardDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 3, 1, 4),
    _Xgs360026fIPSourceGuardDynamicIPAddress_Type()
)
xgs360026fIPSourceGuardDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardDynamicIPAddress.setStatus("current")
_Xgs360026fIPSourceGuardDynamicMACAddress_Type = MacAddress
_Xgs360026fIPSourceGuardDynamicMACAddress_Object = MibTableColumn
xgs360026fIPSourceGuardDynamicMACAddress = _Xgs360026fIPSourceGuardDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 1, 3, 1, 5),
    _Xgs360026fIPSourceGuardDynamicMACAddress_Type()
)
xgs360026fIPSourceGuardDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fIPSourceGuardDynamicMACAddress.setStatus("current")
_Xgs360026fARPInspection_ObjectIdentity = ObjectIdentity
xgs360026fARPInspection = _Xgs360026fARPInspection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2)
)
_Xgs360026fARPInspectionConf_ObjectIdentity = ObjectIdentity
xgs360026fARPInspectionConf = _Xgs360026fARPInspectionConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 1)
)


class _Xgs360026fARPInspectionConfMode_Type(Integer32):
    """Custom type xgs360026fARPInspectionConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fARPInspectionConfMode_Type.__name__ = "Integer32"
_Xgs360026fARPInspectionConfMode_Object = MibScalar
xgs360026fARPInspectionConfMode = _Xgs360026fARPInspectionConfMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 1, 1),
    _Xgs360026fARPInspectionConfMode_Type()
)
xgs360026fARPInspectionConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fARPInspectionConfMode.setStatus("current")
_Xgs360026fARPInspectionConfTable_Object = MibTable
xgs360026fARPInspectionConfTable = _Xgs360026fARPInspectionConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    xgs360026fARPInspectionConfTable.setStatus("current")
_Xgs360026fARPInspectionConfEntry_Object = MibTableRow
xgs360026fARPInspectionConfEntry = _Xgs360026fARPInspectionConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 1, 2, 1)
)
xgs360026fARPInspectionConfEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fARPInspectionConfPortIndex"),
)
if mibBuilder.loadTexts:
    xgs360026fARPInspectionConfEntry.setStatus("current")


class _Xgs360026fARPInspectionConfPortIndex_Type(Integer32):
    """Custom type xgs360026fARPInspectionConfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fARPInspectionConfPortIndex_Type.__name__ = "Integer32"
_Xgs360026fARPInspectionConfPortIndex_Object = MibTableColumn
xgs360026fARPInspectionConfPortIndex = _Xgs360026fARPInspectionConfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 1, 2, 1, 1),
    _Xgs360026fARPInspectionConfPortIndex_Type()
)
xgs360026fARPInspectionConfPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fARPInspectionConfPortIndex.setStatus("current")


class _Xgs360026fARPInspectionConfPortMode_Type(Integer32):
    """Custom type xgs360026fARPInspectionConfPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fARPInspectionConfPortMode_Type.__name__ = "Integer32"
_Xgs360026fARPInspectionConfPortMode_Object = MibTableColumn
xgs360026fARPInspectionConfPortMode = _Xgs360026fARPInspectionConfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 1, 2, 1, 2),
    _Xgs360026fARPInspectionConfPortMode_Type()
)
xgs360026fARPInspectionConfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fARPInspectionConfPortMode.setStatus("current")
_Xgs360026fARPInspectionStatic_ObjectIdentity = ObjectIdentity
xgs360026fARPInspectionStatic = _Xgs360026fARPInspectionStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 2)
)


class _Xgs360026fARPInspectionStaticCreate_Type(Integer32):
    """Custom type xgs360026fARPInspectionStaticCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fARPInspectionStaticCreate_Type.__name__ = "Integer32"
_Xgs360026fARPInspectionStaticCreate_Object = MibScalar
xgs360026fARPInspectionStaticCreate = _Xgs360026fARPInspectionStaticCreate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 2, 1),
    _Xgs360026fARPInspectionStaticCreate_Type()
)
xgs360026fARPInspectionStaticCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fARPInspectionStaticCreate.setStatus("current")
_Xgs360026fARPInspectionStaticTable_Object = MibTable
xgs360026fARPInspectionStaticTable = _Xgs360026fARPInspectionStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    xgs360026fARPInspectionStaticTable.setStatus("current")
_Xgs360026fARPInspectionStaticEntry_Object = MibTableRow
xgs360026fARPInspectionStaticEntry = _Xgs360026fARPInspectionStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 2, 2, 1)
)
xgs360026fARPInspectionStaticEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fARPInspectionStaticIndex"),
)
if mibBuilder.loadTexts:
    xgs360026fARPInspectionStaticEntry.setStatus("current")


class _Xgs360026fARPInspectionStaticIndex_Type(Integer32):
    """Custom type xgs360026fARPInspectionStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fARPInspectionStaticIndex_Type.__name__ = "Integer32"
_Xgs360026fARPInspectionStaticIndex_Object = MibTableColumn
xgs360026fARPInspectionStaticIndex = _Xgs360026fARPInspectionStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 2, 2, 1, 1),
    _Xgs360026fARPInspectionStaticIndex_Type()
)
xgs360026fARPInspectionStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fARPInspectionStaticIndex.setStatus("current")


class _Xgs360026fARPInspectionStaticPort_Type(Integer32):
    """Custom type xgs360026fARPInspectionStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fARPInspectionStaticPort_Type.__name__ = "Integer32"
_Xgs360026fARPInspectionStaticPort_Object = MibTableColumn
xgs360026fARPInspectionStaticPort = _Xgs360026fARPInspectionStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 2, 2, 1, 2),
    _Xgs360026fARPInspectionStaticPort_Type()
)
xgs360026fARPInspectionStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fARPInspectionStaticPort.setStatus("current")


class _Xgs360026fARPInspectionStaticVLANId_Type(Integer32):
    """Custom type xgs360026fARPInspectionStaticVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Xgs360026fARPInspectionStaticVLANId_Type.__name__ = "Integer32"
_Xgs360026fARPInspectionStaticVLANId_Object = MibTableColumn
xgs360026fARPInspectionStaticVLANId = _Xgs360026fARPInspectionStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 2, 2, 1, 3),
    _Xgs360026fARPInspectionStaticVLANId_Type()
)
xgs360026fARPInspectionStaticVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fARPInspectionStaticVLANId.setStatus("current")
_Xgs360026fARPInspectionStaticIPAddress_Type = IpAddress
_Xgs360026fARPInspectionStaticIPAddress_Object = MibTableColumn
xgs360026fARPInspectionStaticIPAddress = _Xgs360026fARPInspectionStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 2, 2, 1, 4),
    _Xgs360026fARPInspectionStaticIPAddress_Type()
)
xgs360026fARPInspectionStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fARPInspectionStaticIPAddress.setStatus("current")
_Xgs360026fARPInspectionStaticMACAddress_Type = MacAddress
_Xgs360026fARPInspectionStaticMACAddress_Object = MibTableColumn
xgs360026fARPInspectionStaticMACAddress = _Xgs360026fARPInspectionStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 2, 2, 1, 5),
    _Xgs360026fARPInspectionStaticMACAddress_Type()
)
xgs360026fARPInspectionStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fARPInspectionStaticMACAddress.setStatus("current")


class _Xgs360026fARPInspectionStaticRowStatus_Type(Integer32):
    """Custom type xgs360026fARPInspectionStaticRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Xgs360026fARPInspectionStaticRowStatus_Type.__name__ = "Integer32"
_Xgs360026fARPInspectionStaticRowStatus_Object = MibTableColumn
xgs360026fARPInspectionStaticRowStatus = _Xgs360026fARPInspectionStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 2, 2, 1, 6),
    _Xgs360026fARPInspectionStaticRowStatus_Type()
)
xgs360026fARPInspectionStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fARPInspectionStaticRowStatus.setStatus("current")
_Xgs360026fARPInspectionDynamicTable_Object = MibTable
xgs360026fARPInspectionDynamicTable = _Xgs360026fARPInspectionDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 3)
)
if mibBuilder.loadTexts:
    xgs360026fARPInspectionDynamicTable.setStatus("current")
_Xgs360026fARPInspectionDynamicEntry_Object = MibTableRow
xgs360026fARPInspectionDynamicEntry = _Xgs360026fARPInspectionDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 3, 1)
)
xgs360026fARPInspectionDynamicEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fARPInspectionDynamicIndex"),
)
if mibBuilder.loadTexts:
    xgs360026fARPInspectionDynamicEntry.setStatus("current")


class _Xgs360026fARPInspectionDynamicIndex_Type(Integer32):
    """Custom type xgs360026fARPInspectionDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fARPInspectionDynamicIndex_Type.__name__ = "Integer32"
_Xgs360026fARPInspectionDynamicIndex_Object = MibTableColumn
xgs360026fARPInspectionDynamicIndex = _Xgs360026fARPInspectionDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 3, 1, 1),
    _Xgs360026fARPInspectionDynamicIndex_Type()
)
xgs360026fARPInspectionDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fARPInspectionDynamicIndex.setStatus("current")


class _Xgs360026fARPInspectionDynamicPort_Type(Integer32):
    """Custom type xgs360026fARPInspectionDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fARPInspectionDynamicPort_Type.__name__ = "Integer32"
_Xgs360026fARPInspectionDynamicPort_Object = MibTableColumn
xgs360026fARPInspectionDynamicPort = _Xgs360026fARPInspectionDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 3, 1, 2),
    _Xgs360026fARPInspectionDynamicPort_Type()
)
xgs360026fARPInspectionDynamicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fARPInspectionDynamicPort.setStatus("current")


class _Xgs360026fARPInspectionDynamicVLANId_Type(Integer32):
    """Custom type xgs360026fARPInspectionDynamicVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Xgs360026fARPInspectionDynamicVLANId_Type.__name__ = "Integer32"
_Xgs360026fARPInspectionDynamicVLANId_Object = MibTableColumn
xgs360026fARPInspectionDynamicVLANId = _Xgs360026fARPInspectionDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 3, 1, 3),
    _Xgs360026fARPInspectionDynamicVLANId_Type()
)
xgs360026fARPInspectionDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fARPInspectionDynamicVLANId.setStatus("current")
_Xgs360026fARPInspectionDynamicIPAddress_Type = IpAddress
_Xgs360026fARPInspectionDynamicIPAddress_Object = MibTableColumn
xgs360026fARPInspectionDynamicIPAddress = _Xgs360026fARPInspectionDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 3, 1, 4),
    _Xgs360026fARPInspectionDynamicIPAddress_Type()
)
xgs360026fARPInspectionDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fARPInspectionDynamicIPAddress.setStatus("current")
_Xgs360026fARPInspectionDynamicMACAddress_Type = MacAddress
_Xgs360026fARPInspectionDynamicMACAddress_Object = MibTableColumn
xgs360026fARPInspectionDynamicMACAddress = _Xgs360026fARPInspectionDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 2, 3, 1, 5),
    _Xgs360026fARPInspectionDynamicMACAddress_Type()
)
xgs360026fARPInspectionDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fARPInspectionDynamicMACAddress.setStatus("current")
_Xgs360026fDHCPSnooping_ObjectIdentity = ObjectIdentity
xgs360026fDHCPSnooping = _Xgs360026fDHCPSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3)
)
_Xgs360026fDHCPSnoopingConf_ObjectIdentity = ObjectIdentity
xgs360026fDHCPSnoopingConf = _Xgs360026fDHCPSnoopingConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 1)
)


class _Xgs360026fDHCPSnoopingMode_Type(Integer32):
    """Custom type xgs360026fDHCPSnoopingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fDHCPSnoopingMode_Type.__name__ = "Integer32"
_Xgs360026fDHCPSnoopingMode_Object = MibScalar
xgs360026fDHCPSnoopingMode = _Xgs360026fDHCPSnoopingMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 1, 1),
    _Xgs360026fDHCPSnoopingMode_Type()
)
xgs360026fDHCPSnoopingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingMode.setStatus("current")
_Xgs360026fDHCPSnoopingPortModeConfigurationTable_Object = MibTable
xgs360026fDHCPSnoopingPortModeConfigurationTable = _Xgs360026fDHCPSnoopingPortModeConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingPortModeConfigurationTable.setStatus("current")
_Xgs360026fDHCPSnoopingPortModeConfigurationEntry_Object = MibTableRow
xgs360026fDHCPSnoopingPortModeConfigurationEntry = _Xgs360026fDHCPSnoopingPortModeConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 1, 2, 1)
)
xgs360026fDHCPSnoopingPortModeConfigurationEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fDHCPSnoopingPortModeConfigurationPort"),
)
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingPortModeConfigurationEntry.setStatus("current")


class _Xgs360026fDHCPSnoopingPortModeConfigurationPort_Type(Integer32):
    """Custom type xgs360026fDHCPSnoopingPortModeConfigurationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fDHCPSnoopingPortModeConfigurationPort_Type.__name__ = "Integer32"
_Xgs360026fDHCPSnoopingPortModeConfigurationPort_Object = MibTableColumn
xgs360026fDHCPSnoopingPortModeConfigurationPort = _Xgs360026fDHCPSnoopingPortModeConfigurationPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 1, 2, 1, 1),
    _Xgs360026fDHCPSnoopingPortModeConfigurationPort_Type()
)
xgs360026fDHCPSnoopingPortModeConfigurationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingPortModeConfigurationPort.setStatus("current")


class _Xgs360026fDHCPSnoopingPortModeConfigurationMode_Type(Integer32):
    """Custom type xgs360026fDHCPSnoopingPortModeConfigurationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fDHCPSnoopingPortModeConfigurationMode_Type.__name__ = "Integer32"
_Xgs360026fDHCPSnoopingPortModeConfigurationMode_Object = MibTableColumn
xgs360026fDHCPSnoopingPortModeConfigurationMode = _Xgs360026fDHCPSnoopingPortModeConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 1, 2, 1, 2),
    _Xgs360026fDHCPSnoopingPortModeConfigurationMode_Type()
)
xgs360026fDHCPSnoopingPortModeConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingPortModeConfigurationMode.setStatus("current")
_Xgs360026fDHCPSnoopingStatisticsTable_Object = MibTable
xgs360026fDHCPSnoopingStatisticsTable = _Xgs360026fDHCPSnoopingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2)
)
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingStatisticsTable.setStatus("current")
_Xgs360026fDHCPSnoopingStatisticsEntry_Object = MibTableRow
xgs360026fDHCPSnoopingStatisticsEntry = _Xgs360026fDHCPSnoopingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1)
)
xgs360026fDHCPSnoopingStatisticsEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fDHCPSnoopingStatisticsPort"),
)
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingStatisticsEntry.setStatus("current")


class _Xgs360026fDHCPSnoopingStatisticsPort_Type(Integer32):
    """Custom type xgs360026fDHCPSnoopingStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fDHCPSnoopingStatisticsPort_Type.__name__ = "Integer32"
_Xgs360026fDHCPSnoopingStatisticsPort_Object = MibTableColumn
xgs360026fDHCPSnoopingStatisticsPort = _Xgs360026fDHCPSnoopingStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 1),
    _Xgs360026fDHCPSnoopingStatisticsPort_Type()
)
xgs360026fDHCPSnoopingStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingStatisticsPort.setStatus("current")


class _Xgs360026fDHCPSnoopingStatisticsClear_Type(Integer32):
    """Custom type xgs360026fDHCPSnoopingStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fDHCPSnoopingStatisticsClear_Type.__name__ = "Integer32"
_Xgs360026fDHCPSnoopingStatisticsClear_Object = MibTableColumn
xgs360026fDHCPSnoopingStatisticsClear = _Xgs360026fDHCPSnoopingStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 2),
    _Xgs360026fDHCPSnoopingStatisticsClear_Type()
)
xgs360026fDHCPSnoopingStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingStatisticsClear.setStatus("current")
_Xgs360026fDHCPSnoopingRxDiscover_Type = Counter32
_Xgs360026fDHCPSnoopingRxDiscover_Object = MibTableColumn
xgs360026fDHCPSnoopingRxDiscover = _Xgs360026fDHCPSnoopingRxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 3),
    _Xgs360026fDHCPSnoopingRxDiscover_Type()
)
xgs360026fDHCPSnoopingRxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingRxDiscover.setStatus("current")
_Xgs360026fDHCPSnoopingRxOffer_Type = Counter32
_Xgs360026fDHCPSnoopingRxOffer_Object = MibTableColumn
xgs360026fDHCPSnoopingRxOffer = _Xgs360026fDHCPSnoopingRxOffer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 4),
    _Xgs360026fDHCPSnoopingRxOffer_Type()
)
xgs360026fDHCPSnoopingRxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingRxOffer.setStatus("current")
_Xgs360026fDHCPSnoopingRxRequest_Type = Counter32
_Xgs360026fDHCPSnoopingRxRequest_Object = MibTableColumn
xgs360026fDHCPSnoopingRxRequest = _Xgs360026fDHCPSnoopingRxRequest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 5),
    _Xgs360026fDHCPSnoopingRxRequest_Type()
)
xgs360026fDHCPSnoopingRxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingRxRequest.setStatus("current")
_Xgs360026fDHCPSnoopingRxDecline_Type = Counter32
_Xgs360026fDHCPSnoopingRxDecline_Object = MibTableColumn
xgs360026fDHCPSnoopingRxDecline = _Xgs360026fDHCPSnoopingRxDecline_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 6),
    _Xgs360026fDHCPSnoopingRxDecline_Type()
)
xgs360026fDHCPSnoopingRxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingRxDecline.setStatus("current")
_Xgs360026fDHCPSnoopingRxACK_Type = Counter32
_Xgs360026fDHCPSnoopingRxACK_Object = MibTableColumn
xgs360026fDHCPSnoopingRxACK = _Xgs360026fDHCPSnoopingRxACK_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 7),
    _Xgs360026fDHCPSnoopingRxACK_Type()
)
xgs360026fDHCPSnoopingRxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingRxACK.setStatus("current")
_Xgs360026fDHCPSnoopingRxNAK_Type = Counter32
_Xgs360026fDHCPSnoopingRxNAK_Object = MibTableColumn
xgs360026fDHCPSnoopingRxNAK = _Xgs360026fDHCPSnoopingRxNAK_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 8),
    _Xgs360026fDHCPSnoopingRxNAK_Type()
)
xgs360026fDHCPSnoopingRxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingRxNAK.setStatus("current")
_Xgs360026fDHCPSnoopingRxRelease_Type = Counter32
_Xgs360026fDHCPSnoopingRxRelease_Object = MibTableColumn
xgs360026fDHCPSnoopingRxRelease = _Xgs360026fDHCPSnoopingRxRelease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 9),
    _Xgs360026fDHCPSnoopingRxRelease_Type()
)
xgs360026fDHCPSnoopingRxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingRxRelease.setStatus("current")
_Xgs360026fDHCPSnoopingRxInform_Type = Counter32
_Xgs360026fDHCPSnoopingRxInform_Object = MibTableColumn
xgs360026fDHCPSnoopingRxInform = _Xgs360026fDHCPSnoopingRxInform_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 10),
    _Xgs360026fDHCPSnoopingRxInform_Type()
)
xgs360026fDHCPSnoopingRxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingRxInform.setStatus("current")
_Xgs360026fDHCPSnoopingRxLeaseQuery_Type = Counter32
_Xgs360026fDHCPSnoopingRxLeaseQuery_Object = MibTableColumn
xgs360026fDHCPSnoopingRxLeaseQuery = _Xgs360026fDHCPSnoopingRxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 11),
    _Xgs360026fDHCPSnoopingRxLeaseQuery_Type()
)
xgs360026fDHCPSnoopingRxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingRxLeaseQuery.setStatus("current")
_Xgs360026fDHCPSnoopingRxLeaseUnassigned_Type = Counter32
_Xgs360026fDHCPSnoopingRxLeaseUnassigned_Object = MibTableColumn
xgs360026fDHCPSnoopingRxLeaseUnassigned = _Xgs360026fDHCPSnoopingRxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 12),
    _Xgs360026fDHCPSnoopingRxLeaseUnassigned_Type()
)
xgs360026fDHCPSnoopingRxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingRxLeaseUnassigned.setStatus("current")
_Xgs360026fDHCPSnoopingRxLeaseUnknown_Type = Counter32
_Xgs360026fDHCPSnoopingRxLeaseUnknown_Object = MibTableColumn
xgs360026fDHCPSnoopingRxLeaseUnknown = _Xgs360026fDHCPSnoopingRxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 13),
    _Xgs360026fDHCPSnoopingRxLeaseUnknown_Type()
)
xgs360026fDHCPSnoopingRxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingRxLeaseUnknown.setStatus("current")
_Xgs360026fDHCPSnoopingRxLeaseActive_Type = Counter32
_Xgs360026fDHCPSnoopingRxLeaseActive_Object = MibTableColumn
xgs360026fDHCPSnoopingRxLeaseActive = _Xgs360026fDHCPSnoopingRxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 14),
    _Xgs360026fDHCPSnoopingRxLeaseActive_Type()
)
xgs360026fDHCPSnoopingRxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingRxLeaseActive.setStatus("current")
_Xgs360026fDHCPSnoopingTxDiscover_Type = Counter32
_Xgs360026fDHCPSnoopingTxDiscover_Object = MibTableColumn
xgs360026fDHCPSnoopingTxDiscover = _Xgs360026fDHCPSnoopingTxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 15),
    _Xgs360026fDHCPSnoopingTxDiscover_Type()
)
xgs360026fDHCPSnoopingTxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingTxDiscover.setStatus("current")
_Xgs360026fDHCPSnoopingTxOffer_Type = Counter32
_Xgs360026fDHCPSnoopingTxOffer_Object = MibTableColumn
xgs360026fDHCPSnoopingTxOffer = _Xgs360026fDHCPSnoopingTxOffer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 16),
    _Xgs360026fDHCPSnoopingTxOffer_Type()
)
xgs360026fDHCPSnoopingTxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingTxOffer.setStatus("current")
_Xgs360026fDHCPSnoopingTxRequest_Type = Counter32
_Xgs360026fDHCPSnoopingTxRequest_Object = MibTableColumn
xgs360026fDHCPSnoopingTxRequest = _Xgs360026fDHCPSnoopingTxRequest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 17),
    _Xgs360026fDHCPSnoopingTxRequest_Type()
)
xgs360026fDHCPSnoopingTxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingTxRequest.setStatus("current")
_Xgs360026fDHCPSnoopingTxDecline_Type = Counter32
_Xgs360026fDHCPSnoopingTxDecline_Object = MibTableColumn
xgs360026fDHCPSnoopingTxDecline = _Xgs360026fDHCPSnoopingTxDecline_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 18),
    _Xgs360026fDHCPSnoopingTxDecline_Type()
)
xgs360026fDHCPSnoopingTxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingTxDecline.setStatus("current")
_Xgs360026fDHCPSnoopingTxACK_Type = Counter32
_Xgs360026fDHCPSnoopingTxACK_Object = MibTableColumn
xgs360026fDHCPSnoopingTxACK = _Xgs360026fDHCPSnoopingTxACK_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 19),
    _Xgs360026fDHCPSnoopingTxACK_Type()
)
xgs360026fDHCPSnoopingTxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingTxACK.setStatus("current")
_Xgs360026fDHCPSnoopingTxNAK_Type = Counter32
_Xgs360026fDHCPSnoopingTxNAK_Object = MibTableColumn
xgs360026fDHCPSnoopingTxNAK = _Xgs360026fDHCPSnoopingTxNAK_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 20),
    _Xgs360026fDHCPSnoopingTxNAK_Type()
)
xgs360026fDHCPSnoopingTxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingTxNAK.setStatus("current")
_Xgs360026fDHCPSnoopingTxRelease_Type = Counter32
_Xgs360026fDHCPSnoopingTxRelease_Object = MibTableColumn
xgs360026fDHCPSnoopingTxRelease = _Xgs360026fDHCPSnoopingTxRelease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 21),
    _Xgs360026fDHCPSnoopingTxRelease_Type()
)
xgs360026fDHCPSnoopingTxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingTxRelease.setStatus("current")
_Xgs360026fDHCPSnoopingTxInform_Type = Counter32
_Xgs360026fDHCPSnoopingTxInform_Object = MibTableColumn
xgs360026fDHCPSnoopingTxInform = _Xgs360026fDHCPSnoopingTxInform_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 22),
    _Xgs360026fDHCPSnoopingTxInform_Type()
)
xgs360026fDHCPSnoopingTxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingTxInform.setStatus("current")
_Xgs360026fDHCPSnoopingTxLeaseQuery_Type = Counter32
_Xgs360026fDHCPSnoopingTxLeaseQuery_Object = MibTableColumn
xgs360026fDHCPSnoopingTxLeaseQuery = _Xgs360026fDHCPSnoopingTxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 23),
    _Xgs360026fDHCPSnoopingTxLeaseQuery_Type()
)
xgs360026fDHCPSnoopingTxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingTxLeaseQuery.setStatus("current")
_Xgs360026fDHCPSnoopingTxLeaseUnassigned_Type = Counter32
_Xgs360026fDHCPSnoopingTxLeaseUnassigned_Object = MibTableColumn
xgs360026fDHCPSnoopingTxLeaseUnassigned = _Xgs360026fDHCPSnoopingTxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 24),
    _Xgs360026fDHCPSnoopingTxLeaseUnassigned_Type()
)
xgs360026fDHCPSnoopingTxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingTxLeaseUnassigned.setStatus("current")
_Xgs360026fDHCPSnoopingTxLeaseUnknown_Type = Counter32
_Xgs360026fDHCPSnoopingTxLeaseUnknown_Object = MibTableColumn
xgs360026fDHCPSnoopingTxLeaseUnknown = _Xgs360026fDHCPSnoopingTxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 25),
    _Xgs360026fDHCPSnoopingTxLeaseUnknown_Type()
)
xgs360026fDHCPSnoopingTxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingTxLeaseUnknown.setStatus("current")
_Xgs360026fDHCPSnoopingTxLeaseActive_Type = Counter32
_Xgs360026fDHCPSnoopingTxLeaseActive_Object = MibTableColumn
xgs360026fDHCPSnoopingTxLeaseActive = _Xgs360026fDHCPSnoopingTxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 3, 2, 1, 26),
    _Xgs360026fDHCPSnoopingTxLeaseActive_Type()
)
xgs360026fDHCPSnoopingTxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fDHCPSnoopingTxLeaseActive.setStatus("current")
_Xgs360026fDHCPRelay_ObjectIdentity = ObjectIdentity
xgs360026fDHCPRelay = _Xgs360026fDHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4)
)
_Xgs360026fDHCPRelayConfiguration_ObjectIdentity = ObjectIdentity
xgs360026fDHCPRelayConfiguration = _Xgs360026fDHCPRelayConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 1)
)


class _Xgs360026fDHCPRelayMode_Type(Integer32):
    """Custom type xgs360026fDHCPRelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fDHCPRelayMode_Type.__name__ = "Integer32"
_Xgs360026fDHCPRelayMode_Object = MibScalar
xgs360026fDHCPRelayMode = _Xgs360026fDHCPRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 1, 1),
    _Xgs360026fDHCPRelayMode_Type()
)
xgs360026fDHCPRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fDHCPRelayMode.setStatus("current")
_Xgs360026fDHCPRelayServer_Type = IpAddress
_Xgs360026fDHCPRelayServer_Object = MibScalar
xgs360026fDHCPRelayServer = _Xgs360026fDHCPRelayServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 1, 2),
    _Xgs360026fDHCPRelayServer_Type()
)
xgs360026fDHCPRelayServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fDHCPRelayServer.setStatus("current")


class _Xgs360026fDHCPRelayInformationMode_Type(Integer32):
    """Custom type xgs360026fDHCPRelayInformationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fDHCPRelayInformationMode_Type.__name__ = "Integer32"
_Xgs360026fDHCPRelayInformationMode_Object = MibScalar
xgs360026fDHCPRelayInformationMode = _Xgs360026fDHCPRelayInformationMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 1, 3),
    _Xgs360026fDHCPRelayInformationMode_Type()
)
xgs360026fDHCPRelayInformationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fDHCPRelayInformationMode.setStatus("current")


class _Xgs360026fDHCPRelayInformationPolicy_Type(Integer32):
    """Custom type xgs360026fDHCPRelayInformationPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Xgs360026fDHCPRelayInformationPolicy_Type.__name__ = "Integer32"
_Xgs360026fDHCPRelayInformationPolicy_Object = MibScalar
xgs360026fDHCPRelayInformationPolicy = _Xgs360026fDHCPRelayInformationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 1, 4),
    _Xgs360026fDHCPRelayInformationPolicy_Type()
)
xgs360026fDHCPRelayInformationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fDHCPRelayInformationPolicy.setStatus("current")
_Xgs360026fDHCPRelayStatistics_ObjectIdentity = ObjectIdentity
xgs360026fDHCPRelayStatistics = _Xgs360026fDHCPRelayStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 2)
)
_Xgs360026fDHCPRelayServerStatistics_ObjectIdentity = ObjectIdentity
xgs360026fDHCPRelayServerStatistics = _Xgs360026fDHCPRelayServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 2, 1)
)
_Xgs360026fServerStatTransmitToServer_Type = Counter32
_Xgs360026fServerStatTransmitToServer_Object = MibScalar
xgs360026fServerStatTransmitToServer = _Xgs360026fServerStatTransmitToServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 2, 1, 1),
    _Xgs360026fServerStatTransmitToServer_Type()
)
xgs360026fServerStatTransmitToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fServerStatTransmitToServer.setStatus("current")
_Xgs360026fServerStatTransmitError_Type = Counter32
_Xgs360026fServerStatTransmitError_Object = MibScalar
xgs360026fServerStatTransmitError = _Xgs360026fServerStatTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 2, 1, 2),
    _Xgs360026fServerStatTransmitError_Type()
)
xgs360026fServerStatTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fServerStatTransmitError.setStatus("current")
_Xgs360026fServerStatReceiveFromServer_Type = Counter32
_Xgs360026fServerStatReceiveFromServer_Object = MibScalar
xgs360026fServerStatReceiveFromServer = _Xgs360026fServerStatReceiveFromServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 2, 1, 3),
    _Xgs360026fServerStatReceiveFromServer_Type()
)
xgs360026fServerStatReceiveFromServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fServerStatReceiveFromServer.setStatus("current")
_Xgs360026fServerStatReceiveMissingAgentOption_Type = Counter32
_Xgs360026fServerStatReceiveMissingAgentOption_Object = MibScalar
xgs360026fServerStatReceiveMissingAgentOption = _Xgs360026fServerStatReceiveMissingAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 2, 1, 4),
    _Xgs360026fServerStatReceiveMissingAgentOption_Type()
)
xgs360026fServerStatReceiveMissingAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fServerStatReceiveMissingAgentOption.setStatus("current")
_Xgs360026fServerStatReceiveMissingCircuitID_Type = Counter32
_Xgs360026fServerStatReceiveMissingCircuitID_Object = MibScalar
xgs360026fServerStatReceiveMissingCircuitID = _Xgs360026fServerStatReceiveMissingCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 2, 1, 5),
    _Xgs360026fServerStatReceiveMissingCircuitID_Type()
)
xgs360026fServerStatReceiveMissingCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fServerStatReceiveMissingCircuitID.setStatus("current")
_Xgs360026fServerStatReceiveMissingRemoteID_Type = Counter32
_Xgs360026fServerStatReceiveMissingRemoteID_Object = MibScalar
xgs360026fServerStatReceiveMissingRemoteID = _Xgs360026fServerStatReceiveMissingRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 2, 1, 6),
    _Xgs360026fServerStatReceiveMissingRemoteID_Type()
)
xgs360026fServerStatReceiveMissingRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fServerStatReceiveMissingRemoteID.setStatus("current")
_Xgs360026fServerStatReceiveBadCircuitID_Type = Counter32
_Xgs360026fServerStatReceiveBadCircuitID_Object = MibScalar
xgs360026fServerStatReceiveBadCircuitID = _Xgs360026fServerStatReceiveBadCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 2, 1, 7),
    _Xgs360026fServerStatReceiveBadCircuitID_Type()
)
xgs360026fServerStatReceiveBadCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fServerStatReceiveBadCircuitID.setStatus("current")
_Xgs360026fServerStatReceiveBadRemoteID_Type = Counter32
_Xgs360026fServerStatReceiveBadRemoteID_Object = MibScalar
xgs360026fServerStatReceiveBadRemoteID = _Xgs360026fServerStatReceiveBadRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 2, 1, 8),
    _Xgs360026fServerStatReceiveBadRemoteID_Type()
)
xgs360026fServerStatReceiveBadRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fServerStatReceiveBadRemoteID.setStatus("current")
_Xgs360026fDHCPRelayClientStatistics_ObjectIdentity = ObjectIdentity
xgs360026fDHCPRelayClientStatistics = _Xgs360026fDHCPRelayClientStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 2, 2)
)
_Xgs360026fClientStatTransmitToClient_Type = Counter32
_Xgs360026fClientStatTransmitToClient_Object = MibScalar
xgs360026fClientStatTransmitToClient = _Xgs360026fClientStatTransmitToClient_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 2, 2, 1),
    _Xgs360026fClientStatTransmitToClient_Type()
)
xgs360026fClientStatTransmitToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fClientStatTransmitToClient.setStatus("current")
_Xgs360026fClientStatTransmitError_Type = Counter32
_Xgs360026fClientStatTransmitError_Object = MibScalar
xgs360026fClientStatTransmitError = _Xgs360026fClientStatTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 2, 2, 2),
    _Xgs360026fClientStatTransmitError_Type()
)
xgs360026fClientStatTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fClientStatTransmitError.setStatus("current")
_Xgs360026fClientStatReceivefromClient_Type = Counter32
_Xgs360026fClientStatReceivefromClient_Object = MibScalar
xgs360026fClientStatReceivefromClient = _Xgs360026fClientStatReceivefromClient_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 2, 2, 3),
    _Xgs360026fClientStatReceivefromClient_Type()
)
xgs360026fClientStatReceivefromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fClientStatReceivefromClient.setStatus("current")
_Xgs360026fClientStatReceiveAgentOption_Type = Counter32
_Xgs360026fClientStatReceiveAgentOption_Object = MibScalar
xgs360026fClientStatReceiveAgentOption = _Xgs360026fClientStatReceiveAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 2, 2, 4),
    _Xgs360026fClientStatReceiveAgentOption_Type()
)
xgs360026fClientStatReceiveAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fClientStatReceiveAgentOption.setStatus("current")
_Xgs360026fClientStatReplaceAgentOption_Type = Counter32
_Xgs360026fClientStatReplaceAgentOption_Object = MibScalar
xgs360026fClientStatReplaceAgentOption = _Xgs360026fClientStatReplaceAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 2, 2, 5),
    _Xgs360026fClientStatReplaceAgentOption_Type()
)
xgs360026fClientStatReplaceAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fClientStatReplaceAgentOption.setStatus("current")
_Xgs360026fClientStatKeepAgentOption_Type = Counter32
_Xgs360026fClientStatKeepAgentOption_Object = MibScalar
xgs360026fClientStatKeepAgentOption = _Xgs360026fClientStatKeepAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 2, 2, 6),
    _Xgs360026fClientStatKeepAgentOption_Type()
)
xgs360026fClientStatKeepAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fClientStatKeepAgentOption.setStatus("current")
_Xgs360026fClientStatDropAgentOption_Type = Counter32
_Xgs360026fClientStatDropAgentOption_Object = MibScalar
xgs360026fClientStatDropAgentOption = _Xgs360026fClientStatDropAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 4, 2, 2, 7),
    _Xgs360026fClientStatDropAgentOption_Type()
)
xgs360026fClientStatDropAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fClientStatDropAgentOption.setStatus("current")
_Xgs360026fPortSecurity_ObjectIdentity = ObjectIdentity
xgs360026fPortSecurity = _Xgs360026fPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5)
)
_Xgs360026fPortSecLimitCtrl_ObjectIdentity = ObjectIdentity
xgs360026fPortSecLimitCtrl = _Xgs360026fPortSecLimitCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 1)
)
_Xgs360026fPortSecLimitCtrlSystemConf_ObjectIdentity = ObjectIdentity
xgs360026fPortSecLimitCtrlSystemConf = _Xgs360026fPortSecLimitCtrlSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 1, 1)
)


class _Xgs360026fPortSecurityMode_Type(Integer32):
    """Custom type xgs360026fPortSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fPortSecurityMode_Type.__name__ = "Integer32"
_Xgs360026fPortSecurityMode_Object = MibScalar
xgs360026fPortSecurityMode = _Xgs360026fPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 1, 1, 1),
    _Xgs360026fPortSecurityMode_Type()
)
xgs360026fPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPortSecurityMode.setStatus("current")


class _Xgs360026fPortSecurityAging_Type(Integer32):
    """Custom type xgs360026fPortSecurityAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fPortSecurityAging_Type.__name__ = "Integer32"
_Xgs360026fPortSecurityAging_Object = MibScalar
xgs360026fPortSecurityAging = _Xgs360026fPortSecurityAging_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 1, 1, 2),
    _Xgs360026fPortSecurityAging_Type()
)
xgs360026fPortSecurityAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPortSecurityAging.setStatus("current")


class _Xgs360026fPortSecurityAgingPeriod_Type(Integer32):
    """Custom type xgs360026fPortSecurityAgingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000000),
    )


_Xgs360026fPortSecurityAgingPeriod_Type.__name__ = "Integer32"
_Xgs360026fPortSecurityAgingPeriod_Object = MibScalar
xgs360026fPortSecurityAgingPeriod = _Xgs360026fPortSecurityAgingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 1, 1, 3),
    _Xgs360026fPortSecurityAgingPeriod_Type()
)
xgs360026fPortSecurityAgingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPortSecurityAgingPeriod.setStatus("current")
_Xgs360026fPortSecLimitCtrlTable_Object = MibTable
xgs360026fPortSecLimitCtrlTable = _Xgs360026fPortSecLimitCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    xgs360026fPortSecLimitCtrlTable.setStatus("current")
_Xgs360026fPortSecLimitCtrlEntry_Object = MibTableRow
xgs360026fPortSecLimitCtrlEntry = _Xgs360026fPortSecLimitCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 1, 2, 1)
)
xgs360026fPortSecLimitCtrlEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fPortSecLimitCtrlPort"),
)
if mibBuilder.loadTexts:
    xgs360026fPortSecLimitCtrlEntry.setStatus("current")


class _Xgs360026fPortSecLimitCtrlPort_Type(Integer32):
    """Custom type xgs360026fPortSecLimitCtrlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fPortSecLimitCtrlPort_Type.__name__ = "Integer32"
_Xgs360026fPortSecLimitCtrlPort_Object = MibTableColumn
xgs360026fPortSecLimitCtrlPort = _Xgs360026fPortSecLimitCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 1, 2, 1, 1),
    _Xgs360026fPortSecLimitCtrlPort_Type()
)
xgs360026fPortSecLimitCtrlPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fPortSecLimitCtrlPort.setStatus("current")


class _Xgs360026fPortSecLimitCtrlPortMode_Type(Integer32):
    """Custom type xgs360026fPortSecLimitCtrlPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fPortSecLimitCtrlPortMode_Type.__name__ = "Integer32"
_Xgs360026fPortSecLimitCtrlPortMode_Object = MibTableColumn
xgs360026fPortSecLimitCtrlPortMode = _Xgs360026fPortSecLimitCtrlPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 1, 2, 1, 2),
    _Xgs360026fPortSecLimitCtrlPortMode_Type()
)
xgs360026fPortSecLimitCtrlPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPortSecLimitCtrlPortMode.setStatus("current")


class _Xgs360026fPortSecLimitCtrlPortLimit_Type(Integer32):
    """Custom type xgs360026fPortSecLimitCtrlPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Xgs360026fPortSecLimitCtrlPortLimit_Type.__name__ = "Integer32"
_Xgs360026fPortSecLimitCtrlPortLimit_Object = MibTableColumn
xgs360026fPortSecLimitCtrlPortLimit = _Xgs360026fPortSecLimitCtrlPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 1, 2, 1, 3),
    _Xgs360026fPortSecLimitCtrlPortLimit_Type()
)
xgs360026fPortSecLimitCtrlPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPortSecLimitCtrlPortLimit.setStatus("current")


class _Xgs360026fPortSecLimitCtrlPortAction_Type(Integer32):
    """Custom type xgs360026fPortSecLimitCtrlPortAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Xgs360026fPortSecLimitCtrlPortAction_Type.__name__ = "Integer32"
_Xgs360026fPortSecLimitCtrlPortAction_Object = MibTableColumn
xgs360026fPortSecLimitCtrlPortAction = _Xgs360026fPortSecLimitCtrlPortAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 1, 2, 1, 4),
    _Xgs360026fPortSecLimitCtrlPortAction_Type()
)
xgs360026fPortSecLimitCtrlPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPortSecLimitCtrlPortAction.setStatus("current")
_Xgs360026fPortSecLimitCtrlPortState_Type = DisplayString
_Xgs360026fPortSecLimitCtrlPortState_Object = MibTableColumn
xgs360026fPortSecLimitCtrlPortState = _Xgs360026fPortSecLimitCtrlPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 1, 2, 1, 5),
    _Xgs360026fPortSecLimitCtrlPortState_Type()
)
xgs360026fPortSecLimitCtrlPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortSecLimitCtrlPortState.setStatus("current")


class _Xgs360026fPortSecLimitCtrlPortReOpen_Type(Integer32):
    """Custom type xgs360026fPortSecLimitCtrlPortReOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fPortSecLimitCtrlPortReOpen_Type.__name__ = "Integer32"
_Xgs360026fPortSecLimitCtrlPortReOpen_Object = MibTableColumn
xgs360026fPortSecLimitCtrlPortReOpen = _Xgs360026fPortSecLimitCtrlPortReOpen_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 1, 2, 1, 6),
    _Xgs360026fPortSecLimitCtrlPortReOpen_Type()
)
xgs360026fPortSecLimitCtrlPortReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPortSecLimitCtrlPortReOpen.setStatus("current")
_Xgs360026fPortSecSwitchStatusTable_Object = MibTable
xgs360026fPortSecSwitchStatusTable = _Xgs360026fPortSecSwitchStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 2)
)
if mibBuilder.loadTexts:
    xgs360026fPortSecSwitchStatusTable.setStatus("current")
_Xgs360026fPortSecSwitchStatusEntry_Object = MibTableRow
xgs360026fPortSecSwitchStatusEntry = _Xgs360026fPortSecSwitchStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 2, 1)
)
xgs360026fPortSecSwitchStatusEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fPortSecSwitchStatusPort"),
)
if mibBuilder.loadTexts:
    xgs360026fPortSecSwitchStatusEntry.setStatus("current")


class _Xgs360026fPortSecSwitchStatusPort_Type(Integer32):
    """Custom type xgs360026fPortSecSwitchStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fPortSecSwitchStatusPort_Type.__name__ = "Integer32"
_Xgs360026fPortSecSwitchStatusPort_Object = MibTableColumn
xgs360026fPortSecSwitchStatusPort = _Xgs360026fPortSecSwitchStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 2, 1, 1),
    _Xgs360026fPortSecSwitchStatusPort_Type()
)
xgs360026fPortSecSwitchStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fPortSecSwitchStatusPort.setStatus("current")
_Xgs360026fPortSecSwitchStatusUsers_Type = DisplayString
_Xgs360026fPortSecSwitchStatusUsers_Object = MibTableColumn
xgs360026fPortSecSwitchStatusUsers = _Xgs360026fPortSecSwitchStatusUsers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 2, 1, 2),
    _Xgs360026fPortSecSwitchStatusUsers_Type()
)
xgs360026fPortSecSwitchStatusUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortSecSwitchStatusUsers.setStatus("current")
_Xgs360026fPortSecSwitchStatusState_Type = DisplayString
_Xgs360026fPortSecSwitchStatusState_Object = MibTableColumn
xgs360026fPortSecSwitchStatusState = _Xgs360026fPortSecSwitchStatusState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 2, 1, 3),
    _Xgs360026fPortSecSwitchStatusState_Type()
)
xgs360026fPortSecSwitchStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortSecSwitchStatusState.setStatus("current")


class _Xgs360026fPortSecSwitchStatusMACCountCurrent_Type(Integer32):
    """Custom type xgs360026fPortSecSwitchStatusMACCountCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fPortSecSwitchStatusMACCountCurrent_Type.__name__ = "Integer32"
_Xgs360026fPortSecSwitchStatusMACCountCurrent_Object = MibTableColumn
xgs360026fPortSecSwitchStatusMACCountCurrent = _Xgs360026fPortSecSwitchStatusMACCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 2, 1, 4),
    _Xgs360026fPortSecSwitchStatusMACCountCurrent_Type()
)
xgs360026fPortSecSwitchStatusMACCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortSecSwitchStatusMACCountCurrent.setStatus("current")


class _Xgs360026fPortSecSwitchStatusMACCountLimit_Type(Integer32):
    """Custom type xgs360026fPortSecSwitchStatusMACCountLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fPortSecSwitchStatusMACCountLimit_Type.__name__ = "Integer32"
_Xgs360026fPortSecSwitchStatusMACCountLimit_Object = MibTableColumn
xgs360026fPortSecSwitchStatusMACCountLimit = _Xgs360026fPortSecSwitchStatusMACCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 2, 1, 5),
    _Xgs360026fPortSecSwitchStatusMACCountLimit_Type()
)
xgs360026fPortSecSwitchStatusMACCountLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortSecSwitchStatusMACCountLimit.setStatus("current")
_Xgs360026fPortSecPortStatus_ObjectIdentity = ObjectIdentity
xgs360026fPortSecPortStatus = _Xgs360026fPortSecPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 3)
)


class _Xgs360026fPortSecPortStatusPort_Type(Integer32):
    """Custom type xgs360026fPortSecPortStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fPortSecPortStatusPort_Type.__name__ = "Integer32"
_Xgs360026fPortSecPortStatusPort_Object = MibScalar
xgs360026fPortSecPortStatusPort = _Xgs360026fPortSecPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 3, 1),
    _Xgs360026fPortSecPortStatusPort_Type()
)
xgs360026fPortSecPortStatusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPortSecPortStatusPort.setStatus("current")
_Xgs360026fPortSecPortStatusTable_Object = MibTable
xgs360026fPortSecPortStatusTable = _Xgs360026fPortSecPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 3, 2)
)
if mibBuilder.loadTexts:
    xgs360026fPortSecPortStatusTable.setStatus("current")
_Xgs360026fPortSecPortStatusEntry_Object = MibTableRow
xgs360026fPortSecPortStatusEntry = _Xgs360026fPortSecPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 3, 2, 1)
)
xgs360026fPortSecPortStatusEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fPortSecPortStatusIndex"),
)
if mibBuilder.loadTexts:
    xgs360026fPortSecPortStatusEntry.setStatus("current")


class _Xgs360026fPortSecPortStatusIndex_Type(Integer32):
    """Custom type xgs360026fPortSecPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fPortSecPortStatusIndex_Type.__name__ = "Integer32"
_Xgs360026fPortSecPortStatusIndex_Object = MibTableColumn
xgs360026fPortSecPortStatusIndex = _Xgs360026fPortSecPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 3, 2, 1, 1),
    _Xgs360026fPortSecPortStatusIndex_Type()
)
xgs360026fPortSecPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fPortSecPortStatusIndex.setStatus("current")
_Xgs360026fPortSecPortStatusMACAddress_Type = MacAddress
_Xgs360026fPortSecPortStatusMACAddress_Object = MibTableColumn
xgs360026fPortSecPortStatusMACAddress = _Xgs360026fPortSecPortStatusMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 3, 2, 1, 2),
    _Xgs360026fPortSecPortStatusMACAddress_Type()
)
xgs360026fPortSecPortStatusMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortSecPortStatusMACAddress.setStatus("current")


class _Xgs360026fPortSecPortStatusVLANId_Type(Integer32):
    """Custom type xgs360026fPortSecPortStatusVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Xgs360026fPortSecPortStatusVLANId_Type.__name__ = "Integer32"
_Xgs360026fPortSecPortStatusVLANId_Object = MibTableColumn
xgs360026fPortSecPortStatusVLANId = _Xgs360026fPortSecPortStatusVLANId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 3, 2, 1, 3),
    _Xgs360026fPortSecPortStatusVLANId_Type()
)
xgs360026fPortSecPortStatusVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortSecPortStatusVLANId.setStatus("current")
_Xgs360026fPortSecPortStatusState_Type = DisplayString
_Xgs360026fPortSecPortStatusState_Object = MibTableColumn
xgs360026fPortSecPortStatusState = _Xgs360026fPortSecPortStatusState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 3, 2, 1, 4),
    _Xgs360026fPortSecPortStatusState_Type()
)
xgs360026fPortSecPortStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortSecPortStatusState.setStatus("current")
_Xgs360026fPortSecPortStatusTimeOfAddition_Type = DisplayString
_Xgs360026fPortSecPortStatusTimeOfAddition_Object = MibTableColumn
xgs360026fPortSecPortStatusTimeOfAddition = _Xgs360026fPortSecPortStatusTimeOfAddition_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 3, 2, 1, 5),
    _Xgs360026fPortSecPortStatusTimeOfAddition_Type()
)
xgs360026fPortSecPortStatusTimeOfAddition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortSecPortStatusTimeOfAddition.setStatus("current")
_Xgs360026fPortSecPortStatusAgeAndHold_Type = DisplayString
_Xgs360026fPortSecPortStatusAgeAndHold_Object = MibTableColumn
xgs360026fPortSecPortStatusAgeAndHold = _Xgs360026fPortSecPortStatusAgeAndHold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 5, 3, 2, 1, 6),
    _Xgs360026fPortSecPortStatusAgeAndHold_Type()
)
xgs360026fPortSecPortStatusAgeAndHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPortSecPortStatusAgeAndHold.setStatus("current")
_Xgs360026fAccessManagement_ObjectIdentity = ObjectIdentity
xgs360026fAccessManagement = _Xgs360026fAccessManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6)
)
_Xgs360026fAccessMgtConf_ObjectIdentity = ObjectIdentity
xgs360026fAccessMgtConf = _Xgs360026fAccessMgtConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 1)
)


class _Xgs360026fAccessMgtConfMode_Type(Integer32):
    """Custom type xgs360026fAccessMgtConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fAccessMgtConfMode_Type.__name__ = "Integer32"
_Xgs360026fAccessMgtConfMode_Object = MibScalar
xgs360026fAccessMgtConfMode = _Xgs360026fAccessMgtConfMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 1, 1),
    _Xgs360026fAccessMgtConfMode_Type()
)
xgs360026fAccessMgtConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fAccessMgtConfMode.setStatus("current")


class _Xgs360026fAccessMgtConfCreate_Type(Integer32):
    """Custom type xgs360026fAccessMgtConfCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fAccessMgtConfCreate_Type.__name__ = "Integer32"
_Xgs360026fAccessMgtConfCreate_Object = MibScalar
xgs360026fAccessMgtConfCreate = _Xgs360026fAccessMgtConfCreate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 1, 2),
    _Xgs360026fAccessMgtConfCreate_Type()
)
xgs360026fAccessMgtConfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fAccessMgtConfCreate.setStatus("current")
_Xgs360026fAccessMgtConfTable_Object = MibTable
xgs360026fAccessMgtConfTable = _Xgs360026fAccessMgtConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 1, 3)
)
if mibBuilder.loadTexts:
    xgs360026fAccessMgtConfTable.setStatus("current")
_Xgs360026fAccessMgtConfEntry_Object = MibTableRow
xgs360026fAccessMgtConfEntry = _Xgs360026fAccessMgtConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 1, 3, 1)
)
xgs360026fAccessMgtConfEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fAccessMgtIndex"),
)
if mibBuilder.loadTexts:
    xgs360026fAccessMgtConfEntry.setStatus("current")


class _Xgs360026fAccessMgtIndex_Type(Integer32):
    """Custom type xgs360026fAccessMgtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Xgs360026fAccessMgtIndex_Type.__name__ = "Integer32"
_Xgs360026fAccessMgtIndex_Object = MibTableColumn
xgs360026fAccessMgtIndex = _Xgs360026fAccessMgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 1, 3, 1, 1),
    _Xgs360026fAccessMgtIndex_Type()
)
xgs360026fAccessMgtIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fAccessMgtIndex.setStatus("current")


class _Xgs360026fAccessMgtAddresstype_Type(Integer32):
    """Custom type xgs360026fAccessMgtAddresstype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fAccessMgtAddresstype_Type.__name__ = "Integer32"
_Xgs360026fAccessMgtAddresstype_Object = MibTableColumn
xgs360026fAccessMgtAddresstype = _Xgs360026fAccessMgtAddresstype_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 1, 3, 1, 2),
    _Xgs360026fAccessMgtAddresstype_Type()
)
xgs360026fAccessMgtAddresstype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fAccessMgtAddresstype.setStatus("current")
_Xgs360026fAccessMgtStartIpAddress_Type = DisplayString
_Xgs360026fAccessMgtStartIpAddress_Object = MibTableColumn
xgs360026fAccessMgtStartIpAddress = _Xgs360026fAccessMgtStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 1, 3, 1, 3),
    _Xgs360026fAccessMgtStartIpAddress_Type()
)
xgs360026fAccessMgtStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fAccessMgtStartIpAddress.setStatus("current")
_Xgs360026fAccessMgtEndIpAddress_Type = DisplayString
_Xgs360026fAccessMgtEndIpAddress_Object = MibTableColumn
xgs360026fAccessMgtEndIpAddress = _Xgs360026fAccessMgtEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 1, 3, 1, 4),
    _Xgs360026fAccessMgtEndIpAddress_Type()
)
xgs360026fAccessMgtEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fAccessMgtEndIpAddress.setStatus("current")


class _Xgs360026fAccessMgtHttpHttps_Type(Integer32):
    """Custom type xgs360026fAccessMgtHttpHttps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fAccessMgtHttpHttps_Type.__name__ = "Integer32"
_Xgs360026fAccessMgtHttpHttps_Object = MibTableColumn
xgs360026fAccessMgtHttpHttps = _Xgs360026fAccessMgtHttpHttps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 1, 3, 1, 5),
    _Xgs360026fAccessMgtHttpHttps_Type()
)
xgs360026fAccessMgtHttpHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fAccessMgtHttpHttps.setStatus("current")


class _Xgs360026fAccessMgtSNMP_Type(Integer32):
    """Custom type xgs360026fAccessMgtSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fAccessMgtSNMP_Type.__name__ = "Integer32"
_Xgs360026fAccessMgtSNMP_Object = MibTableColumn
xgs360026fAccessMgtSNMP = _Xgs360026fAccessMgtSNMP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 1, 3, 1, 6),
    _Xgs360026fAccessMgtSNMP_Type()
)
xgs360026fAccessMgtSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fAccessMgtSNMP.setStatus("current")


class _Xgs360026fAccessMgtTelnetSSH_Type(Integer32):
    """Custom type xgs360026fAccessMgtTelnetSSH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fAccessMgtTelnetSSH_Type.__name__ = "Integer32"
_Xgs360026fAccessMgtTelnetSSH_Object = MibTableColumn
xgs360026fAccessMgtTelnetSSH = _Xgs360026fAccessMgtTelnetSSH_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 1, 3, 1, 7),
    _Xgs360026fAccessMgtTelnetSSH_Type()
)
xgs360026fAccessMgtTelnetSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fAccessMgtTelnetSSH.setStatus("current")


class _Xgs360026fAccessMgtRowStatus_Type(Integer32):
    """Custom type xgs360026fAccessMgtRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Xgs360026fAccessMgtRowStatus_Type.__name__ = "Integer32"
_Xgs360026fAccessMgtRowStatus_Object = MibTableColumn
xgs360026fAccessMgtRowStatus = _Xgs360026fAccessMgtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 1, 3, 1, 8),
    _Xgs360026fAccessMgtRowStatus_Type()
)
xgs360026fAccessMgtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fAccessMgtRowStatus.setStatus("current")
_Xgs360026fAccessMgtStatistics_ObjectIdentity = ObjectIdentity
xgs360026fAccessMgtStatistics = _Xgs360026fAccessMgtStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 2)
)
_Xgs360026fHttpReceivedPkts_Type = Counter32
_Xgs360026fHttpReceivedPkts_Object = MibScalar
xgs360026fHttpReceivedPkts = _Xgs360026fHttpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 2, 1),
    _Xgs360026fHttpReceivedPkts_Type()
)
xgs360026fHttpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fHttpReceivedPkts.setStatus("current")
_Xgs360026fHttpAllowedPkts_Type = Counter32
_Xgs360026fHttpAllowedPkts_Object = MibScalar
xgs360026fHttpAllowedPkts = _Xgs360026fHttpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 2, 2),
    _Xgs360026fHttpAllowedPkts_Type()
)
xgs360026fHttpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fHttpAllowedPkts.setStatus("current")
_Xgs360026fHttpDiscardedPkts_Type = Counter32
_Xgs360026fHttpDiscardedPkts_Object = MibScalar
xgs360026fHttpDiscardedPkts = _Xgs360026fHttpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 2, 3),
    _Xgs360026fHttpDiscardedPkts_Type()
)
xgs360026fHttpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fHttpDiscardedPkts.setStatus("current")
_Xgs360026fHttpsReceivedPkts_Type = Counter32
_Xgs360026fHttpsReceivedPkts_Object = MibScalar
xgs360026fHttpsReceivedPkts = _Xgs360026fHttpsReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 2, 4),
    _Xgs360026fHttpsReceivedPkts_Type()
)
xgs360026fHttpsReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fHttpsReceivedPkts.setStatus("current")
_Xgs360026fHttpsAllowedPkts_Type = Counter32
_Xgs360026fHttpsAllowedPkts_Object = MibScalar
xgs360026fHttpsAllowedPkts = _Xgs360026fHttpsAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 2, 5),
    _Xgs360026fHttpsAllowedPkts_Type()
)
xgs360026fHttpsAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fHttpsAllowedPkts.setStatus("current")
_Xgs360026fHttpsDiscardedPkts_Type = Counter32
_Xgs360026fHttpsDiscardedPkts_Object = MibScalar
xgs360026fHttpsDiscardedPkts = _Xgs360026fHttpsDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 2, 6),
    _Xgs360026fHttpsDiscardedPkts_Type()
)
xgs360026fHttpsDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fHttpsDiscardedPkts.setStatus("current")
_Xgs360026fSnmpReceivedPkts_Type = Counter32
_Xgs360026fSnmpReceivedPkts_Object = MibScalar
xgs360026fSnmpReceivedPkts = _Xgs360026fSnmpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 2, 7),
    _Xgs360026fSnmpReceivedPkts_Type()
)
xgs360026fSnmpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSnmpReceivedPkts.setStatus("current")
_Xgs360026fSnmpAllowedPkts_Type = Counter32
_Xgs360026fSnmpAllowedPkts_Object = MibScalar
xgs360026fSnmpAllowedPkts = _Xgs360026fSnmpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 2, 8),
    _Xgs360026fSnmpAllowedPkts_Type()
)
xgs360026fSnmpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSnmpAllowedPkts.setStatus("current")
_Xgs360026fSnmpDiscardedPkts_Type = Counter32
_Xgs360026fSnmpDiscardedPkts_Object = MibScalar
xgs360026fSnmpDiscardedPkts = _Xgs360026fSnmpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 2, 9),
    _Xgs360026fSnmpDiscardedPkts_Type()
)
xgs360026fSnmpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSnmpDiscardedPkts.setStatus("current")
_Xgs360026fTelnetReceivedPkts_Type = Counter32
_Xgs360026fTelnetReceivedPkts_Object = MibScalar
xgs360026fTelnetReceivedPkts = _Xgs360026fTelnetReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 2, 10),
    _Xgs360026fTelnetReceivedPkts_Type()
)
xgs360026fTelnetReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fTelnetReceivedPkts.setStatus("current")
_Xgs360026fTelnetAllowedPkts_Type = Counter32
_Xgs360026fTelnetAllowedPkts_Object = MibScalar
xgs360026fTelnetAllowedPkts = _Xgs360026fTelnetAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 2, 11),
    _Xgs360026fTelnetAllowedPkts_Type()
)
xgs360026fTelnetAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fTelnetAllowedPkts.setStatus("current")
_Xgs360026fTelnetDiscardedPkts_Type = Counter32
_Xgs360026fTelnetDiscardedPkts_Object = MibScalar
xgs360026fTelnetDiscardedPkts = _Xgs360026fTelnetDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 2, 12),
    _Xgs360026fTelnetDiscardedPkts_Type()
)
xgs360026fTelnetDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fTelnetDiscardedPkts.setStatus("current")
_Xgs360026fSSHReceivedPkts_Type = Counter32
_Xgs360026fSSHReceivedPkts_Object = MibScalar
xgs360026fSSHReceivedPkts = _Xgs360026fSSHReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 2, 13),
    _Xgs360026fSSHReceivedPkts_Type()
)
xgs360026fSSHReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSSHReceivedPkts.setStatus("current")
_Xgs360026fSSHAllowedPkts_Type = Counter32
_Xgs360026fSSHAllowedPkts_Object = MibScalar
xgs360026fSSHAllowedPkts = _Xgs360026fSSHAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 2, 14),
    _Xgs360026fSSHAllowedPkts_Type()
)
xgs360026fSSHAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSSHAllowedPkts.setStatus("current")
_Xgs360026fSSHDiscardedPkts_Type = Counter32
_Xgs360026fSSHDiscardedPkts_Object = MibScalar
xgs360026fSSHDiscardedPkts = _Xgs360026fSSHDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 2, 15),
    _Xgs360026fSSHDiscardedPkts_Type()
)
xgs360026fSSHDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fSSHDiscardedPkts.setStatus("current")


class _Xgs360026fAccessMgtStatisticsClearAll_Type(Integer32):
    """Custom type xgs360026fAccessMgtStatisticsClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fAccessMgtStatisticsClearAll_Type.__name__ = "Integer32"
_Xgs360026fAccessMgtStatisticsClearAll_Object = MibScalar
xgs360026fAccessMgtStatisticsClearAll = _Xgs360026fAccessMgtStatisticsClearAll_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 6, 2, 16),
    _Xgs360026fAccessMgtStatisticsClearAll_Type()
)
xgs360026fAccessMgtStatisticsClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fAccessMgtStatisticsClearAll.setStatus("current")
_Xgs360026fSSH_ObjectIdentity = ObjectIdentity
xgs360026fSSH = _Xgs360026fSSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 7)
)


class _Xgs360026fSSHMode_Type(Integer32):
    """Custom type xgs360026fSSHMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fSSHMode_Type.__name__ = "Integer32"
_Xgs360026fSSHMode_Object = MibScalar
xgs360026fSSHMode = _Xgs360026fSSHMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 7, 1),
    _Xgs360026fSSHMode_Type()
)
xgs360026fSSHMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSSHMode.setStatus("current")
_Xgs360026fHTTPS_ObjectIdentity = ObjectIdentity
xgs360026fHTTPS = _Xgs360026fHTTPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 8)
)


class _Xgs360026fHTTPSMode_Type(Integer32):
    """Custom type xgs360026fHTTPSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fHTTPSMode_Type.__name__ = "Integer32"
_Xgs360026fHTTPSMode_Object = MibScalar
xgs360026fHTTPSMode = _Xgs360026fHTTPSMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 8, 1),
    _Xgs360026fHTTPSMode_Type()
)
xgs360026fHTTPSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fHTTPSMode.setStatus("current")


class _Xgs360026fHTTPSAutoRedirect_Type(Integer32):
    """Custom type xgs360026fHTTPSAutoRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fHTTPSAutoRedirect_Type.__name__ = "Integer32"
_Xgs360026fHTTPSAutoRedirect_Object = MibScalar
xgs360026fHTTPSAutoRedirect = _Xgs360026fHTTPSAutoRedirect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 8, 2),
    _Xgs360026fHTTPSAutoRedirect_Type()
)
xgs360026fHTTPSAutoRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fHTTPSAutoRedirect.setStatus("current")
_Xgs360026fAuthMethod_ObjectIdentity = ObjectIdentity
xgs360026fAuthMethod = _Xgs360026fAuthMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 9)
)


class _Xgs360026fConsoleAuthMethod_Type(Integer32):
    """Custom type xgs360026fConsoleAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Xgs360026fConsoleAuthMethod_Type.__name__ = "Integer32"
_Xgs360026fConsoleAuthMethod_Object = MibScalar
xgs360026fConsoleAuthMethod = _Xgs360026fConsoleAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 9, 1),
    _Xgs360026fConsoleAuthMethod_Type()
)
xgs360026fConsoleAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fConsoleAuthMethod.setStatus("current")


class _Xgs360026fConsoleFallback_Type(Integer32):
    """Custom type xgs360026fConsoleFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fConsoleFallback_Type.__name__ = "Integer32"
_Xgs360026fConsoleFallback_Object = MibScalar
xgs360026fConsoleFallback = _Xgs360026fConsoleFallback_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 9, 2),
    _Xgs360026fConsoleFallback_Type()
)
xgs360026fConsoleFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fConsoleFallback.setStatus("current")


class _Xgs360026fTelnetAuthMethod_Type(Integer32):
    """Custom type xgs360026fTelnetAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Xgs360026fTelnetAuthMethod_Type.__name__ = "Integer32"
_Xgs360026fTelnetAuthMethod_Object = MibScalar
xgs360026fTelnetAuthMethod = _Xgs360026fTelnetAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 9, 3),
    _Xgs360026fTelnetAuthMethod_Type()
)
xgs360026fTelnetAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTelnetAuthMethod.setStatus("current")


class _Xgs360026fTelnetFallback_Type(Integer32):
    """Custom type xgs360026fTelnetFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fTelnetFallback_Type.__name__ = "Integer32"
_Xgs360026fTelnetFallback_Object = MibScalar
xgs360026fTelnetFallback = _Xgs360026fTelnetFallback_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 9, 4),
    _Xgs360026fTelnetFallback_Type()
)
xgs360026fTelnetFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fTelnetFallback.setStatus("current")


class _Xgs360026fSshAuthMethod_Type(Integer32):
    """Custom type xgs360026fSshAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Xgs360026fSshAuthMethod_Type.__name__ = "Integer32"
_Xgs360026fSshAuthMethod_Object = MibScalar
xgs360026fSshAuthMethod = _Xgs360026fSshAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 9, 5),
    _Xgs360026fSshAuthMethod_Type()
)
xgs360026fSshAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSshAuthMethod.setStatus("current")


class _Xgs360026fSshFallback_Type(Integer32):
    """Custom type xgs360026fSshFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fSshFallback_Type.__name__ = "Integer32"
_Xgs360026fSshFallback_Object = MibScalar
xgs360026fSshFallback = _Xgs360026fSshFallback_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 9, 6),
    _Xgs360026fSshFallback_Type()
)
xgs360026fSshFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSshFallback.setStatus("current")


class _Xgs360026fWebAuthMethod_Type(Integer32):
    """Custom type xgs360026fWebAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Xgs360026fWebAuthMethod_Type.__name__ = "Integer32"
_Xgs360026fWebAuthMethod_Object = MibScalar
xgs360026fWebAuthMethod = _Xgs360026fWebAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 9, 7),
    _Xgs360026fWebAuthMethod_Type()
)
xgs360026fWebAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fWebAuthMethod.setStatus("current")


class _Xgs360026fWebFallback_Type(Integer32):
    """Custom type xgs360026fWebFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fWebFallback_Type.__name__ = "Integer32"
_Xgs360026fWebFallback_Object = MibScalar
xgs360026fWebFallback = _Xgs360026fWebFallback_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 3, 9, 8),
    _Xgs360026fWebFallback_Type()
)
xgs360026fWebFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fWebFallback.setStatus("current")
_Xgs360026fMaintenance_ObjectIdentity = ObjectIdentity
xgs360026fMaintenance = _Xgs360026fMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4)
)


class _Xgs360026fRestartDevice_Type(Integer32):
    """Custom type xgs360026fRestartDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fRestartDevice_Type.__name__ = "Integer32"
_Xgs360026fRestartDevice_Object = MibScalar
xgs360026fRestartDevice = _Xgs360026fRestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 1),
    _Xgs360026fRestartDevice_Type()
)
xgs360026fRestartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fRestartDevice.setStatus("current")
_Xgs360026fFirmware_ObjectIdentity = ObjectIdentity
xgs360026fFirmware = _Xgs360026fFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 2)
)
_Xgs360026fFirmwareIpAddress_Type = IpAddress
_Xgs360026fFirmwareIpAddress_Object = MibScalar
xgs360026fFirmwareIpAddress = _Xgs360026fFirmwareIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 2, 1),
    _Xgs360026fFirmwareIpAddress_Type()
)
xgs360026fFirmwareIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fFirmwareIpAddress.setStatus("current")
_Xgs360026fFirmwareFileName_Type = DisplayString
_Xgs360026fFirmwareFileName_Object = MibScalar
xgs360026fFirmwareFileName = _Xgs360026fFirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 2, 2),
    _Xgs360026fFirmwareFileName_Type()
)
xgs360026fFirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fFirmwareFileName.setStatus("current")


class _Xgs360026fDoFirmwareUpgrade_Type(Integer32):
    """Custom type xgs360026fDoFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fDoFirmwareUpgrade_Type.__name__ = "Integer32"
_Xgs360026fDoFirmwareUpgrade_Object = MibScalar
xgs360026fDoFirmwareUpgrade = _Xgs360026fDoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 2, 3),
    _Xgs360026fDoFirmwareUpgrade_Type()
)
xgs360026fDoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fDoFirmwareUpgrade.setStatus("current")
_Xgs360026fSaveOrRestore_ObjectIdentity = ObjectIdentity
xgs360026fSaveOrRestore = _Xgs360026fSaveOrRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 3)
)


class _Xgs360026fFactoryDefaults_Type(Integer32):
    """Custom type xgs360026fFactoryDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fFactoryDefaults_Type.__name__ = "Integer32"
_Xgs360026fFactoryDefaults_Object = MibScalar
xgs360026fFactoryDefaults = _Xgs360026fFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 3, 1),
    _Xgs360026fFactoryDefaults_Type()
)
xgs360026fFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fFactoryDefaults.setStatus("current")


class _Xgs360026fSaveStart_Type(Integer32):
    """Custom type xgs360026fSaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fSaveStart_Type.__name__ = "Integer32"
_Xgs360026fSaveStart_Object = MibScalar
xgs360026fSaveStart = _Xgs360026fSaveStart_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 3, 2),
    _Xgs360026fSaveStart_Type()
)
xgs360026fSaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSaveStart.setStatus("current")


class _Xgs360026fSaveUser_Type(Integer32):
    """Custom type xgs360026fSaveUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fSaveUser_Type.__name__ = "Integer32"
_Xgs360026fSaveUser_Object = MibScalar
xgs360026fSaveUser = _Xgs360026fSaveUser_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 3, 3),
    _Xgs360026fSaveUser_Type()
)
xgs360026fSaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fSaveUser.setStatus("current")


class _Xgs360026fRestoreUser_Type(Integer32):
    """Custom type xgs360026fRestoreUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fRestoreUser_Type.__name__ = "Integer32"
_Xgs360026fRestoreUser_Object = MibScalar
xgs360026fRestoreUser = _Xgs360026fRestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 3, 4),
    _Xgs360026fRestoreUser_Type()
)
xgs360026fRestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fRestoreUser.setStatus("current")
_Xgs360026fExportOrImport_ObjectIdentity = ObjectIdentity
xgs360026fExportOrImport = _Xgs360026fExportOrImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 4)
)
_Xgs360026fExportIpAddress_Type = IpAddress
_Xgs360026fExportIpAddress_Object = MibScalar
xgs360026fExportIpAddress = _Xgs360026fExportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 4, 1),
    _Xgs360026fExportIpAddress_Type()
)
xgs360026fExportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fExportIpAddress.setStatus("current")
_Xgs360026fExportConfigName_Type = DisplayString
_Xgs360026fExportConfigName_Object = MibScalar
xgs360026fExportConfigName = _Xgs360026fExportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 4, 2),
    _Xgs360026fExportConfigName_Type()
)
xgs360026fExportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fExportConfigName.setStatus("current")


class _Xgs360026fDoExportConfig_Type(Integer32):
    """Custom type xgs360026fDoExportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fDoExportConfig_Type.__name__ = "Integer32"
_Xgs360026fDoExportConfig_Object = MibScalar
xgs360026fDoExportConfig = _Xgs360026fDoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 4, 3),
    _Xgs360026fDoExportConfig_Type()
)
xgs360026fDoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fDoExportConfig.setStatus("current")
_Xgs360026fImportIpAddress_Type = IpAddress
_Xgs360026fImportIpAddress_Object = MibScalar
xgs360026fImportIpAddress = _Xgs360026fImportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 4, 4),
    _Xgs360026fImportIpAddress_Type()
)
xgs360026fImportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fImportIpAddress.setStatus("current")
_Xgs360026fImportConfigName_Type = DisplayString
_Xgs360026fImportConfigName_Object = MibScalar
xgs360026fImportConfigName = _Xgs360026fImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 4, 5),
    _Xgs360026fImportConfigName_Type()
)
xgs360026fImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fImportConfigName.setStatus("current")


class _Xgs360026fDoImportConfig_Type(Integer32):
    """Custom type xgs360026fDoImportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fDoImportConfig_Type.__name__ = "Integer32"
_Xgs360026fDoImportConfig_Object = MibScalar
xgs360026fDoImportConfig = _Xgs360026fDoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 4, 6),
    _Xgs360026fDoImportConfig_Type()
)
xgs360026fDoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fDoImportConfig.setStatus("current")
_Xgs360026fDiagnostics_ObjectIdentity = ObjectIdentity
xgs360026fDiagnostics = _Xgs360026fDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5)
)
_Xgs360026fPingIpAddress_Type = IpAddress
_Xgs360026fPingIpAddress_Object = MibScalar
xgs360026fPingIpAddress = _Xgs360026fPingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 1),
    _Xgs360026fPingIpAddress_Type()
)
xgs360026fPingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPingIpAddress.setStatus("current")


class _Xgs360026fPingSize_Type(Integer32):
    """Custom type xgs360026fPingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Xgs360026fPingSize_Type.__name__ = "Integer32"
_Xgs360026fPingSize_Object = MibScalar
xgs360026fPingSize = _Xgs360026fPingSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 2),
    _Xgs360026fPingSize_Type()
)
xgs360026fPingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPingSize.setStatus("current")


class _Xgs360026fDoPingConfig_Type(Integer32):
    """Custom type xgs360026fDoPingConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fDoPingConfig_Type.__name__ = "Integer32"
_Xgs360026fDoPingConfig_Object = MibScalar
xgs360026fDoPingConfig = _Xgs360026fDoPingConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 3),
    _Xgs360026fDoPingConfig_Type()
)
xgs360026fDoPingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fDoPingConfig.setStatus("current")
_Xgs360026fPingResult_Type = DisplayString
_Xgs360026fPingResult_Object = MibScalar
xgs360026fPingResult = _Xgs360026fPingResult_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 4),
    _Xgs360026fPingResult_Type()
)
xgs360026fPingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPingResult.setStatus("current")
_Xgs360026fPing6IpAddress_Type = DisplayString
_Xgs360026fPing6IpAddress_Object = MibScalar
xgs360026fPing6IpAddress = _Xgs360026fPing6IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 5),
    _Xgs360026fPing6IpAddress_Type()
)
xgs360026fPing6IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPing6IpAddress.setStatus("current")


class _Xgs360026fPing6Size_Type(Integer32):
    """Custom type xgs360026fPing6Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Xgs360026fPing6Size_Type.__name__ = "Integer32"
_Xgs360026fPing6Size_Object = MibScalar
xgs360026fPing6Size = _Xgs360026fPing6Size_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 6),
    _Xgs360026fPing6Size_Type()
)
xgs360026fPing6Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fPing6Size.setStatus("current")


class _Xgs360026fDoPing6Config_Type(Integer32):
    """Custom type xgs360026fDoPing6Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Xgs360026fDoPing6Config_Type.__name__ = "Integer32"
_Xgs360026fDoPing6Config_Object = MibScalar
xgs360026fDoPing6Config = _Xgs360026fDoPing6Config_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 7),
    _Xgs360026fDoPing6Config_Type()
)
xgs360026fDoPing6Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fDoPing6Config.setStatus("current")
_Xgs360026fPing6Result_Type = DisplayString
_Xgs360026fPing6Result_Object = MibScalar
xgs360026fPing6Result = _Xgs360026fPing6Result_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 8),
    _Xgs360026fPing6Result_Type()
)
xgs360026fPing6Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fPing6Result.setStatus("current")
_Xgs360026fVeriPHY_ObjectIdentity = ObjectIdentity
xgs360026fVeriPHY = _Xgs360026fVeriPHY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 9)
)


class _Xgs360026fVeriPHYTest_Type(Integer32):
    """Custom type xgs360026fVeriPHYTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fVeriPHYTest_Type.__name__ = "Integer32"
_Xgs360026fVeriPHYTest_Object = MibScalar
xgs360026fVeriPHYTest = _Xgs360026fVeriPHYTest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 9, 1),
    _Xgs360026fVeriPHYTest_Type()
)
xgs360026fVeriPHYTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgs360026fVeriPHYTest.setStatus("current")
_Xgs360026fVeriPHYTable_Object = MibTable
xgs360026fVeriPHYTable = _Xgs360026fVeriPHYTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 9, 2)
)
if mibBuilder.loadTexts:
    xgs360026fVeriPHYTable.setStatus("current")
_Xgs360026fVeriPHYEntry_Object = MibTableRow
xgs360026fVeriPHYEntry = _Xgs360026fVeriPHYEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 9, 2, 1)
)
xgs360026fVeriPHYEntry.setIndexNames(
    (0, "ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fVeriPHYPort"),
)
if mibBuilder.loadTexts:
    xgs360026fVeriPHYEntry.setStatus("current")


class _Xgs360026fVeriPHYPort_Type(Integer32):
    """Custom type xgs360026fVeriPHYPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Xgs360026fVeriPHYPort_Type.__name__ = "Integer32"
_Xgs360026fVeriPHYPort_Object = MibTableColumn
xgs360026fVeriPHYPort = _Xgs360026fVeriPHYPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 9, 2, 1, 1),
    _Xgs360026fVeriPHYPort_Type()
)
xgs360026fVeriPHYPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xgs360026fVeriPHYPort.setStatus("current")
_Xgs360026fVeriPHYPairA_Type = DisplayString
_Xgs360026fVeriPHYPairA_Object = MibTableColumn
xgs360026fVeriPHYPairA = _Xgs360026fVeriPHYPairA_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 9, 2, 1, 2),
    _Xgs360026fVeriPHYPairA_Type()
)
xgs360026fVeriPHYPairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fVeriPHYPairA.setStatus("current")
_Xgs360026fVeriPHYLengthA_Type = DisplayString
_Xgs360026fVeriPHYLengthA_Object = MibTableColumn
xgs360026fVeriPHYLengthA = _Xgs360026fVeriPHYLengthA_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 9, 2, 1, 3),
    _Xgs360026fVeriPHYLengthA_Type()
)
xgs360026fVeriPHYLengthA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fVeriPHYLengthA.setStatus("current")
_Xgs360026fVeriPHYPairB_Type = DisplayString
_Xgs360026fVeriPHYPairB_Object = MibTableColumn
xgs360026fVeriPHYPairB = _Xgs360026fVeriPHYPairB_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 9, 2, 1, 4),
    _Xgs360026fVeriPHYPairB_Type()
)
xgs360026fVeriPHYPairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fVeriPHYPairB.setStatus("current")
_Xgs360026fVeriPHYLengthB_Type = DisplayString
_Xgs360026fVeriPHYLengthB_Object = MibTableColumn
xgs360026fVeriPHYLengthB = _Xgs360026fVeriPHYLengthB_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 9, 2, 1, 5),
    _Xgs360026fVeriPHYLengthB_Type()
)
xgs360026fVeriPHYLengthB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fVeriPHYLengthB.setStatus("current")
_Xgs360026fVeriPHYPairC_Type = DisplayString
_Xgs360026fVeriPHYPairC_Object = MibTableColumn
xgs360026fVeriPHYPairC = _Xgs360026fVeriPHYPairC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 9, 2, 1, 6),
    _Xgs360026fVeriPHYPairC_Type()
)
xgs360026fVeriPHYPairC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fVeriPHYPairC.setStatus("current")
_Xgs360026fVeriPHYLengthC_Type = DisplayString
_Xgs360026fVeriPHYLengthC_Object = MibTableColumn
xgs360026fVeriPHYLengthC = _Xgs360026fVeriPHYLengthC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 9, 2, 1, 7),
    _Xgs360026fVeriPHYLengthC_Type()
)
xgs360026fVeriPHYLengthC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fVeriPHYLengthC.setStatus("current")
_Xgs360026fVeriPHYPairD_Type = DisplayString
_Xgs360026fVeriPHYPairD_Object = MibTableColumn
xgs360026fVeriPHYPairD = _Xgs360026fVeriPHYPairD_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 9, 2, 1, 8),
    _Xgs360026fVeriPHYPairD_Type()
)
xgs360026fVeriPHYPairD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fVeriPHYPairD.setStatus("current")
_Xgs360026fVeriPHYLengthD_Type = DisplayString
_Xgs360026fVeriPHYLengthD_Object = MibTableColumn
xgs360026fVeriPHYLengthD = _Xgs360026fVeriPHYLengthD_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 4, 5, 9, 2, 1, 9),
    _Xgs360026fVeriPHYLengthD_Type()
)
xgs360026fVeriPHYLengthD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fVeriPHYLengthD.setStatus("current")
_Xgs360026fTrap_ObjectIdentity = ObjectIdentity
xgs360026fTrap = _Xgs360026fTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 5)
)
_Xgs360026fTrapEvent_ObjectIdentity = ObjectIdentity
xgs360026fTrapEvent = _Xgs360026fTrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 5, 1)
)
_Xgs360026fTrapVariable_ObjectIdentity = ObjectIdentity
xgs360026fTrapVariable = _Xgs360026fTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 5, 2)
)
_Xgs360026fInformation_Type = DisplayString
_Xgs360026fInformation_Object = MibScalar
xgs360026fInformation = _Xgs360026fInformation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 5, 2, 1),
    _Xgs360026fInformation_Type()
)
xgs360026fInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgs360026fInformation.setStatus("current")

# Managed Objects groups


# Notification objects

xgs360026fEmergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 5, 1, 1)
)
xgs360026fEmergency.setObjects(
    ("ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fInformation")
)
if mibBuilder.loadTexts:
    xgs360026fEmergency.setStatus(
        "current"
    )

xgs360026fAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 5, 1, 2)
)
xgs360026fAlert.setObjects(
    ("ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fInformation")
)
if mibBuilder.loadTexts:
    xgs360026fAlert.setStatus(
        "current"
    )

xgs360026fCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 5, 1, 3)
)
xgs360026fCritical.setObjects(
    ("ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fInformation")
)
if mibBuilder.loadTexts:
    xgs360026fCritical.setStatus(
        "current"
    )

xgs360026fError = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 5, 1, 4)
)
xgs360026fError.setObjects(
    ("ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fInformation")
)
if mibBuilder.loadTexts:
    xgs360026fError.setStatus(
        "current"
    )

xgs360026fWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 5, 1, 5)
)
xgs360026fWarning.setObjects(
    ("ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fInformation")
)
if mibBuilder.loadTexts:
    xgs360026fWarning.setStatus(
        "current"
    )

xgs360026fNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 5, 1, 6)
)
xgs360026fNotice.setObjects(
    ("ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fInformation")
)
if mibBuilder.loadTexts:
    xgs360026fNotice.setStatus(
        "current"
    )

xgs360026fInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 5, 1, 7)
)
xgs360026fInformational.setObjects(
    ("ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fInformation")
)
if mibBuilder.loadTexts:
    xgs360026fInformational.setStatus(
        "current"
    )

xgs360026fDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 77, 5, 1, 8)
)
xgs360026fDebug.setObjects(
    ("ZYXEL-XGS360026F-FUNCTION-MIB", "xgs360026fInformation")
)
if mibBuilder.loadTexts:
    xgs360026fDebug.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-XGS360026F-FUNCTION-MIB",
    **{"zyxel": zyxel,
       "products": products,
       "accessSwitch": accessSwitch,
       "esSeries": esSeries,
       "xgs360026fProductId": xgs360026fProductId,
       "xgs360026fSystem": xgs360026fSystem,
       "xgs360026fSystemInformation": xgs360026fSystemInformation,
       "xgs360026fModelName": xgs360026fModelName,
       "xgs360026fBIOSVersion": xgs360026fBIOSVersion,
       "xgs360026fFirmwareVersion": xgs360026fFirmwareVersion,
       "xgs360026fHardwareMechanicalVersion": xgs360026fHardwareMechanicalVersion,
       "xgs360026fSeriesNumber": xgs360026fSeriesNumber,
       "xgs360026fHostMACAddress": xgs360026fHostMACAddress,
       "xgs360026fConsoleBaudrate": xgs360026fConsoleBaudrate,
       "xgs360026fRAMSize": xgs360026fRAMSize,
       "xgs360026fFlashSize": xgs360026fFlashSize,
       "xgs360026fBridgeFBDSize": xgs360026fBridgeFBDSize,
       "xgs360026fTransmitQueue": xgs360026fTransmitQueue,
       "xgs360026fMaximumFrameSize": xgs360026fMaximumFrameSize,
       "xgs360026fCPULoad": xgs360026fCPULoad,
       "xgs360026fFanSpeed": xgs360026fFanSpeed,
       "xgs360026fPowers": xgs360026fPowers,
       "xgs360026fTemperature1": xgs360026fTemperature1,
       "xgs360026fTemperature2": xgs360026fTemperature2,
       "xgs360026fTemperature3": xgs360026fTemperature3,
       "xgs360026fTemperature4": xgs360026fTemperature4,
       "xgs360026fSystemTime": xgs360026fSystemTime,
       "xgs360026fSystemTimeManual": xgs360026fSystemTimeManual,
       "xgs360026fSystemTimeManualClockSource": xgs360026fSystemTimeManualClockSource,
       "xgs360026fSystemTimeManualLocaltime": xgs360026fSystemTimeManualLocaltime,
       "xgs360026fSystemTimeManualTimeZoneOffset": xgs360026fSystemTimeManualTimeZoneOffset,
       "xgs360026fSystemTimeManualDaylightSavings": xgs360026fSystemTimeManualDaylightSavings,
       "xgs360026fSystemTimeManualTimeSetOffset": xgs360026fSystemTimeManualTimeSetOffset,
       "xgs360026fSystemTimeManualDaylightSavingsType": xgs360026fSystemTimeManualDaylightSavingsType,
       "xgs360026fSystemTimeManualDaylightSavingsBydatesFrom": xgs360026fSystemTimeManualDaylightSavingsBydatesFrom,
       "xgs360026fSystemTimeManualDaylightSavingsBydatesTo": xgs360026fSystemTimeManualDaylightSavingsBydatesTo,
       "xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom": xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom,
       "xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom": xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom,
       "xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom": xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom,
       "xgs360026fSystemTimeManualDaylightSavingsRecurringTimeFrom": xgs360026fSystemTimeManualDaylightSavingsRecurringTimeFrom,
       "xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo": xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo,
       "xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo": xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo,
       "xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo": xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo,
       "xgs360026fSystemTimeManualDaylightSavingsRecurringTimeTo": xgs360026fSystemTimeManualDaylightSavingsRecurringTimeTo,
       "xgs360026fSystemTimeNTP": xgs360026fSystemTimeNTP,
       "xgs360026fSystemTimeNTPTable": xgs360026fSystemTimeNTPTable,
       "xgs360026fSystemTimeNTPEntry": xgs360026fSystemTimeNTPEntry,
       "xgs360026fSystemTimeNTPIndex": xgs360026fSystemTimeNTPIndex,
       "xgs360026fSystemTimeNTPServerIPType": xgs360026fSystemTimeNTPServerIPType,
       "xgs360026fSystemTimeNTPServer": xgs360026fSystemTimeNTPServer,
       "xgs360026fSystemTimeNTPCurrentMode": xgs360026fSystemTimeNTPCurrentMode,
       "xgs360026fSystemAccount": xgs360026fSystemAccount,
       "xgs360026fSystemAccountUsers": xgs360026fSystemAccountUsers,
       "xgs360026fSystemAccountUserCreate": xgs360026fSystemAccountUserCreate,
       "xgs360026fSystemAccountUsersTable": xgs360026fSystemAccountUsersTable,
       "xgs360026fSystemAccountUsersEntry": xgs360026fSystemAccountUsersEntry,
       "xgs360026fUserIndex": xgs360026fUserIndex,
       "xgs360026fUserName": xgs360026fUserName,
       "xgs360026fPassword": xgs360026fPassword,
       "xgs360026fUserPrivilegeLevel": xgs360026fUserPrivilegeLevel,
       "xgs360026fAccountUserRowStatus": xgs360026fAccountUserRowStatus,
       "xgs360026fSystemAccountPrivilegeLevel": xgs360026fSystemAccountPrivilegeLevel,
       "xgs360026fAccountPrivilegeLevel": xgs360026fAccountPrivilegeLevel,
       "xgs360026fAggregationPrivilegeLevel": xgs360026fAggregationPrivilegeLevel,
       "xgs360026fDiagnosticsPrivilegeLevel": xgs360026fDiagnosticsPrivilegeLevel,
       "xgs360026fEPSPrivilegeLevel": xgs360026fEPSPrivilegeLevel,
       "xgs360026fERPSPrivilegeLevel": xgs360026fERPSPrivilegeLevel,
       "xgs360026fETHLinkOAMPrivilegeLevel": xgs360026fETHLinkOAMPrivilegeLevel,
       "xgs360026fEVCPrivilegeLevel": xgs360026fEVCPrivilegeLevel,
       "xgs360026fGARPPrivilegeLevel": xgs360026fGARPPrivilegeLevel,
       "xgs360026fGVRPPrivilegeLevel": xgs360026fGVRPPrivilegeLevel,
       "xgs360026fIPPrivilegeLevel": xgs360026fIPPrivilegeLevel,
       "xgs360026fIPMCSnoopingPrivilegeLevel": xgs360026fIPMCSnoopingPrivilegeLevel,
       "xgs360026fLACPPrivilegeLevel": xgs360026fLACPPrivilegeLevel,
       "xgs360026fLLDPPrivilegeLevel": xgs360026fLLDPPrivilegeLevel,
       "xgs360026fLLDPMEDPrivilegeLevel": xgs360026fLLDPMEDPrivilegeLevel,
       "xgs360026fLoopProtectPrivilegeLevel": xgs360026fLoopProtectPrivilegeLevel,
       "xgs360026fMACTablePrivilegeLevel": xgs360026fMACTablePrivilegeLevel,
       "xgs360026fMEPPrivilegeLevel": xgs360026fMEPPrivilegeLevel,
       "xgs360026fMRSTPPrivilegeLevel": xgs360026fMRSTPPrivilegeLevel,
       "xgs360026fMVRPrivilegeLevel": xgs360026fMVRPrivilegeLevel,
       "xgs360026fMaintenancePrivilegeLevel": xgs360026fMaintenancePrivilegeLevel,
       "xgs360026fMirroringPrivilegeLevel": xgs360026fMirroringPrivilegeLevel,
       "xgs360026fPTPPrivilegeLevel": xgs360026fPTPPrivilegeLevel,
       "xgs360026fPortsPrivilegeLevel": xgs360026fPortsPrivilegeLevel,
       "xgs360026fPrivateVLANsPrivilegeLevel": xgs360026fPrivateVLANsPrivilegeLevel,
       "xgs360026fQoSPrivilegeLevel": xgs360026fQoSPrivilegeLevel,
       "xgs360026fSMTPPrivilegeLevel": xgs360026fSMTPPrivilegeLevel,
       "xgs360026fSNMPPrivilegeLevel": xgs360026fSNMPPrivilegeLevel,
       "xgs360026fSecurityPrivilegeLevel": xgs360026fSecurityPrivilegeLevel,
       "xgs360026fSpanningTreePrivilegeLevel": xgs360026fSpanningTreePrivilegeLevel,
       "xgs360026fSystemPrivilegeLevel": xgs360026fSystemPrivilegeLevel,
       "xgs360026fTrapEventPrivilegeLevel": xgs360026fTrapEventPrivilegeLevel,
       "xgs360026fVCLPrivilegeLevel": xgs360026fVCLPrivilegeLevel,
       "xgs360026fVLANTranslationPrivilegeLevel": xgs360026fVLANTranslationPrivilegeLevel,
       "xgs360026fVLANsPrivilegeLevel": xgs360026fVLANsPrivilegeLevel,
       "xgs360026fIP": xgs360026fIP,
       "xgs360026fIPv4": xgs360026fIPv4,
       "xgs360026fIPv4Configured": xgs360026fIPv4Configured,
       "xgs360026fIpv4DHCPClient": xgs360026fIpv4DHCPClient,
       "xgs360026fIPv4Address": xgs360026fIPv4Address,
       "xgs360026fIPv4Mask": xgs360026fIPv4Mask,
       "xgs360026fIPv4Router": xgs360026fIPv4Router,
       "xgs360026fIPv4VLANId": xgs360026fIPv4VLANId,
       "xgs360026fIPv4DNSServer": xgs360026fIPv4DNSServer,
       "xgs360026fIPv4DNSProxy": xgs360026fIPv4DNSProxy,
       "xgs360026fIPv4Current": xgs360026fIPv4Current,
       "xgs360026fIpv4CurrentDHCPClient": xgs360026fIpv4CurrentDHCPClient,
       "xgs360026fIPv4CurrentAddress": xgs360026fIPv4CurrentAddress,
       "xgs360026fIPv4CurrentMask": xgs360026fIPv4CurrentMask,
       "xgs360026fIPv4CurrentRouter": xgs360026fIPv4CurrentRouter,
       "xgs360026fIPv4CurrentVLANId": xgs360026fIPv4CurrentVLANId,
       "xgs360026fIPv4CurrentDNSServer": xgs360026fIPv4CurrentDNSServer,
       "xgs360026fIPv6": xgs360026fIPv6,
       "xgs360026fIPv6Configured": xgs360026fIPv6Configured,
       "xgs360026fIpv6AutoConfiguration": xgs360026fIpv6AutoConfiguration,
       "xgs360026fIpv6Address": xgs360026fIpv6Address,
       "xgs360026fIpv6Prefix": xgs360026fIpv6Prefix,
       "xgs360026fIpv6Router": xgs360026fIpv6Router,
       "xgs360026fIPv6Current": xgs360026fIPv6Current,
       "xgs360026fIpv6CurrentAutoConfiguration": xgs360026fIpv6CurrentAutoConfiguration,
       "xgs360026fIpv6CurrentAddress": xgs360026fIpv6CurrentAddress,
       "xgs360026fIpv6CurrentLinkLocalAddress": xgs360026fIpv6CurrentLinkLocalAddress,
       "xgs360026fIpv6CurrentPrefix": xgs360026fIpv6CurrentPrefix,
       "xgs360026fIpv6CurrentRouter": xgs360026fIpv6CurrentRouter,
       "xgs360026fSyslog": xgs360026fSyslog,
       "xgs360026fSyslogConf": xgs360026fSyslogConf,
       "xgs360026fServerMode": xgs360026fServerMode,
       "xgs360026fServerAddress1": xgs360026fServerAddress1,
       "xgs360026fServerAddress2": xgs360026fServerAddress2,
       "xgs360026fSyslogLevel": xgs360026fSyslogLevel,
       "xgs360026fSyslogDetailedInfo": xgs360026fSyslogDetailedInfo,
       "xgs360026fSyslogDetailedInfoClear": xgs360026fSyslogDetailedInfoClear,
       "xgs360026fSyslogDetailedInfoTable": xgs360026fSyslogDetailedInfoTable,
       "xgs360026fSyslogDetailedInfoEntry": xgs360026fSyslogDetailedInfoEntry,
       "xgs360026fSyslogDetailedInfoIndex": xgs360026fSyslogDetailedInfoIndex,
       "xgs360026fSyslogDetailedInfoLevel": xgs360026fSyslogDetailedInfoLevel,
       "xgs360026fSyslogDetailedInfoTime": xgs360026fSyslogDetailedInfoTime,
       "xgs360026fSyslogDetailedInfoMessage": xgs360026fSyslogDetailedInfoMessage,
       "xgs360026fSnmp": xgs360026fSnmp,
       "xgs360026fSnmpConf": xgs360026fSnmpConf,
       "xgs360026fGetCommunity": xgs360026fGetCommunity,
       "xgs360026fSetCommunityMode": xgs360026fSetCommunityMode,
       "xgs360026fSetCommunity": xgs360026fSetCommunity,
       "xgs360026fTrapHostConfTable": xgs360026fTrapHostConfTable,
       "xgs360026fTrapHostConfEntry": xgs360026fTrapHostConfEntry,
       "xgs360026fTrapHostConfIndex": xgs360026fTrapHostConfIndex,
       "xgs360026fTrapHostConfVersion": xgs360026fTrapHostConfVersion,
       "xgs360026fTrapHostConfIPType": xgs360026fTrapHostConfIPType,
       "xgs360026fTrapHostConfIP": xgs360026fTrapHostConfIP,
       "xgs360026fTrapHostConfPort": xgs360026fTrapHostConfPort,
       "xgs360026fTrapHostConfCommunity": xgs360026fTrapHostConfCommunity,
       "xgs360026fTrapHostConfSeverityLevel": xgs360026fTrapHostConfSeverityLevel,
       "xgs360026fTrapHostConfSecurityLevel": xgs360026fTrapHostConfSecurityLevel,
       "xgs360026fTrapHostConfAuthPtc": xgs360026fTrapHostConfAuthPtc,
       "xgs360026fTrapHostConfAuthPassword": xgs360026fTrapHostConfAuthPassword,
       "xgs360026fTrapHostConfPrivPtc": xgs360026fTrapHostConfPrivPtc,
       "xgs360026fTrapHostConfPrivPassword": xgs360026fTrapHostConfPrivPassword,
       "xgs360026fTrapHostConfCurrentMode": xgs360026fTrapHostConfCurrentMode,
       "xgs360026fConfiguration": xgs360026fConfiguration,
       "xgs360026fPort": xgs360026fPort,
       "xgs360026fPortConfigurationTable": xgs360026fPortConfigurationTable,
       "xgs360026fPortConfigurationEntry": xgs360026fPortConfigurationEntry,
       "xgs360026fPortConfPort": xgs360026fPortConfPort,
       "xgs360026fPortConfPortMedia": xgs360026fPortConfPortMedia,
       "xgs360026fPortConfLink": xgs360026fPortConfLink,
       "xgs360026fPortConfCurrentSpeed": xgs360026fPortConfCurrentSpeed,
       "xgs360026fPortConfSpeed": xgs360026fPortConfSpeed,
       "xgs360026fPortConfCurrentFlowControlRx": xgs360026fPortConfCurrentFlowControlRx,
       "xgs360026fPortConfCurrentFlowControlTx": xgs360026fPortConfCurrentFlowControlTx,
       "xgs360026fPortConfFlowControl": xgs360026fPortConfFlowControl,
       "xgs360026fPortConfMaxFrameSize": xgs360026fPortConfMaxFrameSize,
       "xgs360026fPortConfExcessiveCollisionMode": xgs360026fPortConfExcessiveCollisionMode,
       "xgs360026fPortConfPowerControl": xgs360026fPortConfPowerControl,
       "xgs360026fPortConfDescription": xgs360026fPortConfDescription,
       "xgs360026fPortTrafficStatisticsTable": xgs360026fPortTrafficStatisticsTable,
       "xgs360026fPortTrafficStatisticsEntry": xgs360026fPortTrafficStatisticsEntry,
       "xgs360026fPortTrafficStatisticsPort": xgs360026fPortTrafficStatisticsPort,
       "xgs360026fPortTrafficStatisticsClear": xgs360026fPortTrafficStatisticsClear,
       "xgs360026fPortTrafficRxPackets": xgs360026fPortTrafficRxPackets,
       "xgs360026fPortTrafficRxOctets": xgs360026fPortTrafficRxOctets,
       "xgs360026fPortTrafficRxUnicast": xgs360026fPortTrafficRxUnicast,
       "xgs360026fPortTrafficRxMulticast": xgs360026fPortTrafficRxMulticast,
       "xgs360026fPortTrafficRxBroadcast": xgs360026fPortTrafficRxBroadcast,
       "xgs360026fPortTrafficRxPause": xgs360026fPortTrafficRxPause,
       "xgs360026fPortTrafficRx64Bytes": xgs360026fPortTrafficRx64Bytes,
       "xgs360026fPortTrafficRx65to127Bytes": xgs360026fPortTrafficRx65to127Bytes,
       "xgs360026fPortTrafficRx128to255Bytes": xgs360026fPortTrafficRx128to255Bytes,
       "xgs360026fPortTrafficRx256to511Bytes": xgs360026fPortTrafficRx256to511Bytes,
       "xgs360026fPortTrafficRx512to1023Bytes": xgs360026fPortTrafficRx512to1023Bytes,
       "xgs360026fPortTrafficRx1024to1526Bytes": xgs360026fPortTrafficRx1024to1526Bytes,
       "xgs360026fPortTrafficRxExceecd1527Bytes": xgs360026fPortTrafficRxExceecd1527Bytes,
       "xgs360026fPortTrafficRxQ0": xgs360026fPortTrafficRxQ0,
       "xgs360026fPortTrafficRxQ1": xgs360026fPortTrafficRxQ1,
       "xgs360026fPortTrafficRxQ2": xgs360026fPortTrafficRxQ2,
       "xgs360026fPortTrafficRxQ3": xgs360026fPortTrafficRxQ3,
       "xgs360026fPortTrafficRxQ4": xgs360026fPortTrafficRxQ4,
       "xgs360026fPortTrafficRxQ5": xgs360026fPortTrafficRxQ5,
       "xgs360026fPortTrafficRxQ6": xgs360026fPortTrafficRxQ6,
       "xgs360026fPortTrafficRxQ7": xgs360026fPortTrafficRxQ7,
       "xgs360026fPortTrafficRxDrops": xgs360026fPortTrafficRxDrops,
       "xgs360026fPortTrafficRxCRCorAlignment": xgs360026fPortTrafficRxCRCorAlignment,
       "xgs360026fPortTrafficRxUndersize": xgs360026fPortTrafficRxUndersize,
       "xgs360026fPortTrafficRxOversize": xgs360026fPortTrafficRxOversize,
       "xgs360026fPortTrafficRxFragments": xgs360026fPortTrafficRxFragments,
       "xgs360026fPortTrafficRxJabber": xgs360026fPortTrafficRxJabber,
       "xgs360026fPortTrafficRxFiltered": xgs360026fPortTrafficRxFiltered,
       "xgs360026fPortTrafficTxPackets": xgs360026fPortTrafficTxPackets,
       "xgs360026fPortTrafficTxOctets": xgs360026fPortTrafficTxOctets,
       "xgs360026fPortTrafficTxUnicast": xgs360026fPortTrafficTxUnicast,
       "xgs360026fPortTrafficTxMulticast": xgs360026fPortTrafficTxMulticast,
       "xgs360026fPortTrafficTxBroadcast": xgs360026fPortTrafficTxBroadcast,
       "xgs360026fPortTrafficTxPause": xgs360026fPortTrafficTxPause,
       "xgs360026fPortTrafficTx64Bytes": xgs360026fPortTrafficTx64Bytes,
       "xgs360026fPortTrafficTx65to127Bytes": xgs360026fPortTrafficTx65to127Bytes,
       "xgs360026fPortTrafficTx128to255Bytes": xgs360026fPortTrafficTx128to255Bytes,
       "xgs360026fPortTrafficTx256to511Bytes": xgs360026fPortTrafficTx256to511Bytes,
       "xgs360026fPortTrafficTx512to1023Bytes": xgs360026fPortTrafficTx512to1023Bytes,
       "xgs360026fPortTrafficTx1024to1526Bytes": xgs360026fPortTrafficTx1024to1526Bytes,
       "xgs360026fPortTrafficTxExceecd1527Bytes": xgs360026fPortTrafficTxExceecd1527Bytes,
       "xgs360026fPortTrafficTxQ0": xgs360026fPortTrafficTxQ0,
       "xgs360026fPortTrafficTxQ1": xgs360026fPortTrafficTxQ1,
       "xgs360026fPortTrafficTxQ2": xgs360026fPortTrafficTxQ2,
       "xgs360026fPortTrafficTxQ3": xgs360026fPortTrafficTxQ3,
       "xgs360026fPortTrafficTxQ4": xgs360026fPortTrafficTxQ4,
       "xgs360026fPortTrafficTxQ5": xgs360026fPortTrafficTxQ5,
       "xgs360026fPortTrafficTxQ6": xgs360026fPortTrafficTxQ6,
       "xgs360026fPortTrafficTxQ7": xgs360026fPortTrafficTxQ7,
       "xgs360026fPortTrafficTxDrops": xgs360026fPortTrafficTxDrops,
       "xgs360026fPortTrafficTxLateOrExcColl": xgs360026fPortTrafficTxLateOrExcColl,
       "xgs360026fPortQoSStatistics": xgs360026fPortQoSStatistics,
       "xgs360026fPortQoSStatisticsClear": xgs360026fPortQoSStatisticsClear,
       "xgs360026fPortQoSStatisticsTable": xgs360026fPortQoSStatisticsTable,
       "xgs360026fPortQoSStatisticsEntry": xgs360026fPortQoSStatisticsEntry,
       "xgs360026fPortQoSStatisticsPort": xgs360026fPortQoSStatisticsPort,
       "xgs360026fPortQoSQ0Rx": xgs360026fPortQoSQ0Rx,
       "xgs360026fPortQoSQ0Tx": xgs360026fPortQoSQ0Tx,
       "xgs360026fPortQoSQ1Rx": xgs360026fPortQoSQ1Rx,
       "xgs360026fPortQoSQ1Tx": xgs360026fPortQoSQ1Tx,
       "xgs360026fPortQoSQ2Rx": xgs360026fPortQoSQ2Rx,
       "xgs360026fPortQoSQ2Tx": xgs360026fPortQoSQ2Tx,
       "xgs360026fPortQoSQ3Rx": xgs360026fPortQoSQ3Rx,
       "xgs360026fPortQoSQ3Tx": xgs360026fPortQoSQ3Tx,
       "xgs360026fPortQoSQ4Rx": xgs360026fPortQoSQ4Rx,
       "xgs360026fPortQoSQ4Tx": xgs360026fPortQoSQ4Tx,
       "xgs360026fPortQoSQ5Rx": xgs360026fPortQoSQ5Rx,
       "xgs360026fPortQoSQ5Tx": xgs360026fPortQoSQ5Tx,
       "xgs360026fPortQoSQ6Rx": xgs360026fPortQoSQ6Rx,
       "xgs360026fPortQoSQ6Tx": xgs360026fPortQoSQ6Tx,
       "xgs360026fPortQoSQ7Rx": xgs360026fPortQoSQ7Rx,
       "xgs360026fPortQoSQ7Tx": xgs360026fPortQoSQ7Tx,
       "xgs360026fSFPInfoTable": xgs360026fSFPInfoTable,
       "xgs360026fSFPInfoEntry": xgs360026fSFPInfoEntry,
       "xgs360026fSFPInfoIndex": xgs360026fSFPInfoIndex,
       "xgs360026fSFPInfoPort": xgs360026fSFPInfoPort,
       "xgs360026fSFPConnectorType": xgs360026fSFPConnectorType,
       "xgs360026fSFPFiberType": xgs360026fSFPFiberType,
       "xgs360026fSFPTxCentralWavelength": xgs360026fSFPTxCentralWavelength,
       "xgs360026fSFPBaudRate": xgs360026fSFPBaudRate,
       "xgs360026fSFPVendorOUI": xgs360026fSFPVendorOUI,
       "xgs360026fSFPVendorName": xgs360026fSFPVendorName,
       "xgs360026fSFPVendorPN": xgs360026fSFPVendorPN,
       "xgs360026fSFPVendorRev": xgs360026fSFPVendorRev,
       "xgs360026fSFPVendorSN": xgs360026fSFPVendorSN,
       "xgs360026fSFPDateCode": xgs360026fSFPDateCode,
       "xgs360026fSFPTemperature": xgs360026fSFPTemperature,
       "xgs360026fSFPVcc": xgs360026fSFPVcc,
       "xgs360026fSFPMon1Bias": xgs360026fSFPMon1Bias,
       "xgs360026fSFPMon2TxPWR": xgs360026fSFPMon2TxPWR,
       "xgs360026fSFPMon3RxPWR": xgs360026fSFPMon3RxPWR,
       "xgs360026fGARP": xgs360026fGARP,
       "xgs360026fGARPConfTable": xgs360026fGARPConfTable,
       "xgs360026fGARPConfEntry": xgs360026fGARPConfEntry,
       "xgs360026fGARPConfPort": xgs360026fGARPConfPort,
       "xgs360026fGARPJoinTimer": xgs360026fGARPJoinTimer,
       "xgs360026fGARPLeaveTimer": xgs360026fGARPLeaveTimer,
       "xgs360026fGARPLeaveAllTimer": xgs360026fGARPLeaveAllTimer,
       "xgs360026fGARPApplicantion": xgs360026fGARPApplicantion,
       "xgs360026fGARPAttributeType": xgs360026fGARPAttributeType,
       "xgs360026fGARPApplicant": xgs360026fGARPApplicant,
       "xgs360026fGARPStatisticsTable": xgs360026fGARPStatisticsTable,
       "xgs360026fGARPStatisticsEntry": xgs360026fGARPStatisticsEntry,
       "xgs360026fGARPStatisticsPort": xgs360026fGARPStatisticsPort,
       "xgs360026fGARPStatisticsPeerMAC": xgs360026fGARPStatisticsPeerMAC,
       "xgs360026fGARPStatisticsFailedCount": xgs360026fGARPStatisticsFailedCount,
       "xgs360026fGVRP": xgs360026fGVRP,
       "xgs360026fGVRPConf": xgs360026fGVRPConf,
       "xgs360026fGVRPMode": xgs360026fGVRPMode,
       "xgs360026fGVRPConfTable": xgs360026fGVRPConfTable,
       "xgs360026fGVRPConfEntry": xgs360026fGVRPConfEntry,
       "xgs360026fGVRPConfPort": xgs360026fGVRPConfPort,
       "xgs360026fGVRPConfPortMode": xgs360026fGVRPConfPortMode,
       "xgs360026fGVRPConfPortRRole": xgs360026fGVRPConfPortRRole,
       "xgs360026fGVRPStatisticsTable": xgs360026fGVRPStatisticsTable,
       "xgs360026fGVRPStatisticsEntry": xgs360026fGVRPStatisticsEntry,
       "xgs360026fGVRPStatisticsPort": xgs360026fGVRPStatisticsPort,
       "xgs360026fGVRPStatisticsJoinTxCnt": xgs360026fGVRPStatisticsJoinTxCnt,
       "xgs360026fGVRPStatisticsLeaveTxCnt": xgs360026fGVRPStatisticsLeaveTxCnt,
       "xgs360026fThermalProtection": xgs360026fThermalProtection,
       "xgs360026fPriority0Temperature": xgs360026fPriority0Temperature,
       "xgs360026fPriority1Temperature": xgs360026fPriority1Temperature,
       "xgs360026fPriority2Temperature": xgs360026fPriority2Temperature,
       "xgs360026fPriority3Temperature": xgs360026fPriority3Temperature,
       "xgs360026fThermalProtectionTable": xgs360026fThermalProtectionTable,
       "xgs360026fThermalProtectionEntry": xgs360026fThermalProtectionEntry,
       "xgs360026fThermalProtectionPort": xgs360026fThermalProtectionPort,
       "xgs360026fThermalProtectionPortTemperature": xgs360026fThermalProtectionPortTemperature,
       "xgs360026fThermalProtectionPortPriority": xgs360026fThermalProtectionPortPriority,
       "xgs360026fThermalProtectionPortStatus": xgs360026fThermalProtectionPortStatus,
       "xgs360026fMirroring": xgs360026fMirroring,
       "xgs360026fPortToMirrorOn": xgs360026fPortToMirrorOn,
       "xgs360026fMirrorTable": xgs360026fMirrorTable,
       "xgs360026fMirrorEntry": xgs360026fMirrorEntry,
       "xgs360026fMirrorPort": xgs360026fMirrorPort,
       "xgs360026fMirrorMode": xgs360026fMirrorMode,
       "xgs360026fTrapEventSeverity": xgs360026fTrapEventSeverity,
       "xgs360026fTrapEventSeverityACL": xgs360026fTrapEventSeverityACL,
       "xgs360026fTrapEventSeverityACLLog": xgs360026fTrapEventSeverityACLLog,
       "xgs360026fTrapEventSeverityAccessMgmt": xgs360026fTrapEventSeverityAccessMgmt,
       "xgs360026fTrapEventSeverityAuthFailed": xgs360026fTrapEventSeverityAuthFailed,
       "xgs360026fTrapEventSeverityColdStart": xgs360026fTrapEventSeverityColdStart,
       "xgs360026fTrapEventSeverityConfigInfo": xgs360026fTrapEventSeverityConfigInfo,
       "xgs360026fTrapEventSeverityFirmwareUpgrade": xgs360026fTrapEventSeverityFirmwareUpgrade,
       "xgs360026fTrapEventSeverityImportExport": xgs360026fTrapEventSeverityImportExport,
       "xgs360026fTrapEventSeverityLACP": xgs360026fTrapEventSeverityLACP,
       "xgs360026fTrapEventSeverityLinkStatus": xgs360026fTrapEventSeverityLinkStatus,
       "xgs360026fTrapEventSeverityLogin": xgs360026fTrapEventSeverityLogin,
       "xgs360026fTrapEventSeverityLogout": xgs360026fTrapEventSeverityLogout,
       "xgs360026fTrapEventSeverityLoopProtect": xgs360026fTrapEventSeverityLoopProtect,
       "xgs360026fTrapEventSeverityMgmtIPChange": xgs360026fTrapEventSeverityMgmtIPChange,
       "xgs360026fTrapEventSeverityModuleChange": xgs360026fTrapEventSeverityModuleChange,
       "xgs360026fTrapEventSeverityNAS": xgs360026fTrapEventSeverityNAS,
       "xgs360026fTrapEventSeverityPasswdChange": xgs360026fTrapEventSeverityPasswdChange,
       "xgs360026fTrapEventSeverityPortSecurity": xgs360026fTrapEventSeverityPortSecurity,
       "xgs360026fTrapEventSeverityThermalProtect": xgs360026fTrapEventSeverityThermalProtect,
       "xgs360026fTrapEventSeverityVLAN": xgs360026fTrapEventSeverityVLAN,
       "xgs360026fTrapEventSeverityWarmStart": xgs360026fTrapEventSeverityWarmStart,
       "xgs360026fSMTP": xgs360026fSMTP,
       "xgs360026fSMTPMailServer": xgs360026fSMTPMailServer,
       "xgs360026fSMTPUserName": xgs360026fSMTPUserName,
       "xgs360026fSMTPPassword": xgs360026fSMTPPassword,
       "xgs360026fSMTPServeriryLevel": xgs360026fSMTPServeriryLevel,
       "xgs360026fSMTPSender": xgs360026fSMTPSender,
       "xgs360026fSMTPReturnPath": xgs360026fSMTPReturnPath,
       "xgs360026fSMTPEmailAddress1": xgs360026fSMTPEmailAddress1,
       "xgs360026fSMTPEmailAddress2": xgs360026fSMTPEmailAddress2,
       "xgs360026fSMTPEmailAddress3": xgs360026fSMTPEmailAddress3,
       "xgs360026fSMTPEmailAddress4": xgs360026fSMTPEmailAddress4,
       "xgs360026fSMTPEmailAddress5": xgs360026fSMTPEmailAddress5,
       "xgs360026fSMTPEmailAddress6": xgs360026fSMTPEmailAddress6,
       "xgs360026fACL": xgs360026fACL,
       "xgs360026fACLPortsConfTable": xgs360026fACLPortsConfTable,
       "xgs360026fACLPortsConfEntry": xgs360026fACLPortsConfEntry,
       "xgs360026fACLPortsConfPort": xgs360026fACLPortsConfPort,
       "xgs360026fACLPortsConfPolicyID": xgs360026fACLPortsConfPolicyID,
       "xgs360026fACLPortsConfAction": xgs360026fACLPortsConfAction,
       "xgs360026fACLPortsConfRateLimiterID": xgs360026fACLPortsConfRateLimiterID,
       "xgs360026fACLPortsConfPortRedirect": xgs360026fACLPortsConfPortRedirect,
       "xgs360026fACLPortsConfLogging": xgs360026fACLPortsConfLogging,
       "xgs360026fACLPortsConfShutdown": xgs360026fACLPortsConfShutdown,
       "xgs360026fACLPortsConfState": xgs360026fACLPortsConfState,
       "xgs360026fACLPortsConfCounter": xgs360026fACLPortsConfCounter,
       "xgs360026fACLRateLimiterTable": xgs360026fACLRateLimiterTable,
       "xgs360026fACLRateLimiterEntry": xgs360026fACLRateLimiterEntry,
       "xgs360026fACLRateLimiterID": xgs360026fACLRateLimiterID,
       "xgs360026fACLRateLimiterRate": xgs360026fACLRateLimiterRate,
       "xgs360026fACLACE": xgs360026fACLACE,
       "xgs360026fACLACECreate": xgs360026fACLACECreate,
       "xgs360026fACLACETable": xgs360026fACLACETable,
       "xgs360026fACLACEEntry": xgs360026fACLACEEntry,
       "xgs360026fACLACEIndex": xgs360026fACLACEIndex,
       "xgs360026fACLACEID": xgs360026fACLACEID,
       "xgs360026fACLACENextID": xgs360026fACLACENextID,
       "xgs360026fACLACEIngressPort": xgs360026fACLACEIngressPort,
       "xgs360026fACLACEPortPolicyNumber": xgs360026fACLACEPortPolicyNumber,
       "xgs360026fACLACEPortPolicyBitmask": xgs360026fACLACEPortPolicyBitmask,
       "xgs360026fACLACEFrameType": xgs360026fACLACEFrameType,
       "xgs360026fACLACEAction": xgs360026fACLACEAction,
       "xgs360026fACLACEDenyPortRedirect": xgs360026fACLACEDenyPortRedirect,
       "xgs360026fACLACELogging": xgs360026fACLACELogging,
       "xgs360026fACLACERateLimiter": xgs360026fACLACERateLimiter,
       "xgs360026fACLACEShutdown": xgs360026fACLACEShutdown,
       "xgs360026fACLACEVLANTagPriority": xgs360026fACLACEVLANTagPriority,
       "xgs360026fACLACEVLANVID": xgs360026fACLACEVLANVID,
       "xgs360026fACLACEEtherType": xgs360026fACLACEEtherType,
       "xgs360026fACLACESMAC": xgs360026fACLACESMAC,
       "xgs360026fACLACEDMACType": xgs360026fACLACEDMACType,
       "xgs360026fACLACEDMAC": xgs360026fACLACEDMAC,
       "xgs360026fACLACEArpOpcode": xgs360026fACLACEArpOpcode,
       "xgs360026fACLACEArpFlagsRequestReply": xgs360026fACLACEArpFlagsRequestReply,
       "xgs360026fACLACEArpFlagsArpSmac": xgs360026fACLACEArpFlagsArpSmac,
       "xgs360026fACLACEArpFlagsRarpDmac": xgs360026fACLACEArpFlagsRarpDmac,
       "xgs360026fACLACEArpFlagsLength": xgs360026fACLACEArpFlagsLength,
       "xgs360026fACLACEArpFlagsIp": xgs360026fACLACEArpFlagsIp,
       "xgs360026fACLACEArpFlagsEthernet": xgs360026fACLACEArpFlagsEthernet,
       "xgs360026fACLACESIPType": xgs360026fACLACESIPType,
       "xgs360026fACLACESIPIPAddress": xgs360026fACLACESIPIPAddress,
       "xgs360026fACLACESIPNetworkPrefix": xgs360026fACLACESIPNetworkPrefix,
       "xgs360026fACLACEDIPType": xgs360026fACLACEDIPType,
       "xgs360026fACLACEDIPIPAddress": xgs360026fACLACEDIPIPAddress,
       "xgs360026fACLACEDIPNetworkPrefix": xgs360026fACLACEDIPNetworkPrefix,
       "xgs360026fACLACEIPProtocol": xgs360026fACLACEIPProtocol,
       "xgs360026fACLACEIPFlagsTTL": xgs360026fACLACEIPFlagsTTL,
       "xgs360026fACLACEIPFlagsOptions": xgs360026fACLACEIPFlagsOptions,
       "xgs360026fACLACEIPFlagsFragment": xgs360026fACLACEIPFlagsFragment,
       "xgs360026fACLACEICMPType": xgs360026fACLACEICMPType,
       "xgs360026fACLACEICMPCode": xgs360026fACLACEICMPCode,
       "xgs360026fACLACESourcePortMin": xgs360026fACLACESourcePortMin,
       "xgs360026fACLACESourcePortMax": xgs360026fACLACESourcePortMax,
       "xgs360026fACLACEDestPortMin": xgs360026fACLACEDestPortMin,
       "xgs360026fACLACEDestPortMax": xgs360026fACLACEDestPortMax,
       "xgs360026fACLACETCPFlagsFin": xgs360026fACLACETCPFlagsFin,
       "xgs360026fACLACETCPFlagsSyn": xgs360026fACLACETCPFlagsSyn,
       "xgs360026fACLACETCPFlagsRst": xgs360026fACLACETCPFlagsRst,
       "xgs360026fACLACETCPFlagsPsh": xgs360026fACLACETCPFlagsPsh,
       "xgs360026fACLACETCPFlagsAck": xgs360026fACLACETCPFlagsAck,
       "xgs360026fACLACETCPFlagsUrg": xgs360026fACLACETCPFlagsUrg,
       "xgs360026fACLACERowStatus": xgs360026fACLACERowStatus,
       "xgs360026fACLACEClear": xgs360026fACLACEClear,
       "xgs360026fACLACEMoveACEID": xgs360026fACLACEMoveACEID,
       "xgs360026fACLACEMoveNextACEID": xgs360026fACLACEMoveNextACEID,
       "xgs360026fACLACEStatusTable": xgs360026fACLACEStatusTable,
       "xgs360026fACLACEStatusEntry": xgs360026fACLACEStatusEntry,
       "xgs360026fACLACEStatusIndex": xgs360026fACLACEStatusIndex,
       "xgs360026fACLACEStatusUser": xgs360026fACLACEStatusUser,
       "xgs360026fACLACEStatusID": xgs360026fACLACEStatusID,
       "xgs360026fACLACEStatusIngressPort": xgs360026fACLACEStatusIngressPort,
       "xgs360026fACLACEStatusFrameType": xgs360026fACLACEStatusFrameType,
       "xgs360026fACLACEStatusAction": xgs360026fACLACEStatusAction,
       "xgs360026fACLACEStatusRateLimiter": xgs360026fACLACEStatusRateLimiter,
       "xgs360026fACLACEStatusPortCopy": xgs360026fACLACEStatusPortCopy,
       "xgs360026fACLACEStatusMirror": xgs360026fACLACEStatusMirror,
       "xgs360026fACLACEStatusCPU": xgs360026fACLACEStatusCPU,
       "xgs360026fACLACEStatusCounter": xgs360026fACLACEStatusCounter,
       "xgs360026fACLACEStatusConflict": xgs360026fACLACEStatusConflict,
       "xgs360026fERPS": xgs360026fERPS,
       "xgs360026fERPSConf": xgs360026fERPSConf,
       "xgs360026fERPSConfCreate": xgs360026fERPSConfCreate,
       "xgs360026fERPSConfTable": xgs360026fERPSConfTable,
       "xgs360026fERPSConfEntry": xgs360026fERPSConfEntry,
       "xgs360026fERPSConfIndex": xgs360026fERPSConfIndex,
       "xgs360026fERPSConfERPSID": xgs360026fERPSConfERPSID,
       "xgs360026fERPSConfPort0": xgs360026fERPSConfPort0,
       "xgs360026fERPSConfPort1": xgs360026fERPSConfPort1,
       "xgs360026fERPSConfPort0SFMEP": xgs360026fERPSConfPort0SFMEP,
       "xgs360026fERPSConfPort1SFMEP": xgs360026fERPSConfPort1SFMEP,
       "xgs360026fERPSConfPort0APSMEP": xgs360026fERPSConfPort0APSMEP,
       "xgs360026fERPSConfPort1APSMEP": xgs360026fERPSConfPort1APSMEP,
       "xgs360026fERPSConfRingType": xgs360026fERPSConfRingType,
       "xgs360026fERPSConfInterconnectedNode": xgs360026fERPSConfInterconnectedNode,
       "xgs360026fERPSConfVirtualChannel": xgs360026fERPSConfVirtualChannel,
       "xgs360026fERPSConfMajorRingID": xgs360026fERPSConfMajorRingID,
       "xgs360026fERPSConfAlarm": xgs360026fERPSConfAlarm,
       "xgs360026fERPSInstanceConfConfigured": xgs360026fERPSInstanceConfConfigured,
       "xgs360026fERPSInstanceConfGuardTime": xgs360026fERPSInstanceConfGuardTime,
       "xgs360026fERPSInstanceConfWTRTime": xgs360026fERPSInstanceConfWTRTime,
       "xgs360026fERPSInstanceConfHoldOffTime": xgs360026fERPSInstanceConfHoldOffTime,
       "xgs360026fERPSInstanceConfVersion": xgs360026fERPSInstanceConfVersion,
       "xgs360026fERPSInstanceConfRevertive": xgs360026fERPSInstanceConfRevertive,
       "xgs360026fERPSInstanceConfVLANconfig": xgs360026fERPSInstanceConfVLANconfig,
       "xgs360026fERPSConfRowStatus": xgs360026fERPSConfRowStatus,
       "xgs360026fMRSTP": xgs360026fMRSTP,
       "xgs360026fMRSTPInstance": xgs360026fMRSTPInstance,
       "xgs360026fMRSTPInstanceConf": xgs360026fMRSTPInstanceConf,
       "xgs360026fMRSTPInstanceConfGlobalState": xgs360026fMRSTPInstanceConfGlobalState,
       "xgs360026fMRSTPInstanceConfigurationTable": xgs360026fMRSTPInstanceConfigurationTable,
       "xgs360026fMRSTPInstanceConfigurationEntry": xgs360026fMRSTPInstanceConfigurationEntry,
       "xgs360026fMRSTPInstanceConfigurationInstance": xgs360026fMRSTPInstanceConfigurationInstance,
       "xgs360026fMRSTPInstanceConfigurationState": xgs360026fMRSTPInstanceConfigurationState,
       "xgs360026fMRSTPInstanceConfigurationVersion": xgs360026fMRSTPInstanceConfigurationVersion,
       "xgs360026fMRSTPInstanceConfigurationPriority": xgs360026fMRSTPInstanceConfigurationPriority,
       "xgs360026fMRSTPInstanceConfigurationHelloTime": xgs360026fMRSTPInstanceConfigurationHelloTime,
       "xgs360026fMRSTPInstanceConfigurationMaxAge": xgs360026fMRSTPInstanceConfigurationMaxAge,
       "xgs360026fMRSTPInstanceConfigurationFWDelay": xgs360026fMRSTPInstanceConfigurationFWDelay,
       "xgs360026fMRSTPInstanceStatus": xgs360026fMRSTPInstanceStatus,
       "xgs360026fMRSTPInstanceStatusTable": xgs360026fMRSTPInstanceStatusTable,
       "xgs360026fMRSTPInstanceStatusEntry": xgs360026fMRSTPInstanceStatusEntry,
       "xgs360026fMRSTPInstanceStatusInstance": xgs360026fMRSTPInstanceStatusInstance,
       "xgs360026fMRSTPInstanceStatusGlobalState": xgs360026fMRSTPInstanceStatusGlobalState,
       "xgs360026fMRSTPInstanceStatusInstanceConfigState": xgs360026fMRSTPInstanceStatusInstanceConfigState,
       "xgs360026fMRSTPInstanceStatusInstanceCurrentState": xgs360026fMRSTPInstanceStatusInstanceCurrentState,
       "xgs360026fMRSTPInstanceStatusBridgeID": xgs360026fMRSTPInstanceStatusBridgeID,
       "xgs360026fMRSTPInstanceStatusBridgePrioriry": xgs360026fMRSTPInstanceStatusBridgePrioriry,
       "xgs360026fMRSTPInstanceStatusRootID": xgs360026fMRSTPInstanceStatusRootID,
       "xgs360026fMRSTPInstanceStatusRootPriority": xgs360026fMRSTPInstanceStatusRootPriority,
       "xgs360026fMRSTPInstanceStatusRootPort": xgs360026fMRSTPInstanceStatusRootPort,
       "xgs360026fMRSTPInstanceStatusRootPathCost": xgs360026fMRSTPInstanceStatusRootPathCost,
       "xgs360026fMRSTPInstanceStatusCurrentMaxAge": xgs360026fMRSTPInstanceStatusCurrentMaxAge,
       "xgs360026fMRSTPInstanceStatusCurrentForwardDelay": xgs360026fMRSTPInstanceStatusCurrentForwardDelay,
       "xgs360026fMRSTPInstanceStatusHelloTime": xgs360026fMRSTPInstanceStatusHelloTime,
       "xgs360026fMRSTPInstanceStatusTopologyChangeCount": xgs360026fMRSTPInstanceStatusTopologyChangeCount,
       "xgs360026fMRSTPInstanceStatusTimeSinceLastTopologyChange": xgs360026fMRSTPInstanceStatusTimeSinceLastTopologyChange,
       "xgs360026fMRSTPPort": xgs360026fMRSTPPort,
       "xgs360026fMRSTPPortConfiguration": xgs360026fMRSTPPortConfiguration,
       "xgs360026fMRSTPPortConfigurationTable": xgs360026fMRSTPPortConfigurationTable,
       "xgs360026fMRSTPPortConfigurationEntry": xgs360026fMRSTPPortConfigurationEntry,
       "xgs360026fMRSTPPortConfigurationPort": xgs360026fMRSTPPortConfigurationPort,
       "xgs360026fMRSTPPortConfigurationInstance": xgs360026fMRSTPPortConfigurationInstance,
       "xgs360026fMRSTPPortConfigurationPathCost": xgs360026fMRSTPPortConfigurationPathCost,
       "xgs360026fMRSTPPortConfigurationPriority": xgs360026fMRSTPPortConfigurationPriority,
       "xgs360026fMRSTPPortConfigurationAdminEdge": xgs360026fMRSTPPortConfigurationAdminEdge,
       "xgs360026fMRSTPPortConfigurationAdminP2P": xgs360026fMRSTPPortConfigurationAdminP2P,
       "xgs360026fMRSTPPortConfigurationMigrateCheck": xgs360026fMRSTPPortConfigurationMigrateCheck,
       "xgs360026fMRSTPPortStatus": xgs360026fMRSTPPortStatus,
       "xgs360026fMRSTPPortStatusTable": xgs360026fMRSTPPortStatusTable,
       "xgs360026fMRSTPPortStatusEntry": xgs360026fMRSTPPortStatusEntry,
       "xgs360026fMRSTPPortStatusPort": xgs360026fMRSTPPortStatusPort,
       "xgs360026fMRSTPPortStatusInstance": xgs360026fMRSTPPortStatusInstance,
       "xgs360026fMRSTPPortStatusState": xgs360026fMRSTPPortStatusState,
       "xgs360026fMRSTPPortStatusRole": xgs360026fMRSTPPortStatusRole,
       "xgs360026fMRSTPPortStatusPathCost": xgs360026fMRSTPPortStatusPathCost,
       "xgs360026fMRSTPPortStatusPathCostConfig": xgs360026fMRSTPPortStatusPathCostConfig,
       "xgs360026fMRSTPPortStatusPriority": xgs360026fMRSTPPortStatusPriority,
       "xgs360026fMRSTPPortStatusAdminEdge": xgs360026fMRSTPPortStatusAdminEdge,
       "xgs360026fMRSTPPortStatusAdminP2P": xgs360026fMRSTPPortStatusAdminP2P,
       "xgs360026fSecurity": xgs360026fSecurity,
       "xgs360026fIPSourceGuard": xgs360026fIPSourceGuard,
       "xgs360026fIPSourceGuardConf": xgs360026fIPSourceGuardConf,
       "xgs360026fIPSourceGuardMode": xgs360026fIPSourceGuardMode,
       "xgs360026fIPSourceGuardPortConfigTable": xgs360026fIPSourceGuardPortConfigTable,
       "xgs360026fIPSourceGuardPortConfigEntry": xgs360026fIPSourceGuardPortConfigEntry,
       "xgs360026fIPSourceGuardPortConfigPort": xgs360026fIPSourceGuardPortConfigPort,
       "xgs360026fIPSourceGuardPortConfigMode": xgs360026fIPSourceGuardPortConfigMode,
       "xgs360026fIPSourceGuardPortMaxDynamicClients": xgs360026fIPSourceGuardPortMaxDynamicClients,
       "xgs360026fIPSourceGuardStatic": xgs360026fIPSourceGuardStatic,
       "xgs360026fIPSourceGuardStaticCreate": xgs360026fIPSourceGuardStaticCreate,
       "xgs360026fIPSourceGuardStaticTable": xgs360026fIPSourceGuardStaticTable,
       "xgs360026fIPSourceGuardStaticEntry": xgs360026fIPSourceGuardStaticEntry,
       "xgs360026fIPSourceGuardStaticIndex": xgs360026fIPSourceGuardStaticIndex,
       "xgs360026fIPSourceGuardStaticPort": xgs360026fIPSourceGuardStaticPort,
       "xgs360026fIPSourceGuardStaticVLANId": xgs360026fIPSourceGuardStaticVLANId,
       "xgs360026fIPSourceGuardStaticIPAddress": xgs360026fIPSourceGuardStaticIPAddress,
       "xgs360026fIPSourceGuardStaticMACAddress": xgs360026fIPSourceGuardStaticMACAddress,
       "xgs360026fIPSourceGuardStaticRowStatus": xgs360026fIPSourceGuardStaticRowStatus,
       "xgs360026fIPSourceGuardDynamicTable": xgs360026fIPSourceGuardDynamicTable,
       "xgs360026fIPSourceGuardDynamicEntry": xgs360026fIPSourceGuardDynamicEntry,
       "xgs360026fIPSourceGuardDynamicIndex": xgs360026fIPSourceGuardDynamicIndex,
       "xgs360026fIPSourceGuardDynamicPort": xgs360026fIPSourceGuardDynamicPort,
       "xgs360026fIPSourceGuardDynamicVLANId": xgs360026fIPSourceGuardDynamicVLANId,
       "xgs360026fIPSourceGuardDynamicIPAddress": xgs360026fIPSourceGuardDynamicIPAddress,
       "xgs360026fIPSourceGuardDynamicMACAddress": xgs360026fIPSourceGuardDynamicMACAddress,
       "xgs360026fARPInspection": xgs360026fARPInspection,
       "xgs360026fARPInspectionConf": xgs360026fARPInspectionConf,
       "xgs360026fARPInspectionConfMode": xgs360026fARPInspectionConfMode,
       "xgs360026fARPInspectionConfTable": xgs360026fARPInspectionConfTable,
       "xgs360026fARPInspectionConfEntry": xgs360026fARPInspectionConfEntry,
       "xgs360026fARPInspectionConfPortIndex": xgs360026fARPInspectionConfPortIndex,
       "xgs360026fARPInspectionConfPortMode": xgs360026fARPInspectionConfPortMode,
       "xgs360026fARPInspectionStatic": xgs360026fARPInspectionStatic,
       "xgs360026fARPInspectionStaticCreate": xgs360026fARPInspectionStaticCreate,
       "xgs360026fARPInspectionStaticTable": xgs360026fARPInspectionStaticTable,
       "xgs360026fARPInspectionStaticEntry": xgs360026fARPInspectionStaticEntry,
       "xgs360026fARPInspectionStaticIndex": xgs360026fARPInspectionStaticIndex,
       "xgs360026fARPInspectionStaticPort": xgs360026fARPInspectionStaticPort,
       "xgs360026fARPInspectionStaticVLANId": xgs360026fARPInspectionStaticVLANId,
       "xgs360026fARPInspectionStaticIPAddress": xgs360026fARPInspectionStaticIPAddress,
       "xgs360026fARPInspectionStaticMACAddress": xgs360026fARPInspectionStaticMACAddress,
       "xgs360026fARPInspectionStaticRowStatus": xgs360026fARPInspectionStaticRowStatus,
       "xgs360026fARPInspectionDynamicTable": xgs360026fARPInspectionDynamicTable,
       "xgs360026fARPInspectionDynamicEntry": xgs360026fARPInspectionDynamicEntry,
       "xgs360026fARPInspectionDynamicIndex": xgs360026fARPInspectionDynamicIndex,
       "xgs360026fARPInspectionDynamicPort": xgs360026fARPInspectionDynamicPort,
       "xgs360026fARPInspectionDynamicVLANId": xgs360026fARPInspectionDynamicVLANId,
       "xgs360026fARPInspectionDynamicIPAddress": xgs360026fARPInspectionDynamicIPAddress,
       "xgs360026fARPInspectionDynamicMACAddress": xgs360026fARPInspectionDynamicMACAddress,
       "xgs360026fDHCPSnooping": xgs360026fDHCPSnooping,
       "xgs360026fDHCPSnoopingConf": xgs360026fDHCPSnoopingConf,
       "xgs360026fDHCPSnoopingMode": xgs360026fDHCPSnoopingMode,
       "xgs360026fDHCPSnoopingPortModeConfigurationTable": xgs360026fDHCPSnoopingPortModeConfigurationTable,
       "xgs360026fDHCPSnoopingPortModeConfigurationEntry": xgs360026fDHCPSnoopingPortModeConfigurationEntry,
       "xgs360026fDHCPSnoopingPortModeConfigurationPort": xgs360026fDHCPSnoopingPortModeConfigurationPort,
       "xgs360026fDHCPSnoopingPortModeConfigurationMode": xgs360026fDHCPSnoopingPortModeConfigurationMode,
       "xgs360026fDHCPSnoopingStatisticsTable": xgs360026fDHCPSnoopingStatisticsTable,
       "xgs360026fDHCPSnoopingStatisticsEntry": xgs360026fDHCPSnoopingStatisticsEntry,
       "xgs360026fDHCPSnoopingStatisticsPort": xgs360026fDHCPSnoopingStatisticsPort,
       "xgs360026fDHCPSnoopingStatisticsClear": xgs360026fDHCPSnoopingStatisticsClear,
       "xgs360026fDHCPSnoopingRxDiscover": xgs360026fDHCPSnoopingRxDiscover,
       "xgs360026fDHCPSnoopingRxOffer": xgs360026fDHCPSnoopingRxOffer,
       "xgs360026fDHCPSnoopingRxRequest": xgs360026fDHCPSnoopingRxRequest,
       "xgs360026fDHCPSnoopingRxDecline": xgs360026fDHCPSnoopingRxDecline,
       "xgs360026fDHCPSnoopingRxACK": xgs360026fDHCPSnoopingRxACK,
       "xgs360026fDHCPSnoopingRxNAK": xgs360026fDHCPSnoopingRxNAK,
       "xgs360026fDHCPSnoopingRxRelease": xgs360026fDHCPSnoopingRxRelease,
       "xgs360026fDHCPSnoopingRxInform": xgs360026fDHCPSnoopingRxInform,
       "xgs360026fDHCPSnoopingRxLeaseQuery": xgs360026fDHCPSnoopingRxLeaseQuery,
       "xgs360026fDHCPSnoopingRxLeaseUnassigned": xgs360026fDHCPSnoopingRxLeaseUnassigned,
       "xgs360026fDHCPSnoopingRxLeaseUnknown": xgs360026fDHCPSnoopingRxLeaseUnknown,
       "xgs360026fDHCPSnoopingRxLeaseActive": xgs360026fDHCPSnoopingRxLeaseActive,
       "xgs360026fDHCPSnoopingTxDiscover": xgs360026fDHCPSnoopingTxDiscover,
       "xgs360026fDHCPSnoopingTxOffer": xgs360026fDHCPSnoopingTxOffer,
       "xgs360026fDHCPSnoopingTxRequest": xgs360026fDHCPSnoopingTxRequest,
       "xgs360026fDHCPSnoopingTxDecline": xgs360026fDHCPSnoopingTxDecline,
       "xgs360026fDHCPSnoopingTxACK": xgs360026fDHCPSnoopingTxACK,
       "xgs360026fDHCPSnoopingTxNAK": xgs360026fDHCPSnoopingTxNAK,
       "xgs360026fDHCPSnoopingTxRelease": xgs360026fDHCPSnoopingTxRelease,
       "xgs360026fDHCPSnoopingTxInform": xgs360026fDHCPSnoopingTxInform,
       "xgs360026fDHCPSnoopingTxLeaseQuery": xgs360026fDHCPSnoopingTxLeaseQuery,
       "xgs360026fDHCPSnoopingTxLeaseUnassigned": xgs360026fDHCPSnoopingTxLeaseUnassigned,
       "xgs360026fDHCPSnoopingTxLeaseUnknown": xgs360026fDHCPSnoopingTxLeaseUnknown,
       "xgs360026fDHCPSnoopingTxLeaseActive": xgs360026fDHCPSnoopingTxLeaseActive,
       "xgs360026fDHCPRelay": xgs360026fDHCPRelay,
       "xgs360026fDHCPRelayConfiguration": xgs360026fDHCPRelayConfiguration,
       "xgs360026fDHCPRelayMode": xgs360026fDHCPRelayMode,
       "xgs360026fDHCPRelayServer": xgs360026fDHCPRelayServer,
       "xgs360026fDHCPRelayInformationMode": xgs360026fDHCPRelayInformationMode,
       "xgs360026fDHCPRelayInformationPolicy": xgs360026fDHCPRelayInformationPolicy,
       "xgs360026fDHCPRelayStatistics": xgs360026fDHCPRelayStatistics,
       "xgs360026fDHCPRelayServerStatistics": xgs360026fDHCPRelayServerStatistics,
       "xgs360026fServerStatTransmitToServer": xgs360026fServerStatTransmitToServer,
       "xgs360026fServerStatTransmitError": xgs360026fServerStatTransmitError,
       "xgs360026fServerStatReceiveFromServer": xgs360026fServerStatReceiveFromServer,
       "xgs360026fServerStatReceiveMissingAgentOption": xgs360026fServerStatReceiveMissingAgentOption,
       "xgs360026fServerStatReceiveMissingCircuitID": xgs360026fServerStatReceiveMissingCircuitID,
       "xgs360026fServerStatReceiveMissingRemoteID": xgs360026fServerStatReceiveMissingRemoteID,
       "xgs360026fServerStatReceiveBadCircuitID": xgs360026fServerStatReceiveBadCircuitID,
       "xgs360026fServerStatReceiveBadRemoteID": xgs360026fServerStatReceiveBadRemoteID,
       "xgs360026fDHCPRelayClientStatistics": xgs360026fDHCPRelayClientStatistics,
       "xgs360026fClientStatTransmitToClient": xgs360026fClientStatTransmitToClient,
       "xgs360026fClientStatTransmitError": xgs360026fClientStatTransmitError,
       "xgs360026fClientStatReceivefromClient": xgs360026fClientStatReceivefromClient,
       "xgs360026fClientStatReceiveAgentOption": xgs360026fClientStatReceiveAgentOption,
       "xgs360026fClientStatReplaceAgentOption": xgs360026fClientStatReplaceAgentOption,
       "xgs360026fClientStatKeepAgentOption": xgs360026fClientStatKeepAgentOption,
       "xgs360026fClientStatDropAgentOption": xgs360026fClientStatDropAgentOption,
       "xgs360026fPortSecurity": xgs360026fPortSecurity,
       "xgs360026fPortSecLimitCtrl": xgs360026fPortSecLimitCtrl,
       "xgs360026fPortSecLimitCtrlSystemConf": xgs360026fPortSecLimitCtrlSystemConf,
       "xgs360026fPortSecurityMode": xgs360026fPortSecurityMode,
       "xgs360026fPortSecurityAging": xgs360026fPortSecurityAging,
       "xgs360026fPortSecurityAgingPeriod": xgs360026fPortSecurityAgingPeriod,
       "xgs360026fPortSecLimitCtrlTable": xgs360026fPortSecLimitCtrlTable,
       "xgs360026fPortSecLimitCtrlEntry": xgs360026fPortSecLimitCtrlEntry,
       "xgs360026fPortSecLimitCtrlPort": xgs360026fPortSecLimitCtrlPort,
       "xgs360026fPortSecLimitCtrlPortMode": xgs360026fPortSecLimitCtrlPortMode,
       "xgs360026fPortSecLimitCtrlPortLimit": xgs360026fPortSecLimitCtrlPortLimit,
       "xgs360026fPortSecLimitCtrlPortAction": xgs360026fPortSecLimitCtrlPortAction,
       "xgs360026fPortSecLimitCtrlPortState": xgs360026fPortSecLimitCtrlPortState,
       "xgs360026fPortSecLimitCtrlPortReOpen": xgs360026fPortSecLimitCtrlPortReOpen,
       "xgs360026fPortSecSwitchStatusTable": xgs360026fPortSecSwitchStatusTable,
       "xgs360026fPortSecSwitchStatusEntry": xgs360026fPortSecSwitchStatusEntry,
       "xgs360026fPortSecSwitchStatusPort": xgs360026fPortSecSwitchStatusPort,
       "xgs360026fPortSecSwitchStatusUsers": xgs360026fPortSecSwitchStatusUsers,
       "xgs360026fPortSecSwitchStatusState": xgs360026fPortSecSwitchStatusState,
       "xgs360026fPortSecSwitchStatusMACCountCurrent": xgs360026fPortSecSwitchStatusMACCountCurrent,
       "xgs360026fPortSecSwitchStatusMACCountLimit": xgs360026fPortSecSwitchStatusMACCountLimit,
       "xgs360026fPortSecPortStatus": xgs360026fPortSecPortStatus,
       "xgs360026fPortSecPortStatusPort": xgs360026fPortSecPortStatusPort,
       "xgs360026fPortSecPortStatusTable": xgs360026fPortSecPortStatusTable,
       "xgs360026fPortSecPortStatusEntry": xgs360026fPortSecPortStatusEntry,
       "xgs360026fPortSecPortStatusIndex": xgs360026fPortSecPortStatusIndex,
       "xgs360026fPortSecPortStatusMACAddress": xgs360026fPortSecPortStatusMACAddress,
       "xgs360026fPortSecPortStatusVLANId": xgs360026fPortSecPortStatusVLANId,
       "xgs360026fPortSecPortStatusState": xgs360026fPortSecPortStatusState,
       "xgs360026fPortSecPortStatusTimeOfAddition": xgs360026fPortSecPortStatusTimeOfAddition,
       "xgs360026fPortSecPortStatusAgeAndHold": xgs360026fPortSecPortStatusAgeAndHold,
       "xgs360026fAccessManagement": xgs360026fAccessManagement,
       "xgs360026fAccessMgtConf": xgs360026fAccessMgtConf,
       "xgs360026fAccessMgtConfMode": xgs360026fAccessMgtConfMode,
       "xgs360026fAccessMgtConfCreate": xgs360026fAccessMgtConfCreate,
       "xgs360026fAccessMgtConfTable": xgs360026fAccessMgtConfTable,
       "xgs360026fAccessMgtConfEntry": xgs360026fAccessMgtConfEntry,
       "xgs360026fAccessMgtIndex": xgs360026fAccessMgtIndex,
       "xgs360026fAccessMgtAddresstype": xgs360026fAccessMgtAddresstype,
       "xgs360026fAccessMgtStartIpAddress": xgs360026fAccessMgtStartIpAddress,
       "xgs360026fAccessMgtEndIpAddress": xgs360026fAccessMgtEndIpAddress,
       "xgs360026fAccessMgtHttpHttps": xgs360026fAccessMgtHttpHttps,
       "xgs360026fAccessMgtSNMP": xgs360026fAccessMgtSNMP,
       "xgs360026fAccessMgtTelnetSSH": xgs360026fAccessMgtTelnetSSH,
       "xgs360026fAccessMgtRowStatus": xgs360026fAccessMgtRowStatus,
       "xgs360026fAccessMgtStatistics": xgs360026fAccessMgtStatistics,
       "xgs360026fHttpReceivedPkts": xgs360026fHttpReceivedPkts,
       "xgs360026fHttpAllowedPkts": xgs360026fHttpAllowedPkts,
       "xgs360026fHttpDiscardedPkts": xgs360026fHttpDiscardedPkts,
       "xgs360026fHttpsReceivedPkts": xgs360026fHttpsReceivedPkts,
       "xgs360026fHttpsAllowedPkts": xgs360026fHttpsAllowedPkts,
       "xgs360026fHttpsDiscardedPkts": xgs360026fHttpsDiscardedPkts,
       "xgs360026fSnmpReceivedPkts": xgs360026fSnmpReceivedPkts,
       "xgs360026fSnmpAllowedPkts": xgs360026fSnmpAllowedPkts,
       "xgs360026fSnmpDiscardedPkts": xgs360026fSnmpDiscardedPkts,
       "xgs360026fTelnetReceivedPkts": xgs360026fTelnetReceivedPkts,
       "xgs360026fTelnetAllowedPkts": xgs360026fTelnetAllowedPkts,
       "xgs360026fTelnetDiscardedPkts": xgs360026fTelnetDiscardedPkts,
       "xgs360026fSSHReceivedPkts": xgs360026fSSHReceivedPkts,
       "xgs360026fSSHAllowedPkts": xgs360026fSSHAllowedPkts,
       "xgs360026fSSHDiscardedPkts": xgs360026fSSHDiscardedPkts,
       "xgs360026fAccessMgtStatisticsClearAll": xgs360026fAccessMgtStatisticsClearAll,
       "xgs360026fSSH": xgs360026fSSH,
       "xgs360026fSSHMode": xgs360026fSSHMode,
       "xgs360026fHTTPS": xgs360026fHTTPS,
       "xgs360026fHTTPSMode": xgs360026fHTTPSMode,
       "xgs360026fHTTPSAutoRedirect": xgs360026fHTTPSAutoRedirect,
       "xgs360026fAuthMethod": xgs360026fAuthMethod,
       "xgs360026fConsoleAuthMethod": xgs360026fConsoleAuthMethod,
       "xgs360026fConsoleFallback": xgs360026fConsoleFallback,
       "xgs360026fTelnetAuthMethod": xgs360026fTelnetAuthMethod,
       "xgs360026fTelnetFallback": xgs360026fTelnetFallback,
       "xgs360026fSshAuthMethod": xgs360026fSshAuthMethod,
       "xgs360026fSshFallback": xgs360026fSshFallback,
       "xgs360026fWebAuthMethod": xgs360026fWebAuthMethod,
       "xgs360026fWebFallback": xgs360026fWebFallback,
       "xgs360026fMaintenance": xgs360026fMaintenance,
       "xgs360026fRestartDevice": xgs360026fRestartDevice,
       "xgs360026fFirmware": xgs360026fFirmware,
       "xgs360026fFirmwareIpAddress": xgs360026fFirmwareIpAddress,
       "xgs360026fFirmwareFileName": xgs360026fFirmwareFileName,
       "xgs360026fDoFirmwareUpgrade": xgs360026fDoFirmwareUpgrade,
       "xgs360026fSaveOrRestore": xgs360026fSaveOrRestore,
       "xgs360026fFactoryDefaults": xgs360026fFactoryDefaults,
       "xgs360026fSaveStart": xgs360026fSaveStart,
       "xgs360026fSaveUser": xgs360026fSaveUser,
       "xgs360026fRestoreUser": xgs360026fRestoreUser,
       "xgs360026fExportOrImport": xgs360026fExportOrImport,
       "xgs360026fExportIpAddress": xgs360026fExportIpAddress,
       "xgs360026fExportConfigName": xgs360026fExportConfigName,
       "xgs360026fDoExportConfig": xgs360026fDoExportConfig,
       "xgs360026fImportIpAddress": xgs360026fImportIpAddress,
       "xgs360026fImportConfigName": xgs360026fImportConfigName,
       "xgs360026fDoImportConfig": xgs360026fDoImportConfig,
       "xgs360026fDiagnostics": xgs360026fDiagnostics,
       "xgs360026fPingIpAddress": xgs360026fPingIpAddress,
       "xgs360026fPingSize": xgs360026fPingSize,
       "xgs360026fDoPingConfig": xgs360026fDoPingConfig,
       "xgs360026fPingResult": xgs360026fPingResult,
       "xgs360026fPing6IpAddress": xgs360026fPing6IpAddress,
       "xgs360026fPing6Size": xgs360026fPing6Size,
       "xgs360026fDoPing6Config": xgs360026fDoPing6Config,
       "xgs360026fPing6Result": xgs360026fPing6Result,
       "xgs360026fVeriPHY": xgs360026fVeriPHY,
       "xgs360026fVeriPHYTest": xgs360026fVeriPHYTest,
       "xgs360026fVeriPHYTable": xgs360026fVeriPHYTable,
       "xgs360026fVeriPHYEntry": xgs360026fVeriPHYEntry,
       "xgs360026fVeriPHYPort": xgs360026fVeriPHYPort,
       "xgs360026fVeriPHYPairA": xgs360026fVeriPHYPairA,
       "xgs360026fVeriPHYLengthA": xgs360026fVeriPHYLengthA,
       "xgs360026fVeriPHYPairB": xgs360026fVeriPHYPairB,
       "xgs360026fVeriPHYLengthB": xgs360026fVeriPHYLengthB,
       "xgs360026fVeriPHYPairC": xgs360026fVeriPHYPairC,
       "xgs360026fVeriPHYLengthC": xgs360026fVeriPHYLengthC,
       "xgs360026fVeriPHYPairD": xgs360026fVeriPHYPairD,
       "xgs360026fVeriPHYLengthD": xgs360026fVeriPHYLengthD,
       "xgs360026fTrap": xgs360026fTrap,
       "xgs360026fTrapEvent": xgs360026fTrapEvent,
       "xgs360026fEmergency": xgs360026fEmergency,
       "xgs360026fAlert": xgs360026fAlert,
       "xgs360026fCritical": xgs360026fCritical,
       "xgs360026fError": xgs360026fError,
       "xgs360026fWarning": xgs360026fWarning,
       "xgs360026fNotice": xgs360026fNotice,
       "xgs360026fInformational": xgs360026fInformational,
       "xgs360026fDebug": xgs360026fDebug,
       "xgs360026fTrapVariable": xgs360026fTrapVariable,
       "xgs360026fInformation": xgs360026fInformation}
)
