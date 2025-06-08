# SNMP MIB module (RUIJIE-IP-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-IP-PRIVATE-MIB.mib
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieIPPrivateMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73)
)
if mibBuilder.loadTexts:
    ruijieIPPrivateMgmt.setRevisions(
        ("2009-09-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieIPPrivateAcNotificationsMIBObjects_ObjectIdentity = ObjectIdentity
ruijieIPPrivateAcNotificationsMIBObjects = _RuijieIPPrivateAcNotificationsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 1)
)
_RuijieIPPrivateAcNtfObjects_ObjectIdentity = ObjectIdentity
ruijieIPPrivateAcNtfObjects = _RuijieIPPrivateAcNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 1, 1)
)
_RuijieIPPrivateAcNotifyIpv4AddressChangeType_Type = Integer32
_RuijieIPPrivateAcNotifyIpv4AddressChangeType_Object = MibScalar
ruijieIPPrivateAcNotifyIpv4AddressChangeType = _RuijieIPPrivateAcNotifyIpv4AddressChangeType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 1, 1, 1),
    _RuijieIPPrivateAcNotifyIpv4AddressChangeType_Type()
)
ruijieIPPrivateAcNotifyIpv4AddressChangeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieIPPrivateAcNotifyIpv4AddressChangeType.setStatus("current")
_RuijieIPPrivateAcNotifyIpv4ChangeAddress_Type = IpAddress
_RuijieIPPrivateAcNotifyIpv4ChangeAddress_Object = MibScalar
ruijieIPPrivateAcNotifyIpv4ChangeAddress = _RuijieIPPrivateAcNotifyIpv4ChangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 1, 1, 2),
    _RuijieIPPrivateAcNotifyIpv4ChangeAddress_Type()
)
ruijieIPPrivateAcNotifyIpv4ChangeAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieIPPrivateAcNotifyIpv4ChangeAddress.setStatus("current")
_RuijieIPPrivateAcNotifyIpv4ChangeAddressMask_Type = IpAddress
_RuijieIPPrivateAcNotifyIpv4ChangeAddressMask_Object = MibScalar
ruijieIPPrivateAcNotifyIpv4ChangeAddressMask = _RuijieIPPrivateAcNotifyIpv4ChangeAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 1, 1, 3),
    _RuijieIPPrivateAcNotifyIpv4ChangeAddressMask_Type()
)
ruijieIPPrivateAcNotifyIpv4ChangeAddressMask.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieIPPrivateAcNotifyIpv4ChangeAddressMask.setStatus("current")
_RuijieIPPrivateAcNotifyIpv4ChangeIfIndex_Type = Integer32
_RuijieIPPrivateAcNotifyIpv4ChangeIfIndex_Object = MibScalar
ruijieIPPrivateAcNotifyIpv4ChangeIfIndex = _RuijieIPPrivateAcNotifyIpv4ChangeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 1, 1, 4),
    _RuijieIPPrivateAcNotifyIpv4ChangeIfIndex_Type()
)
ruijieIPPrivateAcNotifyIpv4ChangeIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieIPPrivateAcNotifyIpv4ChangeIfIndex.setStatus("current")
_RuijieIPPrivateNotifyArpFilterInfo_Type = DisplayString
_RuijieIPPrivateNotifyArpFilterInfo_Object = MibScalar
ruijieIPPrivateNotifyArpFilterInfo = _RuijieIPPrivateNotifyArpFilterInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 1, 1, 5),
    _RuijieIPPrivateNotifyArpFilterInfo_Type()
)
ruijieIPPrivateNotifyArpFilterInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieIPPrivateNotifyArpFilterInfo.setStatus("current")
_RuijieIPPrivateAcNotifications_ObjectIdentity = ObjectIdentity
ruijieIPPrivateAcNotifications = _RuijieIPPrivateAcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 1, 2)
)
_RuijieIPPrivateAcQueryApMIBObject_ObjectIdentity = ObjectIdentity
ruijieIPPrivateAcQueryApMIBObject = _RuijieIPPrivateAcQueryApMIBObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 1, 3)
)
_RuijieIPPrivateAcQueryApInfo_ObjectIdentity = ObjectIdentity
ruijieIPPrivateAcQueryApInfo = _RuijieIPPrivateAcQueryApInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 1, 3, 1)
)
_RuijieIPPrivateAcQueryApMIBTable_Object = MibTable
ruijieIPPrivateAcQueryApMIBTable = _RuijieIPPrivateAcQueryApMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieIPPrivateAcQueryApMIBTable.setStatus("current")
_RuijieIPPrivateApInfoEntry_Object = MibTableRow
ruijieIPPrivateApInfoEntry = _RuijieIPPrivateApInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 1, 3, 1, 1, 1)
)
ruijieIPPrivateApInfoEntry.setIndexNames(
    (0, "RUIJIE-IP-PRIVATE-MIB", "ruijieIPPrivateAcApMacAddr"),
    (0, "RUIJIE-IP-PRIVATE-MIB", "ruijieIPPrivateAcApIp"),
)
if mibBuilder.loadTexts:
    ruijieIPPrivateApInfoEntry.setStatus("current")
