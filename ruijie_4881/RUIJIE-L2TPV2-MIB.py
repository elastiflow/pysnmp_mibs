# SNMP MIB module (RUIJIE-L2TPV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-L2TPV2-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:17 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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

ruijieL2TPv2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieL2TPv2Objects_ObjectIdentity = ObjectIdentity
ruijieL2TPv2Objects = _RuijieL2TPv2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1)
)
_RuijieL2TPv2TunnelTable_Object = MibTable
ruijieL2TPv2TunnelTable = _RuijieL2TPv2TunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieL2TPv2TunnelTable.setStatus("current")
_RuijieL2TPv2TunnelEntry_Object = MibTableRow
ruijieL2TPv2TunnelEntry = _RuijieL2TPv2TunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 1, 1)
)
ruijieL2TPv2TunnelEntry.setIndexNames(
    (0, "RUIJIE-L2TPV2-MIB", "ruijieL2TPv2TunnelLocalID"),
)
if mibBuilder.loadTexts:
    ruijieL2TPv2TunnelEntry.setStatus("current")


class _RuijieL2TPv2TunnelLocalID_Type(Unsigned32):
    """Custom type ruijieL2TPv2TunnelLocalID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieL2TPv2TunnelLocalID_Type.__name__ = "Unsigned32"
_RuijieL2TPv2TunnelLocalID_Object = MibTableColumn
ruijieL2TPv2TunnelLocalID = _RuijieL2TPv2TunnelLocalID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 1, 1, 1),
    _RuijieL2TPv2TunnelLocalID_Type()
)
ruijieL2TPv2TunnelLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2TunnelLocalID.setStatus("current")
_RuijieL2TPv2TunnelRemoteID_Type = Unsigned32
_RuijieL2TPv2TunnelRemoteID_Object = MibTableColumn
ruijieL2TPv2TunnelRemoteID = _RuijieL2TPv2TunnelRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 1, 1, 2),
    _RuijieL2TPv2TunnelRemoteID_Type()
)
ruijieL2TPv2TunnelRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2TunnelRemoteID.setStatus("current")
_RuijieL2TPv2TunnelStatus_Type = Unsigned32
_RuijieL2TPv2TunnelStatus_Object = MibTableColumn
ruijieL2TPv2TunnelStatus = _RuijieL2TPv2TunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 1, 1, 3),
    _RuijieL2TPv2TunnelStatus_Type()
)
ruijieL2TPv2TunnelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieL2TPv2TunnelStatus.setStatus("current")
_RuijieL2TPv2TunnelSrcIP_Type = IpAddress
_RuijieL2TPv2TunnelSrcIP_Object = MibTableColumn
ruijieL2TPv2TunnelSrcIP = _RuijieL2TPv2TunnelSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 1, 1, 4),
    _RuijieL2TPv2TunnelSrcIP_Type()
)
ruijieL2TPv2TunnelSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2TunnelSrcIP.setStatus("current")
_RuijieL2TPv2TunnelDstIP_Type = IpAddress
_RuijieL2TPv2TunnelDstIP_Object = MibTableColumn
ruijieL2TPv2TunnelDstIP = _RuijieL2TPv2TunnelDstIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 1, 1, 5),
    _RuijieL2TPv2TunnelDstIP_Type()
)
ruijieL2TPv2TunnelDstIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2TunnelDstIP.setStatus("current")
_RuijieL2TPv2TunnelLacHostname_Type = OctetString
_RuijieL2TPv2TunnelLacHostname_Object = MibTableColumn
ruijieL2TPv2TunnelLacHostname = _RuijieL2TPv2TunnelLacHostname_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 1, 1, 6),
    _RuijieL2TPv2TunnelLacHostname_Type()
)
ruijieL2TPv2TunnelLacHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2TunnelLacHostname.setStatus("current")
_RuijieL2TPv2TunnelLacVendor_Type = OctetString
_RuijieL2TPv2TunnelLacVendor_Object = MibTableColumn
ruijieL2TPv2TunnelLacVendor = _RuijieL2TPv2TunnelLacVendor_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 1, 1, 7),
    _RuijieL2TPv2TunnelLacVendor_Type()
)
ruijieL2TPv2TunnelLacVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2TunnelLacVendor.setStatus("current")
_RuijieL2TPv2SessionTable_Object = MibTable
ruijieL2TPv2SessionTable = _RuijieL2TPv2SessionTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionTable.setStatus("current")
_RuijieL2TPv2SessionEntry_Object = MibTableRow
ruijieL2TPv2SessionEntry = _RuijieL2TPv2SessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 2, 1)
)
ruijieL2TPv2SessionEntry.setIndexNames(
    (0, "RUIJIE-L2TPV2-MIB", "ruijieL2TPv2TunnelLocalID"),
    (0, "RUIJIE-L2TPV2-MIB", "ruijieL2TPv2SessionLocalID"),
)
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionEntry.setStatus("current")


class _RuijieL2TPv2SessionLocalID_Type(Unsigned32):
    """Custom type ruijieL2TPv2SessionLocalID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieL2TPv2SessionLocalID_Type.__name__ = "Unsigned32"
