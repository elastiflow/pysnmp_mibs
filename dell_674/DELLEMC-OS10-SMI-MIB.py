# SNMP MIB module (DELLEMC-OS10-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/dell_674/DELLEMC-OS10-SMI-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 16:03:24 2025
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

dell = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
if mibBuilder.loadTexts:
    dell.setRevisions(
        ("2017-06-02 18:01",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EnterpriseSW_ObjectIdentity = ObjectIdentity
enterpriseSW = _EnterpriseSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000)
)
_Networking_ObjectIdentity = ObjectIdentity
networking = _Networking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000)
)
_Os10_ObjectIdentity = ObjectIdentity
os10 = _Os10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100)
)
if mibBuilder.loadTexts:
    os10.setStatus("current")
_Os10Experiment_ObjectIdentity = ObjectIdentity
os10Experiment = _Os10Experiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200)
)
if mibBuilder.loadTexts:
    os10Experiment.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELLEMC-OS10-SMI-MIB",
    **{"dell": dell,
       "enterpriseSW": enterpriseSW,
       "networking": networking,
       "os10": os10,
       "os10Experiment": os10Experiment}
)
