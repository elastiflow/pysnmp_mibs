# SNMP MIB module (PRIVATETECH-LGS2624C-FUNCTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/lantech_37072/PRIVATETECH-LGS2624C-FUNCTION-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:14:09 2025
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

privatetech = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37072)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2)
)
_Lgs2624cProductId_ObjectIdentity = ObjectIdentity
lgs2624cProductId = _Lgs2624cProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54)
)
_Lgs2624cSystem_ObjectIdentity = ObjectIdentity
lgs2624cSystem = _Lgs2624cSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1)
)
_Lgs2624cSystemInformation_ObjectIdentity = ObjectIdentity
lgs2624cSystemInformation = _Lgs2624cSystemInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 1)
)
_Lgs2624cModelName_Type = DisplayString
_Lgs2624cModelName_Object = MibScalar
lgs2624cModelName = _Lgs2624cModelName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 1, 1),
    _Lgs2624cModelName_Type()
)
lgs2624cModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cModelName.setStatus("current")
_Lgs2624cBIOSVersion_Type = DisplayString
_Lgs2624cBIOSVersion_Object = MibScalar
lgs2624cBIOSVersion = _Lgs2624cBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 1, 2),
    _Lgs2624cBIOSVersion_Type()
)
lgs2624cBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cBIOSVersion.setStatus("current")
_Lgs2624cFirmwareVersion_Type = DisplayString
_Lgs2624cFirmwareVersion_Object = MibScalar
lgs2624cFirmwareVersion = _Lgs2624cFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 1, 3),
    _Lgs2624cFirmwareVersion_Type()
)
lgs2624cFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cFirmwareVersion.setStatus("current")
_Lgs2624cHardwareMechanicalVersion_Type = DisplayString
_Lgs2624cHardwareMechanicalVersion_Object = MibScalar
lgs2624cHardwareMechanicalVersion = _Lgs2624cHardwareMechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 1, 4),
    _Lgs2624cHardwareMechanicalVersion_Type()
)
lgs2624cHardwareMechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cHardwareMechanicalVersion.setStatus("current")
_Lgs2624cSeriesNumber_Type = DisplayString
_Lgs2624cSeriesNumber_Object = MibScalar
lgs2624cSeriesNumber = _Lgs2624cSeriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 1, 5),
    _Lgs2624cSeriesNumber_Type()
)
lgs2624cSeriesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSeriesNumber.setStatus("current")
_Lgs2624cHostMACAddress_Type = MacAddress
_Lgs2624cHostMACAddress_Object = MibScalar
lgs2624cHostMACAddress = _Lgs2624cHostMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 1, 6),
    _Lgs2624cHostMACAddress_Type()
)
lgs2624cHostMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cHostMACAddress.setStatus("current")
_Lgs2624cConsoleBaudrate_Type = DisplayString
_Lgs2624cConsoleBaudrate_Object = MibScalar
lgs2624cConsoleBaudrate = _Lgs2624cConsoleBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 1, 7),
    _Lgs2624cConsoleBaudrate_Type()
)
lgs2624cConsoleBaudrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cConsoleBaudrate.setStatus("current")
_Lgs2624cRAMSize_Type = DisplayString
_Lgs2624cRAMSize_Object = MibScalar
lgs2624cRAMSize = _Lgs2624cRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 1, 8),
    _Lgs2624cRAMSize_Type()
)
lgs2624cRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cRAMSize.setStatus("current")
_Lgs2624cFlashSize_Type = DisplayString
_Lgs2624cFlashSize_Object = MibScalar
lgs2624cFlashSize = _Lgs2624cFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 1, 9),
    _Lgs2624cFlashSize_Type()
)
lgs2624cFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cFlashSize.setStatus("current")
_Lgs2624cBridgeFBDSize_Type = DisplayString
_Lgs2624cBridgeFBDSize_Object = MibScalar
lgs2624cBridgeFBDSize = _Lgs2624cBridgeFBDSize_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 1, 10),
    _Lgs2624cBridgeFBDSize_Type()
)
lgs2624cBridgeFBDSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cBridgeFBDSize.setStatus("current")
_Lgs2624cTransmitQueue_Type = DisplayString
_Lgs2624cTransmitQueue_Object = MibScalar
lgs2624cTransmitQueue = _Lgs2624cTransmitQueue_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 1, 11),
    _Lgs2624cTransmitQueue_Type()
)
lgs2624cTransmitQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cTransmitQueue.setStatus("current")
_Lgs2624cMaximumFrameSize_Type = DisplayString
_Lgs2624cMaximumFrameSize_Object = MibScalar
lgs2624cMaximumFrameSize = _Lgs2624cMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 1, 12),
    _Lgs2624cMaximumFrameSize_Type()
)
lgs2624cMaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cMaximumFrameSize.setStatus("current")
_Lgs2624cCPULoad_Type = DisplayString
_Lgs2624cCPULoad_Object = MibScalar
lgs2624cCPULoad = _Lgs2624cCPULoad_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 1, 13),
    _Lgs2624cCPULoad_Type()
)
lgs2624cCPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cCPULoad.setStatus("current")
_Lgs2624cSystemTime_ObjectIdentity = ObjectIdentity
lgs2624cSystemTime = _Lgs2624cSystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2)
)
_Lgs2624cSystemTimeManual_ObjectIdentity = ObjectIdentity
lgs2624cSystemTimeManual = _Lgs2624cSystemTimeManual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 1)
)


class _Lgs2624cSystemTimeManualClockSource_Type(Integer32):
    """Custom type lgs2624cSystemTimeManualClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cSystemTimeManualClockSource_Type.__name__ = "Integer32"
_Lgs2624cSystemTimeManualClockSource_Object = MibScalar
lgs2624cSystemTimeManualClockSource = _Lgs2624cSystemTimeManualClockSource_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 1, 1),
    _Lgs2624cSystemTimeManualClockSource_Type()
)
lgs2624cSystemTimeManualClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeManualClockSource.setStatus("current")
_Lgs2624cSystemTimeManualLocaltime_Type = DisplayString
_Lgs2624cSystemTimeManualLocaltime_Object = MibScalar
lgs2624cSystemTimeManualLocaltime = _Lgs2624cSystemTimeManualLocaltime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 1, 2),
    _Lgs2624cSystemTimeManualLocaltime_Type()
)
lgs2624cSystemTimeManualLocaltime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeManualLocaltime.setStatus("current")


class _Lgs2624cSystemTimeManualTimeZoneOffset_Type(Integer32):
    """Custom type lgs2624cSystemTimeManualTimeZoneOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 780),
    )


_Lgs2624cSystemTimeManualTimeZoneOffset_Type.__name__ = "Integer32"
_Lgs2624cSystemTimeManualTimeZoneOffset_Object = MibScalar
lgs2624cSystemTimeManualTimeZoneOffset = _Lgs2624cSystemTimeManualTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 1, 3),
    _Lgs2624cSystemTimeManualTimeZoneOffset_Type()
)
lgs2624cSystemTimeManualTimeZoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeManualTimeZoneOffset.setStatus("current")


class _Lgs2624cSystemTimeManualDaylightSavings_Type(Integer32):
    """Custom type lgs2624cSystemTimeManualDaylightSavings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cSystemTimeManualDaylightSavings_Type.__name__ = "Integer32"
_Lgs2624cSystemTimeManualDaylightSavings_Object = MibScalar
lgs2624cSystemTimeManualDaylightSavings = _Lgs2624cSystemTimeManualDaylightSavings_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 1, 4),
    _Lgs2624cSystemTimeManualDaylightSavings_Type()
)
lgs2624cSystemTimeManualDaylightSavings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeManualDaylightSavings.setStatus("current")


class _Lgs2624cSystemTimeManualTimeSetOffset_Type(Integer32):
    """Custom type lgs2624cSystemTimeManualTimeSetOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Lgs2624cSystemTimeManualTimeSetOffset_Type.__name__ = "Integer32"
_Lgs2624cSystemTimeManualTimeSetOffset_Object = MibScalar
lgs2624cSystemTimeManualTimeSetOffset = _Lgs2624cSystemTimeManualTimeSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 1, 5),
    _Lgs2624cSystemTimeManualTimeSetOffset_Type()
)
lgs2624cSystemTimeManualTimeSetOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeManualTimeSetOffset.setStatus("current")


class _Lgs2624cSystemTimeManualDaylightSavingsType_Type(Integer32):
    """Custom type lgs2624cSystemTimeManualDaylightSavingsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cSystemTimeManualDaylightSavingsType_Type.__name__ = "Integer32"
_Lgs2624cSystemTimeManualDaylightSavingsType_Object = MibScalar
lgs2624cSystemTimeManualDaylightSavingsType = _Lgs2624cSystemTimeManualDaylightSavingsType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 1, 6),
    _Lgs2624cSystemTimeManualDaylightSavingsType_Type()
)
lgs2624cSystemTimeManualDaylightSavingsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeManualDaylightSavingsType.setStatus("current")
_Lgs2624cSystemTimeManualDaylightSavingsBydatesFrom_Type = DisplayString
_Lgs2624cSystemTimeManualDaylightSavingsBydatesFrom_Object = MibScalar
lgs2624cSystemTimeManualDaylightSavingsBydatesFrom = _Lgs2624cSystemTimeManualDaylightSavingsBydatesFrom_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 1, 7),
    _Lgs2624cSystemTimeManualDaylightSavingsBydatesFrom_Type()
)
lgs2624cSystemTimeManualDaylightSavingsBydatesFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeManualDaylightSavingsBydatesFrom.setStatus("current")
_Lgs2624cSystemTimeManualDaylightSavingsBydatesTo_Type = DisplayString
_Lgs2624cSystemTimeManualDaylightSavingsBydatesTo_Object = MibScalar
lgs2624cSystemTimeManualDaylightSavingsBydatesTo = _Lgs2624cSystemTimeManualDaylightSavingsBydatesTo_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 1, 8),
    _Lgs2624cSystemTimeManualDaylightSavingsBydatesTo_Type()
)
lgs2624cSystemTimeManualDaylightSavingsBydatesTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeManualDaylightSavingsBydatesTo.setStatus("current")


class _Lgs2624cSystemTimeManualDaylightSavingsRecurringDayFrom_Type(Integer32):
    """Custom type lgs2624cSystemTimeManualDaylightSavingsRecurringDayFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Lgs2624cSystemTimeManualDaylightSavingsRecurringDayFrom_Type.__name__ = "Integer32"
_Lgs2624cSystemTimeManualDaylightSavingsRecurringDayFrom_Object = MibScalar
lgs2624cSystemTimeManualDaylightSavingsRecurringDayFrom = _Lgs2624cSystemTimeManualDaylightSavingsRecurringDayFrom_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 1, 9),
    _Lgs2624cSystemTimeManualDaylightSavingsRecurringDayFrom_Type()
)
lgs2624cSystemTimeManualDaylightSavingsRecurringDayFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeManualDaylightSavingsRecurringDayFrom.setStatus("current")


class _Lgs2624cSystemTimeManualDaylightSavingsRecurringWeekFrom_Type(Integer32):
    """Custom type lgs2624cSystemTimeManualDaylightSavingsRecurringWeekFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Lgs2624cSystemTimeManualDaylightSavingsRecurringWeekFrom_Type.__name__ = "Integer32"
_Lgs2624cSystemTimeManualDaylightSavingsRecurringWeekFrom_Object = MibScalar
lgs2624cSystemTimeManualDaylightSavingsRecurringWeekFrom = _Lgs2624cSystemTimeManualDaylightSavingsRecurringWeekFrom_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 1, 10),
    _Lgs2624cSystemTimeManualDaylightSavingsRecurringWeekFrom_Type()
)
lgs2624cSystemTimeManualDaylightSavingsRecurringWeekFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeManualDaylightSavingsRecurringWeekFrom.setStatus("current")


class _Lgs2624cSystemTimeManualDaylightSavingsRecurringMonthFrom_Type(Integer32):
    """Custom type lgs2624cSystemTimeManualDaylightSavingsRecurringMonthFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_Lgs2624cSystemTimeManualDaylightSavingsRecurringMonthFrom_Type.__name__ = "Integer32"
_Lgs2624cSystemTimeManualDaylightSavingsRecurringMonthFrom_Object = MibScalar
lgs2624cSystemTimeManualDaylightSavingsRecurringMonthFrom = _Lgs2624cSystemTimeManualDaylightSavingsRecurringMonthFrom_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 1, 11),
    _Lgs2624cSystemTimeManualDaylightSavingsRecurringMonthFrom_Type()
)
lgs2624cSystemTimeManualDaylightSavingsRecurringMonthFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeManualDaylightSavingsRecurringMonthFrom.setStatus("current")
_Lgs2624cSystemTimeManualDaylightSavingsRecurringTimeFrom_Type = DisplayString
_Lgs2624cSystemTimeManualDaylightSavingsRecurringTimeFrom_Object = MibScalar
lgs2624cSystemTimeManualDaylightSavingsRecurringTimeFrom = _Lgs2624cSystemTimeManualDaylightSavingsRecurringTimeFrom_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 1, 12),
    _Lgs2624cSystemTimeManualDaylightSavingsRecurringTimeFrom_Type()
)
lgs2624cSystemTimeManualDaylightSavingsRecurringTimeFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeManualDaylightSavingsRecurringTimeFrom.setStatus("current")


class _Lgs2624cSystemTimeManualDaylightSavingsRecurringDayTo_Type(Integer32):
    """Custom type lgs2624cSystemTimeManualDaylightSavingsRecurringDayTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Lgs2624cSystemTimeManualDaylightSavingsRecurringDayTo_Type.__name__ = "Integer32"
_Lgs2624cSystemTimeManualDaylightSavingsRecurringDayTo_Object = MibScalar
lgs2624cSystemTimeManualDaylightSavingsRecurringDayTo = _Lgs2624cSystemTimeManualDaylightSavingsRecurringDayTo_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 1, 13),
    _Lgs2624cSystemTimeManualDaylightSavingsRecurringDayTo_Type()
)
lgs2624cSystemTimeManualDaylightSavingsRecurringDayTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeManualDaylightSavingsRecurringDayTo.setStatus("current")


class _Lgs2624cSystemTimeManualDaylightSavingsRecurringWeekTo_Type(Integer32):
    """Custom type lgs2624cSystemTimeManualDaylightSavingsRecurringWeekTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Lgs2624cSystemTimeManualDaylightSavingsRecurringWeekTo_Type.__name__ = "Integer32"
_Lgs2624cSystemTimeManualDaylightSavingsRecurringWeekTo_Object = MibScalar
lgs2624cSystemTimeManualDaylightSavingsRecurringWeekTo = _Lgs2624cSystemTimeManualDaylightSavingsRecurringWeekTo_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 1, 14),
    _Lgs2624cSystemTimeManualDaylightSavingsRecurringWeekTo_Type()
)
lgs2624cSystemTimeManualDaylightSavingsRecurringWeekTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeManualDaylightSavingsRecurringWeekTo.setStatus("current")


class _Lgs2624cSystemTimeManualDaylightSavingsRecurringMonthTo_Type(Integer32):
    """Custom type lgs2624cSystemTimeManualDaylightSavingsRecurringMonthTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_Lgs2624cSystemTimeManualDaylightSavingsRecurringMonthTo_Type.__name__ = "Integer32"
_Lgs2624cSystemTimeManualDaylightSavingsRecurringMonthTo_Object = MibScalar
lgs2624cSystemTimeManualDaylightSavingsRecurringMonthTo = _Lgs2624cSystemTimeManualDaylightSavingsRecurringMonthTo_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 1, 15),
    _Lgs2624cSystemTimeManualDaylightSavingsRecurringMonthTo_Type()
)
lgs2624cSystemTimeManualDaylightSavingsRecurringMonthTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeManualDaylightSavingsRecurringMonthTo.setStatus("current")
_Lgs2624cSystemTimeManualDaylightSavingsRecurringTimeTo_Type = DisplayString
_Lgs2624cSystemTimeManualDaylightSavingsRecurringTimeTo_Object = MibScalar
lgs2624cSystemTimeManualDaylightSavingsRecurringTimeTo = _Lgs2624cSystemTimeManualDaylightSavingsRecurringTimeTo_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 1, 16),
    _Lgs2624cSystemTimeManualDaylightSavingsRecurringTimeTo_Type()
)
lgs2624cSystemTimeManualDaylightSavingsRecurringTimeTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeManualDaylightSavingsRecurringTimeTo.setStatus("current")
_Lgs2624cSystemTimeNTP_ObjectIdentity = ObjectIdentity
lgs2624cSystemTimeNTP = _Lgs2624cSystemTimeNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 2)
)
_Lgs2624cSystemTimeNTPTable_Object = MibTable
lgs2624cSystemTimeNTPTable = _Lgs2624cSystemTimeNTPTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lgs2624cSystemTimeNTPTable.setStatus("current")
_Lgs2624cSystemTimeNTPEntry_Object = MibTableRow
lgs2624cSystemTimeNTPEntry = _Lgs2624cSystemTimeNTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 2, 1, 1)
)
lgs2624cSystemTimeNTPEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cSystemTimeNTPIndex"),
)
if mibBuilder.loadTexts:
    lgs2624cSystemTimeNTPEntry.setStatus("current")


class _Lgs2624cSystemTimeNTPIndex_Type(Integer32):
    """Custom type lgs2624cSystemTimeNTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Lgs2624cSystemTimeNTPIndex_Type.__name__ = "Integer32"
_Lgs2624cSystemTimeNTPIndex_Object = MibTableColumn
lgs2624cSystemTimeNTPIndex = _Lgs2624cSystemTimeNTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 2, 1, 1, 1),
    _Lgs2624cSystemTimeNTPIndex_Type()
)
lgs2624cSystemTimeNTPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeNTPIndex.setStatus("current")


class _Lgs2624cSystemTimeNTPServerIPType_Type(Integer32):
    """Custom type lgs2624cSystemTimeNTPServerIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cSystemTimeNTPServerIPType_Type.__name__ = "Integer32"
_Lgs2624cSystemTimeNTPServerIPType_Object = MibTableColumn
lgs2624cSystemTimeNTPServerIPType = _Lgs2624cSystemTimeNTPServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 2, 1, 1, 2),
    _Lgs2624cSystemTimeNTPServerIPType_Type()
)
lgs2624cSystemTimeNTPServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeNTPServerIPType.setStatus("current")
_Lgs2624cSystemTimeNTPServer_Type = DisplayString
_Lgs2624cSystemTimeNTPServer_Object = MibTableColumn
lgs2624cSystemTimeNTPServer = _Lgs2624cSystemTimeNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 2, 1, 1, 3),
    _Lgs2624cSystemTimeNTPServer_Type()
)
lgs2624cSystemTimeNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeNTPServer.setStatus("current")


class _Lgs2624cSystemTimeNTPCurrentMode_Type(Integer32):
    """Custom type lgs2624cSystemTimeNTPCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Lgs2624cSystemTimeNTPCurrentMode_Type.__name__ = "Integer32"
_Lgs2624cSystemTimeNTPCurrentMode_Object = MibTableColumn
lgs2624cSystemTimeNTPCurrentMode = _Lgs2624cSystemTimeNTPCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 2, 2, 1, 1, 4),
    _Lgs2624cSystemTimeNTPCurrentMode_Type()
)
lgs2624cSystemTimeNTPCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemTimeNTPCurrentMode.setStatus("current")
_Lgs2624cSystemAccount_ObjectIdentity = ObjectIdentity
lgs2624cSystemAccount = _Lgs2624cSystemAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3)
)
_Lgs2624cSystemAccountUsers_ObjectIdentity = ObjectIdentity
lgs2624cSystemAccountUsers = _Lgs2624cSystemAccountUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 1)
)


class _Lgs2624cSystemAccountUserCreate_Type(Integer32):
    """Custom type lgs2624cSystemAccountUserCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cSystemAccountUserCreate_Type.__name__ = "Integer32"
_Lgs2624cSystemAccountUserCreate_Object = MibScalar
lgs2624cSystemAccountUserCreate = _Lgs2624cSystemAccountUserCreate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 1, 1),
    _Lgs2624cSystemAccountUserCreate_Type()
)
lgs2624cSystemAccountUserCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemAccountUserCreate.setStatus("current")
_Lgs2624cSystemAccountUsersTable_Object = MibTable
lgs2624cSystemAccountUsersTable = _Lgs2624cSystemAccountUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    lgs2624cSystemAccountUsersTable.setStatus("current")
_Lgs2624cSystemAccountUsersEntry_Object = MibTableRow
lgs2624cSystemAccountUsersEntry = _Lgs2624cSystemAccountUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 1, 2, 1)
)
lgs2624cSystemAccountUsersEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cUserIndex"),
)
if mibBuilder.loadTexts:
    lgs2624cSystemAccountUsersEntry.setStatus("current")


class _Lgs2624cUserIndex_Type(Integer32):
    """Custom type lgs2624cUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Lgs2624cUserIndex_Type.__name__ = "Integer32"
_Lgs2624cUserIndex_Object = MibTableColumn
lgs2624cUserIndex = _Lgs2624cUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 1, 2, 1, 1),
    _Lgs2624cUserIndex_Type()
)
lgs2624cUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cUserIndex.setStatus("current")


class _Lgs2624cUserName_Type(DisplayString):
    """Custom type lgs2624cUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Lgs2624cUserName_Type.__name__ = "DisplayString"
_Lgs2624cUserName_Object = MibTableColumn
lgs2624cUserName = _Lgs2624cUserName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 1, 2, 1, 2),
    _Lgs2624cUserName_Type()
)
lgs2624cUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cUserName.setStatus("current")


class _Lgs2624cPassword_Type(DisplayString):
    """Custom type lgs2624cPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Lgs2624cPassword_Type.__name__ = "DisplayString"
_Lgs2624cPassword_Object = MibTableColumn
lgs2624cPassword = _Lgs2624cPassword_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 1, 2, 1, 3),
    _Lgs2624cPassword_Type()
)
lgs2624cPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPassword.setStatus("current")


class _Lgs2624cUserPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cUserPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cUserPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cUserPrivilegeLevel_Object = MibTableColumn
lgs2624cUserPrivilegeLevel = _Lgs2624cUserPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 1, 2, 1, 4),
    _Lgs2624cUserPrivilegeLevel_Type()
)
lgs2624cUserPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cUserPrivilegeLevel.setStatus("current")


class _Lgs2624cAccountUserRowStatus_Type(Integer32):
    """Custom type lgs2624cAccountUserRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Lgs2624cAccountUserRowStatus_Type.__name__ = "Integer32"
_Lgs2624cAccountUserRowStatus_Object = MibTableColumn
lgs2624cAccountUserRowStatus = _Lgs2624cAccountUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 1, 2, 1, 5),
    _Lgs2624cAccountUserRowStatus_Type()
)
lgs2624cAccountUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cAccountUserRowStatus.setStatus("current")
_Lgs2624cSystemAccountPrivilegeLevel_ObjectIdentity = ObjectIdentity
lgs2624cSystemAccountPrivilegeLevel = _Lgs2624cSystemAccountPrivilegeLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2)
)


class _Lgs2624cAccountPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cAccountPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cAccountPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cAccountPrivilegeLevel_Object = MibScalar
lgs2624cAccountPrivilegeLevel = _Lgs2624cAccountPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 1),
    _Lgs2624cAccountPrivilegeLevel_Type()
)
lgs2624cAccountPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cAccountPrivilegeLevel.setStatus("current")


class _Lgs2624cAggregationPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cAggregationPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cAggregationPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cAggregationPrivilegeLevel_Object = MibScalar
lgs2624cAggregationPrivilegeLevel = _Lgs2624cAggregationPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 2),
    _Lgs2624cAggregationPrivilegeLevel_Type()
)
lgs2624cAggregationPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cAggregationPrivilegeLevel.setStatus("current")


class _Lgs2624cDiagnosticsPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cDiagnosticsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cDiagnosticsPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cDiagnosticsPrivilegeLevel_Object = MibScalar
lgs2624cDiagnosticsPrivilegeLevel = _Lgs2624cDiagnosticsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 3),
    _Lgs2624cDiagnosticsPrivilegeLevel_Type()
)
lgs2624cDiagnosticsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cDiagnosticsPrivilegeLevel.setStatus("current")


class _Lgs2624cEEEPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cEEEPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cEEEPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cEEEPrivilegeLevel_Object = MibScalar
lgs2624cEEEPrivilegeLevel = _Lgs2624cEEEPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 4),
    _Lgs2624cEEEPrivilegeLevel_Type()
)
lgs2624cEEEPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cEEEPrivilegeLevel.setStatus("current")


class _Lgs2624cEasyportPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cEasyportPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cEasyportPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cEasyportPrivilegeLevel_Object = MibScalar
lgs2624cEasyportPrivilegeLevel = _Lgs2624cEasyportPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 5),
    _Lgs2624cEasyportPrivilegeLevel_Type()
)
lgs2624cEasyportPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cEasyportPrivilegeLevel.setStatus("current")


class _Lgs2624cGARPPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cGARPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cGARPPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cGARPPrivilegeLevel_Object = MibScalar
lgs2624cGARPPrivilegeLevel = _Lgs2624cGARPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 6),
    _Lgs2624cGARPPrivilegeLevel_Type()
)
lgs2624cGARPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cGARPPrivilegeLevel.setStatus("current")


class _Lgs2624cGVRPPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cGVRPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cGVRPPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cGVRPPrivilegeLevel_Object = MibScalar
lgs2624cGVRPPrivilegeLevel = _Lgs2624cGVRPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 7),
    _Lgs2624cGVRPPrivilegeLevel_Type()
)
lgs2624cGVRPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cGVRPPrivilegeLevel.setStatus("current")


class _Lgs2624cIPPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cIPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cIPPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cIPPrivilegeLevel_Object = MibScalar
lgs2624cIPPrivilegeLevel = _Lgs2624cIPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 8),
    _Lgs2624cIPPrivilegeLevel_Type()
)
lgs2624cIPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIPPrivilegeLevel.setStatus("current")


class _Lgs2624cIPMCSnoopingPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cIPMCSnoopingPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cIPMCSnoopingPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cIPMCSnoopingPrivilegeLevel_Object = MibScalar
lgs2624cIPMCSnoopingPrivilegeLevel = _Lgs2624cIPMCSnoopingPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 9),
    _Lgs2624cIPMCSnoopingPrivilegeLevel_Type()
)
lgs2624cIPMCSnoopingPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIPMCSnoopingPrivilegeLevel.setStatus("current")


class _Lgs2624cLACPPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cLACPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cLACPPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cLACPPrivilegeLevel_Object = MibScalar
lgs2624cLACPPrivilegeLevel = _Lgs2624cLACPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 10),
    _Lgs2624cLACPPrivilegeLevel_Type()
)
lgs2624cLACPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cLACPPrivilegeLevel.setStatus("current")


class _Lgs2624cLLDPPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cLLDPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cLLDPPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cLLDPPrivilegeLevel_Object = MibScalar
lgs2624cLLDPPrivilegeLevel = _Lgs2624cLLDPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 11),
    _Lgs2624cLLDPPrivilegeLevel_Type()
)
lgs2624cLLDPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cLLDPPrivilegeLevel.setStatus("current")


class _Lgs2624cLLDPMEDPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cLLDPMEDPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cLLDPMEDPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cLLDPMEDPrivilegeLevel_Object = MibScalar
lgs2624cLLDPMEDPrivilegeLevel = _Lgs2624cLLDPMEDPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 12),
    _Lgs2624cLLDPMEDPrivilegeLevel_Type()
)
lgs2624cLLDPMEDPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cLLDPMEDPrivilegeLevel.setStatus("current")


class _Lgs2624cMACTablePrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cMACTablePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cMACTablePrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cMACTablePrivilegeLevel_Object = MibScalar
lgs2624cMACTablePrivilegeLevel = _Lgs2624cMACTablePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 13),
    _Lgs2624cMACTablePrivilegeLevel_Type()
)
lgs2624cMACTablePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cMACTablePrivilegeLevel.setStatus("current")


class _Lgs2624cMRPPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cMRPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cMRPPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cMRPPrivilegeLevel_Object = MibScalar
lgs2624cMRPPrivilegeLevel = _Lgs2624cMRPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 14),
    _Lgs2624cMRPPrivilegeLevel_Type()
)
lgs2624cMRPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cMRPPrivilegeLevel.setStatus("current")


class _Lgs2624cMVRPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cMVRPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cMVRPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cMVRPrivilegeLevel_Object = MibScalar
lgs2624cMVRPrivilegeLevel = _Lgs2624cMVRPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 15),
    _Lgs2624cMVRPrivilegeLevel_Type()
)
lgs2624cMVRPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cMVRPrivilegeLevel.setStatus("current")


class _Lgs2624cMVRPPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cMVRPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cMVRPPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cMVRPPrivilegeLevel_Object = MibScalar
lgs2624cMVRPPrivilegeLevel = _Lgs2624cMVRPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 16),
    _Lgs2624cMVRPPrivilegeLevel_Type()
)
lgs2624cMVRPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cMVRPPrivilegeLevel.setStatus("current")


class _Lgs2624cMaintenancePrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cMaintenancePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cMaintenancePrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cMaintenancePrivilegeLevel_Object = MibScalar
lgs2624cMaintenancePrivilegeLevel = _Lgs2624cMaintenancePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 17),
    _Lgs2624cMaintenancePrivilegeLevel_Type()
)
lgs2624cMaintenancePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cMaintenancePrivilegeLevel.setStatus("current")


class _Lgs2624cMirroringPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cMirroringPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cMirroringPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cMirroringPrivilegeLevel_Object = MibScalar
lgs2624cMirroringPrivilegeLevel = _Lgs2624cMirroringPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 18),
    _Lgs2624cMirroringPrivilegeLevel_Type()
)
lgs2624cMirroringPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cMirroringPrivilegeLevel.setStatus("current")


class _Lgs2624cPortsPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cPortsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cPortsPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cPortsPrivilegeLevel_Object = MibScalar
lgs2624cPortsPrivilegeLevel = _Lgs2624cPortsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 19),
    _Lgs2624cPortsPrivilegeLevel_Type()
)
lgs2624cPortsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortsPrivilegeLevel.setStatus("current")


class _Lgs2624cPrivateVLANsPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cPrivateVLANsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cPrivateVLANsPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cPrivateVLANsPrivilegeLevel_Object = MibScalar
lgs2624cPrivateVLANsPrivilegeLevel = _Lgs2624cPrivateVLANsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 20),
    _Lgs2624cPrivateVLANsPrivilegeLevel_Type()
)
lgs2624cPrivateVLANsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPrivateVLANsPrivilegeLevel.setStatus("current")


class _Lgs2624cQoSPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cQoSPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cQoSPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cQoSPrivilegeLevel_Object = MibScalar
lgs2624cQoSPrivilegeLevel = _Lgs2624cQoSPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 21),
    _Lgs2624cQoSPrivilegeLevel_Type()
)
lgs2624cQoSPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cQoSPrivilegeLevel.setStatus("current")


class _Lgs2624cSMTPPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cSMTPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cSMTPPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cSMTPPrivilegeLevel_Object = MibScalar
lgs2624cSMTPPrivilegeLevel = _Lgs2624cSMTPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 22),
    _Lgs2624cSMTPPrivilegeLevel_Type()
)
lgs2624cSMTPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSMTPPrivilegeLevel.setStatus("current")


class _Lgs2624cSNMPPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cSNMPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cSNMPPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cSNMPPrivilegeLevel_Object = MibScalar
lgs2624cSNMPPrivilegeLevel = _Lgs2624cSNMPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 23),
    _Lgs2624cSNMPPrivilegeLevel_Type()
)
lgs2624cSNMPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSNMPPrivilegeLevel.setStatus("current")


class _Lgs2624cSecurityPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cSecurityPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cSecurityPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cSecurityPrivilegeLevel_Object = MibScalar
lgs2624cSecurityPrivilegeLevel = _Lgs2624cSecurityPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 24),
    _Lgs2624cSecurityPrivilegeLevel_Type()
)
lgs2624cSecurityPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSecurityPrivilegeLevel.setStatus("current")


class _Lgs2624cSpanningTreePrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cSpanningTreePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cSpanningTreePrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cSpanningTreePrivilegeLevel_Object = MibScalar
lgs2624cSpanningTreePrivilegeLevel = _Lgs2624cSpanningTreePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 25),
    _Lgs2624cSpanningTreePrivilegeLevel_Type()
)
lgs2624cSpanningTreePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSpanningTreePrivilegeLevel.setStatus("current")


class _Lgs2624cSystemPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cSystemPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cSystemPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cSystemPrivilegeLevel_Object = MibScalar
lgs2624cSystemPrivilegeLevel = _Lgs2624cSystemPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 26),
    _Lgs2624cSystemPrivilegeLevel_Type()
)
lgs2624cSystemPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSystemPrivilegeLevel.setStatus("current")


class _Lgs2624cTrapEventPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cTrapEventPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cTrapEventPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cTrapEventPrivilegeLevel_Object = MibScalar
lgs2624cTrapEventPrivilegeLevel = _Lgs2624cTrapEventPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 27),
    _Lgs2624cTrapEventPrivilegeLevel_Type()
)
lgs2624cTrapEventPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventPrivilegeLevel.setStatus("current")


class _Lgs2624cVCLPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cVCLPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cVCLPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cVCLPrivilegeLevel_Object = MibScalar
lgs2624cVCLPrivilegeLevel = _Lgs2624cVCLPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 28),
    _Lgs2624cVCLPrivilegeLevel_Type()
)
lgs2624cVCLPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cVCLPrivilegeLevel.setStatus("current")


class _Lgs2624cVLANsPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cVLANsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cVLANsPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cVLANsPrivilegeLevel_Object = MibScalar
lgs2624cVLANsPrivilegeLevel = _Lgs2624cVLANsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 29),
    _Lgs2624cVLANsPrivilegeLevel_Type()
)
lgs2624cVLANsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cVLANsPrivilegeLevel.setStatus("current")


class _Lgs2624cVoiceVLANPrivilegeLevel_Type(Integer32):
    """Custom type lgs2624cVoiceVLANPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Lgs2624cVoiceVLANPrivilegeLevel_Type.__name__ = "Integer32"
_Lgs2624cVoiceVLANPrivilegeLevel_Object = MibScalar
lgs2624cVoiceVLANPrivilegeLevel = _Lgs2624cVoiceVLANPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 3, 2, 30),
    _Lgs2624cVoiceVLANPrivilegeLevel_Type()
)
lgs2624cVoiceVLANPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cVoiceVLANPrivilegeLevel.setStatus("current")
_Lgs2624cIP_ObjectIdentity = ObjectIdentity
lgs2624cIP = _Lgs2624cIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4)
)
_Lgs2624cIPv4_ObjectIdentity = ObjectIdentity
lgs2624cIPv4 = _Lgs2624cIPv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 1)
)
_Lgs2624cIPv4Configured_ObjectIdentity = ObjectIdentity
lgs2624cIPv4Configured = _Lgs2624cIPv4Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 1, 1)
)


class _Lgs2624cIpv4DHCPClient_Type(Integer32):
    """Custom type lgs2624cIpv4DHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cIpv4DHCPClient_Type.__name__ = "Integer32"
_Lgs2624cIpv4DHCPClient_Object = MibScalar
lgs2624cIpv4DHCPClient = _Lgs2624cIpv4DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 1, 1, 1),
    _Lgs2624cIpv4DHCPClient_Type()
)
lgs2624cIpv4DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIpv4DHCPClient.setStatus("current")
_Lgs2624cIPv4Address_Type = IpAddress
_Lgs2624cIPv4Address_Object = MibScalar
lgs2624cIPv4Address = _Lgs2624cIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 1, 1, 2),
    _Lgs2624cIPv4Address_Type()
)
lgs2624cIPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIPv4Address.setStatus("current")
_Lgs2624cIPv4Mask_Type = IpAddress
_Lgs2624cIPv4Mask_Object = MibScalar
lgs2624cIPv4Mask = _Lgs2624cIPv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 1, 1, 3),
    _Lgs2624cIPv4Mask_Type()
)
lgs2624cIPv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIPv4Mask.setStatus("current")
_Lgs2624cIPv4Router_Type = IpAddress
_Lgs2624cIPv4Router_Object = MibScalar
lgs2624cIPv4Router = _Lgs2624cIPv4Router_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 1, 1, 4),
    _Lgs2624cIPv4Router_Type()
)
lgs2624cIPv4Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIPv4Router.setStatus("current")


class _Lgs2624cIPv4VLANId_Type(Integer32):
    """Custom type lgs2624cIPv4VLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2624cIPv4VLANId_Type.__name__ = "Integer32"
_Lgs2624cIPv4VLANId_Object = MibScalar
lgs2624cIPv4VLANId = _Lgs2624cIPv4VLANId_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 1, 1, 5),
    _Lgs2624cIPv4VLANId_Type()
)
lgs2624cIPv4VLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIPv4VLANId.setStatus("current")
_Lgs2624cIPv4DNSServer_Type = IpAddress
_Lgs2624cIPv4DNSServer_Object = MibScalar
lgs2624cIPv4DNSServer = _Lgs2624cIPv4DNSServer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 1, 1, 6),
    _Lgs2624cIPv4DNSServer_Type()
)
lgs2624cIPv4DNSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIPv4DNSServer.setStatus("current")


class _Lgs2624cIPv4DNSProxy_Type(Integer32):
    """Custom type lgs2624cIPv4DNSProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cIPv4DNSProxy_Type.__name__ = "Integer32"
_Lgs2624cIPv4DNSProxy_Object = MibScalar
lgs2624cIPv4DNSProxy = _Lgs2624cIPv4DNSProxy_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 1, 1, 7),
    _Lgs2624cIPv4DNSProxy_Type()
)
lgs2624cIPv4DNSProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIPv4DNSProxy.setStatus("current")
_Lgs2624cIPv4Current_ObjectIdentity = ObjectIdentity
lgs2624cIPv4Current = _Lgs2624cIPv4Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 1, 2)
)


class _Lgs2624cIpv4CurrentDHCPClient_Type(Integer32):
    """Custom type lgs2624cIpv4CurrentDHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cIpv4CurrentDHCPClient_Type.__name__ = "Integer32"
