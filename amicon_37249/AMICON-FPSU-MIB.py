# SNMP MIB module (AMICON-FPSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/amicon_37249/AMICON-FPSU-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:24:13 2025
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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Amicon_ObjectIdentity = ObjectIdentity
amicon = _Amicon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249)
)
_AmiconProducts_ObjectIdentity = ObjectIdentity
amiconProducts = _AmiconProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 1)
)
_AmiconFpsu_ObjectIdentity = ObjectIdentity
amiconFpsu = _AmiconFpsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1)
)
_AmiconFpsuIp_ObjectIdentity = ObjectIdentity
amiconFpsuIp = _AmiconFpsuIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1)
)
_AmiconFpsuIpSysObjectID_ObjectIdentity = ObjectIdentity
amiconFpsuIpSysObjectID = _AmiconFpsuIpSysObjectID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 1)
)
_AFpsuInfo_ObjectIdentity = ObjectIdentity
aFpsuInfo = _AFpsuInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2)
)


class _AFpsuSerialNumber_Type(DisplayString):
    """Custom type aFpsuSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_AFpsuSerialNumber_Type.__name__ = "DisplayString"
_AFpsuSerialNumber_Object = MibScalar
aFpsuSerialNumber = _AFpsuSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 1),
    _AFpsuSerialNumber_Type()
)
aFpsuSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuSerialNumber.setStatus("current")


class _AFpsuBuildDate_Type(DisplayString):
    """Custom type aFpsuBuildDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_AFpsuBuildDate_Type.__name__ = "DisplayString"
_AFpsuBuildDate_Object = MibScalar
aFpsuBuildDate = _AFpsuBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 2),
    _AFpsuBuildDate_Type()
)
aFpsuBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuBuildDate.setStatus("current")
_AFpsuHardware_ObjectIdentity = ObjectIdentity
aFpsuHardware = _AFpsuHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3)
)
_AFpsuHwSystem_ObjectIdentity = ObjectIdentity
aFpsuHwSystem = _AFpsuHwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 1)
)
_AFpsuHwSystemManufacturer_Type = DisplayString
_AFpsuHwSystemManufacturer_Object = MibScalar
aFpsuHwSystemManufacturer = _AFpsuHwSystemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 1, 1),
    _AFpsuHwSystemManufacturer_Type()
)
aFpsuHwSystemManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwSystemManufacturer.setStatus("current")
_AFpsuHwSystemName_Type = DisplayString
_AFpsuHwSystemName_Object = MibScalar
aFpsuHwSystemName = _AFpsuHwSystemName_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 1, 2),
    _AFpsuHwSystemName_Type()
)
aFpsuHwSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwSystemName.setStatus("current")
_AFpsuHwSystemSerialNumber_Type = DisplayString
_AFpsuHwSystemSerialNumber_Object = MibScalar
aFpsuHwSystemSerialNumber = _AFpsuHwSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 1, 3),
    _AFpsuHwSystemSerialNumber_Type()
)
aFpsuHwSystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwSystemSerialNumber.setStatus("current")
_AFpsuHwSystemWakeUpType_Type = DisplayString
_AFpsuHwSystemWakeUpType_Object = MibScalar
aFpsuHwSystemWakeUpType = _AFpsuHwSystemWakeUpType_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 1, 4),
    _AFpsuHwSystemWakeUpType_Type()
)
aFpsuHwSystemWakeUpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwSystemWakeUpType.setStatus("current")
_AFpsuHwMainboard_ObjectIdentity = ObjectIdentity
aFpsuHwMainboard = _AFpsuHwMainboard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 2)
)
_AFpsuHwMainboardManufacturer_Type = DisplayString
_AFpsuHwMainboardManufacturer_Object = MibScalar
aFpsuHwMainboardManufacturer = _AFpsuHwMainboardManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 2, 1),
    _AFpsuHwMainboardManufacturer_Type()
)
aFpsuHwMainboardManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwMainboardManufacturer.setStatus("current")
_AFpsuHwMainboardName_Type = DisplayString
_AFpsuHwMainboardName_Object = MibScalar
aFpsuHwMainboardName = _AFpsuHwMainboardName_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 2, 2),
    _AFpsuHwMainboardName_Type()
)
aFpsuHwMainboardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwMainboardName.setStatus("current")
_AFpsuHwMainboardVersion_Type = DisplayString
_AFpsuHwMainboardVersion_Object = MibScalar
aFpsuHwMainboardVersion = _AFpsuHwMainboardVersion_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 2, 3),
    _AFpsuHwMainboardVersion_Type()
)
aFpsuHwMainboardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwMainboardVersion.setStatus("current")
_AFpsuHwMainboardSerialNumber_Type = DisplayString
_AFpsuHwMainboardSerialNumber_Object = MibScalar
aFpsuHwMainboardSerialNumber = _AFpsuHwMainboardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 2, 4),
    _AFpsuHwMainboardSerialNumber_Type()
)
aFpsuHwMainboardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwMainboardSerialNumber.setStatus("current")
_AFpsuHwMainboardAssetTag_Type = DisplayString
_AFpsuHwMainboardAssetTag_Object = MibScalar
aFpsuHwMainboardAssetTag = _AFpsuHwMainboardAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 2, 5),
    _AFpsuHwMainboardAssetTag_Type()
)
aFpsuHwMainboardAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwMainboardAssetTag.setStatus("current")
_AFpsuHwBios_ObjectIdentity = ObjectIdentity
aFpsuHwBios = _AFpsuHwBios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 3)
)
_AFpsuHwBiosVendor_Type = DisplayString
_AFpsuHwBiosVendor_Object = MibScalar
aFpsuHwBiosVendor = _AFpsuHwBiosVendor_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 3, 1),
    _AFpsuHwBiosVendor_Type()
)
aFpsuHwBiosVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwBiosVendor.setStatus("current")
_AFpsuHwBiosVersion_Type = DisplayString
_AFpsuHwBiosVersion_Object = MibScalar
aFpsuHwBiosVersion = _AFpsuHwBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 3, 2),
    _AFpsuHwBiosVersion_Type()
)
aFpsuHwBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwBiosVersion.setStatus("current")
_AFpsuHwBiosReleaseDate_Type = DisplayString
_AFpsuHwBiosReleaseDate_Object = MibScalar
aFpsuHwBiosReleaseDate = _AFpsuHwBiosReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 3, 3),
    _AFpsuHwBiosReleaseDate_Type()
)
aFpsuHwBiosReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwBiosReleaseDate.setStatus("current")
_AFpsuHwBiosRevision_Type = DisplayString
_AFpsuHwBiosRevision_Object = MibScalar
aFpsuHwBiosRevision = _AFpsuHwBiosRevision_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 3, 4),
    _AFpsuHwBiosRevision_Type()
)
aFpsuHwBiosRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwBiosRevision.setStatus("current")
_AFpsuHwBiosFirmware_Type = DisplayString
_AFpsuHwBiosFirmware_Object = MibScalar
aFpsuHwBiosFirmware = _AFpsuHwBiosFirmware_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 3, 5),
    _AFpsuHwBiosFirmware_Type()
)
aFpsuHwBiosFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwBiosFirmware.setStatus("current")
_AFpsuHwMemory_ObjectIdentity = ObjectIdentity
aFpsuHwMemory = _AFpsuHwMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 4)
)
_AFpsuHwMemoryRamMbs_Type = Integer32
_AFpsuHwMemoryRamMbs_Object = MibScalar
aFpsuHwMemoryRamMbs = _AFpsuHwMemoryRamMbs_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 4, 1),
    _AFpsuHwMemoryRamMbs_Type()
)
aFpsuHwMemoryRamMbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwMemoryRamMbs.setStatus("current")
_AFpsuHwSensors_ObjectIdentity = ObjectIdentity
aFpsuHwSensors = _AFpsuHwSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 5)
)
_AFpsuHwVoltageProbe_Type = DisplayString
_AFpsuHwVoltageProbe_Object = MibScalar
aFpsuHwVoltageProbe = _AFpsuHwVoltageProbe_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 5, 1),
    _AFpsuHwVoltageProbe_Type()
)
aFpsuHwVoltageProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwVoltageProbe.setStatus("current")
_AFpsuHwTemperatureProbe_Type = DisplayString
_AFpsuHwTemperatureProbe_Object = MibScalar
aFpsuHwTemperatureProbe = _AFpsuHwTemperatureProbe_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 5, 2),
    _AFpsuHwTemperatureProbe_Type()
)
aFpsuHwTemperatureProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwTemperatureProbe.setStatus("current")
_AFpsuHwCpuInfoTable_Object = MibTable
aFpsuHwCpuInfoTable = _AFpsuHwCpuInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 6)
)
if mibBuilder.loadTexts:
    aFpsuHwCpuInfoTable.setStatus("current")
_AFpsuHwCpuInfoEntry_Object = MibTableRow
aFpsuHwCpuInfoEntry = _AFpsuHwCpuInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 6, 1)
)
aFpsuHwCpuInfoEntry.setIndexNames(
    (0, "AMICON-FPSU-MIB", "aFpsuHwCpuInfoIndex"),
)
if mibBuilder.loadTexts:
    aFpsuHwCpuInfoEntry.setStatus("current")
_AFpsuHwCpuInfoIndex_Type = Integer32
_AFpsuHwCpuInfoIndex_Object = MibTableColumn
aFpsuHwCpuInfoIndex = _AFpsuHwCpuInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 6, 1, 1),
    _AFpsuHwCpuInfoIndex_Type()
)
aFpsuHwCpuInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwCpuInfoIndex.setStatus("current")
_AFpsuHwCpuInfoSocket_Type = DisplayString
_AFpsuHwCpuInfoSocket_Object = MibTableColumn
aFpsuHwCpuInfoSocket = _AFpsuHwCpuInfoSocket_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 6, 1, 2),
    _AFpsuHwCpuInfoSocket_Type()
)
aFpsuHwCpuInfoSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwCpuInfoSocket.setStatus("current")
_AFpsuHwCpuInfoType_Type = DisplayString
_AFpsuHwCpuInfoType_Object = MibTableColumn
aFpsuHwCpuInfoType = _AFpsuHwCpuInfoType_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 6, 1, 3),
    _AFpsuHwCpuInfoType_Type()
)
aFpsuHwCpuInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwCpuInfoType.setStatus("current")
_AFpsuHwCpuInfoFamily_Type = DisplayString
_AFpsuHwCpuInfoFamily_Object = MibTableColumn
aFpsuHwCpuInfoFamily = _AFpsuHwCpuInfoFamily_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 6, 1, 4),
    _AFpsuHwCpuInfoFamily_Type()
)
aFpsuHwCpuInfoFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwCpuInfoFamily.setStatus("current")
_AFpsuHwCpuInfoManufacturer_Type = DisplayString
_AFpsuHwCpuInfoManufacturer_Object = MibTableColumn
aFpsuHwCpuInfoManufacturer = _AFpsuHwCpuInfoManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 6, 1, 5),
    _AFpsuHwCpuInfoManufacturer_Type()
)
aFpsuHwCpuInfoManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwCpuInfoManufacturer.setStatus("current")
_AFpsuHwCpuInfoSignature_Type = DisplayString
_AFpsuHwCpuInfoSignature_Object = MibTableColumn
aFpsuHwCpuInfoSignature = _AFpsuHwCpuInfoSignature_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 6, 1, 6),
    _AFpsuHwCpuInfoSignature_Type()
)
aFpsuHwCpuInfoSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwCpuInfoSignature.setStatus("current")
_AFpsuHwCpuInfoVersion_Type = DisplayString
_AFpsuHwCpuInfoVersion_Object = MibTableColumn
aFpsuHwCpuInfoVersion = _AFpsuHwCpuInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 6, 1, 7),
    _AFpsuHwCpuInfoVersion_Type()
)
aFpsuHwCpuInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwCpuInfoVersion.setStatus("current")
_AFpsuHwCpuInfoMaxSpeed_Type = Integer32
_AFpsuHwCpuInfoMaxSpeed_Object = MibTableColumn
aFpsuHwCpuInfoMaxSpeed = _AFpsuHwCpuInfoMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 6, 1, 8),
    _AFpsuHwCpuInfoMaxSpeed_Type()
)
aFpsuHwCpuInfoMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwCpuInfoMaxSpeed.setStatus("current")
_AFpsuHwCpuInfoCurrentSpeed_Type = Integer32
_AFpsuHwCpuInfoCurrentSpeed_Object = MibTableColumn
aFpsuHwCpuInfoCurrentSpeed = _AFpsuHwCpuInfoCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 6, 1, 9),
    _AFpsuHwCpuInfoCurrentSpeed_Type()
)
aFpsuHwCpuInfoCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwCpuInfoCurrentSpeed.setStatus("current")
_AFpsuHwCpuInfoCoreCount_Type = Integer32
_AFpsuHwCpuInfoCoreCount_Object = MibTableColumn
aFpsuHwCpuInfoCoreCount = _AFpsuHwCpuInfoCoreCount_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 6, 1, 10),
    _AFpsuHwCpuInfoCoreCount_Type()
)
aFpsuHwCpuInfoCoreCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwCpuInfoCoreCount.setStatus("current")
_AFpsuHwCpuInfoCoreEnabled_Type = Integer32
_AFpsuHwCpuInfoCoreEnabled_Object = MibTableColumn
aFpsuHwCpuInfoCoreEnabled = _AFpsuHwCpuInfoCoreEnabled_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 6, 1, 11),
    _AFpsuHwCpuInfoCoreEnabled_Type()
)
aFpsuHwCpuInfoCoreEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwCpuInfoCoreEnabled.setStatus("current")
_AFpsuHwCpuInfoThreadCount_Type = Integer32
_AFpsuHwCpuInfoThreadCount_Object = MibTableColumn
aFpsuHwCpuInfoThreadCount = _AFpsuHwCpuInfoThreadCount_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 6, 1, 12),
    _AFpsuHwCpuInfoThreadCount_Type()
)
aFpsuHwCpuInfoThreadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwCpuInfoThreadCount.setStatus("current")
_AFpsuHwSmartInfoTable_Object = MibTable
aFpsuHwSmartInfoTable = _AFpsuHwSmartInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 7)
)
if mibBuilder.loadTexts:
    aFpsuHwSmartInfoTable.setStatus("current")
