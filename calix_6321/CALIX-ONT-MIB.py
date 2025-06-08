# SNMP MIB module (CALIX-ONT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/calix_6321/CALIX-ONT-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 17:18:56 2025
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

(c7,) = mibBuilder.importSymbols(
    "CALIX-PRODUCT-MIB",
    "c7")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

calixOnt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CalixOntCurrentTable_Object = MibTable
calixOntCurrentTable = _CalixOntCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    calixOntCurrentTable.setStatus("current")
_CalixOntCurrentEntry_Object = MibTableRow
calixOntCurrentEntry = _CalixOntCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 1, 1)
)
calixOntCurrentEntry.setIndexNames(
    (0, "CALIX-ONT-MIB", "calixOntCurrentIndex"),
)
if mibBuilder.loadTexts:
    calixOntCurrentEntry.setStatus("current")
_CalixOntCurrentIndex_Type = InterfaceIndex
_CalixOntCurrentIndex_Object = MibTableColumn
calixOntCurrentIndex = _CalixOntCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 1, 1, 1),
    _CalixOntCurrentIndex_Type()
)
calixOntCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntCurrentIndex.setStatus("current")
_CalixOntCurrentBip8_Type = PerfCurrentCount
_CalixOntCurrentBip8_Object = MibTableColumn
calixOntCurrentBip8 = _CalixOntCurrentBip8_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 1, 1, 2),
    _CalixOntCurrentBip8_Type()
)
calixOntCurrentBip8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntCurrentBip8.setStatus("current")
_CalixOntCurrentBip8Es_Type = PerfCurrentCount
_CalixOntCurrentBip8Es_Object = MibTableColumn
calixOntCurrentBip8Es = _CalixOntCurrentBip8Es_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 1, 1, 3),
    _CalixOntCurrentBip8Es_Type()
)
calixOntCurrentBip8Es.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntCurrentBip8Es.setStatus("current")
_CalixOntCurrentSes_Type = PerfCurrentCount
_CalixOntCurrentSes_Object = MibTableColumn
calixOntCurrentSes = _CalixOntCurrentSes_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 1, 1, 4),
    _CalixOntCurrentSes_Type()
)
calixOntCurrentSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntCurrentSes.setStatus("current")
_CalixOntCurrentUas_Type = PerfCurrentCount
_CalixOntCurrentUas_Object = MibTableColumn
calixOntCurrentUas = _CalixOntCurrentUas_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 1, 1, 5),
    _CalixOntCurrentUas_Type()
)
calixOntCurrentUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntCurrentUas.setStatus("current")
_CalixOntCurrentMiss_Type = PerfCurrentCount
_CalixOntCurrentMiss_Object = MibTableColumn
calixOntCurrentMiss = _CalixOntCurrentMiss_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 1, 1, 6),
    _CalixOntCurrentMiss_Type()
)
calixOntCurrentMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntCurrentMiss.setStatus("current")
_CalixOntCurrentMissEs_Type = PerfCurrentCount
_CalixOntCurrentMissEs_Object = MibTableColumn
calixOntCurrentMissEs = _CalixOntCurrentMissEs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 1, 1, 7),
    _CalixOntCurrentMissEs_Type()
)
calixOntCurrentMissEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntCurrentMissEs.setStatus("current")
_CalixOntIntervalTable_Object = MibTable
calixOntIntervalTable = _CalixOntIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    calixOntIntervalTable.setStatus("current")
_CalixOntIntervalEntry_Object = MibTableRow
calixOntIntervalEntry = _CalixOntIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 2, 1)
)
calixOntIntervalEntry.setIndexNames(
    (0, "CALIX-ONT-MIB", "calixOntIntervalIndex"),
    (0, "CALIX-ONT-MIB", "calixOntIntervalNumber"),
)
if mibBuilder.loadTexts:
    calixOntIntervalEntry.setStatus("current")
_CalixOntIntervalIndex_Type = InterfaceIndex
_CalixOntIntervalIndex_Object = MibTableColumn
calixOntIntervalIndex = _CalixOntIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 2, 1, 1),
    _CalixOntIntervalIndex_Type()
)
calixOntIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntIntervalIndex.setStatus("current")