_Lgs2624cIpv4CurrentDHCPClient_Object = MibScalar
lgs2624cIpv4CurrentDHCPClient = _Lgs2624cIpv4CurrentDHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 1, 2, 1),
    _Lgs2624cIpv4CurrentDHCPClient_Type()
)
lgs2624cIpv4CurrentDHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIpv4CurrentDHCPClient.setStatus("current")
_Lgs2624cIPv4CurrentAddress_Type = IpAddress
_Lgs2624cIPv4CurrentAddress_Object = MibScalar
lgs2624cIPv4CurrentAddress = _Lgs2624cIPv4CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 1, 2, 2),
    _Lgs2624cIPv4CurrentAddress_Type()
)
lgs2624cIPv4CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cIPv4CurrentAddress.setStatus("current")
_Lgs2624cIPv4CurrentMask_Type = IpAddress
_Lgs2624cIPv4CurrentMask_Object = MibScalar
lgs2624cIPv4CurrentMask = _Lgs2624cIPv4CurrentMask_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 1, 2, 3),
    _Lgs2624cIPv4CurrentMask_Type()
)
lgs2624cIPv4CurrentMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cIPv4CurrentMask.setStatus("current")
_Lgs2624cIPv4CurrentRouter_Type = IpAddress
_Lgs2624cIPv4CurrentRouter_Object = MibScalar
lgs2624cIPv4CurrentRouter = _Lgs2624cIPv4CurrentRouter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 1, 2, 4),
    _Lgs2624cIPv4CurrentRouter_Type()
)
lgs2624cIPv4CurrentRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cIPv4CurrentRouter.setStatus("current")


class _Lgs2624cIPv4CurrentVLANId_Type(Integer32):
    """Custom type lgs2624cIPv4CurrentVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2624cIPv4CurrentVLANId_Type.__name__ = "Integer32"
_Lgs2624cIPv4CurrentVLANId_Object = MibScalar
lgs2624cIPv4CurrentVLANId = _Lgs2624cIPv4CurrentVLANId_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 1, 2, 5),
    _Lgs2624cIPv4CurrentVLANId_Type()
)
lgs2624cIPv4CurrentVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cIPv4CurrentVLANId.setStatus("current")
_Lgs2624cIPv4CurrentDNSServer_Type = IpAddress
_Lgs2624cIPv4CurrentDNSServer_Object = MibScalar
lgs2624cIPv4CurrentDNSServer = _Lgs2624cIPv4CurrentDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 1, 2, 6),
    _Lgs2624cIPv4CurrentDNSServer_Type()
)
lgs2624cIPv4CurrentDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cIPv4CurrentDNSServer.setStatus("current")
_Lgs2624cIPv6_ObjectIdentity = ObjectIdentity
lgs2624cIPv6 = _Lgs2624cIPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 2)
)
_Lgs2624cIPv6Configured_ObjectIdentity = ObjectIdentity
lgs2624cIPv6Configured = _Lgs2624cIPv6Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 2, 1)
)


class _Lgs2624cIpv6AutoConfiguration_Type(Integer32):
    """Custom type lgs2624cIpv6AutoConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cIpv6AutoConfiguration_Type.__name__ = "Integer32"
_Lgs2624cIpv6AutoConfiguration_Object = MibScalar
lgs2624cIpv6AutoConfiguration = _Lgs2624cIpv6AutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 2, 1, 1),
    _Lgs2624cIpv6AutoConfiguration_Type()
)
lgs2624cIpv6AutoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIpv6AutoConfiguration.setStatus("current")


class _Lgs2624cIpv6Address_Type(DisplayString):
    """Custom type lgs2624cIpv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Lgs2624cIpv6Address_Type.__name__ = "DisplayString"
_Lgs2624cIpv6Address_Object = MibScalar
lgs2624cIpv6Address = _Lgs2624cIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 2, 1, 2),
    _Lgs2624cIpv6Address_Type()
)
lgs2624cIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIpv6Address.setStatus("current")


class _Lgs2624cIpv6Prefix_Type(Integer32):
    """Custom type lgs2624cIpv6Prefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Lgs2624cIpv6Prefix_Type.__name__ = "Integer32"
_Lgs2624cIpv6Prefix_Object = MibScalar
lgs2624cIpv6Prefix = _Lgs2624cIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 2, 1, 3),
    _Lgs2624cIpv6Prefix_Type()
)
lgs2624cIpv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIpv6Prefix.setStatus("current")


class _Lgs2624cIpv6Router_Type(DisplayString):
    """Custom type lgs2624cIpv6Router based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Lgs2624cIpv6Router_Type.__name__ = "DisplayString"
_Lgs2624cIpv6Router_Object = MibScalar
lgs2624cIpv6Router = _Lgs2624cIpv6Router_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 2, 1, 4),
    _Lgs2624cIpv6Router_Type()
)
lgs2624cIpv6Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIpv6Router.setStatus("current")
_Lgs2624cIPv6Current_ObjectIdentity = ObjectIdentity
lgs2624cIPv6Current = _Lgs2624cIPv6Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 2, 2)
)


class _Lgs2624cIpv6CurrentAutoConfiguration_Type(Integer32):
    """Custom type lgs2624cIpv6CurrentAutoConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cIpv6CurrentAutoConfiguration_Type.__name__ = "Integer32"
_Lgs2624cIpv6CurrentAutoConfiguration_Object = MibScalar
lgs2624cIpv6CurrentAutoConfiguration = _Lgs2624cIpv6CurrentAutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 2, 2, 1),
    _Lgs2624cIpv6CurrentAutoConfiguration_Type()
)
lgs2624cIpv6CurrentAutoConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cIpv6CurrentAutoConfiguration.setStatus("current")


class _Lgs2624cIpv6CurrentAddress_Type(DisplayString):
    """Custom type lgs2624cIpv6CurrentAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Lgs2624cIpv6CurrentAddress_Type.__name__ = "DisplayString"
_Lgs2624cIpv6CurrentAddress_Object = MibScalar
lgs2624cIpv6CurrentAddress = _Lgs2624cIpv6CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 2, 2, 2),
    _Lgs2624cIpv6CurrentAddress_Type()
)
lgs2624cIpv6CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cIpv6CurrentAddress.setStatus("current")


class _Lgs2624cIpv6CurrentLinkLocalAddress_Type(DisplayString):
    """Custom type lgs2624cIpv6CurrentLinkLocalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Lgs2624cIpv6CurrentLinkLocalAddress_Type.__name__ = "DisplayString"
_Lgs2624cIpv6CurrentLinkLocalAddress_Object = MibScalar
lgs2624cIpv6CurrentLinkLocalAddress = _Lgs2624cIpv6CurrentLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 2, 2, 3),
    _Lgs2624cIpv6CurrentLinkLocalAddress_Type()
)
lgs2624cIpv6CurrentLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cIpv6CurrentLinkLocalAddress.setStatus("current")


class _Lgs2624cIpv6CurrentPrefix_Type(Integer32):
    """Custom type lgs2624cIpv6CurrentPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Lgs2624cIpv6CurrentPrefix_Type.__name__ = "Integer32"
_Lgs2624cIpv6CurrentPrefix_Object = MibScalar
lgs2624cIpv6CurrentPrefix = _Lgs2624cIpv6CurrentPrefix_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 2, 2, 4),
    _Lgs2624cIpv6CurrentPrefix_Type()
)
lgs2624cIpv6CurrentPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cIpv6CurrentPrefix.setStatus("current")


class _Lgs2624cIpv6CurrentRouter_Type(DisplayString):
    """Custom type lgs2624cIpv6CurrentRouter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Lgs2624cIpv6CurrentRouter_Type.__name__ = "DisplayString"
_Lgs2624cIpv6CurrentRouter_Object = MibScalar
lgs2624cIpv6CurrentRouter = _Lgs2624cIpv6CurrentRouter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 4, 2, 2, 5),
    _Lgs2624cIpv6CurrentRouter_Type()
)
lgs2624cIpv6CurrentRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cIpv6CurrentRouter.setStatus("current")
_Lgs2624cSyslog_ObjectIdentity = ObjectIdentity
lgs2624cSyslog = _Lgs2624cSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 5)
)
_Lgs2624cSyslogConf_ObjectIdentity = ObjectIdentity
lgs2624cSyslogConf = _Lgs2624cSyslogConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 5, 1)
)


class _Lgs2624cServerMode_Type(Integer32):
    """Custom type lgs2624cServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cServerMode_Type.__name__ = "Integer32"
_Lgs2624cServerMode_Object = MibScalar
lgs2624cServerMode = _Lgs2624cServerMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 5, 1, 1),
    _Lgs2624cServerMode_Type()
)
lgs2624cServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cServerMode.setStatus("current")
_Lgs2624cServerAddress1_Type = IpAddress
_Lgs2624cServerAddress1_Object = MibScalar
lgs2624cServerAddress1 = _Lgs2624cServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 5, 1, 2),
    _Lgs2624cServerAddress1_Type()
)
lgs2624cServerAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cServerAddress1.setStatus("current")
_Lgs2624cServerAddress2_Type = IpAddress
_Lgs2624cServerAddress2_Object = MibScalar
lgs2624cServerAddress2 = _Lgs2624cServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 5, 1, 3),
    _Lgs2624cServerAddress2_Type()
)
lgs2624cServerAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cServerAddress2.setStatus("current")


class _Lgs2624cSyslogLevel_Type(Integer32):
    """Custom type lgs2624cSyslogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cSyslogLevel_Type.__name__ = "Integer32"
_Lgs2624cSyslogLevel_Object = MibScalar
lgs2624cSyslogLevel = _Lgs2624cSyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 5, 1, 4),
    _Lgs2624cSyslogLevel_Type()
)
lgs2624cSyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSyslogLevel.setStatus("current")
_Lgs2624cSyslogDetailedInfo_ObjectIdentity = ObjectIdentity
lgs2624cSyslogDetailedInfo = _Lgs2624cSyslogDetailedInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 5, 2)
)


class _Lgs2624cSyslogDetailedInfoClear_Type(Integer32):
    """Custom type lgs2624cSyslogDetailedInfoClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cSyslogDetailedInfoClear_Type.__name__ = "Integer32"
_Lgs2624cSyslogDetailedInfoClear_Object = MibScalar
lgs2624cSyslogDetailedInfoClear = _Lgs2624cSyslogDetailedInfoClear_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 5, 2, 1),
    _Lgs2624cSyslogDetailedInfoClear_Type()
)
lgs2624cSyslogDetailedInfoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSyslogDetailedInfoClear.setStatus("current")
_Lgs2624cSyslogDetailedInfoTable_Object = MibTable
lgs2624cSyslogDetailedInfoTable = _Lgs2624cSyslogDetailedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    lgs2624cSyslogDetailedInfoTable.setStatus("current")
_Lgs2624cSyslogDetailedInfoEntry_Object = MibTableRow
lgs2624cSyslogDetailedInfoEntry = _Lgs2624cSyslogDetailedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 5, 2, 2, 1)
)
lgs2624cSyslogDetailedInfoEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cSyslogDetailedInfoIndex"),
)
if mibBuilder.loadTexts:
    lgs2624cSyslogDetailedInfoEntry.setStatus("current")


class _Lgs2624cSyslogDetailedInfoIndex_Type(Integer32):
    """Custom type lgs2624cSyslogDetailedInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Lgs2624cSyslogDetailedInfoIndex_Type.__name__ = "Integer32"
_Lgs2624cSyslogDetailedInfoIndex_Object = MibTableColumn
lgs2624cSyslogDetailedInfoIndex = _Lgs2624cSyslogDetailedInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 5, 2, 2, 1, 1),
    _Lgs2624cSyslogDetailedInfoIndex_Type()
)
lgs2624cSyslogDetailedInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cSyslogDetailedInfoIndex.setStatus("current")
_Lgs2624cSyslogDetailedInfoLevel_Type = DisplayString
_Lgs2624cSyslogDetailedInfoLevel_Object = MibTableColumn
lgs2624cSyslogDetailedInfoLevel = _Lgs2624cSyslogDetailedInfoLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 5, 2, 2, 1, 2),
    _Lgs2624cSyslogDetailedInfoLevel_Type()
)
lgs2624cSyslogDetailedInfoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSyslogDetailedInfoLevel.setStatus("current")


class _Lgs2624cSyslogDetailedInfoTime_Type(DisplayString):
    """Custom type lgs2624cSyslogDetailedInfoTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Lgs2624cSyslogDetailedInfoTime_Type.__name__ = "DisplayString"
_Lgs2624cSyslogDetailedInfoTime_Object = MibTableColumn
lgs2624cSyslogDetailedInfoTime = _Lgs2624cSyslogDetailedInfoTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 5, 2, 2, 1, 3),
    _Lgs2624cSyslogDetailedInfoTime_Type()
)
lgs2624cSyslogDetailedInfoTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSyslogDetailedInfoTime.setStatus("current")
_Lgs2624cSyslogDetailedInfoMessage_Type = DisplayString
_Lgs2624cSyslogDetailedInfoMessage_Object = MibTableColumn
lgs2624cSyslogDetailedInfoMessage = _Lgs2624cSyslogDetailedInfoMessage_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 5, 2, 2, 1, 4),
    _Lgs2624cSyslogDetailedInfoMessage_Type()
)
lgs2624cSyslogDetailedInfoMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSyslogDetailedInfoMessage.setStatus("current")
_Lgs2624cSnmp_ObjectIdentity = ObjectIdentity
lgs2624cSnmp = _Lgs2624cSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6)
)
_Lgs2624cSnmpConf_ObjectIdentity = ObjectIdentity
lgs2624cSnmpConf = _Lgs2624cSnmpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1)
)
_Lgs2624cGetCommunity_Type = DisplayString
_Lgs2624cGetCommunity_Object = MibScalar
lgs2624cGetCommunity = _Lgs2624cGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1, 1),
    _Lgs2624cGetCommunity_Type()
)
lgs2624cGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cGetCommunity.setStatus("current")


class _Lgs2624cSetCommunityMode_Type(Integer32):
    """Custom type lgs2624cSetCommunityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cSetCommunityMode_Type.__name__ = "Integer32"
_Lgs2624cSetCommunityMode_Object = MibScalar
lgs2624cSetCommunityMode = _Lgs2624cSetCommunityMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1, 2),
    _Lgs2624cSetCommunityMode_Type()
)
lgs2624cSetCommunityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSetCommunityMode.setStatus("current")
_Lgs2624cSetCommunity_Type = DisplayString
_Lgs2624cSetCommunity_Object = MibScalar
lgs2624cSetCommunity = _Lgs2624cSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1, 3),
    _Lgs2624cSetCommunity_Type()
)
lgs2624cSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSetCommunity.setStatus("current")
_Lgs2624cTrapHostConfTable_Object = MibTable
lgs2624cTrapHostConfTable = _Lgs2624cTrapHostConfTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1, 4)
)
if mibBuilder.loadTexts:
    lgs2624cTrapHostConfTable.setStatus("current")
_Lgs2624cTrapHostConfEntry_Object = MibTableRow
lgs2624cTrapHostConfEntry = _Lgs2624cTrapHostConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1, 4, 1)
)
lgs2624cTrapHostConfEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cTrapHostConfIndex"),
)
if mibBuilder.loadTexts:
    lgs2624cTrapHostConfEntry.setStatus("current")


class _Lgs2624cTrapHostConfIndex_Type(Integer32):
    """Custom type lgs2624cTrapHostConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Lgs2624cTrapHostConfIndex_Type.__name__ = "Integer32"
_Lgs2624cTrapHostConfIndex_Object = MibTableColumn
lgs2624cTrapHostConfIndex = _Lgs2624cTrapHostConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1, 4, 1, 1),
    _Lgs2624cTrapHostConfIndex_Type()
)
lgs2624cTrapHostConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cTrapHostConfIndex.setStatus("current")


class _Lgs2624cTrapHostConfVersion_Type(Integer32):
    """Custom type lgs2624cTrapHostConfVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3),
    )


_Lgs2624cTrapHostConfVersion_Type.__name__ = "Integer32"
_Lgs2624cTrapHostConfVersion_Object = MibTableColumn
lgs2624cTrapHostConfVersion = _Lgs2624cTrapHostConfVersion_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1, 4, 1, 2),
    _Lgs2624cTrapHostConfVersion_Type()
)
lgs2624cTrapHostConfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapHostConfVersion.setStatus("current")


class _Lgs2624cTrapHostConfIPType_Type(Integer32):
    """Custom type lgs2624cTrapHostConfIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(6, 6),
    )


_Lgs2624cTrapHostConfIPType_Type.__name__ = "Integer32"
_Lgs2624cTrapHostConfIPType_Object = MibTableColumn
lgs2624cTrapHostConfIPType = _Lgs2624cTrapHostConfIPType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1, 4, 1, 3),
    _Lgs2624cTrapHostConfIPType_Type()
)
lgs2624cTrapHostConfIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapHostConfIPType.setStatus("current")
_Lgs2624cTrapHostConfIP_Type = DisplayString
_Lgs2624cTrapHostConfIP_Object = MibTableColumn
lgs2624cTrapHostConfIP = _Lgs2624cTrapHostConfIP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1, 4, 1, 4),
    _Lgs2624cTrapHostConfIP_Type()
)
lgs2624cTrapHostConfIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapHostConfIP.setStatus("current")


class _Lgs2624cTrapHostConfPort_Type(Integer32):
    """Custom type lgs2624cTrapHostConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Lgs2624cTrapHostConfPort_Type.__name__ = "Integer32"
_Lgs2624cTrapHostConfPort_Object = MibTableColumn
lgs2624cTrapHostConfPort = _Lgs2624cTrapHostConfPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1, 4, 1, 5),
    _Lgs2624cTrapHostConfPort_Type()
)
lgs2624cTrapHostConfPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapHostConfPort.setStatus("current")


class _Lgs2624cTrapHostConfCommunity_Type(DisplayString):
    """Custom type lgs2624cTrapHostConfCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Lgs2624cTrapHostConfCommunity_Type.__name__ = "DisplayString"
_Lgs2624cTrapHostConfCommunity_Object = MibTableColumn
lgs2624cTrapHostConfCommunity = _Lgs2624cTrapHostConfCommunity_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1, 4, 1, 6),
    _Lgs2624cTrapHostConfCommunity_Type()
)
lgs2624cTrapHostConfCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapHostConfCommunity.setStatus("current")


class _Lgs2624cTrapHostConfSeverityLevel_Type(Integer32):
    """Custom type lgs2624cTrapHostConfSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapHostConfSeverityLevel_Type.__name__ = "Integer32"
_Lgs2624cTrapHostConfSeverityLevel_Object = MibTableColumn
lgs2624cTrapHostConfSeverityLevel = _Lgs2624cTrapHostConfSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1, 4, 1, 7),
    _Lgs2624cTrapHostConfSeverityLevel_Type()
)
lgs2624cTrapHostConfSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapHostConfSeverityLevel.setStatus("current")


class _Lgs2624cTrapHostConfSecurityLevel_Type(Integer32):
    """Custom type lgs2624cTrapHostConfSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Lgs2624cTrapHostConfSecurityLevel_Type.__name__ = "Integer32"
_Lgs2624cTrapHostConfSecurityLevel_Object = MibTableColumn
lgs2624cTrapHostConfSecurityLevel = _Lgs2624cTrapHostConfSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1, 4, 1, 8),
    _Lgs2624cTrapHostConfSecurityLevel_Type()
)
lgs2624cTrapHostConfSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapHostConfSecurityLevel.setStatus("current")


class _Lgs2624cTrapHostConfAuthPtc_Type(Integer32):
    """Custom type lgs2624cTrapHostConfAuthPtc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Lgs2624cTrapHostConfAuthPtc_Type.__name__ = "Integer32"
_Lgs2624cTrapHostConfAuthPtc_Object = MibTableColumn
lgs2624cTrapHostConfAuthPtc = _Lgs2624cTrapHostConfAuthPtc_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1, 4, 1, 9),
    _Lgs2624cTrapHostConfAuthPtc_Type()
)
lgs2624cTrapHostConfAuthPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapHostConfAuthPtc.setStatus("current")
_Lgs2624cTrapHostConfAuthPassword_Type = DisplayString
_Lgs2624cTrapHostConfAuthPassword_Object = MibTableColumn
lgs2624cTrapHostConfAuthPassword = _Lgs2624cTrapHostConfAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1, 4, 1, 10),
    _Lgs2624cTrapHostConfAuthPassword_Type()
)
lgs2624cTrapHostConfAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapHostConfAuthPassword.setStatus("current")


class _Lgs2624cTrapHostConfPrivPtc_Type(Integer32):
    """Custom type lgs2624cTrapHostConfPrivPtc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cTrapHostConfPrivPtc_Type.__name__ = "Integer32"
_Lgs2624cTrapHostConfPrivPtc_Object = MibTableColumn
lgs2624cTrapHostConfPrivPtc = _Lgs2624cTrapHostConfPrivPtc_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1, 4, 1, 11),
    _Lgs2624cTrapHostConfPrivPtc_Type()
)
lgs2624cTrapHostConfPrivPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapHostConfPrivPtc.setStatus("current")
_Lgs2624cTrapHostConfPrivPassword_Type = DisplayString
_Lgs2624cTrapHostConfPrivPassword_Object = MibTableColumn
lgs2624cTrapHostConfPrivPassword = _Lgs2624cTrapHostConfPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1, 4, 1, 12),
    _Lgs2624cTrapHostConfPrivPassword_Type()
)
lgs2624cTrapHostConfPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapHostConfPrivPassword.setStatus("current")


class _Lgs2624cTrapHostConfCurrentMode_Type(Integer32):
    """Custom type lgs2624cTrapHostConfCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2624cTrapHostConfCurrentMode_Type.__name__ = "Integer32"
_Lgs2624cTrapHostConfCurrentMode_Object = MibTableColumn
lgs2624cTrapHostConfCurrentMode = _Lgs2624cTrapHostConfCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 1, 6, 1, 4, 1, 13),
    _Lgs2624cTrapHostConfCurrentMode_Type()
)
lgs2624cTrapHostConfCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapHostConfCurrentMode.setStatus("current")
_Lgs2624cConfiguration_ObjectIdentity = ObjectIdentity
lgs2624cConfiguration = _Lgs2624cConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2)
)
_Lgs2624cPort_ObjectIdentity = ObjectIdentity
lgs2624cPort = _Lgs2624cPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1)
)
_Lgs2624cPortConfigurationTable_Object = MibTable
lgs2624cPortConfigurationTable = _Lgs2624cPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lgs2624cPortConfigurationTable.setStatus("current")
_Lgs2624cPortConfigurationEntry_Object = MibTableRow
lgs2624cPortConfigurationEntry = _Lgs2624cPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 1, 1)
)
lgs2624cPortConfigurationEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cPortConfPort"),
)
if mibBuilder.loadTexts:
    lgs2624cPortConfigurationEntry.setStatus("current")


class _Lgs2624cPortConfPort_Type(Integer32):
    """Custom type lgs2624cPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cPortConfPort_Type.__name__ = "Integer32"
_Lgs2624cPortConfPort_Object = MibTableColumn
lgs2624cPortConfPort = _Lgs2624cPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 1, 1, 1),
    _Lgs2624cPortConfPort_Type()
)
lgs2624cPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cPortConfPort.setStatus("current")


class _Lgs2624cPortConfPortMedia_Type(DisplayString):
    """Custom type lgs2624cPortConfPortMedia based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_Lgs2624cPortConfPortMedia_Type.__name__ = "DisplayString"
_Lgs2624cPortConfPortMedia_Object = MibTableColumn
lgs2624cPortConfPortMedia = _Lgs2624cPortConfPortMedia_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 1, 1, 2),
    _Lgs2624cPortConfPortMedia_Type()
)
lgs2624cPortConfPortMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortConfPortMedia.setStatus("current")


class _Lgs2624cPortConfLink_Type(DisplayString):
    """Custom type lgs2624cPortConfLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_Lgs2624cPortConfLink_Type.__name__ = "DisplayString"
_Lgs2624cPortConfLink_Object = MibTableColumn
lgs2624cPortConfLink = _Lgs2624cPortConfLink_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 1, 1, 3),
    _Lgs2624cPortConfLink_Type()
)
lgs2624cPortConfLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortConfLink.setStatus("current")


class _Lgs2624cPortConfCurrentSpeed_Type(DisplayString):
    """Custom type lgs2624cPortConfCurrentSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 12),
    )


_Lgs2624cPortConfCurrentSpeed_Type.__name__ = "DisplayString"
_Lgs2624cPortConfCurrentSpeed_Object = MibTableColumn
lgs2624cPortConfCurrentSpeed = _Lgs2624cPortConfCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 1, 1, 4),
    _Lgs2624cPortConfCurrentSpeed_Type()
)
lgs2624cPortConfCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortConfCurrentSpeed.setStatus("current")


class _Lgs2624cPortConfSpeed_Type(Integer32):
    """Custom type lgs2624cPortConfSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Lgs2624cPortConfSpeed_Type.__name__ = "Integer32"
_Lgs2624cPortConfSpeed_Object = MibTableColumn
lgs2624cPortConfSpeed = _Lgs2624cPortConfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 1, 1, 5),
    _Lgs2624cPortConfSpeed_Type()
)
lgs2624cPortConfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortConfSpeed.setStatus("current")


class _Lgs2624cPortConfCurrentFlowControlRx_Type(Integer32):
    """Custom type lgs2624cPortConfCurrentFlowControlRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cPortConfCurrentFlowControlRx_Type.__name__ = "Integer32"
_Lgs2624cPortConfCurrentFlowControlRx_Object = MibTableColumn
lgs2624cPortConfCurrentFlowControlRx = _Lgs2624cPortConfCurrentFlowControlRx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 1, 1, 6),
    _Lgs2624cPortConfCurrentFlowControlRx_Type()
)
lgs2624cPortConfCurrentFlowControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortConfCurrentFlowControlRx.setStatus("current")


class _Lgs2624cPortConfCurrentFlowControlTx_Type(Integer32):
    """Custom type lgs2624cPortConfCurrentFlowControlTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cPortConfCurrentFlowControlTx_Type.__name__ = "Integer32"
_Lgs2624cPortConfCurrentFlowControlTx_Object = MibTableColumn
lgs2624cPortConfCurrentFlowControlTx = _Lgs2624cPortConfCurrentFlowControlTx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 1, 1, 7),
    _Lgs2624cPortConfCurrentFlowControlTx_Type()
)
lgs2624cPortConfCurrentFlowControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortConfCurrentFlowControlTx.setStatus("current")


class _Lgs2624cPortConfFlowControl_Type(Integer32):
    """Custom type lgs2624cPortConfFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cPortConfFlowControl_Type.__name__ = "Integer32"
_Lgs2624cPortConfFlowControl_Object = MibTableColumn
lgs2624cPortConfFlowControl = _Lgs2624cPortConfFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 1, 1, 8),
    _Lgs2624cPortConfFlowControl_Type()
)
lgs2624cPortConfFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortConfFlowControl.setStatus("current")


class _Lgs2624cPortConfMaxFrameSize_Type(Integer32):
    """Custom type lgs2624cPortConfMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_Lgs2624cPortConfMaxFrameSize_Type.__name__ = "Integer32"
_Lgs2624cPortConfMaxFrameSize_Object = MibTableColumn
lgs2624cPortConfMaxFrameSize = _Lgs2624cPortConfMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 1, 1, 9),
    _Lgs2624cPortConfMaxFrameSize_Type()
)
lgs2624cPortConfMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortConfMaxFrameSize.setStatus("current")
_Lgs2624cPortConfExcessiveCollisionMode_Type = DisplayString
_Lgs2624cPortConfExcessiveCollisionMode_Object = MibTableColumn
lgs2624cPortConfExcessiveCollisionMode = _Lgs2624cPortConfExcessiveCollisionMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 1, 1, 10),
    _Lgs2624cPortConfExcessiveCollisionMode_Type()
)
lgs2624cPortConfExcessiveCollisionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortConfExcessiveCollisionMode.setStatus("current")
_Lgs2624cPortConfPowerControl_Type = DisplayString
_Lgs2624cPortConfPowerControl_Object = MibTableColumn
lgs2624cPortConfPowerControl = _Lgs2624cPortConfPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 1, 1, 11),
    _Lgs2624cPortConfPowerControl_Type()
)
lgs2624cPortConfPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortConfPowerControl.setStatus("current")
_Lgs2624cPortConfDescription_Type = DisplayString
_Lgs2624cPortConfDescription_Object = MibTableColumn
lgs2624cPortConfDescription = _Lgs2624cPortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 1, 1, 12),
    _Lgs2624cPortConfDescription_Type()
)
lgs2624cPortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortConfDescription.setStatus("current")
_Lgs2624cPortTrafficStatisticsTable_Object = MibTable
lgs2624cPortTrafficStatisticsTable = _Lgs2624cPortTrafficStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2)
)
if mibBuilder.loadTexts:
    lgs2624cPortTrafficStatisticsTable.setStatus("current")
_Lgs2624cPortTrafficStatisticsEntry_Object = MibTableRow
lgs2624cPortTrafficStatisticsEntry = _Lgs2624cPortTrafficStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1)
)
lgs2624cPortTrafficStatisticsEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cPortTrafficStatisticsPort"),
)
if mibBuilder.loadTexts:
    lgs2624cPortTrafficStatisticsEntry.setStatus("current")


class _Lgs2624cPortTrafficStatisticsPort_Type(Integer32):
    """Custom type lgs2624cPortTrafficStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cPortTrafficStatisticsPort_Type.__name__ = "Integer32"
_Lgs2624cPortTrafficStatisticsPort_Object = MibTableColumn
lgs2624cPortTrafficStatisticsPort = _Lgs2624cPortTrafficStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 1),
    _Lgs2624cPortTrafficStatisticsPort_Type()
)
lgs2624cPortTrafficStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficStatisticsPort.setStatus("current")


