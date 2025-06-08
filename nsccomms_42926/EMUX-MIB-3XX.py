# SNMP MIB module (EMUX-MIB-3XX) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nsccomms_42926/EMUX-MIB-3XX.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:13:34 2025
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(TimeFilter,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nsc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18)
)
if mibBuilder.loadTexts:
    nsc.setRevisions(
        ("2011-02-18 00:00",
         "2011-02-17 00:03",
         "2011-02-17 00:02",
         "2011-02-17 00:01")
    )


# Types definitions



class SnmpAdminString(OctetString):
    """Custom type SnmpAdminString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )




# TEXTUAL-CONVENTIONS



class LldpChassisIdSubtype(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("chassisComponent", 1),
          ("interfaceAlias", 2),
          ("portComponent", 3),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("interfaceName", 6),
          ("local", 7))
    )



class LldpChassisId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class LldpPortIdSubtype(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            7
        )
    )
    namedValues = NamedValues(
        ("local", 7)
    )



class LldpPortId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class LldpManAddrIfSubtype(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ifIndex", 2),
          ("systemPortNumber", 3))
    )



class LldpManAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class LldpPortNumber(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )



class LldpPortList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )



# MIB Managed Objects in the order of their OIDs

_Emux_ObjectIdentity = ObjectIdentity
emux = _Emux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2)
)
_Muxgeneral_ObjectIdentity = ObjectIdentity
muxgeneral = _Muxgeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 1)
)
_BasicInfo_ObjectIdentity = ObjectIdentity
basicInfo = _BasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 1)
)
_HardwareVersion_Type = DisplayString
_HardwareVersion_Object = MibScalar
hardwareVersion = _HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 1, 1),
    _HardwareVersion_Type()
)
hardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareVersion.setStatus("current")
_FwVersion_Type = DisplayString
_FwVersion_Object = MibScalar
fwVersion = _FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 1, 2),
    _FwVersion_Type()
)
fwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVersion.setStatus("current")
_SoftwareVersion_Type = DisplayString
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 1, 3),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("current")
_BootloaderVersion_Type = DisplayString
_BootloaderVersion_Object = MibScalar
bootloaderVersion = _BootloaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 1, 4),
    _BootloaderVersion_Type()
)
bootloaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootloaderVersion.setStatus("current")
_SystemID_Type = DisplayString
_SystemID_Object = MibScalar
systemID = _SystemID_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 1, 7),
    _SystemID_Type()
)
systemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemID.setStatus("current")
_PowerVoltage_Type = DisplayString
_PowerVoltage_Object = MibScalar
powerVoltage = _PowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 1, 8),
    _PowerVoltage_Type()
)
powerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerVoltage.setStatus("current")
_CaseTemperature_Type = DisplayString
_CaseTemperature_Object = MibScalar
caseTemperature = _CaseTemperature_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 1, 9),
    _CaseTemperature_Type()
)
caseTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caseTemperature.setStatus("current")
_EnvVer_Type = DisplayString
_EnvVer_Object = MibScalar
envVer = _EnvVer_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 1, 10),
    _EnvVer_Type()
)
envVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envVer.setStatus("current")
_AccVoltage_Type = DisplayString
_AccVoltage_Object = MibScalar
accVoltage = _AccVoltage_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 1, 11),
    _AccVoltage_Type()
)
accVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVoltage.setStatus("current")
_CurrentConsumption_Type = DisplayString
_CurrentConsumption_Object = MibScalar
currentConsumption = _CurrentConsumption_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 1, 12),
    _CurrentConsumption_Type()
)
currentConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentConsumption.setStatus("current")
_MuxSensor_ObjectIdentity = ObjectIdentity
muxSensor = _MuxSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 1, 13)
)
_Sensor1_Type = DisplayString
_Sensor1_Object = MibScalar
sensor1 = _Sensor1_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 1, 13, 1),
    _Sensor1_Type()
)
sensor1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1.setStatus("current")
_Sensor2_Type = DisplayString
_Sensor2_Object = MibScalar
sensor2 = _Sensor2_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 1, 13, 2),
    _Sensor2_Type()
)
sensor2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor2.setStatus("current")
_Sensor3_Type = DisplayString
_Sensor3_Object = MibScalar
sensor3 = _Sensor3_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 1, 13, 3),
    _Sensor3_Type()
)
sensor3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor3.setStatus("current")
_MuxDateTime_ObjectIdentity = ObjectIdentity
muxDateTime = _MuxDateTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 2)
)
_MuxDate_Type = DisplayString
_MuxDate_Object = MibScalar
muxDate = _MuxDate_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 2, 1),
    _MuxDate_Type()
)
muxDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxDate.setStatus("current")
_MuxTime_Type = DisplayString
_MuxTime_Object = MibScalar
muxTime = _MuxTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 2, 2),
    _MuxTime_Type()
)
muxTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxTime.setStatus("current")
_MuxTimeZone_Type = Integer32
_MuxTimeZone_Object = MibScalar
muxTimeZone = _MuxTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 2, 3),
    _MuxTimeZone_Type()
)
muxTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxTimeZone.setStatus("current")
_MuxTimeServer_Type = OctetString
_MuxTimeServer_Object = MibScalar
muxTimeServer = _MuxTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 2, 4),
    _MuxTimeServer_Type()
)
muxTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxTimeServer.setStatus("current")
_MuxTimeSynchro_Type = Integer32
_MuxTimeSynchro_Object = MibScalar
muxTimeSynchro = _MuxTimeSynchro_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 2, 5),
    _MuxTimeSynchro_Type()
)
muxTimeSynchro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxTimeSynchro.setStatus("current")
_MuxTimeNextSynchro_Type = DisplayString
_MuxTimeNextSynchro_Object = MibScalar
muxTimeNextSynchro = _MuxTimeNextSynchro_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 2, 6),
    _MuxTimeNextSynchro_Type()
)
muxTimeNextSynchro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxTimeNextSynchro.setStatus("current")
_MuxTimeSynchroPeriod_Type = Integer32
_MuxTimeSynchroPeriod_Object = MibScalar
muxTimeSynchroPeriod = _MuxTimeSynchroPeriod_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 2, 8),
    _MuxTimeSynchroPeriod_Type()
)
muxTimeSynchroPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxTimeSynchroPeriod.setStatus("current")
_MuxIP_ObjectIdentity = ObjectIdentity
muxIP = _MuxIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 3)
)
_MuxMAC_Type = OctetString
_MuxMAC_Object = MibScalar
muxMAC = _MuxMAC_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 3, 1),
    _MuxMAC_Type()
)
muxMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxMAC.setStatus("current")
_MuxIPaddr_Type = OctetString
_MuxIPaddr_Object = MibScalar
muxIPaddr = _MuxIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 3, 2),
    _MuxIPaddr_Type()
)
muxIPaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxIPaddr.setStatus("current")
_MuxMask_Type = OctetString
_MuxMask_Object = MibScalar
muxMask = _MuxMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 3, 3),
    _MuxMask_Type()
)
muxMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxMask.setStatus("current")
_MuxGateway_Type = OctetString
_MuxGateway_Object = MibScalar
muxGateway = _MuxGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 3, 4),
    _MuxGateway_Type()
)
muxGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxGateway.setStatus("current")
_MuxVLAN_Type = Integer32
_MuxVLAN_Object = MibScalar
muxVLAN = _MuxVLAN_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 3, 5),
    _MuxVLAN_Type()
)
muxVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxVLAN.setStatus("current")
_MuxVLANPri_Type = Integer32
_MuxVLANPri_Object = MibScalar
muxVLANPri = _MuxVLANPri_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 3, 12),
    _MuxVLANPri_Type()
)
muxVLANPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxVLANPri.setStatus("current")
_MuxMan_ObjectIdentity = ObjectIdentity
muxMan = _MuxMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 4)
)
_MuxManagementLocal_Type = Integer32
_MuxManagementLocal_Object = MibScalar
muxManagementLocal = _MuxManagementLocal_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 4, 6),
    _MuxManagementLocal_Type()
)
muxManagementLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementLocal.setStatus("current")
_MuxManagementGlobal_Type = Integer32
_MuxManagementGlobal_Object = MibScalar
muxManagementGlobal = _MuxManagementGlobal_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 4, 7),
    _MuxManagementGlobal_Type()
)
muxManagementGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementGlobal.setStatus("current")


class _MuxTelnetAccess_Type(Integer32):
    """Custom type muxTelnetAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MuxTelnetAccess_Type.__name__ = "Integer32"
_MuxTelnetAccess_Object = MibScalar
muxTelnetAccess = _MuxTelnetAccess_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 4, 8),
    _MuxTelnetAccess_Type()
)
muxTelnetAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxTelnetAccess.setStatus("current")


class _MuxHTTPAccess_Type(Integer32):
    """Custom type muxHTTPAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MuxHTTPAccess_Type.__name__ = "Integer32"
_MuxHTTPAccess_Object = MibScalar
muxHTTPAccess = _MuxHTTPAccess_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 4, 10),
    _MuxHTTPAccess_Type()
)
muxHTTPAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxHTTPAccess.setStatus("current")
_MuxSNMP_ObjectIdentity = ObjectIdentity
muxSNMP = _MuxSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 4, 11)
)


class _MuxSNMPAccess_Type(Integer32):
    """Custom type muxSNMPAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MuxSNMPAccess_Type.__name__ = "Integer32"
_MuxSNMPAccess_Object = MibScalar
muxSNMPAccess = _MuxSNMPAccess_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 4, 11, 1),
    _MuxSNMPAccess_Type()
)
muxSNMPAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxSNMPAccess.setStatus("current")


class _MuxFTPAccess_Type(Integer32):
    """Custom type muxFTPAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MuxFTPAccess_Type.__name__ = "Integer32"
_MuxFTPAccess_Object = MibScalar
muxFTPAccess = _MuxFTPAccess_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 4, 12),
    _MuxFTPAccess_Type()
)
muxFTPAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxFTPAccess.setStatus("current")


class _MuxMenuOnStart_Type(Integer32):
    """Custom type muxMenuOnStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MuxMenuOnStart_Type.__name__ = "Integer32"
_MuxMenuOnStart_Object = MibScalar
muxMenuOnStart = _MuxMenuOnStart_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 4, 13),
    _MuxMenuOnStart_Type()
)
muxMenuOnStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxMenuOnStart.setStatus("current")


class _MuxStoreCfg_Type(Integer32):
    """Custom type muxStoreCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MuxStoreCfg_Type.__name__ = "Integer32"
_MuxStoreCfg_Object = MibScalar
muxStoreCfg = _MuxStoreCfg_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 4, 14),
    _MuxStoreCfg_Type()
)
muxStoreCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxStoreCfg.setStatus("current")
_MuxRS_ObjectIdentity = ObjectIdentity
muxRS = _MuxRS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 5)
)
_MuxRSBaudRate_Type = Integer32
_MuxRSBaudRate_Object = MibScalar
muxRSBaudRate = _MuxRSBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 5, 1),
    _MuxRSBaudRate_Type()
)
muxRSBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxRSBaudRate.setStatus("current")


class _MuxRSStopBits_Type(Integer32):
    """Custom type muxRSStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("one", 0),
          ("two", 2),
          ("oneAndHalf", 5))
    )


_MuxRSStopBits_Type.__name__ = "Integer32"
_MuxRSStopBits_Object = MibScalar
muxRSStopBits = _MuxRSStopBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 5, 2),
    _MuxRSStopBits_Type()
)
muxRSStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxRSStopBits.setStatus("current")


class _MuxRSParity_Type(Integer32):
    """Custom type muxRSParity based on Integer32"""
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
          ("odd", 1),
          ("even", 2))
    )


_MuxRSParity_Type.__name__ = "Integer32"
_MuxRSParity_Object = MibScalar
muxRSParity = _MuxRSParity_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 5, 3),
    _MuxRSParity_Type()
)
muxRSParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxRSParity.setStatus("current")


