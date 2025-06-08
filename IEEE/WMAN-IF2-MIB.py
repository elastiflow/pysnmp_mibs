# SNMP MIB module (WMAN-IF2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/WMAN-IF2-MIB.mib
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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

wmanIf2Mib = ModuleIdentity(
    (1, 0, 8802, 16, 2)
)
if mibBuilder.loadTexts:
    wmanIf2Mib.setRevisions(
        ("2007-05-22 00:00",
         "2007-03-28 00:00",
         "2007-02-10 00:00",
         "2006-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class WmanIf2SfSchedulingType(TextualConvention, Integer32):
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
          ("extRealTimePollingService", 5),
          ("unsolicitedGrantService", 6))
    )



class WmanIf2PhsRuleVerify(TextualConvention, Integer32):
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



class WmanIf2ClassifierBitMap(TextualConvention, Bits):
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
          ("ipv6FlowLabel", 12),
          ("actionRule", 13))
    )


class WmanIf2SfState(TextualConvention, Integer32):
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



class WmanIf2ServClassName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )



class WmanIf2CsSpecification(TextualConvention, Integer32):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("packetIpV4", 1),
          ("packetIpV6", 2),
          ("packet802dot3Ethernet", 3),
          ("packet802dot1QVlan", 4),
          ("packetIpV4Over802dot3", 5),
          ("packetIpV6Over802dot3", 6),
          ("packetIpV4Over802dot1Q", 7),
          ("packetIpV6Over802dot1Q", 8),
          ("atm", 9),
          ("packet802dot3EthernetRohcHc", 10),
          ("packet802dot3EthernetEcrtpHc", 11),
          ("packetIp2RohcHc", 12),
          ("packetIp2EcrtpHc", 13))
    )



class WmanIf2MacVersion(TextualConvention, Integer32):
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
        *(("ieee802Dot16Of2001", 1),
          ("ieee802Dot16cOf2002", 2),
          ("ieee802Dot16aOf2003", 3),
          ("ieee802Dot16Of2004", 4),
          ("ieee802Dot16e", 5),
          ("tbd", 6))
    )



class WmanIf2CidType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class WmanIf2DataEncryptAlgId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              128)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("des56BitCbcMode", 1),
          ("aes128BitCcmMode", 2),
          ("aes128BitCbcMode", 3),
          ("aes128BitCtrMode", 128))
    )



class WmanIf2DataAuthAlgId(TextualConvention, Integer32):
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
          ("aes128BitCcmMode", 1))
    )



class WmanIf2TekEncryptAlgId(TextualConvention, Integer32):
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
        *(("tripleDes128BitKey", 1),
          ("rsa1024BitKey", 2),
          ("aes128BitKeyEcbMode", 3),
          ("aes128BitKeyWrap", 4))
    )



class WmanIf2PkmErrorCode(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("noFailure", 0),
          ("unauthorizedSs", 1),
          ("unauthorizedSaid", 2),
          ("unsolicited", 3),
          ("invalidKeySequence", 4),
          ("keyReqAuthFailure", 5),
          ("umknownManufactur", 6),
          ("invalidSignature", 7),
          ("asn1ParsingFailure", 8),
          ("ssCaOnHotList", 9),
          ("dataInconsistency", 10),
          ("ssBsIncompatibleSc", 11))
    )



class WmanIf2SaType(TextualConvention, Integer32):
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
        *(("primarySa", 0),
          ("staticSa", 1),
          ("dynamicSa", 2))
    )



class WmanIf2TekState(TextualConvention, Integer32):
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
        *(("start", 1),
          ("opWait", 2),
          ("opReauthWait", 3),
          ("operational", 4),
          ("rekeyWait", 5),
          ("rekeyReauthWait", 6))
    )



class WmanIf2CertificateStat(TextualConvention, Integer32):
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



class WmanIf2ChannelNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )



class WmanIf2OfdmFecCodeType(TextualConvention, Integer32):
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



class WmanIf2OfdmaFecCodeType(TextualConvention, Integer32):
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



class WmanIf2OfdmaUcdFecCode(TextualConvention, Integer32):
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
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52)
        )
    )
    namedValues = NamedValues(
        *(("qpskCc1Over2", 0),
          ("qpskCc3Over4", 1),
          ("sixteenQamCc1Over2", 2),
          ("sixteenQamCc3Over4", 3),
          ("sixtyFourQamCc1Over2", 4),
          ("sixtyFourQamCc2Over3", 5),
          ("sixtyFourQamCc3Over4", 6),
          ("qpskBtc1Over2", 7),
          ("qpskBtc3Over4", 8),
          ("sixteenQamBtc3Over5", 9),
          ("sixteenQamBtc4Over5", 10),
          ("sixtyFourQamBtc5Over8", 11),
          ("sixtyFourQamBtc4Over5", 12),
          ("qpskCtc1Over2", 13),
          ("reserved", 14),
          ("qpskCtc3Over4", 15),
          ("sixteenQamCtc1Over2", 16),
          ("sixteenQamCtc3Over4", 17),
          ("sixtyFourQamCtc1Over2", 18),
          ("sixtyFourQamCtc2Over3", 19),
          ("sixtyFourQamCtc3Over4", 20),
          ("sixtyFourQamCtc5Over6", 21),
          ("qpskZtCc1Over2", 22),
          ("qpskZtCc3Over4", 23),
          ("sixteenQamZtCc1Over2", 24),
          ("sixteenQamZtCc3Over4", 25),
          ("sixtyFourQamZtCc1Over2", 26),
          ("sixtyFourQamZtCc2Over3", 27),
          ("sixtyFourQamZtCc3Over4", 28),
          ("qpskLdpc1over2", 29),
          ("qpskLdpc2over3A", 30),
          ("qpskLdpc3over4A", 31),
          ("sixteenQamLdpc1over2", 32),
          ("sixteenQamLdpc2over3A", 33),
          ("sixteenQamLdpc3over4A", 34),
          ("sixtyFourQamLdpc1over2", 35),
          ("sixtyFourQamLdpc2over3A", 36),
          ("sixtyFourQamLdpc3over4A", 37),
          ("qpskLdpc2over3B", 38),
          ("qpskLdpc3over4B", 39),
          ("sixteenQamLdpc2over3B", 40),
          ("sixteenQamLdpc3over4B", 41),
          ("sixtyFourQamLdpc2over3B", 42),
          ("sixtyFourQamLdpc3over4B", 43),
          ("qpskCcOptIntv1over2", 44),
          ("qpskCcOptIntv3over4", 45),
          ("sixteenQamCcOptIntv1over2", 46),
          ("sixteenQamCcOptIntv3over4", 47),
          ("sixtyFourQamCcOptIntv2over3", 48),
          ("sixtyFourQamCcOptIntv3over4", 49),
          ("qpskLdpc5over6", 50),
          ("sixteenQamLdpc5over6", 51),
          ("sixtyFourQamLdpc5over6", 52))
    )



class WmanIf2OfdmaDcdFecCode(TextualConvention, Integer32):
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
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49)
        )
    )
    namedValues = NamedValues(
        *(("qpskCc1Over2", 0),
          ("qpskCc3Over4", 1),
          ("sixteenQamCc1Over2", 2),
          ("sixteenQamCc3Over4", 3),
          ("sixtyFourQamCc1Over2", 4),
          ("sixtyFourQamCc2Over3", 5),
          ("sixtyFourQamCc3Over4", 6),
          ("qpskBtc1Over2", 7),
          ("qpskBtc3Over4Or2Over3", 8),
          ("sixteenQamBtc3Over5", 9),
          ("sixteenQamBtc4Over5", 10),
          ("sixtyFourQamBtc2Over3Or5Over8", 11),
          ("sixtyFourQamBtc5Over6Or4Over5", 12),
          ("qpskCtc1Over2", 13),
          ("reserved14", 14),
          ("qpskCtc3Over4", 15),
          ("sixteenQamCtc1Over2", 16),
          ("sixteenQamCtc3Over4", 17),
          ("sixtyFourQamCtc1Over2", 18),
          ("sixtyFourQamCtc2Over3", 19),
          ("sixtyFourQamCtc3Over4", 20),
          ("sixtyFourQamCtc5Over6", 21),
          ("qpskZtCc1Over2", 22),
          ("qpskZtCc3Over4", 23),
          ("sixteenQamZtCc1Over2", 24),
          ("sixteenQamZtCc3Over4", 25),
          ("sixtyFourQamZtCc1Over2", 26),
          ("sixtyFourQamZtCc2Over3", 27),
          ("sixtyFourQamZtCc3Over4", 28),
          ("reserved29", 29),
          ("reserved30", 30),
          ("reserved31", 31),
          ("reserved32", 32),
          ("reserved33", 33),
          ("reserved34", 34),
          ("reserved35", 35),
          ("reserved36", 36),
          ("reserved37", 37),
          ("reserved38", 38),
          ("reserved39", 39),
          ("reserved40", 40),
          ("reserved41", 41),
          ("reserved42", 42),
          ("reserved43", 43),
          ("qpskCcOptIntv1over2", 44),
          ("qpskCcOptIntv3over4", 45),
          ("sixteenQamCcOptIntv1over2", 46),
          ("sixteenQamCcOptIntv3over4", 47),
          ("sixtyFourQamCcOptIntv2over3", 48),
          ("sixtyFourQamCcOptIntv3over4", 49))
    )



class WmanIf2NumOfCid(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )



class WmanIf2ArqSupportType(TextualConvention, Integer32):
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



class WmanIf2MaxDsxFlowType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class WmanIf2MacCrcSupport(TextualConvention, Integer32):
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



class WmanIf2MaxMcaFlowType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class WmanIf2MaxMcpGroupCid(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class WmanIf2MaxPkmFlowType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class WmanIf2AuthPolicyType(TextualConvention, Bits):
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


class WmanIf2MaxNumOfSaType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class WmanIf2IpVersionType(TextualConvention, Integer32):
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



class WmanIf2MacCsBitMap(TextualConvention, Bits):
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
          ("packetIpv6Over802Dot1Q", 8),
          ("packet802dot3EthernetRohcHc", 9),
          ("packet802dot3EthernetEcrtpHc", 10),
          ("packetIpv4Orv6RohcHc", 11),
          ("packetIpv4Orv6EcrtpHc", 12))
    )


class WmanIf2MaxClassifiers(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class WmanIf2PhsSupportType(TextualConvention, Integer32):
    status = "current"
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
        *(("noPhsSupport", 0),
          ("atmPhsSupport", 1),
          ("packetPhsSupport", 2),
          ("atmAndPacketPhsSupport", 3))
    )



class WmanIf2BwAllocSupport(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("reserved", 0),
          ("halfDuplexFdd", 1),
          ("fullDuplexFdd", 2))
    )


class WmanIf2PduConstruction(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("piggybackedRequests", 0),
          ("fsnValuesSize", 1))
    )


class WmanIf2SsTransitionGap(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class WmanIf2MaxTxPowerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class WmanIf2OfdmFftSizes(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("fft256", 0),
          ("fft2048", 1))
    )


class WmanIf2OfdmSsDeModType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("qam64", 0),
          ("btc", 1),
          ("ctc", 2),
          ("stc", 3),
          ("aas", 4),
          ("subchannelization", 5))
    )


class WmanIf2OfdmSsModType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("qam64", 0),
          ("btc", 1),
          ("ctc", 2),
          ("subchannelization", 3),
          ("focusedCtBwReq", 4),
          ("ulCyclicDelay", 5))
    )


class WmanIf2OfdmFocusedCt(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("focusedCtSupport", 0)
    )


class WmanIf2OfdmTcSublayer(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("tcSublayerSupport", 0)
    )


class WmanIf2OfdmPrivMap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("regularMap", 0),
          ("compressedMap", 1))
    )


class WmanIf2OfdmUlPower(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ulOpenLoopPwrCntl", 0),
          ("ulAasPreamblePwrCntl", 1))
    )


class WmanIf2BsIdType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6



class WmanIf2Ipv6FlowLabel(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3



class WmanIf2OfdmaFftSizes(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("fft256", 0),
          ("fft2048", 1),
          ("fft128", 2),
          ("fft512", 3),
          ("fft1024", 4))
    )


class WmanIf2OfdmaMsDeModType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("qam64", 0),
          ("btc", 1),
          ("ctc", 2),
          ("stc", 3),
          ("ccWithInterleacer", 4),
          ("harqChase", 5),
          ("harqCtcIr", 6),
          ("reserved", 7),
          ("harqCcIr", 8),
          ("ldpc", 9),
          ("dedicatedPilots", 10))
    )


class WmanIf2OfdmaMsModType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("qam64", 0),
          ("btc", 1),
          ("ctc", 2),
          ("stc", 3),
          ("harqChase", 4),
          ("ctcIr", 5),
          ("ccIr", 6),
          ("ldpc", 7))
    )


class WmanIf2OfdmaPermutation(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("optionalPuscSupport", 0),
          ("optionalFuscSupport", 1),
          ("amcOneBySixSupport", 2),
          ("amcTwoByThreeSupport", 3),
          ("amcThreeByTwoSupport", 4),
          ("amcSupportWithHarqMap", 5),
          ("tusc1Support", 6),
          ("tusc2Support", 7))
    )


class WmanIf2OfdmaDemMimo(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("twoAntStcMatrixA", 0),
          ("twoAntStcMatrixBVCoding", 1),
          ("twoAntStcMatrixBHCoding", 2),
          ("fourAntStcMatrixA", 3),
          ("fourAntStcMatrixBVCoding", 4),
          ("fourAntStcMatrixBHCoding", 5),
          ("fourAntStcMatrixCVCoding", 6),
          ("fourAntStcMatrixCHCodingt", 7))
    )


class WmanIf2OfdmaMimoCap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("twoAntStcMatrixA", 0),
          ("twoAntStcMatrixBVCoding", 1),
          ("fourRxAntenna", 2),
          ("fourAntStcMatrixA", 3),
          ("fourAntStcMatrixBVCoding", 4),
          ("fourAntStcMatrixBHCoding", 5),
          ("fourAntStcMatrixCVCoding", 6),
          ("fourAntStcMatrixCHCodingt", 7),
          ("threeAntStcMatrixA", 8),
          ("threeAntStcMatrixB", 9),
          ("threeAntStcMatrixCVCoding", 10),
          ("threeAntStcMatrixCHCodingt", 11),
          ("calculatingPrecodingWeight", 12),
          ("adaptiveRateControl", 13),
          ("calculatingChannelMatrix", 14),
          ("antennaGrouping", 15),
          ("antennaSelection", 16),
          ("codebookBasedPrecoding", 17),
          ("longTermPrecoding", 18),
          ("mimoMidamble", 19))
    )


class WmanIf2OfdmaUlMimo(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("twoAntSttd", 0),
          ("twoAntSmVCoding", 1),
          ("oneAntCooperativeSm", 2))
    )


class WmanIf2OfdmaPrivMap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("harqMap", 0),
          ("privMap", 1),
          ("reducedPrivMap", 2),
          ("privMapChainEnable", 3),
          ("privMapDlFrameOffset", 4),
          ("privMapUlFrameOffset", 5),
          ("chainConcurrency0", 6),
          ("chainConcurrency1", 7))
    )


class WmanIf2OfdmaAasCap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("aasZone", 0),
          ("aasDiversityMapScan", 1),
          ("aasFbckRsp", 2),
          ("dlAasPreamble", 3),
          ("ulAasPreamble", 4))
    )


class WmanIf2OfdmaCinrCap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("phyCinrPreamble", 0),
          ("phyCinrPilotSubc", 1),
          ("phyCinrDataSubc", 2),
          ("effectiveCinrPreamble", 3),
          ("effectiveCinrPilotSubc", 4),
          ("effectiveCinrDataSubc", 5),
          ("twoCqiChannel", 6),
          ("freqSelectivityReport", 7))
    )


class WmanIf2OfdmaUlPower(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ulOpenLoopPwrCntl", 0),
          ("ulAasPreamblePwrCntl", 1))
    )


class WmanIf2OfdmaMapCap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("harqMap", 0),
          ("extendedHarqIe", 1),
          ("subMapFor1stZone", 2),
          ("subMapForOtherZone", 3),
          ("dlRegionDefinition", 4))
    )


class WmanIf2OfdmaUlCntlCh(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("threeBitMimoFastFeedback", 0),
          ("enhancedFastFeedback", 1),
          ("ulAck", 2),
          ("reserved", 3),
          ("uepFastFeedback", 4),
          ("fastDlMeasurementFeedback", 5),
          ("priSecFastFeedback", 6),
          ("diucCqiFastFeedback", 7))
    )


class WmanIf2OfdmaMsCistCap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("csitTypeA", 0),
          ("csitTypeB", 1),
          ("powerAssignment", 2),
          ("soundingRspTime0", 3),
          ("soundingRspTime1", 4),
          ("soundingRspTime2", 5),
          ("maxSimuSoundInst0", 6),
          ("maxSimuSoundInst1", 7),
          ("maxSimuSoundInst2", 8),
          ("maxSimuSoundInst3", 9),
          ("noP9Or18ForCsitTypeA", 10),
          ("csitNotSupported", 11))
    )


class WmanIf2OfdmaMaxHarq(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("maxUlHarqBurst0", 0),
          ("maxUlHarqBurst1", 1),
          ("maxUlHarqBurst2", 2),
          ("nonHarqBurstInUl", 3),
          ("maxDlHarqBurst0", 4),
          ("maxDlHarqBurst1", 5),
          ("maxDlHarqBurst2", 6),
          ("maxDlHarqBurst3", 7))
    )


class WmanIf2OfdmaModMimo(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("twoTxAntenna", 0),
          ("txDiversity", 1),
          ("spatialMultiplexing", 2),
          ("beamforming", 3),
          ("adaptiveRateControl", 4),
          ("singleAntenna", 5),
          ("twoAntenna", 6))
    )


class WmanIf2SdmaPilotCap(TextualConvention, Integer32):
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
        *(("noSupport", 0),
          ("sdmaPilotAandB", 1),
          ("allSdmaPilotPatterns", 2))
    )



class WmanIf2MultiBurst(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dlWithMultiFecType", 0),
          ("ulWithMultiFecType", 1))
    )



class WmanIf2IncrHarqBuf(TextualConvention, Integer32):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("dlNep0", 0),
          ("dlNep1", 1),
          ("dlNep2", 2),
          ("dlNep3", 3),
          ("dlAggFlag", 4),
          ("reserved0", 5),
          ("reserved1", 6),
          ("reserved2", 7),
          ("ulNep0", 8),
          ("ulNep1", 9),
          ("ulNep2", 10),
          ("ulNep3", 11),
          ("ulAggFlag", 12))
    )



class WmanIf2ChaseHarqBuf(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class WmanIf2PkmVersion(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("pkmVersion1", 0),
          ("pkmVersion2", 1))
    )


class WmanIf2AuthPolicy(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("rsaBasedAuthInitNtwkEntry", 0),
          ("eapBasedAuthInitNtwkEntry", 1),
          ("authenEapBasedAuthInitNtwkEntry", 2),
          ("reserved0", 3),
          ("rsaBasedAuthReentry", 4),
          ("eapBasedAuthReentry", 5),
          ("authenEapBasedAuthReentry", 6),
          ("reserved1", 7))
    )


class WmanIf2MacMode(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("hmac", 0),
          ("cmac", 1),
          ("sixtyfourBitShortHmaca", 2),
          ("eightyBitShortHmaca", 3),
          ("nintysixBitShortHmaca", 4))
    )


class WmanIf2ExtCapability(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("extSubheader", 0)
    )


class WmanIf2PackingSupport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noPackingSupport", 0),
          ("packingSupported", 1))
    )



class WmanIf2ExtRtpsSupport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noExtendedRtpsSupport", 0),
          ("extendedRtpsSupported", 1))
    )



class WmanIf2IpAllocMethod(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("dhcp", 0),
          ("mobileIpv4", 1),
          ("dhcpV6", 2),
          ("ipv6Autoconfig", 3))
    )


class WmanIf2ArqAckType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("selectiveAck", 0),
          ("cumulativeAck", 1),
          ("cumWithSelAck", 2),
          ("cumWithBlockSeqAck", 3))
    )


class WmanIf2MacHeaderSupp(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bwReqUlTxPowerReport", 0),
          ("bwReqCinrReport", 1),
          ("cqichAlloationReq", 2),
          ("phyChannelReport", 3),
          ("bwReqUlSleepCntl", 4),
          ("snReport", 5),
          ("feedbackReport", 6),
          ("sduSn", 7),
          ("sdnSnPeriod0", 8),
          ("sdnSnPeriod1", 9),
          ("sdnSnPeriod2", 10),
          ("dlSleepControl", 11),
          ("feedbackRequest", 12),
          ("mimcModeFeedback", 13),
          ("ulTxPowerReport", 14),
          ("miniFeedback", 15),
          ("snRequest", 16),
          ("shortPduSn", 17),
          ("longPduSn", 18))
    )


class WmanIf2HarqAckDelay(TextualConvention, Integer32):
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
        *(("oneframeoffset", 1),
          ("twoframesoffset", 2),
          ("threeframesoffset", 3))
    )



class WmanIf2AasBeamSel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAllowed", 0),
          ("allowed", 1))
    )



class WmanIf2MaxMacLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class WmanIfPermutationType(TextualConvention, Integer32):
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
        *(("pusc", 1),
          ("fusc", 2),
          ("optionalFusc", 3),
          ("amc", 4))
    )



class WmanIf2HoSupportType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("handover", 0),
          ("mdHandover", 1),
          ("fbssHandover", 2))
    )


class WmanIf2ActionRule(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("discardPacket", 0)
    )


# MIB Managed Objects in the order of their OIDs

_WmanIf2MibObjects_ObjectIdentity = ObjectIdentity
wmanIf2MibObjects = _WmanIf2MibObjects_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1)
)
_WmanIf2BsObjects_ObjectIdentity = ObjectIdentity
wmanIf2BsObjects = _WmanIf2BsObjects_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 1)
)
_WmanIf2BsPacketCs_ObjectIdentity = ObjectIdentity
wmanIf2BsPacketCs = _WmanIf2BsPacketCs_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 1, 1)
)
_WmanIf2BsSsPacketCounterTable_Object = MibTable
wmanIf2BsSsPacketCounterTable = _WmanIf2BsSsPacketCounterTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsPacketCounterTable.setStatus("current")
_WmanIf2BsSsPacketCounterEntry_Object = MibTableRow
wmanIf2BsSsPacketCounterEntry = _WmanIf2BsSsPacketCounterEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 1, 5, 1)
)
wmanIf2BsSsPacketCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-MIB", "wmanIf2CmnCpsSfMacAddress"),
    (0, "WMAN-IF2-MIB", "wmanIf2CmnCpsSfId"),
)
if mibBuilder.loadTexts:
    wmanIf2BsSsPacketCounterEntry.setStatus("current")
_WmanIf2BsSsMacSduCount_Type = Counter64
_WmanIf2BsSsMacSduCount_Object = MibTableColumn
wmanIf2BsSsMacSduCount = _WmanIf2BsSsMacSduCount_Object(
    (1, 0, 8802, 16, 2, 1, 1, 1, 5, 1, 1),
    _WmanIf2BsSsMacSduCount_Type()
)
wmanIf2BsSsMacSduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsMacSduCount.setStatus("current")
_WmanIf2BsSsOctetCount_Type = Counter64
_WmanIf2BsSsOctetCount_Object = MibTableColumn
wmanIf2BsSsOctetCount = _WmanIf2BsSsOctetCount_Object(
    (1, 0, 8802, 16, 2, 1, 1, 1, 5, 1, 2),
    _WmanIf2BsSsOctetCount_Type()
)
wmanIf2BsSsOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOctetCount.setStatus("current")


class _WmanIf2BsSsResetCounter_Type(Integer32):
    """Custom type wmanIf2BsSsResetCounter based on Integer32"""
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


_WmanIf2BsSsResetCounter_Type.__name__ = "Integer32"
_WmanIf2BsSsResetCounter_Object = MibTableColumn
wmanIf2BsSsResetCounter = _WmanIf2BsSsResetCounter_Object(
    (1, 0, 8802, 16, 2, 1, 1, 1, 5, 1, 3),
    _WmanIf2BsSsResetCounter_Type()
)
wmanIf2BsSsResetCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsResetCounter.setStatus("current")
_WmanIf2BsSsResetCounterTime_Type = TimeStamp
_WmanIf2BsSsResetCounterTime_Object = MibTableColumn
wmanIf2BsSsResetCounterTime = _WmanIf2BsSsResetCounterTime_Object(
    (1, 0, 8802, 16, 2, 1, 1, 1, 5, 1, 4),
    _WmanIf2BsSsResetCounterTime_Type()
)
wmanIf2BsSsResetCounterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsResetCounterTime.setStatus("current")
_WmanIf2BsCps_ObjectIdentity = ObjectIdentity
wmanIf2BsCps = _WmanIf2BsCps_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 1, 2)
)
_WmanIf2BsRegisteredSsTable_Object = MibTable
wmanIf2BsRegisteredSsTable = _WmanIf2BsRegisteredSsTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsRegisteredSsTable.setStatus("current")
_WmanIf2BsRegisteredSsEntry_Object = MibTableRow
wmanIf2BsRegisteredSsEntry = _WmanIf2BsRegisteredSsEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1)
)
wmanIf2BsRegisteredSsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-MIB", "wmanIf2BsSsMacAddress"),
)
if mibBuilder.loadTexts:
    wmanIf2BsRegisteredSsEntry.setStatus("current")
_WmanIf2BsSsMacAddress_Type = MacAddress
_WmanIf2BsSsMacAddress_Object = MibTableColumn
wmanIf2BsSsMacAddress = _WmanIf2BsSsMacAddress_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 1),
    _WmanIf2BsSsMacAddress_Type()
)
wmanIf2BsSsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsSsMacAddress.setStatus("current")
_WmanIf2BsSsBasicCid_Type = WmanIf2CidType
_WmanIf2BsSsBasicCid_Object = MibTableColumn
wmanIf2BsSsBasicCid = _WmanIf2BsSsBasicCid_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 2),
    _WmanIf2BsSsBasicCid_Type()
)
wmanIf2BsSsBasicCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsBasicCid.setStatus("current")
_WmanIf2BsSsPrimaryCid_Type = WmanIf2CidType
_WmanIf2BsSsPrimaryCid_Object = MibTableColumn
wmanIf2BsSsPrimaryCid = _WmanIf2BsSsPrimaryCid_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 3),
    _WmanIf2BsSsPrimaryCid_Type()
)
wmanIf2BsSsPrimaryCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPrimaryCid.setStatus("current")
_WmanIf2BsSsSecondaryCid_Type = WmanIf2CidType
_WmanIf2BsSsSecondaryCid_Object = MibTableColumn
wmanIf2BsSsSecondaryCid = _WmanIf2BsSsSecondaryCid_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 4),
    _WmanIf2BsSsSecondaryCid_Type()
)
wmanIf2BsSsSecondaryCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsSecondaryCid.setStatus("current")


class _WmanIf2BsSsManagementSupport_Type(Integer32):
    """Custom type wmanIf2BsSsManagementSupport based on Integer32"""
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


_WmanIf2BsSsManagementSupport_Type.__name__ = "Integer32"
_WmanIf2BsSsManagementSupport_Object = MibTableColumn
wmanIf2BsSsManagementSupport = _WmanIf2BsSsManagementSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 5),
    _WmanIf2BsSsManagementSupport_Type()
)
wmanIf2BsSsManagementSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsManagementSupport.setStatus("current")


class _WmanIf2BsSsIpManagementMode_Type(Integer32):
    """Custom type wmanIf2BsSsIpManagementMode based on Integer32"""
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


_WmanIf2BsSsIpManagementMode_Type.__name__ = "Integer32"
_WmanIf2BsSsIpManagementMode_Object = MibTableColumn
wmanIf2BsSsIpManagementMode = _WmanIf2BsSsIpManagementMode_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 6),
    _WmanIf2BsSsIpManagementMode_Type()
)
wmanIf2BsSsIpManagementMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsIpManagementMode.setStatus("current")
_WmanIf2BsSs2ndMgmtArqEnable_Type = TruthValue
_WmanIf2BsSs2ndMgmtArqEnable_Object = MibTableColumn
wmanIf2BsSs2ndMgmtArqEnable = _WmanIf2BsSs2ndMgmtArqEnable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 7),
    _WmanIf2BsSs2ndMgmtArqEnable_Type()
)
wmanIf2BsSs2ndMgmtArqEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqEnable.setStatus("current")


class _WmanIf2BsSs2ndMgmtArqWindowSize_Type(Integer32):
    """Custom type wmanIf2BsSs2ndMgmtArqWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WmanIf2BsSs2ndMgmtArqWindowSize_Type.__name__ = "Integer32"
_WmanIf2BsSs2ndMgmtArqWindowSize_Object = MibTableColumn
wmanIf2BsSs2ndMgmtArqWindowSize = _WmanIf2BsSs2ndMgmtArqWindowSize_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 8),
    _WmanIf2BsSs2ndMgmtArqWindowSize_Type()
)
wmanIf2BsSs2ndMgmtArqWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqWindowSize.setStatus("current")


class _WmanIf2BsSs2ndMgmtArqDnLinkTxDelay_Type(Integer32):
    """Custom type wmanIf2BsSs2ndMgmtArqDnLinkTxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSs2ndMgmtArqDnLinkTxDelay_Type.__name__ = "Integer32"
_WmanIf2BsSs2ndMgmtArqDnLinkTxDelay_Object = MibTableColumn
wmanIf2BsSs2ndMgmtArqDnLinkTxDelay = _WmanIf2BsSs2ndMgmtArqDnLinkTxDelay_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 9),
    _WmanIf2BsSs2ndMgmtArqDnLinkTxDelay_Type()
)
wmanIf2BsSs2ndMgmtArqDnLinkTxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqDnLinkTxDelay.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqDnLinkTxDelay.setUnits("us")


class _WmanIf2BsSs2ndMgmtArqUpLinkTxDelay_Type(Integer32):
    """Custom type wmanIf2BsSs2ndMgmtArqUpLinkTxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSs2ndMgmtArqUpLinkTxDelay_Type.__name__ = "Integer32"
_WmanIf2BsSs2ndMgmtArqUpLinkTxDelay_Object = MibTableColumn
wmanIf2BsSs2ndMgmtArqUpLinkTxDelay = _WmanIf2BsSs2ndMgmtArqUpLinkTxDelay_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 10),
    _WmanIf2BsSs2ndMgmtArqUpLinkTxDelay_Type()
)
wmanIf2BsSs2ndMgmtArqUpLinkTxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqUpLinkTxDelay.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqUpLinkTxDelay.setUnits("us")


class _WmanIf2BsSs2ndMgmtArqDnLinkRxDelay_Type(Integer32):
    """Custom type wmanIf2BsSs2ndMgmtArqDnLinkRxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSs2ndMgmtArqDnLinkRxDelay_Type.__name__ = "Integer32"
_WmanIf2BsSs2ndMgmtArqDnLinkRxDelay_Object = MibTableColumn
wmanIf2BsSs2ndMgmtArqDnLinkRxDelay = _WmanIf2BsSs2ndMgmtArqDnLinkRxDelay_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 11),
    _WmanIf2BsSs2ndMgmtArqDnLinkRxDelay_Type()
)
wmanIf2BsSs2ndMgmtArqDnLinkRxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqDnLinkRxDelay.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqDnLinkRxDelay.setUnits("us")


class _WmanIf2BsSs2ndMgmtArqUpLinkRxDelay_Type(Integer32):
    """Custom type wmanIf2BsSs2ndMgmtArqUpLinkRxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSs2ndMgmtArqUpLinkRxDelay_Type.__name__ = "Integer32"
_WmanIf2BsSs2ndMgmtArqUpLinkRxDelay_Object = MibTableColumn
wmanIf2BsSs2ndMgmtArqUpLinkRxDelay = _WmanIf2BsSs2ndMgmtArqUpLinkRxDelay_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 12),
    _WmanIf2BsSs2ndMgmtArqUpLinkRxDelay_Type()
)
wmanIf2BsSs2ndMgmtArqUpLinkRxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqUpLinkRxDelay.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqUpLinkRxDelay.setUnits("us")


class _WmanIf2BsSs2ndMgmtArqBlockLifetime_Type(Integer32):
    """Custom type wmanIf2BsSs2ndMgmtArqBlockLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSs2ndMgmtArqBlockLifetime_Type.__name__ = "Integer32"
_WmanIf2BsSs2ndMgmtArqBlockLifetime_Object = MibTableColumn
wmanIf2BsSs2ndMgmtArqBlockLifetime = _WmanIf2BsSs2ndMgmtArqBlockLifetime_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 13),
    _WmanIf2BsSs2ndMgmtArqBlockLifetime_Type()
)
wmanIf2BsSs2ndMgmtArqBlockLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqBlockLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqBlockLifetime.setUnits("10 us")


class _WmanIf2BsSs2ndMgmtArqSyncLossTimeout_Type(Integer32):
    """Custom type wmanIf2BsSs2ndMgmtArqSyncLossTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSs2ndMgmtArqSyncLossTimeout_Type.__name__ = "Integer32"
_WmanIf2BsSs2ndMgmtArqSyncLossTimeout_Object = MibTableColumn
wmanIf2BsSs2ndMgmtArqSyncLossTimeout = _WmanIf2BsSs2ndMgmtArqSyncLossTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 14),
    _WmanIf2BsSs2ndMgmtArqSyncLossTimeout_Type()
)
wmanIf2BsSs2ndMgmtArqSyncLossTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqSyncLossTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqSyncLossTimeout.setUnits("10 us")
_WmanIf2BsSs2ndMgmtArqDeliverInOrder_Type = TruthValue
_WmanIf2BsSs2ndMgmtArqDeliverInOrder_Object = MibTableColumn
wmanIf2BsSs2ndMgmtArqDeliverInOrder = _WmanIf2BsSs2ndMgmtArqDeliverInOrder_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 15),
    _WmanIf2BsSs2ndMgmtArqDeliverInOrder_Type()
)
wmanIf2BsSs2ndMgmtArqDeliverInOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqDeliverInOrder.setStatus("current")


class _WmanIf2BsSs2ndMgmtArqRxPurgeTimeout_Type(Integer32):
    """Custom type wmanIf2BsSs2ndMgmtArqRxPurgeTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSs2ndMgmtArqRxPurgeTimeout_Type.__name__ = "Integer32"
