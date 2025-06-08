# SNMP MIB module (FORCE10-REF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/force10_6027/FORCE10-REF-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:18:05 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

force10 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027)
)
if mibBuilder.loadTexts:
    force10.setRevisions(
        ("2005-01-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AgentPortMask(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_F10Products_ObjectIdentity = ObjectIdentity
f10Products = _F10Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1)
)
_F10SSeriesFamilyMIB_ObjectIdentity = ObjectIdentity
f10SSeriesFamilyMIB = _F10SSeriesFamilyMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3)
)
_SFTOS_ObjectIdentity = ObjectIdentity
sFTOS = _SFTOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORCE10-REF-MIB",
    **{"AgentPortMask": AgentPortMask,
       "force10": force10,
       "f10Products": f10Products,
       "f10SSeriesFamilyMIB": f10SSeriesFamilyMIB,
       "sFTOS": sFTOS}
)
