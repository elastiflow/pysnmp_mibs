# SNMP MIB module (MLINK-PDH-MUXIP-2E1-2FE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/microlink_28568/MLINK-PDH-MUXIP-2E1-2FE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:32:07 2025
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Microlink_ObjectIdentity = ObjectIdentity
microlink = _Microlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568)
)
_Pdh_ObjectIdentity = ObjectIdentity
pdh = _Pdh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2)
)
_MLink_FM_GE_ObjectIdentity = ObjectIdentity
mLink_FM_GE = _MLink_FM_GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21)
)
_MLink_MUXIP_2E1_ObjectIdentity = ObjectIdentity
mLink_MUXIP_2E1 = _MLink_MUXIP_2E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3)
)
_SysInfo_ObjectIdentity = ObjectIdentity
sysInfo = _SysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 1)
)
_SysType_Type = DisplayString
_SysType_Object = MibScalar
sysType = _SysType_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 1, 1),
    _SysType_Type()
)
sysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysType.setStatus("mandatory")
_SysHw_Version_Type = DisplayString
_SysHw_Version_Object = MibScalar
sysHw_Version = _SysHw_Version_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 1, 2),
    _SysHw_Version_Type()
)
sysHw_Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHw_Version.setStatus("mandatory")
_SysSw_Version_Type = DisplayString
_SysSw_Version_Object = MibScalar
sysSw_Version = _SysSw_Version_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 1, 3),
    _SysSw_Version_Type()
)
sysSw_Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSw_Version.setStatus("mandatory")
_SysSerial_Num_Type = DisplayString
_SysSerial_Num_Object = MibScalar
sysSerial_Num = _SysSerial_Num_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 1, 4),
    _SysSerial_Num_Type()
)
sysSerial_Num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSerial_Num.setStatus("mandatory")


class _SysFactoryCode_Type(OctetString):
    """Custom type sysFactoryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SysFactoryCode_Type.__name__ = "OctetString"
_SysFactoryCode_Object = MibScalar
sysFactoryCode = _SysFactoryCode_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 1, 5),
    _SysFactoryCode_Type()
)
sysFactoryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFactoryCode.setStatus("mandatory")
_SysConfig_ObjectIdentity = ObjectIdentity
sysConfig = _SysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2)
)
_HostIPConfig_ObjectIdentity = ObjectIdentity
hostIPConfig = _HostIPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 1)
)
_HostIpAddress_Type = IpAddress
_HostIpAddress_Object = MibScalar
hostIpAddress = _HostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 1, 1),
    _HostIpAddress_Type()
)
hostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIpAddress.setStatus("mandatory")
_HostPhysAddress_Type = PhysAddress
_HostPhysAddress_Object = MibScalar
hostPhysAddress = _HostPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 1, 2),
    _HostPhysAddress_Type()
)
hostPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostPhysAddress.setStatus("mandatory")
_HostSubnetMask_Type = IpAddress
_HostSubnetMask_Object = MibScalar
hostSubnetMask = _HostSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 1, 3),
    _HostSubnetMask_Type()
)
hostSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSubnetMask.setStatus("mandatory")
_HostGwIpAddress_Type = IpAddress
_HostGwIpAddress_Object = MibScalar
hostGwIpAddress = _HostGwIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 1, 4),
    _HostGwIpAddress_Type()
)
hostGwIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostGwIpAddress.setStatus("mandatory")


class _HostVLAN_ID_Type(Integer32):
    """Custom type hostVLAN_ID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HostVLAN_ID_Type.__name__ = "Integer32"
_HostVLAN_ID_Object = MibScalar
hostVLAN_ID = _HostVLAN_ID_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 1, 5),
    _HostVLAN_ID_Type()
)
hostVLAN_ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostVLAN_ID.setStatus("mandatory")
_CommonConfig_ObjectIdentity = ObjectIdentity
commonConfig = _CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 2)
)
_GlobalSettings_Type = Integer32
_GlobalSettings_Object = MibScalar
globalSettings = _GlobalSettings_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 2, 1),
    _GlobalSettings_Type()
)
globalSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalSettings.setStatus("mandatory")


class _Net_ID_Type(Integer32):
    """Custom type net_ID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Net_ID_Type.__name__ = "Integer32"
_Net_ID_Object = MibScalar
net_ID = _Net_ID_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 2, 2),
    _Net_ID_Type()
)
net_ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    net_ID.setStatus("mandatory")


class _ConsoleTimeout_Type(Integer32):
    """Custom type consoleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConsoleTimeout_Type.__name__ = "Integer32"
_ConsoleTimeout_Object = MibScalar
consoleTimeout = _ConsoleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 2, 3),
    _ConsoleTimeout_Type()
)
consoleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleTimeout.setStatus("mandatory")


class _TDMoIP_global_settings_Type(Integer32):
    """Custom type tDMoIP_global_settings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TDMoIP_global_settings_Type.__name__ = "Integer32"
_TDMoIP_global_settings_Object = MibScalar
tDMoIP_global_settings = _TDMoIP_global_settings_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 2, 4),
    _TDMoIP_global_settings_Type()
)
tDMoIP_global_settings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tDMoIP_global_settings.setStatus("mandatory")


class _DstBundleID_UDPPortHead_Type(Integer32):
    """Custom type dstBundleID_UDPPortHead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DstBundleID_UDPPortHead_Type.__name__ = "Integer32"
_DstBundleID_UDPPortHead_Object = MibScalar
dstBundleID_UDPPortHead = _DstBundleID_UDPPortHead_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 2, 5),
    _DstBundleID_UDPPortHead_Type()
)
dstBundleID_UDPPortHead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dstBundleID_UDPPortHead.setStatus("mandatory")
_E1Config_ObjectIdentity = ObjectIdentity
e1Config = _E1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 3)
)
_E1CfgTable_Object = MibTable
e1CfgTable = _E1CfgTable_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    e1CfgTable.setStatus("mandatory")
_E1CfgEntry_Object = MibTableRow
e1CfgEntry = _E1CfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 3, 1, 1)
)
e1CfgEntry.setIndexNames(
    (0, "MLINK-PDH-MUXIP-2E1-2FE-MIB", "e1CfgIndex"),
)
if mibBuilder.loadTexts:
    e1CfgEntry.setStatus("mandatory")
_E1CfgIndex_Type = Integer32
_E1CfgIndex_Object = MibTableColumn
e1CfgIndex = _E1CfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 3, 1, 1, 1),
    _E1CfgIndex_Type()
)
e1CfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1CfgIndex.setStatus("mandatory")


class _E1CfgConfig_Type(Integer32):
    """Custom type e1CfgConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_E1CfgConfig_Type.__name__ = "Integer32"
_E1CfgConfig_Object = MibTableColumn
e1CfgConfig = _E1CfgConfig_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 3, 1, 1, 2),
    _E1CfgConfig_Type()
)
e1CfgConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgConfig.setStatus("mandatory")


class _E1CfgSyncSequence_Type(OctetString):
    """Custom type e1CfgSyncSequence based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_E1CfgSyncSequence_Type.__name__ = "OctetString"
_E1CfgSyncSequence_Object = MibTableColumn
e1CfgSyncSequence = _E1CfgSyncSequence_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 3, 1, 1, 3),
    _E1CfgSyncSequence_Type()
)
e1CfgSyncSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgSyncSequence.setStatus("mandatory")
_EthConfig_ObjectIdentity = ObjectIdentity
ethConfig = _EthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 4)
)
_CopperEthCfgTable_Object = MibTable
copperEthCfgTable = _CopperEthCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    copperEthCfgTable.setStatus("mandatory")
_CopperEthCfgEntry_Object = MibTableRow
copperEthCfgEntry = _CopperEthCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 4, 1, 1)
)
copperEthCfgEntry.setIndexNames(
    (0, "MLINK-PDH-MUXIP-2E1-2FE-MIB", "copperEthCfgIndex"),
)
if mibBuilder.loadTexts:
    copperEthCfgEntry.setStatus("mandatory")
_CopperEthCfgIndex_Type = Integer32
_CopperEthCfgIndex_Object = MibTableColumn
copperEthCfgIndex = _CopperEthCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 4, 1, 1, 1),
    _CopperEthCfgIndex_Type()
)
copperEthCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copperEthCfgIndex.setStatus("mandatory")


class _CopperEthCfgConfig_Type(Integer32):
    """Custom type copperEthCfgConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CopperEthCfgConfig_Type.__name__ = "Integer32"
_CopperEthCfgConfig_Object = MibTableColumn
copperEthCfgConfig = _CopperEthCfgConfig_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 4, 1, 1, 2),
    _CopperEthCfgConfig_Type()
)
copperEthCfgConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copperEthCfgConfig.setStatus("mandatory")
_BundleConfig_ObjectIdentity = ObjectIdentity
bundleConfig = _BundleConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 5)
)
_BundleCfgTable_Object = MibTable
bundleCfgTable = _BundleCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    bundleCfgTable.setStatus("mandatory")
_BundleCfgEntry_Object = MibTableRow
bundleCfgEntry = _BundleCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 5, 1, 1)
)
bundleCfgEntry.setIndexNames(
    (0, "MLINK-PDH-MUXIP-2E1-2FE-MIB", "bundleCfgIndex"),
)
if mibBuilder.loadTexts:
    bundleCfgEntry.setStatus("mandatory")
_BundleCfgIndex_Type = Integer32
_BundleCfgIndex_Object = MibTableColumn
bundleCfgIndex = _BundleCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 5, 1, 1, 1),
    _BundleCfgIndex_Type()
)
bundleCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleCfgIndex.setStatus("mandatory")
_BundleCfgFlags_Type = Integer32
_BundleCfgFlags_Object = MibTableColumn
bundleCfgFlags = _BundleCfgFlags_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 5, 1, 1, 2),
    _BundleCfgFlags_Type()
)
bundleCfgFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bundleCfgFlags.setStatus("mandatory")


class _BundleCfgBundleID_Type(Integer32):
    """Custom type bundleCfgBundleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BundleCfgBundleID_Type.__name__ = "Integer32"
