# SNMP MIB module (AOS-CORE-FACILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/AOS-CORE-FACILITY-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:56 2025
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

(aosCommon,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "aosCommon")

(PmSuspectReasonType,) = mibBuilder.importSymbols(
    "AOS-COMMON-PM-MIB",
    "PmSuspectReasonType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

aosCoreFacilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3)
)
if mibBuilder.loadTexts:
    aosCoreFacilityMIB.setRevisions(
        ("2016-06-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AosCoreFacilityObjects_ObjectIdentity = ObjectIdentity
aosCoreFacilityObjects = _AosCoreFacilityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 1)
)
_AosCoreFacilityStatsObjects_ObjectIdentity = ObjectIdentity
aosCoreFacilityStatsObjects = _AosCoreFacilityStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2)
)
_AosCoreFacCurrOpticalPowerTable_Object = MibTable
aosCoreFacCurrOpticalPowerTable = _AosCoreFacCurrOpticalPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    aosCoreFacCurrOpticalPowerTable.setStatus("current")
_AosCoreFacCurrOpticalPowerEntry_Object = MibTableRow
aosCoreFacCurrOpticalPowerEntry = _AosCoreFacCurrOpticalPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 1, 1)
)
aosCoreFacCurrOpticalPowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aosCoreFacCurrOpticalPowerEntry.setStatus("current")
_AosCoreFacCurrOpticalPowerRx_Type = Integer32
_AosCoreFacCurrOpticalPowerRx_Object = MibTableColumn
aosCoreFacCurrOpticalPowerRx = _AosCoreFacCurrOpticalPowerRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 1, 1, 1),
    _AosCoreFacCurrOpticalPowerRx_Type()
)
aosCoreFacCurrOpticalPowerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacCurrOpticalPowerRx.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacCurrOpticalPowerRx.setUnits("0.1 dbm")
_AosCoreFacCurrOpticalPowerTx_Type = Integer32
_AosCoreFacCurrOpticalPowerTx_Object = MibTableColumn
aosCoreFacCurrOpticalPowerTx = _AosCoreFacCurrOpticalPowerTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 1, 1, 2),
    _AosCoreFacCurrOpticalPowerTx_Type()
)
aosCoreFacCurrOpticalPowerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacCurrOpticalPowerTx.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacCurrOpticalPowerTx.setUnits("0.1 dbm")
_AosCoreFacCurrOpticalPowerSuspectReason_Type = PmSuspectReasonType
_AosCoreFacCurrOpticalPowerSuspectReason_Object = MibTableColumn
aosCoreFacCurrOpticalPowerSuspectReason = _AosCoreFacCurrOpticalPowerSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 1, 1, 3),
    _AosCoreFacCurrOpticalPowerSuspectReason_Type()
)
aosCoreFacCurrOpticalPowerSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacCurrOpticalPowerSuspectReason.setStatus("current")
_AosCoreFacHist15MinOpticalPowerTable_Object = MibTable
aosCoreFacHist15MinOpticalPowerTable = _AosCoreFacHist15MinOpticalPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    aosCoreFacHist15MinOpticalPowerTable.setStatus("current")
_AosCoreFacHist15MinOpticalPowerEntry_Object = MibTableRow
aosCoreFacHist15MinOpticalPowerEntry = _AosCoreFacHist15MinOpticalPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 2, 1)
)
aosCoreFacHist15MinOpticalPowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinOpticalPowerSample"),
)
if mibBuilder.loadTexts:
    aosCoreFacHist15MinOpticalPowerEntry.setStatus("current")