class _Lgs2624cPortTrafficStatisticsClear_Type(Integer32):
    """Custom type lgs2624cPortTrafficStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cPortTrafficStatisticsClear_Type.__name__ = "Integer32"
_Lgs2624cPortTrafficStatisticsClear_Object = MibTableColumn
lgs2624cPortTrafficStatisticsClear = _Lgs2624cPortTrafficStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 2),
    _Lgs2624cPortTrafficStatisticsClear_Type()
)
lgs2624cPortTrafficStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficStatisticsClear.setStatus("current")
_Lgs2624cPortTrafficRxPackets_Type = Counter64
_Lgs2624cPortTrafficRxPackets_Object = MibTableColumn
lgs2624cPortTrafficRxPackets = _Lgs2624cPortTrafficRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 3),
    _Lgs2624cPortTrafficRxPackets_Type()
)
lgs2624cPortTrafficRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxPackets.setStatus("current")
_Lgs2624cPortTrafficRxOctets_Type = Counter64
_Lgs2624cPortTrafficRxOctets_Object = MibTableColumn
lgs2624cPortTrafficRxOctets = _Lgs2624cPortTrafficRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 4),
    _Lgs2624cPortTrafficRxOctets_Type()
)
lgs2624cPortTrafficRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxOctets.setStatus("current")
_Lgs2624cPortTrafficRxUnicast_Type = Counter64
_Lgs2624cPortTrafficRxUnicast_Object = MibTableColumn
lgs2624cPortTrafficRxUnicast = _Lgs2624cPortTrafficRxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 5),
    _Lgs2624cPortTrafficRxUnicast_Type()
)
lgs2624cPortTrafficRxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxUnicast.setStatus("current")
_Lgs2624cPortTrafficRxMulticast_Type = Counter64
_Lgs2624cPortTrafficRxMulticast_Object = MibTableColumn
lgs2624cPortTrafficRxMulticast = _Lgs2624cPortTrafficRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 6),
    _Lgs2624cPortTrafficRxMulticast_Type()
)
lgs2624cPortTrafficRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxMulticast.setStatus("current")
_Lgs2624cPortTrafficRxBroadcast_Type = Counter64
_Lgs2624cPortTrafficRxBroadcast_Object = MibTableColumn
lgs2624cPortTrafficRxBroadcast = _Lgs2624cPortTrafficRxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 7),
    _Lgs2624cPortTrafficRxBroadcast_Type()
)
lgs2624cPortTrafficRxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxBroadcast.setStatus("current")
_Lgs2624cPortTrafficRxPause_Type = Counter64
_Lgs2624cPortTrafficRxPause_Object = MibTableColumn
lgs2624cPortTrafficRxPause = _Lgs2624cPortTrafficRxPause_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 8),
    _Lgs2624cPortTrafficRxPause_Type()
)
lgs2624cPortTrafficRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxPause.setStatus("current")
_Lgs2624cPortTrafficRx64Bytes_Type = Counter64
_Lgs2624cPortTrafficRx64Bytes_Object = MibTableColumn
lgs2624cPortTrafficRx64Bytes = _Lgs2624cPortTrafficRx64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 9),
    _Lgs2624cPortTrafficRx64Bytes_Type()
)
lgs2624cPortTrafficRx64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRx64Bytes.setStatus("current")
_Lgs2624cPortTrafficRx65to127Bytes_Type = Counter64
_Lgs2624cPortTrafficRx65to127Bytes_Object = MibTableColumn
lgs2624cPortTrafficRx65to127Bytes = _Lgs2624cPortTrafficRx65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 10),
    _Lgs2624cPortTrafficRx65to127Bytes_Type()
)
lgs2624cPortTrafficRx65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRx65to127Bytes.setStatus("current")
_Lgs2624cPortTrafficRx128to255Bytes_Type = Counter64
_Lgs2624cPortTrafficRx128to255Bytes_Object = MibTableColumn
lgs2624cPortTrafficRx128to255Bytes = _Lgs2624cPortTrafficRx128to255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 11),
    _Lgs2624cPortTrafficRx128to255Bytes_Type()
)
lgs2624cPortTrafficRx128to255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRx128to255Bytes.setStatus("current")
_Lgs2624cPortTrafficRx256to511Bytes_Type = Counter64
_Lgs2624cPortTrafficRx256to511Bytes_Object = MibTableColumn
lgs2624cPortTrafficRx256to511Bytes = _Lgs2624cPortTrafficRx256to511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 12),
    _Lgs2624cPortTrafficRx256to511Bytes_Type()
)
lgs2624cPortTrafficRx256to511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRx256to511Bytes.setStatus("current")
_Lgs2624cPortTrafficRx512to1023Bytes_Type = Counter64
_Lgs2624cPortTrafficRx512to1023Bytes_Object = MibTableColumn
lgs2624cPortTrafficRx512to1023Bytes = _Lgs2624cPortTrafficRx512to1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 13),
    _Lgs2624cPortTrafficRx512to1023Bytes_Type()
)
lgs2624cPortTrafficRx512to1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRx512to1023Bytes.setStatus("current")
_Lgs2624cPortTrafficRx1024to1526Bytes_Type = Counter64
_Lgs2624cPortTrafficRx1024to1526Bytes_Object = MibTableColumn
lgs2624cPortTrafficRx1024to1526Bytes = _Lgs2624cPortTrafficRx1024to1526Bytes_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 14),
    _Lgs2624cPortTrafficRx1024to1526Bytes_Type()
)
lgs2624cPortTrafficRx1024to1526Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRx1024to1526Bytes.setStatus("current")
_Lgs2624cPortTrafficRxExceecd1527Bytes_Type = Counter64
_Lgs2624cPortTrafficRxExceecd1527Bytes_Object = MibTableColumn
lgs2624cPortTrafficRxExceecd1527Bytes = _Lgs2624cPortTrafficRxExceecd1527Bytes_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 15),
    _Lgs2624cPortTrafficRxExceecd1527Bytes_Type()
)
lgs2624cPortTrafficRxExceecd1527Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxExceecd1527Bytes.setStatus("current")
_Lgs2624cPortTrafficRxQ0_Type = Counter64
_Lgs2624cPortTrafficRxQ0_Object = MibTableColumn
lgs2624cPortTrafficRxQ0 = _Lgs2624cPortTrafficRxQ0_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 16),
    _Lgs2624cPortTrafficRxQ0_Type()
)
lgs2624cPortTrafficRxQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxQ0.setStatus("current")
_Lgs2624cPortTrafficRxQ1_Type = Counter64
_Lgs2624cPortTrafficRxQ1_Object = MibTableColumn
lgs2624cPortTrafficRxQ1 = _Lgs2624cPortTrafficRxQ1_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 17),
    _Lgs2624cPortTrafficRxQ1_Type()
)
lgs2624cPortTrafficRxQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxQ1.setStatus("current")
_Lgs2624cPortTrafficRxQ2_Type = Counter64
_Lgs2624cPortTrafficRxQ2_Object = MibTableColumn
lgs2624cPortTrafficRxQ2 = _Lgs2624cPortTrafficRxQ2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 18),
    _Lgs2624cPortTrafficRxQ2_Type()
)
lgs2624cPortTrafficRxQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxQ2.setStatus("current")
_Lgs2624cPortTrafficRxQ3_Type = Counter64
_Lgs2624cPortTrafficRxQ3_Object = MibTableColumn
lgs2624cPortTrafficRxQ3 = _Lgs2624cPortTrafficRxQ3_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 19),
    _Lgs2624cPortTrafficRxQ3_Type()
)
lgs2624cPortTrafficRxQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxQ3.setStatus("current")
_Lgs2624cPortTrafficRxQ4_Type = Counter64
_Lgs2624cPortTrafficRxQ4_Object = MibTableColumn
lgs2624cPortTrafficRxQ4 = _Lgs2624cPortTrafficRxQ4_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 20),
    _Lgs2624cPortTrafficRxQ4_Type()
)
lgs2624cPortTrafficRxQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxQ4.setStatus("current")
_Lgs2624cPortTrafficRxQ5_Type = Counter64
_Lgs2624cPortTrafficRxQ5_Object = MibTableColumn
lgs2624cPortTrafficRxQ5 = _Lgs2624cPortTrafficRxQ5_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 21),
    _Lgs2624cPortTrafficRxQ5_Type()
)
lgs2624cPortTrafficRxQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxQ5.setStatus("current")
_Lgs2624cPortTrafficRxQ6_Type = Counter64
_Lgs2624cPortTrafficRxQ6_Object = MibTableColumn
lgs2624cPortTrafficRxQ6 = _Lgs2624cPortTrafficRxQ6_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 22),
    _Lgs2624cPortTrafficRxQ6_Type()
)
lgs2624cPortTrafficRxQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxQ6.setStatus("current")
_Lgs2624cPortTrafficRxQ7_Type = Counter64
_Lgs2624cPortTrafficRxQ7_Object = MibTableColumn
lgs2624cPortTrafficRxQ7 = _Lgs2624cPortTrafficRxQ7_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 23),
    _Lgs2624cPortTrafficRxQ7_Type()
)
lgs2624cPortTrafficRxQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxQ7.setStatus("current")
_Lgs2624cPortTrafficRxDrops_Type = Counter64
_Lgs2624cPortTrafficRxDrops_Object = MibTableColumn
lgs2624cPortTrafficRxDrops = _Lgs2624cPortTrafficRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 24),
    _Lgs2624cPortTrafficRxDrops_Type()
)
lgs2624cPortTrafficRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxDrops.setStatus("current")
_Lgs2624cPortTrafficRxCRCorAlignment_Type = Counter64
_Lgs2624cPortTrafficRxCRCorAlignment_Object = MibTableColumn
lgs2624cPortTrafficRxCRCorAlignment = _Lgs2624cPortTrafficRxCRCorAlignment_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 25),
    _Lgs2624cPortTrafficRxCRCorAlignment_Type()
)
lgs2624cPortTrafficRxCRCorAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxCRCorAlignment.setStatus("current")
_Lgs2624cPortTrafficRxUndersize_Type = Counter64
_Lgs2624cPortTrafficRxUndersize_Object = MibTableColumn
lgs2624cPortTrafficRxUndersize = _Lgs2624cPortTrafficRxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 26),
    _Lgs2624cPortTrafficRxUndersize_Type()
)
lgs2624cPortTrafficRxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxUndersize.setStatus("current")
_Lgs2624cPortTrafficRxOversize_Type = Counter64
_Lgs2624cPortTrafficRxOversize_Object = MibTableColumn
lgs2624cPortTrafficRxOversize = _Lgs2624cPortTrafficRxOversize_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 27),
    _Lgs2624cPortTrafficRxOversize_Type()
)
lgs2624cPortTrafficRxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxOversize.setStatus("current")
_Lgs2624cPortTrafficRxFragments_Type = Counter64
_Lgs2624cPortTrafficRxFragments_Object = MibTableColumn
lgs2624cPortTrafficRxFragments = _Lgs2624cPortTrafficRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 28),
    _Lgs2624cPortTrafficRxFragments_Type()
)
lgs2624cPortTrafficRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxFragments.setStatus("current")
_Lgs2624cPortTrafficRxJabber_Type = Counter64
_Lgs2624cPortTrafficRxJabber_Object = MibTableColumn
lgs2624cPortTrafficRxJabber = _Lgs2624cPortTrafficRxJabber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 29),
    _Lgs2624cPortTrafficRxJabber_Type()
)
lgs2624cPortTrafficRxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxJabber.setStatus("current")
_Lgs2624cPortTrafficRxFiltered_Type = Counter64
_Lgs2624cPortTrafficRxFiltered_Object = MibTableColumn
lgs2624cPortTrafficRxFiltered = _Lgs2624cPortTrafficRxFiltered_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 30),
    _Lgs2624cPortTrafficRxFiltered_Type()
)
lgs2624cPortTrafficRxFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficRxFiltered.setStatus("current")
_Lgs2624cPortTrafficTxPackets_Type = Counter64
_Lgs2624cPortTrafficTxPackets_Object = MibTableColumn
lgs2624cPortTrafficTxPackets = _Lgs2624cPortTrafficTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 31),
    _Lgs2624cPortTrafficTxPackets_Type()
)
lgs2624cPortTrafficTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTxPackets.setStatus("current")
_Lgs2624cPortTrafficTxOctets_Type = Counter64
_Lgs2624cPortTrafficTxOctets_Object = MibTableColumn
lgs2624cPortTrafficTxOctets = _Lgs2624cPortTrafficTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 32),
    _Lgs2624cPortTrafficTxOctets_Type()
)
lgs2624cPortTrafficTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTxOctets.setStatus("current")
_Lgs2624cPortTrafficTxUnicast_Type = Counter64
_Lgs2624cPortTrafficTxUnicast_Object = MibTableColumn
lgs2624cPortTrafficTxUnicast = _Lgs2624cPortTrafficTxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 33),
    _Lgs2624cPortTrafficTxUnicast_Type()
)
lgs2624cPortTrafficTxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTxUnicast.setStatus("current")
_Lgs2624cPortTrafficTxMulticast_Type = Counter64
_Lgs2624cPortTrafficTxMulticast_Object = MibTableColumn
lgs2624cPortTrafficTxMulticast = _Lgs2624cPortTrafficTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 34),
    _Lgs2624cPortTrafficTxMulticast_Type()
)
lgs2624cPortTrafficTxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTxMulticast.setStatus("current")
_Lgs2624cPortTrafficTxBroadcast_Type = Counter64
_Lgs2624cPortTrafficTxBroadcast_Object = MibTableColumn
lgs2624cPortTrafficTxBroadcast = _Lgs2624cPortTrafficTxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 35),
    _Lgs2624cPortTrafficTxBroadcast_Type()
)
lgs2624cPortTrafficTxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTxBroadcast.setStatus("current")
_Lgs2624cPortTrafficTxPause_Type = Counter64
_Lgs2624cPortTrafficTxPause_Object = MibTableColumn
lgs2624cPortTrafficTxPause = _Lgs2624cPortTrafficTxPause_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 36),
    _Lgs2624cPortTrafficTxPause_Type()
)
lgs2624cPortTrafficTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTxPause.setStatus("current")
_Lgs2624cPortTrafficTx64Bytes_Type = Counter64
_Lgs2624cPortTrafficTx64Bytes_Object = MibTableColumn
lgs2624cPortTrafficTx64Bytes = _Lgs2624cPortTrafficTx64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 37),
    _Lgs2624cPortTrafficTx64Bytes_Type()
)
lgs2624cPortTrafficTx64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTx64Bytes.setStatus("current")
_Lgs2624cPortTrafficTx65to127Bytes_Type = Counter64
_Lgs2624cPortTrafficTx65to127Bytes_Object = MibTableColumn
lgs2624cPortTrafficTx65to127Bytes = _Lgs2624cPortTrafficTx65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 38),
    _Lgs2624cPortTrafficTx65to127Bytes_Type()
)
lgs2624cPortTrafficTx65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTx65to127Bytes.setStatus("current")
_Lgs2624cPortTrafficTx128to255Bytes_Type = Counter64
_Lgs2624cPortTrafficTx128to255Bytes_Object = MibTableColumn
lgs2624cPortTrafficTx128to255Bytes = _Lgs2624cPortTrafficTx128to255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 39),
    _Lgs2624cPortTrafficTx128to255Bytes_Type()
)
lgs2624cPortTrafficTx128to255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTx128to255Bytes.setStatus("current")
_Lgs2624cPortTrafficTx256to511Bytes_Type = Counter64
_Lgs2624cPortTrafficTx256to511Bytes_Object = MibTableColumn
lgs2624cPortTrafficTx256to511Bytes = _Lgs2624cPortTrafficTx256to511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 40),
    _Lgs2624cPortTrafficTx256to511Bytes_Type()
)
lgs2624cPortTrafficTx256to511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTx256to511Bytes.setStatus("current")
_Lgs2624cPortTrafficTx512to1023Bytes_Type = Counter64
_Lgs2624cPortTrafficTx512to1023Bytes_Object = MibTableColumn
lgs2624cPortTrafficTx512to1023Bytes = _Lgs2624cPortTrafficTx512to1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 41),
    _Lgs2624cPortTrafficTx512to1023Bytes_Type()
)
lgs2624cPortTrafficTx512to1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTx512to1023Bytes.setStatus("current")
_Lgs2624cPortTrafficTx1024to1526Bytes_Type = Counter64
_Lgs2624cPortTrafficTx1024to1526Bytes_Object = MibTableColumn
lgs2624cPortTrafficTx1024to1526Bytes = _Lgs2624cPortTrafficTx1024to1526Bytes_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 42),
    _Lgs2624cPortTrafficTx1024to1526Bytes_Type()
)
lgs2624cPortTrafficTx1024to1526Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTx1024to1526Bytes.setStatus("current")
_Lgs2624cPortTrafficTxExceecd1527Bytes_Type = Counter64
_Lgs2624cPortTrafficTxExceecd1527Bytes_Object = MibTableColumn
lgs2624cPortTrafficTxExceecd1527Bytes = _Lgs2624cPortTrafficTxExceecd1527Bytes_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 43),
    _Lgs2624cPortTrafficTxExceecd1527Bytes_Type()
)
lgs2624cPortTrafficTxExceecd1527Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTxExceecd1527Bytes.setStatus("current")
_Lgs2624cPortTrafficTxQ0_Type = Counter64
_Lgs2624cPortTrafficTxQ0_Object = MibTableColumn
lgs2624cPortTrafficTxQ0 = _Lgs2624cPortTrafficTxQ0_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 44),
    _Lgs2624cPortTrafficTxQ0_Type()
)
lgs2624cPortTrafficTxQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTxQ0.setStatus("current")
_Lgs2624cPortTrafficTxQ1_Type = Counter64
_Lgs2624cPortTrafficTxQ1_Object = MibTableColumn
lgs2624cPortTrafficTxQ1 = _Lgs2624cPortTrafficTxQ1_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 45),
    _Lgs2624cPortTrafficTxQ1_Type()
)
lgs2624cPortTrafficTxQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTxQ1.setStatus("current")
_Lgs2624cPortTrafficTxQ2_Type = Counter64
_Lgs2624cPortTrafficTxQ2_Object = MibTableColumn
lgs2624cPortTrafficTxQ2 = _Lgs2624cPortTrafficTxQ2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 46),
    _Lgs2624cPortTrafficTxQ2_Type()
)
lgs2624cPortTrafficTxQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTxQ2.setStatus("current")
_Lgs2624cPortTrafficTxQ3_Type = Counter64
_Lgs2624cPortTrafficTxQ3_Object = MibTableColumn
lgs2624cPortTrafficTxQ3 = _Lgs2624cPortTrafficTxQ3_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 47),
    _Lgs2624cPortTrafficTxQ3_Type()
)
lgs2624cPortTrafficTxQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTxQ3.setStatus("current")
_Lgs2624cPortTrafficTxQ4_Type = Counter64
_Lgs2624cPortTrafficTxQ4_Object = MibTableColumn
lgs2624cPortTrafficTxQ4 = _Lgs2624cPortTrafficTxQ4_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 48),
    _Lgs2624cPortTrafficTxQ4_Type()
)
lgs2624cPortTrafficTxQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTxQ4.setStatus("current")
_Lgs2624cPortTrafficTxQ5_Type = Counter64
_Lgs2624cPortTrafficTxQ5_Object = MibTableColumn
lgs2624cPortTrafficTxQ5 = _Lgs2624cPortTrafficTxQ5_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 49),
    _Lgs2624cPortTrafficTxQ5_Type()
)
lgs2624cPortTrafficTxQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTxQ5.setStatus("current")
_Lgs2624cPortTrafficTxQ6_Type = Counter64
_Lgs2624cPortTrafficTxQ6_Object = MibTableColumn
lgs2624cPortTrafficTxQ6 = _Lgs2624cPortTrafficTxQ6_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 50),
    _Lgs2624cPortTrafficTxQ6_Type()
)
lgs2624cPortTrafficTxQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTxQ6.setStatus("current")
_Lgs2624cPortTrafficTxQ7_Type = Counter64
_Lgs2624cPortTrafficTxQ7_Object = MibTableColumn
lgs2624cPortTrafficTxQ7 = _Lgs2624cPortTrafficTxQ7_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 51),
    _Lgs2624cPortTrafficTxQ7_Type()
)
lgs2624cPortTrafficTxQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTxQ7.setStatus("current")
_Lgs2624cPortTrafficTxDrops_Type = Counter64
_Lgs2624cPortTrafficTxDrops_Object = MibTableColumn
lgs2624cPortTrafficTxDrops = _Lgs2624cPortTrafficTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 52),
    _Lgs2624cPortTrafficTxDrops_Type()
)
lgs2624cPortTrafficTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTxDrops.setStatus("current")
_Lgs2624cPortTrafficTxLateOrExcColl_Type = Counter64
_Lgs2624cPortTrafficTxLateOrExcColl_Object = MibTableColumn
lgs2624cPortTrafficTxLateOrExcColl = _Lgs2624cPortTrafficTxLateOrExcColl_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 2, 1, 53),
    _Lgs2624cPortTrafficTxLateOrExcColl_Type()
)
lgs2624cPortTrafficTxLateOrExcColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortTrafficTxLateOrExcColl.setStatus("current")
_Lgs2624cPortQoSStatistics_ObjectIdentity = ObjectIdentity
lgs2624cPortQoSStatistics = _Lgs2624cPortQoSStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3)
)


class _Lgs2624cPortQoSStatisticsClear_Type(Integer32):
    """Custom type lgs2624cPortQoSStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cPortQoSStatisticsClear_Type.__name__ = "Integer32"
_Lgs2624cPortQoSStatisticsClear_Object = MibScalar
lgs2624cPortQoSStatisticsClear = _Lgs2624cPortQoSStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 1),
    _Lgs2624cPortQoSStatisticsClear_Type()
)
lgs2624cPortQoSStatisticsClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortQoSStatisticsClear.setStatus("current")
_Lgs2624cPortQoSStatisticsTable_Object = MibTable
lgs2624cPortQoSStatisticsTable = _Lgs2624cPortQoSStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    lgs2624cPortQoSStatisticsTable.setStatus("current")
_Lgs2624cPortQoSStatisticsEntry_Object = MibTableRow
lgs2624cPortQoSStatisticsEntry = _Lgs2624cPortQoSStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2, 1)
)
lgs2624cPortQoSStatisticsEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cPortQoSStatisticsPort"),
)
if mibBuilder.loadTexts:
    lgs2624cPortQoSStatisticsEntry.setStatus("current")


class _Lgs2624cPortQoSStatisticsPort_Type(Integer32):
    """Custom type lgs2624cPortQoSStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cPortQoSStatisticsPort_Type.__name__ = "Integer32"
_Lgs2624cPortQoSStatisticsPort_Object = MibTableColumn
lgs2624cPortQoSStatisticsPort = _Lgs2624cPortQoSStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2, 1, 1),
    _Lgs2624cPortQoSStatisticsPort_Type()
)
lgs2624cPortQoSStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cPortQoSStatisticsPort.setStatus("current")
_Lgs2624cPortQoSQ0Rx_Type = Counter64
_Lgs2624cPortQoSQ0Rx_Object = MibTableColumn
lgs2624cPortQoSQ0Rx = _Lgs2624cPortQoSQ0Rx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2, 1, 2),
    _Lgs2624cPortQoSQ0Rx_Type()
)
lgs2624cPortQoSQ0Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortQoSQ0Rx.setStatus("current")
_Lgs2624cPortQoSQ0Tx_Type = Counter64
_Lgs2624cPortQoSQ0Tx_Object = MibTableColumn
lgs2624cPortQoSQ0Tx = _Lgs2624cPortQoSQ0Tx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2, 1, 3),
    _Lgs2624cPortQoSQ0Tx_Type()
)
lgs2624cPortQoSQ0Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortQoSQ0Tx.setStatus("current")
_Lgs2624cPortQoSQ1Rx_Type = Counter64
_Lgs2624cPortQoSQ1Rx_Object = MibTableColumn
lgs2624cPortQoSQ1Rx = _Lgs2624cPortQoSQ1Rx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2, 1, 4),
    _Lgs2624cPortQoSQ1Rx_Type()
)
lgs2624cPortQoSQ1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortQoSQ1Rx.setStatus("current")
_Lgs2624cPortQoSQ1Tx_Type = Counter64
_Lgs2624cPortQoSQ1Tx_Object = MibTableColumn
lgs2624cPortQoSQ1Tx = _Lgs2624cPortQoSQ1Tx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2, 1, 5),
    _Lgs2624cPortQoSQ1Tx_Type()
)
lgs2624cPortQoSQ1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortQoSQ1Tx.setStatus("current")
_Lgs2624cPortQoSQ2Rx_Type = Counter64
_Lgs2624cPortQoSQ2Rx_Object = MibTableColumn
lgs2624cPortQoSQ2Rx = _Lgs2624cPortQoSQ2Rx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2, 1, 6),
    _Lgs2624cPortQoSQ2Rx_Type()
)
lgs2624cPortQoSQ2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortQoSQ2Rx.setStatus("current")
_Lgs2624cPortQoSQ2Tx_Type = Counter64
_Lgs2624cPortQoSQ2Tx_Object = MibTableColumn
lgs2624cPortQoSQ2Tx = _Lgs2624cPortQoSQ2Tx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2, 1, 7),
    _Lgs2624cPortQoSQ2Tx_Type()
)
lgs2624cPortQoSQ2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortQoSQ2Tx.setStatus("current")
_Lgs2624cPortQoSQ3Rx_Type = Counter64
_Lgs2624cPortQoSQ3Rx_Object = MibTableColumn
lgs2624cPortQoSQ3Rx = _Lgs2624cPortQoSQ3Rx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2, 1, 8),
    _Lgs2624cPortQoSQ3Rx_Type()
)
lgs2624cPortQoSQ3Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortQoSQ3Rx.setStatus("current")
_Lgs2624cPortQoSQ3Tx_Type = Counter64
_Lgs2624cPortQoSQ3Tx_Object = MibTableColumn
lgs2624cPortQoSQ3Tx = _Lgs2624cPortQoSQ3Tx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2, 1, 9),
    _Lgs2624cPortQoSQ3Tx_Type()
)
lgs2624cPortQoSQ3Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortQoSQ3Tx.setStatus("current")
_Lgs2624cPortQoSQ4Rx_Type = Counter64
_Lgs2624cPortQoSQ4Rx_Object = MibTableColumn
lgs2624cPortQoSQ4Rx = _Lgs2624cPortQoSQ4Rx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2, 1, 10),
    _Lgs2624cPortQoSQ4Rx_Type()
)
lgs2624cPortQoSQ4Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortQoSQ4Rx.setStatus("current")
_Lgs2624cPortQoSQ4Tx_Type = Counter64
_Lgs2624cPortQoSQ4Tx_Object = MibTableColumn
lgs2624cPortQoSQ4Tx = _Lgs2624cPortQoSQ4Tx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2, 1, 11),
    _Lgs2624cPortQoSQ4Tx_Type()
)
lgs2624cPortQoSQ4Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortQoSQ4Tx.setStatus("current")
_Lgs2624cPortQoSQ5Rx_Type = Counter64
_Lgs2624cPortQoSQ5Rx_Object = MibTableColumn
lgs2624cPortQoSQ5Rx = _Lgs2624cPortQoSQ5Rx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2, 1, 12),
    _Lgs2624cPortQoSQ5Rx_Type()
)
lgs2624cPortQoSQ5Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortQoSQ5Rx.setStatus("current")
_Lgs2624cPortQoSQ5Tx_Type = Counter64
_Lgs2624cPortQoSQ5Tx_Object = MibTableColumn
lgs2624cPortQoSQ5Tx = _Lgs2624cPortQoSQ5Tx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2, 1, 13),
    _Lgs2624cPortQoSQ5Tx_Type()
)
lgs2624cPortQoSQ5Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortQoSQ5Tx.setStatus("current")
_Lgs2624cPortQoSQ6Rx_Type = Counter64
_Lgs2624cPortQoSQ6Rx_Object = MibTableColumn
lgs2624cPortQoSQ6Rx = _Lgs2624cPortQoSQ6Rx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2, 1, 14),
    _Lgs2624cPortQoSQ6Rx_Type()
)
lgs2624cPortQoSQ6Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortQoSQ6Rx.setStatus("current")
_Lgs2624cPortQoSQ6Tx_Type = Counter64
_Lgs2624cPortQoSQ6Tx_Object = MibTableColumn
lgs2624cPortQoSQ6Tx = _Lgs2624cPortQoSQ6Tx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2, 1, 15),
    _Lgs2624cPortQoSQ6Tx_Type()
)
lgs2624cPortQoSQ6Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortQoSQ6Tx.setStatus("current")
_Lgs2624cPortQoSQ7Rx_Type = Counter64
_Lgs2624cPortQoSQ7Rx_Object = MibTableColumn
lgs2624cPortQoSQ7Rx = _Lgs2624cPortQoSQ7Rx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2, 1, 16),
    _Lgs2624cPortQoSQ7Rx_Type()
)
lgs2624cPortQoSQ7Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortQoSQ7Rx.setStatus("current")
_Lgs2624cPortQoSQ7Tx_Type = Counter64
_Lgs2624cPortQoSQ7Tx_Object = MibTableColumn
lgs2624cPortQoSQ7Tx = _Lgs2624cPortQoSQ7Tx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 3, 2, 1, 17),
    _Lgs2624cPortQoSQ7Tx_Type()
)
lgs2624cPortQoSQ7Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortQoSQ7Tx.setStatus("current")
_Lgs2624cSFPInfoTable_Object = MibTable
lgs2624cSFPInfoTable = _Lgs2624cSFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4)
)
if mibBuilder.loadTexts:
    lgs2624cSFPInfoTable.setStatus("current")
_Lgs2624cSFPInfoEntry_Object = MibTableRow
lgs2624cSFPInfoEntry = _Lgs2624cSFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4, 1)
)
lgs2624cSFPInfoEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cSFPInfoIndex"),
)
if mibBuilder.loadTexts:
    lgs2624cSFPInfoEntry.setStatus("current")


class _Lgs2624cSFPInfoIndex_Type(Integer32):
    """Custom type lgs2624cSFPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cSFPInfoIndex_Type.__name__ = "Integer32"
_Lgs2624cSFPInfoIndex_Object = MibTableColumn
lgs2624cSFPInfoIndex = _Lgs2624cSFPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4, 1, 1),
    _Lgs2624cSFPInfoIndex_Type()
)
lgs2624cSFPInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cSFPInfoIndex.setStatus("current")
_Lgs2624cSFPInfoPort_Type = DisplayString
_Lgs2624cSFPInfoPort_Object = MibTableColumn
lgs2624cSFPInfoPort = _Lgs2624cSFPInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4, 1, 2),
    _Lgs2624cSFPInfoPort_Type()
)
lgs2624cSFPInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSFPInfoPort.setStatus("current")
_Lgs2624cSFPConnectorType_Type = DisplayString
_Lgs2624cSFPConnectorType_Object = MibTableColumn
lgs2624cSFPConnectorType = _Lgs2624cSFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4, 1, 3),
    _Lgs2624cSFPConnectorType_Type()
)
lgs2624cSFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSFPConnectorType.setStatus("current")
_Lgs2624cSFPFiberType_Type = DisplayString
_Lgs2624cSFPFiberType_Object = MibTableColumn
lgs2624cSFPFiberType = _Lgs2624cSFPFiberType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4, 1, 4),
    _Lgs2624cSFPFiberType_Type()
)
lgs2624cSFPFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSFPFiberType.setStatus("current")
_Lgs2624cSFPTxCentralWavelength_Type = DisplayString
_Lgs2624cSFPTxCentralWavelength_Object = MibTableColumn
lgs2624cSFPTxCentralWavelength = _Lgs2624cSFPTxCentralWavelength_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4, 1, 5),
    _Lgs2624cSFPTxCentralWavelength_Type()
)
lgs2624cSFPTxCentralWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSFPTxCentralWavelength.setStatus("current")
_Lgs2624cSFPBaudRate_Type = DisplayString
_Lgs2624cSFPBaudRate_Object = MibTableColumn
lgs2624cSFPBaudRate = _Lgs2624cSFPBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4, 1, 6),
    _Lgs2624cSFPBaudRate_Type()
)
lgs2624cSFPBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSFPBaudRate.setStatus("current")
_Lgs2624cSFPVendorOUI_Type = DisplayString
_Lgs2624cSFPVendorOUI_Object = MibTableColumn
lgs2624cSFPVendorOUI = _Lgs2624cSFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4, 1, 7),
    _Lgs2624cSFPVendorOUI_Type()
)
lgs2624cSFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSFPVendorOUI.setStatus("current")
_Lgs2624cSFPVendorName_Type = DisplayString
_Lgs2624cSFPVendorName_Object = MibTableColumn
lgs2624cSFPVendorName = _Lgs2624cSFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4, 1, 8),
    _Lgs2624cSFPVendorName_Type()
)
lgs2624cSFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSFPVendorName.setStatus("current")
_Lgs2624cSFPVendorPN_Type = DisplayString
_Lgs2624cSFPVendorPN_Object = MibTableColumn
lgs2624cSFPVendorPN = _Lgs2624cSFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4, 1, 9),
    _Lgs2624cSFPVendorPN_Type()
)
lgs2624cSFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSFPVendorPN.setStatus("current")
_Lgs2624cSFPVendorRev_Type = DisplayString
_Lgs2624cSFPVendorRev_Object = MibTableColumn
lgs2624cSFPVendorRev = _Lgs2624cSFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4, 1, 10),
    _Lgs2624cSFPVendorRev_Type()
)
lgs2624cSFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSFPVendorRev.setStatus("current")
_Lgs2624cSFPVendorSN_Type = DisplayString
_Lgs2624cSFPVendorSN_Object = MibTableColumn
lgs2624cSFPVendorSN = _Lgs2624cSFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4, 1, 11),
    _Lgs2624cSFPVendorSN_Type()
)
lgs2624cSFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSFPVendorSN.setStatus("current")
_Lgs2624cSFPDateCode_Type = DisplayString
_Lgs2624cSFPDateCode_Object = MibTableColumn
lgs2624cSFPDateCode = _Lgs2624cSFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4, 1, 12),
    _Lgs2624cSFPDateCode_Type()
)
lgs2624cSFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSFPDateCode.setStatus("current")
_Lgs2624cSFPTemperature_Type = DisplayString
_Lgs2624cSFPTemperature_Object = MibTableColumn
lgs2624cSFPTemperature = _Lgs2624cSFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4, 1, 13),
    _Lgs2624cSFPTemperature_Type()
)
lgs2624cSFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSFPTemperature.setStatus("current")
_Lgs2624cSFPVcc_Type = DisplayString
_Lgs2624cSFPVcc_Object = MibTableColumn
lgs2624cSFPVcc = _Lgs2624cSFPVcc_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4, 1, 14),
    _Lgs2624cSFPVcc_Type()
)
lgs2624cSFPVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSFPVcc.setStatus("current")
_Lgs2624cSFPMon1Bias_Type = DisplayString
_Lgs2624cSFPMon1Bias_Object = MibTableColumn
lgs2624cSFPMon1Bias = _Lgs2624cSFPMon1Bias_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4, 1, 15),
    _Lgs2624cSFPMon1Bias_Type()
)
lgs2624cSFPMon1Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSFPMon1Bias.setStatus("current")
_Lgs2624cSFPMon2TxPWR_Type = DisplayString
_Lgs2624cSFPMon2TxPWR_Object = MibTableColumn
lgs2624cSFPMon2TxPWR = _Lgs2624cSFPMon2TxPWR_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4, 1, 16),
    _Lgs2624cSFPMon2TxPWR_Type()
)
lgs2624cSFPMon2TxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSFPMon2TxPWR.setStatus("current")
_Lgs2624cSFPMon3RxPWR_Type = DisplayString
_Lgs2624cSFPMon3RxPWR_Object = MibTableColumn
lgs2624cSFPMon3RxPWR = _Lgs2624cSFPMon3RxPWR_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 4, 1, 17),
    _Lgs2624cSFPMon3RxPWR_Type()
)
lgs2624cSFPMon3RxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSFPMon3RxPWR.setStatus("current")
_Lgs2624cPortEEETable_Object = MibTable
lgs2624cPortEEETable = _Lgs2624cPortEEETable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 5)
)
if mibBuilder.loadTexts:
    lgs2624cPortEEETable.setStatus("current")
_Lgs2624cPortEEEEntry_Object = MibTableRow
lgs2624cPortEEEEntry = _Lgs2624cPortEEEEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 5, 1)
)
lgs2624cPortEEEEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cPortEEEPort"),
)
if mibBuilder.loadTexts:
    lgs2624cPortEEEEntry.setStatus("current")


class _Lgs2624cPortEEEPort_Type(Integer32):
    """Custom type lgs2624cPortEEEPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cPortEEEPort_Type.__name__ = "Integer32"
_Lgs2624cPortEEEPort_Object = MibTableColumn
lgs2624cPortEEEPort = _Lgs2624cPortEEEPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 5, 1, 1),
    _Lgs2624cPortEEEPort_Type()
)
lgs2624cPortEEEPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cPortEEEPort.setStatus("current")


class _Lgs2624cPortEEEMode_Type(Integer32):
    """Custom type lgs2624cPortEEEMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cPortEEEMode_Type.__name__ = "Integer32"
_Lgs2624cPortEEEMode_Object = MibTableColumn
lgs2624cPortEEEMode = _Lgs2624cPortEEEMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 5, 1, 2),
    _Lgs2624cPortEEEMode_Type()
)
lgs2624cPortEEEMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortEEEMode.setStatus("current")


class _Lgs2624cPortEEEUrgentQueue1_Type(Integer32):
    """Custom type lgs2624cPortEEEUrgentQueue1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cPortEEEUrgentQueue1_Type.__name__ = "Integer32"
_Lgs2624cPortEEEUrgentQueue1_Object = MibTableColumn
lgs2624cPortEEEUrgentQueue1 = _Lgs2624cPortEEEUrgentQueue1_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 5, 1, 3),
    _Lgs2624cPortEEEUrgentQueue1_Type()
)
lgs2624cPortEEEUrgentQueue1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortEEEUrgentQueue1.setStatus("current")


class _Lgs2624cPortEEEUrgentQueue2_Type(Integer32):
    """Custom type lgs2624cPortEEEUrgentQueue2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cPortEEEUrgentQueue2_Type.__name__ = "Integer32"
_Lgs2624cPortEEEUrgentQueue2_Object = MibTableColumn
lgs2624cPortEEEUrgentQueue2 = _Lgs2624cPortEEEUrgentQueue2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 5, 1, 4),
    _Lgs2624cPortEEEUrgentQueue2_Type()
)
lgs2624cPortEEEUrgentQueue2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortEEEUrgentQueue2.setStatus("current")


class _Lgs2624cPortEEEUrgentQueue3_Type(Integer32):
    """Custom type lgs2624cPortEEEUrgentQueue3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cPortEEEUrgentQueue3_Type.__name__ = "Integer32"
_Lgs2624cPortEEEUrgentQueue3_Object = MibTableColumn
lgs2624cPortEEEUrgentQueue3 = _Lgs2624cPortEEEUrgentQueue3_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 5, 1, 5),
    _Lgs2624cPortEEEUrgentQueue3_Type()
)
lgs2624cPortEEEUrgentQueue3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortEEEUrgentQueue3.setStatus("current")


class _Lgs2624cPortEEEUrgentQueue4_Type(Integer32):
    """Custom type lgs2624cPortEEEUrgentQueue4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cPortEEEUrgentQueue4_Type.__name__ = "Integer32"
_Lgs2624cPortEEEUrgentQueue4_Object = MibTableColumn
lgs2624cPortEEEUrgentQueue4 = _Lgs2624cPortEEEUrgentQueue4_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 5, 1, 6),
    _Lgs2624cPortEEEUrgentQueue4_Type()
)
lgs2624cPortEEEUrgentQueue4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortEEEUrgentQueue4.setStatus("current")


class _Lgs2624cPortEEEUrgentQueue5_Type(Integer32):
    """Custom type lgs2624cPortEEEUrgentQueue5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cPortEEEUrgentQueue5_Type.__name__ = "Integer32"
_Lgs2624cPortEEEUrgentQueue5_Object = MibTableColumn
lgs2624cPortEEEUrgentQueue5 = _Lgs2624cPortEEEUrgentQueue5_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 5, 1, 7),
    _Lgs2624cPortEEEUrgentQueue5_Type()
)
lgs2624cPortEEEUrgentQueue5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortEEEUrgentQueue5.setStatus("current")


class _Lgs2624cPortEEEUrgentQueue6_Type(Integer32):
    """Custom type lgs2624cPortEEEUrgentQueue6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cPortEEEUrgentQueue6_Type.__name__ = "Integer32"
_Lgs2624cPortEEEUrgentQueue6_Object = MibTableColumn
lgs2624cPortEEEUrgentQueue6 = _Lgs2624cPortEEEUrgentQueue6_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 5, 1, 8),
    _Lgs2624cPortEEEUrgentQueue6_Type()
)
lgs2624cPortEEEUrgentQueue6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortEEEUrgentQueue6.setStatus("current")


class _Lgs2624cPortEEEUrgentQueue7_Type(Integer32):
    """Custom type lgs2624cPortEEEUrgentQueue7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cPortEEEUrgentQueue7_Type.__name__ = "Integer32"
_Lgs2624cPortEEEUrgentQueue7_Object = MibTableColumn
lgs2624cPortEEEUrgentQueue7 = _Lgs2624cPortEEEUrgentQueue7_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 5, 1, 9),
    _Lgs2624cPortEEEUrgentQueue7_Type()
)
lgs2624cPortEEEUrgentQueue7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortEEEUrgentQueue7.setStatus("current")


class _Lgs2624cPortEEEUrgentQueue8_Type(Integer32):
    """Custom type lgs2624cPortEEEUrgentQueue8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cPortEEEUrgentQueue8_Type.__name__ = "Integer32"
_Lgs2624cPortEEEUrgentQueue8_Object = MibTableColumn
lgs2624cPortEEEUrgentQueue8 = _Lgs2624cPortEEEUrgentQueue8_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 1, 5, 1, 10),
    _Lgs2624cPortEEEUrgentQueue8_Type()
)
lgs2624cPortEEEUrgentQueue8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortEEEUrgentQueue8.setStatus("current")
_Lgs2624cVoiceVLAN_ObjectIdentity = ObjectIdentity
lgs2624cVoiceVLAN = _Lgs2624cVoiceVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2)
)
_Lgs2624cVoiceVLANConf_ObjectIdentity = ObjectIdentity
lgs2624cVoiceVLANConf = _Lgs2624cVoiceVLANConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 1)
)


class _Lgs2624cVoiceVLANMode_Type(Integer32):
    """Custom type lgs2624cVoiceVLANMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cVoiceVLANMode_Type.__name__ = "Integer32"
_Lgs2624cVoiceVLANMode_Object = MibScalar
lgs2624cVoiceVLANMode = _Lgs2624cVoiceVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 1, 1),
    _Lgs2624cVoiceVLANMode_Type()
)
lgs2624cVoiceVLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cVoiceVLANMode.setStatus("current")


class _Lgs2624cVoiceVLANVLANId_Type(Integer32):
    """Custom type lgs2624cVoiceVLANVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2624cVoiceVLANVLANId_Type.__name__ = "Integer32"
_Lgs2624cVoiceVLANVLANId_Object = MibScalar
lgs2624cVoiceVLANVLANId = _Lgs2624cVoiceVLANVLANId_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 1, 2),
    _Lgs2624cVoiceVLANVLANId_Type()
)
lgs2624cVoiceVLANVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cVoiceVLANVLANId.setStatus("current")


class _Lgs2624cVoiceVLANAgingTime_Type(Integer32):
    """Custom type lgs2624cVoiceVLANAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Lgs2624cVoiceVLANAgingTime_Type.__name__ = "Integer32"
_Lgs2624cVoiceVLANAgingTime_Object = MibScalar
lgs2624cVoiceVLANAgingTime = _Lgs2624cVoiceVLANAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 1, 3),
    _Lgs2624cVoiceVLANAgingTime_Type()
)
lgs2624cVoiceVLANAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cVoiceVLANAgingTime.setStatus("current")


class _Lgs2624cVoiceVLANTrafficClass_Type(Integer32):
    """Custom type lgs2624cVoiceVLANTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cVoiceVLANTrafficClass_Type.__name__ = "Integer32"
_Lgs2624cVoiceVLANTrafficClass_Object = MibScalar
lgs2624cVoiceVLANTrafficClass = _Lgs2624cVoiceVLANTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 1, 4),
    _Lgs2624cVoiceVLANTrafficClass_Type()
)
lgs2624cVoiceVLANTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cVoiceVLANTrafficClass.setStatus("current")
_Lgs2624cVoiceVLANPortTable_Object = MibTable
lgs2624cVoiceVLANPortTable = _Lgs2624cVoiceVLANPortTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    lgs2624cVoiceVLANPortTable.setStatus("current")
_Lgs2624cVoiceVLANPortEntry_Object = MibTableRow
lgs2624cVoiceVLANPortEntry = _Lgs2624cVoiceVLANPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 1, 5, 1)
)
lgs2624cVoiceVLANPortEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cVoiceVLANPort"),
)
if mibBuilder.loadTexts:
    lgs2624cVoiceVLANPortEntry.setStatus("current")


