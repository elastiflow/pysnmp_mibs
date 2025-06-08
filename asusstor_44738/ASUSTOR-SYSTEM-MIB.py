# SNMP MIB module (ASUSTOR-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/asusstor_44738/ASUSTOR-SYSTEM-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:41:54 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

asustorSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 44738, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Asustor_ObjectIdentity = ObjectIdentity
asustor = _Asustor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44738)
)
_SysSerialNumber_Type = OctetString
_SysSerialNumber_Object = MibScalar
sysSerialNumber = _SysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 44738, 1, 1),
    _SysSerialNumber_Type()
)
sysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSerialNumber.setStatus("current")
_SysADMVersion_Type = OctetString
_SysADMVersion_Object = MibScalar
sysADMVersion = _SysADMVersion_Object(
    (1, 3, 6, 1, 4, 1, 44738, 1, 2),
    _SysADMVersion_Type()
)
sysADMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysADMVersion.setStatus("current")
_SysBiosVersion_Type = OctetString
_SysBiosVersion_Object = MibScalar
sysBiosVersion = _SysBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 44738, 1, 3),
    _SysBiosVersion_Type()
)
sysBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBiosVersion.setStatus("current")
_SysUptime_Type = OctetString
_SysUptime_Object = MibScalar
sysUptime = _SysUptime_Object(
    (1, 3, 6, 1, 4, 1, 44738, 1, 4),
    _SysUptime_Type()
)
sysUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUptime.setStatus("current")
_SyssysTime_Type = OctetString
_SyssysTime_Object = MibScalar
syssysTime = _SyssysTime_Object(
    (1, 3, 6, 1, 4, 1, 44738, 1, 5),
    _SyssysTime_Type()
)
syssysTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syssysTime.setStatus("current")
_SysTimeZone_Type = OctetString
_SysTimeZone_Object = MibScalar
sysTimeZone = _SysTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 44738, 1, 6),
    _SysTimeZone_Type()
)
sysTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTimeZone.setStatus("current")
_SysUpgradeAvailable_Type = OctetString
_SysUpgradeAvailable_Object = MibScalar
sysUpgradeAvailable = _SysUpgradeAvailable_Object(
    (1, 3, 6, 1, 4, 1, 44738, 1, 7),
    _SysUpgradeAvailable_Type()
)
sysUpgradeAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUpgradeAvailable.setStatus("current")
_SysAsustorID_Type = OctetString
_SysAsustorID_Object = MibScalar
sysAsustorID = _SysAsustorID_Object(
    (1, 3, 6, 1, 4, 1, 44738, 1, 8),
    _SysAsustorID_Type()
)
sysAsustorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAsustorID.setStatus("current")
_SystemConformance_ObjectIdentity = ObjectIdentity
systemConformance = _SystemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44738, 1, 11)
)
_SystemCompliances_ObjectIdentity = ObjectIdentity
systemCompliances = _SystemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44738, 1, 11, 1)
)
_SystemGroups_ObjectIdentity = ObjectIdentity
systemGroups = _SystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44738, 1, 11, 2)
)
_AsustorHardware_ObjectIdentity = ObjectIdentity
asustorHardware = _AsustorHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44738, 2)
)
_HwmodelName_Type = OctetString
_HwmodelName_Object = MibScalar
hwmodelName = _HwmodelName_Object(
    (1, 3, 6, 1, 4, 1, 44738, 2, 1),
    _HwmodelName_Type()
)
hwmodelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwmodelName.setStatus("current")
_HwSysTemperature_Type = Integer32
_HwSysTemperature_Object = MibScalar
hwSysTemperature = _HwSysTemperature_Object(
    (1, 3, 6, 1, 4, 1, 44738, 2, 2),
    _HwSysTemperature_Type()
)
hwSysTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysTemperature.setStatus("current")
_HwCPUTemperature_Type = Integer32
_HwCPUTemperature_Object = MibScalar
hwCPUTemperature = _HwCPUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 44738, 2, 3),
    _HwCPUTemperature_Type()
)
hwCPUTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCPUTemperature.setStatus("current")
_HwTotalMem_Type = Integer32
_HwTotalMem_Object = MibScalar
hwTotalMem = _HwTotalMem_Object(
    (1, 3, 6, 1, 4, 1, 44738, 2, 4),
    _HwTotalMem_Type()
)
hwTotalMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalMem.setStatus("current")
_HwFreeMem_Type = Integer32
_HwFreeMem_Object = MibScalar
hwFreeMem = _HwFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 44738, 2, 5),
    _HwFreeMem_Type()
)
hwFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFreeMem.setStatus("current")
_Hwprocessor_Type = OctetString
_Hwprocessor_Object = MibScalar
hwprocessor = _Hwprocessor_Object(
    (1, 3, 6, 1, 4, 1, 44738, 2, 6),
    _Hwprocessor_Type()
)
hwprocessor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwprocessor.setStatus("current")
_HwCPUUsage_ObjectIdentity = ObjectIdentity
hwCPUUsage = _HwCPUUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44738, 2, 7)
)
_CpuTable_Object = MibTable
cpuTable = _CpuTable_Object(
    (1, 3, 6, 1, 4, 1, 44738, 2, 7, 1)
)
if mibBuilder.loadTexts:
    cpuTable.setStatus("current")
