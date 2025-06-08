# SNMP MIB module (CIE1000-SYSUTIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-SYSUTIL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:42 2025
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

(CIE1000DisplayString,
 CIE1000InterfaceIndex) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000DisplayString",
    "CIE1000InterfaceIndex")

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cie1000SysutilMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24)
)
if mibBuilder.loadTexts:
    cie1000SysutilMib.setRevisions(
        ("2016-02-25 00:00",
         "2016-02-17 00:00",
         "2016-02-15 00:00",
         "2015-11-02 00:00",
         "2015-10-30 00:00",
         "2015-10-20 00:00",
         "2015-10-15 00:00",
         "2014-11-11 00:00",
         "2014-10-10 00:00",
         "2014-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CIE1000SysutilLedColor(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("green", 1),
          ("red", 2),
          ("amber", 3),
          ("green-red", 4),
          ("green-amber", 5))
    )



class CIE1000SysutilLedMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("initial", 0),
          ("solid", 1),
          ("off", 2),
          ("blinking", 3),
          ("alternative", 4))
    )



class CIE1000SysutilLedNameIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("alm", 0),
          ("dca", 1),
          ("dcb", 2),
          ("exp", 3),
          ("poe", 4),
          ("sys", 5))
    )



class CIE1000SysutilPowerSupplyStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("standby", 1),
          ("notPresent", 2))
    )



class CIE1000SysutilRebootType(TextualConvention, Integer32):
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
        *(("noReboot", 0),
          ("coldReboot", 1),
          ("warmReboot", 2),
          ("factoryReset", 3))
    )



class CIE1000SysutilSystemLedClearType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("fatal", 1),
          ("software", 2),
          ("post", 3),
          ("ztp", 4),
          ("stackFwChk", 5))
    )



class CIE1000SysutilTemperatureMonitorSensorType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("board", 0),
          ("junction", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Cie1000SysutilMibObjects_ObjectIdentity = ObjectIdentity
cie1000SysutilMibObjects = _Cie1000SysutilMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1)
)
_Cie1000SysutilCapabilities_ObjectIdentity = ObjectIdentity
cie1000SysutilCapabilities = _Cie1000SysutilCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 1)
)
_Cie1000SysutilCapabilitiesWarmRebootSupported_Type = TruthValue
_Cie1000SysutilCapabilitiesWarmRebootSupported_Object = MibScalar
cie1000SysutilCapabilitiesWarmRebootSupported = _Cie1000SysutilCapabilitiesWarmRebootSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 1, 1),
    _Cie1000SysutilCapabilitiesWarmRebootSupported_Type()
)
cie1000SysutilCapabilitiesWarmRebootSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilCapabilitiesWarmRebootSupported.setStatus("current")
_Cie1000SysutilCapabilitiesPostSupported_Type = TruthValue
_Cie1000SysutilCapabilitiesPostSupported_Object = MibScalar
cie1000SysutilCapabilitiesPostSupported = _Cie1000SysutilCapabilitiesPostSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 1, 2),
    _Cie1000SysutilCapabilitiesPostSupported_Type()
)
cie1000SysutilCapabilitiesPostSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilCapabilitiesPostSupported.setStatus("current")
_Cie1000SysutilCapabilitiesZtpSupported_Type = TruthValue
_Cie1000SysutilCapabilitiesZtpSupported_Object = MibScalar
cie1000SysutilCapabilitiesZtpSupported = _Cie1000SysutilCapabilitiesZtpSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 1, 3),
    _Cie1000SysutilCapabilitiesZtpSupported_Type()
)
cie1000SysutilCapabilitiesZtpSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilCapabilitiesZtpSupported.setStatus("current")
_Cie1000SysutilCapabilitiesStackFwChkSupported_Type = TruthValue
_Cie1000SysutilCapabilitiesStackFwChkSupported_Object = MibScalar
cie1000SysutilCapabilitiesStackFwChkSupported = _Cie1000SysutilCapabilitiesStackFwChkSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 1, 4),
    _Cie1000SysutilCapabilitiesStackFwChkSupported_Type()
)
cie1000SysutilCapabilitiesStackFwChkSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilCapabilitiesStackFwChkSupported.setStatus("current")
_Cie1000SysutilConfig_ObjectIdentity = ObjectIdentity
cie1000SysutilConfig = _Cie1000SysutilConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 2)
)
_Cie1000SysutilConfigSystemInfo_ObjectIdentity = ObjectIdentity
cie1000SysutilConfigSystemInfo = _Cie1000SysutilConfigSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 2, 1)
)


class _Cie1000SysutilConfigSystemInfoHostname_Type(CIE1000DisplayString):
    """Custom type cie1000SysutilConfigSystemInfoHostname based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cie1000SysutilConfigSystemInfoHostname_Type.__name__ = "CIE1000DisplayString"
_Cie1000SysutilConfigSystemInfoHostname_Object = MibScalar
cie1000SysutilConfigSystemInfoHostname = _Cie1000SysutilConfigSystemInfoHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 2, 1, 1),
    _Cie1000SysutilConfigSystemInfoHostname_Type()
)
cie1000SysutilConfigSystemInfoHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SysutilConfigSystemInfoHostname.setStatus("current")


class _Cie1000SysutilConfigSystemInfoContact_Type(CIE1000DisplayString):
    """Custom type cie1000SysutilConfigSystemInfoContact based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cie1000SysutilConfigSystemInfoContact_Type.__name__ = "CIE1000DisplayString"
_Cie1000SysutilConfigSystemInfoContact_Object = MibScalar
cie1000SysutilConfigSystemInfoContact = _Cie1000SysutilConfigSystemInfoContact_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 2, 1, 2),
    _Cie1000SysutilConfigSystemInfoContact_Type()
)
cie1000SysutilConfigSystemInfoContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SysutilConfigSystemInfoContact.setStatus("current")


class _Cie1000SysutilConfigSystemInfoLocation_Type(CIE1000DisplayString):
    """Custom type cie1000SysutilConfigSystemInfoLocation based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cie1000SysutilConfigSystemInfoLocation_Type.__name__ = "CIE1000DisplayString"
_Cie1000SysutilConfigSystemInfoLocation_Object = MibScalar
cie1000SysutilConfigSystemInfoLocation = _Cie1000SysutilConfigSystemInfoLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 2, 1, 3),
    _Cie1000SysutilConfigSystemInfoLocation_Type()
)
cie1000SysutilConfigSystemInfoLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SysutilConfigSystemInfoLocation.setStatus("current")
_Cie1000SysutilConfigSystemTime_ObjectIdentity = ObjectIdentity
cie1000SysutilConfigSystemTime = _Cie1000SysutilConfigSystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 2, 2)
)


class _Cie1000SysutilConfigSystemTimeSystemCurTime_Type(CIE1000DisplayString):
    """Custom type cie1000SysutilConfigSystemTimeSystemCurTime based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Cie1000SysutilConfigSystemTimeSystemCurTime_Type.__name__ = "CIE1000DisplayString"