_BundleCfgBundleID_Object = MibTableColumn
bundleCfgBundleID = _BundleCfgBundleID_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 5, 1, 1, 3),
    _BundleCfgBundleID_Type()
)
bundleCfgBundleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleCfgBundleID.setStatus("mandatory")
_BundleCfgDst_IP_Type = IpAddress
_BundleCfgDst_IP_Object = MibTableColumn
bundleCfgDst_IP = _BundleCfgDst_IP_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 5, 1, 1, 4),
    _BundleCfgDst_IP_Type()
)
bundleCfgDst_IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bundleCfgDst_IP.setStatus("mandatory")


class _BundleCfgDst_BundleID_Type(Integer32):
    """Custom type bundleCfgDst_BundleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BundleCfgDst_BundleID_Type.__name__ = "Integer32"
_BundleCfgDst_BundleID_Object = MibTableColumn
bundleCfgDst_BundleID = _BundleCfgDst_BundleID_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 5, 1, 1, 5),
    _BundleCfgDst_BundleID_Type()
)
bundleCfgDst_BundleID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bundleCfgDst_BundleID.setStatus("mandatory")


class _BundleCfgE1_PortNumber_Type(Integer32):
    """Custom type bundleCfgE1_PortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_BundleCfgE1_PortNumber_Type.__name__ = "Integer32"
_BundleCfgE1_PortNumber_Object = MibTableColumn
bundleCfgE1_PortNumber = _BundleCfgE1_PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 5, 1, 1, 6),
    _BundleCfgE1_PortNumber_Type()
)
bundleCfgE1_PortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bundleCfgE1_PortNumber.setStatus("mandatory")


class _BundleCfgTS_table_Type(Integer32):
    """Custom type bundleCfgTS_table based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_BundleCfgTS_table_Type.__name__ = "Integer32"
_BundleCfgTS_table_Object = MibTableColumn
bundleCfgTS_table = _BundleCfgTS_table_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 5, 1, 1, 7),
    _BundleCfgTS_table_Type()
)
bundleCfgTS_table.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bundleCfgTS_table.setStatus("mandatory")


class _BundleCfgFrameCellNumber_Type(Integer32):
    """Custom type bundleCfgFrameCellNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BundleCfgFrameCellNumber_Type.__name__ = "Integer32"
_BundleCfgFrameCellNumber_Object = MibTableColumn
bundleCfgFrameCellNumber = _BundleCfgFrameCellNumber_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 5, 1, 1, 8),
    _BundleCfgFrameCellNumber_Type()
)
bundleCfgFrameCellNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bundleCfgFrameCellNumber.setStatus("mandatory")


class _BundleCfgPDVT_Type(Integer32):
    """Custom type bundleCfgPDVT based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 250),
    )


_BundleCfgPDVT_Type.__name__ = "Integer32"
_BundleCfgPDVT_Object = MibTableColumn
bundleCfgPDVT = _BundleCfgPDVT_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 5, 1, 1, 9),
    _BundleCfgPDVT_Type()
)
bundleCfgPDVT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bundleCfgPDVT.setStatus("mandatory")


class _BundleCfgIP_TOS_Type(Integer32):
    """Custom type bundleCfgIP_TOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BundleCfgIP_TOS_Type.__name__ = "Integer32"
_BundleCfgIP_TOS_Object = MibTableColumn
bundleCfgIP_TOS = _BundleCfgIP_TOS_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 5, 1, 1, 10),
    _BundleCfgIP_TOS_Type()
)
bundleCfgIP_TOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bundleCfgIP_TOS.setStatus("mandatory")


class _BundleCfgTag_Pri_Type(Integer32):
    """Custom type bundleCfgTag_Pri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BundleCfgTag_Pri_Type.__name__ = "Integer32"
_BundleCfgTag_Pri_Object = MibTableColumn
bundleCfgTag_Pri = _BundleCfgTag_Pri_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 5, 1, 1, 11),
    _BundleCfgTag_Pri_Type()
)
bundleCfgTag_Pri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bundleCfgTag_Pri.setStatus("mandatory")
_E1AdaptClkCfgTable_Object = MibTable
e1AdaptClkCfgTable = _E1AdaptClkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 5, 2)
)
if mibBuilder.loadTexts:
    e1AdaptClkCfgTable.setStatus("mandatory")
_E1AdaptClkCfgEntry_Object = MibTableRow
e1AdaptClkCfgEntry = _E1AdaptClkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 5, 2, 1)
)
e1AdaptClkCfgEntry.setIndexNames(
    (0, "MLINK-PDH-MUXIP-2E1-2FE-MIB", "e1AdaptClkCfgIndex"),
)
if mibBuilder.loadTexts:
    e1AdaptClkCfgEntry.setStatus("mandatory")
_E1AdaptClkCfgIndex_Type = Integer32
_E1AdaptClkCfgIndex_Object = MibTableColumn
e1AdaptClkCfgIndex = _E1AdaptClkCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 5, 2, 1, 1),
    _E1AdaptClkCfgIndex_Type()
)
e1AdaptClkCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1AdaptClkCfgIndex.setStatus("mandatory")


class _E1AdaptClkCfgConfig_Type(Integer32):
    """Custom type e1AdaptClkCfgConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_E1AdaptClkCfgConfig_Type.__name__ = "Integer32"
_E1AdaptClkCfgConfig_Object = MibTableColumn
e1AdaptClkCfgConfig = _E1AdaptClkCfgConfig_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 5, 2, 1, 2),
    _E1AdaptClkCfgConfig_Type()
)
e1AdaptClkCfgConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1AdaptClkCfgConfig.setStatus("mandatory")
_SnmpConfig_ObjectIdentity = ObjectIdentity
snmpConfig = _SnmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 6)
)
_SnmpTrap_Dst1_IpAddress_Type = IpAddress
_SnmpTrap_Dst1_IpAddress_Object = MibScalar
snmpTrap_Dst1_IpAddress = _SnmpTrap_Dst1_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 6, 1),
    _SnmpTrap_Dst1_IpAddress_Type()
)
snmpTrap_Dst1_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap_Dst1_IpAddress.setStatus("mandatory")
_SnmpTrap_Dst2_IpAddress_Type = IpAddress
_SnmpTrap_Dst2_IpAddress_Object = MibScalar
snmpTrap_Dst2_IpAddress = _SnmpTrap_Dst2_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 6, 2),
    _SnmpTrap_Dst2_IpAddress_Type()
)
snmpTrap_Dst2_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap_Dst2_IpAddress.setStatus("mandatory")


class _SnmpTrap_Dest1Port_Type(Integer32):
    """Custom type snmpTrap_Dest1Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpTrap_Dest1Port_Type.__name__ = "Integer32"
_SnmpTrap_Dest1Port_Object = MibScalar
snmpTrap_Dest1Port = _SnmpTrap_Dest1Port_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 6, 3),
    _SnmpTrap_Dest1Port_Type()
)
snmpTrap_Dest1Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap_Dest1Port.setStatus("mandatory")


class _SnmpTrap_Dest2Port_Type(Integer32):
    """Custom type snmpTrap_Dest2Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpTrap_Dest2Port_Type.__name__ = "Integer32"
_SnmpTrap_Dest2Port_Object = MibScalar
snmpTrap_Dest2Port = _SnmpTrap_Dest2Port_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 6, 4),
    _SnmpTrap_Dest2Port_Type()
)
snmpTrap_Dest2Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap_Dest2Port.setStatus("mandatory")
_SnmpTrap_Time1_Type = Integer32
_SnmpTrap_Time1_Object = MibScalar
snmpTrap_Time1 = _SnmpTrap_Time1_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 6, 5),
    _SnmpTrap_Time1_Type()
)
snmpTrap_Time1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap_Time1.setStatus("mandatory")
_SnmpTrap_Time2_Type = Integer32
_SnmpTrap_Time2_Object = MibScalar
snmpTrap_Time2 = _SnmpTrap_Time2_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 6, 6),
    _SnmpTrap_Time2_Type()
)
snmpTrap_Time2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap_Time2.setStatus("mandatory")


