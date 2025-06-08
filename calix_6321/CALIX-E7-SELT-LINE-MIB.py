# SNMP MIB module (CALIX-E7-SELT-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/calix_6321/CALIX-E7-SELT-LINE-MIB.mib
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

(e7,
 e7Modules) = mibBuilder.importSymbols(
    "CALIX-PRODUCT-MIB",
    "e7",
    "e7Modules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

e7SeltTestDiags = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_E7XdslSeltLineTable_Object = MibTable
e7XdslSeltLineTable = _E7XdslSeltLineTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 1)
)
if mibBuilder.loadTexts:
    e7XdslSeltLineTable.setStatus("current")
_E7XdslSeltLineEntry_Object = MibTableRow
e7XdslSeltLineEntry = _E7XdslSeltLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 1, 1)
)
e7XdslSeltLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    e7XdslSeltLineEntry.setStatus("current")
_E7XdslUsMargin_Type = Integer32
_E7XdslUsMargin_Object = MibTableColumn
e7XdslUsMargin = _E7XdslUsMargin_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 1, 1, 1),
    _E7XdslUsMargin_Type()
)
e7XdslUsMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7XdslUsMargin.setStatus("current")
_E7XdslDsMargin_Type = Integer32
_E7XdslDsMargin_Object = MibTableColumn
e7XdslDsMargin = _E7XdslDsMargin_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 1, 1, 2),
    _E7XdslDsMargin_Type()
)
e7XdslDsMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7XdslDsMargin.setStatus("current")
_E7XdslUsNumTones_Type = Integer32
_E7XdslUsNumTones_Object = MibTableColumn
e7XdslUsNumTones = _E7XdslUsNumTones_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 1, 1, 3),
    _E7XdslUsNumTones_Type()
)
e7XdslUsNumTones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7XdslUsNumTones.setStatus("current")
_E7XdslDsNumTones_Type = Integer32
_E7XdslDsNumTones_Object = MibTableColumn
e7XdslDsNumTones = _E7XdslDsNumTones_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 1, 1, 4),
    _E7XdslDsNumTones_Type()
)
e7XdslDsNumTones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7XdslDsNumTones.setStatus("current")
_E7XdslUsRate_Type = Integer32
_E7XdslUsRate_Object = MibTableColumn
e7XdslUsRate = _E7XdslUsRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 1, 1, 5),
    _E7XdslUsRate_Type()
)
e7XdslUsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7XdslUsRate.setStatus("current")
_E7XdslDsRate_Type = Integer32
_E7XdslDsRate_Object = MibTableColumn
e7XdslDsRate = _E7XdslDsRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 1, 1, 6),
    _E7XdslDsRate_Type()
)
e7XdslDsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7XdslDsRate.setStatus("current")
_E7XdslBestFitIdx_Type = Integer32
_E7XdslBestFitIdx_Object = MibTableColumn
e7XdslBestFitIdx = _E7XdslBestFitIdx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 1, 1, 7),
    _E7XdslBestFitIdx_Type()
)
e7XdslBestFitIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7XdslBestFitIdx.setStatus("current")
_E7XdslLoopType_Type = Integer32
_E7XdslLoopType_Object = MibTableColumn
e7XdslLoopType = _E7XdslLoopType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 1, 1, 8),
    _E7XdslLoopType_Type()
)
e7XdslLoopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7XdslLoopType.setStatus("current")
_E7XdslLoopLength_Type = Integer32
_E7XdslLoopLength_Object = MibTableColumn
e7XdslLoopLength = _E7XdslLoopLength_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 1, 1, 9),
    _E7XdslLoopLength_Type()
)
e7XdslLoopLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7XdslLoopLength.setStatus("current")
_E7XdslFitError_Type = Integer32
_E7XdslFitError_Object = MibTableColumn
e7XdslFitError = _E7XdslFitError_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 1, 1, 10),
    _E7XdslFitError_Type()
)
e7XdslFitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7XdslFitError.setStatus("current")


