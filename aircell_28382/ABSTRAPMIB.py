# SNMP MIB module (ABSTRAPMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/aircell_28382/ABSTRAPMIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:18:40 2025
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

(aacuHardwareSerialNumber,
 abpVersion,
 absAcpuBatchVersion,
 absAcpuCldOperStatus,
 absAcpuCldUsbAdminStatus,
 absActiveVideoDownloads,
 absAircardPNOffset,
 absAircardPilotPNASP,
 absAircardPilotStrength,
 absAircardRx0AGC,
 absAircardRx1AGC,
 absAircardSectorID,
 absAircardSignalStrength,
 absAircardTxAGC,
 absAtgClientCount,
 absKUSignalStrength,
 absOperationalStatus,
 absSBBLinkStatus,
 absSBBOperStatus,
 absSBBSignalStrength,
 absSoftwareVersion,
 absSystemMode,
 absTotalActiveClientCount,
 absTotalClientCount,
 absVSMOperStatus,
 absVideoServiceState,
 absWhitelistVersion,
 acpu429PitchAngle,
 acpuAtgModemLinkStatus,
 acpuBios,
 acpuEthernetPortState,
 acpuEthernetPortVlanID,
 acpuHardwareSerialNumber,
 acpuInfo,
 acpuPriABSDataSrvAddr,
 acpuSnortDstIp,
 acpuSnortDstPort,
 acpuSnortProtocol,
 acpuSnortSrcIp,
 acpuSnortSrcPort,
 acpuVenturiClientStatus,
 acpuVenturiTunnelModeAdminStatus,
 acpuVenturiTunnelStatus,
 acpugpsAltitude,
 acpugpsLatitude,
 acpugpsLongitude,
 acpugpsUTCTime,
 aircardEsn,
 aircardInfo,
 aircraftTailNum,
 aircraftType,
 airlineName,
 auxcardInfo,
 cwap1Info,
 cwap2Info,
 cwap3Info,
 cwap4Info,
 cwap5Info,
 cwap6Info,
 cwap7Info,
 cwap8Info,
 cwapType,
 egcPortIndex,
 egcPortVlanID,
 meruControllerInfo,
 passurHealthStatus,
 satelliteSupport,
 sbbPacketErrorRate,
 venturiInfo,
 wapCount,
 weightonWheelsSupport) = mibBuilder.importSymbols(
    "AIRCELL-ACPU-SNMP-MIB",
    "aacuHardwareSerialNumber",
    "abpVersion",
    "absAcpuBatchVersion",
    "absAcpuCldOperStatus",
    "absAcpuCldUsbAdminStatus",
    "absActiveVideoDownloads",
    "absAircardPNOffset",
    "absAircardPilotPNASP",
    "absAircardPilotStrength",
    "absAircardRx0AGC",
    "absAircardRx1AGC",
    "absAircardSectorID",
    "absAircardSignalStrength",
    "absAircardTxAGC",
    "absAtgClientCount",
    "absKUSignalStrength",
    "absOperationalStatus",
    "absSBBLinkStatus",
    "absSBBOperStatus",
    "absSBBSignalStrength",
    "absSoftwareVersion",
    "absSystemMode",
    "absTotalActiveClientCount",
    "absTotalClientCount",
    "absVSMOperStatus",
    "absVideoServiceState",
    "absWhitelistVersion",
    "acpu429PitchAngle",
    "acpuAtgModemLinkStatus",
    "acpuBios",
    "acpuEthernetPortState",
    "acpuEthernetPortVlanID",
    "acpuHardwareSerialNumber",
    "acpuInfo",
    "acpuPriABSDataSrvAddr",
    "acpuSnortDstIp",
    "acpuSnortDstPort",
    "acpuSnortProtocol",
    "acpuSnortSrcIp",
    "acpuSnortSrcPort",
    "acpuVenturiClientStatus",
    "acpuVenturiTunnelModeAdminStatus",
    "acpuVenturiTunnelStatus",
    "acpugpsAltitude",
    "acpugpsLatitude",
    "acpugpsLongitude",
    "acpugpsUTCTime",
    "aircardEsn",
    "aircardInfo",
    "aircraftTailNum",
    "aircraftType",
    "airlineName",
    "auxcardInfo",
    "cwap1Info",
    "cwap2Info",
    "cwap3Info",
    "cwap4Info",
    "cwap5Info",
    "cwap6Info",
    "cwap7Info",
    "cwap8Info",
    "cwapType",
    "egcPortIndex",
    "egcPortVlanID",
    "meruControllerInfo",
    "passurHealthStatus",
    "satelliteSupport",
    "sbbPacketErrorRate",
    "venturiInfo",
    "wapCount",
    "weightonWheelsSupport")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aircellLLC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28382)
)
if mibBuilder.loadTexts:
    aircellLLC.setRevisions(
        ("2012-06-03 17:30",
         "2012-05-03 17:30",
         "2012-01-05 06:30",
         "2011-11-02 06:30",
         "2011-03-03 15:30",
         "2011-01-03 23:07",
         "2010-06-04 18:02",
         "2007-08-08 22:27")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AircellABS_ObjectIdentity = ObjectIdentity
aircellABS = _AircellABS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1)
)
_AircellABSTrap_ObjectIdentity = ObjectIdentity
aircellABSTrap = _AircellABSTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6)
)
_AbsTrapControl_ObjectIdentity = ObjectIdentity
absTrapControl = _AbsTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1)
)
_AcpuSetTrap_Type = Integer32
_AcpuSetTrap_Object = MibScalar
acpuSetTrap = _AcpuSetTrap_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 1),
    _AcpuSetTrap_Type()
)
acpuSetTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpuSetTrap.setStatus("obsolete")


class _AbsHelloTrapType_Type(Integer32):
    """Custom type absHelloTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hello", 1),
          ("goodbye", 2))
    )


_AbsHelloTrapType_Type.__name__ = "Integer32"
_AbsHelloTrapType_Object = MibScalar
absHelloTrapType = _AbsHelloTrapType_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 2),
    _AbsHelloTrapType_Type()
)
absHelloTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absHelloTrapType.setStatus("current")


class _AbsDeviceId_Type(Integer32):
    """Custom type absDeviceId based on Integer32"""
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
        *(("wap", 1),
          ("wiredhandset", 2),
          ("wirelesshandset", 3),
          ("acpu", 4),
          ("egc", 5),
          ("atg", 6),
          ("tm", 7),
          ("aux", 8),
          ("gps", 9),
          ("merucontroller", 10),
          ("videohdd", 11),
          ("contentloader", 12))
    )


_AbsDeviceId_Type.__name__ = "Integer32"
_AbsDeviceId_Object = MibScalar
absDeviceId = _AbsDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 3),
    _AbsDeviceId_Type()
)
absDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absDeviceId.setStatus("current")
_AbsLRUDeviceNoId_Type = Integer32
_AbsLRUDeviceNoId_Object = MibScalar
absLRUDeviceNoId = _AbsLRUDeviceNoId_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 4),
    _AbsLRUDeviceNoId_Type()
)
absLRUDeviceNoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absLRUDeviceNoId.setStatus("current")


class _AbsUnitOperState_Type(Integer32):
    """Custom type absUnitOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("degraded", 3))
    )


_AbsUnitOperState_Type.__name__ = "Integer32"
_AbsUnitOperState_Object = MibScalar
absUnitOperState = _AbsUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 5),
    _AbsUnitOperState_Type()
)
absUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absUnitOperState.setStatus("current")
_AbsacpuTemperature_Type = Integer32
_AbsacpuTemperature_Object = MibScalar
absacpuTemperature = _AbsacpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 6),
    _AbsacpuTemperature_Type()
)
absacpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuTemperature.setStatus("current")