class _Lgs2624cVoiceVLANPort_Type(Integer32):
    """Custom type lgs2624cVoiceVLANPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cVoiceVLANPort_Type.__name__ = "Integer32"
_Lgs2624cVoiceVLANPort_Object = MibTableColumn
lgs2624cVoiceVLANPort = _Lgs2624cVoiceVLANPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 1, 5, 1, 1),
    _Lgs2624cVoiceVLANPort_Type()
)
lgs2624cVoiceVLANPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cVoiceVLANPort.setStatus("current")


class _Lgs2624cVoiceVLANPortMode_Type(Integer32):
    """Custom type lgs2624cVoiceVLANPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2624cVoiceVLANPortMode_Type.__name__ = "Integer32"
_Lgs2624cVoiceVLANPortMode_Object = MibTableColumn
lgs2624cVoiceVLANPortMode = _Lgs2624cVoiceVLANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 1, 5, 1, 2),
    _Lgs2624cVoiceVLANPortMode_Type()
)
lgs2624cVoiceVLANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cVoiceVLANPortMode.setStatus("current")


class _Lgs2624cVoiceVLANPortSecurity_Type(Integer32):
    """Custom type lgs2624cVoiceVLANPortSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cVoiceVLANPortSecurity_Type.__name__ = "Integer32"
_Lgs2624cVoiceVLANPortSecurity_Object = MibTableColumn
lgs2624cVoiceVLANPortSecurity = _Lgs2624cVoiceVLANPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 1, 5, 1, 3),
    _Lgs2624cVoiceVLANPortSecurity_Type()
)
lgs2624cVoiceVLANPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cVoiceVLANPortSecurity.setStatus("current")


class _Lgs2624cVoiceVLANPortDiscoveryProtocol_Type(Integer32):
    """Custom type lgs2624cVoiceVLANPortDiscoveryProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2624cVoiceVLANPortDiscoveryProtocol_Type.__name__ = "Integer32"
_Lgs2624cVoiceVLANPortDiscoveryProtocol_Object = MibTableColumn
lgs2624cVoiceVLANPortDiscoveryProtocol = _Lgs2624cVoiceVLANPortDiscoveryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 1, 5, 1, 4),
    _Lgs2624cVoiceVLANPortDiscoveryProtocol_Type()
)
lgs2624cVoiceVLANPortDiscoveryProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cVoiceVLANPortDiscoveryProtocol.setStatus("current")
_Lgs2624cVoiceVLANOUI_ObjectIdentity = ObjectIdentity
lgs2624cVoiceVLANOUI = _Lgs2624cVoiceVLANOUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 2)
)


class _Lgs2624cVoiceVLANOUICreate_Type(Integer32):
    """Custom type lgs2624cVoiceVLANOUICreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cVoiceVLANOUICreate_Type.__name__ = "Integer32"
_Lgs2624cVoiceVLANOUICreate_Object = MibScalar
lgs2624cVoiceVLANOUICreate = _Lgs2624cVoiceVLANOUICreate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 2, 1),
    _Lgs2624cVoiceVLANOUICreate_Type()
)
lgs2624cVoiceVLANOUICreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cVoiceVLANOUICreate.setStatus("current")
_Lgs2624cVoiceVLANOUITable_Object = MibTable
lgs2624cVoiceVLANOUITable = _Lgs2624cVoiceVLANOUITable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    lgs2624cVoiceVLANOUITable.setStatus("current")
_Lgs2624cVoiceVLANOUIEntry_Object = MibTableRow
lgs2624cVoiceVLANOUIEntry = _Lgs2624cVoiceVLANOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 2, 2, 1)
)
lgs2624cVoiceVLANOUIEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cVoiceVLANOUIIndex"),
)
if mibBuilder.loadTexts:
    lgs2624cVoiceVLANOUIEntry.setStatus("current")


class _Lgs2624cVoiceVLANOUIIndex_Type(Integer32):
    """Custom type lgs2624cVoiceVLANOUIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Lgs2624cVoiceVLANOUIIndex_Type.__name__ = "Integer32"
_Lgs2624cVoiceVLANOUIIndex_Object = MibTableColumn
lgs2624cVoiceVLANOUIIndex = _Lgs2624cVoiceVLANOUIIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 2, 2, 1, 1),
    _Lgs2624cVoiceVLANOUIIndex_Type()
)
lgs2624cVoiceVLANOUIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cVoiceVLANOUIIndex.setStatus("current")


class _Lgs2624cVoiceVLANTelephonyOUI_Type(OctetString):
    """Custom type lgs2624cVoiceVLANTelephonyOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Lgs2624cVoiceVLANTelephonyOUI_Type.__name__ = "OctetString"
_Lgs2624cVoiceVLANTelephonyOUI_Object = MibTableColumn
lgs2624cVoiceVLANTelephonyOUI = _Lgs2624cVoiceVLANTelephonyOUI_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 2, 2, 1, 2),
    _Lgs2624cVoiceVLANTelephonyOUI_Type()
)
lgs2624cVoiceVLANTelephonyOUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cVoiceVLANTelephonyOUI.setStatus("current")


class _Lgs2624cVoiceVLANDescription_Type(DisplayString):
    """Custom type lgs2624cVoiceVLANDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Lgs2624cVoiceVLANDescription_Type.__name__ = "DisplayString"
_Lgs2624cVoiceVLANDescription_Object = MibTableColumn
lgs2624cVoiceVLANDescription = _Lgs2624cVoiceVLANDescription_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 2, 2, 1, 3),
    _Lgs2624cVoiceVLANDescription_Type()
)
lgs2624cVoiceVLANDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cVoiceVLANDescription.setStatus("current")


class _Lgs2624cVoiceVLANOUIRowStatus_Type(Integer32):
    """Custom type lgs2624cVoiceVLANOUIRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Lgs2624cVoiceVLANOUIRowStatus_Type.__name__ = "Integer32"
_Lgs2624cVoiceVLANOUIRowStatus_Object = MibTableColumn
lgs2624cVoiceVLANOUIRowStatus = _Lgs2624cVoiceVLANOUIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 2, 2, 2, 1, 4),
    _Lgs2624cVoiceVLANOUIRowStatus_Type()
)
lgs2624cVoiceVLANOUIRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cVoiceVLANOUIRowStatus.setStatus("current")
_Lgs2624cGARP_ObjectIdentity = ObjectIdentity
lgs2624cGARP = _Lgs2624cGARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 3)
)
_Lgs2624cGARPConfTable_Object = MibTable
lgs2624cGARPConfTable = _Lgs2624cGARPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 3, 1)
)
if mibBuilder.loadTexts:
    lgs2624cGARPConfTable.setStatus("current")
_Lgs2624cGARPConfEntry_Object = MibTableRow
lgs2624cGARPConfEntry = _Lgs2624cGARPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 3, 1, 1)
)
lgs2624cGARPConfEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cGARPConfPort"),
)
if mibBuilder.loadTexts:
    lgs2624cGARPConfEntry.setStatus("current")


class _Lgs2624cGARPConfPort_Type(Integer32):
    """Custom type lgs2624cGARPConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cGARPConfPort_Type.__name__ = "Integer32"
_Lgs2624cGARPConfPort_Object = MibTableColumn
lgs2624cGARPConfPort = _Lgs2624cGARPConfPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 3, 1, 1, 1),
    _Lgs2624cGARPConfPort_Type()
)
lgs2624cGARPConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cGARPConfPort.setStatus("current")


class _Lgs2624cGARPJoinTimer_Type(Integer32):
    """Custom type lgs2624cGARPJoinTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_Lgs2624cGARPJoinTimer_Type.__name__ = "Integer32"
_Lgs2624cGARPJoinTimer_Object = MibTableColumn
lgs2624cGARPJoinTimer = _Lgs2624cGARPJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 3, 1, 1, 2),
    _Lgs2624cGARPJoinTimer_Type()
)
lgs2624cGARPJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cGARPJoinTimer.setStatus("current")


class _Lgs2624cGARPLeaveTimer_Type(Integer32):
    """Custom type lgs2624cGARPLeaveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 3000),
    )


_Lgs2624cGARPLeaveTimer_Type.__name__ = "Integer32"
_Lgs2624cGARPLeaveTimer_Object = MibTableColumn
lgs2624cGARPLeaveTimer = _Lgs2624cGARPLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 3, 1, 1, 3),
    _Lgs2624cGARPLeaveTimer_Type()
)
lgs2624cGARPLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cGARPLeaveTimer.setStatus("current")


class _Lgs2624cGARPLeaveAllTimer_Type(Integer32):
    """Custom type lgs2624cGARPLeaveAllTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 50000),
    )


_Lgs2624cGARPLeaveAllTimer_Type.__name__ = "Integer32"
_Lgs2624cGARPLeaveAllTimer_Object = MibTableColumn
lgs2624cGARPLeaveAllTimer = _Lgs2624cGARPLeaveAllTimer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 3, 1, 1, 4),
    _Lgs2624cGARPLeaveAllTimer_Type()
)
lgs2624cGARPLeaveAllTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cGARPLeaveAllTimer.setStatus("current")


class _Lgs2624cGARPApplicantion_Type(Integer32):
    """Custom type lgs2624cGARPApplicantion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cGARPApplicantion_Type.__name__ = "Integer32"
_Lgs2624cGARPApplicantion_Object = MibTableColumn
lgs2624cGARPApplicantion = _Lgs2624cGARPApplicantion_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 3, 1, 1, 5),
    _Lgs2624cGARPApplicantion_Type()
)
lgs2624cGARPApplicantion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cGARPApplicantion.setStatus("current")


class _Lgs2624cGARPAttributeType_Type(Integer32):
    """Custom type lgs2624cGARPAttributeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cGARPAttributeType_Type.__name__ = "Integer32"
_Lgs2624cGARPAttributeType_Object = MibTableColumn
lgs2624cGARPAttributeType = _Lgs2624cGARPAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 3, 1, 1, 6),
    _Lgs2624cGARPAttributeType_Type()
)
lgs2624cGARPAttributeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cGARPAttributeType.setStatus("current")


class _Lgs2624cGARPApplicant_Type(Integer32):
    """Custom type lgs2624cGARPApplicant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cGARPApplicant_Type.__name__ = "Integer32"
_Lgs2624cGARPApplicant_Object = MibTableColumn
lgs2624cGARPApplicant = _Lgs2624cGARPApplicant_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 3, 1, 1, 7),
    _Lgs2624cGARPApplicant_Type()
)
lgs2624cGARPApplicant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cGARPApplicant.setStatus("current")
_Lgs2624cGARPStatisticsTable_Object = MibTable
lgs2624cGARPStatisticsTable = _Lgs2624cGARPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 3, 2)
)
if mibBuilder.loadTexts:
    lgs2624cGARPStatisticsTable.setStatus("current")
_Lgs2624cGARPStatisticsEntry_Object = MibTableRow
lgs2624cGARPStatisticsEntry = _Lgs2624cGARPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 3, 2, 1)
)
lgs2624cGARPStatisticsEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cGARPStatisticsPort"),
)
if mibBuilder.loadTexts:
    lgs2624cGARPStatisticsEntry.setStatus("current")


class _Lgs2624cGARPStatisticsPort_Type(Integer32):
    """Custom type lgs2624cGARPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cGARPStatisticsPort_Type.__name__ = "Integer32"
_Lgs2624cGARPStatisticsPort_Object = MibTableColumn
lgs2624cGARPStatisticsPort = _Lgs2624cGARPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 3, 2, 1, 1),
    _Lgs2624cGARPStatisticsPort_Type()
)
lgs2624cGARPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cGARPStatisticsPort.setStatus("current")
_Lgs2624cGARPStatisticsPeerMAC_Type = DisplayString
_Lgs2624cGARPStatisticsPeerMAC_Object = MibTableColumn
lgs2624cGARPStatisticsPeerMAC = _Lgs2624cGARPStatisticsPeerMAC_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 3, 2, 1, 2),
    _Lgs2624cGARPStatisticsPeerMAC_Type()
)
lgs2624cGARPStatisticsPeerMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cGARPStatisticsPeerMAC.setStatus("current")
_Lgs2624cGARPStatisticsFailedCount_Type = Counter32
_Lgs2624cGARPStatisticsFailedCount_Object = MibTableColumn
lgs2624cGARPStatisticsFailedCount = _Lgs2624cGARPStatisticsFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 3, 2, 1, 3),
    _Lgs2624cGARPStatisticsFailedCount_Type()
)
lgs2624cGARPStatisticsFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cGARPStatisticsFailedCount.setStatus("current")
_Lgs2624cGVRP_ObjectIdentity = ObjectIdentity
lgs2624cGVRP = _Lgs2624cGVRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 4)
)
_Lgs2624cGVRPConf_ObjectIdentity = ObjectIdentity
lgs2624cGVRPConf = _Lgs2624cGVRPConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 4, 1)
)


class _Lgs2624cGVRPMode_Type(Integer32):
    """Custom type lgs2624cGVRPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cGVRPMode_Type.__name__ = "Integer32"
_Lgs2624cGVRPMode_Object = MibScalar
lgs2624cGVRPMode = _Lgs2624cGVRPMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 4, 1, 1),
    _Lgs2624cGVRPMode_Type()
)
lgs2624cGVRPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cGVRPMode.setStatus("current")
_Lgs2624cGVRPConfTable_Object = MibTable
lgs2624cGVRPConfTable = _Lgs2624cGVRPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    lgs2624cGVRPConfTable.setStatus("current")
_Lgs2624cGVRPConfEntry_Object = MibTableRow
lgs2624cGVRPConfEntry = _Lgs2624cGVRPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 4, 1, 2, 1)
)
lgs2624cGVRPConfEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cGVRPConfPort"),
)
if mibBuilder.loadTexts:
    lgs2624cGVRPConfEntry.setStatus("current")


class _Lgs2624cGVRPConfPort_Type(Integer32):
    """Custom type lgs2624cGVRPConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cGVRPConfPort_Type.__name__ = "Integer32"
_Lgs2624cGVRPConfPort_Object = MibTableColumn
lgs2624cGVRPConfPort = _Lgs2624cGVRPConfPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 4, 1, 2, 1, 1),
    _Lgs2624cGVRPConfPort_Type()
)
lgs2624cGVRPConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cGVRPConfPort.setStatus("current")


class _Lgs2624cGVRPConfPortMode_Type(Integer32):
    """Custom type lgs2624cGVRPConfPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cGVRPConfPortMode_Type.__name__ = "Integer32"
_Lgs2624cGVRPConfPortMode_Object = MibTableColumn
lgs2624cGVRPConfPortMode = _Lgs2624cGVRPConfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 4, 1, 2, 1, 2),
    _Lgs2624cGVRPConfPortMode_Type()
)
lgs2624cGVRPConfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cGVRPConfPortMode.setStatus("current")


class _Lgs2624cGVRPConfPortRRole_Type(Integer32):
    """Custom type lgs2624cGVRPConfPortRRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cGVRPConfPortRRole_Type.__name__ = "Integer32"
_Lgs2624cGVRPConfPortRRole_Object = MibTableColumn
lgs2624cGVRPConfPortRRole = _Lgs2624cGVRPConfPortRRole_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 4, 1, 2, 1, 3),
    _Lgs2624cGVRPConfPortRRole_Type()
)
lgs2624cGVRPConfPortRRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cGVRPConfPortRRole.setStatus("current")
_Lgs2624cGVRPStatisticsTable_Object = MibTable
lgs2624cGVRPStatisticsTable = _Lgs2624cGVRPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 4, 2)
)
if mibBuilder.loadTexts:
    lgs2624cGVRPStatisticsTable.setStatus("current")
_Lgs2624cGVRPStatisticsEntry_Object = MibTableRow
lgs2624cGVRPStatisticsEntry = _Lgs2624cGVRPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 4, 2, 1)
)
lgs2624cGVRPStatisticsEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cGVRPStatisticsPort"),
)
if mibBuilder.loadTexts:
    lgs2624cGVRPStatisticsEntry.setStatus("current")


class _Lgs2624cGVRPStatisticsPort_Type(Integer32):
    """Custom type lgs2624cGVRPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cGVRPStatisticsPort_Type.__name__ = "Integer32"
_Lgs2624cGVRPStatisticsPort_Object = MibTableColumn
lgs2624cGVRPStatisticsPort = _Lgs2624cGVRPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 4, 2, 1, 1),
    _Lgs2624cGVRPStatisticsPort_Type()
)
lgs2624cGVRPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cGVRPStatisticsPort.setStatus("current")
_Lgs2624cGVRPStatisticsJoinTxCnt_Type = Counter32
_Lgs2624cGVRPStatisticsJoinTxCnt_Object = MibTableColumn
lgs2624cGVRPStatisticsJoinTxCnt = _Lgs2624cGVRPStatisticsJoinTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 4, 2, 1, 2),
    _Lgs2624cGVRPStatisticsJoinTxCnt_Type()
)
lgs2624cGVRPStatisticsJoinTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cGVRPStatisticsJoinTxCnt.setStatus("current")
_Lgs2624cGVRPStatisticsLeaveTxCnt_Type = Counter32
_Lgs2624cGVRPStatisticsLeaveTxCnt_Object = MibTableColumn
lgs2624cGVRPStatisticsLeaveTxCnt = _Lgs2624cGVRPStatisticsLeaveTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 4, 2, 1, 3),
    _Lgs2624cGVRPStatisticsLeaveTxCnt_Type()
)
lgs2624cGVRPStatisticsLeaveTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cGVRPStatisticsLeaveTxCnt.setStatus("current")
_Lgs2624cThermalProtection_ObjectIdentity = ObjectIdentity
lgs2624cThermalProtection = _Lgs2624cThermalProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 5)
)


class _Lgs2624cPriority0Temperature_Type(Integer32):
    """Custom type lgs2624cPriority0Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Lgs2624cPriority0Temperature_Type.__name__ = "Integer32"
_Lgs2624cPriority0Temperature_Object = MibScalar
lgs2624cPriority0Temperature = _Lgs2624cPriority0Temperature_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 5, 1),
    _Lgs2624cPriority0Temperature_Type()
)
lgs2624cPriority0Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPriority0Temperature.setStatus("current")


class _Lgs2624cPriority1Temperature_Type(Integer32):
    """Custom type lgs2624cPriority1Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Lgs2624cPriority1Temperature_Type.__name__ = "Integer32"
_Lgs2624cPriority1Temperature_Object = MibScalar
lgs2624cPriority1Temperature = _Lgs2624cPriority1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 5, 2),
    _Lgs2624cPriority1Temperature_Type()
)
lgs2624cPriority1Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPriority1Temperature.setStatus("current")


class _Lgs2624cPriority2Temperature_Type(Integer32):
    """Custom type lgs2624cPriority2Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Lgs2624cPriority2Temperature_Type.__name__ = "Integer32"
_Lgs2624cPriority2Temperature_Object = MibScalar
lgs2624cPriority2Temperature = _Lgs2624cPriority2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 5, 3),
    _Lgs2624cPriority2Temperature_Type()
)
lgs2624cPriority2Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPriority2Temperature.setStatus("current")


class _Lgs2624cPriority3Temperature_Type(Integer32):
    """Custom type lgs2624cPriority3Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Lgs2624cPriority3Temperature_Type.__name__ = "Integer32"
_Lgs2624cPriority3Temperature_Object = MibScalar
lgs2624cPriority3Temperature = _Lgs2624cPriority3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 5, 4),
    _Lgs2624cPriority3Temperature_Type()
)
lgs2624cPriority3Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPriority3Temperature.setStatus("current")
_Lgs2624cThermalProtectionTable_Object = MibTable
lgs2624cThermalProtectionTable = _Lgs2624cThermalProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 5, 5)
)
if mibBuilder.loadTexts:
    lgs2624cThermalProtectionTable.setStatus("current")
_Lgs2624cThermalProtectionEntry_Object = MibTableRow
lgs2624cThermalProtectionEntry = _Lgs2624cThermalProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 5, 5, 1)
)
lgs2624cThermalProtectionEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cThermalProtectionPort"),
)
if mibBuilder.loadTexts:
    lgs2624cThermalProtectionEntry.setStatus("current")


class _Lgs2624cThermalProtectionPort_Type(Integer32):
    """Custom type lgs2624cThermalProtectionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cThermalProtectionPort_Type.__name__ = "Integer32"
_Lgs2624cThermalProtectionPort_Object = MibTableColumn
lgs2624cThermalProtectionPort = _Lgs2624cThermalProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 5, 5, 1, 1),
    _Lgs2624cThermalProtectionPort_Type()
)
lgs2624cThermalProtectionPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cThermalProtectionPort.setStatus("current")


class _Lgs2624cThermalProtectionPortTemperature_Type(Integer32):
    """Custom type lgs2624cThermalProtectionPortTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Lgs2624cThermalProtectionPortTemperature_Type.__name__ = "Integer32"
_Lgs2624cThermalProtectionPortTemperature_Object = MibTableColumn
lgs2624cThermalProtectionPortTemperature = _Lgs2624cThermalProtectionPortTemperature_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 5, 5, 1, 2),
    _Lgs2624cThermalProtectionPortTemperature_Type()
)
lgs2624cThermalProtectionPortTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cThermalProtectionPortTemperature.setStatus("current")


class _Lgs2624cThermalProtectionPortPriority_Type(Integer32):
    """Custom type lgs2624cThermalProtectionPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Lgs2624cThermalProtectionPortPriority_Type.__name__ = "Integer32"
_Lgs2624cThermalProtectionPortPriority_Object = MibTableColumn
lgs2624cThermalProtectionPortPriority = _Lgs2624cThermalProtectionPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 5, 5, 1, 3),
    _Lgs2624cThermalProtectionPortPriority_Type()
)
lgs2624cThermalProtectionPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cThermalProtectionPortPriority.setStatus("current")
_Lgs2624cThermalProtectionPortStatus_Type = DisplayString
_Lgs2624cThermalProtectionPortStatus_Object = MibTableColumn
lgs2624cThermalProtectionPortStatus = _Lgs2624cThermalProtectionPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 5, 5, 1, 4),
    _Lgs2624cThermalProtectionPortStatus_Type()
)
lgs2624cThermalProtectionPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cThermalProtectionPortStatus.setStatus("current")
_Lgs2624cMirroring_ObjectIdentity = ObjectIdentity
lgs2624cMirroring = _Lgs2624cMirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 6)
)


class _Lgs2624cPortToMirrorOn_Type(Integer32):
    """Custom type lgs2624cPortToMirrorOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Lgs2624cPortToMirrorOn_Type.__name__ = "Integer32"
_Lgs2624cPortToMirrorOn_Object = MibScalar
lgs2624cPortToMirrorOn = _Lgs2624cPortToMirrorOn_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 6, 1),
    _Lgs2624cPortToMirrorOn_Type()
)
lgs2624cPortToMirrorOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortToMirrorOn.setStatus("current")
_Lgs2624cMirrorTable_Object = MibTable
lgs2624cMirrorTable = _Lgs2624cMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 6, 2)
)
if mibBuilder.loadTexts:
    lgs2624cMirrorTable.setStatus("current")
_Lgs2624cMirrorEntry_Object = MibTableRow
lgs2624cMirrorEntry = _Lgs2624cMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 6, 2, 1)
)
lgs2624cMirrorEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cMirrorPort"),
)
if mibBuilder.loadTexts:
    lgs2624cMirrorEntry.setStatus("current")


class _Lgs2624cMirrorPort_Type(Integer32):
    """Custom type lgs2624cMirrorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cMirrorPort_Type.__name__ = "Integer32"
_Lgs2624cMirrorPort_Object = MibTableColumn
lgs2624cMirrorPort = _Lgs2624cMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 6, 2, 1, 1),
    _Lgs2624cMirrorPort_Type()
)
lgs2624cMirrorPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cMirrorPort.setStatus("current")


class _Lgs2624cMirrorMode_Type(Integer32):
    """Custom type lgs2624cMirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Lgs2624cMirrorMode_Type.__name__ = "Integer32"
_Lgs2624cMirrorMode_Object = MibTableColumn
lgs2624cMirrorMode = _Lgs2624cMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 6, 2, 1, 2),
    _Lgs2624cMirrorMode_Type()
)
lgs2624cMirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cMirrorMode.setStatus("current")
_Lgs2624cTrapEventSeverity_ObjectIdentity = ObjectIdentity
lgs2624cTrapEventSeverity = _Lgs2624cTrapEventSeverity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7)
)


class _Lgs2624cTrapEventSeverityACL_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityACL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityACL_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityACL_Object = MibScalar
lgs2624cTrapEventSeverityACL = _Lgs2624cTrapEventSeverityACL_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 1),
    _Lgs2624cTrapEventSeverityACL_Type()
)
lgs2624cTrapEventSeverityACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityACL.setStatus("current")


class _Lgs2624cTrapEventSeverityACLLog_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityACLLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityACLLog_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityACLLog_Object = MibScalar
lgs2624cTrapEventSeverityACLLog = _Lgs2624cTrapEventSeverityACLLog_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 2),
    _Lgs2624cTrapEventSeverityACLLog_Type()
)
lgs2624cTrapEventSeverityACLLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityACLLog.setStatus("current")


class _Lgs2624cTrapEventSeverityAccessMgmt_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityAccessMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityAccessMgmt_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityAccessMgmt_Object = MibScalar
lgs2624cTrapEventSeverityAccessMgmt = _Lgs2624cTrapEventSeverityAccessMgmt_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 3),
    _Lgs2624cTrapEventSeverityAccessMgmt_Type()
)
lgs2624cTrapEventSeverityAccessMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityAccessMgmt.setStatus("current")


class _Lgs2624cTrapEventSeverityAuthFailed_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityAuthFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityAuthFailed_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityAuthFailed_Object = MibScalar
lgs2624cTrapEventSeverityAuthFailed = _Lgs2624cTrapEventSeverityAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 4),
    _Lgs2624cTrapEventSeverityAuthFailed_Type()
)
lgs2624cTrapEventSeverityAuthFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityAuthFailed.setStatus("current")


class _Lgs2624cTrapEventSeverityColdStart_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityColdStart_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityColdStart_Object = MibScalar
lgs2624cTrapEventSeverityColdStart = _Lgs2624cTrapEventSeverityColdStart_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 5),
    _Lgs2624cTrapEventSeverityColdStart_Type()
)
lgs2624cTrapEventSeverityColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityColdStart.setStatus("current")


class _Lgs2624cTrapEventSeverityConfigInfo_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityConfigInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityConfigInfo_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityConfigInfo_Object = MibScalar
lgs2624cTrapEventSeverityConfigInfo = _Lgs2624cTrapEventSeverityConfigInfo_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 6),
    _Lgs2624cTrapEventSeverityConfigInfo_Type()
)
lgs2624cTrapEventSeverityConfigInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityConfigInfo.setStatus("current")


class _Lgs2624cTrapEventSeverityFirmwareUpgrade_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityFirmwareUpgrade_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityFirmwareUpgrade_Object = MibScalar
lgs2624cTrapEventSeverityFirmwareUpgrade = _Lgs2624cTrapEventSeverityFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 7),
    _Lgs2624cTrapEventSeverityFirmwareUpgrade_Type()
)
lgs2624cTrapEventSeverityFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityFirmwareUpgrade.setStatus("current")


class _Lgs2624cTrapEventSeverityImportExport_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityImportExport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityImportExport_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityImportExport_Object = MibScalar
lgs2624cTrapEventSeverityImportExport = _Lgs2624cTrapEventSeverityImportExport_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 8),
    _Lgs2624cTrapEventSeverityImportExport_Type()
)
lgs2624cTrapEventSeverityImportExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityImportExport.setStatus("current")


class _Lgs2624cTrapEventSeverityLinkStatus_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityLinkStatus_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityLinkStatus_Object = MibScalar
lgs2624cTrapEventSeverityLinkStatus = _Lgs2624cTrapEventSeverityLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 9),
    _Lgs2624cTrapEventSeverityLinkStatus_Type()
)
lgs2624cTrapEventSeverityLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityLinkStatus.setStatus("current")


class _Lgs2624cTrapEventSeverityLogin_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityLogin_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityLogin_Object = MibScalar
lgs2624cTrapEventSeverityLogin = _Lgs2624cTrapEventSeverityLogin_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 10),
    _Lgs2624cTrapEventSeverityLogin_Type()
)
lgs2624cTrapEventSeverityLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityLogin.setStatus("current")


class _Lgs2624cTrapEventSeverityLogout_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityLogout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityLogout_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityLogout_Object = MibScalar
lgs2624cTrapEventSeverityLogout = _Lgs2624cTrapEventSeverityLogout_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 11),
    _Lgs2624cTrapEventSeverityLogout_Type()
)
lgs2624cTrapEventSeverityLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityLogout.setStatus("current")


class _Lgs2624cTrapEventSeverityMgmtIPChange_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityMgmtIPChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityMgmtIPChange_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityMgmtIPChange_Object = MibScalar
lgs2624cTrapEventSeverityMgmtIPChange = _Lgs2624cTrapEventSeverityMgmtIPChange_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 12),
    _Lgs2624cTrapEventSeverityMgmtIPChange_Type()
)
lgs2624cTrapEventSeverityMgmtIPChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityMgmtIPChange.setStatus("current")


class _Lgs2624cTrapEventSeverityModuleChange_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityModuleChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityModuleChange_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityModuleChange_Object = MibScalar
lgs2624cTrapEventSeverityModuleChange = _Lgs2624cTrapEventSeverityModuleChange_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 13),
    _Lgs2624cTrapEventSeverityModuleChange_Type()
)
lgs2624cTrapEventSeverityModuleChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityModuleChange.setStatus("current")


class _Lgs2624cTrapEventSeverityNAS_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityNAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityNAS_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityNAS_Object = MibScalar
lgs2624cTrapEventSeverityNAS = _Lgs2624cTrapEventSeverityNAS_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 14),
    _Lgs2624cTrapEventSeverityNAS_Type()
)
lgs2624cTrapEventSeverityNAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityNAS.setStatus("current")


class _Lgs2624cTrapEventSeverityPasswdChange_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityPasswdChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityPasswdChange_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityPasswdChange_Object = MibScalar
lgs2624cTrapEventSeverityPasswdChange = _Lgs2624cTrapEventSeverityPasswdChange_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 15),
    _Lgs2624cTrapEventSeverityPasswdChange_Type()
)
lgs2624cTrapEventSeverityPasswdChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityPasswdChange.setStatus("current")


class _Lgs2624cTrapEventSeverityPortSecurity_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityPortSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityPortSecurity_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityPortSecurity_Object = MibScalar
lgs2624cTrapEventSeverityPortSecurity = _Lgs2624cTrapEventSeverityPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 16),
    _Lgs2624cTrapEventSeverityPortSecurity_Type()
)
lgs2624cTrapEventSeverityPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityPortSecurity.setStatus("current")


class _Lgs2624cTrapEventSeverityThermalProtect_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityThermalProtect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityThermalProtect_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityThermalProtect_Object = MibScalar
lgs2624cTrapEventSeverityThermalProtect = _Lgs2624cTrapEventSeverityThermalProtect_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 17),
    _Lgs2624cTrapEventSeverityThermalProtect_Type()
)
lgs2624cTrapEventSeverityThermalProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityThermalProtect.setStatus("current")


class _Lgs2624cTrapEventSeverityVLAN_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityVLAN_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityVLAN_Object = MibScalar
lgs2624cTrapEventSeverityVLAN = _Lgs2624cTrapEventSeverityVLAN_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 18),
    _Lgs2624cTrapEventSeverityVLAN_Type()
)
lgs2624cTrapEventSeverityVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityVLAN.setStatus("current")


class _Lgs2624cTrapEventSeverityWarmStart_Type(Integer32):
    """Custom type lgs2624cTrapEventSeverityWarmStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cTrapEventSeverityWarmStart_Type.__name__ = "Integer32"
_Lgs2624cTrapEventSeverityWarmStart_Object = MibScalar
lgs2624cTrapEventSeverityWarmStart = _Lgs2624cTrapEventSeverityWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 7, 19),
    _Lgs2624cTrapEventSeverityWarmStart_Type()
)
lgs2624cTrapEventSeverityWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTrapEventSeverityWarmStart.setStatus("current")
_Lgs2624cSMTP_ObjectIdentity = ObjectIdentity
lgs2624cSMTP = _Lgs2624cSMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 8)
)
_Lgs2624cSMTPMailServer_Type = DisplayString
_Lgs2624cSMTPMailServer_Object = MibScalar
lgs2624cSMTPMailServer = _Lgs2624cSMTPMailServer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 8, 1),
    _Lgs2624cSMTPMailServer_Type()
)
lgs2624cSMTPMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSMTPMailServer.setStatus("current")
_Lgs2624cSMTPUserName_Type = DisplayString
_Lgs2624cSMTPUserName_Object = MibScalar
lgs2624cSMTPUserName = _Lgs2624cSMTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 8, 2),
    _Lgs2624cSMTPUserName_Type()
)
lgs2624cSMTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSMTPUserName.setStatus("current")
_Lgs2624cSMTPPassword_Type = DisplayString
_Lgs2624cSMTPPassword_Object = MibScalar
lgs2624cSMTPPassword = _Lgs2624cSMTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 8, 3),
    _Lgs2624cSMTPPassword_Type()
)
lgs2624cSMTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSMTPPassword.setStatus("current")


class _Lgs2624cSMTPServeriryLevel_Type(Integer32):
    """Custom type lgs2624cSMTPServeriryLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2624cSMTPServeriryLevel_Type.__name__ = "Integer32"
_Lgs2624cSMTPServeriryLevel_Object = MibScalar
lgs2624cSMTPServeriryLevel = _Lgs2624cSMTPServeriryLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 8, 4),
    _Lgs2624cSMTPServeriryLevel_Type()
)
lgs2624cSMTPServeriryLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSMTPServeriryLevel.setStatus("current")
_Lgs2624cSMTPSender_Type = DisplayString
_Lgs2624cSMTPSender_Object = MibScalar
lgs2624cSMTPSender = _Lgs2624cSMTPSender_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 8, 5),
    _Lgs2624cSMTPSender_Type()
)
lgs2624cSMTPSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSMTPSender.setStatus("current")
_Lgs2624cSMTPReturnPath_Type = DisplayString
_Lgs2624cSMTPReturnPath_Object = MibScalar
lgs2624cSMTPReturnPath = _Lgs2624cSMTPReturnPath_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 8, 6),
    _Lgs2624cSMTPReturnPath_Type()
)
lgs2624cSMTPReturnPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSMTPReturnPath.setStatus("current")
_Lgs2624cSMTPEmailAddress1_Type = DisplayString
_Lgs2624cSMTPEmailAddress1_Object = MibScalar
lgs2624cSMTPEmailAddress1 = _Lgs2624cSMTPEmailAddress1_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 8, 7),
    _Lgs2624cSMTPEmailAddress1_Type()
)
lgs2624cSMTPEmailAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSMTPEmailAddress1.setStatus("current")
_Lgs2624cSMTPEmailAddress2_Type = DisplayString
_Lgs2624cSMTPEmailAddress2_Object = MibScalar
lgs2624cSMTPEmailAddress2 = _Lgs2624cSMTPEmailAddress2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 8, 8),
    _Lgs2624cSMTPEmailAddress2_Type()
)
lgs2624cSMTPEmailAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSMTPEmailAddress2.setStatus("current")
_Lgs2624cSMTPEmailAddress3_Type = DisplayString
_Lgs2624cSMTPEmailAddress3_Object = MibScalar
lgs2624cSMTPEmailAddress3 = _Lgs2624cSMTPEmailAddress3_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 8, 9),
    _Lgs2624cSMTPEmailAddress3_Type()
)
lgs2624cSMTPEmailAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSMTPEmailAddress3.setStatus("current")
_Lgs2624cSMTPEmailAddress4_Type = DisplayString
_Lgs2624cSMTPEmailAddress4_Object = MibScalar
lgs2624cSMTPEmailAddress4 = _Lgs2624cSMTPEmailAddress4_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 8, 10),
    _Lgs2624cSMTPEmailAddress4_Type()
)
lgs2624cSMTPEmailAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSMTPEmailAddress4.setStatus("current")
_Lgs2624cSMTPEmailAddress5_Type = DisplayString
_Lgs2624cSMTPEmailAddress5_Object = MibScalar
lgs2624cSMTPEmailAddress5 = _Lgs2624cSMTPEmailAddress5_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 8, 11),
    _Lgs2624cSMTPEmailAddress5_Type()
)
lgs2624cSMTPEmailAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSMTPEmailAddress5.setStatus("current")
_Lgs2624cSMTPEmailAddress6_Type = DisplayString
_Lgs2624cSMTPEmailAddress6_Object = MibScalar
lgs2624cSMTPEmailAddress6 = _Lgs2624cSMTPEmailAddress6_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 2, 8, 12),
    _Lgs2624cSMTPEmailAddress6_Type()
)
lgs2624cSMTPEmailAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSMTPEmailAddress6.setStatus("current")
_Lgs2624cSecurity_ObjectIdentity = ObjectIdentity
lgs2624cSecurity = _Lgs2624cSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3)
)
_Lgs2624cIPSourceGuard_ObjectIdentity = ObjectIdentity
lgs2624cIPSourceGuard = _Lgs2624cIPSourceGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1)
)
_Lgs2624cIPSourceGuardConf_ObjectIdentity = ObjectIdentity
lgs2624cIPSourceGuardConf = _Lgs2624cIPSourceGuardConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 1)
)


