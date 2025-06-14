# SNMP MIB module (SIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/SIP-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 15:01:16 2025
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
 iso,
 mib_2,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "transmission")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

sipMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SMDSAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1h:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8



class IfIndex(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Sip_ObjectIdentity = ObjectIdentity
sip = _Sip_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 31)
)
_SipL3Table_Object = MibTable
sipL3Table = _SipL3Table_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 1)
)
if mibBuilder.loadTexts:
    sipL3Table.setStatus("current")
_SipL3Entry_Object = MibTableRow
sipL3Entry = _SipL3Entry_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 1, 1)
)
sipL3Entry.setIndexNames(
    (0, "SIP-MIB", "sipL3Index"),
)
if mibBuilder.loadTexts:
    sipL3Entry.setStatus("current")
_SipL3Index_Type = IfIndex
_SipL3Index_Object = MibTableColumn
sipL3Index = _SipL3Index_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 1),
    _SipL3Index_Type()
)
sipL3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL3Index.setStatus("current")
_SipL3ReceivedIndividualDAs_Type = Counter32
_SipL3ReceivedIndividualDAs_Object = MibTableColumn
sipL3ReceivedIndividualDAs = _SipL3ReceivedIndividualDAs_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 2),
    _SipL3ReceivedIndividualDAs_Type()
)
sipL3ReceivedIndividualDAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL3ReceivedIndividualDAs.setStatus("deprecated")
_SipL3ReceivedGAs_Type = Counter32
_SipL3ReceivedGAs_Object = MibTableColumn
sipL3ReceivedGAs = _SipL3ReceivedGAs_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 3),
    _SipL3ReceivedGAs_Type()
)
sipL3ReceivedGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL3ReceivedGAs.setStatus("deprecated")
_SipL3UnrecognizedIndividualDAs_Type = Counter32
_SipL3UnrecognizedIndividualDAs_Object = MibTableColumn
sipL3UnrecognizedIndividualDAs = _SipL3UnrecognizedIndividualDAs_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 4),
    _SipL3UnrecognizedIndividualDAs_Type()
)
sipL3UnrecognizedIndividualDAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL3UnrecognizedIndividualDAs.setStatus("deprecated")
_SipL3UnrecognizedGAs_Type = Counter32
_SipL3UnrecognizedGAs_Object = MibTableColumn
sipL3UnrecognizedGAs = _SipL3UnrecognizedGAs_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 5),
    _SipL3UnrecognizedGAs_Type()
)
sipL3UnrecognizedGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL3UnrecognizedGAs.setStatus("deprecated")
_SipL3SentIndividualDAs_Type = Counter32
_SipL3SentIndividualDAs_Object = MibTableColumn
sipL3SentIndividualDAs = _SipL3SentIndividualDAs_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 6),
    _SipL3SentIndividualDAs_Type()
)
sipL3SentIndividualDAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL3SentIndividualDAs.setStatus("deprecated")
_SipL3SentGAs_Type = Counter32
_SipL3SentGAs_Object = MibTableColumn
sipL3SentGAs = _SipL3SentGAs_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 7),
    _SipL3SentGAs_Type()
)
sipL3SentGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL3SentGAs.setStatus("deprecated")
_SipL3Errors_Type = Counter32
_SipL3Errors_Object = MibTableColumn
sipL3Errors = _SipL3Errors_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 8),
    _SipL3Errors_Type()
)
sipL3Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL3Errors.setStatus("deprecated")
_SipL3InvalidSMDSAddressTypes_Type = Counter32
_SipL3InvalidSMDSAddressTypes_Object = MibTableColumn
sipL3InvalidSMDSAddressTypes = _SipL3InvalidSMDSAddressTypes_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 9),
    _SipL3InvalidSMDSAddressTypes_Type()
)
sipL3InvalidSMDSAddressTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL3InvalidSMDSAddressTypes.setStatus("deprecated")
_SipL3VersionSupport_Type = Integer32
_SipL3VersionSupport_Object = MibTableColumn
sipL3VersionSupport = _SipL3VersionSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 10),
    _SipL3VersionSupport_Type()
)
sipL3VersionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL3VersionSupport.setStatus("current")
_SipL2Table_Object = MibTable
sipL2Table = _SipL2Table_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 2)
)
if mibBuilder.loadTexts:
    sipL2Table.setStatus("current")