class _AbsacpuErrorReason_Type(Integer32):
    """Custom type absacpuErrorReason based on Integer32"""
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
        *(("gpsInvalidData", 1),
          ("communicationLoss", 2),
          ("firstDeviceReset", 3),
          ("lastFailedReset", 4),
          ("dataServerNotAvailable", 5),
          ("ftpUserIdPasswordError", 6),
          ("ftpAbort", 7),
          ("sWActiviationError", 8))
    )


_AbsacpuErrorReason_Type.__name__ = "Integer32"
_AbsacpuErrorReason_Object = MibScalar
absacpuErrorReason = _AbsacpuErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 7),
    _AbsacpuErrorReason_Type()
)
absacpuErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuErrorReason.setStatus("current")


class _AbsacpuMemoryUsage_Type(Integer32):
    """Custom type absacpuMemoryUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AbsacpuMemoryUsage_Type.__name__ = "Integer32"
_AbsacpuMemoryUsage_Object = MibScalar
absacpuMemoryUsage = _AbsacpuMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 8),
    _AbsacpuMemoryUsage_Type()
)
absacpuMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuMemoryUsage.setStatus("current")


class _AbsacpuUserCPUUsage_Type(Integer32):
    """Custom type absacpuUserCPUUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AbsacpuUserCPUUsage_Type.__name__ = "Integer32"
_AbsacpuUserCPUUsage_Object = MibScalar
absacpuUserCPUUsage = _AbsacpuUserCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 9),
    _AbsacpuUserCPUUsage_Type()
)
absacpuUserCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuUserCPUUsage.setStatus("current")
_AbsacpuSystemCPUUsage_Type = Integer32
_AbsacpuSystemCPUUsage_Object = MibScalar
absacpuSystemCPUUsage = _AbsacpuSystemCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 10),
    _AbsacpuSystemCPUUsage_Type()
)
absacpuSystemCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuSystemCPUUsage.setStatus("current")


class _AbsacpuPagingSpace_Type(Integer32):
    """Custom type absacpuPagingSpace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_AbsacpuPagingSpace_Type.__name__ = "Integer32"
_AbsacpuPagingSpace_Object = MibScalar
absacpuPagingSpace = _AbsacpuPagingSpace_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 11),
    _AbsacpuPagingSpace_Type()
)
absacpuPagingSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuPagingSpace.setStatus("current")


class _AbsacpuFlashDiskSpace_Type(Integer32):
    """Custom type absacpuFlashDiskSpace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AbsacpuFlashDiskSpace_Type.__name__ = "Integer32"
_AbsacpuFlashDiskSpace_Object = MibScalar
absacpuFlashDiskSpace = _AbsacpuFlashDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 12),
    _AbsacpuFlashDiskSpace_Type()
)
absacpuFlashDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuFlashDiskSpace.setStatus("current")


class _AbsacpuHardDiskSpace_Type(Integer32):
    """Custom type absacpuHardDiskSpace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AbsacpuHardDiskSpace_Type.__name__ = "Integer32"
_AbsacpuHardDiskSpace_Object = MibScalar
absacpuHardDiskSpace = _AbsacpuHardDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 13),
    _AbsacpuHardDiskSpace_Type()
)
absacpuHardDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuHardDiskSpace.setStatus("current")
_AbsacpuNoofProcesses_Type = Integer32
_AbsacpuNoofProcesses_Object = MibScalar
absacpuNoofProcesses = _AbsacpuNoofProcesses_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 14),
    _AbsacpuNoofProcesses_Type()
)
absacpuNoofProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuNoofProcesses.setStatus("current")


class _AbsacpuProcessOpState_Type(Integer32):
    """Custom type absacpuProcessOpState based on Integer32"""
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


_AbsacpuProcessOpState_Type.__name__ = "Integer32"
_AbsacpuProcessOpState_Object = MibScalar
absacpuProcessOpState = _AbsacpuProcessOpState_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 15),
    _AbsacpuProcessOpState_Type()
)
absacpuProcessOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuProcessOpState.setStatus("current")


class _AbsacpuDNSUsage_Type(Integer32):
    """Custom type absacpuDNSUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failure", 2))
    )


_AbsacpuDNSUsage_Type.__name__ = "Integer32"
_AbsacpuDNSUsage_Object = MibScalar
absacpuDNSUsage = _AbsacpuDNSUsage_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 16),
    _AbsacpuDNSUsage_Type()
)
absacpuDNSUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuDNSUsage.setStatus("current")


class _AbsacpuDHCPUsage_Type(Integer32):
    """Custom type absacpuDHCPUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failure", 2))
    )


_AbsacpuDHCPUsage_Type.__name__ = "Integer32"
_AbsacpuDHCPUsage_Object = MibScalar
absacpuDHCPUsage = _AbsacpuDHCPUsage_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 17),
    _AbsacpuDHCPUsage_Type()
)
absacpuDHCPUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuDHCPUsage.setStatus("current")
_AbsacpuFtpUserId_Type = DisplayString
_AbsacpuFtpUserId_Object = MibScalar
absacpuFtpUserId = _AbsacpuFtpUserId_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 18),
    _AbsacpuFtpUserId_Type()
)
absacpuFtpUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuFtpUserId.setStatus("current")


class _AbsacpuCPUUsageId_Type(Integer32):
    """Custom type absacpuCPUUsageId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("user", 1),
          ("system", 2))
    )


_AbsacpuCPUUsageId_Type.__name__ = "Integer32"
_AbsacpuCPUUsageId_Object = MibScalar
absacpuCPUUsageId = _AbsacpuCPUUsageId_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 19),
    _AbsacpuCPUUsageId_Type()
)
absacpuCPUUsageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuCPUUsageId.setStatus("current")


class _AbsacpuDiskUsageId_Type(Integer32):
    """Custom type absacpuDiskUsageId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("paging", 1),
          ("flashDisk", 2),
          ("hardDisk", 3))
    )


_AbsacpuDiskUsageId_Type.__name__ = "Integer32"
_AbsacpuDiskUsageId_Object = MibScalar
absacpuDiskUsageId = _AbsacpuDiskUsageId_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 20),
    _AbsacpuDiskUsageId_Type()
)
absacpuDiskUsageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuDiskUsageId.setStatus("current")


class _AbsacpuToughDiskTemperature_Type(Integer32):
    """Custom type absacpuToughDiskTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AbsacpuToughDiskTemperature_Type.__name__ = "Integer32"
_AbsacpuToughDiskTemperature_Object = MibScalar
absacpuToughDiskTemperature = _AbsacpuToughDiskTemperature_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 21),
    _AbsacpuToughDiskTemperature_Type()
)
absacpuToughDiskTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuToughDiskTemperature.setStatus("current")
_AcpuSnortAttackType_Type = DisplayString
_AcpuSnortAttackType_Object = MibScalar
acpuSnortAttackType = _AcpuSnortAttackType_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 22),
    _AcpuSnortAttackType_Type()
)
acpuSnortAttackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuSnortAttackType.setStatus("current")
_AbsacpuToughDiskNo_Type = Integer32
_AbsacpuToughDiskNo_Object = MibScalar
absacpuToughDiskNo = _AbsacpuToughDiskNo_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 23),
    _AbsacpuToughDiskNo_Type()
)
absacpuToughDiskNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuToughDiskNo.setStatus("current")


class _AbsAircardFaultType_Type(Integer32):
    """Custom type absAircardFaultType based on Integer32"""
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
        *(("bitFailure", 1),
          ("pa0HighTemp", 2),
          ("pa0lowTemp", 3),
          ("pa0powerFailure", 4),
          ("pa1HighTemp", 5),
          ("pa1lowTemp", 6),
          ("pa1powerFailure", 7))
    )