_WmanIf2BsSs2ndMgmtArqRxPurgeTimeout_Object = MibTableColumn
wmanIf2BsSs2ndMgmtArqRxPurgeTimeout = _WmanIf2BsSs2ndMgmtArqRxPurgeTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 16),
    _WmanIf2BsSs2ndMgmtArqRxPurgeTimeout_Type()
)
wmanIf2BsSs2ndMgmtArqRxPurgeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqRxPurgeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqRxPurgeTimeout.setUnits("10 us")


class _WmanIf2BsSs2ndMgmtArqBlockSize_Type(Integer32):
    """Custom type wmanIf2BsSs2ndMgmtArqBlockSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2040),
    )


_WmanIf2BsSs2ndMgmtArqBlockSize_Type.__name__ = "Integer32"
_WmanIf2BsSs2ndMgmtArqBlockSize_Object = MibTableColumn
wmanIf2BsSs2ndMgmtArqBlockSize = _WmanIf2BsSs2ndMgmtArqBlockSize_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 17),
    _WmanIf2BsSs2ndMgmtArqBlockSize_Type()
)
wmanIf2BsSs2ndMgmtArqBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqBlockSize.setStatus("current")


class _WmanIf2BsSsVendorIdEncoding_Type(OctetString):
    """Custom type wmanIf2BsSsVendorIdEncoding based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_WmanIf2BsSsVendorIdEncoding_Type.__name__ = "OctetString"
_WmanIf2BsSsVendorIdEncoding_Object = MibTableColumn
wmanIf2BsSsVendorIdEncoding = _WmanIf2BsSsVendorIdEncoding_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 18),
    _WmanIf2BsSsVendorIdEncoding_Type()
)
wmanIf2BsSsVendorIdEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsVendorIdEncoding.setStatus("current")


class _WmanIf2BsSsAasBroadcastPermission_Type(Integer32):
    """Custom type wmanIf2BsSsAasBroadcastPermission based on Integer32"""
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


_WmanIf2BsSsAasBroadcastPermission_Type.__name__ = "Integer32"
_WmanIf2BsSsAasBroadcastPermission_Object = MibTableColumn
wmanIf2BsSsAasBroadcastPermission = _WmanIf2BsSsAasBroadcastPermission_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 19),
    _WmanIf2BsSsAasBroadcastPermission_Type()
)
wmanIf2BsSsAasBroadcastPermission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsAasBroadcastPermission.setStatus("current")
_WmanIf2BsSsMaxTxPowerBpsk_Type = WmanIf2MaxTxPowerType
_WmanIf2BsSsMaxTxPowerBpsk_Object = MibTableColumn
wmanIf2BsSsMaxTxPowerBpsk = _WmanIf2BsSsMaxTxPowerBpsk_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 20),
    _WmanIf2BsSsMaxTxPowerBpsk_Type()
)
wmanIf2BsSsMaxTxPowerBpsk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsMaxTxPowerBpsk.setStatus("current")
_WmanIf2BsSsMaxTxPowerQpsk_Type = WmanIf2MaxTxPowerType
_WmanIf2BsSsMaxTxPowerQpsk_Object = MibTableColumn
wmanIf2BsSsMaxTxPowerQpsk = _WmanIf2BsSsMaxTxPowerQpsk_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 21),
    _WmanIf2BsSsMaxTxPowerQpsk_Type()
)
wmanIf2BsSsMaxTxPowerQpsk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsMaxTxPowerQpsk.setStatus("current")
_WmanIf2BsSsMaxTxPower16Qam_Type = WmanIf2MaxTxPowerType
_WmanIf2BsSsMaxTxPower16Qam_Object = MibTableColumn
wmanIf2BsSsMaxTxPower16Qam = _WmanIf2BsSsMaxTxPower16Qam_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 22),
    _WmanIf2BsSsMaxTxPower16Qam_Type()
)
wmanIf2BsSsMaxTxPower16Qam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsMaxTxPower16Qam.setStatus("current")
_WmanIf2BsSsMaxTxPower64Qam_Type = WmanIf2MaxTxPowerType
_WmanIf2BsSsMaxTxPower64Qam_Object = MibTableColumn
wmanIf2BsSsMaxTxPower64Qam = _WmanIf2BsSsMaxTxPower64Qam_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 23),
    _WmanIf2BsSsMaxTxPower64Qam_Type()
)
wmanIf2BsSsMaxTxPower64Qam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsMaxTxPower64Qam.setStatus("current")
_WmanIf2BsSsMacVersion_Type = WmanIf2MacVersion
_WmanIf2BsSsMacVersion_Object = MibTableColumn
wmanIf2BsSsMacVersion = _WmanIf2BsSsMacVersion_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 24),
    _WmanIf2BsSsMacVersion_Type()
)
wmanIf2BsSsMacVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsMacVersion.setStatus("current")
_WmanIf2BsConfigurationTable_Object = MibTable
wmanIf2BsConfigurationTable = _WmanIf2BsConfigurationTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wmanIf2BsConfigurationTable.setStatus("current")
_WmanIf2BsConfigurationEntry_Object = MibTableRow
wmanIf2BsConfigurationEntry = _WmanIf2BsConfigurationEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1)
)
wmanIf2BsConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsConfigurationEntry.setStatus("current")


class _WmanIf2BsDcdInterval_Type(Integer32):
    """Custom type wmanIf2BsDcdInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsDcdInterval_Type.__name__ = "Integer32"
_WmanIf2BsDcdInterval_Object = MibTableColumn
wmanIf2BsDcdInterval = _WmanIf2BsDcdInterval_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 1),
    _WmanIf2BsDcdInterval_Type()
)
wmanIf2BsDcdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsDcdInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsDcdInterval.setUnits("Number of MAC Frames")


class _WmanIf2BsUcdInterval_Type(Integer32):
    """Custom type wmanIf2BsUcdInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsUcdInterval_Type.__name__ = "Integer32"
_WmanIf2BsUcdInterval_Object = MibTableColumn
wmanIf2BsUcdInterval = _WmanIf2BsUcdInterval_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 2),
    _WmanIf2BsUcdInterval_Type()
)
wmanIf2BsUcdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsUcdInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsUcdInterval.setUnits("Number of MAC Frames")


class _WmanIf2BsUcdTransition_Type(Integer32):
    """Custom type wmanIf2BsUcdTransition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_WmanIf2BsUcdTransition_Type.__name__ = "Integer32"
_WmanIf2BsUcdTransition_Object = MibTableColumn
wmanIf2BsUcdTransition = _WmanIf2BsUcdTransition_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 3),
    _WmanIf2BsUcdTransition_Type()
)
wmanIf2BsUcdTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsUcdTransition.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsUcdTransition.setUnits("Number of MAC Frames")


class _WmanIf2BsDcdTransition_Type(Integer32):
    """Custom type wmanIf2BsDcdTransition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_WmanIf2BsDcdTransition_Type.__name__ = "Integer32"
_WmanIf2BsDcdTransition_Object = MibTableColumn
wmanIf2BsDcdTransition = _WmanIf2BsDcdTransition_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 4),
    _WmanIf2BsDcdTransition_Type()
)
wmanIf2BsDcdTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsDcdTransition.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsDcdTransition.setUnits("Number of MAC Frames")


class _WmanIf2BsInitialRangingInterval_Type(Integer32):
    """Custom type wmanIf2BsInitialRangingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )


_WmanIf2BsInitialRangingInterval_Type.__name__ = "Integer32"
_WmanIf2BsInitialRangingInterval_Object = MibTableColumn
wmanIf2BsInitialRangingInterval = _WmanIf2BsInitialRangingInterval_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 5),
    _WmanIf2BsInitialRangingInterval_Type()
)
wmanIf2BsInitialRangingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsInitialRangingInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsInitialRangingInterval.setUnits("Number of MAC Frames")


class _WmanIf2BsT9Timeout_Type(Integer32):
    """Custom type wmanIf2BsT9Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 65535),
    )


_WmanIf2BsT9Timeout_Type.__name__ = "Integer32"
_WmanIf2BsT9Timeout_Object = MibTableColumn
wmanIf2BsT9Timeout = _WmanIf2BsT9Timeout_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 6),
    _WmanIf2BsT9Timeout_Type()
)
wmanIf2BsT9Timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsT9Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsT9Timeout.setUnits("milliseconds")


class _WmanIf2BsSsULMapProcTime_Type(Unsigned32):
    """Custom type wmanIf2BsSsULMapProcTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 4294967295),
    )


_WmanIf2BsSsULMapProcTime_Type.__name__ = "Unsigned32"
_WmanIf2BsSsULMapProcTime_Object = MibTableColumn
wmanIf2BsSsULMapProcTime = _WmanIf2BsSsULMapProcTime_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 7),
    _WmanIf2BsSsULMapProcTime_Type()
)
wmanIf2BsSsULMapProcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsULMapProcTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSsULMapProcTime.setUnits("micro seconds")


class _WmanIf2BsSsRangRespProcTime_Type(Unsigned32):
    """Custom type wmanIf2BsSsRangRespProcTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 4294967295),
    )


_WmanIf2BsSsRangRespProcTime_Type.__name__ = "Unsigned32"
_WmanIf2BsSsRangRespProcTime_Object = MibTableColumn
wmanIf2BsSsRangRespProcTime = _WmanIf2BsSsRangRespProcTime_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 9),
    _WmanIf2BsSsRangRespProcTime_Type()
)
wmanIf2BsSsRangRespProcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsRangRespProcTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSsRangRespProcTime.setUnits("micro seconds")


class _WmanIf2BsT13Timeout_Type(Integer32):
    """Custom type wmanIf2BsT13Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 65535),
    )


_WmanIf2BsT13Timeout_Type.__name__ = "Integer32"
_WmanIf2BsT13Timeout_Object = MibTableColumn
wmanIf2BsT13Timeout = _WmanIf2BsT13Timeout_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 10),
    _WmanIf2BsT13Timeout_Type()
)
wmanIf2BsT13Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsT13Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsT13Timeout.setUnits("minutes")


class _WmanIf2BsT15Timeout_Type(Integer32):
    """Custom type wmanIf2BsT15Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 65535),
    )


_WmanIf2BsT15Timeout_Type.__name__ = "Integer32"
_WmanIf2BsT15Timeout_Object = MibTableColumn
wmanIf2BsT15Timeout = _WmanIf2BsT15Timeout_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 11),
    _WmanIf2BsT15Timeout_Type()
)
wmanIf2BsT15Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsT15Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsT15Timeout.setUnits("milliseconds")


class _WmanIf2BsT17Timeout_Type(Integer32):
    """Custom type wmanIf2BsT17Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_WmanIf2BsT17Timeout_Type.__name__ = "Integer32"
_WmanIf2BsT17Timeout_Object = MibTableColumn
wmanIf2BsT17Timeout = _WmanIf2BsT17Timeout_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 12),
    _WmanIf2BsT17Timeout_Type()
)
wmanIf2BsT17Timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsT17Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsT17Timeout.setUnits("minutes")


class _WmanIf2BsT27IdleTimer_Type(Unsigned32):
    """Custom type wmanIf2BsT27IdleTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 4294967295),
    )


_WmanIf2BsT27IdleTimer_Type.__name__ = "Unsigned32"
_WmanIf2BsT27IdleTimer_Object = MibTableColumn
wmanIf2BsT27IdleTimer = _WmanIf2BsT27IdleTimer_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 13),
    _WmanIf2BsT27IdleTimer_Type()
)
wmanIf2BsT27IdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsT27IdleTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsT27IdleTimer.setUnits("us")


class _WmanIf2BsT27ActiveTimer_Type(Unsigned32):
    """Custom type wmanIf2BsT27ActiveTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 4294967295),
    )


_WmanIf2BsT27ActiveTimer_Type.__name__ = "Unsigned32"
_WmanIf2BsT27ActiveTimer_Object = MibTableColumn
wmanIf2BsT27ActiveTimer = _WmanIf2BsT27ActiveTimer_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 14),
    _WmanIf2BsT27ActiveTimer_Type()
)
wmanIf2BsT27ActiveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsT27ActiveTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsT27ActiveTimer.setUnits("us")


class _WmanIf2Bs2ndMgmtDlQoSProfileIndex_Type(Integer32):
    """Custom type wmanIf2Bs2ndMgmtDlQoSProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2Bs2ndMgmtDlQoSProfileIndex_Type.__name__ = "Integer32"
_WmanIf2Bs2ndMgmtDlQoSProfileIndex_Object = MibTableColumn
wmanIf2Bs2ndMgmtDlQoSProfileIndex = _WmanIf2Bs2ndMgmtDlQoSProfileIndex_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 15),
    _WmanIf2Bs2ndMgmtDlQoSProfileIndex_Type()
)
wmanIf2Bs2ndMgmtDlQoSProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2Bs2ndMgmtDlQoSProfileIndex.setStatus("current")


class _WmanIf2Bs2ndMgmtUlQoSProfileIndex_Type(Integer32):
    """Custom type wmanIf2Bs2ndMgmtUlQoSProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2Bs2ndMgmtUlQoSProfileIndex_Type.__name__ = "Integer32"
_WmanIf2Bs2ndMgmtUlQoSProfileIndex_Object = MibTableColumn
wmanIf2Bs2ndMgmtUlQoSProfileIndex = _WmanIf2Bs2ndMgmtUlQoSProfileIndex_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 16),
    _WmanIf2Bs2ndMgmtUlQoSProfileIndex_Type()
)
wmanIf2Bs2ndMgmtUlQoSProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2Bs2ndMgmtUlQoSProfileIndex.setStatus("current")


class _WmanIf2BsAutoSfidEnabled_Type(Integer32):
    """Custom type wmanIf2BsAutoSfidEnabled based on Integer32"""
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


_WmanIf2BsAutoSfidEnabled_Type.__name__ = "Integer32"
_WmanIf2BsAutoSfidEnabled_Object = MibTableColumn
wmanIf2BsAutoSfidEnabled = _WmanIf2BsAutoSfidEnabled_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 17),
    _WmanIf2BsAutoSfidEnabled_Type()
)
wmanIf2BsAutoSfidEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsAutoSfidEnabled.setStatus("current")


class _WmanIf2BsAutoSfidRangeMin_Type(Unsigned32):
    """Custom type wmanIf2BsAutoSfidRangeMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIf2BsAutoSfidRangeMin_Type.__name__ = "Unsigned32"
_WmanIf2BsAutoSfidRangeMin_Object = MibTableColumn
wmanIf2BsAutoSfidRangeMin = _WmanIf2BsAutoSfidRangeMin_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 18),
    _WmanIf2BsAutoSfidRangeMin_Type()
)
wmanIf2BsAutoSfidRangeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsAutoSfidRangeMin.setStatus("current")


class _WmanIf2BsAutoSfidRangeMax_Type(Unsigned32):
    """Custom type wmanIf2BsAutoSfidRangeMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIf2BsAutoSfidRangeMax_Type.__name__ = "Unsigned32"
_WmanIf2BsAutoSfidRangeMax_Object = MibTableColumn
wmanIf2BsAutoSfidRangeMax = _WmanIf2BsAutoSfidRangeMax_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 19),
    _WmanIf2BsAutoSfidRangeMax_Type()
)
wmanIf2BsAutoSfidRangeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsAutoSfidRangeMax.setStatus("current")


class _WmanIf2BsAasChanFbckReqFreq_Type(Integer32):
    """Custom type wmanIf2BsAasChanFbckReqFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10000),
    )


_WmanIf2BsAasChanFbckReqFreq_Type.__name__ = "Integer32"
_WmanIf2BsAasChanFbckReqFreq_Object = MibTableColumn
wmanIf2BsAasChanFbckReqFreq = _WmanIf2BsAasChanFbckReqFreq_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 20),
    _WmanIf2BsAasChanFbckReqFreq_Type()
)
wmanIf2BsAasChanFbckReqFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsAasChanFbckReqFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsAasChanFbckReqFreq.setUnits("ms")


class _WmanIf2BsAasBeamSelectFreq_Type(Integer32):
    """Custom type wmanIf2BsAasBeamSelectFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10000),
    )


_WmanIf2BsAasBeamSelectFreq_Type.__name__ = "Integer32"
_WmanIf2BsAasBeamSelectFreq_Object = MibTableColumn
wmanIf2BsAasBeamSelectFreq = _WmanIf2BsAasBeamSelectFreq_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 21),
    _WmanIf2BsAasBeamSelectFreq_Type()
)
wmanIf2BsAasBeamSelectFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsAasBeamSelectFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsAasBeamSelectFreq.setUnits("ms")


class _WmanIf2BsAasChanFbckReqResolution_Type(Integer32):
    """Custom type wmanIf2BsAasChanFbckReqResolution based on Integer32"""
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


_WmanIf2BsAasChanFbckReqResolution_Type.__name__ = "Integer32"
_WmanIf2BsAasChanFbckReqResolution_Object = MibTableColumn
wmanIf2BsAasChanFbckReqResolution = _WmanIf2BsAasChanFbckReqResolution_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 22),
    _WmanIf2BsAasChanFbckReqResolution_Type()
)
wmanIf2BsAasChanFbckReqResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsAasChanFbckReqResolution.setStatus("current")


class _WmanIf2BsAasBeamReqResolution_Type(Integer32):
    """Custom type wmanIf2BsAasBeamReqResolution based on Integer32"""
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


_WmanIf2BsAasBeamReqResolution_Type.__name__ = "Integer32"
_WmanIf2BsAasBeamReqResolution_Object = MibTableColumn
wmanIf2BsAasBeamReqResolution = _WmanIf2BsAasBeamReqResolution_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 23),
    _WmanIf2BsAasBeamReqResolution_Type()
)
wmanIf2BsAasBeamReqResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsAasBeamReqResolution.setStatus("current")


class _WmanIf2BsAasNumOptDiversityZones_Type(Integer32):
    """Custom type wmanIf2BsAasNumOptDiversityZones based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsAasNumOptDiversityZones_Type.__name__ = "Integer32"
_WmanIf2BsAasNumOptDiversityZones_Object = MibTableColumn
wmanIf2BsAasNumOptDiversityZones = _WmanIf2BsAasNumOptDiversityZones_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 24),
    _WmanIf2BsAasNumOptDiversityZones_Type()
)
wmanIf2BsAasNumOptDiversityZones.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsAasNumOptDiversityZones.setStatus("current")


class _WmanIf2BsResetSector_Type(Integer32):
    """Custom type wmanIf2BsResetSector based on Integer32"""
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


_WmanIf2BsResetSector_Type.__name__ = "Integer32"
_WmanIf2BsResetSector_Object = MibTableColumn
wmanIf2BsResetSector = _WmanIf2BsResetSector_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 25),
    _WmanIf2BsResetSector_Type()
)
wmanIf2BsResetSector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsResetSector.setStatus("current")


class _WmanIf2BsSaChallengeTimer_Type(Integer32):
    """Custom type wmanIf2BsSaChallengeTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_WmanIf2BsSaChallengeTimer_Type.__name__ = "Integer32"
_WmanIf2BsSaChallengeTimer_Object = MibTableColumn
wmanIf2BsSaChallengeTimer = _WmanIf2BsSaChallengeTimer_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 27),
    _WmanIf2BsSaChallengeTimer_Type()
)
wmanIf2BsSaChallengeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSaChallengeTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSaChallengeTimer.setUnits("100milliseconds")


class _WmanIf2BsSaChallengeMaxResends_Type(Integer32):
    """Custom type wmanIf2BsSaChallengeMaxResends based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WmanIf2BsSaChallengeMaxResends_Type.__name__ = "Integer32"
_WmanIf2BsSaChallengeMaxResends_Object = MibTableColumn
wmanIf2BsSaChallengeMaxResends = _WmanIf2BsSaChallengeMaxResends_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 28),
    _WmanIf2BsSaChallengeMaxResends_Type()
)
wmanIf2BsSaChallengeMaxResends.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSaChallengeMaxResends.setStatus("current")


class _WmanIf2BsSaTekTimer_Type(Integer32):
    """Custom type wmanIf2BsSaTekTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_WmanIf2BsSaTekTimer_Type.__name__ = "Integer32"
_WmanIf2BsSaTekTimer_Object = MibTableColumn
wmanIf2BsSaTekTimer = _WmanIf2BsSaTekTimer_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 29),
    _WmanIf2BsSaTekTimer_Type()
)
wmanIf2BsSaTekTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSaTekTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSaTekTimer.setUnits("milliseconds")


class _WmanIf2BsSaTekReqMaxResends_Type(Integer32):
    """Custom type wmanIf2BsSaTekReqMaxResends based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WmanIf2BsSaTekReqMaxResends_Type.__name__ = "Integer32"
_WmanIf2BsSaTekReqMaxResends_Object = MibTableColumn
wmanIf2BsSaTekReqMaxResends = _WmanIf2BsSaTekReqMaxResends_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 30),
    _WmanIf2BsSaTekReqMaxResends_Type()
)
wmanIf2BsSaTekReqMaxResends.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSaTekReqMaxResends.setStatus("current")


class _WmanIf2Bs2ndEapTimeout_Type(Integer32):
    """Custom type wmanIf2Bs2ndEapTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_WmanIf2Bs2ndEapTimeout_Type.__name__ = "Integer32"
_WmanIf2Bs2ndEapTimeout_Object = MibTableColumn
wmanIf2Bs2ndEapTimeout = _WmanIf2Bs2ndEapTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 31),
    _WmanIf2Bs2ndEapTimeout_Type()
)
wmanIf2Bs2ndEapTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2Bs2ndEapTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2Bs2ndEapTimeout.setUnits("100milliseconds")


class _WmanIf2BsEapCompleteResends_Type(Integer32):
    """Custom type wmanIf2BsEapCompleteResends based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WmanIf2BsEapCompleteResends_Type.__name__ = "Integer32"
_WmanIf2BsEapCompleteResends_Object = MibTableColumn
wmanIf2BsEapCompleteResends = _WmanIf2BsEapCompleteResends_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 2, 1, 32),
    _WmanIf2BsEapCompleteResends_Type()
)
wmanIf2BsEapCompleteResends.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsEapCompleteResends.setStatus("current")
_WmanIf2BsChannelMeasurementTable_Object = MibTable
wmanIf2BsChannelMeasurementTable = _WmanIf2BsChannelMeasurementTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wmanIf2BsChannelMeasurementTable.setStatus("current")
_WmanIf2BsChannelMeasurementEntry_Object = MibTableRow
wmanIf2BsChannelMeasurementEntry = _WmanIf2BsChannelMeasurementEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 3, 1)
)
wmanIf2BsChannelMeasurementEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-MIB", "wmanIf2BsSsMacAddress"),
    (0, "WMAN-IF2-MIB", "wmanIf2BsChannelDirection"),
    (0, "WMAN-IF2-MIB", "wmanIf2BsHistogramIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsChannelMeasurementEntry.setStatus("current")


class _WmanIf2BsChannelDirection_Type(Integer32):
    """Custom type wmanIf2BsChannelDirection based on Integer32"""
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


_WmanIf2BsChannelDirection_Type.__name__ = "Integer32"
_WmanIf2BsChannelDirection_Object = MibTableColumn
wmanIf2BsChannelDirection = _WmanIf2BsChannelDirection_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 3, 1, 1),
    _WmanIf2BsChannelDirection_Type()
)
wmanIf2BsChannelDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsChannelDirection.setStatus("current")


class _WmanIf2BsHistogramIndex_Type(Unsigned32):
    """Custom type wmanIf2BsHistogramIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIf2BsHistogramIndex_Type.__name__ = "Unsigned32"
_WmanIf2BsHistogramIndex_Object = MibTableColumn
wmanIf2BsHistogramIndex = _WmanIf2BsHistogramIndex_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 3, 1, 2),
    _WmanIf2BsHistogramIndex_Type()
)
wmanIf2BsHistogramIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsHistogramIndex.setStatus("current")
_WmanIf2BsChannelNumber_Type = WmanIf2ChannelNumber
_WmanIf2BsChannelNumber_Object = MibTableColumn
wmanIf2BsChannelNumber = _WmanIf2BsChannelNumber_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 3, 1, 3),
    _WmanIf2BsChannelNumber_Type()
)
wmanIf2BsChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsChannelNumber.setStatus("current")


class _WmanIf2BsStartFrame_Type(Integer32):
    """Custom type wmanIf2BsStartFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsStartFrame_Type.__name__ = "Integer32"
_WmanIf2BsStartFrame_Object = MibTableColumn
wmanIf2BsStartFrame = _WmanIf2BsStartFrame_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 3, 1, 4),
    _WmanIf2BsStartFrame_Type()
)
wmanIf2BsStartFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsStartFrame.setStatus("current")


class _WmanIf2BsDuration_Type(Integer32):
    """Custom type wmanIf2BsDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_WmanIf2BsDuration_Type.__name__ = "Integer32"
_WmanIf2BsDuration_Object = MibTableColumn
wmanIf2BsDuration = _WmanIf2BsDuration_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 3, 1, 5),
    _WmanIf2BsDuration_Type()
)
wmanIf2BsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsDuration.setStatus("current")


class _WmanIf2BsBasicReport_Type(Bits):
    """Custom type wmanIf2BsBasicReport based on Bits"""
    namedValues = NamedValues(
        *(("wirelessHuman", 0),
          ("unknownTransmission", 1),
          ("primaryUser", 2),
          ("channelNotMeasured", 3))
    )

_WmanIf2BsBasicReport_Type.__name__ = "Bits"
_WmanIf2BsBasicReport_Object = MibTableColumn
wmanIf2BsBasicReport = _WmanIf2BsBasicReport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 3, 1, 6),
    _WmanIf2BsBasicReport_Type()
)
wmanIf2BsBasicReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsBasicReport.setStatus("current")


class _WmanIf2BsMeanCinrReport_Type(Integer32):
    """Custom type wmanIf2BsMeanCinrReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 37),
    )


_WmanIf2BsMeanCinrReport_Type.__name__ = "Integer32"
_WmanIf2BsMeanCinrReport_Object = MibTableColumn
wmanIf2BsMeanCinrReport = _WmanIf2BsMeanCinrReport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 3, 1, 7),
    _WmanIf2BsMeanCinrReport_Type()
)
wmanIf2BsMeanCinrReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsMeanCinrReport.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsMeanCinrReport.setUnits("dB")


class _WmanIf2BsMeanRssiReport_Type(Integer32):
    """Custom type wmanIf2BsMeanRssiReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-123, -40),
    )


_WmanIf2BsMeanRssiReport_Type.__name__ = "Integer32"
_WmanIf2BsMeanRssiReport_Object = MibTableColumn
wmanIf2BsMeanRssiReport = _WmanIf2BsMeanRssiReport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 3, 1, 8),
    _WmanIf2BsMeanRssiReport_Type()
)
wmanIf2BsMeanRssiReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsMeanRssiReport.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsMeanRssiReport.setUnits("dBm")


class _WmanIf2BsStdDeviationCinrReport_Type(Integer32):
    """Custom type wmanIf2BsStdDeviationCinrReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_WmanIf2BsStdDeviationCinrReport_Type.__name__ = "Integer32"
_WmanIf2BsStdDeviationCinrReport_Object = MibTableColumn
wmanIf2BsStdDeviationCinrReport = _WmanIf2BsStdDeviationCinrReport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 3, 1, 9),
    _WmanIf2BsStdDeviationCinrReport_Type()
)
wmanIf2BsStdDeviationCinrReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsStdDeviationCinrReport.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsStdDeviationCinrReport.setUnits("dB")


class _WmanIf2BsStdDeviationRssiReport_Type(Integer32):
    """Custom type wmanIf2BsStdDeviationRssiReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 42),
    )


_WmanIf2BsStdDeviationRssiReport_Type.__name__ = "Integer32"
_WmanIf2BsStdDeviationRssiReport_Object = MibTableColumn
wmanIf2BsStdDeviationRssiReport = _WmanIf2BsStdDeviationRssiReport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 3, 1, 10),
    _WmanIf2BsStdDeviationRssiReport_Type()
)
wmanIf2BsStdDeviationRssiReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsStdDeviationRssiReport.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsStdDeviationRssiReport.setUnits("dB")
_WmanIf2BsCapabilities_ObjectIdentity = ObjectIdentity
wmanIf2BsCapabilities = _WmanIf2BsCapabilities_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4)
)
_WmanIf2BsBasicCapabilitiesTable_Object = MibTable
wmanIf2BsBasicCapabilitiesTable = _WmanIf2BsBasicCapabilitiesTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3)
)
if mibBuilder.loadTexts:
    wmanIf2BsBasicCapabilitiesTable.setStatus("current")
_WmanIf2BsBasicCapabilitiesEntry_Object = MibTableRow
wmanIf2BsBasicCapabilitiesEntry = _WmanIf2BsBasicCapabilitiesEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1)
)
wmanIf2BsBasicCapabilitiesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsBasicCapabilitiesEntry.setStatus("current")
_WmanIf2BsCapUplinkCidSupport_Type = WmanIf2NumOfCid
_WmanIf2BsCapUplinkCidSupport_Object = MibTableColumn
wmanIf2BsCapUplinkCidSupport = _WmanIf2BsCapUplinkCidSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 1),
    _WmanIf2BsCapUplinkCidSupport_Type()
)
wmanIf2BsCapUplinkCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapUplinkCidSupport.setStatus("current")
_WmanIf2BsCapArqSupport_Type = WmanIf2ArqSupportType
_WmanIf2BsCapArqSupport_Object = MibTableColumn
wmanIf2BsCapArqSupport = _WmanIf2BsCapArqSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 2),
    _WmanIf2BsCapArqSupport_Type()
)
wmanIf2BsCapArqSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapArqSupport.setStatus("current")
_WmanIf2BsCapDsxFlowControl_Type = WmanIf2MaxDsxFlowType
_WmanIf2BsCapDsxFlowControl_Object = MibTableColumn
wmanIf2BsCapDsxFlowControl = _WmanIf2BsCapDsxFlowControl_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 3),
    _WmanIf2BsCapDsxFlowControl_Type()
)
wmanIf2BsCapDsxFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapDsxFlowControl.setStatus("current")
_WmanIf2BsCapMacCrcSupport_Type = WmanIf2MacCrcSupport
_WmanIf2BsCapMacCrcSupport_Object = MibTableColumn
wmanIf2BsCapMacCrcSupport = _WmanIf2BsCapMacCrcSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 4),
    _WmanIf2BsCapMacCrcSupport_Type()
)
wmanIf2BsCapMacCrcSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapMacCrcSupport.setStatus("current")
_WmanIf2BsCapMcaFlowControl_Type = WmanIf2MaxMcaFlowType
_WmanIf2BsCapMcaFlowControl_Object = MibTableColumn
wmanIf2BsCapMcaFlowControl = _WmanIf2BsCapMcaFlowControl_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 5),
    _WmanIf2BsCapMcaFlowControl_Type()
)
wmanIf2BsCapMcaFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapMcaFlowControl.setStatus("current")
_WmanIf2BsCapMcpGroupCidSupport_Type = WmanIf2MaxMcpGroupCid
_WmanIf2BsCapMcpGroupCidSupport_Object = MibTableColumn
wmanIf2BsCapMcpGroupCidSupport = _WmanIf2BsCapMcpGroupCidSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 6),
    _WmanIf2BsCapMcpGroupCidSupport_Type()
)
wmanIf2BsCapMcpGroupCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapMcpGroupCidSupport.setStatus("current")
_WmanIf2BsCapPkmFlowControl_Type = WmanIf2MaxPkmFlowType
_WmanIf2BsCapPkmFlowControl_Object = MibTableColumn
wmanIf2BsCapPkmFlowControl = _WmanIf2BsCapPkmFlowControl_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 7),
    _WmanIf2BsCapPkmFlowControl_Type()
)
wmanIf2BsCapPkmFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapPkmFlowControl.setStatus("current")
_WmanIf2BsCapAuthPolicyControl_Type = WmanIf2AuthPolicyType
_WmanIf2BsCapAuthPolicyControl_Object = MibTableColumn
wmanIf2BsCapAuthPolicyControl = _WmanIf2BsCapAuthPolicyControl_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 8),
    _WmanIf2BsCapAuthPolicyControl_Type()
)
wmanIf2BsCapAuthPolicyControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapAuthPolicyControl.setStatus("current")
_WmanIf2BsCapMaxNumOfSupportedSA_Type = WmanIf2MaxNumOfSaType
_WmanIf2BsCapMaxNumOfSupportedSA_Object = MibTableColumn
wmanIf2BsCapMaxNumOfSupportedSA = _WmanIf2BsCapMaxNumOfSupportedSA_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 9),
    _WmanIf2BsCapMaxNumOfSupportedSA_Type()
)
wmanIf2BsCapMaxNumOfSupportedSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapMaxNumOfSupportedSA.setStatus("current")
_WmanIf2BsCapIpVersion_Type = WmanIf2IpVersionType
_WmanIf2BsCapIpVersion_Object = MibTableColumn
wmanIf2BsCapIpVersion = _WmanIf2BsCapIpVersion_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 10),
    _WmanIf2BsCapIpVersion_Type()
)
wmanIf2BsCapIpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapIpVersion.setStatus("current")
_WmanIf2BsCapMacCsSupportBitMap_Type = WmanIf2MacCsBitMap
_WmanIf2BsCapMacCsSupportBitMap_Object = MibTableColumn
wmanIf2BsCapMacCsSupportBitMap = _WmanIf2BsCapMacCsSupportBitMap_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 11),
    _WmanIf2BsCapMacCsSupportBitMap_Type()
)
wmanIf2BsCapMacCsSupportBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapMacCsSupportBitMap.setStatus("current")
_WmanIf2BsCapMaxNumOfClassifier_Type = WmanIf2MaxClassifiers
_WmanIf2BsCapMaxNumOfClassifier_Object = MibTableColumn
wmanIf2BsCapMaxNumOfClassifier = _WmanIf2BsCapMaxNumOfClassifier_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 12),
    _WmanIf2BsCapMaxNumOfClassifier_Type()
)
wmanIf2BsCapMaxNumOfClassifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapMaxNumOfClassifier.setStatus("current")
_WmanIf2BsCapPhsSupport_Type = WmanIf2PhsSupportType
_WmanIf2BsCapPhsSupport_Object = MibTableColumn
wmanIf2BsCapPhsSupport = _WmanIf2BsCapPhsSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 13),
    _WmanIf2BsCapPhsSupport_Type()
)
wmanIf2BsCapPhsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapPhsSupport.setStatus("current")
_WmanIf2BsCapBandwidthAllocSupport_Type = WmanIf2BwAllocSupport
_WmanIf2BsCapBandwidthAllocSupport_Object = MibTableColumn
wmanIf2BsCapBandwidthAllocSupport = _WmanIf2BsCapBandwidthAllocSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 14),
    _WmanIf2BsCapBandwidthAllocSupport_Type()
)
wmanIf2BsCapBandwidthAllocSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapBandwidthAllocSupport.setStatus("current")
_WmanIf2BsCapPduConstruction_Type = WmanIf2PduConstruction
_WmanIf2BsCapPduConstruction_Object = MibTableColumn
wmanIf2BsCapPduConstruction = _WmanIf2BsCapPduConstruction_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 15),
    _WmanIf2BsCapPduConstruction_Type()
)
wmanIf2BsCapPduConstruction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapPduConstruction.setStatus("current")
_WmanIf2BsCapTtgTransitionGap_Type = WmanIf2SsTransitionGap
_WmanIf2BsCapTtgTransitionGap_Object = MibTableColumn
wmanIf2BsCapTtgTransitionGap = _WmanIf2BsCapTtgTransitionGap_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 16),
    _WmanIf2BsCapTtgTransitionGap_Type()
)
wmanIf2BsCapTtgTransitionGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapTtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsCapTtgTransitionGap.setUnits("us")
_WmanIf2BsCapRtgTransitionGap_Type = WmanIf2SsTransitionGap
_WmanIf2BsCapRtgTransitionGap_Object = MibTableColumn
wmanIf2BsCapRtgTransitionGap = _WmanIf2BsCapRtgTransitionGap_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 17),
    _WmanIf2BsCapRtgTransitionGap_Type()
)
wmanIf2BsCapRtgTransitionGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapRtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsCapRtgTransitionGap.setUnits("us")
_WmanIf2BsCapDownlinkCidSupport_Type = WmanIf2NumOfCid
_WmanIf2BsCapDownlinkCidSupport_Object = MibTableColumn
wmanIf2BsCapDownlinkCidSupport = _WmanIf2BsCapDownlinkCidSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 18),
    _WmanIf2BsCapDownlinkCidSupport_Type()
)
wmanIf2BsCapDownlinkCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapDownlinkCidSupport.setStatus("current")
_WmanIf2BsCapPackingSupport_Type = WmanIf2PackingSupport
_WmanIf2BsCapPackingSupport_Object = MibTableColumn
wmanIf2BsCapPackingSupport = _WmanIf2BsCapPackingSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 19),
    _WmanIf2BsCapPackingSupport_Type()
)
wmanIf2BsCapPackingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapPackingSupport.setStatus("current")
_WmanIf2BsCapExtendedRtpsSupport_Type = WmanIf2ExtRtpsSupport
_WmanIf2BsCapExtendedRtpsSupport_Object = MibTableColumn
wmanIf2BsCapExtendedRtpsSupport = _WmanIf2BsCapExtendedRtpsSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 20),
    _WmanIf2BsCapExtendedRtpsSupport_Type()
)
wmanIf2BsCapExtendedRtpsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapExtendedRtpsSupport.setStatus("current")


class _WmanIf2BsCapMaxNumBurstToMs_Type(Integer32):
    """Custom type wmanIf2BsCapMaxNumBurstToMs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WmanIf2BsCapMaxNumBurstToMs_Type.__name__ = "Integer32"