_SipL2Entry_Object = MibTableRow
sipL2Entry = _SipL2Entry_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 2, 1)
)
sipL2Entry.setIndexNames(
    (0, "SIP-MIB", "sipL2Index"),
)
if mibBuilder.loadTexts:
    sipL2Entry.setStatus("current")
_SipL2Index_Type = IfIndex
_SipL2Index_Object = MibTableColumn
sipL2Index = _SipL2Index_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 2, 1, 1),
    _SipL2Index_Type()
)
sipL2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL2Index.setStatus("current")
_SipL2ReceivedCounts_Type = Counter32
_SipL2ReceivedCounts_Object = MibTableColumn
sipL2ReceivedCounts = _SipL2ReceivedCounts_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 2, 1, 2),
    _SipL2ReceivedCounts_Type()
)
sipL2ReceivedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL2ReceivedCounts.setStatus("current")
_SipL2SentCounts_Type = Counter32
_SipL2SentCounts_Object = MibTableColumn
sipL2SentCounts = _SipL2SentCounts_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 2, 1, 3),
    _SipL2SentCounts_Type()
)
sipL2SentCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL2SentCounts.setStatus("current")
_SipL2HcsOrCRCErrors_Type = Counter32
_SipL2HcsOrCRCErrors_Object = MibTableColumn
sipL2HcsOrCRCErrors = _SipL2HcsOrCRCErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 2, 1, 4),
    _SipL2HcsOrCRCErrors_Type()
)
sipL2HcsOrCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL2HcsOrCRCErrors.setStatus("current")
_SipL2PayloadLengthErrors_Type = Counter32
_SipL2PayloadLengthErrors_Object = MibTableColumn
sipL2PayloadLengthErrors = _SipL2PayloadLengthErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 2, 1, 5),
    _SipL2PayloadLengthErrors_Type()
)
sipL2PayloadLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL2PayloadLengthErrors.setStatus("current")
_SipL2SequenceNumberErrors_Type = Counter32
_SipL2SequenceNumberErrors_Object = MibTableColumn
sipL2SequenceNumberErrors = _SipL2SequenceNumberErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 2, 1, 6),
    _SipL2SequenceNumberErrors_Type()
)
sipL2SequenceNumberErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL2SequenceNumberErrors.setStatus("current")
_SipL2MidCurrentlyActiveErrors_Type = Counter32
_SipL2MidCurrentlyActiveErrors_Object = MibTableColumn
sipL2MidCurrentlyActiveErrors = _SipL2MidCurrentlyActiveErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 2, 1, 7),
    _SipL2MidCurrentlyActiveErrors_Type()
)
sipL2MidCurrentlyActiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL2MidCurrentlyActiveErrors.setStatus("current")
_SipL2BomOrSSMsMIDErrors_Type = Counter32
_SipL2BomOrSSMsMIDErrors_Object = MibTableColumn
sipL2BomOrSSMsMIDErrors = _SipL2BomOrSSMsMIDErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 2, 1, 8),
    _SipL2BomOrSSMsMIDErrors_Type()
)
sipL2BomOrSSMsMIDErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL2BomOrSSMsMIDErrors.setStatus("current")
_SipL2EomsMIDErrors_Type = Counter32
_SipL2EomsMIDErrors_Object = MibTableColumn
sipL2EomsMIDErrors = _SipL2EomsMIDErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 2, 1, 9),
    _SipL2EomsMIDErrors_Type()
)
sipL2EomsMIDErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL2EomsMIDErrors.setStatus("current")
_SipPLCP_ObjectIdentity = ObjectIdentity
sipPLCP = _SipPLCP_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 31, 3)
)
_SipDS1PLCPTable_Object = MibTable
sipDS1PLCPTable = _SipDS1PLCPTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 3, 1)
)
if mibBuilder.loadTexts:
    sipDS1PLCPTable.setStatus("current")
