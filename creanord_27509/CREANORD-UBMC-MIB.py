# SNMP MIB module (CREANORD-UBMC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/creanord_27509/CREANORD-UBMC-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:58:49 2025
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

(creanordRoot,) = mibBuilder.importSymbols(
    "CREANORD-MIB",
    "creanordRoot")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ubmc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27509, 3)
)
if mibBuilder.loadTexts:
    ubmc.setRevisions(
        ("2021-02-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SystemStatus_ObjectIdentity = ObjectIdentity
systemStatus = _SystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1)
)


class _DeviceType_Type(Integer32):
    """Custom type deviceType based on Integer32"""
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
        *(("unknown", 0),
          ("ubmc-xs", 1),
          ("ubmc-small", 2),
          ("ubmc-medium", 3),
          ("ubmc-large", 4))
    )


_DeviceType_Type.__name__ = "Integer32"
_DeviceType_Object = MibScalar
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 1),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("current")


class _DeviceSerialNumber_Type(OctetString):
    """Custom type deviceSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_DeviceSerialNumber_Type.__name__ = "OctetString"
_DeviceSerialNumber_Object = MibScalar
deviceSerialNumber = _DeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 2),
    _DeviceSerialNumber_Type()
)
deviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSerialNumber.setStatus("current")


class _HardwareVersion_Type(OctetString):
    """Custom type hardwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HardwareVersion_Type.__name__ = "OctetString"
_HardwareVersion_Object = MibScalar
hardwareVersion = _HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 3),
    _HardwareVersion_Type()
)
hardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareVersion.setStatus("current")


class _FirmwareVersion_Type(OctetString):
    """Custom type firmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FirmwareVersion_Type.__name__ = "OctetString"
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 4),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")


class _SoftwareVersion_Type(OctetString):
    """Custom type softwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SoftwareVersion_Type.__name__ = "OctetString"
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 5),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("current")


class _UbootVersion_Type(OctetString):
    """Custom type ubootVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_UbootVersion_Type.__name__ = "OctetString"
_UbootVersion_Object = MibScalar
ubootVersion = _UbootVersion_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 6),
    _UbootVersion_Type()
)
ubootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubootVersion.setStatus("current")


class _SystemUptime_Type(OctetString):
    """Custom type systemUptime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SystemUptime_Type.__name__ = "OctetString"
_SystemUptime_Object = MibScalar
systemUptime = _SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 7),
    _SystemUptime_Type()
)
systemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUptime.setStatus("current")
_HostFanTable_Object = MibTable
hostFanTable = _HostFanTable_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 10)
)
if mibBuilder.loadTexts:
    hostFanTable.setStatus("current")
_HostFanEntry_Object = MibTableRow
hostFanEntry = _HostFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 10, 1)
)
hostFanEntry.setIndexNames(
    (0, "CREANORD-UBMC-MIB", "hostFanID"),
)
if mibBuilder.loadTexts:
    hostFanEntry.setStatus("current")


class _HostFanID_Type(Integer32):
    """Custom type hostFanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HostFanID_Type.__name__ = "Integer32"
_HostFanID_Object = MibTableColumn
hostFanID = _HostFanID_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 10, 1, 1),
    _HostFanID_Type()
)
hostFanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostFanID.setStatus("current")


class _HostFanName_Type(OctetString):
    """Custom type hostFanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HostFanName_Type.__name__ = "OctetString"
_HostFanName_Object = MibTableColumn
hostFanName = _HostFanName_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 10, 1, 2),
    _HostFanName_Type()
)
hostFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostFanName.setStatus("current")


class _HostFanFault_Type(Integer32):
    """Custom type hostFanFault based on Integer32"""
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


_HostFanFault_Type.__name__ = "Integer32"
_HostFanFault_Object = MibTableColumn
hostFanFault = _HostFanFault_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 10, 1, 3),
    _HostFanFault_Type()
)
hostFanFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostFanFault.setStatus("current")


