# SNMP MIB module (CISCO-ST-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-ST-TC.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:52:59 2025
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

(ciscoModules,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoModules")

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

storageTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 4)
)
if mibBuilder.loadTexts:
    storageTextualConventions.setRevisions(
        ("2024-08-20 00:00",
         "2021-02-12 00:00",
         "2016-11-30 00:00",
         "2012-08-08 00:00",
         "2011-07-26 00:00",
         "2010-12-24 00:00",
         "2008-05-16 00:00",
         "2005-12-17 00:00",
         "2004-05-18 00:00",
         "2003-09-26 00:00",
         "2003-08-07 00:00",
         "2002-10-04 00:00",
         "2002-09-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VsanIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class DomainId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 239),
    )



class DomainIdOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 239),
    )



class FcAddressId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3



class FcNameId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8



class FcNameIdOrZero(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )



class FcClassOfServices(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("classF", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3),
          ("class4", 4),
          ("class5", 5),
          ("class6", 6))
    )


class FcPortTypes(TextualConvention, Integer32):
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
        *(("auto", 1),
          ("fPort", 2),
          ("flPort", 3),
          ("ePort", 4),
          ("bPort", 5),
          ("fxPort", 6),
          ("sdPort", 7),
          ("tlPort", 8),
          ("nPort", 9),
          ("nlPort", 10),
          ("nxPort", 11),
          ("tePort", 12),
          ("fvPort", 13),
          ("portOperDown", 14),
          ("stPort", 15),
          ("npPort", 16),
          ("tfPort", 17),
          ("tnpPort", 18))
    )



class FcPortTxTypes(TextualConvention, Integer32):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("longWaveLaser", 2),
          ("shortWaveLaser", 3),
          ("longWaveLaserCostReduced", 4),
          ("electrical", 5),
          ("tenGigBaseSr", 6),
          ("tenGigBaseLr", 7),
          ("tenGigBaseEr", 8),
          ("tenGigBaseLx4", 9),
          ("tenGigBaseSw", 10),
          ("tenGigBaseLw", 11),
          ("tenGigBaseEw", 12))
    )



class FcPortModuleTypes(TextualConvention, Integer32):
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
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("gbic", 3),
          ("embedded", 4),
          ("glm", 5),
          ("gbicWithSerialID", 6),
          ("gbicWithoutSerialID", 7),
          ("sfpWithSerialID", 8),
          ("sfpWithoutSerialID", 9),
          ("xfp", 10),
          ("x2Short", 11),
          ("x2Medium", 12),
          ("x2Tall", 13),
          ("xpakShort", 14),
          ("xpakMedium", 15),
          ("xpakTall", 16),
          ("xenpak", 17),
          ("sfpDwdm", 18),
          ("qsfp", 19),
          ("x2Dwdm", 20))
    )



class FcIfSpeed(TextualConvention, Integer32):
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("oneG", 2),
          ("twoG", 3),
          ("fourG", 4),
          ("autoMaxTwoG", 5),
          ("eightG", 6),
          ("autoMaxFourG", 7),
          ("tenG", 8),
          ("autoMaxEightG", 9),
          ("sixteenG", 10),
          ("autoMaxSixteenG", 11),
          ("thirtyTwoG", 12),
          ("autoMaxThirtyTwoG", 13),
          ("fiftyG", 14),
          ("sixtyFourG", 15),
          ("autoMaxSixtyFourG", 16))
    )



class PortMemberList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class FcAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
        ValueSizeConstraint(8, 8),
    )



class FcAddressType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wwn", 1),
          ("fcid", 2))
    )



class InterfaceOperMode(TextualConvention, Integer32):
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
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fPort", 2),
          ("flPort", 3),
          ("ePort", 4),
          ("bPort", 5),
          ("fxPort", 6),
          ("sdPort", 7),
          ("tlPort", 8),
          ("nPort", 9),
          ("nlPort", 10),
          ("nxPort", 11),
          ("tePort", 12),
          ("fvPort", 13),
          ("portOperDown", 14),
          ("stPort", 15),
          ("mgmtPort", 16),
          ("ipsPort", 17),
          ("evPort", 18),
          ("npPort", 19),
          ("tfPort", 20),
          ("tnpPort", 21))
    )



class FcIfServiceStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )



class FcIfSfpDiagLevelType(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("normal", 2),
          ("lowWarning", 3),
          ("lowAlarm", 4),
          ("highWarning", 5),
          ("highAlarm", 6))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ST-TC",
    **{"VsanIndex": VsanIndex,
       "DomainId": DomainId,
       "DomainIdOrZero": DomainIdOrZero,
       "FcAddressId": FcAddressId,
       "FcNameId": FcNameId,
       "FcNameIdOrZero": FcNameIdOrZero,
       "FcClassOfServices": FcClassOfServices,
       "FcPortTypes": FcPortTypes,
       "FcPortTxTypes": FcPortTxTypes,
       "FcPortModuleTypes": FcPortModuleTypes,
       "FcIfSpeed": FcIfSpeed,
       "PortMemberList": PortMemberList,
       "FcAddress": FcAddress,
       "FcAddressType": FcAddressType,
       "InterfaceOperMode": InterfaceOperMode,
       "FcIfServiceStateType": FcIfServiceStateType,
       "FcIfSfpDiagLevelType": FcIfSfpDiagLevelType,
       "storageTextualConventions": storageTextualConventions}
)
