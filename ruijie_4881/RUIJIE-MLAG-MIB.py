# SNMP MIB module (RUIJIE-MLAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-MLAG-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:12 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus",
    "IfIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieMlagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164)
)
if mibBuilder.loadTexts:
    ruijieMlagMIB.setRevisions(
        ("2020-02-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieMlagTraps_ObjectIdentity = ObjectIdentity
ruijieMlagTraps = _RuijieMlagTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1)
)
_RuijieMlagLocalIpv4_Type = IpAddress
_RuijieMlagLocalIpv4_Object = MibScalar
ruijieMlagLocalIpv4 = _RuijieMlagLocalIpv4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1, 1),
    _RuijieMlagLocalIpv4_Type()
)
ruijieMlagLocalIpv4.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMlagLocalIpv4.setStatus("current")
_RuijieMlagPeerIpv4_Type = IpAddress
_RuijieMlagPeerIpv4_Object = MibScalar
ruijieMlagPeerIpv4 = _RuijieMlagPeerIpv4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1, 2),
    _RuijieMlagPeerIpv4_Type()
)
ruijieMlagPeerIpv4.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMlagPeerIpv4.setStatus("current")
_RuijieMlagLocalIpv6_Type = DisplayString
_RuijieMlagLocalIpv6_Object = MibScalar
ruijieMlagLocalIpv6 = _RuijieMlagLocalIpv6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1, 3),
    _RuijieMlagLocalIpv6_Type()
)
ruijieMlagLocalIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMlagLocalIpv6.setStatus("current")
_RuijieMlagPeerIpv6_Type = DisplayString
_RuijieMlagPeerIpv6_Object = MibScalar
ruijieMlagPeerIpv6 = _RuijieMlagPeerIpv6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1, 4),
    _RuijieMlagPeerIpv6_Type()
)
ruijieMlagPeerIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMlagPeerIpv6.setStatus("current")
_RuijieMlagLocalMac_Type = MacAddress
_RuijieMlagLocalMac_Object = MibScalar
ruijieMlagLocalMac = _RuijieMlagLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1, 9),
    _RuijieMlagLocalMac_Type()
)
ruijieMlagLocalMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMlagLocalMac.setStatus("current")
_RuijieMlagPeerMac_Type = MacAddress
_RuijieMlagPeerMac_Object = MibScalar
ruijieMlagPeerMac = _RuijieMlagPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1, 10),
    _RuijieMlagPeerMac_Type()
)
ruijieMlagPeerMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMlagPeerMac.setStatus("current")
_RuijieMlagConsistencyType1_Type = DisplayString
_RuijieMlagConsistencyType1_Object = MibScalar
ruijieMlagConsistencyType1 = _RuijieMlagConsistencyType1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1, 11),
    _RuijieMlagConsistencyType1_Type()
)
ruijieMlagConsistencyType1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMlagConsistencyType1.setStatus("current")
_RuijieMlagConsistencyType2_Type = DisplayString
_RuijieMlagConsistencyType2_Object = MibScalar
ruijieMlagConsistencyType2 = _RuijieMlagConsistencyType2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1, 12),
    _RuijieMlagConsistencyType2_Type()
)
ruijieMlagConsistencyType2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMlagConsistencyType2.setStatus("current")

# Managed Objects groups


# Notification objects

ruijieMlagDualActiveDetectTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1, 5)
)
ruijieMlagDualActiveDetectTraps.setObjects(
      *(("RUIJIE-MLAG-MIB", "ruijieMlagLocalIpv4"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagPeerIpv4"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagLocalIpv6"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagPeerIpv6"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagLocalMac"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagPeerMac"))
)
if mibBuilder.loadTexts:
    ruijieMlagDualActiveDetectTraps.setStatus(
        "current"
    )

ruijieMlagDualActiveRecoverTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1, 6)
)
ruijieMlagDualActiveRecoverTraps.setObjects(
      *(("RUIJIE-MLAG-MIB", "ruijieMlagLocalIpv4"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagPeerIpv4"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagLocalIpv6"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagPeerIpv6"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagLocalMac"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagPeerMac"))
)
if mibBuilder.loadTexts:
    ruijieMlagDualActiveRecoverTraps.setStatus(
        "current"
    )

ruijieMlagDataSyncDisconnectTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1, 7)
)
ruijieMlagDataSyncDisconnectTraps.setObjects(
      *(("RUIJIE-MLAG-MIB", "ruijieMlagLocalIpv4"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagPeerIpv4"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagLocalIpv6"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagPeerIpv6"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagLocalMac"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagPeerMac"))
)
if mibBuilder.loadTexts:
    ruijieMlagDataSyncDisconnectTraps.setStatus(
        "current"
    )

ruijieMlagDataSyncConnectTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1, 8)
)
ruijieMlagDataSyncConnectTraps.setObjects(
      *(("RUIJIE-MLAG-MIB", "ruijieMlagLocalIpv4"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagPeerIpv4"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagLocalIpv6"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagPeerIpv6"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagLocalMac"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagPeerMac"))
)
if mibBuilder.loadTexts:
    ruijieMlagDataSyncConnectTraps.setStatus(
        "current"
    )

ruijieMlagKeepaliveDisconnectTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1, 13)
)
ruijieMlagKeepaliveDisconnectTraps.setObjects(
      *(("RUIJIE-MLAG-MIB", "ruijieMlagLocalIpv4"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagPeerIpv4"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagLocalIpv6"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagPeerIpv6"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagLocalMac"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagPeerMac"))
)
if mibBuilder.loadTexts:
    ruijieMlagKeepaliveDisconnectTraps.setStatus(
        "current"
    )

ruijieMlagKeepaliveConnectTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1, 14)
)
ruijieMlagKeepaliveConnectTraps.setObjects(
      *(("RUIJIE-MLAG-MIB", "ruijieMlagLocalIpv4"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagPeerIpv4"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagLocalIpv6"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagPeerIpv6"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagLocalMac"),
        ("RUIJIE-MLAG-MIB", "ruijieMlagPeerMac"))
)
if mibBuilder.loadTexts:
    ruijieMlagKeepaliveConnectTraps.setStatus(
        "current"
    )

