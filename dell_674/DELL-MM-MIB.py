# SNMP MIB module (DELL-MM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/dell_674/DELL-MM-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 16:02:30 2025
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions



class DellString(DisplayString):
    """Custom type DellString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )





class DellMmType(Integer32):
    """Custom type DellMmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("mxMM", 3))
    )





class DellStatus(Integer32):
    """Custom type DellStatus based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("ok", 3),
          ("nonCritical", 4),
          ("critical", 5),
          ("nonRecoverable", 6))
    )





class DellPowerReading(DisplayString):
    """Custom type DellPowerReading based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )





class DellPowerIndexRange(Integer32):
    """Custom type DellPowerIndexRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )





class DellPSUIndexRange(Integer32):
    """Custom type DellPSUIndexRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )





class DellPSUCapable(Integer32):
    """Custom type DellPSUCapable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("none", 2),
          ("basic", 3))
    )





class DellTemperatureReading(Integer32):
    """Custom type DellTemperatureReading based on Integer32"""




class DellTimestamp(DisplayString):
    """Custom type DellTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(26, 26),
    )
    fixedLength = 26




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Server3_ObjectIdentity = ObjectIdentity
server3 = _Server3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892)
)
_DmmOutOfBandGroup_ObjectIdentity = ObjectIdentity
dmmOutOfBandGroup = _DmmOutOfBandGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6)
)
_DmmInformationGroup_ObjectIdentity = ObjectIdentity
dmmInformationGroup = _DmmInformationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1)
)
_DmmProductInfoGroup_ObjectIdentity = ObjectIdentity
dmmProductInfoGroup = _DmmProductInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1)
)
_DmmProductName_Type = DellString
_DmmProductName_Object = MibScalar
dmmProductName = _DmmProductName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 1),
    _DmmProductName_Type()
)
dmmProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductName.setStatus("mandatory")
_DmmProductShortName_Type = DellString
_DmmProductShortName_Object = MibScalar
dmmProductShortName = _DmmProductShortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 2),
    _DmmProductShortName_Type()
)
dmmProductShortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductShortName.setStatus("mandatory")
_DmmProductDescription_Type = DellString
_DmmProductDescription_Object = MibScalar
dmmProductDescription = _DmmProductDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 3),
    _DmmProductDescription_Type()
)
dmmProductDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductDescription.setStatus("mandatory")
_DmmProductManufacturer_Type = DellString
_DmmProductManufacturer_Object = MibScalar
dmmProductManufacturer = _DmmProductManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 4),
    _DmmProductManufacturer_Type()
)
dmmProductManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductManufacturer.setStatus("mandatory")
_DmmProductVersion_Type = DellString
_DmmProductVersion_Object = MibScalar
dmmProductVersion = _DmmProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 5),
    _DmmProductVersion_Type()
)
dmmProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductVersion.setStatus("mandatory")
_DmmChassisServiceTag_Type = DellString
_DmmChassisServiceTag_Object = MibScalar
dmmChassisServiceTag = _DmmChassisServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 6),
    _DmmChassisServiceTag_Type()
)
dmmChassisServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmChassisServiceTag.setStatus("mandatory")
_DmmProductURL_Type = DellString
_DmmProductURL_Object = MibScalar
dmmProductURL = _DmmProductURL_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 7),
    _DmmProductURL_Type()
)
dmmProductURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductURL.setStatus("mandatory")
_DmmProductChassisAssetTag_Type = DellString
_DmmProductChassisAssetTag_Object = MibScalar
dmmProductChassisAssetTag = _DmmProductChassisAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 8),
    _DmmProductChassisAssetTag_Type()
)
dmmProductChassisAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductChassisAssetTag.setStatus("mandatory")
_DmmProductChassisName_Type = DellString
_DmmProductChassisName_Object = MibScalar
dmmProductChassisName = _DmmProductChassisName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 9),
    _DmmProductChassisName_Type()
)
dmmProductChassisName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductChassisName.setStatus("mandatory")
_DmmProductType_Type = DellMmType
_DmmProductType_Object = MibScalar
dmmProductType = _DmmProductType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 10),
    _DmmProductType_Type()
)
dmmProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductType.setStatus("mandatory")
_DmmProductChassisDataCenter_Type = DellString
_DmmProductChassisDataCenter_Object = MibScalar
dmmProductChassisDataCenter = _DmmProductChassisDataCenter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 11),
    _DmmProductChassisDataCenter_Type()
)
dmmProductChassisDataCenter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductChassisDataCenter.setStatus("mandatory")
_DmmProductChassisAisle_Type = DellString
_DmmProductChassisAisle_Object = MibScalar
dmmProductChassisAisle = _DmmProductChassisAisle_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 12),
    _DmmProductChassisAisle_Type()
)
dmmProductChassisAisle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductChassisAisle.setStatus("mandatory")
_DmmProductChassisRack_Type = DellString
_DmmProductChassisRack_Object = MibScalar
dmmProductChassisRack = _DmmProductChassisRack_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 13),
    _DmmProductChassisRack_Type()
)
dmmProductChassisRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductChassisRack.setStatus("mandatory")
_DmmProductChassisRackSlot_Type = DellString
_DmmProductChassisRackSlot_Object = MibScalar
dmmProductChassisRackSlot = _DmmProductChassisRackSlot_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 14),
    _DmmProductChassisRackSlot_Type()
)
dmmProductChassisRackSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductChassisRackSlot.setStatus("mandatory")
_DmmProductChassisModel_Type = DellString
_DmmProductChassisModel_Object = MibScalar
dmmProductChassisModel = _DmmProductChassisModel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 15),
    _DmmProductChassisModel_Type()
)
dmmProductChassisModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductChassisModel.setStatus("mandatory")
_DmmProductChassisExpressServiceCode_Type = DellString
_DmmProductChassisExpressServiceCode_Object = MibScalar
dmmProductChassisExpressServiceCode = _DmmProductChassisExpressServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 16),
    _DmmProductChassisExpressServiceCode_Type()
)
dmmProductChassisExpressServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductChassisExpressServiceCode.setStatus("mandatory")
_DmmProductChassisSystemID_Type = Integer32
_DmmProductChassisSystemID_Object = MibScalar
dmmProductChassisSystemID = _DmmProductChassisSystemID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 1, 17),
    _DmmProductChassisSystemID_Type()
)
dmmProductChassisSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmProductChassisSystemID.setStatus("mandatory")
_DmmFirmwareGroup_ObjectIdentity = ObjectIdentity
dmmFirmwareGroup = _DmmFirmwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 2)
)
_DmmFirmwareVersion_Type = DellString
_DmmFirmwareVersion_Object = MibScalar
dmmFirmwareVersion = _DmmFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 2, 1),
    _DmmFirmwareVersion_Type()
)
dmmFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmFirmwareVersion.setStatus("mandatory")
_DmmFirmwareVersion2_Type = DellString
_DmmFirmwareVersion2_Object = MibScalar
dmmFirmwareVersion2 = _DmmFirmwareVersion2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 1, 2, 2),
    _DmmFirmwareVersion2_Type()
)
dmmFirmwareVersion2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmFirmwareVersion2.setStatus("mandatory")
_DmmStatusGroup_ObjectIdentity = ObjectIdentity
dmmStatusGroup = _DmmStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 2)
)
_DmmGlobalSystemStatus_Type = DellStatus
_DmmGlobalSystemStatus_Object = MibScalar
dmmGlobalSystemStatus = _DmmGlobalSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 2, 1),
    _DmmGlobalSystemStatus_Type()
)
dmmGlobalSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmGlobalSystemStatus.setStatus("mandatory")
_DmmChassisStatusGroup_ObjectIdentity = ObjectIdentity
dmmChassisStatusGroup = _DmmChassisStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3)
)
_DmmStatusNowGroup_ObjectIdentity = ObjectIdentity
dmmStatusNowGroup = _DmmStatusNowGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3, 1)
)
_DmmIOMCurrStatus_Type = DellStatus
_DmmIOMCurrStatus_Object = MibScalar
dmmIOMCurrStatus = _DmmIOMCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3, 1, 1),
    _DmmIOMCurrStatus_Type()
)
dmmIOMCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmIOMCurrStatus.setStatus("mandatory")
_DmmRedCurrStatus_Type = DellStatus
_DmmRedCurrStatus_Object = MibScalar
dmmRedCurrStatus = _DmmRedCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3, 1, 2),
    _DmmRedCurrStatus_Type()
)
dmmRedCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmRedCurrStatus.setStatus("mandatory")
_DmmPowerCurrStatus_Type = DellStatus
_DmmPowerCurrStatus_Object = MibScalar
dmmPowerCurrStatus = _DmmPowerCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3, 1, 3),
    _DmmPowerCurrStatus_Type()
)
dmmPowerCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerCurrStatus.setStatus("mandatory")
_DmmFanCurrStatus_Type = DellStatus
_DmmFanCurrStatus_Object = MibScalar
dmmFanCurrStatus = _DmmFanCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3, 1, 4),
    _DmmFanCurrStatus_Type()
)
dmmFanCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmFanCurrStatus.setStatus("mandatory")
_DmmBladeCurrStatus_Type = DellStatus
_DmmBladeCurrStatus_Object = MibScalar
dmmBladeCurrStatus = _DmmBladeCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3, 1, 5),
    _DmmBladeCurrStatus_Type()
)
dmmBladeCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmBladeCurrStatus.setStatus("mandatory")
_DmmTempCurrStatus_Type = DellStatus
_DmmTempCurrStatus_Object = MibScalar
dmmTempCurrStatus = _DmmTempCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3, 1, 6),
    _DmmTempCurrStatus_Type()
)
dmmTempCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmTempCurrStatus.setStatus("mandatory")
_DmmMMCurrStatus_Type = DellStatus
_DmmMMCurrStatus_Object = MibScalar
dmmMMCurrStatus = _DmmMMCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3, 1, 7),
    _DmmMMCurrStatus_Type()
)
dmmMMCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmMMCurrStatus.setStatus("mandatory")
_DmmChassisFrontPanelAmbientTemperature_Type = DellTemperatureReading
_DmmChassisFrontPanelAmbientTemperature_Object = MibScalar
dmmChassisFrontPanelAmbientTemperature = _DmmChassisFrontPanelAmbientTemperature_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 3, 1, 8),
    _DmmChassisFrontPanelAmbientTemperature_Type()
)
dmmChassisFrontPanelAmbientTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmChassisFrontPanelAmbientTemperature.setStatus("mandatory")
_DmmChassisPowerGroup_ObjectIdentity = ObjectIdentity
dmmChassisPowerGroup = _DmmChassisPowerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4)
)
_DmmPowerTable_Object = MibTable
dmmPowerTable = _DmmPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1)
)
if mibBuilder.loadTexts:
    dmmPowerTable.setStatus("mandatory")