_Cie1000SysutilConfigSystemTimeSystemCurTime_Object = MibScalar
cie1000SysutilConfigSystemTimeSystemCurTime = _Cie1000SysutilConfigSystemTimeSystemCurTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 2, 2, 1),
    _Cie1000SysutilConfigSystemTimeSystemCurTime_Type()
)
cie1000SysutilConfigSystemTimeSystemCurTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SysutilConfigSystemTimeSystemCurTime.setStatus("current")


class _Cie1000SysutilConfigSystemTimeSystemCurTimeFormat_Type(CIE1000DisplayString):
    """Custom type cie1000SysutilConfigSystemTimeSystemCurTimeFormat based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Cie1000SysutilConfigSystemTimeSystemCurTimeFormat_Type.__name__ = "CIE1000DisplayString"
_Cie1000SysutilConfigSystemTimeSystemCurTimeFormat_Object = MibScalar
cie1000SysutilConfigSystemTimeSystemCurTimeFormat = _Cie1000SysutilConfigSystemTimeSystemCurTimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 2, 2, 2),
    _Cie1000SysutilConfigSystemTimeSystemCurTimeFormat_Type()
)
cie1000SysutilConfigSystemTimeSystemCurTimeFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SysutilConfigSystemTimeSystemCurTimeFormat.setStatus("current")
_Cie1000SysutilConfigTemperatureMonitorTable_Object = MibTable
cie1000SysutilConfigTemperatureMonitorTable = _Cie1000SysutilConfigTemperatureMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cie1000SysutilConfigTemperatureMonitorTable.setStatus("current")
_Cie1000SysutilConfigTemperatureMonitorEntry_Object = MibTableRow
cie1000SysutilConfigTemperatureMonitorEntry = _Cie1000SysutilConfigTemperatureMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 2, 3, 1)
)
cie1000SysutilConfigTemperatureMonitorEntry.setIndexNames(
    (0, "CIE1000-SYSUTIL-MIB", "cie1000SysutilConfigTemperatureMonitorSensorId"),
)
if mibBuilder.loadTexts:
    cie1000SysutilConfigTemperatureMonitorEntry.setStatus("current")
_Cie1000SysutilConfigTemperatureMonitorSensorId_Type = CIE1000SysutilTemperatureMonitorSensorType
_Cie1000SysutilConfigTemperatureMonitorSensorId_Object = MibTableColumn
cie1000SysutilConfigTemperatureMonitorSensorId = _Cie1000SysutilConfigTemperatureMonitorSensorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 2, 3, 1, 1),
    _Cie1000SysutilConfigTemperatureMonitorSensorId_Type()
)
cie1000SysutilConfigTemperatureMonitorSensorId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SysutilConfigTemperatureMonitorSensorId.setStatus("current")


class _Cie1000SysutilConfigTemperatureMonitorLowThreshold_Type(Integer32):
    """Custom type cie1000SysutilConfigTemperatureMonitorLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 125),
    )


_Cie1000SysutilConfigTemperatureMonitorLowThreshold_Type.__name__ = "Integer32"
_Cie1000SysutilConfigTemperatureMonitorLowThreshold_Object = MibTableColumn
cie1000SysutilConfigTemperatureMonitorLowThreshold = _Cie1000SysutilConfigTemperatureMonitorLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 2, 3, 1, 2),
    _Cie1000SysutilConfigTemperatureMonitorLowThreshold_Type()
)
cie1000SysutilConfigTemperatureMonitorLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SysutilConfigTemperatureMonitorLowThreshold.setStatus("current")


class _Cie1000SysutilConfigTemperatureMonitorHighThreshold_Type(Integer32):
    """Custom type cie1000SysutilConfigTemperatureMonitorHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 125),
    )


_Cie1000SysutilConfigTemperatureMonitorHighThreshold_Type.__name__ = "Integer32"
_Cie1000SysutilConfigTemperatureMonitorHighThreshold_Object = MibTableColumn
cie1000SysutilConfigTemperatureMonitorHighThreshold = _Cie1000SysutilConfigTemperatureMonitorHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 2, 3, 1, 3),
    _Cie1000SysutilConfigTemperatureMonitorHighThreshold_Type()
)
cie1000SysutilConfigTemperatureMonitorHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SysutilConfigTemperatureMonitorHighThreshold.setStatus("current")


class _Cie1000SysutilConfigTemperatureMonitorCriticalThreshold_Type(Integer32):
    """Custom type cie1000SysutilConfigTemperatureMonitorCriticalThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 150),
    )


_Cie1000SysutilConfigTemperatureMonitorCriticalThreshold_Type.__name__ = "Integer32"
_Cie1000SysutilConfigTemperatureMonitorCriticalThreshold_Object = MibTableColumn
cie1000SysutilConfigTemperatureMonitorCriticalThreshold = _Cie1000SysutilConfigTemperatureMonitorCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 2, 3, 1, 4),
    _Cie1000SysutilConfigTemperatureMonitorCriticalThreshold_Type()
)
cie1000SysutilConfigTemperatureMonitorCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SysutilConfigTemperatureMonitorCriticalThreshold.setStatus("current")


class _Cie1000SysutilConfigTemperatureMonitorHysteresis_Type(Integer32):
    """Custom type cie1000SysutilConfigTemperatureMonitorHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Cie1000SysutilConfigTemperatureMonitorHysteresis_Type.__name__ = "Integer32"
_Cie1000SysutilConfigTemperatureMonitorHysteresis_Object = MibTableColumn
cie1000SysutilConfigTemperatureMonitorHysteresis = _Cie1000SysutilConfigTemperatureMonitorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 2, 3, 1, 5),
    _Cie1000SysutilConfigTemperatureMonitorHysteresis_Type()
)
cie1000SysutilConfigTemperatureMonitorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SysutilConfigTemperatureMonitorHysteresis.setStatus("current")
_Cie1000SysutilStatus_ObjectIdentity = ObjectIdentity
cie1000SysutilStatus = _Cie1000SysutilStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3)
)
_Cie1000SysutilStatusCpuLoad_ObjectIdentity = ObjectIdentity
cie1000SysutilStatusCpuLoad = _Cie1000SysutilStatusCpuLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 1)
)
_Cie1000SysutilStatusCpuLoadAverage100msec_Type = Unsigned32
_Cie1000SysutilStatusCpuLoadAverage100msec_Object = MibScalar
cie1000SysutilStatusCpuLoadAverage100msec = _Cie1000SysutilStatusCpuLoadAverage100msec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 1, 1),
    _Cie1000SysutilStatusCpuLoadAverage100msec_Type()
)
cie1000SysutilStatusCpuLoadAverage100msec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusCpuLoadAverage100msec.setStatus("current")
_Cie1000SysutilStatusCpuLoadAverage1sec_Type = Unsigned32
_Cie1000SysutilStatusCpuLoadAverage1sec_Object = MibScalar
cie1000SysutilStatusCpuLoadAverage1sec = _Cie1000SysutilStatusCpuLoadAverage1sec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 1, 2),
    _Cie1000SysutilStatusCpuLoadAverage1sec_Type()
)
cie1000SysutilStatusCpuLoadAverage1sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusCpuLoadAverage1sec.setStatus("current")
_Cie1000SysutilStatusCpuLoadAverage10sec_Type = Unsigned32
_Cie1000SysutilStatusCpuLoadAverage10sec_Object = MibScalar
cie1000SysutilStatusCpuLoadAverage10sec = _Cie1000SysutilStatusCpuLoadAverage10sec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 1, 3),
    _Cie1000SysutilStatusCpuLoadAverage10sec_Type()
)
cie1000SysutilStatusCpuLoadAverage10sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusCpuLoadAverage10sec.setStatus("current")
_Cie1000SysutilStatusPowerSupplyTable_Object = MibTable
cie1000SysutilStatusPowerSupplyTable = _Cie1000SysutilStatusPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cie1000SysutilStatusPowerSupplyTable.setStatus("current")
_Cie1000SysutilStatusPowerSupplyEntry_Object = MibTableRow
cie1000SysutilStatusPowerSupplyEntry = _Cie1000SysutilStatusPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 2, 1)
)
cie1000SysutilStatusPowerSupplyEntry.setIndexNames(
    (0, "CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusPowerSupplySwitchId"),
    (0, "CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusPowerSupplyPsuId"),
)
if mibBuilder.loadTexts:
    cie1000SysutilStatusPowerSupplyEntry.setStatus("current")


class _Cie1000SysutilStatusPowerSupplySwitchId_Type(Integer32):
    """Custom type cie1000SysutilStatusPowerSupplySwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Cie1000SysutilStatusPowerSupplySwitchId_Type.__name__ = "Integer32"
