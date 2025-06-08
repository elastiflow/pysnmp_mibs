# SNMP MIB module (ACMEPACKET-PRODUCTS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/acmepacket_9148/ACMEPACKET-PRODUCTS.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:10:25 2025
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

(acmepacket,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacket")

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

acmepacketProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1)
)
if mibBuilder.loadTexts:
    acmepacketProducts.setRevisions(
        ("2012-07-16 00:00",
         "2007-04-03 15:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApNetNet4000Series_ObjectIdentity = ObjectIdentity
apNetNet4000Series = _ApNetNet4000Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 1)
)
if mibBuilder.loadTexts:
    apNetNet4000Series.setStatus("current")
_ApNetNet4250_ObjectIdentity = ObjectIdentity
apNetNet4250 = _ApNetNet4250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 1, 1)
)
if mibBuilder.loadTexts:
    apNetNet4250.setStatus("current")
_ApNetNet4500_ObjectIdentity = ObjectIdentity
apNetNet4500 = _ApNetNet4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 1, 2)
)
if mibBuilder.loadTexts:
    apNetNet4500.setStatus("current")
_ApNetNet9000Series_ObjectIdentity = ObjectIdentity
apNetNet9000Series = _ApNetNet9000Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 2)
)
if mibBuilder.loadTexts:
    apNetNet9000Series.setStatus("current")
_ApNetNet9200_ObjectIdentity = ObjectIdentity
apNetNet9200 = _ApNetNet9200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 2, 1)
)
if mibBuilder.loadTexts:
    apNetNet9200.setStatus("current")
_ApNetNet3000Series_ObjectIdentity = ObjectIdentity
apNetNet3000Series = _ApNetNet3000Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 3)
)
if mibBuilder.loadTexts:
    apNetNet3000Series.setStatus("current")
_ApNetNet3800_ObjectIdentity = ObjectIdentity
apNetNet3800 = _ApNetNet3800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 3, 1)
)
if mibBuilder.loadTexts:
    apNetNet3800.setStatus("current")
_ApNetNet3820_ObjectIdentity = ObjectIdentity
apNetNet3820 = _ApNetNet3820_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 3, 2)
)
if mibBuilder.loadTexts:
    apNetNet3820.setStatus("current")
_ApNetNetOSSeries_ObjectIdentity = ObjectIdentity
apNetNetOSSeries = _ApNetNetOSSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 4)
)
if mibBuilder.loadTexts:
    apNetNetOSSeries.setStatus("current")
_ApNetNetOS_ObjectIdentity = ObjectIdentity
apNetNetOS = _ApNetNetOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 4, 1)
)
if mibBuilder.loadTexts:
    apNetNetOS.setStatus("current")
_ApNetNetOSVM_ObjectIdentity = ObjectIdentity
apNetNetOSVM = _ApNetNetOSVM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 4, 2)
)
if mibBuilder.loadTexts:
    apNetNetOSVM.setStatus("current")
_ApNetNet6000Series_ObjectIdentity = ObjectIdentity
apNetNet6000Series = _ApNetNet6000Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 5)
)
if mibBuilder.loadTexts:
    apNetNet6000Series.setStatus("current")
_ApNetNet6300_ObjectIdentity = ObjectIdentity
apNetNet6300 = _ApNetNet6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 5, 1)
)
if mibBuilder.loadTexts:
    apNetNet6300.setStatus("current")
_ApNetNet1000Series_ObjectIdentity = ObjectIdentity
apNetNet1000Series = _ApNetNet1000Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 6)
)
if mibBuilder.loadTexts:
    apNetNet1000Series.setStatus("current")
_ApNetNet1100_ObjectIdentity = ObjectIdentity
apNetNet1100 = _ApNetNet1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1, 6, 1)
)
if mibBuilder.loadTexts:
    apNetNet1100.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACMEPACKET-PRODUCTS",
    **{"acmepacketProducts": acmepacketProducts,
       "apNetNet4000Series": apNetNet4000Series,
       "apNetNet4250": apNetNet4250,
       "apNetNet4500": apNetNet4500,
       "apNetNet9000Series": apNetNet9000Series,
       "apNetNet9200": apNetNet9200,
       "apNetNet3000Series": apNetNet3000Series,
       "apNetNet3800": apNetNet3800,
       "apNetNet3820": apNetNet3820,
       "apNetNetOSSeries": apNetNetOSSeries,
       "apNetNetOS": apNetNetOS,
       "apNetNetOSVM": apNetNetOSVM,
       "apNetNet6000Series": apNetNet6000Series,
       "apNetNet6300": apNetNet6300,
       "apNetNet1000Series": apNetNet1000Series,
       "apNetNet1100": apNetNet1100}
)
