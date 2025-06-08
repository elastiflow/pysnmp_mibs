# SNMP MIB module (CTS-SGC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/computaris_35787/CTS-SGC-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:02:15 2025
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

(ctsRegMIB,) = mibBuilder.importSymbols(
    "COMPUTARIS-MIB",
    "ctsRegMIB")

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
 ExtUTCTime,
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
    "ExtUTCTime",
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

sgcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35787, 1)
)
if mibBuilder.loadTexts:
    sgcMIB.setRevisions(
        ("2013-09-25 07:25",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SgcDpcStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("active", 1),
          ("congested", 2),
          ("inactive", 3),
          ("restricted", 4))
    )



class SgcSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("info", 4),
          ("cleared", 5))
    )



class SgcSsnStatus(TextualConvention, Integer32):
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
        *(("allowed", 1),
          ("prohibited", 2),
          ("congested", 3))
    )



# MIB Managed Objects in the order of their OIDs

_SgcObjects_ObjectIdentity = ObjectIdentity
sgcObjects = _SgcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1)
)
_SgcAssociationTable_Object = MibTable
sgcAssociationTable = _SgcAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sgcAssociationTable.setStatus("current")
_SgcAssociationEntry_Object = MibTableRow
sgcAssociationEntry = _SgcAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 1, 1)
)
sgcAssociationEntry.setIndexNames(
    (0, "CTS-SGC-MIB", "sgcAssociationEntryIdx"),
)
if mibBuilder.loadTexts:
    sgcAssociationEntry.setStatus("current")
_SgcAssociationEntryIdx_Type = Counter32
_SgcAssociationEntryIdx_Object = MibTableColumn
sgcAssociationEntryIdx = _SgcAssociationEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 1, 1, 1),
    _SgcAssociationEntryIdx_Type()
)
sgcAssociationEntryIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAssociationEntryIdx.setStatus("current")
_SgcAssociationEntryConnectionName_Type = OctetString
_SgcAssociationEntryConnectionName_Object = MibTableColumn
sgcAssociationEntryConnectionName = _SgcAssociationEntryConnectionName_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 1, 1, 2),
    _SgcAssociationEntryConnectionName_Type()
)
sgcAssociationEntryConnectionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAssociationEntryConnectionName.setStatus("current")
_SgcAssociationEntryNodeName_Type = OctetString
_SgcAssociationEntryNodeName_Object = MibTableColumn
sgcAssociationEntryNodeName = _SgcAssociationEntryNodeName_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 1, 1, 3),
    _SgcAssociationEntryNodeName_Type()
)
sgcAssociationEntryNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAssociationEntryNodeName.setStatus("current")


class _SgcAssociationEntryStatus_Type(Integer32):
    """Custom type sgcAssociationEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("established", 1),
          ("inactive", 2))
    )


_SgcAssociationEntryStatus_Type.__name__ = "Integer32"
_SgcAssociationEntryStatus_Object = MibTableColumn
sgcAssociationEntryStatus = _SgcAssociationEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 1, 1, 4),
    _SgcAssociationEntryStatus_Type()
)
sgcAssociationEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAssociationEntryStatus.setStatus("current")
_SgcAssociationEntryRXSctpCount_Type = Counter32
_SgcAssociationEntryRXSctpCount_Object = MibTableColumn
sgcAssociationEntryRXSctpCount = _SgcAssociationEntryRXSctpCount_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 1, 1, 5),
    _SgcAssociationEntryRXSctpCount_Type()
)
sgcAssociationEntryRXSctpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAssociationEntryRXSctpCount.setStatus("current")
_SgcAssociationEntryTXSctpCount_Type = Counter32
_SgcAssociationEntryTXSctpCount_Object = MibTableColumn
sgcAssociationEntryTXSctpCount = _SgcAssociationEntryTXSctpCount_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 1, 1, 6),
    _SgcAssociationEntryTXSctpCount_Type()
)
sgcAssociationEntryTXSctpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAssociationEntryTXSctpCount.setStatus("current")
_SgcAssociationEntryRXDataCount_Type = Counter32
_SgcAssociationEntryRXDataCount_Object = MibTableColumn
sgcAssociationEntryRXDataCount = _SgcAssociationEntryRXDataCount_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 1, 1, 7),
    _SgcAssociationEntryRXDataCount_Type()
)
sgcAssociationEntryRXDataCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAssociationEntryRXDataCount.setStatus("current")
_SgcAssociationEntryTXDataCount_Type = Counter32
_SgcAssociationEntryTXDataCount_Object = MibTableColumn
sgcAssociationEntryTXDataCount = _SgcAssociationEntryTXDataCount_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 1, 1, 8),
    _SgcAssociationEntryTXDataCount_Type()
)
sgcAssociationEntryTXDataCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAssociationEntryTXDataCount.setStatus("current")
_SgcAssociationEntryRXErrorCount_Type = Counter32
_SgcAssociationEntryRXErrorCount_Object = MibTableColumn
sgcAssociationEntryRXErrorCount = _SgcAssociationEntryRXErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 1, 1, 9),
    _SgcAssociationEntryRXErrorCount_Type()
)
sgcAssociationEntryRXErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAssociationEntryRXErrorCount.setStatus("current")
_SgcAssociationEntryTXErrorCount_Type = Counter32
_SgcAssociationEntryTXErrorCount_Object = MibTableColumn
sgcAssociationEntryTXErrorCount = _SgcAssociationEntryTXErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 1, 1, 10),
    _SgcAssociationEntryTXErrorCount_Type()
)
sgcAssociationEntryTXErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAssociationEntryTXErrorCount.setStatus("current")
_SgcAssociationEntryPeerAddresses_Type = OctetString
_SgcAssociationEntryPeerAddresses_Object = MibTableColumn
sgcAssociationEntryPeerAddresses = _SgcAssociationEntryPeerAddresses_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 1, 1, 11),
    _SgcAssociationEntryPeerAddresses_Type()
)
sgcAssociationEntryPeerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAssociationEntryPeerAddresses.setStatus("current")
_SgcAssociationEntrySctpInStreams_Type = Integer32
_SgcAssociationEntrySctpInStreams_Object = MibTableColumn
sgcAssociationEntrySctpInStreams = _SgcAssociationEntrySctpInStreams_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 1, 1, 12),
    _SgcAssociationEntrySctpInStreams_Type()
)
sgcAssociationEntrySctpInStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAssociationEntrySctpInStreams.setStatus("current")
_SgcAssociationEntrySctpOutStreams_Type = Integer32
_SgcAssociationEntrySctpOutStreams_Object = MibTableColumn
sgcAssociationEntrySctpOutStreams = _SgcAssociationEntrySctpOutStreams_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 1, 1, 13),
    _SgcAssociationEntrySctpOutStreams_Type()
)
sgcAssociationEntrySctpOutStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAssociationEntrySctpOutStreams.setStatus("current")
_SgcAssociationEntrySctpOptions_Type = OctetString
_SgcAssociationEntrySctpOptions_Object = MibTableColumn
sgcAssociationEntrySctpOptions = _SgcAssociationEntrySctpOptions_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 1, 1, 14),
    _SgcAssociationEntrySctpOptions_Type()
)
sgcAssociationEntrySctpOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAssociationEntrySctpOptions.setStatus("current")
_SgcAsStateTable_Object = MibTable
sgcAsStateTable = _SgcAsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sgcAsStateTable.setStatus("current")
_SgcAsStateEntry_Object = MibTableRow
sgcAsStateEntry = _SgcAsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 2, 1)
)
sgcAsStateEntry.setIndexNames(
    (0, "CTS-SGC-MIB", "sgcAsStateEntryIdx"),
)
if mibBuilder.loadTexts:
    sgcAsStateEntry.setStatus("current")
_SgcAsStateEntryIdx_Type = Counter32
_SgcAsStateEntryIdx_Object = MibTableColumn
sgcAsStateEntryIdx = _SgcAsStateEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 2, 1, 1),
    _SgcAsStateEntryIdx_Type()
)
sgcAsStateEntryIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAsStateEntryIdx.setStatus("current")
_SgcAsStateEntryAsId_Type = OctetString
_SgcAsStateEntryAsId_Object = MibTableColumn
sgcAsStateEntryAsId = _SgcAsStateEntryAsId_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 2, 1, 2),
    _SgcAsStateEntryAsId_Type()
)
sgcAsStateEntryAsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAsStateEntryAsId.setStatus("current")
_SgcAsStateEntryConnectionId_Type = OctetString
_SgcAsStateEntryConnectionId_Object = MibTableColumn
sgcAsStateEntryConnectionId = _SgcAsStateEntryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 2, 1, 3),
    _SgcAsStateEntryConnectionId_Type()
)
sgcAsStateEntryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAsStateEntryConnectionId.setStatus("current")
_SgcAsStateEntryReceived_Type = Counter32
_SgcAsStateEntryReceived_Object = MibTableColumn
sgcAsStateEntryReceived = _SgcAsStateEntryReceived_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 2, 1, 4),
    _SgcAsStateEntryReceived_Type()
)
sgcAsStateEntryReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAsStateEntryReceived.setStatus("current")
_SgcAsStateEntrySent_Type = Counter32
_SgcAsStateEntrySent_Object = MibTableColumn
sgcAsStateEntrySent = _SgcAsStateEntrySent_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 2, 1, 5),
    _SgcAsStateEntrySent_Type()
)
sgcAsStateEntrySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAsStateEntrySent.setStatus("current")
_SgcAsStateEntryNodeId_Type = OctetString
_SgcAsStateEntryNodeId_Object = MibTableColumn
sgcAsStateEntryNodeId = _SgcAsStateEntryNodeId_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 2, 1, 6),
    _SgcAsStateEntryNodeId_Type()
)
sgcAsStateEntryNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAsStateEntryNodeId.setStatus("current")


class _SgcAsStateEntryStatus_Type(Integer32):
    """Custom type sgcAsStateEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_SgcAsStateEntryStatus_Type.__name__ = "Integer32"