_RuijieL2TPv2SessionLocalID_Object = MibTableColumn
ruijieL2TPv2SessionLocalID = _RuijieL2TPv2SessionLocalID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 2, 1, 1),
    _RuijieL2TPv2SessionLocalID_Type()
)
ruijieL2TPv2SessionLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionLocalID.setStatus("current")
_RuijieL2TPv2SessionRemoteID_Type = Unsigned32
_RuijieL2TPv2SessionRemoteID_Object = MibTableColumn
ruijieL2TPv2SessionRemoteID = _RuijieL2TPv2SessionRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 2, 1, 2),
    _RuijieL2TPv2SessionRemoteID_Type()
)
ruijieL2TPv2SessionRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionRemoteID.setStatus("current")
_RuijieL2TPv2SessionUserName_Type = OctetString
_RuijieL2TPv2SessionUserName_Object = MibTableColumn
ruijieL2TPv2SessionUserName = _RuijieL2TPv2SessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 2, 1, 3),
    _RuijieL2TPv2SessionUserName_Type()
)
ruijieL2TPv2SessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionUserName.setStatus("current")
_RuijieL2TPv2SessionStatus_Type = Unsigned32
_RuijieL2TPv2SessionStatus_Object = MibTableColumn
ruijieL2TPv2SessionStatus = _RuijieL2TPv2SessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 2, 1, 4),
    _RuijieL2TPv2SessionStatus_Type()
)
ruijieL2TPv2SessionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionStatus.setStatus("current")
_RuijieL2TPv2SessionSrcIP_Type = IpAddress
_RuijieL2TPv2SessionSrcIP_Object = MibTableColumn
ruijieL2TPv2SessionSrcIP = _RuijieL2TPv2SessionSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 2, 1, 5),
    _RuijieL2TPv2SessionSrcIP_Type()
)
ruijieL2TPv2SessionSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionSrcIP.setStatus("current")
_RuijieL2TPv2SessionDstIP_Type = IpAddress
_RuijieL2TPv2SessionDstIP_Object = MibTableColumn
ruijieL2TPv2SessionDstIP = _RuijieL2TPv2SessionDstIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 2, 1, 6),
    _RuijieL2TPv2SessionDstIP_Type()
)
ruijieL2TPv2SessionDstIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionDstIP.setStatus("current")
_RuijieL2TPv2SessionLocalVrf_Type = Integer32
_RuijieL2TPv2SessionLocalVrf_Object = MibTableColumn
ruijieL2TPv2SessionLocalVrf = _RuijieL2TPv2SessionLocalVrf_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 2, 1, 7),
    _RuijieL2TPv2SessionLocalVrf_Type()
)
ruijieL2TPv2SessionLocalVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionLocalVrf.setStatus("current")
_RuijieL2TPv2SessionExistTime_Type = Integer32
_RuijieL2TPv2SessionExistTime_Object = MibTableColumn
ruijieL2TPv2SessionExistTime = _RuijieL2TPv2SessionExistTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 2, 1, 8),
    _RuijieL2TPv2SessionExistTime_Type()
)
ruijieL2TPv2SessionExistTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionExistTime.setStatus("current")
_RuijieL2TPv2SessionIMSI_Type = OctetString
_RuijieL2TPv2SessionIMSI_Object = MibTableColumn
ruijieL2TPv2SessionIMSI = _RuijieL2TPv2SessionIMSI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 2, 1, 9),
    _RuijieL2TPv2SessionIMSI_Type()
)
ruijieL2TPv2SessionIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionIMSI.setStatus("current")
_RuijieL2TPv2SessionAccessDeviceID_Type = OctetString
_RuijieL2TPv2SessionAccessDeviceID_Object = MibTableColumn
ruijieL2TPv2SessionAccessDeviceID = _RuijieL2TPv2SessionAccessDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 2, 1, 10),
    _RuijieL2TPv2SessionAccessDeviceID_Type()
)
ruijieL2TPv2SessionAccessDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionAccessDeviceID.setStatus("current")
_RuijieL2TPv2SessionTrafficStatTable_Object = MibTable
ruijieL2TPv2SessionTrafficStatTable = _RuijieL2TPv2SessionTrafficStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionTrafficStatTable.setStatus("current")
_RuijieL2TPv2SessionTrafficStatEntry_Object = MibTableRow
ruijieL2TPv2SessionTrafficStatEntry = _RuijieL2TPv2SessionTrafficStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 3, 1)
)
ruijieL2TPv2SessionTrafficStatEntry.setIndexNames(
    (0, "RUIJIE-L2TPV2-MIB", "ruijieL2TPv2TunnelLocalID"),
    (0, "RUIJIE-L2TPV2-MIB", "ruijieL2TPv2SessionLocalID"),
)
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionTrafficStatEntry.setStatus("current")
_RuijieL2TPv2SessionTrafficStatRxBytes_Type = Counter64
_RuijieL2TPv2SessionTrafficStatRxBytes_Object = MibTableColumn
ruijieL2TPv2SessionTrafficStatRxBytes = _RuijieL2TPv2SessionTrafficStatRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 3, 1, 1),
    _RuijieL2TPv2SessionTrafficStatRxBytes_Type()
)
ruijieL2TPv2SessionTrafficStatRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionTrafficStatRxBytes.setStatus("current")
_RuijieL2TPv2SessionTrafficStatRxPkts_Type = Counter64
_RuijieL2TPv2SessionTrafficStatRxPkts_Object = MibTableColumn
ruijieL2TPv2SessionTrafficStatRxPkts = _RuijieL2TPv2SessionTrafficStatRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 3, 1, 2),
    _RuijieL2TPv2SessionTrafficStatRxPkts_Type()
)
ruijieL2TPv2SessionTrafficStatRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionTrafficStatRxPkts.setStatus("current")
_RuijieL2TPv2SessionTrafficStatRxErrPkts_Type = Counter64
_RuijieL2TPv2SessionTrafficStatRxErrPkts_Object = MibTableColumn
ruijieL2TPv2SessionTrafficStatRxErrPkts = _RuijieL2TPv2SessionTrafficStatRxErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 3, 1, 3),
    _RuijieL2TPv2SessionTrafficStatRxErrPkts_Type()
)
ruijieL2TPv2SessionTrafficStatRxErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionTrafficStatRxErrPkts.setStatus("current")
_RuijieL2TPv2SessionTrafficStatRxSpeed_Type = Counter64
_RuijieL2TPv2SessionTrafficStatRxSpeed_Object = MibTableColumn
ruijieL2TPv2SessionTrafficStatRxSpeed = _RuijieL2TPv2SessionTrafficStatRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 3, 1, 4),
    _RuijieL2TPv2SessionTrafficStatRxSpeed_Type()
)
ruijieL2TPv2SessionTrafficStatRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionTrafficStatRxSpeed.setStatus("current")
_RuijieL2TPv2SessionTrafficStatTxBytes_Type = Counter64
_RuijieL2TPv2SessionTrafficStatTxBytes_Object = MibTableColumn
ruijieL2TPv2SessionTrafficStatTxBytes = _RuijieL2TPv2SessionTrafficStatTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 3, 1, 5),
    _RuijieL2TPv2SessionTrafficStatTxBytes_Type()
)
ruijieL2TPv2SessionTrafficStatTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionTrafficStatTxBytes.setStatus("current")
_RuijieL2TPv2SessionTrafficStatTxPkts_Type = Counter64
_RuijieL2TPv2SessionTrafficStatTxPkts_Object = MibTableColumn
ruijieL2TPv2SessionTrafficStatTxPkts = _RuijieL2TPv2SessionTrafficStatTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 3, 1, 6),
    _RuijieL2TPv2SessionTrafficStatTxPkts_Type()
)
ruijieL2TPv2SessionTrafficStatTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionTrafficStatTxPkts.setStatus("current")
_RuijieL2TPv2SessionTrafficStatTxSpeed_Type = Counter64
_RuijieL2TPv2SessionTrafficStatTxSpeed_Object = MibTableColumn
ruijieL2TPv2SessionTrafficStatTxSpeed = _RuijieL2TPv2SessionTrafficStatTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 1, 3, 1, 7),
    _RuijieL2TPv2SessionTrafficStatTxSpeed_Type()
)
ruijieL2TPv2SessionTrafficStatTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionTrafficStatTxSpeed.setStatus("current")
_RuijieL2TPv2Notifications_ObjectIdentity = ObjectIdentity
ruijieL2TPv2Notifications = _RuijieL2TPv2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 2)
)
_RuijieL2TPv2SessionNotifications_ObjectIdentity = ObjectIdentity
ruijieL2TPv2SessionNotifications = _RuijieL2TPv2SessionNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 2, 1)
)
_RuijieL2TPVersion_Type = OctetString
_RuijieL2TPVersion_Object = MibScalar
ruijieL2TPVersion = _RuijieL2TPVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 3),
    _RuijieL2TPVersion_Type()
)
ruijieL2TPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieL2TPVersion.setStatus("current")