class _SnmpCommunity_Type(DisplayString):
    """Custom type snmpCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnmpCommunity_Type.__name__ = "DisplayString"
_SnmpCommunity_Object = MibScalar
snmpCommunity = _SnmpCommunity_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 6, 7),
    _SnmpCommunity_Type()
)
snmpCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCommunity.setStatus("mandatory")
_VlanConfig_ObjectIdentity = ObjectIdentity
vlanConfig = _VlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 7)
)
_Cpu_default_VID_Type = Integer32
_Cpu_default_VID_Object = MibScalar
cpu_default_VID = _Cpu_default_VID_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 7, 1),
    _Cpu_default_VID_Type()
)
cpu_default_VID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpu_default_VID.setStatus("mandatory")
_Vlan_PortCfgTable_Object = MibTable
vlan_PortCfgTable = _Vlan_PortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 7, 2)
)
if mibBuilder.loadTexts:
    vlan_PortCfgTable.setStatus("mandatory")
_Vlan_PortCfgEntry_Object = MibTableRow
vlan_PortCfgEntry = _Vlan_PortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 7, 2, 1)
)
vlan_PortCfgEntry.setIndexNames(
    (0, "MLINK-PDH-MUXIP-2E1-2FE-MIB", "vlan_PortCfgIndex"),
)
if mibBuilder.loadTexts:
    vlan_PortCfgEntry.setStatus("mandatory")
_Vlan_PortCfgIndex_Type = Integer32
_Vlan_PortCfgIndex_Object = MibTableColumn
vlan_PortCfgIndex = _Vlan_PortCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 7, 2, 1, 1),
    _Vlan_PortCfgIndex_Type()
)
vlan_PortCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlan_PortCfgIndex.setStatus("mandatory")
_Vlan_PortCfgDefVID_Type = Integer32
_Vlan_PortCfgDefVID_Object = MibTableColumn
vlan_PortCfgDefVID = _Vlan_PortCfgDefVID_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 7, 2, 1, 2),
    _Vlan_PortCfgDefVID_Type()
)
vlan_PortCfgDefVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlan_PortCfgDefVID.setStatus("mandatory")
_Vlan_PortCfgConfig_Type = Integer32
_Vlan_PortCfgConfig_Object = MibTableColumn
vlan_PortCfgConfig = _Vlan_PortCfgConfig_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 7, 2, 1, 3),
    _Vlan_PortCfgConfig_Type()
)
vlan_PortCfgConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlan_PortCfgConfig.setStatus("mandatory")
_Vlan_Table_Object = MibTable
vlan_Table = _Vlan_Table_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 7, 3)
)
if mibBuilder.loadTexts:
    vlan_Table.setStatus("mandatory")
_Vlan_TableEntry_Object = MibTableRow
vlan_TableEntry = _Vlan_TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 7, 3, 1)
)
vlan_TableEntry.setIndexNames(
    (0, "MLINK-PDH-MUXIP-2E1-2FE-MIB", "vlan_TableIndex"),
)
if mibBuilder.loadTexts:
    vlan_TableEntry.setStatus("mandatory")
_Vlan_TableIndex_Type = Integer32
_Vlan_TableIndex_Object = MibTableColumn
vlan_TableIndex = _Vlan_TableIndex_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 7, 3, 1, 1),
    _Vlan_TableIndex_Type()
)
vlan_TableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlan_TableIndex.setStatus("mandatory")
_Vlan_TableVID_Type = Integer32
_Vlan_TableVID_Object = MibTableColumn
vlan_TableVID = _Vlan_TableVID_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 7, 3, 1, 2),
    _Vlan_TableVID_Type()
)
vlan_TableVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlan_TableVID.setStatus("mandatory")
_Vlan_TableMember_Type = Integer32
_Vlan_TableMember_Object = MibTableColumn
vlan_TableMember = _Vlan_TableMember_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 7, 3, 1, 3),
    _Vlan_TableMember_Type()
)
vlan_TableMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlan_TableMember.setStatus("mandatory")
_QosConfig_ObjectIdentity = ObjectIdentity
qosConfig = _QosConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 8)
)
_Cpu_QoS_cfg_Type = Integer32
_Cpu_QoS_cfg_Object = MibScalar
cpu_QoS_cfg = _Cpu_QoS_cfg_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 8, 1),
    _Cpu_QoS_cfg_Type()
)
cpu_QoS_cfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpu_QoS_cfg.setStatus("mandatory")
_Tag_Pri_mapping_Type = Integer32
_Tag_Pri_mapping_Object = MibScalar
tag_Pri_mapping = _Tag_Pri_mapping_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 8, 2),
    _Tag_Pri_mapping_Type()
)
tag_Pri_mapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tag_Pri_mapping.setStatus("mandatory")
_Dscp_Pri_mapping_Object = MibTable
dscp_Pri_mapping = _Dscp_Pri_mapping_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 8, 3)
)
if mibBuilder.loadTexts:
    dscp_Pri_mapping.setStatus("mandatory")
_Dscp_mapEntry_Object = MibTableRow
dscp_mapEntry = _Dscp_mapEntry_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 8, 3, 1)
)
dscp_mapEntry.setIndexNames(
    (0, "MLINK-PDH-MUXIP-2E1-2FE-MIB", "dscp_mapIndex"),
)
if mibBuilder.loadTexts:
    dscp_mapEntry.setStatus("mandatory")
_Dscp_mapIndex_Type = Integer32
_Dscp_mapIndex_Object = MibTableColumn
dscp_mapIndex = _Dscp_mapIndex_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 8, 3, 1, 1),
    _Dscp_mapIndex_Type()
)
dscp_mapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dscp_mapIndex.setStatus("mandatory")
_Dscp_mapValue_Type = Integer32
_Dscp_mapValue_Object = MibTableColumn
dscp_mapValue = _Dscp_mapValue_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 8, 3, 1, 2),
    _Dscp_mapValue_Type()
)
dscp_mapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dscp_mapValue.setStatus("mandatory")
_Qos_PortCfgTable_Object = MibTable
qos_PortCfgTable = _Qos_PortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 8, 4)
)
if mibBuilder.loadTexts:
    qos_PortCfgTable.setStatus("mandatory")
_Qos_PortCfgEntry_Object = MibTableRow
qos_PortCfgEntry = _Qos_PortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 8, 4, 1)
)
qos_PortCfgEntry.setIndexNames(
    (0, "MLINK-PDH-MUXIP-2E1-2FE-MIB", "qos_PortCfgIndex"),
)
if mibBuilder.loadTexts:
    qos_PortCfgEntry.setStatus("mandatory")
_Qos_PortCfgIndex_Type = Integer32
_Qos_PortCfgIndex_Object = MibTableColumn
qos_PortCfgIndex = _Qos_PortCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 8, 4, 1, 1),
    _Qos_PortCfgIndex_Type()
)
qos_PortCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qos_PortCfgIndex.setStatus("mandatory")
_Qos_PortCfgConfig_Type = Integer32
_Qos_PortCfgConfig_Object = MibTableColumn
qos_PortCfgConfig = _Qos_PortCfgConfig_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 2, 8, 4, 1, 2),
    _Qos_PortCfgConfig_Type()
)
qos_PortCfgConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qos_PortCfgConfig.setStatus("mandatory")
_SysState_ObjectIdentity = ObjectIdentity
sysState = _SysState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3)
)
_CommonState_ObjectIdentity = ObjectIdentity
commonState = _CommonState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 1)
)


class _LocalAlarm_Type(Integer32):
    """Custom type localAlarm based on Integer32"""
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
        *(("OK", 0),
          ("MAJOR", 1),
          ("MINOR", 2),
          ("MAJOR-MINOR", 3))
    )


_LocalAlarm_Type.__name__ = "Integer32"
_LocalAlarm_Object = MibScalar
localAlarm = _LocalAlarm_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 1, 1),
    _LocalAlarm_Type()
)
localAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localAlarm.setStatus("mandatory")


class _SysTime_Type(OctetString):
    """Custom type sysTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_SysTime_Type.__name__ = "OctetString"
_SysTime_Object = MibScalar
sysTime = _SysTime_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 1, 2),
    _SysTime_Type()
)
sysTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTime.setStatus("mandatory")
_E1State_ObjectIdentity = ObjectIdentity
e1State = _E1State_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2)
)
_E1StatusTable_Object = MibTable
e1StatusTable = _E1StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    e1StatusTable.setStatus("mandatory")
_E1StatusEntry_Object = MibTableRow
e1StatusEntry = _E1StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 1, 1)
)
e1StatusEntry.setIndexNames(
    (0, "MLINK-PDH-MUXIP-2E1-2FE-MIB", "e1StatusIndex"),
)
if mibBuilder.loadTexts:
    e1StatusEntry.setStatus("mandatory")
_E1StatusIndex_Type = Integer32
_E1StatusIndex_Object = MibTableColumn
e1StatusIndex = _E1StatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 1, 1, 1),
    _E1StatusIndex_Type()
)
e1StatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1StatusIndex.setStatus("mandatory")


class _E1StatusStatus_Type(Integer32):
    """Custom type e1StatusStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              6,
              8,
              10,
              15)
        )
    )
    namedValues = NamedValues(
        *(("OK", 0),
          ("LOF", 2),
          ("AIS", 4),
          ("LOFandAIS", 6),
          ("RAI", 8),
          ("LOFandRAI", 10),
          ("LOS", 15))
    )


_E1StatusStatus_Type.__name__ = "Integer32"
_E1StatusStatus_Object = MibTableColumn
e1StatusStatus = _E1StatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 1, 1, 2),
    _E1StatusStatus_Type()
)
e1StatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1StatusStatus.setStatus("mandatory")


class _E1StatusSyncSource_Type(Integer32):
    """Custom type e1StatusSyncSource based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("E1_Port1", 0),
          ("E1_Port2", 1),
          ("E1_Port3", 2),
          ("E1_Port4", 3),
          ("E1_Port5", 4),
          ("E1_Port6", 5),
          ("E1_Port7", 6),
          ("E1_Port8", 7),
          ("E1_Port9", 8),
          ("E1_Port10", 9),
          ("E1_Port11", 10),
          ("E1_Port12", 11),
          ("E1_Port13", 12),
          ("E1_Port14", 13),
          ("E1_Port15", 14),
          ("E1_Port16", 15),
          ("AdaptClk1", 32),
          ("AdaptClk2", 33),
          ("AdaptClk3", 34),
          ("AdaptClk4", 35),
          ("AdaptClk5", 36),
          ("AdaptClk6", 37),
          ("AdaptClk7", 38),
          ("AdaptClk8", 39),
          ("AdaptClk9", 40),
          ("AdaptClk10", 41),
          ("AdaptClk11", 42),
          ("AdaptClk12", 43),
          ("AdaptClk13", 44),
          ("AdaptClk14", 45),
          ("AdaptClk15", 46),
          ("AdaptClk16", 47),
          ("IntGen", 255))
    )


_E1StatusSyncSource_Type.__name__ = "Integer32"
_E1StatusSyncSource_Object = MibTableColumn
e1StatusSyncSource = _E1StatusSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 1, 1, 3),
    _E1StatusSyncSource_Type()
)
e1StatusSyncSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1StatusSyncSource.setStatus("mandatory")
_E1StatusCV_Errors_Type = Counter32
_E1StatusCV_Errors_Object = MibTableColumn
e1StatusCV_Errors = _E1StatusCV_Errors_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 1, 1, 4),
    _E1StatusCV_Errors_Type()
)
e1StatusCV_Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1StatusCV_Errors.setStatus("mandatory")
_E1StatusFAS_Errors_Type = Counter32
_E1StatusFAS_Errors_Object = MibTableColumn
e1StatusFAS_Errors = _E1StatusFAS_Errors_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 1, 1, 5),
    _E1StatusFAS_Errors_Type()
)
e1StatusFAS_Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1StatusFAS_Errors.setStatus("mandatory")
_E1StatusCRC4_Errors_Type = Counter32
_E1StatusCRC4_Errors_Object = MibTableColumn
e1StatusCRC4_Errors = _E1StatusCRC4_Errors_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 1, 1, 6),
    _E1StatusCRC4_Errors_Type()
)
e1StatusCRC4_Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1StatusCRC4_Errors.setStatus("mandatory")
_E1StatusEbit_Errors_Type = Counter32
_E1StatusEbit_Errors_Object = MibTableColumn
e1StatusEbit_Errors = _E1StatusEbit_Errors_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 1, 1, 7),
    _E1StatusEbit_Errors_Type()
)
e1StatusEbit_Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1StatusEbit_Errors.setStatus("mandatory")
_E1G826CurStatTable_Object = MibTable
e1G826CurStatTable = _E1G826CurStatTable_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    e1G826CurStatTable.setStatus("mandatory")
_E1G826CurStatEntry_Object = MibTableRow
e1G826CurStatEntry = _E1G826CurStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 2, 1)
)
e1G826CurStatEntry.setIndexNames(
    (0, "MLINK-PDH-MUXIP-2E1-2FE-MIB", "e1G826CurStatIndex"),
)
if mibBuilder.loadTexts:
    e1G826CurStatEntry.setStatus("mandatory")
