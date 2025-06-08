# SNMP MIB module (CISCO-OSPF-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-OSPF-TRAP-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:13:24 2025
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

(cospfAreaNssaTranslatorState,
 cospfLsdbType,
 cospfShamLinkAreaId,
 cospfShamLinkLocalIpAddress,
 cospfShamLinkNbrArea,
 cospfShamLinkNbrIpAddr,
 cospfShamLinkNbrIpAddrType,
 cospfShamLinkNbrRtrId,
 cospfShamLinkNbrState,
 cospfShamLinkNeighborId,
 cospfShamLinkState,
 cospfShamLinksAreaId,
 cospfShamLinksLocalIpAddr,
 cospfShamLinksLocalIpAddrType,
 cospfShamLinksRemoteIpAddr,
 cospfShamLinksRemoteIpAddrType,
 cospfShamLinksState) = mibBuilder.importSymbols(
    "CISCO-OSPF-MIB",
    "cospfAreaNssaTranslatorState",
    "cospfLsdbType",
    "cospfShamLinkAreaId",
    "cospfShamLinkLocalIpAddress",
    "cospfShamLinkNbrArea",
    "cospfShamLinkNbrIpAddr",
    "cospfShamLinkNbrIpAddrType",
    "cospfShamLinkNbrRtrId",
    "cospfShamLinkNbrState",
    "cospfShamLinkNeighborId",
    "cospfShamLinkState",
    "cospfShamLinksAreaId",
    "cospfShamLinksLocalIpAddr",
    "cospfShamLinksLocalIpAddrType",
    "cospfShamLinksRemoteIpAddr",
    "cospfShamLinksRemoteIpAddrType",
    "cospfShamLinksState")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ospfAddressLessIf,
 ospfAreaId,
 ospfIfIpAddress,
 ospfLsdbAreaId,
 ospfLsdbLsid,
 ospfLsdbRouterId,
 ospfNbrRtrId,
 ospfRouterId,
 ospfVirtIfAreaId,
 ospfVirtIfNeighbor) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "ospfAddressLessIf",
    "ospfAreaId",
    "ospfIfIpAddress",
    "ospfLsdbAreaId",
    "ospfLsdbLsid",
    "ospfLsdbRouterId",
    "ospfNbrRtrId",
    "ospfRouterId",
    "ospfVirtIfAreaId",
    "ospfVirtIfNeighbor")

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

ciscoOspfTrapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 101)
)
if mibBuilder.loadTexts:
    ciscoOspfTrapMIB.setRevisions(
        ("2003-07-18 00:00",
         "2003-02-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoOspfTrapMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoOspfTrapMIBNotifs = _CiscoOspfTrapMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 0)
)
_CiscoOspfTrapMIBObjects_ObjectIdentity = ObjectIdentity
ciscoOspfTrapMIBObjects = _CiscoOspfTrapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 1)
)
_CospfTrapControl_ObjectIdentity = ObjectIdentity
cospfTrapControl = _CospfTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 1, 1)
)


class _CospfSetTrap_Type(Bits):
    """Custom type cospfSetTrap based on Bits"""
    namedValues = NamedValues(
        *(("ifConfigError", 0),
          ("virtIfConfigError", 1),
          ("retransmit", 2),
          ("virtRetransmit", 3),
          ("originateLsa", 4),
          ("originateMaxAgeLsa", 5),
          ("nssaTranslatorStatusChange", 6),
          ("shamLinkStateChange", 7),
          ("shamLinkNbrStateChange", 8),
          ("shamLinkConfigError", 9),
          ("shamLinkAuthFailure", 10),
          ("shamLinkRxBadPacket", 11),
          ("shamLinkTxRetransmit", 12),
          ("shamLinksStateChange", 13))
    )

_CospfSetTrap_Type.__name__ = "Bits"
_CospfSetTrap_Object = MibScalar
cospfSetTrap = _CospfSetTrap_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 1, 1, 1),
    _CospfSetTrap_Type()
)
cospfSetTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cospfSetTrap.setStatus("current")