_WmanIf2BsCapMaxNumBurstToMs_Object = MibTableColumn
wmanIf2BsCapMaxNumBurstToMs = _WmanIf2BsCapMaxNumBurstToMs_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 21),
    _WmanIf2BsCapMaxNumBurstToMs_Type()
)
wmanIf2BsCapMaxNumBurstToMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapMaxNumBurstToMs.setStatus("current")
_WmanIf2BsCapIpAddrAllocMethod_Type = WmanIf2IpAllocMethod
_WmanIf2BsCapIpAddrAllocMethod_Object = MibTableColumn
wmanIf2BsCapIpAddrAllocMethod = _WmanIf2BsCapIpAddrAllocMethod_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 22),
    _WmanIf2BsCapIpAddrAllocMethod_Type()
)
wmanIf2BsCapIpAddrAllocMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapIpAddrAllocMethod.setStatus("current")
_WmanIf2BsCapArqAckType_Type = WmanIf2ArqAckType
_WmanIf2BsCapArqAckType_Object = MibTableColumn
wmanIf2BsCapArqAckType = _WmanIf2BsCapArqAckType_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 23),
    _WmanIf2BsCapArqAckType_Type()
)
wmanIf2BsCapArqAckType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapArqAckType.setStatus("current")
_WmanIf2BsCapMacHeader_Type = WmanIf2MacHeaderSupp
_WmanIf2BsCapMacHeader_Object = MibTableColumn
wmanIf2BsCapMacHeader = _WmanIf2BsCapMacHeader_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 24),
    _WmanIf2BsCapMacHeader_Type()
)
wmanIf2BsCapMacHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapMacHeader.setStatus("current")
_WmanIf2BsCapMaxMacLevelDlFrame_Type = WmanIf2MaxMacLevel
_WmanIf2BsCapMaxMacLevelDlFrame_Object = MibTableColumn
wmanIf2BsCapMaxMacLevelDlFrame = _WmanIf2BsCapMaxMacLevelDlFrame_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 25),
    _WmanIf2BsCapMaxMacLevelDlFrame_Type()
)
wmanIf2BsCapMaxMacLevelDlFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapMaxMacLevelDlFrame.setStatus("current")
_WmanIf2BsCapMaxMacLevelUlFrame_Type = WmanIf2MaxMacLevel
_WmanIf2BsCapMaxMacLevelUlFrame_Object = MibTableColumn
wmanIf2BsCapMaxMacLevelUlFrame = _WmanIf2BsCapMaxMacLevelUlFrame_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 26),
    _WmanIf2BsCapMaxMacLevelUlFrame_Type()
)
wmanIf2BsCapMaxMacLevelUlFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapMaxMacLevelUlFrame.setStatus("current")


class _WmanIf2BsCapNumOfProvisionedSf_Type(Unsigned32):
    """Custom type wmanIf2BsCapNumOfProvisionedSf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsCapNumOfProvisionedSf_Type.__name__ = "Unsigned32"
_WmanIf2BsCapNumOfProvisionedSf_Object = MibTableColumn
wmanIf2BsCapNumOfProvisionedSf = _WmanIf2BsCapNumOfProvisionedSf_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 27),
    _WmanIf2BsCapNumOfProvisionedSf_Type()
)
wmanIf2BsCapNumOfProvisionedSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapNumOfProvisionedSf.setStatus("current")
_WmanIf2BsCapPkmVersion_Type = WmanIf2PkmVersion
_WmanIf2BsCapPkmVersion_Object = MibTableColumn
wmanIf2BsCapPkmVersion = _WmanIf2BsCapPkmVersion_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 28),
    _WmanIf2BsCapPkmVersion_Type()
)
wmanIf2BsCapPkmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapPkmVersion.setStatus("current")
_WmanIf2BsCapAuthPolicy_Type = WmanIf2AuthPolicy
_WmanIf2BsCapAuthPolicy_Object = MibTableColumn
wmanIf2BsCapAuthPolicy = _WmanIf2BsCapAuthPolicy_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 29),
    _WmanIf2BsCapAuthPolicy_Type()
)
wmanIf2BsCapAuthPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapAuthPolicy.setStatus("current")
_WmanIf2BsCapMacMode_Type = WmanIf2MacMode
_WmanIf2BsCapMacMode_Object = MibTableColumn
wmanIf2BsCapMacMode = _WmanIf2BsCapMacMode_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 30),
    _WmanIf2BsCapMacMode_Type()
)
wmanIf2BsCapMacMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapMacMode.setStatus("current")


class _WmanIf2BsCapPnWindowSize_Type(Integer32):
    """Custom type wmanIf2BsCapPnWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsCapPnWindowSize_Type.__name__ = "Integer32"
_WmanIf2BsCapPnWindowSize_Object = MibTableColumn
wmanIf2BsCapPnWindowSize = _WmanIf2BsCapPnWindowSize_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 31),
    _WmanIf2BsCapPnWindowSize_Type()
)
wmanIf2BsCapPnWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapPnWindowSize.setStatus("current")
_WmanIf2BsCapExtCapability_Type = WmanIf2ExtCapability
_WmanIf2BsCapExtCapability_Object = MibTableColumn
wmanIf2BsCapExtCapability = _WmanIf2BsCapExtCapability_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 3, 1, 32),
    _WmanIf2BsCapExtCapability_Type()
)
wmanIf2BsCapExtCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapExtCapability.setStatus("current")
_WmanIf2BsCapabilitiesConfigTable_Object = MibTable
wmanIf2BsCapabilitiesConfigTable = _WmanIf2BsCapabilitiesConfigTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4)
)
if mibBuilder.loadTexts:
    wmanIf2BsCapabilitiesConfigTable.setStatus("current")
_WmanIf2BsCapabilitiesConfigEntry_Object = MibTableRow
wmanIf2BsCapabilitiesConfigEntry = _WmanIf2BsCapabilitiesConfigEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1)
)
wmanIf2BsCapabilitiesConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsCapabilitiesConfigEntry.setStatus("current")
_WmanIf2BsCapCfgUplinkCidSupport_Type = WmanIf2NumOfCid
_WmanIf2BsCapCfgUplinkCidSupport_Object = MibTableColumn
wmanIf2BsCapCfgUplinkCidSupport = _WmanIf2BsCapCfgUplinkCidSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 1),
    _WmanIf2BsCapCfgUplinkCidSupport_Type()
)
wmanIf2BsCapCfgUplinkCidSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgUplinkCidSupport.setStatus("current")
_WmanIf2BsCapCfgArqSupport_Type = WmanIf2ArqSupportType
_WmanIf2BsCapCfgArqSupport_Object = MibTableColumn
wmanIf2BsCapCfgArqSupport = _WmanIf2BsCapCfgArqSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 2),
    _WmanIf2BsCapCfgArqSupport_Type()
)
wmanIf2BsCapCfgArqSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgArqSupport.setStatus("current")
_WmanIf2BsCapCfgDsxFlowControl_Type = WmanIf2MaxDsxFlowType
_WmanIf2BsCapCfgDsxFlowControl_Object = MibTableColumn
wmanIf2BsCapCfgDsxFlowControl = _WmanIf2BsCapCfgDsxFlowControl_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 3),
    _WmanIf2BsCapCfgDsxFlowControl_Type()
)
wmanIf2BsCapCfgDsxFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgDsxFlowControl.setStatus("current")
_WmanIf2BsCapCfgMacCrcSupport_Type = WmanIf2MacCrcSupport
_WmanIf2BsCapCfgMacCrcSupport_Object = MibTableColumn
wmanIf2BsCapCfgMacCrcSupport = _WmanIf2BsCapCfgMacCrcSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 4),
    _WmanIf2BsCapCfgMacCrcSupport_Type()
)
wmanIf2BsCapCfgMacCrcSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgMacCrcSupport.setStatus("current")
_WmanIf2BsCapCfgMcaFlowControl_Type = WmanIf2MaxMcaFlowType
_WmanIf2BsCapCfgMcaFlowControl_Object = MibTableColumn
wmanIf2BsCapCfgMcaFlowControl = _WmanIf2BsCapCfgMcaFlowControl_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 5),
    _WmanIf2BsCapCfgMcaFlowControl_Type()
)
wmanIf2BsCapCfgMcaFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgMcaFlowControl.setStatus("current")
_WmanIf2BsCapCfgMcpGroupCidSupport_Type = WmanIf2MaxMcpGroupCid
_WmanIf2BsCapCfgMcpGroupCidSupport_Object = MibTableColumn
wmanIf2BsCapCfgMcpGroupCidSupport = _WmanIf2BsCapCfgMcpGroupCidSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 6),
    _WmanIf2BsCapCfgMcpGroupCidSupport_Type()
)
wmanIf2BsCapCfgMcpGroupCidSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgMcpGroupCidSupport.setStatus("current")
_WmanIf2BsCapCfgPkmFlowControl_Type = WmanIf2MaxPkmFlowType
_WmanIf2BsCapCfgPkmFlowControl_Object = MibTableColumn
wmanIf2BsCapCfgPkmFlowControl = _WmanIf2BsCapCfgPkmFlowControl_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 7),
    _WmanIf2BsCapCfgPkmFlowControl_Type()
)
wmanIf2BsCapCfgPkmFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgPkmFlowControl.setStatus("current")
_WmanIf2BsCapCfgAuthPolicyControl_Type = WmanIf2AuthPolicyType
_WmanIf2BsCapCfgAuthPolicyControl_Object = MibTableColumn
wmanIf2BsCapCfgAuthPolicyControl = _WmanIf2BsCapCfgAuthPolicyControl_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 8),
    _WmanIf2BsCapCfgAuthPolicyControl_Type()
)
wmanIf2BsCapCfgAuthPolicyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgAuthPolicyControl.setStatus("current")
_WmanIf2BsCapCfgMaxNumOfSupportedSA_Type = WmanIf2MaxNumOfSaType
_WmanIf2BsCapCfgMaxNumOfSupportedSA_Object = MibTableColumn
wmanIf2BsCapCfgMaxNumOfSupportedSA = _WmanIf2BsCapCfgMaxNumOfSupportedSA_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 9),
    _WmanIf2BsCapCfgMaxNumOfSupportedSA_Type()
)
wmanIf2BsCapCfgMaxNumOfSupportedSA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgMaxNumOfSupportedSA.setStatus("current")
_WmanIf2BsCapCfgIpVersion_Type = WmanIf2IpVersionType
_WmanIf2BsCapCfgIpVersion_Object = MibTableColumn
wmanIf2BsCapCfgIpVersion = _WmanIf2BsCapCfgIpVersion_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 10),
    _WmanIf2BsCapCfgIpVersion_Type()
)
wmanIf2BsCapCfgIpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgIpVersion.setStatus("current")
_WmanIf2BsCapCfgMacCsSupportBitMap_Type = WmanIf2MacCsBitMap
_WmanIf2BsCapCfgMacCsSupportBitMap_Object = MibTableColumn
wmanIf2BsCapCfgMacCsSupportBitMap = _WmanIf2BsCapCfgMacCsSupportBitMap_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 11),
    _WmanIf2BsCapCfgMacCsSupportBitMap_Type()
)
wmanIf2BsCapCfgMacCsSupportBitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgMacCsSupportBitMap.setStatus("current")
_WmanIf2BsCapCfgMaxNumOfClassifier_Type = WmanIf2MaxClassifiers
_WmanIf2BsCapCfgMaxNumOfClassifier_Object = MibTableColumn
wmanIf2BsCapCfgMaxNumOfClassifier = _WmanIf2BsCapCfgMaxNumOfClassifier_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 12),
    _WmanIf2BsCapCfgMaxNumOfClassifier_Type()
)
wmanIf2BsCapCfgMaxNumOfClassifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgMaxNumOfClassifier.setStatus("current")
_WmanIf2BsCapCfgPhsSupport_Type = WmanIf2PhsSupportType
_WmanIf2BsCapCfgPhsSupport_Object = MibTableColumn
wmanIf2BsCapCfgPhsSupport = _WmanIf2BsCapCfgPhsSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 13),
    _WmanIf2BsCapCfgPhsSupport_Type()
)
wmanIf2BsCapCfgPhsSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgPhsSupport.setStatus("current")
_WmanIf2BsCapCfgBandwidthAllocSupport_Type = WmanIf2BwAllocSupport
_WmanIf2BsCapCfgBandwidthAllocSupport_Object = MibTableColumn
wmanIf2BsCapCfgBandwidthAllocSupport = _WmanIf2BsCapCfgBandwidthAllocSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 14),
    _WmanIf2BsCapCfgBandwidthAllocSupport_Type()
)
wmanIf2BsCapCfgBandwidthAllocSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgBandwidthAllocSupport.setStatus("current")
_WmanIf2BsCapCfgPduConstruction_Type = WmanIf2PduConstruction
_WmanIf2BsCapCfgPduConstruction_Object = MibTableColumn
wmanIf2BsCapCfgPduConstruction = _WmanIf2BsCapCfgPduConstruction_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 15),
    _WmanIf2BsCapCfgPduConstruction_Type()
)
wmanIf2BsCapCfgPduConstruction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgPduConstruction.setStatus("current")
_WmanIf2BsCapCfgTtgTransitionGap_Type = WmanIf2SsTransitionGap
_WmanIf2BsCapCfgTtgTransitionGap_Object = MibTableColumn
wmanIf2BsCapCfgTtgTransitionGap = _WmanIf2BsCapCfgTtgTransitionGap_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 16),
    _WmanIf2BsCapCfgTtgTransitionGap_Type()
)
wmanIf2BsCapCfgTtgTransitionGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgTtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgTtgTransitionGap.setUnits("us")
_WmanIf2BsCapCfgRtgTransitionGap_Type = WmanIf2SsTransitionGap
_WmanIf2BsCapCfgRtgTransitionGap_Object = MibTableColumn
wmanIf2BsCapCfgRtgTransitionGap = _WmanIf2BsCapCfgRtgTransitionGap_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 17),
    _WmanIf2BsCapCfgRtgTransitionGap_Type()
)
wmanIf2BsCapCfgRtgTransitionGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgRtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgRtgTransitionGap.setUnits("us")
_WmanIf2BsCapCfgDownlinkCidSupport_Type = WmanIf2NumOfCid
_WmanIf2BsCapCfgDownlinkCidSupport_Object = MibTableColumn
wmanIf2BsCapCfgDownlinkCidSupport = _WmanIf2BsCapCfgDownlinkCidSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 18),
    _WmanIf2BsCapCfgDownlinkCidSupport_Type()
)
wmanIf2BsCapCfgDownlinkCidSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgDownlinkCidSupport.setStatus("current")
_WmanIf2BsCapCfgPackingSupport_Type = WmanIf2PackingSupport
_WmanIf2BsCapCfgPackingSupport_Object = MibTableColumn
wmanIf2BsCapCfgPackingSupport = _WmanIf2BsCapCfgPackingSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 19),
    _WmanIf2BsCapCfgPackingSupport_Type()
)
wmanIf2BsCapCfgPackingSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgPackingSupport.setStatus("current")
_WmanIf2BsCapCfgExtendedRtpsSupport_Type = WmanIf2ExtRtpsSupport
_WmanIf2BsCapCfgExtendedRtpsSupport_Object = MibTableColumn
wmanIf2BsCapCfgExtendedRtpsSupport = _WmanIf2BsCapCfgExtendedRtpsSupport_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 20),
    _WmanIf2BsCapCfgExtendedRtpsSupport_Type()
)
wmanIf2BsCapCfgExtendedRtpsSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgExtendedRtpsSupport.setStatus("current")


class _WmanIf2BsCapCfgMaxNumBurstToMs_Type(Integer32):
    """Custom type wmanIf2BsCapCfgMaxNumBurstToMs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WmanIf2BsCapCfgMaxNumBurstToMs_Type.__name__ = "Integer32"
_WmanIf2BsCapCfgMaxNumBurstToMs_Object = MibTableColumn
wmanIf2BsCapCfgMaxNumBurstToMs = _WmanIf2BsCapCfgMaxNumBurstToMs_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 21),
    _WmanIf2BsCapCfgMaxNumBurstToMs_Type()
)
wmanIf2BsCapCfgMaxNumBurstToMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgMaxNumBurstToMs.setStatus("current")
_WmanIf2BsCapCfgIpAddrAllocMethod_Type = WmanIf2IpAllocMethod
_WmanIf2BsCapCfgIpAddrAllocMethod_Object = MibTableColumn
wmanIf2BsCapCfgIpAddrAllocMethod = _WmanIf2BsCapCfgIpAddrAllocMethod_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 22),
    _WmanIf2BsCapCfgIpAddrAllocMethod_Type()
)
wmanIf2BsCapCfgIpAddrAllocMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgIpAddrAllocMethod.setStatus("current")
_WmanIf2BsCapCfgArqAckType_Type = WmanIf2ArqAckType
_WmanIf2BsCapCfgArqAckType_Object = MibTableColumn
wmanIf2BsCapCfgArqAckType = _WmanIf2BsCapCfgArqAckType_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 23),
    _WmanIf2BsCapCfgArqAckType_Type()
)
wmanIf2BsCapCfgArqAckType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgArqAckType.setStatus("current")
_WmanIf2BsCapCfgMacHeader_Type = WmanIf2MacHeaderSupp
_WmanIf2BsCapCfgMacHeader_Object = MibTableColumn
wmanIf2BsCapCfgMacHeader = _WmanIf2BsCapCfgMacHeader_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 24),
    _WmanIf2BsCapCfgMacHeader_Type()
)
wmanIf2BsCapCfgMacHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgMacHeader.setStatus("current")
_WmanIf2BsCapCfgMaxMacLevelDlFrame_Type = WmanIf2MaxMacLevel
_WmanIf2BsCapCfgMaxMacLevelDlFrame_Object = MibTableColumn
wmanIf2BsCapCfgMaxMacLevelDlFrame = _WmanIf2BsCapCfgMaxMacLevelDlFrame_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 25),
    _WmanIf2BsCapCfgMaxMacLevelDlFrame_Type()
)
wmanIf2BsCapCfgMaxMacLevelDlFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgMaxMacLevelDlFrame.setStatus("current")
_WmanIf2BsCapCfgMaxMacLevelUlFrame_Type = WmanIf2MaxMacLevel
_WmanIf2BsCapCfgMaxMacLevelUlFrame_Object = MibTableColumn
wmanIf2BsCapCfgMaxMacLevelUlFrame = _WmanIf2BsCapCfgMaxMacLevelUlFrame_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 26),
    _WmanIf2BsCapCfgMaxMacLevelUlFrame_Type()
)
wmanIf2BsCapCfgMaxMacLevelUlFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgMaxMacLevelUlFrame.setStatus("current")


class _WmanIf2BsCapCfgNumOfProvisionedSf_Type(Unsigned32):
    """Custom type wmanIf2BsCapCfgNumOfProvisionedSf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsCapCfgNumOfProvisionedSf_Type.__name__ = "Unsigned32"
_WmanIf2BsCapCfgNumOfProvisionedSf_Object = MibTableColumn
wmanIf2BsCapCfgNumOfProvisionedSf = _WmanIf2BsCapCfgNumOfProvisionedSf_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 27),
    _WmanIf2BsCapCfgNumOfProvisionedSf_Type()
)
wmanIf2BsCapCfgNumOfProvisionedSf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgNumOfProvisionedSf.setStatus("current")
_WmanIf2BsCapCfgPkmVersion_Type = WmanIf2PkmVersion
_WmanIf2BsCapCfgPkmVersion_Object = MibTableColumn
wmanIf2BsCapCfgPkmVersion = _WmanIf2BsCapCfgPkmVersion_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 28),
    _WmanIf2BsCapCfgPkmVersion_Type()
)
wmanIf2BsCapCfgPkmVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgPkmVersion.setStatus("current")
_WmanIf2BsCapCfgAuthPolicy_Type = WmanIf2AuthPolicy
_WmanIf2BsCapCfgAuthPolicy_Object = MibTableColumn
wmanIf2BsCapCfgAuthPolicy = _WmanIf2BsCapCfgAuthPolicy_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 29),
    _WmanIf2BsCapCfgAuthPolicy_Type()
)
wmanIf2BsCapCfgAuthPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgAuthPolicy.setStatus("current")
_WmanIf2BsCapCfgMacMode_Type = WmanIf2MacMode
_WmanIf2BsCapCfgMacMode_Object = MibTableColumn
wmanIf2BsCapCfgMacMode = _WmanIf2BsCapCfgMacMode_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 30),
    _WmanIf2BsCapCfgMacMode_Type()
)
wmanIf2BsCapCfgMacMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgMacMode.setStatus("current")


class _WmanIf2BsCapCfgPnWindowSize_Type(Integer32):
    """Custom type wmanIf2BsCapCfgPnWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsCapCfgPnWindowSize_Type.__name__ = "Integer32"
_WmanIf2BsCapCfgPnWindowSize_Object = MibTableColumn
wmanIf2BsCapCfgPnWindowSize = _WmanIf2BsCapCfgPnWindowSize_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 31),
    _WmanIf2BsCapCfgPnWindowSize_Type()
)
wmanIf2BsCapCfgPnWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgPnWindowSize.setStatus("current")
_WmanIf2BsCapCfgExtCapability_Type = WmanIf2ExtCapability
_WmanIf2BsCapCfgExtCapability_Object = MibTableColumn
wmanIf2BsCapCfgExtCapability = _WmanIf2BsCapCfgExtCapability_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 4, 4, 1, 32),
    _WmanIf2BsCapCfgExtCapability_Type()
)
wmanIf2BsCapCfgExtCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgExtCapability.setStatus("current")
_WmanIf2BsSsActionsTable_Object = MibTable
wmanIf2BsSsActionsTable = _WmanIf2BsSsActionsTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsActionsTable.setStatus("current")
_WmanIf2BsSsActionsEntry_Object = MibTableRow
wmanIf2BsSsActionsEntry = _WmanIf2BsSsActionsEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 5, 1)
)
wmanIf2BsSsActionsEntry.setIndexNames(
    (0, "WMAN-IF2-MIB", "wmanIf2BsSsActionsMacAddress"),
)
if mibBuilder.loadTexts:
    wmanIf2BsSsActionsEntry.setStatus("current")
_WmanIf2BsSsActionsMacAddress_Type = MacAddress
_WmanIf2BsSsActionsMacAddress_Object = MibTableColumn
wmanIf2BsSsActionsMacAddress = _WmanIf2BsSsActionsMacAddress_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 5, 1, 1),
    _WmanIf2BsSsActionsMacAddress_Type()
)
wmanIf2BsSsActionsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsSsActionsMacAddress.setStatus("current")


class _WmanIf2BsSsActionsResetSs_Type(Integer32):
    """Custom type wmanIf2BsSsActionsResetSs based on Integer32"""
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


_WmanIf2BsSsActionsResetSs_Type.__name__ = "Integer32"
_WmanIf2BsSsActionsResetSs_Object = MibTableColumn
wmanIf2BsSsActionsResetSs = _WmanIf2BsSsActionsResetSs_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 5, 1, 2),
    _WmanIf2BsSsActionsResetSs_Type()
)
wmanIf2BsSsActionsResetSs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsSsActionsResetSs.setStatus("current")


class _WmanIf2BsSsActionsAbortSs_Type(Integer32):
    """Custom type wmanIf2BsSsActionsAbortSs based on Integer32"""
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


_WmanIf2BsSsActionsAbortSs_Type.__name__ = "Integer32"
_WmanIf2BsSsActionsAbortSs_Object = MibTableColumn
wmanIf2BsSsActionsAbortSs = _WmanIf2BsSsActionsAbortSs_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 5, 1, 3),
    _WmanIf2BsSsActionsAbortSs_Type()
)
wmanIf2BsSsActionsAbortSs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsSsActionsAbortSs.setStatus("current")
_WmanIf2BsSsActionsOverrideDnFreq_Type = Unsigned32
_WmanIf2BsSsActionsOverrideDnFreq_Object = MibTableColumn
wmanIf2BsSsActionsOverrideDnFreq = _WmanIf2BsSsActionsOverrideDnFreq_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 5, 1, 4),
    _WmanIf2BsSsActionsOverrideDnFreq_Type()
)
wmanIf2BsSsActionsOverrideDnFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsSsActionsOverrideDnFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSsActionsOverrideDnFreq.setUnits("kHz")


class _WmanIf2BsSsActionsOverrideChannelId_Type(Integer32):
    """Custom type wmanIf2BsSsActionsOverrideChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_WmanIf2BsSsActionsOverrideChannelId_Type.__name__ = "Integer32"
_WmanIf2BsSsActionsOverrideChannelId_Object = MibTableColumn
wmanIf2BsSsActionsOverrideChannelId = _WmanIf2BsSsActionsOverrideChannelId_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 5, 1, 5),
    _WmanIf2BsSsActionsOverrideChannelId_Type()
)
wmanIf2BsSsActionsOverrideChannelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsSsActionsOverrideChannelId.setStatus("current")


class _WmanIf2BsSsActionsDeReRegSs_Type(Integer32):
    """Custom type wmanIf2BsSsActionsDeReRegSs based on Integer32"""
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


_WmanIf2BsSsActionsDeReRegSs_Type.__name__ = "Integer32"
_WmanIf2BsSsActionsDeReRegSs_Object = MibTableColumn
wmanIf2BsSsActionsDeReRegSs = _WmanIf2BsSsActionsDeReRegSs_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 5, 1, 6),
    _WmanIf2BsSsActionsDeReRegSs_Type()
)
wmanIf2BsSsActionsDeReRegSs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsSsActionsDeReRegSs.setStatus("current")


class _WmanIf2BsSsActionsDeReRegSsCode_Type(Integer32):
    """Custom type wmanIf2BsSsActionsDeReRegSsCode based on Integer32"""
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


_WmanIf2BsSsActionsDeReRegSsCode_Type.__name__ = "Integer32"
_WmanIf2BsSsActionsDeReRegSsCode_Object = MibTableColumn
wmanIf2BsSsActionsDeReRegSsCode = _WmanIf2BsSsActionsDeReRegSsCode_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 5, 1, 7),
    _WmanIf2BsSsActionsDeReRegSsCode_Type()
)
wmanIf2BsSsActionsDeReRegSsCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsSsActionsDeReRegSsCode.setStatus("current")
_WmanIf2BsSsActionsRowStatus_Type = RowStatus
_WmanIf2BsSsActionsRowStatus_Object = MibTableColumn
wmanIf2BsSsActionsRowStatus = _WmanIf2BsSsActionsRowStatus_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 5, 1, 8),
    _WmanIf2BsSsActionsRowStatus_Type()
)
wmanIf2BsSsActionsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsSsActionsRowStatus.setStatus("current")
_WmanIf2BsPkmObjects_ObjectIdentity = ObjectIdentity
wmanIf2BsPkmObjects = _WmanIf2BsPkmObjects_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 1, 3)
)
_WmanIf2BsPkmSecurityCapabilityTable_Object = MibTable
wmanIf2BsPkmSecurityCapabilityTable = _WmanIf2BsPkmSecurityCapabilityTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsPkmSecurityCapabilityTable.setStatus("current")
_WmanIf2BsPkmSecurityCapabilityEntry_Object = MibTableRow
wmanIf2BsPkmSecurityCapabilityEntry = _WmanIf2BsPkmSecurityCapabilityEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 1, 1)
)
wmanIf2BsPkmSecurityCapabilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-MIB", "wmanIf2BsPkmSecurityCapIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsPkmSecurityCapabilityEntry.setStatus("current")


class _WmanIf2BsPkmSecurityCapIndex_Type(Integer32):
    """Custom type wmanIf2BsPkmSecurityCapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2BsPkmSecurityCapIndex_Type.__name__ = "Integer32"
_WmanIf2BsPkmSecurityCapIndex_Object = MibTableColumn
wmanIf2BsPkmSecurityCapIndex = _WmanIf2BsPkmSecurityCapIndex_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 1, 1, 1),
    _WmanIf2BsPkmSecurityCapIndex_Type()
)
wmanIf2BsPkmSecurityCapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsPkmSecurityCapIndex.setStatus("current")
_WmanIf2BsPkmScDataEncryptAlgorithm_Type = WmanIf2DataEncryptAlgId
_WmanIf2BsPkmScDataEncryptAlgorithm_Object = MibTableColumn
wmanIf2BsPkmScDataEncryptAlgorithm = _WmanIf2BsPkmScDataEncryptAlgorithm_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 1, 1, 2),
    _WmanIf2BsPkmScDataEncryptAlgorithm_Type()
)
wmanIf2BsPkmScDataEncryptAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsPkmScDataEncryptAlgorithm.setStatus("current")
_WmanIf2BsPkmScDataAuthentAlgorithm_Type = WmanIf2DataAuthAlgId
_WmanIf2BsPkmScDataAuthentAlgorithm_Object = MibTableColumn
wmanIf2BsPkmScDataAuthentAlgorithm = _WmanIf2BsPkmScDataAuthentAlgorithm_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 1, 1, 3),
    _WmanIf2BsPkmScDataAuthentAlgorithm_Type()
)
wmanIf2BsPkmScDataAuthentAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsPkmScDataAuthentAlgorithm.setStatus("current")
_WmanIf2BsPkmScEncryptAlgorithm_Type = WmanIf2TekEncryptAlgId
_WmanIf2BsPkmScEncryptAlgorithm_Object = MibTableColumn
wmanIf2BsPkmScEncryptAlgorithm = _WmanIf2BsPkmScEncryptAlgorithm_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 1, 1, 4),
    _WmanIf2BsPkmScEncryptAlgorithm_Type()
)
wmanIf2BsPkmScEncryptAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsPkmScEncryptAlgorithm.setStatus("current")
_WmanIf2BsSsPkmSecurityCapabilityTable_Object = MibTable
wmanIf2BsSsPkmSecurityCapabilityTable = _WmanIf2BsSsPkmSecurityCapabilityTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmSecurityCapabilityTable.setStatus("current")
_WmanIf2BsSsPkmSecurityCapabilityEntry_Object = MibTableRow
wmanIf2BsSsPkmSecurityCapabilityEntry = _WmanIf2BsSsPkmSecurityCapabilityEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 2, 1)
)
wmanIf2BsSsPkmSecurityCapabilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-MIB", "wmanIf2BsSsMacAddress"),
    (0, "WMAN-IF2-MIB", "wmanIf2BsSsPkmSecurityCapIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmSecurityCapabilityEntry.setStatus("current")


class _WmanIf2BsSsPkmSecurityCapIndex_Type(Integer32):
    """Custom type wmanIf2BsSsPkmSecurityCapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2BsSsPkmSecurityCapIndex_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmSecurityCapIndex_Object = MibTableColumn