class _MuxRSEnable_Type(Integer32):
    """Custom type muxRSEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MuxRSEnable_Type.__name__ = "Integer32"
_MuxRSEnable_Object = MibScalar
muxRSEnable = _MuxRSEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 5, 4),
    _MuxRSEnable_Type()
)
muxRSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxRSEnable.setStatus("current")
_MuxManIP_ObjectIdentity = ObjectIdentity
muxManIP = _MuxManIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7)
)
_MuxManagementIP1_Type = OctetString
_MuxManagementIP1_Object = MibScalar
muxManagementIP1 = _MuxManagementIP1_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 1),
    _MuxManagementIP1_Type()
)
muxManagementIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP1.setStatus("current")
_MuxManagementIP2_Type = OctetString
_MuxManagementIP2_Object = MibScalar
muxManagementIP2 = _MuxManagementIP2_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 2),
    _MuxManagementIP2_Type()
)
muxManagementIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP2.setStatus("current")
_MuxManagementIP3_Type = OctetString
_MuxManagementIP3_Object = MibScalar
muxManagementIP3 = _MuxManagementIP3_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 3),
    _MuxManagementIP3_Type()
)
muxManagementIP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP3.setStatus("current")
_MuxManagementIP4_Type = OctetString
_MuxManagementIP4_Object = MibScalar
muxManagementIP4 = _MuxManagementIP4_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 4),
    _MuxManagementIP4_Type()
)
muxManagementIP4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP4.setStatus("current")
_MuxManagementIP5_Type = OctetString
_MuxManagementIP5_Object = MibScalar
muxManagementIP5 = _MuxManagementIP5_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 5),
    _MuxManagementIP5_Type()
)
muxManagementIP5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP5.setStatus("current")
_MuxManagementIP6_Type = OctetString
_MuxManagementIP6_Object = MibScalar
muxManagementIP6 = _MuxManagementIP6_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 6),
    _MuxManagementIP6_Type()
)
muxManagementIP6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP6.setStatus("current")
_MuxManagementIP7_Type = OctetString
_MuxManagementIP7_Object = MibScalar
muxManagementIP7 = _MuxManagementIP7_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 7),
    _MuxManagementIP7_Type()
)
muxManagementIP7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP7.setStatus("current")
_MuxManagementIP8_Type = OctetString
_MuxManagementIP8_Object = MibScalar
muxManagementIP8 = _MuxManagementIP8_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 8),
    _MuxManagementIP8_Type()
)
muxManagementIP8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP8.setStatus("current")
_MuxManagementIP9_Type = OctetString
_MuxManagementIP9_Object = MibScalar
muxManagementIP9 = _MuxManagementIP9_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 9),
    _MuxManagementIP9_Type()
)
muxManagementIP9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP9.setStatus("current")
_MuxManagementIP10_Type = OctetString
_MuxManagementIP10_Object = MibScalar
muxManagementIP10 = _MuxManagementIP10_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 10),
    _MuxManagementIP10_Type()
)
muxManagementIP10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP10.setStatus("current")
_MuxManagementIP11_Type = OctetString
_MuxManagementIP11_Object = MibScalar
muxManagementIP11 = _MuxManagementIP11_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 11),
    _MuxManagementIP11_Type()
)
muxManagementIP11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP11.setStatus("current")
_MuxManagementIP12_Type = OctetString
_MuxManagementIP12_Object = MibScalar
muxManagementIP12 = _MuxManagementIP12_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 12),
    _MuxManagementIP12_Type()
)
muxManagementIP12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP12.setStatus("current")
_MuxManagementIP13_Type = OctetString
_MuxManagementIP13_Object = MibScalar
muxManagementIP13 = _MuxManagementIP13_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 13),
    _MuxManagementIP13_Type()
)
muxManagementIP13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP13.setStatus("current")
_MuxManagementIP14_Type = OctetString
_MuxManagementIP14_Object = MibScalar
muxManagementIP14 = _MuxManagementIP14_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 14),
    _MuxManagementIP14_Type()
)
muxManagementIP14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP14.setStatus("current")
_MuxManagementIP15_Type = OctetString
_MuxManagementIP15_Object = MibScalar
muxManagementIP15 = _MuxManagementIP15_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 15),
    _MuxManagementIP15_Type()
)
muxManagementIP15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP15.setStatus("current")
_MuxManagementIP16_Type = OctetString
_MuxManagementIP16_Object = MibScalar
muxManagementIP16 = _MuxManagementIP16_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 16),
    _MuxManagementIP16_Type()
)
muxManagementIP16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP16.setStatus("current")
_MuxManagementIP17_Type = OctetString
_MuxManagementIP17_Object = MibScalar
muxManagementIP17 = _MuxManagementIP17_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 17),
    _MuxManagementIP17_Type()
)
muxManagementIP17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP17.setStatus("current")
_MuxManagementIP18_Type = OctetString
_MuxManagementIP18_Object = MibScalar
muxManagementIP18 = _MuxManagementIP18_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 18),
    _MuxManagementIP18_Type()
)
muxManagementIP18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP18.setStatus("current")
_MuxManagementIP19_Type = OctetString
_MuxManagementIP19_Object = MibScalar
muxManagementIP19 = _MuxManagementIP19_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 19),
    _MuxManagementIP19_Type()
)
muxManagementIP19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP19.setStatus("current")
_MuxManagementIP20_Type = OctetString
_MuxManagementIP20_Object = MibScalar
muxManagementIP20 = _MuxManagementIP20_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 20),
    _MuxManagementIP20_Type()
)
muxManagementIP20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP20.setStatus("current")
_MuxManagementIP21_Type = OctetString
_MuxManagementIP21_Object = MibScalar
muxManagementIP21 = _MuxManagementIP21_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 21),
    _MuxManagementIP21_Type()
)
muxManagementIP21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP21.setStatus("current")
_MuxManagementIP22_Type = OctetString
_MuxManagementIP22_Object = MibScalar
muxManagementIP22 = _MuxManagementIP22_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 22),
    _MuxManagementIP22_Type()
)
muxManagementIP22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP22.setStatus("current")
_MuxManagementIP23_Type = OctetString
_MuxManagementIP23_Object = MibScalar
muxManagementIP23 = _MuxManagementIP23_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 23),
    _MuxManagementIP23_Type()
)
muxManagementIP23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP23.setStatus("current")
_MuxManagementIP24_Type = OctetString
_MuxManagementIP24_Object = MibScalar
muxManagementIP24 = _MuxManagementIP24_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 24),
    _MuxManagementIP24_Type()
)
muxManagementIP24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP24.setStatus("current")
_MuxManagementIP25_Type = OctetString
_MuxManagementIP25_Object = MibScalar
muxManagementIP25 = _MuxManagementIP25_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 25),
    _MuxManagementIP25_Type()
)
muxManagementIP25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP25.setStatus("current")
_MuxManagementIP26_Type = OctetString
_MuxManagementIP26_Object = MibScalar
muxManagementIP26 = _MuxManagementIP26_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 26),
    _MuxManagementIP26_Type()
)
muxManagementIP26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP26.setStatus("current")
_MuxManagementIP27_Type = OctetString
_MuxManagementIP27_Object = MibScalar
muxManagementIP27 = _MuxManagementIP27_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 27),
    _MuxManagementIP27_Type()
)
muxManagementIP27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP27.setStatus("current")
_MuxManagementIP28_Type = OctetString
_MuxManagementIP28_Object = MibScalar
muxManagementIP28 = _MuxManagementIP28_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 28),
    _MuxManagementIP28_Type()
)
muxManagementIP28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP28.setStatus("current")
_MuxManagementIP29_Type = OctetString
_MuxManagementIP29_Object = MibScalar
muxManagementIP29 = _MuxManagementIP29_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 29),
    _MuxManagementIP29_Type()
)
muxManagementIP29.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP29.setStatus("current")
_MuxManagementIP30_Type = OctetString
_MuxManagementIP30_Object = MibScalar
muxManagementIP30 = _MuxManagementIP30_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 30),
    _MuxManagementIP30_Type()
)
muxManagementIP30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP30.setStatus("current")
_MuxManagementIP31_Type = OctetString
_MuxManagementIP31_Object = MibScalar
muxManagementIP31 = _MuxManagementIP31_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 31),
    _MuxManagementIP31_Type()
)
muxManagementIP31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP31.setStatus("current")
_MuxManagementIP32_Type = OctetString
_MuxManagementIP32_Object = MibScalar
muxManagementIP32 = _MuxManagementIP32_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 7, 32),
    _MuxManagementIP32_Type()
)
muxManagementIP32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementIP32.setStatus("current")
_MuxManMask_ObjectIdentity = ObjectIdentity
muxManMask = _MuxManMask_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8)
)
_MuxManagementMask1_Type = OctetString
_MuxManagementMask1_Object = MibScalar
muxManagementMask1 = _MuxManagementMask1_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 1),
    _MuxManagementMask1_Type()
)
muxManagementMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask1.setStatus("current")
_MuxManagementMask2_Type = OctetString
_MuxManagementMask2_Object = MibScalar
muxManagementMask2 = _MuxManagementMask2_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 2),
    _MuxManagementMask2_Type()
)
muxManagementMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask2.setStatus("current")
_MuxManagementMask3_Type = OctetString
_MuxManagementMask3_Object = MibScalar
muxManagementMask3 = _MuxManagementMask3_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 3),
    _MuxManagementMask3_Type()
)
muxManagementMask3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask3.setStatus("current")
_MuxManagementMask4_Type = OctetString
_MuxManagementMask4_Object = MibScalar
muxManagementMask4 = _MuxManagementMask4_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 4),
    _MuxManagementMask4_Type()
)
muxManagementMask4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask4.setStatus("current")
_MuxManagementMask5_Type = OctetString
_MuxManagementMask5_Object = MibScalar
muxManagementMask5 = _MuxManagementMask5_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 5),
    _MuxManagementMask5_Type()
)
muxManagementMask5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask5.setStatus("current")
_MuxManagementMask6_Type = OctetString
_MuxManagementMask6_Object = MibScalar
muxManagementMask6 = _MuxManagementMask6_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 6),
    _MuxManagementMask6_Type()
)
muxManagementMask6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask6.setStatus("current")
_MuxManagementMask7_Type = OctetString
_MuxManagementMask7_Object = MibScalar
muxManagementMask7 = _MuxManagementMask7_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 7),
    _MuxManagementMask7_Type()
)
muxManagementMask7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask7.setStatus("current")
_MuxManagementMask8_Type = OctetString
_MuxManagementMask8_Object = MibScalar
muxManagementMask8 = _MuxManagementMask8_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 8),
    _MuxManagementMask8_Type()
)
muxManagementMask8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask8.setStatus("current")
_MuxManagementMask9_Type = OctetString
_MuxManagementMask9_Object = MibScalar
muxManagementMask9 = _MuxManagementMask9_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 9),
    _MuxManagementMask9_Type()
)
muxManagementMask9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask9.setStatus("current")
_MuxManagementMask10_Type = OctetString
_MuxManagementMask10_Object = MibScalar
muxManagementMask10 = _MuxManagementMask10_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 10),
    _MuxManagementMask10_Type()
)
muxManagementMask10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask10.setStatus("current")
_MuxManagementMask11_Type = OctetString
_MuxManagementMask11_Object = MibScalar
muxManagementMask11 = _MuxManagementMask11_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 11),
    _MuxManagementMask11_Type()
)
muxManagementMask11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask11.setStatus("current")
_MuxManagementMask12_Type = OctetString
_MuxManagementMask12_Object = MibScalar
muxManagementMask12 = _MuxManagementMask12_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 12),
    _MuxManagementMask12_Type()
)
muxManagementMask12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask12.setStatus("current")
_MuxManagementMask13_Type = OctetString
_MuxManagementMask13_Object = MibScalar
muxManagementMask13 = _MuxManagementMask13_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 13),
    _MuxManagementMask13_Type()
)
muxManagementMask13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask13.setStatus("current")
_MuxManagementMask14_Type = OctetString
_MuxManagementMask14_Object = MibScalar
muxManagementMask14 = _MuxManagementMask14_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 14),
    _MuxManagementMask14_Type()
)
muxManagementMask14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask14.setStatus("current")
_MuxManagementMask15_Type = OctetString
_MuxManagementMask15_Object = MibScalar
muxManagementMask15 = _MuxManagementMask15_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 15),
    _MuxManagementMask15_Type()
)
muxManagementMask15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask15.setStatus("current")
_MuxManagementMask16_Type = OctetString
_MuxManagementMask16_Object = MibScalar
muxManagementMask16 = _MuxManagementMask16_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 16),
    _MuxManagementMask16_Type()
)
muxManagementMask16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask16.setStatus("current")
_MuxManagementMask17_Type = OctetString
_MuxManagementMask17_Object = MibScalar
muxManagementMask17 = _MuxManagementMask17_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 17),
    _MuxManagementMask17_Type()
)
muxManagementMask17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask17.setStatus("current")
_MuxManagementMask18_Type = OctetString
_MuxManagementMask18_Object = MibScalar
muxManagementMask18 = _MuxManagementMask18_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 18),
    _MuxManagementMask18_Type()
)
muxManagementMask18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask18.setStatus("current")
_MuxManagementMask19_Type = OctetString
_MuxManagementMask19_Object = MibScalar
muxManagementMask19 = _MuxManagementMask19_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 19),
    _MuxManagementMask19_Type()
)
muxManagementMask19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask19.setStatus("current")
_MuxManagementMask20_Type = OctetString
_MuxManagementMask20_Object = MibScalar
muxManagementMask20 = _MuxManagementMask20_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 20),
    _MuxManagementMask20_Type()
)
muxManagementMask20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask20.setStatus("current")
_MuxManagementMask21_Type = OctetString
_MuxManagementMask21_Object = MibScalar
muxManagementMask21 = _MuxManagementMask21_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 21),
    _MuxManagementMask21_Type()
)
muxManagementMask21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask21.setStatus("current")
_MuxManagementMask22_Type = OctetString
_MuxManagementMask22_Object = MibScalar
muxManagementMask22 = _MuxManagementMask22_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 22),
    _MuxManagementMask22_Type()
)
muxManagementMask22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask22.setStatus("current")
_MuxManagementMask23_Type = OctetString
_MuxManagementMask23_Object = MibScalar
muxManagementMask23 = _MuxManagementMask23_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 23),
    _MuxManagementMask23_Type()
)
muxManagementMask23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask23.setStatus("current")
_MuxManagementMask24_Type = OctetString
_MuxManagementMask24_Object = MibScalar
muxManagementMask24 = _MuxManagementMask24_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 24),
    _MuxManagementMask24_Type()
)
muxManagementMask24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask24.setStatus("current")
_MuxManagementMask25_Type = OctetString
_MuxManagementMask25_Object = MibScalar
muxManagementMask25 = _MuxManagementMask25_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 25),
    _MuxManagementMask25_Type()
)
muxManagementMask25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask25.setStatus("current")
_MuxManagementMask26_Type = OctetString
_MuxManagementMask26_Object = MibScalar
muxManagementMask26 = _MuxManagementMask26_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 26),
    _MuxManagementMask26_Type()
)
muxManagementMask26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask26.setStatus("current")
_MuxManagementMask27_Type = OctetString
_MuxManagementMask27_Object = MibScalar
muxManagementMask27 = _MuxManagementMask27_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 27),
    _MuxManagementMask27_Type()
)
muxManagementMask27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask27.setStatus("current")
_MuxManagementMask28_Type = OctetString
_MuxManagementMask28_Object = MibScalar
muxManagementMask28 = _MuxManagementMask28_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 28),
    _MuxManagementMask28_Type()
)
muxManagementMask28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask28.setStatus("current")
_MuxManagementMask29_Type = OctetString
_MuxManagementMask29_Object = MibScalar
muxManagementMask29 = _MuxManagementMask29_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 29),
    _MuxManagementMask29_Type()
)
muxManagementMask29.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask29.setStatus("current")
_MuxManagementMask30_Type = OctetString
_MuxManagementMask30_Object = MibScalar
muxManagementMask30 = _MuxManagementMask30_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 30),
    _MuxManagementMask30_Type()
)
muxManagementMask30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask30.setStatus("current")
_MuxManagementMask31_Type = OctetString
_MuxManagementMask31_Object = MibScalar
muxManagementMask31 = _MuxManagementMask31_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 31),
    _MuxManagementMask31_Type()
)
muxManagementMask31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask31.setStatus("current")
_MuxManagementMask32_Type = OctetString
_MuxManagementMask32_Object = MibScalar
muxManagementMask32 = _MuxManagementMask32_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 1, 8, 32),
    _MuxManagementMask32_Type()
)
muxManagementMask32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxManagementMask32.setStatus("current")
_EthTable_Object = MibTable
ethTable = _EthTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2)
)
if mibBuilder.loadTexts:
    ethTable.setStatus("current")
_EthEntry_Object = MibTableRow
ethEntry = _EthEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1)
)
ethEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ethEntry.setStatus("current")


class _EthType_Type(Integer32):
    """Custom type ethType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("copper", 1),
          ("bl", 2),
          ("bn", 4),
          ("optic", 6))
    )