_AFpsuHwSmartInfoEntry_Object = MibTableRow
aFpsuHwSmartInfoEntry = _AFpsuHwSmartInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 7, 1)
)
aFpsuHwSmartInfoEntry.setIndexNames(
    (0, "AMICON-FPSU-MIB", "aFpsuHwSmartInfoIndex"),
)
if mibBuilder.loadTexts:
    aFpsuHwSmartInfoEntry.setStatus("current")
_AFpsuHwSmartInfoIndex_Type = Integer32
_AFpsuHwSmartInfoIndex_Object = MibTableColumn
aFpsuHwSmartInfoIndex = _AFpsuHwSmartInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 7, 1, 1),
    _AFpsuHwSmartInfoIndex_Type()
)
aFpsuHwSmartInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwSmartInfoIndex.setStatus("current")
_AFpsuHwSmartInfoDev_Type = DisplayString
_AFpsuHwSmartInfoDev_Object = MibTableColumn
aFpsuHwSmartInfoDev = _AFpsuHwSmartInfoDev_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 7, 1, 2),
    _AFpsuHwSmartInfoDev_Type()
)
aFpsuHwSmartInfoDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwSmartInfoDev.setStatus("current")
_AFpsuHwSmartInfoId_Type = Integer32
_AFpsuHwSmartInfoId_Object = MibTableColumn
aFpsuHwSmartInfoId = _AFpsuHwSmartInfoId_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 7, 1, 3),
    _AFpsuHwSmartInfoId_Type()
)
aFpsuHwSmartInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwSmartInfoId.setStatus("current")
_AFpsuHwSmartInfoName_Type = DisplayString
_AFpsuHwSmartInfoName_Object = MibTableColumn
aFpsuHwSmartInfoName = _AFpsuHwSmartInfoName_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 7, 1, 4),
    _AFpsuHwSmartInfoName_Type()
)
aFpsuHwSmartInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwSmartInfoName.setStatus("current")
_AFpsuHwSmartInfoValue_Type = Integer32
_AFpsuHwSmartInfoValue_Object = MibTableColumn
aFpsuHwSmartInfoValue = _AFpsuHwSmartInfoValue_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 7, 1, 5),
    _AFpsuHwSmartInfoValue_Type()
)
aFpsuHwSmartInfoValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwSmartInfoValue.setStatus("current")
_AFpsuHwSmartInfoWorst_Type = Integer32
_AFpsuHwSmartInfoWorst_Object = MibTableColumn
aFpsuHwSmartInfoWorst = _AFpsuHwSmartInfoWorst_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 7, 1, 6),
    _AFpsuHwSmartInfoWorst_Type()
)
aFpsuHwSmartInfoWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwSmartInfoWorst.setStatus("current")
_AFpsuHwSmartInfoThresholds_Type = Integer32
_AFpsuHwSmartInfoThresholds_Object = MibTableColumn
aFpsuHwSmartInfoThresholds = _AFpsuHwSmartInfoThresholds_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 7, 1, 7),
    _AFpsuHwSmartInfoThresholds_Type()
)
aFpsuHwSmartInfoThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwSmartInfoThresholds.setStatus("current")


class _AFpsuHwSmartInfoType_Type(Integer32):
    """Custom type aFpsuHwSmartInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oldage", 0),
          ("prefail", 1))
    )


_AFpsuHwSmartInfoType_Type.__name__ = "Integer32"
_AFpsuHwSmartInfoType_Object = MibTableColumn
aFpsuHwSmartInfoType = _AFpsuHwSmartInfoType_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 7, 1, 8),
    _AFpsuHwSmartInfoType_Type()
)
aFpsuHwSmartInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwSmartInfoType.setStatus("current")


class _AFpsuHwSmartInfoUpdated_Type(Integer32):
    """Custom type aFpsuHwSmartInfoUpdated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("always", 0),
          ("offline", 1))
    )


_AFpsuHwSmartInfoUpdated_Type.__name__ = "Integer32"
_AFpsuHwSmartInfoUpdated_Object = MibTableColumn
aFpsuHwSmartInfoUpdated = _AFpsuHwSmartInfoUpdated_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 7, 1, 9),
    _AFpsuHwSmartInfoUpdated_Type()
)
aFpsuHwSmartInfoUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwSmartInfoUpdated.setStatus("current")


class _AFpsuHwSmartInfoFailed_Type(Integer32):
    """Custom type aFpsuHwSmartInfoFailed based on Integer32"""
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
          ("now", 1),
          ("past", 2))
    )


_AFpsuHwSmartInfoFailed_Type.__name__ = "Integer32"
_AFpsuHwSmartInfoFailed_Object = MibTableColumn
aFpsuHwSmartInfoFailed = _AFpsuHwSmartInfoFailed_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 3, 7, 1, 10),
    _AFpsuHwSmartInfoFailed_Type()
)
aFpsuHwSmartInfoFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwSmartInfoFailed.setStatus("current")
_AFpsuSoftware_ObjectIdentity = ObjectIdentity
aFpsuSoftware = _AFpsuSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 4)
)


class _AFpsuSwVer_Type(DisplayString):
    """Custom type aFpsuSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AFpsuSwVer_Type.__name__ = "DisplayString"
_AFpsuSwVer_Object = MibScalar
aFpsuSwVer = _AFpsuSwVer_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 4, 1),
    _AFpsuSwVer_Type()
)
aFpsuSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuSwVer.setStatus("current")


class _AFpsuSwInstallationDate_Type(DisplayString):
    """Custom type aFpsuSwInstallationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_AFpsuSwInstallationDate_Type.__name__ = "DisplayString"
_AFpsuSwInstallationDate_Object = MibScalar
aFpsuSwInstallationDate = _AFpsuSwInstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 4, 2),
    _AFpsuSwInstallationDate_Type()
)
aFpsuSwInstallationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuSwInstallationDate.setStatus("current")


class _AFpsuSwEndSupportDate_Type(DisplayString):
    """Custom type aFpsuSwEndSupportDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_AFpsuSwEndSupportDate_Type.__name__ = "DisplayString"
_AFpsuSwEndSupportDate_Object = MibScalar
aFpsuSwEndSupportDate = _AFpsuSwEndSupportDate_Object(
    (1, 3, 6, 1, 4, 1, 37249, 1, 1, 1, 2, 4, 3),
    _AFpsuSwEndSupportDate_Type()
)
aFpsuSwEndSupportDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuSwEndSupportDate.setStatus("current")
_AmiconState_ObjectIdentity = ObjectIdentity
amiconState = _AmiconState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 2)
)
_AFpsuState_ObjectIdentity = ObjectIdentity
aFpsuState = _AFpsuState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1)
)
_AFpsuMemoryUse_ObjectIdentity = ObjectIdentity
aFpsuMemoryUse = _AFpsuMemoryUse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 1)
)
_AFpsuMemoryUseTable_Object = MibTable
aFpsuMemoryUseTable = _AFpsuMemoryUseTable_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aFpsuMemoryUseTable.setStatus("current")
_AFpsuMemoryUseEntry_Object = MibTableRow
aFpsuMemoryUseEntry = _AFpsuMemoryUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 1, 1, 1)
)
aFpsuMemoryUseEntry.setIndexNames(
    (0, "AMICON-FPSU-MIB", "aFpsuMemoryUseIndex"),
)
if mibBuilder.loadTexts:
    aFpsuMemoryUseEntry.setStatus("current")
_AFpsuMemoryUseIndex_Type = Integer32
_AFpsuMemoryUseIndex_Object = MibTableColumn
aFpsuMemoryUseIndex = _AFpsuMemoryUseIndex_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 1, 1, 1, 1),
    _AFpsuMemoryUseIndex_Type()
)
aFpsuMemoryUseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuMemoryUseIndex.setStatus("current")
_AFpsuMemoryUseArpMin_Type = Integer32
_AFpsuMemoryUseArpMin_Object = MibTableColumn
aFpsuMemoryUseArpMin = _AFpsuMemoryUseArpMin_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 1, 1, 1, 2),
    _AFpsuMemoryUseArpMin_Type()
)
aFpsuMemoryUseArpMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuMemoryUseArpMin.setStatus("current")
_AFpsuMemoryUseArpMax_Type = Integer32
_AFpsuMemoryUseArpMax_Object = MibTableColumn
aFpsuMemoryUseArpMax = _AFpsuMemoryUseArpMax_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 1, 1, 1, 3),
    _AFpsuMemoryUseArpMax_Type()
)
aFpsuMemoryUseArpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuMemoryUseArpMax.setStatus("current")
_AFpsuMemoryUseArpNow_Type = Integer32
_AFpsuMemoryUseArpNow_Object = MibTableColumn
aFpsuMemoryUseArpNow = _AFpsuMemoryUseArpNow_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 1, 1, 1, 4),
    _AFpsuMemoryUseArpNow_Type()
)
aFpsuMemoryUseArpNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuMemoryUseArpNow.setStatus("current")
_AFpsuMemoryUseRecvMin_Type = Integer32
_AFpsuMemoryUseRecvMin_Object = MibTableColumn
aFpsuMemoryUseRecvMin = _AFpsuMemoryUseRecvMin_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 1, 1, 1, 5),
    _AFpsuMemoryUseRecvMin_Type()
)
aFpsuMemoryUseRecvMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuMemoryUseRecvMin.setStatus("current")
_AFpsuMemoryUseRecvMax_Type = Integer32
_AFpsuMemoryUseRecvMax_Object = MibTableColumn
aFpsuMemoryUseRecvMax = _AFpsuMemoryUseRecvMax_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 1, 1, 1, 6),
    _AFpsuMemoryUseRecvMax_Type()
)
aFpsuMemoryUseRecvMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuMemoryUseRecvMax.setStatus("current")
_AFpsuMemoryUseRecvNow_Type = Integer32
_AFpsuMemoryUseRecvNow_Object = MibTableColumn
aFpsuMemoryUseRecvNow = _AFpsuMemoryUseRecvNow_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 1, 1, 1, 7),
    _AFpsuMemoryUseRecvNow_Type()
)
aFpsuMemoryUseRecvNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuMemoryUseRecvNow.setStatus("current")
_AFpsuMemoryUseSendMin_Type = Integer32
_AFpsuMemoryUseSendMin_Object = MibTableColumn
aFpsuMemoryUseSendMin = _AFpsuMemoryUseSendMin_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 1, 1, 1, 8),
    _AFpsuMemoryUseSendMin_Type()
)
aFpsuMemoryUseSendMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuMemoryUseSendMin.setStatus("current")
_AFpsuMemoryUseSendMax_Type = Integer32
_AFpsuMemoryUseSendMax_Object = MibTableColumn
aFpsuMemoryUseSendMax = _AFpsuMemoryUseSendMax_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 1, 1, 1, 9),
    _AFpsuMemoryUseSendMax_Type()
)
aFpsuMemoryUseSendMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuMemoryUseSendMax.setStatus("current")
_AFpsuMemoryUseSendNow_Type = Integer32
_AFpsuMemoryUseSendNow_Object = MibTableColumn
aFpsuMemoryUseSendNow = _AFpsuMemoryUseSendNow_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 1, 1, 1, 10),
    _AFpsuMemoryUseSendNow_Type()
)
aFpsuMemoryUseSendNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuMemoryUseSendNow.setStatus("current")
_AFpsuMemoryTotal_Type = Integer32
_AFpsuMemoryTotal_Object = MibScalar
aFpsuMemoryTotal = _AFpsuMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 1, 10),
    _AFpsuMemoryTotal_Type()
)
aFpsuMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuMemoryTotal.setStatus("current")
_AFpsuMemoryFree_Type = Integer32
_AFpsuMemoryFree_Object = MibScalar
aFpsuMemoryFree = _AFpsuMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 1, 11),
    _AFpsuMemoryFree_Type()
)
aFpsuMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuMemoryFree.setStatus("current")
_AFpsuUserStateTable_Object = MibTable
aFpsuUserStateTable = _AFpsuUserStateTable_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 2)
)
if mibBuilder.loadTexts:
    aFpsuUserStateTable.setStatus("current")
_AFpsuUserStateEntry_Object = MibTableRow
aFpsuUserStateEntry = _AFpsuUserStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 2, 1)
)
aFpsuUserStateEntry.setIndexNames(
    (0, "AMICON-FPSU-MIB", "aFpsuUserStateIndex"),
)
if mibBuilder.loadTexts:
    aFpsuUserStateEntry.setStatus("current")
_AFpsuUserStateIndex_Type = Integer32
_AFpsuUserStateIndex_Object = MibTableColumn
aFpsuUserStateIndex = _AFpsuUserStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 2, 1, 1),
    _AFpsuUserStateIndex_Type()
)
aFpsuUserStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuUserStateIndex.setStatus("current")
_AFpsuUserStateFirstIp_Type = IpAddress
_AFpsuUserStateFirstIp_Object = MibTableColumn
aFpsuUserStateFirstIp = _AFpsuUserStateFirstIp_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 2, 1, 2),
    _AFpsuUserStateFirstIp_Type()
)
aFpsuUserStateFirstIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuUserStateFirstIp.setStatus("current")


class _AFpsuUserStateFirstWithFpsu_Type(Integer32):
    """Custom type aFpsuUserStateFirstWithFpsu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofpsu", 0),
          ("withfpsu", 1))
    )


