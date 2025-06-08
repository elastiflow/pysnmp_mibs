# SNMP MIB module (BR-ADI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/bernecker_rainer_29312/BR-ADI-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:43:06 2025
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

(bur,) = mibBuilder.importSymbols(
    "BR-TOP-MIB",
    "bur")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

brAdiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2)
)
if mibBuilder.loadTexts:
    brAdiMIB.setRevisions(
        ("2017-09-07 00:00",
         "2016-08-29 00:00",
         "2014-07-17 00:00",
         "2014-01-07 00:00",
         "2013-06-26 00:00",
         "2012-08-17 00:00",
         "2011-10-07 00:00",
         "2011-05-19 00:00",
         "2010-04-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BrAdiObjects_ObjectIdentity = ObjectIdentity
brAdiObjects = _BrAdiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1)
)
_BrPc_ObjectIdentity = ObjectIdentity
brPc = _BrPc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1)
)


class _BrPcModelNumber_Type(DisplayString):
    """Custom type brPcModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrPcModelNumber_Type.__name__ = "DisplayString"
_BrPcModelNumber_Object = MibScalar
brPcModelNumber = _BrPcModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 1),
    _BrPcModelNumber_Type()
)
brPcModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcModelNumber.setStatus("current")


class _BrPcSerialNumber_Type(DisplayString):
    """Custom type brPcSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrPcSerialNumber_Type.__name__ = "DisplayString"
_BrPcSerialNumber_Object = MibScalar
brPcSerialNumber = _BrPcSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 2),
    _BrPcSerialNumber_Type()
)
brPcSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcSerialNumber.setStatus("current")


class _BrPcHardwareRevision_Type(DisplayString):
    """Custom type brPcHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrPcHardwareRevision_Type.__name__ = "DisplayString"
_BrPcHardwareRevision_Object = MibScalar
brPcHardwareRevision = _BrPcHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 3),
    _BrPcHardwareRevision_Type()
)
brPcHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcHardwareRevision.setStatus("current")
_BrPcDeviceId_Type = Unsigned32
_BrPcDeviceId_Object = MibScalar
brPcDeviceId = _BrPcDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 4),
    _BrPcDeviceId_Type()
)
brPcDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcDeviceId.setStatus("current")
_BrPcCompatibilityId_Type = Unsigned32
_BrPcCompatibilityId_Object = MibScalar
brPcCompatibilityId = _BrPcCompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 5),
    _BrPcCompatibilityId_Type()
)
brPcCompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcCompatibilityId.setStatus("current")


class _BrPcDeviceType_Type(Integer32):
    """Custom type brPcDeviceType based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipc2001", 1),
          ("ipc5000", 2),
          ("apc680", 3),
          ("pp100pp200", 4),
          ("mp100mp200", 5),
          ("apc620", 6),
          ("ppc700", 7),
          ("pp300pp400", 8),
          ("mp40", 9),
          ("ppc300", 10),
          ("mp50", 11),
          ("apc810", 12),
          ("ppc800", 13),
          ("apc820", 14),
          ("pp500", 15),
          ("apc510", 16),
          ("apc511", 17),
          ("apc910", 18),
          ("ppc900", 19),
          ("apc2100", 20),
          ("ppc2100", 21),
          ("mp7100", 22),
          ("apc3100", 23),
          ("ppc3100", 24))
    )


_BrPcDeviceType_Type.__name__ = "Integer32"
_BrPcDeviceType_Object = MibScalar
brPcDeviceType = _BrPcDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 6),
    _BrPcDeviceType_Type()
)
brPcDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcDeviceType.setStatus("current")
_BrPcBiosVersion_Type = DisplayString
_BrPcBiosVersion_Object = MibScalar
brPcBiosVersion = _BrPcBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 7),
    _BrPcBiosVersion_Type()
)
brPcBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcBiosVersion.setStatus("current")
_BrPcBrOsVersion_Type = DisplayString
_BrPcBrOsVersion_Object = MibScalar
brPcBrOsVersion = _BrPcBrOsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 8),
    _BrPcBrOsVersion_Type()
)
brPcBrOsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcBrOsVersion.setStatus("current")


class _BrPcCmosProfile_Type(Unsigned32):
    """Custom type brPcCmosProfile based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_BrPcCmosProfile_Type.__name__ = "Unsigned32"
_BrPcCmosProfile_Object = MibScalar
brPcCmosProfile = _BrPcCmosProfile_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 9),
    _BrPcCmosProfile_Type()
)
brPcCmosProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcCmosProfile.setStatus("current")
_BrPcCpuBoardType_Type = DisplayString
_BrPcCpuBoardType_Object = MibScalar
brPcCpuBoardType = _BrPcCpuBoardType_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 10),
    _BrPcCpuBoardType_Type()
)
brPcCpuBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcCpuBoardType.setStatus("current")


class _BrPcFactorySettingsVersion_Type(DisplayString):
    """Custom type brPcFactorySettingsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_BrPcFactorySettingsVersion_Type.__name__ = "DisplayString"
_BrPcFactorySettingsVersion_Object = MibScalar
brPcFactorySettingsVersion = _BrPcFactorySettingsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 11),
    _BrPcFactorySettingsVersion_Type()
)
brPcFactorySettingsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcFactorySettingsVersion.setStatus("current")
_BrPcApLinkFpgaVersion_Type = DisplayString
_BrPcApLinkFpgaVersion_Object = MibScalar
brPcApLinkFpgaVersion = _BrPcApLinkFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 12),
    _BrPcApLinkFpgaVersion_Type()
)
brPcApLinkFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcApLinkFpgaVersion.setStatus("current")
_BrPcApLinkPresent_Type = TruthValue
_BrPcApLinkPresent_Object = MibScalar
brPcApLinkPresent = _BrPcApLinkPresent_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 13),
    _BrPcApLinkPresent_Type()
)
brPcApLinkPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcApLinkPresent.setStatus("current")
_BrPcMtcxFpgaVersion_Type = DisplayString
_BrPcMtcxFpgaVersion_Object = MibScalar
brPcMtcxFpgaVersion = _BrPcMtcxFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 14),
    _BrPcMtcxFpgaVersion_Type()
)
brPcMtcxFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcMtcxFpgaVersion.setStatus("current")
_BrPcMtcxPx32Version_Type = DisplayString
_BrPcMtcxPx32Version_Object = MibScalar
brPcMtcxPx32Version = _BrPcMtcxPx32Version_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 15),
    _BrPcMtcxPx32Version_Type()
)
brPcMtcxPx32Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcMtcxPx32Version.setStatus("current")
_BrPcUserSerialId_Type = Unsigned32
_BrPcUserSerialId_Object = MibScalar
brPcUserSerialId = _BrPcUserSerialId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 16),
    _BrPcUserSerialId_Type()
)
brPcUserSerialId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPcUserSerialId.setStatus("current")


class _BrPcPowerOnCycles_Type(Gauge32):
    """Custom type brPcPowerOnCycles based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_BrPcPowerOnCycles_Type.__name__ = "Gauge32"
_BrPcPowerOnCycles_Object = MibScalar
brPcPowerOnCycles = _BrPcPowerOnCycles_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 17),
    _BrPcPowerOnCycles_Type()
)
brPcPowerOnCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcPowerOnCycles.setStatus("current")


class _BrPcPowerOnHours_Type(Gauge32):
    """Custom type brPcPowerOnHours based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_BrPcPowerOnHours_Type.__name__ = "Gauge32"
_BrPcPowerOnHours_Object = MibScalar
brPcPowerOnHours = _BrPcPowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 18),
    _BrPcPowerOnHours_Type()
)
brPcPowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcPowerOnHours.setStatus("current")
if mibBuilder.loadTexts:
    brPcPowerOnHours.setUnits("hours")


class _BrPcFanOnHours_Type(Gauge32):
    """Custom type brPcFanOnHours based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_BrPcFanOnHours_Type.__name__ = "Gauge32"
_BrPcFanOnHours_Object = MibScalar
brPcFanOnHours = _BrPcFanOnHours_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 19),
    _BrPcFanOnHours_Type()
)
brPcFanOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcFanOnHours.setStatus("current")
if mibBuilder.loadTexts:
    brPcFanOnHours.setUnits("hours")


class _BrPcBatteryState_Type(Integer32):
    """Custom type brPcBatteryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("good", 1),
          ("bad", 2))
    )


_BrPcBatteryState_Type.__name__ = "Integer32"
_BrPcBatteryState_Object = MibScalar
brPcBatteryState = _BrPcBatteryState_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 20),
    _BrPcBatteryState_Type()
)
brPcBatteryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcBatteryState.setStatus("current")


class _BrPcBoardCenterTemperature_Type(Integer32):
    """Custom type brPcBoardCenterTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrPcBoardCenterTemperature_Type.__name__ = "Integer32"
_BrPcBoardCenterTemperature_Object = MibScalar
brPcBoardCenterTemperature = _BrPcBoardCenterTemperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 21),
    _BrPcBoardCenterTemperature_Type()
)
brPcBoardCenterTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcBoardCenterTemperature.setStatus("current")
if mibBuilder.loadTexts:
    brPcBoardCenterTemperature.setUnits("degrees Celsius")


class _BrPcBoardEth2Temperature_Type(Integer32):
    """Custom type brPcBoardEth2Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrPcBoardEth2Temperature_Type.__name__ = "Integer32"
_BrPcBoardEth2Temperature_Object = MibScalar
brPcBoardEth2Temperature = _BrPcBoardEth2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 22),
    _BrPcBoardEth2Temperature_Type()
)
brPcBoardEth2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcBoardEth2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brPcBoardEth2Temperature.setUnits("degrees Celsius")


class _BrPcBoardInTemperature_Type(Integer32):
    """Custom type brPcBoardInTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrPcBoardInTemperature_Type.__name__ = "Integer32"
_BrPcBoardInTemperature_Object = MibScalar
brPcBoardInTemperature = _BrPcBoardInTemperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 23),
    _BrPcBoardInTemperature_Type()
)
brPcBoardInTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcBoardInTemperature.setStatus("current")
if mibBuilder.loadTexts:
    brPcBoardInTemperature.setUnits("degrees Celsius")


class _BrPcBoardIoTemperature_Type(Integer32):
    """Custom type brPcBoardIoTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrPcBoardIoTemperature_Type.__name__ = "Integer32"
_BrPcBoardIoTemperature_Object = MibScalar
brPcBoardIoTemperature = _BrPcBoardIoTemperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 24),
    _BrPcBoardIoTemperature_Type()
)
brPcBoardIoTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcBoardIoTemperature.setStatus("current")
if mibBuilder.loadTexts:
    brPcBoardIoTemperature.setUnits("degrees Celsius")


class _BrPcBoardOutTemperature_Type(Integer32):
    """Custom type brPcBoardOutTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrPcBoardOutTemperature_Type.__name__ = "Integer32"
_BrPcBoardOutTemperature_Object = MibScalar
brPcBoardOutTemperature = _BrPcBoardOutTemperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 25),
    _BrPcBoardOutTemperature_Type()
)
brPcBoardOutTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcBoardOutTemperature.setStatus("current")
if mibBuilder.loadTexts:
    brPcBoardOutTemperature.setUnits("degrees Celsius")


class _BrPcBoardPowerTemperature_Type(Integer32):
    """Custom type brPcBoardPowerTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrPcBoardPowerTemperature_Type.__name__ = "Integer32"
_BrPcBoardPowerTemperature_Object = MibScalar
brPcBoardPowerTemperature = _BrPcBoardPowerTemperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 26),
    _BrPcBoardPowerTemperature_Type()
)
brPcBoardPowerTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcBoardPowerTemperature.setStatus("current")
if mibBuilder.loadTexts:
    brPcBoardPowerTemperature.setUnits("degrees Celsius")
_BrPcCaseFan1Speed_Type = Unsigned32
_BrPcCaseFan1Speed_Object = MibScalar
brPcCaseFan1Speed = _BrPcCaseFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 27),
    _BrPcCaseFan1Speed_Type()
)
brPcCaseFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcCaseFan1Speed.setStatus("current")
if mibBuilder.loadTexts:
    brPcCaseFan1Speed.setUnits("rpm")
_BrPcCaseFan2Speed_Type = Unsigned32
_BrPcCaseFan2Speed_Object = MibScalar
brPcCaseFan2Speed = _BrPcCaseFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 28),
    _BrPcCaseFan2Speed_Type()
)
brPcCaseFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcCaseFan2Speed.setStatus("current")
if mibBuilder.loadTexts:
    brPcCaseFan2Speed.setUnits("rpm")
_BrPcCaseFan3Speed_Type = Unsigned32
_BrPcCaseFan3Speed_Object = MibScalar
brPcCaseFan3Speed = _BrPcCaseFan3Speed_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 29),
    _BrPcCaseFan3Speed_Type()
)
brPcCaseFan3Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcCaseFan3Speed.setStatus("current")
if mibBuilder.loadTexts:
    brPcCaseFan3Speed.setUnits("rpm")
_BrPcCaseFan4Speed_Type = Unsigned32
_BrPcCaseFan4Speed_Object = MibScalar
brPcCaseFan4Speed = _BrPcCaseFan4Speed_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 30),
    _BrPcCaseFan4Speed_Type()
)
brPcCaseFan4Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcCaseFan4Speed.setStatus("current")
if mibBuilder.loadTexts:
    brPcCaseFan4Speed.setUnits("rpm")


class _BrPcCpuBoardTemperature_Type(Integer32):
    """Custom type brPcCpuBoardTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrPcCpuBoardTemperature_Type.__name__ = "Integer32"
_BrPcCpuBoardTemperature_Object = MibScalar
brPcCpuBoardTemperature = _BrPcCpuBoardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 31),
    _BrPcCpuBoardTemperature_Type()
)
brPcCpuBoardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcCpuBoardTemperature.setStatus("current")
if mibBuilder.loadTexts:
    brPcCpuBoardTemperature.setUnits("degrees Celsius")


class _BrPcCpuTemperature_Type(Integer32):
    """Custom type brPcCpuTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrPcCpuTemperature_Type.__name__ = "Integer32"
_BrPcCpuTemperature_Object = MibScalar
brPcCpuTemperature = _BrPcCpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 32),
    _BrPcCpuTemperature_Type()
)
brPcCpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcCpuTemperature.setStatus("current")
if mibBuilder.loadTexts:
    brPcCpuTemperature.setUnits("degrees Celsius")


class _BrPcDrive1Temperature_Type(Integer32):
    """Custom type brPcDrive1Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrPcDrive1Temperature_Type.__name__ = "Integer32"
_BrPcDrive1Temperature_Object = MibScalar
brPcDrive1Temperature = _BrPcDrive1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 33),
    _BrPcDrive1Temperature_Type()
)
brPcDrive1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcDrive1Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brPcDrive1Temperature.setUnits("degrees Celsius")


class _BrPcDrive2Temperature_Type(Integer32):
    """Custom type brPcDrive2Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrPcDrive2Temperature_Type.__name__ = "Integer32"
_BrPcDrive2Temperature_Object = MibScalar
brPcDrive2Temperature = _BrPcDrive2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 34),
    _BrPcDrive2Temperature_Type()
)
brPcDrive2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcDrive2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brPcDrive2Temperature.setUnits("degrees Celsius")


class _BrPcEth2Temperature_Type(Integer32):
    """Custom type brPcEth2Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrPcEth2Temperature_Type.__name__ = "Integer32"
_BrPcEth2Temperature_Object = MibScalar
brPcEth2Temperature = _BrPcEth2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 35),
    _BrPcEth2Temperature_Type()
)
brPcEth2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcEth2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brPcEth2Temperature.setUnits("degrees Celsius")


class _BrPcIfSlotTemperature_Type(Integer32):
    """Custom type brPcIfSlotTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrPcIfSlotTemperature_Type.__name__ = "Integer32"
_BrPcIfSlotTemperature_Object = MibScalar
brPcIfSlotTemperature = _BrPcIfSlotTemperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 36),
    _BrPcIfSlotTemperature_Type()
)
brPcIfSlotTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcIfSlotTemperature.setStatus("current")
if mibBuilder.loadTexts:
    brPcIfSlotTemperature.setUnits("degrees Celsius")


class _BrPcPowerTemperature_Type(Integer32):
    """Custom type brPcPowerTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrPcPowerTemperature_Type.__name__ = "Integer32"
_BrPcPowerTemperature_Object = MibScalar
brPcPowerTemperature = _BrPcPowerTemperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 37),
    _BrPcPowerTemperature_Type()
)
brPcPowerTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcPowerTemperature.setStatus("current")
if mibBuilder.loadTexts:
    brPcPowerTemperature.setUnits("degrees Celsius")


class _BrPcModeNode_Type(Unsigned32):
    """Custom type brPcModeNode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrPcModeNode_Type.__name__ = "Unsigned32"
_BrPcModeNode_Object = MibScalar
brPcModeNode = _BrPcModeNode_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 38),
    _BrPcModeNode_Type()
)
brPcModeNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcModeNode.setStatus("current")
_BrPcMtcxVersion_Type = DisplayString
_BrPcMtcxVersion_Object = MibScalar
brPcMtcxVersion = _BrPcMtcxVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 39),
    _BrPcMtcxVersion_Type()
)
brPcMtcxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcMtcxVersion.setStatus("current")


class _BrPcSys1Temperature_Type(Integer32):
    """Custom type brPcSys1Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrPcSys1Temperature_Type.__name__ = "Integer32"
_BrPcSys1Temperature_Object = MibScalar
brPcSys1Temperature = _BrPcSys1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 40),
    _BrPcSys1Temperature_Type()
)
brPcSys1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcSys1Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brPcSys1Temperature.setUnits("degrees Celsius")


class _BrPcSys2Temperature_Type(Integer32):
    """Custom type brPcSys2Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrPcSys2Temperature_Type.__name__ = "Integer32"
