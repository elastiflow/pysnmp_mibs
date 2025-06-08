# SNMP MIB module (LRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/LRP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:14:46 2025
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(ieee802dot1mibs,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "ieee802dot1mibs")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetPortNumber")

(LldpV2ChassisId,
 LldpV2ChassisIdSubtype,
 LldpV2ManAddress,
 LldpV2PortId,
 LldpV2PortIdSubtype) = mibBuilder.importSymbols(
    "LLDP-V2-TC-MIB",
    "LldpV2ChassisId",
    "LldpV2ChassisIdSubtype",
    "LldpV2ManAddress",
    "LldpV2PortId",
    "LldpV2PortIdSubtype")

(LrpAppId,) = mibBuilder.importSymbols(
    "LRP-TC-MIB",
    "LrpAppId")

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

ieee8021LrpMIB = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 39)
)
if mibBuilder.loadTexts:
    ieee8021LrpMIB.setRevisions(
        ("2024-02-15 00:00",
         "2020-12-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LrpObjects_ObjectIdentity = ObjectIdentity
lrpObjects = _LrpObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 39, 1)
)
_LrpConfiguration_ObjectIdentity = ObjectIdentity
lrpConfiguration = _LrpConfiguration_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1)
)
_LrpDtInstanceTable_Object = MibTable
lrpDtInstanceTable = _LrpDtInstanceTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lrpDtInstanceTable.setStatus("current")
_LrpDtInstanceEntry_Object = MibTableRow
lrpDtInstanceEntry = _LrpDtInstanceEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 1, 1)
)
lrpDtInstanceEntry.setIndexNames(
    (0, "LRP-MIB", "lrpDtInstNumber"),
)
if mibBuilder.loadTexts:
    lrpDtInstanceEntry.setStatus("current")


