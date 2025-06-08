# SNMP MIB module (MIMOSA-NETWORKS-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/mimosa_43356/MIMOSA-NETWORKS-COMMON-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:32:23 2025
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

(DecimalFive,
 DecimalOne,
 DecimalTwo) = mibBuilder.importSymbols(
    "MIMOSA-MIB-TC",
    "DecimalFive",
    "DecimalOne",
    "DecimalTwo")

(mimosaConformanceGroup,
 mimosaWireless) = mibBuilder.importSymbols(
    "MIMOSA-NETWORKS-BASE-MIB",
    "mimosaConformanceGroup",
    "mimosaWireless")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mimosaCommonModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 3)
)
if mibBuilder.loadTexts:
    mimosaCommonModule.setRevisions(
        ("2017-02-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MimosaGeneral_ObjectIdentity = ObjectIdentity
mimosaGeneral = _MimosaGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1)
)


class _MimosaDeviceName_Type(DisplayString):
    """Custom type mimosaDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MimosaDeviceName_Type.__name__ = "DisplayString"
_MimosaDeviceName_Object = MibScalar
mimosaDeviceName = _MimosaDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 1),
    _MimosaDeviceName_Type()
)
mimosaDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaDeviceName.setStatus("current")


class _MimosaSerialNumber_Type(DisplayString):
    """Custom type mimosaSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MimosaSerialNumber_Type.__name__ = "DisplayString"
_MimosaSerialNumber_Object = MibScalar
mimosaSerialNumber = _MimosaSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 2),
    _MimosaSerialNumber_Type()
)
mimosaSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaSerialNumber.setStatus("current")


class _MimosaFirmwareVersion_Type(DisplayString):
    """Custom type mimosaFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MimosaFirmwareVersion_Type.__name__ = "DisplayString"
_MimosaFirmwareVersion_Object = MibScalar
mimosaFirmwareVersion = _MimosaFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 3),
    _MimosaFirmwareVersion_Type()
)
mimosaFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaFirmwareVersion.setStatus("current")


class _MimosaFirmwareBuildDate_Type(DisplayString):
    """Custom type mimosaFirmwareBuildDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MimosaFirmwareBuildDate_Type.__name__ = "DisplayString"
_MimosaFirmwareBuildDate_Object = MibScalar
mimosaFirmwareBuildDate = _MimosaFirmwareBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 4),
    _MimosaFirmwareBuildDate_Type()
)
mimosaFirmwareBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaFirmwareBuildDate.setStatus("current")


class _MimosaLastRebootTime_Type(DisplayString):
    """Custom type mimosaLastRebootTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MimosaLastRebootTime_Type.__name__ = "DisplayString"
_MimosaLastRebootTime_Object = MibScalar
mimosaLastRebootTime = _MimosaLastRebootTime_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 5),
    _MimosaLastRebootTime_Type()
)
mimosaLastRebootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaLastRebootTime.setStatus("current")


class _MimosaUnlockCode_Type(DisplayString):
    """Custom type mimosaUnlockCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MimosaUnlockCode_Type.__name__ = "DisplayString"
_MimosaUnlockCode_Object = MibScalar
mimosaUnlockCode = _MimosaUnlockCode_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 6),
    _MimosaUnlockCode_Type()
)
mimosaUnlockCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaUnlockCode.setStatus("current")


class _MimosaLEDBrightness_Type(Integer32):
    """Custom type mimosaLEDBrightness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("low", 2),
          ("medium", 3),
          ("high", 4),
          ("off", 5))
    )


_MimosaLEDBrightness_Type.__name__ = "Integer32"
_MimosaLEDBrightness_Object = MibScalar
mimosaLEDBrightness = _MimosaLEDBrightness_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 7),
    _MimosaLEDBrightness_Type()
)
mimosaLEDBrightness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaLEDBrightness.setStatus("current")
_MimosaInternalTemp_Type = Integer32
_MimosaInternalTemp_Object = MibScalar
mimosaInternalTemp = _MimosaInternalTemp_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 8),
    _MimosaInternalTemp_Type()
)
mimosaInternalTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaInternalTemp.setStatus("current")
if mibBuilder.loadTexts:
    mimosaInternalTemp.setUnits("C")


class _MimosaRegulatoryDomain_Type(DisplayString):
    """Custom type mimosaRegulatoryDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MimosaRegulatoryDomain_Type.__name__ = "DisplayString"
