# SNMP MIB module (BELAIR-PRODUCTS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_15768/BELAIR-PRODUCTS.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:08:43 2025
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

(belairModules,
 belairRegistrations) = mibBuilder.importSymbols(
    "BELAIR-SMI",
    "belairModules",
    "belairRegistrations")

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

belairProductsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 1, 3)
)
if mibBuilder.loadTexts:
    belairProductsModule.setRevisions(
        ("2009-05-27 11:32",
         "2009-05-11 14:38",
         "2009-02-23 08:45",
         "2008-11-26 14:05",
         "2007-04-11 16:30",
         "2006-01-24 14:00",
         "2005-07-22 13:45",
         "2004-09-20 10:05")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BelairBA200_ObjectIdentity = ObjectIdentity
belairBA200 = _BelairBA200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 2, 1)
)
if mibBuilder.loadTexts:
    belairBA200.setStatus("current")
_BelairBA200D_ObjectIdentity = ObjectIdentity
belairBA200D = _BelairBA200D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 2, 1, 1)
)
if mibBuilder.loadTexts:
    belairBA200D.setStatus("current")
_BelairBA100_ObjectIdentity = ObjectIdentity
belairBA100 = _BelairBA100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 2, 2)
)
if mibBuilder.loadTexts:
    belairBA100.setStatus("current")
_BelairBA100C_ObjectIdentity = ObjectIdentity
belairBA100C = _BelairBA100C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 2, 2, 1)
)
if mibBuilder.loadTexts:
    belairBA100C.setStatus("current")
_BelairBA100S_ObjectIdentity = ObjectIdentity
belairBA100S = _BelairBA100S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 2, 2, 2)
)
if mibBuilder.loadTexts:
    belairBA100S.setStatus("current")
_BelairBA100T_ObjectIdentity = ObjectIdentity
belairBA100T = _BelairBA100T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 2, 2, 3)
)
if mibBuilder.loadTexts:
    belairBA100T.setStatus("current")
_BelairBA100D_ObjectIdentity = ObjectIdentity
belairBA100D = _BelairBA100D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 2, 2, 4)
)
if mibBuilder.loadTexts:
    belairBA100D.setStatus("current")
_BelairBA100M_ObjectIdentity = ObjectIdentity
belairBA100M = _BelairBA100M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 2, 2, 5)
)
if mibBuilder.loadTexts:
    belairBA100M.setStatus("current")
_BelairBA100I_ObjectIdentity = ObjectIdentity
belairBA100I = _BelairBA100I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 2, 2, 6)
)
if mibBuilder.loadTexts:
    belairBA100I.setStatus("current")
_BelairBA50C_ObjectIdentity = ObjectIdentity
belairBA50C = _BelairBA50C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 2, 3)
)
if mibBuilder.loadTexts:
    belairBA50C.setStatus("current")
_BelairBA50S_ObjectIdentity = ObjectIdentity
belairBA50S = _BelairBA50S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 2, 4)
)
if mibBuilder.loadTexts:
    belairBA50S.setStatus("current")
_BelairBA20_ObjectIdentity = ObjectIdentity
belairBA20 = _BelairBA20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 2, 5)
)
if mibBuilder.loadTexts:
    belairBA20.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BELAIR-PRODUCTS",
    **{"belairProductsModule": belairProductsModule,
       "belairBA200": belairBA200,
       "belairBA200D": belairBA200D,
       "belairBA100": belairBA100,
       "belairBA100C": belairBA100C,
       "belairBA100S": belairBA100S,
       "belairBA100T": belairBA100T,
       "belairBA100D": belairBA100D,
       "belairBA100M": belairBA100M,
       "belairBA100I": belairBA100I,
       "belairBA50C": belairBA50C,
       "belairBA50S": belairBA50S,
       "belairBA20": belairBA20}
)