_AFpsuUserStateFirstWithFpsu_Type.__name__ = "Integer32"
_AFpsuUserStateFirstWithFpsu_Object = MibTableColumn
aFpsuUserStateFirstWithFpsu = _AFpsuUserStateFirstWithFpsu_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 2, 1, 3),
    _AFpsuUserStateFirstWithFpsu_Type()
)
aFpsuUserStateFirstWithFpsu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuUserStateFirstWithFpsu.setStatus("current")
_AFpsuUserStateSecondIp_Type = IpAddress
_AFpsuUserStateSecondIp_Object = MibTableColumn
aFpsuUserStateSecondIp = _AFpsuUserStateSecondIp_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 2, 1, 4),
    _AFpsuUserStateSecondIp_Type()
)
aFpsuUserStateSecondIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuUserStateSecondIp.setStatus("current")


class _AFpsuUserStateSecondWithFpsu_Type(Integer32):
    """Custom type aFpsuUserStateSecondWithFpsu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofpsu", 0),
          ("withfpsu", 1))
    )


_AFpsuUserStateSecondWithFpsu_Type.__name__ = "Integer32"
_AFpsuUserStateSecondWithFpsu_Object = MibTableColumn
aFpsuUserStateSecondWithFpsu = _AFpsuUserStateSecondWithFpsu_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 2, 1, 5),
    _AFpsuUserStateSecondWithFpsu_Type()
)
aFpsuUserStateSecondWithFpsu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuUserStateSecondWithFpsu.setStatus("current")
_AFpsuUserStateRecvSrcBytes_Type = Counter64
_AFpsuUserStateRecvSrcBytes_Object = MibTableColumn
aFpsuUserStateRecvSrcBytes = _AFpsuUserStateRecvSrcBytes_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 2, 1, 6),
    _AFpsuUserStateRecvSrcBytes_Type()
)
aFpsuUserStateRecvSrcBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuUserStateRecvSrcBytes.setStatus("current")
_AFpsuUserStateRecvDstBytes_Type = Counter64
_AFpsuUserStateRecvDstBytes_Object = MibTableColumn
aFpsuUserStateRecvDstBytes = _AFpsuUserStateRecvDstBytes_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 2, 1, 7),
    _AFpsuUserStateRecvDstBytes_Type()
)
aFpsuUserStateRecvDstBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuUserStateRecvDstBytes.setStatus("current")


class _AFpsuUserStateError_Type(Integer32):
    """Custom type aFpsuUserStateError based on Integer32"""
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("noerror", 0),
          ("nomem", 1),
          ("badaddr", 2),
          ("shortpack", 3),
          ("dbladdr", 4),
          ("unknown", 5),
          ("remoteunknown", 6),
          ("prohibit", 7),
          ("guardneeded", 8),
          ("guardnotready", 9),
          ("noroute", 10),
          ("iface", 11),
          ("modework", 12),
          ("ttl", 13),
          ("badguard", 14),
          ("unsupreq", 15),
          ("lan", 16),
          ("prohconnect", 17),
          ("lenpack", 18),
          ("cantfrag", 19),
          ("guardnotneeded", 20),
          ("tcpudp", 21),
          ("sourceroute", 22),
          ("invalidtotlen", 23),
          ("invalidoplist", 24),
          ("guardignore", 25),
          ("guardremerr", 26),
          ("serialization", 27),
          ("redirect", 28),
          ("clibadpack", 29),
          ("clinotconnect", 30),
          ("ifaceclientuser", 31),
          ("ifaceclientclient", 32),
          ("vlanunknown", 33))
    )


_AFpsuUserStateError_Type.__name__ = "Integer32"
_AFpsuUserStateError_Object = MibTableColumn
aFpsuUserStateError = _AFpsuUserStateError_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 2, 1, 8),
    _AFpsuUserStateError_Type()
)
aFpsuUserStateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuUserStateError.setStatus("current")
_AFpsuAdminStateTable_Object = MibTable
aFpsuAdminStateTable = _AFpsuAdminStateTable_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 3)
)
if mibBuilder.loadTexts:
    aFpsuAdminStateTable.setStatus("current")
_AFpsuAdminStateEntry_Object = MibTableRow
aFpsuAdminStateEntry = _AFpsuAdminStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 3, 1)
)
aFpsuAdminStateEntry.setIndexNames(
    (0, "AMICON-FPSU-MIB", "aFpsuAdminStateIndex"),
)
if mibBuilder.loadTexts:
    aFpsuAdminStateEntry.setStatus("current")
_AFpsuAdminStateIndex_Type = Integer32
_AFpsuAdminStateIndex_Object = MibTableColumn
aFpsuAdminStateIndex = _AFpsuAdminStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 3, 1, 1),
    _AFpsuAdminStateIndex_Type()
)
aFpsuAdminStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuAdminStateIndex.setStatus("current")
_AFpsuAdminName_Type = DisplayString
_AFpsuAdminName_Object = MibTableColumn
aFpsuAdminName = _AFpsuAdminName_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 3, 1, 2),
    _AFpsuAdminName_Type()
)
aFpsuAdminName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuAdminName.setStatus("current")


class _AFpsuAdminPackedName_Type(DisplayString):
    """Custom type aFpsuAdminPackedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_AFpsuAdminPackedName_Type.__name__ = "DisplayString"
_AFpsuAdminPackedName_Object = MibTableColumn
aFpsuAdminPackedName = _AFpsuAdminPackedName_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 3, 1, 3),
    _AFpsuAdminPackedName_Type()
)
aFpsuAdminPackedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuAdminPackedName.setStatus("current")
_AFpsuAdminStateIp_Type = IpAddress
_AFpsuAdminStateIp_Object = MibTableColumn
aFpsuAdminStateIp = _AFpsuAdminStateIp_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 3, 1, 4),
    _AFpsuAdminStateIp_Type()
)
aFpsuAdminStateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuAdminStateIp.setStatus("current")


class _AFpsuAdminStatePort_Type(Integer32):
    """Custom type aFpsuAdminStatePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AFpsuAdminStatePort_Type.__name__ = "Integer32"
_AFpsuAdminStatePort_Object = MibTableColumn
aFpsuAdminStatePort = _AFpsuAdminStatePort_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 3, 1, 5),
    _AFpsuAdminStatePort_Type()
)
aFpsuAdminStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuAdminStatePort.setStatus("current")
_AFpsuAdminStatePacketsIn_Type = Counter32
_AFpsuAdminStatePacketsIn_Object = MibTableColumn
aFpsuAdminStatePacketsIn = _AFpsuAdminStatePacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 3, 1, 6),
    _AFpsuAdminStatePacketsIn_Type()
)
aFpsuAdminStatePacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuAdminStatePacketsIn.setStatus("current")
_AFpsuAdminStatePacketsOut_Type = Counter32
_AFpsuAdminStatePacketsOut_Object = MibTableColumn
aFpsuAdminStatePacketsOut = _AFpsuAdminStatePacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 3, 1, 7),
    _AFpsuAdminStatePacketsOut_Type()
)
aFpsuAdminStatePacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuAdminStatePacketsOut.setStatus("current")
_AFpsuAdminStateDataIn_Type = Counter64
_AFpsuAdminStateDataIn_Object = MibTableColumn
aFpsuAdminStateDataIn = _AFpsuAdminStateDataIn_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 3, 1, 8),
    _AFpsuAdminStateDataIn_Type()
)
aFpsuAdminStateDataIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuAdminStateDataIn.setStatus("current")
_AFpsuAdminStateDataOut_Type = Counter64
_AFpsuAdminStateDataOut_Object = MibTableColumn
aFpsuAdminStateDataOut = _AFpsuAdminStateDataOut_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 3, 1, 9),
    _AFpsuAdminStateDataOut_Type()
)
aFpsuAdminStateDataOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuAdminStateDataOut.setStatus("current")
_AFpsuAdminStateErrors_Type = Counter32
_AFpsuAdminStateErrors_Object = MibTableColumn
aFpsuAdminStateErrors = _AFpsuAdminStateErrors_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 3, 1, 10),
    _AFpsuAdminStateErrors_Type()
)
aFpsuAdminStateErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuAdminStateErrors.setStatus("current")
_AFpsuAdminStateMtu_Type = Integer32
_AFpsuAdminStateMtu_Object = MibTableColumn
aFpsuAdminStateMtu = _AFpsuAdminStateMtu_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 3, 1, 11),
    _AFpsuAdminStateMtu_Type()
)
aFpsuAdminStateMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuAdminStateMtu.setStatus("current")
_AFpsuAdminStateLastRequest_Type = DisplayString
_AFpsuAdminStateLastRequest_Object = MibTableColumn
aFpsuAdminStateLastRequest = _AFpsuAdminStateLastRequest_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 3, 1, 12),
    _AFpsuAdminStateLastRequest_Type()
)
aFpsuAdminStateLastRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuAdminStateLastRequest.setStatus("current")
_AFpsuClientStateTable_Object = MibTable
aFpsuClientStateTable = _AFpsuClientStateTable_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 4)
)
if mibBuilder.loadTexts:
    aFpsuClientStateTable.setStatus("current")
_AFpsuClientStateEntry_Object = MibTableRow
aFpsuClientStateEntry = _AFpsuClientStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 4, 1)
)
aFpsuClientStateEntry.setIndexNames(
    (0, "AMICON-FPSU-MIB", "aFpsuClientStateIndex"),
)
if mibBuilder.loadTexts:
    aFpsuClientStateEntry.setStatus("current")
_AFpsuClientStateIndex_Type = Integer32
_AFpsuClientStateIndex_Object = MibTableColumn
aFpsuClientStateIndex = _AFpsuClientStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 4, 1, 1),
    _AFpsuClientStateIndex_Type()
)
aFpsuClientStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuClientStateIndex.setStatus("current")


class _AFpsuClientStateName_Type(DisplayString):
    """Custom type aFpsuClientStateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AFpsuClientStateName_Type.__name__ = "DisplayString"
