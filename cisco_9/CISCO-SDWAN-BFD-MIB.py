# SNMP MIB module (CISCO-SDWAN-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SDWAN-BFD-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:52:58 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoSdwanBfdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002)
)
if mibBuilder.loadTexts:
    ciscoSdwanBfdMIB.setRevisions(
        ("2021-01-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class InetAddressIP(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class BfdmgrStateEnum(TextualConvention, Integer32):
    status = "current"
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
        *(("adminDown", 0),
          ("down", 1),
          ("init", 2),
          ("up", 3),
          ("invalid", 4),
          ("inactive", 5))
    )



class NotificationSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3))
    )



class OperState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSdwanBfdMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSdwanBfdMIBNotifs = _CiscoSdwanBfdMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 0)
)
_CiscoSdwanBfdMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSdwanBfdMIBObjects = _CiscoSdwanBfdMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1)
)
_Bfd_ObjectIdentity = ObjectIdentity
bfd = _Bfd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1)
)
_BfdSessionsListTable_Object = MibTable
bfdSessionsListTable = _BfdSessionsListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 1)
)
if mibBuilder.loadTexts:
    bfdSessionsListTable.setStatus("current")
_BfdSessionsListEntry_Object = MibTableRow
bfdSessionsListEntry = _BfdSessionsListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 1, 1)
)
bfdSessionsListEntry.setIndexNames(
    (0, "CISCO-SDWAN-BFD-MIB", "bfdSessionsListSrcIp"),
    (0, "CISCO-SDWAN-BFD-MIB", "bfdSessionsListDstIp"),
    (0, "CISCO-SDWAN-BFD-MIB", "bfdSessionsListProto"),
    (0, "CISCO-SDWAN-BFD-MIB", "bfdSessionsListSrcPort"),
    (0, "CISCO-SDWAN-BFD-MIB", "bfdSessionsListDstPort"),
)
if mibBuilder.loadTexts:
    bfdSessionsListEntry.setStatus("current")
_BfdSessionsListSrcIp_Type = InetAddressIP
_BfdSessionsListSrcIp_Object = MibTableColumn
bfdSessionsListSrcIp = _BfdSessionsListSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 1, 1, 1),
    _BfdSessionsListSrcIp_Type()
)
bfdSessionsListSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdSessionsListSrcIp.setStatus("current")
_BfdSessionsListDstIp_Type = InetAddressIP
_BfdSessionsListDstIp_Object = MibTableColumn
bfdSessionsListDstIp = _BfdSessionsListDstIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 1, 1, 2),
    _BfdSessionsListDstIp_Type()
)
bfdSessionsListDstIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdSessionsListDstIp.setStatus("current")


class _BfdSessionsListProto_Type(Integer32):
    """Custom type bfdSessionsListProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_BfdSessionsListProto_Type.__name__ = "Integer32"
_BfdSessionsListProto_Object = MibTableColumn
bfdSessionsListProto = _BfdSessionsListProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 1, 1, 3),
    _BfdSessionsListProto_Type()
)
bfdSessionsListProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdSessionsListProto.setStatus("current")
_BfdSessionsListSrcPort_Type = UnsignedShort
_BfdSessionsListSrcPort_Object = MibTableColumn
bfdSessionsListSrcPort = _BfdSessionsListSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 1, 1, 4),
    _BfdSessionsListSrcPort_Type()
)
bfdSessionsListSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdSessionsListSrcPort.setStatus("current")
_BfdSessionsListDstPort_Type = UnsignedShort
_BfdSessionsListDstPort_Object = MibTableColumn
bfdSessionsListDstPort = _BfdSessionsListDstPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 1, 1, 5),
    _BfdSessionsListDstPort_Type()
)
bfdSessionsListDstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdSessionsListDstPort.setStatus("current")
_BfdSessionsListSystemIp_Type = InetAddressIP
_BfdSessionsListSystemIp_Object = MibTableColumn
bfdSessionsListSystemIp = _BfdSessionsListSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 1, 1, 6),
    _BfdSessionsListSystemIp_Type()
)
bfdSessionsListSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessionsListSystemIp.setStatus("current")
_BfdSessionsListSiteId_Type = Unsigned32
_BfdSessionsListSiteId_Object = MibTableColumn
bfdSessionsListSiteId = _BfdSessionsListSiteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 1, 1, 7),
    _BfdSessionsListSiteId_Type()
)
bfdSessionsListSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessionsListSiteId.setStatus("current")


class _BfdSessionsListLocalColor_Type(Integer32):
    """Custom type bfdSessionsListLocalColor based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metroEthernet", 3),
          ("bizInternet", 4),
          ("publicInternet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_BfdSessionsListLocalColor_Type.__name__ = "Integer32"
_BfdSessionsListLocalColor_Object = MibTableColumn
bfdSessionsListLocalColor = _BfdSessionsListLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 1, 1, 8),
    _BfdSessionsListLocalColor_Type()
)
bfdSessionsListLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessionsListLocalColor.setStatus("current")


