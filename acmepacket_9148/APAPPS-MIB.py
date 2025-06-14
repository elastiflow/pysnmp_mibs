# SNMP MIB module (APAPPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/acmepacket_9148/APAPPS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:10:25 2025
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

(ApHardwareModuleFamily,
 ApPhyPortType,
 ApPresence,
 ApRedundancyState,
 ApServerStatus) = mibBuilder.importSymbols(
    "ACMEPACKET-TC",
    "ApHardwareModuleFamily",
    "ApPhyPortType",
    "ApPresence",
    "ApRedundancyState",
    "ApServerStatus")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

apAppsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16)
)
if mibBuilder.loadTexts:
    apAppsModule.setRevisions(
        ("2012-03-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApAppsMIBObjects_ObjectIdentity = ObjectIdentity
apAppsMIBObjects = _ApAppsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1)
)
_ApAppsMIBGeneralObjects_ObjectIdentity = ObjectIdentity
apAppsMIBGeneralObjects = _ApAppsMIBGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 1)
)
_ApAppsMIBTabularObjects_ObjectIdentity = ObjectIdentity
apAppsMIBTabularObjects = _ApAppsMIBTabularObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2)
)
_ApAppsENUMTabularObjects_ObjectIdentity = ObjectIdentity
apAppsENUMTabularObjects = _ApAppsENUMTabularObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1)
)
_ApAppsENUMServerStatusTable_Object = MibTable
apAppsENUMServerStatusTable = _ApAppsENUMServerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    apAppsENUMServerStatusTable.setStatus("current")
_ApAppsENUMServerStatusEntry_Object = MibTableRow
apAppsENUMServerStatusEntry = _ApAppsENUMServerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 1, 1)
)
apAppsENUMServerStatusEntry.setIndexNames(
    (0, "APAPPS-MIB", "apAppsENUMConfigName"),
    (0, "APAPPS-MIB", "apAppsENUMServerInetAddressType"),
    (0, "APAPPS-MIB", "apAppsENUMServerInetAddress"),
)
if mibBuilder.loadTexts:
    apAppsENUMServerStatusEntry.setStatus("current")
_ApAppsENUMConfigName_Type = DisplayString
_ApAppsENUMConfigName_Object = MibTableColumn
apAppsENUMConfigName = _ApAppsENUMConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 1, 1, 1),
    _ApAppsENUMConfigName_Type()
)
apAppsENUMConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAppsENUMConfigName.setStatus("current")
_ApAppsENUMServerInetAddressType_Type = InetAddressType
_ApAppsENUMServerInetAddressType_Object = MibTableColumn
apAppsENUMServerInetAddressType = _ApAppsENUMServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 1, 1, 2),
    _ApAppsENUMServerInetAddressType_Type()
)
apAppsENUMServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAppsENUMServerInetAddressType.setStatus("current")
_ApAppsENUMServerInetAddress_Type = InetAddress
_ApAppsENUMServerInetAddress_Object = MibTableColumn
apAppsENUMServerInetAddress = _ApAppsENUMServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 1, 1, 3),
    _ApAppsENUMServerInetAddress_Type()
)
apAppsENUMServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAppsENUMServerInetAddress.setStatus("current")
_ApAppsENUMServerStatus_Type = ApServerStatus
_ApAppsENUMServerStatus_Object = MibTableColumn
apAppsENUMServerStatus = _ApAppsENUMServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 1, 1, 4),
    _ApAppsENUMServerStatus_Type()
)
apAppsENUMServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAppsENUMServerStatus.setStatus("current")
_ApEnumServerRateStatsTable_Object = MibTable
apEnumServerRateStatsTable = _ApEnumServerRateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    apEnumServerRateStatsTable.setStatus("current")
_ApEnumServerRateStatsEntry_Object = MibTableRow
apEnumServerRateStatsEntry = _ApEnumServerRateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    apEnumServerRateStatsEntry.setStatus("current")
_ApEnumServerRateMsgRcvd_Type = Gauge32
_ApEnumServerRateMsgRcvd_Object = MibTableColumn
apEnumServerRateMsgRcvd = _ApEnumServerRateMsgRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 2, 1, 5),
    _ApEnumServerRateMsgRcvd_Type()
)
apEnumServerRateMsgRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnumServerRateMsgRcvd.setStatus("current")
if mibBuilder.loadTexts:
    apEnumServerRateMsgRcvd.setUnits("messages per 10 seconds")
