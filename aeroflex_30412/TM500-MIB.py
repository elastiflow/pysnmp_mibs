# SNMP MIB module (TM500-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/aeroflex_30412/TM500-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 12:24:32 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class SensorType(TextualConvention, Integer32):
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
        *(("temperature", 0),
          ("voltage", 1),
          ("current", 2),
          ("fan", 3),
          ("other", 4))
    )



class SensorMeasType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("analogue", 0),
          ("digital", 1))
    )



class TenThousandth(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )



# MIB Managed Objects in the order of their OIDs

_AeroflexInc_ObjectIdentity = ObjectIdentity
aeroflexInc = _AeroflexInc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30412)
)
_Tm500_ObjectIdentity = ObjectIdentity
tm500 = _Tm500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30412, 42)
)
_Tm500MibVer_Type = Integer32
_Tm500MibVer_Object = MibScalar
tm500MibVer = _Tm500MibVer_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 1),
    _Tm500MibVer_Type()
)
tm500MibVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tm500MibVer.setStatus("current")
_Inventory_ObjectIdentity = ObjectIdentity
inventory = _Inventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2)
)
_Tm500SerialNumber_Type = DisplayString
_Tm500SerialNumber_Object = MibScalar
tm500SerialNumber = _Tm500SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 1),
    _Tm500SerialNumber_Type()
)
tm500SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tm500SerialNumber.setStatus("current")
_Tm500SoftwareLabel_Type = DisplayString
_Tm500SoftwareLabel_Object = MibScalar
tm500SoftwareLabel = _Tm500SoftwareLabel_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 2),
    _Tm500SoftwareLabel_Type()
)
tm500SoftwareLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tm500SoftwareLabel.setStatus("current")
_Tm500SoftwareBuildDate_Type = DisplayString
_Tm500SoftwareBuildDate_Object = MibScalar
tm500SoftwareBuildDate = _Tm500SoftwareBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 3),
    _Tm500SoftwareBuildDate_Type()
)
tm500SoftwareBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tm500SoftwareBuildDate.setStatus("current")


class _Tm500ChassisType_Type(Integer32):
    """Custom type tm500ChassisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1),
          ("unconfigured", 2))
    )


_Tm500ChassisType_Type.__name__ = "Integer32"
_Tm500ChassisType_Object = MibScalar
tm500ChassisType = _Tm500ChassisType_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 4),
    _Tm500ChassisType_Type()
)
tm500ChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tm500ChassisType.setStatus("current")
_FruNumberOf_Type = Integer32
_FruNumberOf_Object = MibScalar
fruNumberOf = _FruNumberOf_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 10),
    _FruNumberOf_Type()
)
fruNumberOf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruNumberOf.setStatus("current")
_FruTable_Object = MibTable
fruTable = _FruTable_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11)
)
if mibBuilder.loadTexts:
    fruTable.setStatus("current")
_FruEntry_Object = MibTableRow
fruEntry = _FruEntry_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11, 1)
)
fruEntry.setIndexNames(
    (0, "TM500-MIB", "fruTableIdx"),
)
if mibBuilder.loadTexts:
    fruEntry.setStatus("current")


class _FruTableIdx_Type(Integer32):
    """Custom type fruTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FruTableIdx_Type.__name__ = "Integer32"
