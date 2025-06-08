# SNMP MIB module (MIMOSA-MIB-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/mimosa_43356/MIMOSA-MIB-TC.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:32:23 2025
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

(mimosa,) = mibBuilder.importSymbols(
    "MIMOSA-NETWORKS-BASE-MIB",
    "mimosa")

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

mimosaMibTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 3)
)
if mibBuilder.loadTexts:
    mimosaMibTC.setRevisions(
        ("2017-02-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DecimalOne(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class DecimalTwo(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"


class DecimalFive(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-5"


class Mimosa5GHzFrequency(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4800, 6200),
    )



class Mimosa5GHzChannelNumber(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIMOSA-MIB-TC",
    **{"DecimalOne": DecimalOne,
       "DecimalTwo": DecimalTwo,
       "DecimalFive": DecimalFive,
       "Mimosa5GHzFrequency": Mimosa5GHzFrequency,
       "Mimosa5GHzChannelNumber": Mimosa5GHzChannelNumber,
       "mimosaMibTC": mimosaMibTC}
)