class _LrpDtInstNumber_Type(Unsigned32):
    """Custom type lrpDtInstNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LrpDtInstNumber_Type.__name__ = "Unsigned32"
_LrpDtInstNumber_Object = MibTableColumn
lrpDtInstNumber = _LrpDtInstNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 1, 1, 1),
    _LrpDtInstNumber_Type()
)
lrpDtInstNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lrpDtInstNumber.setStatus("current")
_LrpDtInstActiveTcp_Type = TruthValue
_LrpDtInstActiveTcp_Object = MibTableColumn
lrpDtInstActiveTcp = _LrpDtInstActiveTcp_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 1, 1, 2),
    _LrpDtInstActiveTcp_Type()
)
lrpDtInstActiveTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpDtInstActiveTcp.setStatus("current")
_LrpDtInstAddressTypes_Type = AddressFamilyNumbers
_LrpDtInstAddressTypes_Object = MibTableColumn
lrpDtInstAddressTypes = _LrpDtInstAddressTypes_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 1, 1, 3),
    _LrpDtInstAddressTypes_Type()
)
lrpDtInstAddressTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpDtInstAddressTypes.setStatus("current")
_LrpDtInstMyAddress_Type = LldpV2ManAddress
_LrpDtInstMyAddress_Object = MibTableColumn
lrpDtInstMyAddress = _LrpDtInstMyAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 1, 1, 4),
    _LrpDtInstMyAddress_Type()
)
lrpDtInstMyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpDtInstMyAddress.setStatus("current")
_LrpDtInstMyTcpPort_Type = InetPortNumber
_LrpDtInstMyTcpPort_Object = MibTableColumn
lrpDtInstMyTcpPort = _LrpDtInstMyTcpPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 1, 1, 5),
    _LrpDtInstMyTcpPort_Type()
)
lrpDtInstMyTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpDtInstMyTcpPort.setStatus("current")
_LrpDtInstNeighborAddress_Type = LldpV2ManAddress
_LrpDtInstNeighborAddress_Object = MibTableColumn
lrpDtInstNeighborAddress = _LrpDtInstNeighborAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 1, 1, 6),
    _LrpDtInstNeighborAddress_Type()
)
lrpDtInstNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpDtInstNeighborAddress.setStatus("current")
_LrpDtInstNeighborTcpPort_Type = InetPortNumber
_LrpDtInstNeighborTcpPort_Object = MibTableColumn
lrpDtInstNeighborTcpPort = _LrpDtInstNeighborTcpPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 1, 1, 7),
    _LrpDtInstNeighborTcpPort_Type()
)
lrpDtInstNeighborTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpDtInstNeighborTcpPort.setStatus("current")
_LrpPortalTable_Object = MibTable
lrpPortalTable = _LrpPortalTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lrpPortalTable.setStatus("current")
_LrpPortalEntry_Object = MibTableRow
lrpPortalEntry = _LrpPortalEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 2, 1)
)
lrpPortalEntry.setIndexNames(
    (0, "LRP-MIB", "lrpPortalNumber"),
)
if mibBuilder.loadTexts:
    lrpPortalEntry.setStatus("current")
_LrpPortalNumber_Type = Unsigned32
_LrpPortalNumber_Object = MibTableColumn
lrpPortalNumber = _LrpPortalNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 2, 1, 1),
    _LrpPortalNumber_Type()
)
lrpPortalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lrpPortalNumber.setStatus("current")
_LrpPortalIfIndex_Type = InterfaceIndex
_LrpPortalIfIndex_Object = MibTableColumn
lrpPortalIfIndex = _LrpPortalIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 2, 1, 2),
    _LrpPortalIfIndex_Type()
)
lrpPortalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPortalIfIndex.setStatus("current")
_LrpPortalDtInstanceIndex_Type = Unsigned32
_LrpPortalDtInstanceIndex_Object = MibTableColumn
lrpPortalDtInstanceIndex = _LrpPortalDtInstanceIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 2, 1, 3),
    _LrpPortalDtInstanceIndex_Type()
)
lrpPortalDtInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPortalDtInstanceIndex.setStatus("current")
_LrpPortalAppId_Type = LrpAppId
_LrpPortalAppId_Object = MibTableColumn
lrpPortalAppId = _LrpPortalAppId_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 2, 1, 4),
    _LrpPortalAppId_Type()
)
lrpPortalAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPortalAppId.setStatus("current")
_LrpPortalMyChassisIdType_Type = LldpV2ChassisIdSubtype
_LrpPortalMyChassisIdType_Object = MibTableColumn
lrpPortalMyChassisIdType = _LrpPortalMyChassisIdType_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 2, 1, 5),
    _LrpPortalMyChassisIdType_Type()
)
lrpPortalMyChassisIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPortalMyChassisIdType.setStatus("current")
_LrpPortalMyChassisId_Type = LldpV2ChassisId
_LrpPortalMyChassisId_Object = MibTableColumn
lrpPortalMyChassisId = _LrpPortalMyChassisId_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 2, 1, 6),
    _LrpPortalMyChassisId_Type()
)
lrpPortalMyChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPortalMyChassisId.setStatus("current")
_LrpPortalMyPortIdType_Type = LldpV2PortIdSubtype
_LrpPortalMyPortIdType_Object = MibTableColumn
lrpPortalMyPortIdType = _LrpPortalMyPortIdType_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 2, 1, 7),
    _LrpPortalMyPortIdType_Type()
)
lrpPortalMyPortIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPortalMyPortIdType.setStatus("current")
_LrpPortalMyPortId_Type = LldpV2PortId
_LrpPortalMyPortId_Object = MibTableColumn
lrpPortalMyPortId = _LrpPortalMyPortId_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 2, 1, 8),
    _LrpPortalMyPortId_Type()
)
lrpPortalMyPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPortalMyPortId.setStatus("current")
_LrpPortalNbrChassisIdType_Type = LldpV2ChassisIdSubtype
_LrpPortalNbrChassisIdType_Object = MibTableColumn
lrpPortalNbrChassisIdType = _LrpPortalNbrChassisIdType_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 2, 1, 9),
    _LrpPortalNbrChassisIdType_Type()
)
lrpPortalNbrChassisIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPortalNbrChassisIdType.setStatus("current")
_LrpPortalNbrChassisId_Type = LldpV2ChassisId
_LrpPortalNbrChassisId_Object = MibTableColumn
lrpPortalNbrChassisId = _LrpPortalNbrChassisId_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 2, 1, 10),
    _LrpPortalNbrChassisId_Type()
)
lrpPortalNbrChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPortalNbrChassisId.setStatus("current")
_LrpPortalNbrPortIdType_Type = LldpV2PortIdSubtype
_LrpPortalNbrPortIdType_Object = MibTableColumn
lrpPortalNbrPortIdType = _LrpPortalNbrPortIdType_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 2, 1, 11),
    _LrpPortalNbrPortIdType_Type()
)
lrpPortalNbrPortIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPortalNbrPortIdType.setStatus("current")
_LrpPortalNbrPortId_Type = LldpV2PortId
_LrpPortalNbrPortId_Object = MibTableColumn
lrpPortalNbrPortId = _LrpPortalNbrPortId_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 2, 1, 12),
    _LrpPortalNbrPortId_Type()
)
lrpPortalNbrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPortalNbrPortId.setStatus("current")
_LrpPortalLocalOverflow_Type = TruthValue
_LrpPortalLocalOverflow_Object = MibTableColumn
lrpPortalLocalOverflow = _LrpPortalLocalOverflow_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 1, 2, 1, 13),
    _LrpPortalLocalOverflow_Type()
)
lrpPortalLocalOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPortalLocalOverflow.setStatus("current")
_LrpStatistics_ObjectIdentity = ObjectIdentity
lrpStatistics = _LrpStatistics_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2)
)
_LrpPortalCountersTable_Object = MibTable
lrpPortalCountersTable = _LrpPortalCountersTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lrpPortalCountersTable.setStatus("current")
_LrpPortalCountersEntry_Object = MibTableRow
lrpPortalCountersEntry = _LrpPortalCountersEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 1, 1)
)
lrpPortalCountersEntry.setIndexNames(
    (0, "LRP-MIB", "lrpPortalNumber"),
)
if mibBuilder.loadTexts:
    lrpPortalCountersEntry.setStatus("current")
_LrpPortalApplicantActiveRecords_Type = Unsigned32
_LrpPortalApplicantActiveRecords_Object = MibTableColumn
lrpPortalApplicantActiveRecords = _LrpPortalApplicantActiveRecords_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 1, 1, 1),
    _LrpPortalApplicantActiveRecords_Type()
)
lrpPortalApplicantActiveRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPortalApplicantActiveRecords.setStatus("current")
_LrpPptCtRegistrarActiveRecords_Type = Unsigned32
_LrpPptCtRegistrarActiveRecords_Object = MibTableColumn
lrpPptCtRegistrarActiveRecords = _LrpPptCtRegistrarActiveRecords_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 1, 1, 2),
    _LrpPptCtRegistrarActiveRecords_Type()
)
lrpPptCtRegistrarActiveRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPptCtRegistrarActiveRecords.setStatus("current")
_LrpPptCtSentHellos_Type = Counter64
_LrpPptCtSentHellos_Object = MibTableColumn
lrpPptCtSentHellos = _LrpPptCtSentHellos_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 1, 1, 3),
    _LrpPptCtSentHellos_Type()
)
lrpPptCtSentHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPptCtSentHellos.setStatus("current")
_LrpPptCtAcceptedHellos_Type = Counter64
_LrpPptCtAcceptedHellos_Object = MibTableColumn
lrpPptCtAcceptedHellos = _LrpPptCtAcceptedHellos_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 1, 1, 4),
    _LrpPptCtAcceptedHellos_Type()
)
lrpPptCtAcceptedHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPptCtAcceptedHellos.setStatus("current")
_LrpPptCtDiscardedHellos_Type = Counter64
_LrpPptCtDiscardedHellos_Object = MibTableColumn
lrpPptCtDiscardedHellos = _LrpPptCtDiscardedHellos_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 1, 1, 5),
    _LrpPptCtDiscardedHellos_Type()
)
lrpPptCtDiscardedHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPptCtDiscardedHellos.setStatus("current")
_LrpPptCtSentRecords_Type = Counter64
_LrpPptCtSentRecords_Object = MibTableColumn
lrpPptCtSentRecords = _LrpPptCtSentRecords_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 1, 1, 6),
    _LrpPptCtSentRecords_Type()
)
lrpPptCtSentRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPptCtSentRecords.setStatus("current")
_LrpPptCtAcceptedRecords_Type = Counter64
_LrpPptCtAcceptedRecords_Object = MibTableColumn
lrpPptCtAcceptedRecords = _LrpPptCtAcceptedRecords_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 1, 1, 7),
    _LrpPptCtAcceptedRecords_Type()
)
lrpPptCtAcceptedRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPptCtAcceptedRecords.setStatus("current")
_LrpPptCtDiscardedRecords_Type = Counter64
_LrpPptCtDiscardedRecords_Object = MibTableColumn
lrpPptCtDiscardedRecords = _LrpPptCtDiscardedRecords_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 1, 1, 8),
    _LrpPptCtDiscardedRecords_Type()
)
lrpPptCtDiscardedRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPptCtDiscardedRecords.setStatus("current")
_LrpPptCtRecordErrors_Type = Counter64
_LrpPptCtRecordErrors_Object = MibTableColumn
lrpPptCtRecordErrors = _LrpPptCtRecordErrors_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 1, 1, 9),
    _LrpPptCtRecordErrors_Type()
)
lrpPptCtRecordErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPptCtRecordErrors.setStatus("current")
_LrpPptCtSentPartials_Type = Counter64
_LrpPptCtSentPartials_Object = MibTableColumn
lrpPptCtSentPartials = _LrpPptCtSentPartials_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 1, 1, 10),
    _LrpPptCtSentPartials_Type()
)
lrpPptCtSentPartials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPptCtSentPartials.setStatus("current")
_LrpPptCtAcceptedPartials_Type = Counter64
_LrpPptCtAcceptedPartials_Object = MibTableColumn
lrpPptCtAcceptedPartials = _LrpPptCtAcceptedPartials_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 1, 1, 11),
    _LrpPptCtAcceptedPartials_Type()
)
lrpPptCtAcceptedPartials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPptCtAcceptedPartials.setStatus("current")
_LrpPptCtDiscardedPartials_Type = Counter64
_LrpPptCtDiscardedPartials_Object = MibTableColumn
lrpPptCtDiscardedPartials = _LrpPptCtDiscardedPartials_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 1, 1, 12),
    _LrpPptCtDiscardedPartials_Type()
)
lrpPptCtDiscardedPartials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPptCtDiscardedPartials.setStatus("current")
_LrpPptCtSentCompletes_Type = Counter64
_LrpPptCtSentCompletes_Object = MibTableColumn
lrpPptCtSentCompletes = _LrpPptCtSentCompletes_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 1, 1, 13),
    _LrpPptCtSentCompletes_Type()
)
lrpPptCtSentCompletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPptCtSentCompletes.setStatus("current")
_LrpPptCtAcceptedCompletes_Type = Counter64
_LrpPptCtAcceptedCompletes_Object = MibTableColumn
lrpPptCtAcceptedCompletes = _LrpPptCtAcceptedCompletes_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 1, 1, 14),
    _LrpPptCtAcceptedCompletes_Type()
)
lrpPptCtAcceptedCompletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPptCtAcceptedCompletes.setStatus("current")
_LrpPptCtDiscardedCompletes_Type = Counter64
_LrpPptCtDiscardedCompletes_Object = MibTableColumn
lrpPptCtDiscardedCompletes = _LrpPptCtDiscardedCompletes_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 1, 1, 15),
    _LrpPptCtDiscardedCompletes_Type()
)
lrpPptCtDiscardedCompletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPptCtDiscardedCompletes.setStatus("current")
_LrpPptCtDiscardedUnknowns_Type = Counter64
_LrpPptCtDiscardedUnknowns_Object = MibTableColumn
lrpPptCtDiscardedUnknowns = _LrpPptCtDiscardedUnknowns_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 1, 1, 16),
    _LrpPptCtDiscardedUnknowns_Type()
)
lrpPptCtDiscardedUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpPptCtDiscardedUnknowns.setStatus("current")
_LrpDtInstanceCountersTable_Object = MibTable
lrpDtInstanceCountersTable = _LrpDtInstanceCountersTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 2)
)
if mibBuilder.loadTexts:
    lrpDtInstanceCountersTable.setStatus("current")
_LrpDtInstanceCountersEntry_Object = MibTableRow
lrpDtInstanceCountersEntry = _LrpDtInstanceCountersEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 2, 1)
)
lrpDtInstanceCountersEntry.setIndexNames(
    (0, "LRP-MIB", "lrpDtInstNumber"),
)
if mibBuilder.loadTexts:
    lrpDtInstanceCountersEntry.setStatus("current")
_LrpDtInstDiscardedLrpdus_Type = Counter64
_LrpDtInstDiscardedLrpdus_Object = MibTableColumn
lrpDtInstDiscardedLrpdus = _LrpDtInstDiscardedLrpdus_Object(
    (1, 3, 111, 2, 802, 1, 1, 39, 1, 2, 2, 1, 1),
    _LrpDtInstDiscardedLrpdus_Type()
)
lrpDtInstDiscardedLrpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrpDtInstDiscardedLrpdus.setStatus("current")
_LrpConformance_ObjectIdentity = ObjectIdentity
lrpConformance = _LrpConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 39, 2)
)
_LrpCompliances_ObjectIdentity = ObjectIdentity
lrpCompliances = _LrpCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 39, 2, 1)
)
_LrpGroups_ObjectIdentity = ObjectIdentity
lrpGroups = _LrpGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 39, 2, 2)
)

# Managed Objects groups

lrpDsDtGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 39, 2, 2, 1)
)
lrpDsDtGroup.setObjects(
      *(("LRP-MIB", "lrpDtInstActiveTcp"),
        ("LRP-MIB", "lrpDtInstAddressTypes"),
        ("LRP-MIB", "lrpDtInstMyAddress"),
        ("LRP-MIB", "lrpDtInstMyTcpPort"),
        ("LRP-MIB", "lrpDtInstNeighborAddress"),
        ("LRP-MIB", "lrpDtInstNeighborTcpPort"),
        ("LRP-MIB", "lrpPortalIfIndex"),
        ("LRP-MIB", "lrpPortalDtInstanceIndex"),
        ("LRP-MIB", "lrpPortalAppId"),
        ("LRP-MIB", "lrpPortalMyChassisIdType"),
        ("LRP-MIB", "lrpPortalMyChassisId"),
        ("LRP-MIB", "lrpPortalMyPortIdType"),
        ("LRP-MIB", "lrpPortalMyPortId"),
        ("LRP-MIB", "lrpPortalNbrChassisIdType"),
        ("LRP-MIB", "lrpPortalNbrChassisId"),
        ("LRP-MIB", "lrpPortalNbrPortIdType"),
        ("LRP-MIB", "lrpPortalNbrPortId"),
        ("LRP-MIB", "lrpPortalLocalOverflow"),
        ("LRP-MIB", "lrpPortalApplicantActiveRecords"),
        ("LRP-MIB", "lrpPptCtRegistrarActiveRecords"),
        ("LRP-MIB", "lrpPptCtSentHellos"),
        ("LRP-MIB", "lrpPptCtAcceptedHellos"),
        ("LRP-MIB", "lrpPptCtDiscardedHellos"),
        ("LRP-MIB", "lrpPptCtSentRecords"),
        ("LRP-MIB", "lrpPptCtAcceptedRecords"),
        ("LRP-MIB", "lrpPptCtDiscardedRecords"),
        ("LRP-MIB", "lrpPptCtRecordErrors"),
        ("LRP-MIB", "lrpPptCtSentPartials"),
        ("LRP-MIB", "lrpPptCtAcceptedPartials"),
        ("LRP-MIB", "lrpPptCtDiscardedPartials"),
        ("LRP-MIB", "lrpPptCtSentCompletes"),
        ("LRP-MIB", "lrpPptCtAcceptedCompletes"),
        ("LRP-MIB", "lrpPptCtDiscardedCompletes"),
        ("LRP-MIB", "lrpPptCtDiscardedUnknowns"),
        ("LRP-MIB", "lrpDtInstDiscardedLrpdus"))
)
if mibBuilder.loadTexts:
    lrpDsDtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lrpCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 39, 2, 1, 1)
)
lrpCompliance.setObjects(
    ("LRP-MIB", "lrpDsDtGroup")
)
if mibBuilder.loadTexts:
    lrpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LRP-MIB",
    **{"ieee8021LrpMIB": ieee8021LrpMIB,
       "lrpObjects": lrpObjects,
       "lrpConfiguration": lrpConfiguration,
       "lrpDtInstanceTable": lrpDtInstanceTable,
       "lrpDtInstanceEntry": lrpDtInstanceEntry,
       "lrpDtInstNumber": lrpDtInstNumber,
       "lrpDtInstActiveTcp": lrpDtInstActiveTcp,
       "lrpDtInstAddressTypes": lrpDtInstAddressTypes,
       "lrpDtInstMyAddress": lrpDtInstMyAddress,
       "lrpDtInstMyTcpPort": lrpDtInstMyTcpPort,
       "lrpDtInstNeighborAddress": lrpDtInstNeighborAddress,
       "lrpDtInstNeighborTcpPort": lrpDtInstNeighborTcpPort,
       "lrpPortalTable": lrpPortalTable,
       "lrpPortalEntry": lrpPortalEntry,
       "lrpPortalNumber": lrpPortalNumber,
       "lrpPortalIfIndex": lrpPortalIfIndex,
       "lrpPortalDtInstanceIndex": lrpPortalDtInstanceIndex,
       "lrpPortalAppId": lrpPortalAppId,
       "lrpPortalMyChassisIdType": lrpPortalMyChassisIdType,
       "lrpPortalMyChassisId": lrpPortalMyChassisId,
       "lrpPortalMyPortIdType": lrpPortalMyPortIdType,
       "lrpPortalMyPortId": lrpPortalMyPortId,
       "lrpPortalNbrChassisIdType": lrpPortalNbrChassisIdType,
       "lrpPortalNbrChassisId": lrpPortalNbrChassisId,
       "lrpPortalNbrPortIdType": lrpPortalNbrPortIdType,
       "lrpPortalNbrPortId": lrpPortalNbrPortId,
       "lrpPortalLocalOverflow": lrpPortalLocalOverflow,
       "lrpStatistics": lrpStatistics,
       "lrpPortalCountersTable": lrpPortalCountersTable,
       "lrpPortalCountersEntry": lrpPortalCountersEntry,
       "lrpPortalApplicantActiveRecords": lrpPortalApplicantActiveRecords,
       "lrpPptCtRegistrarActiveRecords": lrpPptCtRegistrarActiveRecords,
       "lrpPptCtSentHellos": lrpPptCtSentHellos,
       "lrpPptCtAcceptedHellos": lrpPptCtAcceptedHellos,
       "lrpPptCtDiscardedHellos": lrpPptCtDiscardedHellos,
       "lrpPptCtSentRecords": lrpPptCtSentRecords,
       "lrpPptCtAcceptedRecords": lrpPptCtAcceptedRecords,
       "lrpPptCtDiscardedRecords": lrpPptCtDiscardedRecords,
       "lrpPptCtRecordErrors": lrpPptCtRecordErrors,
       "lrpPptCtSentPartials": lrpPptCtSentPartials,
       "lrpPptCtAcceptedPartials": lrpPptCtAcceptedPartials,
       "lrpPptCtDiscardedPartials": lrpPptCtDiscardedPartials,
       "lrpPptCtSentCompletes": lrpPptCtSentCompletes,
       "lrpPptCtAcceptedCompletes": lrpPptCtAcceptedCompletes,
       "lrpPptCtDiscardedCompletes": lrpPptCtDiscardedCompletes,
       "lrpPptCtDiscardedUnknowns": lrpPptCtDiscardedUnknowns,
       "lrpDtInstanceCountersTable": lrpDtInstanceCountersTable,
       "lrpDtInstanceCountersEntry": lrpDtInstanceCountersEntry,
       "lrpDtInstDiscardedLrpdus": lrpDtInstDiscardedLrpdus,
       "lrpConformance": lrpConformance,
       "lrpCompliances": lrpCompliances,
       "lrpCompliance": lrpCompliance,
       "lrpGroups": lrpGroups,
       "lrpDsDtGroup": lrpDsDtGroup}
)