_FruTableIdx_Object = MibTableColumn
fruTableIdx = _FruTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11, 1, 1),
    _FruTableIdx_Type()
)
fruTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fruTableIdx.setStatus("current")
_FruIpmiSiteType_Type = DisplayString
_FruIpmiSiteType_Object = MibTableColumn
fruIpmiSiteType = _FruIpmiSiteType_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11, 1, 2),
    _FruIpmiSiteType_Type()
)
fruIpmiSiteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruIpmiSiteType.setStatus("current")
_FruModuleType_Type = DisplayString
_FruModuleType_Object = MibTableColumn
fruModuleType = _FruModuleType_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11, 1, 3),
    _FruModuleType_Type()
)
fruModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruModuleType.setStatus("current")
_FruBoardName_Type = DisplayString
_FruBoardName_Object = MibTableColumn
fruBoardName = _FruBoardName_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11, 1, 4),
    _FruBoardName_Type()
)
fruBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBoardName.setStatus("current")
_FruBoardManufacturer_Type = DisplayString
_FruBoardManufacturer_Object = MibTableColumn
fruBoardManufacturer = _FruBoardManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11, 1, 5),
    _FruBoardManufacturer_Type()
)
fruBoardManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBoardManufacturer.setStatus("current")
_FruBoardPartNumber_Type = DisplayString
_FruBoardPartNumber_Object = MibTableColumn
fruBoardPartNumber = _FruBoardPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11, 1, 6),
    _FruBoardPartNumber_Type()
)
fruBoardPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBoardPartNumber.setStatus("current")
_FruBoardSerialNumber_Type = DisplayString
_FruBoardSerialNumber_Object = MibTableColumn
fruBoardSerialNumber = _FruBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11, 1, 7),
    _FruBoardSerialNumber_Type()
)
fruBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBoardSerialNumber.setStatus("current")
_FruProductName_Type = DisplayString
_FruProductName_Object = MibTableColumn
fruProductName = _FruProductName_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11, 1, 8),
    _FruProductName_Type()
)
fruProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruProductName.setStatus("current")
_FruProductManufacturer_Type = DisplayString
_FruProductManufacturer_Object = MibTableColumn
fruProductManufacturer = _FruProductManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11, 1, 9),
    _FruProductManufacturer_Type()
)
fruProductManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruProductManufacturer.setStatus("current")
_FruProductModelNumber_Type = DisplayString
_FruProductModelNumber_Object = MibTableColumn
fruProductModelNumber = _FruProductModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11, 1, 10),
    _FruProductModelNumber_Type()
)
fruProductModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruProductModelNumber.setStatus("current")
_FruProductVersionNumber_Type = DisplayString
_FruProductVersionNumber_Object = MibTableColumn
fruProductVersionNumber = _FruProductVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11, 1, 11),
    _FruProductVersionNumber_Type()
)
fruProductVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruProductVersionNumber.setStatus("current")
_FruProductSerialNumber_Type = DisplayString
_FruProductSerialNumber_Object = MibTableColumn
fruProductSerialNumber = _FruProductSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11, 1, 12),
    _FruProductSerialNumber_Type()
)
fruProductSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruProductSerialNumber.setStatus("current")
_FruProductAssetTag_Type = DisplayString
_FruProductAssetTag_Object = MibTableColumn
fruProductAssetTag = _FruProductAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11, 1, 13),
    _FruProductAssetTag_Type()
)
fruProductAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruProductAssetTag.setStatus("current")
_FruProductFruFileId_Type = DisplayString
_FruProductFruFileId_Object = MibTableColumn
fruProductFruFileId = _FruProductFruFileId_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11, 1, 14),
    _FruProductFruFileId_Type()
)
fruProductFruFileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruProductFruFileId.setStatus("current")
_FruProductCustomFields_Type = DisplayString
_FruProductCustomFields_Object = MibTableColumn
fruProductCustomFields = _FruProductCustomFields_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11, 1, 15),
    _FruProductCustomFields_Type()
)
fruProductCustomFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruProductCustomFields.setStatus("current")
_FruDataNonIpmi_Type = OctetString
_FruDataNonIpmi_Object = MibTableColumn
fruDataNonIpmi = _FruDataNonIpmi_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11, 1, 16),
    _FruDataNonIpmi_Type()
)
fruDataNonIpmi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruDataNonIpmi.setStatus("current")