wmanIf2BsSsPkmSecurityCapIndex = _WmanIf2BsSsPkmSecurityCapIndex_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 2, 1, 1),
    _WmanIf2BsSsPkmSecurityCapIndex_Type()
)
wmanIf2BsSsPkmSecurityCapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmSecurityCapIndex.setStatus("current")
_WmanIf2BsSsPkmScDataEncryptAlgorithm_Type = WmanIf2DataEncryptAlgId
_WmanIf2BsSsPkmScDataEncryptAlgorithm_Object = MibTableColumn
wmanIf2BsSsPkmScDataEncryptAlgorithm = _WmanIf2BsSsPkmScDataEncryptAlgorithm_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 2, 1, 2),
    _WmanIf2BsSsPkmScDataEncryptAlgorithm_Type()
)
wmanIf2BsSsPkmScDataEncryptAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmScDataEncryptAlgorithm.setStatus("current")
_WmanIf2BsSsPkmScDataAuthentAlgorithm_Type = WmanIf2DataAuthAlgId
_WmanIf2BsSsPkmScDataAuthentAlgorithm_Object = MibTableColumn
wmanIf2BsSsPkmScDataAuthentAlgorithm = _WmanIf2BsSsPkmScDataAuthentAlgorithm_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 2, 1, 3),
    _WmanIf2BsSsPkmScDataAuthentAlgorithm_Type()
)
wmanIf2BsSsPkmScDataAuthentAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmScDataAuthentAlgorithm.setStatus("current")
_WmanIf2BsSsPkmScEncryptAlgorithm_Type = WmanIf2TekEncryptAlgId
_WmanIf2BsSsPkmScEncryptAlgorithm_Object = MibTableColumn
wmanIf2BsSsPkmScEncryptAlgorithm = _WmanIf2BsSsPkmScEncryptAlgorithm_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 2, 1, 4),
    _WmanIf2BsSsPkmScEncryptAlgorithm_Type()
)
wmanIf2BsSsPkmScEncryptAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmScEncryptAlgorithm.setStatus("current")
_WmanIf2BsPkmV1Objects_ObjectIdentity = ObjectIdentity
wmanIf2BsPkmV1Objects = _WmanIf2BsPkmV1Objects_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 1, 3, 3)
)
_WmanIf2BsPkmV1ConfigTable_Object = MibTable
wmanIf2BsPkmV1ConfigTable = _WmanIf2BsPkmV1ConfigTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1ConfigTable.setStatus("current")
_WmanIf2BsPkmV1ConfigEntry_Object = MibTableRow
wmanIf2BsPkmV1ConfigEntry = _WmanIf2BsPkmV1ConfigEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 3, 1, 1)
)
wmanIf2BsPkmV1ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1ConfigEntry.setStatus("current")


class _WmanIf2BsPkmV1AkLifetime_Type(Integer32):
    """Custom type wmanIf2BsPkmV1AkLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(86400, 6048000),
    )


_WmanIf2BsPkmV1AkLifetime_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1AkLifetime_Object = MibTableColumn
wmanIf2BsPkmV1AkLifetime = _WmanIf2BsPkmV1AkLifetime_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 3, 1, 1, 1),
    _WmanIf2BsPkmV1AkLifetime_Type()
)
wmanIf2BsPkmV1AkLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1AkLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1AkLifetime.setUnits("seconds")


class _WmanIf2BsPkmV1TekLifetime_Type(Integer32):
    """Custom type wmanIf2BsPkmV1TekLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 604800),
    )


_WmanIf2BsPkmV1TekLifetime_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1TekLifetime_Object = MibTableColumn
wmanIf2BsPkmV1TekLifetime = _WmanIf2BsPkmV1TekLifetime_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 3, 1, 1, 2),
    _WmanIf2BsPkmV1TekLifetime_Type()
)
wmanIf2BsPkmV1TekLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1TekLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1TekLifetime.setUnits("seconds")


class _WmanIf2BsPkmV1SelfSigManufCertTrust_Type(Integer32):
    """Custom type wmanIf2BsPkmV1SelfSigManufCertTrust based on Integer32"""
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


_WmanIf2BsPkmV1SelfSigManufCertTrust_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1SelfSigManufCertTrust_Object = MibTableColumn
wmanIf2BsPkmV1SelfSigManufCertTrust = _WmanIf2BsPkmV1SelfSigManufCertTrust_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 3, 1, 1, 3),
    _WmanIf2BsPkmV1SelfSigManufCertTrust_Type()
)
wmanIf2BsPkmV1SelfSigManufCertTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1SelfSigManufCertTrust.setStatus("current")


class _WmanIf2BsPkmV1AuthWaitTimeout_Type(Integer32):
    """Custom type wmanIf2BsPkmV1AuthWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_WmanIf2BsPkmV1AuthWaitTimeout_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1AuthWaitTimeout_Object = MibTableColumn
wmanIf2BsPkmV1AuthWaitTimeout = _WmanIf2BsPkmV1AuthWaitTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 3, 1, 1, 4),
    _WmanIf2BsPkmV1AuthWaitTimeout_Type()
)
wmanIf2BsPkmV1AuthWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1AuthWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1AuthWaitTimeout.setUnits("seconds")


class _WmanIf2BsPkmV1ReauthWaitTimeout_Type(Integer32):
    """Custom type wmanIf2BsPkmV1ReauthWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_WmanIf2BsPkmV1ReauthWaitTimeout_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1ReauthWaitTimeout_Object = MibTableColumn
wmanIf2BsPkmV1ReauthWaitTimeout = _WmanIf2BsPkmV1ReauthWaitTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 3, 1, 1, 5),
    _WmanIf2BsPkmV1ReauthWaitTimeout_Type()
)
wmanIf2BsPkmV1ReauthWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1ReauthWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1ReauthWaitTimeout.setUnits("seconds")


class _WmanIf2BsPkmV1AuthGraceTime_Type(Integer32):
    """Custom type wmanIf2BsPkmV1AuthGraceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 604800),
    )


_WmanIf2BsPkmV1AuthGraceTime_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1AuthGraceTime_Object = MibTableColumn
wmanIf2BsPkmV1AuthGraceTime = _WmanIf2BsPkmV1AuthGraceTime_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 3, 1, 1, 6),
    _WmanIf2BsPkmV1AuthGraceTime_Type()
)
wmanIf2BsPkmV1AuthGraceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1AuthGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1AuthGraceTime.setUnits("seconds")


class _WmanIf2BsPkmV1OpWaitTimeout_Type(Integer32):
    """Custom type wmanIf2BsPkmV1OpWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WmanIf2BsPkmV1OpWaitTimeout_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1OpWaitTimeout_Object = MibTableColumn
wmanIf2BsPkmV1OpWaitTimeout = _WmanIf2BsPkmV1OpWaitTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 3, 1, 1, 7),
    _WmanIf2BsPkmV1OpWaitTimeout_Type()
)
wmanIf2BsPkmV1OpWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1OpWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1OpWaitTimeout.setUnits("seconds")


class _WmanIf2BsPkmV1RekeyWaitTimeout_Type(Integer32):
    """Custom type wmanIf2BsPkmV1RekeyWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WmanIf2BsPkmV1RekeyWaitTimeout_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1RekeyWaitTimeout_Object = MibTableColumn
wmanIf2BsPkmV1RekeyWaitTimeout = _WmanIf2BsPkmV1RekeyWaitTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 3, 1, 1, 8),
    _WmanIf2BsPkmV1RekeyWaitTimeout_Type()
)
wmanIf2BsPkmV1RekeyWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1RekeyWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1RekeyWaitTimeout.setUnits("seconds")


class _WmanIf2BsPkmV1TekGraceTime_Type(Integer32):
    """Custom type wmanIf2BsPkmV1TekGraceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_WmanIf2BsPkmV1TekGraceTime_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1TekGraceTime_Object = MibTableColumn
wmanIf2BsPkmV1TekGraceTime = _WmanIf2BsPkmV1TekGraceTime_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 3, 1, 1, 9),
    _WmanIf2BsPkmV1TekGraceTime_Type()
)
wmanIf2BsPkmV1TekGraceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1TekGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1TekGraceTime.setUnits("seconds")


class _WmanIf2BsPkmV1AuthRejectWaitTimeout_Type(Integer32):
    """Custom type wmanIf2BsPkmV1AuthRejectWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_WmanIf2BsPkmV1AuthRejectWaitTimeout_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1AuthRejectWaitTimeout_Object = MibTableColumn
wmanIf2BsPkmV1AuthRejectWaitTimeout = _WmanIf2BsPkmV1AuthRejectWaitTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 3, 1, 1, 10),
    _WmanIf2BsPkmV1AuthRejectWaitTimeout_Type()
)
wmanIf2BsPkmV1AuthRejectWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1AuthRejectWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1AuthRejectWaitTimeout.setUnits("seconds")
_WmanIf2BsPkmV1CheckCertValidityPeriods_Type = TruthValue
_WmanIf2BsPkmV1CheckCertValidityPeriods_Object = MibTableColumn
wmanIf2BsPkmV1CheckCertValidityPeriods = _WmanIf2BsPkmV1CheckCertValidityPeriods_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 3, 1, 1, 11),
    _WmanIf2BsPkmV1CheckCertValidityPeriods_Type()
)
wmanIf2BsPkmV1CheckCertValidityPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1CheckCertValidityPeriods.setStatus("current")
_WmanIf2BsPkmV2Objects_ObjectIdentity = ObjectIdentity
wmanIf2BsPkmV2Objects = _WmanIf2BsPkmV2Objects_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 1, 3, 4)
)
_WmanIf2BsPkmV2ConfigTable_Object = MibTable
wmanIf2BsPkmV2ConfigTable = _WmanIf2BsPkmV2ConfigTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsPkmV2ConfigTable.setStatus("current")
_WmanIf2BsPkmV2ConfigEntry_Object = MibTableRow
wmanIf2BsPkmV2ConfigEntry = _WmanIf2BsPkmV2ConfigEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 4, 1, 1)
)
wmanIf2BsPkmV2ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsPkmV2ConfigEntry.setStatus("current")


class _WmanIf2BsPkmPmkPrehandshakeLifetime_Type(Integer32):
    """Custom type wmanIf2BsPkmPmkPrehandshakeLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 900),
    )


_WmanIf2BsPkmPmkPrehandshakeLifetime_Type.__name__ = "Integer32"
_WmanIf2BsPkmPmkPrehandshakeLifetime_Object = MibTableColumn
wmanIf2BsPkmPmkPrehandshakeLifetime = _WmanIf2BsPkmPmkPrehandshakeLifetime_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 4, 1, 1, 1),
    _WmanIf2BsPkmPmkPrehandshakeLifetime_Type()
)
wmanIf2BsPkmPmkPrehandshakeLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmPmkPrehandshakeLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmPmkPrehandshakeLifetime.setUnits("seconds")


class _WmanIf2BsPkmPmkLifetime_Type(Integer32):
    """Custom type wmanIf2BsPkmPmkLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_WmanIf2BsPkmPmkLifetime_Type.__name__ = "Integer32"
_WmanIf2BsPkmPmkLifetime_Object = MibTableColumn
wmanIf2BsPkmPmkLifetime = _WmanIf2BsPkmPmkLifetime_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 4, 1, 1, 2),
    _WmanIf2BsPkmPmkLifetime_Type()
)
wmanIf2BsPkmPmkLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmPmkLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmPmkLifetime.setUnits("seconds")


class _WmanIf2BsSaChallengeTimeout_Type(Integer32):
    """Custom type wmanIf2BsSaChallengeTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_WmanIf2BsSaChallengeTimeout_Type.__name__ = "Integer32"
_WmanIf2BsSaChallengeTimeout_Object = MibTableColumn
wmanIf2BsSaChallengeTimeout = _WmanIf2BsSaChallengeTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 4, 1, 1, 3),
    _WmanIf2BsSaChallengeTimeout_Type()
)
wmanIf2BsSaChallengeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSaChallengeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSaChallengeTimeout.setUnits("100milliseconds")


class _WmanIf2BsMaxSaTekChallenge_Type(Integer32):
    """Custom type wmanIf2BsMaxSaTekChallenge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WmanIf2BsMaxSaTekChallenge_Type.__name__ = "Integer32"
_WmanIf2BsMaxSaTekChallenge_Object = MibTableColumn
wmanIf2BsMaxSaTekChallenge = _WmanIf2BsMaxSaTekChallenge_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 4, 1, 1, 4),
    _WmanIf2BsMaxSaTekChallenge_Type()
)
wmanIf2BsMaxSaTekChallenge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsMaxSaTekChallenge.setStatus("current")


class _WmanIf2BsSaTekTimeout_Type(Integer32):
    """Custom type wmanIf2BsSaTekTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_WmanIf2BsSaTekTimeout_Type.__name__ = "Integer32"
_WmanIf2BsSaTekTimeout_Object = MibTableColumn
wmanIf2BsSaTekTimeout = _WmanIf2BsSaTekTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 4, 1, 1, 5),
    _WmanIf2BsSaTekTimeout_Type()
)
wmanIf2BsSaTekTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSaTekTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSaTekTimeout.setUnits("milliseconds")


class _WmanIf2BsMaxSaTekRequest_Type(Integer32):
    """Custom type wmanIf2BsMaxSaTekRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WmanIf2BsMaxSaTekRequest_Type.__name__ = "Integer32"
_WmanIf2BsMaxSaTekRequest_Object = MibTableColumn
wmanIf2BsMaxSaTekRequest = _WmanIf2BsMaxSaTekRequest_Object(
    (1, 0, 8802, 16, 2, 1, 1, 3, 4, 1, 1, 6),
    _WmanIf2BsMaxSaTekRequest_Type()
)
wmanIf2BsMaxSaTekRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsMaxSaTekRequest.setStatus("current")
_WmanIf2BsNotification_ObjectIdentity = ObjectIdentity
wmanIf2BsNotification = _WmanIf2BsNotification_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 1, 5)
)
_WmanIf2BsTrapControl_ObjectIdentity = ObjectIdentity
wmanIf2BsTrapControl = _WmanIf2BsTrapControl_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 1, 5, 1)
)
_WmanIf2BsThresholdConfigTable_Object = MibTable
wmanIf2BsThresholdConfigTable = _WmanIf2BsThresholdConfigTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    wmanIf2BsThresholdConfigTable.setStatus("current")
_WmanIf2BsThresholdConfigEntry_Object = MibTableRow
wmanIf2BsThresholdConfigEntry = _WmanIf2BsThresholdConfigEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 5, 1, 3, 1)
)
wmanIf2BsThresholdConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsThresholdConfigEntry.setStatus("current")


class _WmanIf2BsRssiLowThreshold_Type(Integer32):
    """Custom type wmanIf2BsRssiLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, -80),
    )


_WmanIf2BsRssiLowThreshold_Type.__name__ = "Integer32"
_WmanIf2BsRssiLowThreshold_Object = MibTableColumn
wmanIf2BsRssiLowThreshold = _WmanIf2BsRssiLowThreshold_Object(
    (1, 0, 8802, 16, 2, 1, 1, 5, 1, 3, 1, 1),
    _WmanIf2BsRssiLowThreshold_Type()
)
wmanIf2BsRssiLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsRssiLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsRssiLowThreshold.setUnits("0.25dBm")


class _WmanIf2BsRssiHighThreshold_Type(Integer32):
    """Custom type wmanIf2BsRssiHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, -80),
    )


_WmanIf2BsRssiHighThreshold_Type.__name__ = "Integer32"
_WmanIf2BsRssiHighThreshold_Object = MibTableColumn
wmanIf2BsRssiHighThreshold = _WmanIf2BsRssiHighThreshold_Object(
    (1, 0, 8802, 16, 2, 1, 1, 5, 1, 3, 1, 2),
    _WmanIf2BsRssiHighThreshold_Type()
)
wmanIf2BsRssiHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsRssiHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsRssiHighThreshold.setUnits("0.25dBm")
_WmanIf2BsPhy_ObjectIdentity = ObjectIdentity
wmanIf2BsPhy = _WmanIf2BsPhy_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 1, 6)
)
_WmanIf2BsOfdmaPhy_ObjectIdentity = ObjectIdentity
wmanIf2BsOfdmaPhy = _WmanIf2BsOfdmaPhy_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2)
)
_WmanIf2BsOfdmaUplinkChannelTable_Object = MibTable
wmanIf2BsOfdmaUplinkChannelTable = _WmanIf2BsOfdmaUplinkChannelTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaUplinkChannelTable.setStatus("current")
_WmanIf2BsOfdmaUplinkChannelEntry_Object = MibTableRow
wmanIf2BsOfdmaUplinkChannelEntry = _WmanIf2BsOfdmaUplinkChannelEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 1, 1)
)
wmanIf2BsOfdmaUplinkChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaUplinkChannelEntry.setStatus("current")


class _WmanIf2BsOfdmaCtBasedResvTimeout_Type(Integer32):
    """Custom type wmanIf2BsOfdmaCtBasedResvTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaCtBasedResvTimeout_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaCtBasedResvTimeout_Object = MibTableColumn
wmanIf2BsOfdmaCtBasedResvTimeout = _WmanIf2BsOfdmaCtBasedResvTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 1, 1, 1),
    _WmanIf2BsOfdmaCtBasedResvTimeout_Type()
)
wmanIf2BsOfdmaCtBasedResvTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCtBasedResvTimeout.setStatus("current")


class _WmanIf2BsOfdmaUplinkCenterFreq_Type(Unsigned32):
    """Custom type wmanIf2BsOfdmaUplinkCenterFreq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2496000, 2690000),
        ValueRangeConstraint(3400000, 3620000),
    )


_WmanIf2BsOfdmaUplinkCenterFreq_Type.__name__ = "Unsigned32"
_WmanIf2BsOfdmaUplinkCenterFreq_Object = MibTableColumn
wmanIf2BsOfdmaUplinkCenterFreq = _WmanIf2BsOfdmaUplinkCenterFreq_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 1, 1, 4),
    _WmanIf2BsOfdmaUplinkCenterFreq_Type()
)
wmanIf2BsOfdmaUplinkCenterFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaUplinkCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaUplinkCenterFreq.setUnits("kHz")


class _WmanIf2BsOfdmaStartOfRngCodes_Type(Integer32):
    """Custom type wmanIf2BsOfdmaStartOfRngCodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaStartOfRngCodes_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaStartOfRngCodes_Object = MibTableColumn
wmanIf2BsOfdmaStartOfRngCodes = _WmanIf2BsOfdmaStartOfRngCodes_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 1, 1, 10),
    _WmanIf2BsOfdmaStartOfRngCodes_Type()
)
wmanIf2BsOfdmaStartOfRngCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaStartOfRngCodes.setStatus("current")


class _WmanIf2BsOfdmaPermutationBase_Type(Integer32):
    """Custom type wmanIf2BsOfdmaPermutationBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaPermutationBase_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaPermutationBase_Object = MibTableColumn
wmanIf2BsOfdmaPermutationBase = _WmanIf2BsOfdmaPermutationBase_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 1, 1, 11),
    _WmanIf2BsOfdmaPermutationBase_Type()
)
wmanIf2BsOfdmaPermutationBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaPermutationBase.setStatus("current")


class _WmanIf2BsOfdmaULAllocSubchBitmap_Type(OctetString):
    """Custom type wmanIf2BsOfdmaULAllocSubchBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )
    fixedLength = 9


_WmanIf2BsOfdmaULAllocSubchBitmap_Type.__name__ = "OctetString"
_WmanIf2BsOfdmaULAllocSubchBitmap_Object = MibTableColumn
wmanIf2BsOfdmaULAllocSubchBitmap = _WmanIf2BsOfdmaULAllocSubchBitmap_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 1, 1, 12),
    _WmanIf2BsOfdmaULAllocSubchBitmap_Type()
)
wmanIf2BsOfdmaULAllocSubchBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaULAllocSubchBitmap.setStatus("current")


class _WmanIf2BsOfdmaOptPermULAllocSubchBitmap_Type(OctetString):
    """Custom type wmanIf2BsOfdmaOptPermULAllocSubchBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )
    fixedLength = 13


_WmanIf2BsOfdmaOptPermULAllocSubchBitmap_Type.__name__ = "OctetString"
_WmanIf2BsOfdmaOptPermULAllocSubchBitmap_Object = MibTableColumn
wmanIf2BsOfdmaOptPermULAllocSubchBitmap = _WmanIf2BsOfdmaOptPermULAllocSubchBitmap_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 1, 1, 13),
    _WmanIf2BsOfdmaOptPermULAllocSubchBitmap_Type()
)
wmanIf2BsOfdmaOptPermULAllocSubchBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaOptPermULAllocSubchBitmap.setStatus("current")


class _WmanIf2BsOfdmaBandAMCAllocThreshold_Type(Integer32):
    """Custom type wmanIf2BsOfdmaBandAMCAllocThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaBandAMCAllocThreshold_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaBandAMCAllocThreshold_Object = MibTableColumn
wmanIf2BsOfdmaBandAMCAllocThreshold = _WmanIf2BsOfdmaBandAMCAllocThreshold_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 1, 1, 14),
    _WmanIf2BsOfdmaBandAMCAllocThreshold_Type()
)
wmanIf2BsOfdmaBandAMCAllocThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBandAMCAllocThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBandAMCAllocThreshold.setUnits("dB")


class _WmanIf2BsOfdmaBandAMCReleaseThreshold_Type(Integer32):
    """Custom type wmanIf2BsOfdmaBandAMCReleaseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaBandAMCReleaseThreshold_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaBandAMCReleaseThreshold_Object = MibTableColumn
wmanIf2BsOfdmaBandAMCReleaseThreshold = _WmanIf2BsOfdmaBandAMCReleaseThreshold_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 1, 1, 15),
    _WmanIf2BsOfdmaBandAMCReleaseThreshold_Type()
)
wmanIf2BsOfdmaBandAMCReleaseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBandAMCReleaseThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBandAMCReleaseThreshold.setUnits("dB")


class _WmanIf2BsOfdmaBandAMCAllocTimer_Type(Integer32):
    """Custom type wmanIf2BsOfdmaBandAMCAllocTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaBandAMCAllocTimer_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaBandAMCAllocTimer_Object = MibTableColumn
wmanIf2BsOfdmaBandAMCAllocTimer = _WmanIf2BsOfdmaBandAMCAllocTimer_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 1, 1, 16),
    _WmanIf2BsOfdmaBandAMCAllocTimer_Type()
)
wmanIf2BsOfdmaBandAMCAllocTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBandAMCAllocTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBandAMCAllocTimer.setUnits("Frame")


class _WmanIf2BsOfdmaBandAMCReleaseTimer_Type(Integer32):
    """Custom type wmanIf2BsOfdmaBandAMCReleaseTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaBandAMCReleaseTimer_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaBandAMCReleaseTimer_Object = MibTableColumn
wmanIf2BsOfdmaBandAMCReleaseTimer = _WmanIf2BsOfdmaBandAMCReleaseTimer_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 1, 1, 17),
    _WmanIf2BsOfdmaBandAMCReleaseTimer_Type()
)
wmanIf2BsOfdmaBandAMCReleaseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBandAMCReleaseTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBandAMCReleaseTimer.setUnits("Frame")


class _WmanIf2BsOfdmaBandStatRepMAXPeriod_Type(Integer32):
    """Custom type wmanIf2BsOfdmaBandStatRepMAXPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaBandStatRepMAXPeriod_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaBandStatRepMAXPeriod_Object = MibTableColumn
wmanIf2BsOfdmaBandStatRepMAXPeriod = _WmanIf2BsOfdmaBandStatRepMAXPeriod_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 1, 1, 18),
    _WmanIf2BsOfdmaBandStatRepMAXPeriod_Type()
)
wmanIf2BsOfdmaBandStatRepMAXPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBandStatRepMAXPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBandStatRepMAXPeriod.setUnits("Frame")


class _WmanIf2BsOfdmaBandAMCRetryTimer_Type(Integer32):
    """Custom type wmanIf2BsOfdmaBandAMCRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaBandAMCRetryTimer_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaBandAMCRetryTimer_Object = MibTableColumn
wmanIf2BsOfdmaBandAMCRetryTimer = _WmanIf2BsOfdmaBandAMCRetryTimer_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 1, 1, 19),
    _WmanIf2BsOfdmaBandAMCRetryTimer_Type()
)
wmanIf2BsOfdmaBandAMCRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBandAMCRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBandAMCRetryTimer.setUnits("Frame")
_WmanIf2BsOfdmaDownlinkChannelTable_Object = MibTable
wmanIf2BsOfdmaDownlinkChannelTable = _WmanIf2BsOfdmaDownlinkChannelTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDownlinkChannelTable.setStatus("current")
_WmanIf2BsOfdmaDownlinkChannelEntry_Object = MibTableRow
wmanIf2BsOfdmaDownlinkChannelEntry = _WmanIf2BsOfdmaDownlinkChannelEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 2, 1)
)
wmanIf2BsOfdmaDownlinkChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDownlinkChannelEntry.setStatus("current")


class _WmanIf2BsOfdmaBsEIRP_Type(Integer32):
    """Custom type wmanIf2BsOfdmaBsEIRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_WmanIf2BsOfdmaBsEIRP_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaBsEIRP_Object = MibTableColumn
wmanIf2BsOfdmaBsEIRP = _WmanIf2BsOfdmaBsEIRP_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 2, 1, 1),
    _WmanIf2BsOfdmaBsEIRP_Type()
)
wmanIf2BsOfdmaBsEIRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBsEIRP.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBsEIRP.setUnits("dBm")
_WmanIf2BsOfdmaChannelNumber_Type = WmanIf2ChannelNumber
_WmanIf2BsOfdmaChannelNumber_Object = MibTableColumn
wmanIf2BsOfdmaChannelNumber = _WmanIf2BsOfdmaChannelNumber_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 2, 1, 2),
    _WmanIf2BsOfdmaChannelNumber_Type()
)
wmanIf2BsOfdmaChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaChannelNumber.setStatus("current")


class _WmanIf2BsOfdmaTTG_Type(Integer32):
    """Custom type wmanIf2BsOfdmaTTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsOfdmaTTG_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaTTG_Object = MibTableColumn
wmanIf2BsOfdmaTTG = _WmanIf2BsOfdmaTTG_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 2, 1, 3),
    _WmanIf2BsOfdmaTTG_Type()
)
wmanIf2BsOfdmaTTG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaTTG.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaTTG.setUnits("PS")


class _WmanIf2BsOfdmaRTG_Type(Integer32):
    """Custom type wmanIf2BsOfdmaRTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaRTG_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaRTG_Object = MibTableColumn
wmanIf2BsOfdmaRTG = _WmanIf2BsOfdmaRTG_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 2, 1, 4),
    _WmanIf2BsOfdmaRTG_Type()
)
wmanIf2BsOfdmaRTG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaRTG.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaRTG.setUnits("PS")


class _WmanIf2BsOfdmaInitRngMaxRSS_Type(Integer32):
    """Custom type wmanIf2BsOfdmaInitRngMaxRSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_WmanIf2BsOfdmaInitRngMaxRSS_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaInitRngMaxRSS_Object = MibTableColumn
wmanIf2BsOfdmaInitRngMaxRSS = _WmanIf2BsOfdmaInitRngMaxRSS_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 2, 1, 5),
    _WmanIf2BsOfdmaInitRngMaxRSS_Type()
)
wmanIf2BsOfdmaInitRngMaxRSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaInitRngMaxRSS.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaInitRngMaxRSS.setUnits("dBm")


class _WmanIf2BsOfdmaDownlinkCenterFreq_Type(Unsigned32):
    """Custom type wmanIf2BsOfdmaDownlinkCenterFreq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2496000, 2690000),
        ValueRangeConstraint(3400000, 3620000),
    )


_WmanIf2BsOfdmaDownlinkCenterFreq_Type.__name__ = "Unsigned32"
_WmanIf2BsOfdmaDownlinkCenterFreq_Object = MibTableColumn
wmanIf2BsOfdmaDownlinkCenterFreq = _WmanIf2BsOfdmaDownlinkCenterFreq_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 2, 1, 6),
    _WmanIf2BsOfdmaDownlinkCenterFreq_Type()
)
wmanIf2BsOfdmaDownlinkCenterFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDownlinkCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDownlinkCenterFreq.setUnits("kHz")
_WmanIf2BsOfdmaBsId_Type = WmanIf2BsIdType
_WmanIf2BsOfdmaBsId_Object = MibTableColumn
wmanIf2BsOfdmaBsId = _WmanIf2BsOfdmaBsId_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 2, 1, 7),
    _WmanIf2BsOfdmaBsId_Type()
)
wmanIf2BsOfdmaBsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBsId.setStatus("current")
_WmanIf2BsOfdmaMacVersion_Type = WmanIf2MacVersion
_WmanIf2BsOfdmaMacVersion_Object = MibTableColumn
wmanIf2BsOfdmaMacVersion = _WmanIf2BsOfdmaMacVersion_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 2, 1, 8),
    _WmanIf2BsOfdmaMacVersion_Type()
)
wmanIf2BsOfdmaMacVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaMacVersion.setStatus("current")


class _WmanIf2BsOfdmaFrameDurationCode_Type(Integer32):
    """Custom type wmanIf2BsOfdmaFrameDurationCode based on Integer32"""
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


_WmanIf2BsOfdmaFrameDurationCode_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaFrameDurationCode_Object = MibTableColumn
wmanIf2BsOfdmaFrameDurationCode = _WmanIf2BsOfdmaFrameDurationCode_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 2, 1, 9),
    _WmanIf2BsOfdmaFrameDurationCode_Type()
)
wmanIf2BsOfdmaFrameDurationCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaFrameDurationCode.setStatus("current")
_WmanIf2BsOfdmaUcdBurstProfileTable_Object = MibTable
wmanIf2BsOfdmaUcdBurstProfileTable = _WmanIf2BsOfdmaUcdBurstProfileTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaUcdBurstProfileTable.setStatus("current")
_WmanIf2BsOfdmaUcdBurstProfileEntry_Object = MibTableRow
wmanIf2BsOfdmaUcdBurstProfileEntry = _WmanIf2BsOfdmaUcdBurstProfileEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 3, 1)
)
wmanIf2BsOfdmaUcdBurstProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-MIB", "wmanIf2BsOfdmaUiucIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaUcdBurstProfileEntry.setStatus("current")


class _WmanIf2BsOfdmaUiucIndex_Type(Integer32):
    """Custom type wmanIf2BsOfdmaUiucIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WmanIf2BsOfdmaUiucIndex_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaUiucIndex_Object = MibTableColumn
wmanIf2BsOfdmaUiucIndex = _WmanIf2BsOfdmaUiucIndex_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 3, 1, 1),
    _WmanIf2BsOfdmaUiucIndex_Type()
)
wmanIf2BsOfdmaUiucIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaUiucIndex.setStatus("current")
_WmanIf2BsOfdmaUcdFecCodeType_Type = WmanIf2OfdmaUcdFecCode
_WmanIf2BsOfdmaUcdFecCodeType_Object = MibTableColumn
wmanIf2BsOfdmaUcdFecCodeType = _WmanIf2BsOfdmaUcdFecCodeType_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 3, 1, 2),
    _WmanIf2BsOfdmaUcdFecCodeType_Type()
)
wmanIf2BsOfdmaUcdFecCodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaUcdFecCodeType.setStatus("current")


class _WmanIf2BsOfdmaRangingDataRatio_Type(Integer32):
    """Custom type wmanIf2BsOfdmaRangingDataRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_WmanIf2BsOfdmaRangingDataRatio_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaRangingDataRatio_Object = MibTableColumn
wmanIf2BsOfdmaRangingDataRatio = _WmanIf2BsOfdmaRangingDataRatio_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 3, 1, 3),
    _WmanIf2BsOfdmaRangingDataRatio_Type()
)
wmanIf2BsOfdmaRangingDataRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaRangingDataRatio.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaRangingDataRatio.setUnits("dB")
_WmanIf2BsOfdmaUcdBurstProfileRowStatus_Type = RowStatus
_WmanIf2BsOfdmaUcdBurstProfileRowStatus_Object = MibTableColumn
wmanIf2BsOfdmaUcdBurstProfileRowStatus = _WmanIf2BsOfdmaUcdBurstProfileRowStatus_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 3, 1, 5),
    _WmanIf2BsOfdmaUcdBurstProfileRowStatus_Type()
)
wmanIf2BsOfdmaUcdBurstProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaUcdBurstProfileRowStatus.setStatus("current")
_WmanIf2BsOfdmaDcdBurstProfileTable_Object = MibTable
wmanIf2BsOfdmaDcdBurstProfileTable = _WmanIf2BsOfdmaDcdBurstProfileTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 4)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDcdBurstProfileTable.setStatus("current")
_WmanIf2BsOfdmaDcdBurstProfileEntry_Object = MibTableRow
wmanIf2BsOfdmaDcdBurstProfileEntry = _WmanIf2BsOfdmaDcdBurstProfileEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 4, 1)
)
wmanIf2BsOfdmaDcdBurstProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-MIB", "wmanIf2BsOfdmaDiucIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDcdBurstProfileEntry.setStatus("current")