_Cie1000SysutilStatusPowerSupplySwitchId_Object = MibTableColumn
cie1000SysutilStatusPowerSupplySwitchId = _Cie1000SysutilStatusPowerSupplySwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 2, 1, 1),
    _Cie1000SysutilStatusPowerSupplySwitchId_Type()
)
cie1000SysutilStatusPowerSupplySwitchId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SysutilStatusPowerSupplySwitchId.setStatus("current")


class _Cie1000SysutilStatusPowerSupplyPsuId_Type(Integer32):
    """Custom type cie1000SysutilStatusPowerSupplyPsuId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Cie1000SysutilStatusPowerSupplyPsuId_Type.__name__ = "Integer32"
_Cie1000SysutilStatusPowerSupplyPsuId_Object = MibTableColumn
cie1000SysutilStatusPowerSupplyPsuId = _Cie1000SysutilStatusPowerSupplyPsuId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 2, 1, 2),
    _Cie1000SysutilStatusPowerSupplyPsuId_Type()
)
cie1000SysutilStatusPowerSupplyPsuId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SysutilStatusPowerSupplyPsuId.setStatus("current")
_Cie1000SysutilStatusPowerSupplyState_Type = CIE1000SysutilPowerSupplyStateType
_Cie1000SysutilStatusPowerSupplyState_Object = MibTableColumn
cie1000SysutilStatusPowerSupplyState = _Cie1000SysutilStatusPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 2, 1, 3),
    _Cie1000SysutilStatusPowerSupplyState_Type()
)
cie1000SysutilStatusPowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusPowerSupplyState.setStatus("current")


class _Cie1000SysutilStatusPowerSupplyDescription_Type(CIE1000DisplayString):
    """Custom type cie1000SysutilStatusPowerSupplyDescription based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Cie1000SysutilStatusPowerSupplyDescription_Type.__name__ = "CIE1000DisplayString"
_Cie1000SysutilStatusPowerSupplyDescription_Object = MibTableColumn
cie1000SysutilStatusPowerSupplyDescription = _Cie1000SysutilStatusPowerSupplyDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 2, 1, 4),
    _Cie1000SysutilStatusPowerSupplyDescription_Type()
)
cie1000SysutilStatusPowerSupplyDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusPowerSupplyDescription.setStatus("current")
_Cie1000SysutilStatusSystemLedTable_Object = MibTable
cie1000SysutilStatusSystemLedTable = _Cie1000SysutilStatusSystemLedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cie1000SysutilStatusSystemLedTable.setStatus("current")
_Cie1000SysutilStatusSystemLedEntry_Object = MibTableRow
cie1000SysutilStatusSystemLedEntry = _Cie1000SysutilStatusSystemLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 3, 1)
)
cie1000SysutilStatusSystemLedEntry.setIndexNames(
    (0, "CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusSystemLedSwitchId"),
)
if mibBuilder.loadTexts:
    cie1000SysutilStatusSystemLedEntry.setStatus("current")


class _Cie1000SysutilStatusSystemLedSwitchId_Type(Integer32):
    """Custom type cie1000SysutilStatusSystemLedSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Cie1000SysutilStatusSystemLedSwitchId_Type.__name__ = "Integer32"
_Cie1000SysutilStatusSystemLedSwitchId_Object = MibTableColumn
cie1000SysutilStatusSystemLedSwitchId = _Cie1000SysutilStatusSystemLedSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 3, 1, 1),
    _Cie1000SysutilStatusSystemLedSwitchId_Type()
)
cie1000SysutilStatusSystemLedSwitchId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SysutilStatusSystemLedSwitchId.setStatus("current")


class _Cie1000SysutilStatusSystemLedDescription_Type(CIE1000DisplayString):
    """Custom type cie1000SysutilStatusSystemLedDescription based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Cie1000SysutilStatusSystemLedDescription_Type.__name__ = "CIE1000DisplayString"
_Cie1000SysutilStatusSystemLedDescription_Object = MibTableColumn
cie1000SysutilStatusSystemLedDescription = _Cie1000SysutilStatusSystemLedDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 3, 1, 2),
    _Cie1000SysutilStatusSystemLedDescription_Type()
)
cie1000SysutilStatusSystemLedDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusSystemLedDescription.setStatus("current")
_Cie1000SysutilStatusSystemUptime_ObjectIdentity = ObjectIdentity
cie1000SysutilStatusSystemUptime = _Cie1000SysutilStatusSystemUptime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 4)
)


class _Cie1000SysutilStatusSystemUptimeSystemUptime_Type(CIE1000DisplayString):
    """Custom type cie1000SysutilStatusSystemUptimeSystemUptime based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Cie1000SysutilStatusSystemUptimeSystemUptime_Type.__name__ = "CIE1000DisplayString"
_Cie1000SysutilStatusSystemUptimeSystemUptime_Object = MibScalar
cie1000SysutilStatusSystemUptimeSystemUptime = _Cie1000SysutilStatusSystemUptimeSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 4, 1),
    _Cie1000SysutilStatusSystemUptimeSystemUptime_Type()
)
cie1000SysutilStatusSystemUptimeSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusSystemUptimeSystemUptime.setStatus("current")
_Cie1000SysutilStatusBoardInfo_ObjectIdentity = ObjectIdentity
cie1000SysutilStatusBoardInfo = _Cie1000SysutilStatusBoardInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 5)
)
_Cie1000SysutilStatusBoardInfoBoardMacAddress_Type = MacAddress
_Cie1000SysutilStatusBoardInfoBoardMacAddress_Object = MibScalar
cie1000SysutilStatusBoardInfoBoardMacAddress = _Cie1000SysutilStatusBoardInfoBoardMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 5, 1),
    _Cie1000SysutilStatusBoardInfoBoardMacAddress_Type()
)
cie1000SysutilStatusBoardInfoBoardMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusBoardInfoBoardMacAddress.setStatus("current")
_Cie1000SysutilStatusBoardInfoBoardID_Type = Unsigned32
_Cie1000SysutilStatusBoardInfoBoardID_Object = MibScalar
cie1000SysutilStatusBoardInfoBoardID = _Cie1000SysutilStatusBoardInfoBoardID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 5, 2),
    _Cie1000SysutilStatusBoardInfoBoardID_Type()
)
cie1000SysutilStatusBoardInfoBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusBoardInfoBoardID.setStatus("current")


class _Cie1000SysutilStatusBoardInfoBoardSerial_Type(CIE1000DisplayString):
    """Custom type cie1000SysutilStatusBoardInfoBoardSerial based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Cie1000SysutilStatusBoardInfoBoardSerial_Type.__name__ = "CIE1000DisplayString"