_AFpsuClientStateName_Object = MibTableColumn
aFpsuClientStateName = _AFpsuClientStateName_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 4, 1, 2),
    _AFpsuClientStateName_Type()
)
aFpsuClientStateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuClientStateName.setStatus("current")
_AFpsuClientStateMac_Type = MacAddress
_AFpsuClientStateMac_Object = MibTableColumn
aFpsuClientStateMac = _AFpsuClientStateMac_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 4, 1, 3),
    _AFpsuClientStateMac_Type()
)
aFpsuClientStateMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuClientStateMac.setStatus("current")
_AFpsuClientStateRealIp_Type = IpAddress
_AFpsuClientStateRealIp_Object = MibTableColumn
aFpsuClientStateRealIp = _AFpsuClientStateRealIp_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 4, 1, 4),
    _AFpsuClientStateRealIp_Type()
)
aFpsuClientStateRealIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuClientStateRealIp.setStatus("current")
_AFpsuClientStatePrivateIp_Type = IpAddress
_AFpsuClientStatePrivateIp_Object = MibTableColumn
aFpsuClientStatePrivateIp = _AFpsuClientStatePrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 4, 1, 5),
    _AFpsuClientStatePrivateIp_Type()
)
aFpsuClientStatePrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuClientStatePrivateIp.setStatus("current")


class _AFpsuClientStateLanPort_Type(Integer32):
    """Custom type aFpsuClientStateLanPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AFpsuClientStateLanPort_Type.__name__ = "Integer32"
_AFpsuClientStateLanPort_Object = MibTableColumn
aFpsuClientStateLanPort = _AFpsuClientStateLanPort_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 4, 1, 6),
    _AFpsuClientStateLanPort_Type()
)
aFpsuClientStateLanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuClientStateLanPort.setStatus("current")
_AFpsuClientStateCenter_Type = Integer32
_AFpsuClientStateCenter_Object = MibTableColumn
aFpsuClientStateCenter = _AFpsuClientStateCenter_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 4, 1, 7),
    _AFpsuClientStateCenter_Type()
)
aFpsuClientStateCenter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuClientStateCenter.setStatus("current")
_AFpsuClientStateNumber_Type = Integer32
_AFpsuClientStateNumber_Object = MibTableColumn
aFpsuClientStateNumber = _AFpsuClientStateNumber_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 4, 1, 8),
    _AFpsuClientStateNumber_Type()
)
aFpsuClientStateNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuClientStateNumber.setStatus("current")
_AFpsuClientStateGroup_Type = Integer32
_AFpsuClientStateGroup_Object = MibTableColumn
aFpsuClientStateGroup = _AFpsuClientStateGroup_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 4, 1, 9),
    _AFpsuClientStateGroup_Type()
)
aFpsuClientStateGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuClientStateGroup.setStatus("current")
_AFpsuClientStateDataIn_Type = Counter64
_AFpsuClientStateDataIn_Object = MibTableColumn
aFpsuClientStateDataIn = _AFpsuClientStateDataIn_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 4, 1, 10),
    _AFpsuClientStateDataIn_Type()
)
aFpsuClientStateDataIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuClientStateDataIn.setStatus("current")
_AFpsuClientStateDataOut_Type = Counter64
_AFpsuClientStateDataOut_Object = MibTableColumn
aFpsuClientStateDataOut = _AFpsuClientStateDataOut_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 4, 1, 11),
    _AFpsuClientStateDataOut_Type()
)
aFpsuClientStateDataOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuClientStateDataOut.setStatus("current")
_AFpsuClientStatePacketsIn_Type = Counter32
_AFpsuClientStatePacketsIn_Object = MibTableColumn
aFpsuClientStatePacketsIn = _AFpsuClientStatePacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 4, 1, 12),
    _AFpsuClientStatePacketsIn_Type()
)
aFpsuClientStatePacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuClientStatePacketsIn.setStatus("current")
_AFpsuClientStatePacketsOut_Type = Counter32
_AFpsuClientStatePacketsOut_Object = MibTableColumn
aFpsuClientStatePacketsOut = _AFpsuClientStatePacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 4, 1, 13),
    _AFpsuClientStatePacketsOut_Type()
)
aFpsuClientStatePacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuClientStatePacketsOut.setStatus("current")


class _AFpsuClientStateTunnelOpenTime_Type(DisplayString):
    """Custom type aFpsuClientStateTunnelOpenTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AFpsuClientStateTunnelOpenTime_Type.__name__ = "DisplayString"
_AFpsuClientStateTunnelOpenTime_Object = MibTableColumn
aFpsuClientStateTunnelOpenTime = _AFpsuClientStateTunnelOpenTime_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 4, 1, 14),
    _AFpsuClientStateTunnelOpenTime_Type()
)
aFpsuClientStateTunnelOpenTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuClientStateTunnelOpenTime.setStatus("current")


class _AFpsuClientStateLastExchangeTime_Type(DisplayString):
    """Custom type aFpsuClientStateLastExchangeTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AFpsuClientStateLastExchangeTime_Type.__name__ = "DisplayString"
_AFpsuClientStateLastExchangeTime_Object = MibTableColumn
aFpsuClientStateLastExchangeTime = _AFpsuClientStateLastExchangeTime_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 4, 1, 15),
    _AFpsuClientStateLastExchangeTime_Type()
)
aFpsuClientStateLastExchangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuClientStateLastExchangeTime.setStatus("current")
_AFpsuHotReserveState_ObjectIdentity = ObjectIdentity
aFpsuHotReserveState = _AFpsuHotReserveState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 5)
)


class _AFpsuHotReserveStateVpn_Type(Integer32):
    """Custom type aFpsuHotReserveStateVpn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dataexc", 0),
          ("searchotr", 1),
          ("waitsynok", 3))
    )


_AFpsuHotReserveStateVpn_Type.__name__ = "Integer32"
_AFpsuHotReserveStateVpn_Object = MibScalar
aFpsuHotReserveStateVpn = _AFpsuHotReserveStateVpn_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 5, 1),
    _AFpsuHotReserveStateVpn_Type()
)
aFpsuHotReserveStateVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHotReserveStateVpn.setStatus("current")


class _AFpsuHotReserveStateLocalRole_Type(Integer32):
    """Custom type aFpsuHotReserveStateLocalRole based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("notanswer", 1),
          ("stop", 2),
          ("error", 3),
          ("starting", 4),
          ("working", 5),
          ("reserving", 6),
          ("takework", 7),
          ("ending", 8),
          ("synchro", 9),
          ("blocked", 10),
          ("restart", 11))
    )


_AFpsuHotReserveStateLocalRole_Type.__name__ = "Integer32"
_AFpsuHotReserveStateLocalRole_Object = MibScalar
aFpsuHotReserveStateLocalRole = _AFpsuHotReserveStateLocalRole_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 5, 2),
    _AFpsuHotReserveStateLocalRole_Type()
)
aFpsuHotReserveStateLocalRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHotReserveStateLocalRole.setStatus("current")


class _AFpsuHotReserveStateRemoteRole_Type(Integer32):
    """Custom type aFpsuHotReserveStateRemoteRole based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("notanswer", 1),
          ("stop", 2),
          ("error", 3),
          ("starting", 4),
          ("working", 5),
          ("reserving", 6),
          ("takework", 7),
          ("ending", 8),
          ("synchro", 9),
          ("blocked", 10),
          ("restart", 11))
    )


_AFpsuHotReserveStateRemoteRole_Type.__name__ = "Integer32"
_AFpsuHotReserveStateRemoteRole_Object = MibScalar
aFpsuHotReserveStateRemoteRole = _AFpsuHotReserveStateRemoteRole_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 5, 3),
    _AFpsuHotReserveStateRemoteRole_Type()
)
aFpsuHotReserveStateRemoteRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHotReserveStateRemoteRole.setStatus("current")
_AFpsuHotReserveStateRemoteMac_Type = MacAddress
_AFpsuHotReserveStateRemoteMac_Object = MibScalar
aFpsuHotReserveStateRemoteMac = _AFpsuHotReserveStateRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 5, 4),
    _AFpsuHotReserveStateRemoteMac_Type()
)
aFpsuHotReserveStateRemoteMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHotReserveStateRemoteMac.setStatus("current")


class _AFpsuHotReserveStateLink_Type(Integer32):
    """Custom type aFpsuHotReserveStateLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noreply", 0),
          ("workdone", 1))
    )


_AFpsuHotReserveStateLink_Type.__name__ = "Integer32"
_AFpsuHotReserveStateLink_Object = MibScalar
aFpsuHotReserveStateLink = _AFpsuHotReserveStateLink_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 5, 5),
    _AFpsuHotReserveStateLink_Type()
)
aFpsuHotReserveStateLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHotReserveStateLink.setStatus("current")


class _AFpsuHotReserveStateWork_Type(Integer32):
    """Custom type aFpsuHotReserveStateWork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nowork", 0),
          ("workfine", 1))
    )


_AFpsuHotReserveStateWork_Type.__name__ = "Integer32"
_AFpsuHotReserveStateWork_Object = MibScalar
aFpsuHotReserveStateWork = _AFpsuHotReserveStateWork_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 5, 6),
    _AFpsuHotReserveStateWork_Type()
)
aFpsuHotReserveStateWork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHotReserveStateWork.setStatus("current")
_AFpsuHardwareState_ObjectIdentity = ObjectIdentity
aFpsuHardwareState = _AFpsuHardwareState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6)
)