_SipDS1PLCPEntry_Object = MibTableRow
sipDS1PLCPEntry = _SipDS1PLCPEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 3, 1, 1)
)
sipDS1PLCPEntry.setIndexNames(
    (0, "SIP-MIB", "sipDS1PLCPIndex"),
)
if mibBuilder.loadTexts:
    sipDS1PLCPEntry.setStatus("current")
_SipDS1PLCPIndex_Type = IfIndex
_SipDS1PLCPIndex_Object = MibTableColumn
sipDS1PLCPIndex = _SipDS1PLCPIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 3, 1, 1, 1),
    _SipDS1PLCPIndex_Type()
)
sipDS1PLCPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipDS1PLCPIndex.setStatus("current")
_SipDS1PLCPSEFSs_Type = Counter32
_SipDS1PLCPSEFSs_Object = MibTableColumn
sipDS1PLCPSEFSs = _SipDS1PLCPSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 3, 1, 1, 2),
    _SipDS1PLCPSEFSs_Type()
)
sipDS1PLCPSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipDS1PLCPSEFSs.setStatus("current")


class _SipDS1PLCPAlarmState_Type(Integer32):
    """Custom type sipDS1PLCPAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 1),
          ("receivedFarEndAlarm", 2),
          ("incomingLOF", 3))
    )


_SipDS1PLCPAlarmState_Type.__name__ = "Integer32"
_SipDS1PLCPAlarmState_Object = MibTableColumn
sipDS1PLCPAlarmState = _SipDS1PLCPAlarmState_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 3, 1, 1, 3),
    _SipDS1PLCPAlarmState_Type()
)
sipDS1PLCPAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipDS1PLCPAlarmState.setStatus("current")
_SipDS1PLCPUASs_Type = Counter32
_SipDS1PLCPUASs_Object = MibTableColumn
sipDS1PLCPUASs = _SipDS1PLCPUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 3, 1, 1, 4),
    _SipDS1PLCPUASs_Type()
)
sipDS1PLCPUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipDS1PLCPUASs.setStatus("current")
_SipDS3PLCPTable_Object = MibTable
sipDS3PLCPTable = _SipDS3PLCPTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 3, 2)
)
if mibBuilder.loadTexts:
    sipDS3PLCPTable.setStatus("current")
_SipDS3PLCPEntry_Object = MibTableRow
sipDS3PLCPEntry = _SipDS3PLCPEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 3, 2, 1)
)
sipDS3PLCPEntry.setIndexNames(
    (0, "SIP-MIB", "sipDS3PLCPIndex"),
)
if mibBuilder.loadTexts:
    sipDS3PLCPEntry.setStatus("current")
_SipDS3PLCPIndex_Type = IfIndex
_SipDS3PLCPIndex_Object = MibTableColumn
sipDS3PLCPIndex = _SipDS3PLCPIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 3, 2, 1, 1),
    _SipDS3PLCPIndex_Type()
)
sipDS3PLCPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipDS3PLCPIndex.setStatus("current")
_SipDS3PLCPSEFSs_Type = Counter32
_SipDS3PLCPSEFSs_Object = MibTableColumn
sipDS3PLCPSEFSs = _SipDS3PLCPSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 3, 2, 1, 2),
    _SipDS3PLCPSEFSs_Type()
)
sipDS3PLCPSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipDS3PLCPSEFSs.setStatus("current")


class _SipDS3PLCPAlarmState_Type(Integer32):
    """Custom type sipDS3PLCPAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 1),
          ("receivedFarEndAlarm", 2),
          ("incomingLOF", 3))
    )


