# SNMP MIB module (Barracuda-LB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/barracuda_20632/Barracuda-LB.mib
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

blb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Blbtraps_ObjectIdentity = ObjectIdentity
blbtraps = _Blbtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 5, 1)
)
_SystemActiveServices_Type = Integer32
_SystemActiveServices_Object = MibScalar
systemActiveServices = _SystemActiveServices_Object(
    (1, 3, 6, 1, 4, 1, 20632, 5, 2),
    _SystemActiveServices_Type()
)
systemActiveServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemActiveServices.setStatus("current")
_SystemOperatingServers_Type = Integer32
_SystemOperatingServers_Object = MibScalar
systemOperatingServers = _SystemOperatingServers_Object(
    (1, 3, 6, 1, 4, 1, 20632, 5, 3),
    _SystemOperatingServers_Type()
)
systemOperatingServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemOperatingServers.setStatus("current")
_L4TCPConnections_Type = Integer32
_L4TCPConnections_Object = MibScalar
l4TCPConnections = _L4TCPConnections_Object(
    (1, 3, 6, 1, 4, 1, 20632, 5, 6),
    _L4TCPConnections_Type()
)
l4TCPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l4TCPConnections.setStatus("current")
_L7HTTPRequests_Type = OctetString
_L7HTTPRequests_Object = MibScalar
l7HTTPRequests = _L7HTTPRequests_Object(
    (1, 3, 6, 1, 4, 1, 20632, 5, 7),
    _L7HTTPRequests_Type()
)
l7HTTPRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l7HTTPRequests.setStatus("current")
_RdpUserSessions_Type = Integer32
_RdpUserSessions_Object = MibScalar
rdpUserSessions = _RdpUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 20632, 5, 8),
    _RdpUserSessions_Type()
)
rdpUserSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdpUserSessions.setStatus("current")
_ServiceBandwidth_Type = Integer32
_ServiceBandwidth_Object = MibScalar
serviceBandwidth = _ServiceBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 20632, 5, 9),
    _ServiceBandwidth_Type()
)
serviceBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceBandwidth.setStatus("current")
_TotalBandwidthToLB_Type = Integer32
_TotalBandwidthToLB_Object = MibScalar
totalBandwidthToLB = _TotalBandwidthToLB_Object(
    (1, 3, 6, 1, 4, 1, 20632, 5, 10),
    _TotalBandwidthToLB_Type()
)
totalBandwidthToLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBandwidthToLB.setStatus("current")
_RealServerBandwidth_Type = Integer32
_RealServerBandwidth_Object = MibScalar
realServerBandwidth = _RealServerBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 20632, 5, 11),
    _RealServerBandwidth_Type()
)
realServerBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerBandwidth.setStatus("current")
_ClusterStatus_Type = Integer32
_ClusterStatus_Object = MibScalar
clusterStatus = _ClusterStatus_Object(
    (1, 3, 6, 1, 4, 1, 20632, 5, 12),
    _ClusterStatus_Type()
)
clusterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatus.setStatus("current")
_SystemLoad_Type = Integer32
_SystemLoad_Object = MibScalar
systemLoad = _SystemLoad_Object(
    (1, 3, 6, 1, 4, 1, 20632, 5, 13),
    _SystemLoad_Type()
)
systemLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLoad.setStatus("current")
_CpuTemperature_Type = Integer32
_CpuTemperature_Object = MibScalar
cpuTemperature = _CpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 20632, 5, 14),
    _CpuTemperature_Type()
)
cpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTemperature.setStatus("current")
_FirmwareStorage_Type = Integer32
_FirmwareStorage_Object = MibScalar
firmwareStorage = _FirmwareStorage_Object(
    (1, 3, 6, 1, 4, 1, 20632, 5, 15),
    _FirmwareStorage_Type()
)
firmwareStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareStorage.setStatus("current")
_MailLogStorage_Type = Integer32
_MailLogStorage_Object = MibScalar
mailLogStorage = _MailLogStorage_Object(
    (1, 3, 6, 1, 4, 1, 20632, 5, 16),
    _MailLogStorage_Type()
)
mailLogStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mailLogStorage.setStatus("current")
_OperationMode_Type = Integer32
_OperationMode_Object = MibScalar
operationMode = _OperationMode_Object(
    (1, 3, 6, 1, 4, 1, 20632, 5, 17),
    _OperationMode_Type()
)
operationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationMode.setStatus("current")