class _BfdSessionsListColor_Type(Integer32):
    """Custom type bfdSessionsListColor based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metroEthernet", 3),
          ("bizInternet", 4),
          ("publicInternet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_BfdSessionsListColor_Type.__name__ = "Integer32"
_BfdSessionsListColor_Object = MibTableColumn
bfdSessionsListColor = _BfdSessionsListColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 1, 1, 9),
    _BfdSessionsListColor_Type()
)
bfdSessionsListColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessionsListColor.setStatus("current")
_BfdSessionsListState_Type = BfdmgrStateEnum
_BfdSessionsListState_Object = MibTableColumn
bfdSessionsListState = _BfdSessionsListState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 1, 1, 10),
    _BfdSessionsListState_Type()
)
bfdSessionsListState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessionsListState.setStatus("current")
_BfdSessionsListDetectMultiplier_Type = UnsignedByte
_BfdSessionsListDetectMultiplier_Object = MibTableColumn
bfdSessionsListDetectMultiplier = _BfdSessionsListDetectMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 1, 1, 11),
    _BfdSessionsListDetectMultiplier_Type()
)
bfdSessionsListDetectMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessionsListDetectMultiplier.setStatus("current")
_BfdSessionsListTxInterval_Type = Unsigned32
_BfdSessionsListTxInterval_Object = MibTableColumn
bfdSessionsListTxInterval = _BfdSessionsListTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 1, 1, 12),
    _BfdSessionsListTxInterval_Type()
)
bfdSessionsListTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessionsListTxInterval.setStatus("current")
_BfdSessionsListUptime_Type = String
_BfdSessionsListUptime_Object = MibTableColumn
bfdSessionsListUptime = _BfdSessionsListUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 1, 1, 13),
    _BfdSessionsListUptime_Type()
)
bfdSessionsListUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessionsListUptime.setStatus("current")
_BfdSessionsListTransitions_Type = Integer32
_BfdSessionsListTransitions_Object = MibTableColumn
bfdSessionsListTransitions = _BfdSessionsListTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 1, 1, 14),
    _BfdSessionsListTransitions_Type()
)
bfdSessionsListTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessionsListTransitions.setStatus("current")
_BfdHistoryListTable_Object = MibTable
bfdHistoryListTable = _BfdHistoryListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 2)
)
if mibBuilder.loadTexts:
    bfdHistoryListTable.setStatus("current")
_BfdHistoryListEntry_Object = MibTableRow
bfdHistoryListEntry = _BfdHistoryListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 2, 1)
)
bfdHistoryListEntry.setIndexNames(
    (0, "CISCO-SDWAN-BFD-MIB", "bfdHistoryListSrcIp"),
    (0, "CISCO-SDWAN-BFD-MIB", "bfdHistoryListDstIp"),
    (0, "CISCO-SDWAN-BFD-MIB", "bfdHistoryListProto"),
    (0, "CISCO-SDWAN-BFD-MIB", "bfdHistoryListSrcPort"),
    (0, "CISCO-SDWAN-BFD-MIB", "bfdHistoryListDstPort"),
    (0, "CISCO-SDWAN-BFD-MIB", "bfdHistoryListIndex"),
)
if mibBuilder.loadTexts:
    bfdHistoryListEntry.setStatus("current")
_BfdHistoryListSrcIp_Type = InetAddressIP
_BfdHistoryListSrcIp_Object = MibTableColumn
bfdHistoryListSrcIp = _BfdHistoryListSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 2, 1, 1),
    _BfdHistoryListSrcIp_Type()
)
bfdHistoryListSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdHistoryListSrcIp.setStatus("current")
_BfdHistoryListDstIp_Type = InetAddressIP
_BfdHistoryListDstIp_Object = MibTableColumn
bfdHistoryListDstIp = _BfdHistoryListDstIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 2, 1, 2),
    _BfdHistoryListDstIp_Type()
)
bfdHistoryListDstIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdHistoryListDstIp.setStatus("current")


class _BfdHistoryListProto_Type(Integer32):
    """Custom type bfdHistoryListProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_BfdHistoryListProto_Type.__name__ = "Integer32"
_BfdHistoryListProto_Object = MibTableColumn
bfdHistoryListProto = _BfdHistoryListProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 2, 1, 3),
    _BfdHistoryListProto_Type()
)
bfdHistoryListProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdHistoryListProto.setStatus("current")
_BfdHistoryListSrcPort_Type = UnsignedShort
_BfdHistoryListSrcPort_Object = MibTableColumn
bfdHistoryListSrcPort = _BfdHistoryListSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 2, 1, 4),
    _BfdHistoryListSrcPort_Type()
)
bfdHistoryListSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdHistoryListSrcPort.setStatus("current")
_BfdHistoryListDstPort_Type = UnsignedShort
_BfdHistoryListDstPort_Object = MibTableColumn
bfdHistoryListDstPort = _BfdHistoryListDstPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 2, 1, 5),
    _BfdHistoryListDstPort_Type()
)
bfdHistoryListDstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdHistoryListDstPort.setStatus("current")
_BfdHistoryListIndex_Type = Unsigned32
_BfdHistoryListIndex_Object = MibTableColumn
bfdHistoryListIndex = _BfdHistoryListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 2, 1, 6),
    _BfdHistoryListIndex_Type()
)
bfdHistoryListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdHistoryListIndex.setStatus("current")
_BfdHistoryListSystemIp_Type = InetAddressIP
_BfdHistoryListSystemIp_Object = MibTableColumn
bfdHistoryListSystemIp = _BfdHistoryListSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 2, 1, 7),
    _BfdHistoryListSystemIp_Type()
)
bfdHistoryListSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdHistoryListSystemIp.setStatus("current")
_BfdHistoryListSiteId_Type = Unsigned32
_BfdHistoryListSiteId_Object = MibTableColumn
bfdHistoryListSiteId = _BfdHistoryListSiteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 2, 1, 8),
    _BfdHistoryListSiteId_Type()
)
bfdHistoryListSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdHistoryListSiteId.setStatus("current")