_DmmPowerTableEntry_Object = MibTableRow
dmmPowerTableEntry = _DmmPowerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1)
)
dmmPowerTableEntry.setIndexNames(
    (0, "DELL-MM-MIB", "dmmPowerChassisIndex"),
)
if mibBuilder.loadTexts:
    dmmPowerTableEntry.setStatus("mandatory")
_DmmPowerChassisIndex_Type = DellPowerIndexRange
_DmmPowerChassisIndex_Object = MibTableColumn
dmmPowerChassisIndex = _DmmPowerChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1, 1),
    _DmmPowerChassisIndex_Type()
)
dmmPowerChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerChassisIndex.setStatus("mandatory")
_DmmPowerIdlePower_Type = DellPowerReading
_DmmPowerIdlePower_Object = MibTableColumn
dmmPowerIdlePower = _DmmPowerIdlePower_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1, 2),
    _DmmPowerIdlePower_Type()
)
dmmPowerIdlePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerIdlePower.setStatus("mandatory")
_DmmPowerKWhCumulative_Type = DellPowerReading
_DmmPowerKWhCumulative_Object = MibTableColumn
dmmPowerKWhCumulative = _DmmPowerKWhCumulative_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1, 3),
    _DmmPowerKWhCumulative_Type()
)
dmmPowerKWhCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerKWhCumulative.setStatus("mandatory")
_DmmPowerKWhCumulativeTime_Type = DellTimestamp
_DmmPowerKWhCumulativeTime_Object = MibTableColumn
dmmPowerKWhCumulativeTime = _DmmPowerKWhCumulativeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1, 4),
    _DmmPowerKWhCumulativeTime_Type()
)
dmmPowerKWhCumulativeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerKWhCumulativeTime.setStatus("mandatory")
_DmmPowerWattsPeakUsage_Type = DellPowerReading
_DmmPowerWattsPeakUsage_Object = MibTableColumn
dmmPowerWattsPeakUsage = _DmmPowerWattsPeakUsage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1, 5),
    _DmmPowerWattsPeakUsage_Type()
)
dmmPowerWattsPeakUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerWattsPeakUsage.setStatus("mandatory")
_DmmPowerWattsPeakTime_Type = DellTimestamp
_DmmPowerWattsPeakTime_Object = MibTableColumn
dmmPowerWattsPeakTime = _DmmPowerWattsPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1, 6),
    _DmmPowerWattsPeakTime_Type()
)
dmmPowerWattsPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerWattsPeakTime.setStatus("mandatory")
_DmmPowerWattsMinUsage_Type = DellPowerReading
_DmmPowerWattsMinUsage_Object = MibTableColumn
dmmPowerWattsMinUsage = _DmmPowerWattsMinUsage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1, 7),
    _DmmPowerWattsMinUsage_Type()
)
dmmPowerWattsMinUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerWattsMinUsage.setStatus("mandatory")
_DmmPowerWattsMinTime_Type = DellTimestamp
_DmmPowerWattsMinTime_Object = MibTableColumn
dmmPowerWattsMinTime = _DmmPowerWattsMinTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1, 8),
    _DmmPowerWattsMinTime_Type()
)
dmmPowerWattsMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerWattsMinTime.setStatus("mandatory")
_DmmPowerWattsReading_Type = DellPowerReading
_DmmPowerWattsReading_Object = MibTableColumn
dmmPowerWattsReading = _DmmPowerWattsReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 1, 1, 9),
    _DmmPowerWattsReading_Type()
)
dmmPowerWattsReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPowerWattsReading.setStatus("mandatory")
_DmmPSUTable_Object = MibTable
dmmPSUTable = _DmmPSUTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2)
)
if mibBuilder.loadTexts:
    dmmPSUTable.setStatus("mandatory")
