# SNMP MIB module (CALIX-ONT-ETH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/calix_6321/CALIX-ONT-ETH-MIB.mib
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

calixOntEth = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CalixOntEthCurrentTable_Object = MibTable
calixOntEthCurrentTable = _CalixOntEthCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    calixOntEthCurrentTable.setStatus("current")
_CalixOntEthCurrentEntry_Object = MibTableRow
calixOntEthCurrentEntry = _CalixOntEthCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 1, 1)
)
calixOntEthCurrentEntry.setIndexNames(
    (0, "CALIX-ONT-ETH-MIB", "calixOntEthCurrentIndex"),
)
if mibBuilder.loadTexts:
    calixOntEthCurrentEntry.setStatus("current")
_CalixOntEthCurrentIndex_Type = InterfaceIndex
_CalixOntEthCurrentIndex_Object = MibTableColumn
calixOntEthCurrentIndex = _CalixOntEthCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 1, 1, 1),
    _CalixOntEthCurrentIndex_Type()
)
calixOntEthCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthCurrentIndex.setStatus("current")
_CalixOntEthCurrentAlignErr_Type = PerfCurrentCount
_CalixOntEthCurrentAlignErr_Object = MibTableColumn
calixOntEthCurrentAlignErr = _CalixOntEthCurrentAlignErr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 1, 1, 2),
    _CalixOntEthCurrentAlignErr_Type()
)
calixOntEthCurrentAlignErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthCurrentAlignErr.setStatus("current")
_CalixOntEthCurrentFcsErr_Type = PerfCurrentCount
_CalixOntEthCurrentFcsErr_Object = MibTableColumn
calixOntEthCurrentFcsErr = _CalixOntEthCurrentFcsErr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 1, 1, 3),
    _CalixOntEthCurrentFcsErr_Type()
)
calixOntEthCurrentFcsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthCurrentFcsErr.setStatus("current")
_CalixOntEthCurrentSqeTestErr_Type = PerfCurrentCount
_CalixOntEthCurrentSqeTestErr_Object = MibTableColumn
calixOntEthCurrentSqeTestErr = _CalixOntEthCurrentSqeTestErr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 1, 1, 4),
    _CalixOntEthCurrentSqeTestErr_Type()
)
calixOntEthCurrentSqeTestErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthCurrentSqeTestErr.setStatus("current")
_CalixOntEthCurrentDeferred_Type = PerfCurrentCount
_CalixOntEthCurrentDeferred_Object = MibTableColumn
calixOntEthCurrentDeferred = _CalixOntEthCurrentDeferred_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 1, 1, 5),
    _CalixOntEthCurrentDeferred_Type()
)
calixOntEthCurrentDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthCurrentDeferred.setStatus("current")
_CalixOntEthCurrentLateColl_Type = PerfCurrentCount
_CalixOntEthCurrentLateColl_Object = MibTableColumn
calixOntEthCurrentLateColl = _CalixOntEthCurrentLateColl_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 1, 1, 6),
    _CalixOntEthCurrentLateColl_Type()
)
calixOntEthCurrentLateColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthCurrentLateColl.setStatus("current")
_CalixOntEthCurrentExcessColl_Type = PerfCurrentCount
_CalixOntEthCurrentExcessColl_Object = MibTableColumn
calixOntEthCurrentExcessColl = _CalixOntEthCurrentExcessColl_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 1, 1, 7),
    _CalixOntEthCurrentExcessColl_Type()
)
calixOntEthCurrentExcessColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthCurrentExcessColl.setStatus("current")
_CalixOntEthCurrentFrameTooLongs_Type = PerfCurrentCount
_CalixOntEthCurrentFrameTooLongs_Object = MibTableColumn
calixOntEthCurrentFrameTooLongs = _CalixOntEthCurrentFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 1, 1, 8),
    _CalixOntEthCurrentFrameTooLongs_Type()
)
calixOntEthCurrentFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthCurrentFrameTooLongs.setStatus("current")
_CalixOntEthCurrentRxIntErr_Type = PerfCurrentCount
_CalixOntEthCurrentRxIntErr_Object = MibTableColumn
calixOntEthCurrentRxIntErr = _CalixOntEthCurrentRxIntErr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 1, 1, 9),
    _CalixOntEthCurrentRxIntErr_Type()
)
calixOntEthCurrentRxIntErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthCurrentRxIntErr.setStatus("current")
_CalixOntEthCurrentInBufOvbl_Type = PerfCurrentCount
_CalixOntEthCurrentInBufOvbl_Object = MibTableColumn
calixOntEthCurrentInBufOvbl = _CalixOntEthCurrentInBufOvbl_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 1, 1, 10),
    _CalixOntEthCurrentInBufOvbl_Type()
)
calixOntEthCurrentInBufOvbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthCurrentInBufOvbl.setStatus("current")
_CalixOntEthCurrentOutBufOvbl_Type = PerfCurrentCount
_CalixOntEthCurrentOutBufOvbl_Object = MibTableColumn
calixOntEthCurrentOutBufOvbl = _CalixOntEthCurrentOutBufOvbl_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 1, 1, 11),
    _CalixOntEthCurrentOutBufOvbl_Type()
)
calixOntEthCurrentOutBufOvbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthCurrentOutBufOvbl.setStatus("current")
_CalixOntEthIntervalTable_Object = MibTable
calixOntEthIntervalTable = _CalixOntEthIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    calixOntEthIntervalTable.setStatus("current")
_CalixOntEthIntervalEntry_Object = MibTableRow
calixOntEthIntervalEntry = _CalixOntEthIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 2, 1)
)
calixOntEthIntervalEntry.setIndexNames(
    (0, "CALIX-ONT-ETH-MIB", "calixOntEthIntervalIndex"),
    (0, "CALIX-ONT-ETH-MIB", "calixOntEthIntervalNumber"),
)
if mibBuilder.loadTexts:
    calixOntEthIntervalEntry.setStatus("current")