class _AosCoreFacHist15MinOpticalPowerSample_Type(Integer32):
    """Custom type aosCoreFacHist15MinOpticalPowerSample based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AosCoreFacHist15MinOpticalPowerSample_Type.__name__ = "Integer32"
_AosCoreFacHist15MinOpticalPowerSample_Object = MibTableColumn
aosCoreFacHist15MinOpticalPowerSample = _AosCoreFacHist15MinOpticalPowerSample_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 2, 1, 1),
    _AosCoreFacHist15MinOpticalPowerSample_Type()
)
aosCoreFacHist15MinOpticalPowerSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinOpticalPowerSample.setStatus("current")
_AosCoreFacHist15MinOpticalPowerSampleTime_Type = TimeTicks
_AosCoreFacHist15MinOpticalPowerSampleTime_Object = MibTableColumn
aosCoreFacHist15MinOpticalPowerSampleTime = _AosCoreFacHist15MinOpticalPowerSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 2, 1, 2),
    _AosCoreFacHist15MinOpticalPowerSampleTime_Type()
)
aosCoreFacHist15MinOpticalPowerSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinOpticalPowerSampleTime.setStatus("current")
_AosCoreFacHist15MinOpticalPowerRxLow_Type = Integer32
_AosCoreFacHist15MinOpticalPowerRxLow_Object = MibTableColumn
aosCoreFacHist15MinOpticalPowerRxLow = _AosCoreFacHist15MinOpticalPowerRxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 2, 1, 3),
    _AosCoreFacHist15MinOpticalPowerRxLow_Type()
)
aosCoreFacHist15MinOpticalPowerRxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinOpticalPowerRxLow.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinOpticalPowerRxLow.setUnits("0.1 dbm")
_AosCoreFacHist15MinOpticalPowerRxMed_Type = Integer32
_AosCoreFacHist15MinOpticalPowerRxMed_Object = MibTableColumn
aosCoreFacHist15MinOpticalPowerRxMed = _AosCoreFacHist15MinOpticalPowerRxMed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 2, 1, 4),
    _AosCoreFacHist15MinOpticalPowerRxMed_Type()
)
aosCoreFacHist15MinOpticalPowerRxMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinOpticalPowerRxMed.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinOpticalPowerRxMed.setUnits("0.1 dbm")
_AosCoreFacHist15MinOpticalPowerRxHi_Type = Integer32
_AosCoreFacHist15MinOpticalPowerRxHi_Object = MibTableColumn
aosCoreFacHist15MinOpticalPowerRxHi = _AosCoreFacHist15MinOpticalPowerRxHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 2, 1, 5),
    _AosCoreFacHist15MinOpticalPowerRxHi_Type()
)
aosCoreFacHist15MinOpticalPowerRxHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinOpticalPowerRxHi.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinOpticalPowerRxHi.setUnits("0.1 dbm")
_AosCoreFacHist15MinOpticalPowerTxLow_Type = Integer32
_AosCoreFacHist15MinOpticalPowerTxLow_Object = MibTableColumn
aosCoreFacHist15MinOpticalPowerTxLow = _AosCoreFacHist15MinOpticalPowerTxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 2, 1, 6),
    _AosCoreFacHist15MinOpticalPowerTxLow_Type()
)
aosCoreFacHist15MinOpticalPowerTxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinOpticalPowerTxLow.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinOpticalPowerTxLow.setUnits("0.1 dbm")
_AosCoreFacHist15MinOpticalPowerTxMed_Type = Integer32
_AosCoreFacHist15MinOpticalPowerTxMed_Object = MibTableColumn
aosCoreFacHist15MinOpticalPowerTxMed = _AosCoreFacHist15MinOpticalPowerTxMed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 2, 1, 7),
    _AosCoreFacHist15MinOpticalPowerTxMed_Type()
)
aosCoreFacHist15MinOpticalPowerTxMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinOpticalPowerTxMed.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinOpticalPowerTxMed.setUnits("0.1 dbm")
_AosCoreFacHist15MinOpticalPowerTxHi_Type = Integer32
_AosCoreFacHist15MinOpticalPowerTxHi_Object = MibTableColumn
aosCoreFacHist15MinOpticalPowerTxHi = _AosCoreFacHist15MinOpticalPowerTxHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 2, 1, 8),
    _AosCoreFacHist15MinOpticalPowerTxHi_Type()
)
aosCoreFacHist15MinOpticalPowerTxHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinOpticalPowerTxHi.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinOpticalPowerTxHi.setUnits("0.1 dbm")
_AosCoreFacHist15MinOpticalPowerSuspectReason_Type = PmSuspectReasonType
_AosCoreFacHist15MinOpticalPowerSuspectReason_Object = MibTableColumn
aosCoreFacHist15MinOpticalPowerSuspectReason = _AosCoreFacHist15MinOpticalPowerSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 2, 1, 9),
    _AosCoreFacHist15MinOpticalPowerSuspectReason_Type()
)
aosCoreFacHist15MinOpticalPowerSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinOpticalPowerSuspectReason.setStatus("current")
_AosCoreFacHist1DayOpticalPowerTable_Object = MibTable
aosCoreFacHist1DayOpticalPowerTable = _AosCoreFacHist1DayOpticalPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    aosCoreFacHist1DayOpticalPowerTable.setStatus("current")
_AosCoreFacHist1DayOpticalPowerEntry_Object = MibTableRow
aosCoreFacHist1DayOpticalPowerEntry = _AosCoreFacHist1DayOpticalPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 3, 1)
)
aosCoreFacHist1DayOpticalPowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DayOpticalPowerSample"),
)
if mibBuilder.loadTexts:
    aosCoreFacHist1DayOpticalPowerEntry.setStatus("current")


class _AosCoreFacHist1DayOpticalPowerSample_Type(Integer32):
    """Custom type aosCoreFacHist1DayOpticalPowerSample based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AosCoreFacHist1DayOpticalPowerSample_Type.__name__ = "Integer32"
