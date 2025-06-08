# SNMP MIB module (TARANA) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/tarana_39660/TARANA.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:04:18 2025
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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

aa2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1)
)
if mibBuilder.loadTexts:
    aa2.setRevisions(
        ("2017-03-15 10:33",
         "2017-03-08 12:00",
         "2016-11-08 10:00",
         "2016-09-06 21:03",
         "2016-08-09 10:00",
         "2016-07-22 12:00",
         "2016-03-26 21:10",
         "2016-01-18 02:37",
         "2015-08-04 14:20")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LinkCode(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 13),
    )



class Decibel(TextualConvention, Integer32):
    status = "current"


class Centibel(TextualConvention, Integer32):
    status = "current"


class Millibel(TextualConvention, Integer32):
    status = "current"


class Percent(TextualConvention, Gauge32):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class Permill(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )



class Microdegree(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Taranawireless_ObjectIdentity = ObjectIdentity
taranawireless = _Taranawireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660)
)
_TwSys_ObjectIdentity = ObjectIdentity
twSys = _TwSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1)
)
_TwSysMibRev_Type = Unsigned32
_TwSysMibRev_Object = MibScalar
twSysMibRev = _TwSysMibRev_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 1),
    _TwSysMibRev_Type()
)
twSysMibRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysMibRev.setStatus("current")


class _TwSysCpuTemperature_Type(Integer32):
    """Custom type twSysCpuTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_TwSysCpuTemperature_Type.__name__ = "Integer32"
_TwSysCpuTemperature_Object = MibScalar
twSysCpuTemperature = _TwSysCpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 2),
    _TwSysCpuTemperature_Type()
)
twSysCpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysCpuTemperature.setStatus("current")
if mibBuilder.loadTexts:
    twSysCpuTemperature.setUnits("C")


class _TwSysRadioTemperature_Type(Integer32):
    """Custom type twSysRadioTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_TwSysRadioTemperature_Type.__name__ = "Integer32"
_TwSysRadioTemperature_Object = MibScalar
twSysRadioTemperature = _TwSysRadioTemperature_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 3),
    _TwSysRadioTemperature_Type()
)
twSysRadioTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysRadioTemperature.setStatus("current")
if mibBuilder.loadTexts:
    twSysRadioTemperature.setUnits("C")
_TwSysCpuUtilization_Type = Permill
_TwSysCpuUtilization_Object = MibScalar
twSysCpuUtilization = _TwSysCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 4),
    _TwSysCpuUtilization_Type()
)
twSysCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysCpuUtilization.setStatus("current")
if mibBuilder.loadTexts:
    twSysCpuUtilization.setUnits("0.1 %")
_TwSysMemoryUtilization_Type = Permill
_TwSysMemoryUtilization_Object = MibScalar
twSysMemoryUtilization = _TwSysMemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 5),
    _TwSysMemoryUtilization_Type()
)
twSysMemoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysMemoryUtilization.setStatus("current")
if mibBuilder.loadTexts:
    twSysMemoryUtilization.setUnits("0.1 %")


class _TwSysBootReason_Type(Integer32):
    """Custom type twSysBootReason based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("coldBoot", 0),
          ("warmReboot", 1),
          ("cpuWatchdog", 2),
          ("smcWatchdog", 3),
          ("factoryPowerOn", 4),
          ("factoryShortPress", 5),
          ("factoryLongPress", 6),
          ("unknown", 7))
    )


_TwSysBootReason_Type.__name__ = "Integer32"
_TwSysBootReason_Object = MibScalar
twSysBootReason = _TwSysBootReason_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 6),
    _TwSysBootReason_Type()
)
twSysBootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysBootReason.setStatus("current")


class _TwSysReboot_Type(Integer32):
    """Custom type twSysReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_TwSysReboot_Type.__name__ = "Integer32"
_TwSysReboot_Object = MibScalar
twSysReboot = _TwSysReboot_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 7),
    _TwSysReboot_Type()
)
twSysReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twSysReboot.setStatus("current")
_TwSysNotes_Type = DisplayString
_TwSysNotes_Object = MibScalar
twSysNotes = _TwSysNotes_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 8),
    _TwSysNotes_Type()
)
twSysNotes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twSysNotes.setStatus("current")
_TwSysInstallationDate_Type = DateAndTime
_TwSysInstallationDate_Object = MibScalar
twSysInstallationDate = _TwSysInstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 9),
    _TwSysInstallationDate_Type()
)
twSysInstallationDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twSysInstallationDate.setStatus("current")
_TwSysComponentVersionTable_Object = MibTable
twSysComponentVersionTable = _TwSysComponentVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 10)
)
if mibBuilder.loadTexts:
    twSysComponentVersionTable.setStatus("current")
_TwSysComponentVersionEntry_Object = MibTableRow
twSysComponentVersionEntry = _TwSysComponentVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 10, 1)
)
twSysComponentVersionEntry.setIndexNames(
    (0, "TARANA", "twSysComponentId"),
)
if mibBuilder.loadTexts:
    twSysComponentVersionEntry.setStatus("current")


class _TwSysComponentId_Type(Unsigned32):
    """Custom type twSysComponentId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TwSysComponentId_Type.__name__ = "Unsigned32"
_TwSysComponentId_Object = MibTableColumn
twSysComponentId = _TwSysComponentId_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 10, 1, 1),
    _TwSysComponentId_Type()
)
twSysComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysComponentId.setStatus("current")
_TwSysComponentVersion_Type = DisplayString
_TwSysComponentVersion_Object = MibTableColumn
twSysComponentVersion = _TwSysComponentVersion_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 10, 1, 2),
    _TwSysComponentVersion_Type()
)
twSysComponentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysComponentVersion.setStatus("current")


class _TwSysClockDateAndTime_Type(DisplayString):
    """Custom type twSysClockDateAndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )
    fixed_length = 24


_TwSysClockDateAndTime_Type.__name__ = "DisplayString"
_TwSysClockDateAndTime_Object = MibScalar
twSysClockDateAndTime = _TwSysClockDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 11),
    _TwSysClockDateAndTime_Type()
)
twSysClockDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysClockDateAndTime.setStatus("current")
_TwSysRegulatory_ObjectIdentity = ObjectIdentity
twSysRegulatory = _TwSysRegulatory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 12)
)


class _TwSysRegulatoryDomain_Type(OctetString):
    """Custom type twSysRegulatoryDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TwSysRegulatoryDomain_Type.__name__ = "OctetString"
_TwSysRegulatoryDomain_Object = MibScalar
twSysRegulatoryDomain = _TwSysRegulatoryDomain_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 12, 1),
    _TwSysRegulatoryDomain_Type()
)
twSysRegulatoryDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twSysRegulatoryDomain.setStatus("current")


class _TwSysRegulatoryDomainCountry_Type(OctetString):
    """Custom type twSysRegulatoryDomainCountry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TwSysRegulatoryDomainCountry_Type.__name__ = "OctetString"
_TwSysRegulatoryDomainCountry_Object = MibScalar
twSysRegulatoryDomainCountry = _TwSysRegulatoryDomainCountry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 12, 2),
    _TwSysRegulatoryDomainCountry_Type()
)
twSysRegulatoryDomainCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twSysRegulatoryDomainCountry.setStatus("current")
_TwSysRegulatoryDomainAvailableTable_Object = MibTable
twSysRegulatoryDomainAvailableTable = _TwSysRegulatoryDomainAvailableTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 12, 3)
)
if mibBuilder.loadTexts:
    twSysRegulatoryDomainAvailableTable.setStatus("current")
_TwSysRegulatoryDomainAvailableEntry_Object = MibTableRow
twSysRegulatoryDomainAvailableEntry = _TwSysRegulatoryDomainAvailableEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 12, 3, 1)
)
twSysRegulatoryDomainAvailableEntry.setIndexNames(
    (0, "TARANA", "twSysRegulatoryDomainId"),
)
if mibBuilder.loadTexts:
    twSysRegulatoryDomainAvailableEntry.setStatus("current")


class _TwSysRegulatoryDomainId_Type(Unsigned32):
    """Custom type twSysRegulatoryDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TwSysRegulatoryDomainId_Type.__name__ = "Unsigned32"
_TwSysRegulatoryDomainId_Object = MibTableColumn
twSysRegulatoryDomainId = _TwSysRegulatoryDomainId_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 12, 3, 1, 1),
    _TwSysRegulatoryDomainId_Type()
)
twSysRegulatoryDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysRegulatoryDomainId.setStatus("current")
_TwSysRegulatoryDomainName_Type = OctetString
_TwSysRegulatoryDomainName_Object = MibTableColumn
twSysRegulatoryDomainName = _TwSysRegulatoryDomainName_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 12, 3, 1, 2),
    _TwSysRegulatoryDomainName_Type()
)
twSysRegulatoryDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysRegulatoryDomainName.setStatus("current")
_TwSysRegulatoryDomainDefaultCountry_Type = OctetString
_TwSysRegulatoryDomainDefaultCountry_Object = MibTableColumn
twSysRegulatoryDomainDefaultCountry = _TwSysRegulatoryDomainDefaultCountry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 12, 3, 1, 3),
    _TwSysRegulatoryDomainDefaultCountry_Type()
)
twSysRegulatoryDomainDefaultCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysRegulatoryDomainDefaultCountry.setStatus("current")
_TwSysRegulatoryDomainCountries_Type = OctetString
_TwSysRegulatoryDomainCountries_Object = MibTableColumn
twSysRegulatoryDomainCountries = _TwSysRegulatoryDomainCountries_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 12, 3, 1, 4),
    _TwSysRegulatoryDomainCountries_Type()
)
twSysRegulatoryDomainCountries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysRegulatoryDomainCountries.setStatus("current")
_TwLic_ObjectIdentity = ObjectIdentity
twLic = _TwLic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13)
)
_TwLicFeatTable_Object = MibTable
twLicFeatTable = _TwLicFeatTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 1)
)
if mibBuilder.loadTexts:
    twLicFeatTable.setStatus("current")
_TwLicFeatEntry_Object = MibTableRow
twLicFeatEntry = _TwLicFeatEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 1, 1)
)
twLicFeatEntry.setIndexNames(
    (0, "TARANA", "twLicFeatIndex"),
)
if mibBuilder.loadTexts:
    twLicFeatEntry.setStatus("current")


class _TwLicFeatIndex_Type(Unsigned32):
    """Custom type twLicFeatIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TwLicFeatIndex_Type.__name__ = "Unsigned32"
_TwLicFeatIndex_Object = MibTableColumn
twLicFeatIndex = _TwLicFeatIndex_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 1, 1, 1),
    _TwLicFeatIndex_Type()
)
twLicFeatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLicFeatIndex.setStatus("current")
_TwLicFeatId_Type = DisplayString
_TwLicFeatId_Object = MibTableColumn
twLicFeatId = _TwLicFeatId_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 1, 1, 2),
    _TwLicFeatId_Type()
)
twLicFeatId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLicFeatId.setStatus("current")
_TwLicFeatName_Type = DisplayString
_TwLicFeatName_Object = MibTableColumn
twLicFeatName = _TwLicFeatName_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 1, 1, 3),
    _TwLicFeatName_Type()
)
twLicFeatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLicFeatName.setStatus("current")


class _TwLicFeatPlat_Type(Integer32):
    """Custom type twLicFeatPlat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("common", 3))
    )


_TwLicFeatPlat_Type.__name__ = "Integer32"
_TwLicFeatPlat_Object = MibTableColumn
twLicFeatPlat = _TwLicFeatPlat_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 1, 1, 4),
    _TwLicFeatPlat_Type()
)
twLicFeatPlat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLicFeatPlat.setStatus("current")


class _TwLicFeatType_Type(Integer32):
    """Custom type twLicFeatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("node", 1),
          ("link", 2))
    )


_TwLicFeatType_Type.__name__ = "Integer32"
_TwLicFeatType_Object = MibTableColumn
twLicFeatType = _TwLicFeatType_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 1, 1, 5),
    _TwLicFeatType_Type()
)
twLicFeatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLicFeatType.setStatus("current")
_TwLicFeatDesc_Type = DisplayString
_TwLicFeatDesc_Object = MibTableColumn
twLicFeatDesc = _TwLicFeatDesc_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 1, 1, 6),
    _TwLicFeatDesc_Type()
)
twLicFeatDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLicFeatDesc.setStatus("current")


class _TwLicFeatActiveLink_Type(Bits):
    """Custom type twLicFeatActiveLink based on Bits"""
    namedValues = NamedValues(
        *(("node", 0),
          ("link1", 1),
          ("link2", 2),
          ("link3", 3),
          ("link4", 4),
          ("link5", 5),
          ("link6", 6))
    )

_TwLicFeatActiveLink_Type.__name__ = "Bits"
_TwLicFeatActiveLink_Object = MibTableColumn
twLicFeatActiveLink = _TwLicFeatActiveLink_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 1, 1, 7),
    _TwLicFeatActiveLink_Type()
)
twLicFeatActiveLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLicFeatActiveLink.setStatus("current")
_TwLicInstTable_Object = MibTable
twLicInstTable = _TwLicInstTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 2)
)
if mibBuilder.loadTexts:
    twLicInstTable.setStatus("current")
_TwLicInstEntry_Object = MibTableRow
twLicInstEntry = _TwLicInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 2, 1)
)
twLicInstEntry.setIndexNames(
    (0, "TARANA", "twLicInstIndex"),
)
if mibBuilder.loadTexts:
    twLicInstEntry.setStatus("current")


class _TwLicInstIndex_Type(Unsigned32):
    """Custom type twLicInstIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TwLicInstIndex_Type.__name__ = "Unsigned32"
_TwLicInstIndex_Object = MibTableColumn
twLicInstIndex = _TwLicInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 2, 1, 1),
    _TwLicInstIndex_Type()
)
twLicInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLicInstIndex.setStatus("current")
_TwLicInstVerMajor_Type = Unsigned32
_TwLicInstVerMajor_Object = MibTableColumn
twLicInstVerMajor = _TwLicInstVerMajor_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 2, 1, 2),
    _TwLicInstVerMajor_Type()
)
twLicInstVerMajor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twLicInstVerMajor.setStatus("current")
_TwLicInstVerMinor_Type = Unsigned32
_TwLicInstVerMinor_Object = MibTableColumn
twLicInstVerMinor = _TwLicInstVerMinor_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 2, 1, 3),
    _TwLicInstVerMinor_Type()
)
twLicInstVerMinor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twLicInstVerMinor.setStatus("current")


class _TwLicInstVerStatus_Type(Integer32):
    """Custom type twLicInstVerStatus based on Integer32"""
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
        *(("verified", 1),
          ("featureFail", 2),
          ("platformFail", 3),
          ("versionFail", 4),
          ("signFail", 5),
          ("otherFail", 6))
    )


_TwLicInstVerStatus_Type.__name__ = "Integer32"
_TwLicInstVerStatus_Object = MibTableColumn
twLicInstVerStatus = _TwLicInstVerStatus_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 2, 1, 4),
    _TwLicInstVerStatus_Type()
)
twLicInstVerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLicInstVerStatus.setStatus("current")
_TwLicInstFeatureId_Type = DisplayString
_TwLicInstFeatureId_Object = MibTableColumn
twLicInstFeatureId = _TwLicInstFeatureId_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 2, 1, 5),
    _TwLicInstFeatureId_Type()
)
twLicInstFeatureId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twLicInstFeatureId.setStatus("current")
_TwLicInstFeatureName_Type = DisplayString
_TwLicInstFeatureName_Object = MibTableColumn
twLicInstFeatureName = _TwLicInstFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 2, 1, 6),
    _TwLicInstFeatureName_Type()
)
twLicInstFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLicInstFeatureName.setStatus("current")


class _TwLicInstActive_Type(Integer32):
    """Custom type twLicInstActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("licenseInactive", 1),
          ("licenseActive", 2),
          ("licenseTesting", 3))
    )


_TwLicInstActive_Type.__name__ = "Integer32"
_TwLicInstActive_Object = MibTableColumn
twLicInstActive = _TwLicInstActive_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 2, 1, 7),
    _TwLicInstActive_Type()
)
twLicInstActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLicInstActive.setStatus("current")
_TwLicInstLinkNum_Type = Integer32
_TwLicInstLinkNum_Object = MibTableColumn
twLicInstLinkNum = _TwLicInstLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 2, 1, 8),
    _TwLicInstLinkNum_Type()
)
twLicInstLinkNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twLicInstLinkNum.setStatus("current")
_TwLicInstKeyText_Type = DisplayString
_TwLicInstKeyText_Object = MibTableColumn
twLicInstKeyText = _TwLicInstKeyText_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 2, 1, 9),
    _TwLicInstKeyText_Type()
)
twLicInstKeyText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twLicInstKeyText.setStatus("current")
_TwLicInstSerial_Type = DisplayString
_TwLicInstSerial_Object = MibTableColumn
twLicInstSerial = _TwLicInstSerial_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 2, 1, 10),
    _TwLicInstSerial_Type()
)
twLicInstSerial.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twLicInstSerial.setStatus("current")
_TwLicInstRowStatus_Type = RowStatus
_TwLicInstRowStatus_Object = MibTableColumn
twLicInstRowStatus = _TwLicInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 1, 13, 2, 1, 11),
    _TwLicInstRowStatus_Type()
)
twLicInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twLicInstRowStatus.setStatus("current")
_TwConf_ObjectIdentity = ObjectIdentity
twConf = _TwConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 2)
)


class _TwConfSave_Type(Integer32):
    """Custom type twConfSave based on Integer32"""
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
        *(("ready", 0),
          ("save", 1),
          ("saved", 2),
          ("error", 3),
          ("unsavedchanges", 4))
    )


_TwConfSave_Type.__name__ = "Integer32"
_TwConfSave_Object = MibScalar
twConfSave = _TwConfSave_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 2, 1),
    _TwConfSave_Type()
)
twConfSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twConfSave.setStatus("current")


class _TwConfExportUrl_Type(OctetString):
    """Custom type twConfExportUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TwConfExportUrl_Type.__name__ = "OctetString"
_TwConfExportUrl_Object = MibScalar
twConfExportUrl = _TwConfExportUrl_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 2, 2),
    _TwConfExportUrl_Type()
)
twConfExportUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twConfExportUrl.setStatus("current")


class _TwConfDownloadUrl_Type(OctetString):
    """Custom type twConfDownloadUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TwConfDownloadUrl_Type.__name__ = "OctetString"
_TwConfDownloadUrl_Object = MibScalar
twConfDownloadUrl = _TwConfDownloadUrl_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 2, 3),
    _TwConfDownloadUrl_Type()
)
twConfDownloadUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twConfDownloadUrl.setStatus("current")


class _TwConfImportDownloadedConfig_Type(Integer32):
    """Custom type twConfImportDownloadedConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inprogress", -2),
          ("error", -1),
          ("success", 0),
          ("apply", 1))
    )


_TwConfImportDownloadedConfig_Type.__name__ = "Integer32"
_TwConfImportDownloadedConfig_Object = MibScalar
twConfImportDownloadedConfig = _TwConfImportDownloadedConfig_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 2, 4),
    _TwConfImportDownloadedConfig_Type()
)
twConfImportDownloadedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twConfImportDownloadedConfig.setStatus("current")


class _TwConfRevertTimeout_Type(Integer32):
    """Custom type twConfRevertTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 600),
    )


_TwConfRevertTimeout_Type.__name__ = "Integer32"
_TwConfRevertTimeout_Object = MibScalar
twConfRevertTimeout = _TwConfRevertTimeout_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 2, 5),
    _TwConfRevertTimeout_Type()
)
twConfRevertTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twConfRevertTimeout.setStatus("current")
if mibBuilder.loadTexts:
    twConfRevertTimeout.setUnits("sec")


class _TwConfVersion_Type(OctetString):
    """Custom type twConfVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TwConfVersion_Type.__name__ = "OctetString"
_TwConfVersion_Object = MibScalar
twConfVersion = _TwConfVersion_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 2, 6),
    _TwConfVersion_Type()
)
twConfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twConfVersion.setStatus("current")


class _TwConfSaveDownloadedConfig_Type(Integer32):
    """Custom type twConfSaveDownloadedConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("save", 1)
    )


_TwConfSaveDownloadedConfig_Type.__name__ = "Integer32"
_TwConfSaveDownloadedConfig_Object = MibScalar
twConfSaveDownloadedConfig = _TwConfSaveDownloadedConfig_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 2, 7),
    _TwConfSaveDownloadedConfig_Type()
)
twConfSaveDownloadedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twConfSaveDownloadedConfig.setStatus("obsolete")
_TwSysImage_ObjectIdentity = ObjectIdentity
twSysImage = _TwSysImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 3)
)


class _TwSysImageBankCurrent_Type(Unsigned32):
    """Custom type twSysImageBankCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TwSysImageBankCurrent_Type.__name__ = "Unsigned32"
_TwSysImageBankCurrent_Object = MibScalar
twSysImageBankCurrent = _TwSysImageBankCurrent_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 3, 1),
    _TwSysImageBankCurrent_Type()
)
twSysImageBankCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysImageBankCurrent.setStatus("current")


class _TwSysImageChangeBank_Type(Unsigned32):
    """Custom type twSysImageChangeBank based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3),
    )