_SipDS3PLCPAlarmState_Type.__name__ = "Integer32"
_SipDS3PLCPAlarmState_Object = MibTableColumn
sipDS3PLCPAlarmState = _SipDS3PLCPAlarmState_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 3, 2, 1, 3),
    _SipDS3PLCPAlarmState_Type()
)
sipDS3PLCPAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipDS3PLCPAlarmState.setStatus("current")
_SipDS3PLCPUASs_Type = Counter32
_SipDS3PLCPUASs_Object = MibTableColumn
sipDS3PLCPUASs = _SipDS3PLCPUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 3, 2, 1, 4),
    _SipDS3PLCPUASs_Type()
)
sipDS3PLCPUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipDS3PLCPUASs.setStatus("current")
_SmdsApplications_ObjectIdentity = ObjectIdentity
smdsApplications = _SmdsApplications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 31, 4)
)
_IpOverSMDS_ObjectIdentity = ObjectIdentity
ipOverSMDS = _IpOverSMDS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 31, 4, 1)
)
_IpOverSMDSTable_Object = MibTable
ipOverSMDSTable = _IpOverSMDSTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ipOverSMDSTable.setStatus("current")
_IpOverSMDSEntry_Object = MibTableRow
ipOverSMDSEntry = _IpOverSMDSEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 4, 1, 1, 1)
)
ipOverSMDSEntry.setIndexNames(
    (0, "SIP-MIB", "ipOverSMDSIndex"),
    (0, "SIP-MIB", "ipOverSMDSAddress"),
)
if mibBuilder.loadTexts:
    ipOverSMDSEntry.setStatus("current")
_IpOverSMDSIndex_Type = IfIndex
_IpOverSMDSIndex_Object = MibTableColumn
ipOverSMDSIndex = _IpOverSMDSIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 4, 1, 1, 1, 1),
    _IpOverSMDSIndex_Type()
)
ipOverSMDSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOverSMDSIndex.setStatus("current")
_IpOverSMDSAddress_Type = IpAddress
_IpOverSMDSAddress_Object = MibTableColumn
ipOverSMDSAddress = _IpOverSMDSAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 4, 1, 1, 1, 2),
    _IpOverSMDSAddress_Type()
)
ipOverSMDSAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOverSMDSAddress.setStatus("current")
_IpOverSMDSHA_Type = SMDSAddress
_IpOverSMDSHA_Object = MibTableColumn
ipOverSMDSHA = _IpOverSMDSHA_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 4, 1, 1, 1, 3),
    _IpOverSMDSHA_Type()
)
ipOverSMDSHA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOverSMDSHA.setStatus("current")
_IpOverSMDSLISGA_Type = SMDSAddress
_IpOverSMDSLISGA_Object = MibTableColumn
ipOverSMDSLISGA = _IpOverSMDSLISGA_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 4, 1, 1, 1, 4),
    _IpOverSMDSLISGA_Type()
)
ipOverSMDSLISGA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOverSMDSLISGA.setStatus("current")
_IpOverSMDSARPReq_Type = SMDSAddress
_IpOverSMDSARPReq_Object = MibTableColumn
ipOverSMDSARPReq = _IpOverSMDSARPReq_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 4, 1, 1, 1, 5),
    _IpOverSMDSARPReq_Type()
)
ipOverSMDSARPReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOverSMDSARPReq.setStatus("current")
_SmdsCarrierSelection_ObjectIdentity = ObjectIdentity
smdsCarrierSelection = _SmdsCarrierSelection_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 31, 5)
)
_SipErrorLog_ObjectIdentity = ObjectIdentity
sipErrorLog = _SipErrorLog_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 31, 6)
)
_SipL3PDUErrorTable_Object = MibTable
sipL3PDUErrorTable = _SipL3PDUErrorTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 6, 1)
)
if mibBuilder.loadTexts:
    sipL3PDUErrorTable.setStatus("current")
_SipL3PDUErrorEntry_Object = MibTableRow
sipL3PDUErrorEntry = _SipL3PDUErrorEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 6, 1, 1)
)
sipL3PDUErrorEntry.setIndexNames(
    (0, "SIP-MIB", "sipL3PDUErrorIndex"),
    (0, "SIP-MIB", "sipL3PDUErrorType"),
)
if mibBuilder.loadTexts:
    sipL3PDUErrorEntry.setStatus("current")