_EthType_Type.__name__ = "Integer32"
_EthType_Object = MibTableColumn
ethType = _EthType_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 1),
    _EthType_Type()
)
ethType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethType.setStatus("current")


class _EthMode_Type(Integer32):
    """Custom type ethMode based on Integer32"""
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
        *(("portDown", 0),
          ("portTrunk", 1),
          ("portMulti", 2),
          ("portAccess", 3),
          ("portQinq", 4))
    )


_EthMode_Type.__name__ = "Integer32"
_EthMode_Object = MibTableColumn
ethMode = _EthMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 2),
    _EthMode_Type()
)
ethMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethMode.setStatus("current")


class _EthReservMode_Type(Integer32):
    """Custom type ethReservMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rstp", 3))
    )


_EthReservMode_Type.__name__ = "Integer32"
_EthReservMode_Object = MibTableColumn
ethReservMode = _EthReservMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 3),
    _EthReservMode_Type()
)
ethReservMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethReservMode.setStatus("current")
_EthVlan_Type = Integer32
_EthVlan_Object = MibTableColumn
ethVlan = _EthVlan_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 7),
    _EthVlan_Type()
)
ethVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethVlan.setStatus("current")


class _EthDuplexMode_Type(Integer32):
    """Custom type ethDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("halfDUPLEX10", 1),
          ("fullDUPLEX10", 2),
          ("halfDUPLEX100", 3),
          ("fullDUPLEX100", 4),
          ("fullDUPLEX1000", 6),
          ("auto10", 7))
    )


_EthDuplexMode_Type.__name__ = "Integer32"
_EthDuplexMode_Object = MibTableColumn
ethDuplexMode = _EthDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 9),
    _EthDuplexMode_Type()
)
ethDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDuplexMode.setStatus("current")
_EthStringStatus_Type = DisplayString
_EthStringStatus_Object = MibTableColumn
ethStringStatus = _EthStringStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 10),
    _EthStringStatus_Type()
)
ethStringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStringStatus.setStatus("current")


class _EthLogLevel_Type(Integer32):
    """Custom type ethLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("full", 65535))
    )


_EthLogLevel_Type.__name__ = "Integer32"
_EthLogLevel_Object = MibTableColumn
ethLogLevel = _EthLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 11),
    _EthLogLevel_Type()
)
ethLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethLogLevel.setStatus("current")


class _EthTrapLevel_Type(Integer32):
    """Custom type ethTrapLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("full", 65535))
    )


_EthTrapLevel_Type.__name__ = "Integer32"
_EthTrapLevel_Object = MibTableColumn
ethTrapLevel = _EthTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 12),
    _EthTrapLevel_Type()
)
ethTrapLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethTrapLevel.setStatus("current")
_EthIngressRateLimit_Type = Integer32
_EthIngressRateLimit_Object = MibTableColumn
ethIngressRateLimit = _EthIngressRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 13),
    _EthIngressRateLimit_Type()
)
ethIngressRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIngressRateLimit.setStatus("current")


class _EthSecurity_Type(Integer32):
    """Custom type ethSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("noLearning", 2),
          ("onlyOneMac", 4))
    )


_EthSecurity_Type.__name__ = "Integer32"
_EthSecurity_Object = MibTableColumn
ethSecurity = _EthSecurity_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 15),
    _EthSecurity_Type()
)
ethSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethSecurity.setStatus("current")


class _EthMonitorPort_Type(Integer32):
    """Custom type ethMonitorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("none", -1)
    )


_EthMonitorPort_Type.__name__ = "Integer32"
_EthMonitorPort_Object = MibTableColumn
ethMonitorPort = _EthMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 16),
    _EthMonitorPort_Type()
)
ethMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethMonitorPort.setStatus("current")


class _EthTrunkId_Type(Integer32):
    """Custom type ethTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("none", -1)
    )


_EthTrunkId_Type.__name__ = "Integer32"
_EthTrunkId_Object = MibTableColumn
ethTrunkId = _EthTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 17),
    _EthTrunkId_Type()
)
ethTrunkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethTrunkId.setStatus("current")


class _EthPriorityMode_Type(Integer32):
    """Custom type ethPriorityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16,
              32,
              48,
              112)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("tag", 16),
          ("ip", 32),
          ("ipTag", 48),
          ("tagIP", 112))
    )


_EthPriorityMode_Type.__name__ = "Integer32"
_EthPriorityMode_Object = MibTableColumn
ethPriorityMode = _EthPriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 18),
    _EthPriorityMode_Type()
)
ethPriorityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPriorityMode.setStatus("current")
_EthDefaultPriority_Type = Integer32
_EthDefaultPriority_Object = MibTableColumn
ethDefaultPriority = _EthDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 19),
    _EthDefaultPriority_Type()
)
ethDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDefaultPriority.setStatus("current")
_EthEgressRateLimit_Type = Integer32
_EthEgressRateLimit_Object = MibTableColumn
ethEgressRateLimit = _EthEgressRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 20),
    _EthEgressRateLimit_Type()
)
ethEgressRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethEgressRateLimit.setStatus("current")


class _EthRateLimitMode_Type(Integer32):
    """Custom type ethRateLimitMode based on Integer32"""
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
        *(("all", 0),
          ("broadMultiFloodedUnicast", 1),
          ("broadMulticast", 2),
          ("broadcast", 3))
    )


_EthRateLimitMode_Type.__name__ = "Integer32"
_EthRateLimitMode_Object = MibTableColumn
ethRateLimitMode = _EthRateLimitMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 21),
    _EthRateLimitMode_Type()
)
ethRateLimitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethRateLimitMode.setStatus("current")


class _EthIGMPsnooping_Type(Integer32):
    """Custom type ethIGMPsnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_EthIGMPsnooping_Type.__name__ = "Integer32"
_EthIGMPsnooping_Object = MibTableColumn
ethIGMPsnooping = _EthIGMPsnooping_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 23),
    _EthIGMPsnooping_Type()
)
ethIGMPsnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIGMPsnooping.setStatus("current")
_EthCurrentStat_Type = DisplayString
_EthCurrentStat_Object = MibTableColumn
ethCurrentStat = _EthCurrentStat_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 24),
    _EthCurrentStat_Type()
)
ethCurrentStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentStat.setStatus("current")
_EthMaxLearnNum_Type = Integer32
_EthMaxLearnNum_Object = MibTableColumn
ethMaxLearnNum = _EthMaxLearnNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 26),
    _EthMaxLearnNum_Type()
)
ethMaxLearnNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethMaxLearnNum.setStatus("current")


class _EthDHCPrelay_Type(Integer32):
    """Custom type ethDHCPrelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("trunk", 1),
          ("user", 2))
    )


_EthDHCPrelay_Type.__name__ = "Integer32"
_EthDHCPrelay_Object = MibTableColumn
ethDHCPrelay = _EthDHCPrelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 27),
    _EthDHCPrelay_Type()
)
ethDHCPrelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDHCPrelay.setStatus("current")


class _EthDHCPtrusted_Type(Integer32):
    """Custom type ethDHCPtrusted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_EthDHCPtrusted_Type.__name__ = "Integer32"
_EthDHCPtrusted_Object = MibTableColumn
ethDHCPtrusted = _EthDHCPtrusted_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 28),
    _EthDHCPtrusted_Type()
)
ethDHCPtrusted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDHCPtrusted.setStatus("current")


class _EthIGMPfastleave_Type(Integer32):
    """Custom type ethIGMPfastleave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_EthIGMPfastleave_Type.__name__ = "Integer32"
_EthIGMPfastleave_Object = MibTableColumn
ethIGMPfastleave = _EthIGMPfastleave_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 29),
    _EthIGMPfastleave_Type()
)
ethIGMPfastleave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIGMPfastleave.setStatus("current")


class _EthMVRtype_Type(Integer32):
    """Custom type ethMVRtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source", 1),
          ("receiver", 2))
    )


_EthMVRtype_Type.__name__ = "Integer32"
_EthMVRtype_Object = MibTableColumn
ethMVRtype = _EthMVRtype_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 30),
    _EthMVRtype_Type()
)
ethMVRtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethMVRtype.setStatus("current")


class _EthUserport_Type(Integer32):
    """Custom type ethUserport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_EthUserport_Type.__name__ = "Integer32"
_EthUserport_Object = MibTableColumn
ethUserport = _EthUserport_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 31),
    _EthUserport_Type()
)
ethUserport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethUserport.setStatus("current")


