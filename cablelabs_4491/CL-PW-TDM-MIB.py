# SNMP MIB module (CL-PW-TDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/CL-PW-TDM-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:37:34 2025
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

(teaPwIndex,) = mibBuilder.importSymbols(
    "CL-PW-MIB",
    "teaPwIndex")

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(HCPerfTimeElapsed,) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfTimeElapsed")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

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
 StorageType,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

teaPwTDMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16)
)
if mibBuilder.loadTexts:
    teaPwTDMMIB.setRevisions(
        ("2006-02-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TeaPwTDMCfgIndex(TextualConvention, Unsigned32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_TeaPwTDMObjects_ObjectIdentity = ObjectIdentity
teaPwTDMObjects = _TeaPwTDMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1)
)
_TeaPwTDMTable_Object = MibTable
teaPwTDMTable = _TeaPwTDMTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 1)
)
if mibBuilder.loadTexts:
    teaPwTDMTable.setStatus("current")
_TeaPwTDMEntry_Object = MibTableRow
teaPwTDMEntry = _TeaPwTDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 1, 1)
)
teaPwTDMEntry.setIndexNames(
    (0, "CL-PW-MIB", "teaPwIndex"),
)
if mibBuilder.loadTexts:
    teaPwTDMEntry.setStatus("current")


class _TeaPwTDMRate_Type(Integer32):
    """Custom type teaPwTDMRate based on Integer32"""
    defaultValue = 32


_TeaPwTDMRate_Type.__name__ = "Integer32"
_TeaPwTDMRate_Object = MibTableColumn
teaPwTDMRate = _TeaPwTDMRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 1, 1, 1),
    _TeaPwTDMRate_Type()
)
teaPwTDMRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teaPwTDMRate.setStatus("current")
_TeaPwTDMIfIndex_Type = InterfaceIndexOrZero
_TeaPwTDMIfIndex_Object = MibTableColumn
teaPwTDMIfIndex = _TeaPwTDMIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 1, 1, 2),
    _TeaPwTDMIfIndex_Type()
)
teaPwTDMIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teaPwTDMIfIndex.setStatus("current")
_TeaPwGenTDMCfgIndex_Type = TeaPwTDMCfgIndex
_TeaPwGenTDMCfgIndex_Object = MibTableColumn
teaPwGenTDMCfgIndex = _TeaPwGenTDMCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 1, 1, 3),
    _TeaPwGenTDMCfgIndex_Type()
)
teaPwGenTDMCfgIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teaPwGenTDMCfgIndex.setStatus("current")
_TeaPwRelTDMCfgIndex_Type = TeaPwTDMCfgIndex
_TeaPwRelTDMCfgIndex_Object = MibTableColumn
teaPwRelTDMCfgIndex = _TeaPwRelTDMCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 1, 1, 4),
    _TeaPwRelTDMCfgIndex_Type()
)
teaPwRelTDMCfgIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teaPwRelTDMCfgIndex.setStatus("current")


class _TeaPwTDMConfigError_Type(Bits):
    """Custom type teaPwTDMConfigError based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("tdmTypeIncompatible", 1),
          ("peerRtpIncompatible", 2),
          ("peerPayloadSizeIncompatible", 3))
    )

_TeaPwTDMConfigError_Type.__name__ = "Bits"
_TeaPwTDMConfigError_Object = MibTableColumn
teaPwTDMConfigError = _TeaPwTDMConfigError_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 1, 1, 5),
    _TeaPwTDMConfigError_Type()
)
teaPwTDMConfigError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMConfigError.setStatus("current")


class _TeaPwTDMTimeElapsed_Type(Integer32):
    """Custom type teaPwTDMTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_TeaPwTDMTimeElapsed_Type.__name__ = "Integer32"
_TeaPwTDMTimeElapsed_Object = MibTableColumn
teaPwTDMTimeElapsed = _TeaPwTDMTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 1, 1, 6),
    _TeaPwTDMTimeElapsed_Type()
)
teaPwTDMTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMTimeElapsed.setStatus("current")


class _TeaPwTDMValidIntervals_Type(Integer32):
    """Custom type teaPwTDMValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_TeaPwTDMValidIntervals_Type.__name__ = "Integer32"
_TeaPwTDMValidIntervals_Object = MibTableColumn
teaPwTDMValidIntervals = _TeaPwTDMValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 1, 1, 7),
    _TeaPwTDMValidIntervals_Type()
)
teaPwTDMValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMValidIntervals.setStatus("current")


class _TeaPwTDMCurrentIndications_Type(Bits):
    """Custom type teaPwTDMCurrentIndications based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("strayPacket", 1),
          ("malformedPacket", 2),
          ("excessivePktLossRate", 3),
          ("bufferOverrun", 4),
          ("bufferUnderrun", 5),
          ("remotePktLoss", 6),
          ("pktMisOrder", 7),
          ("packetLoss", 8),
          ("tdmFault", 9))
    )

_TeaPwTDMCurrentIndications_Type.__name__ = "Bits"
_TeaPwTDMCurrentIndications_Object = MibTableColumn
teaPwTDMCurrentIndications = _TeaPwTDMCurrentIndications_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 1, 1, 8),
    _TeaPwTDMCurrentIndications_Type()
)
teaPwTDMCurrentIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMCurrentIndications.setStatus("current")


class _TeaPwTDMLatchedIndications_Type(Bits):
    """Custom type teaPwTDMLatchedIndications based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("staryPacket", 1),
          ("malformedPacket", 2),
          ("excessivePktLossRate", 3),
          ("bufferOverrun", 4),
          ("bufferUnderrun", 5),
          ("remotePktLoss", 6),
          ("pktMisOrder", 7),
          ("packetLoss", 8),
          ("tdmFault", 9))
    )

_TeaPwTDMLatchedIndications_Type.__name__ = "Bits"
_TeaPwTDMLatchedIndications_Object = MibTableColumn
teaPwTDMLatchedIndications = _TeaPwTDMLatchedIndications_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 1, 1, 9),
    _TeaPwTDMLatchedIndications_Type()
)
teaPwTDMLatchedIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMLatchedIndications.setStatus("current")
_TeaPwTDMLastEsTimeStamp_Type = TimeStamp
_TeaPwTDMLastEsTimeStamp_Object = MibTableColumn
teaPwTDMLastEsTimeStamp = _TeaPwTDMLastEsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 1, 1, 10),
    _TeaPwTDMLastEsTimeStamp_Type()
)
teaPwTDMLastEsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMLastEsTimeStamp.setStatus("current")
_TeaPwTDMRtpSSRC_Type = Unsigned32
_TeaPwTDMRtpSSRC_Object = MibTableColumn
teaPwTDMRtpSSRC = _TeaPwTDMRtpSSRC_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 1, 1, 11),
    _TeaPwTDMRtpSSRC_Type()
)
teaPwTDMRtpSSRC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMRtpSSRC.setStatus("current")


class _TeaPwTDMPeerRtpSSRC_Type(Unsigned32):
    """Custom type teaPwTDMPeerRtpSSRC based on Unsigned32"""
    defaultValue = 0


_TeaPwTDMPeerRtpSSRC_Type.__name__ = "Unsigned32"
_TeaPwTDMPeerRtpSSRC_Object = MibTableColumn
teaPwTDMPeerRtpSSRC = _TeaPwTDMPeerRtpSSRC_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 1, 1, 12),
    _TeaPwTDMPeerRtpSSRC_Type()
)
teaPwTDMPeerRtpSSRC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMPeerRtpSSRC.setStatus("current")
_TeaPwTDMCfgIndexNext_Type = TestAndIncr
_TeaPwTDMCfgIndexNext_Object = MibScalar
teaPwTDMCfgIndexNext = _TeaPwTDMCfgIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 2),
    _TeaPwTDMCfgIndexNext_Type()
)
teaPwTDMCfgIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMCfgIndexNext.setStatus("current")
_TeaPwTDMCfgTable_Object = MibTable
teaPwTDMCfgTable = _TeaPwTDMCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3)
)
if mibBuilder.loadTexts:
    teaPwTDMCfgTable.setStatus("current")
_TeaPwTDMCfgEntry_Object = MibTableRow
teaPwTDMCfgEntry = _TeaPwTDMCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1)
)
teaPwTDMCfgEntry.setIndexNames(
    (0, "CL-PW-TDM-MIB", "teaPwGenTDMCfgIndex"),
)
if mibBuilder.loadTexts:
    teaPwTDMCfgEntry.setStatus("current")
_TeaPwTDMCfgIndex_Type = TeaPwTDMCfgIndex
_TeaPwTDMCfgIndex_Object = MibTableColumn
teaPwTDMCfgIndex = _TeaPwTDMCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 1),
    _TeaPwTDMCfgIndex_Type()
)
teaPwTDMCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teaPwTDMCfgIndex.setStatus("current")
_TeaPwTDMCfgRowStatus_Type = RowStatus
_TeaPwTDMCfgRowStatus_Object = MibTableColumn
teaPwTDMCfgRowStatus = _TeaPwTDMCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 2),
    _TeaPwTDMCfgRowStatus_Type()
)
teaPwTDMCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgRowStatus.setStatus("current")


class _TeaPwTDMCfgConfErr_Type(Bits):
    """Custom type teaPwTDMCfgConfErr based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("payloadSize", 1),
          ("jtrBfrDepth", 2))
    )