_SipL3PDUErrorIndex_Type = IfIndex
_SipL3PDUErrorIndex_Object = MibTableColumn
sipL3PDUErrorIndex = _SipL3PDUErrorIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 6, 1, 1, 1),
    _SipL3PDUErrorIndex_Type()
)
sipL3PDUErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL3PDUErrorIndex.setStatus("current")


class _SipL3PDUErrorType_Type(Integer32):
    """Custom type sipL3PDUErrorType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("erroredDAFieldFormat", 1),
          ("erroredSAFieldFormat", 2),
          ("invalidBAsizeFieldValue", 3),
          ("invalidHdrExtLength", 4),
          ("invalidHdrExtElementLength", 5),
          ("invalidHdrExtVersionElementPositionLenthOrValue", 6),
          ("invalidHdrExtCarSelectElementPositionLenghtValueOrFormat", 7),
          ("hePADError", 8),
          ("beTagMismatch", 9),
          ("baSizeFieldNotEqualToLengthField", 10),
          ("incorrectLength", 11),
          ("mriTimeout", 12))
    )


_SipL3PDUErrorType_Type.__name__ = "Integer32"
_SipL3PDUErrorType_Object = MibTableColumn
sipL3PDUErrorType = _SipL3PDUErrorType_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 6, 1, 1, 2),
    _SipL3PDUErrorType_Type()
)
sipL3PDUErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL3PDUErrorType.setStatus("current")
_SipL3PDUErrorSA_Type = SMDSAddress
_SipL3PDUErrorSA_Object = MibTableColumn
sipL3PDUErrorSA = _SipL3PDUErrorSA_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 6, 1, 1, 3),
    _SipL3PDUErrorSA_Type()
)
sipL3PDUErrorSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL3PDUErrorSA.setStatus("current")
_SipL3PDUErrorDA_Type = SMDSAddress
_SipL3PDUErrorDA_Object = MibTableColumn
sipL3PDUErrorDA = _SipL3PDUErrorDA_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 6, 1, 1, 4),
    _SipL3PDUErrorDA_Type()
)
sipL3PDUErrorDA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL3PDUErrorDA.setStatus("current")
_SipL3PDUErrorTimeStamp_Type = TimeStamp
_SipL3PDUErrorTimeStamp_Object = MibTableColumn
sipL3PDUErrorTimeStamp = _SipL3PDUErrorTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 10, 31, 6, 1, 1, 5),
    _SipL3PDUErrorTimeStamp_Type()
)
sipL3PDUErrorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipL3PDUErrorTimeStamp.setStatus("current")
_SipMIBObjects_ObjectIdentity = ObjectIdentity
sipMIBObjects = _SipMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 36, 1)
)
_SipDxiTable_Object = MibTable
sipDxiTable = _SipDxiTable_Object(
    (1, 3, 6, 1, 2, 1, 36, 1, 1)
)
if mibBuilder.loadTexts:
    sipDxiTable.setStatus("current")
_SipDxiEntry_Object = MibTableRow
sipDxiEntry = _SipDxiEntry_Object(
    (1, 3, 6, 1, 2, 1, 36, 1, 1, 1)
)
sipDxiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sipDxiEntry.setStatus("current")


class _SipDxiCrc_Type(Integer32):
    """Custom type sipDxiCrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2))
    )


