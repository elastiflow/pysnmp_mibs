# SNMP MIB module (IEEE8021-PRY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/IEEE8021-PRY-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:12:29 2025
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

(IEEE8021PriorityValue,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PriorityValue")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8021PryMIB = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 36)
)
if mibBuilder.loadTexts:
    ieee8021PryMIB.setRevisions(
        ("2022-10-31 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021PryMIBNotifications_ObjectIdentity = ObjectIdentity
ieee8021PryMIBNotifications = _Ieee8021PryMIBNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 36, 1)
)
_Ieee8021PryMIBObjects_ObjectIdentity = ObjectIdentity
ieee8021PryMIBObjects = _Ieee8021PryMIBObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 36, 2)
)
_Ieee8021PryIfTable_Object = MibTable
ieee8021PryIfTable = _Ieee8021PryIfTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021PryIfTable.setStatus("current")
_Ieee8021PryIfEntry_Object = MibTableRow
ieee8021PryIfEntry = _Ieee8021PryIfEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 1, 1)
)
ieee8021PryIfEntry.setIndexNames(
    (0, "IEEE8021-PRY-MIB", "ieee8021PryIfIndex"),
)
if mibBuilder.loadTexts:
    ieee8021PryIfEntry.setStatus("current")
_Ieee8021PryIfIndex_Type = InterfaceIndex
_Ieee8021PryIfIndex_Object = MibTableColumn
ieee8021PryIfIndex = _Ieee8021PryIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 1, 1, 1),
    _Ieee8021PryIfIndex_Type()
)
ieee8021PryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PryIfIndex.setStatus("current")


class _Ieee8021PryIfRxProtection_Type(TruthValue):
    """Custom type ieee8021PryIfRxProtection based on TruthValue"""
    defaultValue = 1


_Ieee8021PryIfRxProtection_Type.__name__ = "TruthValue"
_Ieee8021PryIfRxProtection_Object = MibTableColumn
ieee8021PryIfRxProtection = _Ieee8021PryIfRxProtection_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 1, 1, 2),
    _Ieee8021PryIfRxProtection_Type()
)
ieee8021PryIfRxProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PryIfRxProtection.setStatus("current")


class _Ieee8021PryIfTxProtection_Type(TruthValue):
    """Custom type ieee8021PryIfTxProtection based on TruthValue"""
    defaultValue = 1


_Ieee8021PryIfTxProtection_Type.__name__ = "TruthValue"
_Ieee8021PryIfTxProtection_Object = MibTableColumn
ieee8021PryIfTxProtection = _Ieee8021PryIfTxProtection_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 1, 1, 3),
    _Ieee8021PryIfTxProtection_Type()
)
ieee8021PryIfTxProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PryIfTxProtection.setStatus("current")


class _Ieee8021PryIfSecySupport_Type(TruthValue):
    """Custom type ieee8021PryIfSecySupport based on TruthValue"""
    defaultValue = 1


_Ieee8021PryIfSecySupport_Type.__name__ = "TruthValue"
_Ieee8021PryIfSecySupport_Object = MibTableColumn
ieee8021PryIfSecySupport = _Ieee8021PryIfSecySupport_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 1, 1, 4),
    _Ieee8021PryIfSecySupport_Type()
)
ieee8021PryIfSecySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryIfSecySupport.setStatus("current")
_Ieee8021PryIfAddr_Type = MacAddress
_Ieee8021PryIfAddr_Object = MibTableColumn
ieee8021PryIfAddr = _Ieee8021PryIfAddr_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 1, 1, 5),
    _Ieee8021PryIfAddr_Type()
)
ieee8021PryIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryIfAddr.setStatus("current")
_Ieee8021PryIfMppduDA_Type = MacAddress
_Ieee8021PryIfMppduDA_Object = MibTableColumn
ieee8021PryIfMppduDA = _Ieee8021PryIfMppduDA_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 1, 1, 6),
    _Ieee8021PryIfMppduDA_Type()
)
ieee8021PryIfMppduDA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PryIfMppduDA.setStatus("current")
_Ieee8021PryIfDefaultReassembly_Type = TruthValue
_Ieee8021PryIfDefaultReassembly_Object = MibTableColumn
ieee8021PryIfDefaultReassembly = _Ieee8021PryIfDefaultReassembly_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 1, 1, 7),
    _Ieee8021PryIfDefaultReassembly_Type()
)
ieee8021PryIfDefaultReassembly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryIfDefaultReassembly.setStatus("current")
_Ieee8021PryIfMaxPeers_Type = Integer32
_Ieee8021PryIfMaxPeers_Object = MibTableColumn
ieee8021PryIfMaxPeers = _Ieee8021PryIfMaxPeers_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 1, 1, 8),
    _Ieee8021PryIfMaxPeers_Type()
)
ieee8021PryIfMaxPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryIfMaxPeers.setStatus("current")
_Ieee8021PryIfNumPeers_Type = Integer32
_Ieee8021PryIfNumPeers_Object = MibTableColumn
ieee8021PryIfNumPeers = _Ieee8021PryIfNumPeers_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 1, 1, 9),
    _Ieee8021PryIfNumPeers_Type()
)
ieee8021PryIfNumPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryIfNumPeers.setStatus("current")
_Ieee8021PrySelectionTable_Object = MibTable
ieee8021PrySelectionTable = _Ieee8021PrySelectionTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 2)
)
if mibBuilder.loadTexts:
    ieee8021PrySelectionTable.setStatus("current")
