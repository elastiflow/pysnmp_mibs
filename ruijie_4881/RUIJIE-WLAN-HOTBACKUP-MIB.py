# SNMP MIB module (RUIJIE-WLAN-HOTBACKUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-WLAN-HOTBACKUP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:52:30 2025
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

ruijieWlanHotbackupMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115)
)
if mibBuilder.loadTexts:
    ruijieWlanHotbackupMIB.setRevisions(
        ("2012-07-31 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieWlanHotbackupMIBObjects_ObjectIdentity = ObjectIdentity
ruijieWlanHotbackupMIBObjects = _RuijieWlanHotbackupMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 1)
)
_RuijieWlanHotbackupPeerTable_Object = MibTable
ruijieWlanHotbackupPeerTable = _RuijieWlanHotbackupPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieWlanHotbackupPeerTable.setStatus("current")
_RuijieWlanHotbackupPeerEntry_Object = MibTableRow
ruijieWlanHotbackupPeerEntry = _RuijieWlanHotbackupPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 1, 1, 1)
)
ruijieWlanHotbackupPeerEntry.setIndexNames(
    (0, "RUIJIE-WLAN-HOTBACKUP-MIB", "ruijieWlanHotbackupIpAddress"),
)
if mibBuilder.loadTexts:
    ruijieWlanHotbackupPeerEntry.setStatus("current")
_RuijieWlanHotbackupIpAddress_Type = IpAddress
_RuijieWlanHotbackupIpAddress_Object = MibTableColumn
ruijieWlanHotbackupIpAddress = _RuijieWlanHotbackupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 1, 1, 1, 1),
    _RuijieWlanHotbackupIpAddress_Type()
)
ruijieWlanHotbackupIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieWlanHotbackupIpAddress.setStatus("current")


class _RuijieWlanHotbackupIsEnabled_Type(Integer32):
    """Custom type ruijieWlanHotbackupIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieWlanHotbackupIsEnabled_Type.__name__ = "Integer32"
_RuijieWlanHotbackupIsEnabled_Object = MibTableColumn
ruijieWlanHotbackupIsEnabled = _RuijieWlanHotbackupIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 1, 1, 1, 2),
    _RuijieWlanHotbackupIsEnabled_Type()
)
ruijieWlanHotbackupIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWlanHotbackupIsEnabled.setStatus("current")


class _RuijieWlanHotbackupState_Type(Integer32):
    """Custom type ruijieWlanHotbackupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("hb-disable", 1),
          ("probe", 2),
          ("hdsk", 3),
          ("tcp-connect", 4),
          ("sulking", 5),
          ("channel-up", 6))
    )


_RuijieWlanHotbackupState_Type.__name__ = "Integer32"
_RuijieWlanHotbackupState_Object = MibTableColumn
ruijieWlanHotbackupState = _RuijieWlanHotbackupState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 1, 1, 1, 3),
    _RuijieWlanHotbackupState_Type()
)
ruijieWlanHotbackupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWlanHotbackupState.setStatus("current")
_RuijieWlanHotbackupContextTable_Object = MibTable
ruijieWlanHotbackupContextTable = _RuijieWlanHotbackupContextTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieWlanHotbackupContextTable.setStatus("current")
_RuijieWlanHotbackupContextEntry_Object = MibTableRow
ruijieWlanHotbackupContextEntry = _RuijieWlanHotbackupContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 1, 2, 1)
)
ruijieWlanHotbackupContextEntry.setIndexNames(
    (0, "RUIJIE-WLAN-HOTBACKUP-MIB", "ruijieWlanHotbackupCtxIpAddress"),
    (0, "RUIJIE-WLAN-HOTBACKUP-MIB", "ruijieWlanHotbackupContextId"),
)
if mibBuilder.loadTexts:
    ruijieWlanHotbackupContextEntry.setStatus("current")
_RuijieWlanHotbackupCtxIpAddress_Type = IpAddress
_RuijieWlanHotbackupCtxIpAddress_Object = MibTableColumn
ruijieWlanHotbackupCtxIpAddress = _RuijieWlanHotbackupCtxIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 1, 2, 1, 1),
    _RuijieWlanHotbackupCtxIpAddress_Type()
)
ruijieWlanHotbackupCtxIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWlanHotbackupCtxIpAddress.setStatus("current")
_RuijieWlanHotbackupContextId_Type = Integer32
_RuijieWlanHotbackupContextId_Object = MibTableColumn
ruijieWlanHotbackupContextId = _RuijieWlanHotbackupContextId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 1, 2, 1, 2),
    _RuijieWlanHotbackupContextId_Type()
)
ruijieWlanHotbackupContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWlanHotbackupContextId.setStatus("current")


