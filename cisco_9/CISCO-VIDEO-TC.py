# SNMP MIB module (CISCO-VIDEO-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-VIDEO-TC.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:02:39 2025
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

ciscoVideoTc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 763)
)
if mibBuilder.loadTexts:
    ciscoVideoTc.setRevisions(
        ("2010-11-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CvcVideoResolution(TextualConvention, Integer32):
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("sqcif", 1),
          ("qcif", 2),
          ("qvga", 3),
          ("sif525", 4),
          ("cif", 5),
          ("hhr525", 6),
          ("hhr625", 7),
          ("vga", 8),
          ("n4sif525", 9),
          ("sd525", 10),
          ("n4cif", 11),
          ("sd625", 12),
          ("svga", 13),
          ("xga", 14),
          ("hd720p", 15),
          ("n4vga", 16),
          ("sxga", 17),
          ("n16sif525", 18),
          ("n16cif", 19),
          ("n4svga", 20),
          ("hd1080p", 21),
          ("n2Kx1K", 22),
          ("n2Kx1080", 23),
          ("n4xga", 24),
          ("n16vga", 25),
          ("n3616x1536", 26),
          ("n3672x1536", 27),
          ("n4Kx2K", 28),
          ("n4096x2304", 29))
    )



class CvcVideoLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9,
              10,
              11,
              12,
              13,
              20,
              21,
              22,
              30,
              31,
              32,
              40,
              41,
              42,
              50,
              51)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("level1b", 9),
          ("level1", 10),
          ("level1dot1", 11),
          ("level1dot2", 12),
          ("level1dot3", 13),
          ("level2", 20),
          ("level2dot1", 21),
          ("level2dot2", 22),
          ("level3", 30),
          ("level3dot1", 31),
          ("level3dot2", 32),
          ("level4", 40),
          ("level4dot1", 41),
          ("level4dot2", 42),
          ("level5", 50),
          ("level5dot1", 51))
    )



class CvcVideoProfile(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("h263Profile0", 10),
          ("h263Profile1", 11),
          ("h263Profile2", 12),
          ("h263Profile3", 13),
          ("h263Profile4", 14),
          ("h263Profile5", 15),
          ("h263Profile6", 16),
          ("h263Profile7", 17),
          ("h263Profile8", 18),
          ("h264ProfileBaseline", 100),
          ("h264ProfileMain", 101),
          ("h264ProfileExtended", 102),
          ("h264ProfileHigh", 103),
          ("h264ProfileHigh10", 104),
          ("h264ProfileHigh422", 105),
          ("h264ProfileHigh444Predictive", 106),
          ("h264ProfileHigh10Intra", 107),
          ("h264ProfileHigh422Intra", 108),
          ("h264ProfileHigh444Intra", 109),
          ("h264ProfileCavlc444Intra", 110))
    )



class CvcVideoCodecAnnexMap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("annexNone", 0),
          ("annexD1", 1),
          ("annexD2", 2),
          ("annexE", 3),
          ("annexF", 4),
          ("annexG", 5),
          ("annexH", 6),
          ("annexI", 7),
          ("annexJ", 8),
          ("annexK", 9),
          ("annexL", 10),
          ("annexM", 11),
          ("annexN", 12),
          ("annexO", 13),
          ("annexP", 14),
          ("annexQ", 15),
          ("annexR", 16),
          ("annexS", 17),
          ("annexT", 18),
          ("annexU", 19),
          ("annexV", 20),
          ("annexW", 21))
    )


class CvcVideoRtpPayloadFormat(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("rfc2190", 1),
          ("rfc2429", 2),
          ("rfc4629", 3),
          ("rfc3984", 4))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VIDEO-TC",
    **{"CvcVideoResolution": CvcVideoResolution,
       "CvcVideoLevel": CvcVideoLevel,
       "CvcVideoProfile": CvcVideoProfile,
       "CvcVideoCodecAnnexMap": CvcVideoCodecAnnexMap,
       "CvcVideoRtpPayloadFormat": CvcVideoRtpPayloadFormat,
       "ciscoVideoTc": ciscoVideoTc}
)
