# SNMP MIB module (BIGSWITCH-SWITCHLIGHT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/bigswitch_37538/BIGSWITCH-SWITCHLIGHT-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:48:03 2025
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

(bsn,) = mibBuilder.importSymbols(
    "BIGSWITCH-MIB",
    "bsn")

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

bsnSwitchlight = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37538, 2)
)
if mibBuilder.loadTexts:
    bsnSwitchlight.setRevisions(
        ("2014-01-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlFlowTables_ObjectIdentity = ObjectIdentity
slFlowTables = _SlFlowTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1)
)
_SlL2Table_ObjectIdentity = ObjectIdentity
slL2Table = _SlL2Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1, 1)
)
_SlTCAMFMTable_ObjectIdentity = ObjectIdentity
slTCAMFMTable = _SlTCAMFMTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1, 2)
)
_SlLinkTables_ObjectIdentity = ObjectIdentity
slLinkTables = _SlLinkTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37538, 2, 2)
)
_SlLinkTable_ObjectIdentity = ObjectIdentity
slLinkTable = _SlLinkTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37538, 2, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIGSWITCH-SWITCHLIGHT-MIB",
    **{"bsnSwitchlight": bsnSwitchlight,
       "slFlowTables": slFlowTables,
       "slL2Table": slL2Table,
       "slTCAMFMTable": slTCAMFMTable,
       "slLinkTables": slLinkTables,
       "slLinkTable": slLinkTable}
)
