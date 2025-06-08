# SNMP MIB module (WMAN-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/WMAN-IF-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:18:43 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
    "transmission")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

wmanIfMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184)
)
if mibBuilder.loadTexts:
    wmanIfMib.setRevisions(
        ("2005-08-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class WmanIfSfSchedulingType(TextualConvention, Integer32):
    status = "current"
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
        *(("undefined", 1),
          ("bestEffort", 2),
          ("nonRealTimePollingService", 3),
          ("realTimePollingService", 4),
          ("reserved", 5),
          ("unsolicitedGrantService", 6))
    )



class WmanIfPhsRuleVerify(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("phsVerifyEnable", 0),
          ("phsVerifyDisable", 1))
    )



class WmanIfClassifierBitMap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("priority", 0),
          ("ipTos", 1),
          ("ipProtocol", 2),
          ("ipMaskedSrcAddr", 3),
          ("ipMaskedDestAddr", 4),
          ("srcPort", 5),
          ("destPort", 6),
          ("destMacAddr", 7),
          ("srcMacAddr", 8),
          ("ethernetProtocol", 9),
          ("userPriority", 10),
          ("vlanId", 11),
          ("ipv6FlowLabel", 12))
    )


class WmanIfSfState(TextualConvention, Integer32):
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
        *(("authorized", 1),
          ("admitted", 2),
          ("active", 3))
    )



class WmanIfServClassName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )



class WmanIfCsSpecification(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("noCs", 0),
          ("packetIpV4", 1),
          ("packetIpV6", 2),
          ("packet802dot3Ethernet", 3),
          ("packet802dot1QVlan", 4),
          ("packetIpV4Over802dot3", 5),
          ("packetIpV6Over802dot3", 6),
          ("packetIpV4Over802dot1Q", 7),
          ("packetIpV6Over802dot1Q", 8),
          ("atm", 9))
    )



class WmanIfMacVersion(TextualConvention, Integer32):
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
        *(("ieee802Dot16Of2001", 1),
          ("ieee802Dot16cOf2002", 2),
          ("ieee802Dot16aOf2003", 3),
          ("ieee802Dot16Of2004", 4))
    )



class WmanIfCidType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class WmanIfDataEncryptAlgId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("des56BitCbcMode", 1),
          ("aesCcmMode", 2))
    )



class WmanIfDataAuthAlgId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noDataAuthentication", 0),
          ("reserved", 1))
    )



class WmanIfTekEncryptAlgId(TextualConvention, Integer32):
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
        *(("tripleDes128BitKey", 1),
          ("rsa1024BitKey", 2),
          ("aes128BitKey", 3))
    )



class WmanIfChannelNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )



class WmanIfOfdmFecCodeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("bpskCc1Over2", 0),
          ("qpskRsCcCc1Over2", 1),
          ("qpskRsCcCc3Over4", 2),
          ("sixteenQamRsCcCc1Over2", 3),
          ("sixteenQamRsCcCc3Over4", 4),
          ("sixtyFourQamRsCcCc2Over3", 5),
          ("sixtyFourQamRsCcCc3Over4", 6),
          ("qpskBtc1Over2", 7),
          ("qpskBtc3Over4", 8),
          ("sixteenQamBtc3Over4", 9),
          ("sixteenQamBtc4Over5", 10),
          ("sixtyFourQamBtc2Over3", 11),
          ("sixtyFourQamBtc5Over6", 12),
          ("qpskCtc1Over2", 13),
          ("qpskCtc2Over3", 14),
          ("qpskCtc3Over4", 15),
          ("sixteenQamCtc1Over2", 16),
          ("sixteenQamCtc3Over4", 17),
          ("sixtyFourQamCtc2Over3", 18),
          ("sixtyFourQamCtc3Over4", 19))
    )



class WmanIfOfdmaFecCodeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("qpskCc1Over2", 0),
          ("qpskCc3Over4", 1),
          ("sixteenQamCc1Over2", 2),
          ("sixteenQamCc3Over4", 3),
          ("sixtyFourQamCc2Over3", 4),
          ("sixtyFourQamCc3Over4", 5),
          ("qpskBtc1Over2", 6),
          ("qpskBtc2Over3", 7),
          ("sixteenQamBtc3Over5", 8),
          ("sixteenQamBtc4Over5", 9),
          ("sixtyFourQamBtc5Over8", 10),
          ("sixtyFourQamBtc4Over5", 11),
          ("qpskCtc1Over2", 12),
          ("qpskCtc2Over3", 13),
          ("qpskCtc3Over4", 14),
          ("sixteenQamCtc1Over2", 15),
          ("sixteenQamCtc3Over4", 16),
          ("sixtyFourQamCtc2Over3", 17),
          ("sixtyFourQamCtc3Over4", 18),
          ("sixtyFourQamCtc5Over6", 19),
          ("qpskZtCc1Over2", 20),
          ("qpskZtCc3Over4", 21),
          ("sixteenQamZtCc1Over2", 22),
          ("sixteenQamZtCc3Over4", 23),
          ("sixtyFourQamZtCc2Over3", 24),
          ("sixtyFourQamZtCc3Over4", 25))
    )



class WmanIfNumOfUplinkCid(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )



class WmanIfArqSupportType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("arqNotSupported", 0),
          ("arqSupported", 1))
    )



class WmanIfMaxDsxFlowType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class WmanIfMacCrcSupport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noMacCrcSupport", 0),
          ("macCrcSupport", 1))
    )



class WmanIfMaxMcaFlowType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class WmanIfMaxMcpGroupCid(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class WmanIfMaxPkmFlowType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class WmanIfAuthPolicyType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ieee802Dot16PrivacySupported", 0),
          ("reserved1", 1),
          ("reserved2", 2),
          ("reserved3", 3),
          ("reserved4", 4),
          ("reserved5", 5),
          ("reserved6", 6),
          ("reserved7", 7))
    )


class WmanIfMaxNumOfSaType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class WmanIfIpVersionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("ipv4", 1),
          ("ipv6", 2))
    )



class WmanIfMacCsBitMap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("atm", 0),
          ("packetIpv4", 1),
          ("packetIpv6", 2),
          ("packet802Dot3", 3),
          ("packet802Dot1Q", 4),
          ("packetIpv4Over802Dot3", 5),
          ("packetIpv6Over802Dot3", 6),
          ("packetIpv4Over802Dot1Q", 7),
          ("packetIpv6Over802Dot1Q", 8))
    )


class WmanIfMaxClassifiers(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class WmanIfPhsSupportType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPhsSupport", 0),
          ("atmPhsSupport", 1),
          ("packetPhsSupport", 2))
    )



class WmanIfBwAllocSupport(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("reserved", 0),
          ("halfDuplexFdd", 1),
          ("fullDuplexFdd", 2))
    )


class WmanIfPduConstruction(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("piggybackedRequests", 0),
          ("fsnValuesSize", 1))
    )


class WmanIfSsTransitionGap(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class WmanIfMaxTxPowerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class WmanIfOfdmFftSizes(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("fft256", 0),
          ("fft2048", 1))
    )


class WmanIfOfdmSsDeModType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("qam64", 0),
          ("btc", 1),
          ("ctc", 2),
          ("stc", 3),
          ("aac", 4))
    )


class WmanIfOfdmSsModType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("qam64", 0),
          ("btc", 1),
          ("ctc", 2),
          ("subchanellization", 3),
          ("focusedCtBwReq", 4))
    )


class WmanIfOfdmFocusedCt(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("focusedCtSupport", 0)
    )


class WmanIfOfdmTcSublayer(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("tcSublayerSupport", 0)
    )


class WmanIfBsIdType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6



class WmanIfIpv6FlowLabel(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3



# MIB Managed Objects in the order of their OIDs

_WmanIfMibObjects_ObjectIdentity = ObjectIdentity
wmanIfMibObjects = _WmanIfMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1)
)
_WmanIfBsObjects_ObjectIdentity = ObjectIdentity
wmanIfBsObjects = _WmanIfBsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1)
)
_WmanIfBsPacketCs_ObjectIdentity = ObjectIdentity
wmanIfBsPacketCs = _WmanIfBsPacketCs_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1)
)
_WmanIfBsProvisionedSfTable_Object = MibTable
wmanIfBsProvisionedSfTable = _WmanIfBsProvisionedSfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wmanIfBsProvisionedSfTable.setStatus("current")
_WmanIfBsProvisionedSfEntry_Object = MibTableRow
wmanIfBsProvisionedSfEntry = _WmanIfBsProvisionedSfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1, 1)
)
wmanIfBsProvisionedSfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfBsSfId"),
)
if mibBuilder.loadTexts:
    wmanIfBsProvisionedSfEntry.setStatus("current")


class _WmanIfBsSfId_Type(Unsigned32):
    """Custom type wmanIfBsSfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfBsSfId_Type.__name__ = "Unsigned32"
_WmanIfBsSfId_Object = MibTableColumn
wmanIfBsSfId = _WmanIfBsSfId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1, 1, 1),
    _WmanIfBsSfId_Type()
)
wmanIfBsSfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsSfId.setStatus("current")


class _WmanIfBsSfDirection_Type(Integer32):
    """Custom type wmanIfBsSfDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 1),
          ("upstream", 2))
    )


_WmanIfBsSfDirection_Type.__name__ = "Integer32"
_WmanIfBsSfDirection_Object = MibTableColumn
wmanIfBsSfDirection = _WmanIfBsSfDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1, 1, 2),
    _WmanIfBsSfDirection_Type()
)
wmanIfBsSfDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsSfDirection.setStatus("current")


class _WmanIfBsServiceClassIndex_Type(Integer32):
    """Custom type wmanIfBsServiceClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIfBsServiceClassIndex_Type.__name__ = "Integer32"
_WmanIfBsServiceClassIndex_Object = MibTableColumn
wmanIfBsServiceClassIndex = _WmanIfBsServiceClassIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1, 1, 3),
    _WmanIfBsServiceClassIndex_Type()
)
wmanIfBsServiceClassIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsServiceClassIndex.setStatus("current")
_WmanIfBsSfState_Type = WmanIfSfState
_WmanIfBsSfState_Object = MibTableColumn
wmanIfBsSfState = _WmanIfBsSfState_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1, 1, 4),
    _WmanIfBsSfState_Type()
)
wmanIfBsSfState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsSfState.setStatus("current")
_WmanIfBsSfProvisionedTime_Type = TimeStamp
_WmanIfBsSfProvisionedTime_Object = MibTableColumn
wmanIfBsSfProvisionedTime = _WmanIfBsSfProvisionedTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1, 1, 5),
    _WmanIfBsSfProvisionedTime_Type()
)
wmanIfBsSfProvisionedTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsSfProvisionedTime.setStatus("current")
_WmanIfBsSfCsSpecification_Type = WmanIfCsSpecification
_WmanIfBsSfCsSpecification_Object = MibTableColumn
wmanIfBsSfCsSpecification = _WmanIfBsSfCsSpecification_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1, 1, 6),
    _WmanIfBsSfCsSpecification_Type()
)
wmanIfBsSfCsSpecification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsSfCsSpecification.setStatus("current")
_WmanIfBsProvisionedSfRowStatus_Type = RowStatus
_WmanIfBsProvisionedSfRowStatus_Object = MibTableColumn
wmanIfBsProvisionedSfRowStatus = _WmanIfBsProvisionedSfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1, 1, 7),
    _WmanIfBsProvisionedSfRowStatus_Type()
)
wmanIfBsProvisionedSfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsProvisionedSfRowStatus.setStatus("current")
_WmanIfBsSsProvisionedForSfTable_Object = MibTable
wmanIfBsSsProvisionedForSfTable = _WmanIfBsSsProvisionedForSfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wmanIfBsSsProvisionedForSfTable.setStatus("current")
_WmanIfBsSsProvisionedForSfEntry_Object = MibTableRow
wmanIfBsSsProvisionedForSfEntry = _WmanIfBsSsProvisionedForSfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1)
)
wmanIfBsSsProvisionedForSfEntry.setIndexNames(
    (0, "WMAN-IF-MIB", "wmanIfBsSsProvMacAddress"),
    (0, "WMAN-IF-MIB", "wmanIfBsProvSfId"),
)
if mibBuilder.loadTexts:
    wmanIfBsSsProvisionedForSfEntry.setStatus("current")
_WmanIfBsSsProvMacAddress_Type = MacAddress
_WmanIfBsSsProvMacAddress_Object = MibTableColumn
wmanIfBsSsProvMacAddress = _WmanIfBsSsProvMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 1),
    _WmanIfBsSsProvMacAddress_Type()
)
wmanIfBsSsProvMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsSsProvMacAddress.setStatus("current")


class _WmanIfBsProvSfId_Type(Unsigned32):
    """Custom type wmanIfBsProvSfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfBsProvSfId_Type.__name__ = "Unsigned32"
_WmanIfBsProvSfId_Object = MibTableColumn
wmanIfBsProvSfId = _WmanIfBsProvSfId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 2),
    _WmanIfBsProvSfId_Type()
)
wmanIfBsProvSfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsProvSfId.setStatus("current")
_WmanIfBsSsProvisionedForSfRowStatus_Type = RowStatus
_WmanIfBsSsProvisionedForSfRowStatus_Object = MibTableColumn
wmanIfBsSsProvisionedForSfRowStatus = _WmanIfBsSsProvisionedForSfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 3),
    _WmanIfBsSsProvisionedForSfRowStatus_Type()
)
wmanIfBsSsProvisionedForSfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsSsProvisionedForSfRowStatus.setStatus("current")
_WmanIfBsServiceClassTable_Object = MibTable
wmanIfBsServiceClassTable = _WmanIfBsServiceClassTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wmanIfBsServiceClassTable.setStatus("current")
_WmanIfBsServiceClassEntry_Object = MibTableRow
wmanIfBsServiceClassEntry = _WmanIfBsServiceClassEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1)
)
wmanIfBsServiceClassEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfBsQoSProfileIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsServiceClassEntry.setStatus("current")


class _WmanIfBsQoSProfileIndex_Type(Integer32):
    """Custom type wmanIfBsQoSProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIfBsQoSProfileIndex_Type.__name__ = "Integer32"
_WmanIfBsQoSProfileIndex_Object = MibTableColumn
wmanIfBsQoSProfileIndex = _WmanIfBsQoSProfileIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 1),
    _WmanIfBsQoSProfileIndex_Type()
)
wmanIfBsQoSProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsQoSProfileIndex.setStatus("current")
_WmanIfBsQosServiceClassName_Type = WmanIfServClassName
_WmanIfBsQosServiceClassName_Object = MibTableColumn
wmanIfBsQosServiceClassName = _WmanIfBsQosServiceClassName_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 2),
    _WmanIfBsQosServiceClassName_Type()
)
wmanIfBsQosServiceClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosServiceClassName.setStatus("current")


class _WmanIfBsQoSTrafficPriority_Type(Integer32):
    """Custom type wmanIfBsQoSTrafficPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIfBsQoSTrafficPriority_Type.__name__ = "Integer32"
_WmanIfBsQoSTrafficPriority_Object = MibTableColumn
wmanIfBsQoSTrafficPriority = _WmanIfBsQoSTrafficPriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 3),
    _WmanIfBsQoSTrafficPriority_Type()
)
wmanIfBsQoSTrafficPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSTrafficPriority.setStatus("current")
_WmanIfBsQoSMaxSustainedRate_Type = Unsigned32
_WmanIfBsQoSMaxSustainedRate_Object = MibTableColumn
wmanIfBsQoSMaxSustainedRate = _WmanIfBsQoSMaxSustainedRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 4),
    _WmanIfBsQoSMaxSustainedRate_Type()
)
wmanIfBsQoSMaxSustainedRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSMaxSustainedRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQoSMaxSustainedRate.setUnits("b/s")
_WmanIfBsQoSMaxTrafficBurst_Type = Unsigned32
_WmanIfBsQoSMaxTrafficBurst_Object = MibTableColumn
wmanIfBsQoSMaxTrafficBurst = _WmanIfBsQoSMaxTrafficBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 5),
    _WmanIfBsQoSMaxTrafficBurst_Type()
)
wmanIfBsQoSMaxTrafficBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSMaxTrafficBurst.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQoSMaxTrafficBurst.setUnits("byte")
_WmanIfBsQoSMinReservedRate_Type = Unsigned32
_WmanIfBsQoSMinReservedRate_Object = MibTableColumn
wmanIfBsQoSMinReservedRate = _WmanIfBsQoSMinReservedRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 6),
    _WmanIfBsQoSMinReservedRate_Type()
)
wmanIfBsQoSMinReservedRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSMinReservedRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQoSMinReservedRate.setUnits("b/s")
_WmanIfBsQoSToleratedJitter_Type = Unsigned32
_WmanIfBsQoSToleratedJitter_Object = MibTableColumn
wmanIfBsQoSToleratedJitter = _WmanIfBsQoSToleratedJitter_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 7),
    _WmanIfBsQoSToleratedJitter_Type()
)
wmanIfBsQoSToleratedJitter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSToleratedJitter.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQoSToleratedJitter.setUnits("millisecond")
_WmanIfBsQoSMaxLatency_Type = Unsigned32
_WmanIfBsQoSMaxLatency_Object = MibTableColumn
wmanIfBsQoSMaxLatency = _WmanIfBsQoSMaxLatency_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 8),
    _WmanIfBsQoSMaxLatency_Type()
)
wmanIfBsQoSMaxLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQoSMaxLatency.setUnits("millisecond")


class _WmanIfBsQoSFixedVsVariableSduInd_Type(Integer32):
    """Custom type wmanIfBsQoSFixedVsVariableSduInd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("variableLength", 0),
          ("fixedLength", 1))
    )


_WmanIfBsQoSFixedVsVariableSduInd_Type.__name__ = "Integer32"
_WmanIfBsQoSFixedVsVariableSduInd_Object = MibTableColumn
wmanIfBsQoSFixedVsVariableSduInd = _WmanIfBsQoSFixedVsVariableSduInd_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 9),
    _WmanIfBsQoSFixedVsVariableSduInd_Type()
)
wmanIfBsQoSFixedVsVariableSduInd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSFixedVsVariableSduInd.setStatus("current")


class _WmanIfBsQoSSduSize_Type(Unsigned32):
    """Custom type wmanIfBsQoSSduSize based on Unsigned32"""
    defaultValue = 49


_WmanIfBsQoSSduSize_Type.__name__ = "Unsigned32"
_WmanIfBsQoSSduSize_Object = MibTableColumn
wmanIfBsQoSSduSize = _WmanIfBsQoSSduSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 10),
    _WmanIfBsQoSSduSize_Type()
)
wmanIfBsQoSSduSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSSduSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQoSSduSize.setUnits("byte")


class _WmanIfBsQosScSchedulingType_Type(WmanIfSfSchedulingType):
    """Custom type wmanIfBsQosScSchedulingType based on WmanIfSfSchedulingType"""
    defaultValue = 2


_WmanIfBsQosScSchedulingType_Type.__name__ = "WmanIfSfSchedulingType"
_WmanIfBsQosScSchedulingType_Object = MibTableColumn
wmanIfBsQosScSchedulingType = _WmanIfBsQosScSchedulingType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 11),
    _WmanIfBsQosScSchedulingType_Type()
)
wmanIfBsQosScSchedulingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosScSchedulingType.setStatus("current")
_WmanIfBsQosScArqEnable_Type = TruthValue
_WmanIfBsQosScArqEnable_Object = MibTableColumn
wmanIfBsQosScArqEnable = _WmanIfBsQosScArqEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 12),
    _WmanIfBsQosScArqEnable_Type()
)
wmanIfBsQosScArqEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqEnable.setStatus("current")


class _WmanIfBsQosScArqWindowSize_Type(Integer32):
    """Custom type wmanIfBsQosScArqWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WmanIfBsQosScArqWindowSize_Type.__name__ = "Integer32"
_WmanIfBsQosScArqWindowSize_Object = MibTableColumn
wmanIfBsQosScArqWindowSize = _WmanIfBsQosScArqWindowSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 13),
    _WmanIfBsQosScArqWindowSize_Type()
)
wmanIfBsQosScArqWindowSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqWindowSize.setStatus("current")


class _WmanIfBsQosScArqBlockLifetime_Type(Integer32):
    """Custom type wmanIfBsQosScArqBlockLifetime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsQosScArqBlockLifetime_Type.__name__ = "Integer32"
_WmanIfBsQosScArqBlockLifetime_Object = MibTableColumn
wmanIfBsQosScArqBlockLifetime = _WmanIfBsQosScArqBlockLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 14),
    _WmanIfBsQosScArqBlockLifetime_Type()
)
wmanIfBsQosScArqBlockLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqBlockLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqBlockLifetime.setUnits("10 us")


class _WmanIfBsQosScArqSyncLossTimeout_Type(Integer32):
    """Custom type wmanIfBsQosScArqSyncLossTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsQosScArqSyncLossTimeout_Type.__name__ = "Integer32"
_WmanIfBsQosScArqSyncLossTimeout_Object = MibTableColumn
wmanIfBsQosScArqSyncLossTimeout = _WmanIfBsQosScArqSyncLossTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 15),
    _WmanIfBsQosScArqSyncLossTimeout_Type()
)
wmanIfBsQosScArqSyncLossTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqSyncLossTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqSyncLossTimeout.setUnits("10 us")
_WmanIfBsQosScArqDeliverInOrder_Type = TruthValue
_WmanIfBsQosScArqDeliverInOrder_Object = MibTableColumn
wmanIfBsQosScArqDeliverInOrder = _WmanIfBsQosScArqDeliverInOrder_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 16),
    _WmanIfBsQosScArqDeliverInOrder_Type()
)
wmanIfBsQosScArqDeliverInOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqDeliverInOrder.setStatus("current")


class _WmanIfBsQosScArqRxPurgeTimeout_Type(Integer32):
    """Custom type wmanIfBsQosScArqRxPurgeTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsQosScArqRxPurgeTimeout_Type.__name__ = "Integer32"
_WmanIfBsQosScArqRxPurgeTimeout_Object = MibTableColumn
wmanIfBsQosScArqRxPurgeTimeout = _WmanIfBsQosScArqRxPurgeTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 17),
    _WmanIfBsQosScArqRxPurgeTimeout_Type()
)
wmanIfBsQosScArqRxPurgeTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqRxPurgeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqRxPurgeTimeout.setUnits("10 us")


class _WmanIfBsQosScArqBlockSize_Type(Integer32):
    """Custom type wmanIfBsQosScArqBlockSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2040),
    )


_WmanIfBsQosScArqBlockSize_Type.__name__ = "Integer32"
_WmanIfBsQosScArqBlockSize_Object = MibTableColumn
wmanIfBsQosScArqBlockSize = _WmanIfBsQosScArqBlockSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 18),
    _WmanIfBsQosScArqBlockSize_Type()
)
wmanIfBsQosScArqBlockSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqBlockSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqBlockSize.setUnits("byte")
_WmanIfBsQosSCMinRsvdTolerableRate_Type = Unsigned32
_WmanIfBsQosSCMinRsvdTolerableRate_Object = MibTableColumn
wmanIfBsQosSCMinRsvdTolerableRate = _WmanIfBsQosSCMinRsvdTolerableRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 19),
    _WmanIfBsQosSCMinRsvdTolerableRate_Type()
)
wmanIfBsQosSCMinRsvdTolerableRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosSCMinRsvdTolerableRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQosSCMinRsvdTolerableRate.setUnits("b/s")


class _WmanIfBsQoSReqTxPolicy_Type(Bits):
    """Custom type wmanIfBsQoSReqTxPolicy based on Bits"""
    namedValues = NamedValues(
        *(("noBroadcastBwReq", 0),
          ("reserved1", 1),
          ("noPiggybackReq", 2),
          ("noFragmentData", 3),
          ("noPHS", 4),
          ("noSduPacking", 5),
          ("noCrc", 6),
          ("reserved2", 7))
    )

_WmanIfBsQoSReqTxPolicy_Type.__name__ = "Bits"
_WmanIfBsQoSReqTxPolicy_Object = MibTableColumn
wmanIfBsQoSReqTxPolicy = _WmanIfBsQoSReqTxPolicy_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 20),
    _WmanIfBsQoSReqTxPolicy_Type()
)
wmanIfBsQoSReqTxPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSReqTxPolicy.setStatus("current")
_WmanIfBsQoSServiceClassRowStatus_Type = RowStatus
_WmanIfBsQoSServiceClassRowStatus_Object = MibTableColumn
wmanIfBsQoSServiceClassRowStatus = _WmanIfBsQoSServiceClassRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 21),
    _WmanIfBsQoSServiceClassRowStatus_Type()
)
wmanIfBsQoSServiceClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSServiceClassRowStatus.setStatus("current")
_WmanIfBsClassifierRuleTable_Object = MibTable
wmanIfBsClassifierRuleTable = _WmanIfBsClassifierRuleTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleTable.setStatus("current")
_WmanIfBsClassifierRuleEntry_Object = MibTableRow
wmanIfBsClassifierRuleEntry = _WmanIfBsClassifierRuleEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1)
)
wmanIfBsClassifierRuleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfBsSfId"),
    (0, "WMAN-IF-MIB", "wmanIfBsClassifierRuleIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleEntry.setStatus("current")


class _WmanIfBsClassifierRuleIndex_Type(Unsigned32):
    """Custom type wmanIfBsClassifierRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfBsClassifierRuleIndex_Type.__name__ = "Unsigned32"
_WmanIfBsClassifierRuleIndex_Object = MibTableColumn
wmanIfBsClassifierRuleIndex = _WmanIfBsClassifierRuleIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 1),
    _WmanIfBsClassifierRuleIndex_Type()
)
wmanIfBsClassifierRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIndex.setStatus("current")


class _WmanIfBsClassifierRulePriority_Type(Integer32):
    """Custom type wmanIfBsClassifierRulePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsClassifierRulePriority_Type.__name__ = "Integer32"
_WmanIfBsClassifierRulePriority_Object = MibTableColumn
wmanIfBsClassifierRulePriority = _WmanIfBsClassifierRulePriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 2),
    _WmanIfBsClassifierRulePriority_Type()
)
wmanIfBsClassifierRulePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRulePriority.setStatus("current")


class _WmanIfBsClassifierRuleIpTosLow_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleIpTosLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsClassifierRuleIpTosLow_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleIpTosLow_Object = MibTableColumn
wmanIfBsClassifierRuleIpTosLow = _WmanIfBsClassifierRuleIpTosLow_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 3),
    _WmanIfBsClassifierRuleIpTosLow_Type()
)
wmanIfBsClassifierRuleIpTosLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIpTosLow.setStatus("current")


class _WmanIfBsClassifierRuleIpTosHigh_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleIpTosHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsClassifierRuleIpTosHigh_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleIpTosHigh_Object = MibTableColumn
wmanIfBsClassifierRuleIpTosHigh = _WmanIfBsClassifierRuleIpTosHigh_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 4),
    _WmanIfBsClassifierRuleIpTosHigh_Type()
)
wmanIfBsClassifierRuleIpTosHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIpTosHigh.setStatus("current")


class _WmanIfBsClassifierRuleIpTosMask_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleIpTosMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsClassifierRuleIpTosMask_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleIpTosMask_Object = MibTableColumn
wmanIfBsClassifierRuleIpTosMask = _WmanIfBsClassifierRuleIpTosMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 5),
    _WmanIfBsClassifierRuleIpTosMask_Type()
)
wmanIfBsClassifierRuleIpTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIpTosMask.setStatus("current")


class _WmanIfBsClassifierRuleIpProtocol_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsClassifierRuleIpProtocol_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleIpProtocol_Object = MibTableColumn
wmanIfBsClassifierRuleIpProtocol = _WmanIfBsClassifierRuleIpProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 6),
    _WmanIfBsClassifierRuleIpProtocol_Type()
)
wmanIfBsClassifierRuleIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIpProtocol.setStatus("current")
_WmanIfBsClassifierRuleIpSourceAddr_Type = InetAddress
_WmanIfBsClassifierRuleIpSourceAddr_Object = MibTableColumn
wmanIfBsClassifierRuleIpSourceAddr = _WmanIfBsClassifierRuleIpSourceAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 7),
    _WmanIfBsClassifierRuleIpSourceAddr_Type()
)
wmanIfBsClassifierRuleIpSourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIpSourceAddr.setStatus("current")
_WmanIfBsClassifierRuleIpSourceMask_Type = InetAddress
_WmanIfBsClassifierRuleIpSourceMask_Object = MibTableColumn
wmanIfBsClassifierRuleIpSourceMask = _WmanIfBsClassifierRuleIpSourceMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 8),
    _WmanIfBsClassifierRuleIpSourceMask_Type()
)
wmanIfBsClassifierRuleIpSourceMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIpSourceMask.setStatus("current")
_WmanIfBsClassifierRuleIpDestAddr_Type = InetAddress
_WmanIfBsClassifierRuleIpDestAddr_Object = MibTableColumn
wmanIfBsClassifierRuleIpDestAddr = _WmanIfBsClassifierRuleIpDestAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 9),
    _WmanIfBsClassifierRuleIpDestAddr_Type()
)
wmanIfBsClassifierRuleIpDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIpDestAddr.setStatus("current")
_WmanIfBsClassifierRuleIpDestMask_Type = InetAddress
_WmanIfBsClassifierRuleIpDestMask_Object = MibTableColumn
wmanIfBsClassifierRuleIpDestMask = _WmanIfBsClassifierRuleIpDestMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 10),
    _WmanIfBsClassifierRuleIpDestMask_Type()
)
wmanIfBsClassifierRuleIpDestMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIpDestMask.setStatus("current")


class _WmanIfBsClassifierRuleSourcePortStart_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleSourcePortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsClassifierRuleSourcePortStart_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleSourcePortStart_Object = MibTableColumn
wmanIfBsClassifierRuleSourcePortStart = _WmanIfBsClassifierRuleSourcePortStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 11),
    _WmanIfBsClassifierRuleSourcePortStart_Type()
)
wmanIfBsClassifierRuleSourcePortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleSourcePortStart.setStatus("current")


class _WmanIfBsClassifierRuleSourcePortEnd_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleSourcePortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsClassifierRuleSourcePortEnd_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleSourcePortEnd_Object = MibTableColumn
wmanIfBsClassifierRuleSourcePortEnd = _WmanIfBsClassifierRuleSourcePortEnd_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 12),
    _WmanIfBsClassifierRuleSourcePortEnd_Type()
)
wmanIfBsClassifierRuleSourcePortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleSourcePortEnd.setStatus("current")


class _WmanIfBsClassifierRuleDestPortStart_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleDestPortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsClassifierRuleDestPortStart_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleDestPortStart_Object = MibTableColumn
wmanIfBsClassifierRuleDestPortStart = _WmanIfBsClassifierRuleDestPortStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 13),
    _WmanIfBsClassifierRuleDestPortStart_Type()
)
wmanIfBsClassifierRuleDestPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleDestPortStart.setStatus("current")


class _WmanIfBsClassifierRuleDestPortEnd_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleDestPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsClassifierRuleDestPortEnd_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleDestPortEnd_Object = MibTableColumn
wmanIfBsClassifierRuleDestPortEnd = _WmanIfBsClassifierRuleDestPortEnd_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 14),
    _WmanIfBsClassifierRuleDestPortEnd_Type()
)
wmanIfBsClassifierRuleDestPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleDestPortEnd.setStatus("current")
_WmanIfBsClassifierRuleDestMacAddr_Type = MacAddress
_WmanIfBsClassifierRuleDestMacAddr_Object = MibTableColumn
wmanIfBsClassifierRuleDestMacAddr = _WmanIfBsClassifierRuleDestMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 15),
    _WmanIfBsClassifierRuleDestMacAddr_Type()
)
wmanIfBsClassifierRuleDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleDestMacAddr.setStatus("current")
_WmanIfBsClassifierRuleDestMacMask_Type = MacAddress
_WmanIfBsClassifierRuleDestMacMask_Object = MibTableColumn
wmanIfBsClassifierRuleDestMacMask = _WmanIfBsClassifierRuleDestMacMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 16),
    _WmanIfBsClassifierRuleDestMacMask_Type()
)
wmanIfBsClassifierRuleDestMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleDestMacMask.setStatus("current")
_WmanIfBsClassifierRuleSourceMacAddr_Type = MacAddress
_WmanIfBsClassifierRuleSourceMacAddr_Object = MibTableColumn
wmanIfBsClassifierRuleSourceMacAddr = _WmanIfBsClassifierRuleSourceMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 17),
    _WmanIfBsClassifierRuleSourceMacAddr_Type()
)
wmanIfBsClassifierRuleSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleSourceMacAddr.setStatus("current")
_WmanIfBsClassifierRuleSourceMacMask_Type = MacAddress
_WmanIfBsClassifierRuleSourceMacMask_Object = MibTableColumn
wmanIfBsClassifierRuleSourceMacMask = _WmanIfBsClassifierRuleSourceMacMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 18),
    _WmanIfBsClassifierRuleSourceMacMask_Type()
)
wmanIfBsClassifierRuleSourceMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleSourceMacMask.setStatus("current")


class _WmanIfBsClassifierRuleEnetProtocolType_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleEnetProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ethertype", 1),
          ("dsap", 2))
    )


_WmanIfBsClassifierRuleEnetProtocolType_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleEnetProtocolType_Object = MibTableColumn
wmanIfBsClassifierRuleEnetProtocolType = _WmanIfBsClassifierRuleEnetProtocolType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 19),
    _WmanIfBsClassifierRuleEnetProtocolType_Type()
)
wmanIfBsClassifierRuleEnetProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleEnetProtocolType.setStatus("current")


class _WmanIfBsClassifierRuleEnetProtocol_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleEnetProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsClassifierRuleEnetProtocol_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleEnetProtocol_Object = MibTableColumn
wmanIfBsClassifierRuleEnetProtocol = _WmanIfBsClassifierRuleEnetProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 20),
    _WmanIfBsClassifierRuleEnetProtocol_Type()
)
wmanIfBsClassifierRuleEnetProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleEnetProtocol.setStatus("current")


class _WmanIfBsClassifierRuleUserPriLow_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleUserPriLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIfBsClassifierRuleUserPriLow_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleUserPriLow_Object = MibTableColumn
wmanIfBsClassifierRuleUserPriLow = _WmanIfBsClassifierRuleUserPriLow_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 21),
    _WmanIfBsClassifierRuleUserPriLow_Type()
)
wmanIfBsClassifierRuleUserPriLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleUserPriLow.setStatus("current")


class _WmanIfBsClassifierRuleUserPriHigh_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleUserPriHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIfBsClassifierRuleUserPriHigh_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleUserPriHigh_Object = MibTableColumn
wmanIfBsClassifierRuleUserPriHigh = _WmanIfBsClassifierRuleUserPriHigh_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 22),
    _WmanIfBsClassifierRuleUserPriHigh_Type()
)
wmanIfBsClassifierRuleUserPriHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleUserPriHigh.setStatus("current")


class _WmanIfBsClassifierRuleVlanId_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WmanIfBsClassifierRuleVlanId_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleVlanId_Object = MibTableColumn
wmanIfBsClassifierRuleVlanId = _WmanIfBsClassifierRuleVlanId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 23),
    _WmanIfBsClassifierRuleVlanId_Type()
)
wmanIfBsClassifierRuleVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleVlanId.setStatus("current")


class _WmanIfBsClassifierRuleState_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleState based on Integer32"""
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


_WmanIfBsClassifierRuleState_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleState_Object = MibTableColumn
wmanIfBsClassifierRuleState = _WmanIfBsClassifierRuleState_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 24),
    _WmanIfBsClassifierRuleState_Type()
)
wmanIfBsClassifierRuleState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleState.setStatus("current")


class _WmanIfBsClassifierRulePhsSize_Type(Integer32):
    """Custom type wmanIfBsClassifierRulePhsSize based on Integer32"""
    defaultValue = 0


_WmanIfBsClassifierRulePhsSize_Type.__name__ = "Integer32"
_WmanIfBsClassifierRulePhsSize_Object = MibTableColumn
wmanIfBsClassifierRulePhsSize = _WmanIfBsClassifierRulePhsSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 25),
    _WmanIfBsClassifierRulePhsSize_Type()
)
wmanIfBsClassifierRulePhsSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRulePhsSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRulePhsSize.setUnits("byte")


class _WmanIfBsClassifierRulePhsMask_Type(OctetString):
    """Custom type wmanIfBsClassifierRulePhsMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_WmanIfBsClassifierRulePhsMask_Type.__name__ = "OctetString"
_WmanIfBsClassifierRulePhsMask_Object = MibTableColumn
wmanIfBsClassifierRulePhsMask = _WmanIfBsClassifierRulePhsMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 26),
    _WmanIfBsClassifierRulePhsMask_Type()
)
wmanIfBsClassifierRulePhsMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRulePhsMask.setStatus("current")


class _WmanIfBsClassifierRulePhsVerify_Type(WmanIfPhsRuleVerify):
    """Custom type wmanIfBsClassifierRulePhsVerify based on WmanIfPhsRuleVerify"""
    defaultValue = 0


_WmanIfBsClassifierRulePhsVerify_Type.__name__ = "WmanIfPhsRuleVerify"
_WmanIfBsClassifierRulePhsVerify_Object = MibTableColumn
wmanIfBsClassifierRulePhsVerify = _WmanIfBsClassifierRulePhsVerify_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 27),
    _WmanIfBsClassifierRulePhsVerify_Type()
)
wmanIfBsClassifierRulePhsVerify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRulePhsVerify.setStatus("current")
_WmanIfBsClassifierRuleIpv6FlowLabel_Type = WmanIfIpv6FlowLabel
_WmanIfBsClassifierRuleIpv6FlowLabel_Object = MibTableColumn
wmanIfBsClassifierRuleIpv6FlowLabel = _WmanIfBsClassifierRuleIpv6FlowLabel_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 28),
    _WmanIfBsClassifierRuleIpv6FlowLabel_Type()
)
wmanIfBsClassifierRuleIpv6FlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIpv6FlowLabel.setStatus("current")
_WmanIfBsClassifierRuleBitMap_Type = WmanIfClassifierBitMap
_WmanIfBsClassifierRuleBitMap_Object = MibTableColumn
wmanIfBsClassifierRuleBitMap = _WmanIfBsClassifierRuleBitMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 29),
    _WmanIfBsClassifierRuleBitMap_Type()
)
wmanIfBsClassifierRuleBitMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleBitMap.setStatus("current")
_WmanIfBsClassifierRuleRowStatus_Type = RowStatus
_WmanIfBsClassifierRuleRowStatus_Object = MibTableColumn
wmanIfBsClassifierRuleRowStatus = _WmanIfBsClassifierRuleRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 30),
    _WmanIfBsClassifierRuleRowStatus_Type()
)
wmanIfBsClassifierRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleRowStatus.setStatus("current")
_WmanIfBsSsPacketCounterTable_Object = MibTable
wmanIfBsSsPacketCounterTable = _WmanIfBsSsPacketCounterTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wmanIfBsSsPacketCounterTable.setStatus("current")
_WmanIfBsSsPacketCounterEntry_Object = MibTableRow
wmanIfBsSsPacketCounterEntry = _WmanIfBsSsPacketCounterEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 5, 1)
)
wmanIfBsSsPacketCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfCmnCpsSfMacAddress"),
    (0, "WMAN-IF-MIB", "wmanIfCmnCpsSfId"),
)
if mibBuilder.loadTexts:
    wmanIfBsSsPacketCounterEntry.setStatus("current")
_WmanIfBsSsMacSduCount_Type = Counter64
_WmanIfBsSsMacSduCount_Object = MibTableColumn
wmanIfBsSsMacSduCount = _WmanIfBsSsMacSduCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 5, 1, 1),
    _WmanIfBsSsMacSduCount_Type()
)
wmanIfBsSsMacSduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsMacSduCount.setStatus("current")
_WmanIfBsSsOctetCount_Type = Counter64
_WmanIfBsSsOctetCount_Object = MibTableColumn
wmanIfBsSsOctetCount = _WmanIfBsSsOctetCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 5, 1, 2),
    _WmanIfBsSsOctetCount_Type()
)
wmanIfBsSsOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsOctetCount.setStatus("current")


class _WmanIfBsSsResetCounter_Type(Integer32):
    """Custom type wmanIfBsSsResetCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("resetCounter", 1))
    )


_WmanIfBsSsResetCounter_Type.__name__ = "Integer32"
_WmanIfBsSsResetCounter_Object = MibTableColumn
wmanIfBsSsResetCounter = _WmanIfBsSsResetCounter_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 5, 1, 3),
    _WmanIfBsSsResetCounter_Type()
)
wmanIfBsSsResetCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsSsResetCounter.setStatus("current")
_WmanIfBsSsResetCounterTime_Type = TimeStamp
_WmanIfBsSsResetCounterTime_Object = MibTableColumn
wmanIfBsSsResetCounterTime = _WmanIfBsSsResetCounterTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 5, 1, 4),
    _WmanIfBsSsResetCounterTime_Type()
)
wmanIfBsSsResetCounterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsResetCounterTime.setStatus("current")
_WmanIfBsCps_ObjectIdentity = ObjectIdentity
wmanIfBsCps = _WmanIfBsCps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2)
)
_WmanIfBsRegisteredSsTable_Object = MibTable
wmanIfBsRegisteredSsTable = _WmanIfBsRegisteredSsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIfBsRegisteredSsTable.setStatus("current")
_WmanIfBsRegisteredSsEntry_Object = MibTableRow
wmanIfBsRegisteredSsEntry = _WmanIfBsRegisteredSsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1)
)
wmanIfBsRegisteredSsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfBsSsMacAddress"),
)
if mibBuilder.loadTexts:
    wmanIfBsRegisteredSsEntry.setStatus("current")
_WmanIfBsSsMacAddress_Type = MacAddress
_WmanIfBsSsMacAddress_Object = MibTableColumn
wmanIfBsSsMacAddress = _WmanIfBsSsMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 1),
    _WmanIfBsSsMacAddress_Type()
)
wmanIfBsSsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsSsMacAddress.setStatus("current")
_WmanIfBsSsBasicCid_Type = WmanIfCidType
_WmanIfBsSsBasicCid_Object = MibTableColumn
wmanIfBsSsBasicCid = _WmanIfBsSsBasicCid_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 2),
    _WmanIfBsSsBasicCid_Type()
)
wmanIfBsSsBasicCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsBasicCid.setStatus("current")
_WmanIfBsSsPrimaryCid_Type = WmanIfCidType
_WmanIfBsSsPrimaryCid_Object = MibTableColumn
wmanIfBsSsPrimaryCid = _WmanIfBsSsPrimaryCid_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 3),
    _WmanIfBsSsPrimaryCid_Type()
)
wmanIfBsSsPrimaryCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPrimaryCid.setStatus("current")
_WmanIfBsSsSecondaryCid_Type = WmanIfCidType
_WmanIfBsSsSecondaryCid_Object = MibTableColumn
wmanIfBsSsSecondaryCid = _WmanIfBsSsSecondaryCid_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 4),
    _WmanIfBsSsSecondaryCid_Type()
)
wmanIfBsSsSecondaryCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsSecondaryCid.setStatus("current")


class _WmanIfBsSsManagementSupport_Type(Integer32):
    """Custom type wmanIfBsSsManagementSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unmanagedSs", 0),
          ("managedSs", 1))
    )


_WmanIfBsSsManagementSupport_Type.__name__ = "Integer32"
_WmanIfBsSsManagementSupport_Object = MibTableColumn
wmanIfBsSsManagementSupport = _WmanIfBsSsManagementSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 5),
    _WmanIfBsSsManagementSupport_Type()
)
wmanIfBsSsManagementSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsManagementSupport.setStatus("current")


class _WmanIfBsSsIpManagementMode_Type(Integer32):
    """Custom type wmanIfBsSsIpManagementMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unmanaged", 0),
          ("ipManaged", 1))
    )


_WmanIfBsSsIpManagementMode_Type.__name__ = "Integer32"
_WmanIfBsSsIpManagementMode_Object = MibTableColumn
wmanIfBsSsIpManagementMode = _WmanIfBsSsIpManagementMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 6),
    _WmanIfBsSsIpManagementMode_Type()
)
wmanIfBsSsIpManagementMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsIpManagementMode.setStatus("current")
_WmanIfBsSs2ndMgmtArqEnable_Type = TruthValue
_WmanIfBsSs2ndMgmtArqEnable_Object = MibTableColumn
wmanIfBsSs2ndMgmtArqEnable = _WmanIfBsSs2ndMgmtArqEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 7),
    _WmanIfBsSs2ndMgmtArqEnable_Type()
)
wmanIfBsSs2ndMgmtArqEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqEnable.setStatus("current")


class _WmanIfBsSs2ndMgmtArqWindowSize_Type(Integer32):
    """Custom type wmanIfBsSs2ndMgmtArqWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WmanIfBsSs2ndMgmtArqWindowSize_Type.__name__ = "Integer32"
_WmanIfBsSs2ndMgmtArqWindowSize_Object = MibTableColumn
wmanIfBsSs2ndMgmtArqWindowSize = _WmanIfBsSs2ndMgmtArqWindowSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 8),
    _WmanIfBsSs2ndMgmtArqWindowSize_Type()
)
wmanIfBsSs2ndMgmtArqWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqWindowSize.setStatus("current")


class _WmanIfBsSs2ndMgmtArqDnLinkTxDelay_Type(Integer32):
    """Custom type wmanIfBsSs2ndMgmtArqDnLinkTxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsSs2ndMgmtArqDnLinkTxDelay_Type.__name__ = "Integer32"
_WmanIfBsSs2ndMgmtArqDnLinkTxDelay_Object = MibTableColumn
wmanIfBsSs2ndMgmtArqDnLinkTxDelay = _WmanIfBsSs2ndMgmtArqDnLinkTxDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 9),
    _WmanIfBsSs2ndMgmtArqDnLinkTxDelay_Type()
)
wmanIfBsSs2ndMgmtArqDnLinkTxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqDnLinkTxDelay.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqDnLinkTxDelay.setUnits("us")


class _WmanIfBsSs2ndMgmtArqUpLinkTxDelay_Type(Integer32):
    """Custom type wmanIfBsSs2ndMgmtArqUpLinkTxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsSs2ndMgmtArqUpLinkTxDelay_Type.__name__ = "Integer32"
_WmanIfBsSs2ndMgmtArqUpLinkTxDelay_Object = MibTableColumn
wmanIfBsSs2ndMgmtArqUpLinkTxDelay = _WmanIfBsSs2ndMgmtArqUpLinkTxDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 10),
    _WmanIfBsSs2ndMgmtArqUpLinkTxDelay_Type()
)
wmanIfBsSs2ndMgmtArqUpLinkTxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqUpLinkTxDelay.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqUpLinkTxDelay.setUnits("us")


class _WmanIfBsSs2ndMgmtArqDnLinkRxDelay_Type(Integer32):
    """Custom type wmanIfBsSs2ndMgmtArqDnLinkRxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsSs2ndMgmtArqDnLinkRxDelay_Type.__name__ = "Integer32"
_WmanIfBsSs2ndMgmtArqDnLinkRxDelay_Object = MibTableColumn
wmanIfBsSs2ndMgmtArqDnLinkRxDelay = _WmanIfBsSs2ndMgmtArqDnLinkRxDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 11),
    _WmanIfBsSs2ndMgmtArqDnLinkRxDelay_Type()
)
wmanIfBsSs2ndMgmtArqDnLinkRxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqDnLinkRxDelay.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqDnLinkRxDelay.setUnits("us")


class _WmanIfBsSs2ndMgmtArqUpLinkRxDelay_Type(Integer32):
    """Custom type wmanIfBsSs2ndMgmtArqUpLinkRxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsSs2ndMgmtArqUpLinkRxDelay_Type.__name__ = "Integer32"
_WmanIfBsSs2ndMgmtArqUpLinkRxDelay_Object = MibTableColumn
wmanIfBsSs2ndMgmtArqUpLinkRxDelay = _WmanIfBsSs2ndMgmtArqUpLinkRxDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 12),
    _WmanIfBsSs2ndMgmtArqUpLinkRxDelay_Type()
)
wmanIfBsSs2ndMgmtArqUpLinkRxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqUpLinkRxDelay.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqUpLinkRxDelay.setUnits("us")


class _WmanIfBsSs2ndMgmtArqBlockLifetime_Type(Integer32):
    """Custom type wmanIfBsSs2ndMgmtArqBlockLifetime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsSs2ndMgmtArqBlockLifetime_Type.__name__ = "Integer32"
_WmanIfBsSs2ndMgmtArqBlockLifetime_Object = MibTableColumn
wmanIfBsSs2ndMgmtArqBlockLifetime = _WmanIfBsSs2ndMgmtArqBlockLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 13),
    _WmanIfBsSs2ndMgmtArqBlockLifetime_Type()
)
wmanIfBsSs2ndMgmtArqBlockLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqBlockLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqBlockLifetime.setUnits("10 us")


class _WmanIfBsSs2ndMgmtArqSyncLossTimeout_Type(Integer32):
    """Custom type wmanIfBsSs2ndMgmtArqSyncLossTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsSs2ndMgmtArqSyncLossTimeout_Type.__name__ = "Integer32"
_WmanIfBsSs2ndMgmtArqSyncLossTimeout_Object = MibTableColumn
wmanIfBsSs2ndMgmtArqSyncLossTimeout = _WmanIfBsSs2ndMgmtArqSyncLossTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 14),
    _WmanIfBsSs2ndMgmtArqSyncLossTimeout_Type()
)
wmanIfBsSs2ndMgmtArqSyncLossTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqSyncLossTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqSyncLossTimeout.setUnits("10 us")
_WmanIfBsSs2ndMgmtArqDeliverInOrder_Type = TruthValue
_WmanIfBsSs2ndMgmtArqDeliverInOrder_Object = MibTableColumn
wmanIfBsSs2ndMgmtArqDeliverInOrder = _WmanIfBsSs2ndMgmtArqDeliverInOrder_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 15),
    _WmanIfBsSs2ndMgmtArqDeliverInOrder_Type()
)
wmanIfBsSs2ndMgmtArqDeliverInOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqDeliverInOrder.setStatus("current")


class _WmanIfBsSs2ndMgmtArqRxPurgeTimeout_Type(Integer32):
    """Custom type wmanIfBsSs2ndMgmtArqRxPurgeTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsSs2ndMgmtArqRxPurgeTimeout_Type.__name__ = "Integer32"
_WmanIfBsSs2ndMgmtArqRxPurgeTimeout_Object = MibTableColumn
wmanIfBsSs2ndMgmtArqRxPurgeTimeout = _WmanIfBsSs2ndMgmtArqRxPurgeTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 16),
    _WmanIfBsSs2ndMgmtArqRxPurgeTimeout_Type()
)
wmanIfBsSs2ndMgmtArqRxPurgeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqRxPurgeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqRxPurgeTimeout.setUnits("10 us")


class _WmanIfBsSs2ndMgmtArqBlockSize_Type(Integer32):
    """Custom type wmanIfBsSs2ndMgmtArqBlockSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2040),
    )


_WmanIfBsSs2ndMgmtArqBlockSize_Type.__name__ = "Integer32"
_WmanIfBsSs2ndMgmtArqBlockSize_Object = MibTableColumn
wmanIfBsSs2ndMgmtArqBlockSize = _WmanIfBsSs2ndMgmtArqBlockSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 17),
    _WmanIfBsSs2ndMgmtArqBlockSize_Type()
)
wmanIfBsSs2ndMgmtArqBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqBlockSize.setStatus("current")


class _WmanIfBsSsVendorIdEncoding_Type(OctetString):
    """Custom type wmanIfBsSsVendorIdEncoding based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_WmanIfBsSsVendorIdEncoding_Type.__name__ = "OctetString"
_WmanIfBsSsVendorIdEncoding_Object = MibTableColumn
wmanIfBsSsVendorIdEncoding = _WmanIfBsSsVendorIdEncoding_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 18),
    _WmanIfBsSsVendorIdEncoding_Type()
)
wmanIfBsSsVendorIdEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsVendorIdEncoding.setStatus("current")


class _WmanIfBsSsAasBroadcastPermission_Type(Integer32):
    """Custom type wmanIfBsSsAasBroadcastPermission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("contBasedBwReqPermitted", 0),
          ("contBasedBwReqNotPermitted", 1))
    )


_WmanIfBsSsAasBroadcastPermission_Type.__name__ = "Integer32"
_WmanIfBsSsAasBroadcastPermission_Object = MibTableColumn
wmanIfBsSsAasBroadcastPermission = _WmanIfBsSsAasBroadcastPermission_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 19),
    _WmanIfBsSsAasBroadcastPermission_Type()
)
wmanIfBsSsAasBroadcastPermission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsAasBroadcastPermission.setStatus("current")
_WmanIfBsSsMaxTxPowerBpsk_Type = WmanIfMaxTxPowerType
_WmanIfBsSsMaxTxPowerBpsk_Object = MibTableColumn
wmanIfBsSsMaxTxPowerBpsk = _WmanIfBsSsMaxTxPowerBpsk_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 20),
    _WmanIfBsSsMaxTxPowerBpsk_Type()
)
wmanIfBsSsMaxTxPowerBpsk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsMaxTxPowerBpsk.setStatus("current")
_WmanIfBsSsMaxTxPowerQpsk_Type = WmanIfMaxTxPowerType
_WmanIfBsSsMaxTxPowerQpsk_Object = MibTableColumn
wmanIfBsSsMaxTxPowerQpsk = _WmanIfBsSsMaxTxPowerQpsk_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 21),
    _WmanIfBsSsMaxTxPowerQpsk_Type()
)
wmanIfBsSsMaxTxPowerQpsk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsMaxTxPowerQpsk.setStatus("current")
_WmanIfBsSsMaxTxPower16Qam_Type = WmanIfMaxTxPowerType
_WmanIfBsSsMaxTxPower16Qam_Object = MibTableColumn
wmanIfBsSsMaxTxPower16Qam = _WmanIfBsSsMaxTxPower16Qam_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 22),
    _WmanIfBsSsMaxTxPower16Qam_Type()
)
wmanIfBsSsMaxTxPower16Qam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsMaxTxPower16Qam.setStatus("current")
_WmanIfBsSsMaxTxPower64Qam_Type = WmanIfMaxTxPowerType
_WmanIfBsSsMaxTxPower64Qam_Object = MibTableColumn
wmanIfBsSsMaxTxPower64Qam = _WmanIfBsSsMaxTxPower64Qam_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 23),
    _WmanIfBsSsMaxTxPower64Qam_Type()
)
wmanIfBsSsMaxTxPower64Qam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsMaxTxPower64Qam.setStatus("current")
_WmanIfBsSsMacVersion_Type = WmanIfMacVersion
_WmanIfBsSsMacVersion_Object = MibTableColumn
wmanIfBsSsMacVersion = _WmanIfBsSsMacVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 24),
    _WmanIfBsSsMacVersion_Type()
)
wmanIfBsSsMacVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsMacVersion.setStatus("current")
_WmanIfBsConfigurationTable_Object = MibTable
wmanIfBsConfigurationTable = _WmanIfBsConfigurationTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wmanIfBsConfigurationTable.setStatus("current")
_WmanIfBsConfigurationEntry_Object = MibTableRow
wmanIfBsConfigurationEntry = _WmanIfBsConfigurationEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1)
)
wmanIfBsConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsConfigurationEntry.setStatus("current")


class _WmanIfBsDcdInterval_Type(Integer32):
    """Custom type wmanIfBsDcdInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WmanIfBsDcdInterval_Type.__name__ = "Integer32"
_WmanIfBsDcdInterval_Object = MibTableColumn
wmanIfBsDcdInterval = _WmanIfBsDcdInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 1),
    _WmanIfBsDcdInterval_Type()
)
wmanIfBsDcdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsDcdInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsDcdInterval.setUnits("milliseconds")


class _WmanIfBsUcdInterval_Type(Integer32):
    """Custom type wmanIfBsUcdInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WmanIfBsUcdInterval_Type.__name__ = "Integer32"
_WmanIfBsUcdInterval_Object = MibTableColumn
wmanIfBsUcdInterval = _WmanIfBsUcdInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 2),
    _WmanIfBsUcdInterval_Type()
)
wmanIfBsUcdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsUcdInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsUcdInterval.setUnits("milliseconds")


class _WmanIfBsUcdTransition_Type(Integer32):
    """Custom type wmanIfBsUcdTransition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_WmanIfBsUcdTransition_Type.__name__ = "Integer32"
_WmanIfBsUcdTransition_Object = MibTableColumn
wmanIfBsUcdTransition = _WmanIfBsUcdTransition_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 3),
    _WmanIfBsUcdTransition_Type()
)
wmanIfBsUcdTransition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsUcdTransition.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsUcdTransition.setUnits("Number of MAC Frames")


class _WmanIfBsDcdTransition_Type(Integer32):
    """Custom type wmanIfBsDcdTransition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_WmanIfBsDcdTransition_Type.__name__ = "Integer32"
_WmanIfBsDcdTransition_Object = MibTableColumn
wmanIfBsDcdTransition = _WmanIfBsDcdTransition_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 4),
    _WmanIfBsDcdTransition_Type()
)
wmanIfBsDcdTransition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsDcdTransition.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsDcdTransition.setUnits("Number of MAC Frames")


class _WmanIfBsInitialRangingInterval_Type(Integer32):
    """Custom type wmanIfBsInitialRangingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_WmanIfBsInitialRangingInterval_Type.__name__ = "Integer32"
_WmanIfBsInitialRangingInterval_Object = MibTableColumn
wmanIfBsInitialRangingInterval = _WmanIfBsInitialRangingInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 5),
    _WmanIfBsInitialRangingInterval_Type()
)
wmanIfBsInitialRangingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsInitialRangingInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsInitialRangingInterval.setUnits("milliseconds")


class _WmanIfBsSsULMapProcTime_Type(Unsigned32):
    """Custom type wmanIfBsSsULMapProcTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 4294967295),
    )


_WmanIfBsSsULMapProcTime_Type.__name__ = "Unsigned32"
_WmanIfBsSsULMapProcTime_Object = MibTableColumn
wmanIfBsSsULMapProcTime = _WmanIfBsSsULMapProcTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 6),
    _WmanIfBsSsULMapProcTime_Type()
)
wmanIfBsSsULMapProcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsSsULMapProcTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSsULMapProcTime.setUnits("micro seconds")


class _WmanIfBsSsRangRespProcTime_Type(Unsigned32):
    """Custom type wmanIfBsSsRangRespProcTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 4294967295),
    )


_WmanIfBsSsRangRespProcTime_Type.__name__ = "Unsigned32"
_WmanIfBsSsRangRespProcTime_Object = MibTableColumn
wmanIfBsSsRangRespProcTime = _WmanIfBsSsRangRespProcTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 7),
    _WmanIfBsSsRangRespProcTime_Type()
)
wmanIfBsSsRangRespProcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsSsRangRespProcTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSsRangRespProcTime.setUnits("micro seconds")


class _WmanIfBsT5Timeout_Type(Integer32):
    """Custom type wmanIfBsT5Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_WmanIfBsT5Timeout_Type.__name__ = "Integer32"
_WmanIfBsT5Timeout_Object = MibTableColumn
wmanIfBsT5Timeout = _WmanIfBsT5Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 8),
    _WmanIfBsT5Timeout_Type()
)
wmanIfBsT5Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsT5Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsT5Timeout.setUnits("milliseconds")


class _WmanIfBsT9Timeout_Type(Integer32):
    """Custom type wmanIfBsT9Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 65535),
    )


_WmanIfBsT9Timeout_Type.__name__ = "Integer32"
_WmanIfBsT9Timeout_Object = MibTableColumn
wmanIfBsT9Timeout = _WmanIfBsT9Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 9),
    _WmanIfBsT9Timeout_Type()
)
wmanIfBsT9Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsT9Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsT9Timeout.setUnits("milliseconds")


class _WmanIfBsT13Timeout_Type(Integer32):
    """Custom type wmanIfBsT13Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 65535),
    )


_WmanIfBsT13Timeout_Type.__name__ = "Integer32"
_WmanIfBsT13Timeout_Object = MibTableColumn
wmanIfBsT13Timeout = _WmanIfBsT13Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 10),
    _WmanIfBsT13Timeout_Type()
)
wmanIfBsT13Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsT13Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsT13Timeout.setUnits("minutes")


class _WmanIfBsT15Timeout_Type(Integer32):
    """Custom type wmanIfBsT15Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 65535),
    )


_WmanIfBsT15Timeout_Type.__name__ = "Integer32"
_WmanIfBsT15Timeout_Object = MibTableColumn
wmanIfBsT15Timeout = _WmanIfBsT15Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 11),
    _WmanIfBsT15Timeout_Type()
)
wmanIfBsT15Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsT15Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsT15Timeout.setUnits("milliseconds")


class _WmanIfBsT17Timeout_Type(Integer32):
    """Custom type wmanIfBsT17Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_WmanIfBsT17Timeout_Type.__name__ = "Integer32"
_WmanIfBsT17Timeout_Object = MibTableColumn
wmanIfBsT17Timeout = _WmanIfBsT17Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 12),
    _WmanIfBsT17Timeout_Type()
)
wmanIfBsT17Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsT17Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsT17Timeout.setUnits("minutes")


class _WmanIfBsT27IdleTimer_Type(Unsigned32):
    """Custom type wmanIfBsT27IdleTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 4294967295),
    )


_WmanIfBsT27IdleTimer_Type.__name__ = "Unsigned32"
_WmanIfBsT27IdleTimer_Object = MibTableColumn
wmanIfBsT27IdleTimer = _WmanIfBsT27IdleTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 13),
    _WmanIfBsT27IdleTimer_Type()
)
wmanIfBsT27IdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsT27IdleTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsT27IdleTimer.setUnits("us")


class _WmanIfBsT27ActiveTimer_Type(Unsigned32):
    """Custom type wmanIfBsT27ActiveTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 4294967295),
    )


_WmanIfBsT27ActiveTimer_Type.__name__ = "Unsigned32"
_WmanIfBsT27ActiveTimer_Object = MibTableColumn
wmanIfBsT27ActiveTimer = _WmanIfBsT27ActiveTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 14),
    _WmanIfBsT27ActiveTimer_Type()
)
wmanIfBsT27ActiveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsT27ActiveTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsT27ActiveTimer.setUnits("us")


class _WmanIfBs2ndMgmtDlQoSProfileIndex_Type(Integer32):
    """Custom type wmanIfBs2ndMgmtDlQoSProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIfBs2ndMgmtDlQoSProfileIndex_Type.__name__ = "Integer32"
_WmanIfBs2ndMgmtDlQoSProfileIndex_Object = MibTableColumn
wmanIfBs2ndMgmtDlQoSProfileIndex = _WmanIfBs2ndMgmtDlQoSProfileIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 15),
    _WmanIfBs2ndMgmtDlQoSProfileIndex_Type()
)
wmanIfBs2ndMgmtDlQoSProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBs2ndMgmtDlQoSProfileIndex.setStatus("current")


class _WmanIfBs2ndMgmtUlQoSProfileIndex_Type(Integer32):
    """Custom type wmanIfBs2ndMgmtUlQoSProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIfBs2ndMgmtUlQoSProfileIndex_Type.__name__ = "Integer32"
_WmanIfBs2ndMgmtUlQoSProfileIndex_Object = MibTableColumn
wmanIfBs2ndMgmtUlQoSProfileIndex = _WmanIfBs2ndMgmtUlQoSProfileIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 16),
    _WmanIfBs2ndMgmtUlQoSProfileIndex_Type()
)
wmanIfBs2ndMgmtUlQoSProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBs2ndMgmtUlQoSProfileIndex.setStatus("current")


class _WmanIfBsAutoSfidEnabled_Type(Integer32):
    """Custom type wmanIfBsAutoSfidEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("autoSfidDisabled", 0),
          ("autoSfidEnabled", 1))
    )


_WmanIfBsAutoSfidEnabled_Type.__name__ = "Integer32"
_WmanIfBsAutoSfidEnabled_Object = MibTableColumn
wmanIfBsAutoSfidEnabled = _WmanIfBsAutoSfidEnabled_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 17),
    _WmanIfBsAutoSfidEnabled_Type()
)
wmanIfBsAutoSfidEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsAutoSfidEnabled.setStatus("current")


class _WmanIfBsAutoSfidRangeMin_Type(Unsigned32):
    """Custom type wmanIfBsAutoSfidRangeMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfBsAutoSfidRangeMin_Type.__name__ = "Unsigned32"
_WmanIfBsAutoSfidRangeMin_Object = MibTableColumn
wmanIfBsAutoSfidRangeMin = _WmanIfBsAutoSfidRangeMin_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 18),
    _WmanIfBsAutoSfidRangeMin_Type()
)
wmanIfBsAutoSfidRangeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsAutoSfidRangeMin.setStatus("current")


class _WmanIfBsAutoSfidRangeMax_Type(Unsigned32):
    """Custom type wmanIfBsAutoSfidRangeMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfBsAutoSfidRangeMax_Type.__name__ = "Unsigned32"
_WmanIfBsAutoSfidRangeMax_Object = MibTableColumn
wmanIfBsAutoSfidRangeMax = _WmanIfBsAutoSfidRangeMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 19),
    _WmanIfBsAutoSfidRangeMax_Type()
)
wmanIfBsAutoSfidRangeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsAutoSfidRangeMax.setStatus("current")


class _WmanIfBsAasChanFbckReqFreq_Type(Integer32):
    """Custom type wmanIfBsAasChanFbckReqFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10000),
    )


_WmanIfBsAasChanFbckReqFreq_Type.__name__ = "Integer32"
_WmanIfBsAasChanFbckReqFreq_Object = MibTableColumn
wmanIfBsAasChanFbckReqFreq = _WmanIfBsAasChanFbckReqFreq_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 20),
    _WmanIfBsAasChanFbckReqFreq_Type()
)
wmanIfBsAasChanFbckReqFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsAasChanFbckReqFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsAasChanFbckReqFreq.setUnits("ms")


class _WmanIfBsAasBeamSelectFreq_Type(Integer32):
    """Custom type wmanIfBsAasBeamSelectFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10000),
    )


_WmanIfBsAasBeamSelectFreq_Type.__name__ = "Integer32"
_WmanIfBsAasBeamSelectFreq_Object = MibTableColumn
wmanIfBsAasBeamSelectFreq = _WmanIfBsAasBeamSelectFreq_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 21),
    _WmanIfBsAasBeamSelectFreq_Type()
)
wmanIfBsAasBeamSelectFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsAasBeamSelectFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsAasBeamSelectFreq.setUnits("ms")


class _WmanIfBsAasChanFbckReqResolution_Type(Integer32):
    """Custom type wmanIfBsAasChanFbckReqResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aasChanFbckRes00", 0),
          ("aasChanFbckRes01", 1),
          ("aasChanFbckRes10", 2),
          ("aasChanFbckRes11", 3))
    )


_WmanIfBsAasChanFbckReqResolution_Type.__name__ = "Integer32"
_WmanIfBsAasChanFbckReqResolution_Object = MibTableColumn
wmanIfBsAasChanFbckReqResolution = _WmanIfBsAasChanFbckReqResolution_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 22),
    _WmanIfBsAasChanFbckReqResolution_Type()
)
wmanIfBsAasChanFbckReqResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsAasChanFbckReqResolution.setStatus("current")


class _WmanIfBsAasBeamReqResolution_Type(Integer32):
    """Custom type wmanIfBsAasBeamReqResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aasBeamReqRes000", 0),
          ("aasBeamReqRes001", 1),
          ("aasBeamReqRes010", 2),
          ("aasBeamReqRes011", 3),
          ("aasBeamReqRes100", 4))
    )


_WmanIfBsAasBeamReqResolution_Type.__name__ = "Integer32"
_WmanIfBsAasBeamReqResolution_Object = MibTableColumn
wmanIfBsAasBeamReqResolution = _WmanIfBsAasBeamReqResolution_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 23),
    _WmanIfBsAasBeamReqResolution_Type()
)
wmanIfBsAasBeamReqResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsAasBeamReqResolution.setStatus("current")


class _WmanIfBsAasNumOptDiversityZones_Type(Integer32):
    """Custom type wmanIfBsAasNumOptDiversityZones based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsAasNumOptDiversityZones_Type.__name__ = "Integer32"
_WmanIfBsAasNumOptDiversityZones_Object = MibTableColumn
wmanIfBsAasNumOptDiversityZones = _WmanIfBsAasNumOptDiversityZones_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 24),
    _WmanIfBsAasNumOptDiversityZones_Type()
)
wmanIfBsAasNumOptDiversityZones.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsAasNumOptDiversityZones.setStatus("current")


class _WmanIfBsResetSector_Type(Integer32):
    """Custom type wmanIfBsResetSector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("actionResetSectorNoAction", 0),
          ("actionResetSector", 1))
    )


_WmanIfBsResetSector_Type.__name__ = "Integer32"
_WmanIfBsResetSector_Object = MibTableColumn
wmanIfBsResetSector = _WmanIfBsResetSector_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 25),
    _WmanIfBsResetSector_Type()
)
wmanIfBsResetSector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsResetSector.setStatus("current")
_WmanIfBsChannelMeasurementTable_Object = MibTable
wmanIfBsChannelMeasurementTable = _WmanIfBsChannelMeasurementTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wmanIfBsChannelMeasurementTable.setStatus("current")
_WmanIfBsChannelMeasurementEntry_Object = MibTableRow
wmanIfBsChannelMeasurementEntry = _WmanIfBsChannelMeasurementEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1)
)
wmanIfBsChannelMeasurementEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfBsSsMacAddress"),
    (0, "WMAN-IF-MIB", "wmanIfBsChannelDirection"),
    (0, "WMAN-IF-MIB", "wmanIfBsHistogramIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsChannelMeasurementEntry.setStatus("current")


class _WmanIfBsChannelDirection_Type(Integer32):
    """Custom type wmanIfBsChannelDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 1),
          ("upstream", 2))
    )


_WmanIfBsChannelDirection_Type.__name__ = "Integer32"
_WmanIfBsChannelDirection_Object = MibTableColumn
wmanIfBsChannelDirection = _WmanIfBsChannelDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 1),
    _WmanIfBsChannelDirection_Type()
)
wmanIfBsChannelDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsChannelDirection.setStatus("current")


class _WmanIfBsHistogramIndex_Type(Unsigned32):
    """Custom type wmanIfBsHistogramIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfBsHistogramIndex_Type.__name__ = "Unsigned32"
_WmanIfBsHistogramIndex_Object = MibTableColumn
wmanIfBsHistogramIndex = _WmanIfBsHistogramIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 2),
    _WmanIfBsHistogramIndex_Type()
)
wmanIfBsHistogramIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsHistogramIndex.setStatus("current")
_WmanIfBsChannelNumber_Type = WmanIfChannelNumber
_WmanIfBsChannelNumber_Object = MibTableColumn
wmanIfBsChannelNumber = _WmanIfBsChannelNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 3),
    _WmanIfBsChannelNumber_Type()
)
wmanIfBsChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsChannelNumber.setStatus("current")


class _WmanIfBsStartFrame_Type(Integer32):
    """Custom type wmanIfBsStartFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsStartFrame_Type.__name__ = "Integer32"
_WmanIfBsStartFrame_Object = MibTableColumn
wmanIfBsStartFrame = _WmanIfBsStartFrame_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 4),
    _WmanIfBsStartFrame_Type()
)
wmanIfBsStartFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsStartFrame.setStatus("current")


class _WmanIfBsDuration_Type(Integer32):
    """Custom type wmanIfBsDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_WmanIfBsDuration_Type.__name__ = "Integer32"
_WmanIfBsDuration_Object = MibTableColumn
wmanIfBsDuration = _WmanIfBsDuration_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 5),
    _WmanIfBsDuration_Type()
)
wmanIfBsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsDuration.setStatus("current")


class _WmanIfBsBasicReport_Type(Bits):
    """Custom type wmanIfBsBasicReport based on Bits"""
    namedValues = NamedValues(
        *(("wirelessHuman", 0),
          ("unknownTransmission", 1),
          ("primaryUser", 2),
          ("channelNotMeasured", 3))
    )

_WmanIfBsBasicReport_Type.__name__ = "Bits"
_WmanIfBsBasicReport_Object = MibTableColumn
wmanIfBsBasicReport = _WmanIfBsBasicReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 6),
    _WmanIfBsBasicReport_Type()
)
wmanIfBsBasicReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsBasicReport.setStatus("current")


class _WmanIfBsMeanCinrReport_Type(Integer32):
    """Custom type wmanIfBsMeanCinrReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_WmanIfBsMeanCinrReport_Type.__name__ = "Integer32"
_WmanIfBsMeanCinrReport_Object = MibTableColumn
wmanIfBsMeanCinrReport = _WmanIfBsMeanCinrReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 7),
    _WmanIfBsMeanCinrReport_Type()
)
wmanIfBsMeanCinrReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsMeanCinrReport.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsMeanCinrReport.setUnits("dB")


class _WmanIfBsMeanRssiReport_Type(Integer32):
    """Custom type wmanIfBsMeanRssiReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_WmanIfBsMeanRssiReport_Type.__name__ = "Integer32"
_WmanIfBsMeanRssiReport_Object = MibTableColumn
wmanIfBsMeanRssiReport = _WmanIfBsMeanRssiReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 8),
    _WmanIfBsMeanRssiReport_Type()
)
wmanIfBsMeanRssiReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsMeanRssiReport.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsMeanRssiReport.setUnits("dBm")


class _WmanIfBsStdDeviationCinrReport_Type(Integer32):
    """Custom type wmanIfBsStdDeviationCinrReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_WmanIfBsStdDeviationCinrReport_Type.__name__ = "Integer32"
_WmanIfBsStdDeviationCinrReport_Object = MibTableColumn
wmanIfBsStdDeviationCinrReport = _WmanIfBsStdDeviationCinrReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 9),
    _WmanIfBsStdDeviationCinrReport_Type()
)
wmanIfBsStdDeviationCinrReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsStdDeviationCinrReport.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsStdDeviationCinrReport.setUnits("dB")


class _WmanIfBsStdDeviationRssiReport_Type(Integer32):
    """Custom type wmanIfBsStdDeviationRssiReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_WmanIfBsStdDeviationRssiReport_Type.__name__ = "Integer32"
_WmanIfBsStdDeviationRssiReport_Object = MibTableColumn
wmanIfBsStdDeviationRssiReport = _WmanIfBsStdDeviationRssiReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 10),
    _WmanIfBsStdDeviationRssiReport_Type()
)
wmanIfBsStdDeviationRssiReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsStdDeviationRssiReport.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsStdDeviationRssiReport.setUnits("dB")
_WmanIfBsCapabilities_ObjectIdentity = ObjectIdentity
wmanIfBsCapabilities = _WmanIfBsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4)
)
_WmanIfBsSsReqCapabilitiesTable_Object = MibTable
wmanIfBsSsReqCapabilitiesTable = _WmanIfBsSsReqCapabilitiesTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapabilitiesTable.setStatus("current")
_WmanIfBsSsReqCapabilitiesEntry_Object = MibTableRow
wmanIfBsSsReqCapabilitiesEntry = _WmanIfBsSsReqCapabilitiesEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapabilitiesEntry.setStatus("current")
_WmanIfBsSsReqCapUplinkCidSupport_Type = WmanIfNumOfUplinkCid
_WmanIfBsSsReqCapUplinkCidSupport_Object = MibTableColumn
wmanIfBsSsReqCapUplinkCidSupport = _WmanIfBsSsReqCapUplinkCidSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1, 1, 1),
    _WmanIfBsSsReqCapUplinkCidSupport_Type()
)
wmanIfBsSsReqCapUplinkCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapUplinkCidSupport.setStatus("current")
_WmanIfBsSsReqCapArqSupport_Type = WmanIfArqSupportType
_WmanIfBsSsReqCapArqSupport_Object = MibTableColumn
wmanIfBsSsReqCapArqSupport = _WmanIfBsSsReqCapArqSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1, 1, 2),
    _WmanIfBsSsReqCapArqSupport_Type()
)
wmanIfBsSsReqCapArqSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapArqSupport.setStatus("current")


class _WmanIfBsSsReqCapDsxFlowControl_Type(WmanIfMaxDsxFlowType):
    """Custom type wmanIfBsSsReqCapDsxFlowControl based on WmanIfMaxDsxFlowType"""
    defaultValue = 0


_WmanIfBsSsReqCapDsxFlowControl_Type.__name__ = "WmanIfMaxDsxFlowType"
_WmanIfBsSsReqCapDsxFlowControl_Object = MibTableColumn
wmanIfBsSsReqCapDsxFlowControl = _WmanIfBsSsReqCapDsxFlowControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1, 1, 3),
    _WmanIfBsSsReqCapDsxFlowControl_Type()
)
wmanIfBsSsReqCapDsxFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapDsxFlowControl.setStatus("current")


class _WmanIfBsSsReqCapMacCrcSupport_Type(WmanIfMacCrcSupport):
    """Custom type wmanIfBsSsReqCapMacCrcSupport based on WmanIfMacCrcSupport"""
    defaultValue = 1


_WmanIfBsSsReqCapMacCrcSupport_Type.__name__ = "WmanIfMacCrcSupport"
_WmanIfBsSsReqCapMacCrcSupport_Object = MibTableColumn
wmanIfBsSsReqCapMacCrcSupport = _WmanIfBsSsReqCapMacCrcSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1, 1, 4),
    _WmanIfBsSsReqCapMacCrcSupport_Type()
)
wmanIfBsSsReqCapMacCrcSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapMacCrcSupport.setStatus("current")


class _WmanIfBsSsReqCapMcaFlowControl_Type(WmanIfMaxMcaFlowType):
    """Custom type wmanIfBsSsReqCapMcaFlowControl based on WmanIfMaxMcaFlowType"""
    defaultValue = 0


_WmanIfBsSsReqCapMcaFlowControl_Type.__name__ = "WmanIfMaxMcaFlowType"
_WmanIfBsSsReqCapMcaFlowControl_Object = MibTableColumn
wmanIfBsSsReqCapMcaFlowControl = _WmanIfBsSsReqCapMcaFlowControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1, 1, 5),
    _WmanIfBsSsReqCapMcaFlowControl_Type()
)
wmanIfBsSsReqCapMcaFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapMcaFlowControl.setStatus("current")


class _WmanIfBsSsReqCapMcpGroupCidSupport_Type(WmanIfMaxMcpGroupCid):
    """Custom type wmanIfBsSsReqCapMcpGroupCidSupport based on WmanIfMaxMcpGroupCid"""
    defaultValue = 0


_WmanIfBsSsReqCapMcpGroupCidSupport_Type.__name__ = "WmanIfMaxMcpGroupCid"
_WmanIfBsSsReqCapMcpGroupCidSupport_Object = MibTableColumn
wmanIfBsSsReqCapMcpGroupCidSupport = _WmanIfBsSsReqCapMcpGroupCidSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1, 1, 6),
    _WmanIfBsSsReqCapMcpGroupCidSupport_Type()
)
wmanIfBsSsReqCapMcpGroupCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapMcpGroupCidSupport.setStatus("current")


class _WmanIfBsSsReqCapPkmFlowControl_Type(WmanIfMaxPkmFlowType):
    """Custom type wmanIfBsSsReqCapPkmFlowControl based on WmanIfMaxPkmFlowType"""
    defaultValue = 0


_WmanIfBsSsReqCapPkmFlowControl_Type.__name__ = "WmanIfMaxPkmFlowType"
_WmanIfBsSsReqCapPkmFlowControl_Object = MibTableColumn
wmanIfBsSsReqCapPkmFlowControl = _WmanIfBsSsReqCapPkmFlowControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1, 1, 7),
    _WmanIfBsSsReqCapPkmFlowControl_Type()
)
wmanIfBsSsReqCapPkmFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapPkmFlowControl.setStatus("current")
_WmanIfBsSsReqCapAuthPolicyControl_Type = WmanIfAuthPolicyType
_WmanIfBsSsReqCapAuthPolicyControl_Object = MibTableColumn
wmanIfBsSsReqCapAuthPolicyControl = _WmanIfBsSsReqCapAuthPolicyControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1, 1, 8),
    _WmanIfBsSsReqCapAuthPolicyControl_Type()
)
wmanIfBsSsReqCapAuthPolicyControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapAuthPolicyControl.setStatus("current")


class _WmanIfBsSsReqCapMaxNumOfSupportedSA_Type(WmanIfMaxNumOfSaType):
    """Custom type wmanIfBsSsReqCapMaxNumOfSupportedSA based on WmanIfMaxNumOfSaType"""
    defaultValue = 1


_WmanIfBsSsReqCapMaxNumOfSupportedSA_Type.__name__ = "WmanIfMaxNumOfSaType"
_WmanIfBsSsReqCapMaxNumOfSupportedSA_Object = MibTableColumn
wmanIfBsSsReqCapMaxNumOfSupportedSA = _WmanIfBsSsReqCapMaxNumOfSupportedSA_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1, 1, 9),
    _WmanIfBsSsReqCapMaxNumOfSupportedSA_Type()
)
wmanIfBsSsReqCapMaxNumOfSupportedSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapMaxNumOfSupportedSA.setStatus("current")
_WmanIfBsSsReqCapIpVersion_Type = WmanIfIpVersionType
_WmanIfBsSsReqCapIpVersion_Object = MibTableColumn
wmanIfBsSsReqCapIpVersion = _WmanIfBsSsReqCapIpVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1, 1, 10),
    _WmanIfBsSsReqCapIpVersion_Type()
)
wmanIfBsSsReqCapIpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapIpVersion.setStatus("current")
_WmanIfBsSsReqCapMacCsSupportBitMap_Type = WmanIfMacCsBitMap
_WmanIfBsSsReqCapMacCsSupportBitMap_Object = MibTableColumn
wmanIfBsSsReqCapMacCsSupportBitMap = _WmanIfBsSsReqCapMacCsSupportBitMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1, 1, 11),
    _WmanIfBsSsReqCapMacCsSupportBitMap_Type()
)
wmanIfBsSsReqCapMacCsSupportBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapMacCsSupportBitMap.setStatus("current")


class _WmanIfBsSsReqCapMaxNumOfClassifier_Type(WmanIfMaxClassifiers):
    """Custom type wmanIfBsSsReqCapMaxNumOfClassifier based on WmanIfMaxClassifiers"""
    defaultValue = 0


_WmanIfBsSsReqCapMaxNumOfClassifier_Type.__name__ = "WmanIfMaxClassifiers"
_WmanIfBsSsReqCapMaxNumOfClassifier_Object = MibTableColumn
wmanIfBsSsReqCapMaxNumOfClassifier = _WmanIfBsSsReqCapMaxNumOfClassifier_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1, 1, 12),
    _WmanIfBsSsReqCapMaxNumOfClassifier_Type()
)
wmanIfBsSsReqCapMaxNumOfClassifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapMaxNumOfClassifier.setStatus("current")


class _WmanIfBsSsReqCapPhsSupport_Type(WmanIfPhsSupportType):
    """Custom type wmanIfBsSsReqCapPhsSupport based on WmanIfPhsSupportType"""
    defaultValue = 0


_WmanIfBsSsReqCapPhsSupport_Type.__name__ = "WmanIfPhsSupportType"
_WmanIfBsSsReqCapPhsSupport_Object = MibTableColumn
wmanIfBsSsReqCapPhsSupport = _WmanIfBsSsReqCapPhsSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1, 1, 13),
    _WmanIfBsSsReqCapPhsSupport_Type()
)
wmanIfBsSsReqCapPhsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapPhsSupport.setStatus("current")
_WmanIfBsSsReqCapBandwidthAllocSupport_Type = WmanIfBwAllocSupport
_WmanIfBsSsReqCapBandwidthAllocSupport_Object = MibTableColumn
wmanIfBsSsReqCapBandwidthAllocSupport = _WmanIfBsSsReqCapBandwidthAllocSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1, 1, 14),
    _WmanIfBsSsReqCapBandwidthAllocSupport_Type()
)
wmanIfBsSsReqCapBandwidthAllocSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapBandwidthAllocSupport.setStatus("current")
_WmanIfBsSsReqCapPduConstruction_Type = WmanIfPduConstruction
_WmanIfBsSsReqCapPduConstruction_Object = MibTableColumn
wmanIfBsSsReqCapPduConstruction = _WmanIfBsSsReqCapPduConstruction_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1, 1, 15),
    _WmanIfBsSsReqCapPduConstruction_Type()
)
wmanIfBsSsReqCapPduConstruction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapPduConstruction.setStatus("current")
_WmanIfBsSsReqCapTtgTransitionGap_Type = WmanIfSsTransitionGap
_WmanIfBsSsReqCapTtgTransitionGap_Object = MibTableColumn
wmanIfBsSsReqCapTtgTransitionGap = _WmanIfBsSsReqCapTtgTransitionGap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1, 1, 16),
    _WmanIfBsSsReqCapTtgTransitionGap_Type()
)
wmanIfBsSsReqCapTtgTransitionGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapTtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapTtgTransitionGap.setUnits("us")
_WmanIfBsSsReqCapRtgTransitionGap_Type = WmanIfSsTransitionGap
_WmanIfBsSsReqCapRtgTransitionGap_Object = MibTableColumn
wmanIfBsSsReqCapRtgTransitionGap = _WmanIfBsSsReqCapRtgTransitionGap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 1, 1, 17),
    _WmanIfBsSsReqCapRtgTransitionGap_Type()
)
wmanIfBsSsReqCapRtgTransitionGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapRtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSsReqCapRtgTransitionGap.setUnits("us")
_WmanIfBsSsRspCapabilitiesTable_Object = MibTable
wmanIfBsSsRspCapabilitiesTable = _WmanIfBsSsRspCapabilitiesTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapabilitiesTable.setStatus("current")
_WmanIfBsSsRspCapabilitiesEntry_Object = MibTableRow
wmanIfBsSsRspCapabilitiesEntry = _WmanIfBsSsRspCapabilitiesEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapabilitiesEntry.setStatus("current")
_WmanIfBsSsRspCapUplinkCidSupport_Type = WmanIfNumOfUplinkCid
_WmanIfBsSsRspCapUplinkCidSupport_Object = MibTableColumn
wmanIfBsSsRspCapUplinkCidSupport = _WmanIfBsSsRspCapUplinkCidSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2, 1, 1),
    _WmanIfBsSsRspCapUplinkCidSupport_Type()
)
wmanIfBsSsRspCapUplinkCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapUplinkCidSupport.setStatus("current")
_WmanIfBsSsRspCapArqSupport_Type = WmanIfArqSupportType
_WmanIfBsSsRspCapArqSupport_Object = MibTableColumn
wmanIfBsSsRspCapArqSupport = _WmanIfBsSsRspCapArqSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2, 1, 2),
    _WmanIfBsSsRspCapArqSupport_Type()
)
wmanIfBsSsRspCapArqSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapArqSupport.setStatus("current")
_WmanIfBsSsRspCapDsxFlowControl_Type = WmanIfMaxDsxFlowType
_WmanIfBsSsRspCapDsxFlowControl_Object = MibTableColumn
wmanIfBsSsRspCapDsxFlowControl = _WmanIfBsSsRspCapDsxFlowControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2, 1, 3),
    _WmanIfBsSsRspCapDsxFlowControl_Type()
)
wmanIfBsSsRspCapDsxFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapDsxFlowControl.setStatus("current")


class _WmanIfBsSsRspCapMacCrcSupport_Type(WmanIfMacCrcSupport):
    """Custom type wmanIfBsSsRspCapMacCrcSupport based on WmanIfMacCrcSupport"""
    defaultValue = 1


_WmanIfBsSsRspCapMacCrcSupport_Type.__name__ = "WmanIfMacCrcSupport"
_WmanIfBsSsRspCapMacCrcSupport_Object = MibTableColumn
wmanIfBsSsRspCapMacCrcSupport = _WmanIfBsSsRspCapMacCrcSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2, 1, 4),
    _WmanIfBsSsRspCapMacCrcSupport_Type()
)
wmanIfBsSsRspCapMacCrcSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapMacCrcSupport.setStatus("current")


class _WmanIfBsSsRspCapMcaFlowControl_Type(WmanIfMaxMcaFlowType):
    """Custom type wmanIfBsSsRspCapMcaFlowControl based on WmanIfMaxMcaFlowType"""
    defaultValue = 0


_WmanIfBsSsRspCapMcaFlowControl_Type.__name__ = "WmanIfMaxMcaFlowType"
_WmanIfBsSsRspCapMcaFlowControl_Object = MibTableColumn
wmanIfBsSsRspCapMcaFlowControl = _WmanIfBsSsRspCapMcaFlowControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2, 1, 5),
    _WmanIfBsSsRspCapMcaFlowControl_Type()
)
wmanIfBsSsRspCapMcaFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapMcaFlowControl.setStatus("current")


class _WmanIfBsSsRspCapMcpGroupCidSupport_Type(WmanIfMaxMcpGroupCid):
    """Custom type wmanIfBsSsRspCapMcpGroupCidSupport based on WmanIfMaxMcpGroupCid"""
    defaultValue = 0


_WmanIfBsSsRspCapMcpGroupCidSupport_Type.__name__ = "WmanIfMaxMcpGroupCid"
_WmanIfBsSsRspCapMcpGroupCidSupport_Object = MibTableColumn
wmanIfBsSsRspCapMcpGroupCidSupport = _WmanIfBsSsRspCapMcpGroupCidSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2, 1, 6),
    _WmanIfBsSsRspCapMcpGroupCidSupport_Type()
)
wmanIfBsSsRspCapMcpGroupCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapMcpGroupCidSupport.setStatus("current")


class _WmanIfBsSsRspCapPkmFlowControl_Type(WmanIfMaxPkmFlowType):
    """Custom type wmanIfBsSsRspCapPkmFlowControl based on WmanIfMaxPkmFlowType"""
    defaultValue = 0


_WmanIfBsSsRspCapPkmFlowControl_Type.__name__ = "WmanIfMaxPkmFlowType"
_WmanIfBsSsRspCapPkmFlowControl_Object = MibTableColumn
wmanIfBsSsRspCapPkmFlowControl = _WmanIfBsSsRspCapPkmFlowControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2, 1, 7),
    _WmanIfBsSsRspCapPkmFlowControl_Type()
)
wmanIfBsSsRspCapPkmFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapPkmFlowControl.setStatus("current")
_WmanIfBsSsRspCapAuthPolicyControl_Type = WmanIfAuthPolicyType
_WmanIfBsSsRspCapAuthPolicyControl_Object = MibTableColumn
wmanIfBsSsRspCapAuthPolicyControl = _WmanIfBsSsRspCapAuthPolicyControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2, 1, 8),
    _WmanIfBsSsRspCapAuthPolicyControl_Type()
)
wmanIfBsSsRspCapAuthPolicyControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapAuthPolicyControl.setStatus("current")


class _WmanIfBsSsRspCapMaxNumOfSupportedSA_Type(WmanIfMaxNumOfSaType):
    """Custom type wmanIfBsSsRspCapMaxNumOfSupportedSA based on WmanIfMaxNumOfSaType"""
    defaultValue = 1


_WmanIfBsSsRspCapMaxNumOfSupportedSA_Type.__name__ = "WmanIfMaxNumOfSaType"
_WmanIfBsSsRspCapMaxNumOfSupportedSA_Object = MibTableColumn
wmanIfBsSsRspCapMaxNumOfSupportedSA = _WmanIfBsSsRspCapMaxNumOfSupportedSA_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2, 1, 9),
    _WmanIfBsSsRspCapMaxNumOfSupportedSA_Type()
)
wmanIfBsSsRspCapMaxNumOfSupportedSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapMaxNumOfSupportedSA.setStatus("current")
_WmanIfBsSsRspCapIpVersion_Type = WmanIfIpVersionType
_WmanIfBsSsRspCapIpVersion_Object = MibTableColumn
wmanIfBsSsRspCapIpVersion = _WmanIfBsSsRspCapIpVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2, 1, 10),
    _WmanIfBsSsRspCapIpVersion_Type()
)
wmanIfBsSsRspCapIpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapIpVersion.setStatus("current")
_WmanIfBsSsRspCapMacCsSupportBitMap_Type = WmanIfMacCsBitMap
_WmanIfBsSsRspCapMacCsSupportBitMap_Object = MibTableColumn
wmanIfBsSsRspCapMacCsSupportBitMap = _WmanIfBsSsRspCapMacCsSupportBitMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2, 1, 11),
    _WmanIfBsSsRspCapMacCsSupportBitMap_Type()
)
wmanIfBsSsRspCapMacCsSupportBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapMacCsSupportBitMap.setStatus("current")


class _WmanIfBsSsRspCapMaxNumOfClassifier_Type(WmanIfMaxClassifiers):
    """Custom type wmanIfBsSsRspCapMaxNumOfClassifier based on WmanIfMaxClassifiers"""
    defaultValue = 0


_WmanIfBsSsRspCapMaxNumOfClassifier_Type.__name__ = "WmanIfMaxClassifiers"
_WmanIfBsSsRspCapMaxNumOfClassifier_Object = MibTableColumn
wmanIfBsSsRspCapMaxNumOfClassifier = _WmanIfBsSsRspCapMaxNumOfClassifier_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2, 1, 12),
    _WmanIfBsSsRspCapMaxNumOfClassifier_Type()
)
wmanIfBsSsRspCapMaxNumOfClassifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapMaxNumOfClassifier.setStatus("current")


class _WmanIfBsSsRspCapPhsSupport_Type(WmanIfPhsSupportType):
    """Custom type wmanIfBsSsRspCapPhsSupport based on WmanIfPhsSupportType"""
    defaultValue = 0


_WmanIfBsSsRspCapPhsSupport_Type.__name__ = "WmanIfPhsSupportType"
_WmanIfBsSsRspCapPhsSupport_Object = MibTableColumn
wmanIfBsSsRspCapPhsSupport = _WmanIfBsSsRspCapPhsSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2, 1, 13),
    _WmanIfBsSsRspCapPhsSupport_Type()
)
wmanIfBsSsRspCapPhsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapPhsSupport.setStatus("current")
_WmanIfBsSsRspCapBandwidthAllocSupport_Type = WmanIfBwAllocSupport
_WmanIfBsSsRspCapBandwidthAllocSupport_Object = MibTableColumn
wmanIfBsSsRspCapBandwidthAllocSupport = _WmanIfBsSsRspCapBandwidthAllocSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2, 1, 14),
    _WmanIfBsSsRspCapBandwidthAllocSupport_Type()
)
wmanIfBsSsRspCapBandwidthAllocSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapBandwidthAllocSupport.setStatus("current")
_WmanIfBsSsRspCapPduConstruction_Type = WmanIfPduConstruction
_WmanIfBsSsRspCapPduConstruction_Object = MibTableColumn
wmanIfBsSsRspCapPduConstruction = _WmanIfBsSsRspCapPduConstruction_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2, 1, 15),
    _WmanIfBsSsRspCapPduConstruction_Type()
)
wmanIfBsSsRspCapPduConstruction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapPduConstruction.setStatus("current")
_WmanIfBsSsRspCapTtgTransitionGap_Type = WmanIfSsTransitionGap
_WmanIfBsSsRspCapTtgTransitionGap_Object = MibTableColumn
wmanIfBsSsRspCapTtgTransitionGap = _WmanIfBsSsRspCapTtgTransitionGap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2, 1, 16),
    _WmanIfBsSsRspCapTtgTransitionGap_Type()
)
wmanIfBsSsRspCapTtgTransitionGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapTtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapTtgTransitionGap.setUnits("us")
_WmanIfBsSsRspCapRtgTransitionGap_Type = WmanIfSsTransitionGap
_WmanIfBsSsRspCapRtgTransitionGap_Object = MibTableColumn
wmanIfBsSsRspCapRtgTransitionGap = _WmanIfBsSsRspCapRtgTransitionGap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 2, 1, 17),
    _WmanIfBsSsRspCapRtgTransitionGap_Type()
)
wmanIfBsSsRspCapRtgTransitionGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapRtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSsRspCapRtgTransitionGap.setUnits("us")
_WmanIfBsBasicCapabilitiesTable_Object = MibTable
wmanIfBsBasicCapabilitiesTable = _WmanIfBsBasicCapabilitiesTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3)
)
if mibBuilder.loadTexts:
    wmanIfBsBasicCapabilitiesTable.setStatus("current")
_WmanIfBsBasicCapabilitiesEntry_Object = MibTableRow
wmanIfBsBasicCapabilitiesEntry = _WmanIfBsBasicCapabilitiesEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3, 1)
)
wmanIfBsBasicCapabilitiesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsBasicCapabilitiesEntry.setStatus("current")
_WmanIfBsCapUplinkCidSupport_Type = WmanIfNumOfUplinkCid
_WmanIfBsCapUplinkCidSupport_Object = MibTableColumn
wmanIfBsCapUplinkCidSupport = _WmanIfBsCapUplinkCidSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3, 1, 1),
    _WmanIfBsCapUplinkCidSupport_Type()
)
wmanIfBsCapUplinkCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsCapUplinkCidSupport.setStatus("current")
_WmanIfBsCapArqSupport_Type = WmanIfArqSupportType
_WmanIfBsCapArqSupport_Object = MibTableColumn
wmanIfBsCapArqSupport = _WmanIfBsCapArqSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3, 1, 2),
    _WmanIfBsCapArqSupport_Type()
)
wmanIfBsCapArqSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsCapArqSupport.setStatus("current")


class _WmanIfBsCapDsxFlowControl_Type(WmanIfMaxDsxFlowType):
    """Custom type wmanIfBsCapDsxFlowControl based on WmanIfMaxDsxFlowType"""
    defaultValue = 0


_WmanIfBsCapDsxFlowControl_Type.__name__ = "WmanIfMaxDsxFlowType"
_WmanIfBsCapDsxFlowControl_Object = MibTableColumn
wmanIfBsCapDsxFlowControl = _WmanIfBsCapDsxFlowControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3, 1, 3),
    _WmanIfBsCapDsxFlowControl_Type()
)
wmanIfBsCapDsxFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsCapDsxFlowControl.setStatus("current")


class _WmanIfBsCapMacCrcSupport_Type(WmanIfMacCrcSupport):
    """Custom type wmanIfBsCapMacCrcSupport based on WmanIfMacCrcSupport"""
    defaultValue = 1


_WmanIfBsCapMacCrcSupport_Type.__name__ = "WmanIfMacCrcSupport"
_WmanIfBsCapMacCrcSupport_Object = MibTableColumn
wmanIfBsCapMacCrcSupport = _WmanIfBsCapMacCrcSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3, 1, 4),
    _WmanIfBsCapMacCrcSupport_Type()
)
wmanIfBsCapMacCrcSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsCapMacCrcSupport.setStatus("current")


class _WmanIfBsCapMcaFlowControl_Type(WmanIfMaxMcaFlowType):
    """Custom type wmanIfBsCapMcaFlowControl based on WmanIfMaxMcaFlowType"""
    defaultValue = 0


_WmanIfBsCapMcaFlowControl_Type.__name__ = "WmanIfMaxMcaFlowType"
_WmanIfBsCapMcaFlowControl_Object = MibTableColumn
wmanIfBsCapMcaFlowControl = _WmanIfBsCapMcaFlowControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3, 1, 5),
    _WmanIfBsCapMcaFlowControl_Type()
)
wmanIfBsCapMcaFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsCapMcaFlowControl.setStatus("current")


class _WmanIfBsCapMcpGroupCidSupport_Type(WmanIfMaxMcpGroupCid):
    """Custom type wmanIfBsCapMcpGroupCidSupport based on WmanIfMaxMcpGroupCid"""
    defaultValue = 0


_WmanIfBsCapMcpGroupCidSupport_Type.__name__ = "WmanIfMaxMcpGroupCid"
_WmanIfBsCapMcpGroupCidSupport_Object = MibTableColumn
wmanIfBsCapMcpGroupCidSupport = _WmanIfBsCapMcpGroupCidSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3, 1, 6),
    _WmanIfBsCapMcpGroupCidSupport_Type()
)
wmanIfBsCapMcpGroupCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsCapMcpGroupCidSupport.setStatus("current")


class _WmanIfBsCapPkmFlowControl_Type(WmanIfMaxPkmFlowType):
    """Custom type wmanIfBsCapPkmFlowControl based on WmanIfMaxPkmFlowType"""
    defaultValue = 0


_WmanIfBsCapPkmFlowControl_Type.__name__ = "WmanIfMaxPkmFlowType"
_WmanIfBsCapPkmFlowControl_Object = MibTableColumn
wmanIfBsCapPkmFlowControl = _WmanIfBsCapPkmFlowControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3, 1, 7),
    _WmanIfBsCapPkmFlowControl_Type()
)
wmanIfBsCapPkmFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsCapPkmFlowControl.setStatus("current")
_WmanIfBsCapAuthPolicyControl_Type = WmanIfAuthPolicyType
_WmanIfBsCapAuthPolicyControl_Object = MibTableColumn
wmanIfBsCapAuthPolicyControl = _WmanIfBsCapAuthPolicyControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3, 1, 8),
    _WmanIfBsCapAuthPolicyControl_Type()
)
wmanIfBsCapAuthPolicyControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsCapAuthPolicyControl.setStatus("current")


class _WmanIfBsCapMaxNumOfSupportedSA_Type(WmanIfMaxNumOfSaType):
    """Custom type wmanIfBsCapMaxNumOfSupportedSA based on WmanIfMaxNumOfSaType"""
    defaultValue = 1


_WmanIfBsCapMaxNumOfSupportedSA_Type.__name__ = "WmanIfMaxNumOfSaType"
_WmanIfBsCapMaxNumOfSupportedSA_Object = MibTableColumn
wmanIfBsCapMaxNumOfSupportedSA = _WmanIfBsCapMaxNumOfSupportedSA_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3, 1, 9),
    _WmanIfBsCapMaxNumOfSupportedSA_Type()
)
wmanIfBsCapMaxNumOfSupportedSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsCapMaxNumOfSupportedSA.setStatus("current")
_WmanIfBsCapIpVersion_Type = WmanIfIpVersionType
_WmanIfBsCapIpVersion_Object = MibTableColumn
wmanIfBsCapIpVersion = _WmanIfBsCapIpVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3, 1, 10),
    _WmanIfBsCapIpVersion_Type()
)
wmanIfBsCapIpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsCapIpVersion.setStatus("current")
_WmanIfBsCapMacCsSupportBitMap_Type = WmanIfMacCsBitMap
_WmanIfBsCapMacCsSupportBitMap_Object = MibTableColumn
wmanIfBsCapMacCsSupportBitMap = _WmanIfBsCapMacCsSupportBitMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3, 1, 11),
    _WmanIfBsCapMacCsSupportBitMap_Type()
)
wmanIfBsCapMacCsSupportBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsCapMacCsSupportBitMap.setStatus("current")


class _WmanIfBsCapMaxNumOfClassifier_Type(WmanIfMaxClassifiers):
    """Custom type wmanIfBsCapMaxNumOfClassifier based on WmanIfMaxClassifiers"""
    defaultValue = 0


_WmanIfBsCapMaxNumOfClassifier_Type.__name__ = "WmanIfMaxClassifiers"
_WmanIfBsCapMaxNumOfClassifier_Object = MibTableColumn
wmanIfBsCapMaxNumOfClassifier = _WmanIfBsCapMaxNumOfClassifier_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3, 1, 12),
    _WmanIfBsCapMaxNumOfClassifier_Type()
)
wmanIfBsCapMaxNumOfClassifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsCapMaxNumOfClassifier.setStatus("current")


class _WmanIfBsCapPhsSupport_Type(WmanIfPhsSupportType):
    """Custom type wmanIfBsCapPhsSupport based on WmanIfPhsSupportType"""
    defaultValue = 0


_WmanIfBsCapPhsSupport_Type.__name__ = "WmanIfPhsSupportType"
_WmanIfBsCapPhsSupport_Object = MibTableColumn
wmanIfBsCapPhsSupport = _WmanIfBsCapPhsSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3, 1, 13),
    _WmanIfBsCapPhsSupport_Type()
)
wmanIfBsCapPhsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsCapPhsSupport.setStatus("current")
_WmanIfBsCapBandwidthAllocSupport_Type = WmanIfBwAllocSupport
_WmanIfBsCapBandwidthAllocSupport_Object = MibTableColumn
wmanIfBsCapBandwidthAllocSupport = _WmanIfBsCapBandwidthAllocSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3, 1, 14),
    _WmanIfBsCapBandwidthAllocSupport_Type()
)
wmanIfBsCapBandwidthAllocSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsCapBandwidthAllocSupport.setStatus("current")
_WmanIfBsCapPduConstruction_Type = WmanIfPduConstruction
_WmanIfBsCapPduConstruction_Object = MibTableColumn
wmanIfBsCapPduConstruction = _WmanIfBsCapPduConstruction_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3, 1, 15),
    _WmanIfBsCapPduConstruction_Type()
)
wmanIfBsCapPduConstruction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsCapPduConstruction.setStatus("current")
_WmanIfBsCapTtgTransitionGap_Type = WmanIfSsTransitionGap
_WmanIfBsCapTtgTransitionGap_Object = MibTableColumn
wmanIfBsCapTtgTransitionGap = _WmanIfBsCapTtgTransitionGap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3, 1, 16),
    _WmanIfBsCapTtgTransitionGap_Type()
)
wmanIfBsCapTtgTransitionGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsCapTtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsCapTtgTransitionGap.setUnits("us")
_WmanIfBsCapRtgTransitionGap_Type = WmanIfSsTransitionGap
_WmanIfBsCapRtgTransitionGap_Object = MibTableColumn
wmanIfBsCapRtgTransitionGap = _WmanIfBsCapRtgTransitionGap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 3, 1, 17),
    _WmanIfBsCapRtgTransitionGap_Type()
)
wmanIfBsCapRtgTransitionGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsCapRtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsCapRtgTransitionGap.setUnits("us")
_WmanIfBsCapabilitiesConfigTable_Object = MibTable
wmanIfBsCapabilitiesConfigTable = _WmanIfBsCapabilitiesConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4)
)
if mibBuilder.loadTexts:
    wmanIfBsCapabilitiesConfigTable.setStatus("current")
_WmanIfBsCapabilitiesConfigEntry_Object = MibTableRow
wmanIfBsCapabilitiesConfigEntry = _WmanIfBsCapabilitiesConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4, 1)
)
wmanIfBsCapabilitiesConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsCapabilitiesConfigEntry.setStatus("current")
_WmanIfBsCapCfgUplinkCidSupport_Type = WmanIfNumOfUplinkCid
_WmanIfBsCapCfgUplinkCidSupport_Object = MibTableColumn
wmanIfBsCapCfgUplinkCidSupport = _WmanIfBsCapCfgUplinkCidSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4, 1, 1),
    _WmanIfBsCapCfgUplinkCidSupport_Type()
)
wmanIfBsCapCfgUplinkCidSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgUplinkCidSupport.setStatus("current")
_WmanIfBsCapCfgArqSupport_Type = WmanIfArqSupportType
_WmanIfBsCapCfgArqSupport_Object = MibTableColumn
wmanIfBsCapCfgArqSupport = _WmanIfBsCapCfgArqSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4, 1, 2),
    _WmanIfBsCapCfgArqSupport_Type()
)
wmanIfBsCapCfgArqSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgArqSupport.setStatus("current")


class _WmanIfBsCapCfgDsxFlowControl_Type(WmanIfMaxDsxFlowType):
    """Custom type wmanIfBsCapCfgDsxFlowControl based on WmanIfMaxDsxFlowType"""
    defaultValue = 0


_WmanIfBsCapCfgDsxFlowControl_Type.__name__ = "WmanIfMaxDsxFlowType"
_WmanIfBsCapCfgDsxFlowControl_Object = MibTableColumn
wmanIfBsCapCfgDsxFlowControl = _WmanIfBsCapCfgDsxFlowControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4, 1, 3),
    _WmanIfBsCapCfgDsxFlowControl_Type()
)
wmanIfBsCapCfgDsxFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgDsxFlowControl.setStatus("current")


class _WmanIfBsCapCfgMacCrcSupport_Type(WmanIfMacCrcSupport):
    """Custom type wmanIfBsCapCfgMacCrcSupport based on WmanIfMacCrcSupport"""
    defaultValue = 1


_WmanIfBsCapCfgMacCrcSupport_Type.__name__ = "WmanIfMacCrcSupport"
_WmanIfBsCapCfgMacCrcSupport_Object = MibTableColumn
wmanIfBsCapCfgMacCrcSupport = _WmanIfBsCapCfgMacCrcSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4, 1, 4),
    _WmanIfBsCapCfgMacCrcSupport_Type()
)
wmanIfBsCapCfgMacCrcSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgMacCrcSupport.setStatus("current")


class _WmanIfBsCapCfgMcaFlowControl_Type(WmanIfMaxMcaFlowType):
    """Custom type wmanIfBsCapCfgMcaFlowControl based on WmanIfMaxMcaFlowType"""
    defaultValue = 0


_WmanIfBsCapCfgMcaFlowControl_Type.__name__ = "WmanIfMaxMcaFlowType"
_WmanIfBsCapCfgMcaFlowControl_Object = MibTableColumn
wmanIfBsCapCfgMcaFlowControl = _WmanIfBsCapCfgMcaFlowControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4, 1, 5),
    _WmanIfBsCapCfgMcaFlowControl_Type()
)
wmanIfBsCapCfgMcaFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgMcaFlowControl.setStatus("current")


class _WmanIfBsCapCfgMcpGroupCidSupport_Type(WmanIfMaxMcpGroupCid):
    """Custom type wmanIfBsCapCfgMcpGroupCidSupport based on WmanIfMaxMcpGroupCid"""
    defaultValue = 0


_WmanIfBsCapCfgMcpGroupCidSupport_Type.__name__ = "WmanIfMaxMcpGroupCid"
_WmanIfBsCapCfgMcpGroupCidSupport_Object = MibTableColumn
wmanIfBsCapCfgMcpGroupCidSupport = _WmanIfBsCapCfgMcpGroupCidSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4, 1, 6),
    _WmanIfBsCapCfgMcpGroupCidSupport_Type()
)
wmanIfBsCapCfgMcpGroupCidSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgMcpGroupCidSupport.setStatus("current")


class _WmanIfBsCapCfgPkmFlowControl_Type(WmanIfMaxPkmFlowType):
    """Custom type wmanIfBsCapCfgPkmFlowControl based on WmanIfMaxPkmFlowType"""
    defaultValue = 0


_WmanIfBsCapCfgPkmFlowControl_Type.__name__ = "WmanIfMaxPkmFlowType"
_WmanIfBsCapCfgPkmFlowControl_Object = MibTableColumn
wmanIfBsCapCfgPkmFlowControl = _WmanIfBsCapCfgPkmFlowControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4, 1, 7),
    _WmanIfBsCapCfgPkmFlowControl_Type()
)
wmanIfBsCapCfgPkmFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgPkmFlowControl.setStatus("current")
_WmanIfBsCapCfgAuthPolicyControl_Type = WmanIfAuthPolicyType
_WmanIfBsCapCfgAuthPolicyControl_Object = MibTableColumn
wmanIfBsCapCfgAuthPolicyControl = _WmanIfBsCapCfgAuthPolicyControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4, 1, 8),
    _WmanIfBsCapCfgAuthPolicyControl_Type()
)
wmanIfBsCapCfgAuthPolicyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgAuthPolicyControl.setStatus("current")


class _WmanIfBsCapCfgMaxNumOfSupportedSA_Type(WmanIfMaxNumOfSaType):
    """Custom type wmanIfBsCapCfgMaxNumOfSupportedSA based on WmanIfMaxNumOfSaType"""
    defaultValue = 1


_WmanIfBsCapCfgMaxNumOfSupportedSA_Type.__name__ = "WmanIfMaxNumOfSaType"
_WmanIfBsCapCfgMaxNumOfSupportedSA_Object = MibTableColumn
wmanIfBsCapCfgMaxNumOfSupportedSA = _WmanIfBsCapCfgMaxNumOfSupportedSA_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4, 1, 9),
    _WmanIfBsCapCfgMaxNumOfSupportedSA_Type()
)
wmanIfBsCapCfgMaxNumOfSupportedSA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgMaxNumOfSupportedSA.setStatus("current")
_WmanIfBsCapCfgIpVersion_Type = WmanIfIpVersionType
_WmanIfBsCapCfgIpVersion_Object = MibTableColumn
wmanIfBsCapCfgIpVersion = _WmanIfBsCapCfgIpVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4, 1, 10),
    _WmanIfBsCapCfgIpVersion_Type()
)
wmanIfBsCapCfgIpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgIpVersion.setStatus("current")
_WmanIfBsCapCfgMacCsSupportBitMap_Type = WmanIfMacCsBitMap
_WmanIfBsCapCfgMacCsSupportBitMap_Object = MibTableColumn
wmanIfBsCapCfgMacCsSupportBitMap = _WmanIfBsCapCfgMacCsSupportBitMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4, 1, 11),
    _WmanIfBsCapCfgMacCsSupportBitMap_Type()
)
wmanIfBsCapCfgMacCsSupportBitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgMacCsSupportBitMap.setStatus("current")


class _WmanIfBsCapCfgMaxNumOfClassifier_Type(WmanIfMaxClassifiers):
    """Custom type wmanIfBsCapCfgMaxNumOfClassifier based on WmanIfMaxClassifiers"""
    defaultValue = 0


_WmanIfBsCapCfgMaxNumOfClassifier_Type.__name__ = "WmanIfMaxClassifiers"
_WmanIfBsCapCfgMaxNumOfClassifier_Object = MibTableColumn
wmanIfBsCapCfgMaxNumOfClassifier = _WmanIfBsCapCfgMaxNumOfClassifier_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4, 1, 12),
    _WmanIfBsCapCfgMaxNumOfClassifier_Type()
)
wmanIfBsCapCfgMaxNumOfClassifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgMaxNumOfClassifier.setStatus("current")


class _WmanIfBsCapCfgPhsSupport_Type(WmanIfPhsSupportType):
    """Custom type wmanIfBsCapCfgPhsSupport based on WmanIfPhsSupportType"""
    defaultValue = 0


_WmanIfBsCapCfgPhsSupport_Type.__name__ = "WmanIfPhsSupportType"
_WmanIfBsCapCfgPhsSupport_Object = MibTableColumn
wmanIfBsCapCfgPhsSupport = _WmanIfBsCapCfgPhsSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4, 1, 13),
    _WmanIfBsCapCfgPhsSupport_Type()
)
wmanIfBsCapCfgPhsSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgPhsSupport.setStatus("current")
_WmanIfBsCapCfgBandwidthAllocSupport_Type = WmanIfBwAllocSupport
_WmanIfBsCapCfgBandwidthAllocSupport_Object = MibTableColumn
wmanIfBsCapCfgBandwidthAllocSupport = _WmanIfBsCapCfgBandwidthAllocSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4, 1, 14),
    _WmanIfBsCapCfgBandwidthAllocSupport_Type()
)
wmanIfBsCapCfgBandwidthAllocSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgBandwidthAllocSupport.setStatus("current")
_WmanIfBsCapCfgPduConstruction_Type = WmanIfPduConstruction
_WmanIfBsCapCfgPduConstruction_Object = MibTableColumn
wmanIfBsCapCfgPduConstruction = _WmanIfBsCapCfgPduConstruction_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4, 1, 15),
    _WmanIfBsCapCfgPduConstruction_Type()
)
wmanIfBsCapCfgPduConstruction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgPduConstruction.setStatus("current")
_WmanIfBsCapCfgTtgTransitionGap_Type = WmanIfSsTransitionGap
_WmanIfBsCapCfgTtgTransitionGap_Object = MibTableColumn
wmanIfBsCapCfgTtgTransitionGap = _WmanIfBsCapCfgTtgTransitionGap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4, 1, 16),
    _WmanIfBsCapCfgTtgTransitionGap_Type()
)
wmanIfBsCapCfgTtgTransitionGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgTtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgTtgTransitionGap.setUnits("us")
_WmanIfBsCapCfgRtgTransitionGap_Type = WmanIfSsTransitionGap
_WmanIfBsCapCfgRtgTransitionGap_Object = MibTableColumn
wmanIfBsCapCfgRtgTransitionGap = _WmanIfBsCapCfgRtgTransitionGap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 4, 4, 1, 17),
    _WmanIfBsCapCfgRtgTransitionGap_Type()
)
wmanIfBsCapCfgRtgTransitionGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgRtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsCapCfgRtgTransitionGap.setUnits("us")
_WmanIfBsSsActionsTable_Object = MibTable
wmanIfBsSsActionsTable = _WmanIfBsSsActionsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    wmanIfBsSsActionsTable.setStatus("current")
_WmanIfBsSsActionsEntry_Object = MibTableRow
wmanIfBsSsActionsEntry = _WmanIfBsSsActionsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 5, 1)
)
wmanIfBsSsActionsEntry.setIndexNames(
    (0, "WMAN-IF-MIB", "wmanIfBsSsActionsMacAddress"),
)
if mibBuilder.loadTexts:
    wmanIfBsSsActionsEntry.setStatus("current")
_WmanIfBsSsActionsMacAddress_Type = MacAddress
_WmanIfBsSsActionsMacAddress_Object = MibTableColumn
wmanIfBsSsActionsMacAddress = _WmanIfBsSsActionsMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 5, 1, 1),
    _WmanIfBsSsActionsMacAddress_Type()
)
wmanIfBsSsActionsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsSsActionsMacAddress.setStatus("current")


class _WmanIfBsSsActionsResetSs_Type(Integer32):
    """Custom type wmanIfBsSsActionsResetSs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("actionsResetSsNoAction", 0),
          ("actionsResetSs", 1))
    )


_WmanIfBsSsActionsResetSs_Type.__name__ = "Integer32"
_WmanIfBsSsActionsResetSs_Object = MibTableColumn
wmanIfBsSsActionsResetSs = _WmanIfBsSsActionsResetSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 5, 1, 2),
    _WmanIfBsSsActionsResetSs_Type()
)
wmanIfBsSsActionsResetSs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsSsActionsResetSs.setStatus("current")


class _WmanIfBsSsActionsAbortSs_Type(Integer32):
    """Custom type wmanIfBsSsActionsAbortSs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("actionsAbortSsNoAction", 0),
          ("actionsAbortSs", 1),
          ("actionAbortSsParams", 2))
    )


_WmanIfBsSsActionsAbortSs_Type.__name__ = "Integer32"
_WmanIfBsSsActionsAbortSs_Object = MibTableColumn
wmanIfBsSsActionsAbortSs = _WmanIfBsSsActionsAbortSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 5, 1, 3),
    _WmanIfBsSsActionsAbortSs_Type()
)
wmanIfBsSsActionsAbortSs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsSsActionsAbortSs.setStatus("current")
_WmanIfBsSsActionsOverrideDnFreq_Type = Unsigned32
_WmanIfBsSsActionsOverrideDnFreq_Object = MibTableColumn
wmanIfBsSsActionsOverrideDnFreq = _WmanIfBsSsActionsOverrideDnFreq_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 5, 1, 4),
    _WmanIfBsSsActionsOverrideDnFreq_Type()
)
wmanIfBsSsActionsOverrideDnFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsSsActionsOverrideDnFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSsActionsOverrideDnFreq.setUnits("kHz")


class _WmanIfBsSsActionsOverrideChannelId_Type(Integer32):
    """Custom type wmanIfBsSsActionsOverrideChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_WmanIfBsSsActionsOverrideChannelId_Type.__name__ = "Integer32"
_WmanIfBsSsActionsOverrideChannelId_Object = MibTableColumn
wmanIfBsSsActionsOverrideChannelId = _WmanIfBsSsActionsOverrideChannelId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 5, 1, 5),
    _WmanIfBsSsActionsOverrideChannelId_Type()
)
wmanIfBsSsActionsOverrideChannelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsSsActionsOverrideChannelId.setStatus("current")


class _WmanIfBsSsActionsDeReRegSs_Type(Integer32):
    """Custom type wmanIfBsSsActionsDeReRegSs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("actionsDeReRegSsNoAction", 0),
          ("actionsDeReRegSs", 1))
    )


_WmanIfBsSsActionsDeReRegSs_Type.__name__ = "Integer32"
_WmanIfBsSsActionsDeReRegSs_Object = MibTableColumn
wmanIfBsSsActionsDeReRegSs = _WmanIfBsSsActionsDeReRegSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 5, 1, 6),
    _WmanIfBsSsActionsDeReRegSs_Type()
)
wmanIfBsSsActionsDeReRegSs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsSsActionsDeReRegSs.setStatus("current")


class _WmanIfBsSsActionsDeReRegSsCode_Type(Integer32):
    """Custom type wmanIfBsSsActionsDeReRegSsCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("actionsDeReRegSsCodeChangeChan", 0),
          ("actionsDeReRegSsCodeNoTransmit", 1),
          ("actionsDeReRegSsCodeLtdTransmit", 2),
          ("actionsDeReRegSsCodeResume", 3))
    )


_WmanIfBsSsActionsDeReRegSsCode_Type.__name__ = "Integer32"
_WmanIfBsSsActionsDeReRegSsCode_Object = MibTableColumn
wmanIfBsSsActionsDeReRegSsCode = _WmanIfBsSsActionsDeReRegSsCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 5, 1, 7),
    _WmanIfBsSsActionsDeReRegSsCode_Type()
)
wmanIfBsSsActionsDeReRegSsCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsSsActionsDeReRegSsCode.setStatus("current")
_WmanIfBsSsActionsRowStatus_Type = RowStatus
_WmanIfBsSsActionsRowStatus_Object = MibTableColumn
wmanIfBsSsActionsRowStatus = _WmanIfBsSsActionsRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 5, 1, 8),
    _WmanIfBsSsActionsRowStatus_Type()
)
wmanIfBsSsActionsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsSsActionsRowStatus.setStatus("current")
_WmanIfBsPkmObjects_ObjectIdentity = ObjectIdentity
wmanIfBsPkmObjects = _WmanIfBsPkmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3)
)
_WmanIfBsPkmBaseTable_Object = MibTable
wmanIfBsPkmBaseTable = _WmanIfBsPkmBaseTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wmanIfBsPkmBaseTable.setStatus("current")
_WmanIfBsPkmBaseEntry_Object = MibTableRow
wmanIfBsPkmBaseEntry = _WmanIfBsPkmBaseEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1)
)
wmanIfBsPkmBaseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsPkmBaseEntry.setStatus("current")


class _WmanIfBsPkmDefaultAuthLifetime_Type(Integer32):
    """Custom type wmanIfBsPkmDefaultAuthLifetime based on Integer32"""
    defaultValue = 604800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(86400, 6048000),
    )


_WmanIfBsPkmDefaultAuthLifetime_Type.__name__ = "Integer32"
_WmanIfBsPkmDefaultAuthLifetime_Object = MibTableColumn
wmanIfBsPkmDefaultAuthLifetime = _WmanIfBsPkmDefaultAuthLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1, 1),
    _WmanIfBsPkmDefaultAuthLifetime_Type()
)
wmanIfBsPkmDefaultAuthLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsPkmDefaultAuthLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsPkmDefaultAuthLifetime.setUnits("seconds")


class _WmanIfBsPkmDefaultTekLifetime_Type(Integer32):
    """Custom type wmanIfBsPkmDefaultTekLifetime based on Integer32"""
    defaultValue = 43200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 604800),
    )


_WmanIfBsPkmDefaultTekLifetime_Type.__name__ = "Integer32"
_WmanIfBsPkmDefaultTekLifetime_Object = MibTableColumn
wmanIfBsPkmDefaultTekLifetime = _WmanIfBsPkmDefaultTekLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1, 2),
    _WmanIfBsPkmDefaultTekLifetime_Type()
)
wmanIfBsPkmDefaultTekLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsPkmDefaultTekLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsPkmDefaultTekLifetime.setUnits("seconds")


class _WmanIfBsPkmDefaultSelfSigManufCertTrust_Type(Integer32):
    """Custom type wmanIfBsPkmDefaultSelfSigManufCertTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 2))
    )


_WmanIfBsPkmDefaultSelfSigManufCertTrust_Type.__name__ = "Integer32"
_WmanIfBsPkmDefaultSelfSigManufCertTrust_Object = MibTableColumn
wmanIfBsPkmDefaultSelfSigManufCertTrust = _WmanIfBsPkmDefaultSelfSigManufCertTrust_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1, 3),
    _WmanIfBsPkmDefaultSelfSigManufCertTrust_Type()
)
wmanIfBsPkmDefaultSelfSigManufCertTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsPkmDefaultSelfSigManufCertTrust.setStatus("current")
_WmanIfBsPkmCheckCertValidityPeriods_Type = TruthValue
_WmanIfBsPkmCheckCertValidityPeriods_Object = MibTableColumn
wmanIfBsPkmCheckCertValidityPeriods = _WmanIfBsPkmCheckCertValidityPeriods_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1, 4),
    _WmanIfBsPkmCheckCertValidityPeriods_Type()
)
wmanIfBsPkmCheckCertValidityPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsPkmCheckCertValidityPeriods.setStatus("current")
_WmanIfBsPkmAuthentInfos_Type = Counter32
_WmanIfBsPkmAuthentInfos_Object = MibTableColumn
wmanIfBsPkmAuthentInfos = _WmanIfBsPkmAuthentInfos_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1, 5),
    _WmanIfBsPkmAuthentInfos_Type()
)
wmanIfBsPkmAuthentInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthentInfos.setStatus("current")
_WmanIfBsPkmAuthRequests_Type = Counter32
_WmanIfBsPkmAuthRequests_Object = MibTableColumn
wmanIfBsPkmAuthRequests = _WmanIfBsPkmAuthRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1, 6),
    _WmanIfBsPkmAuthRequests_Type()
)
wmanIfBsPkmAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthRequests.setStatus("current")
_WmanIfBsPkmAuthReplies_Type = Counter32
_WmanIfBsPkmAuthReplies_Object = MibTableColumn
wmanIfBsPkmAuthReplies = _WmanIfBsPkmAuthReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1, 7),
    _WmanIfBsPkmAuthReplies_Type()
)
wmanIfBsPkmAuthReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthReplies.setStatus("current")
_WmanIfBsPkmAuthRejects_Type = Counter32
_WmanIfBsPkmAuthRejects_Object = MibTableColumn
wmanIfBsPkmAuthRejects = _WmanIfBsPkmAuthRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1, 8),
    _WmanIfBsPkmAuthRejects_Type()
)
wmanIfBsPkmAuthRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthRejects.setStatus("current")
_WmanIfBsPkmAuthInvalids_Type = Counter32
_WmanIfBsPkmAuthInvalids_Object = MibTableColumn
wmanIfBsPkmAuthInvalids = _WmanIfBsPkmAuthInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1, 9),
    _WmanIfBsPkmAuthInvalids_Type()
)
wmanIfBsPkmAuthInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthInvalids.setStatus("current")
_WmanIfBsSsPkmAuthTable_Object = MibTable
wmanIfBsSsPkmAuthTable = _WmanIfBsSsPkmAuthTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthTable.setStatus("current")
_WmanIfBsSsPkmAuthEntry_Object = MibTableRow
wmanIfBsSsPkmAuthEntry = _WmanIfBsSsPkmAuthEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1)
)
wmanIfBsSsPkmAuthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfBsSsPkmAuthMacAddress"),
)
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthEntry.setStatus("current")
_WmanIfBsSsPkmAuthMacAddress_Type = MacAddress
_WmanIfBsSsPkmAuthMacAddress_Object = MibTableColumn
wmanIfBsSsPkmAuthMacAddress = _WmanIfBsSsPkmAuthMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 1),
    _WmanIfBsSsPkmAuthMacAddress_Type()
)
wmanIfBsSsPkmAuthMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthMacAddress.setStatus("current")


class _WmanIfBsSsPkmAuthKeySequenceNumber_Type(Integer32):
    """Custom type wmanIfBsSsPkmAuthKeySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIfBsSsPkmAuthKeySequenceNumber_Type.__name__ = "Integer32"
_WmanIfBsSsPkmAuthKeySequenceNumber_Object = MibTableColumn
wmanIfBsSsPkmAuthKeySequenceNumber = _WmanIfBsSsPkmAuthKeySequenceNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 2),
    _WmanIfBsSsPkmAuthKeySequenceNumber_Type()
)
wmanIfBsSsPkmAuthKeySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthKeySequenceNumber.setStatus("current")
_WmanIfBsSsPkmAuthExpiresOld_Type = DateAndTime
_WmanIfBsSsPkmAuthExpiresOld_Object = MibTableColumn
wmanIfBsSsPkmAuthExpiresOld = _WmanIfBsSsPkmAuthExpiresOld_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 3),
    _WmanIfBsSsPkmAuthExpiresOld_Type()
)
wmanIfBsSsPkmAuthExpiresOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthExpiresOld.setStatus("current")
_WmanIfBsSsPkmAuthExpiresNew_Type = DateAndTime
_WmanIfBsSsPkmAuthExpiresNew_Object = MibTableColumn
wmanIfBsSsPkmAuthExpiresNew = _WmanIfBsSsPkmAuthExpiresNew_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 4),
    _WmanIfBsSsPkmAuthExpiresNew_Type()
)
wmanIfBsSsPkmAuthExpiresNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthExpiresNew.setStatus("current")


class _WmanIfBsSsPkmAuthLifetime_Type(Integer32):
    """Custom type wmanIfBsSsPkmAuthLifetime based on Integer32"""
    defaultValue = 604800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(86400, 6048000),
    )


_WmanIfBsSsPkmAuthLifetime_Type.__name__ = "Integer32"
_WmanIfBsSsPkmAuthLifetime_Object = MibTableColumn
wmanIfBsSsPkmAuthLifetime = _WmanIfBsSsPkmAuthLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 5),
    _WmanIfBsSsPkmAuthLifetime_Type()
)
wmanIfBsSsPkmAuthLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthLifetime.setUnits("seconds")


class _WmanIfBsSsPkmAuthReset_Type(Integer32):
    """Custom type wmanIfBsSsPkmAuthReset based on Integer32"""
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
        *(("noResetRequested", 1),
          ("invalidateAuth", 2),
          ("sendAuthInvalid", 3),
          ("invalidateTeks", 4))
    )


_WmanIfBsSsPkmAuthReset_Type.__name__ = "Integer32"
_WmanIfBsSsPkmAuthReset_Object = MibTableColumn
wmanIfBsSsPkmAuthReset = _WmanIfBsSsPkmAuthReset_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 6),
    _WmanIfBsSsPkmAuthReset_Type()
)
wmanIfBsSsPkmAuthReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthReset.setStatus("current")
_WmanIfBsSsPkmAuthInfos_Type = Counter64
_WmanIfBsSsPkmAuthInfos_Object = MibTableColumn
wmanIfBsSsPkmAuthInfos = _WmanIfBsSsPkmAuthInfos_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 7),
    _WmanIfBsSsPkmAuthInfos_Type()
)
wmanIfBsSsPkmAuthInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthInfos.setStatus("current")
_WmanIfBsSsPkmAuthRequests_Type = Counter64
_WmanIfBsSsPkmAuthRequests_Object = MibTableColumn
wmanIfBsSsPkmAuthRequests = _WmanIfBsSsPkmAuthRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 8),
    _WmanIfBsSsPkmAuthRequests_Type()
)
wmanIfBsSsPkmAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthRequests.setStatus("current")
_WmanIfBsSsPkmAuthReplies_Type = Counter64
_WmanIfBsSsPkmAuthReplies_Object = MibTableColumn
wmanIfBsSsPkmAuthReplies = _WmanIfBsSsPkmAuthReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 9),
    _WmanIfBsSsPkmAuthReplies_Type()
)
wmanIfBsSsPkmAuthReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthReplies.setStatus("current")
_WmanIfBsSsPkmAuthRejects_Type = Counter64
_WmanIfBsSsPkmAuthRejects_Object = MibTableColumn
wmanIfBsSsPkmAuthRejects = _WmanIfBsSsPkmAuthRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 10),
    _WmanIfBsSsPkmAuthRejects_Type()
)
wmanIfBsSsPkmAuthRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthRejects.setStatus("current")
_WmanIfBsSsPkmAuthInvalids_Type = Counter64
_WmanIfBsSsPkmAuthInvalids_Object = MibTableColumn
wmanIfBsSsPkmAuthInvalids = _WmanIfBsSsPkmAuthInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 11),
    _WmanIfBsSsPkmAuthInvalids_Type()
)
wmanIfBsSsPkmAuthInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthInvalids.setStatus("current")


class _WmanIfBsSsPkmAuthRejectErrorCode_Type(Integer32):
    """Custom type wmanIfBsSsPkmAuthRejectErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noInformation", 0),
          ("unauthorizedSs", 1),
          ("unauthorizedSaid", 2),
          ("permanentAuthorizationFailure", 6))
    )


_WmanIfBsSsPkmAuthRejectErrorCode_Type.__name__ = "Integer32"
_WmanIfBsSsPkmAuthRejectErrorCode_Object = MibTableColumn
wmanIfBsSsPkmAuthRejectErrorCode = _WmanIfBsSsPkmAuthRejectErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 12),
    _WmanIfBsSsPkmAuthRejectErrorCode_Type()
)
wmanIfBsSsPkmAuthRejectErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthRejectErrorCode.setStatus("current")


class _WmanIfBsSsPkmAuthRejectErrorString_Type(SnmpAdminString):
    """Custom type wmanIfBsSsPkmAuthRejectErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WmanIfBsSsPkmAuthRejectErrorString_Type.__name__ = "SnmpAdminString"
_WmanIfBsSsPkmAuthRejectErrorString_Object = MibTableColumn
wmanIfBsSsPkmAuthRejectErrorString = _WmanIfBsSsPkmAuthRejectErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 13),
    _WmanIfBsSsPkmAuthRejectErrorString_Type()
)
wmanIfBsSsPkmAuthRejectErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthRejectErrorString.setStatus("current")


class _WmanIfBsSsPkmAuthInvalidErrorCode_Type(Integer32):
    """Custom type wmanIfBsSsPkmAuthInvalidErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noInformation", 0),
          ("unauthorizedSs", 1),
          ("unsolicited", 3),
          ("invalidKeySequence", 4),
          ("keyRequestAuthenticationFailure", 5))
    )


_WmanIfBsSsPkmAuthInvalidErrorCode_Type.__name__ = "Integer32"
_WmanIfBsSsPkmAuthInvalidErrorCode_Object = MibTableColumn
wmanIfBsSsPkmAuthInvalidErrorCode = _WmanIfBsSsPkmAuthInvalidErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 14),
    _WmanIfBsSsPkmAuthInvalidErrorCode_Type()
)
wmanIfBsSsPkmAuthInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthInvalidErrorCode.setStatus("current")


class _WmanIfBsSsPkmAuthInvalidErrorString_Type(SnmpAdminString):
    """Custom type wmanIfBsSsPkmAuthInvalidErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WmanIfBsSsPkmAuthInvalidErrorString_Type.__name__ = "SnmpAdminString"
_WmanIfBsSsPkmAuthInvalidErrorString_Object = MibTableColumn
wmanIfBsSsPkmAuthInvalidErrorString = _WmanIfBsSsPkmAuthInvalidErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 15),
    _WmanIfBsSsPkmAuthInvalidErrorString_Type()
)
wmanIfBsSsPkmAuthInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthInvalidErrorString.setStatus("current")


class _WmanIfBsSsPkmAuthPrimarySAId_Type(Integer32):
    """Custom type wmanIfBsSsPkmAuthPrimarySAId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsSsPkmAuthPrimarySAId_Type.__name__ = "Integer32"
_WmanIfBsSsPkmAuthPrimarySAId_Object = MibTableColumn
wmanIfBsSsPkmAuthPrimarySAId = _WmanIfBsSsPkmAuthPrimarySAId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 16),
    _WmanIfBsSsPkmAuthPrimarySAId_Type()
)
wmanIfBsSsPkmAuthPrimarySAId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthPrimarySAId.setStatus("current")


class _WmanIfBsSsPkmAuthValidStatus_Type(Integer32):
    """Custom type wmanIfBsSsPkmAuthValidStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("validSsChained", 1),
          ("validSsTrusted", 2),
          ("invalidSsUntrusted", 3),
          ("invalidCAUntrusted", 4),
          ("invalidSsOther", 5),
          ("invalidCAOther", 6))
    )


_WmanIfBsSsPkmAuthValidStatus_Type.__name__ = "Integer32"
_WmanIfBsSsPkmAuthValidStatus_Object = MibTableColumn
wmanIfBsSsPkmAuthValidStatus = _WmanIfBsSsPkmAuthValidStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 17),
    _WmanIfBsSsPkmAuthValidStatus_Type()
)
wmanIfBsSsPkmAuthValidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmAuthValidStatus.setStatus("current")
_WmanIfBsPkmTekTable_Object = MibTable
wmanIfBsPkmTekTable = _WmanIfBsPkmTekTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    wmanIfBsPkmTekTable.setStatus("current")
_WmanIfBsPkmTekEntry_Object = MibTableRow
wmanIfBsPkmTekEntry = _WmanIfBsPkmTekEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1)
)
wmanIfBsPkmTekEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfBsPkmTekSAId"),
)
if mibBuilder.loadTexts:
    wmanIfBsPkmTekEntry.setStatus("current")


class _WmanIfBsPkmTekSAId_Type(Integer32):
    """Custom type wmanIfBsPkmTekSAId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsPkmTekSAId_Type.__name__ = "Integer32"
_WmanIfBsPkmTekSAId_Object = MibTableColumn
wmanIfBsPkmTekSAId = _WmanIfBsPkmTekSAId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 1),
    _WmanIfBsPkmTekSAId_Type()
)
wmanIfBsPkmTekSAId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsPkmTekSAId.setStatus("current")


class _WmanIfBsPkmTekSAType_Type(Integer32):
    """Custom type wmanIfBsPkmTekSAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primarySA", 0),
          ("staticSA", 1),
          ("dynamicSA", 2))
    )


_WmanIfBsPkmTekSAType_Type.__name__ = "Integer32"
_WmanIfBsPkmTekSAType_Object = MibTableColumn
wmanIfBsPkmTekSAType = _WmanIfBsPkmTekSAType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 2),
    _WmanIfBsPkmTekSAType_Type()
)
wmanIfBsPkmTekSAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTekSAType.setStatus("current")
_WmanIfBsPkmTekDataEncryptAlg_Type = WmanIfDataEncryptAlgId
_WmanIfBsPkmTekDataEncryptAlg_Object = MibTableColumn
wmanIfBsPkmTekDataEncryptAlg = _WmanIfBsPkmTekDataEncryptAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 3),
    _WmanIfBsPkmTekDataEncryptAlg_Type()
)
wmanIfBsPkmTekDataEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTekDataEncryptAlg.setStatus("current")
_WmanIfBsPkmTekDataAuthentAlg_Type = WmanIfDataAuthAlgId
_WmanIfBsPkmTekDataAuthentAlg_Object = MibTableColumn
wmanIfBsPkmTekDataAuthentAlg = _WmanIfBsPkmTekDataAuthentAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 4),
    _WmanIfBsPkmTekDataAuthentAlg_Type()
)
wmanIfBsPkmTekDataAuthentAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTekDataAuthentAlg.setStatus("current")
_WmanIfBsPkmTekEncryptAlg_Type = WmanIfTekEncryptAlgId
_WmanIfBsPkmTekEncryptAlg_Object = MibTableColumn
wmanIfBsPkmTekEncryptAlg = _WmanIfBsPkmTekEncryptAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 5),
    _WmanIfBsPkmTekEncryptAlg_Type()
)
wmanIfBsPkmTekEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTekEncryptAlg.setStatus("current")


class _WmanIfBsPkmTekLifetime_Type(Integer32):
    """Custom type wmanIfBsPkmTekLifetime based on Integer32"""
    defaultValue = 43200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 604800),
    )


_WmanIfBsPkmTekLifetime_Type.__name__ = "Integer32"
_WmanIfBsPkmTekLifetime_Object = MibTableColumn
wmanIfBsPkmTekLifetime = _WmanIfBsPkmTekLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 6),
    _WmanIfBsPkmTekLifetime_Type()
)
wmanIfBsPkmTekLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTekLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsPkmTekLifetime.setUnits("seconds")


class _WmanIfBsPkmTekKeySequenceNumber_Type(Integer32):
    """Custom type wmanIfBsPkmTekKeySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WmanIfBsPkmTekKeySequenceNumber_Type.__name__ = "Integer32"
_WmanIfBsPkmTekKeySequenceNumber_Object = MibTableColumn
wmanIfBsPkmTekKeySequenceNumber = _WmanIfBsPkmTekKeySequenceNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 7),
    _WmanIfBsPkmTekKeySequenceNumber_Type()
)
wmanIfBsPkmTekKeySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTekKeySequenceNumber.setStatus("current")
_WmanIfBsPkmTekExpiresOld_Type = DateAndTime
_WmanIfBsPkmTekExpiresOld_Object = MibTableColumn
wmanIfBsPkmTekExpiresOld = _WmanIfBsPkmTekExpiresOld_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 8),
    _WmanIfBsPkmTekExpiresOld_Type()
)
wmanIfBsPkmTekExpiresOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTekExpiresOld.setStatus("current")
_WmanIfBsPkmTekExpiresNew_Type = DateAndTime
_WmanIfBsPkmTekExpiresNew_Object = MibTableColumn
wmanIfBsPkmTekExpiresNew = _WmanIfBsPkmTekExpiresNew_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 9),
    _WmanIfBsPkmTekExpiresNew_Type()
)
wmanIfBsPkmTekExpiresNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTekExpiresNew.setStatus("current")
_WmanIfBsPkmTekReset_Type = TruthValue
_WmanIfBsPkmTekReset_Object = MibTableColumn
wmanIfBsPkmTekReset = _WmanIfBsPkmTekReset_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 10),
    _WmanIfBsPkmTekReset_Type()
)
wmanIfBsPkmTekReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsPkmTekReset.setStatus("current")
_WmanIfBsPkmKeyRequests_Type = Counter32
_WmanIfBsPkmKeyRequests_Object = MibTableColumn
wmanIfBsPkmKeyRequests = _WmanIfBsPkmKeyRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 11),
    _WmanIfBsPkmKeyRequests_Type()
)
wmanIfBsPkmKeyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmKeyRequests.setStatus("current")
_WmanIfBsPkmKeyReplies_Type = Counter32
_WmanIfBsPkmKeyReplies_Object = MibTableColumn
wmanIfBsPkmKeyReplies = _WmanIfBsPkmKeyReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 12),
    _WmanIfBsPkmKeyReplies_Type()
)
wmanIfBsPkmKeyReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmKeyReplies.setStatus("current")
_WmanIfBsPkmKeyRejects_Type = Counter32
_WmanIfBsPkmKeyRejects_Object = MibTableColumn
wmanIfBsPkmKeyRejects = _WmanIfBsPkmKeyRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 13),
    _WmanIfBsPkmKeyRejects_Type()
)
wmanIfBsPkmKeyRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmKeyRejects.setStatus("current")
_WmanIfBsPkmTekInvalids_Type = Counter32
_WmanIfBsPkmTekInvalids_Object = MibTableColumn
wmanIfBsPkmTekInvalids = _WmanIfBsPkmTekInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 14),
    _WmanIfBsPkmTekInvalids_Type()
)
wmanIfBsPkmTekInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTekInvalids.setStatus("current")


class _WmanIfBsPkmKeyRejectErrorCode_Type(Integer32):
    """Custom type wmanIfBsPkmKeyRejectErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noInformation", 0),
          ("unauthorizedSaid", 2))
    )


_WmanIfBsPkmKeyRejectErrorCode_Type.__name__ = "Integer32"
_WmanIfBsPkmKeyRejectErrorCode_Object = MibTableColumn
wmanIfBsPkmKeyRejectErrorCode = _WmanIfBsPkmKeyRejectErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 15),
    _WmanIfBsPkmKeyRejectErrorCode_Type()
)
wmanIfBsPkmKeyRejectErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmKeyRejectErrorCode.setStatus("current")


class _WmanIfBsPkmKeyRejectErrorString_Type(SnmpAdminString):
    """Custom type wmanIfBsPkmKeyRejectErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WmanIfBsPkmKeyRejectErrorString_Type.__name__ = "SnmpAdminString"
_WmanIfBsPkmKeyRejectErrorString_Object = MibTableColumn
wmanIfBsPkmKeyRejectErrorString = _WmanIfBsPkmKeyRejectErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 16),
    _WmanIfBsPkmKeyRejectErrorString_Type()
)
wmanIfBsPkmKeyRejectErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmKeyRejectErrorString.setStatus("current")


class _WmanIfBsPkmTekInvalidErrorCode_Type(Integer32):
    """Custom type wmanIfBsPkmTekInvalidErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noInformation", 0),
          ("invalidKeySequence", 4))
    )


_WmanIfBsPkmTekInvalidErrorCode_Type.__name__ = "Integer32"
_WmanIfBsPkmTekInvalidErrorCode_Object = MibTableColumn
wmanIfBsPkmTekInvalidErrorCode = _WmanIfBsPkmTekInvalidErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 17),
    _WmanIfBsPkmTekInvalidErrorCode_Type()
)
wmanIfBsPkmTekInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTekInvalidErrorCode.setStatus("current")


class _WmanIfBsPkmTekInvalidErrorString_Type(SnmpAdminString):
    """Custom type wmanIfBsPkmTekInvalidErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WmanIfBsPkmTekInvalidErrorString_Type.__name__ = "SnmpAdminString"
_WmanIfBsPkmTekInvalidErrorString_Object = MibTableColumn
wmanIfBsPkmTekInvalidErrorString = _WmanIfBsPkmTekInvalidErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 18),
    _WmanIfBsPkmTekInvalidErrorString_Type()
)
wmanIfBsPkmTekInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTekInvalidErrorString.setStatus("current")
_WmanIfBsNotification_ObjectIdentity = ObjectIdentity
wmanIfBsNotification = _WmanIfBsNotification_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4)
)
_WmanIfBsTrapControl_ObjectIdentity = ObjectIdentity
wmanIfBsTrapControl = _WmanIfBsTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1)
)


class _WmanIfBsTrapControlRegister_Type(Bits):
    """Custom type wmanIfBsTrapControlRegister based on Bits"""
    namedValues = NamedValues(
        *(("wmanIfBsSsStatusNotification", 0),
          ("wmanIfBsSsDynamicServiceFail", 1),
          ("wmanIfBsSsRssiStatusChange", 2),
          ("wmanIfBsSsRegistrer", 3),
          ("wmanIfBsSsPkmFail", 4))
    )

_WmanIfBsTrapControlRegister_Type.__name__ = "Bits"
_WmanIfBsTrapControlRegister_Object = MibScalar
wmanIfBsTrapControlRegister = _WmanIfBsTrapControlRegister_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 1),
    _WmanIfBsTrapControlRegister_Type()
)
wmanIfBsTrapControlRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsTrapControlRegister.setStatus("current")


class _WmanIfBsStatusTrapControlRegister_Type(Bits):
    """Custom type wmanIfBsStatusTrapControlRegister based on Bits"""
    namedValues = NamedValues(
        *(("unused", 0),
          ("ssInitRangingSucc", 1),
          ("ssInitRangingFail", 2),
          ("ssRegistered", 3),
          ("ssRegistrationFail", 4),
          ("ssDeregistered", 5),
          ("ssBasicCapabilitySucc", 6),
          ("ssBasicCapabilityFail", 7),
          ("ssAuthorizationSucc", 8),
          ("ssAuthorizationFail", 9),
          ("tftpSucc", 10),
          ("tftpFail", 11),
          ("sfCreationSucc", 12),
          ("sfCreationFail", 13))
    )

_WmanIfBsStatusTrapControlRegister_Type.__name__ = "Bits"
_WmanIfBsStatusTrapControlRegister_Object = MibScalar
wmanIfBsStatusTrapControlRegister = _WmanIfBsStatusTrapControlRegister_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 2),
    _WmanIfBsStatusTrapControlRegister_Type()
)
wmanIfBsStatusTrapControlRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsStatusTrapControlRegister.setStatus("current")
_WmanIfBsThresholdConfigTable_Object = MibTable
wmanIfBsThresholdConfigTable = _WmanIfBsThresholdConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    wmanIfBsThresholdConfigTable.setStatus("current")
_WmanIfBsThresholdConfigEntry_Object = MibTableRow
wmanIfBsThresholdConfigEntry = _WmanIfBsThresholdConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 3, 1)
)
wmanIfBsThresholdConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsThresholdConfigEntry.setStatus("current")
_WmanIfBsRssiLowThreshold_Type = Integer32
_WmanIfBsRssiLowThreshold_Object = MibTableColumn
wmanIfBsRssiLowThreshold = _WmanIfBsRssiLowThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 3, 1, 1),
    _WmanIfBsRssiLowThreshold_Type()
)
wmanIfBsRssiLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsRssiLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsRssiLowThreshold.setUnits("dBm")
_WmanIfBsRssiHighThreshold_Type = Integer32
_WmanIfBsRssiHighThreshold_Object = MibTableColumn
wmanIfBsRssiHighThreshold = _WmanIfBsRssiHighThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 3, 1, 2),
    _WmanIfBsRssiHighThreshold_Type()
)
wmanIfBsRssiHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsRssiHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsRssiHighThreshold.setUnits("dBm")
_WmanIfBsTrapDefinitions_ObjectIdentity = ObjectIdentity
wmanIfBsTrapDefinitions = _WmanIfBsTrapDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2)
)
_WmanIfBsTrapPrefix_ObjectIdentity = ObjectIdentity
wmanIfBsTrapPrefix = _WmanIfBsTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2, 0)
)
_WmanIfBsSsNotificationObjectsTable_Object = MibTable
wmanIfBsSsNotificationObjectsTable = _WmanIfBsSsNotificationObjectsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIfBsSsNotificationObjectsTable.setStatus("current")
_WmanIfBsSsNotificationObjectsEntry_Object = MibTableRow
wmanIfBsSsNotificationObjectsEntry = _WmanIfBsSsNotificationObjectsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2, 1, 1)
)
wmanIfBsSsNotificationObjectsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfBsSsNotificationMacAddr"),
)
if mibBuilder.loadTexts:
    wmanIfBsSsNotificationObjectsEntry.setStatus("current")
_WmanIfBsSsNotificationMacAddr_Type = MacAddress
_WmanIfBsSsNotificationMacAddr_Object = MibTableColumn
wmanIfBsSsNotificationMacAddr = _WmanIfBsSsNotificationMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2, 1, 1, 1),
    _WmanIfBsSsNotificationMacAddr_Type()
)
wmanIfBsSsNotificationMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsNotificationMacAddr.setStatus("current")


class _WmanIfBsSsStatusValue_Type(Integer32):
    """Custom type wmanIfBsSsStatusValue based on Integer32"""
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
        *(("ssInitRangingSucc", 1),
          ("ssInitRangingFail", 2),
          ("ssRegistered", 3),
          ("ssRegistrationFail", 4),
          ("ssDeregistered", 5),
          ("ssBasicCapabilitySucc", 6),
          ("ssBasicCapabilityFail", 7),
          ("ssAuthorizationSucc", 8),
          ("ssAuthorizationFail", 9),
          ("tftpSucc", 10),
          ("tftpFail", 11),
          ("sfCreationSucc", 12),
          ("sfCreationFail", 13))
    )


_WmanIfBsSsStatusValue_Type.__name__ = "Integer32"
_WmanIfBsSsStatusValue_Object = MibTableColumn
wmanIfBsSsStatusValue = _WmanIfBsSsStatusValue_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2, 1, 1, 2),
    _WmanIfBsSsStatusValue_Type()
)
wmanIfBsSsStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsStatusValue.setStatus("current")


class _WmanIfBsSsStatusInfo_Type(OctetString):
    """Custom type wmanIfBsSsStatusInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WmanIfBsSsStatusInfo_Type.__name__ = "OctetString"
_WmanIfBsSsStatusInfo_Object = MibTableColumn
wmanIfBsSsStatusInfo = _WmanIfBsSsStatusInfo_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2, 1, 1, 3),
    _WmanIfBsSsStatusInfo_Type()
)
wmanIfBsSsStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsStatusInfo.setStatus("current")


class _WmanIfBsDynamicServiceType_Type(Integer32):
    """Custom type wmanIfBsDynamicServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bsSfCreationReq", 1),
          ("bsSfCreationRsp", 2),
          ("bsSfCreationAck", 3))
    )


_WmanIfBsDynamicServiceType_Type.__name__ = "Integer32"
_WmanIfBsDynamicServiceType_Object = MibTableColumn
wmanIfBsDynamicServiceType = _WmanIfBsDynamicServiceType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2, 1, 1, 4),
    _WmanIfBsDynamicServiceType_Type()
)
wmanIfBsDynamicServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsDynamicServiceType.setStatus("current")


class _WmanIfBsDynamicServiceFailReason_Type(OctetString):
    """Custom type wmanIfBsDynamicServiceFailReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WmanIfBsDynamicServiceFailReason_Type.__name__ = "OctetString"
_WmanIfBsDynamicServiceFailReason_Object = MibTableColumn
wmanIfBsDynamicServiceFailReason = _WmanIfBsDynamicServiceFailReason_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2, 1, 1, 5),
    _WmanIfBsDynamicServiceFailReason_Type()
)
wmanIfBsDynamicServiceFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsDynamicServiceFailReason.setStatus("current")


class _WmanIfBsSsRssiStatus_Type(Integer32):
    """Custom type wmanIfBsSsRssiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bsRssiAlarm", 1),
          ("bsRssiNoAlarm", 2))
    )


_WmanIfBsSsRssiStatus_Type.__name__ = "Integer32"
_WmanIfBsSsRssiStatus_Object = MibTableColumn
wmanIfBsSsRssiStatus = _WmanIfBsSsRssiStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2, 1, 1, 6),
    _WmanIfBsSsRssiStatus_Type()
)
wmanIfBsSsRssiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRssiStatus.setStatus("current")


class _WmanIfBsSsRssiStatusInfo_Type(OctetString):
    """Custom type wmanIfBsSsRssiStatusInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WmanIfBsSsRssiStatusInfo_Type.__name__ = "OctetString"
_WmanIfBsSsRssiStatusInfo_Object = MibTableColumn
wmanIfBsSsRssiStatusInfo = _WmanIfBsSsRssiStatusInfo_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2, 1, 1, 7),
    _WmanIfBsSsRssiStatusInfo_Type()
)
wmanIfBsSsRssiStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRssiStatusInfo.setStatus("current")


class _WmanIfBsSsRegisterStatus_Type(Integer32):
    """Custom type wmanIfBsSsRegisterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ssRegister", 1),
          ("ssDeregister", 2))
    )


_WmanIfBsSsRegisterStatus_Type.__name__ = "Integer32"
_WmanIfBsSsRegisterStatus_Object = MibTableColumn
wmanIfBsSsRegisterStatus = _WmanIfBsSsRegisterStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2, 1, 1, 8),
    _WmanIfBsSsRegisterStatus_Type()
)
wmanIfBsSsRegisterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRegisterStatus.setStatus("current")
_WmanIfBsPhy_ObjectIdentity = ObjectIdentity
wmanIfBsPhy = _WmanIfBsPhy_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6)
)
_WmanIfBsOfdmPhy_ObjectIdentity = ObjectIdentity
wmanIfBsOfdmPhy = _WmanIfBsOfdmPhy_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1)
)
_WmanIfBsOfdmUplinkChannelTable_Object = MibTable
wmanIfBsOfdmUplinkChannelTable = _WmanIfBsOfdmUplinkChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmUplinkChannelTable.setStatus("current")
_WmanIfBsOfdmUplinkChannelEntry_Object = MibTableRow
wmanIfBsOfdmUplinkChannelEntry = _WmanIfBsOfdmUplinkChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 1, 1)
)
wmanIfBsOfdmUplinkChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmUplinkChannelEntry.setStatus("current")


class _WmanIfBsOfdmCtBasedResvTimeout_Type(Integer32):
    """Custom type wmanIfBsOfdmCtBasedResvTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WmanIfBsOfdmCtBasedResvTimeout_Type.__name__ = "Integer32"
_WmanIfBsOfdmCtBasedResvTimeout_Object = MibTableColumn
wmanIfBsOfdmCtBasedResvTimeout = _WmanIfBsOfdmCtBasedResvTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 1, 1, 1),
    _WmanIfBsOfdmCtBasedResvTimeout_Type()
)
wmanIfBsOfdmCtBasedResvTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmCtBasedResvTimeout.setStatus("current")


class _WmanIfBsOfdmBwReqOppSize_Type(Integer32):
    """Custom type wmanIfBsOfdmBwReqOppSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIfBsOfdmBwReqOppSize_Type.__name__ = "Integer32"
_WmanIfBsOfdmBwReqOppSize_Object = MibTableColumn
wmanIfBsOfdmBwReqOppSize = _WmanIfBsOfdmBwReqOppSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 1, 1, 2),
    _WmanIfBsOfdmBwReqOppSize_Type()
)
wmanIfBsOfdmBwReqOppSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmBwReqOppSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmBwReqOppSize.setUnits("PS")


class _WmanIfBsOfdmRangReqOppSize_Type(Integer32):
    """Custom type wmanIfBsOfdmRangReqOppSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIfBsOfdmRangReqOppSize_Type.__name__ = "Integer32"
_WmanIfBsOfdmRangReqOppSize_Object = MibTableColumn
wmanIfBsOfdmRangReqOppSize = _WmanIfBsOfdmRangReqOppSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 1, 1, 3),
    _WmanIfBsOfdmRangReqOppSize_Type()
)
wmanIfBsOfdmRangReqOppSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmRangReqOppSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmRangReqOppSize.setUnits("PS")
_WmanIfBsOfdmUplinkCenterFreq_Type = Unsigned32
_WmanIfBsOfdmUplinkCenterFreq_Object = MibTableColumn
wmanIfBsOfdmUplinkCenterFreq = _WmanIfBsOfdmUplinkCenterFreq_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 1, 1, 4),
    _WmanIfBsOfdmUplinkCenterFreq_Type()
)
wmanIfBsOfdmUplinkCenterFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmUplinkCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmUplinkCenterFreq.setUnits("kHz")


class _WmanIfBsOfdmNumSubChReqRegionFull_Type(Integer32):
    """Custom type wmanIfBsOfdmNumSubChReqRegionFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("oneSubchannel", 0),
          ("twoSubchannels", 1),
          ("fourSubchannels", 2),
          ("eightSubchannels", 3),
          ("sixteenSubchannels", 4))
    )


_WmanIfBsOfdmNumSubChReqRegionFull_Type.__name__ = "Integer32"
_WmanIfBsOfdmNumSubChReqRegionFull_Object = MibTableColumn
wmanIfBsOfdmNumSubChReqRegionFull = _WmanIfBsOfdmNumSubChReqRegionFull_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 1, 1, 5),
    _WmanIfBsOfdmNumSubChReqRegionFull_Type()
)
wmanIfBsOfdmNumSubChReqRegionFull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmNumSubChReqRegionFull.setStatus("current")


class _WmanIfBsOfdmNumSymbolsReqRegionFull_Type(Integer32):
    """Custom type wmanIfBsOfdmNumSymbolsReqRegionFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_WmanIfBsOfdmNumSymbolsReqRegionFull_Type.__name__ = "Integer32"
_WmanIfBsOfdmNumSymbolsReqRegionFull_Object = MibTableColumn
wmanIfBsOfdmNumSymbolsReqRegionFull = _WmanIfBsOfdmNumSymbolsReqRegionFull_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 1, 1, 6),
    _WmanIfBsOfdmNumSymbolsReqRegionFull_Type()
)
wmanIfBsOfdmNumSymbolsReqRegionFull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmNumSymbolsReqRegionFull.setStatus("current")


class _WmanIfBsOfdmSubChFocusCtCode_Type(Integer32):
    """Custom type wmanIfBsOfdmSubChFocusCtCode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_WmanIfBsOfdmSubChFocusCtCode_Type.__name__ = "Integer32"
_WmanIfBsOfdmSubChFocusCtCode_Object = MibTableColumn
wmanIfBsOfdmSubChFocusCtCode = _WmanIfBsOfdmSubChFocusCtCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 1, 1, 7),
    _WmanIfBsOfdmSubChFocusCtCode_Type()
)
wmanIfBsOfdmSubChFocusCtCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmSubChFocusCtCode.setStatus("current")


class _WmanIfBsOfdmUpLinkChannelId_Type(Integer32):
    """Custom type wmanIfBsOfdmUpLinkChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmUpLinkChannelId_Type.__name__ = "Integer32"
_WmanIfBsOfdmUpLinkChannelId_Object = MibTableColumn
wmanIfBsOfdmUpLinkChannelId = _WmanIfBsOfdmUpLinkChannelId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 1, 1, 8),
    _WmanIfBsOfdmUpLinkChannelId_Type()
)
wmanIfBsOfdmUpLinkChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmUpLinkChannelId.setStatus("current")
_WmanIfBsOfdmDownlinkChannelTable_Object = MibTable
wmanIfBsOfdmDownlinkChannelTable = _WmanIfBsOfdmDownlinkChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmDownlinkChannelTable.setStatus("current")
_WmanIfBsOfdmDownlinkChannelEntry_Object = MibTableRow
wmanIfBsOfdmDownlinkChannelEntry = _WmanIfBsOfdmDownlinkChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 2, 1)
)
wmanIfBsOfdmDownlinkChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmDownlinkChannelEntry.setStatus("current")


class _WmanIfBsOfdmBsEIRP_Type(Integer32):
    """Custom type wmanIfBsOfdmBsEIRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsOfdmBsEIRP_Type.__name__ = "Integer32"
_WmanIfBsOfdmBsEIRP_Object = MibTableColumn
wmanIfBsOfdmBsEIRP = _WmanIfBsOfdmBsEIRP_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 2, 1, 1),
    _WmanIfBsOfdmBsEIRP_Type()
)
wmanIfBsOfdmBsEIRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmBsEIRP.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmBsEIRP.setUnits("dBm")
_WmanIfBsOfdmChannelNumber_Type = WmanIfChannelNumber
_WmanIfBsOfdmChannelNumber_Object = MibTableColumn
wmanIfBsOfdmChannelNumber = _WmanIfBsOfdmChannelNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 2, 1, 2),
    _WmanIfBsOfdmChannelNumber_Type()
)
wmanIfBsOfdmChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmChannelNumber.setStatus("current")


class _WmanIfBsOfdmTTG_Type(Integer32):
    """Custom type wmanIfBsOfdmTTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmTTG_Type.__name__ = "Integer32"
_WmanIfBsOfdmTTG_Object = MibTableColumn
wmanIfBsOfdmTTG = _WmanIfBsOfdmTTG_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 2, 1, 3),
    _WmanIfBsOfdmTTG_Type()
)
wmanIfBsOfdmTTG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmTTG.setStatus("current")


class _WmanIfBsOfdmRTG_Type(Integer32):
    """Custom type wmanIfBsOfdmRTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmRTG_Type.__name__ = "Integer32"
_WmanIfBsOfdmRTG_Object = MibTableColumn
wmanIfBsOfdmRTG = _WmanIfBsOfdmRTG_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 2, 1, 4),
    _WmanIfBsOfdmRTG_Type()
)
wmanIfBsOfdmRTG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmRTG.setStatus("current")


class _WmanIfBsOfdmInitRngMaxRSS_Type(Integer32):
    """Custom type wmanIfBsOfdmInitRngMaxRSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsOfdmInitRngMaxRSS_Type.__name__ = "Integer32"
_WmanIfBsOfdmInitRngMaxRSS_Object = MibTableColumn
wmanIfBsOfdmInitRngMaxRSS = _WmanIfBsOfdmInitRngMaxRSS_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 2, 1, 5),
    _WmanIfBsOfdmInitRngMaxRSS_Type()
)
wmanIfBsOfdmInitRngMaxRSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmInitRngMaxRSS.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmInitRngMaxRSS.setUnits("dBm")
_WmanIfBsOfdmDownlinkCenterFreq_Type = Unsigned32
_WmanIfBsOfdmDownlinkCenterFreq_Object = MibTableColumn
wmanIfBsOfdmDownlinkCenterFreq = _WmanIfBsOfdmDownlinkCenterFreq_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 2, 1, 6),
    _WmanIfBsOfdmDownlinkCenterFreq_Type()
)
wmanIfBsOfdmDownlinkCenterFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmDownlinkCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmDownlinkCenterFreq.setUnits("kHz")
_WmanIfBsOfdmBsId_Type = WmanIfBsIdType
_WmanIfBsOfdmBsId_Object = MibTableColumn
wmanIfBsOfdmBsId = _WmanIfBsOfdmBsId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 2, 1, 7),
    _WmanIfBsOfdmBsId_Type()
)
wmanIfBsOfdmBsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmBsId.setStatus("current")
_WmanIfBsOfdmMacVersion_Type = WmanIfMacVersion
_WmanIfBsOfdmMacVersion_Object = MibTableColumn
wmanIfBsOfdmMacVersion = _WmanIfBsOfdmMacVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 2, 1, 8),
    _WmanIfBsOfdmMacVersion_Type()
)
wmanIfBsOfdmMacVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmMacVersion.setStatus("current")


class _WmanIfBsOfdmFrameDurationCode_Type(Integer32):
    """Custom type wmanIfBsOfdmFrameDurationCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("duration2dot5ms", 0),
          ("duration4ms", 1),
          ("duration5ms", 2),
          ("duration8ms", 3),
          ("duration10ms", 4),
          ("duration12dot5ms", 5),
          ("duration20ms", 6))
    )


_WmanIfBsOfdmFrameDurationCode_Type.__name__ = "Integer32"
_WmanIfBsOfdmFrameDurationCode_Object = MibTableColumn
wmanIfBsOfdmFrameDurationCode = _WmanIfBsOfdmFrameDurationCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 2, 1, 9),
    _WmanIfBsOfdmFrameDurationCode_Type()
)
wmanIfBsOfdmFrameDurationCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmFrameDurationCode.setStatus("current")


class _WmanIfBsOfdmDownLinkChannelId_Type(Integer32):
    """Custom type wmanIfBsOfdmDownLinkChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmDownLinkChannelId_Type.__name__ = "Integer32"
_WmanIfBsOfdmDownLinkChannelId_Object = MibTableColumn
wmanIfBsOfdmDownLinkChannelId = _WmanIfBsOfdmDownLinkChannelId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 2, 1, 10),
    _WmanIfBsOfdmDownLinkChannelId_Type()
)
wmanIfBsOfdmDownLinkChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmDownLinkChannelId.setStatus("current")
_WmanIfBsOfdmUcdBurstProfileTable_Object = MibTable
wmanIfBsOfdmUcdBurstProfileTable = _WmanIfBsOfdmUcdBurstProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 3)
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmUcdBurstProfileTable.setStatus("current")
_WmanIfBsOfdmUcdBurstProfileEntry_Object = MibTableRow
wmanIfBsOfdmUcdBurstProfileEntry = _WmanIfBsOfdmUcdBurstProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 3, 1)
)
wmanIfBsOfdmUcdBurstProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfBsOfdmUiucIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmUcdBurstProfileEntry.setStatus("current")


class _WmanIfBsOfdmUiucIndex_Type(Integer32):
    """Custom type wmanIfBsOfdmUiucIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_WmanIfBsOfdmUiucIndex_Type.__name__ = "Integer32"
_WmanIfBsOfdmUiucIndex_Object = MibTableColumn
wmanIfBsOfdmUiucIndex = _WmanIfBsOfdmUiucIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 3, 1, 1),
    _WmanIfBsOfdmUiucIndex_Type()
)
wmanIfBsOfdmUiucIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsOfdmUiucIndex.setStatus("current")
_WmanIfBsOfdmUcdFecCodeType_Type = WmanIfOfdmFecCodeType
_WmanIfBsOfdmUcdFecCodeType_Object = MibTableColumn
wmanIfBsOfdmUcdFecCodeType = _WmanIfBsOfdmUcdFecCodeType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 3, 1, 2),
    _WmanIfBsOfdmUcdFecCodeType_Type()
)
wmanIfBsOfdmUcdFecCodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmUcdFecCodeType.setStatus("current")


class _WmanIfBsOfdmFocusCtPowerBoost_Type(Integer32):
    """Custom type wmanIfBsOfdmFocusCtPowerBoost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmFocusCtPowerBoost_Type.__name__ = "Integer32"
_WmanIfBsOfdmFocusCtPowerBoost_Object = MibTableColumn
wmanIfBsOfdmFocusCtPowerBoost = _WmanIfBsOfdmFocusCtPowerBoost_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 3, 1, 3),
    _WmanIfBsOfdmFocusCtPowerBoost_Type()
)
wmanIfBsOfdmFocusCtPowerBoost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmFocusCtPowerBoost.setStatus("current")


class _WmanIfBsOfdmUcdTcsEnable_Type(Integer32):
    """Custom type wmanIfBsOfdmUcdTcsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tcsDisabled", 0),
          ("tcsEnabled", 1))
    )


_WmanIfBsOfdmUcdTcsEnable_Type.__name__ = "Integer32"
_WmanIfBsOfdmUcdTcsEnable_Object = MibTableColumn
wmanIfBsOfdmUcdTcsEnable = _WmanIfBsOfdmUcdTcsEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 3, 1, 4),
    _WmanIfBsOfdmUcdTcsEnable_Type()
)
wmanIfBsOfdmUcdTcsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmUcdTcsEnable.setStatus("current")
_WmanIfBsOfdmUcdBurstProfileRowStatus_Type = RowStatus
_WmanIfBsOfdmUcdBurstProfileRowStatus_Object = MibTableColumn
wmanIfBsOfdmUcdBurstProfileRowStatus = _WmanIfBsOfdmUcdBurstProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 3, 1, 5),
    _WmanIfBsOfdmUcdBurstProfileRowStatus_Type()
)
wmanIfBsOfdmUcdBurstProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmUcdBurstProfileRowStatus.setStatus("current")
_WmanIfBsOfdmDcdBurstProfileTable_Object = MibTable
wmanIfBsOfdmDcdBurstProfileTable = _WmanIfBsOfdmDcdBurstProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 4)
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmDcdBurstProfileTable.setStatus("current")
_WmanIfBsOfdmDcdBurstProfileEntry_Object = MibTableRow
wmanIfBsOfdmDcdBurstProfileEntry = _WmanIfBsOfdmDcdBurstProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 4, 1)
)
wmanIfBsOfdmDcdBurstProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfBsOfdmDiucIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmDcdBurstProfileEntry.setStatus("current")


class _WmanIfBsOfdmDiucIndex_Type(Integer32):
    """Custom type wmanIfBsOfdmDiucIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_WmanIfBsOfdmDiucIndex_Type.__name__ = "Integer32"
_WmanIfBsOfdmDiucIndex_Object = MibTableColumn
wmanIfBsOfdmDiucIndex = _WmanIfBsOfdmDiucIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 4, 1, 1),
    _WmanIfBsOfdmDiucIndex_Type()
)
wmanIfBsOfdmDiucIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsOfdmDiucIndex.setStatus("current")
_WmanIfBsOfdmDownlinkFrequency_Type = Unsigned32
_WmanIfBsOfdmDownlinkFrequency_Object = MibTableColumn
wmanIfBsOfdmDownlinkFrequency = _WmanIfBsOfdmDownlinkFrequency_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 4, 1, 2),
    _WmanIfBsOfdmDownlinkFrequency_Type()
)
wmanIfBsOfdmDownlinkFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmDownlinkFrequency.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmDownlinkFrequency.setUnits("kHz")
_WmanIfBsOfdmDcdFecCodeType_Type = WmanIfOfdmFecCodeType
_WmanIfBsOfdmDcdFecCodeType_Object = MibTableColumn
wmanIfBsOfdmDcdFecCodeType = _WmanIfBsOfdmDcdFecCodeType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 4, 1, 3),
    _WmanIfBsOfdmDcdFecCodeType_Type()
)
wmanIfBsOfdmDcdFecCodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmDcdFecCodeType.setStatus("current")


class _WmanIfBsOfdmDiucMandatoryExitThresh_Type(Integer32):
    """Custom type wmanIfBsOfdmDiucMandatoryExitThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmDiucMandatoryExitThresh_Type.__name__ = "Integer32"
_WmanIfBsOfdmDiucMandatoryExitThresh_Object = MibTableColumn
wmanIfBsOfdmDiucMandatoryExitThresh = _WmanIfBsOfdmDiucMandatoryExitThresh_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 4, 1, 4),
    _WmanIfBsOfdmDiucMandatoryExitThresh_Type()
)
wmanIfBsOfdmDiucMandatoryExitThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmDiucMandatoryExitThresh.setStatus("current")


class _WmanIfBsOfdmDiucMinEntryThresh_Type(Integer32):
    """Custom type wmanIfBsOfdmDiucMinEntryThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmDiucMinEntryThresh_Type.__name__ = "Integer32"
_WmanIfBsOfdmDiucMinEntryThresh_Object = MibTableColumn
wmanIfBsOfdmDiucMinEntryThresh = _WmanIfBsOfdmDiucMinEntryThresh_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 4, 1, 5),
    _WmanIfBsOfdmDiucMinEntryThresh_Type()
)
wmanIfBsOfdmDiucMinEntryThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmDiucMinEntryThresh.setStatus("current")


class _WmanIfBsOfdmTcsEnable_Type(Integer32):
    """Custom type wmanIfBsOfdmTcsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tcsDisabled", 0),
          ("tcsEnabled", 1))
    )


_WmanIfBsOfdmTcsEnable_Type.__name__ = "Integer32"
_WmanIfBsOfdmTcsEnable_Object = MibTableColumn
wmanIfBsOfdmTcsEnable = _WmanIfBsOfdmTcsEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 4, 1, 6),
    _WmanIfBsOfdmTcsEnable_Type()
)
wmanIfBsOfdmTcsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmTcsEnable.setStatus("current")
_WmanIfBsOfdmDcdBurstProfileRowStatus_Type = RowStatus
_WmanIfBsOfdmDcdBurstProfileRowStatus_Object = MibTableColumn
wmanIfBsOfdmDcdBurstProfileRowStatus = _WmanIfBsOfdmDcdBurstProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 4, 1, 7),
    _WmanIfBsOfdmDcdBurstProfileRowStatus_Type()
)
wmanIfBsOfdmDcdBurstProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmDcdBurstProfileRowStatus.setStatus("current")
_WmanIfBsOfdmConfigurationTable_Object = MibTable
wmanIfBsOfdmConfigurationTable = _WmanIfBsOfdmConfigurationTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 5)
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmConfigurationTable.setStatus("current")
_WmanIfBsOfdmConfigurationEntry_Object = MibTableRow
wmanIfBsOfdmConfigurationEntry = _WmanIfBsOfdmConfigurationEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 5, 1)
)
wmanIfBsOfdmConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmConfigurationEntry.setStatus("current")


class _WmanIfBsOfdmMinReqRegionFullTxOpp_Type(Integer32):
    """Custom type wmanIfBsOfdmMinReqRegionFullTxOpp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIfBsOfdmMinReqRegionFullTxOpp_Type.__name__ = "Integer32"
_WmanIfBsOfdmMinReqRegionFullTxOpp_Object = MibTableColumn
wmanIfBsOfdmMinReqRegionFullTxOpp = _WmanIfBsOfdmMinReqRegionFullTxOpp_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 5, 1, 1),
    _WmanIfBsOfdmMinReqRegionFullTxOpp_Type()
)
wmanIfBsOfdmMinReqRegionFullTxOpp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmMinReqRegionFullTxOpp.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmMinReqRegionFullTxOpp.setUnits("1/sec")


class _WmanIfBsOfdmMinFocusedCtTxOpp_Type(Integer32):
    """Custom type wmanIfBsOfdmMinFocusedCtTxOpp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsOfdmMinFocusedCtTxOpp_Type.__name__ = "Integer32"
_WmanIfBsOfdmMinFocusedCtTxOpp_Object = MibTableColumn
wmanIfBsOfdmMinFocusedCtTxOpp = _WmanIfBsOfdmMinFocusedCtTxOpp_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 5, 1, 2),
    _WmanIfBsOfdmMinFocusedCtTxOpp_Type()
)
wmanIfBsOfdmMinFocusedCtTxOpp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmMinFocusedCtTxOpp.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmMinFocusedCtTxOpp.setUnits("1/sec")


class _WmanIfBsOfdmMaxRoundTripDelay_Type(Integer32):
    """Custom type wmanIfBsOfdmMaxRoundTripDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIfBsOfdmMaxRoundTripDelay_Type.__name__ = "Integer32"
_WmanIfBsOfdmMaxRoundTripDelay_Object = MibTableColumn
wmanIfBsOfdmMaxRoundTripDelay = _WmanIfBsOfdmMaxRoundTripDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 5, 1, 3),
    _WmanIfBsOfdmMaxRoundTripDelay_Type()
)
wmanIfBsOfdmMaxRoundTripDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmMaxRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmMaxRoundTripDelay.setUnits("us")


class _WmanIfBsOfdmRangeAbortTimingThold_Type(Integer32):
    """Custom type wmanIfBsOfdmRangeAbortTimingThold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmRangeAbortTimingThold_Type.__name__ = "Integer32"
_WmanIfBsOfdmRangeAbortTimingThold_Object = MibTableColumn
wmanIfBsOfdmRangeAbortTimingThold = _WmanIfBsOfdmRangeAbortTimingThold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 5, 1, 4),
    _WmanIfBsOfdmRangeAbortTimingThold_Type()
)
wmanIfBsOfdmRangeAbortTimingThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmRangeAbortTimingThold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmRangeAbortTimingThold.setUnits("1/Fs")


class _WmanIfBsOfdmRangeAbortPowerThold_Type(Integer32):
    """Custom type wmanIfBsOfdmRangeAbortPowerThold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmRangeAbortPowerThold_Type.__name__ = "Integer32"
_WmanIfBsOfdmRangeAbortPowerThold_Object = MibTableColumn
wmanIfBsOfdmRangeAbortPowerThold = _WmanIfBsOfdmRangeAbortPowerThold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 5, 1, 5),
    _WmanIfBsOfdmRangeAbortPowerThold_Type()
)
wmanIfBsOfdmRangeAbortPowerThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmRangeAbortPowerThold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmRangeAbortPowerThold.setUnits("0.25dB")


class _WmanIfBsOfdmRangeAbortFreqThold_Type(Integer32):
    """Custom type wmanIfBsOfdmRangeAbortFreqThold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmRangeAbortFreqThold_Type.__name__ = "Integer32"
_WmanIfBsOfdmRangeAbortFreqThold_Object = MibTableColumn
wmanIfBsOfdmRangeAbortFreqThold = _WmanIfBsOfdmRangeAbortFreqThold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 5, 1, 6),
    _WmanIfBsOfdmRangeAbortFreqThold_Type()
)
wmanIfBsOfdmRangeAbortFreqThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmRangeAbortFreqThold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmRangeAbortFreqThold.setUnits("Hz")


class _WmanIfBsOfdmDnlkRateId_Type(Integer32):
    """Custom type wmanIfBsOfdmDnlkRateId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dnlkRateIdBpsk1Over2", 0),
          ("dnlkRateIdQpsk1Over2", 1),
          ("dnlkRateIdQpsk3Over4", 2),
          ("dnlkRateId16Qam1Over2", 3),
          ("dnlkRateId16Qam3Over4", 4),
          ("dnlkRateId64Qam2Over3", 5),
          ("dnlkRateId64Qam3Over4", 6))
    )


_WmanIfBsOfdmDnlkRateId_Type.__name__ = "Integer32"
_WmanIfBsOfdmDnlkRateId_Object = MibTableColumn
wmanIfBsOfdmDnlkRateId = _WmanIfBsOfdmDnlkRateId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 5, 1, 7),
    _WmanIfBsOfdmDnlkRateId_Type()
)
wmanIfBsOfdmDnlkRateId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmDnlkRateId.setStatus("current")


class _WmanIfBsOfdmRatioG_Type(Integer32):
    """Custom type wmanIfBsOfdmRatioG based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ratio1To4", 0),
          ("ratio1To8", 1),
          ("ratio1To16", 2),
          ("ratio1To32", 3))
    )


_WmanIfBsOfdmRatioG_Type.__name__ = "Integer32"
_WmanIfBsOfdmRatioG_Object = MibTableColumn
wmanIfBsOfdmRatioG = _WmanIfBsOfdmRatioG_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 5, 1, 8),
    _WmanIfBsOfdmRatioG_Type()
)
wmanIfBsOfdmRatioG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmRatioG.setStatus("current")
_WmanIfBsSsOfdmReqCapabilitiesTable_Object = MibTable
wmanIfBsSsOfdmReqCapabilitiesTable = _WmanIfBsSsOfdmReqCapabilitiesTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 6)
)
if mibBuilder.loadTexts:
    wmanIfBsSsOfdmReqCapabilitiesTable.setStatus("current")
_WmanIfBsSsOfdmReqCapabilitiesEntry_Object = MibTableRow
wmanIfBsSsOfdmReqCapabilitiesEntry = _WmanIfBsSsOfdmReqCapabilitiesEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 6, 1)
)
if mibBuilder.loadTexts:
    wmanIfBsSsOfdmReqCapabilitiesEntry.setStatus("current")
_WmanIfBsSsOfdmReqCapFftSizes_Type = WmanIfOfdmFftSizes
_WmanIfBsSsOfdmReqCapFftSizes_Object = MibTableColumn
wmanIfBsSsOfdmReqCapFftSizes = _WmanIfBsSsOfdmReqCapFftSizes_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 6, 1, 1),
    _WmanIfBsSsOfdmReqCapFftSizes_Type()
)
wmanIfBsSsOfdmReqCapFftSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsOfdmReqCapFftSizes.setStatus("current")
_WmanIfBsSsOfdmReqCapSsDemodulator_Type = WmanIfOfdmSsDeModType
_WmanIfBsSsOfdmReqCapSsDemodulator_Object = MibTableColumn
wmanIfBsSsOfdmReqCapSsDemodulator = _WmanIfBsSsOfdmReqCapSsDemodulator_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 6, 1, 2),
    _WmanIfBsSsOfdmReqCapSsDemodulator_Type()
)
wmanIfBsSsOfdmReqCapSsDemodulator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsOfdmReqCapSsDemodulator.setStatus("current")
_WmanIfBsSsOfdmReqCapSsModulator_Type = WmanIfOfdmSsModType
_WmanIfBsSsOfdmReqCapSsModulator_Object = MibTableColumn
wmanIfBsSsOfdmReqCapSsModulator = _WmanIfBsSsOfdmReqCapSsModulator_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 6, 1, 3),
    _WmanIfBsSsOfdmReqCapSsModulator_Type()
)
wmanIfBsSsOfdmReqCapSsModulator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsOfdmReqCapSsModulator.setStatus("current")
_WmanIfBsSsOfdmReqCapFocusedCtSupport_Type = WmanIfOfdmFocusedCt
_WmanIfBsSsOfdmReqCapFocusedCtSupport_Object = MibTableColumn
wmanIfBsSsOfdmReqCapFocusedCtSupport = _WmanIfBsSsOfdmReqCapFocusedCtSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 6, 1, 4),
    _WmanIfBsSsOfdmReqCapFocusedCtSupport_Type()
)
wmanIfBsSsOfdmReqCapFocusedCtSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsOfdmReqCapFocusedCtSupport.setStatus("current")
_WmanIfBsSsOfdmReqCapTcSublayerSupport_Type = WmanIfOfdmTcSublayer
_WmanIfBsSsOfdmReqCapTcSublayerSupport_Object = MibTableColumn
wmanIfBsSsOfdmReqCapTcSublayerSupport = _WmanIfBsSsOfdmReqCapTcSublayerSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 6, 1, 5),
    _WmanIfBsSsOfdmReqCapTcSublayerSupport_Type()
)
wmanIfBsSsOfdmReqCapTcSublayerSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsOfdmReqCapTcSublayerSupport.setStatus("current")
_WmanIfBsSsOfdmRspCapabilitiesTable_Object = MibTable
wmanIfBsSsOfdmRspCapabilitiesTable = _WmanIfBsSsOfdmRspCapabilitiesTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 7)
)
if mibBuilder.loadTexts:
    wmanIfBsSsOfdmRspCapabilitiesTable.setStatus("current")
_WmanIfBsSsOfdmRspCapabilitiesEntry_Object = MibTableRow
wmanIfBsSsOfdmRspCapabilitiesEntry = _WmanIfBsSsOfdmRspCapabilitiesEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 7, 1)
)
if mibBuilder.loadTexts:
    wmanIfBsSsOfdmRspCapabilitiesEntry.setStatus("current")
_WmanIfBsSsOfdmRspCapFftSizes_Type = WmanIfOfdmFftSizes
_WmanIfBsSsOfdmRspCapFftSizes_Object = MibTableColumn
wmanIfBsSsOfdmRspCapFftSizes = _WmanIfBsSsOfdmRspCapFftSizes_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 7, 1, 1),
    _WmanIfBsSsOfdmRspCapFftSizes_Type()
)
wmanIfBsSsOfdmRspCapFftSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsOfdmRspCapFftSizes.setStatus("current")
_WmanIfBsSsOfdmRspCapSsDemodulator_Type = WmanIfOfdmSsDeModType
_WmanIfBsSsOfdmRspCapSsDemodulator_Object = MibTableColumn
wmanIfBsSsOfdmRspCapSsDemodulator = _WmanIfBsSsOfdmRspCapSsDemodulator_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 7, 1, 2),
    _WmanIfBsSsOfdmRspCapSsDemodulator_Type()
)
wmanIfBsSsOfdmRspCapSsDemodulator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsOfdmRspCapSsDemodulator.setStatus("current")
_WmanIfBsSsOfdmRspCapSsModulator_Type = WmanIfOfdmSsModType
_WmanIfBsSsOfdmRspCapSsModulator_Object = MibTableColumn
wmanIfBsSsOfdmRspCapSsModulator = _WmanIfBsSsOfdmRspCapSsModulator_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 7, 1, 3),
    _WmanIfBsSsOfdmRspCapSsModulator_Type()
)
wmanIfBsSsOfdmRspCapSsModulator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsOfdmRspCapSsModulator.setStatus("current")
_WmanIfBsSsOfdmRspCapFocusedCtSupport_Type = WmanIfOfdmFocusedCt
_WmanIfBsSsOfdmRspCapFocusedCtSupport_Object = MibTableColumn
wmanIfBsSsOfdmRspCapFocusedCtSupport = _WmanIfBsSsOfdmRspCapFocusedCtSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 7, 1, 4),
    _WmanIfBsSsOfdmRspCapFocusedCtSupport_Type()
)
wmanIfBsSsOfdmRspCapFocusedCtSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsOfdmRspCapFocusedCtSupport.setStatus("current")
_WmanIfBsSsOfdmRspCapTcSublayerSupport_Type = WmanIfOfdmTcSublayer
_WmanIfBsSsOfdmRspCapTcSublayerSupport_Object = MibTableColumn
wmanIfBsSsOfdmRspCapTcSublayerSupport = _WmanIfBsSsOfdmRspCapTcSublayerSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 7, 1, 5),
    _WmanIfBsSsOfdmRspCapTcSublayerSupport_Type()
)
wmanIfBsSsOfdmRspCapTcSublayerSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsOfdmRspCapTcSublayerSupport.setStatus("current")
_WmanIfBsOfdmCapabilitiesTable_Object = MibTable
wmanIfBsOfdmCapabilitiesTable = _WmanIfBsOfdmCapabilitiesTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 8)
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmCapabilitiesTable.setStatus("current")
_WmanIfBsOfdmCapabilitiesEntry_Object = MibTableRow
wmanIfBsOfdmCapabilitiesEntry = _WmanIfBsOfdmCapabilitiesEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 8, 1)
)
wmanIfBsOfdmCapabilitiesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmCapabilitiesEntry.setStatus("current")
_WmanIfBsOfdmCapFftSizes_Type = WmanIfOfdmFftSizes
_WmanIfBsOfdmCapFftSizes_Object = MibTableColumn
wmanIfBsOfdmCapFftSizes = _WmanIfBsOfdmCapFftSizes_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 8, 1, 1),
    _WmanIfBsOfdmCapFftSizes_Type()
)
wmanIfBsOfdmCapFftSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsOfdmCapFftSizes.setStatus("current")
_WmanIfBsOfdmCapSsDemodulator_Type = WmanIfOfdmSsDeModType
_WmanIfBsOfdmCapSsDemodulator_Object = MibTableColumn
wmanIfBsOfdmCapSsDemodulator = _WmanIfBsOfdmCapSsDemodulator_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 8, 1, 2),
    _WmanIfBsOfdmCapSsDemodulator_Type()
)
wmanIfBsOfdmCapSsDemodulator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsOfdmCapSsDemodulator.setStatus("current")
_WmanIfBsOfdmCapSsModulator_Type = WmanIfOfdmSsModType
_WmanIfBsOfdmCapSsModulator_Object = MibTableColumn
wmanIfBsOfdmCapSsModulator = _WmanIfBsOfdmCapSsModulator_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 8, 1, 3),
    _WmanIfBsOfdmCapSsModulator_Type()
)
wmanIfBsOfdmCapSsModulator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsOfdmCapSsModulator.setStatus("current")
_WmanIfBsOfdmCapFocusedCtSupport_Type = WmanIfOfdmFocusedCt
_WmanIfBsOfdmCapFocusedCtSupport_Object = MibTableColumn
wmanIfBsOfdmCapFocusedCtSupport = _WmanIfBsOfdmCapFocusedCtSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 8, 1, 4),
    _WmanIfBsOfdmCapFocusedCtSupport_Type()
)
wmanIfBsOfdmCapFocusedCtSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsOfdmCapFocusedCtSupport.setStatus("current")
_WmanIfBsOfdmCapTcSublayerSupport_Type = WmanIfOfdmTcSublayer
_WmanIfBsOfdmCapTcSublayerSupport_Object = MibTableColumn
wmanIfBsOfdmCapTcSublayerSupport = _WmanIfBsOfdmCapTcSublayerSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 8, 1, 5),
    _WmanIfBsOfdmCapTcSublayerSupport_Type()
)
wmanIfBsOfdmCapTcSublayerSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsOfdmCapTcSublayerSupport.setStatus("current")
_WmanIfBsOfdmCapabilitiesConfigTable_Object = MibTable
wmanIfBsOfdmCapabilitiesConfigTable = _WmanIfBsOfdmCapabilitiesConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 9)
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmCapabilitiesConfigTable.setStatus("current")
_WmanIfBsOfdmCapabilitiesConfigEntry_Object = MibTableRow
wmanIfBsOfdmCapabilitiesConfigEntry = _WmanIfBsOfdmCapabilitiesConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 9, 1)
)
wmanIfBsOfdmCapabilitiesConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmCapabilitiesConfigEntry.setStatus("current")
_WmanIfBsOfdmCapCfgFftSizes_Type = WmanIfOfdmFftSizes
_WmanIfBsOfdmCapCfgFftSizes_Object = MibTableColumn
wmanIfBsOfdmCapCfgFftSizes = _WmanIfBsOfdmCapCfgFftSizes_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 9, 1, 1),
    _WmanIfBsOfdmCapCfgFftSizes_Type()
)
wmanIfBsOfdmCapCfgFftSizes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmCapCfgFftSizes.setStatus("current")
_WmanIfBsOfdmCapCfgSsDemodulator_Type = WmanIfOfdmSsDeModType
_WmanIfBsOfdmCapCfgSsDemodulator_Object = MibTableColumn
wmanIfBsOfdmCapCfgSsDemodulator = _WmanIfBsOfdmCapCfgSsDemodulator_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 9, 1, 2),
    _WmanIfBsOfdmCapCfgSsDemodulator_Type()
)
wmanIfBsOfdmCapCfgSsDemodulator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmCapCfgSsDemodulator.setStatus("current")
_WmanIfBsOfdmCapCfgSsModulator_Type = WmanIfOfdmSsModType
_WmanIfBsOfdmCapCfgSsModulator_Object = MibTableColumn
wmanIfBsOfdmCapCfgSsModulator = _WmanIfBsOfdmCapCfgSsModulator_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 9, 1, 3),
    _WmanIfBsOfdmCapCfgSsModulator_Type()
)
wmanIfBsOfdmCapCfgSsModulator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmCapCfgSsModulator.setStatus("current")
_WmanIfBsOfdmCapCfgFocusedCtSupport_Type = WmanIfOfdmFocusedCt
_WmanIfBsOfdmCapCfgFocusedCtSupport_Object = MibTableColumn
wmanIfBsOfdmCapCfgFocusedCtSupport = _WmanIfBsOfdmCapCfgFocusedCtSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 9, 1, 4),
    _WmanIfBsOfdmCapCfgFocusedCtSupport_Type()
)
wmanIfBsOfdmCapCfgFocusedCtSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmCapCfgFocusedCtSupport.setStatus("current")
_WmanIfBsOfdmCapCfgTcSublayerSupport_Type = WmanIfOfdmTcSublayer
_WmanIfBsOfdmCapCfgTcSublayerSupport_Object = MibTableColumn
wmanIfBsOfdmCapCfgTcSublayerSupport = _WmanIfBsOfdmCapCfgTcSublayerSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 1, 9, 1, 5),
    _WmanIfBsOfdmCapCfgTcSublayerSupport_Type()
)
wmanIfBsOfdmCapCfgTcSublayerSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmCapCfgTcSublayerSupport.setStatus("current")
_WmanIfBsOfdmaPhy_ObjectIdentity = ObjectIdentity
wmanIfBsOfdmaPhy = _WmanIfBsOfdmaPhy_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2)
)
_WmanIfBsOfdmaUplinkChannelTable_Object = MibTable
wmanIfBsOfdmaUplinkChannelTable = _WmanIfBsOfdmaUplinkChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmaUplinkChannelTable.setStatus("current")
_WmanIfBsOfdmaUplinkChannelEntry_Object = MibTableRow
wmanIfBsOfdmaUplinkChannelEntry = _WmanIfBsOfdmaUplinkChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1)
)
wmanIfBsOfdmaUplinkChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmaUplinkChannelEntry.setStatus("current")


class _WmanIfBsOfdmaCtBasedResvTimeout_Type(Integer32):
    """Custom type wmanIfBsOfdmaCtBasedResvTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WmanIfBsOfdmaCtBasedResvTimeout_Type.__name__ = "Integer32"
_WmanIfBsOfdmaCtBasedResvTimeout_Object = MibTableColumn
wmanIfBsOfdmaCtBasedResvTimeout = _WmanIfBsOfdmaCtBasedResvTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 1),
    _WmanIfBsOfdmaCtBasedResvTimeout_Type()
)
wmanIfBsOfdmaCtBasedResvTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaCtBasedResvTimeout.setStatus("current")


class _WmanIfBsOfdmaBwReqOppSize_Type(Integer32):
    """Custom type wmanIfBsOfdmaBwReqOppSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIfBsOfdmaBwReqOppSize_Type.__name__ = "Integer32"
_WmanIfBsOfdmaBwReqOppSize_Object = MibTableColumn
wmanIfBsOfdmaBwReqOppSize = _WmanIfBsOfdmaBwReqOppSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 2),
    _WmanIfBsOfdmaBwReqOppSize_Type()
)
wmanIfBsOfdmaBwReqOppSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBwReqOppSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBwReqOppSize.setUnits("PS")


class _WmanIfBsOfdmaRangReqOppSize_Type(Integer32):
    """Custom type wmanIfBsOfdmaRangReqOppSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIfBsOfdmaRangReqOppSize_Type.__name__ = "Integer32"
_WmanIfBsOfdmaRangReqOppSize_Object = MibTableColumn
wmanIfBsOfdmaRangReqOppSize = _WmanIfBsOfdmaRangReqOppSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 3),
    _WmanIfBsOfdmaRangReqOppSize_Type()
)
wmanIfBsOfdmaRangReqOppSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaRangReqOppSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaRangReqOppSize.setUnits("PS")
_WmanIfBsOfdmaUplinkCenterFreq_Type = Unsigned32
_WmanIfBsOfdmaUplinkCenterFreq_Object = MibTableColumn
wmanIfBsOfdmaUplinkCenterFreq = _WmanIfBsOfdmaUplinkCenterFreq_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 4),
    _WmanIfBsOfdmaUplinkCenterFreq_Type()
)
wmanIfBsOfdmaUplinkCenterFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaUplinkCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaUplinkCenterFreq.setUnits("kHz")


class _WmanIfBsOfdmaInitRngCodes_Type(Integer32):
    """Custom type wmanIfBsOfdmaInitRngCodes based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaInitRngCodes_Type.__name__ = "Integer32"
_WmanIfBsOfdmaInitRngCodes_Object = MibTableColumn
wmanIfBsOfdmaInitRngCodes = _WmanIfBsOfdmaInitRngCodes_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 5),
    _WmanIfBsOfdmaInitRngCodes_Type()
)
wmanIfBsOfdmaInitRngCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaInitRngCodes.setStatus("current")


class _WmanIfBsOfdmaPeriodicRngCodes_Type(Integer32):
    """Custom type wmanIfBsOfdmaPeriodicRngCodes based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaPeriodicRngCodes_Type.__name__ = "Integer32"
_WmanIfBsOfdmaPeriodicRngCodes_Object = MibTableColumn
wmanIfBsOfdmaPeriodicRngCodes = _WmanIfBsOfdmaPeriodicRngCodes_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 6),
    _WmanIfBsOfdmaPeriodicRngCodes_Type()
)
wmanIfBsOfdmaPeriodicRngCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaPeriodicRngCodes.setStatus("current")


class _WmanIfBsOfdmaBWReqCodes_Type(Integer32):
    """Custom type wmanIfBsOfdmaBWReqCodes based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaBWReqCodes_Type.__name__ = "Integer32"
_WmanIfBsOfdmaBWReqCodes_Object = MibTableColumn
wmanIfBsOfdmaBWReqCodes = _WmanIfBsOfdmaBWReqCodes_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 7),
    _WmanIfBsOfdmaBWReqCodes_Type()
)
wmanIfBsOfdmaBWReqCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBWReqCodes.setStatus("current")


class _WmanIfBsOfdmaPerRngBackoffStart_Type(Integer32):
    """Custom type wmanIfBsOfdmaPerRngBackoffStart based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIfBsOfdmaPerRngBackoffStart_Type.__name__ = "Integer32"
_WmanIfBsOfdmaPerRngBackoffStart_Object = MibTableColumn
wmanIfBsOfdmaPerRngBackoffStart = _WmanIfBsOfdmaPerRngBackoffStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 8),
    _WmanIfBsOfdmaPerRngBackoffStart_Type()
)
wmanIfBsOfdmaPerRngBackoffStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaPerRngBackoffStart.setStatus("current")


class _WmanIfBsOfdmaPerRngBackoffEnd_Type(Integer32):
    """Custom type wmanIfBsOfdmaPerRngBackoffEnd based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIfBsOfdmaPerRngBackoffEnd_Type.__name__ = "Integer32"
_WmanIfBsOfdmaPerRngBackoffEnd_Object = MibTableColumn
wmanIfBsOfdmaPerRngBackoffEnd = _WmanIfBsOfdmaPerRngBackoffEnd_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 9),
    _WmanIfBsOfdmaPerRngBackoffEnd_Type()
)
wmanIfBsOfdmaPerRngBackoffEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaPerRngBackoffEnd.setStatus("current")


class _WmanIfBsOfdmaStartOfRngCodes_Type(Integer32):
    """Custom type wmanIfBsOfdmaStartOfRngCodes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaStartOfRngCodes_Type.__name__ = "Integer32"
_WmanIfBsOfdmaStartOfRngCodes_Object = MibTableColumn
wmanIfBsOfdmaStartOfRngCodes = _WmanIfBsOfdmaStartOfRngCodes_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 10),
    _WmanIfBsOfdmaStartOfRngCodes_Type()
)
wmanIfBsOfdmaStartOfRngCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaStartOfRngCodes.setStatus("current")


class _WmanIfBsOfdmaPermutationBase_Type(Integer32):
    """Custom type wmanIfBsOfdmaPermutationBase based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaPermutationBase_Type.__name__ = "Integer32"
_WmanIfBsOfdmaPermutationBase_Object = MibTableColumn
wmanIfBsOfdmaPermutationBase = _WmanIfBsOfdmaPermutationBase_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 11),
    _WmanIfBsOfdmaPermutationBase_Type()
)
wmanIfBsOfdmaPermutationBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaPermutationBase.setStatus("current")


class _WmanIfBsOfdmaULAllocSubchBitmap_Type(OctetString):
    """Custom type wmanIfBsOfdmaULAllocSubchBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )
    fixedLength = 9


_WmanIfBsOfdmaULAllocSubchBitmap_Type.__name__ = "OctetString"
_WmanIfBsOfdmaULAllocSubchBitmap_Object = MibTableColumn
wmanIfBsOfdmaULAllocSubchBitmap = _WmanIfBsOfdmaULAllocSubchBitmap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 12),
    _WmanIfBsOfdmaULAllocSubchBitmap_Type()
)
wmanIfBsOfdmaULAllocSubchBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaULAllocSubchBitmap.setStatus("current")


class _WmanIfBsOfdmaOptPermULAllocSubchBitmap_Type(OctetString):
    """Custom type wmanIfBsOfdmaOptPermULAllocSubchBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )
    fixedLength = 13


_WmanIfBsOfdmaOptPermULAllocSubchBitmap_Type.__name__ = "OctetString"
_WmanIfBsOfdmaOptPermULAllocSubchBitmap_Object = MibTableColumn
wmanIfBsOfdmaOptPermULAllocSubchBitmap = _WmanIfBsOfdmaOptPermULAllocSubchBitmap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 13),
    _WmanIfBsOfdmaOptPermULAllocSubchBitmap_Type()
)
wmanIfBsOfdmaOptPermULAllocSubchBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaOptPermULAllocSubchBitmap.setStatus("current")


class _WmanIfBsOfdmaBandAMCAllocThreshold_Type(Integer32):
    """Custom type wmanIfBsOfdmaBandAMCAllocThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaBandAMCAllocThreshold_Type.__name__ = "Integer32"
_WmanIfBsOfdmaBandAMCAllocThreshold_Object = MibTableColumn
wmanIfBsOfdmaBandAMCAllocThreshold = _WmanIfBsOfdmaBandAMCAllocThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 14),
    _WmanIfBsOfdmaBandAMCAllocThreshold_Type()
)
wmanIfBsOfdmaBandAMCAllocThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBandAMCAllocThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBandAMCAllocThreshold.setUnits("dB")


class _WmanIfBsOfdmaBandAMCReleaseThreshold_Type(Integer32):
    """Custom type wmanIfBsOfdmaBandAMCReleaseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaBandAMCReleaseThreshold_Type.__name__ = "Integer32"
_WmanIfBsOfdmaBandAMCReleaseThreshold_Object = MibTableColumn
wmanIfBsOfdmaBandAMCReleaseThreshold = _WmanIfBsOfdmaBandAMCReleaseThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 15),
    _WmanIfBsOfdmaBandAMCReleaseThreshold_Type()
)
wmanIfBsOfdmaBandAMCReleaseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBandAMCReleaseThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBandAMCReleaseThreshold.setUnits("dB")


class _WmanIfBsOfdmaBandAMCAllocTimer_Type(Integer32):
    """Custom type wmanIfBsOfdmaBandAMCAllocTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaBandAMCAllocTimer_Type.__name__ = "Integer32"
_WmanIfBsOfdmaBandAMCAllocTimer_Object = MibTableColumn
wmanIfBsOfdmaBandAMCAllocTimer = _WmanIfBsOfdmaBandAMCAllocTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 16),
    _WmanIfBsOfdmaBandAMCAllocTimer_Type()
)
wmanIfBsOfdmaBandAMCAllocTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBandAMCAllocTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBandAMCAllocTimer.setUnits("Frame")


class _WmanIfBsOfdmaBandAMCReleaseTimer_Type(Integer32):
    """Custom type wmanIfBsOfdmaBandAMCReleaseTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaBandAMCReleaseTimer_Type.__name__ = "Integer32"
_WmanIfBsOfdmaBandAMCReleaseTimer_Object = MibTableColumn
wmanIfBsOfdmaBandAMCReleaseTimer = _WmanIfBsOfdmaBandAMCReleaseTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 17),
    _WmanIfBsOfdmaBandAMCReleaseTimer_Type()
)
wmanIfBsOfdmaBandAMCReleaseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBandAMCReleaseTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBandAMCReleaseTimer.setUnits("Frame")


class _WmanIfBsOfdmaBandStatRepMAXPeriod_Type(Integer32):
    """Custom type wmanIfBsOfdmaBandStatRepMAXPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaBandStatRepMAXPeriod_Type.__name__ = "Integer32"
_WmanIfBsOfdmaBandStatRepMAXPeriod_Object = MibTableColumn
wmanIfBsOfdmaBandStatRepMAXPeriod = _WmanIfBsOfdmaBandStatRepMAXPeriod_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 18),
    _WmanIfBsOfdmaBandStatRepMAXPeriod_Type()
)
wmanIfBsOfdmaBandStatRepMAXPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBandStatRepMAXPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBandStatRepMAXPeriod.setUnits("Frame")


class _WmanIfBsOfdmaBandAMCRetryTimer_Type(Integer32):
    """Custom type wmanIfBsOfdmaBandAMCRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaBandAMCRetryTimer_Type.__name__ = "Integer32"
_WmanIfBsOfdmaBandAMCRetryTimer_Object = MibTableColumn
wmanIfBsOfdmaBandAMCRetryTimer = _WmanIfBsOfdmaBandAMCRetryTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 19),
    _WmanIfBsOfdmaBandAMCRetryTimer_Type()
)
wmanIfBsOfdmaBandAMCRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBandAMCRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBandAMCRetryTimer.setUnits("Frame")


class _WmanIfBsOfdmaSafetyChAllocThreshold_Type(Integer32):
    """Custom type wmanIfBsOfdmaSafetyChAllocThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaSafetyChAllocThreshold_Type.__name__ = "Integer32"
_WmanIfBsOfdmaSafetyChAllocThreshold_Object = MibTableColumn
wmanIfBsOfdmaSafetyChAllocThreshold = _WmanIfBsOfdmaSafetyChAllocThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 20),
    _WmanIfBsOfdmaSafetyChAllocThreshold_Type()
)
wmanIfBsOfdmaSafetyChAllocThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaSafetyChAllocThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaSafetyChAllocThreshold.setUnits("dB")


class _WmanIfBsOfdmaSafetyChReleaseThreshold_Type(Integer32):
    """Custom type wmanIfBsOfdmaSafetyChReleaseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaSafetyChReleaseThreshold_Type.__name__ = "Integer32"
_WmanIfBsOfdmaSafetyChReleaseThreshold_Object = MibTableColumn
wmanIfBsOfdmaSafetyChReleaseThreshold = _WmanIfBsOfdmaSafetyChReleaseThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 21),
    _WmanIfBsOfdmaSafetyChReleaseThreshold_Type()
)
wmanIfBsOfdmaSafetyChReleaseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaSafetyChReleaseThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaSafetyChReleaseThreshold.setUnits("dB")


class _WmanIfBsOfdmaSafetyChAllocTimer_Type(Integer32):
    """Custom type wmanIfBsOfdmaSafetyChAllocTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaSafetyChAllocTimer_Type.__name__ = "Integer32"
_WmanIfBsOfdmaSafetyChAllocTimer_Object = MibTableColumn
wmanIfBsOfdmaSafetyChAllocTimer = _WmanIfBsOfdmaSafetyChAllocTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 22),
    _WmanIfBsOfdmaSafetyChAllocTimer_Type()
)
wmanIfBsOfdmaSafetyChAllocTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaSafetyChAllocTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaSafetyChAllocTimer.setUnits("Frame")


class _WmanIfBsOfdmaSafetyChReleaseTimer_Type(Integer32):
    """Custom type wmanIfBsOfdmaSafetyChReleaseTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaSafetyChReleaseTimer_Type.__name__ = "Integer32"
_WmanIfBsOfdmaSafetyChReleaseTimer_Object = MibTableColumn
wmanIfBsOfdmaSafetyChReleaseTimer = _WmanIfBsOfdmaSafetyChReleaseTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 23),
    _WmanIfBsOfdmaSafetyChReleaseTimer_Type()
)
wmanIfBsOfdmaSafetyChReleaseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaSafetyChReleaseTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaSafetyChReleaseTimer.setUnits("Frame")


class _WmanIfBsOfdmaBinStatRepMAXPeriod_Type(Integer32):
    """Custom type wmanIfBsOfdmaBinStatRepMAXPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaBinStatRepMAXPeriod_Type.__name__ = "Integer32"
_WmanIfBsOfdmaBinStatRepMAXPeriod_Object = MibTableColumn
wmanIfBsOfdmaBinStatRepMAXPeriod = _WmanIfBsOfdmaBinStatRepMAXPeriod_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 24),
    _WmanIfBsOfdmaBinStatRepMAXPeriod_Type()
)
wmanIfBsOfdmaBinStatRepMAXPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBinStatRepMAXPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBinStatRepMAXPeriod.setUnits("Frame")


class _WmanIfBsOfdmaSafetyChaRetryTimer_Type(Integer32):
    """Custom type wmanIfBsOfdmaSafetyChaRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaSafetyChaRetryTimer_Type.__name__ = "Integer32"
_WmanIfBsOfdmaSafetyChaRetryTimer_Object = MibTableColumn
wmanIfBsOfdmaSafetyChaRetryTimer = _WmanIfBsOfdmaSafetyChaRetryTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 25),
    _WmanIfBsOfdmaSafetyChaRetryTimer_Type()
)
wmanIfBsOfdmaSafetyChaRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaSafetyChaRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaSafetyChaRetryTimer.setUnits("Frame")


class _WmanIfBsOfdmaHARQAackDelayULBurst_Type(Integer32):
    """Custom type wmanIfBsOfdmaHARQAackDelayULBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneframeoffset", 1),
          ("twoframesoffset", 2),
          ("threeframesoffset", 3))
    )


_WmanIfBsOfdmaHARQAackDelayULBurst_Type.__name__ = "Integer32"
_WmanIfBsOfdmaHARQAackDelayULBurst_Object = MibTableColumn
wmanIfBsOfdmaHARQAackDelayULBurst = _WmanIfBsOfdmaHARQAackDelayULBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 26),
    _WmanIfBsOfdmaHARQAackDelayULBurst_Type()
)
wmanIfBsOfdmaHARQAackDelayULBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaHARQAackDelayULBurst.setStatus("current")


class _WmanIfBsOfdmaCQICHBandAMCTranaDelay_Type(Integer32):
    """Custom type wmanIfBsOfdmaCQICHBandAMCTranaDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaCQICHBandAMCTranaDelay_Type.__name__ = "Integer32"
_WmanIfBsOfdmaCQICHBandAMCTranaDelay_Object = MibTableColumn
wmanIfBsOfdmaCQICHBandAMCTranaDelay = _WmanIfBsOfdmaCQICHBandAMCTranaDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 1, 1, 27),
    _WmanIfBsOfdmaCQICHBandAMCTranaDelay_Type()
)
wmanIfBsOfdmaCQICHBandAMCTranaDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaCQICHBandAMCTranaDelay.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaCQICHBandAMCTranaDelay.setUnits("Frame")
_WmanIfBsOfdmaDownlinkChannelTable_Object = MibTable
wmanIfBsOfdmaDownlinkChannelTable = _WmanIfBsOfdmaDownlinkChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmaDownlinkChannelTable.setStatus("current")
_WmanIfBsOfdmaDownlinkChannelEntry_Object = MibTableRow
wmanIfBsOfdmaDownlinkChannelEntry = _WmanIfBsOfdmaDownlinkChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 2, 1)
)
wmanIfBsOfdmaDownlinkChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmaDownlinkChannelEntry.setStatus("current")


class _WmanIfBsOfdmaBsEIRP_Type(Integer32):
    """Custom type wmanIfBsOfdmaBsEIRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsOfdmaBsEIRP_Type.__name__ = "Integer32"
_WmanIfBsOfdmaBsEIRP_Object = MibTableColumn
wmanIfBsOfdmaBsEIRP = _WmanIfBsOfdmaBsEIRP_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 2, 1, 1),
    _WmanIfBsOfdmaBsEIRP_Type()
)
wmanIfBsOfdmaBsEIRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBsEIRP.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBsEIRP.setUnits("dBm")
_WmanIfBsOfdmaChannelNumber_Type = WmanIfChannelNumber
_WmanIfBsOfdmaChannelNumber_Object = MibTableColumn
wmanIfBsOfdmaChannelNumber = _WmanIfBsOfdmaChannelNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 2, 1, 2),
    _WmanIfBsOfdmaChannelNumber_Type()
)
wmanIfBsOfdmaChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaChannelNumber.setStatus("current")


class _WmanIfBsOfdmaTTG_Type(Integer32):
    """Custom type wmanIfBsOfdmaTTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaTTG_Type.__name__ = "Integer32"
_WmanIfBsOfdmaTTG_Object = MibTableColumn
wmanIfBsOfdmaTTG = _WmanIfBsOfdmaTTG_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 2, 1, 3),
    _WmanIfBsOfdmaTTG_Type()
)
wmanIfBsOfdmaTTG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaTTG.setStatus("current")


class _WmanIfBsOfdmaRTG_Type(Integer32):
    """Custom type wmanIfBsOfdmaRTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaRTG_Type.__name__ = "Integer32"
_WmanIfBsOfdmaRTG_Object = MibTableColumn
wmanIfBsOfdmaRTG = _WmanIfBsOfdmaRTG_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 2, 1, 4),
    _WmanIfBsOfdmaRTG_Type()
)
wmanIfBsOfdmaRTG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaRTG.setStatus("current")


class _WmanIfBsOfdmaInitRngMaxRSS_Type(Integer32):
    """Custom type wmanIfBsOfdmaInitRngMaxRSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsOfdmaInitRngMaxRSS_Type.__name__ = "Integer32"
_WmanIfBsOfdmaInitRngMaxRSS_Object = MibTableColumn
wmanIfBsOfdmaInitRngMaxRSS = _WmanIfBsOfdmaInitRngMaxRSS_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 2, 1, 5),
    _WmanIfBsOfdmaInitRngMaxRSS_Type()
)
wmanIfBsOfdmaInitRngMaxRSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaInitRngMaxRSS.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaInitRngMaxRSS.setUnits("dBm")
_WmanIfBsOfdmaDownlinkCenterFreq_Type = Unsigned32
_WmanIfBsOfdmaDownlinkCenterFreq_Object = MibTableColumn
wmanIfBsOfdmaDownlinkCenterFreq = _WmanIfBsOfdmaDownlinkCenterFreq_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 2, 1, 6),
    _WmanIfBsOfdmaDownlinkCenterFreq_Type()
)
wmanIfBsOfdmaDownlinkCenterFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaDownlinkCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaDownlinkCenterFreq.setUnits("kHz")
_WmanIfBsOfdmaBsId_Type = WmanIfBsIdType
_WmanIfBsOfdmaBsId_Object = MibTableColumn
wmanIfBsOfdmaBsId = _WmanIfBsOfdmaBsId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 2, 1, 7),
    _WmanIfBsOfdmaBsId_Type()
)
wmanIfBsOfdmaBsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaBsId.setStatus("current")
_WmanIfBsOfdmaMacVersion_Type = WmanIfMacVersion
_WmanIfBsOfdmaMacVersion_Object = MibTableColumn
wmanIfBsOfdmaMacVersion = _WmanIfBsOfdmaMacVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 2, 1, 8),
    _WmanIfBsOfdmaMacVersion_Type()
)
wmanIfBsOfdmaMacVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaMacVersion.setStatus("current")


class _WmanIfBsOfdmaFrameDurationCode_Type(Integer32):
    """Custom type wmanIfBsOfdmaFrameDurationCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("aASGap", 0),
          ("duration2ms", 1),
          ("duration2dot5ms", 2),
          ("duration4ms", 3),
          ("duration5ms", 4),
          ("duration8ms", 5),
          ("duration10ms", 6),
          ("duration12dot5ms", 7),
          ("duration20ms", 8))
    )


_WmanIfBsOfdmaFrameDurationCode_Type.__name__ = "Integer32"
_WmanIfBsOfdmaFrameDurationCode_Object = MibTableColumn
wmanIfBsOfdmaFrameDurationCode = _WmanIfBsOfdmaFrameDurationCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 2, 1, 9),
    _WmanIfBsOfdmaFrameDurationCode_Type()
)
wmanIfBsOfdmaFrameDurationCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaFrameDurationCode.setStatus("current")


class _WmanIfBsOfdmaSizeCqichIdField_Type(Integer32):
    """Custom type wmanIfBsOfdmaSizeCqichIdField based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("threebits", 1),
          ("fourbits", 2),
          ("fivebits", 3),
          ("sixbits", 4),
          ("sevenbits", 5),
          ("eightbits", 6),
          ("ninebits", 7))
    )


_WmanIfBsOfdmaSizeCqichIdField_Type.__name__ = "Integer32"
_WmanIfBsOfdmaSizeCqichIdField_Object = MibTableColumn
wmanIfBsOfdmaSizeCqichIdField = _WmanIfBsOfdmaSizeCqichIdField_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 2, 1, 10),
    _WmanIfBsOfdmaSizeCqichIdField_Type()
)
wmanIfBsOfdmaSizeCqichIdField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaSizeCqichIdField.setStatus("current")


class _WmanIfBsOfdmaHARQAackDelayBurst_Type(Integer32):
    """Custom type wmanIfBsOfdmaHARQAackDelayBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneframeoffset", 1),
          ("twoframesoffset", 2),
          ("threeframesoffset", 3))
    )


_WmanIfBsOfdmaHARQAackDelayBurst_Type.__name__ = "Integer32"
_WmanIfBsOfdmaHARQAackDelayBurst_Object = MibTableColumn
wmanIfBsOfdmaHARQAackDelayBurst = _WmanIfBsOfdmaHARQAackDelayBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 2, 1, 11),
    _WmanIfBsOfdmaHARQAackDelayBurst_Type()
)
wmanIfBsOfdmaHARQAackDelayBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaHARQAackDelayBurst.setStatus("current")
_WmanIfBsOfdmaUcdBurstProfileTable_Object = MibTable
wmanIfBsOfdmaUcdBurstProfileTable = _WmanIfBsOfdmaUcdBurstProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmaUcdBurstProfileTable.setStatus("current")
_WmanIfBsOfdmaUcdBurstProfileEntry_Object = MibTableRow
wmanIfBsOfdmaUcdBurstProfileEntry = _WmanIfBsOfdmaUcdBurstProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 3, 1)
)
wmanIfBsOfdmaUcdBurstProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfBsOfdmaUiucIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmaUcdBurstProfileEntry.setStatus("current")


class _WmanIfBsOfdmaUiucIndex_Type(Integer32):
    """Custom type wmanIfBsOfdmaUiucIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WmanIfBsOfdmaUiucIndex_Type.__name__ = "Integer32"
_WmanIfBsOfdmaUiucIndex_Object = MibTableColumn
wmanIfBsOfdmaUiucIndex = _WmanIfBsOfdmaUiucIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 3, 1, 1),
    _WmanIfBsOfdmaUiucIndex_Type()
)
wmanIfBsOfdmaUiucIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaUiucIndex.setStatus("current")
_WmanIfBsOfdmaUcdFecCodeType_Type = WmanIfOfdmaFecCodeType
_WmanIfBsOfdmaUcdFecCodeType_Object = MibTableColumn
wmanIfBsOfdmaUcdFecCodeType = _WmanIfBsOfdmaUcdFecCodeType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 3, 1, 2),
    _WmanIfBsOfdmaUcdFecCodeType_Type()
)
wmanIfBsOfdmaUcdFecCodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaUcdFecCodeType.setStatus("current")


class _WmanIfBsOfdmaRangingDataRatio_Type(Integer32):
    """Custom type wmanIfBsOfdmaRangingDataRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaRangingDataRatio_Type.__name__ = "Integer32"
_WmanIfBsOfdmaRangingDataRatio_Object = MibTableColumn
wmanIfBsOfdmaRangingDataRatio = _WmanIfBsOfdmaRangingDataRatio_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 3, 1, 3),
    _WmanIfBsOfdmaRangingDataRatio_Type()
)
wmanIfBsOfdmaRangingDataRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaRangingDataRatio.setStatus("current")


class _WmanIfBsOfdmaNorCOverNOverride_Type(OctetString):
    """Custom type wmanIfBsOfdmaNorCOverNOverride based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixedLength = 5


_WmanIfBsOfdmaNorCOverNOverride_Type.__name__ = "OctetString"
_WmanIfBsOfdmaNorCOverNOverride_Object = MibTableColumn
wmanIfBsOfdmaNorCOverNOverride = _WmanIfBsOfdmaNorCOverNOverride_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 3, 1, 4),
    _WmanIfBsOfdmaNorCOverNOverride_Type()
)
wmanIfBsOfdmaNorCOverNOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaNorCOverNOverride.setStatus("current")
_WmanIfBsOfdmaUcdBurstProfileRowStatus_Type = RowStatus
_WmanIfBsOfdmaUcdBurstProfileRowStatus_Object = MibTableColumn
wmanIfBsOfdmaUcdBurstProfileRowStatus = _WmanIfBsOfdmaUcdBurstProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 3, 1, 5),
    _WmanIfBsOfdmaUcdBurstProfileRowStatus_Type()
)
wmanIfBsOfdmaUcdBurstProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaUcdBurstProfileRowStatus.setStatus("current")
_WmanIfBsOfdmaDcdBurstProfileTable_Object = MibTable
wmanIfBsOfdmaDcdBurstProfileTable = _WmanIfBsOfdmaDcdBurstProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 4)
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmaDcdBurstProfileTable.setStatus("current")
_WmanIfBsOfdmaDcdBurstProfileEntry_Object = MibTableRow
wmanIfBsOfdmaDcdBurstProfileEntry = _WmanIfBsOfdmaDcdBurstProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 4, 1)
)
wmanIfBsOfdmaDcdBurstProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfBsOfdmaDiucIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsOfdmaDcdBurstProfileEntry.setStatus("current")


class _WmanIfBsOfdmaDiucIndex_Type(Integer32):
    """Custom type wmanIfBsOfdmaDiucIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_WmanIfBsOfdmaDiucIndex_Type.__name__ = "Integer32"
_WmanIfBsOfdmaDiucIndex_Object = MibTableColumn
wmanIfBsOfdmaDiucIndex = _WmanIfBsOfdmaDiucIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 4, 1, 1),
    _WmanIfBsOfdmaDiucIndex_Type()
)
wmanIfBsOfdmaDiucIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaDiucIndex.setStatus("current")
_WmanIfBsOfdmaDownlinkFrequency_Type = Unsigned32
_WmanIfBsOfdmaDownlinkFrequency_Object = MibTableColumn
wmanIfBsOfdmaDownlinkFrequency = _WmanIfBsOfdmaDownlinkFrequency_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 4, 1, 2),
    _WmanIfBsOfdmaDownlinkFrequency_Type()
)
wmanIfBsOfdmaDownlinkFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaDownlinkFrequency.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaDownlinkFrequency.setUnits("kHz")
_WmanIfBsOfdmaDcdFecCodeType_Type = WmanIfOfdmaFecCodeType
_WmanIfBsOfdmaDcdFecCodeType_Object = MibTableColumn
wmanIfBsOfdmaDcdFecCodeType = _WmanIfBsOfdmaDcdFecCodeType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 4, 1, 3),
    _WmanIfBsOfdmaDcdFecCodeType_Type()
)
wmanIfBsOfdmaDcdFecCodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaDcdFecCodeType.setStatus("current")


class _WmanIfBsOfdmaDiucMandatoryExitThresh_Type(Integer32):
    """Custom type wmanIfBsOfdmaDiucMandatoryExitThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaDiucMandatoryExitThresh_Type.__name__ = "Integer32"
_WmanIfBsOfdmaDiucMandatoryExitThresh_Object = MibTableColumn
wmanIfBsOfdmaDiucMandatoryExitThresh = _WmanIfBsOfdmaDiucMandatoryExitThresh_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 4, 1, 4),
    _WmanIfBsOfdmaDiucMandatoryExitThresh_Type()
)
wmanIfBsOfdmaDiucMandatoryExitThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaDiucMandatoryExitThresh.setStatus("current")


class _WmanIfBsOfdmaDiucMinEntryThresh_Type(Integer32):
    """Custom type wmanIfBsOfdmaDiucMinEntryThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsOfdmaDiucMinEntryThresh_Type.__name__ = "Integer32"
_WmanIfBsOfdmaDiucMinEntryThresh_Object = MibTableColumn
wmanIfBsOfdmaDiucMinEntryThresh = _WmanIfBsOfdmaDiucMinEntryThresh_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 4, 1, 5),
    _WmanIfBsOfdmaDiucMinEntryThresh_Type()
)
wmanIfBsOfdmaDiucMinEntryThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaDiucMinEntryThresh.setStatus("current")
_WmanIfBsOfdmaDcdBurstProfileRowStatus_Type = RowStatus
_WmanIfBsOfdmaDcdBurstProfileRowStatus_Object = MibTableColumn
wmanIfBsOfdmaDcdBurstProfileRowStatus = _WmanIfBsOfdmaDcdBurstProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 6, 2, 4, 1, 6),
    _WmanIfBsOfdmaDcdBurstProfileRowStatus_Type()
)
wmanIfBsOfdmaDcdBurstProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsOfdmaDcdBurstProfileRowStatus.setStatus("current")
_WmanIfSsObjects_ObjectIdentity = ObjectIdentity
wmanIfSsObjects = _WmanIfSsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2)
)
_WmanIfSsCps_ObjectIdentity = ObjectIdentity
wmanIfSsCps = _WmanIfSsCps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1)
)
_WmanIfSsConfigurationTable_Object = MibTable
wmanIfSsConfigurationTable = _WmanIfSsConfigurationTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    wmanIfSsConfigurationTable.setStatus("current")
_WmanIfSsConfigurationEntry_Object = MibTableRow
wmanIfSsConfigurationEntry = _WmanIfSsConfigurationEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1)
)
wmanIfSsConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsConfigurationEntry.setStatus("current")


class _WmanIfSsLostDLMapInterval_Type(Integer32):
    """Custom type wmanIfSsLostDLMapInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_WmanIfSsLostDLMapInterval_Type.__name__ = "Integer32"
_WmanIfSsLostDLMapInterval_Object = MibTableColumn
wmanIfSsLostDLMapInterval = _WmanIfSsLostDLMapInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 1),
    _WmanIfSsLostDLMapInterval_Type()
)
wmanIfSsLostDLMapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsLostDLMapInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsLostDLMapInterval.setUnits("milliseconds")


class _WmanIfSsLostULMapInterval_Type(Integer32):
    """Custom type wmanIfSsLostULMapInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_WmanIfSsLostULMapInterval_Type.__name__ = "Integer32"
_WmanIfSsLostULMapInterval_Object = MibTableColumn
wmanIfSsLostULMapInterval = _WmanIfSsLostULMapInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 2),
    _WmanIfSsLostULMapInterval_Type()
)
wmanIfSsLostULMapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsLostULMapInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsLostULMapInterval.setUnits("milliseconds")


class _WmanIfSsContentionRangRetries_Type(Integer32):
    """Custom type wmanIfSsContentionRangRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 65535),
    )


_WmanIfSsContentionRangRetries_Type.__name__ = "Integer32"
_WmanIfSsContentionRangRetries_Object = MibTableColumn
wmanIfSsContentionRangRetries = _WmanIfSsContentionRangRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 3),
    _WmanIfSsContentionRangRetries_Type()
)
wmanIfSsContentionRangRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsContentionRangRetries.setStatus("current")


class _WmanIfSsRequestRetries_Type(Integer32):
    """Custom type wmanIfSsRequestRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 65535),
    )


_WmanIfSsRequestRetries_Type.__name__ = "Integer32"
_WmanIfSsRequestRetries_Object = MibTableColumn
wmanIfSsRequestRetries = _WmanIfSsRequestRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 4),
    _WmanIfSsRequestRetries_Type()
)
wmanIfSsRequestRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsRequestRetries.setStatus("current")


class _WmanIfSsRegRequestRetries_Type(Integer32):
    """Custom type wmanIfSsRegRequestRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_WmanIfSsRegRequestRetries_Type.__name__ = "Integer32"
_WmanIfSsRegRequestRetries_Object = MibTableColumn
wmanIfSsRegRequestRetries = _WmanIfSsRegRequestRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 5),
    _WmanIfSsRegRequestRetries_Type()
)
wmanIfSsRegRequestRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsRegRequestRetries.setStatus("current")


class _WmanIfSsTftpBackoffStart_Type(Integer32):
    """Custom type wmanIfSsTftpBackoffStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIfSsTftpBackoffStart_Type.__name__ = "Integer32"
_WmanIfSsTftpBackoffStart_Object = MibTableColumn
wmanIfSsTftpBackoffStart = _WmanIfSsTftpBackoffStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 6),
    _WmanIfSsTftpBackoffStart_Type()
)
wmanIfSsTftpBackoffStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsTftpBackoffStart.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsTftpBackoffStart.setUnits("seconds")


class _WmanIfSsTftpBackoffEnd_Type(Integer32):
    """Custom type wmanIfSsTftpBackoffEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 65535),
    )


_WmanIfSsTftpBackoffEnd_Type.__name__ = "Integer32"
_WmanIfSsTftpBackoffEnd_Object = MibTableColumn
wmanIfSsTftpBackoffEnd = _WmanIfSsTftpBackoffEnd_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 7),
    _WmanIfSsTftpBackoffEnd_Type()
)
wmanIfSsTftpBackoffEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsTftpBackoffEnd.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsTftpBackoffEnd.setUnits("seconds")


class _WmanIfSsTftpRequestRetries_Type(Integer32):
    """Custom type wmanIfSsTftpRequestRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 65535),
    )


_WmanIfSsTftpRequestRetries_Type.__name__ = "Integer32"
_WmanIfSsTftpRequestRetries_Object = MibTableColumn
wmanIfSsTftpRequestRetries = _WmanIfSsTftpRequestRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 8),
    _WmanIfSsTftpRequestRetries_Type()
)
wmanIfSsTftpRequestRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsTftpRequestRetries.setStatus("current")


class _WmanIfSsTftpDownloadRetries_Type(Integer32):
    """Custom type wmanIfSsTftpDownloadRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_WmanIfSsTftpDownloadRetries_Type.__name__ = "Integer32"
_WmanIfSsTftpDownloadRetries_Object = MibTableColumn
wmanIfSsTftpDownloadRetries = _WmanIfSsTftpDownloadRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 9),
    _WmanIfSsTftpDownloadRetries_Type()
)
wmanIfSsTftpDownloadRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsTftpDownloadRetries.setStatus("current")


class _WmanIfSsTftpWait_Type(Integer32):
    """Custom type wmanIfSsTftpWait based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_WmanIfSsTftpWait_Type.__name__ = "Integer32"
_WmanIfSsTftpWait_Object = MibTableColumn
wmanIfSsTftpWait = _WmanIfSsTftpWait_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 10),
    _WmanIfSsTftpWait_Type()
)
wmanIfSsTftpWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsTftpWait.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsTftpWait.setUnits("minutes")


class _WmanIfSsToDRetries_Type(Integer32):
    """Custom type wmanIfSsToDRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_WmanIfSsToDRetries_Type.__name__ = "Integer32"
_WmanIfSsToDRetries_Object = MibTableColumn
wmanIfSsToDRetries = _WmanIfSsToDRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 11),
    _WmanIfSsToDRetries_Type()
)
wmanIfSsToDRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsToDRetries.setStatus("current")


class _WmanIfSsToDRetryPeriod_Type(Integer32):
    """Custom type wmanIfSsToDRetryPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_WmanIfSsToDRetryPeriod_Type.__name__ = "Integer32"
_WmanIfSsToDRetryPeriod_Object = MibTableColumn
wmanIfSsToDRetryPeriod = _WmanIfSsToDRetryPeriod_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 12),
    _WmanIfSsToDRetryPeriod_Type()
)
wmanIfSsToDRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsToDRetryPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsToDRetryPeriod.setUnits("minutes")


class _WmanIfSsT1Timeout_Type(Integer32):
    """Custom type wmanIfSsT1Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_WmanIfSsT1Timeout_Type.__name__ = "Integer32"
_WmanIfSsT1Timeout_Object = MibTableColumn
wmanIfSsT1Timeout = _WmanIfSsT1Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 13),
    _WmanIfSsT1Timeout_Type()
)
wmanIfSsT1Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT1Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT1Timeout.setUnits("milliseconds")


class _WmanIfSsT2Timeout_Type(Integer32):
    """Custom type wmanIfSsT2Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WmanIfSsT2Timeout_Type.__name__ = "Integer32"
_WmanIfSsT2Timeout_Object = MibTableColumn
wmanIfSsT2Timeout = _WmanIfSsT2Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 14),
    _WmanIfSsT2Timeout_Type()
)
wmanIfSsT2Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT2Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT2Timeout.setUnits("milliseconds")


class _WmanIfSsT3Timeout_Type(Integer32):
    """Custom type wmanIfSsT3Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_WmanIfSsT3Timeout_Type.__name__ = "Integer32"
_WmanIfSsT3Timeout_Object = MibTableColumn
wmanIfSsT3Timeout = _WmanIfSsT3Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 15),
    _WmanIfSsT3Timeout_Type()
)
wmanIfSsT3Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT3Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT3Timeout.setUnits("milliseconds")


class _WmanIfSsT4Timeout_Type(Integer32):
    """Custom type wmanIfSsT4Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 35),
    )


_WmanIfSsT4Timeout_Type.__name__ = "Integer32"
_WmanIfSsT4Timeout_Object = MibTableColumn
wmanIfSsT4Timeout = _WmanIfSsT4Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 16),
    _WmanIfSsT4Timeout_Type()
)
wmanIfSsT4Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT4Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT4Timeout.setUnits("seconds")


class _WmanIfSsT6Timeout_Type(Integer32):
    """Custom type wmanIfSsT6Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_WmanIfSsT6Timeout_Type.__name__ = "Integer32"
_WmanIfSsT6Timeout_Object = MibTableColumn
wmanIfSsT6Timeout = _WmanIfSsT6Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 17),
    _WmanIfSsT6Timeout_Type()
)
wmanIfSsT6Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT6Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT6Timeout.setUnits("milliseconds")


class _WmanIfSsT12Timeout_Type(Integer32):
    """Custom type wmanIfSsT12Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_WmanIfSsT12Timeout_Type.__name__ = "Integer32"
_WmanIfSsT12Timeout_Object = MibTableColumn
wmanIfSsT12Timeout = _WmanIfSsT12Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 18),
    _WmanIfSsT12Timeout_Type()
)
wmanIfSsT12Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT12Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT12Timeout.setUnits("milliseconds")


class _WmanIfSsT14Timeout_Type(Integer32):
    """Custom type wmanIfSsT14Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_WmanIfSsT14Timeout_Type.__name__ = "Integer32"
_WmanIfSsT14Timeout_Object = MibTableColumn
wmanIfSsT14Timeout = _WmanIfSsT14Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 19),
    _WmanIfSsT14Timeout_Type()
)
wmanIfSsT14Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT14Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT14Timeout.setUnits("milliseconds")


class _WmanIfSsT16Timeout_Type(Integer32):
    """Custom type wmanIfSsT16Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_WmanIfSsT16Timeout_Type.__name__ = "Integer32"
_WmanIfSsT16Timeout_Object = MibTableColumn
wmanIfSsT16Timeout = _WmanIfSsT16Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 20),
    _WmanIfSsT16Timeout_Type()
)
wmanIfSsT16Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT16Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT16Timeout.setUnits("milliseconds")


class _WmanIfSsT18Timeout_Type(Integer32):
    """Custom type wmanIfSsT18Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfSsT18Timeout_Type.__name__ = "Integer32"
_WmanIfSsT18Timeout_Object = MibTableColumn
wmanIfSsT18Timeout = _WmanIfSsT18Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 21),
    _WmanIfSsT18Timeout_Type()
)
wmanIfSsT18Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT18Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT18Timeout.setUnits("milliseconds")


class _WmanIfSsT19Timeout_Type(Integer32):
    """Custom type wmanIfSsT19Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_WmanIfSsT19Timeout_Type.__name__ = "Integer32"
_WmanIfSsT19Timeout_Object = MibTableColumn
wmanIfSsT19Timeout = _WmanIfSsT19Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 22),
    _WmanIfSsT19Timeout_Type()
)
wmanIfSsT19Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT19Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT19Timeout.setUnits("milliseconds")


class _WmanIfSsT20Timeout_Type(Integer32):
    """Custom type wmanIfSsT20Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfSsT20Timeout_Type.__name__ = "Integer32"
_WmanIfSsT20Timeout_Object = MibTableColumn
wmanIfSsT20Timeout = _WmanIfSsT20Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 23),
    _WmanIfSsT20Timeout_Type()
)
wmanIfSsT20Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT20Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT20Timeout.setUnits("milliseconds")


class _WmanIfSsT21Timeout_Type(Integer32):
    """Custom type wmanIfSsT21Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WmanIfSsT21Timeout_Type.__name__ = "Integer32"
_WmanIfSsT21Timeout_Object = MibTableColumn
wmanIfSsT21Timeout = _WmanIfSsT21Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 24),
    _WmanIfSsT21Timeout_Type()
)
wmanIfSsT21Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT21Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT21Timeout.setUnits("milliseconds")


class _WmanIfSsSBCRequestRetries_Type(Integer32):
    """Custom type wmanIfSsSBCRequestRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 16),
    )


_WmanIfSsSBCRequestRetries_Type.__name__ = "Integer32"
_WmanIfSsSBCRequestRetries_Object = MibTableColumn
wmanIfSsSBCRequestRetries = _WmanIfSsSBCRequestRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 25),
    _WmanIfSsSBCRequestRetries_Type()
)
wmanIfSsSBCRequestRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsSBCRequestRetries.setStatus("current")


class _WmanIfSsTftpCpltRetries_Type(Integer32):
    """Custom type wmanIfSsTftpCpltRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 16),
    )


_WmanIfSsTftpCpltRetries_Type.__name__ = "Integer32"
_WmanIfSsTftpCpltRetries_Object = MibTableColumn
wmanIfSsTftpCpltRetries = _WmanIfSsTftpCpltRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 26),
    _WmanIfSsTftpCpltRetries_Type()
)
wmanIfSsTftpCpltRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsTftpCpltRetries.setStatus("current")


class _WmanIfSsT26Timeout_Type(Integer32):
    """Custom type wmanIfSsT26Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_WmanIfSsT26Timeout_Type.__name__ = "Integer32"
_WmanIfSsT26Timeout_Object = MibTableColumn
wmanIfSsT26Timeout = _WmanIfSsT26Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 27),
    _WmanIfSsT26Timeout_Type()
)
wmanIfSsT26Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT26Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT26Timeout.setUnits("milliseconds")


class _WmanIfSsDLManagProcTime_Type(Integer32):
    """Custom type wmanIfSsDLManagProcTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_WmanIfSsDLManagProcTime_Type.__name__ = "Integer32"
_WmanIfSsDLManagProcTime_Object = MibTableColumn
wmanIfSsDLManagProcTime = _WmanIfSsDLManagProcTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 28),
    _WmanIfSsDLManagProcTime_Type()
)
wmanIfSsDLManagProcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsDLManagProcTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsDLManagProcTime.setUnits("micro seconds")
_WmanIfSsChannelMeasurementTable_Object = MibTable
wmanIfSsChannelMeasurementTable = _WmanIfSsChannelMeasurementTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    wmanIfSsChannelMeasurementTable.setStatus("current")
_WmanIfSsChannelMeasurementEntry_Object = MibTableRow
wmanIfSsChannelMeasurementEntry = _WmanIfSsChannelMeasurementEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1)
)
wmanIfSsChannelMeasurementEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfSsHistogramIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsChannelMeasurementEntry.setStatus("current")


class _WmanIfSsHistogramIndex_Type(Unsigned32):
    """Custom type wmanIfSsHistogramIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfSsHistogramIndex_Type.__name__ = "Unsigned32"
_WmanIfSsHistogramIndex_Object = MibTableColumn
wmanIfSsHistogramIndex = _WmanIfSsHistogramIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 1),
    _WmanIfSsHistogramIndex_Type()
)
wmanIfSsHistogramIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfSsHistogramIndex.setStatus("current")
_WmanIfSsChannelNumber_Type = WmanIfChannelNumber
_WmanIfSsChannelNumber_Object = MibTableColumn
wmanIfSsChannelNumber = _WmanIfSsChannelNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 2),
    _WmanIfSsChannelNumber_Type()
)
wmanIfSsChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsChannelNumber.setStatus("current")


class _WmanIfSsStartFrame_Type(Integer32):
    """Custom type wmanIfSsStartFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfSsStartFrame_Type.__name__ = "Integer32"
_WmanIfSsStartFrame_Object = MibTableColumn
wmanIfSsStartFrame = _WmanIfSsStartFrame_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 3),
    _WmanIfSsStartFrame_Type()
)
wmanIfSsStartFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsStartFrame.setStatus("current")


class _WmanIfSsDuration_Type(Integer32):
    """Custom type wmanIfSsDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_WmanIfSsDuration_Type.__name__ = "Integer32"
_WmanIfSsDuration_Object = MibTableColumn
wmanIfSsDuration = _WmanIfSsDuration_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 4),
    _WmanIfSsDuration_Type()
)
wmanIfSsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsDuration.setStatus("current")


class _WmanIfSsBasicReport_Type(Bits):
    """Custom type wmanIfSsBasicReport based on Bits"""
    namedValues = NamedValues(
        *(("wirelessHuman", 0),
          ("unknownTransmission", 1),
          ("primaryUser", 2),
          ("channelNotMeasured", 3))
    )

_WmanIfSsBasicReport_Type.__name__ = "Bits"
_WmanIfSsBasicReport_Object = MibTableColumn
wmanIfSsBasicReport = _WmanIfSsBasicReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 5),
    _WmanIfSsBasicReport_Type()
)
wmanIfSsBasicReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsBasicReport.setStatus("current")


class _WmanIfSsMeanCinrReport_Type(Integer32):
    """Custom type wmanIfSsMeanCinrReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_WmanIfSsMeanCinrReport_Type.__name__ = "Integer32"
_WmanIfSsMeanCinrReport_Object = MibTableColumn
wmanIfSsMeanCinrReport = _WmanIfSsMeanCinrReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 6),
    _WmanIfSsMeanCinrReport_Type()
)
wmanIfSsMeanCinrReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsMeanCinrReport.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsMeanCinrReport.setUnits("dB")


class _WmanIfSsStdDeviationCinrReport_Type(Integer32):
    """Custom type wmanIfSsStdDeviationCinrReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_WmanIfSsStdDeviationCinrReport_Type.__name__ = "Integer32"
_WmanIfSsStdDeviationCinrReport_Object = MibTableColumn
wmanIfSsStdDeviationCinrReport = _WmanIfSsStdDeviationCinrReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 7),
    _WmanIfSsStdDeviationCinrReport_Type()
)
wmanIfSsStdDeviationCinrReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsStdDeviationCinrReport.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsStdDeviationCinrReport.setUnits("dB")


class _WmanIfSsMeanRssiReport_Type(Integer32):
    """Custom type wmanIfSsMeanRssiReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_WmanIfSsMeanRssiReport_Type.__name__ = "Integer32"
_WmanIfSsMeanRssiReport_Object = MibTableColumn
wmanIfSsMeanRssiReport = _WmanIfSsMeanRssiReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 8),
    _WmanIfSsMeanRssiReport_Type()
)
wmanIfSsMeanRssiReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsMeanRssiReport.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsMeanRssiReport.setUnits("dBm")


class _WmanIfSsStdDeviationRssiReport_Type(Integer32):
    """Custom type wmanIfSsStdDeviationRssiReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_WmanIfSsStdDeviationRssiReport_Type.__name__ = "Integer32"
_WmanIfSsStdDeviationRssiReport_Object = MibTableColumn
wmanIfSsStdDeviationRssiReport = _WmanIfSsStdDeviationRssiReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 9),
    _WmanIfSsStdDeviationRssiReport_Type()
)
wmanIfSsStdDeviationRssiReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsStdDeviationRssiReport.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsStdDeviationRssiReport.setUnits("dB")
_WmanIfSsPkmObjects_ObjectIdentity = ObjectIdentity
wmanIfSsPkmObjects = _WmanIfSsPkmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2)
)
_WmanIfSsPkmAuthTable_Object = MibTable
wmanIfSsPkmAuthTable = _WmanIfSsPkmAuthTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthTable.setStatus("current")
_WmanIfSsPkmAuthEntry_Object = MibTableRow
wmanIfSsPkmAuthEntry = _WmanIfSsPkmAuthEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1)
)
wmanIfSsPkmAuthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthEntry.setStatus("current")


class _WmanIfSsPkmAuthState_Type(Integer32):
    """Custom type wmanIfSsPkmAuthState based on Integer32"""
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
        *(("start", 1),
          ("authWait", 2),
          ("authorized", 3),
          ("reauthWait", 4),
          ("authRejectWait", 5),
          ("silent", 6))
    )


_WmanIfSsPkmAuthState_Type.__name__ = "Integer32"
_WmanIfSsPkmAuthState_Object = MibTableColumn
wmanIfSsPkmAuthState = _WmanIfSsPkmAuthState_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 1),
    _WmanIfSsPkmAuthState_Type()
)
wmanIfSsPkmAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthState.setStatus("current")


class _WmanIfSsPkmAuthKeySequenceNumber_Type(Integer32):
    """Custom type wmanIfSsPkmAuthKeySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIfSsPkmAuthKeySequenceNumber_Type.__name__ = "Integer32"
_WmanIfSsPkmAuthKeySequenceNumber_Object = MibTableColumn
wmanIfSsPkmAuthKeySequenceNumber = _WmanIfSsPkmAuthKeySequenceNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 2),
    _WmanIfSsPkmAuthKeySequenceNumber_Type()
)
wmanIfSsPkmAuthKeySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthKeySequenceNumber.setStatus("current")
_WmanIfSsPkmAuthExpiresOld_Type = DateAndTime
_WmanIfSsPkmAuthExpiresOld_Object = MibTableColumn
wmanIfSsPkmAuthExpiresOld = _WmanIfSsPkmAuthExpiresOld_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 3),
    _WmanIfSsPkmAuthExpiresOld_Type()
)
wmanIfSsPkmAuthExpiresOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthExpiresOld.setStatus("current")
_WmanIfSsPkmAuthExpiresNew_Type = DateAndTime
_WmanIfSsPkmAuthExpiresNew_Object = MibTableColumn
wmanIfSsPkmAuthExpiresNew = _WmanIfSsPkmAuthExpiresNew_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 4),
    _WmanIfSsPkmAuthExpiresNew_Type()
)
wmanIfSsPkmAuthExpiresNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthExpiresNew.setStatus("current")
_WmanIfSsPkmAuthReset_Type = TruthValue
_WmanIfSsPkmAuthReset_Object = MibTableColumn
wmanIfSsPkmAuthReset = _WmanIfSsPkmAuthReset_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 5),
    _WmanIfSsPkmAuthReset_Type()
)
wmanIfSsPkmAuthReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthReset.setStatus("current")
_WmanIfSsPkmAuthentInfos_Type = Counter32
_WmanIfSsPkmAuthentInfos_Object = MibTableColumn
wmanIfSsPkmAuthentInfos = _WmanIfSsPkmAuthentInfos_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 6),
    _WmanIfSsPkmAuthentInfos_Type()
)
wmanIfSsPkmAuthentInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthentInfos.setStatus("current")
_WmanIfSsPkmAuthRequests_Type = Counter32
_WmanIfSsPkmAuthRequests_Object = MibTableColumn
wmanIfSsPkmAuthRequests = _WmanIfSsPkmAuthRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 7),
    _WmanIfSsPkmAuthRequests_Type()
)
wmanIfSsPkmAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthRequests.setStatus("current")
_WmanIfSsPkmAuthReplies_Type = Counter32
_WmanIfSsPkmAuthReplies_Object = MibTableColumn
wmanIfSsPkmAuthReplies = _WmanIfSsPkmAuthReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 8),
    _WmanIfSsPkmAuthReplies_Type()
)
wmanIfSsPkmAuthReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthReplies.setStatus("current")
_WmanIfSsPkmAuthRejects_Type = Counter32
_WmanIfSsPkmAuthRejects_Object = MibTableColumn
wmanIfSsPkmAuthRejects = _WmanIfSsPkmAuthRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 9),
    _WmanIfSsPkmAuthRejects_Type()
)
wmanIfSsPkmAuthRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthRejects.setStatus("current")
_WmanIfSsPkmAuthInvalids_Type = Counter32
_WmanIfSsPkmAuthInvalids_Object = MibTableColumn
wmanIfSsPkmAuthInvalids = _WmanIfSsPkmAuthInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 10),
    _WmanIfSsPkmAuthInvalids_Type()
)
wmanIfSsPkmAuthInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthInvalids.setStatus("current")


class _WmanIfSsPkmAuthRejectErrorCode_Type(Integer32):
    """Custom type wmanIfSsPkmAuthRejectErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              11)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("unauthorizedSs", 3),
          ("unauthorizedSaid", 4),
          ("permanentAuthorizationFailure", 8),
          ("timeOfDayNotAcquired", 11))
    )


_WmanIfSsPkmAuthRejectErrorCode_Type.__name__ = "Integer32"
_WmanIfSsPkmAuthRejectErrorCode_Object = MibTableColumn
wmanIfSsPkmAuthRejectErrorCode = _WmanIfSsPkmAuthRejectErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 11),
    _WmanIfSsPkmAuthRejectErrorCode_Type()
)
wmanIfSsPkmAuthRejectErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthRejectErrorCode.setStatus("current")


class _WmanIfSsPkmAuthRejectErrorString_Type(SnmpAdminString):
    """Custom type wmanIfSsPkmAuthRejectErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WmanIfSsPkmAuthRejectErrorString_Type.__name__ = "SnmpAdminString"
_WmanIfSsPkmAuthRejectErrorString_Object = MibTableColumn
wmanIfSsPkmAuthRejectErrorString = _WmanIfSsPkmAuthRejectErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 12),
    _WmanIfSsPkmAuthRejectErrorString_Type()
)
wmanIfSsPkmAuthRejectErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthRejectErrorString.setStatus("current")


class _WmanIfSsPkmAuthInvalidErrorCode_Type(Integer32):
    """Custom type wmanIfSsPkmAuthInvalidErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("unauthorizedSs", 3),
          ("unsolicited", 5),
          ("invalidKeySequence", 6),
          ("keyRequestAuthenticationFailure", 7))
    )


_WmanIfSsPkmAuthInvalidErrorCode_Type.__name__ = "Integer32"
_WmanIfSsPkmAuthInvalidErrorCode_Object = MibTableColumn
wmanIfSsPkmAuthInvalidErrorCode = _WmanIfSsPkmAuthInvalidErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 13),
    _WmanIfSsPkmAuthInvalidErrorCode_Type()
)
wmanIfSsPkmAuthInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthInvalidErrorCode.setStatus("current")


class _WmanIfSsPkmAuthInvalidErrorString_Type(SnmpAdminString):
    """Custom type wmanIfSsPkmAuthInvalidErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WmanIfSsPkmAuthInvalidErrorString_Type.__name__ = "SnmpAdminString"
_WmanIfSsPkmAuthInvalidErrorString_Object = MibTableColumn
wmanIfSsPkmAuthInvalidErrorString = _WmanIfSsPkmAuthInvalidErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 14),
    _WmanIfSsPkmAuthInvalidErrorString_Type()
)
wmanIfSsPkmAuthInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthInvalidErrorString.setStatus("current")


class _WmanIfSsPkmAuthGraceTime_Type(Integer32):
    """Custom type wmanIfSsPkmAuthGraceTime based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3024000),
    )


_WmanIfSsPkmAuthGraceTime_Type.__name__ = "Integer32"
_WmanIfSsPkmAuthGraceTime_Object = MibTableColumn
wmanIfSsPkmAuthGraceTime = _WmanIfSsPkmAuthGraceTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 15),
    _WmanIfSsPkmAuthGraceTime_Type()
)
wmanIfSsPkmAuthGraceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthGraceTime.setUnits("seconds")


class _WmanIfSsPkmTekGraceTime_Type(Integer32):
    """Custom type wmanIfSsPkmTekGraceTime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3024000),
    )


_WmanIfSsPkmTekGraceTime_Type.__name__ = "Integer32"
_WmanIfSsPkmTekGraceTime_Object = MibTableColumn
wmanIfSsPkmTekGraceTime = _WmanIfSsPkmTekGraceTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 16),
    _WmanIfSsPkmTekGraceTime_Type()
)
wmanIfSsPkmTekGraceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekGraceTime.setUnits("seconds")


class _WmanIfSsPkmAuthWaitTimeout_Type(Integer32):
    """Custom type wmanIfSsPkmAuthWaitTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_WmanIfSsPkmAuthWaitTimeout_Type.__name__ = "Integer32"
_WmanIfSsPkmAuthWaitTimeout_Object = MibTableColumn
wmanIfSsPkmAuthWaitTimeout = _WmanIfSsPkmAuthWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 17),
    _WmanIfSsPkmAuthWaitTimeout_Type()
)
wmanIfSsPkmAuthWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthWaitTimeout.setUnits("seconds")


class _WmanIfSsPkmReauthWaitTimeout_Type(Integer32):
    """Custom type wmanIfSsPkmReauthWaitTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_WmanIfSsPkmReauthWaitTimeout_Type.__name__ = "Integer32"
_WmanIfSsPkmReauthWaitTimeout_Object = MibTableColumn
wmanIfSsPkmReauthWaitTimeout = _WmanIfSsPkmReauthWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 18),
    _WmanIfSsPkmReauthWaitTimeout_Type()
)
wmanIfSsPkmReauthWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmReauthWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsPkmReauthWaitTimeout.setUnits("seconds")


class _WmanIfSsPkmOpWaitTimeout_Type(Integer32):
    """Custom type wmanIfSsPkmOpWaitTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WmanIfSsPkmOpWaitTimeout_Type.__name__ = "Integer32"
_WmanIfSsPkmOpWaitTimeout_Object = MibTableColumn
wmanIfSsPkmOpWaitTimeout = _WmanIfSsPkmOpWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 19),
    _WmanIfSsPkmOpWaitTimeout_Type()
)
wmanIfSsPkmOpWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmOpWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsPkmOpWaitTimeout.setUnits("seconds")


class _WmanIfSsPkmRekeyWaitTimeout_Type(Integer32):
    """Custom type wmanIfSsPkmRekeyWaitTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WmanIfSsPkmRekeyWaitTimeout_Type.__name__ = "Integer32"
_WmanIfSsPkmRekeyWaitTimeout_Object = MibTableColumn
wmanIfSsPkmRekeyWaitTimeout = _WmanIfSsPkmRekeyWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 20),
    _WmanIfSsPkmRekeyWaitTimeout_Type()
)
wmanIfSsPkmRekeyWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmRekeyWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsPkmRekeyWaitTimeout.setUnits("seconds")


class _WmanIfSsPkmAuthRejectWaitTimeout_Type(Integer32):
    """Custom type wmanIfSsPkmAuthRejectWaitTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_WmanIfSsPkmAuthRejectWaitTimeout_Type.__name__ = "Integer32"
_WmanIfSsPkmAuthRejectWaitTimeout_Object = MibTableColumn
wmanIfSsPkmAuthRejectWaitTimeout = _WmanIfSsPkmAuthRejectWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 21),
    _WmanIfSsPkmAuthRejectWaitTimeout_Type()
)
wmanIfSsPkmAuthRejectWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthRejectWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthRejectWaitTimeout.setUnits("seconds")
_WmanIfSsPkmTekTable_Object = MibTable
wmanIfSsPkmTekTable = _WmanIfSsPkmTekTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    wmanIfSsPkmTekTable.setStatus("current")
_WmanIfSsPkmTekEntry_Object = MibTableRow
wmanIfSsPkmTekEntry = _WmanIfSsPkmTekEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1)
)
wmanIfSsPkmTekEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfSsPkmTekSAId"),
)
if mibBuilder.loadTexts:
    wmanIfSsPkmTekEntry.setStatus("current")


class _WmanIfSsPkmTekSAId_Type(Integer32):
    """Custom type wmanIfSsPkmTekSAId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfSsPkmTekSAId_Type.__name__ = "Integer32"
_WmanIfSsPkmTekSAId_Object = MibTableColumn
wmanIfSsPkmTekSAId = _WmanIfSsPkmTekSAId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 1),
    _WmanIfSsPkmTekSAId_Type()
)
wmanIfSsPkmTekSAId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekSAId.setStatus("current")


class _WmanIfSsPkmTekSAType_Type(Integer32):
    """Custom type wmanIfSsPkmTekSAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primarySA", 0),
          ("staticSA", 1),
          ("dynamicSA", 2))
    )


_WmanIfSsPkmTekSAType_Type.__name__ = "Integer32"
_WmanIfSsPkmTekSAType_Object = MibTableColumn
wmanIfSsPkmTekSAType = _WmanIfSsPkmTekSAType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 2),
    _WmanIfSsPkmTekSAType_Type()
)
wmanIfSsPkmTekSAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekSAType.setStatus("current")
_WmanIfSsPkmTekDataEncryptAlg_Type = WmanIfDataEncryptAlgId
_WmanIfSsPkmTekDataEncryptAlg_Object = MibTableColumn
wmanIfSsPkmTekDataEncryptAlg = _WmanIfSsPkmTekDataEncryptAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 3),
    _WmanIfSsPkmTekDataEncryptAlg_Type()
)
wmanIfSsPkmTekDataEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekDataEncryptAlg.setStatus("current")
_WmanIfSsPkmTekDataAuthentAlg_Type = WmanIfDataAuthAlgId
_WmanIfSsPkmTekDataAuthentAlg_Object = MibTableColumn
wmanIfSsPkmTekDataAuthentAlg = _WmanIfSsPkmTekDataAuthentAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 4),
    _WmanIfSsPkmTekDataAuthentAlg_Type()
)
wmanIfSsPkmTekDataAuthentAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekDataAuthentAlg.setStatus("current")
_WmanIfSsPkmTekEncryptAlg_Type = WmanIfTekEncryptAlgId
_WmanIfSsPkmTekEncryptAlg_Object = MibTableColumn
wmanIfSsPkmTekEncryptAlg = _WmanIfSsPkmTekEncryptAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 5),
    _WmanIfSsPkmTekEncryptAlg_Type()
)
wmanIfSsPkmTekEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekEncryptAlg.setStatus("current")


class _WmanIfSsPkmTekState_Type(Integer32):
    """Custom type wmanIfSsPkmTekState based on Integer32"""
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
        *(("start", 1),
          ("opWait", 2),
          ("opReauthWait", 3),
          ("operational", 4),
          ("rekeyWait", 5),
          ("rekeyReauthWait", 6))
    )


_WmanIfSsPkmTekState_Type.__name__ = "Integer32"
_WmanIfSsPkmTekState_Object = MibTableColumn
wmanIfSsPkmTekState = _WmanIfSsPkmTekState_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 6),
    _WmanIfSsPkmTekState_Type()
)
wmanIfSsPkmTekState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekState.setStatus("current")


class _WmanIfSsPkmTekKeySequenceNumber_Type(Integer32):
    """Custom type wmanIfSsPkmTekKeySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WmanIfSsPkmTekKeySequenceNumber_Type.__name__ = "Integer32"
_WmanIfSsPkmTekKeySequenceNumber_Object = MibTableColumn
wmanIfSsPkmTekKeySequenceNumber = _WmanIfSsPkmTekKeySequenceNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 7),
    _WmanIfSsPkmTekKeySequenceNumber_Type()
)
wmanIfSsPkmTekKeySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekKeySequenceNumber.setStatus("current")
_WmanIfSsPkmTekExpiresOld_Type = DateAndTime
_WmanIfSsPkmTekExpiresOld_Object = MibTableColumn
wmanIfSsPkmTekExpiresOld = _WmanIfSsPkmTekExpiresOld_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 8),
    _WmanIfSsPkmTekExpiresOld_Type()
)
wmanIfSsPkmTekExpiresOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekExpiresOld.setStatus("current")
_WmanIfSsPkmTekExpiresNew_Type = DateAndTime
_WmanIfSsPkmTekExpiresNew_Object = MibTableColumn
wmanIfSsPkmTekExpiresNew = _WmanIfSsPkmTekExpiresNew_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 9),
    _WmanIfSsPkmTekExpiresNew_Type()
)
wmanIfSsPkmTekExpiresNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekExpiresNew.setStatus("current")
_WmanIfSsPkmTekKeyRequests_Type = Counter32
_WmanIfSsPkmTekKeyRequests_Object = MibTableColumn
wmanIfSsPkmTekKeyRequests = _WmanIfSsPkmTekKeyRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 10),
    _WmanIfSsPkmTekKeyRequests_Type()
)
wmanIfSsPkmTekKeyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekKeyRequests.setStatus("current")
_WmanIfSsPkmTekKeyReplies_Type = Counter32
_WmanIfSsPkmTekKeyReplies_Object = MibTableColumn
wmanIfSsPkmTekKeyReplies = _WmanIfSsPkmTekKeyReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 11),
    _WmanIfSsPkmTekKeyReplies_Type()
)
wmanIfSsPkmTekKeyReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekKeyReplies.setStatus("current")
_WmanIfSsPkmTekKeyRejects_Type = Counter32
_WmanIfSsPkmTekKeyRejects_Object = MibTableColumn
wmanIfSsPkmTekKeyRejects = _WmanIfSsPkmTekKeyRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 12),
    _WmanIfSsPkmTekKeyRejects_Type()
)
wmanIfSsPkmTekKeyRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekKeyRejects.setStatus("current")
_WmanIfSsPkmTekInvalids_Type = Counter32
_WmanIfSsPkmTekInvalids_Object = MibTableColumn
wmanIfSsPkmTekInvalids = _WmanIfSsPkmTekInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 13),
    _WmanIfSsPkmTekInvalids_Type()
)
wmanIfSsPkmTekInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekInvalids.setStatus("current")
_WmanIfSsPkmTekAuthPends_Type = Counter32
_WmanIfSsPkmTekAuthPends_Object = MibTableColumn
wmanIfSsPkmTekAuthPends = _WmanIfSsPkmTekAuthPends_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 14),
    _WmanIfSsPkmTekAuthPends_Type()
)
wmanIfSsPkmTekAuthPends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekAuthPends.setStatus("current")


class _WmanIfSsPkmTekKeyRejectErrorCode_Type(Integer32):
    """Custom type wmanIfSsPkmTekKeyRejectErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("unauthorizedSaid", 4))
    )


_WmanIfSsPkmTekKeyRejectErrorCode_Type.__name__ = "Integer32"
_WmanIfSsPkmTekKeyRejectErrorCode_Object = MibTableColumn
wmanIfSsPkmTekKeyRejectErrorCode = _WmanIfSsPkmTekKeyRejectErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 15),
    _WmanIfSsPkmTekKeyRejectErrorCode_Type()
)
wmanIfSsPkmTekKeyRejectErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekKeyRejectErrorCode.setStatus("current")


class _WmanIfSsPkmTekKeyRejectErrorString_Type(SnmpAdminString):
    """Custom type wmanIfSsPkmTekKeyRejectErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WmanIfSsPkmTekKeyRejectErrorString_Type.__name__ = "SnmpAdminString"
_WmanIfSsPkmTekKeyRejectErrorString_Object = MibTableColumn
wmanIfSsPkmTekKeyRejectErrorString = _WmanIfSsPkmTekKeyRejectErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 16),
    _WmanIfSsPkmTekKeyRejectErrorString_Type()
)
wmanIfSsPkmTekKeyRejectErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekKeyRejectErrorString.setStatus("current")


class _WmanIfSsPkmTekInvalidErrorCode_Type(Integer32):
    """Custom type wmanIfSsPkmTekInvalidErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("invalidKeySequence", 6))
    )


_WmanIfSsPkmTekInvalidErrorCode_Type.__name__ = "Integer32"
_WmanIfSsPkmTekInvalidErrorCode_Object = MibTableColumn
wmanIfSsPkmTekInvalidErrorCode = _WmanIfSsPkmTekInvalidErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 17),
    _WmanIfSsPkmTekInvalidErrorCode_Type()
)
wmanIfSsPkmTekInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekInvalidErrorCode.setStatus("current")


class _WmanIfSsPkmTekInvalidErrorString_Type(SnmpAdminString):
    """Custom type wmanIfSsPkmTekInvalidErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WmanIfSsPkmTekInvalidErrorString_Type.__name__ = "SnmpAdminString"
_WmanIfSsPkmTekInvalidErrorString_Object = MibTableColumn
wmanIfSsPkmTekInvalidErrorString = _WmanIfSsPkmTekInvalidErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 18),
    _WmanIfSsPkmTekInvalidErrorString_Type()
)
wmanIfSsPkmTekInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTekInvalidErrorString.setStatus("current")
_WmanIfSsDeviceCertTable_Object = MibTable
wmanIfSsDeviceCertTable = _WmanIfSsDeviceCertTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    wmanIfSsDeviceCertTable.setStatus("current")
_WmanIfSsDeviceCertEntry_Object = MibTableRow
wmanIfSsDeviceCertEntry = _WmanIfSsDeviceCertEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1)
)
wmanIfSsDeviceCertEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsDeviceCertEntry.setStatus("current")


class _WmanIfSsDeviceCert_Type(OctetString):
    """Custom type wmanIfSsDeviceCert based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_WmanIfSsDeviceCert_Type.__name__ = "OctetString"
_WmanIfSsDeviceCert_Object = MibTableColumn
wmanIfSsDeviceCert = _WmanIfSsDeviceCert_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 1),
    _WmanIfSsDeviceCert_Type()
)
wmanIfSsDeviceCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsDeviceCert.setStatus("current")


class _WmanIfSsDeviceManufCert_Type(OctetString):
    """Custom type wmanIfSsDeviceManufCert based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_WmanIfSsDeviceManufCert_Type.__name__ = "OctetString"
_WmanIfSsDeviceManufCert_Object = MibTableColumn
wmanIfSsDeviceManufCert = _WmanIfSsDeviceManufCert_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 2),
    _WmanIfSsDeviceManufCert_Type()
)
wmanIfSsDeviceManufCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsDeviceManufCert.setStatus("current")
_WmanIfSsNotification_ObjectIdentity = ObjectIdentity
wmanIfSsNotification = _WmanIfSsNotification_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3)
)
_WmanIfSsTrapControl_ObjectIdentity = ObjectIdentity
wmanIfSsTrapControl = _WmanIfSsTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1)
)


class _WmanIfSsTrapControlRegister_Type(Bits):
    """Custom type wmanIfSsTrapControlRegister based on Bits"""
    namedValues = NamedValues(
        *(("wmanIfSsTlvUnknown", 0),
          ("wmanIfSsDynamicServiceFail", 1),
          ("wmanIfSsDhcpSuccess", 2),
          ("wmanIfSsRssiStatusChange", 3))
    )

_WmanIfSsTrapControlRegister_Type.__name__ = "Bits"
_WmanIfSsTrapControlRegister_Object = MibScalar
wmanIfSsTrapControlRegister = _WmanIfSsTrapControlRegister_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1, 1),
    _WmanIfSsTrapControlRegister_Type()
)
wmanIfSsTrapControlRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsTrapControlRegister.setStatus("current")
_WmanIfSsThresholdConfigTable_Object = MibTable
wmanIfSsThresholdConfigTable = _WmanIfSsThresholdConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    wmanIfSsThresholdConfigTable.setStatus("current")
_WmanIfSsThresholdConfigEntry_Object = MibTableRow
wmanIfSsThresholdConfigEntry = _WmanIfSsThresholdConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1, 2, 1)
)
wmanIfSsThresholdConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsThresholdConfigEntry.setStatus("current")
_WmanIfSsRssiLowThreshold_Type = Integer32
_WmanIfSsRssiLowThreshold_Object = MibTableColumn
wmanIfSsRssiLowThreshold = _WmanIfSsRssiLowThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1, 2, 1, 1),
    _WmanIfSsRssiLowThreshold_Type()
)
wmanIfSsRssiLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsRssiLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsRssiLowThreshold.setUnits("dBm")
_WmanIfSsRssiHighThreshold_Type = Integer32
_WmanIfSsRssiHighThreshold_Object = MibTableColumn
wmanIfSsRssiHighThreshold = _WmanIfSsRssiHighThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1, 2, 1, 2),
    _WmanIfSsRssiHighThreshold_Type()
)
wmanIfSsRssiHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsRssiHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsRssiHighThreshold.setUnits("dBm")
_WmanIfSsTrapDefinitions_ObjectIdentity = ObjectIdentity
wmanIfSsTrapDefinitions = _WmanIfSsTrapDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2)
)
_WmanIfSsTrapPrefix_ObjectIdentity = ObjectIdentity
wmanIfSsTrapPrefix = _WmanIfSsTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2, 0)
)
_WmanIfSsNotificationObjectsTable_Object = MibTable
wmanIfSsNotificationObjectsTable = _WmanIfSsNotificationObjectsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIfSsNotificationObjectsTable.setStatus("current")
_WmanIfSsNotificationObjectsEntry_Object = MibTableRow
wmanIfSsNotificationObjectsEntry = _WmanIfSsNotificationObjectsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2, 1, 1)
)
wmanIfSsNotificationObjectsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsNotificationObjectsEntry.setStatus("current")
_WmanIfSsMacAddress_Type = MacAddress
_WmanIfSsMacAddress_Object = MibTableColumn
wmanIfSsMacAddress = _WmanIfSsMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2, 1, 1, 1),
    _WmanIfSsMacAddress_Type()
)
wmanIfSsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsMacAddress.setStatus("current")


class _WmanIfSsUnknownTlv_Type(OctetString):
    """Custom type wmanIfSsUnknownTlv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_WmanIfSsUnknownTlv_Type.__name__ = "OctetString"
_WmanIfSsUnknownTlv_Object = MibTableColumn
wmanIfSsUnknownTlv = _WmanIfSsUnknownTlv_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2, 1, 1, 2),
    _WmanIfSsUnknownTlv_Type()
)
wmanIfSsUnknownTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsUnknownTlv.setStatus("current")


class _WmanIfSsDynamicServiceType_Type(Integer32):
    """Custom type wmanIfSsDynamicServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ssSfCreationReq", 1),
          ("ssSfCreationRsp", 2),
          ("ssSfCreationAck", 3))
    )


_WmanIfSsDynamicServiceType_Type.__name__ = "Integer32"
_WmanIfSsDynamicServiceType_Object = MibTableColumn
wmanIfSsDynamicServiceType = _WmanIfSsDynamicServiceType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2, 1, 1, 3),
    _WmanIfSsDynamicServiceType_Type()
)
wmanIfSsDynamicServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsDynamicServiceType.setStatus("current")


class _WmanIfSsDynamicServiceFailReason_Type(OctetString):
    """Custom type wmanIfSsDynamicServiceFailReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WmanIfSsDynamicServiceFailReason_Type.__name__ = "OctetString"
_WmanIfSsDynamicServiceFailReason_Object = MibTableColumn
wmanIfSsDynamicServiceFailReason = _WmanIfSsDynamicServiceFailReason_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2, 1, 1, 4),
    _WmanIfSsDynamicServiceFailReason_Type()
)
wmanIfSsDynamicServiceFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsDynamicServiceFailReason.setStatus("current")


class _WmanIfSsRssiStatus_Type(Integer32):
    """Custom type wmanIfSsRssiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ssRssiAlarm", 1),
          ("ssRssiNoAlarm", 2))
    )


_WmanIfSsRssiStatus_Type.__name__ = "Integer32"
_WmanIfSsRssiStatus_Object = MibTableColumn
wmanIfSsRssiStatus = _WmanIfSsRssiStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2, 1, 1, 5),
    _WmanIfSsRssiStatus_Type()
)
wmanIfSsRssiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsRssiStatus.setStatus("current")


class _WmanIfSsRssiStatusInfo_Type(OctetString):
    """Custom type wmanIfSsRssiStatusInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WmanIfSsRssiStatusInfo_Type.__name__ = "OctetString"
_WmanIfSsRssiStatusInfo_Object = MibTableColumn
wmanIfSsRssiStatusInfo = _WmanIfSsRssiStatusInfo_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2, 1, 1, 6),
    _WmanIfSsRssiStatusInfo_Type()
)
wmanIfSsRssiStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsRssiStatusInfo.setStatus("current")
_WmanIfSsPhy_ObjectIdentity = ObjectIdentity
wmanIfSsPhy = _WmanIfSsPhy_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5)
)
_WmanIfSsOfdmPhy_ObjectIdentity = ObjectIdentity
wmanIfSsOfdmPhy = _WmanIfSsOfdmPhy_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1)
)
_WmanIfSsOfdmUplinkChannelTable_Object = MibTable
wmanIfSsOfdmUplinkChannelTable = _WmanIfSsOfdmUplinkChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    wmanIfSsOfdmUplinkChannelTable.setStatus("current")
_WmanIfSsOfdmUplinkChannelEntry_Object = MibTableRow
wmanIfSsOfdmUplinkChannelEntry = _WmanIfSsOfdmUplinkChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 1, 1)
)
wmanIfSsOfdmUplinkChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsOfdmUplinkChannelEntry.setStatus("current")


class _WmanIfSsOfdmCtBasedResvTimeout_Type(Integer32):
    """Custom type wmanIfSsOfdmCtBasedResvTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WmanIfSsOfdmCtBasedResvTimeout_Type.__name__ = "Integer32"
_WmanIfSsOfdmCtBasedResvTimeout_Object = MibTableColumn
wmanIfSsOfdmCtBasedResvTimeout = _WmanIfSsOfdmCtBasedResvTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 1, 1, 1),
    _WmanIfSsOfdmCtBasedResvTimeout_Type()
)
wmanIfSsOfdmCtBasedResvTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmCtBasedResvTimeout.setStatus("current")


class _WmanIfSsOfdmBwReqOppSize_Type(Integer32):
    """Custom type wmanIfSsOfdmBwReqOppSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIfSsOfdmBwReqOppSize_Type.__name__ = "Integer32"
_WmanIfSsOfdmBwReqOppSize_Object = MibTableColumn
wmanIfSsOfdmBwReqOppSize = _WmanIfSsOfdmBwReqOppSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 1, 1, 2),
    _WmanIfSsOfdmBwReqOppSize_Type()
)
wmanIfSsOfdmBwReqOppSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmBwReqOppSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmBwReqOppSize.setUnits("PS")


class _WmanIfSsOfdmRangReqOppSize_Type(Integer32):
    """Custom type wmanIfSsOfdmRangReqOppSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIfSsOfdmRangReqOppSize_Type.__name__ = "Integer32"
_WmanIfSsOfdmRangReqOppSize_Object = MibTableColumn
wmanIfSsOfdmRangReqOppSize = _WmanIfSsOfdmRangReqOppSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 1, 1, 3),
    _WmanIfSsOfdmRangReqOppSize_Type()
)
wmanIfSsOfdmRangReqOppSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmRangReqOppSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmRangReqOppSize.setUnits("PS")
_WmanIfSsOfdmUplinkCenterFreq_Type = Unsigned32
_WmanIfSsOfdmUplinkCenterFreq_Object = MibTableColumn
wmanIfSsOfdmUplinkCenterFreq = _WmanIfSsOfdmUplinkCenterFreq_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 1, 1, 4),
    _WmanIfSsOfdmUplinkCenterFreq_Type()
)
wmanIfSsOfdmUplinkCenterFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmUplinkCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmUplinkCenterFreq.setUnits("kHz")


class _WmanIfSsOfdmNumSubChReqRegionFull_Type(Integer32):
    """Custom type wmanIfSsOfdmNumSubChReqRegionFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("oneSubchannel", 0),
          ("twoSubchannels", 1),
          ("fourSubchannels", 2),
          ("eightSubchannels", 3),
          ("sixteenSubchannels", 4))
    )


_WmanIfSsOfdmNumSubChReqRegionFull_Type.__name__ = "Integer32"
_WmanIfSsOfdmNumSubChReqRegionFull_Object = MibTableColumn
wmanIfSsOfdmNumSubChReqRegionFull = _WmanIfSsOfdmNumSubChReqRegionFull_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 1, 1, 5),
    _WmanIfSsOfdmNumSubChReqRegionFull_Type()
)
wmanIfSsOfdmNumSubChReqRegionFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmNumSubChReqRegionFull.setStatus("current")


class _WmanIfSsOfdmNumSymbolsReqRegionFull_Type(Integer32):
    """Custom type wmanIfSsOfdmNumSymbolsReqRegionFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_WmanIfSsOfdmNumSymbolsReqRegionFull_Type.__name__ = "Integer32"
_WmanIfSsOfdmNumSymbolsReqRegionFull_Object = MibTableColumn
wmanIfSsOfdmNumSymbolsReqRegionFull = _WmanIfSsOfdmNumSymbolsReqRegionFull_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 1, 1, 6),
    _WmanIfSsOfdmNumSymbolsReqRegionFull_Type()
)
wmanIfSsOfdmNumSymbolsReqRegionFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmNumSymbolsReqRegionFull.setStatus("current")


class _WmanIfSsOfdmSubChFocusCtCode_Type(Integer32):
    """Custom type wmanIfSsOfdmSubChFocusCtCode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_WmanIfSsOfdmSubChFocusCtCode_Type.__name__ = "Integer32"
_WmanIfSsOfdmSubChFocusCtCode_Object = MibTableColumn
wmanIfSsOfdmSubChFocusCtCode = _WmanIfSsOfdmSubChFocusCtCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 1, 1, 7),
    _WmanIfSsOfdmSubChFocusCtCode_Type()
)
wmanIfSsOfdmSubChFocusCtCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmSubChFocusCtCode.setStatus("current")


class _WmanIfSsOfdmUpLinkChannelId_Type(Integer32):
    """Custom type wmanIfSsOfdmUpLinkChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmUpLinkChannelId_Type.__name__ = "Integer32"
_WmanIfSsOfdmUpLinkChannelId_Object = MibTableColumn
wmanIfSsOfdmUpLinkChannelId = _WmanIfSsOfdmUpLinkChannelId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 1, 1, 8),
    _WmanIfSsOfdmUpLinkChannelId_Type()
)
wmanIfSsOfdmUpLinkChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmUpLinkChannelId.setStatus("current")
_WmanIfSsOfdmDownlinkChannelTable_Object = MibTable
wmanIfSsOfdmDownlinkChannelTable = _WmanIfSsOfdmDownlinkChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    wmanIfSsOfdmDownlinkChannelTable.setStatus("current")
_WmanIfSsOfdmDownlinkChannelEntry_Object = MibTableRow
wmanIfSsOfdmDownlinkChannelEntry = _WmanIfSsOfdmDownlinkChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 2, 1)
)
wmanIfSsOfdmDownlinkChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsOfdmDownlinkChannelEntry.setStatus("current")


class _WmanIfSsOfdmBsEIRP_Type(Integer32):
    """Custom type wmanIfSsOfdmBsEIRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfSsOfdmBsEIRP_Type.__name__ = "Integer32"
_WmanIfSsOfdmBsEIRP_Object = MibTableColumn
wmanIfSsOfdmBsEIRP = _WmanIfSsOfdmBsEIRP_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 2, 1, 1),
    _WmanIfSsOfdmBsEIRP_Type()
)
wmanIfSsOfdmBsEIRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmBsEIRP.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmBsEIRP.setUnits("dBm")
_WmanIfSsOfdmChannelNumber_Type = WmanIfChannelNumber
_WmanIfSsOfdmChannelNumber_Object = MibTableColumn
wmanIfSsOfdmChannelNumber = _WmanIfSsOfdmChannelNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 2, 1, 2),
    _WmanIfSsOfdmChannelNumber_Type()
)
wmanIfSsOfdmChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmChannelNumber.setStatus("current")


class _WmanIfSsOfdmTTG_Type(Integer32):
    """Custom type wmanIfSsOfdmTTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmTTG_Type.__name__ = "Integer32"
_WmanIfSsOfdmTTG_Object = MibTableColumn
wmanIfSsOfdmTTG = _WmanIfSsOfdmTTG_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 2, 1, 3),
    _WmanIfSsOfdmTTG_Type()
)
wmanIfSsOfdmTTG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmTTG.setStatus("current")


class _WmanIfSsOfdmRTG_Type(Integer32):
    """Custom type wmanIfSsOfdmRTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmRTG_Type.__name__ = "Integer32"
_WmanIfSsOfdmRTG_Object = MibTableColumn
wmanIfSsOfdmRTG = _WmanIfSsOfdmRTG_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 2, 1, 4),
    _WmanIfSsOfdmRTG_Type()
)
wmanIfSsOfdmRTG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmRTG.setStatus("current")


class _WmanIfSsOfdmInitRngMaxRSS_Type(Integer32):
    """Custom type wmanIfSsOfdmInitRngMaxRSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfSsOfdmInitRngMaxRSS_Type.__name__ = "Integer32"
_WmanIfSsOfdmInitRngMaxRSS_Object = MibTableColumn
wmanIfSsOfdmInitRngMaxRSS = _WmanIfSsOfdmInitRngMaxRSS_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 2, 1, 5),
    _WmanIfSsOfdmInitRngMaxRSS_Type()
)
wmanIfSsOfdmInitRngMaxRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmInitRngMaxRSS.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmInitRngMaxRSS.setUnits("dBm")
_WmanIfSsOfdmDownlinkCenterFreq_Type = Unsigned32
_WmanIfSsOfdmDownlinkCenterFreq_Object = MibTableColumn
wmanIfSsOfdmDownlinkCenterFreq = _WmanIfSsOfdmDownlinkCenterFreq_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 2, 1, 6),
    _WmanIfSsOfdmDownlinkCenterFreq_Type()
)
wmanIfSsOfdmDownlinkCenterFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmDownlinkCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmDownlinkCenterFreq.setUnits("kHz")
_WmanIfSsOfdmBsId_Type = WmanIfBsIdType
_WmanIfSsOfdmBsId_Object = MibTableColumn
wmanIfSsOfdmBsId = _WmanIfSsOfdmBsId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 2, 1, 7),
    _WmanIfSsOfdmBsId_Type()
)
wmanIfSsOfdmBsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmBsId.setStatus("current")
_WmanIfSsOfdmMacVersion_Type = WmanIfMacVersion
_WmanIfSsOfdmMacVersion_Object = MibTableColumn
wmanIfSsOfdmMacVersion = _WmanIfSsOfdmMacVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 2, 1, 8),
    _WmanIfSsOfdmMacVersion_Type()
)
wmanIfSsOfdmMacVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmMacVersion.setStatus("current")


class _WmanIfSsOfdmFrameDurationCode_Type(Integer32):
    """Custom type wmanIfSsOfdmFrameDurationCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("duration2dot5ms", 0),
          ("duration4ms", 1),
          ("duration5ms", 2),
          ("duration8ms", 3),
          ("duration10ms", 4),
          ("duration12dot5ms", 5),
          ("duration20ms", 6))
    )


_WmanIfSsOfdmFrameDurationCode_Type.__name__ = "Integer32"
_WmanIfSsOfdmFrameDurationCode_Object = MibTableColumn
wmanIfSsOfdmFrameDurationCode = _WmanIfSsOfdmFrameDurationCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 2, 1, 9),
    _WmanIfSsOfdmFrameDurationCode_Type()
)
wmanIfSsOfdmFrameDurationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmFrameDurationCode.setStatus("current")


class _WmanIfSsOfdmDownLinkChannelId_Type(Integer32):
    """Custom type wmanIfSsOfdmDownLinkChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmDownLinkChannelId_Type.__name__ = "Integer32"
_WmanIfSsOfdmDownLinkChannelId_Object = MibTableColumn
wmanIfSsOfdmDownLinkChannelId = _WmanIfSsOfdmDownLinkChannelId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 2, 1, 10),
    _WmanIfSsOfdmDownLinkChannelId_Type()
)
wmanIfSsOfdmDownLinkChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmDownLinkChannelId.setStatus("current")
_WmanIfSsOfdmUcdBurstProfileTable_Object = MibTable
wmanIfSsOfdmUcdBurstProfileTable = _WmanIfSsOfdmUcdBurstProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 3)
)
if mibBuilder.loadTexts:
    wmanIfSsOfdmUcdBurstProfileTable.setStatus("current")
_WmanIfSsOfdmUcdBurstProfileEntry_Object = MibTableRow
wmanIfSsOfdmUcdBurstProfileEntry = _WmanIfSsOfdmUcdBurstProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 3, 1)
)
wmanIfSsOfdmUcdBurstProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfSsOfdmUiucIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsOfdmUcdBurstProfileEntry.setStatus("current")


class _WmanIfSsOfdmUiucIndex_Type(Integer32):
    """Custom type wmanIfSsOfdmUiucIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_WmanIfSsOfdmUiucIndex_Type.__name__ = "Integer32"
_WmanIfSsOfdmUiucIndex_Object = MibTableColumn
wmanIfSsOfdmUiucIndex = _WmanIfSsOfdmUiucIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 3, 1, 1),
    _WmanIfSsOfdmUiucIndex_Type()
)
wmanIfSsOfdmUiucIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfSsOfdmUiucIndex.setStatus("current")
_WmanIfSsOfdmUcdFecCodeType_Type = WmanIfOfdmFecCodeType
_WmanIfSsOfdmUcdFecCodeType_Object = MibTableColumn
wmanIfSsOfdmUcdFecCodeType = _WmanIfSsOfdmUcdFecCodeType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 3, 1, 2),
    _WmanIfSsOfdmUcdFecCodeType_Type()
)
wmanIfSsOfdmUcdFecCodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmUcdFecCodeType.setStatus("current")


class _WmanIfSsOfdmFocusCtPowerBoost_Type(Integer32):
    """Custom type wmanIfSsOfdmFocusCtPowerBoost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmFocusCtPowerBoost_Type.__name__ = "Integer32"
_WmanIfSsOfdmFocusCtPowerBoost_Object = MibTableColumn
wmanIfSsOfdmFocusCtPowerBoost = _WmanIfSsOfdmFocusCtPowerBoost_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 3, 1, 3),
    _WmanIfSsOfdmFocusCtPowerBoost_Type()
)
wmanIfSsOfdmFocusCtPowerBoost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmFocusCtPowerBoost.setStatus("current")


class _WmanIfSsOfdmUcdTcsEnable_Type(Integer32):
    """Custom type wmanIfSsOfdmUcdTcsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tcsDisabled", 0),
          ("tcsEnabled", 1))
    )


_WmanIfSsOfdmUcdTcsEnable_Type.__name__ = "Integer32"
_WmanIfSsOfdmUcdTcsEnable_Object = MibTableColumn
wmanIfSsOfdmUcdTcsEnable = _WmanIfSsOfdmUcdTcsEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 3, 1, 4),
    _WmanIfSsOfdmUcdTcsEnable_Type()
)
wmanIfSsOfdmUcdTcsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmUcdTcsEnable.setStatus("current")
_WmanIfSsOfdmDcdBurstProfileTable_Object = MibTable
wmanIfSsOfdmDcdBurstProfileTable = _WmanIfSsOfdmDcdBurstProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 4)
)
if mibBuilder.loadTexts:
    wmanIfSsOfdmDcdBurstProfileTable.setStatus("current")
_WmanIfSsOfdmDcdBurstProfileEntry_Object = MibTableRow
wmanIfSsOfdmDcdBurstProfileEntry = _WmanIfSsOfdmDcdBurstProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 4, 1)
)
wmanIfSsOfdmDcdBurstProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfSsOfdmDiucIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsOfdmDcdBurstProfileEntry.setStatus("current")


class _WmanIfSsOfdmDiucIndex_Type(Integer32):
    """Custom type wmanIfSsOfdmDiucIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_WmanIfSsOfdmDiucIndex_Type.__name__ = "Integer32"
_WmanIfSsOfdmDiucIndex_Object = MibTableColumn
wmanIfSsOfdmDiucIndex = _WmanIfSsOfdmDiucIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 4, 1, 1),
    _WmanIfSsOfdmDiucIndex_Type()
)
wmanIfSsOfdmDiucIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfSsOfdmDiucIndex.setStatus("current")
_WmanIfSsOfdmDownlinkFrequency_Type = Unsigned32
_WmanIfSsOfdmDownlinkFrequency_Object = MibTableColumn
wmanIfSsOfdmDownlinkFrequency = _WmanIfSsOfdmDownlinkFrequency_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 4, 1, 2),
    _WmanIfSsOfdmDownlinkFrequency_Type()
)
wmanIfSsOfdmDownlinkFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmDownlinkFrequency.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmDownlinkFrequency.setUnits("kHz")
_WmanIfSsOfdmDcdFecCodeType_Type = WmanIfOfdmFecCodeType
_WmanIfSsOfdmDcdFecCodeType_Object = MibTableColumn
wmanIfSsOfdmDcdFecCodeType = _WmanIfSsOfdmDcdFecCodeType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 4, 1, 3),
    _WmanIfSsOfdmDcdFecCodeType_Type()
)
wmanIfSsOfdmDcdFecCodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmDcdFecCodeType.setStatus("current")


class _WmanIfSsOfdmDiucMandatoryExitThresh_Type(Integer32):
    """Custom type wmanIfSsOfdmDiucMandatoryExitThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmDiucMandatoryExitThresh_Type.__name__ = "Integer32"
_WmanIfSsOfdmDiucMandatoryExitThresh_Object = MibTableColumn
wmanIfSsOfdmDiucMandatoryExitThresh = _WmanIfSsOfdmDiucMandatoryExitThresh_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 4, 1, 4),
    _WmanIfSsOfdmDiucMandatoryExitThresh_Type()
)
wmanIfSsOfdmDiucMandatoryExitThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmDiucMandatoryExitThresh.setStatus("current")


class _WmanIfSsOfdmDiucMinEntryThresh_Type(Integer32):
    """Custom type wmanIfSsOfdmDiucMinEntryThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmDiucMinEntryThresh_Type.__name__ = "Integer32"
_WmanIfSsOfdmDiucMinEntryThresh_Object = MibTableColumn
wmanIfSsOfdmDiucMinEntryThresh = _WmanIfSsOfdmDiucMinEntryThresh_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 4, 1, 5),
    _WmanIfSsOfdmDiucMinEntryThresh_Type()
)
wmanIfSsOfdmDiucMinEntryThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmDiucMinEntryThresh.setStatus("current")


class _WmanIfSsOfdmTcsEnable_Type(Integer32):
    """Custom type wmanIfSsOfdmTcsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tcsDisabled", 0),
          ("tcsEnabled", 1))
    )


_WmanIfSsOfdmTcsEnable_Type.__name__ = "Integer32"
_WmanIfSsOfdmTcsEnable_Object = MibTableColumn
wmanIfSsOfdmTcsEnable = _WmanIfSsOfdmTcsEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 1, 4, 1, 6),
    _WmanIfSsOfdmTcsEnable_Type()
)
wmanIfSsOfdmTcsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmTcsEnable.setStatus("current")
_WmanIfSsOfdmaPhy_ObjectIdentity = ObjectIdentity
wmanIfSsOfdmaPhy = _WmanIfSsOfdmaPhy_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2)
)
_WmanIfSsOfdmaUplinkChannelTable_Object = MibTable
wmanIfSsOfdmaUplinkChannelTable = _WmanIfSsOfdmaUplinkChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIfSsOfdmaUplinkChannelTable.setStatus("current")
_WmanIfSsOfdmaUplinkChannelEntry_Object = MibTableRow
wmanIfSsOfdmaUplinkChannelEntry = _WmanIfSsOfdmaUplinkChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1)
)
wmanIfSsOfdmaUplinkChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsOfdmaUplinkChannelEntry.setStatus("current")


class _WmanIfSsOfdmaCtBasedResvTimeout_Type(Integer32):
    """Custom type wmanIfSsOfdmaCtBasedResvTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WmanIfSsOfdmaCtBasedResvTimeout_Type.__name__ = "Integer32"
_WmanIfSsOfdmaCtBasedResvTimeout_Object = MibTableColumn
wmanIfSsOfdmaCtBasedResvTimeout = _WmanIfSsOfdmaCtBasedResvTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 1),
    _WmanIfSsOfdmaCtBasedResvTimeout_Type()
)
wmanIfSsOfdmaCtBasedResvTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaCtBasedResvTimeout.setStatus("current")


class _WmanIfSsOfdmaBwReqOppSize_Type(Integer32):
    """Custom type wmanIfSsOfdmaBwReqOppSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIfSsOfdmaBwReqOppSize_Type.__name__ = "Integer32"
_WmanIfSsOfdmaBwReqOppSize_Object = MibTableColumn
wmanIfSsOfdmaBwReqOppSize = _WmanIfSsOfdmaBwReqOppSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 2),
    _WmanIfSsOfdmaBwReqOppSize_Type()
)
wmanIfSsOfdmaBwReqOppSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBwReqOppSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBwReqOppSize.setUnits("PS")


class _WmanIfSsOfdmaRangReqOppSize_Type(Integer32):
    """Custom type wmanIfSsOfdmaRangReqOppSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIfSsOfdmaRangReqOppSize_Type.__name__ = "Integer32"
_WmanIfSsOfdmaRangReqOppSize_Object = MibTableColumn
wmanIfSsOfdmaRangReqOppSize = _WmanIfSsOfdmaRangReqOppSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 3),
    _WmanIfSsOfdmaRangReqOppSize_Type()
)
wmanIfSsOfdmaRangReqOppSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaRangReqOppSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaRangReqOppSize.setUnits("PS")
_WmanIfSsOfdmaUplinkCenterFreq_Type = Unsigned32
_WmanIfSsOfdmaUplinkCenterFreq_Object = MibTableColumn
wmanIfSsOfdmaUplinkCenterFreq = _WmanIfSsOfdmaUplinkCenterFreq_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 4),
    _WmanIfSsOfdmaUplinkCenterFreq_Type()
)
wmanIfSsOfdmaUplinkCenterFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaUplinkCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaUplinkCenterFreq.setUnits("kHz")


class _WmanIfSsOfdmaInitRngCodes_Type(Integer32):
    """Custom type wmanIfSsOfdmaInitRngCodes based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaInitRngCodes_Type.__name__ = "Integer32"
_WmanIfSsOfdmaInitRngCodes_Object = MibTableColumn
wmanIfSsOfdmaInitRngCodes = _WmanIfSsOfdmaInitRngCodes_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 5),
    _WmanIfSsOfdmaInitRngCodes_Type()
)
wmanIfSsOfdmaInitRngCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaInitRngCodes.setStatus("current")


class _WmanIfSsOfdmaPeriodicRngCodes_Type(Integer32):
    """Custom type wmanIfSsOfdmaPeriodicRngCodes based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaPeriodicRngCodes_Type.__name__ = "Integer32"
_WmanIfSsOfdmaPeriodicRngCodes_Object = MibTableColumn
wmanIfSsOfdmaPeriodicRngCodes = _WmanIfSsOfdmaPeriodicRngCodes_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 6),
    _WmanIfSsOfdmaPeriodicRngCodes_Type()
)
wmanIfSsOfdmaPeriodicRngCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaPeriodicRngCodes.setStatus("current")


class _WmanIfSsOfdmaBWReqCodes_Type(Integer32):
    """Custom type wmanIfSsOfdmaBWReqCodes based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaBWReqCodes_Type.__name__ = "Integer32"
_WmanIfSsOfdmaBWReqCodes_Object = MibTableColumn
wmanIfSsOfdmaBWReqCodes = _WmanIfSsOfdmaBWReqCodes_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 7),
    _WmanIfSsOfdmaBWReqCodes_Type()
)
wmanIfSsOfdmaBWReqCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBWReqCodes.setStatus("current")


class _WmanIfSsOfdmaPerRngBackoffStart_Type(Integer32):
    """Custom type wmanIfSsOfdmaPerRngBackoffStart based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIfSsOfdmaPerRngBackoffStart_Type.__name__ = "Integer32"
_WmanIfSsOfdmaPerRngBackoffStart_Object = MibTableColumn
wmanIfSsOfdmaPerRngBackoffStart = _WmanIfSsOfdmaPerRngBackoffStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 8),
    _WmanIfSsOfdmaPerRngBackoffStart_Type()
)
wmanIfSsOfdmaPerRngBackoffStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaPerRngBackoffStart.setStatus("current")


class _WmanIfSsOfdmaPerRngBackoffEnd_Type(Integer32):
    """Custom type wmanIfSsOfdmaPerRngBackoffEnd based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIfSsOfdmaPerRngBackoffEnd_Type.__name__ = "Integer32"
_WmanIfSsOfdmaPerRngBackoffEnd_Object = MibTableColumn
wmanIfSsOfdmaPerRngBackoffEnd = _WmanIfSsOfdmaPerRngBackoffEnd_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 9),
    _WmanIfSsOfdmaPerRngBackoffEnd_Type()
)
wmanIfSsOfdmaPerRngBackoffEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaPerRngBackoffEnd.setStatus("current")


class _WmanIfSsOfdmaStartOfRngCodes_Type(Integer32):
    """Custom type wmanIfSsOfdmaStartOfRngCodes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaStartOfRngCodes_Type.__name__ = "Integer32"
_WmanIfSsOfdmaStartOfRngCodes_Object = MibTableColumn
wmanIfSsOfdmaStartOfRngCodes = _WmanIfSsOfdmaStartOfRngCodes_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 10),
    _WmanIfSsOfdmaStartOfRngCodes_Type()
)
wmanIfSsOfdmaStartOfRngCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaStartOfRngCodes.setStatus("current")


class _WmanIfSsOfdmaPermutationBase_Type(Integer32):
    """Custom type wmanIfSsOfdmaPermutationBase based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaPermutationBase_Type.__name__ = "Integer32"
_WmanIfSsOfdmaPermutationBase_Object = MibTableColumn
wmanIfSsOfdmaPermutationBase = _WmanIfSsOfdmaPermutationBase_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 11),
    _WmanIfSsOfdmaPermutationBase_Type()
)
wmanIfSsOfdmaPermutationBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaPermutationBase.setStatus("current")


class _WmanIfSsOfdmaULAllocSubchBitmap_Type(OctetString):
    """Custom type wmanIfSsOfdmaULAllocSubchBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )
    fixedLength = 9


_WmanIfSsOfdmaULAllocSubchBitmap_Type.__name__ = "OctetString"
_WmanIfSsOfdmaULAllocSubchBitmap_Object = MibTableColumn
wmanIfSsOfdmaULAllocSubchBitmap = _WmanIfSsOfdmaULAllocSubchBitmap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 12),
    _WmanIfSsOfdmaULAllocSubchBitmap_Type()
)
wmanIfSsOfdmaULAllocSubchBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaULAllocSubchBitmap.setStatus("current")


class _WmanIfSsOfdmaOptPermULAllocSubchBitmap_Type(OctetString):
    """Custom type wmanIfSsOfdmaOptPermULAllocSubchBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )
    fixedLength = 13


_WmanIfSsOfdmaOptPermULAllocSubchBitmap_Type.__name__ = "OctetString"
_WmanIfSsOfdmaOptPermULAllocSubchBitmap_Object = MibTableColumn
wmanIfSsOfdmaOptPermULAllocSubchBitmap = _WmanIfSsOfdmaOptPermULAllocSubchBitmap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 13),
    _WmanIfSsOfdmaOptPermULAllocSubchBitmap_Type()
)
wmanIfSsOfdmaOptPermULAllocSubchBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaOptPermULAllocSubchBitmap.setStatus("current")


class _WmanIfSsOfdmaBandAMCAllocThreshold_Type(Integer32):
    """Custom type wmanIfSsOfdmaBandAMCAllocThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaBandAMCAllocThreshold_Type.__name__ = "Integer32"
_WmanIfSsOfdmaBandAMCAllocThreshold_Object = MibTableColumn
wmanIfSsOfdmaBandAMCAllocThreshold = _WmanIfSsOfdmaBandAMCAllocThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 14),
    _WmanIfSsOfdmaBandAMCAllocThreshold_Type()
)
wmanIfSsOfdmaBandAMCAllocThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBandAMCAllocThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBandAMCAllocThreshold.setUnits("dB")


class _WmanIfSsOfdmaBandAMCReleaseThreshold_Type(Integer32):
    """Custom type wmanIfSsOfdmaBandAMCReleaseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaBandAMCReleaseThreshold_Type.__name__ = "Integer32"
_WmanIfSsOfdmaBandAMCReleaseThreshold_Object = MibTableColumn
wmanIfSsOfdmaBandAMCReleaseThreshold = _WmanIfSsOfdmaBandAMCReleaseThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 15),
    _WmanIfSsOfdmaBandAMCReleaseThreshold_Type()
)
wmanIfSsOfdmaBandAMCReleaseThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBandAMCReleaseThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBandAMCReleaseThreshold.setUnits("dB")


class _WmanIfSsOfdmaBandAMCAllocTimer_Type(Integer32):
    """Custom type wmanIfSsOfdmaBandAMCAllocTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaBandAMCAllocTimer_Type.__name__ = "Integer32"
_WmanIfSsOfdmaBandAMCAllocTimer_Object = MibTableColumn
wmanIfSsOfdmaBandAMCAllocTimer = _WmanIfSsOfdmaBandAMCAllocTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 16),
    _WmanIfSsOfdmaBandAMCAllocTimer_Type()
)
wmanIfSsOfdmaBandAMCAllocTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBandAMCAllocTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBandAMCAllocTimer.setUnits("Frame")


class _WmanIfSsOfdmaBandAMCReleaseTimer_Type(Integer32):
    """Custom type wmanIfSsOfdmaBandAMCReleaseTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaBandAMCReleaseTimer_Type.__name__ = "Integer32"
_WmanIfSsOfdmaBandAMCReleaseTimer_Object = MibTableColumn
wmanIfSsOfdmaBandAMCReleaseTimer = _WmanIfSsOfdmaBandAMCReleaseTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 17),
    _WmanIfSsOfdmaBandAMCReleaseTimer_Type()
)
wmanIfSsOfdmaBandAMCReleaseTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBandAMCReleaseTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBandAMCReleaseTimer.setUnits("Frame")


class _WmanIfSsOfdmaBandStatRepMAXPeriod_Type(Integer32):
    """Custom type wmanIfSsOfdmaBandStatRepMAXPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaBandStatRepMAXPeriod_Type.__name__ = "Integer32"
_WmanIfSsOfdmaBandStatRepMAXPeriod_Object = MibTableColumn
wmanIfSsOfdmaBandStatRepMAXPeriod = _WmanIfSsOfdmaBandStatRepMAXPeriod_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 18),
    _WmanIfSsOfdmaBandStatRepMAXPeriod_Type()
)
wmanIfSsOfdmaBandStatRepMAXPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBandStatRepMAXPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBandStatRepMAXPeriod.setUnits("Frame")


class _WmanIfSsOfdmaBandAMCRetryTimer_Type(Integer32):
    """Custom type wmanIfSsOfdmaBandAMCRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaBandAMCRetryTimer_Type.__name__ = "Integer32"
_WmanIfSsOfdmaBandAMCRetryTimer_Object = MibTableColumn
wmanIfSsOfdmaBandAMCRetryTimer = _WmanIfSsOfdmaBandAMCRetryTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 19),
    _WmanIfSsOfdmaBandAMCRetryTimer_Type()
)
wmanIfSsOfdmaBandAMCRetryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBandAMCRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBandAMCRetryTimer.setUnits("Frame")


class _WmanIfSsOfdmaSafetyChAllocThreshold_Type(Integer32):
    """Custom type wmanIfSsOfdmaSafetyChAllocThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaSafetyChAllocThreshold_Type.__name__ = "Integer32"
_WmanIfSsOfdmaSafetyChAllocThreshold_Object = MibTableColumn
wmanIfSsOfdmaSafetyChAllocThreshold = _WmanIfSsOfdmaSafetyChAllocThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 20),
    _WmanIfSsOfdmaSafetyChAllocThreshold_Type()
)
wmanIfSsOfdmaSafetyChAllocThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaSafetyChAllocThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaSafetyChAllocThreshold.setUnits("dB")


class _WmanIfSsOfdmaSafetyChReleaseThreshold_Type(Integer32):
    """Custom type wmanIfSsOfdmaSafetyChReleaseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaSafetyChReleaseThreshold_Type.__name__ = "Integer32"
_WmanIfSsOfdmaSafetyChReleaseThreshold_Object = MibTableColumn
wmanIfSsOfdmaSafetyChReleaseThreshold = _WmanIfSsOfdmaSafetyChReleaseThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 21),
    _WmanIfSsOfdmaSafetyChReleaseThreshold_Type()
)
wmanIfSsOfdmaSafetyChReleaseThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaSafetyChReleaseThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaSafetyChReleaseThreshold.setUnits("dB")


class _WmanIfSsOfdmaSafetyChAllocTimer_Type(Integer32):
    """Custom type wmanIfSsOfdmaSafetyChAllocTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaSafetyChAllocTimer_Type.__name__ = "Integer32"
_WmanIfSsOfdmaSafetyChAllocTimer_Object = MibTableColumn
wmanIfSsOfdmaSafetyChAllocTimer = _WmanIfSsOfdmaSafetyChAllocTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 22),
    _WmanIfSsOfdmaSafetyChAllocTimer_Type()
)
wmanIfSsOfdmaSafetyChAllocTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaSafetyChAllocTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaSafetyChAllocTimer.setUnits("Frame")


class _WmanIfSsOfdmaSafetyChReleaseTimer_Type(Integer32):
    """Custom type wmanIfSsOfdmaSafetyChReleaseTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaSafetyChReleaseTimer_Type.__name__ = "Integer32"
_WmanIfSsOfdmaSafetyChReleaseTimer_Object = MibTableColumn
wmanIfSsOfdmaSafetyChReleaseTimer = _WmanIfSsOfdmaSafetyChReleaseTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 23),
    _WmanIfSsOfdmaSafetyChReleaseTimer_Type()
)
wmanIfSsOfdmaSafetyChReleaseTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaSafetyChReleaseTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaSafetyChReleaseTimer.setUnits("Frame")


class _WmanIfSsOfdmaBinStatRepMAXPeriod_Type(Integer32):
    """Custom type wmanIfSsOfdmaBinStatRepMAXPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaBinStatRepMAXPeriod_Type.__name__ = "Integer32"
_WmanIfSsOfdmaBinStatRepMAXPeriod_Object = MibTableColumn
wmanIfSsOfdmaBinStatRepMAXPeriod = _WmanIfSsOfdmaBinStatRepMAXPeriod_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 24),
    _WmanIfSsOfdmaBinStatRepMAXPeriod_Type()
)
wmanIfSsOfdmaBinStatRepMAXPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBinStatRepMAXPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBinStatRepMAXPeriod.setUnits("Frame")


class _WmanIfSsOfdmaSafetyChaRetryTimer_Type(Integer32):
    """Custom type wmanIfSsOfdmaSafetyChaRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaSafetyChaRetryTimer_Type.__name__ = "Integer32"
_WmanIfSsOfdmaSafetyChaRetryTimer_Object = MibTableColumn
wmanIfSsOfdmaSafetyChaRetryTimer = _WmanIfSsOfdmaSafetyChaRetryTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 25),
    _WmanIfSsOfdmaSafetyChaRetryTimer_Type()
)
wmanIfSsOfdmaSafetyChaRetryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaSafetyChaRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaSafetyChaRetryTimer.setUnits("Frame")


class _WmanIfSsOfdmaHARQAackDelayULBurst_Type(Integer32):
    """Custom type wmanIfSsOfdmaHARQAackDelayULBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneframeoffset", 1),
          ("twoframesoffset", 2),
          ("threeframesoffset", 3))
    )


_WmanIfSsOfdmaHARQAackDelayULBurst_Type.__name__ = "Integer32"
_WmanIfSsOfdmaHARQAackDelayULBurst_Object = MibTableColumn
wmanIfSsOfdmaHARQAackDelayULBurst = _WmanIfSsOfdmaHARQAackDelayULBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 26),
    _WmanIfSsOfdmaHARQAackDelayULBurst_Type()
)
wmanIfSsOfdmaHARQAackDelayULBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaHARQAackDelayULBurst.setStatus("current")


class _WmanIfSsOfdmaCQICHBandAMCTranaDelay_Type(Integer32):
    """Custom type wmanIfSsOfdmaCQICHBandAMCTranaDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaCQICHBandAMCTranaDelay_Type.__name__ = "Integer32"
_WmanIfSsOfdmaCQICHBandAMCTranaDelay_Object = MibTableColumn
wmanIfSsOfdmaCQICHBandAMCTranaDelay = _WmanIfSsOfdmaCQICHBandAMCTranaDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 1, 1, 27),
    _WmanIfSsOfdmaCQICHBandAMCTranaDelay_Type()
)
wmanIfSsOfdmaCQICHBandAMCTranaDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaCQICHBandAMCTranaDelay.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaCQICHBandAMCTranaDelay.setUnits("Frame")
_WmanIfSsOfdmaDownlinkChannelTable_Object = MibTable
wmanIfSsOfdmaDownlinkChannelTable = _WmanIfSsOfdmaDownlinkChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 2)
)
if mibBuilder.loadTexts:
    wmanIfSsOfdmaDownlinkChannelTable.setStatus("current")
_WmanIfSsOfdmaDownlinkChannelEntry_Object = MibTableRow
wmanIfSsOfdmaDownlinkChannelEntry = _WmanIfSsOfdmaDownlinkChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 2, 1)
)
wmanIfSsOfdmaDownlinkChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsOfdmaDownlinkChannelEntry.setStatus("current")


class _WmanIfSsOfdmaBsEIRP_Type(Integer32):
    """Custom type wmanIfSsOfdmaBsEIRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfSsOfdmaBsEIRP_Type.__name__ = "Integer32"
_WmanIfSsOfdmaBsEIRP_Object = MibTableColumn
wmanIfSsOfdmaBsEIRP = _WmanIfSsOfdmaBsEIRP_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 2, 1, 1),
    _WmanIfSsOfdmaBsEIRP_Type()
)
wmanIfSsOfdmaBsEIRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBsEIRP.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBsEIRP.setUnits("dBm")
_WmanIfSsOfdmaChannelNumber_Type = WmanIfChannelNumber
_WmanIfSsOfdmaChannelNumber_Object = MibTableColumn
wmanIfSsOfdmaChannelNumber = _WmanIfSsOfdmaChannelNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 2, 1, 2),
    _WmanIfSsOfdmaChannelNumber_Type()
)
wmanIfSsOfdmaChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaChannelNumber.setStatus("current")


class _WmanIfSsOfdmaTTG_Type(Integer32):
    """Custom type wmanIfSsOfdmaTTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaTTG_Type.__name__ = "Integer32"
_WmanIfSsOfdmaTTG_Object = MibTableColumn
wmanIfSsOfdmaTTG = _WmanIfSsOfdmaTTG_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 2, 1, 3),
    _WmanIfSsOfdmaTTG_Type()
)
wmanIfSsOfdmaTTG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaTTG.setStatus("current")


class _WmanIfSsOfdmaRTG_Type(Integer32):
    """Custom type wmanIfSsOfdmaRTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaRTG_Type.__name__ = "Integer32"
_WmanIfSsOfdmaRTG_Object = MibTableColumn
wmanIfSsOfdmaRTG = _WmanIfSsOfdmaRTG_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 2, 1, 4),
    _WmanIfSsOfdmaRTG_Type()
)
wmanIfSsOfdmaRTG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaRTG.setStatus("current")


class _WmanIfSsOfdmaInitRngMaxRSS_Type(Integer32):
    """Custom type wmanIfSsOfdmaInitRngMaxRSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfSsOfdmaInitRngMaxRSS_Type.__name__ = "Integer32"
_WmanIfSsOfdmaInitRngMaxRSS_Object = MibTableColumn
wmanIfSsOfdmaInitRngMaxRSS = _WmanIfSsOfdmaInitRngMaxRSS_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 2, 1, 5),
    _WmanIfSsOfdmaInitRngMaxRSS_Type()
)
wmanIfSsOfdmaInitRngMaxRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaInitRngMaxRSS.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaInitRngMaxRSS.setUnits("dBm")
_WmanIfSsOfdmaDownlinkCenterFreq_Type = Unsigned32
_WmanIfSsOfdmaDownlinkCenterFreq_Object = MibTableColumn
wmanIfSsOfdmaDownlinkCenterFreq = _WmanIfSsOfdmaDownlinkCenterFreq_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 2, 1, 6),
    _WmanIfSsOfdmaDownlinkCenterFreq_Type()
)
wmanIfSsOfdmaDownlinkCenterFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaDownlinkCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaDownlinkCenterFreq.setUnits("kHz")
_WmanIfSsOfdmaBsId_Type = WmanIfBsIdType
_WmanIfSsOfdmaBsId_Object = MibTableColumn
wmanIfSsOfdmaBsId = _WmanIfSsOfdmaBsId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 2, 1, 7),
    _WmanIfSsOfdmaBsId_Type()
)
wmanIfSsOfdmaBsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaBsId.setStatus("current")
_WmanIfSsOfdmaMacVersion_Type = WmanIfMacVersion
_WmanIfSsOfdmaMacVersion_Object = MibTableColumn
wmanIfSsOfdmaMacVersion = _WmanIfSsOfdmaMacVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 2, 1, 8),
    _WmanIfSsOfdmaMacVersion_Type()
)
wmanIfSsOfdmaMacVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaMacVersion.setStatus("current")


class _WmanIfSsOfdmaFrameDurationCode_Type(Integer32):
    """Custom type wmanIfSsOfdmaFrameDurationCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("aASGap", 0),
          ("duration2ms", 1),
          ("duration2dot5ms", 2),
          ("duration4ms", 3),
          ("duration5ms", 4),
          ("duration8ms", 5),
          ("duration10ms", 6),
          ("duration12dot5ms", 7),
          ("duration20ms", 8))
    )


_WmanIfSsOfdmaFrameDurationCode_Type.__name__ = "Integer32"
_WmanIfSsOfdmaFrameDurationCode_Object = MibTableColumn
wmanIfSsOfdmaFrameDurationCode = _WmanIfSsOfdmaFrameDurationCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 2, 1, 9),
    _WmanIfSsOfdmaFrameDurationCode_Type()
)
wmanIfSsOfdmaFrameDurationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaFrameDurationCode.setStatus("current")


class _WmanIfSsOfdmaSizeCqichIdField_Type(Integer32):
    """Custom type wmanIfSsOfdmaSizeCqichIdField based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("threebits", 1),
          ("fourbits", 2),
          ("fivebits", 3),
          ("sixbits", 4),
          ("sevenbits", 5),
          ("eightbits", 6),
          ("ninebits", 7))
    )


_WmanIfSsOfdmaSizeCqichIdField_Type.__name__ = "Integer32"
_WmanIfSsOfdmaSizeCqichIdField_Object = MibTableColumn
wmanIfSsOfdmaSizeCqichIdField = _WmanIfSsOfdmaSizeCqichIdField_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 2, 1, 10),
    _WmanIfSsOfdmaSizeCqichIdField_Type()
)
wmanIfSsOfdmaSizeCqichIdField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaSizeCqichIdField.setStatus("current")


class _WmanIfSsOfdmaHARQAackDelayBurst_Type(Integer32):
    """Custom type wmanIfSsOfdmaHARQAackDelayBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneframeoffset", 1),
          ("twoframesoffset", 2),
          ("threeframesoffset", 3))
    )


_WmanIfSsOfdmaHARQAackDelayBurst_Type.__name__ = "Integer32"
_WmanIfSsOfdmaHARQAackDelayBurst_Object = MibTableColumn
wmanIfSsOfdmaHARQAackDelayBurst = _WmanIfSsOfdmaHARQAackDelayBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 2, 1, 11),
    _WmanIfSsOfdmaHARQAackDelayBurst_Type()
)
wmanIfSsOfdmaHARQAackDelayBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaHARQAackDelayBurst.setStatus("current")
_WmanIfSsOfdmaUcdBurstProfileTable_Object = MibTable
wmanIfSsOfdmaUcdBurstProfileTable = _WmanIfSsOfdmaUcdBurstProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 3)
)
if mibBuilder.loadTexts:
    wmanIfSsOfdmaUcdBurstProfileTable.setStatus("current")
_WmanIfSsOfdmaUcdBurstProfileEntry_Object = MibTableRow
wmanIfSsOfdmaUcdBurstProfileEntry = _WmanIfSsOfdmaUcdBurstProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 3, 1)
)
wmanIfSsOfdmaUcdBurstProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfSsOfdmaUiucIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsOfdmaUcdBurstProfileEntry.setStatus("current")


class _WmanIfSsOfdmaUiucIndex_Type(Integer32):
    """Custom type wmanIfSsOfdmaUiucIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WmanIfSsOfdmaUiucIndex_Type.__name__ = "Integer32"
_WmanIfSsOfdmaUiucIndex_Object = MibTableColumn
wmanIfSsOfdmaUiucIndex = _WmanIfSsOfdmaUiucIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 3, 1, 1),
    _WmanIfSsOfdmaUiucIndex_Type()
)
wmanIfSsOfdmaUiucIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaUiucIndex.setStatus("current")
_WmanIfSsOfdmaUcdFecCodeType_Type = WmanIfOfdmaFecCodeType
_WmanIfSsOfdmaUcdFecCodeType_Object = MibTableColumn
wmanIfSsOfdmaUcdFecCodeType = _WmanIfSsOfdmaUcdFecCodeType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 3, 1, 2),
    _WmanIfSsOfdmaUcdFecCodeType_Type()
)
wmanIfSsOfdmaUcdFecCodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaUcdFecCodeType.setStatus("current")


class _WmanIfSsOfdmaRangingDataRatio_Type(Integer32):
    """Custom type wmanIfSsOfdmaRangingDataRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaRangingDataRatio_Type.__name__ = "Integer32"
_WmanIfSsOfdmaRangingDataRatio_Object = MibTableColumn
wmanIfSsOfdmaRangingDataRatio = _WmanIfSsOfdmaRangingDataRatio_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 3, 1, 3),
    _WmanIfSsOfdmaRangingDataRatio_Type()
)
wmanIfSsOfdmaRangingDataRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaRangingDataRatio.setStatus("current")


class _WmanIfSsOfdmaNorCOverNOverride_Type(OctetString):
    """Custom type wmanIfSsOfdmaNorCOverNOverride based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixedLength = 5


_WmanIfSsOfdmaNorCOverNOverride_Type.__name__ = "OctetString"
_WmanIfSsOfdmaNorCOverNOverride_Object = MibTableColumn
wmanIfSsOfdmaNorCOverNOverride = _WmanIfSsOfdmaNorCOverNOverride_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 3, 1, 4),
    _WmanIfSsOfdmaNorCOverNOverride_Type()
)
wmanIfSsOfdmaNorCOverNOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaNorCOverNOverride.setStatus("current")
_WmanIfSsOfdmaDcdBurstProfileTable_Object = MibTable
wmanIfSsOfdmaDcdBurstProfileTable = _WmanIfSsOfdmaDcdBurstProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 4)
)
if mibBuilder.loadTexts:
    wmanIfSsOfdmaDcdBurstProfileTable.setStatus("current")
_WmanIfSsOfdmaDcdBurstProfileEntry_Object = MibTableRow
wmanIfSsOfdmaDcdBurstProfileEntry = _WmanIfSsOfdmaDcdBurstProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 4, 1)
)
wmanIfSsOfdmaDcdBurstProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfSsOfdmaDiucIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsOfdmaDcdBurstProfileEntry.setStatus("current")


class _WmanIfSsOfdmaDiucIndex_Type(Integer32):
    """Custom type wmanIfSsOfdmaDiucIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_WmanIfSsOfdmaDiucIndex_Type.__name__ = "Integer32"
_WmanIfSsOfdmaDiucIndex_Object = MibTableColumn
wmanIfSsOfdmaDiucIndex = _WmanIfSsOfdmaDiucIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 4, 1, 1),
    _WmanIfSsOfdmaDiucIndex_Type()
)
wmanIfSsOfdmaDiucIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaDiucIndex.setStatus("current")
_WmanIfSsOfdmaDownlinkFrequency_Type = Unsigned32
_WmanIfSsOfdmaDownlinkFrequency_Object = MibTableColumn
wmanIfSsOfdmaDownlinkFrequency = _WmanIfSsOfdmaDownlinkFrequency_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 4, 1, 2),
    _WmanIfSsOfdmaDownlinkFrequency_Type()
)
wmanIfSsOfdmaDownlinkFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaDownlinkFrequency.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaDownlinkFrequency.setUnits("kHz")
_WmanIfSsOfdmaDcdFecCodeType_Type = WmanIfOfdmaFecCodeType
_WmanIfSsOfdmaDcdFecCodeType_Object = MibTableColumn
wmanIfSsOfdmaDcdFecCodeType = _WmanIfSsOfdmaDcdFecCodeType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 4, 1, 3),
    _WmanIfSsOfdmaDcdFecCodeType_Type()
)
wmanIfSsOfdmaDcdFecCodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaDcdFecCodeType.setStatus("current")


class _WmanIfSsOfdmaDiucMandatoryExitThresh_Type(Integer32):
    """Custom type wmanIfSsOfdmaDiucMandatoryExitThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaDiucMandatoryExitThresh_Type.__name__ = "Integer32"
_WmanIfSsOfdmaDiucMandatoryExitThresh_Object = MibTableColumn
wmanIfSsOfdmaDiucMandatoryExitThresh = _WmanIfSsOfdmaDiucMandatoryExitThresh_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 4, 1, 4),
    _WmanIfSsOfdmaDiucMandatoryExitThresh_Type()
)
wmanIfSsOfdmaDiucMandatoryExitThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaDiucMandatoryExitThresh.setStatus("current")


class _WmanIfSsOfdmaDiucMinEntryThresh_Type(Integer32):
    """Custom type wmanIfSsOfdmaDiucMinEntryThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfSsOfdmaDiucMinEntryThresh_Type.__name__ = "Integer32"
_WmanIfSsOfdmaDiucMinEntryThresh_Object = MibTableColumn
wmanIfSsOfdmaDiucMinEntryThresh = _WmanIfSsOfdmaDiucMinEntryThresh_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 5, 2, 4, 1, 5),
    _WmanIfSsOfdmaDiucMinEntryThresh_Type()
)
wmanIfSsOfdmaDiucMinEntryThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsOfdmaDiucMinEntryThresh.setStatus("current")
_WmanIfCommonObjects_ObjectIdentity = ObjectIdentity
wmanIfCommonObjects = _WmanIfCommonObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3)
)
_WmanIfCmnPacketCs_ObjectIdentity = ObjectIdentity
wmanIfCmnPacketCs = _WmanIfCmnPacketCs_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1)
)
_WmanIfCmnClassifierRuleTable_Object = MibTable
wmanIfCmnClassifierRuleTable = _WmanIfCmnClassifierRuleTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleTable.setStatus("current")
_WmanIfCmnClassifierRuleEntry_Object = MibTableRow
wmanIfCmnClassifierRuleEntry = _WmanIfCmnClassifierRuleEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1)
)
wmanIfCmnClassifierRuleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfCmnCpsSfId"),
    (0, "WMAN-IF-MIB", "wmanIfCmnClassifierRuleIndex"),
)
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleEntry.setStatus("current")


class _WmanIfCmnClassifierRuleIndex_Type(Unsigned32):
    """Custom type wmanIfCmnClassifierRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfCmnClassifierRuleIndex_Type.__name__ = "Unsigned32"
_WmanIfCmnClassifierRuleIndex_Object = MibTableColumn
wmanIfCmnClassifierRuleIndex = _WmanIfCmnClassifierRuleIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 1),
    _WmanIfCmnClassifierRuleIndex_Type()
)
wmanIfCmnClassifierRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIndex.setStatus("current")


class _WmanIfCmnClassifierRulePriority_Type(Integer32):
    """Custom type wmanIfCmnClassifierRulePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfCmnClassifierRulePriority_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRulePriority_Object = MibTableColumn
wmanIfCmnClassifierRulePriority = _WmanIfCmnClassifierRulePriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 2),
    _WmanIfCmnClassifierRulePriority_Type()
)
wmanIfCmnClassifierRulePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRulePriority.setStatus("current")


class _WmanIfCmnClassifierRuleIpTosLow_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleIpTosLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfCmnClassifierRuleIpTosLow_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleIpTosLow_Object = MibTableColumn
wmanIfCmnClassifierRuleIpTosLow = _WmanIfCmnClassifierRuleIpTosLow_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 3),
    _WmanIfCmnClassifierRuleIpTosLow_Type()
)
wmanIfCmnClassifierRuleIpTosLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIpTosLow.setStatus("current")


class _WmanIfCmnClassifierRuleIpTosHigh_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleIpTosHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfCmnClassifierRuleIpTosHigh_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleIpTosHigh_Object = MibTableColumn
wmanIfCmnClassifierRuleIpTosHigh = _WmanIfCmnClassifierRuleIpTosHigh_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 4),
    _WmanIfCmnClassifierRuleIpTosHigh_Type()
)
wmanIfCmnClassifierRuleIpTosHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIpTosHigh.setStatus("current")


class _WmanIfCmnClassifierRuleIpTosMask_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleIpTosMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfCmnClassifierRuleIpTosMask_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleIpTosMask_Object = MibTableColumn
wmanIfCmnClassifierRuleIpTosMask = _WmanIfCmnClassifierRuleIpTosMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 5),
    _WmanIfCmnClassifierRuleIpTosMask_Type()
)
wmanIfCmnClassifierRuleIpTosMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIpTosMask.setStatus("current")


class _WmanIfCmnClassifierRuleIpProtocol_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfCmnClassifierRuleIpProtocol_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleIpProtocol_Object = MibTableColumn
wmanIfCmnClassifierRuleIpProtocol = _WmanIfCmnClassifierRuleIpProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 6),
    _WmanIfCmnClassifierRuleIpProtocol_Type()
)
wmanIfCmnClassifierRuleIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIpProtocol.setStatus("current")
_WmanIfCmnClassifierRuleIpSourceAddr_Type = InetAddress
_WmanIfCmnClassifierRuleIpSourceAddr_Object = MibTableColumn
wmanIfCmnClassifierRuleIpSourceAddr = _WmanIfCmnClassifierRuleIpSourceAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 7),
    _WmanIfCmnClassifierRuleIpSourceAddr_Type()
)
wmanIfCmnClassifierRuleIpSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIpSourceAddr.setStatus("current")
_WmanIfCmnClassifierRuleIpSourceMask_Type = InetAddress
_WmanIfCmnClassifierRuleIpSourceMask_Object = MibTableColumn
wmanIfCmnClassifierRuleIpSourceMask = _WmanIfCmnClassifierRuleIpSourceMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 8),
    _WmanIfCmnClassifierRuleIpSourceMask_Type()
)
wmanIfCmnClassifierRuleIpSourceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIpSourceMask.setStatus("current")
_WmanIfCmnClassifierRuleIpDestAddr_Type = InetAddress
_WmanIfCmnClassifierRuleIpDestAddr_Object = MibTableColumn
wmanIfCmnClassifierRuleIpDestAddr = _WmanIfCmnClassifierRuleIpDestAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 9),
    _WmanIfCmnClassifierRuleIpDestAddr_Type()
)
wmanIfCmnClassifierRuleIpDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIpDestAddr.setStatus("current")
_WmanIfCmnClassifierRuleIpDestMask_Type = InetAddress
_WmanIfCmnClassifierRuleIpDestMask_Object = MibTableColumn
wmanIfCmnClassifierRuleIpDestMask = _WmanIfCmnClassifierRuleIpDestMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 10),
    _WmanIfCmnClassifierRuleIpDestMask_Type()
)
wmanIfCmnClassifierRuleIpDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIpDestMask.setStatus("current")


class _WmanIfCmnClassifierRuleSourcePortStart_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleSourcePortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfCmnClassifierRuleSourcePortStart_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleSourcePortStart_Object = MibTableColumn
wmanIfCmnClassifierRuleSourcePortStart = _WmanIfCmnClassifierRuleSourcePortStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 11),
    _WmanIfCmnClassifierRuleSourcePortStart_Type()
)
wmanIfCmnClassifierRuleSourcePortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleSourcePortStart.setStatus("current")


class _WmanIfCmnClassifierRuleSourcePortEnd_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleSourcePortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfCmnClassifierRuleSourcePortEnd_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleSourcePortEnd_Object = MibTableColumn
wmanIfCmnClassifierRuleSourcePortEnd = _WmanIfCmnClassifierRuleSourcePortEnd_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 12),
    _WmanIfCmnClassifierRuleSourcePortEnd_Type()
)
wmanIfCmnClassifierRuleSourcePortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleSourcePortEnd.setStatus("current")


class _WmanIfCmnClassifierRuleDestPortStart_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleDestPortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfCmnClassifierRuleDestPortStart_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleDestPortStart_Object = MibTableColumn
wmanIfCmnClassifierRuleDestPortStart = _WmanIfCmnClassifierRuleDestPortStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 13),
    _WmanIfCmnClassifierRuleDestPortStart_Type()
)
wmanIfCmnClassifierRuleDestPortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleDestPortStart.setStatus("current")


class _WmanIfCmnClassifierRuleDestPortEnd_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleDestPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfCmnClassifierRuleDestPortEnd_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleDestPortEnd_Object = MibTableColumn
wmanIfCmnClassifierRuleDestPortEnd = _WmanIfCmnClassifierRuleDestPortEnd_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 14),
    _WmanIfCmnClassifierRuleDestPortEnd_Type()
)
wmanIfCmnClassifierRuleDestPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleDestPortEnd.setStatus("current")
_WmanIfCmnClassifierRuleDestMacAddr_Type = MacAddress
_WmanIfCmnClassifierRuleDestMacAddr_Object = MibTableColumn
wmanIfCmnClassifierRuleDestMacAddr = _WmanIfCmnClassifierRuleDestMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 15),
    _WmanIfCmnClassifierRuleDestMacAddr_Type()
)
wmanIfCmnClassifierRuleDestMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleDestMacAddr.setStatus("current")
_WmanIfCmnClassifierRuleDestMacMask_Type = MacAddress
_WmanIfCmnClassifierRuleDestMacMask_Object = MibTableColumn
wmanIfCmnClassifierRuleDestMacMask = _WmanIfCmnClassifierRuleDestMacMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 16),
    _WmanIfCmnClassifierRuleDestMacMask_Type()
)
wmanIfCmnClassifierRuleDestMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleDestMacMask.setStatus("current")
_WmanIfCmnClassifierRuleSourceMacAddr_Type = MacAddress
_WmanIfCmnClassifierRuleSourceMacAddr_Object = MibTableColumn
wmanIfCmnClassifierRuleSourceMacAddr = _WmanIfCmnClassifierRuleSourceMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 17),
    _WmanIfCmnClassifierRuleSourceMacAddr_Type()
)
wmanIfCmnClassifierRuleSourceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleSourceMacAddr.setStatus("current")
_WmanIfCmnClassifierRuleSourceMacMask_Type = MacAddress
_WmanIfCmnClassifierRuleSourceMacMask_Object = MibTableColumn
wmanIfCmnClassifierRuleSourceMacMask = _WmanIfCmnClassifierRuleSourceMacMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 18),
    _WmanIfCmnClassifierRuleSourceMacMask_Type()
)
wmanIfCmnClassifierRuleSourceMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleSourceMacMask.setStatus("current")


class _WmanIfCmnClassifierRuleEnetProtocolType_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleEnetProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ethertype", 1),
          ("dsap", 2))
    )


_WmanIfCmnClassifierRuleEnetProtocolType_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleEnetProtocolType_Object = MibTableColumn
wmanIfCmnClassifierRuleEnetProtocolType = _WmanIfCmnClassifierRuleEnetProtocolType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 19),
    _WmanIfCmnClassifierRuleEnetProtocolType_Type()
)
wmanIfCmnClassifierRuleEnetProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleEnetProtocolType.setStatus("current")


class _WmanIfCmnClassifierRuleEnetProtocol_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleEnetProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfCmnClassifierRuleEnetProtocol_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleEnetProtocol_Object = MibTableColumn
wmanIfCmnClassifierRuleEnetProtocol = _WmanIfCmnClassifierRuleEnetProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 20),
    _WmanIfCmnClassifierRuleEnetProtocol_Type()
)
wmanIfCmnClassifierRuleEnetProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleEnetProtocol.setStatus("current")


class _WmanIfCmnClassifierRuleUserPriLow_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleUserPriLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIfCmnClassifierRuleUserPriLow_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleUserPriLow_Object = MibTableColumn
wmanIfCmnClassifierRuleUserPriLow = _WmanIfCmnClassifierRuleUserPriLow_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 21),
    _WmanIfCmnClassifierRuleUserPriLow_Type()
)
wmanIfCmnClassifierRuleUserPriLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleUserPriLow.setStatus("current")


class _WmanIfCmnClassifierRuleUserPriHigh_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleUserPriHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIfCmnClassifierRuleUserPriHigh_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleUserPriHigh_Object = MibTableColumn
wmanIfCmnClassifierRuleUserPriHigh = _WmanIfCmnClassifierRuleUserPriHigh_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 22),
    _WmanIfCmnClassifierRuleUserPriHigh_Type()
)
wmanIfCmnClassifierRuleUserPriHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleUserPriHigh.setStatus("current")


class _WmanIfCmnClassifierRuleVlanId_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WmanIfCmnClassifierRuleVlanId_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleVlanId_Object = MibTableColumn
wmanIfCmnClassifierRuleVlanId = _WmanIfCmnClassifierRuleVlanId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 23),
    _WmanIfCmnClassifierRuleVlanId_Type()
)
wmanIfCmnClassifierRuleVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleVlanId.setStatus("current")


class _WmanIfCmnClassifierRuleState_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleState based on Integer32"""
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


_WmanIfCmnClassifierRuleState_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleState_Object = MibTableColumn
wmanIfCmnClassifierRuleState = _WmanIfCmnClassifierRuleState_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 24),
    _WmanIfCmnClassifierRuleState_Type()
)
wmanIfCmnClassifierRuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleState.setStatus("current")
_WmanIfCmnClassifierRulePkts_Type = Counter64
_WmanIfCmnClassifierRulePkts_Object = MibTableColumn
wmanIfCmnClassifierRulePkts = _WmanIfCmnClassifierRulePkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 25),
    _WmanIfCmnClassifierRulePkts_Type()
)
wmanIfCmnClassifierRulePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRulePkts.setStatus("current")
_WmanIfCmnClassifierRuleIpv6FlowLabel_Type = WmanIfIpv6FlowLabel
_WmanIfCmnClassifierRuleIpv6FlowLabel_Object = MibTableColumn
wmanIfCmnClassifierRuleIpv6FlowLabel = _WmanIfCmnClassifierRuleIpv6FlowLabel_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 26),
    _WmanIfCmnClassifierRuleIpv6FlowLabel_Type()
)
wmanIfCmnClassifierRuleIpv6FlowLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIpv6FlowLabel.setStatus("current")
_WmanIfCmnClassifierRuleBitMap_Type = WmanIfClassifierBitMap
_WmanIfCmnClassifierRuleBitMap_Object = MibTableColumn
wmanIfCmnClassifierRuleBitMap = _WmanIfCmnClassifierRuleBitMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 27),
    _WmanIfCmnClassifierRuleBitMap_Type()
)
wmanIfCmnClassifierRuleBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleBitMap.setStatus("current")
_WmanIfCmnPhsRuleTable_Object = MibTable
wmanIfCmnPhsRuleTable = _WmanIfCmnPhsRuleTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    wmanIfCmnPhsRuleTable.setStatus("current")
_WmanIfCmnPhsRuleEntry_Object = MibTableRow
wmanIfCmnPhsRuleEntry = _WmanIfCmnPhsRuleEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 2, 1)
)
wmanIfCmnPhsRuleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfCmnCpsSfId"),
    (0, "WMAN-IF-MIB", "wmanIfCmnPhsRulePhsIndex"),
)
if mibBuilder.loadTexts:
    wmanIfCmnPhsRuleEntry.setStatus("current")


class _WmanIfCmnPhsRulePhsIndex_Type(Integer32):
    """Custom type wmanIfCmnPhsRulePhsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WmanIfCmnPhsRulePhsIndex_Type.__name__ = "Integer32"
_WmanIfCmnPhsRulePhsIndex_Object = MibTableColumn
wmanIfCmnPhsRulePhsIndex = _WmanIfCmnPhsRulePhsIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 2, 1, 1),
    _WmanIfCmnPhsRulePhsIndex_Type()
)
wmanIfCmnPhsRulePhsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfCmnPhsRulePhsIndex.setStatus("current")


class _WmanIfCmnPhsRulePhsField_Type(OctetString):
    """Custom type wmanIfCmnPhsRulePhsField based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_WmanIfCmnPhsRulePhsField_Type.__name__ = "OctetString"
_WmanIfCmnPhsRulePhsField_Object = MibTableColumn
wmanIfCmnPhsRulePhsField = _WmanIfCmnPhsRulePhsField_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 2, 1, 2),
    _WmanIfCmnPhsRulePhsField_Type()
)
wmanIfCmnPhsRulePhsField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnPhsRulePhsField.setStatus("current")


class _WmanIfCmnPhsRulePhsMask_Type(OctetString):
    """Custom type wmanIfCmnPhsRulePhsMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_WmanIfCmnPhsRulePhsMask_Type.__name__ = "OctetString"
_WmanIfCmnPhsRulePhsMask_Object = MibTableColumn
wmanIfCmnPhsRulePhsMask = _WmanIfCmnPhsRulePhsMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 2, 1, 3),
    _WmanIfCmnPhsRulePhsMask_Type()
)
wmanIfCmnPhsRulePhsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnPhsRulePhsMask.setStatus("current")


class _WmanIfCmnPhsRulePhsSize_Type(Integer32):
    """Custom type wmanIfCmnPhsRulePhsSize based on Integer32"""
    defaultValue = 0


_WmanIfCmnPhsRulePhsSize_Type.__name__ = "Integer32"
_WmanIfCmnPhsRulePhsSize_Object = MibTableColumn
wmanIfCmnPhsRulePhsSize = _WmanIfCmnPhsRulePhsSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 2, 1, 4),
    _WmanIfCmnPhsRulePhsSize_Type()
)
wmanIfCmnPhsRulePhsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnPhsRulePhsSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnPhsRulePhsSize.setUnits("byte")


class _WmanIfCmnPhsRulePhsVerify_Type(WmanIfPhsRuleVerify):
    """Custom type wmanIfCmnPhsRulePhsVerify based on WmanIfPhsRuleVerify"""
    defaultValue = 0


_WmanIfCmnPhsRulePhsVerify_Type.__name__ = "WmanIfPhsRuleVerify"
_WmanIfCmnPhsRulePhsVerify_Object = MibTableColumn
wmanIfCmnPhsRulePhsVerify = _WmanIfCmnPhsRulePhsVerify_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 2, 1, 5),
    _WmanIfCmnPhsRulePhsVerify_Type()
)
wmanIfCmnPhsRulePhsVerify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnPhsRulePhsVerify.setStatus("current")
_WmanIfCmnCps_ObjectIdentity = ObjectIdentity
wmanIfCmnCps = _WmanIfCmnCps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2)
)
_WmanIfCmnCpsServiceFlowTable_Object = MibTable
wmanIfCmnCpsServiceFlowTable = _WmanIfCmnCpsServiceFlowTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIfCmnCpsServiceFlowTable.setStatus("current")
_WmanIfCmnCpsServiceFlowEntry_Object = MibTableRow
wmanIfCmnCpsServiceFlowEntry = _WmanIfCmnCpsServiceFlowEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1)
)
wmanIfCmnCpsServiceFlowEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfCmnCpsSfMacAddress"),
    (0, "WMAN-IF-MIB", "wmanIfCmnCpsSfId"),
)
if mibBuilder.loadTexts:
    wmanIfCmnCpsServiceFlowEntry.setStatus("current")
_WmanIfCmnCpsSfMacAddress_Type = MacAddress
_WmanIfCmnCpsSfMacAddress_Object = MibTableColumn
wmanIfCmnCpsSfMacAddress = _WmanIfCmnCpsSfMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 1),
    _WmanIfCmnCpsSfMacAddress_Type()
)
wmanIfCmnCpsSfMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfCmnCpsSfMacAddress.setStatus("current")


class _WmanIfCmnCpsSfId_Type(Unsigned32):
    """Custom type wmanIfCmnCpsSfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfCmnCpsSfId_Type.__name__ = "Unsigned32"
_WmanIfCmnCpsSfId_Object = MibTableColumn
wmanIfCmnCpsSfId = _WmanIfCmnCpsSfId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 2),
    _WmanIfCmnCpsSfId_Type()
)
wmanIfCmnCpsSfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsSfId.setStatus("current")
_WmanIfCmnCpsSfCid_Type = WmanIfCidType
_WmanIfCmnCpsSfCid_Object = MibTableColumn
wmanIfCmnCpsSfCid = _WmanIfCmnCpsSfCid_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 3),
    _WmanIfCmnCpsSfCid_Type()
)
wmanIfCmnCpsSfCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsSfCid.setStatus("current")


class _WmanIfCmnCpsSfDirection_Type(Integer32):
    """Custom type wmanIfCmnCpsSfDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 1),
          ("upstream", 2))
    )


_WmanIfCmnCpsSfDirection_Type.__name__ = "Integer32"
_WmanIfCmnCpsSfDirection_Object = MibTableColumn
wmanIfCmnCpsSfDirection = _WmanIfCmnCpsSfDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 4),
    _WmanIfCmnCpsSfDirection_Type()
)
wmanIfCmnCpsSfDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsSfDirection.setStatus("current")
_WmanIfCmnCpsSfState_Type = WmanIfSfState
_WmanIfCmnCpsSfState_Object = MibTableColumn
wmanIfCmnCpsSfState = _WmanIfCmnCpsSfState_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 5),
    _WmanIfCmnCpsSfState_Type()
)
wmanIfCmnCpsSfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsSfState.setStatus("current")


class _WmanIfCmnCpsTrafficPriority_Type(Integer32):
    """Custom type wmanIfCmnCpsTrafficPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIfCmnCpsTrafficPriority_Type.__name__ = "Integer32"
_WmanIfCmnCpsTrafficPriority_Object = MibTableColumn
wmanIfCmnCpsTrafficPriority = _WmanIfCmnCpsTrafficPriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 6),
    _WmanIfCmnCpsTrafficPriority_Type()
)
wmanIfCmnCpsTrafficPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsTrafficPriority.setStatus("current")
_WmanIfCmnCpsMaxSustainedRate_Type = Unsigned32
_WmanIfCmnCpsMaxSustainedRate_Object = MibTableColumn
wmanIfCmnCpsMaxSustainedRate = _WmanIfCmnCpsMaxSustainedRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 7),
    _WmanIfCmnCpsMaxSustainedRate_Type()
)
wmanIfCmnCpsMaxSustainedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMaxSustainedRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMaxSustainedRate.setUnits("b/s")
_WmanIfCmnCpsMaxTrafficBurst_Type = Unsigned32
_WmanIfCmnCpsMaxTrafficBurst_Object = MibTableColumn
wmanIfCmnCpsMaxTrafficBurst = _WmanIfCmnCpsMaxTrafficBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 8),
    _WmanIfCmnCpsMaxTrafficBurst_Type()
)
wmanIfCmnCpsMaxTrafficBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMaxTrafficBurst.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMaxTrafficBurst.setUnits("byte")
_WmanIfCmnCpsMinReservedRate_Type = Unsigned32
_WmanIfCmnCpsMinReservedRate_Object = MibTableColumn
wmanIfCmnCpsMinReservedRate = _WmanIfCmnCpsMinReservedRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 9),
    _WmanIfCmnCpsMinReservedRate_Type()
)
wmanIfCmnCpsMinReservedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMinReservedRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMinReservedRate.setUnits("byte")
_WmanIfCmnCpsToleratedJitter_Type = Unsigned32
_WmanIfCmnCpsToleratedJitter_Object = MibTableColumn
wmanIfCmnCpsToleratedJitter = _WmanIfCmnCpsToleratedJitter_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 10),
    _WmanIfCmnCpsToleratedJitter_Type()
)
wmanIfCmnCpsToleratedJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsToleratedJitter.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnCpsToleratedJitter.setUnits("millisecond")
_WmanIfCmnCpsMaxLatency_Type = Unsigned32
_WmanIfCmnCpsMaxLatency_Object = MibTableColumn
wmanIfCmnCpsMaxLatency = _WmanIfCmnCpsMaxLatency_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 11),
    _WmanIfCmnCpsMaxLatency_Type()
)
wmanIfCmnCpsMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMaxLatency.setUnits("millisecond")


class _WmanIfCmnCpsFixedVsVariableSduInd_Type(Integer32):
    """Custom type wmanIfCmnCpsFixedVsVariableSduInd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("variableLength", 0),
          ("fixedLength", 1))
    )


_WmanIfCmnCpsFixedVsVariableSduInd_Type.__name__ = "Integer32"
_WmanIfCmnCpsFixedVsVariableSduInd_Object = MibTableColumn
wmanIfCmnCpsFixedVsVariableSduInd = _WmanIfCmnCpsFixedVsVariableSduInd_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 12),
    _WmanIfCmnCpsFixedVsVariableSduInd_Type()
)
wmanIfCmnCpsFixedVsVariableSduInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsFixedVsVariableSduInd.setStatus("current")


class _WmanIfCmnCpsSduSize_Type(Unsigned32):
    """Custom type wmanIfCmnCpsSduSize based on Unsigned32"""
    defaultValue = 49


_WmanIfCmnCpsSduSize_Type.__name__ = "Unsigned32"
_WmanIfCmnCpsSduSize_Object = MibTableColumn
wmanIfCmnCpsSduSize = _WmanIfCmnCpsSduSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 13),
    _WmanIfCmnCpsSduSize_Type()
)
wmanIfCmnCpsSduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsSduSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnCpsSduSize.setUnits("byte")


class _WmanIfCmnCpsSfSchedulingType_Type(WmanIfSfSchedulingType):
    """Custom type wmanIfCmnCpsSfSchedulingType based on WmanIfSfSchedulingType"""
    defaultValue = 2


_WmanIfCmnCpsSfSchedulingType_Type.__name__ = "WmanIfSfSchedulingType"
_WmanIfCmnCpsSfSchedulingType_Object = MibTableColumn
wmanIfCmnCpsSfSchedulingType = _WmanIfCmnCpsSfSchedulingType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 14),
    _WmanIfCmnCpsSfSchedulingType_Type()
)
wmanIfCmnCpsSfSchedulingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsSfSchedulingType.setStatus("current")
_WmanIfCmnCpsArqEnable_Type = TruthValue
_WmanIfCmnCpsArqEnable_Object = MibTableColumn
wmanIfCmnCpsArqEnable = _WmanIfCmnCpsArqEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 15),
    _WmanIfCmnCpsArqEnable_Type()
)
wmanIfCmnCpsArqEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqEnable.setStatus("current")


class _WmanIfCmnCpsArqWindowSize_Type(Integer32):
    """Custom type wmanIfCmnCpsArqWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WmanIfCmnCpsArqWindowSize_Type.__name__ = "Integer32"
_WmanIfCmnCpsArqWindowSize_Object = MibTableColumn
wmanIfCmnCpsArqWindowSize = _WmanIfCmnCpsArqWindowSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 16),
    _WmanIfCmnCpsArqWindowSize_Type()
)
wmanIfCmnCpsArqWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqWindowSize.setStatus("current")


class _WmanIfCmnCpsArqBlockLifetime_Type(Integer32):
    """Custom type wmanIfCmnCpsArqBlockLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfCmnCpsArqBlockLifetime_Type.__name__ = "Integer32"
_WmanIfCmnCpsArqBlockLifetime_Object = MibTableColumn
wmanIfCmnCpsArqBlockLifetime = _WmanIfCmnCpsArqBlockLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 17),
    _WmanIfCmnCpsArqBlockLifetime_Type()
)
wmanIfCmnCpsArqBlockLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqBlockLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqBlockLifetime.setUnits("10 us")


class _WmanIfCmnCpsArqSyncLossTimeout_Type(Integer32):
    """Custom type wmanIfCmnCpsArqSyncLossTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfCmnCpsArqSyncLossTimeout_Type.__name__ = "Integer32"
_WmanIfCmnCpsArqSyncLossTimeout_Object = MibTableColumn
wmanIfCmnCpsArqSyncLossTimeout = _WmanIfCmnCpsArqSyncLossTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 18),
    _WmanIfCmnCpsArqSyncLossTimeout_Type()
)
wmanIfCmnCpsArqSyncLossTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqSyncLossTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqSyncLossTimeout.setUnits("10 us")
_WmanIfCmnCpsArqDeliverInOrder_Type = TruthValue
_WmanIfCmnCpsArqDeliverInOrder_Object = MibTableColumn
wmanIfCmnCpsArqDeliverInOrder = _WmanIfCmnCpsArqDeliverInOrder_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 19),
    _WmanIfCmnCpsArqDeliverInOrder_Type()
)
wmanIfCmnCpsArqDeliverInOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqDeliverInOrder.setStatus("current")


class _WmanIfCmnCpsArqRxPurgeTimeout_Type(Integer32):
    """Custom type wmanIfCmnCpsArqRxPurgeTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfCmnCpsArqRxPurgeTimeout_Type.__name__ = "Integer32"
_WmanIfCmnCpsArqRxPurgeTimeout_Object = MibTableColumn
wmanIfCmnCpsArqRxPurgeTimeout = _WmanIfCmnCpsArqRxPurgeTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 20),
    _WmanIfCmnCpsArqRxPurgeTimeout_Type()
)
wmanIfCmnCpsArqRxPurgeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqRxPurgeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqRxPurgeTimeout.setUnits("10 us")


class _WmanIfCmnCpsArqBlockSize_Type(Integer32):
    """Custom type wmanIfCmnCpsArqBlockSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2040),
    )


_WmanIfCmnCpsArqBlockSize_Type.__name__ = "Integer32"
_WmanIfCmnCpsArqBlockSize_Object = MibTableColumn
wmanIfCmnCpsArqBlockSize = _WmanIfCmnCpsArqBlockSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 21),
    _WmanIfCmnCpsArqBlockSize_Type()
)
wmanIfCmnCpsArqBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqBlockSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqBlockSize.setUnits("byte")
_WmanIfCmnCpsMinRsvdTolerableRate_Type = Unsigned32
_WmanIfCmnCpsMinRsvdTolerableRate_Object = MibTableColumn
wmanIfCmnCpsMinRsvdTolerableRate = _WmanIfCmnCpsMinRsvdTolerableRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 22),
    _WmanIfCmnCpsMinRsvdTolerableRate_Type()
)
wmanIfCmnCpsMinRsvdTolerableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMinRsvdTolerableRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMinRsvdTolerableRate.setUnits("b/s")


class _WmanIfCmnCpsReqTxPolicy_Type(Bits):
    """Custom type wmanIfCmnCpsReqTxPolicy based on Bits"""
    namedValues = NamedValues(
        *(("noBroadcastBwReq", 0),
          ("reserved1", 1),
          ("noPiggybackReq", 2),
          ("noFragmentData", 3),
          ("noPHS", 4),
          ("noSduPacking", 5),
          ("noCrc", 6),
          ("reserved2", 7))
    )

_WmanIfCmnCpsReqTxPolicy_Type.__name__ = "Bits"
_WmanIfCmnCpsReqTxPolicy_Object = MibTableColumn
wmanIfCmnCpsReqTxPolicy = _WmanIfCmnCpsReqTxPolicy_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 23),
    _WmanIfCmnCpsReqTxPolicy_Type()
)
wmanIfCmnCpsReqTxPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsReqTxPolicy.setStatus("current")
_WmanIfCmnSfCsSpecification_Type = WmanIfCsSpecification
_WmanIfCmnSfCsSpecification_Object = MibTableColumn
wmanIfCmnSfCsSpecification = _WmanIfCmnSfCsSpecification_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 24),
    _WmanIfCmnSfCsSpecification_Type()
)
wmanIfCmnSfCsSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnSfCsSpecification.setStatus("current")


class _WmanIfCmnCpsTargetSaid_Type(Integer32):
    """Custom type wmanIfCmnCpsTargetSaid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfCmnCpsTargetSaid_Type.__name__ = "Integer32"
_WmanIfCmnCpsTargetSaid_Object = MibTableColumn
wmanIfCmnCpsTargetSaid = _WmanIfCmnCpsTargetSaid_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 25),
    _WmanIfCmnCpsTargetSaid_Type()
)
wmanIfCmnCpsTargetSaid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsTargetSaid.setStatus("current")
_WmanIfCmnBsSsConfigurationTable_Object = MibTable
wmanIfCmnBsSsConfigurationTable = _WmanIfCmnBsSsConfigurationTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    wmanIfCmnBsSsConfigurationTable.setStatus("current")
_WmanIfCmnBsSsConfigurationEntry_Object = MibTableRow
wmanIfCmnBsSsConfigurationEntry = _WmanIfCmnBsSsConfigurationEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2, 1)
)
wmanIfCmnBsSsConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfCmnBsSsConfigurationEntry.setStatus("current")


class _WmanIfCmnInvitedRangRetries_Type(Integer32):
    """Custom type wmanIfCmnInvitedRangRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 65535),
    )


_WmanIfCmnInvitedRangRetries_Type.__name__ = "Integer32"
_WmanIfCmnInvitedRangRetries_Object = MibTableColumn
wmanIfCmnInvitedRangRetries = _WmanIfCmnInvitedRangRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2, 1, 1),
    _WmanIfCmnInvitedRangRetries_Type()
)
wmanIfCmnInvitedRangRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnInvitedRangRetries.setStatus("current")


class _WmanIfCmnDSxReqRetries_Type(Unsigned32):
    """Custom type wmanIfCmnDSxReqRetries based on Unsigned32"""
    defaultValue = 3


_WmanIfCmnDSxReqRetries_Type.__name__ = "Unsigned32"
_WmanIfCmnDSxReqRetries_Object = MibTableColumn
wmanIfCmnDSxReqRetries = _WmanIfCmnDSxReqRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2, 1, 2),
    _WmanIfCmnDSxReqRetries_Type()
)
wmanIfCmnDSxReqRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnDSxReqRetries.setStatus("current")


class _WmanIfCmnDSxRespRetries_Type(Unsigned32):
    """Custom type wmanIfCmnDSxRespRetries based on Unsigned32"""
    defaultValue = 3


_WmanIfCmnDSxRespRetries_Type.__name__ = "Unsigned32"
_WmanIfCmnDSxRespRetries_Object = MibTableColumn
wmanIfCmnDSxRespRetries = _WmanIfCmnDSxRespRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2, 1, 3),
    _WmanIfCmnDSxRespRetries_Type()
)
wmanIfCmnDSxRespRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnDSxRespRetries.setStatus("current")


class _WmanIfCmnT7Timeout_Type(Integer32):
    """Custom type wmanIfCmnT7Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WmanIfCmnT7Timeout_Type.__name__ = "Integer32"
_WmanIfCmnT7Timeout_Object = MibTableColumn
wmanIfCmnT7Timeout = _WmanIfCmnT7Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2, 1, 4),
    _WmanIfCmnT7Timeout_Type()
)
wmanIfCmnT7Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnT7Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnT7Timeout.setUnits("milliseconds")


class _WmanIfCmnT8Timeout_Type(Integer32):
    """Custom type wmanIfCmnT8Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_WmanIfCmnT8Timeout_Type.__name__ = "Integer32"
_WmanIfCmnT8Timeout_Object = MibTableColumn
wmanIfCmnT8Timeout = _WmanIfCmnT8Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2, 1, 5),
    _WmanIfCmnT8Timeout_Type()
)
wmanIfCmnT8Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnT8Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnT8Timeout.setUnits("milliseconds")


class _WmanIfCmnT10Timeout_Type(Integer32):
    """Custom type wmanIfCmnT10Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_WmanIfCmnT10Timeout_Type.__name__ = "Integer32"
_WmanIfCmnT10Timeout_Object = MibTableColumn
wmanIfCmnT10Timeout = _WmanIfCmnT10Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2, 1, 6),
    _WmanIfCmnT10Timeout_Type()
)
wmanIfCmnT10Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnT10Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnT10Timeout.setUnits("milliseconds")


class _WmanIfCmnT22Timeout_Type(Integer32):
    """Custom type wmanIfCmnT22Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_WmanIfCmnT22Timeout_Type.__name__ = "Integer32"
_WmanIfCmnT22Timeout_Object = MibTableColumn
wmanIfCmnT22Timeout = _WmanIfCmnT22Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2, 1, 7),
    _WmanIfCmnT22Timeout_Type()
)
wmanIfCmnT22Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnT22Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnT22Timeout.setUnits("milliseconds")
_WmanIfCmnPkmObjects_ObjectIdentity = ObjectIdentity
wmanIfCmnPkmObjects = _WmanIfCmnPkmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 3)
)
_WmanIfCmnCryptoSuiteTable_Object = MibTable
wmanIfCmnCryptoSuiteTable = _WmanIfCmnCryptoSuiteTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    wmanIfCmnCryptoSuiteTable.setStatus("current")
_WmanIfCmnCryptoSuiteEntry_Object = MibTableRow
wmanIfCmnCryptoSuiteEntry = _WmanIfCmnCryptoSuiteEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 3, 1, 1)
)
wmanIfCmnCryptoSuiteEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-MIB", "wmanIfCmnCryptoSuiteIndex"),
)
if mibBuilder.loadTexts:
    wmanIfCmnCryptoSuiteEntry.setStatus("current")


class _WmanIfCmnCryptoSuiteIndex_Type(Integer32):
    """Custom type wmanIfCmnCryptoSuiteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WmanIfCmnCryptoSuiteIndex_Type.__name__ = "Integer32"
_WmanIfCmnCryptoSuiteIndex_Object = MibTableColumn
wmanIfCmnCryptoSuiteIndex = _WmanIfCmnCryptoSuiteIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 3, 1, 1, 1),
    _WmanIfCmnCryptoSuiteIndex_Type()
)
wmanIfCmnCryptoSuiteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfCmnCryptoSuiteIndex.setStatus("current")
_WmanIfCmnCryptoSuiteDataEncryptAlg_Type = WmanIfDataEncryptAlgId
_WmanIfCmnCryptoSuiteDataEncryptAlg_Object = MibTableColumn
wmanIfCmnCryptoSuiteDataEncryptAlg = _WmanIfCmnCryptoSuiteDataEncryptAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 3, 1, 1, 2),
    _WmanIfCmnCryptoSuiteDataEncryptAlg_Type()
)
wmanIfCmnCryptoSuiteDataEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCryptoSuiteDataEncryptAlg.setStatus("current")
_WmanIfCmnCryptoSuiteDataAuthentAlg_Type = WmanIfDataAuthAlgId
_WmanIfCmnCryptoSuiteDataAuthentAlg_Object = MibTableColumn
wmanIfCmnCryptoSuiteDataAuthentAlg = _WmanIfCmnCryptoSuiteDataAuthentAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 3, 1, 1, 3),
    _WmanIfCmnCryptoSuiteDataAuthentAlg_Type()
)
wmanIfCmnCryptoSuiteDataAuthentAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCryptoSuiteDataAuthentAlg.setStatus("current")
_WmanIfCmnCryptoSuiteTekEncryptAlg_Type = WmanIfTekEncryptAlgId
_WmanIfCmnCryptoSuiteTekEncryptAlg_Object = MibTableColumn
wmanIfCmnCryptoSuiteTekEncryptAlg = _WmanIfCmnCryptoSuiteTekEncryptAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 3, 1, 1, 4),
    _WmanIfCmnCryptoSuiteTekEncryptAlg_Type()
)
wmanIfCmnCryptoSuiteTekEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCryptoSuiteTekEncryptAlg.setStatus("current")
_WmanIfMibConformance_ObjectIdentity = ObjectIdentity
wmanIfMibConformance = _WmanIfMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 2)
)
_WmanIfMibGroups_ObjectIdentity = ObjectIdentity
wmanIfMibGroups = _WmanIfMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 2, 1)
)
_WmanIfMibCompliances_ObjectIdentity = ObjectIdentity
wmanIfMibCompliances = _WmanIfMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 2, 2)
)
wmanIfBsRegisteredSsEntry.registerAugmentions(
    ("WMAN-IF-MIB",
     "wmanIfBsSsReqCapabilitiesEntry")
)
wmanIfBsSsReqCapabilitiesEntry.setIndexNames(*wmanIfBsRegisteredSsEntry.getIndexNames())
wmanIfBsRegisteredSsEntry.registerAugmentions(
    ("WMAN-IF-MIB",
     "wmanIfBsSsRspCapabilitiesEntry")
)
wmanIfBsSsRspCapabilitiesEntry.setIndexNames(*wmanIfBsRegisteredSsEntry.getIndexNames())
wmanIfBsRegisteredSsEntry.registerAugmentions(
    ("WMAN-IF-MIB",
     "wmanIfBsSsOfdmReqCapabilitiesEntry")
)
wmanIfBsSsOfdmReqCapabilitiesEntry.setIndexNames(*wmanIfBsRegisteredSsEntry.getIndexNames())
wmanIfBsRegisteredSsEntry.registerAugmentions(
    ("WMAN-IF-MIB",
     "wmanIfBsSsOfdmRspCapabilitiesEntry")
)
wmanIfBsSsOfdmRspCapabilitiesEntry.setIndexNames(*wmanIfBsRegisteredSsEntry.getIndexNames())

# Managed Objects groups

wmanIfMibCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 184, 2, 1, 1)
)
wmanIfMibCommonGroup.setObjects(
      *(("WMAN-IF-MIB", "wmanIfCmnClassifierRulePriority"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleIpTosLow"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleIpTosHigh"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleIpTosMask"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleIpProtocol"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleIpSourceAddr"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleIpSourceMask"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleIpDestAddr"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleIpDestMask"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleSourcePortStart"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleSourcePortEnd"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleDestPortStart"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleDestPortEnd"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleDestMacAddr"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleDestMacMask"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleSourceMacAddr"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleSourceMacMask"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleEnetProtocolType"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleEnetProtocol"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleUserPriLow"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleUserPriHigh"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleVlanId"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleState"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRulePkts"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleIpv6FlowLabel"),
        ("WMAN-IF-MIB", "wmanIfCmnClassifierRuleBitMap"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsTargetSaid"),
        ("WMAN-IF-MIB", "wmanIfCmnInvitedRangRetries"),
        ("WMAN-IF-MIB", "wmanIfCmnDSxReqRetries"),
        ("WMAN-IF-MIB", "wmanIfCmnDSxRespRetries"),
        ("WMAN-IF-MIB", "wmanIfCmnT7Timeout"),
        ("WMAN-IF-MIB", "wmanIfCmnT8Timeout"),
        ("WMAN-IF-MIB", "wmanIfCmnT10Timeout"),
        ("WMAN-IF-MIB", "wmanIfCmnT22Timeout"),
        ("WMAN-IF-MIB", "wmanIfCmnCryptoSuiteDataEncryptAlg"),
        ("WMAN-IF-MIB", "wmanIfCmnCryptoSuiteDataAuthentAlg"),
        ("WMAN-IF-MIB", "wmanIfCmnCryptoSuiteTekEncryptAlg"))
)
if mibBuilder.loadTexts:
    wmanIfMibCommonGroup.setStatus("current")

wmanIfMibQoSGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 184, 2, 1, 2)
)
wmanIfMibQoSGroup.setObjects(
      *(("WMAN-IF-MIB", "wmanIfCmnCpsSfId"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsSfCid"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsSfDirection"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsSfState"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsTrafficPriority"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsMaxSustainedRate"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsMaxTrafficBurst"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsMinReservedRate"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsToleratedJitter"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsMaxLatency"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsFixedVsVariableSduInd"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsSduSize"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsSfSchedulingType"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsArqEnable"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsArqWindowSize"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsArqBlockLifetime"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsArqSyncLossTimeout"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsArqDeliverInOrder"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsArqRxPurgeTimeout"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsArqBlockSize"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsMinRsvdTolerableRate"),
        ("WMAN-IF-MIB", "wmanIfCmnCpsReqTxPolicy"),
        ("WMAN-IF-MIB", "wmanIfCmnSfCsSpecification"))
)
if mibBuilder.loadTexts:
    wmanIfMibQoSGroup.setStatus("current")

wmanIfMibBsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 184, 2, 1, 3)
)
wmanIfMibBsGroup.setObjects(
      *(("WMAN-IF-MIB", "wmanIfBsSfDirection"),
        ("WMAN-IF-MIB", "wmanIfBsServiceClassIndex"),
        ("WMAN-IF-MIB", "wmanIfBsSfState"),
        ("WMAN-IF-MIB", "wmanIfBsSfProvisionedTime"),
        ("WMAN-IF-MIB", "wmanIfBsProvisionedSfRowStatus"),
        ("WMAN-IF-MIB", "wmanIfBsSsProvisionedForSfRowStatus"),
        ("WMAN-IF-MIB", "wmanIfBsSfCsSpecification"),
        ("WMAN-IF-MIB", "wmanIfBsQosServiceClassName"),
        ("WMAN-IF-MIB", "wmanIfBsQoSTrafficPriority"),
        ("WMAN-IF-MIB", "wmanIfBsQoSMaxSustainedRate"),
        ("WMAN-IF-MIB", "wmanIfBsQoSMaxTrafficBurst"),
        ("WMAN-IF-MIB", "wmanIfBsQoSMinReservedRate"),
        ("WMAN-IF-MIB", "wmanIfBsQoSToleratedJitter"),
        ("WMAN-IF-MIB", "wmanIfBsQoSMaxLatency"),
        ("WMAN-IF-MIB", "wmanIfBsQoSFixedVsVariableSduInd"),
        ("WMAN-IF-MIB", "wmanIfBsQoSSduSize"),
        ("WMAN-IF-MIB", "wmanIfBsQosScSchedulingType"),
        ("WMAN-IF-MIB", "wmanIfBsQosScArqEnable"),
        ("WMAN-IF-MIB", "wmanIfBsQosScArqWindowSize"),
        ("WMAN-IF-MIB", "wmanIfBsQosScArqBlockLifetime"),
        ("WMAN-IF-MIB", "wmanIfBsQosScArqSyncLossTimeout"),
        ("WMAN-IF-MIB", "wmanIfBsQosScArqDeliverInOrder"),
        ("WMAN-IF-MIB", "wmanIfBsQosScArqRxPurgeTimeout"),
        ("WMAN-IF-MIB", "wmanIfBsQosScArqBlockSize"),
        ("WMAN-IF-MIB", "wmanIfBsQosSCMinRsvdTolerableRate"),
        ("WMAN-IF-MIB", "wmanIfBsQoSReqTxPolicy"),
        ("WMAN-IF-MIB", "wmanIfBsQoSServiceClassRowStatus"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRulePriority"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleIpTosLow"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleIpTosHigh"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleIpTosMask"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleIpProtocol"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleIpSourceAddr"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleIpSourceMask"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleIpDestAddr"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleIpDestMask"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleSourcePortStart"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleSourcePortEnd"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleDestPortStart"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleDestPortEnd"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleDestMacAddr"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleDestMacMask"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleSourceMacAddr"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleSourceMacMask"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleEnetProtocolType"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleEnetProtocol"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleUserPriLow"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleUserPriHigh"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleVlanId"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleState"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRulePhsSize"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRulePhsMask"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRulePhsVerify"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleIpv6FlowLabel"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleBitMap"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleRowStatus"),
        ("WMAN-IF-MIB", "wmanIfBsSsMacSduCount"),
        ("WMAN-IF-MIB", "wmanIfBsSsOctetCount"),
        ("WMAN-IF-MIB", "wmanIfBsSsResetCounter"),
        ("WMAN-IF-MIB", "wmanIfBsSsResetCounterTime"),
        ("WMAN-IF-MIB", "wmanIfBsSsBasicCid"),
        ("WMAN-IF-MIB", "wmanIfBsSsPrimaryCid"),
        ("WMAN-IF-MIB", "wmanIfBsSsSecondaryCid"),
        ("WMAN-IF-MIB", "wmanIfBsSsManagementSupport"),
        ("WMAN-IF-MIB", "wmanIfBsSsIpManagementMode"),
        ("WMAN-IF-MIB", "wmanIfBs2ndMgmtDlQoSProfileIndex"),
        ("WMAN-IF-MIB", "wmanIfBs2ndMgmtUlQoSProfileIndex"),
        ("WMAN-IF-MIB", "wmanIfBsAutoSfidEnabled"),
        ("WMAN-IF-MIB", "wmanIfBsAutoSfidRangeMin"),
        ("WMAN-IF-MIB", "wmanIfBsAutoSfidRangeMax"),
        ("WMAN-IF-MIB", "wmanIfBsResetSector"),
        ("WMAN-IF-MIB", "wmanIfBsSs2ndMgmtArqEnable"),
        ("WMAN-IF-MIB", "wmanIfBsSs2ndMgmtArqWindowSize"),
        ("WMAN-IF-MIB", "wmanIfBsSs2ndMgmtArqDnLinkTxDelay"),
        ("WMAN-IF-MIB", "wmanIfBsSs2ndMgmtArqUpLinkTxDelay"),
        ("WMAN-IF-MIB", "wmanIfBsSs2ndMgmtArqDnLinkRxDelay"),
        ("WMAN-IF-MIB", "wmanIfBsSs2ndMgmtArqUpLinkRxDelay"),
        ("WMAN-IF-MIB", "wmanIfBsSs2ndMgmtArqBlockLifetime"),
        ("WMAN-IF-MIB", "wmanIfBsSs2ndMgmtArqSyncLossTimeout"),
        ("WMAN-IF-MIB", "wmanIfBsSs2ndMgmtArqDeliverInOrder"),
        ("WMAN-IF-MIB", "wmanIfBsSs2ndMgmtArqRxPurgeTimeout"),
        ("WMAN-IF-MIB", "wmanIfBsSs2ndMgmtArqBlockSize"),
        ("WMAN-IF-MIB", "wmanIfBsSsVendorIdEncoding"),
        ("WMAN-IF-MIB", "wmanIfBsSsAasBroadcastPermission"),
        ("WMAN-IF-MIB", "wmanIfBsSsMaxTxPowerBpsk"),
        ("WMAN-IF-MIB", "wmanIfBsSsMaxTxPowerQpsk"),
        ("WMAN-IF-MIB", "wmanIfBsSsMaxTxPower16Qam"),
        ("WMAN-IF-MIB", "wmanIfBsSsMaxTxPower64Qam"),
        ("WMAN-IF-MIB", "wmanIfBsSsMacVersion"),
        ("WMAN-IF-MIB", "wmanIfBsDcdInterval"),
        ("WMAN-IF-MIB", "wmanIfBsUcdInterval"),
        ("WMAN-IF-MIB", "wmanIfBsUcdTransition"),
        ("WMAN-IF-MIB", "wmanIfBsDcdTransition"),
        ("WMAN-IF-MIB", "wmanIfBsInitialRangingInterval"),
        ("WMAN-IF-MIB", "wmanIfBsSsULMapProcTime"),
        ("WMAN-IF-MIB", "wmanIfBsSsRangRespProcTime"),
        ("WMAN-IF-MIB", "wmanIfBsT5Timeout"),
        ("WMAN-IF-MIB", "wmanIfBsT9Timeout"),
        ("WMAN-IF-MIB", "wmanIfBsT13Timeout"),
        ("WMAN-IF-MIB", "wmanIfBsT15Timeout"),
        ("WMAN-IF-MIB", "wmanIfBsT17Timeout"),
        ("WMAN-IF-MIB", "wmanIfBsT27IdleTimer"),
        ("WMAN-IF-MIB", "wmanIfBsT27ActiveTimer"),
        ("WMAN-IF-MIB", "wmanIfBsHistogramIndex"),
        ("WMAN-IF-MIB", "wmanIfBsChannelNumber"),
        ("WMAN-IF-MIB", "wmanIfBsStartFrame"),
        ("WMAN-IF-MIB", "wmanIfBsDuration"),
        ("WMAN-IF-MIB", "wmanIfBsBasicReport"),
        ("WMAN-IF-MIB", "wmanIfBsMeanCinrReport"),
        ("WMAN-IF-MIB", "wmanIfBsMeanRssiReport"),
        ("WMAN-IF-MIB", "wmanIfBsStdDeviationCinrReport"),
        ("WMAN-IF-MIB", "wmanIfBsStdDeviationRssiReport"),
        ("WMAN-IF-MIB", "wmanIfBsSsReqCapUplinkCidSupport"),
        ("WMAN-IF-MIB", "wmanIfBsSsReqCapArqSupport"),
        ("WMAN-IF-MIB", "wmanIfBsSsReqCapDsxFlowControl"),
        ("WMAN-IF-MIB", "wmanIfBsSsReqCapMacCrcSupport"),
        ("WMAN-IF-MIB", "wmanIfBsSsReqCapMcaFlowControl"),
        ("WMAN-IF-MIB", "wmanIfBsSsReqCapMcpGroupCidSupport"),
        ("WMAN-IF-MIB", "wmanIfBsSsReqCapPkmFlowControl"),
        ("WMAN-IF-MIB", "wmanIfBsSsReqCapAuthPolicyControl"),
        ("WMAN-IF-MIB", "wmanIfBsSsReqCapMaxNumOfSupportedSA"),
        ("WMAN-IF-MIB", "wmanIfBsSsReqCapIpVersion"),
        ("WMAN-IF-MIB", "wmanIfBsSsReqCapMacCsSupportBitMap"),
        ("WMAN-IF-MIB", "wmanIfBsSsReqCapMaxNumOfClassifier"),
        ("WMAN-IF-MIB", "wmanIfBsSsReqCapPhsSupport"),
        ("WMAN-IF-MIB", "wmanIfBsSsReqCapBandwidthAllocSupport"),
        ("WMAN-IF-MIB", "wmanIfBsSsReqCapPduConstruction"),
        ("WMAN-IF-MIB", "wmanIfBsSsReqCapTtgTransitionGap"),
        ("WMAN-IF-MIB", "wmanIfBsSsReqCapRtgTransitionGap"),
        ("WMAN-IF-MIB", "wmanIfBsSsRspCapUplinkCidSupport"),
        ("WMAN-IF-MIB", "wmanIfBsSsRspCapArqSupport"),
        ("WMAN-IF-MIB", "wmanIfBsSsRspCapDsxFlowControl"),
        ("WMAN-IF-MIB", "wmanIfBsSsRspCapMacCrcSupport"),
        ("WMAN-IF-MIB", "wmanIfBsSsRspCapMcaFlowControl"),
        ("WMAN-IF-MIB", "wmanIfBsSsRspCapMcpGroupCidSupport"),
        ("WMAN-IF-MIB", "wmanIfBsSsRspCapPkmFlowControl"),
        ("WMAN-IF-MIB", "wmanIfBsSsRspCapAuthPolicyControl"),
        ("WMAN-IF-MIB", "wmanIfBsSsRspCapMaxNumOfSupportedSA"),
        ("WMAN-IF-MIB", "wmanIfBsSsRspCapIpVersion"),
        ("WMAN-IF-MIB", "wmanIfBsSsRspCapMacCsSupportBitMap"),
        ("WMAN-IF-MIB", "wmanIfBsSsRspCapMaxNumOfClassifier"),
        ("WMAN-IF-MIB", "wmanIfBsSsRspCapPhsSupport"),
        ("WMAN-IF-MIB", "wmanIfBsSsRspCapBandwidthAllocSupport"),
        ("WMAN-IF-MIB", "wmanIfBsSsRspCapPduConstruction"),
        ("WMAN-IF-MIB", "wmanIfBsSsRspCapTtgTransitionGap"),
        ("WMAN-IF-MIB", "wmanIfBsSsRspCapRtgTransitionGap"),
        ("WMAN-IF-MIB", "wmanIfBsCapUplinkCidSupport"),
        ("WMAN-IF-MIB", "wmanIfBsCapArqSupport"),
        ("WMAN-IF-MIB", "wmanIfBsCapDsxFlowControl"),
        ("WMAN-IF-MIB", "wmanIfBsCapMacCrcSupport"),
        ("WMAN-IF-MIB", "wmanIfBsCapMcaFlowControl"),
        ("WMAN-IF-MIB", "wmanIfBsCapMcpGroupCidSupport"),
        ("WMAN-IF-MIB", "wmanIfBsCapPkmFlowControl"),
        ("WMAN-IF-MIB", "wmanIfBsCapAuthPolicyControl"),
        ("WMAN-IF-MIB", "wmanIfBsCapMaxNumOfSupportedSA"),
        ("WMAN-IF-MIB", "wmanIfBsCapIpVersion"),
        ("WMAN-IF-MIB", "wmanIfBsCapMacCsSupportBitMap"),
        ("WMAN-IF-MIB", "wmanIfBsCapMaxNumOfClassifier"),
        ("WMAN-IF-MIB", "wmanIfBsCapPhsSupport"),
        ("WMAN-IF-MIB", "wmanIfBsCapBandwidthAllocSupport"),
        ("WMAN-IF-MIB", "wmanIfBsCapPduConstruction"),
        ("WMAN-IF-MIB", "wmanIfBsCapTtgTransitionGap"),
        ("WMAN-IF-MIB", "wmanIfBsCapRtgTransitionGap"),
        ("WMAN-IF-MIB", "wmanIfBsCapCfgUplinkCidSupport"),
        ("WMAN-IF-MIB", "wmanIfBsCapCfgArqSupport"),
        ("WMAN-IF-MIB", "wmanIfBsCapCfgDsxFlowControl"),
        ("WMAN-IF-MIB", "wmanIfBsCapCfgMacCrcSupport"),
        ("WMAN-IF-MIB", "wmanIfBsCapCfgMcaFlowControl"),
        ("WMAN-IF-MIB", "wmanIfBsCapCfgMcpGroupCidSupport"),
        ("WMAN-IF-MIB", "wmanIfBsCapCfgPkmFlowControl"),
        ("WMAN-IF-MIB", "wmanIfBsCapCfgAuthPolicyControl"),
        ("WMAN-IF-MIB", "wmanIfBsCapCfgMaxNumOfSupportedSA"),
        ("WMAN-IF-MIB", "wmanIfBsCapCfgIpVersion"),
        ("WMAN-IF-MIB", "wmanIfBsCapCfgMacCsSupportBitMap"),
        ("WMAN-IF-MIB", "wmanIfBsCapCfgMaxNumOfClassifier"),
        ("WMAN-IF-MIB", "wmanIfBsCapCfgPhsSupport"),
        ("WMAN-IF-MIB", "wmanIfBsCapCfgBandwidthAllocSupport"),
        ("WMAN-IF-MIB", "wmanIfBsCapCfgPduConstruction"),
        ("WMAN-IF-MIB", "wmanIfBsCapCfgTtgTransitionGap"),
        ("WMAN-IF-MIB", "wmanIfBsCapCfgRtgTransitionGap"),
        ("WMAN-IF-MIB", "wmanIfBsSsActionsResetSs"),
        ("WMAN-IF-MIB", "wmanIfBsSsActionsAbortSs"),
        ("WMAN-IF-MIB", "wmanIfBsSsActionsOverrideDnFreq"),
        ("WMAN-IF-MIB", "wmanIfBsSsActionsOverrideChannelId"),
        ("WMAN-IF-MIB", "wmanIfBsSsActionsDeReRegSs"),
        ("WMAN-IF-MIB", "wmanIfBsSsActionsDeReRegSsCode"),
        ("WMAN-IF-MIB", "wmanIfBsSsActionsRowStatus"),
        ("WMAN-IF-MIB", "wmanIfBsPkmDefaultAuthLifetime"),
        ("WMAN-IF-MIB", "wmanIfBsPkmDefaultTekLifetime"),
        ("WMAN-IF-MIB", "wmanIfBsPkmDefaultSelfSigManufCertTrust"),
        ("WMAN-IF-MIB", "wmanIfBsPkmCheckCertValidityPeriods"),
        ("WMAN-IF-MIB", "wmanIfBsPkmAuthentInfos"),
        ("WMAN-IF-MIB", "wmanIfBsPkmAuthRequests"),
        ("WMAN-IF-MIB", "wmanIfBsPkmAuthReplies"),
        ("WMAN-IF-MIB", "wmanIfBsPkmAuthRejects"),
        ("WMAN-IF-MIB", "wmanIfBsPkmAuthInvalids"),
        ("WMAN-IF-MIB", "wmanIfBsSsPkmAuthKeySequenceNumber"),
        ("WMAN-IF-MIB", "wmanIfBsSsPkmAuthExpiresOld"),
        ("WMAN-IF-MIB", "wmanIfBsSsPkmAuthExpiresNew"),
        ("WMAN-IF-MIB", "wmanIfBsSsPkmAuthLifetime"),
        ("WMAN-IF-MIB", "wmanIfBsSsPkmAuthReset"),
        ("WMAN-IF-MIB", "wmanIfBsSsPkmAuthInfos"),
        ("WMAN-IF-MIB", "wmanIfBsSsPkmAuthRequests"),
        ("WMAN-IF-MIB", "wmanIfBsSsPkmAuthReplies"),
        ("WMAN-IF-MIB", "wmanIfBsSsPkmAuthRejects"),
        ("WMAN-IF-MIB", "wmanIfBsSsPkmAuthInvalids"),
        ("WMAN-IF-MIB", "wmanIfBsSsPkmAuthRejectErrorCode"),
        ("WMAN-IF-MIB", "wmanIfBsSsPkmAuthRejectErrorString"),
        ("WMAN-IF-MIB", "wmanIfBsSsPkmAuthInvalidErrorCode"),
        ("WMAN-IF-MIB", "wmanIfBsSsPkmAuthInvalidErrorString"),
        ("WMAN-IF-MIB", "wmanIfBsSsPkmAuthPrimarySAId"),
        ("WMAN-IF-MIB", "wmanIfBsSsPkmAuthValidStatus"),
        ("WMAN-IF-MIB", "wmanIfBsPkmTekSAType"),
        ("WMAN-IF-MIB", "wmanIfBsPkmTekDataEncryptAlg"),
        ("WMAN-IF-MIB", "wmanIfBsPkmTekDataAuthentAlg"),
        ("WMAN-IF-MIB", "wmanIfBsPkmTekEncryptAlg"),
        ("WMAN-IF-MIB", "wmanIfBsPkmTekLifetime"),
        ("WMAN-IF-MIB", "wmanIfBsPkmTekKeySequenceNumber"),
        ("WMAN-IF-MIB", "wmanIfBsPkmTekExpiresOld"),
        ("WMAN-IF-MIB", "wmanIfBsPkmTekExpiresNew"),
        ("WMAN-IF-MIB", "wmanIfBsPkmTekReset"),
        ("WMAN-IF-MIB", "wmanIfBsPkmKeyRequests"),
        ("WMAN-IF-MIB", "wmanIfBsPkmKeyReplies"),
        ("WMAN-IF-MIB", "wmanIfBsPkmKeyRejects"),
        ("WMAN-IF-MIB", "wmanIfBsPkmTekInvalids"),
        ("WMAN-IF-MIB", "wmanIfBsPkmKeyRejectErrorCode"),
        ("WMAN-IF-MIB", "wmanIfBsPkmKeyRejectErrorString"),
        ("WMAN-IF-MIB", "wmanIfBsPkmTekInvalidErrorCode"),
        ("WMAN-IF-MIB", "wmanIfBsPkmTekInvalidErrorString"),
        ("WMAN-IF-MIB", "wmanIfBsTrapControlRegister"),
        ("WMAN-IF-MIB", "wmanIfBsStatusTrapControlRegister"),
        ("WMAN-IF-MIB", "wmanIfBsRssiLowThreshold"),
        ("WMAN-IF-MIB", "wmanIfBsRssiHighThreshold"),
        ("WMAN-IF-MIB", "wmanIfBsSsNotificationMacAddr"),
        ("WMAN-IF-MIB", "wmanIfBsSsStatusValue"),
        ("WMAN-IF-MIB", "wmanIfBsSsStatusInfo"),
        ("WMAN-IF-MIB", "wmanIfBsDynamicServiceType"),
        ("WMAN-IF-MIB", "wmanIfBsDynamicServiceFailReason"),
        ("WMAN-IF-MIB", "wmanIfBsSsRssiStatus"),
        ("WMAN-IF-MIB", "wmanIfBsSsRssiStatusInfo"),
        ("WMAN-IF-MIB", "wmanIfBsSsRegisterStatus"))
)
if mibBuilder.loadTexts:
    wmanIfMibBsGroup.setStatus("current")

wmanIfMibBsAasGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 184, 2, 1, 4)
)
wmanIfMibBsAasGroup.setObjects(
      *(("WMAN-IF-MIB", "wmanIfBsAasChanFbckReqFreq"),
        ("WMAN-IF-MIB", "wmanIfBsAasBeamSelectFreq"),
        ("WMAN-IF-MIB", "wmanIfBsAasChanFbckReqResolution"),
        ("WMAN-IF-MIB", "wmanIfBsAasBeamReqResolution"),
        ("WMAN-IF-MIB", "wmanIfBsAasNumOptDiversityZones"))
)
if mibBuilder.loadTexts:
    wmanIfMibBsAasGroup.setStatus("current")

wmanIfMibSsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 184, 2, 1, 5)
)
wmanIfMibSsGroup.setObjects(
      *(("WMAN-IF-MIB", "wmanIfSsLostDLMapInterval"),
        ("WMAN-IF-MIB", "wmanIfSsLostULMapInterval"),
        ("WMAN-IF-MIB", "wmanIfSsContentionRangRetries"),
        ("WMAN-IF-MIB", "wmanIfSsRequestRetries"),
        ("WMAN-IF-MIB", "wmanIfSsRegRequestRetries"),
        ("WMAN-IF-MIB", "wmanIfSsTftpBackoffStart"),
        ("WMAN-IF-MIB", "wmanIfSsTftpBackoffEnd"),
        ("WMAN-IF-MIB", "wmanIfSsTftpRequestRetries"),
        ("WMAN-IF-MIB", "wmanIfSsTftpDownloadRetries"),
        ("WMAN-IF-MIB", "wmanIfSsTftpWait"),
        ("WMAN-IF-MIB", "wmanIfSsToDRetries"),
        ("WMAN-IF-MIB", "wmanIfSsToDRetryPeriod"),
        ("WMAN-IF-MIB", "wmanIfSsT1Timeout"),
        ("WMAN-IF-MIB", "wmanIfSsT2Timeout"),
        ("WMAN-IF-MIB", "wmanIfSsT3Timeout"),
        ("WMAN-IF-MIB", "wmanIfSsT4Timeout"),
        ("WMAN-IF-MIB", "wmanIfSsT6Timeout"),
        ("WMAN-IF-MIB", "wmanIfSsT12Timeout"),
        ("WMAN-IF-MIB", "wmanIfSsT14Timeout"),
        ("WMAN-IF-MIB", "wmanIfSsT16Timeout"),
        ("WMAN-IF-MIB", "wmanIfSsT18Timeout"),
        ("WMAN-IF-MIB", "wmanIfSsT19Timeout"),
        ("WMAN-IF-MIB", "wmanIfSsT20Timeout"),
        ("WMAN-IF-MIB", "wmanIfSsT21Timeout"),
        ("WMAN-IF-MIB", "wmanIfSsSBCRequestRetries"),
        ("WMAN-IF-MIB", "wmanIfSsTftpCpltRetries"),
        ("WMAN-IF-MIB", "wmanIfSsT26Timeout"),
        ("WMAN-IF-MIB", "wmanIfSsDLManagProcTime"),
        ("WMAN-IF-MIB", "wmanIfSsChannelNumber"),
        ("WMAN-IF-MIB", "wmanIfSsStartFrame"),
        ("WMAN-IF-MIB", "wmanIfSsDuration"),
        ("WMAN-IF-MIB", "wmanIfSsBasicReport"),
        ("WMAN-IF-MIB", "wmanIfSsMeanCinrReport"),
        ("WMAN-IF-MIB", "wmanIfSsStdDeviationCinrReport"),
        ("WMAN-IF-MIB", "wmanIfSsMeanRssiReport"),
        ("WMAN-IF-MIB", "wmanIfSsStdDeviationRssiReport"),
        ("WMAN-IF-MIB", "wmanIfSsPkmAuthState"),
        ("WMAN-IF-MIB", "wmanIfSsPkmAuthKeySequenceNumber"),
        ("WMAN-IF-MIB", "wmanIfSsPkmAuthExpiresOld"),
        ("WMAN-IF-MIB", "wmanIfSsPkmAuthExpiresNew"),
        ("WMAN-IF-MIB", "wmanIfSsPkmAuthReset"),
        ("WMAN-IF-MIB", "wmanIfSsPkmAuthentInfos"),
        ("WMAN-IF-MIB", "wmanIfSsPkmAuthRequests"),
        ("WMAN-IF-MIB", "wmanIfSsPkmAuthReplies"),
        ("WMAN-IF-MIB", "wmanIfSsPkmAuthRejects"),
        ("WMAN-IF-MIB", "wmanIfSsPkmAuthInvalids"),
        ("WMAN-IF-MIB", "wmanIfSsPkmAuthRejectErrorCode"),
        ("WMAN-IF-MIB", "wmanIfSsPkmAuthRejectErrorString"),
        ("WMAN-IF-MIB", "wmanIfSsPkmAuthInvalidErrorCode"),
        ("WMAN-IF-MIB", "wmanIfSsPkmAuthInvalidErrorString"),
        ("WMAN-IF-MIB", "wmanIfSsPkmAuthGraceTime"),
        ("WMAN-IF-MIB", "wmanIfSsPkmTekGraceTime"),
        ("WMAN-IF-MIB", "wmanIfSsPkmAuthWaitTimeout"),
        ("WMAN-IF-MIB", "wmanIfSsPkmReauthWaitTimeout"),
        ("WMAN-IF-MIB", "wmanIfSsPkmOpWaitTimeout"),
        ("WMAN-IF-MIB", "wmanIfSsPkmRekeyWaitTimeout"),
        ("WMAN-IF-MIB", "wmanIfSsPkmAuthRejectWaitTimeout"),
        ("WMAN-IF-MIB", "wmanIfSsPkmTekSAType"),
        ("WMAN-IF-MIB", "wmanIfSsPkmTekDataEncryptAlg"),
        ("WMAN-IF-MIB", "wmanIfSsPkmTekDataAuthentAlg"),
        ("WMAN-IF-MIB", "wmanIfSsPkmTekEncryptAlg"),
        ("WMAN-IF-MIB", "wmanIfSsPkmTekState"),
        ("WMAN-IF-MIB", "wmanIfSsPkmTekKeySequenceNumber"),
        ("WMAN-IF-MIB", "wmanIfSsPkmTekExpiresOld"),
        ("WMAN-IF-MIB", "wmanIfSsPkmTekExpiresNew"),
        ("WMAN-IF-MIB", "wmanIfSsPkmTekKeyRequests"),
        ("WMAN-IF-MIB", "wmanIfSsPkmTekKeyReplies"),
        ("WMAN-IF-MIB", "wmanIfSsPkmTekKeyRejects"),
        ("WMAN-IF-MIB", "wmanIfSsPkmTekInvalids"),
        ("WMAN-IF-MIB", "wmanIfSsPkmTekAuthPends"),
        ("WMAN-IF-MIB", "wmanIfSsPkmTekKeyRejectErrorCode"),
        ("WMAN-IF-MIB", "wmanIfSsPkmTekKeyRejectErrorString"),
        ("WMAN-IF-MIB", "wmanIfSsPkmTekInvalidErrorCode"),
        ("WMAN-IF-MIB", "wmanIfSsPkmTekInvalidErrorString"),
        ("WMAN-IF-MIB", "wmanIfSsDeviceCert"),
        ("WMAN-IF-MIB", "wmanIfSsDeviceManufCert"),
        ("WMAN-IF-MIB", "wmanIfSsTrapControlRegister"),
        ("WMAN-IF-MIB", "wmanIfSsRssiLowThreshold"),
        ("WMAN-IF-MIB", "wmanIfSsRssiHighThreshold"),
        ("WMAN-IF-MIB", "wmanIfSsMacAddress"),
        ("WMAN-IF-MIB", "wmanIfSsUnknownTlv"),
        ("WMAN-IF-MIB", "wmanIfSsDynamicServiceType"),
        ("WMAN-IF-MIB", "wmanIfSsDynamicServiceFailReason"),
        ("WMAN-IF-MIB", "wmanIfSsRssiStatus"),
        ("WMAN-IF-MIB", "wmanIfSsRssiStatusInfo"))
)
if mibBuilder.loadTexts:
    wmanIfMibSsGroup.setStatus("current")

wmanIfMibBsOfdmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 184, 2, 1, 6)
)
wmanIfMibBsOfdmGroup.setObjects(
      *(("WMAN-IF-MIB", "wmanIfBsOfdmCtBasedResvTimeout"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmBwReqOppSize"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmRangReqOppSize"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmUplinkCenterFreq"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmNumSubChReqRegionFull"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmNumSymbolsReqRegionFull"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmSubChFocusCtCode"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmUpLinkChannelId"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmBsEIRP"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmChannelNumber"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmTTG"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmRTG"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmInitRngMaxRSS"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmDownlinkCenterFreq"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmBsId"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmMacVersion"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmFrameDurationCode"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmDownLinkChannelId"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmUcdFecCodeType"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmFocusCtPowerBoost"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmUcdTcsEnable"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmUcdBurstProfileRowStatus"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmDownlinkFrequency"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmDcdFecCodeType"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmDiucMandatoryExitThresh"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmDiucMinEntryThresh"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmTcsEnable"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmDcdBurstProfileRowStatus"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmMinReqRegionFullTxOpp"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmMinFocusedCtTxOpp"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmMaxRoundTripDelay"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmRangeAbortTimingThold"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmRangeAbortPowerThold"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmRangeAbortFreqThold"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmDnlkRateId"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmRatioG"),
        ("WMAN-IF-MIB", "wmanIfBsSsOfdmReqCapFftSizes"),
        ("WMAN-IF-MIB", "wmanIfBsSsOfdmReqCapSsDemodulator"),
        ("WMAN-IF-MIB", "wmanIfBsSsOfdmReqCapSsModulator"),
        ("WMAN-IF-MIB", "wmanIfBsSsOfdmReqCapFocusedCtSupport"),
        ("WMAN-IF-MIB", "wmanIfBsSsOfdmReqCapTcSublayerSupport"),
        ("WMAN-IF-MIB", "wmanIfBsSsOfdmRspCapFftSizes"),
        ("WMAN-IF-MIB", "wmanIfBsSsOfdmRspCapSsDemodulator"),
        ("WMAN-IF-MIB", "wmanIfBsSsOfdmRspCapSsModulator"),
        ("WMAN-IF-MIB", "wmanIfBsSsOfdmRspCapFocusedCtSupport"),
        ("WMAN-IF-MIB", "wmanIfBsSsOfdmRspCapTcSublayerSupport"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmCapFftSizes"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmCapSsDemodulator"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmCapSsModulator"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmCapFocusedCtSupport"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmCapTcSublayerSupport"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmCapCfgFftSizes"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmCapCfgSsDemodulator"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmCapCfgSsModulator"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmCapCfgFocusedCtSupport"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmCapCfgTcSublayerSupport"))
)
if mibBuilder.loadTexts:
    wmanIfMibBsOfdmGroup.setStatus("current")

wmanIfMibSsOfdmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 184, 2, 1, 7)
)
wmanIfMibSsOfdmGroup.setObjects(
      *(("WMAN-IF-MIB", "wmanIfSsOfdmCtBasedResvTimeout"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmBwReqOppSize"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmRangReqOppSize"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmUplinkCenterFreq"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmNumSubChReqRegionFull"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmNumSymbolsReqRegionFull"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmSubChFocusCtCode"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmUpLinkChannelId"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmBsEIRP"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmChannelNumber"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmTTG"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmRTG"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmInitRngMaxRSS"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmDownlinkCenterFreq"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmBsId"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmMacVersion"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmFrameDurationCode"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmDownLinkChannelId"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmUcdFecCodeType"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmFocusCtPowerBoost"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmUcdTcsEnable"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmDownlinkFrequency"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmDcdFecCodeType"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmDiucMandatoryExitThresh"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmDiucMinEntryThresh"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmTcsEnable"))
)
if mibBuilder.loadTexts:
    wmanIfMibSsOfdmGroup.setStatus("current")

wmanIfMibBsOfdmaGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 184, 2, 1, 8)
)
wmanIfMibBsOfdmaGroup.setObjects(
      *(("WMAN-IF-MIB", "wmanIfBsOfdmaCtBasedResvTimeout"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaBwReqOppSize"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaRangReqOppSize"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaUplinkCenterFreq"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaInitRngCodes"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaPeriodicRngCodes"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaBWReqCodes"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaPerRngBackoffStart"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaPerRngBackoffEnd"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaStartOfRngCodes"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaPermutationBase"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaULAllocSubchBitmap"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaOptPermULAllocSubchBitmap"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaBandAMCAllocThreshold"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaBandAMCReleaseThreshold"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaBandAMCAllocTimer"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaBandAMCReleaseTimer"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaBandStatRepMAXPeriod"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaBandAMCRetryTimer"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaSafetyChAllocThreshold"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaSafetyChReleaseThreshold"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaSafetyChAllocTimer"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaSafetyChReleaseTimer"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaBinStatRepMAXPeriod"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaSafetyChaRetryTimer"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaHARQAackDelayULBurst"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaCQICHBandAMCTranaDelay"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaBsEIRP"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaChannelNumber"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaTTG"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaRTG"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaInitRngMaxRSS"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaDownlinkCenterFreq"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaBsId"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaMacVersion"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaFrameDurationCode"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaSizeCqichIdField"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaHARQAackDelayBurst"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaUcdFecCodeType"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaRangingDataRatio"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaNorCOverNOverride"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaUcdBurstProfileRowStatus"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaDownlinkFrequency"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaDcdFecCodeType"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaDiucMandatoryExitThresh"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaDiucMinEntryThresh"),
        ("WMAN-IF-MIB", "wmanIfBsOfdmaDcdBurstProfileRowStatus"))
)
if mibBuilder.loadTexts:
    wmanIfMibBsOfdmaGroup.setStatus("current")

wmanIfMibSsOfdmaGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 184, 2, 1, 9)
)
wmanIfMibSsOfdmaGroup.setObjects(
      *(("WMAN-IF-MIB", "wmanIfSsOfdmaCtBasedResvTimeout"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaBwReqOppSize"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaRangReqOppSize"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaUplinkCenterFreq"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaInitRngCodes"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaPeriodicRngCodes"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaBWReqCodes"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaPerRngBackoffStart"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaPerRngBackoffEnd"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaStartOfRngCodes"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaPermutationBase"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaULAllocSubchBitmap"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaOptPermULAllocSubchBitmap"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaBandAMCAllocThreshold"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaBandAMCReleaseThreshold"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaBandAMCAllocTimer"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaBandAMCReleaseTimer"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaBandStatRepMAXPeriod"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaBandAMCRetryTimer"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaSafetyChAllocThreshold"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaSafetyChReleaseThreshold"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaSafetyChAllocTimer"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaSafetyChReleaseTimer"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaBinStatRepMAXPeriod"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaSafetyChaRetryTimer"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaHARQAackDelayULBurst"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaCQICHBandAMCTranaDelay"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaBsEIRP"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaChannelNumber"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaTTG"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaRTG"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaInitRngMaxRSS"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaDownlinkCenterFreq"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaBsId"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaMacVersion"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaFrameDurationCode"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaSizeCqichIdField"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaHARQAackDelayBurst"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaUiucIndex"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaUcdFecCodeType"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaRangingDataRatio"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaNorCOverNOverride"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaDiucIndex"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaDownlinkFrequency"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaDcdFecCodeType"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaDiucMandatoryExitThresh"),
        ("WMAN-IF-MIB", "wmanIfSsOfdmaDiucMinEntryThresh"))
)
if mibBuilder.loadTexts:
    wmanIfMibSsOfdmaGroup.setStatus("current")

wmanIfMibCmnPhsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 184, 2, 1, 12)
)
wmanIfMibCmnPhsGroup.setObjects(
      *(("WMAN-IF-MIB", "wmanIfCmnPhsRulePhsField"),
        ("WMAN-IF-MIB", "wmanIfCmnPhsRulePhsMask"),
        ("WMAN-IF-MIB", "wmanIfCmnPhsRulePhsSize"),
        ("WMAN-IF-MIB", "wmanIfCmnPhsRulePhsVerify"))
)
if mibBuilder.loadTexts:
    wmanIfMibCmnPhsGroup.setStatus("current")

wmanIfMibBsPhsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 184, 2, 1, 13)
)
wmanIfMibBsPhsGroup.setObjects(
      *(("WMAN-IF-MIB", "wmanIfBsClassifierRulePhsSize"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRulePhsMask"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRulePhsVerify"),
        ("WMAN-IF-MIB", "wmanIfBsClassifierRuleBitMap"))
)
if mibBuilder.loadTexts:
    wmanIfMibBsPhsGroup.setStatus("current")


# Notification objects

wmanIfBsSsStatusNotificationTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2, 0, 1)
)
wmanIfBsSsStatusNotificationTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("WMAN-IF-MIB", "wmanIfBsSsNotificationMacAddr"),
        ("WMAN-IF-MIB", "wmanIfBsSsStatusValue"),
        ("WMAN-IF-MIB", "wmanIfBsSsStatusInfo"))
)
if mibBuilder.loadTexts:
    wmanIfBsSsStatusNotificationTrap.setStatus(
        "current"
    )

wmanIfBsSsDynamicServiceFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2, 0, 2)
)
wmanIfBsSsDynamicServiceFailTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("WMAN-IF-MIB", "wmanIfBsSsNotificationMacAddr"),
        ("WMAN-IF-MIB", "wmanIfBsDynamicServiceType"),
        ("WMAN-IF-MIB", "wmanIfBsDynamicServiceFailReason"))
)
if mibBuilder.loadTexts:
    wmanIfBsSsDynamicServiceFailTrap.setStatus(
        "current"
    )

wmanIfBsSsRssiStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2, 0, 3)
)
wmanIfBsSsRssiStatusChangeTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("WMAN-IF-MIB", "wmanIfBsSsNotificationMacAddr"),
        ("WMAN-IF-MIB", "wmanIfBsSsRssiStatus"),
        ("WMAN-IF-MIB", "wmanIfBsSsRssiStatusInfo"))
)
if mibBuilder.loadTexts:
    wmanIfBsSsRssiStatusChangeTrap.setStatus(
        "current"
    )

wmanIfBsSsPkmFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2, 0, 4)
)
wmanIfBsSsPkmFailTrap.setObjects(
    ("WMAN-IF-MIB", "wmanIfBsSsNotificationMacAddr")
)
if mibBuilder.loadTexts:
    wmanIfBsSsPkmFailTrap.setStatus(
        "current"
    )

wmanIfBsSsRegistrerTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2, 0, 5)
)
wmanIfBsSsRegistrerTrap.setObjects(
      *(("WMAN-IF-MIB", "wmanIfBsSsNotificationMacAddr"),
        ("WMAN-IF-MIB", "wmanIfBsSsRegisterStatus"))
)
if mibBuilder.loadTexts:
    wmanIfBsSsRegistrerTrap.setStatus(
        "current"
    )

wmanIfSsTlvUnknownTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2, 0, 1)
)
wmanIfSsTlvUnknownTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("WMAN-IF-MIB", "wmanIfSsMacAddress"),
        ("WMAN-IF-MIB", "wmanIfSsUnknownTlv"))
)
if mibBuilder.loadTexts:
    wmanIfSsTlvUnknownTrap.setStatus(
        "current"
    )

wmanIfSsDynamicServiceFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2, 0, 2)
)
wmanIfSsDynamicServiceFailTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("WMAN-IF-MIB", "wmanIfSsMacAddress"),
        ("WMAN-IF-MIB", "wmanIfSsDynamicServiceType"),
        ("WMAN-IF-MIB", "wmanIfSsDynamicServiceFailReason"))
)
if mibBuilder.loadTexts:
    wmanIfSsDynamicServiceFailTrap.setStatus(
        "current"
    )

wmanIfSsDhcpSuccessTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2, 0, 3)
)
wmanIfSsDhcpSuccessTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("WMAN-IF-MIB", "wmanIfSsMacAddress"))
)
if mibBuilder.loadTexts:
    wmanIfSsDhcpSuccessTrap.setStatus(
        "current"
    )

wmanIfSsRssiStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2, 0, 4)
)
wmanIfSsRssiStatusChangeTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("WMAN-IF-MIB", "wmanIfSsMacAddress"),
        ("WMAN-IF-MIB", "wmanIfSsRssiStatus"),
        ("WMAN-IF-MIB", "wmanIfSsRssiStatusInfo"))
)
if mibBuilder.loadTexts:
    wmanIfSsRssiStatusChangeTrap.setStatus(
        "current"
    )


# Notifications groups

wmanIfMibBsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 184, 2, 1, 10)
)
wmanIfMibBsNotificationGroup.setObjects(
      *(("WMAN-IF-MIB", "wmanIfBsSsStatusNotificationTrap"),
        ("WMAN-IF-MIB", "wmanIfBsSsDynamicServiceFailTrap"),
        ("WMAN-IF-MIB", "wmanIfBsSsRssiStatusChangeTrap"),
        ("WMAN-IF-MIB", "wmanIfBsSsPkmFailTrap"),
        ("WMAN-IF-MIB", "wmanIfBsSsRegistrerTrap"))
)
if mibBuilder.loadTexts:
    wmanIfMibBsNotificationGroup.setStatus(
        "current"
    )

wmanIfMibSsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 184, 2, 1, 11)
)
wmanIfMibSsNotificationGroup.setObjects(
      *(("WMAN-IF-MIB", "wmanIfSsTlvUnknownTrap"),
        ("WMAN-IF-MIB", "wmanIfSsDynamicServiceFailTrap"),
        ("WMAN-IF-MIB", "wmanIfSsDhcpSuccessTrap"),
        ("WMAN-IF-MIB", "wmanIfSsRssiStatusChangeTrap"))
)
if mibBuilder.loadTexts:
    wmanIfMibSsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

wmanIfMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 184, 2, 2, 1)
)
wmanIfMibCompliance.setObjects(
      *(("WMAN-IF-MIB", "wmanIfMibCommonGroup"),
        ("WMAN-IF-MIB", "wmanIfMibQoSGroup"),
        ("WMAN-IF-MIB", "wmanIfMibBsGroup"),
        ("WMAN-IF-MIB", "wmanIfMibBsAasGroup"),
        ("WMAN-IF-MIB", "wmanIfMibSsGroup"),
        ("WMAN-IF-MIB", "wmanIfMibBsOfdmGroup"),
        ("WMAN-IF-MIB", "wmanIfMibSsOfdmGroup"),
        ("WMAN-IF-MIB", "wmanIfMibBsOfdmaGroup"),
        ("WMAN-IF-MIB", "wmanIfMibSsOfdmaGroup"),
        ("WMAN-IF-MIB", "wmanIfMibBsNotificationGroup"),
        ("WMAN-IF-MIB", "wmanIfMibSsNotificationGroup"),
        ("WMAN-IF-MIB", "wmanIfMibCmnPhsGroup"),
        ("WMAN-IF-MIB", "wmanIfMibBsPhsGroup"))
)
if mibBuilder.loadTexts:
    wmanIfMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WMAN-IF-MIB",
    **{"WmanIfSfSchedulingType": WmanIfSfSchedulingType,
       "WmanIfPhsRuleVerify": WmanIfPhsRuleVerify,
       "WmanIfClassifierBitMap": WmanIfClassifierBitMap,
       "WmanIfSfState": WmanIfSfState,
       "WmanIfServClassName": WmanIfServClassName,
       "WmanIfCsSpecification": WmanIfCsSpecification,
       "WmanIfMacVersion": WmanIfMacVersion,
       "WmanIfCidType": WmanIfCidType,
       "WmanIfDataEncryptAlgId": WmanIfDataEncryptAlgId,
       "WmanIfDataAuthAlgId": WmanIfDataAuthAlgId,
       "WmanIfTekEncryptAlgId": WmanIfTekEncryptAlgId,
       "WmanIfChannelNumber": WmanIfChannelNumber,
       "WmanIfOfdmFecCodeType": WmanIfOfdmFecCodeType,
       "WmanIfOfdmaFecCodeType": WmanIfOfdmaFecCodeType,
       "WmanIfNumOfUplinkCid": WmanIfNumOfUplinkCid,
       "WmanIfArqSupportType": WmanIfArqSupportType,
       "WmanIfMaxDsxFlowType": WmanIfMaxDsxFlowType,
       "WmanIfMacCrcSupport": WmanIfMacCrcSupport,
       "WmanIfMaxMcaFlowType": WmanIfMaxMcaFlowType,
       "WmanIfMaxMcpGroupCid": WmanIfMaxMcpGroupCid,
       "WmanIfMaxPkmFlowType": WmanIfMaxPkmFlowType,
       "WmanIfAuthPolicyType": WmanIfAuthPolicyType,
       "WmanIfMaxNumOfSaType": WmanIfMaxNumOfSaType,
       "WmanIfIpVersionType": WmanIfIpVersionType,
       "WmanIfMacCsBitMap": WmanIfMacCsBitMap,
       "WmanIfMaxClassifiers": WmanIfMaxClassifiers,
       "WmanIfPhsSupportType": WmanIfPhsSupportType,
       "WmanIfBwAllocSupport": WmanIfBwAllocSupport,
       "WmanIfPduConstruction": WmanIfPduConstruction,
       "WmanIfSsTransitionGap": WmanIfSsTransitionGap,
       "WmanIfMaxTxPowerType": WmanIfMaxTxPowerType,
       "WmanIfOfdmFftSizes": WmanIfOfdmFftSizes,
       "WmanIfOfdmSsDeModType": WmanIfOfdmSsDeModType,
       "WmanIfOfdmSsModType": WmanIfOfdmSsModType,
       "WmanIfOfdmFocusedCt": WmanIfOfdmFocusedCt,
       "WmanIfOfdmTcSublayer": WmanIfOfdmTcSublayer,
       "WmanIfBsIdType": WmanIfBsIdType,
       "WmanIfIpv6FlowLabel": WmanIfIpv6FlowLabel,
       "wmanIfMib": wmanIfMib,
       "wmanIfMibObjects": wmanIfMibObjects,
       "wmanIfBsObjects": wmanIfBsObjects,
       "wmanIfBsPacketCs": wmanIfBsPacketCs,
       "wmanIfBsProvisionedSfTable": wmanIfBsProvisionedSfTable,
       "wmanIfBsProvisionedSfEntry": wmanIfBsProvisionedSfEntry,
       "wmanIfBsSfId": wmanIfBsSfId,
       "wmanIfBsSfDirection": wmanIfBsSfDirection,
       "wmanIfBsServiceClassIndex": wmanIfBsServiceClassIndex,
       "wmanIfBsSfState": wmanIfBsSfState,
       "wmanIfBsSfProvisionedTime": wmanIfBsSfProvisionedTime,
       "wmanIfBsSfCsSpecification": wmanIfBsSfCsSpecification,
       "wmanIfBsProvisionedSfRowStatus": wmanIfBsProvisionedSfRowStatus,
       "wmanIfBsSsProvisionedForSfTable": wmanIfBsSsProvisionedForSfTable,
       "wmanIfBsSsProvisionedForSfEntry": wmanIfBsSsProvisionedForSfEntry,
       "wmanIfBsSsProvMacAddress": wmanIfBsSsProvMacAddress,
       "wmanIfBsProvSfId": wmanIfBsProvSfId,
       "wmanIfBsSsProvisionedForSfRowStatus": wmanIfBsSsProvisionedForSfRowStatus,
       "wmanIfBsServiceClassTable": wmanIfBsServiceClassTable,
       "wmanIfBsServiceClassEntry": wmanIfBsServiceClassEntry,
       "wmanIfBsQoSProfileIndex": wmanIfBsQoSProfileIndex,
       "wmanIfBsQosServiceClassName": wmanIfBsQosServiceClassName,
       "wmanIfBsQoSTrafficPriority": wmanIfBsQoSTrafficPriority,
       "wmanIfBsQoSMaxSustainedRate": wmanIfBsQoSMaxSustainedRate,
       "wmanIfBsQoSMaxTrafficBurst": wmanIfBsQoSMaxTrafficBurst,
       "wmanIfBsQoSMinReservedRate": wmanIfBsQoSMinReservedRate,
       "wmanIfBsQoSToleratedJitter": wmanIfBsQoSToleratedJitter,
       "wmanIfBsQoSMaxLatency": wmanIfBsQoSMaxLatency,
       "wmanIfBsQoSFixedVsVariableSduInd": wmanIfBsQoSFixedVsVariableSduInd,
       "wmanIfBsQoSSduSize": wmanIfBsQoSSduSize,
       "wmanIfBsQosScSchedulingType": wmanIfBsQosScSchedulingType,
       "wmanIfBsQosScArqEnable": wmanIfBsQosScArqEnable,
       "wmanIfBsQosScArqWindowSize": wmanIfBsQosScArqWindowSize,
       "wmanIfBsQosScArqBlockLifetime": wmanIfBsQosScArqBlockLifetime,
       "wmanIfBsQosScArqSyncLossTimeout": wmanIfBsQosScArqSyncLossTimeout,
       "wmanIfBsQosScArqDeliverInOrder": wmanIfBsQosScArqDeliverInOrder,
       "wmanIfBsQosScArqRxPurgeTimeout": wmanIfBsQosScArqRxPurgeTimeout,
       "wmanIfBsQosScArqBlockSize": wmanIfBsQosScArqBlockSize,
       "wmanIfBsQosSCMinRsvdTolerableRate": wmanIfBsQosSCMinRsvdTolerableRate,
       "wmanIfBsQoSReqTxPolicy": wmanIfBsQoSReqTxPolicy,
       "wmanIfBsQoSServiceClassRowStatus": wmanIfBsQoSServiceClassRowStatus,
       "wmanIfBsClassifierRuleTable": wmanIfBsClassifierRuleTable,
       "wmanIfBsClassifierRuleEntry": wmanIfBsClassifierRuleEntry,
       "wmanIfBsClassifierRuleIndex": wmanIfBsClassifierRuleIndex,
       "wmanIfBsClassifierRulePriority": wmanIfBsClassifierRulePriority,
       "wmanIfBsClassifierRuleIpTosLow": wmanIfBsClassifierRuleIpTosLow,
       "wmanIfBsClassifierRuleIpTosHigh": wmanIfBsClassifierRuleIpTosHigh,
       "wmanIfBsClassifierRuleIpTosMask": wmanIfBsClassifierRuleIpTosMask,
       "wmanIfBsClassifierRuleIpProtocol": wmanIfBsClassifierRuleIpProtocol,
       "wmanIfBsClassifierRuleIpSourceAddr": wmanIfBsClassifierRuleIpSourceAddr,
       "wmanIfBsClassifierRuleIpSourceMask": wmanIfBsClassifierRuleIpSourceMask,
       "wmanIfBsClassifierRuleIpDestAddr": wmanIfBsClassifierRuleIpDestAddr,
       "wmanIfBsClassifierRuleIpDestMask": wmanIfBsClassifierRuleIpDestMask,
       "wmanIfBsClassifierRuleSourcePortStart": wmanIfBsClassifierRuleSourcePortStart,
       "wmanIfBsClassifierRuleSourcePortEnd": wmanIfBsClassifierRuleSourcePortEnd,
       "wmanIfBsClassifierRuleDestPortStart": wmanIfBsClassifierRuleDestPortStart,
       "wmanIfBsClassifierRuleDestPortEnd": wmanIfBsClassifierRuleDestPortEnd,
       "wmanIfBsClassifierRuleDestMacAddr": wmanIfBsClassifierRuleDestMacAddr,
       "wmanIfBsClassifierRuleDestMacMask": wmanIfBsClassifierRuleDestMacMask,
       "wmanIfBsClassifierRuleSourceMacAddr": wmanIfBsClassifierRuleSourceMacAddr,
       "wmanIfBsClassifierRuleSourceMacMask": wmanIfBsClassifierRuleSourceMacMask,
       "wmanIfBsClassifierRuleEnetProtocolType": wmanIfBsClassifierRuleEnetProtocolType,
       "wmanIfBsClassifierRuleEnetProtocol": wmanIfBsClassifierRuleEnetProtocol,
       "wmanIfBsClassifierRuleUserPriLow": wmanIfBsClassifierRuleUserPriLow,
       "wmanIfBsClassifierRuleUserPriHigh": wmanIfBsClassifierRuleUserPriHigh,
       "wmanIfBsClassifierRuleVlanId": wmanIfBsClassifierRuleVlanId,
       "wmanIfBsClassifierRuleState": wmanIfBsClassifierRuleState,
       "wmanIfBsClassifierRulePhsSize": wmanIfBsClassifierRulePhsSize,
       "wmanIfBsClassifierRulePhsMask": wmanIfBsClassifierRulePhsMask,
       "wmanIfBsClassifierRulePhsVerify": wmanIfBsClassifierRulePhsVerify,
       "wmanIfBsClassifierRuleIpv6FlowLabel": wmanIfBsClassifierRuleIpv6FlowLabel,
       "wmanIfBsClassifierRuleBitMap": wmanIfBsClassifierRuleBitMap,
       "wmanIfBsClassifierRuleRowStatus": wmanIfBsClassifierRuleRowStatus,
       "wmanIfBsSsPacketCounterTable": wmanIfBsSsPacketCounterTable,
       "wmanIfBsSsPacketCounterEntry": wmanIfBsSsPacketCounterEntry,
       "wmanIfBsSsMacSduCount": wmanIfBsSsMacSduCount,
       "wmanIfBsSsOctetCount": wmanIfBsSsOctetCount,
       "wmanIfBsSsResetCounter": wmanIfBsSsResetCounter,
       "wmanIfBsSsResetCounterTime": wmanIfBsSsResetCounterTime,
       "wmanIfBsCps": wmanIfBsCps,
       "wmanIfBsRegisteredSsTable": wmanIfBsRegisteredSsTable,
       "wmanIfBsRegisteredSsEntry": wmanIfBsRegisteredSsEntry,
       "wmanIfBsSsMacAddress": wmanIfBsSsMacAddress,
       "wmanIfBsSsBasicCid": wmanIfBsSsBasicCid,
       "wmanIfBsSsPrimaryCid": wmanIfBsSsPrimaryCid,
       "wmanIfBsSsSecondaryCid": wmanIfBsSsSecondaryCid,
       "wmanIfBsSsManagementSupport": wmanIfBsSsManagementSupport,
       "wmanIfBsSsIpManagementMode": wmanIfBsSsIpManagementMode,
       "wmanIfBsSs2ndMgmtArqEnable": wmanIfBsSs2ndMgmtArqEnable,
       "wmanIfBsSs2ndMgmtArqWindowSize": wmanIfBsSs2ndMgmtArqWindowSize,
       "wmanIfBsSs2ndMgmtArqDnLinkTxDelay": wmanIfBsSs2ndMgmtArqDnLinkTxDelay,
       "wmanIfBsSs2ndMgmtArqUpLinkTxDelay": wmanIfBsSs2ndMgmtArqUpLinkTxDelay,
       "wmanIfBsSs2ndMgmtArqDnLinkRxDelay": wmanIfBsSs2ndMgmtArqDnLinkRxDelay,
       "wmanIfBsSs2ndMgmtArqUpLinkRxDelay": wmanIfBsSs2ndMgmtArqUpLinkRxDelay,
       "wmanIfBsSs2ndMgmtArqBlockLifetime": wmanIfBsSs2ndMgmtArqBlockLifetime,
       "wmanIfBsSs2ndMgmtArqSyncLossTimeout": wmanIfBsSs2ndMgmtArqSyncLossTimeout,
       "wmanIfBsSs2ndMgmtArqDeliverInOrder": wmanIfBsSs2ndMgmtArqDeliverInOrder,
       "wmanIfBsSs2ndMgmtArqRxPurgeTimeout": wmanIfBsSs2ndMgmtArqRxPurgeTimeout,
       "wmanIfBsSs2ndMgmtArqBlockSize": wmanIfBsSs2ndMgmtArqBlockSize,
       "wmanIfBsSsVendorIdEncoding": wmanIfBsSsVendorIdEncoding,
       "wmanIfBsSsAasBroadcastPermission": wmanIfBsSsAasBroadcastPermission,
       "wmanIfBsSsMaxTxPowerBpsk": wmanIfBsSsMaxTxPowerBpsk,
       "wmanIfBsSsMaxTxPowerQpsk": wmanIfBsSsMaxTxPowerQpsk,
       "wmanIfBsSsMaxTxPower16Qam": wmanIfBsSsMaxTxPower16Qam,
       "wmanIfBsSsMaxTxPower64Qam": wmanIfBsSsMaxTxPower64Qam,
       "wmanIfBsSsMacVersion": wmanIfBsSsMacVersion,
       "wmanIfBsConfigurationTable": wmanIfBsConfigurationTable,
       "wmanIfBsConfigurationEntry": wmanIfBsConfigurationEntry,
       "wmanIfBsDcdInterval": wmanIfBsDcdInterval,
       "wmanIfBsUcdInterval": wmanIfBsUcdInterval,
       "wmanIfBsUcdTransition": wmanIfBsUcdTransition,
       "wmanIfBsDcdTransition": wmanIfBsDcdTransition,
       "wmanIfBsInitialRangingInterval": wmanIfBsInitialRangingInterval,
       "wmanIfBsSsULMapProcTime": wmanIfBsSsULMapProcTime,
       "wmanIfBsSsRangRespProcTime": wmanIfBsSsRangRespProcTime,
       "wmanIfBsT5Timeout": wmanIfBsT5Timeout,
       "wmanIfBsT9Timeout": wmanIfBsT9Timeout,
       "wmanIfBsT13Timeout": wmanIfBsT13Timeout,
       "wmanIfBsT15Timeout": wmanIfBsT15Timeout,
       "wmanIfBsT17Timeout": wmanIfBsT17Timeout,
       "wmanIfBsT27IdleTimer": wmanIfBsT27IdleTimer,
       "wmanIfBsT27ActiveTimer": wmanIfBsT27ActiveTimer,
       "wmanIfBs2ndMgmtDlQoSProfileIndex": wmanIfBs2ndMgmtDlQoSProfileIndex,
       "wmanIfBs2ndMgmtUlQoSProfileIndex": wmanIfBs2ndMgmtUlQoSProfileIndex,
       "wmanIfBsAutoSfidEnabled": wmanIfBsAutoSfidEnabled,
       "wmanIfBsAutoSfidRangeMin": wmanIfBsAutoSfidRangeMin,
       "wmanIfBsAutoSfidRangeMax": wmanIfBsAutoSfidRangeMax,
       "wmanIfBsAasChanFbckReqFreq": wmanIfBsAasChanFbckReqFreq,
       "wmanIfBsAasBeamSelectFreq": wmanIfBsAasBeamSelectFreq,
       "wmanIfBsAasChanFbckReqResolution": wmanIfBsAasChanFbckReqResolution,
       "wmanIfBsAasBeamReqResolution": wmanIfBsAasBeamReqResolution,
       "wmanIfBsAasNumOptDiversityZones": wmanIfBsAasNumOptDiversityZones,
       "wmanIfBsResetSector": wmanIfBsResetSector,
       "wmanIfBsChannelMeasurementTable": wmanIfBsChannelMeasurementTable,
       "wmanIfBsChannelMeasurementEntry": wmanIfBsChannelMeasurementEntry,
       "wmanIfBsChannelDirection": wmanIfBsChannelDirection,
       "wmanIfBsHistogramIndex": wmanIfBsHistogramIndex,
       "wmanIfBsChannelNumber": wmanIfBsChannelNumber,
       "wmanIfBsStartFrame": wmanIfBsStartFrame,
       "wmanIfBsDuration": wmanIfBsDuration,
       "wmanIfBsBasicReport": wmanIfBsBasicReport,
       "wmanIfBsMeanCinrReport": wmanIfBsMeanCinrReport,
       "wmanIfBsMeanRssiReport": wmanIfBsMeanRssiReport,
       "wmanIfBsStdDeviationCinrReport": wmanIfBsStdDeviationCinrReport,
       "wmanIfBsStdDeviationRssiReport": wmanIfBsStdDeviationRssiReport,
       "wmanIfBsCapabilities": wmanIfBsCapabilities,
       "wmanIfBsSsReqCapabilitiesTable": wmanIfBsSsReqCapabilitiesTable,
       "wmanIfBsSsReqCapabilitiesEntry": wmanIfBsSsReqCapabilitiesEntry,
       "wmanIfBsSsReqCapUplinkCidSupport": wmanIfBsSsReqCapUplinkCidSupport,
       "wmanIfBsSsReqCapArqSupport": wmanIfBsSsReqCapArqSupport,
       "wmanIfBsSsReqCapDsxFlowControl": wmanIfBsSsReqCapDsxFlowControl,
       "wmanIfBsSsReqCapMacCrcSupport": wmanIfBsSsReqCapMacCrcSupport,
       "wmanIfBsSsReqCapMcaFlowControl": wmanIfBsSsReqCapMcaFlowControl,
       "wmanIfBsSsReqCapMcpGroupCidSupport": wmanIfBsSsReqCapMcpGroupCidSupport,
       "wmanIfBsSsReqCapPkmFlowControl": wmanIfBsSsReqCapPkmFlowControl,
       "wmanIfBsSsReqCapAuthPolicyControl": wmanIfBsSsReqCapAuthPolicyControl,
       "wmanIfBsSsReqCapMaxNumOfSupportedSA": wmanIfBsSsReqCapMaxNumOfSupportedSA,
       "wmanIfBsSsReqCapIpVersion": wmanIfBsSsReqCapIpVersion,
       "wmanIfBsSsReqCapMacCsSupportBitMap": wmanIfBsSsReqCapMacCsSupportBitMap,
       "wmanIfBsSsReqCapMaxNumOfClassifier": wmanIfBsSsReqCapMaxNumOfClassifier,
       "wmanIfBsSsReqCapPhsSupport": wmanIfBsSsReqCapPhsSupport,
       "wmanIfBsSsReqCapBandwidthAllocSupport": wmanIfBsSsReqCapBandwidthAllocSupport,
       "wmanIfBsSsReqCapPduConstruction": wmanIfBsSsReqCapPduConstruction,
       "wmanIfBsSsReqCapTtgTransitionGap": wmanIfBsSsReqCapTtgTransitionGap,
       "wmanIfBsSsReqCapRtgTransitionGap": wmanIfBsSsReqCapRtgTransitionGap,
       "wmanIfBsSsRspCapabilitiesTable": wmanIfBsSsRspCapabilitiesTable,
       "wmanIfBsSsRspCapabilitiesEntry": wmanIfBsSsRspCapabilitiesEntry,
       "wmanIfBsSsRspCapUplinkCidSupport": wmanIfBsSsRspCapUplinkCidSupport,
       "wmanIfBsSsRspCapArqSupport": wmanIfBsSsRspCapArqSupport,
       "wmanIfBsSsRspCapDsxFlowControl": wmanIfBsSsRspCapDsxFlowControl,
       "wmanIfBsSsRspCapMacCrcSupport": wmanIfBsSsRspCapMacCrcSupport,
       "wmanIfBsSsRspCapMcaFlowControl": wmanIfBsSsRspCapMcaFlowControl,
       "wmanIfBsSsRspCapMcpGroupCidSupport": wmanIfBsSsRspCapMcpGroupCidSupport,
       "wmanIfBsSsRspCapPkmFlowControl": wmanIfBsSsRspCapPkmFlowControl,
       "wmanIfBsSsRspCapAuthPolicyControl": wmanIfBsSsRspCapAuthPolicyControl,
       "wmanIfBsSsRspCapMaxNumOfSupportedSA": wmanIfBsSsRspCapMaxNumOfSupportedSA,
       "wmanIfBsSsRspCapIpVersion": wmanIfBsSsRspCapIpVersion,
       "wmanIfBsSsRspCapMacCsSupportBitMap": wmanIfBsSsRspCapMacCsSupportBitMap,
       "wmanIfBsSsRspCapMaxNumOfClassifier": wmanIfBsSsRspCapMaxNumOfClassifier,
       "wmanIfBsSsRspCapPhsSupport": wmanIfBsSsRspCapPhsSupport,
       "wmanIfBsSsRspCapBandwidthAllocSupport": wmanIfBsSsRspCapBandwidthAllocSupport,
       "wmanIfBsSsRspCapPduConstruction": wmanIfBsSsRspCapPduConstruction,
       "wmanIfBsSsRspCapTtgTransitionGap": wmanIfBsSsRspCapTtgTransitionGap,
       "wmanIfBsSsRspCapRtgTransitionGap": wmanIfBsSsRspCapRtgTransitionGap,
       "wmanIfBsBasicCapabilitiesTable": wmanIfBsBasicCapabilitiesTable,
       "wmanIfBsBasicCapabilitiesEntry": wmanIfBsBasicCapabilitiesEntry,
       "wmanIfBsCapUplinkCidSupport": wmanIfBsCapUplinkCidSupport,
       "wmanIfBsCapArqSupport": wmanIfBsCapArqSupport,
       "wmanIfBsCapDsxFlowControl": wmanIfBsCapDsxFlowControl,
       "wmanIfBsCapMacCrcSupport": wmanIfBsCapMacCrcSupport,
       "wmanIfBsCapMcaFlowControl": wmanIfBsCapMcaFlowControl,
       "wmanIfBsCapMcpGroupCidSupport": wmanIfBsCapMcpGroupCidSupport,
       "wmanIfBsCapPkmFlowControl": wmanIfBsCapPkmFlowControl,
       "wmanIfBsCapAuthPolicyControl": wmanIfBsCapAuthPolicyControl,
       "wmanIfBsCapMaxNumOfSupportedSA": wmanIfBsCapMaxNumOfSupportedSA,
       "wmanIfBsCapIpVersion": wmanIfBsCapIpVersion,
       "wmanIfBsCapMacCsSupportBitMap": wmanIfBsCapMacCsSupportBitMap,
       "wmanIfBsCapMaxNumOfClassifier": wmanIfBsCapMaxNumOfClassifier,
       "wmanIfBsCapPhsSupport": wmanIfBsCapPhsSupport,
       "wmanIfBsCapBandwidthAllocSupport": wmanIfBsCapBandwidthAllocSupport,
       "wmanIfBsCapPduConstruction": wmanIfBsCapPduConstruction,
       "wmanIfBsCapTtgTransitionGap": wmanIfBsCapTtgTransitionGap,
       "wmanIfBsCapRtgTransitionGap": wmanIfBsCapRtgTransitionGap,
       "wmanIfBsCapabilitiesConfigTable": wmanIfBsCapabilitiesConfigTable,
       "wmanIfBsCapabilitiesConfigEntry": wmanIfBsCapabilitiesConfigEntry,
       "wmanIfBsCapCfgUplinkCidSupport": wmanIfBsCapCfgUplinkCidSupport,
       "wmanIfBsCapCfgArqSupport": wmanIfBsCapCfgArqSupport,
       "wmanIfBsCapCfgDsxFlowControl": wmanIfBsCapCfgDsxFlowControl,
       "wmanIfBsCapCfgMacCrcSupport": wmanIfBsCapCfgMacCrcSupport,
       "wmanIfBsCapCfgMcaFlowControl": wmanIfBsCapCfgMcaFlowControl,
       "wmanIfBsCapCfgMcpGroupCidSupport": wmanIfBsCapCfgMcpGroupCidSupport,
       "wmanIfBsCapCfgPkmFlowControl": wmanIfBsCapCfgPkmFlowControl,
       "wmanIfBsCapCfgAuthPolicyControl": wmanIfBsCapCfgAuthPolicyControl,
       "wmanIfBsCapCfgMaxNumOfSupportedSA": wmanIfBsCapCfgMaxNumOfSupportedSA,
       "wmanIfBsCapCfgIpVersion": wmanIfBsCapCfgIpVersion,
       "wmanIfBsCapCfgMacCsSupportBitMap": wmanIfBsCapCfgMacCsSupportBitMap,
       "wmanIfBsCapCfgMaxNumOfClassifier": wmanIfBsCapCfgMaxNumOfClassifier,
       "wmanIfBsCapCfgPhsSupport": wmanIfBsCapCfgPhsSupport,
       "wmanIfBsCapCfgBandwidthAllocSupport": wmanIfBsCapCfgBandwidthAllocSupport,
       "wmanIfBsCapCfgPduConstruction": wmanIfBsCapCfgPduConstruction,
       "wmanIfBsCapCfgTtgTransitionGap": wmanIfBsCapCfgTtgTransitionGap,
       "wmanIfBsCapCfgRtgTransitionGap": wmanIfBsCapCfgRtgTransitionGap,
       "wmanIfBsSsActionsTable": wmanIfBsSsActionsTable,
       "wmanIfBsSsActionsEntry": wmanIfBsSsActionsEntry,
       "wmanIfBsSsActionsMacAddress": wmanIfBsSsActionsMacAddress,
       "wmanIfBsSsActionsResetSs": wmanIfBsSsActionsResetSs,
       "wmanIfBsSsActionsAbortSs": wmanIfBsSsActionsAbortSs,
       "wmanIfBsSsActionsOverrideDnFreq": wmanIfBsSsActionsOverrideDnFreq,
       "wmanIfBsSsActionsOverrideChannelId": wmanIfBsSsActionsOverrideChannelId,
       "wmanIfBsSsActionsDeReRegSs": wmanIfBsSsActionsDeReRegSs,
       "wmanIfBsSsActionsDeReRegSsCode": wmanIfBsSsActionsDeReRegSsCode,
       "wmanIfBsSsActionsRowStatus": wmanIfBsSsActionsRowStatus,
       "wmanIfBsPkmObjects": wmanIfBsPkmObjects,
       "wmanIfBsPkmBaseTable": wmanIfBsPkmBaseTable,
       "wmanIfBsPkmBaseEntry": wmanIfBsPkmBaseEntry,
       "wmanIfBsPkmDefaultAuthLifetime": wmanIfBsPkmDefaultAuthLifetime,
       "wmanIfBsPkmDefaultTekLifetime": wmanIfBsPkmDefaultTekLifetime,
       "wmanIfBsPkmDefaultSelfSigManufCertTrust": wmanIfBsPkmDefaultSelfSigManufCertTrust,
       "wmanIfBsPkmCheckCertValidityPeriods": wmanIfBsPkmCheckCertValidityPeriods,
       "wmanIfBsPkmAuthentInfos": wmanIfBsPkmAuthentInfos,
       "wmanIfBsPkmAuthRequests": wmanIfBsPkmAuthRequests,
       "wmanIfBsPkmAuthReplies": wmanIfBsPkmAuthReplies,
       "wmanIfBsPkmAuthRejects": wmanIfBsPkmAuthRejects,
       "wmanIfBsPkmAuthInvalids": wmanIfBsPkmAuthInvalids,
       "wmanIfBsSsPkmAuthTable": wmanIfBsSsPkmAuthTable,
       "wmanIfBsSsPkmAuthEntry": wmanIfBsSsPkmAuthEntry,
       "wmanIfBsSsPkmAuthMacAddress": wmanIfBsSsPkmAuthMacAddress,
       "wmanIfBsSsPkmAuthKeySequenceNumber": wmanIfBsSsPkmAuthKeySequenceNumber,
       "wmanIfBsSsPkmAuthExpiresOld": wmanIfBsSsPkmAuthExpiresOld,
       "wmanIfBsSsPkmAuthExpiresNew": wmanIfBsSsPkmAuthExpiresNew,
       "wmanIfBsSsPkmAuthLifetime": wmanIfBsSsPkmAuthLifetime,
       "wmanIfBsSsPkmAuthReset": wmanIfBsSsPkmAuthReset,
       "wmanIfBsSsPkmAuthInfos": wmanIfBsSsPkmAuthInfos,
       "wmanIfBsSsPkmAuthRequests": wmanIfBsSsPkmAuthRequests,
       "wmanIfBsSsPkmAuthReplies": wmanIfBsSsPkmAuthReplies,
       "wmanIfBsSsPkmAuthRejects": wmanIfBsSsPkmAuthRejects,
       "wmanIfBsSsPkmAuthInvalids": wmanIfBsSsPkmAuthInvalids,
       "wmanIfBsSsPkmAuthRejectErrorCode": wmanIfBsSsPkmAuthRejectErrorCode,
       "wmanIfBsSsPkmAuthRejectErrorString": wmanIfBsSsPkmAuthRejectErrorString,
       "wmanIfBsSsPkmAuthInvalidErrorCode": wmanIfBsSsPkmAuthInvalidErrorCode,
       "wmanIfBsSsPkmAuthInvalidErrorString": wmanIfBsSsPkmAuthInvalidErrorString,
       "wmanIfBsSsPkmAuthPrimarySAId": wmanIfBsSsPkmAuthPrimarySAId,
       "wmanIfBsSsPkmAuthValidStatus": wmanIfBsSsPkmAuthValidStatus,
       "wmanIfBsPkmTekTable": wmanIfBsPkmTekTable,
       "wmanIfBsPkmTekEntry": wmanIfBsPkmTekEntry,
       "wmanIfBsPkmTekSAId": wmanIfBsPkmTekSAId,
       "wmanIfBsPkmTekSAType": wmanIfBsPkmTekSAType,
       "wmanIfBsPkmTekDataEncryptAlg": wmanIfBsPkmTekDataEncryptAlg,
       "wmanIfBsPkmTekDataAuthentAlg": wmanIfBsPkmTekDataAuthentAlg,
       "wmanIfBsPkmTekEncryptAlg": wmanIfBsPkmTekEncryptAlg,
       "wmanIfBsPkmTekLifetime": wmanIfBsPkmTekLifetime,
       "wmanIfBsPkmTekKeySequenceNumber": wmanIfBsPkmTekKeySequenceNumber,
       "wmanIfBsPkmTekExpiresOld": wmanIfBsPkmTekExpiresOld,
       "wmanIfBsPkmTekExpiresNew": wmanIfBsPkmTekExpiresNew,
       "wmanIfBsPkmTekReset": wmanIfBsPkmTekReset,
       "wmanIfBsPkmKeyRequests": wmanIfBsPkmKeyRequests,
       "wmanIfBsPkmKeyReplies": wmanIfBsPkmKeyReplies,
       "wmanIfBsPkmKeyRejects": wmanIfBsPkmKeyRejects,
       "wmanIfBsPkmTekInvalids": wmanIfBsPkmTekInvalids,
       "wmanIfBsPkmKeyRejectErrorCode": wmanIfBsPkmKeyRejectErrorCode,
       "wmanIfBsPkmKeyRejectErrorString": wmanIfBsPkmKeyRejectErrorString,
       "wmanIfBsPkmTekInvalidErrorCode": wmanIfBsPkmTekInvalidErrorCode,
       "wmanIfBsPkmTekInvalidErrorString": wmanIfBsPkmTekInvalidErrorString,
       "wmanIfBsNotification": wmanIfBsNotification,
       "wmanIfBsTrapControl": wmanIfBsTrapControl,
       "wmanIfBsTrapControlRegister": wmanIfBsTrapControlRegister,
       "wmanIfBsStatusTrapControlRegister": wmanIfBsStatusTrapControlRegister,
       "wmanIfBsThresholdConfigTable": wmanIfBsThresholdConfigTable,
       "wmanIfBsThresholdConfigEntry": wmanIfBsThresholdConfigEntry,
       "wmanIfBsRssiLowThreshold": wmanIfBsRssiLowThreshold,
       "wmanIfBsRssiHighThreshold": wmanIfBsRssiHighThreshold,
       "wmanIfBsTrapDefinitions": wmanIfBsTrapDefinitions,
       "wmanIfBsTrapPrefix": wmanIfBsTrapPrefix,
       "wmanIfBsSsStatusNotificationTrap": wmanIfBsSsStatusNotificationTrap,
       "wmanIfBsSsDynamicServiceFailTrap": wmanIfBsSsDynamicServiceFailTrap,
       "wmanIfBsSsRssiStatusChangeTrap": wmanIfBsSsRssiStatusChangeTrap,
       "wmanIfBsSsPkmFailTrap": wmanIfBsSsPkmFailTrap,
       "wmanIfBsSsRegistrerTrap": wmanIfBsSsRegistrerTrap,
       "wmanIfBsSsNotificationObjectsTable": wmanIfBsSsNotificationObjectsTable,
       "wmanIfBsSsNotificationObjectsEntry": wmanIfBsSsNotificationObjectsEntry,
       "wmanIfBsSsNotificationMacAddr": wmanIfBsSsNotificationMacAddr,
       "wmanIfBsSsStatusValue": wmanIfBsSsStatusValue,
       "wmanIfBsSsStatusInfo": wmanIfBsSsStatusInfo,
       "wmanIfBsDynamicServiceType": wmanIfBsDynamicServiceType,
       "wmanIfBsDynamicServiceFailReason": wmanIfBsDynamicServiceFailReason,
       "wmanIfBsSsRssiStatus": wmanIfBsSsRssiStatus,
       "wmanIfBsSsRssiStatusInfo": wmanIfBsSsRssiStatusInfo,
       "wmanIfBsSsRegisterStatus": wmanIfBsSsRegisterStatus,
       "wmanIfBsPhy": wmanIfBsPhy,
       "wmanIfBsOfdmPhy": wmanIfBsOfdmPhy,
       "wmanIfBsOfdmUplinkChannelTable": wmanIfBsOfdmUplinkChannelTable,
       "wmanIfBsOfdmUplinkChannelEntry": wmanIfBsOfdmUplinkChannelEntry,
       "wmanIfBsOfdmCtBasedResvTimeout": wmanIfBsOfdmCtBasedResvTimeout,
       "wmanIfBsOfdmBwReqOppSize": wmanIfBsOfdmBwReqOppSize,
       "wmanIfBsOfdmRangReqOppSize": wmanIfBsOfdmRangReqOppSize,
       "wmanIfBsOfdmUplinkCenterFreq": wmanIfBsOfdmUplinkCenterFreq,
       "wmanIfBsOfdmNumSubChReqRegionFull": wmanIfBsOfdmNumSubChReqRegionFull,
       "wmanIfBsOfdmNumSymbolsReqRegionFull": wmanIfBsOfdmNumSymbolsReqRegionFull,
       "wmanIfBsOfdmSubChFocusCtCode": wmanIfBsOfdmSubChFocusCtCode,
       "wmanIfBsOfdmUpLinkChannelId": wmanIfBsOfdmUpLinkChannelId,
       "wmanIfBsOfdmDownlinkChannelTable": wmanIfBsOfdmDownlinkChannelTable,
       "wmanIfBsOfdmDownlinkChannelEntry": wmanIfBsOfdmDownlinkChannelEntry,
       "wmanIfBsOfdmBsEIRP": wmanIfBsOfdmBsEIRP,
       "wmanIfBsOfdmChannelNumber": wmanIfBsOfdmChannelNumber,
       "wmanIfBsOfdmTTG": wmanIfBsOfdmTTG,
       "wmanIfBsOfdmRTG": wmanIfBsOfdmRTG,
       "wmanIfBsOfdmInitRngMaxRSS": wmanIfBsOfdmInitRngMaxRSS,
       "wmanIfBsOfdmDownlinkCenterFreq": wmanIfBsOfdmDownlinkCenterFreq,
       "wmanIfBsOfdmBsId": wmanIfBsOfdmBsId,
       "wmanIfBsOfdmMacVersion": wmanIfBsOfdmMacVersion,
       "wmanIfBsOfdmFrameDurationCode": wmanIfBsOfdmFrameDurationCode,
       "wmanIfBsOfdmDownLinkChannelId": wmanIfBsOfdmDownLinkChannelId,
       "wmanIfBsOfdmUcdBurstProfileTable": wmanIfBsOfdmUcdBurstProfileTable,
       "wmanIfBsOfdmUcdBurstProfileEntry": wmanIfBsOfdmUcdBurstProfileEntry,
       "wmanIfBsOfdmUiucIndex": wmanIfBsOfdmUiucIndex,
       "wmanIfBsOfdmUcdFecCodeType": wmanIfBsOfdmUcdFecCodeType,
       "wmanIfBsOfdmFocusCtPowerBoost": wmanIfBsOfdmFocusCtPowerBoost,
       "wmanIfBsOfdmUcdTcsEnable": wmanIfBsOfdmUcdTcsEnable,
       "wmanIfBsOfdmUcdBurstProfileRowStatus": wmanIfBsOfdmUcdBurstProfileRowStatus,
       "wmanIfBsOfdmDcdBurstProfileTable": wmanIfBsOfdmDcdBurstProfileTable,
       "wmanIfBsOfdmDcdBurstProfileEntry": wmanIfBsOfdmDcdBurstProfileEntry,
       "wmanIfBsOfdmDiucIndex": wmanIfBsOfdmDiucIndex,
       "wmanIfBsOfdmDownlinkFrequency": wmanIfBsOfdmDownlinkFrequency,
       "wmanIfBsOfdmDcdFecCodeType": wmanIfBsOfdmDcdFecCodeType,
       "wmanIfBsOfdmDiucMandatoryExitThresh": wmanIfBsOfdmDiucMandatoryExitThresh,
       "wmanIfBsOfdmDiucMinEntryThresh": wmanIfBsOfdmDiucMinEntryThresh,
       "wmanIfBsOfdmTcsEnable": wmanIfBsOfdmTcsEnable,
       "wmanIfBsOfdmDcdBurstProfileRowStatus": wmanIfBsOfdmDcdBurstProfileRowStatus,
       "wmanIfBsOfdmConfigurationTable": wmanIfBsOfdmConfigurationTable,
       "wmanIfBsOfdmConfigurationEntry": wmanIfBsOfdmConfigurationEntry,
       "wmanIfBsOfdmMinReqRegionFullTxOpp": wmanIfBsOfdmMinReqRegionFullTxOpp,
       "wmanIfBsOfdmMinFocusedCtTxOpp": wmanIfBsOfdmMinFocusedCtTxOpp,
       "wmanIfBsOfdmMaxRoundTripDelay": wmanIfBsOfdmMaxRoundTripDelay,
       "wmanIfBsOfdmRangeAbortTimingThold": wmanIfBsOfdmRangeAbortTimingThold,
       "wmanIfBsOfdmRangeAbortPowerThold": wmanIfBsOfdmRangeAbortPowerThold,
       "wmanIfBsOfdmRangeAbortFreqThold": wmanIfBsOfdmRangeAbortFreqThold,
       "wmanIfBsOfdmDnlkRateId": wmanIfBsOfdmDnlkRateId,
       "wmanIfBsOfdmRatioG": wmanIfBsOfdmRatioG,
       "wmanIfBsSsOfdmReqCapabilitiesTable": wmanIfBsSsOfdmReqCapabilitiesTable,
       "wmanIfBsSsOfdmReqCapabilitiesEntry": wmanIfBsSsOfdmReqCapabilitiesEntry,
       "wmanIfBsSsOfdmReqCapFftSizes": wmanIfBsSsOfdmReqCapFftSizes,
       "wmanIfBsSsOfdmReqCapSsDemodulator": wmanIfBsSsOfdmReqCapSsDemodulator,
       "wmanIfBsSsOfdmReqCapSsModulator": wmanIfBsSsOfdmReqCapSsModulator,
       "wmanIfBsSsOfdmReqCapFocusedCtSupport": wmanIfBsSsOfdmReqCapFocusedCtSupport,
       "wmanIfBsSsOfdmReqCapTcSublayerSupport": wmanIfBsSsOfdmReqCapTcSublayerSupport,
       "wmanIfBsSsOfdmRspCapabilitiesTable": wmanIfBsSsOfdmRspCapabilitiesTable,
       "wmanIfBsSsOfdmRspCapabilitiesEntry": wmanIfBsSsOfdmRspCapabilitiesEntry,
       "wmanIfBsSsOfdmRspCapFftSizes": wmanIfBsSsOfdmRspCapFftSizes,
       "wmanIfBsSsOfdmRspCapSsDemodulator": wmanIfBsSsOfdmRspCapSsDemodulator,
       "wmanIfBsSsOfdmRspCapSsModulator": wmanIfBsSsOfdmRspCapSsModulator,
       "wmanIfBsSsOfdmRspCapFocusedCtSupport": wmanIfBsSsOfdmRspCapFocusedCtSupport,
       "wmanIfBsSsOfdmRspCapTcSublayerSupport": wmanIfBsSsOfdmRspCapTcSublayerSupport,
       "wmanIfBsOfdmCapabilitiesTable": wmanIfBsOfdmCapabilitiesTable,
       "wmanIfBsOfdmCapabilitiesEntry": wmanIfBsOfdmCapabilitiesEntry,
       "wmanIfBsOfdmCapFftSizes": wmanIfBsOfdmCapFftSizes,
       "wmanIfBsOfdmCapSsDemodulator": wmanIfBsOfdmCapSsDemodulator,
       "wmanIfBsOfdmCapSsModulator": wmanIfBsOfdmCapSsModulator,
       "wmanIfBsOfdmCapFocusedCtSupport": wmanIfBsOfdmCapFocusedCtSupport,
       "wmanIfBsOfdmCapTcSublayerSupport": wmanIfBsOfdmCapTcSublayerSupport,
       "wmanIfBsOfdmCapabilitiesConfigTable": wmanIfBsOfdmCapabilitiesConfigTable,
       "wmanIfBsOfdmCapabilitiesConfigEntry": wmanIfBsOfdmCapabilitiesConfigEntry,
       "wmanIfBsOfdmCapCfgFftSizes": wmanIfBsOfdmCapCfgFftSizes,
       "wmanIfBsOfdmCapCfgSsDemodulator": wmanIfBsOfdmCapCfgSsDemodulator,
       "wmanIfBsOfdmCapCfgSsModulator": wmanIfBsOfdmCapCfgSsModulator,
       "wmanIfBsOfdmCapCfgFocusedCtSupport": wmanIfBsOfdmCapCfgFocusedCtSupport,
       "wmanIfBsOfdmCapCfgTcSublayerSupport": wmanIfBsOfdmCapCfgTcSublayerSupport,
       "wmanIfBsOfdmaPhy": wmanIfBsOfdmaPhy,
       "wmanIfBsOfdmaUplinkChannelTable": wmanIfBsOfdmaUplinkChannelTable,
       "wmanIfBsOfdmaUplinkChannelEntry": wmanIfBsOfdmaUplinkChannelEntry,
       "wmanIfBsOfdmaCtBasedResvTimeout": wmanIfBsOfdmaCtBasedResvTimeout,
       "wmanIfBsOfdmaBwReqOppSize": wmanIfBsOfdmaBwReqOppSize,
       "wmanIfBsOfdmaRangReqOppSize": wmanIfBsOfdmaRangReqOppSize,
       "wmanIfBsOfdmaUplinkCenterFreq": wmanIfBsOfdmaUplinkCenterFreq,
       "wmanIfBsOfdmaInitRngCodes": wmanIfBsOfdmaInitRngCodes,
       "wmanIfBsOfdmaPeriodicRngCodes": wmanIfBsOfdmaPeriodicRngCodes,
       "wmanIfBsOfdmaBWReqCodes": wmanIfBsOfdmaBWReqCodes,
       "wmanIfBsOfdmaPerRngBackoffStart": wmanIfBsOfdmaPerRngBackoffStart,
       "wmanIfBsOfdmaPerRngBackoffEnd": wmanIfBsOfdmaPerRngBackoffEnd,
       "wmanIfBsOfdmaStartOfRngCodes": wmanIfBsOfdmaStartOfRngCodes,
       "wmanIfBsOfdmaPermutationBase": wmanIfBsOfdmaPermutationBase,
       "wmanIfBsOfdmaULAllocSubchBitmap": wmanIfBsOfdmaULAllocSubchBitmap,
       "wmanIfBsOfdmaOptPermULAllocSubchBitmap": wmanIfBsOfdmaOptPermULAllocSubchBitmap,
       "wmanIfBsOfdmaBandAMCAllocThreshold": wmanIfBsOfdmaBandAMCAllocThreshold,
       "wmanIfBsOfdmaBandAMCReleaseThreshold": wmanIfBsOfdmaBandAMCReleaseThreshold,
       "wmanIfBsOfdmaBandAMCAllocTimer": wmanIfBsOfdmaBandAMCAllocTimer,
       "wmanIfBsOfdmaBandAMCReleaseTimer": wmanIfBsOfdmaBandAMCReleaseTimer,
       "wmanIfBsOfdmaBandStatRepMAXPeriod": wmanIfBsOfdmaBandStatRepMAXPeriod,
       "wmanIfBsOfdmaBandAMCRetryTimer": wmanIfBsOfdmaBandAMCRetryTimer,
       "wmanIfBsOfdmaSafetyChAllocThreshold": wmanIfBsOfdmaSafetyChAllocThreshold,
       "wmanIfBsOfdmaSafetyChReleaseThreshold": wmanIfBsOfdmaSafetyChReleaseThreshold,
       "wmanIfBsOfdmaSafetyChAllocTimer": wmanIfBsOfdmaSafetyChAllocTimer,
       "wmanIfBsOfdmaSafetyChReleaseTimer": wmanIfBsOfdmaSafetyChReleaseTimer,
       "wmanIfBsOfdmaBinStatRepMAXPeriod": wmanIfBsOfdmaBinStatRepMAXPeriod,
       "wmanIfBsOfdmaSafetyChaRetryTimer": wmanIfBsOfdmaSafetyChaRetryTimer,
       "wmanIfBsOfdmaHARQAackDelayULBurst": wmanIfBsOfdmaHARQAackDelayULBurst,
       "wmanIfBsOfdmaCQICHBandAMCTranaDelay": wmanIfBsOfdmaCQICHBandAMCTranaDelay,
       "wmanIfBsOfdmaDownlinkChannelTable": wmanIfBsOfdmaDownlinkChannelTable,
       "wmanIfBsOfdmaDownlinkChannelEntry": wmanIfBsOfdmaDownlinkChannelEntry,
       "wmanIfBsOfdmaBsEIRP": wmanIfBsOfdmaBsEIRP,
       "wmanIfBsOfdmaChannelNumber": wmanIfBsOfdmaChannelNumber,
       "wmanIfBsOfdmaTTG": wmanIfBsOfdmaTTG,
       "wmanIfBsOfdmaRTG": wmanIfBsOfdmaRTG,
       "wmanIfBsOfdmaInitRngMaxRSS": wmanIfBsOfdmaInitRngMaxRSS,
       "wmanIfBsOfdmaDownlinkCenterFreq": wmanIfBsOfdmaDownlinkCenterFreq,
       "wmanIfBsOfdmaBsId": wmanIfBsOfdmaBsId,
       "wmanIfBsOfdmaMacVersion": wmanIfBsOfdmaMacVersion,
       "wmanIfBsOfdmaFrameDurationCode": wmanIfBsOfdmaFrameDurationCode,
       "wmanIfBsOfdmaSizeCqichIdField": wmanIfBsOfdmaSizeCqichIdField,
       "wmanIfBsOfdmaHARQAackDelayBurst": wmanIfBsOfdmaHARQAackDelayBurst,
       "wmanIfBsOfdmaUcdBurstProfileTable": wmanIfBsOfdmaUcdBurstProfileTable,
       "wmanIfBsOfdmaUcdBurstProfileEntry": wmanIfBsOfdmaUcdBurstProfileEntry,
       "wmanIfBsOfdmaUiucIndex": wmanIfBsOfdmaUiucIndex,
       "wmanIfBsOfdmaUcdFecCodeType": wmanIfBsOfdmaUcdFecCodeType,
       "wmanIfBsOfdmaRangingDataRatio": wmanIfBsOfdmaRangingDataRatio,
       "wmanIfBsOfdmaNorCOverNOverride": wmanIfBsOfdmaNorCOverNOverride,
       "wmanIfBsOfdmaUcdBurstProfileRowStatus": wmanIfBsOfdmaUcdBurstProfileRowStatus,
       "wmanIfBsOfdmaDcdBurstProfileTable": wmanIfBsOfdmaDcdBurstProfileTable,
       "wmanIfBsOfdmaDcdBurstProfileEntry": wmanIfBsOfdmaDcdBurstProfileEntry,
       "wmanIfBsOfdmaDiucIndex": wmanIfBsOfdmaDiucIndex,
       "wmanIfBsOfdmaDownlinkFrequency": wmanIfBsOfdmaDownlinkFrequency,
       "wmanIfBsOfdmaDcdFecCodeType": wmanIfBsOfdmaDcdFecCodeType,
       "wmanIfBsOfdmaDiucMandatoryExitThresh": wmanIfBsOfdmaDiucMandatoryExitThresh,
       "wmanIfBsOfdmaDiucMinEntryThresh": wmanIfBsOfdmaDiucMinEntryThresh,
       "wmanIfBsOfdmaDcdBurstProfileRowStatus": wmanIfBsOfdmaDcdBurstProfileRowStatus,
       "wmanIfSsObjects": wmanIfSsObjects,
       "wmanIfSsCps": wmanIfSsCps,
       "wmanIfSsConfigurationTable": wmanIfSsConfigurationTable,
       "wmanIfSsConfigurationEntry": wmanIfSsConfigurationEntry,
       "wmanIfSsLostDLMapInterval": wmanIfSsLostDLMapInterval,
       "wmanIfSsLostULMapInterval": wmanIfSsLostULMapInterval,
       "wmanIfSsContentionRangRetries": wmanIfSsContentionRangRetries,
       "wmanIfSsRequestRetries": wmanIfSsRequestRetries,
       "wmanIfSsRegRequestRetries": wmanIfSsRegRequestRetries,
       "wmanIfSsTftpBackoffStart": wmanIfSsTftpBackoffStart,
       "wmanIfSsTftpBackoffEnd": wmanIfSsTftpBackoffEnd,
       "wmanIfSsTftpRequestRetries": wmanIfSsTftpRequestRetries,
       "wmanIfSsTftpDownloadRetries": wmanIfSsTftpDownloadRetries,
       "wmanIfSsTftpWait": wmanIfSsTftpWait,
       "wmanIfSsToDRetries": wmanIfSsToDRetries,
       "wmanIfSsToDRetryPeriod": wmanIfSsToDRetryPeriod,
       "wmanIfSsT1Timeout": wmanIfSsT1Timeout,
       "wmanIfSsT2Timeout": wmanIfSsT2Timeout,
       "wmanIfSsT3Timeout": wmanIfSsT3Timeout,
       "wmanIfSsT4Timeout": wmanIfSsT4Timeout,
       "wmanIfSsT6Timeout": wmanIfSsT6Timeout,
       "wmanIfSsT12Timeout": wmanIfSsT12Timeout,
       "wmanIfSsT14Timeout": wmanIfSsT14Timeout,
       "wmanIfSsT16Timeout": wmanIfSsT16Timeout,
       "wmanIfSsT18Timeout": wmanIfSsT18Timeout,
       "wmanIfSsT19Timeout": wmanIfSsT19Timeout,
       "wmanIfSsT20Timeout": wmanIfSsT20Timeout,
       "wmanIfSsT21Timeout": wmanIfSsT21Timeout,
       "wmanIfSsSBCRequestRetries": wmanIfSsSBCRequestRetries,
       "wmanIfSsTftpCpltRetries": wmanIfSsTftpCpltRetries,
       "wmanIfSsT26Timeout": wmanIfSsT26Timeout,
       "wmanIfSsDLManagProcTime": wmanIfSsDLManagProcTime,
       "wmanIfSsChannelMeasurementTable": wmanIfSsChannelMeasurementTable,
       "wmanIfSsChannelMeasurementEntry": wmanIfSsChannelMeasurementEntry,
       "wmanIfSsHistogramIndex": wmanIfSsHistogramIndex,
       "wmanIfSsChannelNumber": wmanIfSsChannelNumber,
       "wmanIfSsStartFrame": wmanIfSsStartFrame,
       "wmanIfSsDuration": wmanIfSsDuration,
       "wmanIfSsBasicReport": wmanIfSsBasicReport,
       "wmanIfSsMeanCinrReport": wmanIfSsMeanCinrReport,
       "wmanIfSsStdDeviationCinrReport": wmanIfSsStdDeviationCinrReport,
       "wmanIfSsMeanRssiReport": wmanIfSsMeanRssiReport,
       "wmanIfSsStdDeviationRssiReport": wmanIfSsStdDeviationRssiReport,
       "wmanIfSsPkmObjects": wmanIfSsPkmObjects,
       "wmanIfSsPkmAuthTable": wmanIfSsPkmAuthTable,
       "wmanIfSsPkmAuthEntry": wmanIfSsPkmAuthEntry,
       "wmanIfSsPkmAuthState": wmanIfSsPkmAuthState,
       "wmanIfSsPkmAuthKeySequenceNumber": wmanIfSsPkmAuthKeySequenceNumber,
       "wmanIfSsPkmAuthExpiresOld": wmanIfSsPkmAuthExpiresOld,
       "wmanIfSsPkmAuthExpiresNew": wmanIfSsPkmAuthExpiresNew,
       "wmanIfSsPkmAuthReset": wmanIfSsPkmAuthReset,
       "wmanIfSsPkmAuthentInfos": wmanIfSsPkmAuthentInfos,
       "wmanIfSsPkmAuthRequests": wmanIfSsPkmAuthRequests,
       "wmanIfSsPkmAuthReplies": wmanIfSsPkmAuthReplies,
       "wmanIfSsPkmAuthRejects": wmanIfSsPkmAuthRejects,
       "wmanIfSsPkmAuthInvalids": wmanIfSsPkmAuthInvalids,
       "wmanIfSsPkmAuthRejectErrorCode": wmanIfSsPkmAuthRejectErrorCode,
       "wmanIfSsPkmAuthRejectErrorString": wmanIfSsPkmAuthRejectErrorString,
       "wmanIfSsPkmAuthInvalidErrorCode": wmanIfSsPkmAuthInvalidErrorCode,
       "wmanIfSsPkmAuthInvalidErrorString": wmanIfSsPkmAuthInvalidErrorString,
       "wmanIfSsPkmAuthGraceTime": wmanIfSsPkmAuthGraceTime,
       "wmanIfSsPkmTekGraceTime": wmanIfSsPkmTekGraceTime,
       "wmanIfSsPkmAuthWaitTimeout": wmanIfSsPkmAuthWaitTimeout,
       "wmanIfSsPkmReauthWaitTimeout": wmanIfSsPkmReauthWaitTimeout,
       "wmanIfSsPkmOpWaitTimeout": wmanIfSsPkmOpWaitTimeout,
       "wmanIfSsPkmRekeyWaitTimeout": wmanIfSsPkmRekeyWaitTimeout,
       "wmanIfSsPkmAuthRejectWaitTimeout": wmanIfSsPkmAuthRejectWaitTimeout,
       "wmanIfSsPkmTekTable": wmanIfSsPkmTekTable,
       "wmanIfSsPkmTekEntry": wmanIfSsPkmTekEntry,
       "wmanIfSsPkmTekSAId": wmanIfSsPkmTekSAId,
       "wmanIfSsPkmTekSAType": wmanIfSsPkmTekSAType,
       "wmanIfSsPkmTekDataEncryptAlg": wmanIfSsPkmTekDataEncryptAlg,
       "wmanIfSsPkmTekDataAuthentAlg": wmanIfSsPkmTekDataAuthentAlg,
       "wmanIfSsPkmTekEncryptAlg": wmanIfSsPkmTekEncryptAlg,
       "wmanIfSsPkmTekState": wmanIfSsPkmTekState,
       "wmanIfSsPkmTekKeySequenceNumber": wmanIfSsPkmTekKeySequenceNumber,
       "wmanIfSsPkmTekExpiresOld": wmanIfSsPkmTekExpiresOld,
       "wmanIfSsPkmTekExpiresNew": wmanIfSsPkmTekExpiresNew,
       "wmanIfSsPkmTekKeyRequests": wmanIfSsPkmTekKeyRequests,
       "wmanIfSsPkmTekKeyReplies": wmanIfSsPkmTekKeyReplies,
       "wmanIfSsPkmTekKeyRejects": wmanIfSsPkmTekKeyRejects,
       "wmanIfSsPkmTekInvalids": wmanIfSsPkmTekInvalids,
       "wmanIfSsPkmTekAuthPends": wmanIfSsPkmTekAuthPends,
       "wmanIfSsPkmTekKeyRejectErrorCode": wmanIfSsPkmTekKeyRejectErrorCode,
       "wmanIfSsPkmTekKeyRejectErrorString": wmanIfSsPkmTekKeyRejectErrorString,
       "wmanIfSsPkmTekInvalidErrorCode": wmanIfSsPkmTekInvalidErrorCode,
       "wmanIfSsPkmTekInvalidErrorString": wmanIfSsPkmTekInvalidErrorString,
       "wmanIfSsDeviceCertTable": wmanIfSsDeviceCertTable,
       "wmanIfSsDeviceCertEntry": wmanIfSsDeviceCertEntry,
       "wmanIfSsDeviceCert": wmanIfSsDeviceCert,
       "wmanIfSsDeviceManufCert": wmanIfSsDeviceManufCert,
       "wmanIfSsNotification": wmanIfSsNotification,
       "wmanIfSsTrapControl": wmanIfSsTrapControl,
       "wmanIfSsTrapControlRegister": wmanIfSsTrapControlRegister,
       "wmanIfSsThresholdConfigTable": wmanIfSsThresholdConfigTable,
       "wmanIfSsThresholdConfigEntry": wmanIfSsThresholdConfigEntry,
       "wmanIfSsRssiLowThreshold": wmanIfSsRssiLowThreshold,
       "wmanIfSsRssiHighThreshold": wmanIfSsRssiHighThreshold,
       "wmanIfSsTrapDefinitions": wmanIfSsTrapDefinitions,
       "wmanIfSsTrapPrefix": wmanIfSsTrapPrefix,
       "wmanIfSsTlvUnknownTrap": wmanIfSsTlvUnknownTrap,
       "wmanIfSsDynamicServiceFailTrap": wmanIfSsDynamicServiceFailTrap,
       "wmanIfSsDhcpSuccessTrap": wmanIfSsDhcpSuccessTrap,
       "wmanIfSsRssiStatusChangeTrap": wmanIfSsRssiStatusChangeTrap,
       "wmanIfSsNotificationObjectsTable": wmanIfSsNotificationObjectsTable,
       "wmanIfSsNotificationObjectsEntry": wmanIfSsNotificationObjectsEntry,
       "wmanIfSsMacAddress": wmanIfSsMacAddress,
       "wmanIfSsUnknownTlv": wmanIfSsUnknownTlv,
       "wmanIfSsDynamicServiceType": wmanIfSsDynamicServiceType,
       "wmanIfSsDynamicServiceFailReason": wmanIfSsDynamicServiceFailReason,
       "wmanIfSsRssiStatus": wmanIfSsRssiStatus,
       "wmanIfSsRssiStatusInfo": wmanIfSsRssiStatusInfo,
       "wmanIfSsPhy": wmanIfSsPhy,
       "wmanIfSsOfdmPhy": wmanIfSsOfdmPhy,
       "wmanIfSsOfdmUplinkChannelTable": wmanIfSsOfdmUplinkChannelTable,
       "wmanIfSsOfdmUplinkChannelEntry": wmanIfSsOfdmUplinkChannelEntry,
       "wmanIfSsOfdmCtBasedResvTimeout": wmanIfSsOfdmCtBasedResvTimeout,
       "wmanIfSsOfdmBwReqOppSize": wmanIfSsOfdmBwReqOppSize,
       "wmanIfSsOfdmRangReqOppSize": wmanIfSsOfdmRangReqOppSize,
       "wmanIfSsOfdmUplinkCenterFreq": wmanIfSsOfdmUplinkCenterFreq,
       "wmanIfSsOfdmNumSubChReqRegionFull": wmanIfSsOfdmNumSubChReqRegionFull,
       "wmanIfSsOfdmNumSymbolsReqRegionFull": wmanIfSsOfdmNumSymbolsReqRegionFull,
       "wmanIfSsOfdmSubChFocusCtCode": wmanIfSsOfdmSubChFocusCtCode,
       "wmanIfSsOfdmUpLinkChannelId": wmanIfSsOfdmUpLinkChannelId,
       "wmanIfSsOfdmDownlinkChannelTable": wmanIfSsOfdmDownlinkChannelTable,
       "wmanIfSsOfdmDownlinkChannelEntry": wmanIfSsOfdmDownlinkChannelEntry,
       "wmanIfSsOfdmBsEIRP": wmanIfSsOfdmBsEIRP,
       "wmanIfSsOfdmChannelNumber": wmanIfSsOfdmChannelNumber,
       "wmanIfSsOfdmTTG": wmanIfSsOfdmTTG,
       "wmanIfSsOfdmRTG": wmanIfSsOfdmRTG,
       "wmanIfSsOfdmInitRngMaxRSS": wmanIfSsOfdmInitRngMaxRSS,
       "wmanIfSsOfdmDownlinkCenterFreq": wmanIfSsOfdmDownlinkCenterFreq,
       "wmanIfSsOfdmBsId": wmanIfSsOfdmBsId,
       "wmanIfSsOfdmMacVersion": wmanIfSsOfdmMacVersion,
       "wmanIfSsOfdmFrameDurationCode": wmanIfSsOfdmFrameDurationCode,
       "wmanIfSsOfdmDownLinkChannelId": wmanIfSsOfdmDownLinkChannelId,
       "wmanIfSsOfdmUcdBurstProfileTable": wmanIfSsOfdmUcdBurstProfileTable,
       "wmanIfSsOfdmUcdBurstProfileEntry": wmanIfSsOfdmUcdBurstProfileEntry,
       "wmanIfSsOfdmUiucIndex": wmanIfSsOfdmUiucIndex,
       "wmanIfSsOfdmUcdFecCodeType": wmanIfSsOfdmUcdFecCodeType,
       "wmanIfSsOfdmFocusCtPowerBoost": wmanIfSsOfdmFocusCtPowerBoost,
       "wmanIfSsOfdmUcdTcsEnable": wmanIfSsOfdmUcdTcsEnable,
       "wmanIfSsOfdmDcdBurstProfileTable": wmanIfSsOfdmDcdBurstProfileTable,
       "wmanIfSsOfdmDcdBurstProfileEntry": wmanIfSsOfdmDcdBurstProfileEntry,
       "wmanIfSsOfdmDiucIndex": wmanIfSsOfdmDiucIndex,
       "wmanIfSsOfdmDownlinkFrequency": wmanIfSsOfdmDownlinkFrequency,
       "wmanIfSsOfdmDcdFecCodeType": wmanIfSsOfdmDcdFecCodeType,
       "wmanIfSsOfdmDiucMandatoryExitThresh": wmanIfSsOfdmDiucMandatoryExitThresh,
       "wmanIfSsOfdmDiucMinEntryThresh": wmanIfSsOfdmDiucMinEntryThresh,
       "wmanIfSsOfdmTcsEnable": wmanIfSsOfdmTcsEnable,
       "wmanIfSsOfdmaPhy": wmanIfSsOfdmaPhy,
       "wmanIfSsOfdmaUplinkChannelTable": wmanIfSsOfdmaUplinkChannelTable,
       "wmanIfSsOfdmaUplinkChannelEntry": wmanIfSsOfdmaUplinkChannelEntry,
       "wmanIfSsOfdmaCtBasedResvTimeout": wmanIfSsOfdmaCtBasedResvTimeout,
       "wmanIfSsOfdmaBwReqOppSize": wmanIfSsOfdmaBwReqOppSize,
       "wmanIfSsOfdmaRangReqOppSize": wmanIfSsOfdmaRangReqOppSize,
       "wmanIfSsOfdmaUplinkCenterFreq": wmanIfSsOfdmaUplinkCenterFreq,
       "wmanIfSsOfdmaInitRngCodes": wmanIfSsOfdmaInitRngCodes,
       "wmanIfSsOfdmaPeriodicRngCodes": wmanIfSsOfdmaPeriodicRngCodes,
       "wmanIfSsOfdmaBWReqCodes": wmanIfSsOfdmaBWReqCodes,
       "wmanIfSsOfdmaPerRngBackoffStart": wmanIfSsOfdmaPerRngBackoffStart,
       "wmanIfSsOfdmaPerRngBackoffEnd": wmanIfSsOfdmaPerRngBackoffEnd,
       "wmanIfSsOfdmaStartOfRngCodes": wmanIfSsOfdmaStartOfRngCodes,
       "wmanIfSsOfdmaPermutationBase": wmanIfSsOfdmaPermutationBase,
       "wmanIfSsOfdmaULAllocSubchBitmap": wmanIfSsOfdmaULAllocSubchBitmap,
       "wmanIfSsOfdmaOptPermULAllocSubchBitmap": wmanIfSsOfdmaOptPermULAllocSubchBitmap,
       "wmanIfSsOfdmaBandAMCAllocThreshold": wmanIfSsOfdmaBandAMCAllocThreshold,
       "wmanIfSsOfdmaBandAMCReleaseThreshold": wmanIfSsOfdmaBandAMCReleaseThreshold,
       "wmanIfSsOfdmaBandAMCAllocTimer": wmanIfSsOfdmaBandAMCAllocTimer,
       "wmanIfSsOfdmaBandAMCReleaseTimer": wmanIfSsOfdmaBandAMCReleaseTimer,
       "wmanIfSsOfdmaBandStatRepMAXPeriod": wmanIfSsOfdmaBandStatRepMAXPeriod,
       "wmanIfSsOfdmaBandAMCRetryTimer": wmanIfSsOfdmaBandAMCRetryTimer,
       "wmanIfSsOfdmaSafetyChAllocThreshold": wmanIfSsOfdmaSafetyChAllocThreshold,
       "wmanIfSsOfdmaSafetyChReleaseThreshold": wmanIfSsOfdmaSafetyChReleaseThreshold,
       "wmanIfSsOfdmaSafetyChAllocTimer": wmanIfSsOfdmaSafetyChAllocTimer,
       "wmanIfSsOfdmaSafetyChReleaseTimer": wmanIfSsOfdmaSafetyChReleaseTimer,
       "wmanIfSsOfdmaBinStatRepMAXPeriod": wmanIfSsOfdmaBinStatRepMAXPeriod,
       "wmanIfSsOfdmaSafetyChaRetryTimer": wmanIfSsOfdmaSafetyChaRetryTimer,
       "wmanIfSsOfdmaHARQAackDelayULBurst": wmanIfSsOfdmaHARQAackDelayULBurst,
       "wmanIfSsOfdmaCQICHBandAMCTranaDelay": wmanIfSsOfdmaCQICHBandAMCTranaDelay,
       "wmanIfSsOfdmaDownlinkChannelTable": wmanIfSsOfdmaDownlinkChannelTable,
       "wmanIfSsOfdmaDownlinkChannelEntry": wmanIfSsOfdmaDownlinkChannelEntry,
       "wmanIfSsOfdmaBsEIRP": wmanIfSsOfdmaBsEIRP,
       "wmanIfSsOfdmaChannelNumber": wmanIfSsOfdmaChannelNumber,
       "wmanIfSsOfdmaTTG": wmanIfSsOfdmaTTG,
       "wmanIfSsOfdmaRTG": wmanIfSsOfdmaRTG,
       "wmanIfSsOfdmaInitRngMaxRSS": wmanIfSsOfdmaInitRngMaxRSS,
       "wmanIfSsOfdmaDownlinkCenterFreq": wmanIfSsOfdmaDownlinkCenterFreq,
       "wmanIfSsOfdmaBsId": wmanIfSsOfdmaBsId,
       "wmanIfSsOfdmaMacVersion": wmanIfSsOfdmaMacVersion,
       "wmanIfSsOfdmaFrameDurationCode": wmanIfSsOfdmaFrameDurationCode,
       "wmanIfSsOfdmaSizeCqichIdField": wmanIfSsOfdmaSizeCqichIdField,
       "wmanIfSsOfdmaHARQAackDelayBurst": wmanIfSsOfdmaHARQAackDelayBurst,
       "wmanIfSsOfdmaUcdBurstProfileTable": wmanIfSsOfdmaUcdBurstProfileTable,
       "wmanIfSsOfdmaUcdBurstProfileEntry": wmanIfSsOfdmaUcdBurstProfileEntry,
       "wmanIfSsOfdmaUiucIndex": wmanIfSsOfdmaUiucIndex,
       "wmanIfSsOfdmaUcdFecCodeType": wmanIfSsOfdmaUcdFecCodeType,
       "wmanIfSsOfdmaRangingDataRatio": wmanIfSsOfdmaRangingDataRatio,
       "wmanIfSsOfdmaNorCOverNOverride": wmanIfSsOfdmaNorCOverNOverride,
       "wmanIfSsOfdmaDcdBurstProfileTable": wmanIfSsOfdmaDcdBurstProfileTable,
       "wmanIfSsOfdmaDcdBurstProfileEntry": wmanIfSsOfdmaDcdBurstProfileEntry,
       "wmanIfSsOfdmaDiucIndex": wmanIfSsOfdmaDiucIndex,
       "wmanIfSsOfdmaDownlinkFrequency": wmanIfSsOfdmaDownlinkFrequency,
       "wmanIfSsOfdmaDcdFecCodeType": wmanIfSsOfdmaDcdFecCodeType,
       "wmanIfSsOfdmaDiucMandatoryExitThresh": wmanIfSsOfdmaDiucMandatoryExitThresh,
       "wmanIfSsOfdmaDiucMinEntryThresh": wmanIfSsOfdmaDiucMinEntryThresh,
       "wmanIfCommonObjects": wmanIfCommonObjects,
       "wmanIfCmnPacketCs": wmanIfCmnPacketCs,
       "wmanIfCmnClassifierRuleTable": wmanIfCmnClassifierRuleTable,
       "wmanIfCmnClassifierRuleEntry": wmanIfCmnClassifierRuleEntry,
       "wmanIfCmnClassifierRuleIndex": wmanIfCmnClassifierRuleIndex,
       "wmanIfCmnClassifierRulePriority": wmanIfCmnClassifierRulePriority,
       "wmanIfCmnClassifierRuleIpTosLow": wmanIfCmnClassifierRuleIpTosLow,
       "wmanIfCmnClassifierRuleIpTosHigh": wmanIfCmnClassifierRuleIpTosHigh,
       "wmanIfCmnClassifierRuleIpTosMask": wmanIfCmnClassifierRuleIpTosMask,
       "wmanIfCmnClassifierRuleIpProtocol": wmanIfCmnClassifierRuleIpProtocol,
       "wmanIfCmnClassifierRuleIpSourceAddr": wmanIfCmnClassifierRuleIpSourceAddr,
       "wmanIfCmnClassifierRuleIpSourceMask": wmanIfCmnClassifierRuleIpSourceMask,
       "wmanIfCmnClassifierRuleIpDestAddr": wmanIfCmnClassifierRuleIpDestAddr,
       "wmanIfCmnClassifierRuleIpDestMask": wmanIfCmnClassifierRuleIpDestMask,
       "wmanIfCmnClassifierRuleSourcePortStart": wmanIfCmnClassifierRuleSourcePortStart,
       "wmanIfCmnClassifierRuleSourcePortEnd": wmanIfCmnClassifierRuleSourcePortEnd,
       "wmanIfCmnClassifierRuleDestPortStart": wmanIfCmnClassifierRuleDestPortStart,
       "wmanIfCmnClassifierRuleDestPortEnd": wmanIfCmnClassifierRuleDestPortEnd,
       "wmanIfCmnClassifierRuleDestMacAddr": wmanIfCmnClassifierRuleDestMacAddr,
       "wmanIfCmnClassifierRuleDestMacMask": wmanIfCmnClassifierRuleDestMacMask,
       "wmanIfCmnClassifierRuleSourceMacAddr": wmanIfCmnClassifierRuleSourceMacAddr,
       "wmanIfCmnClassifierRuleSourceMacMask": wmanIfCmnClassifierRuleSourceMacMask,
       "wmanIfCmnClassifierRuleEnetProtocolType": wmanIfCmnClassifierRuleEnetProtocolType,
       "wmanIfCmnClassifierRuleEnetProtocol": wmanIfCmnClassifierRuleEnetProtocol,
       "wmanIfCmnClassifierRuleUserPriLow": wmanIfCmnClassifierRuleUserPriLow,
       "wmanIfCmnClassifierRuleUserPriHigh": wmanIfCmnClassifierRuleUserPriHigh,
       "wmanIfCmnClassifierRuleVlanId": wmanIfCmnClassifierRuleVlanId,
       "wmanIfCmnClassifierRuleState": wmanIfCmnClassifierRuleState,
       "wmanIfCmnClassifierRulePkts": wmanIfCmnClassifierRulePkts,
       "wmanIfCmnClassifierRuleIpv6FlowLabel": wmanIfCmnClassifierRuleIpv6FlowLabel,
       "wmanIfCmnClassifierRuleBitMap": wmanIfCmnClassifierRuleBitMap,
       "wmanIfCmnPhsRuleTable": wmanIfCmnPhsRuleTable,
       "wmanIfCmnPhsRuleEntry": wmanIfCmnPhsRuleEntry,
       "wmanIfCmnPhsRulePhsIndex": wmanIfCmnPhsRulePhsIndex,
       "wmanIfCmnPhsRulePhsField": wmanIfCmnPhsRulePhsField,
       "wmanIfCmnPhsRulePhsMask": wmanIfCmnPhsRulePhsMask,
       "wmanIfCmnPhsRulePhsSize": wmanIfCmnPhsRulePhsSize,
       "wmanIfCmnPhsRulePhsVerify": wmanIfCmnPhsRulePhsVerify,
       "wmanIfCmnCps": wmanIfCmnCps,
       "wmanIfCmnCpsServiceFlowTable": wmanIfCmnCpsServiceFlowTable,
       "wmanIfCmnCpsServiceFlowEntry": wmanIfCmnCpsServiceFlowEntry,
       "wmanIfCmnCpsSfMacAddress": wmanIfCmnCpsSfMacAddress,
       "wmanIfCmnCpsSfId": wmanIfCmnCpsSfId,
       "wmanIfCmnCpsSfCid": wmanIfCmnCpsSfCid,
       "wmanIfCmnCpsSfDirection": wmanIfCmnCpsSfDirection,
       "wmanIfCmnCpsSfState": wmanIfCmnCpsSfState,
       "wmanIfCmnCpsTrafficPriority": wmanIfCmnCpsTrafficPriority,
       "wmanIfCmnCpsMaxSustainedRate": wmanIfCmnCpsMaxSustainedRate,
       "wmanIfCmnCpsMaxTrafficBurst": wmanIfCmnCpsMaxTrafficBurst,
       "wmanIfCmnCpsMinReservedRate": wmanIfCmnCpsMinReservedRate,
       "wmanIfCmnCpsToleratedJitter": wmanIfCmnCpsToleratedJitter,
       "wmanIfCmnCpsMaxLatency": wmanIfCmnCpsMaxLatency,
       "wmanIfCmnCpsFixedVsVariableSduInd": wmanIfCmnCpsFixedVsVariableSduInd,
       "wmanIfCmnCpsSduSize": wmanIfCmnCpsSduSize,
       "wmanIfCmnCpsSfSchedulingType": wmanIfCmnCpsSfSchedulingType,
       "wmanIfCmnCpsArqEnable": wmanIfCmnCpsArqEnable,
       "wmanIfCmnCpsArqWindowSize": wmanIfCmnCpsArqWindowSize,
       "wmanIfCmnCpsArqBlockLifetime": wmanIfCmnCpsArqBlockLifetime,
       "wmanIfCmnCpsArqSyncLossTimeout": wmanIfCmnCpsArqSyncLossTimeout,
       "wmanIfCmnCpsArqDeliverInOrder": wmanIfCmnCpsArqDeliverInOrder,
       "wmanIfCmnCpsArqRxPurgeTimeout": wmanIfCmnCpsArqRxPurgeTimeout,
       "wmanIfCmnCpsArqBlockSize": wmanIfCmnCpsArqBlockSize,
       "wmanIfCmnCpsMinRsvdTolerableRate": wmanIfCmnCpsMinRsvdTolerableRate,
       "wmanIfCmnCpsReqTxPolicy": wmanIfCmnCpsReqTxPolicy,
       "wmanIfCmnSfCsSpecification": wmanIfCmnSfCsSpecification,
       "wmanIfCmnCpsTargetSaid": wmanIfCmnCpsTargetSaid,
       "wmanIfCmnBsSsConfigurationTable": wmanIfCmnBsSsConfigurationTable,
       "wmanIfCmnBsSsConfigurationEntry": wmanIfCmnBsSsConfigurationEntry,
       "wmanIfCmnInvitedRangRetries": wmanIfCmnInvitedRangRetries,
       "wmanIfCmnDSxReqRetries": wmanIfCmnDSxReqRetries,
       "wmanIfCmnDSxRespRetries": wmanIfCmnDSxRespRetries,
       "wmanIfCmnT7Timeout": wmanIfCmnT7Timeout,
       "wmanIfCmnT8Timeout": wmanIfCmnT8Timeout,
       "wmanIfCmnT10Timeout": wmanIfCmnT10Timeout,
       "wmanIfCmnT22Timeout": wmanIfCmnT22Timeout,
       "wmanIfCmnPkmObjects": wmanIfCmnPkmObjects,
       "wmanIfCmnCryptoSuiteTable": wmanIfCmnCryptoSuiteTable,
       "wmanIfCmnCryptoSuiteEntry": wmanIfCmnCryptoSuiteEntry,
       "wmanIfCmnCryptoSuiteIndex": wmanIfCmnCryptoSuiteIndex,
       "wmanIfCmnCryptoSuiteDataEncryptAlg": wmanIfCmnCryptoSuiteDataEncryptAlg,
       "wmanIfCmnCryptoSuiteDataAuthentAlg": wmanIfCmnCryptoSuiteDataAuthentAlg,
       "wmanIfCmnCryptoSuiteTekEncryptAlg": wmanIfCmnCryptoSuiteTekEncryptAlg,
       "wmanIfMibConformance": wmanIfMibConformance,
       "wmanIfMibGroups": wmanIfMibGroups,
       "wmanIfMibCommonGroup": wmanIfMibCommonGroup,
       "wmanIfMibQoSGroup": wmanIfMibQoSGroup,
       "wmanIfMibBsGroup": wmanIfMibBsGroup,
       "wmanIfMibBsAasGroup": wmanIfMibBsAasGroup,
       "wmanIfMibSsGroup": wmanIfMibSsGroup,
       "wmanIfMibBsOfdmGroup": wmanIfMibBsOfdmGroup,
       "wmanIfMibSsOfdmGroup": wmanIfMibSsOfdmGroup,
       "wmanIfMibBsOfdmaGroup": wmanIfMibBsOfdmaGroup,
       "wmanIfMibSsOfdmaGroup": wmanIfMibSsOfdmaGroup,
       "wmanIfMibBsNotificationGroup": wmanIfMibBsNotificationGroup,
       "wmanIfMibSsNotificationGroup": wmanIfMibSsNotificationGroup,
       "wmanIfMibCmnPhsGroup": wmanIfMibCmnPhsGroup,
       "wmanIfMibBsPhsGroup": wmanIfMibBsPhsGroup,
       "wmanIfMibCompliances": wmanIfMibCompliances,
       "wmanIfMibCompliance": wmanIfMibCompliance}
)
