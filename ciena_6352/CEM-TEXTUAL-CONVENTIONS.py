# SNMP MIB module (CEM-TEXTUAL-CONVENTIONS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-TEXTUAL-CONVENTIONS.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:21 2025
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

(cnTextualConventions,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "cnTextualConventions")

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

cnTextualConventionsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 13, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CnSlotGroupNameType(TextualConvention, Integer32):
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("cnSlotGroupZero", 0),
          ("cnSlotGroupOne", 1),
          ("cnSlotGroupTwo", 2),
          ("cnSlotGroupThree", 3),
          ("cnSlotGroupFour", 4),
          ("cnSlotGroupFive", 5),
          ("cnSlotGroupSix", 6),
          ("cnSlotGroupSeven", 7),
          ("cnSlotGroupEight", 8),
          ("cnSlotGroupNine", 9),
          ("cnSlotGroupTen", 10),
          ("cnSlotGroupEleven", 11),
          ("cnSlotGroupTwelve", 12),
          ("cnSlotGroupThirteen", 13),
          ("cnSlotGroupFourteen", 14),
          ("cnSlotGroupFifteen", 15),
          ("cnSlotGroupSixteen", 16),
          ("cnSlotGroupOneTwo", 17),
          ("cnSlotGroupThreeFour", 18),
          ("cnSlotGroupFiveSix", 19),
          ("cnSlotGroupSevenEight", 20),
          ("cnSlotGroupNineTen", 21),
          ("cnSlotGroupElevenTwelve", 22),
          ("cnSlotGroupThirteenFourteen", 23),
          ("cnSlotGroupFifteenSixteen", 24))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-TEXTUAL-CONVENTIONS",
    **{"CnSlotGroupNameType": CnSlotGroupNameType,
       "cnTextualConventionsModule": cnTextualConventionsModule}
)