_AbsAircardFaultType_Type.__name__ = "Integer32"
_AbsAircardFaultType_Object = MibScalar
absAircardFaultType = _AbsAircardFaultType_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 24),
    _AbsAircardFaultType_Type()
)
absAircardFaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAircardFaultType.setStatus("current")


class _AbsAircardState_Type(Integer32):
    """Custom type absAircardState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("readyForOperation", 2),
          ("callEstablished", 3))
    )


_AbsAircardState_Type.__name__ = "Integer32"
_AbsAircardState_Object = MibScalar
absAircardState = _AbsAircardState_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 25),
    _AbsAircardState_Type()
)
absAircardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAircardState.setStatus("obsolete")
_AbsHandSetAlertMessage_Type = DisplayString
_AbsHandSetAlertMessage_Object = MibScalar
absHandSetAlertMessage = _AbsHandSetAlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 26),
    _AbsHandSetAlertMessage_Type()
)
absHandSetAlertMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absHandSetAlertMessage.setStatus("current")


class _AbsResetReason_Type(Integer32):
    """Custom type absResetReason based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("powerOnReset", 1),
          ("normal", 2),
          ("lruHardwareFailure", 3),
          ("acpuSoftwareFailure", 4),
          ("conditionalReset", 5),
          ("acpuSoftwareActivation", 6),
          ("watchdogReset", 7),
          ("externalReset", 8),
          ("selfReset", 9))
    )


_AbsResetReason_Type.__name__ = "Integer32"
_AbsResetReason_Object = MibScalar
absResetReason = _AbsResetReason_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 27),
    _AbsResetReason_Type()
)
absResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absResetReason.setStatus("current")
_AbsCwapSSID_Type = DisplayString
_AbsCwapSSID_Object = MibScalar
absCwapSSID = _AbsCwapSSID_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 28),
    _AbsCwapSSID_Type()
)
absCwapSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCwapSSID.setStatus("current")


class _AbsCwapSSIDStatus_Type(Integer32):
    """Custom type absCwapSSIDStatus based on Integer32"""
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


_AbsCwapSSIDStatus_Type.__name__ = "Integer32"
_AbsCwapSSIDStatus_Object = MibScalar
absCwapSSIDStatus = _AbsCwapSSIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 29),
    _AbsCwapSSIDStatus_Type()
)
absCwapSSIDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCwapSSIDStatus.setStatus("current")
_AbsCwapSSIDStateChangeOriginator_Type = DisplayString
_AbsCwapSSIDStateChangeOriginator_Object = MibScalar
absCwapSSIDStateChangeOriginator = _AbsCwapSSIDStateChangeOriginator_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 30),
    _AbsCwapSSIDStateChangeOriginator_Type()
)
absCwapSSIDStateChangeOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCwapSSIDStateChangeOriginator.setStatus("current")
_AbsBundleName_Type = DisplayString
_AbsBundleName_Object = MibScalar
absBundleName = _AbsBundleName_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 31),
    _AbsBundleName_Type()
)
absBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absBundleName.setStatus("current")


class _AbsShutdownReason_Type(Integer32):
    """Custom type absShutdownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acpuTemperatureCritical", 1),
          ("normal", 2))
    )


_AbsShutdownReason_Type.__name__ = "Integer32"
_AbsShutdownReason_Object = MibScalar
absShutdownReason = _AbsShutdownReason_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 39),
    _AbsShutdownReason_Type()
)
absShutdownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absShutdownReason.setStatus("current")
_AbsacpuNoofThreads_Type = Integer32
_AbsacpuNoofThreads_Object = MibScalar
absacpuNoofThreads = _AbsacpuNoofThreads_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 40),
    _AbsacpuNoofThreads_Type()
)
absacpuNoofThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuNoofThreads.setStatus("current")


class _AbsSoftwareType_Type(Integer32):
    """Custom type absSoftwareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sw", 1),
          ("video", 2),
          ("content", 3))
    )


_AbsSoftwareType_Type.__name__ = "Integer32"
_AbsSoftwareType_Object = MibScalar
absSoftwareType = _AbsSoftwareType_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 41),
    _AbsSoftwareType_Type()
)
absSoftwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absSoftwareType.setStatus("current")


class _AbsDownloadState_Type(Integer32):
    """Custom type absDownloadState based on Integer32"""
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
        *(("failed", 1),
          ("start", 2),
          ("progressing", 3),
          ("complete", 4))
    )


_AbsDownloadState_Type.__name__ = "Integer32"
_AbsDownloadState_Object = MibScalar
absDownloadState = _AbsDownloadState_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 42),
    _AbsDownloadState_Type()
)
absDownloadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absDownloadState.setStatus("current")


class _AbsActivationState_Type(Integer32):
    """Custom type absActivationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("start", 2),
          ("complete", 3))
    )


_AbsActivationState_Type.__name__ = "Integer32"
_AbsActivationState_Object = MibScalar
absActivationState = _AbsActivationState_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 43),
    _AbsActivationState_Type()
)
absActivationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absActivationState.setStatus("current")


class _AbsCompatibilityType_Type(Integer32):
    """Custom type absCompatibilityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("software", 1),
          ("hardware", 2))
    )


_AbsCompatibilityType_Type.__name__ = "Integer32"
_AbsCompatibilityType_Object = MibScalar
absCompatibilityType = _AbsCompatibilityType_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 44),
    _AbsCompatibilityType_Type()
)
absCompatibilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCompatibilityType.setStatus("current")
_AbsFileNameOrBundleName_Type = DisplayString
_AbsFileNameOrBundleName_Object = MibScalar
absFileNameOrBundleName = _AbsFileNameOrBundleName_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 45),
    _AbsFileNameOrBundleName_Type()
)
absFileNameOrBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absFileNameOrBundleName.setStatus("current")
_AbsErrorString_Type = DisplayString
_AbsErrorString_Object = MibScalar
absErrorString = _AbsErrorString_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 46),
    _AbsErrorString_Type()
)
absErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absErrorString.setStatus("current")
_AbsDataServerAddress_Type = DisplayString
_AbsDataServerAddress_Object = MibScalar
absDataServerAddress = _AbsDataServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 47),
    _AbsDataServerAddress_Type()
)
absDataServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absDataServerAddress.setStatus("current")
_AbsacpuProcessName_Type = DisplayString
_AbsacpuProcessName_Object = MibScalar
absacpuProcessName = _AbsacpuProcessName_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 48),
    _AbsacpuProcessName_Type()
)
absacpuProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absacpuProcessName.setStatus("current")
_AbsResetReasonDescription_Type = DisplayString
_AbsResetReasonDescription_Object = MibScalar
absResetReasonDescription = _AbsResetReasonDescription_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 49),
    _AbsResetReasonDescription_Type()
)
absResetReasonDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absResetReasonDescription.setStatus("current")


class _AcpuHDDPartitionStatus_Type(Integer32):
    """Custom type acpuHDDPartitionStatus based on Integer32"""
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
        *(("bothPartitionsFailed", 0),
          ("secondaryPartitionFailed", 1),
          ("bothPartitionsHealthy", 2),
          ("primaryPartitionHealthy", 3),
          ("sda1Healthy", 4),
          ("invalidHardDiskPartition", 5),
          ("unknown", 6))
    )