_TwSysImageChangeBank_Type.__name__ = "Unsigned32"
_TwSysImageChangeBank_Object = MibScalar
twSysImageChangeBank = _TwSysImageChangeBank_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 3, 2),
    _TwSysImageChangeBank_Type()
)
twSysImageChangeBank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twSysImageChangeBank.setStatus("current")


class _TwSysImageDownloadStart_Type(OctetString):
    """Custom type twSysImageDownloadStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TwSysImageDownloadStart_Type.__name__ = "OctetString"
_TwSysImageDownloadStart_Object = MibScalar
twSysImageDownloadStart = _TwSysImageDownloadStart_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 3, 3),
    _TwSysImageDownloadStart_Type()
)
twSysImageDownloadStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twSysImageDownloadStart.setStatus("current")


class _TwSysImageDownloadStatus_Type(Integer32):
    """Custom type twSysImageDownloadStatus based on Integer32"""
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
        *(("idle", 0),
          ("success", 1),
          ("inProgress", 2),
          ("failedDownload", 3),
          ("failedVerfication", 4),
          ("failedTimeoutError", 5))
    )


_TwSysImageDownloadStatus_Type.__name__ = "Integer32"
_TwSysImageDownloadStatus_Object = MibScalar
twSysImageDownloadStatus = _TwSysImageDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 3, 4),
    _TwSysImageDownloadStatus_Type()
)
twSysImageDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysImageDownloadStatus.setStatus("current")
_TwSysImageDownloadProgress_Type = Permill
_TwSysImageDownloadProgress_Object = MibScalar
twSysImageDownloadProgress = _TwSysImageDownloadProgress_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 3, 5),
    _TwSysImageDownloadProgress_Type()
)
twSysImageDownloadProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysImageDownloadProgress.setStatus("current")
if mibBuilder.loadTexts:
    twSysImageDownloadProgress.setUnits("0.1 %")


class _TwSysImageDownloadStop_Type(Integer32):
    """Custom type twSysImageDownloadStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("stop", 1)
    )


_TwSysImageDownloadStop_Type.__name__ = "Integer32"
_TwSysImageDownloadStop_Object = MibScalar
twSysImageDownloadStop = _TwSysImageDownloadStop_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 3, 6),
    _TwSysImageDownloadStop_Type()
)
twSysImageDownloadStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twSysImageDownloadStop.setStatus("current")


class _TwSysImageUpgradeStart_Type(Integer32):
    """Custom type twSysImageUpgradeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_TwSysImageUpgradeStart_Type.__name__ = "Integer32"
_TwSysImageUpgradeStart_Object = MibScalar
twSysImageUpgradeStart = _TwSysImageUpgradeStart_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 3, 7),
    _TwSysImageUpgradeStart_Type()
)
twSysImageUpgradeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twSysImageUpgradeStart.setStatus("current")


class _TwSysImageUpgradeStatus_Type(Integer32):
    """Custom type twSysImageUpgradeStatus based on Integer32"""
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
        *(("idle", 0),
          ("success", 1),
          ("inProgress", 2),
          ("failedUpgrade", 3),
          ("failedNoImage", 4),
          ("failedTimeoutError", 5))
    )


_TwSysImageUpgradeStatus_Type.__name__ = "Integer32"
_TwSysImageUpgradeStatus_Object = MibScalar
twSysImageUpgradeStatus = _TwSysImageUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 3, 8),
    _TwSysImageUpgradeStatus_Type()
)
twSysImageUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysImageUpgradeStatus.setStatus("current")
_TwSysImageUpgradeProgress_Type = Permill
_TwSysImageUpgradeProgress_Object = MibScalar
twSysImageUpgradeProgress = _TwSysImageUpgradeProgress_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 3, 9),
    _TwSysImageUpgradeProgress_Type()
)
twSysImageUpgradeProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysImageUpgradeProgress.setStatus("current")
if mibBuilder.loadTexts:
    twSysImageUpgradeProgress.setUnits("0.1 %")


class _TwSysImageUpgradeStop_Type(Integer32):
    """Custom type twSysImageUpgradeStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("stop", 1)
    )


_TwSysImageUpgradeStop_Type.__name__ = "Integer32"
_TwSysImageUpgradeStop_Object = MibScalar
twSysImageUpgradeStop = _TwSysImageUpgradeStop_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 3, 10),
    _TwSysImageUpgradeStop_Type()
)
twSysImageUpgradeStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twSysImageUpgradeStop.setStatus("current")
_TwSysImageBankTable_Object = MibTable
twSysImageBankTable = _TwSysImageBankTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 3, 11)
)
if mibBuilder.loadTexts:
    twSysImageBankTable.setStatus("current")
_TwSysImageBankEntry_Object = MibTableRow
twSysImageBankEntry = _TwSysImageBankEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 3, 11, 1)
)
twSysImageBankEntry.setIndexNames(
    (0, "TARANA", "twSysImageBankId"),
)
if mibBuilder.loadTexts:
    twSysImageBankEntry.setStatus("current")


class _TwSysImageBankId_Type(Unsigned32):
    """Custom type twSysImageBankId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TwSysImageBankId_Type.__name__ = "Unsigned32"
_TwSysImageBankId_Object = MibTableColumn
twSysImageBankId = _TwSysImageBankId_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 3, 11, 1, 1),
    _TwSysImageBankId_Type()
)
twSysImageBankId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysImageBankId.setStatus("current")


class _TwSysImageBankVersion_Type(OctetString):
    """Custom type twSysImageBankVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_TwSysImageBankVersion_Type.__name__ = "OctetString"
_TwSysImageBankVersion_Object = MibTableColumn
twSysImageBankVersion = _TwSysImageBankVersion_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 3, 11, 1, 2),
    _TwSysImageBankVersion_Type()
)
twSysImageBankVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysImageBankVersion.setStatus("current")


class _TwSysImageBankStatus_Type(Integer32):
    """Custom type twSysImageBankStatus based on Integer32"""
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
        *(("factory", 0),
          ("programmed", 1),
          ("unusable", 2),
          ("blank", 3),
          ("error", 4))
    )


_TwSysImageBankStatus_Type.__name__ = "Integer32"
_TwSysImageBankStatus_Object = MibTableColumn
twSysImageBankStatus = _TwSysImageBankStatus_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 3, 11, 1, 3),
    _TwSysImageBankStatus_Type()
)
twSysImageBankStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSysImageBankStatus.setStatus("current")
_TwClocking_ObjectIdentity = ObjectIdentity
twClocking = _TwClocking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 4)
)


class _TwClockingGpsPresent_Type(Integer32):
    """Custom type twClockingGpsPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 0),
          ("present", 1))
    )


_TwClockingGpsPresent_Type.__name__ = "Integer32"
_TwClockingGpsPresent_Object = MibScalar
twClockingGpsPresent = _TwClockingGpsPresent_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 4, 1),
    _TwClockingGpsPresent_Type()
)
twClockingGpsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twClockingGpsPresent.setStatus("current")


class _TwClockingGpsStatus_Type(Integer32):
    """Custom type twClockingGpsStatus based on Integer32"""
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
        *(("unknown", 0),
          ("unlocked", 1),
          ("locked2D", 2),
          ("locked3D", 3))
    )


_TwClockingGpsStatus_Type.__name__ = "Integer32"
_TwClockingGpsStatus_Object = MibScalar
twClockingGpsStatus = _TwClockingGpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 4, 2),
    _TwClockingGpsStatus_Type()
)
twClockingGpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twClockingGpsStatus.setStatus("current")


class _TwClockingLockStatus_Type(Integer32):
    """Custom type twClockingLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freerun", 0),
          ("holdover", 1),
          ("lockedToGps", 2))
    )


_TwClockingLockStatus_Type.__name__ = "Integer32"
_TwClockingLockStatus_Object = MibScalar
twClockingLockStatus = _TwClockingLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 4, 3),
    _TwClockingLockStatus_Type()
)
twClockingLockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twClockingLockStatus.setStatus("current")


class _TwClockingGpsSnr_Type(Centibel):
    """Custom type twClockingGpsSnr based on Centibel"""
    subtypeSpec = Centibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_TwClockingGpsSnr_Type.__name__ = "Centibel"
_TwClockingGpsSnr_Object = MibScalar
twClockingGpsSnr = _TwClockingGpsSnr_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 4, 4),
    _TwClockingGpsSnr_Type()
)
twClockingGpsSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twClockingGpsSnr.setStatus("current")
if mibBuilder.loadTexts:
    twClockingGpsSnr.setUnits("0.1 dB")


class _TwClockingGpsLat_Type(Microdegree):
    """Custom type twClockingGpsLat based on Microdegree"""
    subtypeSpec = Microdegree.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90000000, 90000000),
    )


_TwClockingGpsLat_Type.__name__ = "Microdegree"
_TwClockingGpsLat_Object = MibScalar
twClockingGpsLat = _TwClockingGpsLat_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 4, 5),
    _TwClockingGpsLat_Type()
)
twClockingGpsLat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twClockingGpsLat.setStatus("current")
if mibBuilder.loadTexts:
    twClockingGpsLat.setUnits("micro-degree")


class _TwClockingGpsLon_Type(Microdegree):
    """Custom type twClockingGpsLon based on Microdegree"""
    subtypeSpec = Microdegree.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-180000000, 180000000),
    )


_TwClockingGpsLon_Type.__name__ = "Microdegree"
_TwClockingGpsLon_Object = MibScalar
twClockingGpsLon = _TwClockingGpsLon_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 4, 6),
    _TwClockingGpsLon_Type()
)
twClockingGpsLon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twClockingGpsLon.setStatus("current")
if mibBuilder.loadTexts:
    twClockingGpsLon.setUnits("micro-degrees")


class _TwClockingGpsElevation_Type(Unsigned32):
    """Custom type twClockingGpsElevation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TwClockingGpsElevation_Type.__name__ = "Unsigned32"
_TwClockingGpsElevation_Object = MibScalar
twClockingGpsElevation = _TwClockingGpsElevation_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 4, 7),
    _TwClockingGpsElevation_Type()
)
twClockingGpsElevation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twClockingGpsElevation.setStatus("current")
if mibBuilder.loadTexts:
    twClockingGpsElevation.setUnits("cm")


class _TwClockingGpsNumberOfSatellites_Type(Unsigned32):
    """Custom type twClockingGpsNumberOfSatellites based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TwClockingGpsNumberOfSatellites_Type.__name__ = "Unsigned32"
_TwClockingGpsNumberOfSatellites_Object = MibScalar
twClockingGpsNumberOfSatellites = _TwClockingGpsNumberOfSatellites_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 4, 8),
    _TwClockingGpsNumberOfSatellites_Type()
)
twClockingGpsNumberOfSatellites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twClockingGpsNumberOfSatellites.setStatus("current")
_TwNetwork_ObjectIdentity = ObjectIdentity
twNetwork = _TwNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5)
)


class _TwNetworkProfile_Type(Unsigned32):
    """Custom type twNetworkProfile based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_TwNetworkProfile_Type.__name__ = "Unsigned32"
_TwNetworkProfile_Object = MibScalar
twNetworkProfile = _TwNetworkProfile_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 1),
    _TwNetworkProfile_Type()
)
twNetworkProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twNetworkProfile.setStatus("current")


class _TwNetworkClockSource_Type(Integer32):
    """Custom type twNetworkClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("gps", 0),
          ("freerun", 4),
          ("wired", 5))
    )


_TwNetworkClockSource_Type.__name__ = "Integer32"
_TwNetworkClockSource_Object = MibScalar
twNetworkClockSource = _TwNetworkClockSource_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 2),
    _TwNetworkClockSource_Type()
)
twNetworkClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twNetworkClockSource.setStatus("current")
_TwNetworkMinFreq_Type = Unsigned32
_TwNetworkMinFreq_Object = MibScalar
twNetworkMinFreq = _TwNetworkMinFreq_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 3),
    _TwNetworkMinFreq_Type()
)
twNetworkMinFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNetworkMinFreq.setStatus("current")
if mibBuilder.loadTexts:
    twNetworkMinFreq.setUnits("KHz")
_TwNetworkMaxFreq_Type = Unsigned32
_TwNetworkMaxFreq_Object = MibScalar
twNetworkMaxFreq = _TwNetworkMaxFreq_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 4),
    _TwNetworkMaxFreq_Type()
)
twNetworkMaxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNetworkMaxFreq.setStatus("current")
if mibBuilder.loadTexts:
    twNetworkMaxFreq.setUnits("KHz")
_TwNetworkFrequency_Type = Unsigned32
_TwNetworkFrequency_Object = MibScalar
twNetworkFrequency = _TwNetworkFrequency_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 5),
    _TwNetworkFrequency_Type()
)
twNetworkFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twNetworkFrequency.setStatus("current")
if mibBuilder.loadTexts:
    twNetworkFrequency.setUnits("KHz")
_TwNetworkProfileAvailableTable_Object = MibTable
twNetworkProfileAvailableTable = _TwNetworkProfileAvailableTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 6)
)
if mibBuilder.loadTexts:
    twNetworkProfileAvailableTable.setStatus("current")
_TwNetworkProfileAvailableEntry_Object = MibTableRow
twNetworkProfileAvailableEntry = _TwNetworkProfileAvailableEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 6, 1)
)
twNetworkProfileAvailableEntry.setIndexNames(
    (0, "TARANA", "twNetworkProfileId"),
)
if mibBuilder.loadTexts:
    twNetworkProfileAvailableEntry.setStatus("current")


class _TwNetworkProfileId_Type(Unsigned32):
    """Custom type twNetworkProfileId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_TwNetworkProfileId_Type.__name__ = "Unsigned32"
_TwNetworkProfileId_Object = MibTableColumn
twNetworkProfileId = _TwNetworkProfileId_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 6, 1, 1),
    _TwNetworkProfileId_Type()
)
twNetworkProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNetworkProfileId.setStatus("current")
_TwNetworkProfileDescription_Type = DisplayString
_TwNetworkProfileDescription_Object = MibTableColumn
twNetworkProfileDescription = _TwNetworkProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 6, 1, 2),
    _TwNetworkProfileDescription_Type()
)
twNetworkProfileDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNetworkProfileDescription.setStatus("current")
_TwNetworkProfileDLSymbols_Type = Unsigned32
_TwNetworkProfileDLSymbols_Object = MibTableColumn
twNetworkProfileDLSymbols = _TwNetworkProfileDLSymbols_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 6, 1, 3),
    _TwNetworkProfileDLSymbols_Type()
)
twNetworkProfileDLSymbols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNetworkProfileDLSymbols.setStatus("current")
_TwNetworkProfileULSymbols_Type = Unsigned32
_TwNetworkProfileULSymbols_Object = MibTableColumn
twNetworkProfileULSymbols = _TwNetworkProfileULSymbols_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 6, 1, 4),
    _TwNetworkProfileULSymbols_Type()
)
twNetworkProfileULSymbols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNetworkProfileULSymbols.setStatus("current")


class _TwNetworkProfileFrameTime_Type(Unsigned32):
    """Custom type twNetworkProfileFrameTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TwNetworkProfileFrameTime_Type.__name__ = "Unsigned32"
_TwNetworkProfileFrameTime_Object = MibTableColumn
twNetworkProfileFrameTime = _TwNetworkProfileFrameTime_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 6, 1, 5),
    _TwNetworkProfileFrameTime_Type()
)
twNetworkProfileFrameTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNetworkProfileFrameTime.setStatus("current")
if mibBuilder.loadTexts:
    twNetworkProfileFrameTime.setUnits("usec")


class _TwNetworkProfileCyclicPrefixRatio_Type(Integer32):
    """Custom type twNetworkProfileCyclicPrefixRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              16,
              24,
              32)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("sixteen", 16),
          ("twentyFour", 24),
          ("thirtyTwo", 32))
    )


_TwNetworkProfileCyclicPrefixRatio_Type.__name__ = "Integer32"
_TwNetworkProfileCyclicPrefixRatio_Object = MibTableColumn
twNetworkProfileCyclicPrefixRatio = _TwNetworkProfileCyclicPrefixRatio_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 6, 1, 6),
    _TwNetworkProfileCyclicPrefixRatio_Type()
)
twNetworkProfileCyclicPrefixRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNetworkProfileCyclicPrefixRatio.setStatus("current")


class _TwNetworkProfileMaxDistance_Type(Unsigned32):
    """Custom type twNetworkProfileMaxDistance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TwNetworkProfileMaxDistance_Type.__name__ = "Unsigned32"
_TwNetworkProfileMaxDistance_Object = MibTableColumn
twNetworkProfileMaxDistance = _TwNetworkProfileMaxDistance_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 6, 1, 7),
    _TwNetworkProfileMaxDistance_Type()
)
twNetworkProfileMaxDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNetworkProfileMaxDistance.setStatus("current")
if mibBuilder.loadTexts:
    twNetworkProfileMaxDistance.setUnits("m")
_TwNetworkAcmProfileAvailableTable_Object = MibTable
twNetworkAcmProfileAvailableTable = _TwNetworkAcmProfileAvailableTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 7)
)
if mibBuilder.loadTexts:
    twNetworkAcmProfileAvailableTable.setStatus("current")
_TwNetworkAcmProfileAvailableEntry_Object = MibTableRow
twNetworkAcmProfileAvailableEntry = _TwNetworkAcmProfileAvailableEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 7, 1)
)
twNetworkAcmProfileAvailableEntry.setIndexNames(
    (0, "TARANA", "twNetworkAcmProfileId"),
)
if mibBuilder.loadTexts:
    twNetworkAcmProfileAvailableEntry.setStatus("current")


class _TwNetworkAcmProfileId_Type(Unsigned32):
    """Custom type twNetworkAcmProfileId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_TwNetworkAcmProfileId_Type.__name__ = "Unsigned32"
_TwNetworkAcmProfileId_Object = MibTableColumn
twNetworkAcmProfileId = _TwNetworkAcmProfileId_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 7, 1, 1),
    _TwNetworkAcmProfileId_Type()
)
twNetworkAcmProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNetworkAcmProfileId.setStatus("current")
_TwNetworkAcmProfileDescription_Type = DisplayString
_TwNetworkAcmProfileDescription_Object = MibTableColumn
twNetworkAcmProfileDescription = _TwNetworkAcmProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 7, 1, 2),
    _TwNetworkAcmProfileDescription_Type()
)
twNetworkAcmProfileDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNetworkAcmProfileDescription.setStatus("current")
_TwNetworkChannelBandwidth_Type = Unsigned32
_TwNetworkChannelBandwidth_Object = MibScalar
twNetworkChannelBandwidth = _TwNetworkChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 8),
    _TwNetworkChannelBandwidth_Type()
)
twNetworkChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNetworkChannelBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    twNetworkChannelBandwidth.setUnits("MHz")


class _TwNetworkCodeOperatorId_Type(Unsigned32):
    """Custom type twNetworkCodeOperatorId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TwNetworkCodeOperatorId_Type.__name__ = "Unsigned32"
_TwNetworkCodeOperatorId_Object = MibScalar
twNetworkCodeOperatorId = _TwNetworkCodeOperatorId_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 9),
    _TwNetworkCodeOperatorId_Type()
)
twNetworkCodeOperatorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twNetworkCodeOperatorId.setStatus("current")


class _TwNetworkCodeAreaId_Type(Unsigned32):
    """Custom type twNetworkCodeAreaId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TwNetworkCodeAreaId_Type.__name__ = "Unsigned32"
_TwNetworkCodeAreaId_Object = MibScalar
twNetworkCodeAreaId = _TwNetworkCodeAreaId_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 10),
    _TwNetworkCodeAreaId_Type()
)
twNetworkCodeAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twNetworkCodeAreaId.setStatus("current")


class _TwNetworkCodeGroupId_Type(Unsigned32):
    """Custom type twNetworkCodeGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TwNetworkCodeGroupId_Type.__name__ = "Unsigned32"
_TwNetworkCodeGroupId_Object = MibScalar
twNetworkCodeGroupId = _TwNetworkCodeGroupId_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 11),
    _TwNetworkCodeGroupId_Type()
)
twNetworkCodeGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twNetworkCodeGroupId.setStatus("current")


class _TwNetworkCodeSetId_Type(Unsigned32):
    """Custom type twNetworkCodeSetId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TwNetworkCodeSetId_Type.__name__ = "Unsigned32"
_TwNetworkCodeSetId_Object = MibScalar
twNetworkCodeSetId = _TwNetworkCodeSetId_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 5, 12),
    _TwNetworkCodeSetId_Type()
)
twNetworkCodeSetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twNetworkCodeSetId.setStatus("current")
_TwSector_ObjectIdentity = ObjectIdentity
twSector = _TwSector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 7)
)


class _TwSectorNumLinks_Type(Unsigned32):
    """Custom type twSectorNumLinks based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TwSectorNumLinks_Type.__name__ = "Unsigned32"
_TwSectorNumLinks_Object = MibScalar
twSectorNumLinks = _TwSectorNumLinks_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 7, 1),
    _TwSectorNumLinks_Type()
)
twSectorNumLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSectorNumLinks.setStatus("current")