class _CalixOntIntervalNumber_Type(Integer32):
    """Custom type calixOntIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CalixOntIntervalNumber_Type.__name__ = "Integer32"
_CalixOntIntervalNumber_Object = MibTableColumn
calixOntIntervalNumber = _CalixOntIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 2, 1, 2),
    _CalixOntIntervalNumber_Type()
)
calixOntIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntIntervalNumber.setStatus("current")
_CalixOntIntervalBip8_Type = PerfIntervalCount
_CalixOntIntervalBip8_Object = MibTableColumn
calixOntIntervalBip8 = _CalixOntIntervalBip8_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 2, 1, 3),
    _CalixOntIntervalBip8_Type()
)
calixOntIntervalBip8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntIntervalBip8.setStatus("current")
_CalixOntIntervalBip8Es_Type = PerfIntervalCount
_CalixOntIntervalBip8Es_Object = MibTableColumn
calixOntIntervalBip8Es = _CalixOntIntervalBip8Es_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 2, 1, 4),
    _CalixOntIntervalBip8Es_Type()
)
calixOntIntervalBip8Es.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntIntervalBip8Es.setStatus("current")
_CalixOntIntervalSes_Type = PerfIntervalCount
_CalixOntIntervalSes_Object = MibTableColumn
calixOntIntervalSes = _CalixOntIntervalSes_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 2, 1, 5),
    _CalixOntIntervalSes_Type()
)
calixOntIntervalSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntIntervalSes.setStatus("current")
_CalixOntIntervalUas_Type = PerfIntervalCount
_CalixOntIntervalUas_Object = MibTableColumn
calixOntIntervalUas = _CalixOntIntervalUas_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 2, 1, 6),
    _CalixOntIntervalUas_Type()
)
calixOntIntervalUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntIntervalUas.setStatus("current")
_CalixOntIntervalMiss_Type = PerfIntervalCount
_CalixOntIntervalMiss_Object = MibTableColumn
calixOntIntervalMiss = _CalixOntIntervalMiss_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 2, 1, 7),
    _CalixOntIntervalMiss_Type()
)
calixOntIntervalMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntIntervalMiss.setStatus("current")
_CalixOntIntervalMissEs_Type = PerfIntervalCount
_CalixOntIntervalMissEs_Object = MibTableColumn
calixOntIntervalMissEs = _CalixOntIntervalMissEs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 2, 1, 8),
    _CalixOntIntervalMissEs_Type()
)
calixOntIntervalMissEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntIntervalMissEs.setStatus("current")
_CalixOntIntervalValidData_Type = TruthValue
_CalixOntIntervalValidData_Object = MibTableColumn
calixOntIntervalValidData = _CalixOntIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 2, 1, 9),
    _CalixOntIntervalValidData_Type()
)
calixOntIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntIntervalValidData.setStatus("current")
_CalixOntTotalTable_Object = MibTable
calixOntTotalTable = _CalixOntTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 3)
)
if mibBuilder.loadTexts:
    calixOntTotalTable.setStatus("current")
_CalixOntTotalEntry_Object = MibTableRow
calixOntTotalEntry = _CalixOntTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 3, 1)
)
calixOntTotalEntry.setIndexNames(
    (0, "CALIX-ONT-MIB", "calixOntTotalIndex"),
)
if mibBuilder.loadTexts:
    calixOntTotalEntry.setStatus("current")
_CalixOntTotalIndex_Type = InterfaceIndex
_CalixOntTotalIndex_Object = MibTableColumn
calixOntTotalIndex = _CalixOntTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 3, 1, 1),
    _CalixOntTotalIndex_Type()
)
calixOntTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntTotalIndex.setStatus("current")
_CalixOntTotalBip8_Type = PerfTotalCount
_CalixOntTotalBip8_Object = MibTableColumn
calixOntTotalBip8 = _CalixOntTotalBip8_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 3, 1, 2),
    _CalixOntTotalBip8_Type()
)
calixOntTotalBip8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntTotalBip8.setStatus("current")
_CalixOntTotalBip8Es_Type = PerfTotalCount
_CalixOntTotalBip8Es_Object = MibTableColumn
calixOntTotalBip8Es = _CalixOntTotalBip8Es_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 3, 1, 3),
    _CalixOntTotalBip8Es_Type()
)
calixOntTotalBip8Es.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntTotalBip8Es.setStatus("current")
_CalixOntTotalSes_Type = PerfTotalCount
_CalixOntTotalSes_Object = MibTableColumn
calixOntTotalSes = _CalixOntTotalSes_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 3, 1, 4),
    _CalixOntTotalSes_Type()
)
calixOntTotalSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntTotalSes.setStatus("current")
_CalixOntTotalUas_Type = PerfTotalCount
_CalixOntTotalUas_Object = MibTableColumn
calixOntTotalUas = _CalixOntTotalUas_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 3, 1, 5),
    _CalixOntTotalUas_Type()
)
calixOntTotalUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntTotalUas.setStatus("current")
_CalixOntTotalMiss_Type = PerfTotalCount
_CalixOntTotalMiss_Object = MibTableColumn
calixOntTotalMiss = _CalixOntTotalMiss_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 3, 1, 6),
    _CalixOntTotalMiss_Type()
)
calixOntTotalMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntTotalMiss.setStatus("current")
_CalixOntTotalMissEs_Type = PerfTotalCount
_CalixOntTotalMissEs_Object = MibTableColumn
calixOntTotalMissEs = _CalixOntTotalMissEs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 3, 1, 7),
    _CalixOntTotalMissEs_Type()
)
calixOntTotalMissEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntTotalMissEs.setStatus("current")
_CalixOntFarEndCurrentTable_Object = MibTable
calixOntFarEndCurrentTable = _CalixOntFarEndCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 4)
)
if mibBuilder.loadTexts:
    calixOntFarEndCurrentTable.setStatus("current")
_CalixOntFarEndCurrentEntry_Object = MibTableRow
calixOntFarEndCurrentEntry = _CalixOntFarEndCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 4, 1)
)
calixOntFarEndCurrentEntry.setIndexNames(
    (0, "CALIX-ONT-MIB", "calixOntFarEndCurrentIndex"),
)
if mibBuilder.loadTexts:
    calixOntFarEndCurrentEntry.setStatus("current")
_CalixOntFarEndCurrentIndex_Type = InterfaceIndex
_CalixOntFarEndCurrentIndex_Object = MibTableColumn
calixOntFarEndCurrentIndex = _CalixOntFarEndCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 4, 1, 1),
    _CalixOntFarEndCurrentIndex_Type()
)
calixOntFarEndCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndCurrentIndex.setStatus("current")


class _CalixOntFarEndTimeElapsed_Type(Integer32):
    """Custom type calixOntFarEndTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_CalixOntFarEndTimeElapsed_Type.__name__ = "Integer32"