_BrPcSys2Temperature_Object = MibScalar
brPcSys2Temperature = _BrPcSys2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 41),
    _BrPcSys2Temperature_Type()
)
brPcSys2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcSys2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brPcSys2Temperature.setUnits("degrees Celsius")


class _BrPcSys3Temperature_Type(Integer32):
    """Custom type brPcSys3Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrPcSys3Temperature_Type.__name__ = "Integer32"
_BrPcSys3Temperature_Object = MibScalar
brPcSys3Temperature = _BrPcSys3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 42),
    _BrPcSys3Temperature_Type()
)
brPcSys3Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcSys3Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brPcSys3Temperature.setUnits("degrees Celsius")


class _BrPcSys4Temperature_Type(Integer32):
    """Custom type brPcSys4Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrPcSys4Temperature_Type.__name__ = "Integer32"
_BrPcSys4Temperature_Object = MibScalar
brPcSys4Temperature = _BrPcSys4Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 43),
    _BrPcSys4Temperature_Type()
)
brPcSys4Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcSys4Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brPcSys4Temperature.setUnits("degrees Celsius")


class _BrPcBiosBootMode_Type(Integer32):
    """Custom type brPcBiosBootMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("backup", 0),
          ("normal", 1))
    )


_BrPcBiosBootMode_Type.__name__ = "Integer32"
_BrPcBiosBootMode_Object = MibScalar
brPcBiosBootMode = _BrPcBiosBootMode_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 44),
    _BrPcBiosBootMode_Type()
)
brPcBiosBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcBiosBootMode.setStatus("current")


class _BrPcMtcxBootMode_Type(Integer32):
    """Custom type brPcMtcxBootMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_BrPcMtcxBootMode_Type.__name__ = "Integer32"
_BrPcMtcxBootMode_Object = MibScalar
brPcMtcxBootMode = _BrPcMtcxBootMode_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 1, 45),
    _BrPcMtcxBootMode_Type()
)
brPcMtcxBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPcMtcxBootMode.setStatus("current")
_BrUps_ObjectIdentity = ObjectIdentity
brUps = _BrUps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 2)
)
_BrUpsDetected_Type = TruthValue
_BrUpsDetected_Object = MibScalar
brUpsDetected = _BrUpsDetected_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 2, 1),
    _BrUpsDetected_Type()
)
brUpsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brUpsDetected.setStatus("current")
_BrUpsLinked_Type = TruthValue
_BrUpsLinked_Object = MibScalar
brUpsLinked = _BrUpsLinked_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 2, 2),
    _BrUpsLinked_Type()
)
brUpsLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brUpsLinked.setStatus("current")


class _BrUpsModelNumber_Type(DisplayString):
    """Custom type brUpsModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrUpsModelNumber_Type.__name__ = "DisplayString"
_BrUpsModelNumber_Object = MibScalar
brUpsModelNumber = _BrUpsModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 2, 3),
    _BrUpsModelNumber_Type()
)
brUpsModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brUpsModelNumber.setStatus("current")


class _BrUpsSerialNumber_Type(DisplayString):
    """Custom type brUpsSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrUpsSerialNumber_Type.__name__ = "DisplayString"
_BrUpsSerialNumber_Object = MibScalar
brUpsSerialNumber = _BrUpsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 2, 4),
    _BrUpsSerialNumber_Type()
)
brUpsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brUpsSerialNumber.setStatus("current")


class _BrUpsHardwareRevision_Type(DisplayString):
    """Custom type brUpsHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrUpsHardwareRevision_Type.__name__ = "DisplayString"
_BrUpsHardwareRevision_Object = MibScalar
brUpsHardwareRevision = _BrUpsHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 2, 5),
    _BrUpsHardwareRevision_Type()
)
brUpsHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brUpsHardwareRevision.setStatus("current")
_BrUpsDeviceId_Type = Unsigned32
_BrUpsDeviceId_Object = MibScalar
brUpsDeviceId = _BrUpsDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 2, 6),
    _BrUpsDeviceId_Type()
)
brUpsDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brUpsDeviceId.setStatus("current")
_BrUpsCompatibilityId_Type = Unsigned32
_BrUpsCompatibilityId_Object = MibScalar
brUpsCompatibilityId = _BrUpsCompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 2, 7),
    _BrUpsCompatibilityId_Type()
)
brUpsCompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brUpsCompatibilityId.setStatus("current")
_BrUpsFirmwareVersion_Type = DisplayString
_BrUpsFirmwareVersion_Object = MibScalar
brUpsFirmwareVersion = _BrUpsFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 2, 8),
    _BrUpsFirmwareVersion_Type()
)
brUpsFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brUpsFirmwareVersion.setStatus("current")


class _BrUpsFactorySettingsVersion_Type(DisplayString):
    """Custom type brUpsFactorySettingsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_BrUpsFactorySettingsVersion_Type.__name__ = "DisplayString"
_BrUpsFactorySettingsVersion_Object = MibScalar
brUpsFactorySettingsVersion = _BrUpsFactorySettingsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 2, 9),
    _BrUpsFactorySettingsVersion_Type()
)
brUpsFactorySettingsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brUpsFactorySettingsVersion.setStatus("current")


class _BrUpsBatterySettingsVersion_Type(DisplayString):
    """Custom type brUpsBatterySettingsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_BrUpsBatterySettingsVersion_Type.__name__ = "DisplayString"
_BrUpsBatterySettingsVersion_Object = MibScalar
brUpsBatterySettingsVersion = _BrUpsBatterySettingsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 2, 10),
    _BrUpsBatterySettingsVersion_Type()
)
brUpsBatterySettingsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brUpsBatterySettingsVersion.setStatus("current")


class _BrUpsStatus_Type(Bits):
    """Custom type brUpsStatus based on Bits"""
    namedValues = NamedValues(
        *(("powerOk", 0),
          ("batterySettingsFailure", 1),
          ("onBattery", 2),
          ("lowBatteryLevel", 3),
          ("batteryPolarityReversed", 4),
          ("batteryFailure", 5),
          ("batteryLifetimeReached", 6),
          ("shutdownActive", 7),
          ("overCurrent", 8),
          ("factorySettingsFailure", 9),
          ("userSettingsFailure", 10),
          ("reserved11", 11),
          ("reserved12", 12),
          ("reserved13", 13),
          ("reserved14", 14),
          ("batteryTemperaturExceeded", 15),
          ("reserved16", 16),
          ("reserved17", 17),
          ("reserved18", 18),
          ("reserved19", 19),
          ("reserved20", 20),
          ("reserved21", 21),
          ("reserved22", 22),
          ("reserved23", 23),
          ("reserved24", 24),
          ("reserved25", 25),
          ("reserved26", 26),
          ("reserved27", 27),
          ("reserved28", 28),
          ("reserved29", 29),
          ("reserved30", 30),
          ("reserved31", 31))
    )

_BrUpsStatus_Type.__name__ = "Bits"
_BrUpsStatus_Object = MibScalar
brUpsStatus = _BrUpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 2, 11),
    _BrUpsStatus_Type()
)
brUpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brUpsStatus.setStatus("current")
_BrUpsBatteryCurrent_Type = Integer32
_BrUpsBatteryCurrent_Object = MibScalar
brUpsBatteryCurrent = _BrUpsBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 2, 12),
    _BrUpsBatteryCurrent_Type()
)
brUpsBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brUpsBatteryCurrent.setStatus("current")
if mibBuilder.loadTexts:
    brUpsBatteryCurrent.setUnits("mA")
_BrUpsBatteryVoltage_Type = Integer32
_BrUpsBatteryVoltage_Object = MibScalar
brUpsBatteryVoltage = _BrUpsBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 2, 13),
    _BrUpsBatteryVoltage_Type()
)
brUpsBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brUpsBatteryVoltage.setStatus("current")
if mibBuilder.loadTexts:
    brUpsBatteryVoltage.setUnits("mV")


class _BrUpsBatteryTemperature_Type(Integer32):
    """Custom type brUpsBatteryTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrUpsBatteryTemperature_Type.__name__ = "Integer32"
_BrUpsBatteryTemperature_Object = MibScalar
brUpsBatteryTemperature = _BrUpsBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 2, 14),
    _BrUpsBatteryTemperature_Type()
)
brUpsBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brUpsBatteryTemperature.setStatus("current")
if mibBuilder.loadTexts:
    brUpsBatteryTemperature.setUnits("degrees Celsius")


class _BrUpsOnBatteryCycles_Type(Gauge32):
    """Custom type brUpsOnBatteryCycles based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_BrUpsOnBatteryCycles_Type.__name__ = "Gauge32"
_BrUpsOnBatteryCycles_Object = MibScalar
brUpsOnBatteryCycles = _BrUpsOnBatteryCycles_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 2, 15),
    _BrUpsOnBatteryCycles_Type()
)
brUpsOnBatteryCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brUpsOnBatteryCycles.setStatus("current")


class _BrUpsBatteryOnHours_Type(Gauge32):
    """Custom type brUpsBatteryOnHours based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_BrUpsBatteryOnHours_Type.__name__ = "Gauge32"
_BrUpsBatteryOnHours_Object = MibScalar
brUpsBatteryOnHours = _BrUpsBatteryOnHours_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 2, 16),
    _BrUpsBatteryOnHours_Type()
)
brUpsBatteryOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brUpsBatteryOnHours.setStatus("current")
if mibBuilder.loadTexts:
    brUpsBatteryOnHours.setUnits("hours")


class _BrUpsType_Type(DisplayString):
    """Custom type brUpsType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BrUpsType_Type.__name__ = "DisplayString"
_BrUpsType_Object = MibScalar
brUpsType = _BrUpsType_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 2, 17),
    _BrUpsType_Type()
)
brUpsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brUpsType.setStatus("current")
_BrPanel_ObjectIdentity = ObjectIdentity
brPanel = _BrPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3)
)


class _BrPanelCount_Type(Integer32):
    """Custom type brPanelCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_BrPanelCount_Type.__name__ = "Integer32"
_BrPanelCount_Object = MibScalar
brPanelCount = _BrPanelCount_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 1),
    _BrPanelCount_Type()
)
brPanelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelCount.setStatus("current")
_BrPanelTable_Object = MibTable
brPanelTable = _BrPanelTable_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    brPanelTable.setStatus("current")
_BrPanelEntry_Object = MibTableRow
brPanelEntry = _BrPanelEntry_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 2, 1)
)
brPanelEntry.setIndexNames(
    (0, "BR-ADI-MIB", "brPanelIndex"),
)
if mibBuilder.loadTexts:
    brPanelEntry.setStatus("current")


class _BrPanelIndex_Type(Unsigned32):
    """Custom type brPanelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BrPanelIndex_Type.__name__ = "Unsigned32"
_BrPanelIndex_Object = MibTableColumn
brPanelIndex = _BrPanelIndex_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 2, 1, 1),
    _BrPanelIndex_Type()
)
brPanelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brPanelIndex.setStatus("current")


class _BrPanelAddress_Type(Unsigned32):
    """Custom type brPanelAddress based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_BrPanelAddress_Type.__name__ = "Unsigned32"
_BrPanelAddress_Object = MibTableColumn
brPanelAddress = _BrPanelAddress_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 2, 1, 2),
    _BrPanelAddress_Type()
)
brPanelAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelAddress.setStatus("current")
_BrPanelDetected_Type = TruthValue
_BrPanelDetected_Object = MibTableColumn
brPanelDetected = _BrPanelDetected_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 2, 1, 3),
    _BrPanelDetected_Type()
)
brPanelDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelDetected.setStatus("current")
_BrPanelLinked_Type = TruthValue
_BrPanelLinked_Object = MibTableColumn
brPanelLinked = _BrPanelLinked_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 2, 1, 4),
    _BrPanelLinked_Type()
)
brPanelLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelLinked.setStatus("current")
_BrPanelLocked_Type = TruthValue
_BrPanelLocked_Object = MibTableColumn
brPanelLocked = _BrPanelLocked_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 2, 1, 5),
    _BrPanelLocked_Type()
)
brPanelLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelLocked.setStatus("current")


class _BrPanelModelNumber_Type(DisplayString):
    """Custom type brPanelModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrPanelModelNumber_Type.__name__ = "DisplayString"
_BrPanelModelNumber_Object = MibTableColumn
brPanelModelNumber = _BrPanelModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 2, 1, 6),
    _BrPanelModelNumber_Type()
)
brPanelModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelModelNumber.setStatus("current")


class _BrPanelSerialNumber_Type(DisplayString):
    """Custom type brPanelSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrPanelSerialNumber_Type.__name__ = "DisplayString"
_BrPanelSerialNumber_Object = MibTableColumn
brPanelSerialNumber = _BrPanelSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 2, 1, 7),
    _BrPanelSerialNumber_Type()
)
brPanelSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelSerialNumber.setStatus("current")


class _BrPanelHardwareRevision_Type(DisplayString):
    """Custom type brPanelHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrPanelHardwareRevision_Type.__name__ = "DisplayString"
_BrPanelHardwareRevision_Object = MibTableColumn
brPanelHardwareRevision = _BrPanelHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 2, 1, 8),
    _BrPanelHardwareRevision_Type()
)
brPanelHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelHardwareRevision.setStatus("current")
_BrPanelDeviceId_Type = Unsigned32
_BrPanelDeviceId_Object = MibTableColumn
brPanelDeviceId = _BrPanelDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 2, 1, 9),
    _BrPanelDeviceId_Type()
)
brPanelDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelDeviceId.setStatus("current")
_BrPanelCompatibilityId_Type = Unsigned32
_BrPanelCompatibilityId_Object = MibTableColumn
brPanelCompatibilityId = _BrPanelCompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 2, 1, 10),
    _BrPanelCompatibilityId_Type()
)
brPanelCompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelCompatibilityId.setStatus("current")
_BrPanelApLinkFpgaVersion_Type = DisplayString
_BrPanelApLinkFpgaVersion_Object = MibTableColumn
brPanelApLinkFpgaVersion = _BrPanelApLinkFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 2, 1, 11),
    _BrPanelApLinkFpgaVersion_Type()
)
brPanelApLinkFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelApLinkFpgaVersion.setStatus("current")


class _BrPanelBacklightOnCycles_Type(Gauge32):
    """Custom type brPanelBacklightOnCycles based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_BrPanelBacklightOnCycles_Type.__name__ = "Gauge32"
_BrPanelBacklightOnCycles_Object = MibTableColumn
brPanelBacklightOnCycles = _BrPanelBacklightOnCycles_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 2, 1, 12),
    _BrPanelBacklightOnCycles_Type()
)
brPanelBacklightOnCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelBacklightOnCycles.setStatus("current")


class _BrPanelBacklightOnHours_Type(Gauge32):
    """Custom type brPanelBacklightOnHours based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_BrPanelBacklightOnHours_Type.__name__ = "Gauge32"
_BrPanelBacklightOnHours_Object = MibTableColumn
brPanelBacklightOnHours = _BrPanelBacklightOnHours_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 2, 1, 13),
    _BrPanelBacklightOnHours_Type()
)
brPanelBacklightOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelBacklightOnHours.setStatus("current")
if mibBuilder.loadTexts:
    brPanelBacklightOnHours.setUnits("hours")


class _BrPanelTemperature_Type(Integer32):
    """Custom type brPanelTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrPanelTemperature_Type.__name__ = "Integer32"
_BrPanelTemperature_Object = MibTableColumn
brPanelTemperature = _BrPanelTemperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 2, 1, 14),
    _BrPanelTemperature_Type()
)
brPanelTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelTemperature.setStatus("current")
if mibBuilder.loadTexts:
    brPanelTemperature.setUnits("degrees Celsius")


class _BrPanelPowerOnCycles_Type(Gauge32):
    """Custom type brPanelPowerOnCycles based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_BrPanelPowerOnCycles_Type.__name__ = "Gauge32"
_BrPanelPowerOnCycles_Object = MibTableColumn
brPanelPowerOnCycles = _BrPanelPowerOnCycles_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 2, 1, 15),
    _BrPanelPowerOnCycles_Type()
)
brPanelPowerOnCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelPowerOnCycles.setStatus("current")


class _BrPanelPowerOnHours_Type(Gauge32):
    """Custom type brPanelPowerOnHours based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_BrPanelPowerOnHours_Type.__name__ = "Gauge32"
_BrPanelPowerOnHours_Object = MibTableColumn
brPanelPowerOnHours = _BrPanelPowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 2, 1, 16),
    _BrPanelPowerOnHours_Type()
)
brPanelPowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelPowerOnHours.setStatus("current")
if mibBuilder.loadTexts:
    brPanelPowerOnHours.setUnits("hours")
_BrPanelExpansionUnitTable_Object = MibTable
brPanelExpansionUnitTable = _BrPanelExpansionUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    brPanelExpansionUnitTable.setStatus("current")
_BrPanelExpansionUnitEntry_Object = MibTableRow
brPanelExpansionUnitEntry = _BrPanelExpansionUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 3, 1)
)
brPanelExpansionUnitEntry.setIndexNames(
    (0, "BR-ADI-MIB", "brPanelExpansionUnitIndex"),
)
if mibBuilder.loadTexts:
    brPanelExpansionUnitEntry.setStatus("current")


class _BrPanelExpansionUnitIndex_Type(Unsigned32):
    """Custom type brPanelExpansionUnitIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BrPanelExpansionUnitIndex_Type.__name__ = "Unsigned32"
_BrPanelExpansionUnitIndex_Object = MibTableColumn
brPanelExpansionUnitIndex = _BrPanelExpansionUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 3, 1, 1),
    _BrPanelExpansionUnitIndex_Type()
)
brPanelExpansionUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brPanelExpansionUnitIndex.setStatus("current")
_BrPanelExpansionUnitPresent_Type = TruthValue
_BrPanelExpansionUnitPresent_Object = MibTableColumn
brPanelExpansionUnitPresent = _BrPanelExpansionUnitPresent_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 3, 1, 2),
    _BrPanelExpansionUnitPresent_Type()
)
brPanelExpansionUnitPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelExpansionUnitPresent.setStatus("current")


class _BrPanelExpansionUnitModelNumber_Type(DisplayString):
    """Custom type brPanelExpansionUnitModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrPanelExpansionUnitModelNumber_Type.__name__ = "DisplayString"
