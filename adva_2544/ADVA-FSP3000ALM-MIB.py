# SNMP MIB module (ADVA-FSP3000ALM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/ADVA-FSP3000ALM-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:55 2025
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

(IdentityTranslation,
 TrapAlarmSeverity,
 TrapCounter) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "IdentityTranslation",
    "TrapAlarmSeverity",
    "TrapCounter")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsp3000alm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14)
)
if mibBuilder.loadTexts:
    fsp3000alm.setRevisions(
        ("2015-09-01 00:00",
         "2015-06-01 00:00",
         "2015-04-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Fsp3000almAlarmListType(TextualConvention, Integer32):
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56)
        )
    )
    namedValues = NamedValues(
        *(("alarmTempCPU", 1),
          ("alarmTempBoard1", 2),
          ("alarmTempBoard2Low", 3),
          ("alarmTempBoard2High", 4),
          ("alarmTempLaserLow", 5),
          ("alarmTempLaserHigh", 6),
          ("alarmMonNotRunning", 7),
          ("alarmFpRunning", 8),
          ("alarmFaRunning", 9),
          ("alarmFpMissing", 10),
          ("alarmThresCrossedFast", 11),
          ("alarmThresCrossedMedium", 12),
          ("alarmThresCrossedSlow", 13),
          ("alarmLinkBudgetExceeded", 14),
          ("alarmLinkBudgetNearlyExceeded", 15),
          ("alarmManagementState", 16),
          ("alarmDisabledState", 17),
          ("stateChangedTrap", 18),
          ("objectChangedTrap", 19),
          ("trapsinkCreatedTrap", 20),
          ("trapsinkDeletedTrap", 21),
          ("transient15MinMeasCollected", 22),
          ("transient1DayMeasCollected", 23),
          ("transientFpStarted", 24),
          ("transientFpCompleted", 25),
          ("transientFpFailed", 26),
          ("transientSwMgmtActionStarted", 27),
          ("transientSwMgmtActionCompleted", 28),
          ("transientSwMgmtActionFailed", 29),
          ("transientDbMgmtActionStarted", 30),
          ("transientDbMgmtActionCompleted", 31),
          ("transientDbMgmtActionFailed", 32),
          ("alarmNtpServerUnreachable", 33),
          ("transientFpSaved", 34),
          ("transientMonStarted", 35),
          ("transientMonStopped", 36),
          ("transientOtdrMeasurementStarted", 37),
          ("transientOtdrMeasurementCompleted", 38),
          ("transientOtdrMeasurementFailed", 39),
          ("transientOtdrMeasurementSaved", 40),
          ("transientFaStarted", 41),
          ("transientFaCompleted", 42),
          ("transientFaFailed", 43),
          ("transientFaSaved", 44),
          ("transientInternalError", 45),
          ("alarmRebootRunning", 46),
          ("alarmWarmupRunning", 47),
          ("alarmBadSysStat", 48),
          ("alarmWrongFWVersion", 49),
          ("alarmMonProcNotRunning", 50),
          ("transientFaDeleted", 51),
          ("transientOtdrMeasurementDeleted", 52),
          ("transientOtdrTraceMgmtTransferStarted", 53),
          ("transientOtdrTraceMgmtTransferCompleted", 54),
          ("transientOtdrTraceMgmtTransferFailed", 55),
          ("alarmAlmPackageMismatch", 56))
    )



# MIB Managed Objects in the order of their OIDs

_AdvaMIB_ObjectIdentity = ObjectIdentity
advaMIB = _AdvaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1)
)
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0)
)
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1)
)
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 1, 1)
)
alarmEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "alarmSource"),
    (0, "ADVA-FSP3000ALM-MIB", "alarmType"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")


class _AlarmSource_Type(Integer32):
    """Custom type alarmSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlarmSource_Type.__name__ = "Integer32"
_AlarmSource_Object = MibTableColumn
alarmSource = _AlarmSource_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 1, 1, 1),
    _AlarmSource_Type()
)
alarmSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmSource.setStatus("current")
_AlarmType_Type = Fsp3000almAlarmListType
_AlarmType_Object = MibTableColumn
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 1, 1, 2),
    _AlarmType_Type()
)
alarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmType.setStatus("current")
_AlarmSeverity_Type = TrapAlarmSeverity
_AlarmSeverity_Object = MibTableColumn
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 1, 1, 3),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_AlarmTimeStamp_Type = DateAndTime
_AlarmTimeStamp_Object = MibTableColumn
alarmTimeStamp = _AlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 1, 1, 4),
    _AlarmTimeStamp_Type()
)
alarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTimeStamp.setStatus("current")
_AlarmSeverityTable_Object = MibTable
alarmSeverityTable = _AlarmSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    alarmSeverityTable.setStatus("current")
_AlarmSeverityEntry_Object = MibTableRow
alarmSeverityEntry = _AlarmSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 2, 1)
)
alarmSeverityEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "alarmSource"),
    (0, "ADVA-FSP3000ALM-MIB", "alarmSeverityType"),
)
if mibBuilder.loadTexts:
    alarmSeverityEntry.setStatus("current")
_AlarmSeverityType_Type = Fsp3000almAlarmListType
_AlarmSeverityType_Object = MibTableColumn
alarmSeverityType = _AlarmSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 2, 1, 2),
    _AlarmSeverityType_Type()
)
alarmSeverityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmSeverityType.setStatus("current")
_AlarmSeverityValue_Type = TrapAlarmSeverity
_AlarmSeverityValue_Object = MibTableColumn
alarmSeverityValue = _AlarmSeverityValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 2, 1, 3),
    _AlarmSeverityValue_Type()
)
alarmSeverityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSeverityValue.setStatus("current")
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2)
)
_Shelf_ObjectIdentity = ObjectIdentity
shelf = _Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1)
)
_ShelfUnitName_Type = SnmpAdminString
_ShelfUnitName_Object = MibScalar
shelfUnitName = _ShelfUnitName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 1),
    _ShelfUnitName_Type()
)
shelfUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfUnitName.setStatus("current")
_FirmwarePackageRev_Type = SnmpAdminString
_FirmwarePackageRev_Object = MibScalar
firmwarePackageRev = _FirmwarePackageRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 2),
    _FirmwarePackageRev_Type()
)
firmwarePackageRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwarePackageRev.setStatus("current")
_HardwareRev_Type = SnmpAdminString
_HardwareRev_Object = MibScalar
hardwareRev = _HardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 3),
    _HardwareRev_Type()
)
hardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareRev.setStatus("current")
_FpgaRev_Type = SnmpAdminString
_FpgaRev_Object = MibScalar
fpgaRev = _FpgaRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 4),
    _FpgaRev_Type()
)
fpgaRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpgaRev.setStatus("current")
_SerialNumber_Type = SnmpAdminString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 5),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_PartNumber_Type = SnmpAdminString
_PartNumber_Object = MibScalar
partNumber = _PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 6),
    _PartNumber_Type()
)
partNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partNumber.setStatus("current")
_CleiCode_Type = SnmpAdminString
_CleiCode_Object = MibScalar
cleiCode = _CleiCode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 7),
    _CleiCode_Type()
)
cleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cleiCode.setStatus("current")
_VendorId_Type = SnmpAdminString
_VendorId_Object = MibScalar
vendorId = _VendorId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 8),
    _VendorId_Type()
)
vendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorId.setStatus("current")
_InventoryType_Type = SnmpAdminString
_InventoryType_Object = MibScalar
inventoryType = _InventoryType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 9),
    _InventoryType_Type()
)
inventoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryType.setStatus("current")
_UniversalSerialIdent_Type = SnmpAdminString
_UniversalSerialIdent_Object = MibScalar
universalSerialIdent = _UniversalSerialIdent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 10),
    _UniversalSerialIdent_Type()
)
universalSerialIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    universalSerialIdent.setStatus("current")
_TempCPU_Type = Integer32
_TempCPU_Object = MibScalar
tempCPU = _TempCPU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 11),
    _TempCPU_Type()
)
tempCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempCPU.setStatus("current")
_TresholdMaxTempCPU_Type = Integer32
_TresholdMaxTempCPU_Object = MibScalar
tresholdMaxTempCPU = _TresholdMaxTempCPU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 12),
    _TresholdMaxTempCPU_Type()
)
tresholdMaxTempCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tresholdMaxTempCPU.setStatus("current")
_TempBoard1_Type = Integer32
_TempBoard1_Object = MibScalar
tempBoard1 = _TempBoard1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 13),
    _TempBoard1_Type()
)
tempBoard1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempBoard1.setStatus("current")
_TresholdMaxTempBoard1_Type = Integer32
_TresholdMaxTempBoard1_Object = MibScalar
tresholdMaxTempBoard1 = _TresholdMaxTempBoard1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 14),
    _TresholdMaxTempBoard1_Type()
)
tresholdMaxTempBoard1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tresholdMaxTempBoard1.setStatus("current")
_TempBoard2_Type = Integer32
_TempBoard2_Object = MibScalar
tempBoard2 = _TempBoard2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 15),
    _TempBoard2_Type()
)
tempBoard2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempBoard2.setStatus("current")
_TresholdMinTempBoard2_Type = Integer32
_TresholdMinTempBoard2_Object = MibScalar
tresholdMinTempBoard2 = _TresholdMinTempBoard2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 16),
    _TresholdMinTempBoard2_Type()
)
tresholdMinTempBoard2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tresholdMinTempBoard2.setStatus("current")
_TresholdMaxTempBoard2_Type = Integer32
_TresholdMaxTempBoard2_Object = MibScalar
tresholdMaxTempBoard2 = _TresholdMaxTempBoard2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 17),
    _TresholdMaxTempBoard2_Type()
)
tresholdMaxTempBoard2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tresholdMaxTempBoard2.setStatus("current")
_TempLaser_Type = Integer32
_TempLaser_Object = MibScalar
tempLaser = _TempLaser_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 18),
    _TempLaser_Type()
)
tempLaser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempLaser.setStatus("current")
_TresholdMinTempLaser_Type = Integer32
_TresholdMinTempLaser_Object = MibScalar
tresholdMinTempLaser = _TresholdMinTempLaser_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 19),
    _TresholdMinTempLaser_Type()
)
tresholdMinTempLaser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tresholdMinTempLaser.setStatus("current")
_TresholdMaxTempLaser_Type = Integer32
_TresholdMaxTempLaser_Object = MibScalar
tresholdMaxTempLaser = _TresholdMaxTempLaser_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 20),
    _TresholdMaxTempLaser_Type()
)
tresholdMaxTempLaser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tresholdMaxTempLaser.setStatus("current")


class _AidString_Type(OctetString):
    """Custom type aidString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AidString_Type.__name__ = "OctetString"
_AidString_Object = MibScalar
aidString = _AidString_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 21),
    _AidString_Type()
)
aidString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aidString.setStatus("current")


class _ShelfName_Type(DisplayString):
    """Custom type shelfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ShelfName_Type.__name__ = "DisplayString"
_ShelfName_Object = MibScalar
shelfName = _ShelfName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 22),
    _ShelfName_Type()
)
shelfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfName.setStatus("current")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2, 1)
)
portEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")


class _PortId_Type(Integer32):
    """Custom type portId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PortId_Type.__name__ = "Integer32"
_PortId_Object = MibTableColumn
portId = _PortId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2, 1, 1),
    _PortId_Type()
)
portId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portId.setStatus("current")


class _PortAdminState_Type(Integer32):
    """Custom type portAdminState based on Integer32"""
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
        *(("undefined", 0),
          ("uas", 1),
          ("is", 2),
          ("ains", 3),
          ("mgt", 4),
          ("mt", 5),
          ("dsbld", 6),
          ("pps", 7))
    )


_PortAdminState_Type.__name__ = "Integer32"
_PortAdminState_Object = MibTableColumn
portAdminState = _PortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2, 1, 2),
    _PortAdminState_Type()
)
portAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAdminState.setStatus("current")


class _PortOperState_Type(Integer32):
    """Custom type portOperState based on Integer32"""
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
        *(("undefined", 0),
          ("nr", 1),
          ("anr", 2),
          ("out", 3),
          ("un", 4))
    )


_PortOperState_Type.__name__ = "Integer32"
_PortOperState_Object = MibTableColumn
portOperState = _PortOperState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2, 1, 3),
    _PortOperState_Type()
)
portOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOperState.setStatus("current")