class _BfdHistoryListColor_Type(Integer32):
    """Custom type bfdHistoryListColor based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metroEthernet", 3),
          ("bizInternet", 4),
          ("publicInternet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_BfdHistoryListColor_Type.__name__ = "Integer32"
_BfdHistoryListColor_Object = MibTableColumn
bfdHistoryListColor = _BfdHistoryListColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 2, 1, 9),
    _BfdHistoryListColor_Type()
)
bfdHistoryListColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdHistoryListColor.setStatus("current")
_BfdHistoryListState_Type = BfdmgrStateEnum
_BfdHistoryListState_Object = MibTableColumn
bfdHistoryListState = _BfdHistoryListState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 2, 1, 10),
    _BfdHistoryListState_Type()
)
bfdHistoryListState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdHistoryListState.setStatus("current")
_BfdHistoryListTime_Type = String
_BfdHistoryListTime_Object = MibTableColumn
bfdHistoryListTime = _BfdHistoryListTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 2, 1, 11),
    _BfdHistoryListTime_Type()
)
bfdHistoryListTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdHistoryListTime.setStatus("current")
_BfdHistoryListRxPkts_Type = Counter64
_BfdHistoryListRxPkts_Object = MibTableColumn
bfdHistoryListRxPkts = _BfdHistoryListRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 2, 1, 12),
    _BfdHistoryListRxPkts_Type()
)
bfdHistoryListRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdHistoryListRxPkts.setStatus("current")
_BfdHistoryListTxPkts_Type = Counter64
_BfdHistoryListTxPkts_Object = MibTableColumn
bfdHistoryListTxPkts = _BfdHistoryListTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 2, 1, 13),
    _BfdHistoryListTxPkts_Type()
)
bfdHistoryListTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdHistoryListTxPkts.setStatus("current")
_BfdHistoryListDel_Type = UnsignedByte
_BfdHistoryListDel_Object = MibTableColumn
bfdHistoryListDel = _BfdHistoryListDel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 2, 1, 14),
    _BfdHistoryListDel_Type()
)
bfdHistoryListDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdHistoryListDel.setStatus("current")


class _BfdHistoryListFlags_Type(String):
    """Custom type bfdHistoryListFlags based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BfdHistoryListFlags_Type.__name__ = "String"
_BfdHistoryListFlags_Object = MibTableColumn
bfdHistoryListFlags = _BfdHistoryListFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 2, 1, 15),
    _BfdHistoryListFlags_Type()
)
bfdHistoryListFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdHistoryListFlags.setStatus("current")
_BfdSummary_ObjectIdentity = ObjectIdentity
bfdSummary = _BfdSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 5)
)
_BfdSummaryBfdSessionsTotal_Type = Unsigned32
_BfdSummaryBfdSessionsTotal_Object = MibScalar
bfdSummaryBfdSessionsTotal = _BfdSummaryBfdSessionsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 5, 1),
    _BfdSummaryBfdSessionsTotal_Type()
)
bfdSummaryBfdSessionsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSummaryBfdSessionsTotal.setStatus("current")
_BfdSummaryBfdSessionsUp_Type = Unsigned32
_BfdSummaryBfdSessionsUp_Object = MibScalar
bfdSummaryBfdSessionsUp = _BfdSummaryBfdSessionsUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 5, 2),
    _BfdSummaryBfdSessionsUp_Type()
)
bfdSummaryBfdSessionsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSummaryBfdSessionsUp.setStatus("current")
_BfdSummaryBfdSessionsMax_Type = Unsigned32
_BfdSummaryBfdSessionsMax_Object = MibScalar
bfdSummaryBfdSessionsMax = _BfdSummaryBfdSessionsMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 5, 3),
    _BfdSummaryBfdSessionsMax_Type()
)
bfdSummaryBfdSessionsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSummaryBfdSessionsMax.setStatus("current")
_BfdSummaryBfdSessionsFlap_Type = Unsigned32
_BfdSummaryBfdSessionsFlap_Object = MibScalar
bfdSummaryBfdSessionsFlap = _BfdSummaryBfdSessionsFlap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 5, 4),
    _BfdSummaryBfdSessionsFlap_Type()
)
bfdSummaryBfdSessionsFlap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSummaryBfdSessionsFlap.setStatus("current")
_BfdSummaryPollInterval_Type = Unsigned32
_BfdSummaryPollInterval_Object = MibScalar
bfdSummaryPollInterval = _BfdSummaryPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 5, 5),
    _BfdSummaryPollInterval_Type()
)
bfdSummaryPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSummaryPollInterval.setStatus("current")
_BfdSummaryBfdSessionsUpSuspended_Type = Unsigned32
_BfdSummaryBfdSessionsUpSuspended_Object = MibScalar
bfdSummaryBfdSessionsUpSuspended = _BfdSummaryBfdSessionsUpSuspended_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 5, 6),
    _BfdSummaryBfdSessionsUpSuspended_Type()
)
bfdSummaryBfdSessionsUpSuspended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSummaryBfdSessionsUpSuspended.setStatus("current")
_BfdSummaryBfdSessionsDownSuspended_Type = Unsigned32
_BfdSummaryBfdSessionsDownSuspended_Object = MibScalar
bfdSummaryBfdSessionsDownSuspended = _BfdSummaryBfdSessionsDownSuspended_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 5, 7),
    _BfdSummaryBfdSessionsDownSuspended_Type()
)
bfdSummaryBfdSessionsDownSuspended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSummaryBfdSessionsDownSuspended.setStatus("current")
_BfdTlocSummaryListTable_Object = MibTable
bfdTlocSummaryListTable = _BfdTlocSummaryListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 6)
)
if mibBuilder.loadTexts:
    bfdTlocSummaryListTable.setStatus("current")