_TeaPwTDMCfgConfErr_Type.__name__ = "Bits"
_TeaPwTDMCfgConfErr_Object = MibTableColumn
teaPwTDMCfgConfErr = _TeaPwTDMCfgConfErr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 3),
    _TeaPwTDMCfgConfErr_Type()
)
teaPwTDMCfgConfErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMCfgConfErr.setStatus("current")
_TeaPwTDMCfgPayloadSize_Type = Unsigned32
_TeaPwTDMCfgPayloadSize_Object = MibTableColumn
teaPwTDMCfgPayloadSize = _TeaPwTDMCfgPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 4),
    _TeaPwTDMCfgPayloadSize_Type()
)
teaPwTDMCfgPayloadSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgPayloadSize.setStatus("current")


class _TeaPwTDMCfgPktReorder_Type(TruthValue):
    """Custom type teaPwTDMCfgPktReorder based on TruthValue"""
    defaultValue = 1


_TeaPwTDMCfgPktReorder_Type.__name__ = "TruthValue"
_TeaPwTDMCfgPktReorder_Object = MibTableColumn
teaPwTDMCfgPktReorder = _TeaPwTDMCfgPktReorder_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 5),
    _TeaPwTDMCfgPktReorder_Type()
)
teaPwTDMCfgPktReorder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgPktReorder.setStatus("current")


class _TeaPwTDMCfgRtpHdrUsed_Type(TruthValue):
    """Custom type teaPwTDMCfgRtpHdrUsed based on TruthValue"""
    defaultValue = 2


_TeaPwTDMCfgRtpHdrUsed_Type.__name__ = "TruthValue"
_TeaPwTDMCfgRtpHdrUsed_Object = MibTableColumn
teaPwTDMCfgRtpHdrUsed = _TeaPwTDMCfgRtpHdrUsed_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 6),
    _TeaPwTDMCfgRtpHdrUsed_Type()
)
teaPwTDMCfgRtpHdrUsed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgRtpHdrUsed.setStatus("current")


class _TeaPwTDMCfgJtrBfrDepth_Type(Unsigned32):
    """Custom type teaPwTDMCfgJtrBfrDepth based on Unsigned32"""
    defaultValue = 3000


_TeaPwTDMCfgJtrBfrDepth_Type.__name__ = "Unsigned32"
_TeaPwTDMCfgJtrBfrDepth_Object = MibTableColumn
teaPwTDMCfgJtrBfrDepth = _TeaPwTDMCfgJtrBfrDepth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 7),
    _TeaPwTDMCfgJtrBfrDepth_Type()
)
teaPwTDMCfgJtrBfrDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgJtrBfrDepth.setStatus("current")
if mibBuilder.loadTexts:
    teaPwTDMCfgJtrBfrDepth.setUnits("microsecond")


class _TeaPwTDMCfgPayloadSuppression_Type(Integer32):
    """Custom type teaPwTDMCfgPayloadSuppression based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TeaPwTDMCfgPayloadSuppression_Type.__name__ = "Integer32"
_TeaPwTDMCfgPayloadSuppression_Object = MibTableColumn
teaPwTDMCfgPayloadSuppression = _TeaPwTDMCfgPayloadSuppression_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 8),
    _TeaPwTDMCfgPayloadSuppression_Type()
)
teaPwTDMCfgPayloadSuppression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgPayloadSuppression.setStatus("current")


class _TeaPwTDMCfgConsecPktsInSynch_Type(Unsigned32):
    """Custom type teaPwTDMCfgConsecPktsInSynch based on Unsigned32"""
    defaultValue = 0


_TeaPwTDMCfgConsecPktsInSynch_Type.__name__ = "Unsigned32"
_TeaPwTDMCfgConsecPktsInSynch_Object = MibTableColumn
teaPwTDMCfgConsecPktsInSynch = _TeaPwTDMCfgConsecPktsInSynch_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 9),
    _TeaPwTDMCfgConsecPktsInSynch_Type()
)
teaPwTDMCfgConsecPktsInSynch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgConsecPktsInSynch.setStatus("current")


class _TeaPwTDMCfgConsecMissPktsOutSynch_Type(Unsigned32):
    """Custom type teaPwTDMCfgConsecMissPktsOutSynch based on Unsigned32"""
    defaultValue = 0


_TeaPwTDMCfgConsecMissPktsOutSynch_Type.__name__ = "Unsigned32"
_TeaPwTDMCfgConsecMissPktsOutSynch_Object = MibTableColumn
teaPwTDMCfgConsecMissPktsOutSynch = _TeaPwTDMCfgConsecMissPktsOutSynch_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 10),
    _TeaPwTDMCfgConsecMissPktsOutSynch_Type()
)
teaPwTDMCfgConsecMissPktsOutSynch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgConsecMissPktsOutSynch.setStatus("current")


class _TeaPwTDMCfgSetUp2SynchTimeOut_Type(Unsigned32):
    """Custom type teaPwTDMCfgSetUp2SynchTimeOut based on Unsigned32"""
    defaultValue = 5


_TeaPwTDMCfgSetUp2SynchTimeOut_Type.__name__ = "Unsigned32"
_TeaPwTDMCfgSetUp2SynchTimeOut_Object = MibTableColumn
teaPwTDMCfgSetUp2SynchTimeOut = _TeaPwTDMCfgSetUp2SynchTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 11),
    _TeaPwTDMCfgSetUp2SynchTimeOut_Type()
)
teaPwTDMCfgSetUp2SynchTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgSetUp2SynchTimeOut.setStatus("current")


class _TeaPwTDMCfgPktReplacePolicy_Type(Integer32):
    """Custom type teaPwTDMCfgPktReplacePolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ais", 1),
          ("fillerPattern", 2),
          ("implementationSpecific", 3))
    )


_TeaPwTDMCfgPktReplacePolicy_Type.__name__ = "Integer32"
_TeaPwTDMCfgPktReplacePolicy_Object = MibTableColumn
teaPwTDMCfgPktReplacePolicy = _TeaPwTDMCfgPktReplacePolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 12),
    _TeaPwTDMCfgPktReplacePolicy_Type()
)
teaPwTDMCfgPktReplacePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgPktReplacePolicy.setStatus("current")
_TeaPwTDMCfgAvePktLossTimeWindow_Type = Integer32
_TeaPwTDMCfgAvePktLossTimeWindow_Object = MibTableColumn
teaPwTDMCfgAvePktLossTimeWindow = _TeaPwTDMCfgAvePktLossTimeWindow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 13),
    _TeaPwTDMCfgAvePktLossTimeWindow_Type()
)
teaPwTDMCfgAvePktLossTimeWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgAvePktLossTimeWindow.setStatus("current")
if mibBuilder.loadTexts:
    teaPwTDMCfgAvePktLossTimeWindow.setUnits("millisecond")
_TeaPwTDMCfgExcessivePktLossThreshold_Type = Unsigned32
_TeaPwTDMCfgExcessivePktLossThreshold_Object = MibTableColumn
teaPwTDMCfgExcessivePktLossThreshold = _TeaPwTDMCfgExcessivePktLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 14),
    _TeaPwTDMCfgExcessivePktLossThreshold_Type()
)
teaPwTDMCfgExcessivePktLossThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgExcessivePktLossThreshold.setStatus("current")


class _TeaPwTDMCfgAlarmThreshold_Type(Unsigned32):
    """Custom type teaPwTDMCfgAlarmThreshold based on Unsigned32"""
    defaultValue = 2500


_TeaPwTDMCfgAlarmThreshold_Type.__name__ = "Unsigned32"
_TeaPwTDMCfgAlarmThreshold_Object = MibTableColumn
teaPwTDMCfgAlarmThreshold = _TeaPwTDMCfgAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 15),
    _TeaPwTDMCfgAlarmThreshold_Type()
)
teaPwTDMCfgAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgAlarmThreshold.setStatus("current")


class _TeaPwTDMCfgClearAlarmThreshold_Type(Unsigned32):
    """Custom type teaPwTDMCfgClearAlarmThreshold based on Unsigned32"""
    defaultValue = 10000


_TeaPwTDMCfgClearAlarmThreshold_Type.__name__ = "Unsigned32"
_TeaPwTDMCfgClearAlarmThreshold_Object = MibTableColumn
teaPwTDMCfgClearAlarmThreshold = _TeaPwTDMCfgClearAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 16),
    _TeaPwTDMCfgClearAlarmThreshold_Type()
)
teaPwTDMCfgClearAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgClearAlarmThreshold.setStatus("current")


class _TeaPwTDMCfgMissingPktsToSes_Type(Unsigned32):
    """Custom type teaPwTDMCfgMissingPktsToSes based on Unsigned32"""
    defaultValue = 3


_TeaPwTDMCfgMissingPktsToSes_Type.__name__ = "Unsigned32"
_TeaPwTDMCfgMissingPktsToSes_Object = MibTableColumn
teaPwTDMCfgMissingPktsToSes = _TeaPwTDMCfgMissingPktsToSes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 17),
    _TeaPwTDMCfgMissingPktsToSes_Type()
)
teaPwTDMCfgMissingPktsToSes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgMissingPktsToSes.setStatus("current")
if mibBuilder.loadTexts:
    teaPwTDMCfgMissingPktsToSes.setUnits("seconds")