_E1G826CurStatIndex_Type = Integer32
_E1G826CurStatIndex_Object = MibTableColumn
e1G826CurStatIndex = _E1G826CurStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 2, 1, 1),
    _E1G826CurStatIndex_Type()
)
e1G826CurStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826CurStatIndex.setStatus("mandatory")
_E1G826CurStatEB_CRC4_Type = Counter32
_E1G826CurStatEB_CRC4_Object = MibTableColumn
e1G826CurStatEB_CRC4 = _E1G826CurStatEB_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 2, 1, 2),
    _E1G826CurStatEB_CRC4_Type()
)
e1G826CurStatEB_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826CurStatEB_CRC4.setStatus("mandatory")
_E1G826CurStatES_CRC4_Type = Counter32
_E1G826CurStatES_CRC4_Object = MibTableColumn
e1G826CurStatES_CRC4 = _E1G826CurStatES_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 2, 1, 3),
    _E1G826CurStatES_CRC4_Type()
)
e1G826CurStatES_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826CurStatES_CRC4.setStatus("mandatory")
_E1G826CurStatSES_CRC4_Type = Counter32
_E1G826CurStatSES_CRC4_Object = MibTableColumn
e1G826CurStatSES_CRC4 = _E1G826CurStatSES_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 2, 1, 4),
    _E1G826CurStatSES_CRC4_Type()
)
e1G826CurStatSES_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826CurStatSES_CRC4.setStatus("mandatory")
_E1G826CurStatAvTime_CRC4_Type = Counter32
_E1G826CurStatAvTime_CRC4_Object = MibTableColumn
e1G826CurStatAvTime_CRC4 = _E1G826CurStatAvTime_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 2, 1, 5),
    _E1G826CurStatAvTime_CRC4_Type()
)
e1G826CurStatAvTime_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826CurStatAvTime_CRC4.setStatus("mandatory")
_E1G826CurStatUnAvTime_CRC4_Type = Counter32
_E1G826CurStatUnAvTime_CRC4_Object = MibTableColumn
e1G826CurStatUnAvTime_CRC4 = _E1G826CurStatUnAvTime_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 2, 1, 6),
    _E1G826CurStatUnAvTime_CRC4_Type()
)
e1G826CurStatUnAvTime_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826CurStatUnAvTime_CRC4.setStatus("mandatory")
_E1G826CurStatEB_Ebit_Type = Counter32
_E1G826CurStatEB_Ebit_Object = MibTableColumn
e1G826CurStatEB_Ebit = _E1G826CurStatEB_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 2, 1, 7),
    _E1G826CurStatEB_Ebit_Type()
)
e1G826CurStatEB_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826CurStatEB_Ebit.setStatus("mandatory")
_E1G826CurStatES_Ebit_Type = Counter32
_E1G826CurStatES_Ebit_Object = MibTableColumn
e1G826CurStatES_Ebit = _E1G826CurStatES_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 2, 1, 8),
    _E1G826CurStatES_Ebit_Type()
)
e1G826CurStatES_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826CurStatES_Ebit.setStatus("mandatory")
_E1G826CurStatSES_Ebit_Type = Counter32
_E1G826CurStatSES_Ebit_Object = MibTableColumn
e1G826CurStatSES_Ebit = _E1G826CurStatSES_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 2, 1, 9),
    _E1G826CurStatSES_Ebit_Type()
)
e1G826CurStatSES_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826CurStatSES_Ebit.setStatus("mandatory")
_E1G826CurStatAvTime_Ebit_Type = Counter32
_E1G826CurStatAvTime_Ebit_Object = MibTableColumn
e1G826CurStatAvTime_Ebit = _E1G826CurStatAvTime_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 2, 1, 10),
    _E1G826CurStatAvTime_Ebit_Type()
)
e1G826CurStatAvTime_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826CurStatAvTime_Ebit.setStatus("mandatory")
_E1G826CurStatUnAvTime_Ebit_Type = Counter32
_E1G826CurStatUnAvTime_Ebit_Object = MibTableColumn
e1G826CurStatUnAvTime_Ebit = _E1G826CurStatUnAvTime_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 2, 1, 11),
    _E1G826CurStatUnAvTime_Ebit_Type()
)
e1G826CurStatUnAvTime_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826CurStatUnAvTime_Ebit.setStatus("mandatory")
_E1G826_15m_StatTable_Object = MibTable
e1G826_15m_StatTable = _E1G826_15m_StatTable_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 3)
)
if mibBuilder.loadTexts:
    e1G826_15m_StatTable.setStatus("mandatory")
_E1G826_15m_StatEntry_Object = MibTableRow
e1G826_15m_StatEntry = _E1G826_15m_StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 3, 1)
)
e1G826_15m_StatEntry.setIndexNames(
    (0, "MLINK-PDH-MUXIP-2E1-2FE-MIB", "e1G826_15m_StatIndex"),
)
if mibBuilder.loadTexts:
    e1G826_15m_StatEntry.setStatus("mandatory")
_E1G826_15m_StatIndex_Type = Integer32
_E1G826_15m_StatIndex_Object = MibTableColumn
e1G826_15m_StatIndex = _E1G826_15m_StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 3, 1, 1),
    _E1G826_15m_StatIndex_Type()
)
e1G826_15m_StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_15m_StatIndex.setStatus("mandatory")
_E1G826_15m_StatEB_CRC4_Type = Counter32
_E1G826_15m_StatEB_CRC4_Object = MibTableColumn
e1G826_15m_StatEB_CRC4 = _E1G826_15m_StatEB_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 3, 1, 2),
    _E1G826_15m_StatEB_CRC4_Type()
)
e1G826_15m_StatEB_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_15m_StatEB_CRC4.setStatus("mandatory")
_E1G826_15m_StatES_CRC4_Type = Counter32
_E1G826_15m_StatES_CRC4_Object = MibTableColumn
e1G826_15m_StatES_CRC4 = _E1G826_15m_StatES_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 3, 1, 3),
    _E1G826_15m_StatES_CRC4_Type()
)
e1G826_15m_StatES_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_15m_StatES_CRC4.setStatus("mandatory")
_E1G826_15m_StatSES_CRC4_Type = Counter32
_E1G826_15m_StatSES_CRC4_Object = MibTableColumn
e1G826_15m_StatSES_CRC4 = _E1G826_15m_StatSES_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 3, 1, 4),
    _E1G826_15m_StatSES_CRC4_Type()
)
e1G826_15m_StatSES_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_15m_StatSES_CRC4.setStatus("mandatory")
_E1G826_15m_StatAvTime_CRC4_Type = Counter32
_E1G826_15m_StatAvTime_CRC4_Object = MibTableColumn
e1G826_15m_StatAvTime_CRC4 = _E1G826_15m_StatAvTime_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 3, 1, 5),
    _E1G826_15m_StatAvTime_CRC4_Type()
)
e1G826_15m_StatAvTime_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_15m_StatAvTime_CRC4.setStatus("mandatory")
_E1G826_15m_StatUnAvTime_CRC4_Type = Counter32
_E1G826_15m_StatUnAvTime_CRC4_Object = MibTableColumn
e1G826_15m_StatUnAvTime_CRC4 = _E1G826_15m_StatUnAvTime_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 3, 1, 6),
    _E1G826_15m_StatUnAvTime_CRC4_Type()
)
e1G826_15m_StatUnAvTime_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_15m_StatUnAvTime_CRC4.setStatus("mandatory")
_E1G826_15m_StatEB_Ebit_Type = Counter32
_E1G826_15m_StatEB_Ebit_Object = MibTableColumn
e1G826_15m_StatEB_Ebit = _E1G826_15m_StatEB_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 3, 1, 7),
    _E1G826_15m_StatEB_Ebit_Type()
)
e1G826_15m_StatEB_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_15m_StatEB_Ebit.setStatus("mandatory")
_E1G826_15m_StatES_Ebit_Type = Counter32
_E1G826_15m_StatES_Ebit_Object = MibTableColumn
e1G826_15m_StatES_Ebit = _E1G826_15m_StatES_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 3, 1, 8),
    _E1G826_15m_StatES_Ebit_Type()
)
e1G826_15m_StatES_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_15m_StatES_Ebit.setStatus("mandatory")
_E1G826_15m_StatSES_Ebit_Type = Counter32
_E1G826_15m_StatSES_Ebit_Object = MibTableColumn
e1G826_15m_StatSES_Ebit = _E1G826_15m_StatSES_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 3, 1, 9),
    _E1G826_15m_StatSES_Ebit_Type()
)
e1G826_15m_StatSES_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_15m_StatSES_Ebit.setStatus("mandatory")
_E1G826_15m_StatAvTime_Ebit_Type = Counter32
_E1G826_15m_StatAvTime_Ebit_Object = MibTableColumn
e1G826_15m_StatAvTime_Ebit = _E1G826_15m_StatAvTime_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 3, 1, 10),
    _E1G826_15m_StatAvTime_Ebit_Type()
)
e1G826_15m_StatAvTime_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_15m_StatAvTime_Ebit.setStatus("mandatory")
_E1G826_15m_StatUnAvTime_Ebit_Type = Counter32
_E1G826_15m_StatUnAvTime_Ebit_Object = MibTableColumn
e1G826_15m_StatUnAvTime_Ebit = _E1G826_15m_StatUnAvTime_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 3, 1, 11),
    _E1G826_15m_StatUnAvTime_Ebit_Type()
)
e1G826_15m_StatUnAvTime_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_15m_StatUnAvTime_Ebit.setStatus("mandatory")
_E1G826_24h_StatTable_Object = MibTable
e1G826_24h_StatTable = _E1G826_24h_StatTable_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 4)
)
if mibBuilder.loadTexts:
    e1G826_24h_StatTable.setStatus("mandatory")