class _AFpsuHwWatchDog_Type(Integer32):
    """Custom type aFpsuHwWatchDog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noactive", 0),
          ("hardwarewd", 1),
          ("softwarewd", 2))
    )


_AFpsuHwWatchDog_Type.__name__ = "Integer32"
_AFpsuHwWatchDog_Object = MibScalar
aFpsuHwWatchDog = _AFpsuHwWatchDog_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 1),
    _AFpsuHwWatchDog_Type()
)
aFpsuHwWatchDog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwWatchDog.setStatus("current")
_AFpsuHardwareFanState_ObjectIdentity = ObjectIdentity
aFpsuHardwareFanState = _AFpsuHardwareFanState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 2)
)
_AFpsuHwFan1Speed_Type = Integer32
_AFpsuHwFan1Speed_Object = MibScalar
aFpsuHwFan1Speed = _AFpsuHwFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 2, 1),
    _AFpsuHwFan1Speed_Type()
)
aFpsuHwFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwFan1Speed.setStatus("current")
_AFpsuHwFan2Speed_Type = Integer32
_AFpsuHwFan2Speed_Object = MibScalar
aFpsuHwFan2Speed = _AFpsuHwFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 2, 2),
    _AFpsuHwFan2Speed_Type()
)
aFpsuHwFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwFan2Speed.setStatus("current")
_AFpsuHwFan3Speed_Type = Integer32
_AFpsuHwFan3Speed_Object = MibScalar
aFpsuHwFan3Speed = _AFpsuHwFan3Speed_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 2, 3),
    _AFpsuHwFan3Speed_Type()
)
aFpsuHwFan3Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwFan3Speed.setStatus("current")
_AFpsuHardwareTemperatureState_ObjectIdentity = ObjectIdentity
aFpsuHardwareTemperatureState = _AFpsuHardwareTemperatureState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 3)
)
_AFpsuHwCpuTemperature_Type = Integer32
_AFpsuHwCpuTemperature_Object = MibScalar
aFpsuHwCpuTemperature = _AFpsuHwCpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 3, 1),
    _AFpsuHwCpuTemperature_Type()
)
aFpsuHwCpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwCpuTemperature.setStatus("current")
_AFpsuHwMBTemperature_Type = Integer32
_AFpsuHwMBTemperature_Object = MibScalar
aFpsuHwMBTemperature = _AFpsuHwMBTemperature_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 3, 2),
    _AFpsuHwMBTemperature_Type()
)
aFpsuHwMBTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwMBTemperature.setStatus("current")
_AFpsuHardwareVoltageState_ObjectIdentity = ObjectIdentity
aFpsuHardwareVoltageState = _AFpsuHardwareVoltageState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 4)
)
_AFpsuHwPowerVoltage3_Type = DisplayString
_AFpsuHwPowerVoltage3_Object = MibScalar
aFpsuHwPowerVoltage3 = _AFpsuHwPowerVoltage3_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 4, 1),
    _AFpsuHwPowerVoltage3_Type()
)
aFpsuHwPowerVoltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwPowerVoltage3.setStatus("current")
_AFpsuHwPowerVoltage5_Type = DisplayString
_AFpsuHwPowerVoltage5_Object = MibScalar
aFpsuHwPowerVoltage5 = _AFpsuHwPowerVoltage5_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 4, 2),
    _AFpsuHwPowerVoltage5_Type()
)
aFpsuHwPowerVoltage5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwPowerVoltage5.setStatus("current")
_AFpsuHwPowerVoltage12_Type = DisplayString
_AFpsuHwPowerVoltage12_Object = MibScalar
aFpsuHwPowerVoltage12 = _AFpsuHwPowerVoltage12_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 4, 3),
    _AFpsuHwPowerVoltage12_Type()
)
aFpsuHwPowerVoltage12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwPowerVoltage12.setStatus("current")
_AFpsuHwCpuLoad_Type = Integer32
_AFpsuHwCpuLoad_Object = MibScalar
aFpsuHwCpuLoad = _AFpsuHwCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 5),
    _AFpsuHwCpuLoad_Type()
)
aFpsuHwCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwCpuLoad.setStatus("current")
_AFpsuHardwarePowerSupplyState_ObjectIdentity = ObjectIdentity
aFpsuHardwarePowerSupplyState = _AFpsuHardwarePowerSupplyState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 6)
)
_AFpsuHardwarePowerSupply1State_ObjectIdentity = ObjectIdentity
aFpsuHardwarePowerSupply1State = _AFpsuHardwarePowerSupply1State_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 6, 1)
)
_AFpsuHwPowerPS1_Type = Integer32
_AFpsuHwPowerPS1_Object = MibScalar
aFpsuHwPowerPS1 = _AFpsuHwPowerPS1_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 6, 1, 1),
    _AFpsuHwPowerPS1_Type()
)
aFpsuHwPowerPS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwPowerPS1.setStatus("current")
_AFpsuHwTemperaturePS1_Type = Integer32
_AFpsuHwTemperaturePS1_Object = MibScalar
aFpsuHwTemperaturePS1 = _AFpsuHwTemperaturePS1_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 6, 1, 2),
    _AFpsuHwTemperaturePS1_Type()
)
aFpsuHwTemperaturePS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwTemperaturePS1.setStatus("current")
_AFpsuHardwarePowerSupply2State_ObjectIdentity = ObjectIdentity
aFpsuHardwarePowerSupply2State = _AFpsuHardwarePowerSupply2State_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 6, 2)
)
_AFpsuHwPowerPS2_Type = Integer32
_AFpsuHwPowerPS2_Object = MibScalar
aFpsuHwPowerPS2 = _AFpsuHwPowerPS2_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 6, 2, 1),
    _AFpsuHwPowerPS2_Type()
)
aFpsuHwPowerPS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwPowerPS2.setStatus("current")
_AFpsuHwTemperaturePS2_Type = Integer32
_AFpsuHwTemperaturePS2_Object = MibScalar
aFpsuHwTemperaturePS2 = _AFpsuHwTemperaturePS2_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 6, 6, 2, 2),
    _AFpsuHwTemperaturePS2_Type()
)
aFpsuHwTemperaturePS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuHwTemperaturePS2.setStatus("current")
_AFpsuOtherStateTable_Object = MibTable
aFpsuOtherStateTable = _AFpsuOtherStateTable_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 7)
)
if mibBuilder.loadTexts:
    aFpsuOtherStateTable.setStatus("current")
_AFpsuOtherStateEntry_Object = MibTableRow
aFpsuOtherStateEntry = _AFpsuOtherStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 7, 1)
)
aFpsuOtherStateEntry.setIndexNames(
    (0, "AMICON-FPSU-MIB", "aFpsuOtherStateIndex"),
)
if mibBuilder.loadTexts:
    aFpsuOtherStateEntry.setStatus("current")
_AFpsuOtherStateIndex_Type = Integer32
_AFpsuOtherStateIndex_Object = MibTableColumn
aFpsuOtherStateIndex = _AFpsuOtherStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 7, 1, 1),
    _AFpsuOtherStateIndex_Type()
)
aFpsuOtherStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuOtherStateIndex.setStatus("current")
_AFpsuOtherStateIp_Type = IpAddress
_AFpsuOtherStateIp_Object = MibTableColumn
aFpsuOtherStateIp = _AFpsuOtherStateIp_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 7, 1, 2),
    _AFpsuOtherStateIp_Type()
)
aFpsuOtherStateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuOtherStateIp.setStatus("current")


class _AFpsuOtherStateSend_Type(Integer32):
    """Custom type aFpsuOtherStateSend based on Integer32"""
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
        *(("nosendrecv", 1),
          ("sendonly", 2),
          ("recvonly", 3),
          ("sendrecv", 4),
          ("waitarp", 5),
          ("waitsynrr", 6),
          ("waitsynok", 7))
    )


_AFpsuOtherStateSend_Type.__name__ = "Integer32"
_AFpsuOtherStateSend_Object = MibTableColumn
aFpsuOtherStateSend = _AFpsuOtherStateSend_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 7, 1, 3),
    _AFpsuOtherStateSend_Type()
)
aFpsuOtherStateSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuOtherStateSend.setStatus("current")


class _AFpsuOtherStateCompression_Type(Integer32):
    """Custom type aFpsuOtherStateCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AFpsuOtherStateCompression_Type.__name__ = "Integer32"
_AFpsuOtherStateCompression_Object = MibTableColumn
aFpsuOtherStateCompression = _AFpsuOtherStateCompression_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 7, 1, 4),
    _AFpsuOtherStateCompression_Type()
)
aFpsuOtherStateCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuOtherStateCompression.setStatus("current")


class _AFpsuOtherStateEncryption_Type(Integer32):
    """Custom type aFpsuOtherStateEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noecncryption", 1),
          ("encription", 2),
          ("packetencryption", 3))
    )


_AFpsuOtherStateEncryption_Type.__name__ = "Integer32"
_AFpsuOtherStateEncryption_Object = MibTableColumn
aFpsuOtherStateEncryption = _AFpsuOtherStateEncryption_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 7, 1, 5),
    _AFpsuOtherStateEncryption_Type()
)
aFpsuOtherStateEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuOtherStateEncryption.setStatus("current")
_AFpsuDrwebState_ObjectIdentity = ObjectIdentity
aFpsuDrwebState = _AFpsuDrwebState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 8)
)
_AFpsuDrwebdCount_Type = Integer32
_AFpsuDrwebdCount_Object = MibScalar
aFpsuDrwebdCount = _AFpsuDrwebdCount_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 8, 1),
    _AFpsuDrwebdCount_Type()
)
aFpsuDrwebdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuDrwebdCount.setStatus("current")
_AFpsuDrwebdMemUsage_Type = Integer32
_AFpsuDrwebdMemUsage_Object = MibScalar
aFpsuDrwebdMemUsage = _AFpsuDrwebdMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 8, 2),
    _AFpsuDrwebdMemUsage_Type()
)
aFpsuDrwebdMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuDrwebdMemUsage.setStatus("current")
_AFpsuDrwebOutSize_Type = Integer32
_AFpsuDrwebOutSize_Object = MibScalar
aFpsuDrwebOutSize = _AFpsuDrwebOutSize_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 8, 3),
    _AFpsuDrwebOutSize_Type()
)
aFpsuDrwebOutSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuDrwebOutSize.setStatus("current")
_AFpsuDrwebInSize_Type = Integer32
_AFpsuDrwebInSize_Object = MibScalar
aFpsuDrwebInSize = _AFpsuDrwebInSize_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 8, 4),
    _AFpsuDrwebInSize_Type()
)
aFpsuDrwebInSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuDrwebInSize.setStatus("current")
_AFpsuDrwebTmpSize_Type = Integer32
_AFpsuDrwebTmpSize_Object = MibScalar
aFpsuDrwebTmpSize = _AFpsuDrwebTmpSize_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 8, 5),
    _AFpsuDrwebTmpSize_Type()
)
aFpsuDrwebTmpSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuDrwebTmpSize.setStatus("current")
_AFpsuDrwebInfectedSize_Type = Integer32
_AFpsuDrwebInfectedSize_Object = MibScalar
aFpsuDrwebInfectedSize = _AFpsuDrwebInfectedSize_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 8, 6),
    _AFpsuDrwebInfectedSize_Type()
)
aFpsuDrwebInfectedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuDrwebInfectedSize.setStatus("current")
_AFpsuDrwebDiskFreeSize_Type = Integer32
_AFpsuDrwebDiskFreeSize_Object = MibScalar
aFpsuDrwebDiskFreeSize = _AFpsuDrwebDiskFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 8, 7),
    _AFpsuDrwebDiskFreeSize_Type()
)
aFpsuDrwebDiskFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuDrwebDiskFreeSize.setStatus("current")
_AFpsuDrwebUpdateTime_Type = DisplayString
_AFpsuDrwebUpdateTime_Object = MibScalar
aFpsuDrwebUpdateTime = _AFpsuDrwebUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 8, 8),
    _AFpsuDrwebUpdateTime_Type()
)
aFpsuDrwebUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuDrwebUpdateTime.setStatus("current")
_AFpsuDrwebKeyExpireTime_Type = DisplayString
_AFpsuDrwebKeyExpireTime_Object = MibScalar
aFpsuDrwebKeyExpireTime = _AFpsuDrwebKeyExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 8, 9),
    _AFpsuDrwebKeyExpireTime_Type()
)
aFpsuDrwebKeyExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuDrwebKeyExpireTime.setStatus("current")
_AFpsuDrwebProcsStateTable_Object = MibTable
aFpsuDrwebProcsStateTable = _AFpsuDrwebProcsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 8, 10)
)
if mibBuilder.loadTexts:
    aFpsuDrwebProcsStateTable.setStatus("current")
_AFpsuDrwebProcsStateEntry_Object = MibTableRow
aFpsuDrwebProcsStateEntry = _AFpsuDrwebProcsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 8, 10, 1)
)
aFpsuDrwebProcsStateEntry.setIndexNames(
    (0, "AMICON-FPSU-MIB", "aFpsuDrwebProcsStateIndex"),
)
if mibBuilder.loadTexts:
    aFpsuDrwebProcsStateEntry.setStatus("current")
_AFpsuDrwebProcsStateIndex_Type = Integer32
_AFpsuDrwebProcsStateIndex_Object = MibTableColumn
aFpsuDrwebProcsStateIndex = _AFpsuDrwebProcsStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 8, 10, 1, 1),
    _AFpsuDrwebProcsStateIndex_Type()
)
aFpsuDrwebProcsStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuDrwebProcsStateIndex.setStatus("current")
_AFpsuDrwebProcsStateName_Type = DisplayString
_AFpsuDrwebProcsStateName_Object = MibTableColumn
aFpsuDrwebProcsStateName = _AFpsuDrwebProcsStateName_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 8, 10, 1, 2),
    _AFpsuDrwebProcsStateName_Type()
)
aFpsuDrwebProcsStateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuDrwebProcsStateName.setStatus("current")
_AFpsuDrwebProcsStateCount_Type = Integer32
_AFpsuDrwebProcsStateCount_Object = MibTableColumn
aFpsuDrwebProcsStateCount = _AFpsuDrwebProcsStateCount_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 8, 10, 1, 3),
    _AFpsuDrwebProcsStateCount_Type()
)
aFpsuDrwebProcsStateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuDrwebProcsStateCount.setStatus("current")
_AFpsuDrwebProcsStateMemory_Type = Integer32
_AFpsuDrwebProcsStateMemory_Object = MibTableColumn
aFpsuDrwebProcsStateMemory = _AFpsuDrwebProcsStateMemory_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 8, 10, 1, 4),
    _AFpsuDrwebProcsStateMemory_Type()
)
aFpsuDrwebProcsStateMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuDrwebProcsStateMemory.setStatus("current")
_AFpsuDrwebProcsStateSockets_Type = Integer32
_AFpsuDrwebProcsStateSockets_Object = MibTableColumn
aFpsuDrwebProcsStateSockets = _AFpsuDrwebProcsStateSockets_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 8, 10, 1, 5),
    _AFpsuDrwebProcsStateSockets_Type()
)
aFpsuDrwebProcsStateSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuDrwebProcsStateSockets.setStatus("current")
_AFpsuFwState_ObjectIdentity = ObjectIdentity
aFpsuFwState = _AFpsuFwState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 9)
)
_AFpsuFwConnCount_Type = Integer32
_AFpsuFwConnCount_Object = MibScalar
aFpsuFwConnCount = _AFpsuFwConnCount_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 9, 1),
    _AFpsuFwConnCount_Type()
)
aFpsuFwConnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuFwConnCount.setStatus("current")
_AFpsuFwTcpCount_Type = Integer32
_AFpsuFwTcpCount_Object = MibScalar
aFpsuFwTcpCount = _AFpsuFwTcpCount_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 9, 2),
    _AFpsuFwTcpCount_Type()
)
aFpsuFwTcpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuFwTcpCount.setStatus("current")
_AFpsuFwUdpCount_Type = Integer32
_AFpsuFwUdpCount_Object = MibScalar
aFpsuFwUdpCount = _AFpsuFwUdpCount_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 9, 3),
    _AFpsuFwUdpCount_Type()
)
aFpsuFwUdpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuFwUdpCount.setStatus("current")
_AFpsuFwIcmpCount_Type = Integer32
_AFpsuFwIcmpCount_Object = MibScalar
aFpsuFwIcmpCount = _AFpsuFwIcmpCount_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 9, 4),
    _AFpsuFwIcmpCount_Type()
)
aFpsuFwIcmpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuFwIcmpCount.setStatus("current")
_AFpsuFwOtherCount_Type = Integer32
_AFpsuFwOtherCount_Object = MibScalar
aFpsuFwOtherCount = _AFpsuFwOtherCount_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 9, 5),
    _AFpsuFwOtherCount_Type()
)
aFpsuFwOtherCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuFwOtherCount.setStatus("current")


class _AFpsuFwTcpFlood_Type(Integer32):
    """Custom type aFpsuFwTcpFlood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("flooddetected", 1))
    )