class _RuijieWlanHotbackupContextState_Type(Integer32):
    """Custom type ruijieWlanHotbackupContextState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("unknown", 1),
          ("single-active", 2),
          ("single-standby", 3),
          ("pair-active", 4),
          ("pair-standby", 5))
    )


_RuijieWlanHotbackupContextState_Type.__name__ = "Integer32"
_RuijieWlanHotbackupContextState_Object = MibTableColumn
ruijieWlanHotbackupContextState = _RuijieWlanHotbackupContextState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 1, 2, 1, 3),
    _RuijieWlanHotbackupContextState_Type()
)
ruijieWlanHotbackupContextState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWlanHotbackupContextState.setStatus("current")
_RuijieWlanHotbackupNotificationsMIBObjects_ObjectIdentity = ObjectIdentity
ruijieWlanHotbackupNotificationsMIBObjects = _RuijieWlanHotbackupNotificationsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 2)
)
_RuijieWlanHotbackupNtfObjects_ObjectIdentity = ObjectIdentity
ruijieWlanHotbackupNtfObjects = _RuijieWlanHotbackupNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 2, 1)
)
_RuijieNotifyPeerIpType_Type = InetAddressType
_RuijieNotifyPeerIpType_Object = MibScalar
ruijieNotifyPeerIpType = _RuijieNotifyPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 2, 1, 1),
    _RuijieNotifyPeerIpType_Type()
)
ruijieNotifyPeerIpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyPeerIpType.setStatus("current")
_RuijieNotifyPeerIp_Type = InetAddress
_RuijieNotifyPeerIp_Object = MibScalar
ruijieNotifyPeerIp = _RuijieNotifyPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 2, 1, 2),
    _RuijieNotifyPeerIp_Type()
)
ruijieNotifyPeerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyPeerIp.setStatus("current")


class _RuijieNotifyCtxId_Type(Integer32):
    """Custom type ruijieNotifyCtxId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieNotifyCtxId_Type.__name__ = "Integer32"
_RuijieNotifyCtxId_Object = MibScalar
ruijieNotifyCtxId = _RuijieNotifyCtxId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 2, 1, 3),
    _RuijieNotifyCtxId_Type()
)
ruijieNotifyCtxId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyCtxId.setStatus("current")


class _RuijieNotifyOldState_Type(Integer32):
    """Custom type ruijieNotifyOldState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("unknown", 1),
          ("single-active", 2),
          ("single-standby", 3),
          ("pair-active", 4),
          ("pair-standby", 5))
    )


_RuijieNotifyOldState_Type.__name__ = "Integer32"
_RuijieNotifyOldState_Object = MibScalar
ruijieNotifyOldState = _RuijieNotifyOldState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 2, 1, 4),
    _RuijieNotifyOldState_Type()
)
ruijieNotifyOldState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyOldState.setStatus("current")


class _RuijieNotifyNewState_Type(Integer32):
    """Custom type ruijieNotifyNewState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("unknown", 1),
          ("single-active", 2),
          ("single-standby", 3),
          ("pair-active", 4),
          ("pair-standby", 5))
    )


_RuijieNotifyNewState_Type.__name__ = "Integer32"
_RuijieNotifyNewState_Object = MibScalar
ruijieNotifyNewState = _RuijieNotifyNewState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 2, 1, 5),
    _RuijieNotifyNewState_Type()
)
ruijieNotifyNewState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyNewState.setStatus("current")
_RuijieWlanHotbackupNotifications_ObjectIdentity = ObjectIdentity
ruijieWlanHotbackupNotifications = _RuijieWlanHotbackupNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 2, 2)
)

# Managed Objects groups


# Notification objects

ruijieNotifyWlanHBChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 115, 2, 2, 1)
)
ruijieNotifyWlanHBChange.setObjects(
      *(("RUIJIE-WLAN-HOTBACKUP-MIB", "ruijieNotifyPeerIpType"),
        ("RUIJIE-WLAN-HOTBACKUP-MIB", "ruijieNotifyPeerIp"),
        ("RUIJIE-WLAN-HOTBACKUP-MIB", "ruijieNotifyCtxId"),
        ("RUIJIE-WLAN-HOTBACKUP-MIB", "ruijieNotifyOldState"),
        ("RUIJIE-WLAN-HOTBACKUP-MIB", "ruijieNotifyNewState"))
)
if mibBuilder.loadTexts:
    ruijieNotifyWlanHBChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-WLAN-HOTBACKUP-MIB",
    **{"ruijieWlanHotbackupMIB": ruijieWlanHotbackupMIB,
       "ruijieWlanHotbackupMIBObjects": ruijieWlanHotbackupMIBObjects,
       "ruijieWlanHotbackupPeerTable": ruijieWlanHotbackupPeerTable,
       "ruijieWlanHotbackupPeerEntry": ruijieWlanHotbackupPeerEntry,
       "ruijieWlanHotbackupIpAddress": ruijieWlanHotbackupIpAddress,
       "ruijieWlanHotbackupIsEnabled": ruijieWlanHotbackupIsEnabled,
       "ruijieWlanHotbackupState": ruijieWlanHotbackupState,
       "ruijieWlanHotbackupContextTable": ruijieWlanHotbackupContextTable,
       "ruijieWlanHotbackupContextEntry": ruijieWlanHotbackupContextEntry,
       "ruijieWlanHotbackupCtxIpAddress": ruijieWlanHotbackupCtxIpAddress,
       "ruijieWlanHotbackupContextId": ruijieWlanHotbackupContextId,
       "ruijieWlanHotbackupContextState": ruijieWlanHotbackupContextState,
       "ruijieWlanHotbackupNotificationsMIBObjects": ruijieWlanHotbackupNotificationsMIBObjects,
       "ruijieWlanHotbackupNtfObjects": ruijieWlanHotbackupNtfObjects,
       "ruijieNotifyPeerIpType": ruijieNotifyPeerIpType,
       "ruijieNotifyPeerIp": ruijieNotifyPeerIp,
       "ruijieNotifyCtxId": ruijieNotifyCtxId,
       "ruijieNotifyOldState": ruijieNotifyOldState,
       "ruijieNotifyNewState": ruijieNotifyNewState,
       "ruijieWlanHotbackupNotifications": ruijieWlanHotbackupNotifications,
       "ruijieNotifyWlanHBChange": ruijieNotifyWlanHBChange}
)