class _E7XdslSeltLineCmndConfLdsfFailReason_Type(Integer32):
    """Custom type e7XdslSeltLineCmndConfLdsfFailReason based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("success", 2),
          ("inProgress", 3),
          ("cannotRun", 4),
          ("aborted", 5),
          ("failed", 6))
    )


_E7XdslSeltLineCmndConfLdsfFailReason_Type.__name__ = "Integer32"
_E7XdslSeltLineCmndConfLdsfFailReason_Object = MibTableColumn
e7XdslSeltLineCmndConfLdsfFailReason = _E7XdslSeltLineCmndConfLdsfFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 1, 1, 11),
    _E7XdslSeltLineCmndConfLdsfFailReason_Type()
)
e7XdslSeltLineCmndConfLdsfFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7XdslSeltLineCmndConfLdsfFailReason.setStatus("current")


class _E7XdslSeltLineCmndConfLdsf_Type(Integer32):
    """Custom type e7XdslSeltLineCmndConfLdsf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inhibit", 0),
          ("force", 1))
    )


_E7XdslSeltLineCmndConfLdsf_Type.__name__ = "Integer32"
_E7XdslSeltLineCmndConfLdsf_Object = MibTableColumn
e7XdslSeltLineCmndConfLdsf = _E7XdslSeltLineCmndConfLdsf_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 1, 1, 12),
    _E7XdslSeltLineCmndConfLdsf_Type()
)
e7XdslSeltLineCmndConfLdsf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7XdslSeltLineCmndConfLdsf.setStatus("current")
_E7SeltReportStatusTable_Object = MibTable
e7SeltReportStatusTable = _E7SeltReportStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 2)
)
if mibBuilder.loadTexts:
    e7SeltReportStatusTable.setStatus("current")
_E7SeltReportStatusEntry_Object = MibTableRow
e7SeltReportStatusEntry = _E7SeltReportStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 2, 1)
)
e7SeltReportStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CALIX-E7-SELT-LINE-MIB", "e7SeltBestFitIdx"),
)
if mibBuilder.loadTexts:
    e7SeltReportStatusEntry.setStatus("current")