class _FruNumberOfSensor_Type(Integer32):
    """Custom type fruNumberOfSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FruNumberOfSensor_Type.__name__ = "Integer32"
_FruNumberOfSensor_Object = MibTableColumn
fruNumberOfSensor = _FruNumberOfSensor_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 11, 1, 17),
    _FruNumberOfSensor_Type()
)
fruNumberOfSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruNumberOfSensor.setStatus("current")
_SensorTable_Object = MibTable
sensorTable = _SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 12)
)
if mibBuilder.loadTexts:
    sensorTable.setStatus("current")
_SensorEntry_Object = MibTableRow
sensorEntry = _SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 12, 1)
)
sensorEntry.setIndexNames(
    (0, "TM500-MIB", "fruTableIdx"),
    (0, "TM500-MIB", "sensorTableIdx"),
)
if mibBuilder.loadTexts:
    sensorEntry.setStatus("current")


class _SensorTableIdx_Type(Integer32):
    """Custom type sensorTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SensorTableIdx_Type.__name__ = "Integer32"
_SensorTableIdx_Object = MibTableColumn
sensorTableIdx = _SensorTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 12, 1, 1),
    _SensorTableIdx_Type()
)
sensorTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sensorTableIdx.setStatus("current")
_SensorName_Type = DisplayString
_SensorName_Object = MibTableColumn
sensorName = _SensorName_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 12, 1, 2),
    _SensorName_Type()
)
sensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorName.setStatus("current")
_SensorType_Type = SensorType
_SensorType_Object = MibTableColumn
sensorType = _SensorType_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 12, 1, 3),
    _SensorType_Type()
)
sensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorType.setStatus("current")
_SensorMeasType_Type = SensorMeasType
_SensorMeasType_Object = MibTableColumn
sensorMeasType = _SensorMeasType_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 12, 1, 4),
    _SensorMeasType_Type()
)
sensorMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorMeasType.setStatus("current")
_SensorValue_Type = TenThousandth
_SensorValue_Object = MibTableColumn
sensorValue = _SensorValue_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 12, 1, 5),
    _SensorValue_Type()
)
sensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorValue.setStatus("current")
_SensorUnit_Type = DisplayString
_SensorUnit_Object = MibTableColumn
sensorUnit = _SensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 12, 1, 6),
    _SensorUnit_Type()
)
sensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorUnit.setStatus("current")
_SensorNominal_Type = TenThousandth
_SensorNominal_Object = MibTableColumn
sensorNominal = _SensorNominal_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 12, 1, 7),
    _SensorNominal_Type()
)
sensorNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorNominal.setStatus("current")
_SensorUpperNominal_Type = TenThousandth
_SensorUpperNominal_Object = MibTableColumn
sensorUpperNominal = _SensorUpperNominal_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 12, 1, 8),
    _SensorUpperNominal_Type()
)
sensorUpperNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorUpperNominal.setStatus("current")
_SensorLowerNominal_Type = TenThousandth
_SensorLowerNominal_Object = MibTableColumn
sensorLowerNominal = _SensorLowerNominal_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 12, 1, 9),
    _SensorLowerNominal_Type()
)
sensorLowerNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorLowerNominal.setStatus("current")
_SensorUpperNonrecoverableThreshold_Type = TenThousandth
_SensorUpperNonrecoverableThreshold_Object = MibTableColumn
sensorUpperNonrecoverableThreshold = _SensorUpperNonrecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 12, 1, 10),
    _SensorUpperNonrecoverableThreshold_Type()
)
sensorUpperNonrecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorUpperNonrecoverableThreshold.setStatus("current")
_SensorUpperCriticalThreshold_Type = TenThousandth
_SensorUpperCriticalThreshold_Object = MibTableColumn
sensorUpperCriticalThreshold = _SensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 12, 1, 11),
    _SensorUpperCriticalThreshold_Type()
)
sensorUpperCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorUpperCriticalThreshold.setStatus("current")
_SensorUpperNonCriticalThreshold_Type = TenThousandth
_SensorUpperNonCriticalThreshold_Object = MibTableColumn
sensorUpperNonCriticalThreshold = _SensorUpperNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 12, 1, 12),
    _SensorUpperNonCriticalThreshold_Type()
)
sensorUpperNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorUpperNonCriticalThreshold.setStatus("current")
_SensorLowerNonrecoverableThreshold_Type = TenThousandth
_SensorLowerNonrecoverableThreshold_Object = MibTableColumn
sensorLowerNonrecoverableThreshold = _SensorLowerNonrecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 12, 1, 13),
    _SensorLowerNonrecoverableThreshold_Type()
)
sensorLowerNonrecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorLowerNonrecoverableThreshold.setStatus("current")
_SensorLowerCriticalThreshold_Type = TenThousandth
_SensorLowerCriticalThreshold_Object = MibTableColumn
sensorLowerCriticalThreshold = _SensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 12, 1, 14),
    _SensorLowerCriticalThreshold_Type()
)
sensorLowerCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorLowerCriticalThreshold.setStatus("current")
_SensorLowerNonCriticalThreshold_Type = TenThousandth
_SensorLowerNonCriticalThreshold_Object = MibTableColumn
sensorLowerNonCriticalThreshold = _SensorLowerNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 2, 12, 1, 15),
    _SensorLowerNonCriticalThreshold_Type()
)
sensorLowerNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorLowerNonCriticalThreshold.setStatus("current")
_Utilisation_ObjectIdentity = ObjectIdentity
utilisation = _Utilisation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30412, 42, 3)
)
_CurrentConfiguration_Type = DisplayString
_CurrentConfiguration_Object = MibScalar
currentConfiguration = _CurrentConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 3, 1),
    _CurrentConfiguration_Type()
)
currentConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentConfiguration.setStatus("current")
_UeNumberOf_Type = Unsigned32
_UeNumberOf_Object = MibScalar
ueNumberOf = _UeNumberOf_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 3, 2),
    _UeNumberOf_Type()
)
ueNumberOf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ueNumberOf.setStatus("current")
_UlTrafficCount_Type = Counter64
_UlTrafficCount_Object = MibScalar
ulTrafficCount = _UlTrafficCount_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 3, 3),
    _UlTrafficCount_Type()
)
ulTrafficCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulTrafficCount.setStatus("current")
_DlTrafficCount_Type = Counter64
_DlTrafficCount_Object = MibScalar
dlTrafficCount = _DlTrafficCount_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 3, 4),
    _DlTrafficCount_Type()
)
dlTrafficCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlTrafficCount.setStatus("current")
_LicenseFlagNumberOf_Type = Integer32
_LicenseFlagNumberOf_Object = MibScalar
licenseFlagNumberOf = _LicenseFlagNumberOf_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 3, 10),
    _LicenseFlagNumberOf_Type()
)
licenseFlagNumberOf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFlagNumberOf.setStatus("current")
_LicenseFlagTable_Object = MibTable
licenseFlagTable = _LicenseFlagTable_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 3, 11)
)
if mibBuilder.loadTexts:
    licenseFlagTable.setStatus("current")