_SipDxiCrc_Type.__name__ = "Integer32"
_SipDxiCrc_Object = MibTableColumn
sipDxiCrc = _SipDxiCrc_Object(
    (1, 3, 6, 1, 2, 1, 36, 1, 1, 1, 1),
    _SipDxiCrc_Type()
)
sipDxiCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipDxiCrc.setStatus("current")
_SipDxiOutDiscards_Type = Counter32
_SipDxiOutDiscards_Object = MibTableColumn
sipDxiOutDiscards = _SipDxiOutDiscards_Object(
    (1, 3, 6, 1, 2, 1, 36, 1, 1, 1, 2),
    _SipDxiOutDiscards_Type()
)
sipDxiOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipDxiOutDiscards.setStatus("current")
_SipDxiInErrors_Type = Counter32
_SipDxiInErrors_Object = MibTableColumn
sipDxiInErrors = _SipDxiInErrors_Object(
    (1, 3, 6, 1, 2, 1, 36, 1, 1, 1, 3),
    _SipDxiInErrors_Type()
)
sipDxiInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipDxiInErrors.setStatus("current")
_SipDxiInAborts_Type = Counter32
_SipDxiInAborts_Object = MibTableColumn
sipDxiInAborts = _SipDxiInAborts_Object(
    (1, 3, 6, 1, 2, 1, 36, 1, 1, 1, 4),
    _SipDxiInAborts_Type()
)
sipDxiInAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipDxiInAborts.setStatus("current")
_SipDxiInTestFrames_Type = Counter32
_SipDxiInTestFrames_Object = MibTableColumn
sipDxiInTestFrames = _SipDxiInTestFrames_Object(
    (1, 3, 6, 1, 2, 1, 36, 1, 1, 1, 5),
    _SipDxiInTestFrames_Type()
)
sipDxiInTestFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipDxiInTestFrames.setStatus("current")
_SipDxiOutTestFrames_Type = Counter32
_SipDxiOutTestFrames_Object = MibTableColumn
sipDxiOutTestFrames = _SipDxiOutTestFrames_Object(
    (1, 3, 6, 1, 2, 1, 36, 1, 1, 1, 6),
    _SipDxiOutTestFrames_Type()
)
sipDxiOutTestFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipDxiOutTestFrames.setStatus("current")
_SipDxiHbpNoAcks_Type = Counter32
_SipDxiHbpNoAcks_Object = MibTableColumn
sipDxiHbpNoAcks = _SipDxiHbpNoAcks_Object(
    (1, 3, 6, 1, 2, 1, 36, 1, 1, 1, 7),
    _SipDxiHbpNoAcks_Type()
)
sipDxiHbpNoAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipDxiHbpNoAcks.setStatus("current")
_SmdsConformance_ObjectIdentity = ObjectIdentity
smdsConformance = _SmdsConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 36, 2)
)
_SmdsGroups_ObjectIdentity = ObjectIdentity
smdsGroups = _SmdsGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 36, 2, 1)
)
_SmdsCompliances_ObjectIdentity = ObjectIdentity
smdsCompliances = _SmdsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 36, 2, 2)
)

# Managed Objects groups

sipLevel3Stuff = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 36, 2, 1, 1)
)
sipLevel3Stuff.setObjects(
      *(("SIP-MIB", "sipL3Index"),
        ("SIP-MIB", "sipL3VersionSupport"),
        ("SIP-MIB", "sipL3PDUErrorIndex"),
        ("SIP-MIB", "sipL3PDUErrorType"),
        ("SIP-MIB", "sipL3PDUErrorSA"),
        ("SIP-MIB", "sipL3PDUErrorDA"),
        ("SIP-MIB", "sipL3PDUErrorTimeStamp"))
)
if mibBuilder.loadTexts:
    sipLevel3Stuff.setStatus("current")

sipLevel2Stuff = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 36, 2, 1, 2)
)
sipLevel2Stuff.setObjects(
      *(("SIP-MIB", "sipL2Index"),
        ("SIP-MIB", "sipL2HcsOrCRCErrors"),
        ("SIP-MIB", "sipL2PayloadLengthErrors"),
        ("SIP-MIB", "sipL2SequenceNumberErrors"),
        ("SIP-MIB", "sipL2MidCurrentlyActiveErrors"),
        ("SIP-MIB", "sipL2BomOrSSMsMIDErrors"),
        ("SIP-MIB", "sipL2EomsMIDErrors"))
)
if mibBuilder.loadTexts:
    sipLevel2Stuff.setStatus("current")

