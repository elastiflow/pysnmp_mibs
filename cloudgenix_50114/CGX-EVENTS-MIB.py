# SNMP MIB module (CGX-EVENTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cloudgenix_50114/CGX-EVENTS-MIB.mib
# Produced by pysmi-1.6.1 at Wed Jun  4 13:56:22 2025
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

(cgxMgmt,) = mibBuilder.importSymbols(
    "CLOUDGENIX-SMI",
    "cgxMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cgxEventsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1)
)
if mibBuilder.loadTexts:
    cgxEventsMIB.setRevisions(
        ("2022-02-24 19:35",
         "2017-06-19 18:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CgxEventsNotifications_ObjectIdentity = ObjectIdentity
cgxEventsNotifications = _CgxEventsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0)
)
_CgxEventsObjects_ObjectIdentity = ObjectIdentity
cgxEventsObjects = _CgxEventsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1)
)
_CgxEventsObjectStats_ObjectIdentity = ObjectIdentity
cgxEventsObjectStats = _CgxEventsObjectStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 1)
)
_CgxVpnObjects_ObjectIdentity = ObjectIdentity
cgxVpnObjects = _CgxVpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 2)
)
_CgxVpnLinkId_Type = DisplayString
_CgxVpnLinkId_Object = MibScalar
cgxVpnLinkId = _CgxVpnLinkId_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 2, 1),
    _CgxVpnLinkId_Type()
)
cgxVpnLinkId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxVpnLinkId.setStatus("current")
_CgxRoutingObjects_ObjectIdentity = ObjectIdentity
cgxRoutingObjects = _CgxRoutingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 3)
)
_CgxRoutePeerId_Type = DisplayString
_CgxRoutePeerId_Object = MibScalar
cgxRoutePeerId = _CgxRoutePeerId_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 3, 1),
    _CgxRoutePeerId_Type()
)
cgxRoutePeerId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxRoutePeerId.setStatus("current")
_CgxRoutePeerName_Type = DisplayString
_CgxRoutePeerName_Object = MibScalar
cgxRoutePeerName = _CgxRoutePeerName_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 3, 2),
    _CgxRoutePeerName_Type()
)
cgxRoutePeerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxRoutePeerName.setStatus("current")
_CgxRoutePeerIp_Type = IpAddress
_CgxRoutePeerIp_Object = MibScalar
cgxRoutePeerIp = _CgxRoutePeerIp_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 3, 3),
    _CgxRoutePeerIp_Type()
)
cgxRoutePeerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxRoutePeerIp.setStatus("current")
_CgxRoutePeerType_Type = DisplayString
_CgxRoutePeerType_Object = MibScalar
cgxRoutePeerType = _CgxRoutePeerType_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 3, 4),
    _CgxRoutePeerType_Type()
)
cgxRoutePeerType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxRoutePeerType.setStatus("current")
_CgxSiteObjects_ObjectIdentity = ObjectIdentity
cgxSiteObjects = _CgxSiteObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 4)
)
_CgxSiteId_Type = DisplayString
_CgxSiteId_Object = MibScalar
cgxSiteId = _CgxSiteId_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 4, 1),
    _CgxSiteId_Type()
)
cgxSiteId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxSiteId.setStatus("current")
_CgxSiteName_Type = DisplayString
_CgxSiteName_Object = MibScalar
cgxSiteName = _CgxSiteName_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 4, 2),
    _CgxSiteName_Type()
)
cgxSiteName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxSiteName.setStatus("current")
_CgxSiteRemoteId_Type = DisplayString
_CgxSiteRemoteId_Object = MibScalar
cgxSiteRemoteId = _CgxSiteRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 4, 3),
    _CgxSiteRemoteId_Type()
)
cgxSiteRemoteId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxSiteRemoteId.setStatus("current")
_CgxSiteRemoteName_Type = DisplayString
_CgxSiteRemoteName_Object = MibScalar
cgxSiteRemoteName = _CgxSiteRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 4, 4),
    _CgxSiteRemoteName_Type()
)
cgxSiteRemoteName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxSiteRemoteName.setStatus("current")
_CgxSiteWanInterfaceId_Type = DisplayString
_CgxSiteWanInterfaceId_Object = MibScalar
cgxSiteWanInterfaceId = _CgxSiteWanInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 4, 5),
    _CgxSiteWanInterfaceId_Type()
)
cgxSiteWanInterfaceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxSiteWanInterfaceId.setStatus("current")
_CgxSiteWanInterfaceName_Type = DisplayString
_CgxSiteWanInterfaceName_Object = MibScalar
cgxSiteWanInterfaceName = _CgxSiteWanInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 4, 6),
    _CgxSiteWanInterfaceName_Type()
)
cgxSiteWanInterfaceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxSiteWanInterfaceName.setStatus("current")
_CgxElementObjects_ObjectIdentity = ObjectIdentity
cgxElementObjects = _CgxElementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 5)
)
_CgxElementId_Type = DisplayString
_CgxElementId_Object = MibScalar
cgxElementId = _CgxElementId_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 5, 1),
    _CgxElementId_Type()
)
cgxElementId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxElementId.setStatus("current")
_CgxElementName_Type = DisplayString
_CgxElementName_Object = MibScalar
cgxElementName = _CgxElementName_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 5, 2),
    _CgxElementName_Type()
)
cgxElementName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxElementName.setStatus("current")
_CgxElementRemoteId_Type = DisplayString
_CgxElementRemoteId_Object = MibScalar
cgxElementRemoteId = _CgxElementRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 5, 3),
    _CgxElementRemoteId_Type()
)
cgxElementRemoteId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxElementRemoteId.setStatus("current")
_CgxElementRemoteName_Type = DisplayString
_CgxElementRemoteName_Object = MibScalar
cgxElementRemoteName = _CgxElementRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 5, 4),
    _CgxElementRemoteName_Type()
)
cgxElementRemoteName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxElementRemoteName.setStatus("current")
_CgxWanObjects_ObjectIdentity = ObjectIdentity
cgxWanObjects = _CgxWanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 6)
)
_CgxWanNetworkId_Type = DisplayString
_CgxWanNetworkId_Object = MibScalar
cgxWanNetworkId = _CgxWanNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 6, 1),
    _CgxWanNetworkId_Type()
)
cgxWanNetworkId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxWanNetworkId.setStatus("current")
_CgxWanNetworkName_Type = DisplayString
_CgxWanNetworkName_Object = MibScalar
cgxWanNetworkName = _CgxWanNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 6, 2),
    _CgxWanNetworkName_Type()
)
cgxWanNetworkName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxWanNetworkName.setStatus("current")
_CgxWanNetworkType_Type = DisplayString
_CgxWanNetworkType_Object = MibScalar
cgxWanNetworkType = _CgxWanNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 6, 3),
    _CgxWanNetworkType_Type()
)
cgxWanNetworkType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxWanNetworkType.setStatus("current")
_CgxWanNetworkRemoteId_Type = DisplayString
_CgxWanNetworkRemoteId_Object = MibScalar
cgxWanNetworkRemoteId = _CgxWanNetworkRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 6, 4),
    _CgxWanNetworkRemoteId_Type()
)
cgxWanNetworkRemoteId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxWanNetworkRemoteId.setStatus("current")
_CgxWanNetworkRemoteName_Type = DisplayString
_CgxWanNetworkRemoteName_Object = MibScalar
cgxWanNetworkRemoteName = _CgxWanNetworkRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 6, 5),
    _CgxWanNetworkRemoteName_Type()
)
cgxWanNetworkRemoteName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxWanNetworkRemoteName.setStatus("current")
_CgxWanNetworkRemoteType_Type = DisplayString
_CgxWanNetworkRemoteType_Object = MibScalar
cgxWanNetworkRemoteType = _CgxWanNetworkRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 6, 6),
    _CgxWanNetworkRemoteType_Type()
)
cgxWanNetworkRemoteType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxWanNetworkRemoteType.setStatus("current")
_CgxWanNetworkPrefix_Type = DisplayString
_CgxWanNetworkPrefix_Object = MibScalar
cgxWanNetworkPrefix = _CgxWanNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 6, 7),
    _CgxWanNetworkPrefix_Type()
)
cgxWanNetworkPrefix.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxWanNetworkPrefix.setStatus("current")
_CgxProcessObjects_ObjectIdentity = ObjectIdentity
cgxProcessObjects = _CgxProcessObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 7)
)
_CgxProcessId_Type = DisplayString
_CgxProcessId_Object = MibScalar
cgxProcessId = _CgxProcessId_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 7, 1),
    _CgxProcessId_Type()
)
cgxProcessId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxProcessId.setStatus("current")
_CgxProcessName_Type = DisplayString
_CgxProcessName_Object = MibScalar
cgxProcessName = _CgxProcessName_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 1, 7, 2),
    _CgxProcessName_Type()
)
cgxProcessName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgxProcessName.setStatus("current")
_CgxEventsConformance_ObjectIdentity = ObjectIdentity
cgxEventsConformance = _CgxEventsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 2)
)
_CgxEventsCompliances_ObjectIdentity = ObjectIdentity
cgxEventsCompliances = _CgxEventsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 2, 1)
)
_CgxEventsGroups_ObjectIdentity = ObjectIdentity
cgxEventsGroups = _CgxEventsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 2, 2)
)