class _Lgs2624cIPSourceGuardMode_Type(Integer32):
    """Custom type lgs2624cIPSourceGuardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cIPSourceGuardMode_Type.__name__ = "Integer32"
_Lgs2624cIPSourceGuardMode_Object = MibScalar
lgs2624cIPSourceGuardMode = _Lgs2624cIPSourceGuardMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 1, 1),
    _Lgs2624cIPSourceGuardMode_Type()
)
lgs2624cIPSourceGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardMode.setStatus("current")
_Lgs2624cIPSourceGuardPortConfigTable_Object = MibTable
lgs2624cIPSourceGuardPortConfigTable = _Lgs2624cIPSourceGuardPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardPortConfigTable.setStatus("current")
_Lgs2624cIPSourceGuardPortConfigEntry_Object = MibTableRow
lgs2624cIPSourceGuardPortConfigEntry = _Lgs2624cIPSourceGuardPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 1, 2, 1)
)
lgs2624cIPSourceGuardPortConfigEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cIPSourceGuardPortConfigPort"),
)
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardPortConfigEntry.setStatus("current")


class _Lgs2624cIPSourceGuardPortConfigPort_Type(Integer32):
    """Custom type lgs2624cIPSourceGuardPortConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cIPSourceGuardPortConfigPort_Type.__name__ = "Integer32"
_Lgs2624cIPSourceGuardPortConfigPort_Object = MibTableColumn
lgs2624cIPSourceGuardPortConfigPort = _Lgs2624cIPSourceGuardPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 1, 2, 1, 1),
    _Lgs2624cIPSourceGuardPortConfigPort_Type()
)
lgs2624cIPSourceGuardPortConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardPortConfigPort.setStatus("current")


class _Lgs2624cIPSourceGuardPortConfigMode_Type(Integer32):
    """Custom type lgs2624cIPSourceGuardPortConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cIPSourceGuardPortConfigMode_Type.__name__ = "Integer32"
_Lgs2624cIPSourceGuardPortConfigMode_Object = MibTableColumn
lgs2624cIPSourceGuardPortConfigMode = _Lgs2624cIPSourceGuardPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 1, 2, 1, 2),
    _Lgs2624cIPSourceGuardPortConfigMode_Type()
)
lgs2624cIPSourceGuardPortConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardPortConfigMode.setStatus("current")


class _Lgs2624cIPSourceGuardPortMaxDynamicClients_Type(Integer32):
    """Custom type lgs2624cIPSourceGuardPortMaxDynamicClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(99, 99),
    )


_Lgs2624cIPSourceGuardPortMaxDynamicClients_Type.__name__ = "Integer32"
_Lgs2624cIPSourceGuardPortMaxDynamicClients_Object = MibTableColumn
lgs2624cIPSourceGuardPortMaxDynamicClients = _Lgs2624cIPSourceGuardPortMaxDynamicClients_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 1, 2, 1, 3),
    _Lgs2624cIPSourceGuardPortMaxDynamicClients_Type()
)
lgs2624cIPSourceGuardPortMaxDynamicClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardPortMaxDynamicClients.setStatus("current")
_Lgs2624cIPSourceGuardStatic_ObjectIdentity = ObjectIdentity
lgs2624cIPSourceGuardStatic = _Lgs2624cIPSourceGuardStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 2)
)


class _Lgs2624cIPSourceGuardStaticCreate_Type(Integer32):
    """Custom type lgs2624cIPSourceGuardStaticCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cIPSourceGuardStaticCreate_Type.__name__ = "Integer32"
_Lgs2624cIPSourceGuardStaticCreate_Object = MibScalar
lgs2624cIPSourceGuardStaticCreate = _Lgs2624cIPSourceGuardStaticCreate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 2, 1),
    _Lgs2624cIPSourceGuardStaticCreate_Type()
)
lgs2624cIPSourceGuardStaticCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardStaticCreate.setStatus("current")
_Lgs2624cIPSourceGuardStaticTable_Object = MibTable
lgs2624cIPSourceGuardStaticTable = _Lgs2624cIPSourceGuardStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardStaticTable.setStatus("current")
_Lgs2624cIPSourceGuardStaticEntry_Object = MibTableRow
lgs2624cIPSourceGuardStaticEntry = _Lgs2624cIPSourceGuardStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 2, 2, 1)
)
lgs2624cIPSourceGuardStaticEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cIPSourceGuardStaticIndex"),
)
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardStaticEntry.setStatus("current")


class _Lgs2624cIPSourceGuardStaticIndex_Type(Integer32):
    """Custom type lgs2624cIPSourceGuardStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_Lgs2624cIPSourceGuardStaticIndex_Type.__name__ = "Integer32"
_Lgs2624cIPSourceGuardStaticIndex_Object = MibTableColumn
lgs2624cIPSourceGuardStaticIndex = _Lgs2624cIPSourceGuardStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 2, 2, 1, 1),
    _Lgs2624cIPSourceGuardStaticIndex_Type()
)
lgs2624cIPSourceGuardStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardStaticIndex.setStatus("current")


class _Lgs2624cIPSourceGuardStaticPort_Type(Integer32):
    """Custom type lgs2624cIPSourceGuardStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cIPSourceGuardStaticPort_Type.__name__ = "Integer32"
_Lgs2624cIPSourceGuardStaticPort_Object = MibTableColumn
lgs2624cIPSourceGuardStaticPort = _Lgs2624cIPSourceGuardStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 2, 2, 1, 2),
    _Lgs2624cIPSourceGuardStaticPort_Type()
)
lgs2624cIPSourceGuardStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardStaticPort.setStatus("current")


class _Lgs2624cIPSourceGuardStaticVLANId_Type(Integer32):
    """Custom type lgs2624cIPSourceGuardStaticVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2624cIPSourceGuardStaticVLANId_Type.__name__ = "Integer32"
_Lgs2624cIPSourceGuardStaticVLANId_Object = MibTableColumn
lgs2624cIPSourceGuardStaticVLANId = _Lgs2624cIPSourceGuardStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 2, 2, 1, 3),
    _Lgs2624cIPSourceGuardStaticVLANId_Type()
)
lgs2624cIPSourceGuardStaticVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardStaticVLANId.setStatus("current")
_Lgs2624cIPSourceGuardStaticIPAddress_Type = IpAddress
_Lgs2624cIPSourceGuardStaticIPAddress_Object = MibTableColumn
lgs2624cIPSourceGuardStaticIPAddress = _Lgs2624cIPSourceGuardStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 2, 2, 1, 4),
    _Lgs2624cIPSourceGuardStaticIPAddress_Type()
)
lgs2624cIPSourceGuardStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardStaticIPAddress.setStatus("current")
_Lgs2624cIPSourceGuardStaticMACAddress_Type = MacAddress
_Lgs2624cIPSourceGuardStaticMACAddress_Object = MibTableColumn
lgs2624cIPSourceGuardStaticMACAddress = _Lgs2624cIPSourceGuardStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 2, 2, 1, 5),
    _Lgs2624cIPSourceGuardStaticMACAddress_Type()
)
lgs2624cIPSourceGuardStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardStaticMACAddress.setStatus("current")


class _Lgs2624cIPSourceGuardStaticRowStatus_Type(Integer32):
    """Custom type lgs2624cIPSourceGuardStaticRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Lgs2624cIPSourceGuardStaticRowStatus_Type.__name__ = "Integer32"
_Lgs2624cIPSourceGuardStaticRowStatus_Object = MibTableColumn
lgs2624cIPSourceGuardStaticRowStatus = _Lgs2624cIPSourceGuardStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 2, 2, 1, 6),
    _Lgs2624cIPSourceGuardStaticRowStatus_Type()
)
lgs2624cIPSourceGuardStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardStaticRowStatus.setStatus("current")
_Lgs2624cIPSourceGuardDynamicTable_Object = MibTable
lgs2624cIPSourceGuardDynamicTable = _Lgs2624cIPSourceGuardDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 3)
)
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardDynamicTable.setStatus("current")
_Lgs2624cIPSourceGuardDynamicEntry_Object = MibTableRow
lgs2624cIPSourceGuardDynamicEntry = _Lgs2624cIPSourceGuardDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 3, 1)
)
lgs2624cIPSourceGuardDynamicEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cIPSourceGuardDynamicIndex"),
)
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardDynamicEntry.setStatus("current")


class _Lgs2624cIPSourceGuardDynamicIndex_Type(Integer32):
    """Custom type lgs2624cIPSourceGuardDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cIPSourceGuardDynamicIndex_Type.__name__ = "Integer32"
_Lgs2624cIPSourceGuardDynamicIndex_Object = MibTableColumn
lgs2624cIPSourceGuardDynamicIndex = _Lgs2624cIPSourceGuardDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 3, 1, 1),
    _Lgs2624cIPSourceGuardDynamicIndex_Type()
)
lgs2624cIPSourceGuardDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardDynamicIndex.setStatus("current")


class _Lgs2624cIPSourceGuardDynamicPort_Type(Integer32):
    """Custom type lgs2624cIPSourceGuardDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Lgs2624cIPSourceGuardDynamicPort_Type.__name__ = "Integer32"
_Lgs2624cIPSourceGuardDynamicPort_Object = MibTableColumn
lgs2624cIPSourceGuardDynamicPort = _Lgs2624cIPSourceGuardDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 3, 1, 2),
    _Lgs2624cIPSourceGuardDynamicPort_Type()
)
lgs2624cIPSourceGuardDynamicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardDynamicPort.setStatus("current")


class _Lgs2624cIPSourceGuardDynamicVLANId_Type(Integer32):
    """Custom type lgs2624cIPSourceGuardDynamicVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2624cIPSourceGuardDynamicVLANId_Type.__name__ = "Integer32"
_Lgs2624cIPSourceGuardDynamicVLANId_Object = MibTableColumn
lgs2624cIPSourceGuardDynamicVLANId = _Lgs2624cIPSourceGuardDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 3, 1, 3),
    _Lgs2624cIPSourceGuardDynamicVLANId_Type()
)
lgs2624cIPSourceGuardDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardDynamicVLANId.setStatus("current")
_Lgs2624cIPSourceGuardDynamicIPAddress_Type = IpAddress
_Lgs2624cIPSourceGuardDynamicIPAddress_Object = MibTableColumn
lgs2624cIPSourceGuardDynamicIPAddress = _Lgs2624cIPSourceGuardDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 3, 1, 4),
    _Lgs2624cIPSourceGuardDynamicIPAddress_Type()
)
lgs2624cIPSourceGuardDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardDynamicIPAddress.setStatus("current")
_Lgs2624cIPSourceGuardDynamicMACAddress_Type = MacAddress
_Lgs2624cIPSourceGuardDynamicMACAddress_Object = MibTableColumn
lgs2624cIPSourceGuardDynamicMACAddress = _Lgs2624cIPSourceGuardDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 1, 3, 1, 5),
    _Lgs2624cIPSourceGuardDynamicMACAddress_Type()
)
lgs2624cIPSourceGuardDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cIPSourceGuardDynamicMACAddress.setStatus("current")
_Lgs2624cARPInspection_ObjectIdentity = ObjectIdentity
lgs2624cARPInspection = _Lgs2624cARPInspection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2)
)
_Lgs2624cARPInspectionConf_ObjectIdentity = ObjectIdentity
lgs2624cARPInspectionConf = _Lgs2624cARPInspectionConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 1)
)


class _Lgs2624cARPInspectionConfMode_Type(Integer32):
    """Custom type lgs2624cARPInspectionConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cARPInspectionConfMode_Type.__name__ = "Integer32"
_Lgs2624cARPInspectionConfMode_Object = MibScalar
lgs2624cARPInspectionConfMode = _Lgs2624cARPInspectionConfMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 1, 1),
    _Lgs2624cARPInspectionConfMode_Type()
)
lgs2624cARPInspectionConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cARPInspectionConfMode.setStatus("current")
_Lgs2624cARPInspectionConfTable_Object = MibTable
lgs2624cARPInspectionConfTable = _Lgs2624cARPInspectionConfTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    lgs2624cARPInspectionConfTable.setStatus("current")
_Lgs2624cARPInspectionConfEntry_Object = MibTableRow
lgs2624cARPInspectionConfEntry = _Lgs2624cARPInspectionConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 1, 2, 1)
)
lgs2624cARPInspectionConfEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cARPInspectionConfPortIndex"),
)
if mibBuilder.loadTexts:
    lgs2624cARPInspectionConfEntry.setStatus("current")


class _Lgs2624cARPInspectionConfPortIndex_Type(Integer32):
    """Custom type lgs2624cARPInspectionConfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cARPInspectionConfPortIndex_Type.__name__ = "Integer32"
_Lgs2624cARPInspectionConfPortIndex_Object = MibTableColumn
lgs2624cARPInspectionConfPortIndex = _Lgs2624cARPInspectionConfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 1, 2, 1, 1),
    _Lgs2624cARPInspectionConfPortIndex_Type()
)
lgs2624cARPInspectionConfPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cARPInspectionConfPortIndex.setStatus("current")


class _Lgs2624cARPInspectionConfPortMode_Type(Integer32):
    """Custom type lgs2624cARPInspectionConfPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cARPInspectionConfPortMode_Type.__name__ = "Integer32"
_Lgs2624cARPInspectionConfPortMode_Object = MibTableColumn
lgs2624cARPInspectionConfPortMode = _Lgs2624cARPInspectionConfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 1, 2, 1, 2),
    _Lgs2624cARPInspectionConfPortMode_Type()
)
lgs2624cARPInspectionConfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cARPInspectionConfPortMode.setStatus("current")
_Lgs2624cARPInspectionStatic_ObjectIdentity = ObjectIdentity
lgs2624cARPInspectionStatic = _Lgs2624cARPInspectionStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 2)
)


class _Lgs2624cARPInspectionStaticCreate_Type(Integer32):
    """Custom type lgs2624cARPInspectionStaticCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cARPInspectionStaticCreate_Type.__name__ = "Integer32"
_Lgs2624cARPInspectionStaticCreate_Object = MibScalar
lgs2624cARPInspectionStaticCreate = _Lgs2624cARPInspectionStaticCreate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 2, 1),
    _Lgs2624cARPInspectionStaticCreate_Type()
)
lgs2624cARPInspectionStaticCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cARPInspectionStaticCreate.setStatus("current")
_Lgs2624cARPInspectionStaticTable_Object = MibTable
lgs2624cARPInspectionStaticTable = _Lgs2624cARPInspectionStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    lgs2624cARPInspectionStaticTable.setStatus("current")
_Lgs2624cARPInspectionStaticEntry_Object = MibTableRow
lgs2624cARPInspectionStaticEntry = _Lgs2624cARPInspectionStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 2, 2, 1)
)
lgs2624cARPInspectionStaticEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cARPInspectionStaticIndex"),
)
if mibBuilder.loadTexts:
    lgs2624cARPInspectionStaticEntry.setStatus("current")


class _Lgs2624cARPInspectionStaticIndex_Type(Integer32):
    """Custom type lgs2624cARPInspectionStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cARPInspectionStaticIndex_Type.__name__ = "Integer32"
_Lgs2624cARPInspectionStaticIndex_Object = MibTableColumn
lgs2624cARPInspectionStaticIndex = _Lgs2624cARPInspectionStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 2, 2, 1, 1),
    _Lgs2624cARPInspectionStaticIndex_Type()
)
lgs2624cARPInspectionStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cARPInspectionStaticIndex.setStatus("current")


class _Lgs2624cARPInspectionStaticPort_Type(Integer32):
    """Custom type lgs2624cARPInspectionStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cARPInspectionStaticPort_Type.__name__ = "Integer32"
_Lgs2624cARPInspectionStaticPort_Object = MibTableColumn
lgs2624cARPInspectionStaticPort = _Lgs2624cARPInspectionStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 2, 2, 1, 2),
    _Lgs2624cARPInspectionStaticPort_Type()
)
lgs2624cARPInspectionStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cARPInspectionStaticPort.setStatus("current")


class _Lgs2624cARPInspectionStaticVLANId_Type(Integer32):
    """Custom type lgs2624cARPInspectionStaticVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2624cARPInspectionStaticVLANId_Type.__name__ = "Integer32"
_Lgs2624cARPInspectionStaticVLANId_Object = MibTableColumn
lgs2624cARPInspectionStaticVLANId = _Lgs2624cARPInspectionStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 2, 2, 1, 3),
    _Lgs2624cARPInspectionStaticVLANId_Type()
)
lgs2624cARPInspectionStaticVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cARPInspectionStaticVLANId.setStatus("current")
_Lgs2624cARPInspectionStaticIPAddress_Type = IpAddress
_Lgs2624cARPInspectionStaticIPAddress_Object = MibTableColumn
lgs2624cARPInspectionStaticIPAddress = _Lgs2624cARPInspectionStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 2, 2, 1, 4),
    _Lgs2624cARPInspectionStaticIPAddress_Type()
)
lgs2624cARPInspectionStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cARPInspectionStaticIPAddress.setStatus("current")
_Lgs2624cARPInspectionStaticMACAddress_Type = MacAddress
_Lgs2624cARPInspectionStaticMACAddress_Object = MibTableColumn
lgs2624cARPInspectionStaticMACAddress = _Lgs2624cARPInspectionStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 2, 2, 1, 5),
    _Lgs2624cARPInspectionStaticMACAddress_Type()
)
lgs2624cARPInspectionStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cARPInspectionStaticMACAddress.setStatus("current")


class _Lgs2624cARPInspectionStaticRowStatus_Type(Integer32):
    """Custom type lgs2624cARPInspectionStaticRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Lgs2624cARPInspectionStaticRowStatus_Type.__name__ = "Integer32"
_Lgs2624cARPInspectionStaticRowStatus_Object = MibTableColumn
lgs2624cARPInspectionStaticRowStatus = _Lgs2624cARPInspectionStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 2, 2, 1, 6),
    _Lgs2624cARPInspectionStaticRowStatus_Type()
)
lgs2624cARPInspectionStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cARPInspectionStaticRowStatus.setStatus("current")
_Lgs2624cARPInspectionDynamicTable_Object = MibTable
lgs2624cARPInspectionDynamicTable = _Lgs2624cARPInspectionDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 3)
)
if mibBuilder.loadTexts:
    lgs2624cARPInspectionDynamicTable.setStatus("current")
_Lgs2624cARPInspectionDynamicEntry_Object = MibTableRow
lgs2624cARPInspectionDynamicEntry = _Lgs2624cARPInspectionDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 3, 1)
)
lgs2624cARPInspectionDynamicEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cARPInspectionDynamicIndex"),
)
if mibBuilder.loadTexts:
    lgs2624cARPInspectionDynamicEntry.setStatus("current")


class _Lgs2624cARPInspectionDynamicIndex_Type(Integer32):
    """Custom type lgs2624cARPInspectionDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cARPInspectionDynamicIndex_Type.__name__ = "Integer32"
_Lgs2624cARPInspectionDynamicIndex_Object = MibTableColumn
lgs2624cARPInspectionDynamicIndex = _Lgs2624cARPInspectionDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 3, 1, 1),
    _Lgs2624cARPInspectionDynamicIndex_Type()
)
lgs2624cARPInspectionDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cARPInspectionDynamicIndex.setStatus("current")


class _Lgs2624cARPInspectionDynamicPort_Type(Integer32):
    """Custom type lgs2624cARPInspectionDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cARPInspectionDynamicPort_Type.__name__ = "Integer32"
_Lgs2624cARPInspectionDynamicPort_Object = MibTableColumn
lgs2624cARPInspectionDynamicPort = _Lgs2624cARPInspectionDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 3, 1, 2),
    _Lgs2624cARPInspectionDynamicPort_Type()
)
lgs2624cARPInspectionDynamicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cARPInspectionDynamicPort.setStatus("current")


class _Lgs2624cARPInspectionDynamicVLANId_Type(Integer32):
    """Custom type lgs2624cARPInspectionDynamicVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2624cARPInspectionDynamicVLANId_Type.__name__ = "Integer32"
_Lgs2624cARPInspectionDynamicVLANId_Object = MibTableColumn
lgs2624cARPInspectionDynamicVLANId = _Lgs2624cARPInspectionDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 3, 1, 3),
    _Lgs2624cARPInspectionDynamicVLANId_Type()
)
lgs2624cARPInspectionDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cARPInspectionDynamicVLANId.setStatus("current")
_Lgs2624cARPInspectionDynamicIPAddress_Type = IpAddress
_Lgs2624cARPInspectionDynamicIPAddress_Object = MibTableColumn
lgs2624cARPInspectionDynamicIPAddress = _Lgs2624cARPInspectionDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 3, 1, 4),
    _Lgs2624cARPInspectionDynamicIPAddress_Type()
)
lgs2624cARPInspectionDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cARPInspectionDynamicIPAddress.setStatus("current")
_Lgs2624cARPInspectionDynamicMACAddress_Type = MacAddress
_Lgs2624cARPInspectionDynamicMACAddress_Object = MibTableColumn
lgs2624cARPInspectionDynamicMACAddress = _Lgs2624cARPInspectionDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 2, 3, 1, 5),
    _Lgs2624cARPInspectionDynamicMACAddress_Type()
)
lgs2624cARPInspectionDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cARPInspectionDynamicMACAddress.setStatus("current")
_Lgs2624cDHCPSnooping_ObjectIdentity = ObjectIdentity
lgs2624cDHCPSnooping = _Lgs2624cDHCPSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3)
)
_Lgs2624cDHCPSnoopingConf_ObjectIdentity = ObjectIdentity
lgs2624cDHCPSnoopingConf = _Lgs2624cDHCPSnoopingConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 1)
)


class _Lgs2624cDHCPSnoopingMode_Type(Integer32):
    """Custom type lgs2624cDHCPSnoopingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cDHCPSnoopingMode_Type.__name__ = "Integer32"
_Lgs2624cDHCPSnoopingMode_Object = MibScalar
lgs2624cDHCPSnoopingMode = _Lgs2624cDHCPSnoopingMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 1, 1),
    _Lgs2624cDHCPSnoopingMode_Type()
)
lgs2624cDHCPSnoopingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingMode.setStatus("current")
_Lgs2624cDHCPSnoopingPortModeConfigurationTable_Object = MibTable
lgs2624cDHCPSnoopingPortModeConfigurationTable = _Lgs2624cDHCPSnoopingPortModeConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingPortModeConfigurationTable.setStatus("current")
_Lgs2624cDHCPSnoopingPortModeConfigurationEntry_Object = MibTableRow
lgs2624cDHCPSnoopingPortModeConfigurationEntry = _Lgs2624cDHCPSnoopingPortModeConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 1, 2, 1)
)
lgs2624cDHCPSnoopingPortModeConfigurationEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cDHCPSnoopingPortModeConfigurationPort"),
)
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingPortModeConfigurationEntry.setStatus("current")


class _Lgs2624cDHCPSnoopingPortModeConfigurationPort_Type(Integer32):
    """Custom type lgs2624cDHCPSnoopingPortModeConfigurationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cDHCPSnoopingPortModeConfigurationPort_Type.__name__ = "Integer32"
_Lgs2624cDHCPSnoopingPortModeConfigurationPort_Object = MibTableColumn
lgs2624cDHCPSnoopingPortModeConfigurationPort = _Lgs2624cDHCPSnoopingPortModeConfigurationPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 1, 2, 1, 1),
    _Lgs2624cDHCPSnoopingPortModeConfigurationPort_Type()
)
lgs2624cDHCPSnoopingPortModeConfigurationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingPortModeConfigurationPort.setStatus("current")


class _Lgs2624cDHCPSnoopingPortModeConfigurationMode_Type(Integer32):
    """Custom type lgs2624cDHCPSnoopingPortModeConfigurationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cDHCPSnoopingPortModeConfigurationMode_Type.__name__ = "Integer32"
_Lgs2624cDHCPSnoopingPortModeConfigurationMode_Object = MibTableColumn
lgs2624cDHCPSnoopingPortModeConfigurationMode = _Lgs2624cDHCPSnoopingPortModeConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 1, 2, 1, 2),
    _Lgs2624cDHCPSnoopingPortModeConfigurationMode_Type()
)
lgs2624cDHCPSnoopingPortModeConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingPortModeConfigurationMode.setStatus("current")
_Lgs2624cDHCPSnoopingStatisticsTable_Object = MibTable
lgs2624cDHCPSnoopingStatisticsTable = _Lgs2624cDHCPSnoopingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2)
)
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingStatisticsTable.setStatus("current")
_Lgs2624cDHCPSnoopingStatisticsEntry_Object = MibTableRow
lgs2624cDHCPSnoopingStatisticsEntry = _Lgs2624cDHCPSnoopingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1)
)
lgs2624cDHCPSnoopingStatisticsEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cDHCPSnoopingStatisticsPort"),
)
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingStatisticsEntry.setStatus("current")


class _Lgs2624cDHCPSnoopingStatisticsPort_Type(Integer32):
    """Custom type lgs2624cDHCPSnoopingStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cDHCPSnoopingStatisticsPort_Type.__name__ = "Integer32"
_Lgs2624cDHCPSnoopingStatisticsPort_Object = MibTableColumn
lgs2624cDHCPSnoopingStatisticsPort = _Lgs2624cDHCPSnoopingStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 1),
    _Lgs2624cDHCPSnoopingStatisticsPort_Type()
)
lgs2624cDHCPSnoopingStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingStatisticsPort.setStatus("current")


class _Lgs2624cDHCPSnoopingStatisticsClear_Type(Integer32):
    """Custom type lgs2624cDHCPSnoopingStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cDHCPSnoopingStatisticsClear_Type.__name__ = "Integer32"
_Lgs2624cDHCPSnoopingStatisticsClear_Object = MibTableColumn
lgs2624cDHCPSnoopingStatisticsClear = _Lgs2624cDHCPSnoopingStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 2),
    _Lgs2624cDHCPSnoopingStatisticsClear_Type()
)
lgs2624cDHCPSnoopingStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingStatisticsClear.setStatus("current")
_Lgs2624cDHCPSnoopingRxDiscover_Type = Counter32
_Lgs2624cDHCPSnoopingRxDiscover_Object = MibTableColumn
lgs2624cDHCPSnoopingRxDiscover = _Lgs2624cDHCPSnoopingRxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 3),
    _Lgs2624cDHCPSnoopingRxDiscover_Type()
)
lgs2624cDHCPSnoopingRxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingRxDiscover.setStatus("current")
_Lgs2624cDHCPSnoopingRxOffer_Type = Counter32
_Lgs2624cDHCPSnoopingRxOffer_Object = MibTableColumn
lgs2624cDHCPSnoopingRxOffer = _Lgs2624cDHCPSnoopingRxOffer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 4),
    _Lgs2624cDHCPSnoopingRxOffer_Type()
)
lgs2624cDHCPSnoopingRxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingRxOffer.setStatus("current")
_Lgs2624cDHCPSnoopingRxRequest_Type = Counter32
_Lgs2624cDHCPSnoopingRxRequest_Object = MibTableColumn
lgs2624cDHCPSnoopingRxRequest = _Lgs2624cDHCPSnoopingRxRequest_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 5),
    _Lgs2624cDHCPSnoopingRxRequest_Type()
)
lgs2624cDHCPSnoopingRxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingRxRequest.setStatus("current")
_Lgs2624cDHCPSnoopingRxDecline_Type = Counter32
_Lgs2624cDHCPSnoopingRxDecline_Object = MibTableColumn
lgs2624cDHCPSnoopingRxDecline = _Lgs2624cDHCPSnoopingRxDecline_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 6),
    _Lgs2624cDHCPSnoopingRxDecline_Type()
)
lgs2624cDHCPSnoopingRxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingRxDecline.setStatus("current")
_Lgs2624cDHCPSnoopingRxACK_Type = Counter32
_Lgs2624cDHCPSnoopingRxACK_Object = MibTableColumn
lgs2624cDHCPSnoopingRxACK = _Lgs2624cDHCPSnoopingRxACK_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 7),
    _Lgs2624cDHCPSnoopingRxACK_Type()
)
lgs2624cDHCPSnoopingRxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingRxACK.setStatus("current")
_Lgs2624cDHCPSnoopingRxNAK_Type = Counter32
_Lgs2624cDHCPSnoopingRxNAK_Object = MibTableColumn
lgs2624cDHCPSnoopingRxNAK = _Lgs2624cDHCPSnoopingRxNAK_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 8),
    _Lgs2624cDHCPSnoopingRxNAK_Type()
)
lgs2624cDHCPSnoopingRxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingRxNAK.setStatus("current")
_Lgs2624cDHCPSnoopingRxRelease_Type = Counter32
_Lgs2624cDHCPSnoopingRxRelease_Object = MibTableColumn
lgs2624cDHCPSnoopingRxRelease = _Lgs2624cDHCPSnoopingRxRelease_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 9),
    _Lgs2624cDHCPSnoopingRxRelease_Type()
)
lgs2624cDHCPSnoopingRxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingRxRelease.setStatus("current")
_Lgs2624cDHCPSnoopingRxInform_Type = Counter32
_Lgs2624cDHCPSnoopingRxInform_Object = MibTableColumn
lgs2624cDHCPSnoopingRxInform = _Lgs2624cDHCPSnoopingRxInform_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 10),
    _Lgs2624cDHCPSnoopingRxInform_Type()
)
lgs2624cDHCPSnoopingRxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingRxInform.setStatus("current")
_Lgs2624cDHCPSnoopingRxLeaseQuery_Type = Counter32
_Lgs2624cDHCPSnoopingRxLeaseQuery_Object = MibTableColumn
lgs2624cDHCPSnoopingRxLeaseQuery = _Lgs2624cDHCPSnoopingRxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 11),
    _Lgs2624cDHCPSnoopingRxLeaseQuery_Type()
)
lgs2624cDHCPSnoopingRxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingRxLeaseQuery.setStatus("current")
_Lgs2624cDHCPSnoopingRxLeaseUnassigned_Type = Counter32
_Lgs2624cDHCPSnoopingRxLeaseUnassigned_Object = MibTableColumn
lgs2624cDHCPSnoopingRxLeaseUnassigned = _Lgs2624cDHCPSnoopingRxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 12),
    _Lgs2624cDHCPSnoopingRxLeaseUnassigned_Type()
)
lgs2624cDHCPSnoopingRxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingRxLeaseUnassigned.setStatus("current")
_Lgs2624cDHCPSnoopingRxLeaseUnknown_Type = Counter32
_Lgs2624cDHCPSnoopingRxLeaseUnknown_Object = MibTableColumn
lgs2624cDHCPSnoopingRxLeaseUnknown = _Lgs2624cDHCPSnoopingRxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 13),
    _Lgs2624cDHCPSnoopingRxLeaseUnknown_Type()
)
lgs2624cDHCPSnoopingRxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingRxLeaseUnknown.setStatus("current")
_Lgs2624cDHCPSnoopingRxLeaseActive_Type = Counter32
_Lgs2624cDHCPSnoopingRxLeaseActive_Object = MibTableColumn
lgs2624cDHCPSnoopingRxLeaseActive = _Lgs2624cDHCPSnoopingRxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 14),
    _Lgs2624cDHCPSnoopingRxLeaseActive_Type()
)
lgs2624cDHCPSnoopingRxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingRxLeaseActive.setStatus("current")
_Lgs2624cDHCPSnoopingTxDiscover_Type = Counter32
_Lgs2624cDHCPSnoopingTxDiscover_Object = MibTableColumn
lgs2624cDHCPSnoopingTxDiscover = _Lgs2624cDHCPSnoopingTxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 15),
    _Lgs2624cDHCPSnoopingTxDiscover_Type()
)
lgs2624cDHCPSnoopingTxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingTxDiscover.setStatus("current")
_Lgs2624cDHCPSnoopingTxOffer_Type = Counter32
_Lgs2624cDHCPSnoopingTxOffer_Object = MibTableColumn
lgs2624cDHCPSnoopingTxOffer = _Lgs2624cDHCPSnoopingTxOffer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 16),
    _Lgs2624cDHCPSnoopingTxOffer_Type()
)
lgs2624cDHCPSnoopingTxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingTxOffer.setStatus("current")
_Lgs2624cDHCPSnoopingTxRequest_Type = Counter32
_Lgs2624cDHCPSnoopingTxRequest_Object = MibTableColumn
lgs2624cDHCPSnoopingTxRequest = _Lgs2624cDHCPSnoopingTxRequest_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 17),
    _Lgs2624cDHCPSnoopingTxRequest_Type()
)
lgs2624cDHCPSnoopingTxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingTxRequest.setStatus("current")
_Lgs2624cDHCPSnoopingTxDecline_Type = Counter32
_Lgs2624cDHCPSnoopingTxDecline_Object = MibTableColumn
lgs2624cDHCPSnoopingTxDecline = _Lgs2624cDHCPSnoopingTxDecline_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 18),
    _Lgs2624cDHCPSnoopingTxDecline_Type()
)
lgs2624cDHCPSnoopingTxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingTxDecline.setStatus("current")
_Lgs2624cDHCPSnoopingTxACK_Type = Counter32
_Lgs2624cDHCPSnoopingTxACK_Object = MibTableColumn
lgs2624cDHCPSnoopingTxACK = _Lgs2624cDHCPSnoopingTxACK_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 19),
    _Lgs2624cDHCPSnoopingTxACK_Type()
)
lgs2624cDHCPSnoopingTxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingTxACK.setStatus("current")
_Lgs2624cDHCPSnoopingTxNAK_Type = Counter32
_Lgs2624cDHCPSnoopingTxNAK_Object = MibTableColumn
lgs2624cDHCPSnoopingTxNAK = _Lgs2624cDHCPSnoopingTxNAK_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 20),
    _Lgs2624cDHCPSnoopingTxNAK_Type()
)
lgs2624cDHCPSnoopingTxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingTxNAK.setStatus("current")
_Lgs2624cDHCPSnoopingTxRelease_Type = Counter32
_Lgs2624cDHCPSnoopingTxRelease_Object = MibTableColumn
lgs2624cDHCPSnoopingTxRelease = _Lgs2624cDHCPSnoopingTxRelease_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 21),
    _Lgs2624cDHCPSnoopingTxRelease_Type()
)
lgs2624cDHCPSnoopingTxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingTxRelease.setStatus("current")
_Lgs2624cDHCPSnoopingTxInform_Type = Counter32
_Lgs2624cDHCPSnoopingTxInform_Object = MibTableColumn
lgs2624cDHCPSnoopingTxInform = _Lgs2624cDHCPSnoopingTxInform_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 22),
    _Lgs2624cDHCPSnoopingTxInform_Type()
)
lgs2624cDHCPSnoopingTxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingTxInform.setStatus("current")
_Lgs2624cDHCPSnoopingTxLeaseQuery_Type = Counter32
_Lgs2624cDHCPSnoopingTxLeaseQuery_Object = MibTableColumn
lgs2624cDHCPSnoopingTxLeaseQuery = _Lgs2624cDHCPSnoopingTxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 23),
    _Lgs2624cDHCPSnoopingTxLeaseQuery_Type()
)
lgs2624cDHCPSnoopingTxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingTxLeaseQuery.setStatus("current")
_Lgs2624cDHCPSnoopingTxLeaseUnassigned_Type = Counter32
_Lgs2624cDHCPSnoopingTxLeaseUnassigned_Object = MibTableColumn
lgs2624cDHCPSnoopingTxLeaseUnassigned = _Lgs2624cDHCPSnoopingTxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 24),
    _Lgs2624cDHCPSnoopingTxLeaseUnassigned_Type()
)
lgs2624cDHCPSnoopingTxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingTxLeaseUnassigned.setStatus("current")
_Lgs2624cDHCPSnoopingTxLeaseUnknown_Type = Counter32
_Lgs2624cDHCPSnoopingTxLeaseUnknown_Object = MibTableColumn
lgs2624cDHCPSnoopingTxLeaseUnknown = _Lgs2624cDHCPSnoopingTxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 25),
    _Lgs2624cDHCPSnoopingTxLeaseUnknown_Type()
)
lgs2624cDHCPSnoopingTxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingTxLeaseUnknown.setStatus("current")
_Lgs2624cDHCPSnoopingTxLeaseActive_Type = Counter32
_Lgs2624cDHCPSnoopingTxLeaseActive_Object = MibTableColumn
lgs2624cDHCPSnoopingTxLeaseActive = _Lgs2624cDHCPSnoopingTxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 3, 2, 1, 26),
    _Lgs2624cDHCPSnoopingTxLeaseActive_Type()
)
lgs2624cDHCPSnoopingTxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cDHCPSnoopingTxLeaseActive.setStatus("current")
_Lgs2624cDHCPRelay_ObjectIdentity = ObjectIdentity
lgs2624cDHCPRelay = _Lgs2624cDHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4)
)
_Lgs2624cDHCPRelayConfiguration_ObjectIdentity = ObjectIdentity
lgs2624cDHCPRelayConfiguration = _Lgs2624cDHCPRelayConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 1)
)


class _Lgs2624cDHCPRelayMode_Type(Integer32):
    """Custom type lgs2624cDHCPRelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cDHCPRelayMode_Type.__name__ = "Integer32"
_Lgs2624cDHCPRelayMode_Object = MibScalar
lgs2624cDHCPRelayMode = _Lgs2624cDHCPRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 1, 1),
    _Lgs2624cDHCPRelayMode_Type()
)
lgs2624cDHCPRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cDHCPRelayMode.setStatus("current")
_Lgs2624cDHCPRelayServer_Type = IpAddress
_Lgs2624cDHCPRelayServer_Object = MibScalar
lgs2624cDHCPRelayServer = _Lgs2624cDHCPRelayServer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 1, 2),
    _Lgs2624cDHCPRelayServer_Type()
)
lgs2624cDHCPRelayServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cDHCPRelayServer.setStatus("current")


class _Lgs2624cDHCPRelayInformationMode_Type(Integer32):
    """Custom type lgs2624cDHCPRelayInformationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cDHCPRelayInformationMode_Type.__name__ = "Integer32"
_Lgs2624cDHCPRelayInformationMode_Object = MibScalar
lgs2624cDHCPRelayInformationMode = _Lgs2624cDHCPRelayInformationMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 1, 3),
    _Lgs2624cDHCPRelayInformationMode_Type()
)
lgs2624cDHCPRelayInformationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cDHCPRelayInformationMode.setStatus("current")