class _WmanIf2BsOfdmaDiucIndex_Type(Integer32):
    """Custom type wmanIf2BsOfdmaDiucIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_WmanIf2BsOfdmaDiucIndex_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaDiucIndex_Object = MibTableColumn
wmanIf2BsOfdmaDiucIndex = _WmanIf2BsOfdmaDiucIndex_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 4, 1, 1),
    _WmanIf2BsOfdmaDiucIndex_Type()
)
wmanIf2BsOfdmaDiucIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDiucIndex.setStatus("current")
_WmanIf2BsOfdmaDownlinkFrequency_Type = Unsigned32
_WmanIf2BsOfdmaDownlinkFrequency_Object = MibTableColumn
wmanIf2BsOfdmaDownlinkFrequency = _WmanIf2BsOfdmaDownlinkFrequency_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 4, 1, 2),
    _WmanIf2BsOfdmaDownlinkFrequency_Type()
)
wmanIf2BsOfdmaDownlinkFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDownlinkFrequency.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDownlinkFrequency.setUnits("kHz")
_WmanIf2BsOfdmaDcdFecCodeType_Type = WmanIf2OfdmaDcdFecCode
_WmanIf2BsOfdmaDcdFecCodeType_Object = MibTableColumn
wmanIf2BsOfdmaDcdFecCodeType = _WmanIf2BsOfdmaDcdFecCodeType_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 4, 1, 3),
    _WmanIf2BsOfdmaDcdFecCodeType_Type()
)
wmanIf2BsOfdmaDcdFecCodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDcdFecCodeType.setStatus("current")
_WmanIf2BsOfdmaDcdBurstProfileRowStatus_Type = RowStatus
_WmanIf2BsOfdmaDcdBurstProfileRowStatus_Object = MibTableColumn
wmanIf2BsOfdmaDcdBurstProfileRowStatus = _WmanIf2BsOfdmaDcdBurstProfileRowStatus_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 4, 1, 6),
    _WmanIf2BsOfdmaDcdBurstProfileRowStatus_Type()
)
wmanIf2BsOfdmaDcdBurstProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDcdBurstProfileRowStatus.setStatus("current")
_WmanIf2BsOfdmaCapabilitiesTable_Object = MibTable
wmanIf2BsOfdmaCapabilitiesTable = _WmanIf2BsOfdmaCapabilitiesTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapabilitiesTable.setStatus("current")
_WmanIf2BsOfdmaCapabilitiesEntry_Object = MibTableRow
wmanIf2BsOfdmaCapabilitiesEntry = _WmanIf2BsOfdmaCapabilitiesEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1)
)
wmanIf2BsOfdmaCapabilitiesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapabilitiesEntry.setStatus("current")
_WmanIf2BsOfdmaCapFftSizes_Type = WmanIf2OfdmaFftSizes
_WmanIf2BsOfdmaCapFftSizes_Object = MibTableColumn
wmanIf2BsOfdmaCapFftSizes = _WmanIf2BsOfdmaCapFftSizes_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 1),
    _WmanIf2BsOfdmaCapFftSizes_Type()
)
wmanIf2BsOfdmaCapFftSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapFftSizes.setStatus("current")
_WmanIf2BsOfdmaCapDemodulator_Type = WmanIf2OfdmaMsDeModType
_WmanIf2BsOfdmaCapDemodulator_Object = MibTableColumn
wmanIf2BsOfdmaCapDemodulator = _WmanIf2BsOfdmaCapDemodulator_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 2),
    _WmanIf2BsOfdmaCapDemodulator_Type()
)
wmanIf2BsOfdmaCapDemodulator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapDemodulator.setStatus("current")
_WmanIf2BsOfdmaCapModulator_Type = WmanIf2OfdmaMsModType
_WmanIf2BsOfdmaCapModulator_Object = MibTableColumn
wmanIf2BsOfdmaCapModulator = _WmanIf2BsOfdmaCapModulator_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 3),
    _WmanIf2BsOfdmaCapModulator_Type()
)
wmanIf2BsOfdmaCapModulator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapModulator.setStatus("current")
_WmanIf2BsOfdmaCapNoHarqChannel_Type = Unsigned32
_WmanIf2BsOfdmaCapNoHarqChannel_Object = MibTableColumn
wmanIf2BsOfdmaCapNoHarqChannel = _WmanIf2BsOfdmaCapNoHarqChannel_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 4),
    _WmanIf2BsOfdmaCapNoHarqChannel_Type()
)
wmanIf2BsOfdmaCapNoHarqChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapNoHarqChannel.setStatus("current")
_WmanIf2BsOfdmaCapPermutation_Type = WmanIf2OfdmaPermutation
_WmanIf2BsOfdmaCapPermutation_Object = MibTableColumn
wmanIf2BsOfdmaCapPermutation = _WmanIf2BsOfdmaCapPermutation_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 5),
    _WmanIf2BsOfdmaCapPermutation_Type()
)
wmanIf2BsOfdmaCapPermutation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapPermutation.setStatus("current")
_WmanIf2BsSsOfdmaCapDemMimo_Type = WmanIf2OfdmaDemMimo
_WmanIf2BsSsOfdmaCapDemMimo_Object = MibTableColumn
wmanIf2BsSsOfdmaCapDemMimo = _WmanIf2BsSsOfdmaCapDemMimo_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 6),
    _WmanIf2BsSsOfdmaCapDemMimo_Type()
)
wmanIf2BsSsOfdmaCapDemMimo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapDemMimo.setStatus("current")
_WmanIf2BsSsOfdmaCapMimoCapability_Type = WmanIf2OfdmaMimoCap
_WmanIf2BsSsOfdmaCapMimoCapability_Object = MibTableColumn
wmanIf2BsSsOfdmaCapMimoCapability = _WmanIf2BsSsOfdmaCapMimoCapability_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 7),
    _WmanIf2BsSsOfdmaCapMimoCapability_Type()
)
wmanIf2BsSsOfdmaCapMimoCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapMimoCapability.setStatus("current")
_WmanIf2BsSsOfdmaCapUlMimo_Type = WmanIf2OfdmaUlMimo
_WmanIf2BsSsOfdmaCapUlMimo_Object = MibTableColumn
wmanIf2BsSsOfdmaCapUlMimo = _WmanIf2BsSsOfdmaCapUlMimo_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 8),
    _WmanIf2BsSsOfdmaCapUlMimo_Type()
)
wmanIf2BsSsOfdmaCapUlMimo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapUlMimo.setStatus("current")
_WmanIf2BsSsOfdmaCapPrivateMap_Type = WmanIf2OfdmaPrivMap
_WmanIf2BsSsOfdmaCapPrivateMap_Object = MibTableColumn
wmanIf2BsSsOfdmaCapPrivateMap = _WmanIf2BsSsOfdmaCapPrivateMap_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 9),
    _WmanIf2BsSsOfdmaCapPrivateMap_Type()
)
wmanIf2BsSsOfdmaCapPrivateMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapPrivateMap.setStatus("current")
_WmanIf2BsSsOfdmaCapAasCapability_Type = WmanIf2OfdmaAasCap
_WmanIf2BsSsOfdmaCapAasCapability_Object = MibTableColumn
wmanIf2BsSsOfdmaCapAasCapability = _WmanIf2BsSsOfdmaCapAasCapability_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 10),
    _WmanIf2BsSsOfdmaCapAasCapability_Type()
)
wmanIf2BsSsOfdmaCapAasCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapAasCapability.setStatus("current")
_WmanIf2BsSsOfdmaCapCinrMeasurement_Type = WmanIf2OfdmaCinrCap
_WmanIf2BsSsOfdmaCapCinrMeasurement_Object = MibTableColumn
wmanIf2BsSsOfdmaCapCinrMeasurement = _WmanIf2BsSsOfdmaCapCinrMeasurement_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 11),
    _WmanIf2BsSsOfdmaCapCinrMeasurement_Type()
)
wmanIf2BsSsOfdmaCapCinrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapCinrMeasurement.setStatus("current")
_WmanIf2BsSsOfdmaCapUlPowerControl_Type = WmanIf2OfdmaUlPower
_WmanIf2BsSsOfdmaCapUlPowerControl_Object = MibTableColumn
wmanIf2BsSsOfdmaCapUlPowerControl = _WmanIf2BsSsOfdmaCapUlPowerControl_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 12),
    _WmanIf2BsSsOfdmaCapUlPowerControl_Type()
)
wmanIf2BsSsOfdmaCapUlPowerControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapUlPowerControl.setStatus("current")
_WmanIf2BsSsOfdmaCapMapCapability_Type = WmanIf2OfdmaMapCap
_WmanIf2BsSsOfdmaCapMapCapability_Object = MibTableColumn
wmanIf2BsSsOfdmaCapMapCapability = _WmanIf2BsSsOfdmaCapMapCapability_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 13),
    _WmanIf2BsSsOfdmaCapMapCapability_Type()
)
wmanIf2BsSsOfdmaCapMapCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapMapCapability.setStatus("current")
_WmanIf2BsSsOfdmaCapUlControlChannel_Type = WmanIf2OfdmaUlCntlCh
_WmanIf2BsSsOfdmaCapUlControlChannel_Object = MibTableColumn
wmanIf2BsSsOfdmaCapUlControlChannel = _WmanIf2BsSsOfdmaCapUlControlChannel_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 14),
    _WmanIf2BsSsOfdmaCapUlControlChannel_Type()
)
wmanIf2BsSsOfdmaCapUlControlChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapUlControlChannel.setStatus("current")
_WmanIf2BsSsOfdmaCapCistCapability_Type = WmanIf2OfdmaMsCistCap
_WmanIf2BsSsOfdmaCapCistCapability_Object = MibTableColumn
wmanIf2BsSsOfdmaCapCistCapability = _WmanIf2BsSsOfdmaCapCistCapability_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 15),
    _WmanIf2BsSsOfdmaCapCistCapability_Type()
)
wmanIf2BsSsOfdmaCapCistCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapCistCapability.setStatus("current")
_WmanIf2BsSsOfdmaCapMaxHarqBurst_Type = WmanIf2OfdmaMaxHarq
_WmanIf2BsSsOfdmaCapMaxHarqBurst_Object = MibTableColumn
wmanIf2BsSsOfdmaCapMaxHarqBurst = _WmanIf2BsSsOfdmaCapMaxHarqBurst_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 16),
    _WmanIf2BsSsOfdmaCapMaxHarqBurst_Type()
)
wmanIf2BsSsOfdmaCapMaxHarqBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapMaxHarqBurst.setStatus("current")
_WmanIf2BsSsOfdmaCapModMimo_Type = WmanIf2OfdmaModMimo
_WmanIf2BsSsOfdmaCapModMimo_Object = MibTableColumn
wmanIf2BsSsOfdmaCapModMimo = _WmanIf2BsSsOfdmaCapModMimo_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 17),
    _WmanIf2BsSsOfdmaCapModMimo_Type()
)
wmanIf2BsSsOfdmaCapModMimo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapModMimo.setStatus("current")
_WmanIf2BsSsOfdmaCapSdmaPilot_Type = WmanIf2SdmaPilotCap
_WmanIf2BsSsOfdmaCapSdmaPilot_Object = MibTableColumn
wmanIf2BsSsOfdmaCapSdmaPilot = _WmanIf2BsSsOfdmaCapSdmaPilot_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 18),
    _WmanIf2BsSsOfdmaCapSdmaPilot_Type()
)
wmanIf2BsSsOfdmaCapSdmaPilot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapSdmaPilot.setStatus("current")
_WmanIf2BsSsOfdmaCapMultipleBurst_Type = WmanIf2MultiBurst
_WmanIf2BsSsOfdmaCapMultipleBurst_Object = MibTableColumn
wmanIf2BsSsOfdmaCapMultipleBurst = _WmanIf2BsSsOfdmaCapMultipleBurst_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 19),
    _WmanIf2BsSsOfdmaCapMultipleBurst_Type()
)
wmanIf2BsSsOfdmaCapMultipleBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapMultipleBurst.setStatus("current")
_WmanIf2BsSsOfdmaCapIncrHarqBuffer_Type = WmanIf2IncrHarqBuf
_WmanIf2BsSsOfdmaCapIncrHarqBuffer_Object = MibTableColumn
wmanIf2BsSsOfdmaCapIncrHarqBuffer = _WmanIf2BsSsOfdmaCapIncrHarqBuffer_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 20),
    _WmanIf2BsSsOfdmaCapIncrHarqBuffer_Type()
)
wmanIf2BsSsOfdmaCapIncrHarqBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapIncrHarqBuffer.setStatus("current")
_WmanIf2BsSsOfdmaCapChaseHarqBuffer_Type = WmanIf2ChaseHarqBuf
_WmanIf2BsSsOfdmaCapChaseHarqBuffer_Object = MibTableColumn
wmanIf2BsSsOfdmaCapChaseHarqBuffer = _WmanIf2BsSsOfdmaCapChaseHarqBuffer_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 7, 1, 21),
    _WmanIf2BsSsOfdmaCapChaseHarqBuffer_Type()
)
wmanIf2BsSsOfdmaCapChaseHarqBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapChaseHarqBuffer.setStatus("current")
_WmanIf2BsOfdmaCapabilitiesConfigTable_Object = MibTable
wmanIf2BsOfdmaCapabilitiesConfigTable = _WmanIf2BsOfdmaCapabilitiesConfigTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapabilitiesConfigTable.setStatus("current")
_WmanIf2BsOfdmaCapabilitiesConfigEntry_Object = MibTableRow
wmanIf2BsOfdmaCapabilitiesConfigEntry = _WmanIf2BsOfdmaCapabilitiesConfigEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1)
)
wmanIf2BsOfdmaCapabilitiesConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapabilitiesConfigEntry.setStatus("current")
_WmanIf2BsOfdmaCapCfgFftSizes_Type = WmanIf2OfdmaFftSizes
_WmanIf2BsOfdmaCapCfgFftSizes_Object = MibTableColumn
wmanIf2BsOfdmaCapCfgFftSizes = _WmanIf2BsOfdmaCapCfgFftSizes_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 1),
    _WmanIf2BsOfdmaCapCfgFftSizes_Type()
)
wmanIf2BsOfdmaCapCfgFftSizes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapCfgFftSizes.setStatus("current")
_WmanIf2BsOfdmaCapCfgDemodulator_Type = WmanIf2OfdmaMsDeModType
_WmanIf2BsOfdmaCapCfgDemodulator_Object = MibTableColumn
wmanIf2BsOfdmaCapCfgDemodulator = _WmanIf2BsOfdmaCapCfgDemodulator_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 2),
    _WmanIf2BsOfdmaCapCfgDemodulator_Type()
)
wmanIf2BsOfdmaCapCfgDemodulator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapCfgDemodulator.setStatus("current")
_WmanIf2BsOfdmaCapCfgModulator_Type = WmanIf2OfdmaMsModType
_WmanIf2BsOfdmaCapCfgModulator_Object = MibTableColumn
wmanIf2BsOfdmaCapCfgModulator = _WmanIf2BsOfdmaCapCfgModulator_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 3),
    _WmanIf2BsOfdmaCapCfgModulator_Type()
)
wmanIf2BsOfdmaCapCfgModulator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapCfgModulator.setStatus("current")
_WmanIf2BsOfdmaCapCfgNoHarqChannel_Type = Unsigned32
_WmanIf2BsOfdmaCapCfgNoHarqChannel_Object = MibTableColumn
wmanIf2BsOfdmaCapCfgNoHarqChannel = _WmanIf2BsOfdmaCapCfgNoHarqChannel_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 4),
    _WmanIf2BsOfdmaCapCfgNoHarqChannel_Type()
)
wmanIf2BsOfdmaCapCfgNoHarqChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapCfgNoHarqChannel.setStatus("current")
_WmanIf2BsOfdmaCapCfgPermutation_Type = WmanIf2OfdmaPermutation
_WmanIf2BsOfdmaCapCfgPermutation_Object = MibTableColumn
wmanIf2BsOfdmaCapCfgPermutation = _WmanIf2BsOfdmaCapCfgPermutation_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 5),
    _WmanIf2BsOfdmaCapCfgPermutation_Type()
)
wmanIf2BsOfdmaCapCfgPermutation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapCfgPermutation.setStatus("current")
_WmanIf2BsSsOfdmaCapCfgDemMimo_Type = WmanIf2OfdmaDemMimo
_WmanIf2BsSsOfdmaCapCfgDemMimo_Object = MibTableColumn
wmanIf2BsSsOfdmaCapCfgDemMimo = _WmanIf2BsSsOfdmaCapCfgDemMimo_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 6),
    _WmanIf2BsSsOfdmaCapCfgDemMimo_Type()
)
wmanIf2BsSsOfdmaCapCfgDemMimo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapCfgDemMimo.setStatus("current")
_WmanIf2BsSsOfdmaCapCfgMimoCapability_Type = WmanIf2OfdmaMimoCap
_WmanIf2BsSsOfdmaCapCfgMimoCapability_Object = MibTableColumn
wmanIf2BsSsOfdmaCapCfgMimoCapability = _WmanIf2BsSsOfdmaCapCfgMimoCapability_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 7),
    _WmanIf2BsSsOfdmaCapCfgMimoCapability_Type()
)
wmanIf2BsSsOfdmaCapCfgMimoCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapCfgMimoCapability.setStatus("current")
_WmanIf2BsSsOfdmaCapCfgUlMimo_Type = WmanIf2OfdmaUlMimo
_WmanIf2BsSsOfdmaCapCfgUlMimo_Object = MibTableColumn
wmanIf2BsSsOfdmaCapCfgUlMimo = _WmanIf2BsSsOfdmaCapCfgUlMimo_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 8),
    _WmanIf2BsSsOfdmaCapCfgUlMimo_Type()
)
wmanIf2BsSsOfdmaCapCfgUlMimo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapCfgUlMimo.setStatus("current")
_WmanIf2BsSsOfdmaCapCfgPrivateMap_Type = WmanIf2OfdmaPrivMap
_WmanIf2BsSsOfdmaCapCfgPrivateMap_Object = MibTableColumn
wmanIf2BsSsOfdmaCapCfgPrivateMap = _WmanIf2BsSsOfdmaCapCfgPrivateMap_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 9),
    _WmanIf2BsSsOfdmaCapCfgPrivateMap_Type()
)
wmanIf2BsSsOfdmaCapCfgPrivateMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapCfgPrivateMap.setStatus("current")
_WmanIf2BsSsOfdmaCapCfgAasCapability_Type = WmanIf2OfdmaAasCap
_WmanIf2BsSsOfdmaCapCfgAasCapability_Object = MibTableColumn
wmanIf2BsSsOfdmaCapCfgAasCapability = _WmanIf2BsSsOfdmaCapCfgAasCapability_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 10),
    _WmanIf2BsSsOfdmaCapCfgAasCapability_Type()
)
wmanIf2BsSsOfdmaCapCfgAasCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapCfgAasCapability.setStatus("current")
_WmanIf2BsSsOfdmaCapCfgCinrMeasurement_Type = WmanIf2OfdmaCinrCap
_WmanIf2BsSsOfdmaCapCfgCinrMeasurement_Object = MibTableColumn
wmanIf2BsSsOfdmaCapCfgCinrMeasurement = _WmanIf2BsSsOfdmaCapCfgCinrMeasurement_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 11),
    _WmanIf2BsSsOfdmaCapCfgCinrMeasurement_Type()
)
wmanIf2BsSsOfdmaCapCfgCinrMeasurement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapCfgCinrMeasurement.setStatus("current")
_WmanIf2BsSsOfdmaCapCfgUlPowerControl_Type = WmanIf2OfdmaUlPower
_WmanIf2BsSsOfdmaCapCfgUlPowerControl_Object = MibTableColumn
wmanIf2BsSsOfdmaCapCfgUlPowerControl = _WmanIf2BsSsOfdmaCapCfgUlPowerControl_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 12),
    _WmanIf2BsSsOfdmaCapCfgUlPowerControl_Type()
)
wmanIf2BsSsOfdmaCapCfgUlPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapCfgUlPowerControl.setStatus("current")
_WmanIf2BsSsOfdmaCapCfgMapCapability_Type = WmanIf2OfdmaMapCap
_WmanIf2BsSsOfdmaCapCfgMapCapability_Object = MibTableColumn
wmanIf2BsSsOfdmaCapCfgMapCapability = _WmanIf2BsSsOfdmaCapCfgMapCapability_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 13),
    _WmanIf2BsSsOfdmaCapCfgMapCapability_Type()
)
wmanIf2BsSsOfdmaCapCfgMapCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapCfgMapCapability.setStatus("current")
_WmanIf2BsSsOfdmaCapCfgUlControlChannel_Type = WmanIf2OfdmaUlCntlCh
_WmanIf2BsSsOfdmaCapCfgUlControlChannel_Object = MibTableColumn
wmanIf2BsSsOfdmaCapCfgUlControlChannel = _WmanIf2BsSsOfdmaCapCfgUlControlChannel_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 14),
    _WmanIf2BsSsOfdmaCapCfgUlControlChannel_Type()
)
wmanIf2BsSsOfdmaCapCfgUlControlChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapCfgUlControlChannel.setStatus("current")
_WmanIf2BsSsOfdmaCapCfgCistCapability_Type = WmanIf2OfdmaMsCistCap
_WmanIf2BsSsOfdmaCapCfgCistCapability_Object = MibTableColumn
wmanIf2BsSsOfdmaCapCfgCistCapability = _WmanIf2BsSsOfdmaCapCfgCistCapability_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 15),
    _WmanIf2BsSsOfdmaCapCfgCistCapability_Type()
)
wmanIf2BsSsOfdmaCapCfgCistCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapCfgCistCapability.setStatus("current")
_WmanIf2BsSsOfdmaCapCfgMaxHarqBurst_Type = WmanIf2OfdmaMaxHarq
_WmanIf2BsSsOfdmaCapCfgMaxHarqBurst_Object = MibTableColumn
wmanIf2BsSsOfdmaCapCfgMaxHarqBurst = _WmanIf2BsSsOfdmaCapCfgMaxHarqBurst_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 16),
    _WmanIf2BsSsOfdmaCapCfgMaxHarqBurst_Type()
)
wmanIf2BsSsOfdmaCapCfgMaxHarqBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapCfgMaxHarqBurst.setStatus("current")
_WmanIf2BsSsOfdmaCapCfgModMimo_Type = WmanIf2OfdmaModMimo
_WmanIf2BsSsOfdmaCapCfgModMimo_Object = MibTableColumn
wmanIf2BsSsOfdmaCapCfgModMimo = _WmanIf2BsSsOfdmaCapCfgModMimo_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 17),
    _WmanIf2BsSsOfdmaCapCfgModMimo_Type()
)
wmanIf2BsSsOfdmaCapCfgModMimo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapCfgModMimo.setStatus("current")
_WmanIf2BsSsOfdmaCapCfgSdmaPilot_Type = WmanIf2SdmaPilotCap
_WmanIf2BsSsOfdmaCapCfgSdmaPilot_Object = MibTableColumn
wmanIf2BsSsOfdmaCapCfgSdmaPilot = _WmanIf2BsSsOfdmaCapCfgSdmaPilot_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 18),
    _WmanIf2BsSsOfdmaCapCfgSdmaPilot_Type()
)
wmanIf2BsSsOfdmaCapCfgSdmaPilot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapCfgSdmaPilot.setStatus("current")
_WmanIf2BsSsOfdmaCapCfgMultipleBurst_Type = WmanIf2MultiBurst
_WmanIf2BsSsOfdmaCapCfgMultipleBurst_Object = MibTableColumn
wmanIf2BsSsOfdmaCapCfgMultipleBurst = _WmanIf2BsSsOfdmaCapCfgMultipleBurst_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 19),
    _WmanIf2BsSsOfdmaCapCfgMultipleBurst_Type()
)
wmanIf2BsSsOfdmaCapCfgMultipleBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapCfgMultipleBurst.setStatus("current")
_WmanIf2BsSsOfdmaCapCfgIncrHarqBuffer_Type = WmanIf2IncrHarqBuf
_WmanIf2BsSsOfdmaCapCfgIncrHarqBuffer_Object = MibTableColumn
wmanIf2BsSsOfdmaCapCfgIncrHarqBuffer = _WmanIf2BsSsOfdmaCapCfgIncrHarqBuffer_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 20),
    _WmanIf2BsSsOfdmaCapCfgIncrHarqBuffer_Type()
)
wmanIf2BsSsOfdmaCapCfgIncrHarqBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapCfgIncrHarqBuffer.setStatus("current")
_WmanIf2BsSsOfdmaCapCfgChaseHarqBuffer_Type = WmanIf2ChaseHarqBuf
_WmanIf2BsSsOfdmaCapCfgChaseHarqBuffer_Object = MibTableColumn
wmanIf2BsSsOfdmaCapCfgChaseHarqBuffer = _WmanIf2BsSsOfdmaCapCfgChaseHarqBuffer_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 8, 1, 21),
    _WmanIf2BsSsOfdmaCapCfgChaseHarqBuffer_Type()
)
wmanIf2BsSsOfdmaCapCfgChaseHarqBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaCapCfgChaseHarqBuffer.setStatus("current")
_WmanIf2BsOfdmaExUplinkChannelTable_Object = MibTable
wmanIf2BsOfdmaExUplinkChannelTable = _WmanIf2BsOfdmaExUplinkChannelTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExUplinkChannelTable.setStatus("current")
_WmanIf2BsOfdmaExUplinkChannelEntry_Object = MibTableRow
wmanIf2BsOfdmaExUplinkChannelEntry = _WmanIf2BsOfdmaExUplinkChannelEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExUplinkChannelEntry.setStatus("current")


class _WmanIf2BsOfdmaExHandoverRangingStart_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExHandoverRangingStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaExHandoverRangingStart_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExHandoverRangingStart_Object = MibTableColumn
wmanIf2BsOfdmaExHandoverRangingStart = _WmanIf2BsOfdmaExHandoverRangingStart_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 1),
    _WmanIf2BsOfdmaExHandoverRangingStart_Type()
)
wmanIf2BsOfdmaExHandoverRangingStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExHandoverRangingStart.setStatus("current")


class _WmanIf2BsOfdmaExHandoverRangingEnd_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExHandoverRangingEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaExHandoverRangingEnd_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExHandoverRangingEnd_Object = MibTableColumn
wmanIf2BsOfdmaExHandoverRangingEnd = _WmanIf2BsOfdmaExHandoverRangingEnd_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 2),
    _WmanIf2BsOfdmaExHandoverRangingEnd_Type()
)
wmanIf2BsOfdmaExHandoverRangingEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExHandoverRangingEnd.setStatus("current")
_WmanIf2BsOfdmaExHARQAckDelayDLBurst_Type = WmanIf2HarqAckDelay
_WmanIf2BsOfdmaExHARQAckDelayDLBurst_Object = MibTableColumn
wmanIf2BsOfdmaExHARQAckDelayDLBurst = _WmanIf2BsOfdmaExHARQAckDelayDLBurst_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 3),
    _WmanIf2BsOfdmaExHARQAckDelayDLBurst_Type()
)
wmanIf2BsOfdmaExHARQAckDelayDLBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExHARQAckDelayDLBurst.setStatus("current")


class _WmanIf2BsOfdmaExUlAmcAlloPhyBandsBitmap_Type(OctetString):
    """Custom type wmanIf2BsOfdmaExUlAmcAlloPhyBandsBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6


_WmanIf2BsOfdmaExUlAmcAlloPhyBandsBitmap_Type.__name__ = "OctetString"
_WmanIf2BsOfdmaExUlAmcAlloPhyBandsBitmap_Object = MibTableColumn
wmanIf2BsOfdmaExUlAmcAlloPhyBandsBitmap = _WmanIf2BsOfdmaExUlAmcAlloPhyBandsBitmap_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 4),
    _WmanIf2BsOfdmaExUlAmcAlloPhyBandsBitmap_Type()
)
wmanIf2BsOfdmaExUlAmcAlloPhyBandsBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExUlAmcAlloPhyBandsBitmap.setStatus("current")


class _WmanIf2BsOfdmaExMaxRetransmission_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExMaxRetransmission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaExMaxRetransmission_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExMaxRetransmission_Object = MibTableColumn
wmanIf2BsOfdmaExMaxRetransmission = _WmanIf2BsOfdmaExMaxRetransmission_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 5),
    _WmanIf2BsOfdmaExMaxRetransmission_Type()
)
wmanIf2BsOfdmaExMaxRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExMaxRetransmission.setStatus("current")


class _WmanIf2BsOfdmaExNormalizedCnOverride_Type(OctetString):
    """Custom type wmanIf2BsOfdmaExNormalizedCnOverride based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_WmanIf2BsOfdmaExNormalizedCnOverride_Type.__name__ = "OctetString"
_WmanIf2BsOfdmaExNormalizedCnOverride_Object = MibTableColumn
wmanIf2BsOfdmaExNormalizedCnOverride = _WmanIf2BsOfdmaExNormalizedCnOverride_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 6),
    _WmanIf2BsOfdmaExNormalizedCnOverride_Type()
)
wmanIf2BsOfdmaExNormalizedCnOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExNormalizedCnOverride.setStatus("current")


class _WmanIf2BsOfdmaExSizeOfCqichId_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExSizeOfCqichId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2BsOfdmaExSizeOfCqichId_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExSizeOfCqichId_Object = MibTableColumn
wmanIf2BsOfdmaExSizeOfCqichId = _WmanIf2BsOfdmaExSizeOfCqichId_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 7),
    _WmanIf2BsOfdmaExSizeOfCqichId_Type()
)
wmanIf2BsOfdmaExSizeOfCqichId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExSizeOfCqichId.setStatus("current")


class _WmanIf2BsOfdmaExNormalizedCnValue_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExNormalizedCnValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_WmanIf2BsOfdmaExNormalizedCnValue_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExNormalizedCnValue_Object = MibTableColumn
wmanIf2BsOfdmaExNormalizedCnValue = _WmanIf2BsOfdmaExNormalizedCnValue_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 8),
    _WmanIf2BsOfdmaExNormalizedCnValue_Type()
)
wmanIf2BsOfdmaExNormalizedCnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExNormalizedCnValue.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExNormalizedCnValue.setUnits("dB")


class _WmanIf2BsOfdmaExNormalizedCnOverride2_Type(OctetString):
    """Custom type wmanIf2BsOfdmaExNormalizedCnOverride2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_WmanIf2BsOfdmaExNormalizedCnOverride2_Type.__name__ = "OctetString"
_WmanIf2BsOfdmaExNormalizedCnOverride2_Object = MibTableColumn
wmanIf2BsOfdmaExNormalizedCnOverride2 = _WmanIf2BsOfdmaExNormalizedCnOverride2_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 9),
    _WmanIf2BsOfdmaExNormalizedCnOverride2_Type()
)
wmanIf2BsOfdmaExNormalizedCnOverride2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExNormalizedCnOverride2.setStatus("current")


class _WmanIf2BsOfdmaExBandAmcEntryAvgCinr_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExBandAmcEntryAvgCinr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_WmanIf2BsOfdmaExBandAmcEntryAvgCinr_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExBandAmcEntryAvgCinr_Object = MibTableColumn
wmanIf2BsOfdmaExBandAmcEntryAvgCinr = _WmanIf2BsOfdmaExBandAmcEntryAvgCinr_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 10),
    _WmanIf2BsOfdmaExBandAmcEntryAvgCinr_Type()
)
wmanIf2BsOfdmaExBandAmcEntryAvgCinr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExBandAmcEntryAvgCinr.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExBandAmcEntryAvgCinr.setUnits("dB")


class _WmanIf2BsOfdmaExAasPreambleUpperBond_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExAasPreambleUpperBond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_WmanIf2BsOfdmaExAasPreambleUpperBond_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExAasPreambleUpperBond_Object = MibTableColumn
wmanIf2BsOfdmaExAasPreambleUpperBond = _WmanIf2BsOfdmaExAasPreambleUpperBond_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 11),
    _WmanIf2BsOfdmaExAasPreambleUpperBond_Type()
)
wmanIf2BsOfdmaExAasPreambleUpperBond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExAasPreambleUpperBond.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExAasPreambleUpperBond.setUnits("0.25 dB")


class _WmanIf2BsOfdmaExAasPreambleLowerBond_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExAasPreambleLowerBond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_WmanIf2BsOfdmaExAasPreambleLowerBond_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExAasPreambleLowerBond_Object = MibTableColumn
wmanIf2BsOfdmaExAasPreambleLowerBond = _WmanIf2BsOfdmaExAasPreambleLowerBond_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 12),
    _WmanIf2BsOfdmaExAasPreambleLowerBond_Type()
)
wmanIf2BsOfdmaExAasPreambleLowerBond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExAasPreambleLowerBond.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExAasPreambleLowerBond.setUnits("0.25 dB")
_WmanIf2BsOfdmaExAasBeamSelectAllowed_Type = WmanIf2AasBeamSel
_WmanIf2BsOfdmaExAasBeamSelectAllowed_Object = MibTableColumn
wmanIf2BsOfdmaExAasBeamSelectAllowed = _WmanIf2BsOfdmaExAasBeamSelectAllowed_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 13),
    _WmanIf2BsOfdmaExAasBeamSelectAllowed_Type()
)
wmanIf2BsOfdmaExAasBeamSelectAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExAasBeamSelectAllowed.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExAasBeamSelectAllowed.setUnits("0.25 dB")