class _EthForceVlan_Type(Integer32):
    """Custom type ethForceVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_EthForceVlan_Type.__name__ = "Integer32"
_EthForceVlan_Object = MibTableColumn
ethForceVlan = _EthForceVlan_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 32),
    _EthForceVlan_Type()
)
ethForceVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethForceVlan.setStatus("current")
_EthResetStat_Type = Integer32
_EthResetStat_Object = MibTableColumn
ethResetStat = _EthResetStat_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 33),
    _EthResetStat_Type()
)
ethResetStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethResetStat.setStatus("current")
_EthStateInternal_Type = Integer32
_EthStateInternal_Object = MibTableColumn
ethStateInternal = _EthStateInternal_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 2, 1, 34),
    _EthStateInternal_Type()
)
ethStateInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethStateInternal.setStatus("current")
_E1Old1_ObjectIdentity = ObjectIdentity
e1Old1 = _E1Old1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 3)
)
_E1Old2_ObjectIdentity = ObjectIdentity
e1Old2 = _E1Old2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 5)
)
_BranchSysReset_ObjectIdentity = ObjectIdentity
branchSysReset = _BranchSysReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 6)
)
_SubBranchSysReset_ObjectIdentity = ObjectIdentity
subBranchSysReset = _SubBranchSysReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 6, 1)
)
_SysReset_Type = DisplayString
_SysReset_Object = MibScalar
sysReset = _SysReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 6, 1, 1),
    _SysReset_Type()
)
sysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysReset.setStatus("current")
_MuxRSTP_ObjectIdentity = ObjectIdentity
muxRSTP = _MuxRSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 9)
)
_RSTPForwardDelay_Type = Integer32
_RSTPForwardDelay_Object = MibScalar
rSTPForwardDelay = _RSTPForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 9, 1),
    _RSTPForwardDelay_Type()
)
rSTPForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rSTPForwardDelay.setStatus("current")
_RSTPMaxAge_Type = Integer32
_RSTPMaxAge_Object = MibScalar
rSTPMaxAge = _RSTPMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 9, 2),
    _RSTPMaxAge_Type()
)
rSTPMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rSTPMaxAge.setStatus("current")
_RSTPHelloTime_Type = Integer32
_RSTPHelloTime_Object = MibScalar
rSTPHelloTime = _RSTPHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 9, 3),
    _RSTPHelloTime_Type()
)
rSTPHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rSTPHelloTime.setStatus("current")
_RSTPBridgePrio_Type = Integer32
_RSTPBridgePrio_Object = MibScalar
rSTPBridgePrio = _RSTPBridgePrio_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 9, 4),
    _RSTPBridgePrio_Type()
)
rSTPBridgePrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rSTPBridgePrio.setStatus("current")
_RSTPTable_Object = MibTable
rSTPTable = _RSTPTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 9, 5)
)
if mibBuilder.loadTexts:
    rSTPTable.setStatus("current")
_RSTPEntry_Object = MibTableRow
rSTPEntry = _RSTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 9, 5, 1)
)
rSTPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rSTPEntry.setStatus("current")
_RSTPPortPrio_Type = Integer32
_RSTPPortPrio_Object = MibTableColumn
rSTPPortPrio = _RSTPPortPrio_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 9, 5, 1, 1),
    _RSTPPortPrio_Type()
)
rSTPPortPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rSTPPortPrio.setStatus("current")


class _RSTPEdge_Type(Integer32):
    """Custom type rSTPEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RSTPEdge_Type.__name__ = "Integer32"
_RSTPEdge_Object = MibTableColumn
rSTPEdge = _RSTPEdge_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 9, 5, 1, 2),
    _RSTPEdge_Type()
)
rSTPEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rSTPEdge.setStatus("current")
_RSTPPathCost_Type = Integer32
_RSTPPathCost_Object = MibTableColumn
rSTPPathCost = _RSTPPathCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 9, 5, 1, 3),
    _RSTPPathCost_Type()
)
rSTPPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rSTPPathCost.setStatus("current")


class _RSTPp2p_Type(Integer32):
    """Custom type rSTPp2p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 0),
          ("no", 1),
          ("auto", 2))
    )


_RSTPp2p_Type.__name__ = "Integer32"
_RSTPp2p_Object = MibTableColumn
rSTPp2p = _RSTPp2p_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 9, 5, 1, 4),
    _RSTPp2p_Type()
)
rSTPp2p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rSTPp2p.setStatus("current")


class _RSTPRootGuard_Type(Integer32):
    """Custom type rSTPRootGuard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RSTPRootGuard_Type.__name__ = "Integer32"
_RSTPRootGuard_Object = MibTableColumn
rSTPRootGuard = _RSTPRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 9, 5, 1, 5),
    _RSTPRootGuard_Type()
)
rSTPRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rSTPRootGuard.setStatus("current")


class _RSTPState_Type(Integer32):
    """Custom type rSTPState based on Integer32"""
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
        *(("disabled", 0),
          ("discarding", 1),
          ("learning", 2),
          ("forwarding", 3),
          ("nonStp", 4),
          ("unknown", 5))
    )


_RSTPState_Type.__name__ = "Integer32"
_RSTPState_Object = MibTableColumn
rSTPState = _RSTPState_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 9, 5, 1, 6),
    _RSTPState_Type()
)
rSTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSTPState.setStatus("current")


class _RSTPRole_Type(Integer32):
    """Custom type rSTPRole based on Integer32"""
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
        *(("disabled", 0),
          ("alternate", 1),
          ("backup", 2),
          ("root", 3),
          ("designated", 4),
          ("nonStp", 5))
    )


_RSTPRole_Type.__name__ = "Integer32"
_RSTPRole_Object = MibTableColumn
rSTPRole = _RSTPRole_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 9, 5, 1, 7),
    _RSTPRole_Type()
)
rSTPRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSTPRole.setStatus("current")
_LldpMib_ObjectIdentity = ObjectIdentity
lldpMib = _LldpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 16)
)
_LldpObjects_ObjectIdentity = ObjectIdentity
lldpObjects = _LldpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1)
)
_LldpConfiguration_ObjectIdentity = ObjectIdentity
lldpConfiguration = _LldpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 1)
)


class _LldpMessageTxInterval_Type(Integer32):
    """Custom type lldpMessageTxInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 32768),
    )


_LldpMessageTxInterval_Type.__name__ = "Integer32"
_LldpMessageTxInterval_Object = MibScalar
lldpMessageTxInterval = _LldpMessageTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 1, 1),
    _LldpMessageTxInterval_Type()
)
lldpMessageTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMessageTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    lldpMessageTxInterval.setUnits("seconds")


class _LldpMessageTxHoldMultiplier_Type(Integer32):
    """Custom type lldpMessageTxHoldMultiplier based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_LldpMessageTxHoldMultiplier_Type.__name__ = "Integer32"
_LldpMessageTxHoldMultiplier_Object = MibScalar
lldpMessageTxHoldMultiplier = _LldpMessageTxHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 1, 2),
    _LldpMessageTxHoldMultiplier_Type()
)
lldpMessageTxHoldMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMessageTxHoldMultiplier.setStatus("current")
_LldpPortConfigTable_Object = MibTable
lldpPortConfigTable = _LldpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 1, 6)
)
if mibBuilder.loadTexts:
    lldpPortConfigTable.setStatus("current")
_LldpPortConfigEntry_Object = MibTableRow
lldpPortConfigEntry = _LldpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 1, 6, 1)
)
lldpPortConfigEntry.setIndexNames(
    (0, "EMUX-MIB-3XX", "lldpPortConfigPortNum"),
)
if mibBuilder.loadTexts:
    lldpPortConfigEntry.setStatus("current")
_LldpPortConfigPortNum_Type = LldpPortNumber
_LldpPortConfigPortNum_Object = MibTableColumn
lldpPortConfigPortNum = _LldpPortConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 1, 6, 1, 1),
    _LldpPortConfigPortNum_Type()
)
lldpPortConfigPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpPortConfigPortNum.setStatus("current")


class _LldpPortConfigAdminStatus_Type(Integer32):
    """Custom type lldpPortConfigAdminStatus based on Integer32"""
    defaultValue = 3

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
        *(("txOnly", 1),
          ("rxOnly", 2),
          ("txAndRx", 3),
          ("disabled", 4))
    )


_LldpPortConfigAdminStatus_Type.__name__ = "Integer32"
_LldpPortConfigAdminStatus_Object = MibTableColumn
lldpPortConfigAdminStatus = _LldpPortConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 1, 6, 1, 2),
    _LldpPortConfigAdminStatus_Type()
)
lldpPortConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortConfigAdminStatus.setStatus("current")


class _LldpPortConfigTLVsTxEnable_Type(Bits):
    """Custom type lldpPortConfigTLVsTxEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("portDesc", 0),
          ("sysName", 1),
          ("sysDesc", 2),
          ("sysCap", 3))
    )

_LldpPortConfigTLVsTxEnable_Type.__name__ = "Bits"
_LldpPortConfigTLVsTxEnable_Object = MibTableColumn
lldpPortConfigTLVsTxEnable = _LldpPortConfigTLVsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 1, 6, 1, 3),
    _LldpPortConfigTLVsTxEnable_Type()
)
lldpPortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortConfigTLVsTxEnable.setStatus("current")
_LldpRemoteSystemsData_ObjectIdentity = ObjectIdentity
lldpRemoteSystemsData = _LldpRemoteSystemsData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 4)
)
_LldpRemTable_Object = MibTable
lldpRemTable = _LldpRemTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lldpRemTable.setStatus("current")
_LldpRemEntry_Object = MibTableRow
lldpRemEntry = _LldpRemEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 4, 1, 1)
)
lldpRemEntry.setIndexNames(
    (0, "EMUX-MIB-3XX", "lldpRemTimeMark"),
    (0, "EMUX-MIB-3XX", "lldpRemLocalPortNum"),
    (0, "EMUX-MIB-3XX", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpRemEntry.setStatus("current")
_LldpRemTimeMark_Type = TimeFilter
_LldpRemTimeMark_Object = MibTableColumn
lldpRemTimeMark = _LldpRemTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 4, 1, 1, 1),
    _LldpRemTimeMark_Type()
)
lldpRemTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpRemTimeMark.setStatus("current")
_LldpRemLocalPortNum_Type = LldpPortNumber
_LldpRemLocalPortNum_Object = MibTableColumn
lldpRemLocalPortNum = _LldpRemLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 4, 1, 1, 2),
    _LldpRemLocalPortNum_Type()
)
lldpRemLocalPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpRemLocalPortNum.setStatus("current")


class _LldpRemIndex_Type(Integer32):
    """Custom type lldpRemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpRemIndex_Type.__name__ = "Integer32"
_LldpRemIndex_Object = MibTableColumn
lldpRemIndex = _LldpRemIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 4, 1, 1, 3),
    _LldpRemIndex_Type()
)
lldpRemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpRemIndex.setStatus("current")
_LldpRemChassisIdSubtype_Type = LldpChassisIdSubtype
_LldpRemChassisIdSubtype_Object = MibTableColumn
lldpRemChassisIdSubtype = _LldpRemChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 4, 1, 1, 4),
    _LldpRemChassisIdSubtype_Type()
)
lldpRemChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemChassisIdSubtype.setStatus("current")
_LldpRemChassisId_Type = LldpChassisId
_LldpRemChassisId_Object = MibTableColumn
lldpRemChassisId = _LldpRemChassisId_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 4, 1, 1, 5),
    _LldpRemChassisId_Type()
)
lldpRemChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemChassisId.setStatus("current")
_LldpRemPortIdSubtype_Type = LldpPortIdSubtype
_LldpRemPortIdSubtype_Object = MibTableColumn
lldpRemPortIdSubtype = _LldpRemPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 4, 1, 1, 6),
    _LldpRemPortIdSubtype_Type()
)
lldpRemPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemPortIdSubtype.setStatus("current")
_LldpRemPortId_Type = LldpPortId
_LldpRemPortId_Object = MibTableColumn
lldpRemPortId = _LldpRemPortId_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 4, 1, 1, 7),
    _LldpRemPortId_Type()
)
lldpRemPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemPortId.setStatus("current")
_LldpRemPortDesc_Type = SnmpAdminString
_LldpRemPortDesc_Object = MibTableColumn
lldpRemPortDesc = _LldpRemPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 4, 1, 1, 8),
    _LldpRemPortDesc_Type()
)
lldpRemPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemPortDesc.setStatus("current")


class _LldpRemSysName_Type(SnmpAdminString):
    """Custom type lldpRemSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpRemSysName_Type.__name__ = "SnmpAdminString"
_LldpRemSysName_Object = MibTableColumn
lldpRemSysName = _LldpRemSysName_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 4, 1, 1, 9),
    _LldpRemSysName_Type()
)
lldpRemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemSysName.setStatus("current")


class _LldpRemSysDesc_Type(SnmpAdminString):
    """Custom type lldpRemSysDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpRemSysDesc_Type.__name__ = "SnmpAdminString"