class _Lgs2624cDHCPRelayInformationPolicy_Type(Integer32):
    """Custom type lgs2624cDHCPRelayInformationPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2624cDHCPRelayInformationPolicy_Type.__name__ = "Integer32"
_Lgs2624cDHCPRelayInformationPolicy_Object = MibScalar
lgs2624cDHCPRelayInformationPolicy = _Lgs2624cDHCPRelayInformationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 1, 4),
    _Lgs2624cDHCPRelayInformationPolicy_Type()
)
lgs2624cDHCPRelayInformationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cDHCPRelayInformationPolicy.setStatus("current")
_Lgs2624cDHCPRelayStatistics_ObjectIdentity = ObjectIdentity
lgs2624cDHCPRelayStatistics = _Lgs2624cDHCPRelayStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 2)
)
_Lgs2624cDHCPRelayServerStatistics_ObjectIdentity = ObjectIdentity
lgs2624cDHCPRelayServerStatistics = _Lgs2624cDHCPRelayServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 2, 1)
)
_Lgs2624cServerStatTransmitToServer_Type = Counter32
_Lgs2624cServerStatTransmitToServer_Object = MibScalar
lgs2624cServerStatTransmitToServer = _Lgs2624cServerStatTransmitToServer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 2, 1, 1),
    _Lgs2624cServerStatTransmitToServer_Type()
)
lgs2624cServerStatTransmitToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cServerStatTransmitToServer.setStatus("current")
_Lgs2624cServerStatTransmitError_Type = Counter32
_Lgs2624cServerStatTransmitError_Object = MibScalar
lgs2624cServerStatTransmitError = _Lgs2624cServerStatTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 2, 1, 2),
    _Lgs2624cServerStatTransmitError_Type()
)
lgs2624cServerStatTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cServerStatTransmitError.setStatus("current")
_Lgs2624cServerStatReceiveFromServer_Type = Counter32
_Lgs2624cServerStatReceiveFromServer_Object = MibScalar
lgs2624cServerStatReceiveFromServer = _Lgs2624cServerStatReceiveFromServer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 2, 1, 3),
    _Lgs2624cServerStatReceiveFromServer_Type()
)
lgs2624cServerStatReceiveFromServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cServerStatReceiveFromServer.setStatus("current")
_Lgs2624cServerStatReceiveMissingAgentOption_Type = Counter32
_Lgs2624cServerStatReceiveMissingAgentOption_Object = MibScalar
lgs2624cServerStatReceiveMissingAgentOption = _Lgs2624cServerStatReceiveMissingAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 2, 1, 4),
    _Lgs2624cServerStatReceiveMissingAgentOption_Type()
)
lgs2624cServerStatReceiveMissingAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cServerStatReceiveMissingAgentOption.setStatus("current")
_Lgs2624cServerStatReceiveMissingCircuitID_Type = Counter32
_Lgs2624cServerStatReceiveMissingCircuitID_Object = MibScalar
lgs2624cServerStatReceiveMissingCircuitID = _Lgs2624cServerStatReceiveMissingCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 2, 1, 5),
    _Lgs2624cServerStatReceiveMissingCircuitID_Type()
)
lgs2624cServerStatReceiveMissingCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cServerStatReceiveMissingCircuitID.setStatus("current")
_Lgs2624cServerStatReceiveMissingRemoteID_Type = Counter32
_Lgs2624cServerStatReceiveMissingRemoteID_Object = MibScalar
lgs2624cServerStatReceiveMissingRemoteID = _Lgs2624cServerStatReceiveMissingRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 2, 1, 6),
    _Lgs2624cServerStatReceiveMissingRemoteID_Type()
)
lgs2624cServerStatReceiveMissingRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cServerStatReceiveMissingRemoteID.setStatus("current")
_Lgs2624cServerStatReceiveBadCircuitID_Type = Counter32
_Lgs2624cServerStatReceiveBadCircuitID_Object = MibScalar
lgs2624cServerStatReceiveBadCircuitID = _Lgs2624cServerStatReceiveBadCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 2, 1, 7),
    _Lgs2624cServerStatReceiveBadCircuitID_Type()
)
lgs2624cServerStatReceiveBadCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cServerStatReceiveBadCircuitID.setStatus("current")
_Lgs2624cServerStatReceiveBadRemoteID_Type = Counter32
_Lgs2624cServerStatReceiveBadRemoteID_Object = MibScalar
lgs2624cServerStatReceiveBadRemoteID = _Lgs2624cServerStatReceiveBadRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 2, 1, 8),
    _Lgs2624cServerStatReceiveBadRemoteID_Type()
)
lgs2624cServerStatReceiveBadRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cServerStatReceiveBadRemoteID.setStatus("current")
_Lgs2624cDHCPRelayClientStatistics_ObjectIdentity = ObjectIdentity
lgs2624cDHCPRelayClientStatistics = _Lgs2624cDHCPRelayClientStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 2, 2)
)
_Lgs2624cClientStatTransmitToClient_Type = Counter32
_Lgs2624cClientStatTransmitToClient_Object = MibScalar
lgs2624cClientStatTransmitToClient = _Lgs2624cClientStatTransmitToClient_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 2, 2, 1),
    _Lgs2624cClientStatTransmitToClient_Type()
)
lgs2624cClientStatTransmitToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cClientStatTransmitToClient.setStatus("current")
_Lgs2624cClientStatTransmitError_Type = Counter32
_Lgs2624cClientStatTransmitError_Object = MibScalar
lgs2624cClientStatTransmitError = _Lgs2624cClientStatTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 2, 2, 2),
    _Lgs2624cClientStatTransmitError_Type()
)
lgs2624cClientStatTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cClientStatTransmitError.setStatus("current")
_Lgs2624cClientStatReceivefromClient_Type = Counter32
_Lgs2624cClientStatReceivefromClient_Object = MibScalar
lgs2624cClientStatReceivefromClient = _Lgs2624cClientStatReceivefromClient_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 2, 2, 3),
    _Lgs2624cClientStatReceivefromClient_Type()
)
lgs2624cClientStatReceivefromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cClientStatReceivefromClient.setStatus("current")
_Lgs2624cClientStatReceiveAgentOption_Type = Counter32
_Lgs2624cClientStatReceiveAgentOption_Object = MibScalar
lgs2624cClientStatReceiveAgentOption = _Lgs2624cClientStatReceiveAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 2, 2, 4),
    _Lgs2624cClientStatReceiveAgentOption_Type()
)
lgs2624cClientStatReceiveAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cClientStatReceiveAgentOption.setStatus("current")
_Lgs2624cClientStatReplaceAgentOption_Type = Counter32
_Lgs2624cClientStatReplaceAgentOption_Object = MibScalar
lgs2624cClientStatReplaceAgentOption = _Lgs2624cClientStatReplaceAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 2, 2, 5),
    _Lgs2624cClientStatReplaceAgentOption_Type()
)
lgs2624cClientStatReplaceAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cClientStatReplaceAgentOption.setStatus("current")
_Lgs2624cClientStatKeepAgentOption_Type = Counter32
_Lgs2624cClientStatKeepAgentOption_Object = MibScalar
lgs2624cClientStatKeepAgentOption = _Lgs2624cClientStatKeepAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 2, 2, 6),
    _Lgs2624cClientStatKeepAgentOption_Type()
)
lgs2624cClientStatKeepAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cClientStatKeepAgentOption.setStatus("current")
_Lgs2624cClientStatDropAgentOption_Type = Counter32
_Lgs2624cClientStatDropAgentOption_Object = MibScalar
lgs2624cClientStatDropAgentOption = _Lgs2624cClientStatDropAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 4, 2, 2, 7),
    _Lgs2624cClientStatDropAgentOption_Type()
)
lgs2624cClientStatDropAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cClientStatDropAgentOption.setStatus("current")
_Lgs2624cPortSecurity_ObjectIdentity = ObjectIdentity
lgs2624cPortSecurity = _Lgs2624cPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5)
)
_Lgs2624cPortSecLimitCtrl_ObjectIdentity = ObjectIdentity
lgs2624cPortSecLimitCtrl = _Lgs2624cPortSecLimitCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 1)
)
_Lgs2624cPortSecLimitCtrlSystemConf_ObjectIdentity = ObjectIdentity
lgs2624cPortSecLimitCtrlSystemConf = _Lgs2624cPortSecLimitCtrlSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 1, 1)
)


class _Lgs2624cPortSecurityMode_Type(Integer32):
    """Custom type lgs2624cPortSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cPortSecurityMode_Type.__name__ = "Integer32"
_Lgs2624cPortSecurityMode_Object = MibScalar
lgs2624cPortSecurityMode = _Lgs2624cPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 1, 1, 1),
    _Lgs2624cPortSecurityMode_Type()
)
lgs2624cPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortSecurityMode.setStatus("current")


class _Lgs2624cPortSecurityAging_Type(Integer32):
    """Custom type lgs2624cPortSecurityAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cPortSecurityAging_Type.__name__ = "Integer32"
_Lgs2624cPortSecurityAging_Object = MibScalar
lgs2624cPortSecurityAging = _Lgs2624cPortSecurityAging_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 1, 1, 2),
    _Lgs2624cPortSecurityAging_Type()
)
lgs2624cPortSecurityAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortSecurityAging.setStatus("current")


class _Lgs2624cPortSecurityAgingPeriod_Type(Integer32):
    """Custom type lgs2624cPortSecurityAgingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000000),
    )


_Lgs2624cPortSecurityAgingPeriod_Type.__name__ = "Integer32"
_Lgs2624cPortSecurityAgingPeriod_Object = MibScalar
lgs2624cPortSecurityAgingPeriod = _Lgs2624cPortSecurityAgingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 1, 1, 3),
    _Lgs2624cPortSecurityAgingPeriod_Type()
)
lgs2624cPortSecurityAgingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortSecurityAgingPeriod.setStatus("current")
_Lgs2624cPortSecLimitCtrlTable_Object = MibTable
lgs2624cPortSecLimitCtrlTable = _Lgs2624cPortSecLimitCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    lgs2624cPortSecLimitCtrlTable.setStatus("current")
_Lgs2624cPortSecLimitCtrlEntry_Object = MibTableRow
lgs2624cPortSecLimitCtrlEntry = _Lgs2624cPortSecLimitCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 1, 2, 1)
)
lgs2624cPortSecLimitCtrlEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cPortSecLimitCtrlPort"),
)
if mibBuilder.loadTexts:
    lgs2624cPortSecLimitCtrlEntry.setStatus("current")


class _Lgs2624cPortSecLimitCtrlPort_Type(Integer32):
    """Custom type lgs2624cPortSecLimitCtrlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cPortSecLimitCtrlPort_Type.__name__ = "Integer32"
_Lgs2624cPortSecLimitCtrlPort_Object = MibTableColumn
lgs2624cPortSecLimitCtrlPort = _Lgs2624cPortSecLimitCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 1, 2, 1, 1),
    _Lgs2624cPortSecLimitCtrlPort_Type()
)
lgs2624cPortSecLimitCtrlPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cPortSecLimitCtrlPort.setStatus("current")


class _Lgs2624cPortSecLimitCtrlPortMode_Type(Integer32):
    """Custom type lgs2624cPortSecLimitCtrlPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cPortSecLimitCtrlPortMode_Type.__name__ = "Integer32"
_Lgs2624cPortSecLimitCtrlPortMode_Object = MibTableColumn
lgs2624cPortSecLimitCtrlPortMode = _Lgs2624cPortSecLimitCtrlPortMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 1, 2, 1, 2),
    _Lgs2624cPortSecLimitCtrlPortMode_Type()
)
lgs2624cPortSecLimitCtrlPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortSecLimitCtrlPortMode.setStatus("current")


class _Lgs2624cPortSecLimitCtrlPortLimit_Type(Integer32):
    """Custom type lgs2624cPortSecLimitCtrlPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Lgs2624cPortSecLimitCtrlPortLimit_Type.__name__ = "Integer32"
_Lgs2624cPortSecLimitCtrlPortLimit_Object = MibTableColumn
lgs2624cPortSecLimitCtrlPortLimit = _Lgs2624cPortSecLimitCtrlPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 1, 2, 1, 3),
    _Lgs2624cPortSecLimitCtrlPortLimit_Type()
)
lgs2624cPortSecLimitCtrlPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortSecLimitCtrlPortLimit.setStatus("current")


class _Lgs2624cPortSecLimitCtrlPortAction_Type(Integer32):
    """Custom type lgs2624cPortSecLimitCtrlPortAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Lgs2624cPortSecLimitCtrlPortAction_Type.__name__ = "Integer32"
_Lgs2624cPortSecLimitCtrlPortAction_Object = MibTableColumn
lgs2624cPortSecLimitCtrlPortAction = _Lgs2624cPortSecLimitCtrlPortAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 1, 2, 1, 4),
    _Lgs2624cPortSecLimitCtrlPortAction_Type()
)
lgs2624cPortSecLimitCtrlPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortSecLimitCtrlPortAction.setStatus("current")
_Lgs2624cPortSecLimitCtrlPortState_Type = DisplayString
_Lgs2624cPortSecLimitCtrlPortState_Object = MibTableColumn
lgs2624cPortSecLimitCtrlPortState = _Lgs2624cPortSecLimitCtrlPortState_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 1, 2, 1, 5),
    _Lgs2624cPortSecLimitCtrlPortState_Type()
)
lgs2624cPortSecLimitCtrlPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortSecLimitCtrlPortState.setStatus("current")


class _Lgs2624cPortSecLimitCtrlPortReOpen_Type(Integer32):
    """Custom type lgs2624cPortSecLimitCtrlPortReOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cPortSecLimitCtrlPortReOpen_Type.__name__ = "Integer32"
_Lgs2624cPortSecLimitCtrlPortReOpen_Object = MibTableColumn
lgs2624cPortSecLimitCtrlPortReOpen = _Lgs2624cPortSecLimitCtrlPortReOpen_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 1, 2, 1, 6),
    _Lgs2624cPortSecLimitCtrlPortReOpen_Type()
)
lgs2624cPortSecLimitCtrlPortReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortSecLimitCtrlPortReOpen.setStatus("current")
_Lgs2624cPortSecSwitchStatusTable_Object = MibTable
lgs2624cPortSecSwitchStatusTable = _Lgs2624cPortSecSwitchStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 2)
)
if mibBuilder.loadTexts:
    lgs2624cPortSecSwitchStatusTable.setStatus("current")
_Lgs2624cPortSecSwitchStatusEntry_Object = MibTableRow
lgs2624cPortSecSwitchStatusEntry = _Lgs2624cPortSecSwitchStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 2, 1)
)
lgs2624cPortSecSwitchStatusEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cPortSecSwitchStatusPort"),
)
if mibBuilder.loadTexts:
    lgs2624cPortSecSwitchStatusEntry.setStatus("current")


class _Lgs2624cPortSecSwitchStatusPort_Type(Integer32):
    """Custom type lgs2624cPortSecSwitchStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cPortSecSwitchStatusPort_Type.__name__ = "Integer32"
_Lgs2624cPortSecSwitchStatusPort_Object = MibTableColumn
lgs2624cPortSecSwitchStatusPort = _Lgs2624cPortSecSwitchStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 2, 1, 1),
    _Lgs2624cPortSecSwitchStatusPort_Type()
)
lgs2624cPortSecSwitchStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cPortSecSwitchStatusPort.setStatus("current")
_Lgs2624cPortSecSwitchStatusUsers_Type = DisplayString
_Lgs2624cPortSecSwitchStatusUsers_Object = MibTableColumn
lgs2624cPortSecSwitchStatusUsers = _Lgs2624cPortSecSwitchStatusUsers_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 2, 1, 2),
    _Lgs2624cPortSecSwitchStatusUsers_Type()
)
lgs2624cPortSecSwitchStatusUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortSecSwitchStatusUsers.setStatus("current")
_Lgs2624cPortSecSwitchStatusState_Type = DisplayString
_Lgs2624cPortSecSwitchStatusState_Object = MibTableColumn
lgs2624cPortSecSwitchStatusState = _Lgs2624cPortSecSwitchStatusState_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 2, 1, 3),
    _Lgs2624cPortSecSwitchStatusState_Type()
)
lgs2624cPortSecSwitchStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortSecSwitchStatusState.setStatus("current")


class _Lgs2624cPortSecSwitchStatusMACCountCurrent_Type(Integer32):
    """Custom type lgs2624cPortSecSwitchStatusMACCountCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cPortSecSwitchStatusMACCountCurrent_Type.__name__ = "Integer32"
_Lgs2624cPortSecSwitchStatusMACCountCurrent_Object = MibTableColumn
lgs2624cPortSecSwitchStatusMACCountCurrent = _Lgs2624cPortSecSwitchStatusMACCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 2, 1, 4),
    _Lgs2624cPortSecSwitchStatusMACCountCurrent_Type()
)
lgs2624cPortSecSwitchStatusMACCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortSecSwitchStatusMACCountCurrent.setStatus("current")


class _Lgs2624cPortSecSwitchStatusMACCountLimit_Type(Integer32):
    """Custom type lgs2624cPortSecSwitchStatusMACCountLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cPortSecSwitchStatusMACCountLimit_Type.__name__ = "Integer32"
_Lgs2624cPortSecSwitchStatusMACCountLimit_Object = MibTableColumn
lgs2624cPortSecSwitchStatusMACCountLimit = _Lgs2624cPortSecSwitchStatusMACCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 2, 1, 5),
    _Lgs2624cPortSecSwitchStatusMACCountLimit_Type()
)
lgs2624cPortSecSwitchStatusMACCountLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortSecSwitchStatusMACCountLimit.setStatus("current")
_Lgs2624cPortSecPortStatus_ObjectIdentity = ObjectIdentity
lgs2624cPortSecPortStatus = _Lgs2624cPortSecPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 3)
)


class _Lgs2624cPortSecPortStatusPort_Type(Integer32):
    """Custom type lgs2624cPortSecPortStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cPortSecPortStatusPort_Type.__name__ = "Integer32"
_Lgs2624cPortSecPortStatusPort_Object = MibScalar
lgs2624cPortSecPortStatusPort = _Lgs2624cPortSecPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 3, 1),
    _Lgs2624cPortSecPortStatusPort_Type()
)
lgs2624cPortSecPortStatusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPortSecPortStatusPort.setStatus("current")
_Lgs2624cPortSecPortStatusTable_Object = MibTable
lgs2624cPortSecPortStatusTable = _Lgs2624cPortSecPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 3, 2)
)
if mibBuilder.loadTexts:
    lgs2624cPortSecPortStatusTable.setStatus("current")
_Lgs2624cPortSecPortStatusEntry_Object = MibTableRow
lgs2624cPortSecPortStatusEntry = _Lgs2624cPortSecPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 3, 2, 1)
)
lgs2624cPortSecPortStatusEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cPortSecPortStatusIndex"),
)
if mibBuilder.loadTexts:
    lgs2624cPortSecPortStatusEntry.setStatus("current")


class _Lgs2624cPortSecPortStatusIndex_Type(Integer32):
    """Custom type lgs2624cPortSecPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cPortSecPortStatusIndex_Type.__name__ = "Integer32"
_Lgs2624cPortSecPortStatusIndex_Object = MibTableColumn
lgs2624cPortSecPortStatusIndex = _Lgs2624cPortSecPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 3, 2, 1, 1),
    _Lgs2624cPortSecPortStatusIndex_Type()
)
lgs2624cPortSecPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cPortSecPortStatusIndex.setStatus("current")
_Lgs2624cPortSecPortStatusMACAddress_Type = MacAddress
_Lgs2624cPortSecPortStatusMACAddress_Object = MibTableColumn
lgs2624cPortSecPortStatusMACAddress = _Lgs2624cPortSecPortStatusMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 3, 2, 1, 2),
    _Lgs2624cPortSecPortStatusMACAddress_Type()
)
lgs2624cPortSecPortStatusMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortSecPortStatusMACAddress.setStatus("current")


class _Lgs2624cPortSecPortStatusVLANId_Type(Integer32):
    """Custom type lgs2624cPortSecPortStatusVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2624cPortSecPortStatusVLANId_Type.__name__ = "Integer32"
_Lgs2624cPortSecPortStatusVLANId_Object = MibTableColumn
lgs2624cPortSecPortStatusVLANId = _Lgs2624cPortSecPortStatusVLANId_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 3, 2, 1, 3),
    _Lgs2624cPortSecPortStatusVLANId_Type()
)
lgs2624cPortSecPortStatusVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortSecPortStatusVLANId.setStatus("current")
_Lgs2624cPortSecPortStatusState_Type = DisplayString
_Lgs2624cPortSecPortStatusState_Object = MibTableColumn
lgs2624cPortSecPortStatusState = _Lgs2624cPortSecPortStatusState_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 3, 2, 1, 4),
    _Lgs2624cPortSecPortStatusState_Type()
)
lgs2624cPortSecPortStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortSecPortStatusState.setStatus("current")
_Lgs2624cPortSecPortStatusTimeOfAddition_Type = DisplayString
_Lgs2624cPortSecPortStatusTimeOfAddition_Object = MibTableColumn
lgs2624cPortSecPortStatusTimeOfAddition = _Lgs2624cPortSecPortStatusTimeOfAddition_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 3, 2, 1, 5),
    _Lgs2624cPortSecPortStatusTimeOfAddition_Type()
)
lgs2624cPortSecPortStatusTimeOfAddition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortSecPortStatusTimeOfAddition.setStatus("current")
_Lgs2624cPortSecPortStatusAgeAndHold_Type = DisplayString
_Lgs2624cPortSecPortStatusAgeAndHold_Object = MibTableColumn
lgs2624cPortSecPortStatusAgeAndHold = _Lgs2624cPortSecPortStatusAgeAndHold_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 5, 3, 2, 1, 6),
    _Lgs2624cPortSecPortStatusAgeAndHold_Type()
)
lgs2624cPortSecPortStatusAgeAndHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPortSecPortStatusAgeAndHold.setStatus("current")
_Lgs2624cAccessManagement_ObjectIdentity = ObjectIdentity
lgs2624cAccessManagement = _Lgs2624cAccessManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6)
)
_Lgs2624cAccessMgtConf_ObjectIdentity = ObjectIdentity
lgs2624cAccessMgtConf = _Lgs2624cAccessMgtConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 1)
)


class _Lgs2624cAccessMgtConfMode_Type(Integer32):
    """Custom type lgs2624cAccessMgtConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cAccessMgtConfMode_Type.__name__ = "Integer32"
_Lgs2624cAccessMgtConfMode_Object = MibScalar
lgs2624cAccessMgtConfMode = _Lgs2624cAccessMgtConfMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 1, 1),
    _Lgs2624cAccessMgtConfMode_Type()
)
lgs2624cAccessMgtConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cAccessMgtConfMode.setStatus("current")


class _Lgs2624cAccessMgtConfCreate_Type(Integer32):
    """Custom type lgs2624cAccessMgtConfCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cAccessMgtConfCreate_Type.__name__ = "Integer32"
_Lgs2624cAccessMgtConfCreate_Object = MibScalar
lgs2624cAccessMgtConfCreate = _Lgs2624cAccessMgtConfCreate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 1, 2),
    _Lgs2624cAccessMgtConfCreate_Type()
)
lgs2624cAccessMgtConfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cAccessMgtConfCreate.setStatus("current")
_Lgs2624cAccessMgtConfTable_Object = MibTable
lgs2624cAccessMgtConfTable = _Lgs2624cAccessMgtConfTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 1, 3)
)
if mibBuilder.loadTexts:
    lgs2624cAccessMgtConfTable.setStatus("current")
_Lgs2624cAccessMgtConfEntry_Object = MibTableRow
lgs2624cAccessMgtConfEntry = _Lgs2624cAccessMgtConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 1, 3, 1)
)
lgs2624cAccessMgtConfEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cAccessMgtIndex"),
)
if mibBuilder.loadTexts:
    lgs2624cAccessMgtConfEntry.setStatus("current")


class _Lgs2624cAccessMgtIndex_Type(Integer32):
    """Custom type lgs2624cAccessMgtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Lgs2624cAccessMgtIndex_Type.__name__ = "Integer32"
_Lgs2624cAccessMgtIndex_Object = MibTableColumn
lgs2624cAccessMgtIndex = _Lgs2624cAccessMgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 1, 3, 1, 1),
    _Lgs2624cAccessMgtIndex_Type()
)
lgs2624cAccessMgtIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cAccessMgtIndex.setStatus("current")


class _Lgs2624cAccessMgtAddresstype_Type(Integer32):
    """Custom type lgs2624cAccessMgtAddresstype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cAccessMgtAddresstype_Type.__name__ = "Integer32"
_Lgs2624cAccessMgtAddresstype_Object = MibTableColumn
lgs2624cAccessMgtAddresstype = _Lgs2624cAccessMgtAddresstype_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 1, 3, 1, 2),
    _Lgs2624cAccessMgtAddresstype_Type()
)
lgs2624cAccessMgtAddresstype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cAccessMgtAddresstype.setStatus("current")
_Lgs2624cAccessMgtStartIpAddress_Type = DisplayString
_Lgs2624cAccessMgtStartIpAddress_Object = MibTableColumn
lgs2624cAccessMgtStartIpAddress = _Lgs2624cAccessMgtStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 1, 3, 1, 3),
    _Lgs2624cAccessMgtStartIpAddress_Type()
)
lgs2624cAccessMgtStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cAccessMgtStartIpAddress.setStatus("current")
_Lgs2624cAccessMgtEndIpAddress_Type = DisplayString
_Lgs2624cAccessMgtEndIpAddress_Object = MibTableColumn
lgs2624cAccessMgtEndIpAddress = _Lgs2624cAccessMgtEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 1, 3, 1, 4),
    _Lgs2624cAccessMgtEndIpAddress_Type()
)
lgs2624cAccessMgtEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cAccessMgtEndIpAddress.setStatus("current")


class _Lgs2624cAccessMgtHttpHttps_Type(Integer32):
    """Custom type lgs2624cAccessMgtHttpHttps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cAccessMgtHttpHttps_Type.__name__ = "Integer32"
_Lgs2624cAccessMgtHttpHttps_Object = MibTableColumn
lgs2624cAccessMgtHttpHttps = _Lgs2624cAccessMgtHttpHttps_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 1, 3, 1, 5),
    _Lgs2624cAccessMgtHttpHttps_Type()
)
lgs2624cAccessMgtHttpHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cAccessMgtHttpHttps.setStatus("current")


class _Lgs2624cAccessMgtSNMP_Type(Integer32):
    """Custom type lgs2624cAccessMgtSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cAccessMgtSNMP_Type.__name__ = "Integer32"
_Lgs2624cAccessMgtSNMP_Object = MibTableColumn
lgs2624cAccessMgtSNMP = _Lgs2624cAccessMgtSNMP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 1, 3, 1, 6),
    _Lgs2624cAccessMgtSNMP_Type()
)
lgs2624cAccessMgtSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cAccessMgtSNMP.setStatus("current")


class _Lgs2624cAccessMgtTelnetSSH_Type(Integer32):
    """Custom type lgs2624cAccessMgtTelnetSSH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cAccessMgtTelnetSSH_Type.__name__ = "Integer32"
_Lgs2624cAccessMgtTelnetSSH_Object = MibTableColumn
lgs2624cAccessMgtTelnetSSH = _Lgs2624cAccessMgtTelnetSSH_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 1, 3, 1, 7),
    _Lgs2624cAccessMgtTelnetSSH_Type()
)
lgs2624cAccessMgtTelnetSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cAccessMgtTelnetSSH.setStatus("current")


class _Lgs2624cAccessMgtRowStatus_Type(Integer32):
    """Custom type lgs2624cAccessMgtRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Lgs2624cAccessMgtRowStatus_Type.__name__ = "Integer32"
_Lgs2624cAccessMgtRowStatus_Object = MibTableColumn
lgs2624cAccessMgtRowStatus = _Lgs2624cAccessMgtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 1, 3, 1, 8),
    _Lgs2624cAccessMgtRowStatus_Type()
)
lgs2624cAccessMgtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cAccessMgtRowStatus.setStatus("current")
_Lgs2624cAccessMgtStatistics_ObjectIdentity = ObjectIdentity
lgs2624cAccessMgtStatistics = _Lgs2624cAccessMgtStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 2)
)
_Lgs2624cHttpReceivedPkts_Type = Counter32
_Lgs2624cHttpReceivedPkts_Object = MibScalar
lgs2624cHttpReceivedPkts = _Lgs2624cHttpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 2, 1),
    _Lgs2624cHttpReceivedPkts_Type()
)
lgs2624cHttpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cHttpReceivedPkts.setStatus("current")
_Lgs2624cHttpAllowedPkts_Type = Counter32
_Lgs2624cHttpAllowedPkts_Object = MibScalar
lgs2624cHttpAllowedPkts = _Lgs2624cHttpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 2, 2),
    _Lgs2624cHttpAllowedPkts_Type()
)
lgs2624cHttpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cHttpAllowedPkts.setStatus("current")
_Lgs2624cHttpDiscardedPkts_Type = Counter32
_Lgs2624cHttpDiscardedPkts_Object = MibScalar
lgs2624cHttpDiscardedPkts = _Lgs2624cHttpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 2, 3),
    _Lgs2624cHttpDiscardedPkts_Type()
)
lgs2624cHttpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cHttpDiscardedPkts.setStatus("current")
_Lgs2624cHttpsReceivedPkts_Type = Counter32
_Lgs2624cHttpsReceivedPkts_Object = MibScalar
lgs2624cHttpsReceivedPkts = _Lgs2624cHttpsReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 2, 4),
    _Lgs2624cHttpsReceivedPkts_Type()
)
lgs2624cHttpsReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cHttpsReceivedPkts.setStatus("current")
_Lgs2624cHttpsAllowedPkts_Type = Counter32
_Lgs2624cHttpsAllowedPkts_Object = MibScalar
lgs2624cHttpsAllowedPkts = _Lgs2624cHttpsAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 2, 5),
    _Lgs2624cHttpsAllowedPkts_Type()
)
lgs2624cHttpsAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cHttpsAllowedPkts.setStatus("current")
_Lgs2624cHttpsDiscardedPkts_Type = Counter32
_Lgs2624cHttpsDiscardedPkts_Object = MibScalar
lgs2624cHttpsDiscardedPkts = _Lgs2624cHttpsDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 2, 6),
    _Lgs2624cHttpsDiscardedPkts_Type()
)
lgs2624cHttpsDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cHttpsDiscardedPkts.setStatus("current")
_Lgs2624cSnmpReceivedPkts_Type = Counter32
_Lgs2624cSnmpReceivedPkts_Object = MibScalar
lgs2624cSnmpReceivedPkts = _Lgs2624cSnmpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 2, 7),
    _Lgs2624cSnmpReceivedPkts_Type()
)
lgs2624cSnmpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSnmpReceivedPkts.setStatus("current")
_Lgs2624cSnmpAllowedPkts_Type = Counter32
_Lgs2624cSnmpAllowedPkts_Object = MibScalar
lgs2624cSnmpAllowedPkts = _Lgs2624cSnmpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 2, 8),
    _Lgs2624cSnmpAllowedPkts_Type()
)
lgs2624cSnmpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSnmpAllowedPkts.setStatus("current")
_Lgs2624cSnmpDiscardedPkts_Type = Counter32
_Lgs2624cSnmpDiscardedPkts_Object = MibScalar
lgs2624cSnmpDiscardedPkts = _Lgs2624cSnmpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 2, 9),
    _Lgs2624cSnmpDiscardedPkts_Type()
)
lgs2624cSnmpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSnmpDiscardedPkts.setStatus("current")
_Lgs2624cTelnetReceivedPkts_Type = Counter32
_Lgs2624cTelnetReceivedPkts_Object = MibScalar
lgs2624cTelnetReceivedPkts = _Lgs2624cTelnetReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 2, 10),
    _Lgs2624cTelnetReceivedPkts_Type()
)
lgs2624cTelnetReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cTelnetReceivedPkts.setStatus("current")
_Lgs2624cTelnetAllowedPkts_Type = Counter32
_Lgs2624cTelnetAllowedPkts_Object = MibScalar
lgs2624cTelnetAllowedPkts = _Lgs2624cTelnetAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 2, 11),
    _Lgs2624cTelnetAllowedPkts_Type()
)
lgs2624cTelnetAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cTelnetAllowedPkts.setStatus("current")
_Lgs2624cTelnetDiscardedPkts_Type = Counter32
_Lgs2624cTelnetDiscardedPkts_Object = MibScalar
lgs2624cTelnetDiscardedPkts = _Lgs2624cTelnetDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 2, 12),
    _Lgs2624cTelnetDiscardedPkts_Type()
)
lgs2624cTelnetDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cTelnetDiscardedPkts.setStatus("current")
_Lgs2624cSSHReceivedPkts_Type = Counter32
_Lgs2624cSSHReceivedPkts_Object = MibScalar
lgs2624cSSHReceivedPkts = _Lgs2624cSSHReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 2, 13),
    _Lgs2624cSSHReceivedPkts_Type()
)
lgs2624cSSHReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSSHReceivedPkts.setStatus("current")
_Lgs2624cSSHAllowedPkts_Type = Counter32
_Lgs2624cSSHAllowedPkts_Object = MibScalar
lgs2624cSSHAllowedPkts = _Lgs2624cSSHAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 2, 14),
    _Lgs2624cSSHAllowedPkts_Type()
)
lgs2624cSSHAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSSHAllowedPkts.setStatus("current")
_Lgs2624cSSHDiscardedPkts_Type = Counter32
_Lgs2624cSSHDiscardedPkts_Object = MibScalar
lgs2624cSSHDiscardedPkts = _Lgs2624cSSHDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 2, 15),
    _Lgs2624cSSHDiscardedPkts_Type()
)
lgs2624cSSHDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cSSHDiscardedPkts.setStatus("current")


class _Lgs2624cAccessMgtStatisticsClearAll_Type(Integer32):
    """Custom type lgs2624cAccessMgtStatisticsClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cAccessMgtStatisticsClearAll_Type.__name__ = "Integer32"
_Lgs2624cAccessMgtStatisticsClearAll_Object = MibScalar
lgs2624cAccessMgtStatisticsClearAll = _Lgs2624cAccessMgtStatisticsClearAll_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 6, 2, 16),
    _Lgs2624cAccessMgtStatisticsClearAll_Type()
)
lgs2624cAccessMgtStatisticsClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cAccessMgtStatisticsClearAll.setStatus("current")
_Lgs2624cSSH_ObjectIdentity = ObjectIdentity
lgs2624cSSH = _Lgs2624cSSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 7)
)


class _Lgs2624cSSHMode_Type(Integer32):
    """Custom type lgs2624cSSHMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cSSHMode_Type.__name__ = "Integer32"
_Lgs2624cSSHMode_Object = MibScalar
lgs2624cSSHMode = _Lgs2624cSSHMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 7, 1),
    _Lgs2624cSSHMode_Type()
)
lgs2624cSSHMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSSHMode.setStatus("current")
_Lgs2624cHTTPS_ObjectIdentity = ObjectIdentity
lgs2624cHTTPS = _Lgs2624cHTTPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 8)
)


class _Lgs2624cHTTPSMode_Type(Integer32):
    """Custom type lgs2624cHTTPSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cHTTPSMode_Type.__name__ = "Integer32"
_Lgs2624cHTTPSMode_Object = MibScalar
lgs2624cHTTPSMode = _Lgs2624cHTTPSMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 8, 1),
    _Lgs2624cHTTPSMode_Type()
)
lgs2624cHTTPSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cHTTPSMode.setStatus("current")


class _Lgs2624cHTTPSAutoRedirect_Type(Integer32):
    """Custom type lgs2624cHTTPSAutoRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cHTTPSAutoRedirect_Type.__name__ = "Integer32"
_Lgs2624cHTTPSAutoRedirect_Object = MibScalar
lgs2624cHTTPSAutoRedirect = _Lgs2624cHTTPSAutoRedirect_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 8, 2),
    _Lgs2624cHTTPSAutoRedirect_Type()
)
lgs2624cHTTPSAutoRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cHTTPSAutoRedirect.setStatus("current")
_Lgs2624cAuthMethod_ObjectIdentity = ObjectIdentity
lgs2624cAuthMethod = _Lgs2624cAuthMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 9)
)


class _Lgs2624cConsoleAuthMethod_Type(Integer32):
    """Custom type lgs2624cConsoleAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Lgs2624cConsoleAuthMethod_Type.__name__ = "Integer32"
_Lgs2624cConsoleAuthMethod_Object = MibScalar
lgs2624cConsoleAuthMethod = _Lgs2624cConsoleAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 9, 1),
    _Lgs2624cConsoleAuthMethod_Type()
)
lgs2624cConsoleAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cConsoleAuthMethod.setStatus("current")


class _Lgs2624cConsoleFallback_Type(Integer32):
    """Custom type lgs2624cConsoleFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cConsoleFallback_Type.__name__ = "Integer32"
_Lgs2624cConsoleFallback_Object = MibScalar
lgs2624cConsoleFallback = _Lgs2624cConsoleFallback_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 9, 2),
    _Lgs2624cConsoleFallback_Type()
)
lgs2624cConsoleFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cConsoleFallback.setStatus("current")


class _Lgs2624cTelnetAuthMethod_Type(Integer32):
    """Custom type lgs2624cTelnetAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Lgs2624cTelnetAuthMethod_Type.__name__ = "Integer32"
_Lgs2624cTelnetAuthMethod_Object = MibScalar
lgs2624cTelnetAuthMethod = _Lgs2624cTelnetAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 9, 3),
    _Lgs2624cTelnetAuthMethod_Type()
)
lgs2624cTelnetAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTelnetAuthMethod.setStatus("current")


class _Lgs2624cTelnetFallback_Type(Integer32):
    """Custom type lgs2624cTelnetFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cTelnetFallback_Type.__name__ = "Integer32"
_Lgs2624cTelnetFallback_Object = MibScalar
lgs2624cTelnetFallback = _Lgs2624cTelnetFallback_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 9, 4),
    _Lgs2624cTelnetFallback_Type()
)
lgs2624cTelnetFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cTelnetFallback.setStatus("current")


class _Lgs2624cSshAuthMethod_Type(Integer32):
    """Custom type lgs2624cSshAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Lgs2624cSshAuthMethod_Type.__name__ = "Integer32"