class _HostFanWarning_Type(Integer32):
    """Custom type hostFanWarning based on Integer32"""
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


_HostFanWarning_Type.__name__ = "Integer32"
_HostFanWarning_Object = MibTableColumn
hostFanWarning = _HostFanWarning_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 10, 1, 4),
    _HostFanWarning_Type()
)
hostFanWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostFanWarning.setStatus("current")


class _HostFanStatus_Type(Integer32):
    """Custom type hostFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("green", 1),
          ("yellow", 2),
          ("orange", 4),
          ("red", 8))
    )


_HostFanStatus_Type.__name__ = "Integer32"
_HostFanStatus_Object = MibTableColumn
hostFanStatus = _HostFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 10, 1, 5),
    _HostFanStatus_Type()
)
hostFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostFanStatus.setStatus("current")
_HostFanSpeed_Type = Integer32
_HostFanSpeed_Object = MibTableColumn
hostFanSpeed = _HostFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 10, 1, 6),
    _HostFanSpeed_Type()
)
hostFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostFanSpeed.setStatus("current")
_HostFanRuntime_Type = Integer32
_HostFanRuntime_Object = MibTableColumn
hostFanRuntime = _HostFanRuntime_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 10, 1, 7),
    _HostFanRuntime_Type()
)
hostFanRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostFanRuntime.setStatus("current")
_HostSensorTable_Object = MibTable
hostSensorTable = _HostSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 11)
)
if mibBuilder.loadTexts:
    hostSensorTable.setStatus("current")
_HostSensorEntry_Object = MibTableRow
hostSensorEntry = _HostSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 11, 1)
)
hostSensorEntry.setIndexNames(
    (0, "CREANORD-UBMC-MIB", "hostSensorID"),
)
if mibBuilder.loadTexts:
    hostSensorEntry.setStatus("current")


class _HostSensorID_Type(Integer32):
    """Custom type hostSensorID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HostSensorID_Type.__name__ = "Integer32"
_HostSensorID_Object = MibTableColumn
hostSensorID = _HostSensorID_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 11, 1, 1),
    _HostSensorID_Type()
)
hostSensorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSensorID.setStatus("current")


class _HostSensorName_Type(OctetString):
    """Custom type hostSensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HostSensorName_Type.__name__ = "OctetString"
_HostSensorName_Object = MibTableColumn
hostSensorName = _HostSensorName_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 11, 1, 2),
    _HostSensorName_Type()
)
hostSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSensorName.setStatus("current")
_HostSensorTemperature_Type = OctetString
_HostSensorTemperature_Object = MibTableColumn
hostSensorTemperature = _HostSensorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 11, 1, 3),
    _HostSensorTemperature_Type()
)
hostSensorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSensorTemperature.setStatus("current")
_HostSensorPeak_Type = OctetString
_HostSensorPeak_Object = MibTableColumn
hostSensorPeak = _HostSensorPeak_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 11, 1, 4),
    _HostSensorPeak_Type()
)
hostSensorPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSensorPeak.setStatus("current")
_HostVoltageTable_Object = MibTable
hostVoltageTable = _HostVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 12)
)
if mibBuilder.loadTexts:
    hostVoltageTable.setStatus("current")
_HostVoltageEntry_Object = MibTableRow
hostVoltageEntry = _HostVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 12, 1)
)
hostVoltageEntry.setIndexNames(
    (0, "CREANORD-UBMC-MIB", "hostVoltageID"),
)
if mibBuilder.loadTexts:
    hostVoltageEntry.setStatus("current")


class _HostVoltageID_Type(Integer32):
    """Custom type hostVoltageID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HostVoltageID_Type.__name__ = "Integer32"
_HostVoltageID_Object = MibTableColumn
hostVoltageID = _HostVoltageID_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 12, 1, 1),
    _HostVoltageID_Type()
)
hostVoltageID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostVoltageID.setStatus("current")


