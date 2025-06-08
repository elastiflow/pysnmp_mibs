# SNMP MIB module (Barracuda-SPYWARE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/barracuda_20632/Barracuda-SPYWARE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:37:18 2025
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

(barracuda,) = mibBuilder.importSymbols(
    "Barracuda-REF",
    "barracuda")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

bspyware = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ActiveTCPConnections_Type = Integer32
_ActiveTCPConnections_Object = MibScalar
activeTCPConnections = _ActiveTCPConnections_Object(
    (1, 3, 6, 1, 4, 1, 20632, 3, 2),
    _ActiveTCPConnections_Type()
)
activeTCPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeTCPConnections.setStatus("current")
_Bspywaretraps_ObjectIdentity = ObjectIdentity
bspywaretraps = _Bspywaretraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 3, 2)
)
_Throughput_Type = Integer32
_Throughput_Object = MibScalar
throughput = _Throughput_Object(
    (1, 3, 6, 1, 4, 1, 20632, 3, 3),
    _Throughput_Type()
)
throughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    throughput.setStatus("current")
_PolicyBlocks_Type = Integer32
_PolicyBlocks_Object = MibScalar
policyBlocks = _PolicyBlocks_Object(
    (1, 3, 6, 1, 4, 1, 20632, 3, 4),
    _PolicyBlocks_Type()
)
policyBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyBlocks.setStatus("current")
_SpywareWebHitBlocks_Type = Integer32
_SpywareWebHitBlocks_Object = MibScalar
spywareWebHitBlocks = _SpywareWebHitBlocks_Object(
    (1, 3, 6, 1, 4, 1, 20632, 3, 5),
    _SpywareWebHitBlocks_Type()
)
spywareWebHitBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spywareWebHitBlocks.setStatus("current")
_SpywareDownloadBlock_Type = Integer32
_SpywareDownloadBlock_Object = MibScalar
spywareDownloadBlock = _SpywareDownloadBlock_Object(
    (1, 3, 6, 1, 4, 1, 20632, 3, 6),
    _SpywareDownloadBlock_Type()
)
spywareDownloadBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spywareDownloadBlock.setStatus("current")
_VirusDownloadBlock_Type = Integer32
_VirusDownloadBlock_Object = MibScalar
virusDownloadBlock = _VirusDownloadBlock_Object(
    (1, 3, 6, 1, 4, 1, 20632, 3, 7),
    _VirusDownloadBlock_Type()
)
virusDownloadBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virusDownloadBlock.setStatus("current")
_SpywareProtocolBlock_Type = Integer32
_SpywareProtocolBlock_Object = MibScalar
spywareProtocolBlock = _SpywareProtocolBlock_Object(
    (1, 3, 6, 1, 4, 1, 20632, 3, 8),
    _SpywareProtocolBlock_Type()
)
spywareProtocolBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spywareProtocolBlock.setStatus("current")
_HttpTrafficAllowed_Type = Integer32
_HttpTrafficAllowed_Object = MibScalar
httpTrafficAllowed = _HttpTrafficAllowed_Object(
    (1, 3, 6, 1, 4, 1, 20632, 3, 9),
    _HttpTrafficAllowed_Type()
)
httpTrafficAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTrafficAllowed.setStatus("current")
_CpuFanSpeed_Type = Integer32
_CpuFanSpeed_Object = MibScalar
cpuFanSpeed = _CpuFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 20632, 3, 10, 1),
    _CpuFanSpeed_Type()
)
cpuFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFanSpeed.setStatus("current")
_SystemFanSpeed_Type = Integer32
_SystemFanSpeed_Object = MibScalar
systemFanSpeed = _SystemFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 20632, 3, 10, 2),
    _SystemFanSpeed_Type()
)
systemFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFanSpeed.setStatus("current")
_CpuTemperature_Type = Integer32
_CpuTemperature_Object = MibScalar
cpuTemperature = _CpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 20632, 3, 10, 3),
    _CpuTemperature_Type()
)
cpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTemperature.setStatus("current")
_SystemTemperature_Type = Integer32
_SystemTemperature_Object = MibScalar
systemTemperature = _SystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 20632, 3, 10, 4),
    _SystemTemperature_Type()
)
systemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTemperature.setStatus("current")
_FirmwareStorage_Type = Integer32
_FirmwareStorage_Object = MibScalar
firmwareStorage = _FirmwareStorage_Object(
    (1, 3, 6, 1, 4, 1, 20632, 3, 10, 5),
    _FirmwareStorage_Type()
)
firmwareStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareStorage.setStatus("current")
_LogStorage_Type = Integer32
_LogStorage_Object = MibScalar
logStorage = _LogStorage_Object(
    (1, 3, 6, 1, 4, 1, 20632, 3, 10, 6),
    _LogStorage_Type()
)
logStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logStorage.setStatus("current")
_SystemUpTime_Type = Integer32
_SystemUpTime_Object = MibScalar
systemUpTime = _SystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 20632, 3, 11),
    _SystemUpTime_Type()
)
systemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpTime.setStatus("current")

