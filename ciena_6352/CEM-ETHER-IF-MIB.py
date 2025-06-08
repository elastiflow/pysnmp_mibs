# SNMP MIB module (CEM-ETHER-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-ETHER-IF-MIB.mib
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

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cemEtherIfModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 21)
)
if mibBuilder.loadTexts:
    cemEtherIfModule.setRevisions(
        ("2002-04-03 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CemEtherIfMIB_ObjectIdentity = ObjectIdentity
cemEtherIfMIB = _CemEtherIfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 21, 1)
)
if mibBuilder.loadTexts:
    cemEtherIfMIB.setStatus("current")
_CemEtherIfTables_ObjectIdentity = ObjectIdentity
cemEtherIfTables = _CemEtherIfTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 21, 1, 1)
)
if mibBuilder.loadTexts:
    cemEtherIfTables.setStatus("current")
_CemEtherIfTable_Object = MibTable
cemEtherIfTable = _CemEtherIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 21, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cemEtherIfTable.setStatus("current")
_CemEtherIfEntry_Object = MibTableRow
cemEtherIfEntry = _CemEtherIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 21, 1, 1, 1, 1)
)
cemEtherIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cemEtherIfEntry.setStatus("current")
_CemEtherIfRowStatus_Type = RowStatus
_CemEtherIfRowStatus_Object = MibTableColumn
cemEtherIfRowStatus = _CemEtherIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 21, 1, 1, 1, 1, 1),
    _CemEtherIfRowStatus_Type()
)
cemEtherIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cemEtherIfRowStatus.setStatus("current")
_CemEtherIfGroups_ObjectIdentity = ObjectIdentity
cemEtherIfGroups = _CemEtherIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 21, 1, 2)
)
if mibBuilder.loadTexts:
    cemEtherIfGroups.setStatus("current")
_CemEtherIfConformance_ObjectIdentity = ObjectIdentity
cemEtherIfConformance = _CemEtherIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 21, 1, 3)
)
if mibBuilder.loadTexts:
    cemEtherIfConformance.setStatus("current")

# Managed Objects groups

cemEtherIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 21, 1, 2, 1)
)
cemEtherIfGroup.setObjects(
    ("CEM-ETHER-IF-MIB", "cemEtherIfRowStatus")
)
if mibBuilder.loadTexts:
    cemEtherIfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cemEtherIfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6352, 21, 1, 3, 1)
)
cemEtherIfCompliance.setObjects(
    ("CEM-ETHER-IF-MIB", "cemEtherIfGroup")
)
if mibBuilder.loadTexts:
    cemEtherIfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-ETHER-IF-MIB",
    **{"cemEtherIfModule": cemEtherIfModule,
       "cemEtherIfMIB": cemEtherIfMIB,
       "cemEtherIfTables": cemEtherIfTables,
       "cemEtherIfTable": cemEtherIfTable,
       "cemEtherIfEntry": cemEtherIfEntry,
       "cemEtherIfRowStatus": cemEtherIfRowStatus,
       "cemEtherIfGroups": cemEtherIfGroups,
       "cemEtherIfGroup": cemEtherIfGroup,
       "cemEtherIfConformance": cemEtherIfConformance,
       "cemEtherIfCompliance": cemEtherIfCompliance}
)