_LldpRemSysDesc_Object = MibTableColumn
lldpRemSysDesc = _LldpRemSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 4, 1, 1, 10),
    _LldpRemSysDesc_Type()
)
lldpRemSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemSysDesc.setStatus("current")
_LldpRemManAddrSubtype_Type = AddressFamilyNumbers
_LldpRemManAddrSubtype_Object = MibTableColumn
lldpRemManAddrSubtype = _LldpRemManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 4, 1, 1, 11),
    _LldpRemManAddrSubtype_Type()
)
lldpRemManAddrSubtype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpRemManAddrSubtype.setStatus("current")
_LldpRemManAddr_Type = LldpManAddress
_LldpRemManAddr_Object = MibTableColumn
lldpRemManAddr = _LldpRemManAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 4, 1, 1, 12),
    _LldpRemManAddr_Type()
)
lldpRemManAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpRemManAddr.setStatus("current")
_LldpRemManAddrStr_Type = DisplayString
_LldpRemManAddrStr_Object = MibTableColumn
lldpRemManAddrStr = _LldpRemManAddrStr_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 4, 1, 1, 13),
    _LldpRemManAddrStr_Type()
)
lldpRemManAddrStr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpRemManAddrStr.setStatus("current")
_LldpRemDataValid_Type = Integer32
_LldpRemDataValid_Object = MibTableColumn
lldpRemDataValid = _LldpRemDataValid_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 16, 1, 4, 1, 1, 14),
    _LldpRemDataValid_Type()
)
lldpRemDataValid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpRemDataValid.setStatus("current")
_E1SubChTable_Object = MibTable
e1SubChTable = _E1SubChTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17)
)
if mibBuilder.loadTexts:
    e1SubChTable.setStatus("current")
_E1SubChEntry_Object = MibTableRow
e1SubChEntry = _E1SubChEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1)
)
e1SubChEntry.setIndexNames(
    (0, "EMUX-MIB-3XX", "e1SubChIndex"),
)
if mibBuilder.loadTexts:
    e1SubChEntry.setStatus("current")


class _E1SubChIndex_Type(Integer32):
    """Custom type e1SubChIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_E1SubChIndex_Type.__name__ = "Integer32"
_E1SubChIndex_Object = MibTableColumn
e1SubChIndex = _E1SubChIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 1),
    _E1SubChIndex_Type()
)
e1SubChIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1SubChIndex.setStatus("current")


class _E1aMode_Type(Bits):
    """Custom type e1aMode based on Bits"""
    namedValues = NamedValues(
        *(("powerDown", 0),
          ("work", 1),
          ("localLoop", 2),
          ("remoteLoop", 3),
          ("testMode", 4),
          ("listening", 5),
          ("reset", 6))
    )

_E1aMode_Type.__name__ = "Bits"
_E1aMode_Object = MibTableColumn
e1aMode = _E1aMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 2),
    _E1aMode_Type()
)
e1aMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1aMode.setStatus("current")
_E1aSetupPayload_Type = Integer32
_E1aSetupPayload_Object = MibTableColumn
e1aSetupPayload = _E1aSetupPayload_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 3),
    _E1aSetupPayload_Type()
)
e1aSetupPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1aSetupPayload.setStatus("current")
_E1aSetupJBuf_Type = Integer32
_E1aSetupJBuf_Object = MibTableColumn
e1aSetupJBuf = _E1aSetupJBuf_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 4),
    _E1aSetupJBuf_Type()
)
e1aSetupJBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1aSetupJBuf.setStatus("current")
_E1aSetupGap_Type = Integer32
_E1aSetupGap_Object = MibTableColumn
e1aSetupGap = _E1aSetupGap_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 5),
    _E1aSetupGap_Type()
)
e1aSetupGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1aSetupGap.setStatus("current")


class _E1ProtLevel_Type(Integer32):
    """Custom type e1ProtLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("mac", 1),
          ("udp", 2))
    )


_E1ProtLevel_Type.__name__ = "Integer32"
_E1ProtLevel_Object = MibTableColumn
e1ProtLevel = _E1ProtLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 6),
    _E1ProtLevel_Type()
)
e1ProtLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1ProtLevel.setStatus("current")
_E1Vlan_Type = Integer32
_E1Vlan_Object = MibTableColumn
e1Vlan = _E1Vlan_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 7),
    _E1Vlan_Type()
)
e1Vlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1Vlan.setStatus("current")
_E1VlanPri_Type = Integer32
_E1VlanPri_Object = MibTableColumn
e1VlanPri = _E1VlanPri_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 8),
    _E1VlanPri_Type()
)
e1VlanPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1VlanPri.setStatus("current")
_E1ToS_Type = Integer32
_E1ToS_Object = MibTableColumn
e1ToS = _E1ToS_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 9),
    _E1ToS_Type()
)
e1ToS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1ToS.setStatus("current")
_E1DstChannel_Type = Integer32
_E1DstChannel_Object = MibTableColumn
e1DstChannel = _E1DstChannel_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 10),
    _E1DstChannel_Type()
)
e1DstChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1DstChannel.setStatus("current")
_E1DstMAC_Type = OctetString
_E1DstMAC_Object = MibTableColumn
e1DstMAC = _E1DstMAC_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 11),
    _E1DstMAC_Type()
)
e1DstMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1DstMAC.setStatus("current")
_E1DstIP_Type = OctetString
_E1DstIP_Object = MibTableColumn
e1DstIP = _E1DstIP_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 12),
    _E1DstIP_Type()
)
e1DstIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1DstIP.setStatus("current")
_E1Leds_Type = Integer32
_E1Leds_Object = MibTableColumn
e1Leds = _E1Leds_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 13),
    _E1Leds_Type()
)
e1Leds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1Leds.setStatus("current")


class _E1Framed_Type(Integer32):
    """Custom type e1Framed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unframed", 0),
          ("framed", 1))
    )


_E1Framed_Type.__name__ = "Integer32"
_E1Framed_Object = MibTableColumn
e1Framed = _E1Framed_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 14),
    _E1Framed_Type()
)
e1Framed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1Framed.setStatus("current")
_E1Description_Type = DisplayString
_E1Description_Object = MibTableColumn
e1Description = _E1Description_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 15),
    _E1Description_Type()
)
e1Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1Description.setStatus("current")
_E1TestStatus_Type = DisplayString
_E1TestStatus_Object = MibTableColumn
e1TestStatus = _E1TestStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 16),
    _E1TestStatus_Type()
)
e1TestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1TestStatus.setStatus("current")
_E1LogLevel_Type = Integer32
_E1LogLevel_Object = MibTableColumn
e1LogLevel = _E1LogLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 17),
    _E1LogLevel_Type()
)
e1LogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1LogLevel.setStatus("current")
_E1TrapLevel_Type = Integer32
_E1TrapLevel_Object = MibTableColumn
e1TrapLevel = _E1TrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 18),
    _E1TrapLevel_Type()
)
e1TrapLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1TrapLevel.setStatus("current")
_E1AvgTime_Type = Integer32
_E1AvgTime_Object = MibTableColumn
e1AvgTime = _E1AvgTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 19),
    _E1AvgTime_Type()
)
e1AvgTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1AvgTime.setStatus("current")
_E1DstMask_Type = Counter64
_E1DstMask_Object = MibTableColumn
e1DstMask = _E1DstMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 20),
    _E1DstMask_Type()
)
e1DstMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1DstMask.setStatus("current")
_E1DstSubchIndex_Type = Integer32
_E1DstSubchIndex_Object = MibTableColumn
e1DstSubchIndex = _E1DstSubchIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 21),
    _E1DstSubchIndex_Type()
)
e1DstSubchIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1DstSubchIndex.setStatus("current")
_E1DstTextMask_Type = DisplayString
_E1DstTextMask_Object = MibTableColumn
e1DstTextMask = _E1DstTextMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 22),
    _E1DstTextMask_Type()
)
e1DstTextMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1DstTextMask.setStatus("current")
_E1aUptime_Type = Integer32
_E1aUptime_Object = MibTableColumn
e1aUptime = _E1aUptime_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 23),
    _E1aUptime_Type()
)
e1aUptime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1aUptime.setStatus("current")
_E1lState_Type = Integer32
_E1lState_Object = MibTableColumn
e1lState = _E1lState_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 24),
    _E1lState_Type()
)
e1lState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1lState.setStatus("current")
_E1rState_Type = Integer32
_E1rState_Object = MibTableColumn
e1rState = _E1rState_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 25),
    _E1rState_Type()
)
e1rState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1rState.setStatus("current")
_E1sMask_Type = Counter64
_E1sMask_Object = MibTableColumn
e1sMask = _E1sMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 26),
    _E1sMask_Type()
)
e1sMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1sMask.setStatus("current")
_E1stMask_Type = DisplayString
_E1stMask_Object = MibTableColumn
e1stMask = _E1stMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 27),
    _E1stMask_Type()
)
e1stMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1stMask.setStatus("current")
_E1SubchNum_Type = Integer32
_E1SubchNum_Object = MibTableColumn
e1SubchNum = _E1SubchNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 28),
    _E1SubchNum_Type()
)
e1SubchNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1SubchNum.setStatus("current")


class _E1Compression_Type(Integer32):
    """Custom type e1Compression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("uncompressed", 0),
          ("compressed", 1))
    )


_E1Compression_Type.__name__ = "Integer32"
_E1Compression_Object = MibTableColumn
e1Compression = _E1Compression_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 29),
    _E1Compression_Type()
)
e1Compression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1Compression.setStatus("current")
_E1CompressTime_Type = Integer32
_E1CompressTime_Object = MibTableColumn
e1CompressTime = _E1CompressTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 30),
    _E1CompressTime_Type()
)
e1CompressTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CompressTime.setStatus("current")
_E1LIUstate_Type = Counter64
_E1LIUstate_Object = MibTableColumn
e1LIUstate = _E1LIUstate_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 31),
    _E1LIUstate_Type()
)
e1LIUstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1LIUstate.setStatus("current")


class _E1GatewayBypass_Type(Integer32):
    """Custom type e1GatewayBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_E1GatewayBypass_Type.__name__ = "Integer32"
_E1GatewayBypass_Object = MibTableColumn
e1GatewayBypass = _E1GatewayBypass_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 32),
    _E1GatewayBypass_Type()
)
e1GatewayBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1GatewayBypass.setStatus("current")
_E1OutFreq_Type = Integer32
_E1OutFreq_Object = MibTableColumn
e1OutFreq = _E1OutFreq_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 33),
    _E1OutFreq_Type()
)
e1OutFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1OutFreq.setStatus("current")
_E1LeftSlip_Type = Integer32
_E1LeftSlip_Object = MibTableColumn
e1LeftSlip = _E1LeftSlip_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 34),
    _E1LeftSlip_Type()
)
e1LeftSlip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1LeftSlip.setStatus("current")
_E1RightSlip_Type = Integer32
_E1RightSlip_Object = MibTableColumn
e1RightSlip = _E1RightSlip_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 35),
    _E1RightSlip_Type()
)
e1RightSlip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1RightSlip.setStatus("current")
_E1LeftSlipPkt_Type = Integer32
_E1LeftSlipPkt_Object = MibTableColumn
e1LeftSlipPkt = _E1LeftSlipPkt_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 36),
    _E1LeftSlipPkt_Type()
)
e1LeftSlipPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1LeftSlipPkt.setStatus("current")
_E1RightSlipPkt_Type = Integer32
_E1RightSlipPkt_Object = MibTableColumn
e1RightSlipPkt = _E1RightSlipPkt_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 37),
    _E1RightSlipPkt_Type()
)
e1RightSlipPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1RightSlipPkt.setStatus("current")
_UsedTimeSlots_Type = Integer32
_UsedTimeSlots_Object = MibTableColumn
usedTimeSlots = _UsedTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 38),
    _UsedTimeSlots_Type()
)
usedTimeSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usedTimeSlots.setStatus("current")
_LiuStat_Type = DisplayString
_LiuStat_Object = MibTableColumn
liuStat = _LiuStat_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 39),
    _LiuStat_Type()
)
liuStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liuStat.setStatus("current")
_PktStat_Type = DisplayString
_PktStat_Object = MibTableColumn
pktStat = _PktStat_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 40),
    _PktStat_Type()
)
pktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktStat.setStatus("current")
_StateStat_Type = DisplayString
_StateStat_Object = MibTableColumn
stateStat = _StateStat_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 41),
    _StateStat_Type()
)
stateStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateStat.setStatus("current")
_TimeStat_Type = DisplayString
_TimeStat_Object = MibTableColumn
timeStat = _TimeStat_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 42),
    _TimeStat_Type()
)
timeStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeStat.setStatus("current")
_ResetStat_Type = Integer32
_ResetStat_Object = MibTableColumn
resetStat = _ResetStat_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 45),
    _ResetStat_Type()
)
resetStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetStat.setStatus("current")
_SaveStat_Type = Integer32
_SaveStat_Object = MibTableColumn
saveStat = _SaveStat_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 46),
    _SaveStat_Type()
)
saveStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveStat.setStatus("current")
_E1fstate_Type = Integer32
_E1fstate_Object = MibTableColumn
e1fstate = _E1fstate_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 47),
    _E1fstate_Type()
)
e1fstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1fstate.setStatus("current")


class _SpregMode_Type(Integer32):
    """Custom type spregMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pid", 0),
          ("saMODE", 1),
          ("iaMODE", 2))
    )