class _TwSectorBwMap_Type(Unsigned32):
    """Custom type twSectorBwMap based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TwSectorBwMap_Type.__name__ = "Unsigned32"
_TwSectorBwMap_Object = MibScalar
twSectorBwMap = _TwSectorBwMap_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 7, 2),
    _TwSectorBwMap_Type()
)
twSectorBwMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twSectorBwMap.setStatus("current")
_TwSectorBwMapProfileAvailableTable_Object = MibTable
twSectorBwMapProfileAvailableTable = _TwSectorBwMapProfileAvailableTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 7, 3)
)
if mibBuilder.loadTexts:
    twSectorBwMapProfileAvailableTable.setStatus("current")
_TwSectorBwMapProfileAvailableEntry_Object = MibTableRow
twSectorBwMapProfileAvailableEntry = _TwSectorBwMapProfileAvailableEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 7, 3, 1)
)
twSectorBwMapProfileAvailableEntry.setIndexNames(
    (0, "TARANA", "twSectorBwMapProfileId"),
)
if mibBuilder.loadTexts:
    twSectorBwMapProfileAvailableEntry.setStatus("current")


class _TwSectorBwMapProfileId_Type(Unsigned32):
    """Custom type twSectorBwMapProfileId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TwSectorBwMapProfileId_Type.__name__ = "Unsigned32"
_TwSectorBwMapProfileId_Object = MibTableColumn
twSectorBwMapProfileId = _TwSectorBwMapProfileId_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 7, 3, 1, 1),
    _TwSectorBwMapProfileId_Type()
)
twSectorBwMapProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSectorBwMapProfileId.setStatus("current")
_TwSectorBwMapProfileDescription_Type = DisplayString
_TwSectorBwMapProfileDescription_Object = MibTableColumn
twSectorBwMapProfileDescription = _TwSectorBwMapProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 7, 3, 1, 2),
    _TwSectorBwMapProfileDescription_Type()
)
twSectorBwMapProfileDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twSectorBwMapProfileDescription.setStatus("current")
_TwNode_ObjectIdentity = ObjectIdentity
twNode = _TwNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8)
)


class _TwNodeMode_Type(Integer32):
    """Custom type twNodeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1))
    )


_TwNodeMode_Type.__name__ = "Integer32"
_TwNodeMode_Object = MibScalar
twNodeMode = _TwNodeMode_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 1),
    _TwNodeMode_Type()
)
twNodeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twNodeMode.setStatus("current")
_TwNodeLinkCode_Type = LinkCode
_TwNodeLinkCode_Object = MibScalar
twNodeLinkCode = _TwNodeLinkCode_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 2),
    _TwNodeLinkCode_Type()
)
twNodeLinkCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twNodeLinkCode.setStatus("current")


class _TwNodeTxOpmode_Type(Integer32):
    """Custom type twNodeTxOpmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_TwNodeTxOpmode_Type.__name__ = "Integer32"
_TwNodeTxOpmode_Object = MibScalar
twNodeTxOpmode = _TwNodeTxOpmode_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 3),
    _TwNodeTxOpmode_Type()
)
twNodeTxOpmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twNodeTxOpmode.setStatus("current")


class _TwNodeTxMaxRegulatoryPower_Type(Centibel):
    """Custom type twNodeTxMaxRegulatoryPower based on Centibel"""
    subtypeSpec = Centibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TwNodeTxMaxRegulatoryPower_Type.__name__ = "Centibel"
_TwNodeTxMaxRegulatoryPower_Object = MibScalar
twNodeTxMaxRegulatoryPower = _TwNodeTxMaxRegulatoryPower_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 4),
    _TwNodeTxMaxRegulatoryPower_Type()
)
twNodeTxMaxRegulatoryPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNodeTxMaxRegulatoryPower.setStatus("current")
if mibBuilder.loadTexts:
    twNodeTxMaxRegulatoryPower.setUnits("0.1 dBm")


class _TwNodeTxMaxPermittedPower_Type(Centibel):
    """Custom type twNodeTxMaxPermittedPower based on Centibel"""
    subtypeSpec = Centibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TwNodeTxMaxPermittedPower_Type.__name__ = "Centibel"
_TwNodeTxMaxPermittedPower_Object = MibScalar
twNodeTxMaxPermittedPower = _TwNodeTxMaxPermittedPower_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 5),
    _TwNodeTxMaxPermittedPower_Type()
)
twNodeTxMaxPermittedPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twNodeTxMaxPermittedPower.setStatus("current")
if mibBuilder.loadTexts:
    twNodeTxMaxPermittedPower.setUnits("0.1 dBm")


class _TwNodeTxTotalPower_Type(Centibel):
    """Custom type twNodeTxTotalPower based on Centibel"""
    subtypeSpec = Centibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 500),
    )


_TwNodeTxTotalPower_Type.__name__ = "Centibel"
_TwNodeTxTotalPower_Object = MibScalar
twNodeTxTotalPower = _TwNodeTxTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 6),
    _TwNodeTxTotalPower_Type()
)
twNodeTxTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNodeTxTotalPower.setStatus("current")
if mibBuilder.loadTexts:
    twNodeTxTotalPower.setUnits("0.1 dBm")
_TwNodeRssi_Type = Centibel
_TwNodeRssi_Object = MibScalar
twNodeRssi = _TwNodeRssi_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 7),
    _TwNodeRssi_Type()
)
twNodeRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNodeRssi.setStatus("current")
if mibBuilder.loadTexts:
    twNodeRssi.setUnits("0.1 dBm")


class _TwNodeTxAttenuation_Type(Centibel):
    """Custom type twNodeTxAttenuation based on Centibel"""
    subtypeSpec = Centibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 600),
    )


_TwNodeTxAttenuation_Type.__name__ = "Centibel"
_TwNodeTxAttenuation_Object = MibScalar
twNodeTxAttenuation = _TwNodeTxAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 8),
    _TwNodeTxAttenuation_Type()
)
twNodeTxAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNodeTxAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    twNodeTxAttenuation.setUnits("0.1 dB")


class _TwNodeRxGain_Type(Centibel):
    """Custom type twNodeRxGain based on Centibel"""
    subtypeSpec = Centibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 900),
    )


_TwNodeRxGain_Type.__name__ = "Centibel"
_TwNodeRxGain_Object = MibScalar
twNodeRxGain = _TwNodeRxGain_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 9),
    _TwNodeRxGain_Type()
)
twNodeRxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNodeRxGain.setStatus("current")
if mibBuilder.loadTexts:
    twNodeRxGain.setUnits("0.1 dB")


class _TwNodeTxHeadroom_Type(Centibel):
    """Custom type twNodeTxHeadroom based on Centibel"""
    subtypeSpec = Centibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 500),
    )


_TwNodeTxHeadroom_Type.__name__ = "Centibel"
_TwNodeTxHeadroom_Object = MibScalar
twNodeTxHeadroom = _TwNodeTxHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 10),
    _TwNodeTxHeadroom_Type()
)
twNodeTxHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNodeTxHeadroom.setStatus("current")
if mibBuilder.loadTexts:
    twNodeTxHeadroom.setUnits("0.1 dB")


class _TwNodeAntInactive_Type(Unsigned32):
    """Custom type twNodeAntInactive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_TwNodeAntInactive_Type.__name__ = "Unsigned32"
_TwNodeAntInactive_Object = MibScalar
twNodeAntInactive = _TwNodeAntInactive_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 11),
    _TwNodeAntInactive_Type()
)
twNodeAntInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNodeAntInactive.setStatus("current")


class _TwNodeAntStatus_Type(Integer32):
    """Custom type twNodeAntStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("impaired", 0),
          ("degraded", 1),
          ("operational", 2))
    )


_TwNodeAntStatus_Type.__name__ = "Integer32"
_TwNodeAntStatus_Object = MibScalar
twNodeAntStatus = _TwNodeAntStatus_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 12),
    _TwNodeAntStatus_Type()
)
twNodeAntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNodeAntStatus.setStatus("current")


class _TwNodeTxMinPermittedPower_Type(Centibel):
    """Custom type twNodeTxMinPermittedPower based on Centibel"""
    subtypeSpec = Centibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TwNodeTxMinPermittedPower_Type.__name__ = "Centibel"
_TwNodeTxMinPermittedPower_Object = MibScalar
twNodeTxMinPermittedPower = _TwNodeTxMinPermittedPower_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 13),
    _TwNodeTxMinPermittedPower_Type()
)
twNodeTxMinPermittedPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twNodeTxMinPermittedPower.setStatus("current")
if mibBuilder.loadTexts:
    twNodeTxMinPermittedPower.setUnits("0.1 dBm")
_TwNodeFrequencyTable_Object = MibTable
twNodeFrequencyTable = _TwNodeFrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 14)
)
if mibBuilder.loadTexts:
    twNodeFrequencyTable.setStatus("current")
_TwNodeFrequencyEntry_Object = MibTableRow
twNodeFrequencyEntry = _TwNodeFrequencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 14, 1)
)
twNodeFrequencyEntry.setIndexNames(
    (0, "TARANA", "twNodeFrequencyChannelNum"),
)
if mibBuilder.loadTexts:
    twNodeFrequencyEntry.setStatus("current")


class _TwNodeFrequencyChannelNum_Type(Unsigned32):
    """Custom type twNodeFrequencyChannelNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TwNodeFrequencyChannelNum_Type.__name__ = "Unsigned32"
_TwNodeFrequencyChannelNum_Object = MibTableColumn
twNodeFrequencyChannelNum = _TwNodeFrequencyChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 14, 1, 1),
    _TwNodeFrequencyChannelNum_Type()
)
twNodeFrequencyChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNodeFrequencyChannelNum.setStatus("current")
_TwNodeFrequencyValue_Type = Unsigned32
_TwNodeFrequencyValue_Object = MibTableColumn
twNodeFrequencyValue = _TwNodeFrequencyValue_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 14, 1, 2),
    _TwNodeFrequencyValue_Type()
)
twNodeFrequencyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNodeFrequencyValue.setStatus("current")
if mibBuilder.loadTexts:
    twNodeFrequencyValue.setUnits("kHz")
_TwNodeFrequencyChannelStatus_Type = DisplayString
_TwNodeFrequencyChannelStatus_Object = MibTableColumn
twNodeFrequencyChannelStatus = _TwNodeFrequencyChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 14, 1, 3),
    _TwNodeFrequencyChannelStatus_Type()
)
twNodeFrequencyChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNodeFrequencyChannelStatus.setStatus("current")
_TwNodeDxs_ObjectIdentity = ObjectIdentity
twNodeDxs = _TwNodeDxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 15)
)


class _TwNodeDcsChannelChangeReason_Type(Integer32):
    """Custom type twNodeDcsChannelChangeReason based on Integer32"""
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
        *(("none", 0),
          ("usrCmd", 1),
          ("noLink", 2),
          ("dfsRadar", 3),
          ("dcsMcsLow", 4))
    )


_TwNodeDcsChannelChangeReason_Type.__name__ = "Integer32"
_TwNodeDcsChannelChangeReason_Object = MibScalar
twNodeDcsChannelChangeReason = _TwNodeDcsChannelChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 15, 1),
    _TwNodeDcsChannelChangeReason_Type()
)
twNodeDcsChannelChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNodeDcsChannelChangeReason.setStatus("current")


class _TwNodeDfsStatus_Type(Integer32):
    """Custom type twNodeDfsStatus based on Integer32"""
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
        *(("noDfsReqd", 0),
          ("unknown", 1),
          ("cacInProgress", 2),
          ("cacComplete", 3),
          ("radar", 4))
    )


_TwNodeDfsStatus_Type.__name__ = "Integer32"
_TwNodeDfsStatus_Object = MibScalar
twNodeDfsStatus = _TwNodeDfsStatus_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 15, 2),
    _TwNodeDfsStatus_Type()
)
twNodeDfsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNodeDfsStatus.setStatus("current")


class _TwNodeDcsMode_Type(Integer32):
    """Custom type twNodeDcsMode based on Integer32"""
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
        *(("off", 0),
          ("on", 1),
          ("debugA", 2),
          ("debugB", 3))
    )


_TwNodeDcsMode_Type.__name__ = "Integer32"
_TwNodeDcsMode_Object = MibScalar
twNodeDcsMode = _TwNodeDcsMode_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 15, 3),
    _TwNodeDcsMode_Type()
)
twNodeDcsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twNodeDcsMode.setStatus("current")
_TwNodeDcsChannelChangeTime_Type = Unsigned32
_TwNodeDcsChannelChangeTime_Object = MibScalar
twNodeDcsChannelChangeTime = _TwNodeDcsChannelChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 15, 4),
    _TwNodeDcsChannelChangeTime_Type()
)
twNodeDcsChannelChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNodeDcsChannelChangeTime.setStatus("current")
if mibBuilder.loadTexts:
    twNodeDcsChannelChangeTime.setUnits("sec")
_TwNodeDcsChannelChangeCount_Type = Unsigned32
_TwNodeDcsChannelChangeCount_Object = MibScalar
twNodeDcsChannelChangeCount = _TwNodeDcsChannelChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 15, 5),
    _TwNodeDcsChannelChangeCount_Type()
)
twNodeDcsChannelChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNodeDcsChannelChangeCount.setStatus("current")
_TwNodeDfsChannelChangeTime_Type = Unsigned32
_TwNodeDfsChannelChangeTime_Object = MibScalar
twNodeDfsChannelChangeTime = _TwNodeDfsChannelChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 15, 6),
    _TwNodeDfsChannelChangeTime_Type()
)
twNodeDfsChannelChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNodeDfsChannelChangeTime.setStatus("current")
if mibBuilder.loadTexts:
    twNodeDfsChannelChangeTime.setUnits("sec")
_TwNodeDfsChannelChangeCount_Type = Unsigned32
_TwNodeDfsChannelChangeCount_Object = MibScalar
twNodeDfsChannelChangeCount = _TwNodeDfsChannelChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 15, 7),
    _TwNodeDfsChannelChangeCount_Type()
)
twNodeDfsChannelChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNodeDfsChannelChangeCount.setStatus("current")
_TwNodeBlacklistTable_Object = MibTable
twNodeBlacklistTable = _TwNodeBlacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 16)
)
if mibBuilder.loadTexts:
    twNodeBlacklistTable.setStatus("current")
_TwNodeBlacklistEntry_Object = MibTableRow
twNodeBlacklistEntry = _TwNodeBlacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 16, 1)
)
twNodeBlacklistEntry.setIndexNames(
    (0, "TARANA", "twNodeBlacklistIndex"),
)
if mibBuilder.loadTexts:
    twNodeBlacklistEntry.setStatus("current")


class _TwNodeBlacklistIndex_Type(Unsigned32):
    """Custom type twNodeBlacklistIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TwNodeBlacklistIndex_Type.__name__ = "Unsigned32"
_TwNodeBlacklistIndex_Object = MibTableColumn
twNodeBlacklistIndex = _TwNodeBlacklistIndex_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 16, 1, 1),
    _TwNodeBlacklistIndex_Type()
)
twNodeBlacklistIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twNodeBlacklistIndex.setStatus("current")
_TwNodeBlacklistFreqStartKHz_Type = Unsigned32
_TwNodeBlacklistFreqStartKHz_Object = MibTableColumn
twNodeBlacklistFreqStartKHz = _TwNodeBlacklistFreqStartKHz_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 16, 1, 2),
    _TwNodeBlacklistFreqStartKHz_Type()
)
twNodeBlacklistFreqStartKHz.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twNodeBlacklistFreqStartKHz.setStatus("current")
_TwNodeBlacklistFreqEndKHz_Type = Unsigned32
_TwNodeBlacklistFreqEndKHz_Object = MibTableColumn
twNodeBlacklistFreqEndKHz = _TwNodeBlacklistFreqEndKHz_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 16, 1, 3),
    _TwNodeBlacklistFreqEndKHz_Type()
)
twNodeBlacklistFreqEndKHz.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twNodeBlacklistFreqEndKHz.setStatus("current")
_TwNodeBlacklistRowStatus_Type = RowStatus
_TwNodeBlacklistRowStatus_Object = MibTableColumn
twNodeBlacklistRowStatus = _TwNodeBlacklistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 8, 16, 1, 4),
    _TwNodeBlacklistRowStatus_Type()
)
twNodeBlacklistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twNodeBlacklistRowStatus.setStatus("current")
_TwLink_ObjectIdentity = ObjectIdentity
twLink = _TwLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9)
)
_TwLinkConfigTable_Object = MibTable
twLinkConfigTable = _TwLinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 1)
)
if mibBuilder.loadTexts:
    twLinkConfigTable.setStatus("current")
_TwLinkConfigEntry_Object = MibTableRow
twLinkConfigEntry = _TwLinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 1, 1)
)
twLinkConfigEntry.setIndexNames(
    (0, "TARANA", "twLinkInterfaceId"),
)
if mibBuilder.loadTexts:
    twLinkConfigEntry.setStatus("current")


class _TwLinkInterfaceId_Type(Unsigned32):
    """Custom type twLinkInterfaceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_TwLinkInterfaceId_Type.__name__ = "Unsigned32"
_TwLinkInterfaceId_Object = MibTableColumn
twLinkInterfaceId = _TwLinkInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 1, 1, 1),
    _TwLinkInterfaceId_Type()
)
twLinkInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkInterfaceId.setStatus("current")


class _TwLinkNumber_Type(Unsigned32):
    """Custom type twLinkNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TwLinkNumber_Type.__name__ = "Unsigned32"
_TwLinkNumber_Object = MibTableColumn
twLinkNumber = _TwLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 1, 1, 2),
    _TwLinkNumber_Type()
)
twLinkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twLinkNumber.setStatus("current")


class _TwLinkAcmEnable_Type(Integer32):
    """Custom type twLinkAcmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_TwLinkAcmEnable_Type.__name__ = "Integer32"
_TwLinkAcmEnable_Object = MibTableColumn
twLinkAcmEnable = _TwLinkAcmEnable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 1, 1, 4),
    _TwLinkAcmEnable_Type()
)
twLinkAcmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twLinkAcmEnable.setStatus("current")


class _TwLinkAcmProfile_Type(Unsigned32):
    """Custom type twLinkAcmProfile based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_TwLinkAcmProfile_Type.__name__ = "Unsigned32"
_TwLinkAcmProfile_Object = MibTableColumn
twLinkAcmProfile = _TwLinkAcmProfile_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 1, 1, 5),
    _TwLinkAcmProfile_Type()
)
twLinkAcmProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twLinkAcmProfile.setStatus("current")


class _TwLinkMcsMin_Type(Unsigned32):
    """Custom type twLinkMcsMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_TwLinkMcsMin_Type.__name__ = "Unsigned32"
_TwLinkMcsMin_Object = MibTableColumn
twLinkMcsMin = _TwLinkMcsMin_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 1, 1, 6),
    _TwLinkMcsMin_Type()
)
twLinkMcsMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twLinkMcsMin.setStatus("current")


class _TwLinkMcsMax_Type(Unsigned32):
    """Custom type twLinkMcsMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_TwLinkMcsMax_Type.__name__ = "Unsigned32"
_TwLinkMcsMax_Object = MibTableColumn
twLinkMcsMax = _TwLinkMcsMax_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 1, 1, 7),
    _TwLinkMcsMax_Type()
)
twLinkMcsMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twLinkMcsMax.setStatus("current")


class _TwLinkMcsFixed_Type(Unsigned32):
    """Custom type twLinkMcsFixed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_TwLinkMcsFixed_Type.__name__ = "Unsigned32"
_TwLinkMcsFixed_Object = MibTableColumn
twLinkMcsFixed = _TwLinkMcsFixed_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 1, 1, 8),
    _TwLinkMcsFixed_Type()
)
twLinkMcsFixed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twLinkMcsFixed.setStatus("current")


class _TwLinkResetCounters_Type(Integer32):
    """Custom type twLinkResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("resetCounters", 1))
    )


_TwLinkResetCounters_Type.__name__ = "Integer32"
_TwLinkResetCounters_Object = MibTableColumn
twLinkResetCounters = _TwLinkResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 1, 1, 9),
    _TwLinkResetCounters_Type()
)
twLinkResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twLinkResetCounters.setStatus("current")


class _TwLinkAdaptiveMarginEnable_Type(Integer32):
    """Custom type twLinkAdaptiveMarginEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_TwLinkAdaptiveMarginEnable_Type.__name__ = "Integer32"
_TwLinkAdaptiveMarginEnable_Object = MibTableColumn
twLinkAdaptiveMarginEnable = _TwLinkAdaptiveMarginEnable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 1, 1, 10),
    _TwLinkAdaptiveMarginEnable_Type()
)
twLinkAdaptiveMarginEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twLinkAdaptiveMarginEnable.setStatus("current")
_TwLinkAcmMargin_Type = Centibel
_TwLinkAcmMargin_Object = MibTableColumn
twLinkAcmMargin = _TwLinkAcmMargin_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 1, 1, 11),
    _TwLinkAcmMargin_Type()
)
twLinkAcmMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twLinkAcmMargin.setStatus("current")
if mibBuilder.loadTexts:
    twLinkAcmMargin.setUnits("0.1 dB")


class _TwLinkArqEnable_Type(Integer32):
    """Custom type twLinkArqEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_TwLinkArqEnable_Type.__name__ = "Integer32"
_TwLinkArqEnable_Object = MibTableColumn
twLinkArqEnable = _TwLinkArqEnable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 1, 1, 12),
    _TwLinkArqEnable_Type()
)
twLinkArqEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twLinkArqEnable.setStatus("current")