_AcpuHDDPartitionStatus_Type.__name__ = "Integer32"
_AcpuHDDPartitionStatus_Object = MibScalar
acpuHDDPartitionStatus = _AcpuHDDPartitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 50),
    _AcpuHDDPartitionStatus_Type()
)
acpuHDDPartitionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuHDDPartitionStatus.setStatus("current")
_AbsLruMacAddress_Type = DisplayString
_AbsLruMacAddress_Object = MibScalar
absLruMacAddress = _AbsLruMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 51),
    _AbsLruMacAddress_Type()
)
absLruMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absLruMacAddress.setStatus("current")
_AbsDownloadPercComp_Type = DisplayString
_AbsDownloadPercComp_Object = MibScalar
absDownloadPercComp = _AbsDownloadPercComp_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 52),
    _AbsDownloadPercComp_Type()
)
absDownloadPercComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absDownloadPercComp.setStatus("current")
_AbsHighCPUProcess_Type = DisplayString
_AbsHighCPUProcess_Object = MibScalar
absHighCPUProcess = _AbsHighCPUProcess_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 53),
    _AbsHighCPUProcess_Type()
)
absHighCPUProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absHighCPUProcess.setStatus("current")
_AbsHighIOWaitProcess_Type = DisplayString
_AbsHighIOWaitProcess_Object = MibScalar
absHighIOWaitProcess = _AbsHighIOWaitProcess_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 54),
    _AbsHighIOWaitProcess_Type()
)
absHighIOWaitProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absHighIOWaitProcess.setStatus("current")


class _Abs429ErrorStatus_Type(Integer32):
    """Custom type abs429ErrorStatus based on Integer32"""
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
        *(("noFlightInfoData", 1),
          ("noTimingData", 2),
          ("noPositionData", 3),
          ("unknownCommunicationError", 4),
          ("multipleDataErrors", 5))
    )


_Abs429ErrorStatus_Type.__name__ = "Integer32"
_Abs429ErrorStatus_Object = MibScalar
abs429ErrorStatus = _Abs429ErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 56),
    _Abs429ErrorStatus_Type()
)
abs429ErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    abs429ErrorStatus.setStatus("current")


class _AbsHddStatus_Type(Integer32):
    """Custom type absHddStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("online", 1),
          ("failure", 2),
          ("recoveryStart", 3),
          ("permanentlyFailed", 4))
    )


_AbsHddStatus_Type.__name__ = "Integer32"
_AbsHddStatus_Object = MibScalar
absHddStatus = _AbsHddStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 57),
    _AbsHddStatus_Type()
)
absHddStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absHddStatus.setStatus("current")
_AbsHddNum_Type = Integer32
_AbsHddNum_Object = MibScalar
absHddNum = _AbsHddNum_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 58),
    _AbsHddNum_Type()
)
absHddNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absHddNum.setStatus("current")
_AbsHddPartition_Type = Integer32
_AbsHddPartition_Object = MibScalar
absHddPartition = _AbsHddPartition_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 59),
    _AbsHddPartition_Type()
)
absHddPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absHddPartition.setStatus("current")


class _AbsCSOverloadType_Type(Integer32):
    """Custom type absCSOverloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("pingRttThreshold", 1),
          ("rlVCQueueDrop", 2),
          ("csTxBytes", 3),
          ("cwapPingRttThreshold", 4),
          ("cwapChannelRateThreshold", 5))
    )


_AbsCSOverloadType_Type.__name__ = "Integer32"
_AbsCSOverloadType_Object = MibScalar
absCSOverloadType = _AbsCSOverloadType_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 60),
    _AbsCSOverloadType_Type()
)
absCSOverloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCSOverloadType.setStatus("current")


class _AbsCldUsbValidationReason_Type(Integer32):
    """Custom type absCldUsbValidationReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("validationFailure", 1),
          ("checksumFailure", 2),
          ("failToTransfer", 3),
          ("mfCorrupt", 4),
          ("mountFailure", 5))
    )


_AbsCldUsbValidationReason_Type.__name__ = "Integer32"
_AbsCldUsbValidationReason_Object = MibScalar
absCldUsbValidationReason = _AbsCldUsbValidationReason_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 61),
    _AbsCldUsbValidationReason_Type()
)
absCldUsbValidationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCldUsbValidationReason.setStatus("current")


class _AbsCldUsbSlotNumber_Type(Integer32):
    """Custom type absCldUsbSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AbsCldUsbSlotNumber_Type.__name__ = "Integer32"
_AbsCldUsbSlotNumber_Object = MibScalar
absCldUsbSlotNumber = _AbsCldUsbSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 62),
    _AbsCldUsbSlotNumber_Type()
)
absCldUsbSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCldUsbSlotNumber.setStatus("current")
_AbsCldUsbSerialNumber_Type = DisplayString
_AbsCldUsbSerialNumber_Object = MibScalar
absCldUsbSerialNumber = _AbsCldUsbSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 63),
    _AbsCldUsbSerialNumber_Type()
)
absCldUsbSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCldUsbSerialNumber.setStatus("current")