_CpuEntry_Object = MibTableRow
cpuEntry = _CpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 44738, 2, 7, 1, 1)
)
cpuEntry.setIndexNames(
    (0, "ASUSTOR-SYSTEM-MIB", "cpuIndex"),
)
if mibBuilder.loadTexts:
    cpuEntry.setStatus("current")


class _CpuIndex_Type(Integer32):
    """Custom type cpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpuIndex_Type.__name__ = "Integer32"
_CpuIndex_Object = MibTableColumn
cpuIndex = _CpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 44738, 2, 7, 1, 1, 1),
    _CpuIndex_Type()
)
cpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpuIndex.setStatus("current")


class _CpuUsage_Type(Integer32):
    """Custom type cpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUsage_Type.__name__ = "Integer32"
_CpuUsage_Object = MibTableColumn
cpuUsage = _CpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 44738, 2, 7, 1, 1, 2),
    _CpuUsage_Type()
)
cpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUsage.setStatus("current")
_HwFanSpeed_ObjectIdentity = ObjectIdentity
hwFanSpeed = _HwFanSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44738, 2, 8)
)
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 44738, 2, 8, 1)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("current")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 44738, 2, 8, 1, 1)
)
fanEntry.setIndexNames(
    (0, "ASUSTOR-SYSTEM-MIB", "fanIndex"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("current")


class _FanIndex_Type(Integer32):
    """Custom type fanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FanIndex_Type.__name__ = "Integer32"
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 44738, 2, 8, 1, 1, 1),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fanIndex.setStatus("current")
_FanSpeed_Type = Integer32
_FanSpeed_Object = MibTableColumn
fanSpeed = _FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 44738, 2, 8, 1, 1, 2),
    _FanSpeed_Type()
)
fanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeed.setStatus("current")
_AsustorNetwork_ObjectIdentity = ObjectIdentity
asustorNetwork = _AsustorNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44738, 3)
)
_NetTable_Object = MibTable
netTable = _NetTable_Object(
    (1, 3, 6, 1, 4, 1, 44738, 3, 1)
)
if mibBuilder.loadTexts:
    netTable.setStatus("current")
_NetEntry_Object = MibTableRow
netEntry = _NetEntry_Object(
    (1, 3, 6, 1, 4, 1, 44738, 3, 1, 1)
)
netEntry.setIndexNames(
    (0, "ASUSTOR-SYSTEM-MIB", "netIndex"),
)
if mibBuilder.loadTexts:
    netEntry.setStatus("current")


class _NetIndex_Type(Integer32):
    """Custom type netIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetIndex_Type.__name__ = "Integer32"
_NetIndex_Object = MibTableColumn
netIndex = _NetIndex_Object(
    (1, 3, 6, 1, 4, 1, 44738, 3, 1, 1, 1),
    _NetIndex_Type()
)
netIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netIndex.setStatus("current")
_NetInterface_Type = OctetString
_NetInterface_Object = MibTableColumn
netInterface = _NetInterface_Object(
    (1, 3, 6, 1, 4, 1, 44738, 3, 1, 1, 2),
    _NetInterface_Type()
)
netInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netInterface.setStatus("current")
_NetMacAddress_Type = PhysAddress
_NetMacAddress_Object = MibTableColumn
netMacAddress = _NetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 44738, 3, 1, 1, 3),
    _NetMacAddress_Type()
)
netMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMacAddress.setStatus("current")
_NetIPv4Address_Type = PhysAddress
_NetIPv4Address_Object = MibTableColumn
netIPv4Address = _NetIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 44738, 3, 1, 1, 4),
    _NetIPv4Address_Type()
)
netIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netIPv4Address.setStatus("current")
_NetIPv6Address_Type = PhysAddress
_NetIPv6Address_Object = MibTableColumn
netIPv6Address = _NetIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 44738, 3, 1, 1, 5),
    _NetIPv6Address_Type()
)
netIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netIPv6Address.setStatus("current")
_NetPacketSent_Type = Integer32
_NetPacketSent_Object = MibTableColumn
netPacketSent = _NetPacketSent_Object(
    (1, 3, 6, 1, 4, 1, 44738, 3, 1, 1, 6),
    _NetPacketSent_Type()
)
netPacketSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketSent.setStatus("current")
_NetPacketReceived_Type = Integer32
_NetPacketReceived_Object = MibTableColumn
netPacketReceived = _NetPacketReceived_Object(
    (1, 3, 6, 1, 4, 1, 44738, 3, 1, 1, 7),
    _NetPacketReceived_Type()
)
netPacketReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketReceived.setStatus("current")

