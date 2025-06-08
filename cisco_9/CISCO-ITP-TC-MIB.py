# SNMP MIB module (CISCO-ITP-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-ITP-TC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:47:33 2025
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

ciscoItpTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 231)
)
if mibBuilder.loadTexts:
    ciscoItpTextualConventions.setRevisions(
        ("2004-04-26 00:00",
         "2003-08-03 00:00",
         "2003-01-29 00:00",
         "2001-12-11 00:00",
         "2001-10-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CItpTcAclId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2700, 2999),
    )



class CItpTcCLLI(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )



class CItpTcDisplayPC(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )



class CItpTcEncodingSchemeValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class CItpTcGlobalTitleSelector(TextualConvention, Integer32):
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
        *(("nai", 1),
          ("tt", 2),
          ("ttNpEs", 3),
          ("ttNpNaiEs", 4))
    )



class CItpTcGlobalTitleSelectorName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )



class CItpTcGtaAddr(TextualConvention, OctetString):
    status = "deprecated"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8



class CItpTcGtaLongAddr(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class CItpTcGtaDisplay(TextualConvention, OctetString):
    status = "deprecated"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )



class CItpTcGtaDisplayZB(TextualConvention, OctetString):
    status = "deprecated"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )



class CItpTcGtaLongDisplay(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class CItpTcGtaDisplayLen(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )



class CItpTcGtaLongDisplayLen(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )



class CItpTcNetworkName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )



class CItpTcInstanceNumber(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CItpTcLinksetId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )



class CItpTcLinkSLC(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class CItpTcLinkType(TextualConvention, Integer32):
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
        *(("other", 1),
          ("serial", 2),
          ("sctpIp", 3),
          ("hsl", 4),
          ("virtual", 5))
    )



class CItpTcNAI(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CItpTcNetworkIndicator(TextualConvention, Integer32):
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
        *(("international", 0),
          ("internationatSpare", 1),
          ("national", 2),
          ("nationalSpare", 3))
    )



class CItpTcNumberingPlan(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CItpTcPointCode(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777216),
    )



class CItpTcPointCodeMask(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777216),
    )



class CItpTcPointCodeType(TextualConvention, Integer32):
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
        *(("primary", 1),
          ("additional", 2),
          ("capability", 3),
          ("xua", 4))
    )



class CItpTcQos(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )



class CItpTcRouteTableName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )



class CItpTcServiceIndicator(TextualConvention, Integer32):
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("snmm", 0),
          ("sntm", 1),
          ("spare2", 2),
          ("sccp", 3),
          ("tup", 4),
          ("isup", 5),
          ("dupc", 6),
          ("dupf", 7),
          ("mtup", 8),
          ("bisup", 9),
          ("sisup", 10),
          ("spare11", 11),
          ("spare12", 12),
          ("spare13", 13),
          ("spare14", 14),
          ("spare15", 15))
    )



class CItpTcSls(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CItpTcSs7Variant(TextualConvention, Integer32):
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
        *(("ansi", 1),
          ("itu", 2),
          ("china", 3))
    )



class CItpTcSubSystemNumber(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 255),
    )



class CItpTcSubSystemNumberMask(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )



class CItpTcTableLoadStatus(TextualConvention, Integer32):
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
        *(("loadNotRequested", 1),
          ("loadInProgress", 2),
          ("loadComplete", 3),
          ("loadCompleteWithErrors", 4),
          ("loadFailed", 5))
    )



class CItpTcTimerMtp2T01(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 150000),
    )



class CItpTcTimerMtp2T02(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 150000),
    )



class CItpTcTimerMtp2T03(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 14000),
    )



class CItpTcTimerMtp2T04E(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(400, 660),
    )



class CItpTcTimerMtp2T04N(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2007, 9500),
    )



class CItpTcTimerMtp2T05(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(80, 120),
    )



class CItpTcTimerMtp2T06(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 6000),
    )



class CItpTcTimerMtp2T07(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 6000),
    )



class CItpTcTimerMtp3T01(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1200),
    )



class CItpTcTimerMtp3T02(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(700, 2000),
    )



class CItpTcTimerMtp3T03(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1200),
    )



class CItpTcTimerMtp3T04(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1200),
    )



class CItpTcTimerMtp3T05(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1200),
    )