_SgcAsStateEntryStatus_Object = MibTableColumn
sgcAsStateEntryStatus = _SgcAsStateEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 2, 1, 7),
    _SgcAsStateEntryStatus_Type()
)
sgcAsStateEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcAsStateEntryStatus.setStatus("current")
_SgcLocalSsnTable_Object = MibTable
sgcLocalSsnTable = _SgcLocalSsnTable_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sgcLocalSsnTable.setStatus("current")
_SgcLocalSsnEntry_Object = MibTableRow
sgcLocalSsnEntry = _SgcLocalSsnEntry_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 3, 1)
)
sgcLocalSsnEntry.setIndexNames(
    (0, "CTS-SGC-MIB", "sgcLocalSsnEntrySsn"),
)
if mibBuilder.loadTexts:
    sgcLocalSsnEntry.setStatus("current")
_SgcLocalSsnEntrySsn_Type = Counter32
_SgcLocalSsnEntrySsn_Object = MibTableColumn
sgcLocalSsnEntrySsn = _SgcLocalSsnEntrySsn_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 3, 1, 1),
    _SgcLocalSsnEntrySsn_Type()
)
sgcLocalSsnEntrySsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcLocalSsnEntrySsn.setStatus("current")
_SgcLocalSsnEntryStatus_Type = SgcSsnStatus
_SgcLocalSsnEntryStatus_Object = MibTableColumn
sgcLocalSsnEntryStatus = _SgcLocalSsnEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 3, 1, 2),
    _SgcLocalSsnEntryStatus_Type()
)
sgcLocalSsnEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcLocalSsnEntryStatus.setStatus("current")
_SgcLocalSsnEntrySent_Type = Counter32
_SgcLocalSsnEntrySent_Object = MibTableColumn
sgcLocalSsnEntrySent = _SgcLocalSsnEntrySent_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 3, 1, 3),
    _SgcLocalSsnEntrySent_Type()
)
sgcLocalSsnEntrySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcLocalSsnEntrySent.setStatus("current")
_SgcLocalSsnEntryReceived_Type = Counter32
_SgcLocalSsnEntryReceived_Object = MibTableColumn
sgcLocalSsnEntryReceived = _SgcLocalSsnEntryReceived_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 3, 1, 4),
    _SgcLocalSsnEntryReceived_Type()
)
sgcLocalSsnEntryReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcLocalSsnEntryReceived.setStatus("current")
_SgcLocalSsnEntryUnitdataReqCount_Type = Counter32
_SgcLocalSsnEntryUnitdataReqCount_Object = MibTableColumn
sgcLocalSsnEntryUnitdataReqCount = _SgcLocalSsnEntryUnitdataReqCount_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 3, 1, 5),
    _SgcLocalSsnEntryUnitdataReqCount_Type()
)
sgcLocalSsnEntryUnitdataReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcLocalSsnEntryUnitdataReqCount.setStatus("current")
_SgcLocalSsnEntryUDTSentCount_Type = Counter32
_SgcLocalSsnEntryUDTSentCount_Object = MibTableColumn
sgcLocalSsnEntryUDTSentCount = _SgcLocalSsnEntryUDTSentCount_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 3, 1, 6),
    _SgcLocalSsnEntryUDTSentCount_Type()
)
sgcLocalSsnEntryUDTSentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcLocalSsnEntryUDTSentCount.setStatus("current")
_SgcLocalSsnEntryXUDTSentNoSegmentationCount_Type = Counter32
_SgcLocalSsnEntryXUDTSentNoSegmentationCount_Object = MibTableColumn
sgcLocalSsnEntryXUDTSentNoSegmentationCount = _SgcLocalSsnEntryXUDTSentNoSegmentationCount_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 3, 1, 7),
    _SgcLocalSsnEntryXUDTSentNoSegmentationCount_Type()
)
sgcLocalSsnEntryXUDTSentNoSegmentationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcLocalSsnEntryXUDTSentNoSegmentationCount.setStatus("current")
_SgcLocalSsnEntryXUDTSentSegmentationCount_Type = Counter32
_SgcLocalSsnEntryXUDTSentSegmentationCount_Object = MibTableColumn
sgcLocalSsnEntryXUDTSentSegmentationCount = _SgcLocalSsnEntryXUDTSentSegmentationCount_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 3, 1, 8),
    _SgcLocalSsnEntryXUDTSentSegmentationCount_Type()
)
sgcLocalSsnEntryXUDTSentSegmentationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcLocalSsnEntryXUDTSentSegmentationCount.setStatus("current")
_SgcLocalSsnEntrySegmentationFailureCount_Type = Counter32
_SgcLocalSsnEntrySegmentationFailureCount_Object = MibTableColumn
sgcLocalSsnEntrySegmentationFailureCount = _SgcLocalSsnEntrySegmentationFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 3, 1, 9),
    _SgcLocalSsnEntrySegmentationFailureCount_Type()
)
sgcLocalSsnEntrySegmentationFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcLocalSsnEntrySegmentationFailureCount.setStatus("current")
_SgcLocalSsnEntryUDTReceivedCount_Type = Counter32
_SgcLocalSsnEntryUDTReceivedCount_Object = MibTableColumn
sgcLocalSsnEntryUDTReceivedCount = _SgcLocalSsnEntryUDTReceivedCount_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 3, 1, 10),
    _SgcLocalSsnEntryUDTReceivedCount_Type()
)
sgcLocalSsnEntryUDTReceivedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcLocalSsnEntryUDTReceivedCount.setStatus("current")
_SgcLocalSsnEntryXUDTReceivedNoSegmentationCount_Type = Counter32
_SgcLocalSsnEntryXUDTReceivedNoSegmentationCount_Object = MibTableColumn
sgcLocalSsnEntryXUDTReceivedNoSegmentationCount = _SgcLocalSsnEntryXUDTReceivedNoSegmentationCount_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 3, 1, 11),
    _SgcLocalSsnEntryXUDTReceivedNoSegmentationCount_Type()
)
sgcLocalSsnEntryXUDTReceivedNoSegmentationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcLocalSsnEntryXUDTReceivedNoSegmentationCount.setStatus("current")
_SgcLocalSsnEntryXUDTReceivedSegmentationCount_Type = Counter32
_SgcLocalSsnEntryXUDTReceivedSegmentationCount_Object = MibTableColumn
sgcLocalSsnEntryXUDTReceivedSegmentationCount = _SgcLocalSsnEntryXUDTReceivedSegmentationCount_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 3, 1, 12),
    _SgcLocalSsnEntryXUDTReceivedSegmentationCount_Type()
)
sgcLocalSsnEntryXUDTReceivedSegmentationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcLocalSsnEntryXUDTReceivedSegmentationCount.setStatus("current")
_SgcLocalSsnEntryUnitdataIndCount_Type = Counter32
_SgcLocalSsnEntryUnitdataIndCount_Object = MibTableColumn
sgcLocalSsnEntryUnitdataIndCount = _SgcLocalSsnEntryUnitdataIndCount_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 3, 1, 13),
    _SgcLocalSsnEntryUnitdataIndCount_Type()
)
sgcLocalSsnEntryUnitdataIndCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcLocalSsnEntryUnitdataIndCount.setStatus("current")
_SgcLocalSsnEntryReassembledUnitdataIndCount_Type = Counter32
_SgcLocalSsnEntryReassembledUnitdataIndCount_Object = MibTableColumn
sgcLocalSsnEntryReassembledUnitdataIndCount = _SgcLocalSsnEntryReassembledUnitdataIndCount_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 3, 1, 14),
    _SgcLocalSsnEntryReassembledUnitdataIndCount_Type()
)
sgcLocalSsnEntryReassembledUnitdataIndCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcLocalSsnEntryReassembledUnitdataIndCount.setStatus("current")
_SgcLocalSsnEntryReassemblyFailureCount_Type = Counter32
_SgcLocalSsnEntryReassemblyFailureCount_Object = MibTableColumn
sgcLocalSsnEntryReassemblyFailureCount = _SgcLocalSsnEntryReassemblyFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 3, 1, 15),
    _SgcLocalSsnEntryReassemblyFailureCount_Type()
)
sgcLocalSsnEntryReassemblyFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcLocalSsnEntryReassemblyFailureCount.setStatus("current")
_SgcTcapConnectionTable_Object = MibTable
sgcTcapConnectionTable = _SgcTcapConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sgcTcapConnectionTable.setStatus("current")
_SgcTcapConnectionEntry_Object = MibTableRow
sgcTcapConnectionEntry = _SgcTcapConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 4, 1)
)
sgcTcapConnectionEntry.setIndexNames(
    (0, "CTS-SGC-MIB", "sgcTcapConnectionEntryIdx"),
)
if mibBuilder.loadTexts:
    sgcTcapConnectionEntry.setStatus("current")