_AFpsuFwTcpFlood_Type.__name__ = "Integer32"
_AFpsuFwTcpFlood_Object = MibScalar
aFpsuFwTcpFlood = _AFpsuFwTcpFlood_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 9, 6),
    _AFpsuFwTcpFlood_Type()
)
aFpsuFwTcpFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuFwTcpFlood.setStatus("current")


class _AFpsuFwUdpFlood_Type(Integer32):
    """Custom type aFpsuFwUdpFlood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("flooddetected", 1))
    )


_AFpsuFwUdpFlood_Type.__name__ = "Integer32"
_AFpsuFwUdpFlood_Object = MibScalar
aFpsuFwUdpFlood = _AFpsuFwUdpFlood_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 9, 7),
    _AFpsuFwUdpFlood_Type()
)
aFpsuFwUdpFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuFwUdpFlood.setStatus("current")


class _AFpsuFwIcmpFlood_Type(Integer32):
    """Custom type aFpsuFwIcmpFlood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("flooddetected", 1))
    )


_AFpsuFwIcmpFlood_Type.__name__ = "Integer32"
_AFpsuFwIcmpFlood_Object = MibScalar
aFpsuFwIcmpFlood = _AFpsuFwIcmpFlood_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 9, 8),
    _AFpsuFwIcmpFlood_Type()
)
aFpsuFwIcmpFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuFwIcmpFlood.setStatus("current")