class _TwLinkAbicEnable_Type(Integer32):
    """Custom type twLinkAbicEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_TwLinkAbicEnable_Type.__name__ = "Integer32"
_TwLinkAbicEnable_Object = MibTableColumn
twLinkAbicEnable = _TwLinkAbicEnable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 1, 1, 13),
    _TwLinkAbicEnable_Type()
)
twLinkAbicEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twLinkAbicEnable.setStatus("current")
_TwLinkPhyStatsTable_Object = MibTable
twLinkPhyStatsTable = _TwLinkPhyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 2)
)
if mibBuilder.loadTexts:
    twLinkPhyStatsTable.setStatus("current")
_TwLinkPhyStatsEntry_Object = MibTableRow
twLinkPhyStatsEntry = _TwLinkPhyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 2, 1)
)
twLinkPhyStatsEntry.setIndexNames(
    (0, "TARANA", "twLinkInterfaceId"),
)
if mibBuilder.loadTexts:
    twLinkPhyStatsEntry.setStatus("current")


class _TwLinkPhyState_Type(Integer32):
    """Custom type twLinkPhyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
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
        *(("invalid", -1),
          ("init", 0),
          ("align", 1),
          ("acq", 2),
          ("refine", 3),
          ("sync", 4),
          ("cal", 5),
          ("range", 6),
          ("pwrlow", 7),
          ("pwrhigh", 8),
          ("track", 9),
          ("exit", 10))
    )


_TwLinkPhyState_Type.__name__ = "Integer32"
_TwLinkPhyState_Object = MibTableColumn
twLinkPhyState = _TwLinkPhyState_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 2, 1, 1),
    _TwLinkPhyState_Type()
)
twLinkPhyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkPhyState.setStatus("current")
_TwLinkPhyUpTime_Type = Counter32
_TwLinkPhyUpTime_Object = MibTableColumn
twLinkPhyUpTime = _TwLinkPhyUpTime_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 2, 1, 2),
    _TwLinkPhyUpTime_Type()
)
twLinkPhyUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkPhyUpTime.setStatus("current")
if mibBuilder.loadTexts:
    twLinkPhyUpTime.setUnits("sec")


class _TwLinkPhyPathRange_Type(Unsigned32):
    """Custom type twLinkPhyPathRange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TwLinkPhyPathRange_Type.__name__ = "Unsigned32"
_TwLinkPhyPathRange_Object = MibTableColumn
twLinkPhyPathRange = _TwLinkPhyPathRange_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 2, 1, 3),
    _TwLinkPhyPathRange_Type()
)
twLinkPhyPathRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkPhyPathRange.setStatus("current")
if mibBuilder.loadTexts:
    twLinkPhyPathRange.setUnits("m")


class _TwLinkPhyPathLoss_Type(Centibel):
    """Custom type twLinkPhyPathLoss based on Centibel"""
    subtypeSpec = Centibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-990, 2000),
    )


_TwLinkPhyPathLoss_Type.__name__ = "Centibel"
_TwLinkPhyPathLoss_Object = MibTableColumn
twLinkPhyPathLoss = _TwLinkPhyPathLoss_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 2, 1, 4),
    _TwLinkPhyPathLoss_Type()
)
twLinkPhyPathLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkPhyPathLoss.setStatus("current")
if mibBuilder.loadTexts:
    twLinkPhyPathLoss.setUnits("0.1 dB")


class _TwLinkPhySinr_Type(Centibel):
    """Custom type twLinkPhySinr based on Centibel"""
    subtypeSpec = Centibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 1000),
    )


_TwLinkPhySinr_Type.__name__ = "Centibel"
_TwLinkPhySinr_Object = MibTableColumn
twLinkPhySinr = _TwLinkPhySinr_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 2, 1, 5),
    _TwLinkPhySinr_Type()
)
twLinkPhySinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkPhySinr.setStatus("current")
if mibBuilder.loadTexts:
    twLinkPhySinr.setUnits("0.1 dB")


class _TwLinkPhyTxMcs_Type(Unsigned32):
    """Custom type twLinkPhyTxMcs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_TwLinkPhyTxMcs_Type.__name__ = "Unsigned32"
_TwLinkPhyTxMcs_Object = MibTableColumn
twLinkPhyTxMcs = _TwLinkPhyTxMcs_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 2, 1, 6),
    _TwLinkPhyTxMcs_Type()
)
twLinkPhyTxMcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkPhyTxMcs.setStatus("current")


class _TwLinkPhyRxMcs_Type(Unsigned32):
    """Custom type twLinkPhyRxMcs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_TwLinkPhyRxMcs_Type.__name__ = "Unsigned32"
_TwLinkPhyRxMcs_Object = MibTableColumn
twLinkPhyRxMcs = _TwLinkPhyRxMcs_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 2, 1, 7),
    _TwLinkPhyRxMcs_Type()
)
twLinkPhyRxMcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkPhyRxMcs.setStatus("current")
_TwLinkPhyInterferenceDutyCycle_Type = Permill
_TwLinkPhyInterferenceDutyCycle_Object = MibTableColumn
twLinkPhyInterferenceDutyCycle = _TwLinkPhyInterferenceDutyCycle_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 2, 1, 8),
    _TwLinkPhyInterferenceDutyCycle_Type()
)
twLinkPhyInterferenceDutyCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkPhyInterferenceDutyCycle.setStatus("current")
if mibBuilder.loadTexts:
    twLinkPhyInterferenceDutyCycle.setUnits("0.1 %")


class _TwLinkPhyInterferenceSignalRatio_Type(Centibel):
    """Custom type twLinkPhyInterferenceSignalRatio based on Centibel"""
    subtypeSpec = Centibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-990, 2000),
    )


_TwLinkPhyInterferenceSignalRatio_Type.__name__ = "Centibel"
_TwLinkPhyInterferenceSignalRatio_Object = MibTableColumn
twLinkPhyInterferenceSignalRatio = _TwLinkPhyInterferenceSignalRatio_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 2, 1, 9),
    _TwLinkPhyInterferenceSignalRatio_Type()
)
twLinkPhyInterferenceSignalRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkPhyInterferenceSignalRatio.setStatus("current")
if mibBuilder.loadTexts:
    twLinkPhyInterferenceSignalRatio.setUnits("0.1 dB")
_TwLinkPhyTxPower_Type = Centibel
_TwLinkPhyTxPower_Object = MibTableColumn
twLinkPhyTxPower = _TwLinkPhyTxPower_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 2, 1, 10),
    _TwLinkPhyTxPower_Type()
)
twLinkPhyTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkPhyTxPower.setStatus("current")
if mibBuilder.loadTexts:
    twLinkPhyTxPower.setUnits("0.1 dB")
_TwLinkPhyRxSignalLevel_Type = Centibel
_TwLinkPhyRxSignalLevel_Object = MibTableColumn
twLinkPhyRxSignalLevel = _TwLinkPhyRxSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 2, 1, 11),
    _TwLinkPhyRxSignalLevel_Type()
)
twLinkPhyRxSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkPhyRxSignalLevel.setStatus("current")
if mibBuilder.loadTexts:
    twLinkPhyRxSignalLevel.setUnits("0.1 dB")
_TwLinkMacStatsTable_Object = MibTable
twLinkMacStatsTable = _TwLinkMacStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 3)
)
if mibBuilder.loadTexts:
    twLinkMacStatsTable.setStatus("current")
_TwLinkMacStatsEntry_Object = MibTableRow
twLinkMacStatsEntry = _TwLinkMacStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 3, 1)
)
twLinkMacStatsEntry.setIndexNames(
    (0, "TARANA", "twLinkInterfaceId"),
)
if mibBuilder.loadTexts:
    twLinkMacStatsEntry.setStatus("current")


class _TwLinkMacState_Type(Integer32):
    """Custom type twLinkMacState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_TwLinkMacState_Type.__name__ = "Integer32"
_TwLinkMacState_Object = MibTableColumn
twLinkMacState = _TwLinkMacState_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 3, 1, 1),
    _TwLinkMacState_Type()
)
twLinkMacState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkMacState.setStatus("current")
_TwLinkMacUpTime_Type = Counter32
_TwLinkMacUpTime_Object = MibTableColumn
twLinkMacUpTime = _TwLinkMacUpTime_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 3, 1, 2),
    _TwLinkMacUpTime_Type()
)
twLinkMacUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkMacUpTime.setStatus("current")
if mibBuilder.loadTexts:
    twLinkMacUpTime.setUnits("sec")


class _TwLinkMacTxCapacity_Type(Gauge32):
    """Custom type twLinkMacTxCapacity based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000),
    )


_TwLinkMacTxCapacity_Type.__name__ = "Gauge32"
_TwLinkMacTxCapacity_Object = MibTableColumn
twLinkMacTxCapacity = _TwLinkMacTxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 3, 1, 3),
    _TwLinkMacTxCapacity_Type()
)
twLinkMacTxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkMacTxCapacity.setStatus("current")
if mibBuilder.loadTexts:
    twLinkMacTxCapacity.setUnits("Kbps")


class _TwLinkMacRxCapacity_Type(Gauge32):
    """Custom type twLinkMacRxCapacity based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000),
    )


_TwLinkMacRxCapacity_Type.__name__ = "Gauge32"
_TwLinkMacRxCapacity_Object = MibTableColumn
twLinkMacRxCapacity = _TwLinkMacRxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 3, 1, 4),
    _TwLinkMacRxCapacity_Type()
)
twLinkMacRxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkMacRxCapacity.setStatus("current")
if mibBuilder.loadTexts:
    twLinkMacRxCapacity.setUnits("Kbps")
_TwLinkPerfTable_Object = MibTable
twLinkPerfTable = _TwLinkPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4)
)
if mibBuilder.loadTexts:
    twLinkPerfTable.setStatus("current")
_TwLinkPerfEntry_Object = MibTableRow
twLinkPerfEntry = _TwLinkPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1)
)
twLinkPerfEntry.setIndexNames(
    (0, "TARANA", "twLinkInterfaceId"),
)
if mibBuilder.loadTexts:
    twLinkPerfEntry.setStatus("current")
_TwLinkTxPackets_Type = Counter64
_TwLinkTxPackets_Object = MibTableColumn
twLinkTxPackets = _TwLinkTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1, 1),
    _TwLinkTxPackets_Type()
)
twLinkTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkTxPackets.setStatus("current")
_TwLinkRxPackets_Type = Counter64
_TwLinkRxPackets_Object = MibTableColumn
twLinkRxPackets = _TwLinkRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1, 2),
    _TwLinkRxPackets_Type()
)
twLinkRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkRxPackets.setStatus("current")
_TwLinkTxBytes_Type = Counter64
_TwLinkTxBytes_Object = MibTableColumn
twLinkTxBytes = _TwLinkTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1, 3),
    _TwLinkTxBytes_Type()
)
twLinkTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkTxBytes.setStatus("current")
_TwLinkRxBytes_Type = Counter64
_TwLinkRxBytes_Object = MibTableColumn
twLinkRxBytes = _TwLinkRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1, 4),
    _TwLinkRxBytes_Type()
)
twLinkRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkRxBytes.setStatus("current")


class _TwLinkTxPacketRate_Type(Gauge32):
    """Custom type twLinkTxPacketRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TwLinkTxPacketRate_Type.__name__ = "Gauge32"
_TwLinkTxPacketRate_Object = MibTableColumn
twLinkTxPacketRate = _TwLinkTxPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1, 5),
    _TwLinkTxPacketRate_Type()
)
twLinkTxPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkTxPacketRate.setStatus("current")


class _TwLinkRxPacketRate_Type(Gauge32):
    """Custom type twLinkRxPacketRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TwLinkRxPacketRate_Type.__name__ = "Gauge32"
_TwLinkRxPacketRate_Object = MibTableColumn
twLinkRxPacketRate = _TwLinkRxPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1, 6),
    _TwLinkRxPacketRate_Type()
)
twLinkRxPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkRxPacketRate.setStatus("current")


class _TwLinkTxBitRate_Type(Gauge32):
    """Custom type twLinkTxBitRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000),
    )


_TwLinkTxBitRate_Type.__name__ = "Gauge32"
_TwLinkTxBitRate_Object = MibTableColumn
twLinkTxBitRate = _TwLinkTxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1, 7),
    _TwLinkTxBitRate_Type()
)
twLinkTxBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkTxBitRate.setStatus("current")
if mibBuilder.loadTexts:
    twLinkTxBitRate.setUnits("Kbps")


class _TwLinkRxBitRate_Type(Gauge32):
    """Custom type twLinkRxBitRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000),
    )


_TwLinkRxBitRate_Type.__name__ = "Gauge32"
_TwLinkRxBitRate_Object = MibTableColumn
twLinkRxBitRate = _TwLinkRxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1, 8),
    _TwLinkRxBitRate_Type()
)
twLinkRxBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkRxBitRate.setStatus("current")
if mibBuilder.loadTexts:
    twLinkRxBitRate.setUnits("Kbps")
_TwLinkTxLinkUtilization_Type = Permill
_TwLinkTxLinkUtilization_Object = MibTableColumn
twLinkTxLinkUtilization = _TwLinkTxLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1, 9),
    _TwLinkTxLinkUtilization_Type()
)
twLinkTxLinkUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkTxLinkUtilization.setStatus("current")
if mibBuilder.loadTexts:
    twLinkTxLinkUtilization.setUnits("0.1 %")
_TwLinkRxLinkUtilization_Type = Permill
_TwLinkRxLinkUtilization_Object = MibTableColumn
twLinkRxLinkUtilization = _TwLinkRxLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1, 10),
    _TwLinkRxLinkUtilization_Type()
)
twLinkRxLinkUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkRxLinkUtilization.setStatus("current")
if mibBuilder.loadTexts:
    twLinkRxLinkUtilization.setUnits("0.1 %")
_TwLinkRxBlockErrors_Type = Counter64
_TwLinkRxBlockErrors_Object = MibTableColumn
twLinkRxBlockErrors = _TwLinkRxBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1, 11),
    _TwLinkRxBlockErrors_Type()
)
twLinkRxBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkRxBlockErrors.setStatus("current")
_TwLinkRxFrameErrors_Type = Counter64
_TwLinkRxFrameErrors_Object = MibTableColumn
twLinkRxFrameErrors = _TwLinkRxFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1, 12),
    _TwLinkRxFrameErrors_Type()
)
twLinkRxFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkRxFrameErrors.setStatus("current")


class _TwLinkRxBlockErrorRate_Type(Millibel):
    """Custom type twLinkRxBlockErrorRate based on Millibel"""
    subtypeSpec = Millibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20000, 0),
    )


_TwLinkRxBlockErrorRate_Type.__name__ = "Millibel"
_TwLinkRxBlockErrorRate_Object = MibTableColumn
twLinkRxBlockErrorRate = _TwLinkRxBlockErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1, 13),
    _TwLinkRxBlockErrorRate_Type()
)
twLinkRxBlockErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkRxBlockErrorRate.setStatus("current")


class _TwLinkRxFrameErrorRate_Type(Millibel):
    """Custom type twLinkRxFrameErrorRate based on Millibel"""
    subtypeSpec = Millibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20000, 0),
    )


_TwLinkRxFrameErrorRate_Type.__name__ = "Millibel"
_TwLinkRxFrameErrorRate_Object = MibTableColumn
twLinkRxFrameErrorRate = _TwLinkRxFrameErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1, 14),
    _TwLinkRxFrameErrorRate_Type()
)
twLinkRxFrameErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkRxFrameErrorRate.setStatus("current")


class _TwLinkRxPacketErrorRate_Type(Millibel):
    """Custom type twLinkRxPacketErrorRate based on Millibel"""
    subtypeSpec = Millibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20000, 0),
    )


_TwLinkRxPacketErrorRate_Type.__name__ = "Millibel"
_TwLinkRxPacketErrorRate_Object = MibTableColumn
twLinkRxPacketErrorRate = _TwLinkRxPacketErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1, 15),
    _TwLinkRxPacketErrorRate_Type()
)
twLinkRxPacketErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkRxPacketErrorRate.setStatus("current")


class _TwLinkRxBitErrorRate_Type(Millibel):
    """Custom type twLinkRxBitErrorRate based on Millibel"""
    subtypeSpec = Millibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20000, 0),
    )


_TwLinkRxBitErrorRate_Type.__name__ = "Millibel"
_TwLinkRxBitErrorRate_Object = MibTableColumn
twLinkRxBitErrorRate = _TwLinkRxBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1, 16),
    _TwLinkRxBitErrorRate_Type()
)
twLinkRxBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkRxBitErrorRate.setStatus("current")
_TwLinkRxPacketErrors_Type = Counter64
_TwLinkRxPacketErrors_Object = MibTableColumn
twLinkRxPacketErrors = _TwLinkRxPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1, 17),
    _TwLinkRxPacketErrors_Type()
)
twLinkRxPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkRxPacketErrors.setStatus("current")
_TwLinkCountersUptime_Type = Counter32
_TwLinkCountersUptime_Object = MibTableColumn
twLinkCountersUptime = _TwLinkCountersUptime_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 4, 1, 18),
    _TwLinkCountersUptime_Type()
)
twLinkCountersUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkCountersUptime.setStatus("current")
if mibBuilder.loadTexts:
    twLinkCountersUptime.setUnits("sec")
_TwLinkErrorStatsTable_Object = MibTable
twLinkErrorStatsTable = _TwLinkErrorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 5)
)
if mibBuilder.loadTexts:
    twLinkErrorStatsTable.setStatus("current")
_TwLinkErrorStatsEntry_Object = MibTableRow
twLinkErrorStatsEntry = _TwLinkErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 5, 1)
)
twLinkErrorStatsEntry.setIndexNames(
    (0, "TARANA", "twLinkInterfaceId"),
)
if mibBuilder.loadTexts:
    twLinkErrorStatsEntry.setStatus("current")
_TwLinkErroredSeconds_Type = Counter64
_TwLinkErroredSeconds_Object = MibTableColumn
twLinkErroredSeconds = _TwLinkErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 5, 1, 1),
    _TwLinkErroredSeconds_Type()
)
twLinkErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkErroredSeconds.setStatus("current")
if mibBuilder.loadTexts:
    twLinkErroredSeconds.setUnits("s")
_TwLinkSeverelyErroredSeconds_Type = Counter64
_TwLinkSeverelyErroredSeconds_Object = MibTableColumn
twLinkSeverelyErroredSeconds = _TwLinkSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 5, 1, 2),
    _TwLinkSeverelyErroredSeconds_Type()
)
twLinkSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkSeverelyErroredSeconds.setStatus("current")
if mibBuilder.loadTexts:
    twLinkSeverelyErroredSeconds.setUnits("s")
_TwLinkBackgroundBlockErrors_Type = Counter64
_TwLinkBackgroundBlockErrors_Object = MibTableColumn
twLinkBackgroundBlockErrors = _TwLinkBackgroundBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 5, 1, 3),
    _TwLinkBackgroundBlockErrors_Type()
)
twLinkBackgroundBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkBackgroundBlockErrors.setStatus("current")
_TwLinkUnavailableSeconds_Type = Counter64
_TwLinkUnavailableSeconds_Object = MibTableColumn
twLinkUnavailableSeconds = _TwLinkUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 5, 1, 4),
    _TwLinkUnavailableSeconds_Type()
)
twLinkUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkUnavailableSeconds.setStatus("current")
if mibBuilder.loadTexts:
    twLinkUnavailableSeconds.setUnits("s")