_CalixOntFarEndTimeElapsed_Object = MibTableColumn
calixOntFarEndTimeElapsed = _CalixOntFarEndTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 4, 1, 2),
    _CalixOntFarEndTimeElapsed_Type()
)
calixOntFarEndTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndTimeElapsed.setStatus("current")


class _CalixOntFarEndValidIntervals_Type(Integer32):
    """Custom type calixOntFarEndValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CalixOntFarEndValidIntervals_Type.__name__ = "Integer32"
_CalixOntFarEndValidIntervals_Object = MibTableColumn
calixOntFarEndValidIntervals = _CalixOntFarEndValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 4, 1, 3),
    _CalixOntFarEndValidIntervals_Type()
)
calixOntFarEndValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndValidIntervals.setStatus("current")
_CalixOntFarEndCurrentBip8_Type = PerfCurrentCount
_CalixOntFarEndCurrentBip8_Object = MibTableColumn
calixOntFarEndCurrentBip8 = _CalixOntFarEndCurrentBip8_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 4, 1, 4),
    _CalixOntFarEndCurrentBip8_Type()
)
calixOntFarEndCurrentBip8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndCurrentBip8.setStatus("current")
_CalixOntFarEndCurrentBip8Es_Type = PerfCurrentCount
_CalixOntFarEndCurrentBip8Es_Object = MibTableColumn
calixOntFarEndCurrentBip8Es = _CalixOntFarEndCurrentBip8Es_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 4, 1, 5),
    _CalixOntFarEndCurrentBip8Es_Type()
)
calixOntFarEndCurrentBip8Es.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndCurrentBip8Es.setStatus("current")
_CalixOntFarEndCurrentSes_Type = PerfCurrentCount
_CalixOntFarEndCurrentSes_Object = MibTableColumn
calixOntFarEndCurrentSes = _CalixOntFarEndCurrentSes_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 4, 1, 6),
    _CalixOntFarEndCurrentSes_Type()
)
calixOntFarEndCurrentSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndCurrentSes.setStatus("current")
_CalixOntFarEndCurrentUas_Type = PerfCurrentCount
_CalixOntFarEndCurrentUas_Object = MibTableColumn
calixOntFarEndCurrentUas = _CalixOntFarEndCurrentUas_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 4, 1, 7),
    _CalixOntFarEndCurrentUas_Type()
)
calixOntFarEndCurrentUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndCurrentUas.setStatus("current")


class _CalixOntFarEndInvalidIntervals_Type(Integer32):
    """Custom type calixOntFarEndInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CalixOntFarEndInvalidIntervals_Type.__name__ = "Integer32"
