# SNMP MIB module (ZYXEL-olt1408-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-olt1408-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:20:55 2025
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

(BridgeId,
 Timeout,
 dot1dBasePort) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout",
    "dot1dBasePort")

(OperationResponseStatus,) = mibBuilder.importSymbols(
    "DISMAN-PING-MIB",
    "OperationResponseStatus")

(dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepIdentifier")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ospfAddressLessIf,
 ospfAreaId,
 ospfIfIpAddress,
 ospfLsdbAreaId,
 ospfLsdbLsid,
 ospfLsdbRouterId,
 ospfLsdbType,
 ospfNbrAddressLessIndex,
 ospfNbrIpAddr,
 ospfVirtIfAreaId,
 ospfVirtIfNeighbor) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "ospfAddressLessIf",
    "ospfAreaId",
    "ospfIfIpAddress",
    "ospfLsdbAreaId",
    "ospfLsdbLsid",
    "ospfLsdbRouterId",
    "ospfLsdbType",
    "ospfNbrAddressLessIndex",
    "ospfNbrIpAddr",
    "ospfVirtIfAreaId",
    "ospfVirtIfNeighbor")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "dot1qVlanIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysObjectID,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysObjectID")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

faultMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 30)
)

faultTrapsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 31)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UtcTimeStamp(TextualConvention, Unsigned32):
    status = "current"


class EventIdNumber(TextualConvention, Integer32):
    status = "current"


class EventSeverity(TextualConvention, Integer32):
    status = "current"
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("informational", 4))
    )



class EventServiceAffective(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noServiceAffected", 1),
          ("serviceAffected", 2))
    )



class InstanceType(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("node", 2),
          ("shelf", 3),
          ("line", 4),
          ("switch", 5),
          ("lsp", 6),
          ("l2Interface", 7),
          ("l3Interface", 8),
          ("rowIndex", 9),
          ("aid", 10))
    )



class EventPersistence(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("delta", 2))
    )



class MstiOrCistInstanceIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



class RemoteOnuStatus(TextualConvention, Integer32):
    status = "current"
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("oos", 0),
          ("is", 1),
          ("oosLO", 2),
          ("oosNR", 3),
          ("oosCD", 4),
          ("oosNP", 5),
          ("oosPF", 6),
          ("oosAD", 7),
          ("oosOD", 8),
          ("oosOO", 9),
          ("oosTM", 10),
          ("oosCO", 11),
          ("oosUO", 12),
          ("oosNO", 13),
          ("oosGS", 14),
          ("oosGF", 15),
          ("oosAF", 16),
          ("oosVO", 17),
          ("oosDG", 18),
          ("oosLS", 19),
          ("oosSB", 20))
    )



# MIB Managed Objects in the order of their OIDs

_Zyxel_ObjectIdentity = ObjectIdentity
zyxel = _Zyxel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1)
)
_AccessSwitch_ObjectIdentity = ObjectIdentity
accessSwitch = _AccessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5)
)
_GponSeries_ObjectIdentity = ObjectIdentity
gponSeries = _GponSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17)
)
_Olt1408_ObjectIdentity = ObjectIdentity
olt1408 = _Olt1408_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6)
)
_SysInfo_ObjectIdentity = ObjectIdentity
sysInfo = _SysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1)
)
_SysSwPlatformMajorVers_Type = Integer32
_SysSwPlatformMajorVers_Object = MibScalar
sysSwPlatformMajorVers = _SysSwPlatformMajorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 1),
    _SysSwPlatformMajorVers_Type()
)
sysSwPlatformMajorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwPlatformMajorVers.setStatus("current")
_SysSwPlatformMinorVers_Type = Integer32
_SysSwPlatformMinorVers_Object = MibScalar
sysSwPlatformMinorVers = _SysSwPlatformMinorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 2),
    _SysSwPlatformMinorVers_Type()
)
sysSwPlatformMinorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwPlatformMinorVers.setStatus("current")
_SysSwModelString_Type = DisplayString
_SysSwModelString_Object = MibScalar
sysSwModelString = _SysSwModelString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 3),
    _SysSwModelString_Type()
)
sysSwModelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwModelString.setStatus("current")
_SysSwDay_Type = Integer32
_SysSwDay_Object = MibScalar
sysSwDay = _SysSwDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 4),
    _SysSwDay_Type()
)
sysSwDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwDay.setStatus("current")
_SysSwMonth_Type = Integer32
_SysSwMonth_Object = MibScalar
sysSwMonth = _SysSwMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 5),
    _SysSwMonth_Type()
)
sysSwMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwMonth.setStatus("current")
_SysSwYear_Type = Integer32
_SysSwYear_Object = MibScalar
sysSwYear = _SysSwYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 6),
    _SysSwYear_Type()
)
sysSwYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwYear.setStatus("current")
_SysSerialNumber_Type = DisplayString
_SysSerialNumber_Object = MibScalar
sysSerialNumber = _SysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 7),
    _SysSerialNumber_Type()
)
sysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSerialNumber.setStatus("current")


class _SysSwBootUpImage_Type(Integer32):
    """Custom type sysSwBootUpImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("image1", 1),
          ("image2", 2))
    )


_SysSwBootUpImage_Type.__name__ = "Integer32"
_SysSwBootUpImage_Object = MibScalar
sysSwBootUpImage = _SysSwBootUpImage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 8),
    _SysSwBootUpImage_Type()
)
sysSwBootUpImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwBootUpImage.setStatus("current")
_SysImage1FwVersion_Type = DisplayString
_SysImage1FwVersion_Object = MibScalar
sysImage1FwVersion = _SysImage1FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 9),
    _SysImage1FwVersion_Type()
)
sysImage1FwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysImage1FwVersion.setStatus("current")
_SysImage2FwVersion_Type = DisplayString
_SysImage2FwVersion_Object = MibScalar
sysImage2FwVersion = _SysImage2FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 10),
    _SysImage2FwVersion_Type()
)
sysImage2FwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysImage2FwVersion.setStatus("current")
_SysCurrentFwVersion_Type = DisplayString
_SysCurrentFwVersion_Object = MibScalar
sysCurrentFwVersion = _SysCurrentFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 11),
    _SysCurrentFwVersion_Type()
)
sysCurrentFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCurrentFwVersion.setStatus("current")
_PwrInfo_ObjectIdentity = ObjectIdentity
pwrInfo = _PwrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 18)
)


class _PwrInfoSource_Type(Integer32):
    """Custom type pwrInfoSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dc", 0),
          ("ac", 1),
          ("battery", 2))
    )


_PwrInfoSource_Type.__name__ = "Integer32"
_PwrInfoSource_Object = MibScalar
pwrInfoSource = _PwrInfoSource_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 18, 1),
    _PwrInfoSource_Type()
)
pwrInfoSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrInfoSource.setStatus("current")
_PwrInfoSysPowerConsumption_Type = Integer32
_PwrInfoSysPowerConsumption_Object = MibScalar
pwrInfoSysPowerConsumption = _PwrInfoSysPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 18, 2),
    _PwrInfoSysPowerConsumption_Type()
)
pwrInfoSysPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrInfoSysPowerConsumption.setStatus("current")
_PwrInfoBatChargingPower_Type = Integer32
_PwrInfoBatChargingPower_Object = MibScalar
pwrInfoBatChargingPower = _PwrInfoBatChargingPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 18, 3),
    _PwrInfoBatChargingPower_Type()
)
pwrInfoBatChargingPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrInfoBatChargingPower.setStatus("current")


class _PwrInfoBatExistence_Type(Integer32):
    """Custom type pwrInfoBatExistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noExist", 0),
          ("exist", 1))
    )


_PwrInfoBatExistence_Type.__name__ = "Integer32"
_PwrInfoBatExistence_Object = MibScalar
pwrInfoBatExistence = _PwrInfoBatExistence_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 18, 4),
    _PwrInfoBatExistence_Type()
)
pwrInfoBatExistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrInfoBatExistence.setStatus("current")
_PwrInfoBatTemperature_Type = Integer32
_PwrInfoBatTemperature_Object = MibScalar
pwrInfoBatTemperature = _PwrInfoBatTemperature_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 18, 5),
    _PwrInfoBatTemperature_Type()
)
pwrInfoBatTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrInfoBatTemperature.setStatus("current")
_PwrInfoBatRemainingPower_Type = Integer32
_PwrInfoBatRemainingPower_Object = MibScalar
pwrInfoBatRemainingPower = _PwrInfoBatRemainingPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 18, 6),
    _PwrInfoBatRemainingPower_Type()
)
pwrInfoBatRemainingPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrInfoBatRemainingPower.setStatus("current")
_PwrInfoBatVoltage_Type = Integer32
_PwrInfoBatVoltage_Object = MibScalar
pwrInfoBatVoltage = _PwrInfoBatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 18, 7),
    _PwrInfoBatVoltage_Type()
)
pwrInfoBatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrInfoBatVoltage.setStatus("current")


class _PwrInfoBatCapacityValidation_Type(Integer32):
    """Custom type pwrInfoBatCapacityValidation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_PwrInfoBatCapacityValidation_Type.__name__ = "Integer32"
_PwrInfoBatCapacityValidation_Object = MibScalar
pwrInfoBatCapacityValidation = _PwrInfoBatCapacityValidation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 18, 8),
    _PwrInfoBatCapacityValidation_Type()
)
pwrInfoBatCapacityValidation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrInfoBatCapacityValidation.setStatus("current")


class _PwrInfoChargerStatus_Type(Integer32):
    """Custom type pwrInfoChargerStatus based on Integer32"""
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


_PwrInfoChargerStatus_Type.__name__ = "Integer32"
_PwrInfoChargerStatus_Object = MibScalar
pwrInfoChargerStatus = _PwrInfoChargerStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 18, 9),
    _PwrInfoChargerStatus_Type()
)
pwrInfoChargerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrInfoChargerStatus.setStatus("current")
_PwrInfoChargingCurrent_Type = Integer32
_PwrInfoChargingCurrent_Object = MibScalar
pwrInfoChargingCurrent = _PwrInfoChargingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 18, 10),
    _PwrInfoChargingCurrent_Type()
)
pwrInfoChargingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrInfoChargingCurrent.setStatus("current")
_PwrInfoChargingVoltage_Type = Integer32
_PwrInfoChargingVoltage_Object = MibScalar
pwrInfoChargingVoltage = _PwrInfoChargingVoltage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 18, 11),
    _PwrInfoChargingVoltage_Type()
)
pwrInfoChargingVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrInfoChargingVoltage.setStatus("current")
_PwrInfoChargingTime_Type = Integer32
_PwrInfoChargingTime_Object = MibScalar
pwrInfoChargingTime = _PwrInfoChargingTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 18, 12),
    _PwrInfoChargingTime_Type()
)
pwrInfoChargingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrInfoChargingTime.setStatus("current")


class _PwrInfoTrickleChargerStatus_Type(Integer32):
    """Custom type pwrInfoTrickleChargerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("none", 2))
    )


_PwrInfoTrickleChargerStatus_Type.__name__ = "Integer32"
_PwrInfoTrickleChargerStatus_Object = MibScalar
pwrInfoTrickleChargerStatus = _PwrInfoTrickleChargerStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 18, 13),
    _PwrInfoTrickleChargerStatus_Type()
)
pwrInfoTrickleChargerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrInfoTrickleChargerStatus.setStatus("current")
_BatterySetting_ObjectIdentity = ObjectIdentity
batterySetting = _BatterySetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 18, 14)
)
_BatteryCapacity_Type = Integer32
_BatteryCapacity_Object = MibScalar
batteryCapacity = _BatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 18, 14, 1),
    _BatteryCapacity_Type()
)
batteryCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCapacity.setStatus("current")


class _BatteryTempThresholdHigh_Type(Integer32):
    """Custom type batteryTempThresholdHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 50),
    )


_BatteryTempThresholdHigh_Type.__name__ = "Integer32"
_BatteryTempThresholdHigh_Object = MibScalar
batteryTempThresholdHigh = _BatteryTempThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 18, 14, 2),
    _BatteryTempThresholdHigh_Type()
)
batteryTempThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempThresholdHigh.setStatus("current")


class _BatteryTempThresholdLow_Type(Integer32):
    """Custom type batteryTempThresholdLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 50),
    )


_BatteryTempThresholdLow_Type.__name__ = "Integer32"
_BatteryTempThresholdLow_Object = MibScalar
batteryTempThresholdLow = _BatteryTempThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 1, 18, 14, 3),
    _BatteryTempThresholdLow_Type()
)
batteryTempThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempThresholdLow.setStatus("current")
_RateLimitSetup_ObjectIdentity = ObjectIdentity
rateLimitSetup = _RateLimitSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 2)
)
_RateLimitState_Type = EnabledStatus
_RateLimitState_Object = MibScalar
rateLimitState = _RateLimitState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 2, 1),
    _RateLimitState_Type()
)
rateLimitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitState.setStatus("current")
_RateLimitPortTable_Object = MibTable
rateLimitPortTable = _RateLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 2, 2)
)
if mibBuilder.loadTexts:
    rateLimitPortTable.setStatus("current")
_RateLimitPortEntry_Object = MibTableRow
rateLimitPortEntry = _RateLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 2, 2, 1)
)
rateLimitPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rateLimitPortEntry.setStatus("current")
_RateLimitPortState_Type = EnabledStatus
_RateLimitPortState_Object = MibTableColumn
rateLimitPortState = _RateLimitPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 2, 2, 1, 1),
    _RateLimitPortState_Type()
)
rateLimitPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortState.setStatus("current")
_RateLimitPortCommitRate_Type = Integer32
_RateLimitPortCommitRate_Object = MibTableColumn
rateLimitPortCommitRate = _RateLimitPortCommitRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 2, 2, 1, 2),
    _RateLimitPortCommitRate_Type()
)
rateLimitPortCommitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortCommitRate.setStatus("current")
_RateLimitPortPeakRate_Type = Integer32
_RateLimitPortPeakRate_Object = MibTableColumn
rateLimitPortPeakRate = _RateLimitPortPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 2, 2, 1, 3),
    _RateLimitPortPeakRate_Type()
)
rateLimitPortPeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortPeakRate.setStatus("current")
_RateLimitPortEgrRate_Type = Integer32
_RateLimitPortEgrRate_Object = MibTableColumn
rateLimitPortEgrRate = _RateLimitPortEgrRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 2, 2, 1, 4),
    _RateLimitPortEgrRate_Type()
)
rateLimitPortEgrRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortEgrRate.setStatus("current")
_RateLimitPortPeakState_Type = EnabledStatus
_RateLimitPortPeakState_Object = MibTableColumn
rateLimitPortPeakState = _RateLimitPortPeakState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 2, 2, 1, 5),
    _RateLimitPortPeakState_Type()
)
rateLimitPortPeakState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortPeakState.setStatus("current")
_RateLimitPortEgrState_Type = EnabledStatus
_RateLimitPortEgrState_Object = MibTableColumn
rateLimitPortEgrState = _RateLimitPortEgrState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 2, 2, 1, 6),
    _RateLimitPortEgrState_Type()
)
rateLimitPortEgrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortEgrState.setStatus("current")
_RateLimitPortCommitState_Type = EnabledStatus
_RateLimitPortCommitState_Object = MibTableColumn
rateLimitPortCommitState = _RateLimitPortCommitState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 2, 2, 1, 7),
    _RateLimitPortCommitState_Type()
)
rateLimitPortCommitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortCommitState.setStatus("current")
_BrLimitSetup_ObjectIdentity = ObjectIdentity
brLimitSetup = _BrLimitSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 3)
)
_BrLimitState_Type = EnabledStatus
_BrLimitState_Object = MibScalar
brLimitState = _BrLimitState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 3, 1),
    _BrLimitState_Type()
)
brLimitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitState.setStatus("current")
_BrLimitPortTable_Object = MibTable
brLimitPortTable = _BrLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 3, 2)
)
if mibBuilder.loadTexts:
    brLimitPortTable.setStatus("current")
_BrLimitPortEntry_Object = MibTableRow
brLimitPortEntry = _BrLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 3, 2, 1)
)
brLimitPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    brLimitPortEntry.setStatus("current")
_BrLimitPortBrState_Type = EnabledStatus
_BrLimitPortBrState_Object = MibTableColumn
brLimitPortBrState = _BrLimitPortBrState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 3, 2, 1, 1),
    _BrLimitPortBrState_Type()
)
brLimitPortBrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortBrState.setStatus("current")
_BrLimitPortBrRate_Type = Integer32
_BrLimitPortBrRate_Object = MibTableColumn
brLimitPortBrRate = _BrLimitPortBrRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 3, 2, 1, 2),
    _BrLimitPortBrRate_Type()
)
brLimitPortBrRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortBrRate.setStatus("current")
_BrLimitPortMcState_Type = EnabledStatus
_BrLimitPortMcState_Object = MibTableColumn
brLimitPortMcState = _BrLimitPortMcState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 3, 2, 1, 3),
    _BrLimitPortMcState_Type()
)
brLimitPortMcState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortMcState.setStatus("current")
_BrLimitPortMcRate_Type = Integer32
_BrLimitPortMcRate_Object = MibTableColumn
brLimitPortMcRate = _BrLimitPortMcRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 3, 2, 1, 4),
    _BrLimitPortMcRate_Type()
)
brLimitPortMcRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortMcRate.setStatus("current")
_BrLimitPortDlfState_Type = EnabledStatus
_BrLimitPortDlfState_Object = MibTableColumn
brLimitPortDlfState = _BrLimitPortDlfState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 3, 2, 1, 5),
    _BrLimitPortDlfState_Type()
)
brLimitPortDlfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortDlfState.setStatus("current")
_BrLimitPortDlfRate_Type = Integer32
_BrLimitPortDlfRate_Object = MibTableColumn
brLimitPortDlfRate = _BrLimitPortDlfRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 3, 2, 1, 6),
    _BrLimitPortDlfRate_Type()
)
brLimitPortDlfRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortDlfRate.setStatus("current")
_PortSecuritySetup_ObjectIdentity = ObjectIdentity
portSecuritySetup = _PortSecuritySetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 4)
)
_PortSecurityState_Type = EnabledStatus
_PortSecurityState_Object = MibScalar
portSecurityState = _PortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 4, 1),
    _PortSecurityState_Type()
)
portSecurityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityState.setStatus("current")
_PortSecurityPortTable_Object = MibTable
portSecurityPortTable = _PortSecurityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 4, 2)
)
if mibBuilder.loadTexts:
    portSecurityPortTable.setStatus("current")
_PortSecurityPortEntry_Object = MibTableRow
portSecurityPortEntry = _PortSecurityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 4, 2, 1)
)
portSecurityPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portSecurityPortEntry.setStatus("current")
_PortSecurityPortState_Type = EnabledStatus
_PortSecurityPortState_Object = MibTableColumn
portSecurityPortState = _PortSecurityPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 4, 2, 1, 1),
    _PortSecurityPortState_Type()
)
portSecurityPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortState.setStatus("current")
_PortSecurityPortLearnState_Type = EnabledStatus
_PortSecurityPortLearnState_Object = MibTableColumn
portSecurityPortLearnState = _PortSecurityPortLearnState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 4, 2, 1, 2),
    _PortSecurityPortLearnState_Type()
)
portSecurityPortLearnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortLearnState.setStatus("current")
_PortSecurityPortCount_Type = Integer32
_PortSecurityPortCount_Object = MibTableColumn
portSecurityPortCount = _PortSecurityPortCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 4, 2, 1, 3),
    _PortSecurityPortCount_Type()
)
portSecurityPortCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortCount.setStatus("current")
_PortSecurityMacFreeze_Type = PortList
_PortSecurityMacFreeze_Object = MibScalar
portSecurityMacFreeze = _PortSecurityMacFreeze_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 4, 3),
    _PortSecurityMacFreeze_Type()
)
portSecurityMacFreeze.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityMacFreeze.setStatus("current")
_VlanTrunkSetup_ObjectIdentity = ObjectIdentity
vlanTrunkSetup = _VlanTrunkSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 5)
)
_VlanTrunkPortTable_Object = MibTable
vlanTrunkPortTable = _VlanTrunkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 5, 1)
)
if mibBuilder.loadTexts:
    vlanTrunkPortTable.setStatus("current")
_VlanTrunkPortEntry_Object = MibTableRow
vlanTrunkPortEntry = _VlanTrunkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 5, 1, 1)
)
vlanTrunkPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    vlanTrunkPortEntry.setStatus("current")
_VlanTrunkPortState_Type = EnabledStatus
_VlanTrunkPortState_Object = MibTableColumn
vlanTrunkPortState = _VlanTrunkPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 5, 1, 1, 1),
    _VlanTrunkPortState_Type()
)
vlanTrunkPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkPortState.setStatus("current")
_CtlProtTransSetup_ObjectIdentity = ObjectIdentity
ctlProtTransSetup = _CtlProtTransSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 6)
)
_CtlProtTransState_Type = EnabledStatus
_CtlProtTransState_Object = MibScalar
ctlProtTransState = _CtlProtTransState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 6, 1),
    _CtlProtTransState_Type()
)
ctlProtTransState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlProtTransState.setStatus("current")
_CtlProtTransTunnelPortTable_Object = MibTable
ctlProtTransTunnelPortTable = _CtlProtTransTunnelPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 6, 2)
)
if mibBuilder.loadTexts:
    ctlProtTransTunnelPortTable.setStatus("current")
_CtlProtTransTunnelPortEntry_Object = MibTableRow
ctlProtTransTunnelPortEntry = _CtlProtTransTunnelPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 6, 2, 1)
)
ctlProtTransTunnelPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    ctlProtTransTunnelPortEntry.setStatus("current")


class _CtlProtTransTunnelMode_Type(Integer32):
    """Custom type ctlProtTransTunnelMode based on Integer32"""
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
        *(("peer", 0),
          ("tunnel", 1),
          ("discard", 2),
          ("network", 3))
    )


_CtlProtTransTunnelMode_Type.__name__ = "Integer32"
_CtlProtTransTunnelMode_Object = MibTableColumn
ctlProtTransTunnelMode = _CtlProtTransTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 6, 2, 1, 1),
    _CtlProtTransTunnelMode_Type()
)
ctlProtTransTunnelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlProtTransTunnelMode.setStatus("current")
_VlanStackSetup_ObjectIdentity = ObjectIdentity
vlanStackSetup = _VlanStackSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 7)
)
_VlanStackPortTable_Object = MibTable
vlanStackPortTable = _VlanStackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 7, 3)
)
if mibBuilder.loadTexts:
    vlanStackPortTable.setStatus("current")
_VlanStackPortEntry_Object = MibTableRow
vlanStackPortEntry = _VlanStackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 7, 3, 1)
)
vlanStackPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    vlanStackPortEntry.setStatus("current")


class _VlanStackPortMode_Type(Integer32):
    """Custom type vlanStackPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("access", 2),
          ("tunnel", 3))
    )


_VlanStackPortMode_Type.__name__ = "Integer32"
_VlanStackPortMode_Object = MibTableColumn
vlanStackPortMode = _VlanStackPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 7, 3, 1, 1),
    _VlanStackPortMode_Type()
)
vlanStackPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackPortMode.setStatus("current")
_VlanStackPortVid_Type = Integer32
_VlanStackPortVid_Object = MibTableColumn
vlanStackPortVid = _VlanStackPortVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 7, 3, 1, 2),
    _VlanStackPortVid_Type()
)
vlanStackPortVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackPortVid.setStatus("current")


class _VlanStackPortPrio_Type(Integer32):
    """Custom type vlanStackPortPrio based on Integer32"""
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
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7))
    )


_VlanStackPortPrio_Type.__name__ = "Integer32"
_VlanStackPortPrio_Object = MibTableColumn
vlanStackPortPrio = _VlanStackPortPrio_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 7, 3, 1, 3),
    _VlanStackPortPrio_Type()
)
vlanStackPortPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackPortPrio.setStatus("current")
_VlanStackTunnelPortTpid_Type = Integer32
_VlanStackTunnelPortTpid_Object = MibTableColumn
vlanStackTunnelPortTpid = _VlanStackTunnelPortTpid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 7, 3, 1, 4),
    _VlanStackTunnelPortTpid_Type()
)
vlanStackTunnelPortTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackTunnelPortTpid.setStatus("current")
_Dot1xSetup_ObjectIdentity = ObjectIdentity
dot1xSetup = _Dot1xSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 8)
)
_PortAuthState_Type = EnabledStatus
_PortAuthState_Object = MibScalar
portAuthState = _PortAuthState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 8, 3),
    _PortAuthState_Type()
)
portAuthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthState.setStatus("current")
_HwMonitorInfo_ObjectIdentity = ObjectIdentity
hwMonitorInfo = _HwMonitorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9)
)
_FanRpmTable_Object = MibTable
fanRpmTable = _FanRpmTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 1)
)
if mibBuilder.loadTexts:
    fanRpmTable.setStatus("current")
_FanRpmEntry_Object = MibTableRow
fanRpmEntry = _FanRpmEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 1, 1)
)
fanRpmEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "fanRpmIndex"),
)
if mibBuilder.loadTexts:
    fanRpmEntry.setStatus("current")
_FanRpmIndex_Type = Integer32
_FanRpmIndex_Object = MibTableColumn
fanRpmIndex = _FanRpmIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 1, 1, 1),
    _FanRpmIndex_Type()
)
fanRpmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmIndex.setStatus("current")
_FanRpmName_Type = DisplayString
_FanRpmName_Object = MibTableColumn
fanRpmName = _FanRpmName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 1, 1, 2),
    _FanRpmName_Type()
)
fanRpmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmName.setStatus("current")
_FanRpmCurValue_Type = Integer32
_FanRpmCurValue_Object = MibTableColumn
fanRpmCurValue = _FanRpmCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 1, 1, 3),
    _FanRpmCurValue_Type()
)
fanRpmCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmCurValue.setStatus("current")
_FanRpmMaxValue_Type = Integer32
_FanRpmMaxValue_Object = MibTableColumn
fanRpmMaxValue = _FanRpmMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 1, 1, 4),
    _FanRpmMaxValue_Type()
)
fanRpmMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmMaxValue.setStatus("current")
_FanRpmMinValue_Type = Integer32
_FanRpmMinValue_Object = MibTableColumn
fanRpmMinValue = _FanRpmMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 1, 1, 5),
    _FanRpmMinValue_Type()
)
fanRpmMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmMinValue.setStatus("current")
_FanRpmLowThresh_Type = Integer32
_FanRpmLowThresh_Object = MibTableColumn
fanRpmLowThresh = _FanRpmLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 1, 1, 6),
    _FanRpmLowThresh_Type()
)
fanRpmLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmLowThresh.setStatus("current")
_FanRpmDescr_Type = DisplayString
_FanRpmDescr_Object = MibTableColumn
fanRpmDescr = _FanRpmDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 1, 1, 7),
    _FanRpmDescr_Type()
)
fanRpmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmDescr.setStatus("current")
_TempTable_Object = MibTable
tempTable = _TempTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 2)
)
if mibBuilder.loadTexts:
    tempTable.setStatus("current")
_TempEntry_Object = MibTableRow
tempEntry = _TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 2, 1)
)
tempEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "tempIndex"),
)
if mibBuilder.loadTexts:
    tempEntry.setStatus("current")
_TempIndex_Type = Integer32
_TempIndex_Object = MibTableColumn
tempIndex = _TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 2, 1, 1),
    _TempIndex_Type()
)
tempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempIndex.setStatus("current")
_TempName_Type = DisplayString
_TempName_Object = MibTableColumn
tempName = _TempName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 2, 1, 2),
    _TempName_Type()
)
tempName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempName.setStatus("current")
_TempCurValue_Type = Integer32
_TempCurValue_Object = MibTableColumn
tempCurValue = _TempCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 2, 1, 3),
    _TempCurValue_Type()
)
tempCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempCurValue.setStatus("current")
_TempMaxValue_Type = Integer32
_TempMaxValue_Object = MibTableColumn
tempMaxValue = _TempMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 2, 1, 4),
    _TempMaxValue_Type()
)
tempMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMaxValue.setStatus("current")
_TempMinValue_Type = Integer32
_TempMinValue_Object = MibTableColumn
tempMinValue = _TempMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 2, 1, 5),
    _TempMinValue_Type()
)
tempMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMinValue.setStatus("current")
_TempHighThresh_Type = Integer32
_TempHighThresh_Object = MibTableColumn
tempHighThresh = _TempHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 2, 1, 6),
    _TempHighThresh_Type()
)
tempHighThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHighThresh.setStatus("current")
_TempDescr_Type = DisplayString
_TempDescr_Object = MibTableColumn
tempDescr = _TempDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 2, 1, 7),
    _TempDescr_Type()
)
tempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempDescr.setStatus("current")
_VoltageTable_Object = MibTable
voltageTable = _VoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 3)
)
if mibBuilder.loadTexts:
    voltageTable.setStatus("current")
_VoltageEntry_Object = MibTableRow
voltageEntry = _VoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 3, 1)
)
voltageEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "voltageIndex"),
)
if mibBuilder.loadTexts:
    voltageEntry.setStatus("current")
_VoltageIndex_Type = Integer32
_VoltageIndex_Object = MibTableColumn
voltageIndex = _VoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 3, 1, 1),
    _VoltageIndex_Type()
)
voltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageIndex.setStatus("current")
_VoltageName_Type = DisplayString
_VoltageName_Object = MibTableColumn
voltageName = _VoltageName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 3, 1, 2),
    _VoltageName_Type()
)
voltageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageName.setStatus("current")
_VoltageCurValue_Type = Integer32
_VoltageCurValue_Object = MibTableColumn
voltageCurValue = _VoltageCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 3, 1, 3),
    _VoltageCurValue_Type()
)
voltageCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageCurValue.setStatus("current")
_VoltageMaxValue_Type = Integer32
_VoltageMaxValue_Object = MibTableColumn
voltageMaxValue = _VoltageMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 3, 1, 4),
    _VoltageMaxValue_Type()
)
voltageMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageMaxValue.setStatus("current")
_VoltageMinValue_Type = Integer32
_VoltageMinValue_Object = MibTableColumn
voltageMinValue = _VoltageMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 3, 1, 5),
    _VoltageMinValue_Type()
)
voltageMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageMinValue.setStatus("current")
_VoltageNominalValue_Type = Integer32
_VoltageNominalValue_Object = MibTableColumn
voltageNominalValue = _VoltageNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 3, 1, 6),
    _VoltageNominalValue_Type()
)
voltageNominalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageNominalValue.setStatus("current")
_VoltageLowThresh_Type = Integer32
_VoltageLowThresh_Object = MibTableColumn
voltageLowThresh = _VoltageLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 3, 1, 7),
    _VoltageLowThresh_Type()
)
voltageLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageLowThresh.setStatus("current")
_VoltageDescr_Type = DisplayString
_VoltageDescr_Object = MibTableColumn
voltageDescr = _VoltageDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 9, 3, 1, 8),
    _VoltageDescr_Type()
)
voltageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageDescr.setStatus("current")
_SnmpSetup_ObjectIdentity = ObjectIdentity
snmpSetup = _SnmpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10)
)
_SnmpGetCommunity_Type = DisplayString
_SnmpGetCommunity_Object = MibScalar
snmpGetCommunity = _SnmpGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 1),
    _SnmpGetCommunity_Type()
)
snmpGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGetCommunity.setStatus("current")
_SnmpSetCommunity_Type = DisplayString
_SnmpSetCommunity_Object = MibScalar
snmpSetCommunity = _SnmpSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 2),
    _SnmpSetCommunity_Type()
)
snmpSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSetCommunity.setStatus("current")
_SnmpTrapCommunity_Type = DisplayString
_SnmpTrapCommunity_Object = MibScalar
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 3),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("current")
_SnmpTrapDestTable_Object = MibTable
snmpTrapDestTable = _SnmpTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 4)
)
if mibBuilder.loadTexts:
    snmpTrapDestTable.setStatus("current")
_SnmpTrapDestEntry_Object = MibTableRow
snmpTrapDestEntry = _SnmpTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 4, 1)
)
snmpTrapDestEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "snmpTrapDestIP"),
)
if mibBuilder.loadTexts:
    snmpTrapDestEntry.setStatus("current")
_SnmpTrapDestIP_Type = IpAddress
_SnmpTrapDestIP_Object = MibTableColumn
snmpTrapDestIP = _SnmpTrapDestIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 4, 1, 1),
    _SnmpTrapDestIP_Type()
)
snmpTrapDestIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapDestIP.setStatus("current")
_SnmpTrapDestRowStatus_Type = RowStatus
_SnmpTrapDestRowStatus_Object = MibTableColumn
snmpTrapDestRowStatus = _SnmpTrapDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 4, 1, 2),
    _SnmpTrapDestRowStatus_Type()
)
snmpTrapDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapDestRowStatus.setStatus("current")
_SnmpTrapDestPort_Type = Integer32
_SnmpTrapDestPort_Object = MibTableColumn
snmpTrapDestPort = _SnmpTrapDestPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 4, 1, 3),
    _SnmpTrapDestPort_Type()
)
snmpTrapDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestPort.setStatus("current")


class _SnmpTrapVersion_Type(Integer32):
    """Custom type snmpTrapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2c", 1),
          ("v3", 2))
    )


_SnmpTrapVersion_Type.__name__ = "Integer32"
_SnmpTrapVersion_Object = MibTableColumn
snmpTrapVersion = _SnmpTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 4, 1, 4),
    _SnmpTrapVersion_Type()
)
snmpTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapVersion.setStatus("current")
_SnmpTrapUserName_Type = DisplayString
_SnmpTrapUserName_Object = MibTableColumn
snmpTrapUserName = _SnmpTrapUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 4, 1, 5),
    _SnmpTrapUserName_Type()
)
snmpTrapUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapUserName.setStatus("current")


class _SnmpVersion_Type(Integer32):
    """Custom type snmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v2c", 0),
          ("v3", 1),
          ("v3v2c", 2))
    )


_SnmpVersion_Type.__name__ = "Integer32"
_SnmpVersion_Object = MibScalar
snmpVersion = _SnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 5),
    _SnmpVersion_Type()
)
snmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpVersion.setStatus("current")
_SnmpUserTable_Object = MibTable
snmpUserTable = _SnmpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 6)
)
if mibBuilder.loadTexts:
    snmpUserTable.setStatus("current")
_SnmpUserEntry_Object = MibTableRow
snmpUserEntry = _SnmpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 6, 1)
)
snmpUserEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "snmpUserName"),
)
if mibBuilder.loadTexts:
    snmpUserEntry.setStatus("current")
_SnmpUserName_Type = DisplayString
_SnmpUserName_Object = MibTableColumn
snmpUserName = _SnmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 6, 1, 1),
    _SnmpUserName_Type()
)
snmpUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserName.setStatus("current")


class _SnmpUserSecurityLevel_Type(Integer32):
    """Custom type snmpUserSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 0),
          ("authNoPriv", 1),
          ("authPriv", 2))
    )


_SnmpUserSecurityLevel_Type.__name__ = "Integer32"
_SnmpUserSecurityLevel_Object = MibTableColumn
snmpUserSecurityLevel = _SnmpUserSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 6, 1, 2),
    _SnmpUserSecurityLevel_Type()
)
snmpUserSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserSecurityLevel.setStatus("current")


class _SnmpUserAuthProtocol_Type(Integer32):
    """Custom type snmpUserAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("md5", 0),
          ("sha", 1))
    )


_SnmpUserAuthProtocol_Type.__name__ = "Integer32"
_SnmpUserAuthProtocol_Object = MibTableColumn
snmpUserAuthProtocol = _SnmpUserAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 6, 1, 3),
    _SnmpUserAuthProtocol_Type()
)
snmpUserAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserAuthProtocol.setStatus("current")


class _SnmpUserPrivProtocol_Type(Integer32):
    """Custom type snmpUserPrivProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("des", 0),
          ("aes", 1))
    )


_SnmpUserPrivProtocol_Type.__name__ = "Integer32"
_SnmpUserPrivProtocol_Object = MibTableColumn
snmpUserPrivProtocol = _SnmpUserPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 6, 1, 4),
    _SnmpUserPrivProtocol_Type()
)
snmpUserPrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserPrivProtocol.setStatus("current")
_SnmpUserGroup_Type = DisplayString
_SnmpUserGroup_Object = MibTableColumn
snmpUserGroup = _SnmpUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 6, 1, 5),
    _SnmpUserGroup_Type()
)
snmpUserGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserGroup.setStatus("current")
_SnmpTrapGroupTable_Object = MibTable
snmpTrapGroupTable = _SnmpTrapGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 7)
)
if mibBuilder.loadTexts:
    snmpTrapGroupTable.setStatus("current")
_SnmpTrapGroupEntry_Object = MibTableRow
snmpTrapGroupEntry = _SnmpTrapGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 7, 1)
)
snmpTrapGroupEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "snmpTrapDestIP"),
)
if mibBuilder.loadTexts:
    snmpTrapGroupEntry.setStatus("current")


class _SnmpTrapSystemGroup_Type(Bits):
    """Custom type snmpTrapSystemGroup based on Bits"""
    namedValues = NamedValues(
        *(("coldStart", 0),
          ("warmStart", 1),
          ("fanSpeed", 2),
          ("temperature", 3),
          ("voltage", 4),
          ("reset", 5),
          ("timeSync", 6),
          ("intrusionlock", 7),
          ("externalAlarm", 10),
          ("loopGuard", 13))
    )

_SnmpTrapSystemGroup_Type.__name__ = "Bits"
_SnmpTrapSystemGroup_Object = MibTableColumn
snmpTrapSystemGroup = _SnmpTrapSystemGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 7, 1, 1),
    _SnmpTrapSystemGroup_Type()
)
snmpTrapSystemGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapSystemGroup.setStatus("current")


class _SnmpTrapInterfaceGroup_Type(Bits):
    """Custom type snmpTrapInterfaceGroup based on Bits"""
    namedValues = NamedValues(
        *(("linkup", 0),
          ("linkdown", 1),
          ("autonegotiation", 2),
          ("lldp", 3),
          ("transceiverDdm", 4),
          ("ploam", 6),
          ("omci", 7),
          ("rogue", 8),
          ("remoteOnt", 9))
    )

_SnmpTrapInterfaceGroup_Type.__name__ = "Bits"
_SnmpTrapInterfaceGroup_Object = MibTableColumn
snmpTrapInterfaceGroup = _SnmpTrapInterfaceGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 7, 1, 2),
    _SnmpTrapInterfaceGroup_Type()
)
snmpTrapInterfaceGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapInterfaceGroup.setStatus("current")


class _SnmpTrapAAAGroup_Type(Bits):
    """Custom type snmpTrapAAAGroup based on Bits"""
    namedValues = NamedValues(
        *(("authentication", 0),
          ("accounting", 1))
    )

_SnmpTrapAAAGroup_Type.__name__ = "Bits"
_SnmpTrapAAAGroup_Object = MibTableColumn
snmpTrapAAAGroup = _SnmpTrapAAAGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 7, 1, 3),
    _SnmpTrapAAAGroup_Type()
)
snmpTrapAAAGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapAAAGroup.setStatus("current")


class _SnmpTrapIPGroup_Type(Bits):
    """Custom type snmpTrapIPGroup based on Bits"""
    namedValues = NamedValues(
        *(("ping", 0),
          ("traceroute", 1))
    )

_SnmpTrapIPGroup_Type.__name__ = "Bits"
_SnmpTrapIPGroup_Object = MibTableColumn
snmpTrapIPGroup = _SnmpTrapIPGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 7, 1, 4),
    _SnmpTrapIPGroup_Type()
)
snmpTrapIPGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapIPGroup.setStatus("current")


class _SnmpTrapSwitchGroup_Type(Bits):
    """Custom type snmpTrapSwitchGroup based on Bits"""
    namedValues = NamedValues(
        *(("stp", 0),
          ("mactable", 1),
          ("rmon", 2),
          ("cfm", 3))
    )

_SnmpTrapSwitchGroup_Type.__name__ = "Bits"
_SnmpTrapSwitchGroup_Object = MibTableColumn
snmpTrapSwitchGroup = _SnmpTrapSwitchGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 10, 7, 1, 5),
    _SnmpTrapSwitchGroup_Type()
)
snmpTrapSwitchGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapSwitchGroup.setStatus("current")
_DateTimeSetup_ObjectIdentity = ObjectIdentity
dateTimeSetup = _DateTimeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11)
)


class _DateTimeServerType_Type(Integer32):
    """Custom type dateTimeServerType based on Integer32"""
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
          ("daytime", 2),
          ("time", 3),
          ("ntp", 4))
    )


_DateTimeServerType_Type.__name__ = "Integer32"
_DateTimeServerType_Object = MibScalar
dateTimeServerType = _DateTimeServerType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 1),
    _DateTimeServerType_Type()
)
dateTimeServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeServerType.setStatus("current")
_DateTimeServerIP_Type = IpAddress
_DateTimeServerIP_Object = MibScalar
dateTimeServerIP = _DateTimeServerIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 2),
    _DateTimeServerIP_Type()
)
dateTimeServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeServerIP.setStatus("current")
_DateTimeZone_Type = Integer32
_DateTimeZone_Object = MibScalar
dateTimeZone = _DateTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 3),
    _DateTimeZone_Type()
)
dateTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeZone.setStatus("current")
_DateTimeNewDateYear_Type = Integer32
_DateTimeNewDateYear_Object = MibScalar
dateTimeNewDateYear = _DateTimeNewDateYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 4),
    _DateTimeNewDateYear_Type()
)
dateTimeNewDateYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewDateYear.setStatus("current")
_DateTimeNewDateMonth_Type = Integer32
_DateTimeNewDateMonth_Object = MibScalar
dateTimeNewDateMonth = _DateTimeNewDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 5),
    _DateTimeNewDateMonth_Type()
)
dateTimeNewDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewDateMonth.setStatus("current")
_DateTimeNewDateDay_Type = Integer32
_DateTimeNewDateDay_Object = MibScalar
dateTimeNewDateDay = _DateTimeNewDateDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 6),
    _DateTimeNewDateDay_Type()
)
dateTimeNewDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewDateDay.setStatus("current")
_DateTimeNewTimeHour_Type = Integer32
_DateTimeNewTimeHour_Object = MibScalar
dateTimeNewTimeHour = _DateTimeNewTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 7),
    _DateTimeNewTimeHour_Type()
)
dateTimeNewTimeHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewTimeHour.setStatus("current")
_DateTimeNewTimeMinute_Type = Integer32
_DateTimeNewTimeMinute_Object = MibScalar
dateTimeNewTimeMinute = _DateTimeNewTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 8),
    _DateTimeNewTimeMinute_Type()
)
dateTimeNewTimeMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewTimeMinute.setStatus("current")
_DateTimeNewTimeSecond_Type = Integer32
_DateTimeNewTimeSecond_Object = MibScalar
dateTimeNewTimeSecond = _DateTimeNewTimeSecond_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 9),
    _DateTimeNewTimeSecond_Type()
)
dateTimeNewTimeSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewTimeSecond.setStatus("current")
_DateTimeDaylightSavingTimeSetup_ObjectIdentity = ObjectIdentity
dateTimeDaylightSavingTimeSetup = _DateTimeDaylightSavingTimeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 10)
)
_DaylightSavingTimeState_Type = EnabledStatus
_DaylightSavingTimeState_Object = MibScalar
daylightSavingTimeState = _DaylightSavingTimeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 10, 1),
    _DaylightSavingTimeState_Type()
)
daylightSavingTimeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeState.setStatus("current")


class _DaylightSavingTimeStartDateWeek_Type(Integer32):
    """Custom type daylightSavingTimeStartDateWeek based on Integer32"""
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
        *(("first", 1),
          ("second", 2),
          ("third", 3),
          ("fourth", 4),
          ("last", 5))
    )


_DaylightSavingTimeStartDateWeek_Type.__name__ = "Integer32"
_DaylightSavingTimeStartDateWeek_Object = MibScalar
daylightSavingTimeStartDateWeek = _DaylightSavingTimeStartDateWeek_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 10, 2),
    _DaylightSavingTimeStartDateWeek_Type()
)
daylightSavingTimeStartDateWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeStartDateWeek.setStatus("current")


class _DaylightSavingTimeStartDateDay_Type(Integer32):
    """Custom type daylightSavingTimeStartDateDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sunday", 0),
          ("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6))
    )


_DaylightSavingTimeStartDateDay_Type.__name__ = "Integer32"
_DaylightSavingTimeStartDateDay_Object = MibScalar
daylightSavingTimeStartDateDay = _DaylightSavingTimeStartDateDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 10, 3),
    _DaylightSavingTimeStartDateDay_Type()
)
daylightSavingTimeStartDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeStartDateDay.setStatus("current")


class _DaylightSavingTimeStartDateMonth_Type(Integer32):
    """Custom type daylightSavingTimeStartDateMonth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("january", 1),
          ("february", 2),
          ("march", 3),
          ("april", 4),
          ("may", 5),
          ("june", 6),
          ("july", 7),
          ("august", 8),
          ("september", 9),
          ("october", 10),
          ("november", 11),
          ("december", 12))
    )


_DaylightSavingTimeStartDateMonth_Type.__name__ = "Integer32"
_DaylightSavingTimeStartDateMonth_Object = MibScalar
daylightSavingTimeStartDateMonth = _DaylightSavingTimeStartDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 10, 4),
    _DaylightSavingTimeStartDateMonth_Type()
)
daylightSavingTimeStartDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeStartDateMonth.setStatus("current")
_DaylightSavingTimeStartDateHour_Type = Integer32
_DaylightSavingTimeStartDateHour_Object = MibScalar
daylightSavingTimeStartDateHour = _DaylightSavingTimeStartDateHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 10, 5),
    _DaylightSavingTimeStartDateHour_Type()
)
daylightSavingTimeStartDateHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeStartDateHour.setStatus("current")


class _DaylightSavingTimeEndDateWeek_Type(Integer32):
    """Custom type daylightSavingTimeEndDateWeek based on Integer32"""
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
        *(("first", 1),
          ("second", 2),
          ("third", 3),
          ("fourth", 4),
          ("last", 5))
    )


_DaylightSavingTimeEndDateWeek_Type.__name__ = "Integer32"
_DaylightSavingTimeEndDateWeek_Object = MibScalar
daylightSavingTimeEndDateWeek = _DaylightSavingTimeEndDateWeek_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 10, 6),
    _DaylightSavingTimeEndDateWeek_Type()
)
daylightSavingTimeEndDateWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeEndDateWeek.setStatus("current")


class _DaylightSavingTimeEndDateDay_Type(Integer32):
    """Custom type daylightSavingTimeEndDateDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sunday", 0),
          ("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6))
    )


_DaylightSavingTimeEndDateDay_Type.__name__ = "Integer32"
_DaylightSavingTimeEndDateDay_Object = MibScalar
daylightSavingTimeEndDateDay = _DaylightSavingTimeEndDateDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 10, 7),
    _DaylightSavingTimeEndDateDay_Type()
)
daylightSavingTimeEndDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeEndDateDay.setStatus("current")


class _DaylightSavingTimeEndDateMonth_Type(Integer32):
    """Custom type daylightSavingTimeEndDateMonth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("january", 1),
          ("february", 2),
          ("march", 3),
          ("april", 4),
          ("may", 5),
          ("june", 6),
          ("july", 7),
          ("august", 8),
          ("september", 9),
          ("october", 10),
          ("november", 11),
          ("december", 12))
    )


_DaylightSavingTimeEndDateMonth_Type.__name__ = "Integer32"
_DaylightSavingTimeEndDateMonth_Object = MibScalar
daylightSavingTimeEndDateMonth = _DaylightSavingTimeEndDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 10, 8),
    _DaylightSavingTimeEndDateMonth_Type()
)
daylightSavingTimeEndDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeEndDateMonth.setStatus("current")
_DaylightSavingTimeEndDateHour_Type = Integer32
_DaylightSavingTimeEndDateHour_Object = MibScalar
daylightSavingTimeEndDateHour = _DaylightSavingTimeEndDateHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 11, 10, 9),
    _DaylightSavingTimeEndDateHour_Type()
)
daylightSavingTimeEndDateHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeEndDateHour.setStatus("current")
_SysMgmt_ObjectIdentity = ObjectIdentity
sysMgmt = _SysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12)
)


class _SysMgmtConfigSave_Type(Integer32):
    """Custom type sysMgmtConfigSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config1", 1),
          ("config2", 2))
    )


_SysMgmtConfigSave_Type.__name__ = "Integer32"
_SysMgmtConfigSave_Object = MibScalar
sysMgmtConfigSave = _SysMgmtConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 1),
    _SysMgmtConfigSave_Type()
)
sysMgmtConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtConfigSave.setStatus("current")


class _SysMgmtBootupConfig_Type(Integer32):
    """Custom type sysMgmtBootupConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config1", 1),
          ("config2", 2))
    )


_SysMgmtBootupConfig_Type.__name__ = "Integer32"
_SysMgmtBootupConfig_Object = MibScalar
sysMgmtBootupConfig = _SysMgmtBootupConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 2),
    _SysMgmtBootupConfig_Type()
)
sysMgmtBootupConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtBootupConfig.setStatus("current")


class _SysMgmtReboot_Type(Integer32):
    """Custom type sysMgmtReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("reboot", 1))
    )


_SysMgmtReboot_Type.__name__ = "Integer32"
_SysMgmtReboot_Object = MibScalar
sysMgmtReboot = _SysMgmtReboot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 3),
    _SysMgmtReboot_Type()
)
sysMgmtReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtReboot.setStatus("current")


class _SysMgmtDefaultConfig_Type(Integer32):
    """Custom type sysMgmtDefaultConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("resetToDefault", 1),
          ("resetToDefaultWithoutIp", 2))
    )


_SysMgmtDefaultConfig_Type.__name__ = "Integer32"
_SysMgmtDefaultConfig_Object = MibScalar
sysMgmtDefaultConfig = _SysMgmtDefaultConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 4),
    _SysMgmtDefaultConfig_Type()
)
sysMgmtDefaultConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtDefaultConfig.setStatus("current")


class _SysMgmtLastActionStatus_Type(Integer32):
    """Custom type sysMgmtLastActionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("success", 1),
          ("fail", 2))
    )


_SysMgmtLastActionStatus_Type.__name__ = "Integer32"
_SysMgmtLastActionStatus_Object = MibScalar
sysMgmtLastActionStatus = _SysMgmtLastActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 5),
    _SysMgmtLastActionStatus_Type()
)
sysMgmtLastActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtLastActionStatus.setStatus("current")


class _SysMgmtSystemStatus_Type(Bits):
    """Custom type sysMgmtSystemStatus based on Bits"""
    namedValues = NamedValues(
        *(("sysAlarmDetected", 0),
          ("sysTemperatureError", 1),
          ("sysFanRPMError", 2),
          ("sysVoltageRangeError", 3))
    )

_SysMgmtSystemStatus_Type.__name__ = "Bits"
_SysMgmtSystemStatus_Object = MibScalar
sysMgmtSystemStatus = _SysMgmtSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 6),
    _SysMgmtSystemStatus_Type()
)
sysMgmtSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtSystemStatus.setStatus("current")
_SysMgmtCPUUsage_Type = Integer32
_SysMgmtCPUUsage_Object = MibScalar
sysMgmtCPUUsage = _SysMgmtCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 7),
    _SysMgmtCPUUsage_Type()
)
sysMgmtCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtCPUUsage.setStatus("current")


class _SysMgmtBootupImage_Type(Integer32):
    """Custom type sysMgmtBootupImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("image1", 1),
          ("image2", 2))
    )


_SysMgmtBootupImage_Type.__name__ = "Integer32"
_SysMgmtBootupImage_Object = MibScalar
sysMgmtBootupImage = _SysMgmtBootupImage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 8),
    _SysMgmtBootupImage_Type()
)
sysMgmtBootupImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtBootupImage.setStatus("current")


class _SysMgmtCounterReset_Type(Integer32):
    """Custom type sysMgmtCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SysMgmtCounterReset_Type.__name__ = "Integer32"
_SysMgmtCounterReset_Object = MibScalar
sysMgmtCounterReset = _SysMgmtCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 9),
    _SysMgmtCounterReset_Type()
)
sysMgmtCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtCounterReset.setStatus("current")
_SysMgmtTftpServiceSetup_ObjectIdentity = ObjectIdentity
sysMgmtTftpServiceSetup = _SysMgmtTftpServiceSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 10)
)
_SysMgmtTftpServerIp_Type = IpAddress
_SysMgmtTftpServerIp_Object = MibScalar
sysMgmtTftpServerIp = _SysMgmtTftpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 10, 1),
    _SysMgmtTftpServerIp_Type()
)
sysMgmtTftpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtTftpServerIp.setStatus("current")
_SysMgmtTftpRemoteFileName_Type = DisplayString
_SysMgmtTftpRemoteFileName_Object = MibScalar
sysMgmtTftpRemoteFileName = _SysMgmtTftpRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 10, 2),
    _SysMgmtTftpRemoteFileName_Type()
)
sysMgmtTftpRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtTftpRemoteFileName.setStatus("current")


class _SysMgmtTftpConfigIndex_Type(Integer32):
    """Custom type sysMgmtTftpConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config1", 1),
          ("config2", 2))
    )


_SysMgmtTftpConfigIndex_Type.__name__ = "Integer32"
_SysMgmtTftpConfigIndex_Object = MibScalar
sysMgmtTftpConfigIndex = _SysMgmtTftpConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 10, 3),
    _SysMgmtTftpConfigIndex_Type()
)
sysMgmtTftpConfigIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtTftpConfigIndex.setStatus("current")


class _SysMgmtTftpAction_Type(Integer32):
    """Custom type sysMgmtTftpAction based on Integer32"""
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
          ("backupConfig", 1),
          ("restoreConfig", 2),
          ("mergeConfig", 3))
    )


_SysMgmtTftpAction_Type.__name__ = "Integer32"
_SysMgmtTftpAction_Object = MibScalar
sysMgmtTftpAction = _SysMgmtTftpAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 10, 4),
    _SysMgmtTftpAction_Type()
)
sysMgmtTftpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtTftpAction.setStatus("current")


class _SysMgmtTftpActionStatus_Type(Integer32):
    """Custom type sysMgmtTftpActionStatus based on Integer32"""
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
          ("success", 1),
          ("fail", 2),
          ("underAction", 3))
    )


_SysMgmtTftpActionStatus_Type.__name__ = "Integer32"
_SysMgmtTftpActionStatus_Object = MibScalar
sysMgmtTftpActionStatus = _SysMgmtTftpActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 10, 5),
    _SysMgmtTftpActionStatus_Type()
)
sysMgmtTftpActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtTftpActionStatus.setStatus("current")


class _SysMgmtTftpActionPrivilege13_Type(Integer32):
    """Custom type sysMgmtTftpActionPrivilege13 based on Integer32"""
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
          ("backupConfig", 1),
          ("restoreConfig", 2),
          ("mergeConfig", 3))
    )


_SysMgmtTftpActionPrivilege13_Type.__name__ = "Integer32"
_SysMgmtTftpActionPrivilege13_Object = MibScalar
sysMgmtTftpActionPrivilege13 = _SysMgmtTftpActionPrivilege13_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 10, 113),
    _SysMgmtTftpActionPrivilege13_Type()
)
sysMgmtTftpActionPrivilege13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtTftpActionPrivilege13.setStatus("current")
_SysLoginSetup_ObjectIdentity = ObjectIdentity
sysLoginSetup = _SysLoginSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 11)
)
_LoginLimitMaxNumberOfUser_Type = Integer32
_LoginLimitMaxNumberOfUser_Object = MibScalar
loginLimitMaxNumberOfUser = _LoginLimitMaxNumberOfUser_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 11, 1),
    _LoginLimitMaxNumberOfUser_Type()
)
loginLimitMaxNumberOfUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginLimitMaxNumberOfUser.setStatus("current")
_SysLoginSetupTable_Object = MibTable
sysLoginSetupTable = _SysLoginSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 11, 2)
)
if mibBuilder.loadTexts:
    sysLoginSetupTable.setStatus("current")
_SysLoginSetupEntry_Object = MibTableRow
sysLoginSetupEntry = _SysLoginSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 11, 2, 1)
)
sysLoginSetupEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "sysLoginName"),
)
if mibBuilder.loadTexts:
    sysLoginSetupEntry.setStatus("current")
_SysLoginName_Type = DisplayString
_SysLoginName_Object = MibTableColumn
sysLoginName = _SysLoginName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 11, 2, 1, 1),
    _SysLoginName_Type()
)
sysLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLoginName.setStatus("current")
_SysLoginPassword_Type = DisplayString
_SysLoginPassword_Object = MibTableColumn
sysLoginPassword = _SysLoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 11, 2, 1, 2),
    _SysLoginPassword_Type()
)
sysLoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLoginPassword.setStatus("current")
_SysLoginPrivilege_Type = Integer32
_SysLoginPrivilege_Object = MibTableColumn
sysLoginPrivilege = _SysLoginPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 11, 2, 1, 3),
    _SysLoginPrivilege_Type()
)
sysLoginPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLoginPrivilege.setStatus("current")
_SysLoginRowStatus_Type = RowStatus
_SysLoginRowStatus_Object = MibTableColumn
sysLoginRowStatus = _SysLoginRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 11, 2, 1, 4),
    _SysLoginRowStatus_Type()
)
sysLoginRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysLoginRowStatus.setStatus("current")


class _SysMgmtCPUUsageThreshold_Type(Integer32):
    """Custom type sysMgmtCPUUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysMgmtCPUUsageThreshold_Type.__name__ = "Integer32"
_SysMgmtCPUUsageThreshold_Object = MibScalar
sysMgmtCPUUsageThreshold = _SysMgmtCPUUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 12),
    _SysMgmtCPUUsageThreshold_Type()
)
sysMgmtCPUUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtCPUUsageThreshold.setStatus("current")


class _SysMgmtMemoryUsageThreshold_Type(Integer32):
    """Custom type sysMgmtMemoryUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysMgmtMemoryUsageThreshold_Type.__name__ = "Integer32"
_SysMgmtMemoryUsageThreshold_Object = MibScalar
sysMgmtMemoryUsageThreshold = _SysMgmtMemoryUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 13),
    _SysMgmtMemoryUsageThreshold_Type()
)
sysMgmtMemoryUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtMemoryUsageThreshold.setStatus("current")
_SysMgmtUartLogoutTime_Type = Integer32
_SysMgmtUartLogoutTime_Object = MibScalar
sysMgmtUartLogoutTime = _SysMgmtUartLogoutTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 14),
    _SysMgmtUartLogoutTime_Type()
)
sysMgmtUartLogoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtUartLogoutTime.setStatus("current")


class _SysMgmtConfigSavePrivilege13_Type(Integer32):
    """Custom type sysMgmtConfigSavePrivilege13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config1", 1),
          ("config2", 2))
    )


_SysMgmtConfigSavePrivilege13_Type.__name__ = "Integer32"
_SysMgmtConfigSavePrivilege13_Object = MibScalar
sysMgmtConfigSavePrivilege13 = _SysMgmtConfigSavePrivilege13_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 113),
    _SysMgmtConfigSavePrivilege13_Type()
)
sysMgmtConfigSavePrivilege13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtConfigSavePrivilege13.setStatus("current")


class _SysMgmtDefaultConfigPrivilege13_Type(Integer32):
    """Custom type sysMgmtDefaultConfigPrivilege13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("resetToDefault", 1))
    )


_SysMgmtDefaultConfigPrivilege13_Type.__name__ = "Integer32"
_SysMgmtDefaultConfigPrivilege13_Object = MibScalar
sysMgmtDefaultConfigPrivilege13 = _SysMgmtDefaultConfigPrivilege13_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 12, 213),
    _SysMgmtDefaultConfigPrivilege13_Type()
)
sysMgmtDefaultConfigPrivilege13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtDefaultConfigPrivilege13.setStatus("current")
_Layer2Setup_ObjectIdentity = ObjectIdentity
layer2Setup = _Layer2Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13)
)


class _VlanTypeSetup_Type(Integer32):
    """Custom type vlanTypeSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dot1Q", 1)
    )


_VlanTypeSetup_Type.__name__ = "Integer32"
_VlanTypeSetup_Object = MibScalar
vlanTypeSetup = _VlanTypeSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 1),
    _VlanTypeSetup_Type()
)
vlanTypeSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTypeSetup.setStatus("current")


class _IgmpSnoopingStateSetup_Type(Integer32):
    """Custom type igmpSnoopingStateSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enableIgmpSnooping", 2),
          ("enableIgmpProxying", 3))
    )


_IgmpSnoopingStateSetup_Type.__name__ = "Integer32"
_IgmpSnoopingStateSetup_Object = MibScalar
igmpSnoopingStateSetup = _IgmpSnoopingStateSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 2),
    _IgmpSnoopingStateSetup_Type()
)
igmpSnoopingStateSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingStateSetup.setStatus("current")
_TagVlanPortIsolationState_Type = EnabledStatus
_TagVlanPortIsolationState_Object = MibScalar
tagVlanPortIsolationState = _TagVlanPortIsolationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 3),
    _TagVlanPortIsolationState_Type()
)
tagVlanPortIsolationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tagVlanPortIsolationState.setStatus("current")
_StpState_Type = EnabledStatus
_StpState_Object = MibScalar
stpState = _StpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 4),
    _StpState_Type()
)
stpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpState.setStatus("current")


class _UnknownMulticastFrameForwarding_Type(Integer32):
    """Custom type unknownMulticastFrameForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flooding", 1),
          ("drop", 2))
    )


_UnknownMulticastFrameForwarding_Type.__name__ = "Integer32"
_UnknownMulticastFrameForwarding_Object = MibScalar
unknownMulticastFrameForwarding = _UnknownMulticastFrameForwarding_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 6),
    _UnknownMulticastFrameForwarding_Type()
)
unknownMulticastFrameForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unknownMulticastFrameForwarding.setStatus("current")
_MulticastGrpHostTimeout_Type = Integer32
_MulticastGrpHostTimeout_Object = MibScalar
multicastGrpHostTimeout = _MulticastGrpHostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 7),
    _MulticastGrpHostTimeout_Type()
)
multicastGrpHostTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastGrpHostTimeout.setStatus("current")
_MulticastLeaveTimeout_Type = Integer32
_MulticastLeaveTimeout_Object = MibScalar
multicastLeaveTimeout = _MulticastLeaveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 8),
    _MulticastLeaveTimeout_Type()
)
multicastLeaveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastLeaveTimeout.setStatus("current")


class _ReservedMulticastFrameForwarding_Type(Integer32):
    """Custom type reservedMulticastFrameForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flooding", 1),
          ("drop", 2))
    )


_ReservedMulticastFrameForwarding_Type.__name__ = "Integer32"
_ReservedMulticastFrameForwarding_Object = MibScalar
reservedMulticastFrameForwarding = _ReservedMulticastFrameForwarding_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 9),
    _ReservedMulticastFrameForwarding_Type()
)
reservedMulticastFrameForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reservedMulticastFrameForwarding.setStatus("current")
_Igmpsnp8021pPriority_Type = Integer32
_Igmpsnp8021pPriority_Object = MibScalar
igmpsnp8021pPriority = _Igmpsnp8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 10),
    _Igmpsnp8021pPriority_Type()
)
igmpsnp8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsnp8021pPriority.setStatus("current")


class _IgmpsnpVlanMode_Type(Integer32):
    """Custom type igmpsnpVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fixed", 2))
    )


_IgmpsnpVlanMode_Type.__name__ = "Integer32"
_IgmpsnpVlanMode_Object = MibScalar
igmpsnpVlanMode = _IgmpsnpVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 11),
    _IgmpsnpVlanMode_Type()
)
igmpsnpVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsnpVlanMode.setStatus("current")


class _StpMode_Type(Integer32):
    """Custom type stpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 1),
          ("mstp", 2))
    )


_StpMode_Type.__name__ = "Integer32"
_StpMode_Object = MibScalar
stpMode = _StpMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 12),
    _StpMode_Type()
)
stpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpMode.setStatus("current")
_IgmpsnpVlanTable_Object = MibTable
igmpsnpVlanTable = _IgmpsnpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 13)
)
if mibBuilder.loadTexts:
    igmpsnpVlanTable.setStatus("current")
_IgmpsnpVlanEntry_Object = MibTableRow
igmpsnpVlanEntry = _IgmpsnpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 13, 1)
)
igmpsnpVlanEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "igmpsnpVid"),
)
if mibBuilder.loadTexts:
    igmpsnpVlanEntry.setStatus("current")
_IgmpsnpVid_Type = Integer32
_IgmpsnpVid_Object = MibTableColumn
igmpsnpVid = _IgmpsnpVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 13, 1, 1),
    _IgmpsnpVid_Type()
)
igmpsnpVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsnpVid.setStatus("current")
_IgmpsnpVlanName_Type = DisplayString
_IgmpsnpVlanName_Object = MibTableColumn
igmpsnpVlanName = _IgmpsnpVlanName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 13, 1, 2),
    _IgmpsnpVlanName_Type()
)
igmpsnpVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsnpVlanName.setStatus("current")
_IgmpsnpVlanRowStatus_Type = RowStatus
_IgmpsnpVlanRowStatus_Object = MibTableColumn
igmpsnpVlanRowStatus = _IgmpsnpVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 13, 1, 3),
    _IgmpsnpVlanRowStatus_Type()
)
igmpsnpVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpsnpVlanRowStatus.setStatus("current")
_EthernetCfmStateSetup_Type = EnabledStatus
_EthernetCfmStateSetup_Object = MibScalar
ethernetCfmStateSetup = _EthernetCfmStateSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 15),
    _EthernetCfmStateSetup_Type()
)
ethernetCfmStateSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetCfmStateSetup.setStatus("current")
_LldpStateSetup_Type = EnabledStatus
_LldpStateSetup_Object = MibScalar
lldpStateSetup = _LldpStateSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 16),
    _LldpStateSetup_Type()
)
lldpStateSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpStateSetup.setStatus("current")
_SmartIsolationState_Type = EnabledStatus
_SmartIsolationState_Object = MibScalar
smartIsolationState = _SmartIsolationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 18),
    _SmartIsolationState_Type()
)
smartIsolationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartIsolationState.setStatus("current")
_MgmdMLDsupport_Type = EnabledStatus
_MgmdMLDsupport_Object = MibScalar
mgmdMLDsupport = _MgmdMLDsupport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 19),
    _MgmdMLDsupport_Type()
)
mgmdMLDsupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmdMLDsupport.setStatus("current")
_Mgmdv3mode_Type = EnabledStatus
_Mgmdv3mode_Object = MibScalar
mgmdv3mode = _Mgmdv3mode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 20),
    _Mgmdv3mode_Type()
)
mgmdv3mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmdv3mode.setStatus("current")


class _MgmdReportTag_Type(Integer32):
    """Custom type mgmdReportTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mvlan", 0),
          ("aniVlan", 1))
    )


_MgmdReportTag_Type.__name__ = "Integer32"
_MgmdReportTag_Object = MibScalar
mgmdReportTag = _MgmdReportTag_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 21),
    _MgmdReportTag_Type()
)
mgmdReportTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmdReportTag.setStatus("current")
_MgmdIgmpProxyWorkingIP_Type = IpAddress
_MgmdIgmpProxyWorkingIP_Object = MibScalar
mgmdIgmpProxyWorkingIP = _MgmdIgmpProxyWorkingIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 22),
    _MgmdIgmpProxyWorkingIP_Type()
)
mgmdIgmpProxyWorkingIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmdIgmpProxyWorkingIP.setStatus("current")


class _MgmdQueryTag_Type(Integer32):
    """Custom type mgmdQueryTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mvlan", 0),
          ("aniVlan", 1))
    )


_MgmdQueryTag_Type.__name__ = "Integer32"
_MgmdQueryTag_Object = MibScalar
mgmdQueryTag = _MgmdQueryTag_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 23),
    _MgmdQueryTag_Type()
)
mgmdQueryTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmdQueryTag.setStatus("current")


class _DsMeterMacroMode_Type(Integer32):
    """Custom type dsMeterMacroMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pir", 0),
          ("cir", 1))
    )


_DsMeterMacroMode_Type.__name__ = "Integer32"
_DsMeterMacroMode_Object = MibScalar
dsMeterMacroMode = _DsMeterMacroMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 13, 24),
    _DsMeterMacroMode_Type()
)
dsMeterMacroMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMeterMacroMode.setStatus("current")
_IpSetup_ObjectIdentity = ObjectIdentity
ipSetup = _IpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 14)
)
_DnsIpAddress_Type = IpAddress
_DnsIpAddress_Object = MibScalar
dnsIpAddress = _DnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 14, 1),
    _DnsIpAddress_Type()
)
dnsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsIpAddress.setStatus("current")


class _DefaultMgmt_Type(Integer32):
    """Custom type defaultMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inBand", 0),
          ("outOfBand", 1))
    )


_DefaultMgmt_Type.__name__ = "Integer32"
_DefaultMgmt_Object = MibScalar
defaultMgmt = _DefaultMgmt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 14, 2),
    _DefaultMgmt_Type()
)
defaultMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultMgmt.setStatus("current")
_DefaultGateway_Type = IpAddress
_DefaultGateway_Object = MibScalar
defaultGateway = _DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 14, 3),
    _DefaultGateway_Type()
)
defaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultGateway.setStatus("current")
_OutOfBandIpSetup_ObjectIdentity = ObjectIdentity
outOfBandIpSetup = _OutOfBandIpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 14, 4)
)
_OutOfBandIp_Type = IpAddress
_OutOfBandIp_Object = MibScalar
outOfBandIp = _OutOfBandIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 14, 4, 1),
    _OutOfBandIp_Type()
)
outOfBandIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outOfBandIp.setStatus("current")
_OutOfBandSubnetMask_Type = IpAddress
_OutOfBandSubnetMask_Object = MibScalar
outOfBandSubnetMask = _OutOfBandSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 14, 4, 2),
    _OutOfBandSubnetMask_Type()
)
outOfBandSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outOfBandSubnetMask.setStatus("current")
_OutOfBandGateway_Type = IpAddress
_OutOfBandGateway_Object = MibScalar
outOfBandGateway = _OutOfBandGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 14, 4, 3),
    _OutOfBandGateway_Type()
)
outOfBandGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outOfBandGateway.setStatus("current")
_MaxNumOfInbandIp_Type = Integer32
_MaxNumOfInbandIp_Object = MibScalar
maxNumOfInbandIp = _MaxNumOfInbandIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 14, 5),
    _MaxNumOfInbandIp_Type()
)
maxNumOfInbandIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfInbandIp.setStatus("current")
_InbandIpTable_Object = MibTable
inbandIpTable = _InbandIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 14, 6)
)
if mibBuilder.loadTexts:
    inbandIpTable.setStatus("current")
_InbandIpEntry_Object = MibTableRow
inbandIpEntry = _InbandIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 14, 6, 1)
)
inbandIpEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "inbandEntryIp"),
    (0, "ZYXEL-olt1408-MIB", "inbandEntrySubnetMask"),
)
if mibBuilder.loadTexts:
    inbandIpEntry.setStatus("current")
_InbandEntryIp_Type = IpAddress
_InbandEntryIp_Object = MibTableColumn
inbandEntryIp = _InbandEntryIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 14, 6, 1, 1),
    _InbandEntryIp_Type()
)
inbandEntryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandEntryIp.setStatus("current")
_InbandEntrySubnetMask_Type = IpAddress
_InbandEntrySubnetMask_Object = MibTableColumn
inbandEntrySubnetMask = _InbandEntrySubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 14, 6, 1, 2),
    _InbandEntrySubnetMask_Type()
)
inbandEntrySubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandEntrySubnetMask.setStatus("current")
_InbandEntryVid_Type = Integer32
_InbandEntryVid_Object = MibTableColumn
inbandEntryVid = _InbandEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 14, 6, 1, 3),
    _InbandEntryVid_Type()
)
inbandEntryVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandEntryVid.setStatus("current")
_InbandEntryRowStatus_Type = RowStatus
_InbandEntryRowStatus_Object = MibTableColumn
inbandEntryRowStatus = _InbandEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 14, 6, 1, 4),
    _InbandEntryRowStatus_Type()
)
inbandEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inbandEntryRowStatus.setStatus("current")
_FilterSetup_ObjectIdentity = ObjectIdentity
filterSetup = _FilterSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 15)
)
_FilterTable_Object = MibTable
filterTable = _FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 15, 1)
)
if mibBuilder.loadTexts:
    filterTable.setStatus("current")
_FilterEntry_Object = MibTableRow
filterEntry = _FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 15, 1, 1)
)
filterEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "filterMacAddr"),
    (0, "ZYXEL-olt1408-MIB", "filterVid"),
)
if mibBuilder.loadTexts:
    filterEntry.setStatus("current")
_FilterName_Type = DisplayString
_FilterName_Object = MibTableColumn
filterName = _FilterName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 15, 1, 1, 1),
    _FilterName_Type()
)
filterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterName.setStatus("current")


class _FilterActionState_Type(Integer32):
    """Custom type filterActionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discardSource", 1),
          ("discardDestination", 2),
          ("both", 3))
    )


_FilterActionState_Type.__name__ = "Integer32"
_FilterActionState_Object = MibTableColumn
filterActionState = _FilterActionState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 15, 1, 1, 2),
    _FilterActionState_Type()
)
filterActionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterActionState.setStatus("current")
_FilterMacAddr_Type = MacAddress
_FilterMacAddr_Object = MibTableColumn
filterMacAddr = _FilterMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 15, 1, 1, 3),
    _FilterMacAddr_Type()
)
filterMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    filterMacAddr.setStatus("current")
_FilterVid_Type = Integer32
_FilterVid_Object = MibTableColumn
filterVid = _FilterVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 15, 1, 1, 4),
    _FilterVid_Type()
)
filterVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    filterVid.setStatus("current")
_FilterRowStatus_Type = RowStatus
_FilterRowStatus_Object = MibTableColumn
filterRowStatus = _FilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 15, 1, 1, 5),
    _FilterRowStatus_Type()
)
filterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRowStatus.setStatus("current")
_MirrorSetup_ObjectIdentity = ObjectIdentity
mirrorSetup = _MirrorSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 16)
)
_MirrorState_Type = EnabledStatus
_MirrorState_Object = MibScalar
mirrorState = _MirrorState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 16, 1),
    _MirrorState_Type()
)
mirrorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorState.setStatus("current")
_MirrorMonitorPort_Type = Integer32
_MirrorMonitorPort_Object = MibScalar
mirrorMonitorPort = _MirrorMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 16, 2),
    _MirrorMonitorPort_Type()
)
mirrorMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorMonitorPort.setStatus("current")
_MirrorTable_Object = MibTable
mirrorTable = _MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 16, 3)
)
if mibBuilder.loadTexts:
    mirrorTable.setStatus("current")
_MirrorEntry_Object = MibTableRow
mirrorEntry = _MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 16, 3, 1)
)
mirrorEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    mirrorEntry.setStatus("current")
_MirrorMirroredState_Type = EnabledStatus
_MirrorMirroredState_Object = MibTableColumn
mirrorMirroredState = _MirrorMirroredState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 16, 3, 1, 1),
    _MirrorMirroredState_Type()
)
mirrorMirroredState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorMirroredState.setStatus("current")


class _MirrorDirection_Type(Integer32):
    """Custom type mirrorDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 0),
          ("egress", 1),
          ("both", 2))
    )


_MirrorDirection_Type.__name__ = "Integer32"
_MirrorDirection_Object = MibTableColumn
mirrorDirection = _MirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 16, 3, 1, 2),
    _MirrorDirection_Type()
)
mirrorDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorDirection.setStatus("current")


class _MirrorVlan_Type(Integer32):
    """Custom type mirrorVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MirrorVlan_Type.__name__ = "Integer32"
_MirrorVlan_Object = MibScalar
mirrorVlan = _MirrorVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 16, 4),
    _MirrorVlan_Type()
)
mirrorVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorVlan.setStatus("current")
_AggrSetup_ObjectIdentity = ObjectIdentity
aggrSetup = _AggrSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17)
)
_AggrState_Type = EnabledStatus
_AggrState_Object = MibScalar
aggrState = _AggrState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17, 1),
    _AggrState_Type()
)
aggrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrState.setStatus("current")


class _AggrSystemPriority_Type(Integer32):
    """Custom type aggrSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AggrSystemPriority_Type.__name__ = "Integer32"
_AggrSystemPriority_Object = MibScalar
aggrSystemPriority = _AggrSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17, 2),
    _AggrSystemPriority_Type()
)
aggrSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrSystemPriority.setStatus("current")
_AggrGroupTable_Object = MibTable
aggrGroupTable = _AggrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17, 3)
)
if mibBuilder.loadTexts:
    aggrGroupTable.setStatus("current")
_AggrGroupEntry_Object = MibTableRow
aggrGroupEntry = _AggrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17, 3, 1)
)
aggrGroupEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "aggrGroupIndex"),
)
if mibBuilder.loadTexts:
    aggrGroupEntry.setStatus("current")
_AggrGroupIndex_Type = Integer32
_AggrGroupIndex_Object = MibTableColumn
aggrGroupIndex = _AggrGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17, 3, 1, 1),
    _AggrGroupIndex_Type()
)
aggrGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrGroupIndex.setStatus("current")
_AggrGroupState_Type = EnabledStatus
_AggrGroupState_Object = MibTableColumn
aggrGroupState = _AggrGroupState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17, 3, 1, 2),
    _AggrGroupState_Type()
)
aggrGroupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrGroupState.setStatus("current")
_AggrGroupDynamicState_Type = EnabledStatus
_AggrGroupDynamicState_Object = MibTableColumn
aggrGroupDynamicState = _AggrGroupDynamicState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17, 3, 1, 3),
    _AggrGroupDynamicState_Type()
)
aggrGroupDynamicState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrGroupDynamicState.setStatus("current")


class _AggrGroupCriteria_Type(Integer32):
    """Custom type aggrGroupCriteria based on Integer32"""
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
        *(("srcMac", 1),
          ("dstMac", 2),
          ("srcDstMac", 3),
          ("srcIp", 4),
          ("dstIp", 5),
          ("srcDstIp", 6))
    )


_AggrGroupCriteria_Type.__name__ = "Integer32"
_AggrGroupCriteria_Object = MibTableColumn
aggrGroupCriteria = _AggrGroupCriteria_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17, 3, 1, 4),
    _AggrGroupCriteria_Type()
)
aggrGroupCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrGroupCriteria.setStatus("current")
_AggrPortTable_Object = MibTable
aggrPortTable = _AggrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17, 4)
)
if mibBuilder.loadTexts:
    aggrPortTable.setStatus("current")
_AggrPortEntry_Object = MibTableRow
aggrPortEntry = _AggrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17, 4, 1)
)
aggrPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    aggrPortEntry.setStatus("current")


class _AggrPortGroup_Type(Integer32):
    """Custom type aggrPortGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("t1", 1),
          ("t2", 2))
    )


_AggrPortGroup_Type.__name__ = "Integer32"
_AggrPortGroup_Object = MibTableColumn
aggrPortGroup = _AggrPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17, 4, 1, 1),
    _AggrPortGroup_Type()
)
aggrPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrPortGroup.setStatus("current")


class _AggrPortDynamicStateTimeout_Type(Integer32):
    """Custom type aggrPortDynamicStateTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(30, 30),
    )


_AggrPortDynamicStateTimeout_Type.__name__ = "Integer32"
_AggrPortDynamicStateTimeout_Object = MibTableColumn
aggrPortDynamicStateTimeout = _AggrPortDynamicStateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17, 4, 1, 2),
    _AggrPortDynamicStateTimeout_Type()
)
aggrPortDynamicStateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrPortDynamicStateTimeout.setStatus("current")
_AggrStatusTable_Object = MibTable
aggrStatusTable = _AggrStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17, 5)
)
if mibBuilder.loadTexts:
    aggrStatusTable.setStatus("current")
_AggrStatusEntry_Object = MibTableRow
aggrStatusEntry = _AggrStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17, 5, 1)
)
aggrStatusEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "aggrGroupIndex"),
)
if mibBuilder.loadTexts:
    aggrStatusEntry.setStatus("current")
_AggrStatusActorID_Type = DisplayString
_AggrStatusActorID_Object = MibTableColumn
aggrStatusActorID = _AggrStatusActorID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17, 5, 1, 1),
    _AggrStatusActorID_Type()
)
aggrStatusActorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrStatusActorID.setStatus("current")
_AggrStatusPartnerID_Type = DisplayString
_AggrStatusPartnerID_Object = MibTableColumn
aggrStatusPartnerID = _AggrStatusPartnerID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17, 5, 1, 2),
    _AggrStatusPartnerID_Type()
)
aggrStatusPartnerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrStatusPartnerID.setStatus("current")
_AggrStatusLinkPorts_Type = PortList
_AggrStatusLinkPorts_Object = MibTableColumn
aggrStatusLinkPorts = _AggrStatusLinkPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17, 5, 1, 3),
    _AggrStatusLinkPorts_Type()
)
aggrStatusLinkPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrStatusLinkPorts.setStatus("current")
_AggrStatusSyncPorts_Type = PortList
_AggrStatusSyncPorts_Object = MibTableColumn
aggrStatusSyncPorts = _AggrStatusSyncPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 17, 5, 1, 4),
    _AggrStatusSyncPorts_Type()
)
aggrStatusSyncPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrStatusSyncPorts.setStatus("current")
_AccessCtlSetup_ObjectIdentity = ObjectIdentity
accessCtlSetup = _AccessCtlSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 18)
)
_AccessCtlTable_Object = MibTable
accessCtlTable = _AccessCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 18, 1)
)
if mibBuilder.loadTexts:
    accessCtlTable.setStatus("current")
_AccessCtlEntry_Object = MibTableRow
accessCtlEntry = _AccessCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 18, 1, 1)
)
accessCtlEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "accessCtlService"),
)
if mibBuilder.loadTexts:
    accessCtlEntry.setStatus("current")


class _AccessCtlService_Type(Integer32):
    """Custom type accessCtlService based on Integer32"""
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
        *(("telnet", 1),
          ("ssh", 2),
          ("ftp", 3),
          ("http", 4),
          ("https", 5),
          ("icmp", 6),
          ("snmp", 7))
    )


_AccessCtlService_Type.__name__ = "Integer32"
_AccessCtlService_Object = MibTableColumn
accessCtlService = _AccessCtlService_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 18, 1, 1, 1),
    _AccessCtlService_Type()
)
accessCtlService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessCtlService.setStatus("current")
_AccessCtlEnable_Type = EnabledStatus
_AccessCtlEnable_Object = MibTableColumn
accessCtlEnable = _AccessCtlEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 18, 1, 1, 2),
    _AccessCtlEnable_Type()
)
accessCtlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtlEnable.setStatus("current")
_AccessCtlServicePort_Type = Integer32
_AccessCtlServicePort_Object = MibTableColumn
accessCtlServicePort = _AccessCtlServicePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 18, 1, 1, 3),
    _AccessCtlServicePort_Type()
)
accessCtlServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtlServicePort.setStatus("current")
_AccessCtlTimeout_Type = Integer32
_AccessCtlTimeout_Object = MibTableColumn
accessCtlTimeout = _AccessCtlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 18, 1, 1, 4),
    _AccessCtlTimeout_Type()
)
accessCtlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtlTimeout.setStatus("current")
_SecuredClientTable_Object = MibTable
securedClientTable = _SecuredClientTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 18, 2)
)
if mibBuilder.loadTexts:
    securedClientTable.setStatus("current")
_SecuredClientEntry_Object = MibTableRow
securedClientEntry = _SecuredClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 18, 2, 1)
)
securedClientEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "securedClientIndex"),
)
if mibBuilder.loadTexts:
    securedClientEntry.setStatus("current")
_SecuredClientIndex_Type = Integer32
_SecuredClientIndex_Object = MibTableColumn
securedClientIndex = _SecuredClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 18, 2, 1, 1),
    _SecuredClientIndex_Type()
)
securedClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securedClientIndex.setStatus("current")
_SecuredClientEnable_Type = EnabledStatus
_SecuredClientEnable_Object = MibTableColumn
securedClientEnable = _SecuredClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 18, 2, 1, 2),
    _SecuredClientEnable_Type()
)
securedClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEnable.setStatus("current")
_SecuredClientStartIp_Type = IpAddress
_SecuredClientStartIp_Object = MibTableColumn
securedClientStartIp = _SecuredClientStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 18, 2, 1, 3),
    _SecuredClientStartIp_Type()
)
securedClientStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientStartIp.setStatus("current")
_SecuredClientEndIp_Type = IpAddress
_SecuredClientEndIp_Object = MibTableColumn
securedClientEndIp = _SecuredClientEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 18, 2, 1, 4),
    _SecuredClientEndIp_Type()
)
securedClientEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEndIp.setStatus("current")


class _SecuredClientService_Type(Bits):
    """Custom type securedClientService based on Bits"""
    namedValues = NamedValues(
        *(("telnet", 0),
          ("ftp", 1),
          ("http", 2),
          ("icmp", 3),
          ("snmp", 4),
          ("ssh", 5),
          ("https", 6))
    )

_SecuredClientService_Type.__name__ = "Bits"
_SecuredClientService_Object = MibTableColumn
securedClientService = _SecuredClientService_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 18, 2, 1, 5),
    _SecuredClientService_Type()
)
securedClientService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientService.setStatus("current")
_QueuingMethodSetup_ObjectIdentity = ObjectIdentity
queuingMethodSetup = _QueuingMethodSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 19)
)
_PortQueuingMethodTable_Object = MibTable
portQueuingMethodTable = _PortQueuingMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 19, 1)
)
if mibBuilder.loadTexts:
    portQueuingMethodTable.setStatus("current")
_PortQueuingMethodEntry_Object = MibTableRow
portQueuingMethodEntry = _PortQueuingMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 19, 1, 1)
)
portQueuingMethodEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "portQueuingMethodQueue"),
)
if mibBuilder.loadTexts:
    portQueuingMethodEntry.setStatus("current")
_PortQueuingMethodQueue_Type = Integer32
_PortQueuingMethodQueue_Object = MibTableColumn
portQueuingMethodQueue = _PortQueuingMethodQueue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 19, 1, 1, 1),
    _PortQueuingMethodQueue_Type()
)
portQueuingMethodQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portQueuingMethodQueue.setStatus("current")
_PortQueuingMethodWeight_Type = Integer32
_PortQueuingMethodWeight_Object = MibTableColumn
portQueuingMethodWeight = _PortQueuingMethodWeight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 19, 1, 1, 2),
    _PortQueuingMethodWeight_Type()
)
portQueuingMethodWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portQueuingMethodWeight.setStatus("current")


class _PortQueuingMethodMode_Type(Integer32):
    """Custom type portQueuingMethodMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("strictlyPriority", 0),
          ("weightedFairScheduling", 1))
    )


_PortQueuingMethodMode_Type.__name__ = "Integer32"
_PortQueuingMethodMode_Object = MibTableColumn
portQueuingMethodMode = _PortQueuingMethodMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 19, 1, 1, 3),
    _PortQueuingMethodMode_Type()
)
portQueuingMethodMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portQueuingMethodMode.setStatus("current")
_PortQueuingMethodHybridSpqTable_Object = MibTable
portQueuingMethodHybridSpqTable = _PortQueuingMethodHybridSpqTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 19, 2)
)
if mibBuilder.loadTexts:
    portQueuingMethodHybridSpqTable.setStatus("current")
_PortQueuingMethodHybridSpqEntry_Object = MibTableRow
portQueuingMethodHybridSpqEntry = _PortQueuingMethodHybridSpqEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 19, 2, 1)
)
portQueuingMethodHybridSpqEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portQueuingMethodHybridSpqEntry.setStatus("current")


class _PortQueuingMethodHybridSpq_Type(Integer32):
    """Custom type portQueuingMethodHybridSpq based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("q0", 1),
          ("q1", 2),
          ("q2", 3),
          ("q3", 4),
          ("q4", 5),
          ("q5", 6),
          ("q6", 7),
          ("q7", 8))
    )


_PortQueuingMethodHybridSpq_Type.__name__ = "Integer32"
_PortQueuingMethodHybridSpq_Object = MibTableColumn
portQueuingMethodHybridSpq = _PortQueuingMethodHybridSpq_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 19, 2, 1, 1),
    _PortQueuingMethodHybridSpq_Type()
)
portQueuingMethodHybridSpq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portQueuingMethodHybridSpq.setStatus("current")
_DhcpSetup_ObjectIdentity = ObjectIdentity
dhcpSetup = _DhcpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20)
)
_GlobalDhcpRelay_ObjectIdentity = ObjectIdentity
globalDhcpRelay = _GlobalDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 1)
)
_GlobalDhcpRelayEnable_Type = EnabledStatus
_GlobalDhcpRelayEnable_Object = MibScalar
globalDhcpRelayEnable = _GlobalDhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 1, 1),
    _GlobalDhcpRelayEnable_Type()
)
globalDhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalDhcpRelayEnable.setStatus("current")
_GlobalDhcpRelayOption82Enable_Type = EnabledStatus
_GlobalDhcpRelayOption82Enable_Object = MibScalar
globalDhcpRelayOption82Enable = _GlobalDhcpRelayOption82Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 1, 2),
    _GlobalDhcpRelayOption82Enable_Type()
)
globalDhcpRelayOption82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalDhcpRelayOption82Enable.setStatus("current")
_GlobalDhcpRelayInfoEnable_Type = EnabledStatus
_GlobalDhcpRelayInfoEnable_Object = MibScalar
globalDhcpRelayInfoEnable = _GlobalDhcpRelayInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 1, 3),
    _GlobalDhcpRelayInfoEnable_Type()
)
globalDhcpRelayInfoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalDhcpRelayInfoEnable.setStatus("current")
_GlobalDhcpRelayInfoData_Type = DisplayString
_GlobalDhcpRelayInfoData_Object = MibScalar
globalDhcpRelayInfoData = _GlobalDhcpRelayInfoData_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 1, 4),
    _GlobalDhcpRelayInfoData_Type()
)
globalDhcpRelayInfoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalDhcpRelayInfoData.setStatus("current")
_MaxNumberOfGlobalDhcpRelayRemoteServer_Type = Integer32
_MaxNumberOfGlobalDhcpRelayRemoteServer_Object = MibScalar
maxNumberOfGlobalDhcpRelayRemoteServer = _MaxNumberOfGlobalDhcpRelayRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 1, 5),
    _MaxNumberOfGlobalDhcpRelayRemoteServer_Type()
)
maxNumberOfGlobalDhcpRelayRemoteServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfGlobalDhcpRelayRemoteServer.setStatus("current")
_GlobalDhcpRelayRemoteServerTable_Object = MibTable
globalDhcpRelayRemoteServerTable = _GlobalDhcpRelayRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 1, 6)
)
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteServerTable.setStatus("current")
_GlobalDhcpRelayRemoteServerEntry_Object = MibTableRow
globalDhcpRelayRemoteServerEntry = _GlobalDhcpRelayRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 1, 6, 1)
)
globalDhcpRelayRemoteServerEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "globalDhcpRelayRemoteServerIp"),
)
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteServerEntry.setStatus("current")
_GlobalDhcpRelayRemoteServerIp_Type = IpAddress
_GlobalDhcpRelayRemoteServerIp_Object = MibTableColumn
globalDhcpRelayRemoteServerIp = _GlobalDhcpRelayRemoteServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 1, 6, 1, 1),
    _GlobalDhcpRelayRemoteServerIp_Type()
)
globalDhcpRelayRemoteServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteServerIp.setStatus("current")
_GlobalDhcpRelayRemoteServerRowStatus_Type = RowStatus
_GlobalDhcpRelayRemoteServerRowStatus_Object = MibTableColumn
globalDhcpRelayRemoteServerRowStatus = _GlobalDhcpRelayRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 1, 6, 1, 2),
    _GlobalDhcpRelayRemoteServerRowStatus_Type()
)
globalDhcpRelayRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteServerRowStatus.setStatus("current")


class _GlobalDhcpRelayOption82Format_Type(Integer32):
    """Custom type globalDhcpRelayOption82Format based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GlobalDhcpRelayOption82Format_Type.__name__ = "Integer32"
_GlobalDhcpRelayOption82Format_Object = MibScalar
globalDhcpRelayOption82Format = _GlobalDhcpRelayOption82Format_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 1, 7),
    _GlobalDhcpRelayOption82Format_Type()
)
globalDhcpRelayOption82Format.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalDhcpRelayOption82Format.setStatus("current")
_DhcpServer_ObjectIdentity = ObjectIdentity
dhcpServer = _DhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 2)
)
_MaxNumberOfDhcpServers_Type = Integer32
_MaxNumberOfDhcpServers_Object = MibScalar
maxNumberOfDhcpServers = _MaxNumberOfDhcpServers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 2, 1),
    _MaxNumberOfDhcpServers_Type()
)
maxNumberOfDhcpServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfDhcpServers.setStatus("current")
_DhcpServerTable_Object = MibTable
dhcpServerTable = _DhcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 2, 2)
)
if mibBuilder.loadTexts:
    dhcpServerTable.setStatus("current")
_DhcpServerEntry_Object = MibTableRow
dhcpServerEntry = _DhcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 2, 2, 1)
)
dhcpServerEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "dhcpServerVid"),
)
if mibBuilder.loadTexts:
    dhcpServerEntry.setStatus("current")
_DhcpServerVid_Type = Integer32
_DhcpServerVid_Object = MibTableColumn
dhcpServerVid = _DhcpServerVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 2, 2, 1, 1),
    _DhcpServerVid_Type()
)
dhcpServerVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerVid.setStatus("current")
_DhcpServerStartAddr_Type = IpAddress
_DhcpServerStartAddr_Object = MibTableColumn
dhcpServerStartAddr = _DhcpServerStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 2, 2, 1, 2),
    _DhcpServerStartAddr_Type()
)
dhcpServerStartAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerStartAddr.setStatus("current")
_DhcpServerPoolSize_Type = Integer32
_DhcpServerPoolSize_Object = MibTableColumn
dhcpServerPoolSize = _DhcpServerPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 2, 2, 1, 3),
    _DhcpServerPoolSize_Type()
)
dhcpServerPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerPoolSize.setStatus("current")
_DhcpServerMask_Type = IpAddress
_DhcpServerMask_Object = MibTableColumn
dhcpServerMask = _DhcpServerMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 2, 2, 1, 4),
    _DhcpServerMask_Type()
)
dhcpServerMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerMask.setStatus("current")
_DhcpServerGateway_Type = IpAddress
_DhcpServerGateway_Object = MibTableColumn
dhcpServerGateway = _DhcpServerGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 2, 2, 1, 5),
    _DhcpServerGateway_Type()
)
dhcpServerGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerGateway.setStatus("current")
_DhcpServerPrimaryDNS_Type = IpAddress
_DhcpServerPrimaryDNS_Object = MibTableColumn
dhcpServerPrimaryDNS = _DhcpServerPrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 2, 2, 1, 6),
    _DhcpServerPrimaryDNS_Type()
)
dhcpServerPrimaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerPrimaryDNS.setStatus("current")
_DhcpServerSecondaryDNS_Type = IpAddress
_DhcpServerSecondaryDNS_Object = MibTableColumn
dhcpServerSecondaryDNS = _DhcpServerSecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 2, 2, 1, 7),
    _DhcpServerSecondaryDNS_Type()
)
dhcpServerSecondaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerSecondaryDNS.setStatus("current")
_DhcpServerRowStatus_Type = RowStatus
_DhcpServerRowStatus_Object = MibTableColumn
dhcpServerRowStatus = _DhcpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 2, 2, 1, 8),
    _DhcpServerRowStatus_Type()
)
dhcpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpServerRowStatus.setStatus("current")
_DhcpRelay_ObjectIdentity = ObjectIdentity
dhcpRelay = _DhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 3)
)
_DhcpRelayInfoData_Type = DisplayString
_DhcpRelayInfoData_Object = MibScalar
dhcpRelayInfoData = _DhcpRelayInfoData_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 3, 1),
    _DhcpRelayInfoData_Type()
)
dhcpRelayInfoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayInfoData.setStatus("current")
_MaxNumberOfDhcpRelay_Type = Integer32
_MaxNumberOfDhcpRelay_Object = MibScalar
maxNumberOfDhcpRelay = _MaxNumberOfDhcpRelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 3, 2),
    _MaxNumberOfDhcpRelay_Type()
)
maxNumberOfDhcpRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfDhcpRelay.setStatus("current")
_MaxNumberOfDhcpRelayRemoteServer_Type = Integer32
_MaxNumberOfDhcpRelayRemoteServer_Object = MibScalar
maxNumberOfDhcpRelayRemoteServer = _MaxNumberOfDhcpRelayRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 3, 3),
    _MaxNumberOfDhcpRelayRemoteServer_Type()
)
maxNumberOfDhcpRelayRemoteServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfDhcpRelayRemoteServer.setStatus("current")
_DhcpRelayRemoteServerTable_Object = MibTable
dhcpRelayRemoteServerTable = _DhcpRelayRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 3, 4)
)
if mibBuilder.loadTexts:
    dhcpRelayRemoteServerTable.setStatus("current")
_DhcpRelayRemoteServerEntry_Object = MibTableRow
dhcpRelayRemoteServerEntry = _DhcpRelayRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 3, 4, 1)
)
dhcpRelayRemoteServerEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "dhcpRelayVid"),
    (0, "ZYXEL-olt1408-MIB", "dhcpRelayRemoteServerIp"),
)
if mibBuilder.loadTexts:
    dhcpRelayRemoteServerEntry.setStatus("current")
_DhcpRelayVid_Type = Integer32
_DhcpRelayVid_Object = MibTableColumn
dhcpRelayVid = _DhcpRelayVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 3, 4, 1, 1),
    _DhcpRelayVid_Type()
)
dhcpRelayVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayVid.setStatus("current")
_DhcpRelayRemoteServerIp_Type = IpAddress
_DhcpRelayRemoteServerIp_Object = MibTableColumn
dhcpRelayRemoteServerIp = _DhcpRelayRemoteServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 3, 4, 1, 2),
    _DhcpRelayRemoteServerIp_Type()
)
dhcpRelayRemoteServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayRemoteServerIp.setStatus("current")
_DhcpRelayRemoteServerRowStatus_Type = RowStatus
_DhcpRelayRemoteServerRowStatus_Object = MibTableColumn
dhcpRelayRemoteServerRowStatus = _DhcpRelayRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 3, 4, 1, 3),
    _DhcpRelayRemoteServerRowStatus_Type()
)
dhcpRelayRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelayRemoteServerRowStatus.setStatus("current")
_DhcpRelayTable_Object = MibTable
dhcpRelayTable = _DhcpRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 3, 5)
)
if mibBuilder.loadTexts:
    dhcpRelayTable.setStatus("current")
_DhcpRelayEntry_Object = MibTableRow
dhcpRelayEntry = _DhcpRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 3, 5, 1)
)
dhcpRelayEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "dhcpRelayVid"),
)
if mibBuilder.loadTexts:
    dhcpRelayEntry.setStatus("current")
_DhcpRelayOption82Enable_Type = EnabledStatus
_DhcpRelayOption82Enable_Object = MibTableColumn
dhcpRelayOption82Enable = _DhcpRelayOption82Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 3, 5, 1, 1),
    _DhcpRelayOption82Enable_Type()
)
dhcpRelayOption82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Enable.setStatus("current")
_DhcpRelayInfoEnable_Type = EnabledStatus
_DhcpRelayInfoEnable_Object = MibTableColumn
dhcpRelayInfoEnable = _DhcpRelayInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 3, 5, 1, 2),
    _DhcpRelayInfoEnable_Type()
)
dhcpRelayInfoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayInfoEnable.setStatus("current")


class _DhcpRelayOption82Format_Type(Integer32):
    """Custom type dhcpRelayOption82Format based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DhcpRelayOption82Format_Type.__name__ = "Integer32"
_DhcpRelayOption82Format_Object = MibTableColumn
dhcpRelayOption82Format = _DhcpRelayOption82Format_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 20, 3, 5, 1, 3),
    _DhcpRelayOption82Format_Type()
)
dhcpRelayOption82Format.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Format.setStatus("current")
_ArpInfo_ObjectIdentity = ObjectIdentity
arpInfo = _ArpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 22)
)
_ArpTable_Object = MibTable
arpTable = _ArpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 22, 1)
)
if mibBuilder.loadTexts:
    arpTable.setStatus("current")
_ArpEntry_Object = MibTableRow
arpEntry = _ArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 22, 1, 1)
)
arpEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "arpIpAddr"),
    (0, "ZYXEL-olt1408-MIB", "arpMacVid"),
)
if mibBuilder.loadTexts:
    arpEntry.setStatus("current")
_ArpIndex_Type = Integer32
_ArpIndex_Object = MibTableColumn
arpIndex = _ArpIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 22, 1, 1, 1),
    _ArpIndex_Type()
)
arpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIndex.setStatus("current")
_ArpIpAddr_Type = IpAddress
_ArpIpAddr_Object = MibTableColumn
arpIpAddr = _ArpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 22, 1, 1, 2),
    _ArpIpAddr_Type()
)
arpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIpAddr.setStatus("current")
_ArpMacAddr_Type = MacAddress
_ArpMacAddr_Object = MibTableColumn
arpMacAddr = _ArpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 22, 1, 1, 3),
    _ArpMacAddr_Type()
)
arpMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpMacAddr.setStatus("current")
_ArpMacVid_Type = Integer32
_ArpMacVid_Object = MibTableColumn
arpMacVid = _ArpMacVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 22, 1, 1, 4),
    _ArpMacVid_Type()
)
arpMacVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpMacVid.setStatus("current")
_ArpType_Type = Integer32
_ArpType_Object = MibTableColumn
arpType = _ArpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 22, 1, 1, 5),
    _ArpType_Type()
)
arpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpType.setStatus("current")
_ArpPort_Type = DisplayString
_ArpPort_Object = MibTableColumn
arpPort = _ArpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 22, 1, 1, 6),
    _ArpPort_Type()
)
arpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpPort.setStatus("current")
_ArpAge_Type = Integer32
_ArpAge_Object = MibTableColumn
arpAge = _ArpAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 22, 1, 1, 7),
    _ArpAge_Type()
)
arpAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpAge.setStatus("current")
_PortOpModeSetup_ObjectIdentity = ObjectIdentity
portOpModeSetup = _PortOpModeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 23)
)
_PortOpModePortTable_Object = MibTable
portOpModePortTable = _PortOpModePortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 23, 1)
)
if mibBuilder.loadTexts:
    portOpModePortTable.setStatus("current")
_PortOpModePortEntry_Object = MibTableRow
portOpModePortEntry = _PortOpModePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 23, 1, 1)
)
portOpModePortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portOpModePortEntry.setStatus("current")


class _PortOpModePortSpeedDuplex_Type(Integer32):
    """Custom type portOpModePortSpeedDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("speed100Full", 4),
          ("speed1000Full", 5),
          ("speed10000Full", 6),
          ("speed2500Full", 8))
    )


_PortOpModePortSpeedDuplex_Type.__name__ = "Integer32"
_PortOpModePortSpeedDuplex_Object = MibTableColumn
portOpModePortSpeedDuplex = _PortOpModePortSpeedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 23, 1, 1, 1),
    _PortOpModePortSpeedDuplex_Type()
)
portOpModePortSpeedDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortSpeedDuplex.setStatus("current")


class _PortOpModePortFlowCntl_Type(Integer32):
    """Custom type portOpModePortFlowCntl based on Integer32"""
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


_PortOpModePortFlowCntl_Type.__name__ = "Integer32"
_PortOpModePortFlowCntl_Object = MibTableColumn
portOpModePortFlowCntl = _PortOpModePortFlowCntl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 23, 1, 1, 2),
    _PortOpModePortFlowCntl_Type()
)
portOpModePortFlowCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortFlowCntl.setStatus("current")


class _PortOpModePortName_Type(OctetString):
    """Custom type portOpModePortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PortOpModePortName_Type.__name__ = "OctetString"
_PortOpModePortName_Object = MibTableColumn
portOpModePortName = _PortOpModePortName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 23, 1, 1, 3),
    _PortOpModePortName_Type()
)
portOpModePortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortName.setStatus("current")


class _PortOpModePortModuleType_Type(Integer32):
    """Custom type portOpModePortModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastEthernet10or100", 0),
          ("gigabitEthernet100or1000", 1),
          ("xgEthernet10000", 2))
    )


_PortOpModePortModuleType_Type.__name__ = "Integer32"
_PortOpModePortModuleType_Object = MibTableColumn
portOpModePortModuleType = _PortOpModePortModuleType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 23, 1, 1, 4),
    _PortOpModePortModuleType_Type()
)
portOpModePortModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortModuleType.setStatus("current")


class _PortOpModePortLinkUpType_Type(Integer32):
    """Custom type portOpModePortLinkUpType based on Integer32"""
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
        *(("down", 0),
          ("utp", 1),
          ("sfp", 2),
          ("xfp", 3),
          ("cx4", 4))
    )


_PortOpModePortLinkUpType_Type.__name__ = "Integer32"
_PortOpModePortLinkUpType_Object = MibTableColumn
portOpModePortLinkUpType = _PortOpModePortLinkUpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 23, 1, 1, 5),
    _PortOpModePortLinkUpType_Type()
)
portOpModePortLinkUpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortLinkUpType.setStatus("current")


class _PortOpModePortCounterReset_Type(Integer32):
    """Custom type portOpModePortCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PortOpModePortCounterReset_Type.__name__ = "Integer32"
_PortOpModePortCounterReset_Object = MibTableColumn
portOpModePortCounterReset = _PortOpModePortCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 23, 1, 1, 8),
    _PortOpModePortCounterReset_Type()
)
portOpModePortCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortCounterReset.setStatus("current")
_PortOpModePortMaxFrameSize_Type = Integer32
_PortOpModePortMaxFrameSize_Object = MibTableColumn
portOpModePortMaxFrameSize = _PortOpModePortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 23, 1, 1, 10),
    _PortOpModePortMaxFrameSize_Type()
)
portOpModePortMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortMaxFrameSize.setStatus("current")
_MulticastPortSetup_ObjectIdentity = ObjectIdentity
multicastPortSetup = _MulticastPortSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 25)
)
_MulticastPortTable_Object = MibTable
multicastPortTable = _MulticastPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 25, 1)
)
if mibBuilder.loadTexts:
    multicastPortTable.setStatus("current")
_MulticastPortEntry_Object = MibTableRow
multicastPortEntry = _MulticastPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 25, 1, 1)
)
multicastPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    multicastPortEntry.setStatus("current")
_MulticastPortImmediateLeave_Type = EnabledStatus
_MulticastPortImmediateLeave_Object = MibTableColumn
multicastPortImmediateLeave = _MulticastPortImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 25, 1, 1, 1),
    _MulticastPortImmediateLeave_Type()
)
multicastPortImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortImmediateLeave.setStatus("current")


class _MulticastPortQueryMode_Type(Integer32):
    """Custom type multicastPortQueryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoMode", 1),
          ("fixMode", 2),
          ("edgeMode", 3))
    )


_MulticastPortQueryMode_Type.__name__ = "Integer32"
_MulticastPortQueryMode_Object = MibTableColumn
multicastPortQueryMode = _MulticastPortQueryMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 25, 1, 1, 5),
    _MulticastPortQueryMode_Type()
)
multicastPortQueryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortQueryMode.setStatus("current")
_MulticastStatus_ObjectIdentity = ObjectIdentity
multicastStatus = _MulticastStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26)
)
_MulticastStatusTable_Object = MibTable
multicastStatusTable = _MulticastStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 1)
)
if mibBuilder.loadTexts:
    multicastStatusTable.setStatus("current")
_MulticastStatusEntry_Object = MibTableRow
multicastStatusEntry = _MulticastStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 1, 1)
)
multicastStatusEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "multicastStatusVlanID"),
    (0, "ZYXEL-olt1408-MIB", "multicastStatusPort"),
    (0, "ZYXEL-olt1408-MIB", "multicastStatusGroup"),
)
if mibBuilder.loadTexts:
    multicastStatusEntry.setStatus("current")
_MulticastStatusIndex_Type = Integer32
_MulticastStatusIndex_Object = MibTableColumn
multicastStatusIndex = _MulticastStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 1, 1, 1),
    _MulticastStatusIndex_Type()
)
multicastStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusIndex.setStatus("current")
_MulticastStatusVlanID_Type = Integer32
_MulticastStatusVlanID_Object = MibTableColumn
multicastStatusVlanID = _MulticastStatusVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 1, 1, 2),
    _MulticastStatusVlanID_Type()
)
multicastStatusVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusVlanID.setStatus("current")
_MulticastStatusPort_Type = Integer32
_MulticastStatusPort_Object = MibTableColumn
multicastStatusPort = _MulticastStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 1, 1, 3),
    _MulticastStatusPort_Type()
)
multicastStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusPort.setStatus("current")
_MulticastStatusGroup_Type = IpAddress
_MulticastStatusGroup_Object = MibTableColumn
multicastStatusGroup = _MulticastStatusGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 1, 1, 4),
    _MulticastStatusGroup_Type()
)
multicastStatusGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusGroup.setStatus("current")
_IgmpCountTable_Object = MibTable
igmpCountTable = _IgmpCountTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 2)
)
if mibBuilder.loadTexts:
    igmpCountTable.setStatus("current")
_IgmpCountEntry_Object = MibTableRow
igmpCountEntry = _IgmpCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 2, 1)
)
igmpCountEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "igmpCountIndex"),
)
if mibBuilder.loadTexts:
    igmpCountEntry.setStatus("current")
_IgmpCountIndex_Type = Integer32
_IgmpCountIndex_Object = MibTableColumn
igmpCountIndex = _IgmpCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 2, 1, 1),
    _IgmpCountIndex_Type()
)
igmpCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountIndex.setStatus("current")
_IgmpCountInQuery_Type = Integer32
_IgmpCountInQuery_Object = MibTableColumn
igmpCountInQuery = _IgmpCountInQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 2, 1, 2),
    _IgmpCountInQuery_Type()
)
igmpCountInQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountInQuery.setStatus("current")
_IgmpCountInReport_Type = Integer32
_IgmpCountInReport_Object = MibTableColumn
igmpCountInReport = _IgmpCountInReport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 2, 1, 3),
    _IgmpCountInReport_Type()
)
igmpCountInReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountInReport.setStatus("current")
_IgmpCountInLeave_Type = Integer32
_IgmpCountInLeave_Object = MibTableColumn
igmpCountInLeave = _IgmpCountInLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 2, 1, 4),
    _IgmpCountInLeave_Type()
)
igmpCountInLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountInLeave.setStatus("current")
_IgmpCountInQueryDrop_Type = Integer32
_IgmpCountInQueryDrop_Object = MibTableColumn
igmpCountInQueryDrop = _IgmpCountInQueryDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 2, 1, 5),
    _IgmpCountInQueryDrop_Type()
)
igmpCountInQueryDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountInQueryDrop.setStatus("current")
_IgmpCountInReportDrop_Type = Integer32
_IgmpCountInReportDrop_Object = MibTableColumn
igmpCountInReportDrop = _IgmpCountInReportDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 2, 1, 6),
    _IgmpCountInReportDrop_Type()
)
igmpCountInReportDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountInReportDrop.setStatus("current")
_IgmpCountInLeaveDrop_Type = Integer32
_IgmpCountInLeaveDrop_Object = MibTableColumn
igmpCountInLeaveDrop = _IgmpCountInLeaveDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 2, 1, 7),
    _IgmpCountInLeaveDrop_Type()
)
igmpCountInLeaveDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountInLeaveDrop.setStatus("current")
_IgmpCountOutQuery_Type = Integer32
_IgmpCountOutQuery_Object = MibTableColumn
igmpCountOutQuery = _IgmpCountOutQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 2, 1, 8),
    _IgmpCountOutQuery_Type()
)
igmpCountOutQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountOutQuery.setStatus("current")
_IgmpCountOutReport_Type = Integer32
_IgmpCountOutReport_Object = MibTableColumn
igmpCountOutReport = _IgmpCountOutReport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 2, 1, 9),
    _IgmpCountOutReport_Type()
)
igmpCountOutReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountOutReport.setStatus("current")
_IgmpCountOutLeave_Type = Integer32
_IgmpCountOutLeave_Object = MibTableColumn
igmpCountOutLeave = _IgmpCountOutLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 2, 1, 10),
    _IgmpCountOutLeave_Type()
)
igmpCountOutLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountOutLeave.setStatus("current")
_MulticastVlanStatusTable_Object = MibTable
multicastVlanStatusTable = _MulticastVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 3)
)
if mibBuilder.loadTexts:
    multicastVlanStatusTable.setStatus("current")
_MulticastVlanStatusEntry_Object = MibTableRow
multicastVlanStatusEntry = _MulticastVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 3, 1)
)
multicastVlanStatusEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "multicastVlanStatusVlanID"),
)
if mibBuilder.loadTexts:
    multicastVlanStatusEntry.setStatus("current")
_MulticastVlanStatusVlanID_Type = Integer32
_MulticastVlanStatusVlanID_Object = MibTableColumn
multicastVlanStatusVlanID = _MulticastVlanStatusVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 3, 1, 1),
    _MulticastVlanStatusVlanID_Type()
)
multicastVlanStatusVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVlanStatusVlanID.setStatus("current")


class _MulticastVlanStatusType_Type(Integer32):
    """Custom type multicastVlanStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("mvr", 2),
          ("static", 3))
    )


_MulticastVlanStatusType_Type.__name__ = "Integer32"
_MulticastVlanStatusType_Object = MibTableColumn
multicastVlanStatusType = _MulticastVlanStatusType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 3, 1, 2),
    _MulticastVlanStatusType_Type()
)
multicastVlanStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVlanStatusType.setStatus("current")
_MulticastVlanQueryPort_Type = PortList
_MulticastVlanQueryPort_Object = MibTableColumn
multicastVlanQueryPort = _MulticastVlanQueryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 3, 1, 3),
    _MulticastVlanQueryPort_Type()
)
multicastVlanQueryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVlanQueryPort.setStatus("current")
_MulticastVlanQuerySrcIp_Type = IpAddress
_MulticastVlanQuerySrcIp_Object = MibTableColumn
multicastVlanQuerySrcIp = _MulticastVlanQuerySrcIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 3, 1, 4),
    _MulticastVlanQuerySrcIp_Type()
)
multicastVlanQuerySrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVlanQuerySrcIp.setStatus("current")
_IgmpCounterPortTable_Object = MibTable
igmpCounterPortTable = _IgmpCounterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 4)
)
if mibBuilder.loadTexts:
    igmpCounterPortTable.setStatus("current")
_IgmpCounterPortEntry_Object = MibTableRow
igmpCounterPortEntry = _IgmpCounterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 4, 1)
)
igmpCounterPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    igmpCounterPortEntry.setStatus("current")
_IgmpCounterPortJoin_Type = Counter32
_IgmpCounterPortJoin_Object = MibTableColumn
igmpCounterPortJoin = _IgmpCounterPortJoin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 4, 1, 1),
    _IgmpCounterPortJoin_Type()
)
igmpCounterPortJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCounterPortJoin.setStatus("current")
_IgmpCounterPortLeave_Type = Counter32
_IgmpCounterPortLeave_Object = MibTableColumn
igmpCounterPortLeave = _IgmpCounterPortLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 4, 1, 2),
    _IgmpCounterPortLeave_Type()
)
igmpCounterPortLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCounterPortLeave.setStatus("current")
_IgmpCounterPortActiveGroup_Type = Integer32
_IgmpCounterPortActiveGroup_Object = MibTableColumn
igmpCounterPortActiveGroup = _IgmpCounterPortActiveGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 4, 1, 3),
    _IgmpCounterPortActiveGroup_Type()
)
igmpCounterPortActiveGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCounterPortActiveGroup.setStatus("current")
_IgmpCounterPortQuery_Type = Counter32
_IgmpCounterPortQuery_Object = MibTableColumn
igmpCounterPortQuery = _IgmpCounterPortQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 4, 1, 4),
    _IgmpCounterPortQuery_Type()
)
igmpCounterPortQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCounterPortQuery.setStatus("current")
_IgmpCounterVlanTable_Object = MibTable
igmpCounterVlanTable = _IgmpCounterVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 5)
)
if mibBuilder.loadTexts:
    igmpCounterVlanTable.setStatus("current")
_IgmpCounterVlanEntry_Object = MibTableRow
igmpCounterVlanEntry = _IgmpCounterVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 5, 1)
)
igmpCounterVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpCounterVlanEntry.setStatus("current")
_IgmpCounterVlanJoin_Type = Counter32
_IgmpCounterVlanJoin_Object = MibTableColumn
igmpCounterVlanJoin = _IgmpCounterVlanJoin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 5, 1, 1),
    _IgmpCounterVlanJoin_Type()
)
igmpCounterVlanJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCounterVlanJoin.setStatus("current")
_IgmpCounterVlanLeave_Type = Counter32
_IgmpCounterVlanLeave_Object = MibTableColumn
igmpCounterVlanLeave = _IgmpCounterVlanLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 5, 1, 2),
    _IgmpCounterVlanLeave_Type()
)
igmpCounterVlanLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCounterVlanLeave.setStatus("current")
_IgmpCounterVlanActiveGroup_Type = Integer32
_IgmpCounterVlanActiveGroup_Object = MibTableColumn
igmpCounterVlanActiveGroup = _IgmpCounterVlanActiveGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 5, 1, 3),
    _IgmpCounterVlanActiveGroup_Type()
)
igmpCounterVlanActiveGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCounterVlanActiveGroup.setStatus("current")
_IgmpCounterVlanQuery_Type = Counter32
_IgmpCounterVlanQuery_Object = MibTableColumn
igmpCounterVlanQuery = _IgmpCounterVlanQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 5, 1, 4),
    _IgmpCounterVlanQuery_Type()
)
igmpCounterVlanQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCounterVlanQuery.setStatus("current")
_MulticastCurrentGroupStatusTable_Object = MibTable
multicastCurrentGroupStatusTable = _MulticastCurrentGroupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 6)
)
if mibBuilder.loadTexts:
    multicastCurrentGroupStatusTable.setStatus("current")
_MulticastCurrentGroupStatusEntry_Object = MibTableRow
multicastCurrentGroupStatusEntry = _MulticastCurrentGroupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 6, 1)
)
multicastCurrentGroupStatusEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "multicastStatusVlanID"),
    (0, "ZYXEL-olt1408-MIB", "multicastStatusGroup"),
)
if mibBuilder.loadTexts:
    multicastCurrentGroupStatusEntry.setStatus("current")
_MulticastCurrentNumberOfActivePort_Type = Integer32
_MulticastCurrentNumberOfActivePort_Object = MibTableColumn
multicastCurrentNumberOfActivePort = _MulticastCurrentNumberOfActivePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 6, 1, 1),
    _MulticastCurrentNumberOfActivePort_Type()
)
multicastCurrentNumberOfActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastCurrentNumberOfActivePort.setStatus("current")
_MulticastClientSrcIpTable_Object = MibTable
multicastClientSrcIpTable = _MulticastClientSrcIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 7)
)
if mibBuilder.loadTexts:
    multicastClientSrcIpTable.setStatus("current")
_MulticastClientSrcIpEntry_Object = MibTableRow
multicastClientSrcIpEntry = _MulticastClientSrcIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 7, 1)
)
multicastClientSrcIpEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "multicastStatusVlanID"),
    (0, "ZYXEL-olt1408-MIB", "multicastStatusPort"),
    (0, "ZYXEL-olt1408-MIB", "multicastStatusGroup"),
    (0, "ZYXEL-olt1408-MIB", "multicastClientSrcIpIndex"),
)
if mibBuilder.loadTexts:
    multicastClientSrcIpEntry.setStatus("current")
_MulticastClientSrcIpIndex_Type = Integer32
_MulticastClientSrcIpIndex_Object = MibTableColumn
multicastClientSrcIpIndex = _MulticastClientSrcIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 7, 1, 1),
    _MulticastClientSrcIpIndex_Type()
)
multicastClientSrcIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastClientSrcIpIndex.setStatus("current")
_MulticastClientSrcIpAddress_Type = IpAddress
_MulticastClientSrcIpAddress_Object = MibTableColumn
multicastClientSrcIpAddress = _MulticastClientSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 7, 1, 2),
    _MulticastClientSrcIpAddress_Type()
)
multicastClientSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastClientSrcIpAddress.setStatus("current")
_MgmdStatusTable_Object = MibTable
mgmdStatusTable = _MgmdStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 8)
)
if mibBuilder.loadTexts:
    mgmdStatusTable.setStatus("current")
_MgmdStatusEntry_Object = MibTableRow
mgmdStatusEntry = _MgmdStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 8, 1)
)
mgmdStatusEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "mgmdStatusVlanID"),
    (0, "ZYXEL-olt1408-MIB", "mgmdStatusPort"),
    (0, "ZYXEL-olt1408-MIB", "mgmdStatusGroupAddressType"),
    (0, "ZYXEL-olt1408-MIB", "mgmdStatusGroupAddress"),
)
if mibBuilder.loadTexts:
    mgmdStatusEntry.setStatus("current")
_MgmdStatusIndex_Type = Integer32
_MgmdStatusIndex_Object = MibTableColumn
mgmdStatusIndex = _MgmdStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 8, 1, 1),
    _MgmdStatusIndex_Type()
)
mgmdStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdStatusIndex.setStatus("current")
_MgmdStatusVlanID_Type = Integer32
_MgmdStatusVlanID_Object = MibTableColumn
mgmdStatusVlanID = _MgmdStatusVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 8, 1, 2),
    _MgmdStatusVlanID_Type()
)
mgmdStatusVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdStatusVlanID.setStatus("current")
_MgmdStatusPort_Type = Integer32
_MgmdStatusPort_Object = MibTableColumn
mgmdStatusPort = _MgmdStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 8, 1, 3),
    _MgmdStatusPort_Type()
)
mgmdStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdStatusPort.setStatus("current")


class _MgmdStatusGroupAddressType_Type(InetAddressType):
    """Custom type mgmdStatusGroupAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_MgmdStatusGroupAddressType_Type.__name__ = "InetAddressType"
_MgmdStatusGroupAddressType_Object = MibTableColumn
mgmdStatusGroupAddressType = _MgmdStatusGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 8, 1, 4),
    _MgmdStatusGroupAddressType_Type()
)
mgmdStatusGroupAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdStatusGroupAddressType.setStatus("current")


class _MgmdStatusGroupAddress_Type(InetAddress):
    """Custom type mgmdStatusGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdStatusGroupAddress_Type.__name__ = "InetAddress"
_MgmdStatusGroupAddress_Object = MibTableColumn
mgmdStatusGroupAddress = _MgmdStatusGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 8, 1, 5),
    _MgmdStatusGroupAddress_Type()
)
mgmdStatusGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdStatusGroupAddress.setStatus("current")


class _MgmdStatusGroupFilterMode_Type(Integer32):
    """Custom type mgmdStatusGroupFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_MgmdStatusGroupFilterMode_Type.__name__ = "Integer32"
_MgmdStatusGroupFilterMode_Object = MibTableColumn
mgmdStatusGroupFilterMode = _MgmdStatusGroupFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 8, 1, 6),
    _MgmdStatusGroupFilterMode_Type()
)
mgmdStatusGroupFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdStatusGroupFilterMode.setStatus("current")
_MgmdStatusGroupUpTime_Type = DisplayString
_MgmdStatusGroupUpTime_Object = MibTableColumn
mgmdStatusGroupUpTime = _MgmdStatusGroupUpTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 8, 1, 7),
    _MgmdStatusGroupUpTime_Type()
)
mgmdStatusGroupUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdStatusGroupUpTime.setStatus("current")
_MgmdCountTable_Object = MibTable
mgmdCountTable = _MgmdCountTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 9)
)
if mibBuilder.loadTexts:
    mgmdCountTable.setStatus("current")
_MgmdCountEntry_Object = MibTableRow
mgmdCountEntry = _MgmdCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 9, 1)
)
mgmdCountEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "mgmdCountIndex"),
)
if mibBuilder.loadTexts:
    mgmdCountEntry.setStatus("current")
_MgmdCountIndex_Type = Integer32
_MgmdCountIndex_Object = MibTableColumn
mgmdCountIndex = _MgmdCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 9, 1, 1),
    _MgmdCountIndex_Type()
)
mgmdCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountIndex.setStatus("current")
_MgmdCountInQuery_Type = Integer32
_MgmdCountInQuery_Object = MibTableColumn
mgmdCountInQuery = _MgmdCountInQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 9, 1, 2),
    _MgmdCountInQuery_Type()
)
mgmdCountInQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountInQuery.setStatus("current")
_MgmdCountInReport_Type = Integer32
_MgmdCountInReport_Object = MibTableColumn
mgmdCountInReport = _MgmdCountInReport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 9, 1, 3),
    _MgmdCountInReport_Type()
)
mgmdCountInReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountInReport.setStatus("current")
_MgmdCountInLeave_Type = Integer32
_MgmdCountInLeave_Object = MibTableColumn
mgmdCountInLeave = _MgmdCountInLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 9, 1, 4),
    _MgmdCountInLeave_Type()
)
mgmdCountInLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountInLeave.setStatus("current")
_MgmdCountInQueryDrop_Type = Integer32
_MgmdCountInQueryDrop_Object = MibTableColumn
mgmdCountInQueryDrop = _MgmdCountInQueryDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 9, 1, 5),
    _MgmdCountInQueryDrop_Type()
)
mgmdCountInQueryDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountInQueryDrop.setStatus("current")
_MgmdCountInReportDrop_Type = Integer32
_MgmdCountInReportDrop_Object = MibTableColumn
mgmdCountInReportDrop = _MgmdCountInReportDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 9, 1, 6),
    _MgmdCountInReportDrop_Type()
)
mgmdCountInReportDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountInReportDrop.setStatus("current")
_MgmdCountInLeaveDrop_Type = Integer32
_MgmdCountInLeaveDrop_Object = MibTableColumn
mgmdCountInLeaveDrop = _MgmdCountInLeaveDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 9, 1, 7),
    _MgmdCountInLeaveDrop_Type()
)
mgmdCountInLeaveDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountInLeaveDrop.setStatus("current")
_MgmdCountOutQuery_Type = Integer32
_MgmdCountOutQuery_Object = MibTableColumn
mgmdCountOutQuery = _MgmdCountOutQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 9, 1, 8),
    _MgmdCountOutQuery_Type()
)
mgmdCountOutQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountOutQuery.setStatus("current")
_MgmdCountOutReport_Type = Integer32
_MgmdCountOutReport_Object = MibTableColumn
mgmdCountOutReport = _MgmdCountOutReport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 9, 1, 9),
    _MgmdCountOutReport_Type()
)
mgmdCountOutReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountOutReport.setStatus("current")
_MgmdCountOutLeave_Type = Integer32
_MgmdCountOutLeave_Object = MibTableColumn
mgmdCountOutLeave = _MgmdCountOutLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 9, 1, 10),
    _MgmdCountOutLeave_Type()
)
mgmdCountOutLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountOutLeave.setStatus("current")
_MgmdVlanStatusTable_Object = MibTable
mgmdVlanStatusTable = _MgmdVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 10)
)
if mibBuilder.loadTexts:
    mgmdVlanStatusTable.setStatus("current")
_MgmdVlanStatusEntry_Object = MibTableRow
mgmdVlanStatusEntry = _MgmdVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 10, 1)
)
mgmdVlanStatusEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "mgmdVlanStatusVlanID"),
)
if mibBuilder.loadTexts:
    mgmdVlanStatusEntry.setStatus("current")
_MgmdVlanStatusVlanID_Type = Integer32
_MgmdVlanStatusVlanID_Object = MibTableColumn
mgmdVlanStatusVlanID = _MgmdVlanStatusVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 10, 1, 1),
    _MgmdVlanStatusVlanID_Type()
)
mgmdVlanStatusVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdVlanStatusVlanID.setStatus("current")


class _MgmdVlanStatusType_Type(Integer32):
    """Custom type mgmdVlanStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("mvr", 2),
          ("static", 3))
    )


_MgmdVlanStatusType_Type.__name__ = "Integer32"
_MgmdVlanStatusType_Object = MibTableColumn
mgmdVlanStatusType = _MgmdVlanStatusType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 10, 1, 2),
    _MgmdVlanStatusType_Type()
)
mgmdVlanStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdVlanStatusType.setStatus("current")
_MgmdVlanQueryPort_Type = PortList
_MgmdVlanQueryPort_Object = MibTableColumn
mgmdVlanQueryPort = _MgmdVlanQueryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 10, 1, 3),
    _MgmdVlanQueryPort_Type()
)
mgmdVlanQueryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdVlanQueryPort.setStatus("current")


class _MgmdVlanQuerySrcIpType_Type(InetAddressType):
    """Custom type mgmdVlanQuerySrcIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_MgmdVlanQuerySrcIpType_Type.__name__ = "InetAddressType"
_MgmdVlanQuerySrcIpType_Object = MibTableColumn
mgmdVlanQuerySrcIpType = _MgmdVlanQuerySrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 10, 1, 4),
    _MgmdVlanQuerySrcIpType_Type()
)
mgmdVlanQuerySrcIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdVlanQuerySrcIpType.setStatus("current")


class _MgmdVlanQuerySrcIp_Type(InetAddress):
    """Custom type mgmdVlanQuerySrcIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdVlanQuerySrcIp_Type.__name__ = "InetAddress"
_MgmdVlanQuerySrcIp_Object = MibTableColumn
mgmdVlanQuerySrcIp = _MgmdVlanQuerySrcIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 10, 1, 5),
    _MgmdVlanQuerySrcIp_Type()
)
mgmdVlanQuerySrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdVlanQuerySrcIp.setStatus("current")
_MgmdCounterPortTable_Object = MibTable
mgmdCounterPortTable = _MgmdCounterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11)
)
if mibBuilder.loadTexts:
    mgmdCounterPortTable.setStatus("current")
_MgmdCounterPortEntry_Object = MibTableRow
mgmdCounterPortEntry = _MgmdCounterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1)
)
mgmdCounterPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    mgmdCounterPortEntry.setStatus("current")
_MgmdCounterPortV1ReportIn_Type = Counter32
_MgmdCounterPortV1ReportIn_Object = MibTableColumn
mgmdCounterPortV1ReportIn = _MgmdCounterPortV1ReportIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 1),
    _MgmdCounterPortV1ReportIn_Type()
)
mgmdCounterPortV1ReportIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortV1ReportIn.setStatus("current")
_MgmdCounterPortV2ReportIn_Type = Counter32
_MgmdCounterPortV2ReportIn_Object = MibTableColumn
mgmdCounterPortV2ReportIn = _MgmdCounterPortV2ReportIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 2),
    _MgmdCounterPortV2ReportIn_Type()
)
mgmdCounterPortV2ReportIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortV2ReportIn.setStatus("current")
_MgmdCounterPortV3ReportIn_Type = Counter32
_MgmdCounterPortV3ReportIn_Object = MibTableColumn
mgmdCounterPortV3ReportIn = _MgmdCounterPortV3ReportIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 3),
    _MgmdCounterPortV3ReportIn_Type()
)
mgmdCounterPortV3ReportIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortV3ReportIn.setStatus("current")
_MgmdCounterPortLeaveIn_Type = Counter32
_MgmdCounterPortLeaveIn_Object = MibTableColumn
mgmdCounterPortLeaveIn = _MgmdCounterPortLeaveIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 4),
    _MgmdCounterPortLeaveIn_Type()
)
mgmdCounterPortLeaveIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortLeaveIn.setStatus("current")
_MgmdCounterPortTotalReportIn_Type = Counter32
_MgmdCounterPortTotalReportIn_Object = MibTableColumn
mgmdCounterPortTotalReportIn = _MgmdCounterPortTotalReportIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 5),
    _MgmdCounterPortTotalReportIn_Type()
)
mgmdCounterPortTotalReportIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortTotalReportIn.setStatus("current")
_MgmdCounterPortV1ReportOut_Type = Counter32
_MgmdCounterPortV1ReportOut_Object = MibTableColumn
mgmdCounterPortV1ReportOut = _MgmdCounterPortV1ReportOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 6),
    _MgmdCounterPortV1ReportOut_Type()
)
mgmdCounterPortV1ReportOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortV1ReportOut.setStatus("current")
_MgmdCounterPortV2ReportOut_Type = Counter32
_MgmdCounterPortV2ReportOut_Object = MibTableColumn
mgmdCounterPortV2ReportOut = _MgmdCounterPortV2ReportOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 7),
    _MgmdCounterPortV2ReportOut_Type()
)
mgmdCounterPortV2ReportOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortV2ReportOut.setStatus("current")
_MgmdCounterPortV3ReportOut_Type = Counter32
_MgmdCounterPortV3ReportOut_Object = MibTableColumn
mgmdCounterPortV3ReportOut = _MgmdCounterPortV3ReportOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 8),
    _MgmdCounterPortV3ReportOut_Type()
)
mgmdCounterPortV3ReportOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortV3ReportOut.setStatus("current")
_MgmdCounterPortLeaveOut_Type = Counter32
_MgmdCounterPortLeaveOut_Object = MibTableColumn
mgmdCounterPortLeaveOut = _MgmdCounterPortLeaveOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 9),
    _MgmdCounterPortLeaveOut_Type()
)
mgmdCounterPortLeaveOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortLeaveOut.setStatus("current")
_MgmdCounterPortTotalReportOut_Type = Counter32
_MgmdCounterPortTotalReportOut_Object = MibTableColumn
mgmdCounterPortTotalReportOut = _MgmdCounterPortTotalReportOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 10),
    _MgmdCounterPortTotalReportOut_Type()
)
mgmdCounterPortTotalReportOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortTotalReportOut.setStatus("current")
_MgmdCounterPortV1QueryIn_Type = Counter32
_MgmdCounterPortV1QueryIn_Object = MibTableColumn
mgmdCounterPortV1QueryIn = _MgmdCounterPortV1QueryIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 11),
    _MgmdCounterPortV1QueryIn_Type()
)
mgmdCounterPortV1QueryIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortV1QueryIn.setStatus("current")
_MgmdCounterPortV2QueryIn_Type = Counter32
_MgmdCounterPortV2QueryIn_Object = MibTableColumn
mgmdCounterPortV2QueryIn = _MgmdCounterPortV2QueryIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 12),
    _MgmdCounterPortV2QueryIn_Type()
)
mgmdCounterPortV2QueryIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortV2QueryIn.setStatus("current")
_MgmdCounterPortV3QueryIn_Type = Counter32
_MgmdCounterPortV3QueryIn_Object = MibTableColumn
mgmdCounterPortV3QueryIn = _MgmdCounterPortV3QueryIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 13),
    _MgmdCounterPortV3QueryIn_Type()
)
mgmdCounterPortV3QueryIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortV3QueryIn.setStatus("current")
_MgmdCounterPortTotalQueryIn_Type = Counter32
_MgmdCounterPortTotalQueryIn_Object = MibTableColumn
mgmdCounterPortTotalQueryIn = _MgmdCounterPortTotalQueryIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 14),
    _MgmdCounterPortTotalQueryIn_Type()
)
mgmdCounterPortTotalQueryIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortTotalQueryIn.setStatus("current")
_MgmdCounterPortV1QueryOut_Type = Counter32
_MgmdCounterPortV1QueryOut_Object = MibTableColumn
mgmdCounterPortV1QueryOut = _MgmdCounterPortV1QueryOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 15),
    _MgmdCounterPortV1QueryOut_Type()
)
mgmdCounterPortV1QueryOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortV1QueryOut.setStatus("current")
_MgmdCounterPortV2QueryOut_Type = Counter32
_MgmdCounterPortV2QueryOut_Object = MibTableColumn
mgmdCounterPortV2QueryOut = _MgmdCounterPortV2QueryOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 16),
    _MgmdCounterPortV2QueryOut_Type()
)
mgmdCounterPortV2QueryOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortV2QueryOut.setStatus("current")
_MgmdCounterPortV3QueryOut_Type = Counter32
_MgmdCounterPortV3QueryOut_Object = MibTableColumn
mgmdCounterPortV3QueryOut = _MgmdCounterPortV3QueryOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 17),
    _MgmdCounterPortV3QueryOut_Type()
)
mgmdCounterPortV3QueryOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortV3QueryOut.setStatus("current")
_MgmdCounterPortTotalQueryOut_Type = Counter32
_MgmdCounterPortTotalQueryOut_Object = MibTableColumn
mgmdCounterPortTotalQueryOut = _MgmdCounterPortTotalQueryOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 18),
    _MgmdCounterPortTotalQueryOut_Type()
)
mgmdCounterPortTotalQueryOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortTotalQueryOut.setStatus("current")
_MgmdCounterPortRecordDropMaxGrpLimit_Type = Counter32
_MgmdCounterPortRecordDropMaxGrpLimit_Object = MibTableColumn
mgmdCounterPortRecordDropMaxGrpLimit = _MgmdCounterPortRecordDropMaxGrpLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 19),
    _MgmdCounterPortRecordDropMaxGrpLimit_Type()
)
mgmdCounterPortRecordDropMaxGrpLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortRecordDropMaxGrpLimit.setStatus("current")
_MgmdCounterPortRecordDropGrpFilter_Type = Counter32
_MgmdCounterPortRecordDropGrpFilter_Object = MibTableColumn
mgmdCounterPortRecordDropGrpFilter = _MgmdCounterPortRecordDropGrpFilter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 20),
    _MgmdCounterPortRecordDropGrpFilter_Type()
)
mgmdCounterPortRecordDropGrpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortRecordDropGrpFilter.setStatus("current")
_MgmdCounterPortRecordDropMVR_Type = Counter32
_MgmdCounterPortRecordDropMVR_Object = MibTableColumn
mgmdCounterPortRecordDropMVR = _MgmdCounterPortRecordDropMVR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 21),
    _MgmdCounterPortRecordDropMVR_Type()
)
mgmdCounterPortRecordDropMVR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortRecordDropMVR.setStatus("current")
_MgmdCounterPortRecordDropOther_Type = Counter32
_MgmdCounterPortRecordDropOther_Object = MibTableColumn
mgmdCounterPortRecordDropOther = _MgmdCounterPortRecordDropOther_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 22),
    _MgmdCounterPortRecordDropOther_Type()
)
mgmdCounterPortRecordDropOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortRecordDropOther.setStatus("current")
_MgmdCounterPortDropRateLimit_Type = Counter32
_MgmdCounterPortDropRateLimit_Object = MibTableColumn
mgmdCounterPortDropRateLimit = _MgmdCounterPortDropRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 23),
    _MgmdCounterPortDropRateLimit_Type()
)
mgmdCounterPortDropRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortDropRateLimit.setStatus("current")
_MgmdCounterPortReportDropOther_Type = Counter32
_MgmdCounterPortReportDropOther_Object = MibTableColumn
mgmdCounterPortReportDropOther = _MgmdCounterPortReportDropOther_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 24),
    _MgmdCounterPortReportDropOther_Type()
)
mgmdCounterPortReportDropOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortReportDropOther.setStatus("current")
_MgmdCounterPortQueryDropOther_Type = Counter32
_MgmdCounterPortQueryDropOther_Object = MibTableColumn
mgmdCounterPortQueryDropOther = _MgmdCounterPortQueryDropOther_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 11, 1, 25),
    _MgmdCounterPortQueryDropOther_Type()
)
mgmdCounterPortQueryDropOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortQueryDropOther.setStatus("current")
_MgmdCounterVlanTable_Object = MibTable
mgmdCounterVlanTable = _MgmdCounterVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12)
)
if mibBuilder.loadTexts:
    mgmdCounterVlanTable.setStatus("current")
_MgmdCounterVlanEntry_Object = MibTableRow
mgmdCounterVlanEntry = _MgmdCounterVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1)
)
mgmdCounterVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    mgmdCounterVlanEntry.setStatus("current")
_MgmdCounterVlanV1ReportIn_Type = Counter32
_MgmdCounterVlanV1ReportIn_Object = MibTableColumn
mgmdCounterVlanV1ReportIn = _MgmdCounterVlanV1ReportIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 1),
    _MgmdCounterVlanV1ReportIn_Type()
)
mgmdCounterVlanV1ReportIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanV1ReportIn.setStatus("current")
_MgmdCounterVlanV2ReportIn_Type = Counter32
_MgmdCounterVlanV2ReportIn_Object = MibTableColumn
mgmdCounterVlanV2ReportIn = _MgmdCounterVlanV2ReportIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 2),
    _MgmdCounterVlanV2ReportIn_Type()
)
mgmdCounterVlanV2ReportIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanV2ReportIn.setStatus("current")
_MgmdCounterVlanV3ReportIn_Type = Counter32
_MgmdCounterVlanV3ReportIn_Object = MibTableColumn
mgmdCounterVlanV3ReportIn = _MgmdCounterVlanV3ReportIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 3),
    _MgmdCounterVlanV3ReportIn_Type()
)
mgmdCounterVlanV3ReportIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanV3ReportIn.setStatus("current")
_MgmdCounterVlanLeaveIn_Type = Counter32
_MgmdCounterVlanLeaveIn_Object = MibTableColumn
mgmdCounterVlanLeaveIn = _MgmdCounterVlanLeaveIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 4),
    _MgmdCounterVlanLeaveIn_Type()
)
mgmdCounterVlanLeaveIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanLeaveIn.setStatus("current")
_MgmdCounterVlanTotalReportIn_Type = Counter32
_MgmdCounterVlanTotalReportIn_Object = MibTableColumn
mgmdCounterVlanTotalReportIn = _MgmdCounterVlanTotalReportIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 5),
    _MgmdCounterVlanTotalReportIn_Type()
)
mgmdCounterVlanTotalReportIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanTotalReportIn.setStatus("current")
_MgmdCounterVlanV1ReportOut_Type = Counter32
_MgmdCounterVlanV1ReportOut_Object = MibTableColumn
mgmdCounterVlanV1ReportOut = _MgmdCounterVlanV1ReportOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 6),
    _MgmdCounterVlanV1ReportOut_Type()
)
mgmdCounterVlanV1ReportOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanV1ReportOut.setStatus("current")
_MgmdCounterVlanV2ReportOut_Type = Counter32
_MgmdCounterVlanV2ReportOut_Object = MibTableColumn
mgmdCounterVlanV2ReportOut = _MgmdCounterVlanV2ReportOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 7),
    _MgmdCounterVlanV2ReportOut_Type()
)
mgmdCounterVlanV2ReportOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanV2ReportOut.setStatus("current")
_MgmdCounterVlanV3ReportOut_Type = Counter32
_MgmdCounterVlanV3ReportOut_Object = MibTableColumn
mgmdCounterVlanV3ReportOut = _MgmdCounterVlanV3ReportOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 8),
    _MgmdCounterVlanV3ReportOut_Type()
)
mgmdCounterVlanV3ReportOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanV3ReportOut.setStatus("current")
_MgmdCounterVlanLeaveOut_Type = Counter32
_MgmdCounterVlanLeaveOut_Object = MibTableColumn
mgmdCounterVlanLeaveOut = _MgmdCounterVlanLeaveOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 9),
    _MgmdCounterVlanLeaveOut_Type()
)
mgmdCounterVlanLeaveOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanLeaveOut.setStatus("current")
_MgmdCounterVlanTotalReportOut_Type = Counter32
_MgmdCounterVlanTotalReportOut_Object = MibTableColumn
mgmdCounterVlanTotalReportOut = _MgmdCounterVlanTotalReportOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 10),
    _MgmdCounterVlanTotalReportOut_Type()
)
mgmdCounterVlanTotalReportOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanTotalReportOut.setStatus("current")
_MgmdCounterVlanV1QueryIn_Type = Counter32
_MgmdCounterVlanV1QueryIn_Object = MibTableColumn
mgmdCounterVlanV1QueryIn = _MgmdCounterVlanV1QueryIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 11),
    _MgmdCounterVlanV1QueryIn_Type()
)
mgmdCounterVlanV1QueryIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanV1QueryIn.setStatus("current")
_MgmdCounterVlanV2QueryIn_Type = Counter32
_MgmdCounterVlanV2QueryIn_Object = MibTableColumn
mgmdCounterVlanV2QueryIn = _MgmdCounterVlanV2QueryIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 12),
    _MgmdCounterVlanV2QueryIn_Type()
)
mgmdCounterVlanV2QueryIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanV2QueryIn.setStatus("current")
_MgmdCounterVlanV3QueryIn_Type = Counter32
_MgmdCounterVlanV3QueryIn_Object = MibTableColumn
mgmdCounterVlanV3QueryIn = _MgmdCounterVlanV3QueryIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 13),
    _MgmdCounterVlanV3QueryIn_Type()
)
mgmdCounterVlanV3QueryIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanV3QueryIn.setStatus("current")
_MgmdCounterVlanTotalQueryIn_Type = Counter32
_MgmdCounterVlanTotalQueryIn_Object = MibTableColumn
mgmdCounterVlanTotalQueryIn = _MgmdCounterVlanTotalQueryIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 14),
    _MgmdCounterVlanTotalQueryIn_Type()
)
mgmdCounterVlanTotalQueryIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanTotalQueryIn.setStatus("current")
_MgmdCounterVlanV1QueryOut_Type = Counter32
_MgmdCounterVlanV1QueryOut_Object = MibTableColumn
mgmdCounterVlanV1QueryOut = _MgmdCounterVlanV1QueryOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 15),
    _MgmdCounterVlanV1QueryOut_Type()
)
mgmdCounterVlanV1QueryOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanV1QueryOut.setStatus("current")
_MgmdCounterVlanV2QueryOut_Type = Counter32
_MgmdCounterVlanV2QueryOut_Object = MibTableColumn
mgmdCounterVlanV2QueryOut = _MgmdCounterVlanV2QueryOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 16),
    _MgmdCounterVlanV2QueryOut_Type()
)
mgmdCounterVlanV2QueryOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanV2QueryOut.setStatus("current")
_MgmdCounterVlanV3QueryOut_Type = Counter32
_MgmdCounterVlanV3QueryOut_Object = MibTableColumn
mgmdCounterVlanV3QueryOut = _MgmdCounterVlanV3QueryOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 17),
    _MgmdCounterVlanV3QueryOut_Type()
)
mgmdCounterVlanV3QueryOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanV3QueryOut.setStatus("current")
_MgmdCounterVlanTotalQueryOut_Type = Counter32
_MgmdCounterVlanTotalQueryOut_Object = MibTableColumn
mgmdCounterVlanTotalQueryOut = _MgmdCounterVlanTotalQueryOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 18),
    _MgmdCounterVlanTotalQueryOut_Type()
)
mgmdCounterVlanTotalQueryOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanTotalQueryOut.setStatus("current")
_MgmdCounterVlanRecordDropMaxGrpLimit_Type = Counter32
_MgmdCounterVlanRecordDropMaxGrpLimit_Object = MibTableColumn
mgmdCounterVlanRecordDropMaxGrpLimit = _MgmdCounterVlanRecordDropMaxGrpLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 19),
    _MgmdCounterVlanRecordDropMaxGrpLimit_Type()
)
mgmdCounterVlanRecordDropMaxGrpLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanRecordDropMaxGrpLimit.setStatus("current")
_MgmdCounterVlanRecordDropGrpFilter_Type = Counter32
_MgmdCounterVlanRecordDropGrpFilter_Object = MibTableColumn
mgmdCounterVlanRecordDropGrpFilter = _MgmdCounterVlanRecordDropGrpFilter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 20),
    _MgmdCounterVlanRecordDropGrpFilter_Type()
)
mgmdCounterVlanRecordDropGrpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanRecordDropGrpFilter.setStatus("current")
_MgmdCounterVlanRecordDropMVR_Type = Counter32
_MgmdCounterVlanRecordDropMVR_Object = MibTableColumn
mgmdCounterVlanRecordDropMVR = _MgmdCounterVlanRecordDropMVR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 21),
    _MgmdCounterVlanRecordDropMVR_Type()
)
mgmdCounterVlanRecordDropMVR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanRecordDropMVR.setStatus("current")
_MgmdCounterVlanRecordDropOther_Type = Counter32
_MgmdCounterVlanRecordDropOther_Object = MibTableColumn
mgmdCounterVlanRecordDropOther = _MgmdCounterVlanRecordDropOther_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 22),
    _MgmdCounterVlanRecordDropOther_Type()
)
mgmdCounterVlanRecordDropOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanRecordDropOther.setStatus("current")
_MgmdCounterVlanDropRateLimit_Type = Counter32
_MgmdCounterVlanDropRateLimit_Object = MibTableColumn
mgmdCounterVlanDropRateLimit = _MgmdCounterVlanDropRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 23),
    _MgmdCounterVlanDropRateLimit_Type()
)
mgmdCounterVlanDropRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanDropRateLimit.setStatus("current")
_MgmdCounterVlanReportDropOther_Type = Counter32
_MgmdCounterVlanReportDropOther_Object = MibTableColumn
mgmdCounterVlanReportDropOther = _MgmdCounterVlanReportDropOther_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 24),
    _MgmdCounterVlanReportDropOther_Type()
)
mgmdCounterVlanReportDropOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanReportDropOther.setStatus("current")
_MgmdCounterVlanQueryDropOther_Type = Counter32
_MgmdCounterVlanQueryDropOther_Object = MibTableColumn
mgmdCounterVlanQueryDropOther = _MgmdCounterVlanQueryDropOther_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 12, 1, 25),
    _MgmdCounterVlanQueryDropOther_Type()
)
mgmdCounterVlanQueryDropOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanQueryDropOther.setStatus("current")
_MgmdCurrentGroupStatusTable_Object = MibTable
mgmdCurrentGroupStatusTable = _MgmdCurrentGroupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 13)
)
if mibBuilder.loadTexts:
    mgmdCurrentGroupStatusTable.setStatus("current")
_MgmdCurrentGroupStatusEntry_Object = MibTableRow
mgmdCurrentGroupStatusEntry = _MgmdCurrentGroupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 13, 1)
)
mgmdCurrentGroupStatusEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "mgmdStatusVlanID"),
    (0, "ZYXEL-olt1408-MIB", "mgmdStatusGroupAddressType"),
    (0, "ZYXEL-olt1408-MIB", "mgmdStatusGroupAddress"),
)
if mibBuilder.loadTexts:
    mgmdCurrentGroupStatusEntry.setStatus("current")
_MgmdCurrentNumberOfActivePort_Type = Integer32
_MgmdCurrentNumberOfActivePort_Object = MibTableColumn
mgmdCurrentNumberOfActivePort = _MgmdCurrentNumberOfActivePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 13, 1, 1),
    _MgmdCurrentNumberOfActivePort_Type()
)
mgmdCurrentNumberOfActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCurrentNumberOfActivePort.setStatus("current")
_MgmdClientSrcIpTable_Object = MibTable
mgmdClientSrcIpTable = _MgmdClientSrcIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 14)
)
if mibBuilder.loadTexts:
    mgmdClientSrcIpTable.setStatus("current")
_MgmdClientSrcIpEntry_Object = MibTableRow
mgmdClientSrcIpEntry = _MgmdClientSrcIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 14, 1)
)
mgmdClientSrcIpEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "mgmdClientSrcIpAddressType"),
    (0, "ZYXEL-olt1408-MIB", "mgmdClientSrcIpIndex"),
    (0, "ZYXEL-olt1408-MIB", "mgmdStatusVlanID"),
    (0, "ZYXEL-olt1408-MIB", "mgmdStatusPort"),
    (0, "ZYXEL-olt1408-MIB", "mgmdStatusGroupAddress"),
)
if mibBuilder.loadTexts:
    mgmdClientSrcIpEntry.setStatus("current")
_MgmdClientSrcIpIndex_Type = Integer32
_MgmdClientSrcIpIndex_Object = MibTableColumn
mgmdClientSrcIpIndex = _MgmdClientSrcIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 14, 1, 1),
    _MgmdClientSrcIpIndex_Type()
)
mgmdClientSrcIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdClientSrcIpIndex.setStatus("current")


class _MgmdClientSrcIpAddressType_Type(InetAddressType):
    """Custom type mgmdClientSrcIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_MgmdClientSrcIpAddressType_Type.__name__ = "InetAddressType"
_MgmdClientSrcIpAddressType_Object = MibTableColumn
mgmdClientSrcIpAddressType = _MgmdClientSrcIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 14, 1, 2),
    _MgmdClientSrcIpAddressType_Type()
)
mgmdClientSrcIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdClientSrcIpAddressType.setStatus("current")


class _MgmdClientSrcIpAddress_Type(InetAddress):
    """Custom type mgmdClientSrcIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdClientSrcIpAddress_Type.__name__ = "InetAddress"
_MgmdClientSrcIpAddress_Object = MibTableColumn
mgmdClientSrcIpAddress = _MgmdClientSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 14, 1, 3),
    _MgmdClientSrcIpAddress_Type()
)
mgmdClientSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdClientSrcIpAddress.setStatus("current")
_MgmdSrcListTable_Object = MibTable
mgmdSrcListTable = _MgmdSrcListTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 15)
)
if mibBuilder.loadTexts:
    mgmdSrcListTable.setStatus("current")
_MgmdSrcListEntry_Object = MibTableRow
mgmdSrcListEntry = _MgmdSrcListEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 15, 1)
)
mgmdSrcListEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "mgmdSrcListAddressType"),
    (0, "ZYXEL-olt1408-MIB", "mgmdStatusVlanID"),
    (0, "ZYXEL-olt1408-MIB", "mgmdStatusPort"),
    (0, "ZYXEL-olt1408-MIB", "mgmdStatusGroupAddress"),
    (0, "ZYXEL-olt1408-MIB", "mgmdSrcListAddress"),
)
if mibBuilder.loadTexts:
    mgmdSrcListEntry.setStatus("current")


class _MgmdSrcListAddressType_Type(InetAddressType):
    """Custom type mgmdSrcListAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_MgmdSrcListAddressType_Type.__name__ = "InetAddressType"
_MgmdSrcListAddressType_Object = MibTableColumn
mgmdSrcListAddressType = _MgmdSrcListAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 15, 1, 1),
    _MgmdSrcListAddressType_Type()
)
mgmdSrcListAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdSrcListAddressType.setStatus("current")


class _MgmdSrcListAddress_Type(InetAddress):
    """Custom type mgmdSrcListAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdSrcListAddress_Type.__name__ = "InetAddress"
_MgmdSrcListAddress_Object = MibTableColumn
mgmdSrcListAddress = _MgmdSrcListAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 15, 1, 2),
    _MgmdSrcListAddress_Type()
)
mgmdSrcListAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdSrcListAddress.setStatus("current")
_MgmdPortCounterResetTable_Object = MibTable
mgmdPortCounterResetTable = _MgmdPortCounterResetTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 16)
)
if mibBuilder.loadTexts:
    mgmdPortCounterResetTable.setStatus("current")
_MgmdPortCounterResetEntry_Object = MibTableRow
mgmdPortCounterResetEntry = _MgmdPortCounterResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 16, 1)
)
mgmdPortCounterResetEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    mgmdPortCounterResetEntry.setStatus("current")


class _MgmdPortCounterReset_Type(Integer32):
    """Custom type mgmdPortCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_MgmdPortCounterReset_Type.__name__ = "Integer32"
_MgmdPortCounterReset_Object = MibTableColumn
mgmdPortCounterReset = _MgmdPortCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 16, 1, 1),
    _MgmdPortCounterReset_Type()
)
mgmdPortCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmdPortCounterReset.setStatus("current")


class _MgmdAnyPortCounterReset_Type(Integer32):
    """Custom type mgmdAnyPortCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_MgmdAnyPortCounterReset_Type.__name__ = "Integer32"
_MgmdAnyPortCounterReset_Object = MibScalar
mgmdAnyPortCounterReset = _MgmdAnyPortCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 17),
    _MgmdAnyPortCounterReset_Type()
)
mgmdAnyPortCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmdAnyPortCounterReset.setStatus("current")


class _MgmdAnyVlanCounterReset_Type(Integer32):
    """Custom type mgmdAnyVlanCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_MgmdAnyVlanCounterReset_Type.__name__ = "Integer32"
_MgmdAnyVlanCounterReset_Object = MibScalar
mgmdAnyVlanCounterReset = _MgmdAnyVlanCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 18),
    _MgmdAnyVlanCounterReset_Type()
)
mgmdAnyVlanCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmdAnyVlanCounterReset.setStatus("current")
_IgmpchannelCountTable_Object = MibTable
igmpchannelCountTable = _IgmpchannelCountTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 19)
)
if mibBuilder.loadTexts:
    igmpchannelCountTable.setStatus("current")
_IgmpchannelCountEntry_Object = MibTableRow
igmpchannelCountEntry = _IgmpchannelCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 19, 1)
)
igmpchannelCountEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "uniPort"),
    (0, "ZYXEL-olt1408-MIB", "uniportIgmpchannelUniSvid"),
    (0, "ZYXEL-olt1408-MIB", "uniportIgmpchannelUniCvid"),
)
if mibBuilder.loadTexts:
    igmpchannelCountEntry.setStatus("current")
_IgmpchannelCountInReportV1_Type = Integer32
_IgmpchannelCountInReportV1_Object = MibTableColumn
igmpchannelCountInReportV1 = _IgmpchannelCountInReportV1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 19, 1, 1),
    _IgmpchannelCountInReportV1_Type()
)
igmpchannelCountInReportV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpchannelCountInReportV1.setStatus("current")
_IgmpchannelCountInReportV2_Type = Integer32
_IgmpchannelCountInReportV2_Object = MibTableColumn
igmpchannelCountInReportV2 = _IgmpchannelCountInReportV2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 19, 1, 2),
    _IgmpchannelCountInReportV2_Type()
)
igmpchannelCountInReportV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpchannelCountInReportV2.setStatus("current")
_IgmpchannelCountInReportV3_Type = Integer32
_IgmpchannelCountInReportV3_Object = MibTableColumn
igmpchannelCountInReportV3 = _IgmpchannelCountInReportV3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 19, 1, 3),
    _IgmpchannelCountInReportV3_Type()
)
igmpchannelCountInReportV3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpchannelCountInReportV3.setStatus("current")
_IgmpchannelCountInReportLeave_Type = Integer32
_IgmpchannelCountInReportLeave_Object = MibTableColumn
igmpchannelCountInReportLeave = _IgmpchannelCountInReportLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 19, 1, 4),
    _IgmpchannelCountInReportLeave_Type()
)
igmpchannelCountInReportLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpchannelCountInReportLeave.setStatus("current")
_IgmpchannelCountDropRateLimit_Type = Integer32
_IgmpchannelCountDropRateLimit_Object = MibTableColumn
igmpchannelCountDropRateLimit = _IgmpchannelCountDropRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 19, 1, 5),
    _IgmpchannelCountDropRateLimit_Type()
)
igmpchannelCountDropRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpchannelCountDropRateLimit.setStatus("current")
_IgmpchannelCountDropOthers_Type = Integer32
_IgmpchannelCountDropOthers_Object = MibTableColumn
igmpchannelCountDropOthers = _IgmpchannelCountDropOthers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 19, 1, 6),
    _IgmpchannelCountDropOthers_Type()
)
igmpchannelCountDropOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpchannelCountDropOthers.setStatus("current")
_IgmpchannelStatusTable_Object = MibTable
igmpchannelStatusTable = _IgmpchannelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 20)
)
if mibBuilder.loadTexts:
    igmpchannelStatusTable.setStatus("current")
_IgmpchannelStatusEntry_Object = MibTableRow
igmpchannelStatusEntry = _IgmpchannelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 20, 1)
)
igmpchannelStatusEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "igmpchannelStatusVlanID"),
    (0, "ZYXEL-olt1408-MIB", "igmpchannelStatusPort"),
    (0, "ZYXEL-olt1408-MIB", "igmpchannelStatusGroupAddressType"),
    (0, "ZYXEL-olt1408-MIB", "igmpchannelStatusGroupAddress"),
    (0, "ZYXEL-olt1408-MIB", "igmpchannelStatusGem"),
)
if mibBuilder.loadTexts:
    igmpchannelStatusEntry.setStatus("current")
_IgmpchannelStatusVlanID_Type = Integer32
_IgmpchannelStatusVlanID_Object = MibTableColumn
igmpchannelStatusVlanID = _IgmpchannelStatusVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 20, 1, 1),
    _IgmpchannelStatusVlanID_Type()
)
igmpchannelStatusVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpchannelStatusVlanID.setStatus("current")
_IgmpchannelStatusPort_Type = Integer32
_IgmpchannelStatusPort_Object = MibTableColumn
igmpchannelStatusPort = _IgmpchannelStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 20, 1, 2),
    _IgmpchannelStatusPort_Type()
)
igmpchannelStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpchannelStatusPort.setStatus("current")


class _IgmpchannelStatusGroupAddressType_Type(InetAddressType):
    """Custom type igmpchannelStatusGroupAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_IgmpchannelStatusGroupAddressType_Type.__name__ = "InetAddressType"
_IgmpchannelStatusGroupAddressType_Object = MibTableColumn
igmpchannelStatusGroupAddressType = _IgmpchannelStatusGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 20, 1, 3),
    _IgmpchannelStatusGroupAddressType_Type()
)
igmpchannelStatusGroupAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpchannelStatusGroupAddressType.setStatus("current")


class _IgmpchannelStatusGroupAddress_Type(InetAddress):
    """Custom type igmpchannelStatusGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IgmpchannelStatusGroupAddress_Type.__name__ = "InetAddress"
_IgmpchannelStatusGroupAddress_Object = MibTableColumn
igmpchannelStatusGroupAddress = _IgmpchannelStatusGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 20, 1, 4),
    _IgmpchannelStatusGroupAddress_Type()
)
igmpchannelStatusGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpchannelStatusGroupAddress.setStatus("current")
_IgmpchannelStatusGem_Type = Integer32
_IgmpchannelStatusGem_Object = MibTableColumn
igmpchannelStatusGem = _IgmpchannelStatusGem_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 20, 1, 5),
    _IgmpchannelStatusGem_Type()
)
igmpchannelStatusGem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpchannelStatusGem.setStatus("current")
_IgmpchannelStatusPortAid_Type = DisplayString
_IgmpchannelStatusPortAid_Object = MibTableColumn
igmpchannelStatusPortAid = _IgmpchannelStatusPortAid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 20, 1, 6),
    _IgmpchannelStatusPortAid_Type()
)
igmpchannelStatusPortAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpchannelStatusPortAid.setStatus("current")
_IgmpchannelStatusUniVid_Type = Integer32
_IgmpchannelStatusUniVid_Object = MibTableColumn
igmpchannelStatusUniVid = _IgmpchannelStatusUniVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 20, 1, 7),
    _IgmpchannelStatusUniVid_Type()
)
igmpchannelStatusUniVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpchannelStatusUniVid.setStatus("current")


class _IgmpchannelStatusGroupFilterMode_Type(Integer32):
    """Custom type igmpchannelStatusGroupFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_IgmpchannelStatusGroupFilterMode_Type.__name__ = "Integer32"
_IgmpchannelStatusGroupFilterMode_Object = MibTableColumn
igmpchannelStatusGroupFilterMode = _IgmpchannelStatusGroupFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 20, 1, 8),
    _IgmpchannelStatusGroupFilterMode_Type()
)
igmpchannelStatusGroupFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpchannelStatusGroupFilterMode.setStatus("current")
_IgmpchannelStatusGroupUpTime_Type = DisplayString
_IgmpchannelStatusGroupUpTime_Object = MibTableColumn
igmpchannelStatusGroupUpTime = _IgmpchannelStatusGroupUpTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 20, 1, 9),
    _IgmpchannelStatusGroupUpTime_Type()
)
igmpchannelStatusGroupUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpchannelStatusGroupUpTime.setStatus("current")
_IgmpchannelClientSrcIpTable_Object = MibTable
igmpchannelClientSrcIpTable = _IgmpchannelClientSrcIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 21)
)
if mibBuilder.loadTexts:
    igmpchannelClientSrcIpTable.setStatus("current")
_IgmpchannelClientSrcIpEntry_Object = MibTableRow
igmpchannelClientSrcIpEntry = _IgmpchannelClientSrcIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 21, 1)
)
igmpchannelClientSrcIpEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "igmpchannelClientSrcIpAddressType"),
    (0, "ZYXEL-olt1408-MIB", "igmpchannelClientSrcIpIndex"),
    (0, "ZYXEL-olt1408-MIB", "igmpchannelStatusVlanID"),
    (0, "ZYXEL-olt1408-MIB", "igmpchannelStatusPort"),
    (0, "ZYXEL-olt1408-MIB", "igmpchannelStatusGroupAddress"),
    (0, "ZYXEL-olt1408-MIB", "igmpchannelStatusGem"),
)
if mibBuilder.loadTexts:
    igmpchannelClientSrcIpEntry.setStatus("current")
_IgmpchannelClientSrcIpIndex_Type = Integer32
_IgmpchannelClientSrcIpIndex_Object = MibTableColumn
igmpchannelClientSrcIpIndex = _IgmpchannelClientSrcIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 21, 1, 1),
    _IgmpchannelClientSrcIpIndex_Type()
)
igmpchannelClientSrcIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpchannelClientSrcIpIndex.setStatus("current")


class _IgmpchannelClientSrcIpAddressType_Type(InetAddressType):
    """Custom type igmpchannelClientSrcIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_IgmpchannelClientSrcIpAddressType_Type.__name__ = "InetAddressType"
_IgmpchannelClientSrcIpAddressType_Object = MibTableColumn
igmpchannelClientSrcIpAddressType = _IgmpchannelClientSrcIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 21, 1, 2),
    _IgmpchannelClientSrcIpAddressType_Type()
)
igmpchannelClientSrcIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpchannelClientSrcIpAddressType.setStatus("current")


class _IgmpchannelClientSrcIpAddress_Type(InetAddress):
    """Custom type igmpchannelClientSrcIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IgmpchannelClientSrcIpAddress_Type.__name__ = "InetAddress"
_IgmpchannelClientSrcIpAddress_Object = MibTableColumn
igmpchannelClientSrcIpAddress = _IgmpchannelClientSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 26, 21, 1, 3),
    _IgmpchannelClientSrcIpAddress_Type()
)
igmpchannelClientSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpchannelClientSrcIpAddress.setStatus("current")
_MvrSetup_ObjectIdentity = ObjectIdentity
mvrSetup = _MvrSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28)
)
_MaxNumberOfMVR_Type = Integer32
_MaxNumberOfMVR_Object = MibScalar
maxNumberOfMVR = _MaxNumberOfMVR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 1),
    _MaxNumberOfMVR_Type()
)
maxNumberOfMVR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfMVR.setStatus("current")
_MvrTable_Object = MibTable
mvrTable = _MvrTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 2)
)
if mibBuilder.loadTexts:
    mvrTable.setStatus("current")
_MvrEntry_Object = MibTableRow
mvrEntry = _MvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 2, 1)
)
mvrEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "mvrVlanID"),
)
if mibBuilder.loadTexts:
    mvrEntry.setStatus("current")
_MvrVlanID_Type = Integer32
_MvrVlanID_Object = MibTableColumn
mvrVlanID = _MvrVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 2, 1, 1),
    _MvrVlanID_Type()
)
mvrVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrVlanID.setStatus("current")
_MvrName_Type = DisplayString
_MvrName_Object = MibTableColumn
mvrName = _MvrName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 2, 1, 2),
    _MvrName_Type()
)
mvrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrName.setStatus("current")


class _MvrMode_Type(Integer32):
    """Custom type mvrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("compatible", 1))
    )


_MvrMode_Type.__name__ = "Integer32"
_MvrMode_Object = MibTableColumn
mvrMode = _MvrMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 2, 1, 3),
    _MvrMode_Type()
)
mvrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrMode.setStatus("current")
_MvrRowStatus_Type = RowStatus
_MvrRowStatus_Object = MibTableColumn
mvrRowStatus = _MvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 2, 1, 4),
    _MvrRowStatus_Type()
)
mvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvrRowStatus.setStatus("current")
_Mvr8021pPriority_Type = Integer32
_Mvr8021pPriority_Object = MibTableColumn
mvr8021pPriority = _Mvr8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 2, 1, 5),
    _Mvr8021pPriority_Type()
)
mvr8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvr8021pPriority.setStatus("current")
_MvrPortTable_Object = MibTable
mvrPortTable = _MvrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 3)
)
if mibBuilder.loadTexts:
    mvrPortTable.setStatus("current")
_MvrPortEntry_Object = MibTableRow
mvrPortEntry = _MvrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 3, 1)
)
mvrPortEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "mvrVlanID"),
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    mvrPortEntry.setStatus("current")


class _MvrPortRole_Type(Integer32):
    """Custom type mvrPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("sourcePort", 2),
          ("receiverPort", 3))
    )


_MvrPortRole_Type.__name__ = "Integer32"
_MvrPortRole_Object = MibTableColumn
mvrPortRole = _MvrPortRole_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 3, 1, 1),
    _MvrPortRole_Type()
)
mvrPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortRole.setStatus("current")
_MvrPortTagging_Type = EnabledStatus
_MvrPortTagging_Object = MibTableColumn
mvrPortTagging = _MvrPortTagging_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 3, 1, 2),
    _MvrPortTagging_Type()
)
mvrPortTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortTagging.setStatus("current")
_MaxNumberOfMvrGroup_Type = Integer32
_MaxNumberOfMvrGroup_Object = MibScalar
maxNumberOfMvrGroup = _MaxNumberOfMvrGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 4),
    _MaxNumberOfMvrGroup_Type()
)
maxNumberOfMvrGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfMvrGroup.setStatus("current")
_MvrGroupTable_Object = MibTable
mvrGroupTable = _MvrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 5)
)
if mibBuilder.loadTexts:
    mvrGroupTable.setStatus("current")
_MvrGroupEntry_Object = MibTableRow
mvrGroupEntry = _MvrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 5, 1)
)
mvrGroupEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "mvrVlanID"),
    (0, "ZYXEL-olt1408-MIB", "mvrGroupName"),
)
if mibBuilder.loadTexts:
    mvrGroupEntry.setStatus("current")
_MvrGroupName_Type = DisplayString
_MvrGroupName_Object = MibTableColumn
mvrGroupName = _MvrGroupName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 5, 1, 1),
    _MvrGroupName_Type()
)
mvrGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrGroupName.setStatus("current")
_MvrGroupStartAddress_Type = IpAddress
_MvrGroupStartAddress_Object = MibTableColumn
mvrGroupStartAddress = _MvrGroupStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 5, 1, 2),
    _MvrGroupStartAddress_Type()
)
mvrGroupStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupStartAddress.setStatus("current")
_MvrGroupEndAddress_Type = IpAddress
_MvrGroupEndAddress_Object = MibTableColumn
mvrGroupEndAddress = _MvrGroupEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 5, 1, 3),
    _MvrGroupEndAddress_Type()
)
mvrGroupEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupEndAddress.setStatus("current")
_MvrGroupRowStatus_Type = RowStatus
_MvrGroupRowStatus_Object = MibTableColumn
mvrGroupRowStatus = _MvrGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 5, 1, 4),
    _MvrGroupRowStatus_Type()
)
mvrGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvrGroupRowStatus.setStatus("current")


class _MvrBehavior_Type(Integer32):
    """Custom type mvrBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igmpSnooping", 1),
          ("igmpProxy", 2))
    )


_MvrBehavior_Type.__name__ = "Integer32"
_MvrBehavior_Object = MibScalar
mvrBehavior = _MvrBehavior_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 6),
    _MvrBehavior_Type()
)
mvrBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrBehavior.setStatus("current")
_MvrMgmdGroupTable_Object = MibTable
mvrMgmdGroupTable = _MvrMgmdGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 7)
)
if mibBuilder.loadTexts:
    mvrMgmdGroupTable.setStatus("current")
_MvrMgmdGroupEntry_Object = MibTableRow
mvrMgmdGroupEntry = _MvrMgmdGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 7, 1)
)
mvrMgmdGroupEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "mvrVlanID"),
    (0, "ZYXEL-olt1408-MIB", "mvrMgmdGroupName"),
)
if mibBuilder.loadTexts:
    mvrMgmdGroupEntry.setStatus("current")
_MvrMgmdGroupName_Type = DisplayString
_MvrMgmdGroupName_Object = MibTableColumn
mvrMgmdGroupName = _MvrMgmdGroupName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 7, 1, 1),
    _MvrMgmdGroupName_Type()
)
mvrMgmdGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrMgmdGroupName.setStatus("current")
_MvrMgmdGroupAddressType_Type = InetAddressType
_MvrMgmdGroupAddressType_Object = MibTableColumn
mvrMgmdGroupAddressType = _MvrMgmdGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 7, 1, 2),
    _MvrMgmdGroupAddressType_Type()
)
mvrMgmdGroupAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrMgmdGroupAddressType.setStatus("current")
_MvrMgmdGroupStartAddress_Type = InetAddress
_MvrMgmdGroupStartAddress_Object = MibTableColumn
mvrMgmdGroupStartAddress = _MvrMgmdGroupStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 7, 1, 3),
    _MvrMgmdGroupStartAddress_Type()
)
mvrMgmdGroupStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrMgmdGroupStartAddress.setStatus("current")
_MvrMgmdGroupEndAddress_Type = InetAddress
_MvrMgmdGroupEndAddress_Object = MibTableColumn
mvrMgmdGroupEndAddress = _MvrMgmdGroupEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 7, 1, 4),
    _MvrMgmdGroupEndAddress_Type()
)
mvrMgmdGroupEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrMgmdGroupEndAddress.setStatus("current")
_MvrMgmdGroupRowStatus_Type = RowStatus
_MvrMgmdGroupRowStatus_Object = MibTableColumn
mvrMgmdGroupRowStatus = _MvrMgmdGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 28, 7, 1, 5),
    _MvrMgmdGroupRowStatus_Type()
)
mvrMgmdGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvrMgmdGroupRowStatus.setStatus("current")
_EventObjects_ObjectIdentity = ObjectIdentity
eventObjects = _EventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 30, 1)
)
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 30, 1, 1)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("current")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 30, 1, 1, 1)
)
eventEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "eventSeqNum"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("current")
_EventSeqNum_Type = Integer32
_EventSeqNum_Object = MibTableColumn
eventSeqNum = _EventSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 30, 1, 1, 1, 1),
    _EventSeqNum_Type()
)
eventSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSeqNum.setStatus("current")
_EventEventId_Type = EventIdNumber
_EventEventId_Object = MibTableColumn
eventEventId = _EventEventId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 30, 1, 1, 1, 2),
    _EventEventId_Type()
)
eventEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventEventId.setStatus("current")


class _EventName_Type(DisplayString):
    """Custom type eventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_EventName_Type.__name__ = "DisplayString"
_EventName_Object = MibTableColumn
eventName = _EventName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 30, 1, 1, 1, 3),
    _EventName_Type()
)
eventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventName.setStatus("current")
_EventInstanceType_Type = InstanceType
_EventInstanceType_Object = MibTableColumn
eventInstanceType = _EventInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 30, 1, 1, 1, 4),
    _EventInstanceType_Type()
)
eventInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceType.setStatus("current")
_EventInstanceId_Type = DisplayString
_EventInstanceId_Object = MibTableColumn
eventInstanceId = _EventInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 30, 1, 1, 1, 5),
    _EventInstanceId_Type()
)
eventInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceId.setStatus("current")
_EventInstanceName_Type = DisplayString
_EventInstanceName_Object = MibTableColumn
eventInstanceName = _EventInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 30, 1, 1, 1, 6),
    _EventInstanceName_Type()
)
eventInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceName.setStatus("current")
_EventSeverity_Type = EventSeverity
_EventSeverity_Object = MibTableColumn
eventSeverity = _EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 30, 1, 1, 1, 7),
    _EventSeverity_Type()
)
eventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSeverity.setStatus("current")
_EventSetTime_Type = UtcTimeStamp
_EventSetTime_Object = MibTableColumn
eventSetTime = _EventSetTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 30, 1, 1, 1, 8),
    _EventSetTime_Type()
)
eventSetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSetTime.setStatus("current")


class _EventDescription_Type(DisplayString):
    """Custom type eventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EventDescription_Type.__name__ = "DisplayString"
_EventDescription_Object = MibTableColumn
eventDescription = _EventDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 30, 1, 1, 1, 9),
    _EventDescription_Type()
)
eventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDescription.setStatus("current")
_EventServAffective_Type = EventServiceAffective
_EventServAffective_Object = MibTableColumn
eventServAffective = _EventServAffective_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 30, 1, 1, 1, 10),
    _EventServAffective_Type()
)
eventServAffective.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventServAffective.setStatus("current")
_EventInstanceIdNumber_Type = Integer32
_EventInstanceIdNumber_Object = MibTableColumn
eventInstanceIdNumber = _EventInstanceIdNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 30, 1, 1, 1, 11),
    _EventInstanceIdNumber_Type()
)
eventInstanceIdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceIdNumber.setStatus("current")
_TrapInfoObjects_ObjectIdentity = ObjectIdentity
trapInfoObjects = _TrapInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 31, 1)
)
_TrapRefSeqNum_Type = Integer32
_TrapRefSeqNum_Object = MibScalar
trapRefSeqNum = _TrapRefSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 31, 1, 1),
    _TrapRefSeqNum_Type()
)
trapRefSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapRefSeqNum.setStatus("current")
_TrapPersistence_Type = EventPersistence
_TrapPersistence_Object = MibScalar
trapPersistence = _TrapPersistence_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 31, 1, 2),
    _TrapPersistence_Type()
)
trapPersistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPersistence.setStatus("current")
_TrapSenderNodeId_Type = Integer32
_TrapSenderNodeId_Object = MibScalar
trapSenderNodeId = _TrapSenderNodeId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 31, 1, 3),
    _TrapSenderNodeId_Type()
)
trapSenderNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSenderNodeId.setStatus("current")
_TrapSenderStatus_Type = Integer32
_TrapSenderStatus_Object = MibScalar
trapSenderStatus = _TrapSenderStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 31, 1, 4),
    _TrapSenderStatus_Type()
)
trapSenderStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSenderStatus.setStatus("current")
_TrapNotifications_ObjectIdentity = ObjectIdentity
trapNotifications = _TrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 31, 2)
)
_ProtoBasedVlanSetup_ObjectIdentity = ObjectIdentity
protoBasedVlanSetup = _ProtoBasedVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 32)
)
_ProtoBasedVlanTable_Object = MibTable
protoBasedVlanTable = _ProtoBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 32, 1)
)
if mibBuilder.loadTexts:
    protoBasedVlanTable.setStatus("current")
_ProtoBasedVlanEntry_Object = MibTableRow
protoBasedVlanEntry = _ProtoBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 32, 1, 1)
)
protoBasedVlanEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "protoBasedVlanPort"),
    (0, "ZYXEL-olt1408-MIB", "protoBasedVlanPacketType"),
    (0, "ZYXEL-olt1408-MIB", "protoBasedVlanEtherType"),
)
if mibBuilder.loadTexts:
    protoBasedVlanEntry.setStatus("current")
_ProtoBasedVlanPort_Type = Integer32
_ProtoBasedVlanPort_Object = MibTableColumn
protoBasedVlanPort = _ProtoBasedVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 32, 1, 1, 1),
    _ProtoBasedVlanPort_Type()
)
protoBasedVlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protoBasedVlanPort.setStatus("current")


class _ProtoBasedVlanPacketType_Type(Integer32):
    """Custom type protoBasedVlanPacketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("etherII", 1)
    )


_ProtoBasedVlanPacketType_Type.__name__ = "Integer32"
_ProtoBasedVlanPacketType_Object = MibTableColumn
protoBasedVlanPacketType = _ProtoBasedVlanPacketType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 32, 1, 1, 2),
    _ProtoBasedVlanPacketType_Type()
)
protoBasedVlanPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protoBasedVlanPacketType.setStatus("current")
_ProtoBasedVlanEtherType_Type = Integer32
_ProtoBasedVlanEtherType_Object = MibTableColumn
protoBasedVlanEtherType = _ProtoBasedVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 32, 1, 1, 3),
    _ProtoBasedVlanEtherType_Type()
)
protoBasedVlanEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protoBasedVlanEtherType.setStatus("current")


class _ProtoBasedVlanName_Type(DisplayString):
    """Custom type protoBasedVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProtoBasedVlanName_Type.__name__ = "DisplayString"
_ProtoBasedVlanName_Object = MibTableColumn
protoBasedVlanName = _ProtoBasedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 32, 1, 1, 4),
    _ProtoBasedVlanName_Type()
)
protoBasedVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protoBasedVlanName.setStatus("current")


class _ProtoBasedVlanVid_Type(Integer32):
    """Custom type protoBasedVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ProtoBasedVlanVid_Type.__name__ = "Integer32"
_ProtoBasedVlanVid_Object = MibTableColumn
protoBasedVlanVid = _ProtoBasedVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 32, 1, 1, 5),
    _ProtoBasedVlanVid_Type()
)
protoBasedVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protoBasedVlanVid.setStatus("current")


class _ProtoBasedVlanPriority_Type(Integer32):
    """Custom type protoBasedVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ProtoBasedVlanPriority_Type.__name__ = "Integer32"
_ProtoBasedVlanPriority_Object = MibTableColumn
protoBasedVlanPriority = _ProtoBasedVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 32, 1, 1, 6),
    _ProtoBasedVlanPriority_Type()
)
protoBasedVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protoBasedVlanPriority.setStatus("current")
_ProtoBasedVlanState_Type = RowStatus
_ProtoBasedVlanState_Object = MibTableColumn
protoBasedVlanState = _ProtoBasedVlanState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 32, 1, 1, 7),
    _ProtoBasedVlanState_Type()
)
protoBasedVlanState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protoBasedVlanState.setStatus("current")
_SysLogSetup_ObjectIdentity = ObjectIdentity
sysLogSetup = _SysLogSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33)
)
_SysLogState_Type = EnabledStatus
_SysLogState_Object = MibScalar
sysLogState = _SysLogState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 1),
    _SysLogState_Type()
)
sysLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogState.setStatus("current")
_SysLogTypeTable_Object = MibTable
sysLogTypeTable = _SysLogTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 2)
)
if mibBuilder.loadTexts:
    sysLogTypeTable.setStatus("current")
_SysLogTypeEntry_Object = MibTableRow
sysLogTypeEntry = _SysLogTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 2, 1)
)
sysLogTypeEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "sysLogTypeIndex"),
)
if mibBuilder.loadTexts:
    sysLogTypeEntry.setStatus("current")
_SysLogTypeIndex_Type = Integer32
_SysLogTypeIndex_Object = MibTableColumn
sysLogTypeIndex = _SysLogTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 2, 1, 1),
    _SysLogTypeIndex_Type()
)
sysLogTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysLogTypeIndex.setStatus("current")
_SysLogTypeName_Type = DisplayString
_SysLogTypeName_Object = MibTableColumn
sysLogTypeName = _SysLogTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 2, 1, 2),
    _SysLogTypeName_Type()
)
sysLogTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLogTypeName.setStatus("current")
_SysLogTypeState_Type = EnabledStatus
_SysLogTypeState_Object = MibTableColumn
sysLogTypeState = _SysLogTypeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 2, 1, 3),
    _SysLogTypeState_Type()
)
sysLogTypeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogTypeState.setStatus("current")


class _SysLogTypeFacility_Type(Integer32):
    """Custom type sysLogTypeFacility based on Integer32"""
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
        *(("localUser0", 0),
          ("localUser1", 1),
          ("localUser2", 2),
          ("localUser3", 3),
          ("localUser4", 4),
          ("localUser5", 5),
          ("localUser6", 6),
          ("localUser7", 7))
    )


_SysLogTypeFacility_Type.__name__ = "Integer32"
_SysLogTypeFacility_Object = MibTableColumn
sysLogTypeFacility = _SysLogTypeFacility_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 2, 1, 4),
    _SysLogTypeFacility_Type()
)
sysLogTypeFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogTypeFacility.setStatus("current")


class _SysLogTypeLevel_Type(Integer32):
    """Custom type sysLogTypeLevel based on Integer32"""
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
        *(("level0", 0),
          ("level0to1", 1),
          ("level0to2", 2),
          ("level0to3", 3),
          ("level0to4", 4),
          ("level0to5", 5),
          ("level0to6", 6),
          ("level0to7", 7))
    )


_SysLogTypeLevel_Type.__name__ = "Integer32"
_SysLogTypeLevel_Object = MibTableColumn
sysLogTypeLevel = _SysLogTypeLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 2, 1, 5),
    _SysLogTypeLevel_Type()
)
sysLogTypeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogTypeLevel.setStatus("current")
_SysLogServerTable_Object = MibTable
sysLogServerTable = _SysLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 3)
)
if mibBuilder.loadTexts:
    sysLogServerTable.setStatus("current")
_SysLogServerEntry_Object = MibTableRow
sysLogServerEntry = _SysLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 3, 1)
)
sysLogServerEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "sysLogServerAddress"),
)
if mibBuilder.loadTexts:
    sysLogServerEntry.setStatus("current")
_SysLogServerAddress_Type = IpAddress
_SysLogServerAddress_Object = MibTableColumn
sysLogServerAddress = _SysLogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 3, 1, 1),
    _SysLogServerAddress_Type()
)
sysLogServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysLogServerAddress.setStatus("current")


class _SysLogServerLogLevel_Type(Integer32):
    """Custom type sysLogServerLogLevel based on Integer32"""
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
        *(("level0", 0),
          ("level0to1", 1),
          ("level0to2", 2),
          ("level0to3", 3),
          ("level0to4", 4),
          ("level0to5", 5),
          ("level0to6", 6),
          ("level0to7", 7))
    )


_SysLogServerLogLevel_Type.__name__ = "Integer32"
_SysLogServerLogLevel_Object = MibTableColumn
sysLogServerLogLevel = _SysLogServerLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 3, 1, 2),
    _SysLogServerLogLevel_Type()
)
sysLogServerLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogServerLogLevel.setStatus("current")
_SysLogServerRowStatus_Type = RowStatus
_SysLogServerRowStatus_Object = MibTableColumn
sysLogServerRowStatus = _SysLogServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 3, 1, 3),
    _SysLogServerRowStatus_Type()
)
sysLogServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysLogServerRowStatus.setStatus("current")
_SysLogUploadSetup_ObjectIdentity = ObjectIdentity
sysLogUploadSetup = _SysLogUploadSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 4)
)
_SysLogUploadState_Type = EnabledStatus
_SysLogUploadState_Object = MibScalar
sysLogUploadState = _SysLogUploadState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 4, 1),
    _SysLogUploadState_Type()
)
sysLogUploadState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogUploadState.setStatus("current")
_SysLogUploadTime_Type = DisplayString
_SysLogUploadTime_Object = MibScalar
sysLogUploadTime = _SysLogUploadTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 4, 2),
    _SysLogUploadTime_Type()
)
sysLogUploadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogUploadTime.setStatus("current")
_SysLogUploadServerTable_Object = MibTable
sysLogUploadServerTable = _SysLogUploadServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 4, 3)
)
if mibBuilder.loadTexts:
    sysLogUploadServerTable.setStatus("current")
_SysLogUploadServerEntry_Object = MibTableRow
sysLogUploadServerEntry = _SysLogUploadServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 4, 3, 1)
)
sysLogUploadServerEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "sysLogUploadServerAddress"),
)
if mibBuilder.loadTexts:
    sysLogUploadServerEntry.setStatus("current")
_SysLogUploadServerAddress_Type = IpAddress
_SysLogUploadServerAddress_Object = MibTableColumn
sysLogUploadServerAddress = _SysLogUploadServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 4, 3, 1, 1),
    _SysLogUploadServerAddress_Type()
)
sysLogUploadServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysLogUploadServerAddress.setStatus("current")
_SysLogUploadServerUsername_Type = DisplayString
_SysLogUploadServerUsername_Object = MibTableColumn
sysLogUploadServerUsername = _SysLogUploadServerUsername_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 4, 3, 1, 2),
    _SysLogUploadServerUsername_Type()
)
sysLogUploadServerUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogUploadServerUsername.setStatus("current")
_SysLogUploadServerPassword_Type = DisplayString
_SysLogUploadServerPassword_Object = MibTableColumn
sysLogUploadServerPassword = _SysLogUploadServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 4, 3, 1, 3),
    _SysLogUploadServerPassword_Type()
)
sysLogUploadServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogUploadServerPassword.setStatus("current")
_SysLogUploadServerFilepath_Type = DisplayString
_SysLogUploadServerFilepath_Object = MibTableColumn
sysLogUploadServerFilepath = _SysLogUploadServerFilepath_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 4, 3, 1, 4),
    _SysLogUploadServerFilepath_Type()
)
sysLogUploadServerFilepath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogUploadServerFilepath.setStatus("current")
_SysLogUploadServerRowStatus_Type = RowStatus
_SysLogUploadServerRowStatus_Object = MibTableColumn
sysLogUploadServerRowStatus = _SysLogUploadServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 33, 4, 3, 1, 5),
    _SysLogUploadServerRowStatus_Type()
)
sysLogUploadServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysLogUploadServerRowStatus.setStatus("current")
_IpStatus_ObjectIdentity = ObjectIdentity
ipStatus = _IpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 39)
)
_IpStatusTable_Object = MibTable
ipStatusTable = _IpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 39, 1)
)
if mibBuilder.loadTexts:
    ipStatusTable.setStatus("current")
_IpStatusEntry_Object = MibTableRow
ipStatusEntry = _IpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 39, 1, 1)
)
ipStatusEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "ipStatusIPAddress"),
    (0, "ZYXEL-olt1408-MIB", "ipStatusVid"),
)
if mibBuilder.loadTexts:
    ipStatusEntry.setStatus("current")
_IpStatusIPAddress_Type = IpAddress
_IpStatusIPAddress_Object = MibTableColumn
ipStatusIPAddress = _IpStatusIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 39, 1, 1, 1),
    _IpStatusIPAddress_Type()
)
ipStatusIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStatusIPAddress.setStatus("current")
_IpStatusVid_Type = Integer32
_IpStatusVid_Object = MibTableColumn
ipStatusVid = _IpStatusVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 39, 1, 1, 2),
    _IpStatusVid_Type()
)
ipStatusVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStatusVid.setStatus("current")
_IpStatusPort_Type = DisplayString
_IpStatusPort_Object = MibTableColumn
ipStatusPort = _IpStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 39, 1, 1, 3),
    _IpStatusPort_Type()
)
ipStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStatusPort.setStatus("current")


class _IpStatusType_Type(Integer32):
    """Custom type ipStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_IpStatusType_Type.__name__ = "Integer32"
_IpStatusType_Object = MibTableColumn
ipStatusType = _IpStatusType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 39, 1, 1, 4),
    _IpStatusType_Type()
)
ipStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStatusType.setStatus("current")
_DhcpSnp_ObjectIdentity = ObjectIdentity
dhcpSnp = _DhcpSnp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100)
)
_DhcpSnpVlanTable_Object = MibTable
dhcpSnpVlanTable = _DhcpSnpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 1)
)
if mibBuilder.loadTexts:
    dhcpSnpVlanTable.setStatus("current")
_DhcpSnpVlanEntry_Object = MibTableRow
dhcpSnpVlanEntry = _DhcpSnpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 1, 1)
)
dhcpSnpVlanEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "dhcpSnpVlanEntryVid"),
)
if mibBuilder.loadTexts:
    dhcpSnpVlanEntry.setStatus("current")


class _DhcpSnpVlanEntryVid_Type(Integer32):
    """Custom type dhcpSnpVlanEntryVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpSnpVlanEntryVid_Type.__name__ = "Integer32"
_DhcpSnpVlanEntryVid_Object = MibTableColumn
dhcpSnpVlanEntryVid = _DhcpSnpVlanEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 1, 1, 1),
    _DhcpSnpVlanEntryVid_Type()
)
dhcpSnpVlanEntryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpVlanEntryVid.setStatus("current")
_DhcpSnpVlanEntryEnable_Type = EnabledStatus
_DhcpSnpVlanEntryEnable_Object = MibTableColumn
dhcpSnpVlanEntryEnable = _DhcpSnpVlanEntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 1, 1, 2),
    _DhcpSnpVlanEntryEnable_Type()
)
dhcpSnpVlanEntryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpVlanEntryEnable.setStatus("current")
_DhcpSnpVlanEntryOption82Enable_Type = EnabledStatus
_DhcpSnpVlanEntryOption82Enable_Object = MibTableColumn
dhcpSnpVlanEntryOption82Enable = _DhcpSnpVlanEntryOption82Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 1, 1, 3),
    _DhcpSnpVlanEntryOption82Enable_Type()
)
dhcpSnpVlanEntryOption82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpVlanEntryOption82Enable.setStatus("current")
_DhcpSnpVlanEntryInfo_Type = EnabledStatus
_DhcpSnpVlanEntryInfo_Object = MibTableColumn
dhcpSnpVlanEntryInfo = _DhcpSnpVlanEntryInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 1, 1, 4),
    _DhcpSnpVlanEntryInfo_Type()
)
dhcpSnpVlanEntryInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpVlanEntryInfo.setStatus("current")
_DhcpSnpVlanEntryOption82FormatEnable_Type = EnabledStatus
_DhcpSnpVlanEntryOption82FormatEnable_Object = MibTableColumn
dhcpSnpVlanEntryOption82FormatEnable = _DhcpSnpVlanEntryOption82FormatEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 1, 1, 5),
    _DhcpSnpVlanEntryOption82FormatEnable_Type()
)
dhcpSnpVlanEntryOption82FormatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpVlanEntryOption82FormatEnable.setStatus("current")
_DhcpSnpPortTable_Object = MibTable
dhcpSnpPortTable = _DhcpSnpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 2)
)
if mibBuilder.loadTexts:
    dhcpSnpPortTable.setStatus("current")
_DhcpSnpPortEntry_Object = MibTableRow
dhcpSnpPortEntry = _DhcpSnpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 2, 1)
)
dhcpSnpPortEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "dhcpSnpPortEntryPort"),
)
if mibBuilder.loadTexts:
    dhcpSnpPortEntry.setStatus("current")
_DhcpSnpPortEntryPort_Type = Integer32
_DhcpSnpPortEntryPort_Object = MibTableColumn
dhcpSnpPortEntryPort = _DhcpSnpPortEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 2, 1, 1),
    _DhcpSnpPortEntryPort_Type()
)
dhcpSnpPortEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpPortEntryPort.setStatus("current")
_DhcpSnpPortEntryTrust_Type = EnabledStatus
_DhcpSnpPortEntryTrust_Object = MibTableColumn
dhcpSnpPortEntryTrust = _DhcpSnpPortEntryTrust_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 2, 1, 2),
    _DhcpSnpPortEntryTrust_Type()
)
dhcpSnpPortEntryTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpPortEntryTrust.setStatus("current")


class _DhcpSnpPortEntryRate_Type(Integer32):
    """Custom type dhcpSnpPortEntryRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_DhcpSnpPortEntryRate_Type.__name__ = "Integer32"
_DhcpSnpPortEntryRate_Object = MibTableColumn
dhcpSnpPortEntryRate = _DhcpSnpPortEntryRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 2, 1, 3),
    _DhcpSnpPortEntryRate_Type()
)
dhcpSnpPortEntryRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpPortEntryRate.setStatus("current")
_DhcpSnpBindTable_Object = MibTable
dhcpSnpBindTable = _DhcpSnpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 3)
)
if mibBuilder.loadTexts:
    dhcpSnpBindTable.setStatus("current")
_DhcpSnpBindEntry_Object = MibTableRow
dhcpSnpBindEntry = _DhcpSnpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 3, 1)
)
dhcpSnpBindEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "dhcpSnpBindEntryMac"),
    (0, "ZYXEL-olt1408-MIB", "dhcpSnpBindEntryVid"),
)
if mibBuilder.loadTexts:
    dhcpSnpBindEntry.setStatus("current")
_DhcpSnpBindEntryMac_Type = MacAddress
_DhcpSnpBindEntryMac_Object = MibTableColumn
dhcpSnpBindEntryMac = _DhcpSnpBindEntryMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 3, 1, 1),
    _DhcpSnpBindEntryMac_Type()
)
dhcpSnpBindEntryMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpBindEntryMac.setStatus("current")
_DhcpSnpBindEntryVid_Type = Integer32
_DhcpSnpBindEntryVid_Object = MibTableColumn
dhcpSnpBindEntryVid = _DhcpSnpBindEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 3, 1, 2),
    _DhcpSnpBindEntryVid_Type()
)
dhcpSnpBindEntryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpBindEntryVid.setStatus("current")
_DhcpSnpBindEntryIP_Type = IpAddress
_DhcpSnpBindEntryIP_Object = MibTableColumn
dhcpSnpBindEntryIP = _DhcpSnpBindEntryIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 3, 1, 3),
    _DhcpSnpBindEntryIP_Type()
)
dhcpSnpBindEntryIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpBindEntryIP.setStatus("current")
_DhcpSnpBindEntryLease_Type = Integer32
_DhcpSnpBindEntryLease_Object = MibTableColumn
dhcpSnpBindEntryLease = _DhcpSnpBindEntryLease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 3, 1, 4),
    _DhcpSnpBindEntryLease_Type()
)
dhcpSnpBindEntryLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpBindEntryLease.setStatus("current")


class _DhcpSnpBindEntryType_Type(Integer32):
    """Custom type dhcpSnpBindEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("dynamic", 2)
    )


_DhcpSnpBindEntryType_Type.__name__ = "Integer32"
_DhcpSnpBindEntryType_Object = MibTableColumn
dhcpSnpBindEntryType = _DhcpSnpBindEntryType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 3, 1, 5),
    _DhcpSnpBindEntryType_Type()
)
dhcpSnpBindEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpBindEntryType.setStatus("current")
_DhcpSnpBindEntryPort_Type = DisplayString
_DhcpSnpBindEntryPort_Object = MibTableColumn
dhcpSnpBindEntryPort = _DhcpSnpBindEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 3, 1, 6),
    _DhcpSnpBindEntryPort_Type()
)
dhcpSnpBindEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpBindEntryPort.setStatus("current")
_DhcpSnpEnable_Type = EnabledStatus
_DhcpSnpEnable_Object = MibScalar
dhcpSnpEnable = _DhcpSnpEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 4),
    _DhcpSnpEnable_Type()
)
dhcpSnpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpEnable.setStatus("current")
_DhcpSnpDb_ObjectIdentity = ObjectIdentity
dhcpSnpDb = _DhcpSnpDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5)
)


class _DhcpSnpDbAbort_Type(Integer32):
    """Custom type dhcpSnpDbAbort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_DhcpSnpDbAbort_Type.__name__ = "Integer32"
_DhcpSnpDbAbort_Object = MibScalar
dhcpSnpDbAbort = _DhcpSnpDbAbort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 1),
    _DhcpSnpDbAbort_Type()
)
dhcpSnpDbAbort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpDbAbort.setStatus("current")


class _DhcpSnpDbWriteDelay_Type(Integer32):
    """Custom type dhcpSnpDbWriteDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_DhcpSnpDbWriteDelay_Type.__name__ = "Integer32"
_DhcpSnpDbWriteDelay_Object = MibScalar
dhcpSnpDbWriteDelay = _DhcpSnpDbWriteDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 2),
    _DhcpSnpDbWriteDelay_Type()
)
dhcpSnpDbWriteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpDbWriteDelay.setStatus("current")


class _DhcpSnpDbUrl_Type(DisplayString):
    """Custom type dhcpSnpDbUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpSnpDbUrl_Type.__name__ = "DisplayString"
_DhcpSnpDbUrl_Object = MibScalar
dhcpSnpDbUrl = _DhcpSnpDbUrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 3),
    _DhcpSnpDbUrl_Type()
)
dhcpSnpDbUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpDbUrl.setStatus("current")


class _DhcpSnpDbUrlRenew_Type(DisplayString):
    """Custom type dhcpSnpDbUrlRenew based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpSnpDbUrlRenew_Type.__name__ = "DisplayString"
_DhcpSnpDbUrlRenew_Object = MibScalar
dhcpSnpDbUrlRenew = _DhcpSnpDbUrlRenew_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 4),
    _DhcpSnpDbUrlRenew_Type()
)
dhcpSnpDbUrlRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpDbUrlRenew.setStatus("current")
_DhcpSnpDbStat_ObjectIdentity = ObjectIdentity
dhcpSnpDbStat = _DhcpSnpDbStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5)
)
_DhcpSnpDbStatClear_Type = EnabledStatus
_DhcpSnpDbStatClear_Object = MibScalar
dhcpSnpDbStatClear = _DhcpSnpDbStatClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 1),
    _DhcpSnpDbStatClear_Type()
)
dhcpSnpDbStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpDbStatClear.setStatus("current")


class _DhcpSnpDbStatAgentRunning_Type(Integer32):
    """Custom type dhcpSnpDbStatAgentRunning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("read", 1),
          ("write", 2))
    )


_DhcpSnpDbStatAgentRunning_Type.__name__ = "Integer32"
_DhcpSnpDbStatAgentRunning_Object = MibScalar
dhcpSnpDbStatAgentRunning = _DhcpSnpDbStatAgentRunning_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 2),
    _DhcpSnpDbStatAgentRunning_Type()
)
dhcpSnpDbStatAgentRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatAgentRunning.setStatus("current")
_DhcpSnpDbStatDelayExpiry_Type = Integer32
_DhcpSnpDbStatDelayExpiry_Object = MibScalar
dhcpSnpDbStatDelayExpiry = _DhcpSnpDbStatDelayExpiry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 3),
    _DhcpSnpDbStatDelayExpiry_Type()
)
dhcpSnpDbStatDelayExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatDelayExpiry.setStatus("current")
_DhcpSnpDbStatAbortExpiry_Type = Integer32
_DhcpSnpDbStatAbortExpiry_Object = MibScalar
dhcpSnpDbStatAbortExpiry = _DhcpSnpDbStatAbortExpiry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 4),
    _DhcpSnpDbStatAbortExpiry_Type()
)
dhcpSnpDbStatAbortExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatAbortExpiry.setStatus("current")
_DhcpSnpDbStatLastSuccTime_Type = DisplayString
_DhcpSnpDbStatLastSuccTime_Object = MibScalar
dhcpSnpDbStatLastSuccTime = _DhcpSnpDbStatLastSuccTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 5),
    _DhcpSnpDbStatLastSuccTime_Type()
)
dhcpSnpDbStatLastSuccTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastSuccTime.setStatus("current")
_DhcpSnpDbStatLastFailTime_Type = DisplayString
_DhcpSnpDbStatLastFailTime_Object = MibScalar
dhcpSnpDbStatLastFailTime = _DhcpSnpDbStatLastFailTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 6),
    _DhcpSnpDbStatLastFailTime_Type()
)
dhcpSnpDbStatLastFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastFailTime.setStatus("current")
_DhcpSnpDbStatLastFailReason_Type = DisplayString
_DhcpSnpDbStatLastFailReason_Object = MibScalar
dhcpSnpDbStatLastFailReason = _DhcpSnpDbStatLastFailReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 7),
    _DhcpSnpDbStatLastFailReason_Type()
)
dhcpSnpDbStatLastFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastFailReason.setStatus("current")
_DhcpSnpDbStatTotalAttempt_Type = Integer32
_DhcpSnpDbStatTotalAttempt_Object = MibScalar
dhcpSnpDbStatTotalAttempt = _DhcpSnpDbStatTotalAttempt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 8),
    _DhcpSnpDbStatTotalAttempt_Type()
)
dhcpSnpDbStatTotalAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatTotalAttempt.setStatus("current")
_DhcpSnpDbStatStartupFail_Type = Integer32
_DhcpSnpDbStatStartupFail_Object = MibScalar
dhcpSnpDbStatStartupFail = _DhcpSnpDbStatStartupFail_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 9),
    _DhcpSnpDbStatStartupFail_Type()
)
dhcpSnpDbStatStartupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatStartupFail.setStatus("current")
_DhcpSnpDbStatSuccTrans_Type = Integer32
_DhcpSnpDbStatSuccTrans_Object = MibScalar
dhcpSnpDbStatSuccTrans = _DhcpSnpDbStatSuccTrans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 10),
    _DhcpSnpDbStatSuccTrans_Type()
)
dhcpSnpDbStatSuccTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatSuccTrans.setStatus("current")
_DhcpSnpDbStatFailTrans_Type = Integer32
_DhcpSnpDbStatFailTrans_Object = MibScalar
dhcpSnpDbStatFailTrans = _DhcpSnpDbStatFailTrans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 11),
    _DhcpSnpDbStatFailTrans_Type()
)
dhcpSnpDbStatFailTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatFailTrans.setStatus("current")
_DhcpSnpDbStatSuccRead_Type = Integer32
_DhcpSnpDbStatSuccRead_Object = MibScalar
dhcpSnpDbStatSuccRead = _DhcpSnpDbStatSuccRead_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 12),
    _DhcpSnpDbStatSuccRead_Type()
)
dhcpSnpDbStatSuccRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatSuccRead.setStatus("current")
_DhcpSnpDbStatFailRead_Type = Integer32
_DhcpSnpDbStatFailRead_Object = MibScalar
dhcpSnpDbStatFailRead = _DhcpSnpDbStatFailRead_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 13),
    _DhcpSnpDbStatFailRead_Type()
)
dhcpSnpDbStatFailRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatFailRead.setStatus("current")
_DhcpSnpDbStatSuccWrite_Type = Integer32
_DhcpSnpDbStatSuccWrite_Object = MibScalar
dhcpSnpDbStatSuccWrite = _DhcpSnpDbStatSuccWrite_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 14),
    _DhcpSnpDbStatSuccWrite_Type()
)
dhcpSnpDbStatSuccWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatSuccWrite.setStatus("current")
_DhcpSnpDbStatFailWrite_Type = Integer32
_DhcpSnpDbStatFailWrite_Object = MibScalar
dhcpSnpDbStatFailWrite = _DhcpSnpDbStatFailWrite_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 15),
    _DhcpSnpDbStatFailWrite_Type()
)
dhcpSnpDbStatFailWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatFailWrite.setStatus("current")


class _DhcpSnpDbStatFirstSuccAccess_Type(Integer32):
    """Custom type dhcpSnpDbStatFirstSuccAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("read", 1),
          ("write", 2))
    )


_DhcpSnpDbStatFirstSuccAccess_Type.__name__ = "Integer32"
_DhcpSnpDbStatFirstSuccAccess_Object = MibScalar
dhcpSnpDbStatFirstSuccAccess = _DhcpSnpDbStatFirstSuccAccess_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 16),
    _DhcpSnpDbStatFirstSuccAccess_Type()
)
dhcpSnpDbStatFirstSuccAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatFirstSuccAccess.setStatus("current")
_DhcpSnpDbStatLastIgnoreBindCol_Type = Integer32
_DhcpSnpDbStatLastIgnoreBindCol_Object = MibScalar
dhcpSnpDbStatLastIgnoreBindCol = _DhcpSnpDbStatLastIgnoreBindCol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 17),
    _DhcpSnpDbStatLastIgnoreBindCol_Type()
)
dhcpSnpDbStatLastIgnoreBindCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastIgnoreBindCol.setStatus("current")
_DhcpSnpDbStatLastIgnoreExpireLease_Type = Integer32
_DhcpSnpDbStatLastIgnoreExpireLease_Object = MibScalar
dhcpSnpDbStatLastIgnoreExpireLease = _DhcpSnpDbStatLastIgnoreExpireLease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 18),
    _DhcpSnpDbStatLastIgnoreExpireLease_Type()
)
dhcpSnpDbStatLastIgnoreExpireLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastIgnoreExpireLease.setStatus("current")
_DhcpSnpDbStatLastIgnoreInvalidIntf_Type = Integer32
_DhcpSnpDbStatLastIgnoreInvalidIntf_Object = MibScalar
dhcpSnpDbStatLastIgnoreInvalidIntf = _DhcpSnpDbStatLastIgnoreInvalidIntf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 19),
    _DhcpSnpDbStatLastIgnoreInvalidIntf_Type()
)
dhcpSnpDbStatLastIgnoreInvalidIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastIgnoreInvalidIntf.setStatus("current")
_DhcpSnpDbStatLastIgnoreUnsuppVlan_Type = Integer32
_DhcpSnpDbStatLastIgnoreUnsuppVlan_Object = MibScalar
dhcpSnpDbStatLastIgnoreUnsuppVlan = _DhcpSnpDbStatLastIgnoreUnsuppVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 20),
    _DhcpSnpDbStatLastIgnoreUnsuppVlan_Type()
)
dhcpSnpDbStatLastIgnoreUnsuppVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastIgnoreUnsuppVlan.setStatus("current")
_DhcpSnpDbStatLastIgnoreParse_Type = Integer32
_DhcpSnpDbStatLastIgnoreParse_Object = MibScalar
dhcpSnpDbStatLastIgnoreParse = _DhcpSnpDbStatLastIgnoreParse_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 21),
    _DhcpSnpDbStatLastIgnoreParse_Type()
)
dhcpSnpDbStatLastIgnoreParse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastIgnoreParse.setStatus("current")
_DhcpSnpDbStatTotalIgnoreBindCol_Type = Integer32
_DhcpSnpDbStatTotalIgnoreBindCol_Object = MibScalar
dhcpSnpDbStatTotalIgnoreBindCol = _DhcpSnpDbStatTotalIgnoreBindCol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 22),
    _DhcpSnpDbStatTotalIgnoreBindCol_Type()
)
dhcpSnpDbStatTotalIgnoreBindCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatTotalIgnoreBindCol.setStatus("current")
_DhcpSnpDbStatTotalIgnoreExpireLease_Type = Integer32
_DhcpSnpDbStatTotalIgnoreExpireLease_Object = MibScalar
dhcpSnpDbStatTotalIgnoreExpireLease = _DhcpSnpDbStatTotalIgnoreExpireLease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 23),
    _DhcpSnpDbStatTotalIgnoreExpireLease_Type()
)
dhcpSnpDbStatTotalIgnoreExpireLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatTotalIgnoreExpireLease.setStatus("current")
_DhcpSnpDbStatTotalIgnoreInvalidIntf_Type = Integer32
_DhcpSnpDbStatTotalIgnoreInvalidIntf_Object = MibScalar
dhcpSnpDbStatTotalIgnoreInvalidIntf = _DhcpSnpDbStatTotalIgnoreInvalidIntf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 24),
    _DhcpSnpDbStatTotalIgnoreInvalidIntf_Type()
)
dhcpSnpDbStatTotalIgnoreInvalidIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatTotalIgnoreInvalidIntf.setStatus("current")
_DhcpSnpDbStatTotalIgnoreUnsuppVlan_Type = Integer32
_DhcpSnpDbStatTotalIgnoreUnsuppVlan_Object = MibScalar
dhcpSnpDbStatTotalIgnoreUnsuppVlan = _DhcpSnpDbStatTotalIgnoreUnsuppVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 25),
    _DhcpSnpDbStatTotalIgnoreUnsuppVlan_Type()
)
dhcpSnpDbStatTotalIgnoreUnsuppVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatTotalIgnoreUnsuppVlan.setStatus("current")
_DhcpSnpDbStatTotalIgnoreParse_Type = Integer32
_DhcpSnpDbStatTotalIgnoreParse_Object = MibScalar
dhcpSnpDbStatTotalIgnoreParse = _DhcpSnpDbStatTotalIgnoreParse_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 26),
    _DhcpSnpDbStatTotalIgnoreParse_Type()
)
dhcpSnpDbStatTotalIgnoreParse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatTotalIgnoreParse.setStatus("current")


class _DhcpSnpDbStatFirstSuccessAccess_Type(Integer32):
    """Custom type dhcpSnpDbStatFirstSuccessAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("read", 1),
          ("write", 2))
    )


_DhcpSnpDbStatFirstSuccessAccess_Type.__name__ = "Integer32"
_DhcpSnpDbStatFirstSuccessAccess_Object = MibScalar
dhcpSnpDbStatFirstSuccessAccess = _DhcpSnpDbStatFirstSuccessAccess_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 5, 5, 27),
    _DhcpSnpDbStatFirstSuccessAccess_Type()
)
dhcpSnpDbStatFirstSuccessAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatFirstSuccessAccess.setStatus("current")
_DhcpSnpDhcpVlan_ObjectIdentity = ObjectIdentity
dhcpSnpDhcpVlan = _DhcpSnpDhcpVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 6)
)


class _DhcpSnpDhcpVlanVid_Type(Integer32):
    """Custom type dhcpSnpDhcpVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_DhcpSnpDhcpVlanVid_Type.__name__ = "Integer32"
_DhcpSnpDhcpVlanVid_Object = MibScalar
dhcpSnpDhcpVlanVid = _DhcpSnpDhcpVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 100, 6, 1),
    _DhcpSnpDhcpVlanVid_Type()
)
dhcpSnpDhcpVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpDhcpVlanVid.setStatus("current")
_Ipsg_ObjectIdentity = ObjectIdentity
ipsg = _Ipsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 101)
)
_IpsgTable_Object = MibTable
ipsgTable = _IpsgTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 101, 1)
)
if mibBuilder.loadTexts:
    ipsgTable.setStatus("current")
_IpsgEntry_Object = MibTableRow
ipsgEntry = _IpsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 101, 1, 1)
)
ipsgEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "ipsgEntryMac"),
    (0, "ZYXEL-olt1408-MIB", "ipsgEntryVid"),
)
if mibBuilder.loadTexts:
    ipsgEntry.setStatus("current")
_IpsgEntryMac_Type = MacAddress
_IpsgEntryMac_Object = MibTableColumn
ipsgEntryMac = _IpsgEntryMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 101, 1, 1, 1),
    _IpsgEntryMac_Type()
)
ipsgEntryMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsgEntryMac.setStatus("current")


class _IpsgEntryVid_Type(Integer32):
    """Custom type ipsgEntryVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IpsgEntryVid_Type.__name__ = "Integer32"
_IpsgEntryVid_Object = MibTableColumn
ipsgEntryVid = _IpsgEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 101, 1, 1, 2),
    _IpsgEntryVid_Type()
)
ipsgEntryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsgEntryVid.setStatus("current")
_IpsgEntryIp_Type = IpAddress
_IpsgEntryIp_Object = MibTableColumn
ipsgEntryIp = _IpsgEntryIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 101, 1, 1, 3),
    _IpsgEntryIp_Type()
)
ipsgEntryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsgEntryIp.setStatus("current")
_IpsgEntryLease_Type = Integer32
_IpsgEntryLease_Object = MibTableColumn
ipsgEntryLease = _IpsgEntryLease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 101, 1, 1, 4),
    _IpsgEntryLease_Type()
)
ipsgEntryLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsgEntryLease.setStatus("current")


class _IpsgEntryType_Type(Integer32):
    """Custom type ipsgEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp", 2))
    )


_IpsgEntryType_Type.__name__ = "Integer32"
_IpsgEntryType_Object = MibTableColumn
ipsgEntryType = _IpsgEntryType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 101, 1, 1, 5),
    _IpsgEntryType_Type()
)
ipsgEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsgEntryType.setStatus("current")
_IpsgEntryPort_Type = Integer32
_IpsgEntryPort_Object = MibTableColumn
ipsgEntryPort = _IpsgEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 101, 1, 1, 6),
    _IpsgEntryPort_Type()
)
ipsgEntryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsgEntryPort.setStatus("current")
_IpsgEntryState_Type = RowStatus
_IpsgEntryState_Object = MibTableColumn
ipsgEntryState = _IpsgEntryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 101, 1, 1, 7),
    _IpsgEntryState_Type()
)
ipsgEntryState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsgEntryState.setStatus("current")
_ArpInspect_ObjectIdentity = ObjectIdentity
arpInspect = _ArpInspect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102)
)
_ArpInspectSetup_ObjectIdentity = ObjectIdentity
arpInspectSetup = _ArpInspectSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 1)
)
_ArpInspectState_Type = EnabledStatus
_ArpInspectState_Object = MibScalar
arpInspectState = _ArpInspectState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 1, 1),
    _ArpInspectState_Type()
)
arpInspectState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectState.setStatus("current")


class _ArpInspectFilterAgingTime_Type(Integer32):
    """Custom type arpInspectFilterAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArpInspectFilterAgingTime_Type.__name__ = "Integer32"
_ArpInspectFilterAgingTime_Object = MibScalar
arpInspectFilterAgingTime = _ArpInspectFilterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 1, 2),
    _ArpInspectFilterAgingTime_Type()
)
arpInspectFilterAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectFilterAgingTime.setStatus("current")
_ArpInspectLog_ObjectIdentity = ObjectIdentity
arpInspectLog = _ArpInspectLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 1, 3)
)


class _ArpInspectLogEntries_Type(Integer32):
    """Custom type arpInspectLogEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ArpInspectLogEntries_Type.__name__ = "Integer32"
_ArpInspectLogEntries_Object = MibScalar
arpInspectLogEntries = _ArpInspectLogEntries_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 1, 3, 1),
    _ArpInspectLogEntries_Type()
)
arpInspectLogEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectLogEntries.setStatus("current")


class _ArpInspectLogRate_Type(Integer32):
    """Custom type arpInspectLogRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ArpInspectLogRate_Type.__name__ = "Integer32"
_ArpInspectLogRate_Object = MibScalar
arpInspectLogRate = _ArpInspectLogRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 1, 3, 2),
    _ArpInspectLogRate_Type()
)
arpInspectLogRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectLogRate.setStatus("current")


class _ArpInspectLogInterval_Type(Integer32):
    """Custom type arpInspectLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_ArpInspectLogInterval_Type.__name__ = "Integer32"
_ArpInspectLogInterval_Object = MibScalar
arpInspectLogInterval = _ArpInspectLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 1, 3, 3),
    _ArpInspectLogInterval_Type()
)
arpInspectLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectLogInterval.setStatus("current")
_ArpInspectVlanTable_Object = MibTable
arpInspectVlanTable = _ArpInspectVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 1, 4)
)
if mibBuilder.loadTexts:
    arpInspectVlanTable.setStatus("current")
_ArpInspectVlanEntry_Object = MibTableRow
arpInspectVlanEntry = _ArpInspectVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 1, 4, 1)
)
arpInspectVlanEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "arpInspectVlanVid"),
)
if mibBuilder.loadTexts:
    arpInspectVlanEntry.setStatus("current")


class _ArpInspectVlanVid_Type(Integer32):
    """Custom type arpInspectVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ArpInspectVlanVid_Type.__name__ = "Integer32"
_ArpInspectVlanVid_Object = MibTableColumn
arpInspectVlanVid = _ArpInspectVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 1, 4, 1, 1),
    _ArpInspectVlanVid_Type()
)
arpInspectVlanVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectVlanVid.setStatus("current")


class _ArpInspectVlanLog_Type(Integer32):
    """Custom type arpInspectVlanLog based on Integer32"""
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
        *(("all", 1),
          ("none", 2),
          ("permit", 3),
          ("deny", 4))
    )


_ArpInspectVlanLog_Type.__name__ = "Integer32"
_ArpInspectVlanLog_Object = MibTableColumn
arpInspectVlanLog = _ArpInspectVlanLog_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 1, 4, 1, 2),
    _ArpInspectVlanLog_Type()
)
arpInspectVlanLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectVlanLog.setStatus("current")


class _ArpInspectVlanStatus_Type(Integer32):
    """Custom type arpInspectVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ArpInspectVlanStatus_Type.__name__ = "Integer32"
_ArpInspectVlanStatus_Object = MibTableColumn
arpInspectVlanStatus = _ArpInspectVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 1, 4, 1, 3),
    _ArpInspectVlanStatus_Type()
)
arpInspectVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectVlanStatus.setStatus("current")
_ArpInspectPortTable_Object = MibTable
arpInspectPortTable = _ArpInspectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 1, 5)
)
if mibBuilder.loadTexts:
    arpInspectPortTable.setStatus("current")
_ArpInspectPortEntry_Object = MibTableRow
arpInspectPortEntry = _ArpInspectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 1, 5, 1)
)
arpInspectPortEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "arpInspectPortIndex"),
)
if mibBuilder.loadTexts:
    arpInspectPortEntry.setStatus("current")
_ArpInspectPortIndex_Type = Integer32
_ArpInspectPortIndex_Object = MibTableColumn
arpInspectPortIndex = _ArpInspectPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 1, 5, 1, 1),
    _ArpInspectPortIndex_Type()
)
arpInspectPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectPortIndex.setStatus("current")


class _ArpInspectPortTrust_Type(Integer32):
    """Custom type arpInspectPortTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 2))
    )


_ArpInspectPortTrust_Type.__name__ = "Integer32"
_ArpInspectPortTrust_Object = MibTableColumn
arpInspectPortTrust = _ArpInspectPortTrust_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 1, 5, 1, 2),
    _ArpInspectPortTrust_Type()
)
arpInspectPortTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectPortTrust.setStatus("current")


class _ArpInspectPortRate_Type(Integer32):
    """Custom type arpInspectPortRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_ArpInspectPortRate_Type.__name__ = "Integer32"
_ArpInspectPortRate_Object = MibTableColumn
arpInspectPortRate = _ArpInspectPortRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 1, 5, 1, 3),
    _ArpInspectPortRate_Type()
)
arpInspectPortRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectPortRate.setStatus("current")


class _ArpInspectPortInterval_Type(Integer32):
    """Custom type arpInspectPortInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ArpInspectPortInterval_Type.__name__ = "Integer32"
_ArpInspectPortInterval_Object = MibTableColumn
arpInspectPortInterval = _ArpInspectPortInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 1, 5, 1, 4),
    _ArpInspectPortInterval_Type()
)
arpInspectPortInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectPortInterval.setStatus("current")
_ArpInspectStatus_ObjectIdentity = ObjectIdentity
arpInspectStatus = _ArpInspectStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2)
)
_ArpInspectFilterClear_Type = EnabledStatus
_ArpInspectFilterClear_Object = MibScalar
arpInspectFilterClear = _ArpInspectFilterClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 1),
    _ArpInspectFilterClear_Type()
)
arpInspectFilterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectFilterClear.setStatus("current")
_ArpInspectLogClear_Type = EnabledStatus
_ArpInspectLogClear_Object = MibScalar
arpInspectLogClear = _ArpInspectLogClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 2),
    _ArpInspectLogClear_Type()
)
arpInspectLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectLogClear.setStatus("current")
_ArpInspectFilterTable_Object = MibTable
arpInspectFilterTable = _ArpInspectFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 3)
)
if mibBuilder.loadTexts:
    arpInspectFilterTable.setStatus("current")
_ArpInspectFilterEntry_Object = MibTableRow
arpInspectFilterEntry = _ArpInspectFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 3, 1)
)
arpInspectFilterEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "arpInspectFilterMac"),
    (0, "ZYXEL-olt1408-MIB", "arpInspectFilterVid"),
)
if mibBuilder.loadTexts:
    arpInspectFilterEntry.setStatus("current")
_ArpInspectFilterMac_Type = MacAddress
_ArpInspectFilterMac_Object = MibTableColumn
arpInspectFilterMac = _ArpInspectFilterMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 3, 1, 1),
    _ArpInspectFilterMac_Type()
)
arpInspectFilterMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectFilterMac.setStatus("current")


class _ArpInspectFilterVid_Type(Integer32):
    """Custom type arpInspectFilterVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ArpInspectFilterVid_Type.__name__ = "Integer32"
_ArpInspectFilterVid_Object = MibTableColumn
arpInspectFilterVid = _ArpInspectFilterVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 3, 1, 2),
    _ArpInspectFilterVid_Type()
)
arpInspectFilterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectFilterVid.setStatus("current")
_ArpInspectFilterPort_Type = Integer32
_ArpInspectFilterPort_Object = MibTableColumn
arpInspectFilterPort = _ArpInspectFilterPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 3, 1, 3),
    _ArpInspectFilterPort_Type()
)
arpInspectFilterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectFilterPort.setStatus("current")
_ArpInspectFilterExpiry_Type = Integer32
_ArpInspectFilterExpiry_Object = MibTableColumn
arpInspectFilterExpiry = _ArpInspectFilterExpiry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 3, 1, 4),
    _ArpInspectFilterExpiry_Type()
)
arpInspectFilterExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectFilterExpiry.setStatus("current")


class _ArpInspectFilterReason_Type(Integer32):
    """Custom type arpInspectFilterReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macVid", 1),
          ("port", 2),
          ("ip", 3))
    )


_ArpInspectFilterReason_Type.__name__ = "Integer32"
_ArpInspectFilterReason_Object = MibTableColumn
arpInspectFilterReason = _ArpInspectFilterReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 3, 1, 5),
    _ArpInspectFilterReason_Type()
)
arpInspectFilterReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectFilterReason.setStatus("current")
_ArpInspectFilterRowStatus_Type = RowStatus
_ArpInspectFilterRowStatus_Object = MibTableColumn
arpInspectFilterRowStatus = _ArpInspectFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 3, 1, 6),
    _ArpInspectFilterRowStatus_Type()
)
arpInspectFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arpInspectFilterRowStatus.setStatus("current")
_ArpInspectLogTable_Object = MibTable
arpInspectLogTable = _ArpInspectLogTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 4)
)
if mibBuilder.loadTexts:
    arpInspectLogTable.setStatus("current")
_ArpInspectLogEntry_Object = MibTableRow
arpInspectLogEntry = _ArpInspectLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 4, 1)
)
arpInspectLogEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "arpInspectLogMac"),
    (0, "ZYXEL-olt1408-MIB", "arpInspectLogVid"),
    (0, "ZYXEL-olt1408-MIB", "arpInspectLogPort"),
    (0, "ZYXEL-olt1408-MIB", "arpInspectLogIp"),
    (0, "ZYXEL-olt1408-MIB", "arpInspectLogReason"),
)
if mibBuilder.loadTexts:
    arpInspectLogEntry.setStatus("current")
_ArpInspectLogMac_Type = MacAddress
_ArpInspectLogMac_Object = MibTableColumn
arpInspectLogMac = _ArpInspectLogMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 4, 1, 1),
    _ArpInspectLogMac_Type()
)
arpInspectLogMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogMac.setStatus("current")


class _ArpInspectLogVid_Type(Integer32):
    """Custom type arpInspectLogVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ArpInspectLogVid_Type.__name__ = "Integer32"
_ArpInspectLogVid_Object = MibTableColumn
arpInspectLogVid = _ArpInspectLogVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 4, 1, 2),
    _ArpInspectLogVid_Type()
)
arpInspectLogVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogVid.setStatus("current")
_ArpInspectLogPort_Type = Integer32
_ArpInspectLogPort_Object = MibTableColumn
arpInspectLogPort = _ArpInspectLogPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 4, 1, 3),
    _ArpInspectLogPort_Type()
)
arpInspectLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogPort.setStatus("current")
_ArpInspectLogIp_Type = IpAddress
_ArpInspectLogIp_Object = MibTableColumn
arpInspectLogIp = _ArpInspectLogIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 4, 1, 4),
    _ArpInspectLogIp_Type()
)
arpInspectLogIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogIp.setStatus("current")
_ArpInspectLogNumPkt_Type = Integer32
_ArpInspectLogNumPkt_Object = MibTableColumn
arpInspectLogNumPkt = _ArpInspectLogNumPkt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 4, 1, 5),
    _ArpInspectLogNumPkt_Type()
)
arpInspectLogNumPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogNumPkt.setStatus("current")


class _ArpInspectLogReason_Type(Integer32):
    """Custom type arpInspectLogReason based on Integer32"""
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
        *(("deny", 1),
          ("denyStatic", 2),
          ("denyDHCP", 3),
          ("permitStatic", 4),
          ("permitDHCP", 5))
    )


_ArpInspectLogReason_Type.__name__ = "Integer32"
_ArpInspectLogReason_Object = MibTableColumn
arpInspectLogReason = _ArpInspectLogReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 4, 1, 6),
    _ArpInspectLogReason_Type()
)
arpInspectLogReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogReason.setStatus("current")
_ArpInspectLogTime_Type = DateAndTime
_ArpInspectLogTime_Object = MibTableColumn
arpInspectLogTime = _ArpInspectLogTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 4, 1, 7),
    _ArpInspectLogTime_Type()
)
arpInspectLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogTime.setStatus("current")
_ArpInspectStatisticsTable_Object = MibTable
arpInspectStatisticsTable = _ArpInspectStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 5)
)
if mibBuilder.loadTexts:
    arpInspectStatisticsTable.setStatus("current")
_ArpInspectStatisticsEntry_Object = MibTableRow
arpInspectStatisticsEntry = _ArpInspectStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 5, 1)
)
arpInspectStatisticsEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "arpInspectStatisticsVid"),
)
if mibBuilder.loadTexts:
    arpInspectStatisticsEntry.setStatus("current")
_ArpInspectStatisticsVid_Type = Integer32
_ArpInspectStatisticsVid_Object = MibTableColumn
arpInspectStatisticsVid = _ArpInspectStatisticsVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 5, 1, 1),
    _ArpInspectStatisticsVid_Type()
)
arpInspectStatisticsVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectStatisticsVid.setStatus("current")
_ArpInspectStatisticsReceived_Type = Counter32
_ArpInspectStatisticsReceived_Object = MibTableColumn
arpInspectStatisticsReceived = _ArpInspectStatisticsReceived_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 5, 1, 2),
    _ArpInspectStatisticsReceived_Type()
)
arpInspectStatisticsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectStatisticsReceived.setStatus("current")
_ArpInspectStatisticsRequest_Type = Counter32
_ArpInspectStatisticsRequest_Object = MibTableColumn
arpInspectStatisticsRequest = _ArpInspectStatisticsRequest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 5, 1, 3),
    _ArpInspectStatisticsRequest_Type()
)
arpInspectStatisticsRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectStatisticsRequest.setStatus("current")
_ArpInspectStatisticsReply_Type = Counter32
_ArpInspectStatisticsReply_Object = MibTableColumn
arpInspectStatisticsReply = _ArpInspectStatisticsReply_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 5, 1, 4),
    _ArpInspectStatisticsReply_Type()
)
arpInspectStatisticsReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectStatisticsReply.setStatus("current")
_ArpInspectStatisticsForward_Type = Counter32
_ArpInspectStatisticsForward_Object = MibTableColumn
arpInspectStatisticsForward = _ArpInspectStatisticsForward_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 5, 1, 5),
    _ArpInspectStatisticsForward_Type()
)
arpInspectStatisticsForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectStatisticsForward.setStatus("current")
_ArpInspectStatisticsDrop_Type = Counter32
_ArpInspectStatisticsDrop_Object = MibTableColumn
arpInspectStatisticsDrop = _ArpInspectStatisticsDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 5, 1, 6),
    _ArpInspectStatisticsDrop_Type()
)
arpInspectStatisticsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectStatisticsDrop.setStatus("current")
_ArpInspectStatisticsClear_Type = EnabledStatus
_ArpInspectStatisticsClear_Object = MibTableColumn
arpInspectStatisticsClear = _ArpInspectStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 102, 2, 5, 1, 7),
    _ArpInspectStatisticsClear_Type()
)
arpInspectStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectStatisticsClear.setStatus("current")
_TrTCMSetup_ObjectIdentity = ObjectIdentity
trTCMSetup = _TrTCMSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 103)
)
_TrTCMState_Type = EnabledStatus
_TrTCMState_Object = MibScalar
trTCMState = _TrTCMState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 103, 1),
    _TrTCMState_Type()
)
trTCMState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMState.setStatus("current")


class _TrTCMMode_Type(Integer32):
    """Custom type trTCMMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("colorAware", 0),
          ("colorBlind", 1))
    )


_TrTCMMode_Type.__name__ = "Integer32"
_TrTCMMode_Object = MibScalar
trTCMMode = _TrTCMMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 103, 2),
    _TrTCMMode_Type()
)
trTCMMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMMode.setStatus("current")
_TrTCMPortTable_Object = MibTable
trTCMPortTable = _TrTCMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 103, 3)
)
if mibBuilder.loadTexts:
    trTCMPortTable.setStatus("current")
_TrTCMPortEntry_Object = MibTableRow
trTCMPortEntry = _TrTCMPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 103, 3, 1)
)
trTCMPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    trTCMPortEntry.setStatus("current")
_TrTCMPortState_Type = EnabledStatus
_TrTCMPortState_Object = MibTableColumn
trTCMPortState = _TrTCMPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 103, 3, 1, 1),
    _TrTCMPortState_Type()
)
trTCMPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMPortState.setStatus("current")
_TrTCMPortCIR_Type = Integer32
_TrTCMPortCIR_Object = MibTableColumn
trTCMPortCIR = _TrTCMPortCIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 103, 3, 1, 2),
    _TrTCMPortCIR_Type()
)
trTCMPortCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMPortCIR.setStatus("current")
_TrTCMPortPIR_Type = Integer32
_TrTCMPortPIR_Object = MibTableColumn
trTCMPortPIR = _TrTCMPortPIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 103, 3, 1, 3),
    _TrTCMPortPIR_Type()
)
trTCMPortPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMPortPIR.setStatus("current")
_TrTCMPortDscpGreen_Type = Integer32
_TrTCMPortDscpGreen_Object = MibTableColumn
trTCMPortDscpGreen = _TrTCMPortDscpGreen_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 103, 3, 1, 4),
    _TrTCMPortDscpGreen_Type()
)
trTCMPortDscpGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMPortDscpGreen.setStatus("current")
_TrTCMPortDscpYellow_Type = Integer32
_TrTCMPortDscpYellow_Object = MibTableColumn
trTCMPortDscpYellow = _TrTCMPortDscpYellow_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 103, 3, 1, 5),
    _TrTCMPortDscpYellow_Type()
)
trTCMPortDscpYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMPortDscpYellow.setStatus("current")
_TrTCMPortDscpRed_Type = Integer32
_TrTCMPortDscpRed_Object = MibTableColumn
trTCMPortDscpRed = _TrTCMPortDscpRed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 103, 3, 1, 6),
    _TrTCMPortDscpRed_Type()
)
trTCMPortDscpRed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMPortDscpRed.setStatus("current")
_LoopGuardSetup_ObjectIdentity = ObjectIdentity
loopGuardSetup = _LoopGuardSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 104)
)
_LoopGuardState_Type = EnabledStatus
_LoopGuardState_Object = MibScalar
loopGuardState = _LoopGuardState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 104, 1),
    _LoopGuardState_Type()
)
loopGuardState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopGuardState.setStatus("current")
_LoopGuardPortTable_Object = MibTable
loopGuardPortTable = _LoopGuardPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 104, 2)
)
if mibBuilder.loadTexts:
    loopGuardPortTable.setStatus("current")
_LoopGuardPortEntry_Object = MibTableRow
loopGuardPortEntry = _LoopGuardPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 104, 2, 1)
)
loopGuardPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    loopGuardPortEntry.setStatus("current")
_LoopGuardPortState_Type = EnabledStatus
_LoopGuardPortState_Object = MibTableColumn
loopGuardPortState = _LoopGuardPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 104, 2, 1, 1),
    _LoopGuardPortState_Type()
)
loopGuardPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopGuardPortState.setStatus("current")
_SubnetBasedVlanSetup_ObjectIdentity = ObjectIdentity
subnetBasedVlanSetup = _SubnetBasedVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 105)
)
_SubnetBasedVlanState_Type = EnabledStatus
_SubnetBasedVlanState_Object = MibScalar
subnetBasedVlanState = _SubnetBasedVlanState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 105, 1),
    _SubnetBasedVlanState_Type()
)
subnetBasedVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetBasedVlanState.setStatus("current")
_DhcpVlanOverrideState_Type = EnabledStatus
_DhcpVlanOverrideState_Object = MibScalar
dhcpVlanOverrideState = _DhcpVlanOverrideState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 105, 2),
    _DhcpVlanOverrideState_Type()
)
dhcpVlanOverrideState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpVlanOverrideState.setStatus("current")
_SubnetBasedVlanTable_Object = MibTable
subnetBasedVlanTable = _SubnetBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 105, 3)
)
if mibBuilder.loadTexts:
    subnetBasedVlanTable.setStatus("current")
_SubnetBasedVlanEntry_Object = MibTableRow
subnetBasedVlanEntry = _SubnetBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 105, 3, 1)
)
subnetBasedVlanEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "subnetBasedVlanSrcIp"),
    (0, "ZYXEL-olt1408-MIB", "subnetBasedVlanSrcMaskBit"),
)
if mibBuilder.loadTexts:
    subnetBasedVlanEntry.setStatus("current")
_SubnetBasedVlanSrcIp_Type = IpAddress
_SubnetBasedVlanSrcIp_Object = MibTableColumn
subnetBasedVlanSrcIp = _SubnetBasedVlanSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 105, 3, 1, 1),
    _SubnetBasedVlanSrcIp_Type()
)
subnetBasedVlanSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subnetBasedVlanSrcIp.setStatus("current")


class _SubnetBasedVlanSrcMaskBit_Type(Integer32):
    """Custom type subnetBasedVlanSrcMaskBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SubnetBasedVlanSrcMaskBit_Type.__name__ = "Integer32"
_SubnetBasedVlanSrcMaskBit_Object = MibTableColumn
subnetBasedVlanSrcMaskBit = _SubnetBasedVlanSrcMaskBit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 105, 3, 1, 2),
    _SubnetBasedVlanSrcMaskBit_Type()
)
subnetBasedVlanSrcMaskBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subnetBasedVlanSrcMaskBit.setStatus("current")


class _SubnetBasedVlanName_Type(DisplayString):
    """Custom type subnetBasedVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SubnetBasedVlanName_Type.__name__ = "DisplayString"
_SubnetBasedVlanName_Object = MibTableColumn
subnetBasedVlanName = _SubnetBasedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 105, 3, 1, 3),
    _SubnetBasedVlanName_Type()
)
subnetBasedVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetBasedVlanName.setStatus("current")


class _SubnetBasedVlanVid_Type(Integer32):
    """Custom type subnetBasedVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SubnetBasedVlanVid_Type.__name__ = "Integer32"
_SubnetBasedVlanVid_Object = MibTableColumn
subnetBasedVlanVid = _SubnetBasedVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 105, 3, 1, 4),
    _SubnetBasedVlanVid_Type()
)
subnetBasedVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetBasedVlanVid.setStatus("current")


class _SubnetBasedVlanPriority_Type(Integer32):
    """Custom type subnetBasedVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SubnetBasedVlanPriority_Type.__name__ = "Integer32"
_SubnetBasedVlanPriority_Object = MibTableColumn
subnetBasedVlanPriority = _SubnetBasedVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 105, 3, 1, 5),
    _SubnetBasedVlanPriority_Type()
)
subnetBasedVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetBasedVlanPriority.setStatus("current")
_SubnetBasedVlanEntryState_Type = RowStatus
_SubnetBasedVlanEntryState_Object = MibTableColumn
subnetBasedVlanEntryState = _SubnetBasedVlanEntryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 105, 3, 1, 6),
    _SubnetBasedVlanEntryState_Type()
)
subnetBasedVlanEntryState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subnetBasedVlanEntryState.setStatus("current")
_MacAuthenticationSetup_ObjectIdentity = ObjectIdentity
macAuthenticationSetup = _MacAuthenticationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 106)
)
_MacAuthenticationState_Type = EnabledStatus
_MacAuthenticationState_Object = MibScalar
macAuthenticationState = _MacAuthenticationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 106, 1),
    _MacAuthenticationState_Type()
)
macAuthenticationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAuthenticationState.setStatus("current")
_MacAuthenticationNamePrefix_Type = DisplayString
_MacAuthenticationNamePrefix_Object = MibScalar
macAuthenticationNamePrefix = _MacAuthenticationNamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 106, 2),
    _MacAuthenticationNamePrefix_Type()
)
macAuthenticationNamePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAuthenticationNamePrefix.setStatus("current")
_MacAuthenticationPassword_Type = DisplayString
_MacAuthenticationPassword_Object = MibScalar
macAuthenticationPassword = _MacAuthenticationPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 106, 3),
    _MacAuthenticationPassword_Type()
)
macAuthenticationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAuthenticationPassword.setStatus("current")
_MacAuthenticationTimeout_Type = Integer32
_MacAuthenticationTimeout_Object = MibScalar
macAuthenticationTimeout = _MacAuthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 106, 4),
    _MacAuthenticationTimeout_Type()
)
macAuthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAuthenticationTimeout.setStatus("current")
_MacAuthenticationPortTable_Object = MibTable
macAuthenticationPortTable = _MacAuthenticationPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 106, 5)
)
if mibBuilder.loadTexts:
    macAuthenticationPortTable.setStatus("current")
_MacAuthenticationPortEntry_Object = MibTableRow
macAuthenticationPortEntry = _MacAuthenticationPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 106, 5, 1)
)
macAuthenticationPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    macAuthenticationPortEntry.setStatus("current")
_MacAuthenticationPortState_Type = EnabledStatus
_MacAuthenticationPortState_Object = MibTableColumn
macAuthenticationPortState = _MacAuthenticationPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 106, 5, 1, 1),
    _MacAuthenticationPortState_Type()
)
macAuthenticationPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAuthenticationPortState.setStatus("current")
_Mstp_ObjectIdentity = ObjectIdentity
mstp = _Mstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107)
)
_MstpGen_ObjectIdentity = ObjectIdentity
mstpGen = _MstpGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 1)
)
_MstpGenState_Type = EnabledStatus
_MstpGenState_Object = MibScalar
mstpGenState = _MstpGenState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 1, 1),
    _MstpGenState_Type()
)
mstpGenState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenState.setStatus("current")
_MstpGenCfgIdName_Type = DisplayString
_MstpGenCfgIdName_Object = MibScalar
mstpGenCfgIdName = _MstpGenCfgIdName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 1, 2),
    _MstpGenCfgIdName_Type()
)
mstpGenCfgIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenCfgIdName.setStatus("current")
_MstpGenCfgIdRevLevel_Type = Integer32
_MstpGenCfgIdRevLevel_Object = MibScalar
mstpGenCfgIdRevLevel = _MstpGenCfgIdRevLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 1, 3),
    _MstpGenCfgIdRevLevel_Type()
)
mstpGenCfgIdRevLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenCfgIdRevLevel.setStatus("current")


class _MstpGenCfgIdCfgDigest_Type(OctetString):
    """Custom type mstpGenCfgIdCfgDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_MstpGenCfgIdCfgDigest_Type.__name__ = "OctetString"
_MstpGenCfgIdCfgDigest_Object = MibScalar
mstpGenCfgIdCfgDigest = _MstpGenCfgIdCfgDigest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 1, 4),
    _MstpGenCfgIdCfgDigest_Type()
)
mstpGenCfgIdCfgDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenCfgIdCfgDigest.setStatus("current")


class _MstpGenHelloTime_Type(Timeout):
    """Custom type mstpGenHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MstpGenHelloTime_Type.__name__ = "Timeout"
_MstpGenHelloTime_Object = MibScalar
mstpGenHelloTime = _MstpGenHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 1, 5),
    _MstpGenHelloTime_Type()
)
mstpGenHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenHelloTime.setStatus("current")


class _MstpGenMaxAge_Type(Timeout):
    """Custom type mstpGenMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_MstpGenMaxAge_Type.__name__ = "Timeout"
_MstpGenMaxAge_Object = MibScalar
mstpGenMaxAge = _MstpGenMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 1, 6),
    _MstpGenMaxAge_Type()
)
mstpGenMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenMaxAge.setStatus("current")


class _MstpGenForwardDelay_Type(Timeout):
    """Custom type mstpGenForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_MstpGenForwardDelay_Type.__name__ = "Timeout"
_MstpGenForwardDelay_Object = MibScalar
mstpGenForwardDelay = _MstpGenForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 1, 7),
    _MstpGenForwardDelay_Type()
)
mstpGenForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenForwardDelay.setStatus("current")


class _MstpGenMaxHops_Type(Integer32):
    """Custom type mstpGenMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MstpGenMaxHops_Type.__name__ = "Integer32"
_MstpGenMaxHops_Object = MibScalar
mstpGenMaxHops = _MstpGenMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 1, 8),
    _MstpGenMaxHops_Type()
)
mstpGenMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenMaxHops.setStatus("current")
_MstpGenCistRootPathCost_Type = Integer32
_MstpGenCistRootPathCost_Object = MibScalar
mstpGenCistRootPathCost = _MstpGenCistRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 1, 9),
    _MstpGenCistRootPathCost_Type()
)
mstpGenCistRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenCistRootPathCost.setStatus("current")


class _MstpGenCistRootBrid_Type(OctetString):
    """Custom type mstpGenCistRootBrid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_MstpGenCistRootBrid_Type.__name__ = "OctetString"
_MstpGenCistRootBrid_Object = MibScalar
mstpGenCistRootBrid = _MstpGenCistRootBrid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 1, 10),
    _MstpGenCistRootBrid_Type()
)
mstpGenCistRootBrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenCistRootBrid.setStatus("current")
_MstMapTable_Object = MibTable
mstMapTable = _MstMapTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 20)
)
if mibBuilder.loadTexts:
    mstMapTable.setStatus("current")
_MstMapEntry_Object = MibTableRow
mstMapEntry = _MstMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 20, 1)
)
mstMapEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "mstMapIndex"),
)
if mibBuilder.loadTexts:
    mstMapEntry.setStatus("current")
_MstMapIndex_Type = MstiOrCistInstanceIndex
_MstMapIndex_Object = MibTableColumn
mstMapIndex = _MstMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 20, 1, 1),
    _MstMapIndex_Type()
)
mstMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstMapIndex.setStatus("current")


class _MstMapVlans1k_Type(OctetString):
    """Custom type mstMapVlans1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstMapVlans1k_Type.__name__ = "OctetString"
_MstMapVlans1k_Object = MibTableColumn
mstMapVlans1k = _MstMapVlans1k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 20, 1, 2),
    _MstMapVlans1k_Type()
)
mstMapVlans1k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMapVlans1k.setStatus("current")


class _MstMapVlans2k_Type(OctetString):
    """Custom type mstMapVlans2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstMapVlans2k_Type.__name__ = "OctetString"
_MstMapVlans2k_Object = MibTableColumn
mstMapVlans2k = _MstMapVlans2k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 20, 1, 3),
    _MstMapVlans2k_Type()
)
mstMapVlans2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMapVlans2k.setStatus("current")


class _MstMapVlans3k_Type(OctetString):
    """Custom type mstMapVlans3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstMapVlans3k_Type.__name__ = "OctetString"
_MstMapVlans3k_Object = MibTableColumn
mstMapVlans3k = _MstMapVlans3k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 20, 1, 4),
    _MstMapVlans3k_Type()
)
mstMapVlans3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMapVlans3k.setStatus("current")


class _MstMapVlans4k_Type(OctetString):
    """Custom type mstMapVlans4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstMapVlans4k_Type.__name__ = "OctetString"
_MstMapVlans4k_Object = MibTableColumn
mstMapVlans4k = _MstMapVlans4k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 20, 1, 5),
    _MstMapVlans4k_Type()
)
mstMapVlans4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMapVlans4k.setStatus("current")
_MstMapRowStatus_Type = RowStatus
_MstMapRowStatus_Object = MibTableColumn
mstMapRowStatus = _MstMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 20, 1, 6),
    _MstMapRowStatus_Type()
)
mstMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstMapRowStatus.setStatus("current")
_MstVlanTable_Object = MibTable
mstVlanTable = _MstVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 30)
)
if mibBuilder.loadTexts:
    mstVlanTable.setStatus("current")
_MstVlanEntry_Object = MibTableRow
mstVlanEntry = _MstVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 30, 1)
)
mstVlanEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "mstVlanIndex"),
)
if mibBuilder.loadTexts:
    mstVlanEntry.setStatus("current")


class _MstVlanIndex_Type(Integer32):
    """Custom type mstVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MstVlanIndex_Type.__name__ = "Integer32"
_MstVlanIndex_Object = MibTableColumn
mstVlanIndex = _MstVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 30, 1, 1),
    _MstVlanIndex_Type()
)
mstVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstVlanIndex.setStatus("current")
_MstVlanMstIndex_Type = MstiOrCistInstanceIndex
_MstVlanMstIndex_Object = MibTableColumn
mstVlanMstIndex = _MstVlanMstIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 30, 1, 2),
    _MstVlanMstIndex_Type()
)
mstVlanMstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstVlanMstIndex.setStatus("current")
_MstpPortTable_Object = MibTable
mstpPortTable = _MstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 40)
)
if mibBuilder.loadTexts:
    mstpPortTable.setStatus("current")
_MstpPortEntry_Object = MibTableRow
mstpPortEntry = _MstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 40, 1)
)
mstpPortEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "mstpPortIndex"),
)
if mibBuilder.loadTexts:
    mstpPortEntry.setStatus("current")


class _MstpPortIndex_Type(Integer32):
    """Custom type mstpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MstpPortIndex_Type.__name__ = "Integer32"
_MstpPortIndex_Object = MibTableColumn
mstpPortIndex = _MstpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 40, 1, 1),
    _MstpPortIndex_Type()
)
mstpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstpPortIndex.setStatus("current")
_MstpPortOperEdgePort_Type = TruthValue
_MstpPortOperEdgePort_Object = MibTableColumn
mstpPortOperEdgePort = _MstpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 40, 1, 2),
    _MstpPortOperEdgePort_Type()
)
mstpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortOperEdgePort.setStatus("current")
_MstpPortOperPointToPointMAC_Type = TruthValue
_MstpPortOperPointToPointMAC_Object = MibTableColumn
mstpPortOperPointToPointMAC = _MstpPortOperPointToPointMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 40, 1, 3),
    _MstpPortOperPointToPointMAC_Type()
)
mstpPortOperPointToPointMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortOperPointToPointMAC.setStatus("current")


class _MstpPortAdminEdgePort_Type(Integer32):
    """Custom type mstpPortAdminEdgePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_MstpPortAdminEdgePort_Type.__name__ = "Integer32"
_MstpPortAdminEdgePort_Object = MibTableColumn
mstpPortAdminEdgePort = _MstpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 40, 1, 4),
    _MstpPortAdminEdgePort_Type()
)
mstpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpPortAdminEdgePort.setStatus("current")
_MstpXstTable_Object = MibTable
mstpXstTable = _MstpXstTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 50)
)
if mibBuilder.loadTexts:
    mstpXstTable.setStatus("current")
_MstpXstEntry_Object = MibTableRow
mstpXstEntry = _MstpXstEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 50, 1)
)
mstpXstEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "mstpXstId"),
)
if mibBuilder.loadTexts:
    mstpXstEntry.setStatus("current")
_MstpXstId_Type = MstiOrCistInstanceIndex
_MstpXstId_Object = MibTableColumn
mstpXstId = _MstpXstId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 50, 1, 1),
    _MstpXstId_Type()
)
mstpXstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstId.setStatus("current")


class _MstpXstBridgePriority_Type(Integer32):
    """Custom type mstpXstBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_MstpXstBridgePriority_Type.__name__ = "Integer32"
_MstpXstBridgePriority_Object = MibTableColumn
mstpXstBridgePriority = _MstpXstBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 50, 1, 2),
    _MstpXstBridgePriority_Type()
)
mstpXstBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpXstBridgePriority.setStatus("current")
_MstpXstBridgeId_Type = BridgeId
_MstpXstBridgeId_Object = MibTableColumn
mstpXstBridgeId = _MstpXstBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 50, 1, 3),
    _MstpXstBridgeId_Type()
)
mstpXstBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstBridgeId.setStatus("current")
_MstpXstInternalRootCost_Type = Integer32
_MstpXstInternalRootCost_Object = MibTableColumn
mstpXstInternalRootCost = _MstpXstInternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 50, 1, 4),
    _MstpXstInternalRootCost_Type()
)
mstpXstInternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstInternalRootCost.setStatus("current")
_MstpXstRootPort_Type = Integer32
_MstpXstRootPort_Object = MibTableColumn
mstpXstRootPort = _MstpXstRootPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 50, 1, 5),
    _MstpXstRootPort_Type()
)
mstpXstRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstRootPort.setStatus("current")
_MstpXstTimeSinceTopologyChange_Type = TimeTicks
_MstpXstTimeSinceTopologyChange_Object = MibTableColumn
mstpXstTimeSinceTopologyChange = _MstpXstTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 50, 1, 6),
    _MstpXstTimeSinceTopologyChange_Type()
)
mstpXstTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstTimeSinceTopologyChange.setStatus("current")
_MstpXstTopologyChangesCount_Type = Counter32
_MstpXstTopologyChangesCount_Object = MibTableColumn
mstpXstTopologyChangesCount = _MstpXstTopologyChangesCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 50, 1, 7),
    _MstpXstTopologyChangesCount_Type()
)
mstpXstTopologyChangesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstTopologyChangesCount.setStatus("current")
_MstpXstPortTable_Object = MibTable
mstpXstPortTable = _MstpXstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 60)
)
if mibBuilder.loadTexts:
    mstpXstPortTable.setStatus("current")
_MstpXstPortEntry_Object = MibTableRow
mstpXstPortEntry = _MstpXstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 60, 1)
)
mstpXstPortEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "mstpXstPortXstId"),
    (0, "ZYXEL-olt1408-MIB", "mstpXstPortIndex"),
)
if mibBuilder.loadTexts:
    mstpXstPortEntry.setStatus("current")
_MstpXstPortXstId_Type = MstiOrCistInstanceIndex
_MstpXstPortXstId_Object = MibTableColumn
mstpXstPortXstId = _MstpXstPortXstId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 60, 1, 1),
    _MstpXstPortXstId_Type()
)
mstpXstPortXstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstpXstPortXstId.setStatus("current")


class _MstpXstPortIndex_Type(Integer32):
    """Custom type mstpXstPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MstpXstPortIndex_Type.__name__ = "Integer32"
_MstpXstPortIndex_Object = MibTableColumn
mstpXstPortIndex = _MstpXstPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 60, 1, 2),
    _MstpXstPortIndex_Type()
)
mstpXstPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortIndex.setStatus("current")
_MstpXstPortEnable_Type = EnabledStatus
_MstpXstPortEnable_Object = MibTableColumn
mstpXstPortEnable = _MstpXstPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 60, 1, 3),
    _MstpXstPortEnable_Type()
)
mstpXstPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpXstPortEnable.setStatus("current")


class _MstpXstPortPriority_Type(Integer32):
    """Custom type mstpXstPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MstpXstPortPriority_Type.__name__ = "Integer32"
_MstpXstPortPriority_Object = MibTableColumn
mstpXstPortPriority = _MstpXstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 60, 1, 4),
    _MstpXstPortPriority_Type()
)
mstpXstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpXstPortPriority.setStatus("current")


class _MstpXstPortPathCost_Type(Integer32):
    """Custom type mstpXstPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MstpXstPortPathCost_Type.__name__ = "Integer32"
_MstpXstPortPathCost_Object = MibTableColumn
mstpXstPortPathCost = _MstpXstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 60, 1, 5),
    _MstpXstPortPathCost_Type()
)
mstpXstPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpXstPortPathCost.setStatus("current")


class _MstpXstPortState_Type(Integer32):
    """Custom type mstpXstPortState based on Integer32"""
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
        *(("disabled", 0),
          ("discarding", 1),
          ("learning", 2),
          ("forwarding", 3),
          ("unknown", 4))
    )


_MstpXstPortState_Type.__name__ = "Integer32"
_MstpXstPortState_Object = MibTableColumn
mstpXstPortState = _MstpXstPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 60, 1, 6),
    _MstpXstPortState_Type()
)
mstpXstPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortState.setStatus("current")
_MstpXstPortDesignatedRoot_Type = BridgeId
_MstpXstPortDesignatedRoot_Object = MibTableColumn
mstpXstPortDesignatedRoot = _MstpXstPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 60, 1, 7),
    _MstpXstPortDesignatedRoot_Type()
)
mstpXstPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedRoot.setStatus("current")
_MstpXstPortDesignatedCost_Type = Integer32
_MstpXstPortDesignatedCost_Object = MibTableColumn
mstpXstPortDesignatedCost = _MstpXstPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 60, 1, 8),
    _MstpXstPortDesignatedCost_Type()
)
mstpXstPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedCost.setStatus("current")
_MstpXstPortDesignatedBridge_Type = BridgeId
_MstpXstPortDesignatedBridge_Object = MibTableColumn
mstpXstPortDesignatedBridge = _MstpXstPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 60, 1, 9),
    _MstpXstPortDesignatedBridge_Type()
)
mstpXstPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedBridge.setStatus("current")
_MstpXstPortDesignatedPort_Type = Integer32
_MstpXstPortDesignatedPort_Object = MibTableColumn
mstpXstPortDesignatedPort = _MstpXstPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 60, 1, 10),
    _MstpXstPortDesignatedPort_Type()
)
mstpXstPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedPort.setStatus("current")
_MstpNotifications_ObjectIdentity = ObjectIdentity
mstpNotifications = _MstpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 70)
)
_RadiusServerSetup_ObjectIdentity = ObjectIdentity
radiusServerSetup = _RadiusServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 108)
)
_RadiusAuthServerSetup_ObjectIdentity = ObjectIdentity
radiusAuthServerSetup = _RadiusAuthServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 108, 1)
)


class _RadiusAuthServerMode_Type(Integer32):
    """Custom type radiusAuthServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("indexPriority", 1),
          ("roundRobin", 2))
    )


_RadiusAuthServerMode_Type.__name__ = "Integer32"
_RadiusAuthServerMode_Object = MibScalar
radiusAuthServerMode = _RadiusAuthServerMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 108, 1, 1),
    _RadiusAuthServerMode_Type()
)
radiusAuthServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerMode.setStatus("current")
_RadiusAuthServerTimeout_Type = Integer32
_RadiusAuthServerTimeout_Object = MibScalar
radiusAuthServerTimeout = _RadiusAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 108, 1, 2),
    _RadiusAuthServerTimeout_Type()
)
radiusAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerTimeout.setStatus("current")
_RadiusAuthServerTable_Object = MibTable
radiusAuthServerTable = _RadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 108, 1, 3)
)
if mibBuilder.loadTexts:
    radiusAuthServerTable.setStatus("current")
_RadiusAuthServerEntry_Object = MibTableRow
radiusAuthServerEntry = _RadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 108, 1, 3, 1)
)
radiusAuthServerEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "radiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    radiusAuthServerEntry.setStatus("current")
_RadiusAuthServerIndex_Type = Integer32
_RadiusAuthServerIndex_Object = MibTableColumn
radiusAuthServerIndex = _RadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 108, 1, 3, 1, 1),
    _RadiusAuthServerIndex_Type()
)
radiusAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAuthServerIndex.setStatus("current")
_RadiusAuthServerIpAddr_Type = IpAddress
_RadiusAuthServerIpAddr_Object = MibTableColumn
radiusAuthServerIpAddr = _RadiusAuthServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 108, 1, 3, 1, 2),
    _RadiusAuthServerIpAddr_Type()
)
radiusAuthServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerIpAddr.setStatus("current")
_RadiusAuthServerUdpPort_Type = Integer32
_RadiusAuthServerUdpPort_Object = MibTableColumn
radiusAuthServerUdpPort = _RadiusAuthServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 108, 1, 3, 1, 3),
    _RadiusAuthServerUdpPort_Type()
)
radiusAuthServerUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerUdpPort.setStatus("current")
_RadiusAuthServerSharedSecret_Type = DisplayString
_RadiusAuthServerSharedSecret_Object = MibTableColumn
radiusAuthServerSharedSecret = _RadiusAuthServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 108, 1, 3, 1, 4),
    _RadiusAuthServerSharedSecret_Type()
)
radiusAuthServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerSharedSecret.setStatus("current")
_RadiusAcctServerSetup_ObjectIdentity = ObjectIdentity
radiusAcctServerSetup = _RadiusAcctServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 108, 2)
)
_RadiusAcctServerTimeout_Type = Integer32
_RadiusAcctServerTimeout_Object = MibScalar
radiusAcctServerTimeout = _RadiusAcctServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 108, 2, 1),
    _RadiusAcctServerTimeout_Type()
)
radiusAcctServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerTimeout.setStatus("current")
_RadiusAcctServerTable_Object = MibTable
radiusAcctServerTable = _RadiusAcctServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 108, 2, 2)
)
if mibBuilder.loadTexts:
    radiusAcctServerTable.setStatus("current")
_RadiusAcctServerEntry_Object = MibTableRow
radiusAcctServerEntry = _RadiusAcctServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 108, 2, 2, 1)
)
radiusAcctServerEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "radiusAcctServerIndex"),
)
if mibBuilder.loadTexts:
    radiusAcctServerEntry.setStatus("current")
_RadiusAcctServerIndex_Type = Integer32
_RadiusAcctServerIndex_Object = MibTableColumn
radiusAcctServerIndex = _RadiusAcctServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 108, 2, 2, 1, 1),
    _RadiusAcctServerIndex_Type()
)
radiusAcctServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAcctServerIndex.setStatus("current")
_RadiusAcctServerIpAddr_Type = IpAddress
_RadiusAcctServerIpAddr_Object = MibTableColumn
radiusAcctServerIpAddr = _RadiusAcctServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 108, 2, 2, 1, 2),
    _RadiusAcctServerIpAddr_Type()
)
radiusAcctServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerIpAddr.setStatus("current")
_RadiusAcctServerUdpPort_Type = Integer32
_RadiusAcctServerUdpPort_Object = MibTableColumn
radiusAcctServerUdpPort = _RadiusAcctServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 108, 2, 2, 1, 3),
    _RadiusAcctServerUdpPort_Type()
)
radiusAcctServerUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerUdpPort.setStatus("current")
_RadiusAcctServerSharedSecret_Type = DisplayString
_RadiusAcctServerSharedSecret_Object = MibTableColumn
radiusAcctServerSharedSecret = _RadiusAcctServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 108, 2, 2, 1, 4),
    _RadiusAcctServerSharedSecret_Type()
)
radiusAcctServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerSharedSecret.setStatus("current")
_TacacsServerSetup_ObjectIdentity = ObjectIdentity
tacacsServerSetup = _TacacsServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 109)
)
_TacacsAuthServerSetup_ObjectIdentity = ObjectIdentity
tacacsAuthServerSetup = _TacacsAuthServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 109, 1)
)


class _TacacsAuthServerMode_Type(Integer32):
    """Custom type tacacsAuthServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("indexPriority", 1),
          ("roundRobin", 2))
    )


_TacacsAuthServerMode_Type.__name__ = "Integer32"
_TacacsAuthServerMode_Object = MibScalar
tacacsAuthServerMode = _TacacsAuthServerMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 109, 1, 1),
    _TacacsAuthServerMode_Type()
)
tacacsAuthServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerMode.setStatus("current")
_TacacsAuthServerTimeout_Type = Integer32
_TacacsAuthServerTimeout_Object = MibScalar
tacacsAuthServerTimeout = _TacacsAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 109, 1, 2),
    _TacacsAuthServerTimeout_Type()
)
tacacsAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerTimeout.setStatus("current")
_TacacsAuthServerTable_Object = MibTable
tacacsAuthServerTable = _TacacsAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 109, 1, 3)
)
if mibBuilder.loadTexts:
    tacacsAuthServerTable.setStatus("current")
_TacacsAuthServerEntry_Object = MibTableRow
tacacsAuthServerEntry = _TacacsAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 109, 1, 3, 1)
)
tacacsAuthServerEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "tacacsAuthServerIndex"),
)
if mibBuilder.loadTexts:
    tacacsAuthServerEntry.setStatus("current")
_TacacsAuthServerIndex_Type = Integer32
_TacacsAuthServerIndex_Object = MibTableColumn
tacacsAuthServerIndex = _TacacsAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 109, 1, 3, 1, 1),
    _TacacsAuthServerIndex_Type()
)
tacacsAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacacsAuthServerIndex.setStatus("current")
_TacacsAuthServerIpAddr_Type = IpAddress
_TacacsAuthServerIpAddr_Object = MibTableColumn
tacacsAuthServerIpAddr = _TacacsAuthServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 109, 1, 3, 1, 2),
    _TacacsAuthServerIpAddr_Type()
)
tacacsAuthServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerIpAddr.setStatus("current")
_TacacsAuthServerTcpPort_Type = Integer32
_TacacsAuthServerTcpPort_Object = MibTableColumn
tacacsAuthServerTcpPort = _TacacsAuthServerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 109, 1, 3, 1, 3),
    _TacacsAuthServerTcpPort_Type()
)
tacacsAuthServerTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerTcpPort.setStatus("current")
_TacacsAuthServerSharedSecret_Type = DisplayString
_TacacsAuthServerSharedSecret_Object = MibTableColumn
tacacsAuthServerSharedSecret = _TacacsAuthServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 109, 1, 3, 1, 4),
    _TacacsAuthServerSharedSecret_Type()
)
tacacsAuthServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerSharedSecret.setStatus("current")
_TacacsAcctServerSetup_ObjectIdentity = ObjectIdentity
tacacsAcctServerSetup = _TacacsAcctServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 109, 2)
)
_TacacsAcctServerTimeout_Type = Integer32
_TacacsAcctServerTimeout_Object = MibScalar
tacacsAcctServerTimeout = _TacacsAcctServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 109, 2, 1),
    _TacacsAcctServerTimeout_Type()
)
tacacsAcctServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAcctServerTimeout.setStatus("current")
_TacacsAcctServerTable_Object = MibTable
tacacsAcctServerTable = _TacacsAcctServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 109, 2, 2)
)
if mibBuilder.loadTexts:
    tacacsAcctServerTable.setStatus("current")
_TacacsAcctServerEntry_Object = MibTableRow
tacacsAcctServerEntry = _TacacsAcctServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 109, 2, 2, 1)
)
tacacsAcctServerEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "tacacsAcctServerIndex"),
)
if mibBuilder.loadTexts:
    tacacsAcctServerEntry.setStatus("current")
_TacacsAcctServerIndex_Type = Integer32
_TacacsAcctServerIndex_Object = MibTableColumn
tacacsAcctServerIndex = _TacacsAcctServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 109, 2, 2, 1, 1),
    _TacacsAcctServerIndex_Type()
)
tacacsAcctServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacacsAcctServerIndex.setStatus("current")
_TacacsAcctServerIpAddr_Type = IpAddress
_TacacsAcctServerIpAddr_Object = MibTableColumn
tacacsAcctServerIpAddr = _TacacsAcctServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 109, 2, 2, 1, 2),
    _TacacsAcctServerIpAddr_Type()
)
tacacsAcctServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAcctServerIpAddr.setStatus("current")
_TacacsAcctServerTcpPort_Type = Integer32
_TacacsAcctServerTcpPort_Object = MibTableColumn
tacacsAcctServerTcpPort = _TacacsAcctServerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 109, 2, 2, 1, 3),
    _TacacsAcctServerTcpPort_Type()
)
tacacsAcctServerTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAcctServerTcpPort.setStatus("current")
_TacacsAcctServerSharedSecret_Type = DisplayString
_TacacsAcctServerSharedSecret_Object = MibTableColumn
tacacsAcctServerSharedSecret = _TacacsAcctServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 109, 2, 2, 1, 4),
    _TacacsAcctServerSharedSecret_Type()
)
tacacsAcctServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAcctServerSharedSecret.setStatus("current")
_AaaSetup_ObjectIdentity = ObjectIdentity
aaaSetup = _AaaSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110)
)
_AuthenticationSetup_ObjectIdentity = ObjectIdentity
authenticationSetup = _AuthenticationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 1)
)
_AuthenticationTypeTable_Object = MibTable
authenticationTypeTable = _AuthenticationTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 1, 1)
)
if mibBuilder.loadTexts:
    authenticationTypeTable.setStatus("current")
_AuthenticationTypeEntry_Object = MibTableRow
authenticationTypeEntry = _AuthenticationTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 1, 1, 1)
)
authenticationTypeEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "authenticationTypeName"),
)
if mibBuilder.loadTexts:
    authenticationTypeEntry.setStatus("current")
_AuthenticationTypeName_Type = DisplayString
_AuthenticationTypeName_Object = MibTableColumn
authenticationTypeName = _AuthenticationTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 1, 1, 1, 1),
    _AuthenticationTypeName_Type()
)
authenticationTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenticationTypeName.setStatus("current")
_AuthenticationTypeMethodList_Type = OctetString
_AuthenticationTypeMethodList_Object = MibTableColumn
authenticationTypeMethodList = _AuthenticationTypeMethodList_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 1, 1, 1, 2),
    _AuthenticationTypeMethodList_Type()
)
authenticationTypeMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationTypeMethodList.setStatus("current")
_AccountingSetup_ObjectIdentity = ObjectIdentity
accountingSetup = _AccountingSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 2)
)
_AccountingUpdatePeriod_Type = Integer32
_AccountingUpdatePeriod_Object = MibScalar
accountingUpdatePeriod = _AccountingUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 2, 1),
    _AccountingUpdatePeriod_Type()
)
accountingUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingUpdatePeriod.setStatus("current")
_AccountingTypeTable_Object = MibTable
accountingTypeTable = _AccountingTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 2, 2)
)
if mibBuilder.loadTexts:
    accountingTypeTable.setStatus("current")
_AccountingTypeEntry_Object = MibTableRow
accountingTypeEntry = _AccountingTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 2, 2, 1)
)
accountingTypeEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "accountingTypeName"),
)
if mibBuilder.loadTexts:
    accountingTypeEntry.setStatus("current")
_AccountingTypeName_Type = DisplayString
_AccountingTypeName_Object = MibTableColumn
accountingTypeName = _AccountingTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 2, 2, 1, 1),
    _AccountingTypeName_Type()
)
accountingTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accountingTypeName.setStatus("current")
_AccountingTypeActive_Type = EnabledStatus
_AccountingTypeActive_Object = MibTableColumn
accountingTypeActive = _AccountingTypeActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 2, 2, 1, 2),
    _AccountingTypeActive_Type()
)
accountingTypeActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingTypeActive.setStatus("current")
_AccountingTypeBroadcast_Type = EnabledStatus
_AccountingTypeBroadcast_Object = MibTableColumn
accountingTypeBroadcast = _AccountingTypeBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 2, 2, 1, 3),
    _AccountingTypeBroadcast_Type()
)
accountingTypeBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingTypeBroadcast.setStatus("current")


class _AccountingTypeMode_Type(Integer32):
    """Custom type accountingTypeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("startStop", 1),
          ("stopOnly", 2),
          ("notAvailable", 255))
    )


_AccountingTypeMode_Type.__name__ = "Integer32"
_AccountingTypeMode_Object = MibTableColumn
accountingTypeMode = _AccountingTypeMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 2, 2, 1, 4),
    _AccountingTypeMode_Type()
)
accountingTypeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingTypeMode.setStatus("current")


class _AccountingTypeMethod_Type(Integer32):
    """Custom type accountingTypeMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("tacacs", 2))
    )


_AccountingTypeMethod_Type.__name__ = "Integer32"
_AccountingTypeMethod_Object = MibTableColumn
accountingTypeMethod = _AccountingTypeMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 2, 2, 1, 5),
    _AccountingTypeMethod_Type()
)
accountingTypeMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingTypeMethod.setStatus("current")


class _AccountingTypePrivilege_Type(Integer32):
    """Custom type accountingTypePrivilege based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("privilege0", 0),
          ("privilege1", 1),
          ("privilege2", 2),
          ("privilege3", 3),
          ("privilege4", 4),
          ("privilege5", 5),
          ("privilege6", 6),
          ("privilege7", 7),
          ("privilege8", 8),
          ("privilege9", 9),
          ("privilege10", 10),
          ("privilege11", 11),
          ("privilege12", 12),
          ("privilege13", 13),
          ("privilege14", 14),
          ("notAvailable", 255))
    )


_AccountingTypePrivilege_Type.__name__ = "Integer32"
_AccountingTypePrivilege_Object = MibTableColumn
accountingTypePrivilege = _AccountingTypePrivilege_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 2, 2, 1, 6),
    _AccountingTypePrivilege_Type()
)
accountingTypePrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingTypePrivilege.setStatus("current")
_AuthorizationSetup_ObjectIdentity = ObjectIdentity
authorizationSetup = _AuthorizationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 3)
)
_AuthorizationTypeTable_Object = MibTable
authorizationTypeTable = _AuthorizationTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 3, 1)
)
if mibBuilder.loadTexts:
    authorizationTypeTable.setStatus("current")
_AuthorizationTypeEntry_Object = MibTableRow
authorizationTypeEntry = _AuthorizationTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 3, 1, 1)
)
authorizationTypeEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "authorizationTypeName"),
)
if mibBuilder.loadTexts:
    authorizationTypeEntry.setStatus("current")
_AuthorizationTypeName_Type = DisplayString
_AuthorizationTypeName_Object = MibTableColumn
authorizationTypeName = _AuthorizationTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 3, 1, 1, 1),
    _AuthorizationTypeName_Type()
)
authorizationTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authorizationTypeName.setStatus("current")
_AuthorizationTypeActive_Type = EnabledStatus
_AuthorizationTypeActive_Object = MibTableColumn
authorizationTypeActive = _AuthorizationTypeActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 3, 1, 1, 2),
    _AuthorizationTypeActive_Type()
)
authorizationTypeActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authorizationTypeActive.setStatus("current")


class _AuthorizationTypeMethod_Type(Integer32):
    """Custom type authorizationTypeMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("tacacs", 2))
    )


_AuthorizationTypeMethod_Type.__name__ = "Integer32"
_AuthorizationTypeMethod_Object = MibTableColumn
authorizationTypeMethod = _AuthorizationTypeMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 110, 3, 1, 1, 3),
    _AuthorizationTypeMethod_Type()
)
authorizationTypeMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authorizationTypeMethod.setStatus("current")
_VlanTranslationSetup_ObjectIdentity = ObjectIdentity
vlanTranslationSetup = _VlanTranslationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 116)
)
_VlanTranslationRuleTable_Object = MibTable
vlanTranslationRuleTable = _VlanTranslationRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 116, 1)
)
if mibBuilder.loadTexts:
    vlanTranslationRuleTable.setStatus("current")
_VlanTranslationRuleEntry_Object = MibTableRow
vlanTranslationRuleEntry = _VlanTranslationRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 116, 1, 1)
)
vlanTranslationRuleEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "vlanTranslationRulePort"),
    (0, "ZYXEL-olt1408-MIB", "vlanTranslationRuleOuterVid"),
    (0, "ZYXEL-olt1408-MIB", "vlanTranslationRuleOuterPriority"),
    (0, "ZYXEL-olt1408-MIB", "vlanTranslationRuleInnerVid"),
    (0, "ZYXEL-olt1408-MIB", "vlanTranslationRuleInnerPriority"),
)
if mibBuilder.loadTexts:
    vlanTranslationRuleEntry.setStatus("current")
_VlanTranslationRuleName_Type = DisplayString
_VlanTranslationRuleName_Object = MibTableColumn
vlanTranslationRuleName = _VlanTranslationRuleName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 116, 1, 1, 1),
    _VlanTranslationRuleName_Type()
)
vlanTranslationRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTranslationRuleName.setStatus("current")
_VlanTranslationRulePort_Type = Integer32
_VlanTranslationRulePort_Object = MibTableColumn
vlanTranslationRulePort = _VlanTranslationRulePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 116, 1, 1, 2),
    _VlanTranslationRulePort_Type()
)
vlanTranslationRulePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTranslationRulePort.setStatus("current")
_VlanTranslationRuleOuterVid_Type = Integer32
_VlanTranslationRuleOuterVid_Object = MibTableColumn
vlanTranslationRuleOuterVid = _VlanTranslationRuleOuterVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 116, 1, 1, 3),
    _VlanTranslationRuleOuterVid_Type()
)
vlanTranslationRuleOuterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTranslationRuleOuterVid.setStatus("current")


class _VlanTranslationRuleOuterPriority_Type(Integer32):
    """Custom type vlanTranslationRuleOuterPriority based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7),
          ("priorityIgnore", 8))
    )


_VlanTranslationRuleOuterPriority_Type.__name__ = "Integer32"
_VlanTranslationRuleOuterPriority_Object = MibTableColumn
vlanTranslationRuleOuterPriority = _VlanTranslationRuleOuterPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 116, 1, 1, 4),
    _VlanTranslationRuleOuterPriority_Type()
)
vlanTranslationRuleOuterPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTranslationRuleOuterPriority.setStatus("current")
_VlanTranslationRuleInnerVid_Type = Integer32
_VlanTranslationRuleInnerVid_Object = MibTableColumn
vlanTranslationRuleInnerVid = _VlanTranslationRuleInnerVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 116, 1, 1, 5),
    _VlanTranslationRuleInnerVid_Type()
)
vlanTranslationRuleInnerVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTranslationRuleInnerVid.setStatus("current")


class _VlanTranslationRuleInnerPriority_Type(Integer32):
    """Custom type vlanTranslationRuleInnerPriority based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7),
          ("priorityIgnore", 8))
    )


_VlanTranslationRuleInnerPriority_Type.__name__ = "Integer32"
_VlanTranslationRuleInnerPriority_Object = MibTableColumn
vlanTranslationRuleInnerPriority = _VlanTranslationRuleInnerPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 116, 1, 1, 6),
    _VlanTranslationRuleInnerPriority_Type()
)
vlanTranslationRuleInnerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTranslationRuleInnerPriority.setStatus("current")
_VlanTranslationRuleTransSVid_Type = Integer32
_VlanTranslationRuleTransSVid_Object = MibTableColumn
vlanTranslationRuleTransSVid = _VlanTranslationRuleTransSVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 116, 1, 1, 7),
    _VlanTranslationRuleTransSVid_Type()
)
vlanTranslationRuleTransSVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTranslationRuleTransSVid.setStatus("current")


class _VlanTranslationRuleSPriority_Type(Integer32):
    """Custom type vlanTranslationRuleSPriority based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7),
          ("priorityIgnore", 8))
    )


_VlanTranslationRuleSPriority_Type.__name__ = "Integer32"
_VlanTranslationRuleSPriority_Object = MibTableColumn
vlanTranslationRuleSPriority = _VlanTranslationRuleSPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 116, 1, 1, 8),
    _VlanTranslationRuleSPriority_Type()
)
vlanTranslationRuleSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTranslationRuleSPriority.setStatus("current")
_VlanTranslationRuleTransCVid_Type = Integer32
_VlanTranslationRuleTransCVid_Object = MibTableColumn
vlanTranslationRuleTransCVid = _VlanTranslationRuleTransCVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 116, 1, 1, 9),
    _VlanTranslationRuleTransCVid_Type()
)
vlanTranslationRuleTransCVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTranslationRuleTransCVid.setStatus("current")


class _VlanTranslationRuleCPriority_Type(Integer32):
    """Custom type vlanTranslationRuleCPriority based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7),
          ("priorityIgnore", 8))
    )


_VlanTranslationRuleCPriority_Type.__name__ = "Integer32"
_VlanTranslationRuleCPriority_Object = MibTableColumn
vlanTranslationRuleCPriority = _VlanTranslationRuleCPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 116, 1, 1, 10),
    _VlanTranslationRuleCPriority_Type()
)
vlanTranslationRuleCPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTranslationRuleCPriority.setStatus("current")
_VlanTranslationRuleN1Map_Type = Integer32
_VlanTranslationRuleN1Map_Object = MibTableColumn
vlanTranslationRuleN1Map = _VlanTranslationRuleN1Map_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 116, 1, 1, 11),
    _VlanTranslationRuleN1Map_Type()
)
vlanTranslationRuleN1Map.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTranslationRuleN1Map.setStatus("current")


class _VlanTranslationRuleCrossConnect_Type(Integer32):
    """Custom type vlanTranslationRuleCrossConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_VlanTranslationRuleCrossConnect_Type.__name__ = "Integer32"
_VlanTranslationRuleCrossConnect_Object = MibTableColumn
vlanTranslationRuleCrossConnect = _VlanTranslationRuleCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 116, 1, 1, 12),
    _VlanTranslationRuleCrossConnect_Type()
)
vlanTranslationRuleCrossConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTranslationRuleCrossConnect.setStatus("current")
_VlanTranslationRuleCrossPort_Type = Integer32
_VlanTranslationRuleCrossPort_Object = MibTableColumn
vlanTranslationRuleCrossPort = _VlanTranslationRuleCrossPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 116, 1, 1, 13),
    _VlanTranslationRuleCrossPort_Type()
)
vlanTranslationRuleCrossPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTranslationRuleCrossPort.setStatus("current")


class _VlanTranslationRuleTr156_Type(Integer32):
    """Custom type vlanTranslationRuleTr156 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_VlanTranslationRuleTr156_Type.__name__ = "Integer32"
_VlanTranslationRuleTr156_Object = MibTableColumn
vlanTranslationRuleTr156 = _VlanTranslationRuleTr156_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 116, 1, 1, 14),
    _VlanTranslationRuleTr156_Type()
)
vlanTranslationRuleTr156.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTranslationRuleTr156.setStatus("current")
_VlanTranslationRuleRowStatus_Type = RowStatus
_VlanTranslationRuleRowStatus_Object = MibTableColumn
vlanTranslationRuleRowStatus = _VlanTranslationRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 116, 1, 1, 15),
    _VlanTranslationRuleRowStatus_Type()
)
vlanTranslationRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTranslationRuleRowStatus.setStatus("current")
_TransceiverInfo_ObjectIdentity = ObjectIdentity
transceiverInfo = _TransceiverInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117)
)
_TransceiverSerialInfoTable_Object = MibTable
transceiverSerialInfoTable = _TransceiverSerialInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 1)
)
if mibBuilder.loadTexts:
    transceiverSerialInfoTable.setStatus("current")
_TransceiverSerialInfoEntry_Object = MibTableRow
transceiverSerialInfoEntry = _TransceiverSerialInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 1, 1)
)
transceiverSerialInfoEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "transceiverSerialInfoEntryPort"),
)
if mibBuilder.loadTexts:
    transceiverSerialInfoEntry.setStatus("current")
_TransceiverSerialInfoEntryPort_Type = Integer32
_TransceiverSerialInfoEntryPort_Object = MibTableColumn
transceiverSerialInfoEntryPort = _TransceiverSerialInfoEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 1, 1, 1),
    _TransceiverSerialInfoEntryPort_Type()
)
transceiverSerialInfoEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryPort.setStatus("current")


class _TransceiverSerialInfoEntryStatus_Type(Integer32):
    """Custom type transceiverSerialInfoEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("okWithDdm", 1),
          ("okWithoutDdm", 2),
          ("nonOperational", 3))
    )


_TransceiverSerialInfoEntryStatus_Type.__name__ = "Integer32"
_TransceiverSerialInfoEntryStatus_Object = MibTableColumn
transceiverSerialInfoEntryStatus = _TransceiverSerialInfoEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 1, 1, 2),
    _TransceiverSerialInfoEntryStatus_Type()
)
transceiverSerialInfoEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryStatus.setStatus("current")
_TransceiverSerialInfoEntryVendor_Type = DisplayString
_TransceiverSerialInfoEntryVendor_Object = MibTableColumn
transceiverSerialInfoEntryVendor = _TransceiverSerialInfoEntryVendor_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 1, 1, 3),
    _TransceiverSerialInfoEntryVendor_Type()
)
transceiverSerialInfoEntryVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryVendor.setStatus("current")
_TransceiverSerialInfoEntryPartNo_Type = DisplayString
_TransceiverSerialInfoEntryPartNo_Object = MibTableColumn
transceiverSerialInfoEntryPartNo = _TransceiverSerialInfoEntryPartNo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 1, 1, 4),
    _TransceiverSerialInfoEntryPartNo_Type()
)
transceiverSerialInfoEntryPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryPartNo.setStatus("current")
_TransceiverSerialInfoEntrySerialNo_Type = DisplayString
_TransceiverSerialInfoEntrySerialNo_Object = MibTableColumn
transceiverSerialInfoEntrySerialNo = _TransceiverSerialInfoEntrySerialNo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 1, 1, 5),
    _TransceiverSerialInfoEntrySerialNo_Type()
)
transceiverSerialInfoEntrySerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntrySerialNo.setStatus("current")
_TransceiverSerialInfoEntryRevision_Type = DisplayString
_TransceiverSerialInfoEntryRevision_Object = MibTableColumn
transceiverSerialInfoEntryRevision = _TransceiverSerialInfoEntryRevision_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 1, 1, 6),
    _TransceiverSerialInfoEntryRevision_Type()
)
transceiverSerialInfoEntryRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryRevision.setStatus("current")
_TransceiverSerialInfoEntryDateCode_Type = DisplayString
_TransceiverSerialInfoEntryDateCode_Object = MibTableColumn
transceiverSerialInfoEntryDateCode = _TransceiverSerialInfoEntryDateCode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 1, 1, 7),
    _TransceiverSerialInfoEntryDateCode_Type()
)
transceiverSerialInfoEntryDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryDateCode.setStatus("current")
_TransceiverSerialInfoEntryTransceiver_Type = DisplayString
_TransceiverSerialInfoEntryTransceiver_Object = MibTableColumn
transceiverSerialInfoEntryTransceiver = _TransceiverSerialInfoEntryTransceiver_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 1, 1, 8),
    _TransceiverSerialInfoEntryTransceiver_Type()
)
transceiverSerialInfoEntryTransceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryTransceiver.setStatus("current")
_TransceiverDdmInfoTable_Object = MibTable
transceiverDdmInfoTable = _TransceiverDdmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 2)
)
if mibBuilder.loadTexts:
    transceiverDdmInfoTable.setStatus("current")
_TransceiverDdmInfoEntry_Object = MibTableRow
transceiverDdmInfoEntry = _TransceiverDdmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 2, 1)
)
transceiverDdmInfoEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "transceiverDdmInfoEntryPort"),
    (0, "ZYXEL-olt1408-MIB", "transceiverDdmInfoEntryType"),
)
if mibBuilder.loadTexts:
    transceiverDdmInfoEntry.setStatus("current")
_TransceiverDdmInfoEntryPort_Type = Integer32
_TransceiverDdmInfoEntryPort_Object = MibTableColumn
transceiverDdmInfoEntryPort = _TransceiverDdmInfoEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 2, 1, 1),
    _TransceiverDdmInfoEntryPort_Type()
)
transceiverDdmInfoEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryPort.setStatus("current")
_TransceiverDdmInfoEntryType_Type = Integer32
_TransceiverDdmInfoEntryType_Object = MibTableColumn
transceiverDdmInfoEntryType = _TransceiverDdmInfoEntryType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 2, 1, 2),
    _TransceiverDdmInfoEntryType_Type()
)
transceiverDdmInfoEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryType.setStatus("current")
_TransceiverDdmInfoEntryAlarmMax_Type = DisplayString
_TransceiverDdmInfoEntryAlarmMax_Object = MibTableColumn
transceiverDdmInfoEntryAlarmMax = _TransceiverDdmInfoEntryAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 2, 1, 3),
    _TransceiverDdmInfoEntryAlarmMax_Type()
)
transceiverDdmInfoEntryAlarmMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryAlarmMax.setStatus("current")
_TransceiverDdmInfoEntryAlarmMin_Type = DisplayString
_TransceiverDdmInfoEntryAlarmMin_Object = MibTableColumn
transceiverDdmInfoEntryAlarmMin = _TransceiverDdmInfoEntryAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 2, 1, 4),
    _TransceiverDdmInfoEntryAlarmMin_Type()
)
transceiverDdmInfoEntryAlarmMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryAlarmMin.setStatus("current")
_TransceiverDdmInfoEntryWarnMax_Type = DisplayString
_TransceiverDdmInfoEntryWarnMax_Object = MibTableColumn
transceiverDdmInfoEntryWarnMax = _TransceiverDdmInfoEntryWarnMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 2, 1, 5),
    _TransceiverDdmInfoEntryWarnMax_Type()
)
transceiverDdmInfoEntryWarnMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryWarnMax.setStatus("current")
_TransceiverDdmInfoEntryWarnMin_Type = DisplayString
_TransceiverDdmInfoEntryWarnMin_Object = MibTableColumn
transceiverDdmInfoEntryWarnMin = _TransceiverDdmInfoEntryWarnMin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 2, 1, 6),
    _TransceiverDdmInfoEntryWarnMin_Type()
)
transceiverDdmInfoEntryWarnMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryWarnMin.setStatus("current")
_TransceiverDdmInfoEntryCurrent_Type = DisplayString
_TransceiverDdmInfoEntryCurrent_Object = MibTableColumn
transceiverDdmInfoEntryCurrent = _TransceiverDdmInfoEntryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 2, 1, 7),
    _TransceiverDdmInfoEntryCurrent_Type()
)
transceiverDdmInfoEntryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryCurrent.setStatus("current")
_TransceiverDdmInfoEntryDescription_Type = DisplayString
_TransceiverDdmInfoEntryDescription_Object = MibTableColumn
transceiverDdmInfoEntryDescription = _TransceiverDdmInfoEntryDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 2, 1, 8),
    _TransceiverDdmInfoEntryDescription_Type()
)
transceiverDdmInfoEntryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryDescription.setStatus("current")
_TransceiverDdmInfoProfileTable_Object = MibTable
transceiverDdmInfoProfileTable = _TransceiverDdmInfoProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 3)
)
if mibBuilder.loadTexts:
    transceiverDdmInfoProfileTable.setStatus("current")
_TransceiverDdmInfoProfileEntry_Object = MibTableRow
transceiverDdmInfoProfileEntry = _TransceiverDdmInfoProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 3, 1)
)
transceiverDdmInfoProfileEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "transceiverDdmInfoProfilePort"),
    (0, "ZYXEL-olt1408-MIB", "transceiverDdmInfoProfileType"),
)
if mibBuilder.loadTexts:
    transceiverDdmInfoProfileEntry.setStatus("current")
_TransceiverDdmInfoProfilePort_Type = Integer32
_TransceiverDdmInfoProfilePort_Object = MibTableColumn
transceiverDdmInfoProfilePort = _TransceiverDdmInfoProfilePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 3, 1, 1),
    _TransceiverDdmInfoProfilePort_Type()
)
transceiverDdmInfoProfilePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoProfilePort.setStatus("current")
_TransceiverDdmInfoProfileType_Type = Integer32
_TransceiverDdmInfoProfileType_Object = MibTableColumn
transceiverDdmInfoProfileType = _TransceiverDdmInfoProfileType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 3, 1, 2),
    _TransceiverDdmInfoProfileType_Type()
)
transceiverDdmInfoProfileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoProfileType.setStatus("current")
_TransceiverDdmInfoProfileAlarmMax_Type = DisplayString
_TransceiverDdmInfoProfileAlarmMax_Object = MibTableColumn
transceiverDdmInfoProfileAlarmMax = _TransceiverDdmInfoProfileAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 3, 1, 3),
    _TransceiverDdmInfoProfileAlarmMax_Type()
)
transceiverDdmInfoProfileAlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transceiverDdmInfoProfileAlarmMax.setStatus("current")
_TransceiverDdmInfoProfileAlarmMin_Type = DisplayString
_TransceiverDdmInfoProfileAlarmMin_Object = MibTableColumn
transceiverDdmInfoProfileAlarmMin = _TransceiverDdmInfoProfileAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 3, 1, 4),
    _TransceiverDdmInfoProfileAlarmMin_Type()
)
transceiverDdmInfoProfileAlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transceiverDdmInfoProfileAlarmMin.setStatus("current")
_TransceiverDdmInfoProfileWarnMax_Type = DisplayString
_TransceiverDdmInfoProfileWarnMax_Object = MibTableColumn
transceiverDdmInfoProfileWarnMax = _TransceiverDdmInfoProfileWarnMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 3, 1, 5),
    _TransceiverDdmInfoProfileWarnMax_Type()
)
transceiverDdmInfoProfileWarnMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transceiverDdmInfoProfileWarnMax.setStatus("current")
_TransceiverDdmInfoProfileWarnMin_Type = DisplayString
_TransceiverDdmInfoProfileWarnMin_Object = MibTableColumn
transceiverDdmInfoProfileWarnMin = _TransceiverDdmInfoProfileWarnMin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 3, 1, 6),
    _TransceiverDdmInfoProfileWarnMin_Type()
)
transceiverDdmInfoProfileWarnMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transceiverDdmInfoProfileWarnMin.setStatus("current")
_TransceiverDdmInfoProfileDescription_Type = DisplayString
_TransceiverDdmInfoProfileDescription_Object = MibTableColumn
transceiverDdmInfoProfileDescription = _TransceiverDdmInfoProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 3, 1, 7),
    _TransceiverDdmInfoProfileDescription_Type()
)
transceiverDdmInfoProfileDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoProfileDescription.setStatus("current")
_TransceiverDdmInfoProfileRowstatus_Type = RowStatus
_TransceiverDdmInfoProfileRowstatus_Object = MibTableColumn
transceiverDdmInfoProfileRowstatus = _TransceiverDdmInfoProfileRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 3, 1, 8),
    _TransceiverDdmInfoProfileRowstatus_Type()
)
transceiverDdmInfoProfileRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    transceiverDdmInfoProfileRowstatus.setStatus("current")
_TimeSlot_Type = Integer32
_TimeSlot_Object = MibTableColumn
timeSlot = _TimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 3, 1, 9),
    _TimeSlot_Type()
)
timeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeSlot.setStatus("current")
_TransceiverPerOntTable_Object = MibTable
transceiverPerOntTable = _TransceiverPerOntTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 4)
)
if mibBuilder.loadTexts:
    transceiverPerOntTable.setStatus("current")
_TransceiverPerOntEntry_Object = MibTableRow
transceiverPerOntEntry = _TransceiverPerOntEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 4, 1)
)
transceiverPerOntEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "transceiverPerOntNumber"),
)
if mibBuilder.loadTexts:
    transceiverPerOntEntry.setStatus("current")
_TransceiverPerOntNumber_Type = Integer32
_TransceiverPerOntNumber_Object = MibTableColumn
transceiverPerOntNumber = _TransceiverPerOntNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 4, 1, 1),
    _TransceiverPerOntNumber_Type()
)
transceiverPerOntNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    transceiverPerOntNumber.setStatus("current")
_TransceiverPerOntRxPower_Type = DisplayString
_TransceiverPerOntRxPower_Object = MibTableColumn
transceiverPerOntRxPower = _TransceiverPerOntRxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 117, 4, 1, 2),
    _TransceiverPerOntRxPower_Type()
)
transceiverPerOntRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverPerOntRxPower.setStatus("current")
_Dot1agCfmSetup_ObjectIdentity = ObjectIdentity
dot1agCfmSetup = _Dot1agCfmSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 119)
)
_Dot1agCfmMIBObjects_ObjectIdentity = ObjectIdentity
dot1agCfmMIBObjects = _Dot1agCfmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 119, 1)
)
_Dot1agCfmMep_ObjectIdentity = ObjectIdentity
dot1agCfmMep = _Dot1agCfmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 119, 1, 7)
)
_Zyswdot1agCfmMepTable_Object = MibTable
zyswdot1agCfmMepTable = _Zyswdot1agCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 119, 1, 7, 1)
)
if mibBuilder.loadTexts:
    zyswdot1agCfmMepTable.setStatus("current")
_Zyswdot1agCfmMepEntry_Object = MibTableRow
zyswdot1agCfmMepEntry = _Zyswdot1agCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 119, 1, 7, 1, 1)
)
zyswdot1agCfmMepEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    zyswdot1agCfmMepEntry.setStatus("current")


class _Zyswdot1agCfmMepTransmitLbmDataTlvSize_Type(Unsigned32):
    """Custom type zyswdot1agCfmMepTransmitLbmDataTlvSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_Zyswdot1agCfmMepTransmitLbmDataTlvSize_Type.__name__ = "Unsigned32"
_Zyswdot1agCfmMepTransmitLbmDataTlvSize_Object = MibTableColumn
zyswdot1agCfmMepTransmitLbmDataTlvSize = _Zyswdot1agCfmMepTransmitLbmDataTlvSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 119, 1, 7, 1, 1, 1),
    _Zyswdot1agCfmMepTransmitLbmDataTlvSize_Type()
)
zyswdot1agCfmMepTransmitLbmDataTlvSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyswdot1agCfmMepTransmitLbmDataTlvSize.setStatus("current")
_SysMemoryPool_ObjectIdentity = ObjectIdentity
sysMemoryPool = _SysMemoryPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 124)
)
_SysMemoryPoolTable_Object = MibTable
sysMemoryPoolTable = _SysMemoryPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 124, 1)
)
if mibBuilder.loadTexts:
    sysMemoryPoolTable.setStatus("current")
_SysMemoryPoolEntry_Object = MibTableRow
sysMemoryPoolEntry = _SysMemoryPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 124, 1, 1)
)
sysMemoryPoolEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "sysMemoryPoolId"),
)
if mibBuilder.loadTexts:
    sysMemoryPoolEntry.setStatus("current")
_SysMemoryPoolId_Type = Unsigned32
_SysMemoryPoolId_Object = MibTableColumn
sysMemoryPoolId = _SysMemoryPoolId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 124, 1, 1, 1),
    _SysMemoryPoolId_Type()
)
sysMemoryPoolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemoryPoolId.setStatus("current")


class _SysMemoryPoolName_Type(OctetString):
    """Custom type sysMemoryPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysMemoryPoolName_Type.__name__ = "OctetString"
_SysMemoryPoolName_Object = MibTableColumn
sysMemoryPoolName = _SysMemoryPoolName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 124, 1, 1, 2),
    _SysMemoryPoolName_Type()
)
sysMemoryPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemoryPoolName.setStatus("current")
_SysMemoryPoolTotal_Type = Unsigned32
_SysMemoryPoolTotal_Object = MibTableColumn
sysMemoryPoolTotal = _SysMemoryPoolTotal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 124, 1, 1, 3),
    _SysMemoryPoolTotal_Type()
)
sysMemoryPoolTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemoryPoolTotal.setStatus("current")
_SysMemoryPoolUsed_Type = Unsigned32
_SysMemoryPoolUsed_Object = MibTableColumn
sysMemoryPoolUsed = _SysMemoryPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 124, 1, 1, 4),
    _SysMemoryPoolUsed_Type()
)
sysMemoryPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemoryPoolUsed.setStatus("current")


class _SysMemoryPoolUtil_Type(Unsigned32):
    """Custom type sysMemoryPoolUtil based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysMemoryPoolUtil_Type.__name__ = "Unsigned32"
_SysMemoryPoolUtil_Object = MibTableColumn
sysMemoryPoolUtil = _SysMemoryPoolUtil_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 124, 1, 1, 5),
    _SysMemoryPoolUtil_Type()
)
sysMemoryPoolUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemoryPoolUtil.setStatus("current")
_Pppoe_ObjectIdentity = ObjectIdentity
pppoe = _Pppoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125)
)
_PppoeIaSetup_ObjectIdentity = ObjectIdentity
pppoeIaSetup = _PppoeIaSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1)
)
_PppoeIaState_Type = EnabledStatus
_PppoeIaState_Object = MibScalar
pppoeIaState = _PppoeIaState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1, 1),
    _PppoeIaState_Type()
)
pppoeIaState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaState.setStatus("current")
_PppoeIaPortTable_Object = MibTable
pppoeIaPortTable = _PppoeIaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1, 7)
)
if mibBuilder.loadTexts:
    pppoeIaPortTable.setStatus("current")
_PppoeIaPortEntry_Object = MibTableRow
pppoeIaPortEntry = _PppoeIaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1, 7, 1)
)
pppoeIaPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    pppoeIaPortEntry.setStatus("current")
_PppoeIaPortEntryPort_Type = Integer32
_PppoeIaPortEntryPort_Object = MibTableColumn
pppoeIaPortEntryPort = _PppoeIaPortEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1, 7, 1, 1),
    _PppoeIaPortEntryPort_Type()
)
pppoeIaPortEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeIaPortEntryPort.setStatus("current")
_PppoeIaPortEntryTrust_Type = EnabledStatus
_PppoeIaPortEntryTrust_Object = MibTableColumn
pppoeIaPortEntryTrust = _PppoeIaPortEntryTrust_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1, 7, 1, 2),
    _PppoeIaPortEntryTrust_Type()
)
pppoeIaPortEntryTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaPortEntryTrust.setStatus("current")
_PppoeIaVlanTable_Object = MibTable
pppoeIaVlanTable = _PppoeIaVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1, 8)
)
if mibBuilder.loadTexts:
    pppoeIaVlanTable.setStatus("current")
_PppoeIaVlanEntry_Object = MibTableRow
pppoeIaVlanEntry = _PppoeIaVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1, 8, 1)
)
pppoeIaVlanEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "pppoeIaVlanEntryVid"),
)
if mibBuilder.loadTexts:
    pppoeIaVlanEntry.setStatus("current")


class _PppoeIaVlanEntryVid_Type(Integer32):
    """Custom type pppoeIaVlanEntryVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PppoeIaVlanEntryVid_Type.__name__ = "Integer32"
_PppoeIaVlanEntryVid_Object = MibTableColumn
pppoeIaVlanEntryVid = _PppoeIaVlanEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1, 8, 1, 1),
    _PppoeIaVlanEntryVid_Type()
)
pppoeIaVlanEntryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeIaVlanEntryVid.setStatus("current")
_PppoeIaVlanEntryCircuitID_Type = EnabledStatus
_PppoeIaVlanEntryCircuitID_Object = MibTableColumn
pppoeIaVlanEntryCircuitID = _PppoeIaVlanEntryCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1, 8, 1, 2),
    _PppoeIaVlanEntryCircuitID_Type()
)
pppoeIaVlanEntryCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaVlanEntryCircuitID.setStatus("current")
_PppoeIaVlanEntryRemoteID_Type = EnabledStatus
_PppoeIaVlanEntryRemoteID_Object = MibTableColumn
pppoeIaVlanEntryRemoteID = _PppoeIaVlanEntryRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1, 8, 1, 3),
    _PppoeIaVlanEntryRemoteID_Type()
)
pppoeIaVlanEntryRemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaVlanEntryRemoteID.setStatus("current")
_PppoeIaVlanEntryRowStatus_Type = RowStatus
_PppoeIaVlanEntryRowStatus_Object = MibTableColumn
pppoeIaVlanEntryRowStatus = _PppoeIaVlanEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1, 8, 1, 4),
    _PppoeIaVlanEntryRowStatus_Type()
)
pppoeIaVlanEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeIaVlanEntryRowStatus.setStatus("current")
_PppoeIaVlanOpt82Table_Object = MibTable
pppoeIaVlanOpt82Table = _PppoeIaVlanOpt82Table_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1, 10)
)
if mibBuilder.loadTexts:
    pppoeIaVlanOpt82Table.setStatus("current")
_PppoeIaVlanOpt82Entry_Object = MibTableRow
pppoeIaVlanOpt82Entry = _PppoeIaVlanOpt82Entry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1, 10, 1)
)
pppoeIaVlanOpt82Entry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "pppoeIaVlanOpt82EntryVid"),
)
if mibBuilder.loadTexts:
    pppoeIaVlanOpt82Entry.setStatus("current")


class _PppoeIaVlanOpt82EntryVid_Type(Integer32):
    """Custom type pppoeIaVlanOpt82EntryVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PppoeIaVlanOpt82EntryVid_Type.__name__ = "Integer32"
_PppoeIaVlanOpt82EntryVid_Object = MibTableColumn
pppoeIaVlanOpt82EntryVid = _PppoeIaVlanOpt82EntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1, 10, 1, 1),
    _PppoeIaVlanOpt82EntryVid_Type()
)
pppoeIaVlanOpt82EntryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeIaVlanOpt82EntryVid.setStatus("current")
_PppoeIaVlanOpt82Enable_Type = EnabledStatus
_PppoeIaVlanOpt82Enable_Object = MibTableColumn
pppoeIaVlanOpt82Enable = _PppoeIaVlanOpt82Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1, 10, 1, 2),
    _PppoeIaVlanOpt82Enable_Type()
)
pppoeIaVlanOpt82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaVlanOpt82Enable.setStatus("current")
_PppoeIaVlanOpt82EntryCircuitIDString_Type = DisplayString
_PppoeIaVlanOpt82EntryCircuitIDString_Object = MibTableColumn
pppoeIaVlanOpt82EntryCircuitIDString = _PppoeIaVlanOpt82EntryCircuitIDString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1, 10, 1, 3),
    _PppoeIaVlanOpt82EntryCircuitIDString_Type()
)
pppoeIaVlanOpt82EntryCircuitIDString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaVlanOpt82EntryCircuitIDString.setStatus("current")
_PppoeIaVlanOpt82EntryRemoteIDString_Type = DisplayString
_PppoeIaVlanOpt82EntryRemoteIDString_Object = MibTableColumn
pppoeIaVlanOpt82EntryRemoteIDString = _PppoeIaVlanOpt82EntryRemoteIDString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1, 10, 1, 4),
    _PppoeIaVlanOpt82EntryRemoteIDString_Type()
)
pppoeIaVlanOpt82EntryRemoteIDString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaVlanOpt82EntryRemoteIDString.setStatus("current")
_PppoeIaVlanOpt82EntryRowStatus_Type = RowStatus
_PppoeIaVlanOpt82EntryRowStatus_Object = MibTableColumn
pppoeIaVlanOpt82EntryRowStatus = _PppoeIaVlanOpt82EntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 1, 10, 1, 5),
    _PppoeIaVlanOpt82EntryRowStatus_Type()
)
pppoeIaVlanOpt82EntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeIaVlanOpt82EntryRowStatus.setStatus("current")
_PppoeClientTestTable_Object = MibTable
pppoeClientTestTable = _PppoeClientTestTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 2)
)
if mibBuilder.loadTexts:
    pppoeClientTestTable.setStatus("current")
_PppoeClientTestEntry_Object = MibTableRow
pppoeClientTestEntry = _PppoeClientTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 2, 1)
)
pppoeClientTestEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "pppoeClientTestEntryIndex"),
)
if mibBuilder.loadTexts:
    pppoeClientTestEntry.setStatus("current")
_PppoeClientTestEntryIndex_Type = Integer32
_PppoeClientTestEntryIndex_Object = MibTableColumn
pppoeClientTestEntryIndex = _PppoeClientTestEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 2, 1, 1),
    _PppoeClientTestEntryIndex_Type()
)
pppoeClientTestEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeClientTestEntryIndex.setStatus("current")
_PppoeClientTestEntryPort_Type = Integer32
_PppoeClientTestEntryPort_Object = MibTableColumn
pppoeClientTestEntryPort = _PppoeClientTestEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 2, 1, 2),
    _PppoeClientTestEntryPort_Type()
)
pppoeClientTestEntryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeClientTestEntryPort.setStatus("current")
_PppoeClientTestEntryOntId_Type = Integer32
_PppoeClientTestEntryOntId_Object = MibTableColumn
pppoeClientTestEntryOntId = _PppoeClientTestEntryOntId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 2, 1, 3),
    _PppoeClientTestEntryOntId_Type()
)
pppoeClientTestEntryOntId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeClientTestEntryOntId.setStatus("current")
_PppoeClientTestEntryOntCardId_Type = Integer32
_PppoeClientTestEntryOntCardId_Object = MibTableColumn
pppoeClientTestEntryOntCardId = _PppoeClientTestEntryOntCardId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 2, 1, 4),
    _PppoeClientTestEntryOntCardId_Type()
)
pppoeClientTestEntryOntCardId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeClientTestEntryOntCardId.setStatus("current")
_PppoeClientTestEntryUniport_Type = Integer32
_PppoeClientTestEntryUniport_Object = MibTableColumn
pppoeClientTestEntryUniport = _PppoeClientTestEntryUniport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 2, 1, 5),
    _PppoeClientTestEntryUniport_Type()
)
pppoeClientTestEntryUniport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeClientTestEntryUniport.setStatus("current")
_PppoeClientTestEntryUsername_Type = DisplayString
_PppoeClientTestEntryUsername_Object = MibTableColumn
pppoeClientTestEntryUsername = _PppoeClientTestEntryUsername_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 2, 1, 6),
    _PppoeClientTestEntryUsername_Type()
)
pppoeClientTestEntryUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeClientTestEntryUsername.setStatus("current")
_PppoeClientTestEntryPassword_Type = DisplayString
_PppoeClientTestEntryPassword_Object = MibTableColumn
pppoeClientTestEntryPassword = _PppoeClientTestEntryPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 2, 1, 7),
    _PppoeClientTestEntryPassword_Type()
)
pppoeClientTestEntryPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeClientTestEntryPassword.setStatus("current")


class _PppoeClientTestEntrySNISVID_Type(Integer32):
    """Custom type pppoeClientTestEntrySNISVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PppoeClientTestEntrySNISVID_Type.__name__ = "Integer32"
_PppoeClientTestEntrySNISVID_Object = MibTableColumn
pppoeClientTestEntrySNISVID = _PppoeClientTestEntrySNISVID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 2, 1, 8),
    _PppoeClientTestEntrySNISVID_Type()
)
pppoeClientTestEntrySNISVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeClientTestEntrySNISVID.setStatus("current")


class _PppoeClientTestEntrySNICVID_Type(Integer32):
    """Custom type pppoeClientTestEntrySNICVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PppoeClientTestEntrySNICVID_Type.__name__ = "Integer32"
_PppoeClientTestEntrySNICVID_Object = MibTableColumn
pppoeClientTestEntrySNICVID = _PppoeClientTestEntrySNICVID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 2, 1, 9),
    _PppoeClientTestEntrySNICVID_Type()
)
pppoeClientTestEntrySNICVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeClientTestEntrySNICVID.setStatus("current")


class _PppoeClientTestEntryNNISVID_Type(Integer32):
    """Custom type pppoeClientTestEntryNNISVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PppoeClientTestEntryNNISVID_Type.__name__ = "Integer32"
_PppoeClientTestEntryNNISVID_Object = MibTableColumn
pppoeClientTestEntryNNISVID = _PppoeClientTestEntryNNISVID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 2, 1, 10),
    _PppoeClientTestEntryNNISVID_Type()
)
pppoeClientTestEntryNNISVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeClientTestEntryNNISVID.setStatus("current")


class _PppoeClientTestEntryUNIVID_Type(Integer32):
    """Custom type pppoeClientTestEntryUNIVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PppoeClientTestEntryUNIVID_Type.__name__ = "Integer32"
_PppoeClientTestEntryUNIVID_Object = MibTableColumn
pppoeClientTestEntryUNIVID = _PppoeClientTestEntryUNIVID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 2, 1, 11),
    _PppoeClientTestEntryUNIVID_Type()
)
pppoeClientTestEntryUNIVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeClientTestEntryUNIVID.setStatus("current")
_PppoeClientTestEntrySn_Type = DisplayString
_PppoeClientTestEntrySn_Object = MibTableColumn
pppoeClientTestEntrySn = _PppoeClientTestEntrySn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 2, 1, 12),
    _PppoeClientTestEntrySn_Type()
)
pppoeClientTestEntrySn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeClientTestEntrySn.setStatus("current")


class _PppoeClientTestEntryTimeout_Type(Integer32):
    """Custom type pppoeClientTestEntryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_PppoeClientTestEntryTimeout_Type.__name__ = "Integer32"
_PppoeClientTestEntryTimeout_Object = MibTableColumn
pppoeClientTestEntryTimeout = _PppoeClientTestEntryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 2, 1, 13),
    _PppoeClientTestEntryTimeout_Type()
)
pppoeClientTestEntryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeClientTestEntryTimeout.setStatus("current")
_PppoeClientTestEntryIpaddr_Type = IpAddress
_PppoeClientTestEntryIpaddr_Object = MibTableColumn
pppoeClientTestEntryIpaddr = _PppoeClientTestEntryIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 2, 1, 14),
    _PppoeClientTestEntryIpaddr_Type()
)
pppoeClientTestEntryIpaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeClientTestEntryIpaddr.setStatus("current")


class _PppoeClientTestEntryStatus_Type(Integer32):
    """Custom type pppoeClientTestEntryStatus based on Integer32"""
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
        *(("idle", 0),
          ("onging", 1),
          ("success", 2),
          ("fail", 3),
          ("start", 4))
    )


_PppoeClientTestEntryStatus_Type.__name__ = "Integer32"
_PppoeClientTestEntryStatus_Object = MibTableColumn
pppoeClientTestEntryStatus = _PppoeClientTestEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 125, 2, 1, 15),
    _PppoeClientTestEntryStatus_Type()
)
pppoeClientTestEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeClientTestEntryStatus.setStatus("current")
_ArpLearningSetup_ObjectIdentity = ObjectIdentity
arpLearningSetup = _ArpLearningSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 126)
)
_ArpLearningPortTable_Object = MibTable
arpLearningPortTable = _ArpLearningPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 126, 1)
)
if mibBuilder.loadTexts:
    arpLearningPortTable.setStatus("current")
_ArpLearningPortEntry_Object = MibTableRow
arpLearningPortEntry = _ArpLearningPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 126, 1, 1)
)
arpLearningPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    arpLearningPortEntry.setStatus("current")


class _ArpLearningPortMode_Type(Integer32):
    """Custom type arpLearningPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("arpReply", 0),
          ("gratuitousArp", 1),
          ("arpRequest", 2))
    )


_ArpLearningPortMode_Type.__name__ = "Integer32"
_ArpLearningPortMode_Object = MibTableColumn
arpLearningPortMode = _ArpLearningPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 126, 1, 1, 1),
    _ArpLearningPortMode_Type()
)
arpLearningPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpLearningPortMode.setStatus("current")
_StaticRouteSetup_ObjectIdentity = ObjectIdentity
staticRouteSetup = _StaticRouteSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 127)
)
_MaxNumberOfStaticRoutes_Type = Integer32
_MaxNumberOfStaticRoutes_Object = MibScalar
maxNumberOfStaticRoutes = _MaxNumberOfStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 127, 1),
    _MaxNumberOfStaticRoutes_Type()
)
maxNumberOfStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfStaticRoutes.setStatus("current")
_StaticRouteTable_Object = MibTable
staticRouteTable = _StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 127, 2)
)
if mibBuilder.loadTexts:
    staticRouteTable.setStatus("current")
_StaticRouteEntry_Object = MibTableRow
staticRouteEntry = _StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 127, 2, 1)
)
staticRouteEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "staticRouteIp"),
    (0, "ZYXEL-olt1408-MIB", "staticRouteMask"),
    (0, "ZYXEL-olt1408-MIB", "staticRouteGateway"),
)
if mibBuilder.loadTexts:
    staticRouteEntry.setStatus("current")
_StaticRouteName_Type = DisplayString
_StaticRouteName_Object = MibTableColumn
staticRouteName = _StaticRouteName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 127, 2, 1, 1),
    _StaticRouteName_Type()
)
staticRouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteName.setStatus("current")
_StaticRouteIp_Type = IpAddress
_StaticRouteIp_Object = MibTableColumn
staticRouteIp = _StaticRouteIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 127, 2, 1, 2),
    _StaticRouteIp_Type()
)
staticRouteIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticRouteIp.setStatus("current")
_StaticRouteMask_Type = IpAddress
_StaticRouteMask_Object = MibTableColumn
staticRouteMask = _StaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 127, 2, 1, 3),
    _StaticRouteMask_Type()
)
staticRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticRouteMask.setStatus("current")
_StaticRouteGateway_Type = IpAddress
_StaticRouteGateway_Object = MibTableColumn
staticRouteGateway = _StaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 127, 2, 1, 4),
    _StaticRouteGateway_Type()
)
staticRouteGateway.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticRouteGateway.setStatus("current")
_StaticRouteMetric_Type = Integer32
_StaticRouteMetric_Object = MibTableColumn
staticRouteMetric = _StaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 127, 2, 1, 5),
    _StaticRouteMetric_Type()
)
staticRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteMetric.setStatus("current")
_StaticRouteRowStatus_Type = RowStatus
_StaticRouteRowStatus_Object = MibTableColumn
staticRouteRowStatus = _StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 127, 2, 1, 6),
    _StaticRouteRowStatus_Type()
)
staticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteRowStatus.setStatus("current")
_RoutingStatus_ObjectIdentity = ObjectIdentity
routingStatus = _RoutingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 128)
)
_RoutingStatusTable_Object = MibTable
routingStatusTable = _RoutingStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 128, 1)
)
if mibBuilder.loadTexts:
    routingStatusTable.setStatus("current")
_RoutingStatusEntry_Object = MibTableRow
routingStatusEntry = _RoutingStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 128, 1, 1)
)
routingStatusEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "routingStatusDestAddress"),
    (0, "ZYXEL-olt1408-MIB", "routingStatusDestMaskbits"),
    (0, "ZYXEL-olt1408-MIB", "routingStatusGateway"),
)
if mibBuilder.loadTexts:
    routingStatusEntry.setStatus("current")
_RoutingStatusDestAddress_Type = IpAddress
_RoutingStatusDestAddress_Object = MibTableColumn
routingStatusDestAddress = _RoutingStatusDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 128, 1, 1, 1),
    _RoutingStatusDestAddress_Type()
)
routingStatusDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingStatusDestAddress.setStatus("current")
_RoutingStatusDestMaskbits_Type = Integer32
_RoutingStatusDestMaskbits_Object = MibTableColumn
routingStatusDestMaskbits = _RoutingStatusDestMaskbits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 128, 1, 1, 2),
    _RoutingStatusDestMaskbits_Type()
)
routingStatusDestMaskbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingStatusDestMaskbits.setStatus("current")
_RoutingStatusGateway_Type = IpAddress
_RoutingStatusGateway_Object = MibTableColumn
routingStatusGateway = _RoutingStatusGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 128, 1, 1, 3),
    _RoutingStatusGateway_Type()
)
routingStatusGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingStatusGateway.setStatus("current")
_RoutingStatusInterface_Type = IpAddress
_RoutingStatusInterface_Object = MibTableColumn
routingStatusInterface = _RoutingStatusInterface_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 128, 1, 1, 4),
    _RoutingStatusInterface_Type()
)
routingStatusInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingStatusInterface.setStatus("current")
_RoutingStatusMetric_Type = Integer32
_RoutingStatusMetric_Object = MibTableColumn
routingStatusMetric = _RoutingStatusMetric_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 128, 1, 1, 5),
    _RoutingStatusMetric_Type()
)
routingStatusMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingStatusMetric.setStatus("current")


class _RoutingStatusType_Type(Integer32):
    """Custom type routingStatusType based on Integer32"""
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
        *(("rip", 1),
          ("bgp", 2),
          ("ospf", 3),
          ("static", 4))
    )


_RoutingStatusType_Type.__name__ = "Integer32"
_RoutingStatusType_Object = MibTableColumn
routingStatusType = _RoutingStatusType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 128, 1, 1, 6),
    _RoutingStatusType_Type()
)
routingStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingStatusType.setStatus("current")
_ExternalAlarmSetup_ObjectIdentity = ObjectIdentity
externalAlarmSetup = _ExternalAlarmSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 129)
)
_ExternalAlarmTable_Object = MibTable
externalAlarmTable = _ExternalAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 129, 1)
)
if mibBuilder.loadTexts:
    externalAlarmTable.setStatus("current")
_ExternalAlarmEntry_Object = MibTableRow
externalAlarmEntry = _ExternalAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 129, 1, 1)
)
externalAlarmEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "externalAlarmIndex"),
)
if mibBuilder.loadTexts:
    externalAlarmEntry.setStatus("current")
_ExternalAlarmIndex_Type = Integer32
_ExternalAlarmIndex_Object = MibTableColumn
externalAlarmIndex = _ExternalAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 129, 1, 1, 1),
    _ExternalAlarmIndex_Type()
)
externalAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalAlarmIndex.setStatus("current")
_ExternalAlarmName_Type = DisplayString
_ExternalAlarmName_Object = MibTableColumn
externalAlarmName = _ExternalAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 129, 1, 1, 2),
    _ExternalAlarmName_Type()
)
externalAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAlarmName.setStatus("current")


class _ExternalAlarmStatus_Type(Integer32):
    """Custom type externalAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asserted", 1),
          ("notasserted", 2))
    )


_ExternalAlarmStatus_Type.__name__ = "Integer32"
_ExternalAlarmStatus_Object = MibTableColumn
externalAlarmStatus = _ExternalAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 129, 1, 1, 3),
    _ExternalAlarmStatus_Type()
)
externalAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalAlarmStatus.setStatus("current")
_Errdisable_ObjectIdentity = ObjectIdentity
errdisable = _Errdisable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130)
)
_Recovery_ObjectIdentity = ObjectIdentity
recovery = _Recovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 1)
)
_ErrdisableRecoverySetup_ObjectIdentity = ObjectIdentity
errdisableRecoverySetup = _ErrdisableRecoverySetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 1, 1)
)
_ErrdisableRecoveryState_Type = EnabledStatus
_ErrdisableRecoveryState_Object = MibScalar
errdisableRecoveryState = _ErrdisableRecoveryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 1, 1, 1),
    _ErrdisableRecoveryState_Type()
)
errdisableRecoveryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errdisableRecoveryState.setStatus("current")
_ErrdisableRecoveryReasonTable_Object = MibTable
errdisableRecoveryReasonTable = _ErrdisableRecoveryReasonTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 1, 1, 2)
)
if mibBuilder.loadTexts:
    errdisableRecoveryReasonTable.setStatus("current")
_ErrdisableRecoveryReasonEntry_Object = MibTableRow
errdisableRecoveryReasonEntry = _ErrdisableRecoveryReasonEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 1, 1, 2, 1)
)
errdisableRecoveryReasonEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "errdisableRecoveryReason"),
)
if mibBuilder.loadTexts:
    errdisableRecoveryReasonEntry.setStatus("current")


class _ErrdisableRecoveryReason_Type(Integer32):
    """Custom type errdisableRecoveryReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("loopguard", 0),
          ("arp", 1),
          ("bpdu", 2),
          ("igmp", 3),
          ("pppoe", 4),
          ("ftp", 5),
          ("icmp", 6))
    )


_ErrdisableRecoveryReason_Type.__name__ = "Integer32"
_ErrdisableRecoveryReason_Object = MibTableColumn
errdisableRecoveryReason = _ErrdisableRecoveryReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 1, 1, 2, 1, 1),
    _ErrdisableRecoveryReason_Type()
)
errdisableRecoveryReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errdisableRecoveryReason.setStatus("current")


class _ErrdisableRecoveryReasonActive_Type(Integer32):
    """Custom type errdisableRecoveryReasonActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ErrdisableRecoveryReasonActive_Type.__name__ = "Integer32"
_ErrdisableRecoveryReasonActive_Object = MibTableColumn
errdisableRecoveryReasonActive = _ErrdisableRecoveryReasonActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 1, 1, 2, 1, 2),
    _ErrdisableRecoveryReasonActive_Type()
)
errdisableRecoveryReasonActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errdisableRecoveryReasonActive.setStatus("current")


class _ErrdisableRecoveryReasonInterval_Type(Integer32):
    """Custom type errdisableRecoveryReasonInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 2592000),
    )


_ErrdisableRecoveryReasonInterval_Type.__name__ = "Integer32"
_ErrdisableRecoveryReasonInterval_Object = MibTableColumn
errdisableRecoveryReasonInterval = _ErrdisableRecoveryReasonInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 1, 1, 2, 1, 3),
    _ErrdisableRecoveryReasonInterval_Type()
)
errdisableRecoveryReasonInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errdisableRecoveryReasonInterval.setStatus("current")
_ErrdisableRecoveryIfStatusTable_Object = MibTable
errdisableRecoveryIfStatusTable = _ErrdisableRecoveryIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 1, 1, 3)
)
if mibBuilder.loadTexts:
    errdisableRecoveryIfStatusTable.setStatus("current")
_ErrdisableRecoveryIfStatusEntry_Object = MibTableRow
errdisableRecoveryIfStatusEntry = _ErrdisableRecoveryIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 1, 1, 3, 1)
)
errdisableRecoveryIfStatusEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "errdisableRecoveryIfStatusReason"),
    (0, "ZYXEL-olt1408-MIB", "errdisableRecoveryIfStatusPort"),
)
if mibBuilder.loadTexts:
    errdisableRecoveryIfStatusEntry.setStatus("current")


class _ErrdisableRecoveryIfStatusReason_Type(Integer32):
    """Custom type errdisableRecoveryIfStatusReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("loopguard", 0),
          ("arp", 1),
          ("bpdu", 2),
          ("igmp", 3),
          ("pppoe", 4),
          ("ftp", 5),
          ("icmp", 6))
    )


_ErrdisableRecoveryIfStatusReason_Type.__name__ = "Integer32"
_ErrdisableRecoveryIfStatusReason_Object = MibTableColumn
errdisableRecoveryIfStatusReason = _ErrdisableRecoveryIfStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 1, 1, 3, 1, 1),
    _ErrdisableRecoveryIfStatusReason_Type()
)
errdisableRecoveryIfStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errdisableRecoveryIfStatusReason.setStatus("current")
_ErrdisableRecoveryIfStatusPort_Type = Integer32
_ErrdisableRecoveryIfStatusPort_Object = MibTableColumn
errdisableRecoveryIfStatusPort = _ErrdisableRecoveryIfStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 1, 1, 3, 1, 2),
    _ErrdisableRecoveryIfStatusPort_Type()
)
errdisableRecoveryIfStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errdisableRecoveryIfStatusPort.setStatus("current")


class _ErrdisableRecoveryIfStatusTimeToRecover_Type(Integer32):
    """Custom type errdisableRecoveryIfStatusTimeToRecover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 2592000),
    )


_ErrdisableRecoveryIfStatusTimeToRecover_Type.__name__ = "Integer32"
_ErrdisableRecoveryIfStatusTimeToRecover_Object = MibTableColumn
errdisableRecoveryIfStatusTimeToRecover = _ErrdisableRecoveryIfStatusTimeToRecover_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 1, 1, 3, 1, 3),
    _ErrdisableRecoveryIfStatusTimeToRecover_Type()
)
errdisableRecoveryIfStatusTimeToRecover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errdisableRecoveryIfStatusTimeToRecover.setStatus("current")
_Detect_ObjectIdentity = ObjectIdentity
detect = _Detect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 2)
)
_ErrdisableDetectReasonTable_Object = MibTable
errdisableDetectReasonTable = _ErrdisableDetectReasonTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 2, 1)
)
if mibBuilder.loadTexts:
    errdisableDetectReasonTable.setStatus("current")
_ErrdisableDetectReasonEntry_Object = MibTableRow
errdisableDetectReasonEntry = _ErrdisableDetectReasonEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 2, 1, 1)
)
errdisableDetectReasonEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "errdisableDetectReason"),
)
if mibBuilder.loadTexts:
    errdisableDetectReasonEntry.setStatus("current")


class _ErrdisableDetectReason_Type(Integer32):
    """Custom type errdisableDetectReason based on Integer32"""
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
        *(("arp", 1),
          ("bpdu", 2),
          ("igmp", 3),
          ("pppoe", 4),
          ("ftp", 5),
          ("icmp", 6))
    )


_ErrdisableDetectReason_Type.__name__ = "Integer32"
_ErrdisableDetectReason_Object = MibTableColumn
errdisableDetectReason = _ErrdisableDetectReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 2, 1, 1, 1),
    _ErrdisableDetectReason_Type()
)
errdisableDetectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errdisableDetectReason.setStatus("current")
_ErrdisableDetectReasonEnable_Type = EnabledStatus
_ErrdisableDetectReasonEnable_Object = MibTableColumn
errdisableDetectReasonEnable = _ErrdisableDetectReasonEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 2, 1, 1, 2),
    _ErrdisableDetectReasonEnable_Type()
)
errdisableDetectReasonEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errdisableDetectReasonEnable.setStatus("current")


class _ErrdisableDetectReasonMode_Type(Integer32):
    """Custom type errdisableDetectReasonMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactivePort", 1),
          ("inactiveReason", 2),
          ("rateLimitation", 3))
    )


_ErrdisableDetectReasonMode_Type.__name__ = "Integer32"
_ErrdisableDetectReasonMode_Object = MibTableColumn
errdisableDetectReasonMode = _ErrdisableDetectReasonMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 2, 1, 1, 3),
    _ErrdisableDetectReasonMode_Type()
)
errdisableDetectReasonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errdisableDetectReasonMode.setStatus("current")
_ErrdisableTrapInfoObject_ObjectIdentity = ObjectIdentity
errdisableTrapInfoObject = _ErrdisableTrapInfoObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 3)
)
_ErrdisableTrapPort_Type = Integer32
_ErrdisableTrapPort_Object = MibScalar
errdisableTrapPort = _ErrdisableTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 3, 1),
    _ErrdisableTrapPort_Type()
)
errdisableTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errdisableTrapPort.setStatus("current")


class _ErrdisableTrapReason_Type(Integer32):
    """Custom type errdisableTrapReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("loopguard", 0),
          ("arp", 1),
          ("bpdu", 2),
          ("igmp", 3),
          ("pppoe", 4),
          ("ftp", 5),
          ("icmp", 6))
    )


_ErrdisableTrapReason_Type.__name__ = "Integer32"
_ErrdisableTrapReason_Object = MibScalar
errdisableTrapReason = _ErrdisableTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 3, 2),
    _ErrdisableTrapReason_Type()
)
errdisableTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errdisableTrapReason.setStatus("current")


class _ErrdisableTrapMode_Type(Integer32):
    """Custom type errdisableTrapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactivePort", 0),
          ("inactiveReason", 1),
          ("rateLimitation", 2))
    )


_ErrdisableTrapMode_Type.__name__ = "Integer32"
_ErrdisableTrapMode_Object = MibScalar
errdisableTrapMode = _ErrdisableTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 3, 3),
    _ErrdisableTrapMode_Type()
)
errdisableTrapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errdisableTrapMode.setStatus("current")
_ErrdisableTrapNotifications_ObjectIdentity = ObjectIdentity
errdisableTrapNotifications = _ErrdisableTrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 4)
)
_CpuProtectionSetup_ObjectIdentity = ObjectIdentity
cpuProtectionSetup = _CpuProtectionSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 131)
)
_CpuProtectionTable_Object = MibTable
cpuProtectionTable = _CpuProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 131, 1)
)
if mibBuilder.loadTexts:
    cpuProtectionTable.setStatus("current")
_CpuProtectionEntry_Object = MibTableRow
cpuProtectionEntry = _CpuProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 131, 1, 1)
)
cpuProtectionEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "cpuProtectionPort"),
    (0, "ZYXEL-olt1408-MIB", "cpuProtectionReason"),
)
if mibBuilder.loadTexts:
    cpuProtectionEntry.setStatus("current")
_CpuProtectionPort_Type = Integer32
_CpuProtectionPort_Object = MibTableColumn
cpuProtectionPort = _CpuProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 131, 1, 1, 1),
    _CpuProtectionPort_Type()
)
cpuProtectionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuProtectionPort.setStatus("current")


class _CpuProtectionReason_Type(Integer32):
    """Custom type cpuProtectionReason based on Integer32"""
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
        *(("arp", 1),
          ("bpdu", 2),
          ("igmp", 3),
          ("pppoe", 4),
          ("ftp", 5),
          ("icmp", 6))
    )


_CpuProtectionReason_Type.__name__ = "Integer32"
_CpuProtectionReason_Object = MibTableColumn
cpuProtectionReason = _CpuProtectionReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 131, 1, 1, 2),
    _CpuProtectionReason_Type()
)
cpuProtectionReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuProtectionReason.setStatus("current")


class _CpuProtectionRateLimitSet_Type(Integer32):
    """Custom type cpuProtectionRateLimitSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CpuProtectionRateLimitSet_Type.__name__ = "Integer32"
_CpuProtectionRateLimitSet_Object = MibTableColumn
cpuProtectionRateLimitSet = _CpuProtectionRateLimitSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 131, 1, 1, 3),
    _CpuProtectionRateLimitSet_Type()
)
cpuProtectionRateLimitSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuProtectionRateLimitSet.setStatus("current")
_RemoteOnt_ObjectIdentity = ObjectIdentity
remoteOnt = _RemoteOnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135)
)
_OntSetup_ObjectIdentity = ObjectIdentity
ontSetup = _OntSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1)
)
_OntTable_Object = MibTable
ontTable = _OntTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1)
)
if mibBuilder.loadTexts:
    ontTable.setStatus("current")
_OntEntry_Object = MibTableRow
ontEntry = _OntEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1)
)
ontEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
)
if mibBuilder.loadTexts:
    ontEntry.setStatus("current")
_OntNumber_Type = Integer32
_OntNumber_Object = MibTableColumn
ontNumber = _OntNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 1),
    _OntNumber_Type()
)
ontNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ontNumber.setStatus("current")
_Password_Type = DisplayString
_Password_Object = MibTableColumn
password = _Password_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 4),
    _Password_Type()
)
password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    password.setStatus("current")
_PlanVersion_Type = DisplayString
_PlanVersion_Object = MibTableColumn
planVersion = _PlanVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 5),
    _PlanVersion_Type()
)
planVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    planVersion.setStatus("current")
_Sn_Type = DisplayString
_Sn_Object = MibTableColumn
sn = _Sn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 6),
    _Sn_Type()
)
sn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sn.setStatus("current")
_LoopbackConfig_Type = EnabledStatus
_LoopbackConfig_Object = MibTableColumn
loopbackConfig = _LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 7),
    _LoopbackConfig_Type()
)
loopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbackConfig.setStatus("current")


class _LoopbackStatus_Type(Integer32):
    """Custom type loopbackStatus based on Integer32"""
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
          ("underTesting", 1),
          ("success", 2),
          ("fail", 3))
    )


_LoopbackStatus_Type.__name__ = "Integer32"
_LoopbackStatus_Object = MibTableColumn
loopbackStatus = _LoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 8),
    _LoopbackStatus_Type()
)
loopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopbackStatus.setStatus("current")


class _Model_Type(Integer32):
    """Custom type model based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("pmg1006ORpmg2006ORpmg1005ORpmg2005", 1),
          ("pmg5318b20a", 2),
          ("pmg3000b20a", 3),
          ("na1", 4),
          ("gpt2542gnaucORpmg5318b20bORpmg5318b20cORpmg5317ORpmg5323", 5),
          ("o00xx0vpq", 6),
          ("na2", 7),
          ("gpt2820gnORgpt2840gnORgpt2841hntORgpt2840hnt", 8))
    )


_Model_Type.__name__ = "Integer32"
_Model_Object = MibTableColumn
model = _Model_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 9),
    _Model_Type()
)
model.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    model.setStatus("current")
_OntRowStatus_Type = RowStatus
_OntRowStatus_Object = MibTableColumn
ontRowStatus = _OntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 10),
    _OntRowStatus_Type()
)
ontRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ontRowStatus.setStatus("current")


class _OntAction_Type(Integer32):
    """Custom type ontAction based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("rebootOnt", 1),
          ("checkUpgardeFW", 2),
          ("upgradingFW", 3),
          ("delAllConfig", 4),
          ("downloadFile", 5),
          ("uploadFile", 6),
          ("switchImageRule", 7),
          ("clearUpgradeStatus", 8),
          ("clearWaitingQueue", 9))
    )


_OntAction_Type.__name__ = "Integer32"
_OntAction_Object = MibTableColumn
ontAction = _OntAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 11),
    _OntAction_Type()
)
ontAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAction.setStatus("current")
_AlarmProfile_Type = DisplayString
_AlarmProfile_Object = MibTableColumn
alarmProfile = _AlarmProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 12),
    _AlarmProfile_Type()
)
alarmProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmProfile.setStatus("current")


class _FullBridg_Type(Integer32):
    """Custom type fullBridg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FullBridg_Type.__name__ = "Integer32"
_FullBridg_Object = MibTableColumn
fullBridg = _FullBridg_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 13),
    _FullBridg_Type()
)
fullBridg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fullBridg.setStatus("current")


class _AntiMacSpoofing_Type(Integer32):
    """Custom type antiMacSpoofing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AntiMacSpoofing_Type.__name__ = "Integer32"
_AntiMacSpoofing_Object = MibTableColumn
antiMacSpoofing = _AntiMacSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 14),
    _AntiMacSpoofing_Type()
)
antiMacSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    antiMacSpoofing.setStatus("current")
_Description_Type = DisplayString
_Description_Object = MibTableColumn
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 15),
    _Description_Type()
)
description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    description.setStatus("current")
_Option82CircuitIdOptInfo_Type = DisplayString
_Option82CircuitIdOptInfo_Object = MibTableColumn
option82CircuitIdOptInfo = _Option82CircuitIdOptInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 16),
    _Option82CircuitIdOptInfo_Type()
)
option82CircuitIdOptInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    option82CircuitIdOptInfo.setStatus("current")
_Option82RemoteIdOptInfo_Type = DisplayString
_Option82RemoteIdOptInfo_Object = MibTableColumn
option82RemoteIdOptInfo = _Option82RemoteIdOptInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 17),
    _Option82RemoteIdOptInfo_Type()
)
option82RemoteIdOptInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    option82RemoteIdOptInfo.setStatus("current")
_TemplateDescription_Type = DisplayString
_TemplateDescription_Object = MibTableColumn
templateDescription = _TemplateDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 18),
    _TemplateDescription_Type()
)
templateDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    templateDescription.setStatus("current")
_UsFecMode_Type = EnabledStatus
_UsFecMode_Object = MibTableColumn
usFecMode = _UsFecMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 19),
    _UsFecMode_Type()
)
usFecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usFecMode.setStatus("current")


class _Option82DisableDhcp_Type(Integer32):
    """Custom type option82DisableDhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Option82DisableDhcp_Type.__name__ = "Integer32"
_Option82DisableDhcp_Object = MibTableColumn
option82DisableDhcp = _Option82DisableDhcp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 20),
    _Option82DisableDhcp_Type()
)
option82DisableDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    option82DisableDhcp.setStatus("current")


class _Option82PassThroughDhcp_Type(Integer32):
    """Custom type option82PassThroughDhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Option82PassThroughDhcp_Type.__name__ = "Integer32"
_Option82PassThroughDhcp_Object = MibTableColumn
option82PassThroughDhcp = _Option82PassThroughDhcp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 21),
    _Option82PassThroughDhcp_Type()
)
option82PassThroughDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    option82PassThroughDhcp.setStatus("current")


class _Option82DisablePppoe_Type(Integer32):
    """Custom type option82DisablePppoe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Option82DisablePppoe_Type.__name__ = "Integer32"
_Option82DisablePppoe_Object = MibTableColumn
option82DisablePppoe = _Option82DisablePppoe_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 22),
    _Option82DisablePppoe_Type()
)
option82DisablePppoe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    option82DisablePppoe.setStatus("current")


class _Option82PassThroughPppoe_Type(Integer32):
    """Custom type option82PassThroughPppoe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Option82PassThroughPppoe_Type.__name__ = "Integer32"
_Option82PassThroughPppoe_Object = MibTableColumn
option82PassThroughPppoe = _Option82PassThroughPppoe_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 1, 1, 23),
    _Option82PassThroughPppoe_Type()
)
option82PassThroughPppoe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    option82PassThroughPppoe.setStatus("current")
_OntBwGroupTable_Object = MibTable
ontBwGroupTable = _OntBwGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 2)
)
if mibBuilder.loadTexts:
    ontBwGroupTable.setStatus("current")
_OntBwGroupEntry_Object = MibTableRow
ontBwGroupEntry = _OntBwGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 2, 1)
)
ontBwGroupEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontBwGroupId"),
)
if mibBuilder.loadTexts:
    ontBwGroupEntry.setStatus("current")


class _OntBwGroupId_Type(Integer32):
    """Custom type ontBwGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_OntBwGroupId_Type.__name__ = "Integer32"
_OntBwGroupId_Object = MibTableColumn
ontBwGroupId = _OntBwGroupId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 2, 1, 1),
    _OntBwGroupId_Type()
)
ontBwGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ontBwGroupId.setStatus("current")


class _OntBwGroupUstype_Type(Integer32):
    """Custom type ontBwGroupUstype based on Integer32"""
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
        *(("type1", 1),
          ("type2", 2),
          ("type3", 3),
          ("type4", 4),
          ("type5", 5))
    )


_OntBwGroupUstype_Type.__name__ = "Integer32"
_OntBwGroupUstype_Object = MibTableColumn
ontBwGroupUstype = _OntBwGroupUstype_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 2, 1, 2),
    _OntBwGroupUstype_Type()
)
ontBwGroupUstype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontBwGroupUstype.setStatus("current")
_OntBwGroupUsbwprofname_Type = DisplayString
_OntBwGroupUsbwprofname_Object = MibTableColumn
ontBwGroupUsbwprofname = _OntBwGroupUsbwprofname_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 2, 1, 3),
    _OntBwGroupUsbwprofname_Type()
)
ontBwGroupUsbwprofname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontBwGroupUsbwprofname.setStatus("current")
_OntBwGroupDsbwprofname_Type = DisplayString
_OntBwGroupDsbwprofname_Object = MibTableColumn
ontBwGroupDsbwprofname = _OntBwGroupDsbwprofname_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 2, 1, 4),
    _OntBwGroupDsbwprofname_Type()
)
ontBwGroupDsbwprofname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontBwGroupDsbwprofname.setStatus("current")
_OntBwGroupRowStatus_Type = RowStatus
_OntBwGroupRowStatus_Object = MibTableColumn
ontBwGroupRowStatus = _OntBwGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 2, 1, 5),
    _OntBwGroupRowStatus_Type()
)
ontBwGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ontBwGroupRowStatus.setStatus("current")
_OntFileTransferParamTable_Object = MibTable
ontFileTransferParamTable = _OntFileTransferParamTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 3)
)
if mibBuilder.loadTexts:
    ontFileTransferParamTable.setStatus("current")
_OntFileTransferParamEntry_Object = MibTableRow
ontFileTransferParamEntry = _OntFileTransferParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 3, 1)
)
ontFileTransferParamEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
)
if mibBuilder.loadTexts:
    ontFileTransferParamEntry.setStatus("current")
_OntFileTransferFileUri_Type = OctetString
_OntFileTransferFileUri_Object = MibTableColumn
ontFileTransferFileUri = _OntFileTransferFileUri_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 3, 1, 1),
    _OntFileTransferFileUri_Type()
)
ontFileTransferFileUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontFileTransferFileUri.setStatus("current")
_OntFileTransferLocalFileName_Type = OctetString
_OntFileTransferLocalFileName_Object = MibTableColumn
ontFileTransferLocalFileName = _OntFileTransferLocalFileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 3, 1, 2),
    _OntFileTransferLocalFileName_Type()
)
ontFileTransferLocalFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontFileTransferLocalFileName.setStatus("current")
_OntFileTransferUserName_Type = OctetString
_OntFileTransferUserName_Object = MibTableColumn
ontFileTransferUserName = _OntFileTransferUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 3, 1, 3),
    _OntFileTransferUserName_Type()
)
ontFileTransferUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontFileTransferUserName.setStatus("current")
_OntFileTransferPassword_Type = OctetString
_OntFileTransferPassword_Object = MibTableColumn
ontFileTransferPassword = _OntFileTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 3, 1, 4),
    _OntFileTransferPassword_Type()
)
ontFileTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontFileTransferPassword.setStatus("current")
_OntWanConfigTable_Object = MibTable
ontWanConfigTable = _OntWanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 4)
)
if mibBuilder.loadTexts:
    ontWanConfigTable.setStatus("current")
_OntWanConfigEntry_Object = MibTableRow
ontWanConfigEntry = _OntWanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 4, 1)
)
ontWanConfigEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontWanConfigId"),
)
if mibBuilder.loadTexts:
    ontWanConfigEntry.setStatus("current")


class _OntWanConfigId_Type(Integer32):
    """Custom type ontWanConfigId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_OntWanConfigId_Type.__name__ = "Integer32"
_OntWanConfigId_Object = MibTableColumn
ontWanConfigId = _OntWanConfigId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 4, 1, 1),
    _OntWanConfigId_Type()
)
ontWanConfigId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ontWanConfigId.setStatus("current")
_OntWanConfigVlan_Type = Integer32
_OntWanConfigVlan_Object = MibTableColumn
ontWanConfigVlan = _OntWanConfigVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 4, 1, 2),
    _OntWanConfigVlan_Type()
)
ontWanConfigVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontWanConfigVlan.setStatus("current")
_OntWanConfigPriority_Type = Integer32
_OntWanConfigPriority_Object = MibTableColumn
ontWanConfigPriority = _OntWanConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 4, 1, 3),
    _OntWanConfigPriority_Type()
)
ontWanConfigPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontWanConfigPriority.setStatus("current")


class _OntWanConfigNat_Type(Integer32):
    """Custom type ontWanConfigNat based on Integer32"""
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


_OntWanConfigNat_Type.__name__ = "Integer32"
_OntWanConfigNat_Object = MibTableColumn
ontWanConfigNat = _OntWanConfigNat_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 4, 1, 4),
    _OntWanConfigNat_Type()
)
ontWanConfigNat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontWanConfigNat.setStatus("current")
_OntWanConfigUsername_Type = DisplayString
_OntWanConfigUsername_Object = MibTableColumn
ontWanConfigUsername = _OntWanConfigUsername_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 4, 1, 5),
    _OntWanConfigUsername_Type()
)
ontWanConfigUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontWanConfigUsername.setStatus("current")
_OntWanConfigPassword_Type = DisplayString
_OntWanConfigPassword_Object = MibTableColumn
ontWanConfigPassword = _OntWanConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 4, 1, 6),
    _OntWanConfigPassword_Type()
)
ontWanConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontWanConfigPassword.setStatus("current")
_OntWanConfigRowStatus_Type = RowStatus
_OntWanConfigRowStatus_Object = MibTableColumn
ontWanConfigRowStatus = _OntWanConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 4, 1, 7),
    _OntWanConfigRowStatus_Type()
)
ontWanConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ontWanConfigRowStatus.setStatus("current")
_OntResetTable_Object = MibTable
ontResetTable = _OntResetTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 5)
)
if mibBuilder.loadTexts:
    ontResetTable.setStatus("current")
_OntResetEntry_Object = MibTableRow
ontResetEntry = _OntResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 5, 1)
)
ontResetEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
)
if mibBuilder.loadTexts:
    ontResetEntry.setStatus("current")


class _OntResetAction_Type(Integer32):
    """Custom type ontResetAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_OntResetAction_Type.__name__ = "Integer32"
_OntResetAction_Object = MibTableColumn
ontResetAction = _OntResetAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 5, 1, 1),
    _OntResetAction_Type()
)
ontResetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontResetAction.setStatus("current")
_OntConfgurationStatus_Type = Integer32
_OntConfgurationStatus_Object = MibTableColumn
ontConfgurationStatus = _OntConfgurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 5, 1, 2),
    _OntConfgurationStatus_Type()
)
ontConfgurationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontConfgurationStatus.setStatus("current")
_OntTimeOfRestore_Type = Integer32
_OntTimeOfRestore_Object = MibTableColumn
ontTimeOfRestore = _OntTimeOfRestore_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 5, 1, 3),
    _OntTimeOfRestore_Type()
)
ontTimeOfRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontTimeOfRestore.setStatus("current")
_OntStormingTable_Object = MibTable
ontStormingTable = _OntStormingTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 6)
)
if mibBuilder.loadTexts:
    ontStormingTable.setStatus("current")
_OntStormingEntry_Object = MibTableRow
ontStormingEntry = _OntStormingEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 6, 1)
)
ontStormingEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
)
if mibBuilder.loadTexts:
    ontStormingEntry.setStatus("current")
_OntStormingThreshold_Type = Integer32
_OntStormingThreshold_Object = MibTableColumn
ontStormingThreshold = _OntStormingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 6, 1, 1),
    _OntStormingThreshold_Type()
)
ontStormingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontStormingThreshold.setStatus("current")


class _OntStormingLoopGuard_Type(Integer32):
    """Custom type ontStormingLoopGuard based on Integer32"""
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


_OntStormingLoopGuard_Type.__name__ = "Integer32"
_OntStormingLoopGuard_Object = MibTableColumn
ontStormingLoopGuard = _OntStormingLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 6, 1, 2),
    _OntStormingLoopGuard_Type()
)
ontStormingLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontStormingLoopGuard.setStatus("current")
_OntAclServiceTable_Object = MibTable
ontAclServiceTable = _OntAclServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 7)
)
if mibBuilder.loadTexts:
    ontAclServiceTable.setStatus("current")
_OntAclServiceEntry_Object = MibTableRow
ontAclServiceEntry = _OntAclServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 7, 1)
)
ontAclServiceEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontAclRuleId"),
)
if mibBuilder.loadTexts:
    ontAclServiceEntry.setStatus("current")


class _OntAclRuleId_Type(Integer32):
    """Custom type ontAclRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_OntAclRuleId_Type.__name__ = "Integer32"
_OntAclRuleId_Object = MibTableColumn
ontAclRuleId = _OntAclRuleId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 7, 1, 1),
    _OntAclRuleId_Type()
)
ontAclRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ontAclRuleId.setStatus("current")
_OntAclProfName_Type = DisplayString
_OntAclProfName_Object = MibTableColumn
ontAclProfName = _OntAclProfName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 7, 1, 2),
    _OntAclProfName_Type()
)
ontAclProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAclProfName.setStatus("current")
_OntAclServiceRowStatus_Type = RowStatus
_OntAclServiceRowStatus_Object = MibTableColumn
ontAclServiceRowStatus = _OntAclServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 1, 7, 1, 3),
    _OntAclServiceRowStatus_Type()
)
ontAclServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ontAclServiceRowStatus.setStatus("current")
_OntcardTable_Object = MibTable
ontcardTable = _OntcardTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 2)
)
if mibBuilder.loadTexts:
    ontcardTable.setStatus("current")
_OntcardEntry_Object = MibTableRow
ontcardEntry = _OntcardEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 2, 1)
)
ontcardEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
)
if mibBuilder.loadTexts:
    ontcardEntry.setStatus("current")
_Ontcard_Type = Integer32
_Ontcard_Object = MibTableColumn
ontcard = _Ontcard_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 2, 1, 1),
    _Ontcard_Type()
)
ontcard.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ontcard.setStatus("current")


class _OntcardType_Type(Integer32):
    """Custom type ontcardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(24,
              32,
              35,
              38,
              47,
              48,
              49)
        )
    )
    namedValues = NamedValues(
        *(("speed10or100BaseT", 24),
          ("pots", 32),
          ("vdsl2", 35),
          ("video", 38),
          ("speed10or100or1000BaseT", 47),
          ("veip", 48),
          ("etherOrVeip", 49))
    )


_OntcardType_Type.__name__ = "Integer32"
_OntcardType_Object = MibTableColumn
ontcardType = _OntcardType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 2, 1, 2),
    _OntcardType_Type()
)
ontcardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontcardType.setStatus("current")
_Numofport_Type = Integer32
_Numofport_Object = MibTableColumn
numofport = _Numofport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 2, 1, 3),
    _Numofport_Type()
)
numofport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numofport.setStatus("current")
_OntcardRowStatus_Type = RowStatus
_OntcardRowStatus_Object = MibTableColumn
ontcardRowStatus = _OntcardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 2, 1, 4),
    _OntcardRowStatus_Type()
)
ontcardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ontcardRowStatus.setStatus("current")


class _OntcardAction_Type(Integer32):
    """Custom type ontcardAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("delAllConfig", 1))
    )


_OntcardAction_Type.__name__ = "Integer32"
_OntcardAction_Object = MibTableColumn
ontcardAction = _OntcardAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 2, 1, 5),
    _OntcardAction_Type()
)
ontcardAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontcardAction.setStatus("current")
_OntenetTable_Object = MibTable
ontenetTable = _OntenetTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 3)
)
if mibBuilder.loadTexts:
    ontenetTable.setStatus("current")
_OntenetEntry_Object = MibTableRow
ontenetEntry = _OntenetEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 3, 1)
)
ontenetEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "ontenetCardPort"),
)
if mibBuilder.loadTexts:
    ontenetEntry.setStatus("current")
_OntenetCardPort_Type = Integer32
_OntenetCardPort_Object = MibTableColumn
ontenetCardPort = _OntenetCardPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 3, 1, 1),
    _OntenetCardPort_Type()
)
ontenetCardPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ontenetCardPort.setStatus("current")


class _PmenetEnable_Type(Integer32):
    """Custom type pmenetEnable based on Integer32"""
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
        *(("disable", 0),
          ("baseOnModelID", 1),
          ("bit64", 2),
          ("bit32", 3))
    )


_PmenetEnable_Type.__name__ = "Integer32"
_PmenetEnable_Object = MibTableColumn
pmenetEnable = _PmenetEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 3, 1, 2),
    _PmenetEnable_Type()
)
pmenetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmenetEnable.setStatus("current")


class _PortSpeed_Type(Integer32):
    """Custom type portSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("speed2500Full", 2),
          ("speed1000Full", 3),
          ("speed100Full", 5),
          ("speed10Full", 7))
    )


_PortSpeed_Type.__name__ = "Integer32"
_PortSpeed_Object = MibTableColumn
portSpeed = _PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 3, 1, 3),
    _PortSpeed_Type()
)
portSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpeed.setStatus("current")
_OntenetRowStatus_Type = RowStatus
_OntenetRowStatus_Object = MibTableColumn
ontenetRowStatus = _OntenetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 3, 1, 4),
    _OntenetRowStatus_Type()
)
ontenetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ontenetRowStatus.setStatus("current")


class _OntenetAction_Type(Integer32):
    """Custom type ontenetAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("delAllConfig", 1))
    )


_OntenetAction_Type.__name__ = "Integer32"
_OntenetAction_Object = MibTableColumn
ontenetAction = _OntenetAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 3, 1, 5),
    _OntenetAction_Type()
)
ontenetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontenetAction.setStatus("current")
_OntvdslTable_Object = MibTable
ontvdslTable = _OntvdslTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 4)
)
if mibBuilder.loadTexts:
    ontvdslTable.setStatus("current")
_OntvdslEntry_Object = MibTableRow
ontvdslEntry = _OntvdslEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 4, 1)
)
ontvdslEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "ontvdslCardPort"),
)
if mibBuilder.loadTexts:
    ontvdslEntry.setStatus("current")
_OntvdslCardPort_Type = Integer32
_OntvdslCardPort_Object = MibTableColumn
ontvdslCardPort = _OntvdslCardPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 4, 1, 1),
    _OntvdslCardPort_Type()
)
ontvdslCardPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ontvdslCardPort.setStatus("current")
_LineTemplate_Type = DisplayString
_LineTemplate_Object = MibTableColumn
lineTemplate = _LineTemplate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 4, 1, 2),
    _LineTemplate_Type()
)
lineTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineTemplate.setStatus("current")
_OntvdslRowStatus_Type = RowStatus
_OntvdslRowStatus_Object = MibTableColumn
ontvdslRowStatus = _OntvdslRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 4, 1, 3),
    _OntvdslRowStatus_Type()
)
ontvdslRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ontvdslRowStatus.setStatus("current")


class _OntvdslAction_Type(Integer32):
    """Custom type ontvdslAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("delAllConfig", 1))
    )


_OntvdslAction_Type.__name__ = "Integer32"
_OntvdslAction_Object = MibTableColumn
ontvdslAction = _OntvdslAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 4, 1, 4),
    _OntvdslAction_Type()
)
ontvdslAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontvdslAction.setStatus("current")
_OntuniportSetup_ObjectIdentity = ObjectIdentity
ontuniportSetup = _OntuniportSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5)
)
_OntuniportTable_Object = MibTable
ontuniportTable = _OntuniportTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 1)
)
if mibBuilder.loadTexts:
    ontuniportTable.setStatus("current")
_OntuniportEntry_Object = MibTableRow
ontuniportEntry = _OntuniportEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 1, 1)
)
ontuniportEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "uniPort"),
)
if mibBuilder.loadTexts:
    ontuniportEntry.setStatus("current")
_UniPort_Type = Integer32
_UniPort_Object = MibTableColumn
uniPort = _UniPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 1, 1, 1),
    _UniPort_Type()
)
uniPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniPort.setStatus("current")
_UniPortRowStatus_Type = RowStatus
_UniPortRowStatus_Object = MibTableColumn
uniPortRowStatus = _UniPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 1, 1, 2),
    _UniPortRowStatus_Type()
)
uniPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniPortRowStatus.setStatus("current")


class _UniPortAction_Type(Integer32):
    """Custom type uniPortAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("delAllConfig", 1))
    )


_UniPortAction_Type.__name__ = "Integer32"
_UniPortAction_Object = MibTableColumn
uniPortAction = _UniPortAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 1, 1, 3),
    _UniPortAction_Type()
)
uniPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortAction.setStatus("current")


class _UniportMacLimit_Type(Integer32):
    """Custom type uniportMacLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("inactive", 0)
    )


_UniportMacLimit_Type.__name__ = "Integer32"
_UniportMacLimit_Object = MibTableColumn
uniportMacLimit = _UniportMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 1, 1, 4),
    _UniportMacLimit_Type()
)
uniportMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportMacLimit.setStatus("current")
_UniportIgmpchannelTable_Object = MibTable
uniportIgmpchannelTable = _UniportIgmpchannelTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 2)
)
if mibBuilder.loadTexts:
    uniportIgmpchannelTable.setStatus("current")
_UniportIgmpchannelEntry_Object = MibTableRow
uniportIgmpchannelEntry = _UniportIgmpchannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 2, 1)
)
uniportIgmpchannelEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "uniPort"),
    (0, "ZYXEL-olt1408-MIB", "uniportIgmpchannelUniSvid"),
    (0, "ZYXEL-olt1408-MIB", "uniportIgmpchannelUniCvid"),
)
if mibBuilder.loadTexts:
    uniportIgmpchannelEntry.setStatus("current")


class _UniportIgmpchannelUniSvid_Type(Integer32):
    """Custom type uniportIgmpchannelUniSvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_UniportIgmpchannelUniSvid_Type.__name__ = "Integer32"
_UniportIgmpchannelUniSvid_Object = MibTableColumn
uniportIgmpchannelUniSvid = _UniportIgmpchannelUniSvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 2, 1, 1),
    _UniportIgmpchannelUniSvid_Type()
)
uniportIgmpchannelUniSvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniportIgmpchannelUniSvid.setStatus("current")


class _UniportIgmpchannelUniCvid_Type(Integer32):
    """Custom type uniportIgmpchannelUniCvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_UniportIgmpchannelUniCvid_Type.__name__ = "Integer32"
_UniportIgmpchannelUniCvid_Object = MibTableColumn
uniportIgmpchannelUniCvid = _UniportIgmpchannelUniCvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 2, 1, 2),
    _UniportIgmpchannelUniCvid_Type()
)
uniportIgmpchannelUniCvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniportIgmpchannelUniCvid.setStatus("current")


class _UniportIgmpchannelVersion_Type(Integer32):
    """Custom type uniportIgmpchannelVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igmpv2", 2),
          ("igmpv3", 3))
    )


_UniportIgmpchannelVersion_Type.__name__ = "Integer32"
_UniportIgmpchannelVersion_Object = MibTableColumn
uniportIgmpchannelVersion = _UniportIgmpchannelVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 2, 1, 3),
    _UniportIgmpchannelVersion_Type()
)
uniportIgmpchannelVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportIgmpchannelVersion.setStatus("current")


class _UniportIgmpchannelMaxgroup_Type(Integer32):
    """Custom type uniportIgmpchannelMaxgroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_UniportIgmpchannelMaxgroup_Type.__name__ = "Integer32"
_UniportIgmpchannelMaxgroup_Object = MibTableColumn
uniportIgmpchannelMaxgroup = _UniportIgmpchannelMaxgroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 2, 1, 4),
    _UniportIgmpchannelMaxgroup_Type()
)
uniportIgmpchannelMaxgroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportIgmpchannelMaxgroup.setStatus("current")


class _UniportIgmpchannelMaxmsg_Type(Integer32):
    """Custom type uniportIgmpchannelMaxmsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UniportIgmpchannelMaxmsg_Type.__name__ = "Integer32"
_UniportIgmpchannelMaxmsg_Object = MibTableColumn
uniportIgmpchannelMaxmsg = _UniportIgmpchannelMaxmsg_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 2, 1, 5),
    _UniportIgmpchannelMaxmsg_Type()
)
uniportIgmpchannelMaxmsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportIgmpchannelMaxmsg.setStatus("current")


class _UniportIgmpchannelSignaling_Type(Integer32):
    """Custom type uniportIgmpchannelSignaling based on Integer32"""
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


_UniportIgmpchannelSignaling_Type.__name__ = "Integer32"
_UniportIgmpchannelSignaling_Object = MibTableColumn
uniportIgmpchannelSignaling = _UniportIgmpchannelSignaling_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 2, 1, 6),
    _UniportIgmpchannelSignaling_Type()
)
uniportIgmpchannelSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportIgmpchannelSignaling.setStatus("current")
_UniportIgmpchannelPreviewpkg_Type = DisplayString
_UniportIgmpchannelPreviewpkg_Object = MibTableColumn
uniportIgmpchannelPreviewpkg = _UniportIgmpchannelPreviewpkg_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 2, 1, 7),
    _UniportIgmpchannelPreviewpkg_Type()
)
uniportIgmpchannelPreviewpkg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportIgmpchannelPreviewpkg.setStatus("current")
_UniportIgmpchannelFullviewpkg_Type = DisplayString
_UniportIgmpchannelFullviewpkg_Object = MibTableColumn
uniportIgmpchannelFullviewpkg = _UniportIgmpchannelFullviewpkg_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 2, 1, 8),
    _UniportIgmpchannelFullviewpkg_Type()
)
uniportIgmpchannelFullviewpkg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportIgmpchannelFullviewpkg.setStatus("current")
_UniportIgmpchannelRowStatus_Type = RowStatus
_UniportIgmpchannelRowStatus_Object = MibTableColumn
uniportIgmpchannelRowStatus = _UniportIgmpchannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 2, 1, 10),
    _UniportIgmpchannelRowStatus_Type()
)
uniportIgmpchannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniportIgmpchannelRowStatus.setStatus("current")


class _UniportIgmpchannelTrafficTxTag_Type(Integer32):
    """Custom type uniportIgmpchannelTrafficTxTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 3),
          ("untag", 4),
          ("replace", 5))
    )


_UniportIgmpchannelTrafficTxTag_Type.__name__ = "Integer32"
_UniportIgmpchannelTrafficTxTag_Object = MibTableColumn
uniportIgmpchannelTrafficTxTag = _UniportIgmpchannelTrafficTxTag_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 2, 1, 11),
    _UniportIgmpchannelTrafficTxTag_Type()
)
uniportIgmpchannelTrafficTxTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportIgmpchannelTrafficTxTag.setStatus("current")
_UniportIgmpchannelCacProf_Type = DisplayString
_UniportIgmpchannelCacProf_Object = MibTableColumn
uniportIgmpchannelCacProf = _UniportIgmpchannelCacProf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 2, 1, 12),
    _UniportIgmpchannelCacProf_Type()
)
uniportIgmpchannelCacProf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportIgmpchannelCacProf.setStatus("current")


class _UniportIgmpchannelTrafficTxTagRepVid_Type(Integer32):
    """Custom type uniportIgmpchannelTrafficTxTagRepVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_UniportIgmpchannelTrafficTxTagRepVid_Type.__name__ = "Integer32"
_UniportIgmpchannelTrafficTxTagRepVid_Object = MibTableColumn
uniportIgmpchannelTrafficTxTagRepVid = _UniportIgmpchannelTrafficTxTagRepVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 2, 1, 13),
    _UniportIgmpchannelTrafficTxTagRepVid_Type()
)
uniportIgmpchannelTrafficTxTagRepVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportIgmpchannelTrafficTxTagRepVid.setStatus("current")
_UniportProtoBasedTable_Object = MibTable
uniportProtoBasedTable = _UniportProtoBasedTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 3)
)
if mibBuilder.loadTexts:
    uniportProtoBasedTable.setStatus("current")
_UniportProtoBasedEntry_Object = MibTableRow
uniportProtoBasedEntry = _UniportProtoBasedEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 3, 1)
)
uniportProtoBasedEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "uniPort"),
    (0, "ZYXEL-olt1408-MIB", "uniportProtoBasedEtherType"),
)
if mibBuilder.loadTexts:
    uniportProtoBasedEntry.setStatus("current")
_UniportProtoBasedEtherType_Type = Integer32
_UniportProtoBasedEtherType_Object = MibTableColumn
uniportProtoBasedEtherType = _UniportProtoBasedEtherType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 3, 1, 1),
    _UniportProtoBasedEtherType_Type()
)
uniportProtoBasedEtherType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniportProtoBasedEtherType.setStatus("current")
_UniportProtoBasedSvid_Type = Integer32
_UniportProtoBasedSvid_Object = MibTableColumn
uniportProtoBasedSvid = _UniportProtoBasedSvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 3, 1, 2),
    _UniportProtoBasedSvid_Type()
)
uniportProtoBasedSvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportProtoBasedSvid.setStatus("current")
_UniportProtoBasedCvid_Type = Integer32
_UniportProtoBasedCvid_Object = MibTableColumn
uniportProtoBasedCvid = _UniportProtoBasedCvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 3, 1, 3),
    _UniportProtoBasedCvid_Type()
)
uniportProtoBasedCvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportProtoBasedCvid.setStatus("current")
_UniportProtoBasedPriority_Type = Integer32
_UniportProtoBasedPriority_Object = MibTableColumn
uniportProtoBasedPriority = _UniportProtoBasedPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 3, 1, 4),
    _UniportProtoBasedPriority_Type()
)
uniportProtoBasedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportProtoBasedPriority.setStatus("current")
_UniportProtoBasedRowStatus_Type = RowStatus
_UniportProtoBasedRowStatus_Object = MibTableColumn
uniportProtoBasedRowStatus = _UniportProtoBasedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 3, 1, 5),
    _UniportProtoBasedRowStatus_Type()
)
uniportProtoBasedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniportProtoBasedRowStatus.setStatus("current")
_UniportPvidTable_Object = MibTable
uniportPvidTable = _UniportPvidTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 4)
)
if mibBuilder.loadTexts:
    uniportPvidTable.setStatus("current")
_UniportPvidEntry_Object = MibTableRow
uniportPvidEntry = _UniportPvidEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 4, 1)
)
uniportPvidEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "uniPort"),
)
if mibBuilder.loadTexts:
    uniportPvidEntry.setStatus("current")
_UniportPvidUniSvid_Type = Integer32
_UniportPvidUniSvid_Object = MibTableColumn
uniportPvidUniSvid = _UniportPvidUniSvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 4, 1, 1),
    _UniportPvidUniSvid_Type()
)
uniportPvidUniSvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportPvidUniSvid.setStatus("current")
_UniportPvidUniCvid_Type = Integer32
_UniportPvidUniCvid_Object = MibTableColumn
uniportPvidUniCvid = _UniportPvidUniCvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 4, 1, 2),
    _UniportPvidUniCvid_Type()
)
uniportPvidUniCvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportPvidUniCvid.setStatus("current")
_UniportPvidPriority_Type = Integer32
_UniportPvidPriority_Object = MibTableColumn
uniportPvidPriority = _UniportPvidPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 4, 1, 3),
    _UniportPvidPriority_Type()
)
uniportPvidPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportPvidPriority.setStatus("current")
_UniportPvidRowStatus_Type = RowStatus
_UniportPvidRowStatus_Object = MibTableColumn
uniportPvidRowStatus = _UniportPvidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 4, 1, 4),
    _UniportPvidRowStatus_Type()
)
uniportPvidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniportPvidRowStatus.setStatus("current")
_UniportQueueTable_Object = MibTable
uniportQueueTable = _UniportQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 5)
)
if mibBuilder.loadTexts:
    uniportQueueTable.setStatus("current")
_UniportQueueEntry_Object = MibTableRow
uniportQueueEntry = _UniportQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 5, 1)
)
uniportQueueEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "uniPort"),
    (0, "ZYXEL-olt1408-MIB", "uniportQueueTc"),
)
if mibBuilder.loadTexts:
    uniportQueueEntry.setStatus("current")


class _UniportQueueTc_Type(Integer32):
    """Custom type uniportQueueTc based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7),
          ("tcNull", 8))
    )


_UniportQueueTc_Type.__name__ = "Integer32"
_UniportQueueTc_Object = MibTableColumn
uniportQueueTc = _UniportQueueTc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 5, 1, 1),
    _UniportQueueTc_Type()
)
uniportQueueTc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniportQueueTc.setStatus("current")


class _UniportQueuePriority_Type(Integer32):
    """Custom type uniportQueuePriority based on Integer32"""
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
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7))
    )


_UniportQueuePriority_Type.__name__ = "Integer32"
_UniportQueuePriority_Object = MibTableColumn
uniportQueuePriority = _UniportQueuePriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 5, 1, 2),
    _UniportQueuePriority_Type()
)
uniportQueuePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportQueuePriority.setStatus("current")
_UniportQueueWeight_Type = Integer32
_UniportQueueWeight_Object = MibTableColumn
uniportQueueWeight = _UniportQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 5, 1, 3),
    _UniportQueueWeight_Type()
)
uniportQueueWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportQueueWeight.setStatus("current")
_UniportQueueUsbwprofname_Type = DisplayString
_UniportQueueUsbwprofname_Object = MibTableColumn
uniportQueueUsbwprofname = _UniportQueueUsbwprofname_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 5, 1, 4),
    _UniportQueueUsbwprofname_Type()
)
uniportQueueUsbwprofname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportQueueUsbwprofname.setStatus("current")
_UniportQueueDsbwprofname_Type = DisplayString
_UniportQueueDsbwprofname_Object = MibTableColumn
uniportQueueDsbwprofname = _UniportQueueDsbwprofname_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 5, 1, 5),
    _UniportQueueDsbwprofname_Type()
)
uniportQueueDsbwprofname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportQueueDsbwprofname.setStatus("current")


class _UniportQueueDsoption_Type(Integer32):
    """Custom type uniportQueueDsoption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("olt", 0),
          ("ont", 1))
    )


_UniportQueueDsoption_Type.__name__ = "Integer32"
_UniportQueueDsoption_Object = MibTableColumn
uniportQueueDsoption = _UniportQueueDsoption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 5, 1, 6),
    _UniportQueueDsoption_Type()
)
uniportQueueDsoption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportQueueDsoption.setStatus("current")
_UniportQueueUsbwsharegroupid_Type = Integer32
_UniportQueueUsbwsharegroupid_Object = MibTableColumn
uniportQueueUsbwsharegroupid = _UniportQueueUsbwsharegroupid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 5, 1, 7),
    _UniportQueueUsbwsharegroupid_Type()
)
uniportQueueUsbwsharegroupid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportQueueUsbwsharegroupid.setStatus("current")
_UniportQueueRowStatus_Type = RowStatus
_UniportQueueRowStatus_Object = MibTableColumn
uniportQueueRowStatus = _UniportQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 5, 1, 8),
    _UniportQueueRowStatus_Type()
)
uniportQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniportQueueRowStatus.setStatus("current")
_UniportQueueDsbwsharegroupid_Type = Integer32
_UniportQueueDsbwsharegroupid_Object = MibTableColumn
uniportQueueDsbwsharegroupid = _UniportQueueDsbwsharegroupid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 5, 1, 9),
    _UniportQueueDsbwsharegroupid_Type()
)
uniportQueueDsbwsharegroupid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportQueueDsbwsharegroupid.setStatus("current")
_UniportVlanTable_Object = MibTable
uniportVlanTable = _UniportVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 6)
)
if mibBuilder.loadTexts:
    uniportVlanTable.setStatus("current")
_UniportVlanEntry_Object = MibTableRow
uniportVlanEntry = _UniportVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 6, 1)
)
uniportVlanEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "uniPort"),
    (0, "ZYXEL-olt1408-MIB", "uniportVlanUniSvid"),
    (0, "ZYXEL-olt1408-MIB", "uniportVlanUniCvid"),
)
if mibBuilder.loadTexts:
    uniportVlanEntry.setStatus("current")
_UniportVlanUniSvid_Type = Integer32
_UniportVlanUniSvid_Object = MibTableColumn
uniportVlanUniSvid = _UniportVlanUniSvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 6, 1, 1),
    _UniportVlanUniSvid_Type()
)
uniportVlanUniSvid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniportVlanUniSvid.setStatus("current")
_UniportVlanUniCvid_Type = Integer32
_UniportVlanUniCvid_Object = MibTableColumn
uniportVlanUniCvid = _UniportVlanUniCvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 6, 1, 2),
    _UniportVlanUniCvid_Type()
)
uniportVlanUniCvid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniportVlanUniCvid.setStatus("current")
_UniportVlanNetworkSvid_Type = Integer32
_UniportVlanNetworkSvid_Object = MibTableColumn
uniportVlanNetworkSvid = _UniportVlanNetworkSvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 6, 1, 3),
    _UniportVlanNetworkSvid_Type()
)
uniportVlanNetworkSvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVlanNetworkSvid.setStatus("current")


class _UniportVlanNetworkSpri_Type(Integer32):
    """Custom type uniportVlanNetworkSpri based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7),
          ("priorityNull", 8))
    )


_UniportVlanNetworkSpri_Type.__name__ = "Integer32"
_UniportVlanNetworkSpri_Object = MibTableColumn
uniportVlanNetworkSpri = _UniportVlanNetworkSpri_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 6, 1, 4),
    _UniportVlanNetworkSpri_Type()
)
uniportVlanNetworkSpri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVlanNetworkSpri.setStatus("current")
_UniportVlanNetworkCvid_Type = Integer32
_UniportVlanNetworkCvid_Object = MibTableColumn
uniportVlanNetworkCvid = _UniportVlanNetworkCvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 6, 1, 5),
    _UniportVlanNetworkCvid_Type()
)
uniportVlanNetworkCvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVlanNetworkCvid.setStatus("current")
_UniportVlanIngProf_Type = DisplayString
_UniportVlanIngProf_Object = MibTableColumn
uniportVlanIngProf = _UniportVlanIngProf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 6, 1, 6),
    _UniportVlanIngProf_Type()
)
uniportVlanIngProf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVlanIngProf.setStatus("current")
_UniportVlanGemPort_Type = Integer32
_UniportVlanGemPort_Object = MibTableColumn
uniportVlanGemPort = _UniportVlanGemPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 6, 1, 7),
    _UniportVlanGemPort_Type()
)
uniportVlanGemPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVlanGemPort.setStatus("current")


class _UniportVlanTr156_Type(Integer32):
    """Custom type uniportVlanTr156 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_UniportVlanTr156_Type.__name__ = "Integer32"
_UniportVlanTr156_Object = MibTableColumn
uniportVlanTr156 = _UniportVlanTr156_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 6, 1, 8),
    _UniportVlanTr156_Type()
)
uniportVlanTr156.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVlanTr156.setStatus("current")


class _UniportVlanTxTag_Type(Integer32):
    """Custom type uniportVlanTxTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("untag", 1),
          ("tag", 2),
          ("pritag", 3))
    )


_UniportVlanTxTag_Type.__name__ = "Integer32"
_UniportVlanTxTag_Object = MibTableColumn
uniportVlanTxTag = _UniportVlanTxTag_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 6, 1, 9),
    _UniportVlanTxTag_Type()
)
uniportVlanTxTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVlanTxTag.setStatus("current")
_UniportVlanPbitProf_Type = DisplayString
_UniportVlanPbitProf_Object = MibTableColumn
uniportVlanPbitProf = _UniportVlanPbitProf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 6, 1, 10),
    _UniportVlanPbitProf_Type()
)
uniportVlanPbitProf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVlanPbitProf.setStatus("current")


class _UniportVlanDscpToPbit_Type(Integer32):
    """Custom type uniportVlanDscpToPbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_UniportVlanDscpToPbit_Type.__name__ = "Integer32"
_UniportVlanDscpToPbit_Object = MibTableColumn
uniportVlanDscpToPbit = _UniportVlanDscpToPbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 6, 1, 11),
    _UniportVlanDscpToPbit_Type()
)
uniportVlanDscpToPbit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVlanDscpToPbit.setStatus("current")


class _UniportVlanAesEncrypt_Type(Integer32):
    """Custom type uniportVlanAesEncrypt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_UniportVlanAesEncrypt_Type.__name__ = "Integer32"
_UniportVlanAesEncrypt_Object = MibTableColumn
uniportVlanAesEncrypt = _UniportVlanAesEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 6, 1, 12),
    _UniportVlanAesEncrypt_Type()
)
uniportVlanAesEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVlanAesEncrypt.setStatus("current")
_UniportVlanRowStatus_Type = RowStatus
_UniportVlanRowStatus_Object = MibTableColumn
uniportVlanRowStatus = _UniportVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 6, 1, 13),
    _UniportVlanRowStatus_Type()
)
uniportVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniportVlanRowStatus.setStatus("current")


class _UniportVlanSharePriority_Type(Integer32):
    """Custom type uniportVlanSharePriority based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7),
          ("off", 8))
    )


_UniportVlanSharePriority_Type.__name__ = "Integer32"
_UniportVlanSharePriority_Object = MibTableColumn
uniportVlanSharePriority = _UniportVlanSharePriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 6, 1, 14),
    _UniportVlanSharePriority_Type()
)
uniportVlanSharePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVlanSharePriority.setStatus("current")
_UniportVlanMacNum_Type = Integer32
_UniportVlanMacNum_Object = MibTableColumn
uniportVlanMacNum = _UniportVlanMacNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 6, 1, 15),
    _UniportVlanMacNum_Type()
)
uniportVlanMacNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVlanMacNum.setStatus("current")
_UniportVoipTable_Object = MibTable
uniportVoipTable = _UniportVoipTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 7)
)
if mibBuilder.loadTexts:
    uniportVoipTable.setStatus("current")
_UniportVoipEntry_Object = MibTableRow
uniportVoipEntry = _UniportVoipEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 7, 1)
)
uniportVoipEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "uniPort"),
)
if mibBuilder.loadTexts:
    uniportVoipEntry.setStatus("current")
_UniportVoipMode_Type = Integer32
_UniportVoipMode_Object = MibTableColumn
uniportVoipMode = _UniportVoipMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 7, 1, 1),
    _UniportVoipMode_Type()
)
uniportVoipMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVoipMode.setStatus("current")
_UniportVoipUniCvid_Type = Integer32
_UniportVoipUniCvid_Object = MibTableColumn
uniportVoipUniCvid = _UniportVoipUniCvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 7, 1, 2),
    _UniportVoipUniCvid_Type()
)
uniportVoipUniCvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVoipUniCvid.setStatus("current")
_UniportVoipCommProfName_Type = DisplayString
_UniportVoipCommProfName_Object = MibTableColumn
uniportVoipCommProfName = _UniportVoipCommProfName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 7, 1, 3),
    _UniportVoipCommProfName_Type()
)
uniportVoipCommProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVoipCommProfName.setStatus("current")
_UniportVoipSipProfName_Type = DisplayString
_UniportVoipSipProfName_Object = MibTableColumn
uniportVoipSipProfName = _UniportVoipSipProfName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 7, 1, 4),
    _UniportVoipSipProfName_Type()
)
uniportVoipSipProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVoipSipProfName.setStatus("current")
_UniportVoipUsername_Type = DisplayString
_UniportVoipUsername_Object = MibTableColumn
uniportVoipUsername = _UniportVoipUsername_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 7, 1, 5),
    _UniportVoipUsername_Type()
)
uniportVoipUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVoipUsername.setStatus("current")
_UniportVoipPassword_Type = DisplayString
_UniportVoipPassword_Object = MibTableColumn
uniportVoipPassword = _UniportVoipPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 7, 1, 6),
    _UniportVoipPassword_Type()
)
uniportVoipPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVoipPassword.setStatus("current")
_UniportVoipDialPlanName_Type = DisplayString
_UniportVoipDialPlanName_Object = MibTableColumn
uniportVoipDialPlanName = _UniportVoipDialPlanName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 7, 1, 7),
    _UniportVoipDialPlanName_Type()
)
uniportVoipDialPlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVoipDialPlanName.setStatus("current")
_UniportVoipAor_Type = DisplayString
_UniportVoipAor_Object = MibTableColumn
uniportVoipAor = _UniportVoipAor_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 7, 1, 8),
    _UniportVoipAor_Type()
)
uniportVoipAor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVoipAor.setStatus("current")
_UniportVoipDispName_Type = DisplayString
_UniportVoipDispName_Object = MibTableColumn
uniportVoipDispName = _UniportVoipDispName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 7, 1, 9),
    _UniportVoipDispName_Type()
)
uniportVoipDispName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVoipDispName.setStatus("current")
_UniportVoipVmailUri_Type = DisplayString
_UniportVoipVmailUri_Object = MibTableColumn
uniportVoipVmailUri = _UniportVoipVmailUri_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 7, 1, 10),
    _UniportVoipVmailUri_Type()
)
uniportVoipVmailUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVoipVmailUri.setStatus("current")
_UniportVoipVmailExtimer_Type = Integer32
_UniportVoipVmailExtimer_Object = MibTableColumn
uniportVoipVmailExtimer = _UniportVoipVmailExtimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 7, 1, 11),
    _UniportVoipVmailExtimer_Type()
)
uniportVoipVmailExtimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVoipVmailExtimer.setStatus("current")
_UniportVoipReleaseTimer_Type = Integer32
_UniportVoipReleaseTimer_Object = MibTableColumn
uniportVoipReleaseTimer = _UniportVoipReleaseTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 7, 1, 12),
    _UniportVoipReleaseTimer_Type()
)
uniportVoipReleaseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVoipReleaseTimer.setStatus("current")
_UniportVoipRohTimer_Type = Integer32
_UniportVoipRohTimer_Object = MibTableColumn
uniportVoipRohTimer = _UniportVoipRohTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 7, 1, 13),
    _UniportVoipRohTimer_Type()
)
uniportVoipRohTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniportVoipRohTimer.setStatus("current")
_UniportVoipRowStatus_Type = RowStatus
_UniportVoipRowStatus_Object = MibTableColumn
uniportVoipRowStatus = _UniportVoipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 5, 7, 1, 14),
    _UniportVoipRowStatus_Type()
)
uniportVoipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniportVoipRowStatus.setStatus("current")
_OntOmciCfmTable_ObjectIdentity = ObjectIdentity
ontOmciCfmTable = _OntOmciCfmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 6)
)
_OmciCfmMdTable_Object = MibTable
omciCfmMdTable = _OmciCfmMdTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 6, 1)
)
if mibBuilder.loadTexts:
    omciCfmMdTable.setStatus("current")
_OmciCfmMdEntry_Object = MibTableRow
omciCfmMdEntry = _OmciCfmMdEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 6, 1, 1)
)
omciCfmMdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
)
if mibBuilder.loadTexts:
    omciCfmMdEntry.setStatus("current")


class _OmciCfmMdIndex_Type(Unsigned32):
    """Custom type omciCfmMdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OmciCfmMdIndex_Type.__name__ = "Unsigned32"
_OmciCfmMdIndex_Object = MibTableColumn
omciCfmMdIndex = _OmciCfmMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 6, 1, 1, 1),
    _OmciCfmMdIndex_Type()
)
omciCfmMdIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    omciCfmMdIndex.setStatus("current")


class _OmciCfmMdFormat_Type(Integer32):
    """Custom type omciCfmMdFormat based on Integer32"""
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
          ("dns", 2),
          ("mac", 3),
          ("string", 4))
    )


_OmciCfmMdFormat_Type.__name__ = "Integer32"
_OmciCfmMdFormat_Object = MibTableColumn
omciCfmMdFormat = _OmciCfmMdFormat_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 6, 1, 1, 2),
    _OmciCfmMdFormat_Type()
)
omciCfmMdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    omciCfmMdFormat.setStatus("current")
_OmciCfmMdName_Type = OctetString
_OmciCfmMdName_Object = MibTableColumn
omciCfmMdName = _OmciCfmMdName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 6, 1, 1, 3),
    _OmciCfmMdName_Type()
)
omciCfmMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    omciCfmMdName.setStatus("current")
_OmciCfmMdLevel_Type = Integer32
_OmciCfmMdLevel_Object = MibTableColumn
omciCfmMdLevel = _OmciCfmMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 6, 1, 1, 4),
    _OmciCfmMdLevel_Type()
)
omciCfmMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    omciCfmMdLevel.setStatus("current")
_OmciCfmMdRowStatus_Type = RowStatus
_OmciCfmMdRowStatus_Object = MibTableColumn
omciCfmMdRowStatus = _OmciCfmMdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 6, 1, 1, 5),
    _OmciCfmMdRowStatus_Type()
)
omciCfmMdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    omciCfmMdRowStatus.setStatus("current")
_OmciCfmMaTable_Object = MibTable
omciCfmMaTable = _OmciCfmMaTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 6, 2)
)
if mibBuilder.loadTexts:
    omciCfmMaTable.setStatus("current")
_OmciCfmMaEntry_Object = MibTableRow
omciCfmMaEntry = _OmciCfmMaEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 6, 2, 1)
)
omciCfmMaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
)
if mibBuilder.loadTexts:
    omciCfmMaEntry.setStatus("current")


class _OmciCfmMaIndex_Type(Unsigned32):
    """Custom type omciCfmMaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OmciCfmMaIndex_Type.__name__ = "Unsigned32"
_OmciCfmMaIndex_Object = MibTableColumn
omciCfmMaIndex = _OmciCfmMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 6, 2, 1, 1),
    _OmciCfmMaIndex_Type()
)
omciCfmMaIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    omciCfmMaIndex.setStatus("current")


class _OmciCfmMaMdIndex_Type(Unsigned32):
    """Custom type omciCfmMaMdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OmciCfmMaMdIndex_Type.__name__ = "Unsigned32"
_OmciCfmMaMdIndex_Object = MibTableColumn
omciCfmMaMdIndex = _OmciCfmMaMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 6, 2, 1, 2),
    _OmciCfmMaMdIndex_Type()
)
omciCfmMaMdIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    omciCfmMaMdIndex.setStatus("current")


class _OmciCfmMaFormat_Type(Integer32):
    """Custom type omciCfmMaFormat based on Integer32"""
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
        *(("vid", 1),
          ("string", 2),
          ("integer", 3),
          ("vpnid", 4))
    )


_OmciCfmMaFormat_Type.__name__ = "Integer32"
_OmciCfmMaFormat_Object = MibTableColumn
omciCfmMaFormat = _OmciCfmMaFormat_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 6, 2, 1, 3),
    _OmciCfmMaFormat_Type()
)
omciCfmMaFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    omciCfmMaFormat.setStatus("current")
_OmciCfmMaName_Type = OctetString
_OmciCfmMaName_Object = MibTableColumn
omciCfmMaName = _OmciCfmMaName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 6, 2, 1, 4),
    _OmciCfmMaName_Type()
)
omciCfmMaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    omciCfmMaName.setStatus("current")


class _OmciCfmMaCcmInterval_Type(Integer32):
    """Custom type omciCfmMaCcmInterval based on Integer32"""
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
        *(("ccmDisable", 0),
          ("ccm3point33ms", 1),
          ("ccm10ms", 2),
          ("ccm100ms", 3),
          ("ccm1s", 4),
          ("ccm10s", 5),
          ("ccm1min", 6),
          ("ccm10min", 7))
    )


_OmciCfmMaCcmInterval_Type.__name__ = "Integer32"
_OmciCfmMaCcmInterval_Object = MibTableColumn
omciCfmMaCcmInterval = _OmciCfmMaCcmInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 6, 2, 1, 5),
    _OmciCfmMaCcmInterval_Type()
)
omciCfmMaCcmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    omciCfmMaCcmInterval.setStatus("current")
_OmciCfmMaRowStatus_Type = RowStatus
_OmciCfmMaRowStatus_Object = MibTableColumn
omciCfmMaRowStatus = _OmciCfmMaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 6, 2, 1, 6),
    _OmciCfmMaRowStatus_Type()
)
omciCfmMaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    omciCfmMaRowStatus.setStatus("current")
_OntuniportOmciCfmTable_ObjectIdentity = ObjectIdentity
ontuniportOmciCfmTable = _OntuniportOmciCfmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 7)
)
_OmciCfmMepTable_Object = MibTable
omciCfmMepTable = _OmciCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 7, 1)
)
if mibBuilder.loadTexts:
    omciCfmMepTable.setStatus("current")
_OmciCfmMepEntry_Object = MibTableRow
omciCfmMepEntry = _OmciCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 7, 1, 1)
)
omciCfmMepEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "uniPort"),
)
if mibBuilder.loadTexts:
    omciCfmMepEntry.setStatus("current")


class _OmciCfmMepIdentifier_Type(Unsigned32):
    """Custom type omciCfmMepIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_OmciCfmMepIdentifier_Type.__name__ = "Unsigned32"
_OmciCfmMepIdentifier_Object = MibTableColumn
omciCfmMepIdentifier = _OmciCfmMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 7, 1, 1, 1),
    _OmciCfmMepIdentifier_Type()
)
omciCfmMepIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    omciCfmMepIdentifier.setStatus("current")


class _OmciCfmMepMaIndex_Type(Unsigned32):
    """Custom type omciCfmMepMaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OmciCfmMepMaIndex_Type.__name__ = "Unsigned32"
_OmciCfmMepMaIndex_Object = MibTableColumn
omciCfmMepMaIndex = _OmciCfmMepMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 7, 1, 1, 2),
    _OmciCfmMepMaIndex_Type()
)
omciCfmMepMaIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    omciCfmMepMaIndex.setStatus("current")


class _OmciCfmMepCcmLtmPriority_Type(Integer32):
    """Custom type omciCfmMepCcmLtmPriority based on Integer32"""
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
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7))
    )


_OmciCfmMepCcmLtmPriority_Type.__name__ = "Integer32"
_OmciCfmMepCcmLtmPriority_Object = MibTableColumn
omciCfmMepCcmLtmPriority = _OmciCfmMepCcmLtmPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 7, 1, 1, 3),
    _OmciCfmMepCcmLtmPriority_Type()
)
omciCfmMepCcmLtmPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    omciCfmMepCcmLtmPriority.setStatus("current")
_OmciCfmMepRowStatus_Type = RowStatus
_OmciCfmMepRowStatus_Object = MibTableColumn
omciCfmMepRowStatus = _OmciCfmMepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 7, 1, 1, 4),
    _OmciCfmMepRowStatus_Type()
)
omciCfmMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    omciCfmMepRowStatus.setStatus("current")
_OntQosProfile_ObjectIdentity = ObjectIdentity
ontQosProfile = _OntQosProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8)
)
_IngressProfileTable_Object = MibTable
ingressProfileTable = _IngressProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 1)
)
if mibBuilder.loadTexts:
    ingressProfileTable.setStatus("current")
_IngressProfileEntry_Object = MibTableRow
ingressProfileEntry = _IngressProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 1, 1)
)
ingressProfileEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "ingressProfileName"),
)
if mibBuilder.loadTexts:
    ingressProfileEntry.setStatus("current")
_IngressProfileName_Type = OctetString
_IngressProfileName_Object = MibTableColumn
ingressProfileName = _IngressProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 1, 1, 1),
    _IngressProfileName_Type()
)
ingressProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressProfileName.setStatus("current")


class _IngressProfileDot1p0tc_Type(Integer32):
    """Custom type ingressProfileDot1p0tc based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7),
          ("tcNULL", 8))
    )


_IngressProfileDot1p0tc_Type.__name__ = "Integer32"
_IngressProfileDot1p0tc_Object = MibTableColumn
ingressProfileDot1p0tc = _IngressProfileDot1p0tc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 1, 1, 2),
    _IngressProfileDot1p0tc_Type()
)
ingressProfileDot1p0tc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressProfileDot1p0tc.setStatus("current")


class _IngressProfileDot1p1tc_Type(Integer32):
    """Custom type ingressProfileDot1p1tc based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7),
          ("tcNULL", 8))
    )


_IngressProfileDot1p1tc_Type.__name__ = "Integer32"
_IngressProfileDot1p1tc_Object = MibTableColumn
ingressProfileDot1p1tc = _IngressProfileDot1p1tc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 1, 1, 3),
    _IngressProfileDot1p1tc_Type()
)
ingressProfileDot1p1tc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressProfileDot1p1tc.setStatus("current")


class _IngressProfileDot1p2tc_Type(Integer32):
    """Custom type ingressProfileDot1p2tc based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7),
          ("tcNULL", 8))
    )


_IngressProfileDot1p2tc_Type.__name__ = "Integer32"
_IngressProfileDot1p2tc_Object = MibTableColumn
ingressProfileDot1p2tc = _IngressProfileDot1p2tc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 1, 1, 4),
    _IngressProfileDot1p2tc_Type()
)
ingressProfileDot1p2tc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressProfileDot1p2tc.setStatus("current")


class _IngressProfileDot1p3tc_Type(Integer32):
    """Custom type ingressProfileDot1p3tc based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7),
          ("tcNULL", 8))
    )


_IngressProfileDot1p3tc_Type.__name__ = "Integer32"
_IngressProfileDot1p3tc_Object = MibTableColumn
ingressProfileDot1p3tc = _IngressProfileDot1p3tc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 1, 1, 5),
    _IngressProfileDot1p3tc_Type()
)
ingressProfileDot1p3tc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressProfileDot1p3tc.setStatus("current")


class _IngressProfileDot1p4tc_Type(Integer32):
    """Custom type ingressProfileDot1p4tc based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7),
          ("tcNULL", 8))
    )


_IngressProfileDot1p4tc_Type.__name__ = "Integer32"
_IngressProfileDot1p4tc_Object = MibTableColumn
ingressProfileDot1p4tc = _IngressProfileDot1p4tc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 1, 1, 6),
    _IngressProfileDot1p4tc_Type()
)
ingressProfileDot1p4tc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressProfileDot1p4tc.setStatus("current")


class _IngressProfileDot1p5tc_Type(Integer32):
    """Custom type ingressProfileDot1p5tc based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7),
          ("tcNULL", 8))
    )


_IngressProfileDot1p5tc_Type.__name__ = "Integer32"
_IngressProfileDot1p5tc_Object = MibTableColumn
ingressProfileDot1p5tc = _IngressProfileDot1p5tc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 1, 1, 7),
    _IngressProfileDot1p5tc_Type()
)
ingressProfileDot1p5tc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressProfileDot1p5tc.setStatus("current")


class _IngressProfileDot1p6tc_Type(Integer32):
    """Custom type ingressProfileDot1p6tc based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7),
          ("tcNULL", 8))
    )


_IngressProfileDot1p6tc_Type.__name__ = "Integer32"
_IngressProfileDot1p6tc_Object = MibTableColumn
ingressProfileDot1p6tc = _IngressProfileDot1p6tc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 1, 1, 8),
    _IngressProfileDot1p6tc_Type()
)
ingressProfileDot1p6tc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressProfileDot1p6tc.setStatus("current")


class _IngressProfileDot1p7tc_Type(Integer32):
    """Custom type ingressProfileDot1p7tc based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7),
          ("tcNULL", 8))
    )


_IngressProfileDot1p7tc_Type.__name__ = "Integer32"
_IngressProfileDot1p7tc_Object = MibTableColumn
ingressProfileDot1p7tc = _IngressProfileDot1p7tc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 1, 1, 9),
    _IngressProfileDot1p7tc_Type()
)
ingressProfileDot1p7tc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressProfileDot1p7tc.setStatus("current")
_IngressProfileRowStatus_Type = RowStatus
_IngressProfileRowStatus_Object = MibTableColumn
ingressProfileRowStatus = _IngressProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 1, 1, 10),
    _IngressProfileRowStatus_Type()
)
ingressProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ingressProfileRowStatus.setStatus("current")
_PbitProfileTable_Object = MibTable
pbitProfileTable = _PbitProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 2)
)
if mibBuilder.loadTexts:
    pbitProfileTable.setStatus("current")
_PbitProfileEntry_Object = MibTableRow
pbitProfileEntry = _PbitProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 2, 1)
)
pbitProfileEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "pbitProfileName"),
)
if mibBuilder.loadTexts:
    pbitProfileEntry.setStatus("current")
_PbitProfileName_Type = OctetString
_PbitProfileName_Object = MibTableColumn
pbitProfileName = _PbitProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 2, 1, 1),
    _PbitProfileName_Type()
)
pbitProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbitProfileName.setStatus("current")


class _PbitProfileP0to_Type(Integer32):
    """Custom type pbitProfileP0to based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7),
          ("tcDrop", 8))
    )


_PbitProfileP0to_Type.__name__ = "Integer32"
_PbitProfileP0to_Object = MibTableColumn
pbitProfileP0to = _PbitProfileP0to_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 2, 1, 2),
    _PbitProfileP0to_Type()
)
pbitProfileP0to.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbitProfileP0to.setStatus("current")


class _PbitProfileP1to_Type(Integer32):
    """Custom type pbitProfileP1to based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7),
          ("tcDrop", 8))
    )


_PbitProfileP1to_Type.__name__ = "Integer32"
_PbitProfileP1to_Object = MibTableColumn
pbitProfileP1to = _PbitProfileP1to_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 2, 1, 3),
    _PbitProfileP1to_Type()
)
pbitProfileP1to.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbitProfileP1to.setStatus("current")


class _PbitProfileP2to_Type(Integer32):
    """Custom type pbitProfileP2to based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7),
          ("tcDrop", 8))
    )


_PbitProfileP2to_Type.__name__ = "Integer32"
_PbitProfileP2to_Object = MibTableColumn
pbitProfileP2to = _PbitProfileP2to_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 2, 1, 4),
    _PbitProfileP2to_Type()
)
pbitProfileP2to.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbitProfileP2to.setStatus("current")


class _PbitProfileP3to_Type(Integer32):
    """Custom type pbitProfileP3to based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7),
          ("tcDrop", 8))
    )


_PbitProfileP3to_Type.__name__ = "Integer32"
_PbitProfileP3to_Object = MibTableColumn
pbitProfileP3to = _PbitProfileP3to_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 2, 1, 5),
    _PbitProfileP3to_Type()
)
pbitProfileP3to.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbitProfileP3to.setStatus("current")


class _PbitProfileP4to_Type(Integer32):
    """Custom type pbitProfileP4to based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7),
          ("tcDrop", 8))
    )


_PbitProfileP4to_Type.__name__ = "Integer32"
_PbitProfileP4to_Object = MibTableColumn
pbitProfileP4to = _PbitProfileP4to_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 2, 1, 6),
    _PbitProfileP4to_Type()
)
pbitProfileP4to.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbitProfileP4to.setStatus("current")


class _PbitProfileP5to_Type(Integer32):
    """Custom type pbitProfileP5to based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7),
          ("tcDrop", 8))
    )


_PbitProfileP5to_Type.__name__ = "Integer32"
_PbitProfileP5to_Object = MibTableColumn
pbitProfileP5to = _PbitProfileP5to_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 2, 1, 7),
    _PbitProfileP5to_Type()
)
pbitProfileP5to.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbitProfileP5to.setStatus("current")


class _PbitProfileP6to_Type(Integer32):
    """Custom type pbitProfileP6to based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7),
          ("tcDrop", 8))
    )


_PbitProfileP6to_Type.__name__ = "Integer32"
_PbitProfileP6to_Object = MibTableColumn
pbitProfileP6to = _PbitProfileP6to_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 2, 1, 8),
    _PbitProfileP6to_Type()
)
pbitProfileP6to.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbitProfileP6to.setStatus("current")


class _PbitProfileP7to_Type(Integer32):
    """Custom type pbitProfileP7to based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7),
          ("tcDrop", 8))
    )


_PbitProfileP7to_Type.__name__ = "Integer32"
_PbitProfileP7to_Object = MibTableColumn
pbitProfileP7to = _PbitProfileP7to_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 2, 1, 9),
    _PbitProfileP7to_Type()
)
pbitProfileP7to.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbitProfileP7to.setStatus("current")
_PbitProfileRowStatus_Type = RowStatus
_PbitProfileRowStatus_Object = MibTableColumn
pbitProfileRowStatus = _PbitProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 2, 1, 10),
    _PbitProfileRowStatus_Type()
)
pbitProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pbitProfileRowStatus.setStatus("current")
_BwProfileTable_Object = MibTable
bwProfileTable = _BwProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 3)
)
if mibBuilder.loadTexts:
    bwProfileTable.setStatus("current")
_BwProfileEntry_Object = MibTableRow
bwProfileEntry = _BwProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 3, 1)
)
bwProfileEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "bwProfileName"),
)
if mibBuilder.loadTexts:
    bwProfileEntry.setStatus("current")
_BwProfileName_Type = OctetString
_BwProfileName_Object = MibTableColumn
bwProfileName = _BwProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 3, 1, 1),
    _BwProfileName_Type()
)
bwProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwProfileName.setStatus("current")
_BwProfileSir_Type = Integer32
_BwProfileSir_Object = MibTableColumn
bwProfileSir = _BwProfileSir_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 3, 1, 2),
    _BwProfileSir_Type()
)
bwProfileSir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwProfileSir.setStatus("current")
_BwProfileAir_Type = Integer32
_BwProfileAir_Object = MibTableColumn
bwProfileAir = _BwProfileAir_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 3, 1, 3),
    _BwProfileAir_Type()
)
bwProfileAir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwProfileAir.setStatus("current")
_BwProfilePir_Type = Integer32
_BwProfilePir_Object = MibTableColumn
bwProfilePir = _BwProfilePir_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 3, 1, 4),
    _BwProfilePir_Type()
)
bwProfilePir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwProfilePir.setStatus("current")
_BwProfileRowStatus_Type = RowStatus
_BwProfileRowStatus_Object = MibTableColumn
bwProfileRowStatus = _BwProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 3, 1, 5),
    _BwProfileRowStatus_Type()
)
bwProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwProfileRowStatus.setStatus("current")
_BwProfileModify_Type = OctetString
_BwProfileModify_Object = MibTableColumn
bwProfileModify = _BwProfileModify_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 3, 1, 6),
    _BwProfileModify_Type()
)
bwProfileModify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwProfileModify.setStatus("current")
_BwProfileUstype_Type = Integer32
_BwProfileUstype_Object = MibTableColumn
bwProfileUstype = _BwProfileUstype_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 3, 1, 7),
    _BwProfileUstype_Type()
)
bwProfileUstype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwProfileUstype.setStatus("current")
_CacProfileTable_Object = MibTable
cacProfileTable = _CacProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 4)
)
if mibBuilder.loadTexts:
    cacProfileTable.setStatus("current")
_CacProfileEntry_Object = MibTableRow
cacProfileEntry = _CacProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 4, 1)
)
cacProfileEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "cacProfileName"),
)
if mibBuilder.loadTexts:
    cacProfileEntry.setStatus("current")
_CacProfileName_Type = OctetString
_CacProfileName_Object = MibTableColumn
cacProfileName = _CacProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 4, 1, 1),
    _CacProfileName_Type()
)
cacProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacProfileName.setStatus("current")


class _CacProfileMcastBw_Type(Integer32):
    """Custom type cacProfileMcastBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CacProfileMcastBw_Type.__name__ = "Integer32"
_CacProfileMcastBw_Object = MibTableColumn
cacProfileMcastBw = _CacProfileMcastBw_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 4, 1, 2),
    _CacProfileMcastBw_Type()
)
cacProfileMcastBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacProfileMcastBw.setStatus("current")
_CacProfileRowStatus_Type = RowStatus
_CacProfileRowStatus_Object = MibTableColumn
cacProfileRowStatus = _CacProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 8, 4, 1, 3),
    _CacProfileRowStatus_Type()
)
cacProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cacProfileRowStatus.setStatus("current")
_OntAlarmProfileTable_Object = MibTable
ontAlarmProfileTable = _OntAlarmProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 10)
)
if mibBuilder.loadTexts:
    ontAlarmProfileTable.setStatus("current")
_OntAlarmProfileEntry_Object = MibTableRow
ontAlarmProfileEntry = _OntAlarmProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 10, 1)
)
ontAlarmProfileEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "ontAlarmProfileName"),
)
if mibBuilder.loadTexts:
    ontAlarmProfileEntry.setStatus("current")
_OntAlarmProfileName_Type = OctetString
_OntAlarmProfileName_Object = MibTableColumn
ontAlarmProfileName = _OntAlarmProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 10, 1, 1),
    _OntAlarmProfileName_Type()
)
ontAlarmProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontAlarmProfileName.setStatus("current")
_OntAlarmProfileFeedVoltThreshLow_Type = DisplayString
_OntAlarmProfileFeedVoltThreshLow_Object = MibTableColumn
ontAlarmProfileFeedVoltThreshLow = _OntAlarmProfileFeedVoltThreshLow_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 10, 1, 2),
    _OntAlarmProfileFeedVoltThreshLow_Type()
)
ontAlarmProfileFeedVoltThreshLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAlarmProfileFeedVoltThreshLow.setStatus("current")
_OntAlarmProfileFeedVoltThreshUp_Type = DisplayString
_OntAlarmProfileFeedVoltThreshUp_Object = MibTableColumn
ontAlarmProfileFeedVoltThreshUp = _OntAlarmProfileFeedVoltThreshUp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 10, 1, 3),
    _OntAlarmProfileFeedVoltThreshUp_Type()
)
ontAlarmProfileFeedVoltThreshUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAlarmProfileFeedVoltThreshUp.setStatus("current")
_OntAlarmProfileBiasCurrThreshLow_Type = DisplayString
_OntAlarmProfileBiasCurrThreshLow_Object = MibTableColumn
ontAlarmProfileBiasCurrThreshLow = _OntAlarmProfileBiasCurrThreshLow_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 10, 1, 4),
    _OntAlarmProfileBiasCurrThreshLow_Type()
)
ontAlarmProfileBiasCurrThreshLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAlarmProfileBiasCurrThreshLow.setStatus("current")
_OntAlarmProfileBiasCurrThreshUp_Type = DisplayString
_OntAlarmProfileBiasCurrThreshUp_Object = MibTableColumn
ontAlarmProfileBiasCurrThreshUp = _OntAlarmProfileBiasCurrThreshUp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 10, 1, 5),
    _OntAlarmProfileBiasCurrThreshUp_Type()
)
ontAlarmProfileBiasCurrThreshUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAlarmProfileBiasCurrThreshUp.setStatus("current")
_OntAlarmProfileTemperatureThreshLow_Type = DisplayString
_OntAlarmProfileTemperatureThreshLow_Object = MibTableColumn
ontAlarmProfileTemperatureThreshLow = _OntAlarmProfileTemperatureThreshLow_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 10, 1, 6),
    _OntAlarmProfileTemperatureThreshLow_Type()
)
ontAlarmProfileTemperatureThreshLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAlarmProfileTemperatureThreshLow.setStatus("current")
_OntAlarmProfileTemperatureThreshUp_Type = DisplayString
_OntAlarmProfileTemperatureThreshUp_Object = MibTableColumn
ontAlarmProfileTemperatureThreshUp = _OntAlarmProfileTemperatureThreshUp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 10, 1, 7),
    _OntAlarmProfileTemperatureThreshUp_Type()
)
ontAlarmProfileTemperatureThreshUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAlarmProfileTemperatureThreshUp.setStatus("current")
_OntAlarmProfileTxPowerThreshLow_Type = DisplayString
_OntAlarmProfileTxPowerThreshLow_Object = MibTableColumn
ontAlarmProfileTxPowerThreshLow = _OntAlarmProfileTxPowerThreshLow_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 10, 1, 8),
    _OntAlarmProfileTxPowerThreshLow_Type()
)
ontAlarmProfileTxPowerThreshLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAlarmProfileTxPowerThreshLow.setStatus("current")
_OntAlarmProfileTxPowerThreshUp_Type = DisplayString
_OntAlarmProfileTxPowerThreshUp_Object = MibTableColumn
ontAlarmProfileTxPowerThreshUp = _OntAlarmProfileTxPowerThreshUp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 10, 1, 9),
    _OntAlarmProfileTxPowerThreshUp_Type()
)
ontAlarmProfileTxPowerThreshUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAlarmProfileTxPowerThreshUp.setStatus("current")
_OntAlarmProfileRowStatus_Type = RowStatus
_OntAlarmProfileRowStatus_Object = MibTableColumn
ontAlarmProfileRowStatus = _OntAlarmProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 10, 1, 10),
    _OntAlarmProfileRowStatus_Type()
)
ontAlarmProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ontAlarmProfileRowStatus.setStatus("current")
_OntAlarmProfileRxPowerThreshLow_Type = DisplayString
_OntAlarmProfileRxPowerThreshLow_Object = MibTableColumn
ontAlarmProfileRxPowerThreshLow = _OntAlarmProfileRxPowerThreshLow_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 10, 1, 11),
    _OntAlarmProfileRxPowerThreshLow_Type()
)
ontAlarmProfileRxPowerThreshLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAlarmProfileRxPowerThreshLow.setStatus("current")
_OntAlarmProfileRxPowerThreshUp_Type = DisplayString
_OntAlarmProfileRxPowerThreshUp_Object = MibTableColumn
ontAlarmProfileRxPowerThreshUp = _OntAlarmProfileRxPowerThreshUp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 10, 1, 12),
    _OntAlarmProfileRxPowerThreshUp_Type()
)
ontAlarmProfileRxPowerThreshUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAlarmProfileRxPowerThreshUp.setStatus("current")
_OntvenetTable_Object = MibTable
ontvenetTable = _OntvenetTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 11)
)
if mibBuilder.loadTexts:
    ontvenetTable.setStatus("current")
_OntvenetEntry_Object = MibTableRow
ontvenetEntry = _OntvenetEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 11, 1)
)
ontvenetEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "ontvenetCardPort"),
)
if mibBuilder.loadTexts:
    ontvenetEntry.setStatus("current")
_OntvenetCardPort_Type = Integer32
_OntvenetCardPort_Object = MibTableColumn
ontvenetCardPort = _OntvenetCardPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 11, 1, 1),
    _OntvenetCardPort_Type()
)
ontvenetCardPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ontvenetCardPort.setStatus("current")


class _PmvenetEnable_Type(Integer32):
    """Custom type pmvenetEnable based on Integer32"""
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
        *(("disable", 0),
          ("baseOnModelID", 1),
          ("bit64", 2),
          ("bit32", 3))
    )


_PmvenetEnable_Type.__name__ = "Integer32"
_PmvenetEnable_Object = MibTableColumn
pmvenetEnable = _PmvenetEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 11, 1, 2),
    _PmvenetEnable_Type()
)
pmvenetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmvenetEnable.setStatus("current")
_OntvenetRowStatus_Type = RowStatus
_OntvenetRowStatus_Object = MibTableColumn
ontvenetRowStatus = _OntvenetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 11, 1, 3),
    _OntvenetRowStatus_Type()
)
ontvenetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ontvenetRowStatus.setStatus("current")


class _OntvenetAction_Type(Integer32):
    """Custom type ontvenetAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("delAllConfig", 1))
    )


_OntvenetAction_Type.__name__ = "Integer32"
_OntvenetAction_Object = MibTableColumn
ontvenetAction = _OntvenetAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 11, 1, 4),
    _OntvenetAction_Type()
)
ontvenetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontvenetAction.setStatus("current")
_OntpotsTable_Object = MibTable
ontpotsTable = _OntpotsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 12)
)
if mibBuilder.loadTexts:
    ontpotsTable.setStatus("current")
_OntpotsEntry_Object = MibTableRow
ontpotsEntry = _OntpotsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 12, 1)
)
ontpotsEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "ontpotsCardPort"),
)
if mibBuilder.loadTexts:
    ontpotsEntry.setStatus("current")
_OntpotsCardPort_Type = Integer32
_OntpotsCardPort_Object = MibTableColumn
ontpotsCardPort = _OntpotsCardPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 12, 1, 1),
    _OntpotsCardPort_Type()
)
ontpotsCardPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ontpotsCardPort.setStatus("current")
_OntpotsRowStatus_Type = RowStatus
_OntpotsRowStatus_Object = MibTableColumn
ontpotsRowStatus = _OntpotsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 12, 1, 2),
    _OntpotsRowStatus_Type()
)
ontpotsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ontpotsRowStatus.setStatus("current")


class _OntpotsAction_Type(Integer32):
    """Custom type ontpotsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("delAllConfig", 1))
    )


_OntpotsAction_Type.__name__ = "Integer32"
_OntpotsAction_Object = MibTableColumn
ontpotsAction = _OntpotsAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 12, 1, 3),
    _OntpotsAction_Type()
)
ontpotsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontpotsAction.setStatus("current")
_OntVoipProfile_ObjectIdentity = ObjectIdentity
ontVoipProfile = _OntVoipProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13)
)
_SipProfileTable_Object = MibTable
sipProfileTable = _SipProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1)
)
if mibBuilder.loadTexts:
    sipProfileTable.setStatus("current")
_SipProfileEntry_Object = MibTableRow
sipProfileEntry = _SipProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1)
)
sipProfileEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "sipProfileName"),
)
if mibBuilder.loadTexts:
    sipProfileEntry.setStatus("current")
_SipProfileName_Type = DisplayString
_SipProfileName_Object = MibTableColumn
sipProfileName = _SipProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 1),
    _SipProfileName_Type()
)
sipProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipProfileName.setStatus("current")
_SipProfileProxyServiceAddr_Type = DisplayString
_SipProfileProxyServiceAddr_Object = MibTableColumn
sipProfileProxyServiceAddr = _SipProfileProxyServiceAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 2),
    _SipProfileProxyServiceAddr_Type()
)
sipProfileProxyServiceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileProxyServiceAddr.setStatus("current")
_SipProfileOutProxyAddr_Type = DisplayString
_SipProfileOutProxyAddr_Object = MibTableColumn
sipProfileOutProxyAddr = _SipProfileOutProxyAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 3),
    _SipProfileOutProxyAddr_Type()
)
sipProfileOutProxyAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileOutProxyAddr.setStatus("current")
_SipProfilePriDns_Type = IpAddress
_SipProfilePriDns_Object = MibTableColumn
sipProfilePriDns = _SipProfilePriDns_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 4),
    _SipProfilePriDns_Type()
)
sipProfilePriDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfilePriDns.setStatus("current")
_SipProfileSecDns_Type = IpAddress
_SipProfileSecDns_Object = MibTableColumn
sipProfileSecDns = _SipProfileSecDns_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 5),
    _SipProfileSecDns_Type()
)
sipProfileSecDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileSecDns.setStatus("current")
_SipProfileRegExpTime_Type = Integer32
_SipProfileRegExpTime_Object = MibTableColumn
sipProfileRegExpTime = _SipProfileRegExpTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 6),
    _SipProfileRegExpTime_Type()
)
sipProfileRegExpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileRegExpTime.setStatus("current")
_SipProfileReregHeadStartTime_Type = Integer32
_SipProfileReregHeadStartTime_Object = MibTableColumn
sipProfileReregHeadStartTime = _SipProfileReregHeadStartTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 7),
    _SipProfileReregHeadStartTime_Type()
)
sipProfileReregHeadStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileReregHeadStartTime.setStatus("current")
_SipProfileHostPartUri_Type = DisplayString
_SipProfileHostPartUri_Object = MibTableColumn
sipProfileHostPartUri = _SipProfileHostPartUri_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 8),
    _SipProfileHostPartUri_Type()
)
sipProfileHostPartUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileHostPartUri.setStatus("current")
_SipProfileRegistrar_Type = DisplayString
_SipProfileRegistrar_Object = MibTableColumn
sipProfileRegistrar = _SipProfileRegistrar_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 9),
    _SipProfileRegistrar_Type()
)
sipProfileRegistrar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileRegistrar.setStatus("current")
_SipProfileSoftSwitch_Type = DisplayString
_SipProfileSoftSwitch_Object = MibTableColumn
sipProfileSoftSwitch = _SipProfileSoftSwitch_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 10),
    _SipProfileSoftSwitch_Type()
)
sipProfileSoftSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileSoftSwitch.setStatus("current")


class _SipProfileCid_Type(Bits):
    """Custom type sipProfileCid based on Bits"""
    namedValues = NamedValues(
        *(("calNum", 0),
          ("calNam", 1),
          ("cidBlo", 2),
          ("cidNum", 3),
          ("cidNam", 4),
          ("acr", 5))
    )

_SipProfileCid_Type.__name__ = "Bits"
_SipProfileCid_Object = MibTableColumn
sipProfileCid = _SipProfileCid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 11),
    _SipProfileCid_Type()
)
sipProfileCid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileCid.setStatus("current")


class _SipProfileCallWait_Type(Bits):
    """Custom type sipProfileCallWait based on Bits"""
    namedValues = NamedValues(
        *(("calWai", 0),
          ("cidAnn", 1))
    )

_SipProfileCallWait_Type.__name__ = "Bits"
_SipProfileCallWait_Object = MibTableColumn
sipProfileCallWait = _SipProfileCallWait_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 12),
    _SipProfileCallWait_Type()
)
sipProfileCallWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileCallWait.setStatus("current")


class _SipProfileCallProgTrans_Type(Bits):
    """Custom type sipProfileCallProgTrans based on Bits"""
    namedValues = NamedValues(
        *(("threeWay", 0),
          ("calTra", 1),
          ("calHol", 2),
          ("calPar", 3),
          ("notDis", 4),
          ("flash", 5),
          ("origin", 6),
          ("sixWay", 7))
    )

_SipProfileCallProgTrans_Type.__name__ = "Bits"
_SipProfileCallProgTrans_Object = MibTableColumn
sipProfileCallProgTrans = _SipProfileCallProgTrans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 13),
    _SipProfileCallProgTrans_Type()
)
sipProfileCallProgTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileCallProgTrans.setStatus("current")


class _SipProfileCallPresent_Type(Bits):
    """Custom type sipProfileCallPresent based on Bits"""
    namedValues = NamedValues(
        *(("splRin", 0),
          ("diaTon", 1),
          ("visInd", 2),
          ("calFor", 3))
    )

_SipProfileCallPresent_Type.__name__ = "Bits"
_SipProfileCallPresent_Object = MibTableColumn
sipProfileCallPresent = _SipProfileCallPresent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 14),
    _SipProfileCallPresent_Type()
)
sipProfileCallPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileCallPresent.setStatus("current")


class _SipProfileDirectCon_Type(Bits):
    """Custom type sipProfileDirectCon based on Bits"""
    namedValues = NamedValues(
        *(("enable", 0),
          ("disOpt", 1))
    )

_SipProfileDirectCon_Type.__name__ = "Bits"
_SipProfileDirectCon_Object = MibTableColumn
sipProfileDirectCon = _SipProfileDirectCon_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 15),
    _SipProfileDirectCon_Type()
)
sipProfileDirectCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileDirectCon.setStatus("current")
_SipProfileDirectConUri_Type = DisplayString
_SipProfileDirectConUri_Object = MibTableColumn
sipProfileDirectConUri = _SipProfileDirectConUri_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 16),
    _SipProfileDirectConUri_Type()
)
sipProfileDirectConUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileDirectConUri.setStatus("current")
_SipProfileBridgeLineAgentUri_Type = DisplayString
_SipProfileBridgeLineAgentUri_Object = MibTableColumn
sipProfileBridgeLineAgentUri = _SipProfileBridgeLineAgentUri_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 17),
    _SipProfileBridgeLineAgentUri_Type()
)
sipProfileBridgeLineAgentUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileBridgeLineAgentUri.setStatus("current")
_SipProfileConfFactoryUri_Type = DisplayString
_SipProfileConfFactoryUri_Object = MibTableColumn
sipProfileConfFactoryUri = _SipProfileConfFactoryUri_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 18),
    _SipProfileConfFactoryUri_Type()
)
sipProfileConfFactoryUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileConfFactoryUri.setStatus("current")
_SipProfileRowStatus_Type = RowStatus
_SipProfileRowStatus_Object = MibTableColumn
sipProfileRowStatus = _SipProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 1, 1, 19),
    _SipProfileRowStatus_Type()
)
sipProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRowStatus.setStatus("current")
_CommonProfileTable_Object = MibTable
commonProfileTable = _CommonProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2)
)
if mibBuilder.loadTexts:
    commonProfileTable.setStatus("current")
_CommonProfileEntry_Object = MibTableRow
commonProfileEntry = _CommonProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1)
)
commonProfileEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "commonProfileName"),
)
if mibBuilder.loadTexts:
    commonProfileEntry.setStatus("current")
_CommonProfileName_Type = DisplayString
_CommonProfileName_Object = MibTableColumn
commonProfileName = _CommonProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 1),
    _CommonProfileName_Type()
)
commonProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonProfileName.setStatus("current")
_CommonProfileLocalPortMin_Type = Integer32
_CommonProfileLocalPortMin_Object = MibTableColumn
commonProfileLocalPortMin = _CommonProfileLocalPortMin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 2),
    _CommonProfileLocalPortMin_Type()
)
commonProfileLocalPortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfileLocalPortMin.setStatus("current")
_CommonProfileLocalPortMax_Type = Integer32
_CommonProfileLocalPortMax_Object = MibTableColumn
commonProfileLocalPortMax = _CommonProfileLocalPortMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 3),
    _CommonProfileLocalPortMax_Type()
)
commonProfileLocalPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfileLocalPortMax.setStatus("current")
_CommonProfileDscpMark_Type = Integer32
_CommonProfileDscpMark_Object = MibTableColumn
commonProfileDscpMark = _CommonProfileDscpMark_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 4),
    _CommonProfileDscpMark_Type()
)
commonProfileDscpMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfileDscpMark.setStatus("current")


class _CommonProfilePiggyback_Type(Integer32):
    """Custom type commonProfilePiggyback based on Integer32"""
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


_CommonProfilePiggyback_Type.__name__ = "Integer32"
_CommonProfilePiggyback_Object = MibTableColumn
commonProfilePiggyback = _CommonProfilePiggyback_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 5),
    _CommonProfilePiggyback_Type()
)
commonProfilePiggyback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfilePiggyback.setStatus("current")


class _CommonProfileTone_Type(Integer32):
    """Custom type commonProfileTone based on Integer32"""
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


_CommonProfileTone_Type.__name__ = "Integer32"
_CommonProfileTone_Object = MibTableColumn
commonProfileTone = _CommonProfileTone_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 6),
    _CommonProfileTone_Type()
)
commonProfileTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfileTone.setStatus("current")


class _CommonProfileDtmf_Type(Integer32):
    """Custom type commonProfileDtmf based on Integer32"""
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


_CommonProfileDtmf_Type.__name__ = "Integer32"
_CommonProfileDtmf_Object = MibTableColumn
commonProfileDtmf = _CommonProfileDtmf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 7),
    _CommonProfileDtmf_Type()
)
commonProfileDtmf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfileDtmf.setStatus("current")


class _CommonProfileCas_Type(Integer32):
    """Custom type commonProfileCas based on Integer32"""
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


_CommonProfileCas_Type.__name__ = "Integer32"
_CommonProfileCas_Object = MibTableColumn
commonProfileCas = _CommonProfileCas_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 8),
    _CommonProfileCas_Type()
)
commonProfileCas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfileCas.setStatus("current")


class _CommonProfileAnnounceType_Type(Integer32):
    """Custom type commonProfileAnnounceType based on Integer32"""
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
        *(("silence", 0),
          ("reoTon", 1),
          ("fasBus", 2),
          ("voiAnn", 3))
    )


_CommonProfileAnnounceType_Type.__name__ = "Integer32"
_CommonProfileAnnounceType_Object = MibTableColumn
commonProfileAnnounceType = _CommonProfileAnnounceType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 9),
    _CommonProfileAnnounceType_Type()
)
commonProfileAnnounceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfileAnnounceType.setStatus("current")
_CommonProfileJitterTarget_Type = Integer32
_CommonProfileJitterTarget_Object = MibTableColumn
commonProfileJitterTarget = _CommonProfileJitterTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 10),
    _CommonProfileJitterTarget_Type()
)
commonProfileJitterTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfileJitterTarget.setStatus("current")
_CommonProfileJitterBufMax_Type = Integer32
_CommonProfileJitterBufMax_Object = MibTableColumn
commonProfileJitterBufMax = _CommonProfileJitterBufMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 11),
    _CommonProfileJitterBufMax_Type()
)
commonProfileJitterBufMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfileJitterBufMax.setStatus("current")


class _CommonProfileEchoCancel_Type(Integer32):
    """Custom type commonProfileEchoCancel based on Integer32"""
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


_CommonProfileEchoCancel_Type.__name__ = "Integer32"
_CommonProfileEchoCancel_Object = MibTableColumn
commonProfileEchoCancel = _CommonProfileEchoCancel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 12),
    _CommonProfileEchoCancel_Type()
)
commonProfileEchoCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfileEchoCancel.setStatus("current")
_CommonProfilePstnProtocol_Type = Integer32
_CommonProfilePstnProtocol_Object = MibTableColumn
commonProfilePstnProtocol = _CommonProfilePstnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 13),
    _CommonProfilePstnProtocol_Type()
)
commonProfilePstnProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfilePstnProtocol.setStatus("current")


class _CommonProfileFaxMode_Type(Integer32):
    """Custom type commonProfileFaxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("passthru", 0),
          ("t38", 1))
    )


_CommonProfileFaxMode_Type.__name__ = "Integer32"
_CommonProfileFaxMode_Object = MibTableColumn
commonProfileFaxMode = _CommonProfileFaxMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 14),
    _CommonProfileFaxMode_Type()
)
commonProfileFaxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfileFaxMode.setStatus("current")


class _CommonProfile1stCodec_Type(Integer32):
    """Custom type commonProfile1stCodec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("pcmu", 0),
          ("gsm", 3),
          ("g723", 4),
          ("dvi48000", 5),
          ("dvi416000", 6),
          ("lpc", 7),
          ("pcma", 8),
          ("g722", 9),
          ("l162", 10),
          ("l161", 11),
          ("qcelp", 12),
          ("cn", 13),
          ("mpa", 14),
          ("g728", 15),
          ("dvi411025", 16),
          ("dvi422050", 17),
          ("g729", 18))
    )


_CommonProfile1stCodec_Type.__name__ = "Integer32"
_CommonProfile1stCodec_Object = MibTableColumn
commonProfile1stCodec = _CommonProfile1stCodec_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 15),
    _CommonProfile1stCodec_Type()
)
commonProfile1stCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfile1stCodec.setStatus("current")


class _CommonProfile2ndCodec_Type(Integer32):
    """Custom type commonProfile2ndCodec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("pcmu", 0),
          ("gsm", 3),
          ("g723", 4),
          ("dvi48000", 5),
          ("dvi416000", 6),
          ("lpc", 7),
          ("pcma", 8),
          ("g722", 9),
          ("l162", 10),
          ("l161", 11),
          ("qcelp", 12),
          ("cn", 13),
          ("mpa", 14),
          ("g728", 15),
          ("dvi411025", 16),
          ("dvi422050", 17),
          ("g729", 18))
    )


_CommonProfile2ndCodec_Type.__name__ = "Integer32"
_CommonProfile2ndCodec_Object = MibTableColumn
commonProfile2ndCodec = _CommonProfile2ndCodec_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 16),
    _CommonProfile2ndCodec_Type()
)
commonProfile2ndCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfile2ndCodec.setStatus("current")


class _CommonProfile3rdCodec_Type(Integer32):
    """Custom type commonProfile3rdCodec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("pcmu", 0),
          ("gsm", 3),
          ("g723", 4),
          ("dvi48000", 5),
          ("dvi416000", 6),
          ("lpc", 7),
          ("pcma", 8),
          ("g722", 9),
          ("l162", 10),
          ("l161", 11),
          ("qcelp", 12),
          ("cn", 13),
          ("mpa", 14),
          ("g728", 15),
          ("dvi411025", 16),
          ("dvi422050", 17),
          ("g729", 18))
    )


_CommonProfile3rdCodec_Type.__name__ = "Integer32"
_CommonProfile3rdCodec_Object = MibTableColumn
commonProfile3rdCodec = _CommonProfile3rdCodec_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 17),
    _CommonProfile3rdCodec_Type()
)
commonProfile3rdCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfile3rdCodec.setStatus("current")


class _CommonProfile4thCodec_Type(Integer32):
    """Custom type commonProfile4thCodec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("pcmu", 0),
          ("gsm", 3),
          ("g723", 4),
          ("dvi48000", 5),
          ("dvi416000", 6),
          ("lpc", 7),
          ("pcma", 8),
          ("g722", 9),
          ("l162", 10),
          ("l161", 11),
          ("qcelp", 12),
          ("cn", 13),
          ("mpa", 14),
          ("g728", 15),
          ("dvi411025", 16),
          ("dvi422050", 17),
          ("g729", 18))
    )


_CommonProfile4thCodec_Type.__name__ = "Integer32"
_CommonProfile4thCodec_Object = MibTableColumn
commonProfile4thCodec = _CommonProfile4thCodec_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 18),
    _CommonProfile4thCodec_Type()
)
commonProfile4thCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfile4thCodec.setStatus("current")
_CommonProfile1stPacketPeriod_Type = Integer32
_CommonProfile1stPacketPeriod_Object = MibTableColumn
commonProfile1stPacketPeriod = _CommonProfile1stPacketPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 19),
    _CommonProfile1stPacketPeriod_Type()
)
commonProfile1stPacketPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfile1stPacketPeriod.setStatus("current")
_CommonProfile2ndPacketPeriod_Type = Integer32
_CommonProfile2ndPacketPeriod_Object = MibTableColumn
commonProfile2ndPacketPeriod = _CommonProfile2ndPacketPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 20),
    _CommonProfile2ndPacketPeriod_Type()
)
commonProfile2ndPacketPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfile2ndPacketPeriod.setStatus("current")
_CommonProfile3rdPacketPeriod_Type = Integer32
_CommonProfile3rdPacketPeriod_Object = MibTableColumn
commonProfile3rdPacketPeriod = _CommonProfile3rdPacketPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 21),
    _CommonProfile3rdPacketPeriod_Type()
)
commonProfile3rdPacketPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfile3rdPacketPeriod.setStatus("current")
_CommonProfile4thPacketPeriod_Type = Integer32
_CommonProfile4thPacketPeriod_Object = MibTableColumn
commonProfile4thPacketPeriod = _CommonProfile4thPacketPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 22),
    _CommonProfile4thPacketPeriod_Type()
)
commonProfile4thPacketPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfile4thPacketPeriod.setStatus("current")


class _CommonProfile1stSilence_Type(Integer32):
    """Custom type commonProfile1stSilence based on Integer32"""
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


_CommonProfile1stSilence_Type.__name__ = "Integer32"
_CommonProfile1stSilence_Object = MibTableColumn
commonProfile1stSilence = _CommonProfile1stSilence_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 23),
    _CommonProfile1stSilence_Type()
)
commonProfile1stSilence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfile1stSilence.setStatus("current")


class _CommonProfile2ndSilence_Type(Integer32):
    """Custom type commonProfile2ndSilence based on Integer32"""
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


_CommonProfile2ndSilence_Type.__name__ = "Integer32"
_CommonProfile2ndSilence_Object = MibTableColumn
commonProfile2ndSilence = _CommonProfile2ndSilence_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 24),
    _CommonProfile2ndSilence_Type()
)
commonProfile2ndSilence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfile2ndSilence.setStatus("current")


class _CommonProfile3rdSilence_Type(Integer32):
    """Custom type commonProfile3rdSilence based on Integer32"""
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


_CommonProfile3rdSilence_Type.__name__ = "Integer32"
_CommonProfile3rdSilence_Object = MibTableColumn
commonProfile3rdSilence = _CommonProfile3rdSilence_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 25),
    _CommonProfile3rdSilence_Type()
)
commonProfile3rdSilence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfile3rdSilence.setStatus("current")


class _CommonProfile4thSilence_Type(Integer32):
    """Custom type commonProfile4thSilence based on Integer32"""
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


_CommonProfile4thSilence_Type.__name__ = "Integer32"
_CommonProfile4thSilence_Object = MibTableColumn
commonProfile4thSilence = _CommonProfile4thSilence_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 26),
    _CommonProfile4thSilence_Type()
)
commonProfile4thSilence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfile4thSilence.setStatus("current")


class _CommonProfileOobDtmf_Type(Integer32):
    """Custom type commonProfileOobDtmf based on Integer32"""
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


_CommonProfileOobDtmf_Type.__name__ = "Integer32"
_CommonProfileOobDtmf_Object = MibTableColumn
commonProfileOobDtmf = _CommonProfileOobDtmf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 27),
    _CommonProfileOobDtmf_Type()
)
commonProfileOobDtmf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfileOobDtmf.setStatus("current")
_CommonProfileRowStatus_Type = RowStatus
_CommonProfileRowStatus_Object = MibTableColumn
commonProfileRowStatus = _CommonProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 28),
    _CommonProfileRowStatus_Type()
)
commonProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    commonProfileRowStatus.setStatus("current")


class _CommonProfileSignalCode_Type(Integer32):
    """Custom type commonProfileSignalCode based on Integer32"""
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
        *(("loopStart", 0),
          ("groundStart", 1),
          ("loopReverseBattery", 2),
          ("coinFirst", 3),
          ("dialToneFirst", 4),
          ("multiparty", 5))
    )


_CommonProfileSignalCode_Type.__name__ = "Integer32"
_CommonProfileSignalCode_Object = MibTableColumn
commonProfileSignalCode = _CommonProfileSignalCode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 2, 1, 29),
    _CommonProfileSignalCode_Type()
)
commonProfileSignalCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProfileSignalCode.setStatus("current")
_DialPlan_ObjectIdentity = ObjectIdentity
dialPlan = _DialPlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 3)
)
_DialPlanCommTable_Object = MibTable
dialPlanCommTable = _DialPlanCommTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 3, 1)
)
if mibBuilder.loadTexts:
    dialPlanCommTable.setStatus("current")
_DialPlanCommEntry_Object = MibTableRow
dialPlanCommEntry = _DialPlanCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 3, 1, 1)
)
dialPlanCommEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "dialPlanCommName"),
)
if mibBuilder.loadTexts:
    dialPlanCommEntry.setStatus("current")
_DialPlanCommName_Type = DisplayString
_DialPlanCommName_Object = MibTableColumn
dialPlanCommName = _DialPlanCommName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 3, 1, 1, 1),
    _DialPlanCommName_Type()
)
dialPlanCommName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialPlanCommName.setStatus("current")
_DialPlanCommMaxSize_Type = Integer32
_DialPlanCommMaxSize_Object = MibTableColumn
dialPlanCommMaxSize = _DialPlanCommMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 3, 1, 1, 2),
    _DialPlanCommMaxSize_Type()
)
dialPlanCommMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialPlanCommMaxSize.setStatus("current")
_DialPlanCommCriticalTimeout_Type = Integer32
_DialPlanCommCriticalTimeout_Object = MibTableColumn
dialPlanCommCriticalTimeout = _DialPlanCommCriticalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 3, 1, 1, 3),
    _DialPlanCommCriticalTimeout_Type()
)
dialPlanCommCriticalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialPlanCommCriticalTimeout.setStatus("current")
_DialPlanCommPartialTimeout_Type = Integer32
_DialPlanCommPartialTimeout_Object = MibTableColumn
dialPlanCommPartialTimeout = _DialPlanCommPartialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 3, 1, 1, 4),
    _DialPlanCommPartialTimeout_Type()
)
dialPlanCommPartialTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialPlanCommPartialTimeout.setStatus("current")


class _DialPlanCommFormat_Type(Integer32):
    """Custom type dialPlanCommFormat based on Integer32"""
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
        *(("notDefined", 0),
          ("h248", 1),
          ("nsc", 2),
          ("vendorSpecific", 3))
    )


_DialPlanCommFormat_Type.__name__ = "Integer32"
_DialPlanCommFormat_Object = MibTableColumn
dialPlanCommFormat = _DialPlanCommFormat_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 3, 1, 1, 5),
    _DialPlanCommFormat_Type()
)
dialPlanCommFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialPlanCommFormat.setStatus("current")
_DialPlanCommRowStatus_Type = RowStatus
_DialPlanCommRowStatus_Object = MibTableColumn
dialPlanCommRowStatus = _DialPlanCommRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 3, 1, 1, 6),
    _DialPlanCommRowStatus_Type()
)
dialPlanCommRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialPlanCommRowStatus.setStatus("current")
_DialPlanContTable_Object = MibTable
dialPlanContTable = _DialPlanContTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 3, 2)
)
if mibBuilder.loadTexts:
    dialPlanContTable.setStatus("current")
_DialPlanContEntry_Object = MibTableRow
dialPlanContEntry = _DialPlanContEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 3, 2, 1)
)
dialPlanContEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "dialPlanContName"),
    (0, "ZYXEL-olt1408-MIB", "dialPlanContId"),
)
if mibBuilder.loadTexts:
    dialPlanContEntry.setStatus("current")
_DialPlanContName_Type = OctetString
_DialPlanContName_Object = MibTableColumn
dialPlanContName = _DialPlanContName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 3, 2, 1, 1),
    _DialPlanContName_Type()
)
dialPlanContName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialPlanContName.setStatus("current")
_DialPlanContId_Type = Integer32
_DialPlanContId_Object = MibTableColumn
dialPlanContId = _DialPlanContId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 3, 2, 1, 2),
    _DialPlanContId_Type()
)
dialPlanContId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialPlanContId.setStatus("current")
_DialPlanContToken_Type = OctetString
_DialPlanContToken_Object = MibTableColumn
dialPlanContToken = _DialPlanContToken_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 3, 2, 1, 3),
    _DialPlanContToken_Type()
)
dialPlanContToken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialPlanContToken.setStatus("current")
_DialPlanContRowStatus_Type = RowStatus
_DialPlanContRowStatus_Object = MibTableColumn
dialPlanContRowStatus = _DialPlanContRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 13, 3, 2, 1, 4),
    _DialPlanContRowStatus_Type()
)
dialPlanContRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialPlanContRowStatus.setStatus("current")
_OntvideoTable_Object = MibTable
ontvideoTable = _OntvideoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 14)
)
if mibBuilder.loadTexts:
    ontvideoTable.setStatus("current")
_OntvideoEntry_Object = MibTableRow
ontvideoEntry = _OntvideoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 14, 1)
)
ontvideoEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "ontvideoPort"),
)
if mibBuilder.loadTexts:
    ontvideoEntry.setStatus("current")
_OntvideoPort_Type = Integer32
_OntvideoPort_Object = MibTableColumn
ontvideoPort = _OntvideoPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 14, 1, 1),
    _OntvideoPort_Type()
)
ontvideoPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ontvideoPort.setStatus("current")
_OntvideoRowStatus_Type = RowStatus
_OntvideoRowStatus_Object = MibTableColumn
ontvideoRowStatus = _OntvideoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 14, 1, 2),
    _OntvideoRowStatus_Type()
)
ontvideoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ontvideoRowStatus.setStatus("current")


class _OntvideoAction_Type(Integer32):
    """Custom type ontvideoAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("delAllConfig", 1))
    )


_OntvideoAction_Type.__name__ = "Integer32"
_OntvideoAction_Object = MibTableColumn
ontvideoAction = _OntvideoAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 14, 1, 3),
    _OntvideoAction_Type()
)
ontvideoAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontvideoAction.setStatus("current")
_OnuVendorVersion_ObjectIdentity = ObjectIdentity
onuVendorVersion = _OnuVendorVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 15)
)
_OnuVendorVersionTable_Object = MibTable
onuVendorVersionTable = _OnuVendorVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 15, 1)
)
if mibBuilder.loadTexts:
    onuVendorVersionTable.setStatus("current")
_OnuVendorVersionEntry_Object = MibTableRow
onuVendorVersionEntry = _OnuVendorVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 15, 1, 1)
)
onuVendorVersionEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "onuVendorVersionModelName"),
)
if mibBuilder.loadTexts:
    onuVendorVersionEntry.setStatus("current")
_OnuVendorVersionName_Type = OctetString
_OnuVendorVersionName_Object = MibTableColumn
onuVendorVersionName = _OnuVendorVersionName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 15, 1, 1, 1),
    _OnuVendorVersionName_Type()
)
onuVendorVersionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVendorVersionName.setStatus("current")
_OnuVendorVersionSoftwareVer_Type = OctetString
_OnuVendorVersionSoftwareVer_Object = MibTableColumn
onuVendorVersionSoftwareVer = _OnuVendorVersionSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 15, 1, 1, 2),
    _OnuVendorVersionSoftwareVer_Type()
)
onuVendorVersionSoftwareVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVendorVersionSoftwareVer.setStatus("current")
_OnuVendorVersionModelName_Type = OctetString
_OnuVendorVersionModelName_Object = MibTableColumn
onuVendorVersionModelName = _OnuVendorVersionModelName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 15, 1, 1, 3),
    _OnuVendorVersionModelName_Type()
)
onuVendorVersionModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuVendorVersionModelName.setStatus("current")


class _OnuVendorVersionModelID_Type(Integer32):
    """Custom type onuVendorVersionModelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_OnuVendorVersionModelID_Type.__name__ = "Integer32"
_OnuVendorVersionModelID_Object = MibTableColumn
onuVendorVersionModelID = _OnuVendorVersionModelID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 15, 1, 1, 4),
    _OnuVendorVersionModelID_Type()
)
onuVendorVersionModelID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVendorVersionModelID.setStatus("current")


class _OnuVendorVersionCard1_Type(Integer32):
    """Custom type onuVendorVersionCard1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OnuVendorVersionCard1_Type.__name__ = "Integer32"
_OnuVendorVersionCard1_Object = MibTableColumn
onuVendorVersionCard1 = _OnuVendorVersionCard1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 15, 1, 1, 5),
    _OnuVendorVersionCard1_Type()
)
onuVendorVersionCard1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVendorVersionCard1.setStatus("current")


class _OnuVendorVersionCard2_Type(Integer32):
    """Custom type onuVendorVersionCard2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OnuVendorVersionCard2_Type.__name__ = "Integer32"
_OnuVendorVersionCard2_Object = MibTableColumn
onuVendorVersionCard2 = _OnuVendorVersionCard2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 15, 1, 1, 6),
    _OnuVendorVersionCard2_Type()
)
onuVendorVersionCard2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVendorVersionCard2.setStatus("current")


class _OnuVendorVersionCard3_Type(Integer32):
    """Custom type onuVendorVersionCard3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OnuVendorVersionCard3_Type.__name__ = "Integer32"
_OnuVendorVersionCard3_Object = MibTableColumn
onuVendorVersionCard3 = _OnuVendorVersionCard3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 15, 1, 1, 7),
    _OnuVendorVersionCard3_Type()
)
onuVendorVersionCard3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVendorVersionCard3.setStatus("current")


class _OnuVendorVersionCard4_Type(Integer32):
    """Custom type onuVendorVersionCard4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OnuVendorVersionCard4_Type.__name__ = "Integer32"
_OnuVendorVersionCard4_Object = MibTableColumn
onuVendorVersionCard4 = _OnuVendorVersionCard4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 15, 1, 1, 8),
    _OnuVendorVersionCard4_Type()
)
onuVendorVersionCard4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVendorVersionCard4.setStatus("current")


class _OnuVendorVersionCard5_Type(Integer32):
    """Custom type onuVendorVersionCard5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OnuVendorVersionCard5_Type.__name__ = "Integer32"
_OnuVendorVersionCard5_Object = MibTableColumn
onuVendorVersionCard5 = _OnuVendorVersionCard5_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 15, 1, 1, 9),
    _OnuVendorVersionCard5_Type()
)
onuVendorVersionCard5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuVendorVersionCard5.setStatus("current")
_OnuVendorVersionRowStatus_Type = RowStatus
_OnuVendorVersionRowStatus_Object = MibTableColumn
onuVendorVersionRowStatus = _OnuVendorVersionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 15, 1, 1, 10),
    _OnuVendorVersionRowStatus_Type()
)
onuVendorVersionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuVendorVersionRowStatus.setStatus("current")
_OntPmRateTable_Object = MibTable
ontPmRateTable = _OntPmRateTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 16)
)
if mibBuilder.loadTexts:
    ontPmRateTable.setStatus("current")
_OntPmRateEntry_Object = MibTableRow
ontPmRateEntry = _OntPmRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 16, 1)
)
ontPmRateEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "ontPmRateIndex"),
)
if mibBuilder.loadTexts:
    ontPmRateEntry.setStatus("current")
_OntPmRateDot1dBasePort_Type = Integer32
_OntPmRateDot1dBasePort_Object = MibTableColumn
ontPmRateDot1dBasePort = _OntPmRateDot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 16, 1, 1),
    _OntPmRateDot1dBasePort_Type()
)
ontPmRateDot1dBasePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontPmRateDot1dBasePort.setStatus("current")
_OntPmRateOnt_Type = Integer32
_OntPmRateOnt_Object = MibTableColumn
ontPmRateOnt = _OntPmRateOnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 16, 1, 2),
    _OntPmRateOnt_Type()
)
ontPmRateOnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontPmRateOnt.setStatus("current")


class _OntPmRateMonitor_Type(Integer32):
    """Custom type ontPmRateMonitor based on Integer32"""
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


_OntPmRateMonitor_Type.__name__ = "Integer32"
_OntPmRateMonitor_Object = MibTableColumn
ontPmRateMonitor = _OntPmRateMonitor_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 16, 1, 3),
    _OntPmRateMonitor_Type()
)
ontPmRateMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontPmRateMonitor.setStatus("current")
_OntPmRateIndex_Type = Integer32
_OntPmRateIndex_Object = MibTableColumn
ontPmRateIndex = _OntPmRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 16, 1, 4),
    _OntPmRateIndex_Type()
)
ontPmRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ontPmRateIndex.setStatus("current")
_OntAclProfileTable_Object = MibTable
ontAclProfileTable = _OntAclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 17)
)
if mibBuilder.loadTexts:
    ontAclProfileTable.setStatus("current")
_OntAclProfileEntry_Object = MibTableRow
ontAclProfileEntry = _OntAclProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 17, 1)
)
ontAclProfileEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "ontAclProfileName"),
)
if mibBuilder.loadTexts:
    ontAclProfileEntry.setStatus("current")
_OntAclProfileName_Type = OctetString
_OntAclProfileName_Object = MibTableColumn
ontAclProfileName = _OntAclProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 17, 1, 1),
    _OntAclProfileName_Type()
)
ontAclProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontAclProfileName.setStatus("current")


class _OntAclProfileEnable_Type(Integer32):
    """Custom type ontAclProfileEnable based on Integer32"""
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


_OntAclProfileEnable_Type.__name__ = "Integer32"
_OntAclProfileEnable_Object = MibTableColumn
ontAclProfileEnable = _OntAclProfileEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 17, 1, 2),
    _OntAclProfileEnable_Type()
)
ontAclProfileEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAclProfileEnable.setStatus("current")


class _OntAclProfilePolicy_Type(Integer32):
    """Custom type ontAclProfilePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("drop", 0),
          ("trust", 1))
    )


_OntAclProfilePolicy_Type.__name__ = "Integer32"
_OntAclProfilePolicy_Object = MibTableColumn
ontAclProfilePolicy = _OntAclProfilePolicy_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 17, 1, 3),
    _OntAclProfilePolicy_Type()
)
ontAclProfilePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAclProfilePolicy.setStatus("current")


class _OntAclProfileInterface_Type(Integer32):
    """Custom type ontAclProfileInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan", 0),
          ("wan", 1),
          ("both", 2))
    )


_OntAclProfileInterface_Type.__name__ = "Integer32"
_OntAclProfileInterface_Object = MibTableColumn
ontAclProfileInterface = _OntAclProfileInterface_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 17, 1, 4),
    _OntAclProfileInterface_Type()
)
ontAclProfileInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAclProfileInterface.setStatus("current")


class _OntAclProfileIpProtocol_Type(Integer32):
    """Custom type ontAclProfileIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OntAclProfileIpProtocol_Type.__name__ = "Integer32"
_OntAclProfileIpProtocol_Object = MibTableColumn
ontAclProfileIpProtocol = _OntAclProfileIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 17, 1, 5),
    _OntAclProfileIpProtocol_Type()
)
ontAclProfileIpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAclProfileIpProtocol.setStatus("current")


class _OntAclProfileSourceL4Port_Type(Integer32):
    """Custom type ontAclProfileSourceL4Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OntAclProfileSourceL4Port_Type.__name__ = "Integer32"
_OntAclProfileSourceL4Port_Object = MibTableColumn
ontAclProfileSourceL4Port = _OntAclProfileSourceL4Port_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 17, 1, 6),
    _OntAclProfileSourceL4Port_Type()
)
ontAclProfileSourceL4Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAclProfileSourceL4Port.setStatus("current")


class _OntAclProfileDestinationL4Port_Type(Integer32):
    """Custom type ontAclProfileDestinationL4Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OntAclProfileDestinationL4Port_Type.__name__ = "Integer32"
_OntAclProfileDestinationL4Port_Object = MibTableColumn
ontAclProfileDestinationL4Port = _OntAclProfileDestinationL4Port_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 17, 1, 7),
    _OntAclProfileDestinationL4Port_Type()
)
ontAclProfileDestinationL4Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAclProfileDestinationL4Port.setStatus("current")
_OntAclProfileSourceIpAddress_Type = IpAddress
_OntAclProfileSourceIpAddress_Object = MibTableColumn
ontAclProfileSourceIpAddress = _OntAclProfileSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 17, 1, 8),
    _OntAclProfileSourceIpAddress_Type()
)
ontAclProfileSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAclProfileSourceIpAddress.setStatus("current")


class _OntAclProfileSourceIpMask_Type(Integer32):
    """Custom type ontAclProfileSourceIpMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_OntAclProfileSourceIpMask_Type.__name__ = "Integer32"
_OntAclProfileSourceIpMask_Object = MibTableColumn
ontAclProfileSourceIpMask = _OntAclProfileSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 17, 1, 9),
    _OntAclProfileSourceIpMask_Type()
)
ontAclProfileSourceIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAclProfileSourceIpMask.setStatus("current")
_OntAclProfileDestinationIpAddress_Type = IpAddress
_OntAclProfileDestinationIpAddress_Object = MibTableColumn
ontAclProfileDestinationIpAddress = _OntAclProfileDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 17, 1, 10),
    _OntAclProfileDestinationIpAddress_Type()
)
ontAclProfileDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAclProfileDestinationIpAddress.setStatus("current")


class _OntAclProfileDestinationIpMask_Type(Integer32):
    """Custom type ontAclProfileDestinationIpMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_OntAclProfileDestinationIpMask_Type.__name__ = "Integer32"
_OntAclProfileDestinationIpMask_Object = MibTableColumn
ontAclProfileDestinationIpMask = _OntAclProfileDestinationIpMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 17, 1, 11),
    _OntAclProfileDestinationIpMask_Type()
)
ontAclProfileDestinationIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAclProfileDestinationIpMask.setStatus("current")
_OntAclProfileSourceMacAddress_Type = MacAddress
_OntAclProfileSourceMacAddress_Object = MibTableColumn
ontAclProfileSourceMacAddress = _OntAclProfileSourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 17, 1, 12),
    _OntAclProfileSourceMacAddress_Type()
)
ontAclProfileSourceMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAclProfileSourceMacAddress.setStatus("current")
_OntAclProfileDestinationMacAddress_Type = MacAddress
_OntAclProfileDestinationMacAddress_Object = MibTableColumn
ontAclProfileDestinationMacAddress = _OntAclProfileDestinationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 17, 1, 13),
    _OntAclProfileDestinationMacAddress_Type()
)
ontAclProfileDestinationMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontAclProfileDestinationMacAddress.setStatus("current")
_OntAclProfileRowStatus_Type = RowStatus
_OntAclProfileRowStatus_Object = MibTableColumn
ontAclProfileRowStatus = _OntAclProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 135, 17, 1, 14),
    _OntAclProfileRowStatus_Type()
)
ontAclProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ontAclProfileRowStatus.setStatus("current")
_RemoteOntInfo_ObjectIdentity = ObjectIdentity
remoteOntInfo = _RemoteOntInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136)
)
_PonStatusTable_Object = MibTable
ponStatusTable = _PonStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 2)
)
if mibBuilder.loadTexts:
    ponStatusTable.setStatus("current")
_PonStatusEntry_Object = MibTableRow
ponStatusEntry = _PonStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 2, 1)
)
ponStatusEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    ponStatusEntry.setStatus("current")


class _State_Type(Integer32):
    """Custom type state based on Integer32"""
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


_State_Type.__name__ = "Integer32"
_State_Object = MibTableColumn
state = _State_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 2, 1, 1),
    _State_Type()
)
state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    state.setStatus("current")


class _OltKeyExchange_Type(Integer32):
    """Custom type oltKeyExchange based on Integer32"""
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


_OltKeyExchange_Type.__name__ = "Integer32"
_OltKeyExchange_Object = MibTableColumn
oltKeyExchange = _OltKeyExchange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 2, 1, 2),
    _OltKeyExchange_Type()
)
oltKeyExchange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltKeyExchange.setStatus("current")


class _SnAcq_Type(Integer32):
    """Custom type snAcq based on Integer32"""
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


_SnAcq_Type.__name__ = "Integer32"
_SnAcq_Object = MibTableColumn
snAcq = _SnAcq_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 2, 1, 3),
    _SnAcq_Type()
)
snAcq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAcq.setStatus("current")


class _RogueDectect_Type(Integer32):
    """Custom type rogueDectect based on Integer32"""
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


_RogueDectect_Type.__name__ = "Integer32"
_RogueDectect_Object = MibTableColumn
rogueDectect = _RogueDectect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 2, 1, 4),
    _RogueDectect_Type()
)
rogueDectect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueDectect.setStatus("current")


class _RogueDestructState_Type(Integer32):
    """Custom type rogueDestructState based on Integer32"""
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


_RogueDestructState_Type.__name__ = "Integer32"
_RogueDestructState_Object = MibTableColumn
rogueDestructState = _RogueDestructState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 2, 1, 5),
    _RogueDestructState_Type()
)
rogueDestructState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueDestructState.setStatus("current")
_ProcInterval_Type = Integer32
_ProcInterval_Object = MibTableColumn
procInterval = _ProcInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 2, 1, 6),
    _ProcInterval_Type()
)
procInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procInterval.setStatus("current")
_ProcIntervalSec_Type = Integer32
_ProcIntervalSec_Object = MibTableColumn
procIntervalSec = _ProcIntervalSec_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 2, 1, 7),
    _ProcIntervalSec_Type()
)
procIntervalSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procIntervalSec.setStatus("current")


class _Los_Type(Integer32):
    """Custom type los based on Integer32"""
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


_Los_Type.__name__ = "Integer32"
_Los_Object = MibTableColumn
los = _Los_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 2, 1, 8),
    _Los_Type()
)
los.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    los.setStatus("current")
_Last_Type = Integer32
_Last_Object = MibTableColumn
last = _Last_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 2, 1, 9),
    _Last_Type()
)
last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    last.setStatus("current")
_EndOfBurstOffset_Type = Integer32
_EndOfBurstOffset_Object = MibTableColumn
endOfBurstOffset = _EndOfBurstOffset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 2, 1, 10),
    _EndOfBurstOffset_Type()
)
endOfBurstOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfBurstOffset.setStatus("current")
_OntStatusTable_ObjectIdentity = ObjectIdentity
ontStatusTable = _OntStatusTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3)
)
_OntCurrentStatusTable_Object = MibTable
ontCurrentStatusTable = _OntCurrentStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 1)
)
if mibBuilder.loadTexts:
    ontCurrentStatusTable.setStatus("current")
_OntCurrentStatusEntry_Object = MibTableRow
ontCurrentStatusEntry = _OntCurrentStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 1, 1)
)
ontCurrentStatusEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
)
if mibBuilder.loadTexts:
    ontCurrentStatusEntry.setStatus("current")
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibTableColumn
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 1, 1, 1),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_PasswordOnt_Type = DisplayString
_PasswordOnt_Object = MibTableColumn
passwordOnt = _PasswordOnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 1, 1, 2),
    _PasswordOnt_Type()
)
passwordOnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passwordOnt.setStatus("current")
_OntStatus_Type = RemoteOnuStatus
_OntStatus_Object = MibTableColumn
ontStatus = _OntStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 1, 1, 3),
    _OntStatus_Type()
)
ontStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontStatus.setStatus("current")
_VersionA_Type = DisplayString
_VersionA_Object = MibTableColumn
versionA = _VersionA_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 1, 1, 4),
    _VersionA_Type()
)
versionA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionA.setStatus("current")
_VersionB_Type = DisplayString
_VersionB_Object = MibTableColumn
versionB = _VersionB_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 1, 1, 5),
    _VersionB_Type()
)
versionB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionB.setStatus("current")


class _ActVersion_Type(Integer32):
    """Custom type actVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("versionA", 1),
          ("versionB", 2))
    )


_ActVersion_Type.__name__ = "Integer32"
_ActVersion_Object = MibTableColumn
actVersion = _ActVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 1, 1, 6),
    _ActVersion_Type()
)
actVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actVersion.setStatus("current")
_EstimatedDistance_Type = Unsigned32
_EstimatedDistance_Object = MibTableColumn
estimatedDistance = _EstimatedDistance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 1, 1, 7),
    _EstimatedDistance_Type()
)
estimatedDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    estimatedDistance.setStatus("current")
if mibBuilder.loadTexts:
    estimatedDistance.setUnits("meter")


class _PppoeStatus_Type(Integer32):
    """Custom type pppoeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1),
          ("notAvailable", 2))
    )


_PppoeStatus_Type.__name__ = "Integer32"
_PppoeStatus_Object = MibTableColumn
pppoeStatus = _PppoeStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 1, 1, 8),
    _PppoeStatus_Type()
)
pppoeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeStatus.setStatus("current")
_OnuVersion_Type = DisplayString
_OnuVersion_Object = MibTableColumn
onuVersion = _OnuVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 1, 1, 9),
    _OnuVersion_Type()
)
onuVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuVersion.setStatus("current")
_WanIp_Type = IpAddress
_WanIp_Object = MibTableColumn
wanIp = _WanIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 1, 1, 10),
    _WanIp_Type()
)
wanIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIp.setStatus("current")
_OntStatusElapsedTime_Type = Unsigned32
_OntStatusElapsedTime_Object = MibTableColumn
ontStatusElapsedTime = _OntStatusElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 1, 1, 11),
    _OntStatusElapsedTime_Type()
)
ontStatusElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontStatusElapsedTime.setStatus("current")
_OnuModelName_Type = DisplayString
_OnuModelName_Object = MibTableColumn
onuModelName = _OnuModelName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 1, 1, 12),
    _OnuModelName_Type()
)
onuModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuModelName.setStatus("current")


class _OnuModelId_Type(Integer32):
    """Custom type onuModelId based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("pmg1006ORpmg2006ORpmg1005ORpmg2005", 1),
          ("pmg5318b20a", 2),
          ("pmg3000b20a", 3),
          ("na1", 4),
          ("gpt2542gnaucORpmg5318b20bORpmg5318b20cORpmg5317ORpmg5323", 5),
          ("o00xx0vpq", 6),
          ("na2", 7),
          ("gpt2820gnORgpt2840gnORgpt2841hntORgpt2840hnt", 8))
    )


_OnuModelId_Type.__name__ = "Integer32"
_OnuModelId_Object = MibTableColumn
onuModelId = _OnuModelId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 1, 1, 13),
    _OnuModelId_Type()
)
onuModelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuModelId.setStatus("current")


class _UpgradeStatus_Type(Integer32):
    """Custom type upgradeStatus based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("matched", 1),
          ("downloading", 2),
          ("successful", 3),
          ("failed", 4),
          ("failedWhtiOntDown", 5),
          ("notFoundTheMatchImage", 6),
          ("noPlannedVer", 7),
          ("timeout", 8),
          ("ontNotReady", 9),
          ("swdlQueueFull", 10),
          ("inDownloadingQueue", 11),
          ("inWaitingQueue", 12),
          ("mismatched", 13),
          ("changeToImage1", 14),
          ("changeToImage2", 15),
          ("noImage", 16),
          ("alreadySuccess", 17),
          ("alreadyChangeToImage1", 18),
          ("alreadyChangeToImage2", 19),
          ("ontProcessing", 20))
    )


_UpgradeStatus_Type.__name__ = "Integer32"
_UpgradeStatus_Object = MibTableColumn
upgradeStatus = _UpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 1, 1, 14),
    _UpgradeStatus_Type()
)
upgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeStatus.setStatus("current")
_OntCountersTable_Object = MibTable
ontCountersTable = _OntCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 4)
)
if mibBuilder.loadTexts:
    ontCountersTable.setStatus("current")
_OntCountersEntry_Object = MibTableRow
ontCountersEntry = _OntCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 4, 1)
)
ontCountersEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
)
if mibBuilder.loadTexts:
    ontCountersEntry.setStatus("current")
_OntCountersUnreceivedBursts_Type = Counter32
_OntCountersUnreceivedBursts_Object = MibTableColumn
ontCountersUnreceivedBursts = _OntCountersUnreceivedBursts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 4, 1, 1),
    _OntCountersUnreceivedBursts_Type()
)
ontCountersUnreceivedBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontCountersUnreceivedBursts.setStatus("current")
_OntCountersPositiveDriftBits_Type = Counter32
_OntCountersPositiveDriftBits_Object = MibTableColumn
ontCountersPositiveDriftBits = _OntCountersPositiveDriftBits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 4, 1, 2),
    _OntCountersPositiveDriftBits_Type()
)
ontCountersPositiveDriftBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontCountersPositiveDriftBits.setStatus("current")
_OntCountersNegativeDriftBits_Type = Counter32
_OntCountersNegativeDriftBits_Object = MibTableColumn
ontCountersNegativeDriftBits = _OntCountersNegativeDriftBits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 4, 1, 3),
    _OntCountersNegativeDriftBits_Type()
)
ontCountersNegativeDriftBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontCountersNegativeDriftBits.setStatus("current")
_OntCountersBip8Errors_Type = Counter32
_OntCountersBip8Errors_Object = MibTableColumn
ontCountersBip8Errors = _OntCountersBip8Errors_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 4, 1, 4),
    _OntCountersBip8Errors_Type()
)
ontCountersBip8Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontCountersBip8Errors.setStatus("current")
_OntCountersCorrectedBytes_Type = Counter32
_OntCountersCorrectedBytes_Object = MibTableColumn
ontCountersCorrectedBytes = _OntCountersCorrectedBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 4, 1, 5),
    _OntCountersCorrectedBytes_Type()
)
ontCountersCorrectedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontCountersCorrectedBytes.setStatus("current")
_OntCountersCorrectedCodewords_Type = Counter32
_OntCountersCorrectedCodewords_Object = MibTableColumn
ontCountersCorrectedCodewords = _OntCountersCorrectedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 4, 1, 6),
    _OntCountersCorrectedCodewords_Type()
)
ontCountersCorrectedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontCountersCorrectedCodewords.setStatus("current")
_OntCountersUncorrctableCodewords_Type = Counter32
_OntCountersUncorrctableCodewords_Object = MibTableColumn
ontCountersUncorrctableCodewords = _OntCountersUncorrctableCodewords_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 4, 1, 7),
    _OntCountersUncorrctableCodewords_Type()
)
ontCountersUncorrctableCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontCountersUncorrctableCodewords.setStatus("current")
_OntCountersTotalReceivedCodewords_Type = Counter32
_OntCountersTotalReceivedCodewords_Object = MibTableColumn
ontCountersTotalReceivedCodewords = _OntCountersTotalReceivedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 4, 1, 8),
    _OntCountersTotalReceivedCodewords_Type()
)
ontCountersTotalReceivedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontCountersTotalReceivedCodewords.setStatus("current")
_OntCountersDsBer_Type = Counter32
_OntCountersDsBer_Object = MibTableColumn
ontCountersDsBer = _OntCountersDsBer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 4, 1, 9),
    _OntCountersDsBer_Type()
)
ontCountersDsBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontCountersDsBer.setStatus("current")
_OntBwGroupStatusTable_Object = MibTable
ontBwGroupStatusTable = _OntBwGroupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 5)
)
if mibBuilder.loadTexts:
    ontBwGroupStatusTable.setStatus("current")
_OntBwGroupStatusEntry_Object = MibTableRow
ontBwGroupStatusEntry = _OntBwGroupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 5, 1)
)
ontBwGroupStatusEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontBwGroupId"),
)
if mibBuilder.loadTexts:
    ontBwGroupStatusEntry.setStatus("current")
_OntBwGroupStatusAllocId_Type = Integer32
_OntBwGroupStatusAllocId_Object = MibTableColumn
ontBwGroupStatusAllocId = _OntBwGroupStatusAllocId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 5, 1, 1),
    _OntBwGroupStatusAllocId_Type()
)
ontBwGroupStatusAllocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontBwGroupStatusAllocId.setStatus("current")
_OntBwGroupStatusCurrUsDataRate_Type = Integer32
_OntBwGroupStatusCurrUsDataRate_Object = MibTableColumn
ontBwGroupStatusCurrUsDataRate = _OntBwGroupStatusCurrUsDataRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 5, 1, 2),
    _OntBwGroupStatusCurrUsDataRate_Type()
)
ontBwGroupStatusCurrUsDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontBwGroupStatusCurrUsDataRate.setStatus("current")
_OntWanStatusTable_Object = MibTable
ontWanStatusTable = _OntWanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 6)
)
if mibBuilder.loadTexts:
    ontWanStatusTable.setStatus("current")
_OntWanStatusEntry_Object = MibTableRow
ontWanStatusEntry = _OntWanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 6, 1)
)
ontWanStatusEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontWanId"),
)
if mibBuilder.loadTexts:
    ontWanStatusEntry.setStatus("current")


class _OntWanId_Type(Integer32):
    """Custom type ontWanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_OntWanId_Type.__name__ = "Integer32"
_OntWanId_Object = MibTableColumn
ontWanId = _OntWanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 6, 1, 1),
    _OntWanId_Type()
)
ontWanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ontWanId.setStatus("current")


class _OntWanStatusEnable_Type(Integer32):
    """Custom type ontWanStatusEnable based on Integer32"""
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


_OntWanStatusEnable_Type.__name__ = "Integer32"
_OntWanStatusEnable_Object = MibTableColumn
ontWanStatusEnable = _OntWanStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 6, 1, 2),
    _OntWanStatusEnable_Type()
)
ontWanStatusEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontWanStatusEnable.setStatus("current")


class _OntWanStatusType_Type(Integer32):
    """Custom type ontWanStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipoe", 0),
          ("pppoe", 1),
          ("bridging", 2))
    )


_OntWanStatusType_Type.__name__ = "Integer32"
_OntWanStatusType_Object = MibTableColumn
ontWanStatusType = _OntWanStatusType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 6, 1, 3),
    _OntWanStatusType_Type()
)
ontWanStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontWanStatusType.setStatus("current")


class _OntWanStatusLinkStatus_Type(Integer32):
    """Custom type ontWanStatusLinkStatus based on Integer32"""
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


_OntWanStatusLinkStatus_Type.__name__ = "Integer32"
_OntWanStatusLinkStatus_Object = MibTableColumn
ontWanStatusLinkStatus = _OntWanStatusLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 6, 1, 4),
    _OntWanStatusLinkStatus_Type()
)
ontWanStatusLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontWanStatusLinkStatus.setStatus("current")


class _OntWanStatusServiceType_Type(Bits):
    """Custom type ontWanStatusServiceType based on Bits"""
    namedValues = NamedValues(
        *(("data", 0),
          ("voip", 1),
          ("management", 2),
          ("iptv", 3))
    )

_OntWanStatusServiceType_Type.__name__ = "Bits"
_OntWanStatusServiceType_Object = MibTableColumn
ontWanStatusServiceType = _OntWanStatusServiceType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 6, 1, 5),
    _OntWanStatusServiceType_Type()
)
ontWanStatusServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontWanStatusServiceType.setStatus("current")
_OntWanStatusVlan_Type = Integer32
_OntWanStatusVlan_Object = MibTableColumn
ontWanStatusVlan = _OntWanStatusVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 6, 1, 6),
    _OntWanStatusVlan_Type()
)
ontWanStatusVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontWanStatusVlan.setStatus("current")
_OntWanStatusPriority_Type = Integer32
_OntWanStatusPriority_Object = MibTableColumn
ontWanStatusPriority = _OntWanStatusPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 6, 1, 7),
    _OntWanStatusPriority_Type()
)
ontWanStatusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontWanStatusPriority.setStatus("current")


class _OntWanStatusIpMode_Type(Integer32):
    """Custom type ontWanStatusIpMode based on Integer32"""
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


_OntWanStatusIpMode_Type.__name__ = "Integer32"
_OntWanStatusIpMode_Object = MibTableColumn
ontWanStatusIpMode = _OntWanStatusIpMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 6, 1, 8),
    _OntWanStatusIpMode_Type()
)
ontWanStatusIpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontWanStatusIpMode.setStatus("current")
_OntWanStatusIp_Type = IpAddress
_OntWanStatusIp_Object = MibTableColumn
ontWanStatusIp = _OntWanStatusIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 6, 1, 9),
    _OntWanStatusIp_Type()
)
ontWanStatusIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontWanStatusIp.setStatus("current")
_OntWanStatusMask_Type = IpAddress
_OntWanStatusMask_Object = MibTableColumn
ontWanStatusMask = _OntWanStatusMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 6, 1, 10),
    _OntWanStatusMask_Type()
)
ontWanStatusMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontWanStatusMask.setStatus("current")
_OntWanStatusGateway_Type = IpAddress
_OntWanStatusGateway_Object = MibTableColumn
ontWanStatusGateway = _OntWanStatusGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 6, 1, 11),
    _OntWanStatusGateway_Type()
)
ontWanStatusGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontWanStatusGateway.setStatus("current")
_OntWanStatusPrimaryDns_Type = IpAddress
_OntWanStatusPrimaryDns_Object = MibTableColumn
ontWanStatusPrimaryDns = _OntWanStatusPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 6, 1, 12),
    _OntWanStatusPrimaryDns_Type()
)
ontWanStatusPrimaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontWanStatusPrimaryDns.setStatus("current")
_OntWanStatusSecondDns_Type = IpAddress
_OntWanStatusSecondDns_Object = MibTableColumn
ontWanStatusSecondDns = _OntWanStatusSecondDns_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 6, 1, 13),
    _OntWanStatusSecondDns_Type()
)
ontWanStatusSecondDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontWanStatusSecondDns.setStatus("current")


class _OntWanStatusNat_Type(Integer32):
    """Custom type ontWanStatusNat based on Integer32"""
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


_OntWanStatusNat_Type.__name__ = "Integer32"
_OntWanStatusNat_Object = MibTableColumn
ontWanStatusNat = _OntWanStatusNat_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 6, 1, 14),
    _OntWanStatusNat_Type()
)
ontWanStatusNat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontWanStatusNat.setStatus("current")


class _OntWanStatusGetState_Type(Integer32):
    """Custom type ontWanStatusGetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("processing", 1))
    )


_OntWanStatusGetState_Type.__name__ = "Integer32"
_OntWanStatusGetState_Object = MibTableColumn
ontWanStatusGetState = _OntWanStatusGetState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 6, 1, 15),
    _OntWanStatusGetState_Type()
)
ontWanStatusGetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontWanStatusGetState.setStatus("current")
_OntStatusHistTable_Object = MibTable
ontStatusHistTable = _OntStatusHistTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 7)
)
if mibBuilder.loadTexts:
    ontStatusHistTable.setStatus("current")
_OntStatusHistEntry_Object = MibTableRow
ontStatusHistEntry = _OntStatusHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 7, 1)
)
ontStatusHistEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontStatusHistIdx"),
)
if mibBuilder.loadTexts:
    ontStatusHistEntry.setStatus("current")


class _OntStatusHistIdx_Type(Integer32):
    """Custom type ontStatusHistIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_OntStatusHistIdx_Type.__name__ = "Integer32"
_OntStatusHistIdx_Object = MibTableColumn
ontStatusHistIdx = _OntStatusHistIdx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 7, 1, 1),
    _OntStatusHistIdx_Type()
)
ontStatusHistIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ontStatusHistIdx.setStatus("current")
_OntStatusHistStatus_Type = RemoteOnuStatus
_OntStatusHistStatus_Object = MibTableColumn
ontStatusHistStatus = _OntStatusHistStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 7, 1, 2),
    _OntStatusHistStatus_Type()
)
ontStatusHistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontStatusHistStatus.setStatus("current")
_OntStatusHistYear_Type = Integer32
_OntStatusHistYear_Object = MibTableColumn
ontStatusHistYear = _OntStatusHistYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 7, 1, 3),
    _OntStatusHistYear_Type()
)
ontStatusHistYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontStatusHistYear.setStatus("current")
_OntStatusHistMonth_Type = Integer32
_OntStatusHistMonth_Object = MibTableColumn
ontStatusHistMonth = _OntStatusHistMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 7, 1, 4),
    _OntStatusHistMonth_Type()
)
ontStatusHistMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontStatusHistMonth.setStatus("current")
_OntStatusHistDay_Type = Integer32
_OntStatusHistDay_Object = MibTableColumn
ontStatusHistDay = _OntStatusHistDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 7, 1, 5),
    _OntStatusHistDay_Type()
)
ontStatusHistDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontStatusHistDay.setStatus("current")
_OntStatusHistHour_Type = Integer32
_OntStatusHistHour_Object = MibTableColumn
ontStatusHistHour = _OntStatusHistHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 7, 1, 6),
    _OntStatusHistHour_Type()
)
ontStatusHistHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontStatusHistHour.setStatus("current")
_OntStatusHistMin_Type = Integer32
_OntStatusHistMin_Object = MibTableColumn
ontStatusHistMin = _OntStatusHistMin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 7, 1, 7),
    _OntStatusHistMin_Type()
)
ontStatusHistMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontStatusHistMin.setStatus("current")
_OntStatusHistSec_Type = Integer32
_OntStatusHistSec_Object = MibTableColumn
ontStatusHistSec = _OntStatusHistSec_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 7, 1, 8),
    _OntStatusHistSec_Type()
)
ontStatusHistSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontStatusHistSec.setStatus("current")
_OntStormingStatusTable_Object = MibTable
ontStormingStatusTable = _OntStormingStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 8)
)
if mibBuilder.loadTexts:
    ontStormingStatusTable.setStatus("current")
_OntStormingStatusEntry_Object = MibTableRow
ontStormingStatusEntry = _OntStormingStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 8, 1)
)
ontStormingStatusEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
)
if mibBuilder.loadTexts:
    ontStormingStatusEntry.setStatus("current")


class _OntStormingBcastOverThr_Type(Integer32):
    """Custom type ontStormingBcastOverThr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("no", 1),
          ("yes", 2))
    )


_OntStormingBcastOverThr_Type.__name__ = "Integer32"
_OntStormingBcastOverThr_Object = MibTableColumn
ontStormingBcastOverThr = _OntStormingBcastOverThr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 8, 1, 1),
    _OntStormingBcastOverThr_Type()
)
ontStormingBcastOverThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontStormingBcastOverThr.setStatus("current")


class _OntStormingMcastOverThr_Type(Integer32):
    """Custom type ontStormingMcastOverThr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("no", 1),
          ("yes", 2))
    )


_OntStormingMcastOverThr_Type.__name__ = "Integer32"
_OntStormingMcastOverThr_Object = MibTableColumn
ontStormingMcastOverThr = _OntStormingMcastOverThr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 8, 1, 2),
    _OntStormingMcastOverThr_Type()
)
ontStormingMcastOverThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontStormingMcastOverThr.setStatus("current")


class _OntStormingUnknowOverThr_Type(Integer32):
    """Custom type ontStormingUnknowOverThr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("no", 1),
          ("yes", 2))
    )


_OntStormingUnknowOverThr_Type.__name__ = "Integer32"
_OntStormingUnknowOverThr_Object = MibTableColumn
ontStormingUnknowOverThr = _OntStormingUnknowOverThr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 8, 1, 3),
    _OntStormingUnknowOverThr_Type()
)
ontStormingUnknowOverThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontStormingUnknowOverThr.setStatus("current")


class _OntStormingDdosArpDetect_Type(Integer32):
    """Custom type ontStormingDdosArpDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("no", 1),
          ("yes", 2))
    )


_OntStormingDdosArpDetect_Type.__name__ = "Integer32"
_OntStormingDdosArpDetect_Object = MibTableColumn
ontStormingDdosArpDetect = _OntStormingDdosArpDetect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 8, 1, 4),
    _OntStormingDdosArpDetect_Type()
)
ontStormingDdosArpDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontStormingDdosArpDetect.setStatus("current")


class _OntStormingDdosTcpDetect_Type(Integer32):
    """Custom type ontStormingDdosTcpDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("no", 1),
          ("yes", 2))
    )


_OntStormingDdosTcpDetect_Type.__name__ = "Integer32"
_OntStormingDdosTcpDetect_Object = MibTableColumn
ontStormingDdosTcpDetect = _OntStormingDdosTcpDetect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 8, 1, 5),
    _OntStormingDdosTcpDetect_Type()
)
ontStormingDdosTcpDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontStormingDdosTcpDetect.setStatus("current")


class _OntStormingDdosUdpDetect_Type(Integer32):
    """Custom type ontStormingDdosUdpDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("no", 1),
          ("yes", 2))
    )


_OntStormingDdosUdpDetect_Type.__name__ = "Integer32"
_OntStormingDdosUdpDetect_Object = MibTableColumn
ontStormingDdosUdpDetect = _OntStormingDdosUdpDetect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 8, 1, 6),
    _OntStormingDdosUdpDetect_Type()
)
ontStormingDdosUdpDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontStormingDdosUdpDetect.setStatus("current")


class _OntStormingLoopguardDetect_Type(Integer32):
    """Custom type ontStormingLoopguardDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("no", 1),
          ("yes", 2))
    )


_OntStormingLoopguardDetect_Type.__name__ = "Integer32"
_OntStormingLoopguardDetect_Object = MibTableColumn
ontStormingLoopguardDetect = _OntStormingLoopguardDetect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 8, 1, 7),
    _OntStormingLoopguardDetect_Type()
)
ontStormingLoopguardDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontStormingLoopguardDetect.setStatus("current")
_OntAclServiceStatusTable_Object = MibTable
ontAclServiceStatusTable = _OntAclServiceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 9)
)
if mibBuilder.loadTexts:
    ontAclServiceStatusTable.setStatus("current")
_OntAclServiceStatusEntry_Object = MibTableRow
ontAclServiceStatusEntry = _OntAclServiceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 9, 1)
)
ontAclServiceStatusEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontAclRuleId"),
)
if mibBuilder.loadTexts:
    ontAclServiceStatusEntry.setStatus("current")
_OntAclServiceStatusState_Type = DisplayString
_OntAclServiceStatusState_Object = MibTableColumn
ontAclServiceStatusState = _OntAclServiceStatusState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 9, 1, 1),
    _OntAclServiceStatusState_Type()
)
ontAclServiceStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontAclServiceStatusState.setStatus("current")
_OntAclServiceStatusProfileName_Type = DisplayString
_OntAclServiceStatusProfileName_Object = MibTableColumn
ontAclServiceStatusProfileName = _OntAclServiceStatusProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 3, 9, 1, 2),
    _OntAclServiceStatusProfileName_Type()
)
ontAclServiceStatusProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontAclServiceStatusProfileName.setStatus("current")
_OntCardStatusTable_Object = MibTable
ontCardStatusTable = _OntCardStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 4)
)
if mibBuilder.loadTexts:
    ontCardStatusTable.setStatus("current")
_OntCardStatusEntry_Object = MibTableRow
ontCardStatusEntry = _OntCardStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 4, 1)
)
ontCardStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
)
if mibBuilder.loadTexts:
    ontCardStatusEntry.setStatus("current")
_Status_Type = RemoteOnuStatus
_Status_Object = MibTableColumn
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 4, 1, 1),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("current")


class _AdminState_Type(Integer32):
    """Custom type adminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unlocked", 0),
          ("locked", 1))
    )


_AdminState_Type.__name__ = "Integer32"
_AdminState_Object = MibTableColumn
adminState = _AdminState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 4, 1, 2),
    _AdminState_Type()
)
adminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminState.setStatus("current")


class _ExpectType_Type(Integer32):
    """Custom type expectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ether", 0),
          ("veip", 1),
          ("pots", 2),
          ("xdsl", 3),
          ("giga", 4),
          ("video", 5),
          ("unknow", 6))
    )


_ExpectType_Type.__name__ = "Integer32"
_ExpectType_Object = MibTableColumn
expectType = _ExpectType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 4, 1, 4),
    _ExpectType_Type()
)
expectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expectType.setStatus("current")


class _ActualType_Type(Integer32):
    """Custom type actualType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ether", 0),
          ("veip", 1),
          ("pots", 2),
          ("xdsl", 3),
          ("giga", 4),
          ("video", 5),
          ("unknow", 6))
    )


_ActualType_Type.__name__ = "Integer32"
_ActualType_Object = MibTableColumn
actualType = _ActualType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 4, 1, 5),
    _ActualType_Type()
)
actualType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualType.setStatus("current")
_ExpectedPort_Type = Integer32
_ExpectedPort_Object = MibTableColumn
expectedPort = _ExpectedPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 4, 1, 6),
    _ExpectedPort_Type()
)
expectedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expectedPort.setStatus("current")
_ActualPort_Type = Integer32
_ActualPort_Object = MibTableColumn
actualPort = _ActualPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 4, 1, 7),
    _ActualPort_Type()
)
actualPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualPort.setStatus("current")
_OntDdmiStatusTable_Object = MibTable
ontDdmiStatusTable = _OntDdmiStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 5)
)
if mibBuilder.loadTexts:
    ontDdmiStatusTable.setStatus("current")
_OntDdmiStatusEntry_Object = MibTableRow
ontDdmiStatusEntry = _OntDdmiStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 5, 1)
)
ontDdmiStatusEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
)
if mibBuilder.loadTexts:
    ontDdmiStatusEntry.setStatus("current")
_Voltage_Type = DisplayString
_Voltage_Object = MibTableColumn
voltage = _Voltage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 5, 1, 1),
    _Voltage_Type()
)
voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage.setStatus("current")
_RxPower_Type = DisplayString
_RxPower_Object = MibTableColumn
rxPower = _RxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 5, 1, 2),
    _RxPower_Type()
)
rxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPower.setStatus("current")
_TxPower_Type = DisplayString
_TxPower_Object = MibTableColumn
txPower = _TxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 5, 1, 3),
    _TxPower_Type()
)
txPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPower.setStatus("current")
_LaserCurrent_Type = DisplayString
_LaserCurrent_Object = MibTableColumn
laserCurrent = _LaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 5, 1, 4),
    _LaserCurrent_Type()
)
laserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laserCurrent.setStatus("current")
_OntTemperature_Type = DisplayString
_OntTemperature_Object = MibTableColumn
ontTemperature = _OntTemperature_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 5, 1, 5),
    _OntTemperature_Type()
)
ontTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontTemperature.setStatus("current")
_OntDdmiRowStatus_Type = EnabledStatus
_OntDdmiRowStatus_Object = MibTableColumn
ontDdmiRowStatus = _OntDdmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 5, 1, 6),
    _OntDdmiRowStatus_Type()
)
ontDdmiRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontDdmiRowStatus.setStatus("current")


class _OntDdmiStatus_Type(Integer32):
    """Custom type ontDdmiStatus based on Integer32"""
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
          ("waiting", 1),
          ("processing", 2),
          ("done", 3))
    )


_OntDdmiStatus_Type.__name__ = "Integer32"
_OntDdmiStatus_Object = MibTableColumn
ontDdmiStatus = _OntDdmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 5, 1, 7),
    _OntDdmiStatus_Type()
)
ontDdmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontDdmiStatus.setStatus("current")
_OntEnetPmCounters_ObjectIdentity = ObjectIdentity
ontEnetPmCounters = _OntEnetPmCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6)
)
_OntEnetCurrentPmCountersTable_Object = MibTable
ontEnetCurrentPmCountersTable = _OntEnetCurrentPmCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 1)
)
if mibBuilder.loadTexts:
    ontEnetCurrentPmCountersTable.setStatus("current")
_OntEnetCurrentPmCountersEntry_Object = MibTableRow
ontEnetCurrentPmCountersEntry = _OntEnetCurrentPmCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 1, 1)
)
ontEnetCurrentPmCountersEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "ontenetCardPort"),
)
if mibBuilder.loadTexts:
    ontEnetCurrentPmCountersEntry.setStatus("current")
_OntEnetCurrentPmUsOctets_Type = Counter64
_OntEnetCurrentPmUsOctets_Object = MibTableColumn
ontEnetCurrentPmUsOctets = _OntEnetCurrentPmUsOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 1, 1, 1),
    _OntEnetCurrentPmUsOctets_Type()
)
ontEnetCurrentPmUsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetCurrentPmUsOctets.setStatus("current")
_OntEnetCurrentPmUsPackets_Type = Counter64
_OntEnetCurrentPmUsPackets_Object = MibTableColumn
ontEnetCurrentPmUsPackets = _OntEnetCurrentPmUsPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 1, 1, 2),
    _OntEnetCurrentPmUsPackets_Type()
)
ontEnetCurrentPmUsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetCurrentPmUsPackets.setStatus("current")
_OntEnetCurrentPmUsMcastPackets_Type = Counter64
_OntEnetCurrentPmUsMcastPackets_Object = MibTableColumn
ontEnetCurrentPmUsMcastPackets = _OntEnetCurrentPmUsMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 1, 1, 3),
    _OntEnetCurrentPmUsMcastPackets_Type()
)
ontEnetCurrentPmUsMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetCurrentPmUsMcastPackets.setStatus("current")
_OntEnetCurrentPmUsBcastPackets_Type = Counter64
_OntEnetCurrentPmUsBcastPackets_Object = MibTableColumn
ontEnetCurrentPmUsBcastPackets = _OntEnetCurrentPmUsBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 1, 1, 4),
    _OntEnetCurrentPmUsBcastPackets_Type()
)
ontEnetCurrentPmUsBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetCurrentPmUsBcastPackets.setStatus("current")
_OntEnetCurrentPmDsOctets_Type = Counter64
_OntEnetCurrentPmDsOctets_Object = MibTableColumn
ontEnetCurrentPmDsOctets = _OntEnetCurrentPmDsOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 1, 1, 5),
    _OntEnetCurrentPmDsOctets_Type()
)
ontEnetCurrentPmDsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetCurrentPmDsOctets.setStatus("current")
_OntEnetCurrentPmDsPackets_Type = Counter64
_OntEnetCurrentPmDsPackets_Object = MibTableColumn
ontEnetCurrentPmDsPackets = _OntEnetCurrentPmDsPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 1, 1, 6),
    _OntEnetCurrentPmDsPackets_Type()
)
ontEnetCurrentPmDsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetCurrentPmDsPackets.setStatus("current")
_OntEnetCurrentPmDsMcastPackets_Type = Counter64
_OntEnetCurrentPmDsMcastPackets_Object = MibTableColumn
ontEnetCurrentPmDsMcastPackets = _OntEnetCurrentPmDsMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 1, 1, 7),
    _OntEnetCurrentPmDsMcastPackets_Type()
)
ontEnetCurrentPmDsMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetCurrentPmDsMcastPackets.setStatus("current")
_OntEnetCurrentPmDsBcastPackets_Type = Counter64
_OntEnetCurrentPmDsBcastPackets_Object = MibTableColumn
ontEnetCurrentPmDsBcastPackets = _OntEnetCurrentPmDsBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 1, 1, 8),
    _OntEnetCurrentPmDsBcastPackets_Type()
)
ontEnetCurrentPmDsBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetCurrentPmDsBcastPackets.setStatus("current")
_OntEnetPmCountersGetCurrent_Type = EnabledStatus
_OntEnetPmCountersGetCurrent_Object = MibTableColumn
ontEnetPmCountersGetCurrent = _OntEnetPmCountersGetCurrent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 1, 1, 9),
    _OntEnetPmCountersGetCurrent_Type()
)
ontEnetPmCountersGetCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontEnetPmCountersGetCurrent.setStatus("current")


class _OntEnetPmCountersCheckGetCurrent_Type(Integer32):
    """Custom type ontEnetPmCountersCheckGetCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("standby", 0),
          ("processing", 1))
    )


_OntEnetPmCountersCheckGetCurrent_Type.__name__ = "Integer32"
_OntEnetPmCountersCheckGetCurrent_Object = MibTableColumn
ontEnetPmCountersCheckGetCurrent = _OntEnetPmCountersCheckGetCurrent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 1, 1, 10),
    _OntEnetPmCountersCheckGetCurrent_Type()
)
ontEnetPmCountersCheckGetCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetPmCountersCheckGetCurrent.setStatus("current")
_OntEnetLast15PmCountersTable_Object = MibTable
ontEnetLast15PmCountersTable = _OntEnetLast15PmCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 2)
)
if mibBuilder.loadTexts:
    ontEnetLast15PmCountersTable.setStatus("current")
_OntEnetLast15PmCountersEntry_Object = MibTableRow
ontEnetLast15PmCountersEntry = _OntEnetLast15PmCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 2, 1)
)
ontEnetLast15PmCountersEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "ontenetCardPort"),
)
if mibBuilder.loadTexts:
    ontEnetLast15PmCountersEntry.setStatus("current")
_OntEnetLast15PmUsOctets_Type = Counter64
_OntEnetLast15PmUsOctets_Object = MibTableColumn
ontEnetLast15PmUsOctets = _OntEnetLast15PmUsOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 2, 1, 1),
    _OntEnetLast15PmUsOctets_Type()
)
ontEnetLast15PmUsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetLast15PmUsOctets.setStatus("current")
_OntEnetLast15PmUsPackets_Type = Counter64
_OntEnetLast15PmUsPackets_Object = MibTableColumn
ontEnetLast15PmUsPackets = _OntEnetLast15PmUsPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 2, 1, 2),
    _OntEnetLast15PmUsPackets_Type()
)
ontEnetLast15PmUsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetLast15PmUsPackets.setStatus("current")
_OntEnetLast15PmUsMcastPackets_Type = Counter64
_OntEnetLast15PmUsMcastPackets_Object = MibTableColumn
ontEnetLast15PmUsMcastPackets = _OntEnetLast15PmUsMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 2, 1, 3),
    _OntEnetLast15PmUsMcastPackets_Type()
)
ontEnetLast15PmUsMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetLast15PmUsMcastPackets.setStatus("current")
_OntEnetLast15PmUsBcastPackets_Type = Counter64
_OntEnetLast15PmUsBcastPackets_Object = MibTableColumn
ontEnetLast15PmUsBcastPackets = _OntEnetLast15PmUsBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 2, 1, 4),
    _OntEnetLast15PmUsBcastPackets_Type()
)
ontEnetLast15PmUsBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetLast15PmUsBcastPackets.setStatus("current")
_OntEnetLast15PmDsOctets_Type = Counter64
_OntEnetLast15PmDsOctets_Object = MibTableColumn
ontEnetLast15PmDsOctets = _OntEnetLast15PmDsOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 2, 1, 5),
    _OntEnetLast15PmDsOctets_Type()
)
ontEnetLast15PmDsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetLast15PmDsOctets.setStatus("current")
_OntEnetLast15PmDsPackets_Type = Counter64
_OntEnetLast15PmDsPackets_Object = MibTableColumn
ontEnetLast15PmDsPackets = _OntEnetLast15PmDsPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 2, 1, 6),
    _OntEnetLast15PmDsPackets_Type()
)
ontEnetLast15PmDsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetLast15PmDsPackets.setStatus("current")
_OntEnetLast15PmDsMcastPackets_Type = Counter64
_OntEnetLast15PmDsMcastPackets_Object = MibTableColumn
ontEnetLast15PmDsMcastPackets = _OntEnetLast15PmDsMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 2, 1, 7),
    _OntEnetLast15PmDsMcastPackets_Type()
)
ontEnetLast15PmDsMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetLast15PmDsMcastPackets.setStatus("current")
_OntEnetLast15PmDsBcastPackets_Type = Counter64
_OntEnetLast15PmDsBcastPackets_Object = MibTableColumn
ontEnetLast15PmDsBcastPackets = _OntEnetLast15PmDsBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 2, 1, 8),
    _OntEnetLast15PmDsBcastPackets_Type()
)
ontEnetLast15PmDsBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetLast15PmDsBcastPackets.setStatus("current")
_OntEnetLast15PmInterval_Type = Counter32
_OntEnetLast15PmInterval_Object = MibTableColumn
ontEnetLast15PmInterval = _OntEnetLast15PmInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 6, 2, 1, 9),
    _OntEnetLast15PmInterval_Type()
)
ontEnetLast15PmInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetLast15PmInterval.setStatus("current")
_OntEnetStatus_ObjectIdentity = ObjectIdentity
ontEnetStatus = _OntEnetStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 7)
)
_OntEnetStatusTable_Object = MibTable
ontEnetStatusTable = _OntEnetStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 7, 1)
)
if mibBuilder.loadTexts:
    ontEnetStatusTable.setStatus("current")
_OntEnetStatusEntry_Object = MibTableRow
ontEnetStatusEntry = _OntEnetStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 7, 1, 1)
)
ontEnetStatusEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "ontenetCardPort"),
)
if mibBuilder.loadTexts:
    ontEnetStatusEntry.setStatus("current")
_OntEnetPortStatus_Type = RemoteOnuStatus
_OntEnetPortStatus_Object = MibTableColumn
ontEnetPortStatus = _OntEnetPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 7, 1, 1, 1),
    _OntEnetPortStatus_Type()
)
ontEnetPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontEnetPortStatus.setStatus("current")
_OntVenetPmCounters_ObjectIdentity = ObjectIdentity
ontVenetPmCounters = _OntVenetPmCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8)
)
_OntVenetCurrentPmCountersTable_Object = MibTable
ontVenetCurrentPmCountersTable = _OntVenetCurrentPmCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 1)
)
if mibBuilder.loadTexts:
    ontVenetCurrentPmCountersTable.setStatus("current")
_OntVenetCurrentPmCountersEntry_Object = MibTableRow
ontVenetCurrentPmCountersEntry = _OntVenetCurrentPmCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 1, 1)
)
ontVenetCurrentPmCountersEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "ontenetCardPort"),
)
if mibBuilder.loadTexts:
    ontVenetCurrentPmCountersEntry.setStatus("current")
_OntVenetCurrentPmUsOctets_Type = Counter64
_OntVenetCurrentPmUsOctets_Object = MibTableColumn
ontVenetCurrentPmUsOctets = _OntVenetCurrentPmUsOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 1, 1, 1),
    _OntVenetCurrentPmUsOctets_Type()
)
ontVenetCurrentPmUsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetCurrentPmUsOctets.setStatus("current")
_OntVenetCurrentPmUsPackets_Type = Counter64
_OntVenetCurrentPmUsPackets_Object = MibTableColumn
ontVenetCurrentPmUsPackets = _OntVenetCurrentPmUsPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 1, 1, 2),
    _OntVenetCurrentPmUsPackets_Type()
)
ontVenetCurrentPmUsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetCurrentPmUsPackets.setStatus("current")
_OntVenetCurrentPmUsMcastPackets_Type = Counter64
_OntVenetCurrentPmUsMcastPackets_Object = MibTableColumn
ontVenetCurrentPmUsMcastPackets = _OntVenetCurrentPmUsMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 1, 1, 3),
    _OntVenetCurrentPmUsMcastPackets_Type()
)
ontVenetCurrentPmUsMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetCurrentPmUsMcastPackets.setStatus("current")
_OntVenetCurrentPmUsBcastPackets_Type = Counter64
_OntVenetCurrentPmUsBcastPackets_Object = MibTableColumn
ontVenetCurrentPmUsBcastPackets = _OntVenetCurrentPmUsBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 1, 1, 4),
    _OntVenetCurrentPmUsBcastPackets_Type()
)
ontVenetCurrentPmUsBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetCurrentPmUsBcastPackets.setStatus("current")
_OntVenetCurrentPmDsOctets_Type = Counter64
_OntVenetCurrentPmDsOctets_Object = MibTableColumn
ontVenetCurrentPmDsOctets = _OntVenetCurrentPmDsOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 1, 1, 5),
    _OntVenetCurrentPmDsOctets_Type()
)
ontVenetCurrentPmDsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetCurrentPmDsOctets.setStatus("current")
_OntVenetCurrentPmDsPackets_Type = Counter64
_OntVenetCurrentPmDsPackets_Object = MibTableColumn
ontVenetCurrentPmDsPackets = _OntVenetCurrentPmDsPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 1, 1, 6),
    _OntVenetCurrentPmDsPackets_Type()
)
ontVenetCurrentPmDsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetCurrentPmDsPackets.setStatus("current")
_OntVenetCurrentPmDsMcastPackets_Type = Counter64
_OntVenetCurrentPmDsMcastPackets_Object = MibTableColumn
ontVenetCurrentPmDsMcastPackets = _OntVenetCurrentPmDsMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 1, 1, 7),
    _OntVenetCurrentPmDsMcastPackets_Type()
)
ontVenetCurrentPmDsMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetCurrentPmDsMcastPackets.setStatus("current")
_OntVenetCurrentPmDsBcastPackets_Type = Counter64
_OntVenetCurrentPmDsBcastPackets_Object = MibTableColumn
ontVenetCurrentPmDsBcastPackets = _OntVenetCurrentPmDsBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 1, 1, 8),
    _OntVenetCurrentPmDsBcastPackets_Type()
)
ontVenetCurrentPmDsBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetCurrentPmDsBcastPackets.setStatus("current")
_OntVenetPmCountersGetCurrent_Type = EnabledStatus
_OntVenetPmCountersGetCurrent_Object = MibTableColumn
ontVenetPmCountersGetCurrent = _OntVenetPmCountersGetCurrent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 1, 1, 9),
    _OntVenetPmCountersGetCurrent_Type()
)
ontVenetPmCountersGetCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontVenetPmCountersGetCurrent.setStatus("current")


class _OntVenetPmCountersCheckGetCurrent_Type(Integer32):
    """Custom type ontVenetPmCountersCheckGetCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("standby", 0),
          ("processing", 1))
    )


_OntVenetPmCountersCheckGetCurrent_Type.__name__ = "Integer32"
_OntVenetPmCountersCheckGetCurrent_Object = MibTableColumn
ontVenetPmCountersCheckGetCurrent = _OntVenetPmCountersCheckGetCurrent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 1, 1, 10),
    _OntVenetPmCountersCheckGetCurrent_Type()
)
ontVenetPmCountersCheckGetCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetPmCountersCheckGetCurrent.setStatus("current")
_OntVenetLast15PmCountersTable_Object = MibTable
ontVenetLast15PmCountersTable = _OntVenetLast15PmCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 2)
)
if mibBuilder.loadTexts:
    ontVenetLast15PmCountersTable.setStatus("current")
_OntVenetLast15PmCountersEntry_Object = MibTableRow
ontVenetLast15PmCountersEntry = _OntVenetLast15PmCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 2, 1)
)
ontVenetLast15PmCountersEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "ontenetCardPort"),
)
if mibBuilder.loadTexts:
    ontVenetLast15PmCountersEntry.setStatus("current")
_OntVenetLast15PmUsOctets_Type = Counter64
_OntVenetLast15PmUsOctets_Object = MibTableColumn
ontVenetLast15PmUsOctets = _OntVenetLast15PmUsOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 2, 1, 1),
    _OntVenetLast15PmUsOctets_Type()
)
ontVenetLast15PmUsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetLast15PmUsOctets.setStatus("current")
_OntVenetLast15PmUsPackets_Type = Counter64
_OntVenetLast15PmUsPackets_Object = MibTableColumn
ontVenetLast15PmUsPackets = _OntVenetLast15PmUsPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 2, 1, 2),
    _OntVenetLast15PmUsPackets_Type()
)
ontVenetLast15PmUsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetLast15PmUsPackets.setStatus("current")
_OntVenetLast15PmUsMcastPackets_Type = Counter64
_OntVenetLast15PmUsMcastPackets_Object = MibTableColumn
ontVenetLast15PmUsMcastPackets = _OntVenetLast15PmUsMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 2, 1, 3),
    _OntVenetLast15PmUsMcastPackets_Type()
)
ontVenetLast15PmUsMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetLast15PmUsMcastPackets.setStatus("current")
_OntVenetLast15PmUsBcastPackets_Type = Counter64
_OntVenetLast15PmUsBcastPackets_Object = MibTableColumn
ontVenetLast15PmUsBcastPackets = _OntVenetLast15PmUsBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 2, 1, 4),
    _OntVenetLast15PmUsBcastPackets_Type()
)
ontVenetLast15PmUsBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetLast15PmUsBcastPackets.setStatus("current")
_OntVenetLast15PmDsOctets_Type = Counter64
_OntVenetLast15PmDsOctets_Object = MibTableColumn
ontVenetLast15PmDsOctets = _OntVenetLast15PmDsOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 2, 1, 5),
    _OntVenetLast15PmDsOctets_Type()
)
ontVenetLast15PmDsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetLast15PmDsOctets.setStatus("current")
_OntVenetLast15PmDsPackets_Type = Counter64
_OntVenetLast15PmDsPackets_Object = MibTableColumn
ontVenetLast15PmDsPackets = _OntVenetLast15PmDsPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 2, 1, 6),
    _OntVenetLast15PmDsPackets_Type()
)
ontVenetLast15PmDsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetLast15PmDsPackets.setStatus("current")
_OntVenetLast15PmDsMcastPackets_Type = Counter64
_OntVenetLast15PmDsMcastPackets_Object = MibTableColumn
ontVenetLast15PmDsMcastPackets = _OntVenetLast15PmDsMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 2, 1, 7),
    _OntVenetLast15PmDsMcastPackets_Type()
)
ontVenetLast15PmDsMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetLast15PmDsMcastPackets.setStatus("current")
_OntVenetLast15PmDsBcastPackets_Type = Counter64
_OntVenetLast15PmDsBcastPackets_Object = MibTableColumn
ontVenetLast15PmDsBcastPackets = _OntVenetLast15PmDsBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 2, 1, 8),
    _OntVenetLast15PmDsBcastPackets_Type()
)
ontVenetLast15PmDsBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetLast15PmDsBcastPackets.setStatus("current")
_OntVenetLast15PmInterval_Type = Counter32
_OntVenetLast15PmInterval_Object = MibTableColumn
ontVenetLast15PmInterval = _OntVenetLast15PmInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 8, 2, 1, 9),
    _OntVenetLast15PmInterval_Type()
)
ontVenetLast15PmInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetLast15PmInterval.setStatus("current")
_OntVenetStatusInfo_ObjectIdentity = ObjectIdentity
ontVenetStatusInfo = _OntVenetStatusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 9)
)
_OntVenetStatusTable_Object = MibTable
ontVenetStatusTable = _OntVenetStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 9, 1)
)
if mibBuilder.loadTexts:
    ontVenetStatusTable.setStatus("current")
_OntVenetStatusEntry_Object = MibTableRow
ontVenetStatusEntry = _OntVenetStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 9, 1, 1)
)
ontVenetStatusEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "ontvenetCardPort"),
)
if mibBuilder.loadTexts:
    ontVenetStatusEntry.setStatus("current")
_OntVenetStatus_Type = RemoteOnuStatus
_OntVenetStatus_Object = MibTableColumn
ontVenetStatus = _OntVenetStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 9, 1, 1, 1),
    _OntVenetStatus_Type()
)
ontVenetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVenetStatus.setStatus("current")
_OntPotsStatusInfo_ObjectIdentity = ObjectIdentity
ontPotsStatusInfo = _OntPotsStatusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 10)
)
_OntPotsStatusTable_Object = MibTable
ontPotsStatusTable = _OntPotsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 10, 1)
)
if mibBuilder.loadTexts:
    ontPotsStatusTable.setStatus("current")
_OntPotsStatusEntry_Object = MibTableRow
ontPotsStatusEntry = _OntPotsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 10, 1, 1)
)
ontPotsStatusEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "ontpotsCardPort"),
)
if mibBuilder.loadTexts:
    ontPotsStatusEntry.setStatus("current")
_OntPotsStatus_Type = RemoteOnuStatus
_OntPotsStatus_Object = MibTableColumn
ontPotsStatus = _OntPotsStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 10, 1, 1, 1),
    _OntPotsStatus_Type()
)
ontPotsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontPotsStatus.setStatus("current")
_OntUniportStatusInfo_ObjectIdentity = ObjectIdentity
ontUniportStatusInfo = _OntUniportStatusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 11)
)
_UniportVlanStatusTable_Object = MibTable
uniportVlanStatusTable = _UniportVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 11, 1)
)
if mibBuilder.loadTexts:
    uniportVlanStatusTable.setStatus("current")
_UniportVlanStatusEntry_Object = MibTableRow
uniportVlanStatusEntry = _UniportVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 11, 1, 1)
)
uniportVlanStatusEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "uniPort"),
    (0, "ZYXEL-olt1408-MIB", "uniportVlanUniSvid"),
    (0, "ZYXEL-olt1408-MIB", "uniportVlanUniCvid"),
)
if mibBuilder.loadTexts:
    uniportVlanStatusEntry.setStatus("current")
_UniportVlanStatus_Type = RemoteOnuStatus
_UniportVlanStatus_Object = MibTableColumn
uniportVlanStatus = _UniportVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 11, 1, 1, 1),
    _UniportVlanStatus_Type()
)
uniportVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniportVlanStatus.setStatus("current")
_OntVideoStatus_ObjectIdentity = ObjectIdentity
ontVideoStatus = _OntVideoStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 12)
)
_OntVideoStatusTable_Object = MibTable
ontVideoStatusTable = _OntVideoStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 12, 1)
)
if mibBuilder.loadTexts:
    ontVideoStatusTable.setStatus("current")
_OntVideoStatusEntry_Object = MibTableRow
ontVideoStatusEntry = _OntVideoStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 12, 1, 1)
)
ontVideoStatusEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "ontvideoPort"),
)
if mibBuilder.loadTexts:
    ontVideoStatusEntry.setStatus("current")
_OntVideoPortStatus_Type = RemoteOnuStatus
_OntVideoPortStatus_Object = MibTableColumn
ontVideoPortStatus = _OntVideoPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 12, 1, 1, 1),
    _OntVideoPortStatus_Type()
)
ontVideoPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontVideoPortStatus.setStatus("current")
_OntDdmiHistoryTable_Object = MibTable
ontDdmiHistoryTable = _OntDdmiHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 13)
)
if mibBuilder.loadTexts:
    ontDdmiHistoryTable.setStatus("current")
_OntDdmiHistoryEntry_Object = MibTableRow
ontDdmiHistoryEntry = _OntDdmiHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 13, 1)
)
ontDdmiHistoryEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "timeSlot"),
)
if mibBuilder.loadTexts:
    ontDdmiHistoryEntry.setStatus("current")
_OntDdmiHistoryVoltage15M_Type = DisplayString
_OntDdmiHistoryVoltage15M_Object = MibTableColumn
ontDdmiHistoryVoltage15M = _OntDdmiHistoryVoltage15M_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 13, 1, 1),
    _OntDdmiHistoryVoltage15M_Type()
)
ontDdmiHistoryVoltage15M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontDdmiHistoryVoltage15M.setStatus("current")
_OntDdmiHistoryRxPower15M_Type = DisplayString
_OntDdmiHistoryRxPower15M_Object = MibTableColumn
ontDdmiHistoryRxPower15M = _OntDdmiHistoryRxPower15M_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 13, 1, 2),
    _OntDdmiHistoryRxPower15M_Type()
)
ontDdmiHistoryRxPower15M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontDdmiHistoryRxPower15M.setStatus("current")
_OntDdmiHistoryTxPower15M_Type = DisplayString
_OntDdmiHistoryTxPower15M_Object = MibTableColumn
ontDdmiHistoryTxPower15M = _OntDdmiHistoryTxPower15M_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 13, 1, 3),
    _OntDdmiHistoryTxPower15M_Type()
)
ontDdmiHistoryTxPower15M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontDdmiHistoryTxPower15M.setStatus("current")
_OntDdmiHistoryLaserCurrent15M_Type = DisplayString
_OntDdmiHistoryLaserCurrent15M_Object = MibTableColumn
ontDdmiHistoryLaserCurrent15M = _OntDdmiHistoryLaserCurrent15M_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 13, 1, 4),
    _OntDdmiHistoryLaserCurrent15M_Type()
)
ontDdmiHistoryLaserCurrent15M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontDdmiHistoryLaserCurrent15M.setStatus("current")
_OntDdmiHistoryTemperature15M_Type = DisplayString
_OntDdmiHistoryTemperature15M_Object = MibTableColumn
ontDdmiHistoryTemperature15M = _OntDdmiHistoryTemperature15M_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 13, 1, 5),
    _OntDdmiHistoryTemperature15M_Type()
)
ontDdmiHistoryTemperature15M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontDdmiHistoryTemperature15M.setStatus("current")
_OntDdmiHistoryUpdateTime15M_Type = DisplayString
_OntDdmiHistoryUpdateTime15M_Object = MibTableColumn
ontDdmiHistoryUpdateTime15M = _OntDdmiHistoryUpdateTime15M_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 13, 1, 6),
    _OntDdmiHistoryUpdateTime15M_Type()
)
ontDdmiHistoryUpdateTime15M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontDdmiHistoryUpdateTime15M.setStatus("current")
_OntDdmiLatest15MTable_Object = MibTable
ontDdmiLatest15MTable = _OntDdmiLatest15MTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 14)
)
if mibBuilder.loadTexts:
    ontDdmiLatest15MTable.setStatus("current")
_OntDdmiLatest15MEntry_Object = MibTableRow
ontDdmiLatest15MEntry = _OntDdmiLatest15MEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 14, 1)
)
ontDdmiLatest15MEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
)
if mibBuilder.loadTexts:
    ontDdmiLatest15MEntry.setStatus("current")
_OntDdmiLatest15MVoltage_Type = DisplayString
_OntDdmiLatest15MVoltage_Object = MibTableColumn
ontDdmiLatest15MVoltage = _OntDdmiLatest15MVoltage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 14, 1, 1),
    _OntDdmiLatest15MVoltage_Type()
)
ontDdmiLatest15MVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontDdmiLatest15MVoltage.setStatus("current")
_OntDdmiLatest15MRxPower_Type = DisplayString
_OntDdmiLatest15MRxPower_Object = MibTableColumn
ontDdmiLatest15MRxPower = _OntDdmiLatest15MRxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 14, 1, 2),
    _OntDdmiLatest15MRxPower_Type()
)
ontDdmiLatest15MRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontDdmiLatest15MRxPower.setStatus("current")
_OntDdmiLatest15MTxPower_Type = DisplayString
_OntDdmiLatest15MTxPower_Object = MibTableColumn
ontDdmiLatest15MTxPower = _OntDdmiLatest15MTxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 14, 1, 3),
    _OntDdmiLatest15MTxPower_Type()
)
ontDdmiLatest15MTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontDdmiLatest15MTxPower.setStatus("current")
_OntDdmiLatest15MLaserCurrent_Type = DisplayString
_OntDdmiLatest15MLaserCurrent_Object = MibTableColumn
ontDdmiLatest15MLaserCurrent = _OntDdmiLatest15MLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 14, 1, 4),
    _OntDdmiLatest15MLaserCurrent_Type()
)
ontDdmiLatest15MLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontDdmiLatest15MLaserCurrent.setStatus("current")
_OntDdmiLatest15MTemperature_Type = DisplayString
_OntDdmiLatest15MTemperature_Object = MibTableColumn
ontDdmiLatest15MTemperature = _OntDdmiLatest15MTemperature_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 14, 1, 5),
    _OntDdmiLatest15MTemperature_Type()
)
ontDdmiLatest15MTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontDdmiLatest15MTemperature.setStatus("current")
_OntPmRateIntervalTable_Object = MibTable
ontPmRateIntervalTable = _OntPmRateIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 15)
)
if mibBuilder.loadTexts:
    ontPmRateIntervalTable.setStatus("current")
_OntPmRateIntervalEntry_Object = MibTableRow
ontPmRateIntervalEntry = _OntPmRateIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 15, 1)
)
ontPmRateIntervalEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "ontNumber"),
    (0, "ZYXEL-olt1408-MIB", "ontcard"),
    (0, "ZYXEL-olt1408-MIB", "uniPort"),
)
if mibBuilder.loadTexts:
    ontPmRateIntervalEntry.setStatus("current")
_OntPmRateIntervalTime_Type = DisplayString
_OntPmRateIntervalTime_Object = MibTableColumn
ontPmRateIntervalTime = _OntPmRateIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 15, 1, 1),
    _OntPmRateIntervalTime_Type()
)
ontPmRateIntervalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontPmRateIntervalTime.setStatus("current")
_OntPmRateIntervalUsRate_Type = Integer32
_OntPmRateIntervalUsRate_Object = MibTableColumn
ontPmRateIntervalUsRate = _OntPmRateIntervalUsRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 15, 1, 2),
    _OntPmRateIntervalUsRate_Type()
)
ontPmRateIntervalUsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontPmRateIntervalUsRate.setStatus("current")
_OntPmRateIntervalDsRate_Type = Integer32
_OntPmRateIntervalDsRate_Object = MibTableColumn
ontPmRateIntervalDsRate = _OntPmRateIntervalDsRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 136, 15, 1, 3),
    _OntPmRateIntervalDsRate_Type()
)
ontPmRateIntervalDsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontPmRateIntervalDsRate.setStatus("current")
_AntiSpoofSetup_ObjectIdentity = ObjectIdentity
antiSpoofSetup = _AntiSpoofSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 138)
)
_AntiSpoofState_Type = EnabledStatus
_AntiSpoofState_Object = MibScalar
antiSpoofState = _AntiSpoofState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 138, 1),
    _AntiSpoofState_Type()
)
antiSpoofState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    antiSpoofState.setStatus("current")
_AntiSpoofPortTable_Object = MibTable
antiSpoofPortTable = _AntiSpoofPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 138, 2)
)
if mibBuilder.loadTexts:
    antiSpoofPortTable.setStatus("current")
_AntiSpoofPortEntry_Object = MibTableRow
antiSpoofPortEntry = _AntiSpoofPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 138, 2, 1)
)
antiSpoofPortEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "antiSpoofActiveByPort"),
)
if mibBuilder.loadTexts:
    antiSpoofPortEntry.setStatus("current")
_AntiSpoofActiveByPort_Type = EnabledStatus
_AntiSpoofActiveByPort_Object = MibTableColumn
antiSpoofActiveByPort = _AntiSpoofActiveByPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 138, 2, 1, 1),
    _AntiSpoofActiveByPort_Type()
)
antiSpoofActiveByPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    antiSpoofActiveByPort.setStatus("current")
_AntiSpoofTable_Object = MibTable
antiSpoofTable = _AntiSpoofTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 138, 3)
)
if mibBuilder.loadTexts:
    antiSpoofTable.setStatus("current")
_AntiSpoofEntry_Object = MibTableRow
antiSpoofEntry = _AntiSpoofEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 138, 3, 1)
)
antiSpoofEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "antiSpoofPort"),
    (0, "ZYXEL-olt1408-MIB", "antiSpoofMode"),
    (0, "ZYXEL-olt1408-MIB", "antiSpoofSetting"),
)
if mibBuilder.loadTexts:
    antiSpoofEntry.setStatus("current")
_AntiSpoofPort_Type = Integer32
_AntiSpoofPort_Object = MibTableColumn
antiSpoofPort = _AntiSpoofPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 138, 3, 1, 1),
    _AntiSpoofPort_Type()
)
antiSpoofPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antiSpoofPort.setStatus("current")


class _AntiSpoofMode_Type(Integer32):
    """Custom type antiSpoofMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("inclusiveIp", 1),
          ("inclusiveMac", 2),
          ("inclusiveIpMac", 3),
          ("exclusiveIp", 5),
          ("exclusiveMac", 6),
          ("exclusiveIpMac", 7),
          ("inclusiveOuimac", 8))
    )


_AntiSpoofMode_Type.__name__ = "Integer32"
_AntiSpoofMode_Object = MibTableColumn
antiSpoofMode = _AntiSpoofMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 138, 3, 1, 2),
    _AntiSpoofMode_Type()
)
antiSpoofMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antiSpoofMode.setStatus("current")
_AntiSpoofSetting_Type = DisplayString
_AntiSpoofSetting_Object = MibTableColumn
antiSpoofSetting = _AntiSpoofSetting_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 138, 3, 1, 3),
    _AntiSpoofSetting_Type()
)
antiSpoofSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antiSpoofSetting.setStatus("current")
_AntiSpoofRowStatus_Type = RowStatus
_AntiSpoofRowStatus_Object = MibTableColumn
antiSpoofRowStatus = _AntiSpoofRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 138, 3, 1, 4),
    _AntiSpoofRowStatus_Type()
)
antiSpoofRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    antiSpoofRowStatus.setStatus("current")
_MulticastChannelSetup_ObjectIdentity = ObjectIdentity
multicastChannelSetup = _MulticastChannelSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 140)
)
_MulticastChannelTable_Object = MibTable
multicastChannelTable = _MulticastChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 140, 1)
)
if mibBuilder.loadTexts:
    multicastChannelTable.setStatus("current")
_MulticastChannelEntry_Object = MibTableRow
multicastChannelEntry = _MulticastChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 140, 1, 1)
)
multicastChannelEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "multicastChannelStartIp"),
    (0, "ZYXEL-olt1408-MIB", "multicastChannelEndIp"),
    (0, "ZYXEL-olt1408-MIB", "multicastChannelSvid"),
    (0, "ZYXEL-olt1408-MIB", "multicastChannelCvid"),
)
if mibBuilder.loadTexts:
    multicastChannelEntry.setStatus("current")
_MulticastChannelStartIp_Type = IpAddress
_MulticastChannelStartIp_Object = MibTableColumn
multicastChannelStartIp = _MulticastChannelStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 140, 1, 1, 1),
    _MulticastChannelStartIp_Type()
)
multicastChannelStartIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastChannelStartIp.setStatus("current")
_MulticastChannelEndIp_Type = IpAddress
_MulticastChannelEndIp_Object = MibTableColumn
multicastChannelEndIp = _MulticastChannelEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 140, 1, 1, 2),
    _MulticastChannelEndIp_Type()
)
multicastChannelEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastChannelEndIp.setStatus("current")


class _MulticastChannelSvid_Type(Integer32):
    """Custom type multicastChannelSvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_MulticastChannelSvid_Type.__name__ = "Integer32"
_MulticastChannelSvid_Object = MibTableColumn
multicastChannelSvid = _MulticastChannelSvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 140, 1, 1, 3),
    _MulticastChannelSvid_Type()
)
multicastChannelSvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastChannelSvid.setStatus("current")


class _MulticastChannelCvid_Type(Integer32):
    """Custom type multicastChannelCvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MulticastChannelCvid_Type.__name__ = "Integer32"
_MulticastChannelCvid_Object = MibTableColumn
multicastChannelCvid = _MulticastChannelCvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 140, 1, 1, 4),
    _MulticastChannelCvid_Type()
)
multicastChannelCvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastChannelCvid.setStatus("current")


class _MulticastChannelPbit_Type(Integer32):
    """Custom type multicastChannelPbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MulticastChannelPbit_Type.__name__ = "Integer32"
_MulticastChannelPbit_Object = MibTableColumn
multicastChannelPbit = _MulticastChannelPbit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 140, 1, 1, 5),
    _MulticastChannelPbit_Type()
)
multicastChannelPbit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastChannelPbit.setStatus("current")
_MulticastChannelSrcIp_Type = IpAddress
_MulticastChannelSrcIp_Object = MibTableColumn
multicastChannelSrcIp = _MulticastChannelSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 140, 1, 1, 6),
    _MulticastChannelSrcIp_Type()
)
multicastChannelSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastChannelSrcIp.setStatus("current")


class _MulticastChannelPkgMember_Type(Integer32):
    """Custom type multicastChannelPkgMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_MulticastChannelPkgMember_Type.__name__ = "Integer32"
_MulticastChannelPkgMember_Object = MibTableColumn
multicastChannelPkgMember = _MulticastChannelPkgMember_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 140, 1, 1, 7),
    _MulticastChannelPkgMember_Type()
)
multicastChannelPkgMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastChannelPkgMember.setStatus("current")


class _MulticastChannelPreviewDuration_Type(Integer32):
    """Custom type multicastChannelPreviewDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6000),
    )


_MulticastChannelPreviewDuration_Type.__name__ = "Integer32"
_MulticastChannelPreviewDuration_Object = MibTableColumn
multicastChannelPreviewDuration = _MulticastChannelPreviewDuration_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 140, 1, 1, 8),
    _MulticastChannelPreviewDuration_Type()
)
multicastChannelPreviewDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastChannelPreviewDuration.setStatus("current")


class _MulticastChannelPreviewCount_Type(Integer32):
    """Custom type multicastChannelPreviewCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MulticastChannelPreviewCount_Type.__name__ = "Integer32"
_MulticastChannelPreviewCount_Object = MibTableColumn
multicastChannelPreviewCount = _MulticastChannelPreviewCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 140, 1, 1, 9),
    _MulticastChannelPreviewCount_Type()
)
multicastChannelPreviewCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastChannelPreviewCount.setStatus("current")


class _MulticastChannelPreviewBlackout_Type(Integer32):
    """Custom type multicastChannelPreviewBlackout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_MulticastChannelPreviewBlackout_Type.__name__ = "Integer32"
_MulticastChannelPreviewBlackout_Object = MibTableColumn
multicastChannelPreviewBlackout = _MulticastChannelPreviewBlackout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 140, 1, 1, 10),
    _MulticastChannelPreviewBlackout_Type()
)
multicastChannelPreviewBlackout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastChannelPreviewBlackout.setStatus("current")
_MulticastChannelRowStatus_Type = RowStatus
_MulticastChannelRowStatus_Object = MibTableColumn
multicastChannelRowStatus = _MulticastChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 140, 1, 1, 11),
    _MulticastChannelRowStatus_Type()
)
multicastChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastChannelRowStatus.setStatus("current")
_MulticastChannelCacProf_Type = DisplayString
_MulticastChannelCacProf_Object = MibTableColumn
multicastChannelCacProf = _MulticastChannelCacProf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 140, 1, 1, 12),
    _MulticastChannelCacProf_Type()
)
multicastChannelCacProf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastChannelCacProf.setStatus("current")
_PonSetup_ObjectIdentity = ObjectIdentity
ponSetup = _PonSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142)
)
_PonTable_ObjectIdentity = ObjectIdentity
ponTable = _PonTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1)
)
_PonSetupTable_Object = MibTable
ponSetupTable = _PonSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 1)
)
if mibBuilder.loadTexts:
    ponSetupTable.setStatus("current")
_PonSetupEntry_Object = MibTableRow
ponSetupEntry = _PonSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 1, 1)
)
ponSetupEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    ponSetupEntry.setStatus("current")
_TransceiverTxDisable_Type = EnabledStatus
_TransceiverTxDisable_Object = MibTableColumn
transceiverTxDisable = _TransceiverTxDisable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 1, 1, 1),
    _TransceiverTxDisable_Type()
)
transceiverTxDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transceiverTxDisable.setStatus("current")
_InO7State_Type = DisplayString
_InO7State_Object = MibTableColumn
inO7State = _InO7State_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 1, 1, 2),
    _InO7State_Type()
)
inO7State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inO7State.setStatus("current")
_OutO7State_Type = DisplayString
_OutO7State_Object = MibTableColumn
outO7State = _OutO7State_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 1, 1, 3),
    _OutO7State_Type()
)
outO7State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outO7State.setStatus("current")


class _LinkState_Type(Integer32):
    """Custom type linkState based on Integer32"""
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


_LinkState_Type.__name__ = "Integer32"
_LinkState_Object = MibTableColumn
linkState = _LinkState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 1, 1, 4),
    _LinkState_Type()
)
linkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkState.setStatus("current")
_AvailableBandwidth_Type = Integer32
_AvailableBandwidth_Object = MibTableColumn
availableBandwidth = _AvailableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 1, 1, 5),
    _AvailableBandwidth_Type()
)
availableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availableBandwidth.setStatus("current")


class _DelimiterDetected_Type(Integer32):
    """Custom type delimiterDetected based on Integer32"""
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


_DelimiterDetected_Type.__name__ = "Integer32"
_DelimiterDetected_Object = MibTableColumn
delimiterDetected = _DelimiterDetected_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 1, 1, 6),
    _DelimiterDetected_Type()
)
delimiterDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delimiterDetected.setStatus("current")
_PonConfigTable_Object = MibTable
ponConfigTable = _PonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 2)
)
if mibBuilder.loadTexts:
    ponConfigTable.setStatus("current")
_PonConfigEntry_Object = MibTableRow
ponConfigEntry = _PonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 2, 1)
)
ponConfigEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    ponConfigEntry.setStatus("current")


class _TransceiverType_Type(Integer32):
    """Custom type transceiverType based on Integer32"""
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("ligent", 0),
          ("luminent", 1),
          ("fiberxon", 2),
          ("fujitsu", 3),
          ("ligentA", 4),
          ("ligentB", 5),
          ("luminentA", 6),
          ("luminentB", 7),
          ("fiberxonA", 8),
          ("fujitsuA", 9),
          ("nec", 10),
          ("neoptec", 11),
          ("ligentC", 12),
          ("fiberxonB", 13),
          ("fujitsu30537", 14),
          ("neophotonicsA", 15),
          ("neophotonicsB", 16),
          ("neophotonicsC", 17),
          ("superxon", 18),
          ("wtd", 19),
          ("delta", 20),
          ("no1", 21),
          ("no2", 22),
          ("none", 23))
    )


_TransceiverType_Type.__name__ = "Integer32"
_TransceiverType_Object = MibTableColumn
transceiverType = _TransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 2, 1, 1),
    _TransceiverType_Type()
)
transceiverType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transceiverType.setStatus("current")


class _RegisterMethod_Type(Integer32):
    """Custom type registerMethod based on Integer32"""
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
        *(("methodA", 0),
          ("methodC", 1),
          ("methodCAutolock", 2),
          ("methodD", 3),
          ("methodE", 4))
    )


_RegisterMethod_Type.__name__ = "Integer32"
_RegisterMethod_Object = MibTableColumn
registerMethod = _RegisterMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 2, 1, 2),
    _RegisterMethod_Type()
)
registerMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    registerMethod.setStatus("current")
_PonConfigRowStatus_Type = RowStatus
_PonConfigRowStatus_Object = MibTableColumn
ponConfigRowStatus = _PonConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 2, 1, 3),
    _PonConfigRowStatus_Type()
)
ponConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ponConfigRowStatus.setStatus("current")


class _TemplateOption_Type(Integer32):
    """Custom type templateOption based on Integer32"""
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
        *(("template121", 1),
          ("template122", 2),
          ("template123", 3),
          ("template124", 4),
          ("template125", 5),
          ("template126", 6),
          ("template127", 7),
          ("template128", 8))
    )


_TemplateOption_Type.__name__ = "Integer32"
_TemplateOption_Object = MibTableColumn
templateOption = _TemplateOption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 2, 1, 4),
    _TemplateOption_Type()
)
templateOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    templateOption.setStatus("current")
_OntTemplate_Type = EnabledStatus
_OntTemplate_Object = MibTableColumn
ontTemplate = _OntTemplate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 2, 1, 5),
    _OntTemplate_Type()
)
ontTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontTemplate.setStatus("current")
_FecMode_Type = EnabledStatus
_FecMode_Object = MibTableColumn
fecMode = _FecMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 2, 1, 6),
    _FecMode_Type()
)
fecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fecMode.setStatus("current")


class _RangingDistance_Type(Integer32):
    """Custom type rangingDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 60),
    )


_RangingDistance_Type.__name__ = "Integer32"
_RangingDistance_Object = MibTableColumn
rangingDistance = _RangingDistance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 2, 1, 7),
    _RangingDistance_Type()
)
rangingDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rangingDistance.setStatus("current")
_BipErrThres_Type = Unsigned32
_BipErrThres_Object = MibTableColumn
bipErrThres = _BipErrThres_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 2, 1, 8),
    _BipErrThres_Type()
)
bipErrThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bipErrThres.setStatus("current")
_FecCorrByteThres_Type = Unsigned32
_FecCorrByteThres_Object = MibTableColumn
fecCorrByteThres = _FecCorrByteThres_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 2, 1, 9),
    _FecCorrByteThres_Type()
)
fecCorrByteThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fecCorrByteThres.setStatus("current")
_FecCorrCodeWordThres_Type = Unsigned32
_FecCorrCodeWordThres_Object = MibTableColumn
fecCorrCodeWordThres = _FecCorrCodeWordThres_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 2, 1, 10),
    _FecCorrCodeWordThres_Type()
)
fecCorrCodeWordThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fecCorrCodeWordThres.setStatus("current")
_FecUncorrCodeWordThres_Type = Unsigned32
_FecUncorrCodeWordThres_Object = MibTableColumn
fecUncorrCodeWordThres = _FecUncorrCodeWordThres_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 2, 1, 11),
    _FecUncorrCodeWordThres_Type()
)
fecUncorrCodeWordThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fecUncorrCodeWordThres.setStatus("current")
_ReiCounterThres_Type = Unsigned32
_ReiCounterThres_Object = MibTableColumn
reiCounterThres = _ReiCounterThres_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 2, 1, 12),
    _ReiCounterThres_Type()
)
reiCounterThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reiCounterThres.setStatus("current")
_TcaStatus_Type = EnabledStatus
_TcaStatus_Object = MibTableColumn
tcaStatus = _TcaStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 2, 1, 13),
    _TcaStatus_Type()
)
tcaStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcaStatus.setStatus("current")
_UnregisterOntTable_Object = MibTable
unregisterOntTable = _UnregisterOntTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 3)
)
if mibBuilder.loadTexts:
    unregisterOntTable.setStatus("current")
_UnregisterOntEntry_Object = MibTableRow
unregisterOntEntry = _UnregisterOntEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 3, 1)
)
unregisterOntEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "unregisterOntIndex"),
)
if mibBuilder.loadTexts:
    unregisterOntEntry.setStatus("current")
_UnregisterOntSerialNumber_Type = DisplayString
_UnregisterOntSerialNumber_Object = MibTableColumn
unregisterOntSerialNumber = _UnregisterOntSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 3, 1, 1),
    _UnregisterOntSerialNumber_Type()
)
unregisterOntSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unregisterOntSerialNumber.setStatus("current")
_UnregisterOntPassword_Type = DisplayString
_UnregisterOntPassword_Object = MibTableColumn
unregisterOntPassword = _UnregisterOntPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 3, 1, 2),
    _UnregisterOntPassword_Type()
)
unregisterOntPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unregisterOntPassword.setStatus("current")


class _UnregisterOntStatus_Type(Integer32):
    """Custom type unregisterOntStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("active", 1))
    )


_UnregisterOntStatus_Type.__name__ = "Integer32"
_UnregisterOntStatus_Object = MibTableColumn
unregisterOntStatus = _UnregisterOntStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 3, 1, 3),
    _UnregisterOntStatus_Type()
)
unregisterOntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unregisterOntStatus.setStatus("current")
_UnregisterOntIndex_Type = Integer32
_UnregisterOntIndex_Object = MibTableColumn
unregisterOntIndex = _UnregisterOntIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 3, 1, 4),
    _UnregisterOntIndex_Type()
)
unregisterOntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unregisterOntIndex.setStatus("current")
_PonProtectionTable_Object = MibTable
ponProtectionTable = _PonProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 4)
)
if mibBuilder.loadTexts:
    ponProtectionTable.setStatus("current")
_PonProtectionEntry_Object = MibTableRow
ponProtectionEntry = _PonProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 4, 1)
)
ponProtectionEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    ponProtectionEntry.setStatus("current")
_ProtectionPort_Type = Integer32
_ProtectionPort_Object = MibTableColumn
protectionPort = _ProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 4, 1, 1),
    _ProtectionPort_Type()
)
protectionPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protectionPort.setStatus("current")
_PonProtectConfigRowStatus_Type = RowStatus
_PonProtectConfigRowStatus_Object = MibTableColumn
ponProtectConfigRowStatus = _PonProtectConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 4, 1, 2),
    _PonProtectConfigRowStatus_Type()
)
ponProtectConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ponProtectConfigRowStatus.setStatus("current")
_PonRogueOnuTable_Object = MibTable
ponRogueOnuTable = _PonRogueOnuTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 5)
)
if mibBuilder.loadTexts:
    ponRogueOnuTable.setStatus("current")
_PonRogueOnuEntry_Object = MibTableRow
ponRogueOnuEntry = _PonRogueOnuEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 5, 1)
)
ponRogueOnuEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    ponRogueOnuEntry.setStatus("current")


class _RogueDetect_Type(Integer32):
    """Custom type rogueDetect based on Integer32"""
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


_RogueDetect_Type.__name__ = "Integer32"
_RogueDetect_Object = MibTableColumn
rogueDetect = _RogueDetect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 142, 1, 5, 1, 1),
    _RogueDetect_Type()
)
rogueDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rogueDetect.setStatus("current")
_OntFwUpgrade_ObjectIdentity = ObjectIdentity
ontFwUpgrade = _OntFwUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 143)
)
_OntFwUpgradeSetup_ObjectIdentity = ObjectIdentity
ontFwUpgradeSetup = _OntFwUpgradeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 143, 1)
)
_OntImageVersion_Type = DisplayString
_OntImageVersion_Object = MibScalar
ontImageVersion = _OntImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 143, 1, 1),
    _OntImageVersion_Type()
)
ontImageVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontImageVersion.setStatus("current")


class _ReleaseOntImage_Type(Integer32):
    """Custom type releaseOntImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notRelease", 0),
          ("release", 1))
    )


_ReleaseOntImage_Type.__name__ = "Integer32"
_ReleaseOntImage_Object = MibScalar
releaseOntImage = _ReleaseOntImage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 143, 1, 3),
    _ReleaseOntImage_Type()
)
releaseOntImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    releaseOntImage.setStatus("current")


class _AutoReboot_Type(Integer32):
    """Custom type autoReboot based on Integer32"""
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


_AutoReboot_Type.__name__ = "Integer32"
_AutoReboot_Object = MibScalar
autoReboot = _AutoReboot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 143, 1, 4),
    _AutoReboot_Type()
)
autoReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoReboot.setStatus("current")
_OntFwUpgradeAction_ObjectIdentity = ObjectIdentity
ontFwUpgradeAction = _OntFwUpgradeAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 143, 2)
)


class _CheckOntFwPerPon_Type(Bits):
    """Custom type checkOntFwPerPon based on Bits"""
    namedValues = NamedValues(
        *(("pon1", 0),
          ("pon2", 1),
          ("pon3", 2),
          ("pon4", 3),
          ("pon5", 4),
          ("pon6", 5),
          ("pon7", 6),
          ("pon8", 7))
    )

_CheckOntFwPerPon_Type.__name__ = "Bits"
_CheckOntFwPerPon_Object = MibScalar
checkOntFwPerPon = _CheckOntFwPerPon_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 143, 2, 1),
    _CheckOntFwPerPon_Type()
)
checkOntFwPerPon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    checkOntFwPerPon.setStatus("current")


class _OntFwUpgradeClearStatusPerPon_Type(Bits):
    """Custom type ontFwUpgradeClearStatusPerPon based on Bits"""
    namedValues = NamedValues(
        *(("pon1", 0),
          ("pon2", 1),
          ("pon3", 2),
          ("pon4", 3),
          ("pon5", 4),
          ("pon6", 5),
          ("pon7", 6),
          ("pon8", 7))
    )

_OntFwUpgradeClearStatusPerPon_Type.__name__ = "Bits"
_OntFwUpgradeClearStatusPerPon_Object = MibScalar
ontFwUpgradeClearStatusPerPon = _OntFwUpgradeClearStatusPerPon_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 143, 2, 2),
    _OntFwUpgradeClearStatusPerPon_Type()
)
ontFwUpgradeClearStatusPerPon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontFwUpgradeClearStatusPerPon.setStatus("current")


class _OntFwUpgradeClearQueuePerPon_Type(Bits):
    """Custom type ontFwUpgradeClearQueuePerPon based on Bits"""
    namedValues = NamedValues(
        *(("pon1", 0),
          ("pon2", 1),
          ("pon3", 2),
          ("pon4", 3),
          ("pon5", 4),
          ("pon6", 5),
          ("pon7", 6),
          ("pon8", 7))
    )

_OntFwUpgradeClearQueuePerPon_Type.__name__ = "Bits"
_OntFwUpgradeClearQueuePerPon_Object = MibScalar
ontFwUpgradeClearQueuePerPon = _OntFwUpgradeClearQueuePerPon_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 143, 2, 3),
    _OntFwUpgradeClearQueuePerPon_Type()
)
ontFwUpgradeClearQueuePerPon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ontFwUpgradeClearQueuePerPon.setStatus("current")
_OntFwUpgradeInfo_ObjectIdentity = ObjectIdentity
ontFwUpgradeInfo = _OntFwUpgradeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 143, 3)
)
_NumOfOntInQueue_Type = Integer32
_NumOfOntInQueue_Object = MibScalar
numOfOntInQueue = _NumOfOntInQueue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 143, 3, 1),
    _NumOfOntInQueue_Type()
)
numOfOntInQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfOntInQueue.setStatus("current")
_PortBridgeSetup_ObjectIdentity = ObjectIdentity
portBridgeSetup = _PortBridgeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 144)
)
_PortBridgeState_Type = EnabledStatus
_PortBridgeState_Object = MibScalar
portBridgeState = _PortBridgeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 144, 1),
    _PortBridgeState_Type()
)
portBridgeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBridgeState.setStatus("current")
_PortBridgePortTable_Object = MibTable
portBridgePortTable = _PortBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 144, 2)
)
if mibBuilder.loadTexts:
    portBridgePortTable.setStatus("current")
_PortBridgePortEntry_Object = MibTableRow
portBridgePortEntry = _PortBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 144, 2, 1)
)
portBridgePortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portBridgePortEntry.setStatus("current")
_PortBridgePortState_Type = EnabledStatus
_PortBridgePortState_Object = MibTableColumn
portBridgePortState = _PortBridgePortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 144, 2, 1, 1),
    _PortBridgePortState_Type()
)
portBridgePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBridgePortState.setStatus("current")
_Cdr_ObjectIdentity = ObjectIdentity
cdr = _Cdr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 145)
)
_CdrIgmp_ObjectIdentity = ObjectIdentity
cdrIgmp = _CdrIgmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 145, 1)
)
_CdrIgmpSetup_ObjectIdentity = ObjectIdentity
cdrIgmpSetup = _CdrIgmpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 145, 1, 1)
)


class _CdrIgmpActive_Type(Integer32):
    """Custom type cdrIgmpActive based on Integer32"""
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


_CdrIgmpActive_Type.__name__ = "Integer32"
_CdrIgmpActive_Object = MibScalar
cdrIgmpActive = _CdrIgmpActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 145, 1, 1, 1),
    _CdrIgmpActive_Type()
)
cdrIgmpActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrIgmpActive.setStatus("current")
_CdrIgmpLogSize_Type = Integer32
_CdrIgmpLogSize_Object = MibScalar
cdrIgmpLogSize = _CdrIgmpLogSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 145, 1, 1, 2),
    _CdrIgmpLogSize_Type()
)
cdrIgmpLogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrIgmpLogSize.setStatus("current")
_CdrIgmpStatus_ObjectIdentity = ObjectIdentity
cdrIgmpStatus = _CdrIgmpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 145, 1, 2)
)
_CdrIgmpStatusTable_Object = MibTable
cdrIgmpStatusTable = _CdrIgmpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 145, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cdrIgmpStatusTable.setStatus("current")
_CdrIgmpStatusEntry_Object = MibTableRow
cdrIgmpStatusEntry = _CdrIgmpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 145, 1, 2, 1, 1)
)
cdrIgmpStatusEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "cdrIgmpStatusEntryIndex"),
)
if mibBuilder.loadTexts:
    cdrIgmpStatusEntry.setStatus("current")
_CdrIgmpStatusEntryIndex_Type = Integer32
_CdrIgmpStatusEntryIndex_Object = MibTableColumn
cdrIgmpStatusEntryIndex = _CdrIgmpStatusEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 145, 1, 2, 1, 1, 1),
    _CdrIgmpStatusEntryIndex_Type()
)
cdrIgmpStatusEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIgmpStatusEntryIndex.setStatus("current")
_CdrIgmpEventTime_Type = DisplayString
_CdrIgmpEventTime_Object = MibTableColumn
cdrIgmpEventTime = _CdrIgmpEventTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 145, 1, 2, 1, 1, 2),
    _CdrIgmpEventTime_Type()
)
cdrIgmpEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIgmpEventTime.setStatus("current")


class _CdrIgmpEventType_Type(Integer32):
    """Custom type cdrIgmpEventType based on Integer32"""
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
        *(("leaveAutonomous", 0),
          ("leaveTimeout", 1),
          ("leaveEnforce", 2),
          ("joinSuccess", 3),
          ("joinFail", 4),
          ("unknown", 5))
    )


_CdrIgmpEventType_Type.__name__ = "Integer32"
_CdrIgmpEventType_Object = MibTableColumn
cdrIgmpEventType = _CdrIgmpEventType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 145, 1, 2, 1, 1, 3),
    _CdrIgmpEventType_Type()
)
cdrIgmpEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIgmpEventType.setStatus("current")


class _CdrIgmpGroup_Type(InetAddress):
    """Custom type cdrIgmpGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CdrIgmpGroup_Type.__name__ = "InetAddress"
_CdrIgmpGroup_Object = MibTableColumn
cdrIgmpGroup = _CdrIgmpGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 145, 1, 2, 1, 1, 4),
    _CdrIgmpGroup_Type()
)
cdrIgmpGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIgmpGroup.setStatus("current")


class _CdrIgmpPrivilege_Type(Integer32):
    """Custom type cdrIgmpPrivilege based on Integer32"""
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
        *(("permit", 0),
          ("preview", 1),
          ("reject", 2),
          ("unknown", 3))
    )


_CdrIgmpPrivilege_Type.__name__ = "Integer32"
_CdrIgmpPrivilege_Object = MibTableColumn
cdrIgmpPrivilege = _CdrIgmpPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 145, 1, 2, 1, 1, 5),
    _CdrIgmpPrivilege_Type()
)
cdrIgmpPrivilege.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIgmpPrivilege.setStatus("current")
_CdrIgmpUptime_Type = DisplayString
_CdrIgmpUptime_Object = MibTableColumn
cdrIgmpUptime = _CdrIgmpUptime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 145, 1, 2, 1, 1, 6),
    _CdrIgmpUptime_Type()
)
cdrIgmpUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIgmpUptime.setStatus("current")
_CdrIgmpChannel_Type = DisplayString
_CdrIgmpChannel_Object = MibTableColumn
cdrIgmpChannel = _CdrIgmpChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 145, 1, 2, 1, 1, 7),
    _CdrIgmpChannel_Type()
)
cdrIgmpChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIgmpChannel.setStatus("current")
_ClassifierSetup_ObjectIdentity = ObjectIdentity
classifierSetup = _ClassifierSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146)
)
_ClassifierRuleTable_Object = MibTable
classifierRuleTable = _ClassifierRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1)
)
if mibBuilder.loadTexts:
    classifierRuleTable.setStatus("current")
_ClassifierRuleEntry_Object = MibTableRow
classifierRuleEntry = _ClassifierRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1)
)
classifierRuleEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "classifierName"),
)
if mibBuilder.loadTexts:
    classifierRuleEntry.setStatus("current")
_ClassifierName_Type = DisplayString
_ClassifierName_Object = MibTableColumn
classifierName = _ClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 1),
    _ClassifierName_Type()
)
classifierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classifierName.setStatus("current")
_ClassifierEnable_Type = EnabledStatus
_ClassifierEnable_Object = MibTableColumn
classifierEnable = _ClassifierEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 2),
    _ClassifierEnable_Type()
)
classifierEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierEnable.setStatus("current")


class _ClassifierPacketFormat_Type(Integer32):
    """Custom type classifierPacketFormat based on Integer32"""
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
        *(("all", 1),
          ("ethernetIIUntagged", 2),
          ("ethernetIITagged", 3),
          ("ethernet802dot3Untagged", 4),
          ("ethernet802dot3Tagged", 5))
    )


_ClassifierPacketFormat_Type.__name__ = "Integer32"
_ClassifierPacketFormat_Object = MibTableColumn
classifierPacketFormat = _ClassifierPacketFormat_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 3),
    _ClassifierPacketFormat_Type()
)
classifierPacketFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierPacketFormat.setStatus("current")
_ClassifierVlanId_Type = Integer32
_ClassifierVlanId_Object = MibTableColumn
classifierVlanId = _ClassifierVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 4),
    _ClassifierVlanId_Type()
)
classifierVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierVlanId.setStatus("current")
_Classifier8021pPriority_Type = Integer32
_Classifier8021pPriority_Object = MibTableColumn
classifier8021pPriority = _Classifier8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 5),
    _Classifier8021pPriority_Type()
)
classifier8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifier8021pPriority.setStatus("current")
_ClassifierEtherType_Type = Integer32
_ClassifierEtherType_Object = MibTableColumn
classifierEtherType = _ClassifierEtherType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 6),
    _ClassifierEtherType_Type()
)
classifierEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierEtherType.setStatus("current")
_ClassifierSrcMAC_Type = MacAddress
_ClassifierSrcMAC_Object = MibTableColumn
classifierSrcMAC = _ClassifierSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 7),
    _ClassifierSrcMAC_Type()
)
classifierSrcMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierSrcMAC.setStatus("current")
_ClassifierIncomingPort_Type = Integer32
_ClassifierIncomingPort_Object = MibTableColumn
classifierIncomingPort = _ClassifierIncomingPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 8),
    _ClassifierIncomingPort_Type()
)
classifierIncomingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierIncomingPort.setStatus("current")
_ClassifierDstMAC_Type = MacAddress
_ClassifierDstMAC_Object = MibTableColumn
classifierDstMAC = _ClassifierDstMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 9),
    _ClassifierDstMAC_Type()
)
classifierDstMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierDstMAC.setStatus("current")
_ClassifierDSCP_Type = Integer32
_ClassifierDSCP_Object = MibTableColumn
classifierDSCP = _ClassifierDSCP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 10),
    _ClassifierDSCP_Type()
)
classifierDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierDSCP.setStatus("current")
_ClassifierIpProtocol_Type = Integer32
_ClassifierIpProtocol_Object = MibTableColumn
classifierIpProtocol = _ClassifierIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 11),
    _ClassifierIpProtocol_Type()
)
classifierIpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierIpProtocol.setStatus("current")
_ClassifierEstablishOnly_Type = EnabledStatus
_ClassifierEstablishOnly_Object = MibTableColumn
classifierEstablishOnly = _ClassifierEstablishOnly_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 12),
    _ClassifierEstablishOnly_Type()
)
classifierEstablishOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierEstablishOnly.setStatus("current")
_ClassifierSrcIp_Type = IpAddress
_ClassifierSrcIp_Object = MibTableColumn
classifierSrcIp = _ClassifierSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 13),
    _ClassifierSrcIp_Type()
)
classifierSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierSrcIp.setStatus("current")
_ClassifierSrcIpMask_Type = Integer32
_ClassifierSrcIpMask_Object = MibTableColumn
classifierSrcIpMask = _ClassifierSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 14),
    _ClassifierSrcIpMask_Type()
)
classifierSrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierSrcIpMask.setStatus("current")
_ClassifierSrcSocket_Type = Integer32
_ClassifierSrcSocket_Object = MibTableColumn
classifierSrcSocket = _ClassifierSrcSocket_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 15),
    _ClassifierSrcSocket_Type()
)
classifierSrcSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierSrcSocket.setStatus("current")
_ClassifierDstIp_Type = IpAddress
_ClassifierDstIp_Object = MibTableColumn
classifierDstIp = _ClassifierDstIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 16),
    _ClassifierDstIp_Type()
)
classifierDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierDstIp.setStatus("current")
_ClassifierDstIpMask_Type = Integer32
_ClassifierDstIpMask_Object = MibTableColumn
classifierDstIpMask = _ClassifierDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 17),
    _ClassifierDstIpMask_Type()
)
classifierDstIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierDstIpMask.setStatus("current")
_ClassifierDstSocket_Type = Integer32
_ClassifierDstSocket_Object = MibTableColumn
classifierDstSocket = _ClassifierDstSocket_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 18),
    _ClassifierDstSocket_Type()
)
classifierDstSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierDstSocket.setStatus("current")
_ClassifierRowstatus_Type = RowStatus
_ClassifierRowstatus_Object = MibTableColumn
classifierRowstatus = _ClassifierRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 19),
    _ClassifierRowstatus_Type()
)
classifierRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierRowstatus.setStatus("current")
_ClassifierIp6Dscp_Type = Integer32
_ClassifierIp6Dscp_Object = MibTableColumn
classifierIp6Dscp = _ClassifierIp6Dscp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 20),
    _ClassifierIp6Dscp_Type()
)
classifierIp6Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierIp6Dscp.setStatus("current")
_ClassifierIp6NextHeader_Type = Integer32
_ClassifierIp6NextHeader_Object = MibTableColumn
classifierIp6NextHeader = _ClassifierIp6NextHeader_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 21),
    _ClassifierIp6NextHeader_Type()
)
classifierIp6NextHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierIp6NextHeader.setStatus("current")
_ClassifierIp6EstbOnly_Type = Integer32
_ClassifierIp6EstbOnly_Object = MibTableColumn
classifierIp6EstbOnly = _ClassifierIp6EstbOnly_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 22),
    _ClassifierIp6EstbOnly_Type()
)
classifierIp6EstbOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierIp6EstbOnly.setStatus("current")
_ClassifierSrcIp6_Type = DisplayString
_ClassifierSrcIp6_Object = MibTableColumn
classifierSrcIp6 = _ClassifierSrcIp6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 23),
    _ClassifierSrcIp6_Type()
)
classifierSrcIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierSrcIp6.setStatus("current")
_ClassifierSrcIp6PrefixLen_Type = Integer32
_ClassifierSrcIp6PrefixLen_Object = MibTableColumn
classifierSrcIp6PrefixLen = _ClassifierSrcIp6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 24),
    _ClassifierSrcIp6PrefixLen_Type()
)
classifierSrcIp6PrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierSrcIp6PrefixLen.setStatus("current")
_ClassifierDstIp6_Type = DisplayString
_ClassifierDstIp6_Object = MibTableColumn
classifierDstIp6 = _ClassifierDstIp6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 25),
    _ClassifierDstIp6_Type()
)
classifierDstIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierDstIp6.setStatus("current")
_ClassifierDstIp6PrefixLen_Type = Integer32
_ClassifierDstIp6PrefixLen_Object = MibTableColumn
classifierDstIp6PrefixLen = _ClassifierDstIp6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 26),
    _ClassifierDstIp6PrefixLen_Type()
)
classifierDstIp6PrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierDstIp6PrefixLen.setStatus("current")
_ClassifierOutgoingPort_Type = Integer32
_ClassifierOutgoingPort_Object = MibTableColumn
classifierOutgoingPort = _ClassifierOutgoingPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 1, 1, 27),
    _ClassifierOutgoingPort_Type()
)
classifierOutgoingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierOutgoingPort.setStatus("current")
_ClassifierRuleSet_Type = DisplayString
_ClassifierRuleSet_Object = MibScalar
classifierRuleSet = _ClassifierRuleSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 146, 2),
    _ClassifierRuleSet_Type()
)
classifierRuleSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierRuleSet.setStatus("current")
_PolicySetup_ObjectIdentity = ObjectIdentity
policySetup = _PolicySetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147)
)
_PolicyTable_Object = MibTable
policyTable = _PolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1)
)
if mibBuilder.loadTexts:
    policyTable.setStatus("current")
_PolicyEntry_Object = MibTableRow
policyEntry = _PolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1)
)
policyEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "policyName"),
)
if mibBuilder.loadTexts:
    policyEntry.setStatus("current")
_PolicyName_Type = DisplayString
_PolicyName_Object = MibTableColumn
policyName = _PolicyName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 1),
    _PolicyName_Type()
)
policyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyName.setStatus("current")
_PolicyEnable_Type = EnabledStatus
_PolicyEnable_Object = MibTableColumn
policyEnable = _PolicyEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 2),
    _PolicyEnable_Type()
)
policyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyEnable.setStatus("current")
_PolicyClassifier_Type = DisplayString
_PolicyClassifier_Object = MibTableColumn
policyClassifier = _PolicyClassifier_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 3),
    _PolicyClassifier_Type()
)
policyClassifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyClassifier.setStatus("current")
_PolicyVlanId_Type = Integer32
_PolicyVlanId_Object = MibTableColumn
policyVlanId = _PolicyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 4),
    _PolicyVlanId_Type()
)
policyVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyVlanId.setStatus("current")
_PolicyEgressPort_Type = Integer32
_PolicyEgressPort_Object = MibTableColumn
policyEgressPort = _PolicyEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 5),
    _PolicyEgressPort_Type()
)
policyEgressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyEgressPort.setStatus("current")


class _PolicyOutPktFormat_Type(Integer32):
    """Custom type policyOutPktFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tag", 1),
          ("untag", 2))
    )


_PolicyOutPktFormat_Type.__name__ = "Integer32"
_PolicyOutPktFormat_Object = MibTableColumn
policyOutPktFormat = _PolicyOutPktFormat_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 6),
    _PolicyOutPktFormat_Type()
)
policyOutPktFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyOutPktFormat.setStatus("current")
_Policy8021pPriority_Type = Integer32
_Policy8021pPriority_Object = MibTableColumn
policy8021pPriority = _Policy8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 7),
    _Policy8021pPriority_Type()
)
policy8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policy8021pPriority.setStatus("current")
_PolicyDSCP_Type = Integer32
_PolicyDSCP_Object = MibTableColumn
policyDSCP = _PolicyDSCP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 8),
    _PolicyDSCP_Type()
)
policyDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyDSCP.setStatus("current")
_PolicyTOS_Type = Integer32
_PolicyTOS_Object = MibTableColumn
policyTOS = _PolicyTOS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 9),
    _PolicyTOS_Type()
)
policyTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyTOS.setStatus("current")
_PolicySir_Type = Integer32
_PolicySir_Object = MibTableColumn
policySir = _PolicySir_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 10),
    _PolicySir_Type()
)
policySir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policySir.setStatus("current")
_PolicyPir_Type = Integer32
_PolicyPir_Object = MibTableColumn
policyPir = _PolicyPir_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 11),
    _PolicyPir_Type()
)
policyPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyPir.setStatus("current")
_PolicyOutOfProfileDSCP_Type = Integer32
_PolicyOutOfProfileDSCP_Object = MibTableColumn
policyOutOfProfileDSCP = _PolicyOutOfProfileDSCP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 12),
    _PolicyOutOfProfileDSCP_Type()
)
policyOutOfProfileDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyOutOfProfileDSCP.setStatus("current")
_PolicyOutOfProfileGpCosqNew_Type = Integer32
_PolicyOutOfProfileGpCosqNew_Object = MibTableColumn
policyOutOfProfileGpCosqNew = _PolicyOutOfProfileGpCosqNew_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 13),
    _PolicyOutOfProfileGpCosqNew_Type()
)
policyOutOfProfileGpCosqNew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyOutOfProfileGpCosqNew.setStatus("current")


class _PolicyForwardingAction_Type(Integer32):
    """Custom type policyForwardingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noChange", 1),
          ("discardThePacket", 2),
          ("doNotDropTheMatchingFramePreviouslyMarkedForDopping", 3))
    )


_PolicyForwardingAction_Type.__name__ = "Integer32"
_PolicyForwardingAction_Object = MibTableColumn
policyForwardingAction = _PolicyForwardingAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 14),
    _PolicyForwardingAction_Type()
)
policyForwardingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyForwardingAction.setStatus("current")


class _PolicyPriorityAction_Type(Integer32):
    """Custom type policyPriorityAction based on Integer32"""
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
        *(("noChange", 1),
          ("setThePackets802dot1Priority", 2),
          ("sendThePacketToPriorityQueue", 3),
          ("replaceThe802dot1PriorityFieldWithTheIpTosValue", 4))
    )


_PolicyPriorityAction_Type.__name__ = "Integer32"
_PolicyPriorityAction_Object = MibTableColumn
policyPriorityAction = _PolicyPriorityAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 15),
    _PolicyPriorityAction_Type()
)
policyPriorityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyPriorityAction.setStatus("current")


class _PolicyDiffServAction_Type(Integer32):
    """Custom type policyDiffServAction based on Integer32"""
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
        *(("noChange", 1),
          ("setThePacketsTosField", 2),
          ("replaceTheIpTosFieldWithThe802dot1PriorityValue", 3),
          ("setTheDiffservCodepointFieldInTheFrame", 4))
    )


_PolicyDiffServAction_Type.__name__ = "Integer32"
_PolicyDiffServAction_Object = MibTableColumn
policyDiffServAction = _PolicyDiffServAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 16),
    _PolicyDiffServAction_Type()
)
policyDiffServAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyDiffServAction.setStatus("current")


class _PolicyOutgoingAction_Type(Bits):
    """Custom type policyOutgoingAction based on Bits"""
    namedValues = NamedValues(
        *(("sendThePacketToTheMirrorPort", 1),
          ("sendThePacketToTheEgressPort", 2),
          ("sendTheMatchingFramesToTheEgressPort", 3),
          ("setThePacketsVlanId", 4))
    )

_PolicyOutgoingAction_Type.__name__ = "Bits"
_PolicyOutgoingAction_Object = MibTableColumn
policyOutgoingAction = _PolicyOutgoingAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 17),
    _PolicyOutgoingAction_Type()
)
policyOutgoingAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyOutgoingAction.setStatus("current")
_PolicyMeteringEnable_Type = Integer32
_PolicyMeteringEnable_Object = MibTableColumn
policyMeteringEnable = _PolicyMeteringEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 18),
    _PolicyMeteringEnable_Type()
)
policyMeteringEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyMeteringEnable.setStatus("current")


class _PolicyOutOfProfileAction_Type(Bits):
    """Custom type policyOutOfProfileAction based on Bits"""
    namedValues = NamedValues(
        *(("dropThePacket", 1),
          ("changeTheDscpValue", 2),
          ("setOutDropPrecedence", 3),
          ("doNotDropTheMatchingFramePreviouslyMarkedForDropping", 4),
          ("setGpToCosqNew", 5))
    )

_PolicyOutOfProfileAction_Type.__name__ = "Bits"
_PolicyOutOfProfileAction_Object = MibTableColumn
policyOutOfProfileAction = _PolicyOutOfProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 19),
    _PolicyOutOfProfileAction_Type()
)
policyOutOfProfileAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyOutOfProfileAction.setStatus("current")
_PolicyRowstatus_Type = RowStatus
_PolicyRowstatus_Object = MibTableColumn
policyRowstatus = _PolicyRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 20),
    _PolicyRowstatus_Type()
)
policyRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyRowstatus.setStatus("current")
_PolicyMirrorPort_Type = Integer32
_PolicyMirrorPort_Object = MibTableColumn
policyMirrorPort = _PolicyMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 1, 1, 21),
    _PolicyMirrorPort_Type()
)
policyMirrorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyMirrorPort.setStatus("current")
_PolicyRuleSet_Type = DisplayString
_PolicyRuleSet_Object = MibScalar
policyRuleSet = _PolicyRuleSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 147, 2),
    _PolicyRuleSet_Type()
)
policyRuleSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyRuleSet.setStatus("current")
_UniPortOpModeSetup_ObjectIdentity = ObjectIdentity
uniPortOpModeSetup = _UniPortOpModeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 148)
)
_UniPortOpModePortTable_Object = MibTable
uniPortOpModePortTable = _UniPortOpModePortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 148, 1)
)
if mibBuilder.loadTexts:
    uniPortOpModePortTable.setStatus("current")
_UniPortOpModePortEntry_Object = MibTableRow
uniPortOpModePortEntry = _UniPortOpModePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 148, 1, 1)
)
uniPortOpModePortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    uniPortOpModePortEntry.setStatus("current")


class _UniPortOpModePortVlanTranslation_Type(Integer32):
    """Custom type uniPortOpModePortVlanTranslation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_UniPortOpModePortVlanTranslation_Type.__name__ = "Integer32"
_UniPortOpModePortVlanTranslation_Object = MibTableColumn
uniPortOpModePortVlanTranslation = _UniPortOpModePortVlanTranslation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 148, 1, 1, 1),
    _UniPortOpModePortVlanTranslation_Type()
)
uniPortOpModePortVlanTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortOpModePortVlanTranslation.setStatus("current")


class _UniPortOpModePortVlanXlateMissDrop_Type(Integer32):
    """Custom type uniPortOpModePortVlanXlateMissDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_UniPortOpModePortVlanXlateMissDrop_Type.__name__ = "Integer32"
_UniPortOpModePortVlanXlateMissDrop_Object = MibTableColumn
uniPortOpModePortVlanXlateMissDrop = _UniPortOpModePortVlanXlateMissDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 148, 1, 1, 2),
    _UniPortOpModePortVlanXlateMissDrop_Type()
)
uniPortOpModePortVlanXlateMissDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortOpModePortVlanXlateMissDrop.setStatus("current")


class _UniPortOpModePortEgrVlanXlateMissDrop_Type(Integer32):
    """Custom type uniPortOpModePortEgrVlanXlateMissDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_UniPortOpModePortEgrVlanXlateMissDrop_Type.__name__ = "Integer32"
_UniPortOpModePortEgrVlanXlateMissDrop_Object = MibTableColumn
uniPortOpModePortEgrVlanXlateMissDrop = _UniPortOpModePortEgrVlanXlateMissDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 148, 1, 1, 3),
    _UniPortOpModePortEgrVlanXlateMissDrop_Type()
)
uniPortOpModePortEgrVlanXlateMissDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortOpModePortEgrVlanXlateMissDrop.setStatus("current")
_MacInfo_ObjectIdentity = ObjectIdentity
macInfo = _MacInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 149)
)
_MacTable_Object = MibTable
macTable = _MacTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 149, 1)
)
if mibBuilder.loadTexts:
    macTable.setStatus("current")
_MacEntry_Object = MibTableRow
macEntry = _MacEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 149, 1, 1)
)
macEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "macVid"),
    (0, "ZYXEL-olt1408-MIB", "macMacAddr"),
)
if mibBuilder.loadTexts:
    macEntry.setStatus("current")
_MacVid_Type = Integer32
_MacVid_Object = MibTableColumn
macVid = _MacVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 149, 1, 1, 1),
    _MacVid_Type()
)
macVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macVid.setStatus("current")
_MacMacAddr_Type = MacAddress
_MacMacAddr_Object = MibTableColumn
macMacAddr = _MacMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 149, 1, 1, 2),
    _MacMacAddr_Type()
)
macMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macMacAddr.setStatus("current")
_MacPort_Type = Integer32
_MacPort_Object = MibTableColumn
macPort = _MacPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 149, 1, 1, 3),
    _MacPort_Type()
)
macPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macPort.setStatus("current")


class _MacType_Type(Integer32):
    """Custom type macType based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("learned", 3),
          ("self", 4),
          ("mgmt", 5))
    )


_MacType_Type.__name__ = "Integer32"
_MacType_Object = MibTableColumn
macType = _MacType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 149, 1, 1, 4),
    _MacType_Type()
)
macType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macType.setStatus("current")
_MacUniportAid_Type = DisplayString
_MacUniportAid_Object = MibTableColumn
macUniportAid = _MacUniportAid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 149, 1, 1, 5),
    _MacUniportAid_Type()
)
macUniportAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macUniportAid.setStatus("current")
_MacGemflow_Type = DisplayString
_MacGemflow_Object = MibTableColumn
macGemflow = _MacGemflow_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 149, 1, 1, 6),
    _MacGemflow_Type()
)
macGemflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macGemflow.setStatus("current")
_AntiMacSpoofSetup_ObjectIdentity = ObjectIdentity
antiMacSpoofSetup = _AntiMacSpoofSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 150)
)
_AntiMacSpoofState_Type = EnabledStatus
_AntiMacSpoofState_Object = MibScalar
antiMacSpoofState = _AntiMacSpoofState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 150, 1),
    _AntiMacSpoofState_Type()
)
antiMacSpoofState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    antiMacSpoofState.setStatus("current")
_AntiMacSpoofPortTable_Object = MibTable
antiMacSpoofPortTable = _AntiMacSpoofPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 150, 2)
)
if mibBuilder.loadTexts:
    antiMacSpoofPortTable.setStatus("current")
_AntiMacSpoofPortEntry_Object = MibTableRow
antiMacSpoofPortEntry = _AntiMacSpoofPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 150, 2, 1)
)
antiMacSpoofPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    antiMacSpoofPortEntry.setStatus("current")
_AntiMacSpoofPortState_Type = EnabledStatus
_AntiMacSpoofPortState_Object = MibTableColumn
antiMacSpoofPortState = _AntiMacSpoofPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 150, 2, 1, 1),
    _AntiMacSpoofPortState_Type()
)
antiMacSpoofPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    antiMacSpoofPortState.setStatus("current")
_ProtectSwitch_ObjectIdentity = ObjectIdentity
protectSwitch = _ProtectSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153)
)
_ProtectSwitchMsc_ObjectIdentity = ObjectIdentity
protectSwitchMsc = _ProtectSwitchMsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153, 1)
)
_ProtectSwitchPon_ObjectIdentity = ObjectIdentity
protectSwitchPon = _ProtectSwitchPon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153, 2)
)
_ProtectSwitchPonTable_Object = MibTable
protectSwitchPonTable = _ProtectSwitchPonTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153, 2, 1)
)
if mibBuilder.loadTexts:
    protectSwitchPonTable.setStatus("current")
_ProtectSwitchPonEntry_Object = MibTableRow
protectSwitchPonEntry = _ProtectSwitchPonEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153, 2, 1, 1)
)
protectSwitchPonEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-olt1408-MIB", "passivePort"),
)
if mibBuilder.loadTexts:
    protectSwitchPonEntry.setStatus("current")
_PassivePort_Type = Integer32
_PassivePort_Object = MibTableColumn
passivePort = _PassivePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153, 2, 1, 1, 1),
    _PassivePort_Type()
)
passivePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    passivePort.setStatus("current")


class _CurrWorkingPort_Type(Integer32):
    """Custom type currWorkingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("noData", 0)
    )


_CurrWorkingPort_Type.__name__ = "Integer32"
_CurrWorkingPort_Object = MibTableColumn
currWorkingPort = _CurrWorkingPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153, 2, 1, 1, 2),
    _CurrWorkingPort_Type()
)
currWorkingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currWorkingPort.setStatus("current")


class _CurrStandbyPort_Type(Integer32):
    """Custom type currStandbyPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("noData", 0)
    )


_CurrStandbyPort_Type.__name__ = "Integer32"
_CurrStandbyPort_Object = MibTableColumn
currStandbyPort = _CurrStandbyPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153, 2, 1, 1, 3),
    _CurrStandbyPort_Type()
)
currStandbyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currStandbyPort.setStatus("current")


class _DelimiterDetectedOnStandbyPort_Type(Integer32):
    """Custom type delimiterDetectedOnStandbyPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noData", 0),
          ("true", 1),
          ("false", 2))
    )


_DelimiterDetectedOnStandbyPort_Type.__name__ = "Integer32"
_DelimiterDetectedOnStandbyPort_Object = MibTableColumn
delimiterDetectedOnStandbyPort = _DelimiterDetectedOnStandbyPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153, 2, 1, 1, 4),
    _DelimiterDetectedOnStandbyPort_Type()
)
delimiterDetectedOnStandbyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delimiterDetectedOnStandbyPort.setStatus("current")


class _LastSwitchOverReason_Type(Integer32):
    """Custom type lastSwitchOverReason based on Integer32"""
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
        *(("noData", 0),
          ("lossOfSignal", 1),
          ("manual", 2),
          ("chipConnectionFailure", 3),
          ("noOnuDetected", 4))
    )


_LastSwitchOverReason_Type.__name__ = "Integer32"
_LastSwitchOverReason_Object = MibTableColumn
lastSwitchOverReason = _LastSwitchOverReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153, 2, 1, 1, 5),
    _LastSwitchOverReason_Type()
)
lastSwitchOverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSwitchOverReason.setStatus("current")
_LastSwitchOverTimeStampYear_Type = Integer32
_LastSwitchOverTimeStampYear_Object = MibTableColumn
lastSwitchOverTimeStampYear = _LastSwitchOverTimeStampYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153, 2, 1, 1, 6),
    _LastSwitchOverTimeStampYear_Type()
)
lastSwitchOverTimeStampYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSwitchOverTimeStampYear.setStatus("current")
_LastSwitchOverTimeStampMonth_Type = Integer32
_LastSwitchOverTimeStampMonth_Object = MibTableColumn
lastSwitchOverTimeStampMonth = _LastSwitchOverTimeStampMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153, 2, 1, 1, 7),
    _LastSwitchOverTimeStampMonth_Type()
)
lastSwitchOverTimeStampMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSwitchOverTimeStampMonth.setStatus("current")
_LastSwitchOverTimeStampDay_Type = Integer32
_LastSwitchOverTimeStampDay_Object = MibTableColumn
lastSwitchOverTimeStampDay = _LastSwitchOverTimeStampDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153, 2, 1, 1, 8),
    _LastSwitchOverTimeStampDay_Type()
)
lastSwitchOverTimeStampDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSwitchOverTimeStampDay.setStatus("current")
_LastSwitchOverTimeStampHour_Type = Integer32
_LastSwitchOverTimeStampHour_Object = MibTableColumn
lastSwitchOverTimeStampHour = _LastSwitchOverTimeStampHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153, 2, 1, 1, 9),
    _LastSwitchOverTimeStampHour_Type()
)
lastSwitchOverTimeStampHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSwitchOverTimeStampHour.setStatus("current")
_LastSwitchOverTimeStampMinute_Type = Integer32
_LastSwitchOverTimeStampMinute_Object = MibTableColumn
lastSwitchOverTimeStampMinute = _LastSwitchOverTimeStampMinute_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153, 2, 1, 1, 10),
    _LastSwitchOverTimeStampMinute_Type()
)
lastSwitchOverTimeStampMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSwitchOverTimeStampMinute.setStatus("current")
_LastSwitchOverTimeStampSecond_Type = Integer32
_LastSwitchOverTimeStampSecond_Object = MibTableColumn
lastSwitchOverTimeStampSecond = _LastSwitchOverTimeStampSecond_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153, 2, 1, 1, 11),
    _LastSwitchOverTimeStampSecond_Type()
)
lastSwitchOverTimeStampSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSwitchOverTimeStampSecond.setStatus("current")
_SwitchOverTimes_Type = Integer32
_SwitchOverTimes_Object = MibTableColumn
switchOverTimes = _SwitchOverTimes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153, 2, 1, 1, 12),
    _SwitchOverTimes_Type()
)
switchOverTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchOverTimes.setStatus("current")
_TriggerSwitchOver_Type = Integer32
_TriggerSwitchOver_Object = MibTableColumn
triggerSwitchOver = _TriggerSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153, 2, 1, 1, 13),
    _TriggerSwitchOver_Type()
)
triggerSwitchOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    triggerSwitchOver.setStatus("current")
_ProtectSwitchPonRowstatus_Type = RowStatus
_ProtectSwitchPonRowstatus_Object = MibTableColumn
protectSwitchPonRowstatus = _ProtectSwitchPonRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 153, 2, 1, 1, 14),
    _ProtectSwitchPonRowstatus_Type()
)
protectSwitchPonRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectSwitchPonRowstatus.setStatus("current")
_RateThresholdSetup_ObjectIdentity = ObjectIdentity
rateThresholdSetup = _RateThresholdSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 157)
)
_RateThresholdPortTable_Object = MibTable
rateThresholdPortTable = _RateThresholdPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 157, 1)
)
if mibBuilder.loadTexts:
    rateThresholdPortTable.setStatus("current")
_RateThresholdPortEntry_Object = MibTableRow
rateThresholdPortEntry = _RateThresholdPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 157, 1, 1)
)
rateThresholdPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rateThresholdPortEntry.setStatus("current")
_RateThresholdPortIngress_Type = Integer32
_RateThresholdPortIngress_Object = MibTableColumn
rateThresholdPortIngress = _RateThresholdPortIngress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 157, 1, 1, 1),
    _RateThresholdPortIngress_Type()
)
rateThresholdPortIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateThresholdPortIngress.setStatus("current")
_RateThresholdPortEgress_Type = Integer32
_RateThresholdPortEgress_Object = MibTableColumn
rateThresholdPortEgress = _RateThresholdPortEgress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 157, 1, 1, 2),
    _RateThresholdPortEgress_Type()
)
rateThresholdPortEgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateThresholdPortEgress.setStatus("current")
_RateUsagePercentageIngress_Type = Integer32
_RateUsagePercentageIngress_Object = MibTableColumn
rateUsagePercentageIngress = _RateUsagePercentageIngress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 157, 1, 1, 3),
    _RateUsagePercentageIngress_Type()
)
rateUsagePercentageIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateUsagePercentageIngress.setStatus("current")
_RateUsagePercentageEgress_Type = Integer32
_RateUsagePercentageEgress_Object = MibTableColumn
rateUsagePercentageEgress = _RateUsagePercentageEgress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 157, 1, 1, 4),
    _RateUsagePercentageEgress_Type()
)
rateUsagePercentageEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateUsagePercentageEgress.setStatus("current")
_RateUsageKbpsIngress_Type = Integer32
_RateUsageKbpsIngress_Object = MibTableColumn
rateUsageKbpsIngress = _RateUsageKbpsIngress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 157, 1, 1, 5),
    _RateUsageKbpsIngress_Type()
)
rateUsageKbpsIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateUsageKbpsIngress.setStatus("current")
_RateUsageKbpsEgress_Type = Integer32
_RateUsageKbpsEgress_Object = MibTableColumn
rateUsageKbpsEgress = _RateUsageKbpsEgress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 157, 1, 1, 6),
    _RateUsageKbpsEgress_Type()
)
rateUsageKbpsEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateUsageKbpsEgress.setStatus("current")
_ErpsSetup_ObjectIdentity = ObjectIdentity
erpsSetup = _ErpsSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158)
)
_ErpsState_Type = EnabledStatus
_ErpsState_Object = MibScalar
erpsState = _ErpsState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 1),
    _ErpsState_Type()
)
erpsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsState.setStatus("current")
_ErpsRingTable_Object = MibTable
erpsRingTable = _ErpsRingTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2)
)
if mibBuilder.loadTexts:
    erpsRingTable.setStatus("current")
_ErpsRingEntry_Object = MibTableRow
erpsRingEntry = _ErpsRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1)
)
erpsRingEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "erpsRingIndex"),
)
if mibBuilder.loadTexts:
    erpsRingEntry.setStatus("current")
_ErpsPort0_Type = Integer32
_ErpsPort0_Object = MibTableColumn
erpsPort0 = _ErpsPort0_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 1),
    _ErpsPort0_Type()
)
erpsPort0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsPort0.setStatus("current")
_ErpsPort1_Type = Integer32
_ErpsPort1_Object = MibTableColumn
erpsPort1 = _ErpsPort1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 2),
    _ErpsPort1_Type()
)
erpsPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsPort1.setStatus("current")
_ErpsRingId_Type = Integer32
_ErpsRingId_Object = MibTableColumn
erpsRingId = _ErpsRingId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 3),
    _ErpsRingId_Type()
)
erpsRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsRingId.setStatus("current")
_ErpsCcmPort0GroupName_Type = DisplayString
_ErpsCcmPort0GroupName_Object = MibTableColumn
erpsCcmPort0GroupName = _ErpsCcmPort0GroupName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 4),
    _ErpsCcmPort0GroupName_Type()
)
erpsCcmPort0GroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsCcmPort0GroupName.setStatus("current")
_ErpsCcmPort0Level_Type = Integer32
_ErpsCcmPort0Level_Object = MibTableColumn
erpsCcmPort0Level = _ErpsCcmPort0Level_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 5),
    _ErpsCcmPort0Level_Type()
)
erpsCcmPort0Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsCcmPort0Level.setStatus("current")
_ErpsCcmPort0Vlan_Type = Integer32
_ErpsCcmPort0Vlan_Object = MibTableColumn
erpsCcmPort0Vlan = _ErpsCcmPort0Vlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 6),
    _ErpsCcmPort0Vlan_Type()
)
erpsCcmPort0Vlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsCcmPort0Vlan.setStatus("current")
_ErpsCcmPort0TxName_Type = Integer32
_ErpsCcmPort0TxName_Object = MibTableColumn
erpsCcmPort0TxName = _ErpsCcmPort0TxName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 7),
    _ErpsCcmPort0TxName_Type()
)
erpsCcmPort0TxName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsCcmPort0TxName.setStatus("current")


class _ErpsCcmPort0Period_Type(Integer32):
    """Custom type erpsCcmPort0Period based on Integer32"""
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
        *(("none", 0),
          ("erpsCcm3ms", 1),
          ("erpsCcm10ms", 2),
          ("erpsCcm100ms", 3),
          ("erpsCcm1s", 4),
          ("erpsCcm10s", 5),
          ("erpsCcm1min", 6),
          ("erpsCcm10min", 7))
    )


_ErpsCcmPort0Period_Type.__name__ = "Integer32"
_ErpsCcmPort0Period_Object = MibTableColumn
erpsCcmPort0Period = _ErpsCcmPort0Period_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 8),
    _ErpsCcmPort0Period_Type()
)
erpsCcmPort0Period.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsCcmPort0Period.setStatus("current")
_ErpsCcmPort0Priority_Type = Integer32
_ErpsCcmPort0Priority_Object = MibTableColumn
erpsCcmPort0Priority = _ErpsCcmPort0Priority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 9),
    _ErpsCcmPort0Priority_Type()
)
erpsCcmPort0Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsCcmPort0Priority.setStatus("current")
_ErpsCcmPort0IntPriority_Type = Integer32
_ErpsCcmPort0IntPriority_Object = MibTableColumn
erpsCcmPort0IntPriority = _ErpsCcmPort0IntPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 10),
    _ErpsCcmPort0IntPriority_Type()
)
erpsCcmPort0IntPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsCcmPort0IntPriority.setStatus("current")
_ErpsCcmPort0RxName_Type = Integer32
_ErpsCcmPort0RxName_Object = MibTableColumn
erpsCcmPort0RxName = _ErpsCcmPort0RxName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 11),
    _ErpsCcmPort0RxName_Type()
)
erpsCcmPort0RxName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsCcmPort0RxName.setStatus("current")
_ErpsCcmPort1GroupName_Type = DisplayString
_ErpsCcmPort1GroupName_Object = MibTableColumn
erpsCcmPort1GroupName = _ErpsCcmPort1GroupName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 12),
    _ErpsCcmPort1GroupName_Type()
)
erpsCcmPort1GroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsCcmPort1GroupName.setStatus("current")
_ErpsCcmPort1Level_Type = Integer32
_ErpsCcmPort1Level_Object = MibTableColumn
erpsCcmPort1Level = _ErpsCcmPort1Level_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 13),
    _ErpsCcmPort1Level_Type()
)
erpsCcmPort1Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsCcmPort1Level.setStatus("current")
_ErpsCcmPort1Vlan_Type = Integer32
_ErpsCcmPort1Vlan_Object = MibTableColumn
erpsCcmPort1Vlan = _ErpsCcmPort1Vlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 14),
    _ErpsCcmPort1Vlan_Type()
)
erpsCcmPort1Vlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsCcmPort1Vlan.setStatus("current")
_ErpsCcmPort1TxName_Type = Integer32
_ErpsCcmPort1TxName_Object = MibTableColumn
erpsCcmPort1TxName = _ErpsCcmPort1TxName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 15),
    _ErpsCcmPort1TxName_Type()
)
erpsCcmPort1TxName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsCcmPort1TxName.setStatus("current")


class _ErpsCcmPort1Period_Type(Integer32):
    """Custom type erpsCcmPort1Period based on Integer32"""
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
        *(("none", 0),
          ("erpsCcm3ms", 1),
          ("erpsCcm10ms", 2),
          ("erpsCcm100ms", 3),
          ("erpsCcm1s", 4),
          ("erpsCcm10s", 5),
          ("erpsCcm1min", 6),
          ("erpsCcm10min", 7))
    )


_ErpsCcmPort1Period_Type.__name__ = "Integer32"
_ErpsCcmPort1Period_Object = MibTableColumn
erpsCcmPort1Period = _ErpsCcmPort1Period_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 16),
    _ErpsCcmPort1Period_Type()
)
erpsCcmPort1Period.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsCcmPort1Period.setStatus("current")
_ErpsCcmPort1Priority_Type = Integer32
_ErpsCcmPort1Priority_Object = MibTableColumn
erpsCcmPort1Priority = _ErpsCcmPort1Priority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 17),
    _ErpsCcmPort1Priority_Type()
)
erpsCcmPort1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsCcmPort1Priority.setStatus("current")
_ErpsCcmPort1IntPriority_Type = Integer32
_ErpsCcmPort1IntPriority_Object = MibTableColumn
erpsCcmPort1IntPriority = _ErpsCcmPort1IntPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 18),
    _ErpsCcmPort1IntPriority_Type()
)
erpsCcmPort1IntPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsCcmPort1IntPriority.setStatus("current")
_ErpsCcmPort1RxName_Type = Integer32
_ErpsCcmPort1RxName_Object = MibTableColumn
erpsCcmPort1RxName = _ErpsCcmPort1RxName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 19),
    _ErpsCcmPort1RxName_Type()
)
erpsCcmPort1RxName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsCcmPort1RxName.setStatus("current")
_ErpsRapsPort0Vlan_Type = Integer32
_ErpsRapsPort0Vlan_Object = MibTableColumn
erpsRapsPort0Vlan = _ErpsRapsPort0Vlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 20),
    _ErpsRapsPort0Vlan_Type()
)
erpsRapsPort0Vlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsRapsPort0Vlan.setStatus("current")
_ErpsRapsPort0priority_Type = Integer32
_ErpsRapsPort0priority_Object = MibTableColumn
erpsRapsPort0priority = _ErpsRapsPort0priority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 21),
    _ErpsRapsPort0priority_Type()
)
erpsRapsPort0priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsRapsPort0priority.setStatus("current")
_ErpsRapsPort0Level_Type = Integer32
_ErpsRapsPort0Level_Object = MibTableColumn
erpsRapsPort0Level = _ErpsRapsPort0Level_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 22),
    _ErpsRapsPort0Level_Type()
)
erpsRapsPort0Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsRapsPort0Level.setStatus("current")
_ErpsRapsPort1Vlan_Type = Integer32
_ErpsRapsPort1Vlan_Object = MibTableColumn
erpsRapsPort1Vlan = _ErpsRapsPort1Vlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 23),
    _ErpsRapsPort1Vlan_Type()
)
erpsRapsPort1Vlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsRapsPort1Vlan.setStatus("current")
_ErpsRapsPort1priority_Type = Integer32
_ErpsRapsPort1priority_Object = MibTableColumn
erpsRapsPort1priority = _ErpsRapsPort1priority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 24),
    _ErpsRapsPort1priority_Type()
)
erpsRapsPort1priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsRapsPort1priority.setStatus("current")
_ErpsRapsPort1Level_Type = Integer32
_ErpsRapsPort1Level_Object = MibTableColumn
erpsRapsPort1Level = _ErpsRapsPort1Level_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 25),
    _ErpsRapsPort1Level_Type()
)
erpsRapsPort1Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsRapsPort1Level.setStatus("current")
_ErpsRevertiveMode_Type = EnabledStatus
_ErpsRevertiveMode_Object = MibTableColumn
erpsRevertiveMode = _ErpsRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 26),
    _ErpsRevertiveMode_Type()
)
erpsRevertiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsRevertiveMode.setStatus("current")
_ErpsWtr_Type = Integer32
_ErpsWtr_Object = MibTableColumn
erpsWtr = _ErpsWtr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 27),
    _ErpsWtr_Type()
)
erpsWtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsWtr.setStatus("current")


class _ErpsRplOwner_Type(Integer32):
    """Custom type erpsRplOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("port0", 1),
          ("port1", 2))
    )


_ErpsRplOwner_Type.__name__ = "Integer32"
_ErpsRplOwner_Object = MibTableColumn
erpsRplOwner = _ErpsRplOwner_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 28),
    _ErpsRplOwner_Type()
)
erpsRplOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsRplOwner.setStatus("current")


class _ErpsRplNeighbour_Type(Integer32):
    """Custom type erpsRplNeighbour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("port0", 1),
          ("port1", 2))
    )


_ErpsRplNeighbour_Type.__name__ = "Integer32"
_ErpsRplNeighbour_Object = MibTableColumn
erpsRplNeighbour = _ErpsRplNeighbour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 29),
    _ErpsRplNeighbour_Type()
)
erpsRplNeighbour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsRplNeighbour.setStatus("current")


class _ErpsTunnelPort_Type(Integer32):
    """Custom type erpsTunnelPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("port0", 1),
          ("port1", 2))
    )


_ErpsTunnelPort_Type.__name__ = "Integer32"
_ErpsTunnelPort_Object = MibTableColumn
erpsTunnelPort = _ErpsTunnelPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 30),
    _ErpsTunnelPort_Type()
)
erpsTunnelPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsTunnelPort.setStatus("current")
_ErpsRingRowStatus_Type = RowStatus
_ErpsRingRowStatus_Object = MibTableColumn
erpsRingRowStatus = _ErpsRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 31),
    _ErpsRingRowStatus_Type()
)
erpsRingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsRingRowStatus.setStatus("current")
_ErpsRingIndex_Type = Integer32
_ErpsRingIndex_Object = MibTableColumn
erpsRingIndex = _ErpsRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 158, 2, 1, 32),
    _ErpsRingIndex_Type()
)
erpsRingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingIndex.setStatus("current")
_Wred_ObjectIdentity = ObjectIdentity
wred = _Wred_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 159)
)
_WredState_Type = EnabledStatus
_WredState_Object = MibScalar
wredState = _WredState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 159, 1),
    _WredState_Type()
)
wredState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wredState.setStatus("current")
_DhcpClientTest_ObjectIdentity = ObjectIdentity
dhcpClientTest = _DhcpClientTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 160)
)
_DhcpClientTestTimeout_Type = Integer32
_DhcpClientTestTimeout_Object = MibScalar
dhcpClientTestTimeout = _DhcpClientTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 160, 1),
    _DhcpClientTestTimeout_Type()
)
dhcpClientTestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientTestTimeout.setStatus("current")
_DhcpClientTestPortTable_Object = MibTable
dhcpClientTestPortTable = _DhcpClientTestPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 160, 2)
)
if mibBuilder.loadTexts:
    dhcpClientTestPortTable.setStatus("current")
_DhcpClientTestPortEntry_Object = MibTableRow
dhcpClientTestPortEntry = _DhcpClientTestPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 160, 2, 1)
)
dhcpClientTestPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dhcpClientTestPortEntry.setStatus("current")


class _DhcpClientTestPortState_Type(Integer32):
    """Custom type dhcpClientTestPortState based on Integer32"""
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
        *(("test_process_does_not_start_yet", 0),
          ("test_process_is_stopped_by_command", 1),
          ("test_process_is_ongoing", 2),
          ("receive_dhcp_offer_fail", 3),
          ("receive_dhcp_ack_fail", 4),
          ("test_process_successful", 5))
    )


_DhcpClientTestPortState_Type.__name__ = "Integer32"
_DhcpClientTestPortState_Object = MibTableColumn
dhcpClientTestPortState = _DhcpClientTestPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 160, 2, 1, 1),
    _DhcpClientTestPortState_Type()
)
dhcpClientTestPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientTestPortState.setStatus("current")
_DhcpClientTestPortIp_Type = IpAddress
_DhcpClientTestPortIp_Object = MibTableColumn
dhcpClientTestPortIp = _DhcpClientTestPortIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 160, 2, 1, 2),
    _DhcpClientTestPortIp_Type()
)
dhcpClientTestPortIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientTestPortIp.setStatus("current")


class _DhcpClientTestPortOptNniSvid_Type(Integer32):
    """Custom type dhcpClientTestPortOptNniSvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_DhcpClientTestPortOptNniSvid_Type.__name__ = "Integer32"
_DhcpClientTestPortOptNniSvid_Object = MibTableColumn
dhcpClientTestPortOptNniSvid = _DhcpClientTestPortOptNniSvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 160, 2, 1, 3),
    _DhcpClientTestPortOptNniSvid_Type()
)
dhcpClientTestPortOptNniSvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientTestPortOptNniSvid.setStatus("current")


class _DhcpClientTestPortOptSnicvid_Type(Integer32):
    """Custom type dhcpClientTestPortOptSnicvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_DhcpClientTestPortOptSnicvid_Type.__name__ = "Integer32"
_DhcpClientTestPortOptSnicvid_Object = MibTableColumn
dhcpClientTestPortOptSnicvid = _DhcpClientTestPortOptSnicvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 160, 2, 1, 4),
    _DhcpClientTestPortOptSnicvid_Type()
)
dhcpClientTestPortOptSnicvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientTestPortOptSnicvid.setStatus("current")


class _DhcpClientTestPortOptOntid_Type(Integer32):
    """Custom type dhcpClientTestPortOptOntid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DhcpClientTestPortOptOntid_Type.__name__ = "Integer32"
_DhcpClientTestPortOptOntid_Object = MibTableColumn
dhcpClientTestPortOptOntid = _DhcpClientTestPortOptOntid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 160, 2, 1, 5),
    _DhcpClientTestPortOptOntid_Type()
)
dhcpClientTestPortOptOntid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientTestPortOptOntid.setStatus("current")


class _DhcpClientTestPortOptOntcardid_Type(Integer32):
    """Custom type dhcpClientTestPortOptOntcardid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DhcpClientTestPortOptOntcardid_Type.__name__ = "Integer32"
_DhcpClientTestPortOptOntcardid_Object = MibTableColumn
dhcpClientTestPortOptOntcardid = _DhcpClientTestPortOptOntcardid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 160, 2, 1, 6),
    _DhcpClientTestPortOptOntcardid_Type()
)
dhcpClientTestPortOptOntcardid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientTestPortOptOntcardid.setStatus("current")


class _DhcpClientTestPortOptUniport_Type(Integer32):
    """Custom type dhcpClientTestPortOptUniport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DhcpClientTestPortOptUniport_Type.__name__ = "Integer32"
_DhcpClientTestPortOptUniport_Object = MibTableColumn
dhcpClientTestPortOptUniport = _DhcpClientTestPortOptUniport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 160, 2, 1, 7),
    _DhcpClientTestPortOptUniport_Type()
)
dhcpClientTestPortOptUniport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientTestPortOptUniport.setStatus("current")
_DhcpClientTestPortOptOntsn_Type = DisplayString
_DhcpClientTestPortOptOntsn_Object = MibTableColumn
dhcpClientTestPortOptOntsn = _DhcpClientTestPortOptOntsn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 160, 2, 1, 8),
    _DhcpClientTestPortOptOntsn_Type()
)
dhcpClientTestPortOptOntsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientTestPortOptOntsn.setStatus("current")


class _DhcpClientTestPortStartSniSvid_Type(Integer32):
    """Custom type dhcpClientTestPortStartSniSvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpClientTestPortStartSniSvid_Type.__name__ = "Integer32"
_DhcpClientTestPortStartSniSvid_Object = MibTableColumn
dhcpClientTestPortStartSniSvid = _DhcpClientTestPortStartSniSvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 160, 2, 1, 9),
    _DhcpClientTestPortStartSniSvid_Type()
)
dhcpClientTestPortStartSniSvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientTestPortStartSniSvid.setStatus("current")


class _DhcpClientTestPortStopSniSvid_Type(Integer32):
    """Custom type dhcpClientTestPortStopSniSvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpClientTestPortStopSniSvid_Type.__name__ = "Integer32"
_DhcpClientTestPortStopSniSvid_Object = MibTableColumn
dhcpClientTestPortStopSniSvid = _DhcpClientTestPortStopSniSvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 160, 2, 1, 10),
    _DhcpClientTestPortStopSniSvid_Type()
)
dhcpClientTestPortStopSniSvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientTestPortStopSniSvid.setStatus("current")
_SysTimeRef_ObjectIdentity = ObjectIdentity
sysTimeRef = _SysTimeRef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 161)
)
_SysTimeRefPTPState_Type = EnabledStatus
_SysTimeRefPTPState_Object = MibScalar
sysTimeRefPTPState = _SysTimeRefPTPState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 161, 1),
    _SysTimeRefPTPState_Type()
)
sysTimeRefPTPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeRefPTPState.setStatus("current")
_DhcpL2Agent_ObjectIdentity = ObjectIdentity
dhcpL2Agent = _DhcpL2Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 162)
)
_DhcpL2AgentTable_Object = MibTable
dhcpL2AgentTable = _DhcpL2AgentTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 162, 1)
)
if mibBuilder.loadTexts:
    dhcpL2AgentTable.setStatus("current")
_DhcpL2AgentEntry_Object = MibTableRow
dhcpL2AgentEntry = _DhcpL2AgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 162, 1, 1)
)
dhcpL2AgentEntry.setIndexNames(
    (0, "ZYXEL-olt1408-MIB", "dhcpL2AgentVid"),
)
if mibBuilder.loadTexts:
    dhcpL2AgentEntry.setStatus("current")


class _DhcpL2AgentVid_Type(Integer32):
    """Custom type dhcpL2AgentVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpL2AgentVid_Type.__name__ = "Integer32"
_DhcpL2AgentVid_Object = MibTableColumn
dhcpL2AgentVid = _DhcpL2AgentVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 162, 1, 1, 1),
    _DhcpL2AgentVid_Type()
)
dhcpL2AgentVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpL2AgentVid.setStatus("current")


class _DhcpL2AgentEnable_Type(Integer32):
    """Custom type dhcpL2AgentEnable based on Integer32"""
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


_DhcpL2AgentEnable_Type.__name__ = "Integer32"
_DhcpL2AgentEnable_Object = MibTableColumn
dhcpL2AgentEnable = _DhcpL2AgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 162, 1, 1, 2),
    _DhcpL2AgentEnable_Type()
)
dhcpL2AgentEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpL2AgentEnable.setStatus("current")
_DhcpL2AgentOpt82CircuitIdInfo_Type = DisplayString
_DhcpL2AgentOpt82CircuitIdInfo_Object = MibTableColumn
dhcpL2AgentOpt82CircuitIdInfo = _DhcpL2AgentOpt82CircuitIdInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 162, 1, 1, 3),
    _DhcpL2AgentOpt82CircuitIdInfo_Type()
)
dhcpL2AgentOpt82CircuitIdInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpL2AgentOpt82CircuitIdInfo.setStatus("current")
_DhcpL2AgentOpt82RemoteIdInfo_Type = DisplayString
_DhcpL2AgentOpt82RemoteIdInfo_Object = MibTableColumn
dhcpL2AgentOpt82RemoteIdInfo = _DhcpL2AgentOpt82RemoteIdInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 162, 1, 1, 4),
    _DhcpL2AgentOpt82RemoteIdInfo_Type()
)
dhcpL2AgentOpt82RemoteIdInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpL2AgentOpt82RemoteIdInfo.setStatus("current")
_DhcpL2AgentRowStatus_Type = RowStatus
_DhcpL2AgentRowStatus_Object = MibTableColumn
dhcpL2AgentRowStatus = _DhcpL2AgentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 162, 1, 1, 5),
    _DhcpL2AgentRowStatus_Type()
)
dhcpL2AgentRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpL2AgentRowStatus.setStatus("current")
_DhcpL2AgentOpt18InterfaceIdInfo_Type = DisplayString
_DhcpL2AgentOpt18InterfaceIdInfo_Object = MibTableColumn
dhcpL2AgentOpt18InterfaceIdInfo = _DhcpL2AgentOpt18InterfaceIdInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 162, 1, 1, 6),
    _DhcpL2AgentOpt18InterfaceIdInfo_Type()
)
dhcpL2AgentOpt18InterfaceIdInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpL2AgentOpt18InterfaceIdInfo.setStatus("current")
_DhcpL2AgentOpt37RemoteIdInfo_Type = DisplayString
_DhcpL2AgentOpt37RemoteIdInfo_Object = MibTableColumn
dhcpL2AgentOpt37RemoteIdInfo = _DhcpL2AgentOpt37RemoteIdInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 162, 1, 1, 7),
    _DhcpL2AgentOpt37RemoteIdInfo_Type()
)
dhcpL2AgentOpt37RemoteIdInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpL2AgentOpt37RemoteIdInfo.setStatus("current")


class _DhcpL2AgentLDRAEnable_Type(Integer32):
    """Custom type dhcpL2AgentLDRAEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DhcpL2AgentLDRAEnable_Type.__name__ = "Integer32"
_DhcpL2AgentLDRAEnable_Object = MibTableColumn
dhcpL2AgentLDRAEnable = _DhcpL2AgentLDRAEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 162, 1, 1, 8),
    _DhcpL2AgentLDRAEnable_Type()
)
dhcpL2AgentLDRAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpL2AgentLDRAEnable.setStatus("current")

# Managed Objects groups


# Notification objects

eventOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 31, 2, 1)
)
eventOnTrap.setObjects(
      *(("ZYXEL-olt1408-MIB", "eventSeqNum"),
        ("ZYXEL-olt1408-MIB", "eventEventId"),
        ("ZYXEL-olt1408-MIB", "eventName"),
        ("ZYXEL-olt1408-MIB", "eventSetTime"),
        ("ZYXEL-olt1408-MIB", "eventSeverity"),
        ("ZYXEL-olt1408-MIB", "eventInstanceType"),
        ("ZYXEL-olt1408-MIB", "eventInstanceId"),
        ("ZYXEL-olt1408-MIB", "eventInstanceName"),
        ("ZYXEL-olt1408-MIB", "eventServAffective"),
        ("ZYXEL-olt1408-MIB", "eventDescription"),
        ("ZYXEL-olt1408-MIB", "trapPersistence"),
        ("ZYXEL-olt1408-MIB", "trapSenderNodeId"),
        ("SNMPv2-MIB", "sysObjectID"))
)
if mibBuilder.loadTexts:
    eventOnTrap.setStatus(
        "current"
    )

eventClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 31, 2, 2)
)
eventClearedTrap.setObjects(
      *(("ZYXEL-olt1408-MIB", "eventSeqNum"),
        ("ZYXEL-olt1408-MIB", "eventEventId"),
        ("ZYXEL-olt1408-MIB", "eventSetTime"),
        ("ZYXEL-olt1408-MIB", "eventInstanceType"),
        ("ZYXEL-olt1408-MIB", "eventInstanceId"),
        ("ZYXEL-olt1408-MIB", "trapRefSeqNum"),
        ("ZYXEL-olt1408-MIB", "trapSenderNodeId"),
        ("SNMPv2-MIB", "sysObjectID"))
)
if mibBuilder.loadTexts:
    eventClearedTrap.setStatus(
        "current"
    )

newRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 70, 1)
)
newRoot.setObjects(
    ("ZYXEL-olt1408-MIB", "mstpXstId")
)
if mibBuilder.loadTexts:
    newRoot.setStatus(
        "current"
    )

topologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 107, 70, 2)
)
topologyChange.setObjects(
    ("ZYXEL-olt1408-MIB", "mstpXstId")
)
if mibBuilder.loadTexts:
    topologyChange.setStatus(
        "current"
    )

errdisableDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 4, 1)
)
errdisableDetectTrap.setObjects(
      *(("ZYXEL-olt1408-MIB", "errdisableTrapPort"),
        ("ZYXEL-olt1408-MIB", "errdisableTrapReason"),
        ("ZYXEL-olt1408-MIB", "errdisableTrapMode"))
)
if mibBuilder.loadTexts:
    errdisableDetectTrap.setStatus(
        "current"
    )

errdisableRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 6, 130, 4, 2)
)
errdisableRecoveryTrap.setObjects(
      *(("ZYXEL-olt1408-MIB", "errdisableTrapPort"),
        ("ZYXEL-olt1408-MIB", "errdisableTrapReason"),
        ("ZYXEL-olt1408-MIB", "errdisableTrapMode"))
)
if mibBuilder.loadTexts:
    errdisableRecoveryTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-olt1408-MIB",
    **{"UtcTimeStamp": UtcTimeStamp,
       "EventIdNumber": EventIdNumber,
       "EventSeverity": EventSeverity,
       "EventServiceAffective": EventServiceAffective,
       "InstanceType": InstanceType,
       "EventPersistence": EventPersistence,
       "MstiOrCistInstanceIndex": MstiOrCistInstanceIndex,
       "RemoteOnuStatus": RemoteOnuStatus,
       "zyxel": zyxel,
       "products": products,
       "accessSwitch": accessSwitch,
       "gponSeries": gponSeries,
       "olt1408": olt1408,
       "sysInfo": sysInfo,
       "sysSwPlatformMajorVers": sysSwPlatformMajorVers,
       "sysSwPlatformMinorVers": sysSwPlatformMinorVers,
       "sysSwModelString": sysSwModelString,
       "sysSwDay": sysSwDay,
       "sysSwMonth": sysSwMonth,
       "sysSwYear": sysSwYear,
       "sysSerialNumber": sysSerialNumber,
       "sysSwBootUpImage": sysSwBootUpImage,
       "sysImage1FwVersion": sysImage1FwVersion,
       "sysImage2FwVersion": sysImage2FwVersion,
       "sysCurrentFwVersion": sysCurrentFwVersion,
       "pwrInfo": pwrInfo,
       "pwrInfoSource": pwrInfoSource,
       "pwrInfoSysPowerConsumption": pwrInfoSysPowerConsumption,
       "pwrInfoBatChargingPower": pwrInfoBatChargingPower,
       "pwrInfoBatExistence": pwrInfoBatExistence,
       "pwrInfoBatTemperature": pwrInfoBatTemperature,
       "pwrInfoBatRemainingPower": pwrInfoBatRemainingPower,
       "pwrInfoBatVoltage": pwrInfoBatVoltage,
       "pwrInfoBatCapacityValidation": pwrInfoBatCapacityValidation,
       "pwrInfoChargerStatus": pwrInfoChargerStatus,
       "pwrInfoChargingCurrent": pwrInfoChargingCurrent,
       "pwrInfoChargingVoltage": pwrInfoChargingVoltage,
       "pwrInfoChargingTime": pwrInfoChargingTime,
       "pwrInfoTrickleChargerStatus": pwrInfoTrickleChargerStatus,
       "batterySetting": batterySetting,
       "batteryCapacity": batteryCapacity,
       "batteryTempThresholdHigh": batteryTempThresholdHigh,
       "batteryTempThresholdLow": batteryTempThresholdLow,
       "rateLimitSetup": rateLimitSetup,
       "rateLimitState": rateLimitState,
       "rateLimitPortTable": rateLimitPortTable,
       "rateLimitPortEntry": rateLimitPortEntry,
       "rateLimitPortState": rateLimitPortState,
       "rateLimitPortCommitRate": rateLimitPortCommitRate,
       "rateLimitPortPeakRate": rateLimitPortPeakRate,
       "rateLimitPortEgrRate": rateLimitPortEgrRate,
       "rateLimitPortPeakState": rateLimitPortPeakState,
       "rateLimitPortEgrState": rateLimitPortEgrState,
       "rateLimitPortCommitState": rateLimitPortCommitState,
       "brLimitSetup": brLimitSetup,
       "brLimitState": brLimitState,
       "brLimitPortTable": brLimitPortTable,
       "brLimitPortEntry": brLimitPortEntry,
       "brLimitPortBrState": brLimitPortBrState,
       "brLimitPortBrRate": brLimitPortBrRate,
       "brLimitPortMcState": brLimitPortMcState,
       "brLimitPortMcRate": brLimitPortMcRate,
       "brLimitPortDlfState": brLimitPortDlfState,
       "brLimitPortDlfRate": brLimitPortDlfRate,
       "portSecuritySetup": portSecuritySetup,
       "portSecurityState": portSecurityState,
       "portSecurityPortTable": portSecurityPortTable,
       "portSecurityPortEntry": portSecurityPortEntry,
       "portSecurityPortState": portSecurityPortState,
       "portSecurityPortLearnState": portSecurityPortLearnState,
       "portSecurityPortCount": portSecurityPortCount,
       "portSecurityMacFreeze": portSecurityMacFreeze,
       "vlanTrunkSetup": vlanTrunkSetup,
       "vlanTrunkPortTable": vlanTrunkPortTable,
       "vlanTrunkPortEntry": vlanTrunkPortEntry,
       "vlanTrunkPortState": vlanTrunkPortState,
       "ctlProtTransSetup": ctlProtTransSetup,
       "ctlProtTransState": ctlProtTransState,
       "ctlProtTransTunnelPortTable": ctlProtTransTunnelPortTable,
       "ctlProtTransTunnelPortEntry": ctlProtTransTunnelPortEntry,
       "ctlProtTransTunnelMode": ctlProtTransTunnelMode,
       "vlanStackSetup": vlanStackSetup,
       "vlanStackPortTable": vlanStackPortTable,
       "vlanStackPortEntry": vlanStackPortEntry,
       "vlanStackPortMode": vlanStackPortMode,
       "vlanStackPortVid": vlanStackPortVid,
       "vlanStackPortPrio": vlanStackPortPrio,
       "vlanStackTunnelPortTpid": vlanStackTunnelPortTpid,
       "dot1xSetup": dot1xSetup,
       "portAuthState": portAuthState,
       "hwMonitorInfo": hwMonitorInfo,
       "fanRpmTable": fanRpmTable,
       "fanRpmEntry": fanRpmEntry,
       "fanRpmIndex": fanRpmIndex,
       "fanRpmName": fanRpmName,
       "fanRpmCurValue": fanRpmCurValue,
       "fanRpmMaxValue": fanRpmMaxValue,
       "fanRpmMinValue": fanRpmMinValue,
       "fanRpmLowThresh": fanRpmLowThresh,
       "fanRpmDescr": fanRpmDescr,
       "tempTable": tempTable,
       "tempEntry": tempEntry,
       "tempIndex": tempIndex,
       "tempName": tempName,
       "tempCurValue": tempCurValue,
       "tempMaxValue": tempMaxValue,
       "tempMinValue": tempMinValue,
       "tempHighThresh": tempHighThresh,
       "tempDescr": tempDescr,
       "voltageTable": voltageTable,
       "voltageEntry": voltageEntry,
       "voltageIndex": voltageIndex,
       "voltageName": voltageName,
       "voltageCurValue": voltageCurValue,
       "voltageMaxValue": voltageMaxValue,
       "voltageMinValue": voltageMinValue,
       "voltageNominalValue": voltageNominalValue,
       "voltageLowThresh": voltageLowThresh,
       "voltageDescr": voltageDescr,
       "snmpSetup": snmpSetup,
       "snmpGetCommunity": snmpGetCommunity,
       "snmpSetCommunity": snmpSetCommunity,
       "snmpTrapCommunity": snmpTrapCommunity,
       "snmpTrapDestTable": snmpTrapDestTable,
       "snmpTrapDestEntry": snmpTrapDestEntry,
       "snmpTrapDestIP": snmpTrapDestIP,
       "snmpTrapDestRowStatus": snmpTrapDestRowStatus,
       "snmpTrapDestPort": snmpTrapDestPort,
       "snmpTrapVersion": snmpTrapVersion,
       "snmpTrapUserName": snmpTrapUserName,
       "snmpVersion": snmpVersion,
       "snmpUserTable": snmpUserTable,
       "snmpUserEntry": snmpUserEntry,
       "snmpUserName": snmpUserName,
       "snmpUserSecurityLevel": snmpUserSecurityLevel,
       "snmpUserAuthProtocol": snmpUserAuthProtocol,
       "snmpUserPrivProtocol": snmpUserPrivProtocol,
       "snmpUserGroup": snmpUserGroup,
       "snmpTrapGroupTable": snmpTrapGroupTable,
       "snmpTrapGroupEntry": snmpTrapGroupEntry,
       "snmpTrapSystemGroup": snmpTrapSystemGroup,
       "snmpTrapInterfaceGroup": snmpTrapInterfaceGroup,
       "snmpTrapAAAGroup": snmpTrapAAAGroup,
       "snmpTrapIPGroup": snmpTrapIPGroup,
       "snmpTrapSwitchGroup": snmpTrapSwitchGroup,
       "dateTimeSetup": dateTimeSetup,
       "dateTimeServerType": dateTimeServerType,
       "dateTimeServerIP": dateTimeServerIP,
       "dateTimeZone": dateTimeZone,
       "dateTimeNewDateYear": dateTimeNewDateYear,
       "dateTimeNewDateMonth": dateTimeNewDateMonth,
       "dateTimeNewDateDay": dateTimeNewDateDay,
       "dateTimeNewTimeHour": dateTimeNewTimeHour,
       "dateTimeNewTimeMinute": dateTimeNewTimeMinute,
       "dateTimeNewTimeSecond": dateTimeNewTimeSecond,
       "dateTimeDaylightSavingTimeSetup": dateTimeDaylightSavingTimeSetup,
       "daylightSavingTimeState": daylightSavingTimeState,
       "daylightSavingTimeStartDateWeek": daylightSavingTimeStartDateWeek,
       "daylightSavingTimeStartDateDay": daylightSavingTimeStartDateDay,
       "daylightSavingTimeStartDateMonth": daylightSavingTimeStartDateMonth,
       "daylightSavingTimeStartDateHour": daylightSavingTimeStartDateHour,
       "daylightSavingTimeEndDateWeek": daylightSavingTimeEndDateWeek,
       "daylightSavingTimeEndDateDay": daylightSavingTimeEndDateDay,
       "daylightSavingTimeEndDateMonth": daylightSavingTimeEndDateMonth,
       "daylightSavingTimeEndDateHour": daylightSavingTimeEndDateHour,
       "sysMgmt": sysMgmt,
       "sysMgmtConfigSave": sysMgmtConfigSave,
       "sysMgmtBootupConfig": sysMgmtBootupConfig,
       "sysMgmtReboot": sysMgmtReboot,
       "sysMgmtDefaultConfig": sysMgmtDefaultConfig,
       "sysMgmtLastActionStatus": sysMgmtLastActionStatus,
       "sysMgmtSystemStatus": sysMgmtSystemStatus,
       "sysMgmtCPUUsage": sysMgmtCPUUsage,
       "sysMgmtBootupImage": sysMgmtBootupImage,
       "sysMgmtCounterReset": sysMgmtCounterReset,
       "sysMgmtTftpServiceSetup": sysMgmtTftpServiceSetup,
       "sysMgmtTftpServerIp": sysMgmtTftpServerIp,
       "sysMgmtTftpRemoteFileName": sysMgmtTftpRemoteFileName,
       "sysMgmtTftpConfigIndex": sysMgmtTftpConfigIndex,
       "sysMgmtTftpAction": sysMgmtTftpAction,
       "sysMgmtTftpActionStatus": sysMgmtTftpActionStatus,
       "sysMgmtTftpActionPrivilege13": sysMgmtTftpActionPrivilege13,
       "sysLoginSetup": sysLoginSetup,
       "loginLimitMaxNumberOfUser": loginLimitMaxNumberOfUser,
       "sysLoginSetupTable": sysLoginSetupTable,
       "sysLoginSetupEntry": sysLoginSetupEntry,
       "sysLoginName": sysLoginName,
       "sysLoginPassword": sysLoginPassword,
       "sysLoginPrivilege": sysLoginPrivilege,
       "sysLoginRowStatus": sysLoginRowStatus,
       "sysMgmtCPUUsageThreshold": sysMgmtCPUUsageThreshold,
       "sysMgmtMemoryUsageThreshold": sysMgmtMemoryUsageThreshold,
       "sysMgmtUartLogoutTime": sysMgmtUartLogoutTime,
       "sysMgmtConfigSavePrivilege13": sysMgmtConfigSavePrivilege13,
       "sysMgmtDefaultConfigPrivilege13": sysMgmtDefaultConfigPrivilege13,
       "layer2Setup": layer2Setup,
       "vlanTypeSetup": vlanTypeSetup,
       "igmpSnoopingStateSetup": igmpSnoopingStateSetup,
       "tagVlanPortIsolationState": tagVlanPortIsolationState,
       "stpState": stpState,
       "unknownMulticastFrameForwarding": unknownMulticastFrameForwarding,
       "multicastGrpHostTimeout": multicastGrpHostTimeout,
       "multicastLeaveTimeout": multicastLeaveTimeout,
       "reservedMulticastFrameForwarding": reservedMulticastFrameForwarding,
       "igmpsnp8021pPriority": igmpsnp8021pPriority,
       "igmpsnpVlanMode": igmpsnpVlanMode,
       "stpMode": stpMode,
       "igmpsnpVlanTable": igmpsnpVlanTable,
       "igmpsnpVlanEntry": igmpsnpVlanEntry,
       "igmpsnpVid": igmpsnpVid,
       "igmpsnpVlanName": igmpsnpVlanName,
       "igmpsnpVlanRowStatus": igmpsnpVlanRowStatus,
       "ethernetCfmStateSetup": ethernetCfmStateSetup,
       "lldpStateSetup": lldpStateSetup,
       "smartIsolationState": smartIsolationState,
       "mgmdMLDsupport": mgmdMLDsupport,
       "mgmdv3mode": mgmdv3mode,
       "mgmdReportTag": mgmdReportTag,
       "mgmdIgmpProxyWorkingIP": mgmdIgmpProxyWorkingIP,
       "mgmdQueryTag": mgmdQueryTag,
       "dsMeterMacroMode": dsMeterMacroMode,
       "ipSetup": ipSetup,
       "dnsIpAddress": dnsIpAddress,
       "defaultMgmt": defaultMgmt,
       "defaultGateway": defaultGateway,
       "outOfBandIpSetup": outOfBandIpSetup,
       "outOfBandIp": outOfBandIp,
       "outOfBandSubnetMask": outOfBandSubnetMask,
       "outOfBandGateway": outOfBandGateway,
       "maxNumOfInbandIp": maxNumOfInbandIp,
       "inbandIpTable": inbandIpTable,
       "inbandIpEntry": inbandIpEntry,
       "inbandEntryIp": inbandEntryIp,
       "inbandEntrySubnetMask": inbandEntrySubnetMask,
       "inbandEntryVid": inbandEntryVid,
       "inbandEntryRowStatus": inbandEntryRowStatus,
       "filterSetup": filterSetup,
       "filterTable": filterTable,
       "filterEntry": filterEntry,
       "filterName": filterName,
       "filterActionState": filterActionState,
       "filterMacAddr": filterMacAddr,
       "filterVid": filterVid,
       "filterRowStatus": filterRowStatus,
       "mirrorSetup": mirrorSetup,
       "mirrorState": mirrorState,
       "mirrorMonitorPort": mirrorMonitorPort,
       "mirrorTable": mirrorTable,
       "mirrorEntry": mirrorEntry,
       "mirrorMirroredState": mirrorMirroredState,
       "mirrorDirection": mirrorDirection,
       "mirrorVlan": mirrorVlan,
       "aggrSetup": aggrSetup,
       "aggrState": aggrState,
       "aggrSystemPriority": aggrSystemPriority,
       "aggrGroupTable": aggrGroupTable,
       "aggrGroupEntry": aggrGroupEntry,
       "aggrGroupIndex": aggrGroupIndex,
       "aggrGroupState": aggrGroupState,
       "aggrGroupDynamicState": aggrGroupDynamicState,
       "aggrGroupCriteria": aggrGroupCriteria,
       "aggrPortTable": aggrPortTable,
       "aggrPortEntry": aggrPortEntry,
       "aggrPortGroup": aggrPortGroup,
       "aggrPortDynamicStateTimeout": aggrPortDynamicStateTimeout,
       "aggrStatusTable": aggrStatusTable,
       "aggrStatusEntry": aggrStatusEntry,
       "aggrStatusActorID": aggrStatusActorID,
       "aggrStatusPartnerID": aggrStatusPartnerID,
       "aggrStatusLinkPorts": aggrStatusLinkPorts,
       "aggrStatusSyncPorts": aggrStatusSyncPorts,
       "accessCtlSetup": accessCtlSetup,
       "accessCtlTable": accessCtlTable,
       "accessCtlEntry": accessCtlEntry,
       "accessCtlService": accessCtlService,
       "accessCtlEnable": accessCtlEnable,
       "accessCtlServicePort": accessCtlServicePort,
       "accessCtlTimeout": accessCtlTimeout,
       "securedClientTable": securedClientTable,
       "securedClientEntry": securedClientEntry,
       "securedClientIndex": securedClientIndex,
       "securedClientEnable": securedClientEnable,
       "securedClientStartIp": securedClientStartIp,
       "securedClientEndIp": securedClientEndIp,
       "securedClientService": securedClientService,
       "queuingMethodSetup": queuingMethodSetup,
       "portQueuingMethodTable": portQueuingMethodTable,
       "portQueuingMethodEntry": portQueuingMethodEntry,
       "portQueuingMethodQueue": portQueuingMethodQueue,
       "portQueuingMethodWeight": portQueuingMethodWeight,
       "portQueuingMethodMode": portQueuingMethodMode,
       "portQueuingMethodHybridSpqTable": portQueuingMethodHybridSpqTable,
       "portQueuingMethodHybridSpqEntry": portQueuingMethodHybridSpqEntry,
       "portQueuingMethodHybridSpq": portQueuingMethodHybridSpq,
       "dhcpSetup": dhcpSetup,
       "globalDhcpRelay": globalDhcpRelay,
       "globalDhcpRelayEnable": globalDhcpRelayEnable,
       "globalDhcpRelayOption82Enable": globalDhcpRelayOption82Enable,
       "globalDhcpRelayInfoEnable": globalDhcpRelayInfoEnable,
       "globalDhcpRelayInfoData": globalDhcpRelayInfoData,
       "maxNumberOfGlobalDhcpRelayRemoteServer": maxNumberOfGlobalDhcpRelayRemoteServer,
       "globalDhcpRelayRemoteServerTable": globalDhcpRelayRemoteServerTable,
       "globalDhcpRelayRemoteServerEntry": globalDhcpRelayRemoteServerEntry,
       "globalDhcpRelayRemoteServerIp": globalDhcpRelayRemoteServerIp,
       "globalDhcpRelayRemoteServerRowStatus": globalDhcpRelayRemoteServerRowStatus,
       "globalDhcpRelayOption82Format": globalDhcpRelayOption82Format,
       "dhcpServer": dhcpServer,
       "maxNumberOfDhcpServers": maxNumberOfDhcpServers,
       "dhcpServerTable": dhcpServerTable,
       "dhcpServerEntry": dhcpServerEntry,
       "dhcpServerVid": dhcpServerVid,
       "dhcpServerStartAddr": dhcpServerStartAddr,
       "dhcpServerPoolSize": dhcpServerPoolSize,
       "dhcpServerMask": dhcpServerMask,
       "dhcpServerGateway": dhcpServerGateway,
       "dhcpServerPrimaryDNS": dhcpServerPrimaryDNS,
       "dhcpServerSecondaryDNS": dhcpServerSecondaryDNS,
       "dhcpServerRowStatus": dhcpServerRowStatus,
       "dhcpRelay": dhcpRelay,
       "dhcpRelayInfoData": dhcpRelayInfoData,
       "maxNumberOfDhcpRelay": maxNumberOfDhcpRelay,
       "maxNumberOfDhcpRelayRemoteServer": maxNumberOfDhcpRelayRemoteServer,
       "dhcpRelayRemoteServerTable": dhcpRelayRemoteServerTable,
       "dhcpRelayRemoteServerEntry": dhcpRelayRemoteServerEntry,
       "dhcpRelayVid": dhcpRelayVid,
       "dhcpRelayRemoteServerIp": dhcpRelayRemoteServerIp,
       "dhcpRelayRemoteServerRowStatus": dhcpRelayRemoteServerRowStatus,
       "dhcpRelayTable": dhcpRelayTable,
       "dhcpRelayEntry": dhcpRelayEntry,
       "dhcpRelayOption82Enable": dhcpRelayOption82Enable,
       "dhcpRelayInfoEnable": dhcpRelayInfoEnable,
       "dhcpRelayOption82Format": dhcpRelayOption82Format,
       "arpInfo": arpInfo,
       "arpTable": arpTable,
       "arpEntry": arpEntry,
       "arpIndex": arpIndex,
       "arpIpAddr": arpIpAddr,
       "arpMacAddr": arpMacAddr,
       "arpMacVid": arpMacVid,
       "arpType": arpType,
       "arpPort": arpPort,
       "arpAge": arpAge,
       "portOpModeSetup": portOpModeSetup,
       "portOpModePortTable": portOpModePortTable,
       "portOpModePortEntry": portOpModePortEntry,
       "portOpModePortSpeedDuplex": portOpModePortSpeedDuplex,
       "portOpModePortFlowCntl": portOpModePortFlowCntl,
       "portOpModePortName": portOpModePortName,
       "portOpModePortModuleType": portOpModePortModuleType,
       "portOpModePortLinkUpType": portOpModePortLinkUpType,
       "portOpModePortCounterReset": portOpModePortCounterReset,
       "portOpModePortMaxFrameSize": portOpModePortMaxFrameSize,
       "multicastPortSetup": multicastPortSetup,
       "multicastPortTable": multicastPortTable,
       "multicastPortEntry": multicastPortEntry,
       "multicastPortImmediateLeave": multicastPortImmediateLeave,
       "multicastPortQueryMode": multicastPortQueryMode,
       "multicastStatus": multicastStatus,
       "multicastStatusTable": multicastStatusTable,
       "multicastStatusEntry": multicastStatusEntry,
       "multicastStatusIndex": multicastStatusIndex,
       "multicastStatusVlanID": multicastStatusVlanID,
       "multicastStatusPort": multicastStatusPort,
       "multicastStatusGroup": multicastStatusGroup,
       "igmpCountTable": igmpCountTable,
       "igmpCountEntry": igmpCountEntry,
       "igmpCountIndex": igmpCountIndex,
       "igmpCountInQuery": igmpCountInQuery,
       "igmpCountInReport": igmpCountInReport,
       "igmpCountInLeave": igmpCountInLeave,
       "igmpCountInQueryDrop": igmpCountInQueryDrop,
       "igmpCountInReportDrop": igmpCountInReportDrop,
       "igmpCountInLeaveDrop": igmpCountInLeaveDrop,
       "igmpCountOutQuery": igmpCountOutQuery,
       "igmpCountOutReport": igmpCountOutReport,
       "igmpCountOutLeave": igmpCountOutLeave,
       "multicastVlanStatusTable": multicastVlanStatusTable,
       "multicastVlanStatusEntry": multicastVlanStatusEntry,
       "multicastVlanStatusVlanID": multicastVlanStatusVlanID,
       "multicastVlanStatusType": multicastVlanStatusType,
       "multicastVlanQueryPort": multicastVlanQueryPort,
       "multicastVlanQuerySrcIp": multicastVlanQuerySrcIp,
       "igmpCounterPortTable": igmpCounterPortTable,
       "igmpCounterPortEntry": igmpCounterPortEntry,
       "igmpCounterPortJoin": igmpCounterPortJoin,
       "igmpCounterPortLeave": igmpCounterPortLeave,
       "igmpCounterPortActiveGroup": igmpCounterPortActiveGroup,
       "igmpCounterPortQuery": igmpCounterPortQuery,
       "igmpCounterVlanTable": igmpCounterVlanTable,
       "igmpCounterVlanEntry": igmpCounterVlanEntry,
       "igmpCounterVlanJoin": igmpCounterVlanJoin,
       "igmpCounterVlanLeave": igmpCounterVlanLeave,
       "igmpCounterVlanActiveGroup": igmpCounterVlanActiveGroup,
       "igmpCounterVlanQuery": igmpCounterVlanQuery,
       "multicastCurrentGroupStatusTable": multicastCurrentGroupStatusTable,
       "multicastCurrentGroupStatusEntry": multicastCurrentGroupStatusEntry,
       "multicastCurrentNumberOfActivePort": multicastCurrentNumberOfActivePort,
       "multicastClientSrcIpTable": multicastClientSrcIpTable,
       "multicastClientSrcIpEntry": multicastClientSrcIpEntry,
       "multicastClientSrcIpIndex": multicastClientSrcIpIndex,
       "multicastClientSrcIpAddress": multicastClientSrcIpAddress,
       "mgmdStatusTable": mgmdStatusTable,
       "mgmdStatusEntry": mgmdStatusEntry,
       "mgmdStatusIndex": mgmdStatusIndex,
       "mgmdStatusVlanID": mgmdStatusVlanID,
       "mgmdStatusPort": mgmdStatusPort,
       "mgmdStatusGroupAddressType": mgmdStatusGroupAddressType,
       "mgmdStatusGroupAddress": mgmdStatusGroupAddress,
       "mgmdStatusGroupFilterMode": mgmdStatusGroupFilterMode,
       "mgmdStatusGroupUpTime": mgmdStatusGroupUpTime,
       "mgmdCountTable": mgmdCountTable,
       "mgmdCountEntry": mgmdCountEntry,
       "mgmdCountIndex": mgmdCountIndex,
       "mgmdCountInQuery": mgmdCountInQuery,
       "mgmdCountInReport": mgmdCountInReport,
       "mgmdCountInLeave": mgmdCountInLeave,
       "mgmdCountInQueryDrop": mgmdCountInQueryDrop,
       "mgmdCountInReportDrop": mgmdCountInReportDrop,
       "mgmdCountInLeaveDrop": mgmdCountInLeaveDrop,
       "mgmdCountOutQuery": mgmdCountOutQuery,
       "mgmdCountOutReport": mgmdCountOutReport,
       "mgmdCountOutLeave": mgmdCountOutLeave,
       "mgmdVlanStatusTable": mgmdVlanStatusTable,
       "mgmdVlanStatusEntry": mgmdVlanStatusEntry,
       "mgmdVlanStatusVlanID": mgmdVlanStatusVlanID,
       "mgmdVlanStatusType": mgmdVlanStatusType,
       "mgmdVlanQueryPort": mgmdVlanQueryPort,
       "mgmdVlanQuerySrcIpType": mgmdVlanQuerySrcIpType,
       "mgmdVlanQuerySrcIp": mgmdVlanQuerySrcIp,
       "mgmdCounterPortTable": mgmdCounterPortTable,
       "mgmdCounterPortEntry": mgmdCounterPortEntry,
       "mgmdCounterPortV1ReportIn": mgmdCounterPortV1ReportIn,
       "mgmdCounterPortV2ReportIn": mgmdCounterPortV2ReportIn,
       "mgmdCounterPortV3ReportIn": mgmdCounterPortV3ReportIn,
       "mgmdCounterPortLeaveIn": mgmdCounterPortLeaveIn,
       "mgmdCounterPortTotalReportIn": mgmdCounterPortTotalReportIn,
       "mgmdCounterPortV1ReportOut": mgmdCounterPortV1ReportOut,
       "mgmdCounterPortV2ReportOut": mgmdCounterPortV2ReportOut,
       "mgmdCounterPortV3ReportOut": mgmdCounterPortV3ReportOut,
       "mgmdCounterPortLeaveOut": mgmdCounterPortLeaveOut,
       "mgmdCounterPortTotalReportOut": mgmdCounterPortTotalReportOut,
       "mgmdCounterPortV1QueryIn": mgmdCounterPortV1QueryIn,
       "mgmdCounterPortV2QueryIn": mgmdCounterPortV2QueryIn,
       "mgmdCounterPortV3QueryIn": mgmdCounterPortV3QueryIn,
       "mgmdCounterPortTotalQueryIn": mgmdCounterPortTotalQueryIn,
       "mgmdCounterPortV1QueryOut": mgmdCounterPortV1QueryOut,
       "mgmdCounterPortV2QueryOut": mgmdCounterPortV2QueryOut,
       "mgmdCounterPortV3QueryOut": mgmdCounterPortV3QueryOut,
       "mgmdCounterPortTotalQueryOut": mgmdCounterPortTotalQueryOut,
       "mgmdCounterPortRecordDropMaxGrpLimit": mgmdCounterPortRecordDropMaxGrpLimit,
       "mgmdCounterPortRecordDropGrpFilter": mgmdCounterPortRecordDropGrpFilter,
       "mgmdCounterPortRecordDropMVR": mgmdCounterPortRecordDropMVR,
       "mgmdCounterPortRecordDropOther": mgmdCounterPortRecordDropOther,
       "mgmdCounterPortDropRateLimit": mgmdCounterPortDropRateLimit,
       "mgmdCounterPortReportDropOther": mgmdCounterPortReportDropOther,
       "mgmdCounterPortQueryDropOther": mgmdCounterPortQueryDropOther,
       "mgmdCounterVlanTable": mgmdCounterVlanTable,
       "mgmdCounterVlanEntry": mgmdCounterVlanEntry,
       "mgmdCounterVlanV1ReportIn": mgmdCounterVlanV1ReportIn,
       "mgmdCounterVlanV2ReportIn": mgmdCounterVlanV2ReportIn,
       "mgmdCounterVlanV3ReportIn": mgmdCounterVlanV3ReportIn,
       "mgmdCounterVlanLeaveIn": mgmdCounterVlanLeaveIn,
       "mgmdCounterVlanTotalReportIn": mgmdCounterVlanTotalReportIn,
       "mgmdCounterVlanV1ReportOut": mgmdCounterVlanV1ReportOut,
       "mgmdCounterVlanV2ReportOut": mgmdCounterVlanV2ReportOut,
       "mgmdCounterVlanV3ReportOut": mgmdCounterVlanV3ReportOut,
       "mgmdCounterVlanLeaveOut": mgmdCounterVlanLeaveOut,
       "mgmdCounterVlanTotalReportOut": mgmdCounterVlanTotalReportOut,
       "mgmdCounterVlanV1QueryIn": mgmdCounterVlanV1QueryIn,
       "mgmdCounterVlanV2QueryIn": mgmdCounterVlanV2QueryIn,
       "mgmdCounterVlanV3QueryIn": mgmdCounterVlanV3QueryIn,
       "mgmdCounterVlanTotalQueryIn": mgmdCounterVlanTotalQueryIn,
       "mgmdCounterVlanV1QueryOut": mgmdCounterVlanV1QueryOut,
       "mgmdCounterVlanV2QueryOut": mgmdCounterVlanV2QueryOut,
       "mgmdCounterVlanV3QueryOut": mgmdCounterVlanV3QueryOut,
       "mgmdCounterVlanTotalQueryOut": mgmdCounterVlanTotalQueryOut,
       "mgmdCounterVlanRecordDropMaxGrpLimit": mgmdCounterVlanRecordDropMaxGrpLimit,
       "mgmdCounterVlanRecordDropGrpFilter": mgmdCounterVlanRecordDropGrpFilter,
       "mgmdCounterVlanRecordDropMVR": mgmdCounterVlanRecordDropMVR,
       "mgmdCounterVlanRecordDropOther": mgmdCounterVlanRecordDropOther,
       "mgmdCounterVlanDropRateLimit": mgmdCounterVlanDropRateLimit,
       "mgmdCounterVlanReportDropOther": mgmdCounterVlanReportDropOther,
       "mgmdCounterVlanQueryDropOther": mgmdCounterVlanQueryDropOther,
       "mgmdCurrentGroupStatusTable": mgmdCurrentGroupStatusTable,
       "mgmdCurrentGroupStatusEntry": mgmdCurrentGroupStatusEntry,
       "mgmdCurrentNumberOfActivePort": mgmdCurrentNumberOfActivePort,
       "mgmdClientSrcIpTable": mgmdClientSrcIpTable,
       "mgmdClientSrcIpEntry": mgmdClientSrcIpEntry,
       "mgmdClientSrcIpIndex": mgmdClientSrcIpIndex,
       "mgmdClientSrcIpAddressType": mgmdClientSrcIpAddressType,
       "mgmdClientSrcIpAddress": mgmdClientSrcIpAddress,
       "mgmdSrcListTable": mgmdSrcListTable,
       "mgmdSrcListEntry": mgmdSrcListEntry,
       "mgmdSrcListAddressType": mgmdSrcListAddressType,
       "mgmdSrcListAddress": mgmdSrcListAddress,
       "mgmdPortCounterResetTable": mgmdPortCounterResetTable,
       "mgmdPortCounterResetEntry": mgmdPortCounterResetEntry,
       "mgmdPortCounterReset": mgmdPortCounterReset,
       "mgmdAnyPortCounterReset": mgmdAnyPortCounterReset,
       "mgmdAnyVlanCounterReset": mgmdAnyVlanCounterReset,
       "igmpchannelCountTable": igmpchannelCountTable,
       "igmpchannelCountEntry": igmpchannelCountEntry,
       "igmpchannelCountInReportV1": igmpchannelCountInReportV1,
       "igmpchannelCountInReportV2": igmpchannelCountInReportV2,
       "igmpchannelCountInReportV3": igmpchannelCountInReportV3,
       "igmpchannelCountInReportLeave": igmpchannelCountInReportLeave,
       "igmpchannelCountDropRateLimit": igmpchannelCountDropRateLimit,
       "igmpchannelCountDropOthers": igmpchannelCountDropOthers,
       "igmpchannelStatusTable": igmpchannelStatusTable,
       "igmpchannelStatusEntry": igmpchannelStatusEntry,
       "igmpchannelStatusVlanID": igmpchannelStatusVlanID,
       "igmpchannelStatusPort": igmpchannelStatusPort,
       "igmpchannelStatusGroupAddressType": igmpchannelStatusGroupAddressType,
       "igmpchannelStatusGroupAddress": igmpchannelStatusGroupAddress,
       "igmpchannelStatusGem": igmpchannelStatusGem,
       "igmpchannelStatusPortAid": igmpchannelStatusPortAid,
       "igmpchannelStatusUniVid": igmpchannelStatusUniVid,
       "igmpchannelStatusGroupFilterMode": igmpchannelStatusGroupFilterMode,
       "igmpchannelStatusGroupUpTime": igmpchannelStatusGroupUpTime,
       "igmpchannelClientSrcIpTable": igmpchannelClientSrcIpTable,
       "igmpchannelClientSrcIpEntry": igmpchannelClientSrcIpEntry,
       "igmpchannelClientSrcIpIndex": igmpchannelClientSrcIpIndex,
       "igmpchannelClientSrcIpAddressType": igmpchannelClientSrcIpAddressType,
       "igmpchannelClientSrcIpAddress": igmpchannelClientSrcIpAddress,
       "mvrSetup": mvrSetup,
       "maxNumberOfMVR": maxNumberOfMVR,
       "mvrTable": mvrTable,
       "mvrEntry": mvrEntry,
       "mvrVlanID": mvrVlanID,
       "mvrName": mvrName,
       "mvrMode": mvrMode,
       "mvrRowStatus": mvrRowStatus,
       "mvr8021pPriority": mvr8021pPriority,
       "mvrPortTable": mvrPortTable,
       "mvrPortEntry": mvrPortEntry,
       "mvrPortRole": mvrPortRole,
       "mvrPortTagging": mvrPortTagging,
       "maxNumberOfMvrGroup": maxNumberOfMvrGroup,
       "mvrGroupTable": mvrGroupTable,
       "mvrGroupEntry": mvrGroupEntry,
       "mvrGroupName": mvrGroupName,
       "mvrGroupStartAddress": mvrGroupStartAddress,
       "mvrGroupEndAddress": mvrGroupEndAddress,
       "mvrGroupRowStatus": mvrGroupRowStatus,
       "mvrBehavior": mvrBehavior,
       "mvrMgmdGroupTable": mvrMgmdGroupTable,
       "mvrMgmdGroupEntry": mvrMgmdGroupEntry,
       "mvrMgmdGroupName": mvrMgmdGroupName,
       "mvrMgmdGroupAddressType": mvrMgmdGroupAddressType,
       "mvrMgmdGroupStartAddress": mvrMgmdGroupStartAddress,
       "mvrMgmdGroupEndAddress": mvrMgmdGroupEndAddress,
       "mvrMgmdGroupRowStatus": mvrMgmdGroupRowStatus,
       "faultMIB": faultMIB,
       "eventObjects": eventObjects,
       "eventTable": eventTable,
       "eventEntry": eventEntry,
       "eventSeqNum": eventSeqNum,
       "eventEventId": eventEventId,
       "eventName": eventName,
       "eventInstanceType": eventInstanceType,
       "eventInstanceId": eventInstanceId,
       "eventInstanceName": eventInstanceName,
       "eventSeverity": eventSeverity,
       "eventSetTime": eventSetTime,
       "eventDescription": eventDescription,
       "eventServAffective": eventServAffective,
       "eventInstanceIdNumber": eventInstanceIdNumber,
       "faultTrapsMIB": faultTrapsMIB,
       "trapInfoObjects": trapInfoObjects,
       "trapRefSeqNum": trapRefSeqNum,
       "trapPersistence": trapPersistence,
       "trapSenderNodeId": trapSenderNodeId,
       "trapSenderStatus": trapSenderStatus,
       "trapNotifications": trapNotifications,
       "eventOnTrap": eventOnTrap,
       "eventClearedTrap": eventClearedTrap,
       "protoBasedVlanSetup": protoBasedVlanSetup,
       "protoBasedVlanTable": protoBasedVlanTable,
       "protoBasedVlanEntry": protoBasedVlanEntry,
       "protoBasedVlanPort": protoBasedVlanPort,
       "protoBasedVlanPacketType": protoBasedVlanPacketType,
       "protoBasedVlanEtherType": protoBasedVlanEtherType,
       "protoBasedVlanName": protoBasedVlanName,
       "protoBasedVlanVid": protoBasedVlanVid,
       "protoBasedVlanPriority": protoBasedVlanPriority,
       "protoBasedVlanState": protoBasedVlanState,
       "sysLogSetup": sysLogSetup,
       "sysLogState": sysLogState,
       "sysLogTypeTable": sysLogTypeTable,
       "sysLogTypeEntry": sysLogTypeEntry,
       "sysLogTypeIndex": sysLogTypeIndex,
       "sysLogTypeName": sysLogTypeName,
       "sysLogTypeState": sysLogTypeState,
       "sysLogTypeFacility": sysLogTypeFacility,
       "sysLogTypeLevel": sysLogTypeLevel,
       "sysLogServerTable": sysLogServerTable,
       "sysLogServerEntry": sysLogServerEntry,
       "sysLogServerAddress": sysLogServerAddress,
       "sysLogServerLogLevel": sysLogServerLogLevel,
       "sysLogServerRowStatus": sysLogServerRowStatus,
       "sysLogUploadSetup": sysLogUploadSetup,
       "sysLogUploadState": sysLogUploadState,
       "sysLogUploadTime": sysLogUploadTime,
       "sysLogUploadServerTable": sysLogUploadServerTable,
       "sysLogUploadServerEntry": sysLogUploadServerEntry,
       "sysLogUploadServerAddress": sysLogUploadServerAddress,
       "sysLogUploadServerUsername": sysLogUploadServerUsername,
       "sysLogUploadServerPassword": sysLogUploadServerPassword,
       "sysLogUploadServerFilepath": sysLogUploadServerFilepath,
       "sysLogUploadServerRowStatus": sysLogUploadServerRowStatus,
       "ipStatus": ipStatus,
       "ipStatusTable": ipStatusTable,
       "ipStatusEntry": ipStatusEntry,
       "ipStatusIPAddress": ipStatusIPAddress,
       "ipStatusVid": ipStatusVid,
       "ipStatusPort": ipStatusPort,
       "ipStatusType": ipStatusType,
       "dhcpSnp": dhcpSnp,
       "dhcpSnpVlanTable": dhcpSnpVlanTable,
       "dhcpSnpVlanEntry": dhcpSnpVlanEntry,
       "dhcpSnpVlanEntryVid": dhcpSnpVlanEntryVid,
       "dhcpSnpVlanEntryEnable": dhcpSnpVlanEntryEnable,
       "dhcpSnpVlanEntryOption82Enable": dhcpSnpVlanEntryOption82Enable,
       "dhcpSnpVlanEntryInfo": dhcpSnpVlanEntryInfo,
       "dhcpSnpVlanEntryOption82FormatEnable": dhcpSnpVlanEntryOption82FormatEnable,
       "dhcpSnpPortTable": dhcpSnpPortTable,
       "dhcpSnpPortEntry": dhcpSnpPortEntry,
       "dhcpSnpPortEntryPort": dhcpSnpPortEntryPort,
       "dhcpSnpPortEntryTrust": dhcpSnpPortEntryTrust,
       "dhcpSnpPortEntryRate": dhcpSnpPortEntryRate,
       "dhcpSnpBindTable": dhcpSnpBindTable,
       "dhcpSnpBindEntry": dhcpSnpBindEntry,
       "dhcpSnpBindEntryMac": dhcpSnpBindEntryMac,
       "dhcpSnpBindEntryVid": dhcpSnpBindEntryVid,
       "dhcpSnpBindEntryIP": dhcpSnpBindEntryIP,
       "dhcpSnpBindEntryLease": dhcpSnpBindEntryLease,
       "dhcpSnpBindEntryType": dhcpSnpBindEntryType,
       "dhcpSnpBindEntryPort": dhcpSnpBindEntryPort,
       "dhcpSnpEnable": dhcpSnpEnable,
       "dhcpSnpDb": dhcpSnpDb,
       "dhcpSnpDbAbort": dhcpSnpDbAbort,
       "dhcpSnpDbWriteDelay": dhcpSnpDbWriteDelay,
       "dhcpSnpDbUrl": dhcpSnpDbUrl,
       "dhcpSnpDbUrlRenew": dhcpSnpDbUrlRenew,
       "dhcpSnpDbStat": dhcpSnpDbStat,
       "dhcpSnpDbStatClear": dhcpSnpDbStatClear,
       "dhcpSnpDbStatAgentRunning": dhcpSnpDbStatAgentRunning,
       "dhcpSnpDbStatDelayExpiry": dhcpSnpDbStatDelayExpiry,
       "dhcpSnpDbStatAbortExpiry": dhcpSnpDbStatAbortExpiry,
       "dhcpSnpDbStatLastSuccTime": dhcpSnpDbStatLastSuccTime,
       "dhcpSnpDbStatLastFailTime": dhcpSnpDbStatLastFailTime,
       "dhcpSnpDbStatLastFailReason": dhcpSnpDbStatLastFailReason,
       "dhcpSnpDbStatTotalAttempt": dhcpSnpDbStatTotalAttempt,
       "dhcpSnpDbStatStartupFail": dhcpSnpDbStatStartupFail,
       "dhcpSnpDbStatSuccTrans": dhcpSnpDbStatSuccTrans,
       "dhcpSnpDbStatFailTrans": dhcpSnpDbStatFailTrans,
       "dhcpSnpDbStatSuccRead": dhcpSnpDbStatSuccRead,
       "dhcpSnpDbStatFailRead": dhcpSnpDbStatFailRead,
       "dhcpSnpDbStatSuccWrite": dhcpSnpDbStatSuccWrite,
       "dhcpSnpDbStatFailWrite": dhcpSnpDbStatFailWrite,
       "dhcpSnpDbStatFirstSuccAccess": dhcpSnpDbStatFirstSuccAccess,
       "dhcpSnpDbStatLastIgnoreBindCol": dhcpSnpDbStatLastIgnoreBindCol,
       "dhcpSnpDbStatLastIgnoreExpireLease": dhcpSnpDbStatLastIgnoreExpireLease,
       "dhcpSnpDbStatLastIgnoreInvalidIntf": dhcpSnpDbStatLastIgnoreInvalidIntf,
       "dhcpSnpDbStatLastIgnoreUnsuppVlan": dhcpSnpDbStatLastIgnoreUnsuppVlan,
       "dhcpSnpDbStatLastIgnoreParse": dhcpSnpDbStatLastIgnoreParse,
       "dhcpSnpDbStatTotalIgnoreBindCol": dhcpSnpDbStatTotalIgnoreBindCol,
       "dhcpSnpDbStatTotalIgnoreExpireLease": dhcpSnpDbStatTotalIgnoreExpireLease,
       "dhcpSnpDbStatTotalIgnoreInvalidIntf": dhcpSnpDbStatTotalIgnoreInvalidIntf,
       "dhcpSnpDbStatTotalIgnoreUnsuppVlan": dhcpSnpDbStatTotalIgnoreUnsuppVlan,
       "dhcpSnpDbStatTotalIgnoreParse": dhcpSnpDbStatTotalIgnoreParse,
       "dhcpSnpDbStatFirstSuccessAccess": dhcpSnpDbStatFirstSuccessAccess,
       "dhcpSnpDhcpVlan": dhcpSnpDhcpVlan,
       "dhcpSnpDhcpVlanVid": dhcpSnpDhcpVlanVid,
       "ipsg": ipsg,
       "ipsgTable": ipsgTable,
       "ipsgEntry": ipsgEntry,
       "ipsgEntryMac": ipsgEntryMac,
       "ipsgEntryVid": ipsgEntryVid,
       "ipsgEntryIp": ipsgEntryIp,
       "ipsgEntryLease": ipsgEntryLease,
       "ipsgEntryType": ipsgEntryType,
       "ipsgEntryPort": ipsgEntryPort,
       "ipsgEntryState": ipsgEntryState,
       "arpInspect": arpInspect,
       "arpInspectSetup": arpInspectSetup,
       "arpInspectState": arpInspectState,
       "arpInspectFilterAgingTime": arpInspectFilterAgingTime,
       "arpInspectLog": arpInspectLog,
       "arpInspectLogEntries": arpInspectLogEntries,
       "arpInspectLogRate": arpInspectLogRate,
       "arpInspectLogInterval": arpInspectLogInterval,
       "arpInspectVlanTable": arpInspectVlanTable,
       "arpInspectVlanEntry": arpInspectVlanEntry,
       "arpInspectVlanVid": arpInspectVlanVid,
       "arpInspectVlanLog": arpInspectVlanLog,
       "arpInspectVlanStatus": arpInspectVlanStatus,
       "arpInspectPortTable": arpInspectPortTable,
       "arpInspectPortEntry": arpInspectPortEntry,
       "arpInspectPortIndex": arpInspectPortIndex,
       "arpInspectPortTrust": arpInspectPortTrust,
       "arpInspectPortRate": arpInspectPortRate,
       "arpInspectPortInterval": arpInspectPortInterval,
       "arpInspectStatus": arpInspectStatus,
       "arpInspectFilterClear": arpInspectFilterClear,
       "arpInspectLogClear": arpInspectLogClear,
       "arpInspectFilterTable": arpInspectFilterTable,
       "arpInspectFilterEntry": arpInspectFilterEntry,
       "arpInspectFilterMac": arpInspectFilterMac,
       "arpInspectFilterVid": arpInspectFilterVid,
       "arpInspectFilterPort": arpInspectFilterPort,
       "arpInspectFilterExpiry": arpInspectFilterExpiry,
       "arpInspectFilterReason": arpInspectFilterReason,
       "arpInspectFilterRowStatus": arpInspectFilterRowStatus,
       "arpInspectLogTable": arpInspectLogTable,
       "arpInspectLogEntry": arpInspectLogEntry,
       "arpInspectLogMac": arpInspectLogMac,
       "arpInspectLogVid": arpInspectLogVid,
       "arpInspectLogPort": arpInspectLogPort,
       "arpInspectLogIp": arpInspectLogIp,
       "arpInspectLogNumPkt": arpInspectLogNumPkt,
       "arpInspectLogReason": arpInspectLogReason,
       "arpInspectLogTime": arpInspectLogTime,
       "arpInspectStatisticsTable": arpInspectStatisticsTable,
       "arpInspectStatisticsEntry": arpInspectStatisticsEntry,
       "arpInspectStatisticsVid": arpInspectStatisticsVid,
       "arpInspectStatisticsReceived": arpInspectStatisticsReceived,
       "arpInspectStatisticsRequest": arpInspectStatisticsRequest,
       "arpInspectStatisticsReply": arpInspectStatisticsReply,
       "arpInspectStatisticsForward": arpInspectStatisticsForward,
       "arpInspectStatisticsDrop": arpInspectStatisticsDrop,
       "arpInspectStatisticsClear": arpInspectStatisticsClear,
       "trTCMSetup": trTCMSetup,
       "trTCMState": trTCMState,
       "trTCMMode": trTCMMode,
       "trTCMPortTable": trTCMPortTable,
       "trTCMPortEntry": trTCMPortEntry,
       "trTCMPortState": trTCMPortState,
       "trTCMPortCIR": trTCMPortCIR,
       "trTCMPortPIR": trTCMPortPIR,
       "trTCMPortDscpGreen": trTCMPortDscpGreen,
       "trTCMPortDscpYellow": trTCMPortDscpYellow,
       "trTCMPortDscpRed": trTCMPortDscpRed,
       "loopGuardSetup": loopGuardSetup,
       "loopGuardState": loopGuardState,
       "loopGuardPortTable": loopGuardPortTable,
       "loopGuardPortEntry": loopGuardPortEntry,
       "loopGuardPortState": loopGuardPortState,
       "subnetBasedVlanSetup": subnetBasedVlanSetup,
       "subnetBasedVlanState": subnetBasedVlanState,
       "dhcpVlanOverrideState": dhcpVlanOverrideState,
       "subnetBasedVlanTable": subnetBasedVlanTable,
       "subnetBasedVlanEntry": subnetBasedVlanEntry,
       "subnetBasedVlanSrcIp": subnetBasedVlanSrcIp,
       "subnetBasedVlanSrcMaskBit": subnetBasedVlanSrcMaskBit,
       "subnetBasedVlanName": subnetBasedVlanName,
       "subnetBasedVlanVid": subnetBasedVlanVid,
       "subnetBasedVlanPriority": subnetBasedVlanPriority,
       "subnetBasedVlanEntryState": subnetBasedVlanEntryState,
       "macAuthenticationSetup": macAuthenticationSetup,
       "macAuthenticationState": macAuthenticationState,
       "macAuthenticationNamePrefix": macAuthenticationNamePrefix,
       "macAuthenticationPassword": macAuthenticationPassword,
       "macAuthenticationTimeout": macAuthenticationTimeout,
       "macAuthenticationPortTable": macAuthenticationPortTable,
       "macAuthenticationPortEntry": macAuthenticationPortEntry,
       "macAuthenticationPortState": macAuthenticationPortState,
       "mstp": mstp,
       "mstpGen": mstpGen,
       "mstpGenState": mstpGenState,
       "mstpGenCfgIdName": mstpGenCfgIdName,
       "mstpGenCfgIdRevLevel": mstpGenCfgIdRevLevel,
       "mstpGenCfgIdCfgDigest": mstpGenCfgIdCfgDigest,
       "mstpGenHelloTime": mstpGenHelloTime,
       "mstpGenMaxAge": mstpGenMaxAge,
       "mstpGenForwardDelay": mstpGenForwardDelay,
       "mstpGenMaxHops": mstpGenMaxHops,
       "mstpGenCistRootPathCost": mstpGenCistRootPathCost,
       "mstpGenCistRootBrid": mstpGenCistRootBrid,
       "mstMapTable": mstMapTable,
       "mstMapEntry": mstMapEntry,
       "mstMapIndex": mstMapIndex,
       "mstMapVlans1k": mstMapVlans1k,
       "mstMapVlans2k": mstMapVlans2k,
       "mstMapVlans3k": mstMapVlans3k,
       "mstMapVlans4k": mstMapVlans4k,
       "mstMapRowStatus": mstMapRowStatus,
       "mstVlanTable": mstVlanTable,
       "mstVlanEntry": mstVlanEntry,
       "mstVlanIndex": mstVlanIndex,
       "mstVlanMstIndex": mstVlanMstIndex,
       "mstpPortTable": mstpPortTable,
       "mstpPortEntry": mstpPortEntry,
       "mstpPortIndex": mstpPortIndex,
       "mstpPortOperEdgePort": mstpPortOperEdgePort,
       "mstpPortOperPointToPointMAC": mstpPortOperPointToPointMAC,
       "mstpPortAdminEdgePort": mstpPortAdminEdgePort,
       "mstpXstTable": mstpXstTable,
       "mstpXstEntry": mstpXstEntry,
       "mstpXstId": mstpXstId,
       "mstpXstBridgePriority": mstpXstBridgePriority,
       "mstpXstBridgeId": mstpXstBridgeId,
       "mstpXstInternalRootCost": mstpXstInternalRootCost,
       "mstpXstRootPort": mstpXstRootPort,
       "mstpXstTimeSinceTopologyChange": mstpXstTimeSinceTopologyChange,
       "mstpXstTopologyChangesCount": mstpXstTopologyChangesCount,
       "mstpXstPortTable": mstpXstPortTable,
       "mstpXstPortEntry": mstpXstPortEntry,
       "mstpXstPortXstId": mstpXstPortXstId,
       "mstpXstPortIndex": mstpXstPortIndex,
       "mstpXstPortEnable": mstpXstPortEnable,
       "mstpXstPortPriority": mstpXstPortPriority,
       "mstpXstPortPathCost": mstpXstPortPathCost,
       "mstpXstPortState": mstpXstPortState,
       "mstpXstPortDesignatedRoot": mstpXstPortDesignatedRoot,
       "mstpXstPortDesignatedCost": mstpXstPortDesignatedCost,
       "mstpXstPortDesignatedBridge": mstpXstPortDesignatedBridge,
       "mstpXstPortDesignatedPort": mstpXstPortDesignatedPort,
       "mstpNotifications": mstpNotifications,
       "newRoot": newRoot,
       "topologyChange": topologyChange,
       "radiusServerSetup": radiusServerSetup,
       "radiusAuthServerSetup": radiusAuthServerSetup,
       "radiusAuthServerMode": radiusAuthServerMode,
       "radiusAuthServerTimeout": radiusAuthServerTimeout,
       "radiusAuthServerTable": radiusAuthServerTable,
       "radiusAuthServerEntry": radiusAuthServerEntry,
       "radiusAuthServerIndex": radiusAuthServerIndex,
       "radiusAuthServerIpAddr": radiusAuthServerIpAddr,
       "radiusAuthServerUdpPort": radiusAuthServerUdpPort,
       "radiusAuthServerSharedSecret": radiusAuthServerSharedSecret,
       "radiusAcctServerSetup": radiusAcctServerSetup,
       "radiusAcctServerTimeout": radiusAcctServerTimeout,
       "radiusAcctServerTable": radiusAcctServerTable,
       "radiusAcctServerEntry": radiusAcctServerEntry,
       "radiusAcctServerIndex": radiusAcctServerIndex,
       "radiusAcctServerIpAddr": radiusAcctServerIpAddr,
       "radiusAcctServerUdpPort": radiusAcctServerUdpPort,
       "radiusAcctServerSharedSecret": radiusAcctServerSharedSecret,
       "tacacsServerSetup": tacacsServerSetup,
       "tacacsAuthServerSetup": tacacsAuthServerSetup,
       "tacacsAuthServerMode": tacacsAuthServerMode,
       "tacacsAuthServerTimeout": tacacsAuthServerTimeout,
       "tacacsAuthServerTable": tacacsAuthServerTable,
       "tacacsAuthServerEntry": tacacsAuthServerEntry,
       "tacacsAuthServerIndex": tacacsAuthServerIndex,
       "tacacsAuthServerIpAddr": tacacsAuthServerIpAddr,
       "tacacsAuthServerTcpPort": tacacsAuthServerTcpPort,
       "tacacsAuthServerSharedSecret": tacacsAuthServerSharedSecret,
       "tacacsAcctServerSetup": tacacsAcctServerSetup,
       "tacacsAcctServerTimeout": tacacsAcctServerTimeout,
       "tacacsAcctServerTable": tacacsAcctServerTable,
       "tacacsAcctServerEntry": tacacsAcctServerEntry,
       "tacacsAcctServerIndex": tacacsAcctServerIndex,
       "tacacsAcctServerIpAddr": tacacsAcctServerIpAddr,
       "tacacsAcctServerTcpPort": tacacsAcctServerTcpPort,
       "tacacsAcctServerSharedSecret": tacacsAcctServerSharedSecret,
       "aaaSetup": aaaSetup,
       "authenticationSetup": authenticationSetup,
       "authenticationTypeTable": authenticationTypeTable,
       "authenticationTypeEntry": authenticationTypeEntry,
       "authenticationTypeName": authenticationTypeName,
       "authenticationTypeMethodList": authenticationTypeMethodList,
       "accountingSetup": accountingSetup,
       "accountingUpdatePeriod": accountingUpdatePeriod,
       "accountingTypeTable": accountingTypeTable,
       "accountingTypeEntry": accountingTypeEntry,
       "accountingTypeName": accountingTypeName,
       "accountingTypeActive": accountingTypeActive,
       "accountingTypeBroadcast": accountingTypeBroadcast,
       "accountingTypeMode": accountingTypeMode,
       "accountingTypeMethod": accountingTypeMethod,
       "accountingTypePrivilege": accountingTypePrivilege,
       "authorizationSetup": authorizationSetup,
       "authorizationTypeTable": authorizationTypeTable,
       "authorizationTypeEntry": authorizationTypeEntry,
       "authorizationTypeName": authorizationTypeName,
       "authorizationTypeActive": authorizationTypeActive,
       "authorizationTypeMethod": authorizationTypeMethod,
       "vlanTranslationSetup": vlanTranslationSetup,
       "vlanTranslationRuleTable": vlanTranslationRuleTable,
       "vlanTranslationRuleEntry": vlanTranslationRuleEntry,
       "vlanTranslationRuleName": vlanTranslationRuleName,
       "vlanTranslationRulePort": vlanTranslationRulePort,
       "vlanTranslationRuleOuterVid": vlanTranslationRuleOuterVid,
       "vlanTranslationRuleOuterPriority": vlanTranslationRuleOuterPriority,
       "vlanTranslationRuleInnerVid": vlanTranslationRuleInnerVid,
       "vlanTranslationRuleInnerPriority": vlanTranslationRuleInnerPriority,
       "vlanTranslationRuleTransSVid": vlanTranslationRuleTransSVid,
       "vlanTranslationRuleSPriority": vlanTranslationRuleSPriority,
       "vlanTranslationRuleTransCVid": vlanTranslationRuleTransCVid,
       "vlanTranslationRuleCPriority": vlanTranslationRuleCPriority,
       "vlanTranslationRuleN1Map": vlanTranslationRuleN1Map,
       "vlanTranslationRuleCrossConnect": vlanTranslationRuleCrossConnect,
       "vlanTranslationRuleCrossPort": vlanTranslationRuleCrossPort,
       "vlanTranslationRuleTr156": vlanTranslationRuleTr156,
       "vlanTranslationRuleRowStatus": vlanTranslationRuleRowStatus,
       "transceiverInfo": transceiverInfo,
       "transceiverSerialInfoTable": transceiverSerialInfoTable,
       "transceiverSerialInfoEntry": transceiverSerialInfoEntry,
       "transceiverSerialInfoEntryPort": transceiverSerialInfoEntryPort,
       "transceiverSerialInfoEntryStatus": transceiverSerialInfoEntryStatus,
       "transceiverSerialInfoEntryVendor": transceiverSerialInfoEntryVendor,
       "transceiverSerialInfoEntryPartNo": transceiverSerialInfoEntryPartNo,
       "transceiverSerialInfoEntrySerialNo": transceiverSerialInfoEntrySerialNo,
       "transceiverSerialInfoEntryRevision": transceiverSerialInfoEntryRevision,
       "transceiverSerialInfoEntryDateCode": transceiverSerialInfoEntryDateCode,
       "transceiverSerialInfoEntryTransceiver": transceiverSerialInfoEntryTransceiver,
       "transceiverDdmInfoTable": transceiverDdmInfoTable,
       "transceiverDdmInfoEntry": transceiverDdmInfoEntry,
       "transceiverDdmInfoEntryPort": transceiverDdmInfoEntryPort,
       "transceiverDdmInfoEntryType": transceiverDdmInfoEntryType,
       "transceiverDdmInfoEntryAlarmMax": transceiverDdmInfoEntryAlarmMax,
       "transceiverDdmInfoEntryAlarmMin": transceiverDdmInfoEntryAlarmMin,
       "transceiverDdmInfoEntryWarnMax": transceiverDdmInfoEntryWarnMax,
       "transceiverDdmInfoEntryWarnMin": transceiverDdmInfoEntryWarnMin,
       "transceiverDdmInfoEntryCurrent": transceiverDdmInfoEntryCurrent,
       "transceiverDdmInfoEntryDescription": transceiverDdmInfoEntryDescription,
       "transceiverDdmInfoProfileTable": transceiverDdmInfoProfileTable,
       "transceiverDdmInfoProfileEntry": transceiverDdmInfoProfileEntry,
       "transceiverDdmInfoProfilePort": transceiverDdmInfoProfilePort,
       "transceiverDdmInfoProfileType": transceiverDdmInfoProfileType,
       "transceiverDdmInfoProfileAlarmMax": transceiverDdmInfoProfileAlarmMax,
       "transceiverDdmInfoProfileAlarmMin": transceiverDdmInfoProfileAlarmMin,
       "transceiverDdmInfoProfileWarnMax": transceiverDdmInfoProfileWarnMax,
       "transceiverDdmInfoProfileWarnMin": transceiverDdmInfoProfileWarnMin,
       "transceiverDdmInfoProfileDescription": transceiverDdmInfoProfileDescription,
       "transceiverDdmInfoProfileRowstatus": transceiverDdmInfoProfileRowstatus,
       "timeSlot": timeSlot,
       "transceiverPerOntTable": transceiverPerOntTable,
       "transceiverPerOntEntry": transceiverPerOntEntry,
       "transceiverPerOntNumber": transceiverPerOntNumber,
       "transceiverPerOntRxPower": transceiverPerOntRxPower,
       "dot1agCfmSetup": dot1agCfmSetup,
       "dot1agCfmMIBObjects": dot1agCfmMIBObjects,
       "dot1agCfmMep": dot1agCfmMep,
       "zyswdot1agCfmMepTable": zyswdot1agCfmMepTable,
       "zyswdot1agCfmMepEntry": zyswdot1agCfmMepEntry,
       "zyswdot1agCfmMepTransmitLbmDataTlvSize": zyswdot1agCfmMepTransmitLbmDataTlvSize,
       "sysMemoryPool": sysMemoryPool,
       "sysMemoryPoolTable": sysMemoryPoolTable,
       "sysMemoryPoolEntry": sysMemoryPoolEntry,
       "sysMemoryPoolId": sysMemoryPoolId,
       "sysMemoryPoolName": sysMemoryPoolName,
       "sysMemoryPoolTotal": sysMemoryPoolTotal,
       "sysMemoryPoolUsed": sysMemoryPoolUsed,
       "sysMemoryPoolUtil": sysMemoryPoolUtil,
       "pppoe": pppoe,
       "pppoeIaSetup": pppoeIaSetup,
       "pppoeIaState": pppoeIaState,
       "pppoeIaPortTable": pppoeIaPortTable,
       "pppoeIaPortEntry": pppoeIaPortEntry,
       "pppoeIaPortEntryPort": pppoeIaPortEntryPort,
       "pppoeIaPortEntryTrust": pppoeIaPortEntryTrust,
       "pppoeIaVlanTable": pppoeIaVlanTable,
       "pppoeIaVlanEntry": pppoeIaVlanEntry,
       "pppoeIaVlanEntryVid": pppoeIaVlanEntryVid,
       "pppoeIaVlanEntryCircuitID": pppoeIaVlanEntryCircuitID,
       "pppoeIaVlanEntryRemoteID": pppoeIaVlanEntryRemoteID,
       "pppoeIaVlanEntryRowStatus": pppoeIaVlanEntryRowStatus,
       "pppoeIaVlanOpt82Table": pppoeIaVlanOpt82Table,
       "pppoeIaVlanOpt82Entry": pppoeIaVlanOpt82Entry,
       "pppoeIaVlanOpt82EntryVid": pppoeIaVlanOpt82EntryVid,
       "pppoeIaVlanOpt82Enable": pppoeIaVlanOpt82Enable,
       "pppoeIaVlanOpt82EntryCircuitIDString": pppoeIaVlanOpt82EntryCircuitIDString,
       "pppoeIaVlanOpt82EntryRemoteIDString": pppoeIaVlanOpt82EntryRemoteIDString,
       "pppoeIaVlanOpt82EntryRowStatus": pppoeIaVlanOpt82EntryRowStatus,
       "pppoeClientTestTable": pppoeClientTestTable,
       "pppoeClientTestEntry": pppoeClientTestEntry,
       "pppoeClientTestEntryIndex": pppoeClientTestEntryIndex,
       "pppoeClientTestEntryPort": pppoeClientTestEntryPort,
       "pppoeClientTestEntryOntId": pppoeClientTestEntryOntId,
       "pppoeClientTestEntryOntCardId": pppoeClientTestEntryOntCardId,
       "pppoeClientTestEntryUniport": pppoeClientTestEntryUniport,
       "pppoeClientTestEntryUsername": pppoeClientTestEntryUsername,
       "pppoeClientTestEntryPassword": pppoeClientTestEntryPassword,
       "pppoeClientTestEntrySNISVID": pppoeClientTestEntrySNISVID,
       "pppoeClientTestEntrySNICVID": pppoeClientTestEntrySNICVID,
       "pppoeClientTestEntryNNISVID": pppoeClientTestEntryNNISVID,
       "pppoeClientTestEntryUNIVID": pppoeClientTestEntryUNIVID,
       "pppoeClientTestEntrySn": pppoeClientTestEntrySn,
       "pppoeClientTestEntryTimeout": pppoeClientTestEntryTimeout,
       "pppoeClientTestEntryIpaddr": pppoeClientTestEntryIpaddr,
       "pppoeClientTestEntryStatus": pppoeClientTestEntryStatus,
       "arpLearningSetup": arpLearningSetup,
       "arpLearningPortTable": arpLearningPortTable,
       "arpLearningPortEntry": arpLearningPortEntry,
       "arpLearningPortMode": arpLearningPortMode,
       "staticRouteSetup": staticRouteSetup,
       "maxNumberOfStaticRoutes": maxNumberOfStaticRoutes,
       "staticRouteTable": staticRouteTable,
       "staticRouteEntry": staticRouteEntry,
       "staticRouteName": staticRouteName,
       "staticRouteIp": staticRouteIp,
       "staticRouteMask": staticRouteMask,
       "staticRouteGateway": staticRouteGateway,
       "staticRouteMetric": staticRouteMetric,
       "staticRouteRowStatus": staticRouteRowStatus,
       "routingStatus": routingStatus,
       "routingStatusTable": routingStatusTable,
       "routingStatusEntry": routingStatusEntry,
       "routingStatusDestAddress": routingStatusDestAddress,
       "routingStatusDestMaskbits": routingStatusDestMaskbits,
       "routingStatusGateway": routingStatusGateway,
       "routingStatusInterface": routingStatusInterface,
       "routingStatusMetric": routingStatusMetric,
       "routingStatusType": routingStatusType,
       "externalAlarmSetup": externalAlarmSetup,
       "externalAlarmTable": externalAlarmTable,
       "externalAlarmEntry": externalAlarmEntry,
       "externalAlarmIndex": externalAlarmIndex,
       "externalAlarmName": externalAlarmName,
       "externalAlarmStatus": externalAlarmStatus,
       "errdisable": errdisable,
       "recovery": recovery,
       "errdisableRecoverySetup": errdisableRecoverySetup,
       "errdisableRecoveryState": errdisableRecoveryState,
       "errdisableRecoveryReasonTable": errdisableRecoveryReasonTable,
       "errdisableRecoveryReasonEntry": errdisableRecoveryReasonEntry,
       "errdisableRecoveryReason": errdisableRecoveryReason,
       "errdisableRecoveryReasonActive": errdisableRecoveryReasonActive,
       "errdisableRecoveryReasonInterval": errdisableRecoveryReasonInterval,
       "errdisableRecoveryIfStatusTable": errdisableRecoveryIfStatusTable,
       "errdisableRecoveryIfStatusEntry": errdisableRecoveryIfStatusEntry,
       "errdisableRecoveryIfStatusReason": errdisableRecoveryIfStatusReason,
       "errdisableRecoveryIfStatusPort": errdisableRecoveryIfStatusPort,
       "errdisableRecoveryIfStatusTimeToRecover": errdisableRecoveryIfStatusTimeToRecover,
       "detect": detect,
       "errdisableDetectReasonTable": errdisableDetectReasonTable,
       "errdisableDetectReasonEntry": errdisableDetectReasonEntry,
       "errdisableDetectReason": errdisableDetectReason,
       "errdisableDetectReasonEnable": errdisableDetectReasonEnable,
       "errdisableDetectReasonMode": errdisableDetectReasonMode,
       "errdisableTrapInfoObject": errdisableTrapInfoObject,
       "errdisableTrapPort": errdisableTrapPort,
       "errdisableTrapReason": errdisableTrapReason,
       "errdisableTrapMode": errdisableTrapMode,
       "errdisableTrapNotifications": errdisableTrapNotifications,
       "errdisableDetectTrap": errdisableDetectTrap,
       "errdisableRecoveryTrap": errdisableRecoveryTrap,
       "cpuProtectionSetup": cpuProtectionSetup,
       "cpuProtectionTable": cpuProtectionTable,
       "cpuProtectionEntry": cpuProtectionEntry,
       "cpuProtectionPort": cpuProtectionPort,
       "cpuProtectionReason": cpuProtectionReason,
       "cpuProtectionRateLimitSet": cpuProtectionRateLimitSet,
       "remoteOnt": remoteOnt,
       "ontSetup": ontSetup,
       "ontTable": ontTable,
       "ontEntry": ontEntry,
       "ontNumber": ontNumber,
       "password": password,
       "planVersion": planVersion,
       "sn": sn,
       "loopbackConfig": loopbackConfig,
       "loopbackStatus": loopbackStatus,
       "model": model,
       "ontRowStatus": ontRowStatus,
       "ontAction": ontAction,
       "alarmProfile": alarmProfile,
       "fullBridg": fullBridg,
       "antiMacSpoofing": antiMacSpoofing,
       "description": description,
       "option82CircuitIdOptInfo": option82CircuitIdOptInfo,
       "option82RemoteIdOptInfo": option82RemoteIdOptInfo,
       "templateDescription": templateDescription,
       "usFecMode": usFecMode,
       "option82DisableDhcp": option82DisableDhcp,
       "option82PassThroughDhcp": option82PassThroughDhcp,
       "option82DisablePppoe": option82DisablePppoe,
       "option82PassThroughPppoe": option82PassThroughPppoe,
       "ontBwGroupTable": ontBwGroupTable,
       "ontBwGroupEntry": ontBwGroupEntry,
       "ontBwGroupId": ontBwGroupId,
       "ontBwGroupUstype": ontBwGroupUstype,
       "ontBwGroupUsbwprofname": ontBwGroupUsbwprofname,
       "ontBwGroupDsbwprofname": ontBwGroupDsbwprofname,
       "ontBwGroupRowStatus": ontBwGroupRowStatus,
       "ontFileTransferParamTable": ontFileTransferParamTable,
       "ontFileTransferParamEntry": ontFileTransferParamEntry,
       "ontFileTransferFileUri": ontFileTransferFileUri,
       "ontFileTransferLocalFileName": ontFileTransferLocalFileName,
       "ontFileTransferUserName": ontFileTransferUserName,
       "ontFileTransferPassword": ontFileTransferPassword,
       "ontWanConfigTable": ontWanConfigTable,
       "ontWanConfigEntry": ontWanConfigEntry,
       "ontWanConfigId": ontWanConfigId,
       "ontWanConfigVlan": ontWanConfigVlan,
       "ontWanConfigPriority": ontWanConfigPriority,
       "ontWanConfigNat": ontWanConfigNat,
       "ontWanConfigUsername": ontWanConfigUsername,
       "ontWanConfigPassword": ontWanConfigPassword,
       "ontWanConfigRowStatus": ontWanConfigRowStatus,
       "ontResetTable": ontResetTable,
       "ontResetEntry": ontResetEntry,
       "ontResetAction": ontResetAction,
       "ontConfgurationStatus": ontConfgurationStatus,
       "ontTimeOfRestore": ontTimeOfRestore,
       "ontStormingTable": ontStormingTable,
       "ontStormingEntry": ontStormingEntry,
       "ontStormingThreshold": ontStormingThreshold,
       "ontStormingLoopGuard": ontStormingLoopGuard,
       "ontAclServiceTable": ontAclServiceTable,
       "ontAclServiceEntry": ontAclServiceEntry,
       "ontAclRuleId": ontAclRuleId,
       "ontAclProfName": ontAclProfName,
       "ontAclServiceRowStatus": ontAclServiceRowStatus,
       "ontcardTable": ontcardTable,
       "ontcardEntry": ontcardEntry,
       "ontcard": ontcard,
       "ontcardType": ontcardType,
       "numofport": numofport,
       "ontcardRowStatus": ontcardRowStatus,
       "ontcardAction": ontcardAction,
       "ontenetTable": ontenetTable,
       "ontenetEntry": ontenetEntry,
       "ontenetCardPort": ontenetCardPort,
       "pmenetEnable": pmenetEnable,
       "portSpeed": portSpeed,
       "ontenetRowStatus": ontenetRowStatus,
       "ontenetAction": ontenetAction,
       "ontvdslTable": ontvdslTable,
       "ontvdslEntry": ontvdslEntry,
       "ontvdslCardPort": ontvdslCardPort,
       "lineTemplate": lineTemplate,
       "ontvdslRowStatus": ontvdslRowStatus,
       "ontvdslAction": ontvdslAction,
       "ontuniportSetup": ontuniportSetup,
       "ontuniportTable": ontuniportTable,
       "ontuniportEntry": ontuniportEntry,
       "uniPort": uniPort,
       "uniPortRowStatus": uniPortRowStatus,
       "uniPortAction": uniPortAction,
       "uniportMacLimit": uniportMacLimit,
       "uniportIgmpchannelTable": uniportIgmpchannelTable,
       "uniportIgmpchannelEntry": uniportIgmpchannelEntry,
       "uniportIgmpchannelUniSvid": uniportIgmpchannelUniSvid,
       "uniportIgmpchannelUniCvid": uniportIgmpchannelUniCvid,
       "uniportIgmpchannelVersion": uniportIgmpchannelVersion,
       "uniportIgmpchannelMaxgroup": uniportIgmpchannelMaxgroup,
       "uniportIgmpchannelMaxmsg": uniportIgmpchannelMaxmsg,
       "uniportIgmpchannelSignaling": uniportIgmpchannelSignaling,
       "uniportIgmpchannelPreviewpkg": uniportIgmpchannelPreviewpkg,
       "uniportIgmpchannelFullviewpkg": uniportIgmpchannelFullviewpkg,
       "uniportIgmpchannelRowStatus": uniportIgmpchannelRowStatus,
       "uniportIgmpchannelTrafficTxTag": uniportIgmpchannelTrafficTxTag,
       "uniportIgmpchannelCacProf": uniportIgmpchannelCacProf,
       "uniportIgmpchannelTrafficTxTagRepVid": uniportIgmpchannelTrafficTxTagRepVid,
       "uniportProtoBasedTable": uniportProtoBasedTable,
       "uniportProtoBasedEntry": uniportProtoBasedEntry,
       "uniportProtoBasedEtherType": uniportProtoBasedEtherType,
       "uniportProtoBasedSvid": uniportProtoBasedSvid,
       "uniportProtoBasedCvid": uniportProtoBasedCvid,
       "uniportProtoBasedPriority": uniportProtoBasedPriority,
       "uniportProtoBasedRowStatus": uniportProtoBasedRowStatus,
       "uniportPvidTable": uniportPvidTable,
       "uniportPvidEntry": uniportPvidEntry,
       "uniportPvidUniSvid": uniportPvidUniSvid,
       "uniportPvidUniCvid": uniportPvidUniCvid,
       "uniportPvidPriority": uniportPvidPriority,
       "uniportPvidRowStatus": uniportPvidRowStatus,
       "uniportQueueTable": uniportQueueTable,
       "uniportQueueEntry": uniportQueueEntry,
       "uniportQueueTc": uniportQueueTc,
       "uniportQueuePriority": uniportQueuePriority,
       "uniportQueueWeight": uniportQueueWeight,
       "uniportQueueUsbwprofname": uniportQueueUsbwprofname,
       "uniportQueueDsbwprofname": uniportQueueDsbwprofname,
       "uniportQueueDsoption": uniportQueueDsoption,
       "uniportQueueUsbwsharegroupid": uniportQueueUsbwsharegroupid,
       "uniportQueueRowStatus": uniportQueueRowStatus,
       "uniportQueueDsbwsharegroupid": uniportQueueDsbwsharegroupid,
       "uniportVlanTable": uniportVlanTable,
       "uniportVlanEntry": uniportVlanEntry,
       "uniportVlanUniSvid": uniportVlanUniSvid,
       "uniportVlanUniCvid": uniportVlanUniCvid,
       "uniportVlanNetworkSvid": uniportVlanNetworkSvid,
       "uniportVlanNetworkSpri": uniportVlanNetworkSpri,
       "uniportVlanNetworkCvid": uniportVlanNetworkCvid,
       "uniportVlanIngProf": uniportVlanIngProf,
       "uniportVlanGemPort": uniportVlanGemPort,
       "uniportVlanTr156": uniportVlanTr156,
       "uniportVlanTxTag": uniportVlanTxTag,
       "uniportVlanPbitProf": uniportVlanPbitProf,
       "uniportVlanDscpToPbit": uniportVlanDscpToPbit,
       "uniportVlanAesEncrypt": uniportVlanAesEncrypt,
       "uniportVlanRowStatus": uniportVlanRowStatus,
       "uniportVlanSharePriority": uniportVlanSharePriority,
       "uniportVlanMacNum": uniportVlanMacNum,
       "uniportVoipTable": uniportVoipTable,
       "uniportVoipEntry": uniportVoipEntry,
       "uniportVoipMode": uniportVoipMode,
       "uniportVoipUniCvid": uniportVoipUniCvid,
       "uniportVoipCommProfName": uniportVoipCommProfName,
       "uniportVoipSipProfName": uniportVoipSipProfName,
       "uniportVoipUsername": uniportVoipUsername,
       "uniportVoipPassword": uniportVoipPassword,
       "uniportVoipDialPlanName": uniportVoipDialPlanName,
       "uniportVoipAor": uniportVoipAor,
       "uniportVoipDispName": uniportVoipDispName,
       "uniportVoipVmailUri": uniportVoipVmailUri,
       "uniportVoipVmailExtimer": uniportVoipVmailExtimer,
       "uniportVoipReleaseTimer": uniportVoipReleaseTimer,
       "uniportVoipRohTimer": uniportVoipRohTimer,
       "uniportVoipRowStatus": uniportVoipRowStatus,
       "ontOmciCfmTable": ontOmciCfmTable,
       "omciCfmMdTable": omciCfmMdTable,
       "omciCfmMdEntry": omciCfmMdEntry,
       "omciCfmMdIndex": omciCfmMdIndex,
       "omciCfmMdFormat": omciCfmMdFormat,
       "omciCfmMdName": omciCfmMdName,
       "omciCfmMdLevel": omciCfmMdLevel,
       "omciCfmMdRowStatus": omciCfmMdRowStatus,
       "omciCfmMaTable": omciCfmMaTable,
       "omciCfmMaEntry": omciCfmMaEntry,
       "omciCfmMaIndex": omciCfmMaIndex,
       "omciCfmMaMdIndex": omciCfmMaMdIndex,
       "omciCfmMaFormat": omciCfmMaFormat,
       "omciCfmMaName": omciCfmMaName,
       "omciCfmMaCcmInterval": omciCfmMaCcmInterval,
       "omciCfmMaRowStatus": omciCfmMaRowStatus,
       "ontuniportOmciCfmTable": ontuniportOmciCfmTable,
       "omciCfmMepTable": omciCfmMepTable,
       "omciCfmMepEntry": omciCfmMepEntry,
       "omciCfmMepIdentifier": omciCfmMepIdentifier,
       "omciCfmMepMaIndex": omciCfmMepMaIndex,
       "omciCfmMepCcmLtmPriority": omciCfmMepCcmLtmPriority,
       "omciCfmMepRowStatus": omciCfmMepRowStatus,
       "ontQosProfile": ontQosProfile,
       "ingressProfileTable": ingressProfileTable,
       "ingressProfileEntry": ingressProfileEntry,
       "ingressProfileName": ingressProfileName,
       "ingressProfileDot1p0tc": ingressProfileDot1p0tc,
       "ingressProfileDot1p1tc": ingressProfileDot1p1tc,
       "ingressProfileDot1p2tc": ingressProfileDot1p2tc,
       "ingressProfileDot1p3tc": ingressProfileDot1p3tc,
       "ingressProfileDot1p4tc": ingressProfileDot1p4tc,
       "ingressProfileDot1p5tc": ingressProfileDot1p5tc,
       "ingressProfileDot1p6tc": ingressProfileDot1p6tc,
       "ingressProfileDot1p7tc": ingressProfileDot1p7tc,
       "ingressProfileRowStatus": ingressProfileRowStatus,
       "pbitProfileTable": pbitProfileTable,
       "pbitProfileEntry": pbitProfileEntry,
       "pbitProfileName": pbitProfileName,
       "pbitProfileP0to": pbitProfileP0to,
       "pbitProfileP1to": pbitProfileP1to,
       "pbitProfileP2to": pbitProfileP2to,
       "pbitProfileP3to": pbitProfileP3to,
       "pbitProfileP4to": pbitProfileP4to,
       "pbitProfileP5to": pbitProfileP5to,
       "pbitProfileP6to": pbitProfileP6to,
       "pbitProfileP7to": pbitProfileP7to,
       "pbitProfileRowStatus": pbitProfileRowStatus,
       "bwProfileTable": bwProfileTable,
       "bwProfileEntry": bwProfileEntry,
       "bwProfileName": bwProfileName,
       "bwProfileSir": bwProfileSir,
       "bwProfileAir": bwProfileAir,
       "bwProfilePir": bwProfilePir,
       "bwProfileRowStatus": bwProfileRowStatus,
       "bwProfileModify": bwProfileModify,
       "bwProfileUstype": bwProfileUstype,
       "cacProfileTable": cacProfileTable,
       "cacProfileEntry": cacProfileEntry,
       "cacProfileName": cacProfileName,
       "cacProfileMcastBw": cacProfileMcastBw,
       "cacProfileRowStatus": cacProfileRowStatus,
       "ontAlarmProfileTable": ontAlarmProfileTable,
       "ontAlarmProfileEntry": ontAlarmProfileEntry,
       "ontAlarmProfileName": ontAlarmProfileName,
       "ontAlarmProfileFeedVoltThreshLow": ontAlarmProfileFeedVoltThreshLow,
       "ontAlarmProfileFeedVoltThreshUp": ontAlarmProfileFeedVoltThreshUp,
       "ontAlarmProfileBiasCurrThreshLow": ontAlarmProfileBiasCurrThreshLow,
       "ontAlarmProfileBiasCurrThreshUp": ontAlarmProfileBiasCurrThreshUp,
       "ontAlarmProfileTemperatureThreshLow": ontAlarmProfileTemperatureThreshLow,
       "ontAlarmProfileTemperatureThreshUp": ontAlarmProfileTemperatureThreshUp,
       "ontAlarmProfileTxPowerThreshLow": ontAlarmProfileTxPowerThreshLow,
       "ontAlarmProfileTxPowerThreshUp": ontAlarmProfileTxPowerThreshUp,
       "ontAlarmProfileRowStatus": ontAlarmProfileRowStatus,
       "ontAlarmProfileRxPowerThreshLow": ontAlarmProfileRxPowerThreshLow,
       "ontAlarmProfileRxPowerThreshUp": ontAlarmProfileRxPowerThreshUp,
       "ontvenetTable": ontvenetTable,
       "ontvenetEntry": ontvenetEntry,
       "ontvenetCardPort": ontvenetCardPort,
       "pmvenetEnable": pmvenetEnable,
       "ontvenetRowStatus": ontvenetRowStatus,
       "ontvenetAction": ontvenetAction,
       "ontpotsTable": ontpotsTable,
       "ontpotsEntry": ontpotsEntry,
       "ontpotsCardPort": ontpotsCardPort,
       "ontpotsRowStatus": ontpotsRowStatus,
       "ontpotsAction": ontpotsAction,
       "ontVoipProfile": ontVoipProfile,
       "sipProfileTable": sipProfileTable,
       "sipProfileEntry": sipProfileEntry,
       "sipProfileName": sipProfileName,
       "sipProfileProxyServiceAddr": sipProfileProxyServiceAddr,
       "sipProfileOutProxyAddr": sipProfileOutProxyAddr,
       "sipProfilePriDns": sipProfilePriDns,
       "sipProfileSecDns": sipProfileSecDns,
       "sipProfileRegExpTime": sipProfileRegExpTime,
       "sipProfileReregHeadStartTime": sipProfileReregHeadStartTime,
       "sipProfileHostPartUri": sipProfileHostPartUri,
       "sipProfileRegistrar": sipProfileRegistrar,
       "sipProfileSoftSwitch": sipProfileSoftSwitch,
       "sipProfileCid": sipProfileCid,
       "sipProfileCallWait": sipProfileCallWait,
       "sipProfileCallProgTrans": sipProfileCallProgTrans,
       "sipProfileCallPresent": sipProfileCallPresent,
       "sipProfileDirectCon": sipProfileDirectCon,
       "sipProfileDirectConUri": sipProfileDirectConUri,
       "sipProfileBridgeLineAgentUri": sipProfileBridgeLineAgentUri,
       "sipProfileConfFactoryUri": sipProfileConfFactoryUri,
       "sipProfileRowStatus": sipProfileRowStatus,
       "commonProfileTable": commonProfileTable,
       "commonProfileEntry": commonProfileEntry,
       "commonProfileName": commonProfileName,
       "commonProfileLocalPortMin": commonProfileLocalPortMin,
       "commonProfileLocalPortMax": commonProfileLocalPortMax,
       "commonProfileDscpMark": commonProfileDscpMark,
       "commonProfilePiggyback": commonProfilePiggyback,
       "commonProfileTone": commonProfileTone,
       "commonProfileDtmf": commonProfileDtmf,
       "commonProfileCas": commonProfileCas,
       "commonProfileAnnounceType": commonProfileAnnounceType,
       "commonProfileJitterTarget": commonProfileJitterTarget,
       "commonProfileJitterBufMax": commonProfileJitterBufMax,
       "commonProfileEchoCancel": commonProfileEchoCancel,
       "commonProfilePstnProtocol": commonProfilePstnProtocol,
       "commonProfileFaxMode": commonProfileFaxMode,
       "commonProfile1stCodec": commonProfile1stCodec,
       "commonProfile2ndCodec": commonProfile2ndCodec,
       "commonProfile3rdCodec": commonProfile3rdCodec,
       "commonProfile4thCodec": commonProfile4thCodec,
       "commonProfile1stPacketPeriod": commonProfile1stPacketPeriod,
       "commonProfile2ndPacketPeriod": commonProfile2ndPacketPeriod,
       "commonProfile3rdPacketPeriod": commonProfile3rdPacketPeriod,
       "commonProfile4thPacketPeriod": commonProfile4thPacketPeriod,
       "commonProfile1stSilence": commonProfile1stSilence,
       "commonProfile2ndSilence": commonProfile2ndSilence,
       "commonProfile3rdSilence": commonProfile3rdSilence,
       "commonProfile4thSilence": commonProfile4thSilence,
       "commonProfileOobDtmf": commonProfileOobDtmf,
       "commonProfileRowStatus": commonProfileRowStatus,
       "commonProfileSignalCode": commonProfileSignalCode,
       "dialPlan": dialPlan,
       "dialPlanCommTable": dialPlanCommTable,
       "dialPlanCommEntry": dialPlanCommEntry,
       "dialPlanCommName": dialPlanCommName,
       "dialPlanCommMaxSize": dialPlanCommMaxSize,
       "dialPlanCommCriticalTimeout": dialPlanCommCriticalTimeout,
       "dialPlanCommPartialTimeout": dialPlanCommPartialTimeout,
       "dialPlanCommFormat": dialPlanCommFormat,
       "dialPlanCommRowStatus": dialPlanCommRowStatus,
       "dialPlanContTable": dialPlanContTable,
       "dialPlanContEntry": dialPlanContEntry,
       "dialPlanContName": dialPlanContName,
       "dialPlanContId": dialPlanContId,
       "dialPlanContToken": dialPlanContToken,
       "dialPlanContRowStatus": dialPlanContRowStatus,
       "ontvideoTable": ontvideoTable,
       "ontvideoEntry": ontvideoEntry,
       "ontvideoPort": ontvideoPort,
       "ontvideoRowStatus": ontvideoRowStatus,
       "ontvideoAction": ontvideoAction,
       "onuVendorVersion": onuVendorVersion,
       "onuVendorVersionTable": onuVendorVersionTable,
       "onuVendorVersionEntry": onuVendorVersionEntry,
       "onuVendorVersionName": onuVendorVersionName,
       "onuVendorVersionSoftwareVer": onuVendorVersionSoftwareVer,
       "onuVendorVersionModelName": onuVendorVersionModelName,
       "onuVendorVersionModelID": onuVendorVersionModelID,
       "onuVendorVersionCard1": onuVendorVersionCard1,
       "onuVendorVersionCard2": onuVendorVersionCard2,
       "onuVendorVersionCard3": onuVendorVersionCard3,
       "onuVendorVersionCard4": onuVendorVersionCard4,
       "onuVendorVersionCard5": onuVendorVersionCard5,
       "onuVendorVersionRowStatus": onuVendorVersionRowStatus,
       "ontPmRateTable": ontPmRateTable,
       "ontPmRateEntry": ontPmRateEntry,
       "ontPmRateDot1dBasePort": ontPmRateDot1dBasePort,
       "ontPmRateOnt": ontPmRateOnt,
       "ontPmRateMonitor": ontPmRateMonitor,
       "ontPmRateIndex": ontPmRateIndex,
       "ontAclProfileTable": ontAclProfileTable,
       "ontAclProfileEntry": ontAclProfileEntry,
       "ontAclProfileName": ontAclProfileName,
       "ontAclProfileEnable": ontAclProfileEnable,
       "ontAclProfilePolicy": ontAclProfilePolicy,
       "ontAclProfileInterface": ontAclProfileInterface,
       "ontAclProfileIpProtocol": ontAclProfileIpProtocol,
       "ontAclProfileSourceL4Port": ontAclProfileSourceL4Port,
       "ontAclProfileDestinationL4Port": ontAclProfileDestinationL4Port,
       "ontAclProfileSourceIpAddress": ontAclProfileSourceIpAddress,
       "ontAclProfileSourceIpMask": ontAclProfileSourceIpMask,
       "ontAclProfileDestinationIpAddress": ontAclProfileDestinationIpAddress,
       "ontAclProfileDestinationIpMask": ontAclProfileDestinationIpMask,
       "ontAclProfileSourceMacAddress": ontAclProfileSourceMacAddress,
       "ontAclProfileDestinationMacAddress": ontAclProfileDestinationMacAddress,
       "ontAclProfileRowStatus": ontAclProfileRowStatus,
       "remoteOntInfo": remoteOntInfo,
       "ponStatusTable": ponStatusTable,
       "ponStatusEntry": ponStatusEntry,
       "state": state,
       "oltKeyExchange": oltKeyExchange,
       "snAcq": snAcq,
       "rogueDectect": rogueDectect,
       "rogueDestructState": rogueDestructState,
       "procInterval": procInterval,
       "procIntervalSec": procIntervalSec,
       "los": los,
       "last": last,
       "endOfBurstOffset": endOfBurstOffset,
       "ontStatusTable": ontStatusTable,
       "ontCurrentStatusTable": ontCurrentStatusTable,
       "ontCurrentStatusEntry": ontCurrentStatusEntry,
       "serialNumber": serialNumber,
       "passwordOnt": passwordOnt,
       "ontStatus": ontStatus,
       "versionA": versionA,
       "versionB": versionB,
       "actVersion": actVersion,
       "estimatedDistance": estimatedDistance,
       "pppoeStatus": pppoeStatus,
       "onuVersion": onuVersion,
       "wanIp": wanIp,
       "ontStatusElapsedTime": ontStatusElapsedTime,
       "onuModelName": onuModelName,
       "onuModelId": onuModelId,
       "upgradeStatus": upgradeStatus,
       "ontCountersTable": ontCountersTable,
       "ontCountersEntry": ontCountersEntry,
       "ontCountersUnreceivedBursts": ontCountersUnreceivedBursts,
       "ontCountersPositiveDriftBits": ontCountersPositiveDriftBits,
       "ontCountersNegativeDriftBits": ontCountersNegativeDriftBits,
       "ontCountersBip8Errors": ontCountersBip8Errors,
       "ontCountersCorrectedBytes": ontCountersCorrectedBytes,
       "ontCountersCorrectedCodewords": ontCountersCorrectedCodewords,
       "ontCountersUncorrctableCodewords": ontCountersUncorrctableCodewords,
       "ontCountersTotalReceivedCodewords": ontCountersTotalReceivedCodewords,
       "ontCountersDsBer": ontCountersDsBer,
       "ontBwGroupStatusTable": ontBwGroupStatusTable,
       "ontBwGroupStatusEntry": ontBwGroupStatusEntry,
       "ontBwGroupStatusAllocId": ontBwGroupStatusAllocId,
       "ontBwGroupStatusCurrUsDataRate": ontBwGroupStatusCurrUsDataRate,
       "ontWanStatusTable": ontWanStatusTable,
       "ontWanStatusEntry": ontWanStatusEntry,
       "ontWanId": ontWanId,
       "ontWanStatusEnable": ontWanStatusEnable,
       "ontWanStatusType": ontWanStatusType,
       "ontWanStatusLinkStatus": ontWanStatusLinkStatus,
       "ontWanStatusServiceType": ontWanStatusServiceType,
       "ontWanStatusVlan": ontWanStatusVlan,
       "ontWanStatusPriority": ontWanStatusPriority,
       "ontWanStatusIpMode": ontWanStatusIpMode,
       "ontWanStatusIp": ontWanStatusIp,
       "ontWanStatusMask": ontWanStatusMask,
       "ontWanStatusGateway": ontWanStatusGateway,
       "ontWanStatusPrimaryDns": ontWanStatusPrimaryDns,
       "ontWanStatusSecondDns": ontWanStatusSecondDns,
       "ontWanStatusNat": ontWanStatusNat,
       "ontWanStatusGetState": ontWanStatusGetState,
       "ontStatusHistTable": ontStatusHistTable,
       "ontStatusHistEntry": ontStatusHistEntry,
       "ontStatusHistIdx": ontStatusHistIdx,
       "ontStatusHistStatus": ontStatusHistStatus,
       "ontStatusHistYear": ontStatusHistYear,
       "ontStatusHistMonth": ontStatusHistMonth,
       "ontStatusHistDay": ontStatusHistDay,
       "ontStatusHistHour": ontStatusHistHour,
       "ontStatusHistMin": ontStatusHistMin,
       "ontStatusHistSec": ontStatusHistSec,
       "ontStormingStatusTable": ontStormingStatusTable,
       "ontStormingStatusEntry": ontStormingStatusEntry,
       "ontStormingBcastOverThr": ontStormingBcastOverThr,
       "ontStormingMcastOverThr": ontStormingMcastOverThr,
       "ontStormingUnknowOverThr": ontStormingUnknowOverThr,
       "ontStormingDdosArpDetect": ontStormingDdosArpDetect,
       "ontStormingDdosTcpDetect": ontStormingDdosTcpDetect,
       "ontStormingDdosUdpDetect": ontStormingDdosUdpDetect,
       "ontStormingLoopguardDetect": ontStormingLoopguardDetect,
       "ontAclServiceStatusTable": ontAclServiceStatusTable,
       "ontAclServiceStatusEntry": ontAclServiceStatusEntry,
       "ontAclServiceStatusState": ontAclServiceStatusState,
       "ontAclServiceStatusProfileName": ontAclServiceStatusProfileName,
       "ontCardStatusTable": ontCardStatusTable,
       "ontCardStatusEntry": ontCardStatusEntry,
       "status": status,
       "adminState": adminState,
       "expectType": expectType,
       "actualType": actualType,
       "expectedPort": expectedPort,
       "actualPort": actualPort,
       "ontDdmiStatusTable": ontDdmiStatusTable,
       "ontDdmiStatusEntry": ontDdmiStatusEntry,
       "voltage": voltage,
       "rxPower": rxPower,
       "txPower": txPower,
       "laserCurrent": laserCurrent,
       "ontTemperature": ontTemperature,
       "ontDdmiRowStatus": ontDdmiRowStatus,
       "ontDdmiStatus": ontDdmiStatus,
       "ontEnetPmCounters": ontEnetPmCounters,
       "ontEnetCurrentPmCountersTable": ontEnetCurrentPmCountersTable,
       "ontEnetCurrentPmCountersEntry": ontEnetCurrentPmCountersEntry,
       "ontEnetCurrentPmUsOctets": ontEnetCurrentPmUsOctets,
       "ontEnetCurrentPmUsPackets": ontEnetCurrentPmUsPackets,
       "ontEnetCurrentPmUsMcastPackets": ontEnetCurrentPmUsMcastPackets,
       "ontEnetCurrentPmUsBcastPackets": ontEnetCurrentPmUsBcastPackets,
       "ontEnetCurrentPmDsOctets": ontEnetCurrentPmDsOctets,
       "ontEnetCurrentPmDsPackets": ontEnetCurrentPmDsPackets,
       "ontEnetCurrentPmDsMcastPackets": ontEnetCurrentPmDsMcastPackets,
       "ontEnetCurrentPmDsBcastPackets": ontEnetCurrentPmDsBcastPackets,
       "ontEnetPmCountersGetCurrent": ontEnetPmCountersGetCurrent,
       "ontEnetPmCountersCheckGetCurrent": ontEnetPmCountersCheckGetCurrent,
       "ontEnetLast15PmCountersTable": ontEnetLast15PmCountersTable,
       "ontEnetLast15PmCountersEntry": ontEnetLast15PmCountersEntry,
       "ontEnetLast15PmUsOctets": ontEnetLast15PmUsOctets,
       "ontEnetLast15PmUsPackets": ontEnetLast15PmUsPackets,
       "ontEnetLast15PmUsMcastPackets": ontEnetLast15PmUsMcastPackets,
       "ontEnetLast15PmUsBcastPackets": ontEnetLast15PmUsBcastPackets,
       "ontEnetLast15PmDsOctets": ontEnetLast15PmDsOctets,
       "ontEnetLast15PmDsPackets": ontEnetLast15PmDsPackets,
       "ontEnetLast15PmDsMcastPackets": ontEnetLast15PmDsMcastPackets,
       "ontEnetLast15PmDsBcastPackets": ontEnetLast15PmDsBcastPackets,
       "ontEnetLast15PmInterval": ontEnetLast15PmInterval,
       "ontEnetStatus": ontEnetStatus,
       "ontEnetStatusTable": ontEnetStatusTable,
       "ontEnetStatusEntry": ontEnetStatusEntry,
       "ontEnetPortStatus": ontEnetPortStatus,
       "ontVenetPmCounters": ontVenetPmCounters,
       "ontVenetCurrentPmCountersTable": ontVenetCurrentPmCountersTable,
       "ontVenetCurrentPmCountersEntry": ontVenetCurrentPmCountersEntry,
       "ontVenetCurrentPmUsOctets": ontVenetCurrentPmUsOctets,
       "ontVenetCurrentPmUsPackets": ontVenetCurrentPmUsPackets,
       "ontVenetCurrentPmUsMcastPackets": ontVenetCurrentPmUsMcastPackets,
       "ontVenetCurrentPmUsBcastPackets": ontVenetCurrentPmUsBcastPackets,
       "ontVenetCurrentPmDsOctets": ontVenetCurrentPmDsOctets,
       "ontVenetCurrentPmDsPackets": ontVenetCurrentPmDsPackets,
       "ontVenetCurrentPmDsMcastPackets": ontVenetCurrentPmDsMcastPackets,
       "ontVenetCurrentPmDsBcastPackets": ontVenetCurrentPmDsBcastPackets,
       "ontVenetPmCountersGetCurrent": ontVenetPmCountersGetCurrent,
       "ontVenetPmCountersCheckGetCurrent": ontVenetPmCountersCheckGetCurrent,
       "ontVenetLast15PmCountersTable": ontVenetLast15PmCountersTable,
       "ontVenetLast15PmCountersEntry": ontVenetLast15PmCountersEntry,
       "ontVenetLast15PmUsOctets": ontVenetLast15PmUsOctets,
       "ontVenetLast15PmUsPackets": ontVenetLast15PmUsPackets,
       "ontVenetLast15PmUsMcastPackets": ontVenetLast15PmUsMcastPackets,
       "ontVenetLast15PmUsBcastPackets": ontVenetLast15PmUsBcastPackets,
       "ontVenetLast15PmDsOctets": ontVenetLast15PmDsOctets,
       "ontVenetLast15PmDsPackets": ontVenetLast15PmDsPackets,
       "ontVenetLast15PmDsMcastPackets": ontVenetLast15PmDsMcastPackets,
       "ontVenetLast15PmDsBcastPackets": ontVenetLast15PmDsBcastPackets,
       "ontVenetLast15PmInterval": ontVenetLast15PmInterval,
       "ontVenetStatusInfo": ontVenetStatusInfo,
       "ontVenetStatusTable": ontVenetStatusTable,
       "ontVenetStatusEntry": ontVenetStatusEntry,
       "ontVenetStatus": ontVenetStatus,
       "ontPotsStatusInfo": ontPotsStatusInfo,
       "ontPotsStatusTable": ontPotsStatusTable,
       "ontPotsStatusEntry": ontPotsStatusEntry,
       "ontPotsStatus": ontPotsStatus,
       "ontUniportStatusInfo": ontUniportStatusInfo,
       "uniportVlanStatusTable": uniportVlanStatusTable,
       "uniportVlanStatusEntry": uniportVlanStatusEntry,
       "uniportVlanStatus": uniportVlanStatus,
       "ontVideoStatus": ontVideoStatus,
       "ontVideoStatusTable": ontVideoStatusTable,
       "ontVideoStatusEntry": ontVideoStatusEntry,
       "ontVideoPortStatus": ontVideoPortStatus,
       "ontDdmiHistoryTable": ontDdmiHistoryTable,
       "ontDdmiHistoryEntry": ontDdmiHistoryEntry,
       "ontDdmiHistoryVoltage15M": ontDdmiHistoryVoltage15M,
       "ontDdmiHistoryRxPower15M": ontDdmiHistoryRxPower15M,
       "ontDdmiHistoryTxPower15M": ontDdmiHistoryTxPower15M,
       "ontDdmiHistoryLaserCurrent15M": ontDdmiHistoryLaserCurrent15M,
       "ontDdmiHistoryTemperature15M": ontDdmiHistoryTemperature15M,
       "ontDdmiHistoryUpdateTime15M": ontDdmiHistoryUpdateTime15M,
       "ontDdmiLatest15MTable": ontDdmiLatest15MTable,
       "ontDdmiLatest15MEntry": ontDdmiLatest15MEntry,
       "ontDdmiLatest15MVoltage": ontDdmiLatest15MVoltage,
       "ontDdmiLatest15MRxPower": ontDdmiLatest15MRxPower,
       "ontDdmiLatest15MTxPower": ontDdmiLatest15MTxPower,
       "ontDdmiLatest15MLaserCurrent": ontDdmiLatest15MLaserCurrent,
       "ontDdmiLatest15MTemperature": ontDdmiLatest15MTemperature,
       "ontPmRateIntervalTable": ontPmRateIntervalTable,
       "ontPmRateIntervalEntry": ontPmRateIntervalEntry,
       "ontPmRateIntervalTime": ontPmRateIntervalTime,
       "ontPmRateIntervalUsRate": ontPmRateIntervalUsRate,
       "ontPmRateIntervalDsRate": ontPmRateIntervalDsRate,
       "antiSpoofSetup": antiSpoofSetup,
       "antiSpoofState": antiSpoofState,
       "antiSpoofPortTable": antiSpoofPortTable,
       "antiSpoofPortEntry": antiSpoofPortEntry,
       "antiSpoofActiveByPort": antiSpoofActiveByPort,
       "antiSpoofTable": antiSpoofTable,
       "antiSpoofEntry": antiSpoofEntry,
       "antiSpoofPort": antiSpoofPort,
       "antiSpoofMode": antiSpoofMode,
       "antiSpoofSetting": antiSpoofSetting,
       "antiSpoofRowStatus": antiSpoofRowStatus,
       "multicastChannelSetup": multicastChannelSetup,
       "multicastChannelTable": multicastChannelTable,
       "multicastChannelEntry": multicastChannelEntry,
       "multicastChannelStartIp": multicastChannelStartIp,
       "multicastChannelEndIp": multicastChannelEndIp,
       "multicastChannelSvid": multicastChannelSvid,
       "multicastChannelCvid": multicastChannelCvid,
       "multicastChannelPbit": multicastChannelPbit,
       "multicastChannelSrcIp": multicastChannelSrcIp,
       "multicastChannelPkgMember": multicastChannelPkgMember,
       "multicastChannelPreviewDuration": multicastChannelPreviewDuration,
       "multicastChannelPreviewCount": multicastChannelPreviewCount,
       "multicastChannelPreviewBlackout": multicastChannelPreviewBlackout,
       "multicastChannelRowStatus": multicastChannelRowStatus,
       "multicastChannelCacProf": multicastChannelCacProf,
       "ponSetup": ponSetup,
       "ponTable": ponTable,
       "ponSetupTable": ponSetupTable,
       "ponSetupEntry": ponSetupEntry,
       "transceiverTxDisable": transceiverTxDisable,
       "inO7State": inO7State,
       "outO7State": outO7State,
       "linkState": linkState,
       "availableBandwidth": availableBandwidth,
       "delimiterDetected": delimiterDetected,
       "ponConfigTable": ponConfigTable,
       "ponConfigEntry": ponConfigEntry,
       "transceiverType": transceiverType,
       "registerMethod": registerMethod,
       "ponConfigRowStatus": ponConfigRowStatus,
       "templateOption": templateOption,
       "ontTemplate": ontTemplate,
       "fecMode": fecMode,
       "rangingDistance": rangingDistance,
       "bipErrThres": bipErrThres,
       "fecCorrByteThres": fecCorrByteThres,
       "fecCorrCodeWordThres": fecCorrCodeWordThres,
       "fecUncorrCodeWordThres": fecUncorrCodeWordThres,
       "reiCounterThres": reiCounterThres,
       "tcaStatus": tcaStatus,
       "unregisterOntTable": unregisterOntTable,
       "unregisterOntEntry": unregisterOntEntry,
       "unregisterOntSerialNumber": unregisterOntSerialNumber,
       "unregisterOntPassword": unregisterOntPassword,
       "unregisterOntStatus": unregisterOntStatus,
       "unregisterOntIndex": unregisterOntIndex,
       "ponProtectionTable": ponProtectionTable,
       "ponProtectionEntry": ponProtectionEntry,
       "protectionPort": protectionPort,
       "ponProtectConfigRowStatus": ponProtectConfigRowStatus,
       "ponRogueOnuTable": ponRogueOnuTable,
       "ponRogueOnuEntry": ponRogueOnuEntry,
       "rogueDetect": rogueDetect,
       "ontFwUpgrade": ontFwUpgrade,
       "ontFwUpgradeSetup": ontFwUpgradeSetup,
       "ontImageVersion": ontImageVersion,
       "releaseOntImage": releaseOntImage,
       "autoReboot": autoReboot,
       "ontFwUpgradeAction": ontFwUpgradeAction,
       "checkOntFwPerPon": checkOntFwPerPon,
       "ontFwUpgradeClearStatusPerPon": ontFwUpgradeClearStatusPerPon,
       "ontFwUpgradeClearQueuePerPon": ontFwUpgradeClearQueuePerPon,
       "ontFwUpgradeInfo": ontFwUpgradeInfo,
       "numOfOntInQueue": numOfOntInQueue,
       "portBridgeSetup": portBridgeSetup,
       "portBridgeState": portBridgeState,
       "portBridgePortTable": portBridgePortTable,
       "portBridgePortEntry": portBridgePortEntry,
       "portBridgePortState": portBridgePortState,
       "cdr": cdr,
       "cdrIgmp": cdrIgmp,
       "cdrIgmpSetup": cdrIgmpSetup,
       "cdrIgmpActive": cdrIgmpActive,
       "cdrIgmpLogSize": cdrIgmpLogSize,
       "cdrIgmpStatus": cdrIgmpStatus,
       "cdrIgmpStatusTable": cdrIgmpStatusTable,
       "cdrIgmpStatusEntry": cdrIgmpStatusEntry,
       "cdrIgmpStatusEntryIndex": cdrIgmpStatusEntryIndex,
       "cdrIgmpEventTime": cdrIgmpEventTime,
       "cdrIgmpEventType": cdrIgmpEventType,
       "cdrIgmpGroup": cdrIgmpGroup,
       "cdrIgmpPrivilege": cdrIgmpPrivilege,
       "cdrIgmpUptime": cdrIgmpUptime,
       "cdrIgmpChannel": cdrIgmpChannel,
       "classifierSetup": classifierSetup,
       "classifierRuleTable": classifierRuleTable,
       "classifierRuleEntry": classifierRuleEntry,
       "classifierName": classifierName,
       "classifierEnable": classifierEnable,
       "classifierPacketFormat": classifierPacketFormat,
       "classifierVlanId": classifierVlanId,
       "classifier8021pPriority": classifier8021pPriority,
       "classifierEtherType": classifierEtherType,
       "classifierSrcMAC": classifierSrcMAC,
       "classifierIncomingPort": classifierIncomingPort,
       "classifierDstMAC": classifierDstMAC,
       "classifierDSCP": classifierDSCP,
       "classifierIpProtocol": classifierIpProtocol,
       "classifierEstablishOnly": classifierEstablishOnly,
       "classifierSrcIp": classifierSrcIp,
       "classifierSrcIpMask": classifierSrcIpMask,
       "classifierSrcSocket": classifierSrcSocket,
       "classifierDstIp": classifierDstIp,
       "classifierDstIpMask": classifierDstIpMask,
       "classifierDstSocket": classifierDstSocket,
       "classifierRowstatus": classifierRowstatus,
       "classifierIp6Dscp": classifierIp6Dscp,
       "classifierIp6NextHeader": classifierIp6NextHeader,
       "classifierIp6EstbOnly": classifierIp6EstbOnly,
       "classifierSrcIp6": classifierSrcIp6,
       "classifierSrcIp6PrefixLen": classifierSrcIp6PrefixLen,
       "classifierDstIp6": classifierDstIp6,
       "classifierDstIp6PrefixLen": classifierDstIp6PrefixLen,
       "classifierOutgoingPort": classifierOutgoingPort,
       "classifierRuleSet": classifierRuleSet,
       "policySetup": policySetup,
       "policyTable": policyTable,
       "policyEntry": policyEntry,
       "policyName": policyName,
       "policyEnable": policyEnable,
       "policyClassifier": policyClassifier,
       "policyVlanId": policyVlanId,
       "policyEgressPort": policyEgressPort,
       "policyOutPktFormat": policyOutPktFormat,
       "policy8021pPriority": policy8021pPriority,
       "policyDSCP": policyDSCP,
       "policyTOS": policyTOS,
       "policySir": policySir,
       "policyPir": policyPir,
       "policyOutOfProfileDSCP": policyOutOfProfileDSCP,
       "policyOutOfProfileGpCosqNew": policyOutOfProfileGpCosqNew,
       "policyForwardingAction": policyForwardingAction,
       "policyPriorityAction": policyPriorityAction,
       "policyDiffServAction": policyDiffServAction,
       "policyOutgoingAction": policyOutgoingAction,
       "policyMeteringEnable": policyMeteringEnable,
       "policyOutOfProfileAction": policyOutOfProfileAction,
       "policyRowstatus": policyRowstatus,
       "policyMirrorPort": policyMirrorPort,
       "policyRuleSet": policyRuleSet,
       "uniPortOpModeSetup": uniPortOpModeSetup,
       "uniPortOpModePortTable": uniPortOpModePortTable,
       "uniPortOpModePortEntry": uniPortOpModePortEntry,
       "uniPortOpModePortVlanTranslation": uniPortOpModePortVlanTranslation,
       "uniPortOpModePortVlanXlateMissDrop": uniPortOpModePortVlanXlateMissDrop,
       "uniPortOpModePortEgrVlanXlateMissDrop": uniPortOpModePortEgrVlanXlateMissDrop,
       "macInfo": macInfo,
       "macTable": macTable,
       "macEntry": macEntry,
       "macVid": macVid,
       "macMacAddr": macMacAddr,
       "macPort": macPort,
       "macType": macType,
       "macUniportAid": macUniportAid,
       "macGemflow": macGemflow,
       "antiMacSpoofSetup": antiMacSpoofSetup,
       "antiMacSpoofState": antiMacSpoofState,
       "antiMacSpoofPortTable": antiMacSpoofPortTable,
       "antiMacSpoofPortEntry": antiMacSpoofPortEntry,
       "antiMacSpoofPortState": antiMacSpoofPortState,
       "protectSwitch": protectSwitch,
       "protectSwitchMsc": protectSwitchMsc,
       "protectSwitchPon": protectSwitchPon,
       "protectSwitchPonTable": protectSwitchPonTable,
       "protectSwitchPonEntry": protectSwitchPonEntry,
       "passivePort": passivePort,
       "currWorkingPort": currWorkingPort,
       "currStandbyPort": currStandbyPort,
       "delimiterDetectedOnStandbyPort": delimiterDetectedOnStandbyPort,
       "lastSwitchOverReason": lastSwitchOverReason,
       "lastSwitchOverTimeStampYear": lastSwitchOverTimeStampYear,
       "lastSwitchOverTimeStampMonth": lastSwitchOverTimeStampMonth,
       "lastSwitchOverTimeStampDay": lastSwitchOverTimeStampDay,
       "lastSwitchOverTimeStampHour": lastSwitchOverTimeStampHour,
       "lastSwitchOverTimeStampMinute": lastSwitchOverTimeStampMinute,
       "lastSwitchOverTimeStampSecond": lastSwitchOverTimeStampSecond,
       "switchOverTimes": switchOverTimes,
       "triggerSwitchOver": triggerSwitchOver,
       "protectSwitchPonRowstatus": protectSwitchPonRowstatus,
       "rateThresholdSetup": rateThresholdSetup,
       "rateThresholdPortTable": rateThresholdPortTable,
       "rateThresholdPortEntry": rateThresholdPortEntry,
       "rateThresholdPortIngress": rateThresholdPortIngress,
       "rateThresholdPortEgress": rateThresholdPortEgress,
       "rateUsagePercentageIngress": rateUsagePercentageIngress,
       "rateUsagePercentageEgress": rateUsagePercentageEgress,
       "rateUsageKbpsIngress": rateUsageKbpsIngress,
       "rateUsageKbpsEgress": rateUsageKbpsEgress,
       "erpsSetup": erpsSetup,
       "erpsState": erpsState,
       "erpsRingTable": erpsRingTable,
       "erpsRingEntry": erpsRingEntry,
       "erpsPort0": erpsPort0,
       "erpsPort1": erpsPort1,
       "erpsRingId": erpsRingId,
       "erpsCcmPort0GroupName": erpsCcmPort0GroupName,
       "erpsCcmPort0Level": erpsCcmPort0Level,
       "erpsCcmPort0Vlan": erpsCcmPort0Vlan,
       "erpsCcmPort0TxName": erpsCcmPort0TxName,
       "erpsCcmPort0Period": erpsCcmPort0Period,
       "erpsCcmPort0Priority": erpsCcmPort0Priority,
       "erpsCcmPort0IntPriority": erpsCcmPort0IntPriority,
       "erpsCcmPort0RxName": erpsCcmPort0RxName,
       "erpsCcmPort1GroupName": erpsCcmPort1GroupName,
       "erpsCcmPort1Level": erpsCcmPort1Level,
       "erpsCcmPort1Vlan": erpsCcmPort1Vlan,
       "erpsCcmPort1TxName": erpsCcmPort1TxName,
       "erpsCcmPort1Period": erpsCcmPort1Period,
       "erpsCcmPort1Priority": erpsCcmPort1Priority,
       "erpsCcmPort1IntPriority": erpsCcmPort1IntPriority,
       "erpsCcmPort1RxName": erpsCcmPort1RxName,
       "erpsRapsPort0Vlan": erpsRapsPort0Vlan,
       "erpsRapsPort0priority": erpsRapsPort0priority,
       "erpsRapsPort0Level": erpsRapsPort0Level,
       "erpsRapsPort1Vlan": erpsRapsPort1Vlan,
       "erpsRapsPort1priority": erpsRapsPort1priority,
       "erpsRapsPort1Level": erpsRapsPort1Level,
       "erpsRevertiveMode": erpsRevertiveMode,
       "erpsWtr": erpsWtr,
       "erpsRplOwner": erpsRplOwner,
       "erpsRplNeighbour": erpsRplNeighbour,
       "erpsTunnelPort": erpsTunnelPort,
       "erpsRingRowStatus": erpsRingRowStatus,
       "erpsRingIndex": erpsRingIndex,
       "wred": wred,
       "wredState": wredState,
       "dhcpClientTest": dhcpClientTest,
       "dhcpClientTestTimeout": dhcpClientTestTimeout,
       "dhcpClientTestPortTable": dhcpClientTestPortTable,
       "dhcpClientTestPortEntry": dhcpClientTestPortEntry,
       "dhcpClientTestPortState": dhcpClientTestPortState,
       "dhcpClientTestPortIp": dhcpClientTestPortIp,
       "dhcpClientTestPortOptNniSvid": dhcpClientTestPortOptNniSvid,
       "dhcpClientTestPortOptSnicvid": dhcpClientTestPortOptSnicvid,
       "dhcpClientTestPortOptOntid": dhcpClientTestPortOptOntid,
       "dhcpClientTestPortOptOntcardid": dhcpClientTestPortOptOntcardid,
       "dhcpClientTestPortOptUniport": dhcpClientTestPortOptUniport,
       "dhcpClientTestPortOptOntsn": dhcpClientTestPortOptOntsn,
       "dhcpClientTestPortStartSniSvid": dhcpClientTestPortStartSniSvid,
       "dhcpClientTestPortStopSniSvid": dhcpClientTestPortStopSniSvid,
       "sysTimeRef": sysTimeRef,
       "sysTimeRefPTPState": sysTimeRefPTPState,
       "dhcpL2Agent": dhcpL2Agent,
       "dhcpL2AgentTable": dhcpL2AgentTable,
       "dhcpL2AgentEntry": dhcpL2AgentEntry,
       "dhcpL2AgentVid": dhcpL2AgentVid,
       "dhcpL2AgentEnable": dhcpL2AgentEnable,
       "dhcpL2AgentOpt82CircuitIdInfo": dhcpL2AgentOpt82CircuitIdInfo,
       "dhcpL2AgentOpt82RemoteIdInfo": dhcpL2AgentOpt82RemoteIdInfo,
       "dhcpL2AgentRowStatus": dhcpL2AgentRowStatus,
       "dhcpL2AgentOpt18InterfaceIdInfo": dhcpL2AgentOpt18InterfaceIdInfo,
       "dhcpL2AgentOpt37RemoteIdInfo": dhcpL2AgentOpt37RemoteIdInfo,
       "dhcpL2AgentLDRAEnable": dhcpL2AgentLDRAEnable}
)