class _TeaPwTDMCfgTimestampMode_Type(Integer32):
    """Custom type teaPwTDMCfgTimestampMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("absolute", 2),
          ("differential", 3),
          ("primeDifferential", 4))
    )


_TeaPwTDMCfgTimestampMode_Type.__name__ = "Integer32"
_TeaPwTDMCfgTimestampMode_Object = MibTableColumn
teaPwTDMCfgTimestampMode = _TeaPwTDMCfgTimestampMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 18),
    _TeaPwTDMCfgTimestampMode_Type()
)
teaPwTDMCfgTimestampMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgTimestampMode.setStatus("current")
_TeaPwTDMCfgStorageType_Type = StorageType
_TeaPwTDMCfgStorageType_Object = MibTableColumn
teaPwTDMCfgStorageType = _TeaPwTDMCfgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 19),
    _TeaPwTDMCfgStorageType_Type()
)
teaPwTDMCfgStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgStorageType.setStatus("current")


class _TeaPwTMDCfgFillerPattern_Type(Unsigned32):
    """Custom type teaPwTMDCfgFillerPattern based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TeaPwTMDCfgFillerPattern_Type.__name__ = "Unsigned32"
_TeaPwTMDCfgFillerPattern_Object = MibTableColumn
teaPwTMDCfgFillerPattern = _TeaPwTMDCfgFillerPattern_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 20),
    _TeaPwTMDCfgFillerPattern_Type()
)
teaPwTMDCfgFillerPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTMDCfgFillerPattern.setStatus("current")


class _TeaPwTDMCfgLflagPayloadPolicy_Type(Integer32):
    """Custom type teaPwTDMCfgLflagPayloadPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("use", 2))
    )


_TeaPwTDMCfgLflagPayloadPolicy_Type.__name__ = "Integer32"
_TeaPwTDMCfgLflagPayloadPolicy_Object = MibTableColumn
teaPwTDMCfgLflagPayloadPolicy = _TeaPwTDMCfgLflagPayloadPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 21),
    _TeaPwTDMCfgLflagPayloadPolicy_Type()
)
teaPwTDMCfgLflagPayloadPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgLflagPayloadPolicy.setStatus("current")
_TeaPwTDMCfgIPTos_Type = Unsigned32
_TeaPwTDMCfgIPTos_Object = MibTableColumn
teaPwTDMCfgIPTos = _TeaPwTDMCfgIPTos_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 22),
    _TeaPwTDMCfgIPTos_Type()
)
teaPwTDMCfgIPTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgIPTos.setStatus("current")


class _TeaPwTDMCfgRtpPT_Type(Unsigned32):
    """Custom type teaPwTDMCfgRtpPT based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TeaPwTDMCfgRtpPT_Type.__name__ = "Unsigned32"
_TeaPwTDMCfgRtpPT_Object = MibTableColumn
teaPwTDMCfgRtpPT = _TeaPwTDMCfgRtpPT_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 23),
    _TeaPwTDMCfgRtpPT_Type()
)
teaPwTDMCfgRtpPT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgRtpPT.setStatus("current")


class _TeaPwTDMCfgPeerRtpPT_Type(Unsigned32):
    """Custom type teaPwTDMCfgPeerRtpPT based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TeaPwTDMCfgPeerRtpPT_Type.__name__ = "Unsigned32"
_TeaPwTDMCfgPeerRtpPT_Object = MibTableColumn
teaPwTDMCfgPeerRtpPT = _TeaPwTDMCfgPeerRtpPT_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 24),
    _TeaPwTDMCfgPeerRtpPT_Type()
)
teaPwTDMCfgPeerRtpPT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgPeerRtpPT.setStatus("current")


class _TeaPwTDMCfgRtpTSRef_Type(Unsigned32):
    """Custom type teaPwTDMCfgRtpTSRef based on Unsigned32"""
    defaultValue = 1280


_TeaPwTDMCfgRtpTSRef_Type.__name__ = "Unsigned32"
_TeaPwTDMCfgRtpTSRef_Object = MibTableColumn
teaPwTDMCfgRtpTSRef = _TeaPwTDMCfgRtpTSRef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 25),
    _TeaPwTDMCfgRtpTSRef_Type()
)
teaPwTDMCfgRtpTSRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgRtpTSRef.setStatus("current")


class _TeaPwTDMCfgPeerRtpTSRef_Type(Unsigned32):
    """Custom type teaPwTDMCfgPeerRtpTSRef based on Unsigned32"""
    defaultValue = 1280


_TeaPwTDMCfgPeerRtpTSRef_Type.__name__ = "Unsigned32"
_TeaPwTDMCfgPeerRtpTSRef_Object = MibTableColumn
teaPwTDMCfgPeerRtpTSRef = _TeaPwTDMCfgPeerRtpTSRef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 26),
    _TeaPwTDMCfgPeerRtpTSRef_Type()
)
teaPwTDMCfgPeerRtpTSRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgPeerRtpTSRef.setStatus("current")


class _TeaPwTDMCfgSRTPenable_Type(TruthValue):
    """Custom type teaPwTDMCfgSRTPenable based on TruthValue"""
    defaultValue = 2


_TeaPwTDMCfgSRTPenable_Type.__name__ = "TruthValue"
_TeaPwTDMCfgSRTPenable_Object = MibTableColumn
teaPwTDMCfgSRTPenable = _TeaPwTDMCfgSRTPenable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 3, 1, 27),
    _TeaPwTDMCfgSRTPenable_Type()
)
teaPwTDMCfgSRTPenable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgSRTPenable.setStatus("current")
_TeaPwTDMCfgFramedIndexNext_Type = TestAndIncr
_TeaPwTDMCfgFramedIndexNext_Object = MibScalar
teaPwTDMCfgFramedIndexNext = _TeaPwTDMCfgFramedIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 4),
    _TeaPwTDMCfgFramedIndexNext_Type()
)
teaPwTDMCfgFramedIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMCfgFramedIndexNext.setStatus("current")
_TeaPwTDMCfgFramedTable_Object = MibTable
teaPwTDMCfgFramedTable = _TeaPwTDMCfgFramedTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 5)
)
if mibBuilder.loadTexts:
    teaPwTDMCfgFramedTable.setStatus("current")
_TeaPwTDMCfgFramedEntry_Object = MibTableRow
teaPwTDMCfgFramedEntry = _TeaPwTDMCfgFramedEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 5, 1)
)
teaPwTDMCfgFramedEntry.setIndexNames(
    (0, "CL-PW-TDM-MIB", "teaPwTDMCfgFramedIndex"),
)
if mibBuilder.loadTexts:
    teaPwTDMCfgFramedEntry.setStatus("current")
_TeaPwTDMCfgFramedIndex_Type = TeaPwTDMCfgIndex
_TeaPwTDMCfgFramedIndex_Object = MibTableColumn
teaPwTDMCfgFramedIndex = _TeaPwTDMCfgFramedIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 5, 1, 1),
    _TeaPwTDMCfgFramedIndex_Type()
)
teaPwTDMCfgFramedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teaPwTDMCfgFramedIndex.setStatus("current")
_TeaPwTDMCfgFramedRowStatus_Type = RowStatus
_TeaPwTDMCfgFramedRowStatus_Object = MibTableColumn
teaPwTDMCfgFramedRowStatus = _TeaPwTDMCfgFramedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 5, 1, 2),
    _TeaPwTDMCfgFramedRowStatus_Type()
)
teaPwTDMCfgFramedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgFramedRowStatus.setStatus("current")


class _TeaPwTDMCfgFramedIdlePattern_Type(Unsigned32):
    """Custom type teaPwTDMCfgFramedIdlePattern based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TeaPwTDMCfgFramedIdlePattern_Type.__name__ = "Unsigned32"
_TeaPwTDMCfgFramedIdlePattern_Object = MibTableColumn
teaPwTDMCfgFramedIdlePattern = _TeaPwTDMCfgFramedIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 5, 1, 3),
    _TeaPwTDMCfgFramedIdlePattern_Type()
)
teaPwTDMCfgFramedIdlePattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgFramedIdlePattern.setStatus("current")


class _TeaPwTDMCfgFramedLflagPolicy_Type(Integer32):
    """Custom type teaPwTDMCfgFramedLflagPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("trunkAis", 2),
          ("channelIdle", 3))
    )


_TeaPwTDMCfgFramedLflagPolicy_Type.__name__ = "Integer32"
_TeaPwTDMCfgFramedLflagPolicy_Object = MibTableColumn
teaPwTDMCfgFramedLflagPolicy = _TeaPwTDMCfgFramedLflagPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 5, 1, 4),
    _TeaPwTDMCfgFramedLflagPolicy_Type()
)
teaPwTDMCfgFramedLflagPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgFramedLflagPolicy.setStatus("current")


class _TeaPwTDMCfgFramedRflagPolicy_Type(Integer32):
    """Custom type teaPwTDMCfgFramedRflagPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rai", 2),
          ("channelIdle", 3))
    )


_TeaPwTDMCfgFramedRflagPolicy_Type.__name__ = "Integer32"
_TeaPwTDMCfgFramedRflagPolicy_Object = MibTableColumn
teaPwTDMCfgFramedRflagPolicy = _TeaPwTDMCfgFramedRflagPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 5, 1, 5),
    _TeaPwTDMCfgFramedRflagPolicy_Type()
)
teaPwTDMCfgFramedRflagPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgFramedRflagPolicy.setStatus("current")