_RuijieIPPrivateAcApMacAddr_Type = MacAddress
_RuijieIPPrivateAcApMacAddr_Object = MibTableColumn
ruijieIPPrivateAcApMacAddr = _RuijieIPPrivateAcApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 1, 3, 1, 1, 1, 1),
    _RuijieIPPrivateAcApMacAddr_Type()
)
ruijieIPPrivateAcApMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPPrivateAcApMacAddr.setStatus("current")
_RuijieIPPrivateAcApIp_Type = IpAddress
_RuijieIPPrivateAcApIp_Object = MibTableColumn
ruijieIPPrivateAcApIp = _RuijieIPPrivateAcApIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 1, 3, 1, 1, 1, 2),
    _RuijieIPPrivateAcApIp_Type()
)
ruijieIPPrivateAcApIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPPrivateAcApIp.setStatus("current")
_RuijieIPPrivateAcApMask_Type = IpAddress
_RuijieIPPrivateAcApMask_Object = MibTableColumn
ruijieIPPrivateAcApMask = _RuijieIPPrivateAcApMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 1, 3, 1, 1, 1, 3),
    _RuijieIPPrivateAcApMask_Type()
)
ruijieIPPrivateAcApMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPPrivateAcApMask.setStatus("current")
_RuijieIPPrivateAcApGateway_Type = IpAddress
_RuijieIPPrivateAcApGateway_Object = MibTableColumn
ruijieIPPrivateAcApGateway = _RuijieIPPrivateAcApGateway_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 1, 3, 1, 1, 1, 4),
    _RuijieIPPrivateAcApGateway_Type()
)
ruijieIPPrivateAcApGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPPrivateAcApGateway.setStatus("current")
_RuijieIPPrivateMIBConformance_ObjectIdentity = ObjectIdentity
ruijieIPPrivateMIBConformance = _RuijieIPPrivateMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 2)
)
_RuijieIPPrivateMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieIPPrivateMIBCompliances = _RuijieIPPrivateMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 2, 1)
)
_RuijieIPPrivateMIBGroups_ObjectIdentity = ObjectIdentity
ruijieIPPrivateMIBGroups = _RuijieIPPrivateMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 2, 2)
)
_RuijieIfIPMIBObjects_ObjectIdentity = ObjectIdentity
ruijieIfIPMIBObjects = _RuijieIfIPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 3)
)
_RuijieIfIPTable_Object = MibTable
ruijieIfIPTable = _RuijieIfIPTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieIfIPTable.setStatus("current")
_RuijieIfIPEntry_Object = MibTableRow
ruijieIfIPEntry = _RuijieIfIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 3, 1, 1)
)
ruijieIfIPEntry.setIndexNames(
    (0, "RUIJIE-IP-PRIVATE-MIB", "ruijieIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfIPEntry.setStatus("current")
_RuijieIfIndex_Type = IfIndex
_RuijieIfIndex_Object = MibTableColumn
ruijieIfIndex = _RuijieIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 3, 1, 1, 1),
    _RuijieIfIndex_Type()
)
ruijieIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieIfIndex.setStatus("current")
_RuijieIfIPPriIp_Type = IpAddress
_RuijieIfIPPriIp_Object = MibTableColumn
ruijieIfIPPriIp = _RuijieIfIPPriIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 3, 1, 1, 2),
    _RuijieIfIPPriIp_Type()
)
ruijieIfIPPriIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIPPriIp.setStatus("current")
_RuijieIfIP2ndIp1_Type = IpAddress
_RuijieIfIP2ndIp1_Object = MibTableColumn
ruijieIfIP2ndIp1 = _RuijieIfIP2ndIp1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 3, 1, 1, 3),
    _RuijieIfIP2ndIp1_Type()
)
ruijieIfIP2ndIp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIP2ndIp1.setStatus("current")
_RuijieIfIP2ndIp2_Type = IpAddress
_RuijieIfIP2ndIp2_Object = MibTableColumn
ruijieIfIP2ndIp2 = _RuijieIfIP2ndIp2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 3, 1, 1, 4),
    _RuijieIfIP2ndIp2_Type()
)
ruijieIfIP2ndIp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIP2ndIp2.setStatus("current")
_RuijieIfIP2ndIp3_Type = IpAddress
_RuijieIfIP2ndIp3_Object = MibTableColumn
ruijieIfIP2ndIp3 = _RuijieIfIP2ndIp3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 3, 1, 1, 5),
    _RuijieIfIP2ndIp3_Type()
)
ruijieIfIP2ndIp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIP2ndIp3.setStatus("current")
_RuijieIfIP2ndIp4_Type = IpAddress
_RuijieIfIP2ndIp4_Object = MibTableColumn
ruijieIfIP2ndIp4 = _RuijieIfIP2ndIp4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 3, 1, 1, 6),
    _RuijieIfIP2ndIp4_Type()
)
ruijieIfIP2ndIp4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIP2ndIp4.setStatus("current")
_RuijieIfIPv6Table_Object = MibTable
ruijieIfIPv6Table = _RuijieIfIPv6Table_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 3, 2)
)
if mibBuilder.loadTexts:
    ruijieIfIPv6Table.setStatus("current")