_Cie1000SysutilStatusBoardInfoBoardSerial_Object = MibScalar
cie1000SysutilStatusBoardInfoBoardSerial = _Cie1000SysutilStatusBoardInfoBoardSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 5, 3),
    _Cie1000SysutilStatusBoardInfoBoardSerial_Type()
)
cie1000SysutilStatusBoardInfoBoardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusBoardInfoBoardSerial.setStatus("current")


class _Cie1000SysutilStatusBoardInfoBoardType_Type(CIE1000DisplayString):
    """Custom type cie1000SysutilStatusBoardInfoBoardType based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Cie1000SysutilStatusBoardInfoBoardType_Type.__name__ = "CIE1000DisplayString"
_Cie1000SysutilStatusBoardInfoBoardType_Object = MibScalar
cie1000SysutilStatusBoardInfoBoardType = _Cie1000SysutilStatusBoardInfoBoardType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 5, 4),
    _Cie1000SysutilStatusBoardInfoBoardType_Type()
)
cie1000SysutilStatusBoardInfoBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusBoardInfoBoardType.setStatus("current")


class _Cie1000SysutilStatusBoardInfoCipSerial_Type(CIE1000DisplayString):
    """Custom type cie1000SysutilStatusBoardInfoCipSerial based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Cie1000SysutilStatusBoardInfoCipSerial_Type.__name__ = "CIE1000DisplayString"
_Cie1000SysutilStatusBoardInfoCipSerial_Object = MibScalar
cie1000SysutilStatusBoardInfoCipSerial = _Cie1000SysutilStatusBoardInfoCipSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 5, 5),
    _Cie1000SysutilStatusBoardInfoCipSerial_Type()
)
cie1000SysutilStatusBoardInfoCipSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusBoardInfoCipSerial.setStatus("current")
_Cie1000SysutilStatusTemperatureMonitorTable_Object = MibTable
cie1000SysutilStatusTemperatureMonitorTable = _Cie1000SysutilStatusTemperatureMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 6)
)
if mibBuilder.loadTexts:
    cie1000SysutilStatusTemperatureMonitorTable.setStatus("current")
_Cie1000SysutilStatusTemperatureMonitorEntry_Object = MibTableRow
cie1000SysutilStatusTemperatureMonitorEntry = _Cie1000SysutilStatusTemperatureMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 6, 1)
)
cie1000SysutilStatusTemperatureMonitorEntry.setIndexNames(
    (0, "CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusTemperatureMonitorSensorId"),
)
if mibBuilder.loadTexts:
    cie1000SysutilStatusTemperatureMonitorEntry.setStatus("current")
_Cie1000SysutilStatusTemperatureMonitorSensorId_Type = CIE1000SysutilTemperatureMonitorSensorType
_Cie1000SysutilStatusTemperatureMonitorSensorId_Object = MibTableColumn
cie1000SysutilStatusTemperatureMonitorSensorId = _Cie1000SysutilStatusTemperatureMonitorSensorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 6, 1, 1),
    _Cie1000SysutilStatusTemperatureMonitorSensorId_Type()
)
cie1000SysutilStatusTemperatureMonitorSensorId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SysutilStatusTemperatureMonitorSensorId.setStatus("current")
_Cie1000SysutilStatusTemperatureMonitorLowAlarm_Type = TruthValue
_Cie1000SysutilStatusTemperatureMonitorLowAlarm_Object = MibTableColumn
cie1000SysutilStatusTemperatureMonitorLowAlarm = _Cie1000SysutilStatusTemperatureMonitorLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 6, 1, 2),
    _Cie1000SysutilStatusTemperatureMonitorLowAlarm_Type()
)
cie1000SysutilStatusTemperatureMonitorLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusTemperatureMonitorLowAlarm.setStatus("current")
_Cie1000SysutilStatusTemperatureMonitorHighAlarm_Type = TruthValue
_Cie1000SysutilStatusTemperatureMonitorHighAlarm_Object = MibTableColumn
cie1000SysutilStatusTemperatureMonitorHighAlarm = _Cie1000SysutilStatusTemperatureMonitorHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 6, 1, 3),
    _Cie1000SysutilStatusTemperatureMonitorHighAlarm_Type()
)
cie1000SysutilStatusTemperatureMonitorHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusTemperatureMonitorHighAlarm.setStatus("current")
_Cie1000SysutilStatusTemperatureMonitorCriticalAlarm_Type = TruthValue
_Cie1000SysutilStatusTemperatureMonitorCriticalAlarm_Object = MibTableColumn
cie1000SysutilStatusTemperatureMonitorCriticalAlarm = _Cie1000SysutilStatusTemperatureMonitorCriticalAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 6, 1, 4),
    _Cie1000SysutilStatusTemperatureMonitorCriticalAlarm_Type()
)
cie1000SysutilStatusTemperatureMonitorCriticalAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusTemperatureMonitorCriticalAlarm.setStatus("current")
_Cie1000SysutilStatusTemperatureMonitorTemperature_Type = Integer32
_Cie1000SysutilStatusTemperatureMonitorTemperature_Object = MibTableColumn
cie1000SysutilStatusTemperatureMonitorTemperature = _Cie1000SysutilStatusTemperatureMonitorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 6, 1, 5),
    _Cie1000SysutilStatusTemperatureMonitorTemperature_Type()
)
cie1000SysutilStatusTemperatureMonitorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusTemperatureMonitorTemperature.setStatus("current")
_Cie1000SysutilStatusLedStatus_ObjectIdentity = ObjectIdentity
cie1000SysutilStatusLedStatus = _Cie1000SysutilStatusLedStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 7)
)
_Cie1000SysutilStatusLedStatusSystemTable_Object = MibTable
cie1000SysutilStatusLedStatusSystemTable = _Cie1000SysutilStatusLedStatusSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 7, 1)
)
if mibBuilder.loadTexts:
    cie1000SysutilStatusLedStatusSystemTable.setStatus("current")