# Managed Objects groups


# Notification objects

ruijieL2TPv2SessionStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 2, 1, 1)
)
ruijieL2TPv2SessionStart.setObjects(
      *(("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2TunnelDstIP"),
        ("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2TunnelLocalID"),
        ("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2SessionLocalID"),
        ("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2SessionIMSI"),
        ("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2SessionAccessDeviceID"),
        ("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2SessionSrcIP"),
        ("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2SessionExistTime"),
        ("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2SessionLocalVrf"),
        ("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2SessionDstIP"),
        ("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2TunnelSrcIP"))
)
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionStart.setStatus(
        "current"
    )

ruijieL2TPv2SessionStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 117, 2, 1, 2)
)
ruijieL2TPv2SessionStop.setObjects(
      *(("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2TunnelLocalID"),
        ("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2SessionLocalID"),
        ("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2TunnelSrcIP"),
        ("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2TunnelDstIP"),
        ("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2SessionSrcIP"),
        ("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2SessionDstIP"),
        ("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2SessionLocalVrf"),
        ("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2SessionExistTime"),
        ("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2SessionIMSI"),
        ("RUIJIE-L2TPV2-MIB", "ruijieL2TPv2SessionAccessDeviceID"))
)
if mibBuilder.loadTexts:
    ruijieL2TPv2SessionStop.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-L2TPV2-MIB",
    **{"ruijieL2TPv2MIB": ruijieL2TPv2MIB,
       "ruijieL2TPv2Objects": ruijieL2TPv2Objects,
       "ruijieL2TPv2TunnelTable": ruijieL2TPv2TunnelTable,
       "ruijieL2TPv2TunnelEntry": ruijieL2TPv2TunnelEntry,
       "ruijieL2TPv2TunnelLocalID": ruijieL2TPv2TunnelLocalID,
       "ruijieL2TPv2TunnelRemoteID": ruijieL2TPv2TunnelRemoteID,
       "ruijieL2TPv2TunnelStatus": ruijieL2TPv2TunnelStatus,
       "ruijieL2TPv2TunnelSrcIP": ruijieL2TPv2TunnelSrcIP,
       "ruijieL2TPv2TunnelDstIP": ruijieL2TPv2TunnelDstIP,
       "ruijieL2TPv2TunnelLacHostname": ruijieL2TPv2TunnelLacHostname,
       "ruijieL2TPv2TunnelLacVendor": ruijieL2TPv2TunnelLacVendor,
       "ruijieL2TPv2SessionTable": ruijieL2TPv2SessionTable,
       "ruijieL2TPv2SessionEntry": ruijieL2TPv2SessionEntry,
       "ruijieL2TPv2SessionLocalID": ruijieL2TPv2SessionLocalID,
       "ruijieL2TPv2SessionRemoteID": ruijieL2TPv2SessionRemoteID,
       "ruijieL2TPv2SessionUserName": ruijieL2TPv2SessionUserName,
       "ruijieL2TPv2SessionStatus": ruijieL2TPv2SessionStatus,
       "ruijieL2TPv2SessionSrcIP": ruijieL2TPv2SessionSrcIP,
       "ruijieL2TPv2SessionDstIP": ruijieL2TPv2SessionDstIP,
       "ruijieL2TPv2SessionLocalVrf": ruijieL2TPv2SessionLocalVrf,
       "ruijieL2TPv2SessionExistTime": ruijieL2TPv2SessionExistTime,
       "ruijieL2TPv2SessionIMSI": ruijieL2TPv2SessionIMSI,
       "ruijieL2TPv2SessionAccessDeviceID": ruijieL2TPv2SessionAccessDeviceID,
       "ruijieL2TPv2SessionTrafficStatTable": ruijieL2TPv2SessionTrafficStatTable,
       "ruijieL2TPv2SessionTrafficStatEntry": ruijieL2TPv2SessionTrafficStatEntry,
       "ruijieL2TPv2SessionTrafficStatRxBytes": ruijieL2TPv2SessionTrafficStatRxBytes,
       "ruijieL2TPv2SessionTrafficStatRxPkts": ruijieL2TPv2SessionTrafficStatRxPkts,
       "ruijieL2TPv2SessionTrafficStatRxErrPkts": ruijieL2TPv2SessionTrafficStatRxErrPkts,
       "ruijieL2TPv2SessionTrafficStatRxSpeed": ruijieL2TPv2SessionTrafficStatRxSpeed,
       "ruijieL2TPv2SessionTrafficStatTxBytes": ruijieL2TPv2SessionTrafficStatTxBytes,
       "ruijieL2TPv2SessionTrafficStatTxPkts": ruijieL2TPv2SessionTrafficStatTxPkts,
       "ruijieL2TPv2SessionTrafficStatTxSpeed": ruijieL2TPv2SessionTrafficStatTxSpeed,
       "ruijieL2TPv2Notifications": ruijieL2TPv2Notifications,
       "ruijieL2TPv2SessionNotifications": ruijieL2TPv2SessionNotifications,
       "ruijieL2TPv2SessionStart": ruijieL2TPv2SessionStart,
       "ruijieL2TPv2SessionStop": ruijieL2TPv2SessionStop,
       "ruijieL2TPVersion": ruijieL2TPVersion}
)