class _HostVoltageName_Type(OctetString):
    """Custom type hostVoltageName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HostVoltageName_Type.__name__ = "OctetString"
_HostVoltageName_Object = MibTableColumn
hostVoltageName = _HostVoltageName_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 12, 1, 2),
    _HostVoltageName_Type()
)
hostVoltageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostVoltageName.setStatus("current")
_HostVoltage_Type = OctetString
_HostVoltage_Object = MibTableColumn
hostVoltage = _HostVoltage_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 12, 1, 3),
    _HostVoltage_Type()
)
hostVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostVoltage.setStatus("current")
_InterfaceTable_Object = MibTable
interfaceTable = _InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 13)
)
if mibBuilder.loadTexts:
    interfaceTable.setStatus("current")
_InterfaceEntry_Object = MibTableRow
interfaceEntry = _InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 13, 1)
)
interfaceEntry.setIndexNames(
    (0, "CREANORD-UBMC-MIB", "interfaceName"),
)
if mibBuilder.loadTexts:
    interfaceEntry.setStatus("current")


class _InterfaceName_Type(OctetString):
    """Custom type interfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_InterfaceName_Type.__name__ = "OctetString"
_InterfaceName_Object = MibTableColumn
interfaceName = _InterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 13, 1, 1),
    _InterfaceName_Type()
)
interfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceName.setStatus("current")


class _InterfaceLinkStatus_Type(Integer32):
    """Custom type interfaceLinkStatus based on Integer32"""
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


_InterfaceLinkStatus_Type.__name__ = "Integer32"
_InterfaceLinkStatus_Object = MibTableColumn
interfaceLinkStatus = _InterfaceLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 1, 13, 1, 2),
    _InterfaceLinkStatus_Type()
)
interfaceLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceLinkStatus.setStatus("current")
_SystemStatictis_ObjectIdentity = ObjectIdentity
systemStatictis = _SystemStatictis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27509, 3, 2)
)
_InfStatisticsTable_Object = MibTable
infStatisticsTable = _InfStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 2, 1)
)
if mibBuilder.loadTexts:
    infStatisticsTable.setStatus("current")
_InfStatisticsEntry_Object = MibTableRow
infStatisticsEntry = _InfStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 2, 1, 1)
)
infStatisticsEntry.setIndexNames(
    (0, "CREANORD-UBMC-MIB", "infName"),
)
if mibBuilder.loadTexts:
    infStatisticsEntry.setStatus("current")


class _InfName_Type(OctetString):
    """Custom type infName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_InfName_Type.__name__ = "OctetString"
_InfName_Object = MibTableColumn
infName = _InfName_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 2, 1, 1, 1),
    _InfName_Type()
)
infName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infName.setStatus("current")
_InfRxPkts_Type = Counter64
_InfRxPkts_Object = MibTableColumn
infRxPkts = _InfRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 2, 1, 1, 2),
    _InfRxPkts_Type()
)
infRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infRxPkts.setStatus("current")
_InfRxErrors_Type = Counter64
_InfRxErrors_Object = MibTableColumn
infRxErrors = _InfRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 2, 1, 1, 3),
    _InfRxErrors_Type()
)
infRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infRxErrors.setStatus("current")
_InfRxDrops_Type = Counter64
_InfRxDrops_Object = MibTableColumn
infRxDrops = _InfRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 2, 1, 1, 4),
    _InfRxDrops_Type()
)
infRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infRxDrops.setStatus("current")
_InfRxBytes_Type = Counter64
_InfRxBytes_Object = MibTableColumn
infRxBytes = _InfRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 2, 1, 1, 5),
    _InfRxBytes_Type()
)
infRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infRxBytes.setStatus("current")
_InfTxPkts_Type = Counter64
_InfTxPkts_Object = MibTableColumn
infTxPkts = _InfTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 2, 1, 1, 6),
    _InfTxPkts_Type()
)
infTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infTxPkts.setStatus("current")
_InfTxErrors_Type = Counter64
_InfTxErrors_Object = MibTableColumn
infTxErrors = _InfTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 2, 1, 1, 7),
    _InfTxErrors_Type()
)
infTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infTxErrors.setStatus("current")
_InfTxDrops_Type = Counter64
_InfTxDrops_Object = MibTableColumn
infTxDrops = _InfTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 2, 1, 1, 8),
    _InfTxDrops_Type()
)
infTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infTxDrops.setStatus("current")
_InfTxBytes_Type = Counter64
_InfTxBytes_Object = MibTableColumn
infTxBytes = _InfTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 2, 1, 1, 9),
    _InfTxBytes_Type()
)
infTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infTxBytes.setStatus("current")
_SystemConfig_ObjectIdentity = ObjectIdentity
systemConfig = _SystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27509, 3, 3)
)
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11)
)
_TrapObject_ObjectIdentity = ObjectIdentity
trapObject = _TrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 0)
)


class _TrapModule_Type(OctetString):
    """Custom type trapModule based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TrapModule_Type.__name__ = "OctetString"