_SgcTcapConnectionEntryIdx_Type = Counter32
_SgcTcapConnectionEntryIdx_Object = MibTableColumn
sgcTcapConnectionEntryIdx = _SgcTcapConnectionEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 4, 1, 1),
    _SgcTcapConnectionEntryIdx_Type()
)
sgcTcapConnectionEntryIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcTcapConnectionEntryIdx.setStatus("current")
_SgcTcapConnectionEntrySsn_Type = Integer32
_SgcTcapConnectionEntrySsn_Object = MibTableColumn
sgcTcapConnectionEntrySsn = _SgcTcapConnectionEntrySsn_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 4, 1, 2),
    _SgcTcapConnectionEntrySsn_Type()
)
sgcTcapConnectionEntrySsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcTcapConnectionEntrySsn.setStatus("current")
_SgcTcapConnectionEntryPrefix_Type = Integer32
_SgcTcapConnectionEntryPrefix_Object = MibTableColumn
sgcTcapConnectionEntryPrefix = _SgcTcapConnectionEntryPrefix_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 4, 1, 3),
    _SgcTcapConnectionEntryPrefix_Type()
)
sgcTcapConnectionEntryPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcTcapConnectionEntryPrefix.setStatus("current")
_SgcTcapConnectionEntryRemoteIp_Type = OctetString
_SgcTcapConnectionEntryRemoteIp_Object = MibTableColumn
sgcTcapConnectionEntryRemoteIp = _SgcTcapConnectionEntryRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 4, 1, 4),
    _SgcTcapConnectionEntryRemoteIp_Type()
)
sgcTcapConnectionEntryRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcTcapConnectionEntryRemoteIp.setStatus("current")
_SgcTcapConnectionEntryRemotePort_Type = Integer32
_SgcTcapConnectionEntryRemotePort_Object = MibTableColumn
sgcTcapConnectionEntryRemotePort = _SgcTcapConnectionEntryRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 4, 1, 5),
    _SgcTcapConnectionEntryRemotePort_Type()
)
sgcTcapConnectionEntryRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcTcapConnectionEntryRemotePort.setStatus("current")
_SgcTcapConnectionEntryLocalIp_Type = OctetString
_SgcTcapConnectionEntryLocalIp_Object = MibTableColumn
sgcTcapConnectionEntryLocalIp = _SgcTcapConnectionEntryLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 4, 1, 6),
    _SgcTcapConnectionEntryLocalIp_Type()
)
sgcTcapConnectionEntryLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcTcapConnectionEntryLocalIp.setStatus("current")
_SgcTcapConnectionEntryLocalPort_Type = Integer32
_SgcTcapConnectionEntryLocalPort_Object = MibTableColumn
sgcTcapConnectionEntryLocalPort = _SgcTcapConnectionEntryLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 4, 1, 7),
    _SgcTcapConnectionEntryLocalPort_Type()
)
sgcTcapConnectionEntryLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcTcapConnectionEntryLocalPort.setStatus("current")
_SgcTcapConnectionEntryServingNode_Type = OctetString
_SgcTcapConnectionEntryServingNode_Object = MibTableColumn
sgcTcapConnectionEntryServingNode = _SgcTcapConnectionEntryServingNode_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 4, 1, 8),
    _SgcTcapConnectionEntryServingNode_Type()
)
sgcTcapConnectionEntryServingNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcTcapConnectionEntryServingNode.setStatus("current")
_SgcTcapConnectionEntrySent_Type = Counter32
_SgcTcapConnectionEntrySent_Object = MibTableColumn
sgcTcapConnectionEntrySent = _SgcTcapConnectionEntrySent_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 4, 1, 9),
    _SgcTcapConnectionEntrySent_Type()
)
sgcTcapConnectionEntrySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcTcapConnectionEntrySent.setStatus("current")
_SgcTcapConnectionEntryReceived_Type = Counter32
_SgcTcapConnectionEntryReceived_Object = MibTableColumn
sgcTcapConnectionEntryReceived = _SgcTcapConnectionEntryReceived_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 4, 1, 10),
    _SgcTcapConnectionEntryReceived_Type()
)
sgcTcapConnectionEntryReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcTcapConnectionEntryReceived.setStatus("current")
_SgcTcapConnectionEntryConnectedTime_Type = ExtUTCTime
_SgcTcapConnectionEntryConnectedTime_Object = MibTableColumn
sgcTcapConnectionEntryConnectedTime = _SgcTcapConnectionEntryConnectedTime_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 4, 1, 11),
    _SgcTcapConnectionEntryConnectedTime_Type()
)
sgcTcapConnectionEntryConnectedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcTcapConnectionEntryConnectedTime.setStatus("current")
_SgcDpcStatusTable_Object = MibTable
sgcDpcStatusTable = _SgcDpcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 5)
)
if mibBuilder.loadTexts:
    sgcDpcStatusTable.setStatus("current")