_BrPanelExpansionUnitModelNumber_Object = MibTableColumn
brPanelExpansionUnitModelNumber = _BrPanelExpansionUnitModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 3, 1, 3),
    _BrPanelExpansionUnitModelNumber_Type()
)
brPanelExpansionUnitModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelExpansionUnitModelNumber.setStatus("current")


class _BrPanelExpansionUnitSerialNumber_Type(DisplayString):
    """Custom type brPanelExpansionUnitSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrPanelExpansionUnitSerialNumber_Type.__name__ = "DisplayString"
_BrPanelExpansionUnitSerialNumber_Object = MibTableColumn
brPanelExpansionUnitSerialNumber = _BrPanelExpansionUnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 3, 1, 4),
    _BrPanelExpansionUnitSerialNumber_Type()
)
brPanelExpansionUnitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelExpansionUnitSerialNumber.setStatus("current")


class _BrPanelExpansionUnitHardwareRevision_Type(DisplayString):
    """Custom type brPanelExpansionUnitHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrPanelExpansionUnitHardwareRevision_Type.__name__ = "DisplayString"
_BrPanelExpansionUnitHardwareRevision_Object = MibTableColumn
brPanelExpansionUnitHardwareRevision = _BrPanelExpansionUnitHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 3, 1, 5),
    _BrPanelExpansionUnitHardwareRevision_Type()
)
brPanelExpansionUnitHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelExpansionUnitHardwareRevision.setStatus("current")
_BrPanelExpansionUnitDeviceId_Type = Unsigned32
_BrPanelExpansionUnitDeviceId_Object = MibTableColumn
brPanelExpansionUnitDeviceId = _BrPanelExpansionUnitDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 3, 1, 6),
    _BrPanelExpansionUnitDeviceId_Type()
)
brPanelExpansionUnitDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelExpansionUnitDeviceId.setStatus("current")
_BrPanelExpansionUnitCompatibilityId_Type = Unsigned32
_BrPanelExpansionUnitCompatibilityId_Object = MibTableColumn
brPanelExpansionUnitCompatibilityId = _BrPanelExpansionUnitCompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 3, 1, 7),
    _BrPanelExpansionUnitCompatibilityId_Type()
)
brPanelExpansionUnitCompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelExpansionUnitCompatibilityId.setStatus("current")


class _BrPanelExpansionUnitFactorySettingsVersion_Type(DisplayString):
    """Custom type brPanelExpansionUnitFactorySettingsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_BrPanelExpansionUnitFactorySettingsVersion_Type.__name__ = "DisplayString"
_BrPanelExpansionUnitFactorySettingsVersion_Object = MibTableColumn
brPanelExpansionUnitFactorySettingsVersion = _BrPanelExpansionUnitFactorySettingsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 3, 1, 8),
    _BrPanelExpansionUnitFactorySettingsVersion_Type()
)
brPanelExpansionUnitFactorySettingsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelExpansionUnitFactorySettingsVersion.setStatus("current")


class _BrPanelExpansionUnitPowerOnCycles_Type(Gauge32):
    """Custom type brPanelExpansionUnitPowerOnCycles based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_BrPanelExpansionUnitPowerOnCycles_Type.__name__ = "Gauge32"
_BrPanelExpansionUnitPowerOnCycles_Object = MibTableColumn
brPanelExpansionUnitPowerOnCycles = _BrPanelExpansionUnitPowerOnCycles_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 3, 1, 9),
    _BrPanelExpansionUnitPowerOnCycles_Type()
)
brPanelExpansionUnitPowerOnCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelExpansionUnitPowerOnCycles.setStatus("current")


class _BrPanelExpansionUnitPowerOnHours_Type(Gauge32):
    """Custom type brPanelExpansionUnitPowerOnHours based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_BrPanelExpansionUnitPowerOnHours_Type.__name__ = "Gauge32"
_BrPanelExpansionUnitPowerOnHours_Object = MibTableColumn
brPanelExpansionUnitPowerOnHours = _BrPanelExpansionUnitPowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 3, 1, 10),
    _BrPanelExpansionUnitPowerOnHours_Type()
)
brPanelExpansionUnitPowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelExpansionUnitPowerOnHours.setStatus("current")
if mibBuilder.loadTexts:
    brPanelExpansionUnitPowerOnHours.setUnits("hours")
_BrPanelLinkTable_Object = MibTable
brPanelLinkTable = _BrPanelLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    brPanelLinkTable.setStatus("current")
_BrPanelLinkEntry_Object = MibTableRow
brPanelLinkEntry = _BrPanelLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 4, 1)
)
brPanelLinkEntry.setIndexNames(
    (0, "BR-ADI-MIB", "brPanelLinkIndex"),
)
if mibBuilder.loadTexts:
    brPanelLinkEntry.setStatus("current")


class _BrPanelLinkIndex_Type(Unsigned32):
    """Custom type brPanelLinkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BrPanelLinkIndex_Type.__name__ = "Unsigned32"
_BrPanelLinkIndex_Object = MibTableColumn
brPanelLinkIndex = _BrPanelLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 4, 1, 1),
    _BrPanelLinkIndex_Type()
)
brPanelLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brPanelLinkIndex.setStatus("current")
_BrPanelLinkPresent_Type = TruthValue
_BrPanelLinkPresent_Object = MibTableColumn
brPanelLinkPresent = _BrPanelLinkPresent_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 4, 1, 2),
    _BrPanelLinkPresent_Type()
)
brPanelLinkPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelLinkPresent.setStatus("current")
_BrPanelLinkType_Type = DisplayString
_BrPanelLinkType_Object = MibTableColumn
brPanelLinkType = _BrPanelLinkType_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 4, 1, 3),
    _BrPanelLinkType_Type()
)
brPanelLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelLinkType.setStatus("current")


class _BrPanelLinkModelNumber_Type(DisplayString):
    """Custom type brPanelLinkModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrPanelLinkModelNumber_Type.__name__ = "DisplayString"
_BrPanelLinkModelNumber_Object = MibTableColumn
brPanelLinkModelNumber = _BrPanelLinkModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 4, 1, 4),
    _BrPanelLinkModelNumber_Type()
)
brPanelLinkModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelLinkModelNumber.setStatus("current")


class _BrPanelLinkSerialNumber_Type(DisplayString):
    """Custom type brPanelLinkSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrPanelLinkSerialNumber_Type.__name__ = "DisplayString"
_BrPanelLinkSerialNumber_Object = MibTableColumn
brPanelLinkSerialNumber = _BrPanelLinkSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 4, 1, 5),
    _BrPanelLinkSerialNumber_Type()
)
brPanelLinkSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelLinkSerialNumber.setStatus("current")


class _BrPanelLinkHardwareRevision_Type(DisplayString):
    """Custom type brPanelLinkHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrPanelLinkHardwareRevision_Type.__name__ = "DisplayString"
_BrPanelLinkHardwareRevision_Object = MibTableColumn
brPanelLinkHardwareRevision = _BrPanelLinkHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 4, 1, 6),
    _BrPanelLinkHardwareRevision_Type()
)
brPanelLinkHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelLinkHardwareRevision.setStatus("current")
_BrPanelLinkDeviceId_Type = Unsigned32
_BrPanelLinkDeviceId_Object = MibTableColumn
brPanelLinkDeviceId = _BrPanelLinkDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 4, 1, 7),
    _BrPanelLinkDeviceId_Type()
)
brPanelLinkDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelLinkDeviceId.setStatus("current")
_BrPanelLinkCompatibilityId_Type = Unsigned32
_BrPanelLinkCompatibilityId_Object = MibTableColumn
brPanelLinkCompatibilityId = _BrPanelLinkCompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 4, 1, 8),
    _BrPanelLinkCompatibilityId_Type()
)
brPanelLinkCompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelLinkCompatibilityId.setStatus("current")


class _BrPanelLinkFactorySettingsVersion_Type(DisplayString):
    """Custom type brPanelLinkFactorySettingsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_BrPanelLinkFactorySettingsVersion_Type.__name__ = "DisplayString"
_BrPanelLinkFactorySettingsVersion_Object = MibTableColumn
brPanelLinkFactorySettingsVersion = _BrPanelLinkFactorySettingsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 4, 1, 9),
    _BrPanelLinkFactorySettingsVersion_Type()
)
brPanelLinkFactorySettingsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelLinkFactorySettingsVersion.setStatus("current")
_BrPanelLinkFpgaVersion_Type = DisplayString
_BrPanelLinkFpgaVersion_Object = MibTableColumn
brPanelLinkFpgaVersion = _BrPanelLinkFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 4, 1, 10),
    _BrPanelLinkFpgaVersion_Type()
)
brPanelLinkFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelLinkFpgaVersion.setStatus("current")
_BrPanelLinkHdbtVersion_Type = DisplayString
_BrPanelLinkHdbtVersion_Object = MibTableColumn
brPanelLinkHdbtVersion = _BrPanelLinkHdbtVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 4, 1, 11),
    _BrPanelLinkHdbtVersion_Type()
)
brPanelLinkHdbtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelLinkHdbtVersion.setStatus("current")
_BrPanelConverterTable_Object = MibTable
brPanelConverterTable = _BrPanelConverterTable_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 5)
)
if mibBuilder.loadTexts:
    brPanelConverterTable.setStatus("current")
_BrPanelConverterEntry_Object = MibTableRow
brPanelConverterEntry = _BrPanelConverterEntry_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 5, 1)
)
brPanelConverterEntry.setIndexNames(
    (0, "BR-ADI-MIB", "brPanelConverterIndex"),
)
if mibBuilder.loadTexts:
    brPanelConverterEntry.setStatus("current")


class _BrPanelConverterIndex_Type(Unsigned32):
    """Custom type brPanelConverterIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BrPanelConverterIndex_Type.__name__ = "Unsigned32"
_BrPanelConverterIndex_Object = MibTableColumn
brPanelConverterIndex = _BrPanelConverterIndex_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 5, 1, 1),
    _BrPanelConverterIndex_Type()
)
brPanelConverterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brPanelConverterIndex.setStatus("current")
_BrPanelConverterPresent_Type = TruthValue
_BrPanelConverterPresent_Object = MibTableColumn
brPanelConverterPresent = _BrPanelConverterPresent_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 5, 1, 2),
    _BrPanelConverterPresent_Type()
)
brPanelConverterPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelConverterPresent.setStatus("current")


class _BrPanelConverterModelNumber_Type(DisplayString):
    """Custom type brPanelConverterModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrPanelConverterModelNumber_Type.__name__ = "DisplayString"
_BrPanelConverterModelNumber_Object = MibTableColumn
brPanelConverterModelNumber = _BrPanelConverterModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 5, 1, 3),
    _BrPanelConverterModelNumber_Type()
)
brPanelConverterModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelConverterModelNumber.setStatus("current")


class _BrPanelConverterSerialNumber_Type(DisplayString):
    """Custom type brPanelConverterSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrPanelConverterSerialNumber_Type.__name__ = "DisplayString"
_BrPanelConverterSerialNumber_Object = MibTableColumn
brPanelConverterSerialNumber = _BrPanelConverterSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 5, 1, 4),
    _BrPanelConverterSerialNumber_Type()
)
brPanelConverterSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelConverterSerialNumber.setStatus("current")


class _BrPanelConverterHardwareRevision_Type(DisplayString):
    """Custom type brPanelConverterHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrPanelConverterHardwareRevision_Type.__name__ = "DisplayString"
_BrPanelConverterHardwareRevision_Object = MibTableColumn
brPanelConverterHardwareRevision = _BrPanelConverterHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 5, 1, 5),
    _BrPanelConverterHardwareRevision_Type()
)
brPanelConverterHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelConverterHardwareRevision.setStatus("current")
_BrPanelConverterDeviceId_Type = Unsigned32
_BrPanelConverterDeviceId_Object = MibTableColumn
brPanelConverterDeviceId = _BrPanelConverterDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 5, 1, 6),
    _BrPanelConverterDeviceId_Type()
)
brPanelConverterDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelConverterDeviceId.setStatus("current")
_BrPanelConverterCompatibilityId_Type = Unsigned32
_BrPanelConverterCompatibilityId_Object = MibTableColumn
brPanelConverterCompatibilityId = _BrPanelConverterCompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 5, 1, 7),
    _BrPanelConverterCompatibilityId_Type()
)
brPanelConverterCompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelConverterCompatibilityId.setStatus("current")
_BrPanelConverterFpgaVersion_Type = DisplayString
_BrPanelConverterFpgaVersion_Object = MibTableColumn
brPanelConverterFpgaVersion = _BrPanelConverterFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 5, 1, 8),
    _BrPanelConverterFpgaVersion_Type()
)
brPanelConverterFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelConverterFpgaVersion.setStatus("current")


class _BrPanelConverterFpgaBootMode_Type(Integer32):
    """Custom type brPanelConverterFpgaBootMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_BrPanelConverterFpgaBootMode_Type.__name__ = "Integer32"
_BrPanelConverterFpgaBootMode_Object = MibTableColumn
brPanelConverterFpgaBootMode = _BrPanelConverterFpgaBootMode_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 3, 5, 1, 9),
    _BrPanelConverterFpgaBootMode_Type()
)
brPanelConverterFpgaBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelConverterFpgaBootMode.setStatus("current")
_BrCpu_ObjectIdentity = ObjectIdentity
brCpu = _BrCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 4)
)


class _BrCpuModelNumber_Type(DisplayString):
    """Custom type brCpuModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrCpuModelNumber_Type.__name__ = "DisplayString"
_BrCpuModelNumber_Object = MibScalar
brCpuModelNumber = _BrCpuModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 4, 1),
    _BrCpuModelNumber_Type()
)
brCpuModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCpuModelNumber.setStatus("current")


class _BrCpuSerialNumber_Type(DisplayString):
    """Custom type brCpuSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrCpuSerialNumber_Type.__name__ = "DisplayString"
_BrCpuSerialNumber_Object = MibScalar
brCpuSerialNumber = _BrCpuSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 4, 2),
    _BrCpuSerialNumber_Type()
)
brCpuSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCpuSerialNumber.setStatus("current")


class _BrCpuHardwareRevision_Type(DisplayString):
    """Custom type brCpuHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrCpuHardwareRevision_Type.__name__ = "DisplayString"
_BrCpuHardwareRevision_Object = MibScalar
brCpuHardwareRevision = _BrCpuHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 4, 3),
    _BrCpuHardwareRevision_Type()
)
brCpuHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCpuHardwareRevision.setStatus("current")
_BrCpuDeviceId_Type = Unsigned32
_BrCpuDeviceId_Object = MibScalar
brCpuDeviceId = _BrCpuDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 4, 4),
    _BrCpuDeviceId_Type()
)
brCpuDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCpuDeviceId.setStatus("current")
_BrCpuCompatibilityId_Type = Unsigned32
_BrCpuCompatibilityId_Object = MibScalar
brCpuCompatibilityId = _BrCpuCompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 4, 5),
    _BrCpuCompatibilityId_Type()
)
brCpuCompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCpuCompatibilityId.setStatus("current")


class _BrCpuFactorySettingsVersion_Type(DisplayString):
    """Custom type brCpuFactorySettingsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_BrCpuFactorySettingsVersion_Type.__name__ = "DisplayString"
_BrCpuFactorySettingsVersion_Object = MibScalar
brCpuFactorySettingsVersion = _BrCpuFactorySettingsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 4, 6),
    _BrCpuFactorySettingsVersion_Type()
)
brCpuFactorySettingsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCpuFactorySettingsVersion.setStatus("current")


class _BrCpuPowerOnCycles_Type(Gauge32):
    """Custom type brCpuPowerOnCycles based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrCpuPowerOnCycles_Type.__name__ = "Gauge32"
_BrCpuPowerOnCycles_Object = MibScalar
brCpuPowerOnCycles = _BrCpuPowerOnCycles_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 4, 7),
    _BrCpuPowerOnCycles_Type()
)
brCpuPowerOnCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCpuPowerOnCycles.setStatus("current")


class _BrCpuPowerOnHours_Type(Gauge32):
    """Custom type brCpuPowerOnHours based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrCpuPowerOnHours_Type.__name__ = "Gauge32"
_BrCpuPowerOnHours_Object = MibScalar
brCpuPowerOnHours = _BrCpuPowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 4, 8),
    _BrCpuPowerOnHours_Type()
)
brCpuPowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCpuPowerOnHours.setStatus("current")
if mibBuilder.loadTexts:
    brCpuPowerOnHours.setUnits("hours")


class _BrCpu1Temperature_Type(Integer32):
    """Custom type brCpu1Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrCpu1Temperature_Type.__name__ = "Integer32"
_BrCpu1Temperature_Object = MibScalar
brCpu1Temperature = _BrCpu1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 4, 9),
    _BrCpu1Temperature_Type()
)
brCpu1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCpu1Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brCpu1Temperature.setUnits("degrees Celsius")


class _BrCpu2Temperature_Type(Integer32):
    """Custom type brCpu2Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrCpu2Temperature_Type.__name__ = "Integer32"
_BrCpu2Temperature_Object = MibScalar
brCpu2Temperature = _BrCpu2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 4, 10),
    _BrCpu2Temperature_Type()
)
brCpu2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCpu2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brCpu2Temperature.setUnits("degrees Celsius")


class _BrCpu3Temperature_Type(Integer32):
    """Custom type brCpu3Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrCpu3Temperature_Type.__name__ = "Integer32"