class _TeaPwTDMCfgFramedRDPolicy_Type(Integer32):
    """Custom type teaPwTDMCfgFramedRDPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rai", 2),
          ("channelIdle", 3))
    )


_TeaPwTDMCfgFramedRDPolicy_Type.__name__ = "Integer32"
_TeaPwTDMCfgFramedRDPolicy_Object = MibTableColumn
teaPwTDMCfgFramedRDPolicy = _TeaPwTDMCfgFramedRDPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 5, 1, 6),
    _TeaPwTDMCfgFramedRDPolicy_Type()
)
teaPwTDMCfgFramedRDPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgFramedRDPolicy.setStatus("current")


class _TeaPwTDMCfgFramedLopsPolicy_Type(Integer32):
    """Custom type teaPwTDMCfgFramedLopsPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("trunkAis", 2),
          ("channelIdle", 3))
    )


_TeaPwTDMCfgFramedLopsPolicy_Type.__name__ = "Integer32"
_TeaPwTDMCfgFramedLopsPolicy_Object = MibTableColumn
teaPwTDMCfgFramedLopsPolicy = _TeaPwTDMCfgFramedLopsPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 5, 1, 7),
    _TeaPwTDMCfgFramedLopsPolicy_Type()
)
teaPwTDMCfgFramedLopsPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgFramedLopsPolicy.setStatus("current")
_TeaPwTDMCfgFramedSigIPTos_Type = Unsigned32
_TeaPwTDMCfgFramedSigIPTos_Object = MibTableColumn
teaPwTDMCfgFramedSigIPTos = _TeaPwTDMCfgFramedSigIPTos_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 5, 1, 8),
    _TeaPwTDMCfgFramedSigIPTos_Type()
)
teaPwTDMCfgFramedSigIPTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgFramedSigIPTos.setStatus("current")


class _TeaPwTDMCfgFramedSigPT_Type(Unsigned32):
    """Custom type teaPwTDMCfgFramedSigPT based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TeaPwTDMCfgFramedSigPT_Type.__name__ = "Unsigned32"
_TeaPwTDMCfgFramedSigPT_Object = MibTableColumn
teaPwTDMCfgFramedSigPT = _TeaPwTDMCfgFramedSigPT_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 5, 1, 9),
    _TeaPwTDMCfgFramedSigPT_Type()
)
teaPwTDMCfgFramedSigPT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgFramedSigPT.setStatus("current")


class _TeaPwTDMCfgFramedSigPeerPT_Type(Unsigned32):
    """Custom type teaPwTDMCfgFramedSigPeerPT based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TeaPwTDMCfgFramedSigPeerPT_Type.__name__ = "Unsigned32"
_TeaPwTDMCfgFramedSigPeerPT_Object = MibTableColumn
teaPwTDMCfgFramedSigPeerPT = _TeaPwTDMCfgFramedSigPeerPT_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 5, 1, 10),
    _TeaPwTDMCfgFramedSigPeerPT_Type()
)
teaPwTDMCfgFramedSigPeerPT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgFramedSigPeerPT.setStatus("current")