_TrapModule_Object = MibScalar
trapModule = _TrapModule_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 0, 1),
    _TrapModule_Type()
)
trapModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapModule.setStatus("current")


class _TrapEvent_Type(Integer32):
    """Custom type trapEvent based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("warning", 1),
          ("fault", 2),
          ("recover", 3),
          ("up", 4),
          ("down", 5),
          ("on", 6),
          ("off", 7),
          ("connect", 8),
          ("disconnect", 9),
          ("enable", 10),
          ("disable", 11),
          ("timeout", 12),
          ("restore", 13),
          ("reset", 14))
    )


_TrapEvent_Type.__name__ = "Integer32"
_TrapEvent_Object = MibScalar
trapEvent = _TrapEvent_Object(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 0, 2),
    _TrapEvent_Type()
)
trapEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEvent.setStatus("current")

# Managed Objects groups


# Notification objects

trapSystem = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 1)
)
trapSystem.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapSystem.setStatus(
        "current"
    )

trapApplication = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 2)
)
trapApplication.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapApplication.setStatus(
        "current"
    )

trapTerminal = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 3)
)
trapTerminal.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapTerminal.setStatus(
        "current"
    )

trapPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 4)
)
trapPower.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapPower.setStatus(
        "current"
    )

trapSensor = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 5)
)
trapSensor.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapSensor.setStatus(
        "current"
    )

trapFan = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 6)
)
trapFan.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapFan.setStatus(
        "current"
    )

trapColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 7)
)
trapColdStart.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapColdStart.setStatus(
        "current"
    )

trapDyingGasp = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 8)
)
trapDyingGasp.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapDyingGasp.setStatus(
        "current"
    )

trapFanSpeedLowCR = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 9)
)
trapFanSpeedLowCR.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapFanSpeedLowCR.setStatus(
        "current"
    )

trapFanSpeedLowNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 10)
)
trapFanSpeedLowNR.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapFanSpeedLowNR.setStatus(
        "current"
    )

trapFanSpeedHighCR = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 11)
)
trapFanSpeedHighCR.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapFanSpeedHighCR.setStatus(
        "current"
    )

trapFanSpeedHighNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 12)
)
trapFanSpeedHighNR.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapFanSpeedHighNR.setStatus(
        "current"
    )

trapVoltageLowCR = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 13)
)
trapVoltageLowCR.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapVoltageLowCR.setStatus(
        "current"
    )

trapVoltageLowNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 14)
)
trapVoltageLowNR.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapVoltageLowNR.setStatus(
        "current"
    )

trapVoltageHighCR = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 15)
)
trapVoltageHighCR.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapVoltageHighCR.setStatus(
        "current"
    )

trapVoltageHighNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 16)
)
trapVoltageHighNR.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapVoltageHighNR.setStatus(
        "current"
    )

trapTemperatureLowCR = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 17)
)
trapTemperatureLowCR.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapTemperatureLowCR.setStatus(
        "current"
    )

trapTemperatureLowNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 18)
)
trapTemperatureLowNR.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapTemperatureLowNR.setStatus(
        "current"
    )

trapTemperatureHighCR = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 19)
)
trapTemperatureHighCR.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapTemperatureHighCR.setStatus(
        "current"
    )

trapTemperatureHighNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 27509, 3, 11, 20)
)
trapTemperatureHighNR.setObjects(
    ("CREANORD-UBMC-MIB", "trapModule")
)
if mibBuilder.loadTexts:
    trapTemperatureHighNR.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CREANORD-UBMC-MIB",
    **{"ubmc": ubmc,
       "systemStatus": systemStatus,
       "deviceType": deviceType,
       "deviceSerialNumber": deviceSerialNumber,
       "hardwareVersion": hardwareVersion,
       "firmwareVersion": firmwareVersion,
       "softwareVersion": softwareVersion,
       "ubootVersion": ubootVersion,
       "systemUptime": systemUptime,
       "hostFanTable": hostFanTable,
       "hostFanEntry": hostFanEntry,
       "hostFanID": hostFanID,
       "hostFanName": hostFanName,
       "hostFanFault": hostFanFault,
       "hostFanWarning": hostFanWarning,
       "hostFanStatus": hostFanStatus,
       "hostFanSpeed": hostFanSpeed,
       "hostFanRuntime": hostFanRuntime,
       "hostSensorTable": hostSensorTable,
       "hostSensorEntry": hostSensorEntry,
       "hostSensorID": hostSensorID,
       "hostSensorName": hostSensorName,
       "hostSensorTemperature": hostSensorTemperature,
       "hostSensorPeak": hostSensorPeak,
       "hostVoltageTable": hostVoltageTable,
       "hostVoltageEntry": hostVoltageEntry,
       "hostVoltageID": hostVoltageID,
       "hostVoltageName": hostVoltageName,
       "hostVoltage": hostVoltage,
       "interfaceTable": interfaceTable,
       "interfaceEntry": interfaceEntry,
       "interfaceName": interfaceName,
       "interfaceLinkStatus": interfaceLinkStatus,
       "systemStatictis": systemStatictis,
       "infStatisticsTable": infStatisticsTable,
       "infStatisticsEntry": infStatisticsEntry,
       "infName": infName,
       "infRxPkts": infRxPkts,
       "infRxErrors": infRxErrors,
       "infRxDrops": infRxDrops,
       "infRxBytes": infRxBytes,
       "infTxPkts": infTxPkts,
       "infTxErrors": infTxErrors,
       "infTxDrops": infTxDrops,
       "infTxBytes": infTxBytes,
       "systemConfig": systemConfig,
       "trap": trap,
       "trapObject": trapObject,
       "trapModule": trapModule,
       "trapEvent": trapEvent,
       "trapSystem": trapSystem,
       "trapApplication": trapApplication,
       "trapTerminal": trapTerminal,
       "trapPower": trapPower,
       "trapSensor": trapSensor,
       "trapFan": trapFan,
       "trapColdStart": trapColdStart,
       "trapDyingGasp": trapDyingGasp,
       "trapFanSpeedLowCR": trapFanSpeedLowCR,
       "trapFanSpeedLowNR": trapFanSpeedLowNR,
       "trapFanSpeedHighCR": trapFanSpeedHighCR,
       "trapFanSpeedHighNR": trapFanSpeedHighNR,
       "trapVoltageLowCR": trapVoltageLowCR,
       "trapVoltageLowNR": trapVoltageLowNR,
       "trapVoltageHighCR": trapVoltageHighCR,
       "trapVoltageHighNR": trapVoltageHighNR,
       "trapTemperatureLowCR": trapTemperatureLowCR,
       "trapTemperatureLowNR": trapTemperatureLowNR,
       "trapTemperatureHighCR": trapTemperatureHighCR,
       "trapTemperatureHighNR": trapTemperatureHighNR}
)