class _AbsCldUsbStatus_Type(Integer32):
    """Custom type absCldUsbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("unknown", 3))
    )


_AbsCldUsbStatus_Type.__name__ = "Integer32"
_AbsCldUsbStatus_Object = MibScalar
absCldUsbStatus = _AbsCldUsbStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1, 64),
    _AbsCldUsbStatus_Type()
)
absCldUsbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCldUsbStatus.setStatus("current")
_AcpuABSTrapGroups_ObjectIdentity = ObjectIdentity
acpuABSTrapGroups = _AcpuABSTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 2)
)
_AircellABSVersionBasedTraps_ObjectIdentity = ObjectIdentity
aircellABSVersionBasedTraps = _AircellABSVersionBasedTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7)
)
_AcpuMajorVersion_ObjectIdentity = ObjectIdentity
acpuMajorVersion = _AcpuMajorVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7)
)
_AcpuMinorVersion_ObjectIdentity = ObjectIdentity
acpuMinorVersion = _AcpuMinorVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1)
)
_AcpuPatchVersion_ObjectIdentity = ObjectIdentity
acpuPatchVersion = _AcpuPatchVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0)
)
_AbsTraps_ObjectIdentity = ObjectIdentity
absTraps = _AbsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2)
)

# Managed Objects groups

acpuABSObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 2, 1)
)
acpuABSObjectGroup.setObjects(
      *(("ABSTRAPMIB", "acpuSetTrap"),
        ("ABSTRAPMIB", "absHelloTrapType"),
        ("ABSTRAPMIB", "absDeviceId"),
        ("ABSTRAPMIB", "absLRUDeviceNoId"),
        ("ABSTRAPMIB", "absUnitOperState"),
        ("ABSTRAPMIB", "absacpuTemperature"),
        ("ABSTRAPMIB", "absacpuErrorReason"),
        ("ABSTRAPMIB", "absacpuMemoryUsage"),
        ("ABSTRAPMIB", "absacpuUserCPUUsage"),
        ("ABSTRAPMIB", "absacpuSystemCPUUsage"),
        ("ABSTRAPMIB", "absacpuPagingSpace"),
        ("ABSTRAPMIB", "absacpuFlashDiskSpace"),
        ("ABSTRAPMIB", "absacpuHardDiskSpace"),
        ("ABSTRAPMIB", "absacpuNoofProcesses"),
        ("ABSTRAPMIB", "absacpuProcessOpState"),
        ("ABSTRAPMIB", "absacpuDNSUsage"),
        ("ABSTRAPMIB", "absacpuDHCPUsage"),
        ("ABSTRAPMIB", "absacpuFtpUserId"),
        ("ABSTRAPMIB", "absacpuCPUUsageId"),
        ("ABSTRAPMIB", "absacpuDiskUsageId"),
        ("ABSTRAPMIB", "absacpuToughDiskTemperature"),
        ("ABSTRAPMIB", "acpuSnortAttackType"),
        ("ABSTRAPMIB", "absacpuToughDiskNo"),
        ("ABSTRAPMIB", "absAircardState"),
        ("ABSTRAPMIB", "absAircardFaultType"),
        ("ABSTRAPMIB", "absHandSetAlertMessage"),
        ("ABSTRAPMIB", "absResetReason"),
        ("ABSTRAPMIB", "absCwapSSID"),
        ("ABSTRAPMIB", "absCwapSSIDStatus"),
        ("ABSTRAPMIB", "absCwapSSIDStateChangeOriginator"),
        ("ABSTRAPMIB", "absBundleName"),
        ("ABSTRAPMIB", "absDataServerAddress"),
        ("ABSTRAPMIB", "absSoftwareType"),
        ("ABSTRAPMIB", "absDownloadState"),
        ("ABSTRAPMIB", "absActivationState"),
        ("ABSTRAPMIB", "absFileNameOrBundleName"),
        ("ABSTRAPMIB", "absErrorString"),
        ("ABSTRAPMIB", "absCompatibilityType"),
        ("ABSTRAPMIB", "absacpuProcessName"),
        ("ABSTRAPMIB", "absResetReasonDescription"),
        ("ABSTRAPMIB", "absHddStatus"),
        ("ABSTRAPMIB", "absHddNum"),
        ("ABSTRAPMIB", "absHddPartition"),
        ("ABSTRAPMIB", "absHighCPUProcess"),
        ("ABSTRAPMIB", "absHighIOWaitProcess"),
        ("ABSTRAPMIB", "absCSOverloadType"),
        ("ABSTRAPMIB", "absCldUsbValidationReason"),
        ("ABSTRAPMIB", "absCldUsbSlotNumber"),
        ("ABSTRAPMIB", "absCldUsbSerialNumber"),
        ("ABSTRAPMIB", "absCldUsbStatus"),
        ("ABSTRAPMIB", "absDownloadPercComp"),
        ("ABSTRAPMIB", "absLruMacAddress"),
        ("ABSTRAPMIB", "absShutdownReason"),
        ("ABSTRAPMIB", "absacpuNoofThreads"),
        ("ABSTRAPMIB", "acpuHDDPartitionStatus"),
        ("ABSTRAPMIB", "abs429ErrorStatus"))
)
if mibBuilder.loadTexts:
    acpuABSObjectGroup.setStatus("current")


# Notification objects

absSystemStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 1)
)
absSystemStateChange.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftType"),
        ("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("AIRCELL-ACPU-SNMP-MIB", "absOperationalStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absSystemStateChange.setStatus(
        "current"
    )

absTMHelloTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 2)
)
absTMHelloTrap.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absHelloTrapType"),
        ("AIRCELL-ACPU-SNMP-MIB", "absOperationalStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsLatitude"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsLongitude"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsAltitude"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuBatchVersion"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absTMHelloTrap.setStatus(
        "current"
    )

absATGHelloTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 3)
)
absATGHelloTrap.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absHelloTrapType"),
        ("AIRCELL-ACPU-SNMP-MIB", "absOperationalStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsLatitude"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsLongitude"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsAltitude"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardTxAGC"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardRx0AGC"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardRx1AGC"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardSignalStrength"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardPNOffset"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardPilotPNASP"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardSectorID"),
        ("AIRCELL-ACPU-SNMP-MIB", "absTotalClientCount"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAtgClientCount"),
        ("AIRCELL-ACPU-SNMP-MIB", "absTotalActiveClientCount"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuBatchVersion"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absATGHelloTrap.setStatus(
        "current"
    )

absPassurDataError = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 4)
)
absPassurDataError.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftType"),
        ("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("AIRCELL-ACPU-SNMP-MIB", "passurHealthStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absPassurDataError.setStatus(
        "current"
    )

absSystemReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 5)
)
absSystemReset.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absResetReason"),
        ("ABSTRAPMIB", "absResetReasonDescription"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absSystemReset.setStatus(
        "current"
    )

absLRUDeviceOperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 6)
)
absLRUDeviceOperStateChange.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absDeviceId"),
        ("ABSTRAPMIB", "absLRUDeviceNoId"),
        ("ABSTRAPMIB", "absUnitOperState"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absLRUDeviceOperStateChange.setStatus(
        "current"
    )

absLRUDeviceReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 7)
)
absLRUDeviceReset.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absDeviceId"),
        ("ABSTRAPMIB", "absLRUDeviceNoId"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"),
        ("ABSTRAPMIB", "absLruMacAddress"))
)
if mibBuilder.loadTexts:
    absLRUDeviceReset.setStatus(
        "current"
    )

absacpuEthernetPortStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 8)
)
absacpuEthernetPortStateChange.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absUnitOperState"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuEthernetPortState"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absacpuEthernetPortStateChange.setStatus(
        "obsolete"
    )

absacpuEthernetPortVlanStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 9)
)
absacpuEthernetPortVlanStateChange.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuEthernetPortVlanID"),
        ("ABSTRAPMIB", "absUnitOperState"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absacpuEthernetPortVlanStateChange.setStatus(
        "obsolete"
    )

absacpuegcPortStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 10)
)
absacpuegcPortStateChange.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absUnitOperState"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcPortIndex"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absacpuegcPortStateChange.setStatus(
        "obsolete"
    )

absacpuegcPortVlanStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 11)
)
absacpuegcPortVlanStateChange.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcPortIndex"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcPortVlanID"),
        ("ABSTRAPMIB", "absUnitOperState"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absacpuegcPortVlanStateChange.setStatus(
        "obsolete"
    )

absacpuTemperatureHighWater = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 12)
)
absacpuTemperatureHighWater.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absacpuTemperature"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absacpuTemperatureHighWater.setStatus(
        "current"
    )

acpuABSDataServerNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 13)
)
acpuABSDataServerNotAvailable.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absDataServerAddress"),
        ("ABSTRAPMIB", "absErrorString"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    acpuABSDataServerNotAvailable.setStatus(
        "current"
    )

acpuFtpAbort = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 14)
)
acpuFtpAbort.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absDataServerAddress"),
        ("ABSTRAPMIB", "absacpuFtpUserId"),
        ("ABSTRAPMIB", "absErrorString"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    acpuFtpAbort.setStatus(
        "current"
    )

absDownloadStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 15)
)
absDownloadStatus.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absSoftwareType"),
        ("ABSTRAPMIB", "absDownloadState"),
        ("ABSTRAPMIB", "absFileNameOrBundleName"),
        ("ABSTRAPMIB", "absDownloadPercComp"),
        ("ABSTRAPMIB", "absErrorString"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absDownloadStatus.setStatus(
        "current"
    )

absActivationStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 16)
)
absActivationStatus.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absSoftwareType"),
        ("ABSTRAPMIB", "absActivationState"),
        ("ABSTRAPMIB", "absFileNameOrBundleName"),
        ("ABSTRAPMIB", "absErrorString"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absActivationStatus.setStatus(
        "current"
    )

acpuABSDataSrvLogWriteErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 18)
)
acpuABSDataSrvLogWriteErr.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuPriABSDataSrvAddr"),
        ("ABSTRAPMIB", "absacpuErrorReason"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    acpuABSDataSrvLogWriteErr.setStatus(
        "obsolete"
    )

absacpuHighMemUsagePer = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 19)
)
absacpuHighMemUsagePer.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absacpuMemoryUsage"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absacpuHighMemUsagePer.setStatus(
        "current"
    )

absacpuHighCPUUsagePer = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 20)
)
absacpuHighCPUUsagePer.setObjects(
      *(("ABSTRAPMIB", "absacpuCPUUsageId"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absacpuUserCPUUsage"),
        ("ABSTRAPMIB", "absacpuSystemCPUUsage"),
        ("ABSTRAPMIB", "absHighCPUProcess"),
        ("ABSTRAPMIB", "absHighIOWaitProcess"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absacpuHighCPUUsagePer.setStatus(
        "current"
    )

absacpuHighDiskUsagePer = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 21)
)
absacpuHighDiskUsagePer.setObjects(
      *(("ABSTRAPMIB", "absacpuDiskUsageId"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absacpuPagingSpace"),
        ("ABSTRAPMIB", "absacpuFlashDiskSpace"),
        ("ABSTRAPMIB", "absacpuHardDiskSpace"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absacpuHighDiskUsagePer.setStatus(
        "current"
    )

absacpuABSProcessThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 22)
)
absacpuABSProcessThreshold.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absacpuNoofProcesses"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absacpuABSProcessThreshold.setStatus(
        "current"
    )

absacpuProcessOperStChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 23)
)
absacpuProcessOperStChg.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absacpuProcessOpState"),
        ("ABSTRAPMIB", "absacpuProcessName"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absacpuProcessOperStChg.setStatus(
        "current"
    )

absacpuDNSStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 24)
)
absacpuDNSStatus.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absacpuDNSUsage"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absacpuDNSStatus.setStatus(
        "current"
    )

absacpuDHCPStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 25)
)
absacpuDHCPStatus.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absacpuDHCPUsage"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absacpuDHCPStatus.setStatus(
        "current"
    )

absacpuCommLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 26)
)
absacpuCommLoss.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absDeviceId"),
        ("ABSTRAPMIB", "absLRUDeviceNoId"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absacpuCommLoss.setStatus(
        "current"
    )

acpuABSGPSDataError = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 27)
)
acpuABSGPSDataError.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absDeviceId"),
        ("ABSTRAPMIB", "absLRUDeviceNoId"),
        ("ABSTRAPMIB", "absacpuErrorReason"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    acpuABSGPSDataError.setStatus(
        "obsolete"
    )

absSystemModeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 28)
)
absSystemModeChange.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftType"),
        ("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("AIRCELL-ACPU-SNMP-MIB", "absSystemMode"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absSystemModeChange.setStatus(
        "current"
    )

absacpuTemperatureHighTDisk = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 29)
)
absacpuTemperatureHighTDisk.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absacpuToughDiskTemperature"),
        ("ABSTRAPMIB", "absacpuToughDiskNo"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absacpuTemperatureHighTDisk.setStatus(
        "current"
    )

acpuSnortAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 30)
)
acpuSnortAttackDetected.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "acpuSnortAttackType"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuSnortSrcIp"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuSnortDstIp"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuSnortSrcPort"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuSnortDstPort"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuSnortProtocol"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    acpuSnortAttackDetected.setStatus(
        "current"
    )

absAircardStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 31)
)
absAircardStateChange.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuAtgModemLinkStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absAircardStateChange.setStatus(
        "current"
    )

absAircardFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 32)
)
absAircardFault.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absAircardFaultType"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absAircardFault.setStatus(
        "current"
    )

absSoftwareBackout = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 33)
)
absSoftwareBackout.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absSoftwareBackout.setStatus(
        "obsolete"
    )

absSendStdLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 34)
)
absSendStdLog.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absSendStdLog.setStatus(
        "obsolete"
    )

absSendSM = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 35)
)
absSendSM.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absSendSM.setStatus(
        "obsolete"
    )

absSendHandsetMaintenanceAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 36)
)
absSendHandsetMaintenanceAlert.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absHandSetAlertMessage"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absSendHandsetMaintenanceAlert.setStatus(
        "current"
    )

aircardSendRawLogs = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 37)
)
aircardSendRawLogs.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    aircardSendRawLogs.setStatus(
        "obsolete"
    )

aircardRawLogFiltering = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 38)
)
aircardRawLogFiltering.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    aircardRawLogFiltering.setStatus(
        "obsolete"
    )

absEepromFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 39)
)
absEepromFailure.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absEepromFailure.setStatus(
        "current"
    )

absCwapSSIDStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 40)
)
absCwapSSIDStateChange.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftType"),
        ("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("ABSTRAPMIB", "absCwapSSID"),
        ("ABSTRAPMIB", "absCwapSSIDStatus"),
        ("ABSTRAPMIB", "absCwapSSIDStateChangeOriginator"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absCwapSSIDStateChange.setStatus(
        "current"
    )

absCompatibilityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 41)
)
absCompatibilityFailure.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absBundleName"),
        ("ABSTRAPMIB", "absCompatibilityType"),
        ("ABSTRAPMIB", "absErrorString"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absCompatibilityFailure.setStatus(
        "current"
    )

absVenturiStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 45)
)
absVenturiStatusChange.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuVenturiClientStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuVenturiTunnelStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuVenturiTunnelModeAdminStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absVenturiStatusChange.setStatus(
        "current"
    )

absLRUDeviceShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 46)
)
absLRUDeviceShutdown.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absDeviceId"),
        ("ABSTRAPMIB", "absLRUDeviceNoId"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absLRUDeviceShutdown.setStatus(
        "current"
    )

absSystemShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 47)
)
absSystemShutdown.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absShutdownReason"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absSystemShutdown.setStatus(
        "current"
    )

absacpuABSThreadThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 48)
)
absacpuABSThreadThreshold.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absacpuNoofThreads"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absacpuABSThreadThreshold.setStatus(
        "current"
    )

absacpuABSHDDPartitionFailureState = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 49)
)
absacpuABSHDDPartitionFailureState.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "acpuHDDPartitionStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absacpuABSHDDPartitionFailureState.setStatus(
        "current"
    )

absSystemInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 50)
)
absSystemInfo.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("AIRCELL-ACPU-SNMP-MIB", "wapCount"),
        ("AIRCELL-ACPU-SNMP-MIB", "cwapType"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuInfo"),
        ("AIRCELL-ACPU-SNMP-MIB", "absSoftwareVersion"),
        ("AIRCELL-ACPU-SNMP-MIB", "absWhitelistVersion"),
        ("AIRCELL-ACPU-SNMP-MIB", "abpVersion"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircardInfo"),
        ("AIRCELL-ACPU-SNMP-MIB", "auxcardInfo"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuBios"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircardEsn"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuHardwareSerialNumber"),
        ("AIRCELL-ACPU-SNMP-MIB", "aacuHardwareSerialNumber"),
        ("AIRCELL-ACPU-SNMP-MIB", "meruControllerInfo"),
        ("AIRCELL-ACPU-SNMP-MIB", "venturiInfo"),
        ("AIRCELL-ACPU-SNMP-MIB", "cwap1Info"),
        ("AIRCELL-ACPU-SNMP-MIB", "cwap2Info"),
        ("AIRCELL-ACPU-SNMP-MIB", "cwap3Info"),
        ("AIRCELL-ACPU-SNMP-MIB", "cwap4Info"),
        ("AIRCELL-ACPU-SNMP-MIB", "cwap5Info"),
        ("AIRCELL-ACPU-SNMP-MIB", "cwap6Info"),
        ("AIRCELL-ACPU-SNMP-MIB", "cwap7Info"),
        ("AIRCELL-ACPU-SNMP-MIB", "cwap8Info"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"),
        ("AIRCELL-ACPU-SNMP-MIB", "satelliteSupport"),
        ("AIRCELL-ACPU-SNMP-MIB", "weightonWheelsSupport"))
)
if mibBuilder.loadTexts:
    absSystemInfo.setStatus(
        "current"
    )

abs429DataError = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 51)
)
abs429DataError.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftType"),
        ("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("ABSTRAPMIB", "abs429ErrorStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    abs429DataError.setStatus(
        "current"
    )

absKUHelloTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 54)
)
absKUHelloTrap.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("ABSTRAPMIB", "absHelloTrapType"),
        ("AIRCELL-ACPU-SNMP-MIB", "absOperationalStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsLatitude"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsLongitude"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsAltitude"),
        ("AIRCELL-ACPU-SNMP-MIB", "absTotalClientCount"),
        ("AIRCELL-ACPU-SNMP-MIB", "absKUSignalStrength"),
        ("AIRCELL-ACPU-SNMP-MIB", "absTotalActiveClientCount"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuBatchVersion"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absKUHelloTrap.setStatus(
        "current"
    )

absCldOperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 55)
)
absCldOperStateChange.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftType"),
        ("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuCldOperStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuCldUsbAdminStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absCldOperStateChange.setStatus(
        "obsolete"
    )

absUsbOperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 56)
)
absUsbOperStateChange.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftType"),
        ("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("ABSTRAPMIB", "absCldUsbSerialNumber"),
        ("ABSTRAPMIB", "absCldUsbStatus"),
        ("ABSTRAPMIB", "absCldUsbSlotNumber"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuBatchVersion"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absUsbOperStateChange.setStatus(
        "current"
    )

absCldUsbStickError = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 57)
)
absCldUsbStickError.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftType"),
        ("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("ABSTRAPMIB", "absCldUsbValidationReason"),
        ("ABSTRAPMIB", "absCldUsbSlotNumber"),
        ("ABSTRAPMIB", "absCldUsbSerialNumber"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuBatchVersion"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absCldUsbStickError.setStatus(
        "current"
    )

absVideoServiceOperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 58)
)
absVideoServiceOperStateChange.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftType"),
        ("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("AIRCELL-ACPU-SNMP-MIB", "absVSMOperStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absVideoServiceOperStateChange.setStatus(
        "current"
    )

absHddStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 59)
)
absHddStatusTrap.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftType"),
        ("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("ABSTRAPMIB", "absHddNum"),
        ("ABSTRAPMIB", "absHddPartition"),
        ("ABSTRAPMIB", "absHddStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absHddStatusTrap.setStatus(
        "current"
    )

absSystemOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 60)
)
absSystemOverloadTrap.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftType"),
        ("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("ABSTRAPMIB", "absCSOverloadType"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absSystemOverloadTrap.setStatus(
        "current"
    )

absVSAvailabilityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 61)
)
absVSAvailabilityTrap.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftType"),
        ("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("AIRCELL-ACPU-SNMP-MIB", "absVideoServiceState"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absVSAvailabilityTrap.setStatus(
        "current"
    )

absSBBHelloTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 7, 1, 0, 2, 63)
)
absSBBHelloTrap.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("ABSTRAPMIB", "absHelloTrapType"),
        ("AIRCELL-ACPU-SNMP-MIB", "absOperationalStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsLatitude"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsLongitude"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsAltitude"),
        ("AIRCELL-ACPU-SNMP-MIB", "absActiveVideoDownloads"),
        ("AIRCELL-ACPU-SNMP-MIB", "absTotalClientCount"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuBatchVersion"),
        ("AIRCELL-ACPU-SNMP-MIB", "absSBBSignalStrength"),
        ("AIRCELL-ACPU-SNMP-MIB", "sbbPacketErrorRate"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"))
)
if mibBuilder.loadTexts:
    absSBBHelloTrap.setStatus(
        "current"
    )


# Notifications groups

acpuABSNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 2, 2)
)
acpuABSNotificationGroup.setObjects(
      *(("ABSTRAPMIB", "absSystemStateChange"),
        ("ABSTRAPMIB", "absTMHelloTrap"),
        ("ABSTRAPMIB", "absATGHelloTrap"),
        ("ABSTRAPMIB", "absPassurDataError"),
        ("ABSTRAPMIB", "absSystemReset"),
        ("ABSTRAPMIB", "absLRUDeviceOperStateChange"),
        ("ABSTRAPMIB", "absLRUDeviceReset"),
        ("ABSTRAPMIB", "absacpuEthernetPortStateChange"),
        ("ABSTRAPMIB", "absacpuEthernetPortVlanStateChange"),
        ("ABSTRAPMIB", "absacpuegcPortStateChange"),
        ("ABSTRAPMIB", "absacpuegcPortVlanStateChange"),
        ("ABSTRAPMIB", "absacpuTemperatureHighWater"),
        ("ABSTRAPMIB", "acpuABSDataServerNotAvailable"),
        ("ABSTRAPMIB", "acpuFtpAbort"),
        ("ABSTRAPMIB", "absActivationStatus"),
        ("ABSTRAPMIB", "absDownloadStatus"),
        ("ABSTRAPMIB", "absCompatibilityFailure"),
        ("ABSTRAPMIB", "acpuABSDataSrvLogWriteErr"),
        ("ABSTRAPMIB", "absacpuHighMemUsagePer"),
        ("ABSTRAPMIB", "absacpuHighCPUUsagePer"),
        ("ABSTRAPMIB", "absacpuHighDiskUsagePer"),
        ("ABSTRAPMIB", "absacpuABSProcessThreshold"),
        ("ABSTRAPMIB", "absacpuProcessOperStChg"),
        ("ABSTRAPMIB", "absacpuDNSStatus"),
        ("ABSTRAPMIB", "absacpuDHCPStatus"),
        ("ABSTRAPMIB", "absacpuCommLoss"),
        ("ABSTRAPMIB", "acpuABSGPSDataError"),
        ("ABSTRAPMIB", "absSystemModeChange"),
        ("ABSTRAPMIB", "absacpuTemperatureHighTDisk"),
        ("ABSTRAPMIB", "acpuSnortAttackDetected"),
        ("ABSTRAPMIB", "absAircardStateChange"),
        ("ABSTRAPMIB", "absAircardFault"),
        ("ABSTRAPMIB", "absSoftwareBackout"),
        ("ABSTRAPMIB", "absSendStdLog"),
        ("ABSTRAPMIB", "absSendSM"),
        ("ABSTRAPMIB", "aircardSendRawLogs"),
        ("ABSTRAPMIB", "aircardRawLogFiltering"),
        ("ABSTRAPMIB", "absEepromFailure"),
        ("ABSTRAPMIB", "absSendHandsetMaintenanceAlert"),
        ("ABSTRAPMIB", "absCwapSSIDStateChange"),
        ("ABSTRAPMIB", "absVenturiStatusChange"),
        ("ABSTRAPMIB", "absCldOperStateChange"),
        ("ABSTRAPMIB", "absUsbOperStateChange"),
        ("ABSTRAPMIB", "absCldUsbStickError"),
        ("ABSTRAPMIB", "absVideoServiceOperStateChange"),
        ("ABSTRAPMIB", "absHddStatusTrap"),
        ("ABSTRAPMIB", "absSystemOverloadTrap"),
        ("ABSTRAPMIB", "absVSAvailabilityTrap"),
        ("ABSTRAPMIB", "absacpuABSThreadThreshold"),
        ("ABSTRAPMIB", "absLRUDeviceShutdown"),
        ("ABSTRAPMIB", "absSystemShutdown"),
        ("ABSTRAPMIB", "absacpuABSHDDPartitionFailureState"),
        ("ABSTRAPMIB", "absSystemInfo"),
        ("ABSTRAPMIB", "absKUHelloTrap"),
        ("ABSTRAPMIB", "abs429DataError"),
        ("ABSTRAPMIB", "absSBBHelloTrap"))
)
if mibBuilder.loadTexts:
    acpuABSNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ABSTRAPMIB",
    **{"aircellLLC": aircellLLC,
       "aircellABS": aircellABS,
       "aircellABSTrap": aircellABSTrap,
       "absTrapControl": absTrapControl,
       "acpuSetTrap": acpuSetTrap,
       "absHelloTrapType": absHelloTrapType,
       "absDeviceId": absDeviceId,
       "absLRUDeviceNoId": absLRUDeviceNoId,
       "absUnitOperState": absUnitOperState,
       "absacpuTemperature": absacpuTemperature,
       "absacpuErrorReason": absacpuErrorReason,
       "absacpuMemoryUsage": absacpuMemoryUsage,
       "absacpuUserCPUUsage": absacpuUserCPUUsage,
       "absacpuSystemCPUUsage": absacpuSystemCPUUsage,
       "absacpuPagingSpace": absacpuPagingSpace,
       "absacpuFlashDiskSpace": absacpuFlashDiskSpace,
       "absacpuHardDiskSpace": absacpuHardDiskSpace,
       "absacpuNoofProcesses": absacpuNoofProcesses,
       "absacpuProcessOpState": absacpuProcessOpState,
       "absacpuDNSUsage": absacpuDNSUsage,
       "absacpuDHCPUsage": absacpuDHCPUsage,
       "absacpuFtpUserId": absacpuFtpUserId,
       "absacpuCPUUsageId": absacpuCPUUsageId,
       "absacpuDiskUsageId": absacpuDiskUsageId,
       "absacpuToughDiskTemperature": absacpuToughDiskTemperature,
       "acpuSnortAttackType": acpuSnortAttackType,
       "absacpuToughDiskNo": absacpuToughDiskNo,
       "absAircardFaultType": absAircardFaultType,
       "absAircardState": absAircardState,
       "absHandSetAlertMessage": absHandSetAlertMessage,
       "absResetReason": absResetReason,
       "absCwapSSID": absCwapSSID,
       "absCwapSSIDStatus": absCwapSSIDStatus,
       "absCwapSSIDStateChangeOriginator": absCwapSSIDStateChangeOriginator,
       "absBundleName": absBundleName,
       "absShutdownReason": absShutdownReason,
       "absacpuNoofThreads": absacpuNoofThreads,
       "absSoftwareType": absSoftwareType,
       "absDownloadState": absDownloadState,
       "absActivationState": absActivationState,
       "absCompatibilityType": absCompatibilityType,
       "absFileNameOrBundleName": absFileNameOrBundleName,
       "absErrorString": absErrorString,
       "absDataServerAddress": absDataServerAddress,
       "absacpuProcessName": absacpuProcessName,
       "absResetReasonDescription": absResetReasonDescription,
       "acpuHDDPartitionStatus": acpuHDDPartitionStatus,
       "absLruMacAddress": absLruMacAddress,
       "absDownloadPercComp": absDownloadPercComp,
       "absHighCPUProcess": absHighCPUProcess,
       "absHighIOWaitProcess": absHighIOWaitProcess,
       "abs429ErrorStatus": abs429ErrorStatus,
       "absHddStatus": absHddStatus,
       "absHddNum": absHddNum,
       "absHddPartition": absHddPartition,
       "absCSOverloadType": absCSOverloadType,
       "absCldUsbValidationReason": absCldUsbValidationReason,
       "absCldUsbSlotNumber": absCldUsbSlotNumber,
       "absCldUsbSerialNumber": absCldUsbSerialNumber,
       "absCldUsbStatus": absCldUsbStatus,
       "acpuABSTrapGroups": acpuABSTrapGroups,
       "acpuABSObjectGroup": acpuABSObjectGroup,
       "acpuABSNotificationGroup": acpuABSNotificationGroup,
       "aircellABSVersionBasedTraps": aircellABSVersionBasedTraps,
       "acpuMajorVersion": acpuMajorVersion,
       "acpuMinorVersion": acpuMinorVersion,
       "acpuPatchVersion": acpuPatchVersion,
       "absTraps": absTraps,
       "absSystemStateChange": absSystemStateChange,
       "absTMHelloTrap": absTMHelloTrap,
       "absATGHelloTrap": absATGHelloTrap,
       "absPassurDataError": absPassurDataError,
       "absSystemReset": absSystemReset,
       "absLRUDeviceOperStateChange": absLRUDeviceOperStateChange,
       "absLRUDeviceReset": absLRUDeviceReset,
       "absacpuEthernetPortStateChange": absacpuEthernetPortStateChange,
       "absacpuEthernetPortVlanStateChange": absacpuEthernetPortVlanStateChange,
       "absacpuegcPortStateChange": absacpuegcPortStateChange,
       "absacpuegcPortVlanStateChange": absacpuegcPortVlanStateChange,
       "absacpuTemperatureHighWater": absacpuTemperatureHighWater,
       "acpuABSDataServerNotAvailable": acpuABSDataServerNotAvailable,
       "acpuFtpAbort": acpuFtpAbort,
       "absDownloadStatus": absDownloadStatus,
       "absActivationStatus": absActivationStatus,
       "acpuABSDataSrvLogWriteErr": acpuABSDataSrvLogWriteErr,
       "absacpuHighMemUsagePer": absacpuHighMemUsagePer,
       "absacpuHighCPUUsagePer": absacpuHighCPUUsagePer,
       "absacpuHighDiskUsagePer": absacpuHighDiskUsagePer,
       "absacpuABSProcessThreshold": absacpuABSProcessThreshold,
       "absacpuProcessOperStChg": absacpuProcessOperStChg,
       "absacpuDNSStatus": absacpuDNSStatus,
       "absacpuDHCPStatus": absacpuDHCPStatus,
       "absacpuCommLoss": absacpuCommLoss,
       "acpuABSGPSDataError": acpuABSGPSDataError,
       "absSystemModeChange": absSystemModeChange,
       "absacpuTemperatureHighTDisk": absacpuTemperatureHighTDisk,
       "acpuSnortAttackDetected": acpuSnortAttackDetected,
       "absAircardStateChange": absAircardStateChange,
       "absAircardFault": absAircardFault,
       "absSoftwareBackout": absSoftwareBackout,
       "absSendStdLog": absSendStdLog,
       "absSendSM": absSendSM,
       "absSendHandsetMaintenanceAlert": absSendHandsetMaintenanceAlert,
       "aircardSendRawLogs": aircardSendRawLogs,
       "aircardRawLogFiltering": aircardRawLogFiltering,
       "absEepromFailure": absEepromFailure,
       "absCwapSSIDStateChange": absCwapSSIDStateChange,
       "absCompatibilityFailure": absCompatibilityFailure,
       "absVenturiStatusChange": absVenturiStatusChange,
       "absLRUDeviceShutdown": absLRUDeviceShutdown,
       "absSystemShutdown": absSystemShutdown,
       "absacpuABSThreadThreshold": absacpuABSThreadThreshold,
       "absacpuABSHDDPartitionFailureState": absacpuABSHDDPartitionFailureState,
       "absSystemInfo": absSystemInfo,
       "abs429DataError": abs429DataError,
       "absKUHelloTrap": absKUHelloTrap,
       "absCldOperStateChange": absCldOperStateChange,
       "absUsbOperStateChange": absUsbOperStateChange,
       "absCldUsbStickError": absCldUsbStickError,
       "absVideoServiceOperStateChange": absVideoServiceOperStateChange,
       "absHddStatusTrap": absHddStatusTrap,
       "absSystemOverloadTrap": absSystemOverloadTrap,
       "absVSAvailabilityTrap": absVSAvailabilityTrap,
       "absSBBHelloTrap": absSBBHelloTrap}
)