_CalixOntFarEndInvalidIntervals_Object = MibTableColumn
calixOntFarEndInvalidIntervals = _CalixOntFarEndInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 4, 1, 8),
    _CalixOntFarEndInvalidIntervals_Type()
)
calixOntFarEndInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndInvalidIntervals.setStatus("current")
_CalixOntFarEndIntervalTable_Object = MibTable
calixOntFarEndIntervalTable = _CalixOntFarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 5)
)
if mibBuilder.loadTexts:
    calixOntFarEndIntervalTable.setStatus("current")
_CalixOntFarEndIntervalEntry_Object = MibTableRow
calixOntFarEndIntervalEntry = _CalixOntFarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 5, 1)
)
calixOntFarEndIntervalEntry.setIndexNames(
    (0, "CALIX-ONT-MIB", "calixOntFarEndIntervalIndex"),
    (0, "CALIX-ONT-MIB", "calixOntFarEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    calixOntFarEndIntervalEntry.setStatus("current")
_CalixOntFarEndIntervalIndex_Type = InterfaceIndex
_CalixOntFarEndIntervalIndex_Object = MibTableColumn
calixOntFarEndIntervalIndex = _CalixOntFarEndIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 5, 1, 1),
    _CalixOntFarEndIntervalIndex_Type()
)
calixOntFarEndIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndIntervalIndex.setStatus("current")