class _TwLinkErrorStatIntervalType_Type(Integer32):
    """Custom type twLinkErrorStatIntervalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 1),
          ("oneDay", 2))
    )


_TwLinkErrorStatIntervalType_Type.__name__ = "Integer32"
_TwLinkErrorStatIntervalType_Object = MibTableColumn
twLinkErrorStatIntervalType = _TwLinkErrorStatIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 5, 1, 5),
    _TwLinkErrorStatIntervalType_Type()
)
twLinkErrorStatIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkErrorStatIntervalType.setStatus("current")


class _TwLinkErroredSecondsRatio_Type(Millibel):
    """Custom type twLinkErroredSecondsRatio based on Millibel"""
    subtypeSpec = Millibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20000, 0),
    )


_TwLinkErroredSecondsRatio_Type.__name__ = "Millibel"
_TwLinkErroredSecondsRatio_Object = MibTableColumn
twLinkErroredSecondsRatio = _TwLinkErroredSecondsRatio_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 5, 1, 6),
    _TwLinkErroredSecondsRatio_Type()
)
twLinkErroredSecondsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkErroredSecondsRatio.setStatus("current")


class _TwLinkSeverelyErroredSecondsRatio_Type(Millibel):
    """Custom type twLinkSeverelyErroredSecondsRatio based on Millibel"""
    subtypeSpec = Millibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20000, 0),
    )


_TwLinkSeverelyErroredSecondsRatio_Type.__name__ = "Millibel"
_TwLinkSeverelyErroredSecondsRatio_Object = MibTableColumn
twLinkSeverelyErroredSecondsRatio = _TwLinkSeverelyErroredSecondsRatio_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 5, 1, 7),
    _TwLinkSeverelyErroredSecondsRatio_Type()
)
twLinkSeverelyErroredSecondsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkSeverelyErroredSecondsRatio.setStatus("current")


class _TwLinkBackgroundBlockErrorRate_Type(Millibel):
    """Custom type twLinkBackgroundBlockErrorRate based on Millibel"""
    subtypeSpec = Millibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20000, 0),
    )


_TwLinkBackgroundBlockErrorRate_Type.__name__ = "Millibel"
_TwLinkBackgroundBlockErrorRate_Object = MibTableColumn
twLinkBackgroundBlockErrorRate = _TwLinkBackgroundBlockErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 5, 1, 8),
    _TwLinkBackgroundBlockErrorRate_Type()
)
twLinkBackgroundBlockErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkBackgroundBlockErrorRate.setStatus("current")


class _TwLinkUnavailableSecondsRatio_Type(Millibel):
    """Custom type twLinkUnavailableSecondsRatio based on Millibel"""
    subtypeSpec = Millibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20000, 0),
    )


_TwLinkUnavailableSecondsRatio_Type.__name__ = "Millibel"
_TwLinkUnavailableSecondsRatio_Object = MibTableColumn
twLinkUnavailableSecondsRatio = _TwLinkUnavailableSecondsRatio_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 5, 1, 9),
    _TwLinkUnavailableSecondsRatio_Type()
)
twLinkUnavailableSecondsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkUnavailableSecondsRatio.setStatus("current")
_TwLinkMcsHistoryTable_Object = MibTable
twLinkMcsHistoryTable = _TwLinkMcsHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 6)
)
if mibBuilder.loadTexts:
    twLinkMcsHistoryTable.setStatus("current")
_TwLinkMcsHistoryEntry_Object = MibTableRow
twLinkMcsHistoryEntry = _TwLinkMcsHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 6, 1)
)
twLinkMcsHistoryEntry.setIndexNames(
    (0, "TARANA", "twLinkInterfaceId"),
    (0, "TARANA", "twLinkMcsHistoryInterval"),
    (0, "TARANA", "twLinkMcsHistoryMcsId"),
)
if mibBuilder.loadTexts:
    twLinkMcsHistoryEntry.setStatus("current")


class _TwLinkMcsHistoryInterval_Type(Integer32):
    """Custom type twLinkMcsHistoryInterval based on Integer32"""
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
        *(("oneSecond", 1),
          ("oneMinute", 2),
          ("fifteenMinutes", 3),
          ("sixtyMinutes", 4))
    )


_TwLinkMcsHistoryInterval_Type.__name__ = "Integer32"
_TwLinkMcsHistoryInterval_Object = MibTableColumn
twLinkMcsHistoryInterval = _TwLinkMcsHistoryInterval_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 6, 1, 1),
    _TwLinkMcsHistoryInterval_Type()
)
twLinkMcsHistoryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkMcsHistoryInterval.setStatus("current")


class _TwLinkMcsHistoryMcsId_Type(Unsigned32):
    """Custom type twLinkMcsHistoryMcsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_TwLinkMcsHistoryMcsId_Type.__name__ = "Unsigned32"
_TwLinkMcsHistoryMcsId_Object = MibTableColumn
twLinkMcsHistoryMcsId = _TwLinkMcsHistoryMcsId_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 6, 1, 2),
    _TwLinkMcsHistoryMcsId_Type()
)
twLinkMcsHistoryMcsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkMcsHistoryMcsId.setStatus("current")
_TwLinkMcsHistory_Type = Permill
_TwLinkMcsHistory_Object = MibTableColumn
twLinkMcsHistory = _TwLinkMcsHistory_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 6, 1, 3),
    _TwLinkMcsHistory_Type()
)
twLinkMcsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twLinkMcsHistory.setStatus("current")
if mibBuilder.loadTexts:
    twLinkMcsHistory.setUnits("0.1 %")
_TwLinkSecurityTable_Object = MibTable
twLinkSecurityTable = _TwLinkSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 7)
)
if mibBuilder.loadTexts:
    twLinkSecurityTable.setStatus("current")
_TwLinkSecurityEntry_Object = MibTableRow
twLinkSecurityEntry = _TwLinkSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 7, 1)
)
twLinkSecurityEntry.setIndexNames(
    (0, "TARANA", "twLinkInterfaceId"),
)
if mibBuilder.loadTexts:
    twLinkSecurityEntry.setStatus("current")


class _TwLinkTxEncryptionType_Type(Integer32):
    """Custom type twLinkTxEncryptionType based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("aes128", 1),
          ("aes192", 2),
          ("aes256", 3))
    )


_TwLinkTxEncryptionType_Type.__name__ = "Integer32"
_TwLinkTxEncryptionType_Object = MibTableColumn
twLinkTxEncryptionType = _TwLinkTxEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 7, 1, 1),
    _TwLinkTxEncryptionType_Type()
)
twLinkTxEncryptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twLinkTxEncryptionType.setStatus("current")


class _TwLinkTxEncryptionKey_Type(OctetString):
    """Custom type twLinkTxEncryptionKey based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TwLinkTxEncryptionKey_Type.__name__ = "OctetString"
_TwLinkTxEncryptionKey_Object = MibTableColumn
twLinkTxEncryptionKey = _TwLinkTxEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 7, 1, 2),
    _TwLinkTxEncryptionKey_Type()
)
twLinkTxEncryptionKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twLinkTxEncryptionKey.setStatus("current")


class _TwLinkRxEncryptionType_Type(Integer32):
    """Custom type twLinkRxEncryptionType based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("aes128", 1),
          ("aes192", 2),
          ("aes256", 3))
    )


_TwLinkRxEncryptionType_Type.__name__ = "Integer32"
_TwLinkRxEncryptionType_Object = MibTableColumn
twLinkRxEncryptionType = _TwLinkRxEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 7, 1, 3),
    _TwLinkRxEncryptionType_Type()
)
twLinkRxEncryptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twLinkRxEncryptionType.setStatus("current")


class _TwLinkRxEncryptionKey_Type(OctetString):
    """Custom type twLinkRxEncryptionKey based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TwLinkRxEncryptionKey_Type.__name__ = "OctetString"
_TwLinkRxEncryptionKey_Object = MibTableColumn
twLinkRxEncryptionKey = _TwLinkRxEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 9, 7, 1, 4),
    _TwLinkRxEncryptionKey_Type()
)
twLinkRxEncryptionKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twLinkRxEncryptionKey.setStatus("current")
_TwRemoteTable_Object = MibTable
twRemoteTable = _TwRemoteTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10)
)
if mibBuilder.loadTexts:
    twRemoteTable.setStatus("current")
_TwRemoteEntry_Object = MibTableRow
twRemoteEntry = _TwRemoteEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1)
)
twRemoteEntry.setIndexNames(
    (0, "TARANA", "twLinkInterfaceId"),
)
if mibBuilder.loadTexts:
    twRemoteEntry.setStatus("current")
_TwRemotePhysicalSerialNum_Type = OctetString
_TwRemotePhysicalSerialNum_Object = MibTableColumn
twRemotePhysicalSerialNum = _TwRemotePhysicalSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 1),
    _TwRemotePhysicalSerialNum_Type()
)
twRemotePhysicalSerialNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twRemotePhysicalSerialNum.setStatus("current")
_TwRemoteMacAddr_Type = MacAddress
_TwRemoteMacAddr_Object = MibTableColumn
twRemoteMacAddr = _TwRemoteMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 2),
    _TwRemoteMacAddr_Type()
)
twRemoteMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twRemoteMacAddr.setStatus("current")
_TwRemoteIPAddr_Type = IpAddress
_TwRemoteIPAddr_Object = MibTableColumn
twRemoteIPAddr = _TwRemoteIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 3),
    _TwRemoteIPAddr_Type()
)
twRemoteIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twRemoteIPAddr.setStatus("current")


class _TwRemoteLinkPhyState_Type(Integer32):
    """Custom type twRemoteLinkPhyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
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
        *(("invalid", -1),
          ("init", 0),
          ("align", 1),
          ("acq", 2),
          ("refine", 3),
          ("sync", 4),
          ("cal", 5),
          ("range", 6),
          ("pwrlow", 7),
          ("pwrhigh", 8),
          ("track", 9),
          ("exit", 10))
    )


_TwRemoteLinkPhyState_Type.__name__ = "Integer32"
_TwRemoteLinkPhyState_Object = MibTableColumn
twRemoteLinkPhyState = _TwRemoteLinkPhyState_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 4),
    _TwRemoteLinkPhyState_Type()
)
twRemoteLinkPhyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteLinkPhyState.setStatus("current")
_TwRemoteLinkPhyUpTime_Type = Counter32
_TwRemoteLinkPhyUpTime_Object = MibTableColumn
twRemoteLinkPhyUpTime = _TwRemoteLinkPhyUpTime_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 5),
    _TwRemoteLinkPhyUpTime_Type()
)
twRemoteLinkPhyUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteLinkPhyUpTime.setStatus("current")
if mibBuilder.loadTexts:
    twRemoteLinkPhyUpTime.setUnits("sec")


class _TwRemoteLinkPhyPathRange_Type(Unsigned32):
    """Custom type twRemoteLinkPhyPathRange based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TwRemoteLinkPhyPathRange_Type.__name__ = "Unsigned32"
_TwRemoteLinkPhyPathRange_Object = MibTableColumn
twRemoteLinkPhyPathRange = _TwRemoteLinkPhyPathRange_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 6),
    _TwRemoteLinkPhyPathRange_Type()
)
twRemoteLinkPhyPathRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteLinkPhyPathRange.setStatus("current")
if mibBuilder.loadTexts:
    twRemoteLinkPhyPathRange.setUnits("m")


class _TwRemoteLinkPhyPathLoss_Type(Centibel):
    """Custom type twRemoteLinkPhyPathLoss based on Centibel"""
    subtypeSpec = Centibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 2000),
    )


_TwRemoteLinkPhyPathLoss_Type.__name__ = "Centibel"
_TwRemoteLinkPhyPathLoss_Object = MibTableColumn
twRemoteLinkPhyPathLoss = _TwRemoteLinkPhyPathLoss_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 7),
    _TwRemoteLinkPhyPathLoss_Type()
)
twRemoteLinkPhyPathLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteLinkPhyPathLoss.setStatus("current")
if mibBuilder.loadTexts:
    twRemoteLinkPhyPathLoss.setUnits("0.1 dB")


class _TwRemoteLinkPhySinr_Type(Centibel):
    """Custom type twRemoteLinkPhySinr based on Centibel"""
    subtypeSpec = Centibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 400),
    )


_TwRemoteLinkPhySinr_Type.__name__ = "Centibel"
_TwRemoteLinkPhySinr_Object = MibTableColumn
twRemoteLinkPhySinr = _TwRemoteLinkPhySinr_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 8),
    _TwRemoteLinkPhySinr_Type()
)
twRemoteLinkPhySinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteLinkPhySinr.setStatus("current")
if mibBuilder.loadTexts:
    twRemoteLinkPhySinr.setUnits("0.1 dB")


class _TwRemoteLinkMacState_Type(Integer32):
    """Custom type twRemoteLinkMacState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_TwRemoteLinkMacState_Type.__name__ = "Integer32"
_TwRemoteLinkMacState_Object = MibTableColumn
twRemoteLinkMacState = _TwRemoteLinkMacState_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 9),
    _TwRemoteLinkMacState_Type()
)
twRemoteLinkMacState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteLinkMacState.setStatus("current")
_TwRemoteLinkMacUpTime_Type = Counter32
_TwRemoteLinkMacUpTime_Object = MibTableColumn
twRemoteLinkMacUpTime = _TwRemoteLinkMacUpTime_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 10),
    _TwRemoteLinkMacUpTime_Type()
)
twRemoteLinkMacUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteLinkMacUpTime.setStatus("current")
if mibBuilder.loadTexts:
    twRemoteLinkMacUpTime.setUnits("sec")


class _TwRemoteNodeAntStatus_Type(Integer32):
    """Custom type twRemoteNodeAntStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("impaired", 0),
          ("degraded", 1),
          ("operational", 2))
    )


_TwRemoteNodeAntStatus_Type.__name__ = "Integer32"
_TwRemoteNodeAntStatus_Object = MibTableColumn
twRemoteNodeAntStatus = _TwRemoteNodeAntStatus_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 11),
    _TwRemoteNodeAntStatus_Type()
)
twRemoteNodeAntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteNodeAntStatus.setStatus("current")


class _TwRemoteNodeTxTotalPower_Type(Centibel):
    """Custom type twRemoteNodeTxTotalPower based on Centibel"""
    subtypeSpec = Centibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 500),
    )


_TwRemoteNodeTxTotalPower_Type.__name__ = "Centibel"
_TwRemoteNodeTxTotalPower_Object = MibTableColumn
twRemoteNodeTxTotalPower = _TwRemoteNodeTxTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 12),
    _TwRemoteNodeTxTotalPower_Type()
)
twRemoteNodeTxTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteNodeTxTotalPower.setStatus("current")
if mibBuilder.loadTexts:
    twRemoteNodeTxTotalPower.setUnits("0.1 dBm")


class _TwRemoteNodeTxHeadroom_Type(Centibel):
    """Custom type twRemoteNodeTxHeadroom based on Centibel"""
    subtypeSpec = Centibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 500),
    )


_TwRemoteNodeTxHeadroom_Type.__name__ = "Centibel"
_TwRemoteNodeTxHeadroom_Object = MibTableColumn
twRemoteNodeTxHeadroom = _TwRemoteNodeTxHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 13),
    _TwRemoteNodeTxHeadroom_Type()
)
twRemoteNodeTxHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteNodeTxHeadroom.setStatus("current")
if mibBuilder.loadTexts:
    twRemoteNodeTxHeadroom.setUnits("0.1 dB")
_TwRemoteLinkCode_Type = LinkCode
_TwRemoteLinkCode_Object = MibTableColumn
twRemoteLinkCode = _TwRemoteLinkCode_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 14),
    _TwRemoteLinkCode_Type()
)
twRemoteLinkCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteLinkCode.setStatus("current")


class _TwRemoteGpsLat_Type(Microdegree):
    """Custom type twRemoteGpsLat based on Microdegree"""
    subtypeSpec = Microdegree.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90000000, 90000000),
    )


_TwRemoteGpsLat_Type.__name__ = "Microdegree"
_TwRemoteGpsLat_Object = MibTableColumn
twRemoteGpsLat = _TwRemoteGpsLat_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 15),
    _TwRemoteGpsLat_Type()
)
twRemoteGpsLat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteGpsLat.setStatus("current")
if mibBuilder.loadTexts:
    twRemoteGpsLat.setUnits("micro-degree")


class _TwRemoteGpsLon_Type(Microdegree):
    """Custom type twRemoteGpsLon based on Microdegree"""
    subtypeSpec = Microdegree.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-180000000, 180000000),
    )


_TwRemoteGpsLon_Type.__name__ = "Microdegree"
_TwRemoteGpsLon_Object = MibTableColumn
twRemoteGpsLon = _TwRemoteGpsLon_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 16),
    _TwRemoteGpsLon_Type()
)
twRemoteGpsLon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteGpsLon.setStatus("current")
if mibBuilder.loadTexts:
    twRemoteGpsLon.setUnits("micro-degree")


class _TwRemoteGpsElevation_Type(Unsigned32):
    """Custom type twRemoteGpsElevation based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TwRemoteGpsElevation_Type.__name__ = "Unsigned32"
_TwRemoteGpsElevation_Object = MibTableColumn
twRemoteGpsElevation = _TwRemoteGpsElevation_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 17),
    _TwRemoteGpsElevation_Type()
)
twRemoteGpsElevation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteGpsElevation.setStatus("current")
if mibBuilder.loadTexts:
    twRemoteGpsElevation.setUnits("cm")


class _TwRemoteLinkRxPacketErrorRate_Type(Millibel):
    """Custom type twRemoteLinkRxPacketErrorRate based on Millibel"""
    subtypeSpec = Millibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20000, 0),
    )


_TwRemoteLinkRxPacketErrorRate_Type.__name__ = "Millibel"
_TwRemoteLinkRxPacketErrorRate_Object = MibTableColumn
twRemoteLinkRxPacketErrorRate = _TwRemoteLinkRxPacketErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 19),
    _TwRemoteLinkRxPacketErrorRate_Type()
)
twRemoteLinkRxPacketErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteLinkRxPacketErrorRate.setStatus("current")
_TwRemoteLinkRxPacketErrors_Type = Counter64
_TwRemoteLinkRxPacketErrors_Object = MibTableColumn
twRemoteLinkRxPacketErrors = _TwRemoteLinkRxPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 20),
    _TwRemoteLinkRxPacketErrors_Type()
)
twRemoteLinkRxPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteLinkRxPacketErrors.setStatus("current")


class _TwRemoteLinkRxBlockErrorRate_Type(Millibel):
    """Custom type twRemoteLinkRxBlockErrorRate based on Millibel"""
    subtypeSpec = Millibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20000, 0),
    )


_TwRemoteLinkRxBlockErrorRate_Type.__name__ = "Millibel"
_TwRemoteLinkRxBlockErrorRate_Object = MibTableColumn
twRemoteLinkRxBlockErrorRate = _TwRemoteLinkRxBlockErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 21),
    _TwRemoteLinkRxBlockErrorRate_Type()
)
twRemoteLinkRxBlockErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteLinkRxBlockErrorRate.setStatus("current")
_TwRemoteLinkRxBlockErrors_Type = Counter64
_TwRemoteLinkRxBlockErrors_Object = MibTableColumn
twRemoteLinkRxBlockErrors = _TwRemoteLinkRxBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 22),
    _TwRemoteLinkRxBlockErrors_Type()
)
twRemoteLinkRxBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteLinkRxBlockErrors.setStatus("current")


class _TwRemoteLinkRxBitErrorRate_Type(Millibel):
    """Custom type twRemoteLinkRxBitErrorRate based on Millibel"""
    subtypeSpec = Millibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20000, 0),
    )


_TwRemoteLinkRxBitErrorRate_Type.__name__ = "Millibel"
_TwRemoteLinkRxBitErrorRate_Object = MibTableColumn
twRemoteLinkRxBitErrorRate = _TwRemoteLinkRxBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 23),
    _TwRemoteLinkRxBitErrorRate_Type()
)
twRemoteLinkRxBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteLinkRxBitErrorRate.setStatus("current")


class _TwRemoteNodeRssi_Type(Centibel):
    """Custom type twRemoteNodeRssi based on Centibel"""
    subtypeSpec = Centibel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 500),
    )


_TwRemoteNodeRssi_Type.__name__ = "Centibel"
_TwRemoteNodeRssi_Object = MibTableColumn
twRemoteNodeRssi = _TwRemoteNodeRssi_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 24),
    _TwRemoteNodeRssi_Type()
)
twRemoteNodeRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteNodeRssi.setStatus("current")
if mibBuilder.loadTexts:
    twRemoteNodeRssi.setUnits("0.1 dBm")
_TwRemoteSysName_Type = OctetString
_TwRemoteSysName_Object = MibTableColumn
twRemoteSysName = _TwRemoteSysName_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 10, 1, 25),
    _TwRemoteSysName_Type()
)
twRemoteSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twRemoteSysName.setStatus("current")
_TwServices_ObjectIdentity = ObjectIdentity
twServices = _TwServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 11)
)


class _TwServiceLed_Type(Integer32):
    """Custom type twServiceLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TwServiceLed_Type.__name__ = "Integer32"
_TwServiceLed_Object = MibScalar
twServiceLed = _TwServiceLed_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 11, 1),
    _TwServiceLed_Type()
)
twServiceLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twServiceLed.setStatus("current")


class _TwServiceUsbEthernet_Type(Integer32):
    """Custom type twServiceUsbEthernet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TwServiceUsbEthernet_Type.__name__ = "Integer32"
_TwServiceUsbEthernet_Object = MibScalar
twServiceUsbEthernet = _TwServiceUsbEthernet_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 11, 2),
    _TwServiceUsbEthernet_Type()
)
twServiceUsbEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twServiceUsbEthernet.setStatus("current")


class _TwServiceUsbWifi_Type(Integer32):
    """Custom type twServiceUsbWifi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TwServiceUsbWifi_Type.__name__ = "Integer32"
_TwServiceUsbWifi_Object = MibScalar
twServiceUsbWifi = _TwServiceUsbWifi_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 11, 3),
    _TwServiceUsbWifi_Type()
)
twServiceUsbWifi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twServiceUsbWifi.setStatus("current")
_TwServiceLog_ObjectIdentity = ObjectIdentity
twServiceLog = _TwServiceLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 11, 4)
)


class _TwServiceLogLevel_Type(Integer32):
    """Custom type twServiceLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_TwServiceLogLevel_Type.__name__ = "Integer32"
_TwServiceLogLevel_Object = MibScalar
twServiceLogLevel = _TwServiceLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 11, 4, 1),
    _TwServiceLogLevel_Type()
)
twServiceLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twServiceLogLevel.setStatus("current")
_TwServiceLogRemoteServer_Type = IpAddress
_TwServiceLogRemoteServer_Object = MibScalar
twServiceLogRemoteServer = _TwServiceLogRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 11, 4, 2),
    _TwServiceLogRemoteServer_Type()
)
twServiceLogRemoteServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twServiceLogRemoteServer.setStatus("current")
_TwServiceLogComponentLevelTable_Object = MibTable
twServiceLogComponentLevelTable = _TwServiceLogComponentLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 11, 4, 3)
)
if mibBuilder.loadTexts:
    twServiceLogComponentLevelTable.setStatus("current")
_TwServiceLogComponentLevelEntry_Object = MibTableRow
twServiceLogComponentLevelEntry = _TwServiceLogComponentLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 11, 4, 3, 1)
)
twServiceLogComponentLevelEntry.setIndexNames(
    (0, "TARANA", "twSysComponentId"),
)
if mibBuilder.loadTexts:
    twServiceLogComponentLevelEntry.setStatus("current")


class _TwServiceLogComponentLevel_Type(Integer32):
    """Custom type twServiceLogComponentLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TwServiceLogComponentLevel_Type.__name__ = "Integer32"
