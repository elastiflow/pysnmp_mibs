# SNMP MIB module (MF2-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/secui_9560/MF2-SNMP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:59:21 2025
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

(Float,) = mibBuilder.importSymbols(
    "NET-SNMP-TC",
    "Float")

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
 Opaque,
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
    "Opaque",
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

secuidotcom = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9560)
)
if mibBuilder.loadTexts:
    secuidotcom.setRevisions(
        ("2012-04-25 16:00",
         "2011-02-09 18:00",
         "2001-10-05 00:00",
         "2001-05-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1)
)
_Firewall_ObjectIdentity = ObjectIdentity
firewall = _Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1)
)
_Vpn_ObjectIdentity = ObjectIdentity
vpn = _Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 2)
)
_Ips_ObjectIdentity = ObjectIdentity
ips = _Ips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 3)
)
_Waf_ObjectIdentity = ObjectIdentity
waf = _Waf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 4)
)
_Ddos_ObjectIdentity = ObjectIdentity
ddos = _Ddos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 5)
)
_Scan_ObjectIdentity = ObjectIdentity
scan = _Scan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 6)
)
_Utm_ObjectIdentity = ObjectIdentity
utm = _Utm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10)
)
_Snxgu_ObjectIdentity = ObjectIdentity
snxgu = _Snxgu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 1)
)
_Mf2_ObjectIdentity = ObjectIdentity
mf2 = _Mf2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2)
)
_DeviceInfo_ObjectIdentity = ObjectIdentity
deviceInfo = _DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 1)
)
_ModelString_Type = OctetString
_ModelString_Object = MibScalar
modelString = _ModelString_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 1, 1),
    _ModelString_Type()
)
modelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelString.setStatus("current")
_VersionString_Type = OctetString
_VersionString_Object = MibScalar
versionString = _VersionString_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 1, 2),
    _VersionString_Type()
)
versionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionString.setStatus("current")
_IfTableMF2_Object = MibTable
ifTableMF2 = _IfTableMF2_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 2)
)
if mibBuilder.loadTexts:
    ifTableMF2.setStatus("current")
_IfEntryMF2_Object = MibTableRow
ifEntryMF2 = _IfEntryMF2_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 2, 1)
)
ifEntryMF2.setIndexNames(
    (0, "MF2-SNMP-MIB", "mf2IfIndex"),
)
if mibBuilder.loadTexts:
    ifEntryMF2.setStatus("current")