_BrCpu3Temperature_Object = MibScalar
brCpu3Temperature = _BrCpu3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 4, 11),
    _BrCpu3Temperature_Type()
)
brCpu3Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCpu3Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brCpu3Temperature.setUnits("degrees Celsius")


class _BrCpu4Temperature_Type(Integer32):
    """Custom type brCpu4Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrCpu4Temperature_Type.__name__ = "Integer32"
_BrCpu4Temperature_Object = MibScalar
brCpu4Temperature = _BrCpu4Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 4, 12),
    _BrCpu4Temperature_Type()
)
brCpu4Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCpu4Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brCpu4Temperature.setUnits("degrees Celsius")
_BrCpuPower_Type = Integer32
_BrCpuPower_Object = MibScalar
brCpuPower = _BrCpuPower_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 4, 13),
    _BrCpuPower_Type()
)
brCpuPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCpuPower.setStatus("current")
if mibBuilder.loadTexts:
    brCpuPower.setUnits("Milliwatt")
_BrMem_ObjectIdentity = ObjectIdentity
brMem = _BrMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 5)
)


class _BrMemModelNumber_Type(DisplayString):
    """Custom type brMemModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrMemModelNumber_Type.__name__ = "DisplayString"
_BrMemModelNumber_Object = MibScalar
brMemModelNumber = _BrMemModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 5, 1),
    _BrMemModelNumber_Type()
)
brMemModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMemModelNumber.setStatus("current")


class _BrMemSerialNumber_Type(DisplayString):
    """Custom type brMemSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrMemSerialNumber_Type.__name__ = "DisplayString"
_BrMemSerialNumber_Object = MibScalar
brMemSerialNumber = _BrMemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 5, 2),
    _BrMemSerialNumber_Type()
)
brMemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMemSerialNumber.setStatus("current")


class _BrMemHardwareRevision_Type(DisplayString):
    """Custom type brMemHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrMemHardwareRevision_Type.__name__ = "DisplayString"
_BrMemHardwareRevision_Object = MibScalar
brMemHardwareRevision = _BrMemHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 5, 3),
    _BrMemHardwareRevision_Type()
)
brMemHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMemHardwareRevision.setStatus("current")
_BrMemDeviceId_Type = Unsigned32
_BrMemDeviceId_Object = MibScalar
brMemDeviceId = _BrMemDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 5, 4),
    _BrMemDeviceId_Type()
)
brMemDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMemDeviceId.setStatus("current")
_BrMemCompatibilityId_Type = Unsigned32
_BrMemCompatibilityId_Object = MibScalar
brMemCompatibilityId = _BrMemCompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 5, 5),
    _BrMemCompatibilityId_Type()
)
brMemCompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMemCompatibilityId.setStatus("current")


class _BrMemFactorySettingsVersion_Type(DisplayString):
    """Custom type brMemFactorySettingsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_BrMemFactorySettingsVersion_Type.__name__ = "DisplayString"
_BrMemFactorySettingsVersion_Object = MibScalar
brMemFactorySettingsVersion = _BrMemFactorySettingsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 5, 6),
    _BrMemFactorySettingsVersion_Type()
)
brMemFactorySettingsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMemFactorySettingsVersion.setStatus("current")
_BrMemPresent_Type = TruthValue
_BrMemPresent_Object = MibScalar
brMemPresent = _BrMemPresent_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 5, 7),
    _BrMemPresent_Type()
)
brMemPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMemPresent.setStatus("current")
_BrIf_ObjectIdentity = ObjectIdentity
brIf = _BrIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 6)
)
_BrIfPresent_Type = TruthValue
_BrIfPresent_Object = MibScalar
brIfPresent = _BrIfPresent_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 6, 1),
    _BrIfPresent_Type()
)
brIfPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIfPresent.setStatus("current")


class _BrIfModelNumber_Type(DisplayString):
    """Custom type brIfModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrIfModelNumber_Type.__name__ = "DisplayString"
_BrIfModelNumber_Object = MibScalar
brIfModelNumber = _BrIfModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 6, 2),
    _BrIfModelNumber_Type()
)
brIfModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIfModelNumber.setStatus("current")


class _BrIfSerialNumber_Type(DisplayString):
    """Custom type brIfSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrIfSerialNumber_Type.__name__ = "DisplayString"
_BrIfSerialNumber_Object = MibScalar
brIfSerialNumber = _BrIfSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 6, 3),
    _BrIfSerialNumber_Type()
)
brIfSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIfSerialNumber.setStatus("current")


class _BrIfHardwareRevision_Type(DisplayString):
    """Custom type brIfHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrIfHardwareRevision_Type.__name__ = "DisplayString"
_BrIfHardwareRevision_Object = MibScalar
brIfHardwareRevision = _BrIfHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 6, 4),
    _BrIfHardwareRevision_Type()
)
brIfHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIfHardwareRevision.setStatus("current")
_BrIfDeviceId_Type = Unsigned32
_BrIfDeviceId_Object = MibScalar
brIfDeviceId = _BrIfDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 6, 5),
    _BrIfDeviceId_Type()
)
brIfDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIfDeviceId.setStatus("current")
_BrIfCompatibilityId_Type = Unsigned32
_BrIfCompatibilityId_Object = MibScalar
brIfCompatibilityId = _BrIfCompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 6, 6),
    _BrIfCompatibilityId_Type()
)
brIfCompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIfCompatibilityId.setStatus("current")


class _BrIfFactorySettingsVersion_Type(DisplayString):
    """Custom type brIfFactorySettingsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_BrIfFactorySettingsVersion_Type.__name__ = "DisplayString"
_BrIfFactorySettingsVersion_Object = MibScalar
brIfFactorySettingsVersion = _BrIfFactorySettingsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 6, 7),
    _BrIfFactorySettingsVersion_Type()
)
brIfFactorySettingsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIfFactorySettingsVersion.setStatus("current")


class _BrIfPowerOnCycles_Type(Gauge32):
    """Custom type brIfPowerOnCycles based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_BrIfPowerOnCycles_Type.__name__ = "Gauge32"
_BrIfPowerOnCycles_Object = MibScalar
brIfPowerOnCycles = _BrIfPowerOnCycles_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 6, 8),
    _BrIfPowerOnCycles_Type()
)
brIfPowerOnCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIfPowerOnCycles.setStatus("current")


class _BrIfPowerOnHours_Type(Gauge32):
    """Custom type brIfPowerOnHours based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_BrIfPowerOnHours_Type.__name__ = "Gauge32"
_BrIfPowerOnHours_Object = MibScalar
brIfPowerOnHours = _BrIfPowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 6, 9),
    _BrIfPowerOnHours_Type()
)
brIfPowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIfPowerOnHours.setStatus("current")
if mibBuilder.loadTexts:
    brIfPowerOnHours.setUnits("hours")


class _BrIf1Temperature_Type(Integer32):
    """Custom type brIf1Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrIf1Temperature_Type.__name__ = "Integer32"
_BrIf1Temperature_Object = MibScalar
brIf1Temperature = _BrIf1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 6, 10),
    _BrIf1Temperature_Type()
)
brIf1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf1Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brIf1Temperature.setUnits("degrees Celsius")


class _BrIf2Temperature_Type(Integer32):
    """Custom type brIf2Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrIf2Temperature_Type.__name__ = "Integer32"
_BrIf2Temperature_Object = MibScalar
brIf2Temperature = _BrIf2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 6, 11),
    _BrIf2Temperature_Type()
)
brIf2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brIf2Temperature.setUnits("degrees Celsius")


class _BrIf3Temperature_Type(Integer32):
    """Custom type brIf3Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrIf3Temperature_Type.__name__ = "Integer32"
_BrIf3Temperature_Object = MibScalar
brIf3Temperature = _BrIf3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 6, 12),
    _BrIf3Temperature_Type()
)
brIf3Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf3Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brIf3Temperature.setUnits("degrees Celsius")


class _BrIf4Temperature_Type(Integer32):
    """Custom type brIf4Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrIf4Temperature_Type.__name__ = "Integer32"
_BrIf4Temperature_Object = MibScalar
brIf4Temperature = _BrIf4Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 6, 13),
    _BrIf4Temperature_Type()
)
brIf4Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf4Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brIf4Temperature.setUnits("degrees Celsius")
_BrIo_ObjectIdentity = ObjectIdentity
brIo = _BrIo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 7)
)
_BrIoPresent_Type = TruthValue
_BrIoPresent_Object = MibScalar
brIoPresent = _BrIoPresent_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 7, 1),
    _BrIoPresent_Type()
)
brIoPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIoPresent.setStatus("current")


class _BrIoModelNumber_Type(DisplayString):
    """Custom type brIoModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrIoModelNumber_Type.__name__ = "DisplayString"
_BrIoModelNumber_Object = MibScalar
brIoModelNumber = _BrIoModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 7, 2),
    _BrIoModelNumber_Type()
)
brIoModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIoModelNumber.setStatus("current")


class _BrIoSerialNumber_Type(DisplayString):
    """Custom type brIoSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrIoSerialNumber_Type.__name__ = "DisplayString"
_BrIoSerialNumber_Object = MibScalar
brIoSerialNumber = _BrIoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 7, 3),
    _BrIoSerialNumber_Type()
)
brIoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIoSerialNumber.setStatus("current")


class _BrIoHardwareRevision_Type(DisplayString):
    """Custom type brIoHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrIoHardwareRevision_Type.__name__ = "DisplayString"
_BrIoHardwareRevision_Object = MibScalar
brIoHardwareRevision = _BrIoHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 7, 4),
    _BrIoHardwareRevision_Type()
)
brIoHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIoHardwareRevision.setStatus("current")
_BrIoDeviceId_Type = Unsigned32
_BrIoDeviceId_Object = MibScalar
brIoDeviceId = _BrIoDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 7, 5),
    _BrIoDeviceId_Type()
)
brIoDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIoDeviceId.setStatus("current")
_BrIoCompatibilityId_Type = Unsigned32
_BrIoCompatibilityId_Object = MibScalar
brIoCompatibilityId = _BrIoCompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 7, 6),
    _BrIoCompatibilityId_Type()
)
brIoCompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIoCompatibilityId.setStatus("current")


class _BrIoFactorySettingsVersion_Type(DisplayString):
    """Custom type brIoFactorySettingsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_BrIoFactorySettingsVersion_Type.__name__ = "DisplayString"
_BrIoFactorySettingsVersion_Object = MibScalar
brIoFactorySettingsVersion = _BrIoFactorySettingsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 7, 7),
    _BrIoFactorySettingsVersion_Type()
)
brIoFactorySettingsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIoFactorySettingsVersion.setStatus("current")


class _BrIoPowerOnCycles_Type(Gauge32):
    """Custom type brIoPowerOnCycles based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrIoPowerOnCycles_Type.__name__ = "Gauge32"
_BrIoPowerOnCycles_Object = MibScalar
brIoPowerOnCycles = _BrIoPowerOnCycles_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 7, 8),
    _BrIoPowerOnCycles_Type()
)
brIoPowerOnCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIoPowerOnCycles.setStatus("current")


class _BrIoPowerOnHours_Type(Gauge32):
    """Custom type brIoPowerOnHours based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrIoPowerOnHours_Type.__name__ = "Gauge32"
_BrIoPowerOnHours_Object = MibScalar
brIoPowerOnHours = _BrIoPowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 7, 9),
    _BrIoPowerOnHours_Type()
)
brIoPowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIoPowerOnHours.setStatus("current")
if mibBuilder.loadTexts:
    brIoPowerOnHours.setUnits("hours")


class _BrIo1Temperature_Type(Integer32):
    """Custom type brIo1Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrIo1Temperature_Type.__name__ = "Integer32"
_BrIo1Temperature_Object = MibScalar
brIo1Temperature = _BrIo1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 7, 10),
    _BrIo1Temperature_Type()
)
brIo1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIo1Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brIo1Temperature.setUnits("degrees Celsius")


class _BrIo2Temperature_Type(Integer32):
    """Custom type brIo2Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrIo2Temperature_Type.__name__ = "Integer32"
_BrIo2Temperature_Object = MibScalar
brIo2Temperature = _BrIo2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 7, 11),
    _BrIo2Temperature_Type()
)
brIo2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIo2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brIo2Temperature.setUnits("degrees Celsius")


class _BrIo3Temperature_Type(Integer32):
    """Custom type brIo3Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrIo3Temperature_Type.__name__ = "Integer32"
_BrIo3Temperature_Object = MibScalar
brIo3Temperature = _BrIo3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 7, 12),
    _BrIo3Temperature_Type()
)
brIo3Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIo3Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brIo3Temperature.setUnits("degrees Celsius")


class _BrIo4Temperature_Type(Integer32):
    """Custom type brIo4Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrIo4Temperature_Type.__name__ = "Integer32"
_BrIo4Temperature_Object = MibScalar
brIo4Temperature = _BrIo4Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 7, 13),
    _BrIo4Temperature_Type()
)
brIo4Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIo4Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brIo4Temperature.setUnits("degrees Celsius")
_BrIoFpgaVersion_Type = DisplayString
_BrIoFpgaVersion_Object = MibScalar
brIoFpgaVersion = _BrIoFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 7, 14),
    _BrIoFpgaVersion_Type()
)
brIoFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIoFpgaVersion.setStatus("current")


class _BrIoFpgaBootMode_Type(Integer32):
    """Custom type brIoFpgaBootMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_BrIoFpgaBootMode_Type.__name__ = "Integer32"
_BrIoFpgaBootMode_Object = MibScalar
brIoFpgaBootMode = _BrIoFpgaBootMode_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 7, 15),
    _BrIoFpgaBootMode_Type()
)
brIoFpgaBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIoFpgaBootMode.setStatus("current")
_BrBus_ObjectIdentity = ObjectIdentity
brBus = _BrBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 8)
)


class _BrBusModelNumber_Type(DisplayString):
    """Custom type brBusModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrBusModelNumber_Type.__name__ = "DisplayString"
_BrBusModelNumber_Object = MibScalar
brBusModelNumber = _BrBusModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 8, 1),
    _BrBusModelNumber_Type()
)
brBusModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brBusModelNumber.setStatus("current")


class _BrBusSerialNumber_Type(DisplayString):
    """Custom type brBusSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrBusSerialNumber_Type.__name__ = "DisplayString"
_BrBusSerialNumber_Object = MibScalar
brBusSerialNumber = _BrBusSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 8, 2),
    _BrBusSerialNumber_Type()
)
brBusSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brBusSerialNumber.setStatus("current")


class _BrBusHardwareRevision_Type(DisplayString):
    """Custom type brBusHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrBusHardwareRevision_Type.__name__ = "DisplayString"
_BrBusHardwareRevision_Object = MibScalar
brBusHardwareRevision = _BrBusHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 8, 3),
    _BrBusHardwareRevision_Type()
)
brBusHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brBusHardwareRevision.setStatus("current")
_BrBusDeviceId_Type = Unsigned32
_BrBusDeviceId_Object = MibScalar
brBusDeviceId = _BrBusDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 8, 4),
    _BrBusDeviceId_Type()
)
brBusDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brBusDeviceId.setStatus("current")
_BrBusCompatibilityId_Type = Unsigned32
_BrBusCompatibilityId_Object = MibScalar
brBusCompatibilityId = _BrBusCompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 8, 5),
    _BrBusCompatibilityId_Type()
)
brBusCompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brBusCompatibilityId.setStatus("current")


class _BrBusFactorySettingsVersion_Type(DisplayString):
    """Custom type brBusFactorySettingsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_BrBusFactorySettingsVersion_Type.__name__ = "DisplayString"
_BrBusFactorySettingsVersion_Object = MibScalar
brBusFactorySettingsVersion = _BrBusFactorySettingsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 8, 6),
    _BrBusFactorySettingsVersion_Type()
)
brBusFactorySettingsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brBusFactorySettingsVersion.setStatus("current")


class _BrBusPowerOnCycles_Type(Gauge32):
    """Custom type brBusPowerOnCycles based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_BrBusPowerOnCycles_Type.__name__ = "Gauge32"
_BrBusPowerOnCycles_Object = MibScalar
brBusPowerOnCycles = _BrBusPowerOnCycles_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 8, 7),
    _BrBusPowerOnCycles_Type()
)
brBusPowerOnCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brBusPowerOnCycles.setStatus("current")


class _BrBusPowerOnHours_Type(Gauge32):
    """Custom type brBusPowerOnHours based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_BrBusPowerOnHours_Type.__name__ = "Gauge32"
_BrBusPowerOnHours_Object = MibScalar
brBusPowerOnHours = _BrBusPowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 8, 8),
    _BrBusPowerOnHours_Type()
)
brBusPowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brBusPowerOnHours.setStatus("current")
if mibBuilder.loadTexts:
    brBusPowerOnHours.setUnits("hours")
_BrBusPresent_Type = TruthValue
_BrBusPresent_Object = MibScalar
brBusPresent = _BrBusPresent_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 8, 9),
    _BrBusPresent_Type()
)
brBusPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brBusPresent.setStatus("current")
_BrLink_ObjectIdentity = ObjectIdentity
brLink = _BrLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 9)
)
_BrLinkPresent_Type = TruthValue
_BrLinkPresent_Object = MibScalar
brLinkPresent = _BrLinkPresent_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 9, 1),
    _BrLinkPresent_Type()
)
brLinkPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLinkPresent.setStatus("current")


class _BrLinkModelNumber_Type(DisplayString):
    """Custom type brLinkModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrLinkModelNumber_Type.__name__ = "DisplayString"
_BrLinkModelNumber_Object = MibScalar
brLinkModelNumber = _BrLinkModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 9, 2),
    _BrLinkModelNumber_Type()
)
brLinkModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLinkModelNumber.setStatus("current")


class _BrLinkSerialNumber_Type(DisplayString):
    """Custom type brLinkSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrLinkSerialNumber_Type.__name__ = "DisplayString"