_DmmPSUTableEntry_Object = MibTableRow
dmmPSUTableEntry = _DmmPSUTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2, 1)
)
dmmPSUTableEntry.setIndexNames(
    (0, "DELL-MM-MIB", "dmmPSUChassisIndex"),
    (0, "DELL-MM-MIB", "dmmPSUIndex"),
)
if mibBuilder.loadTexts:
    dmmPSUTableEntry.setStatus("mandatory")
_DmmPSUChassisIndex_Type = DellPowerIndexRange
_DmmPSUChassisIndex_Object = MibTableColumn
dmmPSUChassisIndex = _DmmPSUChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2, 1, 1),
    _DmmPSUChassisIndex_Type()
)
dmmPSUChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPSUChassisIndex.setStatus("mandatory")
_DmmPSUIndex_Type = DellPSUIndexRange
_DmmPSUIndex_Object = MibTableColumn
dmmPSUIndex = _DmmPSUIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2, 1, 2),
    _DmmPSUIndex_Type()
)
dmmPSUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPSUIndex.setStatus("mandatory")
_DmmPSULocation_Type = DellString
_DmmPSULocation_Object = MibTableColumn
dmmPSULocation = _DmmPSULocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2, 1, 3),
    _DmmPSULocation_Type()
)
dmmPSULocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPSULocation.setStatus("mandatory")
_DmmPSUState_Type = DellString
_DmmPSUState_Object = MibTableColumn
dmmPSUState = _DmmPSUState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2, 1, 4),
    _DmmPSUState_Type()
)
dmmPSUState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPSUState.setStatus("mandatory")
_DmmPSUType_Type = DellString
_DmmPSUType_Object = MibTableColumn
dmmPSUType = _DmmPSUType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2, 1, 5),
    _DmmPSUType_Type()
)
dmmPSUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPSUType.setStatus("mandatory")
_DmmPSUCapacity_Type = DellPowerReading
_DmmPSUCapacity_Object = MibTableColumn
dmmPSUCapacity = _DmmPSUCapacity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2, 1, 6),
    _DmmPSUCapacity_Type()
)
dmmPSUCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPSUCapacity.setStatus("mandatory")
_DmmPSUVoltage_Type = DellPowerReading
_DmmPSUVoltage_Object = MibTableColumn
dmmPSUVoltage = _DmmPSUVoltage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2, 1, 7),
    _DmmPSUVoltage_Type()
)
dmmPSUVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPSUVoltage.setStatus("mandatory")
_DmmPSUCurrStatus_Type = DellStatus
_DmmPSUCurrStatus_Object = MibTableColumn
dmmPSUCurrStatus = _DmmPSUCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 4, 2, 1, 8),
    _DmmPSUCurrStatus_Type()
)
dmmPSUCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmPSUCurrStatus.setStatus("mandatory")
_DmmChassisAlert2Group_ObjectIdentity = ObjectIdentity
dmmChassisAlert2Group = _DmmChassisAlert2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5)
)
_DmmChassisAlert2Variables_ObjectIdentity = ObjectIdentity
dmmChassisAlert2Variables = _DmmChassisAlert2Variables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 1)
)