class _WmanIf2BsOfdmaExCqichIndicationFlag_Type(OctetString):
    """Custom type wmanIf2BsOfdmaExCqichIndicationFlag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_WmanIf2BsOfdmaExCqichIndicationFlag_Type.__name__ = "OctetString"
_WmanIf2BsOfdmaExCqichIndicationFlag_Object = MibTableColumn
wmanIf2BsOfdmaExCqichIndicationFlag = _WmanIf2BsOfdmaExCqichIndicationFlag_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 14),
    _WmanIf2BsOfdmaExCqichIndicationFlag_Type()
)
wmanIf2BsOfdmaExCqichIndicationFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExCqichIndicationFlag.setStatus("current")
_WmanIf2BsOfdmaExUpPowerAdjStep_Type = Unsigned32
_WmanIf2BsOfdmaExUpPowerAdjStep_Object = MibTableColumn
wmanIf2BsOfdmaExUpPowerAdjStep = _WmanIf2BsOfdmaExUpPowerAdjStep_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 15),
    _WmanIf2BsOfdmaExUpPowerAdjStep_Type()
)
wmanIf2BsOfdmaExUpPowerAdjStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExUpPowerAdjStep.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExUpPowerAdjStep.setUnits("0.01 dB")
_WmanIf2BsOfdmaExDownPowerAdjStep_Type = Unsigned32
_WmanIf2BsOfdmaExDownPowerAdjStep_Object = MibTableColumn
wmanIf2BsOfdmaExDownPowerAdjStep = _WmanIf2BsOfdmaExDownPowerAdjStep_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 16),
    _WmanIf2BsOfdmaExDownPowerAdjStep_Type()
)
wmanIf2BsOfdmaExDownPowerAdjStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExDownPowerAdjStep.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExDownPowerAdjStep.setUnits("0.01 dB")
_WmanIf2BsOfdmaExMinPowerOffsetAdj_Type = Integer32
_WmanIf2BsOfdmaExMinPowerOffsetAdj_Object = MibTableColumn
wmanIf2BsOfdmaExMinPowerOffsetAdj = _WmanIf2BsOfdmaExMinPowerOffsetAdj_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 17),
    _WmanIf2BsOfdmaExMinPowerOffsetAdj_Type()
)
wmanIf2BsOfdmaExMinPowerOffsetAdj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExMinPowerOffsetAdj.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExMinPowerOffsetAdj.setUnits("0.1 dB")
_WmanIf2BsOfdmaExMaxPowerOffsetAdj_Type = Integer32
_WmanIf2BsOfdmaExMaxPowerOffsetAdj_Object = MibTableColumn
wmanIf2BsOfdmaExMaxPowerOffsetAdj = _WmanIf2BsOfdmaExMaxPowerOffsetAdj_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 18),
    _WmanIf2BsOfdmaExMaxPowerOffsetAdj_Type()
)
wmanIf2BsOfdmaExMaxPowerOffsetAdj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExMaxPowerOffsetAdj.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExMaxPowerOffsetAdj.setUnits("0.1 dB")


class _WmanIf2BsOfdmaExHandoverRngCodes_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExHandoverRngCodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaExHandoverRngCodes_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExHandoverRngCodes_Object = MibTableColumn
wmanIf2BsOfdmaExHandoverRngCodes = _WmanIf2BsOfdmaExHandoverRngCodes_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 19),
    _WmanIf2BsOfdmaExHandoverRngCodes_Type()
)
wmanIf2BsOfdmaExHandoverRngCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExHandoverRngCodes.setStatus("current")
_WmanIf2BsOfdmaExInitialRngInterval_Type = Integer32
_WmanIf2BsOfdmaExInitialRngInterval_Object = MibTableColumn
wmanIf2BsOfdmaExInitialRngInterval = _WmanIf2BsOfdmaExInitialRngInterval_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 20),
    _WmanIf2BsOfdmaExInitialRngInterval_Type()
)
wmanIf2BsOfdmaExInitialRngInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExInitialRngInterval.setStatus("current")


class _WmanIf2BsOfdmaExTxPwrRepThreshold_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExTxPwrRepThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaExTxPwrRepThreshold_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExTxPwrRepThreshold_Object = MibTableColumn
wmanIf2BsOfdmaExTxPwrRepThreshold = _WmanIf2BsOfdmaExTxPwrRepThreshold_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 21),
    _WmanIf2BsOfdmaExTxPwrRepThreshold_Type()
)
wmanIf2BsOfdmaExTxPwrRepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExTxPwrRepThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExTxPwrRepThreshold.setUnits("dB")


class _WmanIf2BsOfdmaExTprPower_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExTprPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaExTprPower_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExTprPower_Object = MibTableColumn
wmanIf2BsOfdmaExTprPower = _WmanIf2BsOfdmaExTprPower_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 22),
    _WmanIf2BsOfdmaExTprPower_Type()
)
wmanIf2BsOfdmaExTprPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExTprPower.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExTprPower.setUnits("dB")


class _WmanIf2BsOfdmaExAlphaPavg_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExAlphaPavg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaExAlphaPavg_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExAlphaPavg_Object = MibTableColumn
wmanIf2BsOfdmaExAlphaPavg = _WmanIf2BsOfdmaExAlphaPavg_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 23),
    _WmanIf2BsOfdmaExAlphaPavg_Type()
)
wmanIf2BsOfdmaExAlphaPavg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExAlphaPavg.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExAlphaPavg.setUnits("dB")


class _WmanIf2BsOfdmaExCqichTxPwrRepThreshold_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExCqichTxPwrRepThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaExCqichTxPwrRepThreshold_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExCqichTxPwrRepThreshold_Object = MibTableColumn
wmanIf2BsOfdmaExCqichTxPwrRepThreshold = _WmanIf2BsOfdmaExCqichTxPwrRepThreshold_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 24),
    _WmanIf2BsOfdmaExCqichTxPwrRepThreshold_Type()
)
wmanIf2BsOfdmaExCqichTxPwrRepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExCqichTxPwrRepThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExCqichTxPwrRepThreshold.setUnits("dB")


class _WmanIf2BsOfdmaExCqichTprPower_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExCqichTprPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaExCqichTprPower_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExCqichTprPower_Object = MibTableColumn
wmanIf2BsOfdmaExCqichTprPower = _WmanIf2BsOfdmaExCqichTprPower_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 25),
    _WmanIf2BsOfdmaExCqichTprPower_Type()
)
wmanIf2BsOfdmaExCqichTprPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExCqichTprPower.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExCqichTprPower.setUnits("dB")


class _WmanIf2BsOfdmaExCqichAlphaPavg_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExCqichAlphaPavg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaExCqichAlphaPavg_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExCqichAlphaPavg_Object = MibTableColumn
wmanIf2BsOfdmaExCqichAlphaPavg = _WmanIf2BsOfdmaExCqichAlphaPavg_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 26),
    _WmanIf2BsOfdmaExCqichAlphaPavg_Type()
)
wmanIf2BsOfdmaExCqichAlphaPavg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExCqichAlphaPavg.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExCqichAlphaPavg.setUnits("dB")
_WmanIf2BsOfdmaExNormalizedCnChSounding_Type = Integer32
_WmanIf2BsOfdmaExNormalizedCnChSounding_Object = MibTableColumn
wmanIf2BsOfdmaExNormalizedCnChSounding = _WmanIf2BsOfdmaExNormalizedCnChSounding_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 27),
    _WmanIf2BsOfdmaExNormalizedCnChSounding_Type()
)
wmanIf2BsOfdmaExNormalizedCnChSounding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExNormalizedCnChSounding.setStatus("current")


class _WmanIf2BsOfdmaExInitialRngBackoffStart_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExInitialRngBackoffStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaExInitialRngBackoffStart_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExInitialRngBackoffStart_Object = MibTableColumn
wmanIf2BsOfdmaExInitialRngBackoffStart = _WmanIf2BsOfdmaExInitialRngBackoffStart_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 28),
    _WmanIf2BsOfdmaExInitialRngBackoffStart_Type()
)
wmanIf2BsOfdmaExInitialRngBackoffStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExInitialRngBackoffStart.setStatus("current")


class _WmanIf2BsOfdmaExInitialRngBackoffEnd_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExInitialRngBackoffEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaExInitialRngBackoffEnd_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExInitialRngBackoffEnd_Object = MibTableColumn
wmanIf2BsOfdmaExInitialRngBackoffEnd = _WmanIf2BsOfdmaExInitialRngBackoffEnd_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 29),
    _WmanIf2BsOfdmaExInitialRngBackoffEnd_Type()
)
wmanIf2BsOfdmaExInitialRngBackoffEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExInitialRngBackoffEnd.setStatus("current")


class _WmanIf2BsOfdmaExBwRequestBackoffStart_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExBwRequestBackoffStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaExBwRequestBackoffStart_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExBwRequestBackoffStart_Object = MibTableColumn
wmanIf2BsOfdmaExBwRequestBackoffStart = _WmanIf2BsOfdmaExBwRequestBackoffStart_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 30),
    _WmanIf2BsOfdmaExBwRequestBackoffStart_Type()
)
wmanIf2BsOfdmaExBwRequestBackoffStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExBwRequestBackoffStart.setStatus("current")


class _WmanIf2BsOfdmaExBwRequestBackoffEnd_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExBwRequestBackoffEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaExBwRequestBackoffEnd_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExBwRequestBackoffEnd_Object = MibTableColumn
wmanIf2BsOfdmaExBwRequestBackoffEnd = _WmanIf2BsOfdmaExBwRequestBackoffEnd_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 9, 1, 31),
    _WmanIf2BsOfdmaExBwRequestBackoffEnd_Type()
)
wmanIf2BsOfdmaExBwRequestBackoffEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExBwRequestBackoffEnd.setStatus("current")
_WmanIf2BsOfdmaExDownlinkChannelTable_Object = MibTable
wmanIf2BsOfdmaExDownlinkChannelTable = _WmanIf2BsOfdmaExDownlinkChannelTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 10)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExDownlinkChannelTable.setStatus("current")
_WmanIf2BsOfdmaExDownlinkChannelEntry_Object = MibTableRow
wmanIf2BsOfdmaExDownlinkChannelEntry = _WmanIf2BsOfdmaExDownlinkChannelEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 10, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExDownlinkChannelEntry.setStatus("current")
_WmanIf2BsOfdmaExHARQAckDelayULBurst_Type = WmanIf2HarqAckDelay
_WmanIf2BsOfdmaExHARQAckDelayULBurst_Object = MibTableColumn
wmanIf2BsOfdmaExHARQAckDelayULBurst = _WmanIf2BsOfdmaExHARQAckDelayULBurst_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 10, 1, 1),
    _WmanIf2BsOfdmaExHARQAckDelayULBurst_Type()
)
wmanIf2BsOfdmaExHARQAckDelayULBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExHARQAckDelayULBurst.setStatus("current")
_WmanIf2BsOfdmaExHarqZonePermutation_Type = WmanIfPermutationType
_WmanIf2BsOfdmaExHarqZonePermutation_Object = MibTableColumn
wmanIf2BsOfdmaExHarqZonePermutation = _WmanIf2BsOfdmaExHarqZonePermutation_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 10, 1, 2),
    _WmanIf2BsOfdmaExHarqZonePermutation_Type()
)
wmanIf2BsOfdmaExHarqZonePermutation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExHarqZonePermutation.setStatus("current")


class _WmanIf2BsOfdmaExHMaxRetransmission_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExHMaxRetransmission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaExHMaxRetransmission_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExHMaxRetransmission_Object = MibTableColumn
wmanIf2BsOfdmaExHMaxRetransmission = _WmanIf2BsOfdmaExHMaxRetransmission_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 10, 1, 3),
    _WmanIf2BsOfdmaExHMaxRetransmission_Type()
)
wmanIf2BsOfdmaExHMaxRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExHMaxRetransmission.setStatus("current")


class _WmanIf2BsOfdmaExCinrAlphaAvg_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExCinrAlphaAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaExCinrAlphaAvg_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExCinrAlphaAvg_Object = MibTableColumn
wmanIf2BsOfdmaExCinrAlphaAvg = _WmanIf2BsOfdmaExCinrAlphaAvg_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 10, 1, 4),
    _WmanIf2BsOfdmaExCinrAlphaAvg_Type()
)
wmanIf2BsOfdmaExCinrAlphaAvg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExCinrAlphaAvg.setStatus("current")


class _WmanIf2BsOfdmaExRssiAlphaAvg_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExRssiAlphaAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaExRssiAlphaAvg_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExRssiAlphaAvg_Object = MibTableColumn
wmanIf2BsOfdmaExRssiAlphaAvg = _WmanIf2BsOfdmaExRssiAlphaAvg_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 10, 1, 5),
    _WmanIf2BsOfdmaExRssiAlphaAvg_Type()
)
wmanIf2BsOfdmaExRssiAlphaAvg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExRssiAlphaAvg.setStatus("current")


class _WmanIf2BsOfdmaExDlAmcAlloPhyBandsBitmap_Type(OctetString):
    """Custom type wmanIf2BsOfdmaExDlAmcAlloPhyBandsBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6


_WmanIf2BsOfdmaExDlAmcAlloPhyBandsBitmap_Type.__name__ = "OctetString"
_WmanIf2BsOfdmaExDlAmcAlloPhyBandsBitmap_Object = MibTableColumn
wmanIf2BsOfdmaExDlAmcAlloPhyBandsBitmap = _WmanIf2BsOfdmaExDlAmcAlloPhyBandsBitmap_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 10, 1, 6),
    _WmanIf2BsOfdmaExDlAmcAlloPhyBandsBitmap_Type()
)
wmanIf2BsOfdmaExDlAmcAlloPhyBandsBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExDlAmcAlloPhyBandsBitmap.setStatus("current")
_WmanIf2BsOfdmaExHandoverSupported_Type = WmanIf2HoSupportType
_WmanIf2BsOfdmaExHandoverSupported_Object = MibTableColumn
wmanIf2BsOfdmaExHandoverSupported = _WmanIf2BsOfdmaExHandoverSupported_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 10, 1, 7),
    _WmanIf2BsOfdmaExHandoverSupported_Type()
)
wmanIf2BsOfdmaExHandoverSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExHandoverSupported.setStatus("current")


class _WmanIf2BsOfdmaExThresholdAddBsDivSet_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExThresholdAddBsDivSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaExThresholdAddBsDivSet_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExThresholdAddBsDivSet_Object = MibTableColumn
wmanIf2BsOfdmaExThresholdAddBsDivSet = _WmanIf2BsOfdmaExThresholdAddBsDivSet_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 10, 1, 8),
    _WmanIf2BsOfdmaExThresholdAddBsDivSet_Type()
)
wmanIf2BsOfdmaExThresholdAddBsDivSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExThresholdAddBsDivSet.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExThresholdAddBsDivSet.setUnits("dB")


class _WmanIf2BsOfdmaExThresholdDelBsDivSet_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExThresholdDelBsDivSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaExThresholdDelBsDivSet_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExThresholdDelBsDivSet_Object = MibTableColumn
wmanIf2BsOfdmaExThresholdDelBsDivSet = _WmanIf2BsOfdmaExThresholdDelBsDivSet_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 10, 1, 9),
    _WmanIf2BsOfdmaExThresholdDelBsDivSet_Type()
)
wmanIf2BsOfdmaExThresholdDelBsDivSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExThresholdDelBsDivSet.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExThresholdDelBsDivSet.setUnits("dB")


class _WmanIf2BsOfdmaExAsrSlotLength_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExAsrSlotLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaExAsrSlotLength_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExAsrSlotLength_Object = MibTableColumn
wmanIf2BsOfdmaExAsrSlotLength = _WmanIf2BsOfdmaExAsrSlotLength_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 10, 1, 10),
    _WmanIf2BsOfdmaExAsrSlotLength_Type()
)
wmanIf2BsOfdmaExAsrSlotLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExAsrSlotLength.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExAsrSlotLength.setUnits("Frames")


class _WmanIf2BsOfdmaExAsrSwitchingPeriod_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExAsrSwitchingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaExAsrSwitchingPeriod_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExAsrSwitchingPeriod_Object = MibTableColumn
wmanIf2BsOfdmaExAsrSwitchingPeriod = _WmanIf2BsOfdmaExAsrSwitchingPeriod_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 10, 1, 11),
    _WmanIf2BsOfdmaExAsrSwitchingPeriod_Type()
)
wmanIf2BsOfdmaExAsrSwitchingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExAsrSwitchingPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExAsrSwitchingPeriod.setUnits("ASR slots")


class _WmanIf2BsOfdmaExHysteresisMargin_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExHysteresisMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 57),
    )


_WmanIf2BsOfdmaExHysteresisMargin_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExHysteresisMargin_Object = MibTableColumn
wmanIf2BsOfdmaExHysteresisMargin = _WmanIf2BsOfdmaExHysteresisMargin_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 10, 1, 12),
    _WmanIf2BsOfdmaExHysteresisMargin_Type()
)
wmanIf2BsOfdmaExHysteresisMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExHysteresisMargin.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExHysteresisMargin.setUnits("dB")
_WmanIf2BsOfdmaExTimeToTrigger_Type = Integer32
_WmanIf2BsOfdmaExTimeToTrigger_Object = MibTableColumn
wmanIf2BsOfdmaExTimeToTrigger = _WmanIf2BsOfdmaExTimeToTrigger_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 10, 1, 13),
    _WmanIf2BsOfdmaExTimeToTrigger_Type()
)
wmanIf2BsOfdmaExTimeToTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExTimeToTrigger.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExTimeToTrigger.setUnits("milliseconds")


class _WmanIf2BsOfdmaExRestartCount_Type(Integer32):
    """Custom type wmanIf2BsOfdmaExRestartCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaExRestartCount_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaExRestartCount_Object = MibTableColumn
wmanIf2BsOfdmaExRestartCount = _WmanIf2BsOfdmaExRestartCount_Object(
    (1, 0, 8802, 16, 2, 1, 1, 6, 2, 10, 1, 14),
    _WmanIf2BsOfdmaExRestartCount_Type()
)
wmanIf2BsOfdmaExRestartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaExRestartCount.setStatus("current")
_WmanIf2CommonObjects_ObjectIdentity = ObjectIdentity
wmanIf2CommonObjects = _WmanIf2CommonObjects_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 3)
)
_WmanIf2CmnCps_ObjectIdentity = ObjectIdentity
wmanIf2CmnCps = _WmanIf2CmnCps_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 3, 2)
)
_WmanIf2CmnCpsServiceFlowTable_Object = MibTable
wmanIf2CmnCpsServiceFlowTable = _WmanIf2CmnCpsServiceFlowTable_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIf2CmnCpsServiceFlowTable.setStatus("current")
_WmanIf2CmnCpsServiceFlowEntry_Object = MibTableRow
wmanIf2CmnCpsServiceFlowEntry = _WmanIf2CmnCpsServiceFlowEntry_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1)
)
wmanIf2CmnCpsServiceFlowEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-MIB", "wmanIf2CmnCpsSfMacAddress"),
    (0, "WMAN-IF2-MIB", "wmanIf2CmnCpsSfId"),
)
if mibBuilder.loadTexts:
    wmanIf2CmnCpsServiceFlowEntry.setStatus("current")
_WmanIf2CmnCpsSfMacAddress_Type = MacAddress
_WmanIf2CmnCpsSfMacAddress_Object = MibTableColumn
wmanIf2CmnCpsSfMacAddress = _WmanIf2CmnCpsSfMacAddress_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 1),
    _WmanIf2CmnCpsSfMacAddress_Type()
)
wmanIf2CmnCpsSfMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsSfMacAddress.setStatus("current")


class _WmanIf2CmnCpsSfId_Type(Unsigned32):
    """Custom type wmanIf2CmnCpsSfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIf2CmnCpsSfId_Type.__name__ = "Unsigned32"
_WmanIf2CmnCpsSfId_Object = MibTableColumn
wmanIf2CmnCpsSfId = _WmanIf2CmnCpsSfId_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 2),
    _WmanIf2CmnCpsSfId_Type()
)
wmanIf2CmnCpsSfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsSfId.setStatus("current")
_WmanIf2CmnCpsSfCid_Type = WmanIf2CidType
_WmanIf2CmnCpsSfCid_Object = MibTableColumn
wmanIf2CmnCpsSfCid = _WmanIf2CmnCpsSfCid_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 3),
    _WmanIf2CmnCpsSfCid_Type()
)
wmanIf2CmnCpsSfCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsSfCid.setStatus("current")


class _WmanIf2CmnCpsSfDirection_Type(Integer32):
    """Custom type wmanIf2CmnCpsSfDirection based on Integer32"""
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


_WmanIf2CmnCpsSfDirection_Type.__name__ = "Integer32"
_WmanIf2CmnCpsSfDirection_Object = MibTableColumn
wmanIf2CmnCpsSfDirection = _WmanIf2CmnCpsSfDirection_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 4),
    _WmanIf2CmnCpsSfDirection_Type()
)
wmanIf2CmnCpsSfDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsSfDirection.setStatus("current")
_WmanIf2CmnCpsSfState_Type = WmanIf2SfState
_WmanIf2CmnCpsSfState_Object = MibTableColumn
wmanIf2CmnCpsSfState = _WmanIf2CmnCpsSfState_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 5),
    _WmanIf2CmnCpsSfState_Type()
)
wmanIf2CmnCpsSfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsSfState.setStatus("current")


class _WmanIf2CmnCpsTrafficPriority_Type(Integer32):
    """Custom type wmanIf2CmnCpsTrafficPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2CmnCpsTrafficPriority_Type.__name__ = "Integer32"
_WmanIf2CmnCpsTrafficPriority_Object = MibTableColumn
wmanIf2CmnCpsTrafficPriority = _WmanIf2CmnCpsTrafficPriority_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 6),
    _WmanIf2CmnCpsTrafficPriority_Type()
)
wmanIf2CmnCpsTrafficPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsTrafficPriority.setStatus("current")
_WmanIf2CmnCpsMaxSustainedRate_Type = Unsigned32
_WmanIf2CmnCpsMaxSustainedRate_Object = MibTableColumn
wmanIf2CmnCpsMaxSustainedRate = _WmanIf2CmnCpsMaxSustainedRate_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 7),
    _WmanIf2CmnCpsMaxSustainedRate_Type()
)
wmanIf2CmnCpsMaxSustainedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsMaxSustainedRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsMaxSustainedRate.setUnits("b/s")
_WmanIf2CmnCpsMaxTrafficBurst_Type = Unsigned32
_WmanIf2CmnCpsMaxTrafficBurst_Object = MibTableColumn
wmanIf2CmnCpsMaxTrafficBurst = _WmanIf2CmnCpsMaxTrafficBurst_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 8),
    _WmanIf2CmnCpsMaxTrafficBurst_Type()
)
wmanIf2CmnCpsMaxTrafficBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsMaxTrafficBurst.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsMaxTrafficBurst.setUnits("byte")
_WmanIf2CmnCpsMinReservedRate_Type = Unsigned32
_WmanIf2CmnCpsMinReservedRate_Object = MibTableColumn
wmanIf2CmnCpsMinReservedRate = _WmanIf2CmnCpsMinReservedRate_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 9),
    _WmanIf2CmnCpsMinReservedRate_Type()
)
wmanIf2CmnCpsMinReservedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsMinReservedRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsMinReservedRate.setUnits("byte")
_WmanIf2CmnCpsToleratedJitter_Type = Unsigned32
_WmanIf2CmnCpsToleratedJitter_Object = MibTableColumn
wmanIf2CmnCpsToleratedJitter = _WmanIf2CmnCpsToleratedJitter_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 10),
    _WmanIf2CmnCpsToleratedJitter_Type()
)
wmanIf2CmnCpsToleratedJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsToleratedJitter.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsToleratedJitter.setUnits("millisecond")
_WmanIf2CmnCpsMaxLatency_Type = Unsigned32
_WmanIf2CmnCpsMaxLatency_Object = MibTableColumn
wmanIf2CmnCpsMaxLatency = _WmanIf2CmnCpsMaxLatency_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 11),
    _WmanIf2CmnCpsMaxLatency_Type()
)
wmanIf2CmnCpsMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsMaxLatency.setUnits("millisecond")


class _WmanIf2CmnCpsFixedVsVariableSduInd_Type(Integer32):
    """Custom type wmanIf2CmnCpsFixedVsVariableSduInd based on Integer32"""
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


_WmanIf2CmnCpsFixedVsVariableSduInd_Type.__name__ = "Integer32"
_WmanIf2CmnCpsFixedVsVariableSduInd_Object = MibTableColumn
wmanIf2CmnCpsFixedVsVariableSduInd = _WmanIf2CmnCpsFixedVsVariableSduInd_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 12),
    _WmanIf2CmnCpsFixedVsVariableSduInd_Type()
)
wmanIf2CmnCpsFixedVsVariableSduInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsFixedVsVariableSduInd.setStatus("current")
_WmanIf2CmnCpsSduSize_Type = Unsigned32
_WmanIf2CmnCpsSduSize_Object = MibTableColumn
wmanIf2CmnCpsSduSize = _WmanIf2CmnCpsSduSize_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 13),
    _WmanIf2CmnCpsSduSize_Type()
)
wmanIf2CmnCpsSduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsSduSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsSduSize.setUnits("byte")
_WmanIf2CmnCpsSfSchedulingType_Type = WmanIf2SfSchedulingType
_WmanIf2CmnCpsSfSchedulingType_Object = MibTableColumn
wmanIf2CmnCpsSfSchedulingType = _WmanIf2CmnCpsSfSchedulingType_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 14),
    _WmanIf2CmnCpsSfSchedulingType_Type()
)
wmanIf2CmnCpsSfSchedulingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsSfSchedulingType.setStatus("current")
_WmanIf2CmnCpsArqEnable_Type = TruthValue
_WmanIf2CmnCpsArqEnable_Object = MibTableColumn
wmanIf2CmnCpsArqEnable = _WmanIf2CmnCpsArqEnable_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 15),
    _WmanIf2CmnCpsArqEnable_Type()
)
wmanIf2CmnCpsArqEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsArqEnable.setStatus("current")


class _WmanIf2CmnCpsArqWindowSize_Type(Integer32):
    """Custom type wmanIf2CmnCpsArqWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WmanIf2CmnCpsArqWindowSize_Type.__name__ = "Integer32"
_WmanIf2CmnCpsArqWindowSize_Object = MibTableColumn
wmanIf2CmnCpsArqWindowSize = _WmanIf2CmnCpsArqWindowSize_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 16),
    _WmanIf2CmnCpsArqWindowSize_Type()
)
wmanIf2CmnCpsArqWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsArqWindowSize.setStatus("current")


class _WmanIf2CmnCpsArqBlockLifetime_Type(Integer32):
    """Custom type wmanIf2CmnCpsArqBlockLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2CmnCpsArqBlockLifetime_Type.__name__ = "Integer32"
_WmanIf2CmnCpsArqBlockLifetime_Object = MibTableColumn
wmanIf2CmnCpsArqBlockLifetime = _WmanIf2CmnCpsArqBlockLifetime_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 17),
    _WmanIf2CmnCpsArqBlockLifetime_Type()
)
wmanIf2CmnCpsArqBlockLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsArqBlockLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsArqBlockLifetime.setUnits("10 us")


class _WmanIf2CmnCpsArqSyncLossTimeout_Type(Integer32):
    """Custom type wmanIf2CmnCpsArqSyncLossTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2CmnCpsArqSyncLossTimeout_Type.__name__ = "Integer32"
_WmanIf2CmnCpsArqSyncLossTimeout_Object = MibTableColumn
wmanIf2CmnCpsArqSyncLossTimeout = _WmanIf2CmnCpsArqSyncLossTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 18),
    _WmanIf2CmnCpsArqSyncLossTimeout_Type()
)
wmanIf2CmnCpsArqSyncLossTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsArqSyncLossTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsArqSyncLossTimeout.setUnits("10 us")
_WmanIf2CmnCpsArqDeliverInOrder_Type = TruthValue
_WmanIf2CmnCpsArqDeliverInOrder_Object = MibTableColumn
wmanIf2CmnCpsArqDeliverInOrder = _WmanIf2CmnCpsArqDeliverInOrder_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 19),
    _WmanIf2CmnCpsArqDeliverInOrder_Type()
)
wmanIf2CmnCpsArqDeliverInOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsArqDeliverInOrder.setStatus("current")


class _WmanIf2CmnCpsArqRxPurgeTimeout_Type(Integer32):
    """Custom type wmanIf2CmnCpsArqRxPurgeTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2CmnCpsArqRxPurgeTimeout_Type.__name__ = "Integer32"
_WmanIf2CmnCpsArqRxPurgeTimeout_Object = MibTableColumn
wmanIf2CmnCpsArqRxPurgeTimeout = _WmanIf2CmnCpsArqRxPurgeTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 20),
    _WmanIf2CmnCpsArqRxPurgeTimeout_Type()
)
wmanIf2CmnCpsArqRxPurgeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsArqRxPurgeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsArqRxPurgeTimeout.setUnits("10 us")


class _WmanIf2CmnCpsArqBlockSize_Type(Integer32):
    """Custom type wmanIf2CmnCpsArqBlockSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2040),
    )


_WmanIf2CmnCpsArqBlockSize_Type.__name__ = "Integer32"
_WmanIf2CmnCpsArqBlockSize_Object = MibTableColumn
wmanIf2CmnCpsArqBlockSize = _WmanIf2CmnCpsArqBlockSize_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 21),
    _WmanIf2CmnCpsArqBlockSize_Type()
)
wmanIf2CmnCpsArqBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsArqBlockSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsArqBlockSize.setUnits("byte")
_WmanIf2CmnCpsMinRsvdTolerableRate_Type = Unsigned32
_WmanIf2CmnCpsMinRsvdTolerableRate_Object = MibTableColumn
wmanIf2CmnCpsMinRsvdTolerableRate = _WmanIf2CmnCpsMinRsvdTolerableRate_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 22),
    _WmanIf2CmnCpsMinRsvdTolerableRate_Type()
)
wmanIf2CmnCpsMinRsvdTolerableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsMinRsvdTolerableRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsMinRsvdTolerableRate.setUnits("b/s")


class _WmanIf2CmnCpsReqTxPolicy_Type(Bits):
    """Custom type wmanIf2CmnCpsReqTxPolicy based on Bits"""
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

_WmanIf2CmnCpsReqTxPolicy_Type.__name__ = "Bits"
_WmanIf2CmnCpsReqTxPolicy_Object = MibTableColumn
wmanIf2CmnCpsReqTxPolicy = _WmanIf2CmnCpsReqTxPolicy_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 23),
    _WmanIf2CmnCpsReqTxPolicy_Type()
)
wmanIf2CmnCpsReqTxPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsReqTxPolicy.setStatus("current")
_WmanIf2CmnSfCsSpecification_Type = WmanIf2CsSpecification
_WmanIf2CmnSfCsSpecification_Object = MibTableColumn
wmanIf2CmnSfCsSpecification = _WmanIf2CmnSfCsSpecification_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 24),
    _WmanIf2CmnSfCsSpecification_Type()
)
wmanIf2CmnSfCsSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnSfCsSpecification.setStatus("current")


class _WmanIf2CmnCpsTargetSaid_Type(Integer32):
    """Custom type wmanIf2CmnCpsTargetSaid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2CmnCpsTargetSaid_Type.__name__ = "Integer32"
_WmanIf2CmnCpsTargetSaid_Object = MibTableColumn
wmanIf2CmnCpsTargetSaid = _WmanIf2CmnCpsTargetSaid_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 1, 1, 25),
    _WmanIf2CmnCpsTargetSaid_Type()
)
wmanIf2CmnCpsTargetSaid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2CmnCpsTargetSaid.setStatus("current")
_WmanIf2CmnBsSsConfigurationTable_Object = MibTable
wmanIf2CmnBsSsConfigurationTable = _WmanIf2CmnBsSsConfigurationTable_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    wmanIf2CmnBsSsConfigurationTable.setStatus("current")
_WmanIf2CmnBsSsConfigurationEntry_Object = MibTableRow
wmanIf2CmnBsSsConfigurationEntry = _WmanIf2CmnBsSsConfigurationEntry_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 2, 1)
)
wmanIf2CmnBsSsConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2CmnBsSsConfigurationEntry.setStatus("current")


class _WmanIf2CmnInvitedRangRetries_Type(Integer32):
    """Custom type wmanIf2CmnInvitedRangRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 65535),
    )


_WmanIf2CmnInvitedRangRetries_Type.__name__ = "Integer32"
_WmanIf2CmnInvitedRangRetries_Object = MibTableColumn
wmanIf2CmnInvitedRangRetries = _WmanIf2CmnInvitedRangRetries_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 2, 1, 1),
    _WmanIf2CmnInvitedRangRetries_Type()
)
wmanIf2CmnInvitedRangRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2CmnInvitedRangRetries.setStatus("current")
_WmanIf2CmnDSxReqRetries_Type = Unsigned32
_WmanIf2CmnDSxReqRetries_Object = MibTableColumn
wmanIf2CmnDSxReqRetries = _WmanIf2CmnDSxReqRetries_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 2, 1, 2),
    _WmanIf2CmnDSxReqRetries_Type()
)
wmanIf2CmnDSxReqRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2CmnDSxReqRetries.setStatus("current")
_WmanIf2CmnDSxRespRetries_Type = Unsigned32
_WmanIf2CmnDSxRespRetries_Object = MibTableColumn
wmanIf2CmnDSxRespRetries = _WmanIf2CmnDSxRespRetries_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 2, 1, 3),
    _WmanIf2CmnDSxRespRetries_Type()
)
wmanIf2CmnDSxRespRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2CmnDSxRespRetries.setStatus("current")


class _WmanIf2CmnT7Timeout_Type(Integer32):
    """Custom type wmanIf2CmnT7Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WmanIf2CmnT7Timeout_Type.__name__ = "Integer32"
_WmanIf2CmnT7Timeout_Object = MibTableColumn
wmanIf2CmnT7Timeout = _WmanIf2CmnT7Timeout_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 2, 1, 4),
    _WmanIf2CmnT7Timeout_Type()
)
wmanIf2CmnT7Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2CmnT7Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2CmnT7Timeout.setUnits("milliseconds")


class _WmanIf2CmnT8Timeout_Type(Integer32):
    """Custom type wmanIf2CmnT8Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_WmanIf2CmnT8Timeout_Type.__name__ = "Integer32"
_WmanIf2CmnT8Timeout_Object = MibTableColumn
wmanIf2CmnT8Timeout = _WmanIf2CmnT8Timeout_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 2, 1, 5),
    _WmanIf2CmnT8Timeout_Type()
)
wmanIf2CmnT8Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2CmnT8Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2CmnT8Timeout.setUnits("milliseconds")


class _WmanIf2CmnT10Timeout_Type(Integer32):
    """Custom type wmanIf2CmnT10Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_WmanIf2CmnT10Timeout_Type.__name__ = "Integer32"
_WmanIf2CmnT10Timeout_Object = MibTableColumn
wmanIf2CmnT10Timeout = _WmanIf2CmnT10Timeout_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 2, 1, 6),
    _WmanIf2CmnT10Timeout_Type()
)
wmanIf2CmnT10Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2CmnT10Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2CmnT10Timeout.setUnits("milliseconds")


class _WmanIf2CmnT22Timeout_Type(Integer32):
    """Custom type wmanIf2CmnT22Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_WmanIf2CmnT22Timeout_Type.__name__ = "Integer32"