_Ieee8021PrySelectionEntry_Object = MibTableRow
ieee8021PrySelectionEntry = _Ieee8021PrySelectionEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 2, 1)
)
ieee8021PrySelectionEntry.setIndexNames(
    (0, "IEEE8021-PRY-MIB", "ieee8021PryIfIndex"),
    (0, "IEEE8021-PRY-MIB", "ieee8021PrySelectionPriority"),
)
if mibBuilder.loadTexts:
    ieee8021PrySelectionEntry.setStatus("current")
_Ieee8021PrySelectionPriority_Type = IEEE8021PriorityValue
_Ieee8021PrySelectionPriority_Object = MibTableColumn
ieee8021PrySelectionPriority = _Ieee8021PrySelectionPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 2, 1, 1),
    _Ieee8021PrySelectionPriority_Type()
)
ieee8021PrySelectionPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PrySelectionPriority.setStatus("current")


class _Ieee8021PrySelectionPrivacyType_Type(Integer32):
    """Custom type ieee8021PrySelectionPrivacyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("privacyFrame", 2),
          ("preemptableChannel", 3),
          ("expressChannel", 4))
    )


_Ieee8021PrySelectionPrivacyType_Type.__name__ = "Integer32"
_Ieee8021PrySelectionPrivacyType_Object = MibTableColumn
ieee8021PrySelectionPrivacyType = _Ieee8021PrySelectionPrivacyType_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 2, 1, 2),
    _Ieee8021PrySelectionPrivacyType_Type()
)
ieee8021PrySelectionPrivacyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PrySelectionPrivacyType.setStatus("current")
_Ieee8021PryFrameTable_Object = MibTable
ieee8021PryFrameTable = _Ieee8021PryFrameTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 3)
)
if mibBuilder.loadTexts:
    ieee8021PryFrameTable.setStatus("current")
_Ieee8021PryFrameEntry_Object = MibTableRow
ieee8021PryFrameEntry = _Ieee8021PryFrameEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ieee8021PryFrameEntry.setStatus("current")
_Ieee8021PryFrameAccessPriority_Type = IEEE8021PriorityValue
_Ieee8021PryFrameAccessPriority_Object = MibTableColumn
ieee8021PryFrameAccessPriority = _Ieee8021PryFrameAccessPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 3, 1, 1),
    _Ieee8021PryFrameAccessPriority_Type()
)
ieee8021PryFrameAccessPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PryFrameAccessPriority.setStatus("current")
_Ieee8021PryFrameRevealDE_Type = TruthValue
_Ieee8021PryFrameRevealDE_Object = MibTableColumn
ieee8021PryFrameRevealDE = _Ieee8021PryFrameRevealDE_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 3, 1, 2),
    _Ieee8021PryFrameRevealDE_Type()
)
ieee8021PryFrameRevealDE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PryFrameRevealDE.setStatus("current")


class _Ieee8021PryFramePadding_Type(Integer32):
    """Custom type ieee8021PryFramePadding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("sixteen", 16),
          ("thirtyTwo", 32),
          ("sixtyFour", 64))
    )


_Ieee8021PryFramePadding_Type.__name__ = "Integer32"
_Ieee8021PryFramePadding_Object = MibTableColumn
ieee8021PryFramePadding = _Ieee8021PryFramePadding_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 3, 1, 3),
    _Ieee8021PryFramePadding_Type()
)
ieee8021PryFramePadding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PryFramePadding.setStatus("current")
_Ieee8021PryChannelTable_Object = MibTable
ieee8021PryChannelTable = _Ieee8021PryChannelTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 4)
)
if mibBuilder.loadTexts:
    ieee8021PryChannelTable.setStatus("current")
_Ieee8021PryChannelEntry_Object = MibTableRow
ieee8021PryChannelEntry = _Ieee8021PryChannelEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 4, 1)
)
ieee8021PryChannelEntry.setIndexNames(
    (0, "IEEE8021-PRY-MIB", "ieee8021PryIfIndex"),
    (0, "IEEE8021-PRY-MIB", "ieee8021PryChType"),
)
if mibBuilder.loadTexts:
    ieee8021PryChannelEntry.setStatus("current")


class _Ieee8021PryChType_Type(Integer32):
    """Custom type ieee8021PryChType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("express", 1),
          ("preemptable", 2))
    )


_Ieee8021PryChType_Type.__name__ = "Integer32"
_Ieee8021PryChType_Object = MibTableColumn
ieee8021PryChType = _Ieee8021PryChType_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 4, 1, 1),
    _Ieee8021PryChType_Type()
)
ieee8021PryChType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PryChType.setStatus("current")
_Ieee8021PryChEnable_Type = TruthValue
_Ieee8021PryChEnable_Object = MibTableColumn
ieee8021PryChEnable = _Ieee8021PryChEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 4, 1, 2),
    _Ieee8021PryChEnable_Type()
)
ieee8021PryChEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PryChEnable.setStatus("current")
_Ieee8021PryChFragmentEnable_Type = TruthValue
_Ieee8021PryChFragmentEnable_Object = MibTableColumn
ieee8021PryChFragmentEnable = _Ieee8021PryChFragmentEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 4, 1, 3),
    _Ieee8021PryChFragmentEnable_Type()
)
ieee8021PryChFragmentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PryChFragmentEnable.setStatus("current")
_Ieee8021PryChAccessPriority_Type = IEEE8021PriorityValue
_Ieee8021PryChAccessPriority_Object = MibTableColumn
ieee8021PryChAccessPriority = _Ieee8021PryChAccessPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 4, 1, 4),
    _Ieee8021PryChAccessPriority_Type()
)
ieee8021PryChAccessPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PryChAccessPriority.setStatus("current")


class _Ieee8021PryChUserDataFrameSize_Type(Integer32):
    """Custom type ieee8021PryChUserDataFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 32768),
    )