_E1G826_24h_StatEntry_Object = MibTableRow
e1G826_24h_StatEntry = _E1G826_24h_StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 4, 1)
)
e1G826_24h_StatEntry.setIndexNames(
    (0, "MLINK-PDH-MUXIP-2E1-2FE-MIB", "e1G826_24h_StatIndex"),
)
if mibBuilder.loadTexts:
    e1G826_24h_StatEntry.setStatus("mandatory")
_E1G826_24h_StatIndex_Type = Integer32
_E1G826_24h_StatIndex_Object = MibTableColumn
e1G826_24h_StatIndex = _E1G826_24h_StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 4, 1, 1),
    _E1G826_24h_StatIndex_Type()
)
e1G826_24h_StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_24h_StatIndex.setStatus("mandatory")
_E1G826_24h_StatEB_CRC4_Type = Counter32
_E1G826_24h_StatEB_CRC4_Object = MibTableColumn
e1G826_24h_StatEB_CRC4 = _E1G826_24h_StatEB_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 4, 1, 2),
    _E1G826_24h_StatEB_CRC4_Type()
)
e1G826_24h_StatEB_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_24h_StatEB_CRC4.setStatus("mandatory")
_E1G826_24h_StatES_CRC4_Type = Counter32
_E1G826_24h_StatES_CRC4_Object = MibTableColumn
e1G826_24h_StatES_CRC4 = _E1G826_24h_StatES_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 4, 1, 3),
    _E1G826_24h_StatES_CRC4_Type()
)
e1G826_24h_StatES_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_24h_StatES_CRC4.setStatus("mandatory")
_E1G826_24h_StatSES_CRC4_Type = Counter32
_E1G826_24h_StatSES_CRC4_Object = MibTableColumn
e1G826_24h_StatSES_CRC4 = _E1G826_24h_StatSES_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 4, 1, 4),
    _E1G826_24h_StatSES_CRC4_Type()
)
e1G826_24h_StatSES_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_24h_StatSES_CRC4.setStatus("mandatory")
_E1G826_24h_StatAvTime_CRC4_Type = Counter32
_E1G826_24h_StatAvTime_CRC4_Object = MibTableColumn
e1G826_24h_StatAvTime_CRC4 = _E1G826_24h_StatAvTime_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 4, 1, 5),
    _E1G826_24h_StatAvTime_CRC4_Type()
)
e1G826_24h_StatAvTime_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_24h_StatAvTime_CRC4.setStatus("mandatory")
_E1G826_24h_StatUnAvTime_CRC4_Type = Counter32
_E1G826_24h_StatUnAvTime_CRC4_Object = MibTableColumn
e1G826_24h_StatUnAvTime_CRC4 = _E1G826_24h_StatUnAvTime_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 4, 1, 6),
    _E1G826_24h_StatUnAvTime_CRC4_Type()
)
e1G826_24h_StatUnAvTime_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_24h_StatUnAvTime_CRC4.setStatus("mandatory")
_E1G826_24h_StatEB_Ebit_Type = Counter32
_E1G826_24h_StatEB_Ebit_Object = MibTableColumn
e1G826_24h_StatEB_Ebit = _E1G826_24h_StatEB_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 4, 1, 7),
    _E1G826_24h_StatEB_Ebit_Type()
)
e1G826_24h_StatEB_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_24h_StatEB_Ebit.setStatus("mandatory")
_E1G826_24h_StatES_Ebit_Type = Counter32
_E1G826_24h_StatES_Ebit_Object = MibTableColumn
e1G826_24h_StatES_Ebit = _E1G826_24h_StatES_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 4, 1, 8),
    _E1G826_24h_StatES_Ebit_Type()
)
e1G826_24h_StatES_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_24h_StatES_Ebit.setStatus("mandatory")
_E1G826_24h_StatSES_Ebit_Type = Counter32
_E1G826_24h_StatSES_Ebit_Object = MibTableColumn
e1G826_24h_StatSES_Ebit = _E1G826_24h_StatSES_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 4, 1, 9),
    _E1G826_24h_StatSES_Ebit_Type()
)
e1G826_24h_StatSES_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_24h_StatSES_Ebit.setStatus("mandatory")
_E1G826_24h_StatAvTime_Ebit_Type = Counter32
_E1G826_24h_StatAvTime_Ebit_Object = MibTableColumn
e1G826_24h_StatAvTime_Ebit = _E1G826_24h_StatAvTime_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 4, 1, 10),
    _E1G826_24h_StatAvTime_Ebit_Type()
)
e1G826_24h_StatAvTime_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_24h_StatAvTime_Ebit.setStatus("mandatory")
_E1G826_24h_StatUnAvTime_Ebit_Type = Counter32
_E1G826_24h_StatUnAvTime_Ebit_Object = MibTableColumn
e1G826_24h_StatUnAvTime_Ebit = _E1G826_24h_StatUnAvTime_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 4, 1, 11),
    _E1G826_24h_StatUnAvTime_Ebit_Type()
)
e1G826_24h_StatUnAvTime_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_24h_StatUnAvTime_Ebit.setStatus("mandatory")
_E1G826_7d_StatTable_Object = MibTable
e1G826_7d_StatTable = _E1G826_7d_StatTable_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 5)
)
if mibBuilder.loadTexts:
    e1G826_7d_StatTable.setStatus("mandatory")
_E1G826_7d_StatEntry_Object = MibTableRow
e1G826_7d_StatEntry = _E1G826_7d_StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 5, 1)
)
e1G826_7d_StatEntry.setIndexNames(
    (0, "MLINK-PDH-MUXIP-2E1-2FE-MIB", "e1G826_7d_StatIndex"),
)
if mibBuilder.loadTexts:
    e1G826_7d_StatEntry.setStatus("mandatory")
_E1G826_7d_StatIndex_Type = Integer32
_E1G826_7d_StatIndex_Object = MibTableColumn
e1G826_7d_StatIndex = _E1G826_7d_StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 5, 1, 1),
    _E1G826_7d_StatIndex_Type()
)
e1G826_7d_StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_7d_StatIndex.setStatus("mandatory")
_E1G826_7d_StatEB_CRC4_Type = Counter32
_E1G826_7d_StatEB_CRC4_Object = MibTableColumn
e1G826_7d_StatEB_CRC4 = _E1G826_7d_StatEB_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 5, 1, 2),
    _E1G826_7d_StatEB_CRC4_Type()
)
e1G826_7d_StatEB_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_7d_StatEB_CRC4.setStatus("mandatory")
_E1G826_7d_StatES_CRC4_Type = Counter32
_E1G826_7d_StatES_CRC4_Object = MibTableColumn
e1G826_7d_StatES_CRC4 = _E1G826_7d_StatES_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 5, 1, 3),
    _E1G826_7d_StatES_CRC4_Type()
)
e1G826_7d_StatES_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_7d_StatES_CRC4.setStatus("mandatory")
_E1G826_7d_StatSES_CRC4_Type = Counter32
_E1G826_7d_StatSES_CRC4_Object = MibTableColumn
e1G826_7d_StatSES_CRC4 = _E1G826_7d_StatSES_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 5, 1, 4),
    _E1G826_7d_StatSES_CRC4_Type()
)
e1G826_7d_StatSES_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_7d_StatSES_CRC4.setStatus("mandatory")
_E1G826_7d_StatAvTime_CRC4_Type = Counter32
_E1G826_7d_StatAvTime_CRC4_Object = MibTableColumn
e1G826_7d_StatAvTime_CRC4 = _E1G826_7d_StatAvTime_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 5, 1, 5),
    _E1G826_7d_StatAvTime_CRC4_Type()
)
e1G826_7d_StatAvTime_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_7d_StatAvTime_CRC4.setStatus("mandatory")
_E1G826_7d_StatUnAvTime_CRC4_Type = Counter32
_E1G826_7d_StatUnAvTime_CRC4_Object = MibTableColumn
e1G826_7d_StatUnAvTime_CRC4 = _E1G826_7d_StatUnAvTime_CRC4_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 5, 1, 6),
    _E1G826_7d_StatUnAvTime_CRC4_Type()
)
e1G826_7d_StatUnAvTime_CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_7d_StatUnAvTime_CRC4.setStatus("mandatory")
_E1G826_7d_StatEB_Ebit_Type = Counter32
_E1G826_7d_StatEB_Ebit_Object = MibTableColumn
e1G826_7d_StatEB_Ebit = _E1G826_7d_StatEB_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 5, 1, 7),
    _E1G826_7d_StatEB_Ebit_Type()
)
e1G826_7d_StatEB_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_7d_StatEB_Ebit.setStatus("mandatory")
_E1G826_7d_StatES_Ebit_Type = Counter32
_E1G826_7d_StatES_Ebit_Object = MibTableColumn
e1G826_7d_StatES_Ebit = _E1G826_7d_StatES_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 5, 1, 8),
    _E1G826_7d_StatES_Ebit_Type()
)
e1G826_7d_StatES_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_7d_StatES_Ebit.setStatus("mandatory")
_E1G826_7d_StatSES_Ebit_Type = Counter32
_E1G826_7d_StatSES_Ebit_Object = MibTableColumn
e1G826_7d_StatSES_Ebit = _E1G826_7d_StatSES_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 5, 1, 9),
    _E1G826_7d_StatSES_Ebit_Type()
)
e1G826_7d_StatSES_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_7d_StatSES_Ebit.setStatus("mandatory")
_E1G826_7d_StatAvTime_Ebit_Type = Counter32
_E1G826_7d_StatAvTime_Ebit_Object = MibTableColumn
e1G826_7d_StatAvTime_Ebit = _E1G826_7d_StatAvTime_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 5, 1, 10),
    _E1G826_7d_StatAvTime_Ebit_Type()
)
e1G826_7d_StatAvTime_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_7d_StatAvTime_Ebit.setStatus("mandatory")
_E1G826_7d_StatUnAvTime_Ebit_Type = Counter32
_E1G826_7d_StatUnAvTime_Ebit_Object = MibTableColumn
e1G826_7d_StatUnAvTime_Ebit = _E1G826_7d_StatUnAvTime_Ebit_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 2, 5, 1, 11),
    _E1G826_7d_StatUnAvTime_Ebit_Type()
)
e1G826_7d_StatUnAvTime_Ebit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1G826_7d_StatUnAvTime_Ebit.setStatus("mandatory")
_EthState_ObjectIdentity = ObjectIdentity
ethState = _EthState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 3)
)
_CopperEthStatTable_Object = MibTable
copperEthStatTable = _CopperEthStatTable_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    copperEthStatTable.setStatus("mandatory")
_CopperEthStatEntry_Object = MibTableRow
copperEthStatEntry = _CopperEthStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 3, 1, 1)
)
copperEthStatEntry.setIndexNames(
    (0, "MLINK-PDH-MUXIP-2E1-2FE-MIB", "copperEthStatIndex"),
)
if mibBuilder.loadTexts:
    copperEthStatEntry.setStatus("mandatory")