_TwServiceLogComponentLevel_Object = MibTableColumn
twServiceLogComponentLevel = _TwServiceLogComponentLevel_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 11, 4, 3, 1, 1),
    _TwServiceLogComponentLevel_Type()
)
twServiceLogComponentLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twServiceLogComponentLevel.setStatus("current")
_TwServiceTrapManagerTable_Object = MibTable
twServiceTrapManagerTable = _TwServiceTrapManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 11, 5)
)
if mibBuilder.loadTexts:
    twServiceTrapManagerTable.setStatus("current")
_TwServiceTrapManagerEntry_Object = MibTableRow
twServiceTrapManagerEntry = _TwServiceTrapManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 11, 5, 1)
)
twServiceTrapManagerEntry.setIndexNames(
    (0, "TARANA", "twServiceTrapManagerEntryId"),
)
if mibBuilder.loadTexts:
    twServiceTrapManagerEntry.setStatus("current")


class _TwServiceTrapManagerEntryId_Type(Unsigned32):
    """Custom type twServiceTrapManagerEntryId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TwServiceTrapManagerEntryId_Type.__name__ = "Unsigned32"
_TwServiceTrapManagerEntryId_Object = MibTableColumn
twServiceTrapManagerEntryId = _TwServiceTrapManagerEntryId_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 11, 5, 1, 1),
    _TwServiceTrapManagerEntryId_Type()
)
twServiceTrapManagerEntryId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twServiceTrapManagerEntryId.setStatus("current")
_TwServiceTrapManagerEntryIp_Type = IpAddress
_TwServiceTrapManagerEntryIp_Object = MibTableColumn
twServiceTrapManagerEntryIp = _TwServiceTrapManagerEntryIp_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 11, 5, 1, 2),
    _TwServiceTrapManagerEntryIp_Type()
)
twServiceTrapManagerEntryIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twServiceTrapManagerEntryIp.setStatus("current")


class _TwServiceTrapManagerEntryPort_Type(Unsigned32):
    """Custom type twServiceTrapManagerEntryPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TwServiceTrapManagerEntryPort_Type.__name__ = "Unsigned32"
_TwServiceTrapManagerEntryPort_Object = MibTableColumn
twServiceTrapManagerEntryPort = _TwServiceTrapManagerEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 11, 5, 1, 3),
    _TwServiceTrapManagerEntryPort_Type()
)
twServiceTrapManagerEntryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twServiceTrapManagerEntryPort.setStatus("current")


class _TwServiceTrapManagerCommunity_Type(OctetString):
    """Custom type twServiceTrapManagerCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TwServiceTrapManagerCommunity_Type.__name__ = "OctetString"
_TwServiceTrapManagerCommunity_Object = MibTableColumn
twServiceTrapManagerCommunity = _TwServiceTrapManagerCommunity_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 11, 5, 1, 4),
    _TwServiceTrapManagerCommunity_Type()
)
twServiceTrapManagerCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twServiceTrapManagerCommunity.setStatus("current")
_TwServiceMotionTracking_ObjectIdentity = ObjectIdentity
twServiceMotionTracking = _TwServiceMotionTracking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 11, 6)
)


class _TwMotionTrackingTilt_Type(Microdegree):
    """Custom type twMotionTrackingTilt based on Microdegree"""
    subtypeSpec = Microdegree.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90000000, 90000000),
    )


_TwMotionTrackingTilt_Type.__name__ = "Microdegree"
_TwMotionTrackingTilt_Object = MibScalar
twMotionTrackingTilt = _TwMotionTrackingTilt_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 11, 6, 1),
    _TwMotionTrackingTilt_Type()
)
twMotionTrackingTilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twMotionTrackingTilt.setStatus("current")
if mibBuilder.loadTexts:
    twMotionTrackingTilt.setUnits("micro-degrees")
_TwDiagnostics_ObjectIdentity = ObjectIdentity
twDiagnostics = _TwDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 12)
)


class _TwDiagLinkReset_Type(Integer32):
    """Custom type twDiagLinkReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_TwDiagLinkReset_Type.__name__ = "Integer32"
_TwDiagLinkReset_Object = MibScalar
twDiagLinkReset = _TwDiagLinkReset_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 12, 1),
    _TwDiagLinkReset_Type()
)
twDiagLinkReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twDiagLinkReset.setStatus("current")


class _TwDiagNodeReset_Type(Integer32):
    """Custom type twDiagNodeReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TwDiagNodeReset_Type.__name__ = "Integer32"
_TwDiagNodeReset_Object = MibScalar
twDiagNodeReset = _TwDiagNodeReset_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 12, 2),
    _TwDiagNodeReset_Type()
)
twDiagNodeReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twDiagNodeReset.setStatus("current")


class _TwDiagResetAllCounters_Type(Integer32):
    """Custom type twDiagResetAllCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_TwDiagResetAllCounters_Type.__name__ = "Integer32"
_TwDiagResetAllCounters_Object = MibScalar
twDiagResetAllCounters = _TwDiagResetAllCounters_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 12, 3),
    _TwDiagResetAllCounters_Type()
)
twDiagResetAllCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twDiagResetAllCounters.setStatus("current")


class _TwDiagRunDiagnostics_Type(Integer32):
    """Custom type twDiagRunDiagnostics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("run", 1))
    )


_TwDiagRunDiagnostics_Type.__name__ = "Integer32"
_TwDiagRunDiagnostics_Object = MibScalar
twDiagRunDiagnostics = _TwDiagRunDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 12, 4),
    _TwDiagRunDiagnostics_Type()
)
twDiagRunDiagnostics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twDiagRunDiagnostics.setStatus("current")


class _TwDiagRunStatus_Type(Integer32):
    """Custom type twDiagRunStatus based on Integer32"""
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
        *(("idle", 0),
          ("success", 1),
          ("inprogress", 2),
          ("failed", 3))
    )


_TwDiagRunStatus_Type.__name__ = "Integer32"
_TwDiagRunStatus_Object = MibScalar
twDiagRunStatus = _TwDiagRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 12, 5),
    _TwDiagRunStatus_Type()
)
twDiagRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twDiagRunStatus.setStatus("current")
_TwDiagMacReflector_ObjectIdentity = ObjectIdentity
twDiagMacReflector = _TwDiagMacReflector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 12, 6)
)


class _TwDiagMacReflectorEnable_Type(Integer32):
    """Custom type twDiagMacReflectorEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TwDiagMacReflectorEnable_Type.__name__ = "Integer32"
_TwDiagMacReflectorEnable_Object = MibScalar
twDiagMacReflectorEnable = _TwDiagMacReflectorEnable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 12, 6, 1),
    _TwDiagMacReflectorEnable_Type()
)
twDiagMacReflectorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twDiagMacReflectorEnable.setStatus("current")
_TwDiagMacReflectorInterface_Type = Integer32
_TwDiagMacReflectorInterface_Object = MibScalar
twDiagMacReflectorInterface = _TwDiagMacReflectorInterface_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 12, 6, 2),
    _TwDiagMacReflectorInterface_Type()
)
twDiagMacReflectorInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twDiagMacReflectorInterface.setStatus("current")
_TwDiagMacReflectorSrcMac_Type = MacAddress
_TwDiagMacReflectorSrcMac_Object = MibScalar
twDiagMacReflectorSrcMac = _TwDiagMacReflectorSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 12, 6, 3),
    _TwDiagMacReflectorSrcMac_Type()
)
twDiagMacReflectorSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twDiagMacReflectorSrcMac.setStatus("current")
_TwDiagMacReflectorDstMac_Type = MacAddress
_TwDiagMacReflectorDstMac_Object = MibScalar
twDiagMacReflectorDstMac = _TwDiagMacReflectorDstMac_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 12, 6, 4),
    _TwDiagMacReflectorDstMac_Type()
)
twDiagMacReflectorDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twDiagMacReflectorDstMac.setStatus("current")
_TwNotifications_ObjectIdentity = ObjectIdentity
twNotifications = _TwNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13)
)
_TwNotificationObjects_ObjectIdentity = ObjectIdentity
twNotificationObjects = _TwNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 1)
)
_TwNotifObjIpAddr_Type = IpAddress
_TwNotifObjIpAddr_Object = MibScalar
twNotifObjIpAddr = _TwNotifObjIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 1, 1),
    _TwNotifObjIpAddr_Type()
)
twNotifObjIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    twNotifObjIpAddr.setStatus("current")


class _TwNotifObjSerialNum_Type(OctetString):
    """Custom type twNotifObjSerialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TwNotifObjSerialNum_Type.__name__ = "OctetString"
_TwNotifObjSerialNum_Object = MibScalar
twNotifObjSerialNum = _TwNotifObjSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 1, 2),
    _TwNotifObjSerialNum_Type()
)
twNotifObjSerialNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    twNotifObjSerialNum.setStatus("current")


class _TwNotifObjSeverity_Type(Integer32):
    """Custom type twNotifObjSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6),
          ("info", 7))
    )


_TwNotifObjSeverity_Type.__name__ = "Integer32"
_TwNotifObjSeverity_Object = MibScalar
twNotifObjSeverity = _TwNotifObjSeverity_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 1, 3),
    _TwNotifObjSeverity_Type()
)
twNotifObjSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    twNotifObjSeverity.setStatus("current")
_TwNotifObjMessage_Type = DisplayString
_TwNotifObjMessage_Object = MibScalar
twNotifObjMessage = _TwNotifObjMessage_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 1, 4),
    _TwNotifObjMessage_Type()
)
twNotifObjMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    twNotifObjMessage.setStatus("current")


class _TwNotifObjCategory_Type(Integer32):
    """Custom type twNotifObjCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("investigate", 1),
          ("connectivityFault", 2),
          ("dataCongestionFault", 3),
          ("systemFault", 4),
          ("hardwareFailure", 5),
          ("configurationFault", 8),
          ("systemAccessFault", 10))
    )


_TwNotifObjCategory_Type.__name__ = "Integer32"
_TwNotifObjCategory_Object = MibScalar
twNotifObjCategory = _TwNotifObjCategory_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 1, 5),
    _TwNotifObjCategory_Type()
)
twNotifObjCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    twNotifObjCategory.setStatus("current")
_TwNotifObjName_Type = DisplayString
_TwNotifObjName_Object = MibScalar
twNotifObjName = _TwNotifObjName_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 1, 6),
    _TwNotifObjName_Type()
)
twNotifObjName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    twNotifObjName.setStatus("current")


class _TwNotifObjState_Type(Integer32):
    """Custom type twNotifObjState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_TwNotifObjState_Type.__name__ = "Integer32"
_TwNotifObjState_Object = MibScalar
twNotifObjState = _TwNotifObjState_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 1, 7),
    _TwNotifObjState_Type()
)
twNotifObjState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    twNotifObjState.setStatus("current")


class _TwNotifObjLinkNumber_Type(Integer32):
    """Custom type twNotifObjLinkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TwNotifObjLinkNumber_Type.__name__ = "Integer32"
_TwNotifObjLinkNumber_Object = MibScalar
twNotifObjLinkNumber = _TwNotifObjLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 1, 8),
    _TwNotifObjLinkNumber_Type()
)
twNotifObjLinkNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    twNotifObjLinkNumber.setStatus("current")
_TwNotifObjSysName_Type = DisplayString
_TwNotifObjSysName_Object = MibScalar
twNotifObjSysName = _TwNotifObjSysName_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 1, 9),
    _TwNotifObjSysName_Type()
)
twNotifObjSysName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    twNotifObjSysName.setStatus("current")
_TwNotificationTypes_ObjectIdentity = ObjectIdentity
twNotificationTypes = _TwNotificationTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 2)
)
_TwAlarmTable_Object = MibTable
twAlarmTable = _TwAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 3)
)
if mibBuilder.loadTexts:
    twAlarmTable.setStatus("current")
_TwAlarmEntry_Object = MibTableRow
twAlarmEntry = _TwAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 3, 1)
)
twAlarmEntry.setIndexNames(
    (0, "TARANA", "twAlarmIndex"),
)
if mibBuilder.loadTexts:
    twAlarmEntry.setStatus("current")


class _TwAlarmIndex_Type(Integer32):
    """Custom type twAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_TwAlarmIndex_Type.__name__ = "Integer32"
_TwAlarmIndex_Object = MibTableColumn
twAlarmIndex = _TwAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 3, 1, 1),
    _TwAlarmIndex_Type()
)
twAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twAlarmIndex.setStatus("current")
_TwAlarmName_Type = OctetString
_TwAlarmName_Object = MibTableColumn
twAlarmName = _TwAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 3, 1, 2),
    _TwAlarmName_Type()
)
twAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twAlarmName.setStatus("current")


class _TwAlarmCategory_Type(Integer32):
    """Custom type twAlarmCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("investigate", 1),
          ("connectivityFault", 2),
          ("dataCongestionFault", 3),
          ("systemFault", 4),
          ("hardwareFailure", 5),
          ("configurationFault", 8),
          ("systemAccessFault", 10))
    )


_TwAlarmCategory_Type.__name__ = "Integer32"
_TwAlarmCategory_Object = MibTableColumn
twAlarmCategory = _TwAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 3, 1, 3),
    _TwAlarmCategory_Type()
)
twAlarmCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twAlarmCategory.setStatus("current")


class _TwAlarmSeverity_Type(Integer32):
    """Custom type twAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6),
          ("info", 7))
    )


_TwAlarmSeverity_Type.__name__ = "Integer32"
_TwAlarmSeverity_Object = MibTableColumn
twAlarmSeverity = _TwAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 3, 1, 4),
    _TwAlarmSeverity_Type()
)
twAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twAlarmSeverity.setStatus("current")


class _TwAlarmState_Type(Integer32):
    """Custom type twAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_TwAlarmState_Type.__name__ = "Integer32"
_TwAlarmState_Object = MibTableColumn
twAlarmState = _TwAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 3, 1, 5),
    _TwAlarmState_Type()
)
twAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twAlarmState.setStatus("current")
_TwAlarmRisingThreshold_Type = Integer32
_TwAlarmRisingThreshold_Object = MibTableColumn
twAlarmRisingThreshold = _TwAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 3, 1, 6),
    _TwAlarmRisingThreshold_Type()
)
twAlarmRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twAlarmRisingThreshold.setStatus("current")
_TwAlarmFallingThreshold_Type = Integer32
_TwAlarmFallingThreshold_Object = MibTableColumn
twAlarmFallingThreshold = _TwAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 3, 1, 7),
    _TwAlarmFallingThreshold_Type()
)
twAlarmFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twAlarmFallingThreshold.setStatus("current")


class _TwAlarmTrap_Type(Integer32):
    """Custom type twAlarmTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TwAlarmTrap_Type.__name__ = "Integer32"
_TwAlarmTrap_Object = MibTableColumn
twAlarmTrap = _TwAlarmTrap_Object(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 3, 1, 8),
    _TwAlarmTrap_Type()
)
twAlarmTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twAlarmTrap.setStatus("current")
_TwConformance_ObjectIdentity = ObjectIdentity
twConformance = _TwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 14)
)
_TwGroups_ObjectIdentity = ObjectIdentity
twGroups = _TwGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 1, 14, 1)
)
_TaranawirelessRegids_ObjectIdentity = ObjectIdentity
taranawirelessRegids = _TaranawirelessRegids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 3)
)
_TaranawirelessCommon_ObjectIdentity = ObjectIdentity
taranawirelessCommon = _TaranawirelessCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 4)
)
_TaranawirelessProducts_ObjectIdentity = ObjectIdentity
taranawirelessProducts = _TaranawirelessProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 5)
)
_TaranawirelessExperimental_ObjectIdentity = ObjectIdentity
taranawirelessExperimental = _TaranawirelessExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39660, 6)
)

# Managed Objects groups

