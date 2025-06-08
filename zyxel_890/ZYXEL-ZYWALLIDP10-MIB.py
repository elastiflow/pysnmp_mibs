# SNMP MIB module (ZYXEL-ZYWALLIDP10-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-ZYWALLIDP10-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:20:54 2025
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

(zywallidp10,) = mibBuilder.importSymbols(
    "ZYXEL-MIB",
    "zywallidp10")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZywallIDP10System_ObjectIdentity = ObjectIdentity
zywallIDP10System = _ZywallIDP10System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 1)
)
_SysFirmwareVersion_Type = DisplayString
_SysFirmwareVersion_Object = MibScalar
sysFirmwareVersion = _SysFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 1, 1),
    _SysFirmwareVersion_Type()
)
sysFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFirmwareVersion.setStatus("mandatory")
_SysPolicyVersion_Type = DisplayString
_SysPolicyVersion_Object = MibScalar
sysPolicyVersion = _SysPolicyVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 1, 2),
    _SysPolicyVersion_Type()
)
sysPolicyVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPolicyVersion.setStatus("mandatory")
_SysCPUUsage_Type = Integer32
_SysCPUUsage_Object = MibScalar
sysCPUUsage = _SysCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 1, 3),
    _SysCPUUsage_Type()
)
sysCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCPUUsage.setStatus("mandatory")
_SysFlashUsage_Type = Integer32
_SysFlashUsage_Object = MibScalar
sysFlashUsage = _SysFlashUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 1, 4),
    _SysFlashUsage_Type()
)
sysFlashUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFlashUsage.setStatus("mandatory")
_SysRAMUsage_Type = Integer32
_SysRAMUsage_Object = MibScalar
sysRAMUsage = _SysRAMUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 1, 5),
    _SysRAMUsage_Type()
)
sysRAMUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRAMUsage.setStatus("mandatory")
_SysTCPSession_Type = Integer32
_SysTCPSession_Object = MibScalar
sysTCPSession = _SysTCPSession_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 1, 6),
    _SysTCPSession_Type()
)
sysTCPSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTCPSession.setStatus("mandatory")
_SysPolicyNumber_Type = Integer32
_SysPolicyNumber_Object = MibScalar
sysPolicyNumber = _SysPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 1, 7),
    _SysPolicyNumber_Type()
)
sysPolicyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPolicyNumber.setStatus("mandatory")
_SysState_Type = DisplayString
_SysState_Object = MibScalar
sysState = _SysState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 1, 8),
    _SysState_Type()
)
sysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysState.setStatus("mandatory")
_SysRegistrationStatus_Type = DisplayString
_SysRegistrationStatus_Object = MibScalar
sysRegistrationStatus = _SysRegistrationStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 1, 9),
    _SysRegistrationStatus_Type()
)
sysRegistrationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRegistrationStatus.setStatus("mandatory")
_SysAttackNumbers_Type = Integer32
_SysAttackNumbers_Object = MibScalar
sysAttackNumbers = _SysAttackNumbers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 1, 10),
    _SysAttackNumbers_Type()
)
sysAttackNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAttackNumbers.setStatus("mandatory")
_SysWarningNumbers_Type = Integer32
_SysWarningNumbers_Object = MibScalar
sysWarningNumbers = _SysWarningNumbers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 1, 11),
    _SysWarningNumbers_Type()
)
sysWarningNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysWarningNumbers.setStatus("mandatory")
_ZywallIDP10Network_ObjectIdentity = ObjectIdentity
zywallIDP10Network = _ZywallIDP10Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2)
)
_NetworkInterfaceLinkStatus_ObjectIdentity = ObjectIdentity
networkInterfaceLinkStatus = _NetworkInterfaceLinkStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 1)
)
_LinkStatusWANPort_Type = DisplayString
_LinkStatusWANPort_Object = MibScalar
linkStatusWANPort = _LinkStatusWANPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 1, 1),
    _LinkStatusWANPort_Type()
)
linkStatusWANPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusWANPort.setStatus("mandatory")
_LinkStatusLANPort_Type = DisplayString
_LinkStatusLANPort_Object = MibScalar
linkStatusLANPort = _LinkStatusLANPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 1, 2),
    _LinkStatusLANPort_Type()
)
linkStatusLANPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusLANPort.setStatus("mandatory")
_LinkStatusMGMTPort_Type = DisplayString
_LinkStatusMGMTPort_Object = MibScalar
linkStatusMGMTPort = _LinkStatusMGMTPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 1, 3),
    _LinkStatusMGMTPort_Type()
)
linkStatusMGMTPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusMGMTPort.setStatus("mandatory")
_NetworkMTUSize_ObjectIdentity = ObjectIdentity
networkMTUSize = _NetworkMTUSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 2)
)
_MtuSizeWANPort_Type = Integer32
_MtuSizeWANPort_Object = MibScalar
mtuSizeWANPort = _MtuSizeWANPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 2, 1),
    _MtuSizeWANPort_Type()
)
mtuSizeWANPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtuSizeWANPort.setStatus("mandatory")
_MtuSizeLANPort_Type = Integer32
_MtuSizeLANPort_Object = MibScalar
mtuSizeLANPort = _MtuSizeLANPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 2, 2),
    _MtuSizeLANPort_Type()
)
mtuSizeLANPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtuSizeLANPort.setStatus("mandatory")
_MtuSizeMGMTPort_Type = Integer32
_MtuSizeMGMTPort_Object = MibScalar
mtuSizeMGMTPort = _MtuSizeMGMTPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 2, 3),
    _MtuSizeMGMTPort_Type()
)
mtuSizeMGMTPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtuSizeMGMTPort.setStatus("mandatory")
_NetworkTraffic_ObjectIdentity = ObjectIdentity
networkTraffic = _NetworkTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 3)
)
_TrafficWANPortIn_Type = Integer32
_TrafficWANPortIn_Object = MibScalar
trafficWANPortIn = _TrafficWANPortIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 3, 1),
    _TrafficWANPortIn_Type()
)
trafficWANPortIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficWANPortIn.setStatus("mandatory")
_TrafficWANPortOut_Type = Integer32
_TrafficWANPortOut_Object = MibScalar
trafficWANPortOut = _TrafficWANPortOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 3, 2),
    _TrafficWANPortOut_Type()
)
trafficWANPortOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficWANPortOut.setStatus("mandatory")
_TrafficLANPortIn_Type = Integer32
_TrafficLANPortIn_Object = MibScalar
trafficLANPortIn = _TrafficLANPortIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 3, 3),
    _TrafficLANPortIn_Type()
)
trafficLANPortIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficLANPortIn.setStatus("mandatory")
_TrafficLANPortOut_Type = Integer32
_TrafficLANPortOut_Object = MibScalar
trafficLANPortOut = _TrafficLANPortOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 3, 4),
    _TrafficLANPortOut_Type()
)
trafficLANPortOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficLANPortOut.setStatus("mandatory")
_TrafficMGMTPortIn_Type = Integer32
_TrafficMGMTPortIn_Object = MibScalar
trafficMGMTPortIn = _TrafficMGMTPortIn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 3, 5),
    _TrafficMGMTPortIn_Type()
)
trafficMGMTPortIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficMGMTPortIn.setStatus("mandatory")
_TrafficMGMTPortOut_Type = Integer32
_TrafficMGMTPortOut_Object = MibScalar
trafficMGMTPortOut = _TrafficMGMTPortOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 3, 6),
    _TrafficMGMTPortOut_Type()
)
trafficMGMTPortOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficMGMTPortOut.setStatus("mandatory")
_NetworkInterfaceUtilization_ObjectIdentity = ObjectIdentity
networkInterfaceUtilization = _NetworkInterfaceUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 4)
)
_IntUtilizationWANPort_Type = Integer32
_IntUtilizationWANPort_Object = MibScalar
intUtilizationWANPort = _IntUtilizationWANPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 4, 1),
    _IntUtilizationWANPort_Type()
)
intUtilizationWANPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intUtilizationWANPort.setStatus("mandatory")
_IntUtilizationLANPort_Type = Integer32
_IntUtilizationLANPort_Object = MibScalar
intUtilizationLANPort = _IntUtilizationLANPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 4, 2),
    _IntUtilizationLANPort_Type()
)
intUtilizationLANPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intUtilizationLANPort.setStatus("mandatory")
_IntUtilizationMGMTPort_Type = Integer32
_IntUtilizationMGMTPort_Object = MibScalar
intUtilizationMGMTPort = _IntUtilizationMGMTPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 4, 3),
    _IntUtilizationMGMTPort_Type()
)
intUtilizationMGMTPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intUtilizationMGMTPort.setStatus("mandatory")
_NetworkPacketStatistic_ObjectIdentity = ObjectIdentity
networkPacketStatistic = _NetworkPacketStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 5)
)
_PacketDroppedWANPort_Type = Integer32
_PacketDroppedWANPort_Object = MibScalar
packetDroppedWANPort = _PacketDroppedWANPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 5, 1),
    _PacketDroppedWANPort_Type()
)
packetDroppedWANPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetDroppedWANPort.setStatus("mandatory")
_PacketBlockedWANPort_Type = Integer32
_PacketBlockedWANPort_Object = MibScalar
packetBlockedWANPort = _PacketBlockedWANPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 5, 2),
    _PacketBlockedWANPort_Type()
)
packetBlockedWANPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetBlockedWANPort.setStatus("mandatory")
_PacketForwardedWANPort_Type = Integer32
_PacketForwardedWANPort_Object = MibScalar
packetForwardedWANPort = _PacketForwardedWANPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 5, 3),
    _PacketForwardedWANPort_Type()
)
packetForwardedWANPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetForwardedWANPort.setStatus("mandatory")
_PacketDroppedLANPort_Type = Integer32
_PacketDroppedLANPort_Object = MibScalar
packetDroppedLANPort = _PacketDroppedLANPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 5, 4),
    _PacketDroppedLANPort_Type()
)
packetDroppedLANPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetDroppedLANPort.setStatus("mandatory")
_PacketBlockedLANPort_Type = Integer32
_PacketBlockedLANPort_Object = MibScalar
packetBlockedLANPort = _PacketBlockedLANPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 5, 5),
    _PacketBlockedLANPort_Type()
)
packetBlockedLANPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetBlockedLANPort.setStatus("mandatory")
_PacketForwardedLANPort_Type = Integer32
_PacketForwardedLANPort_Object = MibScalar
packetForwardedLANPort = _PacketForwardedLANPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11, 2, 5, 6),
    _PacketForwardedLANPort_Type()
)
packetForwardedLANPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetForwardedLANPort.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ZYWALLIDP10-MIB",
    **{"zywallIDP10System": zywallIDP10System,
       "sysFirmwareVersion": sysFirmwareVersion,
       "sysPolicyVersion": sysPolicyVersion,
       "sysCPUUsage": sysCPUUsage,
       "sysFlashUsage": sysFlashUsage,
       "sysRAMUsage": sysRAMUsage,
       "sysTCPSession": sysTCPSession,
       "sysPolicyNumber": sysPolicyNumber,
       "sysState": sysState,
       "sysRegistrationStatus": sysRegistrationStatus,
       "sysAttackNumbers": sysAttackNumbers,
       "sysWarningNumbers": sysWarningNumbers,
       "zywallIDP10Network": zywallIDP10Network,
       "networkInterfaceLinkStatus": networkInterfaceLinkStatus,
       "linkStatusWANPort": linkStatusWANPort,
       "linkStatusLANPort": linkStatusLANPort,
       "linkStatusMGMTPort": linkStatusMGMTPort,
       "networkMTUSize": networkMTUSize,
       "mtuSizeWANPort": mtuSizeWANPort,
       "mtuSizeLANPort": mtuSizeLANPort,
       "mtuSizeMGMTPort": mtuSizeMGMTPort,
       "networkTraffic": networkTraffic,
       "trafficWANPortIn": trafficWANPortIn,
       "trafficWANPortOut": trafficWANPortOut,
       "trafficLANPortIn": trafficLANPortIn,
       "trafficLANPortOut": trafficLANPortOut,
       "trafficMGMTPortIn": trafficMGMTPortIn,
       "trafficMGMTPortOut": trafficMGMTPortOut,
       "networkInterfaceUtilization": networkInterfaceUtilization,
       "intUtilizationWANPort": intUtilizationWANPort,
       "intUtilizationLANPort": intUtilizationLANPort,
       "intUtilizationMGMTPort": intUtilizationMGMTPort,
       "networkPacketStatistic": networkPacketStatistic,
       "packetDroppedWANPort": packetDroppedWANPort,
       "packetBlockedWANPort": packetBlockedWANPort,
       "packetForwardedWANPort": packetForwardedWANPort,
       "packetDroppedLANPort": packetDroppedLANPort,
       "packetBlockedLANPort": packetBlockedLANPort,
       "packetForwardedLANPort": packetForwardedLANPort}
)