_BfdTlocSummaryListEntry_Object = MibTableRow
bfdTlocSummaryListEntry = _BfdTlocSummaryListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 6, 1)
)
bfdTlocSummaryListEntry.setIndexNames(
    (0, "CISCO-SDWAN-BFD-MIB", "bfdTlocSummaryListIfName"),
    (0, "CISCO-SDWAN-BFD-MIB", "bfdTlocSummaryListEncap"),
)
if mibBuilder.loadTexts:
    bfdTlocSummaryListEntry.setStatus("current")


class _BfdTlocSummaryListIfName_Type(String):
    """Custom type bfdTlocSummaryListIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BfdTlocSummaryListIfName_Type.__name__ = "String"
_BfdTlocSummaryListIfName_Object = MibTableColumn
bfdTlocSummaryListIfName = _BfdTlocSummaryListIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 6, 1, 1),
    _BfdTlocSummaryListIfName_Type()
)
bfdTlocSummaryListIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdTlocSummaryListIfName.setStatus("current")


class _BfdTlocSummaryListEncap_Type(Integer32):
    """Custom type bfdTlocSummaryListEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_BfdTlocSummaryListEncap_Type.__name__ = "Integer32"
_BfdTlocSummaryListEncap_Object = MibTableColumn
bfdTlocSummaryListEncap = _BfdTlocSummaryListEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 6, 1, 2),
    _BfdTlocSummaryListEncap_Type()
)
bfdTlocSummaryListEncap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdTlocSummaryListEncap.setStatus("current")
_BfdTlocSummaryListSessionsTotal_Type = Unsigned32
_BfdTlocSummaryListSessionsTotal_Object = MibTableColumn
bfdTlocSummaryListSessionsTotal = _BfdTlocSummaryListSessionsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 6, 1, 3),
    _BfdTlocSummaryListSessionsTotal_Type()
)
bfdTlocSummaryListSessionsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdTlocSummaryListSessionsTotal.setStatus("current")
_BfdTlocSummaryListSessionsUp_Type = Unsigned32
_BfdTlocSummaryListSessionsUp_Object = MibTableColumn
bfdTlocSummaryListSessionsUp = _BfdTlocSummaryListSessionsUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 6, 1, 4),
    _BfdTlocSummaryListSessionsUp_Type()
)
bfdTlocSummaryListSessionsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdTlocSummaryListSessionsUp.setStatus("current")
_BfdTlocSummaryListSessionsFlap_Type = Unsigned32
_BfdTlocSummaryListSessionsFlap_Object = MibTableColumn
bfdTlocSummaryListSessionsFlap = _BfdTlocSummaryListSessionsFlap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 6, 1, 5),
    _BfdTlocSummaryListSessionsFlap_Type()
)
bfdTlocSummaryListSessionsFlap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdTlocSummaryListSessionsFlap.setStatus("current")
_BfdTlocSummaryListSessionsUpSuspended_Type = Unsigned32
_BfdTlocSummaryListSessionsUpSuspended_Object = MibTableColumn
bfdTlocSummaryListSessionsUpSuspended = _BfdTlocSummaryListSessionsUpSuspended_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 6, 1, 6),
    _BfdTlocSummaryListSessionsUpSuspended_Type()
)
bfdTlocSummaryListSessionsUpSuspended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdTlocSummaryListSessionsUpSuspended.setStatus("current")
_BfdTlocSummaryListSessionsDownSuspended_Type = Unsigned32
_BfdTlocSummaryListSessionsDownSuspended_Object = MibTableColumn
bfdTlocSummaryListSessionsDownSuspended = _BfdTlocSummaryListSessionsDownSuspended_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 1, 1, 6, 1, 7),
    _BfdTlocSummaryListSessionsDownSuspended_Type()
)
bfdTlocSummaryListSessionsDownSuspended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdTlocSummaryListSessionsDownSuspended.setStatus("current")
_CiscoSdwanBfdMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoSdwanBfdMIBNotifObjects = _CiscoSdwanBfdMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2)
)
_NetconfNotificationSeverity_Type = NotificationSeverity
_NetconfNotificationSeverity_Object = MibScalar
netconfNotificationSeverity = _NetconfNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 2),
    _NetconfNotificationSeverity_Type()
)
netconfNotificationSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netconfNotificationSeverity.setStatus("current")
_CiscoSdwanBfdSourceIp_Type = InetAddressIP
_CiscoSdwanBfdSourceIp_Object = MibScalar
ciscoSdwanBfdSourceIp = _CiscoSdwanBfdSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 3),
    _CiscoSdwanBfdSourceIp_Type()
)
ciscoSdwanBfdSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdSourceIp.setStatus("current")
_CiscoSdwanBfdDestinationIp_Type = InetAddressIP
_CiscoSdwanBfdDestinationIp_Object = MibScalar
ciscoSdwanBfdDestinationIp = _CiscoSdwanBfdDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 4),
    _CiscoSdwanBfdDestinationIp_Type()
)
ciscoSdwanBfdDestinationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdDestinationIp.setStatus("current")
_CiscoSdwanBfdProtocol_Type = Unsigned32
_CiscoSdwanBfdProtocol_Object = MibScalar
ciscoSdwanBfdProtocol = _CiscoSdwanBfdProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 5),
    _CiscoSdwanBfdProtocol_Type()
)
ciscoSdwanBfdProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdProtocol.setStatus("current")
_CiscoSdwanBfdSourcePort_Type = UnsignedShort
_CiscoSdwanBfdSourcePort_Object = MibScalar
ciscoSdwanBfdSourcePort = _CiscoSdwanBfdSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 6),
    _CiscoSdwanBfdSourcePort_Type()
)
ciscoSdwanBfdSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdSourcePort.setStatus("current")
_CiscoSdwanBfdDestinationPort_Type = UnsignedShort
_CiscoSdwanBfdDestinationPort_Object = MibScalar
ciscoSdwanBfdDestinationPort = _CiscoSdwanBfdDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 7),
    _CiscoSdwanBfdDestinationPort_Type()
)
ciscoSdwanBfdDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdDestinationPort.setStatus("current")
_CiscoSdwanBfdLocalSystemIp_Type = InetAddressIP
_CiscoSdwanBfdLocalSystemIp_Object = MibScalar
ciscoSdwanBfdLocalSystemIp = _CiscoSdwanBfdLocalSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 8),
    _CiscoSdwanBfdLocalSystemIp_Type()
)
ciscoSdwanBfdLocalSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdLocalSystemIp.setStatus("current")
_CiscoSdwanBfdLocalColor_Type = OctetString
_CiscoSdwanBfdLocalColor_Object = MibScalar
ciscoSdwanBfdLocalColor = _CiscoSdwanBfdLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 9),
    _CiscoSdwanBfdLocalColor_Type()
)
ciscoSdwanBfdLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdLocalColor.setStatus("current")
_CiscoSdwanBfdRemoteSystemIp_Type = InetAddressIP
_CiscoSdwanBfdRemoteSystemIp_Object = MibScalar
ciscoSdwanBfdRemoteSystemIp = _CiscoSdwanBfdRemoteSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 10),
    _CiscoSdwanBfdRemoteSystemIp_Type()
)
ciscoSdwanBfdRemoteSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdRemoteSystemIp.setStatus("current")
_CiscoSdwanBfdRemoteColor_Type = OctetString
_CiscoSdwanBfdRemoteColor_Object = MibScalar
ciscoSdwanBfdRemoteColor = _CiscoSdwanBfdRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 11),
    _CiscoSdwanBfdRemoteColor_Type()
)
ciscoSdwanBfdRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdRemoteColor.setStatus("current")
_CiscoSdwanBfdNewState_Type = OperState
_CiscoSdwanBfdNewState_Object = MibScalar
ciscoSdwanBfdNewState = _CiscoSdwanBfdNewState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 12),
    _CiscoSdwanBfdNewState_Type()
)
ciscoSdwanBfdNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdNewState.setStatus("current")
_CiscoSdwanBfdDeleted_Type = Unsigned32
_CiscoSdwanBfdDeleted_Object = MibScalar
ciscoSdwanBfdDeleted = _CiscoSdwanBfdDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 13),
    _CiscoSdwanBfdDeleted_Type()
)
ciscoSdwanBfdDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdDeleted.setStatus("current")
_CiscoSdwanBfdFlapReason_Type = Unsigned32
_CiscoSdwanBfdFlapReason_Object = MibScalar
ciscoSdwanBfdFlapReason = _CiscoSdwanBfdFlapReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 14),
    _CiscoSdwanBfdFlapReason_Type()
)
ciscoSdwanBfdFlapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdFlapReason.setStatus("current")
_CiscoSdwanBfdSrcIp_Type = InetAddressIP
_CiscoSdwanBfdSrcIp_Object = MibScalar
ciscoSdwanBfdSrcIp = _CiscoSdwanBfdSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 15),
    _CiscoSdwanBfdSrcIp_Type()
)
ciscoSdwanBfdSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdSrcIp.setStatus("current")
_CiscoSdwanBfdDstIp_Type = InetAddressIP
_CiscoSdwanBfdDstIp_Object = MibScalar
ciscoSdwanBfdDstIp = _CiscoSdwanBfdDstIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 16),
    _CiscoSdwanBfdDstIp_Type()
)
ciscoSdwanBfdDstIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdDstIp.setStatus("current")
_CiscoSdwanBfdProto_Type = Unsigned32
_CiscoSdwanBfdProto_Object = MibScalar
ciscoSdwanBfdProto = _CiscoSdwanBfdProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 17),
    _CiscoSdwanBfdProto_Type()
)
ciscoSdwanBfdProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdProto.setStatus("current")
_CiscoSdwanBfdSrcPort_Type = UnsignedShort
_CiscoSdwanBfdSrcPort_Object = MibScalar
ciscoSdwanBfdSrcPort = _CiscoSdwanBfdSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 18),
    _CiscoSdwanBfdSrcPort_Type()
)
ciscoSdwanBfdSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdSrcPort.setStatus("current")
_CiscoSdwanBfdDstPort_Type = UnsignedShort
_CiscoSdwanBfdDstPort_Object = MibScalar
ciscoSdwanBfdDstPort = _CiscoSdwanBfdDstPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 19),
    _CiscoSdwanBfdDstPort_Type()
)
ciscoSdwanBfdDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdDstPort.setStatus("current")
_CoSdwanBfdLocalColor_Type = OctetString
_CoSdwanBfdLocalColor_Object = MibScalar
coSdwanBfdLocalColor = _CoSdwanBfdLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 22),
    _CoSdwanBfdLocalColor_Type()
)
coSdwanBfdLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coSdwanBfdLocalColor.setStatus("current")
_CiscoSdwanBfdAppProbePFRStats_Type = OctetString
_CiscoSdwanBfdAppProbePFRStats_Object = MibScalar
ciscoSdwanBfdAppProbePFRStats = _CiscoSdwanBfdAppProbePFRStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 25),
    _CiscoSdwanBfdAppProbePFRStats_Type()
)
ciscoSdwanBfdAppProbePFRStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdAppProbePFRStats.setStatus("current")
_CiscoSdwanBfdSlaClasses_Type = OctetString
_CiscoSdwanBfdSlaClasses_Object = MibScalar
ciscoSdwanBfdSlaClasses = _CiscoSdwanBfdSlaClasses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 26),
    _CiscoSdwanBfdSlaClasses_Type()
)
ciscoSdwanBfdSlaClasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdSlaClasses.setStatus("current")
_CiscoSdwanBfdOldSlaClasses_Type = OctetString
_CiscoSdwanBfdOldSlaClasses_Object = MibScalar
ciscoSdwanBfdOldSlaClasses = _CiscoSdwanBfdOldSlaClasses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 2, 27),
    _CiscoSdwanBfdOldSlaClasses_Type()
)
ciscoSdwanBfdOldSlaClasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanBfdOldSlaClasses.setStatus("current")
_CiscoSdwanBfdMIBConform_ObjectIdentity = ObjectIdentity
ciscoSdwanBfdMIBConform = _CiscoSdwanBfdMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 3)
)
_CiscoSdwanBfdMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSdwanBfdMIBCompliances = _CiscoSdwanBfdMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 3, 1)
)
_CiscoSdwanBfdMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSdwanBfdMIBGroups = _CiscoSdwanBfdMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 3, 2)
)