# Managed Objects groups

system = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20632, 3, 10)
)
system.setObjects(
      *(("Barracuda-SPYWARE", "cpuFanSpeed"),
        ("Barracuda-SPYWARE", "systemFanSpeed"),
        ("Barracuda-SPYWARE", "cpuTemperature"),
        ("Barracuda-SPYWARE", "systemTemperature"),
        ("Barracuda-SPYWARE", "logStorage"),
        ("Barracuda-SPYWARE", "firmwareStorage"))
)
if mibBuilder.loadTexts:
    system.setStatus("current")


# Notification objects

activeTCPConnectionsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 3, 2, 2)
)
if mibBuilder.loadTexts:
    activeTCPConnectionsHigh.setStatus(
        "current"
    )

throughputHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 3, 2, 3)
)
if mibBuilder.loadTexts:
    throughputHigh.setStatus(
        "current"
    )

cpuTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 3, 2, 4)
)
if mibBuilder.loadTexts:
    cpuTempHigh.setStatus(
        "current"
    )

sysTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 3, 2, 5)
)
if mibBuilder.loadTexts:
    sysTempHigh.setStatus(
        "current"
    )

cpuFanDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 3, 2, 6)
)
if mibBuilder.loadTexts:
    cpuFanDead.setStatus(
        "current"
    )

sysFanDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 3, 2, 7)
)
if mibBuilder.loadTexts:
    sysFanDead.setStatus(
        "current"
    )

firmwareStorageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 3, 2, 8)
)
if mibBuilder.loadTexts:
    firmwareStorageHigh.setStatus(
        "current"
    )

logStorageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 3, 2, 9)
)
if mibBuilder.loadTexts:
    logStorageHigh.setStatus(
        "current"
    )

lanStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 3, 2, 10)
)
if mibBuilder.loadTexts:
    lanStatus.setStatus(
        "current"
    )

wanStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 3, 2, 11)
)
if mibBuilder.loadTexts:
    wanStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Barracuda-SPYWARE",
    **{"bspyware": bspyware,
       "activeTCPConnections": activeTCPConnections,
       "bspywaretraps": bspywaretraps,
       "activeTCPConnectionsHigh": activeTCPConnectionsHigh,
       "throughputHigh": throughputHigh,
       "cpuTempHigh": cpuTempHigh,
       "sysTempHigh": sysTempHigh,
       "cpuFanDead": cpuFanDead,
       "sysFanDead": sysFanDead,
       "firmwareStorageHigh": firmwareStorageHigh,
       "logStorageHigh": logStorageHigh,
       "lanStatus": lanStatus,
       "wanStatus": wanStatus,
       "throughput": throughput,
       "policyBlocks": policyBlocks,
       "spywareWebHitBlocks": spywareWebHitBlocks,
       "spywareDownloadBlock": spywareDownloadBlock,
       "virusDownloadBlock": virusDownloadBlock,
       "spywareProtocolBlock": spywareProtocolBlock,
       "httpTrafficAllowed": httpTrafficAllowed,
       "system": system,
       "cpuFanSpeed": cpuFanSpeed,
       "systemFanSpeed": systemFanSpeed,
       "cpuTemperature": cpuTemperature,
       "systemTemperature": systemTemperature,
       "firmwareStorage": firmwareStorage,
       "logStorage": logStorage,
       "systemUpTime": systemUpTime}
)
