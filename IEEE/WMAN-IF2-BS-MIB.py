# SNMP MIB module (WMAN-IF2-BS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/WMAN-IF2-BS-MIB.mib
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

wmanIf2BsMib = ModuleIdentity(
    (1, 0, 8802, 16, 2)
)
if mibBuilder.loadTexts:
    wmanIf2BsMib.setRevisions(
        ("2008-02-11 00:00",
         "2007-11-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



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
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ieee802Dot16Of2001", 1),
          ("ieee802Dot16cOf2002andPredcessors", 2),
          ("ieee802Dot16aOf2003andPredcessors", 3),
          ("ieee802Dot16Of2004", 4),
          ("ieee802Dot16Of2004and16eOf2005", 5),
          ("ieee802Dot16Of2004and16efOf2005", 6),
          ("ieee802Dot16Of04and16efOf05and16gOf07", 7),
          ("ieee802Dot16Of2008", 8))
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



class WmanIf2NumOfCid(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class WmanIf2MaxDsxFlowType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
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



class WmanIf2MaxNumOfSaType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class WmanIf2MaxClassifiers(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
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


class WmanIf2OfdmaDemoMimo(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("twoAntStcMatrixA", 0),
          ("twoAntStcMatrixBVertCoding", 1),
          ("twoAntStcMatrixBHorizCoding", 2),
          ("fourAntStcMatrixA", 3),
          ("fourAntStcMatrixBVertCoding", 4),
          ("fourAntStcMatrixBHorizCoding", 5),
          ("fourAntStcMatrixCVertCoding", 6),
          ("fourAntStcMatrixCHorizCodingt", 7),
          ("threeAntStcMatrixA", 8),
          ("threeAntStcMatrixB", 9),
          ("threeAntStcMatrixCVertCoding", 10),
          ("threeAntStcMatrixCHorizCodingt", 11),
          ("calculatingPrecodingWeight", 12),
          ("adaptiveRateControl", 13),
          ("calculatingChannelMatrix", 14),
          ("antennaGrouping", 15),
          ("antennaSelection", 16),
          ("codebookBasedPrecoding", 17),
          ("longTermPrecoding", 18),
          ("mimoMidamble", 19),
          ("alocGranularityDlPuscStc", 20),
          ("concurrentAlocDlPuscStc", 21))
    )


class WmanIf2OfdmaUlMimo(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("twoAntSttd", 0),
          ("twoAntSmVCoding", 1),
          ("oneAntCooperativeSm", 2))
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


class WmanIf2LinkDirection(TextualConvention, Integer32):
    status = "current"
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



class WmanIf2SaServiceType(TextualConvention, Integer32):
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
        *(("unicastService", 0),
          ("groupMulticastService", 1),
          ("mbsService", 2))
    )



class WmanIf2GlobalSrvClass(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ulDlIndicator", 0),
          ("maxSustainedRate0", 1),
          ("maxSustainedRate1", 2),
          ("maxSustainedRate2", 3),
          ("maxSustainedRate3", 4),
          ("maxSustainedRate4", 5),
          ("maxSustainedRate5", 6),
          ("trafficIndication", 7),
          ("maxTrafficBurst0", 8),
          ("maxTrafficBurst1", 9),
          ("maxTrafficBurst2", 10),
          ("maxTrafficBurst3", 11),
          ("maxTrafficBurst4", 12),
          ("maxTrafficBurst5", 13),
          ("minReservedRate0", 14),
          ("minReservedRate1", 15),
          ("minReservedRate2", 16),
          ("minReservedRate3", 17),
          ("minReservedRate4", 18),
          ("minReservedRate5", 19),
          ("maxLatency0", 20),
          ("maxLatency1", 21),
          ("maxLatency2", 22),
          ("maxLatency3", 23),
          ("maxLatency4", 24),
          ("maxLatency5", 25),
          ("sduIndicator", 26),
          ("pagingGeneration", 27),
          ("noBroadcastBr", 28),
          ("noMulticastBr", 29),
          ("noPiggybackReq", 30),
          ("noFragmentData", 31),
          ("noSurpressPayload", 32),
          ("noPackedSdu", 33),
          ("noCrcInMacPdu", 34),
          ("ulGrantType0", 35),
          ("ulGrantType1", 36),
          ("ulGrantType2", 37))
    )


class WmanIf2OfdmaFftSize(TextualConvention, Integer32):
    status = "current"
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
        *(("fft2048", 0),
          ("fft1024", 1),
          ("fft512", 2),
          ("reserved", 3),
          ("fft128", 4))
    )



class WmanIf2OfdmFftSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fft2048", 0),
          ("fft256", 3))
    )



class WmanIf2BsSsCapType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("xxxReq", 1),
          ("xxxRsp", 2))
    )



class WmanIf2BsCapType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inheritedBsCap", 1),
          ("configedBsCap", 2))
    )



class WmanIf2MaxNumBurstTx(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class WmanIf2MaxNumProvSf(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class WmanIf2MinNumFrmsPwrCtrl(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class WmanIf2OfdmaNoHarqChan(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class WmanIf2BasicCapOptions(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("arqSupport", 0),
          ("reserved1", 1),
          ("reserved2", 2),
          ("reserved3", 3),
          ("reserved4", 4),
          ("reserved5", 5),
          ("reserved6", 6),
          ("reserved7", 7),
          ("ipv4Support", 8),
          ("ipv6Support", 9),
          ("reserved10", 10),
          ("reserved11", 11),
          ("reserved12", 12),
          ("reserved13", 13),
          ("reserved14", 14),
          ("reserved15", 15),
          ("csSupportAtm", 16),
          ("csSupportIpv4", 17),
          ("csSupportIpv6", 18),
          ("csSupport802Dot3", 19),
          ("csSupport802Dot1Q", 20),
          ("csSupportIpv4Over802Dot3", 21),
          ("csSupportIpv6Over802Dot3", 22),
          ("csSupportIpv4Over802Dot1Q", 23),
          ("csSupportIpv6Over802Dot1Q", 24),
          ("csSupport802Dot3RohcHc", 25),
          ("csSupport802Dot3EcrtpHc", 26),
          ("csSupportIpv4Over6RohcHc", 27),
          ("csSupportIpv4Over6EcrtpHc", 28),
          ("csSupportGpcs", 29),
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
          ("reserved44", 44),
          ("reserved45", 45),
          ("reserved46", 46),
          ("reserved47", 47),
          ("phsSupportAtm", 48),
          ("phsSupportPacket", 49),
          ("reserved50", 50),
          ("reserved51", 51),
          ("reserved52", 52),
          ("reserved53", 53),
          ("reserved54", 54),
          ("reserved55", 55),
          ("reserved56", 56),
          ("bwAllocSupportFullDuplex", 57),
          ("reserved58", 58),
          ("reserved59", 59),
          ("reserved60", 60),
          ("reserved61", 61),
          ("reserved62", 62),
          ("reserved63", 63),
          ("pduConstructionpiggybackedRequests", 64),
          ("pduConstructionFsn3Bits", 65),
          ("reserved66", 66),
          ("reserved67", 67),
          ("reserved68", 68),
          ("reserved69", 69),
          ("reserved70", 70),
          ("reserved71", 71),
          ("packingSupported", 72),
          ("reserved73", 73),
          ("reserved74", 74),
          ("reserved75", 75),
          ("reserved76", 76),
          ("reserved77", 77),
          ("reserved78", 78),
          ("reserved79", 79),
          ("extendedRtpsSupported", 80),
          ("reserved81", 81),
          ("reserved82", 82),
          ("reserved83", 83),
          ("reserved84", 84),
          ("reserved85", 85),
          ("reserved86", 86),
          ("reserved87", 87),
          ("smcIpAddressAllocDhcp", 88),
          ("smcIpAddressAllocMobileIpv4", 89),
          ("smcIpAddressAllocMobileDhcpv6", 90),
          ("smcIpAddressAllocMobileIpv6Autoconfig", 91),
          ("reserved92", 92),
          ("reserved93", 93),
          ("reserved94", 94),
          ("reserved95", 95),
          ("arqSelectiveAck", 96),
          ("arqCumulativeAck", 97),
          ("arqCumWithSelAckEntry", 98),
          ("arqCumWithBlockSeqAck", 99),
          ("arqSeqBlockAck", 100),
          ("reserved101", 101),
          ("reserved102", 102),
          ("reserved103", 103),
          ("headerSupportBwReqUlTxPowerReport", 104),
          ("headerSupportBwReqCinrReport", 105),
          ("headerSupportCqichAllocationReq", 106),
          ("headerSupportPhyChannelReport", 107),
          ("headerSupportBwReqUlSleepCntl", 108),
          ("headerSupportSnReport", 109),
          ("headerSupportFeedbackReport", 110),
          ("headerSupportSduSn", 111),
          ("headerSupportSduSnPeriod0", 112),
          ("headerSupportSduSnPeriod1", 113),
          ("headerSupportSduSnPeriod2", 114),
          ("headerSupportDlSleepControl", 115),
          ("headerSupportFeedbackRequest", 116),
          ("headerSupportMimcModeFeedback", 117),
          ("headerSupportUlTxPowerReport", 118),
          ("headerSupportMiniFeedback", 119),
          ("headerSupportSnRequest", 120),
          ("reserved121", 121),
          ("reserved122", 122),
          ("reserved123", 123),
          ("reserved124", 124),
          ("reserved125", 125),
          ("reserved126", 126),
          ("reserved127", 127),
          ("pkmVersionSupport1", 128),
          ("pkmVersionSupport2", 129),
          ("reserved130", 130),
          ("reserved131", 131),
          ("reserved132", 132),
          ("reserved133", 133),
          ("reserved134", 134),
          ("reserved135", 135),
          ("authPolicySupportRsaInitialEntry", 136),
          ("authPolicySupportEapInitialEntry", 137),
          ("authPolicySupportAuthEapInitialEntry", 138),
          ("authPolicySupportRsaReentry", 139),
          ("authPolicySupportEapReentry", 140),
          ("authPolicySupportAuthEapReentry", 141),
          ("reserved142", 142),
          ("reserved143", 143),
          ("macModeHmac", 144),
          ("reserved145", 145),
          ("macModeHmac64", 146),
          ("macModeHmac80", 147),
          ("macModeHmac96", 148),
          ("macModeCmac", 149),
          ("reserved150", 150),
          ("reserved151", 151),
          ("extSubheader", 152),
          ("headerSupportShortPduSn", 153),
          ("headerSupportLongPduSn", 154),
          ("reserved155", 155),
          ("reserved156", 156),
          ("reserved157", 157),
          ("reserved158", 158),
          ("reserved159", 159))
    )


class WmanIf2OfdmCapOptions(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ofdmFftSize256", 0),
          ("ofdmFftSize2048", 1),
          ("reserved2", 2),
          ("reserved3", 3),
          ("reserved4", 4),
          ("reserved5", 5),
          ("reserved6", 6),
          ("reserved7", 7),
          ("ofdmSsDemodulatorQam64", 8),
          ("ofdmSsDemodulatorBtc", 9),
          ("ofdmSsDemodulatorCtc", 10),
          ("ofdmSsDemodulatorStc", 11),
          ("ofdmSsDemodulatorAas", 12),
          ("ofdmSsDemodulatorSuchan", 13),
          ("reserved14", 14),
          ("reserved15", 15),
          ("ofdmSsModulatorQam64", 16),
          ("ofdmSsModulatorBtc", 17),
          ("ofdmSsModulatorCtc", 18),
          ("ofdmSsModulatorSubchan", 19),
          ("ofdmSsModulatorFocusedCtBwReq", 20),
          ("ofdmSsModulatorUlCyclicDelay", 21),
          ("reserved22", 22),
          ("reserved23", 23),
          ("ofdmTcSublayerSupport", 24),
          ("reserved25", 25),
          ("reserved26", 26),
          ("reserved27", 27),
          ("reserved28", 28),
          ("reserved29", 29),
          ("reserved30", 30),
          ("reserved31", 31),
          ("ofdmRegularMap", 32),
          ("ofdmCompressedMap", 33),
          ("reserved34", 34),
          ("reserved35", 35),
          ("reserved36", 36),
          ("reserved37", 37),
          ("reserved38", 38),
          ("reserved39", 39),
          ("ofdmUlOpenLoopPwrCtrl", 40),
          ("ofdmUlAasPreamblePwrCtrl", 41),
          ("reserved42", 42),
          ("reserved43", 43),
          ("reserved44", 44),
          ("reserved45", 45),
          ("reserved46", 46),
          ("reserved47", 47),
          ("reserved48", 48))
    )


class WmanIf2OfdmaCapOptions(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("reserved0", 0),
          ("ofdmaFftSize2048", 1),
          ("ofdmaFftSize128", 2),
          ("ofdmaFftSize512", 3),
          ("ofdmaFftSize1024", 4),
          ("reserved5", 5),
          ("reserved6", 6),
          ("reserved7", 7),
          ("ofdmaDemodulatorQam64", 8),
          ("ofdmaDemodulatorBtc", 9),
          ("ofdmaDemodulatorCtc", 10),
          ("ofdmaDemodulatorStc", 11),
          ("ofdmaDemodulatorCcWithInterleaver", 12),
          ("ofdmaDemodulatorHarqChase", 13),
          ("ofdmaDemodulatorHarqCtclr", 14),
          ("reserved15", 15),
          ("ofdmaDemodulatorHarqCclr", 16),
          ("ofdmaDemodulatorLdpc", 17),
          ("ofdmaDemodulatorDedicatedPilots", 18),
          ("reserved19", 19),
          ("reserved20", 20),
          ("reserved21", 21),
          ("reserved22", 22),
          ("reserved23", 23),
          ("ofdmaModulatorQam64", 24),
          ("ofdmaModulatorBtc", 25),
          ("ofdmaModulatorCtc", 26),
          ("ofdmaModulatorStc", 27),
          ("ofdmaModulatorHarqChase", 28),
          ("ofdmaModulatorHarqCtcIr", 29),
          ("ofdmaModulatorHarqCcIr", 30),
          ("ofdmaModulatorHarqLdpc", 31),
          ("odfmaPermutationOptionalPusc", 32),
          ("odfmaPermutationOptionalFusc", 33),
          ("odfmaPermutationAmc1x6", 34),
          ("odfmaPermutationAmc2x3", 35),
          ("odfmaPermutationAmc3x2", 36),
          ("odfmaPermutationAmcWithHarqMap", 37),
          ("odfmaPermutationTusc1", 38),
          ("odfmaPermutationTusc2", 39),
          ("ofdmaDemodMimo2AntStcMatrixA", 40),
          ("ofdmaDemodMimo2AntStcMatrixBVCoding", 41),
          ("ofdmaDemodMimo2AntStcMatrixBHCoding", 42),
          ("ofdmaDemodMimo4AntStcMatrixA", 43),
          ("ofdmaDemodMimo4AntStcMatrixBVCoding", 44),
          ("ofdmaDemodMimo4AntStcMatrixBHCoding", 45),
          ("ofdmaDemodMimo4AntStcMatrixCVCoding", 46),
          ("ofdmaDemodMimo4AntStcMatrixCHCoding", 47),
          ("ofdmaDemodMimo3AntStcMatrixA", 48),
          ("ofdmaDemodMimo3AntStcMatrixB", 49),
          ("ofdmaDemodMimo3AntStcMatrixCVCoding", 50),
          ("ofdmaDemodMimo3AntStcMatrixCHCoding", 51),
          ("ofdmaDemodMimoCalcPrecodeWight", 52),
          ("ofdmaDemodMimoAdaptiveRateCtrl", 53),
          ("ofdmaDemodMimoCalcChanMatrix", 54),
          ("ofdmaDemodMimoAntGroup", 55),
          ("ofdmaDemodMimoAntSelect", 56),
          ("ofdmaDemodMimoCodebookPrecode", 57),
          ("ofdmaDemodMimoLongTermPrecode", 58),
          ("ofdmaDemodMimoMidamble", 59),
          ("ofdmaDemodAllocGranDlPuscStc", 60),
          ("ofdmaDemodConcurentAllocDlPuscStc", 61),
          ("reserved62", 62),
          ("reserved63", 63),
          ("ofdmaPrivateMapHarqMap", 64),
          ("ofdmaPrivateMap", 65),
          ("ofdmaPrivateMapReduced", 66),
          ("ofdmaPrivateMapChainEnable", 67),
          ("ofdmaPrivateMapDlFrameOffset", 68),
          ("ofdmaPrivateMapUlFrameOffset", 69),
          ("ofdmaPrivateMapChainConcurency0", 70),
          ("ofdmaPrivateMapChainConcurency1", 71),
          ("ofdmaAasZone", 72),
          ("ofdmaAasDiverityMapScan", 73),
          ("ofdmaAasFeedbackRsp", 74),
          ("ofdmaAasDlPreamble", 75),
          ("ofdmaAasUlPreamble", 76),
          ("reserved77", 77),
          ("reserved78", 78),
          ("reserved79", 79),
          ("ofdmaCinrPhysicalPreamble", 80),
          ("ofdmaCinrPhysicalPilotSubc", 81),
          ("ofdmaCinrPhysicalDataSubc", 82),
          ("ofdmaCinrEffectivePreamble", 83),
          ("ofdmaCinrEffectivePilotSubc", 84),
          ("ofdmaCinrEffectiveDataSubc", 85),
          ("ofdmaCinr2CqiChannel", 86),
          ("ofdmaFreqSelectivityReport", 87),
          ("ofdmaPwrCtrlOpenLoop", 88),
          ("ofdmaPwrCtrlAasPreamble", 89),
          ("reserved90", 90),
          ("reserved91", 91),
          ("reserved92", 92),
          ("reserved93", 93),
          ("reserved94", 94),
          ("reserved95", 95),
          ("ofdmaMapHarq", 96),
          ("ofdmaMapExtendedHarqIe", 97),
          ("ofdmaMapSubMapForFirstZone", 98),
          ("ofdmaMapSubMapForOtherZones", 99),
          ("ofdmaMapDlRegionDefinition", 100),
          ("reserved101", 101),
          ("reserved102", 102),
          ("reserved103", 103),
          ("ofdmaUlCtrlt3BitMimoFastFeedback", 104),
          ("ofdmaUlCtrltEnhancedFastFeedback", 105),
          ("ofdmaUlCtrltUlAck", 106),
          ("reserved107", 107),
          ("ofdmaUlCtrltUepFastFeedback", 108),
          ("ofdmaUlCtrltFastDlMeasurementFeedback", 109),
          ("ofdmaUlCtrltPriSecFastFeedback", 110),
          ("ofdmaDiucCqiFastFeedback", 111),
          ("ofdmaCsitTypeA", 112),
          ("ofdmaCsitTypeB", 113),
          ("ofdmaPowerAssignment", 114),
          ("ofdmaSoundingRspTime0", 115),
          ("ofdmaSoundingRspTime1", 116),
          ("ofdmaSoundingRspTime2", 117),
          ("ofdmaMaxSimuSoundInst0", 118),
          ("ofdmaMaxSimuSoundInst1", 119),
          ("ofdmaMaxSimuSoundInst2", 120),
          ("ofdmaMaxSimuSoundInst3", 121),
          ("ofdmaNoP9Or18ForCsitTypeA", 122),
          ("ofdmaCsitNotSupported", 123),
          ("reserved124", 124),
          ("reserved125", 125),
          ("reserved126", 126),
          ("reserved127", 127),
          ("ofdmaMaxHarqBurstsUl0", 128),
          ("ofdmaMaxHarqBurstsUl1", 129),
          ("ofdmaMaxHarqBurstsUl2", 130),
          ("ofdmaMaxHarqBurstsUlNonHarqIncluded", 131),
          ("ofdmaMaxHarqBurstsDl0", 132),
          ("ofdmaMaxHarqBurstsDl1", 133),
          ("ofdmaMaxHarqBurstsDl2", 134),
          ("ofdmaMaxHarqBurstsDl3", 135),
          ("ofdmaMimoMod2AntStcMatrixA", 136),
          ("ofdmaMimoMod2AntStcMatrixBVCoding", 137),
          ("ofdmaMimoMod2AntStcMatrixBHCoding", 138),
          ("ofdmaMimoModBeamforming", 139),
          ("ofdmaMimoModAdaptiveRateControl", 140),
          ("ofdmaMimoModSingleAnt", 141),
          ("ofdmaMimoModCollaborativeSm1Ant", 142),
          ("ofdmaMimoModCollaborativeSm2Ants", 143),
          ("ofdmaMimoModDisableUlSubchRotation", 144),
          ("reserved145", 145),
          ("reserved146", 146),
          ("reserved147", 147),
          ("reserved148", 148),
          ("reserved149", 149),
          ("reserved150", 150),
          ("reserved151", 151),
          ("ofdmaMcastBurstsDlMultiFecTypes", 152),
          ("ofdmaMcastBurstsUlMultiFecTypes", 153),
          ("reserved154", 154),
          ("reserved155", 155),
          ("reserved156", 156),
          ("reserved157", 157),
          ("reserved158", 158),
          ("reserved159", 159),
          ("ofdmaHarqIncrBufDlNep0", 160),
          ("ofdmaHarqIncrBufDlNep1", 161),
          ("ofdmaHarqIncrBufDlNep2", 162),
          ("ofdmaHarqIncrBufDlNep3", 163),
          ("ofdmaHarqIncrBufDlAggFlag", 164),
          ("reserved165", 165),
          ("reserved166", 166),
          ("reserved167", 167),
          ("ofdmaHarqIncrBufUlNep0", 168),
          ("ofdmaHarqIncrBufUlNep1", 169),
          ("ofdmaHarqIncrBufUlNep2", 170),
          ("ofdmaHarqIncrBufUlNep3", 171),
          ("ofdmaHarqIncrBufUlAggFlag", 172),
          ("reserved173", 173),
          ("reserved174", 174),
          ("reserved175", 175),
          ("ofdmaHarqChaseBufDlComb0", 176),
          ("ofdmaHarqChaseBufDlComb1", 177),
          ("ofdmaHarqChaseBufDlComb2", 178),
          ("ofdmaHarqChaseBufDlComb3", 179),
          ("ofdmaHarqChaseBufDlComb4", 180),
          ("ofdmaHarqChaseBufDlComb5", 181),
          ("ofdmaHarqChaseBufDlAggFlag", 182),
          ("reserved183", 183),
          ("ofdmaHarqChaseBufUlComb0", 184),
          ("ofdmaHarqChaseBufUlComb1", 185),
          ("ofdmaHarqChaseBufUlComb2", 186),
          ("ofdmaHarqChaseBufUlComb3", 187),
          ("ofdmaHarqChaseBufUlComb4", 188),
          ("ofdmaHarqChaseBufUlComb5", 189),
          ("ofdmaHarqChaseBufUlAggFlag", 190),
          ("reserved191", 191),
          ("odfmaParamSetPhyA", 192),
          ("odfmaParamSetPhyB", 193),
          ("odfmaParamSetHarq0", 194),
          ("odfmaParamSetHarq1", 195),
          ("odfmaParamSetHarq2", 196),
          ("odfmaParamSetMacA", 197),
          ("odfmaParamSetMacB", 198),
          ("reserved199", 199))
    )


# MIB Managed Objects in the order of their OIDs

_WmanIf2MibObjects_ObjectIdentity = ObjectIdentity
wmanIf2MibObjects = _WmanIf2MibObjects_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1)
)
_WmanIf2BsFm_ObjectIdentity = ObjectIdentity
wmanIf2BsFm = _WmanIf2BsFm_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 1)
)
_WmanIf2BsTrapControl_ObjectIdentity = ObjectIdentity
wmanIf2BsTrapControl = _WmanIf2BsTrapControl_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 1, 1)
)


class _WmanIf2BsTrapControlRegister_Type(Bits):
    """Custom type wmanIf2BsTrapControlRegister based on Bits"""
    namedValues = NamedValues(
        *(("wmanIf2BsSsStatusNotification", 0),
          ("wmanIf2BsSsDynamicServiceFail", 1),
          ("wmanIf2BsSsRssiStatusChange", 2),
          ("wmanIf2BsSsRegister", 3),
          ("wmanIf2BsSsPkmFail", 4),
          ("wmanIf2BsPerformanceCounters", 5))
    )

_WmanIf2BsTrapControlRegister_Type.__name__ = "Bits"
_WmanIf2BsTrapControlRegister_Object = MibScalar
wmanIf2BsTrapControlRegister = _WmanIf2BsTrapControlRegister_Object(
    (1, 0, 8802, 16, 2, 1, 1, 1, 1),
    _WmanIf2BsTrapControlRegister_Type()
)
wmanIf2BsTrapControlRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsTrapControlRegister.setStatus("current")


class _WmanIf2BsStatusTrapControlRegister_Type(Bits):
    """Custom type wmanIf2BsStatusTrapControlRegister based on Bits"""
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

_WmanIf2BsStatusTrapControlRegister_Type.__name__ = "Bits"
_WmanIf2BsStatusTrapControlRegister_Object = MibScalar
wmanIf2BsStatusTrapControlRegister = _WmanIf2BsStatusTrapControlRegister_Object(
    (1, 0, 8802, 16, 2, 1, 1, 1, 2),
    _WmanIf2BsStatusTrapControlRegister_Type()
)
wmanIf2BsStatusTrapControlRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsStatusTrapControlRegister.setStatus("current")
_WmanIf2BsThresholdConfigTable_Object = MibTable
wmanIf2BsThresholdConfigTable = _WmanIf2BsThresholdConfigTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wmanIf2BsThresholdConfigTable.setStatus("current")
_WmanIf2BsThresholdConfigEntry_Object = MibTableRow
wmanIf2BsThresholdConfigEntry = _WmanIf2BsThresholdConfigEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 1, 3, 1)
)
wmanIf2BsThresholdConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsThresholdConfigEntry.setStatus("current")
_WmanIf2BsRssiLowThreshold_Type = Integer32
_WmanIf2BsRssiLowThreshold_Object = MibTableColumn
wmanIf2BsRssiLowThreshold = _WmanIf2BsRssiLowThreshold_Object(
    (1, 0, 8802, 16, 2, 1, 1, 1, 3, 1, 1),
    _WmanIf2BsRssiLowThreshold_Type()
)
wmanIf2BsRssiLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsRssiLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsRssiLowThreshold.setUnits("dBm")
_WmanIf2BsRssiHighThreshold_Type = Integer32
_WmanIf2BsRssiHighThreshold_Object = MibTableColumn
wmanIf2BsRssiHighThreshold = _WmanIf2BsRssiHighThreshold_Object(
    (1, 0, 8802, 16, 2, 1, 1, 1, 3, 1, 2),
    _WmanIf2BsRssiHighThreshold_Type()
)
wmanIf2BsRssiHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsRssiHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsRssiHighThreshold.setUnits("dBm")
_WmanIf2BsTrapDefinitions_ObjectIdentity = ObjectIdentity
wmanIf2BsTrapDefinitions = _WmanIf2BsTrapDefinitions_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 1, 2)
)
_WmanIf2BsTrapPrefix_ObjectIdentity = ObjectIdentity
wmanIf2BsTrapPrefix = _WmanIf2BsTrapPrefix_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 1, 2, 0)
)
_WmanIf2BsSsNotificationObjectsTable_Object = MibTable
wmanIf2BsSsNotificationObjectsTable = _WmanIf2BsSsNotificationObjectsTable_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsNotificationObjectsTable.setStatus("current")
_WmanIf2BsSsNotificationObjectsEntry_Object = MibTableRow
wmanIf2BsSsNotificationObjectsEntry = _WmanIf2BsSsNotificationObjectsEntry_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1)
)
wmanIf2BsSsNotificationObjectsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsSsNotificationMacAddr"),
)
if mibBuilder.loadTexts:
    wmanIf2BsSsNotificationObjectsEntry.setStatus("current")
_WmanIf2BsSsNotificationMacAddr_Type = MacAddress
_WmanIf2BsSsNotificationMacAddr_Object = MibTableColumn
wmanIf2BsSsNotificationMacAddr = _WmanIf2BsSsNotificationMacAddr_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 1),
    _WmanIf2BsSsNotificationMacAddr_Type()
)
wmanIf2BsSsNotificationMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsNotificationMacAddr.setStatus("current")


class _WmanIf2BsSsStatusValue_Type(Integer32):
    """Custom type wmanIf2BsSsStatusValue based on Integer32"""
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


_WmanIf2BsSsStatusValue_Type.__name__ = "Integer32"
_WmanIf2BsSsStatusValue_Object = MibTableColumn
wmanIf2BsSsStatusValue = _WmanIf2BsSsStatusValue_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 2),
    _WmanIf2BsSsStatusValue_Type()
)
wmanIf2BsSsStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsStatusValue.setStatus("current")


class _WmanIf2BsSsStatusInfo_Type(OctetString):
    """Custom type wmanIf2BsSsStatusInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WmanIf2BsSsStatusInfo_Type.__name__ = "OctetString"
_WmanIf2BsSsStatusInfo_Object = MibTableColumn
wmanIf2BsSsStatusInfo = _WmanIf2BsSsStatusInfo_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 3),
    _WmanIf2BsSsStatusInfo_Type()
)
wmanIf2BsSsStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsStatusInfo.setStatus("current")


class _WmanIf2BsDynamicServiceType_Type(Integer32):
    """Custom type wmanIf2BsDynamicServiceType based on Integer32"""
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


_WmanIf2BsDynamicServiceType_Type.__name__ = "Integer32"
_WmanIf2BsDynamicServiceType_Object = MibTableColumn
wmanIf2BsDynamicServiceType = _WmanIf2BsDynamicServiceType_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 4),
    _WmanIf2BsDynamicServiceType_Type()
)
wmanIf2BsDynamicServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsDynamicServiceType.setStatus("current")


class _WmanIf2BsDynamicServiceFailReason_Type(OctetString):
    """Custom type wmanIf2BsDynamicServiceFailReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WmanIf2BsDynamicServiceFailReason_Type.__name__ = "OctetString"
_WmanIf2BsDynamicServiceFailReason_Object = MibTableColumn
wmanIf2BsDynamicServiceFailReason = _WmanIf2BsDynamicServiceFailReason_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 5),
    _WmanIf2BsDynamicServiceFailReason_Type()
)
wmanIf2BsDynamicServiceFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsDynamicServiceFailReason.setStatus("current")


class _WmanIf2BsSsRssiStatus_Type(Integer32):
    """Custom type wmanIf2BsSsRssiStatus based on Integer32"""
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


_WmanIf2BsSsRssiStatus_Type.__name__ = "Integer32"
_WmanIf2BsSsRssiStatus_Object = MibTableColumn
wmanIf2BsSsRssiStatus = _WmanIf2BsSsRssiStatus_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 6),
    _WmanIf2BsSsRssiStatus_Type()
)
wmanIf2BsSsRssiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRssiStatus.setStatus("current")


class _WmanIf2BsSsRssiStatusInfo_Type(OctetString):
    """Custom type wmanIf2BsSsRssiStatusInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WmanIf2BsSsRssiStatusInfo_Type.__name__ = "OctetString"
_WmanIf2BsSsRssiStatusInfo_Object = MibTableColumn
wmanIf2BsSsRssiStatusInfo = _WmanIf2BsSsRssiStatusInfo_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 7),
    _WmanIf2BsSsRssiStatusInfo_Type()
)
wmanIf2BsSsRssiStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRssiStatusInfo.setStatus("current")


class _WmanIf2BsSsRegisterStatus_Type(Integer32):
    """Custom type wmanIf2BsSsRegisterStatus based on Integer32"""
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


_WmanIf2BsSsRegisterStatus_Type.__name__ = "Integer32"
_WmanIf2BsSsRegisterStatus_Object = MibTableColumn
wmanIf2BsSsRegisterStatus = _WmanIf2BsSsRegisterStatus_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 8),
    _WmanIf2BsSsRegisterStatus_Type()
)
wmanIf2BsSsRegisterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRegisterStatus.setStatus("current")


class _WmanIf2BsDynamicServiceFailSfid_Type(Unsigned32):
    """Custom type wmanIf2BsDynamicServiceFailSfid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIf2BsDynamicServiceFailSfid_Type.__name__ = "Unsigned32"
_WmanIf2BsDynamicServiceFailSfid_Object = MibTableColumn
wmanIf2BsDynamicServiceFailSfid = _WmanIf2BsDynamicServiceFailSfid_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 9),
    _WmanIf2BsDynamicServiceFailSfid_Type()
)
wmanIf2BsDynamicServiceFailSfid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsDynamicServiceFailSfid.setStatus("current")
_WmanIf2BsEventNotificationTime_Type = TimeStamp
_WmanIf2BsEventNotificationTime_Object = MibTableColumn
wmanIf2BsEventNotificationTime = _WmanIf2BsEventNotificationTime_Object(
    (1, 0, 8802, 16, 2, 1, 1, 2, 1, 1, 10),
    _WmanIf2BsEventNotificationTime_Type()
)
wmanIf2BsEventNotificationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsEventNotificationTime.setStatus("current")
_WmanIf2BsCm_ObjectIdentity = ObjectIdentity
wmanIf2BsCm = _WmanIf2BsCm_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 2)
)
_WmanIf2BsRegisteredSsTable_Object = MibTable
wmanIf2BsRegisteredSsTable = _WmanIf2BsRegisteredSsTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsRegisteredSsTable.setStatus("current")
_WmanIf2BsRegisteredSsEntry_Object = MibTableRow
wmanIf2BsRegisteredSsEntry = _WmanIf2BsRegisteredSsEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 1, 1)
)
wmanIf2BsRegisteredSsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsSsMacAddress"),
)
if mibBuilder.loadTexts:
    wmanIf2BsRegisteredSsEntry.setStatus("current")
_WmanIf2BsSsMacAddress_Type = MacAddress
_WmanIf2BsSsMacAddress_Object = MibTableColumn
wmanIf2BsSsMacAddress = _WmanIf2BsSsMacAddress_Object(
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 1),
    _WmanIf2BsSsMacAddress_Type()
)
wmanIf2BsSsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsSsMacAddress.setStatus("current")
_WmanIf2BsSsBasicCid_Type = WmanIf2CidType
_WmanIf2BsSsBasicCid_Object = MibTableColumn
wmanIf2BsSsBasicCid = _WmanIf2BsSsBasicCid_Object(
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 2),
    _WmanIf2BsSsBasicCid_Type()
)
wmanIf2BsSsBasicCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsBasicCid.setStatus("current")
_WmanIf2BsSsPrimaryCid_Type = WmanIf2CidType
_WmanIf2BsSsPrimaryCid_Object = MibTableColumn
wmanIf2BsSsPrimaryCid = _WmanIf2BsSsPrimaryCid_Object(
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 3),
    _WmanIf2BsSsPrimaryCid_Type()
)
wmanIf2BsSsPrimaryCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPrimaryCid.setStatus("current")
_WmanIf2BsSsSecondaryCid_Type = WmanIf2CidType
_WmanIf2BsSsSecondaryCid_Object = MibTableColumn
wmanIf2BsSsSecondaryCid = _WmanIf2BsSsSecondaryCid_Object(
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 4),
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
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 5),
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
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 6),
    _WmanIf2BsSsIpManagementMode_Type()
)
wmanIf2BsSsIpManagementMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsIpManagementMode.setStatus("current")
_WmanIf2BsSs2ndMgmtArqEnable_Type = TruthValue
_WmanIf2BsSs2ndMgmtArqEnable_Object = MibTableColumn
wmanIf2BsSs2ndMgmtArqEnable = _WmanIf2BsSs2ndMgmtArqEnable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 7),
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
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 8),
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
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 9),
    _WmanIf2BsSs2ndMgmtArqDnLinkTxDelay_Type()
)
wmanIf2BsSs2ndMgmtArqDnLinkTxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqDnLinkTxDelay.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqDnLinkTxDelay.setUnits("microsecond")


class _WmanIf2BsSs2ndMgmtArqUpLinkTxDelay_Type(Integer32):
    """Custom type wmanIf2BsSs2ndMgmtArqUpLinkTxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSs2ndMgmtArqUpLinkTxDelay_Type.__name__ = "Integer32"
_WmanIf2BsSs2ndMgmtArqUpLinkTxDelay_Object = MibTableColumn
wmanIf2BsSs2ndMgmtArqUpLinkTxDelay = _WmanIf2BsSs2ndMgmtArqUpLinkTxDelay_Object(
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 10),
    _WmanIf2BsSs2ndMgmtArqUpLinkTxDelay_Type()
)
wmanIf2BsSs2ndMgmtArqUpLinkTxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqUpLinkTxDelay.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqUpLinkTxDelay.setUnits("microsecond")


class _WmanIf2BsSs2ndMgmtArqDnLinkRxDelay_Type(Integer32):
    """Custom type wmanIf2BsSs2ndMgmtArqDnLinkRxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSs2ndMgmtArqDnLinkRxDelay_Type.__name__ = "Integer32"
_WmanIf2BsSs2ndMgmtArqDnLinkRxDelay_Object = MibTableColumn
wmanIf2BsSs2ndMgmtArqDnLinkRxDelay = _WmanIf2BsSs2ndMgmtArqDnLinkRxDelay_Object(
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 11),
    _WmanIf2BsSs2ndMgmtArqDnLinkRxDelay_Type()
)
wmanIf2BsSs2ndMgmtArqDnLinkRxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqDnLinkRxDelay.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqDnLinkRxDelay.setUnits("microsecond")


class _WmanIf2BsSs2ndMgmtArqUpLinkRxDelay_Type(Integer32):
    """Custom type wmanIf2BsSs2ndMgmtArqUpLinkRxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSs2ndMgmtArqUpLinkRxDelay_Type.__name__ = "Integer32"
_WmanIf2BsSs2ndMgmtArqUpLinkRxDelay_Object = MibTableColumn
wmanIf2BsSs2ndMgmtArqUpLinkRxDelay = _WmanIf2BsSs2ndMgmtArqUpLinkRxDelay_Object(
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 12),
    _WmanIf2BsSs2ndMgmtArqUpLinkRxDelay_Type()
)
wmanIf2BsSs2ndMgmtArqUpLinkRxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqUpLinkRxDelay.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqUpLinkRxDelay.setUnits("microsecond")


class _WmanIf2BsSs2ndMgmtArqBlockLifetime_Type(Integer32):
    """Custom type wmanIf2BsSs2ndMgmtArqBlockLifetime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSs2ndMgmtArqBlockLifetime_Type.__name__ = "Integer32"
_WmanIf2BsSs2ndMgmtArqBlockLifetime_Object = MibTableColumn
wmanIf2BsSs2ndMgmtArqBlockLifetime = _WmanIf2BsSs2ndMgmtArqBlockLifetime_Object(
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 13),
    _WmanIf2BsSs2ndMgmtArqBlockLifetime_Type()
)
wmanIf2BsSs2ndMgmtArqBlockLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqBlockLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqBlockLifetime.setUnits("10 us")


class _WmanIf2BsSs2ndMgmtArqSyncLossTimeout_Type(Integer32):
    """Custom type wmanIf2BsSs2ndMgmtArqSyncLossTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSs2ndMgmtArqSyncLossTimeout_Type.__name__ = "Integer32"
_WmanIf2BsSs2ndMgmtArqSyncLossTimeout_Object = MibTableColumn
wmanIf2BsSs2ndMgmtArqSyncLossTimeout = _WmanIf2BsSs2ndMgmtArqSyncLossTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 14),
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
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 15),
    _WmanIf2BsSs2ndMgmtArqDeliverInOrder_Type()
)
wmanIf2BsSs2ndMgmtArqDeliverInOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSs2ndMgmtArqDeliverInOrder.setStatus("current")


class _WmanIf2BsSs2ndMgmtArqRxPurgeTimeout_Type(Integer32):
    """Custom type wmanIf2BsSs2ndMgmtArqRxPurgeTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSs2ndMgmtArqRxPurgeTimeout_Type.__name__ = "Integer32"
_WmanIf2BsSs2ndMgmtArqRxPurgeTimeout_Object = MibTableColumn
wmanIf2BsSs2ndMgmtArqRxPurgeTimeout = _WmanIf2BsSs2ndMgmtArqRxPurgeTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 16),
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
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 17),
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
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 18),
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
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 19),
    _WmanIf2BsSsAasBroadcastPermission_Type()
)
wmanIf2BsSsAasBroadcastPermission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsAasBroadcastPermission.setStatus("current")
_WmanIf2BsSsMaxTxPowerBpsk_Type = WmanIf2MaxTxPowerType
_WmanIf2BsSsMaxTxPowerBpsk_Object = MibTableColumn
wmanIf2BsSsMaxTxPowerBpsk = _WmanIf2BsSsMaxTxPowerBpsk_Object(
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 20),
    _WmanIf2BsSsMaxTxPowerBpsk_Type()
)
wmanIf2BsSsMaxTxPowerBpsk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsMaxTxPowerBpsk.setStatus("current")
_WmanIf2BsSsMaxTxPowerQpsk_Type = WmanIf2MaxTxPowerType
_WmanIf2BsSsMaxTxPowerQpsk_Object = MibTableColumn
wmanIf2BsSsMaxTxPowerQpsk = _WmanIf2BsSsMaxTxPowerQpsk_Object(
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 21),
    _WmanIf2BsSsMaxTxPowerQpsk_Type()
)
wmanIf2BsSsMaxTxPowerQpsk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsMaxTxPowerQpsk.setStatus("current")
_WmanIf2BsSsMaxTxPower16Qam_Type = WmanIf2MaxTxPowerType
_WmanIf2BsSsMaxTxPower16Qam_Object = MibTableColumn
wmanIf2BsSsMaxTxPower16Qam = _WmanIf2BsSsMaxTxPower16Qam_Object(
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 22),
    _WmanIf2BsSsMaxTxPower16Qam_Type()
)
wmanIf2BsSsMaxTxPower16Qam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsMaxTxPower16Qam.setStatus("current")
_WmanIf2BsSsMaxTxPower64Qam_Type = WmanIf2MaxTxPowerType
_WmanIf2BsSsMaxTxPower64Qam_Object = MibTableColumn
wmanIf2BsSsMaxTxPower64Qam = _WmanIf2BsSsMaxTxPower64Qam_Object(
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 23),
    _WmanIf2BsSsMaxTxPower64Qam_Type()
)
wmanIf2BsSsMaxTxPower64Qam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsMaxTxPower64Qam.setStatus("current")
_WmanIf2BsSsMacVersion_Type = WmanIf2MacVersion
_WmanIf2BsSsMacVersion_Object = MibTableColumn
wmanIf2BsSsMacVersion = _WmanIf2BsSsMacVersion_Object(
    (1, 0, 8802, 16, 2, 1, 2, 1, 1, 24),
    _WmanIf2BsSsMacVersion_Type()
)
wmanIf2BsSsMacVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsMacVersion.setStatus("current")
_WmanIf2BsConfigurationTable_Object = MibTable
wmanIf2BsConfigurationTable = _WmanIf2BsConfigurationTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wmanIf2BsConfigurationTable.setStatus("current")
_WmanIf2BsConfigurationEntry_Object = MibTableRow
wmanIf2BsConfigurationEntry = _WmanIf2BsConfigurationEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1)
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
        ValueRangeConstraint(0, 10000),
    )


_WmanIf2BsDcdInterval_Type.__name__ = "Integer32"
_WmanIf2BsDcdInterval_Object = MibTableColumn
wmanIf2BsDcdInterval = _WmanIf2BsDcdInterval_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 1),
    _WmanIf2BsDcdInterval_Type()
)
wmanIf2BsDcdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsDcdInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsDcdInterval.setUnits("milliseconds")


class _WmanIf2BsUcdInterval_Type(Integer32):
    """Custom type wmanIf2BsUcdInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WmanIf2BsUcdInterval_Type.__name__ = "Integer32"
_WmanIf2BsUcdInterval_Object = MibTableColumn
wmanIf2BsUcdInterval = _WmanIf2BsUcdInterval_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 2),
    _WmanIf2BsUcdInterval_Type()
)
wmanIf2BsUcdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsUcdInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsUcdInterval.setUnits("milliseconds")


class _WmanIf2BsUcdTransition_Type(Integer32):
    """Custom type wmanIf2BsUcdTransition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_WmanIf2BsUcdTransition_Type.__name__ = "Integer32"
_WmanIf2BsUcdTransition_Object = MibTableColumn
wmanIf2BsUcdTransition = _WmanIf2BsUcdTransition_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 3),
    _WmanIf2BsUcdTransition_Type()
)
wmanIf2BsUcdTransition.setMaxAccess("read-write")
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
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 4),
    _WmanIf2BsDcdTransition_Type()
)
wmanIf2BsDcdTransition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsDcdTransition.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsDcdTransition.setUnits("Number of MAC Frames")


class _WmanIf2BsInitialRangingInterval_Type(Integer32):
    """Custom type wmanIf2BsInitialRangingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_WmanIf2BsInitialRangingInterval_Type.__name__ = "Integer32"
_WmanIf2BsInitialRangingInterval_Object = MibTableColumn
wmanIf2BsInitialRangingInterval = _WmanIf2BsInitialRangingInterval_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 5),
    _WmanIf2BsInitialRangingInterval_Type()
)
wmanIf2BsInitialRangingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsInitialRangingInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsInitialRangingInterval.setUnits("milliseconds")


class _WmanIf2BsSsULMapProcTime_Type(Unsigned32):
    """Custom type wmanIf2BsSsULMapProcTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 4294967295),
    )


_WmanIf2BsSsULMapProcTime_Type.__name__ = "Unsigned32"
_WmanIf2BsSsULMapProcTime_Object = MibTableColumn
wmanIf2BsSsULMapProcTime = _WmanIf2BsSsULMapProcTime_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 6),
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
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 7),
    _WmanIf2BsSsRangRespProcTime_Type()
)
wmanIf2BsSsRangRespProcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsRangRespProcTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSsRangRespProcTime.setUnits("micro seconds")


class _WmanIf2BsT9Timeout_Type(Integer32):
    """Custom type wmanIf2BsT9Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 65535),
    )


_WmanIf2BsT9Timeout_Type.__name__ = "Integer32"
_WmanIf2BsT9Timeout_Object = MibTableColumn
wmanIf2BsT9Timeout = _WmanIf2BsT9Timeout_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 9),
    _WmanIf2BsT9Timeout_Type()
)
wmanIf2BsT9Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsT9Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsT9Timeout.setUnits("milliseconds")


class _WmanIf2BsT13Timeout_Type(Integer32):
    """Custom type wmanIf2BsT13Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 65535),
    )


_WmanIf2BsT13Timeout_Type.__name__ = "Integer32"
_WmanIf2BsT13Timeout_Object = MibTableColumn
wmanIf2BsT13Timeout = _WmanIf2BsT13Timeout_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 10),
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
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 11),
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
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 12),
    _WmanIf2BsT17Timeout_Type()
)
wmanIf2BsT17Timeout.setMaxAccess("read-write")
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
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 13),
    _WmanIf2BsT27IdleTimer_Type()
)
wmanIf2BsT27IdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsT27IdleTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsT27IdleTimer.setUnits("microsecond")


class _WmanIf2BsT27ActiveTimer_Type(Unsigned32):
    """Custom type wmanIf2BsT27ActiveTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 4294967295),
    )


_WmanIf2BsT27ActiveTimer_Type.__name__ = "Unsigned32"
_WmanIf2BsT27ActiveTimer_Object = MibTableColumn
wmanIf2BsT27ActiveTimer = _WmanIf2BsT27ActiveTimer_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 14),
    _WmanIf2BsT27ActiveTimer_Type()
)
wmanIf2BsT27ActiveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsT27ActiveTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsT27ActiveTimer.setUnits("microsecond")


class _WmanIf2Bs2ndMgmtDlQoSProfileIndex_Type(Integer32):
    """Custom type wmanIf2Bs2ndMgmtDlQoSProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2Bs2ndMgmtDlQoSProfileIndex_Type.__name__ = "Integer32"
_WmanIf2Bs2ndMgmtDlQoSProfileIndex_Object = MibTableColumn
wmanIf2Bs2ndMgmtDlQoSProfileIndex = _WmanIf2Bs2ndMgmtDlQoSProfileIndex_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 15),
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
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 16),
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
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 17),
    _WmanIf2BsAutoSfidEnabled_Type()
)
wmanIf2BsAutoSfidEnabled.setMaxAccess("read-write")
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
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 18),
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
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 19),
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
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 20),
    _WmanIf2BsAasChanFbckReqFreq_Type()
)
wmanIf2BsAasChanFbckReqFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsAasChanFbckReqFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsAasChanFbckReqFreq.setUnits("millisecond")


class _WmanIf2BsAasBeamSelectFreq_Type(Integer32):
    """Custom type wmanIf2BsAasBeamSelectFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10000),
    )


_WmanIf2BsAasBeamSelectFreq_Type.__name__ = "Integer32"
_WmanIf2BsAasBeamSelectFreq_Object = MibTableColumn
wmanIf2BsAasBeamSelectFreq = _WmanIf2BsAasBeamSelectFreq_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 21),
    _WmanIf2BsAasBeamSelectFreq_Type()
)
wmanIf2BsAasBeamSelectFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsAasBeamSelectFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsAasBeamSelectFreq.setUnits("millisecond")


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
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 22),
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
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 23),
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
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 24),
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
        *(("noAction", 0),
          ("sectorReset", 1))
    )


_WmanIf2BsResetSector_Type.__name__ = "Integer32"
_WmanIf2BsResetSector_Object = MibTableColumn
wmanIf2BsResetSector = _WmanIf2BsResetSector_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 25),
    _WmanIf2BsResetSector_Type()
)
wmanIf2BsResetSector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsResetSector.setStatus("current")


class _WmanIf2BsSaChallengeTimer_Type(Integer32):
    """Custom type wmanIf2BsSaChallengeTimer based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 2000),
    )


_WmanIf2BsSaChallengeTimer_Type.__name__ = "Integer32"
_WmanIf2BsSaChallengeTimer_Object = MibTableColumn
wmanIf2BsSaChallengeTimer = _WmanIf2BsSaChallengeTimer_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 27),
    _WmanIf2BsSaChallengeTimer_Type()
)
wmanIf2BsSaChallengeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSaChallengeTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSaChallengeTimer.setUnits("milliseconds")


class _WmanIf2BsSaChallengeMaxResends_Type(Integer32):
    """Custom type wmanIf2BsSaChallengeMaxResends based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WmanIf2BsSaChallengeMaxResends_Type.__name__ = "Integer32"
_WmanIf2BsSaChallengeMaxResends_Object = MibTableColumn
wmanIf2BsSaChallengeMaxResends = _WmanIf2BsSaChallengeMaxResends_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 28),
    _WmanIf2BsSaChallengeMaxResends_Type()
)
wmanIf2BsSaChallengeMaxResends.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSaChallengeMaxResends.setStatus("current")


class _WmanIf2BsSaTekTimer_Type(Integer32):
    """Custom type wmanIf2BsSaTekTimer based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_WmanIf2BsSaTekTimer_Type.__name__ = "Integer32"
_WmanIf2BsSaTekTimer_Object = MibTableColumn
wmanIf2BsSaTekTimer = _WmanIf2BsSaTekTimer_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 29),
    _WmanIf2BsSaTekTimer_Type()
)
wmanIf2BsSaTekTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSaTekTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSaTekTimer.setUnits("milliseconds")


class _WmanIf2BsSaTekReqMaxResends_Type(Integer32):
    """Custom type wmanIf2BsSaTekReqMaxResends based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WmanIf2BsSaTekReqMaxResends_Type.__name__ = "Integer32"
_WmanIf2BsSaTekReqMaxResends_Object = MibTableColumn
wmanIf2BsSaTekReqMaxResends = _WmanIf2BsSaTekReqMaxResends_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 30),
    _WmanIf2BsSaTekReqMaxResends_Type()
)
wmanIf2BsSaTekReqMaxResends.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSaTekReqMaxResends.setStatus("current")


class _WmanIf2Bs2ndEapTimeout_Type(Integer32):
    """Custom type wmanIf2Bs2ndEapTimeout based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1000),
    )


_WmanIf2Bs2ndEapTimeout_Type.__name__ = "Integer32"
_WmanIf2Bs2ndEapTimeout_Object = MibTableColumn
wmanIf2Bs2ndEapTimeout = _WmanIf2Bs2ndEapTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 31),
    _WmanIf2Bs2ndEapTimeout_Type()
)
wmanIf2Bs2ndEapTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2Bs2ndEapTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2Bs2ndEapTimeout.setUnits("milliseconds")


class _WmanIf2BsEapCompleteResends_Type(Integer32):
    """Custom type wmanIf2BsEapCompleteResends based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WmanIf2BsEapCompleteResends_Type.__name__ = "Integer32"
_WmanIf2BsEapCompleteResends_Object = MibTableColumn
wmanIf2BsEapCompleteResends = _WmanIf2BsEapCompleteResends_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 32),
    _WmanIf2BsEapCompleteResends_Type()
)
wmanIf2BsEapCompleteResends.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsEapCompleteResends.setStatus("current")


class _WmanIf2BsInvitedRangRetries_Type(Integer32):
    """Custom type wmanIf2BsInvitedRangRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 65535),
    )


_WmanIf2BsInvitedRangRetries_Type.__name__ = "Integer32"
_WmanIf2BsInvitedRangRetries_Object = MibTableColumn
wmanIf2BsInvitedRangRetries = _WmanIf2BsInvitedRangRetries_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 33),
    _WmanIf2BsInvitedRangRetries_Type()
)
wmanIf2BsInvitedRangRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsInvitedRangRetries.setStatus("current")


class _WmanIf2BsDSxReqRetries_Type(Unsigned32):
    """Custom type wmanIf2BsDSxReqRetries based on Unsigned32"""
    defaultValue = 3


_WmanIf2BsDSxReqRetries_Type.__name__ = "Unsigned32"
_WmanIf2BsDSxReqRetries_Object = MibTableColumn
wmanIf2BsDSxReqRetries = _WmanIf2BsDSxReqRetries_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 34),
    _WmanIf2BsDSxReqRetries_Type()
)
wmanIf2BsDSxReqRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsDSxReqRetries.setStatus("current")


class _WmanIf2BsDSxRespRetries_Type(Unsigned32):
    """Custom type wmanIf2BsDSxRespRetries based on Unsigned32"""
    defaultValue = 3


_WmanIf2BsDSxRespRetries_Type.__name__ = "Unsigned32"
_WmanIf2BsDSxRespRetries_Object = MibTableColumn
wmanIf2BsDSxRespRetries = _WmanIf2BsDSxRespRetries_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 35),
    _WmanIf2BsDSxRespRetries_Type()
)
wmanIf2BsDSxRespRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsDSxRespRetries.setStatus("current")


class _WmanIf2BsT7Timeout_Type(Integer32):
    """Custom type wmanIf2BsT7Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WmanIf2BsT7Timeout_Type.__name__ = "Integer32"
_WmanIf2BsT7Timeout_Object = MibTableColumn
wmanIf2BsT7Timeout = _WmanIf2BsT7Timeout_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 36),
    _WmanIf2BsT7Timeout_Type()
)
wmanIf2BsT7Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsT7Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsT7Timeout.setUnits("milliseconds")


class _WmanIf2BsT8Timeout_Type(Integer32):
    """Custom type wmanIf2BsT8Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_WmanIf2BsT8Timeout_Type.__name__ = "Integer32"
_WmanIf2BsT8Timeout_Object = MibTableColumn
wmanIf2BsT8Timeout = _WmanIf2BsT8Timeout_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 37),
    _WmanIf2BsT8Timeout_Type()
)
wmanIf2BsT8Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsT8Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsT8Timeout.setUnits("milliseconds")


class _WmanIf2BsT10Timeout_Type(Integer32):
    """Custom type wmanIf2BsT10Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_WmanIf2BsT10Timeout_Type.__name__ = "Integer32"
_WmanIf2BsT10Timeout_Object = MibTableColumn
wmanIf2BsT10Timeout = _WmanIf2BsT10Timeout_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 38),
    _WmanIf2BsT10Timeout_Type()
)
wmanIf2BsT10Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsT10Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsT10Timeout.setUnits("milliseconds")


class _WmanIf2BsT22Timeout_Type(Integer32):
    """Custom type wmanIf2BsT22Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_WmanIf2BsT22Timeout_Type.__name__ = "Integer32"
_WmanIf2BsT22Timeout_Object = MibTableColumn
wmanIf2BsT22Timeout = _WmanIf2BsT22Timeout_Object(
    (1, 0, 8802, 16, 2, 1, 2, 2, 1, 39),
    _WmanIf2BsT22Timeout_Type()
)
wmanIf2BsT22Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsT22Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsT22Timeout.setUnits("milliseconds")
_WmanIf2BsSsReqCapabilitiesTable_Object = MibTable
wmanIf2BsSsReqCapabilitiesTable = _WmanIf2BsSsReqCapabilitiesTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapabilitiesTable.setStatus("current")
_WmanIf2BsSsReqCapabilitiesEntry_Object = MibTableRow
wmanIf2BsSsReqCapabilitiesEntry = _WmanIf2BsSsReqCapabilitiesEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapabilitiesEntry.setStatus("current")
_WmanIf2BsSsReqCapUplinkCidSupport_Type = WmanIf2NumOfCid
_WmanIf2BsSsReqCapUplinkCidSupport_Object = MibTableColumn
wmanIf2BsSsReqCapUplinkCidSupport = _WmanIf2BsSsReqCapUplinkCidSupport_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 1),
    _WmanIf2BsSsReqCapUplinkCidSupport_Type()
)
wmanIf2BsSsReqCapUplinkCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapUplinkCidSupport.setStatus("current")


class _WmanIf2BsSsReqCapDsxFlowControl_Type(WmanIf2MaxDsxFlowType):
    """Custom type wmanIf2BsSsReqCapDsxFlowControl based on WmanIf2MaxDsxFlowType"""
    defaultValue = 0


_WmanIf2BsSsReqCapDsxFlowControl_Type.__name__ = "WmanIf2MaxDsxFlowType"
_WmanIf2BsSsReqCapDsxFlowControl_Object = MibTableColumn
wmanIf2BsSsReqCapDsxFlowControl = _WmanIf2BsSsReqCapDsxFlowControl_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 2),
    _WmanIf2BsSsReqCapDsxFlowControl_Type()
)
wmanIf2BsSsReqCapDsxFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapDsxFlowControl.setStatus("current")


class _WmanIf2BsSsReqCapMcaFlowControl_Type(WmanIf2MaxMcaFlowType):
    """Custom type wmanIf2BsSsReqCapMcaFlowControl based on WmanIf2MaxMcaFlowType"""
    defaultValue = 0


_WmanIf2BsSsReqCapMcaFlowControl_Type.__name__ = "WmanIf2MaxMcaFlowType"
_WmanIf2BsSsReqCapMcaFlowControl_Object = MibTableColumn
wmanIf2BsSsReqCapMcaFlowControl = _WmanIf2BsSsReqCapMcaFlowControl_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 3),
    _WmanIf2BsSsReqCapMcaFlowControl_Type()
)
wmanIf2BsSsReqCapMcaFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapMcaFlowControl.setStatus("current")


class _WmanIf2BsSsReqCapMcpGroupCidSupport_Type(WmanIf2MaxMcpGroupCid):
    """Custom type wmanIf2BsSsReqCapMcpGroupCidSupport based on WmanIf2MaxMcpGroupCid"""
    defaultValue = 0


_WmanIf2BsSsReqCapMcpGroupCidSupport_Type.__name__ = "WmanIf2MaxMcpGroupCid"
_WmanIf2BsSsReqCapMcpGroupCidSupport_Object = MibTableColumn
wmanIf2BsSsReqCapMcpGroupCidSupport = _WmanIf2BsSsReqCapMcpGroupCidSupport_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 4),
    _WmanIf2BsSsReqCapMcpGroupCidSupport_Type()
)
wmanIf2BsSsReqCapMcpGroupCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapMcpGroupCidSupport.setStatus("current")


class _WmanIf2BsSsReqCapPkmFlowControl_Type(WmanIf2MaxPkmFlowType):
    """Custom type wmanIf2BsSsReqCapPkmFlowControl based on WmanIf2MaxPkmFlowType"""
    defaultValue = 0


_WmanIf2BsSsReqCapPkmFlowControl_Type.__name__ = "WmanIf2MaxPkmFlowType"
_WmanIf2BsSsReqCapPkmFlowControl_Object = MibTableColumn
wmanIf2BsSsReqCapPkmFlowControl = _WmanIf2BsSsReqCapPkmFlowControl_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 5),
    _WmanIf2BsSsReqCapPkmFlowControl_Type()
)
wmanIf2BsSsReqCapPkmFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapPkmFlowControl.setStatus("current")


class _WmanIf2BsSsReqCapMaxNumOfSupportedSA_Type(WmanIf2MaxNumOfSaType):
    """Custom type wmanIf2BsSsReqCapMaxNumOfSupportedSA based on WmanIf2MaxNumOfSaType"""
    defaultValue = 1


_WmanIf2BsSsReqCapMaxNumOfSupportedSA_Type.__name__ = "WmanIf2MaxNumOfSaType"
_WmanIf2BsSsReqCapMaxNumOfSupportedSA_Object = MibTableColumn
wmanIf2BsSsReqCapMaxNumOfSupportedSA = _WmanIf2BsSsReqCapMaxNumOfSupportedSA_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 6),
    _WmanIf2BsSsReqCapMaxNumOfSupportedSA_Type()
)
wmanIf2BsSsReqCapMaxNumOfSupportedSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapMaxNumOfSupportedSA.setStatus("current")


class _WmanIf2BsSsReqCapMaxNumOfClassifier_Type(WmanIf2MaxClassifiers):
    """Custom type wmanIf2BsSsReqCapMaxNumOfClassifier based on WmanIf2MaxClassifiers"""
    defaultValue = 0


_WmanIf2BsSsReqCapMaxNumOfClassifier_Type.__name__ = "WmanIf2MaxClassifiers"
_WmanIf2BsSsReqCapMaxNumOfClassifier_Object = MibTableColumn
wmanIf2BsSsReqCapMaxNumOfClassifier = _WmanIf2BsSsReqCapMaxNumOfClassifier_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 7),
    _WmanIf2BsSsReqCapMaxNumOfClassifier_Type()
)
wmanIf2BsSsReqCapMaxNumOfClassifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapMaxNumOfClassifier.setStatus("current")
_WmanIf2BsSsReqCapTtgTransitionGap_Type = WmanIf2SsTransitionGap
_WmanIf2BsSsReqCapTtgTransitionGap_Object = MibTableColumn
wmanIf2BsSsReqCapTtgTransitionGap = _WmanIf2BsSsReqCapTtgTransitionGap_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 8),
    _WmanIf2BsSsReqCapTtgTransitionGap_Type()
)
wmanIf2BsSsReqCapTtgTransitionGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapTtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapTtgTransitionGap.setUnits("microsecond")
_WmanIf2BsSsReqCapRtgTransitionGap_Type = WmanIf2SsTransitionGap
_WmanIf2BsSsReqCapRtgTransitionGap_Object = MibTableColumn
wmanIf2BsSsReqCapRtgTransitionGap = _WmanIf2BsSsReqCapRtgTransitionGap_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 9),
    _WmanIf2BsSsReqCapRtgTransitionGap_Type()
)
wmanIf2BsSsReqCapRtgTransitionGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapRtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapRtgTransitionGap.setUnits("microsecond")
_WmanIf2BsSsReqCapDownlinkCidSupport_Type = WmanIf2NumOfCid
_WmanIf2BsSsReqCapDownlinkCidSupport_Object = MibTableColumn
wmanIf2BsSsReqCapDownlinkCidSupport = _WmanIf2BsSsReqCapDownlinkCidSupport_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 10),
    _WmanIf2BsSsReqCapDownlinkCidSupport_Type()
)
wmanIf2BsSsReqCapDownlinkCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapDownlinkCidSupport.setStatus("current")
_WmanIf2BsSsReqCapMaxNumBurstToMs_Type = WmanIf2MaxNumBurstTx
_WmanIf2BsSsReqCapMaxNumBurstToMs_Object = MibTableColumn
wmanIf2BsSsReqCapMaxNumBurstToMs = _WmanIf2BsSsReqCapMaxNumBurstToMs_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 11),
    _WmanIf2BsSsReqCapMaxNumBurstToMs_Type()
)
wmanIf2BsSsReqCapMaxNumBurstToMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapMaxNumBurstToMs.setStatus("current")


class _WmanIf2BsSsReqCapMaxMacLevelDlFrame_Type(WmanIf2MaxMacLevel):
    """Custom type wmanIf2BsSsReqCapMaxMacLevelDlFrame based on WmanIf2MaxMacLevel"""
    defaultValue = 0


_WmanIf2BsSsReqCapMaxMacLevelDlFrame_Type.__name__ = "WmanIf2MaxMacLevel"
_WmanIf2BsSsReqCapMaxMacLevelDlFrame_Object = MibTableColumn
wmanIf2BsSsReqCapMaxMacLevelDlFrame = _WmanIf2BsSsReqCapMaxMacLevelDlFrame_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 12),
    _WmanIf2BsSsReqCapMaxMacLevelDlFrame_Type()
)
wmanIf2BsSsReqCapMaxMacLevelDlFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapMaxMacLevelDlFrame.setStatus("current")


class _WmanIf2BsSsReqCapMaxMacLevelUlFrame_Type(WmanIf2MaxMacLevel):
    """Custom type wmanIf2BsSsReqCapMaxMacLevelUlFrame based on WmanIf2MaxMacLevel"""
    defaultValue = 0


_WmanIf2BsSsReqCapMaxMacLevelUlFrame_Type.__name__ = "WmanIf2MaxMacLevel"
_WmanIf2BsSsReqCapMaxMacLevelUlFrame_Object = MibTableColumn
wmanIf2BsSsReqCapMaxMacLevelUlFrame = _WmanIf2BsSsReqCapMaxMacLevelUlFrame_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 13),
    _WmanIf2BsSsReqCapMaxMacLevelUlFrame_Type()
)
wmanIf2BsSsReqCapMaxMacLevelUlFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapMaxMacLevelUlFrame.setStatus("current")


class _WmanIf2BsSsReqCapPnWindowSize_Type(Integer32):
    """Custom type wmanIf2BsSsReqCapPnWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSsReqCapPnWindowSize_Type.__name__ = "Integer32"
_WmanIf2BsSsReqCapPnWindowSize_Object = MibTableColumn
wmanIf2BsSsReqCapPnWindowSize = _WmanIf2BsSsReqCapPnWindowSize_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 14),
    _WmanIf2BsSsReqCapPnWindowSize_Type()
)
wmanIf2BsSsReqCapPnWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapPnWindowSize.setStatus("current")
_WmanIf2BsSsOfdmReqCapLoopPwrControlSw_Type = Unsigned32
_WmanIf2BsSsOfdmReqCapLoopPwrControlSw_Object = MibTableColumn
wmanIf2BsSsOfdmReqCapLoopPwrControlSw = _WmanIf2BsSsOfdmReqCapLoopPwrControlSw_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 15),
    _WmanIf2BsSsOfdmReqCapLoopPwrControlSw_Type()
)
wmanIf2BsSsOfdmReqCapLoopPwrControlSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmReqCapLoopPwrControlSw.setStatus("current")
_WmanIf2BsSsOfdmaReqCapSdmaPilot_Type = WmanIf2SdmaPilotCap
_WmanIf2BsSsOfdmaReqCapSdmaPilot_Object = MibTableColumn
wmanIf2BsSsOfdmaReqCapSdmaPilot = _WmanIf2BsSsOfdmaReqCapSdmaPilot_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 16),
    _WmanIf2BsSsOfdmaReqCapSdmaPilot_Type()
)
wmanIf2BsSsOfdmaReqCapSdmaPilot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaReqCapSdmaPilot.setStatus("current")
_WmanIf2BsSsOfdmaReqCapNoUlHarqChannel_Type = WmanIf2OfdmaNoHarqChan
_WmanIf2BsSsOfdmaReqCapNoUlHarqChannel_Object = MibTableColumn
wmanIf2BsSsOfdmaReqCapNoUlHarqChannel = _WmanIf2BsSsOfdmaReqCapNoUlHarqChannel_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 17),
    _WmanIf2BsSsOfdmaReqCapNoUlHarqChannel_Type()
)
wmanIf2BsSsOfdmaReqCapNoUlHarqChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaReqCapNoUlHarqChannel.setStatus("current")
_WmanIf2BsSsOfdmaReqCapNoDlHarqChannel_Type = WmanIf2OfdmaNoHarqChan
_WmanIf2BsSsOfdmaReqCapNoDlHarqChannel_Object = MibTableColumn
wmanIf2BsSsOfdmaReqCapNoDlHarqChannel = _WmanIf2BsSsOfdmaReqCapNoDlHarqChannel_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 18),
    _WmanIf2BsSsOfdmaReqCapNoDlHarqChannel_Type()
)
wmanIf2BsSsOfdmaReqCapNoDlHarqChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaReqCapNoDlHarqChannel.setStatus("current")
_WmanIf2BsSsReqCapOptionsBasic_Type = WmanIf2BasicCapOptions
_WmanIf2BsSsReqCapOptionsBasic_Object = MibTableColumn
wmanIf2BsSsReqCapOptionsBasic = _WmanIf2BsSsReqCapOptionsBasic_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 19),
    _WmanIf2BsSsReqCapOptionsBasic_Type()
)
wmanIf2BsSsReqCapOptionsBasic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapOptionsBasic.setStatus("current")
_WmanIf2BsSsReqCapOptionsOfdm_Type = WmanIf2OfdmCapOptions
_WmanIf2BsSsReqCapOptionsOfdm_Object = MibTableColumn
wmanIf2BsSsReqCapOptionsOfdm = _WmanIf2BsSsReqCapOptionsOfdm_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 20),
    _WmanIf2BsSsReqCapOptionsOfdm_Type()
)
wmanIf2BsSsReqCapOptionsOfdm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapOptionsOfdm.setStatus("current")
_WmanIf2BsSsReqCapOptionsOfdma_Type = WmanIf2OfdmaCapOptions
_WmanIf2BsSsReqCapOptionsOfdma_Object = MibTableColumn
wmanIf2BsSsReqCapOptionsOfdma = _WmanIf2BsSsReqCapOptionsOfdma_Object(
    (1, 0, 8802, 16, 2, 1, 2, 3, 1, 21),
    _WmanIf2BsSsReqCapOptionsOfdma_Type()
)
wmanIf2BsSsReqCapOptionsOfdma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsReqCapOptionsOfdma.setStatus("current")
_WmanIf2BsSsRspCapabilitiesTable_Object = MibTable
wmanIf2BsSsRspCapabilitiesTable = _WmanIf2BsSsRspCapabilitiesTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapabilitiesTable.setStatus("current")
_WmanIf2BsSsRspCapabilitiesEntry_Object = MibTableRow
wmanIf2BsSsRspCapabilitiesEntry = _WmanIf2BsSsRspCapabilitiesEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapabilitiesEntry.setStatus("current")
_WmanIf2BsSsRspCapUplinkCidSupport_Type = WmanIf2NumOfCid
_WmanIf2BsSsRspCapUplinkCidSupport_Object = MibTableColumn
wmanIf2BsSsRspCapUplinkCidSupport = _WmanIf2BsSsRspCapUplinkCidSupport_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 1),
    _WmanIf2BsSsRspCapUplinkCidSupport_Type()
)
wmanIf2BsSsRspCapUplinkCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapUplinkCidSupport.setStatus("current")
_WmanIf2BsSsRspCapDsxFlowControl_Type = WmanIf2MaxDsxFlowType
_WmanIf2BsSsRspCapDsxFlowControl_Object = MibTableColumn
wmanIf2BsSsRspCapDsxFlowControl = _WmanIf2BsSsRspCapDsxFlowControl_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 2),
    _WmanIf2BsSsRspCapDsxFlowControl_Type()
)
wmanIf2BsSsRspCapDsxFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapDsxFlowControl.setStatus("current")


class _WmanIf2BsSsRspCapMcaFlowControl_Type(WmanIf2MaxMcaFlowType):
    """Custom type wmanIf2BsSsRspCapMcaFlowControl based on WmanIf2MaxMcaFlowType"""
    defaultValue = 0


_WmanIf2BsSsRspCapMcaFlowControl_Type.__name__ = "WmanIf2MaxMcaFlowType"
_WmanIf2BsSsRspCapMcaFlowControl_Object = MibTableColumn
wmanIf2BsSsRspCapMcaFlowControl = _WmanIf2BsSsRspCapMcaFlowControl_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 3),
    _WmanIf2BsSsRspCapMcaFlowControl_Type()
)
wmanIf2BsSsRspCapMcaFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapMcaFlowControl.setStatus("current")


class _WmanIf2BsSsRspCapMcpGroupCidSupport_Type(WmanIf2MaxMcpGroupCid):
    """Custom type wmanIf2BsSsRspCapMcpGroupCidSupport based on WmanIf2MaxMcpGroupCid"""
    defaultValue = 0


_WmanIf2BsSsRspCapMcpGroupCidSupport_Type.__name__ = "WmanIf2MaxMcpGroupCid"
_WmanIf2BsSsRspCapMcpGroupCidSupport_Object = MibTableColumn
wmanIf2BsSsRspCapMcpGroupCidSupport = _WmanIf2BsSsRspCapMcpGroupCidSupport_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 4),
    _WmanIf2BsSsRspCapMcpGroupCidSupport_Type()
)
wmanIf2BsSsRspCapMcpGroupCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapMcpGroupCidSupport.setStatus("current")


class _WmanIf2BsSsRspCapPkmFlowControl_Type(WmanIf2MaxPkmFlowType):
    """Custom type wmanIf2BsSsRspCapPkmFlowControl based on WmanIf2MaxPkmFlowType"""
    defaultValue = 0


_WmanIf2BsSsRspCapPkmFlowControl_Type.__name__ = "WmanIf2MaxPkmFlowType"
_WmanIf2BsSsRspCapPkmFlowControl_Object = MibTableColumn
wmanIf2BsSsRspCapPkmFlowControl = _WmanIf2BsSsRspCapPkmFlowControl_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 5),
    _WmanIf2BsSsRspCapPkmFlowControl_Type()
)
wmanIf2BsSsRspCapPkmFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapPkmFlowControl.setStatus("current")


class _WmanIf2BsSsRspCapMaxNumOfSupportedSA_Type(WmanIf2MaxNumOfSaType):
    """Custom type wmanIf2BsSsRspCapMaxNumOfSupportedSA based on WmanIf2MaxNumOfSaType"""
    defaultValue = 1


_WmanIf2BsSsRspCapMaxNumOfSupportedSA_Type.__name__ = "WmanIf2MaxNumOfSaType"
_WmanIf2BsSsRspCapMaxNumOfSupportedSA_Object = MibTableColumn
wmanIf2BsSsRspCapMaxNumOfSupportedSA = _WmanIf2BsSsRspCapMaxNumOfSupportedSA_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 6),
    _WmanIf2BsSsRspCapMaxNumOfSupportedSA_Type()
)
wmanIf2BsSsRspCapMaxNumOfSupportedSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapMaxNumOfSupportedSA.setStatus("current")


class _WmanIf2BsSsRspCapMaxNumOfClassifier_Type(WmanIf2MaxClassifiers):
    """Custom type wmanIf2BsSsRspCapMaxNumOfClassifier based on WmanIf2MaxClassifiers"""
    defaultValue = 0


_WmanIf2BsSsRspCapMaxNumOfClassifier_Type.__name__ = "WmanIf2MaxClassifiers"
_WmanIf2BsSsRspCapMaxNumOfClassifier_Object = MibTableColumn
wmanIf2BsSsRspCapMaxNumOfClassifier = _WmanIf2BsSsRspCapMaxNumOfClassifier_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 7),
    _WmanIf2BsSsRspCapMaxNumOfClassifier_Type()
)
wmanIf2BsSsRspCapMaxNumOfClassifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapMaxNumOfClassifier.setStatus("current")
_WmanIf2BsSsRspCapTtgTransitionGap_Type = WmanIf2SsTransitionGap
_WmanIf2BsSsRspCapTtgTransitionGap_Object = MibTableColumn
wmanIf2BsSsRspCapTtgTransitionGap = _WmanIf2BsSsRspCapTtgTransitionGap_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 8),
    _WmanIf2BsSsRspCapTtgTransitionGap_Type()
)
wmanIf2BsSsRspCapTtgTransitionGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapTtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapTtgTransitionGap.setUnits("microsecond")
_WmanIf2BsSsRspCapRtgTransitionGap_Type = WmanIf2SsTransitionGap
_WmanIf2BsSsRspCapRtgTransitionGap_Object = MibTableColumn
wmanIf2BsSsRspCapRtgTransitionGap = _WmanIf2BsSsRspCapRtgTransitionGap_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 9),
    _WmanIf2BsSsRspCapRtgTransitionGap_Type()
)
wmanIf2BsSsRspCapRtgTransitionGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapRtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapRtgTransitionGap.setUnits("microsecond")
_WmanIf2BsSsRspCapDownlinkCidSupport_Type = WmanIf2NumOfCid
_WmanIf2BsSsRspCapDownlinkCidSupport_Object = MibTableColumn
wmanIf2BsSsRspCapDownlinkCidSupport = _WmanIf2BsSsRspCapDownlinkCidSupport_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 10),
    _WmanIf2BsSsRspCapDownlinkCidSupport_Type()
)
wmanIf2BsSsRspCapDownlinkCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapDownlinkCidSupport.setStatus("current")


class _WmanIf2BsSsRspCapMaxNumBurstToMs_Type(Integer32):
    """Custom type wmanIf2BsSsRspCapMaxNumBurstToMs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WmanIf2BsSsRspCapMaxNumBurstToMs_Type.__name__ = "Integer32"
_WmanIf2BsSsRspCapMaxNumBurstToMs_Object = MibTableColumn
wmanIf2BsSsRspCapMaxNumBurstToMs = _WmanIf2BsSsRspCapMaxNumBurstToMs_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 11),
    _WmanIf2BsSsRspCapMaxNumBurstToMs_Type()
)
wmanIf2BsSsRspCapMaxNumBurstToMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapMaxNumBurstToMs.setStatus("current")


class _WmanIf2BsSsRspCapMaxMacLevelDlFrame_Type(WmanIf2MaxMacLevel):
    """Custom type wmanIf2BsSsRspCapMaxMacLevelDlFrame based on WmanIf2MaxMacLevel"""
    defaultValue = 0


_WmanIf2BsSsRspCapMaxMacLevelDlFrame_Type.__name__ = "WmanIf2MaxMacLevel"
_WmanIf2BsSsRspCapMaxMacLevelDlFrame_Object = MibTableColumn
wmanIf2BsSsRspCapMaxMacLevelDlFrame = _WmanIf2BsSsRspCapMaxMacLevelDlFrame_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 12),
    _WmanIf2BsSsRspCapMaxMacLevelDlFrame_Type()
)
wmanIf2BsSsRspCapMaxMacLevelDlFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapMaxMacLevelDlFrame.setStatus("current")


class _WmanIf2BsSsRspCapMaxMacLevelUlFrame_Type(WmanIf2MaxMacLevel):
    """Custom type wmanIf2BsSsRspCapMaxMacLevelUlFrame based on WmanIf2MaxMacLevel"""
    defaultValue = 0


_WmanIf2BsSsRspCapMaxMacLevelUlFrame_Type.__name__ = "WmanIf2MaxMacLevel"
_WmanIf2BsSsRspCapMaxMacLevelUlFrame_Object = MibTableColumn
wmanIf2BsSsRspCapMaxMacLevelUlFrame = _WmanIf2BsSsRspCapMaxMacLevelUlFrame_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 13),
    _WmanIf2BsSsRspCapMaxMacLevelUlFrame_Type()
)
wmanIf2BsSsRspCapMaxMacLevelUlFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapMaxMacLevelUlFrame.setStatus("current")


class _WmanIf2BsSsRspCapNumOfProvisionedSf_Type(Unsigned32):
    """Custom type wmanIf2BsSsRspCapNumOfProvisionedSf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsSsRspCapNumOfProvisionedSf_Type.__name__ = "Unsigned32"
_WmanIf2BsSsRspCapNumOfProvisionedSf_Object = MibTableColumn
wmanIf2BsSsRspCapNumOfProvisionedSf = _WmanIf2BsSsRspCapNumOfProvisionedSf_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 14),
    _WmanIf2BsSsRspCapNumOfProvisionedSf_Type()
)
wmanIf2BsSsRspCapNumOfProvisionedSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapNumOfProvisionedSf.setStatus("current")


class _WmanIf2BsSsRspCapPnWindowSize_Type(Integer32):
    """Custom type wmanIf2BsSsRspCapPnWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSsRspCapPnWindowSize_Type.__name__ = "Integer32"
_WmanIf2BsSsRspCapPnWindowSize_Object = MibTableColumn
wmanIf2BsSsRspCapPnWindowSize = _WmanIf2BsSsRspCapPnWindowSize_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 15),
    _WmanIf2BsSsRspCapPnWindowSize_Type()
)
wmanIf2BsSsRspCapPnWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapPnWindowSize.setStatus("current")
_WmanIf2BsSsOfdmRspCapLoopPwrControlSw_Type = Unsigned32
_WmanIf2BsSsOfdmRspCapLoopPwrControlSw_Object = MibTableColumn
wmanIf2BsSsOfdmRspCapLoopPwrControlSw = _WmanIf2BsSsOfdmRspCapLoopPwrControlSw_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 16),
    _WmanIf2BsSsOfdmRspCapLoopPwrControlSw_Type()
)
wmanIf2BsSsOfdmRspCapLoopPwrControlSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmRspCapLoopPwrControlSw.setStatus("current")
_WmanIf2BsSsOfdmaRspCapSdmaPilot_Type = WmanIf2SdmaPilotCap
_WmanIf2BsSsOfdmaRspCapSdmaPilot_Object = MibTableColumn
wmanIf2BsSsOfdmaRspCapSdmaPilot = _WmanIf2BsSsOfdmaRspCapSdmaPilot_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 17),
    _WmanIf2BsSsOfdmaRspCapSdmaPilot_Type()
)
wmanIf2BsSsOfdmaRspCapSdmaPilot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaRspCapSdmaPilot.setStatus("current")
_WmanIf2BsSsOfdmaRspCapNoUlHarqChannel_Type = WmanIf2OfdmaNoHarqChan
_WmanIf2BsSsOfdmaRspCapNoUlHarqChannel_Object = MibTableColumn
wmanIf2BsSsOfdmaRspCapNoUlHarqChannel = _WmanIf2BsSsOfdmaRspCapNoUlHarqChannel_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 18),
    _WmanIf2BsSsOfdmaRspCapNoUlHarqChannel_Type()
)
wmanIf2BsSsOfdmaRspCapNoUlHarqChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaRspCapNoUlHarqChannel.setStatus("current")
_WmanIf2BsSsOfdmaRspCapNoDlHarqChannel_Type = WmanIf2OfdmaNoHarqChan
_WmanIf2BsSsOfdmaRspCapNoDlHarqChannel_Object = MibTableColumn
wmanIf2BsSsOfdmaRspCapNoDlHarqChannel = _WmanIf2BsSsOfdmaRspCapNoDlHarqChannel_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 19),
    _WmanIf2BsSsOfdmaRspCapNoDlHarqChannel_Type()
)
wmanIf2BsSsOfdmaRspCapNoDlHarqChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsOfdmaRspCapNoDlHarqChannel.setStatus("current")
_WmanIf2BsSsRspCapOptionsBasic_Type = WmanIf2BasicCapOptions
_WmanIf2BsSsRspCapOptionsBasic_Object = MibTableColumn
wmanIf2BsSsRspCapOptionsBasic = _WmanIf2BsSsRspCapOptionsBasic_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 20),
    _WmanIf2BsSsRspCapOptionsBasic_Type()
)
wmanIf2BsSsRspCapOptionsBasic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapOptionsBasic.setStatus("current")
_WmanIf2BsSsRspCapOptionsOfdm_Type = WmanIf2OfdmCapOptions
_WmanIf2BsSsRspCapOptionsOfdm_Object = MibTableColumn
wmanIf2BsSsRspCapOptionsOfdm = _WmanIf2BsSsRspCapOptionsOfdm_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 21),
    _WmanIf2BsSsRspCapOptionsOfdm_Type()
)
wmanIf2BsSsRspCapOptionsOfdm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapOptionsOfdm.setStatus("current")
_WmanIf2BsSsRspCapOptionsOfdma_Type = WmanIf2OfdmaCapOptions
_WmanIf2BsSsRspCapOptionsOfdma_Object = MibTableColumn
wmanIf2BsSsRspCapOptionsOfdma = _WmanIf2BsSsRspCapOptionsOfdma_Object(
    (1, 0, 8802, 16, 2, 1, 2, 4, 1, 22),
    _WmanIf2BsSsRspCapOptionsOfdma_Type()
)
wmanIf2BsSsRspCapOptionsOfdma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRspCapOptionsOfdma.setStatus("current")
_WmanIf2BsBasicCapabilitiesTable_Object = MibTable
wmanIf2BsBasicCapabilitiesTable = _WmanIf2BsBasicCapabilitiesTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    wmanIf2BsBasicCapabilitiesTable.setStatus("current")
_WmanIf2BsBasicCapabilitiesEntry_Object = MibTableRow
wmanIf2BsBasicCapabilitiesEntry = _WmanIf2BsBasicCapabilitiesEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1)
)
wmanIf2BsBasicCapabilitiesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsBasicCapabilitiesEntry.setStatus("current")
_WmanIf2BsCapUplinkCidSupport_Type = WmanIf2NumOfCid
_WmanIf2BsCapUplinkCidSupport_Object = MibTableColumn
wmanIf2BsCapUplinkCidSupport = _WmanIf2BsCapUplinkCidSupport_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 1),
    _WmanIf2BsCapUplinkCidSupport_Type()
)
wmanIf2BsCapUplinkCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapUplinkCidSupport.setStatus("current")


class _WmanIf2BsCapDsxFlowControl_Type(WmanIf2MaxDsxFlowType):
    """Custom type wmanIf2BsCapDsxFlowControl based on WmanIf2MaxDsxFlowType"""
    defaultValue = 0


_WmanIf2BsCapDsxFlowControl_Type.__name__ = "WmanIf2MaxDsxFlowType"
_WmanIf2BsCapDsxFlowControl_Object = MibTableColumn
wmanIf2BsCapDsxFlowControl = _WmanIf2BsCapDsxFlowControl_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 2),
    _WmanIf2BsCapDsxFlowControl_Type()
)
wmanIf2BsCapDsxFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapDsxFlowControl.setStatus("current")


class _WmanIf2BsCapMcaFlowControl_Type(WmanIf2MaxMcaFlowType):
    """Custom type wmanIf2BsCapMcaFlowControl based on WmanIf2MaxMcaFlowType"""
    defaultValue = 0


_WmanIf2BsCapMcaFlowControl_Type.__name__ = "WmanIf2MaxMcaFlowType"
_WmanIf2BsCapMcaFlowControl_Object = MibTableColumn
wmanIf2BsCapMcaFlowControl = _WmanIf2BsCapMcaFlowControl_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 3),
    _WmanIf2BsCapMcaFlowControl_Type()
)
wmanIf2BsCapMcaFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapMcaFlowControl.setStatus("current")


class _WmanIf2BsCapMcpGroupCidSupport_Type(WmanIf2MaxMcpGroupCid):
    """Custom type wmanIf2BsCapMcpGroupCidSupport based on WmanIf2MaxMcpGroupCid"""
    defaultValue = 0


_WmanIf2BsCapMcpGroupCidSupport_Type.__name__ = "WmanIf2MaxMcpGroupCid"
_WmanIf2BsCapMcpGroupCidSupport_Object = MibTableColumn
wmanIf2BsCapMcpGroupCidSupport = _WmanIf2BsCapMcpGroupCidSupport_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 4),
    _WmanIf2BsCapMcpGroupCidSupport_Type()
)
wmanIf2BsCapMcpGroupCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapMcpGroupCidSupport.setStatus("current")


class _WmanIf2BsCapPkmFlowControl_Type(WmanIf2MaxPkmFlowType):
    """Custom type wmanIf2BsCapPkmFlowControl based on WmanIf2MaxPkmFlowType"""
    defaultValue = 0


_WmanIf2BsCapPkmFlowControl_Type.__name__ = "WmanIf2MaxPkmFlowType"
_WmanIf2BsCapPkmFlowControl_Object = MibTableColumn
wmanIf2BsCapPkmFlowControl = _WmanIf2BsCapPkmFlowControl_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 5),
    _WmanIf2BsCapPkmFlowControl_Type()
)
wmanIf2BsCapPkmFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapPkmFlowControl.setStatus("current")


class _WmanIf2BsCapMaxNumOfSupportedSA_Type(WmanIf2MaxNumOfSaType):
    """Custom type wmanIf2BsCapMaxNumOfSupportedSA based on WmanIf2MaxNumOfSaType"""
    defaultValue = 1


_WmanIf2BsCapMaxNumOfSupportedSA_Type.__name__ = "WmanIf2MaxNumOfSaType"
_WmanIf2BsCapMaxNumOfSupportedSA_Object = MibTableColumn
wmanIf2BsCapMaxNumOfSupportedSA = _WmanIf2BsCapMaxNumOfSupportedSA_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 6),
    _WmanIf2BsCapMaxNumOfSupportedSA_Type()
)
wmanIf2BsCapMaxNumOfSupportedSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapMaxNumOfSupportedSA.setStatus("current")


class _WmanIf2BsCapMaxNumOfClassifier_Type(WmanIf2MaxClassifiers):
    """Custom type wmanIf2BsCapMaxNumOfClassifier based on WmanIf2MaxClassifiers"""
    defaultValue = 0


_WmanIf2BsCapMaxNumOfClassifier_Type.__name__ = "WmanIf2MaxClassifiers"
_WmanIf2BsCapMaxNumOfClassifier_Object = MibTableColumn
wmanIf2BsCapMaxNumOfClassifier = _WmanIf2BsCapMaxNumOfClassifier_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 7),
    _WmanIf2BsCapMaxNumOfClassifier_Type()
)
wmanIf2BsCapMaxNumOfClassifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapMaxNumOfClassifier.setStatus("current")
_WmanIf2BsCapTtgTransitionGap_Type = WmanIf2SsTransitionGap
_WmanIf2BsCapTtgTransitionGap_Object = MibTableColumn
wmanIf2BsCapTtgTransitionGap = _WmanIf2BsCapTtgTransitionGap_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 8),
    _WmanIf2BsCapTtgTransitionGap_Type()
)
wmanIf2BsCapTtgTransitionGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapTtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsCapTtgTransitionGap.setUnits("microsecond")
_WmanIf2BsCapRtgTransitionGap_Type = WmanIf2SsTransitionGap
_WmanIf2BsCapRtgTransitionGap_Object = MibTableColumn
wmanIf2BsCapRtgTransitionGap = _WmanIf2BsCapRtgTransitionGap_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 9),
    _WmanIf2BsCapRtgTransitionGap_Type()
)
wmanIf2BsCapRtgTransitionGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapRtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsCapRtgTransitionGap.setUnits("microsecond")
_WmanIf2BsCapDownlinkCidSupport_Type = WmanIf2NumOfCid
_WmanIf2BsCapDownlinkCidSupport_Object = MibTableColumn
wmanIf2BsCapDownlinkCidSupport = _WmanIf2BsCapDownlinkCidSupport_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 10),
    _WmanIf2BsCapDownlinkCidSupport_Type()
)
wmanIf2BsCapDownlinkCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapDownlinkCidSupport.setStatus("current")


class _WmanIf2BsCapMaxNumBurstToMs_Type(Integer32):
    """Custom type wmanIf2BsCapMaxNumBurstToMs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WmanIf2BsCapMaxNumBurstToMs_Type.__name__ = "Integer32"
_WmanIf2BsCapMaxNumBurstToMs_Object = MibTableColumn
wmanIf2BsCapMaxNumBurstToMs = _WmanIf2BsCapMaxNumBurstToMs_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 11),
    _WmanIf2BsCapMaxNumBurstToMs_Type()
)
wmanIf2BsCapMaxNumBurstToMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapMaxNumBurstToMs.setStatus("current")


class _WmanIf2BsCapMaxMacLevelDlFrame_Type(WmanIf2MaxMacLevel):
    """Custom type wmanIf2BsCapMaxMacLevelDlFrame based on WmanIf2MaxMacLevel"""
    defaultValue = 0


_WmanIf2BsCapMaxMacLevelDlFrame_Type.__name__ = "WmanIf2MaxMacLevel"
_WmanIf2BsCapMaxMacLevelDlFrame_Object = MibTableColumn
wmanIf2BsCapMaxMacLevelDlFrame = _WmanIf2BsCapMaxMacLevelDlFrame_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 12),
    _WmanIf2BsCapMaxMacLevelDlFrame_Type()
)
wmanIf2BsCapMaxMacLevelDlFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapMaxMacLevelDlFrame.setStatus("current")


class _WmanIf2BsCapMaxMacLevelUlFrame_Type(WmanIf2MaxMacLevel):
    """Custom type wmanIf2BsCapMaxMacLevelUlFrame based on WmanIf2MaxMacLevel"""
    defaultValue = 0


_WmanIf2BsCapMaxMacLevelUlFrame_Type.__name__ = "WmanIf2MaxMacLevel"
_WmanIf2BsCapMaxMacLevelUlFrame_Object = MibTableColumn
wmanIf2BsCapMaxMacLevelUlFrame = _WmanIf2BsCapMaxMacLevelUlFrame_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 13),
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
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 14),
    _WmanIf2BsCapNumOfProvisionedSf_Type()
)
wmanIf2BsCapNumOfProvisionedSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapNumOfProvisionedSf.setStatus("current")


class _WmanIf2BsCapPnWindowSize_Type(Integer32):
    """Custom type wmanIf2BsCapPnWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsCapPnWindowSize_Type.__name__ = "Integer32"
_WmanIf2BsCapPnWindowSize_Object = MibTableColumn
wmanIf2BsCapPnWindowSize = _WmanIf2BsCapPnWindowSize_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 15),
    _WmanIf2BsCapPnWindowSize_Type()
)
wmanIf2BsCapPnWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapPnWindowSize.setStatus("current")
_WmanIf2BsOfdmCapLoopPwrControlSw_Type = Unsigned32
_WmanIf2BsOfdmCapLoopPwrControlSw_Object = MibTableColumn
wmanIf2BsOfdmCapLoopPwrControlSw = _WmanIf2BsOfdmCapLoopPwrControlSw_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 16),
    _WmanIf2BsOfdmCapLoopPwrControlSw_Type()
)
wmanIf2BsOfdmCapLoopPwrControlSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmCapLoopPwrControlSw.setStatus("current")
_WmanIf2BsOfdmaCapSdmaPilot_Type = WmanIf2SdmaPilotCap
_WmanIf2BsOfdmaCapSdmaPilot_Object = MibTableColumn
wmanIf2BsOfdmaCapSdmaPilot = _WmanIf2BsOfdmaCapSdmaPilot_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 17),
    _WmanIf2BsOfdmaCapSdmaPilot_Type()
)
wmanIf2BsOfdmaCapSdmaPilot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapSdmaPilot.setStatus("current")
_WmanIf2BsOfdmaCapNoUlHarqChannel_Type = WmanIf2OfdmaNoHarqChan
_WmanIf2BsOfdmaCapNoUlHarqChannel_Object = MibTableColumn
wmanIf2BsOfdmaCapNoUlHarqChannel = _WmanIf2BsOfdmaCapNoUlHarqChannel_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 18),
    _WmanIf2BsOfdmaCapNoUlHarqChannel_Type()
)
wmanIf2BsOfdmaCapNoUlHarqChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapNoUlHarqChannel.setStatus("current")
_WmanIf2BsOfdmaCapNoDlHarqChannel_Type = WmanIf2OfdmaNoHarqChan
_WmanIf2BsOfdmaCapNoDlHarqChannel_Object = MibTableColumn
wmanIf2BsOfdmaCapNoDlHarqChannel = _WmanIf2BsOfdmaCapNoDlHarqChannel_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 19),
    _WmanIf2BsOfdmaCapNoDlHarqChannel_Type()
)
wmanIf2BsOfdmaCapNoDlHarqChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapNoDlHarqChannel.setStatus("current")
_WmanIf2BsCapOptionsBasic_Type = WmanIf2BasicCapOptions
_WmanIf2BsCapOptionsBasic_Object = MibTableColumn
wmanIf2BsCapOptionsBasic = _WmanIf2BsCapOptionsBasic_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 20),
    _WmanIf2BsCapOptionsBasic_Type()
)
wmanIf2BsCapOptionsBasic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapOptionsBasic.setStatus("current")
_WmanIf2BsCapOptionsOfdm_Type = WmanIf2OfdmCapOptions
_WmanIf2BsCapOptionsOfdm_Object = MibTableColumn
wmanIf2BsCapOptionsOfdm = _WmanIf2BsCapOptionsOfdm_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 21),
    _WmanIf2BsCapOptionsOfdm_Type()
)
wmanIf2BsCapOptionsOfdm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapOptionsOfdm.setStatus("current")
_WmanIf2BsCapOptionsOfdma_Type = WmanIf2OfdmaCapOptions
_WmanIf2BsCapOptionsOfdma_Object = MibTableColumn
wmanIf2BsCapOptionsOfdma = _WmanIf2BsCapOptionsOfdma_Object(
    (1, 0, 8802, 16, 2, 1, 2, 5, 1, 22),
    _WmanIf2BsCapOptionsOfdma_Type()
)
wmanIf2BsCapOptionsOfdma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapOptionsOfdma.setStatus("current")
_WmanIf2BsCapabilitiesConfigTable_Object = MibTable
wmanIf2BsCapabilitiesConfigTable = _WmanIf2BsCapabilitiesConfigTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    wmanIf2BsCapabilitiesConfigTable.setStatus("current")
_WmanIf2BsCapabilitiesConfigEntry_Object = MibTableRow
wmanIf2BsCapabilitiesConfigEntry = _WmanIf2BsCapabilitiesConfigEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1)
)
wmanIf2BsCapabilitiesConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsCapabilitiesConfigEntry.setStatus("current")
_WmanIf2BsCapCfgUplinkCidSupport_Type = WmanIf2NumOfCid
_WmanIf2BsCapCfgUplinkCidSupport_Object = MibTableColumn
wmanIf2BsCapCfgUplinkCidSupport = _WmanIf2BsCapCfgUplinkCidSupport_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 1),
    _WmanIf2BsCapCfgUplinkCidSupport_Type()
)
wmanIf2BsCapCfgUplinkCidSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgUplinkCidSupport.setStatus("current")


class _WmanIf2BsCapCfgDsxFlowControl_Type(WmanIf2MaxDsxFlowType):
    """Custom type wmanIf2BsCapCfgDsxFlowControl based on WmanIf2MaxDsxFlowType"""
    defaultValue = 0


_WmanIf2BsCapCfgDsxFlowControl_Type.__name__ = "WmanIf2MaxDsxFlowType"
_WmanIf2BsCapCfgDsxFlowControl_Object = MibTableColumn
wmanIf2BsCapCfgDsxFlowControl = _WmanIf2BsCapCfgDsxFlowControl_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 2),
    _WmanIf2BsCapCfgDsxFlowControl_Type()
)
wmanIf2BsCapCfgDsxFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgDsxFlowControl.setStatus("current")


class _WmanIf2BsCapCfgMcaFlowControl_Type(WmanIf2MaxMcaFlowType):
    """Custom type wmanIf2BsCapCfgMcaFlowControl based on WmanIf2MaxMcaFlowType"""
    defaultValue = 0


_WmanIf2BsCapCfgMcaFlowControl_Type.__name__ = "WmanIf2MaxMcaFlowType"
_WmanIf2BsCapCfgMcaFlowControl_Object = MibTableColumn
wmanIf2BsCapCfgMcaFlowControl = _WmanIf2BsCapCfgMcaFlowControl_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 3),
    _WmanIf2BsCapCfgMcaFlowControl_Type()
)
wmanIf2BsCapCfgMcaFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgMcaFlowControl.setStatus("current")


class _WmanIf2BsCapCfgMcpGroupCidSupport_Type(WmanIf2MaxMcpGroupCid):
    """Custom type wmanIf2BsCapCfgMcpGroupCidSupport based on WmanIf2MaxMcpGroupCid"""
    defaultValue = 0


_WmanIf2BsCapCfgMcpGroupCidSupport_Type.__name__ = "WmanIf2MaxMcpGroupCid"
_WmanIf2BsCapCfgMcpGroupCidSupport_Object = MibTableColumn
wmanIf2BsCapCfgMcpGroupCidSupport = _WmanIf2BsCapCfgMcpGroupCidSupport_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 4),
    _WmanIf2BsCapCfgMcpGroupCidSupport_Type()
)
wmanIf2BsCapCfgMcpGroupCidSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgMcpGroupCidSupport.setStatus("current")


class _WmanIf2BsCapCfgPkmFlowControl_Type(WmanIf2MaxPkmFlowType):
    """Custom type wmanIf2BsCapCfgPkmFlowControl based on WmanIf2MaxPkmFlowType"""
    defaultValue = 0


_WmanIf2BsCapCfgPkmFlowControl_Type.__name__ = "WmanIf2MaxPkmFlowType"
_WmanIf2BsCapCfgPkmFlowControl_Object = MibTableColumn
wmanIf2BsCapCfgPkmFlowControl = _WmanIf2BsCapCfgPkmFlowControl_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 5),
    _WmanIf2BsCapCfgPkmFlowControl_Type()
)
wmanIf2BsCapCfgPkmFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgPkmFlowControl.setStatus("current")


class _WmanIf2BsCapCfgMaxNumOfSupportedSA_Type(WmanIf2MaxNumOfSaType):
    """Custom type wmanIf2BsCapCfgMaxNumOfSupportedSA based on WmanIf2MaxNumOfSaType"""
    defaultValue = 1


_WmanIf2BsCapCfgMaxNumOfSupportedSA_Type.__name__ = "WmanIf2MaxNumOfSaType"
_WmanIf2BsCapCfgMaxNumOfSupportedSA_Object = MibTableColumn
wmanIf2BsCapCfgMaxNumOfSupportedSA = _WmanIf2BsCapCfgMaxNumOfSupportedSA_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 6),
    _WmanIf2BsCapCfgMaxNumOfSupportedSA_Type()
)
wmanIf2BsCapCfgMaxNumOfSupportedSA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgMaxNumOfSupportedSA.setStatus("current")


class _WmanIf2BsCapCfgMaxNumOfClassifier_Type(WmanIf2MaxClassifiers):
    """Custom type wmanIf2BsCapCfgMaxNumOfClassifier based on WmanIf2MaxClassifiers"""
    defaultValue = 0


_WmanIf2BsCapCfgMaxNumOfClassifier_Type.__name__ = "WmanIf2MaxClassifiers"
_WmanIf2BsCapCfgMaxNumOfClassifier_Object = MibTableColumn
wmanIf2BsCapCfgMaxNumOfClassifier = _WmanIf2BsCapCfgMaxNumOfClassifier_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 7),
    _WmanIf2BsCapCfgMaxNumOfClassifier_Type()
)
wmanIf2BsCapCfgMaxNumOfClassifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgMaxNumOfClassifier.setStatus("current")
_WmanIf2BsCapCfgTtgTransitionGap_Type = WmanIf2SsTransitionGap
_WmanIf2BsCapCfgTtgTransitionGap_Object = MibTableColumn
wmanIf2BsCapCfgTtgTransitionGap = _WmanIf2BsCapCfgTtgTransitionGap_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 8),
    _WmanIf2BsCapCfgTtgTransitionGap_Type()
)
wmanIf2BsCapCfgTtgTransitionGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgTtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgTtgTransitionGap.setUnits("microsecond")
_WmanIf2BsCapCfgRtgTransitionGap_Type = WmanIf2SsTransitionGap
_WmanIf2BsCapCfgRtgTransitionGap_Object = MibTableColumn
wmanIf2BsCapCfgRtgTransitionGap = _WmanIf2BsCapCfgRtgTransitionGap_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 9),
    _WmanIf2BsCapCfgRtgTransitionGap_Type()
)
wmanIf2BsCapCfgRtgTransitionGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgRtgTransitionGap.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgRtgTransitionGap.setUnits("microsecond")
_WmanIf2BsCapCfgDownlinkCidSupport_Type = WmanIf2NumOfCid
_WmanIf2BsCapCfgDownlinkCidSupport_Object = MibTableColumn
wmanIf2BsCapCfgDownlinkCidSupport = _WmanIf2BsCapCfgDownlinkCidSupport_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 10),
    _WmanIf2BsCapCfgDownlinkCidSupport_Type()
)
wmanIf2BsCapCfgDownlinkCidSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgDownlinkCidSupport.setStatus("current")


class _WmanIf2BsCapCfgMaxNumBurstToMs_Type(Integer32):
    """Custom type wmanIf2BsCapCfgMaxNumBurstToMs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WmanIf2BsCapCfgMaxNumBurstToMs_Type.__name__ = "Integer32"
_WmanIf2BsCapCfgMaxNumBurstToMs_Object = MibTableColumn
wmanIf2BsCapCfgMaxNumBurstToMs = _WmanIf2BsCapCfgMaxNumBurstToMs_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 11),
    _WmanIf2BsCapCfgMaxNumBurstToMs_Type()
)
wmanIf2BsCapCfgMaxNumBurstToMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgMaxNumBurstToMs.setStatus("current")


class _WmanIf2BsCapCfgMaxMacLevelDlFrame_Type(WmanIf2MaxMacLevel):
    """Custom type wmanIf2BsCapCfgMaxMacLevelDlFrame based on WmanIf2MaxMacLevel"""
    defaultValue = 0


_WmanIf2BsCapCfgMaxMacLevelDlFrame_Type.__name__ = "WmanIf2MaxMacLevel"
_WmanIf2BsCapCfgMaxMacLevelDlFrame_Object = MibTableColumn
wmanIf2BsCapCfgMaxMacLevelDlFrame = _WmanIf2BsCapCfgMaxMacLevelDlFrame_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 12),
    _WmanIf2BsCapCfgMaxMacLevelDlFrame_Type()
)
wmanIf2BsCapCfgMaxMacLevelDlFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgMaxMacLevelDlFrame.setStatus("current")


class _WmanIf2BsCapCfgMaxMacLevelUlFrame_Type(WmanIf2MaxMacLevel):
    """Custom type wmanIf2BsCapCfgMaxMacLevelUlFrame based on WmanIf2MaxMacLevel"""
    defaultValue = 0


_WmanIf2BsCapCfgMaxMacLevelUlFrame_Type.__name__ = "WmanIf2MaxMacLevel"
_WmanIf2BsCapCfgMaxMacLevelUlFrame_Object = MibTableColumn
wmanIf2BsCapCfgMaxMacLevelUlFrame = _WmanIf2BsCapCfgMaxMacLevelUlFrame_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 13),
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
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 14),
    _WmanIf2BsCapCfgNumOfProvisionedSf_Type()
)
wmanIf2BsCapCfgNumOfProvisionedSf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgNumOfProvisionedSf.setStatus("current")


class _WmanIf2BsCapCfgPnWindowSize_Type(Integer32):
    """Custom type wmanIf2BsCapCfgPnWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsCapCfgPnWindowSize_Type.__name__ = "Integer32"
_WmanIf2BsCapCfgPnWindowSize_Object = MibTableColumn
wmanIf2BsCapCfgPnWindowSize = _WmanIf2BsCapCfgPnWindowSize_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 15),
    _WmanIf2BsCapCfgPnWindowSize_Type()
)
wmanIf2BsCapCfgPnWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgPnWindowSize.setStatus("current")
_WmanIf2BsOfdmCapCfgLoopPwrControlSw_Type = Unsigned32
_WmanIf2BsOfdmCapCfgLoopPwrControlSw_Object = MibTableColumn
wmanIf2BsOfdmCapCfgLoopPwrControlSw = _WmanIf2BsOfdmCapCfgLoopPwrControlSw_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 16),
    _WmanIf2BsOfdmCapCfgLoopPwrControlSw_Type()
)
wmanIf2BsOfdmCapCfgLoopPwrControlSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmCapCfgLoopPwrControlSw.setStatus("current")
_WmanIf2BsOfdmaCapCfgSdmaPilot_Type = WmanIf2SdmaPilotCap
_WmanIf2BsOfdmaCapCfgSdmaPilot_Object = MibTableColumn
wmanIf2BsOfdmaCapCfgSdmaPilot = _WmanIf2BsOfdmaCapCfgSdmaPilot_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 17),
    _WmanIf2BsOfdmaCapCfgSdmaPilot_Type()
)
wmanIf2BsOfdmaCapCfgSdmaPilot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapCfgSdmaPilot.setStatus("current")
_WmanIf2BsOfdmaCapCfgNoUlHarqChannel_Type = WmanIf2OfdmaNoHarqChan
_WmanIf2BsOfdmaCapCfgNoUlHarqChannel_Object = MibTableColumn
wmanIf2BsOfdmaCapCfgNoUlHarqChannel = _WmanIf2BsOfdmaCapCfgNoUlHarqChannel_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 18),
    _WmanIf2BsOfdmaCapCfgNoUlHarqChannel_Type()
)
wmanIf2BsOfdmaCapCfgNoUlHarqChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapCfgNoUlHarqChannel.setStatus("current")
_WmanIf2BsOfdmaCapCfgNoDlHarqChannel_Type = WmanIf2OfdmaNoHarqChan
_WmanIf2BsOfdmaCapCfgNoDlHarqChannel_Object = MibTableColumn
wmanIf2BsOfdmaCapCfgNoDlHarqChannel = _WmanIf2BsOfdmaCapCfgNoDlHarqChannel_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 19),
    _WmanIf2BsOfdmaCapCfgNoDlHarqChannel_Type()
)
wmanIf2BsOfdmaCapCfgNoDlHarqChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCapCfgNoDlHarqChannel.setStatus("current")
_WmanIf2BsCapCfgOptionsBasic_Type = WmanIf2BasicCapOptions
_WmanIf2BsCapCfgOptionsBasic_Object = MibTableColumn
wmanIf2BsCapCfgOptionsBasic = _WmanIf2BsCapCfgOptionsBasic_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 20),
    _WmanIf2BsCapCfgOptionsBasic_Type()
)
wmanIf2BsCapCfgOptionsBasic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgOptionsBasic.setStatus("current")
_WmanIf2BsCapCfgOptionsOfdm_Type = WmanIf2OfdmCapOptions
_WmanIf2BsCapCfgOptionsOfdm_Object = MibTableColumn
wmanIf2BsCapCfgOptionsOfdm = _WmanIf2BsCapCfgOptionsOfdm_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 21),
    _WmanIf2BsCapCfgOptionsOfdm_Type()
)
wmanIf2BsCapCfgOptionsOfdm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgOptionsOfdm.setStatus("current")
_WmanIf2BsCapCfgOptionsOfdma_Type = WmanIf2OfdmaCapOptions
_WmanIf2BsCapCfgOptionsOfdma_Object = MibTableColumn
wmanIf2BsCapCfgOptionsOfdma = _WmanIf2BsCapCfgOptionsOfdma_Object(
    (1, 0, 8802, 16, 2, 1, 2, 6, 1, 22),
    _WmanIf2BsCapCfgOptionsOfdma_Type()
)
wmanIf2BsCapCfgOptionsOfdma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsCapCfgOptionsOfdma.setStatus("current")
_WmanIf2BsSsActionsTable_Object = MibTable
wmanIf2BsSsActionsTable = _WmanIf2BsSsActionsTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsActionsTable.setStatus("current")
_WmanIf2BsSsActionsEntry_Object = MibTableRow
wmanIf2BsSsActionsEntry = _WmanIf2BsSsActionsEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 7, 1)
)
wmanIf2BsSsActionsEntry.setIndexNames(
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsSsActionsMacAddress"),
)
if mibBuilder.loadTexts:
    wmanIf2BsSsActionsEntry.setStatus("current")
_WmanIf2BsSsActionsMacAddress_Type = MacAddress
_WmanIf2BsSsActionsMacAddress_Object = MibTableColumn
wmanIf2BsSsActionsMacAddress = _WmanIf2BsSsActionsMacAddress_Object(
    (1, 0, 8802, 16, 2, 1, 2, 7, 1, 1),
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
    (1, 0, 8802, 16, 2, 1, 2, 7, 1, 2),
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
    (1, 0, 8802, 16, 2, 1, 2, 7, 1, 3),
    _WmanIf2BsSsActionsAbortSs_Type()
)
wmanIf2BsSsActionsAbortSs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsSsActionsAbortSs.setStatus("current")
_WmanIf2BsSsActionsOverrideDnFreq_Type = Unsigned32
_WmanIf2BsSsActionsOverrideDnFreq_Object = MibTableColumn
wmanIf2BsSsActionsOverrideDnFreq = _WmanIf2BsSsActionsOverrideDnFreq_Object(
    (1, 0, 8802, 16, 2, 1, 2, 7, 1, 4),
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
    (1, 0, 8802, 16, 2, 1, 2, 7, 1, 5),
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
    (1, 0, 8802, 16, 2, 1, 2, 7, 1, 6),
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
    (1, 0, 8802, 16, 2, 1, 2, 7, 1, 7),
    _WmanIf2BsSsActionsDeReRegSsCode_Type()
)
wmanIf2BsSsActionsDeReRegSsCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsSsActionsDeReRegSsCode.setStatus("current")
_WmanIf2BsSsActionsRowStatus_Type = RowStatus
_WmanIf2BsSsActionsRowStatus_Object = MibTableColumn
wmanIf2BsSsActionsRowStatus = _WmanIf2BsSsActionsRowStatus_Object(
    (1, 0, 8802, 16, 2, 1, 2, 7, 1, 8),
    _WmanIf2BsSsActionsRowStatus_Type()
)
wmanIf2BsSsActionsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsSsActionsRowStatus.setStatus("current")
_WmanIf2BsMulticastPollingTable_Object = MibTable
wmanIf2BsMulticastPollingTable = _WmanIf2BsMulticastPollingTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 8)
)
if mibBuilder.loadTexts:
    wmanIf2BsMulticastPollingTable.setStatus("current")
_WmanIf2BsMulticastPollingEntry_Object = MibTableRow
wmanIf2BsMulticastPollingEntry = _WmanIf2BsMulticastPollingEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 8, 1)
)
wmanIf2BsMulticastPollingEntry.setIndexNames(
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsMulticastPollingCid"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsSsMacAddress"),
)
if mibBuilder.loadTexts:
    wmanIf2BsMulticastPollingEntry.setStatus("current")
_WmanIf2BsMulticastPollingCid_Type = WmanIf2CidType
_WmanIf2BsMulticastPollingCid_Object = MibTableColumn
wmanIf2BsMulticastPollingCid = _WmanIf2BsMulticastPollingCid_Object(
    (1, 0, 8802, 16, 2, 1, 2, 8, 1, 1),
    _WmanIf2BsMulticastPollingCid_Type()
)
wmanIf2BsMulticastPollingCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsMulticastPollingCid.setStatus("current")


class _WmanIf2BsMulticastGroupType_Type(Integer32):
    """Custom type wmanIf2BsMulticastGroupType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("regular", 0),
          ("aas", 1))
    )


_WmanIf2BsMulticastGroupType_Type.__name__ = "Integer32"
_WmanIf2BsMulticastGroupType_Object = MibTableColumn
wmanIf2BsMulticastGroupType = _WmanIf2BsMulticastGroupType_Object(
    (1, 0, 8802, 16, 2, 1, 2, 8, 1, 2),
    _WmanIf2BsMulticastGroupType_Type()
)
wmanIf2BsMulticastGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsMulticastGroupType.setStatus("current")


class _WmanIf2BsPeriodAllocationParameterM_Type(Integer32):
    """Custom type wmanIf2BsPeriodAllocationParameterM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsPeriodAllocationParameterM_Type.__name__ = "Integer32"
_WmanIf2BsPeriodAllocationParameterM_Object = MibTableColumn
wmanIf2BsPeriodAllocationParameterM = _WmanIf2BsPeriodAllocationParameterM_Object(
    (1, 0, 8802, 16, 2, 1, 2, 8, 1, 3),
    _WmanIf2BsPeriodAllocationParameterM_Type()
)
wmanIf2BsPeriodAllocationParameterM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsPeriodAllocationParameterM.setStatus("current")


class _WmanIf2BsPeriodAllocationParameterK_Type(Integer32):
    """Custom type wmanIf2BsPeriodAllocationParameterK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsPeriodAllocationParameterK_Type.__name__ = "Integer32"
_WmanIf2BsPeriodAllocationParameterK_Object = MibTableColumn
wmanIf2BsPeriodAllocationParameterK = _WmanIf2BsPeriodAllocationParameterK_Object(
    (1, 0, 8802, 16, 2, 1, 2, 8, 1, 4),
    _WmanIf2BsPeriodAllocationParameterK_Type()
)
wmanIf2BsPeriodAllocationParameterK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsPeriodAllocationParameterK.setStatus("current")


class _WmanIf2BsPeriodAllocationParameterN_Type(Integer32):
    """Custom type wmanIf2BsPeriodAllocationParameterN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsPeriodAllocationParameterN_Type.__name__ = "Integer32"
_WmanIf2BsPeriodAllocationParameterN_Object = MibTableColumn
wmanIf2BsPeriodAllocationParameterN = _WmanIf2BsPeriodAllocationParameterN_Object(
    (1, 0, 8802, 16, 2, 1, 2, 8, 1, 5),
    _WmanIf2BsPeriodAllocationParameterN_Type()
)
wmanIf2BsPeriodAllocationParameterN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsPeriodAllocationParameterN.setStatus("current")


class _WmanIf2BsPeriodicAllocationType_Type(Integer32):
    """Custom type wmanIf2BsPeriodicAllocationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("reqRegionFull", 0),
          ("regRegionFocused", 1))
    )


_WmanIf2BsPeriodicAllocationType_Type.__name__ = "Integer32"
_WmanIf2BsPeriodicAllocationType_Object = MibTableColumn
wmanIf2BsPeriodicAllocationType = _WmanIf2BsPeriodicAllocationType_Object(
    (1, 0, 8802, 16, 2, 1, 2, 8, 1, 6),
    _WmanIf2BsPeriodicAllocationType_Type()
)
wmanIf2BsPeriodicAllocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsPeriodicAllocationType.setStatus("current")
_WmanIf2BsPhy_ObjectIdentity = ObjectIdentity
wmanIf2BsPhy = _WmanIf2BsPhy_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 2, 9)
)
_WmanIf2BsCmnPhy_ObjectIdentity = ObjectIdentity
wmanIf2BsCmnPhy = _WmanIf2BsCmnPhy_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 2, 9, 1)
)
_WmanIf2BsCmnPhyUplinkChannelTable_Object = MibTable
wmanIf2BsCmnPhyUplinkChannelTable = _WmanIf2BsCmnPhyUplinkChannelTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyUplinkChannelTable.setStatus("current")
_WmanIf2BsCmnPhyUplinkChannelEntry_Object = MibTableRow
wmanIf2BsCmnPhyUplinkChannelEntry = _WmanIf2BsCmnPhyUplinkChannelEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 1, 1, 1)
)
wmanIf2BsCmnPhyUplinkChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyUplinkChannelEntry.setStatus("current")


class _WmanIf2BsCmnPhyCtBasedResvTimeout_Type(Integer32):
    """Custom type wmanIf2BsCmnPhyCtBasedResvTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WmanIf2BsCmnPhyCtBasedResvTimeout_Type.__name__ = "Integer32"
_WmanIf2BsCmnPhyCtBasedResvTimeout_Object = MibTableColumn
wmanIf2BsCmnPhyCtBasedResvTimeout = _WmanIf2BsCmnPhyCtBasedResvTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 1, 1, 1, 1),
    _WmanIf2BsCmnPhyCtBasedResvTimeout_Type()
)
wmanIf2BsCmnPhyCtBasedResvTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyCtBasedResvTimeout.setStatus("current")
_WmanIf2BsCmnPhyUplinkCenterFreq_Type = Unsigned32
_WmanIf2BsCmnPhyUplinkCenterFreq_Object = MibTableColumn
wmanIf2BsCmnPhyUplinkCenterFreq = _WmanIf2BsCmnPhyUplinkCenterFreq_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 1, 1, 1, 2),
    _WmanIf2BsCmnPhyUplinkCenterFreq_Type()
)
wmanIf2BsCmnPhyUplinkCenterFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyUplinkCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyUplinkCenterFreq.setUnits("kHz")
_WmanIf2BsCmnPhyDownlinkChannelTable_Object = MibTable
wmanIf2BsCmnPhyDownlinkChannelTable = _WmanIf2BsCmnPhyDownlinkChannelTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 1, 2)
)
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyDownlinkChannelTable.setStatus("current")
_WmanIf2BsCmnPhyDownlinkChannelEntry_Object = MibTableRow
wmanIf2BsCmnPhyDownlinkChannelEntry = _WmanIf2BsCmnPhyDownlinkChannelEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 1, 2, 1)
)
wmanIf2BsCmnPhyDownlinkChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyDownlinkChannelEntry.setStatus("current")


class _WmanIf2BsCmnPhyBsEIRP_Type(Integer32):
    """Custom type wmanIf2BsCmnPhyBsEIRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_WmanIf2BsCmnPhyBsEIRP_Type.__name__ = "Integer32"
_WmanIf2BsCmnPhyBsEIRP_Object = MibTableColumn
wmanIf2BsCmnPhyBsEIRP = _WmanIf2BsCmnPhyBsEIRP_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 1, 2, 1, 1),
    _WmanIf2BsCmnPhyBsEIRP_Type()
)
wmanIf2BsCmnPhyBsEIRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyBsEIRP.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyBsEIRP.setUnits("dBm")
_WmanIf2BsCmnPhyChannelNumber_Type = WmanIf2ChannelNumber
_WmanIf2BsCmnPhyChannelNumber_Object = MibTableColumn
wmanIf2BsCmnPhyChannelNumber = _WmanIf2BsCmnPhyChannelNumber_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 1, 2, 1, 2),
    _WmanIf2BsCmnPhyChannelNumber_Type()
)
wmanIf2BsCmnPhyChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyChannelNumber.setStatus("current")


class _WmanIf2BsCmnPhyTTG_Type(Integer32):
    """Custom type wmanIf2BsCmnPhyTTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsCmnPhyTTG_Type.__name__ = "Integer32"
_WmanIf2BsCmnPhyTTG_Object = MibTableColumn
wmanIf2BsCmnPhyTTG = _WmanIf2BsCmnPhyTTG_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 1, 2, 1, 3),
    _WmanIf2BsCmnPhyTTG_Type()
)
wmanIf2BsCmnPhyTTG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyTTG.setStatus("current")


class _WmanIf2BsCmnPhyRTG_Type(Integer32):
    """Custom type wmanIf2BsCmnPhyRTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsCmnPhyRTG_Type.__name__ = "Integer32"
_WmanIf2BsCmnPhyRTG_Object = MibTableColumn
wmanIf2BsCmnPhyRTG = _WmanIf2BsCmnPhyRTG_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 1, 2, 1, 4),
    _WmanIf2BsCmnPhyRTG_Type()
)
wmanIf2BsCmnPhyRTG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyRTG.setStatus("current")


class _WmanIf2BsCmnPhyInitRngMaxRSS_Type(Integer32):
    """Custom type wmanIf2BsCmnPhyInitRngMaxRSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_WmanIf2BsCmnPhyInitRngMaxRSS_Type.__name__ = "Integer32"
_WmanIf2BsCmnPhyInitRngMaxRSS_Object = MibTableColumn
wmanIf2BsCmnPhyInitRngMaxRSS = _WmanIf2BsCmnPhyInitRngMaxRSS_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 1, 2, 1, 5),
    _WmanIf2BsCmnPhyInitRngMaxRSS_Type()
)
wmanIf2BsCmnPhyInitRngMaxRSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyInitRngMaxRSS.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyInitRngMaxRSS.setUnits("dBm")
_WmanIf2BsCmnPhyDownlinkCenterFreq_Type = Unsigned32
_WmanIf2BsCmnPhyDownlinkCenterFreq_Object = MibTableColumn
wmanIf2BsCmnPhyDownlinkCenterFreq = _WmanIf2BsCmnPhyDownlinkCenterFreq_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 1, 2, 1, 6),
    _WmanIf2BsCmnPhyDownlinkCenterFreq_Type()
)
wmanIf2BsCmnPhyDownlinkCenterFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyDownlinkCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyDownlinkCenterFreq.setUnits("kHz")
_WmanIf2BsCmnPhyBsId_Type = WmanIf2BsIdType
_WmanIf2BsCmnPhyBsId_Object = MibTableColumn
wmanIf2BsCmnPhyBsId = _WmanIf2BsCmnPhyBsId_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 1, 2, 1, 7),
    _WmanIf2BsCmnPhyBsId_Type()
)
wmanIf2BsCmnPhyBsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyBsId.setStatus("current")
_WmanIf2BsCmnPhyMacVersion_Type = WmanIf2MacVersion
_WmanIf2BsCmnPhyMacVersion_Object = MibTableColumn
wmanIf2BsCmnPhyMacVersion = _WmanIf2BsCmnPhyMacVersion_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 1, 2, 1, 8),
    _WmanIf2BsCmnPhyMacVersion_Type()
)
wmanIf2BsCmnPhyMacVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyMacVersion.setStatus("current")


class _WmanIf2BsCmnPhyCyclicPrefix_Type(Integer32):
    """Custom type wmanIf2BsCmnPhyCyclicPrefix based on Integer32"""
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


_WmanIf2BsCmnPhyCyclicPrefix_Type.__name__ = "Integer32"
_WmanIf2BsCmnPhyCyclicPrefix_Object = MibTableColumn
wmanIf2BsCmnPhyCyclicPrefix = _WmanIf2BsCmnPhyCyclicPrefix_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 1, 2, 1, 9),
    _WmanIf2BsCmnPhyCyclicPrefix_Type()
)
wmanIf2BsCmnPhyCyclicPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCmnPhyCyclicPrefix.setStatus("current")
_WmanIf2BsOfdmPhy_ObjectIdentity = ObjectIdentity
wmanIf2BsOfdmPhy = _WmanIf2BsOfdmPhy_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2)
)
_WmanIf2BsOfdmUplinkChannelTable_Object = MibTable
wmanIf2BsOfdmUplinkChannelTable = _WmanIf2BsOfdmUplinkChannelTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmUplinkChannelTable.setStatus("current")
_WmanIf2BsOfdmUplinkChannelEntry_Object = MibTableRow
wmanIf2BsOfdmUplinkChannelEntry = _WmanIf2BsOfdmUplinkChannelEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 1, 1)
)
wmanIf2BsOfdmUplinkChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmUplinkChannelEntry.setStatus("current")


class _WmanIf2BsOfdmBwReqOppSize_Type(Integer32):
    """Custom type wmanIf2BsOfdmBwReqOppSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2BsOfdmBwReqOppSize_Type.__name__ = "Integer32"
_WmanIf2BsOfdmBwReqOppSize_Object = MibTableColumn
wmanIf2BsOfdmBwReqOppSize = _WmanIf2BsOfdmBwReqOppSize_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 1, 1, 1),
    _WmanIf2BsOfdmBwReqOppSize_Type()
)
wmanIf2BsOfdmBwReqOppSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmBwReqOppSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmBwReqOppSize.setUnits("PS")


class _WmanIf2BsOfdmRangReqOppSize_Type(Integer32):
    """Custom type wmanIf2BsOfdmRangReqOppSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2BsOfdmRangReqOppSize_Type.__name__ = "Integer32"
_WmanIf2BsOfdmRangReqOppSize_Object = MibTableColumn
wmanIf2BsOfdmRangReqOppSize = _WmanIf2BsOfdmRangReqOppSize_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 1, 1, 2),
    _WmanIf2BsOfdmRangReqOppSize_Type()
)
wmanIf2BsOfdmRangReqOppSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmRangReqOppSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmRangReqOppSize.setUnits("PS")


class _WmanIf2BsOfdmNumSubChReqRegionFull_Type(Integer32):
    """Custom type wmanIf2BsOfdmNumSubChReqRegionFull based on Integer32"""
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


_WmanIf2BsOfdmNumSubChReqRegionFull_Type.__name__ = "Integer32"
_WmanIf2BsOfdmNumSubChReqRegionFull_Object = MibTableColumn
wmanIf2BsOfdmNumSubChReqRegionFull = _WmanIf2BsOfdmNumSubChReqRegionFull_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 1, 1, 3),
    _WmanIf2BsOfdmNumSubChReqRegionFull_Type()
)
wmanIf2BsOfdmNumSubChReqRegionFull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmNumSubChReqRegionFull.setStatus("current")


class _WmanIf2BsOfdmNumSymbolsReqRegionFull_Type(Integer32):
    """Custom type wmanIf2BsOfdmNumSymbolsReqRegionFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_WmanIf2BsOfdmNumSymbolsReqRegionFull_Type.__name__ = "Integer32"
_WmanIf2BsOfdmNumSymbolsReqRegionFull_Object = MibTableColumn
wmanIf2BsOfdmNumSymbolsReqRegionFull = _WmanIf2BsOfdmNumSymbolsReqRegionFull_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 1, 1, 4),
    _WmanIf2BsOfdmNumSymbolsReqRegionFull_Type()
)
wmanIf2BsOfdmNumSymbolsReqRegionFull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmNumSymbolsReqRegionFull.setStatus("current")


class _WmanIf2BsOfdmSubChFocusCtCode_Type(Integer32):
    """Custom type wmanIf2BsOfdmSubChFocusCtCode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_WmanIf2BsOfdmSubChFocusCtCode_Type.__name__ = "Integer32"
_WmanIf2BsOfdmSubChFocusCtCode_Object = MibTableColumn
wmanIf2BsOfdmSubChFocusCtCode = _WmanIf2BsOfdmSubChFocusCtCode_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 1, 1, 5),
    _WmanIf2BsOfdmSubChFocusCtCode_Type()
)
wmanIf2BsOfdmSubChFocusCtCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmSubChFocusCtCode.setStatus("current")
_WmanIf2BsOfdmDownlinkChannelTable_Object = MibTable
wmanIf2BsOfdmDownlinkChannelTable = _WmanIf2BsOfdmDownlinkChannelTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 2)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmDownlinkChannelTable.setStatus("current")
_WmanIf2BsOfdmDownlinkChannelEntry_Object = MibTableRow
wmanIf2BsOfdmDownlinkChannelEntry = _WmanIf2BsOfdmDownlinkChannelEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 2, 1)
)
wmanIf2BsOfdmDownlinkChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmDownlinkChannelEntry.setStatus("current")


class _WmanIf2BsOfdmFrameDurationCode_Type(Integer32):
    """Custom type wmanIf2BsOfdmFrameDurationCode based on Integer32"""
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


_WmanIf2BsOfdmFrameDurationCode_Type.__name__ = "Integer32"
_WmanIf2BsOfdmFrameDurationCode_Object = MibTableColumn
wmanIf2BsOfdmFrameDurationCode = _WmanIf2BsOfdmFrameDurationCode_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 2, 1, 1),
    _WmanIf2BsOfdmFrameDurationCode_Type()
)
wmanIf2BsOfdmFrameDurationCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmFrameDurationCode.setStatus("current")
_WmanIf2BsOfdmFftSize_Type = WmanIf2OfdmFftSize
_WmanIf2BsOfdmFftSize_Object = MibTableColumn
wmanIf2BsOfdmFftSize = _WmanIf2BsOfdmFftSize_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 2, 1, 2),
    _WmanIf2BsOfdmFftSize_Type()
)
wmanIf2BsOfdmFftSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmFftSize.setStatus("current")
_WmanIf2BsOfdmUcdBurstProfileTable_Object = MibTable
wmanIf2BsOfdmUcdBurstProfileTable = _WmanIf2BsOfdmUcdBurstProfileTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 3)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmUcdBurstProfileTable.setStatus("current")
_WmanIf2BsOfdmUcdBurstProfileEntry_Object = MibTableRow
wmanIf2BsOfdmUcdBurstProfileEntry = _WmanIf2BsOfdmUcdBurstProfileEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 3, 1)
)
wmanIf2BsOfdmUcdBurstProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsOfdmUiucIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmUcdBurstProfileEntry.setStatus("current")


class _WmanIf2BsOfdmUiucIndex_Type(Integer32):
    """Custom type wmanIf2BsOfdmUiucIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_WmanIf2BsOfdmUiucIndex_Type.__name__ = "Integer32"
_WmanIf2BsOfdmUiucIndex_Object = MibTableColumn
wmanIf2BsOfdmUiucIndex = _WmanIf2BsOfdmUiucIndex_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 3, 1, 1),
    _WmanIf2BsOfdmUiucIndex_Type()
)
wmanIf2BsOfdmUiucIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmUiucIndex.setStatus("current")
_WmanIf2BsOfdmUcdFecCodeType_Type = WmanIf2OfdmFecCodeType
_WmanIf2BsOfdmUcdFecCodeType_Object = MibTableColumn
wmanIf2BsOfdmUcdFecCodeType = _WmanIf2BsOfdmUcdFecCodeType_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 3, 1, 2),
    _WmanIf2BsOfdmUcdFecCodeType_Type()
)
wmanIf2BsOfdmUcdFecCodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmUcdFecCodeType.setStatus("current")


class _WmanIf2BsOfdmFocusCtPowerBoost_Type(Integer32):
    """Custom type wmanIf2BsOfdmFocusCtPowerBoost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmFocusCtPowerBoost_Type.__name__ = "Integer32"
_WmanIf2BsOfdmFocusCtPowerBoost_Object = MibTableColumn
wmanIf2BsOfdmFocusCtPowerBoost = _WmanIf2BsOfdmFocusCtPowerBoost_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 3, 1, 3),
    _WmanIf2BsOfdmFocusCtPowerBoost_Type()
)
wmanIf2BsOfdmFocusCtPowerBoost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmFocusCtPowerBoost.setStatus("current")


class _WmanIf2BsOfdmUcdTcsEnable_Type(Integer32):
    """Custom type wmanIf2BsOfdmUcdTcsEnable based on Integer32"""
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


_WmanIf2BsOfdmUcdTcsEnable_Type.__name__ = "Integer32"
_WmanIf2BsOfdmUcdTcsEnable_Object = MibTableColumn
wmanIf2BsOfdmUcdTcsEnable = _WmanIf2BsOfdmUcdTcsEnable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 3, 1, 4),
    _WmanIf2BsOfdmUcdTcsEnable_Type()
)
wmanIf2BsOfdmUcdTcsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmUcdTcsEnable.setStatus("current")
_WmanIf2BsOfdmUcdBurstProfileRowStatus_Type = RowStatus
_WmanIf2BsOfdmUcdBurstProfileRowStatus_Object = MibTableColumn
wmanIf2BsOfdmUcdBurstProfileRowStatus = _WmanIf2BsOfdmUcdBurstProfileRowStatus_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 3, 1, 5),
    _WmanIf2BsOfdmUcdBurstProfileRowStatus_Type()
)
wmanIf2BsOfdmUcdBurstProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmUcdBurstProfileRowStatus.setStatus("current")
_WmanIf2BsOfdmDcdBurstProfileTable_Object = MibTable
wmanIf2BsOfdmDcdBurstProfileTable = _WmanIf2BsOfdmDcdBurstProfileTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 4)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmDcdBurstProfileTable.setStatus("current")
_WmanIf2BsOfdmDcdBurstProfileEntry_Object = MibTableRow
wmanIf2BsOfdmDcdBurstProfileEntry = _WmanIf2BsOfdmDcdBurstProfileEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 4, 1)
)
wmanIf2BsOfdmDcdBurstProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsOfdmDiucIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmDcdBurstProfileEntry.setStatus("current")


class _WmanIf2BsOfdmDiucIndex_Type(Integer32):
    """Custom type wmanIf2BsOfdmDiucIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_WmanIf2BsOfdmDiucIndex_Type.__name__ = "Integer32"
_WmanIf2BsOfdmDiucIndex_Object = MibTableColumn
wmanIf2BsOfdmDiucIndex = _WmanIf2BsOfdmDiucIndex_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 4, 1, 1),
    _WmanIf2BsOfdmDiucIndex_Type()
)
wmanIf2BsOfdmDiucIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmDiucIndex.setStatus("current")
_WmanIf2BsOfdmDcdFecCodeType_Type = WmanIf2OfdmFecCodeType
_WmanIf2BsOfdmDcdFecCodeType_Object = MibTableColumn
wmanIf2BsOfdmDcdFecCodeType = _WmanIf2BsOfdmDcdFecCodeType_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 4, 1, 2),
    _WmanIf2BsOfdmDcdFecCodeType_Type()
)
wmanIf2BsOfdmDcdFecCodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmDcdFecCodeType.setStatus("current")


class _WmanIf2BsOfdmTcsEnable_Type(Integer32):
    """Custom type wmanIf2BsOfdmTcsEnable based on Integer32"""
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


_WmanIf2BsOfdmTcsEnable_Type.__name__ = "Integer32"
_WmanIf2BsOfdmTcsEnable_Object = MibTableColumn
wmanIf2BsOfdmTcsEnable = _WmanIf2BsOfdmTcsEnable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 4, 1, 3),
    _WmanIf2BsOfdmTcsEnable_Type()
)
wmanIf2BsOfdmTcsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmTcsEnable.setStatus("current")
_WmanIf2BsOfdmDcdBurstProfileRowStatus_Type = RowStatus
_WmanIf2BsOfdmDcdBurstProfileRowStatus_Object = MibTableColumn
wmanIf2BsOfdmDcdBurstProfileRowStatus = _WmanIf2BsOfdmDcdBurstProfileRowStatus_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 4, 1, 4),
    _WmanIf2BsOfdmDcdBurstProfileRowStatus_Type()
)
wmanIf2BsOfdmDcdBurstProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmDcdBurstProfileRowStatus.setStatus("current")
_WmanIf2BsOfdmConfigurationTable_Object = MibTable
wmanIf2BsOfdmConfigurationTable = _WmanIf2BsOfdmConfigurationTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 5)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmConfigurationTable.setStatus("current")
_WmanIf2BsOfdmConfigurationEntry_Object = MibTableRow
wmanIf2BsOfdmConfigurationEntry = _WmanIf2BsOfdmConfigurationEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 5, 1)
)
wmanIf2BsOfdmConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmConfigurationEntry.setStatus("current")


class _WmanIf2BsOfdmMinReqRegionFullTxOpp_Type(Integer32):
    """Custom type wmanIf2BsOfdmMinReqRegionFullTxOpp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2BsOfdmMinReqRegionFullTxOpp_Type.__name__ = "Integer32"
_WmanIf2BsOfdmMinReqRegionFullTxOpp_Object = MibTableColumn
wmanIf2BsOfdmMinReqRegionFullTxOpp = _WmanIf2BsOfdmMinReqRegionFullTxOpp_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 5, 1, 1),
    _WmanIf2BsOfdmMinReqRegionFullTxOpp_Type()
)
wmanIf2BsOfdmMinReqRegionFullTxOpp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmMinReqRegionFullTxOpp.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmMinReqRegionFullTxOpp.setUnits("n per second")


class _WmanIf2BsOfdmMinFocusedCtTxOpp_Type(Integer32):
    """Custom type wmanIf2BsOfdmMinFocusedCtTxOpp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsOfdmMinFocusedCtTxOpp_Type.__name__ = "Integer32"
_WmanIf2BsOfdmMinFocusedCtTxOpp_Object = MibTableColumn
wmanIf2BsOfdmMinFocusedCtTxOpp = _WmanIf2BsOfdmMinFocusedCtTxOpp_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 5, 1, 2),
    _WmanIf2BsOfdmMinFocusedCtTxOpp_Type()
)
wmanIf2BsOfdmMinFocusedCtTxOpp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmMinFocusedCtTxOpp.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmMinFocusedCtTxOpp.setUnits("1/sec")


class _WmanIf2BsOfdmMaxRoundTripDelay_Type(Integer32):
    """Custom type wmanIf2BsOfdmMaxRoundTripDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2BsOfdmMaxRoundTripDelay_Type.__name__ = "Integer32"
_WmanIf2BsOfdmMaxRoundTripDelay_Object = MibTableColumn
wmanIf2BsOfdmMaxRoundTripDelay = _WmanIf2BsOfdmMaxRoundTripDelay_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 5, 1, 3),
    _WmanIf2BsOfdmMaxRoundTripDelay_Type()
)
wmanIf2BsOfdmMaxRoundTripDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmMaxRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmMaxRoundTripDelay.setUnits("microsecond")


class _WmanIf2BsOfdmRangeAbortTimingThold_Type(Integer32):
    """Custom type wmanIf2BsOfdmRangeAbortTimingThold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmRangeAbortTimingThold_Type.__name__ = "Integer32"
_WmanIf2BsOfdmRangeAbortTimingThold_Object = MibTableColumn
wmanIf2BsOfdmRangeAbortTimingThold = _WmanIf2BsOfdmRangeAbortTimingThold_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 5, 1, 4),
    _WmanIf2BsOfdmRangeAbortTimingThold_Type()
)
wmanIf2BsOfdmRangeAbortTimingThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmRangeAbortTimingThold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmRangeAbortTimingThold.setUnits("1/Fs")


class _WmanIf2BsOfdmRangeAbortPowerThold_Type(Integer32):
    """Custom type wmanIf2BsOfdmRangeAbortPowerThold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmRangeAbortPowerThold_Type.__name__ = "Integer32"
_WmanIf2BsOfdmRangeAbortPowerThold_Object = MibTableColumn
wmanIf2BsOfdmRangeAbortPowerThold = _WmanIf2BsOfdmRangeAbortPowerThold_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 5, 1, 5),
    _WmanIf2BsOfdmRangeAbortPowerThold_Type()
)
wmanIf2BsOfdmRangeAbortPowerThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmRangeAbortPowerThold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmRangeAbortPowerThold.setUnits("0.25dB")


class _WmanIf2BsOfdmRangeAbortFreqThold_Type(Integer32):
    """Custom type wmanIf2BsOfdmRangeAbortFreqThold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmRangeAbortFreqThold_Type.__name__ = "Integer32"
_WmanIf2BsOfdmRangeAbortFreqThold_Object = MibTableColumn
wmanIf2BsOfdmRangeAbortFreqThold = _WmanIf2BsOfdmRangeAbortFreqThold_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 5, 1, 6),
    _WmanIf2BsOfdmRangeAbortFreqThold_Type()
)
wmanIf2BsOfdmRangeAbortFreqThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmRangeAbortFreqThold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmRangeAbortFreqThold.setUnits("Hz")


class _WmanIf2BsOfdmDnlkRateId_Type(Integer32):
    """Custom type wmanIf2BsOfdmDnlkRateId based on Integer32"""
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


_WmanIf2BsOfdmDnlkRateId_Type.__name__ = "Integer32"
_WmanIf2BsOfdmDnlkRateId_Object = MibTableColumn
wmanIf2BsOfdmDnlkRateId = _WmanIf2BsOfdmDnlkRateId_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 2, 5, 1, 7),
    _WmanIf2BsOfdmDnlkRateId_Type()
)
wmanIf2BsOfdmDnlkRateId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmDnlkRateId.setStatus("current")
_WmanIf2BsOfdmaPhy_ObjectIdentity = ObjectIdentity
wmanIf2BsOfdmaPhy = _WmanIf2BsOfdmaPhy_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3)
)
_WmanIf2BsOfdmaUplinkChannelTable_Object = MibTable
wmanIf2BsOfdmaUplinkChannelTable = _WmanIf2BsOfdmaUplinkChannelTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaUplinkChannelTable.setStatus("current")
_WmanIf2BsOfdmaUplinkChannelEntry_Object = MibTableRow
wmanIf2BsOfdmaUplinkChannelEntry = _WmanIf2BsOfdmaUplinkChannelEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1)
)
wmanIf2BsOfdmaUplinkChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaUplinkChannelEntry.setStatus("current")


class _WmanIf2BsOfdmaStartOfRngCodes_Type(Integer32):
    """Custom type wmanIf2BsOfdmaStartOfRngCodes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaStartOfRngCodes_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaStartOfRngCodes_Object = MibTableColumn
wmanIf2BsOfdmaStartOfRngCodes = _WmanIf2BsOfdmaStartOfRngCodes_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 1),
    _WmanIf2BsOfdmaStartOfRngCodes_Type()
)
wmanIf2BsOfdmaStartOfRngCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaStartOfRngCodes.setStatus("current")


class _WmanIf2BsOfdmaPermutationBase_Type(Integer32):
    """Custom type wmanIf2BsOfdmaPermutationBase based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaPermutationBase_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaPermutationBase_Object = MibTableColumn
wmanIf2BsOfdmaPermutationBase = _WmanIf2BsOfdmaPermutationBase_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 2),
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
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 3),
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
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 4),
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
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 5),
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
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 6),
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
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 7),
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
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 8),
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
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 9),
    _WmanIf2BsOfdmaBandStatRepMAXPeriod_Type()
)
wmanIf2BsOfdmaBandStatRepMAXPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBandStatRepMAXPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBandStatRepMAXPeriod.setUnits("Frame")


class _WmanIf2BsOfdmaPerRngBackoffStart_Type(Integer32):
    """Custom type wmanIf2BsOfdmaPerRngBackoffStart based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaPerRngBackoffStart_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaPerRngBackoffStart_Object = MibTableColumn
wmanIf2BsOfdmaPerRngBackoffStart = _WmanIf2BsOfdmaPerRngBackoffStart_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 10),
    _WmanIf2BsOfdmaPerRngBackoffStart_Type()
)
wmanIf2BsOfdmaPerRngBackoffStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaPerRngBackoffStart.setStatus("current")


class _WmanIf2BsOfdmaPerRngBackoffEnd_Type(Integer32):
    """Custom type wmanIf2BsOfdmaPerRngBackoffEnd based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaPerRngBackoffEnd_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaPerRngBackoffEnd_Object = MibTableColumn
wmanIf2BsOfdmaPerRngBackoffEnd = _WmanIf2BsOfdmaPerRngBackoffEnd_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 11),
    _WmanIf2BsOfdmaPerRngBackoffEnd_Type()
)
wmanIf2BsOfdmaPerRngBackoffEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaPerRngBackoffEnd.setStatus("current")


class _WmanIf2BsOfdmaBandAMCRetryTimer_Type(Integer32):
    """Custom type wmanIf2BsOfdmaBandAMCRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaBandAMCRetryTimer_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaBandAMCRetryTimer_Object = MibTableColumn
wmanIf2BsOfdmaBandAMCRetryTimer = _WmanIf2BsOfdmaBandAMCRetryTimer_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 12),
    _WmanIf2BsOfdmaBandAMCRetryTimer_Type()
)
wmanIf2BsOfdmaBandAMCRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBandAMCRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBandAMCRetryTimer.setUnits("Frame")


class _WmanIf2BsOfdmaInitRngCodes_Type(Integer32):
    """Custom type wmanIf2BsOfdmaInitRngCodes based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaInitRngCodes_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaInitRngCodes_Object = MibTableColumn
wmanIf2BsOfdmaInitRngCodes = _WmanIf2BsOfdmaInitRngCodes_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 13),
    _WmanIf2BsOfdmaInitRngCodes_Type()
)
wmanIf2BsOfdmaInitRngCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaInitRngCodes.setStatus("current")


class _WmanIf2BsOfdmaPeriodicRngCodes_Type(Integer32):
    """Custom type wmanIf2BsOfdmaPeriodicRngCodes based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaPeriodicRngCodes_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaPeriodicRngCodes_Object = MibTableColumn
wmanIf2BsOfdmaPeriodicRngCodes = _WmanIf2BsOfdmaPeriodicRngCodes_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 14),
    _WmanIf2BsOfdmaPeriodicRngCodes_Type()
)
wmanIf2BsOfdmaPeriodicRngCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaPeriodicRngCodes.setStatus("current")


class _WmanIf2BsOfdmaBWReqCodes_Type(Integer32):
    """Custom type wmanIf2BsOfdmaBWReqCodes based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaBWReqCodes_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaBWReqCodes_Object = MibTableColumn
wmanIf2BsOfdmaBWReqCodes = _WmanIf2BsOfdmaBWReqCodes_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 15),
    _WmanIf2BsOfdmaBWReqCodes_Type()
)
wmanIf2BsOfdmaBWReqCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBWReqCodes.setStatus("current")


class _WmanIf2BsOfdmaHandoverRangingStart_Type(Integer32):
    """Custom type wmanIf2BsOfdmaHandoverRangingStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaHandoverRangingStart_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaHandoverRangingStart_Object = MibTableColumn
wmanIf2BsOfdmaHandoverRangingStart = _WmanIf2BsOfdmaHandoverRangingStart_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 16),
    _WmanIf2BsOfdmaHandoverRangingStart_Type()
)
wmanIf2BsOfdmaHandoverRangingStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaHandoverRangingStart.setStatus("current")


class _WmanIf2BsOfdmaHandoverRangingEnd_Type(Integer32):
    """Custom type wmanIf2BsOfdmaHandoverRangingEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaHandoverRangingEnd_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaHandoverRangingEnd_Object = MibTableColumn
wmanIf2BsOfdmaHandoverRangingEnd = _WmanIf2BsOfdmaHandoverRangingEnd_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 17),
    _WmanIf2BsOfdmaHandoverRangingEnd_Type()
)
wmanIf2BsOfdmaHandoverRangingEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaHandoverRangingEnd.setStatus("current")
_WmanIf2BsOfdmaHARQAckDelayDLBurst_Type = WmanIf2HarqAckDelay
_WmanIf2BsOfdmaHARQAckDelayDLBurst_Object = MibTableColumn
wmanIf2BsOfdmaHARQAckDelayDLBurst = _WmanIf2BsOfdmaHARQAckDelayDLBurst_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 18),
    _WmanIf2BsOfdmaHARQAckDelayDLBurst_Type()
)
wmanIf2BsOfdmaHARQAckDelayDLBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaHARQAckDelayDLBurst.setStatus("current")


class _WmanIf2BsOfdmaUlAmcAlloPhyBandsBitmap_Type(OctetString):
    """Custom type wmanIf2BsOfdmaUlAmcAlloPhyBandsBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6


_WmanIf2BsOfdmaUlAmcAlloPhyBandsBitmap_Type.__name__ = "OctetString"
_WmanIf2BsOfdmaUlAmcAlloPhyBandsBitmap_Object = MibTableColumn
wmanIf2BsOfdmaUlAmcAlloPhyBandsBitmap = _WmanIf2BsOfdmaUlAmcAlloPhyBandsBitmap_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 19),
    _WmanIf2BsOfdmaUlAmcAlloPhyBandsBitmap_Type()
)
wmanIf2BsOfdmaUlAmcAlloPhyBandsBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaUlAmcAlloPhyBandsBitmap.setStatus("current")


class _WmanIf2BsOfdmaMaxRetransmission_Type(Integer32):
    """Custom type wmanIf2BsOfdmaMaxRetransmission based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WmanIf2BsOfdmaMaxRetransmission_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaMaxRetransmission_Object = MibTableColumn
wmanIf2BsOfdmaMaxRetransmission = _WmanIf2BsOfdmaMaxRetransmission_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 20),
    _WmanIf2BsOfdmaMaxRetransmission_Type()
)
wmanIf2BsOfdmaMaxRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaMaxRetransmission.setStatus("current")


class _WmanIf2BsOfdmaNormalizedCnOverride_Type(OctetString):
    """Custom type wmanIf2BsOfdmaNormalizedCnOverride based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_WmanIf2BsOfdmaNormalizedCnOverride_Type.__name__ = "OctetString"
_WmanIf2BsOfdmaNormalizedCnOverride_Object = MibTableColumn
wmanIf2BsOfdmaNormalizedCnOverride = _WmanIf2BsOfdmaNormalizedCnOverride_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 21),
    _WmanIf2BsOfdmaNormalizedCnOverride_Type()
)
wmanIf2BsOfdmaNormalizedCnOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaNormalizedCnOverride.setStatus("current")


class _WmanIf2BsOfdmaSizeOfCqichId_Type(Integer32):
    """Custom type wmanIf2BsOfdmaSizeOfCqichId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2BsOfdmaSizeOfCqichId_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaSizeOfCqichId_Object = MibTableColumn
wmanIf2BsOfdmaSizeOfCqichId = _WmanIf2BsOfdmaSizeOfCqichId_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 22),
    _WmanIf2BsOfdmaSizeOfCqichId_Type()
)
wmanIf2BsOfdmaSizeOfCqichId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaSizeOfCqichId.setStatus("current")


class _WmanIf2BsOfdmaNormalizedCnValue_Type(Integer32):
    """Custom type wmanIf2BsOfdmaNormalizedCnValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_WmanIf2BsOfdmaNormalizedCnValue_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaNormalizedCnValue_Object = MibTableColumn
wmanIf2BsOfdmaNormalizedCnValue = _WmanIf2BsOfdmaNormalizedCnValue_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 23),
    _WmanIf2BsOfdmaNormalizedCnValue_Type()
)
wmanIf2BsOfdmaNormalizedCnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaNormalizedCnValue.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaNormalizedCnValue.setUnits("dB")


class _WmanIf2BsOfdmaNormalizedCnOverride2_Type(OctetString):
    """Custom type wmanIf2BsOfdmaNormalizedCnOverride2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixedLength = 7


_WmanIf2BsOfdmaNormalizedCnOverride2_Type.__name__ = "OctetString"
_WmanIf2BsOfdmaNormalizedCnOverride2_Object = MibTableColumn
wmanIf2BsOfdmaNormalizedCnOverride2 = _WmanIf2BsOfdmaNormalizedCnOverride2_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 24),
    _WmanIf2BsOfdmaNormalizedCnOverride2_Type()
)
wmanIf2BsOfdmaNormalizedCnOverride2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaNormalizedCnOverride2.setStatus("current")


class _WmanIf2BsOfdmaBandAmcEntryAvgCinr_Type(Integer32):
    """Custom type wmanIf2BsOfdmaBandAmcEntryAvgCinr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_WmanIf2BsOfdmaBandAmcEntryAvgCinr_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaBandAmcEntryAvgCinr_Object = MibTableColumn
wmanIf2BsOfdmaBandAmcEntryAvgCinr = _WmanIf2BsOfdmaBandAmcEntryAvgCinr_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 25),
    _WmanIf2BsOfdmaBandAmcEntryAvgCinr_Type()
)
wmanIf2BsOfdmaBandAmcEntryAvgCinr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBandAmcEntryAvgCinr.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBandAmcEntryAvgCinr.setUnits("dB")


class _WmanIf2BsOfdmaAasPreambleUpperBond_Type(Integer32):
    """Custom type wmanIf2BsOfdmaAasPreambleUpperBond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_WmanIf2BsOfdmaAasPreambleUpperBond_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaAasPreambleUpperBond_Object = MibTableColumn
wmanIf2BsOfdmaAasPreambleUpperBond = _WmanIf2BsOfdmaAasPreambleUpperBond_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 26),
    _WmanIf2BsOfdmaAasPreambleUpperBond_Type()
)
wmanIf2BsOfdmaAasPreambleUpperBond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaAasPreambleUpperBond.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaAasPreambleUpperBond.setUnits("0.25 dB")


class _WmanIf2BsOfdmaAasPreambleLowerBond_Type(Integer32):
    """Custom type wmanIf2BsOfdmaAasPreambleLowerBond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_WmanIf2BsOfdmaAasPreambleLowerBond_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaAasPreambleLowerBond_Object = MibTableColumn
wmanIf2BsOfdmaAasPreambleLowerBond = _WmanIf2BsOfdmaAasPreambleLowerBond_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 27),
    _WmanIf2BsOfdmaAasPreambleLowerBond_Type()
)
wmanIf2BsOfdmaAasPreambleLowerBond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaAasPreambleLowerBond.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaAasPreambleLowerBond.setUnits("0.25 dB")


class _WmanIf2BsOfdmaAasBeamSelectAllowed_Type(WmanIf2AasBeamSel):
    """Custom type wmanIf2BsOfdmaAasBeamSelectAllowed based on WmanIf2AasBeamSel"""
    defaultValue = 1


_WmanIf2BsOfdmaAasBeamSelectAllowed_Type.__name__ = "WmanIf2AasBeamSel"
_WmanIf2BsOfdmaAasBeamSelectAllowed_Object = MibTableColumn
wmanIf2BsOfdmaAasBeamSelectAllowed = _WmanIf2BsOfdmaAasBeamSelectAllowed_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 28),
    _WmanIf2BsOfdmaAasBeamSelectAllowed_Type()
)
wmanIf2BsOfdmaAasBeamSelectAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaAasBeamSelectAllowed.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaAasBeamSelectAllowed.setUnits("0.25 dB")


class _WmanIf2BsOfdmaCqichIndicationFlag_Type(OctetString):
    """Custom type wmanIf2BsOfdmaCqichIndicationFlag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_WmanIf2BsOfdmaCqichIndicationFlag_Type.__name__ = "OctetString"
_WmanIf2BsOfdmaCqichIndicationFlag_Object = MibTableColumn
wmanIf2BsOfdmaCqichIndicationFlag = _WmanIf2BsOfdmaCqichIndicationFlag_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 29),
    _WmanIf2BsOfdmaCqichIndicationFlag_Type()
)
wmanIf2BsOfdmaCqichIndicationFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCqichIndicationFlag.setStatus("current")
_WmanIf2BsOfdmaUpPowerAdjStep_Type = Unsigned32
_WmanIf2BsOfdmaUpPowerAdjStep_Object = MibTableColumn
wmanIf2BsOfdmaUpPowerAdjStep = _WmanIf2BsOfdmaUpPowerAdjStep_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 30),
    _WmanIf2BsOfdmaUpPowerAdjStep_Type()
)
wmanIf2BsOfdmaUpPowerAdjStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaUpPowerAdjStep.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaUpPowerAdjStep.setUnits("0.01 dB")
_WmanIf2BsOfdmaDownPowerAdjStep_Type = Unsigned32
_WmanIf2BsOfdmaDownPowerAdjStep_Object = MibTableColumn
wmanIf2BsOfdmaDownPowerAdjStep = _WmanIf2BsOfdmaDownPowerAdjStep_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 31),
    _WmanIf2BsOfdmaDownPowerAdjStep_Type()
)
wmanIf2BsOfdmaDownPowerAdjStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDownPowerAdjStep.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDownPowerAdjStep.setUnits("0.01 dB")
_WmanIf2BsOfdmaMinPowerOffsetAdj_Type = Integer32
_WmanIf2BsOfdmaMinPowerOffsetAdj_Object = MibTableColumn
wmanIf2BsOfdmaMinPowerOffsetAdj = _WmanIf2BsOfdmaMinPowerOffsetAdj_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 32),
    _WmanIf2BsOfdmaMinPowerOffsetAdj_Type()
)
wmanIf2BsOfdmaMinPowerOffsetAdj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaMinPowerOffsetAdj.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaMinPowerOffsetAdj.setUnits("0.1 dB")
_WmanIf2BsOfdmaMaxPowerOffsetAdj_Type = Integer32
_WmanIf2BsOfdmaMaxPowerOffsetAdj_Object = MibTableColumn
wmanIf2BsOfdmaMaxPowerOffsetAdj = _WmanIf2BsOfdmaMaxPowerOffsetAdj_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 33),
    _WmanIf2BsOfdmaMaxPowerOffsetAdj_Type()
)
wmanIf2BsOfdmaMaxPowerOffsetAdj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaMaxPowerOffsetAdj.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaMaxPowerOffsetAdj.setUnits("0.1 dB")


class _WmanIf2BsOfdmaHandoverRngCodes_Type(Integer32):
    """Custom type wmanIf2BsOfdmaHandoverRngCodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaHandoverRngCodes_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaHandoverRngCodes_Object = MibTableColumn
wmanIf2BsOfdmaHandoverRngCodes = _WmanIf2BsOfdmaHandoverRngCodes_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 34),
    _WmanIf2BsOfdmaHandoverRngCodes_Type()
)
wmanIf2BsOfdmaHandoverRngCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaHandoverRngCodes.setStatus("current")
_WmanIf2BsOfdmaInitialRngInterval_Type = Integer32
_WmanIf2BsOfdmaInitialRngInterval_Object = MibTableColumn
wmanIf2BsOfdmaInitialRngInterval = _WmanIf2BsOfdmaInitialRngInterval_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 35),
    _WmanIf2BsOfdmaInitialRngInterval_Type()
)
wmanIf2BsOfdmaInitialRngInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaInitialRngInterval.setStatus("current")


class _WmanIf2BsOfdmaTxPwrRepThreshold_Type(Integer32):
    """Custom type wmanIf2BsOfdmaTxPwrRepThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaTxPwrRepThreshold_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaTxPwrRepThreshold_Object = MibTableColumn
wmanIf2BsOfdmaTxPwrRepThreshold = _WmanIf2BsOfdmaTxPwrRepThreshold_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 36),
    _WmanIf2BsOfdmaTxPwrRepThreshold_Type()
)
wmanIf2BsOfdmaTxPwrRepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaTxPwrRepThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaTxPwrRepThreshold.setUnits("dB")


class _WmanIf2BsOfdmaTprPower_Type(Integer32):
    """Custom type wmanIf2BsOfdmaTprPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaTprPower_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaTprPower_Object = MibTableColumn
wmanIf2BsOfdmaTprPower = _WmanIf2BsOfdmaTprPower_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 37),
    _WmanIf2BsOfdmaTprPower_Type()
)
wmanIf2BsOfdmaTprPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaTprPower.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaTprPower.setUnits("dB")


class _WmanIf2BsOfdmaAlphaPavg_Type(Integer32):
    """Custom type wmanIf2BsOfdmaAlphaPavg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaAlphaPavg_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaAlphaPavg_Object = MibTableColumn
wmanIf2BsOfdmaAlphaPavg = _WmanIf2BsOfdmaAlphaPavg_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 38),
    _WmanIf2BsOfdmaAlphaPavg_Type()
)
wmanIf2BsOfdmaAlphaPavg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaAlphaPavg.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaAlphaPavg.setUnits("dB")


class _WmanIf2BsOfdmaCqichTxPwrRepThreshold_Type(Integer32):
    """Custom type wmanIf2BsOfdmaCqichTxPwrRepThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaCqichTxPwrRepThreshold_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaCqichTxPwrRepThreshold_Object = MibTableColumn
wmanIf2BsOfdmaCqichTxPwrRepThreshold = _WmanIf2BsOfdmaCqichTxPwrRepThreshold_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 39),
    _WmanIf2BsOfdmaCqichTxPwrRepThreshold_Type()
)
wmanIf2BsOfdmaCqichTxPwrRepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCqichTxPwrRepThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCqichTxPwrRepThreshold.setUnits("dB")


class _WmanIf2BsOfdmaCqichTprPower_Type(Integer32):
    """Custom type wmanIf2BsOfdmaCqichTprPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaCqichTprPower_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaCqichTprPower_Object = MibTableColumn
wmanIf2BsOfdmaCqichTprPower = _WmanIf2BsOfdmaCqichTprPower_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 40),
    _WmanIf2BsOfdmaCqichTprPower_Type()
)
wmanIf2BsOfdmaCqichTprPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCqichTprPower.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCqichTprPower.setUnits("dB")


class _WmanIf2BsOfdmaCqichAlphaPavg_Type(Integer32):
    """Custom type wmanIf2BsOfdmaCqichAlphaPavg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaCqichAlphaPavg_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaCqichAlphaPavg_Object = MibTableColumn
wmanIf2BsOfdmaCqichAlphaPavg = _WmanIf2BsOfdmaCqichAlphaPavg_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 41),
    _WmanIf2BsOfdmaCqichAlphaPavg_Type()
)
wmanIf2BsOfdmaCqichAlphaPavg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCqichAlphaPavg.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCqichAlphaPavg.setUnits("dB")
_WmanIf2BsOfdmaNormalizedCnChSounding_Type = Integer32
_WmanIf2BsOfdmaNormalizedCnChSounding_Object = MibTableColumn
wmanIf2BsOfdmaNormalizedCnChSounding = _WmanIf2BsOfdmaNormalizedCnChSounding_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 42),
    _WmanIf2BsOfdmaNormalizedCnChSounding_Type()
)
wmanIf2BsOfdmaNormalizedCnChSounding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaNormalizedCnChSounding.setStatus("current")


class _WmanIf2BsOfdmaInitialRngBackoffStart_Type(Integer32):
    """Custom type wmanIf2BsOfdmaInitialRngBackoffStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaInitialRngBackoffStart_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaInitialRngBackoffStart_Object = MibTableColumn
wmanIf2BsOfdmaInitialRngBackoffStart = _WmanIf2BsOfdmaInitialRngBackoffStart_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 43),
    _WmanIf2BsOfdmaInitialRngBackoffStart_Type()
)
wmanIf2BsOfdmaInitialRngBackoffStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaInitialRngBackoffStart.setStatus("current")


class _WmanIf2BsOfdmaInitialRngBackoffEnd_Type(Integer32):
    """Custom type wmanIf2BsOfdmaInitialRngBackoffEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaInitialRngBackoffEnd_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaInitialRngBackoffEnd_Object = MibTableColumn
wmanIf2BsOfdmaInitialRngBackoffEnd = _WmanIf2BsOfdmaInitialRngBackoffEnd_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 44),
    _WmanIf2BsOfdmaInitialRngBackoffEnd_Type()
)
wmanIf2BsOfdmaInitialRngBackoffEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaInitialRngBackoffEnd.setStatus("current")


class _WmanIf2BsOfdmaBwRequestBackoffStart_Type(Integer32):
    """Custom type wmanIf2BsOfdmaBwRequestBackoffStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaBwRequestBackoffStart_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaBwRequestBackoffStart_Object = MibTableColumn
wmanIf2BsOfdmaBwRequestBackoffStart = _WmanIf2BsOfdmaBwRequestBackoffStart_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 45),
    _WmanIf2BsOfdmaBwRequestBackoffStart_Type()
)
wmanIf2BsOfdmaBwRequestBackoffStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBwRequestBackoffStart.setStatus("current")


class _WmanIf2BsOfdmaBwRequestBackoffEnd_Type(Integer32):
    """Custom type wmanIf2BsOfdmaBwRequestBackoffEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaBwRequestBackoffEnd_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaBwRequestBackoffEnd_Object = MibTableColumn
wmanIf2BsOfdmaBwRequestBackoffEnd = _WmanIf2BsOfdmaBwRequestBackoffEnd_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 1, 1, 46),
    _WmanIf2BsOfdmaBwRequestBackoffEnd_Type()
)
wmanIf2BsOfdmaBwRequestBackoffEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaBwRequestBackoffEnd.setStatus("current")
_WmanIf2BsOfdmaDownlinkChannelTable_Object = MibTable
wmanIf2BsOfdmaDownlinkChannelTable = _WmanIf2BsOfdmaDownlinkChannelTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 2)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDownlinkChannelTable.setStatus("current")
_WmanIf2BsOfdmaDownlinkChannelEntry_Object = MibTableRow
wmanIf2BsOfdmaDownlinkChannelEntry = _WmanIf2BsOfdmaDownlinkChannelEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 2, 1)
)
wmanIf2BsOfdmaDownlinkChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDownlinkChannelEntry.setStatus("current")


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
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 2, 1, 1),
    _WmanIf2BsOfdmaFrameDurationCode_Type()
)
wmanIf2BsOfdmaFrameDurationCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaFrameDurationCode.setStatus("current")
_WmanIf2BsOfdmaFftSize_Type = WmanIf2OfdmaFftSize
_WmanIf2BsOfdmaFftSize_Object = MibTableColumn
wmanIf2BsOfdmaFftSize = _WmanIf2BsOfdmaFftSize_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 2, 1, 2),
    _WmanIf2BsOfdmaFftSize_Type()
)
wmanIf2BsOfdmaFftSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaFftSize.setStatus("current")
_WmanIf2BsOfdmaHARQAckDelayULBurst_Type = WmanIf2HarqAckDelay
_WmanIf2BsOfdmaHARQAckDelayULBurst_Object = MibTableColumn
wmanIf2BsOfdmaHARQAckDelayULBurst = _WmanIf2BsOfdmaHARQAckDelayULBurst_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 2, 1, 3),
    _WmanIf2BsOfdmaHARQAckDelayULBurst_Type()
)
wmanIf2BsOfdmaHARQAckDelayULBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaHARQAckDelayULBurst.setStatus("current")
_WmanIf2BsOfdmaHarqZonePermutation_Type = WmanIfPermutationType
_WmanIf2BsOfdmaHarqZonePermutation_Object = MibTableColumn
wmanIf2BsOfdmaHarqZonePermutation = _WmanIf2BsOfdmaHarqZonePermutation_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 2, 1, 4),
    _WmanIf2BsOfdmaHarqZonePermutation_Type()
)
wmanIf2BsOfdmaHarqZonePermutation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaHarqZonePermutation.setStatus("current")


class _WmanIf2BsOfdmaHMaxRetransmission_Type(Integer32):
    """Custom type wmanIf2BsOfdmaHMaxRetransmission based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaHMaxRetransmission_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaHMaxRetransmission_Object = MibTableColumn
wmanIf2BsOfdmaHMaxRetransmission = _WmanIf2BsOfdmaHMaxRetransmission_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 2, 1, 5),
    _WmanIf2BsOfdmaHMaxRetransmission_Type()
)
wmanIf2BsOfdmaHMaxRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaHMaxRetransmission.setStatus("current")


class _WmanIf2BsOfdmaCinrAlphaAvg_Type(Integer32):
    """Custom type wmanIf2BsOfdmaCinrAlphaAvg based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaCinrAlphaAvg_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaCinrAlphaAvg_Object = MibTableColumn
wmanIf2BsOfdmaCinrAlphaAvg = _WmanIf2BsOfdmaCinrAlphaAvg_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 2, 1, 6),
    _WmanIf2BsOfdmaCinrAlphaAvg_Type()
)
wmanIf2BsOfdmaCinrAlphaAvg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaCinrAlphaAvg.setStatus("current")


class _WmanIf2BsOfdmaRssiAlphaAvg_Type(Integer32):
    """Custom type wmanIf2BsOfdmaRssiAlphaAvg based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaRssiAlphaAvg_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaRssiAlphaAvg_Object = MibTableColumn
wmanIf2BsOfdmaRssiAlphaAvg = _WmanIf2BsOfdmaRssiAlphaAvg_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 2, 1, 7),
    _WmanIf2BsOfdmaRssiAlphaAvg_Type()
)
wmanIf2BsOfdmaRssiAlphaAvg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaRssiAlphaAvg.setStatus("current")


class _WmanIf2BsOfdmaDlAmcAlloPhyBandsBitmap_Type(OctetString):
    """Custom type wmanIf2BsOfdmaDlAmcAlloPhyBandsBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6


_WmanIf2BsOfdmaDlAmcAlloPhyBandsBitmap_Type.__name__ = "OctetString"
_WmanIf2BsOfdmaDlAmcAlloPhyBandsBitmap_Object = MibTableColumn
wmanIf2BsOfdmaDlAmcAlloPhyBandsBitmap = _WmanIf2BsOfdmaDlAmcAlloPhyBandsBitmap_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 2, 1, 8),
    _WmanIf2BsOfdmaDlAmcAlloPhyBandsBitmap_Type()
)
wmanIf2BsOfdmaDlAmcAlloPhyBandsBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDlAmcAlloPhyBandsBitmap.setStatus("current")
_WmanIf2BsOfdmaHandoverSupported_Type = WmanIf2HoSupportType
_WmanIf2BsOfdmaHandoverSupported_Object = MibTableColumn
wmanIf2BsOfdmaHandoverSupported = _WmanIf2BsOfdmaHandoverSupported_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 2, 1, 9),
    _WmanIf2BsOfdmaHandoverSupported_Type()
)
wmanIf2BsOfdmaHandoverSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaHandoverSupported.setStatus("current")


class _WmanIf2BsOfdmaThresholdAddBsDivSet_Type(Integer32):
    """Custom type wmanIf2BsOfdmaThresholdAddBsDivSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaThresholdAddBsDivSet_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaThresholdAddBsDivSet_Object = MibTableColumn
wmanIf2BsOfdmaThresholdAddBsDivSet = _WmanIf2BsOfdmaThresholdAddBsDivSet_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 2, 1, 10),
    _WmanIf2BsOfdmaThresholdAddBsDivSet_Type()
)
wmanIf2BsOfdmaThresholdAddBsDivSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaThresholdAddBsDivSet.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaThresholdAddBsDivSet.setUnits("dB")


class _WmanIf2BsOfdmaThresholdDelBsDivSet_Type(Integer32):
    """Custom type wmanIf2BsOfdmaThresholdDelBsDivSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaThresholdDelBsDivSet_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaThresholdDelBsDivSet_Object = MibTableColumn
wmanIf2BsOfdmaThresholdDelBsDivSet = _WmanIf2BsOfdmaThresholdDelBsDivSet_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 2, 1, 12),
    _WmanIf2BsOfdmaThresholdDelBsDivSet_Type()
)
wmanIf2BsOfdmaThresholdDelBsDivSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaThresholdDelBsDivSet.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaThresholdDelBsDivSet.setUnits("dB")


class _WmanIf2BsOfdmaAsrSlotLength_Type(Integer32):
    """Custom type wmanIf2BsOfdmaAsrSlotLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaAsrSlotLength_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaAsrSlotLength_Object = MibTableColumn
wmanIf2BsOfdmaAsrSlotLength = _WmanIf2BsOfdmaAsrSlotLength_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 2, 1, 13),
    _WmanIf2BsOfdmaAsrSlotLength_Type()
)
wmanIf2BsOfdmaAsrSlotLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaAsrSlotLength.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaAsrSlotLength.setUnits("Frames")


class _WmanIf2BsOfdmaAsrSwitchingPeriod_Type(Integer32):
    """Custom type wmanIf2BsOfdmaAsrSwitchingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsOfdmaAsrSwitchingPeriod_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaAsrSwitchingPeriod_Object = MibTableColumn
wmanIf2BsOfdmaAsrSwitchingPeriod = _WmanIf2BsOfdmaAsrSwitchingPeriod_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 2, 1, 14),
    _WmanIf2BsOfdmaAsrSwitchingPeriod_Type()
)
wmanIf2BsOfdmaAsrSwitchingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaAsrSwitchingPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaAsrSwitchingPeriod.setUnits("ASR slots")


class _WmanIf2BsOfdmaHysteresisMargin_Type(Integer32):
    """Custom type wmanIf2BsOfdmaHysteresisMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 57),
    )


_WmanIf2BsOfdmaHysteresisMargin_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaHysteresisMargin_Object = MibTableColumn
wmanIf2BsOfdmaHysteresisMargin = _WmanIf2BsOfdmaHysteresisMargin_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 2, 1, 15),
    _WmanIf2BsOfdmaHysteresisMargin_Type()
)
wmanIf2BsOfdmaHysteresisMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaHysteresisMargin.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaHysteresisMargin.setUnits("dB")
_WmanIf2BsOfdmaTimeToTrigger_Type = Integer32
_WmanIf2BsOfdmaTimeToTrigger_Object = MibTableColumn
wmanIf2BsOfdmaTimeToTrigger = _WmanIf2BsOfdmaTimeToTrigger_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 2, 1, 16),
    _WmanIf2BsOfdmaTimeToTrigger_Type()
)
wmanIf2BsOfdmaTimeToTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaTimeToTrigger.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaTimeToTrigger.setUnits("milliseconds")


class _WmanIf2BsOfdmaRestartCount_Type(Integer32):
    """Custom type wmanIf2BsOfdmaRestartCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2BsOfdmaRestartCount_Type.__name__ = "Integer32"
_WmanIf2BsOfdmaRestartCount_Object = MibTableColumn
wmanIf2BsOfdmaRestartCount = _WmanIf2BsOfdmaRestartCount_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 2, 1, 17),
    _WmanIf2BsOfdmaRestartCount_Type()
)
wmanIf2BsOfdmaRestartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaRestartCount.setStatus("current")
_WmanIf2BsOfdmaUcdBurstProfileTable_Object = MibTable
wmanIf2BsOfdmaUcdBurstProfileTable = _WmanIf2BsOfdmaUcdBurstProfileTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 3)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaUcdBurstProfileTable.setStatus("current")
_WmanIf2BsOfdmaUcdBurstProfileEntry_Object = MibTableRow
wmanIf2BsOfdmaUcdBurstProfileEntry = _WmanIf2BsOfdmaUcdBurstProfileEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 3, 1)
)
wmanIf2BsOfdmaUcdBurstProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsOfdmaUiucIndex"),
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
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 3, 1, 1),
    _WmanIf2BsOfdmaUiucIndex_Type()
)
wmanIf2BsOfdmaUiucIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaUiucIndex.setStatus("current")
_WmanIf2BsOfdmaUcdFecCodeType_Type = WmanIf2OfdmaUcdFecCode
_WmanIf2BsOfdmaUcdFecCodeType_Object = MibTableColumn
wmanIf2BsOfdmaUcdFecCodeType = _WmanIf2BsOfdmaUcdFecCodeType_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 3, 1, 2),
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
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 3, 1, 3),
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
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 3, 1, 5),
    _WmanIf2BsOfdmaUcdBurstProfileRowStatus_Type()
)
wmanIf2BsOfdmaUcdBurstProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaUcdBurstProfileRowStatus.setStatus("current")
_WmanIf2BsOfdmaDcdBurstProfileTable_Object = MibTable
wmanIf2BsOfdmaDcdBurstProfileTable = _WmanIf2BsOfdmaDcdBurstProfileTable_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 4)
)
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDcdBurstProfileTable.setStatus("current")
_WmanIf2BsOfdmaDcdBurstProfileEntry_Object = MibTableRow
wmanIf2BsOfdmaDcdBurstProfileEntry = _WmanIf2BsOfdmaDcdBurstProfileEntry_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 4, 1)
)
wmanIf2BsOfdmaDcdBurstProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsOfdmaDiucIndex"),
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
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 4, 1, 1),
    _WmanIf2BsOfdmaDiucIndex_Type()
)
wmanIf2BsOfdmaDiucIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDiucIndex.setStatus("current")
_WmanIf2BsOfdmaDcdFecCodeType_Type = WmanIf2OfdmaDcdFecCode
_WmanIf2BsOfdmaDcdFecCodeType_Object = MibTableColumn
wmanIf2BsOfdmaDcdFecCodeType = _WmanIf2BsOfdmaDcdFecCodeType_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 4, 1, 2),
    _WmanIf2BsOfdmaDcdFecCodeType_Type()
)
wmanIf2BsOfdmaDcdFecCodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDcdFecCodeType.setStatus("current")
_WmanIf2BsOfdmaDcdBurstProfileRowStatus_Type = RowStatus
_WmanIf2BsOfdmaDcdBurstProfileRowStatus_Object = MibTableColumn
wmanIf2BsOfdmaDcdBurstProfileRowStatus = _WmanIf2BsOfdmaDcdBurstProfileRowStatus_Object(
    (1, 0, 8802, 16, 2, 1, 2, 9, 3, 4, 1, 3),
    _WmanIf2BsOfdmaDcdBurstProfileRowStatus_Type()
)
wmanIf2BsOfdmaDcdBurstProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsOfdmaDcdBurstProfileRowStatus.setStatus("current")
_WmanIf2BsAm_ObjectIdentity = ObjectIdentity
wmanIf2BsAm = _WmanIf2BsAm_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 3)
)
_WmanIf2BsOtaUsageDataRecordTable_Object = MibTable
wmanIf2BsOtaUsageDataRecordTable = _WmanIf2BsOtaUsageDataRecordTable_Object(
    (1, 0, 8802, 16, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsOtaUsageDataRecordTable.setStatus("current")
_WmanIf2BsOtaUsageDataRecordEntry_Object = MibTableRow
wmanIf2BsOtaUsageDataRecordEntry = _WmanIf2BsOtaUsageDataRecordEntry_Object(
    (1, 0, 8802, 16, 2, 1, 3, 1, 1)
)
wmanIf2BsOtaUsageDataRecordEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsSsMacAddress"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsCid"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsSessionId"),
)
if mibBuilder.loadTexts:
    wmanIf2BsOtaUsageDataRecordEntry.setStatus("current")


class _WmanIf2BsSessionId_Type(Unsigned32):
    """Custom type wmanIf2BsSessionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIf2BsSessionId_Type.__name__ = "Unsigned32"
_WmanIf2BsSessionId_Object = MibTableColumn
wmanIf2BsSessionId = _WmanIf2BsSessionId_Object(
    (1, 0, 8802, 16, 2, 1, 3, 1, 1, 1),
    _WmanIf2BsSessionId_Type()
)
wmanIf2BsSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsSessionId.setStatus("current")


class _WmanIf2BsCid_Type(Integer32):
    """Custom type wmanIf2BsCid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsCid_Type.__name__ = "Integer32"
_WmanIf2BsCid_Object = MibTableColumn
wmanIf2BsCid = _WmanIf2BsCid_Object(
    (1, 0, 8802, 16, 2, 1, 3, 1, 1, 2),
    _WmanIf2BsCid_Type()
)
wmanIf2BsCid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsCid.setStatus("current")


class _WmanIf2BsServiceFlowId_Type(Unsigned32):
    """Custom type wmanIf2BsServiceFlowId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIf2BsServiceFlowId_Type.__name__ = "Unsigned32"
_WmanIf2BsServiceFlowId_Object = MibTableColumn
wmanIf2BsServiceFlowId = _WmanIf2BsServiceFlowId_Object(
    (1, 0, 8802, 16, 2, 1, 3, 1, 1, 3),
    _WmanIf2BsServiceFlowId_Type()
)
wmanIf2BsServiceFlowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsServiceFlowId.setStatus("current")
_WmanIf2BsMacSduCount_Type = Counter64
_WmanIf2BsMacSduCount_Object = MibTableColumn
wmanIf2BsMacSduCount = _WmanIf2BsMacSduCount_Object(
    (1, 0, 8802, 16, 2, 1, 3, 1, 1, 4),
    _WmanIf2BsMacSduCount_Type()
)
wmanIf2BsMacSduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsMacSduCount.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsMacSduCount.setUnits("SDU")
_WmanIf2BsOctetCount_Type = Counter64
_WmanIf2BsOctetCount_Object = MibTableColumn
wmanIf2BsOctetCount = _WmanIf2BsOctetCount_Object(
    (1, 0, 8802, 16, 2, 1, 3, 1, 1, 5),
    _WmanIf2BsOctetCount_Type()
)
wmanIf2BsOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsOctetCount.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsOctetCount.setUnits("Octet")
_WmanIf2BsSessionEstablishTime_Type = TimeStamp
_WmanIf2BsSessionEstablishTime_Object = MibTableColumn
wmanIf2BsSessionEstablishTime = _WmanIf2BsSessionEstablishTime_Object(
    (1, 0, 8802, 16, 2, 1, 3, 1, 1, 6),
    _WmanIf2BsSessionEstablishTime_Type()
)
wmanIf2BsSessionEstablishTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSessionEstablishTime.setStatus("current")
_WmanIf2BsSessionTerminateTime_Type = TimeStamp
_WmanIf2BsSessionTerminateTime_Object = MibTableColumn
wmanIf2BsSessionTerminateTime = _WmanIf2BsSessionTerminateTime_Object(
    (1, 0, 8802, 16, 2, 1, 3, 1, 1, 7),
    _WmanIf2BsSessionTerminateTime_Type()
)
wmanIf2BsSessionTerminateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSessionTerminateTime.setStatus("current")
_WmanIf2BsGlobalServiceClass_Type = WmanIf2GlobalSrvClass
_WmanIf2BsGlobalServiceClass_Object = MibTableColumn
wmanIf2BsGlobalServiceClass = _WmanIf2BsGlobalServiceClass_Object(
    (1, 0, 8802, 16, 2, 1, 3, 1, 1, 8),
    _WmanIf2BsGlobalServiceClass_Type()
)
wmanIf2BsGlobalServiceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsGlobalServiceClass.setStatus("current")


class _WmanIf2BsQoSProfileIndex_Type(Integer32):
    """Custom type wmanIf2BsQoSProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2BsQoSProfileIndex_Type.__name__ = "Integer32"
_WmanIf2BsQoSProfileIndex_Object = MibTableColumn
wmanIf2BsQoSProfileIndex = _WmanIf2BsQoSProfileIndex_Object(
    (1, 0, 8802, 16, 2, 1, 3, 1, 1, 9),
    _WmanIf2BsQoSProfileIndex_Type()
)
wmanIf2BsQoSProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsQoSProfileIndex.setStatus("current")
_WmanIf2BsPm_ObjectIdentity = ObjectIdentity
wmanIf2BsPm = _WmanIf2BsPm_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 4)
)
_WmanIf2BsChannelMeasurementTable_Object = MibTable
wmanIf2BsChannelMeasurementTable = _WmanIf2BsChannelMeasurementTable_Object(
    (1, 0, 8802, 16, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsChannelMeasurementTable.setStatus("current")
_WmanIf2BsChannelMeasurementEntry_Object = MibTableRow
wmanIf2BsChannelMeasurementEntry = _WmanIf2BsChannelMeasurementEntry_Object(
    (1, 0, 8802, 16, 2, 1, 4, 1, 1)
)
wmanIf2BsChannelMeasurementEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsSsMacAddress"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsChannelDirection"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsHistogramIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsChannelMeasurementEntry.setStatus("current")
_WmanIf2BsChannelDirection_Type = WmanIf2LinkDirection
_WmanIf2BsChannelDirection_Object = MibTableColumn
wmanIf2BsChannelDirection = _WmanIf2BsChannelDirection_Object(
    (1, 0, 8802, 16, 2, 1, 4, 1, 1, 1),
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
    (1, 0, 8802, 16, 2, 1, 4, 1, 1, 2),
    _WmanIf2BsHistogramIndex_Type()
)
wmanIf2BsHistogramIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsHistogramIndex.setStatus("current")
_WmanIf2BsChannelNumber_Type = WmanIf2ChannelNumber
_WmanIf2BsChannelNumber_Object = MibTableColumn
wmanIf2BsChannelNumber = _WmanIf2BsChannelNumber_Object(
    (1, 0, 8802, 16, 2, 1, 4, 1, 1, 3),
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
    (1, 0, 8802, 16, 2, 1, 4, 1, 1, 4),
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
    (1, 0, 8802, 16, 2, 1, 4, 1, 1, 5),
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
    (1, 0, 8802, 16, 2, 1, 4, 1, 1, 6),
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
    (1, 0, 8802, 16, 2, 1, 4, 1, 1, 7),
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
    (1, 0, 8802, 16, 2, 1, 4, 1, 1, 8),
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
    (1, 0, 8802, 16, 2, 1, 4, 1, 1, 9),
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
    (1, 0, 8802, 16, 2, 1, 4, 1, 1, 10),
    _WmanIf2BsStdDeviationRssiReport_Type()
)
wmanIf2BsStdDeviationRssiReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsStdDeviationRssiReport.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsStdDeviationRssiReport.setUnits("dB")
_WmanIf2BsStatisticsConfigTable_Object = MibTable
wmanIf2BsStatisticsConfigTable = _WmanIf2BsStatisticsConfigTable_Object(
    (1, 0, 8802, 16, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    wmanIf2BsStatisticsConfigTable.setStatus("current")
_WmanIf2BsStatisticsConfigEntry_Object = MibTableRow
wmanIf2BsStatisticsConfigEntry = _WmanIf2BsStatisticsConfigEntry_Object(
    (1, 0, 8802, 16, 2, 1, 4, 2, 1)
)
wmanIf2BsStatisticsConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsStatisticsConfigEntry.setStatus("current")


class _WmanIf2BsDataSampleInterval_Type(Integer32):
    """Custom type wmanIf2BsDataSampleInterval based on Integer32"""
    defaultValue = 1


_WmanIf2BsDataSampleInterval_Type.__name__ = "Integer32"
_WmanIf2BsDataSampleInterval_Object = MibTableColumn
wmanIf2BsDataSampleInterval = _WmanIf2BsDataSampleInterval_Object(
    (1, 0, 8802, 16, 2, 1, 4, 2, 1, 1),
    _WmanIf2BsDataSampleInterval_Type()
)
wmanIf2BsDataSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsDataSampleInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsDataSampleInterval.setUnits("Seconds")


class _WmanIf2BsCountersReportInterval_Type(Integer32):
    """Custom type wmanIf2BsCountersReportInterval based on Integer32"""
    defaultValue = 15


_WmanIf2BsCountersReportInterval_Type.__name__ = "Integer32"
_WmanIf2BsCountersReportInterval_Object = MibTableColumn
wmanIf2BsCountersReportInterval = _WmanIf2BsCountersReportInterval_Object(
    (1, 0, 8802, 16, 2, 1, 4, 2, 1, 2),
    _WmanIf2BsCountersReportInterval_Type()
)
wmanIf2BsCountersReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsCountersReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsCountersReportInterval.setUnits("Minutes")
_WmanIf2BsSsStartupStatisticsTable_Object = MibTable
wmanIf2BsSsStartupStatisticsTable = _WmanIf2BsSsStartupStatisticsTable_Object(
    (1, 0, 8802, 16, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsStartupStatisticsTable.setStatus("current")
_WmanIf2BsSsStartupStatisticsEntry_Object = MibTableRow
wmanIf2BsSsStartupStatisticsEntry = _WmanIf2BsSsStartupStatisticsEntry_Object(
    (1, 0, 8802, 16, 2, 1, 4, 3, 1)
)
wmanIf2BsSsStartupStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsSsStartupStatisticsEntry.setStatus("current")
_WmanIf2BsSsAuthenAttempt_Type = Counter64
_WmanIf2BsSsAuthenAttempt_Object = MibTableColumn
wmanIf2BsSsAuthenAttempt = _WmanIf2BsSsAuthenAttempt_Object(
    (1, 0, 8802, 16, 2, 1, 4, 3, 1, 1),
    _WmanIf2BsSsAuthenAttempt_Type()
)
wmanIf2BsSsAuthenAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsAuthenAttempt.setStatus("current")
_WmanIf2BsSsAuthenSuccess_Type = Counter64
_WmanIf2BsSsAuthenSuccess_Object = MibTableColumn
wmanIf2BsSsAuthenSuccess = _WmanIf2BsSsAuthenSuccess_Object(
    (1, 0, 8802, 16, 2, 1, 4, 3, 1, 2),
    _WmanIf2BsSsAuthenSuccess_Type()
)
wmanIf2BsSsAuthenSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsAuthenSuccess.setStatus("current")
_WmanIf2BsSsAuthenSuccessRate_Type = Integer32
_WmanIf2BsSsAuthenSuccessRate_Object = MibTableColumn
wmanIf2BsSsAuthenSuccessRate = _WmanIf2BsSsAuthenSuccessRate_Object(
    (1, 0, 8802, 16, 2, 1, 4, 3, 1, 3),
    _WmanIf2BsSsAuthenSuccessRate_Type()
)
wmanIf2BsSsAuthenSuccessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsAuthenSuccessRate.setStatus("current")
_WmanIf2BsSsRangingAttempt_Type = Counter64
_WmanIf2BsSsRangingAttempt_Object = MibTableColumn
wmanIf2BsSsRangingAttempt = _WmanIf2BsSsRangingAttempt_Object(
    (1, 0, 8802, 16, 2, 1, 4, 3, 1, 4),
    _WmanIf2BsSsRangingAttempt_Type()
)
wmanIf2BsSsRangingAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRangingAttempt.setStatus("current")
_WmanIf2BsSsRangingSuccess_Type = Counter64
_WmanIf2BsSsRangingSuccess_Object = MibTableColumn
wmanIf2BsSsRangingSuccess = _WmanIf2BsSsRangingSuccess_Object(
    (1, 0, 8802, 16, 2, 1, 4, 3, 1, 5),
    _WmanIf2BsSsRangingSuccess_Type()
)
wmanIf2BsSsRangingSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRangingSuccess.setStatus("current")
_WmanIf2BsSsRangingSuccessRate_Type = Integer32
_WmanIf2BsSsRangingSuccessRate_Object = MibTableColumn
wmanIf2BsSsRangingSuccessRate = _WmanIf2BsSsRangingSuccessRate_Object(
    (1, 0, 8802, 16, 2, 1, 4, 3, 1, 6),
    _WmanIf2BsSsRangingSuccessRate_Type()
)
wmanIf2BsSsRangingSuccessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsRangingSuccessRate.setStatus("current")
_WmanIf2BsDataRateStatisticsTable_Object = MibTable
wmanIf2BsDataRateStatisticsTable = _WmanIf2BsDataRateStatisticsTable_Object(
    (1, 0, 8802, 16, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    wmanIf2BsDataRateStatisticsTable.setStatus("current")
_WmanIf2BsDataRateStatisticsEntry_Object = MibTableRow
wmanIf2BsDataRateStatisticsEntry = _WmanIf2BsDataRateStatisticsEntry_Object(
    (1, 0, 8802, 16, 2, 1, 4, 4, 1)
)
wmanIf2BsDataRateStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsDataRateStatisticsEntry.setStatus("current")
_WmanIf2BsAvgDlUserThroughput_Type = Counter32
_WmanIf2BsAvgDlUserThroughput_Object = MibTableColumn
wmanIf2BsAvgDlUserThroughput = _WmanIf2BsAvgDlUserThroughput_Object(
    (1, 0, 8802, 16, 2, 1, 4, 4, 1, 1),
    _WmanIf2BsAvgDlUserThroughput_Type()
)
wmanIf2BsAvgDlUserThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsAvgDlUserThroughput.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsAvgDlUserThroughput.setUnits("Octet")
_WmanIf2BsAvgUlUserThroughput_Type = Counter32
_WmanIf2BsAvgUlUserThroughput_Object = MibTableColumn
wmanIf2BsAvgUlUserThroughput = _WmanIf2BsAvgUlUserThroughput_Object(
    (1, 0, 8802, 16, 2, 1, 4, 4, 1, 2),
    _WmanIf2BsAvgUlUserThroughput_Type()
)
wmanIf2BsAvgUlUserThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsAvgUlUserThroughput.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsAvgUlUserThroughput.setUnits("Octet")
_WmanIf2BsAvgDlMacThroughput_Type = Counter32
_WmanIf2BsAvgDlMacThroughput_Object = MibTableColumn
wmanIf2BsAvgDlMacThroughput = _WmanIf2BsAvgDlMacThroughput_Object(
    (1, 0, 8802, 16, 2, 1, 4, 4, 1, 3),
    _WmanIf2BsAvgDlMacThroughput_Type()
)
wmanIf2BsAvgDlMacThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsAvgDlMacThroughput.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsAvgDlMacThroughput.setUnits("Octet")
_WmanIf2BsAvgUlMacThroughput_Type = Counter32
_WmanIf2BsAvgUlMacThroughput_Object = MibTableColumn
wmanIf2BsAvgUlMacThroughput = _WmanIf2BsAvgUlMacThroughput_Object(
    (1, 0, 8802, 16, 2, 1, 4, 4, 1, 4),
    _WmanIf2BsAvgUlMacThroughput_Type()
)
wmanIf2BsAvgUlMacThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsAvgUlMacThroughput.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsAvgUlMacThroughput.setUnits("Octet")
_WmanIf2BsAvgDlPhyThroughput_Type = Counter32
_WmanIf2BsAvgDlPhyThroughput_Object = MibTableColumn
wmanIf2BsAvgDlPhyThroughput = _WmanIf2BsAvgDlPhyThroughput_Object(
    (1, 0, 8802, 16, 2, 1, 4, 4, 1, 5),
    _WmanIf2BsAvgDlPhyThroughput_Type()
)
wmanIf2BsAvgDlPhyThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsAvgDlPhyThroughput.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsAvgDlPhyThroughput.setUnits("Octet")
_WmanIf2BsAvgUlPhyThroughput_Type = Counter32
_WmanIf2BsAvgUlPhyThroughput_Object = MibTableColumn
wmanIf2BsAvgUlPhyThroughput = _WmanIf2BsAvgUlPhyThroughput_Object(
    (1, 0, 8802, 16, 2, 1, 4, 4, 1, 6),
    _WmanIf2BsAvgUlPhyThroughput_Type()
)
wmanIf2BsAvgUlPhyThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsAvgUlPhyThroughput.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsAvgUlPhyThroughput.setUnits("Octet")
_WmanIf2BsPeakDlUserThroughput_Type = Counter32
_WmanIf2BsPeakDlUserThroughput_Object = MibTableColumn
wmanIf2BsPeakDlUserThroughput = _WmanIf2BsPeakDlUserThroughput_Object(
    (1, 0, 8802, 16, 2, 1, 4, 4, 1, 7),
    _WmanIf2BsPeakDlUserThroughput_Type()
)
wmanIf2BsPeakDlUserThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsPeakDlUserThroughput.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPeakDlUserThroughput.setUnits("Octet")
_WmanIf2BsPeakUlUserThroughput_Type = Counter32
_WmanIf2BsPeakUlUserThroughput_Object = MibTableColumn
wmanIf2BsPeakUlUserThroughput = _WmanIf2BsPeakUlUserThroughput_Object(
    (1, 0, 8802, 16, 2, 1, 4, 4, 1, 8),
    _WmanIf2BsPeakUlUserThroughput_Type()
)
wmanIf2BsPeakUlUserThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsPeakUlUserThroughput.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPeakUlUserThroughput.setUnits("Octet")
_WmanIf2BsPeakDlMacThroughput_Type = Counter32
_WmanIf2BsPeakDlMacThroughput_Object = MibTableColumn
wmanIf2BsPeakDlMacThroughput = _WmanIf2BsPeakDlMacThroughput_Object(
    (1, 0, 8802, 16, 2, 1, 4, 4, 1, 9),
    _WmanIf2BsPeakDlMacThroughput_Type()
)
wmanIf2BsPeakDlMacThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsPeakDlMacThroughput.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPeakDlMacThroughput.setUnits("Octet")
_WmanIf2BsPeakUlMacThroughput_Type = Counter32
_WmanIf2BsPeakUlMacThroughput_Object = MibTableColumn
wmanIf2BsPeakUlMacThroughput = _WmanIf2BsPeakUlMacThroughput_Object(
    (1, 0, 8802, 16, 2, 1, 4, 4, 1, 10),
    _WmanIf2BsPeakUlMacThroughput_Type()
)
wmanIf2BsPeakUlMacThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsPeakUlMacThroughput.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPeakUlMacThroughput.setUnits("Octet")
_WmanIf2BsPeakDlPhyThroughput_Type = Counter32
_WmanIf2BsPeakDlPhyThroughput_Object = MibTableColumn
wmanIf2BsPeakDlPhyThroughput = _WmanIf2BsPeakDlPhyThroughput_Object(
    (1, 0, 8802, 16, 2, 1, 4, 4, 1, 11),
    _WmanIf2BsPeakDlPhyThroughput_Type()
)
wmanIf2BsPeakDlPhyThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsPeakDlPhyThroughput.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPeakDlPhyThroughput.setUnits("Octet")
_WmanIf2BsPeakUlPhyThroughput_Type = Counter32
_WmanIf2BsPeakUlPhyThroughput_Object = MibTableColumn
wmanIf2BsPeakUlPhyThroughput = _WmanIf2BsPeakUlPhyThroughput_Object(
    (1, 0, 8802, 16, 2, 1, 4, 4, 1, 12),
    _WmanIf2BsPeakUlPhyThroughput_Type()
)
wmanIf2BsPeakUlPhyThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsPeakUlPhyThroughput.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPeakUlPhyThroughput.setUnits("Octet")
_WmanIf2BsAvgDlCellEdgeThroughput_Type = Counter32
_WmanIf2BsAvgDlCellEdgeThroughput_Object = MibTableColumn
wmanIf2BsAvgDlCellEdgeThroughput = _WmanIf2BsAvgDlCellEdgeThroughput_Object(
    (1, 0, 8802, 16, 2, 1, 4, 4, 1, 13),
    _WmanIf2BsAvgDlCellEdgeThroughput_Type()
)
wmanIf2BsAvgDlCellEdgeThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsAvgDlCellEdgeThroughput.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsAvgDlCellEdgeThroughput.setUnits("Octet")
_WmanIf2BsAvgUlCellEdgeThroughput_Type = Counter32
_WmanIf2BsAvgUlCellEdgeThroughput_Object = MibTableColumn
wmanIf2BsAvgUlCellEdgeThroughput = _WmanIf2BsAvgUlCellEdgeThroughput_Object(
    (1, 0, 8802, 16, 2, 1, 4, 4, 1, 14),
    _WmanIf2BsAvgUlCellEdgeThroughput_Type()
)
wmanIf2BsAvgUlCellEdgeThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsAvgUlCellEdgeThroughput.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsAvgUlCellEdgeThroughput.setUnits("Octet")
_WmanIf2BsDataRateMeasurements_Type = Counter64
_WmanIf2BsDataRateMeasurements_Object = MibTableColumn
wmanIf2BsDataRateMeasurements = _WmanIf2BsDataRateMeasurements_Object(
    (1, 0, 8802, 16, 2, 1, 4, 4, 1, 15),
    _WmanIf2BsDataRateMeasurements_Type()
)
wmanIf2BsDataRateMeasurements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsDataRateMeasurements.setStatus("current")
_WmanIf2BsNetworkEntryStatisticsTable_Object = MibTable
wmanIf2BsNetworkEntryStatisticsTable = _WmanIf2BsNetworkEntryStatisticsTable_Object(
    (1, 0, 8802, 16, 2, 1, 4, 5)
)
if mibBuilder.loadTexts:
    wmanIf2BsNetworkEntryStatisticsTable.setStatus("current")
_WmanIf2BsNetworkEntryStatisticsEntry_Object = MibTableRow
wmanIf2BsNetworkEntryStatisticsEntry = _WmanIf2BsNetworkEntryStatisticsEntry_Object(
    (1, 0, 8802, 16, 2, 1, 4, 5, 1)
)
wmanIf2BsNetworkEntryStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsNetworkEntryStatisticsEntry.setStatus("current")
_WmanIf2BsAvgNetworkEntryTime_Type = Integer32
_WmanIf2BsAvgNetworkEntryTime_Object = MibTableColumn
wmanIf2BsAvgNetworkEntryTime = _WmanIf2BsAvgNetworkEntryTime_Object(
    (1, 0, 8802, 16, 2, 1, 4, 5, 1, 1),
    _WmanIf2BsAvgNetworkEntryTime_Type()
)
wmanIf2BsAvgNetworkEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsAvgNetworkEntryTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsAvgNetworkEntryTime.setUnits("second")
_WmanIf2BsMaxNetworkEntryTime_Type = Integer32
_WmanIf2BsMaxNetworkEntryTime_Object = MibTableColumn
wmanIf2BsMaxNetworkEntryTime = _WmanIf2BsMaxNetworkEntryTime_Object(
    (1, 0, 8802, 16, 2, 1, 4, 5, 1, 2),
    _WmanIf2BsMaxNetworkEntryTime_Type()
)
wmanIf2BsMaxNetworkEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsMaxNetworkEntryTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsMaxNetworkEntryTime.setUnits("second")
_WmanIf2BsAvgNetworkReEntryTime_Type = Integer32
_WmanIf2BsAvgNetworkReEntryTime_Object = MibTableColumn
wmanIf2BsAvgNetworkReEntryTime = _WmanIf2BsAvgNetworkReEntryTime_Object(
    (1, 0, 8802, 16, 2, 1, 4, 5, 1, 3),
    _WmanIf2BsAvgNetworkReEntryTime_Type()
)
wmanIf2BsAvgNetworkReEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsAvgNetworkReEntryTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsAvgNetworkReEntryTime.setUnits("second")
_WmanIf2BsMaxNetworkReEntryTime_Type = Integer32
_WmanIf2BsMaxNetworkReEntryTime_Object = MibTableColumn
wmanIf2BsMaxNetworkReEntryTime = _WmanIf2BsMaxNetworkReEntryTime_Object(
    (1, 0, 8802, 16, 2, 1, 4, 5, 1, 4),
    _WmanIf2BsMaxNetworkReEntryTime_Type()
)
wmanIf2BsMaxNetworkReEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsMaxNetworkReEntryTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsMaxNetworkReEntryTime.setUnits("second")
_WmanIf2BsNumOfNetworkEntries_Type = Counter64
_WmanIf2BsNumOfNetworkEntries_Object = MibTableColumn
wmanIf2BsNumOfNetworkEntries = _WmanIf2BsNumOfNetworkEntries_Object(
    (1, 0, 8802, 16, 2, 1, 4, 5, 1, 5),
    _WmanIf2BsNumOfNetworkEntries_Type()
)
wmanIf2BsNumOfNetworkEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsNumOfNetworkEntries.setStatus("current")
_WmanIf2BsNumOfNetworkReEntries_Type = Counter64
_WmanIf2BsNumOfNetworkReEntries_Object = MibTableColumn
wmanIf2BsNumOfNetworkReEntries = _WmanIf2BsNumOfNetworkReEntries_Object(
    (1, 0, 8802, 16, 2, 1, 4, 5, 1, 6),
    _WmanIf2BsNumOfNetworkReEntries_Type()
)
wmanIf2BsNumOfNetworkReEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsNumOfNetworkReEntries.setStatus("current")
_WmanIf2BsPacketErrorRateTable_Object = MibTable
wmanIf2BsPacketErrorRateTable = _WmanIf2BsPacketErrorRateTable_Object(
    (1, 0, 8802, 16, 2, 1, 4, 6)
)
if mibBuilder.loadTexts:
    wmanIf2BsPacketErrorRateTable.setStatus("current")
_WmanIf2BsPacketErrorRateEntry_Object = MibTableRow
wmanIf2BsPacketErrorRateEntry = _WmanIf2BsPacketErrorRateEntry_Object(
    (1, 0, 8802, 16, 2, 1, 4, 6, 1)
)
wmanIf2BsPacketErrorRateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsPacketErrorRateEntry.setStatus("current")
_WmanIf2BsDlPacketsSend_Type = Counter64
_WmanIf2BsDlPacketsSend_Object = MibTableColumn
wmanIf2BsDlPacketsSend = _WmanIf2BsDlPacketsSend_Object(
    (1, 0, 8802, 16, 2, 1, 4, 6, 1, 1),
    _WmanIf2BsDlPacketsSend_Type()
)
wmanIf2BsDlPacketsSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsDlPacketsSend.setStatus("current")
_WmanIf2BsDlPacketsErrored_Type = Counter64
_WmanIf2BsDlPacketsErrored_Object = MibTableColumn
wmanIf2BsDlPacketsErrored = _WmanIf2BsDlPacketsErrored_Object(
    (1, 0, 8802, 16, 2, 1, 4, 6, 1, 2),
    _WmanIf2BsDlPacketsErrored_Type()
)
wmanIf2BsDlPacketsErrored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsDlPacketsErrored.setStatus("current")
_WmanIf2BsDlPacketErrorRate_Type = Unsigned32
_WmanIf2BsDlPacketErrorRate_Object = MibTableColumn
wmanIf2BsDlPacketErrorRate = _WmanIf2BsDlPacketErrorRate_Object(
    (1, 0, 8802, 16, 2, 1, 4, 6, 1, 3),
    _WmanIf2BsDlPacketErrorRate_Type()
)
wmanIf2BsDlPacketErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsDlPacketErrorRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsDlPacketErrorRate.setUnits("1x10E-7")
_WmanIf2BsSsHandoverMetricsTable_Object = MibTable
wmanIf2BsSsHandoverMetricsTable = _WmanIf2BsSsHandoverMetricsTable_Object(
    (1, 0, 8802, 16, 2, 1, 4, 7)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsHandoverMetricsTable.setStatus("current")
_WmanIf2BsSsHandoverMetricsEntry_Object = MibTableRow
wmanIf2BsSsHandoverMetricsEntry = _WmanIf2BsSsHandoverMetricsEntry_Object(
    (1, 0, 8802, 16, 2, 1, 4, 7, 1)
)
wmanIf2BsSsHandoverMetricsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsSsHandoverMetricsEntry.setStatus("current")
_WmanIf2BsSsHandoverAttempt_Type = Counter64
_WmanIf2BsSsHandoverAttempt_Object = MibTableColumn
wmanIf2BsSsHandoverAttempt = _WmanIf2BsSsHandoverAttempt_Object(
    (1, 0, 8802, 16, 2, 1, 4, 7, 1, 1),
    _WmanIf2BsSsHandoverAttempt_Type()
)
wmanIf2BsSsHandoverAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsHandoverAttempt.setStatus("current")
_WmanIf2BsSsHandoverSuccess_Type = Counter64
_WmanIf2BsSsHandoverSuccess_Object = MibTableColumn
wmanIf2BsSsHandoverSuccess = _WmanIf2BsSsHandoverSuccess_Object(
    (1, 0, 8802, 16, 2, 1, 4, 7, 1, 2),
    _WmanIf2BsSsHandoverSuccess_Type()
)
wmanIf2BsSsHandoverSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsHandoverSuccess.setStatus("current")
_WmanIf2BsSsHandoverSuccessRate_Type = Integer32
_WmanIf2BsSsHandoverSuccessRate_Object = MibTableColumn
wmanIf2BsSsHandoverSuccessRate = _WmanIf2BsSsHandoverSuccessRate_Object(
    (1, 0, 8802, 16, 2, 1, 4, 7, 1, 3),
    _WmanIf2BsSsHandoverSuccessRate_Type()
)
wmanIf2BsSsHandoverSuccessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsHandoverSuccessRate.setStatus("current")
_WmanIf2BsSsHandoverCancel_Type = Counter64
_WmanIf2BsSsHandoverCancel_Object = MibTableColumn
wmanIf2BsSsHandoverCancel = _WmanIf2BsSsHandoverCancel_Object(
    (1, 0, 8802, 16, 2, 1, 4, 7, 1, 4),
    _WmanIf2BsSsHandoverCancel_Type()
)
wmanIf2BsSsHandoverCancel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsHandoverCancel.setStatus("current")
_WmanIf2BsSsHandoverReject_Type = Counter64
_WmanIf2BsSsHandoverReject_Object = MibTableColumn
wmanIf2BsSsHandoverReject = _WmanIf2BsSsHandoverReject_Object(
    (1, 0, 8802, 16, 2, 1, 4, 7, 1, 5),
    _WmanIf2BsSsHandoverReject_Type()
)
wmanIf2BsSsHandoverReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsHandoverReject.setStatus("current")
_WmanIf2BsSsHandoverCancelRate_Type = Integer32
_WmanIf2BsSsHandoverCancelRate_Object = MibTableColumn
wmanIf2BsSsHandoverCancelRate = _WmanIf2BsSsHandoverCancelRate_Object(
    (1, 0, 8802, 16, 2, 1, 4, 7, 1, 6),
    _WmanIf2BsSsHandoverCancelRate_Type()
)
wmanIf2BsSsHandoverCancelRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsHandoverCancelRate.setStatus("current")
_WmanIf2BsSsHandoverRejectRate_Type = Integer32
_WmanIf2BsSsHandoverRejectRate_Object = MibTableColumn
wmanIf2BsSsHandoverRejectRate = _WmanIf2BsSsHandoverRejectRate_Object(
    (1, 0, 8802, 16, 2, 1, 4, 7, 1, 7),
    _WmanIf2BsSsHandoverRejectRate_Type()
)
wmanIf2BsSsHandoverRejectRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsHandoverRejectRate.setStatus("current")
_WmanIf2BsSsAvgHandoverTime_Type = Integer32
_WmanIf2BsSsAvgHandoverTime_Object = MibTableColumn
wmanIf2BsSsAvgHandoverTime = _WmanIf2BsSsAvgHandoverTime_Object(
    (1, 0, 8802, 16, 2, 1, 4, 7, 1, 8),
    _WmanIf2BsSsAvgHandoverTime_Type()
)
wmanIf2BsSsAvgHandoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsAvgHandoverTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSsAvgHandoverTime.setUnits("millisecond")
_WmanIf2BsSsUnexpectedHandover_Type = Counter64
_WmanIf2BsSsUnexpectedHandover_Object = MibTableColumn
wmanIf2BsSsUnexpectedHandover = _WmanIf2BsSsUnexpectedHandover_Object(
    (1, 0, 8802, 16, 2, 1, 4, 7, 1, 9),
    _WmanIf2BsSsUnexpectedHandover_Type()
)
wmanIf2BsSsUnexpectedHandover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsUnexpectedHandover.setStatus("current")
_WmanIf2BsSsUserMetricsTable_Object = MibTable
wmanIf2BsSsUserMetricsTable = _WmanIf2BsSsUserMetricsTable_Object(
    (1, 0, 8802, 16, 2, 1, 4, 8)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsUserMetricsTable.setStatus("current")
_WmanIf2BsSsUserMetricsEntry_Object = MibTableRow
wmanIf2BsSsUserMetricsEntry = _WmanIf2BsSsUserMetricsEntry_Object(
    (1, 0, 8802, 16, 2, 1, 4, 8, 1)
)
wmanIf2BsSsUserMetricsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsSsUserMetricsEntry.setStatus("current")
_WmanIf2BsSsActiveUsers_Type = Counter64
_WmanIf2BsSsActiveUsers_Object = MibTableColumn
wmanIf2BsSsActiveUsers = _WmanIf2BsSsActiveUsers_Object(
    (1, 0, 8802, 16, 2, 1, 4, 8, 1, 1),
    _WmanIf2BsSsActiveUsers_Type()
)
wmanIf2BsSsActiveUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsActiveUsers.setStatus("current")
_WmanIf2BsSsPeakNormalModeUsers_Type = Counter64
_WmanIf2BsSsPeakNormalModeUsers_Object = MibTableColumn
wmanIf2BsSsPeakNormalModeUsers = _WmanIf2BsSsPeakNormalModeUsers_Object(
    (1, 0, 8802, 16, 2, 1, 4, 8, 1, 2),
    _WmanIf2BsSsPeakNormalModeUsers_Type()
)
wmanIf2BsSsPeakNormalModeUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPeakNormalModeUsers.setStatus("current")
_WmanIf2BsSsPeakSleepModeUsers_Type = Counter64
_WmanIf2BsSsPeakSleepModeUsers_Object = MibTableColumn
wmanIf2BsSsPeakSleepModeUsers = _WmanIf2BsSsPeakSleepModeUsers_Object(
    (1, 0, 8802, 16, 2, 1, 4, 8, 1, 3),
    _WmanIf2BsSsPeakSleepModeUsers_Type()
)
wmanIf2BsSsPeakSleepModeUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPeakSleepModeUsers.setStatus("current")
_WmanIf2BsSsPeakIdleModeUsers_Type = Counter64
_WmanIf2BsSsPeakIdleModeUsers_Object = MibTableColumn
wmanIf2BsSsPeakIdleModeUsers = _WmanIf2BsSsPeakIdleModeUsers_Object(
    (1, 0, 8802, 16, 2, 1, 4, 8, 1, 4),
    _WmanIf2BsSsPeakIdleModeUsers_Type()
)
wmanIf2BsSsPeakIdleModeUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPeakIdleModeUsers.setStatus("current")
_WmanIf2BsSsAvgNormalModeUsers_Type = Integer32
_WmanIf2BsSsAvgNormalModeUsers_Object = MibTableColumn
wmanIf2BsSsAvgNormalModeUsers = _WmanIf2BsSsAvgNormalModeUsers_Object(
    (1, 0, 8802, 16, 2, 1, 4, 8, 1, 5),
    _WmanIf2BsSsAvgNormalModeUsers_Type()
)
wmanIf2BsSsAvgNormalModeUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsAvgNormalModeUsers.setStatus("current")
_WmanIf2BsSsCidmetricsTable_Object = MibTable
wmanIf2BsSsCidmetricsTable = _WmanIf2BsSsCidmetricsTable_Object(
    (1, 0, 8802, 16, 2, 1, 4, 9)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsCidmetricsTable.setStatus("current")
_WmanIf2BsSsCidmetricsEntry_Object = MibTableRow
wmanIf2BsSsCidmetricsEntry = _WmanIf2BsSsCidmetricsEntry_Object(
    (1, 0, 8802, 16, 2, 1, 4, 9, 1)
)
wmanIf2BsSsCidmetricsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsSsCidmetricsEntry.setStatus("current")
_WmanIf2BsSsBasicAndPrimaryCids_Type = Counter64
_WmanIf2BsSsBasicAndPrimaryCids_Object = MibTableColumn
wmanIf2BsSsBasicAndPrimaryCids = _WmanIf2BsSsBasicAndPrimaryCids_Object(
    (1, 0, 8802, 16, 2, 1, 4, 9, 1, 1),
    _WmanIf2BsSsBasicAndPrimaryCids_Type()
)
wmanIf2BsSsBasicAndPrimaryCids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsBasicAndPrimaryCids.setStatus("current")
_WmanIf2BsSsMaximumUserCids_Type = Counter64
_WmanIf2BsSsMaximumUserCids_Object = MibTableColumn
wmanIf2BsSsMaximumUserCids = _WmanIf2BsSsMaximumUserCids_Object(
    (1, 0, 8802, 16, 2, 1, 4, 9, 1, 2),
    _WmanIf2BsSsMaximumUserCids_Type()
)
wmanIf2BsSsMaximumUserCids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsMaximumUserCids.setStatus("current")
_WmanIf2BsSsAvgUserCids_Type = Counter64
_WmanIf2BsSsAvgUserCids_Object = MibTableColumn
wmanIf2BsSsAvgUserCids = _WmanIf2BsSsAvgUserCids_Object(
    (1, 0, 8802, 16, 2, 1, 4, 9, 1, 3),
    _WmanIf2BsSsAvgUserCids_Type()
)
wmanIf2BsSsAvgUserCids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsAvgUserCids.setStatus("current")
_WmanIf2BsSm_ObjectIdentity = ObjectIdentity
wmanIf2BsSm = _WmanIf2BsSm_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 5)
)
_WmanIf2BsPkmSecurityCapabilityTable_Object = MibTable
wmanIf2BsPkmSecurityCapabilityTable = _WmanIf2BsPkmSecurityCapabilityTable_Object(
    (1, 0, 8802, 16, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsPkmSecurityCapabilityTable.setStatus("current")
_WmanIf2BsPkmSecurityCapabilityEntry_Object = MibTableRow
wmanIf2BsPkmSecurityCapabilityEntry = _WmanIf2BsPkmSecurityCapabilityEntry_Object(
    (1, 0, 8802, 16, 2, 1, 5, 1, 1)
)
wmanIf2BsPkmSecurityCapabilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsPkmSecurityCapIndex"),
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
    (1, 0, 8802, 16, 2, 1, 5, 1, 1, 1),
    _WmanIf2BsPkmSecurityCapIndex_Type()
)
wmanIf2BsPkmSecurityCapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsPkmSecurityCapIndex.setStatus("current")
_WmanIf2BsPkmScDataEncryptAlgorithm_Type = WmanIf2DataEncryptAlgId
_WmanIf2BsPkmScDataEncryptAlgorithm_Object = MibTableColumn
wmanIf2BsPkmScDataEncryptAlgorithm = _WmanIf2BsPkmScDataEncryptAlgorithm_Object(
    (1, 0, 8802, 16, 2, 1, 5, 1, 1, 2),
    _WmanIf2BsPkmScDataEncryptAlgorithm_Type()
)
wmanIf2BsPkmScDataEncryptAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsPkmScDataEncryptAlgorithm.setStatus("current")
_WmanIf2BsPkmScDataAuthentAlgorithm_Type = WmanIf2DataAuthAlgId
_WmanIf2BsPkmScDataAuthentAlgorithm_Object = MibTableColumn
wmanIf2BsPkmScDataAuthentAlgorithm = _WmanIf2BsPkmScDataAuthentAlgorithm_Object(
    (1, 0, 8802, 16, 2, 1, 5, 1, 1, 3),
    _WmanIf2BsPkmScDataAuthentAlgorithm_Type()
)
wmanIf2BsPkmScDataAuthentAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsPkmScDataAuthentAlgorithm.setStatus("current")
_WmanIf2BsPkmScEncryptAlgorithm_Type = WmanIf2TekEncryptAlgId
_WmanIf2BsPkmScEncryptAlgorithm_Object = MibTableColumn
wmanIf2BsPkmScEncryptAlgorithm = _WmanIf2BsPkmScEncryptAlgorithm_Object(
    (1, 0, 8802, 16, 2, 1, 5, 1, 1, 4),
    _WmanIf2BsPkmScEncryptAlgorithm_Type()
)
wmanIf2BsPkmScEncryptAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsPkmScEncryptAlgorithm.setStatus("current")
_WmanIf2BsSsPkmSecurityCapabilityTable_Object = MibTable
wmanIf2BsSsPkmSecurityCapabilityTable = _WmanIf2BsSsPkmSecurityCapabilityTable_Object(
    (1, 0, 8802, 16, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmSecurityCapabilityTable.setStatus("current")
_WmanIf2BsSsPkmSecurityCapabilityEntry_Object = MibTableRow
wmanIf2BsSsPkmSecurityCapabilityEntry = _WmanIf2BsSsPkmSecurityCapabilityEntry_Object(
    (1, 0, 8802, 16, 2, 1, 5, 2, 1)
)
wmanIf2BsSsPkmSecurityCapabilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsSsMacAddress"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsSsPkmSecurityCapIndex"),
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
    (1, 0, 8802, 16, 2, 1, 5, 2, 1, 1),
    _WmanIf2BsSsPkmSecurityCapIndex_Type()
)
wmanIf2BsSsPkmSecurityCapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmSecurityCapIndex.setStatus("current")
_WmanIf2BsSsPkmScDataEncryptAlgorithm_Type = WmanIf2DataEncryptAlgId
_WmanIf2BsSsPkmScDataEncryptAlgorithm_Object = MibTableColumn
wmanIf2BsSsPkmScDataEncryptAlgorithm = _WmanIf2BsSsPkmScDataEncryptAlgorithm_Object(
    (1, 0, 8802, 16, 2, 1, 5, 2, 1, 2),
    _WmanIf2BsSsPkmScDataEncryptAlgorithm_Type()
)
wmanIf2BsSsPkmScDataEncryptAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmScDataEncryptAlgorithm.setStatus("current")
_WmanIf2BsSsPkmScDataAuthentAlgorithm_Type = WmanIf2DataAuthAlgId
_WmanIf2BsSsPkmScDataAuthentAlgorithm_Object = MibTableColumn
wmanIf2BsSsPkmScDataAuthentAlgorithm = _WmanIf2BsSsPkmScDataAuthentAlgorithm_Object(
    (1, 0, 8802, 16, 2, 1, 5, 2, 1, 3),
    _WmanIf2BsSsPkmScDataAuthentAlgorithm_Type()
)
wmanIf2BsSsPkmScDataAuthentAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmScDataAuthentAlgorithm.setStatus("current")
_WmanIf2BsSsPkmScEncryptAlgorithm_Type = WmanIf2TekEncryptAlgId
_WmanIf2BsSsPkmScEncryptAlgorithm_Object = MibTableColumn
wmanIf2BsSsPkmScEncryptAlgorithm = _WmanIf2BsSsPkmScEncryptAlgorithm_Object(
    (1, 0, 8802, 16, 2, 1, 5, 2, 1, 4),
    _WmanIf2BsSsPkmScEncryptAlgorithm_Type()
)
wmanIf2BsSsPkmScEncryptAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmScEncryptAlgorithm.setStatus("current")
_WmanIf2BsPkmV1Objects_ObjectIdentity = ObjectIdentity
wmanIf2BsPkmV1Objects = _WmanIf2BsPkmV1Objects_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 5, 3)
)
_WmanIf2BsPkmV1ConfigTable_Object = MibTable
wmanIf2BsPkmV1ConfigTable = _WmanIf2BsPkmV1ConfigTable_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1ConfigTable.setStatus("current")
_WmanIf2BsPkmV1ConfigEntry_Object = MibTableRow
wmanIf2BsPkmV1ConfigEntry = _WmanIf2BsPkmV1ConfigEntry_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 1, 1)
)
wmanIf2BsPkmV1ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1ConfigEntry.setStatus("current")


class _WmanIf2BsPkmV1AkLifetime_Type(Integer32):
    """Custom type wmanIf2BsPkmV1AkLifetime based on Integer32"""
    defaultValue = 604800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(86400, 6048000),
    )


_WmanIf2BsPkmV1AkLifetime_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1AkLifetime_Object = MibTableColumn
wmanIf2BsPkmV1AkLifetime = _WmanIf2BsPkmV1AkLifetime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 1, 1, 1),
    _WmanIf2BsPkmV1AkLifetime_Type()
)
wmanIf2BsPkmV1AkLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1AkLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1AkLifetime.setUnits("seconds")


class _WmanIf2BsPkmV1TekLifetime_Type(Integer32):
    """Custom type wmanIf2BsPkmV1TekLifetime based on Integer32"""
    defaultValue = 43200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 604800),
    )


_WmanIf2BsPkmV1TekLifetime_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1TekLifetime_Object = MibTableColumn
wmanIf2BsPkmV1TekLifetime = _WmanIf2BsPkmV1TekLifetime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 1, 1, 2),
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
    (1, 0, 8802, 16, 2, 1, 5, 3, 1, 1, 3),
    _WmanIf2BsPkmV1SelfSigManufCertTrust_Type()
)
wmanIf2BsPkmV1SelfSigManufCertTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1SelfSigManufCertTrust.setStatus("current")


class _WmanIf2BsPkmV1AuthWaitTimeout_Type(Integer32):
    """Custom type wmanIf2BsPkmV1AuthWaitTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_WmanIf2BsPkmV1AuthWaitTimeout_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1AuthWaitTimeout_Object = MibTableColumn
wmanIf2BsPkmV1AuthWaitTimeout = _WmanIf2BsPkmV1AuthWaitTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 1, 1, 4),
    _WmanIf2BsPkmV1AuthWaitTimeout_Type()
)
wmanIf2BsPkmV1AuthWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1AuthWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1AuthWaitTimeout.setUnits("seconds")


class _WmanIf2BsPkmV1ReauthWaitTimeout_Type(Integer32):
    """Custom type wmanIf2BsPkmV1ReauthWaitTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_WmanIf2BsPkmV1ReauthWaitTimeout_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1ReauthWaitTimeout_Object = MibTableColumn
wmanIf2BsPkmV1ReauthWaitTimeout = _WmanIf2BsPkmV1ReauthWaitTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 1, 1, 5),
    _WmanIf2BsPkmV1ReauthWaitTimeout_Type()
)
wmanIf2BsPkmV1ReauthWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1ReauthWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1ReauthWaitTimeout.setUnits("seconds")


class _WmanIf2BsPkmV1AuthGraceTime_Type(Integer32):
    """Custom type wmanIf2BsPkmV1AuthGraceTime based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3024000),
    )


_WmanIf2BsPkmV1AuthGraceTime_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1AuthGraceTime_Object = MibTableColumn
wmanIf2BsPkmV1AuthGraceTime = _WmanIf2BsPkmV1AuthGraceTime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 1, 1, 6),
    _WmanIf2BsPkmV1AuthGraceTime_Type()
)
wmanIf2BsPkmV1AuthGraceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1AuthGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1AuthGraceTime.setUnits("seconds")


class _WmanIf2BsPkmV1OpWaitTimeout_Type(Integer32):
    """Custom type wmanIf2BsPkmV1OpWaitTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WmanIf2BsPkmV1OpWaitTimeout_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1OpWaitTimeout_Object = MibTableColumn
wmanIf2BsPkmV1OpWaitTimeout = _WmanIf2BsPkmV1OpWaitTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 1, 1, 7),
    _WmanIf2BsPkmV1OpWaitTimeout_Type()
)
wmanIf2BsPkmV1OpWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1OpWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1OpWaitTimeout.setUnits("seconds")


class _WmanIf2BsPkmV1RekeyWaitTimeout_Type(Integer32):
    """Custom type wmanIf2BsPkmV1RekeyWaitTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WmanIf2BsPkmV1RekeyWaitTimeout_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1RekeyWaitTimeout_Object = MibTableColumn
wmanIf2BsPkmV1RekeyWaitTimeout = _WmanIf2BsPkmV1RekeyWaitTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 1, 1, 8),
    _WmanIf2BsPkmV1RekeyWaitTimeout_Type()
)
wmanIf2BsPkmV1RekeyWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1RekeyWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1RekeyWaitTimeout.setUnits("seconds")


class _WmanIf2BsPkmV1TekGraceTime_Type(Integer32):
    """Custom type wmanIf2BsPkmV1TekGraceTime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3024000),
    )


_WmanIf2BsPkmV1TekGraceTime_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1TekGraceTime_Object = MibTableColumn
wmanIf2BsPkmV1TekGraceTime = _WmanIf2BsPkmV1TekGraceTime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 1, 1, 9),
    _WmanIf2BsPkmV1TekGraceTime_Type()
)
wmanIf2BsPkmV1TekGraceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1TekGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1TekGraceTime.setUnits("seconds")


class _WmanIf2BsPkmV1AuthRejectWaitTimeout_Type(Integer32):
    """Custom type wmanIf2BsPkmV1AuthRejectWaitTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_WmanIf2BsPkmV1AuthRejectWaitTimeout_Type.__name__ = "Integer32"
_WmanIf2BsPkmV1AuthRejectWaitTimeout_Object = MibTableColumn
wmanIf2BsPkmV1AuthRejectWaitTimeout = _WmanIf2BsPkmV1AuthRejectWaitTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 1, 1, 10),
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
    (1, 0, 8802, 16, 2, 1, 5, 3, 1, 1, 11),
    _WmanIf2BsPkmV1CheckCertValidityPeriods_Type()
)
wmanIf2BsPkmV1CheckCertValidityPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmV1CheckCertValidityPeriods.setStatus("current")
_WmanIf2BsSsPkmV1AuthorizationTable_Object = MibTable
wmanIf2BsSsPkmV1AuthorizationTable = _WmanIf2BsSsPkmV1AuthorizationTable_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1AuthorizationTable.setStatus("current")
_WmanIf2BsSsPkmV1AuthorizationEntry_Object = MibTableRow
wmanIf2BsSsPkmV1AuthorizationEntry = _WmanIf2BsSsPkmV1AuthorizationEntry_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 2, 1)
)
wmanIf2BsSsPkmV1AuthorizationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsSsPkmV1AuthMacAddress"),
)
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1AuthorizationEntry.setStatus("current")
_WmanIf2BsSsPkmV1AuthMacAddress_Type = MacAddress
_WmanIf2BsSsPkmV1AuthMacAddress_Object = MibTableColumn
wmanIf2BsSsPkmV1AuthMacAddress = _WmanIf2BsSsPkmV1AuthMacAddress_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 2, 1, 1),
    _WmanIf2BsSsPkmV1AuthMacAddress_Type()
)
wmanIf2BsSsPkmV1AuthMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1AuthMacAddress.setStatus("current")


class _WmanIf2BsSsPkmV1CaCertificate_Type(OctetString):
    """Custom type wmanIf2BsSsPkmV1CaCertificate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_WmanIf2BsSsPkmV1CaCertificate_Type.__name__ = "OctetString"
_WmanIf2BsSsPkmV1CaCertificate_Object = MibTableColumn
wmanIf2BsSsPkmV1CaCertificate = _WmanIf2BsSsPkmV1CaCertificate_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 2, 1, 2),
    _WmanIf2BsSsPkmV1CaCertificate_Type()
)
wmanIf2BsSsPkmV1CaCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1CaCertificate.setStatus("current")


class _WmanIf2BsSsPkmV1SsCertificate_Type(OctetString):
    """Custom type wmanIf2BsSsPkmV1SsCertificate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_WmanIf2BsSsPkmV1SsCertificate_Type.__name__ = "OctetString"
_WmanIf2BsSsPkmV1SsCertificate_Object = MibTableColumn
wmanIf2BsSsPkmV1SsCertificate = _WmanIf2BsSsPkmV1SsCertificate_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 2, 1, 3),
    _WmanIf2BsSsPkmV1SsCertificate_Type()
)
wmanIf2BsSsPkmV1SsCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1SsCertificate.setStatus("current")


class _WmanIf2BsSsPkmV1PrimarySaId_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV1PrimarySaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSsPkmV1PrimarySaId_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV1PrimarySaId_Object = MibTableColumn
wmanIf2BsSsPkmV1PrimarySaId = _WmanIf2BsSsPkmV1PrimarySaId_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 2, 1, 4),
    _WmanIf2BsSsPkmV1PrimarySaId_Type()
)
wmanIf2BsSsPkmV1PrimarySaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1PrimarySaId.setStatus("current")


class _WmanIf2BsSsPkmV1AuthKeySequenceNumber_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV1AuthKeySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsSsPkmV1AuthKeySequenceNumber_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV1AuthKeySequenceNumber_Object = MibTableColumn
wmanIf2BsSsPkmV1AuthKeySequenceNumber = _WmanIf2BsSsPkmV1AuthKeySequenceNumber_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 2, 1, 5),
    _WmanIf2BsSsPkmV1AuthKeySequenceNumber_Type()
)
wmanIf2BsSsPkmV1AuthKeySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1AuthKeySequenceNumber.setStatus("current")


class _WmanIf2BsSsPkmV1AuthKeyLifetime_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV1AuthKeyLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(86400, 6048000),
    )


_WmanIf2BsSsPkmV1AuthKeyLifetime_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV1AuthKeyLifetime_Object = MibTableColumn
wmanIf2BsSsPkmV1AuthKeyLifetime = _WmanIf2BsSsPkmV1AuthKeyLifetime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 2, 1, 6),
    _WmanIf2BsSsPkmV1AuthKeyLifetime_Type()
)
wmanIf2BsSsPkmV1AuthKeyLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1AuthKeyLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1AuthKeyLifetime.setUnits("seconds")
_WmanIf2BsSsPkmV1AuthRejectError_Type = WmanIf2PkmErrorCode
_WmanIf2BsSsPkmV1AuthRejectError_Object = MibTableColumn
wmanIf2BsSsPkmV1AuthRejectError = _WmanIf2BsSsPkmV1AuthRejectError_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 2, 1, 7),
    _WmanIf2BsSsPkmV1AuthRejectError_Type()
)
wmanIf2BsSsPkmV1AuthRejectError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1AuthRejectError.setStatus("current")
_WmanIf2BsSsPkmV1AuthInvalidError_Type = WmanIf2PkmErrorCode
_WmanIf2BsSsPkmV1AuthInvalidError_Object = MibTableColumn
wmanIf2BsSsPkmV1AuthInvalidError = _WmanIf2BsSsPkmV1AuthInvalidError_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 2, 1, 8),
    _WmanIf2BsSsPkmV1AuthInvalidError_Type()
)
wmanIf2BsSsPkmV1AuthInvalidError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1AuthInvalidError.setStatus("current")
_WmanIf2BsSsPkmV1AkN_1ExpireTime_Type = DateAndTime
_WmanIf2BsSsPkmV1AkN_1ExpireTime_Object = MibTableColumn
wmanIf2BsSsPkmV1AkN_1ExpireTime = _WmanIf2BsSsPkmV1AkN_1ExpireTime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 2, 1, 9),
    _WmanIf2BsSsPkmV1AkN_1ExpireTime_Type()
)
wmanIf2BsSsPkmV1AkN_1ExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1AkN_1ExpireTime.setStatus("current")
_WmanIf2BsSsPkmV1AkNExpireTime_Type = DateAndTime
_WmanIf2BsSsPkmV1AkNExpireTime_Object = MibTableColumn
wmanIf2BsSsPkmV1AkNExpireTime = _WmanIf2BsSsPkmV1AkNExpireTime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 2, 1, 10),
    _WmanIf2BsSsPkmV1AkNExpireTime_Type()
)
wmanIf2BsSsPkmV1AkNExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1AkNExpireTime.setStatus("current")
_WmanIf2BsSsPkmV1CertificateStatus_Type = WmanIf2CertificateStat
_WmanIf2BsSsPkmV1CertificateStatus_Object = MibTableColumn
wmanIf2BsSsPkmV1CertificateStatus = _WmanIf2BsSsPkmV1CertificateStatus_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 2, 1, 11),
    _WmanIf2BsSsPkmV1CertificateStatus_Type()
)
wmanIf2BsSsPkmV1CertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1CertificateStatus.setStatus("current")


class _WmanIf2BsSsPkmV1AuthReset_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV1AuthReset based on Integer32"""
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


_WmanIf2BsSsPkmV1AuthReset_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV1AuthReset_Object = MibTableColumn
wmanIf2BsSsPkmV1AuthReset = _WmanIf2BsSsPkmV1AuthReset_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 2, 1, 12),
    _WmanIf2BsSsPkmV1AuthReset_Type()
)
wmanIf2BsSsPkmV1AuthReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1AuthReset.setStatus("current")
_WmanIf2BsSsPkmV1TekTable_Object = MibTable
wmanIf2BsSsPkmV1TekTable = _WmanIf2BsSsPkmV1TekTable_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1TekTable.setStatus("current")
_WmanIf2BsSsPkmV1TekEntry_Object = MibTableRow
wmanIf2BsSsPkmV1TekEntry = _WmanIf2BsSsPkmV1TekEntry_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 3, 1)
)
wmanIf2BsSsPkmV1TekEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsSsMacAddress"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsSsPkmV1SaidIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1TekEntry.setStatus("current")


class _WmanIf2BsSsPkmV1SaidIndex_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV1SaidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSsPkmV1SaidIndex_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV1SaidIndex_Object = MibTableColumn
wmanIf2BsSsPkmV1SaidIndex = _WmanIf2BsSsPkmV1SaidIndex_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 3, 1, 1),
    _WmanIf2BsSsPkmV1SaidIndex_Type()
)
wmanIf2BsSsPkmV1SaidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1SaidIndex.setStatus("current")
_WmanIf2BsSsPkmV1SaType_Type = WmanIf2SaType
_WmanIf2BsSsPkmV1SaType_Object = MibTableColumn
wmanIf2BsSsPkmV1SaType = _WmanIf2BsSsPkmV1SaType_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 3, 1, 2),
    _WmanIf2BsSsPkmV1SaType_Type()
)
wmanIf2BsSsPkmV1SaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1SaType.setStatus("current")
_WmanIf2BsSsPkmV1TekDataEncryptAlgorithm_Type = WmanIf2DataEncryptAlgId
_WmanIf2BsSsPkmV1TekDataEncryptAlgorithm_Object = MibTableColumn
wmanIf2BsSsPkmV1TekDataEncryptAlgorithm = _WmanIf2BsSsPkmV1TekDataEncryptAlgorithm_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 3, 1, 3),
    _WmanIf2BsSsPkmV1TekDataEncryptAlgorithm_Type()
)
wmanIf2BsSsPkmV1TekDataEncryptAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1TekDataEncryptAlgorithm.setStatus("current")
_WmanIf2BsSsPkmV1TekDataAuthentAlgorithm_Type = WmanIf2DataAuthAlgId
_WmanIf2BsSsPkmV1TekDataAuthentAlgorithm_Object = MibTableColumn
wmanIf2BsSsPkmV1TekDataAuthentAlgorithm = _WmanIf2BsSsPkmV1TekDataAuthentAlgorithm_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 3, 1, 4),
    _WmanIf2BsSsPkmV1TekDataAuthentAlgorithm_Type()
)
wmanIf2BsSsPkmV1TekDataAuthentAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1TekDataAuthentAlgorithm.setStatus("current")
_WmanIf2BsSsPkmV1TekEncryptAlgorithm_Type = WmanIf2TekEncryptAlgId
_WmanIf2BsSsPkmV1TekEncryptAlgorithm_Object = MibTableColumn
wmanIf2BsSsPkmV1TekEncryptAlgorithm = _WmanIf2BsSsPkmV1TekEncryptAlgorithm_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 3, 1, 5),
    _WmanIf2BsSsPkmV1TekEncryptAlgorithm_Type()
)
wmanIf2BsSsPkmV1TekEncryptAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1TekEncryptAlgorithm.setStatus("current")


class _WmanIf2BsSsPkmV1TekN_1SequenceNumber_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV1TekN_1SequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WmanIf2BsSsPkmV1TekN_1SequenceNumber_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV1TekN_1SequenceNumber_Object = MibTableColumn
wmanIf2BsSsPkmV1TekN_1SequenceNumber = _WmanIf2BsSsPkmV1TekN_1SequenceNumber_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 3, 1, 6),
    _WmanIf2BsSsPkmV1TekN_1SequenceNumber_Type()
)
wmanIf2BsSsPkmV1TekN_1SequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1TekN_1SequenceNumber.setStatus("current")


class _WmanIf2BsSsPkmV1TekN_1Lifetime_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV1TekN_1Lifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 604800),
    )


_WmanIf2BsSsPkmV1TekN_1Lifetime_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV1TekN_1Lifetime_Object = MibTableColumn
wmanIf2BsSsPkmV1TekN_1Lifetime = _WmanIf2BsSsPkmV1TekN_1Lifetime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 3, 1, 7),
    _WmanIf2BsSsPkmV1TekN_1Lifetime_Type()
)
wmanIf2BsSsPkmV1TekN_1Lifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1TekN_1Lifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1TekN_1Lifetime.setUnits("seconds")


class _WmanIf2BsSsPkmV1TekNSequenceNumber_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV1TekNSequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WmanIf2BsSsPkmV1TekNSequenceNumber_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV1TekNSequenceNumber_Object = MibTableColumn
wmanIf2BsSsPkmV1TekNSequenceNumber = _WmanIf2BsSsPkmV1TekNSequenceNumber_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 3, 1, 8),
    _WmanIf2BsSsPkmV1TekNSequenceNumber_Type()
)
wmanIf2BsSsPkmV1TekNSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1TekNSequenceNumber.setStatus("current")


class _WmanIf2BsSsPkmV1TekNLifetime_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV1TekNLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 604800),
    )


_WmanIf2BsSsPkmV1TekNLifetime_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV1TekNLifetime_Object = MibTableColumn
wmanIf2BsSsPkmV1TekNLifetime = _WmanIf2BsSsPkmV1TekNLifetime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 3, 1, 9),
    _WmanIf2BsSsPkmV1TekNLifetime_Type()
)
wmanIf2BsSsPkmV1TekNLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1TekNLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1TekNLifetime.setUnits("seconds")
_WmanIf2BsSsPkmV1KeyRejectError_Type = WmanIf2PkmErrorCode
_WmanIf2BsSsPkmV1KeyRejectError_Object = MibTableColumn
wmanIf2BsSsPkmV1KeyRejectError = _WmanIf2BsSsPkmV1KeyRejectError_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 3, 1, 10),
    _WmanIf2BsSsPkmV1KeyRejectError_Type()
)
wmanIf2BsSsPkmV1KeyRejectError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1KeyRejectError.setStatus("current")
_WmanIf2BsSsPkmV1TekInvalidError_Type = WmanIf2PkmErrorCode
_WmanIf2BsSsPkmV1TekInvalidError_Object = MibTableColumn
wmanIf2BsSsPkmV1TekInvalidError = _WmanIf2BsSsPkmV1TekInvalidError_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 3, 1, 11),
    _WmanIf2BsSsPkmV1TekInvalidError_Type()
)
wmanIf2BsSsPkmV1TekInvalidError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1TekInvalidError.setStatus("current")
_WmanIf2BsSsPkmV1TekN_1ExpireTime_Type = DateAndTime
_WmanIf2BsSsPkmV1TekN_1ExpireTime_Object = MibTableColumn
wmanIf2BsSsPkmV1TekN_1ExpireTime = _WmanIf2BsSsPkmV1TekN_1ExpireTime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 3, 1, 12),
    _WmanIf2BsSsPkmV1TekN_1ExpireTime_Type()
)
wmanIf2BsSsPkmV1TekN_1ExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1TekN_1ExpireTime.setStatus("current")
_WmanIf2BsSsPkmV1TekNExpireTime_Type = DateAndTime
_WmanIf2BsSsPkmV1TekNExpireTime_Object = MibTableColumn
wmanIf2BsSsPkmV1TekNExpireTime = _WmanIf2BsSsPkmV1TekNExpireTime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 3, 1, 13),
    _WmanIf2BsSsPkmV1TekNExpireTime_Type()
)
wmanIf2BsSsPkmV1TekNExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1TekNExpireTime.setStatus("current")
_WmanIf2BsSsPkmV1TekReset_Type = TruthValue
_WmanIf2BsSsPkmV1TekReset_Object = MibTableColumn
wmanIf2BsSsPkmV1TekReset = _WmanIf2BsSsPkmV1TekReset_Object(
    (1, 0, 8802, 16, 2, 1, 5, 3, 3, 1, 14),
    _WmanIf2BsSsPkmV1TekReset_Type()
)
wmanIf2BsSsPkmV1TekReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV1TekReset.setStatus("current")
_WmanIf2BsPkmV2Objects_ObjectIdentity = ObjectIdentity
wmanIf2BsPkmV2Objects = _WmanIf2BsPkmV2Objects_ObjectIdentity(
    (1, 0, 8802, 16, 2, 1, 5, 4)
)
_WmanIf2BsPkmV2ConfigTable_Object = MibTable
wmanIf2BsPkmV2ConfigTable = _WmanIf2BsPkmV2ConfigTable_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    wmanIf2BsPkmV2ConfigTable.setStatus("current")
_WmanIf2BsPkmV2ConfigEntry_Object = MibTableRow
wmanIf2BsPkmV2ConfigEntry = _WmanIf2BsPkmV2ConfigEntry_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 1, 1)
)
wmanIf2BsPkmV2ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsPkmV2ConfigEntry.setStatus("current")


class _WmanIf2BsPkmPmkPrehandshakeLifetime_Type(Integer32):
    """Custom type wmanIf2BsPkmPmkPrehandshakeLifetime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 900),
    )


_WmanIf2BsPkmPmkPrehandshakeLifetime_Type.__name__ = "Integer32"
_WmanIf2BsPkmPmkPrehandshakeLifetime_Object = MibTableColumn
wmanIf2BsPkmPmkPrehandshakeLifetime = _WmanIf2BsPkmPmkPrehandshakeLifetime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 1, 1, 1),
    _WmanIf2BsPkmPmkPrehandshakeLifetime_Type()
)
wmanIf2BsPkmPmkPrehandshakeLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmPmkPrehandshakeLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmPmkPrehandshakeLifetime.setUnits("seconds")


class _WmanIf2BsPkmPmkLifetime_Type(Integer32):
    """Custom type wmanIf2BsPkmPmkLifetime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_WmanIf2BsPkmPmkLifetime_Type.__name__ = "Integer32"
_WmanIf2BsPkmPmkLifetime_Object = MibTableColumn
wmanIf2BsPkmPmkLifetime = _WmanIf2BsPkmPmkLifetime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 1, 1, 2),
    _WmanIf2BsPkmPmkLifetime_Type()
)
wmanIf2BsPkmPmkLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsPkmPmkLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsPkmPmkLifetime.setUnits("seconds")


class _WmanIf2BsSaChallengeTimeout_Type(Integer32):
    """Custom type wmanIf2BsSaChallengeTimeout based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 2000),
    )


_WmanIf2BsSaChallengeTimeout_Type.__name__ = "Integer32"
_WmanIf2BsSaChallengeTimeout_Object = MibTableColumn
wmanIf2BsSaChallengeTimeout = _WmanIf2BsSaChallengeTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 1, 1, 3),
    _WmanIf2BsSaChallengeTimeout_Type()
)
wmanIf2BsSaChallengeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSaChallengeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSaChallengeTimeout.setUnits("milliseconds")


class _WmanIf2BsMaxSaTekChallenge_Type(Integer32):
    """Custom type wmanIf2BsMaxSaTekChallenge based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WmanIf2BsMaxSaTekChallenge_Type.__name__ = "Integer32"
_WmanIf2BsMaxSaTekChallenge_Object = MibTableColumn
wmanIf2BsMaxSaTekChallenge = _WmanIf2BsMaxSaTekChallenge_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 1, 1, 4),
    _WmanIf2BsMaxSaTekChallenge_Type()
)
wmanIf2BsMaxSaTekChallenge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsMaxSaTekChallenge.setStatus("current")


class _WmanIf2BsSaTekTimeout_Type(Integer32):
    """Custom type wmanIf2BsSaTekTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_WmanIf2BsSaTekTimeout_Type.__name__ = "Integer32"
_WmanIf2BsSaTekTimeout_Object = MibTableColumn
wmanIf2BsSaTekTimeout = _WmanIf2BsSaTekTimeout_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 1, 1, 5),
    _WmanIf2BsSaTekTimeout_Type()
)
wmanIf2BsSaTekTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsSaTekTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSaTekTimeout.setUnits("milliseconds")


class _WmanIf2BsMaxSaTekRequest_Type(Integer32):
    """Custom type wmanIf2BsMaxSaTekRequest based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WmanIf2BsMaxSaTekRequest_Type.__name__ = "Integer32"
_WmanIf2BsMaxSaTekRequest_Object = MibTableColumn
wmanIf2BsMaxSaTekRequest = _WmanIf2BsMaxSaTekRequest_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 1, 1, 6),
    _WmanIf2BsMaxSaTekRequest_Type()
)
wmanIf2BsMaxSaTekRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2BsMaxSaTekRequest.setStatus("current")
_WmanIf2BsSsPkmV2RsaAuthTable_Object = MibTable
wmanIf2BsSsPkmV2RsaAuthTable = _WmanIf2BsSsPkmV2RsaAuthTable_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 2)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2RsaAuthTable.setStatus("current")
_WmanIf2BsSsPkmV2RsaAuthEntry_Object = MibTableRow
wmanIf2BsSsPkmV2RsaAuthEntry = _WmanIf2BsSsPkmV2RsaAuthEntry_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 2, 1)
)
wmanIf2BsSsPkmV2RsaAuthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsSsMacAddress"),
)
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2RsaAuthEntry.setStatus("current")


class _WmanIf2BsSsPkmV2BsCertificate_Type(OctetString):
    """Custom type wmanIf2BsSsPkmV2BsCertificate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_WmanIf2BsSsPkmV2BsCertificate_Type.__name__ = "OctetString"
_WmanIf2BsSsPkmV2BsCertificate_Object = MibTableColumn
wmanIf2BsSsPkmV2BsCertificate = _WmanIf2BsSsPkmV2BsCertificate_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 2, 1, 1),
    _WmanIf2BsSsPkmV2BsCertificate_Type()
)
wmanIf2BsSsPkmV2BsCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2BsCertificate.setStatus("current")


class _WmanIf2BsSsPkmV2SsCertificate_Type(OctetString):
    """Custom type wmanIf2BsSsPkmV2SsCertificate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_WmanIf2BsSsPkmV2SsCertificate_Type.__name__ = "OctetString"
_WmanIf2BsSsPkmV2SsCertificate_Object = MibTableColumn
wmanIf2BsSsPkmV2SsCertificate = _WmanIf2BsSsPkmV2SsCertificate_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 2, 1, 2),
    _WmanIf2BsSsPkmV2SsCertificate_Type()
)
wmanIf2BsSsPkmV2SsCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2SsCertificate.setStatus("current")


class _WmanIf2BsSsPkmV2SaId_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV2SaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSsPkmV2SaId_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV2SaId_Object = MibTableColumn
wmanIf2BsSsPkmV2SaId = _WmanIf2BsSsPkmV2SaId_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 2, 1, 3),
    _WmanIf2BsSsPkmV2SaId_Type()
)
wmanIf2BsSsPkmV2SaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2SaId.setStatus("current")


class _WmanIf2BsSsPkmV2SsRandom_Type(OctetString):
    """Custom type wmanIf2BsSsPkmV2SsRandom based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_WmanIf2BsSsPkmV2SsRandom_Type.__name__ = "OctetString"
_WmanIf2BsSsPkmV2SsRandom_Object = MibTableColumn
wmanIf2BsSsPkmV2SsRandom = _WmanIf2BsSsPkmV2SsRandom_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 2, 1, 4),
    _WmanIf2BsSsPkmV2SsRandom_Type()
)
wmanIf2BsSsPkmV2SsRandom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2SsRandom.setStatus("current")


class _WmanIf2BsSsPkmV2BsRandom_Type(OctetString):
    """Custom type wmanIf2BsSsPkmV2BsRandom based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_WmanIf2BsSsPkmV2BsRandom_Type.__name__ = "OctetString"
_WmanIf2BsSsPkmV2BsRandom_Object = MibTableColumn
wmanIf2BsSsPkmV2BsRandom = _WmanIf2BsSsPkmV2BsRandom_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 2, 1, 5),
    _WmanIf2BsSsPkmV2BsRandom_Type()
)
wmanIf2BsSsPkmV2BsRandom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2BsRandom.setStatus("current")


class _WmanIf2BsSsPkmV2AuthKeySequenceNumber_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV2AuthKeySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsSsPkmV2AuthKeySequenceNumber_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV2AuthKeySequenceNumber_Object = MibTableColumn
wmanIf2BsSsPkmV2AuthKeySequenceNumber = _WmanIf2BsSsPkmV2AuthKeySequenceNumber_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 2, 1, 6),
    _WmanIf2BsSsPkmV2AuthKeySequenceNumber_Type()
)
wmanIf2BsSsPkmV2AuthKeySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2AuthKeySequenceNumber.setStatus("current")


class _WmanIf2BsSsPkmV2AuthKeyLifetime_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV2AuthKeyLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(86400, 6048000),
    )


_WmanIf2BsSsPkmV2AuthKeyLifetime_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV2AuthKeyLifetime_Object = MibTableColumn
wmanIf2BsSsPkmV2AuthKeyLifetime = _WmanIf2BsSsPkmV2AuthKeyLifetime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 2, 1, 7),
    _WmanIf2BsSsPkmV2AuthKeyLifetime_Type()
)
wmanIf2BsSsPkmV2AuthKeyLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2AuthKeyLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2AuthKeyLifetime.setUnits("seconds")


class _WmanIf2BsSsPkmV2AuthResult_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV2AuthResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("success", 0),
          ("reject", 1))
    )


_WmanIf2BsSsPkmV2AuthResult_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV2AuthResult_Object = MibTableColumn
wmanIf2BsSsPkmV2AuthResult = _WmanIf2BsSsPkmV2AuthResult_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 2, 1, 8),
    _WmanIf2BsSsPkmV2AuthResult_Type()
)
wmanIf2BsSsPkmV2AuthResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2AuthResult.setStatus("current")
_WmanIf2BsSsPkmV2AuthFailure_Type = WmanIf2PkmErrorCode
_WmanIf2BsSsPkmV2AuthFailure_Object = MibTableColumn
wmanIf2BsSsPkmV2AuthFailure = _WmanIf2BsSsPkmV2AuthFailure_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 2, 1, 9),
    _WmanIf2BsSsPkmV2AuthFailure_Type()
)
wmanIf2BsSsPkmV2AuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2AuthFailure.setStatus("current")
_WmanIf2BsSsPkmV2AkN_1ExpireTime_Type = DateAndTime
_WmanIf2BsSsPkmV2AkN_1ExpireTime_Object = MibTableColumn
wmanIf2BsSsPkmV2AkN_1ExpireTime = _WmanIf2BsSsPkmV2AkN_1ExpireTime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 2, 1, 10),
    _WmanIf2BsSsPkmV2AkN_1ExpireTime_Type()
)
wmanIf2BsSsPkmV2AkN_1ExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2AkN_1ExpireTime.setStatus("current")
_WmanIf2BsSsPkmV2AkNExpireTime_Type = DateAndTime
_WmanIf2BsSsPkmV2AkNExpireTime_Object = MibTableColumn
wmanIf2BsSsPkmV2AkNExpireTime = _WmanIf2BsSsPkmV2AkNExpireTime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 2, 1, 11),
    _WmanIf2BsSsPkmV2AkNExpireTime_Type()
)
wmanIf2BsSsPkmV2AkNExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2AkNExpireTime.setStatus("current")
_WmanIf2BsSsPkmV2CertificateStatus_Type = WmanIf2CertificateStat
_WmanIf2BsSsPkmV2CertificateStatus_Object = MibTableColumn
wmanIf2BsSsPkmV2CertificateStatus = _WmanIf2BsSsPkmV2CertificateStatus_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 2, 1, 12),
    _WmanIf2BsSsPkmV2CertificateStatus_Type()
)
wmanIf2BsSsPkmV2CertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2CertificateStatus.setStatus("current")
_WmanIf2BsSsPkmV2TekTable_Object = MibTable
wmanIf2BsSsPkmV2TekTable = _WmanIf2BsSsPkmV2TekTable_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 3)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2TekTable.setStatus("current")
_WmanIf2BsSsPkmV2TekEntry_Object = MibTableRow
wmanIf2BsSsPkmV2TekEntry = _WmanIf2BsSsPkmV2TekEntry_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 3, 1)
)
wmanIf2BsSsPkmV2TekEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsSsMacAddress"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsSsPkmV2SaidIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2TekEntry.setStatus("current")


class _WmanIf2BsSsPkmV2SaidIndex_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV2SaidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2BsSsPkmV2SaidIndex_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV2SaidIndex_Object = MibTableColumn
wmanIf2BsSsPkmV2SaidIndex = _WmanIf2BsSsPkmV2SaidIndex_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 3, 1, 1),
    _WmanIf2BsSsPkmV2SaidIndex_Type()
)
wmanIf2BsSsPkmV2SaidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2SaidIndex.setStatus("current")
_WmanIf2BsSsPkmV2SaType_Type = WmanIf2SaType
_WmanIf2BsSsPkmV2SaType_Object = MibTableColumn
wmanIf2BsSsPkmV2SaType = _WmanIf2BsSsPkmV2SaType_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 3, 1, 2),
    _WmanIf2BsSsPkmV2SaType_Type()
)
wmanIf2BsSsPkmV2SaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2SaType.setStatus("current")
_WmanIf2BsSsPkmV2SaServiceType_Type = WmanIf2SaServiceType
_WmanIf2BsSsPkmV2SaServiceType_Object = MibTableColumn
wmanIf2BsSsPkmV2SaServiceType = _WmanIf2BsSsPkmV2SaServiceType_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 3, 1, 3),
    _WmanIf2BsSsPkmV2SaServiceType_Type()
)
wmanIf2BsSsPkmV2SaServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2SaServiceType.setStatus("current")
_WmanIf2BsSsPkmV2TekDataEncryptAlgorithm_Type = WmanIf2DataEncryptAlgId
_WmanIf2BsSsPkmV2TekDataEncryptAlgorithm_Object = MibTableColumn
wmanIf2BsSsPkmV2TekDataEncryptAlgorithm = _WmanIf2BsSsPkmV2TekDataEncryptAlgorithm_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 3, 1, 4),
    _WmanIf2BsSsPkmV2TekDataEncryptAlgorithm_Type()
)
wmanIf2BsSsPkmV2TekDataEncryptAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2TekDataEncryptAlgorithm.setStatus("current")
_WmanIf2BsSsPkmV2TekDataAuthentAlgorithm_Type = WmanIf2DataAuthAlgId
_WmanIf2BsSsPkmV2TekDataAuthentAlgorithm_Object = MibTableColumn
wmanIf2BsSsPkmV2TekDataAuthentAlgorithm = _WmanIf2BsSsPkmV2TekDataAuthentAlgorithm_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 3, 1, 5),
    _WmanIf2BsSsPkmV2TekDataAuthentAlgorithm_Type()
)
wmanIf2BsSsPkmV2TekDataAuthentAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2TekDataAuthentAlgorithm.setStatus("current")
_WmanIf2BsSsPkmV2TekEncryptAlgorithm_Type = WmanIf2TekEncryptAlgId
_WmanIf2BsSsPkmV2TekEncryptAlgorithm_Object = MibTableColumn
wmanIf2BsSsPkmV2TekEncryptAlgorithm = _WmanIf2BsSsPkmV2TekEncryptAlgorithm_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 3, 1, 6),
    _WmanIf2BsSsPkmV2TekEncryptAlgorithm_Type()
)
wmanIf2BsSsPkmV2TekEncryptAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2TekEncryptAlgorithm.setStatus("current")


class _WmanIf2BsSsPkmV2TekN_1SequenceNumber_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV2TekN_1SequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WmanIf2BsSsPkmV2TekN_1SequenceNumber_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV2TekN_1SequenceNumber_Object = MibTableColumn
wmanIf2BsSsPkmV2TekN_1SequenceNumber = _WmanIf2BsSsPkmV2TekN_1SequenceNumber_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 3, 1, 7),
    _WmanIf2BsSsPkmV2TekN_1SequenceNumber_Type()
)
wmanIf2BsSsPkmV2TekN_1SequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2TekN_1SequenceNumber.setStatus("current")


class _WmanIf2BsSsPkmV2TekN_1Lifetime_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV2TekN_1Lifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 604800),
    )


_WmanIf2BsSsPkmV2TekN_1Lifetime_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV2TekN_1Lifetime_Object = MibTableColumn
wmanIf2BsSsPkmV2TekN_1Lifetime = _WmanIf2BsSsPkmV2TekN_1Lifetime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 3, 1, 8),
    _WmanIf2BsSsPkmV2TekN_1Lifetime_Type()
)
wmanIf2BsSsPkmV2TekN_1Lifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2TekN_1Lifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2TekN_1Lifetime.setUnits("seconds")


class _WmanIf2BsSsPkmV2TekNSequenceNumber_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV2TekNSequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WmanIf2BsSsPkmV2TekNSequenceNumber_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV2TekNSequenceNumber_Object = MibTableColumn
wmanIf2BsSsPkmV2TekNSequenceNumber = _WmanIf2BsSsPkmV2TekNSequenceNumber_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 3, 1, 9),
    _WmanIf2BsSsPkmV2TekNSequenceNumber_Type()
)
wmanIf2BsSsPkmV2TekNSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2TekNSequenceNumber.setStatus("current")


class _WmanIf2BsSsPkmV2TekNLifetime_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV2TekNLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 604800),
    )


_WmanIf2BsSsPkmV2TekNLifetime_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV2TekNLifetime_Object = MibTableColumn
wmanIf2BsSsPkmV2TekNLifetime = _WmanIf2BsSsPkmV2TekNLifetime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 3, 1, 10),
    _WmanIf2BsSsPkmV2TekNLifetime_Type()
)
wmanIf2BsSsPkmV2TekNLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2TekNLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2TekNLifetime.setUnits("seconds")
_WmanIf2BsSsPkmV2TekInvalidError_Type = WmanIf2PkmErrorCode
_WmanIf2BsSsPkmV2TekInvalidError_Object = MibTableColumn
wmanIf2BsSsPkmV2TekInvalidError = _WmanIf2BsSsPkmV2TekInvalidError_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 3, 1, 11),
    _WmanIf2BsSsPkmV2TekInvalidError_Type()
)
wmanIf2BsSsPkmV2TekInvalidError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2TekInvalidError.setStatus("current")
_WmanIf2BsSsPkmV2TekN_1ExpireTime_Type = DateAndTime
_WmanIf2BsSsPkmV2TekN_1ExpireTime_Object = MibTableColumn
wmanIf2BsSsPkmV2TekN_1ExpireTime = _WmanIf2BsSsPkmV2TekN_1ExpireTime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 3, 1, 12),
    _WmanIf2BsSsPkmV2TekN_1ExpireTime_Type()
)
wmanIf2BsSsPkmV2TekN_1ExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2TekN_1ExpireTime.setStatus("current")
_WmanIf2BsSsPkmV2TekNExpireTime_Type = DateAndTime
_WmanIf2BsSsPkmV2TekNExpireTime_Object = MibTableColumn
wmanIf2BsSsPkmV2TekNExpireTime = _WmanIf2BsSsPkmV2TekNExpireTime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 3, 1, 13),
    _WmanIf2BsSsPkmV2TekNExpireTime_Type()
)
wmanIf2BsSsPkmV2TekNExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2TekNExpireTime.setStatus("current")
_WmanIf2BsSsPkmV23wayHandshakeTable_Object = MibTable
wmanIf2BsSsPkmV23wayHandshakeTable = _WmanIf2BsSsPkmV23wayHandshakeTable_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 4)
)
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV23wayHandshakeTable.setStatus("current")
_WmanIf2BsSsPkmV23wayHandshakeEntry_Object = MibTableRow
wmanIf2BsSsPkmV23wayHandshakeEntry = _WmanIf2BsSsPkmV23wayHandshakeEntry_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 4, 1)
)
wmanIf2BsSsPkmV23wayHandshakeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2-BS-MIB", "wmanIf2BsSsMacAddress"),
)
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV23wayHandshakeEntry.setStatus("current")


class _WmanIf2BsSsPkmV2SaTekBsRandom_Type(OctetString):
    """Custom type wmanIf2BsSsPkmV2SaTekBsRandom based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_WmanIf2BsSsPkmV2SaTekBsRandom_Type.__name__ = "OctetString"
_WmanIf2BsSsPkmV2SaTekBsRandom_Object = MibTableColumn
wmanIf2BsSsPkmV2SaTekBsRandom = _WmanIf2BsSsPkmV2SaTekBsRandom_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 4, 1, 1),
    _WmanIf2BsSsPkmV2SaTekBsRandom_Type()
)
wmanIf2BsSsPkmV2SaTekBsRandom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2SaTekBsRandom.setStatus("current")


class _WmanIf2BsSsPkmV2SaTekAkSequenceNumber_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV2SaTekAkSequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2BsSsPkmV2SaTekAkSequenceNumber_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV2SaTekAkSequenceNumber_Object = MibTableColumn
wmanIf2BsSsPkmV2SaTekAkSequenceNumber = _WmanIf2BsSsPkmV2SaTekAkSequenceNumber_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 4, 1, 2),
    _WmanIf2BsSsPkmV2SaTekAkSequenceNumber_Type()
)
wmanIf2BsSsPkmV2SaTekAkSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2SaTekAkSequenceNumber.setStatus("current")


class _WmanIf2BsSsPkmV2SaTekAkId_Type(OctetString):
    """Custom type wmanIf2BsSsPkmV2SaTekAkId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_WmanIf2BsSsPkmV2SaTekAkId_Type.__name__ = "OctetString"
_WmanIf2BsSsPkmV2SaTekAkId_Object = MibTableColumn
wmanIf2BsSsPkmV2SaTekAkId = _WmanIf2BsSsPkmV2SaTekAkId_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 4, 1, 3),
    _WmanIf2BsSsPkmV2SaTekAkId_Type()
)
wmanIf2BsSsPkmV2SaTekAkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2SaTekAkId.setStatus("current")


class _WmanIf2BsSsPkmV2KeyLifetime_Type(Integer32):
    """Custom type wmanIf2BsSsPkmV2KeyLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_WmanIf2BsSsPkmV2KeyLifetime_Type.__name__ = "Integer32"
_WmanIf2BsSsPkmV2KeyLifetime_Object = MibTableColumn
wmanIf2BsSsPkmV2KeyLifetime = _WmanIf2BsSsPkmV2KeyLifetime_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 4, 1, 4),
    _WmanIf2BsSsPkmV2KeyLifetime_Type()
)
wmanIf2BsSsPkmV2KeyLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2KeyLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2KeyLifetime.setUnits("seconds")


class _WmanIf2BsSsPkmV2SaTekMsRandom_Type(OctetString):
    """Custom type wmanIf2BsSsPkmV2SaTekMsRandom based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_WmanIf2BsSsPkmV2SaTekMsRandom_Type.__name__ = "OctetString"
_WmanIf2BsSsPkmV2SaTekMsRandom_Object = MibTableColumn
wmanIf2BsSsPkmV2SaTekMsRandom = _WmanIf2BsSsPkmV2SaTekMsRandom_Object(
    (1, 0, 8802, 16, 2, 1, 5, 4, 4, 1, 5),
    _WmanIf2BsSsPkmV2SaTekMsRandom_Type()
)
wmanIf2BsSsPkmV2SaTekMsRandom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmV2SaTekMsRandom.setStatus("current")
_WmanIf2MibConformance_ObjectIdentity = ObjectIdentity
wmanIf2MibConformance = _WmanIf2MibConformance_ObjectIdentity(
    (1, 0, 8802, 16, 2, 2)
)
_WmanIf2BsMibGroups_ObjectIdentity = ObjectIdentity
wmanIf2BsMibGroups = _WmanIf2BsMibGroups_ObjectIdentity(
    (1, 0, 8802, 16, 2, 2, 1)
)
_WmanIf2BsMibCompliances_ObjectIdentity = ObjectIdentity
wmanIf2BsMibCompliances = _WmanIf2BsMibCompliances_ObjectIdentity(
    (1, 0, 8802, 16, 2, 2, 2)
)
wmanIf2BsRegisteredSsEntry.registerAugmentions(
    ("WMAN-IF2-BS-MIB",
     "wmanIf2BsSsReqCapabilitiesEntry")
)
wmanIf2BsSsReqCapabilitiesEntry.setIndexNames(*wmanIf2BsRegisteredSsEntry.getIndexNames())
wmanIf2BsRegisteredSsEntry.registerAugmentions(
    ("WMAN-IF2-BS-MIB",
     "wmanIf2BsSsRspCapabilitiesEntry")
)
wmanIf2BsSsRspCapabilitiesEntry.setIndexNames(*wmanIf2BsRegisteredSsEntry.getIndexNames())

# Managed Objects groups

wmanIf2MibBsGroup = ObjectGroup(
    (1, 0, 8802, 16, 2, 2, 1, 1)
)
wmanIf2MibBsGroup.setObjects(
      *(("WMAN-IF2-BS-MIB", "wmanIf2BsSsBasicCid"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsPrimaryCid"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsSecondaryCid"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsManagementSupport"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsIpManagementMode"),
        ("WMAN-IF2-BS-MIB", "wmanIf2Bs2ndMgmtDlQoSProfileIndex"),
        ("WMAN-IF2-BS-MIB", "wmanIf2Bs2ndMgmtUlQoSProfileIndex"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsAutoSfidEnabled"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsAutoSfidRangeMin"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsAutoSfidRangeMax"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsResetSector"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSs2ndMgmtArqEnable"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSs2ndMgmtArqWindowSize"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSs2ndMgmtArqDnLinkTxDelay"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSs2ndMgmtArqUpLinkTxDelay"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSs2ndMgmtArqDnLinkRxDelay"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSs2ndMgmtArqUpLinkRxDelay"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSs2ndMgmtArqBlockLifetime"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSs2ndMgmtArqSyncLossTimeout"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSs2ndMgmtArqDeliverInOrder"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSs2ndMgmtArqRxPurgeTimeout"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSs2ndMgmtArqBlockSize"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsVendorIdEncoding"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsAasBroadcastPermission"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsMaxTxPowerBpsk"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsMaxTxPowerQpsk"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsMaxTxPower16Qam"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsMaxTxPower64Qam"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsMacVersion"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsDcdInterval"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsUcdInterval"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsUcdTransition"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsDcdTransition"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsInitialRangingInterval"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsULMapProcTime"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsRangRespProcTime"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsT9Timeout"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsT13Timeout"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsT15Timeout"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsT17Timeout"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsT27IdleTimer"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsT27ActiveTimer"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsHistogramIndex"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsChannelNumber"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsStartFrame"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsDuration"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsBasicReport"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsMeanCinrReport"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsMeanRssiReport"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsStdDeviationCinrReport"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsStdDeviationRssiReport"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsActionsResetSs"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsActionsAbortSs"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsActionsOverrideDnFreq"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsActionsOverrideChannelId"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsActionsDeReRegSs"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsActionsDeReRegSsCode"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsActionsRowStatus"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsPkmV1AkLifetime"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsPkmV1TekLifetime"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsPkmV1SelfSigManufCertTrust"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsPkmV1CheckCertValidityPeriods"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsTrapControlRegister"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsStatusTrapControlRegister"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsRssiLowThreshold"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsRssiHighThreshold"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsNotificationMacAddr"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsStatusValue"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsStatusInfo"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsDynamicServiceType"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsDynamicServiceFailReason"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsRssiStatus"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsRssiStatusInfo"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsRegisterStatus"))
)
if mibBuilder.loadTexts:
    wmanIf2MibBsGroup.setStatus("current")

wmanIf2MibBsAasGroup = ObjectGroup(
    (1, 0, 8802, 16, 2, 2, 1, 2)
)
wmanIf2MibBsAasGroup.setObjects(
      *(("WMAN-IF2-BS-MIB", "wmanIf2BsAasChanFbckReqFreq"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsAasBeamSelectFreq"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsAasChanFbckReqResolution"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsAasBeamReqResolution"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsAasNumOptDiversityZones"))
)
if mibBuilder.loadTexts:
    wmanIf2MibBsAasGroup.setStatus("current")

wmanIf2MibBsOfdmGroup = ObjectGroup(
    (1, 0, 8802, 16, 2, 2, 1, 3)
)
wmanIf2MibBsOfdmGroup.setObjects(
      *(("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmBwReqOppSize"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmRangReqOppSize"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmNumSubChReqRegionFull"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmNumSymbolsReqRegionFull"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmSubChFocusCtCode"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmFrameDurationCode"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmUcdFecCodeType"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmFocusCtPowerBoost"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmUcdTcsEnable"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmUcdBurstProfileRowStatus"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmDcdFecCodeType"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmTcsEnable"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmDcdBurstProfileRowStatus"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmMinReqRegionFullTxOpp"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmMinFocusedCtTxOpp"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmMaxRoundTripDelay"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmRangeAbortTimingThold"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmRangeAbortPowerThold"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmRangeAbortFreqThold"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmDnlkRateId"))
)
if mibBuilder.loadTexts:
    wmanIf2MibBsOfdmGroup.setStatus("current")

wmanIf2MibBsOfdmaGroup = ObjectGroup(
    (1, 0, 8802, 16, 2, 2, 1, 4)
)
wmanIf2MibBsOfdmaGroup.setObjects(
      *(("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmaStartOfRngCodes"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmaPermutationBase"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmaULAllocSubchBitmap"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmaOptPermULAllocSubchBitmap"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmaBandAMCAllocThreshold"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmaBandAMCReleaseThreshold"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmaBandAMCAllocTimer"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmaBandAMCReleaseTimer"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmaBandStatRepMAXPeriod"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmaBandAMCRetryTimer"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmaFrameDurationCode"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmaUcdFecCodeType"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmaRangingDataRatio"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmaUcdBurstProfileRowStatus"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmaDcdFecCodeType"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsOfdmaDcdBurstProfileRowStatus"))
)
if mibBuilder.loadTexts:
    wmanIf2MibBsOfdmaGroup.setStatus("current")


# Notification objects

wmanIf2BsSsStatusNotificationTrap = NotificationType(
    (1, 0, 8802, 16, 2, 1, 1, 2, 0, 1)
)
wmanIf2BsSsStatusNotificationTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsNotificationMacAddr"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsStatusValue"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsStatusInfo"))
)
if mibBuilder.loadTexts:
    wmanIf2BsSsStatusNotificationTrap.setStatus(
        "current"
    )

wmanIf2BsSsRssiStatusChangeTrap = NotificationType(
    (1, 0, 8802, 16, 2, 1, 1, 2, 0, 2)
)
wmanIf2BsSsRssiStatusChangeTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsNotificationMacAddr"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsRssiStatus"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsRssiStatusInfo"))
)
if mibBuilder.loadTexts:
    wmanIf2BsSsRssiStatusChangeTrap.setStatus(
        "current"
    )

wmanIf2BsSsPkmFailTrap = NotificationType(
    (1, 0, 8802, 16, 2, 1, 1, 2, 0, 3)
)
wmanIf2BsSsPkmFailTrap.setObjects(
    ("WMAN-IF2-BS-MIB", "wmanIf2BsSsNotificationMacAddr")
)
if mibBuilder.loadTexts:
    wmanIf2BsSsPkmFailTrap.setStatus(
        "current"
    )

wmanIf2BsSsDynamicServiceFailTrap = NotificationType(
    (1, 0, 8802, 16, 2, 1, 1, 2, 0, 4)
)
wmanIf2BsSsDynamicServiceFailTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsNotificationMacAddr"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsDynamicServiceType"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsDynamicServiceFailReason"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsDynamicServiceFailSfid"))
)
if mibBuilder.loadTexts:
    wmanIf2BsSsDynamicServiceFailTrap.setStatus(
        "current"
    )

wmanIf2BsSsRegisterTrap = NotificationType(
    (1, 0, 8802, 16, 2, 1, 1, 2, 0, 5)
)
wmanIf2BsSsRegisterTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsNotificationMacAddr"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsRegisterStatus"))
)
if mibBuilder.loadTexts:
    wmanIf2BsSsRegisterTrap.setStatus(
        "current"
    )

wmanIf2BsPerformanceCountersTrap = NotificationType(
    (1, 0, 8802, 16, 2, 1, 1, 2, 0, 6)
)
wmanIf2BsPerformanceCountersTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsAuthenAttempt"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsAuthenSuccess"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsAuthenSuccessRate"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsRangingAttempt"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsRangingSuccess"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsRangingSuccessRate"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsAvgDlUserThroughput"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsAvgUlUserThroughput"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsAvgDlMacThroughput"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsAvgUlMacThroughput"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsAvgDlPhyThroughput"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsAvgUlPhyThroughput"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsPeakDlUserThroughput"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsPeakUlUserThroughput"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsPeakDlMacThroughput"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsPeakUlMacThroughput"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsPeakDlPhyThroughput"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsPeakUlPhyThroughput"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsAvgDlCellEdgeThroughput"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsAvgUlCellEdgeThroughput"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsDataRateMeasurements"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsAvgNetworkEntryTime"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsMaxNetworkEntryTime"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsAvgNetworkReEntryTime"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsMaxNetworkReEntryTime"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsNumOfNetworkEntries"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsNumOfNetworkReEntries"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsDlPacketsSend"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsDlPacketsErrored"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsDlPacketErrorRate"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsEventNotificationTime"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsHandoverAttempt"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsHandoverSuccess"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsHandoverSuccessRate"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsHandoverCancel"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsHandoverReject"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsHandoverCancelRate"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsHandoverRejectRate"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsAvgHandoverTime"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsUnexpectedHandover"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsActiveUsers"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsPeakNormalModeUsers"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsPeakSleepModeUsers"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsPeakIdleModeUsers"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsBasicAndPrimaryCids"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsMaximumUserCids"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsAvgUserCids"))
)
if mibBuilder.loadTexts:
    wmanIf2BsPerformanceCountersTrap.setStatus(
        "current"
    )


# Notifications groups

wmanIf2MibBsNotificationGroup = NotificationGroup(
    (1, 0, 8802, 16, 2, 2, 1, 5)
)
wmanIf2MibBsNotificationGroup.setObjects(
      *(("WMAN-IF2-BS-MIB", "wmanIf2BsSsStatusNotificationTrap"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsRssiStatusChangeTrap"),
        ("WMAN-IF2-BS-MIB", "wmanIf2BsSsPkmFailTrap"))
)
if mibBuilder.loadTexts:
    wmanIf2MibBsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

wmanIf2BsMibCompliance = ModuleCompliance(
    (1, 0, 8802, 16, 2, 2, 2, 1)
)
wmanIf2BsMibCompliance.setObjects(
      *(("WMAN-IF2-BS-MIB", "wmanIf2MibBsGroup"),
        ("WMAN-IF2-BS-MIB", "wmanIf2MibBsAasGroup"),
        ("WMAN-IF2-BS-MIB", "wmanIf2MibBsOfdmGroup"),
        ("WMAN-IF2-BS-MIB", "wmanIf2MibBsOfdmaGroup"),
        ("WMAN-IF2-BS-MIB", "wmanIf2MibBsNotificationGroup"))
)
if mibBuilder.loadTexts:
    wmanIf2BsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WMAN-IF2-BS-MIB",
    **{"WmanIf2MacVersion": WmanIf2MacVersion,
       "WmanIf2CidType": WmanIf2CidType,
       "WmanIf2DataEncryptAlgId": WmanIf2DataEncryptAlgId,
       "WmanIf2DataAuthAlgId": WmanIf2DataAuthAlgId,
       "WmanIf2TekEncryptAlgId": WmanIf2TekEncryptAlgId,
       "WmanIf2PkmErrorCode": WmanIf2PkmErrorCode,
       "WmanIf2SaType": WmanIf2SaType,
       "WmanIf2CertificateStat": WmanIf2CertificateStat,
       "WmanIf2ChannelNumber": WmanIf2ChannelNumber,
       "WmanIf2OfdmFecCodeType": WmanIf2OfdmFecCodeType,
       "WmanIf2OfdmaUcdFecCode": WmanIf2OfdmaUcdFecCode,
       "WmanIf2OfdmaDcdFecCode": WmanIf2OfdmaDcdFecCode,
       "WmanIf2NumOfCid": WmanIf2NumOfCid,
       "WmanIf2MaxDsxFlowType": WmanIf2MaxDsxFlowType,
       "WmanIf2MaxMcaFlowType": WmanIf2MaxMcaFlowType,
       "WmanIf2MaxMcpGroupCid": WmanIf2MaxMcpGroupCid,
       "WmanIf2MaxPkmFlowType": WmanIf2MaxPkmFlowType,
       "WmanIf2MaxNumOfSaType": WmanIf2MaxNumOfSaType,
       "WmanIf2MaxClassifiers": WmanIf2MaxClassifiers,
       "WmanIf2SsTransitionGap": WmanIf2SsTransitionGap,
       "WmanIf2MaxTxPowerType": WmanIf2MaxTxPowerType,
       "WmanIf2BsIdType": WmanIf2BsIdType,
       "WmanIf2Ipv6FlowLabel": WmanIf2Ipv6FlowLabel,
       "WmanIf2OfdmaDemMimo": WmanIf2OfdmaDemMimo,
       "WmanIf2OfdmaDemoMimo": WmanIf2OfdmaDemoMimo,
       "WmanIf2OfdmaUlMimo": WmanIf2OfdmaUlMimo,
       "WmanIf2SdmaPilotCap": WmanIf2SdmaPilotCap,
       "WmanIf2HarqAckDelay": WmanIf2HarqAckDelay,
       "WmanIf2AasBeamSel": WmanIf2AasBeamSel,
       "WmanIf2MaxMacLevel": WmanIf2MaxMacLevel,
       "WmanIfPermutationType": WmanIfPermutationType,
       "WmanIf2HoSupportType": WmanIf2HoSupportType,
       "WmanIf2ActionRule": WmanIf2ActionRule,
       "WmanIf2LinkDirection": WmanIf2LinkDirection,
       "WmanIf2SaServiceType": WmanIf2SaServiceType,
       "WmanIf2GlobalSrvClass": WmanIf2GlobalSrvClass,
       "WmanIf2OfdmaFftSize": WmanIf2OfdmaFftSize,
       "WmanIf2OfdmFftSize": WmanIf2OfdmFftSize,
       "WmanIf2BsSsCapType": WmanIf2BsSsCapType,
       "WmanIf2BsCapType": WmanIf2BsCapType,
       "WmanIf2MaxNumBurstTx": WmanIf2MaxNumBurstTx,
       "WmanIf2MaxNumProvSf": WmanIf2MaxNumProvSf,
       "WmanIf2MinNumFrmsPwrCtrl": WmanIf2MinNumFrmsPwrCtrl,
       "WmanIf2OfdmaNoHarqChan": WmanIf2OfdmaNoHarqChan,
       "WmanIf2BasicCapOptions": WmanIf2BasicCapOptions,
       "WmanIf2OfdmCapOptions": WmanIf2OfdmCapOptions,
       "WmanIf2OfdmaCapOptions": WmanIf2OfdmaCapOptions,
       "wmanIf2BsMib": wmanIf2BsMib,
       "wmanIf2MibObjects": wmanIf2MibObjects,
       "wmanIf2BsFm": wmanIf2BsFm,
       "wmanIf2BsTrapControl": wmanIf2BsTrapControl,
       "wmanIf2BsTrapControlRegister": wmanIf2BsTrapControlRegister,
       "wmanIf2BsStatusTrapControlRegister": wmanIf2BsStatusTrapControlRegister,
       "wmanIf2BsThresholdConfigTable": wmanIf2BsThresholdConfigTable,
       "wmanIf2BsThresholdConfigEntry": wmanIf2BsThresholdConfigEntry,
       "wmanIf2BsRssiLowThreshold": wmanIf2BsRssiLowThreshold,
       "wmanIf2BsRssiHighThreshold": wmanIf2BsRssiHighThreshold,
       "wmanIf2BsTrapDefinitions": wmanIf2BsTrapDefinitions,
       "wmanIf2BsTrapPrefix": wmanIf2BsTrapPrefix,
       "wmanIf2BsSsStatusNotificationTrap": wmanIf2BsSsStatusNotificationTrap,
       "wmanIf2BsSsRssiStatusChangeTrap": wmanIf2BsSsRssiStatusChangeTrap,
       "wmanIf2BsSsPkmFailTrap": wmanIf2BsSsPkmFailTrap,
       "wmanIf2BsSsDynamicServiceFailTrap": wmanIf2BsSsDynamicServiceFailTrap,
       "wmanIf2BsSsRegisterTrap": wmanIf2BsSsRegisterTrap,
       "wmanIf2BsPerformanceCountersTrap": wmanIf2BsPerformanceCountersTrap,
       "wmanIf2BsSsNotificationObjectsTable": wmanIf2BsSsNotificationObjectsTable,
       "wmanIf2BsSsNotificationObjectsEntry": wmanIf2BsSsNotificationObjectsEntry,
       "wmanIf2BsSsNotificationMacAddr": wmanIf2BsSsNotificationMacAddr,
       "wmanIf2BsSsStatusValue": wmanIf2BsSsStatusValue,
       "wmanIf2BsSsStatusInfo": wmanIf2BsSsStatusInfo,
       "wmanIf2BsDynamicServiceType": wmanIf2BsDynamicServiceType,
       "wmanIf2BsDynamicServiceFailReason": wmanIf2BsDynamicServiceFailReason,
       "wmanIf2BsSsRssiStatus": wmanIf2BsSsRssiStatus,
       "wmanIf2BsSsRssiStatusInfo": wmanIf2BsSsRssiStatusInfo,
       "wmanIf2BsSsRegisterStatus": wmanIf2BsSsRegisterStatus,
       "wmanIf2BsDynamicServiceFailSfid": wmanIf2BsDynamicServiceFailSfid,
       "wmanIf2BsEventNotificationTime": wmanIf2BsEventNotificationTime,
       "wmanIf2BsCm": wmanIf2BsCm,
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
       "wmanIf2BsSsULMapProcTime": wmanIf2BsSsULMapProcTime,
       "wmanIf2BsSsRangRespProcTime": wmanIf2BsSsRangRespProcTime,
       "wmanIf2BsT9Timeout": wmanIf2BsT9Timeout,
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
       "wmanIf2BsInvitedRangRetries": wmanIf2BsInvitedRangRetries,
       "wmanIf2BsDSxReqRetries": wmanIf2BsDSxReqRetries,
       "wmanIf2BsDSxRespRetries": wmanIf2BsDSxRespRetries,
       "wmanIf2BsT7Timeout": wmanIf2BsT7Timeout,
       "wmanIf2BsT8Timeout": wmanIf2BsT8Timeout,
       "wmanIf2BsT10Timeout": wmanIf2BsT10Timeout,
       "wmanIf2BsT22Timeout": wmanIf2BsT22Timeout,
       "wmanIf2BsSsReqCapabilitiesTable": wmanIf2BsSsReqCapabilitiesTable,
       "wmanIf2BsSsReqCapabilitiesEntry": wmanIf2BsSsReqCapabilitiesEntry,
       "wmanIf2BsSsReqCapUplinkCidSupport": wmanIf2BsSsReqCapUplinkCidSupport,
       "wmanIf2BsSsReqCapDsxFlowControl": wmanIf2BsSsReqCapDsxFlowControl,
       "wmanIf2BsSsReqCapMcaFlowControl": wmanIf2BsSsReqCapMcaFlowControl,
       "wmanIf2BsSsReqCapMcpGroupCidSupport": wmanIf2BsSsReqCapMcpGroupCidSupport,
       "wmanIf2BsSsReqCapPkmFlowControl": wmanIf2BsSsReqCapPkmFlowControl,
       "wmanIf2BsSsReqCapMaxNumOfSupportedSA": wmanIf2BsSsReqCapMaxNumOfSupportedSA,
       "wmanIf2BsSsReqCapMaxNumOfClassifier": wmanIf2BsSsReqCapMaxNumOfClassifier,
       "wmanIf2BsSsReqCapTtgTransitionGap": wmanIf2BsSsReqCapTtgTransitionGap,
       "wmanIf2BsSsReqCapRtgTransitionGap": wmanIf2BsSsReqCapRtgTransitionGap,
       "wmanIf2BsSsReqCapDownlinkCidSupport": wmanIf2BsSsReqCapDownlinkCidSupport,
       "wmanIf2BsSsReqCapMaxNumBurstToMs": wmanIf2BsSsReqCapMaxNumBurstToMs,
       "wmanIf2BsSsReqCapMaxMacLevelDlFrame": wmanIf2BsSsReqCapMaxMacLevelDlFrame,
       "wmanIf2BsSsReqCapMaxMacLevelUlFrame": wmanIf2BsSsReqCapMaxMacLevelUlFrame,
       "wmanIf2BsSsReqCapPnWindowSize": wmanIf2BsSsReqCapPnWindowSize,
       "wmanIf2BsSsOfdmReqCapLoopPwrControlSw": wmanIf2BsSsOfdmReqCapLoopPwrControlSw,
       "wmanIf2BsSsOfdmaReqCapSdmaPilot": wmanIf2BsSsOfdmaReqCapSdmaPilot,
       "wmanIf2BsSsOfdmaReqCapNoUlHarqChannel": wmanIf2BsSsOfdmaReqCapNoUlHarqChannel,
       "wmanIf2BsSsOfdmaReqCapNoDlHarqChannel": wmanIf2BsSsOfdmaReqCapNoDlHarqChannel,
       "wmanIf2BsSsReqCapOptionsBasic": wmanIf2BsSsReqCapOptionsBasic,
       "wmanIf2BsSsReqCapOptionsOfdm": wmanIf2BsSsReqCapOptionsOfdm,
       "wmanIf2BsSsReqCapOptionsOfdma": wmanIf2BsSsReqCapOptionsOfdma,
       "wmanIf2BsSsRspCapabilitiesTable": wmanIf2BsSsRspCapabilitiesTable,
       "wmanIf2BsSsRspCapabilitiesEntry": wmanIf2BsSsRspCapabilitiesEntry,
       "wmanIf2BsSsRspCapUplinkCidSupport": wmanIf2BsSsRspCapUplinkCidSupport,
       "wmanIf2BsSsRspCapDsxFlowControl": wmanIf2BsSsRspCapDsxFlowControl,
       "wmanIf2BsSsRspCapMcaFlowControl": wmanIf2BsSsRspCapMcaFlowControl,
       "wmanIf2BsSsRspCapMcpGroupCidSupport": wmanIf2BsSsRspCapMcpGroupCidSupport,
       "wmanIf2BsSsRspCapPkmFlowControl": wmanIf2BsSsRspCapPkmFlowControl,
       "wmanIf2BsSsRspCapMaxNumOfSupportedSA": wmanIf2BsSsRspCapMaxNumOfSupportedSA,
       "wmanIf2BsSsRspCapMaxNumOfClassifier": wmanIf2BsSsRspCapMaxNumOfClassifier,
       "wmanIf2BsSsRspCapTtgTransitionGap": wmanIf2BsSsRspCapTtgTransitionGap,
       "wmanIf2BsSsRspCapRtgTransitionGap": wmanIf2BsSsRspCapRtgTransitionGap,
       "wmanIf2BsSsRspCapDownlinkCidSupport": wmanIf2BsSsRspCapDownlinkCidSupport,
       "wmanIf2BsSsRspCapMaxNumBurstToMs": wmanIf2BsSsRspCapMaxNumBurstToMs,
       "wmanIf2BsSsRspCapMaxMacLevelDlFrame": wmanIf2BsSsRspCapMaxMacLevelDlFrame,
       "wmanIf2BsSsRspCapMaxMacLevelUlFrame": wmanIf2BsSsRspCapMaxMacLevelUlFrame,
       "wmanIf2BsSsRspCapNumOfProvisionedSf": wmanIf2BsSsRspCapNumOfProvisionedSf,
       "wmanIf2BsSsRspCapPnWindowSize": wmanIf2BsSsRspCapPnWindowSize,
       "wmanIf2BsSsOfdmRspCapLoopPwrControlSw": wmanIf2BsSsOfdmRspCapLoopPwrControlSw,
       "wmanIf2BsSsOfdmaRspCapSdmaPilot": wmanIf2BsSsOfdmaRspCapSdmaPilot,
       "wmanIf2BsSsOfdmaRspCapNoUlHarqChannel": wmanIf2BsSsOfdmaRspCapNoUlHarqChannel,
       "wmanIf2BsSsOfdmaRspCapNoDlHarqChannel": wmanIf2BsSsOfdmaRspCapNoDlHarqChannel,
       "wmanIf2BsSsRspCapOptionsBasic": wmanIf2BsSsRspCapOptionsBasic,
       "wmanIf2BsSsRspCapOptionsOfdm": wmanIf2BsSsRspCapOptionsOfdm,
       "wmanIf2BsSsRspCapOptionsOfdma": wmanIf2BsSsRspCapOptionsOfdma,
       "wmanIf2BsBasicCapabilitiesTable": wmanIf2BsBasicCapabilitiesTable,
       "wmanIf2BsBasicCapabilitiesEntry": wmanIf2BsBasicCapabilitiesEntry,
       "wmanIf2BsCapUplinkCidSupport": wmanIf2BsCapUplinkCidSupport,
       "wmanIf2BsCapDsxFlowControl": wmanIf2BsCapDsxFlowControl,
       "wmanIf2BsCapMcaFlowControl": wmanIf2BsCapMcaFlowControl,
       "wmanIf2BsCapMcpGroupCidSupport": wmanIf2BsCapMcpGroupCidSupport,
       "wmanIf2BsCapPkmFlowControl": wmanIf2BsCapPkmFlowControl,
       "wmanIf2BsCapMaxNumOfSupportedSA": wmanIf2BsCapMaxNumOfSupportedSA,
       "wmanIf2BsCapMaxNumOfClassifier": wmanIf2BsCapMaxNumOfClassifier,
       "wmanIf2BsCapTtgTransitionGap": wmanIf2BsCapTtgTransitionGap,
       "wmanIf2BsCapRtgTransitionGap": wmanIf2BsCapRtgTransitionGap,
       "wmanIf2BsCapDownlinkCidSupport": wmanIf2BsCapDownlinkCidSupport,
       "wmanIf2BsCapMaxNumBurstToMs": wmanIf2BsCapMaxNumBurstToMs,
       "wmanIf2BsCapMaxMacLevelDlFrame": wmanIf2BsCapMaxMacLevelDlFrame,
       "wmanIf2BsCapMaxMacLevelUlFrame": wmanIf2BsCapMaxMacLevelUlFrame,
       "wmanIf2BsCapNumOfProvisionedSf": wmanIf2BsCapNumOfProvisionedSf,
       "wmanIf2BsCapPnWindowSize": wmanIf2BsCapPnWindowSize,
       "wmanIf2BsOfdmCapLoopPwrControlSw": wmanIf2BsOfdmCapLoopPwrControlSw,
       "wmanIf2BsOfdmaCapSdmaPilot": wmanIf2BsOfdmaCapSdmaPilot,
       "wmanIf2BsOfdmaCapNoUlHarqChannel": wmanIf2BsOfdmaCapNoUlHarqChannel,
       "wmanIf2BsOfdmaCapNoDlHarqChannel": wmanIf2BsOfdmaCapNoDlHarqChannel,
       "wmanIf2BsCapOptionsBasic": wmanIf2BsCapOptionsBasic,
       "wmanIf2BsCapOptionsOfdm": wmanIf2BsCapOptionsOfdm,
       "wmanIf2BsCapOptionsOfdma": wmanIf2BsCapOptionsOfdma,
       "wmanIf2BsCapabilitiesConfigTable": wmanIf2BsCapabilitiesConfigTable,
       "wmanIf2BsCapabilitiesConfigEntry": wmanIf2BsCapabilitiesConfigEntry,
       "wmanIf2BsCapCfgUplinkCidSupport": wmanIf2BsCapCfgUplinkCidSupport,
       "wmanIf2BsCapCfgDsxFlowControl": wmanIf2BsCapCfgDsxFlowControl,
       "wmanIf2BsCapCfgMcaFlowControl": wmanIf2BsCapCfgMcaFlowControl,
       "wmanIf2BsCapCfgMcpGroupCidSupport": wmanIf2BsCapCfgMcpGroupCidSupport,
       "wmanIf2BsCapCfgPkmFlowControl": wmanIf2BsCapCfgPkmFlowControl,
       "wmanIf2BsCapCfgMaxNumOfSupportedSA": wmanIf2BsCapCfgMaxNumOfSupportedSA,
       "wmanIf2BsCapCfgMaxNumOfClassifier": wmanIf2BsCapCfgMaxNumOfClassifier,
       "wmanIf2BsCapCfgTtgTransitionGap": wmanIf2BsCapCfgTtgTransitionGap,
       "wmanIf2BsCapCfgRtgTransitionGap": wmanIf2BsCapCfgRtgTransitionGap,
       "wmanIf2BsCapCfgDownlinkCidSupport": wmanIf2BsCapCfgDownlinkCidSupport,
       "wmanIf2BsCapCfgMaxNumBurstToMs": wmanIf2BsCapCfgMaxNumBurstToMs,
       "wmanIf2BsCapCfgMaxMacLevelDlFrame": wmanIf2BsCapCfgMaxMacLevelDlFrame,
       "wmanIf2BsCapCfgMaxMacLevelUlFrame": wmanIf2BsCapCfgMaxMacLevelUlFrame,
       "wmanIf2BsCapCfgNumOfProvisionedSf": wmanIf2BsCapCfgNumOfProvisionedSf,
       "wmanIf2BsCapCfgPnWindowSize": wmanIf2BsCapCfgPnWindowSize,
       "wmanIf2BsOfdmCapCfgLoopPwrControlSw": wmanIf2BsOfdmCapCfgLoopPwrControlSw,
       "wmanIf2BsOfdmaCapCfgSdmaPilot": wmanIf2BsOfdmaCapCfgSdmaPilot,
       "wmanIf2BsOfdmaCapCfgNoUlHarqChannel": wmanIf2BsOfdmaCapCfgNoUlHarqChannel,
       "wmanIf2BsOfdmaCapCfgNoDlHarqChannel": wmanIf2BsOfdmaCapCfgNoDlHarqChannel,
       "wmanIf2BsCapCfgOptionsBasic": wmanIf2BsCapCfgOptionsBasic,
       "wmanIf2BsCapCfgOptionsOfdm": wmanIf2BsCapCfgOptionsOfdm,
       "wmanIf2BsCapCfgOptionsOfdma": wmanIf2BsCapCfgOptionsOfdma,
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
       "wmanIf2BsMulticastPollingTable": wmanIf2BsMulticastPollingTable,
       "wmanIf2BsMulticastPollingEntry": wmanIf2BsMulticastPollingEntry,
       "wmanIf2BsMulticastPollingCid": wmanIf2BsMulticastPollingCid,
       "wmanIf2BsMulticastGroupType": wmanIf2BsMulticastGroupType,
       "wmanIf2BsPeriodAllocationParameterM": wmanIf2BsPeriodAllocationParameterM,
       "wmanIf2BsPeriodAllocationParameterK": wmanIf2BsPeriodAllocationParameterK,
       "wmanIf2BsPeriodAllocationParameterN": wmanIf2BsPeriodAllocationParameterN,
       "wmanIf2BsPeriodicAllocationType": wmanIf2BsPeriodicAllocationType,
       "wmanIf2BsPhy": wmanIf2BsPhy,
       "wmanIf2BsCmnPhy": wmanIf2BsCmnPhy,
       "wmanIf2BsCmnPhyUplinkChannelTable": wmanIf2BsCmnPhyUplinkChannelTable,
       "wmanIf2BsCmnPhyUplinkChannelEntry": wmanIf2BsCmnPhyUplinkChannelEntry,
       "wmanIf2BsCmnPhyCtBasedResvTimeout": wmanIf2BsCmnPhyCtBasedResvTimeout,
       "wmanIf2BsCmnPhyUplinkCenterFreq": wmanIf2BsCmnPhyUplinkCenterFreq,
       "wmanIf2BsCmnPhyDownlinkChannelTable": wmanIf2BsCmnPhyDownlinkChannelTable,
       "wmanIf2BsCmnPhyDownlinkChannelEntry": wmanIf2BsCmnPhyDownlinkChannelEntry,
       "wmanIf2BsCmnPhyBsEIRP": wmanIf2BsCmnPhyBsEIRP,
       "wmanIf2BsCmnPhyChannelNumber": wmanIf2BsCmnPhyChannelNumber,
       "wmanIf2BsCmnPhyTTG": wmanIf2BsCmnPhyTTG,
       "wmanIf2BsCmnPhyRTG": wmanIf2BsCmnPhyRTG,
       "wmanIf2BsCmnPhyInitRngMaxRSS": wmanIf2BsCmnPhyInitRngMaxRSS,
       "wmanIf2BsCmnPhyDownlinkCenterFreq": wmanIf2BsCmnPhyDownlinkCenterFreq,
       "wmanIf2BsCmnPhyBsId": wmanIf2BsCmnPhyBsId,
       "wmanIf2BsCmnPhyMacVersion": wmanIf2BsCmnPhyMacVersion,
       "wmanIf2BsCmnPhyCyclicPrefix": wmanIf2BsCmnPhyCyclicPrefix,
       "wmanIf2BsOfdmPhy": wmanIf2BsOfdmPhy,
       "wmanIf2BsOfdmUplinkChannelTable": wmanIf2BsOfdmUplinkChannelTable,
       "wmanIf2BsOfdmUplinkChannelEntry": wmanIf2BsOfdmUplinkChannelEntry,
       "wmanIf2BsOfdmBwReqOppSize": wmanIf2BsOfdmBwReqOppSize,
       "wmanIf2BsOfdmRangReqOppSize": wmanIf2BsOfdmRangReqOppSize,
       "wmanIf2BsOfdmNumSubChReqRegionFull": wmanIf2BsOfdmNumSubChReqRegionFull,
       "wmanIf2BsOfdmNumSymbolsReqRegionFull": wmanIf2BsOfdmNumSymbolsReqRegionFull,
       "wmanIf2BsOfdmSubChFocusCtCode": wmanIf2BsOfdmSubChFocusCtCode,
       "wmanIf2BsOfdmDownlinkChannelTable": wmanIf2BsOfdmDownlinkChannelTable,
       "wmanIf2BsOfdmDownlinkChannelEntry": wmanIf2BsOfdmDownlinkChannelEntry,
       "wmanIf2BsOfdmFrameDurationCode": wmanIf2BsOfdmFrameDurationCode,
       "wmanIf2BsOfdmFftSize": wmanIf2BsOfdmFftSize,
       "wmanIf2BsOfdmUcdBurstProfileTable": wmanIf2BsOfdmUcdBurstProfileTable,
       "wmanIf2BsOfdmUcdBurstProfileEntry": wmanIf2BsOfdmUcdBurstProfileEntry,
       "wmanIf2BsOfdmUiucIndex": wmanIf2BsOfdmUiucIndex,
       "wmanIf2BsOfdmUcdFecCodeType": wmanIf2BsOfdmUcdFecCodeType,
       "wmanIf2BsOfdmFocusCtPowerBoost": wmanIf2BsOfdmFocusCtPowerBoost,
       "wmanIf2BsOfdmUcdTcsEnable": wmanIf2BsOfdmUcdTcsEnable,
       "wmanIf2BsOfdmUcdBurstProfileRowStatus": wmanIf2BsOfdmUcdBurstProfileRowStatus,
       "wmanIf2BsOfdmDcdBurstProfileTable": wmanIf2BsOfdmDcdBurstProfileTable,
       "wmanIf2BsOfdmDcdBurstProfileEntry": wmanIf2BsOfdmDcdBurstProfileEntry,
       "wmanIf2BsOfdmDiucIndex": wmanIf2BsOfdmDiucIndex,
       "wmanIf2BsOfdmDcdFecCodeType": wmanIf2BsOfdmDcdFecCodeType,
       "wmanIf2BsOfdmTcsEnable": wmanIf2BsOfdmTcsEnable,
       "wmanIf2BsOfdmDcdBurstProfileRowStatus": wmanIf2BsOfdmDcdBurstProfileRowStatus,
       "wmanIf2BsOfdmConfigurationTable": wmanIf2BsOfdmConfigurationTable,
       "wmanIf2BsOfdmConfigurationEntry": wmanIf2BsOfdmConfigurationEntry,
       "wmanIf2BsOfdmMinReqRegionFullTxOpp": wmanIf2BsOfdmMinReqRegionFullTxOpp,
       "wmanIf2BsOfdmMinFocusedCtTxOpp": wmanIf2BsOfdmMinFocusedCtTxOpp,
       "wmanIf2BsOfdmMaxRoundTripDelay": wmanIf2BsOfdmMaxRoundTripDelay,
       "wmanIf2BsOfdmRangeAbortTimingThold": wmanIf2BsOfdmRangeAbortTimingThold,
       "wmanIf2BsOfdmRangeAbortPowerThold": wmanIf2BsOfdmRangeAbortPowerThold,
       "wmanIf2BsOfdmRangeAbortFreqThold": wmanIf2BsOfdmRangeAbortFreqThold,
       "wmanIf2BsOfdmDnlkRateId": wmanIf2BsOfdmDnlkRateId,
       "wmanIf2BsOfdmaPhy": wmanIf2BsOfdmaPhy,
       "wmanIf2BsOfdmaUplinkChannelTable": wmanIf2BsOfdmaUplinkChannelTable,
       "wmanIf2BsOfdmaUplinkChannelEntry": wmanIf2BsOfdmaUplinkChannelEntry,
       "wmanIf2BsOfdmaStartOfRngCodes": wmanIf2BsOfdmaStartOfRngCodes,
       "wmanIf2BsOfdmaPermutationBase": wmanIf2BsOfdmaPermutationBase,
       "wmanIf2BsOfdmaULAllocSubchBitmap": wmanIf2BsOfdmaULAllocSubchBitmap,
       "wmanIf2BsOfdmaOptPermULAllocSubchBitmap": wmanIf2BsOfdmaOptPermULAllocSubchBitmap,
       "wmanIf2BsOfdmaBandAMCAllocThreshold": wmanIf2BsOfdmaBandAMCAllocThreshold,
       "wmanIf2BsOfdmaBandAMCReleaseThreshold": wmanIf2BsOfdmaBandAMCReleaseThreshold,
       "wmanIf2BsOfdmaBandAMCAllocTimer": wmanIf2BsOfdmaBandAMCAllocTimer,
       "wmanIf2BsOfdmaBandAMCReleaseTimer": wmanIf2BsOfdmaBandAMCReleaseTimer,
       "wmanIf2BsOfdmaBandStatRepMAXPeriod": wmanIf2BsOfdmaBandStatRepMAXPeriod,
       "wmanIf2BsOfdmaPerRngBackoffStart": wmanIf2BsOfdmaPerRngBackoffStart,
       "wmanIf2BsOfdmaPerRngBackoffEnd": wmanIf2BsOfdmaPerRngBackoffEnd,
       "wmanIf2BsOfdmaBandAMCRetryTimer": wmanIf2BsOfdmaBandAMCRetryTimer,
       "wmanIf2BsOfdmaInitRngCodes": wmanIf2BsOfdmaInitRngCodes,
       "wmanIf2BsOfdmaPeriodicRngCodes": wmanIf2BsOfdmaPeriodicRngCodes,
       "wmanIf2BsOfdmaBWReqCodes": wmanIf2BsOfdmaBWReqCodes,
       "wmanIf2BsOfdmaHandoverRangingStart": wmanIf2BsOfdmaHandoverRangingStart,
       "wmanIf2BsOfdmaHandoverRangingEnd": wmanIf2BsOfdmaHandoverRangingEnd,
       "wmanIf2BsOfdmaHARQAckDelayDLBurst": wmanIf2BsOfdmaHARQAckDelayDLBurst,
       "wmanIf2BsOfdmaUlAmcAlloPhyBandsBitmap": wmanIf2BsOfdmaUlAmcAlloPhyBandsBitmap,
       "wmanIf2BsOfdmaMaxRetransmission": wmanIf2BsOfdmaMaxRetransmission,
       "wmanIf2BsOfdmaNormalizedCnOverride": wmanIf2BsOfdmaNormalizedCnOverride,
       "wmanIf2BsOfdmaSizeOfCqichId": wmanIf2BsOfdmaSizeOfCqichId,
       "wmanIf2BsOfdmaNormalizedCnValue": wmanIf2BsOfdmaNormalizedCnValue,
       "wmanIf2BsOfdmaNormalizedCnOverride2": wmanIf2BsOfdmaNormalizedCnOverride2,
       "wmanIf2BsOfdmaBandAmcEntryAvgCinr": wmanIf2BsOfdmaBandAmcEntryAvgCinr,
       "wmanIf2BsOfdmaAasPreambleUpperBond": wmanIf2BsOfdmaAasPreambleUpperBond,
       "wmanIf2BsOfdmaAasPreambleLowerBond": wmanIf2BsOfdmaAasPreambleLowerBond,
       "wmanIf2BsOfdmaAasBeamSelectAllowed": wmanIf2BsOfdmaAasBeamSelectAllowed,
       "wmanIf2BsOfdmaCqichIndicationFlag": wmanIf2BsOfdmaCqichIndicationFlag,
       "wmanIf2BsOfdmaUpPowerAdjStep": wmanIf2BsOfdmaUpPowerAdjStep,
       "wmanIf2BsOfdmaDownPowerAdjStep": wmanIf2BsOfdmaDownPowerAdjStep,
       "wmanIf2BsOfdmaMinPowerOffsetAdj": wmanIf2BsOfdmaMinPowerOffsetAdj,
       "wmanIf2BsOfdmaMaxPowerOffsetAdj": wmanIf2BsOfdmaMaxPowerOffsetAdj,
       "wmanIf2BsOfdmaHandoverRngCodes": wmanIf2BsOfdmaHandoverRngCodes,
       "wmanIf2BsOfdmaInitialRngInterval": wmanIf2BsOfdmaInitialRngInterval,
       "wmanIf2BsOfdmaTxPwrRepThreshold": wmanIf2BsOfdmaTxPwrRepThreshold,
       "wmanIf2BsOfdmaTprPower": wmanIf2BsOfdmaTprPower,
       "wmanIf2BsOfdmaAlphaPavg": wmanIf2BsOfdmaAlphaPavg,
       "wmanIf2BsOfdmaCqichTxPwrRepThreshold": wmanIf2BsOfdmaCqichTxPwrRepThreshold,
       "wmanIf2BsOfdmaCqichTprPower": wmanIf2BsOfdmaCqichTprPower,
       "wmanIf2BsOfdmaCqichAlphaPavg": wmanIf2BsOfdmaCqichAlphaPavg,
       "wmanIf2BsOfdmaNormalizedCnChSounding": wmanIf2BsOfdmaNormalizedCnChSounding,
       "wmanIf2BsOfdmaInitialRngBackoffStart": wmanIf2BsOfdmaInitialRngBackoffStart,
       "wmanIf2BsOfdmaInitialRngBackoffEnd": wmanIf2BsOfdmaInitialRngBackoffEnd,
       "wmanIf2BsOfdmaBwRequestBackoffStart": wmanIf2BsOfdmaBwRequestBackoffStart,
       "wmanIf2BsOfdmaBwRequestBackoffEnd": wmanIf2BsOfdmaBwRequestBackoffEnd,
       "wmanIf2BsOfdmaDownlinkChannelTable": wmanIf2BsOfdmaDownlinkChannelTable,
       "wmanIf2BsOfdmaDownlinkChannelEntry": wmanIf2BsOfdmaDownlinkChannelEntry,
       "wmanIf2BsOfdmaFrameDurationCode": wmanIf2BsOfdmaFrameDurationCode,
       "wmanIf2BsOfdmaFftSize": wmanIf2BsOfdmaFftSize,
       "wmanIf2BsOfdmaHARQAckDelayULBurst": wmanIf2BsOfdmaHARQAckDelayULBurst,
       "wmanIf2BsOfdmaHarqZonePermutation": wmanIf2BsOfdmaHarqZonePermutation,
       "wmanIf2BsOfdmaHMaxRetransmission": wmanIf2BsOfdmaHMaxRetransmission,
       "wmanIf2BsOfdmaCinrAlphaAvg": wmanIf2BsOfdmaCinrAlphaAvg,
       "wmanIf2BsOfdmaRssiAlphaAvg": wmanIf2BsOfdmaRssiAlphaAvg,
       "wmanIf2BsOfdmaDlAmcAlloPhyBandsBitmap": wmanIf2BsOfdmaDlAmcAlloPhyBandsBitmap,
       "wmanIf2BsOfdmaHandoverSupported": wmanIf2BsOfdmaHandoverSupported,
       "wmanIf2BsOfdmaThresholdAddBsDivSet": wmanIf2BsOfdmaThresholdAddBsDivSet,
       "wmanIf2BsOfdmaThresholdDelBsDivSet": wmanIf2BsOfdmaThresholdDelBsDivSet,
       "wmanIf2BsOfdmaAsrSlotLength": wmanIf2BsOfdmaAsrSlotLength,
       "wmanIf2BsOfdmaAsrSwitchingPeriod": wmanIf2BsOfdmaAsrSwitchingPeriod,
       "wmanIf2BsOfdmaHysteresisMargin": wmanIf2BsOfdmaHysteresisMargin,
       "wmanIf2BsOfdmaTimeToTrigger": wmanIf2BsOfdmaTimeToTrigger,
       "wmanIf2BsOfdmaRestartCount": wmanIf2BsOfdmaRestartCount,
       "wmanIf2BsOfdmaUcdBurstProfileTable": wmanIf2BsOfdmaUcdBurstProfileTable,
       "wmanIf2BsOfdmaUcdBurstProfileEntry": wmanIf2BsOfdmaUcdBurstProfileEntry,
       "wmanIf2BsOfdmaUiucIndex": wmanIf2BsOfdmaUiucIndex,
       "wmanIf2BsOfdmaUcdFecCodeType": wmanIf2BsOfdmaUcdFecCodeType,
       "wmanIf2BsOfdmaRangingDataRatio": wmanIf2BsOfdmaRangingDataRatio,
       "wmanIf2BsOfdmaUcdBurstProfileRowStatus": wmanIf2BsOfdmaUcdBurstProfileRowStatus,
       "wmanIf2BsOfdmaDcdBurstProfileTable": wmanIf2BsOfdmaDcdBurstProfileTable,
       "wmanIf2BsOfdmaDcdBurstProfileEntry": wmanIf2BsOfdmaDcdBurstProfileEntry,
       "wmanIf2BsOfdmaDiucIndex": wmanIf2BsOfdmaDiucIndex,
       "wmanIf2BsOfdmaDcdFecCodeType": wmanIf2BsOfdmaDcdFecCodeType,
       "wmanIf2BsOfdmaDcdBurstProfileRowStatus": wmanIf2BsOfdmaDcdBurstProfileRowStatus,
       "wmanIf2BsAm": wmanIf2BsAm,
       "wmanIf2BsOtaUsageDataRecordTable": wmanIf2BsOtaUsageDataRecordTable,
       "wmanIf2BsOtaUsageDataRecordEntry": wmanIf2BsOtaUsageDataRecordEntry,
       "wmanIf2BsSessionId": wmanIf2BsSessionId,
       "wmanIf2BsCid": wmanIf2BsCid,
       "wmanIf2BsServiceFlowId": wmanIf2BsServiceFlowId,
       "wmanIf2BsMacSduCount": wmanIf2BsMacSduCount,
       "wmanIf2BsOctetCount": wmanIf2BsOctetCount,
       "wmanIf2BsSessionEstablishTime": wmanIf2BsSessionEstablishTime,
       "wmanIf2BsSessionTerminateTime": wmanIf2BsSessionTerminateTime,
       "wmanIf2BsGlobalServiceClass": wmanIf2BsGlobalServiceClass,
       "wmanIf2BsQoSProfileIndex": wmanIf2BsQoSProfileIndex,
       "wmanIf2BsPm": wmanIf2BsPm,
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
       "wmanIf2BsStatisticsConfigTable": wmanIf2BsStatisticsConfigTable,
       "wmanIf2BsStatisticsConfigEntry": wmanIf2BsStatisticsConfigEntry,
       "wmanIf2BsDataSampleInterval": wmanIf2BsDataSampleInterval,
       "wmanIf2BsCountersReportInterval": wmanIf2BsCountersReportInterval,
       "wmanIf2BsSsStartupStatisticsTable": wmanIf2BsSsStartupStatisticsTable,
       "wmanIf2BsSsStartupStatisticsEntry": wmanIf2BsSsStartupStatisticsEntry,
       "wmanIf2BsSsAuthenAttempt": wmanIf2BsSsAuthenAttempt,
       "wmanIf2BsSsAuthenSuccess": wmanIf2BsSsAuthenSuccess,
       "wmanIf2BsSsAuthenSuccessRate": wmanIf2BsSsAuthenSuccessRate,
       "wmanIf2BsSsRangingAttempt": wmanIf2BsSsRangingAttempt,
       "wmanIf2BsSsRangingSuccess": wmanIf2BsSsRangingSuccess,
       "wmanIf2BsSsRangingSuccessRate": wmanIf2BsSsRangingSuccessRate,
       "wmanIf2BsDataRateStatisticsTable": wmanIf2BsDataRateStatisticsTable,
       "wmanIf2BsDataRateStatisticsEntry": wmanIf2BsDataRateStatisticsEntry,
       "wmanIf2BsAvgDlUserThroughput": wmanIf2BsAvgDlUserThroughput,
       "wmanIf2BsAvgUlUserThroughput": wmanIf2BsAvgUlUserThroughput,
       "wmanIf2BsAvgDlMacThroughput": wmanIf2BsAvgDlMacThroughput,
       "wmanIf2BsAvgUlMacThroughput": wmanIf2BsAvgUlMacThroughput,
       "wmanIf2BsAvgDlPhyThroughput": wmanIf2BsAvgDlPhyThroughput,
       "wmanIf2BsAvgUlPhyThroughput": wmanIf2BsAvgUlPhyThroughput,
       "wmanIf2BsPeakDlUserThroughput": wmanIf2BsPeakDlUserThroughput,
       "wmanIf2BsPeakUlUserThroughput": wmanIf2BsPeakUlUserThroughput,
       "wmanIf2BsPeakDlMacThroughput": wmanIf2BsPeakDlMacThroughput,
       "wmanIf2BsPeakUlMacThroughput": wmanIf2BsPeakUlMacThroughput,
       "wmanIf2BsPeakDlPhyThroughput": wmanIf2BsPeakDlPhyThroughput,
       "wmanIf2BsPeakUlPhyThroughput": wmanIf2BsPeakUlPhyThroughput,
       "wmanIf2BsAvgDlCellEdgeThroughput": wmanIf2BsAvgDlCellEdgeThroughput,
       "wmanIf2BsAvgUlCellEdgeThroughput": wmanIf2BsAvgUlCellEdgeThroughput,
       "wmanIf2BsDataRateMeasurements": wmanIf2BsDataRateMeasurements,
       "wmanIf2BsNetworkEntryStatisticsTable": wmanIf2BsNetworkEntryStatisticsTable,
       "wmanIf2BsNetworkEntryStatisticsEntry": wmanIf2BsNetworkEntryStatisticsEntry,
       "wmanIf2BsAvgNetworkEntryTime": wmanIf2BsAvgNetworkEntryTime,
       "wmanIf2BsMaxNetworkEntryTime": wmanIf2BsMaxNetworkEntryTime,
       "wmanIf2BsAvgNetworkReEntryTime": wmanIf2BsAvgNetworkReEntryTime,
       "wmanIf2BsMaxNetworkReEntryTime": wmanIf2BsMaxNetworkReEntryTime,
       "wmanIf2BsNumOfNetworkEntries": wmanIf2BsNumOfNetworkEntries,
       "wmanIf2BsNumOfNetworkReEntries": wmanIf2BsNumOfNetworkReEntries,
       "wmanIf2BsPacketErrorRateTable": wmanIf2BsPacketErrorRateTable,
       "wmanIf2BsPacketErrorRateEntry": wmanIf2BsPacketErrorRateEntry,
       "wmanIf2BsDlPacketsSend": wmanIf2BsDlPacketsSend,
       "wmanIf2BsDlPacketsErrored": wmanIf2BsDlPacketsErrored,
       "wmanIf2BsDlPacketErrorRate": wmanIf2BsDlPacketErrorRate,
       "wmanIf2BsSsHandoverMetricsTable": wmanIf2BsSsHandoverMetricsTable,
       "wmanIf2BsSsHandoverMetricsEntry": wmanIf2BsSsHandoverMetricsEntry,
       "wmanIf2BsSsHandoverAttempt": wmanIf2BsSsHandoverAttempt,
       "wmanIf2BsSsHandoverSuccess": wmanIf2BsSsHandoverSuccess,
       "wmanIf2BsSsHandoverSuccessRate": wmanIf2BsSsHandoverSuccessRate,
       "wmanIf2BsSsHandoverCancel": wmanIf2BsSsHandoverCancel,
       "wmanIf2BsSsHandoverReject": wmanIf2BsSsHandoverReject,
       "wmanIf2BsSsHandoverCancelRate": wmanIf2BsSsHandoverCancelRate,
       "wmanIf2BsSsHandoverRejectRate": wmanIf2BsSsHandoverRejectRate,
       "wmanIf2BsSsAvgHandoverTime": wmanIf2BsSsAvgHandoverTime,
       "wmanIf2BsSsUnexpectedHandover": wmanIf2BsSsUnexpectedHandover,
       "wmanIf2BsSsUserMetricsTable": wmanIf2BsSsUserMetricsTable,
       "wmanIf2BsSsUserMetricsEntry": wmanIf2BsSsUserMetricsEntry,
       "wmanIf2BsSsActiveUsers": wmanIf2BsSsActiveUsers,
       "wmanIf2BsSsPeakNormalModeUsers": wmanIf2BsSsPeakNormalModeUsers,
       "wmanIf2BsSsPeakSleepModeUsers": wmanIf2BsSsPeakSleepModeUsers,
       "wmanIf2BsSsPeakIdleModeUsers": wmanIf2BsSsPeakIdleModeUsers,
       "wmanIf2BsSsAvgNormalModeUsers": wmanIf2BsSsAvgNormalModeUsers,
       "wmanIf2BsSsCidmetricsTable": wmanIf2BsSsCidmetricsTable,
       "wmanIf2BsSsCidmetricsEntry": wmanIf2BsSsCidmetricsEntry,
       "wmanIf2BsSsBasicAndPrimaryCids": wmanIf2BsSsBasicAndPrimaryCids,
       "wmanIf2BsSsMaximumUserCids": wmanIf2BsSsMaximumUserCids,
       "wmanIf2BsSsAvgUserCids": wmanIf2BsSsAvgUserCids,
       "wmanIf2BsSm": wmanIf2BsSm,
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
       "wmanIf2BsSsPkmV1AuthorizationTable": wmanIf2BsSsPkmV1AuthorizationTable,
       "wmanIf2BsSsPkmV1AuthorizationEntry": wmanIf2BsSsPkmV1AuthorizationEntry,
       "wmanIf2BsSsPkmV1AuthMacAddress": wmanIf2BsSsPkmV1AuthMacAddress,
       "wmanIf2BsSsPkmV1CaCertificate": wmanIf2BsSsPkmV1CaCertificate,
       "wmanIf2BsSsPkmV1SsCertificate": wmanIf2BsSsPkmV1SsCertificate,
       "wmanIf2BsSsPkmV1PrimarySaId": wmanIf2BsSsPkmV1PrimarySaId,
       "wmanIf2BsSsPkmV1AuthKeySequenceNumber": wmanIf2BsSsPkmV1AuthKeySequenceNumber,
       "wmanIf2BsSsPkmV1AuthKeyLifetime": wmanIf2BsSsPkmV1AuthKeyLifetime,
       "wmanIf2BsSsPkmV1AuthRejectError": wmanIf2BsSsPkmV1AuthRejectError,
       "wmanIf2BsSsPkmV1AuthInvalidError": wmanIf2BsSsPkmV1AuthInvalidError,
       "wmanIf2BsSsPkmV1AkN-1ExpireTime": wmanIf2BsSsPkmV1AkN_1ExpireTime,
       "wmanIf2BsSsPkmV1AkNExpireTime": wmanIf2BsSsPkmV1AkNExpireTime,
       "wmanIf2BsSsPkmV1CertificateStatus": wmanIf2BsSsPkmV1CertificateStatus,
       "wmanIf2BsSsPkmV1AuthReset": wmanIf2BsSsPkmV1AuthReset,
       "wmanIf2BsSsPkmV1TekTable": wmanIf2BsSsPkmV1TekTable,
       "wmanIf2BsSsPkmV1TekEntry": wmanIf2BsSsPkmV1TekEntry,
       "wmanIf2BsSsPkmV1SaidIndex": wmanIf2BsSsPkmV1SaidIndex,
       "wmanIf2BsSsPkmV1SaType": wmanIf2BsSsPkmV1SaType,
       "wmanIf2BsSsPkmV1TekDataEncryptAlgorithm": wmanIf2BsSsPkmV1TekDataEncryptAlgorithm,
       "wmanIf2BsSsPkmV1TekDataAuthentAlgorithm": wmanIf2BsSsPkmV1TekDataAuthentAlgorithm,
       "wmanIf2BsSsPkmV1TekEncryptAlgorithm": wmanIf2BsSsPkmV1TekEncryptAlgorithm,
       "wmanIf2BsSsPkmV1TekN-1SequenceNumber": wmanIf2BsSsPkmV1TekN_1SequenceNumber,
       "wmanIf2BsSsPkmV1TekN-1Lifetime": wmanIf2BsSsPkmV1TekN_1Lifetime,
       "wmanIf2BsSsPkmV1TekNSequenceNumber": wmanIf2BsSsPkmV1TekNSequenceNumber,
       "wmanIf2BsSsPkmV1TekNLifetime": wmanIf2BsSsPkmV1TekNLifetime,
       "wmanIf2BsSsPkmV1KeyRejectError": wmanIf2BsSsPkmV1KeyRejectError,
       "wmanIf2BsSsPkmV1TekInvalidError": wmanIf2BsSsPkmV1TekInvalidError,
       "wmanIf2BsSsPkmV1TekN-1ExpireTime": wmanIf2BsSsPkmV1TekN_1ExpireTime,
       "wmanIf2BsSsPkmV1TekNExpireTime": wmanIf2BsSsPkmV1TekNExpireTime,
       "wmanIf2BsSsPkmV1TekReset": wmanIf2BsSsPkmV1TekReset,
       "wmanIf2BsPkmV2Objects": wmanIf2BsPkmV2Objects,
       "wmanIf2BsPkmV2ConfigTable": wmanIf2BsPkmV2ConfigTable,
       "wmanIf2BsPkmV2ConfigEntry": wmanIf2BsPkmV2ConfigEntry,
       "wmanIf2BsPkmPmkPrehandshakeLifetime": wmanIf2BsPkmPmkPrehandshakeLifetime,
       "wmanIf2BsPkmPmkLifetime": wmanIf2BsPkmPmkLifetime,
       "wmanIf2BsSaChallengeTimeout": wmanIf2BsSaChallengeTimeout,
       "wmanIf2BsMaxSaTekChallenge": wmanIf2BsMaxSaTekChallenge,
       "wmanIf2BsSaTekTimeout": wmanIf2BsSaTekTimeout,
       "wmanIf2BsMaxSaTekRequest": wmanIf2BsMaxSaTekRequest,
       "wmanIf2BsSsPkmV2RsaAuthTable": wmanIf2BsSsPkmV2RsaAuthTable,
       "wmanIf2BsSsPkmV2RsaAuthEntry": wmanIf2BsSsPkmV2RsaAuthEntry,
       "wmanIf2BsSsPkmV2BsCertificate": wmanIf2BsSsPkmV2BsCertificate,
       "wmanIf2BsSsPkmV2SsCertificate": wmanIf2BsSsPkmV2SsCertificate,
       "wmanIf2BsSsPkmV2SaId": wmanIf2BsSsPkmV2SaId,
       "wmanIf2BsSsPkmV2SsRandom": wmanIf2BsSsPkmV2SsRandom,
       "wmanIf2BsSsPkmV2BsRandom": wmanIf2BsSsPkmV2BsRandom,
       "wmanIf2BsSsPkmV2AuthKeySequenceNumber": wmanIf2BsSsPkmV2AuthKeySequenceNumber,
       "wmanIf2BsSsPkmV2AuthKeyLifetime": wmanIf2BsSsPkmV2AuthKeyLifetime,
       "wmanIf2BsSsPkmV2AuthResult": wmanIf2BsSsPkmV2AuthResult,
       "wmanIf2BsSsPkmV2AuthFailure": wmanIf2BsSsPkmV2AuthFailure,
       "wmanIf2BsSsPkmV2AkN-1ExpireTime": wmanIf2BsSsPkmV2AkN_1ExpireTime,
       "wmanIf2BsSsPkmV2AkNExpireTime": wmanIf2BsSsPkmV2AkNExpireTime,
       "wmanIf2BsSsPkmV2CertificateStatus": wmanIf2BsSsPkmV2CertificateStatus,
       "wmanIf2BsSsPkmV2TekTable": wmanIf2BsSsPkmV2TekTable,
       "wmanIf2BsSsPkmV2TekEntry": wmanIf2BsSsPkmV2TekEntry,
       "wmanIf2BsSsPkmV2SaidIndex": wmanIf2BsSsPkmV2SaidIndex,
       "wmanIf2BsSsPkmV2SaType": wmanIf2BsSsPkmV2SaType,
       "wmanIf2BsSsPkmV2SaServiceType": wmanIf2BsSsPkmV2SaServiceType,
       "wmanIf2BsSsPkmV2TekDataEncryptAlgorithm": wmanIf2BsSsPkmV2TekDataEncryptAlgorithm,
       "wmanIf2BsSsPkmV2TekDataAuthentAlgorithm": wmanIf2BsSsPkmV2TekDataAuthentAlgorithm,
       "wmanIf2BsSsPkmV2TekEncryptAlgorithm": wmanIf2BsSsPkmV2TekEncryptAlgorithm,
       "wmanIf2BsSsPkmV2TekN-1SequenceNumber": wmanIf2BsSsPkmV2TekN_1SequenceNumber,
       "wmanIf2BsSsPkmV2TekN-1Lifetime": wmanIf2BsSsPkmV2TekN_1Lifetime,
       "wmanIf2BsSsPkmV2TekNSequenceNumber": wmanIf2BsSsPkmV2TekNSequenceNumber,
       "wmanIf2BsSsPkmV2TekNLifetime": wmanIf2BsSsPkmV2TekNLifetime,
       "wmanIf2BsSsPkmV2TekInvalidError": wmanIf2BsSsPkmV2TekInvalidError,
       "wmanIf2BsSsPkmV2TekN-1ExpireTime": wmanIf2BsSsPkmV2TekN_1ExpireTime,
       "wmanIf2BsSsPkmV2TekNExpireTime": wmanIf2BsSsPkmV2TekNExpireTime,
       "wmanIf2BsSsPkmV23wayHandshakeTable": wmanIf2BsSsPkmV23wayHandshakeTable,
       "wmanIf2BsSsPkmV23wayHandshakeEntry": wmanIf2BsSsPkmV23wayHandshakeEntry,
       "wmanIf2BsSsPkmV2SaTekBsRandom": wmanIf2BsSsPkmV2SaTekBsRandom,
       "wmanIf2BsSsPkmV2SaTekAkSequenceNumber": wmanIf2BsSsPkmV2SaTekAkSequenceNumber,
       "wmanIf2BsSsPkmV2SaTekAkId": wmanIf2BsSsPkmV2SaTekAkId,
       "wmanIf2BsSsPkmV2KeyLifetime": wmanIf2BsSsPkmV2KeyLifetime,
       "wmanIf2BsSsPkmV2SaTekMsRandom": wmanIf2BsSsPkmV2SaTekMsRandom,
       "wmanIf2MibConformance": wmanIf2MibConformance,
       "wmanIf2BsMibGroups": wmanIf2BsMibGroups,
       "wmanIf2MibBsGroup": wmanIf2MibBsGroup,
       "wmanIf2MibBsAasGroup": wmanIf2MibBsAasGroup,
       "wmanIf2MibBsOfdmGroup": wmanIf2MibBsOfdmGroup,
       "wmanIf2MibBsOfdmaGroup": wmanIf2MibBsOfdmaGroup,
       "wmanIf2MibBsNotificationGroup": wmanIf2MibBsNotificationGroup,
       "wmanIf2BsMibCompliances": wmanIf2BsMibCompliances,
       "wmanIf2BsMibCompliance": wmanIf2BsMibCompliance}
)
