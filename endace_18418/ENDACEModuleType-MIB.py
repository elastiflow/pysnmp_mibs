# SNMP MIB module (ENDACEModuleType-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/endace_18418/ENDACEModuleType-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:13:01 2025
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

(endace,) = mibBuilder.importSymbols(
    "ENDACE-MIB",
    "endace")

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

endaceModuleType = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 3)
)
if mibBuilder.loadTexts:
    endaceModuleType.setRevisions(
        ("2007-05-23 00:00",
         "2007-01-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EndaceModuleType(TextualConvention, Integer32):
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
              52,
              53,
              54,
              55,
              56,
              57)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("dag35e", 1),
          ("dag35", 2),
          ("dag36d", 3),
          ("dag36e", 4),
          ("dag36ge", 5),
          ("dag37d", 6),
          ("dag37ge", 7),
          ("dag37t", 8),
          ("dag38s", 9),
          ("dag42ge", 10),
          ("dag423ge", 11),
          ("dag42", 12),
          ("dag423", 13),
          ("dag43ge", 14),
          ("dag43s", 15),
          ("dag452e", 16),
          ("dag452gf", 17),
          ("dag452cf", 18),
          ("dag454e", 19),
          ("dag452z", 20),
          ("dag50s", 21),
          ("dag52x", 22),
          ("dag52sxa", 23),
          ("dag60", 24),
          ("dag61", 25),
          ("dag62", 26),
          ("dag70s", 27),
          ("dag70ge", 28),
          ("dag71s", 29),
          ("dag82x", 30),
          ("dag82x2", 31),
          ("dag82z", 32),
          ("dag800", 33),
          ("dag810", 34),
          ("dag50z", 35),
          ("dag50dup", 36),
          ("dag50sg2a", 37),
          ("dag50sg2adup", 38),
          ("dag452z8", 39),
          ("dag840", 40),
          ("dag54s12", 41),
          ("dag54sg48", 42),
          ("dag50sg3a", 43),
          ("dag54ga", 44),
          ("dag54sa12", 45),
          ("dag54sga48", 46),
          ("dag75g2", 47),
          ("dag75g4", 48),
          ("dag75be", 49),
          ("dag75ce", 50),
          ("dag74s", 51),
          ("dag74s48", 52),
          ("dag37t4", 53),
          ("dag91x2Rx", 54),
          ("dag91x2Tx", 55),
          ("dag850", 56),
          ("dag92x", 57))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENDACEModuleType-MIB",
    **{"EndaceModuleType": EndaceModuleType,
       "endaceModuleType": endaceModuleType}
)
