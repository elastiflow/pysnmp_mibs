# SNMP MIB module (A3COM-HUAWEI-DHCPR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-DHCPR-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:05:03 2025
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

(huaweiMgmt,
 hwDhcp) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "huaweiMgmt",
    "hwDhcp")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwDHCPRelayMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1)
)
if mibBuilder.loadTexts:
    hwDHCPRelayMib.setRevisions(
        ("2003-02-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwDHCPRelayMibObject_ObjectIdentity = ObjectIdentity
hwDHCPRelayMibObject = _HwDHCPRelayMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1)
)
_HwDHCPRIPTable_Object = MibTable
hwDHCPRIPTable = _HwDHCPRIPTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwDHCPRIPTable.setStatus("current")
_HwDHCPRIPEntry_Object = MibTableRow
hwDHCPRIPEntry = _HwDHCPRIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 1, 1)
)
hwDHCPRIPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRIPAddr"),
)
if mibBuilder.loadTexts:
    hwDHCPRIPEntry.setStatus("current")
_HwDHCPRIPAddr_Type = IpAddress
_HwDHCPRIPAddr_Object = MibTableColumn
hwDHCPRIPAddr = _HwDHCPRIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 1, 1, 1),
    _HwDHCPRIPAddr_Type()
)
hwDHCPRIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPRIPAddr.setStatus("current")
_HwDHCPRIPRowStatus_Type = RowStatus
_HwDHCPRIPRowStatus_Object = MibTableColumn
hwDHCPRIPRowStatus = _HwDHCPRIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 1, 1, 2),
    _HwDHCPRIPRowStatus_Type()
)
hwDHCPRIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDHCPRIPRowStatus.setStatus("current")
_HwDHCPRSeletAllocateModeTable_Object = MibTable
hwDHCPRSeletAllocateModeTable = _HwDHCPRSeletAllocateModeTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwDHCPRSeletAllocateModeTable.setStatus("current")
_HwDHCPRSeletAllocateModeEntry_Object = MibTableRow
hwDHCPRSeletAllocateModeEntry = _HwDHCPRSeletAllocateModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 2, 1)
)
hwDHCPRSeletAllocateModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwDHCPRSeletAllocateModeEntry.setStatus("current")


class _HwDHCPRSelectAllocateMode_Type(Integer32):
    """Custom type hwDHCPRSelectAllocateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("global", 0),
          ("interface", 1),
          ("relay", 2))
    )


_HwDHCPRSelectAllocateMode_Type.__name__ = "Integer32"
_HwDHCPRSelectAllocateMode_Object = MibTableColumn
hwDHCPRSelectAllocateMode = _HwDHCPRSelectAllocateMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 2, 1, 1),
    _HwDHCPRSelectAllocateMode_Type()
)
hwDHCPRSelectAllocateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPRSelectAllocateMode.setStatus("current")


class _HwDHCPRelayCycleStatus_Type(Integer32):
    """Custom type hwDHCPRelayCycleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1))
    )