_LicenseFlagEntry_Object = MibTableRow
licenseFlagEntry = _LicenseFlagEntry_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 3, 11, 1)
)
licenseFlagEntry.setIndexNames(
    (0, "TM500-MIB", "licenseFlagTableIdx"),
)
if mibBuilder.loadTexts:
    licenseFlagEntry.setStatus("current")


class _LicenseFlagTableIdx_Type(Integer32):
    """Custom type licenseFlagTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_LicenseFlagTableIdx_Type.__name__ = "Integer32"
_LicenseFlagTableIdx_Object = MibTableColumn
licenseFlagTableIdx = _LicenseFlagTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 3, 11, 1, 1),
    _LicenseFlagTableIdx_Type()
)
licenseFlagTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    licenseFlagTableIdx.setStatus("current")
_LicenseFlagName_Type = DisplayString
_LicenseFlagName_Object = MibTableColumn
licenseFlagName = _LicenseFlagName_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 3, 11, 1, 2),
    _LicenseFlagName_Type()
)
licenseFlagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFlagName.setStatus("current")
_LicenseFlagUsed_Type = TruthValue
_LicenseFlagUsed_Object = MibTableColumn
licenseFlagUsed = _LicenseFlagUsed_Object(
    (1, 3, 6, 1, 4, 1, 30412, 42, 3, 11, 1, 3),
    _LicenseFlagUsed_Type()
)
licenseFlagUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFlagUsed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TM500-MIB",
    **{"SensorType": SensorType,
       "SensorMeasType": SensorMeasType,
       "TenThousandth": TenThousandth,
       "aeroflexInc": aeroflexInc,
       "tm500": tm500,
       "tm500MibVer": tm500MibVer,
       "inventory": inventory,
       "tm500SerialNumber": tm500SerialNumber,
       "tm500SoftwareLabel": tm500SoftwareLabel,
       "tm500SoftwareBuildDate": tm500SoftwareBuildDate,
       "tm500ChassisType": tm500ChassisType,
       "fruNumberOf": fruNumberOf,
       "fruTable": fruTable,
       "fruEntry": fruEntry,
       "fruTableIdx": fruTableIdx,
       "fruIpmiSiteType": fruIpmiSiteType,
       "fruModuleType": fruModuleType,
       "fruBoardName": fruBoardName,
       "fruBoardManufacturer": fruBoardManufacturer,
       "fruBoardPartNumber": fruBoardPartNumber,
       "fruBoardSerialNumber": fruBoardSerialNumber,
       "fruProductName": fruProductName,
       "fruProductManufacturer": fruProductManufacturer,
       "fruProductModelNumber": fruProductModelNumber,
       "fruProductVersionNumber": fruProductVersionNumber,
       "fruProductSerialNumber": fruProductSerialNumber,
       "fruProductAssetTag": fruProductAssetTag,
       "fruProductFruFileId": fruProductFruFileId,
       "fruProductCustomFields": fruProductCustomFields,
       "fruDataNonIpmi": fruDataNonIpmi,
       "fruNumberOfSensor": fruNumberOfSensor,
       "sensorTable": sensorTable,
       "sensorEntry": sensorEntry,
       "sensorTableIdx": sensorTableIdx,
       "sensorName": sensorName,
       "sensorType": sensorType,
       "sensorMeasType": sensorMeasType,
       "sensorValue": sensorValue,
       "sensorUnit": sensorUnit,
       "sensorNominal": sensorNominal,
       "sensorUpperNominal": sensorUpperNominal,
       "sensorLowerNominal": sensorLowerNominal,
       "sensorUpperNonrecoverableThreshold": sensorUpperNonrecoverableThreshold,
       "sensorUpperCriticalThreshold": sensorUpperCriticalThreshold,
       "sensorUpperNonCriticalThreshold": sensorUpperNonCriticalThreshold,
       "sensorLowerNonrecoverableThreshold": sensorLowerNonrecoverableThreshold,
       "sensorLowerCriticalThreshold": sensorLowerCriticalThreshold,
       "sensorLowerNonCriticalThreshold": sensorLowerNonCriticalThreshold,
       "utilisation": utilisation,
       "currentConfiguration": currentConfiguration,
       "ueNumberOf": ueNumberOf,
       "ulTrafficCount": ulTrafficCount,
       "dlTrafficCount": dlTrafficCount,
       "licenseFlagNumberOf": licenseFlagNumberOf,
       "licenseFlagTable": licenseFlagTable,
       "licenseFlagEntry": licenseFlagEntry,
       "licenseFlagTableIdx": licenseFlagTableIdx,
       "licenseFlagName": licenseFlagName,
       "licenseFlagUsed": licenseFlagUsed}
)
