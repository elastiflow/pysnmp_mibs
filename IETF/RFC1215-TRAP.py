# SNMP MIB module (RFC1215-TRAP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/RFC1215-TRAP.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:57:36 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(egpNeighAddr,) = mibBuilder.importSymbols(
    "RFC1213-MIB",
    "egpNeighAddr")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(snmp,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmp")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

coldStart = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 0)
)
if mibBuilder.loadTexts:
    coldStart.setStatus(
        ""
    )

warmStart = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 1)
)
if mibBuilder.loadTexts:
    warmStart.setStatus(
        ""
    )

linkDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 2)
)
linkDown.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    linkDown.setStatus(
        ""
    )

linkUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 3)
)
linkUp.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    linkUp.setStatus(
        ""
    )

authenticationFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 4)
)
if mibBuilder.loadTexts:
    authenticationFailure.setStatus(
        ""
    )

egpNeighborLoss = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 5)
)
egpNeighborLoss.setObjects(
    ("RFC1213-MIB", "egpNeighAddr")
)
if mibBuilder.loadTexts:
    egpNeighborLoss.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1215-TRAP",
    **{"coldStart": coldStart,
       "warmStart": warmStart,
       "linkDown": linkDown,
       "linkUp": linkUp,
       "authenticationFailure": authenticationFailure,
       "egpNeighborLoss": egpNeighborLoss}
)