_HwDHCPRelayCycleStatus_Type.__name__ = "Integer32"
_HwDHCPRelayCycleStatus_Object = MibScalar
hwDHCPRelayCycleStatus = _HwDHCPRelayCycleStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 3),
    _HwDHCPRelayCycleStatus_Type()
)
hwDHCPRelayCycleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPRelayCycleStatus.setStatus("current")
_HwDHCPRRxBadPktNum_Type = Integer32
_HwDHCPRRxBadPktNum_Object = MibScalar
hwDHCPRRxBadPktNum = _HwDHCPRRxBadPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 4),
    _HwDHCPRRxBadPktNum_Type()
)
hwDHCPRRxBadPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPRRxBadPktNum.setStatus("current")
_HwDHCPRRxServerPktNum_Type = Integer32
_HwDHCPRRxServerPktNum_Object = MibScalar
hwDHCPRRxServerPktNum = _HwDHCPRRxServerPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 5),
    _HwDHCPRRxServerPktNum_Type()
)
hwDHCPRRxServerPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPRRxServerPktNum.setStatus("current")
_HwDHCPRTxServerPktNum_Type = Integer32
_HwDHCPRTxServerPktNum_Object = MibScalar
hwDHCPRTxServerPktNum = _HwDHCPRTxServerPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 6),
    _HwDHCPRTxServerPktNum_Type()
)
hwDHCPRTxServerPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPRTxServerPktNum.setStatus("current")
_HwDHCPRRxClientPktNum_Type = Integer32
_HwDHCPRRxClientPktNum_Object = MibScalar
hwDHCPRRxClientPktNum = _HwDHCPRRxClientPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 7),
    _HwDHCPRRxClientPktNum_Type()
)
hwDHCPRRxClientPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPRRxClientPktNum.setStatus("current")
_HwDHCPRTxClientPktNum_Type = Integer32
_HwDHCPRTxClientPktNum_Object = MibScalar
hwDHCPRTxClientPktNum = _HwDHCPRTxClientPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 8),
    _HwDHCPRTxClientPktNum_Type()
)
hwDHCPRTxClientPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPRTxClientPktNum.setStatus("current")
_HwDHCPRTxClientUniPktNum_Type = Integer32
_HwDHCPRTxClientUniPktNum_Object = MibScalar
hwDHCPRTxClientUniPktNum = _HwDHCPRTxClientUniPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 9),
    _HwDHCPRTxClientUniPktNum_Type()
)
hwDHCPRTxClientUniPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPRTxClientUniPktNum.setStatus("current")
_HwDHCPRTxClientBroPktNum_Type = Integer32
_HwDHCPRTxClientBroPktNum_Object = MibScalar
hwDHCPRTxClientBroPktNum = _HwDHCPRTxClientBroPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 10),
    _HwDHCPRTxClientBroPktNum_Type()
)
hwDHCPRTxClientBroPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPRTxClientBroPktNum.setStatus("current")
_HwDHCPRelayDiscoverPktNum_Type = Integer32
_HwDHCPRelayDiscoverPktNum_Object = MibScalar
hwDHCPRelayDiscoverPktNum = _HwDHCPRelayDiscoverPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 11),
    _HwDHCPRelayDiscoverPktNum_Type()
)
hwDHCPRelayDiscoverPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPRelayDiscoverPktNum.setStatus("current")
_HwDHCPRelayRequestPktNum_Type = Integer32
_HwDHCPRelayRequestPktNum_Object = MibScalar
hwDHCPRelayRequestPktNum = _HwDHCPRelayRequestPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 12),
    _HwDHCPRelayRequestPktNum_Type()
)
hwDHCPRelayRequestPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPRelayRequestPktNum.setStatus("current")
_HwDHCPRelayDeclinePktNum_Type = Integer32
_HwDHCPRelayDeclinePktNum_Object = MibScalar
hwDHCPRelayDeclinePktNum = _HwDHCPRelayDeclinePktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 13),
    _HwDHCPRelayDeclinePktNum_Type()
)
hwDHCPRelayDeclinePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPRelayDeclinePktNum.setStatus("current")
_HwDHCPRelayReleasePktNum_Type = Integer32
_HwDHCPRelayReleasePktNum_Object = MibScalar
hwDHCPRelayReleasePktNum = _HwDHCPRelayReleasePktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 14),
    _HwDHCPRelayReleasePktNum_Type()
)
hwDHCPRelayReleasePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPRelayReleasePktNum.setStatus("current")
_HwDHCPRelayInformPktNum_Type = Integer32
_HwDHCPRelayInformPktNum_Object = MibScalar
hwDHCPRelayInformPktNum = _HwDHCPRelayInformPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 15),
    _HwDHCPRelayInformPktNum_Type()
)
hwDHCPRelayInformPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPRelayInformPktNum.setStatus("current")
_HwDHCPRelayOfferPktNum_Type = Integer32
_HwDHCPRelayOfferPktNum_Object = MibScalar
hwDHCPRelayOfferPktNum = _HwDHCPRelayOfferPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 16),
    _HwDHCPRelayOfferPktNum_Type()
)
hwDHCPRelayOfferPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPRelayOfferPktNum.setStatus("current")
_HwDHCPRelayAckPktNum_Type = Integer32
_HwDHCPRelayAckPktNum_Object = MibScalar
hwDHCPRelayAckPktNum = _HwDHCPRelayAckPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 17),
    _HwDHCPRelayAckPktNum_Type()
)
hwDHCPRelayAckPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPRelayAckPktNum.setStatus("current")
_HwDHCPRelayNakPktNum_Type = Integer32
_HwDHCPRelayNakPktNum_Object = MibScalar
hwDHCPRelayNakPktNum = _HwDHCPRelayNakPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 18),
    _HwDHCPRelayNakPktNum_Type()
)
hwDHCPRelayNakPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPRelayNakPktNum.setStatus("current")