_CopperEthStatIndex_Type = Integer32
_CopperEthStatIndex_Object = MibTableColumn
copperEthStatIndex = _CopperEthStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 3, 1, 1, 1),
    _CopperEthStatIndex_Type()
)
copperEthStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copperEthStatIndex.setStatus("mandatory")
_CopperEthStatStatus_Type = Integer32
_CopperEthStatStatus_Object = MibTableColumn
copperEthStatStatus = _CopperEthStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 3, 1, 1, 2),
    _CopperEthStatStatus_Type()
)
copperEthStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copperEthStatStatus.setStatus("mandatory")
_CopperEthStatRxGoodOctets_Type = Counter32
_CopperEthStatRxGoodOctets_Object = MibTableColumn
copperEthStatRxGoodOctets = _CopperEthStatRxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 3, 1, 1, 3),
    _CopperEthStatRxGoodOctets_Type()
)
copperEthStatRxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copperEthStatRxGoodOctets.setStatus("mandatory")
_CopperEthStatRxBadOctets_Type = Counter32
_CopperEthStatRxBadOctets_Object = MibTableColumn
copperEthStatRxBadOctets = _CopperEthStatRxBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 3, 1, 1, 4),
    _CopperEthStatRxBadOctets_Type()
)
copperEthStatRxBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copperEthStatRxBadOctets.setStatus("mandatory")
_CopperEthStatRxFrames_Type = Counter32
_CopperEthStatRxFrames_Object = MibTableColumn
copperEthStatRxFrames = _CopperEthStatRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 3, 1, 1, 5),
    _CopperEthStatRxFrames_Type()
)
copperEthStatRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copperEthStatRxFrames.setStatus("mandatory")
_CopperEthStatRxErrors_Type = Counter32
_CopperEthStatRxErrors_Object = MibTableColumn
copperEthStatRxErrors = _CopperEthStatRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 3, 1, 1, 6),
    _CopperEthStatRxErrors_Type()
)
copperEthStatRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copperEthStatRxErrors.setStatus("mandatory")
_CopperEthStatTxOctets_Type = Counter32
_CopperEthStatTxOctets_Object = MibTableColumn
copperEthStatTxOctets = _CopperEthStatTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 3, 1, 1, 7),
    _CopperEthStatTxOctets_Type()
)
copperEthStatTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copperEthStatTxOctets.setStatus("mandatory")
_CopperEthStatTxFrames_Type = Counter32
_CopperEthStatTxFrames_Object = MibTableColumn
copperEthStatTxFrames = _CopperEthStatTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 3, 1, 1, 8),
    _CopperEthStatTxFrames_Type()
)
copperEthStatTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copperEthStatTxFrames.setStatus("mandatory")
_BundleState_ObjectIdentity = ObjectIdentity
bundleState = _BundleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4)
)
_BundleStatTable_Object = MibTable
bundleStatTable = _BundleStatTable_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    bundleStatTable.setStatus("mandatory")
_BundleStatEntry_Object = MibTableRow
bundleStatEntry = _BundleStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 1, 1)
)
bundleStatEntry.setIndexNames(
    (0, "MLINK-PDH-MUXIP-2E1-2FE-MIB", "bundleStatIndex"),
)
if mibBuilder.loadTexts:
    bundleStatEntry.setStatus("mandatory")
_BundleStatIndex_Type = Integer32
_BundleStatIndex_Object = MibTableColumn
bundleStatIndex = _BundleStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 1, 1, 1),
    _BundleStatIndex_Type()
)
bundleStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleStatIndex.setStatus("mandatory")


class _BundleStatStatus_Type(Integer32):
    """Custom type bundleStatStatus based on Integer32"""
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
        *(("Inactive", 0),
          ("Dst_MAC_detection", 1),
          ("OAM_handshake", 2),
          ("Connected", 3),
          ("Closing", 4))
    )


_BundleStatStatus_Type.__name__ = "Integer32"
_BundleStatStatus_Object = MibTableColumn
bundleStatStatus = _BundleStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 1, 1, 2),
    _BundleStatStatus_Type()
)
bundleStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleStatStatus.setStatus("mandatory")
_BundleStatFlags_Type = Integer32
_BundleStatFlags_Object = MibTableColumn
bundleStatFlags = _BundleStatFlags_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 1, 1, 3),
    _BundleStatFlags_Type()
)
bundleStatFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleStatFlags.setStatus("mandatory")
_BundleStatRxGoodFrames_Type = Counter32
_BundleStatRxGoodFrames_Object = MibTableColumn
bundleStatRxGoodFrames = _BundleStatRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 1, 1, 4),
    _BundleStatRxGoodFrames_Type()
)
bundleStatRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleStatRxGoodFrames.setStatus("mandatory")
_BundleStatRxLostFrames_Type = Counter32
_BundleStatRxLostFrames_Object = MibTableColumn
bundleStatRxLostFrames = _BundleStatRxLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 1, 1, 5),
    _BundleStatRxLostFrames_Type()
)
bundleStatRxLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleStatRxLostFrames.setStatus("mandatory")
_BundleStatRxLostCells_Type = Counter32
_BundleStatRxLostCells_Object = MibTableColumn
bundleStatRxLostCells = _BundleStatRxLostCells_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 1, 1, 6),
    _BundleStatRxLostCells_Type()
)
bundleStatRxLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleStatRxLostCells.setStatus("mandatory")
_BundleStatRxOowFrames_Type = Counter32
_BundleStatRxOowFrames_Object = MibTableColumn
bundleStatRxOowFrames = _BundleStatRxOowFrames_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 1, 1, 7),
    _BundleStatRxOowFrames_Type()
)
bundleStatRxOowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleStatRxOowFrames.setStatus("mandatory")
_BundleStatTxGoodFrames_Type = Counter32
_BundleStatTxGoodFrames_Object = MibTableColumn
bundleStatTxGoodFrames = _BundleStatTxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 1, 1, 8),
    _BundleStatTxGoodFrames_Type()
)
bundleStatTxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleStatTxGoodFrames.setStatus("mandatory")


class _BundleStatJBC_Status_Type(Integer32):
    """Custom type bundleStatJBC_Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Empty", 0),
          ("OK", 1),
          ("Full", 2))
    )


_BundleStatJBC_Status_Type.__name__ = "Integer32"
_BundleStatJBC_Status_Object = MibTableColumn
bundleStatJBC_Status = _BundleStatJBC_Status_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 1, 1, 9),
    _BundleStatJBC_Status_Type()
)
bundleStatJBC_Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleStatJBC_Status.setStatus("mandatory")
_BundleStatJBC_CurLevel_Type = Integer32
_BundleStatJBC_CurLevel_Object = MibTableColumn
bundleStatJBC_CurLevel = _BundleStatJBC_CurLevel_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 1, 1, 10),
    _BundleStatJBC_CurLevel_Type()
)
bundleStatJBC_CurLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleStatJBC_CurLevel.setStatus("mandatory")
_BundleStatJBC_MinLevel_Type = Integer32
_BundleStatJBC_MinLevel_Object = MibTableColumn
bundleStatJBC_MinLevel = _BundleStatJBC_MinLevel_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 1, 1, 11),
    _BundleStatJBC_MinLevel_Type()
)
bundleStatJBC_MinLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleStatJBC_MinLevel.setStatus("mandatory")
_BundleStatJBC_MaxLevel_Type = Integer32
_BundleStatJBC_MaxLevel_Object = MibTableColumn
bundleStatJBC_MaxLevel = _BundleStatJBC_MaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 1, 1, 12),
    _BundleStatJBC_MaxLevel_Type()
)
bundleStatJBC_MaxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleStatJBC_MaxLevel.setStatus("mandatory")
_BundleStatJBC_Overrun_Type = Counter32
_BundleStatJBC_Overrun_Object = MibTableColumn
bundleStatJBC_Overrun = _BundleStatJBC_Overrun_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 1, 1, 13),
    _BundleStatJBC_Overrun_Type()
)
bundleStatJBC_Overrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleStatJBC_Overrun.setStatus("mandatory")
_BundleStatJBC_Underrun_Type = Counter32
_BundleStatJBC_Underrun_Object = MibTableColumn
bundleStatJBC_Underrun = _BundleStatJBC_Underrun_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 1, 1, 14),
    _BundleStatJBC_Underrun_Type()
)
bundleStatJBC_Underrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleStatJBC_Underrun.setStatus("mandatory")
_E1AdaptClkStatTable_Object = MibTable
e1AdaptClkStatTable = _E1AdaptClkStatTable_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 2)
)
if mibBuilder.loadTexts:
    e1AdaptClkStatTable.setStatus("mandatory")
_E1AdaptClkStatEntry_Object = MibTableRow
e1AdaptClkStatEntry = _E1AdaptClkStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 2, 1)
)
e1AdaptClkStatEntry.setIndexNames(
    (0, "MLINK-PDH-MUXIP-2E1-2FE-MIB", "e1AdaptClkStatIndex"),
)
if mibBuilder.loadTexts:
    e1AdaptClkStatEntry.setStatus("mandatory")
_E1AdaptClkStatIndex_Type = Integer32
_E1AdaptClkStatIndex_Object = MibTableColumn
e1AdaptClkStatIndex = _E1AdaptClkStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 2, 1, 1),
    _E1AdaptClkStatIndex_Type()
)
e1AdaptClkStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1AdaptClkStatIndex.setStatus("mandatory")


class _E1AdaptClkStatStatus_Type(Integer32):
    """Custom type e1AdaptClkStatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("Idle", 0),
          ("Acquisition", 2),
          ("Tracking1", 3),
          ("Tracking2", 4),
          ("OverOrUnderrun_recovery", 5))
    )