_AosCoreFacHist1DayOpticalPowerSample_Object = MibTableColumn
aosCoreFacHist1DayOpticalPowerSample = _AosCoreFacHist1DayOpticalPowerSample_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 3, 1, 1),
    _AosCoreFacHist1DayOpticalPowerSample_Type()
)
aosCoreFacHist1DayOpticalPowerSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayOpticalPowerSample.setStatus("current")
_AosCoreFacHist1DayOpticalPowerSampleTime_Type = TimeTicks
_AosCoreFacHist1DayOpticalPowerSampleTime_Object = MibTableColumn
aosCoreFacHist1DayOpticalPowerSampleTime = _AosCoreFacHist1DayOpticalPowerSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 3, 1, 2),
    _AosCoreFacHist1DayOpticalPowerSampleTime_Type()
)
aosCoreFacHist1DayOpticalPowerSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayOpticalPowerSampleTime.setStatus("current")
_AosCoreFacHist1DayOpticalPowerRxLow_Type = Integer32
_AosCoreFacHist1DayOpticalPowerRxLow_Object = MibTableColumn
aosCoreFacHist1DayOpticalPowerRxLow = _AosCoreFacHist1DayOpticalPowerRxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 3, 1, 3),
    _AosCoreFacHist1DayOpticalPowerRxLow_Type()
)
aosCoreFacHist1DayOpticalPowerRxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayOpticalPowerRxLow.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayOpticalPowerRxLow.setUnits("0.1 dbm")
_AosCoreFacHist1DayOpticalPowerRxMed_Type = Integer32
_AosCoreFacHist1DayOpticalPowerRxMed_Object = MibTableColumn
aosCoreFacHist1DayOpticalPowerRxMed = _AosCoreFacHist1DayOpticalPowerRxMed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 3, 1, 4),
    _AosCoreFacHist1DayOpticalPowerRxMed_Type()
)
aosCoreFacHist1DayOpticalPowerRxMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayOpticalPowerRxMed.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayOpticalPowerRxMed.setUnits("0.1 dbm")
_AosCoreFacHist1DayOpticalPowerRxHi_Type = Integer32
_AosCoreFacHist1DayOpticalPowerRxHi_Object = MibTableColumn
aosCoreFacHist1DayOpticalPowerRxHi = _AosCoreFacHist1DayOpticalPowerRxHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 3, 1, 5),
    _AosCoreFacHist1DayOpticalPowerRxHi_Type()
)
aosCoreFacHist1DayOpticalPowerRxHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayOpticalPowerRxHi.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayOpticalPowerRxHi.setUnits("0.1 dbm")
_AosCoreFacHist1DayOpticalPowerTxLow_Type = Integer32
_AosCoreFacHist1DayOpticalPowerTxLow_Object = MibTableColumn
aosCoreFacHist1DayOpticalPowerTxLow = _AosCoreFacHist1DayOpticalPowerTxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 3, 1, 6),
    _AosCoreFacHist1DayOpticalPowerTxLow_Type()
)
aosCoreFacHist1DayOpticalPowerTxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayOpticalPowerTxLow.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayOpticalPowerTxLow.setUnits("0.1 dbm")
_AosCoreFacHist1DayOpticalPowerTxMed_Type = Integer32
_AosCoreFacHist1DayOpticalPowerTxMed_Object = MibTableColumn
aosCoreFacHist1DayOpticalPowerTxMed = _AosCoreFacHist1DayOpticalPowerTxMed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 3, 1, 7),
    _AosCoreFacHist1DayOpticalPowerTxMed_Type()
)
aosCoreFacHist1DayOpticalPowerTxMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayOpticalPowerTxMed.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayOpticalPowerTxMed.setUnits("0.1 dbm")
_AosCoreFacHist1DayOpticalPowerTxHi_Type = Integer32
_AosCoreFacHist1DayOpticalPowerTxHi_Object = MibTableColumn
aosCoreFacHist1DayOpticalPowerTxHi = _AosCoreFacHist1DayOpticalPowerTxHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 3, 1, 8),
    _AosCoreFacHist1DayOpticalPowerTxHi_Type()
)
aosCoreFacHist1DayOpticalPowerTxHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayOpticalPowerTxHi.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayOpticalPowerTxHi.setUnits("0.1 dbm")
_AosCoreFacHist1DayOpticalPowerSuspectReason_Type = PmSuspectReasonType
_AosCoreFacHist1DayOpticalPowerSuspectReason_Object = MibTableColumn
aosCoreFacHist1DayOpticalPowerSuspectReason = _AosCoreFacHist1DayOpticalPowerSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 3, 1, 9),
    _AosCoreFacHist1DayOpticalPowerSuspectReason_Type()
)
aosCoreFacHist1DayOpticalPowerSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayOpticalPowerSuspectReason.setStatus("current")
_AosCoreFacCurrFecTable_Object = MibTable
aosCoreFacCurrFecTable = _AosCoreFacCurrFecTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    aosCoreFacCurrFecTable.setStatus("current")
_AosCoreFacCurrFecEntry_Object = MibTableRow
aosCoreFacCurrFecEntry = _AosCoreFacCurrFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 4, 1)
)
aosCoreFacCurrFecEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aosCoreFacCurrFecEntry.setStatus("current")
_AosCoreFacCurrFecCorrectedErrors_Type = Counter64
_AosCoreFacCurrFecCorrectedErrors_Object = MibTableColumn
aosCoreFacCurrFecCorrectedErrors = _AosCoreFacCurrFecCorrectedErrors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 4, 1, 1),
    _AosCoreFacCurrFecCorrectedErrors_Type()
)
aosCoreFacCurrFecCorrectedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacCurrFecCorrectedErrors.setStatus("current")
_AosCoreFacCurrFecUncorrectedBlocks_Type = Counter64
_AosCoreFacCurrFecUncorrectedBlocks_Object = MibTableColumn
aosCoreFacCurrFecUncorrectedBlocks = _AosCoreFacCurrFecUncorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 4, 1, 2),
    _AosCoreFacCurrFecUncorrectedBlocks_Type()
)
aosCoreFacCurrFecUncorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacCurrFecUncorrectedBlocks.setStatus("current")
_AosCoreFacCurrFecBitErrorRate_Type = Counter64
_AosCoreFacCurrFecBitErrorRate_Object = MibTableColumn
aosCoreFacCurrFecBitErrorRate = _AosCoreFacCurrFecBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 4, 1, 3),
    _AosCoreFacCurrFecBitErrorRate_Type()
)
aosCoreFacCurrFecBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacCurrFecBitErrorRate.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacCurrFecBitErrorRate.setUnits("1e-18")
_AosCoreFacCurrFecSuspectReason_Type = PmSuspectReasonType
_AosCoreFacCurrFecSuspectReason_Object = MibTableColumn
aosCoreFacCurrFecSuspectReason = _AosCoreFacCurrFecSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 4, 1, 4),
    _AosCoreFacCurrFecSuspectReason_Type()
)
aosCoreFacCurrFecSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacCurrFecSuspectReason.setStatus("current")
_AosCoreFacHist15MinFecTable_Object = MibTable
aosCoreFacHist15MinFecTable = _AosCoreFacHist15MinFecTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    aosCoreFacHist15MinFecTable.setStatus("current")
_AosCoreFacHist15MinFecEntry_Object = MibTableRow
aosCoreFacHist15MinFecEntry = _AosCoreFacHist15MinFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 5, 1)
)
aosCoreFacHist15MinFecEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinFecSample"),
)
if mibBuilder.loadTexts:
    aosCoreFacHist15MinFecEntry.setStatus("current")