class _CospfConfigErrorType_Type(Integer32):
    """Custom type cospfConfigErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("badVersion", 1),
          ("areaMismatch", 2),
          ("unknownNbmaNbr", 3),
          ("unknownVirtualNbr", 4),
          ("authTypeMismatch", 5),
          ("authFailure", 6),
          ("netMaskMismatch", 7),
          ("helloIntervalMismatch", 8),
          ("deadIntervalMismatch", 9),
          ("optionMismatch", 10),
          ("mtuMismatch", 11),
          ("noError", 12),
          ("unknownShamLinkNbr", 13))
    )


_CospfConfigErrorType_Type.__name__ = "Integer32"
_CospfConfigErrorType_Object = MibScalar
cospfConfigErrorType = _CospfConfigErrorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 1, 1, 2),
    _CospfConfigErrorType_Type()
)
cospfConfigErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfConfigErrorType.setStatus("current")


class _CospfPacketType_Type(Integer32):
    """Custom type cospfPacketType based on Integer32"""
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
        *(("hello", 1),
          ("dbDescript", 2),
          ("lsReq", 3),
          ("lsUpdate", 4),
          ("lsAck", 5),
          ("nullPacket", 6))
    )


_CospfPacketType_Type.__name__ = "Integer32"
_CospfPacketType_Object = MibScalar
cospfPacketType = _CospfPacketType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 1, 1, 3),
    _CospfPacketType_Type()
)
cospfPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfPacketType.setStatus("current")
_CospfPacketSrc_Type = IpAddress
_CospfPacketSrc_Object = MibScalar
cospfPacketSrc = _CospfPacketSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 1, 1, 4),
    _CospfPacketSrc_Type()
)
cospfPacketSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfPacketSrc.setStatus("current")
_CiscoOspfTrapMIBConform_ObjectIdentity = ObjectIdentity
ciscoOspfTrapMIBConform = _CiscoOspfTrapMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 2)
)
_CiscoOspfTrapMIBGroups_ObjectIdentity = ObjectIdentity
ciscoOspfTrapMIBGroups = _CiscoOspfTrapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 2, 1)
)
_CiscoOspfTrapMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoOspfTrapMIBCompliances = _CiscoOspfTrapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 2, 2)
)

# Managed Objects groups

ciscoOspfTrapControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 2, 1, 2)
)
ciscoOspfTrapControlGroup.setObjects(
      *(("CISCO-OSPF-TRAP-MIB", "cospfSetTrap"),
        ("CISCO-OSPF-TRAP-MIB", "cospfConfigErrorType"),
        ("CISCO-OSPF-TRAP-MIB", "cospfPacketType"),
        ("CISCO-OSPF-TRAP-MIB", "cospfPacketSrc"))
)
if mibBuilder.loadTexts:
    ciscoOspfTrapControlGroup.setStatus("current")


# Notification objects

cospfIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 1)
)
cospfIfConfigError.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfIfIpAddress"),
        ("OSPF-MIB", "ospfAddressLessIf"),
        ("CISCO-OSPF-TRAP-MIB", "cospfPacketSrc"),
        ("CISCO-OSPF-TRAP-MIB", "cospfConfigErrorType"),
        ("CISCO-OSPF-TRAP-MIB", "cospfPacketType"))
)
if mibBuilder.loadTexts:
    cospfIfConfigError.setStatus(
        "current"
    )

cospfVirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 2)
)
cospfVirtIfConfigError.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfVirtIfAreaId"),
        ("OSPF-MIB", "ospfVirtIfNeighbor"),
        ("CISCO-OSPF-TRAP-MIB", "cospfConfigErrorType"),
        ("CISCO-OSPF-TRAP-MIB", "cospfPacketType"))
)
if mibBuilder.loadTexts:
    cospfVirtIfConfigError.setStatus(
        "current"
    )

cospfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 3)
)
cospfTxRetransmit.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfIfIpAddress"),
        ("OSPF-MIB", "ospfAddressLessIf"),
        ("OSPF-MIB", "ospfNbrRtrId"),
        ("CISCO-OSPF-TRAP-MIB", "cospfPacketType"),
        ("CISCO-OSPF-MIB", "cospfLsdbType"),
        ("OSPF-MIB", "ospfLsdbLsid"),
        ("OSPF-MIB", "ospfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    cospfTxRetransmit.setStatus(
        "current"
    )

cospfVirtIfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 4)
)
cospfVirtIfTxRetransmit.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfVirtIfAreaId"),
        ("OSPF-MIB", "ospfVirtIfNeighbor"),
        ("CISCO-OSPF-TRAP-MIB", "cospfPacketType"),
        ("CISCO-OSPF-MIB", "cospfLsdbType"),
        ("OSPF-MIB", "ospfLsdbLsid"),
        ("OSPF-MIB", "ospfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    cospfVirtIfTxRetransmit.setStatus(
        "current"
    )

cospfOriginateLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 5)
)
cospfOriginateLsa.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfLsdbAreaId"),
        ("CISCO-OSPF-MIB", "cospfLsdbType"),
        ("OSPF-MIB", "ospfLsdbLsid"),
        ("OSPF-MIB", "ospfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    cospfOriginateLsa.setStatus(
        "current"
    )

cospfMaxAgeLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 6)
)
cospfMaxAgeLsa.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfLsdbAreaId"),
        ("CISCO-OSPF-MIB", "cospfLsdbType"),
        ("OSPF-MIB", "ospfLsdbLsid"),
        ("CISCO-OSPF-MIB", "cospfLsdbType"),
        ("OSPF-MIB", "ospfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    cospfMaxAgeLsa.setStatus(
        "current"
    )

cospfNssaTranslatorStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 7)
)
cospfNssaTranslatorStatusChange.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfAreaId"),
        ("CISCO-OSPF-MIB", "cospfAreaNssaTranslatorState"))
)
if mibBuilder.loadTexts:
    cospfNssaTranslatorStatusChange.setStatus(
        "current"
    )

cospfShamLinkStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 8)
)
cospfShamLinkStateChange.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("CISCO-OSPF-MIB", "cospfShamLinkAreaId"),
        ("CISCO-OSPF-MIB", "cospfShamLinkLocalIpAddress"),
        ("CISCO-OSPF-MIB", "cospfShamLinkNeighborId"),
        ("CISCO-OSPF-MIB", "cospfShamLinkState"))
)
if mibBuilder.loadTexts:
    cospfShamLinkStateChange.setStatus(
        "deprecated"
    )

cospfShamLinkNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 9)
)
cospfShamLinkNbrStateChange.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("CISCO-OSPF-MIB", "cospfShamLinkNbrArea"),
        ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddrType"),
        ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddr"),
        ("CISCO-OSPF-MIB", "cospfShamLinkNbrIpAddrType"),
        ("CISCO-OSPF-MIB", "cospfShamLinkNbrIpAddr"),
        ("CISCO-OSPF-MIB", "cospfShamLinkNbrRtrId"),
        ("CISCO-OSPF-MIB", "cospfShamLinkNbrState"))
)
if mibBuilder.loadTexts:
    cospfShamLinkNbrStateChange.setStatus(
        "current"
    )

cospfShamLinkConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 10)
)
cospfShamLinkConfigError.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("CISCO-OSPF-MIB", "cospfShamLinksAreaId"),
        ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddrType"),
        ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddr"),
        ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddrType"),
        ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddr"),
        ("CISCO-OSPF-TRAP-MIB", "cospfConfigErrorType"),
        ("CISCO-OSPF-TRAP-MIB", "cospfPacketType"))
)
if mibBuilder.loadTexts:
    cospfShamLinkConfigError.setStatus(
        "current"
    )

cospfShamLinkAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 11)
)
cospfShamLinkAuthFailure.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("CISCO-OSPF-MIB", "cospfShamLinksAreaId"),
        ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddrType"),
        ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddr"),
        ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddrType"),
        ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddr"),
        ("CISCO-OSPF-TRAP-MIB", "cospfConfigErrorType"),
        ("CISCO-OSPF-TRAP-MIB", "cospfPacketType"))
)
if mibBuilder.loadTexts:
    cospfShamLinkAuthFailure.setStatus(
        "current"
    )

cospfShamLinkRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 12)
)
cospfShamLinkRxBadPacket.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("CISCO-OSPF-MIB", "cospfShamLinksAreaId"),
        ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddrType"),
        ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddr"),
        ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddrType"),
        ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddr"),
        ("CISCO-OSPF-TRAP-MIB", "cospfPacketType"))
)
if mibBuilder.loadTexts:
    cospfShamLinkRxBadPacket.setStatus(
        "current"
    )

cospfShamLinkTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 13)
)
cospfShamLinkTxRetransmit.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("CISCO-OSPF-MIB", "cospfShamLinksAreaId"),
        ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddrType"),
        ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddr"),
        ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddrType"),
        ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddr"),
        ("CISCO-OSPF-TRAP-MIB", "cospfPacketType"),
        ("CISCO-OSPF-MIB", "cospfLsdbType"),
        ("OSPF-MIB", "ospfLsdbLsid"),
        ("OSPF-MIB", "ospfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    cospfShamLinkTxRetransmit.setStatus(
        "current"
    )

cospfShamLinksStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 14)
)
cospfShamLinksStateChange.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("CISCO-OSPF-MIB", "cospfShamLinksAreaId"),
        ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddrType"),
        ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddr"),
        ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddrType"),
        ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddr"),
        ("CISCO-OSPF-MIB", "cospfShamLinksState"))
)
if mibBuilder.loadTexts:
    cospfShamLinksStateChange.setStatus(
        "current"
    )


# Notifications groups

ciscoOspfTrapEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 2, 1, 1)
)
ciscoOspfTrapEventGroup.setObjects(
      *(("CISCO-OSPF-TRAP-MIB", "cospfIfConfigError"),
        ("CISCO-OSPF-TRAP-MIB", "cospfVirtIfConfigError"),
        ("CISCO-OSPF-TRAP-MIB", "cospfTxRetransmit"),
        ("CISCO-OSPF-TRAP-MIB", "cospfVirtIfTxRetransmit"),
        ("CISCO-OSPF-TRAP-MIB", "cospfOriginateLsa"),
        ("CISCO-OSPF-TRAP-MIB", "cospfMaxAgeLsa"),
        ("CISCO-OSPF-TRAP-MIB", "cospfNssaTranslatorStatusChange"),
        ("CISCO-OSPF-TRAP-MIB", "cospfShamLinkStateChange"))
)
if mibBuilder.loadTexts:
    ciscoOspfTrapEventGroup.setStatus(
        "deprecated"
    )

ciscoOspfTrapEventGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 2, 1, 3)
)
ciscoOspfTrapEventGroupRev1.setObjects(
      *(("CISCO-OSPF-TRAP-MIB", "cospfIfConfigError"),
        ("CISCO-OSPF-TRAP-MIB", "cospfVirtIfConfigError"),
        ("CISCO-OSPF-TRAP-MIB", "cospfTxRetransmit"),
        ("CISCO-OSPF-TRAP-MIB", "cospfVirtIfTxRetransmit"),
        ("CISCO-OSPF-TRAP-MIB", "cospfOriginateLsa"),
        ("CISCO-OSPF-TRAP-MIB", "cospfMaxAgeLsa"),
        ("CISCO-OSPF-TRAP-MIB", "cospfNssaTranslatorStatusChange"),
        ("CISCO-OSPF-TRAP-MIB", "cospfShamLinksStateChange"),
        ("CISCO-OSPF-TRAP-MIB", "cospfShamLinkNbrStateChange"),
        ("CISCO-OSPF-TRAP-MIB", "cospfShamLinkConfigError"),
        ("CISCO-OSPF-TRAP-MIB", "cospfShamLinkAuthFailure"),
        ("CISCO-OSPF-TRAP-MIB", "cospfShamLinkRxBadPacket"),
        ("CISCO-OSPF-TRAP-MIB", "cospfShamLinkTxRetransmit"))
)
if mibBuilder.loadTexts:
    ciscoOspfTrapEventGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoOspfTrapMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 2, 2, 1)
)
ciscoOspfTrapMIBCompliance.setObjects(
      *(("CISCO-OSPF-TRAP-MIB", "ciscoOspfTrapEventGroup"),
        ("CISCO-OSPF-TRAP-MIB", "ciscoOspfTrapControlGroup"))
)
if mibBuilder.loadTexts:
    ciscoOspfTrapMIBCompliance.setStatus(
        "deprecated"
    )

ciscoOspfTrapMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 101, 2, 2, 2)
)
ciscoOspfTrapMIBComplianceRev1.setObjects(
      *(("CISCO-OSPF-TRAP-MIB", "ciscoOspfTrapEventGroupRev1"),
        ("CISCO-OSPF-TRAP-MIB", "ciscoOspfTrapControlGroup"))
)
if mibBuilder.loadTexts:
    ciscoOspfTrapMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-OSPF-TRAP-MIB",
    **{"ciscoOspfTrapMIB": ciscoOspfTrapMIB,
       "ciscoOspfTrapMIBNotifs": ciscoOspfTrapMIBNotifs,
       "cospfIfConfigError": cospfIfConfigError,
       "cospfVirtIfConfigError": cospfVirtIfConfigError,
       "cospfTxRetransmit": cospfTxRetransmit,
       "cospfVirtIfTxRetransmit": cospfVirtIfTxRetransmit,
       "cospfOriginateLsa": cospfOriginateLsa,
       "cospfMaxAgeLsa": cospfMaxAgeLsa,
       "cospfNssaTranslatorStatusChange": cospfNssaTranslatorStatusChange,
       "cospfShamLinkStateChange": cospfShamLinkStateChange,
       "cospfShamLinkNbrStateChange": cospfShamLinkNbrStateChange,
       "cospfShamLinkConfigError": cospfShamLinkConfigError,
       "cospfShamLinkAuthFailure": cospfShamLinkAuthFailure,
       "cospfShamLinkRxBadPacket": cospfShamLinkRxBadPacket,
       "cospfShamLinkTxRetransmit": cospfShamLinkTxRetransmit,
       "cospfShamLinksStateChange": cospfShamLinksStateChange,
       "ciscoOspfTrapMIBObjects": ciscoOspfTrapMIBObjects,
       "cospfTrapControl": cospfTrapControl,
       "cospfSetTrap": cospfSetTrap,
       "cospfConfigErrorType": cospfConfigErrorType,
       "cospfPacketType": cospfPacketType,
       "cospfPacketSrc": cospfPacketSrc,
       "ciscoOspfTrapMIBConform": ciscoOspfTrapMIBConform,
       "ciscoOspfTrapMIBGroups": ciscoOspfTrapMIBGroups,
       "ciscoOspfTrapEventGroup": ciscoOspfTrapEventGroup,
       "ciscoOspfTrapControlGroup": ciscoOspfTrapControlGroup,
       "ciscoOspfTrapEventGroupRev1": ciscoOspfTrapEventGroupRev1,
       "ciscoOspfTrapMIBCompliances": ciscoOspfTrapMIBCompliances,
       "ciscoOspfTrapMIBCompliance": ciscoOspfTrapMIBCompliance,
       "ciscoOspfTrapMIBComplianceRev1": ciscoOspfTrapMIBComplianceRev1}
)