class CItpTcTimerMtp3T06(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1200),
    )



class CItpTcTimerMtp3T07(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 2000),
    )



class CItpTcTimerMtp3T08(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(800, 1200),
    )



class CItpTcTimerMtp3T10(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30000, 60000),
    )



class CItpTcTimerMtp3T11(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30000, 90000),
    )



class CItpTcTimerMtp3T12(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(800, 1500),
    )



class CItpTcTimerMtp3T13(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(800, 1500),
    )



class CItpTcTimerMtp3T14(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 3000),
    )



class CItpTcTimerMtp3T15(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 3000),
    )



class CItpTcTimerMtp3T16(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1400, 2000),
    )



class CItpTcTimerMtp3T17(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(800, 1500),
    )



class CItpTcTimerMtp3T18(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 31000),
    )



class CItpTcTimerMtp3T19(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(67000, 600000),
    )



class CItpTcTimerMtp3T20(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 120000),
    )



class CItpTcTimerMtp3T21(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(63000, 120000),
    )



class CItpTcTimerMtp3T22(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(36000, 360000),
    )



class CItpTcTimerMtp3T23(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9000, 360000),
    )



class CItpTcTimerMtp3T24(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 60000),
    )



class CItpTcTimerMtp3T25(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30000, 35000),
    )



class CItpTcTimerMtp3T26(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(12000, 15000),
    )



class CItpTcTimerMtp3T27(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 50000),
    )



class CItpTcTimerMtp3T28(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3000, 35000),
    )



class CItpTcTimerMtp3T29(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60000, 65000),
    )



class CItpTcTimerMtp3T30(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30000, 35000),
    )



class CItpTcTimerMtp3T31(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10000, 120000),
    )



class CItpTcTimerMtp3T32(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 120000),
    )



class CItpTcTimerMtp3T33(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60000, 600000),
    )



class CItpTcTimerMtp3T34(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 120000),
    )



class CItpTcTimerLinkTest(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 12000),
    )



class CItpTcTimerLinkMessage(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30000, 90000),
    )



class CItpTcTimerLinkActRetry(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60000, 90000),
    )



class CItpTcTranslationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tt", 1),
          ("ssn", 2))
    )