class _AosCoreFacHist15MinFecSample_Type(Integer32):
    """Custom type aosCoreFacHist15MinFecSample based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AosCoreFacHist15MinFecSample_Type.__name__ = "Integer32"
_AosCoreFacHist15MinFecSample_Object = MibTableColumn
aosCoreFacHist15MinFecSample = _AosCoreFacHist15MinFecSample_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 5, 1, 1),
    _AosCoreFacHist15MinFecSample_Type()
)
aosCoreFacHist15MinFecSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinFecSample.setStatus("current")
_AosCoreFacHist15MinFecSampleTime_Type = TimeTicks
_AosCoreFacHist15MinFecSampleTime_Object = MibTableColumn
aosCoreFacHist15MinFecSampleTime = _AosCoreFacHist15MinFecSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 5, 1, 2),
    _AosCoreFacHist15MinFecSampleTime_Type()
)
aosCoreFacHist15MinFecSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinFecSampleTime.setStatus("current")
_AosCoreFacHist15MinFecCorrectedErrors_Type = Counter64
_AosCoreFacHist15MinFecCorrectedErrors_Object = MibTableColumn
aosCoreFacHist15MinFecCorrectedErrors = _AosCoreFacHist15MinFecCorrectedErrors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 5, 1, 3),
    _AosCoreFacHist15MinFecCorrectedErrors_Type()
)
aosCoreFacHist15MinFecCorrectedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinFecCorrectedErrors.setStatus("current")
_AosCoreFacHist15MinFecUncorrectedBlocks_Type = Counter64
_AosCoreFacHist15MinFecUncorrectedBlocks_Object = MibTableColumn
aosCoreFacHist15MinFecUncorrectedBlocks = _AosCoreFacHist15MinFecUncorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 5, 1, 4),
    _AosCoreFacHist15MinFecUncorrectedBlocks_Type()
)
aosCoreFacHist15MinFecUncorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinFecUncorrectedBlocks.setStatus("current")
_AosCoreFacHist15MinFecBitErrorRate_Type = Counter64
_AosCoreFacHist15MinFecBitErrorRate_Object = MibTableColumn
aosCoreFacHist15MinFecBitErrorRate = _AosCoreFacHist15MinFecBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 5, 1, 5),
    _AosCoreFacHist15MinFecBitErrorRate_Type()
)
aosCoreFacHist15MinFecBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinFecBitErrorRate.setStatus("current")
_AosCoreFacHist15MinFecSuspectReason_Type = PmSuspectReasonType
_AosCoreFacHist15MinFecSuspectReason_Object = MibTableColumn
aosCoreFacHist15MinFecSuspectReason = _AosCoreFacHist15MinFecSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 5, 1, 6),
    _AosCoreFacHist15MinFecSuspectReason_Type()
)
aosCoreFacHist15MinFecSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinFecSuspectReason.setStatus("current")
_AosCoreFacHist1DayFecTable_Object = MibTable
aosCoreFacHist1DayFecTable = _AosCoreFacHist1DayFecTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 6)
)
if mibBuilder.loadTexts:
    aosCoreFacHist1DayFecTable.setStatus("current")
_AosCoreFacHist1DayFecEntry_Object = MibTableRow
aosCoreFacHist1DayFecEntry = _AosCoreFacHist1DayFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 6, 1)
)
aosCoreFacHist1DayFecEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DayFecSample"),
)
if mibBuilder.loadTexts:
    aosCoreFacHist1DayFecEntry.setStatus("current")


class _AosCoreFacHist1DayFecSample_Type(Integer32):
    """Custom type aosCoreFacHist1DayFecSample based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AosCoreFacHist1DayFecSample_Type.__name__ = "Integer32"