twCapabilitiesAll = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39660, 1, 14, 1, 1)
)
twCapabilitiesAll.setObjects(
      *(("TARANA", "twServiceLogRemoteServer"),
        ("TARANA", "twServiceLogComponentLevel"),
        ("TARANA", "twServiceTrapManagerEntryIp"),
        ("TARANA", "twServiceTrapManagerEntryPort"),
        ("TARANA", "twServiceTrapManagerCommunity"),
        ("TARANA", "twLinkErrorStatIntervalType"),
        ("TARANA", "twLinkErroredSecondsRatio"),
        ("TARANA", "twLinkSeverelyErroredSecondsRatio"),
        ("TARANA", "twLinkBackgroundBlockErrorRate"),
        ("TARANA", "twLinkUnavailableSecondsRatio"),
        ("TARANA", "twSysCpuTemperature"),
        ("TARANA", "twSysRadioTemperature"),
        ("TARANA", "twSysCpuUtilization"),
        ("TARANA", "twSysMemoryUtilization"),
        ("TARANA", "twSysBootReason"),
        ("TARANA", "twSysNotes"),
        ("TARANA", "twSysInstallationDate"),
        ("TARANA", "twConfSave"),
        ("TARANA", "twConfExportUrl"),
        ("TARANA", "twConfDownloadUrl"),
        ("TARANA", "twConfImportDownloadedConfig"),
        ("TARANA", "twConfRevertTimeout"),
        ("TARANA", "twSysImageBankCurrent"),
        ("TARANA", "twSysImageChangeBank"),
        ("TARANA", "twSysImageDownloadStart"),
        ("TARANA", "twSysImageDownloadStatus"),
        ("TARANA", "twSysImageDownloadStop"),
        ("TARANA", "twSysImageUpgradeStart"),
        ("TARANA", "twSysImageUpgradeStatus"),
        ("TARANA", "twSysImageUpgradeStop"),
        ("TARANA", "twSysImageBankId"),
        ("TARANA", "twSysImageBankVersion"),
        ("TARANA", "twSysImageBankStatus"),
        ("TARANA", "twNetworkProfile"),
        ("TARANA", "twNetworkClockSource"),
        ("TARANA", "twNetworkMinFreq"),
        ("TARANA", "twNetworkMaxFreq"),
        ("TARANA", "twNetworkFrequency"),
        ("TARANA", "twNetworkProfileId"),
        ("TARANA", "twNetworkProfileDescription"),
        ("TARANA", "twNetworkProfileDLSymbols"),
        ("TARANA", "twNetworkProfileULSymbols"),
        ("TARANA", "twNetworkProfileFrameTime"),
        ("TARANA", "twNetworkProfileCyclicPrefixRatio"),
        ("TARANA", "twNetworkProfileMaxDistance"),
        ("TARANA", "twNodeMode"),
        ("TARANA", "twNodeLinkCode"),
        ("TARANA", "twNodeTxOpmode"),
        ("TARANA", "twNodeTxMaxRegulatoryPower"),
        ("TARANA", "twNodeTxMaxPermittedPower"),
        ("TARANA", "twNodeTxTotalPower"),
        ("TARANA", "twNodeTxAttenuation"),
        ("TARANA", "twNodeRxGain"),
        ("TARANA", "twNodeTxHeadroom"),
        ("TARANA", "twNodeAntInactive"),
        ("TARANA", "twNodeAntStatus"),
        ("TARANA", "twLinkInterfaceId"),
        ("TARANA", "twLinkAcmEnable"),
        ("TARANA", "twLinkResetCounters"),
        ("TARANA", "twLinkPhyState"),
        ("TARANA", "twLinkPhyUpTime"),
        ("TARANA", "twLinkPhyPathRange"),
        ("TARANA", "twLinkPhyPathLoss"),
        ("TARANA", "twLinkMacState"),
        ("TARANA", "twLinkMacUpTime"),
        ("TARANA", "twRemoteLinkPhyState"),
        ("TARANA", "twRemoteLinkPhyUpTime"),
        ("TARANA", "twRemoteLinkPhyPathRange"),
        ("TARANA", "twRemoteLinkPhyPathLoss"),
        ("TARANA", "twRemoteLinkMacState"),
        ("TARANA", "twRemoteLinkMacUpTime"),
        ("TARANA", "twRemoteNodeAntStatus"),
        ("TARANA", "twRemoteNodeTxTotalPower"),
        ("TARANA", "twRemoteNodeTxHeadroom"),
        ("TARANA", "twRemoteLinkCode"),
        ("TARANA", "twRemoteGpsLat"),
        ("TARANA", "twRemoteGpsLon"),
        ("TARANA", "twRemoteGpsElevation"),
        ("TARANA", "twRemoteLinkRxPacketErrorRate"),
        ("TARANA", "twDiagResetAllCounters"),
        ("TARANA", "twDiagRunDiagnostics"),
        ("TARANA", "twDiagRunStatus"),
        ("TARANA", "twSysComponentVersion"),
        ("TARANA", "twSysImageDownloadProgress"),
        ("TARANA", "twSysImageUpgradeProgress"),
        ("TARANA", "twLinkAcmProfile"),
        ("TARANA", "twLinkMcsMin"),
        ("TARANA", "twLinkMcsMax"),
        ("TARANA", "twLinkMcsFixed"),
        ("TARANA", "twLinkAdaptiveMarginEnable"),
        ("TARANA", "twLinkAcmMargin"),
        ("TARANA", "twLinkMacTxCapacity"),
        ("TARANA", "twLinkMacRxCapacity"),
        ("TARANA", "twLinkTxPackets"),
        ("TARANA", "twLinkRxPackets"),
        ("TARANA", "twLinkTxBytes"),
        ("TARANA", "twLinkRxBytes"),
        ("TARANA", "twLinkTxPacketRate"),
        ("TARANA", "twLinkRxPacketRate"),
        ("TARANA", "twLinkRxBlockErrorRate"),
        ("TARANA", "twLinkRxFrameErrorRate"),
        ("TARANA", "twLinkErroredSeconds"),
        ("TARANA", "twLinkSeverelyErroredSeconds"),
        ("TARANA", "twLinkBackgroundBlockErrors"),
        ("TARANA", "twLinkUnavailableSeconds"),
        ("TARANA", "twRemoteIPAddr"),
        ("TARANA", "twNodeRssi"),
        ("TARANA", "twLinkPhySinr"),
        ("TARANA", "twLinkPhyTxMcs"),
        ("TARANA", "twLinkPhyRxMcs"),
        ("TARANA", "twLinkMcsHistoryInterval"),
        ("TARANA", "twRemoteLinkPhySinr"),
        ("TARANA", "twRemoteMacAddr"),
        ("TARANA", "twServiceLed"),
        ("TARANA", "twServiceUsbEthernet"),
        ("TARANA", "twLinkMcsHistoryMcsId"),
        ("TARANA", "twLinkMcsHistory"),
        ("TARANA", "twServiceUsbWifi"),
        ("TARANA", "twSysMibRev"),
        ("TARANA", "twNetworkAcmProfileId"),
        ("TARANA", "twLinkTxBitRate"),
        ("TARANA", "twLinkRxBitRate"),
        ("TARANA", "twLinkTxLinkUtilization"),
        ("TARANA", "twLinkRxBlockErrors"),
        ("TARANA", "twLinkRxFrameErrors"),
        ("TARANA", "twLinkRxPacketErrorRate"),
        ("TARANA", "twServiceTrapManagerEntryId"),
        ("TARANA", "twNetworkAcmProfileDescription"),
        ("TARANA", "twRemotePhysicalSerialNum"),
        ("TARANA", "twDiagNodeReset"),
        ("TARANA", "twConfVersion"),
        ("TARANA", "twLinkRxBitErrorRate"),
        ("TARANA", "twLinkRxPacketErrors"),
        ("TARANA", "twLinkCountersUptime"),
        ("TARANA", "twRemoteNodeRssi"),
        ("TARANA", "twRemoteSysName"),
        ("TARANA", "twDiagMacReflectorEnable"),
        ("TARANA", "twDiagMacReflectorInterface"),
        ("TARANA", "twDiagMacReflectorSrcMac"),
        ("TARANA", "twDiagMacReflectorDstMac"),
        ("TARANA", "twDiagLinkReset"),
        ("TARANA", "twLinkTxEncryptionType"),
        ("TARANA", "twLinkTxEncryptionKey"),
        ("TARANA", "twLinkRxEncryptionType"),
        ("TARANA", "twLinkRxEncryptionKey"),
        ("TARANA", "twRemoteLinkRxPacketErrors"),
        ("TARANA", "twRemoteLinkRxBlockErrorRate"),
        ("TARANA", "twRemoteLinkRxBlockErrors"),
        ("TARANA", "twRemoteLinkRxBitErrorRate"),
        ("TARANA", "twSysClockDateAndTime"),
        ("TARANA", "twNotifObjIpAddr"),
        ("TARANA", "twNotifObjSerialNum"),
        ("TARANA", "twNotifObjSeverity"),
        ("TARANA", "twNotifObjMessage"),
        ("TARANA", "twServiceLogLevel"),
        ("TARANA", "twClockingGpsPresent"),
        ("TARANA", "twClockingGpsStatus"),
        ("TARANA", "twClockingLockStatus"),
        ("TARANA", "twClockingGpsSnr"),
        ("TARANA", "twClockingGpsLat"),
        ("TARANA", "twClockingGpsLon"),
        ("TARANA", "twClockingGpsElevation"),
        ("TARANA", "twClockingGpsNumberOfSatellites"),
        ("TARANA", "twSysReboot"),
        ("TARANA", "twSysComponentId"),
        ("TARANA", "twLinkAbicEnable"),
        ("TARANA", "twLinkArqEnable"),
        ("TARANA", "twLinkPhyInterferenceSignalRatio"),
        ("TARANA", "twSysRegulatoryDomainCountry"),
        ("TARANA", "twSysRegulatoryDomain"),
        ("TARANA", "twLinkPhyInterferenceDutyCycle"),
        ("TARANA", "twNodeTxMinPermittedPower"),
        ("TARANA", "twSectorBwMapProfileDescription"),
        ("TARANA", "twSectorBwMapProfileId"),
        ("TARANA", "twMotionTrackingTilt"),
        ("TARANA", "twNotifObjCategory"),
        ("TARANA", "twNotifObjState"),
        ("TARANA", "twNotifObjLinkNumber"),
        ("TARANA", "twNodeDcsChannelChangeReason"),
        ("TARANA", "twNodeDfsStatus"),
        ("TARANA", "twNodeDcsMode"),
        ("TARANA", "twNodeDcsChannelChangeTime"),
        ("TARANA", "twNodeDcsChannelChangeCount"),
        ("TARANA", "twNodeDfsChannelChangeTime"),
        ("TARANA", "twNodeDfsChannelChangeCount"),
        ("TARANA", "twNodeFrequencyChannelNum"),
        ("TARANA", "twNodeFrequencyValue"),
        ("TARANA", "twNodeFrequencyChannelStatus"),
        ("TARANA", "twSysRegulatoryDomainId"),
        ("TARANA", "twSysRegulatoryDomainName"),
        ("TARANA", "twSysRegulatoryDomainCountries"),
        ("TARANA", "twSysRegulatoryDomainDefaultCountry"),
        ("TARANA", "twNetworkChannelBandwidth"),
        ("TARANA", "twAlarmIndex"),
        ("TARANA", "twAlarmName"),
        ("TARANA", "twAlarmCategory"),
        ("TARANA", "twAlarmSeverity"),
        ("TARANA", "twAlarmState"),
        ("TARANA", "twAlarmRisingThreshold"),
        ("TARANA", "twAlarmFallingThreshold"),
        ("TARANA", "twAlarmTrap"),
        ("TARANA", "twNotifObjSysName"),
        ("TARANA", "twNetworkCodeOperatorId"),
        ("TARANA", "twNetworkCodeAreaId"),
        ("TARANA", "twNetworkCodeGroupId"),
        ("TARANA", "twNetworkCodeSetId"),
        ("TARANA", "twLicFeatIndex"),
        ("TARANA", "twLicFeatId"),
        ("TARANA", "twLicFeatName"),
        ("TARANA", "twLicFeatPlat"),
        ("TARANA", "twLicFeatType"),
        ("TARANA", "twLicFeatDesc"),
        ("TARANA", "twLicFeatActiveLink"),
        ("TARANA", "twLicInstIndex"),
        ("TARANA", "twLicInstVerMajor"),
        ("TARANA", "twLicInstVerMinor"),
        ("TARANA", "twLicInstVerStatus"),
        ("TARANA", "twLicInstFeatureId"),
        ("TARANA", "twLicInstFeatureName"),
        ("TARANA", "twLicInstActive"),
        ("TARANA", "twLicInstLinkNum"),
        ("TARANA", "twLicInstKeyText"),
        ("TARANA", "twLicInstRowStatus"),
        ("TARANA", "twNodeBlacklistIndex"),
        ("TARANA", "twNodeBlacklistFreqStartKHz"),
        ("TARANA", "twNodeBlacklistFreqEndKHz"),
        ("TARANA", "twNodeBlacklistRowStatus"),
        ("TARANA", "twLinkPhyTxPower"),
        ("TARANA", "twLinkPhyRxSignalLevel"),
        ("TARANA", "twSectorBwMap"),
        ("TARANA", "twSectorNumLinks"),
        ("TARANA", "twLinkNumber"),
        ("TARANA", "twLicInstSerial"),
        ("TARANA", "twNotifObjName"),
        ("TARANA", "twLinkRxLinkUtilization"))
)
if mibBuilder.loadTexts:
    twCapabilitiesAll.setStatus("current")


# Notification objects

twNotifBootReason = NotificationType(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 2, 1)
)
twNotifBootReason.setObjects(
      *(("TARANA", "twNotifObjName"),
        ("TARANA", "twNotifObjCategory"),
        ("TARANA", "twNotifObjSeverity"),
        ("TARANA", "twNotifObjSerialNum"),
        ("TARANA", "twSysClockDateAndTime"),
        ("TARANA", "twNotifObjIpAddr"),
        ("TARANA", "twNotifObjSysName"),
        ("TARANA", "twNotifObjMessage"),
        ("TARANA", "twNotifObjState"),
        ("TARANA", "twSysBootReason"))
)
if mibBuilder.loadTexts:
    twNotifBootReason.setStatus(
        "current"
    )

twNotifGpsLockFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 2, 2)
)
twNotifGpsLockFailure.setObjects(
      *(("TARANA", "twNotifObjName"),
        ("TARANA", "twNotifObjCategory"),
        ("TARANA", "twNotifObjSeverity"),
        ("TARANA", "twNotifObjSerialNum"),
        ("TARANA", "twSysClockDateAndTime"),
        ("TARANA", "twNotifObjIpAddr"),
        ("TARANA", "twNotifObjSysName"),
        ("TARANA", "twNotifObjMessage"),
        ("TARANA", "twNotifObjState"),
        ("TARANA", "twClockingGpsStatus"),
        ("TARANA", "twClockingLockStatus"),
        ("TARANA", "twClockingGpsSnr"),
        ("TARANA", "twClockingGpsLat"),
        ("TARANA", "twClockingGpsLon"),
        ("TARANA", "twClockingGpsElevation"),
        ("TARANA", "twClockingGpsNumberOfSatellites"))
)
if mibBuilder.loadTexts:
    twNotifGpsLockFailure.setStatus(
        "current"
    )

twNotifOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 2, 3)
)
twNotifOverTemperature.setObjects(
      *(("TARANA", "twNotifObjName"),
        ("TARANA", "twNotifObjCategory"),
        ("TARANA", "twNotifObjSeverity"),
        ("TARANA", "twNotifObjSerialNum"),
        ("TARANA", "twSysClockDateAndTime"),
        ("TARANA", "twNotifObjIpAddr"),
        ("TARANA", "twNotifObjSysName"),
        ("TARANA", "twNotifObjMessage"),
        ("TARANA", "twNotifObjState"),
        ("TARANA", "twSysCpuTemperature"),
        ("TARANA", "twSysRadioTemperature"),
        ("TARANA", "twSysCpuUtilization"),
        ("TARANA", "twNodeTxTotalPower"))
)
if mibBuilder.loadTexts:
    twNotifOverTemperature.setStatus(
        "current"
    )

twNotifLowVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 2, 4)
)
twNotifLowVoltage.setObjects(
      *(("TARANA", "twNotifObjName"),
        ("TARANA", "twNotifObjCategory"),
        ("TARANA", "twNotifObjSeverity"),
        ("TARANA", "twNotifObjSerialNum"),
        ("TARANA", "twSysClockDateAndTime"),
        ("TARANA", "twNotifObjIpAddr"),
        ("TARANA", "twNotifObjSysName"),
        ("TARANA", "twNotifObjMessage"),
        ("TARANA", "twNotifObjState"))
)
if mibBuilder.loadTexts:
    twNotifLowVoltage.setStatus(
        "current"
    )

twNotifRfLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 2, 5)
)
twNotifRfLinkDown.setObjects(
      *(("TARANA", "twNotifObjName"),
        ("TARANA", "twNotifObjCategory"),
        ("TARANA", "twNotifObjSeverity"),
        ("TARANA", "twNotifObjSerialNum"),
        ("TARANA", "twSysClockDateAndTime"),
        ("TARANA", "twNotifObjIpAddr"),
        ("TARANA", "twNotifObjSysName"),
        ("TARANA", "twNotifObjMessage"),
        ("TARANA", "twNotifObjState"),
        ("TARANA", "twNotifObjLinkNumber"),
        ("TARANA", "twLinkPhyState"),
        ("TARANA", "twLinkMacState"),
        ("TARANA", "twNodeTxOpmode"),
        ("TARANA", "twNodeTxTotalPower"),
        ("TARANA", "twNodeRssi"),
        ("TARANA", "twNetworkFrequency"))
)
if mibBuilder.loadTexts:
    twNotifRfLinkDown.setStatus(
        "current"
    )

twNotifRfLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 2, 6)
)
twNotifRfLinkUp.setObjects(
      *(("TARANA", "twNotifObjName"),
        ("TARANA", "twNotifObjCategory"),
        ("TARANA", "twNotifObjSeverity"),
        ("TARANA", "twNotifObjSerialNum"),
        ("TARANA", "twSysClockDateAndTime"),
        ("TARANA", "twNotifObjIpAddr"),
        ("TARANA", "twNotifObjSysName"),
        ("TARANA", "twNotifObjMessage"),
        ("TARANA", "twNotifObjState"),
        ("TARANA", "twNotifObjLinkNumber"),
        ("TARANA", "twLinkPhyState"),
        ("TARANA", "twLinkMacState"),
        ("TARANA", "twNodeTxOpmode"),
        ("TARANA", "twNodeTxTotalPower"),
        ("TARANA", "twNodeRssi"),
        ("TARANA", "twNetworkFrequency"))
)
if mibBuilder.loadTexts:
    twNotifRfLinkUp.setStatus(
        "current"
    )

twNotifTxCapacity = NotificationType(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 2, 7)
)
twNotifTxCapacity.setObjects(
      *(("TARANA", "twNotifObjName"),
        ("TARANA", "twNotifObjCategory"),
        ("TARANA", "twNotifObjSeverity"),
        ("TARANA", "twNotifObjSerialNum"),
        ("TARANA", "twSysClockDateAndTime"),
        ("TARANA", "twNotifObjIpAddr"),
        ("TARANA", "twNotifObjSysName"),
        ("TARANA", "twNotifObjMessage"),
        ("TARANA", "twNotifObjState"),
        ("TARANA", "twNotifObjLinkNumber"),
        ("TARANA", "twLinkPhyPathRange"),
        ("TARANA", "twLinkPhyPathLoss"),
        ("TARANA", "twRemoteNodeRssi"),
        ("TARANA", "twRemoteLinkPhySinr"),
        ("TARANA", "twRemoteLinkRxBlockErrorRate"),
        ("TARANA", "twRemoteLinkRxPacketErrorRate"),
        ("TARANA", "twRemoteNodeAntStatus"))
)
if mibBuilder.loadTexts:
    twNotifTxCapacity.setStatus(
        "current"
    )

twNotifRxCapacity = NotificationType(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 2, 8)
)
twNotifRxCapacity.setObjects(
      *(("TARANA", "twNotifObjName"),
        ("TARANA", "twNotifObjCategory"),
        ("TARANA", "twNotifObjSeverity"),
        ("TARANA", "twNotifObjSerialNum"),
        ("TARANA", "twSysClockDateAndTime"),
        ("TARANA", "twNotifObjIpAddr"),
        ("TARANA", "twNotifObjSysName"),
        ("TARANA", "twNotifObjMessage"),
        ("TARANA", "twNotifObjState"),
        ("TARANA", "twNotifObjLinkNumber"),
        ("TARANA", "twLinkPhyPathRange"),
        ("TARANA", "twLinkPhyPathLoss"),
        ("TARANA", "twNodeRssi"),
        ("TARANA", "twLinkPhySinr"),
        ("TARANA", "twLinkRxBlockErrorRate"),
        ("TARANA", "twLinkRxPacketErrorRate"),
        ("TARANA", "twNodeAntStatus"),
        ("TARANA", "twLinkPhyInterferenceDutyCycle"),
        ("TARANA", "twLinkPhyInterferenceSignalRatio"))
)
if mibBuilder.loadTexts:
    twNotifRxCapacity.setStatus(
        "current"
    )

twNotifPhySinr = NotificationType(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 2, 9)
)
twNotifPhySinr.setObjects(
      *(("TARANA", "twNotifObjName"),
        ("TARANA", "twNotifObjCategory"),
        ("TARANA", "twNotifObjSeverity"),
        ("TARANA", "twNotifObjSerialNum"),
        ("TARANA", "twSysClockDateAndTime"),
        ("TARANA", "twNotifObjIpAddr"),
        ("TARANA", "twNotifObjSysName"),
        ("TARANA", "twNotifObjMessage"),
        ("TARANA", "twNotifObjState"),
        ("TARANA", "twNotifObjLinkNumber"),
        ("TARANA", "twLinkPhyPathRange"),
        ("TARANA", "twLinkPhyPathLoss"),
        ("TARANA", "twNodeRssi"),
        ("TARANA", "twLinkPhySinr"),
        ("TARANA", "twNodeAntStatus"),
        ("TARANA", "twLinkPhyInterferenceDutyCycle"),
        ("TARANA", "twLinkPhyInterferenceSignalRatio"),
        ("TARANA", "twRemoteNodeTxTotalPower"),
        ("TARANA", "twRemoteNodeTxHeadroom"))
)
if mibBuilder.loadTexts:
    twNotifPhySinr.setStatus(
        "current"
    )

twNotifRxPktError = NotificationType(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 2, 10)
)
twNotifRxPktError.setObjects(
      *(("TARANA", "twNotifObjName"),
        ("TARANA", "twNotifObjCategory"),
        ("TARANA", "twNotifObjSeverity"),
        ("TARANA", "twNotifObjSerialNum"),
        ("TARANA", "twSysClockDateAndTime"),
        ("TARANA", "twNotifObjIpAddr"),
        ("TARANA", "twNotifObjSysName"),
        ("TARANA", "twNotifObjMessage"),
        ("TARANA", "twNotifObjState"),
        ("TARANA", "twNotifObjLinkNumber"),
        ("TARANA", "twNodeRssi"),
        ("TARANA", "twLinkPhySinr"),
        ("TARANA", "twNodeAntStatus"),
        ("TARANA", "twLinkPhyInterferenceDutyCycle"),
        ("TARANA", "twLinkPhyInterferenceSignalRatio"),
        ("TARANA", "twLinkAcmEnable"),
        ("TARANA", "twLinkAcmProfile"),
        ("TARANA", "twLinkRxBitRate"),
        ("TARANA", "twLinkRxBlockErrorRate"),
        ("TARANA", "twLinkRxPacketErrorRate"))
)
if mibBuilder.loadTexts:
    twNotifRxPktError.setStatus(
        "current"
    )

twNotifTxPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 2, 11)
)
twNotifTxPower.setObjects(
      *(("TARANA", "twNotifObjName"),
        ("TARANA", "twNotifObjCategory"),
        ("TARANA", "twNotifObjSeverity"),
        ("TARANA", "twNotifObjSerialNum"),
        ("TARANA", "twSysClockDateAndTime"),
        ("TARANA", "twNotifObjIpAddr"),
        ("TARANA", "twNotifObjSysName"),
        ("TARANA", "twNotifObjMessage"),
        ("TARANA", "twNotifObjState"),
        ("TARANA", "twNodeTxTotalPower"),
        ("TARANA", "twNodeTxAttenuation"),
        ("TARANA", "twNodeAntStatus"))
)
if mibBuilder.loadTexts:
    twNotifTxPower.setStatus(
        "current"
    )

twNotifAntStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 2, 12)
)
twNotifAntStatus.setObjects(
      *(("TARANA", "twNotifObjName"),
        ("TARANA", "twNotifObjCategory"),
        ("TARANA", "twNotifObjSeverity"),
        ("TARANA", "twNotifObjSerialNum"),
        ("TARANA", "twSysClockDateAndTime"),
        ("TARANA", "twNotifObjIpAddr"),
        ("TARANA", "twNotifObjSysName"),
        ("TARANA", "twNotifObjMessage"),
        ("TARANA", "twNotifObjState"),
        ("TARANA", "twNodeTxTotalPower"),
        ("TARANA", "twNodeTxAttenuation"),
        ("TARANA", "twNodeRxGain"),
        ("TARANA", "twNodeAntInactive"))
)
if mibBuilder.loadTexts:
    twNotifAntStatus.setStatus(
        "current"
    )

twNotifConfSave = NotificationType(
    (1, 3, 6, 1, 4, 1, 39660, 1, 13, 2, 13)
)
twNotifConfSave.setObjects(
      *(("TARANA", "twNotifObjName"),
        ("TARANA", "twNotifObjCategory"),
        ("TARANA", "twNotifObjSeverity"),
        ("TARANA", "twNotifObjSerialNum"),
        ("TARANA", "twSysClockDateAndTime"),
        ("TARANA", "twNotifObjIpAddr"),
        ("TARANA", "twNotifObjSysName"),
        ("TARANA", "twNotifObjMessage"),
        ("TARANA", "twNotifObjState"),
        ("TARANA", "twConfSave"))
)
if mibBuilder.loadTexts:
    twNotifConfSave.setStatus(
        "current"
    )


# Notifications groups