# Managed Objects groups


# Notification objects

cpuFanDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 5, 1, 2)
)
if mibBuilder.loadTexts:
    cpuFanDead.setStatus(
        "current"
    )

sysFanDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 5, 1, 3)
)
if mibBuilder.loadTexts:
    sysFanDead.setStatus(
        "current"
    )

cpuTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 5, 1, 4)
)
if mibBuilder.loadTexts:
    cpuTempHigh.setStatus(
        "current"
    )

firmwareStorageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 5, 1, 5)
)
if mibBuilder.loadTexts:
    firmwareStorageHigh.setStatus(
        "current"
    )

logsStorageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 5, 1, 6)
)
if mibBuilder.loadTexts:
    logsStorageHigh.setStatus(
        "current"
    )

serviceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 5, 1, 7)
)
if mibBuilder.loadTexts:
    serviceUp.setStatus(
        "current"
    )

serviceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 5, 1, 8)
)
if mibBuilder.loadTexts:
    serviceDown.setStatus(
        "current"
    )

serverUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 5, 1, 9)
)
if mibBuilder.loadTexts:
    serverUp.setStatus(
        "current"
    )

serverDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 5, 1, 10)
)
if mibBuilder.loadTexts:
    serverDown.setStatus(
        "current"
    )

openConnsLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 5, 1, 11)
)
if mibBuilder.loadTexts:
    openConnsLimitReached.setStatus(
        "current"
    )

cpsLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 5, 1, 12)
)
if mibBuilder.loadTexts:
    cpsLimitReached.setStatus(
        "current"
    )

sslTPSLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 5, 1, 13)
)
if mibBuilder.loadTexts:
    sslTPSLimitReached.setStatus(
        "current"
    )

highAvailabilityStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 5, 1, 14)
)
if mibBuilder.loadTexts:
    highAvailabilityStatus.setStatus(
        "current"
    )

cpuTempCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 5, 1, 15)
)
if mibBuilder.loadTexts:
    cpuTempCritical.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Barracuda-LB",
    **{"blb": blb,
       "blbtraps": blbtraps,
       "cpuFanDead": cpuFanDead,
       "sysFanDead": sysFanDead,
       "cpuTempHigh": cpuTempHigh,
       "firmwareStorageHigh": firmwareStorageHigh,
       "logsStorageHigh": logsStorageHigh,
       "serviceUp": serviceUp,
       "serviceDown": serviceDown,
       "serverUp": serverUp,
       "serverDown": serverDown,
       "openConnsLimitReached": openConnsLimitReached,
       "cpsLimitReached": cpsLimitReached,
       "sslTPSLimitReached": sslTPSLimitReached,
       "highAvailabilityStatus": highAvailabilityStatus,
       "cpuTempCritical": cpuTempCritical,
       "systemActiveServices": systemActiveServices,
       "systemOperatingServers": systemOperatingServers,
       "l4TCPConnections": l4TCPConnections,
       "l7HTTPRequests": l7HTTPRequests,
       "rdpUserSessions": rdpUserSessions,
       "serviceBandwidth": serviceBandwidth,
       "totalBandwidthToLB": totalBandwidthToLB,
       "realServerBandwidth": realServerBandwidth,
       "clusterStatus": clusterStatus,
       "systemLoad": systemLoad,
       "cpuTemperature": cpuTemperature,
       "firmwareStorage": firmwareStorage,
       "mailLogStorage": mailLogStorage,
       "operationMode": operationMode}
)