class _PortName_Type(DisplayString):
    """Custom type portName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PortName_Type.__name__ = "DisplayString"
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2, 1, 4),
    _PortName_Type()
)
portName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portName.setStatus("current")
_PortAidString_Type = IdentityTranslation
_PortAidString_Object = MibTableColumn
portAidString = _PortAidString_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2, 1, 5),
    _PortAidString_Type()
)
portAidString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAidString.setStatus("current")
_Measurement_ObjectIdentity = ObjectIdentity
measurement = _Measurement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3)
)
_MeasurementLossTable_Object = MibTable
measurementLossTable = _MeasurementLossTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1)
)
if mibBuilder.loadTexts:
    measurementLossTable.setStatus("current")
_MeasurementLossEntry_Object = MibTableRow
measurementLossEntry = _MeasurementLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1, 1)
)
measurementLossEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "measurementLossIndex"),
)
if mibBuilder.loadTexts:
    measurementLossEntry.setStatus("current")


class _MeasurementLossIndex_Type(Integer32):
    """Custom type measurementLossIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MeasurementLossIndex_Type.__name__ = "Integer32"
_MeasurementLossIndex_Object = MibTableColumn
measurementLossIndex = _MeasurementLossIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1, 1, 1),
    _MeasurementLossIndex_Type()
)
measurementLossIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementLossIndex.setStatus("current")


class _MeasurementLossLinkLoss_Type(Integer32):
    """Custom type measurementLossLinkLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )


_MeasurementLossLinkLoss_Type.__name__ = "Integer32"
_MeasurementLossLinkLoss_Object = MibTableColumn
measurementLossLinkLoss = _MeasurementLossLinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1, 1, 2),
    _MeasurementLossLinkLoss_Type()
)
measurementLossLinkLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementLossLinkLoss.setStatus("current")
_MeasurementLossLinkFaultLoc_Type = Integer32
_MeasurementLossLinkFaultLoc_Object = MibTableColumn
measurementLossLinkFaultLoc = _MeasurementLossLinkFaultLoc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1, 1, 3),
    _MeasurementLossLinkFaultLoc_Type()
)
measurementLossLinkFaultLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementLossLinkFaultLoc.setStatus("current")
_MeasurementLossLinkFaultLocRes_Type = Integer32
_MeasurementLossLinkFaultLocRes_Object = MibTableColumn
measurementLossLinkFaultLocRes = _MeasurementLossLinkFaultLocRes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1, 1, 4),
    _MeasurementLossLinkFaultLocRes_Type()
)
measurementLossLinkFaultLocRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementLossLinkFaultLocRes.setStatus("current")
_MeasurementLossDevFast_Type = Integer32
_MeasurementLossDevFast_Object = MibTableColumn
measurementLossDevFast = _MeasurementLossDevFast_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1, 1, 5),
    _MeasurementLossDevFast_Type()
)
measurementLossDevFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementLossDevFast.setStatus("current")
_MeasurementLossDevMedium_Type = Integer32
_MeasurementLossDevMedium_Object = MibTableColumn
measurementLossDevMedium = _MeasurementLossDevMedium_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1, 1, 6),
    _MeasurementLossDevMedium_Type()
)
measurementLossDevMedium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementLossDevMedium.setStatus("current")
_MeasurementLossDevSlow_Type = Integer32
_MeasurementLossDevSlow_Object = MibTableColumn
measurementLossDevSlow = _MeasurementLossDevSlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1, 1, 7),
    _MeasurementLossDevSlow_Type()
)
measurementLossDevSlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementLossDevSlow.setStatus("current")
_MeasurementLossDataTimestamp_Type = DateAndTime
_MeasurementLossDataTimestamp_Object = MibTableColumn
measurementLossDataTimestamp = _MeasurementLossDataTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1, 1, 8),
    _MeasurementLossDataTimestamp_Type()
)
measurementLossDataTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementLossDataTimestamp.setStatus("current")
_HistMeasLoss15MinTable_Object = MibTable
histMeasLoss15MinTable = _HistMeasLoss15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4)
)
if mibBuilder.loadTexts:
    histMeasLoss15MinTable.setStatus("current")
_HistMeasLoss15MinEntry_Object = MibTableRow
histMeasLoss15MinEntry = _HistMeasLoss15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4, 1)
)
histMeasLoss15MinEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "histMeasLoss15MinNumber"),
)
if mibBuilder.loadTexts:
    histMeasLoss15MinEntry.setStatus("current")


class _HistMeasLoss15MinNumber_Type(Integer32):
    """Custom type histMeasLoss15MinNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_HistMeasLoss15MinNumber_Type.__name__ = "Integer32"
_HistMeasLoss15MinNumber_Object = MibTableColumn
histMeasLoss15MinNumber = _HistMeasLoss15MinNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4, 1, 1),
    _HistMeasLoss15MinNumber_Type()
)
histMeasLoss15MinNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    histMeasLoss15MinNumber.setStatus("current")
_HistMeasLoss15MinLow_Type = Integer32
_HistMeasLoss15MinLow_Object = MibTableColumn
histMeasLoss15MinLow = _HistMeasLoss15MinLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4, 1, 2),
    _HistMeasLoss15MinLow_Type()
)
histMeasLoss15MinLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss15MinLow.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss15MinLow.setUnits("0.1 dBm")
_HistMeasLoss15MinMean_Type = Integer32
_HistMeasLoss15MinMean_Object = MibTableColumn
histMeasLoss15MinMean = _HistMeasLoss15MinMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4, 1, 3),
    _HistMeasLoss15MinMean_Type()
)
histMeasLoss15MinMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss15MinMean.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss15MinMean.setUnits("0.1 dBm")
_HistMeasLoss15MinHigh_Type = Integer32
_HistMeasLoss15MinHigh_Object = MibTableColumn
histMeasLoss15MinHigh = _HistMeasLoss15MinHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4, 1, 4),
    _HistMeasLoss15MinHigh_Type()
)
histMeasLoss15MinHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss15MinHigh.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss15MinHigh.setUnits("0.1 dBm")
_HistMeasLoss15MinValidFlag_Type = TruthValue
_HistMeasLoss15MinValidFlag_Object = MibTableColumn
histMeasLoss15MinValidFlag = _HistMeasLoss15MinValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4, 1, 5),
    _HistMeasLoss15MinValidFlag_Type()
)
histMeasLoss15MinValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss15MinValidFlag.setStatus("current")
_HistMeasLoss15MinTimeStamp_Type = DateAndTime
_HistMeasLoss15MinTimeStamp_Object = MibTableColumn
histMeasLoss15MinTimeStamp = _HistMeasLoss15MinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4, 1, 6),
    _HistMeasLoss15MinTimeStamp_Type()
)
histMeasLoss15MinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss15MinTimeStamp.setStatus("current")
_HistMeasLoss1DayTable_Object = MibTable
histMeasLoss1DayTable = _HistMeasLoss1DayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5)
)
if mibBuilder.loadTexts:
    histMeasLoss1DayTable.setStatus("current")
_HistMeasLoss1DayEntry_Object = MibTableRow
histMeasLoss1DayEntry = _HistMeasLoss1DayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5, 1)
)
histMeasLoss1DayEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "histMeasLoss1DayNumber"),
)
if mibBuilder.loadTexts:
    histMeasLoss1DayEntry.setStatus("current")


class _HistMeasLoss1DayNumber_Type(Integer32):
    """Custom type histMeasLoss1DayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_HistMeasLoss1DayNumber_Type.__name__ = "Integer32"
_HistMeasLoss1DayNumber_Object = MibTableColumn
histMeasLoss1DayNumber = _HistMeasLoss1DayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5, 1, 1),
    _HistMeasLoss1DayNumber_Type()
)
histMeasLoss1DayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    histMeasLoss1DayNumber.setStatus("current")
_HistMeasLoss1DayLow_Type = Integer32
_HistMeasLoss1DayLow_Object = MibTableColumn
histMeasLoss1DayLow = _HistMeasLoss1DayLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5, 1, 2),
    _HistMeasLoss1DayLow_Type()
)
histMeasLoss1DayLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss1DayLow.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss1DayLow.setUnits("0.1 dBm")
_HistMeasLoss1DayMean_Type = Integer32
_HistMeasLoss1DayMean_Object = MibTableColumn
histMeasLoss1DayMean = _HistMeasLoss1DayMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5, 1, 3),
    _HistMeasLoss1DayMean_Type()
)
histMeasLoss1DayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss1DayMean.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss1DayMean.setUnits("0.1 dBm")
_HistMeasLoss1DayHigh_Type = Integer32
_HistMeasLoss1DayHigh_Object = MibTableColumn
histMeasLoss1DayHigh = _HistMeasLoss1DayHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5, 1, 4),
    _HistMeasLoss1DayHigh_Type()
)
histMeasLoss1DayHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss1DayHigh.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss1DayHigh.setUnits("0.1 dBm")
_HistMeasLoss1DayValidFlag_Type = TruthValue
_HistMeasLoss1DayValidFlag_Object = MibTableColumn
histMeasLoss1DayValidFlag = _HistMeasLoss1DayValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5, 1, 5),
    _HistMeasLoss1DayValidFlag_Type()
)
histMeasLoss1DayValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss1DayValidFlag.setStatus("current")
_HistMeasLoss1DayTimeStamp_Type = DateAndTime
_HistMeasLoss1DayTimeStamp_Object = MibTableColumn
histMeasLoss1DayTimeStamp = _HistMeasLoss1DayTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5, 1, 6),
    _HistMeasLoss1DayTimeStamp_Type()
)
histMeasLoss1DayTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss1DayTimeStamp.setStatus("current")
_PortThresTable_Object = MibTable
portThresTable = _PortThresTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6)
)
if mibBuilder.loadTexts:
    portThresTable.setStatus("current")
_PortThresEntry_Object = MibTableRow
portThresEntry = _PortThresEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1)
)
portThresEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
)
if mibBuilder.loadTexts:
    portThresEntry.setStatus("current")
_PortThresDeviationFast_Type = Integer32
_PortThresDeviationFast_Object = MibTableColumn
portThresDeviationFast = _PortThresDeviationFast_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 2),
    _PortThresDeviationFast_Type()
)
portThresDeviationFast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portThresDeviationFast.setStatus("current")
_PortThresDeviationMedium_Type = Integer32
_PortThresDeviationMedium_Object = MibTableColumn
portThresDeviationMedium = _PortThresDeviationMedium_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 3),
    _PortThresDeviationMedium_Type()
)
portThresDeviationMedium.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portThresDeviationMedium.setStatus("current")
_PortThresDeviationSlow_Type = Integer32
_PortThresDeviationSlow_Object = MibTableColumn
portThresDeviationSlow = _PortThresDeviationSlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 4),
    _PortThresDeviationSlow_Type()
)
portThresDeviationSlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portThresDeviationSlow.setStatus("current")
_PortThresBudget_Type = Integer32
_PortThresBudget_Object = MibTableColumn
portThresBudget = _PortThresBudget_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 5),
    _PortThresBudget_Type()
)
portThresBudget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portThresBudget.setStatus("current")
_PortThresCloseToBudget_Type = Integer32
_PortThresCloseToBudget_Object = MibTableColumn
portThresCloseToBudget = _PortThresCloseToBudget_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 6),
    _PortThresCloseToBudget_Type()
)
portThresCloseToBudget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portThresCloseToBudget.setStatus("current")
_PortPeriodLossDevTable_Object = MibTable
portPeriodLossDevTable = _PortPeriodLossDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 7)
)
if mibBuilder.loadTexts:
    portPeriodLossDevTable.setStatus("current")
_PortPeriodLossDevEntry_Object = MibTableRow
portPeriodLossDevEntry = _PortPeriodLossDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 7, 1)
)
portPeriodLossDevEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
)
if mibBuilder.loadTexts:
    portPeriodLossDevEntry.setStatus("current")
_PortPeriodLossDevFast_Type = Integer32
_PortPeriodLossDevFast_Object = MibTableColumn
portPeriodLossDevFast = _PortPeriodLossDevFast_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 7, 1, 1),
    _PortPeriodLossDevFast_Type()
)
portPeriodLossDevFast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPeriodLossDevFast.setStatus("current")
_PortPeriodLossDevMedium_Type = Integer32
_PortPeriodLossDevMedium_Object = MibTableColumn
portPeriodLossDevMedium = _PortPeriodLossDevMedium_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 7, 1, 2),
    _PortPeriodLossDevMedium_Type()
)
portPeriodLossDevMedium.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPeriodLossDevMedium.setStatus("current")
_PortPeriodLossDevSlow_Type = Integer32
_PortPeriodLossDevSlow_Object = MibTableColumn
portPeriodLossDevSlow = _PortPeriodLossDevSlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 7, 1, 3),
    _PortPeriodLossDevSlow_Type()
)
portPeriodLossDevSlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPeriodLossDevSlow.setStatus("current")
_MeasurementFpTable_Object = MibTable
measurementFpTable = _MeasurementFpTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8)
)
if mibBuilder.loadTexts:
    measurementFpTable.setStatus("current")
_MeasurementFpEntry_Object = MibTableRow
measurementFpEntry = _MeasurementFpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1)
)
measurementFpEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "measurementFpIndex"),
)
if mibBuilder.loadTexts:
    measurementFpEntry.setStatus("current")


class _MeasurementFpIndex_Type(Integer32):
    """Custom type measurementFpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MeasurementFpIndex_Type.__name__ = "Integer32"