class _CalixOntFarEndIntervalNumber_Type(Integer32):
    """Custom type calixOntFarEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CalixOntFarEndIntervalNumber_Type.__name__ = "Integer32"
_CalixOntFarEndIntervalNumber_Object = MibTableColumn
calixOntFarEndIntervalNumber = _CalixOntFarEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 5, 1, 2),
    _CalixOntFarEndIntervalNumber_Type()
)
calixOntFarEndIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndIntervalNumber.setStatus("current")
_CalixOntFarEndIntervalBip8_Type = PerfIntervalCount
_CalixOntFarEndIntervalBip8_Object = MibTableColumn
calixOntFarEndIntervalBip8 = _CalixOntFarEndIntervalBip8_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 5, 1, 3),
    _CalixOntFarEndIntervalBip8_Type()
)
calixOntFarEndIntervalBip8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndIntervalBip8.setStatus("current")
_CalixOntFarEndIntervalBip8Es_Type = PerfIntervalCount
_CalixOntFarEndIntervalBip8Es_Object = MibTableColumn
calixOntFarEndIntervalBip8Es = _CalixOntFarEndIntervalBip8Es_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 5, 1, 4),
    _CalixOntFarEndIntervalBip8Es_Type()
)
calixOntFarEndIntervalBip8Es.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndIntervalBip8Es.setStatus("current")
_CalixOntFarEndIntervalSes_Type = PerfIntervalCount
_CalixOntFarEndIntervalSes_Object = MibTableColumn
calixOntFarEndIntervalSes = _CalixOntFarEndIntervalSes_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 5, 1, 5),
    _CalixOntFarEndIntervalSes_Type()
)
calixOntFarEndIntervalSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndIntervalSes.setStatus("current")
_CalixOntFarEndIntervalUas_Type = PerfIntervalCount
_CalixOntFarEndIntervalUas_Object = MibTableColumn
calixOntFarEndIntervalUas = _CalixOntFarEndIntervalUas_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 5, 1, 6),
    _CalixOntFarEndIntervalUas_Type()
)
calixOntFarEndIntervalUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndIntervalUas.setStatus("current")
_CalixOntFarEndIntervalValidData_Type = TruthValue
_CalixOntFarEndIntervalValidData_Object = MibTableColumn
calixOntFarEndIntervalValidData = _CalixOntFarEndIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 5, 1, 7),
    _CalixOntFarEndIntervalValidData_Type()
)
calixOntFarEndIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndIntervalValidData.setStatus("current")
_CalixOntFarEndTotalTable_Object = MibTable
calixOntFarEndTotalTable = _CalixOntFarEndTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 6)
)
if mibBuilder.loadTexts:
    calixOntFarEndTotalTable.setStatus("current")
_CalixOntFarEndTotalEntry_Object = MibTableRow
calixOntFarEndTotalEntry = _CalixOntFarEndTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 6, 1)
)
calixOntFarEndTotalEntry.setIndexNames(
    (0, "CALIX-ONT-MIB", "calixOntFarEndTotalIndex"),
)
if mibBuilder.loadTexts:
    calixOntFarEndTotalEntry.setStatus("current")
_CalixOntFarEndTotalIndex_Type = InterfaceIndex
_CalixOntFarEndTotalIndex_Object = MibTableColumn
calixOntFarEndTotalIndex = _CalixOntFarEndTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 6, 1, 1),
    _CalixOntFarEndTotalIndex_Type()
)
calixOntFarEndTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndTotalIndex.setStatus("current")
_CalixOntFarEndTotalBip8_Type = PerfTotalCount
_CalixOntFarEndTotalBip8_Object = MibTableColumn
calixOntFarEndTotalBip8 = _CalixOntFarEndTotalBip8_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 6, 1, 2),
    _CalixOntFarEndTotalBip8_Type()
)
calixOntFarEndTotalBip8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndTotalBip8.setStatus("current")
_CalixOntFarEndTotalBip8Es_Type = PerfTotalCount
_CalixOntFarEndTotalBip8Es_Object = MibTableColumn
calixOntFarEndTotalBip8Es = _CalixOntFarEndTotalBip8Es_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 6, 1, 3),
    _CalixOntFarEndTotalBip8Es_Type()
)
calixOntFarEndTotalBip8Es.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndTotalBip8Es.setStatus("current")
_CalixOntFarEndTotalSes_Type = PerfTotalCount
_CalixOntFarEndTotalSes_Object = MibTableColumn
calixOntFarEndTotalSes = _CalixOntFarEndTotalSes_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 6, 1, 4),
    _CalixOntFarEndTotalSes_Type()
)
calixOntFarEndTotalSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndTotalSes.setStatus("current")
_CalixOntFarEndTotalUas_Type = PerfTotalCount
_CalixOntFarEndTotalUas_Object = MibTableColumn
calixOntFarEndTotalUas = _CalixOntFarEndTotalUas_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 6, 6, 1, 5),
    _CalixOntFarEndTotalUas_Type()
)
calixOntFarEndTotalUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntFarEndTotalUas.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CALIX-ONT-MIB",
    **{"calixOnt": calixOnt,
       "calixOntCurrentTable": calixOntCurrentTable,
       "calixOntCurrentEntry": calixOntCurrentEntry,
       "calixOntCurrentIndex": calixOntCurrentIndex,
       "calixOntCurrentBip8": calixOntCurrentBip8,
       "calixOntCurrentBip8Es": calixOntCurrentBip8Es,
       "calixOntCurrentSes": calixOntCurrentSes,
       "calixOntCurrentUas": calixOntCurrentUas,
       "calixOntCurrentMiss": calixOntCurrentMiss,
       "calixOntCurrentMissEs": calixOntCurrentMissEs,
       "calixOntIntervalTable": calixOntIntervalTable,
       "calixOntIntervalEntry": calixOntIntervalEntry,
       "calixOntIntervalIndex": calixOntIntervalIndex,
       "calixOntIntervalNumber": calixOntIntervalNumber,
       "calixOntIntervalBip8": calixOntIntervalBip8,
       "calixOntIntervalBip8Es": calixOntIntervalBip8Es,
       "calixOntIntervalSes": calixOntIntervalSes,
       "calixOntIntervalUas": calixOntIntervalUas,
       "calixOntIntervalMiss": calixOntIntervalMiss,
       "calixOntIntervalMissEs": calixOntIntervalMissEs,
       "calixOntIntervalValidData": calixOntIntervalValidData,
       "calixOntTotalTable": calixOntTotalTable,
       "calixOntTotalEntry": calixOntTotalEntry,
       "calixOntTotalIndex": calixOntTotalIndex,
       "calixOntTotalBip8": calixOntTotalBip8,
       "calixOntTotalBip8Es": calixOntTotalBip8Es,
       "calixOntTotalSes": calixOntTotalSes,
       "calixOntTotalUas": calixOntTotalUas,
       "calixOntTotalMiss": calixOntTotalMiss,
       "calixOntTotalMissEs": calixOntTotalMissEs,
       "calixOntFarEndCurrentTable": calixOntFarEndCurrentTable,
       "calixOntFarEndCurrentEntry": calixOntFarEndCurrentEntry,
       "calixOntFarEndCurrentIndex": calixOntFarEndCurrentIndex,
       "calixOntFarEndTimeElapsed": calixOntFarEndTimeElapsed,
       "calixOntFarEndValidIntervals": calixOntFarEndValidIntervals,
       "calixOntFarEndCurrentBip8": calixOntFarEndCurrentBip8,
       "calixOntFarEndCurrentBip8Es": calixOntFarEndCurrentBip8Es,
       "calixOntFarEndCurrentSes": calixOntFarEndCurrentSes,
       "calixOntFarEndCurrentUas": calixOntFarEndCurrentUas,
       "calixOntFarEndInvalidIntervals": calixOntFarEndInvalidIntervals,
       "calixOntFarEndIntervalTable": calixOntFarEndIntervalTable,
       "calixOntFarEndIntervalEntry": calixOntFarEndIntervalEntry,
       "calixOntFarEndIntervalIndex": calixOntFarEndIntervalIndex,
       "calixOntFarEndIntervalNumber": calixOntFarEndIntervalNumber,
       "calixOntFarEndIntervalBip8": calixOntFarEndIntervalBip8,
       "calixOntFarEndIntervalBip8Es": calixOntFarEndIntervalBip8Es,
       "calixOntFarEndIntervalSes": calixOntFarEndIntervalSes,
       "calixOntFarEndIntervalUas": calixOntFarEndIntervalUas,
       "calixOntFarEndIntervalValidData": calixOntFarEndIntervalValidData,
       "calixOntFarEndTotalTable": calixOntFarEndTotalTable,
       "calixOntFarEndTotalEntry": calixOntFarEndTotalEntry,
       "calixOntFarEndTotalIndex": calixOntFarEndTotalIndex,
       "calixOntFarEndTotalBip8": calixOntFarEndTotalBip8,
       "calixOntFarEndTotalBip8Es": calixOntFarEndTotalBip8Es,
       "calixOntFarEndTotalSes": calixOntFarEndTotalSes,
       "calixOntFarEndTotalUas": calixOntFarEndTotalUas}
)