class _TeaPwTDMCfgFramedSigIdle_Type(Unsigned32):
    """Custom type teaPwTDMCfgFramedSigIdle based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TeaPwTDMCfgFramedSigIdle_Type.__name__ = "Unsigned32"
_TeaPwTDMCfgFramedSigIdle_Object = MibTableColumn
teaPwTDMCfgFramedSigIdle = _TeaPwTDMCfgFramedSigIdle_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 5, 1, 11),
    _TeaPwTDMCfgFramedSigIdle_Type()
)
teaPwTDMCfgFramedSigIdle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgFramedSigIdle.setStatus("current")


class _TeaPwTDMCfgFramedSigInterval_Type(Unsigned32):
    """Custom type teaPwTDMCfgFramedSigInterval based on Unsigned32"""
    defaultValue = 5


_TeaPwTDMCfgFramedSigInterval_Type.__name__ = "Unsigned32"
_TeaPwTDMCfgFramedSigInterval_Object = MibTableColumn
teaPwTDMCfgFramedSigInterval = _TeaPwTDMCfgFramedSigInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 5, 1, 12),
    _TeaPwTDMCfgFramedSigInterval_Type()
)
teaPwTDMCfgFramedSigInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgFramedSigInterval.setStatus("current")


class _TeaPwTDMCfgFramedSigMaxInterval_Type(Unsigned32):
    """Custom type teaPwTDMCfgFramedSigMaxInterval based on Unsigned32"""
    defaultValue = 5


_TeaPwTDMCfgFramedSigMaxInterval_Type.__name__ = "Unsigned32"
_TeaPwTDMCfgFramedSigMaxInterval_Object = MibTableColumn
teaPwTDMCfgFramedSigMaxInterval = _TeaPwTDMCfgFramedSigMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 5, 1, 13),
    _TeaPwTDMCfgFramedSigMaxInterval_Type()
)
teaPwTDMCfgFramedSigMaxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwTDMCfgFramedSigMaxInterval.setStatus("current")
_TeaPwTDMPerfCurrentTable_Object = MibTable
teaPwTDMPerfCurrentTable = _TeaPwTDMPerfCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 6)
)
if mibBuilder.loadTexts:
    teaPwTDMPerfCurrentTable.setStatus("current")
_TeaPwTDMPerfCurrentEntry_Object = MibTableRow
teaPwTDMPerfCurrentEntry = _TeaPwTDMPerfCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 6, 1)
)
teaPwTDMPerfCurrentEntry.setIndexNames(
    (0, "CL-PW-MIB", "teaPwIndex"),
)
if mibBuilder.loadTexts:
    teaPwTDMPerfCurrentEntry.setStatus("current")
_TeaPwTDMPerfCurrentMissingPkts_Type = PerfCurrentCount
_TeaPwTDMPerfCurrentMissingPkts_Object = MibTableColumn
teaPwTDMPerfCurrentMissingPkts = _TeaPwTDMPerfCurrentMissingPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 6, 1, 1),
    _TeaPwTDMPerfCurrentMissingPkts_Type()
)
teaPwTDMPerfCurrentMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfCurrentMissingPkts.setStatus("current")
_TeaPwTDMPerfCurrentPktsReOrder_Type = PerfCurrentCount
_TeaPwTDMPerfCurrentPktsReOrder_Object = MibTableColumn
teaPwTDMPerfCurrentPktsReOrder = _TeaPwTDMPerfCurrentPktsReOrder_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 6, 1, 2),
    _TeaPwTDMPerfCurrentPktsReOrder_Type()
)
teaPwTDMPerfCurrentPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfCurrentPktsReOrder.setStatus("current")
_TeaPwTDMPerfCurrentJtrBfrUnderruns_Type = PerfCurrentCount
_TeaPwTDMPerfCurrentJtrBfrUnderruns_Object = MibTableColumn
teaPwTDMPerfCurrentJtrBfrUnderruns = _TeaPwTDMPerfCurrentJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 6, 1, 3),
    _TeaPwTDMPerfCurrentJtrBfrUnderruns_Type()
)
teaPwTDMPerfCurrentJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfCurrentJtrBfrUnderruns.setStatus("current")
_TeaPwTDMPerfCurrentMisOrderDropped_Type = PerfCurrentCount
_TeaPwTDMPerfCurrentMisOrderDropped_Object = MibTableColumn
teaPwTDMPerfCurrentMisOrderDropped = _TeaPwTDMPerfCurrentMisOrderDropped_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 6, 1, 4),
    _TeaPwTDMPerfCurrentMisOrderDropped_Type()
)
teaPwTDMPerfCurrentMisOrderDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfCurrentMisOrderDropped.setStatus("current")
_TeaPwTDMPerfCurrentMalformedPkt_Type = PerfCurrentCount
_TeaPwTDMPerfCurrentMalformedPkt_Object = MibTableColumn
teaPwTDMPerfCurrentMalformedPkt = _TeaPwTDMPerfCurrentMalformedPkt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 6, 1, 5),
    _TeaPwTDMPerfCurrentMalformedPkt_Type()
)
teaPwTDMPerfCurrentMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfCurrentMalformedPkt.setStatus("current")
_TeaPwTDMPerfCurrentESs_Type = PerfCurrentCount
_TeaPwTDMPerfCurrentESs_Object = MibTableColumn
teaPwTDMPerfCurrentESs = _TeaPwTDMPerfCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 6, 1, 6),
    _TeaPwTDMPerfCurrentESs_Type()
)
teaPwTDMPerfCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfCurrentESs.setStatus("current")
_TeaPwTDMPerfCurrentSESs_Type = PerfCurrentCount
_TeaPwTDMPerfCurrentSESs_Object = MibTableColumn
teaPwTDMPerfCurrentSESs = _TeaPwTDMPerfCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 6, 1, 7),
    _TeaPwTDMPerfCurrentSESs_Type()
)
teaPwTDMPerfCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfCurrentSESs.setStatus("current")
_TeaPwTDMPerfCurrentUASs_Type = PerfCurrentCount
_TeaPwTDMPerfCurrentUASs_Object = MibTableColumn
teaPwTDMPerfCurrentUASs = _TeaPwTDMPerfCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 6, 1, 8),
    _TeaPwTDMPerfCurrentUASs_Type()
)
teaPwTDMPerfCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfCurrentUASs.setStatus("current")
_TeaPwTDMPerfCurrentFC_Type = PerfCurrentCount
_TeaPwTDMPerfCurrentFC_Object = MibTableColumn
teaPwTDMPerfCurrentFC = _TeaPwTDMPerfCurrentFC_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 6, 1, 9),
    _TeaPwTDMPerfCurrentFC_Type()
)
teaPwTDMPerfCurrentFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfCurrentFC.setStatus("current")
_TeaPwTDMPerfCurrentJtrBfrMin_Type = Unsigned32
_TeaPwTDMPerfCurrentJtrBfrMin_Object = MibTableColumn
teaPwTDMPerfCurrentJtrBfrMin = _TeaPwTDMPerfCurrentJtrBfrMin_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 6, 1, 10),
    _TeaPwTDMPerfCurrentJtrBfrMin_Type()
)
teaPwTDMPerfCurrentJtrBfrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfCurrentJtrBfrMin.setStatus("current")
_TeaPwTDMPerfCurrentJtrBfr_Type = Unsigned32
_TeaPwTDMPerfCurrentJtrBfr_Object = MibTableColumn
teaPwTDMPerfCurrentJtrBfr = _TeaPwTDMPerfCurrentJtrBfr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 6, 1, 11),
    _TeaPwTDMPerfCurrentJtrBfr_Type()
)
teaPwTDMPerfCurrentJtrBfr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfCurrentJtrBfr.setStatus("current")
_TeaPwTDMPerfCurrentJtrBfrMax_Type = Unsigned32
_TeaPwTDMPerfCurrentJtrBfrMax_Object = MibTableColumn
teaPwTDMPerfCurrentJtrBfrMax = _TeaPwTDMPerfCurrentJtrBfrMax_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 6, 1, 12),
    _TeaPwTDMPerfCurrentJtrBfrMax_Type()
)
teaPwTDMPerfCurrentJtrBfrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfCurrentJtrBfrMax.setStatus("current")
_TeaPwTDMPerfIntervalTable_Object = MibTable
teaPwTDMPerfIntervalTable = _TeaPwTDMPerfIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 7)
)
if mibBuilder.loadTexts:
    teaPwTDMPerfIntervalTable.setStatus("current")
_TeaPwTDMPerfIntervalEntry_Object = MibTableRow
teaPwTDMPerfIntervalEntry = _TeaPwTDMPerfIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 7, 1)
)
teaPwTDMPerfIntervalEntry.setIndexNames(
    (0, "CL-PW-MIB", "teaPwIndex"),
    (0, "CL-PW-TDM-MIB", "teaPwTDMPerfIntervalNumber"),
)
if mibBuilder.loadTexts:
    teaPwTDMPerfIntervalEntry.setStatus("current")
_TeaPwTDMPerfIntervalNumber_Type = Unsigned32
_TeaPwTDMPerfIntervalNumber_Object = MibTableColumn
teaPwTDMPerfIntervalNumber = _TeaPwTDMPerfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 7, 1, 1),
    _TeaPwTDMPerfIntervalNumber_Type()
)
teaPwTDMPerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teaPwTDMPerfIntervalNumber.setStatus("current")
_TeaPwTDMPerfIntervalValidData_Type = TruthValue
_TeaPwTDMPerfIntervalValidData_Object = MibTableColumn
teaPwTDMPerfIntervalValidData = _TeaPwTDMPerfIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 7, 1, 2),
    _TeaPwTDMPerfIntervalValidData_Type()
)
teaPwTDMPerfIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfIntervalValidData.setStatus("current")
_TeaPwTDMPerfIntervalDuration_Type = Integer32
_TeaPwTDMPerfIntervalDuration_Object = MibTableColumn
teaPwTDMPerfIntervalDuration = _TeaPwTDMPerfIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 7, 1, 3),
    _TeaPwTDMPerfIntervalDuration_Type()
)
teaPwTDMPerfIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfIntervalDuration.setStatus("current")
_TeaPwTDMPerfIntervalMissingPkts_Type = PerfIntervalCount
_TeaPwTDMPerfIntervalMissingPkts_Object = MibTableColumn
teaPwTDMPerfIntervalMissingPkts = _TeaPwTDMPerfIntervalMissingPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 7, 1, 4),
    _TeaPwTDMPerfIntervalMissingPkts_Type()
)
teaPwTDMPerfIntervalMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfIntervalMissingPkts.setStatus("current")
_TeaPwTDMPerfIntervalPktsReOrder_Type = PerfIntervalCount
_TeaPwTDMPerfIntervalPktsReOrder_Object = MibTableColumn
teaPwTDMPerfIntervalPktsReOrder = _TeaPwTDMPerfIntervalPktsReOrder_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 7, 1, 5),
    _TeaPwTDMPerfIntervalPktsReOrder_Type()
)
teaPwTDMPerfIntervalPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfIntervalPktsReOrder.setStatus("current")
_TeaPwTDMPerfIntervalJtrBfrUnderruns_Type = PerfIntervalCount
_TeaPwTDMPerfIntervalJtrBfrUnderruns_Object = MibTableColumn
teaPwTDMPerfIntervalJtrBfrUnderruns = _TeaPwTDMPerfIntervalJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 7, 1, 6),
    _TeaPwTDMPerfIntervalJtrBfrUnderruns_Type()
)
teaPwTDMPerfIntervalJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfIntervalJtrBfrUnderruns.setStatus("current")
_TeaPwTDMPerfIntervalMisOrderDropped_Type = PerfIntervalCount
_TeaPwTDMPerfIntervalMisOrderDropped_Object = MibTableColumn
teaPwTDMPerfIntervalMisOrderDropped = _TeaPwTDMPerfIntervalMisOrderDropped_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 7, 1, 7),
    _TeaPwTDMPerfIntervalMisOrderDropped_Type()
)
teaPwTDMPerfIntervalMisOrderDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfIntervalMisOrderDropped.setStatus("current")
_TeaPwTDMPerfIntervalMalformedPkt_Type = PerfIntervalCount
_TeaPwTDMPerfIntervalMalformedPkt_Object = MibTableColumn
teaPwTDMPerfIntervalMalformedPkt = _TeaPwTDMPerfIntervalMalformedPkt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 7, 1, 8),
    _TeaPwTDMPerfIntervalMalformedPkt_Type()
)
teaPwTDMPerfIntervalMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfIntervalMalformedPkt.setStatus("current")
_TeaPwTDMPerfIntervalESs_Type = PerfIntervalCount
_TeaPwTDMPerfIntervalESs_Object = MibTableColumn
teaPwTDMPerfIntervalESs = _TeaPwTDMPerfIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 7, 1, 9),
    _TeaPwTDMPerfIntervalESs_Type()
)
teaPwTDMPerfIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfIntervalESs.setStatus("current")
_TeaPwTDMPerfIntervalSESs_Type = PerfIntervalCount
_TeaPwTDMPerfIntervalSESs_Object = MibTableColumn
teaPwTDMPerfIntervalSESs = _TeaPwTDMPerfIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 7, 1, 10),
    _TeaPwTDMPerfIntervalSESs_Type()
)
teaPwTDMPerfIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfIntervalSESs.setStatus("current")
_TeaPwTDMPerfIntervalUASs_Type = PerfIntervalCount
_TeaPwTDMPerfIntervalUASs_Object = MibTableColumn
teaPwTDMPerfIntervalUASs = _TeaPwTDMPerfIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 7, 1, 11),
    _TeaPwTDMPerfIntervalUASs_Type()
)
teaPwTDMPerfIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfIntervalUASs.setStatus("current")
_TeaPwTDMPerfIntervalFC_Type = PerfIntervalCount
_TeaPwTDMPerfIntervalFC_Object = MibTableColumn
teaPwTDMPerfIntervalFC = _TeaPwTDMPerfIntervalFC_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 7, 1, 12),
    _TeaPwTDMPerfIntervalFC_Type()
)
teaPwTDMPerfIntervalFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfIntervalFC.setStatus("current")
_TeaPwTDMPerfIntervalJtrBfrMin_Type = Unsigned32
_TeaPwTDMPerfIntervalJtrBfrMin_Object = MibTableColumn
teaPwTDMPerfIntervalJtrBfrMin = _TeaPwTDMPerfIntervalJtrBfrMin_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 7, 1, 13),
    _TeaPwTDMPerfIntervalJtrBfrMin_Type()
)
teaPwTDMPerfIntervalJtrBfrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfIntervalJtrBfrMin.setStatus("current")
_TeaPwTDMPerfIntervalJtrBfrMax_Type = Unsigned32
_TeaPwTDMPerfIntervalJtrBfrMax_Object = MibTableColumn
teaPwTDMPerfIntervalJtrBfrMax = _TeaPwTDMPerfIntervalJtrBfrMax_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 7, 1, 14),
    _TeaPwTDMPerfIntervalJtrBfrMax_Type()
)
teaPwTDMPerfIntervalJtrBfrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerfIntervalJtrBfrMax.setStatus("current")
_TeaPwTDMPerf1DayIntervalTable_Object = MibTable
teaPwTDMPerf1DayIntervalTable = _TeaPwTDMPerf1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 8)
)
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalTable.setStatus("current")
_TeaPwTDMPerf1DayIntervalEntry_Object = MibTableRow
teaPwTDMPerf1DayIntervalEntry = _TeaPwTDMPerf1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 8, 1)
)
teaPwTDMPerf1DayIntervalEntry.setIndexNames(
    (0, "CL-PW-MIB", "teaPwIndex"),
    (0, "CL-PW-TDM-MIB", "teaPwTDMPerf1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalEntry.setStatus("current")


class _TeaPwTDMPerf1DayIntervalNumber_Type(Unsigned32):
    """Custom type teaPwTDMPerf1DayIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_TeaPwTDMPerf1DayIntervalNumber_Type.__name__ = "Unsigned32"