ruijieMlagConsistencyCheckType1Traps = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1, 15)
)
ruijieMlagConsistencyCheckType1Traps.setObjects(
    ("RUIJIE-MLAG-MIB", "ruijieMlagConsistencyType1")
)
if mibBuilder.loadTexts:
    ruijieMlagConsistencyCheckType1Traps.setStatus(
        "current"
    )

ruijieMlagConsistencyCheckType1ResumeTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1, 16)
)
ruijieMlagConsistencyCheckType1ResumeTraps.setObjects(
    ("RUIJIE-MLAG-MIB", "ruijieMlagConsistencyType1")
)
if mibBuilder.loadTexts:
    ruijieMlagConsistencyCheckType1ResumeTraps.setStatus(
        "current"
    )

ruijieMlagConsistencyCheckType2Traps = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1, 17)
)
ruijieMlagConsistencyCheckType2Traps.setObjects(
    ("RUIJIE-MLAG-MIB", "ruijieMlagConsistencyType2")
)
if mibBuilder.loadTexts:
    ruijieMlagConsistencyCheckType2Traps.setStatus(
        "current"
    )

ruijieMlagConsistencyCheckType2ResumeTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 164, 1, 18)
)
ruijieMlagConsistencyCheckType2ResumeTraps.setObjects(
    ("RUIJIE-MLAG-MIB", "ruijieMlagConsistencyType2")
)
if mibBuilder.loadTexts:
    ruijieMlagConsistencyCheckType2ResumeTraps.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-MLAG-MIB",
    **{"ruijieMlagMIB": ruijieMlagMIB,
       "ruijieMlagTraps": ruijieMlagTraps,
       "ruijieMlagLocalIpv4": ruijieMlagLocalIpv4,
       "ruijieMlagPeerIpv4": ruijieMlagPeerIpv4,
       "ruijieMlagLocalIpv6": ruijieMlagLocalIpv6,
       "ruijieMlagPeerIpv6": ruijieMlagPeerIpv6,
       "ruijieMlagDualActiveDetectTraps": ruijieMlagDualActiveDetectTraps,
       "ruijieMlagDualActiveRecoverTraps": ruijieMlagDualActiveRecoverTraps,
       "ruijieMlagDataSyncDisconnectTraps": ruijieMlagDataSyncDisconnectTraps,
       "ruijieMlagDataSyncConnectTraps": ruijieMlagDataSyncConnectTraps,
       "ruijieMlagLocalMac": ruijieMlagLocalMac,
       "ruijieMlagPeerMac": ruijieMlagPeerMac,
       "ruijieMlagConsistencyType1": ruijieMlagConsistencyType1,
       "ruijieMlagConsistencyType2": ruijieMlagConsistencyType2,
       "ruijieMlagKeepaliveDisconnectTraps": ruijieMlagKeepaliveDisconnectTraps,
       "ruijieMlagKeepaliveConnectTraps": ruijieMlagKeepaliveConnectTraps,
       "ruijieMlagConsistencyCheckType1Traps": ruijieMlagConsistencyCheckType1Traps,
       "ruijieMlagConsistencyCheckType1ResumeTraps": ruijieMlagConsistencyCheckType1ResumeTraps,
       "ruijieMlagConsistencyCheckType2Traps": ruijieMlagConsistencyCheckType2Traps,
       "ruijieMlagConsistencyCheckType2ResumeTraps": ruijieMlagConsistencyCheckType2ResumeTraps}
)
