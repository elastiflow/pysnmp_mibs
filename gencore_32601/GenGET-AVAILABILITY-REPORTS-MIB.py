# SNMP MIB module (GenGET-AVAILABILITY-REPORTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gencore_32601/GenGET-AVAILABILITY-REPORTS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:08:41 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

genesis = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32601)
)
if mibBuilder.loadTexts:
    genesis.setRevisions(
        ("2016-03-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GenGET_ObjectIdentity = ObjectIdentity
genGET = _GenGET_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32601, 1)
)
_LTE_ObjectIdentity = ObjectIdentity
lTE = _LTE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2)
)
_Availability_ObjectIdentity = ObjectIdentity
availability = _Availability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 4)
)
_PmAvailabilityMIB_ObjectIdentity = ObjectIdentity
pmAvailabilityMIB = _PmAvailabilityMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 4, 1)
)
_PmAvailabilityMIBV2_ObjectIdentity = ObjectIdentity
pmAvailabilityMIBV2 = _PmAvailabilityMIBV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 4, 1, 0)
)
_PmAvailabilityObjects_ObjectIdentity = ObjectIdentity
pmAvailabilityObjects = _PmAvailabilityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 4, 1, 1)
)
_PmAvailabilityTableObjects_ObjectIdentity = ObjectIdentity
pmAvailabilityTableObjects = _PmAvailabilityTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 4, 1, 1, 1)
)
_PmAvailabilityTable_Object = MibTable
pmAvailabilityTable = _PmAvailabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 4, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pmAvailabilityTable.setStatus("mandatory")
_PmAvailabilityTableEntry_Object = MibTableRow
pmAvailabilityTableEntry = _PmAvailabilityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 4, 1, 1, 1, 1, 1)
)
pmAvailabilityTableEntry.setIndexNames(
    (0, "GenGET-AVAILABILITY-REPORTS-MIB", "pmAvailabilityId"),
)
if mibBuilder.loadTexts:
    pmAvailabilityTableEntry.setStatus("mandatory")


class _PmAvailabilityId_Type(Integer32):
    """Custom type pmAvailabilityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_PmAvailabilityId_Type.__name__ = "Integer32"
_PmAvailabilityId_Object = MibTableColumn
pmAvailabilityId = _PmAvailabilityId_Object(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 4, 1, 1, 1, 1, 1, 1),
    _PmAvailabilityId_Type()
)
pmAvailabilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAvailabilityId.setStatus("mandatory")
_PmAvailabilityStartDateAndTime_Type = DateAndTime
_PmAvailabilityStartDateAndTime_Object = MibTableColumn
pmAvailabilityStartDateAndTime = _PmAvailabilityStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 4, 1, 1, 1, 1, 1, 2),
    _PmAvailabilityStartDateAndTime_Type()
)
pmAvailabilityStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAvailabilityStartDateAndTime.setStatus("mandatory")
_PmAvailabilityDuration_Type = Unsigned32
_PmAvailabilityDuration_Object = MibTableColumn
pmAvailabilityDuration = _PmAvailabilityDuration_Object(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 4, 1, 1, 1, 1, 1, 3),
    _PmAvailabilityDuration_Type()
)
pmAvailabilityDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAvailabilityDuration.setStatus("mandatory")
_PmAvailabilityPlannedUnplanned_Type = DisplayString
_PmAvailabilityPlannedUnplanned_Object = MibTableColumn
pmAvailabilityPlannedUnplanned = _PmAvailabilityPlannedUnplanned_Object(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 4, 1, 1, 1, 1, 1, 4),
    _PmAvailabilityPlannedUnplanned_Type()
)
pmAvailabilityPlannedUnplanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAvailabilityPlannedUnplanned.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GenGET-AVAILABILITY-REPORTS-MIB",
    **{"genesis": genesis,
       "genGET": genGET,
       "lTE": lTE,
       "availability": availability,
       "pmAvailabilityMIB": pmAvailabilityMIB,
       "pmAvailabilityMIBV2": pmAvailabilityMIBV2,
       "pmAvailabilityObjects": pmAvailabilityObjects,
       "pmAvailabilityTableObjects": pmAvailabilityTableObjects,
       "pmAvailabilityTable": pmAvailabilityTable,
       "pmAvailabilityTableEntry": pmAvailabilityTableEntry,
       "pmAvailabilityId": pmAvailabilityId,
       "pmAvailabilityStartDateAndTime": pmAvailabilityStartDateAndTime,
       "pmAvailabilityDuration": pmAvailabilityDuration,
       "pmAvailabilityPlannedUnplanned": pmAvailabilityPlannedUnplanned}
)