_TeaPwTDMPerf1DayIntervalNumber_Object = MibTableColumn
teaPwTDMPerf1DayIntervalNumber = _TeaPwTDMPerf1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 8, 1, 1),
    _TeaPwTDMPerf1DayIntervalNumber_Type()
)
teaPwTDMPerf1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalNumber.setStatus("current")
_TeaPwTDMPerf1DayIntervalValidData_Type = TruthValue
_TeaPwTDMPerf1DayIntervalValidData_Object = MibTableColumn
teaPwTDMPerf1DayIntervalValidData = _TeaPwTDMPerf1DayIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 8, 1, 2),
    _TeaPwTDMPerf1DayIntervalValidData_Type()
)
teaPwTDMPerf1DayIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalValidData.setStatus("current")
_TeaPwTDMPerf1DayIntervalMoniSecs_Type = HCPerfTimeElapsed
_TeaPwTDMPerf1DayIntervalMoniSecs_Object = MibTableColumn
teaPwTDMPerf1DayIntervalMoniSecs = _TeaPwTDMPerf1DayIntervalMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 8, 1, 3),
    _TeaPwTDMPerf1DayIntervalMoniSecs_Type()
)
teaPwTDMPerf1DayIntervalMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalMoniSecs.setUnits("seconds")
_TeaPwTDMPerf1DayIntervalMissingPkts_Type = Counter32
_TeaPwTDMPerf1DayIntervalMissingPkts_Object = MibTableColumn
teaPwTDMPerf1DayIntervalMissingPkts = _TeaPwTDMPerf1DayIntervalMissingPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 8, 1, 4),
    _TeaPwTDMPerf1DayIntervalMissingPkts_Type()
)
teaPwTDMPerf1DayIntervalMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalMissingPkts.setStatus("current")
_TeaPwTDMPerf1DayIntervalPktsReOrder_Type = Counter32
_TeaPwTDMPerf1DayIntervalPktsReOrder_Object = MibTableColumn
teaPwTDMPerf1DayIntervalPktsReOrder = _TeaPwTDMPerf1DayIntervalPktsReOrder_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 8, 1, 5),
    _TeaPwTDMPerf1DayIntervalPktsReOrder_Type()
)
teaPwTDMPerf1DayIntervalPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalPktsReOrder.setStatus("current")
_TeaPwTDMPerf1DayIntervalJtrBfrUnderruns_Type = Counter32
_TeaPwTDMPerf1DayIntervalJtrBfrUnderruns_Object = MibTableColumn
teaPwTDMPerf1DayIntervalJtrBfrUnderruns = _TeaPwTDMPerf1DayIntervalJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 8, 1, 6),
    _TeaPwTDMPerf1DayIntervalJtrBfrUnderruns_Type()
)
teaPwTDMPerf1DayIntervalJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalJtrBfrUnderruns.setStatus("current")
_TeaPwTDMPerf1DayIntervalMisOrderDropped_Type = Counter32
_TeaPwTDMPerf1DayIntervalMisOrderDropped_Object = MibTableColumn
teaPwTDMPerf1DayIntervalMisOrderDropped = _TeaPwTDMPerf1DayIntervalMisOrderDropped_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 8, 1, 7),
    _TeaPwTDMPerf1DayIntervalMisOrderDropped_Type()
)
teaPwTDMPerf1DayIntervalMisOrderDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalMisOrderDropped.setStatus("current")
_TeaPwTDMPerf1DayIntervalMalformedPkt_Type = Counter32
_TeaPwTDMPerf1DayIntervalMalformedPkt_Object = MibTableColumn
teaPwTDMPerf1DayIntervalMalformedPkt = _TeaPwTDMPerf1DayIntervalMalformedPkt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 8, 1, 8),
    _TeaPwTDMPerf1DayIntervalMalformedPkt_Type()
)
teaPwTDMPerf1DayIntervalMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalMalformedPkt.setStatus("current")
_TeaPwTDMPerf1DayIntervalESs_Type = Counter32
_TeaPwTDMPerf1DayIntervalESs_Object = MibTableColumn
teaPwTDMPerf1DayIntervalESs = _TeaPwTDMPerf1DayIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 8, 1, 9),
    _TeaPwTDMPerf1DayIntervalESs_Type()
)
teaPwTDMPerf1DayIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalESs.setStatus("current")
_TeaPwTDMPerf1DayIntervalSESs_Type = Counter32
_TeaPwTDMPerf1DayIntervalSESs_Object = MibTableColumn
teaPwTDMPerf1DayIntervalSESs = _TeaPwTDMPerf1DayIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 8, 1, 10),
    _TeaPwTDMPerf1DayIntervalSESs_Type()
)
teaPwTDMPerf1DayIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalSESs.setStatus("current")
_TeaPwTDMPerf1DayIntervalUASs_Type = Counter32
_TeaPwTDMPerf1DayIntervalUASs_Object = MibTableColumn
teaPwTDMPerf1DayIntervalUASs = _TeaPwTDMPerf1DayIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 8, 1, 11),
    _TeaPwTDMPerf1DayIntervalUASs_Type()
)
teaPwTDMPerf1DayIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalUASs.setStatus("current")
_TeaPwTDMPerf1DayIntervalFC_Type = Counter32
_TeaPwTDMPerf1DayIntervalFC_Object = MibTableColumn
teaPwTDMPerf1DayIntervalFC = _TeaPwTDMPerf1DayIntervalFC_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 8, 1, 12),
    _TeaPwTDMPerf1DayIntervalFC_Type()
)
teaPwTDMPerf1DayIntervalFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalFC.setStatus("current")
_TeaPwTDMPerf1DayIntervalDiscontinuityTime_Type = TimeStamp
_TeaPwTDMPerf1DayIntervalDiscontinuityTime_Object = MibTableColumn
teaPwTDMPerf1DayIntervalDiscontinuityTime = _TeaPwTDMPerf1DayIntervalDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 8, 1, 13),
    _TeaPwTDMPerf1DayIntervalDiscontinuityTime_Type()
)
teaPwTDMPerf1DayIntervalDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalDiscontinuityTime.setStatus("current")
_TeaPwTDMPerf1DayIntervalJtrBfrMin_Type = Unsigned32
_TeaPwTDMPerf1DayIntervalJtrBfrMin_Object = MibTableColumn
teaPwTDMPerf1DayIntervalJtrBfrMin = _TeaPwTDMPerf1DayIntervalJtrBfrMin_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 8, 1, 14),
    _TeaPwTDMPerf1DayIntervalJtrBfrMin_Type()
)
teaPwTDMPerf1DayIntervalJtrBfrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalJtrBfrMin.setStatus("current")
_TeaPwTDMPerf1DayIntervalJtrBfrMax_Type = Unsigned32
_TeaPwTDMPerf1DayIntervalJtrBfrMax_Object = MibTableColumn
teaPwTDMPerf1DayIntervalJtrBfrMax = _TeaPwTDMPerf1DayIntervalJtrBfrMax_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 1, 8, 1, 15),
    _TeaPwTDMPerf1DayIntervalJtrBfrMax_Type()
)
teaPwTDMPerf1DayIntervalJtrBfrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalJtrBfrMax.setStatus("current")
_TeaPwTDMTraps_ObjectIdentity = ObjectIdentity
teaPwTDMTraps = _TeaPwTDMTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 2)
)
_TeaPwTDMConformance_ObjectIdentity = ObjectIdentity
teaPwTDMConformance = _TeaPwTDMConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 3)
)
_TeaPwTDMGroups_ObjectIdentity = ObjectIdentity
teaPwTDMGroups = _TeaPwTDMGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 3, 1)
)
_TeaPwTDMCompliances_ObjectIdentity = ObjectIdentity
teaPwTDMCompliances = _TeaPwTDMCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 3, 2)
)

# Managed Objects groups

teaPwTDMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 3, 1, 1)
)
teaPwTDMGroup.setObjects(
      *(("CL-PW-TDM-MIB", "teaPwTDMRate"),
        ("CL-PW-TDM-MIB", "teaPwTDMIfIndex"),
        ("CL-PW-TDM-MIB", "teaPwGenTDMCfgIndex"),
        ("CL-PW-TDM-MIB", "teaPwRelTDMCfgIndex"),
        ("CL-PW-TDM-MIB", "teaPwTDMConfigError"),
        ("CL-PW-TDM-MIB", "teaPwTDMTimeElapsed"),
        ("CL-PW-TDM-MIB", "teaPwTDMValidIntervals"),
        ("CL-PW-TDM-MIB", "teaPwTDMCurrentIndications"),
        ("CL-PW-TDM-MIB", "teaPwTDMLatchedIndications"),
        ("CL-PW-TDM-MIB", "teaPwTDMLastEsTimeStamp"),
        ("CL-PW-TDM-MIB", "teaPwTDMRtpSSRC"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgIndexNext"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgRowStatus"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgConfErr"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgPayloadSize"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgPktReorder"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgRtpHdrUsed"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgJtrBfrDepth"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgPayloadSuppression"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgConsecPktsInSynch"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgConsecMissPktsOutSynch"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgSetUp2SynchTimeOut"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgPktReplacePolicy"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgAvePktLossTimeWindow"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgExcessivePktLossThreshold"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgAlarmThreshold"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgClearAlarmThreshold"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgMissingPktsToSes"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgTimestampMode"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgStorageType"),
        ("CL-PW-TDM-MIB", "teaPwTMDCfgFillerPattern"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgLflagPayloadPolicy"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgIPTos"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgRtpPT"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgRtpTSRef"))
)
if mibBuilder.loadTexts:
    teaPwTDMGroup.setStatus("current")

teaPwTDMPerfCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 3, 1, 2)
)
teaPwTDMPerfCurrentGroup.setObjects(
      *(("CL-PW-TDM-MIB", "teaPwTDMPerfCurrentMissingPkts"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfCurrentPktsReOrder"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfCurrentJtrBfrUnderruns"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfCurrentMisOrderDropped"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfCurrentMalformedPkt"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfCurrentESs"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfCurrentSESs"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfCurrentUASs"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfCurrentFC"))
)
if mibBuilder.loadTexts:
    teaPwTDMPerfCurrentGroup.setStatus("current")

teaPwTDMPerfCurrentJtrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 3, 1, 3)
)
teaPwTDMPerfCurrentJtrGroup.setObjects(
      *(("CL-PW-TDM-MIB", "teaPwTDMPerfCurrentJtrBfrMin"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfCurrentJtrBfr"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfCurrentJtrBfrMax"))
)
if mibBuilder.loadTexts:
    teaPwTDMPerfCurrentJtrGroup.setStatus("current")

teaPwTDMPerfIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 3, 1, 4)
)
teaPwTDMPerfIntervalGroup.setObjects(
      *(("CL-PW-TDM-MIB", "teaPwTDMPerfIntervalValidData"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfIntervalDuration"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfIntervalMissingPkts"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfIntervalPktsReOrder"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfIntervalJtrBfrUnderruns"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfIntervalMisOrderDropped"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfIntervalMalformedPkt"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfIntervalESs"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfIntervalSESs"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfIntervalUASs"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfIntervalFC"))
)
if mibBuilder.loadTexts:
    teaPwTDMPerfIntervalGroup.setStatus("current")

teaPwTDMPerfIntervalJtrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 3, 1, 5)
)
teaPwTDMPerfIntervalJtrGroup.setObjects(
      *(("CL-PW-TDM-MIB", "teaPwTDMPerfIntervalJtrBfrMin"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfIntervalJtrBfrMax"))
)
if mibBuilder.loadTexts:
    teaPwTDMPerfIntervalJtrGroup.setStatus("current")

teaPwTDMCfgFramedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 3, 1, 6)
)
teaPwTDMCfgFramedGroup.setObjects(
      *(("CL-PW-TDM-MIB", "teaPwTDMCfgFramedRowStatus"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgFramedIdlePattern"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgFramedLflagPolicy"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgFramedRflagPolicy"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgFramedRDPolicy"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgFramedLopsPolicy"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgFramedSigIPTos"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgFramedSigPT"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgFramedSigIdle"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgFramedSigInterval"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgFramedSigMaxInterval"))
)
if mibBuilder.loadTexts:
    teaPwTDMCfgFramedGroup.setStatus("current")

teaPwTDMCfgPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 3, 1, 7)
)
teaPwTDMCfgPeerGroup.setObjects(
      *(("CL-PW-TDM-MIB", "teaPwTDMCfgPeerRtpTSRef"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgPeerRtpPT"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgFramedSigPeerPT"),
        ("CL-PW-TDM-MIB", "teaPwTDMPeerRtpSSRC"))
)
if mibBuilder.loadTexts:
    teaPwTDMCfgPeerGroup.setStatus("current")

teaPwRtpTDMCfgSRTPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 3, 1, 8)
)
teaPwRtpTDMCfgSRTPGroup.setObjects(
    ("CL-PW-TDM-MIB", "teaPwTDMCfgSRTPenable")
)
if mibBuilder.loadTexts:
    teaPwRtpTDMCfgSRTPGroup.setStatus("current")