_SpregMode_Type.__name__ = "Integer32"
_SpregMode_Object = MibTableColumn
spregMode = _SpregMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 48),
    _SpregMode_Type()
)
spregMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spregMode.setStatus("current")
_SpregQueueSize_Type = Integer32
_SpregQueueSize_Object = MibTableColumn
spregQueueSize = _SpregQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 49),
    _SpregQueueSize_Type()
)
spregQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spregQueueSize.setStatus("current")


class _RecoveryLost_Type(Integer32):
    """Custom type recoveryLost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RecoveryLost_Type.__name__ = "Integer32"
_RecoveryLost_Object = MibTableColumn
recoveryLost = _RecoveryLost_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 50),
    _RecoveryLost_Type()
)
recoveryLost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recoveryLost.setStatus("current")
_V5SignalLabel_Type = Integer32
_V5SignalLabel_Object = MibTableColumn
v5SignalLabel = _V5SignalLabel_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 51),
    _V5SignalLabel_Type()
)
v5SignalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5SignalLabel.setStatus("current")
_V5SignalLabelText_Type = DisplayString
_V5SignalLabelText_Object = MibTableColumn
v5SignalLabelText = _V5SignalLabelText_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 52),
    _V5SignalLabelText_Type()
)
v5SignalLabelText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5SignalLabelText.setStatus("current")
_E1IfIndex_Type = Integer32
_E1IfIndex_Object = MibTableColumn
e1IfIndex = _E1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 53),
    _E1IfIndex_Type()
)
e1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1IfIndex.setStatus("current")
_E1WanIP_Type = OctetString
_E1WanIP_Object = MibTableColumn
e1WanIP = _E1WanIP_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 54),
    _E1WanIP_Type()
)
e1WanIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1WanIP.setStatus("current")
_E1RemoteSIPPort_Type = Integer32
_E1RemoteSIPPort_Object = MibTableColumn
e1RemoteSIPPort = _E1RemoteSIPPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 55),
    _E1RemoteSIPPort_Type()
)
e1RemoteSIPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1RemoteSIPPort.setStatus("current")
_E1RemoteTDMPort_Type = Integer32
_E1RemoteTDMPort_Object = MibTableColumn
e1RemoteTDMPort = _E1RemoteTDMPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 56),
    _E1RemoteTDMPort_Type()
)
e1RemoteTDMPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1RemoteTDMPort.setStatus("current")
_E1UsedTimeslotsCount_Type = Integer32
_E1UsedTimeslotsCount_Object = MibTableColumn
e1UsedTimeslotsCount = _E1UsedTimeslotsCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 2, 17, 1, 57),
    _E1UsedTimeslotsCount_Type()
)
e1UsedTimeslotsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1UsedTimeslotsCount.setStatus("current")
_MuxCompliances_ObjectIdentity = ObjectIdentity
muxCompliances = _MuxCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 30)
)
_MuxGroups_ObjectIdentity = ObjectIdentity
muxGroups = _MuxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 31)
)
_LldpCompliances_ObjectIdentity = ObjectIdentity
lldpCompliances = _LldpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 32)
)
_LldpGroups_ObjectIdentity = ObjectIdentity
lldpGroups = _LldpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 2, 33)
)
_MuxExtended_ObjectIdentity = ObjectIdentity
muxExtended = _MuxExtended_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3)
)
_Leds_ObjectIdentity = ObjectIdentity
leds = _Leds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 2)
)
_SystemLed_Type = Integer32
_SystemLed_Object = MibScalar
systemLed = _SystemLed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1),
    _SystemLed_Type()
)
systemLed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemLed.setStatus("current")
_CtrlLed_Type = Integer32
_CtrlLed_Object = MibScalar
ctrlLed = _CtrlLed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3),
    _CtrlLed_Type()
)
ctrlLed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctrlLed.setStatus("current")
_CtrlAlarm_Type = Integer32
_CtrlAlarm_Object = MibScalar
ctrlAlarm = _CtrlAlarm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 4),
    _CtrlAlarm_Type()
)
ctrlAlarm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctrlAlarm.setStatus("current")
_CtrlAlarmReset_Type = Integer32
_CtrlAlarmReset_Object = MibScalar
ctrlAlarmReset = _CtrlAlarmReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 5),
    _CtrlAlarmReset_Type()
)
ctrlAlarmReset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctrlAlarmReset.setStatus("current")

# Managed Objects groups

muxBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18, 2, 31, 1)
)
muxBaseGroup.setObjects(
      *(("EMUX-MIB-3XX", "hardwareVersion"),
        ("EMUX-MIB-3XX", "fwVersion"),
        ("EMUX-MIB-3XX", "softwareVersion"),
        ("EMUX-MIB-3XX", "bootloaderVersion"),
        ("EMUX-MIB-3XX", "systemID"),
        ("EMUX-MIB-3XX", "powerVoltage"),
        ("EMUX-MIB-3XX", "caseTemperature"),
        ("EMUX-MIB-3XX", "envVer"),
        ("EMUX-MIB-3XX", "accVoltage"),
        ("EMUX-MIB-3XX", "currentConsumption"))
)
if mibBuilder.loadTexts:
    muxBaseGroup.setStatus("current")

muxSensorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18, 2, 31, 2)
)
muxSensorGroup.setObjects(
      *(("EMUX-MIB-3XX", "sensor1"),
        ("EMUX-MIB-3XX", "sensor2"),
        ("EMUX-MIB-3XX", "sensor3"))
)
if mibBuilder.loadTexts:
    muxSensorGroup.setStatus("current")

muxDateTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18, 2, 31, 3)
)
muxDateTimeGroup.setObjects(
      *(("EMUX-MIB-3XX", "muxDate"),
        ("EMUX-MIB-3XX", "muxTime"),
        ("EMUX-MIB-3XX", "muxTimeZone"),
        ("EMUX-MIB-3XX", "muxTimeServer"),
        ("EMUX-MIB-3XX", "muxTimeSynchro"),
        ("EMUX-MIB-3XX", "muxTimeNextSynchro"),
        ("EMUX-MIB-3XX", "muxTimeSynchroPeriod"))
)
if mibBuilder.loadTexts:
    muxDateTimeGroup.setStatus("current")

muxIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18, 2, 31, 4)
)
muxIpGroup.setObjects(
      *(("EMUX-MIB-3XX", "muxMAC"),
        ("EMUX-MIB-3XX", "muxIPaddr"),
        ("EMUX-MIB-3XX", "muxMask"),
        ("EMUX-MIB-3XX", "muxGateway"),
        ("EMUX-MIB-3XX", "muxVLAN"),
        ("EMUX-MIB-3XX", "muxVLANPri"))
)
if mibBuilder.loadTexts:
    muxIpGroup.setStatus("current")

muxMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18, 2, 31, 5)
)
muxMgmtGroup.setObjects(
      *(("EMUX-MIB-3XX", "muxManagementLocal"),
        ("EMUX-MIB-3XX", "muxManagementGlobal"),
        ("EMUX-MIB-3XX", "muxTelnetAccess"),
        ("EMUX-MIB-3XX", "muxHTTPAccess"),
        ("EMUX-MIB-3XX", "muxFTPAccess"),
        ("EMUX-MIB-3XX", "muxMenuOnStart"),
        ("EMUX-MIB-3XX", "muxStoreCfg"))
)
if mibBuilder.loadTexts:
    muxMgmtGroup.setStatus("current")

muxSNMPAccessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18, 2, 31, 6)
)
muxSNMPAccessGroup.setObjects(
    ("EMUX-MIB-3XX", "muxSNMPAccess")
)
if mibBuilder.loadTexts:
    muxSNMPAccessGroup.setStatus("current")

muxRSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18, 2, 31, 7)
)
muxRSGroup.setObjects(
      *(("EMUX-MIB-3XX", "muxRSBaudRate"),
        ("EMUX-MIB-3XX", "muxRSStopBits"),
        ("EMUX-MIB-3XX", "muxRSParity"),
        ("EMUX-MIB-3XX", "muxRSEnable"))
)
if mibBuilder.loadTexts:
    muxRSGroup.setStatus("current")

muxMgmtIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18, 2, 31, 8)
)
muxMgmtIpGroup.setObjects(
      *(("EMUX-MIB-3XX", "muxManagementIP1"),
        ("EMUX-MIB-3XX", "muxManagementIP2"),
        ("EMUX-MIB-3XX", "muxManagementIP3"),
        ("EMUX-MIB-3XX", "muxManagementIP4"),
        ("EMUX-MIB-3XX", "muxManagementIP5"),
        ("EMUX-MIB-3XX", "muxManagementIP6"),
        ("EMUX-MIB-3XX", "muxManagementIP7"),
        ("EMUX-MIB-3XX", "muxManagementIP8"),
        ("EMUX-MIB-3XX", "muxManagementIP9"),
        ("EMUX-MIB-3XX", "muxManagementIP10"),
        ("EMUX-MIB-3XX", "muxManagementIP11"),
        ("EMUX-MIB-3XX", "muxManagementIP12"),
        ("EMUX-MIB-3XX", "muxManagementIP13"),
        ("EMUX-MIB-3XX", "muxManagementIP14"),
        ("EMUX-MIB-3XX", "muxManagementIP15"),
        ("EMUX-MIB-3XX", "muxManagementIP16"),
        ("EMUX-MIB-3XX", "muxManagementIP17"),
        ("EMUX-MIB-3XX", "muxManagementIP18"),
        ("EMUX-MIB-3XX", "muxManagementIP19"),
        ("EMUX-MIB-3XX", "muxManagementIP20"),
        ("EMUX-MIB-3XX", "muxManagementIP21"),
        ("EMUX-MIB-3XX", "muxManagementIP22"),
        ("EMUX-MIB-3XX", "muxManagementIP23"),
        ("EMUX-MIB-3XX", "muxManagementIP24"),
        ("EMUX-MIB-3XX", "muxManagementIP25"),
        ("EMUX-MIB-3XX", "muxManagementIP26"),
        ("EMUX-MIB-3XX", "muxManagementIP27"),
        ("EMUX-MIB-3XX", "muxManagementIP28"),
        ("EMUX-MIB-3XX", "muxManagementIP29"),
        ("EMUX-MIB-3XX", "muxManagementIP30"),
        ("EMUX-MIB-3XX", "muxManagementIP31"),
        ("EMUX-MIB-3XX", "muxManagementIP32"))
)
if mibBuilder.loadTexts:
    muxMgmtIpGroup.setStatus("current")

muxMgmtMaskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18, 2, 31, 9)
)
muxMgmtMaskGroup.setObjects(
      *(("EMUX-MIB-3XX", "muxManagementMask1"),
        ("EMUX-MIB-3XX", "muxManagementMask2"),
        ("EMUX-MIB-3XX", "muxManagementMask3"),
        ("EMUX-MIB-3XX", "muxManagementMask4"),
        ("EMUX-MIB-3XX", "muxManagementMask5"),
        ("EMUX-MIB-3XX", "muxManagementMask6"),
        ("EMUX-MIB-3XX", "muxManagementMask7"),
        ("EMUX-MIB-3XX", "muxManagementMask8"),
        ("EMUX-MIB-3XX", "muxManagementMask9"),
        ("EMUX-MIB-3XX", "muxManagementMask10"),
        ("EMUX-MIB-3XX", "muxManagementMask11"),
        ("EMUX-MIB-3XX", "muxManagementMask12"),
        ("EMUX-MIB-3XX", "muxManagementMask13"),
        ("EMUX-MIB-3XX", "muxManagementMask14"),
        ("EMUX-MIB-3XX", "muxManagementMask15"),
        ("EMUX-MIB-3XX", "muxManagementMask16"),
        ("EMUX-MIB-3XX", "muxManagementMask17"),
        ("EMUX-MIB-3XX", "muxManagementMask18"),
        ("EMUX-MIB-3XX", "muxManagementMask19"),
        ("EMUX-MIB-3XX", "muxManagementMask20"),
        ("EMUX-MIB-3XX", "muxManagementMask21"),
        ("EMUX-MIB-3XX", "muxManagementMask22"),
        ("EMUX-MIB-3XX", "muxManagementMask23"),
        ("EMUX-MIB-3XX", "muxManagementMask24"),
        ("EMUX-MIB-3XX", "muxManagementMask25"),
        ("EMUX-MIB-3XX", "muxManagementMask26"),
        ("EMUX-MIB-3XX", "muxManagementMask27"),
        ("EMUX-MIB-3XX", "muxManagementMask28"),
        ("EMUX-MIB-3XX", "muxManagementMask29"),
        ("EMUX-MIB-3XX", "muxManagementMask30"),
        ("EMUX-MIB-3XX", "muxManagementMask31"),
        ("EMUX-MIB-3XX", "muxManagementMask32"))
)
if mibBuilder.loadTexts:
    muxMgmtMaskGroup.setStatus("current")

muxEthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18, 2, 31, 10)
)
muxEthGroup.setObjects(
      *(("EMUX-MIB-3XX", "ethType"),
        ("EMUX-MIB-3XX", "ethMode"),
        ("EMUX-MIB-3XX", "ethReservMode"),
        ("EMUX-MIB-3XX", "ethVlan"),
        ("EMUX-MIB-3XX", "ethDuplexMode"),
        ("EMUX-MIB-3XX", "ethStringStatus"),
        ("EMUX-MIB-3XX", "ethLogLevel"),
        ("EMUX-MIB-3XX", "ethTrapLevel"),
        ("EMUX-MIB-3XX", "ethIngressRateLimit"),
        ("EMUX-MIB-3XX", "ethSecurity"),
        ("EMUX-MIB-3XX", "ethMonitorPort"),
        ("EMUX-MIB-3XX", "ethTrunkId"),
        ("EMUX-MIB-3XX", "ethPriorityMode"),
        ("EMUX-MIB-3XX", "ethDefaultPriority"),
        ("EMUX-MIB-3XX", "ethEgressRateLimit"),
        ("EMUX-MIB-3XX", "ethRateLimitMode"),
        ("EMUX-MIB-3XX", "ethIGMPsnooping"),
        ("EMUX-MIB-3XX", "ethCurrentStat"),
        ("EMUX-MIB-3XX", "ethMaxLearnNum"),
        ("EMUX-MIB-3XX", "ethDHCPrelay"),
        ("EMUX-MIB-3XX", "ethDHCPtrusted"),
        ("EMUX-MIB-3XX", "ethIGMPfastleave"),
        ("EMUX-MIB-3XX", "ethMVRtype"),
        ("EMUX-MIB-3XX", "ethUserport"),
        ("EMUX-MIB-3XX", "ethForceVlan"),
        ("EMUX-MIB-3XX", "ethResetStat"),
        ("EMUX-MIB-3XX", "ethStateInternal"))
)
if mibBuilder.loadTexts:
    muxEthGroup.setStatus("current")

muxRSTPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18, 2, 31, 11)
)
muxRSTPGroup.setObjects(
      *(("EMUX-MIB-3XX", "rSTPForwardDelay"),
        ("EMUX-MIB-3XX", "rSTPMaxAge"),
        ("EMUX-MIB-3XX", "rSTPHelloTime"),
        ("EMUX-MIB-3XX", "rSTPBridgePrio"))
)
if mibBuilder.loadTexts:
    muxRSTPGroup.setStatus("current")

muxRSTPInterfacesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18, 2, 31, 12)
)
muxRSTPInterfacesGroup.setObjects(
      *(("EMUX-MIB-3XX", "rSTPPortPrio"),
        ("EMUX-MIB-3XX", "rSTPEdge"),
        ("EMUX-MIB-3XX", "rSTPPathCost"),
        ("EMUX-MIB-3XX", "rSTPp2p"),
        ("EMUX-MIB-3XX", "rSTPRootGuard"),
        ("EMUX-MIB-3XX", "rSTPState"),
        ("EMUX-MIB-3XX", "rSTPRole"))
)
if mibBuilder.loadTexts:
    muxRSTPInterfacesGroup.setStatus("current")

muxMaintenanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18, 2, 31, 13)
)
muxMaintenanceGroup.setObjects(
    ("EMUX-MIB-3XX", "sysReset")
)
if mibBuilder.loadTexts:
    muxMaintenanceGroup.setStatus("current")

muxE1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18, 2, 31, 14)
)
muxE1Group.setObjects(
      *(("EMUX-MIB-3XX", "e1SubChIndex"),
        ("EMUX-MIB-3XX", "e1aMode"),
        ("EMUX-MIB-3XX", "e1aSetupPayload"),
        ("EMUX-MIB-3XX", "e1aSetupJBuf"),
        ("EMUX-MIB-3XX", "e1aSetupGap"),
        ("EMUX-MIB-3XX", "e1ProtLevel"),
        ("EMUX-MIB-3XX", "e1Vlan"),
        ("EMUX-MIB-3XX", "e1VlanPri"),
        ("EMUX-MIB-3XX", "e1ToS"),
        ("EMUX-MIB-3XX", "e1DstChannel"),
        ("EMUX-MIB-3XX", "e1DstMAC"),
        ("EMUX-MIB-3XX", "e1DstIP"),
        ("EMUX-MIB-3XX", "e1Leds"),
        ("EMUX-MIB-3XX", "e1Framed"),
        ("EMUX-MIB-3XX", "e1Description"),
        ("EMUX-MIB-3XX", "e1TestStatus"),
        ("EMUX-MIB-3XX", "e1LogLevel"),
        ("EMUX-MIB-3XX", "e1TrapLevel"),
        ("EMUX-MIB-3XX", "e1AvgTime"),
        ("EMUX-MIB-3XX", "e1DstMask"),
        ("EMUX-MIB-3XX", "e1DstSubchIndex"),
        ("EMUX-MIB-3XX", "e1DstTextMask"),
        ("EMUX-MIB-3XX", "e1aUptime"),
        ("EMUX-MIB-3XX", "e1lState"),
        ("EMUX-MIB-3XX", "e1rState"),
        ("EMUX-MIB-3XX", "e1sMask"),
        ("EMUX-MIB-3XX", "e1stMask"),
        ("EMUX-MIB-3XX", "e1SubchNum"),
        ("EMUX-MIB-3XX", "e1Compression"),
        ("EMUX-MIB-3XX", "e1CompressTime"),
        ("EMUX-MIB-3XX", "e1LIUstate"),
        ("EMUX-MIB-3XX", "e1GatewayBypass"),
        ("EMUX-MIB-3XX", "e1OutFreq"),
        ("EMUX-MIB-3XX", "e1LeftSlip"),
        ("EMUX-MIB-3XX", "e1RightSlip"),
        ("EMUX-MIB-3XX", "usedTimeSlots"),
        ("EMUX-MIB-3XX", "liuStat"),
        ("EMUX-MIB-3XX", "pktStat"),
        ("EMUX-MIB-3XX", "stateStat"),
        ("EMUX-MIB-3XX", "e1LeftSlipPkt"),
        ("EMUX-MIB-3XX", "e1RightSlipPkt"),
        ("EMUX-MIB-3XX", "timeStat"),
        ("EMUX-MIB-3XX", "resetStat"),
        ("EMUX-MIB-3XX", "saveStat"),
        ("EMUX-MIB-3XX", "e1fstate"),
        ("EMUX-MIB-3XX", "spregMode"),
        ("EMUX-MIB-3XX", "spregQueueSize"),
        ("EMUX-MIB-3XX", "recoveryLost"),
        ("EMUX-MIB-3XX", "v5SignalLabel"),
        ("EMUX-MIB-3XX", "v5SignalLabelText"),
        ("EMUX-MIB-3XX", "e1IfIndex"),
        ("EMUX-MIB-3XX", "e1WanIP"),
        ("EMUX-MIB-3XX", "e1RemoteSIPPort"),
        ("EMUX-MIB-3XX", "e1RemoteTDMPort"),
        ("EMUX-MIB-3XX", "e1UsedTimeslotsCount"))
)
if mibBuilder.loadTexts:
    muxE1Group.setStatus("current")

lldpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18, 2, 33, 1)
)
lldpConfigGroup.setObjects(
    ("EMUX-MIB-3XX", "lldpPortConfigAdminStatus")
)
if mibBuilder.loadTexts:
    lldpConfigGroup.setStatus("current")

lldpConfigTxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18, 2, 33, 3)
)
lldpConfigTxGroup.setObjects(
      *(("EMUX-MIB-3XX", "lldpMessageTxInterval"),
        ("EMUX-MIB-3XX", "lldpMessageTxHoldMultiplier"),
        ("EMUX-MIB-3XX", "lldpPortConfigTLVsTxEnable"))
)
if mibBuilder.loadTexts:
    lldpConfigTxGroup.setStatus("current")

lldpRemSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18, 2, 33, 7)
)
lldpRemSysGroup.setObjects(
      *(("EMUX-MIB-3XX", "lldpRemChassisIdSubtype"),
        ("EMUX-MIB-3XX", "lldpRemChassisId"),
        ("EMUX-MIB-3XX", "lldpRemPortIdSubtype"),
        ("EMUX-MIB-3XX", "lldpRemPortId"),
        ("EMUX-MIB-3XX", "lldpRemPortDesc"),
        ("EMUX-MIB-3XX", "lldpRemSysName"),
        ("EMUX-MIB-3XX", "lldpRemSysDesc"))
)
if mibBuilder.loadTexts:
    lldpRemSysGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

emuxCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 18, 2, 30, 30)
)
emuxCompliance.setObjects(
      *(("EMUX-MIB-3XX", "muxBaseGroup"),
        ("EMUX-MIB-3XX", "muxSensorGroup"),
        ("EMUX-MIB-3XX", "muxDateTimeGroup"),
        ("EMUX-MIB-3XX", "muxIpGroup"),
        ("EMUX-MIB-3XX", "muxMgmtGroup"),
        ("EMUX-MIB-3XX", "muxSNMPAccessGroup"),
        ("EMUX-MIB-3XX", "muxRSGroup"),
        ("EMUX-MIB-3XX", "muxMgmtIpGroup"),
        ("EMUX-MIB-3XX", "muxMgmtMaskGroup"),
        ("EMUX-MIB-3XX", "muxEthGroup"),
        ("EMUX-MIB-3XX", "muxRSTPGroup"),
        ("EMUX-MIB-3XX", "muxRSTPInterfacesGroup"),
        ("EMUX-MIB-3XX", "muxMaintenanceGroup"),
        ("EMUX-MIB-3XX", "muxE1Group"))
)
if mibBuilder.loadTexts:
    emuxCompliance.setStatus(
        "current"
    )

lldpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 18, 2, 32, 1)
)
lldpCompliance.setObjects(
    ("EMUX-MIB-3XX", "lldpConfigGroup")
)
if mibBuilder.loadTexts:
    lldpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EMUX-MIB-3XX",
    **{"SnmpAdminString": SnmpAdminString,
       "LldpChassisIdSubtype": LldpChassisIdSubtype,
       "LldpChassisId": LldpChassisId,
       "LldpPortIdSubtype": LldpPortIdSubtype,
       "LldpPortId": LldpPortId,
       "LldpManAddrIfSubtype": LldpManAddrIfSubtype,
       "LldpManAddress": LldpManAddress,
       "LldpPortNumber": LldpPortNumber,
       "LldpPortList": LldpPortList,
       "nsc": nsc,
       "emux": emux,
       "muxgeneral": muxgeneral,
       "basicInfo": basicInfo,
       "hardwareVersion": hardwareVersion,
       "fwVersion": fwVersion,
       "softwareVersion": softwareVersion,
       "bootloaderVersion": bootloaderVersion,
       "systemID": systemID,
       "powerVoltage": powerVoltage,
       "caseTemperature": caseTemperature,
       "envVer": envVer,
       "accVoltage": accVoltage,
       "currentConsumption": currentConsumption,
       "muxSensor": muxSensor,
       "sensor1": sensor1,
       "sensor2": sensor2,
       "sensor3": sensor3,
       "muxDateTime": muxDateTime,
       "muxDate": muxDate,
       "muxTime": muxTime,
       "muxTimeZone": muxTimeZone,
       "muxTimeServer": muxTimeServer,
       "muxTimeSynchro": muxTimeSynchro,
       "muxTimeNextSynchro": muxTimeNextSynchro,
       "muxTimeSynchroPeriod": muxTimeSynchroPeriod,
       "muxIP": muxIP,
       "muxMAC": muxMAC,
       "muxIPaddr": muxIPaddr,
       "muxMask": muxMask,
       "muxGateway": muxGateway,
       "muxVLAN": muxVLAN,
       "muxVLANPri": muxVLANPri,
       "muxMan": muxMan,
       "muxManagementLocal": muxManagementLocal,
       "muxManagementGlobal": muxManagementGlobal,
       "muxTelnetAccess": muxTelnetAccess,
       "muxHTTPAccess": muxHTTPAccess,
       "muxSNMP": muxSNMP,
       "muxSNMPAccess": muxSNMPAccess,
       "muxFTPAccess": muxFTPAccess,
       "muxMenuOnStart": muxMenuOnStart,
       "muxStoreCfg": muxStoreCfg,
       "muxRS": muxRS,
       "muxRSBaudRate": muxRSBaudRate,
       "muxRSStopBits": muxRSStopBits,
       "muxRSParity": muxRSParity,
       "muxRSEnable": muxRSEnable,
       "muxManIP": muxManIP,
       "muxManagementIP1": muxManagementIP1,
       "muxManagementIP2": muxManagementIP2,
       "muxManagementIP3": muxManagementIP3,
       "muxManagementIP4": muxManagementIP4,
       "muxManagementIP5": muxManagementIP5,
       "muxManagementIP6": muxManagementIP6,
       "muxManagementIP7": muxManagementIP7,
       "muxManagementIP8": muxManagementIP8,
       "muxManagementIP9": muxManagementIP9,
       "muxManagementIP10": muxManagementIP10,
       "muxManagementIP11": muxManagementIP11,
       "muxManagementIP12": muxManagementIP12,
       "muxManagementIP13": muxManagementIP13,
       "muxManagementIP14": muxManagementIP14,
       "muxManagementIP15": muxManagementIP15,
       "muxManagementIP16": muxManagementIP16,
       "muxManagementIP17": muxManagementIP17,
       "muxManagementIP18": muxManagementIP18,
       "muxManagementIP19": muxManagementIP19,
       "muxManagementIP20": muxManagementIP20,
       "muxManagementIP21": muxManagementIP21,
       "muxManagementIP22": muxManagementIP22,
       "muxManagementIP23": muxManagementIP23,
       "muxManagementIP24": muxManagementIP24,
       "muxManagementIP25": muxManagementIP25,
       "muxManagementIP26": muxManagementIP26,
       "muxManagementIP27": muxManagementIP27,
       "muxManagementIP28": muxManagementIP28,
       "muxManagementIP29": muxManagementIP29,
       "muxManagementIP30": muxManagementIP30,
       "muxManagementIP31": muxManagementIP31,
       "muxManagementIP32": muxManagementIP32,
       "muxManMask": muxManMask,
       "muxManagementMask1": muxManagementMask1,
       "muxManagementMask2": muxManagementMask2,
       "muxManagementMask3": muxManagementMask3,
       "muxManagementMask4": muxManagementMask4,
       "muxManagementMask5": muxManagementMask5,
       "muxManagementMask6": muxManagementMask6,
       "muxManagementMask7": muxManagementMask7,
       "muxManagementMask8": muxManagementMask8,
       "muxManagementMask9": muxManagementMask9,
       "muxManagementMask10": muxManagementMask10,
       "muxManagementMask11": muxManagementMask11,
       "muxManagementMask12": muxManagementMask12,
       "muxManagementMask13": muxManagementMask13,
       "muxManagementMask14": muxManagementMask14,
       "muxManagementMask15": muxManagementMask15,
       "muxManagementMask16": muxManagementMask16,
       "muxManagementMask17": muxManagementMask17,
       "muxManagementMask18": muxManagementMask18,
       "muxManagementMask19": muxManagementMask19,
       "muxManagementMask20": muxManagementMask20,
       "muxManagementMask21": muxManagementMask21,
       "muxManagementMask22": muxManagementMask22,
       "muxManagementMask23": muxManagementMask23,
       "muxManagementMask24": muxManagementMask24,
       "muxManagementMask25": muxManagementMask25,
       "muxManagementMask26": muxManagementMask26,
       "muxManagementMask27": muxManagementMask27,
       "muxManagementMask28": muxManagementMask28,
       "muxManagementMask29": muxManagementMask29,
       "muxManagementMask30": muxManagementMask30,
       "muxManagementMask31": muxManagementMask31,
       "muxManagementMask32": muxManagementMask32,
       "ethTable": ethTable,
       "ethEntry": ethEntry,
       "ethType": ethType,
       "ethMode": ethMode,
       "ethReservMode": ethReservMode,
       "ethVlan": ethVlan,
       "ethDuplexMode": ethDuplexMode,
       "ethStringStatus": ethStringStatus,
       "ethLogLevel": ethLogLevel,
       "ethTrapLevel": ethTrapLevel,
       "ethIngressRateLimit": ethIngressRateLimit,
       "ethSecurity": ethSecurity,
       "ethMonitorPort": ethMonitorPort,
       "ethTrunkId": ethTrunkId,
       "ethPriorityMode": ethPriorityMode,
       "ethDefaultPriority": ethDefaultPriority,
       "ethEgressRateLimit": ethEgressRateLimit,
       "ethRateLimitMode": ethRateLimitMode,
       "ethIGMPsnooping": ethIGMPsnooping,
       "ethCurrentStat": ethCurrentStat,
       "ethMaxLearnNum": ethMaxLearnNum,
       "ethDHCPrelay": ethDHCPrelay,
       "ethDHCPtrusted": ethDHCPtrusted,
       "ethIGMPfastleave": ethIGMPfastleave,
       "ethMVRtype": ethMVRtype,
       "ethUserport": ethUserport,
       "ethForceVlan": ethForceVlan,
       "ethResetStat": ethResetStat,
       "ethStateInternal": ethStateInternal,
       "e1Old1": e1Old1,
       "e1Old2": e1Old2,
       "branchSysReset": branchSysReset,
       "subBranchSysReset": subBranchSysReset,
       "sysReset": sysReset,
       "muxRSTP": muxRSTP,
       "rSTPForwardDelay": rSTPForwardDelay,
       "rSTPMaxAge": rSTPMaxAge,
       "rSTPHelloTime": rSTPHelloTime,
       "rSTPBridgePrio": rSTPBridgePrio,
       "rSTPTable": rSTPTable,
       "rSTPEntry": rSTPEntry,
       "rSTPPortPrio": rSTPPortPrio,
       "rSTPEdge": rSTPEdge,
       "rSTPPathCost": rSTPPathCost,
       "rSTPp2p": rSTPp2p,
       "rSTPRootGuard": rSTPRootGuard,
       "rSTPState": rSTPState,
       "rSTPRole": rSTPRole,
       "lldpMib": lldpMib,
       "lldpObjects": lldpObjects,
       "lldpConfiguration": lldpConfiguration,
       "lldpMessageTxInterval": lldpMessageTxInterval,
       "lldpMessageTxHoldMultiplier": lldpMessageTxHoldMultiplier,
       "lldpPortConfigTable": lldpPortConfigTable,
       "lldpPortConfigEntry": lldpPortConfigEntry,
       "lldpPortConfigPortNum": lldpPortConfigPortNum,
       "lldpPortConfigAdminStatus": lldpPortConfigAdminStatus,
       "lldpPortConfigTLVsTxEnable": lldpPortConfigTLVsTxEnable,
       "lldpRemoteSystemsData": lldpRemoteSystemsData,
       "lldpRemTable": lldpRemTable,
       "lldpRemEntry": lldpRemEntry,
       "lldpRemTimeMark": lldpRemTimeMark,
       "lldpRemLocalPortNum": lldpRemLocalPortNum,
       "lldpRemIndex": lldpRemIndex,
       "lldpRemChassisIdSubtype": lldpRemChassisIdSubtype,
       "lldpRemChassisId": lldpRemChassisId,
       "lldpRemPortIdSubtype": lldpRemPortIdSubtype,
       "lldpRemPortId": lldpRemPortId,
       "lldpRemPortDesc": lldpRemPortDesc,
       "lldpRemSysName": lldpRemSysName,
       "lldpRemSysDesc": lldpRemSysDesc,
       "lldpRemManAddrSubtype": lldpRemManAddrSubtype,
       "lldpRemManAddr": lldpRemManAddr,
       "lldpRemManAddrStr": lldpRemManAddrStr,
       "lldpRemDataValid": lldpRemDataValid,
       "e1SubChTable": e1SubChTable,
       "e1SubChEntry": e1SubChEntry,
       "e1SubChIndex": e1SubChIndex,
       "e1aMode": e1aMode,
       "e1aSetupPayload": e1aSetupPayload,
       "e1aSetupJBuf": e1aSetupJBuf,
       "e1aSetupGap": e1aSetupGap,
       "e1ProtLevel": e1ProtLevel,
       "e1Vlan": e1Vlan,
       "e1VlanPri": e1VlanPri,
       "e1ToS": e1ToS,
       "e1DstChannel": e1DstChannel,
       "e1DstMAC": e1DstMAC,
       "e1DstIP": e1DstIP,
       "e1Leds": e1Leds,
       "e1Framed": e1Framed,
       "e1Description": e1Description,
       "e1TestStatus": e1TestStatus,
       "e1LogLevel": e1LogLevel,
       "e1TrapLevel": e1TrapLevel,
       "e1AvgTime": e1AvgTime,
       "e1DstMask": e1DstMask,
       "e1DstSubchIndex": e1DstSubchIndex,
       "e1DstTextMask": e1DstTextMask,
       "e1aUptime": e1aUptime,
       "e1lState": e1lState,
       "e1rState": e1rState,
       "e1sMask": e1sMask,
       "e1stMask": e1stMask,
       "e1SubchNum": e1SubchNum,
       "e1Compression": e1Compression,
       "e1CompressTime": e1CompressTime,
       "e1LIUstate": e1LIUstate,
       "e1GatewayBypass": e1GatewayBypass,
       "e1OutFreq": e1OutFreq,
       "e1LeftSlip": e1LeftSlip,
       "e1RightSlip": e1RightSlip,
       "e1LeftSlipPkt": e1LeftSlipPkt,
       "e1RightSlipPkt": e1RightSlipPkt,
       "usedTimeSlots": usedTimeSlots,
       "liuStat": liuStat,
       "pktStat": pktStat,
       "stateStat": stateStat,
       "timeStat": timeStat,
       "resetStat": resetStat,
       "saveStat": saveStat,
       "e1fstate": e1fstate,
       "spregMode": spregMode,
       "spregQueueSize": spregQueueSize,
       "recoveryLost": recoveryLost,
       "v5SignalLabel": v5SignalLabel,
       "v5SignalLabelText": v5SignalLabelText,
       "e1IfIndex": e1IfIndex,
       "e1WanIP": e1WanIP,
       "e1RemoteSIPPort": e1RemoteSIPPort,
       "e1RemoteTDMPort": e1RemoteTDMPort,
       "e1UsedTimeslotsCount": e1UsedTimeslotsCount,
       "muxCompliances": muxCompliances,
       "emuxCompliance": emuxCompliance,
       "muxGroups": muxGroups,
       "muxBaseGroup": muxBaseGroup,
       "muxSensorGroup": muxSensorGroup,
       "muxDateTimeGroup": muxDateTimeGroup,
       "muxIpGroup": muxIpGroup,
       "muxMgmtGroup": muxMgmtGroup,
       "muxSNMPAccessGroup": muxSNMPAccessGroup,
       "muxRSGroup": muxRSGroup,
       "muxMgmtIpGroup": muxMgmtIpGroup,
       "muxMgmtMaskGroup": muxMgmtMaskGroup,
       "muxEthGroup": muxEthGroup,
       "muxRSTPGroup": muxRSTPGroup,
       "muxRSTPInterfacesGroup": muxRSTPInterfacesGroup,
       "muxMaintenanceGroup": muxMaintenanceGroup,
       "muxE1Group": muxE1Group,
       "lldpCompliances": lldpCompliances,
       "lldpCompliance": lldpCompliance,
       "lldpGroups": lldpGroups,
       "lldpConfigGroup": lldpConfigGroup,
       "lldpConfigTxGroup": lldpConfigTxGroup,
       "lldpRemSysGroup": lldpRemSysGroup,
       "muxExtended": muxExtended,
       "leds": leds,
       "systemLed": systemLed,
       "ctrlLed": ctrlLed,
       "ctrlAlarm": ctrlAlarm,
       "ctrlAlarmReset": ctrlAlarmReset}
)