_AosCoreFacHist1DayFecSample_Object = MibTableColumn
aosCoreFacHist1DayFecSample = _AosCoreFacHist1DayFecSample_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 6, 1, 1),
    _AosCoreFacHist1DayFecSample_Type()
)
aosCoreFacHist1DayFecSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayFecSample.setStatus("current")
_AosCoreFacHist1DayFecSampleTime_Type = TimeTicks
_AosCoreFacHist1DayFecSampleTime_Object = MibTableColumn
aosCoreFacHist1DayFecSampleTime = _AosCoreFacHist1DayFecSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 6, 1, 2),
    _AosCoreFacHist1DayFecSampleTime_Type()
)
aosCoreFacHist1DayFecSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayFecSampleTime.setStatus("current")
_AosCoreFacHist1DayFecCorrectedErrors_Type = Counter64
_AosCoreFacHist1DayFecCorrectedErrors_Object = MibTableColumn
aosCoreFacHist1DayFecCorrectedErrors = _AosCoreFacHist1DayFecCorrectedErrors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 6, 1, 3),
    _AosCoreFacHist1DayFecCorrectedErrors_Type()
)
aosCoreFacHist1DayFecCorrectedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayFecCorrectedErrors.setStatus("current")
_AosCoreFacHist1DayFecUncorrectedBlocks_Type = Counter64
_AosCoreFacHist1DayFecUncorrectedBlocks_Object = MibTableColumn
aosCoreFacHist1DayFecUncorrectedBlocks = _AosCoreFacHist1DayFecUncorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 6, 1, 4),
    _AosCoreFacHist1DayFecUncorrectedBlocks_Type()
)
aosCoreFacHist1DayFecUncorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayFecUncorrectedBlocks.setStatus("current")
_AosCoreFacHist1DayFecBitErrorRate_Type = Counter64
_AosCoreFacHist1DayFecBitErrorRate_Object = MibTableColumn
aosCoreFacHist1DayFecBitErrorRate = _AosCoreFacHist1DayFecBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 6, 1, 5),
    _AosCoreFacHist1DayFecBitErrorRate_Type()
)
aosCoreFacHist1DayFecBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayFecBitErrorRate.setStatus("current")
_AosCoreFacHist1DayFecSuspectReason_Type = PmSuspectReasonType
_AosCoreFacHist1DayFecSuspectReason_Object = MibTableColumn
aosCoreFacHist1DayFecSuspectReason = _AosCoreFacHist1DayFecSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 6, 1, 6),
    _AosCoreFacHist1DayFecSuspectReason_Type()
)
aosCoreFacHist1DayFecSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DayFecSuspectReason.setStatus("current")
_AosCoreFacCurrSnrTable_Object = MibTable
aosCoreFacCurrSnrTable = _AosCoreFacCurrSnrTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 7)
)
if mibBuilder.loadTexts:
    aosCoreFacCurrSnrTable.setStatus("current")
_AosCoreFacCurrSnrEntry_Object = MibTableRow
aosCoreFacCurrSnrEntry = _AosCoreFacCurrSnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 7, 1)
)
aosCoreFacCurrSnrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aosCoreFacCurrSnrEntry.setStatus("current")
_AosCoreFacCurrSnrValue_Type = Counter64
_AosCoreFacCurrSnrValue_Object = MibTableColumn
aosCoreFacCurrSnrValue = _AosCoreFacCurrSnrValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 7, 1, 1),
    _AosCoreFacCurrSnrValue_Type()
)
aosCoreFacCurrSnrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacCurrSnrValue.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacCurrSnrValue.setUnits("10 dB")
_AosCoreFacCurrSnrSuspectReason_Type = PmSuspectReasonType
_AosCoreFacCurrSnrSuspectReason_Object = MibTableColumn
aosCoreFacCurrSnrSuspectReason = _AosCoreFacCurrSnrSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 7, 1, 2),
    _AosCoreFacCurrSnrSuspectReason_Type()
)
aosCoreFacCurrSnrSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacCurrSnrSuspectReason.setStatus("current")
_AosCoreFacHist15MinSnrTable_Object = MibTable
aosCoreFacHist15MinSnrTable = _AosCoreFacHist15MinSnrTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 8)
)
if mibBuilder.loadTexts:
    aosCoreFacHist15MinSnrTable.setStatus("current")
_AosCoreFacHist15MinSnrEntry_Object = MibTableRow
aosCoreFacHist15MinSnrEntry = _AosCoreFacHist15MinSnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 8, 1)
)
aosCoreFacHist15MinSnrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinSnrSample"),
)
if mibBuilder.loadTexts:
    aosCoreFacHist15MinSnrEntry.setStatus("current")