# Managed Objects groups

systemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44738, 1, 11, 2, 1)
)
systemGroup.setObjects(
      *(("ASUSTOR-SYSTEM-MIB", "sysSerialNumber"),
        ("ASUSTOR-SYSTEM-MIB", "sysADMVersion"),
        ("ASUSTOR-SYSTEM-MIB", "sysBiosVersion"),
        ("ASUSTOR-SYSTEM-MIB", "sysUptime"),
        ("ASUSTOR-SYSTEM-MIB", "syssysTime"),
        ("ASUSTOR-SYSTEM-MIB", "sysTimeZone"),
        ("ASUSTOR-SYSTEM-MIB", "sysUpgradeAvailable"),
        ("ASUSTOR-SYSTEM-MIB", "sysAsustorID"),
        ("ASUSTOR-SYSTEM-MIB", "hwmodelName"),
        ("ASUSTOR-SYSTEM-MIB", "hwSysTemperature"),
        ("ASUSTOR-SYSTEM-MIB", "hwCPUTemperature"),
        ("ASUSTOR-SYSTEM-MIB", "hwTotalMem"),
        ("ASUSTOR-SYSTEM-MIB", "hwFreeMem"),
        ("ASUSTOR-SYSTEM-MIB", "hwprocessor"))
)
if mibBuilder.loadTexts:
    systemGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

systemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44738, 1, 11, 1, 1)
)
systemCompliance.setObjects(
    ("ASUSTOR-SYSTEM-MIB", "systemGroup")
)
if mibBuilder.loadTexts:
    systemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASUSTOR-SYSTEM-MIB",
    **{"asustor": asustor,
       "asustorSystem": asustorSystem,
       "sysSerialNumber": sysSerialNumber,
       "sysADMVersion": sysADMVersion,
       "sysBiosVersion": sysBiosVersion,
       "sysUptime": sysUptime,
       "syssysTime": syssysTime,
       "sysTimeZone": sysTimeZone,
       "sysUpgradeAvailable": sysUpgradeAvailable,
       "sysAsustorID": sysAsustorID,
       "systemConformance": systemConformance,
       "systemCompliances": systemCompliances,
       "systemCompliance": systemCompliance,
       "systemGroups": systemGroups,
       "systemGroup": systemGroup,
       "asustorHardware": asustorHardware,
       "hwmodelName": hwmodelName,
       "hwSysTemperature": hwSysTemperature,
       "hwCPUTemperature": hwCPUTemperature,
       "hwTotalMem": hwTotalMem,
       "hwFreeMem": hwFreeMem,
       "hwprocessor": hwprocessor,
       "hwCPUUsage": hwCPUUsage,
       "cpuTable": cpuTable,
       "cpuEntry": cpuEntry,
       "cpuIndex": cpuIndex,
       "cpuUsage": cpuUsage,
       "hwFanSpeed": hwFanSpeed,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanIndex": fanIndex,
       "fanSpeed": fanSpeed,
       "asustorNetwork": asustorNetwork,
       "netTable": netTable,
       "netEntry": netEntry,
       "netIndex": netIndex,
       "netInterface": netInterface,
       "netMacAddress": netMacAddress,
       "netIPv4Address": netIPv4Address,
       "netIPv6Address": netIPv6Address,
       "netPacketSent": netPacketSent,
       "netPacketReceived": netPacketReceived}
)