twNotificationsAll = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 39660, 1, 14, 1, 2)
)
twNotificationsAll.setObjects(
      *(("TARANA", "twNotifBootReason"),
        ("TARANA", "twNotifOverTemperature"),
        ("TARANA", "twNotifRfLinkUp"),
        ("TARANA", "twNotifTxCapacity"),
        ("TARANA", "twNotifRxCapacity"),
        ("TARANA", "twNotifPhySinr"),
        ("TARANA", "twNotifRxPktError"),
        ("TARANA", "twNotifTxPower"),
        ("TARANA", "twNotifAntStatus"),
        ("TARANA", "twNotifConfSave"),
        ("TARANA", "twNotifLowVoltage"),
        ("TARANA", "twNotifGpsLockFailure"),
        ("TARANA", "twNotifRfLinkDown"))
)
if mibBuilder.loadTexts:
    twNotificationsAll.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TARANA",
    **{"LinkCode": LinkCode,
       "Decibel": Decibel,
       "Centibel": Centibel,
       "Millibel": Millibel,
       "Percent": Percent,
       "Permill": Permill,
       "Microdegree": Microdegree,
       "taranawireless": taranawireless,
       "aa2": aa2,
       "twSys": twSys,
       "twSysMibRev": twSysMibRev,
       "twSysCpuTemperature": twSysCpuTemperature,
       "twSysRadioTemperature": twSysRadioTemperature,
       "twSysCpuUtilization": twSysCpuUtilization,
       "twSysMemoryUtilization": twSysMemoryUtilization,
       "twSysBootReason": twSysBootReason,
       "twSysReboot": twSysReboot,
       "twSysNotes": twSysNotes,
       "twSysInstallationDate": twSysInstallationDate,
       "twSysComponentVersionTable": twSysComponentVersionTable,
       "twSysComponentVersionEntry": twSysComponentVersionEntry,
       "twSysComponentId": twSysComponentId,
       "twSysComponentVersion": twSysComponentVersion,
       "twSysClockDateAndTime": twSysClockDateAndTime,
       "twSysRegulatory": twSysRegulatory,
       "twSysRegulatoryDomain": twSysRegulatoryDomain,
       "twSysRegulatoryDomainCountry": twSysRegulatoryDomainCountry,
       "twSysRegulatoryDomainAvailableTable": twSysRegulatoryDomainAvailableTable,
       "twSysRegulatoryDomainAvailableEntry": twSysRegulatoryDomainAvailableEntry,
       "twSysRegulatoryDomainId": twSysRegulatoryDomainId,
       "twSysRegulatoryDomainName": twSysRegulatoryDomainName,
       "twSysRegulatoryDomainDefaultCountry": twSysRegulatoryDomainDefaultCountry,
       "twSysRegulatoryDomainCountries": twSysRegulatoryDomainCountries,
       "twLic": twLic,
       "twLicFeatTable": twLicFeatTable,
       "twLicFeatEntry": twLicFeatEntry,
       "twLicFeatIndex": twLicFeatIndex,
       "twLicFeatId": twLicFeatId,
       "twLicFeatName": twLicFeatName,
       "twLicFeatPlat": twLicFeatPlat,
       "twLicFeatType": twLicFeatType,
       "twLicFeatDesc": twLicFeatDesc,
       "twLicFeatActiveLink": twLicFeatActiveLink,
       "twLicInstTable": twLicInstTable,
       "twLicInstEntry": twLicInstEntry,
       "twLicInstIndex": twLicInstIndex,
       "twLicInstVerMajor": twLicInstVerMajor,
       "twLicInstVerMinor": twLicInstVerMinor,
       "twLicInstVerStatus": twLicInstVerStatus,
       "twLicInstFeatureId": twLicInstFeatureId,
       "twLicInstFeatureName": twLicInstFeatureName,
       "twLicInstActive": twLicInstActive,
       "twLicInstLinkNum": twLicInstLinkNum,
       "twLicInstKeyText": twLicInstKeyText,
       "twLicInstSerial": twLicInstSerial,
       "twLicInstRowStatus": twLicInstRowStatus,
       "twConf": twConf,
       "twConfSave": twConfSave,
       "twConfExportUrl": twConfExportUrl,
       "twConfDownloadUrl": twConfDownloadUrl,
       "twConfImportDownloadedConfig": twConfImportDownloadedConfig,
       "twConfRevertTimeout": twConfRevertTimeout,
       "twConfVersion": twConfVersion,
       "twConfSaveDownloadedConfig": twConfSaveDownloadedConfig,
       "twSysImage": twSysImage,
       "twSysImageBankCurrent": twSysImageBankCurrent,
       "twSysImageChangeBank": twSysImageChangeBank,
       "twSysImageDownloadStart": twSysImageDownloadStart,
       "twSysImageDownloadStatus": twSysImageDownloadStatus,
       "twSysImageDownloadProgress": twSysImageDownloadProgress,
       "twSysImageDownloadStop": twSysImageDownloadStop,
       "twSysImageUpgradeStart": twSysImageUpgradeStart,
       "twSysImageUpgradeStatus": twSysImageUpgradeStatus,
       "twSysImageUpgradeProgress": twSysImageUpgradeProgress,
       "twSysImageUpgradeStop": twSysImageUpgradeStop,
       "twSysImageBankTable": twSysImageBankTable,
       "twSysImageBankEntry": twSysImageBankEntry,
       "twSysImageBankId": twSysImageBankId,
       "twSysImageBankVersion": twSysImageBankVersion,
       "twSysImageBankStatus": twSysImageBankStatus,
       "twClocking": twClocking,
       "twClockingGpsPresent": twClockingGpsPresent,
       "twClockingGpsStatus": twClockingGpsStatus,
       "twClockingLockStatus": twClockingLockStatus,
       "twClockingGpsSnr": twClockingGpsSnr,
       "twClockingGpsLat": twClockingGpsLat,
       "twClockingGpsLon": twClockingGpsLon,
       "twClockingGpsElevation": twClockingGpsElevation,
       "twClockingGpsNumberOfSatellites": twClockingGpsNumberOfSatellites,
       "twNetwork": twNetwork,
       "twNetworkProfile": twNetworkProfile,
       "twNetworkClockSource": twNetworkClockSource,
       "twNetworkMinFreq": twNetworkMinFreq,
       "twNetworkMaxFreq": twNetworkMaxFreq,
       "twNetworkFrequency": twNetworkFrequency,
       "twNetworkProfileAvailableTable": twNetworkProfileAvailableTable,
       "twNetworkProfileAvailableEntry": twNetworkProfileAvailableEntry,
       "twNetworkProfileId": twNetworkProfileId,
       "twNetworkProfileDescription": twNetworkProfileDescription,
       "twNetworkProfileDLSymbols": twNetworkProfileDLSymbols,
       "twNetworkProfileULSymbols": twNetworkProfileULSymbols,
       "twNetworkProfileFrameTime": twNetworkProfileFrameTime,
       "twNetworkProfileCyclicPrefixRatio": twNetworkProfileCyclicPrefixRatio,
       "twNetworkProfileMaxDistance": twNetworkProfileMaxDistance,
       "twNetworkAcmProfileAvailableTable": twNetworkAcmProfileAvailableTable,
       "twNetworkAcmProfileAvailableEntry": twNetworkAcmProfileAvailableEntry,
       "twNetworkAcmProfileId": twNetworkAcmProfileId,
       "twNetworkAcmProfileDescription": twNetworkAcmProfileDescription,
       "twNetworkChannelBandwidth": twNetworkChannelBandwidth,
       "twNetworkCodeOperatorId": twNetworkCodeOperatorId,
       "twNetworkCodeAreaId": twNetworkCodeAreaId,
       "twNetworkCodeGroupId": twNetworkCodeGroupId,
       "twNetworkCodeSetId": twNetworkCodeSetId,
       "twSector": twSector,
       "twSectorNumLinks": twSectorNumLinks,
       "twSectorBwMap": twSectorBwMap,
       "twSectorBwMapProfileAvailableTable": twSectorBwMapProfileAvailableTable,
       "twSectorBwMapProfileAvailableEntry": twSectorBwMapProfileAvailableEntry,
       "twSectorBwMapProfileId": twSectorBwMapProfileId,
       "twSectorBwMapProfileDescription": twSectorBwMapProfileDescription,
       "twNode": twNode,
       "twNodeMode": twNodeMode,
       "twNodeLinkCode": twNodeLinkCode,
       "twNodeTxOpmode": twNodeTxOpmode,
       "twNodeTxMaxRegulatoryPower": twNodeTxMaxRegulatoryPower,
       "twNodeTxMaxPermittedPower": twNodeTxMaxPermittedPower,
       "twNodeTxTotalPower": twNodeTxTotalPower,
       "twNodeRssi": twNodeRssi,
       "twNodeTxAttenuation": twNodeTxAttenuation,
       "twNodeRxGain": twNodeRxGain,
       "twNodeTxHeadroom": twNodeTxHeadroom,
       "twNodeAntInactive": twNodeAntInactive,
       "twNodeAntStatus": twNodeAntStatus,
       "twNodeTxMinPermittedPower": twNodeTxMinPermittedPower,
       "twNodeFrequencyTable": twNodeFrequencyTable,
       "twNodeFrequencyEntry": twNodeFrequencyEntry,
       "twNodeFrequencyChannelNum": twNodeFrequencyChannelNum,
       "twNodeFrequencyValue": twNodeFrequencyValue,
       "twNodeFrequencyChannelStatus": twNodeFrequencyChannelStatus,
       "twNodeDxs": twNodeDxs,
       "twNodeDcsChannelChangeReason": twNodeDcsChannelChangeReason,
       "twNodeDfsStatus": twNodeDfsStatus,
       "twNodeDcsMode": twNodeDcsMode,
       "twNodeDcsChannelChangeTime": twNodeDcsChannelChangeTime,
       "twNodeDcsChannelChangeCount": twNodeDcsChannelChangeCount,
       "twNodeDfsChannelChangeTime": twNodeDfsChannelChangeTime,
       "twNodeDfsChannelChangeCount": twNodeDfsChannelChangeCount,
       "twNodeBlacklistTable": twNodeBlacklistTable,
       "twNodeBlacklistEntry": twNodeBlacklistEntry,
       "twNodeBlacklistIndex": twNodeBlacklistIndex,
       "twNodeBlacklistFreqStartKHz": twNodeBlacklistFreqStartKHz,
       "twNodeBlacklistFreqEndKHz": twNodeBlacklistFreqEndKHz,
       "twNodeBlacklistRowStatus": twNodeBlacklistRowStatus,
       "twLink": twLink,
       "twLinkConfigTable": twLinkConfigTable,
       "twLinkConfigEntry": twLinkConfigEntry,
       "twLinkInterfaceId": twLinkInterfaceId,
       "twLinkNumber": twLinkNumber,
       "twLinkAcmEnable": twLinkAcmEnable,
       "twLinkAcmProfile": twLinkAcmProfile,
       "twLinkMcsMin": twLinkMcsMin,
       "twLinkMcsMax": twLinkMcsMax,
       "twLinkMcsFixed": twLinkMcsFixed,
       "twLinkResetCounters": twLinkResetCounters,
       "twLinkAdaptiveMarginEnable": twLinkAdaptiveMarginEnable,
       "twLinkAcmMargin": twLinkAcmMargin,
       "twLinkArqEnable": twLinkArqEnable,
       "twLinkAbicEnable": twLinkAbicEnable,
       "twLinkPhyStatsTable": twLinkPhyStatsTable,
       "twLinkPhyStatsEntry": twLinkPhyStatsEntry,
       "twLinkPhyState": twLinkPhyState,
       "twLinkPhyUpTime": twLinkPhyUpTime,
       "twLinkPhyPathRange": twLinkPhyPathRange,
       "twLinkPhyPathLoss": twLinkPhyPathLoss,
       "twLinkPhySinr": twLinkPhySinr,
       "twLinkPhyTxMcs": twLinkPhyTxMcs,
       "twLinkPhyRxMcs": twLinkPhyRxMcs,
       "twLinkPhyInterferenceDutyCycle": twLinkPhyInterferenceDutyCycle,
       "twLinkPhyInterferenceSignalRatio": twLinkPhyInterferenceSignalRatio,
       "twLinkPhyTxPower": twLinkPhyTxPower,
       "twLinkPhyRxSignalLevel": twLinkPhyRxSignalLevel,
       "twLinkMacStatsTable": twLinkMacStatsTable,
       "twLinkMacStatsEntry": twLinkMacStatsEntry,
       "twLinkMacState": twLinkMacState,
       "twLinkMacUpTime": twLinkMacUpTime,
       "twLinkMacTxCapacity": twLinkMacTxCapacity,
       "twLinkMacRxCapacity": twLinkMacRxCapacity,
       "twLinkPerfTable": twLinkPerfTable,
       "twLinkPerfEntry": twLinkPerfEntry,
       "twLinkTxPackets": twLinkTxPackets,
       "twLinkRxPackets": twLinkRxPackets,
       "twLinkTxBytes": twLinkTxBytes,
       "twLinkRxBytes": twLinkRxBytes,
       "twLinkTxPacketRate": twLinkTxPacketRate,
       "twLinkRxPacketRate": twLinkRxPacketRate,
       "twLinkTxBitRate": twLinkTxBitRate,
       "twLinkRxBitRate": twLinkRxBitRate,
       "twLinkTxLinkUtilization": twLinkTxLinkUtilization,
       "twLinkRxLinkUtilization": twLinkRxLinkUtilization,
       "twLinkRxBlockErrors": twLinkRxBlockErrors,
       "twLinkRxFrameErrors": twLinkRxFrameErrors,
       "twLinkRxBlockErrorRate": twLinkRxBlockErrorRate,
       "twLinkRxFrameErrorRate": twLinkRxFrameErrorRate,
       "twLinkRxPacketErrorRate": twLinkRxPacketErrorRate,
       "twLinkRxBitErrorRate": twLinkRxBitErrorRate,
       "twLinkRxPacketErrors": twLinkRxPacketErrors,
       "twLinkCountersUptime": twLinkCountersUptime,
       "twLinkErrorStatsTable": twLinkErrorStatsTable,
       "twLinkErrorStatsEntry": twLinkErrorStatsEntry,
       "twLinkErroredSeconds": twLinkErroredSeconds,
       "twLinkSeverelyErroredSeconds": twLinkSeverelyErroredSeconds,
       "twLinkBackgroundBlockErrors": twLinkBackgroundBlockErrors,
       "twLinkUnavailableSeconds": twLinkUnavailableSeconds,
       "twLinkErrorStatIntervalType": twLinkErrorStatIntervalType,
       "twLinkErroredSecondsRatio": twLinkErroredSecondsRatio,
       "twLinkSeverelyErroredSecondsRatio": twLinkSeverelyErroredSecondsRatio,
       "twLinkBackgroundBlockErrorRate": twLinkBackgroundBlockErrorRate,
       "twLinkUnavailableSecondsRatio": twLinkUnavailableSecondsRatio,
       "twLinkMcsHistoryTable": twLinkMcsHistoryTable,
       "twLinkMcsHistoryEntry": twLinkMcsHistoryEntry,
       "twLinkMcsHistoryInterval": twLinkMcsHistoryInterval,
       "twLinkMcsHistoryMcsId": twLinkMcsHistoryMcsId,
       "twLinkMcsHistory": twLinkMcsHistory,
       "twLinkSecurityTable": twLinkSecurityTable,
       "twLinkSecurityEntry": twLinkSecurityEntry,
       "twLinkTxEncryptionType": twLinkTxEncryptionType,
       "twLinkTxEncryptionKey": twLinkTxEncryptionKey,
       "twLinkRxEncryptionType": twLinkRxEncryptionType,
       "twLinkRxEncryptionKey": twLinkRxEncryptionKey,
       "twRemoteTable": twRemoteTable,
       "twRemoteEntry": twRemoteEntry,
       "twRemotePhysicalSerialNum": twRemotePhysicalSerialNum,
       "twRemoteMacAddr": twRemoteMacAddr,
       "twRemoteIPAddr": twRemoteIPAddr,
       "twRemoteLinkPhyState": twRemoteLinkPhyState,
       "twRemoteLinkPhyUpTime": twRemoteLinkPhyUpTime,
       "twRemoteLinkPhyPathRange": twRemoteLinkPhyPathRange,
       "twRemoteLinkPhyPathLoss": twRemoteLinkPhyPathLoss,
       "twRemoteLinkPhySinr": twRemoteLinkPhySinr,
       "twRemoteLinkMacState": twRemoteLinkMacState,
       "twRemoteLinkMacUpTime": twRemoteLinkMacUpTime,
       "twRemoteNodeAntStatus": twRemoteNodeAntStatus,
       "twRemoteNodeTxTotalPower": twRemoteNodeTxTotalPower,
       "twRemoteNodeTxHeadroom": twRemoteNodeTxHeadroom,
       "twRemoteLinkCode": twRemoteLinkCode,
       "twRemoteGpsLat": twRemoteGpsLat,
       "twRemoteGpsLon": twRemoteGpsLon,
       "twRemoteGpsElevation": twRemoteGpsElevation,
       "twRemoteLinkRxPacketErrorRate": twRemoteLinkRxPacketErrorRate,
       "twRemoteLinkRxPacketErrors": twRemoteLinkRxPacketErrors,
       "twRemoteLinkRxBlockErrorRate": twRemoteLinkRxBlockErrorRate,
       "twRemoteLinkRxBlockErrors": twRemoteLinkRxBlockErrors,
       "twRemoteLinkRxBitErrorRate": twRemoteLinkRxBitErrorRate,
       "twRemoteNodeRssi": twRemoteNodeRssi,
       "twRemoteSysName": twRemoteSysName,
       "twServices": twServices,
       "twServiceLed": twServiceLed,
       "twServiceUsbEthernet": twServiceUsbEthernet,
       "twServiceUsbWifi": twServiceUsbWifi,
       "twServiceLog": twServiceLog,
       "twServiceLogLevel": twServiceLogLevel,
       "twServiceLogRemoteServer": twServiceLogRemoteServer,
       "twServiceLogComponentLevelTable": twServiceLogComponentLevelTable,
       "twServiceLogComponentLevelEntry": twServiceLogComponentLevelEntry,
       "twServiceLogComponentLevel": twServiceLogComponentLevel,
       "twServiceTrapManagerTable": twServiceTrapManagerTable,
       "twServiceTrapManagerEntry": twServiceTrapManagerEntry,
       "twServiceTrapManagerEntryId": twServiceTrapManagerEntryId,
       "twServiceTrapManagerEntryIp": twServiceTrapManagerEntryIp,
       "twServiceTrapManagerEntryPort": twServiceTrapManagerEntryPort,
       "twServiceTrapManagerCommunity": twServiceTrapManagerCommunity,
       "twServiceMotionTracking": twServiceMotionTracking,
       "twMotionTrackingTilt": twMotionTrackingTilt,
       "twDiagnostics": twDiagnostics,
       "twDiagLinkReset": twDiagLinkReset,
       "twDiagNodeReset": twDiagNodeReset,
       "twDiagResetAllCounters": twDiagResetAllCounters,
       "twDiagRunDiagnostics": twDiagRunDiagnostics,
       "twDiagRunStatus": twDiagRunStatus,
       "twDiagMacReflector": twDiagMacReflector,
       "twDiagMacReflectorEnable": twDiagMacReflectorEnable,
       "twDiagMacReflectorInterface": twDiagMacReflectorInterface,
       "twDiagMacReflectorSrcMac": twDiagMacReflectorSrcMac,
       "twDiagMacReflectorDstMac": twDiagMacReflectorDstMac,
       "twNotifications": twNotifications,
       "twNotificationObjects": twNotificationObjects,
       "twNotifObjIpAddr": twNotifObjIpAddr,
       "twNotifObjSerialNum": twNotifObjSerialNum,
       "twNotifObjSeverity": twNotifObjSeverity,
       "twNotifObjMessage": twNotifObjMessage,
       "twNotifObjCategory": twNotifObjCategory,
       "twNotifObjName": twNotifObjName,
       "twNotifObjState": twNotifObjState,
       "twNotifObjLinkNumber": twNotifObjLinkNumber,
       "twNotifObjSysName": twNotifObjSysName,
       "twNotificationTypes": twNotificationTypes,
       "twNotifBootReason": twNotifBootReason,
       "twNotifGpsLockFailure": twNotifGpsLockFailure,
       "twNotifOverTemperature": twNotifOverTemperature,
       "twNotifLowVoltage": twNotifLowVoltage,
       "twNotifRfLinkDown": twNotifRfLinkDown,
       "twNotifRfLinkUp": twNotifRfLinkUp,
       "twNotifTxCapacity": twNotifTxCapacity,
       "twNotifRxCapacity": twNotifRxCapacity,
       "twNotifPhySinr": twNotifPhySinr,
       "twNotifRxPktError": twNotifRxPktError,
       "twNotifTxPower": twNotifTxPower,
       "twNotifAntStatus": twNotifAntStatus,
       "twNotifConfSave": twNotifConfSave,
       "twAlarmTable": twAlarmTable,
       "twAlarmEntry": twAlarmEntry,
       "twAlarmIndex": twAlarmIndex,
       "twAlarmName": twAlarmName,
       "twAlarmCategory": twAlarmCategory,
       "twAlarmSeverity": twAlarmSeverity,
       "twAlarmState": twAlarmState,
       "twAlarmRisingThreshold": twAlarmRisingThreshold,
       "twAlarmFallingThreshold": twAlarmFallingThreshold,
       "twAlarmTrap": twAlarmTrap,
       "twConformance": twConformance,
       "twGroups": twGroups,
       "twCapabilitiesAll": twCapabilitiesAll,
       "twNotificationsAll": twNotificationsAll,
       "taranawirelessRegids": taranawirelessRegids,
       "taranawirelessCommon": taranawirelessCommon,
       "taranawirelessProducts": taranawirelessProducts,
       "taranawirelessExperimental": taranawirelessExperimental}
)