_WmanIf2CmnT22Timeout_Object = MibTableColumn
wmanIf2CmnT22Timeout = _WmanIf2CmnT22Timeout_Object(
    (1, 0, 8802, 16, 2, 1, 3, 2, 2, 1, 7),
    _WmanIf2CmnT22Timeout_Type()
)
wmanIf2CmnT22Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2CmnT22Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2CmnT22Timeout.setUnits("milliseconds")
_WmanIf2MibConformance_ObjectIdentity = ObjectIdentity
wmanIf2MibConformance = _WmanIf2MibConformance_ObjectIdentity(
    (1, 0, 8802, 16, 2, 2)
)
_WmanIf2MibGroups_ObjectIdentity = ObjectIdentity
wmanIf2MibGroups = _WmanIf2MibGroups_ObjectIdentity(
    (1, 0, 8802, 16, 2, 2, 1)
)
_WmanIf2MibCompliances_ObjectIdentity = ObjectIdentity
wmanIf2MibCompliances = _WmanIf2MibCompliances_ObjectIdentity(
    (1, 0, 8802, 16, 2, 2, 2)
)
wmanIf2BsOfdmaUplinkChannelEntry.registerAugmentions(
    ("WMAN-IF2-MIB",
     "wmanIf2BsOfdmaExUplinkChannelEntry")
)
wmanIf2BsOfdmaExUplinkChannelEntry.setIndexNames(*wmanIf2BsOfdmaUplinkChannelEntry.getIndexNames())
wmanIf2BsOfdmaDownlinkChannelEntry.registerAugmentions(
    ("WMAN-IF2-MIB",
     "wmanIf2BsOfdmaExDownlinkChannelEntry")
)
wmanIf2BsOfdmaExDownlinkChannelEntry.setIndexNames(*wmanIf2BsOfdmaDownlinkChannelEntry.getIndexNames())

# Managed Objects groups

wmanIf2MibCommonGroup = ObjectGroup(
    (1, 0, 8802, 16, 2, 2, 1, 1)
)
wmanIf2MibCommonGroup.setObjects(
      *(("WMAN-IF2-MIB", "wmanIf2CmnCpsTargetSaid"),
        ("WMAN-IF2-MIB", "wmanIf2CmnInvitedRangRetries"),
        ("WMAN-IF2-MIB", "wmanIf2CmnDSxReqRetries"),
        ("WMAN-IF2-MIB", "wmanIf2CmnDSxRespRetries"),
        ("WMAN-IF2-MIB", "wmanIf2CmnT7Timeout"),
        ("WMAN-IF2-MIB", "wmanIf2CmnT8Timeout"),
        ("WMAN-IF2-MIB", "wmanIf2CmnT10Timeout"),
        ("WMAN-IF2-MIB", "wmanIf2CmnT22Timeout"))
)
if mibBuilder.loadTexts:
    wmanIf2MibCommonGroup.setStatus("current")

wmanIf2MibQoSGroup = ObjectGroup(
    (1, 0, 8802, 16, 2, 2, 1, 2)
)
wmanIf2MibQoSGroup.setObjects(
      *(("WMAN-IF2-MIB", "wmanIf2CmnCpsSfId"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsSfCid"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsSfDirection"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsSfState"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsTrafficPriority"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsMaxSustainedRate"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsMaxTrafficBurst"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsMinReservedRate"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsToleratedJitter"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsMaxLatency"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsFixedVsVariableSduInd"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsSduSize"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsSfSchedulingType"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsArqEnable"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsArqWindowSize"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsArqBlockLifetime"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsArqSyncLossTimeout"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsArqDeliverInOrder"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsArqRxPurgeTimeout"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsArqBlockSize"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsMinRsvdTolerableRate"),
        ("WMAN-IF2-MIB", "wmanIf2CmnCpsReqTxPolicy"),
        ("WMAN-IF2-MIB", "wmanIf2CmnSfCsSpecification"))
)
if mibBuilder.loadTexts:
    wmanIf2MibQoSGroup.setStatus("current")