_Cie1000SysutilStatusLedStatusSystemEntry_Object = MibTableRow
cie1000SysutilStatusLedStatusSystemEntry = _Cie1000SysutilStatusLedStatusSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 7, 1, 1)
)
cie1000SysutilStatusLedStatusSystemEntry.setIndexNames(
    (0, "CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusLedStatusSystemLedId"),
)
if mibBuilder.loadTexts:
    cie1000SysutilStatusLedStatusSystemEntry.setStatus("current")
_Cie1000SysutilStatusLedStatusSystemLedId_Type = CIE1000SysutilLedNameIndex
_Cie1000SysutilStatusLedStatusSystemLedId_Object = MibTableColumn
cie1000SysutilStatusLedStatusSystemLedId = _Cie1000SysutilStatusLedStatusSystemLedId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 7, 1, 1, 1),
    _Cie1000SysutilStatusLedStatusSystemLedId_Type()
)
cie1000SysutilStatusLedStatusSystemLedId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SysutilStatusLedStatusSystemLedId.setStatus("current")
_Cie1000SysutilStatusLedStatusSystemLedColor_Type = CIE1000SysutilLedColor
_Cie1000SysutilStatusLedStatusSystemLedColor_Object = MibTableColumn
cie1000SysutilStatusLedStatusSystemLedColor = _Cie1000SysutilStatusLedStatusSystemLedColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 7, 1, 1, 2),
    _Cie1000SysutilStatusLedStatusSystemLedColor_Type()
)
cie1000SysutilStatusLedStatusSystemLedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusLedStatusSystemLedColor.setStatus("current")
_Cie1000SysutilStatusLedStatusSystemLedMode_Type = CIE1000SysutilLedMode
_Cie1000SysutilStatusLedStatusSystemLedMode_Object = MibTableColumn
cie1000SysutilStatusLedStatusSystemLedMode = _Cie1000SysutilStatusLedStatusSystemLedMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 7, 1, 1, 3),
    _Cie1000SysutilStatusLedStatusSystemLedMode_Type()
)
cie1000SysutilStatusLedStatusSystemLedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusLedStatusSystemLedMode.setStatus("current")


class _Cie1000SysutilStatusLedStatusSystemDescription_Type(CIE1000DisplayString):
    """Custom type cie1000SysutilStatusLedStatusSystemDescription based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Cie1000SysutilStatusLedStatusSystemDescription_Type.__name__ = "CIE1000DisplayString"
_Cie1000SysutilStatusLedStatusSystemDescription_Object = MibTableColumn
cie1000SysutilStatusLedStatusSystemDescription = _Cie1000SysutilStatusLedStatusSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 7, 1, 1, 4),
    _Cie1000SysutilStatusLedStatusSystemDescription_Type()
)
cie1000SysutilStatusLedStatusSystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusLedStatusSystemDescription.setStatus("current")
_Cie1000SysutilStatusLedStatusPortTable_Object = MibTable
cie1000SysutilStatusLedStatusPortTable = _Cie1000SysutilStatusLedStatusPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 7, 2)
)
if mibBuilder.loadTexts:
    cie1000SysutilStatusLedStatusPortTable.setStatus("current")
_Cie1000SysutilStatusLedStatusPortEntry_Object = MibTableRow
cie1000SysutilStatusLedStatusPortEntry = _Cie1000SysutilStatusLedStatusPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 7, 2, 1)
)
cie1000SysutilStatusLedStatusPortEntry.setIndexNames(
    (0, "CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusLedStatusPortIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000SysutilStatusLedStatusPortEntry.setStatus("current")
_Cie1000SysutilStatusLedStatusPortIfIndex_Type = CIE1000InterfaceIndex
_Cie1000SysutilStatusLedStatusPortIfIndex_Object = MibTableColumn
cie1000SysutilStatusLedStatusPortIfIndex = _Cie1000SysutilStatusLedStatusPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 7, 2, 1, 1),
    _Cie1000SysutilStatusLedStatusPortIfIndex_Type()
)
cie1000SysutilStatusLedStatusPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SysutilStatusLedStatusPortIfIndex.setStatus("current")
_Cie1000SysutilStatusLedStatusPortLedColor_Type = CIE1000SysutilLedColor
_Cie1000SysutilStatusLedStatusPortLedColor_Object = MibTableColumn
cie1000SysutilStatusLedStatusPortLedColor = _Cie1000SysutilStatusLedStatusPortLedColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 7, 2, 1, 2),
    _Cie1000SysutilStatusLedStatusPortLedColor_Type()
)
cie1000SysutilStatusLedStatusPortLedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusLedStatusPortLedColor.setStatus("current")
_Cie1000SysutilStatusLedStatusPortLedMode_Type = CIE1000SysutilLedMode
_Cie1000SysutilStatusLedStatusPortLedMode_Object = MibTableColumn
cie1000SysutilStatusLedStatusPortLedMode = _Cie1000SysutilStatusLedStatusPortLedMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 7, 2, 1, 3),
    _Cie1000SysutilStatusLedStatusPortLedMode_Type()
)
cie1000SysutilStatusLedStatusPortLedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusLedStatusPortLedMode.setStatus("current")


class _Cie1000SysutilStatusLedStatusPortDescription_Type(CIE1000DisplayString):
    """Custom type cie1000SysutilStatusLedStatusPortDescription based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Cie1000SysutilStatusLedStatusPortDescription_Type.__name__ = "CIE1000DisplayString"
_Cie1000SysutilStatusLedStatusPortDescription_Object = MibTableColumn
cie1000SysutilStatusLedStatusPortDescription = _Cie1000SysutilStatusLedStatusPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 3, 7, 2, 1, 4),
    _Cie1000SysutilStatusLedStatusPortDescription_Type()
)
cie1000SysutilStatusLedStatusPortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SysutilStatusLedStatusPortDescription.setStatus("current")
_Cie1000SysutilControl_ObjectIdentity = ObjectIdentity
cie1000SysutilControl = _Cie1000SysutilControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 4)
)
_Cie1000SysutilControlRebootTable_Object = MibTable
cie1000SysutilControlRebootTable = _Cie1000SysutilControlRebootTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cie1000SysutilControlRebootTable.setStatus("current")
_Cie1000SysutilControlRebootEntry_Object = MibTableRow
cie1000SysutilControlRebootEntry = _Cie1000SysutilControlRebootEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 4, 1, 1)
)
cie1000SysutilControlRebootEntry.setIndexNames(
    (0, "CIE1000-SYSUTIL-MIB", "cie1000SysutilControlRebootSwitchId"),
)
if mibBuilder.loadTexts:
    cie1000SysutilControlRebootEntry.setStatus("current")