class CItpTcURL(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class CItpTcXuaName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-TC-MIB",
    **{"CItpTcAclId": CItpTcAclId,
       "CItpTcCLLI": CItpTcCLLI,
       "CItpTcDisplayPC": CItpTcDisplayPC,
       "CItpTcEncodingSchemeValue": CItpTcEncodingSchemeValue,
       "CItpTcGlobalTitleSelector": CItpTcGlobalTitleSelector,
       "CItpTcGlobalTitleSelectorName": CItpTcGlobalTitleSelectorName,
       "CItpTcGtaAddr": CItpTcGtaAddr,
       "CItpTcGtaLongAddr": CItpTcGtaLongAddr,
       "CItpTcGtaDisplay": CItpTcGtaDisplay,
       "CItpTcGtaDisplayZB": CItpTcGtaDisplayZB,
       "CItpTcGtaLongDisplay": CItpTcGtaLongDisplay,
       "CItpTcGtaDisplayLen": CItpTcGtaDisplayLen,
       "CItpTcGtaLongDisplayLen": CItpTcGtaLongDisplayLen,
       "CItpTcNetworkName": CItpTcNetworkName,
       "CItpTcInstanceNumber": CItpTcInstanceNumber,
       "CItpTcLinksetId": CItpTcLinksetId,
       "CItpTcLinkSLC": CItpTcLinkSLC,
       "CItpTcLinkType": CItpTcLinkType,
       "CItpTcNAI": CItpTcNAI,
       "CItpTcNetworkIndicator": CItpTcNetworkIndicator,
       "CItpTcNumberingPlan": CItpTcNumberingPlan,
       "CItpTcPointCode": CItpTcPointCode,
       "CItpTcPointCodeMask": CItpTcPointCodeMask,
       "CItpTcPointCodeType": CItpTcPointCodeType,
       "CItpTcQos": CItpTcQos,
       "CItpTcRouteTableName": CItpTcRouteTableName,
       "CItpTcServiceIndicator": CItpTcServiceIndicator,
       "CItpTcSls": CItpTcSls,
       "CItpTcSs7Variant": CItpTcSs7Variant,
       "CItpTcSubSystemNumber": CItpTcSubSystemNumber,
       "CItpTcSubSystemNumberMask": CItpTcSubSystemNumberMask,
       "CItpTcTableLoadStatus": CItpTcTableLoadStatus,
       "CItpTcTimerMtp2T01": CItpTcTimerMtp2T01,
       "CItpTcTimerMtp2T02": CItpTcTimerMtp2T02,
       "CItpTcTimerMtp2T03": CItpTcTimerMtp2T03,
       "CItpTcTimerMtp2T04E": CItpTcTimerMtp2T04E,
       "CItpTcTimerMtp2T04N": CItpTcTimerMtp2T04N,
       "CItpTcTimerMtp2T05": CItpTcTimerMtp2T05,
       "CItpTcTimerMtp2T06": CItpTcTimerMtp2T06,
       "CItpTcTimerMtp2T07": CItpTcTimerMtp2T07,
       "CItpTcTimerMtp3T01": CItpTcTimerMtp3T01,
       "CItpTcTimerMtp3T02": CItpTcTimerMtp3T02,
       "CItpTcTimerMtp3T03": CItpTcTimerMtp3T03,
       "CItpTcTimerMtp3T04": CItpTcTimerMtp3T04,
       "CItpTcTimerMtp3T05": CItpTcTimerMtp3T05,
       "CItpTcTimerMtp3T06": CItpTcTimerMtp3T06,
       "CItpTcTimerMtp3T07": CItpTcTimerMtp3T07,
       "CItpTcTimerMtp3T08": CItpTcTimerMtp3T08,
       "CItpTcTimerMtp3T10": CItpTcTimerMtp3T10,
       "CItpTcTimerMtp3T11": CItpTcTimerMtp3T11,
       "CItpTcTimerMtp3T12": CItpTcTimerMtp3T12,
       "CItpTcTimerMtp3T13": CItpTcTimerMtp3T13,
       "CItpTcTimerMtp3T14": CItpTcTimerMtp3T14,
       "CItpTcTimerMtp3T15": CItpTcTimerMtp3T15,
       "CItpTcTimerMtp3T16": CItpTcTimerMtp3T16,
       "CItpTcTimerMtp3T17": CItpTcTimerMtp3T17,
       "CItpTcTimerMtp3T18": CItpTcTimerMtp3T18,
       "CItpTcTimerMtp3T19": CItpTcTimerMtp3T19,
       "CItpTcTimerMtp3T20": CItpTcTimerMtp3T20,
       "CItpTcTimerMtp3T21": CItpTcTimerMtp3T21,
       "CItpTcTimerMtp3T22": CItpTcTimerMtp3T22,
       "CItpTcTimerMtp3T23": CItpTcTimerMtp3T23,
       "CItpTcTimerMtp3T24": CItpTcTimerMtp3T24,
       "CItpTcTimerMtp3T25": CItpTcTimerMtp3T25,
       "CItpTcTimerMtp3T26": CItpTcTimerMtp3T26,
       "CItpTcTimerMtp3T27": CItpTcTimerMtp3T27,
       "CItpTcTimerMtp3T28": CItpTcTimerMtp3T28,
       "CItpTcTimerMtp3T29": CItpTcTimerMtp3T29,
       "CItpTcTimerMtp3T30": CItpTcTimerMtp3T30,
       "CItpTcTimerMtp3T31": CItpTcTimerMtp3T31,
       "CItpTcTimerMtp3T32": CItpTcTimerMtp3T32,
       "CItpTcTimerMtp3T33": CItpTcTimerMtp3T33,
       "CItpTcTimerMtp3T34": CItpTcTimerMtp3T34,
       "CItpTcTimerLinkTest": CItpTcTimerLinkTest,
       "CItpTcTimerLinkMessage": CItpTcTimerLinkMessage,
       "CItpTcTimerLinkActRetry": CItpTcTimerLinkActRetry,
       "CItpTcTranslationType": CItpTcTranslationType,
       "CItpTcURL": CItpTcURL,
       "CItpTcXuaName": CItpTcXuaName,
       "ciscoItpTextualConventions": ciscoItpTextualConventions}
)
