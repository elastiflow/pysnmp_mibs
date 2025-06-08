# SNMP MIB module (ZYXEL-ZYWALL-ZLD-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-ZYWALL-ZLD-COMMON-MIB.mib
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

(zywallZLDCommon,) = mibBuilder.importSymbols(
    "ZYXEL-MIB",
    "zywallZLDCommon")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZldSystem_ObjectIdentity = ObjectIdentity
zldSystem = _ZldSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 1)
)
_SysCPUUsage_Type = Integer32
_SysCPUUsage_Object = MibScalar
sysCPUUsage = _SysCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 1, 1),
    _SysCPUUsage_Type()
)
sysCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCPUUsage.setStatus("mandatory")
_SysRAMUsage_Type = Integer32
_SysRAMUsage_Object = MibScalar
sysRAMUsage = _SysRAMUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 1, 2),
    _SysRAMUsage_Type()
)
sysRAMUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRAMUsage.setStatus("mandatory")
_SysCPU5SecUsage_Type = Integer32
_SysCPU5SecUsage_Object = MibScalar
sysCPU5SecUsage = _SysCPU5SecUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 1, 3),
    _SysCPU5SecUsage_Type()
)
sysCPU5SecUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCPU5SecUsage.setStatus("mandatory")
_SysCPU1MinUsage_Type = Integer32
_SysCPU1MinUsage_Object = MibScalar
sysCPU1MinUsage = _SysCPU1MinUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 1, 4),
    _SysCPU1MinUsage_Type()
)
sysCPU1MinUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCPU1MinUsage.setStatus("mandatory")
_SysCPU5MinUsage_Type = Integer32
_SysCPU5MinUsage_Object = MibScalar
sysCPU5MinUsage = _SysCPU5MinUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 1, 5),
    _SysCPU5MinUsage_Type()
)
sysCPU5MinUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCPU5MinUsage.setStatus("mandatory")
_SysSessionNum_Type = Integer32
_SysSessionNum_Object = MibScalar
sysSessionNum = _SysSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 1, 6),
    _SysSessionNum_Type()
)
sysSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSessionNum.setStatus("mandatory")
_SysFLASHUsage_Type = Integer32
_SysFLASHUsage_Object = MibScalar
sysFLASHUsage = _SysFLASHUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 1, 7),
    _SysFLASHUsage_Type()
)
sysFLASHUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFLASHUsage.setStatus("mandatory")
_ZldIpSecVPN_ObjectIdentity = ObjectIdentity
zldIpSecVPN = _ZldIpSecVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2)
)
_VpnIpSecTotalThroughput_Type = Integer32
_VpnIpSecTotalThroughput_Object = MibScalar
vpnIpSecTotalThroughput = _VpnIpSecTotalThroughput_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 1),
    _VpnIpSecTotalThroughput_Type()
)
vpnIpSecTotalThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnIpSecTotalThroughput.setStatus("mandatory")
_VpnTunnelTable_Object = MibTable
vpnTunnelTable = _VpnTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 2)
)
if mibBuilder.loadTexts:
    vpnTunnelTable.setStatus("current")
_VpnTunnelEntry_Object = MibTableRow
vpnTunnelEntry = _VpnTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 2, 1)
)
vpnTunnelEntry.setIndexNames(
    (0, "ZYXEL-ZYWALL-ZLD-COMMON-MIB", "vpnTunnelIndex"),
)
if mibBuilder.loadTexts:
    vpnTunnelEntry.setStatus("current")
_VpnTunnelName_Type = DisplayString
_VpnTunnelName_Object = MibTableColumn
vpnTunnelName = _VpnTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 2, 1, 1),
    _VpnTunnelName_Type()
)
vpnTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelName.setStatus("current")
_VpnIKEName_Type = DisplayString
_VpnIKEName_Object = MibTableColumn
vpnIKEName = _VpnIKEName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 2, 1, 2),
    _VpnIKEName_Type()
)
vpnIKEName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnIKEName.setStatus("current")
_VpnTunnelSPI_Type = DisplayString
_VpnTunnelSPI_Object = MibTableColumn
vpnTunnelSPI = _VpnTunnelSPI_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 2, 1, 3),
    _VpnTunnelSPI_Type()
)
vpnTunnelSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelSPI.setStatus("current")
_VpnStatusTable_Object = MibTable
vpnStatusTable = _VpnStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 4)
)
if mibBuilder.loadTexts:
    vpnStatusTable.setStatus("current")
_VpnStatusEntry_Object = MibTableRow
vpnStatusEntry = _VpnStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 4, 1)
)
vpnStatusEntry.setIndexNames(
    (0, "ZYXEL-ZYWALL-ZLD-COMMON-MIB", "vpnStatusIndex"),
)
if mibBuilder.loadTexts:
    vpnStatusEntry.setStatus("current")