_Ieee8021PryChUserDataFrameSize_Type.__name__ = "Integer32"
_Ieee8021PryChUserDataFrameSize_Object = MibTableColumn
ieee8021PryChUserDataFrameSize = _Ieee8021PryChUserDataFrameSize_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 4, 1, 5),
    _Ieee8021PryChUserDataFrameSize_Type()
)
ieee8021PryChUserDataFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PryChUserDataFrameSize.setStatus("current")


class _Ieee8021PryChMppduGeneration_Type(Integer32):
    """Custom type ieee8021PryChMppduGeneration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("transmissionGate", 2),
          ("other", 3))
    )


_Ieee8021PryChMppduGeneration_Type.__name__ = "Integer32"
_Ieee8021PryChMppduGeneration_Object = MibTableColumn
ieee8021PryChMppduGeneration = _Ieee8021PryChMppduGeneration_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 4, 1, 6),
    _Ieee8021PryChMppduGeneration_Type()
)
ieee8021PryChMppduGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PryChMppduGeneration.setStatus("current")
_Ieee8021PryChRequestedKbitRate_Type = Unsigned32
_Ieee8021PryChRequestedKbitRate_Object = MibTableColumn
ieee8021PryChRequestedKbitRate = _Ieee8021PryChRequestedKbitRate_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 4, 1, 7),
    _Ieee8021PryChRequestedKbitRate_Type()
)
ieee8021PryChRequestedKbitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PryChRequestedKbitRate.setStatus("current")
_Ieee8021PryChMppduBitsOnWire_Type = Unsigned32
_Ieee8021PryChMppduBitsOnWire_Object = MibTableColumn
ieee8021PryChMppduBitsOnWire = _Ieee8021PryChMppduBitsOnWire_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 4, 1, 8),
    _Ieee8021PryChMppduBitsOnWire_Type()
)
ieee8021PryChMppduBitsOnWire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryChMppduBitsOnWire.setStatus("current")
_Ieee8021PryChMppduInterval_Type = Unsigned32
_Ieee8021PryChMppduInterval_Object = MibTableColumn
ieee8021PryChMppduInterval = _Ieee8021PryChMppduInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 4, 1, 9),
    _Ieee8021PryChMppduInterval_Type()
)
ieee8021PryChMppduInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryChMppduInterval.setStatus("current")
_Ieee8021PryChUserBurstOctets_Type = Unsigned32
_Ieee8021PryChUserBurstOctets_Object = MibTableColumn
ieee8021PryChUserBurstOctets = _Ieee8021PryChUserBurstOctets_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 4, 1, 10),
    _Ieee8021PryChUserBurstOctets_Type()
)
ieee8021PryChUserBurstOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PryChUserBurstOctets.setStatus("current")
_Ieee8021PryPeerTable_Object = MibTable
ieee8021PryPeerTable = _Ieee8021PryPeerTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 5)
)
if mibBuilder.loadTexts:
    ieee8021PryPeerTable.setStatus("current")
_Ieee8021PryPeerEntry_Object = MibTableRow
ieee8021PryPeerEntry = _Ieee8021PryPeerEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 5, 1)
)
ieee8021PryPeerEntry.setIndexNames(
    (0, "IEEE8021-PRY-MIB", "ieee8021PryIfIndex"),
    (0, "IEEE8021-PRY-MIB", "ieee8021PryPeerAddr"),
)
if mibBuilder.loadTexts:
    ieee8021PryPeerEntry.setStatus("current")
_Ieee8021PryPeerAddr_Type = MacAddress
_Ieee8021PryPeerAddr_Object = MibTableColumn
ieee8021PryPeerAddr = _Ieee8021PryPeerAddr_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 5, 1, 1),
    _Ieee8021PryPeerAddr_Type()
)
ieee8021PryPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PryPeerAddr.setStatus("current")
_Ieee8021PryPeerRowStatus_Type = RowStatus
_Ieee8021PryPeerRowStatus_Object = MibTableColumn
ieee8021PryPeerRowStatus = _Ieee8021PryPeerRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 5, 1, 2),
    _Ieee8021PryPeerRowStatus_Type()
)
ieee8021PryPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PryPeerRowStatus.setStatus("current")
_Ieee8021PryOutTable_Object = MibTable
ieee8021PryOutTable = _Ieee8021PryOutTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 6)
)
if mibBuilder.loadTexts:
    ieee8021PryOutTable.setStatus("current")
_Ieee8021PryOutEntry_Object = MibTableRow
ieee8021PryOutEntry = _Ieee8021PryOutEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 6, 1)
)
if mibBuilder.loadTexts:
    ieee8021PryOutEntry.setStatus("current")
_Ieee8021PryOutPrivacyFrames_Type = Counter64
_Ieee8021PryOutPrivacyFrames_Object = MibTableColumn
ieee8021PryOutPrivacyFrames = _Ieee8021PryOutPrivacyFrames_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 6, 1, 1),
    _Ieee8021PryOutPrivacyFrames_Type()
)
ieee8021PryOutPrivacyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryOutPrivacyFrames.setStatus("current")
_Ieee8021PryOutPfUserOctets_Type = Counter64
_Ieee8021PryOutPfUserOctets_Object = MibTableColumn
ieee8021PryOutPfUserOctets = _Ieee8021PryOutPfUserOctets_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 6, 1, 2),
    _Ieee8021PryOutPfUserOctets_Type()
)
ieee8021PryOutPfUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryOutPfUserOctets.setStatus("current")
_Ieee8021PryOutPfPadOctets_Type = Counter64
_Ieee8021PryOutPfPadOctets_Object = MibTableColumn
ieee8021PryOutPfPadOctets = _Ieee8021PryOutPfPadOctets_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 6, 1, 3),
    _Ieee8021PryOutPfPadOctets_Type()
)
ieee8021PryOutPfPadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryOutPfPadOctets.setStatus("current")
_Ieee8021PryOutUnprtFrames_Type = Counter64
_Ieee8021PryOutUnprtFrames_Object = MibTableColumn
ieee8021PryOutUnprtFrames = _Ieee8021PryOutUnprtFrames_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 6, 1, 4),
    _Ieee8021PryOutUnprtFrames_Type()
)
ieee8021PryOutUnprtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryOutUnprtFrames.setStatus("current")
_Ieee8021PryOutUnprtOctets_Type = Counter64
_Ieee8021PryOutUnprtOctets_Object = MibTableColumn
ieee8021PryOutUnprtOctets = _Ieee8021PryOutUnprtOctets_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 6, 1, 5),
    _Ieee8021PryOutUnprtOctets_Type()
)
ieee8021PryOutUnprtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryOutUnprtOctets.setStatus("current")
_Ieee8021PryChannelOutTable_Object = MibTable
ieee8021PryChannelOutTable = _Ieee8021PryChannelOutTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 7)
)
if mibBuilder.loadTexts:
    ieee8021PryChannelOutTable.setStatus("current")
_Ieee8021PryChannelOutEntry_Object = MibTableRow
ieee8021PryChannelOutEntry = _Ieee8021PryChannelOutEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 7, 1)
)
if mibBuilder.loadTexts:
    ieee8021PryChannelOutEntry.setStatus("current")
_Ieee8021PryChOutUserFrames_Type = Counter64
_Ieee8021PryChOutUserFrames_Object = MibTableColumn
ieee8021PryChOutUserFrames = _Ieee8021PryChOutUserFrames_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 7, 1, 1),
    _Ieee8021PryChOutUserFrames_Type()
)
ieee8021PryChOutUserFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryChOutUserFrames.setStatus("current")
_Ieee8021PryChOutUserOctets_Type = Counter64
_Ieee8021PryChOutUserOctets_Object = MibTableColumn
ieee8021PryChOutUserOctets = _Ieee8021PryChOutUserOctets_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 7, 1, 2),
    _Ieee8021PryChOutUserOctets_Type()
)
ieee8021PryChOutUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryChOutUserOctets.setStatus("current")
_Ieee8021PryChOutPadOctets_Type = Counter64
_Ieee8021PryChOutPadOctets_Object = MibTableColumn
ieee8021PryChOutPadOctets = _Ieee8021PryChOutPadOctets_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 7, 1, 3),
    _Ieee8021PryChOutPadOctets_Type()
)
ieee8021PryChOutPadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryChOutPadOctets.setStatus("current")
_Ieee8021PryChOutMppdus_Type = Counter64
_Ieee8021PryChOutMppdus_Object = MibTableColumn
ieee8021PryChOutMppdus = _Ieee8021PryChOutMppdus_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 7, 1, 4),
    _Ieee8021PryChOutMppdus_Type()
)
ieee8021PryChOutMppdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryChOutMppdus.setStatus("current")
_Ieee8021PryChOutEncapFrames_Type = Counter64
_Ieee8021PryChOutEncapFrames_Object = MibTableColumn
ieee8021PryChOutEncapFrames = _Ieee8021PryChOutEncapFrames_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 7, 1, 5),
    _Ieee8021PryChOutEncapFrames_Type()
)
ieee8021PryChOutEncapFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryChOutEncapFrames.setStatus("current")
_Ieee8021PryChOutExpFragments_Type = Counter64
_Ieee8021PryChOutExpFragments_Object = MibTableColumn
ieee8021PryChOutExpFragments = _Ieee8021PryChOutExpFragments_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 7, 1, 6),
    _Ieee8021PryChOutExpFragments_Type()
)
ieee8021PryChOutExpFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryChOutExpFragments.setStatus("current")
_Ieee8021PryChOutPreFragments_Type = Counter64
_Ieee8021PryChOutPreFragments_Object = MibTableColumn
ieee8021PryChOutPreFragments = _Ieee8021PryChOutPreFragments_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 7, 1, 7),
    _Ieee8021PryChOutPreFragments_Type()
)
ieee8021PryChOutPreFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryChOutPreFragments.setStatus("current")
_Ieee8021PryInTable_Object = MibTable
ieee8021PryInTable = _Ieee8021PryInTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 8)
)
if mibBuilder.loadTexts:
    ieee8021PryInTable.setStatus("current")
_Ieee8021PryInEntry_Object = MibTableRow
ieee8021PryInEntry = _Ieee8021PryInEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 8, 1)
)
if mibBuilder.loadTexts:
    ieee8021PryInEntry.setStatus("current")
_Ieee8021PryInUserFrames_Type = Counter64
_Ieee8021PryInUserFrames_Object = MibTableColumn
ieee8021PryInUserFrames = _Ieee8021PryInUserFrames_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 8, 1, 1),
    _Ieee8021PryInUserFrames_Type()
)
ieee8021PryInUserFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryInUserFrames.setStatus("current")
_Ieee8021PryInUserOctets_Type = Counter64
_Ieee8021PryInUserOctets_Object = MibTableColumn
ieee8021PryInUserOctets = _Ieee8021PryInUserOctets_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 8, 1, 2),
    _Ieee8021PryInUserOctets_Type()
)
ieee8021PryInUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryInUserOctets.setStatus("current")
_Ieee8021PryInPadOctets_Type = Counter64
_Ieee8021PryInPadOctets_Object = MibTableColumn
ieee8021PryInPadOctets = _Ieee8021PryInPadOctets_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 8, 1, 3),
    _Ieee8021PryInPadOctets_Type()
)
ieee8021PryInPadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryInPadOctets.setStatus("current")
_Ieee8021PryInMppdus_Type = Counter64
_Ieee8021PryInMppdus_Object = MibTableColumn
ieee8021PryInMppdus = _Ieee8021PryInMppdus_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 8, 1, 4),
    _Ieee8021PryInMppdus_Type()
)
ieee8021PryInMppdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryInMppdus.setStatus("current")
_Ieee8021PryInEncapFrames_Type = Counter64
_Ieee8021PryInEncapFrames_Object = MibTableColumn
ieee8021PryInEncapFrames = _Ieee8021PryInEncapFrames_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 8, 1, 5),
    _Ieee8021PryInEncapFrames_Type()
)
ieee8021PryInEncapFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryInEncapFrames.setStatus("current")
_Ieee8021PryInExpFragments_Type = Counter64
_Ieee8021PryInExpFragments_Object = MibTableColumn
ieee8021PryInExpFragments = _Ieee8021PryInExpFragments_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 8, 1, 6),
    _Ieee8021PryInExpFragments_Type()
)
ieee8021PryInExpFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryInExpFragments.setStatus("current")
_Ieee8021PryInPreFragments_Type = Counter64
_Ieee8021PryInPreFragments_Object = MibTableColumn
ieee8021PryInPreFragments = _Ieee8021PryInPreFragments_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 8, 1, 7),
    _Ieee8021PryInPreFragments_Type()
)
ieee8021PryInPreFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryInPreFragments.setStatus("current")
_Ieee8021PryInExpDiscards_Type = Counter64
_Ieee8021PryInExpDiscards_Object = MibTableColumn
ieee8021PryInExpDiscards = _Ieee8021PryInExpDiscards_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 8, 1, 8),
    _Ieee8021PryInExpDiscards_Type()
)
ieee8021PryInExpDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryInExpDiscards.setStatus("current")
_Ieee8021PryInPreDiscards_Type = Counter64
_Ieee8021PryInPreDiscards_Object = MibTableColumn
ieee8021PryInPreDiscards = _Ieee8021PryInPreDiscards_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 8, 1, 9),
    _Ieee8021PryInPreDiscards_Type()
)
ieee8021PryInPreDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryInPreDiscards.setStatus("current")
_Ieee8021PryInUnknownMppcis_Type = Counter64
_Ieee8021PryInUnknownMppcis_Object = MibTableColumn
ieee8021PryInUnknownMppcis = _Ieee8021PryInUnknownMppcis_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 8, 1, 10),
    _Ieee8021PryInUnknownMppcis_Type()
)
ieee8021PryInUnknownMppcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryInUnknownMppcis.setStatus("current")
_Ieee8021PryInErroredMppdus_Type = Counter64
_Ieee8021PryInErroredMppdus_Object = MibTableColumn
ieee8021PryInErroredMppdus = _Ieee8021PryInErroredMppdus_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 8, 1, 11),
    _Ieee8021PryInErroredMppdus_Type()
)
ieee8021PryInErroredMppdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryInErroredMppdus.setStatus("current")
_Ieee8021PryInUnprtFrames_Type = Counter64
_Ieee8021PryInUnprtFrames_Object = MibTableColumn
ieee8021PryInUnprtFrames = _Ieee8021PryInUnprtFrames_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 8, 1, 12),
    _Ieee8021PryInUnprtFrames_Type()
)
ieee8021PryInUnprtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryInUnprtFrames.setStatus("current")
_Ieee8021PryInUnprtOctets_Type = Counter64
_Ieee8021PryInUnprtOctets_Object = MibTableColumn
ieee8021PryInUnprtOctets = _Ieee8021PryInUnprtOctets_Object(
    (1, 3, 111, 2, 802, 1, 1, 36, 2, 8, 1, 13),
    _Ieee8021PryInUnprtOctets_Type()
)
ieee8021PryInUnprtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PryInUnprtOctets.setStatus("current")
_Ieee8021PryMIBConformance_ObjectIdentity = ObjectIdentity
ieee8021PryMIBConformance = _Ieee8021PryMIBConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 36, 3)
)
_Ieee8021PryMIBCompliances_ObjectIdentity = ObjectIdentity
ieee8021PryMIBCompliances = _Ieee8021PryMIBCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 36, 3, 1)
)
_Ieee8021PryMIBGroups_ObjectIdentity = ObjectIdentity
ieee8021PryMIBGroups = _Ieee8021PryMIBGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 36, 3, 2)
)
ieee8021PrySelectionEntry.registerAugmentions(
    ("IEEE8021-PRY-MIB",
     "ieee8021PryFrameEntry")
)
ieee8021PryFrameEntry.setIndexNames(*ieee8021PrySelectionEntry.getIndexNames())
ieee8021PryIfEntry.registerAugmentions(
    ("IEEE8021-PRY-MIB",
     "ieee8021PryOutEntry")
)
ieee8021PryOutEntry.setIndexNames(*ieee8021PryIfEntry.getIndexNames())
ieee8021PryChannelEntry.registerAugmentions(
    ("IEEE8021-PRY-MIB",
     "ieee8021PryChannelOutEntry")
)
ieee8021PryChannelOutEntry.setIndexNames(*ieee8021PryChannelEntry.getIndexNames())
ieee8021PryIfEntry.registerAugmentions(
    ("IEEE8021-PRY-MIB",
     "ieee8021PryInEntry")
)
ieee8021PryInEntry.setIndexNames(*ieee8021PryIfEntry.getIndexNames())

# Managed Objects groups

ieee8021PryIfGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 36, 3, 2, 1)
)
ieee8021PryIfGroup.setObjects(
      *(("IEEE8021-PRY-MIB", "ieee8021PryIfRxProtection"),
        ("IEEE8021-PRY-MIB", "ieee8021PryIfTxProtection"),
        ("IEEE8021-PRY-MIB", "ieee8021PryIfSecySupport"),
        ("IEEE8021-PRY-MIB", "ieee8021PryIfAddr"),
        ("IEEE8021-PRY-MIB", "ieee8021PryIfMppduDA"),
        ("IEEE8021-PRY-MIB", "ieee8021PryIfDefaultReassembly"),
        ("IEEE8021-PRY-MIB", "ieee8021PryIfMaxPeers"),
        ("IEEE8021-PRY-MIB", "ieee8021PryIfNumPeers"),
        ("IEEE8021-PRY-MIB", "ieee8021PryIfNumPeers"))
)
if mibBuilder.loadTexts:
    ieee8021PryIfGroup.setStatus("current")

ieee8021PrySelectionGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 36, 3, 2, 2)
)
ieee8021PrySelectionGroup.setObjects(
    ("IEEE8021-PRY-MIB", "ieee8021PrySelectionPrivacyType")
)
if mibBuilder.loadTexts:
    ieee8021PrySelectionGroup.setStatus("current")

ieee8021PryFrameGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 36, 3, 2, 3)
)
ieee8021PryFrameGroup.setObjects(
      *(("IEEE8021-PRY-MIB", "ieee8021PryFrameAccessPriority"),
        ("IEEE8021-PRY-MIB", "ieee8021PryFrameRevealDE"),
        ("IEEE8021-PRY-MIB", "ieee8021PryFramePadding"))
)
if mibBuilder.loadTexts:
    ieee8021PryFrameGroup.setStatus("current")

ieee8021PryChannelGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 36, 3, 2, 4)
)
ieee8021PryChannelGroup.setObjects(
      *(("IEEE8021-PRY-MIB", "ieee8021PryChEnable"),
        ("IEEE8021-PRY-MIB", "ieee8021PryChFragmentEnable"),
        ("IEEE8021-PRY-MIB", "ieee8021PryChAccessPriority"),
        ("IEEE8021-PRY-MIB", "ieee8021PryChUserDataFrameSize"),
        ("IEEE8021-PRY-MIB", "ieee8021PryChMppduGeneration"),
        ("IEEE8021-PRY-MIB", "ieee8021PryChRequestedKbitRate"),
        ("IEEE8021-PRY-MIB", "ieee8021PryChMppduBitsOnWire"),
        ("IEEE8021-PRY-MIB", "ieee8021PryChMppduInterval"),
        ("IEEE8021-PRY-MIB", "ieee8021PryChUserBurstOctets"))
)
if mibBuilder.loadTexts:
    ieee8021PryChannelGroup.setStatus("current")

ieee8021PryPeerGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 36, 3, 2, 5)
)
ieee8021PryPeerGroup.setObjects(
    ("IEEE8021-PRY-MIB", "ieee8021PryPeerRowStatus")
)
if mibBuilder.loadTexts:
    ieee8021PryPeerGroup.setStatus("current")

ieee8021PryOutGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 36, 3, 2, 6)
)
ieee8021PryOutGroup.setObjects(
      *(("IEEE8021-PRY-MIB", "ieee8021PryOutPrivacyFrames"),
        ("IEEE8021-PRY-MIB", "ieee8021PryOutPfUserOctets"),
        ("IEEE8021-PRY-MIB", "ieee8021PryOutPfPadOctets"),
        ("IEEE8021-PRY-MIB", "ieee8021PryOutUnprtFrames"),
        ("IEEE8021-PRY-MIB", "ieee8021PryOutUnprtOctets"))
)
if mibBuilder.loadTexts:
    ieee8021PryOutGroup.setStatus("current")

ieee8021PryChOutGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 36, 3, 2, 7)
)
ieee8021PryChOutGroup.setObjects(
      *(("IEEE8021-PRY-MIB", "ieee8021PryChOutUserFrames"),
        ("IEEE8021-PRY-MIB", "ieee8021PryChOutUserOctets"),
        ("IEEE8021-PRY-MIB", "ieee8021PryChOutPadOctets"),
        ("IEEE8021-PRY-MIB", "ieee8021PryChOutMppdus"),
        ("IEEE8021-PRY-MIB", "ieee8021PryChOutEncapFrames"),
        ("IEEE8021-PRY-MIB", "ieee8021PryChOutExpFragments"),
        ("IEEE8021-PRY-MIB", "ieee8021PryChOutPreFragments"))
)
if mibBuilder.loadTexts:
    ieee8021PryChOutGroup.setStatus("current")

ieee8021PryInGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 36, 3, 2, 8)
)
ieee8021PryInGroup.setObjects(
      *(("IEEE8021-PRY-MIB", "ieee8021PryInUserFrames"),
        ("IEEE8021-PRY-MIB", "ieee8021PryInUserOctets"),
        ("IEEE8021-PRY-MIB", "ieee8021PryInPadOctets"),
        ("IEEE8021-PRY-MIB", "ieee8021PryInMppdus"),
        ("IEEE8021-PRY-MIB", "ieee8021PryInEncapFrames"),
        ("IEEE8021-PRY-MIB", "ieee8021PryInExpFragments"),
        ("IEEE8021-PRY-MIB", "ieee8021PryInPreFragments"),
        ("IEEE8021-PRY-MIB", "ieee8021PryInExpDiscards"),
        ("IEEE8021-PRY-MIB", "ieee8021PryInPreDiscards"),
        ("IEEE8021-PRY-MIB", "ieee8021PryInUnknownMppcis"),
        ("IEEE8021-PRY-MIB", "ieee8021PryInErroredMppdus"),
        ("IEEE8021-PRY-MIB", "ieee8021PryInUnprtFrames"),
        ("IEEE8021-PRY-MIB", "ieee8021PryInUnprtOctets"))
)
if mibBuilder.loadTexts:
    ieee8021PryInGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021PryMIBCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 36, 3, 1, 1)
)
ieee8021PryMIBCompliance.setObjects(
      *(("IEEE8021-PRY-MIB", "ieee8021PryIfGroup"),
        ("IEEE8021-PRY-MIB", "ieee8021PrySelectionGroup"),
        ("IEEE8021-PRY-MIB", "ieee8021PryFrameGroup"),
        ("IEEE8021-PRY-MIB", "ieee8021PryChannelGroup"),
        ("IEEE8021-PRY-MIB", "ieee8021PryPeerGroup"),
        ("IEEE8021-PRY-MIB", "ieee8021PryOutGroup"),
        ("IEEE8021-PRY-MIB", "ieee8021PryChOutGroup"),
        ("IEEE8021-PRY-MIB", "ieee8021PryInGroup"))
)
if mibBuilder.loadTexts:
    ieee8021PryMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-PRY-MIB",
    **{"ieee8021PryMIB": ieee8021PryMIB,
       "ieee8021PryMIBNotifications": ieee8021PryMIBNotifications,
       "ieee8021PryMIBObjects": ieee8021PryMIBObjects,
       "ieee8021PryIfTable": ieee8021PryIfTable,
       "ieee8021PryIfEntry": ieee8021PryIfEntry,
       "ieee8021PryIfIndex": ieee8021PryIfIndex,
       "ieee8021PryIfRxProtection": ieee8021PryIfRxProtection,
       "ieee8021PryIfTxProtection": ieee8021PryIfTxProtection,
       "ieee8021PryIfSecySupport": ieee8021PryIfSecySupport,
       "ieee8021PryIfAddr": ieee8021PryIfAddr,
       "ieee8021PryIfMppduDA": ieee8021PryIfMppduDA,
       "ieee8021PryIfDefaultReassembly": ieee8021PryIfDefaultReassembly,
       "ieee8021PryIfMaxPeers": ieee8021PryIfMaxPeers,
       "ieee8021PryIfNumPeers": ieee8021PryIfNumPeers,
       "ieee8021PrySelectionTable": ieee8021PrySelectionTable,
       "ieee8021PrySelectionEntry": ieee8021PrySelectionEntry,
       "ieee8021PrySelectionPriority": ieee8021PrySelectionPriority,
       "ieee8021PrySelectionPrivacyType": ieee8021PrySelectionPrivacyType,
       "ieee8021PryFrameTable": ieee8021PryFrameTable,
       "ieee8021PryFrameEntry": ieee8021PryFrameEntry,
       "ieee8021PryFrameAccessPriority": ieee8021PryFrameAccessPriority,
       "ieee8021PryFrameRevealDE": ieee8021PryFrameRevealDE,
       "ieee8021PryFramePadding": ieee8021PryFramePadding,
       "ieee8021PryChannelTable": ieee8021PryChannelTable,
       "ieee8021PryChannelEntry": ieee8021PryChannelEntry,
       "ieee8021PryChType": ieee8021PryChType,
       "ieee8021PryChEnable": ieee8021PryChEnable,
       "ieee8021PryChFragmentEnable": ieee8021PryChFragmentEnable,
       "ieee8021PryChAccessPriority": ieee8021PryChAccessPriority,
       "ieee8021PryChUserDataFrameSize": ieee8021PryChUserDataFrameSize,
       "ieee8021PryChMppduGeneration": ieee8021PryChMppduGeneration,
       "ieee8021PryChRequestedKbitRate": ieee8021PryChRequestedKbitRate,
       "ieee8021PryChMppduBitsOnWire": ieee8021PryChMppduBitsOnWire,
       "ieee8021PryChMppduInterval": ieee8021PryChMppduInterval,
       "ieee8021PryChUserBurstOctets": ieee8021PryChUserBurstOctets,
       "ieee8021PryPeerTable": ieee8021PryPeerTable,
       "ieee8021PryPeerEntry": ieee8021PryPeerEntry,
       "ieee8021PryPeerAddr": ieee8021PryPeerAddr,
       "ieee8021PryPeerRowStatus": ieee8021PryPeerRowStatus,
       "ieee8021PryOutTable": ieee8021PryOutTable,
       "ieee8021PryOutEntry": ieee8021PryOutEntry,
       "ieee8021PryOutPrivacyFrames": ieee8021PryOutPrivacyFrames,
       "ieee8021PryOutPfUserOctets": ieee8021PryOutPfUserOctets,
       "ieee8021PryOutPfPadOctets": ieee8021PryOutPfPadOctets,
       "ieee8021PryOutUnprtFrames": ieee8021PryOutUnprtFrames,
       "ieee8021PryOutUnprtOctets": ieee8021PryOutUnprtOctets,
       "ieee8021PryChannelOutTable": ieee8021PryChannelOutTable,
       "ieee8021PryChannelOutEntry": ieee8021PryChannelOutEntry,
       "ieee8021PryChOutUserFrames": ieee8021PryChOutUserFrames,
       "ieee8021PryChOutUserOctets": ieee8021PryChOutUserOctets,
       "ieee8021PryChOutPadOctets": ieee8021PryChOutPadOctets,
       "ieee8021PryChOutMppdus": ieee8021PryChOutMppdus,
       "ieee8021PryChOutEncapFrames": ieee8021PryChOutEncapFrames,
       "ieee8021PryChOutExpFragments": ieee8021PryChOutExpFragments,
       "ieee8021PryChOutPreFragments": ieee8021PryChOutPreFragments,
       "ieee8021PryInTable": ieee8021PryInTable,
       "ieee8021PryInEntry": ieee8021PryInEntry,
       "ieee8021PryInUserFrames": ieee8021PryInUserFrames,
       "ieee8021PryInUserOctets": ieee8021PryInUserOctets,
       "ieee8021PryInPadOctets": ieee8021PryInPadOctets,
       "ieee8021PryInMppdus": ieee8021PryInMppdus,
       "ieee8021PryInEncapFrames": ieee8021PryInEncapFrames,
       "ieee8021PryInExpFragments": ieee8021PryInExpFragments,
       "ieee8021PryInPreFragments": ieee8021PryInPreFragments,
       "ieee8021PryInExpDiscards": ieee8021PryInExpDiscards,
       "ieee8021PryInPreDiscards": ieee8021PryInPreDiscards,
       "ieee8021PryInUnknownMppcis": ieee8021PryInUnknownMppcis,
       "ieee8021PryInErroredMppdus": ieee8021PryInErroredMppdus,
       "ieee8021PryInUnprtFrames": ieee8021PryInUnprtFrames,
       "ieee8021PryInUnprtOctets": ieee8021PryInUnprtOctets,
       "ieee8021PryMIBConformance": ieee8021PryMIBConformance,
       "ieee8021PryMIBCompliances": ieee8021PryMIBCompliances,
       "ieee8021PryMIBCompliance": ieee8021PryMIBCompliance,
       "ieee8021PryMIBGroups": ieee8021PryMIBGroups,
       "ieee8021PryIfGroup": ieee8021PryIfGroup,
       "ieee8021PrySelectionGroup": ieee8021PrySelectionGroup,
       "ieee8021PryFrameGroup": ieee8021PryFrameGroup,
       "ieee8021PryChannelGroup": ieee8021PryChannelGroup,
       "ieee8021PryPeerGroup": ieee8021PryPeerGroup,
       "ieee8021PryOutGroup": ieee8021PryOutGroup,
       "ieee8021PryChOutGroup": ieee8021PryChOutGroup,
       "ieee8021PryInGroup": ieee8021PryInGroup}
)