class _HwDHCPRelayStatisticsReset_Type(Integer32):
    """Custom type hwDHCPRelayStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("reset", 1))
    )


_HwDHCPRelayStatisticsReset_Type.__name__ = "Integer32"
_HwDHCPRelayStatisticsReset_Object = MibScalar
hwDHCPRelayStatisticsReset = _HwDHCPRelayStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 1, 19),
    _HwDHCPRelayStatisticsReset_Type()
)
hwDHCPRelayStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPRelayStatisticsReset.setStatus("current")
_HwDHCPRelayMIBConformance_ObjectIdentity = ObjectIdentity
hwDHCPRelayMIBConformance = _HwDHCPRelayMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 2)
)
_HwDHCPRelayMIBCompliances_ObjectIdentity = ObjectIdentity
hwDHCPRelayMIBCompliances = _HwDHCPRelayMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 2, 1)
)
_HwDHCPRelayMIBGroups_ObjectIdentity = ObjectIdentity
hwDHCPRelayMIBGroups = _HwDHCPRelayMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 2, 2)
)

# Managed Objects groups

hwDHCPRelayMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 1, 2, 2, 1)
)
hwDHCPRelayMIBGroup.setObjects(
      *(("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRIPAddr"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRIPRowStatus"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRSelectAllocateMode"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRelayCycleStatus"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRRxBadPktNum"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRRxServerPktNum"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRTxServerPktNum"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRRxClientPktNum"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRTxClientPktNum"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRTxClientUniPktNum"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRTxClientBroPktNum"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRelayDiscoverPktNum"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRelayRequestPktNum"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRelayDeclinePktNum"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRelayReleasePktNum"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRelayInformPktNum"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRelayOfferPktNum"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRelayAckPktNum"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRelayNakPktNum"),
        ("A3COM-HUAWEI-DHCPR-MIB", "hwDHCPRelayStatisticsReset"))
)
if mibBuilder.loadTexts:
    hwDHCPRelayMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-DHCPR-MIB",
    **{"hwDHCPRelayMib": hwDHCPRelayMib,
       "hwDHCPRelayMibObject": hwDHCPRelayMibObject,
       "hwDHCPRIPTable": hwDHCPRIPTable,
       "hwDHCPRIPEntry": hwDHCPRIPEntry,
       "hwDHCPRIPAddr": hwDHCPRIPAddr,
       "hwDHCPRIPRowStatus": hwDHCPRIPRowStatus,
       "hwDHCPRSeletAllocateModeTable": hwDHCPRSeletAllocateModeTable,
       "hwDHCPRSeletAllocateModeEntry": hwDHCPRSeletAllocateModeEntry,
       "hwDHCPRSelectAllocateMode": hwDHCPRSelectAllocateMode,
       "hwDHCPRelayCycleStatus": hwDHCPRelayCycleStatus,
       "hwDHCPRRxBadPktNum": hwDHCPRRxBadPktNum,
       "hwDHCPRRxServerPktNum": hwDHCPRRxServerPktNum,
       "hwDHCPRTxServerPktNum": hwDHCPRTxServerPktNum,
       "hwDHCPRRxClientPktNum": hwDHCPRRxClientPktNum,
       "hwDHCPRTxClientPktNum": hwDHCPRTxClientPktNum,
       "hwDHCPRTxClientUniPktNum": hwDHCPRTxClientUniPktNum,
       "hwDHCPRTxClientBroPktNum": hwDHCPRTxClientBroPktNum,
       "hwDHCPRelayDiscoverPktNum": hwDHCPRelayDiscoverPktNum,
       "hwDHCPRelayRequestPktNum": hwDHCPRelayRequestPktNum,
       "hwDHCPRelayDeclinePktNum": hwDHCPRelayDeclinePktNum,
       "hwDHCPRelayReleasePktNum": hwDHCPRelayReleasePktNum,
       "hwDHCPRelayInformPktNum": hwDHCPRelayInformPktNum,
       "hwDHCPRelayOfferPktNum": hwDHCPRelayOfferPktNum,
       "hwDHCPRelayAckPktNum": hwDHCPRelayAckPktNum,
       "hwDHCPRelayNakPktNum": hwDHCPRelayNakPktNum,
       "hwDHCPRelayStatisticsReset": hwDHCPRelayStatisticsReset,
       "hwDHCPRelayMIBConformance": hwDHCPRelayMIBConformance,
       "hwDHCPRelayMIBCompliances": hwDHCPRelayMIBCompliances,
       "hwDHCPRelayMIBGroups": hwDHCPRelayMIBGroups,
       "hwDHCPRelayMIBGroup": hwDHCPRelayMIBGroup}
)