class _DmmCA2MessageID_Type(DisplayString):
    """Custom type dmmCA2MessageID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DmmCA2MessageID_Type.__name__ = "DisplayString"
_DmmCA2MessageID_Object = MibScalar
dmmCA2MessageID = _DmmCA2MessageID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 1, 1),
    _DmmCA2MessageID_Type()
)
dmmCA2MessageID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmCA2MessageID.setStatus("mandatory")
_DmmCA2Message_Type = DellString
_DmmCA2Message_Object = MibScalar
dmmCA2Message = _DmmCA2Message_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 1, 2),
    _DmmCA2Message_Type()
)
dmmCA2Message.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmCA2Message.setStatus("mandatory")
_DmmCA2MessageArgs_Type = DellString
_DmmCA2MessageArgs_Object = MibScalar
dmmCA2MessageArgs = _DmmCA2MessageArgs_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 1, 3),
    _DmmCA2MessageArgs_Type()
)
dmmCA2MessageArgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmCA2MessageArgs.setStatus("mandatory")
_DmmCA2AlertStatus_Type = DellStatus
_DmmCA2AlertStatus_Object = MibScalar
dmmCA2AlertStatus = _DmmCA2AlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 1, 4),
    _DmmCA2AlertStatus_Type()
)
dmmCA2AlertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmCA2AlertStatus.setStatus("mandatory")


class _DmmCA2FQDD_Type(DisplayString):
    """Custom type dmmCA2FQDD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DmmCA2FQDD_Type.__name__ = "DisplayString"
_DmmCA2FQDD_Object = MibScalar
dmmCA2FQDD = _DmmCA2FQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 1, 5),
    _DmmCA2FQDD_Type()
)
dmmCA2FQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmCA2FQDD.setStatus("mandatory")
_DmmGenericAlertGroup_ObjectIdentity = ObjectIdentity
dmmGenericAlertGroup = _DmmGenericAlertGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6)
)
_DmmGenericAlertVariables_ObjectIdentity = ObjectIdentity
dmmGenericAlertVariables = _DmmGenericAlertVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 1)
)
_DmmDeviceServiceTag_Type = DellString
_DmmDeviceServiceTag_Object = MibScalar
dmmDeviceServiceTag = _DmmDeviceServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 1, 1),
    _DmmDeviceServiceTag_Type()
)
dmmDeviceServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmmDeviceServiceTag.setStatus("mandatory")

# Managed Objects groups


# Notification objects

alert2FanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2153)
)
alert2FanFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2FanFailure.setStatus(
        ""
    )

alert2FanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2154)
)
alert2FanWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2FanWarning.setStatus(
        ""
    )

alert2FanInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2155)
)
alert2FanInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2FanInformation.setStatus(
        ""
    )

alert2TemperatureProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2161)
)
alert2TemperatureProbeFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2TemperatureProbeFailure.setStatus(
        ""
    )

alert2TemperatureProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2162)
)
alert2TemperatureProbeWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2TemperatureProbeWarning.setStatus(
        ""
    )

alert2TemperatureProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2163)
)
alert2TemperatureProbeNormal.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2TemperatureProbeNormal.setStatus(
        ""
    )

alert2VoltageProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2169)
)
alert2VoltageProbeFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2VoltageProbeFailure.setStatus(
        ""
    )

alert2VoltageProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2170)
)
alert2VoltageProbeWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2VoltageProbeWarning.setStatus(
        ""
    )

alert2VoltageProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2171)
)
alert2VoltageProbeNormal.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2VoltageProbeNormal.setStatus(
        ""
    )

alert2AmperageProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2177)
)
alert2AmperageProbeFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2AmperageProbeFailure.setStatus(
        ""
    )

alert2AmperageProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2178)
)
alert2AmperageProbeWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2AmperageProbeWarning.setStatus(
        ""
    )

alert2AmperageProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2179)
)
alert2AmperageProbeNormal.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2AmperageProbeNormal.setStatus(
        ""
    )

alert2PowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2185)
)
alert2PowerSupplyFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyFailure.setStatus(
        ""
    )

alert2PowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2186)
)
alert2PowerSupplyWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyWarning.setStatus(
        ""
    )

alert2PowerSupplyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2187)
)
alert2PowerSupplyNormal.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyNormal.setStatus(
        ""
    )

alert2BatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2225)
)
alert2BatteryFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2BatteryFailure.setStatus(
        ""
    )

alert2BatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2226)
)
alert2BatteryWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2BatteryWarning.setStatus(
        ""
    )

alert2BatteryNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2227)
)
alert2BatteryNormal.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2BatteryNormal.setStatus(
        ""
    )

alert2LinkStatusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2249)
)
alert2LinkStatusFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2LinkStatusFailure.setStatus(
        ""
    )

alert2LinkStatusWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2250)
)
alert2LinkStatusWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2LinkStatusWarning.setStatus(
        ""
    )

alert2LinkStatusInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2251)
)
alert2LinkStatusInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2LinkStatusInformation.setStatus(
        ""
    )

alert2PowerUsageFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2273)
)
alert2PowerUsageFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageFailure.setStatus(
        ""
    )

alert2PowerUsageWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2274)
)
alert2PowerUsageWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageWarning.setStatus(
        ""
    )

alert2PowerUsageInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2275)
)
alert2PowerUsageInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageInformation.setStatus(
        ""
    )

alert2HardwareConfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2329)
)
alert2HardwareConfigurationFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2HardwareConfigurationFailure.setStatus(
        ""
    )

alert2HardwareConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2330)
)
alert2HardwareConfigurationWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2HardwareConfigurationWarning.setStatus(
        ""
    )

alert2HardwareConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2331)
)
alert2HardwareConfigurationInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2HardwareConfigurationInformation.setStatus(
        ""
    )

alert2SoftwareConfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2337)
)
alert2SoftwareConfigurationFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SoftwareConfigurationFailure.setStatus(
        ""
    )