class _AosCoreFacHist15MinSnrSample_Type(Integer32):
    """Custom type aosCoreFacHist15MinSnrSample based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AosCoreFacHist15MinSnrSample_Type.__name__ = "Integer32"
_AosCoreFacHist15MinSnrSample_Object = MibTableColumn
aosCoreFacHist15MinSnrSample = _AosCoreFacHist15MinSnrSample_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 8, 1, 1),
    _AosCoreFacHist15MinSnrSample_Type()
)
aosCoreFacHist15MinSnrSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinSnrSample.setStatus("current")
_AosCoreFacHist15MinSnrSampleTime_Type = TimeTicks
_AosCoreFacHist15MinSnrSampleTime_Object = MibTableColumn
aosCoreFacHist15MinSnrSampleTime = _AosCoreFacHist15MinSnrSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 8, 1, 2),
    _AosCoreFacHist15MinSnrSampleTime_Type()
)
aosCoreFacHist15MinSnrSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinSnrSampleTime.setStatus("current")
_AosCoreFacHist15MinSnrValueLow_Type = Counter64
_AosCoreFacHist15MinSnrValueLow_Object = MibTableColumn
aosCoreFacHist15MinSnrValueLow = _AosCoreFacHist15MinSnrValueLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 8, 1, 3),
    _AosCoreFacHist15MinSnrValueLow_Type()
)
aosCoreFacHist15MinSnrValueLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinSnrValueLow.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinSnrValueLow.setUnits("10 dB")
_AosCoreFacHist15MinSnrValueMean_Type = Counter64
_AosCoreFacHist15MinSnrValueMean_Object = MibTableColumn
aosCoreFacHist15MinSnrValueMean = _AosCoreFacHist15MinSnrValueMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 8, 1, 4),
    _AosCoreFacHist15MinSnrValueMean_Type()
)
aosCoreFacHist15MinSnrValueMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinSnrValueMean.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinSnrValueMean.setUnits("10 dB")
_AosCoreFacHist15MinSnrValueHigh_Type = Counter64
_AosCoreFacHist15MinSnrValueHigh_Object = MibTableColumn
aosCoreFacHist15MinSnrValueHigh = _AosCoreFacHist15MinSnrValueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 8, 1, 5),
    _AosCoreFacHist15MinSnrValueHigh_Type()
)
aosCoreFacHist15MinSnrValueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinSnrValueHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinSnrValueHigh.setUnits("10 dB")
_AosCoreFacHist15MinSnrSuspectReason_Type = PmSuspectReasonType
_AosCoreFacHist15MinSnrSuspectReason_Object = MibTableColumn
aosCoreFacHist15MinSnrSuspectReason = _AosCoreFacHist15MinSnrSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 8, 1, 6),
    _AosCoreFacHist15MinSnrSuspectReason_Type()
)
aosCoreFacHist15MinSnrSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist15MinSnrSuspectReason.setStatus("current")
_AosCoreFacHist1DaySnrTable_Object = MibTable
aosCoreFacHist1DaySnrTable = _AosCoreFacHist1DaySnrTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 9)
)
if mibBuilder.loadTexts:
    aosCoreFacHist1DaySnrTable.setStatus("current")
_AosCoreFacHist1DaySnrEntry_Object = MibTableRow
aosCoreFacHist1DaySnrEntry = _AosCoreFacHist1DaySnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 9, 1)
)
aosCoreFacHist1DaySnrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DaySnrSample"),
)
if mibBuilder.loadTexts:
    aosCoreFacHist1DaySnrEntry.setStatus("current")


class _AosCoreFacHist1DaySnrSample_Type(Integer32):
    """Custom type aosCoreFacHist1DaySnrSample based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AosCoreFacHist1DaySnrSample_Type.__name__ = "Integer32"
_AosCoreFacHist1DaySnrSample_Object = MibTableColumn
aosCoreFacHist1DaySnrSample = _AosCoreFacHist1DaySnrSample_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 9, 1, 1),
    _AosCoreFacHist1DaySnrSample_Type()
)
aosCoreFacHist1DaySnrSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DaySnrSample.setStatus("current")
_AosCoreFacHist1DaySnrSampleTime_Type = TimeTicks
_AosCoreFacHist1DaySnrSampleTime_Object = MibTableColumn
aosCoreFacHist1DaySnrSampleTime = _AosCoreFacHist1DaySnrSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 9, 1, 2),
    _AosCoreFacHist1DaySnrSampleTime_Type()
)
aosCoreFacHist1DaySnrSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DaySnrSampleTime.setStatus("current")
_AosCoreFacHist1DaySnrValueLow_Type = Counter64
_AosCoreFacHist1DaySnrValueLow_Object = MibTableColumn
aosCoreFacHist1DaySnrValueLow = _AosCoreFacHist1DaySnrValueLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 9, 1, 3),
    _AosCoreFacHist1DaySnrValueLow_Type()
)
aosCoreFacHist1DaySnrValueLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DaySnrValueLow.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacHist1DaySnrValueLow.setUnits("10 dB")
_AosCoreFacHist1DaySnrValueMean_Type = Counter64
_AosCoreFacHist1DaySnrValueMean_Object = MibTableColumn
aosCoreFacHist1DaySnrValueMean = _AosCoreFacHist1DaySnrValueMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 9, 1, 4),
    _AosCoreFacHist1DaySnrValueMean_Type()
)
aosCoreFacHist1DaySnrValueMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DaySnrValueMean.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacHist1DaySnrValueMean.setUnits("10 dB")
_AosCoreFacHist1DaySnrValueHigh_Type = Counter64
_AosCoreFacHist1DaySnrValueHigh_Object = MibTableColumn
aosCoreFacHist1DaySnrValueHigh = _AosCoreFacHist1DaySnrValueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 9, 1, 5),
    _AosCoreFacHist1DaySnrValueHigh_Type()
)
aosCoreFacHist1DaySnrValueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DaySnrValueHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosCoreFacHist1DaySnrValueHigh.setUnits("10 dB")
_AosCoreFacHist1DaySnrSuspectReason_Type = PmSuspectReasonType
_AosCoreFacHist1DaySnrSuspectReason_Object = MibTableColumn
aosCoreFacHist1DaySnrSuspectReason = _AosCoreFacHist1DaySnrSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 2, 9, 1, 6),
    _AosCoreFacHist1DaySnrSuspectReason_Type()
)
aosCoreFacHist1DaySnrSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreFacHist1DaySnrSuspectReason.setStatus("current")
_AosCoreFacilityConformance_ObjectIdentity = ObjectIdentity
aosCoreFacilityConformance = _AosCoreFacilityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 3)
)
_AosCoreFacilityCompliances_ObjectIdentity = ObjectIdentity
aosCoreFacilityCompliances = _AosCoreFacilityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 3, 1)
)
_AosCoreFacilityGroups_ObjectIdentity = ObjectIdentity
aosCoreFacilityGroups = _AosCoreFacilityGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 3, 2)
)

# Managed Objects groups

aosCoreFacilityStatsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 3, 2, 1)
)
aosCoreFacilityStatsObjectGroup.setObjects(
      *(("AOS-CORE-FACILITY-MIB", "aosCoreFacCurrOpticalPowerRx"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacCurrOpticalPowerTx"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacCurrOpticalPowerSuspectReason"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinOpticalPowerSample"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinOpticalPowerSampleTime"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinOpticalPowerRxLow"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinOpticalPowerRxMed"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinOpticalPowerRxHi"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinOpticalPowerTxLow"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinOpticalPowerTxMed"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinOpticalPowerTxHi"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinOpticalPowerSuspectReason"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DayOpticalPowerSample"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DayOpticalPowerSampleTime"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DayOpticalPowerRxLow"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DayOpticalPowerRxMed"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DayOpticalPowerRxHi"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DayOpticalPowerTxLow"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DayOpticalPowerTxMed"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DayOpticalPowerTxHi"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DayOpticalPowerSuspectReason"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacCurrFecCorrectedErrors"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacCurrFecUncorrectedBlocks"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacCurrFecBitErrorRate"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacCurrFecSuspectReason"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinFecSample"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinFecSampleTime"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinFecCorrectedErrors"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinFecUncorrectedBlocks"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinFecBitErrorRate"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinFecSuspectReason"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DayFecSample"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DayFecSampleTime"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DayFecCorrectedErrors"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DayFecUncorrectedBlocks"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DayFecBitErrorRate"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DayFecSuspectReason"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacCurrSnrValue"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacCurrSnrSuspectReason"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinSnrSample"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinSnrSampleTime"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinSnrValueLow"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinSnrValueMean"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinSnrValueHigh"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist15MinSnrSuspectReason"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DaySnrSample"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DaySnrSampleTime"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DaySnrValueLow"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DaySnrValueMean"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DaySnrValueHigh"),
        ("AOS-CORE-FACILITY-MIB", "aosCoreFacHist1DaySnrSuspectReason"))
)
if mibBuilder.loadTexts:
    aosCoreFacilityStatsObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aosCoreFacilityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 3, 3, 1, 1)
)
aosCoreFacilityCompliance.setObjects(
    ("AOS-CORE-FACILITY-MIB", "aosCoreFacilityStatsObjectGroup")
)
if mibBuilder.loadTexts:
    aosCoreFacilityCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AOS-CORE-FACILITY-MIB",
    **{"aosCoreFacilityMIB": aosCoreFacilityMIB,
       "aosCoreFacilityObjects": aosCoreFacilityObjects,
       "aosCoreFacilityStatsObjects": aosCoreFacilityStatsObjects,
       "aosCoreFacCurrOpticalPowerTable": aosCoreFacCurrOpticalPowerTable,
       "aosCoreFacCurrOpticalPowerEntry": aosCoreFacCurrOpticalPowerEntry,
       "aosCoreFacCurrOpticalPowerRx": aosCoreFacCurrOpticalPowerRx,
       "aosCoreFacCurrOpticalPowerTx": aosCoreFacCurrOpticalPowerTx,
       "aosCoreFacCurrOpticalPowerSuspectReason": aosCoreFacCurrOpticalPowerSuspectReason,
       "aosCoreFacHist15MinOpticalPowerTable": aosCoreFacHist15MinOpticalPowerTable,
       "aosCoreFacHist15MinOpticalPowerEntry": aosCoreFacHist15MinOpticalPowerEntry,
       "aosCoreFacHist15MinOpticalPowerSample": aosCoreFacHist15MinOpticalPowerSample,
       "aosCoreFacHist15MinOpticalPowerSampleTime": aosCoreFacHist15MinOpticalPowerSampleTime,
       "aosCoreFacHist15MinOpticalPowerRxLow": aosCoreFacHist15MinOpticalPowerRxLow,
       "aosCoreFacHist15MinOpticalPowerRxMed": aosCoreFacHist15MinOpticalPowerRxMed,
       "aosCoreFacHist15MinOpticalPowerRxHi": aosCoreFacHist15MinOpticalPowerRxHi,
       "aosCoreFacHist15MinOpticalPowerTxLow": aosCoreFacHist15MinOpticalPowerTxLow,
       "aosCoreFacHist15MinOpticalPowerTxMed": aosCoreFacHist15MinOpticalPowerTxMed,
       "aosCoreFacHist15MinOpticalPowerTxHi": aosCoreFacHist15MinOpticalPowerTxHi,
       "aosCoreFacHist15MinOpticalPowerSuspectReason": aosCoreFacHist15MinOpticalPowerSuspectReason,
       "aosCoreFacHist1DayOpticalPowerTable": aosCoreFacHist1DayOpticalPowerTable,
       "aosCoreFacHist1DayOpticalPowerEntry": aosCoreFacHist1DayOpticalPowerEntry,
       "aosCoreFacHist1DayOpticalPowerSample": aosCoreFacHist1DayOpticalPowerSample,
       "aosCoreFacHist1DayOpticalPowerSampleTime": aosCoreFacHist1DayOpticalPowerSampleTime,
       "aosCoreFacHist1DayOpticalPowerRxLow": aosCoreFacHist1DayOpticalPowerRxLow,
       "aosCoreFacHist1DayOpticalPowerRxMed": aosCoreFacHist1DayOpticalPowerRxMed,
       "aosCoreFacHist1DayOpticalPowerRxHi": aosCoreFacHist1DayOpticalPowerRxHi,
       "aosCoreFacHist1DayOpticalPowerTxLow": aosCoreFacHist1DayOpticalPowerTxLow,
       "aosCoreFacHist1DayOpticalPowerTxMed": aosCoreFacHist1DayOpticalPowerTxMed,
       "aosCoreFacHist1DayOpticalPowerTxHi": aosCoreFacHist1DayOpticalPowerTxHi,
       "aosCoreFacHist1DayOpticalPowerSuspectReason": aosCoreFacHist1DayOpticalPowerSuspectReason,
       "aosCoreFacCurrFecTable": aosCoreFacCurrFecTable,
       "aosCoreFacCurrFecEntry": aosCoreFacCurrFecEntry,
       "aosCoreFacCurrFecCorrectedErrors": aosCoreFacCurrFecCorrectedErrors,
       "aosCoreFacCurrFecUncorrectedBlocks": aosCoreFacCurrFecUncorrectedBlocks,
       "aosCoreFacCurrFecBitErrorRate": aosCoreFacCurrFecBitErrorRate,
       "aosCoreFacCurrFecSuspectReason": aosCoreFacCurrFecSuspectReason,
       "aosCoreFacHist15MinFecTable": aosCoreFacHist15MinFecTable,
       "aosCoreFacHist15MinFecEntry": aosCoreFacHist15MinFecEntry,
       "aosCoreFacHist15MinFecSample": aosCoreFacHist15MinFecSample,
       "aosCoreFacHist15MinFecSampleTime": aosCoreFacHist15MinFecSampleTime,
       "aosCoreFacHist15MinFecCorrectedErrors": aosCoreFacHist15MinFecCorrectedErrors,
       "aosCoreFacHist15MinFecUncorrectedBlocks": aosCoreFacHist15MinFecUncorrectedBlocks,
       "aosCoreFacHist15MinFecBitErrorRate": aosCoreFacHist15MinFecBitErrorRate,
       "aosCoreFacHist15MinFecSuspectReason": aosCoreFacHist15MinFecSuspectReason,
       "aosCoreFacHist1DayFecTable": aosCoreFacHist1DayFecTable,
       "aosCoreFacHist1DayFecEntry": aosCoreFacHist1DayFecEntry,
       "aosCoreFacHist1DayFecSample": aosCoreFacHist1DayFecSample,
       "aosCoreFacHist1DayFecSampleTime": aosCoreFacHist1DayFecSampleTime,
       "aosCoreFacHist1DayFecCorrectedErrors": aosCoreFacHist1DayFecCorrectedErrors,
       "aosCoreFacHist1DayFecUncorrectedBlocks": aosCoreFacHist1DayFecUncorrectedBlocks,
       "aosCoreFacHist1DayFecBitErrorRate": aosCoreFacHist1DayFecBitErrorRate,
       "aosCoreFacHist1DayFecSuspectReason": aosCoreFacHist1DayFecSuspectReason,
       "aosCoreFacCurrSnrTable": aosCoreFacCurrSnrTable,
       "aosCoreFacCurrSnrEntry": aosCoreFacCurrSnrEntry,
       "aosCoreFacCurrSnrValue": aosCoreFacCurrSnrValue,
       "aosCoreFacCurrSnrSuspectReason": aosCoreFacCurrSnrSuspectReason,
       "aosCoreFacHist15MinSnrTable": aosCoreFacHist15MinSnrTable,
       "aosCoreFacHist15MinSnrEntry": aosCoreFacHist15MinSnrEntry,
       "aosCoreFacHist15MinSnrSample": aosCoreFacHist15MinSnrSample,
       "aosCoreFacHist15MinSnrSampleTime": aosCoreFacHist15MinSnrSampleTime,
       "aosCoreFacHist15MinSnrValueLow": aosCoreFacHist15MinSnrValueLow,
       "aosCoreFacHist15MinSnrValueMean": aosCoreFacHist15MinSnrValueMean,
       "aosCoreFacHist15MinSnrValueHigh": aosCoreFacHist15MinSnrValueHigh,
       "aosCoreFacHist15MinSnrSuspectReason": aosCoreFacHist15MinSnrSuspectReason,
       "aosCoreFacHist1DaySnrTable": aosCoreFacHist1DaySnrTable,
       "aosCoreFacHist1DaySnrEntry": aosCoreFacHist1DaySnrEntry,
       "aosCoreFacHist1DaySnrSample": aosCoreFacHist1DaySnrSample,
       "aosCoreFacHist1DaySnrSampleTime": aosCoreFacHist1DaySnrSampleTime,
       "aosCoreFacHist1DaySnrValueLow": aosCoreFacHist1DaySnrValueLow,
       "aosCoreFacHist1DaySnrValueMean": aosCoreFacHist1DaySnrValueMean,
       "aosCoreFacHist1DaySnrValueHigh": aosCoreFacHist1DaySnrValueHigh,
       "aosCoreFacHist1DaySnrSuspectReason": aosCoreFacHist1DaySnrSuspectReason,
       "aosCoreFacilityConformance": aosCoreFacilityConformance,
       "aosCoreFacilityCompliances": aosCoreFacilityCompliances,
       "aosCoreFacilityCompliance": aosCoreFacilityCompliance,
       "aosCoreFacilityGroups": aosCoreFacilityGroups,
       "aosCoreFacilityStatsObjectGroup": aosCoreFacilityStatsObjectGroup}
)