class _AFpsuFwOtherFlood_Type(Integer32):
    """Custom type aFpsuFwOtherFlood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("flooddetected", 1))
    )


_AFpsuFwOtherFlood_Type.__name__ = "Integer32"
_AFpsuFwOtherFlood_Object = MibScalar
aFpsuFwOtherFlood = _AFpsuFwOtherFlood_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 9, 9),
    _AFpsuFwOtherFlood_Type()
)
aFpsuFwOtherFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuFwOtherFlood.setStatus("current")
_AFpsuFwMemUsed_Type = Integer32
_AFpsuFwMemUsed_Object = MibScalar
aFpsuFwMemUsed = _AFpsuFwMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 9, 10),
    _AFpsuFwMemUsed_Type()
)
aFpsuFwMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuFwMemUsed.setStatus("current")
_AFpsuFwFiltredPps_Type = Integer32
_AFpsuFwFiltredPps_Object = MibScalar
aFpsuFwFiltredPps = _AFpsuFwFiltredPps_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 9, 11),
    _AFpsuFwFiltredPps_Type()
)
aFpsuFwFiltredPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuFwFiltredPps.setStatus("current")
_AFpsuFwBanned_Type = Integer32
_AFpsuFwBanned_Object = MibScalar
aFpsuFwBanned = _AFpsuFwBanned_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 9, 12),
    _AFpsuFwBanned_Type()
)
aFpsuFwBanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuFwBanned.setStatus("current")
_AFpsuFwBannedTable_Object = MibTable
aFpsuFwBannedTable = _AFpsuFwBannedTable_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 9, 13)
)
if mibBuilder.loadTexts:
    aFpsuFwBannedTable.setStatus("current")
_AFpsuFwBannedTableEntry_Object = MibTableRow
aFpsuFwBannedTableEntry = _AFpsuFwBannedTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 9, 13, 1)
)
aFpsuFwBannedTableEntry.setIndexNames(
    (0, "AMICON-FPSU-MIB", "aFpsuFwBannedTableIndex"),
)
if mibBuilder.loadTexts:
    aFpsuFwBannedTableEntry.setStatus("current")
_AFpsuFwBannedTableIndex_Type = Integer32
_AFpsuFwBannedTableIndex_Object = MibTableColumn
aFpsuFwBannedTableIndex = _AFpsuFwBannedTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 9, 13, 1, 1),
    _AFpsuFwBannedTableIndex_Type()
)
aFpsuFwBannedTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuFwBannedTableIndex.setStatus("current")
_AFpsuFwBannedTableIp_Type = IpAddress
_AFpsuFwBannedTableIp_Object = MibTableColumn
aFpsuFwBannedTableIp = _AFpsuFwBannedTableIp_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 9, 13, 1, 2),
    _AFpsuFwBannedTableIp_Type()
)
aFpsuFwBannedTableIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuFwBannedTableIp.setStatus("current")
_AFpsuLanPortsStateTable_Object = MibTable
aFpsuLanPortsStateTable = _AFpsuLanPortsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 10)
)
if mibBuilder.loadTexts:
    aFpsuLanPortsStateTable.setStatus("current")
_AFpsuLanPortsStateEntry_Object = MibTableRow
aFpsuLanPortsStateEntry = _AFpsuLanPortsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 10, 1)
)
aFpsuLanPortsStateEntry.setIndexNames(
    (0, "AMICON-FPSU-MIB", "aFpsuLanPortsStateIndex"),
)
if mibBuilder.loadTexts:
    aFpsuLanPortsStateEntry.setStatus("current")
_AFpsuLanPortsStateIndex_Type = Integer32
_AFpsuLanPortsStateIndex_Object = MibTableColumn
aFpsuLanPortsStateIndex = _AFpsuLanPortsStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 10, 1, 1),
    _AFpsuLanPortsStateIndex_Type()
)
aFpsuLanPortsStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuLanPortsStateIndex.setStatus("current")
_AFpsuLanPortsStateSpeedIn_Type = Counter64
_AFpsuLanPortsStateSpeedIn_Object = MibTableColumn
aFpsuLanPortsStateSpeedIn = _AFpsuLanPortsStateSpeedIn_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 10, 1, 2),
    _AFpsuLanPortsStateSpeedIn_Type()
)
aFpsuLanPortsStateSpeedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuLanPortsStateSpeedIn.setStatus("current")
_AFpsuLanPortsStateSpeedOut_Type = Counter64
_AFpsuLanPortsStateSpeedOut_Object = MibTableColumn
aFpsuLanPortsStateSpeedOut = _AFpsuLanPortsStateSpeedOut_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 10, 1, 3),
    _AFpsuLanPortsStateSpeedOut_Type()
)
aFpsuLanPortsStateSpeedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuLanPortsStateSpeedOut.setStatus("current")
_AFpsuLanPortsStatePpsIn_Type = Counter64
_AFpsuLanPortsStatePpsIn_Object = MibTableColumn
aFpsuLanPortsStatePpsIn = _AFpsuLanPortsStatePpsIn_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 10, 1, 4),
    _AFpsuLanPortsStatePpsIn_Type()
)
aFpsuLanPortsStatePpsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuLanPortsStatePpsIn.setStatus("current")
_AFpsuLanPortsStatePpsOut_Type = Counter64
_AFpsuLanPortsStatePpsOut_Object = MibTableColumn
aFpsuLanPortsStatePpsOut = _AFpsuLanPortsStatePpsOut_Object(
    (1, 3, 6, 1, 4, 1, 37249, 2, 1, 10, 1, 5),
    _AFpsuLanPortsStatePpsOut_Type()
)
aFpsuLanPortsStatePpsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFpsuLanPortsStatePpsOut.setStatus("current")
_AmiconTraps_ObjectIdentity = ObjectIdentity
amiconTraps = _AmiconTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 3)
)
_AmiconFpsuTraps_ObjectIdentity = ObjectIdentity
amiconFpsuTraps = _AmiconFpsuTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1)
)
_AFpsuIpTraps_ObjectIdentity = ObjectIdentity
aFpsuIpTraps = _AFpsuIpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1)
)
_AFpsuIpSystemTraps_ObjectIdentity = ObjectIdentity
aFpsuIpSystemTraps = _AFpsuIpSystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 1)
)
_AFpsuIpNetTraps_ObjectIdentity = ObjectIdentity
aFpsuIpNetTraps = _AFpsuIpNetTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 2)
)
_AFpsuIpAdminTraps_ObjectIdentity = ObjectIdentity
aFpsuIpAdminTraps = _AFpsuIpAdminTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 3)
)
_AFpsuFwTraps_ObjectIdentity = ObjectIdentity
aFpsuFwTraps = _AFpsuFwTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 4)
)

# Managed Objects groups


# Notification objects

aFpsuTrapStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aFpsuTrapStop.setStatus(
        "current"
    )

aFpsuTrapHotReserve = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 1, 2)
)
aFpsuTrapHotReserve.setObjects(
      *(("AMICON-FPSU-MIB", "aFpsuHotReserveStateLocalRole"),
        ("AMICON-FPSU-MIB", "aFpsuHotReserveStateRemoteRole"))
)
if mibBuilder.loadTexts:
    aFpsuTrapHotReserve.setStatus(
        "current"
    )

aFpsuTrapCpuLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 1, 3)
)
aFpsuTrapCpuLoad.setObjects(
    ("AMICON-FPSU-MIB", "aFpsuHwCpuLoad")
)
if mibBuilder.loadTexts:
    aFpsuTrapCpuLoad.setStatus(
        "current"
    )

aFpsuTrapOverTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 1, 4)
)
aFpsuTrapOverTemp.setObjects(
      *(("AMICON-FPSU-MIB", "aFpsuHwCpuTemperature"),
        ("AMICON-FPSU-MIB", "aFpsuHwMBTemperature"))
)
if mibBuilder.loadTexts:
    aFpsuTrapOverTemp.setStatus(
        "current"
    )

aFpsuTrapDiskError = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    aFpsuTrapDiskError.setStatus(
        "current"
    )

aFpsuTrapHotReserveNoLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    aFpsuTrapHotReserveNoLink.setStatus(
        "current"
    )

aFpsuTrapSupportEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 1, 7)
)
aFpsuTrapSupportEnd.setObjects(
    ("AMICON-FPSU-MIB", "aFpsuSwEndSupportDate")
)
if mibBuilder.loadTexts:
    aFpsuTrapSupportEnd.setStatus(
        "current"
    )

aFpsuTrapAlive = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    aFpsuTrapAlive.setStatus(
        "current"
    )

aFpsuTrapOtherLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 2, 1)
)
aFpsuTrapOtherLinkDown.setObjects(
      *(("AMICON-FPSU-MIB", "aFpsuOtherStateIndex"),
        ("AMICON-FPSU-MIB", "aFpsuOtherStateIp"))
)
if mibBuilder.loadTexts:
    aFpsuTrapOtherLinkDown.setStatus(
        "current"
    )

aFpsuTrapOtherLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 2, 2)
)
aFpsuTrapOtherLinkUp.setObjects(
      *(("AMICON-FPSU-MIB", "aFpsuOtherStateIndex"),
        ("AMICON-FPSU-MIB", "aFpsuOtherStateIp"))
)
if mibBuilder.loadTexts:
    aFpsuTrapOtherLinkUp.setStatus(
        "current"
    )

aFpsuTrapClientConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 2, 3)
)
aFpsuTrapClientConnect.setObjects(
      *(("AMICON-FPSU-MIB", "aFpsuClientStateName"),
        ("AMICON-FPSU-MIB", "aFpsuClientStateRealIp"),
        ("AMICON-FPSU-MIB", "aFpsuClientStateLanPort"))
)
if mibBuilder.loadTexts:
    aFpsuTrapClientConnect.setStatus(
        "current"
    )

aFpsuTrapClientDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 2, 4)
)
aFpsuTrapClientDisconnect.setObjects(
      *(("AMICON-FPSU-MIB", "aFpsuClientStateName"),
        ("AMICON-FPSU-MIB", "aFpsuClientStateRealIp"),
        ("AMICON-FPSU-MIB", "aFpsuClientStateLanPort"))
)
if mibBuilder.loadTexts:
    aFpsuTrapClientDisconnect.setStatus(
        "current"
    )

aFpsuTrapRadmGetConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 3, 1)
)
aFpsuTrapRadmGetConfig.setObjects(
      *(("AMICON-FPSU-MIB", "aFpsuAdminName"),
        ("AMICON-FPSU-MIB", "aFpsuAdminStateIp"),
        ("AMICON-FPSU-MIB", "aFpsuAdminStatePort"))
)
if mibBuilder.loadTexts:
    aFpsuTrapRadmGetConfig.setStatus(
        "current"
    )

aFpsuTrapRadmChangeConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 3, 2)
)
aFpsuTrapRadmChangeConfig.setObjects(
      *(("AMICON-FPSU-MIB", "aFpsuAdminName"),
        ("AMICON-FPSU-MIB", "aFpsuAdminStateIp"),
        ("AMICON-FPSU-MIB", "aFpsuAdminStatePort"))
)
if mibBuilder.loadTexts:
    aFpsuTrapRadmChangeConfig.setStatus(
        "current"
    )

aFpsuTrapRadmPutKeys = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 3, 3)
)
aFpsuTrapRadmPutKeys.setObjects(
      *(("AMICON-FPSU-MIB", "aFpsuAdminName"),
        ("AMICON-FPSU-MIB", "aFpsuAdminStateIp"),
        ("AMICON-FPSU-MIB", "aFpsuAdminStatePort"))
)
if mibBuilder.loadTexts:
    aFpsuTrapRadmPutKeys.setStatus(
        "current"
    )

aFpsuTrapRadmDelKeys = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 3, 4)
)
aFpsuTrapRadmDelKeys.setObjects(
      *(("AMICON-FPSU-MIB", "aFpsuAdminName"),
        ("AMICON-FPSU-MIB", "aFpsuAdminStateIp"),
        ("AMICON-FPSU-MIB", "aFpsuAdminStatePort"))
)
if mibBuilder.loadTexts:
    aFpsuTrapRadmDelKeys.setStatus(
        "current"
    )

aFpsuTrapRadmPutClientsKey = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 3, 5)
)
aFpsuTrapRadmPutClientsKey.setObjects(
      *(("AMICON-FPSU-MIB", "aFpsuAdminName"),
        ("AMICON-FPSU-MIB", "aFpsuAdminStateIp"),
        ("AMICON-FPSU-MIB", "aFpsuAdminStatePort"))
)
if mibBuilder.loadTexts:
    aFpsuTrapRadmPutClientsKey.setStatus(
        "current"
    )

aFpsuTrapRadmDelClientsKey = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 3, 6)
)
aFpsuTrapRadmDelClientsKey.setObjects(
      *(("AMICON-FPSU-MIB", "aFpsuAdminName"),
        ("AMICON-FPSU-MIB", "aFpsuAdminStateIp"),
        ("AMICON-FPSU-MIB", "aFpsuAdminStatePort"))
)
if mibBuilder.loadTexts:
    aFpsuTrapRadmDelClientsKey.setStatus(
        "current"
    )

aFpsuTrapRadmReBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 3, 7)
)
aFpsuTrapRadmReBoot.setObjects(
      *(("AMICON-FPSU-MIB", "aFpsuAdminName"),
        ("AMICON-FPSU-MIB", "aFpsuAdminStateIp"),
        ("AMICON-FPSU-MIB", "aFpsuAdminStatePort"))
)
if mibBuilder.loadTexts:
    aFpsuTrapRadmReBoot.setStatus(
        "current"
    )

aFpsuTrapRadmClock = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 3, 8)
)
aFpsuTrapRadmClock.setObjects(
      *(("AMICON-FPSU-MIB", "aFpsuAdminName"),
        ("AMICON-FPSU-MIB", "aFpsuAdminStateIp"),
        ("AMICON-FPSU-MIB", "aFpsuAdminStatePort"))
)
if mibBuilder.loadTexts:
    aFpsuTrapRadmClock.setStatus(
        "current"
    )

aFpsuTrapFwBann = NotificationType(
    (1, 3, 6, 1, 4, 1, 37249, 3, 1, 1, 4, 1)
)
aFpsuTrapFwBann.setObjects(
    ("AMICON-FPSU-MIB", "aFpsuFwBannedTableIp")
)
if mibBuilder.loadTexts:
    aFpsuTrapFwBann.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AMICON-FPSU-MIB",
    **{"amicon": amicon,
       "amiconProducts": amiconProducts,
       "amiconFpsu": amiconFpsu,
       "amiconFpsuIp": amiconFpsuIp,
       "amiconFpsuIpSysObjectID": amiconFpsuIpSysObjectID,
       "aFpsuInfo": aFpsuInfo,
       "aFpsuSerialNumber": aFpsuSerialNumber,
       "aFpsuBuildDate": aFpsuBuildDate,
       "aFpsuHardware": aFpsuHardware,
       "aFpsuHwSystem": aFpsuHwSystem,
       "aFpsuHwSystemManufacturer": aFpsuHwSystemManufacturer,
       "aFpsuHwSystemName": aFpsuHwSystemName,
       "aFpsuHwSystemSerialNumber": aFpsuHwSystemSerialNumber,
       "aFpsuHwSystemWakeUpType": aFpsuHwSystemWakeUpType,
       "aFpsuHwMainboard": aFpsuHwMainboard,
       "aFpsuHwMainboardManufacturer": aFpsuHwMainboardManufacturer,
       "aFpsuHwMainboardName": aFpsuHwMainboardName,
       "aFpsuHwMainboardVersion": aFpsuHwMainboardVersion,
       "aFpsuHwMainboardSerialNumber": aFpsuHwMainboardSerialNumber,
       "aFpsuHwMainboardAssetTag": aFpsuHwMainboardAssetTag,
       "aFpsuHwBios": aFpsuHwBios,
       "aFpsuHwBiosVendor": aFpsuHwBiosVendor,
       "aFpsuHwBiosVersion": aFpsuHwBiosVersion,
       "aFpsuHwBiosReleaseDate": aFpsuHwBiosReleaseDate,
       "aFpsuHwBiosRevision": aFpsuHwBiosRevision,
       "aFpsuHwBiosFirmware": aFpsuHwBiosFirmware,
       "aFpsuHwMemory": aFpsuHwMemory,
       "aFpsuHwMemoryRamMbs": aFpsuHwMemoryRamMbs,
       "aFpsuHwSensors": aFpsuHwSensors,
       "aFpsuHwVoltageProbe": aFpsuHwVoltageProbe,
       "aFpsuHwTemperatureProbe": aFpsuHwTemperatureProbe,
       "aFpsuHwCpuInfoTable": aFpsuHwCpuInfoTable,
       "aFpsuHwCpuInfoEntry": aFpsuHwCpuInfoEntry,
       "aFpsuHwCpuInfoIndex": aFpsuHwCpuInfoIndex,
       "aFpsuHwCpuInfoSocket": aFpsuHwCpuInfoSocket,
       "aFpsuHwCpuInfoType": aFpsuHwCpuInfoType,
       "aFpsuHwCpuInfoFamily": aFpsuHwCpuInfoFamily,
       "aFpsuHwCpuInfoManufacturer": aFpsuHwCpuInfoManufacturer,
       "aFpsuHwCpuInfoSignature": aFpsuHwCpuInfoSignature,
       "aFpsuHwCpuInfoVersion": aFpsuHwCpuInfoVersion,
       "aFpsuHwCpuInfoMaxSpeed": aFpsuHwCpuInfoMaxSpeed,
       "aFpsuHwCpuInfoCurrentSpeed": aFpsuHwCpuInfoCurrentSpeed,
       "aFpsuHwCpuInfoCoreCount": aFpsuHwCpuInfoCoreCount,
       "aFpsuHwCpuInfoCoreEnabled": aFpsuHwCpuInfoCoreEnabled,
       "aFpsuHwCpuInfoThreadCount": aFpsuHwCpuInfoThreadCount,
       "aFpsuHwSmartInfoTable": aFpsuHwSmartInfoTable,
       "aFpsuHwSmartInfoEntry": aFpsuHwSmartInfoEntry,
       "aFpsuHwSmartInfoIndex": aFpsuHwSmartInfoIndex,
       "aFpsuHwSmartInfoDev": aFpsuHwSmartInfoDev,
       "aFpsuHwSmartInfoId": aFpsuHwSmartInfoId,
       "aFpsuHwSmartInfoName": aFpsuHwSmartInfoName,
       "aFpsuHwSmartInfoValue": aFpsuHwSmartInfoValue,
       "aFpsuHwSmartInfoWorst": aFpsuHwSmartInfoWorst,
       "aFpsuHwSmartInfoThresholds": aFpsuHwSmartInfoThresholds,
       "aFpsuHwSmartInfoType": aFpsuHwSmartInfoType,
       "aFpsuHwSmartInfoUpdated": aFpsuHwSmartInfoUpdated,
       "aFpsuHwSmartInfoFailed": aFpsuHwSmartInfoFailed,
       "aFpsuSoftware": aFpsuSoftware,
       "aFpsuSwVer": aFpsuSwVer,
       "aFpsuSwInstallationDate": aFpsuSwInstallationDate,
       "aFpsuSwEndSupportDate": aFpsuSwEndSupportDate,
       "amiconState": amiconState,
       "aFpsuState": aFpsuState,
       "aFpsuMemoryUse": aFpsuMemoryUse,
       "aFpsuMemoryUseTable": aFpsuMemoryUseTable,
       "aFpsuMemoryUseEntry": aFpsuMemoryUseEntry,
       "aFpsuMemoryUseIndex": aFpsuMemoryUseIndex,
       "aFpsuMemoryUseArpMin": aFpsuMemoryUseArpMin,
       "aFpsuMemoryUseArpMax": aFpsuMemoryUseArpMax,
       "aFpsuMemoryUseArpNow": aFpsuMemoryUseArpNow,
       "aFpsuMemoryUseRecvMin": aFpsuMemoryUseRecvMin,
       "aFpsuMemoryUseRecvMax": aFpsuMemoryUseRecvMax,
       "aFpsuMemoryUseRecvNow": aFpsuMemoryUseRecvNow,
       "aFpsuMemoryUseSendMin": aFpsuMemoryUseSendMin,
       "aFpsuMemoryUseSendMax": aFpsuMemoryUseSendMax,
       "aFpsuMemoryUseSendNow": aFpsuMemoryUseSendNow,
       "aFpsuMemoryTotal": aFpsuMemoryTotal,
       "aFpsuMemoryFree": aFpsuMemoryFree,
       "aFpsuUserStateTable": aFpsuUserStateTable,
       "aFpsuUserStateEntry": aFpsuUserStateEntry,
       "aFpsuUserStateIndex": aFpsuUserStateIndex,
       "aFpsuUserStateFirstIp": aFpsuUserStateFirstIp,
       "aFpsuUserStateFirstWithFpsu": aFpsuUserStateFirstWithFpsu,
       "aFpsuUserStateSecondIp": aFpsuUserStateSecondIp,
       "aFpsuUserStateSecondWithFpsu": aFpsuUserStateSecondWithFpsu,
       "aFpsuUserStateRecvSrcBytes": aFpsuUserStateRecvSrcBytes,
       "aFpsuUserStateRecvDstBytes": aFpsuUserStateRecvDstBytes,
       "aFpsuUserStateError": aFpsuUserStateError,
       "aFpsuAdminStateTable": aFpsuAdminStateTable,
       "aFpsuAdminStateEntry": aFpsuAdminStateEntry,
       "aFpsuAdminStateIndex": aFpsuAdminStateIndex,
       "aFpsuAdminName": aFpsuAdminName,
       "aFpsuAdminPackedName": aFpsuAdminPackedName,
       "aFpsuAdminStateIp": aFpsuAdminStateIp,
       "aFpsuAdminStatePort": aFpsuAdminStatePort,
       "aFpsuAdminStatePacketsIn": aFpsuAdminStatePacketsIn,
       "aFpsuAdminStatePacketsOut": aFpsuAdminStatePacketsOut,
       "aFpsuAdminStateDataIn": aFpsuAdminStateDataIn,
       "aFpsuAdminStateDataOut": aFpsuAdminStateDataOut,
       "aFpsuAdminStateErrors": aFpsuAdminStateErrors,
       "aFpsuAdminStateMtu": aFpsuAdminStateMtu,
       "aFpsuAdminStateLastRequest": aFpsuAdminStateLastRequest,
       "aFpsuClientStateTable": aFpsuClientStateTable,
       "aFpsuClientStateEntry": aFpsuClientStateEntry,
       "aFpsuClientStateIndex": aFpsuClientStateIndex,
       "aFpsuClientStateName": aFpsuClientStateName,
       "aFpsuClientStateMac": aFpsuClientStateMac,
       "aFpsuClientStateRealIp": aFpsuClientStateRealIp,
       "aFpsuClientStatePrivateIp": aFpsuClientStatePrivateIp,
       "aFpsuClientStateLanPort": aFpsuClientStateLanPort,
       "aFpsuClientStateCenter": aFpsuClientStateCenter,
       "aFpsuClientStateNumber": aFpsuClientStateNumber,
       "aFpsuClientStateGroup": aFpsuClientStateGroup,
       "aFpsuClientStateDataIn": aFpsuClientStateDataIn,
       "aFpsuClientStateDataOut": aFpsuClientStateDataOut,
       "aFpsuClientStatePacketsIn": aFpsuClientStatePacketsIn,
       "aFpsuClientStatePacketsOut": aFpsuClientStatePacketsOut,
       "aFpsuClientStateTunnelOpenTime": aFpsuClientStateTunnelOpenTime,
       "aFpsuClientStateLastExchangeTime": aFpsuClientStateLastExchangeTime,
       "aFpsuHotReserveState": aFpsuHotReserveState,
       "aFpsuHotReserveStateVpn": aFpsuHotReserveStateVpn,
       "aFpsuHotReserveStateLocalRole": aFpsuHotReserveStateLocalRole,
       "aFpsuHotReserveStateRemoteRole": aFpsuHotReserveStateRemoteRole,
       "aFpsuHotReserveStateRemoteMac": aFpsuHotReserveStateRemoteMac,
       "aFpsuHotReserveStateLink": aFpsuHotReserveStateLink,
       "aFpsuHotReserveStateWork": aFpsuHotReserveStateWork,
       "aFpsuHardwareState": aFpsuHardwareState,
       "aFpsuHwWatchDog": aFpsuHwWatchDog,
       "aFpsuHardwareFanState": aFpsuHardwareFanState,
       "aFpsuHwFan1Speed": aFpsuHwFan1Speed,
       "aFpsuHwFan2Speed": aFpsuHwFan2Speed,
       "aFpsuHwFan3Speed": aFpsuHwFan3Speed,
       "aFpsuHardwareTemperatureState": aFpsuHardwareTemperatureState,
       "aFpsuHwCpuTemperature": aFpsuHwCpuTemperature,
       "aFpsuHwMBTemperature": aFpsuHwMBTemperature,
       "aFpsuHardwareVoltageState": aFpsuHardwareVoltageState,
       "aFpsuHwPowerVoltage3": aFpsuHwPowerVoltage3,
       "aFpsuHwPowerVoltage5": aFpsuHwPowerVoltage5,
       "aFpsuHwPowerVoltage12": aFpsuHwPowerVoltage12,
       "aFpsuHwCpuLoad": aFpsuHwCpuLoad,
       "aFpsuHardwarePowerSupplyState": aFpsuHardwarePowerSupplyState,
       "aFpsuHardwarePowerSupply1State": aFpsuHardwarePowerSupply1State,
       "aFpsuHwPowerPS1": aFpsuHwPowerPS1,
       "aFpsuHwTemperaturePS1": aFpsuHwTemperaturePS1,
       "aFpsuHardwarePowerSupply2State": aFpsuHardwarePowerSupply2State,
       "aFpsuHwPowerPS2": aFpsuHwPowerPS2,
       "aFpsuHwTemperaturePS2": aFpsuHwTemperaturePS2,
       "aFpsuOtherStateTable": aFpsuOtherStateTable,
       "aFpsuOtherStateEntry": aFpsuOtherStateEntry,
       "aFpsuOtherStateIndex": aFpsuOtherStateIndex,
       "aFpsuOtherStateIp": aFpsuOtherStateIp,
       "aFpsuOtherStateSend": aFpsuOtherStateSend,
       "aFpsuOtherStateCompression": aFpsuOtherStateCompression,
       "aFpsuOtherStateEncryption": aFpsuOtherStateEncryption,
       "aFpsuDrwebState": aFpsuDrwebState,
       "aFpsuDrwebdCount": aFpsuDrwebdCount,
       "aFpsuDrwebdMemUsage": aFpsuDrwebdMemUsage,
       "aFpsuDrwebOutSize": aFpsuDrwebOutSize,
       "aFpsuDrwebInSize": aFpsuDrwebInSize,
       "aFpsuDrwebTmpSize": aFpsuDrwebTmpSize,
       "aFpsuDrwebInfectedSize": aFpsuDrwebInfectedSize,
       "aFpsuDrwebDiskFreeSize": aFpsuDrwebDiskFreeSize,
       "aFpsuDrwebUpdateTime": aFpsuDrwebUpdateTime,
       "aFpsuDrwebKeyExpireTime": aFpsuDrwebKeyExpireTime,
       "aFpsuDrwebProcsStateTable": aFpsuDrwebProcsStateTable,
       "aFpsuDrwebProcsStateEntry": aFpsuDrwebProcsStateEntry,
       "aFpsuDrwebProcsStateIndex": aFpsuDrwebProcsStateIndex,
       "aFpsuDrwebProcsStateName": aFpsuDrwebProcsStateName,
       "aFpsuDrwebProcsStateCount": aFpsuDrwebProcsStateCount,
       "aFpsuDrwebProcsStateMemory": aFpsuDrwebProcsStateMemory,
       "aFpsuDrwebProcsStateSockets": aFpsuDrwebProcsStateSockets,
       "aFpsuFwState": aFpsuFwState,
       "aFpsuFwConnCount": aFpsuFwConnCount,
       "aFpsuFwTcpCount": aFpsuFwTcpCount,
       "aFpsuFwUdpCount": aFpsuFwUdpCount,
       "aFpsuFwIcmpCount": aFpsuFwIcmpCount,
       "aFpsuFwOtherCount": aFpsuFwOtherCount,
       "aFpsuFwTcpFlood": aFpsuFwTcpFlood,
       "aFpsuFwUdpFlood": aFpsuFwUdpFlood,
       "aFpsuFwIcmpFlood": aFpsuFwIcmpFlood,
       "aFpsuFwOtherFlood": aFpsuFwOtherFlood,
       "aFpsuFwMemUsed": aFpsuFwMemUsed,
       "aFpsuFwFiltredPps": aFpsuFwFiltredPps,
       "aFpsuFwBanned": aFpsuFwBanned,
       "aFpsuFwBannedTable": aFpsuFwBannedTable,
       "aFpsuFwBannedTableEntry": aFpsuFwBannedTableEntry,
       "aFpsuFwBannedTableIndex": aFpsuFwBannedTableIndex,
       "aFpsuFwBannedTableIp": aFpsuFwBannedTableIp,
       "aFpsuLanPortsStateTable": aFpsuLanPortsStateTable,
       "aFpsuLanPortsStateEntry": aFpsuLanPortsStateEntry,
       "aFpsuLanPortsStateIndex": aFpsuLanPortsStateIndex,
       "aFpsuLanPortsStateSpeedIn": aFpsuLanPortsStateSpeedIn,
       "aFpsuLanPortsStateSpeedOut": aFpsuLanPortsStateSpeedOut,
       "aFpsuLanPortsStatePpsIn": aFpsuLanPortsStatePpsIn,
       "aFpsuLanPortsStatePpsOut": aFpsuLanPortsStatePpsOut,
       "amiconTraps": amiconTraps,
       "amiconFpsuTraps": amiconFpsuTraps,
       "aFpsuIpTraps": aFpsuIpTraps,
       "aFpsuIpSystemTraps": aFpsuIpSystemTraps,
       "aFpsuTrapStop": aFpsuTrapStop,
       "aFpsuTrapHotReserve": aFpsuTrapHotReserve,
       "aFpsuTrapCpuLoad": aFpsuTrapCpuLoad,
       "aFpsuTrapOverTemp": aFpsuTrapOverTemp,
       "aFpsuTrapDiskError": aFpsuTrapDiskError,
       "aFpsuTrapHotReserveNoLink": aFpsuTrapHotReserveNoLink,
       "aFpsuTrapSupportEnd": aFpsuTrapSupportEnd,
       "aFpsuTrapAlive": aFpsuTrapAlive,
       "aFpsuIpNetTraps": aFpsuIpNetTraps,
       "aFpsuTrapOtherLinkDown": aFpsuTrapOtherLinkDown,
       "aFpsuTrapOtherLinkUp": aFpsuTrapOtherLinkUp,
       "aFpsuTrapClientConnect": aFpsuTrapClientConnect,
       "aFpsuTrapClientDisconnect": aFpsuTrapClientDisconnect,
       "aFpsuIpAdminTraps": aFpsuIpAdminTraps,
       "aFpsuTrapRadmGetConfig": aFpsuTrapRadmGetConfig,
       "aFpsuTrapRadmChangeConfig": aFpsuTrapRadmChangeConfig,
       "aFpsuTrapRadmPutKeys": aFpsuTrapRadmPutKeys,
       "aFpsuTrapRadmDelKeys": aFpsuTrapRadmDelKeys,
       "aFpsuTrapRadmPutClientsKey": aFpsuTrapRadmPutClientsKey,
       "aFpsuTrapRadmDelClientsKey": aFpsuTrapRadmDelClientsKey,
       "aFpsuTrapRadmReBoot": aFpsuTrapRadmReBoot,
       "aFpsuTrapRadmClock": aFpsuTrapRadmClock,
       "aFpsuFwTraps": aFpsuFwTraps,
       "aFpsuTrapFwBann": aFpsuTrapFwBann}
)