_MeasurementFpIndex_Object = MibTableColumn
measurementFpIndex = _MeasurementFpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 1),
    _MeasurementFpIndex_Type()
)
measurementFpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    measurementFpIndex.setStatus("current")


class _MeasurementFpRefractiveIndex_Type(Integer32):
    """Custom type measurementFpRefractiveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1400000, 1550000),
    )


_MeasurementFpRefractiveIndex_Type.__name__ = "Integer32"
_MeasurementFpRefractiveIndex_Object = MibTableColumn
measurementFpRefractiveIndex = _MeasurementFpRefractiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 2),
    _MeasurementFpRefractiveIndex_Type()
)
measurementFpRefractiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpRefractiveIndex.setStatus("current")


class _MeasurementFpExternalOffset_Type(Integer32):
    """Custom type measurementFpExternalOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MeasurementFpExternalOffset_Type.__name__ = "Integer32"
_MeasurementFpExternalOffset_Object = MibTableColumn
measurementFpExternalOffset = _MeasurementFpExternalOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 3),
    _MeasurementFpExternalOffset_Type()
)
measurementFpExternalOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpExternalOffset.setStatus("current")


class _MeasurementFpCouplerLoss_Type(Integer32):
    """Custom type measurementFpCouplerLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MeasurementFpCouplerLoss_Type.__name__ = "Integer32"
_MeasurementFpCouplerLoss_Object = MibTableColumn
measurementFpCouplerLoss = _MeasurementFpCouplerLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 4),
    _MeasurementFpCouplerLoss_Type()
)
measurementFpCouplerLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpCouplerLoss.setStatus("current")
_MeasurementFpLinkLoss_Type = Integer32
_MeasurementFpLinkLoss_Object = MibTableColumn
measurementFpLinkLoss = _MeasurementFpLinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 5),
    _MeasurementFpLinkLoss_Type()
)
measurementFpLinkLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpLinkLoss.setStatus("current")
_MeasurementFpLineEndPos_Type = Integer32
_MeasurementFpLineEndPos_Object = MibTableColumn
measurementFpLineEndPos = _MeasurementFpLineEndPos_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 6),
    _MeasurementFpLineEndPos_Type()
)
measurementFpLineEndPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpLineEndPos.setStatus("current")
_MeasurementFpDataTimestamp_Type = DateAndTime
_MeasurementFpDataTimestamp_Object = MibTableColumn
measurementFpDataTimestamp = _MeasurementFpDataTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 7),
    _MeasurementFpDataTimestamp_Type()
)
measurementFpDataTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpDataTimestamp.setStatus("current")
_MeasurementFaTable_Object = MibTable
measurementFaTable = _MeasurementFaTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 9)
)
if mibBuilder.loadTexts:
    measurementFaTable.setStatus("current")
_MeasurementFaEntry_Object = MibTableRow
measurementFaEntry = _MeasurementFaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 9, 1)
)
measurementFaEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "measurementFaIndex"),
)
if mibBuilder.loadTexts:
    measurementFaEntry.setStatus("current")


class _MeasurementFaIndex_Type(Integer32):
    """Custom type measurementFaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MeasurementFaIndex_Type.__name__ = "Integer32"
_MeasurementFaIndex_Object = MibTableColumn
measurementFaIndex = _MeasurementFaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 9, 1, 1),
    _MeasurementFaIndex_Type()
)
measurementFaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    measurementFaIndex.setStatus("current")
_MeasurementFaLinkLoss_Type = Integer32
_MeasurementFaLinkLoss_Object = MibTableColumn
measurementFaLinkLoss = _MeasurementFaLinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 9, 1, 2),
    _MeasurementFaLinkLoss_Type()
)
measurementFaLinkLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFaLinkLoss.setStatus("current")
_MeasurementFaFaultPos_Type = Integer32
_MeasurementFaFaultPos_Object = MibTableColumn
measurementFaFaultPos = _MeasurementFaFaultPos_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 9, 1, 3),
    _MeasurementFaFaultPos_Type()
)
measurementFaFaultPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFaFaultPos.setStatus("current")


class _MeasurementFaDeprecated_Type(Integer32):
    """Custom type measurementFaDeprecated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("no", 1),
          ("yes", 2))
    )


_MeasurementFaDeprecated_Type.__name__ = "Integer32"
_MeasurementFaDeprecated_Object = MibTableColumn
measurementFaDeprecated = _MeasurementFaDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 9, 1, 4),
    _MeasurementFaDeprecated_Type()
)
measurementFaDeprecated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    measurementFaDeprecated.setStatus("current")
_MeasurementFaDataTimestamp_Type = DateAndTime
_MeasurementFaDataTimestamp_Object = MibTableColumn
measurementFaDataTimestamp = _MeasurementFaDataTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 9, 1, 5),
    _MeasurementFaDataTimestamp_Type()
)
measurementFaDataTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFaDataTimestamp.setStatus("current")
_MeasurementOtdrTable_Object = MibTable
measurementOtdrTable = _MeasurementOtdrTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10)
)
if mibBuilder.loadTexts:
    measurementOtdrTable.setStatus("current")
_MeasurementOtdrEntry_Object = MibTableRow
measurementOtdrEntry = _MeasurementOtdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1)
)
measurementOtdrEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "measurementOtdrIndex"),
)
if mibBuilder.loadTexts:
    measurementOtdrEntry.setStatus("current")


class _MeasurementOtdrIndex_Type(Integer32):
    """Custom type measurementOtdrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MeasurementOtdrIndex_Type.__name__ = "Integer32"
_MeasurementOtdrIndex_Object = MibTableColumn
measurementOtdrIndex = _MeasurementOtdrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 1),
    _MeasurementOtdrIndex_Type()
)
measurementOtdrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    measurementOtdrIndex.setStatus("current")


class _MeasurementOtdrLength_Type(Integer32):
    """Custom type measurementOtdrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 35000),
    )


_MeasurementOtdrLength_Type.__name__ = "Integer32"
_MeasurementOtdrLength_Object = MibTableColumn
measurementOtdrLength = _MeasurementOtdrLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 2),
    _MeasurementOtdrLength_Type()
)
measurementOtdrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementOtdrLength.setStatus("current")


class _MeasurementOtdrExternalOffset_Type(Integer32):
    """Custom type measurementOtdrExternalOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MeasurementOtdrExternalOffset_Type.__name__ = "Integer32"
_MeasurementOtdrExternalOffset_Object = MibTableColumn
measurementOtdrExternalOffset = _MeasurementOtdrExternalOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 3),
    _MeasurementOtdrExternalOffset_Type()
)
measurementOtdrExternalOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementOtdrExternalOffset.setStatus("current")


class _MeasurementOtdrRefractiveIndex_Type(Integer32):
    """Custom type measurementOtdrRefractiveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1400000, 1550000),
    )


_MeasurementOtdrRefractiveIndex_Type.__name__ = "Integer32"
_MeasurementOtdrRefractiveIndex_Object = MibTableColumn
measurementOtdrRefractiveIndex = _MeasurementOtdrRefractiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 4),
    _MeasurementOtdrRefractiveIndex_Type()
)
measurementOtdrRefractiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementOtdrRefractiveIndex.setStatus("current")


class _MeasurementOtdrPowerLevel_Type(Integer32):
    """Custom type measurementOtdrPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 2000),
    )


_MeasurementOtdrPowerLevel_Type.__name__ = "Integer32"
_MeasurementOtdrPowerLevel_Object = MibTableColumn
measurementOtdrPowerLevel = _MeasurementOtdrPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 5),
    _MeasurementOtdrPowerLevel_Type()
)
measurementOtdrPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementOtdrPowerLevel.setStatus("current")


class _MeasurementOtdrPulseWidth_Type(Integer32):
    """Custom type measurementOtdrPulseWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 600),
    )


_MeasurementOtdrPulseWidth_Type.__name__ = "Integer32"
_MeasurementOtdrPulseWidth_Object = MibTableColumn
measurementOtdrPulseWidth = _MeasurementOtdrPulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 6),
    _MeasurementOtdrPulseWidth_Type()
)
measurementOtdrPulseWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementOtdrPulseWidth.setStatus("current")


class _MeasurementOtdrAverageRate_Type(Integer32):
    """Custom type measurementOtdrAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MeasurementOtdrAverageRate_Type.__name__ = "Integer32"
_MeasurementOtdrAverageRate_Object = MibTableColumn
measurementOtdrAverageRate = _MeasurementOtdrAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 7),
    _MeasurementOtdrAverageRate_Type()
)
measurementOtdrAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementOtdrAverageRate.setStatus("current")
_MeasurementOtdrDataTimestamp_Type = DateAndTime
_MeasurementOtdrDataTimestamp_Object = MibTableColumn
measurementOtdrDataTimestamp = _MeasurementOtdrDataTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 8),
    _MeasurementOtdrDataTimestamp_Type()
)
measurementOtdrDataTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementOtdrDataTimestamp.setStatus("current")
_EventLogs_ObjectIdentity = ObjectIdentity
eventLogs = _EventLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4)
)
_EventsLogged_Type = Unsigned32
_EventsLogged_Object = MibScalar
eventsLogged = _EventsLogged_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 1),
    _EventsLogged_Type()
)
eventsLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventsLogged.setStatus("current")
_EventLogTable_Object = MibTable
eventLogTable = _EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 2)
)
if mibBuilder.loadTexts:
    eventLogTable.setStatus("current")
_EventLogEntry_Object = MibTableRow
eventLogEntry = _EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 2, 1)
)
eventLogEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "eventLogIndex"),
)
if mibBuilder.loadTexts:
    eventLogEntry.setStatus("current")
_EventLogIndex_Type = Unsigned32
_EventLogIndex_Object = MibTableColumn
eventLogIndex = _EventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 2, 1, 1),
    _EventLogIndex_Type()
)
eventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventLogIndex.setStatus("current")
_EventLogTimeStamp_Type = DateAndTime
_EventLogTimeStamp_Object = MibTableColumn
eventLogTimeStamp = _EventLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 2, 1, 2),
    _EventLogTimeStamp_Type()
)
eventLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogTimeStamp.setStatus("current")
_EventLogNotificationOID_Type = ObjectIdentifier
_EventLogNotificationOID_Object = MibTableColumn
eventLogNotificationOID = _EventLogNotificationOID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 2, 1, 3),
    _EventLogNotificationOID_Type()
)
eventLogNotificationOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogNotificationOID.setStatus("current")
_EventLogIdentityTranslation_Type = IdentityTranslation
_EventLogIdentityTranslation_Object = MibTableColumn
eventLogIdentityTranslation = _EventLogIdentityTranslation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 2, 1, 4),
    _EventLogIdentityTranslation_Type()
)
eventLogIdentityTranslation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogIdentityTranslation.setStatus("current")
_EventLogVarTable_Object = MibTable
eventLogVarTable = _EventLogVarTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3)
)
if mibBuilder.loadTexts:
    eventLogVarTable.setStatus("current")
_EventLogVarEntry_Object = MibTableRow
eventLogVarEntry = _EventLogVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1)
)
eventLogVarEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "eventLogIndex"),
    (0, "ADVA-FSP3000ALM-MIB", "eventLogVarIndex"),
)
if mibBuilder.loadTexts:
    eventLogVarEntry.setStatus("current")
_EventLogVarIndex_Type = Unsigned32
_EventLogVarIndex_Object = MibTableColumn
eventLogVarIndex = _EventLogVarIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1, 1),
    _EventLogVarIndex_Type()
)
eventLogVarIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventLogVarIndex.setStatus("current")
_EventLogVarId_Type = ObjectIdentifier
_EventLogVarId_Object = MibTableColumn
eventLogVarId = _EventLogVarId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1, 2),
    _EventLogVarId_Type()
)
eventLogVarId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogVarId.setStatus("current")