_RuijieIfIPv6Entry_Object = MibTableRow
ruijieIfIPv6Entry = _RuijieIfIPv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 3, 2, 1)
)
ruijieIfIPv6Entry.setIndexNames(
    (0, "RUIJIE-IP-PRIVATE-MIB", "ruijieIfIPv6Index"),
)
if mibBuilder.loadTexts:
    ruijieIfIPv6Entry.setStatus("current")
_RuijieIfIPv6Index_Type = IfIndex
_RuijieIfIPv6Index_Object = MibTableColumn
ruijieIfIPv6Index = _RuijieIfIPv6Index_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 3, 2, 1, 1),
    _RuijieIfIPv6Index_Type()
)
ruijieIfIPv6Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieIfIPv6Index.setStatus("current")
_RuijieIfIPv6LinkLocalIp_Type = Ipv6Address
_RuijieIfIPv6LinkLocalIp_Object = MibTableColumn
ruijieIfIPv6LinkLocalIp = _RuijieIfIPv6LinkLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 3, 2, 1, 2),
    _RuijieIfIPv6LinkLocalIp_Type()
)
ruijieIfIPv6LinkLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIPv6LinkLocalIp.setStatus("current")
_RuijieIfIPv6Ip1_Type = Ipv6Address
_RuijieIfIPv6Ip1_Object = MibTableColumn
ruijieIfIPv6Ip1 = _RuijieIfIPv6Ip1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 3, 2, 1, 3),
    _RuijieIfIPv6Ip1_Type()
)
ruijieIfIPv6Ip1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIPv6Ip1.setStatus("current")
_RuijieIfIPv6Ip2_Type = Ipv6Address
_RuijieIfIPv6Ip2_Object = MibTableColumn
ruijieIfIPv6Ip2 = _RuijieIfIPv6Ip2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 3, 2, 1, 4),
    _RuijieIfIPv6Ip2_Type()
)
ruijieIfIPv6Ip2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIPv6Ip2.setStatus("current")
_RuijieIfIPv6Ip3_Type = Ipv6Address
_RuijieIfIPv6Ip3_Object = MibTableColumn
ruijieIfIPv6Ip3 = _RuijieIfIPv6Ip3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 3, 2, 1, 5),
    _RuijieIfIPv6Ip3_Type()
)
ruijieIfIPv6Ip3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIPv6Ip3.setStatus("current")
_RuijieIfIPv6Ip4_Type = Ipv6Address
_RuijieIfIPv6Ip4_Object = MibTableColumn
ruijieIfIPv6Ip4 = _RuijieIfIPv6Ip4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 3, 2, 1, 6),
    _RuijieIfIPv6Ip4_Type()
)
ruijieIfIPv6Ip4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIPv6Ip4.setStatus("current")