sipDS1PLCPStuff = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 36, 2, 1, 3)
)
sipDS1PLCPStuff.setObjects(
      *(("SIP-MIB", "sipDS1PLCPIndex"),
        ("SIP-MIB", "sipDS1PLCPSEFSs"),
        ("SIP-MIB", "sipDS1PLCPAlarmState"),
        ("SIP-MIB", "sipDS1PLCPUASs"))
)
if mibBuilder.loadTexts:
    sipDS1PLCPStuff.setStatus("current")

sipDS3PLCPStuff = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 36, 2, 1, 4)
)
sipDS3PLCPStuff.setObjects(
      *(("SIP-MIB", "sipDS3PLCPIndex"),
        ("SIP-MIB", "sipDS3PLCPSEFSs"),
        ("SIP-MIB", "sipDS3PLCPAlarmState"),
        ("SIP-MIB", "sipDS3PLCPUASs"))
)
if mibBuilder.loadTexts:
    sipDS3PLCPStuff.setStatus("current")

sipIPApplicationsStuff = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 36, 2, 1, 5)
)
sipIPApplicationsStuff.setObjects(
      *(("SIP-MIB", "ipOverSMDSIndex"),
        ("SIP-MIB", "ipOverSMDSAddress"),
        ("SIP-MIB", "ipOverSMDSHA"),
        ("SIP-MIB", "ipOverSMDSLISGA"),
        ("SIP-MIB", "ipOverSMDSARPReq"))
)
if mibBuilder.loadTexts:
    sipIPApplicationsStuff.setStatus("current")

sipDxiStuff = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 36, 2, 1, 6)
)
sipDxiStuff.setObjects(
      *(("SIP-MIB", "sipDxiCrc"),
        ("SIP-MIB", "sipDxiOutDiscards"),
        ("SIP-MIB", "sipDxiInErrors"),
        ("SIP-MIB", "sipDxiInAborts"),
        ("SIP-MIB", "sipDxiInTestFrames"),
        ("SIP-MIB", "sipDxiOutTestFrames"),
        ("SIP-MIB", "sipDxiHbpNoAcks"))
)
if mibBuilder.loadTexts:
    sipDxiStuff.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

smdsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 36, 2, 2, 1)
)
smdsCompliance.setObjects(
      *(("SIP-MIB", "sipLevel3Stuff"),
        ("SIP-MIB", "sipLevel2Stuff"),
        ("SIP-MIB", "sipDS1PLCPStuff"),
        ("SIP-MIB", "sipDS3PLCPStuff"),
        ("SIP-MIB", "sipIPApplicationsStuff"),
        ("SIP-MIB", "sipDxiStuff"))
)
if mibBuilder.loadTexts:
    smdsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIP-MIB",
    **{"SMDSAddress": SMDSAddress,
       "IfIndex": IfIndex,
       "sip": sip,
       "sipL3Table": sipL3Table,
       "sipL3Entry": sipL3Entry,
       "sipL3Index": sipL3Index,
       "sipL3ReceivedIndividualDAs": sipL3ReceivedIndividualDAs,
       "sipL3ReceivedGAs": sipL3ReceivedGAs,
       "sipL3UnrecognizedIndividualDAs": sipL3UnrecognizedIndividualDAs,
       "sipL3UnrecognizedGAs": sipL3UnrecognizedGAs,
       "sipL3SentIndividualDAs": sipL3SentIndividualDAs,
       "sipL3SentGAs": sipL3SentGAs,
       "sipL3Errors": sipL3Errors,
       "sipL3InvalidSMDSAddressTypes": sipL3InvalidSMDSAddressTypes,
       "sipL3VersionSupport": sipL3VersionSupport,
       "sipL2Table": sipL2Table,
       "sipL2Entry": sipL2Entry,
       "sipL2Index": sipL2Index,
       "sipL2ReceivedCounts": sipL2ReceivedCounts,
       "sipL2SentCounts": sipL2SentCounts,
       "sipL2HcsOrCRCErrors": sipL2HcsOrCRCErrors,
       "sipL2PayloadLengthErrors": sipL2PayloadLengthErrors,
       "sipL2SequenceNumberErrors": sipL2SequenceNumberErrors,
       "sipL2MidCurrentlyActiveErrors": sipL2MidCurrentlyActiveErrors,
       "sipL2BomOrSSMsMIDErrors": sipL2BomOrSSMsMIDErrors,
       "sipL2EomsMIDErrors": sipL2EomsMIDErrors,
       "sipPLCP": sipPLCP,
       "sipDS1PLCPTable": sipDS1PLCPTable,
       "sipDS1PLCPEntry": sipDS1PLCPEntry,
       "sipDS1PLCPIndex": sipDS1PLCPIndex,
       "sipDS1PLCPSEFSs": sipDS1PLCPSEFSs,
       "sipDS1PLCPAlarmState": sipDS1PLCPAlarmState,
       "sipDS1PLCPUASs": sipDS1PLCPUASs,
       "sipDS3PLCPTable": sipDS3PLCPTable,
       "sipDS3PLCPEntry": sipDS3PLCPEntry,
       "sipDS3PLCPIndex": sipDS3PLCPIndex,
       "sipDS3PLCPSEFSs": sipDS3PLCPSEFSs,
       "sipDS3PLCPAlarmState": sipDS3PLCPAlarmState,
       "sipDS3PLCPUASs": sipDS3PLCPUASs,
       "smdsApplications": smdsApplications,
       "ipOverSMDS": ipOverSMDS,
       "ipOverSMDSTable": ipOverSMDSTable,
       "ipOverSMDSEntry": ipOverSMDSEntry,
       "ipOverSMDSIndex": ipOverSMDSIndex,
       "ipOverSMDSAddress": ipOverSMDSAddress,
       "ipOverSMDSHA": ipOverSMDSHA,
       "ipOverSMDSLISGA": ipOverSMDSLISGA,
       "ipOverSMDSARPReq": ipOverSMDSARPReq,
       "smdsCarrierSelection": smdsCarrierSelection,
       "sipErrorLog": sipErrorLog,
       "sipL3PDUErrorTable": sipL3PDUErrorTable,
       "sipL3PDUErrorEntry": sipL3PDUErrorEntry,
       "sipL3PDUErrorIndex": sipL3PDUErrorIndex,
       "sipL3PDUErrorType": sipL3PDUErrorType,
       "sipL3PDUErrorSA": sipL3PDUErrorSA,
       "sipL3PDUErrorDA": sipL3PDUErrorDA,
       "sipL3PDUErrorTimeStamp": sipL3PDUErrorTimeStamp,
       "sipMIB": sipMIB,
       "sipMIBObjects": sipMIBObjects,
       "sipDxiTable": sipDxiTable,
       "sipDxiEntry": sipDxiEntry,
       "sipDxiCrc": sipDxiCrc,
       "sipDxiOutDiscards": sipDxiOutDiscards,
       "sipDxiInErrors": sipDxiInErrors,
       "sipDxiInAborts": sipDxiInAborts,
       "sipDxiInTestFrames": sipDxiInTestFrames,
       "sipDxiOutTestFrames": sipDxiOutTestFrames,
       "sipDxiHbpNoAcks": sipDxiHbpNoAcks,
       "smdsConformance": smdsConformance,
       "smdsGroups": smdsGroups,
       "sipLevel3Stuff": sipLevel3Stuff,
       "sipLevel2Stuff": sipLevel2Stuff,
       "sipDS1PLCPStuff": sipDS1PLCPStuff,
       "sipDS3PLCPStuff": sipDS3PLCPStuff,
       "sipIPApplicationsStuff": sipIPApplicationsStuff,
       "sipDxiStuff": sipDxiStuff,
       "smdsCompliances": smdsCompliances,
       "smdsCompliance": smdsCompliance}
)