_ApEnumServerRateMsgSent_Type = Gauge32
_ApEnumServerRateMsgSent_Object = MibTableColumn
apEnumServerRateMsgSent = _ApEnumServerRateMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 2, 1, 6),
    _ApEnumServerRateMsgSent_Type()
)
apEnumServerRateMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnumServerRateMsgSent.setStatus("current")
if mibBuilder.loadTexts:
    apEnumServerRateMsgSent.setUnits("messages per 10 seconds")
_ApEnumServerRateReqRcvd_Type = Gauge32
_ApEnumServerRateReqRcvd_Object = MibTableColumn
apEnumServerRateReqRcvd = _ApEnumServerRateReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 2, 1, 7),
    _ApEnumServerRateReqRcvd_Type()
)
apEnumServerRateReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnumServerRateReqRcvd.setStatus("current")
if mibBuilder.loadTexts:
    apEnumServerRateReqRcvd.setUnits("messages per 10 seconds")
_ApEnumServerRateReqSent_Type = Gauge32
_ApEnumServerRateReqSent_Object = MibTableColumn
apEnumServerRateReqSent = _ApEnumServerRateReqSent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 2, 1, 8),
    _ApEnumServerRateReqSent_Type()
)
apEnumServerRateReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnumServerRateReqSent.setStatus("current")
if mibBuilder.loadTexts:
    apEnumServerRateReqSent.setUnits("messages per 10 seconds")
_ApEnumServerRateRspRcvd_Type = Gauge32
_ApEnumServerRateRspRcvd_Object = MibTableColumn
apEnumServerRateRspRcvd = _ApEnumServerRateRspRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 2, 1, 9),
    _ApEnumServerRateRspRcvd_Type()
)
apEnumServerRateRspRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnumServerRateRspRcvd.setStatus("current")
if mibBuilder.loadTexts:
    apEnumServerRateRspRcvd.setUnits("messages per 10 seconds")
_ApEnumServerRateRspSent_Type = Gauge32
_ApEnumServerRateRspSent_Object = MibTableColumn
apEnumServerRateRspSent = _ApEnumServerRateRspSent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 1, 2, 1, 10),
    _ApEnumServerRateRspSent_Type()
)
apEnumServerRateRspSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnumServerRateRspSent.setStatus("current")
if mibBuilder.loadTexts:
    apEnumServerRateRspSent.setUnits("messages per 10 seconds")
_ApAppsDNSTabularObjects_ObjectIdentity = ObjectIdentity
apAppsDNSTabularObjects = _ApAppsDNSTabularObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 2)
)
_ApAppsDnsServerStatusTable_Object = MibTable
apAppsDnsServerStatusTable = _ApAppsDnsServerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    apAppsDnsServerStatusTable.setStatus("current")
_ApAppsDnsServerStatusEntry_Object = MibTableRow
apAppsDnsServerStatusEntry = _ApAppsDnsServerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 2, 1, 1)
)
apAppsDnsServerStatusEntry.setIndexNames(
    (0, "APAPPS-MIB", "apAppsDnsInterfaceName"),
    (0, "APAPPS-MIB", "apAppsDnsServerInetAddressType"),
    (0, "APAPPS-MIB", "apAppsDnsServerInetAddress"),
)
if mibBuilder.loadTexts:
    apAppsDnsServerStatusEntry.setStatus("current")