class _EventLogVarType_Type(Integer32):
    """Custom type eventLogVarType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("integer32", 1),
          ("ipAddress", 2),
          ("octetString", 3),
          ("objectId", 4),
          ("counter64", 5),
          ("unsigned32", 7))
    )


_EventLogVarType_Type.__name__ = "Integer32"
_EventLogVarType_Object = MibTableColumn
eventLogVarType = _EventLogVarType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1, 3),
    _EventLogVarType_Type()
)
eventLogVarType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogVarType.setStatus("current")
_EventLogVarInteger32Val_Type = Integer32
_EventLogVarInteger32Val_Object = MibTableColumn
eventLogVarInteger32Val = _EventLogVarInteger32Val_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1, 4),
    _EventLogVarInteger32Val_Type()
)
eventLogVarInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogVarInteger32Val.setStatus("current")
_EventLogVarIpAddressVal_Type = IpAddress
_EventLogVarIpAddressVal_Object = MibTableColumn
eventLogVarIpAddressVal = _EventLogVarIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1, 5),
    _EventLogVarIpAddressVal_Type()
)
eventLogVarIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogVarIpAddressVal.setStatus("current")


class _EventLogVarOctetStringVal_Type(OctetString):
    """Custom type eventLogVarOctetStringVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EventLogVarOctetStringVal_Type.__name__ = "OctetString"
_EventLogVarOctetStringVal_Object = MibTableColumn
eventLogVarOctetStringVal = _EventLogVarOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1, 6),
    _EventLogVarOctetStringVal_Type()
)
eventLogVarOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogVarOctetStringVal.setStatus("current")
_EventLogVarOidVal_Type = ObjectIdentifier
_EventLogVarOidVal_Object = MibTableColumn
eventLogVarOidVal = _EventLogVarOidVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1, 7),
    _EventLogVarOidVal_Type()
)
eventLogVarOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogVarOidVal.setStatus("current")
_EventLogVarCounter64Val_Type = Counter64
_EventLogVarCounter64Val_Object = MibTableColumn
eventLogVarCounter64Val = _EventLogVarCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1, 8),
    _EventLogVarCounter64Val_Type()
)
eventLogVarCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogVarCounter64Val.setStatus("current")
_EventLogVarUnsigned32Val_Type = Unsigned32
_EventLogVarUnsigned32Val_Object = MibTableColumn
eventLogVarUnsigned32Val = _EventLogVarUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1, 10),
    _EventLogVarUnsigned32Val_Type()
)
eventLogVarUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogVarUnsigned32Val.setStatus("current")
_TrapsinkTable_Object = MibTable
trapsinkTable = _TrapsinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 4)
)
if mibBuilder.loadTexts:
    trapsinkTable.setStatus("current")
_TrapsinkEntry_Object = MibTableRow
trapsinkEntry = _TrapsinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 4, 1)
)
trapsinkEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "trapsinkAddress"),
    (0, "ADVA-FSP3000ALM-MIB", "trapsinkPort"),
)
if mibBuilder.loadTexts:
    trapsinkEntry.setStatus("current")
_TrapsinkAddress_Type = IpAddress
_TrapsinkAddress_Object = MibTableColumn
trapsinkAddress = _TrapsinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 4, 1, 1),
    _TrapsinkAddress_Type()
)
trapsinkAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapsinkAddress.setStatus("current")


class _TrapsinkPort_Type(Integer32):
    """Custom type trapsinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrapsinkPort_Type.__name__ = "Integer32"
_TrapsinkPort_Object = MibTableColumn
trapsinkPort = _TrapsinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 4, 1, 2),
    _TrapsinkPort_Type()
)
trapsinkPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapsinkPort.setStatus("current")


class _TrapsinkCommunity_Type(DisplayString):
    """Custom type trapsinkCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TrapsinkCommunity_Type.__name__ = "DisplayString"
_TrapsinkCommunity_Object = MibTableColumn
trapsinkCommunity = _TrapsinkCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 4, 1, 3),
    _TrapsinkCommunity_Type()
)
trapsinkCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapsinkCommunity.setStatus("current")
_TrapsinkRowStatus_Type = RowStatus
_TrapsinkRowStatus_Object = MibTableColumn
trapsinkRowStatus = _TrapsinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 4, 1, 4),
    _TrapsinkRowStatus_Type()
)
trapsinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapsinkRowStatus.setStatus("current")


class _TrapsinkVersion_Type(Integer32):
    """Custom type trapsinkVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_TrapsinkVersion_Type.__name__ = "Integer32"
_TrapsinkVersion_Object = MibTableColumn
trapsinkVersion = _TrapsinkVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 4, 1, 5),
    _TrapsinkVersion_Type()
)
trapsinkVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapsinkVersion.setStatus("current")
_TrapsinkUserName_Type = DisplayString
_TrapsinkUserName_Object = MibTableColumn
trapsinkUserName = _TrapsinkUserName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 4, 1, 6),
    _TrapsinkUserName_Type()
)
trapsinkUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapsinkUserName.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5)
)
_Information_ObjectIdentity = ObjectIdentity
information = _Information_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 1)
)
_SoftwareVersion_Type = SnmpAdminString
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 1, 1),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("current")
_LocalDateAndTime_Type = DateAndTime
_LocalDateAndTime_Object = MibScalar
localDateAndTime = _LocalDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 1, 2),
    _LocalDateAndTime_Type()
)
localDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localDateAndTime.setStatus("current")
_ReleaseNumber_Type = Integer32
_ReleaseNumber_Object = MibScalar
releaseNumber = _ReleaseNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 1, 3),
    _ReleaseNumber_Type()
)
releaseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    releaseNumber.setStatus("current")
_ExpectedSoftwareVersion_Type = SnmpAdminString
_ExpectedSoftwareVersion_Object = MibScalar
expectedSoftwareVersion = _ExpectedSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 1, 4),
    _ExpectedSoftwareVersion_Type()
)
expectedSoftwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expectedSoftwareVersion.setStatus("current")
_IpSettings_ObjectIdentity = ObjectIdentity
ipSettings = _IpSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2)
)
_IpAddress_Type = IpAddress
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 1),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 2),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_Gateway_Type = IpAddress
_Gateway_Object = MibScalar
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 3),
    _Gateway_Type()
)
gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gateway.setStatus("current")
_Dns1_Type = IpAddress
_Dns1_Object = MibScalar
dns1 = _Dns1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 4),
    _Dns1_Type()
)
dns1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dns1.setStatus("current")
_Dns2_Type = IpAddress
_Dns2_Object = MibScalar
dns2 = _Dns2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 5),
    _Dns2_Type()
)
dns2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dns2.setStatus("current")
_SoftwareMgmt_ObjectIdentity = ObjectIdentity
softwareMgmt = _SoftwareMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3)
)
_SoftwareMgmtFileTable_Object = MibTable
softwareMgmtFileTable = _SoftwareMgmtFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 1)
)
if mibBuilder.loadTexts:
    softwareMgmtFileTable.setStatus("current")
_SoftwareMgmtFileEntry_Object = MibTableRow
softwareMgmtFileEntry = _SoftwareMgmtFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 1, 1)
)
softwareMgmtFileEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "softwareMgmtFileIndex"),
)
if mibBuilder.loadTexts:
    softwareMgmtFileEntry.setStatus("current")


class _SoftwareMgmtFileIndex_Type(Integer32):
    """Custom type softwareMgmtFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SoftwareMgmtFileIndex_Type.__name__ = "Integer32"
_SoftwareMgmtFileIndex_Object = MibTableColumn
softwareMgmtFileIndex = _SoftwareMgmtFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 1, 1, 1),
    _SoftwareMgmtFileIndex_Type()
)
softwareMgmtFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    softwareMgmtFileIndex.setStatus("current")
_SoftwareMgmtFileSize_Type = Unsigned32
_SoftwareMgmtFileSize_Object = MibTableColumn
softwareMgmtFileSize = _SoftwareMgmtFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 1, 1, 2),
    _SoftwareMgmtFileSize_Type()
)
softwareMgmtFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareMgmtFileSize.setStatus("current")
if mibBuilder.loadTexts:
    softwareMgmtFileSize.setUnits("Byte")
_SoftwareMgmtFileCreationTime_Type = DateAndTime
_SoftwareMgmtFileCreationTime_Object = MibTableColumn
softwareMgmtFileCreationTime = _SoftwareMgmtFileCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 1, 1, 3),
    _SoftwareMgmtFileCreationTime_Type()
)
softwareMgmtFileCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareMgmtFileCreationTime.setStatus("current")
_SoftwareMgmtFileVersion_Type = SnmpAdminString
_SoftwareMgmtFileVersion_Object = MibTableColumn
softwareMgmtFileVersion = _SoftwareMgmtFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 1, 1, 4),
    _SoftwareMgmtFileVersion_Type()
)
softwareMgmtFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareMgmtFileVersion.setStatus("current")
_SoftwareMgmtFileFileName_Type = SnmpAdminString
_SoftwareMgmtFileFileName_Object = MibTableColumn
softwareMgmtFileFileName = _SoftwareMgmtFileFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 1, 1, 5),
    _SoftwareMgmtFileFileName_Type()
)
softwareMgmtFileFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareMgmtFileFileName.setStatus("current")
_SoftwareMgmtFileRowStatus_Type = RowStatus
_SoftwareMgmtFileRowStatus_Object = MibTableColumn
softwareMgmtFileRowStatus = _SoftwareMgmtFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 1, 1, 6),
    _SoftwareMgmtFileRowStatus_Type()
)
softwareMgmtFileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtFileRowStatus.setStatus("current")


class _SoftwareMgmtRequest_Type(Integer32):
    """Custom type softwareMgmtRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("download", 2),
          ("installActivate", 3),
          ("reboot", 6),
          ("downloadInstallActivate", 8))
    )


_SoftwareMgmtRequest_Type.__name__ = "Integer32"
_SoftwareMgmtRequest_Object = MibScalar
softwareMgmtRequest = _SoftwareMgmtRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 2),
    _SoftwareMgmtRequest_Type()
)
softwareMgmtRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtRequest.setStatus("current")


class _SoftwareMgmtState_Type(Integer32):
    """Custom type softwareMgmtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("downloading", 2),
          ("downloadReadyForInstallation", 3),
          ("installingSoftware", 4),
          ("rebooting", 7),
          ("failure", 8))
    )


_SoftwareMgmtState_Type.__name__ = "Integer32"
_SoftwareMgmtState_Object = MibScalar
softwareMgmtState = _SoftwareMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 3),
    _SoftwareMgmtState_Type()
)
softwareMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareMgmtState.setStatus("current")


class _SoftwareMgmtLastError_Type(Integer32):
    """Custom type softwareMgmtLastError based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("downloadLoginFailed", 2),
          ("downloadFileNotFound", 3),
          ("downloadFileNoAccess", 4),
          ("downloadServerUnreachable", 5),
          ("downloadFailed", 6),
          ("installationFailed", 7),
          ("restoreFailed", 8),
          ("noSpaceLeft", 9),
          ("internalError", 10),
          ("invalidBackupFile", 11),
          ("installationVersionMismatch", 12),
          ("installationFileNotExist", 13),
          ("installationChecksumError", 14))
    )


_SoftwareMgmtLastError_Type.__name__ = "Integer32"
_SoftwareMgmtLastError_Object = MibScalar
softwareMgmtLastError = _SoftwareMgmtLastError_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 4),
    _SoftwareMgmtLastError_Type()
)
softwareMgmtLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareMgmtLastError.setStatus("current")


class _SoftwareMgmtDatabaseUsage_Type(Integer32):
    """Custom type softwareMgmtDatabaseUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("current", 1),
          ("storage", 2),
          ("factoryDefault", 3))
    )