_Lgs2624cSshAuthMethod_Object = MibScalar
lgs2624cSshAuthMethod = _Lgs2624cSshAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 9, 5),
    _Lgs2624cSshAuthMethod_Type()
)
lgs2624cSshAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSshAuthMethod.setStatus("current")


class _Lgs2624cSshFallback_Type(Integer32):
    """Custom type lgs2624cSshFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cSshFallback_Type.__name__ = "Integer32"
_Lgs2624cSshFallback_Object = MibScalar
lgs2624cSshFallback = _Lgs2624cSshFallback_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 9, 6),
    _Lgs2624cSshFallback_Type()
)
lgs2624cSshFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSshFallback.setStatus("current")


class _Lgs2624cWebAuthMethod_Type(Integer32):
    """Custom type lgs2624cWebAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Lgs2624cWebAuthMethod_Type.__name__ = "Integer32"
_Lgs2624cWebAuthMethod_Object = MibScalar
lgs2624cWebAuthMethod = _Lgs2624cWebAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 9, 7),
    _Lgs2624cWebAuthMethod_Type()
)
lgs2624cWebAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cWebAuthMethod.setStatus("current")


class _Lgs2624cWebFallback_Type(Integer32):
    """Custom type lgs2624cWebFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cWebFallback_Type.__name__ = "Integer32"
_Lgs2624cWebFallback_Object = MibScalar
lgs2624cWebFallback = _Lgs2624cWebFallback_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 3, 9, 8),
    _Lgs2624cWebFallback_Type()
)
lgs2624cWebFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cWebFallback.setStatus("current")
_Lgs2624cMaintenance_ObjectIdentity = ObjectIdentity
lgs2624cMaintenance = _Lgs2624cMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4)
)


class _Lgs2624cRestartDevice_Type(Integer32):
    """Custom type lgs2624cRestartDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cRestartDevice_Type.__name__ = "Integer32"
_Lgs2624cRestartDevice_Object = MibScalar
lgs2624cRestartDevice = _Lgs2624cRestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 1),
    _Lgs2624cRestartDevice_Type()
)
lgs2624cRestartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cRestartDevice.setStatus("current")
_Lgs2624cFirmware_ObjectIdentity = ObjectIdentity
lgs2624cFirmware = _Lgs2624cFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 2)
)
_Lgs2624cFirmwareIpAddress_Type = IpAddress
_Lgs2624cFirmwareIpAddress_Object = MibScalar
lgs2624cFirmwareIpAddress = _Lgs2624cFirmwareIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 2, 1),
    _Lgs2624cFirmwareIpAddress_Type()
)
lgs2624cFirmwareIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cFirmwareIpAddress.setStatus("current")
_Lgs2624cFirmwareFileName_Type = DisplayString
_Lgs2624cFirmwareFileName_Object = MibScalar
lgs2624cFirmwareFileName = _Lgs2624cFirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 2, 2),
    _Lgs2624cFirmwareFileName_Type()
)
lgs2624cFirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cFirmwareFileName.setStatus("current")


class _Lgs2624cDoFirmwareUpgrade_Type(Integer32):
    """Custom type lgs2624cDoFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cDoFirmwareUpgrade_Type.__name__ = "Integer32"
_Lgs2624cDoFirmwareUpgrade_Object = MibScalar
lgs2624cDoFirmwareUpgrade = _Lgs2624cDoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 2, 3),
    _Lgs2624cDoFirmwareUpgrade_Type()
)
lgs2624cDoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cDoFirmwareUpgrade.setStatus("current")
_Lgs2624cSaveOrRestore_ObjectIdentity = ObjectIdentity
lgs2624cSaveOrRestore = _Lgs2624cSaveOrRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 3)
)


class _Lgs2624cFactoryDefaults_Type(Integer32):
    """Custom type lgs2624cFactoryDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cFactoryDefaults_Type.__name__ = "Integer32"
_Lgs2624cFactoryDefaults_Object = MibScalar
lgs2624cFactoryDefaults = _Lgs2624cFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 3, 1),
    _Lgs2624cFactoryDefaults_Type()
)
lgs2624cFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cFactoryDefaults.setStatus("current")


class _Lgs2624cSaveStart_Type(Integer32):
    """Custom type lgs2624cSaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cSaveStart_Type.__name__ = "Integer32"
_Lgs2624cSaveStart_Object = MibScalar
lgs2624cSaveStart = _Lgs2624cSaveStart_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 3, 2),
    _Lgs2624cSaveStart_Type()
)
lgs2624cSaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSaveStart.setStatus("current")


class _Lgs2624cSaveUser_Type(Integer32):
    """Custom type lgs2624cSaveUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cSaveUser_Type.__name__ = "Integer32"
_Lgs2624cSaveUser_Object = MibScalar
lgs2624cSaveUser = _Lgs2624cSaveUser_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 3, 3),
    _Lgs2624cSaveUser_Type()
)
lgs2624cSaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cSaveUser.setStatus("current")


class _Lgs2624cRestoreUser_Type(Integer32):
    """Custom type lgs2624cRestoreUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cRestoreUser_Type.__name__ = "Integer32"
_Lgs2624cRestoreUser_Object = MibScalar
lgs2624cRestoreUser = _Lgs2624cRestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 3, 4),
    _Lgs2624cRestoreUser_Type()
)
lgs2624cRestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cRestoreUser.setStatus("current")
_Lgs2624cExportOrImport_ObjectIdentity = ObjectIdentity
lgs2624cExportOrImport = _Lgs2624cExportOrImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 4)
)
_Lgs2624cExportIpAddress_Type = IpAddress
_Lgs2624cExportIpAddress_Object = MibScalar
lgs2624cExportIpAddress = _Lgs2624cExportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 4, 1),
    _Lgs2624cExportIpAddress_Type()
)
lgs2624cExportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cExportIpAddress.setStatus("current")
_Lgs2624cExportConfigName_Type = DisplayString
_Lgs2624cExportConfigName_Object = MibScalar
lgs2624cExportConfigName = _Lgs2624cExportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 4, 2),
    _Lgs2624cExportConfigName_Type()
)
lgs2624cExportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cExportConfigName.setStatus("current")


class _Lgs2624cDoExportConfig_Type(Integer32):
    """Custom type lgs2624cDoExportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cDoExportConfig_Type.__name__ = "Integer32"
_Lgs2624cDoExportConfig_Object = MibScalar
lgs2624cDoExportConfig = _Lgs2624cDoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 4, 3),
    _Lgs2624cDoExportConfig_Type()
)
lgs2624cDoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cDoExportConfig.setStatus("current")
_Lgs2624cImportIpAddress_Type = IpAddress
_Lgs2624cImportIpAddress_Object = MibScalar
lgs2624cImportIpAddress = _Lgs2624cImportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 4, 4),
    _Lgs2624cImportIpAddress_Type()
)
lgs2624cImportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cImportIpAddress.setStatus("current")
_Lgs2624cImportConfigName_Type = DisplayString
_Lgs2624cImportConfigName_Object = MibScalar
lgs2624cImportConfigName = _Lgs2624cImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 4, 5),
    _Lgs2624cImportConfigName_Type()
)
lgs2624cImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cImportConfigName.setStatus("current")


class _Lgs2624cDoImportConfig_Type(Integer32):
    """Custom type lgs2624cDoImportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cDoImportConfig_Type.__name__ = "Integer32"
_Lgs2624cDoImportConfig_Object = MibScalar
lgs2624cDoImportConfig = _Lgs2624cDoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 4, 6),
    _Lgs2624cDoImportConfig_Type()
)
lgs2624cDoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cDoImportConfig.setStatus("current")
_Lgs2624cDiagnostics_ObjectIdentity = ObjectIdentity
lgs2624cDiagnostics = _Lgs2624cDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5)
)
_Lgs2624cPingIpAddress_Type = IpAddress
_Lgs2624cPingIpAddress_Object = MibScalar
lgs2624cPingIpAddress = _Lgs2624cPingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 1),
    _Lgs2624cPingIpAddress_Type()
)
lgs2624cPingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPingIpAddress.setStatus("current")


class _Lgs2624cPingSize_Type(Integer32):
    """Custom type lgs2624cPingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Lgs2624cPingSize_Type.__name__ = "Integer32"
_Lgs2624cPingSize_Object = MibScalar
lgs2624cPingSize = _Lgs2624cPingSize_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 2),
    _Lgs2624cPingSize_Type()
)
lgs2624cPingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPingSize.setStatus("current")


class _Lgs2624cDoPingConfig_Type(Integer32):
    """Custom type lgs2624cDoPingConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cDoPingConfig_Type.__name__ = "Integer32"
_Lgs2624cDoPingConfig_Object = MibScalar
lgs2624cDoPingConfig = _Lgs2624cDoPingConfig_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 3),
    _Lgs2624cDoPingConfig_Type()
)
lgs2624cDoPingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cDoPingConfig.setStatus("current")
_Lgs2624cPingResult_Type = DisplayString
_Lgs2624cPingResult_Object = MibScalar
lgs2624cPingResult = _Lgs2624cPingResult_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 4),
    _Lgs2624cPingResult_Type()
)
lgs2624cPingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPingResult.setStatus("current")
_Lgs2624cPing6IpAddress_Type = DisplayString
_Lgs2624cPing6IpAddress_Object = MibScalar
lgs2624cPing6IpAddress = _Lgs2624cPing6IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 5),
    _Lgs2624cPing6IpAddress_Type()
)
lgs2624cPing6IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPing6IpAddress.setStatus("current")


class _Lgs2624cPing6Size_Type(Integer32):
    """Custom type lgs2624cPing6Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Lgs2624cPing6Size_Type.__name__ = "Integer32"
_Lgs2624cPing6Size_Object = MibScalar
lgs2624cPing6Size = _Lgs2624cPing6Size_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 6),
    _Lgs2624cPing6Size_Type()
)
lgs2624cPing6Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cPing6Size.setStatus("current")


class _Lgs2624cDoPing6Config_Type(Integer32):
    """Custom type lgs2624cDoPing6Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Lgs2624cDoPing6Config_Type.__name__ = "Integer32"
_Lgs2624cDoPing6Config_Object = MibScalar
lgs2624cDoPing6Config = _Lgs2624cDoPing6Config_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 7),
    _Lgs2624cDoPing6Config_Type()
)
lgs2624cDoPing6Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cDoPing6Config.setStatus("current")
_Lgs2624cPing6Result_Type = DisplayString
_Lgs2624cPing6Result_Object = MibScalar
lgs2624cPing6Result = _Lgs2624cPing6Result_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 8),
    _Lgs2624cPing6Result_Type()
)
lgs2624cPing6Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cPing6Result.setStatus("current")
_Lgs2624cVeriPHY_ObjectIdentity = ObjectIdentity
lgs2624cVeriPHY = _Lgs2624cVeriPHY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 9)
)


class _Lgs2624cVeriPHYTest_Type(Integer32):
    """Custom type lgs2624cVeriPHYTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cVeriPHYTest_Type.__name__ = "Integer32"
_Lgs2624cVeriPHYTest_Object = MibScalar
lgs2624cVeriPHYTest = _Lgs2624cVeriPHYTest_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 9, 1),
    _Lgs2624cVeriPHYTest_Type()
)
lgs2624cVeriPHYTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2624cVeriPHYTest.setStatus("current")
_Lgs2624cVeriPHYTable_Object = MibTable
lgs2624cVeriPHYTable = _Lgs2624cVeriPHYTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 9, 2)
)
if mibBuilder.loadTexts:
    lgs2624cVeriPHYTable.setStatus("current")
_Lgs2624cVeriPHYEntry_Object = MibTableRow
lgs2624cVeriPHYEntry = _Lgs2624cVeriPHYEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 9, 2, 1)
)
lgs2624cVeriPHYEntry.setIndexNames(
    (0, "PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cVeriPHYPort"),
)
if mibBuilder.loadTexts:
    lgs2624cVeriPHYEntry.setStatus("current")