_MimosaRegulatoryDomain_Object = MibScalar
mimosaRegulatoryDomain = _MimosaRegulatoryDomain_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 9),
    _MimosaRegulatoryDomain_Type()
)
mimosaRegulatoryDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaRegulatoryDomain.setStatus("current")


class _MimosaRebootReason_Type(DisplayString):
    """Custom type mimosaRebootReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MimosaRebootReason_Type.__name__ = "DisplayString"
_MimosaRebootReason_Object = MibScalar
mimosaRebootReason = _MimosaRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 10),
    _MimosaRebootReason_Type()
)
mimosaRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaRebootReason.setStatus("current")
_MimosaLocInfo_ObjectIdentity = ObjectIdentity
mimosaLocInfo = _MimosaLocInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2)
)
_MimosaLongitude_Type = DecimalFive
_MimosaLongitude_Object = MibScalar
mimosaLongitude = _MimosaLongitude_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 1),
    _MimosaLongitude_Type()
)
mimosaLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaLongitude.setStatus("current")
_MimosaLatitude_Type = DecimalFive
_MimosaLatitude_Object = MibScalar
mimosaLatitude = _MimosaLatitude_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 2),
    _MimosaLatitude_Type()
)
mimosaLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaLatitude.setStatus("current")
_MimosaAltitude_Type = DecimalTwo
_MimosaAltitude_Object = MibScalar
mimosaAltitude = _MimosaAltitude_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 3),
    _MimosaAltitude_Type()
)
mimosaAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaAltitude.setStatus("current")
if mibBuilder.loadTexts:
    mimosaAltitude.setUnits("meters")
_MimosaSatelliteSNR_Type = DecimalOne
_MimosaSatelliteSNR_Object = MibScalar
mimosaSatelliteSNR = _MimosaSatelliteSNR_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 4),
    _MimosaSatelliteSNR_Type()
)
mimosaSatelliteSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaSatelliteSNR.setStatus("current")
if mibBuilder.loadTexts:
    mimosaSatelliteSNR.setUnits("dB")


class _MimosaSatelliteStrength_Type(Integer32):
    """Custom type mimosaSatelliteStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("bad", 2))
    )


_MimosaSatelliteStrength_Type.__name__ = "Integer32"
_MimosaSatelliteStrength_Object = MibScalar
mimosaSatelliteStrength = _MimosaSatelliteStrength_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 5),
    _MimosaSatelliteStrength_Type()
)
mimosaSatelliteStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaSatelliteStrength.setStatus("current")
_MimosaGPSSatellites_Type = Integer32
_MimosaGPSSatellites_Object = MibScalar
mimosaGPSSatellites = _MimosaGPSSatellites_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 6),
    _MimosaGPSSatellites_Type()
)
mimosaGPSSatellites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaGPSSatellites.setStatus("current")
_MimosaGlonassSatellites_Type = Integer32
_MimosaGlonassSatellites_Object = MibScalar
mimosaGlonassSatellites = _MimosaGlonassSatellites_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 7),
    _MimosaGlonassSatellites_Type()
)
mimosaGlonassSatellites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaGlonassSatellites.setStatus("current")
_MimosaClockAccuracy_Type = DecimalTwo
_MimosaClockAccuracy_Object = MibScalar
mimosaClockAccuracy = _MimosaClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 8),
    _MimosaClockAccuracy_Type()
)
mimosaClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaClockAccuracy.setStatus("current")
if mibBuilder.loadTexts:
    mimosaClockAccuracy.setUnits("PPB")
_MimosaCommonConformance_ObjectIdentity = ObjectIdentity
mimosaCommonConformance = _MimosaCommonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 1)
)
_MimosaCommonCompliances_ObjectIdentity = ObjectIdentity
mimosaCommonCompliances = _MimosaCommonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 1, 1)
)
_MimosaCommonGroups_ObjectIdentity = ObjectIdentity
mimosaCommonGroups = _MimosaCommonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 1, 2)
)

# Managed Objects groups

mimosaGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 1, 2, 1)
)
mimosaGeneralGroup.setObjects(
      *(("MIMOSA-NETWORKS-COMMON-MIB", "mimosaDeviceName"),
        ("MIMOSA-NETWORKS-COMMON-MIB", "mimosaSerialNumber"),
        ("MIMOSA-NETWORKS-COMMON-MIB", "mimosaFirmwareVersion"),
        ("MIMOSA-NETWORKS-COMMON-MIB", "mimosaFirmwareBuildDate"),
        ("MIMOSA-NETWORKS-COMMON-MIB", "mimosaLastRebootTime"),
        ("MIMOSA-NETWORKS-COMMON-MIB", "mimosaUnlockCode"),
        ("MIMOSA-NETWORKS-COMMON-MIB", "mimosaLEDBrightness"),
        ("MIMOSA-NETWORKS-COMMON-MIB", "mimosaInternalTemp"),
        ("MIMOSA-NETWORKS-COMMON-MIB", "mimosaRegulatoryDomain"),
        ("MIMOSA-NETWORKS-COMMON-MIB", "mimosaRebootReason"))
)
if mibBuilder.loadTexts:
    mimosaGeneralGroup.setStatus("current")

mimosaLocationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 1, 2, 2)
)
mimosaLocationGroup.setObjects(
      *(("MIMOSA-NETWORKS-COMMON-MIB", "mimosaLongitude"),
        ("MIMOSA-NETWORKS-COMMON-MIB", "mimosaLatitude"),
        ("MIMOSA-NETWORKS-COMMON-MIB", "mimosaAltitude"),
        ("MIMOSA-NETWORKS-COMMON-MIB", "mimosaSatelliteSNR"),
        ("MIMOSA-NETWORKS-COMMON-MIB", "mimosaSatelliteStrength"),
        ("MIMOSA-NETWORKS-COMMON-MIB", "mimosaGPSSatellites"),
        ("MIMOSA-NETWORKS-COMMON-MIB", "mimosaGlonassSatellites"),
        ("MIMOSA-NETWORKS-COMMON-MIB", "mimosaClockAccuracy"))
)
if mibBuilder.loadTexts:
    mimosaLocationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mimosaCommonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 1, 1, 1)
)
mimosaCommonCompliance.setObjects(
      *(("MIMOSA-NETWORKS-COMMON-MIB", "mimosaGeneralGroup"),
        ("MIMOSA-NETWORKS-COMMON-MIB", "mimosaLocationGroup"))
)
if mibBuilder.loadTexts:
    mimosaCommonCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIMOSA-NETWORKS-COMMON-MIB",
    **{"mimosaGeneral": mimosaGeneral,
       "mimosaDeviceName": mimosaDeviceName,
       "mimosaSerialNumber": mimosaSerialNumber,
       "mimosaFirmwareVersion": mimosaFirmwareVersion,
       "mimosaFirmwareBuildDate": mimosaFirmwareBuildDate,
       "mimosaLastRebootTime": mimosaLastRebootTime,
       "mimosaUnlockCode": mimosaUnlockCode,
       "mimosaLEDBrightness": mimosaLEDBrightness,
       "mimosaInternalTemp": mimosaInternalTemp,
       "mimosaRegulatoryDomain": mimosaRegulatoryDomain,
       "mimosaRebootReason": mimosaRebootReason,
       "mimosaLocInfo": mimosaLocInfo,
       "mimosaLongitude": mimosaLongitude,
       "mimosaLatitude": mimosaLatitude,
       "mimosaAltitude": mimosaAltitude,
       "mimosaSatelliteSNR": mimosaSatelliteSNR,
       "mimosaSatelliteStrength": mimosaSatelliteStrength,
       "mimosaGPSSatellites": mimosaGPSSatellites,
       "mimosaGlonassSatellites": mimosaGlonassSatellites,
       "mimosaClockAccuracy": mimosaClockAccuracy,
       "mimosaCommonConformance": mimosaCommonConformance,
       "mimosaCommonCompliances": mimosaCommonCompliances,
       "mimosaCommonCompliance": mimosaCommonCompliance,
       "mimosaCommonGroups": mimosaCommonGroups,
       "mimosaGeneralGroup": mimosaGeneralGroup,
       "mimosaLocationGroup": mimosaLocationGroup,
       "mimosaCommonModule": mimosaCommonModule}
)