_E1AdaptClkStatStatus_Type.__name__ = "Integer32"
_E1AdaptClkStatStatus_Object = MibTableColumn
e1AdaptClkStatStatus = _E1AdaptClkStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 2, 1, 2),
    _E1AdaptClkStatStatus_Type()
)
e1AdaptClkStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1AdaptClkStatStatus.setStatus("mandatory")
_E1AdaptClkStatRestartCounter_Type = Counter32
_E1AdaptClkStatRestartCounter_Object = MibTableColumn
e1AdaptClkStatRestartCounter = _E1AdaptClkStatRestartCounter_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 4, 2, 1, 3),
    _E1AdaptClkStatRestartCounter_Type()
)
e1AdaptClkStatRestartCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1AdaptClkStatRestartCounter.setStatus("mandatory")
_EventJournal_ObjectIdentity = ObjectIdentity
eventJournal = _EventJournal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 5)
)
_EventsTable_Object = MibTable
eventsTable = _EventsTable_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 5, 1)
)
if mibBuilder.loadTexts:
    eventsTable.setStatus("mandatory")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 5, 1, 1)
)
eventEntry.setIndexNames(
    (0, "MLINK-PDH-MUXIP-2E1-2FE-MIB", "EventIndex"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("mandatory")
_EventIndex_Type = Integer32
_EventIndex_Object = MibTableColumn
eventIndex = _EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 5, 1, 1, 1),
    _EventIndex_Type()
)
eventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventIndex.setStatus("mandatory")


class _EventElement_Type(OctetString):
    """Custom type eventElement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_EventElement_Type.__name__ = "OctetString"
_EventElement_Object = MibTableColumn
eventElement = _EventElement_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 3, 5, 1, 1, 2),
    _EventElement_Type()
)
eventElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventElement.setStatus("mandatory")
_Trap_bind_ObjectIdentity = ObjectIdentity
trap_bind = _Trap_bind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 4)
)


class _Trap_GlobalAlarm_Type(Integer32):
    """Custom type trap_GlobalAlarm based on Integer32"""
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
        *(("Normal", 0),
          ("Major", 1),
          ("Minor", 2),
          ("MajorAndMinor", 3))
    )


_Trap_GlobalAlarm_Type.__name__ = "Integer32"
_Trap_GlobalAlarm_Object = MibScalar
trap_GlobalAlarm = _Trap_GlobalAlarm_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 4, 1),
    _Trap_GlobalAlarm_Type()
)
trap_GlobalAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trap_GlobalAlarm.setStatus("mandatory")
_Trap_EventType_Type = Integer32
_Trap_EventType_Object = MibScalar
trap_EventType = _Trap_EventType_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 4, 2),
    _Trap_EventType_Type()
)
trap_EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trap_EventType.setStatus("mandatory")
_Trap_IfIndex_Type = Integer32
_Trap_IfIndex_Object = MibScalar
trap_IfIndex = _Trap_IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 4, 3),
    _Trap_IfIndex_Type()
)
trap_IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trap_IfIndex.setStatus("mandatory")
_Trap_IfStatus_Type = Integer32
_Trap_IfStatus_Object = MibScalar
trap_IfStatus = _Trap_IfStatus_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 4, 4),
    _Trap_IfStatus_Type()
)
trap_IfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trap_IfStatus.setStatus("mandatory")
_Commands_ObjectIdentity = ObjectIdentity
commands = _Commands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 5)
)


class _ApplyCmd_Type(Integer32):
    """Custom type applyCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("Set", 1)
    )


_ApplyCmd_Type.__name__ = "Integer32"
_ApplyCmd_Object = MibScalar
applyCmd = _ApplyCmd_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 5, 1),
    _ApplyCmd_Type()
)
applyCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applyCmd.setStatus("mandatory")


class _SaveCmd_Type(Integer32):
    """Custom type saveCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("Set", 1)
    )


_SaveCmd_Type.__name__ = "Integer32"
_SaveCmd_Object = MibScalar
saveCmd = _SaveCmd_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 5, 2),
    _SaveCmd_Type()
)
saveCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveCmd.setStatus("mandatory")


class _RestoreCmd_Type(Integer32):
    """Custom type restoreCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("Set", 1)
    )


_RestoreCmd_Type.__name__ = "Integer32"
_RestoreCmd_Object = MibScalar
restoreCmd = _RestoreCmd_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 5, 3),
    _RestoreCmd_Type()
)
restoreCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restoreCmd.setStatus("mandatory")


class _ResetCmd_Type(Integer32):
    """Custom type resetCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("Set", 1)
    )


_ResetCmd_Type.__name__ = "Integer32"
_ResetCmd_Object = MibScalar
resetCmd = _ResetCmd_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 5, 4),
    _ResetCmd_Type()
)
resetCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetCmd.setStatus("mandatory")


class _JournalEraseCmd_Type(Integer32):
    """Custom type journalEraseCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("Set", 1)
    )


_JournalEraseCmd_Type.__name__ = "Integer32"
_JournalEraseCmd_Object = MibScalar
journalEraseCmd = _JournalEraseCmd_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 5, 5),
    _JournalEraseCmd_Type()
)
journalEraseCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    journalEraseCmd.setStatus("mandatory")
_ClearStatsCmd_Type = Integer32
_ClearStatsCmd_Object = MibScalar
clearStatsCmd = _ClearStatsCmd_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 5, 6),
    _ClearStatsCmd_Type()
)
clearStatsCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearStatsCmd.setStatus("mandatory")