class _Cie1000SysutilControlRebootSwitchId_Type(Integer32):
    """Custom type cie1000SysutilControlRebootSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Cie1000SysutilControlRebootSwitchId_Type.__name__ = "Integer32"
_Cie1000SysutilControlRebootSwitchId_Object = MibTableColumn
cie1000SysutilControlRebootSwitchId = _Cie1000SysutilControlRebootSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 4, 1, 1, 1),
    _Cie1000SysutilControlRebootSwitchId_Type()
)
cie1000SysutilControlRebootSwitchId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SysutilControlRebootSwitchId.setStatus("current")
_Cie1000SysutilControlRebootType_Type = CIE1000SysutilRebootType
_Cie1000SysutilControlRebootType_Object = MibTableColumn
cie1000SysutilControlRebootType = _Cie1000SysutilControlRebootType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 4, 1, 1, 2),
    _Cie1000SysutilControlRebootType_Type()
)
cie1000SysutilControlRebootType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SysutilControlRebootType.setStatus("current")
_Cie1000SysutilControlSystemLedTable_Object = MibTable
cie1000SysutilControlSystemLedTable = _Cie1000SysutilControlSystemLedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cie1000SysutilControlSystemLedTable.setStatus("current")
_Cie1000SysutilControlSystemLedEntry_Object = MibTableRow
cie1000SysutilControlSystemLedEntry = _Cie1000SysutilControlSystemLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 4, 2, 1)
)
cie1000SysutilControlSystemLedEntry.setIndexNames(
    (0, "CIE1000-SYSUTIL-MIB", "cie1000SysutilControlSystemLedSwitchId"),
)
if mibBuilder.loadTexts:
    cie1000SysutilControlSystemLedEntry.setStatus("current")


class _Cie1000SysutilControlSystemLedSwitchId_Type(Integer32):
    """Custom type cie1000SysutilControlSystemLedSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Cie1000SysutilControlSystemLedSwitchId_Type.__name__ = "Integer32"
_Cie1000SysutilControlSystemLedSwitchId_Object = MibTableColumn
cie1000SysutilControlSystemLedSwitchId = _Cie1000SysutilControlSystemLedSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 4, 2, 1, 1),
    _Cie1000SysutilControlSystemLedSwitchId_Type()
)
cie1000SysutilControlSystemLedSwitchId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SysutilControlSystemLedSwitchId.setStatus("current")
_Cie1000SysutilControlSystemLedClearStatus_Type = CIE1000SysutilSystemLedClearType
_Cie1000SysutilControlSystemLedClearStatus_Object = MibTableColumn
cie1000SysutilControlSystemLedClearStatus = _Cie1000SysutilControlSystemLedClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 1, 4, 2, 1, 2),
    _Cie1000SysutilControlSystemLedClearStatus_Type()
)
cie1000SysutilControlSystemLedClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SysutilControlSystemLedClearStatus.setStatus("current")
_Cie1000SysutilMibConformance_ObjectIdentity = ObjectIdentity
cie1000SysutilMibConformance = _Cie1000SysutilMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 2)
)
_Cie1000SysutilMibCompliances_ObjectIdentity = ObjectIdentity
cie1000SysutilMibCompliances = _Cie1000SysutilMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 2, 1)
)
_Cie1000SysutilMibGroups_ObjectIdentity = ObjectIdentity
cie1000SysutilMibGroups = _Cie1000SysutilMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 2, 2)
)

# Managed Objects groups

cie1000SysutilCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 2, 2, 1)
)
cie1000SysutilCapabilitiesInfoGroup.setObjects(
      *(("CIE1000-SYSUTIL-MIB", "cie1000SysutilCapabilitiesWarmRebootSupported"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilCapabilitiesPostSupported"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilCapabilitiesZtpSupported"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilCapabilitiesStackFwChkSupported"))
)
if mibBuilder.loadTexts:
    cie1000SysutilCapabilitiesInfoGroup.setStatus("current")

cie1000SysutilConfigSystemInfoInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 2, 2, 2)
)
cie1000SysutilConfigSystemInfoInfoGroup.setObjects(
      *(("CIE1000-SYSUTIL-MIB", "cie1000SysutilConfigSystemInfoHostname"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilConfigSystemInfoContact"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilConfigSystemInfoLocation"))
)
if mibBuilder.loadTexts:
    cie1000SysutilConfigSystemInfoInfoGroup.setStatus("current")

cie1000SysutilConfigSystemTimeInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 2, 2, 3)
)
cie1000SysutilConfigSystemTimeInfoGroup.setObjects(
      *(("CIE1000-SYSUTIL-MIB", "cie1000SysutilConfigSystemTimeSystemCurTime"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilConfigSystemTimeSystemCurTimeFormat"))
)
if mibBuilder.loadTexts:
    cie1000SysutilConfigSystemTimeInfoGroup.setStatus("current")

cie1000SysutilConfigTemperatureMonitorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 2, 2, 4)
)
cie1000SysutilConfigTemperatureMonitorInfoGroup.setObjects(
      *(("CIE1000-SYSUTIL-MIB", "cie1000SysutilConfigTemperatureMonitorSensorId"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilConfigTemperatureMonitorLowThreshold"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilConfigTemperatureMonitorHighThreshold"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilConfigTemperatureMonitorCriticalThreshold"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilConfigTemperatureMonitorHysteresis"))
)
if mibBuilder.loadTexts:
    cie1000SysutilConfigTemperatureMonitorInfoGroup.setStatus("current")

cie1000SysutilStatusCpuLoadInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 2, 2, 5)
)
cie1000SysutilStatusCpuLoadInfoGroup.setObjects(
      *(("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusCpuLoadAverage100msec"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusCpuLoadAverage1sec"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusCpuLoadAverage10sec"))
)
if mibBuilder.loadTexts:
    cie1000SysutilStatusCpuLoadInfoGroup.setStatus("current")

cie1000SysutilStatusPowerSupplyInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 2, 2, 6)
)
cie1000SysutilStatusPowerSupplyInfoGroup.setObjects(
      *(("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusPowerSupplySwitchId"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusPowerSupplyPsuId"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusPowerSupplyState"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusPowerSupplyDescription"))
)
if mibBuilder.loadTexts:
    cie1000SysutilStatusPowerSupplyInfoGroup.setStatus("current")

cie1000SysutilStatusSystemLedInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 2, 2, 7)
)
cie1000SysutilStatusSystemLedInfoGroup.setObjects(
      *(("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusSystemLedSwitchId"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusSystemLedDescription"))
)
if mibBuilder.loadTexts:
    cie1000SysutilStatusSystemLedInfoGroup.setStatus("current")

cie1000SysutilStatusSystemUptimeInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 2, 2, 8)
)
cie1000SysutilStatusSystemUptimeInfoGroup.setObjects(
    ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusSystemUptimeSystemUptime")
)
if mibBuilder.loadTexts:
    cie1000SysutilStatusSystemUptimeInfoGroup.setStatus("current")

cie1000SysutilStatusBoardInfoInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 2, 2, 9)
)
cie1000SysutilStatusBoardInfoInfoGroup.setObjects(
      *(("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusBoardInfoBoardMacAddress"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusBoardInfoBoardID"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusBoardInfoBoardSerial"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusBoardInfoBoardType"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusBoardInfoCipSerial"))
)
if mibBuilder.loadTexts:
    cie1000SysutilStatusBoardInfoInfoGroup.setStatus("current")

cie1000SysutilStatusTemperatureMonitorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 2, 2, 10)
)
cie1000SysutilStatusTemperatureMonitorInfoGroup.setObjects(
      *(("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusTemperatureMonitorSensorId"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusTemperatureMonitorLowAlarm"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusTemperatureMonitorHighAlarm"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusTemperatureMonitorCriticalAlarm"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusTemperatureMonitorTemperature"))
)
if mibBuilder.loadTexts:
    cie1000SysutilStatusTemperatureMonitorInfoGroup.setStatus("current")

cie1000SysutilStatusLedStatusSystemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 2, 2, 11)
)
cie1000SysutilStatusLedStatusSystemInfoGroup.setObjects(
      *(("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusLedStatusSystemLedId"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusLedStatusSystemLedColor"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusLedStatusSystemLedMode"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusLedStatusSystemDescription"))
)
if mibBuilder.loadTexts:
    cie1000SysutilStatusLedStatusSystemInfoGroup.setStatus("current")

cie1000SysutilStatusLedStatusPortInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 2, 2, 12)
)
cie1000SysutilStatusLedStatusPortInfoGroup.setObjects(
      *(("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusLedStatusPortIfIndex"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusLedStatusPortLedColor"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusLedStatusPortLedMode"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusLedStatusPortDescription"))
)
if mibBuilder.loadTexts:
    cie1000SysutilStatusLedStatusPortInfoGroup.setStatus("current")

cie1000SysutilControlRebootInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 2, 2, 13)
)
cie1000SysutilControlRebootInfoGroup.setObjects(
      *(("CIE1000-SYSUTIL-MIB", "cie1000SysutilControlRebootSwitchId"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilControlRebootType"))
)
if mibBuilder.loadTexts:
    cie1000SysutilControlRebootInfoGroup.setStatus("current")

cie1000SysutilControlSystemLedInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 2, 2, 14)
)
cie1000SysutilControlSystemLedInfoGroup.setObjects(
      *(("CIE1000-SYSUTIL-MIB", "cie1000SysutilControlSystemLedSwitchId"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilControlSystemLedClearStatus"))
)
if mibBuilder.loadTexts:
    cie1000SysutilControlSystemLedInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000SysutilMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 24, 2, 1, 1)
)
cie1000SysutilMibCompliance.setObjects(
      *(("CIE1000-SYSUTIL-MIB", "cie1000SysutilCapabilitiesInfoGroup"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilConfigSystemInfoInfoGroup"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilConfigSystemTimeInfoGroup"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilConfigTemperatureMonitorInfoGroup"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusCpuLoadInfoGroup"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusPowerSupplyInfoGroup"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusSystemLedInfoGroup"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusSystemUptimeInfoGroup"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusBoardInfoInfoGroup"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusTemperatureMonitorInfoGroup"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusLedStatusSystemInfoGroup"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilStatusLedStatusPortInfoGroup"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilControlRebootInfoGroup"),
        ("CIE1000-SYSUTIL-MIB", "cie1000SysutilControlSystemLedInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000SysutilMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-SYSUTIL-MIB",
    **{"CIE1000SysutilLedColor": CIE1000SysutilLedColor,
       "CIE1000SysutilLedMode": CIE1000SysutilLedMode,
       "CIE1000SysutilLedNameIndex": CIE1000SysutilLedNameIndex,
       "CIE1000SysutilPowerSupplyStateType": CIE1000SysutilPowerSupplyStateType,
       "CIE1000SysutilRebootType": CIE1000SysutilRebootType,
       "CIE1000SysutilSystemLedClearType": CIE1000SysutilSystemLedClearType,
       "CIE1000SysutilTemperatureMonitorSensorType": CIE1000SysutilTemperatureMonitorSensorType,
       "cie1000SysutilMib": cie1000SysutilMib,
       "cie1000SysutilMibObjects": cie1000SysutilMibObjects,
       "cie1000SysutilCapabilities": cie1000SysutilCapabilities,
       "cie1000SysutilCapabilitiesWarmRebootSupported": cie1000SysutilCapabilitiesWarmRebootSupported,
       "cie1000SysutilCapabilitiesPostSupported": cie1000SysutilCapabilitiesPostSupported,
       "cie1000SysutilCapabilitiesZtpSupported": cie1000SysutilCapabilitiesZtpSupported,
       "cie1000SysutilCapabilitiesStackFwChkSupported": cie1000SysutilCapabilitiesStackFwChkSupported,
       "cie1000SysutilConfig": cie1000SysutilConfig,
       "cie1000SysutilConfigSystemInfo": cie1000SysutilConfigSystemInfo,
       "cie1000SysutilConfigSystemInfoHostname": cie1000SysutilConfigSystemInfoHostname,
       "cie1000SysutilConfigSystemInfoContact": cie1000SysutilConfigSystemInfoContact,
       "cie1000SysutilConfigSystemInfoLocation": cie1000SysutilConfigSystemInfoLocation,
       "cie1000SysutilConfigSystemTime": cie1000SysutilConfigSystemTime,
       "cie1000SysutilConfigSystemTimeSystemCurTime": cie1000SysutilConfigSystemTimeSystemCurTime,
       "cie1000SysutilConfigSystemTimeSystemCurTimeFormat": cie1000SysutilConfigSystemTimeSystemCurTimeFormat,
       "cie1000SysutilConfigTemperatureMonitorTable": cie1000SysutilConfigTemperatureMonitorTable,
       "cie1000SysutilConfigTemperatureMonitorEntry": cie1000SysutilConfigTemperatureMonitorEntry,
       "cie1000SysutilConfigTemperatureMonitorSensorId": cie1000SysutilConfigTemperatureMonitorSensorId,
       "cie1000SysutilConfigTemperatureMonitorLowThreshold": cie1000SysutilConfigTemperatureMonitorLowThreshold,
       "cie1000SysutilConfigTemperatureMonitorHighThreshold": cie1000SysutilConfigTemperatureMonitorHighThreshold,
       "cie1000SysutilConfigTemperatureMonitorCriticalThreshold": cie1000SysutilConfigTemperatureMonitorCriticalThreshold,
       "cie1000SysutilConfigTemperatureMonitorHysteresis": cie1000SysutilConfigTemperatureMonitorHysteresis,
       "cie1000SysutilStatus": cie1000SysutilStatus,
       "cie1000SysutilStatusCpuLoad": cie1000SysutilStatusCpuLoad,
       "cie1000SysutilStatusCpuLoadAverage100msec": cie1000SysutilStatusCpuLoadAverage100msec,
       "cie1000SysutilStatusCpuLoadAverage1sec": cie1000SysutilStatusCpuLoadAverage1sec,
       "cie1000SysutilStatusCpuLoadAverage10sec": cie1000SysutilStatusCpuLoadAverage10sec,
       "cie1000SysutilStatusPowerSupplyTable": cie1000SysutilStatusPowerSupplyTable,
       "cie1000SysutilStatusPowerSupplyEntry": cie1000SysutilStatusPowerSupplyEntry,
       "cie1000SysutilStatusPowerSupplySwitchId": cie1000SysutilStatusPowerSupplySwitchId,
       "cie1000SysutilStatusPowerSupplyPsuId": cie1000SysutilStatusPowerSupplyPsuId,
       "cie1000SysutilStatusPowerSupplyState": cie1000SysutilStatusPowerSupplyState,
       "cie1000SysutilStatusPowerSupplyDescription": cie1000SysutilStatusPowerSupplyDescription,
       "cie1000SysutilStatusSystemLedTable": cie1000SysutilStatusSystemLedTable,
       "cie1000SysutilStatusSystemLedEntry": cie1000SysutilStatusSystemLedEntry,
       "cie1000SysutilStatusSystemLedSwitchId": cie1000SysutilStatusSystemLedSwitchId,
       "cie1000SysutilStatusSystemLedDescription": cie1000SysutilStatusSystemLedDescription,
       "cie1000SysutilStatusSystemUptime": cie1000SysutilStatusSystemUptime,
       "cie1000SysutilStatusSystemUptimeSystemUptime": cie1000SysutilStatusSystemUptimeSystemUptime,
       "cie1000SysutilStatusBoardInfo": cie1000SysutilStatusBoardInfo,
       "cie1000SysutilStatusBoardInfoBoardMacAddress": cie1000SysutilStatusBoardInfoBoardMacAddress,
       "cie1000SysutilStatusBoardInfoBoardID": cie1000SysutilStatusBoardInfoBoardID,
       "cie1000SysutilStatusBoardInfoBoardSerial": cie1000SysutilStatusBoardInfoBoardSerial,
       "cie1000SysutilStatusBoardInfoBoardType": cie1000SysutilStatusBoardInfoBoardType,
       "cie1000SysutilStatusBoardInfoCipSerial": cie1000SysutilStatusBoardInfoCipSerial,
       "cie1000SysutilStatusTemperatureMonitorTable": cie1000SysutilStatusTemperatureMonitorTable,
       "cie1000SysutilStatusTemperatureMonitorEntry": cie1000SysutilStatusTemperatureMonitorEntry,
       "cie1000SysutilStatusTemperatureMonitorSensorId": cie1000SysutilStatusTemperatureMonitorSensorId,
       "cie1000SysutilStatusTemperatureMonitorLowAlarm": cie1000SysutilStatusTemperatureMonitorLowAlarm,
       "cie1000SysutilStatusTemperatureMonitorHighAlarm": cie1000SysutilStatusTemperatureMonitorHighAlarm,
       "cie1000SysutilStatusTemperatureMonitorCriticalAlarm": cie1000SysutilStatusTemperatureMonitorCriticalAlarm,
       "cie1000SysutilStatusTemperatureMonitorTemperature": cie1000SysutilStatusTemperatureMonitorTemperature,
       "cie1000SysutilStatusLedStatus": cie1000SysutilStatusLedStatus,
       "cie1000SysutilStatusLedStatusSystemTable": cie1000SysutilStatusLedStatusSystemTable,
       "cie1000SysutilStatusLedStatusSystemEntry": cie1000SysutilStatusLedStatusSystemEntry,
       "cie1000SysutilStatusLedStatusSystemLedId": cie1000SysutilStatusLedStatusSystemLedId,
       "cie1000SysutilStatusLedStatusSystemLedColor": cie1000SysutilStatusLedStatusSystemLedColor,
       "cie1000SysutilStatusLedStatusSystemLedMode": cie1000SysutilStatusLedStatusSystemLedMode,
       "cie1000SysutilStatusLedStatusSystemDescription": cie1000SysutilStatusLedStatusSystemDescription,
       "cie1000SysutilStatusLedStatusPortTable": cie1000SysutilStatusLedStatusPortTable,
       "cie1000SysutilStatusLedStatusPortEntry": cie1000SysutilStatusLedStatusPortEntry,
       "cie1000SysutilStatusLedStatusPortIfIndex": cie1000SysutilStatusLedStatusPortIfIndex,
       "cie1000SysutilStatusLedStatusPortLedColor": cie1000SysutilStatusLedStatusPortLedColor,
       "cie1000SysutilStatusLedStatusPortLedMode": cie1000SysutilStatusLedStatusPortLedMode,
       "cie1000SysutilStatusLedStatusPortDescription": cie1000SysutilStatusLedStatusPortDescription,
       "cie1000SysutilControl": cie1000SysutilControl,
       "cie1000SysutilControlRebootTable": cie1000SysutilControlRebootTable,
       "cie1000SysutilControlRebootEntry": cie1000SysutilControlRebootEntry,
       "cie1000SysutilControlRebootSwitchId": cie1000SysutilControlRebootSwitchId,
       "cie1000SysutilControlRebootType": cie1000SysutilControlRebootType,
       "cie1000SysutilControlSystemLedTable": cie1000SysutilControlSystemLedTable,
       "cie1000SysutilControlSystemLedEntry": cie1000SysutilControlSystemLedEntry,
       "cie1000SysutilControlSystemLedSwitchId": cie1000SysutilControlSystemLedSwitchId,
       "cie1000SysutilControlSystemLedClearStatus": cie1000SysutilControlSystemLedClearStatus,
       "cie1000SysutilMibConformance": cie1000SysutilMibConformance,
       "cie1000SysutilMibCompliances": cie1000SysutilMibCompliances,
       "cie1000SysutilMibCompliance": cie1000SysutilMibCompliance,
       "cie1000SysutilMibGroups": cie1000SysutilMibGroups,
       "cie1000SysutilCapabilitiesInfoGroup": cie1000SysutilCapabilitiesInfoGroup,
       "cie1000SysutilConfigSystemInfoInfoGroup": cie1000SysutilConfigSystemInfoInfoGroup,
       "cie1000SysutilConfigSystemTimeInfoGroup": cie1000SysutilConfigSystemTimeInfoGroup,
       "cie1000SysutilConfigTemperatureMonitorInfoGroup": cie1000SysutilConfigTemperatureMonitorInfoGroup,
       "cie1000SysutilStatusCpuLoadInfoGroup": cie1000SysutilStatusCpuLoadInfoGroup,
       "cie1000SysutilStatusPowerSupplyInfoGroup": cie1000SysutilStatusPowerSupplyInfoGroup,
       "cie1000SysutilStatusSystemLedInfoGroup": cie1000SysutilStatusSystemLedInfoGroup,
       "cie1000SysutilStatusSystemUptimeInfoGroup": cie1000SysutilStatusSystemUptimeInfoGroup,
       "cie1000SysutilStatusBoardInfoInfoGroup": cie1000SysutilStatusBoardInfoInfoGroup,
       "cie1000SysutilStatusTemperatureMonitorInfoGroup": cie1000SysutilStatusTemperatureMonitorInfoGroup,
       "cie1000SysutilStatusLedStatusSystemInfoGroup": cie1000SysutilStatusLedStatusSystemInfoGroup,
       "cie1000SysutilStatusLedStatusPortInfoGroup": cie1000SysutilStatusLedStatusPortInfoGroup,
       "cie1000SysutilControlRebootInfoGroup": cie1000SysutilControlRebootInfoGroup,
       "cie1000SysutilControlSystemLedInfoGroup": cie1000SysutilControlSystemLedInfoGroup}
)