_VpnStatusIndex_Type = Integer32
_VpnStatusIndex_Object = MibTableColumn
vpnStatusIndex = _VpnStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 4, 1, 1),
    _VpnStatusIndex_Type()
)
vpnStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnStatusIndex.setStatus("current")
_VpnStatusConnectionName_Type = DisplayString
_VpnStatusConnectionName_Object = MibTableColumn
vpnStatusConnectionName = _VpnStatusConnectionName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 4, 1, 2),
    _VpnStatusConnectionName_Type()
)
vpnStatusConnectionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnStatusConnectionName.setStatus("current")
_VpnStatusGateway_Type = DisplayString
_VpnStatusGateway_Object = MibTableColumn
vpnStatusGateway = _VpnStatusGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 4, 1, 3),
    _VpnStatusGateway_Type()
)
vpnStatusGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnStatusGateway.setStatus("current")
_VpnStatusIPVersion_Type = DisplayString
_VpnStatusIPVersion_Object = MibTableColumn
vpnStatusIPVersion = _VpnStatusIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 4, 1, 4),
    _VpnStatusIPVersion_Type()
)
vpnStatusIPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnStatusIPVersion.setStatus("current")


class _VpnStatusActiveStatus_Type(Integer32):
    """Custom type vpnStatusActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_VpnStatusActiveStatus_Type.__name__ = "Integer32"
_VpnStatusActiveStatus_Object = MibTableColumn
vpnStatusActiveStatus = _VpnStatusActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 4, 1, 5),
    _VpnStatusActiveStatus_Type()
)
vpnStatusActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnStatusActiveStatus.setStatus("current")


class _VpnStatusConnectStatus_Type(Integer32):
    """Custom type vpnStatusConnectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("connected", 1))
    )


_VpnStatusConnectStatus_Type.__name__ = "Integer32"
_VpnStatusConnectStatus_Object = MibTableColumn
vpnStatusConnectStatus = _VpnStatusConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 4, 1, 6),
    _VpnStatusConnectStatus_Type()
)
vpnStatusConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnStatusConnectStatus.setStatus("current")
_VpnConnectionCounter_ObjectIdentity = ObjectIdentity
vpnConnectionCounter = _VpnConnectionCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 5)
)
_VpnConnectionTotal_Type = Counter32
_VpnConnectionTotal_Object = MibScalar
vpnConnectionTotal = _VpnConnectionTotal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 5, 1),
    _VpnConnectionTotal_Type()
)
vpnConnectionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnConnectionTotal.setStatus("current")
_VpnConnectionActive_Type = Counter32
_VpnConnectionActive_Object = MibScalar
vpnConnectionActive = _VpnConnectionActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 5, 2),
    _VpnConnectionActive_Type()
)
vpnConnectionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnConnectionActive.setStatus("current")
_VpnConnectionConnected_Type = Counter32
_VpnConnectionConnected_Object = MibScalar
vpnConnectionConnected = _VpnConnectionConnected_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 5, 3),
    _VpnConnectionConnected_Type()
)
vpnConnectionConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnConnectionConnected.setStatus("current")
_VpnConnectionDisconnected_Type = Counter32
_VpnConnectionDisconnected_Object = MibScalar
vpnConnectionDisconnected = _VpnConnectionDisconnected_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 5, 4),
    _VpnConnectionDisconnected_Type()
)
vpnConnectionDisconnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnConnectionDisconnected.setStatus("current")
_VpnSaMonitorTable_Object = MibTable
vpnSaMonitorTable = _VpnSaMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 6)
)
if mibBuilder.loadTexts:
    vpnSaMonitorTable.setStatus("current")
_VpnSaMonitorEntry_Object = MibTableRow
vpnSaMonitorEntry = _VpnSaMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 6, 1)
)
vpnSaMonitorEntry.setIndexNames(
    (0, "ZYXEL-ZYWALL-ZLD-COMMON-MIB", "vpnSaMonitorIndex"),
)
if mibBuilder.loadTexts:
    vpnSaMonitorEntry.setStatus("current")