class _ResetSettingsCmd_Type(Integer32):
    """Custom type resetSettingsCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("Set", 1)
    )


_ResetSettingsCmd_Type.__name__ = "Integer32"
_ResetSettingsCmd_Object = MibScalar
resetSettingsCmd = _ResetSettingsCmd_Object(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 5, 7),
    _ResetSettingsCmd_Type()
)
resetSettingsCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetSettingsCmd.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mLink_MUXIP_2E1_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 28568, 2, 21, 3, 0, 1)
)
mLink_MUXIP_2E1_trap.setObjects(
      *(("MLINK-PDH-MUXIP-2E1-2FE-MIB", "sysType"),
        ("MLINK-PDH-MUXIP-2E1-2FE-MIB", "Net_ID"),
        ("MLINK-PDH-MUXIP-2E1-2FE-MIB", "sysSw_Version"),
        ("MLINK-PDH-MUXIP-2E1-2FE-MIB", "sysHw_Version"),
        ("MLINK-PDH-MUXIP-2E1-2FE-MIB", "sysSerial_Num"),
        ("MLINK-PDH-MUXIP-2E1-2FE-MIB", "trap_GlobalAlarm"),
        ("MLINK-PDH-MUXIP-2E1-2FE-MIB", "trap_EventType"),
        ("MLINK-PDH-MUXIP-2E1-2FE-MIB", "trap_IfIndex"),
        ("MLINK-PDH-MUXIP-2E1-2FE-MIB", "trap_IfStatus"))
)
if mibBuilder.loadTexts:
    mLink_MUXIP_2E1_trap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MLINK-PDH-MUXIP-2E1-2FE-MIB",
    **{"microlink": microlink,
       "pdh": pdh,
       "mLink-FM-GE": mLink_FM_GE,
       "mLink-MUXIP-2E1": mLink_MUXIP_2E1,
       "mLink-MUXIP-2E1-trap": mLink_MUXIP_2E1_trap,
       "sysInfo": sysInfo,
       "sysType": sysType,
       "sysHw_Version": sysHw_Version,
       "sysSw_Version": sysSw_Version,
       "sysSerial_Num": sysSerial_Num,
       "sysFactoryCode": sysFactoryCode,
       "sysConfig": sysConfig,
       "hostIPConfig": hostIPConfig,
       "hostIpAddress": hostIpAddress,
       "hostPhysAddress": hostPhysAddress,
       "hostSubnetMask": hostSubnetMask,
       "hostGwIpAddress": hostGwIpAddress,
       "hostVLAN_ID": hostVLAN_ID,
       "commonConfig": commonConfig,
       "globalSettings": globalSettings,
       "net_ID": net_ID,
       "consoleTimeout": consoleTimeout,
       "tDMoIP_global_settings": tDMoIP_global_settings,
       "dstBundleID_UDPPortHead": dstBundleID_UDPPortHead,
       "e1Config": e1Config,
       "e1CfgTable": e1CfgTable,
       "e1CfgEntry": e1CfgEntry,
       "e1CfgIndex": e1CfgIndex,
       "e1CfgConfig": e1CfgConfig,
       "e1CfgSyncSequence": e1CfgSyncSequence,
       "ethConfig": ethConfig,
       "copperEthCfgTable": copperEthCfgTable,
       "copperEthCfgEntry": copperEthCfgEntry,
       "copperEthCfgIndex": copperEthCfgIndex,
       "copperEthCfgConfig": copperEthCfgConfig,
       "bundleConfig": bundleConfig,
       "bundleCfgTable": bundleCfgTable,
       "bundleCfgEntry": bundleCfgEntry,
       "bundleCfgIndex": bundleCfgIndex,
       "bundleCfgFlags": bundleCfgFlags,
       "bundleCfgBundleID": bundleCfgBundleID,
       "bundleCfgDst_IP": bundleCfgDst_IP,
       "bundleCfgDst_BundleID": bundleCfgDst_BundleID,
       "bundleCfgE1_PortNumber": bundleCfgE1_PortNumber,
       "bundleCfgTS_table": bundleCfgTS_table,
       "bundleCfgFrameCellNumber": bundleCfgFrameCellNumber,
       "bundleCfgPDVT": bundleCfgPDVT,
       "bundleCfgIP_TOS": bundleCfgIP_TOS,
       "bundleCfgTag_Pri": bundleCfgTag_Pri,
       "e1AdaptClkCfgTable": e1AdaptClkCfgTable,
       "e1AdaptClkCfgEntry": e1AdaptClkCfgEntry,
       "e1AdaptClkCfgIndex": e1AdaptClkCfgIndex,
       "e1AdaptClkCfgConfig": e1AdaptClkCfgConfig,
       "snmpConfig": snmpConfig,
       "snmpTrap_Dst1_IpAddress": snmpTrap_Dst1_IpAddress,
       "snmpTrap_Dst2_IpAddress": snmpTrap_Dst2_IpAddress,
       "snmpTrap-Dest1Port": snmpTrap_Dest1Port,
       "snmpTrap-Dest2Port": snmpTrap_Dest2Port,
       "snmpTrap-Time1": snmpTrap_Time1,
       "snmpTrap-Time2": snmpTrap_Time2,
       "snmpCommunity": snmpCommunity,
       "vlanConfig": vlanConfig,
       "cpu_default_VID": cpu_default_VID,
       "vlan_PortCfgTable": vlan_PortCfgTable,
       "vlan_PortCfgEntry": vlan_PortCfgEntry,
       "vlan_PortCfgIndex": vlan_PortCfgIndex,
       "vlan_PortCfgDefVID": vlan_PortCfgDefVID,
       "vlan_PortCfgConfig": vlan_PortCfgConfig,
       "vlan_Table": vlan_Table,
       "vlan_TableEntry": vlan_TableEntry,
       "vlan_TableIndex": vlan_TableIndex,
       "vlan_TableVID": vlan_TableVID,
       "vlan_TableMember": vlan_TableMember,
       "qosConfig": qosConfig,
       "cpu_QoS_cfg": cpu_QoS_cfg,
       "tag_Pri_mapping": tag_Pri_mapping,
       "dscp_Pri_mapping": dscp_Pri_mapping,
       "dscp_mapEntry": dscp_mapEntry,
       "dscp_mapIndex": dscp_mapIndex,
       "dscp_mapValue": dscp_mapValue,
       "qos_PortCfgTable": qos_PortCfgTable,
       "qos_PortCfgEntry": qos_PortCfgEntry,
       "qos_PortCfgIndex": qos_PortCfgIndex,
       "qos_PortCfgConfig": qos_PortCfgConfig,
       "sysState": sysState,
       "commonState": commonState,
       "localAlarm": localAlarm,
       "sysTime": sysTime,
       "e1State": e1State,
       "e1StatusTable": e1StatusTable,
       "e1StatusEntry": e1StatusEntry,
       "e1StatusIndex": e1StatusIndex,
       "e1StatusStatus": e1StatusStatus,
       "e1StatusSyncSource": e1StatusSyncSource,
       "e1StatusCV_Errors": e1StatusCV_Errors,
       "e1StatusFAS_Errors": e1StatusFAS_Errors,
       "e1StatusCRC4_Errors": e1StatusCRC4_Errors,
       "e1StatusEbit_Errors": e1StatusEbit_Errors,
       "e1G826CurStatTable": e1G826CurStatTable,
       "e1G826CurStatEntry": e1G826CurStatEntry,
       "e1G826CurStatIndex": e1G826CurStatIndex,
       "e1G826CurStatEB_CRC4": e1G826CurStatEB_CRC4,
       "e1G826CurStatES_CRC4": e1G826CurStatES_CRC4,
       "e1G826CurStatSES_CRC4": e1G826CurStatSES_CRC4,
       "e1G826CurStatAvTime_CRC4": e1G826CurStatAvTime_CRC4,
       "e1G826CurStatUnAvTime_CRC4": e1G826CurStatUnAvTime_CRC4,
       "e1G826CurStatEB_Ebit": e1G826CurStatEB_Ebit,
       "e1G826CurStatES_Ebit": e1G826CurStatES_Ebit,
       "e1G826CurStatSES_Ebit": e1G826CurStatSES_Ebit,
       "e1G826CurStatAvTime_Ebit": e1G826CurStatAvTime_Ebit,
       "e1G826CurStatUnAvTime_Ebit": e1G826CurStatUnAvTime_Ebit,
       "e1G826_15m_StatTable": e1G826_15m_StatTable,
       "e1G826_15m_StatEntry": e1G826_15m_StatEntry,
       "e1G826_15m_StatIndex": e1G826_15m_StatIndex,
       "e1G826_15m_StatEB_CRC4": e1G826_15m_StatEB_CRC4,
       "e1G826_15m_StatES_CRC4": e1G826_15m_StatES_CRC4,
       "e1G826_15m_StatSES_CRC4": e1G826_15m_StatSES_CRC4,
       "e1G826_15m_StatAvTime_CRC4": e1G826_15m_StatAvTime_CRC4,
       "e1G826_15m_StatUnAvTime_CRC4": e1G826_15m_StatUnAvTime_CRC4,
       "e1G826_15m_StatEB_Ebit": e1G826_15m_StatEB_Ebit,
       "e1G826_15m_StatES_Ebit": e1G826_15m_StatES_Ebit,
       "e1G826_15m_StatSES_Ebit": e1G826_15m_StatSES_Ebit,
       "e1G826_15m_StatAvTime_Ebit": e1G826_15m_StatAvTime_Ebit,
       "e1G826_15m_StatUnAvTime_Ebit": e1G826_15m_StatUnAvTime_Ebit,
       "e1G826_24h_StatTable": e1G826_24h_StatTable,
       "e1G826_24h_StatEntry": e1G826_24h_StatEntry,
       "e1G826_24h_StatIndex": e1G826_24h_StatIndex,
       "e1G826_24h_StatEB_CRC4": e1G826_24h_StatEB_CRC4,
       "e1G826_24h_StatES_CRC4": e1G826_24h_StatES_CRC4,
       "e1G826_24h_StatSES_CRC4": e1G826_24h_StatSES_CRC4,
       "e1G826_24h_StatAvTime_CRC4": e1G826_24h_StatAvTime_CRC4,
       "e1G826_24h_StatUnAvTime_CRC4": e1G826_24h_StatUnAvTime_CRC4,
       "e1G826_24h_StatEB_Ebit": e1G826_24h_StatEB_Ebit,
       "e1G826_24h_StatES_Ebit": e1G826_24h_StatES_Ebit,
       "e1G826_24h_StatSES_Ebit": e1G826_24h_StatSES_Ebit,
       "e1G826_24h_StatAvTime_Ebit": e1G826_24h_StatAvTime_Ebit,
       "e1G826_24h_StatUnAvTime_Ebit": e1G826_24h_StatUnAvTime_Ebit,
       "e1G826_7d_StatTable": e1G826_7d_StatTable,
       "e1G826_7d_StatEntry": e1G826_7d_StatEntry,
       "e1G826_7d_StatIndex": e1G826_7d_StatIndex,
       "e1G826_7d_StatEB_CRC4": e1G826_7d_StatEB_CRC4,
       "e1G826_7d_StatES_CRC4": e1G826_7d_StatES_CRC4,
       "e1G826_7d_StatSES_CRC4": e1G826_7d_StatSES_CRC4,
       "e1G826_7d_StatAvTime_CRC4": e1G826_7d_StatAvTime_CRC4,
       "e1G826_7d_StatUnAvTime_CRC4": e1G826_7d_StatUnAvTime_CRC4,
       "e1G826_7d_StatEB_Ebit": e1G826_7d_StatEB_Ebit,
       "e1G826_7d_StatES_Ebit": e1G826_7d_StatES_Ebit,
       "e1G826_7d_StatSES_Ebit": e1G826_7d_StatSES_Ebit,
       "e1G826_7d_StatAvTime_Ebit": e1G826_7d_StatAvTime_Ebit,
       "e1G826_7d_StatUnAvTime_Ebit": e1G826_7d_StatUnAvTime_Ebit,
       "ethState": ethState,
       "copperEthStatTable": copperEthStatTable,
       "copperEthStatEntry": copperEthStatEntry,
       "copperEthStatIndex": copperEthStatIndex,
       "copperEthStatStatus": copperEthStatStatus,
       "copperEthStatRxGoodOctets": copperEthStatRxGoodOctets,
       "copperEthStatRxBadOctets": copperEthStatRxBadOctets,
       "copperEthStatRxFrames": copperEthStatRxFrames,
       "copperEthStatRxErrors": copperEthStatRxErrors,
       "copperEthStatTxOctets": copperEthStatTxOctets,
       "copperEthStatTxFrames": copperEthStatTxFrames,
       "bundleState": bundleState,
       "bundleStatTable": bundleStatTable,
       "bundleStatEntry": bundleStatEntry,
       "bundleStatIndex": bundleStatIndex,
       "bundleStatStatus": bundleStatStatus,
       "bundleStatFlags": bundleStatFlags,
       "bundleStatRxGoodFrames": bundleStatRxGoodFrames,
       "bundleStatRxLostFrames": bundleStatRxLostFrames,
       "bundleStatRxLostCells": bundleStatRxLostCells,
       "bundleStatRxOowFrames": bundleStatRxOowFrames,
       "bundleStatTxGoodFrames": bundleStatTxGoodFrames,
       "bundleStatJBC_Status": bundleStatJBC_Status,
       "bundleStatJBC_CurLevel": bundleStatJBC_CurLevel,
       "bundleStatJBC_MinLevel": bundleStatJBC_MinLevel,
       "bundleStatJBC_MaxLevel": bundleStatJBC_MaxLevel,
       "bundleStatJBC_Overrun": bundleStatJBC_Overrun,
       "bundleStatJBC_Underrun": bundleStatJBC_Underrun,
       "e1AdaptClkStatTable": e1AdaptClkStatTable,
       "e1AdaptClkStatEntry": e1AdaptClkStatEntry,
       "e1AdaptClkStatIndex": e1AdaptClkStatIndex,
       "e1AdaptClkStatStatus": e1AdaptClkStatStatus,
       "e1AdaptClkStatRestartCounter": e1AdaptClkStatRestartCounter,
       "eventJournal": eventJournal,
       "eventsTable": eventsTable,
       "eventEntry": eventEntry,
       "eventIndex": eventIndex,
       "eventElement": eventElement,
       "trap-bind": trap_bind,
       "trap_GlobalAlarm": trap_GlobalAlarm,
       "trap_EventType": trap_EventType,
       "trap_IfIndex": trap_IfIndex,
       "trap_IfStatus": trap_IfStatus,
       "commands": commands,
       "applyCmd": applyCmd,
       "saveCmd": saveCmd,
       "restoreCmd": restoreCmd,
       "resetCmd": resetCmd,
       "journalEraseCmd": journalEraseCmd,
       "clearStatsCmd": clearStatsCmd,
       "resetSettingsCmd": resetSettingsCmd}
)