# Managed Objects groups

ruijieIPPrivateMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 2, 2, 1)
)
ruijieIPPrivateMIBGroup.setObjects(
      *(("RUIJIE-IP-PRIVATE-MIB", "ruijieIPPrivateAcNotifyIpv4AddressChangeType"),
        ("RUIJIE-IP-PRIVATE-MIB", "ruijieIPPrivateAcNotifyIpv4ChangeAddress"),
        ("RUIJIE-IP-PRIVATE-MIB", "ruijieIPPrivateAcNotifyIpv4ChangeAddressMask"),
        ("RUIJIE-IP-PRIVATE-MIB", "ruijieIPPrivateAcNotifyIpv4ChangeIfIndex"),
        ("RUIJIE-IP-PRIVATE-MIB", "ruijieIPPrivateAcApMacAddr"),
        ("RUIJIE-IP-PRIVATE-MIB", "ruijieIPPrivateAcApIp"),
        ("RUIJIE-IP-PRIVATE-MIB", "ruijieIPPrivateAcApMask"),
        ("RUIJIE-IP-PRIVATE-MIB", "ruijieIPPrivateAcApGateway"))
)
if mibBuilder.loadTexts:
    ruijieIPPrivateMIBGroup.setStatus("current")


# Notification objects

ruijieIPPrivateAcNotifyChangeIpv4AddressAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 1, 2, 1)
)
ruijieIPPrivateAcNotifyChangeIpv4AddressAlarm.setObjects(
      *(("RUIJIE-IP-PRIVATE-MIB", "ruijieIPPrivateAcNotifyIpv4AddressChangeType"),
        ("RUIJIE-IP-PRIVATE-MIB", "ruijieIPPrivateAcNotifyIpv4ChangeAddress"),
        ("RUIJIE-IP-PRIVATE-MIB", "ruijieIPPrivateAcNotifyIpv4ChangeAddressMask"),
        ("RUIJIE-IP-PRIVATE-MIB", "ruijieIPPrivateAcNotifyIpv4ChangeIfIndex"))
)
if mibBuilder.loadTexts:
    ruijieIPPrivateAcNotifyChangeIpv4AddressAlarm.setStatus(
        "current"
    )

ruijieIPPrivateNotifyArpFilter = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 1, 2, 2)
)
ruijieIPPrivateNotifyArpFilter.setObjects(
    ("RUIJIE-IP-PRIVATE-MIB", "ruijieIPPrivateNotifyArpFilterInfo")
)
if mibBuilder.loadTexts:
    ruijieIPPrivateNotifyArpFilter.setStatus(
        "current"
    )


# Notifications groups

ruijieIPPrivateTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 2, 2, 2)
)
ruijieIPPrivateTrapGroup.setObjects(
    ("RUIJIE-IP-PRIVATE-MIB", "ruijieIPPrivateAcNotifyChangeIpv4AddressAlarm")
)
if mibBuilder.loadTexts:
    ruijieIPPrivateTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieIPPrivateMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 73, 2, 1, 1)
)
ruijieIPPrivateMIBCompliance.setObjects(
      *(("RUIJIE-IP-PRIVATE-MIB", "ruijieIPPrivateMIBGroup"),
        ("RUIJIE-IP-PRIVATE-MIB", "ruijieIPPrivateTrapGroup"))
)
if mibBuilder.loadTexts:
    ruijieIPPrivateMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-IP-PRIVATE-MIB",
    **{"ruijieIPPrivateMgmt": ruijieIPPrivateMgmt,
       "ruijieIPPrivateAcNotificationsMIBObjects": ruijieIPPrivateAcNotificationsMIBObjects,
       "ruijieIPPrivateAcNtfObjects": ruijieIPPrivateAcNtfObjects,
       "ruijieIPPrivateAcNotifyIpv4AddressChangeType": ruijieIPPrivateAcNotifyIpv4AddressChangeType,
       "ruijieIPPrivateAcNotifyIpv4ChangeAddress": ruijieIPPrivateAcNotifyIpv4ChangeAddress,
       "ruijieIPPrivateAcNotifyIpv4ChangeAddressMask": ruijieIPPrivateAcNotifyIpv4ChangeAddressMask,
       "ruijieIPPrivateAcNotifyIpv4ChangeIfIndex": ruijieIPPrivateAcNotifyIpv4ChangeIfIndex,
       "ruijieIPPrivateNotifyArpFilterInfo": ruijieIPPrivateNotifyArpFilterInfo,
       "ruijieIPPrivateAcNotifications": ruijieIPPrivateAcNotifications,
       "ruijieIPPrivateAcNotifyChangeIpv4AddressAlarm": ruijieIPPrivateAcNotifyChangeIpv4AddressAlarm,
       "ruijieIPPrivateNotifyArpFilter": ruijieIPPrivateNotifyArpFilter,
       "ruijieIPPrivateAcQueryApMIBObject": ruijieIPPrivateAcQueryApMIBObject,
       "ruijieIPPrivateAcQueryApInfo": ruijieIPPrivateAcQueryApInfo,
       "ruijieIPPrivateAcQueryApMIBTable": ruijieIPPrivateAcQueryApMIBTable,
       "ruijieIPPrivateApInfoEntry": ruijieIPPrivateApInfoEntry,
       "ruijieIPPrivateAcApMacAddr": ruijieIPPrivateAcApMacAddr,
       "ruijieIPPrivateAcApIp": ruijieIPPrivateAcApIp,
       "ruijieIPPrivateAcApMask": ruijieIPPrivateAcApMask,
       "ruijieIPPrivateAcApGateway": ruijieIPPrivateAcApGateway,
       "ruijieIPPrivateMIBConformance": ruijieIPPrivateMIBConformance,
       "ruijieIPPrivateMIBCompliances": ruijieIPPrivateMIBCompliances,
       "ruijieIPPrivateMIBCompliance": ruijieIPPrivateMIBCompliance,
       "ruijieIPPrivateMIBGroups": ruijieIPPrivateMIBGroups,
       "ruijieIPPrivateMIBGroup": ruijieIPPrivateMIBGroup,
       "ruijieIPPrivateTrapGroup": ruijieIPPrivateTrapGroup,
       "ruijieIfIPMIBObjects": ruijieIfIPMIBObjects,
       "ruijieIfIPTable": ruijieIfIPTable,
       "ruijieIfIPEntry": ruijieIfIPEntry,
       "ruijieIfIndex": ruijieIfIndex,
       "ruijieIfIPPriIp": ruijieIfIPPriIp,
       "ruijieIfIP2ndIp1": ruijieIfIP2ndIp1,
       "ruijieIfIP2ndIp2": ruijieIfIP2ndIp2,
       "ruijieIfIP2ndIp3": ruijieIfIP2ndIp3,
       "ruijieIfIP2ndIp4": ruijieIfIP2ndIp4,
       "ruijieIfIPv6Table": ruijieIfIPv6Table,
       "ruijieIfIPv6Entry": ruijieIfIPv6Entry,
       "ruijieIfIPv6Index": ruijieIfIPv6Index,
       "ruijieIfIPv6LinkLocalIp": ruijieIfIPv6LinkLocalIp,
       "ruijieIfIPv6Ip1": ruijieIfIPv6Ip1,
       "ruijieIfIPv6Ip2": ruijieIfIPv6Ip2,
       "ruijieIfIPv6Ip3": ruijieIfIPv6Ip3,
       "ruijieIfIPv6Ip4": ruijieIfIPv6Ip4}
)
