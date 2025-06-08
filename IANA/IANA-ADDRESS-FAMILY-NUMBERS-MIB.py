# SNMP MIB module (IANA-ADDRESS-FAMILY-NUMBERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/IANA-ADDRESS-FAMILY-NUMBERS-MIB.mib
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

ianaAddressFamilyNumbers = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 72)
)
if mibBuilder.loadTexts:
    ianaAddressFamilyNumbers.setRevisions(
        ("2000-09-08 00:00",
         "2000-03-01 00:00",
         "2000-02-04 00:00",
         "1999-08-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AddressFamilyNumbers(TextualConvention, Integer32):
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
              65535)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("ipV4", 1),
          ("ipV6", 2),
          ("nsap", 3),
          ("hdlc", 4),
          ("bbn1822", 5),
          ("all802", 6),
          ("e163", 7),
          ("e164", 8),
          ("f69", 9),
          ("x121", 10),
          ("ipx", 11),
          ("appletalk", 12),
          ("decnetIV", 13),
          ("banyanVines", 14),
          ("e164withNsap", 15),
          ("dns", 16),
          ("distinguishedname", 17),
          ("asnumber", 18),
          ("xtpoveripv4", 19),
          ("xtpoveripv6", 20),
          ("xtpnativemodextp", 21),
          ("reserved", 65535))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    **{"AddressFamilyNumbers": AddressFamilyNumbers,
       "ianaAddressFamilyNumbers": ianaAddressFamilyNumbers}
)
