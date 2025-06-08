# SNMP MIB module (IANA-FINISHER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/IANA-FINISHER-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:35:45 2025
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ianafinisherMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 110)
)
if mibBuilder.loadTexts:
    ianafinisherMIB.setRevisions(
        ("2004-06-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FinDeviceTypeTC(TextualConvention, Integer32):
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("stitcher", 3),
          ("folder", 4),
          ("binder", 5),
          ("trimmer", 6),
          ("dieCutter", 7),
          ("puncher", 8),
          ("perforater", 9),
          ("slitter", 10),
          ("separationCutter", 11),
          ("imprinter", 12),
          ("wrapper", 13),
          ("bander", 14),
          ("makeEnvelope", 15),
          ("stacker", 16),
          ("sheetRotator", 17),
          ("inserter", 18))
    )



class FinAttributeTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              30,
              31,
              40,
              50,
              80,
              81,
              82,
              83,
              100,
              130,
              160,
              161,
              162)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("deviceName", 3),
          ("deviceVendorName", 4),
          ("deviceModel", 5),
          ("deviceVersion", 6),
          ("deviceSerialNumber", 7),
          ("maximumSheets", 8),
          ("finProcessOffsetUnits", 9),
          ("finReferenceEdge", 10),
          ("finAxisOffset", 11),
          ("finJogEdge", 12),
          ("finHeadLocation", 13),
          ("finOperationRestrictions", 14),
          ("finNumberOfPositions", 15),
          ("namedConfiguration", 16),
          ("finMediaTypeRestriction", 17),
          ("finPrinterInputTraySupported", 18),
          ("finPreviousFinishingOperation", 19),
          ("finNextFinishingOperation", 20),
          ("stitchingType", 30),
          ("stitchingDirection", 31),
          ("foldingType", 40),
          ("bindingType", 50),
          ("punchHoleType", 80),
          ("punchHoleSizeLongDim", 81),
          ("punchHoleSizeShortDim", 82),
          ("punchPattern", 83),
          ("slittingType", 100),
          ("wrappingType", 130),
          ("stackOutputType", 160),
          ("stackOffset", 161),
          ("stackRotation", 162))
    )



class FinEdgeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("topEdge", 3),
          ("bottomEdge", 4),
          ("leftEdge", 5),
          ("rightEdge", 6))
    )



class FinStitchingTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("stapleTopLeft", 4),
          ("stapleBottomLeft", 5),
          ("stapleTopRight", 6),
          ("stapleBottomRight", 7),
          ("saddleStitch", 8),
          ("edgeStitch", 9),
          ("stapleDual", 10))
    )



class FinStitchingDirTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 2),
          ("topDown", 3),
          ("bottomUp", 4))
    )



class FinStitchingAngleTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 2),
          ("horizontal", 3),
          ("vertical", 4),
          ("slanted", 5))
    )



class FinFoldingTypeTC(TextualConvention, Integer32):
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
          ("unknown", 2),
          ("zFold", 3),
          ("halfFold", 4),
          ("letterFold", 5))
    )



class FinBindingTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
        *(("other", 1),
          ("unknown", 2),
          ("tape", 4),
          ("plastic", 5),
          ("velo", 6),
          ("perfect", 7),
          ("spiral", 8),
          ("adhesive", 9),
          ("comb", 10),
          ("padding", 11))
    )



class FinPunchHoleTypeTC(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("round", 3),
          ("oblong", 4),
          ("square", 5),
          ("rectangular", 6),
          ("star", 7))
    )



class FinPunchPatternTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("twoHoleUSTop", 4),
          ("threeHoleUS", 5),
          ("twoHoleDIN", 6),
          ("fourHoleDIN", 7),
          ("twentyTwoHoleUS", 8),
          ("nineteenHoleUS", 9),
          ("twoHoleMetric", 10),
          ("swedish4Hole", 11),
          ("twoHoleUSSide", 12),
          ("fiveHoleUS", 13),
          ("sevenHoleUS", 14),
          ("mixed7H4S", 15),
          ("norweg6Hole", 16),
          ("metric26Hole", 17),
          ("metric30Hole", 18))
    )



class FinSlittingTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("slitAndSeparate", 4),
          ("slitAndMerge", 5))
    )



class FinWrappingTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("shrinkWrap", 4),
          ("paperWrap", 5))
    )



class FinStackOutputTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("straight", 4),
          ("offset", 5),
          ("crissCross", 6))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANA-FINISHER-MIB",
    **{"FinDeviceTypeTC": FinDeviceTypeTC,
       "FinAttributeTypeTC": FinAttributeTypeTC,
       "FinEdgeTC": FinEdgeTC,
       "FinStitchingTypeTC": FinStitchingTypeTC,
       "FinStitchingDirTypeTC": FinStitchingDirTypeTC,
       "FinStitchingAngleTypeTC": FinStitchingAngleTypeTC,
       "FinFoldingTypeTC": FinFoldingTypeTC,
       "FinBindingTypeTC": FinBindingTypeTC,
       "FinPunchHoleTypeTC": FinPunchHoleTypeTC,
       "FinPunchPatternTC": FinPunchPatternTC,
       "FinSlittingTypeTC": FinSlittingTypeTC,
       "FinWrappingTypeTC": FinWrappingTypeTC,
       "FinStackOutputTypeTC": FinStackOutputTypeTC,
       "ianafinisherMIB": ianafinisherMIB}
)