_SoftwareMgmtDatabaseUsage_Type.__name__ = "Integer32"
_SoftwareMgmtDatabaseUsage_Object = MibScalar
softwareMgmtDatabaseUsage = _SoftwareMgmtDatabaseUsage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 5),
    _SoftwareMgmtDatabaseUsage_Type()
)
softwareMgmtDatabaseUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtDatabaseUsage.setStatus("current")
_SoftwareMgmtDatabaseFileName_Type = SnmpAdminString
_SoftwareMgmtDatabaseFileName_Object = MibScalar
softwareMgmtDatabaseFileName = _SoftwareMgmtDatabaseFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 6),
    _SoftwareMgmtDatabaseFileName_Type()
)
softwareMgmtDatabaseFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtDatabaseFileName.setStatus("current")
_SoftwareMgmtServerAddress_Type = IpAddress
_SoftwareMgmtServerAddress_Object = MibScalar
softwareMgmtServerAddress = _SoftwareMgmtServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 7),
    _SoftwareMgmtServerAddress_Type()
)
softwareMgmtServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtServerAddress.setStatus("current")
_SoftwareMgmtServerLogin_Type = SnmpAdminString
_SoftwareMgmtServerLogin_Object = MibScalar
softwareMgmtServerLogin = _SoftwareMgmtServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 8),
    _SoftwareMgmtServerLogin_Type()
)
softwareMgmtServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtServerLogin.setStatus("current")
_SoftwareMgmtServerPasswd_Type = SnmpAdminString
_SoftwareMgmtServerPasswd_Object = MibScalar
softwareMgmtServerPasswd = _SoftwareMgmtServerPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 9),
    _SoftwareMgmtServerPasswd_Type()
)
softwareMgmtServerPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtServerPasswd.setStatus("current")
_SoftwareMgmtServerDirectory_Type = SnmpAdminString
_SoftwareMgmtServerDirectory_Object = MibScalar
softwareMgmtServerDirectory = _SoftwareMgmtServerDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 10),
    _SoftwareMgmtServerDirectory_Type()
)
softwareMgmtServerDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtServerDirectory.setStatus("current")
_SoftwareMgmtFileName_Type = SnmpAdminString
_SoftwareMgmtFileName_Object = MibScalar
softwareMgmtFileName = _SoftwareMgmtFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 11),
    _SoftwareMgmtFileName_Type()
)
softwareMgmtFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtFileName.setStatus("current")


class _SoftwareMgmtTransferProtocol_Type(Integer32):
    """Custom type softwareMgmtTransferProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("scp", 2))
    )


_SoftwareMgmtTransferProtocol_Type.__name__ = "Integer32"
_SoftwareMgmtTransferProtocol_Object = MibScalar
softwareMgmtTransferProtocol = _SoftwareMgmtTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 12),
    _SoftwareMgmtTransferProtocol_Type()
)
softwareMgmtTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtTransferProtocol.setStatus("current")


class _SoftwareMgmtFtpPort_Type(Integer32):
    """Custom type softwareMgmtFtpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SoftwareMgmtFtpPort_Type.__name__ = "Integer32"
_SoftwareMgmtFtpPort_Object = MibScalar
softwareMgmtFtpPort = _SoftwareMgmtFtpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 13),
    _SoftwareMgmtFtpPort_Type()
)
softwareMgmtFtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtFtpPort.setStatus("current")


class _SoftwareMgmtActionProgress_Type(Integer32):
    """Custom type softwareMgmtActionProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_SoftwareMgmtActionProgress_Type.__name__ = "Integer32"
_SoftwareMgmtActionProgress_Object = MibScalar
softwareMgmtActionProgress = _SoftwareMgmtActionProgress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 14),
    _SoftwareMgmtActionProgress_Type()
)
softwareMgmtActionProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareMgmtActionProgress.setStatus("current")
if mibBuilder.loadTexts:
    softwareMgmtActionProgress.setUnits("%")
_DatabaseMgmt_ObjectIdentity = ObjectIdentity
databaseMgmt = _DatabaseMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4)
)
_DatabaseMgmtFileTable_Object = MibTable
databaseMgmtFileTable = _DatabaseMgmtFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 1)
)
if mibBuilder.loadTexts:
    databaseMgmtFileTable.setStatus("current")
_DatabaseMgmtFileEntry_Object = MibTableRow
databaseMgmtFileEntry = _DatabaseMgmtFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 1, 1)
)
databaseMgmtFileEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "databaseMgmtFileIndex"),
)
if mibBuilder.loadTexts:
    databaseMgmtFileEntry.setStatus("current")


class _DatabaseMgmtFileIndex_Type(Integer32):
    """Custom type databaseMgmtFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_DatabaseMgmtFileIndex_Type.__name__ = "Integer32"
_DatabaseMgmtFileIndex_Object = MibTableColumn
databaseMgmtFileIndex = _DatabaseMgmtFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 1, 1, 1),
    _DatabaseMgmtFileIndex_Type()
)
databaseMgmtFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    databaseMgmtFileIndex.setStatus("current")
_DatabaseMgmtFileSize_Type = Unsigned32
_DatabaseMgmtFileSize_Object = MibTableColumn
databaseMgmtFileSize = _DatabaseMgmtFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 1, 1, 2),
    _DatabaseMgmtFileSize_Type()
)
databaseMgmtFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseMgmtFileSize.setStatus("current")
if mibBuilder.loadTexts:
    databaseMgmtFileSize.setUnits("Byte")
_DatabaseMgmtFileCreationTime_Type = DateAndTime
_DatabaseMgmtFileCreationTime_Object = MibTableColumn
databaseMgmtFileCreationTime = _DatabaseMgmtFileCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 1, 1, 3),
    _DatabaseMgmtFileCreationTime_Type()
)
databaseMgmtFileCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseMgmtFileCreationTime.setStatus("current")
_DatabaseMgmtFileVersion_Type = SnmpAdminString
_DatabaseMgmtFileVersion_Object = MibTableColumn
databaseMgmtFileVersion = _DatabaseMgmtFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 1, 1, 4),
    _DatabaseMgmtFileVersion_Type()
)
databaseMgmtFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseMgmtFileVersion.setStatus("current")
_DatabaseMgmtFileFileName_Type = SnmpAdminString
_DatabaseMgmtFileFileName_Object = MibTableColumn
databaseMgmtFileFileName = _DatabaseMgmtFileFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 1, 1, 5),
    _DatabaseMgmtFileFileName_Type()
)
databaseMgmtFileFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseMgmtFileFileName.setStatus("current")
_DatabaseMgmtFileRowStatus_Type = RowStatus
_DatabaseMgmtFileRowStatus_Object = MibTableColumn
databaseMgmtFileRowStatus = _DatabaseMgmtFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 1, 1, 6),
    _DatabaseMgmtFileRowStatus_Type()
)
databaseMgmtFileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtFileRowStatus.setStatus("current")


class _DatabaseMgmtRequest_Type(Integer32):
    """Custom type databaseMgmtRequest based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("download", 2),
          ("upload", 3),
          ("runBackup", 4),
          ("runBackupUpload", 5),
          ("runRestore", 6),
          ("runDownloadRestore", 7),
          ("resetToFactory", 8))
    )


_DatabaseMgmtRequest_Type.__name__ = "Integer32"
_DatabaseMgmtRequest_Object = MibScalar
databaseMgmtRequest = _DatabaseMgmtRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 2),
    _DatabaseMgmtRequest_Type()
)
databaseMgmtRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtRequest.setStatus("current")


class _DatabaseMgmtState_Type(Integer32):
    """Custom type databaseMgmtState based on Integer32"""
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
        *(("idle", 1),
          ("downloading", 2),
          ("uploading", 3),
          ("runningBackup", 4),
          ("runningRestore", 5),
          ("resettingToFactory", 6),
          ("failure", 7))
    )


_DatabaseMgmtState_Type.__name__ = "Integer32"
_DatabaseMgmtState_Object = MibScalar
databaseMgmtState = _DatabaseMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 3),
    _DatabaseMgmtState_Type()
)
databaseMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseMgmtState.setStatus("current")


class _DatabaseMgmtLastError_Type(Integer32):
    """Custom type databaseMgmtLastError based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("transferLoginFailed", 2),
          ("transferFileNotFound", 3),
          ("transferFileNoAccess", 4),
          ("transferServerUnreachable", 5),
          ("transferFailed", 6),
          ("backupFailed", 7),
          ("restoreFailed", 8),
          ("noSpaceLeft", 9),
          ("internalError", 10),
          ("invalidBackupFile", 11))
    )


_DatabaseMgmtLastError_Type.__name__ = "Integer32"
_DatabaseMgmtLastError_Object = MibScalar
databaseMgmtLastError = _DatabaseMgmtLastError_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 4),
    _DatabaseMgmtLastError_Type()
)
databaseMgmtLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseMgmtLastError.setStatus("current")
_DatabaseMgmtServerAddress_Type = IpAddress
_DatabaseMgmtServerAddress_Object = MibScalar
databaseMgmtServerAddress = _DatabaseMgmtServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 5),
    _DatabaseMgmtServerAddress_Type()
)
databaseMgmtServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtServerAddress.setStatus("current")
_DatabaseMgmtServerLogin_Type = SnmpAdminString
_DatabaseMgmtServerLogin_Object = MibScalar
databaseMgmtServerLogin = _DatabaseMgmtServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 6),
    _DatabaseMgmtServerLogin_Type()
)
databaseMgmtServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtServerLogin.setStatus("current")
_DatabaseMgmtServerPasswd_Type = SnmpAdminString
_DatabaseMgmtServerPasswd_Object = MibScalar
databaseMgmtServerPasswd = _DatabaseMgmtServerPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 7),
    _DatabaseMgmtServerPasswd_Type()
)
databaseMgmtServerPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtServerPasswd.setStatus("current")
_DatabaseMgmtServerDirectory_Type = SnmpAdminString
_DatabaseMgmtServerDirectory_Object = MibScalar
databaseMgmtServerDirectory = _DatabaseMgmtServerDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 8),
    _DatabaseMgmtServerDirectory_Type()
)
databaseMgmtServerDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtServerDirectory.setStatus("current")
_DatabaseMgmtFileName_Type = SnmpAdminString
_DatabaseMgmtFileName_Object = MibScalar
databaseMgmtFileName = _DatabaseMgmtFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 9),
    _DatabaseMgmtFileName_Type()
)
databaseMgmtFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtFileName.setStatus("current")


class _DatabaseMgmtTransferProtocol_Type(Integer32):
    """Custom type databaseMgmtTransferProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("scp", 2))
    )


_DatabaseMgmtTransferProtocol_Type.__name__ = "Integer32"
_DatabaseMgmtTransferProtocol_Object = MibScalar
databaseMgmtTransferProtocol = _DatabaseMgmtTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 10),
    _DatabaseMgmtTransferProtocol_Type()
)
databaseMgmtTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtTransferProtocol.setStatus("current")


class _DatabaseMgmtFtpPort_Type(Integer32):
    """Custom type databaseMgmtFtpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DatabaseMgmtFtpPort_Type.__name__ = "Integer32"
_DatabaseMgmtFtpPort_Object = MibScalar
databaseMgmtFtpPort = _DatabaseMgmtFtpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 11),
    _DatabaseMgmtFtpPort_Type()
)
databaseMgmtFtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtFtpPort.setStatus("current")


class _DatabaseMgmtActionProgress_Type(Integer32):
    """Custom type databaseMgmtActionProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_DatabaseMgmtActionProgress_Type.__name__ = "Integer32"
_DatabaseMgmtActionProgress_Object = MibScalar
databaseMgmtActionProgress = _DatabaseMgmtActionProgress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 12),
    _DatabaseMgmtActionProgress_Type()
)
databaseMgmtActionProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseMgmtActionProgress.setStatus("current")
if mibBuilder.loadTexts:
    databaseMgmtActionProgress.setUnits("%")
_NtpMgmt_ObjectIdentity = ObjectIdentity
ntpMgmt = _NtpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 5)
)


class _NtpClientConfig_Type(Integer32):
    """Custom type ntpClientConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NtpClientConfig_Type.__name__ = "Integer32"
_NtpClientConfig_Object = MibScalar
ntpClientConfig = _NtpClientConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 5, 1),
    _NtpClientConfig_Type()
)
ntpClientConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpClientConfig.setStatus("current")
_NtpServerName_Type = DisplayString
_NtpServerName_Object = MibScalar
ntpServerName = _NtpServerName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 5, 2),
    _NtpServerName_Type()
)
ntpServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServerName.setStatus("current")
_GeneralSettings_ObjectIdentity = ObjectIdentity
generalSettings = _GeneralSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6)
)