_BrLinkSerialNumber_Object = MibScalar
brLinkSerialNumber = _BrLinkSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 9, 3),
    _BrLinkSerialNumber_Type()
)
brLinkSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLinkSerialNumber.setStatus("current")


class _BrLinkHardwareRevision_Type(DisplayString):
    """Custom type brLinkHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrLinkHardwareRevision_Type.__name__ = "DisplayString"
_BrLinkHardwareRevision_Object = MibScalar
brLinkHardwareRevision = _BrLinkHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 9, 4),
    _BrLinkHardwareRevision_Type()
)
brLinkHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLinkHardwareRevision.setStatus("current")
_BrLinkDeviceId_Type = Unsigned32
_BrLinkDeviceId_Object = MibScalar
brLinkDeviceId = _BrLinkDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 9, 5),
    _BrLinkDeviceId_Type()
)
brLinkDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLinkDeviceId.setStatus("current")
_BrLinkCompatibilityId_Type = Unsigned32
_BrLinkCompatibilityId_Object = MibScalar
brLinkCompatibilityId = _BrLinkCompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 9, 6),
    _BrLinkCompatibilityId_Type()
)
brLinkCompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLinkCompatibilityId.setStatus("current")


class _BrLinkFactorySettingsVersion_Type(DisplayString):
    """Custom type brLinkFactorySettingsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_BrLinkFactorySettingsVersion_Type.__name__ = "DisplayString"
_BrLinkFactorySettingsVersion_Object = MibScalar
brLinkFactorySettingsVersion = _BrLinkFactorySettingsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 9, 7),
    _BrLinkFactorySettingsVersion_Type()
)
brLinkFactorySettingsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLinkFactorySettingsVersion.setStatus("current")


class _BrLinkPowerOnCycles_Type(Gauge32):
    """Custom type brLinkPowerOnCycles based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_BrLinkPowerOnCycles_Type.__name__ = "Gauge32"
_BrLinkPowerOnCycles_Object = MibScalar
brLinkPowerOnCycles = _BrLinkPowerOnCycles_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 9, 8),
    _BrLinkPowerOnCycles_Type()
)
brLinkPowerOnCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLinkPowerOnCycles.setStatus("current")


class _BrLinkPowerOnHours_Type(Gauge32):
    """Custom type brLinkPowerOnHours based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_BrLinkPowerOnHours_Type.__name__ = "Gauge32"
_BrLinkPowerOnHours_Object = MibScalar
brLinkPowerOnHours = _BrLinkPowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 9, 9),
    _BrLinkPowerOnHours_Type()
)
brLinkPowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLinkPowerOnHours.setStatus("current")
if mibBuilder.loadTexts:
    brLinkPowerOnHours.setUnits("hours")


class _BrLink1Temperature_Type(Integer32):
    """Custom type brLink1Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrLink1Temperature_Type.__name__ = "Integer32"
_BrLink1Temperature_Object = MibScalar
brLink1Temperature = _BrLink1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 9, 10),
    _BrLink1Temperature_Type()
)
brLink1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLink1Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brLink1Temperature.setUnits("degrees Celsius")


class _BrLink2Temperature_Type(Integer32):
    """Custom type brLink2Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrLink2Temperature_Type.__name__ = "Integer32"
_BrLink2Temperature_Object = MibScalar
brLink2Temperature = _BrLink2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 9, 11),
    _BrLink2Temperature_Type()
)
brLink2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLink2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brLink2Temperature.setUnits("degrees Celsius")


class _BrLink3Temperature_Type(Integer32):
    """Custom type brLink3Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrLink3Temperature_Type.__name__ = "Integer32"
_BrLink3Temperature_Object = MibScalar
brLink3Temperature = _BrLink3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 9, 12),
    _BrLink3Temperature_Type()
)
brLink3Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLink3Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brLink3Temperature.setUnits("degrees Celsius")


class _BrLink4Temperature_Type(Integer32):
    """Custom type brLink4Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrLink4Temperature_Type.__name__ = "Integer32"
_BrLink4Temperature_Object = MibScalar
brLink4Temperature = _BrLink4Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 9, 13),
    _BrLink4Temperature_Type()
)
brLink4Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLink4Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brLink4Temperature.setUnits("degrees Celsius")
_BrLinkFpgaVersion_Type = DisplayString
_BrLinkFpgaVersion_Object = MibScalar
brLinkFpgaVersion = _BrLinkFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 9, 14),
    _BrLinkFpgaVersion_Type()
)
brLinkFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLinkFpgaVersion.setStatus("current")


class _BrLinkFpgaBootMode_Type(Integer32):
    """Custom type brLinkFpgaBootMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_BrLinkFpgaBootMode_Type.__name__ = "Integer32"
_BrLinkFpgaBootMode_Object = MibScalar
brLinkFpgaBootMode = _BrLinkFpgaBootMode_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 9, 15),
    _BrLinkFpgaBootMode_Type()
)
brLinkFpgaBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLinkFpgaBootMode.setStatus("current")
_BrIf2_ObjectIdentity = ObjectIdentity
brIf2 = _BrIf2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 10)
)
_BrIf2Present_Type = TruthValue
_BrIf2Present_Object = MibScalar
brIf2Present = _BrIf2Present_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 10, 1),
    _BrIf2Present_Type()
)
brIf2Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf2Present.setStatus("current")


class _BrIf2ModelNumber_Type(DisplayString):
    """Custom type brIf2ModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrIf2ModelNumber_Type.__name__ = "DisplayString"
_BrIf2ModelNumber_Object = MibScalar
brIf2ModelNumber = _BrIf2ModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 10, 2),
    _BrIf2ModelNumber_Type()
)
brIf2ModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf2ModelNumber.setStatus("current")


class _BrIf2SerialNumber_Type(DisplayString):
    """Custom type brIf2SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrIf2SerialNumber_Type.__name__ = "DisplayString"
_BrIf2SerialNumber_Object = MibScalar
brIf2SerialNumber = _BrIf2SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 10, 3),
    _BrIf2SerialNumber_Type()
)
brIf2SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf2SerialNumber.setStatus("current")


class _BrIf2HardwareRevision_Type(DisplayString):
    """Custom type brIf2HardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrIf2HardwareRevision_Type.__name__ = "DisplayString"
_BrIf2HardwareRevision_Object = MibScalar
brIf2HardwareRevision = _BrIf2HardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 10, 4),
    _BrIf2HardwareRevision_Type()
)
brIf2HardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf2HardwareRevision.setStatus("current")
_BrIf2DeviceId_Type = Unsigned32
_BrIf2DeviceId_Object = MibScalar
brIf2DeviceId = _BrIf2DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 10, 5),
    _BrIf2DeviceId_Type()
)
brIf2DeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf2DeviceId.setStatus("current")
_BrIf2CompatibilityId_Type = Unsigned32
_BrIf2CompatibilityId_Object = MibScalar
brIf2CompatibilityId = _BrIf2CompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 10, 6),
    _BrIf2CompatibilityId_Type()
)
brIf2CompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf2CompatibilityId.setStatus("current")


class _BrIf2FactorySettingsVersion_Type(DisplayString):
    """Custom type brIf2FactorySettingsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_BrIf2FactorySettingsVersion_Type.__name__ = "DisplayString"
_BrIf2FactorySettingsVersion_Object = MibScalar
brIf2FactorySettingsVersion = _BrIf2FactorySettingsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 10, 7),
    _BrIf2FactorySettingsVersion_Type()
)
brIf2FactorySettingsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf2FactorySettingsVersion.setStatus("current")


class _BrIf2PowerOnCycles_Type(Gauge32):
    """Custom type brIf2PowerOnCycles based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_BrIf2PowerOnCycles_Type.__name__ = "Gauge32"
_BrIf2PowerOnCycles_Object = MibScalar
brIf2PowerOnCycles = _BrIf2PowerOnCycles_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 10, 8),
    _BrIf2PowerOnCycles_Type()
)
brIf2PowerOnCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf2PowerOnCycles.setStatus("current")


class _BrIf2PowerOnHours_Type(Gauge32):
    """Custom type brIf2PowerOnHours based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_BrIf2PowerOnHours_Type.__name__ = "Gauge32"
_BrIf2PowerOnHours_Object = MibScalar
brIf2PowerOnHours = _BrIf2PowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 10, 9),
    _BrIf2PowerOnHours_Type()
)
brIf2PowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf2PowerOnHours.setStatus("current")
if mibBuilder.loadTexts:
    brIf2PowerOnHours.setUnits("hours")
_BrMem2_ObjectIdentity = ObjectIdentity
brMem2 = _BrMem2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 11)
)


class _BrMem2ModelNumber_Type(DisplayString):
    """Custom type brMem2ModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrMem2ModelNumber_Type.__name__ = "DisplayString"
_BrMem2ModelNumber_Object = MibScalar
brMem2ModelNumber = _BrMem2ModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 11, 1),
    _BrMem2ModelNumber_Type()
)
brMem2ModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMem2ModelNumber.setStatus("current")


class _BrMem2SerialNumber_Type(DisplayString):
    """Custom type brMem2SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrMem2SerialNumber_Type.__name__ = "DisplayString"
_BrMem2SerialNumber_Object = MibScalar
brMem2SerialNumber = _BrMem2SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 11, 2),
    _BrMem2SerialNumber_Type()
)
brMem2SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMem2SerialNumber.setStatus("current")


class _BrMem2HardwareRevision_Type(DisplayString):
    """Custom type brMem2HardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrMem2HardwareRevision_Type.__name__ = "DisplayString"
_BrMem2HardwareRevision_Object = MibScalar
brMem2HardwareRevision = _BrMem2HardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 11, 3),
    _BrMem2HardwareRevision_Type()
)
brMem2HardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMem2HardwareRevision.setStatus("current")
_BrMem2DeviceId_Type = Unsigned32
_BrMem2DeviceId_Object = MibScalar
brMem2DeviceId = _BrMem2DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 11, 4),
    _BrMem2DeviceId_Type()
)
brMem2DeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMem2DeviceId.setStatus("current")
_BrMem2CompatibilityId_Type = Unsigned32
_BrMem2CompatibilityId_Object = MibScalar
brMem2CompatibilityId = _BrMem2CompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 11, 5),
    _BrMem2CompatibilityId_Type()
)
brMem2CompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMem2CompatibilityId.setStatus("current")


class _BrMem2FactorySettingsVersion_Type(DisplayString):
    """Custom type brMem2FactorySettingsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_BrMem2FactorySettingsVersion_Type.__name__ = "DisplayString"
_BrMem2FactorySettingsVersion_Object = MibScalar
brMem2FactorySettingsVersion = _BrMem2FactorySettingsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 11, 6),
    _BrMem2FactorySettingsVersion_Type()
)
brMem2FactorySettingsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMem2FactorySettingsVersion.setStatus("current")
_BrMem2Present_Type = TruthValue
_BrMem2Present_Object = MibScalar
brMem2Present = _BrMem2Present_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 11, 7),
    _BrMem2Present_Type()
)
brMem2Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMem2Present.setStatus("current")
_BrFan_ObjectIdentity = ObjectIdentity
brFan = _BrFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 12)
)
_BrFanPresent_Type = TruthValue
_BrFanPresent_Object = MibScalar
brFanPresent = _BrFanPresent_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 12, 1),
    _BrFanPresent_Type()
)
brFanPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFanPresent.setStatus("current")


class _BrFanModelNumber_Type(DisplayString):
    """Custom type brFanModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrFanModelNumber_Type.__name__ = "DisplayString"
_BrFanModelNumber_Object = MibScalar
brFanModelNumber = _BrFanModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 12, 2),
    _BrFanModelNumber_Type()
)
brFanModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFanModelNumber.setStatus("current")


class _BrFanSerialNumber_Type(DisplayString):
    """Custom type brFanSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrFanSerialNumber_Type.__name__ = "DisplayString"
_BrFanSerialNumber_Object = MibScalar
brFanSerialNumber = _BrFanSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 12, 3),
    _BrFanSerialNumber_Type()
)
brFanSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFanSerialNumber.setStatus("current")


class _BrFanHardwareRevision_Type(DisplayString):
    """Custom type brFanHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrFanHardwareRevision_Type.__name__ = "DisplayString"
_BrFanHardwareRevision_Object = MibScalar
brFanHardwareRevision = _BrFanHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 12, 4),
    _BrFanHardwareRevision_Type()
)
brFanHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFanHardwareRevision.setStatus("current")
_BrFanDeviceId_Type = Unsigned32
_BrFanDeviceId_Object = MibScalar
brFanDeviceId = _BrFanDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 12, 5),
    _BrFanDeviceId_Type()
)
brFanDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFanDeviceId.setStatus("current")
_BrFanCompatibilityId_Type = Unsigned32
_BrFanCompatibilityId_Object = MibScalar
brFanCompatibilityId = _BrFanCompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 12, 6),
    _BrFanCompatibilityId_Type()
)
brFanCompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFanCompatibilityId.setStatus("current")


class _BrFanFactorySettingsVersion_Type(DisplayString):
    """Custom type brFanFactorySettingsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_BrFanFactorySettingsVersion_Type.__name__ = "DisplayString"
_BrFanFactorySettingsVersion_Object = MibScalar
brFanFactorySettingsVersion = _BrFanFactorySettingsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 12, 7),
    _BrFanFactorySettingsVersion_Type()
)
brFanFactorySettingsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFanFactorySettingsVersion.setStatus("current")


class _BrFanOnCycles_Type(Gauge32):
    """Custom type brFanOnCycles based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_BrFanOnCycles_Type.__name__ = "Gauge32"
_BrFanOnCycles_Object = MibScalar
brFanOnCycles = _BrFanOnCycles_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 12, 8),
    _BrFanOnCycles_Type()
)
brFanOnCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFanOnCycles.setStatus("current")


class _BrFanOnHours_Type(Gauge32):
    """Custom type brFanOnHours based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_BrFanOnHours_Type.__name__ = "Gauge32"
_BrFanOnHours_Object = MibScalar
brFanOnHours = _BrFanOnHours_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 12, 9),
    _BrFanOnHours_Type()
)
brFanOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFanOnHours.setStatus("current")
if mibBuilder.loadTexts:
    brFanOnHours.setUnits("hours")
_BrFan1Speed_Type = Unsigned32
_BrFan1Speed_Object = MibScalar
brFan1Speed = _BrFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 12, 10),
    _BrFan1Speed_Type()
)
brFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFan1Speed.setStatus("current")
if mibBuilder.loadTexts:
    brFan1Speed.setUnits("rpm")
_BrFan2Speed_Type = Unsigned32
_BrFan2Speed_Object = MibScalar
brFan2Speed = _BrFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 12, 11),
    _BrFan2Speed_Type()
)
brFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFan2Speed.setStatus("current")
if mibBuilder.loadTexts:
    brFan2Speed.setUnits("rpm")
_BrFan3Speed_Type = Unsigned32
_BrFan3Speed_Object = MibScalar
brFan3Speed = _BrFan3Speed_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 12, 12),
    _BrFan3Speed_Type()
)
brFan3Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFan3Speed.setStatus("current")
if mibBuilder.loadTexts:
    brFan3Speed.setUnits("rpm")
_BrFan4Speed_Type = Unsigned32
_BrFan4Speed_Object = MibScalar
brFan4Speed = _BrFan4Speed_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 12, 13),
    _BrFan4Speed_Type()
)
brFan4Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFan4Speed.setStatus("current")
if mibBuilder.loadTexts:
    brFan4Speed.setUnits("rpm")
_BrDrive1_ObjectIdentity = ObjectIdentity
brDrive1 = _BrDrive1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 13)
)
_BrDrive1Present_Type = TruthValue
_BrDrive1Present_Object = MibScalar
brDrive1Present = _BrDrive1Present_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 13, 1),
    _BrDrive1Present_Type()
)
brDrive1Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDrive1Present.setStatus("current")


class _BrDrive1ModelNumber_Type(DisplayString):
    """Custom type brDrive1ModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrDrive1ModelNumber_Type.__name__ = "DisplayString"
_BrDrive1ModelNumber_Object = MibScalar
brDrive1ModelNumber = _BrDrive1ModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 13, 2),
    _BrDrive1ModelNumber_Type()
)
brDrive1ModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDrive1ModelNumber.setStatus("current")


class _BrDrive1SerialNumber_Type(DisplayString):
    """Custom type brDrive1SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrDrive1SerialNumber_Type.__name__ = "DisplayString"
_BrDrive1SerialNumber_Object = MibScalar
brDrive1SerialNumber = _BrDrive1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 13, 3),
    _BrDrive1SerialNumber_Type()
)
brDrive1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDrive1SerialNumber.setStatus("current")


class _BrDrive1HardwareRevision_Type(DisplayString):
    """Custom type brDrive1HardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrDrive1HardwareRevision_Type.__name__ = "DisplayString"
_BrDrive1HardwareRevision_Object = MibScalar
brDrive1HardwareRevision = _BrDrive1HardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 13, 4),
    _BrDrive1HardwareRevision_Type()
)
brDrive1HardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDrive1HardwareRevision.setStatus("current")
_BrDrive1DeviceId_Type = Unsigned32
_BrDrive1DeviceId_Object = MibScalar
brDrive1DeviceId = _BrDrive1DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 13, 5),
    _BrDrive1DeviceId_Type()
)
brDrive1DeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDrive1DeviceId.setStatus("current")
_BrDrive1CompatibilityId_Type = Unsigned32
_BrDrive1CompatibilityId_Object = MibScalar
brDrive1CompatibilityId = _BrDrive1CompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 13, 6),
    _BrDrive1CompatibilityId_Type()
)
brDrive1CompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDrive1CompatibilityId.setStatus("current")