# Managed Objects groups

cSdwanBfdSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 3, 2, 1)
)
cSdwanBfdSummaryGroup.setObjects(
      *(("CISCO-SDWAN-BFD-MIB", "bfdSummaryBfdSessionsTotal"),
        ("CISCO-SDWAN-BFD-MIB", "bfdSummaryBfdSessionsUp"),
        ("CISCO-SDWAN-BFD-MIB", "bfdSummaryBfdSessionsMax"),
        ("CISCO-SDWAN-BFD-MIB", "bfdSummaryBfdSessionsFlap"),
        ("CISCO-SDWAN-BFD-MIB", "bfdSummaryPollInterval"),
        ("CISCO-SDWAN-BFD-MIB", "bfdSummaryBfdSessionsUpSuspended"),
        ("CISCO-SDWAN-BFD-MIB", "bfdSummaryBfdSessionsDownSuspended"))
)
if mibBuilder.loadTexts:
    cSdwanBfdSummaryGroup.setStatus("current")

cSdwanBfdSessionsListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 3, 2, 2)
)
cSdwanBfdSessionsListGroup.setObjects(
      *(("CISCO-SDWAN-BFD-MIB", "bfdSessionsListSystemIp"),
        ("CISCO-SDWAN-BFD-MIB", "bfdSessionsListSiteId"),
        ("CISCO-SDWAN-BFD-MIB", "bfdSessionsListLocalColor"),
        ("CISCO-SDWAN-BFD-MIB", "bfdSessionsListColor"),
        ("CISCO-SDWAN-BFD-MIB", "bfdSessionsListState"),
        ("CISCO-SDWAN-BFD-MIB", "bfdSessionsListDetectMultiplier"),
        ("CISCO-SDWAN-BFD-MIB", "bfdSessionsListTxInterval"),
        ("CISCO-SDWAN-BFD-MIB", "bfdSessionsListUptime"),
        ("CISCO-SDWAN-BFD-MIB", "bfdSessionsListTransitions"))
)
if mibBuilder.loadTexts:
    cSdwanBfdSessionsListGroup.setStatus("current")

cSdwanBfdHistoryListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 3, 2, 3)
)
cSdwanBfdHistoryListGroup.setObjects(
      *(("CISCO-SDWAN-BFD-MIB", "bfdHistoryListSystemIp"),
        ("CISCO-SDWAN-BFD-MIB", "bfdHistoryListSiteId"),
        ("CISCO-SDWAN-BFD-MIB", "bfdHistoryListColor"),
        ("CISCO-SDWAN-BFD-MIB", "bfdHistoryListState"),
        ("CISCO-SDWAN-BFD-MIB", "bfdHistoryListTime"),
        ("CISCO-SDWAN-BFD-MIB", "bfdHistoryListRxPkts"),
        ("CISCO-SDWAN-BFD-MIB", "bfdHistoryListTxPkts"),
        ("CISCO-SDWAN-BFD-MIB", "bfdHistoryListDel"),
        ("CISCO-SDWAN-BFD-MIB", "bfdHistoryListFlags"))
)
if mibBuilder.loadTexts:
    cSdwanBfdHistoryListGroup.setStatus("current")

cSdwanBfdTlocSummaryListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 3, 2, 4)
)
cSdwanBfdTlocSummaryListGroup.setObjects(
      *(("CISCO-SDWAN-BFD-MIB", "bfdTlocSummaryListSessionsTotal"),
        ("CISCO-SDWAN-BFD-MIB", "bfdTlocSummaryListSessionsUp"),
        ("CISCO-SDWAN-BFD-MIB", "bfdTlocSummaryListSessionsFlap"),
        ("CISCO-SDWAN-BFD-MIB", "bfdTlocSummaryListSessionsUpSuspended"),
        ("CISCO-SDWAN-BFD-MIB", "bfdTlocSummaryListSessionsDownSuspended"))
)
if mibBuilder.loadTexts:
    cSdwanBfdTlocSummaryListGroup.setStatus("current")

cSdwanBfdNotifObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 3, 2, 5)
)
cSdwanBfdNotifObjsGroup.setObjects(
      *(("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdSourceIp"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdDestinationIp"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdProto"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdSourcePort"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdDestinationPort"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdLocalSystemIp"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdLocalColor"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdRemoteSystemIp"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdRemoteColor"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdNewState"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdDeleted"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdFlapReason"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdSuspendState"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdSrcIp"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdDstIp"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdProto"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdSrcPort"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdDstPort"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdLocalSystemIp"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdLocalColor"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdRemoteSystemIp"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdRemoteColor"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdAppProbePFRStats"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdSlaClasses"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdOldSlaClasses"))
)
if mibBuilder.loadTexts:
    cSdwanBfdNotifObjsGroup.setStatus("current")


# Notification objects

ciscoSdwanBfdStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 0, 1)
)
ciscoSdwanBfdStateChange.setObjects(
      *(("CISCO-SDWAN-BFD-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdSourceIp"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdDestinationIp"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdProto"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdSourcePort"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdDestinationPort"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdLocalSystemIp"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdLocalColor"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdRemoteSystemIp"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdRemoteColor"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdNewState"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdDeleted"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdFlapReason"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdSuspendState"))
)
if mibBuilder.loadTexts:
    ciscoSdwanBfdStateChange.setStatus(
        "current"
    )

ciscoSdwanBfdSlaChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 0, 2)
)
ciscoSdwanBfdSlaChange.setObjects(
      *(("CISCO-SDWAN-BFD-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdSrcIp"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdDstIp"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdProto"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdSrcPort"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdDstPort"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdLocalSystemIp"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdLocalColor"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdRemoteSystemIp"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdRemoteColor"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdAppProbePFRStats"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdSlaClasses"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdOldSlaClasses"))
)
if mibBuilder.loadTexts:
    ciscoSdwanBfdSlaChange.setStatus(
        "current"
    )


# Notifications groups

cSdwanOperSystemNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 3, 2, 6)
)
cSdwanOperSystemNotifsGroup.setObjects(
      *(("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdStateChange"),
        ("CISCO-SDWAN-BFD-MIB", "ciscoSdwanBfdSlaChange"))
)
if mibBuilder.loadTexts:
    cSdwanOperSystemNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSdwanBfdMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 1002, 3, 1, 1)
)
ciscoSdwanBfdMIBCompliance.setObjects(
      *(("CISCO-SDWAN-BFD-MIB", "cSdwanBfdSummaryGroup"),
        ("CISCO-SDWAN-BFD-MIB", "cSdwanBfdSessionsListGroup"),
        ("CISCO-SDWAN-BFD-MIB", "cSdwanBfdHistoryListGroup"),
        ("CISCO-SDWAN-BFD-MIB", "cSdwanBfdTlocSummaryListGroup"),
        ("CISCO-SDWAN-BFD-MIB", "cSdwanBfdNotifObjsGroup"))
)
if mibBuilder.loadTexts:
    ciscoSdwanBfdMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SDWAN-BFD-MIB",
    **{"InetAddressIP": InetAddressIP,
       "UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "String": String,
       "BfdmgrStateEnum": BfdmgrStateEnum,
       "NotificationSeverity": NotificationSeverity,
       "OperState": OperState,
       "ciscoSdwanBfdMIB": ciscoSdwanBfdMIB,
       "ciscoSdwanBfdMIBNotifs": ciscoSdwanBfdMIBNotifs,
       "ciscoSdwanBfdStateChange": ciscoSdwanBfdStateChange,
       "ciscoSdwanBfdSlaChange": ciscoSdwanBfdSlaChange,
       "ciscoSdwanBfdMIBObjects": ciscoSdwanBfdMIBObjects,
       "bfd": bfd,
       "bfdSessionsListTable": bfdSessionsListTable,
       "bfdSessionsListEntry": bfdSessionsListEntry,
       "bfdSessionsListSrcIp": bfdSessionsListSrcIp,
       "bfdSessionsListDstIp": bfdSessionsListDstIp,
       "bfdSessionsListProto": bfdSessionsListProto,
       "bfdSessionsListSrcPort": bfdSessionsListSrcPort,
       "bfdSessionsListDstPort": bfdSessionsListDstPort,
       "bfdSessionsListSystemIp": bfdSessionsListSystemIp,
       "bfdSessionsListSiteId": bfdSessionsListSiteId,
       "bfdSessionsListLocalColor": bfdSessionsListLocalColor,
       "bfdSessionsListColor": bfdSessionsListColor,
       "bfdSessionsListState": bfdSessionsListState,
       "bfdSessionsListDetectMultiplier": bfdSessionsListDetectMultiplier,
       "bfdSessionsListTxInterval": bfdSessionsListTxInterval,
       "bfdSessionsListUptime": bfdSessionsListUptime,
       "bfdSessionsListTransitions": bfdSessionsListTransitions,
       "bfdHistoryListTable": bfdHistoryListTable,
       "bfdHistoryListEntry": bfdHistoryListEntry,
       "bfdHistoryListSrcIp": bfdHistoryListSrcIp,
       "bfdHistoryListDstIp": bfdHistoryListDstIp,
       "bfdHistoryListProto": bfdHistoryListProto,
       "bfdHistoryListSrcPort": bfdHistoryListSrcPort,
       "bfdHistoryListDstPort": bfdHistoryListDstPort,
       "bfdHistoryListIndex": bfdHistoryListIndex,
       "bfdHistoryListSystemIp": bfdHistoryListSystemIp,
       "bfdHistoryListSiteId": bfdHistoryListSiteId,
       "bfdHistoryListColor": bfdHistoryListColor,
       "bfdHistoryListState": bfdHistoryListState,
       "bfdHistoryListTime": bfdHistoryListTime,
       "bfdHistoryListRxPkts": bfdHistoryListRxPkts,
       "bfdHistoryListTxPkts": bfdHistoryListTxPkts,
       "bfdHistoryListDel": bfdHistoryListDel,
       "bfdHistoryListFlags": bfdHistoryListFlags,
       "bfdSummary": bfdSummary,
       "bfdSummaryBfdSessionsTotal": bfdSummaryBfdSessionsTotal,
       "bfdSummaryBfdSessionsUp": bfdSummaryBfdSessionsUp,
       "bfdSummaryBfdSessionsMax": bfdSummaryBfdSessionsMax,
       "bfdSummaryBfdSessionsFlap": bfdSummaryBfdSessionsFlap,
       "bfdSummaryPollInterval": bfdSummaryPollInterval,
       "bfdSummaryBfdSessionsUpSuspended": bfdSummaryBfdSessionsUpSuspended,
       "bfdSummaryBfdSessionsDownSuspended": bfdSummaryBfdSessionsDownSuspended,
       "bfdTlocSummaryListTable": bfdTlocSummaryListTable,
       "bfdTlocSummaryListEntry": bfdTlocSummaryListEntry,
       "bfdTlocSummaryListIfName": bfdTlocSummaryListIfName,
       "bfdTlocSummaryListEncap": bfdTlocSummaryListEncap,
       "bfdTlocSummaryListSessionsTotal": bfdTlocSummaryListSessionsTotal,
       "bfdTlocSummaryListSessionsUp": bfdTlocSummaryListSessionsUp,
       "bfdTlocSummaryListSessionsFlap": bfdTlocSummaryListSessionsFlap,
       "bfdTlocSummaryListSessionsUpSuspended": bfdTlocSummaryListSessionsUpSuspended,
       "bfdTlocSummaryListSessionsDownSuspended": bfdTlocSummaryListSessionsDownSuspended,
       "ciscoSdwanBfdMIBNotifObjects": ciscoSdwanBfdMIBNotifObjects,
       "netconfNotificationSeverity": netconfNotificationSeverity,
       "ciscoSdwanBfdSourceIp": ciscoSdwanBfdSourceIp,
       "ciscoSdwanBfdDestinationIp": ciscoSdwanBfdDestinationIp,
       "ciscoSdwanBfdProtocol": ciscoSdwanBfdProtocol,
       "ciscoSdwanBfdSourcePort": ciscoSdwanBfdSourcePort,
       "ciscoSdwanBfdDestinationPort": ciscoSdwanBfdDestinationPort,
       "ciscoSdwanBfdLocalSystemIp": ciscoSdwanBfdLocalSystemIp,
       "ciscoSdwanBfdLocalColor": ciscoSdwanBfdLocalColor,
       "ciscoSdwanBfdRemoteSystemIp": ciscoSdwanBfdRemoteSystemIp,
       "ciscoSdwanBfdRemoteColor": ciscoSdwanBfdRemoteColor,
       "ciscoSdwanBfdNewState": ciscoSdwanBfdNewState,
       "ciscoSdwanBfdDeleted": ciscoSdwanBfdDeleted,
       "ciscoSdwanBfdFlapReason": ciscoSdwanBfdFlapReason,
       "ciscoSdwanBfdSrcIp": ciscoSdwanBfdSrcIp,
       "ciscoSdwanBfdDstIp": ciscoSdwanBfdDstIp,
       "ciscoSdwanBfdProto": ciscoSdwanBfdProto,
       "ciscoSdwanBfdSrcPort": ciscoSdwanBfdSrcPort,
       "ciscoSdwanBfdDstPort": ciscoSdwanBfdDstPort,
       "coSdwanBfdLocalColor": coSdwanBfdLocalColor,
       "ciscoSdwanBfdAppProbePFRStats": ciscoSdwanBfdAppProbePFRStats,
       "ciscoSdwanBfdSlaClasses": ciscoSdwanBfdSlaClasses,
       "ciscoSdwanBfdOldSlaClasses": ciscoSdwanBfdOldSlaClasses,
       "ciscoSdwanBfdMIBConform": ciscoSdwanBfdMIBConform,
       "ciscoSdwanBfdMIBCompliances": ciscoSdwanBfdMIBCompliances,
       "ciscoSdwanBfdMIBCompliance": ciscoSdwanBfdMIBCompliance,
       "ciscoSdwanBfdMIBGroups": ciscoSdwanBfdMIBGroups,
       "cSdwanBfdSummaryGroup": cSdwanBfdSummaryGroup,
       "cSdwanBfdSessionsListGroup": cSdwanBfdSessionsListGroup,
       "cSdwanBfdHistoryListGroup": cSdwanBfdHistoryListGroup,
       "cSdwanBfdTlocSummaryListGroup": cSdwanBfdTlocSummaryListGroup,
       "cSdwanBfdNotifObjsGroup": cSdwanBfdNotifObjsGroup,
       "cSdwanOperSystemNotifsGroup": cSdwanOperSystemNotifsGroup}
)