_VpnSaMonitorIndex_Type = Integer32
_VpnSaMonitorIndex_Object = MibTableColumn
vpnSaMonitorIndex = _VpnSaMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 6, 1, 1),
    _VpnSaMonitorIndex_Type()
)
vpnSaMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSaMonitorIndex.setStatus("current")
_VpnSaMonitorConnectionName_Type = DisplayString
_VpnSaMonitorConnectionName_Object = MibTableColumn
vpnSaMonitorConnectionName = _VpnSaMonitorConnectionName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 6, 1, 2),
    _VpnSaMonitorConnectionName_Type()
)
vpnSaMonitorConnectionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSaMonitorConnectionName.setStatus("current")
_VpnSaMonitorPolicy_Type = DisplayString
_VpnSaMonitorPolicy_Object = MibTableColumn
vpnSaMonitorPolicy = _VpnSaMonitorPolicy_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 6, 1, 3),
    _VpnSaMonitorPolicy_Type()
)
vpnSaMonitorPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSaMonitorPolicy.setStatus("current")
_VpnSaMonitorUpTime_Type = Integer32
_VpnSaMonitorUpTime_Object = MibTableColumn
vpnSaMonitorUpTime = _VpnSaMonitorUpTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 6, 1, 4),
    _VpnSaMonitorUpTime_Type()
)
vpnSaMonitorUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSaMonitorUpTime.setStatus("current")
_VpnSaMonitorTimeout_Type = Integer32
_VpnSaMonitorTimeout_Object = MibTableColumn
vpnSaMonitorTimeout = _VpnSaMonitorTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 6, 1, 5),
    _VpnSaMonitorTimeout_Type()
)
vpnSaMonitorTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSaMonitorTimeout.setStatus("current")
_VpnSaMonitorInPkts_Type = Counter64
_VpnSaMonitorInPkts_Object = MibTableColumn
vpnSaMonitorInPkts = _VpnSaMonitorInPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 6, 1, 6),
    _VpnSaMonitorInPkts_Type()
)
vpnSaMonitorInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSaMonitorInPkts.setStatus("current")
_VpnSaMonitorInBytes_Type = Counter64
_VpnSaMonitorInBytes_Object = MibTableColumn
vpnSaMonitorInBytes = _VpnSaMonitorInBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 6, 1, 7),
    _VpnSaMonitorInBytes_Type()
)
vpnSaMonitorInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSaMonitorInBytes.setStatus("current")
_VpnSaMonitorOutPkts_Type = Counter64
_VpnSaMonitorOutPkts_Object = MibTableColumn
vpnSaMonitorOutPkts = _VpnSaMonitorOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 6, 1, 8),
    _VpnSaMonitorOutPkts_Type()
)
vpnSaMonitorOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSaMonitorOutPkts.setStatus("current")
_VpnSaMonitorOutBytes_Type = Counter64
_VpnSaMonitorOutBytes_Object = MibTableColumn
vpnSaMonitorOutBytes = _VpnSaMonitorOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 6, 1, 9),
    _VpnSaMonitorOutBytes_Type()
)
vpnSaMonitorOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSaMonitorOutBytes.setStatus("current")

# Managed Objects groups


# Notification objects

vpnTunnelDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22, 2, 3)
)
vpnTunnelDisconnected.setObjects(
      *(("ZYXEL-ZYWALL-ZLD-COMMON-MIB", "vpnTunnelName"),
        ("ZYXEL-ZYWALL-ZLD-COMMON-MIB", "vpnIKEName"),
        ("ZYXEL-ZYWALL-ZLD-COMMON-MIB", "vpnTunnelSPI"))
)
if mibBuilder.loadTexts:
    vpnTunnelDisconnected.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ZYWALL-ZLD-COMMON-MIB",
    **{"zldSystem": zldSystem,
       "sysCPUUsage": sysCPUUsage,
       "sysRAMUsage": sysRAMUsage,
       "sysCPU5SecUsage": sysCPU5SecUsage,
       "sysCPU1MinUsage": sysCPU1MinUsage,
       "sysCPU5MinUsage": sysCPU5MinUsage,
       "sysSessionNum": sysSessionNum,
       "sysFLASHUsage": sysFLASHUsage,
       "zldIpSecVPN": zldIpSecVPN,
       "vpnIpSecTotalThroughput": vpnIpSecTotalThroughput,
       "vpnTunnelTable": vpnTunnelTable,
       "vpnTunnelEntry": vpnTunnelEntry,
       "vpnTunnelName": vpnTunnelName,
       "vpnIKEName": vpnIKEName,
       "vpnTunnelSPI": vpnTunnelSPI,
       "vpnTunnelDisconnected": vpnTunnelDisconnected,
       "vpnStatusTable": vpnStatusTable,
       "vpnStatusEntry": vpnStatusEntry,
       "vpnStatusIndex": vpnStatusIndex,
       "vpnStatusConnectionName": vpnStatusConnectionName,
       "vpnStatusGateway": vpnStatusGateway,
       "vpnStatusIPVersion": vpnStatusIPVersion,
       "vpnStatusActiveStatus": vpnStatusActiveStatus,
       "vpnStatusConnectStatus": vpnStatusConnectStatus,
       "vpnConnectionCounter": vpnConnectionCounter,
       "vpnConnectionTotal": vpnConnectionTotal,
       "vpnConnectionActive": vpnConnectionActive,
       "vpnConnectionConnected": vpnConnectionConnected,
       "vpnConnectionDisconnected": vpnConnectionDisconnected,
       "vpnSaMonitorTable": vpnSaMonitorTable,
       "vpnSaMonitorEntry": vpnSaMonitorEntry,
       "vpnSaMonitorIndex": vpnSaMonitorIndex,
       "vpnSaMonitorConnectionName": vpnSaMonitorConnectionName,
       "vpnSaMonitorPolicy": vpnSaMonitorPolicy,
       "vpnSaMonitorUpTime": vpnSaMonitorUpTime,
       "vpnSaMonitorTimeout": vpnSaMonitorTimeout,
       "vpnSaMonitorInPkts": vpnSaMonitorInPkts,
       "vpnSaMonitorInBytes": vpnSaMonitorInBytes,
       "vpnSaMonitorOutPkts": vpnSaMonitorOutPkts,
       "vpnSaMonitorOutBytes": vpnSaMonitorOutBytes}
)