class _ApAppsDnsInterfaceName_Type(DisplayString):
    """Custom type apAppsDnsInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApAppsDnsInterfaceName_Type.__name__ = "DisplayString"
_ApAppsDnsInterfaceName_Object = MibTableColumn
apAppsDnsInterfaceName = _ApAppsDnsInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 2, 1, 1, 1),
    _ApAppsDnsInterfaceName_Type()
)
apAppsDnsInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAppsDnsInterfaceName.setStatus("current")
_ApAppsDnsServerInetAddressType_Type = InetAddressType
_ApAppsDnsServerInetAddressType_Object = MibTableColumn
apAppsDnsServerInetAddressType = _ApAppsDnsServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 2, 1, 1, 2),
    _ApAppsDnsServerInetAddressType_Type()
)
apAppsDnsServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAppsDnsServerInetAddressType.setStatus("current")
_ApAppsDnsServerInetAddress_Type = InetAddress
_ApAppsDnsServerInetAddress_Object = MibTableColumn
apAppsDnsServerInetAddress = _ApAppsDnsServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 2, 1, 1, 3),
    _ApAppsDnsServerInetAddress_Type()
)
apAppsDnsServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAppsDnsServerInetAddress.setStatus("current")
_ApAppsDnsServerStatus_Type = ApServerStatus
_ApAppsDnsServerStatus_Object = MibTableColumn
apAppsDnsServerStatus = _ApAppsDnsServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 1, 2, 2, 1, 1, 4),
    _ApAppsDnsServerStatus_Type()
)
apAppsDnsServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAppsDnsServerStatus.setStatus("current")
_ApAppsNotificationObjects_ObjectIdentity = ObjectIdentity
apAppsNotificationObjects = _ApAppsNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 2)
)
_ApAppsNotifObjects_ObjectIdentity = ObjectIdentity
apAppsNotifObjects = _ApAppsNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 1)
)
_ApAppsNotifPrefix_ObjectIdentity = ObjectIdentity
apAppsNotifPrefix = _ApAppsNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2)
)
_ApAppsEnumNotif_ObjectIdentity = ObjectIdentity
apAppsEnumNotif = _ApAppsEnumNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 1)
)
_ApAppsEnumNotifications_ObjectIdentity = ObjectIdentity
apAppsEnumNotifications = _ApAppsEnumNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 1, 0)
)
_ApAppsDnsNotif_ObjectIdentity = ObjectIdentity
apAppsDnsNotif = _ApAppsDnsNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 2)
)
_ApAppsDnsNotifications_ObjectIdentity = ObjectIdentity
apAppsDnsNotifications = _ApAppsDnsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 2, 0)
)
_ApAppsConformance_ObjectIdentity = ObjectIdentity
apAppsConformance = _ApAppsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 3)
)
_ApAppsObjectGroups_ObjectIdentity = ObjectIdentity
apAppsObjectGroups = _ApAppsObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 3, 1)
)
_ApAppsNotificationGroups_ObjectIdentity = ObjectIdentity
apAppsNotificationGroups = _ApAppsNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 3, 2)
)
apAppsENUMServerStatusEntry.registerAugmentions(
    ("APAPPS-MIB",
     "apEnumServerRateStatsEntry")
)
apEnumServerRateStatsEntry.setIndexNames(*apAppsENUMServerStatusEntry.getIndexNames())

# Managed Objects groups

apAppsENUMServerStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 3, 1, 1)
)
apAppsENUMServerStatusGroup.setObjects(
      *(("APAPPS-MIB", "apAppsENUMConfigName"),
        ("APAPPS-MIB", "apAppsENUMServerInetAddressType"),
        ("APAPPS-MIB", "apAppsENUMServerInetAddress"),
        ("APAPPS-MIB", "apAppsENUMServerStatus"))
)
if mibBuilder.loadTexts:
    apAppsENUMServerStatusGroup.setStatus("current")

apAppsDnsServerStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 3, 1, 2)
)
apAppsDnsServerStatusGroup.setObjects(
      *(("APAPPS-MIB", "apAppsDnsInterfaceName"),
        ("APAPPS-MIB", "apAppsDnsServerInetAddressType"),
        ("APAPPS-MIB", "apAppsDnsServerInetAddress"),
        ("APAPPS-MIB", "apAppsDnsServerStatus"))
)
if mibBuilder.loadTexts:
    apAppsDnsServerStatusGroup.setStatus("current")

apAppsENUMServerRateStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 3, 1, 3)
)
apAppsENUMServerRateStatsGroup.setObjects(
      *(("APAPPS-MIB", "apEnumServerRateMsgRcvd"),
        ("APAPPS-MIB", "apEnumServerRateMsgSent"),
        ("APAPPS-MIB", "apEnumServerRateReqRcvd"),
        ("APAPPS-MIB", "apEnumServerRateReqSent"),
        ("APAPPS-MIB", "apEnumServerRateRspRcvd"),
        ("APAPPS-MIB", "apEnumServerRateRspSent"))
)
if mibBuilder.loadTexts:
    apAppsENUMServerRateStatsGroup.setStatus("current")


# Notification objects

apAppsENUMServerStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 1, 0, 1)
)
apAppsENUMServerStatusChangeTrap.setObjects(
      *(("APAPPS-MIB", "apAppsENUMConfigName"),
        ("APAPPS-MIB", "apAppsENUMServerInetAddressType"),
        ("APAPPS-MIB", "apAppsENUMServerInetAddress"),
        ("APAPPS-MIB", "apAppsENUMServerStatus"))
)
if mibBuilder.loadTexts:
    apAppsENUMServerStatusChangeTrap.setStatus(
        "current"
    )

apAppsDnsServerStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 2, 2, 2, 0, 1)
)
apAppsDnsServerStatusChangeTrap.setObjects(
      *(("APAPPS-MIB", "apAppsDnsInterfaceName"),
        ("APAPPS-MIB", "apAppsDnsServerInetAddressType"),
        ("APAPPS-MIB", "apAppsDnsServerInetAddress"),
        ("APAPPS-MIB", "apAppsDnsServerStatus"))
)
if mibBuilder.loadTexts:
    apAppsDnsServerStatusChangeTrap.setStatus(
        "current"
    )


# Notifications groups

apAppsEnumServerNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 3, 2, 1)
)
apAppsEnumServerNotificationsGroup.setObjects(
    ("APAPPS-MIB", "apAppsENUMServerStatusChangeTrap")
)
if mibBuilder.loadTexts:
    apAppsEnumServerNotificationsGroup.setStatus(
        "current"
    )

apAppsDnsServerNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 16, 3, 2, 2)
)
apAppsDnsServerNotificationsGroup.setObjects(
    ("APAPPS-MIB", "apAppsDnsServerStatusChangeTrap")
)
if mibBuilder.loadTexts:
    apAppsDnsServerNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APAPPS-MIB",
    **{"apAppsModule": apAppsModule,
       "apAppsMIBObjects": apAppsMIBObjects,
       "apAppsMIBGeneralObjects": apAppsMIBGeneralObjects,
       "apAppsMIBTabularObjects": apAppsMIBTabularObjects,
       "apAppsENUMTabularObjects": apAppsENUMTabularObjects,
       "apAppsENUMServerStatusTable": apAppsENUMServerStatusTable,
       "apAppsENUMServerStatusEntry": apAppsENUMServerStatusEntry,
       "apAppsENUMConfigName": apAppsENUMConfigName,
       "apAppsENUMServerInetAddressType": apAppsENUMServerInetAddressType,
       "apAppsENUMServerInetAddress": apAppsENUMServerInetAddress,
       "apAppsENUMServerStatus": apAppsENUMServerStatus,
       "apEnumServerRateStatsTable": apEnumServerRateStatsTable,
       "apEnumServerRateStatsEntry": apEnumServerRateStatsEntry,
       "apEnumServerRateMsgRcvd": apEnumServerRateMsgRcvd,
       "apEnumServerRateMsgSent": apEnumServerRateMsgSent,
       "apEnumServerRateReqRcvd": apEnumServerRateReqRcvd,
       "apEnumServerRateReqSent": apEnumServerRateReqSent,
       "apEnumServerRateRspRcvd": apEnumServerRateRspRcvd,
       "apEnumServerRateRspSent": apEnumServerRateRspSent,
       "apAppsDNSTabularObjects": apAppsDNSTabularObjects,
       "apAppsDnsServerStatusTable": apAppsDnsServerStatusTable,
       "apAppsDnsServerStatusEntry": apAppsDnsServerStatusEntry,
       "apAppsDnsInterfaceName": apAppsDnsInterfaceName,
       "apAppsDnsServerInetAddressType": apAppsDnsServerInetAddressType,
       "apAppsDnsServerInetAddress": apAppsDnsServerInetAddress,
       "apAppsDnsServerStatus": apAppsDnsServerStatus,
       "apAppsNotificationObjects": apAppsNotificationObjects,
       "apAppsNotifObjects": apAppsNotifObjects,
       "apAppsNotifPrefix": apAppsNotifPrefix,
       "apAppsEnumNotif": apAppsEnumNotif,
       "apAppsEnumNotifications": apAppsEnumNotifications,
       "apAppsENUMServerStatusChangeTrap": apAppsENUMServerStatusChangeTrap,
       "apAppsDnsNotif": apAppsDnsNotif,
       "apAppsDnsNotifications": apAppsDnsNotifications,
       "apAppsDnsServerStatusChangeTrap": apAppsDnsServerStatusChangeTrap,
       "apAppsConformance": apAppsConformance,
       "apAppsObjectGroups": apAppsObjectGroups,
       "apAppsENUMServerStatusGroup": apAppsENUMServerStatusGroup,
       "apAppsDnsServerStatusGroup": apAppsDnsServerStatusGroup,
       "apAppsENUMServerRateStatsGroup": apAppsENUMServerRateStatsGroup,
       "apAppsNotificationGroups": apAppsNotificationGroups,
       "apAppsEnumServerNotificationsGroup": apAppsEnumServerNotificationsGroup,
       "apAppsDnsServerNotificationsGroup": apAppsDnsServerNotificationsGroup}
)