class _BrDrive1FactorySettingsVersion_Type(DisplayString):
    """Custom type brDrive1FactorySettingsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_BrDrive1FactorySettingsVersion_Type.__name__ = "DisplayString"
_BrDrive1FactorySettingsVersion_Object = MibScalar
brDrive1FactorySettingsVersion = _BrDrive1FactorySettingsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 13, 7),
    _BrDrive1FactorySettingsVersion_Type()
)
brDrive1FactorySettingsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDrive1FactorySettingsVersion.setStatus("current")


class _BrDrive1Temperature_Type(Integer32):
    """Custom type brDrive1Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrDrive1Temperature_Type.__name__ = "Integer32"
_BrDrive1Temperature_Object = MibScalar
brDrive1Temperature = _BrDrive1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 13, 8),
    _BrDrive1Temperature_Type()
)
brDrive1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDrive1Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brDrive1Temperature.setUnits("degrees Celsius")
_BrDrive2_ObjectIdentity = ObjectIdentity
brDrive2 = _BrDrive2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 14)
)
_BrDrive2Present_Type = TruthValue
_BrDrive2Present_Object = MibScalar
brDrive2Present = _BrDrive2Present_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 14, 1),
    _BrDrive2Present_Type()
)
brDrive2Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDrive2Present.setStatus("current")


class _BrDrive2ModelNumber_Type(DisplayString):
    """Custom type brDrive2ModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrDrive2ModelNumber_Type.__name__ = "DisplayString"
_BrDrive2ModelNumber_Object = MibScalar
brDrive2ModelNumber = _BrDrive2ModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 14, 2),
    _BrDrive2ModelNumber_Type()
)
brDrive2ModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDrive2ModelNumber.setStatus("current")


class _BrDrive2SerialNumber_Type(DisplayString):
    """Custom type brDrive2SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrDrive2SerialNumber_Type.__name__ = "DisplayString"
_BrDrive2SerialNumber_Object = MibScalar
brDrive2SerialNumber = _BrDrive2SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 14, 3),
    _BrDrive2SerialNumber_Type()
)
brDrive2SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDrive2SerialNumber.setStatus("current")


class _BrDrive2HardwareRevision_Type(DisplayString):
    """Custom type brDrive2HardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrDrive2HardwareRevision_Type.__name__ = "DisplayString"
_BrDrive2HardwareRevision_Object = MibScalar
brDrive2HardwareRevision = _BrDrive2HardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 14, 4),
    _BrDrive2HardwareRevision_Type()
)
brDrive2HardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDrive2HardwareRevision.setStatus("current")
_BrDrive2DeviceId_Type = Unsigned32
_BrDrive2DeviceId_Object = MibScalar
brDrive2DeviceId = _BrDrive2DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 14, 5),
    _BrDrive2DeviceId_Type()
)
brDrive2DeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDrive2DeviceId.setStatus("current")
_BrDrive2CompatibilityId_Type = Unsigned32
_BrDrive2CompatibilityId_Object = MibScalar
brDrive2CompatibilityId = _BrDrive2CompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 14, 6),
    _BrDrive2CompatibilityId_Type()
)
brDrive2CompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDrive2CompatibilityId.setStatus("current")


class _BrDrive2FactorySettingsVersion_Type(DisplayString):
    """Custom type brDrive2FactorySettingsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_BrDrive2FactorySettingsVersion_Type.__name__ = "DisplayString"
_BrDrive2FactorySettingsVersion_Object = MibScalar
brDrive2FactorySettingsVersion = _BrDrive2FactorySettingsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 14, 7),
    _BrDrive2FactorySettingsVersion_Type()
)
brDrive2FactorySettingsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDrive2FactorySettingsVersion.setStatus("current")


class _BrDrive2Temperature_Type(Integer32):
    """Custom type brDrive2Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrDrive2Temperature_Type.__name__ = "Integer32"
_BrDrive2Temperature_Object = MibScalar
brDrive2Temperature = _BrDrive2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 14, 8),
    _BrDrive2Temperature_Type()
)
brDrive2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDrive2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    brDrive2Temperature.setUnits("degrees Celsius")
_BrFan2_ObjectIdentity = ObjectIdentity
brFan2 = _BrFan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 15)
)
_BrFan2Present_Type = TruthValue
_BrFan2Present_Object = MibScalar
brFan2Present = _BrFan2Present_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 15, 1),
    _BrFan2Present_Type()
)
brFan2Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFan2Present.setStatus("current")


class _BrFan2ModelNumber_Type(DisplayString):
    """Custom type brFan2ModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrFan2ModelNumber_Type.__name__ = "DisplayString"
_BrFan2ModelNumber_Object = MibScalar
brFan2ModelNumber = _BrFan2ModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 15, 2),
    _BrFan2ModelNumber_Type()
)
brFan2ModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFan2ModelNumber.setStatus("current")


class _BrFan2SerialNumber_Type(DisplayString):
    """Custom type brFan2SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrFan2SerialNumber_Type.__name__ = "DisplayString"
_BrFan2SerialNumber_Object = MibScalar
brFan2SerialNumber = _BrFan2SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 15, 3),
    _BrFan2SerialNumber_Type()
)
brFan2SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFan2SerialNumber.setStatus("current")


class _BrFan2HardwareRevision_Type(DisplayString):
    """Custom type brFan2HardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrFan2HardwareRevision_Type.__name__ = "DisplayString"
_BrFan2HardwareRevision_Object = MibScalar
brFan2HardwareRevision = _BrFan2HardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 15, 4),
    _BrFan2HardwareRevision_Type()
)
brFan2HardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFan2HardwareRevision.setStatus("current")
_BrFan2DeviceId_Type = Unsigned32
_BrFan2DeviceId_Object = MibScalar
brFan2DeviceId = _BrFan2DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 15, 5),
    _BrFan2DeviceId_Type()
)
brFan2DeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFan2DeviceId.setStatus("current")
_BrFan2CompatibilityId_Type = Unsigned32
_BrFan2CompatibilityId_Object = MibScalar
brFan2CompatibilityId = _BrFan2CompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 15, 6),
    _BrFan2CompatibilityId_Type()
)
brFan2CompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFan2CompatibilityId.setStatus("current")


class _BrFan2FactorySettingsVersion_Type(DisplayString):
    """Custom type brFan2FactorySettingsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_BrFan2FactorySettingsVersion_Type.__name__ = "DisplayString"
_BrFan2FactorySettingsVersion_Object = MibScalar
brFan2FactorySettingsVersion = _BrFan2FactorySettingsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 15, 7),
    _BrFan2FactorySettingsVersion_Type()
)
brFan2FactorySettingsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFan2FactorySettingsVersion.setStatus("current")


class _BrFan2OnCycles_Type(Gauge32):
    """Custom type brFan2OnCycles based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_BrFan2OnCycles_Type.__name__ = "Gauge32"
_BrFan2OnCycles_Object = MibScalar
brFan2OnCycles = _BrFan2OnCycles_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 15, 8),
    _BrFan2OnCycles_Type()
)
brFan2OnCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFan2OnCycles.setStatus("current")


class _BrFan2OnHours_Type(Gauge32):
    """Custom type brFan2OnHours based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_BrFan2OnHours_Type.__name__ = "Gauge32"
_BrFan2OnHours_Object = MibScalar
brFan2OnHours = _BrFan2OnHours_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 15, 9),
    _BrFan2OnHours_Type()
)
brFan2OnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFan2OnHours.setStatus("current")
if mibBuilder.loadTexts:
    brFan2OnHours.setUnits("hours")
_BrFan21Speed_Type = Unsigned32
_BrFan21Speed_Object = MibScalar
brFan21Speed = _BrFan21Speed_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 15, 10),
    _BrFan21Speed_Type()
)
brFan21Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFan21Speed.setStatus("current")
if mibBuilder.loadTexts:
    brFan21Speed.setUnits("rpm")
_BrFan22Speed_Type = Unsigned32
_BrFan22Speed_Object = MibScalar
brFan22Speed = _BrFan22Speed_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 15, 11),
    _BrFan22Speed_Type()
)
brFan22Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFan22Speed.setStatus("current")
if mibBuilder.loadTexts:
    brFan22Speed.setUnits("rpm")
_BrFan23Speed_Type = Unsigned32
_BrFan23Speed_Object = MibScalar
brFan23Speed = _BrFan23Speed_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 15, 12),
    _BrFan23Speed_Type()
)
brFan23Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFan23Speed.setStatus("current")
if mibBuilder.loadTexts:
    brFan23Speed.setUnits("rpm")
_BrFan24Speed_Type = Unsigned32
_BrFan24Speed_Object = MibScalar
brFan24Speed = _BrFan24Speed_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 15, 13),
    _BrFan24Speed_Type()
)
brFan24Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFan24Speed.setStatus("current")
if mibBuilder.loadTexts:
    brFan24Speed.setUnits("rpm")
_BrIf3_ObjectIdentity = ObjectIdentity
brIf3 = _BrIf3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 16)
)
_BrIf3Present_Type = TruthValue
_BrIf3Present_Object = MibScalar
brIf3Present = _BrIf3Present_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 16, 1),
    _BrIf3Present_Type()
)
brIf3Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf3Present.setStatus("current")


class _BrIf3ModelNumber_Type(DisplayString):
    """Custom type brIf3ModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BrIf3ModelNumber_Type.__name__ = "DisplayString"
_BrIf3ModelNumber_Object = MibScalar
brIf3ModelNumber = _BrIf3ModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 16, 2),
    _BrIf3ModelNumber_Type()
)
brIf3ModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf3ModelNumber.setStatus("current")


class _BrIf3SerialNumber_Type(DisplayString):
    """Custom type brIf3SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_BrIf3SerialNumber_Type.__name__ = "DisplayString"
_BrIf3SerialNumber_Object = MibScalar
brIf3SerialNumber = _BrIf3SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 16, 3),
    _BrIf3SerialNumber_Type()
)
brIf3SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf3SerialNumber.setStatus("current")


class _BrIf3HardwareRevision_Type(DisplayString):
    """Custom type brIf3HardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BrIf3HardwareRevision_Type.__name__ = "DisplayString"
_BrIf3HardwareRevision_Object = MibScalar
brIf3HardwareRevision = _BrIf3HardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 16, 4),
    _BrIf3HardwareRevision_Type()
)
brIf3HardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf3HardwareRevision.setStatus("current")
_BrIf3DeviceId_Type = Unsigned32
_BrIf3DeviceId_Object = MibScalar
brIf3DeviceId = _BrIf3DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 16, 5),
    _BrIf3DeviceId_Type()
)
brIf3DeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf3DeviceId.setStatus("current")
_BrIf3CompatibilityId_Type = Unsigned32
_BrIf3CompatibilityId_Object = MibScalar
brIf3CompatibilityId = _BrIf3CompatibilityId_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 16, 6),
    _BrIf3CompatibilityId_Type()
)
brIf3CompatibilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf3CompatibilityId.setStatus("current")


class _BrIf3FactorySettingsVersion_Type(DisplayString):
    """Custom type brIf3FactorySettingsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_BrIf3FactorySettingsVersion_Type.__name__ = "DisplayString"
_BrIf3FactorySettingsVersion_Object = MibScalar
brIf3FactorySettingsVersion = _BrIf3FactorySettingsVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 16, 7),
    _BrIf3FactorySettingsVersion_Type()
)
brIf3FactorySettingsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf3FactorySettingsVersion.setStatus("current")


class _BrIf3PowerOnCycles_Type(Gauge32):
    """Custom type brIf3PowerOnCycles based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_BrIf3PowerOnCycles_Type.__name__ = "Gauge32"
_BrIf3PowerOnCycles_Object = MibScalar
brIf3PowerOnCycles = _BrIf3PowerOnCycles_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 16, 8),
    _BrIf3PowerOnCycles_Type()
)
brIf3PowerOnCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf3PowerOnCycles.setStatus("current")


class _BrIf3PowerOnHours_Type(Gauge32):
    """Custom type brIf3PowerOnHours based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_BrIf3PowerOnHours_Type.__name__ = "Gauge32"
_BrIf3PowerOnHours_Object = MibScalar
brIf3PowerOnHours = _BrIf3PowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 16, 9),
    _BrIf3PowerOnHours_Type()
)
brIf3PowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf3PowerOnHours.setStatus("current")
if mibBuilder.loadTexts:
    brIf3PowerOnHours.setUnits("hours")


class _BrIf3Temperature1_Type(Integer32):
    """Custom type brIf3Temperature1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_BrIf3Temperature1_Type.__name__ = "Integer32"
_BrIf3Temperature1_Object = MibScalar
brIf3Temperature1 = _BrIf3Temperature1_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 16, 10),
    _BrIf3Temperature1_Type()
)
brIf3Temperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf3Temperature1.setStatus("current")
if mibBuilder.loadTexts:
    brIf3Temperature1.setUnits("degrees Celsius")
_BrIf3FpgaVersion_Type = DisplayString
_BrIf3FpgaVersion_Object = MibScalar
brIf3FpgaVersion = _BrIf3FpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 16, 11),
    _BrIf3FpgaVersion_Type()
)
brIf3FpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf3FpgaVersion.setStatus("current")