alert2SoftwareConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2338)
)
alert2SoftwareConfigurationWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SoftwareConfigurationWarning.setStatus(
        ""
    )

alert2SoftwareConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2339)
)
alert2SoftwareConfigurationInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SoftwareConfigurationInformation.setStatus(
        ""
    )

alert2SystemEventLogFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2377)
)
alert2SystemEventLogFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SystemEventLogFailure.setStatus(
        ""
    )

alert2SystemEventLogWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2378)
)
alert2SystemEventLogWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SystemEventLogWarning.setStatus(
        ""
    )

alert2SystemEventLogInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2379)
)
alert2SystemEventLogInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SystemEventLogInformation.setStatus(
        ""
    )

alert2SecurityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2385)
)
alert2SecurityFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SecurityFailure.setStatus(
        ""
    )

alert2SecurityWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2386)
)
alert2SecurityWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SecurityWarning.setStatus(
        ""
    )

alert2SecurityInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2387)
)
alert2SecurityInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SecurityInformation.setStatus(
        ""
    )

alert2CableFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2393)
)
alert2CableFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2CableFailure.setStatus(
        ""
    )

alert2PowerSupplyAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2465)
)
alert2PowerSupplyAbsent.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyAbsent.setStatus(
        ""
    )

alert2RedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2473)
)
alert2RedundancyLost.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2RedundancyLost.setStatus(
        ""
    )

alert2RedundancyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2474)
)
alert2RedundancyDegraded.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2RedundancyDegraded.setStatus(
        ""
    )

alert2RedundancyInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2475)
)
alert2RedundancyInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2RedundancyInformation.setStatus(
        ""
    )

alert2CMCFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2545)
)
alert2CMCFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2CMCFailure.setStatus(
        ""
    )

alert2CMCWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2546)
)
alert2CMCWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2CMCWarning.setStatus(
        ""
    )

alert2IOVirtualizationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2553)
)
alert2IOVirtualizationFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2IOVirtualizationFailure.setStatus(
        ""
    )

alert2IOVirtualizationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2554)
)
alert2IOVirtualizationWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2IOVirtualizationWarning.setStatus(
        ""
    )

alert2IOVirtualizationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 2555)
)
alert2IOVirtualizationInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2IOVirtualizationInformation.setStatus(
        ""
    )

alert2StorageManagementFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4177)
)
alert2StorageManagementFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageManagementFailure.setStatus(
        ""
    )

alert2StorageManagementWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4178)
)
alert2StorageManagementWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageManagementWarning.setStatus(
        ""
    )

alert2StorageManagementInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4179)
)
alert2StorageManagementInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageManagementInformation.setStatus(
        ""
    )

alert2StorageFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4201)
)
alert2StorageFanFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageFanFailure.setStatus(
        ""
    )

alert2StorageFanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4202)
)
alert2StorageFanWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageFanWarning.setStatus(
        ""
    )

alert2StorageFanInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4203)
)
alert2StorageFanInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageFanInformation.setStatus(
        ""
    )

alert2StorageTemperatureProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4209)
)
alert2StorageTemperatureProbeFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageTemperatureProbeFailure.setStatus(
        ""
    )

alert2StorageTemperatureProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4210)
)
alert2StorageTemperatureProbeWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageTemperatureProbeWarning.setStatus(
        ""
    )

alert2StorageTemperatureProbeInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4211)
)
alert2StorageTemperatureProbeInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageTemperatureProbeInformation.setStatus(
        ""
    )

alert2StoragePowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4233)
)
alert2StoragePowerSupplyFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StoragePowerSupplyFailure.setStatus(
        ""
    )

alert2StoragePowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4234)
)
alert2StoragePowerSupplyWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StoragePowerSupplyWarning.setStatus(
        ""
    )

alert2StoragePowerSupplyInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4235)
)
alert2StoragePowerSupplyInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StoragePowerSupplyInformation.setStatus(
        ""
    )

alert2StorageBatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4273)
)
alert2StorageBatteryFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageBatteryFailure.setStatus(
        ""
    )

alert2StorageBatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4274)
)
alert2StorageBatteryWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageBatteryWarning.setStatus(
        ""
    )

alert2StorageBatteryInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4275)
)
alert2StorageBatteryInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageBatteryInformation.setStatus(
        ""
    )

alert2StorageControllerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4329)
)
alert2StorageControllerFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageControllerFailure.setStatus(
        ""
    )

alert2StorageControllerWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4330)
)
alert2StorageControllerWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageControllerWarning.setStatus(
        ""
    )

alert2StorageControllerInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4331)
)
alert2StorageControllerInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageControllerInformation.setStatus(
        ""
    )

alert2StorageEnclosureFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4337)
)
alert2StorageEnclosureFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageEnclosureFailure.setStatus(
        ""
    )

alert2StorageEnclosureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4338)
)
alert2StorageEnclosureWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageEnclosureWarning.setStatus(
        ""
    )

alert2StorageEnclosureInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4339)
)
alert2StorageEnclosureInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageEnclosureInformation.setStatus(
        ""
    )

alert2StoragePhysicalDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4345)
)
alert2StoragePhysicalDiskFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StoragePhysicalDiskFailure.setStatus(
        ""
    )

alert2StoragePhysicalDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4346)
)
alert2StoragePhysicalDiskWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StoragePhysicalDiskWarning.setStatus(
        ""
    )

alert2StoragePhysicalDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4347)
)
alert2StoragePhysicalDiskInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StoragePhysicalDiskInformation.setStatus(
        ""
    )

alert2StorageVirtualDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4353)
)
alert2StorageVirtualDiskFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageVirtualDiskFailure.setStatus(
        ""
    )

alert2StorageVirtualDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4354)
)
alert2StorageVirtualDiskWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageVirtualDiskWarning.setStatus(
        ""
    )

alert2StorageVirtualDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4355)
)
alert2StorageVirtualDiskInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageVirtualDiskInformation.setStatus(
        ""
    )