class _E7SeltBestFitIdx_Type(Integer32):
    """Custom type e7SeltBestFitIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_E7SeltBestFitIdx_Type.__name__ = "Integer32"
_E7SeltBestFitIdx_Object = MibTableColumn
e7SeltBestFitIdx = _E7SeltBestFitIdx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 2, 1, 1),
    _E7SeltBestFitIdx_Type()
)
e7SeltBestFitIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7SeltBestFitIdx.setStatus("current")
_E7SeltReportValid_Type = Integer32
_E7SeltReportValid_Object = MibTableColumn
e7SeltReportValid = _E7SeltReportValid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 2, 1, 2),
    _E7SeltReportValid_Type()
)
e7SeltReportValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7SeltReportValid.setStatus("current")
_E7SeltRoundTripDelay_Type = OctetString
_E7SeltRoundTripDelay_Object = MibTableColumn
e7SeltRoundTripDelay = _E7SeltRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 2, 1, 3),
    _E7SeltRoundTripDelay_Type()
)
e7SeltRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7SeltRoundTripDelay.setStatus("current")
_E7SeltRoundTripError_Type = OctetString
_E7SeltRoundTripError_Object = MibTableColumn
e7SeltRoundTripError = _E7SeltRoundTripError_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 2, 1, 4),
    _E7SeltRoundTripError_Type()
)
e7SeltRoundTripError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7SeltRoundTripError.setStatus("current")
_E7SeltAttn300KHz_Type = OctetString
_E7SeltAttn300KHz_Object = MibTableColumn
e7SeltAttn300KHz = _E7SeltAttn300KHz_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 2, 1, 5),
    _E7SeltAttn300KHz_Type()
)
e7SeltAttn300KHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7SeltAttn300KHz.setStatus("current")
_E7SeltAttn180KHz_Type = OctetString
_E7SeltAttn180KHz_Object = MibTableColumn
e7SeltAttn180KHz = _E7SeltAttn180KHz_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 2, 1, 6),
    _E7SeltAttn180KHz_Type()
)
e7SeltAttn180KHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7SeltAttn180KHz.setStatus("current")
_E7SeltAttn1MHz_Type = OctetString
_E7SeltAttn1MHz_Object = MibTableColumn
e7SeltAttn1MHz = _E7SeltAttn1MHz_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 2, 1, 7),
    _E7SeltAttn1MHz_Type()
)
e7SeltAttn1MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7SeltAttn1MHz.setStatus("current")
_E7SeltAttnEndOfRange_Type = OctetString
_E7SeltAttnEndOfRange_Object = MibTableColumn
e7SeltAttnEndOfRange = _E7SeltAttnEndOfRange_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 2, 1, 8),
    _E7SeltAttnEndOfRange_Type()
)
e7SeltAttnEndOfRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7SeltAttnEndOfRange.setStatus("current")
_E7SeltFitError_Type = OctetString
_E7SeltFitError_Object = MibTableColumn
e7SeltFitError = _E7SeltFitError_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 2, 1, 9),
    _E7SeltFitError_Type()
)
e7SeltFitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7SeltFitError.setStatus("current")
_E7SeltTerminationPhase_Type = OctetString
_E7SeltTerminationPhase_Object = MibTableColumn
e7SeltTerminationPhase = _E7SeltTerminationPhase_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 2, 1, 10),
    _E7SeltTerminationPhase_Type()
)
e7SeltTerminationPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7SeltTerminationPhase.setStatus("current")
_E7SeltTransferFunction_Type = OctetString
_E7SeltTransferFunction_Object = MibTableColumn
e7SeltTransferFunction = _E7SeltTransferFunction_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 2, 1, 11),
    _E7SeltTransferFunction_Type()
)
e7SeltTransferFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7SeltTransferFunction.setStatus("current")
_E7SeltRangeStart_Type = Integer32
_E7SeltRangeStart_Object = MibTableColumn
e7SeltRangeStart = _E7SeltRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 2, 1, 12),
    _E7SeltRangeStart_Type()
)
e7SeltRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7SeltRangeStart.setStatus("current")
_E7SeltRangeStop_Type = Integer32
_E7SeltRangeStop_Object = MibTableColumn
e7SeltRangeStop = _E7SeltRangeStop_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 9, 2, 1, 13),
    _E7SeltRangeStop_Type()
)
e7SeltRangeStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7SeltRangeStop.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CALIX-E7-SELT-LINE-MIB",
    **{"e7SeltTestDiags": e7SeltTestDiags,
       "e7XdslSeltLineTable": e7XdslSeltLineTable,
       "e7XdslSeltLineEntry": e7XdslSeltLineEntry,
       "e7XdslUsMargin": e7XdslUsMargin,
       "e7XdslDsMargin": e7XdslDsMargin,
       "e7XdslUsNumTones": e7XdslUsNumTones,
       "e7XdslDsNumTones": e7XdslDsNumTones,
       "e7XdslUsRate": e7XdslUsRate,
       "e7XdslDsRate": e7XdslDsRate,
       "e7XdslBestFitIdx": e7XdslBestFitIdx,
       "e7XdslLoopType": e7XdslLoopType,
       "e7XdslLoopLength": e7XdslLoopLength,
       "e7XdslFitError": e7XdslFitError,
       "e7XdslSeltLineCmndConfLdsfFailReason": e7XdslSeltLineCmndConfLdsfFailReason,
       "e7XdslSeltLineCmndConfLdsf": e7XdslSeltLineCmndConfLdsf,
       "e7SeltReportStatusTable": e7SeltReportStatusTable,
       "e7SeltReportStatusEntry": e7SeltReportStatusEntry,
       "e7SeltBestFitIdx": e7SeltBestFitIdx,
       "e7SeltReportValid": e7SeltReportValid,
       "e7SeltRoundTripDelay": e7SeltRoundTripDelay,
       "e7SeltRoundTripError": e7SeltRoundTripError,
       "e7SeltAttn300KHz": e7SeltAttn300KHz,
       "e7SeltAttn180KHz": e7SeltAttn180KHz,
       "e7SeltAttn1MHz": e7SeltAttn1MHz,
       "e7SeltAttnEndOfRange": e7SeltAttnEndOfRange,
       "e7SeltFitError": e7SeltFitError,
       "e7SeltTerminationPhase": e7SeltTerminationPhase,
       "e7SeltTransferFunction": e7SeltTransferFunction,
       "e7SeltRangeStart": e7SeltRangeStart,
       "e7SeltRangeStop": e7SeltRangeStop}
)