_SgcDpcStatusEntry_Object = MibTableRow
sgcDpcStatusEntry = _SgcDpcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 5, 1)
)
sgcDpcStatusEntry.setIndexNames(
    (0, "CTS-SGC-MIB", "sgcDpcStatusEntryDPC"),
)
if mibBuilder.loadTexts:
    sgcDpcStatusEntry.setStatus("current")
_SgcDpcStatusEntryDPC_Type = OctetString
_SgcDpcStatusEntryDPC_Object = MibTableColumn
sgcDpcStatusEntryDPC = _SgcDpcStatusEntryDPC_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 5, 1, 1),
    _SgcDpcStatusEntryDPC_Type()
)
sgcDpcStatusEntryDPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcDpcStatusEntryDPC.setStatus("current")
_SgcDpcStatusEntryConnectionId_Type = OctetString
_SgcDpcStatusEntryConnectionId_Object = MibTableColumn
sgcDpcStatusEntryConnectionId = _SgcDpcStatusEntryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 5, 1, 2),
    _SgcDpcStatusEntryConnectionId_Type()
)
sgcDpcStatusEntryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcDpcStatusEntryConnectionId.setStatus("current")
_SgcDpcStatusEntryStatus_Type = SgcDpcStatus
_SgcDpcStatusEntryStatus_Object = MibTableColumn
sgcDpcStatusEntryStatus = _SgcDpcStatusEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 5, 1, 3),
    _SgcDpcStatusEntryStatus_Type()
)
sgcDpcStatusEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcDpcStatusEntryStatus.setStatus("current")
_SgcGtRoutingTable_Object = MibTable
sgcGtRoutingTable = _SgcGtRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 6)
)
if mibBuilder.loadTexts:
    sgcGtRoutingTable.setStatus("current")
_SgcGtRoutingEntry_Object = MibTableRow
sgcGtRoutingEntry = _SgcGtRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 6, 1)
)
sgcGtRoutingEntry.setIndexNames(
    (0, "CTS-SGC-MIB", "sgcGtRoutingEntryIdx"),
)
if mibBuilder.loadTexts:
    sgcGtRoutingEntry.setStatus("current")
_SgcGtRoutingEntryIdx_Type = Counter32
_SgcGtRoutingEntryIdx_Object = MibTableColumn
sgcGtRoutingEntryIdx = _SgcGtRoutingEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 6, 1, 1),
    _SgcGtRoutingEntryIdx_Type()
)
sgcGtRoutingEntryIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcGtRoutingEntryIdx.setStatus("current")
_SgcGtRoutingEntryAddrType_Type = OctetString
_SgcGtRoutingEntryAddrType_Object = MibTableColumn
sgcGtRoutingEntryAddrType = _SgcGtRoutingEntryAddrType_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 6, 1, 2),
    _SgcGtRoutingEntryAddrType_Type()
)
sgcGtRoutingEntryAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcGtRoutingEntryAddrType.setStatus("current")
_SgcGtRoutingEntryAddressInfo_Type = OctetString
_SgcGtRoutingEntryAddressInfo_Object = MibTableColumn
sgcGtRoutingEntryAddressInfo = _SgcGtRoutingEntryAddressInfo_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 6, 1, 3),
    _SgcGtRoutingEntryAddressInfo_Type()
)
sgcGtRoutingEntryAddressInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcGtRoutingEntryAddressInfo.setStatus("current")
_SgcGtRoutingEntryConnectionId_Type = OctetString
_SgcGtRoutingEntryConnectionId_Object = MibTableColumn
sgcGtRoutingEntryConnectionId = _SgcGtRoutingEntryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 6, 1, 4),
    _SgcGtRoutingEntryConnectionId_Type()
)
sgcGtRoutingEntryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcGtRoutingEntryConnectionId.setStatus("current")
_SgcGtRoutingEntryDPC_Type = OctetString
_SgcGtRoutingEntryDPC_Object = MibTableColumn
sgcGtRoutingEntryDPC = _SgcGtRoutingEntryDPC_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 6, 1, 5),
    _SgcGtRoutingEntryDPC_Type()
)
sgcGtRoutingEntryDPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcGtRoutingEntryDPC.setStatus("current")
_SgcGtRoutingEntryRc_Type = Integer32
_SgcGtRoutingEntryRc_Object = MibTableColumn
sgcGtRoutingEntryRc = _SgcGtRoutingEntryRc_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 6, 1, 6),
    _SgcGtRoutingEntryRc_Type()
)
sgcGtRoutingEntryRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcGtRoutingEntryRc.setStatus("current")
_SgcGtRoutingEntryNodeId_Type = OctetString
_SgcGtRoutingEntryNodeId_Object = MibTableColumn
sgcGtRoutingEntryNodeId = _SgcGtRoutingEntryNodeId_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 6, 1, 7),
    _SgcGtRoutingEntryNodeId_Type()
)
sgcGtRoutingEntryNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcGtRoutingEntryNodeId.setStatus("current")
_SgcPcRoutingTable_Object = MibTable
sgcPcRoutingTable = _SgcPcRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 7)
)
if mibBuilder.loadTexts:
    sgcPcRoutingTable.setStatus("current")