alert2StorageSecurityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4433)
)
alert2StorageSecurityFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageSecurityFailure.setStatus(
        ""
    )

alert2StorageSecurityWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4434)
)
alert2StorageSecurityWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageSecurityWarning.setStatus(
        ""
    )

alert2StorageSecurityInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 4435)
)
alert2StorageSecurityInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2StorageSecurityInformation.setStatus(
        ""
    )

alert2SoftwareChangeUpdateWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 6314)
)
alert2SoftwareChangeUpdateWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SoftwareChangeUpdateWarning.setStatus(
        ""
    )

alert2PowerSupplyAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8329)
)
alert2PowerSupplyAuditFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyAuditFailure.setStatus(
        ""
    )

alert2PowerSupplyAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8330)
)
alert2PowerSupplyAuditWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyAuditWarning.setStatus(
        ""
    )

alert2SoftwareChangeAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8361)
)
alert2SoftwareChangeAuditFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SoftwareChangeAuditFailure.setStatus(
        ""
    )

alert2PowerUsageAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8417)
)
alert2PowerUsageAuditFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageAuditFailure.setStatus(
        ""
    )

alert2PowerUsageAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8418)
)
alert2PowerUsageAuditWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageAuditWarning.setStatus(
        ""
    )

alert2PowerUsageAuditInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8419)
)
alert2PowerUsageAuditInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageAuditInformation.setStatus(
        ""
    )

alert2LicenseFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8513)
)
alert2LicenseFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2LicenseFailure.setStatus(
        ""
    )

alert2LicenseWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8514)
)
alert2LicenseWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2LicenseWarning.setStatus(
        ""
    )

alert2LicenseInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8515)
)
alert2LicenseInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2LicenseInformation.setStatus(
        ""
    )

alert2PCIDeviceAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8562)
)
alert2PCIDeviceAuditWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PCIDeviceAuditWarning.setStatus(
        ""
    )

alert2CMCAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8689)
)
alert2CMCAuditFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2CMCAuditFailure.setStatus(
        ""
    )

alert2CMCAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8690)
)
alert2CMCAuditWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2CMCAuditWarning.setStatus(
        ""
    )

alert2CMCAuditInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8691)
)
alert2CMCAuditInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2CMCAuditInformation.setStatus(
        ""
    )

alert2IOVirtualizationAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 8698)
)
alert2IOVirtualizationAuditWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2IOVirtualizationAuditWarning.setStatus(
        ""
    )

alert2CMCTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 10395)
)
alert2CMCTestTrap.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2CMCTestTrap.setStatus(
        ""
    )

alert2SWCConfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 10529)
)
alert2SWCConfigurationFailure.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SWCConfigurationFailure.setStatus(
        ""
    )

alert2SWCConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 10530)
)
alert2SWCConfigurationWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2SWCConfigurationWarning.setStatus(
        ""
    )

alert2PCIDeviceConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 10611)
)
alert2PCIDeviceConfigurationInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2PCIDeviceConfigurationInformation.setStatus(
        ""
    )

alert2IOVConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 10746)
)
alert2IOVConfigurationWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2IOVConfigurationWarning.setStatus(
        ""
    )

alert2IOVConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 5, 0, 10747)
)
alert2IOVConfigurationInformation.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmCA2FQDD"),
        ("DELL-MM-MIB", "dmmProductChassisName"),
        ("DELL-MM-MIB", "dmmChassisServiceTag"))
)
if mibBuilder.loadTexts:
    alert2IOVConfigurationInformation.setStatus(
        ""
    )

alertGenericCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 0, 100)
)
alertGenericCritical.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmDeviceServiceTag"))
)
if mibBuilder.loadTexts:
    alertGenericCritical.setStatus(
        ""
    )

alertGenericWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 0, 200)
)
alertGenericWarning.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmDeviceServiceTag"))
)
if mibBuilder.loadTexts:
    alertGenericWarning.setStatus(
        ""
    )

alertGenericNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 0, 300)
)
alertGenericNormal.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmDeviceServiceTag"))
)
if mibBuilder.loadTexts:
    alertGenericNormal.setStatus(
        ""
    )

alertGenericInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 0, 400)
)
alertGenericInformational.setObjects(
      *(("DELL-MM-MIB", "dmmCA2MessageID"),
        ("DELL-MM-MIB", "dmmCA2Message"),
        ("DELL-MM-MIB", "dmmCA2MessageArgs"),
        ("DELL-MM-MIB", "dmmCA2AlertStatus"),
        ("DELL-MM-MIB", "dmmDeviceServiceTag"))
)
if mibBuilder.loadTexts:
    alertGenericInformational.setStatus(
        ""
    )

alertGenericTestTrapEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 6, 6, 0, 500)
)
alertGenericTestTrapEvent.setObjects(
    ("DELL-MM-MIB", "dmmCA2Message")
)
if mibBuilder.loadTexts:
    alertGenericTestTrapEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-MM-MIB",
    **{"DellString": DellString,
       "DellMmType": DellMmType,
       "DellStatus": DellStatus,
       "DellPowerReading": DellPowerReading,
       "DellPowerIndexRange": DellPowerIndexRange,
       "DellPSUIndexRange": DellPSUIndexRange,
       "DellPSUCapable": DellPSUCapable,
       "DellTemperatureReading": DellTemperatureReading,
       "DellTimestamp": DellTimestamp,
       "dell": dell,
       "server3": server3,
       "dmmOutOfBandGroup": dmmOutOfBandGroup,
       "dmmInformationGroup": dmmInformationGroup,
       "dmmProductInfoGroup": dmmProductInfoGroup,
       "dmmProductName": dmmProductName,
       "dmmProductShortName": dmmProductShortName,
       "dmmProductDescription": dmmProductDescription,
       "dmmProductManufacturer": dmmProductManufacturer,
       "dmmProductVersion": dmmProductVersion,
       "dmmChassisServiceTag": dmmChassisServiceTag,
       "dmmProductURL": dmmProductURL,
       "dmmProductChassisAssetTag": dmmProductChassisAssetTag,
       "dmmProductChassisName": dmmProductChassisName,
       "dmmProductType": dmmProductType,
       "dmmProductChassisDataCenter": dmmProductChassisDataCenter,
       "dmmProductChassisAisle": dmmProductChassisAisle,
       "dmmProductChassisRack": dmmProductChassisRack,
       "dmmProductChassisRackSlot": dmmProductChassisRackSlot,
       "dmmProductChassisModel": dmmProductChassisModel,
       "dmmProductChassisExpressServiceCode": dmmProductChassisExpressServiceCode,
       "dmmProductChassisSystemID": dmmProductChassisSystemID,
       "dmmFirmwareGroup": dmmFirmwareGroup,
       "dmmFirmwareVersion": dmmFirmwareVersion,
       "dmmFirmwareVersion2": dmmFirmwareVersion2,
       "dmmStatusGroup": dmmStatusGroup,
       "dmmGlobalSystemStatus": dmmGlobalSystemStatus,
       "dmmChassisStatusGroup": dmmChassisStatusGroup,
       "dmmStatusNowGroup": dmmStatusNowGroup,
       "dmmIOMCurrStatus": dmmIOMCurrStatus,
       "dmmRedCurrStatus": dmmRedCurrStatus,
       "dmmPowerCurrStatus": dmmPowerCurrStatus,
       "dmmFanCurrStatus": dmmFanCurrStatus,
       "dmmBladeCurrStatus": dmmBladeCurrStatus,
       "dmmTempCurrStatus": dmmTempCurrStatus,
       "dmmMMCurrStatus": dmmMMCurrStatus,
       "dmmChassisFrontPanelAmbientTemperature": dmmChassisFrontPanelAmbientTemperature,
       "dmmChassisPowerGroup": dmmChassisPowerGroup,
       "dmmPowerTable": dmmPowerTable,
       "dmmPowerTableEntry": dmmPowerTableEntry,
       "dmmPowerChassisIndex": dmmPowerChassisIndex,
       "dmmPowerIdlePower": dmmPowerIdlePower,
       "dmmPowerKWhCumulative": dmmPowerKWhCumulative,
       "dmmPowerKWhCumulativeTime": dmmPowerKWhCumulativeTime,
       "dmmPowerWattsPeakUsage": dmmPowerWattsPeakUsage,
       "dmmPowerWattsPeakTime": dmmPowerWattsPeakTime,
       "dmmPowerWattsMinUsage": dmmPowerWattsMinUsage,
       "dmmPowerWattsMinTime": dmmPowerWattsMinTime,
       "dmmPowerWattsReading": dmmPowerWattsReading,
       "dmmPSUTable": dmmPSUTable,
       "dmmPSUTableEntry": dmmPSUTableEntry,
       "dmmPSUChassisIndex": dmmPSUChassisIndex,
       "dmmPSUIndex": dmmPSUIndex,
       "dmmPSULocation": dmmPSULocation,
       "dmmPSUState": dmmPSUState,
       "dmmPSUType": dmmPSUType,
       "dmmPSUCapacity": dmmPSUCapacity,
       "dmmPSUVoltage": dmmPSUVoltage,
       "dmmPSUCurrStatus": dmmPSUCurrStatus,
       "dmmChassisAlert2Group": dmmChassisAlert2Group,
       "alert2FanFailure": alert2FanFailure,
       "alert2FanWarning": alert2FanWarning,
       "alert2FanInformation": alert2FanInformation,
       "alert2TemperatureProbeFailure": alert2TemperatureProbeFailure,
       "alert2TemperatureProbeWarning": alert2TemperatureProbeWarning,
       "alert2TemperatureProbeNormal": alert2TemperatureProbeNormal,
       "alert2VoltageProbeFailure": alert2VoltageProbeFailure,
       "alert2VoltageProbeWarning": alert2VoltageProbeWarning,
       "alert2VoltageProbeNormal": alert2VoltageProbeNormal,
       "alert2AmperageProbeFailure": alert2AmperageProbeFailure,
       "alert2AmperageProbeWarning": alert2AmperageProbeWarning,
       "alert2AmperageProbeNormal": alert2AmperageProbeNormal,
       "alert2PowerSupplyFailure": alert2PowerSupplyFailure,
       "alert2PowerSupplyWarning": alert2PowerSupplyWarning,
       "alert2PowerSupplyNormal": alert2PowerSupplyNormal,
       "alert2BatteryFailure": alert2BatteryFailure,
       "alert2BatteryWarning": alert2BatteryWarning,
       "alert2BatteryNormal": alert2BatteryNormal,
       "alert2LinkStatusFailure": alert2LinkStatusFailure,
       "alert2LinkStatusWarning": alert2LinkStatusWarning,
       "alert2LinkStatusInformation": alert2LinkStatusInformation,
       "alert2PowerUsageFailure": alert2PowerUsageFailure,
       "alert2PowerUsageWarning": alert2PowerUsageWarning,
       "alert2PowerUsageInformation": alert2PowerUsageInformation,
       "alert2HardwareConfigurationFailure": alert2HardwareConfigurationFailure,
       "alert2HardwareConfigurationWarning": alert2HardwareConfigurationWarning,
       "alert2HardwareConfigurationInformation": alert2HardwareConfigurationInformation,
       "alert2SoftwareConfigurationFailure": alert2SoftwareConfigurationFailure,
       "alert2SoftwareConfigurationWarning": alert2SoftwareConfigurationWarning,
       "alert2SoftwareConfigurationInformation": alert2SoftwareConfigurationInformation,
       "alert2SystemEventLogFailure": alert2SystemEventLogFailure,
       "alert2SystemEventLogWarning": alert2SystemEventLogWarning,
       "alert2SystemEventLogInformation": alert2SystemEventLogInformation,
       "alert2SecurityFailure": alert2SecurityFailure,
       "alert2SecurityWarning": alert2SecurityWarning,
       "alert2SecurityInformation": alert2SecurityInformation,
       "alert2CableFailure": alert2CableFailure,
       "alert2PowerSupplyAbsent": alert2PowerSupplyAbsent,
       "alert2RedundancyLost": alert2RedundancyLost,
       "alert2RedundancyDegraded": alert2RedundancyDegraded,
       "alert2RedundancyInformation": alert2RedundancyInformation,
       "alert2CMCFailure": alert2CMCFailure,
       "alert2CMCWarning": alert2CMCWarning,
       "alert2IOVirtualizationFailure": alert2IOVirtualizationFailure,
       "alert2IOVirtualizationWarning": alert2IOVirtualizationWarning,
       "alert2IOVirtualizationInformation": alert2IOVirtualizationInformation,
       "alert2StorageManagementFailure": alert2StorageManagementFailure,
       "alert2StorageManagementWarning": alert2StorageManagementWarning,
       "alert2StorageManagementInformation": alert2StorageManagementInformation,
       "alert2StorageFanFailure": alert2StorageFanFailure,
       "alert2StorageFanWarning": alert2StorageFanWarning,
       "alert2StorageFanInformation": alert2StorageFanInformation,
       "alert2StorageTemperatureProbeFailure": alert2StorageTemperatureProbeFailure,
       "alert2StorageTemperatureProbeWarning": alert2StorageTemperatureProbeWarning,
       "alert2StorageTemperatureProbeInformation": alert2StorageTemperatureProbeInformation,
       "alert2StoragePowerSupplyFailure": alert2StoragePowerSupplyFailure,
       "alert2StoragePowerSupplyWarning": alert2StoragePowerSupplyWarning,
       "alert2StoragePowerSupplyInformation": alert2StoragePowerSupplyInformation,
       "alert2StorageBatteryFailure": alert2StorageBatteryFailure,
       "alert2StorageBatteryWarning": alert2StorageBatteryWarning,
       "alert2StorageBatteryInformation": alert2StorageBatteryInformation,
       "alert2StorageControllerFailure": alert2StorageControllerFailure,
       "alert2StorageControllerWarning": alert2StorageControllerWarning,
       "alert2StorageControllerInformation": alert2StorageControllerInformation,
       "alert2StorageEnclosureFailure": alert2StorageEnclosureFailure,
       "alert2StorageEnclosureWarning": alert2StorageEnclosureWarning,
       "alert2StorageEnclosureInformation": alert2StorageEnclosureInformation,
       "alert2StoragePhysicalDiskFailure": alert2StoragePhysicalDiskFailure,
       "alert2StoragePhysicalDiskWarning": alert2StoragePhysicalDiskWarning,
       "alert2StoragePhysicalDiskInformation": alert2StoragePhysicalDiskInformation,
       "alert2StorageVirtualDiskFailure": alert2StorageVirtualDiskFailure,
       "alert2StorageVirtualDiskWarning": alert2StorageVirtualDiskWarning,
       "alert2StorageVirtualDiskInformation": alert2StorageVirtualDiskInformation,
       "alert2StorageSecurityFailure": alert2StorageSecurityFailure,
       "alert2StorageSecurityWarning": alert2StorageSecurityWarning,
       "alert2StorageSecurityInformation": alert2StorageSecurityInformation,
       "alert2SoftwareChangeUpdateWarning": alert2SoftwareChangeUpdateWarning,
       "alert2PowerSupplyAuditFailure": alert2PowerSupplyAuditFailure,
       "alert2PowerSupplyAuditWarning": alert2PowerSupplyAuditWarning,
       "alert2SoftwareChangeAuditFailure": alert2SoftwareChangeAuditFailure,
       "alert2PowerUsageAuditFailure": alert2PowerUsageAuditFailure,
       "alert2PowerUsageAuditWarning": alert2PowerUsageAuditWarning,
       "alert2PowerUsageAuditInformation": alert2PowerUsageAuditInformation,
       "alert2LicenseFailure": alert2LicenseFailure,
       "alert2LicenseWarning": alert2LicenseWarning,
       "alert2LicenseInformation": alert2LicenseInformation,
       "alert2PCIDeviceAuditWarning": alert2PCIDeviceAuditWarning,
       "alert2CMCAuditFailure": alert2CMCAuditFailure,
       "alert2CMCAuditWarning": alert2CMCAuditWarning,
       "alert2CMCAuditInformation": alert2CMCAuditInformation,
       "alert2IOVirtualizationAuditWarning": alert2IOVirtualizationAuditWarning,
       "alert2CMCTestTrap": alert2CMCTestTrap,
       "alert2SWCConfigurationFailure": alert2SWCConfigurationFailure,
       "alert2SWCConfigurationWarning": alert2SWCConfigurationWarning,
       "alert2PCIDeviceConfigurationInformation": alert2PCIDeviceConfigurationInformation,
       "alert2IOVConfigurationWarning": alert2IOVConfigurationWarning,
       "alert2IOVConfigurationInformation": alert2IOVConfigurationInformation,
       "dmmChassisAlert2Variables": dmmChassisAlert2Variables,
       "dmmCA2MessageID": dmmCA2MessageID,
       "dmmCA2Message": dmmCA2Message,
       "dmmCA2MessageArgs": dmmCA2MessageArgs,
       "dmmCA2AlertStatus": dmmCA2AlertStatus,
       "dmmCA2FQDD": dmmCA2FQDD,
       "dmmGenericAlertGroup": dmmGenericAlertGroup,
       "alertGenericCritical": alertGenericCritical,
       "alertGenericWarning": alertGenericWarning,
       "alertGenericNormal": alertGenericNormal,
       "alertGenericInformational": alertGenericInformational,
       "alertGenericTestTrapEvent": alertGenericTestTrapEvent,
       "dmmGenericAlertVariables": dmmGenericAlertVariables,
       "dmmDeviceServiceTag": dmmDeviceServiceTag}
)