_CalixOntEthIntervalIndex_Type = InterfaceIndex
_CalixOntEthIntervalIndex_Object = MibTableColumn
calixOntEthIntervalIndex = _CalixOntEthIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 2, 1, 1),
    _CalixOntEthIntervalIndex_Type()
)
calixOntEthIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthIntervalIndex.setStatus("current")


class _CalixOntEthIntervalNumber_Type(Integer32):
    """Custom type calixOntEthIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CalixOntEthIntervalNumber_Type.__name__ = "Integer32"
_CalixOntEthIntervalNumber_Object = MibTableColumn
calixOntEthIntervalNumber = _CalixOntEthIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 2, 1, 2),
    _CalixOntEthIntervalNumber_Type()
)
calixOntEthIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthIntervalNumber.setStatus("current")
_CalixOntEthIntervalAlignErr_Type = PerfIntervalCount
_CalixOntEthIntervalAlignErr_Object = MibTableColumn
calixOntEthIntervalAlignErr = _CalixOntEthIntervalAlignErr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 2, 1, 3),
    _CalixOntEthIntervalAlignErr_Type()
)
calixOntEthIntervalAlignErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthIntervalAlignErr.setStatus("current")
_CalixOntEthIntervalFcsErr_Type = PerfIntervalCount
_CalixOntEthIntervalFcsErr_Object = MibTableColumn
calixOntEthIntervalFcsErr = _CalixOntEthIntervalFcsErr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 2, 1, 4),
    _CalixOntEthIntervalFcsErr_Type()
)
calixOntEthIntervalFcsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthIntervalFcsErr.setStatus("current")
_CalixOntEthIntervalSqeTestErr_Type = PerfIntervalCount
_CalixOntEthIntervalSqeTestErr_Object = MibTableColumn
calixOntEthIntervalSqeTestErr = _CalixOntEthIntervalSqeTestErr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 2, 1, 5),
    _CalixOntEthIntervalSqeTestErr_Type()
)
calixOntEthIntervalSqeTestErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthIntervalSqeTestErr.setStatus("current")
_CalixOntEthIntervalDeferred_Type = PerfIntervalCount
_CalixOntEthIntervalDeferred_Object = MibTableColumn
calixOntEthIntervalDeferred = _CalixOntEthIntervalDeferred_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 2, 1, 6),
    _CalixOntEthIntervalDeferred_Type()
)
calixOntEthIntervalDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthIntervalDeferred.setStatus("current")
_CalixOntEthIntervalLateColl_Type = PerfIntervalCount
_CalixOntEthIntervalLateColl_Object = MibTableColumn
calixOntEthIntervalLateColl = _CalixOntEthIntervalLateColl_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 2, 1, 7),
    _CalixOntEthIntervalLateColl_Type()
)
calixOntEthIntervalLateColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthIntervalLateColl.setStatus("current")
_CalixOntEthIntervalExcessColl_Type = PerfIntervalCount
_CalixOntEthIntervalExcessColl_Object = MibTableColumn
calixOntEthIntervalExcessColl = _CalixOntEthIntervalExcessColl_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 2, 1, 8),
    _CalixOntEthIntervalExcessColl_Type()
)
calixOntEthIntervalExcessColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthIntervalExcessColl.setStatus("current")
_CalixOntEthIntervalFrameTooLongs_Type = PerfIntervalCount
_CalixOntEthIntervalFrameTooLongs_Object = MibTableColumn
calixOntEthIntervalFrameTooLongs = _CalixOntEthIntervalFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 2, 1, 9),
    _CalixOntEthIntervalFrameTooLongs_Type()
)
calixOntEthIntervalFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthIntervalFrameTooLongs.setStatus("current")
_CalixOntEthIntervalRxIntErr_Type = PerfIntervalCount
_CalixOntEthIntervalRxIntErr_Object = MibTableColumn
calixOntEthIntervalRxIntErr = _CalixOntEthIntervalRxIntErr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 2, 1, 10),
    _CalixOntEthIntervalRxIntErr_Type()
)
calixOntEthIntervalRxIntErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthIntervalRxIntErr.setStatus("current")
_CalixOntEthIntervalInBufOvbl_Type = PerfIntervalCount
_CalixOntEthIntervalInBufOvbl_Object = MibTableColumn
calixOntEthIntervalInBufOvbl = _CalixOntEthIntervalInBufOvbl_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 2, 1, 11),
    _CalixOntEthIntervalInBufOvbl_Type()
)
calixOntEthIntervalInBufOvbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthIntervalInBufOvbl.setStatus("current")
_CalixOntEthIntervalOutBufOvbl_Type = PerfIntervalCount
_CalixOntEthIntervalOutBufOvbl_Object = MibTableColumn
calixOntEthIntervalOutBufOvbl = _CalixOntEthIntervalOutBufOvbl_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 2, 1, 12),
    _CalixOntEthIntervalOutBufOvbl_Type()
)
calixOntEthIntervalOutBufOvbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthIntervalOutBufOvbl.setStatus("current")
_CalixOntEthIntervalValidData_Type = TruthValue
_CalixOntEthIntervalValidData_Object = MibTableColumn
calixOntEthIntervalValidData = _CalixOntEthIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 2, 1, 13),
    _CalixOntEthIntervalValidData_Type()
)
calixOntEthIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthIntervalValidData.setStatus("current")
_CalixOntEthTotalTable_Object = MibTable
calixOntEthTotalTable = _CalixOntEthTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 3)
)
if mibBuilder.loadTexts:
    calixOntEthTotalTable.setStatus("current")
_CalixOntEthTotalEntry_Object = MibTableRow
calixOntEthTotalEntry = _CalixOntEthTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 3, 1)
)
calixOntEthTotalEntry.setIndexNames(
    (0, "CALIX-ONT-ETH-MIB", "calixOntEthTotalIndex"),
)
if mibBuilder.loadTexts:
    calixOntEthTotalEntry.setStatus("current")
_CalixOntEthTotalIndex_Type = InterfaceIndex
_CalixOntEthTotalIndex_Object = MibTableColumn
calixOntEthTotalIndex = _CalixOntEthTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 3, 1, 1),
    _CalixOntEthTotalIndex_Type()
)
calixOntEthTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthTotalIndex.setStatus("current")
_CalixOntEthTotalAlignErr_Type = PerfTotalCount
_CalixOntEthTotalAlignErr_Object = MibTableColumn
calixOntEthTotalAlignErr = _CalixOntEthTotalAlignErr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 3, 1, 2),
    _CalixOntEthTotalAlignErr_Type()
)
calixOntEthTotalAlignErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthTotalAlignErr.setStatus("current")
_CalixOntEthTotalFcsErr_Type = PerfTotalCount
_CalixOntEthTotalFcsErr_Object = MibTableColumn
calixOntEthTotalFcsErr = _CalixOntEthTotalFcsErr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 3, 1, 3),
    _CalixOntEthTotalFcsErr_Type()
)
calixOntEthTotalFcsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthTotalFcsErr.setStatus("current")
_CalixOntEthTotalSqeTestErr_Type = PerfTotalCount
_CalixOntEthTotalSqeTestErr_Object = MibTableColumn
calixOntEthTotalSqeTestErr = _CalixOntEthTotalSqeTestErr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 3, 1, 4),
    _CalixOntEthTotalSqeTestErr_Type()
)
calixOntEthTotalSqeTestErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthTotalSqeTestErr.setStatus("current")
_CalixOntEthTotalDeferred_Type = PerfTotalCount
_CalixOntEthTotalDeferred_Object = MibTableColumn
calixOntEthTotalDeferred = _CalixOntEthTotalDeferred_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 3, 1, 5),
    _CalixOntEthTotalDeferred_Type()
)
calixOntEthTotalDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthTotalDeferred.setStatus("current")
_CalixOntEthTotalLateColl_Type = PerfTotalCount
_CalixOntEthTotalLateColl_Object = MibTableColumn
calixOntEthTotalLateColl = _CalixOntEthTotalLateColl_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 3, 1, 6),
    _CalixOntEthTotalLateColl_Type()
)
calixOntEthTotalLateColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthTotalLateColl.setStatus("current")
_CalixOntEthTotalExcessColl_Type = PerfTotalCount
_CalixOntEthTotalExcessColl_Object = MibTableColumn
calixOntEthTotalExcessColl = _CalixOntEthTotalExcessColl_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 3, 1, 7),
    _CalixOntEthTotalExcessColl_Type()
)
calixOntEthTotalExcessColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthTotalExcessColl.setStatus("current")
_CalixOntEthTotalFrameTooLongs_Type = PerfTotalCount
_CalixOntEthTotalFrameTooLongs_Object = MibTableColumn
calixOntEthTotalFrameTooLongs = _CalixOntEthTotalFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 3, 1, 8),
    _CalixOntEthTotalFrameTooLongs_Type()
)
calixOntEthTotalFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthTotalFrameTooLongs.setStatus("current")
_CalixOntEthTotalRxIntErr_Type = PerfTotalCount
_CalixOntEthTotalRxIntErr_Object = MibTableColumn
calixOntEthTotalRxIntErr = _CalixOntEthTotalRxIntErr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 3, 1, 9),
    _CalixOntEthTotalRxIntErr_Type()
)
calixOntEthTotalRxIntErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthTotalRxIntErr.setStatus("current")
_CalixOntEthTotalInBufOvbl_Type = PerfTotalCount
_CalixOntEthTotalInBufOvbl_Object = MibTableColumn
calixOntEthTotalInBufOvbl = _CalixOntEthTotalInBufOvbl_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 3, 1, 10),
    _CalixOntEthTotalInBufOvbl_Type()
)
calixOntEthTotalInBufOvbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthTotalInBufOvbl.setStatus("current")
_CalixOntEthTotalOutBufOvbl_Type = PerfTotalCount
_CalixOntEthTotalOutBufOvbl_Object = MibTableColumn
calixOntEthTotalOutBufOvbl = _CalixOntEthTotalOutBufOvbl_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 7, 3, 1, 11),
    _CalixOntEthTotalOutBufOvbl_Type()
)
calixOntEthTotalOutBufOvbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOntEthTotalOutBufOvbl.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CALIX-ONT-ETH-MIB",
    **{"calixOntEth": calixOntEth,
       "calixOntEthCurrentTable": calixOntEthCurrentTable,
       "calixOntEthCurrentEntry": calixOntEthCurrentEntry,
       "calixOntEthCurrentIndex": calixOntEthCurrentIndex,
       "calixOntEthCurrentAlignErr": calixOntEthCurrentAlignErr,
       "calixOntEthCurrentFcsErr": calixOntEthCurrentFcsErr,
       "calixOntEthCurrentSqeTestErr": calixOntEthCurrentSqeTestErr,
       "calixOntEthCurrentDeferred": calixOntEthCurrentDeferred,
       "calixOntEthCurrentLateColl": calixOntEthCurrentLateColl,
       "calixOntEthCurrentExcessColl": calixOntEthCurrentExcessColl,
       "calixOntEthCurrentFrameTooLongs": calixOntEthCurrentFrameTooLongs,
       "calixOntEthCurrentRxIntErr": calixOntEthCurrentRxIntErr,
       "calixOntEthCurrentInBufOvbl": calixOntEthCurrentInBufOvbl,
       "calixOntEthCurrentOutBufOvbl": calixOntEthCurrentOutBufOvbl,
       "calixOntEthIntervalTable": calixOntEthIntervalTable,
       "calixOntEthIntervalEntry": calixOntEthIntervalEntry,
       "calixOntEthIntervalIndex": calixOntEthIntervalIndex,
       "calixOntEthIntervalNumber": calixOntEthIntervalNumber,
       "calixOntEthIntervalAlignErr": calixOntEthIntervalAlignErr,
       "calixOntEthIntervalFcsErr": calixOntEthIntervalFcsErr,
       "calixOntEthIntervalSqeTestErr": calixOntEthIntervalSqeTestErr,
       "calixOntEthIntervalDeferred": calixOntEthIntervalDeferred,
       "calixOntEthIntervalLateColl": calixOntEthIntervalLateColl,
       "calixOntEthIntervalExcessColl": calixOntEthIntervalExcessColl,
       "calixOntEthIntervalFrameTooLongs": calixOntEthIntervalFrameTooLongs,
       "calixOntEthIntervalRxIntErr": calixOntEthIntervalRxIntErr,
       "calixOntEthIntervalInBufOvbl": calixOntEthIntervalInBufOvbl,
       "calixOntEthIntervalOutBufOvbl": calixOntEthIntervalOutBufOvbl,
       "calixOntEthIntervalValidData": calixOntEthIntervalValidData,
       "calixOntEthTotalTable": calixOntEthTotalTable,
       "calixOntEthTotalEntry": calixOntEthTotalEntry,
       "calixOntEthTotalIndex": calixOntEthTotalIndex,
       "calixOntEthTotalAlignErr": calixOntEthTotalAlignErr,
       "calixOntEthTotalFcsErr": calixOntEthTotalFcsErr,
       "calixOntEthTotalSqeTestErr": calixOntEthTotalSqeTestErr,
       "calixOntEthTotalDeferred": calixOntEthTotalDeferred,
       "calixOntEthTotalLateColl": calixOntEthTotalLateColl,
       "calixOntEthTotalExcessColl": calixOntEthTotalExcessColl,
       "calixOntEthTotalFrameTooLongs": calixOntEthTotalFrameTooLongs,
       "calixOntEthTotalRxIntErr": calixOntEthTotalRxIntErr,
       "calixOntEthTotalInBufOvbl": calixOntEthTotalInBufOvbl,
       "calixOntEthTotalOutBufOvbl": calixOntEthTotalOutBufOvbl}
)