_SgcPcRoutingEntry_Object = MibTableRow
sgcPcRoutingEntry = _SgcPcRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 7, 1)
)
sgcPcRoutingEntry.setIndexNames(
    (0, "CTS-SGC-MIB", "sgcPcRoutingEntryIdx"),
)
if mibBuilder.loadTexts:
    sgcPcRoutingEntry.setStatus("current")
_SgcPcRoutingEntryIdx_Type = Counter32
_SgcPcRoutingEntryIdx_Object = MibTableColumn
sgcPcRoutingEntryIdx = _SgcPcRoutingEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 7, 1, 1),
    _SgcPcRoutingEntryIdx_Type()
)
sgcPcRoutingEntryIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcPcRoutingEntryIdx.setStatus("current")
_SgcPcRoutingEntryNodeId_Type = OctetString
_SgcPcRoutingEntryNodeId_Object = MibTableColumn
sgcPcRoutingEntryNodeId = _SgcPcRoutingEntryNodeId_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 7, 1, 2),
    _SgcPcRoutingEntryNodeId_Type()
)
sgcPcRoutingEntryNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcPcRoutingEntryNodeId.setStatus("current")
_SgcPcRoutingEntryDPC_Type = OctetString
_SgcPcRoutingEntryDPC_Object = MibTableColumn
sgcPcRoutingEntryDPC = _SgcPcRoutingEntryDPC_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 7, 1, 3),
    _SgcPcRoutingEntryDPC_Type()
)
sgcPcRoutingEntryDPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcPcRoutingEntryDPC.setStatus("current")
_SgcPcRoutingEntryConnectionId_Type = OctetString
_SgcPcRoutingEntryConnectionId_Object = MibTableColumn
sgcPcRoutingEntryConnectionId = _SgcPcRoutingEntryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 7, 1, 4),
    _SgcPcRoutingEntryConnectionId_Type()
)
sgcPcRoutingEntryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcPcRoutingEntryConnectionId.setStatus("current")
_SgcPcRoutingEntryRc_Type = Integer32
_SgcPcRoutingEntryRc_Object = MibTableColumn
sgcPcRoutingEntryRc = _SgcPcRoutingEntryRc_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 7, 1, 5),
    _SgcPcRoutingEntryRc_Type()
)
sgcPcRoutingEntryRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcPcRoutingEntryRc.setStatus("current")
_SgcRemoteSsnTable_Object = MibTable
sgcRemoteSsnTable = _SgcRemoteSsnTable_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 8)
)
if mibBuilder.loadTexts:
    sgcRemoteSsnTable.setStatus("current")
_SgcRemoteSsnEntry_Object = MibTableRow
sgcRemoteSsnEntry = _SgcRemoteSsnEntry_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 8, 1)
)
sgcRemoteSsnEntry.setIndexNames(
    (0, "CTS-SGC-MIB", "sgcRemoteSsnEntryIdx"),
)
if mibBuilder.loadTexts:
    sgcRemoteSsnEntry.setStatus("current")
_SgcRemoteSsnEntryIdx_Type = Counter32
_SgcRemoteSsnEntryIdx_Object = MibTableColumn
sgcRemoteSsnEntryIdx = _SgcRemoteSsnEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 8, 1, 1),
    _SgcRemoteSsnEntryIdx_Type()
)
sgcRemoteSsnEntryIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcRemoteSsnEntryIdx.setStatus("current")
_SgcRemoteSsnEntryDPC_Type = OctetString
_SgcRemoteSsnEntryDPC_Object = MibTableColumn
sgcRemoteSsnEntryDPC = _SgcRemoteSsnEntryDPC_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 8, 1, 2),
    _SgcRemoteSsnEntryDPC_Type()
)
sgcRemoteSsnEntryDPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcRemoteSsnEntryDPC.setStatus("current")
_SgcRemoteSsnEntrySsn_Type = Integer32
_SgcRemoteSsnEntrySsn_Object = MibTableColumn
sgcRemoteSsnEntrySsn = _SgcRemoteSsnEntrySsn_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 8, 1, 3),
    _SgcRemoteSsnEntrySsn_Type()
)
sgcRemoteSsnEntrySsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcRemoteSsnEntrySsn.setStatus("current")
_SgcRemoteSsnEntryStatus_Type = SgcSsnStatus
_SgcRemoteSsnEntryStatus_Object = MibTableColumn
sgcRemoteSsnEntryStatus = _SgcRemoteSsnEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 8, 1, 4),
    _SgcRemoteSsnEntryStatus_Type()
)
sgcRemoteSsnEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcRemoteSsnEntryStatus.setStatus("current")
_SgcHealthTable_Object = MibTable
sgcHealthTable = _SgcHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 9)
)
if mibBuilder.loadTexts:
    sgcHealthTable.setStatus("current")
_SgcHealthEntry_Object = MibTableRow
sgcHealthEntry = _SgcHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 9, 1)
)
sgcHealthEntry.setIndexNames(
    (0, "CTS-SGC-MIB", "sgcHealthEntryNodeId"),
)
if mibBuilder.loadTexts:
    sgcHealthEntry.setStatus("current")