class _OperationMode_Type(Integer32):
    """Custom type operationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("controller", 2))
    )


_OperationMode_Type.__name__ = "Integer32"
_OperationMode_Object = MibScalar
operationMode = _OperationMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 1),
    _OperationMode_Type()
)
operationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operationMode.setStatus("current")
_Maintain_ObjectIdentity = ObjectIdentity
maintain = _Maintain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6)
)
_MaintainTable_Object = MibTable
maintainTable = _MaintainTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1)
)
if mibBuilder.loadTexts:
    maintainTable.setStatus("current")
_MaintainEntry_Object = MibTableRow
maintainEntry = _MaintainEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1)
)
maintainEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
)
if mibBuilder.loadTexts:
    maintainEntry.setStatus("current")


class _MaintainOperationRequest_Type(Integer32):
    """Custom type maintainOperationRequest based on Integer32"""
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
        *(("none", 1),
          ("runFingerprintGeneration", 2),
          ("runOtdrMeasurement", 3),
          ("runFaultAnalysis", 4))
    )


_MaintainOperationRequest_Type.__name__ = "Integer32"
_MaintainOperationRequest_Object = MibTableColumn
maintainOperationRequest = _MaintainOperationRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 1),
    _MaintainOperationRequest_Type()
)
maintainOperationRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationRequest.setStatus("current")


class _MaintainOperationRefractiveIndex_Type(Integer32):
    """Custom type maintainOperationRefractiveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1400000, 1550000),
    )


_MaintainOperationRefractiveIndex_Type.__name__ = "Integer32"
_MaintainOperationRefractiveIndex_Object = MibTableColumn
maintainOperationRefractiveIndex = _MaintainOperationRefractiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 2),
    _MaintainOperationRefractiveIndex_Type()
)
maintainOperationRefractiveIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationRefractiveIndex.setStatus("current")


class _MaintainOperationExternalOffset_Type(Integer32):
    """Custom type maintainOperationExternalOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaintainOperationExternalOffset_Type.__name__ = "Integer32"
_MaintainOperationExternalOffset_Object = MibTableColumn
maintainOperationExternalOffset = _MaintainOperationExternalOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 3),
    _MaintainOperationExternalOffset_Type()
)
maintainOperationExternalOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationExternalOffset.setStatus("current")


class _MaintainOperationCouplerLoss_Type(Integer32):
    """Custom type maintainOperationCouplerLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaintainOperationCouplerLoss_Type.__name__ = "Integer32"
_MaintainOperationCouplerLoss_Object = MibTableColumn
maintainOperationCouplerLoss = _MaintainOperationCouplerLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 4),
    _MaintainOperationCouplerLoss_Type()
)
maintainOperationCouplerLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationCouplerLoss.setStatus("current")


class _MaintainOperationOtdrLength_Type(Integer32):
    """Custom type maintainOperationOtdrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 35000),
    )


_MaintainOperationOtdrLength_Type.__name__ = "Integer32"
_MaintainOperationOtdrLength_Object = MibTableColumn
maintainOperationOtdrLength = _MaintainOperationOtdrLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 5),
    _MaintainOperationOtdrLength_Type()
)
maintainOperationOtdrLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationOtdrLength.setStatus("current")


class _MaintainOperationOtdrPowerLevel_Type(Integer32):
    """Custom type maintainOperationOtdrPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 2000),
    )


_MaintainOperationOtdrPowerLevel_Type.__name__ = "Integer32"
_MaintainOperationOtdrPowerLevel_Object = MibTableColumn
maintainOperationOtdrPowerLevel = _MaintainOperationOtdrPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 6),
    _MaintainOperationOtdrPowerLevel_Type()
)
maintainOperationOtdrPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationOtdrPowerLevel.setStatus("current")


class _MaintainOperationOtdrPulseWidth_Type(Integer32):
    """Custom type maintainOperationOtdrPulseWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 600),
    )


_MaintainOperationOtdrPulseWidth_Type.__name__ = "Integer32"
_MaintainOperationOtdrPulseWidth_Object = MibTableColumn
maintainOperationOtdrPulseWidth = _MaintainOperationOtdrPulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 7),
    _MaintainOperationOtdrPulseWidth_Type()
)
maintainOperationOtdrPulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationOtdrPulseWidth.setStatus("current")


class _MaintainOperationOtdrAverageRate_Type(Integer32):
    """Custom type maintainOperationOtdrAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MaintainOperationOtdrAverageRate_Type.__name__ = "Integer32"
_MaintainOperationOtdrAverageRate_Object = MibTableColumn
maintainOperationOtdrAverageRate = _MaintainOperationOtdrAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 8),
    _MaintainOperationOtdrAverageRate_Type()
)
maintainOperationOtdrAverageRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationOtdrAverageRate.setStatus("current")


class _MaintainOperationState_Type(Integer32):
    """Custom type maintainOperationState based on Integer32"""
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
        *(("idle", 1),
          ("waiting", 2),
          ("fingerprintGenerationRunning", 3),
          ("otdrMeasurementRunning", 4),
          ("faultAnalysisRunning", 5),
          ("failure", 6))
    )


_MaintainOperationState_Type.__name__ = "Integer32"
_MaintainOperationState_Object = MibTableColumn
maintainOperationState = _MaintainOperationState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 9),
    _MaintainOperationState_Type()
)
maintainOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintainOperationState.setStatus("current")


class _MaintainOperationLastError_Type(Integer32):
    """Custom type maintainOperationLastError based on Integer32"""
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
        *(("noError", 1),
          ("reflectionPointNotFound", 2),
          ("noSpaceLeft", 3),
          ("adminStateChanged", 4),
          ("internalError", 5))
    )


_MaintainOperationLastError_Type.__name__ = "Integer32"
_MaintainOperationLastError_Object = MibTableColumn
maintainOperationLastError = _MaintainOperationLastError_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 10),
    _MaintainOperationLastError_Type()
)
maintainOperationLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintainOperationLastError.setStatus("current")
_OtdrTraceMgmt_ObjectIdentity = ObjectIdentity
otdrTraceMgmt = _OtdrTraceMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7)
)
_OtdrTraceMgmtTable_Object = MibTable
otdrTraceMgmtTable = _OtdrTraceMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1)
)
if mibBuilder.loadTexts:
    otdrTraceMgmtTable.setStatus("current")
_OtdrTraceMgmtEntry_Object = MibTableRow
otdrTraceMgmtEntry = _OtdrTraceMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1)
)
otdrTraceMgmtEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
)
if mibBuilder.loadTexts:
    otdrTraceMgmtEntry.setStatus("current")


class _OtdrTraceMgmtRequest_Type(Integer32):
    """Custom type otdrTraceMgmtRequest based on Integer32"""
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
        *(("none", 1),
          ("exportOmTrace", 2),
          ("exportFaTrace", 3),
          ("exportFpTrace", 4))
    )


_OtdrTraceMgmtRequest_Type.__name__ = "Integer32"
_OtdrTraceMgmtRequest_Object = MibTableColumn
otdrTraceMgmtRequest = _OtdrTraceMgmtRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 1),
    _OtdrTraceMgmtRequest_Type()
)
otdrTraceMgmtRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtRequest.setStatus("current")


class _OtdrTraceMgmtState_Type(Integer32):
    """Custom type otdrTraceMgmtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("exportingOmTrace", 5),
          ("exportingFaTrace", 6),
          ("exportingFpTrace", 7),
          ("failure", 8))
    )


_OtdrTraceMgmtState_Type.__name__ = "Integer32"
_OtdrTraceMgmtState_Object = MibTableColumn
otdrTraceMgmtState = _OtdrTraceMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 2),
    _OtdrTraceMgmtState_Type()
)
otdrTraceMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTraceMgmtState.setStatus("current")


class _OtdrTraceMgmtLastError_Type(Integer32):
    """Custom type otdrTraceMgmtLastError based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("transferLoginFailed", 2),
          ("transferFileNotFound", 3),
          ("transferFileNoAccess", 4),
          ("transferServerUnreachable", 5),
          ("transferFailed", 6),
          ("missingOtdrTrace", 7),
          ("wrongOtdrTraceIndex", 8),
          ("internalError", 9),
          ("noSpaceLeft", 10))
    )


_OtdrTraceMgmtLastError_Type.__name__ = "Integer32"
_OtdrTraceMgmtLastError_Object = MibTableColumn
otdrTraceMgmtLastError = _OtdrTraceMgmtLastError_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 3),
    _OtdrTraceMgmtLastError_Type()
)
otdrTraceMgmtLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTraceMgmtLastError.setStatus("current")
_OtdrTraceMgmtServerAddress_Type = IpAddress
_OtdrTraceMgmtServerAddress_Object = MibTableColumn
otdrTraceMgmtServerAddress = _OtdrTraceMgmtServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 4),
    _OtdrTraceMgmtServerAddress_Type()
)
otdrTraceMgmtServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtServerAddress.setStatus("current")
_OtdrTraceMgmtServerLogin_Type = SnmpAdminString
_OtdrTraceMgmtServerLogin_Object = MibTableColumn
otdrTraceMgmtServerLogin = _OtdrTraceMgmtServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 5),
    _OtdrTraceMgmtServerLogin_Type()
)
otdrTraceMgmtServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtServerLogin.setStatus("current")
_OtdrTraceMgmtServerPasswd_Type = SnmpAdminString
_OtdrTraceMgmtServerPasswd_Object = MibTableColumn
otdrTraceMgmtServerPasswd = _OtdrTraceMgmtServerPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 6),
    _OtdrTraceMgmtServerPasswd_Type()
)
otdrTraceMgmtServerPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtServerPasswd.setStatus("current")
_OtdrTraceMgmtServerDirectory_Type = SnmpAdminString
_OtdrTraceMgmtServerDirectory_Object = MibTableColumn
otdrTraceMgmtServerDirectory = _OtdrTraceMgmtServerDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 7),
    _OtdrTraceMgmtServerDirectory_Type()
)
otdrTraceMgmtServerDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtServerDirectory.setStatus("current")
_OtdrTraceMgmtFileName_Type = SnmpAdminString
_OtdrTraceMgmtFileName_Object = MibTableColumn
otdrTraceMgmtFileName = _OtdrTraceMgmtFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 8),
    _OtdrTraceMgmtFileName_Type()
)
otdrTraceMgmtFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtFileName.setStatus("current")


class _OtdrTraceMgmtTransferProtocol_Type(Integer32):
    """Custom type otdrTraceMgmtTransferProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("scp", 2))
    )


_OtdrTraceMgmtTransferProtocol_Type.__name__ = "Integer32"
_OtdrTraceMgmtTransferProtocol_Object = MibTableColumn
otdrTraceMgmtTransferProtocol = _OtdrTraceMgmtTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 9),
    _OtdrTraceMgmtTransferProtocol_Type()
)
otdrTraceMgmtTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtTransferProtocol.setStatus("current")


class _OtdrTraceMgmtFtpPort_Type(Integer32):
    """Custom type otdrTraceMgmtFtpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OtdrTraceMgmtFtpPort_Type.__name__ = "Integer32"
_OtdrTraceMgmtFtpPort_Object = MibTableColumn
otdrTraceMgmtFtpPort = _OtdrTraceMgmtFtpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 10),
    _OtdrTraceMgmtFtpPort_Type()
)
otdrTraceMgmtFtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtFtpPort.setStatus("current")