class _Lgs2624cVeriPHYPort_Type(Integer32):
    """Custom type lgs2624cVeriPHYPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Lgs2624cVeriPHYPort_Type.__name__ = "Integer32"
_Lgs2624cVeriPHYPort_Object = MibTableColumn
lgs2624cVeriPHYPort = _Lgs2624cVeriPHYPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 9, 2, 1, 1),
    _Lgs2624cVeriPHYPort_Type()
)
lgs2624cVeriPHYPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2624cVeriPHYPort.setStatus("current")
_Lgs2624cVeriPHYPairA_Type = DisplayString
_Lgs2624cVeriPHYPairA_Object = MibTableColumn
lgs2624cVeriPHYPairA = _Lgs2624cVeriPHYPairA_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 9, 2, 1, 2),
    _Lgs2624cVeriPHYPairA_Type()
)
lgs2624cVeriPHYPairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cVeriPHYPairA.setStatus("current")
_Lgs2624cVeriPHYLengthA_Type = DisplayString
_Lgs2624cVeriPHYLengthA_Object = MibTableColumn
lgs2624cVeriPHYLengthA = _Lgs2624cVeriPHYLengthA_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 9, 2, 1, 3),
    _Lgs2624cVeriPHYLengthA_Type()
)
lgs2624cVeriPHYLengthA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cVeriPHYLengthA.setStatus("current")
_Lgs2624cVeriPHYPairB_Type = DisplayString
_Lgs2624cVeriPHYPairB_Object = MibTableColumn
lgs2624cVeriPHYPairB = _Lgs2624cVeriPHYPairB_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 9, 2, 1, 4),
    _Lgs2624cVeriPHYPairB_Type()
)
lgs2624cVeriPHYPairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cVeriPHYPairB.setStatus("current")
_Lgs2624cVeriPHYLengthB_Type = DisplayString
_Lgs2624cVeriPHYLengthB_Object = MibTableColumn
lgs2624cVeriPHYLengthB = _Lgs2624cVeriPHYLengthB_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 9, 2, 1, 5),
    _Lgs2624cVeriPHYLengthB_Type()
)
lgs2624cVeriPHYLengthB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cVeriPHYLengthB.setStatus("current")
_Lgs2624cVeriPHYPairC_Type = DisplayString
_Lgs2624cVeriPHYPairC_Object = MibTableColumn
lgs2624cVeriPHYPairC = _Lgs2624cVeriPHYPairC_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 9, 2, 1, 6),
    _Lgs2624cVeriPHYPairC_Type()
)
lgs2624cVeriPHYPairC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cVeriPHYPairC.setStatus("current")
_Lgs2624cVeriPHYLengthC_Type = DisplayString
_Lgs2624cVeriPHYLengthC_Object = MibTableColumn
lgs2624cVeriPHYLengthC = _Lgs2624cVeriPHYLengthC_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 9, 2, 1, 7),
    _Lgs2624cVeriPHYLengthC_Type()
)
lgs2624cVeriPHYLengthC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cVeriPHYLengthC.setStatus("current")
_Lgs2624cVeriPHYPairD_Type = DisplayString
_Lgs2624cVeriPHYPairD_Object = MibTableColumn
lgs2624cVeriPHYPairD = _Lgs2624cVeriPHYPairD_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 9, 2, 1, 8),
    _Lgs2624cVeriPHYPairD_Type()
)
lgs2624cVeriPHYPairD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cVeriPHYPairD.setStatus("current")
_Lgs2624cVeriPHYLengthD_Type = DisplayString
_Lgs2624cVeriPHYLengthD_Object = MibTableColumn
lgs2624cVeriPHYLengthD = _Lgs2624cVeriPHYLengthD_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 4, 5, 9, 2, 1, 9),
    _Lgs2624cVeriPHYLengthD_Type()
)
lgs2624cVeriPHYLengthD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cVeriPHYLengthD.setStatus("current")
_Lgs2624cTrap_ObjectIdentity = ObjectIdentity
lgs2624cTrap = _Lgs2624cTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 5)
)
_Lgs2624cTrapEvent_ObjectIdentity = ObjectIdentity
lgs2624cTrapEvent = _Lgs2624cTrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 5, 1)
)
_Lgs2624cTrapVariable_ObjectIdentity = ObjectIdentity
lgs2624cTrapVariable = _Lgs2624cTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 5, 2)
)
_Lgs2624cInformation_Type = DisplayString
_Lgs2624cInformation_Object = MibScalar
lgs2624cInformation = _Lgs2624cInformation_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 5, 2, 1),
    _Lgs2624cInformation_Type()
)
lgs2624cInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2624cInformation.setStatus("current")

# Managed Objects groups


# Notification objects

lgs2624cEmergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 5, 1, 1)
)
lgs2624cEmergency.setObjects(
    ("PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cInformation")
)
if mibBuilder.loadTexts:
    lgs2624cEmergency.setStatus(
        "current"
    )

lgs2624cAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 5, 1, 2)
)
lgs2624cAlert.setObjects(
    ("PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cInformation")
)
if mibBuilder.loadTexts:
    lgs2624cAlert.setStatus(
        "current"
    )

lgs2624cCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 5, 1, 3)
)
lgs2624cCritical.setObjects(
    ("PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cInformation")
)
if mibBuilder.loadTexts:
    lgs2624cCritical.setStatus(
        "current"
    )

lgs2624cError = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 5, 1, 4)
)
lgs2624cError.setObjects(
    ("PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cInformation")
)
if mibBuilder.loadTexts:
    lgs2624cError.setStatus(
        "current"
    )

lgs2624cWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 5, 1, 5)
)
lgs2624cWarning.setObjects(
    ("PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cInformation")
)
if mibBuilder.loadTexts:
    lgs2624cWarning.setStatus(
        "current"
    )

lgs2624cNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 5, 1, 6)
)
lgs2624cNotice.setObjects(
    ("PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cInformation")
)
if mibBuilder.loadTexts:
    lgs2624cNotice.setStatus(
        "current"
    )

lgs2624cInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 5, 1, 7)
)
lgs2624cInformational.setObjects(
    ("PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cInformation")
)
if mibBuilder.loadTexts:
    lgs2624cInformational.setStatus(
        "current"
    )

lgs2624cDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 54, 5, 1, 8)
)
lgs2624cDebug.setObjects(
    ("PRIVATETECH-LGS2624C-FUNCTION-MIB", "lgs2624cInformation")
)
if mibBuilder.loadTexts:
    lgs2624cDebug.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRIVATETECH-LGS2624C-FUNCTION-MIB",
    **{"privatetech": privatetech,
       "switch": switch,
       "lgs2624cProductId": lgs2624cProductId,
       "lgs2624cSystem": lgs2624cSystem,
       "lgs2624cSystemInformation": lgs2624cSystemInformation,
       "lgs2624cModelName": lgs2624cModelName,
       "lgs2624cBIOSVersion": lgs2624cBIOSVersion,
       "lgs2624cFirmwareVersion": lgs2624cFirmwareVersion,
       "lgs2624cHardwareMechanicalVersion": lgs2624cHardwareMechanicalVersion,
       "lgs2624cSeriesNumber": lgs2624cSeriesNumber,
       "lgs2624cHostMACAddress": lgs2624cHostMACAddress,
       "lgs2624cConsoleBaudrate": lgs2624cConsoleBaudrate,
       "lgs2624cRAMSize": lgs2624cRAMSize,
       "lgs2624cFlashSize": lgs2624cFlashSize,
       "lgs2624cBridgeFBDSize": lgs2624cBridgeFBDSize,
       "lgs2624cTransmitQueue": lgs2624cTransmitQueue,
       "lgs2624cMaximumFrameSize": lgs2624cMaximumFrameSize,
       "lgs2624cCPULoad": lgs2624cCPULoad,
       "lgs2624cSystemTime": lgs2624cSystemTime,
       "lgs2624cSystemTimeManual": lgs2624cSystemTimeManual,
       "lgs2624cSystemTimeManualClockSource": lgs2624cSystemTimeManualClockSource,
       "lgs2624cSystemTimeManualLocaltime": lgs2624cSystemTimeManualLocaltime,
       "lgs2624cSystemTimeManualTimeZoneOffset": lgs2624cSystemTimeManualTimeZoneOffset,
       "lgs2624cSystemTimeManualDaylightSavings": lgs2624cSystemTimeManualDaylightSavings,
       "lgs2624cSystemTimeManualTimeSetOffset": lgs2624cSystemTimeManualTimeSetOffset,
       "lgs2624cSystemTimeManualDaylightSavingsType": lgs2624cSystemTimeManualDaylightSavingsType,
       "lgs2624cSystemTimeManualDaylightSavingsBydatesFrom": lgs2624cSystemTimeManualDaylightSavingsBydatesFrom,
       "lgs2624cSystemTimeManualDaylightSavingsBydatesTo": lgs2624cSystemTimeManualDaylightSavingsBydatesTo,
       "lgs2624cSystemTimeManualDaylightSavingsRecurringDayFrom": lgs2624cSystemTimeManualDaylightSavingsRecurringDayFrom,
       "lgs2624cSystemTimeManualDaylightSavingsRecurringWeekFrom": lgs2624cSystemTimeManualDaylightSavingsRecurringWeekFrom,
       "lgs2624cSystemTimeManualDaylightSavingsRecurringMonthFrom": lgs2624cSystemTimeManualDaylightSavingsRecurringMonthFrom,
       "lgs2624cSystemTimeManualDaylightSavingsRecurringTimeFrom": lgs2624cSystemTimeManualDaylightSavingsRecurringTimeFrom,
       "lgs2624cSystemTimeManualDaylightSavingsRecurringDayTo": lgs2624cSystemTimeManualDaylightSavingsRecurringDayTo,
       "lgs2624cSystemTimeManualDaylightSavingsRecurringWeekTo": lgs2624cSystemTimeManualDaylightSavingsRecurringWeekTo,
       "lgs2624cSystemTimeManualDaylightSavingsRecurringMonthTo": lgs2624cSystemTimeManualDaylightSavingsRecurringMonthTo,
       "lgs2624cSystemTimeManualDaylightSavingsRecurringTimeTo": lgs2624cSystemTimeManualDaylightSavingsRecurringTimeTo,
       "lgs2624cSystemTimeNTP": lgs2624cSystemTimeNTP,
       "lgs2624cSystemTimeNTPTable": lgs2624cSystemTimeNTPTable,
       "lgs2624cSystemTimeNTPEntry": lgs2624cSystemTimeNTPEntry,
       "lgs2624cSystemTimeNTPIndex": lgs2624cSystemTimeNTPIndex,
       "lgs2624cSystemTimeNTPServerIPType": lgs2624cSystemTimeNTPServerIPType,
       "lgs2624cSystemTimeNTPServer": lgs2624cSystemTimeNTPServer,
       "lgs2624cSystemTimeNTPCurrentMode": lgs2624cSystemTimeNTPCurrentMode,
       "lgs2624cSystemAccount": lgs2624cSystemAccount,
       "lgs2624cSystemAccountUsers": lgs2624cSystemAccountUsers,
       "lgs2624cSystemAccountUserCreate": lgs2624cSystemAccountUserCreate,
       "lgs2624cSystemAccountUsersTable": lgs2624cSystemAccountUsersTable,
       "lgs2624cSystemAccountUsersEntry": lgs2624cSystemAccountUsersEntry,
       "lgs2624cUserIndex": lgs2624cUserIndex,
       "lgs2624cUserName": lgs2624cUserName,
       "lgs2624cPassword": lgs2624cPassword,
       "lgs2624cUserPrivilegeLevel": lgs2624cUserPrivilegeLevel,
       "lgs2624cAccountUserRowStatus": lgs2624cAccountUserRowStatus,
       "lgs2624cSystemAccountPrivilegeLevel": lgs2624cSystemAccountPrivilegeLevel,
       "lgs2624cAccountPrivilegeLevel": lgs2624cAccountPrivilegeLevel,
       "lgs2624cAggregationPrivilegeLevel": lgs2624cAggregationPrivilegeLevel,
       "lgs2624cDiagnosticsPrivilegeLevel": lgs2624cDiagnosticsPrivilegeLevel,
       "lgs2624cEEEPrivilegeLevel": lgs2624cEEEPrivilegeLevel,
       "lgs2624cEasyportPrivilegeLevel": lgs2624cEasyportPrivilegeLevel,
       "lgs2624cGARPPrivilegeLevel": lgs2624cGARPPrivilegeLevel,
       "lgs2624cGVRPPrivilegeLevel": lgs2624cGVRPPrivilegeLevel,
       "lgs2624cIPPrivilegeLevel": lgs2624cIPPrivilegeLevel,
       "lgs2624cIPMCSnoopingPrivilegeLevel": lgs2624cIPMCSnoopingPrivilegeLevel,
       "lgs2624cLACPPrivilegeLevel": lgs2624cLACPPrivilegeLevel,
       "lgs2624cLLDPPrivilegeLevel": lgs2624cLLDPPrivilegeLevel,
       "lgs2624cLLDPMEDPrivilegeLevel": lgs2624cLLDPMEDPrivilegeLevel,
       "lgs2624cMACTablePrivilegeLevel": lgs2624cMACTablePrivilegeLevel,
       "lgs2624cMRPPrivilegeLevel": lgs2624cMRPPrivilegeLevel,
       "lgs2624cMVRPrivilegeLevel": lgs2624cMVRPrivilegeLevel,
       "lgs2624cMVRPPrivilegeLevel": lgs2624cMVRPPrivilegeLevel,
       "lgs2624cMaintenancePrivilegeLevel": lgs2624cMaintenancePrivilegeLevel,
       "lgs2624cMirroringPrivilegeLevel": lgs2624cMirroringPrivilegeLevel,
       "lgs2624cPortsPrivilegeLevel": lgs2624cPortsPrivilegeLevel,
       "lgs2624cPrivateVLANsPrivilegeLevel": lgs2624cPrivateVLANsPrivilegeLevel,
       "lgs2624cQoSPrivilegeLevel": lgs2624cQoSPrivilegeLevel,
       "lgs2624cSMTPPrivilegeLevel": lgs2624cSMTPPrivilegeLevel,
       "lgs2624cSNMPPrivilegeLevel": lgs2624cSNMPPrivilegeLevel,
       "lgs2624cSecurityPrivilegeLevel": lgs2624cSecurityPrivilegeLevel,
       "lgs2624cSpanningTreePrivilegeLevel": lgs2624cSpanningTreePrivilegeLevel,
       "lgs2624cSystemPrivilegeLevel": lgs2624cSystemPrivilegeLevel,
       "lgs2624cTrapEventPrivilegeLevel": lgs2624cTrapEventPrivilegeLevel,
       "lgs2624cVCLPrivilegeLevel": lgs2624cVCLPrivilegeLevel,
       "lgs2624cVLANsPrivilegeLevel": lgs2624cVLANsPrivilegeLevel,
       "lgs2624cVoiceVLANPrivilegeLevel": lgs2624cVoiceVLANPrivilegeLevel,
       "lgs2624cIP": lgs2624cIP,
       "lgs2624cIPv4": lgs2624cIPv4,
       "lgs2624cIPv4Configured": lgs2624cIPv4Configured,
       "lgs2624cIpv4DHCPClient": lgs2624cIpv4DHCPClient,
       "lgs2624cIPv4Address": lgs2624cIPv4Address,
       "lgs2624cIPv4Mask": lgs2624cIPv4Mask,
       "lgs2624cIPv4Router": lgs2624cIPv4Router,
       "lgs2624cIPv4VLANId": lgs2624cIPv4VLANId,
       "lgs2624cIPv4DNSServer": lgs2624cIPv4DNSServer,
       "lgs2624cIPv4DNSProxy": lgs2624cIPv4DNSProxy,
       "lgs2624cIPv4Current": lgs2624cIPv4Current,
       "lgs2624cIpv4CurrentDHCPClient": lgs2624cIpv4CurrentDHCPClient,
       "lgs2624cIPv4CurrentAddress": lgs2624cIPv4CurrentAddress,
       "lgs2624cIPv4CurrentMask": lgs2624cIPv4CurrentMask,
       "lgs2624cIPv4CurrentRouter": lgs2624cIPv4CurrentRouter,
       "lgs2624cIPv4CurrentVLANId": lgs2624cIPv4CurrentVLANId,
       "lgs2624cIPv4CurrentDNSServer": lgs2624cIPv4CurrentDNSServer,
       "lgs2624cIPv6": lgs2624cIPv6,
       "lgs2624cIPv6Configured": lgs2624cIPv6Configured,
       "lgs2624cIpv6AutoConfiguration": lgs2624cIpv6AutoConfiguration,
       "lgs2624cIpv6Address": lgs2624cIpv6Address,
       "lgs2624cIpv6Prefix": lgs2624cIpv6Prefix,
       "lgs2624cIpv6Router": lgs2624cIpv6Router,
       "lgs2624cIPv6Current": lgs2624cIPv6Current,
       "lgs2624cIpv6CurrentAutoConfiguration": lgs2624cIpv6CurrentAutoConfiguration,
       "lgs2624cIpv6CurrentAddress": lgs2624cIpv6CurrentAddress,
       "lgs2624cIpv6CurrentLinkLocalAddress": lgs2624cIpv6CurrentLinkLocalAddress,
       "lgs2624cIpv6CurrentPrefix": lgs2624cIpv6CurrentPrefix,
       "lgs2624cIpv6CurrentRouter": lgs2624cIpv6CurrentRouter,
       "lgs2624cSyslog": lgs2624cSyslog,
       "lgs2624cSyslogConf": lgs2624cSyslogConf,
       "lgs2624cServerMode": lgs2624cServerMode,
       "lgs2624cServerAddress1": lgs2624cServerAddress1,
       "lgs2624cServerAddress2": lgs2624cServerAddress2,
       "lgs2624cSyslogLevel": lgs2624cSyslogLevel,
       "lgs2624cSyslogDetailedInfo": lgs2624cSyslogDetailedInfo,
       "lgs2624cSyslogDetailedInfoClear": lgs2624cSyslogDetailedInfoClear,
       "lgs2624cSyslogDetailedInfoTable": lgs2624cSyslogDetailedInfoTable,
       "lgs2624cSyslogDetailedInfoEntry": lgs2624cSyslogDetailedInfoEntry,
       "lgs2624cSyslogDetailedInfoIndex": lgs2624cSyslogDetailedInfoIndex,
       "lgs2624cSyslogDetailedInfoLevel": lgs2624cSyslogDetailedInfoLevel,
       "lgs2624cSyslogDetailedInfoTime": lgs2624cSyslogDetailedInfoTime,
       "lgs2624cSyslogDetailedInfoMessage": lgs2624cSyslogDetailedInfoMessage,
       "lgs2624cSnmp": lgs2624cSnmp,
       "lgs2624cSnmpConf": lgs2624cSnmpConf,
       "lgs2624cGetCommunity": lgs2624cGetCommunity,
       "lgs2624cSetCommunityMode": lgs2624cSetCommunityMode,
       "lgs2624cSetCommunity": lgs2624cSetCommunity,
       "lgs2624cTrapHostConfTable": lgs2624cTrapHostConfTable,
       "lgs2624cTrapHostConfEntry": lgs2624cTrapHostConfEntry,
       "lgs2624cTrapHostConfIndex": lgs2624cTrapHostConfIndex,
       "lgs2624cTrapHostConfVersion": lgs2624cTrapHostConfVersion,
       "lgs2624cTrapHostConfIPType": lgs2624cTrapHostConfIPType,
       "lgs2624cTrapHostConfIP": lgs2624cTrapHostConfIP,
       "lgs2624cTrapHostConfPort": lgs2624cTrapHostConfPort,
       "lgs2624cTrapHostConfCommunity": lgs2624cTrapHostConfCommunity,
       "lgs2624cTrapHostConfSeverityLevel": lgs2624cTrapHostConfSeverityLevel,
       "lgs2624cTrapHostConfSecurityLevel": lgs2624cTrapHostConfSecurityLevel,
       "lgs2624cTrapHostConfAuthPtc": lgs2624cTrapHostConfAuthPtc,
       "lgs2624cTrapHostConfAuthPassword": lgs2624cTrapHostConfAuthPassword,
       "lgs2624cTrapHostConfPrivPtc": lgs2624cTrapHostConfPrivPtc,
       "lgs2624cTrapHostConfPrivPassword": lgs2624cTrapHostConfPrivPassword,
       "lgs2624cTrapHostConfCurrentMode": lgs2624cTrapHostConfCurrentMode,
       "lgs2624cConfiguration": lgs2624cConfiguration,
       "lgs2624cPort": lgs2624cPort,
       "lgs2624cPortConfigurationTable": lgs2624cPortConfigurationTable,
       "lgs2624cPortConfigurationEntry": lgs2624cPortConfigurationEntry,
       "lgs2624cPortConfPort": lgs2624cPortConfPort,
       "lgs2624cPortConfPortMedia": lgs2624cPortConfPortMedia,
       "lgs2624cPortConfLink": lgs2624cPortConfLink,
       "lgs2624cPortConfCurrentSpeed": lgs2624cPortConfCurrentSpeed,
       "lgs2624cPortConfSpeed": lgs2624cPortConfSpeed,
       "lgs2624cPortConfCurrentFlowControlRx": lgs2624cPortConfCurrentFlowControlRx,
       "lgs2624cPortConfCurrentFlowControlTx": lgs2624cPortConfCurrentFlowControlTx,
       "lgs2624cPortConfFlowControl": lgs2624cPortConfFlowControl,
       "lgs2624cPortConfMaxFrameSize": lgs2624cPortConfMaxFrameSize,
       "lgs2624cPortConfExcessiveCollisionMode": lgs2624cPortConfExcessiveCollisionMode,
       "lgs2624cPortConfPowerControl": lgs2624cPortConfPowerControl,
       "lgs2624cPortConfDescription": lgs2624cPortConfDescription,
       "lgs2624cPortTrafficStatisticsTable": lgs2624cPortTrafficStatisticsTable,
       "lgs2624cPortTrafficStatisticsEntry": lgs2624cPortTrafficStatisticsEntry,
       "lgs2624cPortTrafficStatisticsPort": lgs2624cPortTrafficStatisticsPort,
       "lgs2624cPortTrafficStatisticsClear": lgs2624cPortTrafficStatisticsClear,
       "lgs2624cPortTrafficRxPackets": lgs2624cPortTrafficRxPackets,
       "lgs2624cPortTrafficRxOctets": lgs2624cPortTrafficRxOctets,
       "lgs2624cPortTrafficRxUnicast": lgs2624cPortTrafficRxUnicast,
       "lgs2624cPortTrafficRxMulticast": lgs2624cPortTrafficRxMulticast,
       "lgs2624cPortTrafficRxBroadcast": lgs2624cPortTrafficRxBroadcast,
       "lgs2624cPortTrafficRxPause": lgs2624cPortTrafficRxPause,
       "lgs2624cPortTrafficRx64Bytes": lgs2624cPortTrafficRx64Bytes,
       "lgs2624cPortTrafficRx65to127Bytes": lgs2624cPortTrafficRx65to127Bytes,
       "lgs2624cPortTrafficRx128to255Bytes": lgs2624cPortTrafficRx128to255Bytes,
       "lgs2624cPortTrafficRx256to511Bytes": lgs2624cPortTrafficRx256to511Bytes,
       "lgs2624cPortTrafficRx512to1023Bytes": lgs2624cPortTrafficRx512to1023Bytes,
       "lgs2624cPortTrafficRx1024to1526Bytes": lgs2624cPortTrafficRx1024to1526Bytes,
       "lgs2624cPortTrafficRxExceecd1527Bytes": lgs2624cPortTrafficRxExceecd1527Bytes,
       "lgs2624cPortTrafficRxQ0": lgs2624cPortTrafficRxQ0,
       "lgs2624cPortTrafficRxQ1": lgs2624cPortTrafficRxQ1,
       "lgs2624cPortTrafficRxQ2": lgs2624cPortTrafficRxQ2,
       "lgs2624cPortTrafficRxQ3": lgs2624cPortTrafficRxQ3,
       "lgs2624cPortTrafficRxQ4": lgs2624cPortTrafficRxQ4,
       "lgs2624cPortTrafficRxQ5": lgs2624cPortTrafficRxQ5,
       "lgs2624cPortTrafficRxQ6": lgs2624cPortTrafficRxQ6,
       "lgs2624cPortTrafficRxQ7": lgs2624cPortTrafficRxQ7,
       "lgs2624cPortTrafficRxDrops": lgs2624cPortTrafficRxDrops,
       "lgs2624cPortTrafficRxCRCorAlignment": lgs2624cPortTrafficRxCRCorAlignment,
       "lgs2624cPortTrafficRxUndersize": lgs2624cPortTrafficRxUndersize,
       "lgs2624cPortTrafficRxOversize": lgs2624cPortTrafficRxOversize,
       "lgs2624cPortTrafficRxFragments": lgs2624cPortTrafficRxFragments,
       "lgs2624cPortTrafficRxJabber": lgs2624cPortTrafficRxJabber,
       "lgs2624cPortTrafficRxFiltered": lgs2624cPortTrafficRxFiltered,
       "lgs2624cPortTrafficTxPackets": lgs2624cPortTrafficTxPackets,
       "lgs2624cPortTrafficTxOctets": lgs2624cPortTrafficTxOctets,
       "lgs2624cPortTrafficTxUnicast": lgs2624cPortTrafficTxUnicast,
       "lgs2624cPortTrafficTxMulticast": lgs2624cPortTrafficTxMulticast,
       "lgs2624cPortTrafficTxBroadcast": lgs2624cPortTrafficTxBroadcast,
       "lgs2624cPortTrafficTxPause": lgs2624cPortTrafficTxPause,
       "lgs2624cPortTrafficTx64Bytes": lgs2624cPortTrafficTx64Bytes,
       "lgs2624cPortTrafficTx65to127Bytes": lgs2624cPortTrafficTx65to127Bytes,
       "lgs2624cPortTrafficTx128to255Bytes": lgs2624cPortTrafficTx128to255Bytes,
       "lgs2624cPortTrafficTx256to511Bytes": lgs2624cPortTrafficTx256to511Bytes,
       "lgs2624cPortTrafficTx512to1023Bytes": lgs2624cPortTrafficTx512to1023Bytes,
       "lgs2624cPortTrafficTx1024to1526Bytes": lgs2624cPortTrafficTx1024to1526Bytes,
       "lgs2624cPortTrafficTxExceecd1527Bytes": lgs2624cPortTrafficTxExceecd1527Bytes,
       "lgs2624cPortTrafficTxQ0": lgs2624cPortTrafficTxQ0,
       "lgs2624cPortTrafficTxQ1": lgs2624cPortTrafficTxQ1,
       "lgs2624cPortTrafficTxQ2": lgs2624cPortTrafficTxQ2,
       "lgs2624cPortTrafficTxQ3": lgs2624cPortTrafficTxQ3,
       "lgs2624cPortTrafficTxQ4": lgs2624cPortTrafficTxQ4,
       "lgs2624cPortTrafficTxQ5": lgs2624cPortTrafficTxQ5,
       "lgs2624cPortTrafficTxQ6": lgs2624cPortTrafficTxQ6,
       "lgs2624cPortTrafficTxQ7": lgs2624cPortTrafficTxQ7,
       "lgs2624cPortTrafficTxDrops": lgs2624cPortTrafficTxDrops,
       "lgs2624cPortTrafficTxLateOrExcColl": lgs2624cPortTrafficTxLateOrExcColl,
       "lgs2624cPortQoSStatistics": lgs2624cPortQoSStatistics,
       "lgs2624cPortQoSStatisticsClear": lgs2624cPortQoSStatisticsClear,
       "lgs2624cPortQoSStatisticsTable": lgs2624cPortQoSStatisticsTable,
       "lgs2624cPortQoSStatisticsEntry": lgs2624cPortQoSStatisticsEntry,
       "lgs2624cPortQoSStatisticsPort": lgs2624cPortQoSStatisticsPort,
       "lgs2624cPortQoSQ0Rx": lgs2624cPortQoSQ0Rx,
       "lgs2624cPortQoSQ0Tx": lgs2624cPortQoSQ0Tx,
       "lgs2624cPortQoSQ1Rx": lgs2624cPortQoSQ1Rx,
       "lgs2624cPortQoSQ1Tx": lgs2624cPortQoSQ1Tx,
       "lgs2624cPortQoSQ2Rx": lgs2624cPortQoSQ2Rx,
       "lgs2624cPortQoSQ2Tx": lgs2624cPortQoSQ2Tx,
       "lgs2624cPortQoSQ3Rx": lgs2624cPortQoSQ3Rx,
       "lgs2624cPortQoSQ3Tx": lgs2624cPortQoSQ3Tx,
       "lgs2624cPortQoSQ4Rx": lgs2624cPortQoSQ4Rx,
       "lgs2624cPortQoSQ4Tx": lgs2624cPortQoSQ4Tx,
       "lgs2624cPortQoSQ5Rx": lgs2624cPortQoSQ5Rx,
       "lgs2624cPortQoSQ5Tx": lgs2624cPortQoSQ5Tx,
       "lgs2624cPortQoSQ6Rx": lgs2624cPortQoSQ6Rx,
       "lgs2624cPortQoSQ6Tx": lgs2624cPortQoSQ6Tx,
       "lgs2624cPortQoSQ7Rx": lgs2624cPortQoSQ7Rx,
       "lgs2624cPortQoSQ7Tx": lgs2624cPortQoSQ7Tx,
       "lgs2624cSFPInfoTable": lgs2624cSFPInfoTable,
       "lgs2624cSFPInfoEntry": lgs2624cSFPInfoEntry,
       "lgs2624cSFPInfoIndex": lgs2624cSFPInfoIndex,
       "lgs2624cSFPInfoPort": lgs2624cSFPInfoPort,
       "lgs2624cSFPConnectorType": lgs2624cSFPConnectorType,
       "lgs2624cSFPFiberType": lgs2624cSFPFiberType,
       "lgs2624cSFPTxCentralWavelength": lgs2624cSFPTxCentralWavelength,
       "lgs2624cSFPBaudRate": lgs2624cSFPBaudRate,
       "lgs2624cSFPVendorOUI": lgs2624cSFPVendorOUI,
       "lgs2624cSFPVendorName": lgs2624cSFPVendorName,
       "lgs2624cSFPVendorPN": lgs2624cSFPVendorPN,
       "lgs2624cSFPVendorRev": lgs2624cSFPVendorRev,
       "lgs2624cSFPVendorSN": lgs2624cSFPVendorSN,
       "lgs2624cSFPDateCode": lgs2624cSFPDateCode,
       "lgs2624cSFPTemperature": lgs2624cSFPTemperature,
       "lgs2624cSFPVcc": lgs2624cSFPVcc,
       "lgs2624cSFPMon1Bias": lgs2624cSFPMon1Bias,
       "lgs2624cSFPMon2TxPWR": lgs2624cSFPMon2TxPWR,
       "lgs2624cSFPMon3RxPWR": lgs2624cSFPMon3RxPWR,
       "lgs2624cPortEEETable": lgs2624cPortEEETable,
       "lgs2624cPortEEEEntry": lgs2624cPortEEEEntry,
       "lgs2624cPortEEEPort": lgs2624cPortEEEPort,
       "lgs2624cPortEEEMode": lgs2624cPortEEEMode,
       "lgs2624cPortEEEUrgentQueue1": lgs2624cPortEEEUrgentQueue1,
       "lgs2624cPortEEEUrgentQueue2": lgs2624cPortEEEUrgentQueue2,
       "lgs2624cPortEEEUrgentQueue3": lgs2624cPortEEEUrgentQueue3,
       "lgs2624cPortEEEUrgentQueue4": lgs2624cPortEEEUrgentQueue4,
       "lgs2624cPortEEEUrgentQueue5": lgs2624cPortEEEUrgentQueue5,
       "lgs2624cPortEEEUrgentQueue6": lgs2624cPortEEEUrgentQueue6,
       "lgs2624cPortEEEUrgentQueue7": lgs2624cPortEEEUrgentQueue7,
       "lgs2624cPortEEEUrgentQueue8": lgs2624cPortEEEUrgentQueue8,
       "lgs2624cVoiceVLAN": lgs2624cVoiceVLAN,
       "lgs2624cVoiceVLANConf": lgs2624cVoiceVLANConf,
       "lgs2624cVoiceVLANMode": lgs2624cVoiceVLANMode,
       "lgs2624cVoiceVLANVLANId": lgs2624cVoiceVLANVLANId,
       "lgs2624cVoiceVLANAgingTime": lgs2624cVoiceVLANAgingTime,
       "lgs2624cVoiceVLANTrafficClass": lgs2624cVoiceVLANTrafficClass,
       "lgs2624cVoiceVLANPortTable": lgs2624cVoiceVLANPortTable,
       "lgs2624cVoiceVLANPortEntry": lgs2624cVoiceVLANPortEntry,
       "lgs2624cVoiceVLANPort": lgs2624cVoiceVLANPort,
       "lgs2624cVoiceVLANPortMode": lgs2624cVoiceVLANPortMode,
       "lgs2624cVoiceVLANPortSecurity": lgs2624cVoiceVLANPortSecurity,
       "lgs2624cVoiceVLANPortDiscoveryProtocol": lgs2624cVoiceVLANPortDiscoveryProtocol,
       "lgs2624cVoiceVLANOUI": lgs2624cVoiceVLANOUI,
       "lgs2624cVoiceVLANOUICreate": lgs2624cVoiceVLANOUICreate,
       "lgs2624cVoiceVLANOUITable": lgs2624cVoiceVLANOUITable,
       "lgs2624cVoiceVLANOUIEntry": lgs2624cVoiceVLANOUIEntry,
       "lgs2624cVoiceVLANOUIIndex": lgs2624cVoiceVLANOUIIndex,
       "lgs2624cVoiceVLANTelephonyOUI": lgs2624cVoiceVLANTelephonyOUI,
       "lgs2624cVoiceVLANDescription": lgs2624cVoiceVLANDescription,
       "lgs2624cVoiceVLANOUIRowStatus": lgs2624cVoiceVLANOUIRowStatus,
       "lgs2624cGARP": lgs2624cGARP,
       "lgs2624cGARPConfTable": lgs2624cGARPConfTable,
       "lgs2624cGARPConfEntry": lgs2624cGARPConfEntry,
       "lgs2624cGARPConfPort": lgs2624cGARPConfPort,
       "lgs2624cGARPJoinTimer": lgs2624cGARPJoinTimer,
       "lgs2624cGARPLeaveTimer": lgs2624cGARPLeaveTimer,
       "lgs2624cGARPLeaveAllTimer": lgs2624cGARPLeaveAllTimer,
       "lgs2624cGARPApplicantion": lgs2624cGARPApplicantion,
       "lgs2624cGARPAttributeType": lgs2624cGARPAttributeType,
       "lgs2624cGARPApplicant": lgs2624cGARPApplicant,
       "lgs2624cGARPStatisticsTable": lgs2624cGARPStatisticsTable,
       "lgs2624cGARPStatisticsEntry": lgs2624cGARPStatisticsEntry,
       "lgs2624cGARPStatisticsPort": lgs2624cGARPStatisticsPort,
       "lgs2624cGARPStatisticsPeerMAC": lgs2624cGARPStatisticsPeerMAC,
       "lgs2624cGARPStatisticsFailedCount": lgs2624cGARPStatisticsFailedCount,
       "lgs2624cGVRP": lgs2624cGVRP,
       "lgs2624cGVRPConf": lgs2624cGVRPConf,
       "lgs2624cGVRPMode": lgs2624cGVRPMode,
       "lgs2624cGVRPConfTable": lgs2624cGVRPConfTable,
       "lgs2624cGVRPConfEntry": lgs2624cGVRPConfEntry,
       "lgs2624cGVRPConfPort": lgs2624cGVRPConfPort,
       "lgs2624cGVRPConfPortMode": lgs2624cGVRPConfPortMode,
       "lgs2624cGVRPConfPortRRole": lgs2624cGVRPConfPortRRole,
       "lgs2624cGVRPStatisticsTable": lgs2624cGVRPStatisticsTable,
       "lgs2624cGVRPStatisticsEntry": lgs2624cGVRPStatisticsEntry,
       "lgs2624cGVRPStatisticsPort": lgs2624cGVRPStatisticsPort,
       "lgs2624cGVRPStatisticsJoinTxCnt": lgs2624cGVRPStatisticsJoinTxCnt,
       "lgs2624cGVRPStatisticsLeaveTxCnt": lgs2624cGVRPStatisticsLeaveTxCnt,
       "lgs2624cThermalProtection": lgs2624cThermalProtection,
       "lgs2624cPriority0Temperature": lgs2624cPriority0Temperature,
       "lgs2624cPriority1Temperature": lgs2624cPriority1Temperature,
       "lgs2624cPriority2Temperature": lgs2624cPriority2Temperature,
       "lgs2624cPriority3Temperature": lgs2624cPriority3Temperature,
       "lgs2624cThermalProtectionTable": lgs2624cThermalProtectionTable,
       "lgs2624cThermalProtectionEntry": lgs2624cThermalProtectionEntry,
       "lgs2624cThermalProtectionPort": lgs2624cThermalProtectionPort,
       "lgs2624cThermalProtectionPortTemperature": lgs2624cThermalProtectionPortTemperature,
       "lgs2624cThermalProtectionPortPriority": lgs2624cThermalProtectionPortPriority,
       "lgs2624cThermalProtectionPortStatus": lgs2624cThermalProtectionPortStatus,
       "lgs2624cMirroring": lgs2624cMirroring,
       "lgs2624cPortToMirrorOn": lgs2624cPortToMirrorOn,
       "lgs2624cMirrorTable": lgs2624cMirrorTable,
       "lgs2624cMirrorEntry": lgs2624cMirrorEntry,
       "lgs2624cMirrorPort": lgs2624cMirrorPort,
       "lgs2624cMirrorMode": lgs2624cMirrorMode,
       "lgs2624cTrapEventSeverity": lgs2624cTrapEventSeverity,
       "lgs2624cTrapEventSeverityACL": lgs2624cTrapEventSeverityACL,
       "lgs2624cTrapEventSeverityACLLog": lgs2624cTrapEventSeverityACLLog,
       "lgs2624cTrapEventSeverityAccessMgmt": lgs2624cTrapEventSeverityAccessMgmt,
       "lgs2624cTrapEventSeverityAuthFailed": lgs2624cTrapEventSeverityAuthFailed,
       "lgs2624cTrapEventSeverityColdStart": lgs2624cTrapEventSeverityColdStart,
       "lgs2624cTrapEventSeverityConfigInfo": lgs2624cTrapEventSeverityConfigInfo,
       "lgs2624cTrapEventSeverityFirmwareUpgrade": lgs2624cTrapEventSeverityFirmwareUpgrade,
       "lgs2624cTrapEventSeverityImportExport": lgs2624cTrapEventSeverityImportExport,
       "lgs2624cTrapEventSeverityLinkStatus": lgs2624cTrapEventSeverityLinkStatus,
       "lgs2624cTrapEventSeverityLogin": lgs2624cTrapEventSeverityLogin,
       "lgs2624cTrapEventSeverityLogout": lgs2624cTrapEventSeverityLogout,
       "lgs2624cTrapEventSeverityMgmtIPChange": lgs2624cTrapEventSeverityMgmtIPChange,
       "lgs2624cTrapEventSeverityModuleChange": lgs2624cTrapEventSeverityModuleChange,
       "lgs2624cTrapEventSeverityNAS": lgs2624cTrapEventSeverityNAS,
       "lgs2624cTrapEventSeverityPasswdChange": lgs2624cTrapEventSeverityPasswdChange,
       "lgs2624cTrapEventSeverityPortSecurity": lgs2624cTrapEventSeverityPortSecurity,
       "lgs2624cTrapEventSeverityThermalProtect": lgs2624cTrapEventSeverityThermalProtect,
       "lgs2624cTrapEventSeverityVLAN": lgs2624cTrapEventSeverityVLAN,
       "lgs2624cTrapEventSeverityWarmStart": lgs2624cTrapEventSeverityWarmStart,
       "lgs2624cSMTP": lgs2624cSMTP,
       "lgs2624cSMTPMailServer": lgs2624cSMTPMailServer,
       "lgs2624cSMTPUserName": lgs2624cSMTPUserName,
       "lgs2624cSMTPPassword": lgs2624cSMTPPassword,
       "lgs2624cSMTPServeriryLevel": lgs2624cSMTPServeriryLevel,
       "lgs2624cSMTPSender": lgs2624cSMTPSender,
       "lgs2624cSMTPReturnPath": lgs2624cSMTPReturnPath,
       "lgs2624cSMTPEmailAddress1": lgs2624cSMTPEmailAddress1,
       "lgs2624cSMTPEmailAddress2": lgs2624cSMTPEmailAddress2,
       "lgs2624cSMTPEmailAddress3": lgs2624cSMTPEmailAddress3,
       "lgs2624cSMTPEmailAddress4": lgs2624cSMTPEmailAddress4,
       "lgs2624cSMTPEmailAddress5": lgs2624cSMTPEmailAddress5,
       "lgs2624cSMTPEmailAddress6": lgs2624cSMTPEmailAddress6,
       "lgs2624cSecurity": lgs2624cSecurity,
       "lgs2624cIPSourceGuard": lgs2624cIPSourceGuard,
       "lgs2624cIPSourceGuardConf": lgs2624cIPSourceGuardConf,
       "lgs2624cIPSourceGuardMode": lgs2624cIPSourceGuardMode,
       "lgs2624cIPSourceGuardPortConfigTable": lgs2624cIPSourceGuardPortConfigTable,
       "lgs2624cIPSourceGuardPortConfigEntry": lgs2624cIPSourceGuardPortConfigEntry,
       "lgs2624cIPSourceGuardPortConfigPort": lgs2624cIPSourceGuardPortConfigPort,
       "lgs2624cIPSourceGuardPortConfigMode": lgs2624cIPSourceGuardPortConfigMode,
       "lgs2624cIPSourceGuardPortMaxDynamicClients": lgs2624cIPSourceGuardPortMaxDynamicClients,
       "lgs2624cIPSourceGuardStatic": lgs2624cIPSourceGuardStatic,
       "lgs2624cIPSourceGuardStaticCreate": lgs2624cIPSourceGuardStaticCreate,
       "lgs2624cIPSourceGuardStaticTable": lgs2624cIPSourceGuardStaticTable,
       "lgs2624cIPSourceGuardStaticEntry": lgs2624cIPSourceGuardStaticEntry,
       "lgs2624cIPSourceGuardStaticIndex": lgs2624cIPSourceGuardStaticIndex,
       "lgs2624cIPSourceGuardStaticPort": lgs2624cIPSourceGuardStaticPort,
       "lgs2624cIPSourceGuardStaticVLANId": lgs2624cIPSourceGuardStaticVLANId,
       "lgs2624cIPSourceGuardStaticIPAddress": lgs2624cIPSourceGuardStaticIPAddress,
       "lgs2624cIPSourceGuardStaticMACAddress": lgs2624cIPSourceGuardStaticMACAddress,
       "lgs2624cIPSourceGuardStaticRowStatus": lgs2624cIPSourceGuardStaticRowStatus,
       "lgs2624cIPSourceGuardDynamicTable": lgs2624cIPSourceGuardDynamicTable,
       "lgs2624cIPSourceGuardDynamicEntry": lgs2624cIPSourceGuardDynamicEntry,
       "lgs2624cIPSourceGuardDynamicIndex": lgs2624cIPSourceGuardDynamicIndex,
       "lgs2624cIPSourceGuardDynamicPort": lgs2624cIPSourceGuardDynamicPort,
       "lgs2624cIPSourceGuardDynamicVLANId": lgs2624cIPSourceGuardDynamicVLANId,
       "lgs2624cIPSourceGuardDynamicIPAddress": lgs2624cIPSourceGuardDynamicIPAddress,
       "lgs2624cIPSourceGuardDynamicMACAddress": lgs2624cIPSourceGuardDynamicMACAddress,
       "lgs2624cARPInspection": lgs2624cARPInspection,
       "lgs2624cARPInspectionConf": lgs2624cARPInspectionConf,
       "lgs2624cARPInspectionConfMode": lgs2624cARPInspectionConfMode,
       "lgs2624cARPInspectionConfTable": lgs2624cARPInspectionConfTable,
       "lgs2624cARPInspectionConfEntry": lgs2624cARPInspectionConfEntry,
       "lgs2624cARPInspectionConfPortIndex": lgs2624cARPInspectionConfPortIndex,
       "lgs2624cARPInspectionConfPortMode": lgs2624cARPInspectionConfPortMode,
       "lgs2624cARPInspectionStatic": lgs2624cARPInspectionStatic,
       "lgs2624cARPInspectionStaticCreate": lgs2624cARPInspectionStaticCreate,
       "lgs2624cARPInspectionStaticTable": lgs2624cARPInspectionStaticTable,
       "lgs2624cARPInspectionStaticEntry": lgs2624cARPInspectionStaticEntry,
       "lgs2624cARPInspectionStaticIndex": lgs2624cARPInspectionStaticIndex,
       "lgs2624cARPInspectionStaticPort": lgs2624cARPInspectionStaticPort,
       "lgs2624cARPInspectionStaticVLANId": lgs2624cARPInspectionStaticVLANId,
       "lgs2624cARPInspectionStaticIPAddress": lgs2624cARPInspectionStaticIPAddress,
       "lgs2624cARPInspectionStaticMACAddress": lgs2624cARPInspectionStaticMACAddress,
       "lgs2624cARPInspectionStaticRowStatus": lgs2624cARPInspectionStaticRowStatus,
       "lgs2624cARPInspectionDynamicTable": lgs2624cARPInspectionDynamicTable,
       "lgs2624cARPInspectionDynamicEntry": lgs2624cARPInspectionDynamicEntry,
       "lgs2624cARPInspectionDynamicIndex": lgs2624cARPInspectionDynamicIndex,
       "lgs2624cARPInspectionDynamicPort": lgs2624cARPInspectionDynamicPort,
       "lgs2624cARPInspectionDynamicVLANId": lgs2624cARPInspectionDynamicVLANId,
       "lgs2624cARPInspectionDynamicIPAddress": lgs2624cARPInspectionDynamicIPAddress,
       "lgs2624cARPInspectionDynamicMACAddress": lgs2624cARPInspectionDynamicMACAddress,
       "lgs2624cDHCPSnooping": lgs2624cDHCPSnooping,
       "lgs2624cDHCPSnoopingConf": lgs2624cDHCPSnoopingConf,
       "lgs2624cDHCPSnoopingMode": lgs2624cDHCPSnoopingMode,
       "lgs2624cDHCPSnoopingPortModeConfigurationTable": lgs2624cDHCPSnoopingPortModeConfigurationTable,
       "lgs2624cDHCPSnoopingPortModeConfigurationEntry": lgs2624cDHCPSnoopingPortModeConfigurationEntry,
       "lgs2624cDHCPSnoopingPortModeConfigurationPort": lgs2624cDHCPSnoopingPortModeConfigurationPort,
       "lgs2624cDHCPSnoopingPortModeConfigurationMode": lgs2624cDHCPSnoopingPortModeConfigurationMode,
       "lgs2624cDHCPSnoopingStatisticsTable": lgs2624cDHCPSnoopingStatisticsTable,
       "lgs2624cDHCPSnoopingStatisticsEntry": lgs2624cDHCPSnoopingStatisticsEntry,
       "lgs2624cDHCPSnoopingStatisticsPort": lgs2624cDHCPSnoopingStatisticsPort,
       "lgs2624cDHCPSnoopingStatisticsClear": lgs2624cDHCPSnoopingStatisticsClear,
       "lgs2624cDHCPSnoopingRxDiscover": lgs2624cDHCPSnoopingRxDiscover,
       "lgs2624cDHCPSnoopingRxOffer": lgs2624cDHCPSnoopingRxOffer,
       "lgs2624cDHCPSnoopingRxRequest": lgs2624cDHCPSnoopingRxRequest,
       "lgs2624cDHCPSnoopingRxDecline": lgs2624cDHCPSnoopingRxDecline,
       "lgs2624cDHCPSnoopingRxACK": lgs2624cDHCPSnoopingRxACK,
       "lgs2624cDHCPSnoopingRxNAK": lgs2624cDHCPSnoopingRxNAK,
       "lgs2624cDHCPSnoopingRxRelease": lgs2624cDHCPSnoopingRxRelease,
       "lgs2624cDHCPSnoopingRxInform": lgs2624cDHCPSnoopingRxInform,
       "lgs2624cDHCPSnoopingRxLeaseQuery": lgs2624cDHCPSnoopingRxLeaseQuery,
       "lgs2624cDHCPSnoopingRxLeaseUnassigned": lgs2624cDHCPSnoopingRxLeaseUnassigned,
       "lgs2624cDHCPSnoopingRxLeaseUnknown": lgs2624cDHCPSnoopingRxLeaseUnknown,
       "lgs2624cDHCPSnoopingRxLeaseActive": lgs2624cDHCPSnoopingRxLeaseActive,
       "lgs2624cDHCPSnoopingTxDiscover": lgs2624cDHCPSnoopingTxDiscover,
       "lgs2624cDHCPSnoopingTxOffer": lgs2624cDHCPSnoopingTxOffer,
       "lgs2624cDHCPSnoopingTxRequest": lgs2624cDHCPSnoopingTxRequest,
       "lgs2624cDHCPSnoopingTxDecline": lgs2624cDHCPSnoopingTxDecline,
       "lgs2624cDHCPSnoopingTxACK": lgs2624cDHCPSnoopingTxACK,
       "lgs2624cDHCPSnoopingTxNAK": lgs2624cDHCPSnoopingTxNAK,
       "lgs2624cDHCPSnoopingTxRelease": lgs2624cDHCPSnoopingTxRelease,
       "lgs2624cDHCPSnoopingTxInform": lgs2624cDHCPSnoopingTxInform,
       "lgs2624cDHCPSnoopingTxLeaseQuery": lgs2624cDHCPSnoopingTxLeaseQuery,
       "lgs2624cDHCPSnoopingTxLeaseUnassigned": lgs2624cDHCPSnoopingTxLeaseUnassigned,
       "lgs2624cDHCPSnoopingTxLeaseUnknown": lgs2624cDHCPSnoopingTxLeaseUnknown,
       "lgs2624cDHCPSnoopingTxLeaseActive": lgs2624cDHCPSnoopingTxLeaseActive,
       "lgs2624cDHCPRelay": lgs2624cDHCPRelay,
       "lgs2624cDHCPRelayConfiguration": lgs2624cDHCPRelayConfiguration,
       "lgs2624cDHCPRelayMode": lgs2624cDHCPRelayMode,
       "lgs2624cDHCPRelayServer": lgs2624cDHCPRelayServer,
       "lgs2624cDHCPRelayInformationMode": lgs2624cDHCPRelayInformationMode,
       "lgs2624cDHCPRelayInformationPolicy": lgs2624cDHCPRelayInformationPolicy,
       "lgs2624cDHCPRelayStatistics": lgs2624cDHCPRelayStatistics,
       "lgs2624cDHCPRelayServerStatistics": lgs2624cDHCPRelayServerStatistics,
       "lgs2624cServerStatTransmitToServer": lgs2624cServerStatTransmitToServer,
       "lgs2624cServerStatTransmitError": lgs2624cServerStatTransmitError,
       "lgs2624cServerStatReceiveFromServer": lgs2624cServerStatReceiveFromServer,
       "lgs2624cServerStatReceiveMissingAgentOption": lgs2624cServerStatReceiveMissingAgentOption,
       "lgs2624cServerStatReceiveMissingCircuitID": lgs2624cServerStatReceiveMissingCircuitID,
       "lgs2624cServerStatReceiveMissingRemoteID": lgs2624cServerStatReceiveMissingRemoteID,
       "lgs2624cServerStatReceiveBadCircuitID": lgs2624cServerStatReceiveBadCircuitID,
       "lgs2624cServerStatReceiveBadRemoteID": lgs2624cServerStatReceiveBadRemoteID,
       "lgs2624cDHCPRelayClientStatistics": lgs2624cDHCPRelayClientStatistics,
       "lgs2624cClientStatTransmitToClient": lgs2624cClientStatTransmitToClient,
       "lgs2624cClientStatTransmitError": lgs2624cClientStatTransmitError,
       "lgs2624cClientStatReceivefromClient": lgs2624cClientStatReceivefromClient,
       "lgs2624cClientStatReceiveAgentOption": lgs2624cClientStatReceiveAgentOption,
       "lgs2624cClientStatReplaceAgentOption": lgs2624cClientStatReplaceAgentOption,
       "lgs2624cClientStatKeepAgentOption": lgs2624cClientStatKeepAgentOption,
       "lgs2624cClientStatDropAgentOption": lgs2624cClientStatDropAgentOption,
       "lgs2624cPortSecurity": lgs2624cPortSecurity,
       "lgs2624cPortSecLimitCtrl": lgs2624cPortSecLimitCtrl,
       "lgs2624cPortSecLimitCtrlSystemConf": lgs2624cPortSecLimitCtrlSystemConf,
       "lgs2624cPortSecurityMode": lgs2624cPortSecurityMode,
       "lgs2624cPortSecurityAging": lgs2624cPortSecurityAging,
       "lgs2624cPortSecurityAgingPeriod": lgs2624cPortSecurityAgingPeriod,
       "lgs2624cPortSecLimitCtrlTable": lgs2624cPortSecLimitCtrlTable,
       "lgs2624cPortSecLimitCtrlEntry": lgs2624cPortSecLimitCtrlEntry,
       "lgs2624cPortSecLimitCtrlPort": lgs2624cPortSecLimitCtrlPort,
       "lgs2624cPortSecLimitCtrlPortMode": lgs2624cPortSecLimitCtrlPortMode,
       "lgs2624cPortSecLimitCtrlPortLimit": lgs2624cPortSecLimitCtrlPortLimit,
       "lgs2624cPortSecLimitCtrlPortAction": lgs2624cPortSecLimitCtrlPortAction,
       "lgs2624cPortSecLimitCtrlPortState": lgs2624cPortSecLimitCtrlPortState,
       "lgs2624cPortSecLimitCtrlPortReOpen": lgs2624cPortSecLimitCtrlPortReOpen,
       "lgs2624cPortSecSwitchStatusTable": lgs2624cPortSecSwitchStatusTable,
       "lgs2624cPortSecSwitchStatusEntry": lgs2624cPortSecSwitchStatusEntry,
       "lgs2624cPortSecSwitchStatusPort": lgs2624cPortSecSwitchStatusPort,
       "lgs2624cPortSecSwitchStatusUsers": lgs2624cPortSecSwitchStatusUsers,
       "lgs2624cPortSecSwitchStatusState": lgs2624cPortSecSwitchStatusState,
       "lgs2624cPortSecSwitchStatusMACCountCurrent": lgs2624cPortSecSwitchStatusMACCountCurrent,
       "lgs2624cPortSecSwitchStatusMACCountLimit": lgs2624cPortSecSwitchStatusMACCountLimit,
       "lgs2624cPortSecPortStatus": lgs2624cPortSecPortStatus,
       "lgs2624cPortSecPortStatusPort": lgs2624cPortSecPortStatusPort,
       "lgs2624cPortSecPortStatusTable": lgs2624cPortSecPortStatusTable,
       "lgs2624cPortSecPortStatusEntry": lgs2624cPortSecPortStatusEntry,
       "lgs2624cPortSecPortStatusIndex": lgs2624cPortSecPortStatusIndex,
       "lgs2624cPortSecPortStatusMACAddress": lgs2624cPortSecPortStatusMACAddress,
       "lgs2624cPortSecPortStatusVLANId": lgs2624cPortSecPortStatusVLANId,
       "lgs2624cPortSecPortStatusState": lgs2624cPortSecPortStatusState,
       "lgs2624cPortSecPortStatusTimeOfAddition": lgs2624cPortSecPortStatusTimeOfAddition,
       "lgs2624cPortSecPortStatusAgeAndHold": lgs2624cPortSecPortStatusAgeAndHold,
       "lgs2624cAccessManagement": lgs2624cAccessManagement,
       "lgs2624cAccessMgtConf": lgs2624cAccessMgtConf,
       "lgs2624cAccessMgtConfMode": lgs2624cAccessMgtConfMode,
       "lgs2624cAccessMgtConfCreate": lgs2624cAccessMgtConfCreate,
       "lgs2624cAccessMgtConfTable": lgs2624cAccessMgtConfTable,
       "lgs2624cAccessMgtConfEntry": lgs2624cAccessMgtConfEntry,
       "lgs2624cAccessMgtIndex": lgs2624cAccessMgtIndex,
       "lgs2624cAccessMgtAddresstype": lgs2624cAccessMgtAddresstype,
       "lgs2624cAccessMgtStartIpAddress": lgs2624cAccessMgtStartIpAddress,
       "lgs2624cAccessMgtEndIpAddress": lgs2624cAccessMgtEndIpAddress,
       "lgs2624cAccessMgtHttpHttps": lgs2624cAccessMgtHttpHttps,
       "lgs2624cAccessMgtSNMP": lgs2624cAccessMgtSNMP,
       "lgs2624cAccessMgtTelnetSSH": lgs2624cAccessMgtTelnetSSH,
       "lgs2624cAccessMgtRowStatus": lgs2624cAccessMgtRowStatus,
       "lgs2624cAccessMgtStatistics": lgs2624cAccessMgtStatistics,
       "lgs2624cHttpReceivedPkts": lgs2624cHttpReceivedPkts,
       "lgs2624cHttpAllowedPkts": lgs2624cHttpAllowedPkts,
       "lgs2624cHttpDiscardedPkts": lgs2624cHttpDiscardedPkts,
       "lgs2624cHttpsReceivedPkts": lgs2624cHttpsReceivedPkts,
       "lgs2624cHttpsAllowedPkts": lgs2624cHttpsAllowedPkts,
       "lgs2624cHttpsDiscardedPkts": lgs2624cHttpsDiscardedPkts,
       "lgs2624cSnmpReceivedPkts": lgs2624cSnmpReceivedPkts,
       "lgs2624cSnmpAllowedPkts": lgs2624cSnmpAllowedPkts,
       "lgs2624cSnmpDiscardedPkts": lgs2624cSnmpDiscardedPkts,
       "lgs2624cTelnetReceivedPkts": lgs2624cTelnetReceivedPkts,
       "lgs2624cTelnetAllowedPkts": lgs2624cTelnetAllowedPkts,
       "lgs2624cTelnetDiscardedPkts": lgs2624cTelnetDiscardedPkts,
       "lgs2624cSSHReceivedPkts": lgs2624cSSHReceivedPkts,
       "lgs2624cSSHAllowedPkts": lgs2624cSSHAllowedPkts,
       "lgs2624cSSHDiscardedPkts": lgs2624cSSHDiscardedPkts,
       "lgs2624cAccessMgtStatisticsClearAll": lgs2624cAccessMgtStatisticsClearAll,
       "lgs2624cSSH": lgs2624cSSH,
       "lgs2624cSSHMode": lgs2624cSSHMode,
       "lgs2624cHTTPS": lgs2624cHTTPS,
       "lgs2624cHTTPSMode": lgs2624cHTTPSMode,
       "lgs2624cHTTPSAutoRedirect": lgs2624cHTTPSAutoRedirect,
       "lgs2624cAuthMethod": lgs2624cAuthMethod,
       "lgs2624cConsoleAuthMethod": lgs2624cConsoleAuthMethod,
       "lgs2624cConsoleFallback": lgs2624cConsoleFallback,
       "lgs2624cTelnetAuthMethod": lgs2624cTelnetAuthMethod,
       "lgs2624cTelnetFallback": lgs2624cTelnetFallback,
       "lgs2624cSshAuthMethod": lgs2624cSshAuthMethod,
       "lgs2624cSshFallback": lgs2624cSshFallback,
       "lgs2624cWebAuthMethod": lgs2624cWebAuthMethod,
       "lgs2624cWebFallback": lgs2624cWebFallback,
       "lgs2624cMaintenance": lgs2624cMaintenance,
       "lgs2624cRestartDevice": lgs2624cRestartDevice,
       "lgs2624cFirmware": lgs2624cFirmware,
       "lgs2624cFirmwareIpAddress": lgs2624cFirmwareIpAddress,
       "lgs2624cFirmwareFileName": lgs2624cFirmwareFileName,
       "lgs2624cDoFirmwareUpgrade": lgs2624cDoFirmwareUpgrade,
       "lgs2624cSaveOrRestore": lgs2624cSaveOrRestore,
       "lgs2624cFactoryDefaults": lgs2624cFactoryDefaults,
       "lgs2624cSaveStart": lgs2624cSaveStart,
       "lgs2624cSaveUser": lgs2624cSaveUser,
       "lgs2624cRestoreUser": lgs2624cRestoreUser,
       "lgs2624cExportOrImport": lgs2624cExportOrImport,
       "lgs2624cExportIpAddress": lgs2624cExportIpAddress,
       "lgs2624cExportConfigName": lgs2624cExportConfigName,
       "lgs2624cDoExportConfig": lgs2624cDoExportConfig,
       "lgs2624cImportIpAddress": lgs2624cImportIpAddress,
       "lgs2624cImportConfigName": lgs2624cImportConfigName,
       "lgs2624cDoImportConfig": lgs2624cDoImportConfig,
       "lgs2624cDiagnostics": lgs2624cDiagnostics,
       "lgs2624cPingIpAddress": lgs2624cPingIpAddress,
       "lgs2624cPingSize": lgs2624cPingSize,
       "lgs2624cDoPingConfig": lgs2624cDoPingConfig,
       "lgs2624cPingResult": lgs2624cPingResult,
       "lgs2624cPing6IpAddress": lgs2624cPing6IpAddress,
       "lgs2624cPing6Size": lgs2624cPing6Size,
       "lgs2624cDoPing6Config": lgs2624cDoPing6Config,
       "lgs2624cPing6Result": lgs2624cPing6Result,
       "lgs2624cVeriPHY": lgs2624cVeriPHY,
       "lgs2624cVeriPHYTest": lgs2624cVeriPHYTest,
       "lgs2624cVeriPHYTable": lgs2624cVeriPHYTable,
       "lgs2624cVeriPHYEntry": lgs2624cVeriPHYEntry,
       "lgs2624cVeriPHYPort": lgs2624cVeriPHYPort,
       "lgs2624cVeriPHYPairA": lgs2624cVeriPHYPairA,
       "lgs2624cVeriPHYLengthA": lgs2624cVeriPHYLengthA,
       "lgs2624cVeriPHYPairB": lgs2624cVeriPHYPairB,
       "lgs2624cVeriPHYLengthB": lgs2624cVeriPHYLengthB,
       "lgs2624cVeriPHYPairC": lgs2624cVeriPHYPairC,
       "lgs2624cVeriPHYLengthC": lgs2624cVeriPHYLengthC,
       "lgs2624cVeriPHYPairD": lgs2624cVeriPHYPairD,
       "lgs2624cVeriPHYLengthD": lgs2624cVeriPHYLengthD,
       "lgs2624cTrap": lgs2624cTrap,
       "lgs2624cTrapEvent": lgs2624cTrapEvent,
       "lgs2624cEmergency": lgs2624cEmergency,
       "lgs2624cAlert": lgs2624cAlert,
       "lgs2624cCritical": lgs2624cCritical,
       "lgs2624cError": lgs2624cError,
       "lgs2624cWarning": lgs2624cWarning,
       "lgs2624cNotice": lgs2624cNotice,
       "lgs2624cInformational": lgs2624cInformational,
       "lgs2624cDebug": lgs2624cDebug,
       "lgs2624cTrapVariable": lgs2624cTrapVariable,
       "lgs2624cInformation": lgs2624cInformation}
)