teaPwTDMPerf1DayIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 3, 1, 9)
)
teaPwTDMPerf1DayIntervalGroup.setObjects(
      *(("CL-PW-TDM-MIB", "teaPwTDMPerf1DayIntervalValidData"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerf1DayIntervalMoniSecs"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerf1DayIntervalMissingPkts"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerf1DayIntervalPktsReOrder"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerf1DayIntervalJtrBfrUnderruns"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerf1DayIntervalMisOrderDropped"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerf1DayIntervalMalformedPkt"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerf1DayIntervalESs"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerf1DayIntervalSESs"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerf1DayIntervalUASs"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerf1DayIntervalFC"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerf1DayIntervalDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalGroup.setStatus("current")

teaPwTDMPerf1DayIntervalJtrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 3, 1, 10)
)
teaPwTDMPerf1DayIntervalJtrGroup.setObjects(
      *(("CL-PW-TDM-MIB", "teaPwTDMPerf1DayIntervalJtrBfrMin"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerf1DayIntervalJtrBfrMax"))
)
if mibBuilder.loadTexts:
    teaPwTDMPerf1DayIntervalJtrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bsodPwTDMModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 16, 3, 2, 1)
)
bsodPwTDMModuleCompliance.setObjects(
      *(("CL-PW-TDM-MIB", "teaPwTDMGroup"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfCurrentGroup"),
        ("CL-PW-TDM-MIB", "teaPwTDMPerfIntervalGroup"),
        ("CL-PW-TDM-MIB", "teaPwTDMCfgFramedGroup"))
)
if mibBuilder.loadTexts:
    bsodPwTDMModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CL-PW-TDM-MIB",
    **{"TeaPwTDMCfgIndex": TeaPwTDMCfgIndex,
       "teaPwTDMMIB": teaPwTDMMIB,
       "teaPwTDMObjects": teaPwTDMObjects,
       "teaPwTDMTable": teaPwTDMTable,
       "teaPwTDMEntry": teaPwTDMEntry,
       "teaPwTDMRate": teaPwTDMRate,
       "teaPwTDMIfIndex": teaPwTDMIfIndex,
       "teaPwGenTDMCfgIndex": teaPwGenTDMCfgIndex,
       "teaPwRelTDMCfgIndex": teaPwRelTDMCfgIndex,
       "teaPwTDMConfigError": teaPwTDMConfigError,
       "teaPwTDMTimeElapsed": teaPwTDMTimeElapsed,
       "teaPwTDMValidIntervals": teaPwTDMValidIntervals,
       "teaPwTDMCurrentIndications": teaPwTDMCurrentIndications,
       "teaPwTDMLatchedIndications": teaPwTDMLatchedIndications,
       "teaPwTDMLastEsTimeStamp": teaPwTDMLastEsTimeStamp,
       "teaPwTDMRtpSSRC": teaPwTDMRtpSSRC,
       "teaPwTDMPeerRtpSSRC": teaPwTDMPeerRtpSSRC,
       "teaPwTDMCfgIndexNext": teaPwTDMCfgIndexNext,
       "teaPwTDMCfgTable": teaPwTDMCfgTable,
       "teaPwTDMCfgEntry": teaPwTDMCfgEntry,
       "teaPwTDMCfgIndex": teaPwTDMCfgIndex,
       "teaPwTDMCfgRowStatus": teaPwTDMCfgRowStatus,
       "teaPwTDMCfgConfErr": teaPwTDMCfgConfErr,
       "teaPwTDMCfgPayloadSize": teaPwTDMCfgPayloadSize,
       "teaPwTDMCfgPktReorder": teaPwTDMCfgPktReorder,
       "teaPwTDMCfgRtpHdrUsed": teaPwTDMCfgRtpHdrUsed,
       "teaPwTDMCfgJtrBfrDepth": teaPwTDMCfgJtrBfrDepth,
       "teaPwTDMCfgPayloadSuppression": teaPwTDMCfgPayloadSuppression,
       "teaPwTDMCfgConsecPktsInSynch": teaPwTDMCfgConsecPktsInSynch,
       "teaPwTDMCfgConsecMissPktsOutSynch": teaPwTDMCfgConsecMissPktsOutSynch,
       "teaPwTDMCfgSetUp2SynchTimeOut": teaPwTDMCfgSetUp2SynchTimeOut,
       "teaPwTDMCfgPktReplacePolicy": teaPwTDMCfgPktReplacePolicy,
       "teaPwTDMCfgAvePktLossTimeWindow": teaPwTDMCfgAvePktLossTimeWindow,
       "teaPwTDMCfgExcessivePktLossThreshold": teaPwTDMCfgExcessivePktLossThreshold,
       "teaPwTDMCfgAlarmThreshold": teaPwTDMCfgAlarmThreshold,
       "teaPwTDMCfgClearAlarmThreshold": teaPwTDMCfgClearAlarmThreshold,
       "teaPwTDMCfgMissingPktsToSes": teaPwTDMCfgMissingPktsToSes,
       "teaPwTDMCfgTimestampMode": teaPwTDMCfgTimestampMode,
       "teaPwTDMCfgStorageType": teaPwTDMCfgStorageType,
       "teaPwTMDCfgFillerPattern": teaPwTMDCfgFillerPattern,
       "teaPwTDMCfgLflagPayloadPolicy": teaPwTDMCfgLflagPayloadPolicy,
       "teaPwTDMCfgIPTos": teaPwTDMCfgIPTos,
       "teaPwTDMCfgRtpPT": teaPwTDMCfgRtpPT,
       "teaPwTDMCfgPeerRtpPT": teaPwTDMCfgPeerRtpPT,
       "teaPwTDMCfgRtpTSRef": teaPwTDMCfgRtpTSRef,
       "teaPwTDMCfgPeerRtpTSRef": teaPwTDMCfgPeerRtpTSRef,
       "teaPwTDMCfgSRTPenable": teaPwTDMCfgSRTPenable,
       "teaPwTDMCfgFramedIndexNext": teaPwTDMCfgFramedIndexNext,
       "teaPwTDMCfgFramedTable": teaPwTDMCfgFramedTable,
       "teaPwTDMCfgFramedEntry": teaPwTDMCfgFramedEntry,
       "teaPwTDMCfgFramedIndex": teaPwTDMCfgFramedIndex,
       "teaPwTDMCfgFramedRowStatus": teaPwTDMCfgFramedRowStatus,
       "teaPwTDMCfgFramedIdlePattern": teaPwTDMCfgFramedIdlePattern,
       "teaPwTDMCfgFramedLflagPolicy": teaPwTDMCfgFramedLflagPolicy,
       "teaPwTDMCfgFramedRflagPolicy": teaPwTDMCfgFramedRflagPolicy,
       "teaPwTDMCfgFramedRDPolicy": teaPwTDMCfgFramedRDPolicy,
       "teaPwTDMCfgFramedLopsPolicy": teaPwTDMCfgFramedLopsPolicy,
       "teaPwTDMCfgFramedSigIPTos": teaPwTDMCfgFramedSigIPTos,
       "teaPwTDMCfgFramedSigPT": teaPwTDMCfgFramedSigPT,
       "teaPwTDMCfgFramedSigPeerPT": teaPwTDMCfgFramedSigPeerPT,
       "teaPwTDMCfgFramedSigIdle": teaPwTDMCfgFramedSigIdle,
       "teaPwTDMCfgFramedSigInterval": teaPwTDMCfgFramedSigInterval,
       "teaPwTDMCfgFramedSigMaxInterval": teaPwTDMCfgFramedSigMaxInterval,
       "teaPwTDMPerfCurrentTable": teaPwTDMPerfCurrentTable,
       "teaPwTDMPerfCurrentEntry": teaPwTDMPerfCurrentEntry,
       "teaPwTDMPerfCurrentMissingPkts": teaPwTDMPerfCurrentMissingPkts,
       "teaPwTDMPerfCurrentPktsReOrder": teaPwTDMPerfCurrentPktsReOrder,
       "teaPwTDMPerfCurrentJtrBfrUnderruns": teaPwTDMPerfCurrentJtrBfrUnderruns,
       "teaPwTDMPerfCurrentMisOrderDropped": teaPwTDMPerfCurrentMisOrderDropped,
       "teaPwTDMPerfCurrentMalformedPkt": teaPwTDMPerfCurrentMalformedPkt,
       "teaPwTDMPerfCurrentESs": teaPwTDMPerfCurrentESs,
       "teaPwTDMPerfCurrentSESs": teaPwTDMPerfCurrentSESs,
       "teaPwTDMPerfCurrentUASs": teaPwTDMPerfCurrentUASs,
       "teaPwTDMPerfCurrentFC": teaPwTDMPerfCurrentFC,
       "teaPwTDMPerfCurrentJtrBfrMin": teaPwTDMPerfCurrentJtrBfrMin,
       "teaPwTDMPerfCurrentJtrBfr": teaPwTDMPerfCurrentJtrBfr,
       "teaPwTDMPerfCurrentJtrBfrMax": teaPwTDMPerfCurrentJtrBfrMax,
       "teaPwTDMPerfIntervalTable": teaPwTDMPerfIntervalTable,
       "teaPwTDMPerfIntervalEntry": teaPwTDMPerfIntervalEntry,
       "teaPwTDMPerfIntervalNumber": teaPwTDMPerfIntervalNumber,
       "teaPwTDMPerfIntervalValidData": teaPwTDMPerfIntervalValidData,
       "teaPwTDMPerfIntervalDuration": teaPwTDMPerfIntervalDuration,
       "teaPwTDMPerfIntervalMissingPkts": teaPwTDMPerfIntervalMissingPkts,
       "teaPwTDMPerfIntervalPktsReOrder": teaPwTDMPerfIntervalPktsReOrder,
       "teaPwTDMPerfIntervalJtrBfrUnderruns": teaPwTDMPerfIntervalJtrBfrUnderruns,
       "teaPwTDMPerfIntervalMisOrderDropped": teaPwTDMPerfIntervalMisOrderDropped,
       "teaPwTDMPerfIntervalMalformedPkt": teaPwTDMPerfIntervalMalformedPkt,
       "teaPwTDMPerfIntervalESs": teaPwTDMPerfIntervalESs,
       "teaPwTDMPerfIntervalSESs": teaPwTDMPerfIntervalSESs,
       "teaPwTDMPerfIntervalUASs": teaPwTDMPerfIntervalUASs,
       "teaPwTDMPerfIntervalFC": teaPwTDMPerfIntervalFC,
       "teaPwTDMPerfIntervalJtrBfrMin": teaPwTDMPerfIntervalJtrBfrMin,
       "teaPwTDMPerfIntervalJtrBfrMax": teaPwTDMPerfIntervalJtrBfrMax,
       "teaPwTDMPerf1DayIntervalTable": teaPwTDMPerf1DayIntervalTable,
       "teaPwTDMPerf1DayIntervalEntry": teaPwTDMPerf1DayIntervalEntry,
       "teaPwTDMPerf1DayIntervalNumber": teaPwTDMPerf1DayIntervalNumber,
       "teaPwTDMPerf1DayIntervalValidData": teaPwTDMPerf1DayIntervalValidData,
       "teaPwTDMPerf1DayIntervalMoniSecs": teaPwTDMPerf1DayIntervalMoniSecs,
       "teaPwTDMPerf1DayIntervalMissingPkts": teaPwTDMPerf1DayIntervalMissingPkts,
       "teaPwTDMPerf1DayIntervalPktsReOrder": teaPwTDMPerf1DayIntervalPktsReOrder,
       "teaPwTDMPerf1DayIntervalJtrBfrUnderruns": teaPwTDMPerf1DayIntervalJtrBfrUnderruns,
       "teaPwTDMPerf1DayIntervalMisOrderDropped": teaPwTDMPerf1DayIntervalMisOrderDropped,
       "teaPwTDMPerf1DayIntervalMalformedPkt": teaPwTDMPerf1DayIntervalMalformedPkt,
       "teaPwTDMPerf1DayIntervalESs": teaPwTDMPerf1DayIntervalESs,
       "teaPwTDMPerf1DayIntervalSESs": teaPwTDMPerf1DayIntervalSESs,
       "teaPwTDMPerf1DayIntervalUASs": teaPwTDMPerf1DayIntervalUASs,
       "teaPwTDMPerf1DayIntervalFC": teaPwTDMPerf1DayIntervalFC,
       "teaPwTDMPerf1DayIntervalDiscontinuityTime": teaPwTDMPerf1DayIntervalDiscontinuityTime,
       "teaPwTDMPerf1DayIntervalJtrBfrMin": teaPwTDMPerf1DayIntervalJtrBfrMin,
       "teaPwTDMPerf1DayIntervalJtrBfrMax": teaPwTDMPerf1DayIntervalJtrBfrMax,
       "teaPwTDMTraps": teaPwTDMTraps,
       "teaPwTDMConformance": teaPwTDMConformance,
       "teaPwTDMGroups": teaPwTDMGroups,
       "teaPwTDMGroup": teaPwTDMGroup,
       "teaPwTDMPerfCurrentGroup": teaPwTDMPerfCurrentGroup,
       "teaPwTDMPerfCurrentJtrGroup": teaPwTDMPerfCurrentJtrGroup,
       "teaPwTDMPerfIntervalGroup": teaPwTDMPerfIntervalGroup,
       "teaPwTDMPerfIntervalJtrGroup": teaPwTDMPerfIntervalJtrGroup,
       "teaPwTDMCfgFramedGroup": teaPwTDMCfgFramedGroup,
       "teaPwTDMCfgPeerGroup": teaPwTDMCfgPeerGroup,
       "teaPwRtpTDMCfgSRTPGroup": teaPwRtpTDMCfgSRTPGroup,
       "teaPwTDMPerf1DayIntervalGroup": teaPwTDMPerf1DayIntervalGroup,
       "teaPwTDMPerf1DayIntervalJtrGroup": teaPwTDMPerf1DayIntervalJtrGroup,
       "teaPwTDMCompliances": teaPwTDMCompliances,
       "bsodPwTDMModuleCompliance": bsodPwTDMModuleCompliance}
)