_SgcHealthEntryNodeId_Type = OctetString
_SgcHealthEntryNodeId_Object = MibTableColumn
sgcHealthEntryNodeId = _SgcHealthEntryNodeId_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 9, 1, 1),
    _SgcHealthEntryNodeId_Type()
)
sgcHealthEntryNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcHealthEntryNodeId.setStatus("current")
_SgcEntryWorkgroupQueueSize_Type = Integer32
_SgcEntryWorkgroupQueueSize_Object = MibTableColumn
sgcEntryWorkgroupQueueSize = _SgcEntryWorkgroupQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 9, 1, 2),
    _SgcEntryWorkgroupQueueSize_Type()
)
sgcEntryWorkgroupQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcEntryWorkgroupQueueSize.setStatus("current")
_SgcHealthEntryAllocatedIndTasks_Type = Integer32
_SgcHealthEntryAllocatedIndTasks_Object = MibTableColumn
sgcHealthEntryAllocatedIndTasks = _SgcHealthEntryAllocatedIndTasks_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 9, 1, 3),
    _SgcHealthEntryAllocatedIndTasks_Type()
)
sgcHealthEntryAllocatedIndTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcHealthEntryAllocatedIndTasks.setStatus("current")
_SgcHealthEntryAllocatedReqTasks_Type = Integer32
_SgcHealthEntryAllocatedReqTasks_Object = MibTableColumn
sgcHealthEntryAllocatedReqTasks = _SgcHealthEntryAllocatedReqTasks_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 9, 1, 4),
    _SgcHealthEntryAllocatedReqTasks_Type()
)
sgcHealthEntryAllocatedReqTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcHealthEntryAllocatedReqTasks.setStatus("current")
_SgcHealthEntryExecutorTasks_Type = Integer32
_SgcHealthEntryExecutorTasks_Object = MibTableColumn
sgcHealthEntryExecutorTasks = _SgcHealthEntryExecutorTasks_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 9, 1, 5),
    _SgcHealthEntryExecutorTasks_Type()
)
sgcHealthEntryExecutorTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcHealthEntryExecutorTasks.setStatus("current")
_SgcHealthEntryExecutedTasksTime_Type = Counter64
_SgcHealthEntryExecutedTasksTime_Object = MibTableColumn
sgcHealthEntryExecutedTasksTime = _SgcHealthEntryExecutedTasksTime_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 9, 1, 6),
    _SgcHealthEntryExecutedTasksTime_Type()
)
sgcHealthEntryExecutedTasksTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcHealthEntryExecutedTasksTime.setStatus("current")
_SgcHealthEntryExecutedTasksNo_Type = Counter32
_SgcHealthEntryExecutedTasksNo_Object = MibTableColumn
sgcHealthEntryExecutedTasksNo = _SgcHealthEntryExecutedTasksNo_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 1, 9, 1, 7),
    _SgcHealthEntryExecutedTasksNo_Type()
)
sgcHealthEntryExecutedTasksNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcHealthEntryExecutedTasksNo.setStatus("current")
_SgcEvents_ObjectIdentity = ObjectIdentity
sgcEvents = _SgcEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2)
)
_SgcAlarmObjects_ObjectIdentity = ObjectIdentity
sgcAlarmObjects = _SgcAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 4)
)
_SgcEventId_Type = Counter32
_SgcEventId_Object = MibScalar
sgcEventId = _SgcEventId_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 4, 2),
    _SgcEventId_Type()
)
sgcEventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sgcEventId.setStatus("current")
_SgcTimestamp_Type = ExtUTCTime
_SgcTimestamp_Object = MibScalar
sgcTimestamp = _SgcTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 4, 3),
    _SgcTimestamp_Type()
)
sgcTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sgcTimestamp.setStatus("current")
_SgcAlarmName_Type = OctetString
_SgcAlarmName_Object = MibScalar
sgcAlarmName = _SgcAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 4, 4),
    _SgcAlarmName_Type()
)
sgcAlarmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sgcAlarmName.setStatus("current")
_SgcAlarmSeverity_Type = SgcSeverity
_SgcAlarmSeverity_Object = MibScalar
sgcAlarmSeverity = _SgcAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 4, 5),
    _SgcAlarmSeverity_Type()
)
sgcAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sgcAlarmSeverity.setStatus("current")
_SgcAdditionalInfo_Type = OctetString
_SgcAdditionalInfo_Object = MibScalar
sgcAdditionalInfo = _SgcAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 4, 6),
    _SgcAdditionalInfo_Type()
)
sgcAdditionalInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sgcAdditionalInfo.setStatus("current")
_SgcActiveAlarmsTable_Object = MibTable
sgcActiveAlarmsTable = _SgcActiveAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 5)
)
if mibBuilder.loadTexts:
    sgcActiveAlarmsTable.setStatus("current")
_SgcActiveAlarmsEntry_Object = MibTableRow
sgcActiveAlarmsEntry = _SgcActiveAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 5, 1)
)
sgcActiveAlarmsEntry.setIndexNames(
    (0, "CTS-SGC-MIB", "sgcActiveAlarmsEntryId"),
)
if mibBuilder.loadTexts:
    sgcActiveAlarmsEntry.setStatus("current")
_SgcActiveAlarmsEntryId_Type = Counter32
_SgcActiveAlarmsEntryId_Object = MibTableColumn
sgcActiveAlarmsEntryId = _SgcActiveAlarmsEntryId_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 5, 1, 1),
    _SgcActiveAlarmsEntryId_Type()
)
sgcActiveAlarmsEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcActiveAlarmsEntryId.setStatus("current")
_SgcActiveAlarmsEntryTimestamp_Type = ExtUTCTime
_SgcActiveAlarmsEntryTimestamp_Object = MibTableColumn
sgcActiveAlarmsEntryTimestamp = _SgcActiveAlarmsEntryTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 5, 1, 2),
    _SgcActiveAlarmsEntryTimestamp_Type()
)
sgcActiveAlarmsEntryTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcActiveAlarmsEntryTimestamp.setStatus("current")
_SgcActiveAlarmsEntryName_Type = OctetString
_SgcActiveAlarmsEntryName_Object = MibTableColumn
sgcActiveAlarmsEntryName = _SgcActiveAlarmsEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 5, 1, 3),
    _SgcActiveAlarmsEntryName_Type()
)
sgcActiveAlarmsEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcActiveAlarmsEntryName.setStatus("current")
_SgcActiveAlarmsEntrySeverity_Type = SgcSeverity
_SgcActiveAlarmsEntrySeverity_Object = MibTableColumn
sgcActiveAlarmsEntrySeverity = _SgcActiveAlarmsEntrySeverity_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 5, 1, 4),
    _SgcActiveAlarmsEntrySeverity_Type()
)
sgcActiveAlarmsEntrySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcActiveAlarmsEntrySeverity.setStatus("current")
_SgcActiveAlarmsEntryInfo_Type = OctetString
_SgcActiveAlarmsEntryInfo_Object = MibTableColumn
sgcActiveAlarmsEntryInfo = _SgcActiveAlarmsEntryInfo_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 5, 1, 5),
    _SgcActiveAlarmsEntryInfo_Type()
)
sgcActiveAlarmsEntryInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcActiveAlarmsEntryInfo.setStatus("current")
_SgcEventHistoryTable_Object = MibTable
sgcEventHistoryTable = _SgcEventHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 6)
)
if mibBuilder.loadTexts:
    sgcEventHistoryTable.setStatus("current")
_SgcEventHistoryEntry_Object = MibTableRow
sgcEventHistoryEntry = _SgcEventHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 6, 1)
)
sgcEventHistoryEntry.setIndexNames(
    (0, "CTS-SGC-MIB", "sgcEventHistoryEntryIdx"),
)
if mibBuilder.loadTexts:
    sgcEventHistoryEntry.setStatus("current")
_SgcEventHistoryEntryIdx_Type = Counter32
_SgcEventHistoryEntryIdx_Object = MibTableColumn
sgcEventHistoryEntryIdx = _SgcEventHistoryEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 6, 1, 1),
    _SgcEventHistoryEntryIdx_Type()
)
sgcEventHistoryEntryIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcEventHistoryEntryIdx.setStatus("current")
_SgcEventHistoryEntryId_Type = Integer32
_SgcEventHistoryEntryId_Object = MibTableColumn
sgcEventHistoryEntryId = _SgcEventHistoryEntryId_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 6, 1, 2),
    _SgcEventHistoryEntryId_Type()
)
sgcEventHistoryEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcEventHistoryEntryId.setStatus("current")
_SgcEventHistoryEntryName_Type = OctetString
_SgcEventHistoryEntryName_Object = MibTableColumn
sgcEventHistoryEntryName = _SgcEventHistoryEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 6, 1, 3),
    _SgcEventHistoryEntryName_Type()
)
sgcEventHistoryEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcEventHistoryEntryName.setStatus("current")
_SgcEventHistoryEntryTimestamp_Type = ExtUTCTime
_SgcEventHistoryEntryTimestamp_Object = MibTableColumn
sgcEventHistoryEntryTimestamp = _SgcEventHistoryEntryTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 6, 1, 4),
    _SgcEventHistoryEntryTimestamp_Type()
)
sgcEventHistoryEntryTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcEventHistoryEntryTimestamp.setStatus("current")
_SgcEventHistoryEntrySeverity_Type = SgcSeverity
_SgcEventHistoryEntrySeverity_Object = MibTableColumn
sgcEventHistoryEntrySeverity = _SgcEventHistoryEntrySeverity_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 6, 1, 5),
    _SgcEventHistoryEntrySeverity_Type()
)
sgcEventHistoryEntrySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcEventHistoryEntrySeverity.setStatus("current")
_SgcEventHistoryEntryInfo_Type = OctetString
_SgcEventHistoryEntryInfo_Object = MibTableColumn
sgcEventHistoryEntryInfo = _SgcEventHistoryEntryInfo_Object(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 6, 1, 6),
    _SgcEventHistoryEntryInfo_Type()
)
sgcEventHistoryEntryInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgcEventHistoryEntryInfo.setStatus("current")
_SgcConf_ObjectIdentity = ObjectIdentity
sgcConf = _SgcConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35787, 1, 3)
)
_SgcGroups_ObjectIdentity = ObjectIdentity
sgcGroups = _SgcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35787, 1, 3, 1)
)
_SgcCompls_ObjectIdentity = ObjectIdentity
sgcCompls = _SgcCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35787, 1, 3, 2)
)