# Managed Objects groups

cgxVpnObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 2, 2, 2)
)
cgxVpnObjectGroup.setObjects(
    ("CGX-EVENTS-MIB", "cgxVpnLinkId")
)
if mibBuilder.loadTexts:
    cgxVpnObjectGroup.setStatus("current")

cgxRoutingObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 2, 2, 3)
)
cgxRoutingObjectGroup.setObjects(
      *(("CGX-EVENTS-MIB", "cgxRoutePeerId"),
        ("CGX-EVENTS-MIB", "cgxRoutePeerIp"),
        ("CGX-EVENTS-MIB", "cgxRoutePeerName"),
        ("CGX-EVENTS-MIB", "cgxRoutePeerType"))
)
if mibBuilder.loadTexts:
    cgxRoutingObjectGroup.setStatus("current")

cgxSiteObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 2, 2, 4)
)
cgxSiteObjectGroup.setObjects(
      *(("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxSiteRemoteId"),
        ("CGX-EVENTS-MIB", "cgxSiteRemoteName"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceId"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceName"))
)
if mibBuilder.loadTexts:
    cgxSiteObjectGroup.setStatus("current")

cgxElementObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 2, 2, 5)
)
cgxElementObjectGroup.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxElementRemoteId"),
        ("CGX-EVENTS-MIB", "cgxElementRemoteName"))
)
if mibBuilder.loadTexts:
    cgxElementObjectGroup.setStatus("current")

cgxWanObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 2, 2, 6)
)
cgxWanObjectGroup.setObjects(
      *(("CGX-EVENTS-MIB", "cgxWanNetworkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkType"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteType"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkPrefix"))
)
if mibBuilder.loadTexts:
    cgxWanObjectGroup.setStatus("current")

cgxProcessObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 2, 2, 7)
)
cgxProcessObjectGroup.setObjects(
      *(("CGX-EVENTS-MIB", "cgxProcessId"),
        ("CGX-EVENTS-MIB", "cgxProcessName"))
)
if mibBuilder.loadTexts:
    cgxProcessObjectGroup.setStatus("current")


# Notification objects

cgxVpnLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 1)
)
cgxVpnLinkUp.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxElementRemoteId"),
        ("CGX-EVENTS-MIB", "cgxElementRemoteName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxSiteRemoteId"),
        ("CGX-EVENTS-MIB", "cgxSiteRemoteName"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceId"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceName"),
        ("CGX-EVENTS-MIB", "cgxVpnLinkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkType"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteType"))
)
if mibBuilder.loadTexts:
    cgxVpnLinkUp.setStatus(
        "current"
    )

cgxVpnLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 2)
)
cgxVpnLinkDown.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxElementRemoteId"),
        ("CGX-EVENTS-MIB", "cgxElementRemoteName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxSiteRemoteId"),
        ("CGX-EVENTS-MIB", "cgxSiteRemoteName"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceId"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceName"),
        ("CGX-EVENTS-MIB", "cgxVpnLinkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkType"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteType"))
)
if mibBuilder.loadTexts:
    cgxVpnLinkDown.setStatus(
        "current"
    )

cgxVpnPeerUnreachableClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 3)
)
cgxVpnPeerUnreachableClear.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxElementRemoteId"),
        ("CGX-EVENTS-MIB", "cgxElementRemoteName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxSiteRemoteId"),
        ("CGX-EVENTS-MIB", "cgxSiteRemoteName"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceId"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceName"),
        ("CGX-EVENTS-MIB", "cgxVpnLinkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkType"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteType"))
)
if mibBuilder.loadTexts:
    cgxVpnPeerUnreachableClear.setStatus(
        "current"
    )

cgxVpnPeerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 4)
)
cgxVpnPeerUnreachable.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxElementRemoteId"),
        ("CGX-EVENTS-MIB", "cgxElementRemoteName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxSiteRemoteId"),
        ("CGX-EVENTS-MIB", "cgxSiteRemoteName"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceId"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceName"),
        ("CGX-EVENTS-MIB", "cgxVpnLinkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkType"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteType"))
)
if mibBuilder.loadTexts:
    cgxVpnPeerUnreachable.setStatus(
        "current"
    )

cgxVpnBfdUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 5)
)
cgxVpnBfdUp.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxElementRemoteId"),
        ("CGX-EVENTS-MIB", "cgxElementRemoteName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxSiteRemoteId"),
        ("CGX-EVENTS-MIB", "cgxSiteRemoteName"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceId"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceName"),
        ("CGX-EVENTS-MIB", "cgxVpnLinkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkType"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteType"))
)
if mibBuilder.loadTexts:
    cgxVpnBfdUp.setStatus(
        "current"
    )

cgxVpnBfdDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 6)
)
cgxVpnBfdDown.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxElementRemoteId"),
        ("CGX-EVENTS-MIB", "cgxElementRemoteName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxSiteRemoteId"),
        ("CGX-EVENTS-MIB", "cgxSiteRemoteName"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceId"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceName"),
        ("CGX-EVENTS-MIB", "cgxVpnLinkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkType"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkRemoteType"))
)
if mibBuilder.loadTexts:
    cgxVpnBfdDown.setStatus(
        "current"
    )

cgxRoutePeerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 101)
)
cgxRoutePeerUp.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxRoutePeerId"),
        ("CGX-EVENTS-MIB", "cgxRoutePeerIp"),
        ("CGX-EVENTS-MIB", "cgxRoutePeerType"))
)
if mibBuilder.loadTexts:
    cgxRoutePeerUp.setStatus(
        "current"
    )

cgxRoutePeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 102)
)
cgxRoutePeerDown.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxRoutePeerId"),
        ("CGX-EVENTS-MIB", "cgxRoutePeerIp"),
        ("CGX-EVENTS-MIB", "cgxRoutePeerType"))
)
if mibBuilder.loadTexts:
    cgxRoutePeerDown.setStatus(
        "current"
    )

cgxPrivateWanUnreachableClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 201)
)
cgxPrivateWanUnreachableClear.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceId"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkType"))
)
if mibBuilder.loadTexts:
    cgxPrivateWanUnreachableClear.setStatus(
        "current"
    )

cgxPrivateWanUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 202)
)
cgxPrivateWanUnreachable.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceId"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkType"))
)
if mibBuilder.loadTexts:
    cgxPrivateWanUnreachable.setStatus(
        "current"
    )

cgxPrivateWanDegradedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 203)
)
cgxPrivateWanDegradedClear.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceId"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkType"))
)
if mibBuilder.loadTexts:
    cgxPrivateWanDegradedClear.setStatus(
        "current"
    )

cgxPrivateWanDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 204)
)
cgxPrivateWanDegraded.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceId"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkType"))
)
if mibBuilder.loadTexts:
    cgxPrivateWanDegraded.setStatus(
        "current"
    )

cgxPublicWanUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 205)
)
cgxPublicWanUp.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceId"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkType"))
)
if mibBuilder.loadTexts:
    cgxPublicWanUp.setStatus(
        "current"
    )

cgxPublicWanDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 206)
)
cgxPublicWanDown.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceId"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkType"))
)
if mibBuilder.loadTexts:
    cgxPublicWanDown.setStatus(
        "current"
    )

cgxPrivateWanUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 207)
)
cgxPrivateWanUp.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceId"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkType"))
)
if mibBuilder.loadTexts:
    cgxPrivateWanUp.setStatus(
        "current"
    )

cgxPrivateWanDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 208)
)
cgxPrivateWanDown.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceId"),
        ("CGX-EVENTS-MIB", "cgxSiteWanInterfaceName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkId"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkName"),
        ("CGX-EVENTS-MIB", "cgxWanNetworkType"))
)
if mibBuilder.loadTexts:
    cgxPrivateWanDown.setStatus(
        "current"
    )

cgxProcessStopClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 301)
)
cgxProcessStopClear.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxProcessName"))
)
if mibBuilder.loadTexts:
    cgxProcessStopClear.setStatus(
        "current"
    )

cgxProcessStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 302)
)
cgxProcessStop.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxProcessName"))
)
if mibBuilder.loadTexts:
    cgxProcessStop.setStatus(
        "current"
    )

cgxProcessRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 0, 303)
)
cgxProcessRestart.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementId"),
        ("CGX-EVENTS-MIB", "cgxElementName"),
        ("CGX-EVENTS-MIB", "cgxSiteId"),
        ("CGX-EVENTS-MIB", "cgxSiteName"),
        ("CGX-EVENTS-MIB", "cgxProcessName"))
)
if mibBuilder.loadTexts:
    cgxProcessRestart.setStatus(
        "current"
    )


# Notifications groups

cgxVpnNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 2, 2, 102)
)
cgxVpnNotificationGroup.setObjects(
      *(("CGX-EVENTS-MIB", "cgxVpnBfdDown"),
        ("CGX-EVENTS-MIB", "cgxVpnBfdUp"),
        ("CGX-EVENTS-MIB", "cgxVpnLinkDown"),
        ("CGX-EVENTS-MIB", "cgxVpnLinkUp"),
        ("CGX-EVENTS-MIB", "cgxVpnPeerUnreachable"),
        ("CGX-EVENTS-MIB", "cgxVpnPeerUnreachableClear"))
)
if mibBuilder.loadTexts:
    cgxVpnNotificationGroup.setStatus(
        "current"
    )

cgxRoutingNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 2, 2, 103)
)
cgxRoutingNotificationGroup.setObjects(
      *(("CGX-EVENTS-MIB", "cgxRoutePeerDown"),
        ("CGX-EVENTS-MIB", "cgxRoutePeerUp"))
)
if mibBuilder.loadTexts:
    cgxRoutingNotificationGroup.setStatus(
        "current"
    )

cgxWanNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 2, 2, 104)
)
cgxWanNotificationGroup.setObjects(
      *(("CGX-EVENTS-MIB", "cgxPrivateWanDegraded"),
        ("CGX-EVENTS-MIB", "cgxPrivateWanDegradedClear"),
        ("CGX-EVENTS-MIB", "cgxPublicWanDown"),
        ("CGX-EVENTS-MIB", "cgxPublicWanUp"),
        ("CGX-EVENTS-MIB", "cgxPrivateWanDown"),
        ("CGX-EVENTS-MIB", "cgxPrivateWanUp"),
        ("CGX-EVENTS-MIB", "cgxPrivateWanUnreachable"),
        ("CGX-EVENTS-MIB", "cgxPrivateWanUnreachableClear"))
)
if mibBuilder.loadTexts:
    cgxWanNotificationGroup.setStatus(
        "current"
    )

cgxProcessNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 2, 2, 105)
)
cgxProcessNotificationGroup.setObjects(
      *(("CGX-EVENTS-MIB", "cgxProcessStop"),
        ("CGX-EVENTS-MIB", "cgxProcessStopClear"),
        ("CGX-EVENTS-MIB", "cgxProcessRestart"))
)
if mibBuilder.loadTexts:
    cgxProcessNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cgxEventsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 50114, 10, 1, 2, 1, 1)
)
cgxEventsMIBCompliance.setObjects(
      *(("CGX-EVENTS-MIB", "cgxElementObjectGroup"),
        ("CGX-EVENTS-MIB", "cgxProcessNotificationGroup"),
        ("CGX-EVENTS-MIB", "cgxProcessObjectGroup"),
        ("CGX-EVENTS-MIB", "cgxRoutingNotificationGroup"),
        ("CGX-EVENTS-MIB", "cgxRoutingObjectGroup"),
        ("CGX-EVENTS-MIB", "cgxSiteObjectGroup"),
        ("CGX-EVENTS-MIB", "cgxVpnNotificationGroup"),
        ("CGX-EVENTS-MIB", "cgxVpnObjectGroup"),
        ("CGX-EVENTS-MIB", "cgxWanNotificationGroup"),
        ("CGX-EVENTS-MIB", "cgxWanObjectGroup"))
)
if mibBuilder.loadTexts:
    cgxEventsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CGX-EVENTS-MIB",
    **{"cgxEventsMIB": cgxEventsMIB,
       "cgxEventsNotifications": cgxEventsNotifications,
       "cgxVpnLinkUp": cgxVpnLinkUp,
       "cgxVpnLinkDown": cgxVpnLinkDown,
       "cgxVpnPeerUnreachableClear": cgxVpnPeerUnreachableClear,
       "cgxVpnPeerUnreachable": cgxVpnPeerUnreachable,
       "cgxVpnBfdUp": cgxVpnBfdUp,
       "cgxVpnBfdDown": cgxVpnBfdDown,
       "cgxRoutePeerUp": cgxRoutePeerUp,
       "cgxRoutePeerDown": cgxRoutePeerDown,
       "cgxPrivateWanUnreachableClear": cgxPrivateWanUnreachableClear,
       "cgxPrivateWanUnreachable": cgxPrivateWanUnreachable,
       "cgxPrivateWanDegradedClear": cgxPrivateWanDegradedClear,
       "cgxPrivateWanDegraded": cgxPrivateWanDegraded,
       "cgxPublicWanUp": cgxPublicWanUp,
       "cgxPublicWanDown": cgxPublicWanDown,
       "cgxPrivateWanUp": cgxPrivateWanUp,
       "cgxPrivateWanDown": cgxPrivateWanDown,
       "cgxProcessStopClear": cgxProcessStopClear,
       "cgxProcessStop": cgxProcessStop,
       "cgxProcessRestart": cgxProcessRestart,
       "cgxEventsObjects": cgxEventsObjects,
       "cgxEventsObjectStats": cgxEventsObjectStats,
       "cgxVpnObjects": cgxVpnObjects,
       "cgxVpnLinkId": cgxVpnLinkId,
       "cgxRoutingObjects": cgxRoutingObjects,
       "cgxRoutePeerId": cgxRoutePeerId,
       "cgxRoutePeerName": cgxRoutePeerName,
       "cgxRoutePeerIp": cgxRoutePeerIp,
       "cgxRoutePeerType": cgxRoutePeerType,
       "cgxSiteObjects": cgxSiteObjects,
       "cgxSiteId": cgxSiteId,
       "cgxSiteName": cgxSiteName,
       "cgxSiteRemoteId": cgxSiteRemoteId,
       "cgxSiteRemoteName": cgxSiteRemoteName,
       "cgxSiteWanInterfaceId": cgxSiteWanInterfaceId,
       "cgxSiteWanInterfaceName": cgxSiteWanInterfaceName,
       "cgxElementObjects": cgxElementObjects,
       "cgxElementId": cgxElementId,
       "cgxElementName": cgxElementName,
       "cgxElementRemoteId": cgxElementRemoteId,
       "cgxElementRemoteName": cgxElementRemoteName,
       "cgxWanObjects": cgxWanObjects,
       "cgxWanNetworkId": cgxWanNetworkId,
       "cgxWanNetworkName": cgxWanNetworkName,
       "cgxWanNetworkType": cgxWanNetworkType,
       "cgxWanNetworkRemoteId": cgxWanNetworkRemoteId,
       "cgxWanNetworkRemoteName": cgxWanNetworkRemoteName,
       "cgxWanNetworkRemoteType": cgxWanNetworkRemoteType,
       "cgxWanNetworkPrefix": cgxWanNetworkPrefix,
       "cgxProcessObjects": cgxProcessObjects,
       "cgxProcessId": cgxProcessId,
       "cgxProcessName": cgxProcessName,
       "cgxEventsConformance": cgxEventsConformance,
       "cgxEventsCompliances": cgxEventsCompliances,
       "cgxEventsMIBCompliance": cgxEventsMIBCompliance,
       "cgxEventsGroups": cgxEventsGroups,
       "cgxVpnObjectGroup": cgxVpnObjectGroup,
       "cgxRoutingObjectGroup": cgxRoutingObjectGroup,
       "cgxSiteObjectGroup": cgxSiteObjectGroup,
       "cgxElementObjectGroup": cgxElementObjectGroup,
       "cgxWanObjectGroup": cgxWanObjectGroup,
       "cgxProcessObjectGroup": cgxProcessObjectGroup,
       "cgxVpnNotificationGroup": cgxVpnNotificationGroup,
       "cgxRoutingNotificationGroup": cgxRoutingNotificationGroup,
       "cgxWanNotificationGroup": cgxWanNotificationGroup,
       "cgxProcessNotificationGroup": cgxProcessNotificationGroup}
)