class _Mf2IfIndex_Type(Integer32):
    """Custom type mf2IfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Mf2IfIndex_Type.__name__ = "Integer32"
_Mf2IfIndex_Object = MibTableColumn
mf2IfIndex = _Mf2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 2, 1, 1),
    _Mf2IfIndex_Type()
)
mf2IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mf2IfIndex.setStatus("current")
_Mf2IfName_Type = OctetString
_Mf2IfName_Object = MibTableColumn
mf2IfName = _Mf2IfName_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 2, 1, 2),
    _Mf2IfName_Type()
)
mf2IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mf2IfName.setStatus("current")
_Mf2IfZone_Type = OctetString
_Mf2IfZone_Object = MibTableColumn
mf2IfZone = _Mf2IfZone_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 2, 1, 3),
    _Mf2IfZone_Type()
)
mf2IfZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mf2IfZone.setStatus("current")
_Mf2IfStatus_Type = OctetString
_Mf2IfStatus_Object = MibTableColumn
mf2IfStatus = _Mf2IfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 2, 1, 4),
    _Mf2IfStatus_Type()
)
mf2IfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mf2IfStatus.setStatus("current")
_Mf2IfRXbytes_Type = Counter64
_Mf2IfRXbytes_Object = MibTableColumn
mf2IfRXbytes = _Mf2IfRXbytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 2, 1, 5),
    _Mf2IfRXbytes_Type()
)
mf2IfRXbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mf2IfRXbytes.setStatus("current")
_Mf2IfTXbytes_Type = Counter64
_Mf2IfTXbytes_Object = MibTableColumn
mf2IfTXbytes = _Mf2IfTXbytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 2, 1, 6),
    _Mf2IfTXbytes_Type()
)
mf2IfTXbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mf2IfTXbytes.setStatus("current")
_Resources_ObjectIdentity = ObjectIdentity
resources = _Resources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3)
)
_CpuUsageTable_Object = MibTable
cpuUsageTable = _CpuUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cpuUsageTable.setStatus("current")
_CpuUsageEntry_Object = MibTableRow
cpuUsageEntry = _CpuUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 1, 1)
)
cpuUsageEntry.setIndexNames(
    (0, "MF2-SNMP-MIB", "cpuID"),
)
if mibBuilder.loadTexts:
    cpuUsageEntry.setStatus("current")
_CpuID_Type = Integer32
_CpuID_Object = MibTableColumn
cpuID = _CpuID_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 1, 1, 1),
    _CpuID_Type()
)
cpuID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuID.setStatus("current")
_TotalTick_Type = Integer32
_TotalTick_Object = MibTableColumn
totalTick = _TotalTick_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 1, 1, 2),
    _TotalTick_Type()
)
totalTick.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalTick.setStatus("current")
_KernelTick_Type = Integer32
_KernelTick_Object = MibTableColumn
kernelTick = _KernelTick_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 1, 1, 3),
    _KernelTick_Type()
)
kernelTick.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kernelTick.setStatus("current")
_UserTick_Type = Integer32
_UserTick_Object = MibTableColumn
userTick = _UserTick_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 1, 1, 4),
    _UserTick_Type()
)
userTick.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userTick.setStatus("current")
_IdleTick_Type = Integer32
_IdleTick_Object = MibTableColumn
idleTick = _IdleTick_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 1, 1, 5),
    _IdleTick_Type()
)
idleTick.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idleTick.setStatus("current")
_UsageByMonitor_Type = Float
_UsageByMonitor_Object = MibTableColumn
usageByMonitor = _UsageByMonitor_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 1, 1, 6),
    _UsageByMonitor_Type()
)
usageByMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageByMonitor.setStatus("current")
_MemUsage_ObjectIdentity = ObjectIdentity
memUsage = _MemUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 2)
)
_MemTotal_Type = Counter64
_MemTotal_Object = MibScalar
memTotal = _MemTotal_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 2, 1),
    _MemTotal_Type()
)
memTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotal.setStatus("current")
_MemUsed_Type = Counter64
_MemUsed_Object = MibScalar
memUsed = _MemUsed_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 2, 2),
    _MemUsed_Type()
)
memUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUsed.setStatus("current")
_MemFree_Type = Counter64
_MemFree_Object = MibScalar
memFree = _MemFree_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 2, 3),
    _MemFree_Type()
)
memFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memFree.setStatus("current")
_MemUsageByMonitor_Type = Integer32
_MemUsageByMonitor_Object = MibScalar
memUsageByMonitor = _MemUsageByMonitor_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 2, 4),
    _MemUsageByMonitor_Type()
)
memUsageByMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUsageByMonitor.setStatus("current")
_DiskUsage_ObjectIdentity = ObjectIdentity
diskUsage = _DiskUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 3)
)
_DiskBlockSize_Type = Counter64
_DiskBlockSize_Object = MibScalar
diskBlockSize = _DiskBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 3, 1),
    _DiskBlockSize_Type()
)
diskBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskBlockSize.setStatus("current")
_DiskTotalBlocks_Type = Counter64
_DiskTotalBlocks_Object = MibScalar
diskTotalBlocks = _DiskTotalBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 3, 2),
    _DiskTotalBlocks_Type()
)
diskTotalBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTotalBlocks.setStatus("current")
_DiskUsedBlocks_Type = Counter64
_DiskUsedBlocks_Object = MibScalar
diskUsedBlocks = _DiskUsedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 3, 3),
    _DiskUsedBlocks_Type()
)
diskUsedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskUsedBlocks.setStatus("current")
_DiskFreeBlocks_Type = Counter64
_DiskFreeBlocks_Object = MibScalar
diskFreeBlocks = _DiskFreeBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 3, 4),
    _DiskFreeBlocks_Type()
)
diskFreeBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskFreeBlocks.setStatus("current")
_DiskReservedBlocks_Type = Counter64
_DiskReservedBlocks_Object = MibScalar
diskReservedBlocks = _DiskReservedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 3, 5),
    _DiskReservedBlocks_Type()
)
diskReservedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskReservedBlocks.setStatus("current")
_DiskUsageByMonitor_Type = Integer32
_DiskUsageByMonitor_Object = MibScalar
diskUsageByMonitor = _DiskUsageByMonitor_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 3, 3, 6),
    _DiskUsageByMonitor_Type()
)
diskUsageByMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskUsageByMonitor.setStatus("current")
_FwTraffics_ObjectIdentity = ObjectIdentity
fwTraffics = _FwTraffics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4)
)
_TotalInputPackets_Type = Counter64
_TotalInputPackets_Object = MibScalar
totalInputPackets = _TotalInputPackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 1),
    _TotalInputPackets_Type()
)
totalInputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalInputPackets.setStatus("current")
_TotalInputBytes_Type = Counter64
_TotalInputBytes_Object = MibScalar
totalInputBytes = _TotalInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 2),
    _TotalInputBytes_Type()
)
totalInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalInputBytes.setStatus("current")
_InboundInputPackets_Type = Counter64
_InboundInputPackets_Object = MibScalar
inboundInputPackets = _InboundInputPackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 3),
    _InboundInputPackets_Type()
)
inboundInputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundInputPackets.setStatus("current")
_InboundInputBytes_Type = Counter64
_InboundInputBytes_Object = MibScalar
inboundInputBytes = _InboundInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 4),
    _InboundInputBytes_Type()
)
inboundInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundInputBytes.setStatus("current")
_OutboundInputPackets_Type = Counter64
_OutboundInputPackets_Object = MibScalar
outboundInputPackets = _OutboundInputPackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 5),
    _OutboundInputPackets_Type()
)
outboundInputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundInputPackets.setStatus("current")
_OutboundInputBytes_Type = Counter64
_OutboundInputBytes_Object = MibScalar
outboundInputBytes = _OutboundInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 6),
    _OutboundInputBytes_Type()
)
outboundInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundInputBytes.setStatus("current")
_TotalAllowPackets_Type = Counter64
_TotalAllowPackets_Object = MibScalar
totalAllowPackets = _TotalAllowPackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 7),
    _TotalAllowPackets_Type()
)
totalAllowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalAllowPackets.setStatus("current")
_TotalAllowBytes_Type = Counter64
_TotalAllowBytes_Object = MibScalar
totalAllowBytes = _TotalAllowBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 8),
    _TotalAllowBytes_Type()
)
totalAllowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalAllowBytes.setStatus("current")
_InboundAllowPackets_Type = Counter64
_InboundAllowPackets_Object = MibScalar
inboundAllowPackets = _InboundAllowPackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 9),
    _InboundAllowPackets_Type()
)
inboundAllowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundAllowPackets.setStatus("current")
_InboundAllowBytes_Type = Counter64
_InboundAllowBytes_Object = MibScalar
inboundAllowBytes = _InboundAllowBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 10),
    _InboundAllowBytes_Type()
)
inboundAllowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundAllowBytes.setStatus("current")
_OutboundAllowPackets_Type = Counter64
_OutboundAllowPackets_Object = MibScalar
outboundAllowPackets = _OutboundAllowPackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 11),
    _OutboundAllowPackets_Type()
)
outboundAllowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundAllowPackets.setStatus("current")
_OutboundAllowBytes_Type = Counter64
_OutboundAllowBytes_Object = MibScalar
outboundAllowBytes = _OutboundAllowBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 12),
    _OutboundAllowBytes_Type()
)
outboundAllowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundAllowBytes.setStatus("current")
_TotalDenyPackets_Type = Counter64
_TotalDenyPackets_Object = MibScalar
totalDenyPackets = _TotalDenyPackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 13),
    _TotalDenyPackets_Type()
)
totalDenyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalDenyPackets.setStatus("current")
_TotalDenyBytes_Type = Counter64
_TotalDenyBytes_Object = MibScalar
totalDenyBytes = _TotalDenyBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 14),
    _TotalDenyBytes_Type()
)
totalDenyBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalDenyBytes.setStatus("current")
_InboundDenyPackets_Type = Counter64
_InboundDenyPackets_Object = MibScalar
inboundDenyPackets = _InboundDenyPackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 15),
    _InboundDenyPackets_Type()
)
inboundDenyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundDenyPackets.setStatus("current")
_InboundDenyBytes_Type = Counter64
_InboundDenyBytes_Object = MibScalar
inboundDenyBytes = _InboundDenyBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 16),
    _InboundDenyBytes_Type()
)
inboundDenyBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundDenyBytes.setStatus("current")
_OutboundDenyPackets_Type = Counter64
_OutboundDenyPackets_Object = MibScalar
outboundDenyPackets = _OutboundDenyPackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 17),
    _OutboundDenyPackets_Type()
)
outboundDenyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundDenyPackets.setStatus("current")
_OutboundDenyBytes_Type = Counter64
_OutboundDenyBytes_Object = MibScalar
outboundDenyBytes = _OutboundDenyBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 18),
    _OutboundDenyBytes_Type()
)
outboundDenyBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundDenyBytes.setStatus("current")
_TotalTCPPackets_Type = Counter64
_TotalTCPPackets_Object = MibScalar
totalTCPPackets = _TotalTCPPackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 19),
    _TotalTCPPackets_Type()
)
totalTCPPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalTCPPackets.setStatus("current")
_TotalTCPBytes_Type = Counter64
_TotalTCPBytes_Object = MibScalar
totalTCPBytes = _TotalTCPBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 20),
    _TotalTCPBytes_Type()
)
totalTCPBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalTCPBytes.setStatus("current")
_InboundTCPPackets_Type = Counter64
_InboundTCPPackets_Object = MibScalar
inboundTCPPackets = _InboundTCPPackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 21),
    _InboundTCPPackets_Type()
)
inboundTCPPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundTCPPackets.setStatus("current")
_InboundTCPBytes_Type = Counter64
_InboundTCPBytes_Object = MibScalar
inboundTCPBytes = _InboundTCPBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 22),
    _InboundTCPBytes_Type()
)
inboundTCPBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundTCPBytes.setStatus("current")
_OutboundTCPPackets_Type = Counter64
_OutboundTCPPackets_Object = MibScalar
outboundTCPPackets = _OutboundTCPPackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 23),
    _OutboundTCPPackets_Type()
)
outboundTCPPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundTCPPackets.setStatus("current")
_OutboundTCPBytes_Type = Counter64
_OutboundTCPBytes_Object = MibScalar
outboundTCPBytes = _OutboundTCPBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 24),
    _OutboundTCPBytes_Type()
)
outboundTCPBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundTCPBytes.setStatus("current")
_TotalUDPPackets_Type = Counter64
_TotalUDPPackets_Object = MibScalar
totalUDPPackets = _TotalUDPPackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 25),
    _TotalUDPPackets_Type()
)
totalUDPPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalUDPPackets.setStatus("current")
_TotalUDPBytes_Type = Counter64
_TotalUDPBytes_Object = MibScalar
totalUDPBytes = _TotalUDPBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 26),
    _TotalUDPBytes_Type()
)
totalUDPBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalUDPBytes.setStatus("current")
_InboundUDPPackets_Type = Counter64
_InboundUDPPackets_Object = MibScalar
inboundUDPPackets = _InboundUDPPackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 27),
    _InboundUDPPackets_Type()
)
inboundUDPPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundUDPPackets.setStatus("current")
_InboundUDPBytes_Type = Counter64
_InboundUDPBytes_Object = MibScalar
inboundUDPBytes = _InboundUDPBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 28),
    _InboundUDPBytes_Type()
)
inboundUDPBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundUDPBytes.setStatus("current")
_OutboundUDPPackets_Type = Counter64
_OutboundUDPPackets_Object = MibScalar
outboundUDPPackets = _OutboundUDPPackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 29),
    _OutboundUDPPackets_Type()
)
outboundUDPPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundUDPPackets.setStatus("current")
_OutboundUDPBytes_Type = Counter64
_OutboundUDPBytes_Object = MibScalar
outboundUDPBytes = _OutboundUDPBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 30),
    _OutboundUDPBytes_Type()
)
outboundUDPBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundUDPBytes.setStatus("current")
_TotalICMPPackets_Type = Counter64
_TotalICMPPackets_Object = MibScalar
totalICMPPackets = _TotalICMPPackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 31),
    _TotalICMPPackets_Type()
)
totalICMPPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalICMPPackets.setStatus("current")
_TotalICMPBytes_Type = Counter64
_TotalICMPBytes_Object = MibScalar
totalICMPBytes = _TotalICMPBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 32),
    _TotalICMPBytes_Type()
)
totalICMPBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalICMPBytes.setStatus("current")
_InboundICMPPackets_Type = Counter64
_InboundICMPPackets_Object = MibScalar
inboundICMPPackets = _InboundICMPPackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 33),
    _InboundICMPPackets_Type()
)
inboundICMPPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundICMPPackets.setStatus("current")
_InboundICMPBytes_Type = Counter64
_InboundICMPBytes_Object = MibScalar
inboundICMPBytes = _InboundICMPBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 34),
    _InboundICMPBytes_Type()
)
inboundICMPBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundICMPBytes.setStatus("current")
_OutboundICMPPackets_Type = Counter64
_OutboundICMPPackets_Object = MibScalar
outboundICMPPackets = _OutboundICMPPackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 35),
    _OutboundICMPPackets_Type()
)
outboundICMPPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundICMPPackets.setStatus("current")
_OutboundICMPBytes_Type = Counter64
_OutboundICMPBytes_Object = MibScalar
outboundICMPBytes = _OutboundICMPBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 4, 36),
    _OutboundICMPBytes_Type()
)
outboundICMPBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundICMPBytes.setStatus("current")
_Mf2FWruleTable_Object = MibTable
mf2FWruleTable = _Mf2FWruleTable_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 5)
)
if mibBuilder.loadTexts:
    mf2FWruleTable.setStatus("current")
_Mf2FWruleEntry_Object = MibTableRow
mf2FWruleEntry = _Mf2FWruleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 5, 1)
)
mf2FWruleEntry.setIndexNames(
    (0, "MF2-SNMP-MIB", "mf2FWruleIndex"),
)
if mibBuilder.loadTexts:
    mf2FWruleEntry.setStatus("current")
_Mf2FWruleIndex_Type = Integer32
_Mf2FWruleIndex_Object = MibTableColumn
mf2FWruleIndex = _Mf2FWruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 5, 1, 1),
    _Mf2FWruleIndex_Type()
)
mf2FWruleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mf2FWruleIndex.setStatus("current")
_Mf2FWruleID_Type = Integer32
_Mf2FWruleID_Object = MibTableColumn
mf2FWruleID = _Mf2FWruleID_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 5, 1, 2),
    _Mf2FWruleID_Type()
)
mf2FWruleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mf2FWruleID.setStatus("current")
_Mf2FWruleSequence_Type = Integer32
_Mf2FWruleSequence_Object = MibTableColumn
mf2FWruleSequence = _Mf2FWruleSequence_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 5, 1, 3),
    _Mf2FWruleSequence_Type()
)
mf2FWruleSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mf2FWruleSequence.setStatus("current")
_Mf2FWruleAccumulatePackets_Type = Counter64
_Mf2FWruleAccumulatePackets_Object = MibTableColumn
mf2FWruleAccumulatePackets = _Mf2FWruleAccumulatePackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 5, 1, 4),
    _Mf2FWruleAccumulatePackets_Type()
)
mf2FWruleAccumulatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mf2FWruleAccumulatePackets.setStatus("current")
_Mf2FWruleAccumulateBytes_Type = Counter64
_Mf2FWruleAccumulateBytes_Object = MibTableColumn
mf2FWruleAccumulateBytes = _Mf2FWruleAccumulateBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 5, 1, 5),
    _Mf2FWruleAccumulateBytes_Type()
)
mf2FWruleAccumulateBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mf2FWruleAccumulateBytes.setStatus("current")
_Mf2FWruleCurrentSessions_Type = Gauge32
_Mf2FWruleCurrentSessions_Object = MibTableColumn
mf2FWruleCurrentSessions = _Mf2FWruleCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 5, 1, 6),
    _Mf2FWruleCurrentSessions_Type()
)
mf2FWruleCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mf2FWruleCurrentSessions.setStatus("current")
_Mf2FWruleAccumulateSessions_Type = Counter64
_Mf2FWruleAccumulateSessions_Object = MibTableColumn
mf2FWruleAccumulateSessions = _Mf2FWruleAccumulateSessions_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 5, 1, 7),
    _Mf2FWruleAccumulateSessions_Type()
)
mf2FWruleAccumulateSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mf2FWruleAccumulateSessions.setStatus("current")
_Mf2FWruleAccumulateHits_Type = Counter64
_Mf2FWruleAccumulateHits_Object = MibTableColumn
mf2FWruleAccumulateHits = _Mf2FWruleAccumulateHits_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 5, 1, 8),
    _Mf2FWruleAccumulateHits_Type()
)
mf2FWruleAccumulateHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mf2FWruleAccumulateHits.setStatus("current")
_Mf2FWruleLastHit_Type = OctetString
_Mf2FWruleLastHit_Object = MibTableColumn
mf2FWruleLastHit = _Mf2FWruleLastHit_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 5, 1, 9),
    _Mf2FWruleLastHit_Type()
)
mf2FWruleLastHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mf2FWruleLastHit.setStatus("current")
_Mf2FWruleAction_Type = OctetString
_Mf2FWruleAction_Object = MibTableColumn
mf2FWruleAction = _Mf2FWruleAction_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 5, 1, 10),
    _Mf2FWruleAction_Type()
)
mf2FWruleAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mf2FWruleAction.setStatus("current")
_WebFilter_ObjectIdentity = ObjectIdentity
webFilter = _WebFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 32)
)


class _EnableAnonymizer_Type(Integer32):
    """Custom type enableAnonymizer based on Integer32"""
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


_EnableAnonymizer_Type.__name__ = "Integer32"
_EnableAnonymizer_Object = MibScalar
enableAnonymizer = _EnableAnonymizer_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 32, 1),
    _EnableAnonymizer_Type()
)
enableAnonymizer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableAnonymizer.setStatus("current")
_LogCount_Type = Integer32
_LogCount_Object = MibScalar
logCount = _LogCount_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 32, 2),
    _LogCount_Type()
)
logCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logCount.setStatus("current")
_LogTimeout_Type = Integer32
_LogTimeout_Object = MibScalar
logTimeout = _LogTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 32, 3),
    _LogTimeout_Type()
)
logTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logTimeout.setStatus("current")


class _DoUpdateDB_Type(Integer32):
    """Custom type doUpdateDB based on Integer32"""
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


_DoUpdateDB_Type.__name__ = "Integer32"
_DoUpdateDB_Object = MibScalar
doUpdateDB = _DoUpdateDB_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 32, 4),
    _DoUpdateDB_Type()
)
doUpdateDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doUpdateDB.setStatus("current")
_UpdateHost_Type = OctetString
_UpdateHost_Object = MibScalar
updateHost = _UpdateHost_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 32, 5),
    _UpdateHost_Type()
)
updateHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    updateHost.setStatus("current")
_UpdatePath_Type = OctetString
_UpdatePath_Object = MibScalar
updatePath = _UpdatePath_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 32, 6),
    _UpdatePath_Type()
)
updatePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    updatePath.setStatus("current")
_UpdateID_Type = OctetString
_UpdateID_Object = MibScalar
updateID = _UpdateID_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 32, 7),
    _UpdateID_Type()
)
updateID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    updateID.setStatus("current")
_UpdatePasswd_Type = OctetString
_UpdatePasswd_Object = MibScalar
updatePasswd = _UpdatePasswd_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 32, 8),
    _UpdatePasswd_Type()
)
updatePasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    updatePasswd.setStatus("current")
_BlockDBVersion_Type = OctetString
_BlockDBVersion_Object = MibScalar
blockDBVersion = _BlockDBVersion_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 32, 9),
    _BlockDBVersion_Type()
)
blockDBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockDBVersion.setStatus("current")
_BlockDBCount_Type = Integer32
_BlockDBCount_Object = MibScalar
blockDBCount = _BlockDBCount_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 32, 10),
    _BlockDBCount_Type()
)
blockDBCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockDBCount.setStatus("current")
_ExceptDBVersion_Type = OctetString
_ExceptDBVersion_Object = MibScalar
exceptDBVersion = _ExceptDBVersion_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 32, 11),
    _ExceptDBVersion_Type()
)
exceptDBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exceptDBVersion.setStatus("current")
_ExceptDBCount_Type = Integer32
_ExceptDBCount_Object = MibScalar
exceptDBCount = _ExceptDBCount_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 32, 12),
    _ExceptDBCount_Type()
)
exceptDBCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exceptDBCount.setStatus("current")
_AnonymizerDBVersion_Type = OctetString
_AnonymizerDBVersion_Object = MibScalar
anonymizerDBVersion = _AnonymizerDBVersion_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 32, 13),
    _AnonymizerDBVersion_Type()
)
anonymizerDBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anonymizerDBVersion.setStatus("current")
_AnonymizerDBCount_Type = Integer32
_AnonymizerDBCount_Object = MibScalar
anonymizerDBCount = _AnonymizerDBCount_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 32, 14),
    _AnonymizerDBCount_Type()
)
anonymizerDBCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anonymizerDBCount.setStatus("current")
_WebfilterResetMethod_Type = OctetString
_WebfilterResetMethod_Object = MibScalar
webfilterResetMethod = _WebfilterResetMethod_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 32, 15),
    _WebfilterResetMethod_Type()
)
webfilterResetMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webfilterResetMethod.setStatus("current")
_WebfilterResetRedirect_Type = OctetString
_WebfilterResetRedirect_Object = MibScalar
webfilterResetRedirect = _WebfilterResetRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 32, 16),
    _WebfilterResetRedirect_Type()
)
webfilterResetRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webfilterResetRedirect.setStatus("current")
_Mf2Traps_ObjectIdentity = ObjectIdentity
mf2Traps = _Mf2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 128)
)

# Managed Objects groups


# Notification objects

mf2Start = NotificationType(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 128, 1)
)
if mibBuilder.loadTexts:
    mf2Start.setStatus(
        "current"
    )

mf2Shutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 128, 2)
)
if mibBuilder.loadTexts:
    mf2Shutdown.setStatus(
        "current"
    )

mf2Alert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9560, 1, 10, 2, 128, 3)
)
if mibBuilder.loadTexts:
    mf2Alert.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MF2-SNMP-MIB",
    **{"secuidotcom": secuidotcom,
       "products": products,
       "firewall": firewall,
       "vpn": vpn,
       "ips": ips,
       "waf": waf,
       "ddos": ddos,
       "scan": scan,
       "utm": utm,
       "snxgu": snxgu,
       "mf2": mf2,
       "deviceInfo": deviceInfo,
       "modelString": modelString,
       "versionString": versionString,
       "ifTableMF2": ifTableMF2,
       "ifEntryMF2": ifEntryMF2,
       "mf2IfIndex": mf2IfIndex,
       "mf2IfName": mf2IfName,
       "mf2IfZone": mf2IfZone,
       "mf2IfStatus": mf2IfStatus,
       "mf2IfRXbytes": mf2IfRXbytes,
       "mf2IfTXbytes": mf2IfTXbytes,
       "resources": resources,
       "cpuUsageTable": cpuUsageTable,
       "cpuUsageEntry": cpuUsageEntry,
       "cpuID": cpuID,
       "totalTick": totalTick,
       "kernelTick": kernelTick,
       "userTick": userTick,
       "idleTick": idleTick,
       "usageByMonitor": usageByMonitor,
       "memUsage": memUsage,
       "memTotal": memTotal,
       "memUsed": memUsed,
       "memFree": memFree,
       "memUsageByMonitor": memUsageByMonitor,
       "diskUsage": diskUsage,
       "diskBlockSize": diskBlockSize,
       "diskTotalBlocks": diskTotalBlocks,
       "diskUsedBlocks": diskUsedBlocks,
       "diskFreeBlocks": diskFreeBlocks,
       "diskReservedBlocks": diskReservedBlocks,
       "diskUsageByMonitor": diskUsageByMonitor,
       "fwTraffics": fwTraffics,
       "totalInputPackets": totalInputPackets,
       "totalInputBytes": totalInputBytes,
       "inboundInputPackets": inboundInputPackets,
       "inboundInputBytes": inboundInputBytes,
       "outboundInputPackets": outboundInputPackets,
       "outboundInputBytes": outboundInputBytes,
       "totalAllowPackets": totalAllowPackets,
       "totalAllowBytes": totalAllowBytes,
       "inboundAllowPackets": inboundAllowPackets,
       "inboundAllowBytes": inboundAllowBytes,
       "outboundAllowPackets": outboundAllowPackets,
       "outboundAllowBytes": outboundAllowBytes,
       "totalDenyPackets": totalDenyPackets,
       "totalDenyBytes": totalDenyBytes,
       "inboundDenyPackets": inboundDenyPackets,
       "inboundDenyBytes": inboundDenyBytes,
       "outboundDenyPackets": outboundDenyPackets,
       "outboundDenyBytes": outboundDenyBytes,
       "totalTCPPackets": totalTCPPackets,
       "totalTCPBytes": totalTCPBytes,
       "inboundTCPPackets": inboundTCPPackets,
       "inboundTCPBytes": inboundTCPBytes,
       "outboundTCPPackets": outboundTCPPackets,
       "outboundTCPBytes": outboundTCPBytes,
       "totalUDPPackets": totalUDPPackets,
       "totalUDPBytes": totalUDPBytes,
       "inboundUDPPackets": inboundUDPPackets,
       "inboundUDPBytes": inboundUDPBytes,
       "outboundUDPPackets": outboundUDPPackets,
       "outboundUDPBytes": outboundUDPBytes,
       "totalICMPPackets": totalICMPPackets,
       "totalICMPBytes": totalICMPBytes,
       "inboundICMPPackets": inboundICMPPackets,
       "inboundICMPBytes": inboundICMPBytes,
       "outboundICMPPackets": outboundICMPPackets,
       "outboundICMPBytes": outboundICMPBytes,
       "mf2FWruleTable": mf2FWruleTable,
       "mf2FWruleEntry": mf2FWruleEntry,
       "mf2FWruleIndex": mf2FWruleIndex,
       "mf2FWruleID": mf2FWruleID,
       "mf2FWruleSequence": mf2FWruleSequence,
       "mf2FWruleAccumulatePackets": mf2FWruleAccumulatePackets,
       "mf2FWruleAccumulateBytes": mf2FWruleAccumulateBytes,
       "mf2FWruleCurrentSessions": mf2FWruleCurrentSessions,
       "mf2FWruleAccumulateSessions": mf2FWruleAccumulateSessions,
       "mf2FWruleAccumulateHits": mf2FWruleAccumulateHits,
       "mf2FWruleLastHit": mf2FWruleLastHit,
       "mf2FWruleAction": mf2FWruleAction,
       "webFilter": webFilter,
       "enableAnonymizer": enableAnonymizer,
       "logCount": logCount,
       "logTimeout": logTimeout,
       "doUpdateDB": doUpdateDB,
       "updateHost": updateHost,
       "updatePath": updatePath,
       "updateID": updateID,
       "updatePasswd": updatePasswd,
       "blockDBVersion": blockDBVersion,
       "blockDBCount": blockDBCount,
       "exceptDBVersion": exceptDBVersion,
       "exceptDBCount": exceptDBCount,
       "anonymizerDBVersion": anonymizerDBVersion,
       "anonymizerDBCount": anonymizerDBCount,
       "webfilterResetMethod": webfilterResetMethod,
       "webfilterResetRedirect": webfilterResetRedirect,
       "mf2Traps": mf2Traps,
       "mf2Start": mf2Start,
       "mf2Shutdown": mf2Shutdown,
       "mf2Alert": mf2Alert}
)