# Managed Objects groups

sgcBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35787, 1, 3, 1, 1)
)
sgcBasicGroup.setObjects(
      *(("CTS-SGC-MIB", "sgcEventId"),
        ("CTS-SGC-MIB", "sgcTimestamp"),
        ("CTS-SGC-MIB", "sgcAlarmName"),
        ("CTS-SGC-MIB", "sgcAlarmSeverity"),
        ("CTS-SGC-MIB", "sgcAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sgcBasicGroup.setStatus("current")

sgcEventObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35787, 1, 3, 1, 3)
)
sgcEventObjectsGroup.setObjects(
      *(("CTS-SGC-MIB", "sgcActiveAlarmsEntryId"),
        ("CTS-SGC-MIB", "sgcActiveAlarmsEntryTimestamp"),
        ("CTS-SGC-MIB", "sgcActiveAlarmsEntryName"),
        ("CTS-SGC-MIB", "sgcActiveAlarmsEntrySeverity"),
        ("CTS-SGC-MIB", "sgcActiveAlarmsEntryInfo"),
        ("CTS-SGC-MIB", "sgcEventHistoryEntryIdx"),
        ("CTS-SGC-MIB", "sgcEventHistoryEntryId"),
        ("CTS-SGC-MIB", "sgcEventHistoryEntryName"),
        ("CTS-SGC-MIB", "sgcEventHistoryEntryTimestamp"),
        ("CTS-SGC-MIB", "sgcEventHistoryEntrySeverity"),
        ("CTS-SGC-MIB", "sgcEventHistoryEntryInfo"))
)
if mibBuilder.loadTexts:
    sgcEventObjectsGroup.setStatus("current")


# Notification objects

sgcAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 2)
)
sgcAlarm.setObjects(
      *(("CTS-SGC-MIB", "sgcEventId"),
        ("CTS-SGC-MIB", "sgcAlarmName"),
        ("CTS-SGC-MIB", "sgcAlarmSeverity"),
        ("CTS-SGC-MIB", "sgcAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sgcAlarm.setStatus(
        "current"
    )

sgcNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 35787, 1, 2, 3)
)
sgcNotification.setObjects(
      *(("CTS-SGC-MIB", "sgcEventId"),
        ("CTS-SGC-MIB", "sgcAlarmName"),
        ("CTS-SGC-MIB", "sgcAlarmSeverity"),
        ("CTS-SGC-MIB", "sgcAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sgcNotification.setStatus(
        "current"
    )


# Notifications groups

sgcBasicEvents = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35787, 1, 3, 1, 2)
)
sgcBasicEvents.setObjects(
      *(("CTS-SGC-MIB", "sgcAlarm"),
        ("CTS-SGC-MIB", "sgcNotification"))
)
if mibBuilder.loadTexts:
    sgcBasicEvents.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTS-SGC-MIB",
    **{"SgcDpcStatus": SgcDpcStatus,
       "SgcSeverity": SgcSeverity,
       "SgcSsnStatus": SgcSsnStatus,
       "sgcMIB": sgcMIB,
       "sgcObjects": sgcObjects,
       "sgcAssociationTable": sgcAssociationTable,
       "sgcAssociationEntry": sgcAssociationEntry,
       "sgcAssociationEntryIdx": sgcAssociationEntryIdx,
       "sgcAssociationEntryConnectionName": sgcAssociationEntryConnectionName,
       "sgcAssociationEntryNodeName": sgcAssociationEntryNodeName,
       "sgcAssociationEntryStatus": sgcAssociationEntryStatus,
       "sgcAssociationEntryRXSctpCount": sgcAssociationEntryRXSctpCount,
       "sgcAssociationEntryTXSctpCount": sgcAssociationEntryTXSctpCount,
       "sgcAssociationEntryRXDataCount": sgcAssociationEntryRXDataCount,
       "sgcAssociationEntryTXDataCount": sgcAssociationEntryTXDataCount,
       "sgcAssociationEntryRXErrorCount": sgcAssociationEntryRXErrorCount,
       "sgcAssociationEntryTXErrorCount": sgcAssociationEntryTXErrorCount,
       "sgcAssociationEntryPeerAddresses": sgcAssociationEntryPeerAddresses,
       "sgcAssociationEntrySctpInStreams": sgcAssociationEntrySctpInStreams,
       "sgcAssociationEntrySctpOutStreams": sgcAssociationEntrySctpOutStreams,
       "sgcAssociationEntrySctpOptions": sgcAssociationEntrySctpOptions,
       "sgcAsStateTable": sgcAsStateTable,
       "sgcAsStateEntry": sgcAsStateEntry,
       "sgcAsStateEntryIdx": sgcAsStateEntryIdx,
       "sgcAsStateEntryAsId": sgcAsStateEntryAsId,
       "sgcAsStateEntryConnectionId": sgcAsStateEntryConnectionId,
       "sgcAsStateEntryReceived": sgcAsStateEntryReceived,
       "sgcAsStateEntrySent": sgcAsStateEntrySent,
       "sgcAsStateEntryNodeId": sgcAsStateEntryNodeId,
       "sgcAsStateEntryStatus": sgcAsStateEntryStatus,
       "sgcLocalSsnTable": sgcLocalSsnTable,
       "sgcLocalSsnEntry": sgcLocalSsnEntry,
       "sgcLocalSsnEntrySsn": sgcLocalSsnEntrySsn,
       "sgcLocalSsnEntryStatus": sgcLocalSsnEntryStatus,
       "sgcLocalSsnEntrySent": sgcLocalSsnEntrySent,
       "sgcLocalSsnEntryReceived": sgcLocalSsnEntryReceived,
       "sgcLocalSsnEntryUnitdataReqCount": sgcLocalSsnEntryUnitdataReqCount,
       "sgcLocalSsnEntryUDTSentCount": sgcLocalSsnEntryUDTSentCount,
       "sgcLocalSsnEntryXUDTSentNoSegmentationCount": sgcLocalSsnEntryXUDTSentNoSegmentationCount,
       "sgcLocalSsnEntryXUDTSentSegmentationCount": sgcLocalSsnEntryXUDTSentSegmentationCount,
       "sgcLocalSsnEntrySegmentationFailureCount": sgcLocalSsnEntrySegmentationFailureCount,
       "sgcLocalSsnEntryUDTReceivedCount": sgcLocalSsnEntryUDTReceivedCount,
       "sgcLocalSsnEntryXUDTReceivedNoSegmentationCount": sgcLocalSsnEntryXUDTReceivedNoSegmentationCount,
       "sgcLocalSsnEntryXUDTReceivedSegmentationCount": sgcLocalSsnEntryXUDTReceivedSegmentationCount,
       "sgcLocalSsnEntryUnitdataIndCount": sgcLocalSsnEntryUnitdataIndCount,
       "sgcLocalSsnEntryReassembledUnitdataIndCount": sgcLocalSsnEntryReassembledUnitdataIndCount,
       "sgcLocalSsnEntryReassemblyFailureCount": sgcLocalSsnEntryReassemblyFailureCount,
       "sgcTcapConnectionTable": sgcTcapConnectionTable,
       "sgcTcapConnectionEntry": sgcTcapConnectionEntry,
       "sgcTcapConnectionEntryIdx": sgcTcapConnectionEntryIdx,
       "sgcTcapConnectionEntrySsn": sgcTcapConnectionEntrySsn,
       "sgcTcapConnectionEntryPrefix": sgcTcapConnectionEntryPrefix,
       "sgcTcapConnectionEntryRemoteIp": sgcTcapConnectionEntryRemoteIp,
       "sgcTcapConnectionEntryRemotePort": sgcTcapConnectionEntryRemotePort,
       "sgcTcapConnectionEntryLocalIp": sgcTcapConnectionEntryLocalIp,
       "sgcTcapConnectionEntryLocalPort": sgcTcapConnectionEntryLocalPort,
       "sgcTcapConnectionEntryServingNode": sgcTcapConnectionEntryServingNode,
       "sgcTcapConnectionEntrySent": sgcTcapConnectionEntrySent,
       "sgcTcapConnectionEntryReceived": sgcTcapConnectionEntryReceived,
       "sgcTcapConnectionEntryConnectedTime": sgcTcapConnectionEntryConnectedTime,
       "sgcDpcStatusTable": sgcDpcStatusTable,
       "sgcDpcStatusEntry": sgcDpcStatusEntry,
       "sgcDpcStatusEntryDPC": sgcDpcStatusEntryDPC,
       "sgcDpcStatusEntryConnectionId": sgcDpcStatusEntryConnectionId,
       "sgcDpcStatusEntryStatus": sgcDpcStatusEntryStatus,
       "sgcGtRoutingTable": sgcGtRoutingTable,
       "sgcGtRoutingEntry": sgcGtRoutingEntry,
       "sgcGtRoutingEntryIdx": sgcGtRoutingEntryIdx,
       "sgcGtRoutingEntryAddrType": sgcGtRoutingEntryAddrType,
       "sgcGtRoutingEntryAddressInfo": sgcGtRoutingEntryAddressInfo,
       "sgcGtRoutingEntryConnectionId": sgcGtRoutingEntryConnectionId,
       "sgcGtRoutingEntryDPC": sgcGtRoutingEntryDPC,
       "sgcGtRoutingEntryRc": sgcGtRoutingEntryRc,
       "sgcGtRoutingEntryNodeId": sgcGtRoutingEntryNodeId,
       "sgcPcRoutingTable": sgcPcRoutingTable,
       "sgcPcRoutingEntry": sgcPcRoutingEntry,
       "sgcPcRoutingEntryIdx": sgcPcRoutingEntryIdx,
       "sgcPcRoutingEntryNodeId": sgcPcRoutingEntryNodeId,
       "sgcPcRoutingEntryDPC": sgcPcRoutingEntryDPC,
       "sgcPcRoutingEntryConnectionId": sgcPcRoutingEntryConnectionId,
       "sgcPcRoutingEntryRc": sgcPcRoutingEntryRc,
       "sgcRemoteSsnTable": sgcRemoteSsnTable,
       "sgcRemoteSsnEntry": sgcRemoteSsnEntry,
       "sgcRemoteSsnEntryIdx": sgcRemoteSsnEntryIdx,
       "sgcRemoteSsnEntryDPC": sgcRemoteSsnEntryDPC,
       "sgcRemoteSsnEntrySsn": sgcRemoteSsnEntrySsn,
       "sgcRemoteSsnEntryStatus": sgcRemoteSsnEntryStatus,
       "sgcHealthTable": sgcHealthTable,
       "sgcHealthEntry": sgcHealthEntry,
       "sgcHealthEntryNodeId": sgcHealthEntryNodeId,
       "sgcEntryWorkgroupQueueSize": sgcEntryWorkgroupQueueSize,
       "sgcHealthEntryAllocatedIndTasks": sgcHealthEntryAllocatedIndTasks,
       "sgcHealthEntryAllocatedReqTasks": sgcHealthEntryAllocatedReqTasks,
       "sgcHealthEntryExecutorTasks": sgcHealthEntryExecutorTasks,
       "sgcHealthEntryExecutedTasksTime": sgcHealthEntryExecutedTasksTime,
       "sgcHealthEntryExecutedTasksNo": sgcHealthEntryExecutedTasksNo,
       "sgcEvents": sgcEvents,
       "sgcAlarm": sgcAlarm,
       "sgcNotification": sgcNotification,
       "sgcAlarmObjects": sgcAlarmObjects,
       "sgcEventId": sgcEventId,
       "sgcTimestamp": sgcTimestamp,
       "sgcAlarmName": sgcAlarmName,
       "sgcAlarmSeverity": sgcAlarmSeverity,
       "sgcAdditionalInfo": sgcAdditionalInfo,
       "sgcActiveAlarmsTable": sgcActiveAlarmsTable,
       "sgcActiveAlarmsEntry": sgcActiveAlarmsEntry,
       "sgcActiveAlarmsEntryId": sgcActiveAlarmsEntryId,
       "sgcActiveAlarmsEntryTimestamp": sgcActiveAlarmsEntryTimestamp,
       "sgcActiveAlarmsEntryName": sgcActiveAlarmsEntryName,
       "sgcActiveAlarmsEntrySeverity": sgcActiveAlarmsEntrySeverity,
       "sgcActiveAlarmsEntryInfo": sgcActiveAlarmsEntryInfo,
       "sgcEventHistoryTable": sgcEventHistoryTable,
       "sgcEventHistoryEntry": sgcEventHistoryEntry,
       "sgcEventHistoryEntryIdx": sgcEventHistoryEntryIdx,
       "sgcEventHistoryEntryId": sgcEventHistoryEntryId,
       "sgcEventHistoryEntryName": sgcEventHistoryEntryName,
       "sgcEventHistoryEntryTimestamp": sgcEventHistoryEntryTimestamp,
       "sgcEventHistoryEntrySeverity": sgcEventHistoryEntrySeverity,
       "sgcEventHistoryEntryInfo": sgcEventHistoryEntryInfo,
       "sgcConf": sgcConf,
       "sgcGroups": sgcGroups,
       "sgcBasicGroup": sgcBasicGroup,
       "sgcBasicEvents": sgcBasicEvents,
       "sgcEventObjectsGroup": sgcEventObjectsGroup,
       "sgcCompls": sgcCompls}
)