wmanIf2MibBsGroup = ObjectGroup(
    (1, 0, 8802, 16, 2, 2, 1, 3)
)
wmanIf2MibBsGroup.setObjects(
      *(("WMAN-IF2-MIB", "wmanIf2BsSsMacSduCount"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOctetCount"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsResetCounter"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsResetCounterTime"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsBasicCid"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsPrimaryCid"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsSecondaryCid"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsManagementSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsIpManagementMode"),
        ("WMAN-IF2-MIB", "wmanIf2Bs2ndMgmtDlQoSProfileIndex"),
        ("WMAN-IF2-MIB", "wmanIf2Bs2ndMgmtUlQoSProfileIndex"),
        ("WMAN-IF2-MIB", "wmanIf2BsAutoSfidEnabled"),
        ("WMAN-IF2-MIB", "wmanIf2BsAutoSfidRangeMin"),
        ("WMAN-IF2-MIB", "wmanIf2BsAutoSfidRangeMax"),
        ("WMAN-IF2-MIB", "wmanIf2BsResetSector"),
        ("WMAN-IF2-MIB", "wmanIf2BsSs2ndMgmtArqEnable"),
        ("WMAN-IF2-MIB", "wmanIf2BsSs2ndMgmtArqWindowSize"),
        ("WMAN-IF2-MIB", "wmanIf2BsSs2ndMgmtArqDnLinkTxDelay"),
        ("WMAN-IF2-MIB", "wmanIf2BsSs2ndMgmtArqUpLinkTxDelay"),
        ("WMAN-IF2-MIB", "wmanIf2BsSs2ndMgmtArqDnLinkRxDelay"),
        ("WMAN-IF2-MIB", "wmanIf2BsSs2ndMgmtArqUpLinkRxDelay"),
        ("WMAN-IF2-MIB", "wmanIf2BsSs2ndMgmtArqBlockLifetime"),
        ("WMAN-IF2-MIB", "wmanIf2BsSs2ndMgmtArqSyncLossTimeout"),
        ("WMAN-IF2-MIB", "wmanIf2BsSs2ndMgmtArqDeliverInOrder"),
        ("WMAN-IF2-MIB", "wmanIf2BsSs2ndMgmtArqRxPurgeTimeout"),
        ("WMAN-IF2-MIB", "wmanIf2BsSs2ndMgmtArqBlockSize"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsVendorIdEncoding"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsAasBroadcastPermission"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsMaxTxPowerBpsk"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsMaxTxPowerQpsk"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsMaxTxPower16Qam"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsMaxTxPower64Qam"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsMacVersion"),
        ("WMAN-IF2-MIB", "wmanIf2BsDcdInterval"),
        ("WMAN-IF2-MIB", "wmanIf2BsUcdInterval"),
        ("WMAN-IF2-MIB", "wmanIf2BsUcdTransition"),
        ("WMAN-IF2-MIB", "wmanIf2BsDcdTransition"),
        ("WMAN-IF2-MIB", "wmanIf2BsT9Timeout"),
        ("WMAN-IF2-MIB", "wmanIf2BsInitialRangingInterval"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsULMapProcTime"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsRangRespProcTime"),
        ("WMAN-IF2-MIB", "wmanIf2BsT13Timeout"),
        ("WMAN-IF2-MIB", "wmanIf2BsT15Timeout"),
        ("WMAN-IF2-MIB", "wmanIf2BsT17Timeout"),
        ("WMAN-IF2-MIB", "wmanIf2BsT27IdleTimer"),
        ("WMAN-IF2-MIB", "wmanIf2BsT27ActiveTimer"),
        ("WMAN-IF2-MIB", "wmanIf2BsHistogramIndex"),
        ("WMAN-IF2-MIB", "wmanIf2BsChannelNumber"),
        ("WMAN-IF2-MIB", "wmanIf2BsStartFrame"),
        ("WMAN-IF2-MIB", "wmanIf2BsDuration"),
        ("WMAN-IF2-MIB", "wmanIf2BsBasicReport"),
        ("WMAN-IF2-MIB", "wmanIf2BsMeanCinrReport"),
        ("WMAN-IF2-MIB", "wmanIf2BsMeanRssiReport"),
        ("WMAN-IF2-MIB", "wmanIf2BsStdDeviationCinrReport"),
        ("WMAN-IF2-MIB", "wmanIf2BsStdDeviationRssiReport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapUplinkCidSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapArqSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapDsxFlowControl"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapMacCrcSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapMcaFlowControl"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapMcpGroupCidSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapPkmFlowControl"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapAuthPolicyControl"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapMaxNumOfSupportedSA"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapIpVersion"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapMacCsSupportBitMap"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapMaxNumOfClassifier"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapPhsSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapBandwidthAllocSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapPduConstruction"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapTtgTransitionGap"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapRtgTransitionGap"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgUplinkCidSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgArqSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgDsxFlowControl"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgMacCrcSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgMcaFlowControl"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgMcpGroupCidSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgPkmFlowControl"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgAuthPolicyControl"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgMaxNumOfSupportedSA"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgIpVersion"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgMacCsSupportBitMap"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgMaxNumOfClassifier"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgPhsSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgBandwidthAllocSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgPduConstruction"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgTtgTransitionGap"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgRtgTransitionGap"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsActionsResetSs"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsActionsAbortSs"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsActionsOverrideDnFreq"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsActionsOverrideChannelId"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsActionsDeReRegSs"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsActionsDeReRegSsCode"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsActionsRowStatus"),
        ("WMAN-IF2-MIB", "wmanIf2BsPkmV1AkLifetime"),
        ("WMAN-IF2-MIB", "wmanIf2BsPkmV1TekLifetime"),
        ("WMAN-IF2-MIB", "wmanIf2BsPkmV1SelfSigManufCertTrust"),
        ("WMAN-IF2-MIB", "wmanIf2BsPkmV1CheckCertValidityPeriods"))
)
if mibBuilder.loadTexts:
    wmanIf2MibBsGroup.setStatus("current")

wmanIf2MibBsAasGroup = ObjectGroup(
    (1, 0, 8802, 16, 2, 2, 1, 4)
)
wmanIf2MibBsAasGroup.setObjects(
      *(("WMAN-IF2-MIB", "wmanIf2BsAasChanFbckReqFreq"),
        ("WMAN-IF2-MIB", "wmanIf2BsAasBeamSelectFreq"),
        ("WMAN-IF2-MIB", "wmanIf2BsAasChanFbckReqResolution"),
        ("WMAN-IF2-MIB", "wmanIf2BsAasBeamReqResolution"),
        ("WMAN-IF2-MIB", "wmanIf2BsAasNumOptDiversityZones"))
)
if mibBuilder.loadTexts:
    wmanIf2MibBsAasGroup.setStatus("current")

wmanIf2MibBsOfdmaGroup = ObjectGroup(
    (1, 0, 8802, 16, 2, 2, 1, 8)
)
wmanIf2MibBsOfdmaGroup.setObjects(
      *(("WMAN-IF2-MIB", "wmanIf2BsOfdmaCtBasedResvTimeout"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaUplinkCenterFreq"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaStartOfRngCodes"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaPermutationBase"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaULAllocSubchBitmap"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaOptPermULAllocSubchBitmap"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaBandAMCAllocThreshold"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaBandAMCReleaseThreshold"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaBandAMCAllocTimer"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaBandAMCReleaseTimer"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaBandStatRepMAXPeriod"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaBandAMCRetryTimer"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaBsEIRP"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaChannelNumber"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaTTG"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaRTG"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaInitRngMaxRSS"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaDownlinkCenterFreq"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaBsId"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaMacVersion"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaFrameDurationCode"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaUcdFecCodeType"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaRangingDataRatio"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaUcdBurstProfileRowStatus"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaDownlinkFrequency"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaDcdFecCodeType"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaDcdBurstProfileRowStatus"))
)
if mibBuilder.loadTexts:
    wmanIf2MibBsOfdmaGroup.setStatus("current")

wmanIf2MibAllObjects = ObjectGroup(
    (1, 0, 8802, 16, 2, 2, 1, 14)
)
wmanIf2MibAllObjects.setObjects(
      *(("WMAN-IF2-MIB", "wmanIf2BsSaChallengeTimer"),
        ("WMAN-IF2-MIB", "wmanIf2BsSaChallengeMaxResends"),
        ("WMAN-IF2-MIB", "wmanIf2BsSaTekTimer"),
        ("WMAN-IF2-MIB", "wmanIf2BsSaTekReqMaxResends"),
        ("WMAN-IF2-MIB", "wmanIf2Bs2ndEapTimeout"),
        ("WMAN-IF2-MIB", "wmanIf2BsEapCompleteResends"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapDownlinkCidSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapPackingSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapExtendedRtpsSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapMaxNumBurstToMs"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapIpAddrAllocMethod"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapArqAckType"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapMacHeader"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapMaxMacLevelDlFrame"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapMaxMacLevelUlFrame"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapNumOfProvisionedSf"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapPkmVersion"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapAuthPolicy"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapMacMode"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapPnWindowSize"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapExtCapability"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgDownlinkCidSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgPackingSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgExtendedRtpsSupport"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgMaxNumBurstToMs"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgIpAddrAllocMethod"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgArqAckType"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgMacHeader"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgMaxMacLevelDlFrame"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgMaxMacLevelUlFrame"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgNumOfProvisionedSf"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgPkmVersion"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgAuthPolicy"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgMacMode"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgPnWindowSize"),
        ("WMAN-IF2-MIB", "wmanIf2BsCapCfgExtCapability"),
        ("WMAN-IF2-MIB", "wmanIf2BsPkmScDataEncryptAlgorithm"),
        ("WMAN-IF2-MIB", "wmanIf2BsPkmScDataAuthentAlgorithm"),
        ("WMAN-IF2-MIB", "wmanIf2BsPkmScEncryptAlgorithm"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsPkmScDataEncryptAlgorithm"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsPkmScDataAuthentAlgorithm"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsPkmScEncryptAlgorithm"),
        ("WMAN-IF2-MIB", "wmanIf2BsPkmV1AuthWaitTimeout"),
        ("WMAN-IF2-MIB", "wmanIf2BsPkmV1ReauthWaitTimeout"),
        ("WMAN-IF2-MIB", "wmanIf2BsPkmV1AuthGraceTime"),
        ("WMAN-IF2-MIB", "wmanIf2BsPkmV1OpWaitTimeout"),
        ("WMAN-IF2-MIB", "wmanIf2BsPkmV1RekeyWaitTimeout"),
        ("WMAN-IF2-MIB", "wmanIf2BsPkmV1TekGraceTime"),
        ("WMAN-IF2-MIB", "wmanIf2BsPkmV1AuthRejectWaitTimeout"),
        ("WMAN-IF2-MIB", "wmanIf2BsPkmPmkPrehandshakeLifetime"),
        ("WMAN-IF2-MIB", "wmanIf2BsPkmPmkLifetime"),
        ("WMAN-IF2-MIB", "wmanIf2BsSaChallengeTimeout"),
        ("WMAN-IF2-MIB", "wmanIf2BsMaxSaTekChallenge"),
        ("WMAN-IF2-MIB", "wmanIf2BsSaTekTimeout"),
        ("WMAN-IF2-MIB", "wmanIf2BsMaxSaTekRequest"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaCapFftSizes"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaCapDemodulator"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaCapModulator"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaCapNoHarqChannel"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaCapPermutation"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapDemMimo"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapMimoCapability"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapUlMimo"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapPrivateMap"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapAasCapability"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapCinrMeasurement"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapUlPowerControl"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapMapCapability"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapUlControlChannel"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapCistCapability"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapMaxHarqBurst"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapModMimo"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapSdmaPilot"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapMultipleBurst"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapIncrHarqBuffer"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapChaseHarqBuffer"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaCapCfgFftSizes"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaCapCfgDemodulator"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaCapCfgModulator"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaCapCfgNoHarqChannel"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaCapCfgPermutation"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapCfgDemMimo"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapCfgMimoCapability"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapCfgUlMimo"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapCfgPrivateMap"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapCfgAasCapability"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapCfgCinrMeasurement"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapCfgUlPowerControl"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapCfgMapCapability"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapCfgUlControlChannel"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapCfgCistCapability"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapCfgMaxHarqBurst"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapCfgModMimo"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapCfgSdmaPilot"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapCfgMultipleBurst"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapCfgIncrHarqBuffer"),
        ("WMAN-IF2-MIB", "wmanIf2BsSsOfdmaCapCfgChaseHarqBuffer"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExHandoverRangingStart"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExHandoverRangingEnd"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExHARQAckDelayDLBurst"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExUlAmcAlloPhyBandsBitmap"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExMaxRetransmission"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExNormalizedCnOverride"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExSizeOfCqichId"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExNormalizedCnValue"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExNormalizedCnOverride2"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExBandAmcEntryAvgCinr"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExAasPreambleUpperBond"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExAasPreambleLowerBond"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExAasBeamSelectAllowed"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExCqichIndicationFlag"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExUpPowerAdjStep"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExDownPowerAdjStep"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExMinPowerOffsetAdj"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExMaxPowerOffsetAdj"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExHandoverRngCodes"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExInitialRngInterval"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExTxPwrRepThreshold"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExTprPower"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExAlphaPavg"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExCqichTxPwrRepThreshold"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExCqichTprPower"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExCqichAlphaPavg"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExNormalizedCnChSounding"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExInitialRngBackoffStart"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExInitialRngBackoffEnd"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExBwRequestBackoffStart"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExBwRequestBackoffEnd"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExHARQAckDelayULBurst"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExHarqZonePermutation"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExHMaxRetransmission"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExCinrAlphaAvg"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExRssiAlphaAvg"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExDlAmcAlloPhyBandsBitmap"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExHandoverSupported"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExThresholdAddBsDivSet"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExThresholdDelBsDivSet"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExAsrSlotLength"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExAsrSwitchingPeriod"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExHysteresisMargin"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExTimeToTrigger"),
        ("WMAN-IF2-MIB", "wmanIf2BsOfdmaExRestartCount"))
)
if mibBuilder.loadTexts:
    wmanIf2MibAllObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wmanIf2MibCompliance = ModuleCompliance(
    (1, 0, 8802, 16, 2, 2, 2, 1)
)
wmanIf2MibCompliance.setObjects(
      *(("WMAN-IF2-MIB", "wmanIf2MibCommonGroup"),
        ("WMAN-IF2-MIB", "wmanIf2MibQoSGroup"),
        ("WMAN-IF2-MIB", "wmanIf2MibBsGroup"),
        ("WMAN-IF2-MIB", "wmanIf2MibBsAasGroup"),
        ("WMAN-IF2-MIB", "wmanIf2MibBsOfdmaGroup"))
)
if mibBuilder.loadTexts:
    wmanIf2MibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WMAN-IF2-MIB",
    **{"WmanIf2SfSchedulingType": WmanIf2SfSchedulingType,
       "WmanIf2PhsRuleVerify": WmanIf2PhsRuleVerify,
       "WmanIf2ClassifierBitMap": WmanIf2ClassifierBitMap,
       "WmanIf2SfState": WmanIf2SfState,
       "WmanIf2ServClassName": WmanIf2ServClassName,
       "WmanIf2CsSpecification": WmanIf2CsSpecification,
       "WmanIf2MacVersion": WmanIf2MacVersion,
       "WmanIf2CidType": WmanIf2CidType,
       "WmanIf2DataEncryptAlgId": WmanIf2DataEncryptAlgId,
       "WmanIf2DataAuthAlgId": WmanIf2DataAuthAlgId,
       "WmanIf2TekEncryptAlgId": WmanIf2TekEncryptAlgId,
       "WmanIf2PkmErrorCode": WmanIf2PkmErrorCode,
       "WmanIf2SaType": WmanIf2SaType,
       "WmanIf2TekState": WmanIf2TekState,
       "WmanIf2CertificateStat": WmanIf2CertificateStat,
       "WmanIf2ChannelNumber": WmanIf2ChannelNumber,
       "WmanIf2OfdmFecCodeType": WmanIf2OfdmFecCodeType,
       "WmanIf2OfdmaFecCodeType": WmanIf2OfdmaFecCodeType,
       "WmanIf2OfdmaUcdFecCode": WmanIf2OfdmaUcdFecCode,
       "WmanIf2OfdmaDcdFecCode": WmanIf2OfdmaDcdFecCode,
       "WmanIf2NumOfCid": WmanIf2NumOfCid,
       "WmanIf2ArqSupportType": WmanIf2ArqSupportType,
       "WmanIf2MaxDsxFlowType": WmanIf2MaxDsxFlowType,
       "WmanIf2MacCrcSupport": WmanIf2MacCrcSupport,
       "WmanIf2MaxMcaFlowType": WmanIf2MaxMcaFlowType,
       "WmanIf2MaxMcpGroupCid": WmanIf2MaxMcpGroupCid,
       "WmanIf2MaxPkmFlowType": WmanIf2MaxPkmFlowType,
       "WmanIf2AuthPolicyType": WmanIf2AuthPolicyType,
       "WmanIf2MaxNumOfSaType": WmanIf2MaxNumOfSaType,
       "WmanIf2IpVersionType": WmanIf2IpVersionType,
       "WmanIf2MacCsBitMap": WmanIf2MacCsBitMap,
       "WmanIf2MaxClassifiers": WmanIf2MaxClassifiers,
       "WmanIf2PhsSupportType": WmanIf2PhsSupportType,
       "WmanIf2BwAllocSupport": WmanIf2BwAllocSupport,
       "WmanIf2PduConstruction": WmanIf2PduConstruction,
       "WmanIf2SsTransitionGap": WmanIf2SsTransitionGap,
       "WmanIf2MaxTxPowerType": WmanIf2MaxTxPowerType,
       "WmanIf2OfdmFftSizes": WmanIf2OfdmFftSizes,
       "WmanIf2OfdmSsDeModType": WmanIf2OfdmSsDeModType,
       "WmanIf2OfdmSsModType": WmanIf2OfdmSsModType,
       "WmanIf2OfdmFocusedCt": WmanIf2OfdmFocusedCt,
       "WmanIf2OfdmTcSublayer": WmanIf2OfdmTcSublayer,
       "WmanIf2OfdmPrivMap": WmanIf2OfdmPrivMap,
       "WmanIf2OfdmUlPower": WmanIf2OfdmUlPower,
       "WmanIf2BsIdType": WmanIf2BsIdType,
       "WmanIf2Ipv6FlowLabel": WmanIf2Ipv6FlowLabel,
       "WmanIf2OfdmaFftSizes": WmanIf2OfdmaFftSizes,
       "WmanIf2OfdmaMsDeModType": WmanIf2OfdmaMsDeModType,
       "WmanIf2OfdmaMsModType": WmanIf2OfdmaMsModType,
       "WmanIf2OfdmaPermutation": WmanIf2OfdmaPermutation,
       "WmanIf2OfdmaDemMimo": WmanIf2OfdmaDemMimo,
       "WmanIf2OfdmaMimoCap": WmanIf2OfdmaMimoCap,
       "WmanIf2OfdmaUlMimo": WmanIf2OfdmaUlMimo,
       "WmanIf2OfdmaPrivMap": WmanIf2OfdmaPrivMap,
       "WmanIf2OfdmaAasCap": WmanIf2OfdmaAasCap,
       "WmanIf2OfdmaCinrCap": WmanIf2OfdmaCinrCap,
       "WmanIf2OfdmaUlPower": WmanIf2OfdmaUlPower,
       "WmanIf2OfdmaMapCap": WmanIf2OfdmaMapCap,
       "WmanIf2OfdmaUlCntlCh": WmanIf2OfdmaUlCntlCh,
       "WmanIf2OfdmaMsCistCap": WmanIf2OfdmaMsCistCap,
       "WmanIf2OfdmaMaxHarq": WmanIf2OfdmaMaxHarq,
       "WmanIf2OfdmaModMimo": WmanIf2OfdmaModMimo,
       "WmanIf2SdmaPilotCap": WmanIf2SdmaPilotCap,
       "WmanIf2MultiBurst": WmanIf2MultiBurst,
       "WmanIf2IncrHarqBuf": WmanIf2IncrHarqBuf,
       "WmanIf2ChaseHarqBuf": WmanIf2ChaseHarqBuf,
       "WmanIf2PkmVersion": WmanIf2PkmVersion,
       "WmanIf2AuthPolicy": WmanIf2AuthPolicy,
       "WmanIf2MacMode": WmanIf2MacMode,
       "WmanIf2ExtCapability": WmanIf2ExtCapability,
       "WmanIf2PackingSupport": WmanIf2PackingSupport,
       "WmanIf2ExtRtpsSupport": WmanIf2ExtRtpsSupport,
       "WmanIf2IpAllocMethod": WmanIf2IpAllocMethod,
       "WmanIf2ArqAckType": WmanIf2ArqAckType,
       "WmanIf2MacHeaderSupp": WmanIf2MacHeaderSupp,
       "WmanIf2HarqAckDelay": WmanIf2HarqAckDelay,
       "WmanIf2AasBeamSel": WmanIf2AasBeamSel,
       "WmanIf2MaxMacLevel": WmanIf2MaxMacLevel,
       "WmanIfPermutationType": WmanIfPermutationType,
       "WmanIf2HoSupportType": WmanIf2HoSupportType,
       "WmanIf2ActionRule": WmanIf2ActionRule,
       "wmanIf2Mib": wmanIf2Mib,
       "wmanIf2MibObjects": wmanIf2MibObjects,
       "wmanIf2BsObjects": wmanIf2BsObjects,
       "wmanIf2BsPacketCs": wmanIf2BsPacketCs,
       "wmanIf2BsSsPacketCounterTable": wmanIf2BsSsPacketCounterTable,
       "wmanIf2BsSsPacketCounterEntry": wmanIf2BsSsPacketCounterEntry,
       "wmanIf2BsSsMacSduCount": wmanIf2BsSsMacSduCount,
       "wmanIf2BsSsOctetCount": wmanIf2BsSsOctetCount,
       "wmanIf2BsSsResetCounter": wmanIf2BsSsResetCounter,
       "wmanIf2BsSsResetCounterTime": wmanIf2BsSsResetCounterTime,
       "wmanIf2BsCps": wmanIf2BsCps,
       "wmanIf2BsRegisteredSsTable": wmanIf2BsRegisteredSsTable,
       "wmanIf2BsRegisteredSsEntry": wmanIf2BsRegisteredSsEntry,
       "wmanIf2BsSsMacAddress": wmanIf2BsSsMacAddress,
       "wmanIf2BsSsBasicCid": wmanIf2BsSsBasicCid,
       "wmanIf2BsSsPrimaryCid": wmanIf2BsSsPrimaryCid,
       "wmanIf2BsSsSecondaryCid": wmanIf2BsSsSecondaryCid,
       "wmanIf2BsSsManagementSupport": wmanIf2BsSsManagementSupport,
       "wmanIf2BsSsIpManagementMode": wmanIf2BsSsIpManagementMode,
       "wmanIf2BsSs2ndMgmtArqEnable": wmanIf2BsSs2ndMgmtArqEnable,
       "wmanIf2BsSs2ndMgmtArqWindowSize": wmanIf2BsSs2ndMgmtArqWindowSize,
       "wmanIf2BsSs2ndMgmtArqDnLinkTxDelay": wmanIf2BsSs2ndMgmtArqDnLinkTxDelay,
       "wmanIf2BsSs2ndMgmtArqUpLinkTxDelay": wmanIf2BsSs2ndMgmtArqUpLinkTxDelay,
       "wmanIf2BsSs2ndMgmtArqDnLinkRxDelay": wmanIf2BsSs2ndMgmtArqDnLinkRxDelay,
       "wmanIf2BsSs2ndMgmtArqUpLinkRxDelay": wmanIf2BsSs2ndMgmtArqUpLinkRxDelay,
       "wmanIf2BsSs2ndMgmtArqBlockLifetime": wmanIf2BsSs2ndMgmtArqBlockLifetime,
       "wmanIf2BsSs2ndMgmtArqSyncLossTimeout": wmanIf2BsSs2ndMgmtArqSyncLossTimeout,
       "wmanIf2BsSs2ndMgmtArqDeliverInOrder": wmanIf2BsSs2ndMgmtArqDeliverInOrder,
       "wmanIf2BsSs2ndMgmtArqRxPurgeTimeout": wmanIf2BsSs2ndMgmtArqRxPurgeTimeout,
       "wmanIf2BsSs2ndMgmtArqBlockSize": wmanIf2BsSs2ndMgmtArqBlockSize,
       "wmanIf2BsSsVendorIdEncoding": wmanIf2BsSsVendorIdEncoding,
       "wmanIf2BsSsAasBroadcastPermission": wmanIf2BsSsAasBroadcastPermission,
       "wmanIf2BsSsMaxTxPowerBpsk": wmanIf2BsSsMaxTxPowerBpsk,
       "wmanIf2BsSsMaxTxPowerQpsk": wmanIf2BsSsMaxTxPowerQpsk,
       "wmanIf2BsSsMaxTxPower16Qam": wmanIf2BsSsMaxTxPower16Qam,
       "wmanIf2BsSsMaxTxPower64Qam": wmanIf2BsSsMaxTxPower64Qam,
       "wmanIf2BsSsMacVersion": wmanIf2BsSsMacVersion,
       "wmanIf2BsConfigurationTable": wmanIf2BsConfigurationTable,
       "wmanIf2BsConfigurationEntry": wmanIf2BsConfigurationEntry,
       "wmanIf2BsDcdInterval": wmanIf2BsDcdInterval,
       "wmanIf2BsUcdInterval": wmanIf2BsUcdInterval,
       "wmanIf2BsUcdTransition": wmanIf2BsUcdTransition,
       "wmanIf2BsDcdTransition": wmanIf2BsDcdTransition,
       "wmanIf2BsInitialRangingInterval": wmanIf2BsInitialRangingInterval,
       "wmanIf2BsT9Timeout": wmanIf2BsT9Timeout,
       "wmanIf2BsSsULMapProcTime": wmanIf2BsSsULMapProcTime,
       "wmanIf2BsSsRangRespProcTime": wmanIf2BsSsRangRespProcTime,
       "wmanIf2BsT13Timeout": wmanIf2BsT13Timeout,
       "wmanIf2BsT15Timeout": wmanIf2BsT15Timeout,
       "wmanIf2BsT17Timeout": wmanIf2BsT17Timeout,
       "wmanIf2BsT27IdleTimer": wmanIf2BsT27IdleTimer,
       "wmanIf2BsT27ActiveTimer": wmanIf2BsT27ActiveTimer,
       "wmanIf2Bs2ndMgmtDlQoSProfileIndex": wmanIf2Bs2ndMgmtDlQoSProfileIndex,
       "wmanIf2Bs2ndMgmtUlQoSProfileIndex": wmanIf2Bs2ndMgmtUlQoSProfileIndex,
       "wmanIf2BsAutoSfidEnabled": wmanIf2BsAutoSfidEnabled,
       "wmanIf2BsAutoSfidRangeMin": wmanIf2BsAutoSfidRangeMin,
       "wmanIf2BsAutoSfidRangeMax": wmanIf2BsAutoSfidRangeMax,
       "wmanIf2BsAasChanFbckReqFreq": wmanIf2BsAasChanFbckReqFreq,
       "wmanIf2BsAasBeamSelectFreq": wmanIf2BsAasBeamSelectFreq,
       "wmanIf2BsAasChanFbckReqResolution": wmanIf2BsAasChanFbckReqResolution,
       "wmanIf2BsAasBeamReqResolution": wmanIf2BsAasBeamReqResolution,
       "wmanIf2BsAasNumOptDiversityZones": wmanIf2BsAasNumOptDiversityZones,
       "wmanIf2BsResetSector": wmanIf2BsResetSector,
       "wmanIf2BsSaChallengeTimer": wmanIf2BsSaChallengeTimer,
       "wmanIf2BsSaChallengeMaxResends": wmanIf2BsSaChallengeMaxResends,
       "wmanIf2BsSaTekTimer": wmanIf2BsSaTekTimer,
       "wmanIf2BsSaTekReqMaxResends": wmanIf2BsSaTekReqMaxResends,
       "wmanIf2Bs2ndEapTimeout": wmanIf2Bs2ndEapTimeout,
       "wmanIf2BsEapCompleteResends": wmanIf2BsEapCompleteResends,
       "wmanIf2BsChannelMeasurementTable": wmanIf2BsChannelMeasurementTable,
       "wmanIf2BsChannelMeasurementEntry": wmanIf2BsChannelMeasurementEntry,
       "wmanIf2BsChannelDirection": wmanIf2BsChannelDirection,
       "wmanIf2BsHistogramIndex": wmanIf2BsHistogramIndex,
       "wmanIf2BsChannelNumber": wmanIf2BsChannelNumber,
       "wmanIf2BsStartFrame": wmanIf2BsStartFrame,
       "wmanIf2BsDuration": wmanIf2BsDuration,
       "wmanIf2BsBasicReport": wmanIf2BsBasicReport,
       "wmanIf2BsMeanCinrReport": wmanIf2BsMeanCinrReport,
       "wmanIf2BsMeanRssiReport": wmanIf2BsMeanRssiReport,
       "wmanIf2BsStdDeviationCinrReport": wmanIf2BsStdDeviationCinrReport,
       "wmanIf2BsStdDeviationRssiReport": wmanIf2BsStdDeviationRssiReport,
       "wmanIf2BsCapabilities": wmanIf2BsCapabilities,
       "wmanIf2BsBasicCapabilitiesTable": wmanIf2BsBasicCapabilitiesTable,
       "wmanIf2BsBasicCapabilitiesEntry": wmanIf2BsBasicCapabilitiesEntry,
       "wmanIf2BsCapUplinkCidSupport": wmanIf2BsCapUplinkCidSupport,
       "wmanIf2BsCapArqSupport": wmanIf2BsCapArqSupport,
       "wmanIf2BsCapDsxFlowControl": wmanIf2BsCapDsxFlowControl,
       "wmanIf2BsCapMacCrcSupport": wmanIf2BsCapMacCrcSupport,
       "wmanIf2BsCapMcaFlowControl": wmanIf2BsCapMcaFlowControl,
       "wmanIf2BsCapMcpGroupCidSupport": wmanIf2BsCapMcpGroupCidSupport,
       "wmanIf2BsCapPkmFlowControl": wmanIf2BsCapPkmFlowControl,
       "wmanIf2BsCapAuthPolicyControl": wmanIf2BsCapAuthPolicyControl,
       "wmanIf2BsCapMaxNumOfSupportedSA": wmanIf2BsCapMaxNumOfSupportedSA,
       "wmanIf2BsCapIpVersion": wmanIf2BsCapIpVersion,
       "wmanIf2BsCapMacCsSupportBitMap": wmanIf2BsCapMacCsSupportBitMap,
       "wmanIf2BsCapMaxNumOfClassifier": wmanIf2BsCapMaxNumOfClassifier,
       "wmanIf2BsCapPhsSupport": wmanIf2BsCapPhsSupport,
       "wmanIf2BsCapBandwidthAllocSupport": wmanIf2BsCapBandwidthAllocSupport,
       "wmanIf2BsCapPduConstruction": wmanIf2BsCapPduConstruction,
       "wmanIf2BsCapTtgTransitionGap": wmanIf2BsCapTtgTransitionGap,
       "wmanIf2BsCapRtgTransitionGap": wmanIf2BsCapRtgTransitionGap,
       "wmanIf2BsCapDownlinkCidSupport": wmanIf2BsCapDownlinkCidSupport,
       "wmanIf2BsCapPackingSupport": wmanIf2BsCapPackingSupport,
       "wmanIf2BsCapExtendedRtpsSupport": wmanIf2BsCapExtendedRtpsSupport,
       "wmanIf2BsCapMaxNumBurstToMs": wmanIf2BsCapMaxNumBurstToMs,
       "wmanIf2BsCapIpAddrAllocMethod": wmanIf2BsCapIpAddrAllocMethod,
       "wmanIf2BsCapArqAckType": wmanIf2BsCapArqAckType,
       "wmanIf2BsCapMacHeader": wmanIf2BsCapMacHeader,
       "wmanIf2BsCapMaxMacLevelDlFrame": wmanIf2BsCapMaxMacLevelDlFrame,
       "wmanIf2BsCapMaxMacLevelUlFrame": wmanIf2BsCapMaxMacLevelUlFrame,
       "wmanIf2BsCapNumOfProvisionedSf": wmanIf2BsCapNumOfProvisionedSf,
       "wmanIf2BsCapPkmVersion": wmanIf2BsCapPkmVersion,
       "wmanIf2BsCapAuthPolicy": wmanIf2BsCapAuthPolicy,
       "wmanIf2BsCapMacMode": wmanIf2BsCapMacMode,
       "wmanIf2BsCapPnWindowSize": wmanIf2BsCapPnWindowSize,
       "wmanIf2BsCapExtCapability": wmanIf2BsCapExtCapability,
       "wmanIf2BsCapabilitiesConfigTable": wmanIf2BsCapabilitiesConfigTable,
       "wmanIf2BsCapabilitiesConfigEntry": wmanIf2BsCapabilitiesConfigEntry,
       "wmanIf2BsCapCfgUplinkCidSupport": wmanIf2BsCapCfgUplinkCidSupport,
       "wmanIf2BsCapCfgArqSupport": wmanIf2BsCapCfgArqSupport,
       "wmanIf2BsCapCfgDsxFlowControl": wmanIf2BsCapCfgDsxFlowControl,
       "wmanIf2BsCapCfgMacCrcSupport": wmanIf2BsCapCfgMacCrcSupport,
       "wmanIf2BsCapCfgMcaFlowControl": wmanIf2BsCapCfgMcaFlowControl,
       "wmanIf2BsCapCfgMcpGroupCidSupport": wmanIf2BsCapCfgMcpGroupCidSupport,
       "wmanIf2BsCapCfgPkmFlowControl": wmanIf2BsCapCfgPkmFlowControl,
       "wmanIf2BsCapCfgAuthPolicyControl": wmanIf2BsCapCfgAuthPolicyControl,
       "wmanIf2BsCapCfgMaxNumOfSupportedSA": wmanIf2BsCapCfgMaxNumOfSupportedSA,
       "wmanIf2BsCapCfgIpVersion": wmanIf2BsCapCfgIpVersion,
       "wmanIf2BsCapCfgMacCsSupportBitMap": wmanIf2BsCapCfgMacCsSupportBitMap,
       "wmanIf2BsCapCfgMaxNumOfClassifier": wmanIf2BsCapCfgMaxNumOfClassifier,
       "wmanIf2BsCapCfgPhsSupport": wmanIf2BsCapCfgPhsSupport,
       "wmanIf2BsCapCfgBandwidthAllocSupport": wmanIf2BsCapCfgBandwidthAllocSupport,
       "wmanIf2BsCapCfgPduConstruction": wmanIf2BsCapCfgPduConstruction,
       "wmanIf2BsCapCfgTtgTransitionGap": wmanIf2BsCapCfgTtgTransitionGap,
       "wmanIf2BsCapCfgRtgTransitionGap": wmanIf2BsCapCfgRtgTransitionGap,
       "wmanIf2BsCapCfgDownlinkCidSupport": wmanIf2BsCapCfgDownlinkCidSupport,
       "wmanIf2BsCapCfgPackingSupport": wmanIf2BsCapCfgPackingSupport,
       "wmanIf2BsCapCfgExtendedRtpsSupport": wmanIf2BsCapCfgExtendedRtpsSupport,
       "wmanIf2BsCapCfgMaxNumBurstToMs": wmanIf2BsCapCfgMaxNumBurstToMs,
       "wmanIf2BsCapCfgIpAddrAllocMethod": wmanIf2BsCapCfgIpAddrAllocMethod,
       "wmanIf2BsCapCfgArqAckType": wmanIf2BsCapCfgArqAckType,
       "wmanIf2BsCapCfgMacHeader": wmanIf2BsCapCfgMacHeader,
       "wmanIf2BsCapCfgMaxMacLevelDlFrame": wmanIf2BsCapCfgMaxMacLevelDlFrame,
       "wmanIf2BsCapCfgMaxMacLevelUlFrame": wmanIf2BsCapCfgMaxMacLevelUlFrame,
       "wmanIf2BsCapCfgNumOfProvisionedSf": wmanIf2BsCapCfgNumOfProvisionedSf,
       "wmanIf2BsCapCfgPkmVersion": wmanIf2BsCapCfgPkmVersion,
       "wmanIf2BsCapCfgAuthPolicy": wmanIf2BsCapCfgAuthPolicy,
       "wmanIf2BsCapCfgMacMode": wmanIf2BsCapCfgMacMode,
       "wmanIf2BsCapCfgPnWindowSize": wmanIf2BsCapCfgPnWindowSize,
       "wmanIf2BsCapCfgExtCapability": wmanIf2BsCapCfgExtCapability,
       "wmanIf2BsSsActionsTable": wmanIf2BsSsActionsTable,
       "wmanIf2BsSsActionsEntry": wmanIf2BsSsActionsEntry,
       "wmanIf2BsSsActionsMacAddress": wmanIf2BsSsActionsMacAddress,
       "wmanIf2BsSsActionsResetSs": wmanIf2BsSsActionsResetSs,
       "wmanIf2BsSsActionsAbortSs": wmanIf2BsSsActionsAbortSs,
       "wmanIf2BsSsActionsOverrideDnFreq": wmanIf2BsSsActionsOverrideDnFreq,
       "wmanIf2BsSsActionsOverrideChannelId": wmanIf2BsSsActionsOverrideChannelId,
       "wmanIf2BsSsActionsDeReRegSs": wmanIf2BsSsActionsDeReRegSs,
       "wmanIf2BsSsActionsDeReRegSsCode": wmanIf2BsSsActionsDeReRegSsCode,
       "wmanIf2BsSsActionsRowStatus": wmanIf2BsSsActionsRowStatus,
       "wmanIf2BsPkmObjects": wmanIf2BsPkmObjects,
       "wmanIf2BsPkmSecurityCapabilityTable": wmanIf2BsPkmSecurityCapabilityTable,
       "wmanIf2BsPkmSecurityCapabilityEntry": wmanIf2BsPkmSecurityCapabilityEntry,
       "wmanIf2BsPkmSecurityCapIndex": wmanIf2BsPkmSecurityCapIndex,
       "wmanIf2BsPkmScDataEncryptAlgorithm": wmanIf2BsPkmScDataEncryptAlgorithm,
       "wmanIf2BsPkmScDataAuthentAlgorithm": wmanIf2BsPkmScDataAuthentAlgorithm,
       "wmanIf2BsPkmScEncryptAlgorithm": wmanIf2BsPkmScEncryptAlgorithm,
       "wmanIf2BsSsPkmSecurityCapabilityTable": wmanIf2BsSsPkmSecurityCapabilityTable,
       "wmanIf2BsSsPkmSecurityCapabilityEntry": wmanIf2BsSsPkmSecurityCapabilityEntry,
       "wmanIf2BsSsPkmSecurityCapIndex": wmanIf2BsSsPkmSecurityCapIndex,
       "wmanIf2BsSsPkmScDataEncryptAlgorithm": wmanIf2BsSsPkmScDataEncryptAlgorithm,
       "wmanIf2BsSsPkmScDataAuthentAlgorithm": wmanIf2BsSsPkmScDataAuthentAlgorithm,
       "wmanIf2BsSsPkmScEncryptAlgorithm": wmanIf2BsSsPkmScEncryptAlgorithm,
       "wmanIf2BsPkmV1Objects": wmanIf2BsPkmV1Objects,
       "wmanIf2BsPkmV1ConfigTable": wmanIf2BsPkmV1ConfigTable,
       "wmanIf2BsPkmV1ConfigEntry": wmanIf2BsPkmV1ConfigEntry,
       "wmanIf2BsPkmV1AkLifetime": wmanIf2BsPkmV1AkLifetime,
       "wmanIf2BsPkmV1TekLifetime": wmanIf2BsPkmV1TekLifetime,
       "wmanIf2BsPkmV1SelfSigManufCertTrust": wmanIf2BsPkmV1SelfSigManufCertTrust,
       "wmanIf2BsPkmV1AuthWaitTimeout": wmanIf2BsPkmV1AuthWaitTimeout,
       "wmanIf2BsPkmV1ReauthWaitTimeout": wmanIf2BsPkmV1ReauthWaitTimeout,
       "wmanIf2BsPkmV1AuthGraceTime": wmanIf2BsPkmV1AuthGraceTime,
       "wmanIf2BsPkmV1OpWaitTimeout": wmanIf2BsPkmV1OpWaitTimeout,
       "wmanIf2BsPkmV1RekeyWaitTimeout": wmanIf2BsPkmV1RekeyWaitTimeout,
       "wmanIf2BsPkmV1TekGraceTime": wmanIf2BsPkmV1TekGraceTime,
       "wmanIf2BsPkmV1AuthRejectWaitTimeout": wmanIf2BsPkmV1AuthRejectWaitTimeout,
       "wmanIf2BsPkmV1CheckCertValidityPeriods": wmanIf2BsPkmV1CheckCertValidityPeriods,
       "wmanIf2BsPkmV2Objects": wmanIf2BsPkmV2Objects,
       "wmanIf2BsPkmV2ConfigTable": wmanIf2BsPkmV2ConfigTable,
       "wmanIf2BsPkmV2ConfigEntry": wmanIf2BsPkmV2ConfigEntry,
       "wmanIf2BsPkmPmkPrehandshakeLifetime": wmanIf2BsPkmPmkPrehandshakeLifetime,
       "wmanIf2BsPkmPmkLifetime": wmanIf2BsPkmPmkLifetime,
       "wmanIf2BsSaChallengeTimeout": wmanIf2BsSaChallengeTimeout,
       "wmanIf2BsMaxSaTekChallenge": wmanIf2BsMaxSaTekChallenge,
       "wmanIf2BsSaTekTimeout": wmanIf2BsSaTekTimeout,
       "wmanIf2BsMaxSaTekRequest": wmanIf2BsMaxSaTekRequest,
       "wmanIf2BsNotification": wmanIf2BsNotification,
       "wmanIf2BsTrapControl": wmanIf2BsTrapControl,
       "wmanIf2BsThresholdConfigTable": wmanIf2BsThresholdConfigTable,
       "wmanIf2BsThresholdConfigEntry": wmanIf2BsThresholdConfigEntry,
       "wmanIf2BsRssiLowThreshold": wmanIf2BsRssiLowThreshold,
       "wmanIf2BsRssiHighThreshold": wmanIf2BsRssiHighThreshold,
       "wmanIf2BsPhy": wmanIf2BsPhy,
       "wmanIf2BsOfdmaPhy": wmanIf2BsOfdmaPhy,
       "wmanIf2BsOfdmaUplinkChannelTable": wmanIf2BsOfdmaUplinkChannelTable,
       "wmanIf2BsOfdmaUplinkChannelEntry": wmanIf2BsOfdmaUplinkChannelEntry,
       "wmanIf2BsOfdmaCtBasedResvTimeout": wmanIf2BsOfdmaCtBasedResvTimeout,
       "wmanIf2BsOfdmaUplinkCenterFreq": wmanIf2BsOfdmaUplinkCenterFreq,
       "wmanIf2BsOfdmaStartOfRngCodes": wmanIf2BsOfdmaStartOfRngCodes,
       "wmanIf2BsOfdmaPermutationBase": wmanIf2BsOfdmaPermutationBase,
       "wmanIf2BsOfdmaULAllocSubchBitmap": wmanIf2BsOfdmaULAllocSubchBitmap,
       "wmanIf2BsOfdmaOptPermULAllocSubchBitmap": wmanIf2BsOfdmaOptPermULAllocSubchBitmap,
       "wmanIf2BsOfdmaBandAMCAllocThreshold": wmanIf2BsOfdmaBandAMCAllocThreshold,
       "wmanIf2BsOfdmaBandAMCReleaseThreshold": wmanIf2BsOfdmaBandAMCReleaseThreshold,
       "wmanIf2BsOfdmaBandAMCAllocTimer": wmanIf2BsOfdmaBandAMCAllocTimer,
       "wmanIf2BsOfdmaBandAMCReleaseTimer": wmanIf2BsOfdmaBandAMCReleaseTimer,
       "wmanIf2BsOfdmaBandStatRepMAXPeriod": wmanIf2BsOfdmaBandStatRepMAXPeriod,
       "wmanIf2BsOfdmaBandAMCRetryTimer": wmanIf2BsOfdmaBandAMCRetryTimer,
       "wmanIf2BsOfdmaDownlinkChannelTable": wmanIf2BsOfdmaDownlinkChannelTable,
       "wmanIf2BsOfdmaDownlinkChannelEntry": wmanIf2BsOfdmaDownlinkChannelEntry,
       "wmanIf2BsOfdmaBsEIRP": wmanIf2BsOfdmaBsEIRP,
       "wmanIf2BsOfdmaChannelNumber": wmanIf2BsOfdmaChannelNumber,
       "wmanIf2BsOfdmaTTG": wmanIf2BsOfdmaTTG,
       "wmanIf2BsOfdmaRTG": wmanIf2BsOfdmaRTG,
       "wmanIf2BsOfdmaInitRngMaxRSS": wmanIf2BsOfdmaInitRngMaxRSS,
       "wmanIf2BsOfdmaDownlinkCenterFreq": wmanIf2BsOfdmaDownlinkCenterFreq,
       "wmanIf2BsOfdmaBsId": wmanIf2BsOfdmaBsId,
       "wmanIf2BsOfdmaMacVersion": wmanIf2BsOfdmaMacVersion,
       "wmanIf2BsOfdmaFrameDurationCode": wmanIf2BsOfdmaFrameDurationCode,
       "wmanIf2BsOfdmaUcdBurstProfileTable": wmanIf2BsOfdmaUcdBurstProfileTable,
       "wmanIf2BsOfdmaUcdBurstProfileEntry": wmanIf2BsOfdmaUcdBurstProfileEntry,
       "wmanIf2BsOfdmaUiucIndex": wmanIf2BsOfdmaUiucIndex,
       "wmanIf2BsOfdmaUcdFecCodeType": wmanIf2BsOfdmaUcdFecCodeType,
       "wmanIf2BsOfdmaRangingDataRatio": wmanIf2BsOfdmaRangingDataRatio,
       "wmanIf2BsOfdmaUcdBurstProfileRowStatus": wmanIf2BsOfdmaUcdBurstProfileRowStatus,
       "wmanIf2BsOfdmaDcdBurstProfileTable": wmanIf2BsOfdmaDcdBurstProfileTable,
       "wmanIf2BsOfdmaDcdBurstProfileEntry": wmanIf2BsOfdmaDcdBurstProfileEntry,
       "wmanIf2BsOfdmaDiucIndex": wmanIf2BsOfdmaDiucIndex,
       "wmanIf2BsOfdmaDownlinkFrequency": wmanIf2BsOfdmaDownlinkFrequency,
       "wmanIf2BsOfdmaDcdFecCodeType": wmanIf2BsOfdmaDcdFecCodeType,
       "wmanIf2BsOfdmaDcdBurstProfileRowStatus": wmanIf2BsOfdmaDcdBurstProfileRowStatus,
       "wmanIf2BsOfdmaCapabilitiesTable": wmanIf2BsOfdmaCapabilitiesTable,
       "wmanIf2BsOfdmaCapabilitiesEntry": wmanIf2BsOfdmaCapabilitiesEntry,
       "wmanIf2BsOfdmaCapFftSizes": wmanIf2BsOfdmaCapFftSizes,
       "wmanIf2BsOfdmaCapDemodulator": wmanIf2BsOfdmaCapDemodulator,
       "wmanIf2BsOfdmaCapModulator": wmanIf2BsOfdmaCapModulator,
       "wmanIf2BsOfdmaCapNoHarqChannel": wmanIf2BsOfdmaCapNoHarqChannel,
       "wmanIf2BsOfdmaCapPermutation": wmanIf2BsOfdmaCapPermutation,
       "wmanIf2BsSsOfdmaCapDemMimo": wmanIf2BsSsOfdmaCapDemMimo,
       "wmanIf2BsSsOfdmaCapMimoCapability": wmanIf2BsSsOfdmaCapMimoCapability,
       "wmanIf2BsSsOfdmaCapUlMimo": wmanIf2BsSsOfdmaCapUlMimo,
       "wmanIf2BsSsOfdmaCapPrivateMap": wmanIf2BsSsOfdmaCapPrivateMap,
       "wmanIf2BsSsOfdmaCapAasCapability": wmanIf2BsSsOfdmaCapAasCapability,
       "wmanIf2BsSsOfdmaCapCinrMeasurement": wmanIf2BsSsOfdmaCapCinrMeasurement,
       "wmanIf2BsSsOfdmaCapUlPowerControl": wmanIf2BsSsOfdmaCapUlPowerControl,
       "wmanIf2BsSsOfdmaCapMapCapability": wmanIf2BsSsOfdmaCapMapCapability,
       "wmanIf2BsSsOfdmaCapUlControlChannel": wmanIf2BsSsOfdmaCapUlControlChannel,
       "wmanIf2BsSsOfdmaCapCistCapability": wmanIf2BsSsOfdmaCapCistCapability,
       "wmanIf2BsSsOfdmaCapMaxHarqBurst": wmanIf2BsSsOfdmaCapMaxHarqBurst,
       "wmanIf2BsSsOfdmaCapModMimo": wmanIf2BsSsOfdmaCapModMimo,
       "wmanIf2BsSsOfdmaCapSdmaPilot": wmanIf2BsSsOfdmaCapSdmaPilot,
       "wmanIf2BsSsOfdmaCapMultipleBurst": wmanIf2BsSsOfdmaCapMultipleBurst,
       "wmanIf2BsSsOfdmaCapIncrHarqBuffer": wmanIf2BsSsOfdmaCapIncrHarqBuffer,
       "wmanIf2BsSsOfdmaCapChaseHarqBuffer": wmanIf2BsSsOfdmaCapChaseHarqBuffer,
       "wmanIf2BsOfdmaCapabilitiesConfigTable": wmanIf2BsOfdmaCapabilitiesConfigTable,
       "wmanIf2BsOfdmaCapabilitiesConfigEntry": wmanIf2BsOfdmaCapabilitiesConfigEntry,
       "wmanIf2BsOfdmaCapCfgFftSizes": wmanIf2BsOfdmaCapCfgFftSizes,
       "wmanIf2BsOfdmaCapCfgDemodulator": wmanIf2BsOfdmaCapCfgDemodulator,
       "wmanIf2BsOfdmaCapCfgModulator": wmanIf2BsOfdmaCapCfgModulator,
       "wmanIf2BsOfdmaCapCfgNoHarqChannel": wmanIf2BsOfdmaCapCfgNoHarqChannel,
       "wmanIf2BsOfdmaCapCfgPermutation": wmanIf2BsOfdmaCapCfgPermutation,
       "wmanIf2BsSsOfdmaCapCfgDemMimo": wmanIf2BsSsOfdmaCapCfgDemMimo,
       "wmanIf2BsSsOfdmaCapCfgMimoCapability": wmanIf2BsSsOfdmaCapCfgMimoCapability,
       "wmanIf2BsSsOfdmaCapCfgUlMimo": wmanIf2BsSsOfdmaCapCfgUlMimo,
       "wmanIf2BsSsOfdmaCapCfgPrivateMap": wmanIf2BsSsOfdmaCapCfgPrivateMap,
       "wmanIf2BsSsOfdmaCapCfgAasCapability": wmanIf2BsSsOfdmaCapCfgAasCapability,
       "wmanIf2BsSsOfdmaCapCfgCinrMeasurement": wmanIf2BsSsOfdmaCapCfgCinrMeasurement,
       "wmanIf2BsSsOfdmaCapCfgUlPowerControl": wmanIf2BsSsOfdmaCapCfgUlPowerControl,
       "wmanIf2BsSsOfdmaCapCfgMapCapability": wmanIf2BsSsOfdmaCapCfgMapCapability,
       "wmanIf2BsSsOfdmaCapCfgUlControlChannel": wmanIf2BsSsOfdmaCapCfgUlControlChannel,
       "wmanIf2BsSsOfdmaCapCfgCistCapability": wmanIf2BsSsOfdmaCapCfgCistCapability,
       "wmanIf2BsSsOfdmaCapCfgMaxHarqBurst": wmanIf2BsSsOfdmaCapCfgMaxHarqBurst,
       "wmanIf2BsSsOfdmaCapCfgModMimo": wmanIf2BsSsOfdmaCapCfgModMimo,
       "wmanIf2BsSsOfdmaCapCfgSdmaPilot": wmanIf2BsSsOfdmaCapCfgSdmaPilot,
       "wmanIf2BsSsOfdmaCapCfgMultipleBurst": wmanIf2BsSsOfdmaCapCfgMultipleBurst,
       "wmanIf2BsSsOfdmaCapCfgIncrHarqBuffer": wmanIf2BsSsOfdmaCapCfgIncrHarqBuffer,
       "wmanIf2BsSsOfdmaCapCfgChaseHarqBuffer": wmanIf2BsSsOfdmaCapCfgChaseHarqBuffer,
       "wmanIf2BsOfdmaExUplinkChannelTable": wmanIf2BsOfdmaExUplinkChannelTable,
       "wmanIf2BsOfdmaExUplinkChannelEntry": wmanIf2BsOfdmaExUplinkChannelEntry,
       "wmanIf2BsOfdmaExHandoverRangingStart": wmanIf2BsOfdmaExHandoverRangingStart,
       "wmanIf2BsOfdmaExHandoverRangingEnd": wmanIf2BsOfdmaExHandoverRangingEnd,
       "wmanIf2BsOfdmaExHARQAckDelayDLBurst": wmanIf2BsOfdmaExHARQAckDelayDLBurst,
       "wmanIf2BsOfdmaExUlAmcAlloPhyBandsBitmap": wmanIf2BsOfdmaExUlAmcAlloPhyBandsBitmap,
       "wmanIf2BsOfdmaExMaxRetransmission": wmanIf2BsOfdmaExMaxRetransmission,
       "wmanIf2BsOfdmaExNormalizedCnOverride": wmanIf2BsOfdmaExNormalizedCnOverride,
       "wmanIf2BsOfdmaExSizeOfCqichId": wmanIf2BsOfdmaExSizeOfCqichId,
       "wmanIf2BsOfdmaExNormalizedCnValue": wmanIf2BsOfdmaExNormalizedCnValue,
       "wmanIf2BsOfdmaExNormalizedCnOverride2": wmanIf2BsOfdmaExNormalizedCnOverride2,
       "wmanIf2BsOfdmaExBandAmcEntryAvgCinr": wmanIf2BsOfdmaExBandAmcEntryAvgCinr,
       "wmanIf2BsOfdmaExAasPreambleUpperBond": wmanIf2BsOfdmaExAasPreambleUpperBond,
       "wmanIf2BsOfdmaExAasPreambleLowerBond": wmanIf2BsOfdmaExAasPreambleLowerBond,
       "wmanIf2BsOfdmaExAasBeamSelectAllowed": wmanIf2BsOfdmaExAasBeamSelectAllowed,
       "wmanIf2BsOfdmaExCqichIndicationFlag": wmanIf2BsOfdmaExCqichIndicationFlag,
       "wmanIf2BsOfdmaExUpPowerAdjStep": wmanIf2BsOfdmaExUpPowerAdjStep,
       "wmanIf2BsOfdmaExDownPowerAdjStep": wmanIf2BsOfdmaExDownPowerAdjStep,
       "wmanIf2BsOfdmaExMinPowerOffsetAdj": wmanIf2BsOfdmaExMinPowerOffsetAdj,
       "wmanIf2BsOfdmaExMaxPowerOffsetAdj": wmanIf2BsOfdmaExMaxPowerOffsetAdj,
       "wmanIf2BsOfdmaExHandoverRngCodes": wmanIf2BsOfdmaExHandoverRngCodes,
       "wmanIf2BsOfdmaExInitialRngInterval": wmanIf2BsOfdmaExInitialRngInterval,
       "wmanIf2BsOfdmaExTxPwrRepThreshold": wmanIf2BsOfdmaExTxPwrRepThreshold,
       "wmanIf2BsOfdmaExTprPower": wmanIf2BsOfdmaExTprPower,
       "wmanIf2BsOfdmaExAlphaPavg": wmanIf2BsOfdmaExAlphaPavg,
       "wmanIf2BsOfdmaExCqichTxPwrRepThreshold": wmanIf2BsOfdmaExCqichTxPwrRepThreshold,
       "wmanIf2BsOfdmaExCqichTprPower": wmanIf2BsOfdmaExCqichTprPower,
       "wmanIf2BsOfdmaExCqichAlphaPavg": wmanIf2BsOfdmaExCqichAlphaPavg,
       "wmanIf2BsOfdmaExNormalizedCnChSounding": wmanIf2BsOfdmaExNormalizedCnChSounding,
       "wmanIf2BsOfdmaExInitialRngBackoffStart": wmanIf2BsOfdmaExInitialRngBackoffStart,
       "wmanIf2BsOfdmaExInitialRngBackoffEnd": wmanIf2BsOfdmaExInitialRngBackoffEnd,
       "wmanIf2BsOfdmaExBwRequestBackoffStart": wmanIf2BsOfdmaExBwRequestBackoffStart,
       "wmanIf2BsOfdmaExBwRequestBackoffEnd": wmanIf2BsOfdmaExBwRequestBackoffEnd,
       "wmanIf2BsOfdmaExDownlinkChannelTable": wmanIf2BsOfdmaExDownlinkChannelTable,
       "wmanIf2BsOfdmaExDownlinkChannelEntry": wmanIf2BsOfdmaExDownlinkChannelEntry,
       "wmanIf2BsOfdmaExHARQAckDelayULBurst": wmanIf2BsOfdmaExHARQAckDelayULBurst,
       "wmanIf2BsOfdmaExHarqZonePermutation": wmanIf2BsOfdmaExHarqZonePermutation,
       "wmanIf2BsOfdmaExHMaxRetransmission": wmanIf2BsOfdmaExHMaxRetransmission,
       "wmanIf2BsOfdmaExCinrAlphaAvg": wmanIf2BsOfdmaExCinrAlphaAvg,
       "wmanIf2BsOfdmaExRssiAlphaAvg": wmanIf2BsOfdmaExRssiAlphaAvg,
       "wmanIf2BsOfdmaExDlAmcAlloPhyBandsBitmap": wmanIf2BsOfdmaExDlAmcAlloPhyBandsBitmap,
       "wmanIf2BsOfdmaExHandoverSupported": wmanIf2BsOfdmaExHandoverSupported,
       "wmanIf2BsOfdmaExThresholdAddBsDivSet": wmanIf2BsOfdmaExThresholdAddBsDivSet,
       "wmanIf2BsOfdmaExThresholdDelBsDivSet": wmanIf2BsOfdmaExThresholdDelBsDivSet,
       "wmanIf2BsOfdmaExAsrSlotLength": wmanIf2BsOfdmaExAsrSlotLength,
       "wmanIf2BsOfdmaExAsrSwitchingPeriod": wmanIf2BsOfdmaExAsrSwitchingPeriod,
       "wmanIf2BsOfdmaExHysteresisMargin": wmanIf2BsOfdmaExHysteresisMargin,
       "wmanIf2BsOfdmaExTimeToTrigger": wmanIf2BsOfdmaExTimeToTrigger,
       "wmanIf2BsOfdmaExRestartCount": wmanIf2BsOfdmaExRestartCount,
       "wmanIf2CommonObjects": wmanIf2CommonObjects,
       "wmanIf2CmnCps": wmanIf2CmnCps,
       "wmanIf2CmnCpsServiceFlowTable": wmanIf2CmnCpsServiceFlowTable,
       "wmanIf2CmnCpsServiceFlowEntry": wmanIf2CmnCpsServiceFlowEntry,
       "wmanIf2CmnCpsSfMacAddress": wmanIf2CmnCpsSfMacAddress,
       "wmanIf2CmnCpsSfId": wmanIf2CmnCpsSfId,
       "wmanIf2CmnCpsSfCid": wmanIf2CmnCpsSfCid,
       "wmanIf2CmnCpsSfDirection": wmanIf2CmnCpsSfDirection,
       "wmanIf2CmnCpsSfState": wmanIf2CmnCpsSfState,
       "wmanIf2CmnCpsTrafficPriority": wmanIf2CmnCpsTrafficPriority,
       "wmanIf2CmnCpsMaxSustainedRate": wmanIf2CmnCpsMaxSustainedRate,
       "wmanIf2CmnCpsMaxTrafficBurst": wmanIf2CmnCpsMaxTrafficBurst,
       "wmanIf2CmnCpsMinReservedRate": wmanIf2CmnCpsMinReservedRate,
       "wmanIf2CmnCpsToleratedJitter": wmanIf2CmnCpsToleratedJitter,
       "wmanIf2CmnCpsMaxLatency": wmanIf2CmnCpsMaxLatency,
       "wmanIf2CmnCpsFixedVsVariableSduInd": wmanIf2CmnCpsFixedVsVariableSduInd,
       "wmanIf2CmnCpsSduSize": wmanIf2CmnCpsSduSize,
       "wmanIf2CmnCpsSfSchedulingType": wmanIf2CmnCpsSfSchedulingType,
       "wmanIf2CmnCpsArqEnable": wmanIf2CmnCpsArqEnable,
       "wmanIf2CmnCpsArqWindowSize": wmanIf2CmnCpsArqWindowSize,
       "wmanIf2CmnCpsArqBlockLifetime": wmanIf2CmnCpsArqBlockLifetime,
       "wmanIf2CmnCpsArqSyncLossTimeout": wmanIf2CmnCpsArqSyncLossTimeout,
       "wmanIf2CmnCpsArqDeliverInOrder": wmanIf2CmnCpsArqDeliverInOrder,
       "wmanIf2CmnCpsArqRxPurgeTimeout": wmanIf2CmnCpsArqRxPurgeTimeout,
       "wmanIf2CmnCpsArqBlockSize": wmanIf2CmnCpsArqBlockSize,
       "wmanIf2CmnCpsMinRsvdTolerableRate": wmanIf2CmnCpsMinRsvdTolerableRate,
       "wmanIf2CmnCpsReqTxPolicy": wmanIf2CmnCpsReqTxPolicy,
       "wmanIf2CmnSfCsSpecification": wmanIf2CmnSfCsSpecification,
       "wmanIf2CmnCpsTargetSaid": wmanIf2CmnCpsTargetSaid,
       "wmanIf2CmnBsSsConfigurationTable": wmanIf2CmnBsSsConfigurationTable,
       "wmanIf2CmnBsSsConfigurationEntry": wmanIf2CmnBsSsConfigurationEntry,
       "wmanIf2CmnInvitedRangRetries": wmanIf2CmnInvitedRangRetries,
       "wmanIf2CmnDSxReqRetries": wmanIf2CmnDSxReqRetries,
       "wmanIf2CmnDSxRespRetries": wmanIf2CmnDSxRespRetries,
       "wmanIf2CmnT7Timeout": wmanIf2CmnT7Timeout,
       "wmanIf2CmnT8Timeout": wmanIf2CmnT8Timeout,
       "wmanIf2CmnT10Timeout": wmanIf2CmnT10Timeout,
       "wmanIf2CmnT22Timeout": wmanIf2CmnT22Timeout,
       "wmanIf2MibConformance": wmanIf2MibConformance,
       "wmanIf2MibGroups": wmanIf2MibGroups,
       "wmanIf2MibCommonGroup": wmanIf2MibCommonGroup,
       "wmanIf2MibQoSGroup": wmanIf2MibQoSGroup,
       "wmanIf2MibBsGroup": wmanIf2MibBsGroup,
       "wmanIf2MibBsAasGroup": wmanIf2MibBsAasGroup,
       "wmanIf2MibBsOfdmaGroup": wmanIf2MibBsOfdmaGroup,
       "wmanIf2MibAllObjects": wmanIf2MibAllObjects,
       "wmanIf2MibCompliances": wmanIf2MibCompliances,
       "wmanIf2MibCompliance": wmanIf2MibCompliance}
)