class _OtdrTraceMgmtActionProgress_Type(Integer32):
    """Custom type otdrTraceMgmtActionProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_OtdrTraceMgmtActionProgress_Type.__name__ = "Integer32"
_OtdrTraceMgmtActionProgress_Object = MibTableColumn
otdrTraceMgmtActionProgress = _OtdrTraceMgmtActionProgress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 11),
    _OtdrTraceMgmtActionProgress_Type()
)
otdrTraceMgmtActionProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTraceMgmtActionProgress.setStatus("current")
if mibBuilder.loadTexts:
    otdrTraceMgmtActionProgress.setUnits("%")

# Managed Objects groups


# Notification objects

alarmTempCPU = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 1)
)
alarmTempCPU.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmTempCPU.setStatus(
        "current"
    )

alarmTempBoard1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 2)
)
alarmTempBoard1.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmTempBoard1.setStatus(
        "current"
    )

alarmTempBoard2Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 3)
)
alarmTempBoard2Low.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmTempBoard2Low.setStatus(
        "current"
    )

alarmTempBoard2High = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 4)
)
alarmTempBoard2High.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmTempBoard2High.setStatus(
        "current"
    )

alarmTempLaserLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 5)
)
alarmTempLaserLow.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmTempLaserLow.setStatus(
        "current"
    )

alarmTempLaserHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 6)
)
alarmTempLaserHigh.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmTempLaserHigh.setStatus(
        "current"
    )

alarmMonNotRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 7)
)
alarmMonNotRunning.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmMonNotRunning.setStatus(
        "current"
    )

alarmFpRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 8)
)
alarmFpRunning.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmFpRunning.setStatus(
        "current"
    )

alarmFaRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 9)
)
alarmFaRunning.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmFaRunning.setStatus(
        "current"
    )

alarmFpMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 10)
)
alarmFpMissing.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmFpMissing.setStatus(
        "current"
    )

alarmThresCrossedFast = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 11)
)
alarmThresCrossedFast.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmThresCrossedFast.setStatus(
        "current"
    )

alarmThresCrossedMedium = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 12)
)
alarmThresCrossedMedium.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmThresCrossedMedium.setStatus(
        "current"
    )

alarmThresCrossedSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 13)
)
alarmThresCrossedSlow.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmThresCrossedSlow.setStatus(
        "current"
    )

alarmLinkBudgetExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 14)
)
alarmLinkBudgetExceeded.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmLinkBudgetExceeded.setStatus(
        "current"
    )

alarmLinkBudgetNearlyExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 15)
)
alarmLinkBudgetNearlyExceeded.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmLinkBudgetNearlyExceeded.setStatus(
        "current"
    )

alarmManagementState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 16)
)
alarmManagementState.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmManagementState.setStatus(
        "current"
    )

alarmDisabledState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 17)
)
alarmDisabledState.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmDisabledState.setStatus(
        "current"
    )

stateChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 18)
)
stateChangedTrap.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    stateChangedTrap.setStatus(
        "current"
    )

objectChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 19)
)
objectChangedTrap.setObjects(
    ("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp")
)
if mibBuilder.loadTexts:
    objectChangedTrap.setStatus(
        "current"
    )

trapsinkCreatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 20)
)
trapsinkCreatedTrap.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "trapsinkAddress"))
)
if mibBuilder.loadTexts:
    trapsinkCreatedTrap.setStatus(
        "current"
    )

trapsinkDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 21)
)
trapsinkDeletedTrap.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "trapsinkAddress"))
)
if mibBuilder.loadTexts:
    trapsinkDeletedTrap.setStatus(
        "current"
    )

transient15MinMeasCollected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 22)
)
transient15MinMeasCollected.setObjects(
    ("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp")
)
if mibBuilder.loadTexts:
    transient15MinMeasCollected.setStatus(
        "current"
    )

transient1DayMeasCollected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 23)
)
transient1DayMeasCollected.setObjects(
    ("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp")
)
if mibBuilder.loadTexts:
    transient1DayMeasCollected.setStatus(
        "current"
    )

transientFpStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 24)
)
transientFpStarted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFpStarted.setStatus(
        "current"
    )

transientFpCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 25)
)
transientFpCompleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFpCompleted.setStatus(
        "current"
    )

transientFpFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 26)
)
transientFpFailed.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFpFailed.setStatus(
        "current"
    )

transientSwMgmtActionStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 27)
)
transientSwMgmtActionStarted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "softwareMgmtRequest"))
)
if mibBuilder.loadTexts:
    transientSwMgmtActionStarted.setStatus(
        "current"
    )

transientSwMgmtActionCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 28)
)
transientSwMgmtActionCompleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "softwareMgmtRequest"))
)
if mibBuilder.loadTexts:
    transientSwMgmtActionCompleted.setStatus(
        "current"
    )

transientSwMgmtActionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 29)
)
transientSwMgmtActionFailed.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "softwareMgmtRequest"),
        ("ADVA-FSP3000ALM-MIB", "softwareMgmtLastError"))
)
if mibBuilder.loadTexts:
    transientSwMgmtActionFailed.setStatus(
        "current"
    )

transientDbMgmtActionStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 30)
)
transientDbMgmtActionStarted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "databaseMgmtRequest"))
)
if mibBuilder.loadTexts:
    transientDbMgmtActionStarted.setStatus(
        "current"
    )

transientDbMgmtActionCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 31)
)
transientDbMgmtActionCompleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "databaseMgmtRequest"))
)
if mibBuilder.loadTexts:
    transientDbMgmtActionCompleted.setStatus(
        "current"
    )

transientDbMgmtActionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 32)
)
transientDbMgmtActionFailed.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "databaseMgmtRequest"),
        ("ADVA-FSP3000ALM-MIB", "databaseMgmtLastError"))
)
if mibBuilder.loadTexts:
    transientDbMgmtActionFailed.setStatus(
        "current"
    )

alarmNtpServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 33)
)
alarmNtpServerUnreachable.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"),
        ("ADVA-FSP3000ALM-MIB", "ntpServerName"))
)
if mibBuilder.loadTexts:
    alarmNtpServerUnreachable.setStatus(
        "current"
    )

transientFpSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 34)
)
transientFpSaved.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFpSaved.setStatus(
        "current"
    )

transientMonStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 35)
)
transientMonStarted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientMonStarted.setStatus(
        "current"
    )

transientMonStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 36)
)
transientMonStopped.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientMonStopped.setStatus(
        "current"
    )

transientOtdrMeasurementStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 37)
)
transientOtdrMeasurementStarted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientOtdrMeasurementStarted.setStatus(
        "current"
    )

transientOtdrMeasurementCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 38)
)
transientOtdrMeasurementCompleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientOtdrMeasurementCompleted.setStatus(
        "current"
    )

transientOtdrMeasurementFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 39)
)
transientOtdrMeasurementFailed.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientOtdrMeasurementFailed.setStatus(
        "current"
    )

transientOtdrMeasurementSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 40)
)
transientOtdrMeasurementSaved.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientOtdrMeasurementSaved.setStatus(
        "current"
    )

transientFaStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 41)
)
transientFaStarted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFaStarted.setStatus(
        "current"
    )

transientFaCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 42)
)
transientFaCompleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFaCompleted.setStatus(
        "current"
    )

transientFaFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 43)
)
transientFaFailed.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFaFailed.setStatus(
        "current"
    )

transientFaSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 44)
)
transientFaSaved.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFaSaved.setStatus(
        "current"
    )

transientInternalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 45)
)
transientInternalError.setObjects(
    ("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp")
)
if mibBuilder.loadTexts:
    transientInternalError.setStatus(
        "current"
    )

alarmRebootRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 46)
)
alarmRebootRunning.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmRebootRunning.setStatus(
        "current"
    )

alarmWarmupRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 47)
)
alarmWarmupRunning.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmWarmupRunning.setStatus(
        "current"
    )

alarmBadSysStat = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 48)
)
alarmBadSysStat.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmBadSysStat.setStatus(
        "current"
    )

alarmWrongFWVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 49)
)
alarmWrongFWVersion.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmWrongFWVersion.setStatus(
        "current"
    )

alarmMonProcNotRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 50)
)
alarmMonProcNotRunning.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmMonProcNotRunning.setStatus(
        "current"
    )

transientFaDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 51)
)
transientFaDeleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFaDeleted.setStatus(
        "current"
    )

transientOtdrMeasurementDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 52)
)
transientOtdrMeasurementDeleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientOtdrMeasurementDeleted.setStatus(
        "current"
    )

transientOtdrTraceMgmtActionStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 53)
)
transientOtdrTraceMgmtActionStarted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "otdrTraceMgmtRequest"),
        ("ADVA-FSP3000ALM-MIB", "otdrTraceMgmtFileName"))
)
if mibBuilder.loadTexts:
    transientOtdrTraceMgmtActionStarted.setStatus(
        "current"
    )

transientOtdrTraceMgmtActionCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 54)
)
transientOtdrTraceMgmtActionCompleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "otdrTraceMgmtRequest"),
        ("ADVA-FSP3000ALM-MIB", "otdrTraceMgmtFileName"))
)
if mibBuilder.loadTexts:
    transientOtdrTraceMgmtActionCompleted.setStatus(
        "current"
    )

transientOtdrTraceMgmtActionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 55)
)
transientOtdrTraceMgmtActionFailed.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "otdrTraceMgmtRequest"),
        ("ADVA-FSP3000ALM-MIB", "otdrTraceMgmtFileName"),
        ("ADVA-FSP3000ALM-MIB", "otdrTraceMgmtLastError"))
)
if mibBuilder.loadTexts:
    transientOtdrTraceMgmtActionFailed.setStatus(
        "current"
    )

alarmAlmPackageMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 56)
)
alarmAlmPackageMismatch.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmAlmPackageMismatch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADVA-FSP3000ALM-MIB",
    **{"Fsp3000almAlarmListType": Fsp3000almAlarmListType,
       "advaMIB": advaMIB,
       "products": products,
       "fsp3000alm": fsp3000alm,
       "trap": trap,
       "alarmTempCPU": alarmTempCPU,
       "alarmTempBoard1": alarmTempBoard1,
       "alarmTempBoard2Low": alarmTempBoard2Low,
       "alarmTempBoard2High": alarmTempBoard2High,
       "alarmTempLaserLow": alarmTempLaserLow,
       "alarmTempLaserHigh": alarmTempLaserHigh,
       "alarmMonNotRunning": alarmMonNotRunning,
       "alarmFpRunning": alarmFpRunning,
       "alarmFaRunning": alarmFaRunning,
       "alarmFpMissing": alarmFpMissing,
       "alarmThresCrossedFast": alarmThresCrossedFast,
       "alarmThresCrossedMedium": alarmThresCrossedMedium,
       "alarmThresCrossedSlow": alarmThresCrossedSlow,
       "alarmLinkBudgetExceeded": alarmLinkBudgetExceeded,
       "alarmLinkBudgetNearlyExceeded": alarmLinkBudgetNearlyExceeded,
       "alarmManagementState": alarmManagementState,
       "alarmDisabledState": alarmDisabledState,
       "stateChangedTrap": stateChangedTrap,
       "objectChangedTrap": objectChangedTrap,
       "trapsinkCreatedTrap": trapsinkCreatedTrap,
       "trapsinkDeletedTrap": trapsinkDeletedTrap,
       "transient15MinMeasCollected": transient15MinMeasCollected,
       "transient1DayMeasCollected": transient1DayMeasCollected,
       "transientFpStarted": transientFpStarted,
       "transientFpCompleted": transientFpCompleted,
       "transientFpFailed": transientFpFailed,
       "transientSwMgmtActionStarted": transientSwMgmtActionStarted,
       "transientSwMgmtActionCompleted": transientSwMgmtActionCompleted,
       "transientSwMgmtActionFailed": transientSwMgmtActionFailed,
       "transientDbMgmtActionStarted": transientDbMgmtActionStarted,
       "transientDbMgmtActionCompleted": transientDbMgmtActionCompleted,
       "transientDbMgmtActionFailed": transientDbMgmtActionFailed,
       "alarmNtpServerUnreachable": alarmNtpServerUnreachable,
       "transientFpSaved": transientFpSaved,
       "transientMonStarted": transientMonStarted,
       "transientMonStopped": transientMonStopped,
       "transientOtdrMeasurementStarted": transientOtdrMeasurementStarted,
       "transientOtdrMeasurementCompleted": transientOtdrMeasurementCompleted,
       "transientOtdrMeasurementFailed": transientOtdrMeasurementFailed,
       "transientOtdrMeasurementSaved": transientOtdrMeasurementSaved,
       "transientFaStarted": transientFaStarted,
       "transientFaCompleted": transientFaCompleted,
       "transientFaFailed": transientFaFailed,
       "transientFaSaved": transientFaSaved,
       "transientInternalError": transientInternalError,
       "alarmRebootRunning": alarmRebootRunning,
       "alarmWarmupRunning": alarmWarmupRunning,
       "alarmBadSysStat": alarmBadSysStat,
       "alarmWrongFWVersion": alarmWrongFWVersion,
       "alarmMonProcNotRunning": alarmMonProcNotRunning,
       "transientFaDeleted": transientFaDeleted,
       "transientOtdrMeasurementDeleted": transientOtdrMeasurementDeleted,
       "transientOtdrTraceMgmtActionStarted": transientOtdrTraceMgmtActionStarted,
       "transientOtdrTraceMgmtActionCompleted": transientOtdrTraceMgmtActionCompleted,
       "transientOtdrTraceMgmtActionFailed": transientOtdrTraceMgmtActionFailed,
       "alarmAlmPackageMismatch": alarmAlmPackageMismatch,
       "alarm": alarm,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmSource": alarmSource,
       "alarmType": alarmType,
       "alarmSeverity": alarmSeverity,
       "alarmTimeStamp": alarmTimeStamp,
       "alarmSeverityTable": alarmSeverityTable,
       "alarmSeverityEntry": alarmSeverityEntry,
       "alarmSeverityType": alarmSeverityType,
       "alarmSeverityValue": alarmSeverityValue,
       "device": device,
       "shelf": shelf,
       "shelfUnitName": shelfUnitName,
       "firmwarePackageRev": firmwarePackageRev,
       "hardwareRev": hardwareRev,
       "fpgaRev": fpgaRev,
       "serialNumber": serialNumber,
       "partNumber": partNumber,
       "cleiCode": cleiCode,
       "vendorId": vendorId,
       "inventoryType": inventoryType,
       "universalSerialIdent": universalSerialIdent,
       "tempCPU": tempCPU,
       "tresholdMaxTempCPU": tresholdMaxTempCPU,
       "tempBoard1": tempBoard1,
       "tresholdMaxTempBoard1": tresholdMaxTempBoard1,
       "tempBoard2": tempBoard2,
       "tresholdMinTempBoard2": tresholdMinTempBoard2,
       "tresholdMaxTempBoard2": tresholdMaxTempBoard2,
       "tempLaser": tempLaser,
       "tresholdMinTempLaser": tresholdMinTempLaser,
       "tresholdMaxTempLaser": tresholdMaxTempLaser,
       "aidString": aidString,
       "shelfName": shelfName,
       "portTable": portTable,
       "portEntry": portEntry,
       "portId": portId,
       "portAdminState": portAdminState,
       "portOperState": portOperState,
       "portName": portName,
       "portAidString": portAidString,
       "measurement": measurement,
       "measurementLossTable": measurementLossTable,
       "measurementLossEntry": measurementLossEntry,
       "measurementLossIndex": measurementLossIndex,
       "measurementLossLinkLoss": measurementLossLinkLoss,
       "measurementLossLinkFaultLoc": measurementLossLinkFaultLoc,
       "measurementLossLinkFaultLocRes": measurementLossLinkFaultLocRes,
       "measurementLossDevFast": measurementLossDevFast,
       "measurementLossDevMedium": measurementLossDevMedium,
       "measurementLossDevSlow": measurementLossDevSlow,
       "measurementLossDataTimestamp": measurementLossDataTimestamp,
       "histMeasLoss15MinTable": histMeasLoss15MinTable,
       "histMeasLoss15MinEntry": histMeasLoss15MinEntry,
       "histMeasLoss15MinNumber": histMeasLoss15MinNumber,
       "histMeasLoss15MinLow": histMeasLoss15MinLow,
       "histMeasLoss15MinMean": histMeasLoss15MinMean,
       "histMeasLoss15MinHigh": histMeasLoss15MinHigh,
       "histMeasLoss15MinValidFlag": histMeasLoss15MinValidFlag,
       "histMeasLoss15MinTimeStamp": histMeasLoss15MinTimeStamp,
       "histMeasLoss1DayTable": histMeasLoss1DayTable,
       "histMeasLoss1DayEntry": histMeasLoss1DayEntry,
       "histMeasLoss1DayNumber": histMeasLoss1DayNumber,
       "histMeasLoss1DayLow": histMeasLoss1DayLow,
       "histMeasLoss1DayMean": histMeasLoss1DayMean,
       "histMeasLoss1DayHigh": histMeasLoss1DayHigh,
       "histMeasLoss1DayValidFlag": histMeasLoss1DayValidFlag,
       "histMeasLoss1DayTimeStamp": histMeasLoss1DayTimeStamp,
       "portThresTable": portThresTable,
       "portThresEntry": portThresEntry,
       "portThresDeviationFast": portThresDeviationFast,
       "portThresDeviationMedium": portThresDeviationMedium,
       "portThresDeviationSlow": portThresDeviationSlow,
       "portThresBudget": portThresBudget,
       "portThresCloseToBudget": portThresCloseToBudget,
       "portPeriodLossDevTable": portPeriodLossDevTable,
       "portPeriodLossDevEntry": portPeriodLossDevEntry,
       "portPeriodLossDevFast": portPeriodLossDevFast,
       "portPeriodLossDevMedium": portPeriodLossDevMedium,
       "portPeriodLossDevSlow": portPeriodLossDevSlow,
       "measurementFpTable": measurementFpTable,
       "measurementFpEntry": measurementFpEntry,
       "measurementFpIndex": measurementFpIndex,
       "measurementFpRefractiveIndex": measurementFpRefractiveIndex,
       "measurementFpExternalOffset": measurementFpExternalOffset,
       "measurementFpCouplerLoss": measurementFpCouplerLoss,
       "measurementFpLinkLoss": measurementFpLinkLoss,
       "measurementFpLineEndPos": measurementFpLineEndPos,
       "measurementFpDataTimestamp": measurementFpDataTimestamp,
       "measurementFaTable": measurementFaTable,
       "measurementFaEntry": measurementFaEntry,
       "measurementFaIndex": measurementFaIndex,
       "measurementFaLinkLoss": measurementFaLinkLoss,
       "measurementFaFaultPos": measurementFaFaultPos,
       "measurementFaDeprecated": measurementFaDeprecated,
       "measurementFaDataTimestamp": measurementFaDataTimestamp,
       "measurementOtdrTable": measurementOtdrTable,
       "measurementOtdrEntry": measurementOtdrEntry,
       "measurementOtdrIndex": measurementOtdrIndex,
       "measurementOtdrLength": measurementOtdrLength,
       "measurementOtdrExternalOffset": measurementOtdrExternalOffset,
       "measurementOtdrRefractiveIndex": measurementOtdrRefractiveIndex,
       "measurementOtdrPowerLevel": measurementOtdrPowerLevel,
       "measurementOtdrPulseWidth": measurementOtdrPulseWidth,
       "measurementOtdrAverageRate": measurementOtdrAverageRate,
       "measurementOtdrDataTimestamp": measurementOtdrDataTimestamp,
       "eventLogs": eventLogs,
       "eventsLogged": eventsLogged,
       "eventLogTable": eventLogTable,
       "eventLogEntry": eventLogEntry,
       "eventLogIndex": eventLogIndex,
       "eventLogTimeStamp": eventLogTimeStamp,
       "eventLogNotificationOID": eventLogNotificationOID,
       "eventLogIdentityTranslation": eventLogIdentityTranslation,
       "eventLogVarTable": eventLogVarTable,
       "eventLogVarEntry": eventLogVarEntry,
       "eventLogVarIndex": eventLogVarIndex,
       "eventLogVarId": eventLogVarId,
       "eventLogVarType": eventLogVarType,
       "eventLogVarInteger32Val": eventLogVarInteger32Val,
       "eventLogVarIpAddressVal": eventLogVarIpAddressVal,
       "eventLogVarOctetStringVal": eventLogVarOctetStringVal,
       "eventLogVarOidVal": eventLogVarOidVal,
       "eventLogVarCounter64Val": eventLogVarCounter64Val,
       "eventLogVarUnsigned32Val": eventLogVarUnsigned32Val,
       "trapsinkTable": trapsinkTable,
       "trapsinkEntry": trapsinkEntry,
       "trapsinkAddress": trapsinkAddress,
       "trapsinkPort": trapsinkPort,
       "trapsinkCommunity": trapsinkCommunity,
       "trapsinkRowStatus": trapsinkRowStatus,
       "trapsinkVersion": trapsinkVersion,
       "trapsinkUserName": trapsinkUserName,
       "system": system,
       "information": information,
       "softwareVersion": softwareVersion,
       "localDateAndTime": localDateAndTime,
       "releaseNumber": releaseNumber,
       "expectedSoftwareVersion": expectedSoftwareVersion,
       "ipSettings": ipSettings,
       "ipAddress": ipAddress,
       "subnetMask": subnetMask,
       "gateway": gateway,
       "dns1": dns1,
       "dns2": dns2,
       "softwareMgmt": softwareMgmt,
       "softwareMgmtFileTable": softwareMgmtFileTable,
       "softwareMgmtFileEntry": softwareMgmtFileEntry,
       "softwareMgmtFileIndex": softwareMgmtFileIndex,
       "softwareMgmtFileSize": softwareMgmtFileSize,
       "softwareMgmtFileCreationTime": softwareMgmtFileCreationTime,
       "softwareMgmtFileVersion": softwareMgmtFileVersion,
       "softwareMgmtFileFileName": softwareMgmtFileFileName,
       "softwareMgmtFileRowStatus": softwareMgmtFileRowStatus,
       "softwareMgmtRequest": softwareMgmtRequest,
       "softwareMgmtState": softwareMgmtState,
       "softwareMgmtLastError": softwareMgmtLastError,
       "softwareMgmtDatabaseUsage": softwareMgmtDatabaseUsage,
       "softwareMgmtDatabaseFileName": softwareMgmtDatabaseFileName,
       "softwareMgmtServerAddress": softwareMgmtServerAddress,
       "softwareMgmtServerLogin": softwareMgmtServerLogin,
       "softwareMgmtServerPasswd": softwareMgmtServerPasswd,
       "softwareMgmtServerDirectory": softwareMgmtServerDirectory,
       "softwareMgmtFileName": softwareMgmtFileName,
       "softwareMgmtTransferProtocol": softwareMgmtTransferProtocol,
       "softwareMgmtFtpPort": softwareMgmtFtpPort,
       "softwareMgmtActionProgress": softwareMgmtActionProgress,
       "databaseMgmt": databaseMgmt,
       "databaseMgmtFileTable": databaseMgmtFileTable,
       "databaseMgmtFileEntry": databaseMgmtFileEntry,
       "databaseMgmtFileIndex": databaseMgmtFileIndex,
       "databaseMgmtFileSize": databaseMgmtFileSize,
       "databaseMgmtFileCreationTime": databaseMgmtFileCreationTime,
       "databaseMgmtFileVersion": databaseMgmtFileVersion,
       "databaseMgmtFileFileName": databaseMgmtFileFileName,
       "databaseMgmtFileRowStatus": databaseMgmtFileRowStatus,
       "databaseMgmtRequest": databaseMgmtRequest,
       "databaseMgmtState": databaseMgmtState,
       "databaseMgmtLastError": databaseMgmtLastError,
       "databaseMgmtServerAddress": databaseMgmtServerAddress,
       "databaseMgmtServerLogin": databaseMgmtServerLogin,
       "databaseMgmtServerPasswd": databaseMgmtServerPasswd,
       "databaseMgmtServerDirectory": databaseMgmtServerDirectory,
       "databaseMgmtFileName": databaseMgmtFileName,
       "databaseMgmtTransferProtocol": databaseMgmtTransferProtocol,
       "databaseMgmtFtpPort": databaseMgmtFtpPort,
       "databaseMgmtActionProgress": databaseMgmtActionProgress,
       "ntpMgmt": ntpMgmt,
       "ntpClientConfig": ntpClientConfig,
       "ntpServerName": ntpServerName,
       "generalSettings": generalSettings,
       "operationMode": operationMode,
       "maintain": maintain,
       "maintainTable": maintainTable,
       "maintainEntry": maintainEntry,
       "maintainOperationRequest": maintainOperationRequest,
       "maintainOperationRefractiveIndex": maintainOperationRefractiveIndex,
       "maintainOperationExternalOffset": maintainOperationExternalOffset,
       "maintainOperationCouplerLoss": maintainOperationCouplerLoss,
       "maintainOperationOtdrLength": maintainOperationOtdrLength,
       "maintainOperationOtdrPowerLevel": maintainOperationOtdrPowerLevel,
       "maintainOperationOtdrPulseWidth": maintainOperationOtdrPulseWidth,
       "maintainOperationOtdrAverageRate": maintainOperationOtdrAverageRate,
       "maintainOperationState": maintainOperationState,
       "maintainOperationLastError": maintainOperationLastError,
       "otdrTraceMgmt": otdrTraceMgmt,
       "otdrTraceMgmtTable": otdrTraceMgmtTable,
       "otdrTraceMgmtEntry": otdrTraceMgmtEntry,
       "otdrTraceMgmtRequest": otdrTraceMgmtRequest,
       "otdrTraceMgmtState": otdrTraceMgmtState,
       "otdrTraceMgmtLastError": otdrTraceMgmtLastError,
       "otdrTraceMgmtServerAddress": otdrTraceMgmtServerAddress,
       "otdrTraceMgmtServerLogin": otdrTraceMgmtServerLogin,
       "otdrTraceMgmtServerPasswd": otdrTraceMgmtServerPasswd,
       "otdrTraceMgmtServerDirectory": otdrTraceMgmtServerDirectory,
       "otdrTraceMgmtFileName": otdrTraceMgmtFileName,
       "otdrTraceMgmtTransferProtocol": otdrTraceMgmtTransferProtocol,
       "otdrTraceMgmtFtpPort": otdrTraceMgmtFtpPort,
       "otdrTraceMgmtActionProgress": otdrTraceMgmtActionProgress}
)