class _BrIf3FpgaBootMode_Type(Integer32):
    """Custom type brIf3FpgaBootMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_BrIf3FpgaBootMode_Type.__name__ = "Integer32"
_BrIf3FpgaBootMode_Object = MibScalar
brIf3FpgaBootMode = _BrIf3FpgaBootMode_Object(
    (1, 3, 6, 1, 4, 1, 29312, 2, 1, 16, 12),
    _BrIf3FpgaBootMode_Type()
)
brIf3FpgaBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIf3FpgaBootMode.setStatus("current")
_BrAdiConformance_ObjectIdentity = ObjectIdentity
brAdiConformance = _BrAdiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2)
)
_BrAdiCompliances_ObjectIdentity = ObjectIdentity
brAdiCompliances = _BrAdiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 1)
)
_BrAdiGroups_ObjectIdentity = ObjectIdentity
brAdiGroups = _BrAdiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 2)
)

# Managed Objects groups

brAdiPcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 2, 1)
)
brAdiPcGroup.setObjects(
      *(("BR-ADI-MIB", "brPcModelNumber"),
        ("BR-ADI-MIB", "brPcSerialNumber"),
        ("BR-ADI-MIB", "brPcHardwareRevision"),
        ("BR-ADI-MIB", "brPcDeviceId"),
        ("BR-ADI-MIB", "brPcCompatibilityId"),
        ("BR-ADI-MIB", "brPcDeviceType"),
        ("BR-ADI-MIB", "brPcBiosVersion"),
        ("BR-ADI-MIB", "brPcBrOsVersion"),
        ("BR-ADI-MIB", "brPcCmosProfile"),
        ("BR-ADI-MIB", "brPcCpuBoardType"),
        ("BR-ADI-MIB", "brPcFactorySettingsVersion"),
        ("BR-ADI-MIB", "brPcApLinkFpgaVersion"),
        ("BR-ADI-MIB", "brPcApLinkPresent"),
        ("BR-ADI-MIB", "brPcMtcxFpgaVersion"),
        ("BR-ADI-MIB", "brPcMtcxPx32Version"),
        ("BR-ADI-MIB", "brPcUserSerialId"),
        ("BR-ADI-MIB", "brPcPowerOnCycles"),
        ("BR-ADI-MIB", "brPcPowerOnHours"),
        ("BR-ADI-MIB", "brPcFanOnHours"),
        ("BR-ADI-MIB", "brPcBatteryState"),
        ("BR-ADI-MIB", "brPcBoardCenterTemperature"),
        ("BR-ADI-MIB", "brPcBoardEth2Temperature"),
        ("BR-ADI-MIB", "brPcBoardInTemperature"),
        ("BR-ADI-MIB", "brPcBoardIoTemperature"),
        ("BR-ADI-MIB", "brPcBoardOutTemperature"),
        ("BR-ADI-MIB", "brPcBoardPowerTemperature"),
        ("BR-ADI-MIB", "brPcCaseFan1Speed"),
        ("BR-ADI-MIB", "brPcCaseFan2Speed"),
        ("BR-ADI-MIB", "brPcCaseFan3Speed"),
        ("BR-ADI-MIB", "brPcCaseFan4Speed"),
        ("BR-ADI-MIB", "brPcCpuBoardTemperature"),
        ("BR-ADI-MIB", "brPcCpuTemperature"),
        ("BR-ADI-MIB", "brPcDrive1Temperature"),
        ("BR-ADI-MIB", "brPcDrive2Temperature"),
        ("BR-ADI-MIB", "brPcEth2Temperature"),
        ("BR-ADI-MIB", "brPcIfSlotTemperature"),
        ("BR-ADI-MIB", "brPcPowerTemperature"),
        ("BR-ADI-MIB", "brPcModeNode"),
        ("BR-ADI-MIB", "brPcMtcxVersion"),
        ("BR-ADI-MIB", "brPcSys1Temperature"),
        ("BR-ADI-MIB", "brPcSys2Temperature"),
        ("BR-ADI-MIB", "brPcSys3Temperature"),
        ("BR-ADI-MIB", "brPcSys4Temperature"),
        ("BR-ADI-MIB", "brPcBiosBootMode"),
        ("BR-ADI-MIB", "brPcMtcxBootMode"))
)
if mibBuilder.loadTexts:
    brAdiPcGroup.setStatus("current")

brAdiUpsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 2, 2)
)
brAdiUpsGroup.setObjects(
      *(("BR-ADI-MIB", "brUpsDetected"),
        ("BR-ADI-MIB", "brUpsLinked"),
        ("BR-ADI-MIB", "brUpsModelNumber"),
        ("BR-ADI-MIB", "brUpsSerialNumber"),
        ("BR-ADI-MIB", "brUpsHardwareRevision"),
        ("BR-ADI-MIB", "brUpsDeviceId"),
        ("BR-ADI-MIB", "brUpsCompatibilityId"),
        ("BR-ADI-MIB", "brUpsFirmwareVersion"),
        ("BR-ADI-MIB", "brUpsFactorySettingsVersion"),
        ("BR-ADI-MIB", "brUpsBatterySettingsVersion"),
        ("BR-ADI-MIB", "brUpsStatus"),
        ("BR-ADI-MIB", "brUpsBatteryCurrent"),
        ("BR-ADI-MIB", "brUpsBatteryVoltage"),
        ("BR-ADI-MIB", "brUpsBatteryTemperature"),
        ("BR-ADI-MIB", "brUpsOnBatteryCycles"),
        ("BR-ADI-MIB", "brUpsBatteryOnHours"),
        ("BR-ADI-MIB", "brUpsType"))
)
if mibBuilder.loadTexts:
    brAdiUpsGroup.setStatus("current")

brAdiPanelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 2, 3)
)
brAdiPanelGroup.setObjects(
      *(("BR-ADI-MIB", "brPanelCount"),
        ("BR-ADI-MIB", "brPanelAddress"),
        ("BR-ADI-MIB", "brPanelDetected"),
        ("BR-ADI-MIB", "brPanelLinked"),
        ("BR-ADI-MIB", "brPanelLocked"),
        ("BR-ADI-MIB", "brPanelModelNumber"),
        ("BR-ADI-MIB", "brPanelSerialNumber"),
        ("BR-ADI-MIB", "brPanelHardwareRevision"),
        ("BR-ADI-MIB", "brPanelDeviceId"),
        ("BR-ADI-MIB", "brPanelCompatibilityId"),
        ("BR-ADI-MIB", "brPanelApLinkFpgaVersion"),
        ("BR-ADI-MIB", "brPanelBacklightOnCycles"),
        ("BR-ADI-MIB", "brPanelBacklightOnHours"),
        ("BR-ADI-MIB", "brPanelTemperature"),
        ("BR-ADI-MIB", "brPanelPowerOnCycles"),
        ("BR-ADI-MIB", "brPanelPowerOnHours"),
        ("BR-ADI-MIB", "brPanelExpansionUnitPresent"),
        ("BR-ADI-MIB", "brPanelExpansionUnitModelNumber"),
        ("BR-ADI-MIB", "brPanelExpansionUnitSerialNumber"),
        ("BR-ADI-MIB", "brPanelExpansionUnitHardwareRevision"),
        ("BR-ADI-MIB", "brPanelExpansionUnitDeviceId"),
        ("BR-ADI-MIB", "brPanelExpansionUnitCompatibilityId"),
        ("BR-ADI-MIB", "brPanelExpansionUnitFactorySettingsVersion"),
        ("BR-ADI-MIB", "brPanelExpansionUnitPowerOnCycles"),
        ("BR-ADI-MIB", "brPanelExpansionUnitPowerOnHours"),
        ("BR-ADI-MIB", "brPanelLinkPresent"),
        ("BR-ADI-MIB", "brPanelLinkType"),
        ("BR-ADI-MIB", "brPanelLinkModelNumber"),
        ("BR-ADI-MIB", "brPanelLinkSerialNumber"),
        ("BR-ADI-MIB", "brPanelLinkHardwareRevision"),
        ("BR-ADI-MIB", "brPanelLinkDeviceId"),
        ("BR-ADI-MIB", "brPanelLinkCompatibilityId"),
        ("BR-ADI-MIB", "brPanelLinkFactorySettingsVersion"),
        ("BR-ADI-MIB", "brPanelLinkFpgaVersion"),
        ("BR-ADI-MIB", "brPanelLinkHdbtVersion"),
        ("BR-ADI-MIB", "brPanelConverterPresent"),
        ("BR-ADI-MIB", "brPanelConverterModelNumber"),
        ("BR-ADI-MIB", "brPanelConverterSerialNumber"),
        ("BR-ADI-MIB", "brPanelConverterHardwareRevision"),
        ("BR-ADI-MIB", "brPanelConverterDeviceId"),
        ("BR-ADI-MIB", "brPanelConverterCompatibilityId"),
        ("BR-ADI-MIB", "brPanelConverterFpgaVersion"),
        ("BR-ADI-MIB", "brPanelConverterFpgaBootMode"))
)
if mibBuilder.loadTexts:
    brAdiPanelGroup.setStatus("current")

brAdiCpuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 2, 4)
)
brAdiCpuGroup.setObjects(
      *(("BR-ADI-MIB", "brCpuModelNumber"),
        ("BR-ADI-MIB", "brCpuSerialNumber"),
        ("BR-ADI-MIB", "brCpuHardwareRevision"),
        ("BR-ADI-MIB", "brCpuDeviceId"),
        ("BR-ADI-MIB", "brCpuCompatibilityId"),
        ("BR-ADI-MIB", "brCpuFactorySettingsVersion"),
        ("BR-ADI-MIB", "brCpuPowerOnCycles"),
        ("BR-ADI-MIB", "brCpuPowerOnHours"),
        ("BR-ADI-MIB", "brCpu1Temperature"),
        ("BR-ADI-MIB", "brCpu2Temperature"),
        ("BR-ADI-MIB", "brCpu3Temperature"),
        ("BR-ADI-MIB", "brCpu4Temperature"),
        ("BR-ADI-MIB", "brCpuPower"))
)
if mibBuilder.loadTexts:
    brAdiCpuGroup.setStatus("current")

brAdiMemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 2, 5)
)
brAdiMemGroup.setObjects(
      *(("BR-ADI-MIB", "brMemModelNumber"),
        ("BR-ADI-MIB", "brMemSerialNumber"),
        ("BR-ADI-MIB", "brMemHardwareRevision"),
        ("BR-ADI-MIB", "brMemDeviceId"),
        ("BR-ADI-MIB", "brMemCompatibilityId"),
        ("BR-ADI-MIB", "brMemFactorySettingsVersion"),
        ("BR-ADI-MIB", "brMemPresent"))
)
if mibBuilder.loadTexts:
    brAdiMemGroup.setStatus("current")

brAdiIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 2, 6)
)
brAdiIfGroup.setObjects(
      *(("BR-ADI-MIB", "brIfPresent"),
        ("BR-ADI-MIB", "brIfModelNumber"),
        ("BR-ADI-MIB", "brIfSerialNumber"),
        ("BR-ADI-MIB", "brIfHardwareRevision"),
        ("BR-ADI-MIB", "brIfDeviceId"),
        ("BR-ADI-MIB", "brIfCompatibilityId"),
        ("BR-ADI-MIB", "brIfFactorySettingsVersion"),
        ("BR-ADI-MIB", "brIfPowerOnCycles"),
        ("BR-ADI-MIB", "brIfPowerOnHours"),
        ("BR-ADI-MIB", "brIf1Temperature"),
        ("BR-ADI-MIB", "brIf2Temperature"),
        ("BR-ADI-MIB", "brIf3Temperature"),
        ("BR-ADI-MIB", "brIf4Temperature"))
)
if mibBuilder.loadTexts:
    brAdiIfGroup.setStatus("current")

brAdiIoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 2, 7)
)
brAdiIoGroup.setObjects(
      *(("BR-ADI-MIB", "brIoPresent"),
        ("BR-ADI-MIB", "brIoModelNumber"),
        ("BR-ADI-MIB", "brIoSerialNumber"),
        ("BR-ADI-MIB", "brIoHardwareRevision"),
        ("BR-ADI-MIB", "brIoDeviceId"),
        ("BR-ADI-MIB", "brIoCompatibilityId"),
        ("BR-ADI-MIB", "brIoFactorySettingsVersion"),
        ("BR-ADI-MIB", "brIoPowerOnCycles"),
        ("BR-ADI-MIB", "brIoPowerOnHours"),
        ("BR-ADI-MIB", "brIo1Temperature"),
        ("BR-ADI-MIB", "brIo2Temperature"),
        ("BR-ADI-MIB", "brIo3Temperature"),
        ("BR-ADI-MIB", "brIo4Temperature"),
        ("BR-ADI-MIB", "brIoFpgaVersion"),
        ("BR-ADI-MIB", "brIoFpgaBootMode"))
)
if mibBuilder.loadTexts:
    brAdiIoGroup.setStatus("current")

brAdiBusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 2, 8)
)
brAdiBusGroup.setObjects(
      *(("BR-ADI-MIB", "brBusModelNumber"),
        ("BR-ADI-MIB", "brBusSerialNumber"),
        ("BR-ADI-MIB", "brBusHardwareRevision"),
        ("BR-ADI-MIB", "brBusDeviceId"),
        ("BR-ADI-MIB", "brBusCompatibilityId"),
        ("BR-ADI-MIB", "brBusFactorySettingsVersion"),
        ("BR-ADI-MIB", "brBusPowerOnCycles"),
        ("BR-ADI-MIB", "brBusPowerOnHours"),
        ("BR-ADI-MIB", "brBusPresent"))
)
if mibBuilder.loadTexts:
    brAdiBusGroup.setStatus("current")

brAdiLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 2, 9)
)
brAdiLinkGroup.setObjects(
      *(("BR-ADI-MIB", "brLinkPresent"),
        ("BR-ADI-MIB", "brLinkModelNumber"),
        ("BR-ADI-MIB", "brLinkSerialNumber"),
        ("BR-ADI-MIB", "brLinkHardwareRevision"),
        ("BR-ADI-MIB", "brLinkDeviceId"),
        ("BR-ADI-MIB", "brLinkCompatibilityId"),
        ("BR-ADI-MIB", "brLinkFactorySettingsVersion"),
        ("BR-ADI-MIB", "brLinkPowerOnCycles"),
        ("BR-ADI-MIB", "brLinkPowerOnHours"),
        ("BR-ADI-MIB", "brLink1Temperature"),
        ("BR-ADI-MIB", "brLink2Temperature"),
        ("BR-ADI-MIB", "brLink3Temperature"),
        ("BR-ADI-MIB", "brLink4Temperature"),
        ("BR-ADI-MIB", "brLinkFpgaVersion"),
        ("BR-ADI-MIB", "brLinkFpgaBootMode"))
)
if mibBuilder.loadTexts:
    brAdiLinkGroup.setStatus("current")

brAdiIf2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 2, 10)
)
brAdiIf2Group.setObjects(
      *(("BR-ADI-MIB", "brIf2Present"),
        ("BR-ADI-MIB", "brIf2ModelNumber"),
        ("BR-ADI-MIB", "brIf2SerialNumber"),
        ("BR-ADI-MIB", "brIf2HardwareRevision"),
        ("BR-ADI-MIB", "brIf2DeviceId"),
        ("BR-ADI-MIB", "brIf2CompatibilityId"),
        ("BR-ADI-MIB", "brIf2FactorySettingsVersion"),
        ("BR-ADI-MIB", "brIf2PowerOnCycles"),
        ("BR-ADI-MIB", "brIf2PowerOnHours"))
)
if mibBuilder.loadTexts:
    brAdiIf2Group.setStatus("current")

brAdiMem2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 2, 11)
)
brAdiMem2Group.setObjects(
      *(("BR-ADI-MIB", "brMem2ModelNumber"),
        ("BR-ADI-MIB", "brMem2SerialNumber"),
        ("BR-ADI-MIB", "brMem2HardwareRevision"),
        ("BR-ADI-MIB", "brMem2DeviceId"),
        ("BR-ADI-MIB", "brMem2CompatibilityId"),
        ("BR-ADI-MIB", "brMem2FactorySettingsVersion"),
        ("BR-ADI-MIB", "brMem2Present"))
)
if mibBuilder.loadTexts:
    brAdiMem2Group.setStatus("current")

brAdiFanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 2, 12)
)
brAdiFanGroup.setObjects(
      *(("BR-ADI-MIB", "brFanPresent"),
        ("BR-ADI-MIB", "brFanModelNumber"),
        ("BR-ADI-MIB", "brFanSerialNumber"),
        ("BR-ADI-MIB", "brFanHardwareRevision"),
        ("BR-ADI-MIB", "brFanDeviceId"),
        ("BR-ADI-MIB", "brFanCompatibilityId"),
        ("BR-ADI-MIB", "brFanFactorySettingsVersion"),
        ("BR-ADI-MIB", "brFanOnCycles"),
        ("BR-ADI-MIB", "brFanOnHours"),
        ("BR-ADI-MIB", "brFan1Speed"),
        ("BR-ADI-MIB", "brFan2Speed"),
        ("BR-ADI-MIB", "brFan3Speed"),
        ("BR-ADI-MIB", "brFan4Speed"))
)
if mibBuilder.loadTexts:
    brAdiFanGroup.setStatus("current")

brAdiDrive1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 2, 13)
)
brAdiDrive1Group.setObjects(
      *(("BR-ADI-MIB", "brDrive1Present"),
        ("BR-ADI-MIB", "brDrive1ModelNumber"),
        ("BR-ADI-MIB", "brDrive1SerialNumber"),
        ("BR-ADI-MIB", "brDrive1HardwareRevision"),
        ("BR-ADI-MIB", "brDrive1DeviceId"),
        ("BR-ADI-MIB", "brDrive1CompatibilityId"),
        ("BR-ADI-MIB", "brDrive1FactorySettingsVersion"),
        ("BR-ADI-MIB", "brDrive1Temperature"))
)
if mibBuilder.loadTexts:
    brAdiDrive1Group.setStatus("current")

brAdiDrive2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 2, 14)
)
brAdiDrive2Group.setObjects(
      *(("BR-ADI-MIB", "brDrive2Present"),
        ("BR-ADI-MIB", "brDrive2ModelNumber"),
        ("BR-ADI-MIB", "brDrive2SerialNumber"),
        ("BR-ADI-MIB", "brDrive2HardwareRevision"),
        ("BR-ADI-MIB", "brDrive2DeviceId"),
        ("BR-ADI-MIB", "brDrive2CompatibilityId"),
        ("BR-ADI-MIB", "brDrive2FactorySettingsVersion"),
        ("BR-ADI-MIB", "brDrive2Temperature"))
)
if mibBuilder.loadTexts:
    brAdiDrive2Group.setStatus("current")

brAdiFan2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 2, 15)
)
brAdiFan2Group.setObjects(
      *(("BR-ADI-MIB", "brFan2Present"),
        ("BR-ADI-MIB", "brFan2ModelNumber"),
        ("BR-ADI-MIB", "brFan2SerialNumber"),
        ("BR-ADI-MIB", "brFan2HardwareRevision"),
        ("BR-ADI-MIB", "brFan2DeviceId"),
        ("BR-ADI-MIB", "brFan2CompatibilityId"),
        ("BR-ADI-MIB", "brFan2FactorySettingsVersion"),
        ("BR-ADI-MIB", "brFan2OnCycles"),
        ("BR-ADI-MIB", "brFan2OnHours"),
        ("BR-ADI-MIB", "brFan21Speed"),
        ("BR-ADI-MIB", "brFan22Speed"),
        ("BR-ADI-MIB", "brFan23Speed"),
        ("BR-ADI-MIB", "brFan24Speed"))
)
if mibBuilder.loadTexts:
    brAdiFan2Group.setStatus("current")

brAdiIf3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 2, 16)
)
brAdiIf3Group.setObjects(
      *(("BR-ADI-MIB", "brIf3Present"),
        ("BR-ADI-MIB", "brIf3ModelNumber"),
        ("BR-ADI-MIB", "brIf3SerialNumber"),
        ("BR-ADI-MIB", "brIf3HardwareRevision"),
        ("BR-ADI-MIB", "brIf3DeviceId"),
        ("BR-ADI-MIB", "brIf3CompatibilityId"),
        ("BR-ADI-MIB", "brIf3FactorySettingsVersion"),
        ("BR-ADI-MIB", "brIf3PowerOnCycles"),
        ("BR-ADI-MIB", "brIf3PowerOnHours"),
        ("BR-ADI-MIB", "brIf3Temperature1"),
        ("BR-ADI-MIB", "brIf3FpgaVersion"),
        ("BR-ADI-MIB", "brIf3FpgaBootMode"))
)
if mibBuilder.loadTexts:
    brAdiIf3Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

brAdiModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 29312, 2, 2, 1, 1)
)
brAdiModuleCompliance.setObjects(
      *(("BR-ADI-MIB", "brAdiPcGroup"),
        ("BR-ADI-MIB", "brAdiUpsGroup"),
        ("BR-ADI-MIB", "brAdiPanelGroup"),
        ("BR-ADI-MIB", "brAdiCpuGroup"),
        ("BR-ADI-MIB", "brAdiMemGroup"),
        ("BR-ADI-MIB", "brAdiIfGroup"),
        ("BR-ADI-MIB", "brAdiIoGroup"),
        ("BR-ADI-MIB", "brAdiBusGroup"),
        ("BR-ADI-MIB", "brAdiLinkGroup"),
        ("BR-ADI-MIB", "brAdiIf2Group"),
        ("BR-ADI-MIB", "brAdiMem2Group"),
        ("BR-ADI-MIB", "brAdiFanGroup"),
        ("BR-ADI-MIB", "brAdiDrive1Group"),
        ("BR-ADI-MIB", "brAdiDrive2Group"),
        ("BR-ADI-MIB", "brAdiFan2Group"),
        ("BR-ADI-MIB", "brAdiIf3Group"))
)
if mibBuilder.loadTexts:
    brAdiModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BR-ADI-MIB",
    **{"brAdiMIB": brAdiMIB,
       "brAdiObjects": brAdiObjects,
       "brPc": brPc,
       "brPcModelNumber": brPcModelNumber,
       "brPcSerialNumber": brPcSerialNumber,
       "brPcHardwareRevision": brPcHardwareRevision,
       "brPcDeviceId": brPcDeviceId,
       "brPcCompatibilityId": brPcCompatibilityId,
       "brPcDeviceType": brPcDeviceType,
       "brPcBiosVersion": brPcBiosVersion,
       "brPcBrOsVersion": brPcBrOsVersion,
       "brPcCmosProfile": brPcCmosProfile,
       "brPcCpuBoardType": brPcCpuBoardType,
       "brPcFactorySettingsVersion": brPcFactorySettingsVersion,
       "brPcApLinkFpgaVersion": brPcApLinkFpgaVersion,
       "brPcApLinkPresent": brPcApLinkPresent,
       "brPcMtcxFpgaVersion": brPcMtcxFpgaVersion,
       "brPcMtcxPx32Version": brPcMtcxPx32Version,
       "brPcUserSerialId": brPcUserSerialId,
       "brPcPowerOnCycles": brPcPowerOnCycles,
       "brPcPowerOnHours": brPcPowerOnHours,
       "brPcFanOnHours": brPcFanOnHours,
       "brPcBatteryState": brPcBatteryState,
       "brPcBoardCenterTemperature": brPcBoardCenterTemperature,
       "brPcBoardEth2Temperature": brPcBoardEth2Temperature,
       "brPcBoardInTemperature": brPcBoardInTemperature,
       "brPcBoardIoTemperature": brPcBoardIoTemperature,
       "brPcBoardOutTemperature": brPcBoardOutTemperature,
       "brPcBoardPowerTemperature": brPcBoardPowerTemperature,
       "brPcCaseFan1Speed": brPcCaseFan1Speed,
       "brPcCaseFan2Speed": brPcCaseFan2Speed,
       "brPcCaseFan3Speed": brPcCaseFan3Speed,
       "brPcCaseFan4Speed": brPcCaseFan4Speed,
       "brPcCpuBoardTemperature": brPcCpuBoardTemperature,
       "brPcCpuTemperature": brPcCpuTemperature,
       "brPcDrive1Temperature": brPcDrive1Temperature,
       "brPcDrive2Temperature": brPcDrive2Temperature,
       "brPcEth2Temperature": brPcEth2Temperature,
       "brPcIfSlotTemperature": brPcIfSlotTemperature,
       "brPcPowerTemperature": brPcPowerTemperature,
       "brPcModeNode": brPcModeNode,
       "brPcMtcxVersion": brPcMtcxVersion,
       "brPcSys1Temperature": brPcSys1Temperature,
       "brPcSys2Temperature": brPcSys2Temperature,
       "brPcSys3Temperature": brPcSys3Temperature,
       "brPcSys4Temperature": brPcSys4Temperature,
       "brPcBiosBootMode": brPcBiosBootMode,
       "brPcMtcxBootMode": brPcMtcxBootMode,
       "brUps": brUps,
       "brUpsDetected": brUpsDetected,
       "brUpsLinked": brUpsLinked,
       "brUpsModelNumber": brUpsModelNumber,
       "brUpsSerialNumber": brUpsSerialNumber,
       "brUpsHardwareRevision": brUpsHardwareRevision,
       "brUpsDeviceId": brUpsDeviceId,
       "brUpsCompatibilityId": brUpsCompatibilityId,
       "brUpsFirmwareVersion": brUpsFirmwareVersion,
       "brUpsFactorySettingsVersion": brUpsFactorySettingsVersion,
       "brUpsBatterySettingsVersion": brUpsBatterySettingsVersion,
       "brUpsStatus": brUpsStatus,
       "brUpsBatteryCurrent": brUpsBatteryCurrent,
       "brUpsBatteryVoltage": brUpsBatteryVoltage,
       "brUpsBatteryTemperature": brUpsBatteryTemperature,
       "brUpsOnBatteryCycles": brUpsOnBatteryCycles,
       "brUpsBatteryOnHours": brUpsBatteryOnHours,
       "brUpsType": brUpsType,
       "brPanel": brPanel,
       "brPanelCount": brPanelCount,
       "brPanelTable": brPanelTable,
       "brPanelEntry": brPanelEntry,
       "brPanelIndex": brPanelIndex,
       "brPanelAddress": brPanelAddress,
       "brPanelDetected": brPanelDetected,
       "brPanelLinked": brPanelLinked,
       "brPanelLocked": brPanelLocked,
       "brPanelModelNumber": brPanelModelNumber,
       "brPanelSerialNumber": brPanelSerialNumber,
       "brPanelHardwareRevision": brPanelHardwareRevision,
       "brPanelDeviceId": brPanelDeviceId,
       "brPanelCompatibilityId": brPanelCompatibilityId,
       "brPanelApLinkFpgaVersion": brPanelApLinkFpgaVersion,
       "brPanelBacklightOnCycles": brPanelBacklightOnCycles,
       "brPanelBacklightOnHours": brPanelBacklightOnHours,
       "brPanelTemperature": brPanelTemperature,
       "brPanelPowerOnCycles": brPanelPowerOnCycles,
       "brPanelPowerOnHours": brPanelPowerOnHours,
       "brPanelExpansionUnitTable": brPanelExpansionUnitTable,
       "brPanelExpansionUnitEntry": brPanelExpansionUnitEntry,
       "brPanelExpansionUnitIndex": brPanelExpansionUnitIndex,
       "brPanelExpansionUnitPresent": brPanelExpansionUnitPresent,
       "brPanelExpansionUnitModelNumber": brPanelExpansionUnitModelNumber,
       "brPanelExpansionUnitSerialNumber": brPanelExpansionUnitSerialNumber,
       "brPanelExpansionUnitHardwareRevision": brPanelExpansionUnitHardwareRevision,
       "brPanelExpansionUnitDeviceId": brPanelExpansionUnitDeviceId,
       "brPanelExpansionUnitCompatibilityId": brPanelExpansionUnitCompatibilityId,
       "brPanelExpansionUnitFactorySettingsVersion": brPanelExpansionUnitFactorySettingsVersion,
       "brPanelExpansionUnitPowerOnCycles": brPanelExpansionUnitPowerOnCycles,
       "brPanelExpansionUnitPowerOnHours": brPanelExpansionUnitPowerOnHours,
       "brPanelLinkTable": brPanelLinkTable,
       "brPanelLinkEntry": brPanelLinkEntry,
       "brPanelLinkIndex": brPanelLinkIndex,
       "brPanelLinkPresent": brPanelLinkPresent,
       "brPanelLinkType": brPanelLinkType,
       "brPanelLinkModelNumber": brPanelLinkModelNumber,
       "brPanelLinkSerialNumber": brPanelLinkSerialNumber,
       "brPanelLinkHardwareRevision": brPanelLinkHardwareRevision,
       "brPanelLinkDeviceId": brPanelLinkDeviceId,
       "brPanelLinkCompatibilityId": brPanelLinkCompatibilityId,
       "brPanelLinkFactorySettingsVersion": brPanelLinkFactorySettingsVersion,
       "brPanelLinkFpgaVersion": brPanelLinkFpgaVersion,
       "brPanelLinkHdbtVersion": brPanelLinkHdbtVersion,
       "brPanelConverterTable": brPanelConverterTable,
       "brPanelConverterEntry": brPanelConverterEntry,
       "brPanelConverterIndex": brPanelConverterIndex,
       "brPanelConverterPresent": brPanelConverterPresent,
       "brPanelConverterModelNumber": brPanelConverterModelNumber,
       "brPanelConverterSerialNumber": brPanelConverterSerialNumber,
       "brPanelConverterHardwareRevision": brPanelConverterHardwareRevision,
       "brPanelConverterDeviceId": brPanelConverterDeviceId,
       "brPanelConverterCompatibilityId": brPanelConverterCompatibilityId,
       "brPanelConverterFpgaVersion": brPanelConverterFpgaVersion,
       "brPanelConverterFpgaBootMode": brPanelConverterFpgaBootMode,
       "brCpu": brCpu,
       "brCpuModelNumber": brCpuModelNumber,
       "brCpuSerialNumber": brCpuSerialNumber,
       "brCpuHardwareRevision": brCpuHardwareRevision,
       "brCpuDeviceId": brCpuDeviceId,
       "brCpuCompatibilityId": brCpuCompatibilityId,
       "brCpuFactorySettingsVersion": brCpuFactorySettingsVersion,
       "brCpuPowerOnCycles": brCpuPowerOnCycles,
       "brCpuPowerOnHours": brCpuPowerOnHours,
       "brCpu1Temperature": brCpu1Temperature,
       "brCpu2Temperature": brCpu2Temperature,
       "brCpu3Temperature": brCpu3Temperature,
       "brCpu4Temperature": brCpu4Temperature,
       "brCpuPower": brCpuPower,
       "brMem": brMem,
       "brMemModelNumber": brMemModelNumber,
       "brMemSerialNumber": brMemSerialNumber,
       "brMemHardwareRevision": brMemHardwareRevision,
       "brMemDeviceId": brMemDeviceId,
       "brMemCompatibilityId": brMemCompatibilityId,
       "brMemFactorySettingsVersion": brMemFactorySettingsVersion,
       "brMemPresent": brMemPresent,
       "brIf": brIf,
       "brIfPresent": brIfPresent,
       "brIfModelNumber": brIfModelNumber,
       "brIfSerialNumber": brIfSerialNumber,
       "brIfHardwareRevision": brIfHardwareRevision,
       "brIfDeviceId": brIfDeviceId,
       "brIfCompatibilityId": brIfCompatibilityId,
       "brIfFactorySettingsVersion": brIfFactorySettingsVersion,
       "brIfPowerOnCycles": brIfPowerOnCycles,
       "brIfPowerOnHours": brIfPowerOnHours,
       "brIf1Temperature": brIf1Temperature,
       "brIf2Temperature": brIf2Temperature,
       "brIf3Temperature": brIf3Temperature,
       "brIf4Temperature": brIf4Temperature,
       "brIo": brIo,
       "brIoPresent": brIoPresent,
       "brIoModelNumber": brIoModelNumber,
       "brIoSerialNumber": brIoSerialNumber,
       "brIoHardwareRevision": brIoHardwareRevision,
       "brIoDeviceId": brIoDeviceId,
       "brIoCompatibilityId": brIoCompatibilityId,
       "brIoFactorySettingsVersion": brIoFactorySettingsVersion,
       "brIoPowerOnCycles": brIoPowerOnCycles,
       "brIoPowerOnHours": brIoPowerOnHours,
       "brIo1Temperature": brIo1Temperature,
       "brIo2Temperature": brIo2Temperature,
       "brIo3Temperature": brIo3Temperature,
       "brIo4Temperature": brIo4Temperature,
       "brIoFpgaVersion": brIoFpgaVersion,
       "brIoFpgaBootMode": brIoFpgaBootMode,
       "brBus": brBus,
       "brBusModelNumber": brBusModelNumber,
       "brBusSerialNumber": brBusSerialNumber,
       "brBusHardwareRevision": brBusHardwareRevision,
       "brBusDeviceId": brBusDeviceId,
       "brBusCompatibilityId": brBusCompatibilityId,
       "brBusFactorySettingsVersion": brBusFactorySettingsVersion,
       "brBusPowerOnCycles": brBusPowerOnCycles,
       "brBusPowerOnHours": brBusPowerOnHours,
       "brBusPresent": brBusPresent,
       "brLink": brLink,
       "brLinkPresent": brLinkPresent,
       "brLinkModelNumber": brLinkModelNumber,
       "brLinkSerialNumber": brLinkSerialNumber,
       "brLinkHardwareRevision": brLinkHardwareRevision,
       "brLinkDeviceId": brLinkDeviceId,
       "brLinkCompatibilityId": brLinkCompatibilityId,
       "brLinkFactorySettingsVersion": brLinkFactorySettingsVersion,
       "brLinkPowerOnCycles": brLinkPowerOnCycles,
       "brLinkPowerOnHours": brLinkPowerOnHours,
       "brLink1Temperature": brLink1Temperature,
       "brLink2Temperature": brLink2Temperature,
       "brLink3Temperature": brLink3Temperature,
       "brLink4Temperature": brLink4Temperature,
       "brLinkFpgaVersion": brLinkFpgaVersion,
       "brLinkFpgaBootMode": brLinkFpgaBootMode,
       "brIf2": brIf2,
       "brIf2Present": brIf2Present,
       "brIf2ModelNumber": brIf2ModelNumber,
       "brIf2SerialNumber": brIf2SerialNumber,
       "brIf2HardwareRevision": brIf2HardwareRevision,
       "brIf2DeviceId": brIf2DeviceId,
       "brIf2CompatibilityId": brIf2CompatibilityId,
       "brIf2FactorySettingsVersion": brIf2FactorySettingsVersion,
       "brIf2PowerOnCycles": brIf2PowerOnCycles,
       "brIf2PowerOnHours": brIf2PowerOnHours,
       "brMem2": brMem2,
       "brMem2ModelNumber": brMem2ModelNumber,
       "brMem2SerialNumber": brMem2SerialNumber,
       "brMem2HardwareRevision": brMem2HardwareRevision,
       "brMem2DeviceId": brMem2DeviceId,
       "brMem2CompatibilityId": brMem2CompatibilityId,
       "brMem2FactorySettingsVersion": brMem2FactorySettingsVersion,
       "brMem2Present": brMem2Present,
       "brFan": brFan,
       "brFanPresent": brFanPresent,
       "brFanModelNumber": brFanModelNumber,
       "brFanSerialNumber": brFanSerialNumber,
       "brFanHardwareRevision": brFanHardwareRevision,
       "brFanDeviceId": brFanDeviceId,
       "brFanCompatibilityId": brFanCompatibilityId,
       "brFanFactorySettingsVersion": brFanFactorySettingsVersion,
       "brFanOnCycles": brFanOnCycles,
       "brFanOnHours": brFanOnHours,
       "brFan1Speed": brFan1Speed,
       "brFan2Speed": brFan2Speed,
       "brFan3Speed": brFan3Speed,
       "brFan4Speed": brFan4Speed,
       "brDrive1": brDrive1,
       "brDrive1Present": brDrive1Present,
       "brDrive1ModelNumber": brDrive1ModelNumber,
       "brDrive1SerialNumber": brDrive1SerialNumber,
       "brDrive1HardwareRevision": brDrive1HardwareRevision,
       "brDrive1DeviceId": brDrive1DeviceId,
       "brDrive1CompatibilityId": brDrive1CompatibilityId,
       "brDrive1FactorySettingsVersion": brDrive1FactorySettingsVersion,
       "brDrive1Temperature": brDrive1Temperature,
       "brDrive2": brDrive2,
       "brDrive2Present": brDrive2Present,
       "brDrive2ModelNumber": brDrive2ModelNumber,
       "brDrive2SerialNumber": brDrive2SerialNumber,
       "brDrive2HardwareRevision": brDrive2HardwareRevision,
       "brDrive2DeviceId": brDrive2DeviceId,
       "brDrive2CompatibilityId": brDrive2CompatibilityId,
       "brDrive2FactorySettingsVersion": brDrive2FactorySettingsVersion,
       "brDrive2Temperature": brDrive2Temperature,
       "brFan2": brFan2,
       "brFan2Present": brFan2Present,
       "brFan2ModelNumber": brFan2ModelNumber,
       "brFan2SerialNumber": brFan2SerialNumber,
       "brFan2HardwareRevision": brFan2HardwareRevision,
       "brFan2DeviceId": brFan2DeviceId,
       "brFan2CompatibilityId": brFan2CompatibilityId,
       "brFan2FactorySettingsVersion": brFan2FactorySettingsVersion,
       "brFan2OnCycles": brFan2OnCycles,
       "brFan2OnHours": brFan2OnHours,
       "brFan21Speed": brFan21Speed,
       "brFan22Speed": brFan22Speed,
       "brFan23Speed": brFan23Speed,
       "brFan24Speed": brFan24Speed,
       "brIf3": brIf3,
       "brIf3Present": brIf3Present,
       "brIf3ModelNumber": brIf3ModelNumber,
       "brIf3SerialNumber": brIf3SerialNumber,
       "brIf3HardwareRevision": brIf3HardwareRevision,
       "brIf3DeviceId": brIf3DeviceId,
       "brIf3CompatibilityId": brIf3CompatibilityId,
       "brIf3FactorySettingsVersion": brIf3FactorySettingsVersion,
       "brIf3PowerOnCycles": brIf3PowerOnCycles,
       "brIf3PowerOnHours": brIf3PowerOnHours,
       "brIf3Temperature1": brIf3Temperature1,
       "brIf3FpgaVersion": brIf3FpgaVersion,
       "brIf3FpgaBootMode": brIf3FpgaBootMode,
       "brAdiConformance": brAdiConformance,
       "brAdiCompliances": brAdiCompliances,
       "brAdiModuleCompliance": brAdiModuleCompliance,
       "brAdiGroups": brAdiGroups,
       "brAdiPcGroup": brAdiPcGroup,
       "brAdiUpsGroup": brAdiUpsGroup,
       "brAdiPanelGroup": brAdiPanelGroup,
       "brAdiCpuGroup": brAdiCpuGroup,
       "brAdiMemGroup": brAdiMemGroup,
       "brAdiIfGroup": brAdiIfGroup,
       "brAdiIoGroup": brAdiIoGroup,
       "brAdiBusGroup": brAdiBusGroup,
       "brAdiLinkGroup": brAdiLinkGroup,
       "brAdiIf2Group": brAdiIf2Group,
       "brAdiMem2Group": brAdiMem2Group,
       "brAdiFanGroup": brAdiFanGroup,
       "brAdiDrive1Group": brAdiDrive1Group,
       "brAdiDrive2Group": brAdiDrive2Group,
       "brAdiFan2Group": brAdiFan2Group,
       "brAdiIf3Group": brAdiIf3Group}
)
