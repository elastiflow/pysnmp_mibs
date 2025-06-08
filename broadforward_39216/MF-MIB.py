# SNMP MIB module (MF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/broadforward_39216/MF-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:58:58 2025
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

mfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39216, 1)
)
if mibBuilder.loadTexts:
    mfMib.setRevisions(
        ("2012-01-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdminStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1),
          ("destroy", 2),
          ("reload", 3))
    )



class OperationalStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1),
          ("loading", 2),
          ("stopping", 3))
    )



class ReloadAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("read", 1),
          ("dump", 2))
    )



class TraceLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("critical", 1),
          ("error", 2),
          ("warning", 3),
          ("notice", 4),
          ("info", 5),
          ("debug", 6))
    )



class LogLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("critical", 1),
          ("error", 2),
          ("warning", 3),
          ("notice", 4),
          ("info", 5),
          ("debug", 6))
    )



class RateUnit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tps", 0),
          ("tpm", 1),
          ("tph", 2))
    )



# MIB Managed Objects in the order of their OIDs

_MfInfo_ObjectIdentity = ObjectIdentity
mfInfo = _MfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39216, 1, 1)
)
_ServerName_Type = DisplayString
_ServerName_Object = MibScalar
serverName = _ServerName_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 1, 1),
    _ServerName_Type()
)
serverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverName.setStatus("current")
_TraceLevel_Type = TraceLevel
_TraceLevel_Object = MibScalar
traceLevel = _TraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 1, 2),
    _TraceLevel_Type()
)
traceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceLevel.setStatus("current")
_LastRestart_Type = Unsigned32
_LastRestart_Object = MibScalar
lastRestart = _LastRestart_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 1, 3),
    _LastRestart_Type()
)
lastRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastRestart.setStatus("current")
_LogLevel_Type = LogLevel
_LogLevel_Object = MibScalar
logLevel = _LogLevel_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 1, 4),
    _LogLevel_Type()
)
logLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logLevel.setStatus("current")


class _Severity_Type(Integer32):
    """Custom type severity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("info", 1),
          ("minor", 2),
          ("warning", 3),
          ("major", 4),
          ("critical", 5))
    )


_Severity_Type.__name__ = "Integer32"
_Severity_Object = MibScalar
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 1, 5),
    _Severity_Type()
)
severity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    severity.setStatus("current")
_CbNodeIp_Type = DisplayString
_CbNodeIp_Object = MibScalar
cbNodeIp = _CbNodeIp_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 1, 6),
    _CbNodeIp_Type()
)
cbNodeIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cbNodeIp.setStatus("current")
_CbNodeName_Type = DisplayString
_CbNodeName_Object = MibScalar
cbNodeName = _CbNodeName_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 1, 7),
    _CbNodeName_Type()
)
cbNodeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cbNodeName.setStatus("current")
_CbNodeStatus_Type = DisplayString
_CbNodeStatus_Object = MibScalar
cbNodeStatus = _CbNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 1, 8),
    _CbNodeStatus_Type()
)
cbNodeStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cbNodeStatus.setStatus("current")
_AdminStatus_Type = AdminStatus
_AdminStatus_Object = MibScalar
adminStatus = _AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 1, 9),
    _AdminStatus_Type()
)
adminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminStatus.setStatus("current")
_MfStatus_ObjectIdentity = ObjectIdentity
mfStatus = _MfStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2)
)
_TotalTxCount_Type = Counter64
_TotalTxCount_Object = MibScalar
totalTxCount = _TotalTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 1),
    _TotalTxCount_Type()
)
totalTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    totalTxCount.setStatus("current")
_SuccessTxCount_Type = Counter64
_SuccessTxCount_Object = MibScalar
successTxCount = _SuccessTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 2),
    _SuccessTxCount_Type()
)
successTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTxCount.setStatus("current")
_FailedTxCount_Type = Counter64
_FailedTxCount_Object = MibScalar
failedTxCount = _FailedTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 3),
    _FailedTxCount_Type()
)
failedTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failedTxCount.setStatus("current")
_FailedProcessTxCount_Type = Counter64
_FailedProcessTxCount_Object = MibScalar
failedProcessTxCount = _FailedProcessTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 4),
    _FailedProcessTxCount_Type()
)
failedProcessTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failedProcessTxCount.setStatus("current")
_FailedDroppedTxCount_Type = Counter64
_FailedDroppedTxCount_Object = MibScalar
failedDroppedTxCount = _FailedDroppedTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 5),
    _FailedDroppedTxCount_Type()
)
failedDroppedTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failedDroppedTxCount.setStatus("current")
_FailedShutdownTxCount_Type = Counter64
_FailedShutdownTxCount_Object = MibScalar
failedShutdownTxCount = _FailedShutdownTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 6),
    _FailedShutdownTxCount_Type()
)
failedShutdownTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failedShutdownTxCount.setStatus("current")
_FailedUnknownFlowTxCount_Type = Counter64
_FailedUnknownFlowTxCount_Object = MibScalar
failedUnknownFlowTxCount = _FailedUnknownFlowTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 7),
    _FailedUnknownFlowTxCount_Type()
)
failedUnknownFlowTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failedUnknownFlowTxCount.setStatus("current")
_FailedTimeoutTxCount_Type = Counter64
_FailedTimeoutTxCount_Object = MibScalar
failedTimeoutTxCount = _FailedTimeoutTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 8),
    _FailedTimeoutTxCount_Type()
)
failedTimeoutTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failedTimeoutTxCount.setStatus("current")
_FailedCongestionTxCount_Type = Counter64
_FailedCongestionTxCount_Object = MibScalar
failedCongestionTxCount = _FailedCongestionTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 9),
    _FailedCongestionTxCount_Type()
)
failedCongestionTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failedCongestionTxCount.setStatus("current")
_RejectIngressTxCount_Type = Counter64
_RejectIngressTxCount_Object = MibScalar
rejectIngressTxCount = _RejectIngressTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 10),
    _RejectIngressTxCount_Type()
)
rejectIngressTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rejectIngressTxCount.setStatus("current")
_ActivateFlow_Type = DisplayString
_ActivateFlow_Object = MibScalar
activateFlow = _ActivateFlow_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 15),
    _ActivateFlow_Type()
)
activateFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activateFlow.setStatus("current")
_LastErrorReason_Type = DisplayString
_LastErrorReason_Object = MibScalar
lastErrorReason = _LastErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 16),
    _LastErrorReason_Type()
)
lastErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastErrorReason.setStatus("current")
_ActivateRRule_Type = DisplayString
_ActivateRRule_Object = MibScalar
activateRRule = _ActivateRRule_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 17),
    _ActivateRRule_Type()
)
activateRRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activateRRule.setStatus("current")
_QueueSize_Type = Integer32
_QueueSize_Object = MibScalar
queueSize = _QueueSize_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 18),
    _QueueSize_Type()
)
queueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueSize.setStatus("current")
_QueueSizeB_Type = Integer32
_QueueSizeB_Object = MibScalar
queueSizeB = _QueueSizeB_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 19),
    _QueueSizeB_Type()
)
queueSizeB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueSizeB.setStatus("current")
_FlowTable_Object = MibTable
flowTable = _FlowTable_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20)
)
if mibBuilder.loadTexts:
    flowTable.setStatus("current")
_FlowEntry_Object = MibTableRow
flowEntry = _FlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1)
)
flowEntry.setIndexNames(
    (0, "MF-MIB", "flowIndex"),
)
if mibBuilder.loadTexts:
    flowEntry.setStatus("current")


class _FlowIndex_Type(Integer32):
    """Custom type flowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlowIndex_Type.__name__ = "Integer32"
_FlowIndex_Object = MibTableColumn
flowIndex = _FlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 1),
    _FlowIndex_Type()
)
flowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowIndex.setStatus("current")
_FlowAdminStatus_Type = AdminStatus
_FlowAdminStatus_Object = MibTableColumn
flowAdminStatus = _FlowAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 2),
    _FlowAdminStatus_Type()
)
flowAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowAdminStatus.setStatus("current")
_FlowName_Type = DisplayString
_FlowName_Object = MibTableColumn
flowName = _FlowName_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 3),
    _FlowName_Type()
)
flowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowName.setStatus("current")
_FlowDescription_Type = DisplayString
_FlowDescription_Object = MibTableColumn
flowDescription = _FlowDescription_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 4),
    _FlowDescription_Type()
)
flowDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDescription.setStatus("current")
_FlowLastActivatedOn_Type = Unsigned32
_FlowLastActivatedOn_Object = MibTableColumn
flowLastActivatedOn = _FlowLastActivatedOn_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 5),
    _FlowLastActivatedOn_Type()
)
flowLastActivatedOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowLastActivatedOn.setStatus("current")
_FlowTxBeingProcessed_Type = Gauge32
_FlowTxBeingProcessed_Object = MibTableColumn
flowTxBeingProcessed = _FlowTxBeingProcessed_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 6),
    _FlowTxBeingProcessed_Type()
)
flowTxBeingProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowTxBeingProcessed.setStatus("current")
_FlowOperationalStatus_Type = OperationalStatus
_FlowOperationalStatus_Object = MibTableColumn
flowOperationalStatus = _FlowOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 7),
    _FlowOperationalStatus_Type()
)
flowOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowOperationalStatus.setStatus("current")
_FlowLogLevel_Type = LogLevel
_FlowLogLevel_Object = MibTableColumn
flowLogLevel = _FlowLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 8),
    _FlowLogLevel_Type()
)
flowLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowLogLevel.setStatus("current")
_FlowTotalTxCount_Type = Counter64
_FlowTotalTxCount_Object = MibTableColumn
flowTotalTxCount = _FlowTotalTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 11),
    _FlowTotalTxCount_Type()
)
flowTotalTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowTotalTxCount.setStatus("current")
_FlowSuccessTxCount_Type = Counter64
_FlowSuccessTxCount_Object = MibTableColumn
flowSuccessTxCount = _FlowSuccessTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 12),
    _FlowSuccessTxCount_Type()
)
flowSuccessTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowSuccessTxCount.setStatus("current")
_FlowFailedTxCount_Type = Counter64
_FlowFailedTxCount_Object = MibTableColumn
flowFailedTxCount = _FlowFailedTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 13),
    _FlowFailedTxCount_Type()
)
flowFailedTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowFailedTxCount.setStatus("current")
_FlowFailedProcessTxCount_Type = Counter64
_FlowFailedProcessTxCount_Object = MibTableColumn
flowFailedProcessTxCount = _FlowFailedProcessTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 14),
    _FlowFailedProcessTxCount_Type()
)
flowFailedProcessTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowFailedProcessTxCount.setStatus("current")
_FlowFailedDroppedTxCount_Type = Counter64
_FlowFailedDroppedTxCount_Object = MibTableColumn
flowFailedDroppedTxCount = _FlowFailedDroppedTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 15),
    _FlowFailedDroppedTxCount_Type()
)
flowFailedDroppedTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowFailedDroppedTxCount.setStatus("current")
_FlowFailedShutdownTxCount_Type = Counter64
_FlowFailedShutdownTxCount_Object = MibTableColumn
flowFailedShutdownTxCount = _FlowFailedShutdownTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 16),
    _FlowFailedShutdownTxCount_Type()
)
flowFailedShutdownTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowFailedShutdownTxCount.setStatus("current")
_FlowFailedTimeoutTxCount_Type = Counter64
_FlowFailedTimeoutTxCount_Object = MibTableColumn
flowFailedTimeoutTxCount = _FlowFailedTimeoutTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 17),
    _FlowFailedTimeoutTxCount_Type()
)
flowFailedTimeoutTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowFailedTimeoutTxCount.setStatus("current")
_FlowFailedCongestionTxCount_Type = Counter64
_FlowFailedCongestionTxCount_Object = MibTableColumn
flowFailedCongestionTxCount = _FlowFailedCongestionTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 18),
    _FlowFailedCongestionTxCount_Type()
)
flowFailedCongestionTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowFailedCongestionTxCount.setStatus("current")
_FlowRejectIngressTxCount_Type = Counter64
_FlowRejectIngressTxCount_Object = MibTableColumn
flowRejectIngressTxCount = _FlowRejectIngressTxCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 19),
    _FlowRejectIngressTxCount_Type()
)
flowRejectIngressTxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowRejectIngressTxCount.setStatus("current")
_FlowMinimumTotalTxDelay_Type = Gauge32
_FlowMinimumTotalTxDelay_Object = MibTableColumn
flowMinimumTotalTxDelay = _FlowMinimumTotalTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 31),
    _FlowMinimumTotalTxDelay_Type()
)
flowMinimumTotalTxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowMinimumTotalTxDelay.setStatus("current")
_FlowMaximumTotalTxDelay_Type = Gauge32
_FlowMaximumTotalTxDelay_Object = MibTableColumn
flowMaximumTotalTxDelay = _FlowMaximumTotalTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 32),
    _FlowMaximumTotalTxDelay_Type()
)
flowMaximumTotalTxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowMaximumTotalTxDelay.setStatus("current")
_FlowAverageTotalTxDelay_Type = Gauge32
_FlowAverageTotalTxDelay_Object = MibTableColumn
flowAverageTotalTxDelay = _FlowAverageTotalTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 33),
    _FlowAverageTotalTxDelay_Type()
)
flowAverageTotalTxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowAverageTotalTxDelay.setStatus("current")
_FlowPercentageBelow5msec_Type = Gauge32
_FlowPercentageBelow5msec_Object = MibTableColumn
flowPercentageBelow5msec = _FlowPercentageBelow5msec_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 34),
    _FlowPercentageBelow5msec_Type()
)
flowPercentageBelow5msec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowPercentageBelow5msec.setStatus("current")
_FlowPercentageBelow10msec_Type = Gauge32
_FlowPercentageBelow10msec_Object = MibTableColumn
flowPercentageBelow10msec = _FlowPercentageBelow10msec_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 20, 1, 35),
    _FlowPercentageBelow10msec_Type()
)
flowPercentageBelow10msec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowPercentageBelow10msec.setStatus("current")
_QueuedMsgGauge_Type = Gauge32
_QueuedMsgGauge_Object = MibScalar
queuedMsgGauge = _QueuedMsgGauge_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 21),
    _QueuedMsgGauge_Type()
)
queuedMsgGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queuedMsgGauge.setStatus("current")
_HighestQueuedMsgGauge_Type = Gauge32
_HighestQueuedMsgGauge_Object = MibScalar
highestQueuedMsgGauge = _HighestQueuedMsgGauge_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 22),
    _HighestQueuedMsgGauge_Type()
)
highestQueuedMsgGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highestQueuedMsgGauge.setStatus("current")
_QueuedMsgGaugeB_Type = Gauge32
_QueuedMsgGaugeB_Object = MibScalar
queuedMsgGaugeB = _QueuedMsgGaugeB_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 23),
    _QueuedMsgGaugeB_Type()
)
queuedMsgGaugeB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queuedMsgGaugeB.setStatus("current")
_HighestQueuedMsgGaugeB_Type = Gauge32
_HighestQueuedMsgGaugeB_Object = MibScalar
highestQueuedMsgGaugeB = _HighestQueuedMsgGaugeB_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 24),
    _HighestQueuedMsgGaugeB_Type()
)
highestQueuedMsgGaugeB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highestQueuedMsgGaugeB.setStatus("current")
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("current")
_ModuleEntry_Object = MibTableRow
moduleEntry = _ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1)
)
moduleEntry.setIndexNames(
    (0, "MF-MIB", "moduleIndex"),
)
if mibBuilder.loadTexts:
    moduleEntry.setStatus("current")


class _ModuleIndex_Type(Integer32):
    """Custom type moduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ModuleIndex_Type.__name__ = "Integer32"
_ModuleIndex_Object = MibTableColumn
moduleIndex = _ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 1),
    _ModuleIndex_Type()
)
moduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    moduleIndex.setStatus("current")
_ModuleName_Type = DisplayString
_ModuleName_Object = MibTableColumn
moduleName = _ModuleName_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 2),
    _ModuleName_Type()
)
moduleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleName.setStatus("current")
_ModuleDescription_Type = DisplayString
_ModuleDescription_Object = MibTableColumn
moduleDescription = _ModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 3),
    _ModuleDescription_Type()
)
moduleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDescription.setStatus("current")
_ModuleQueueSize_Type = Integer32
_ModuleQueueSize_Object = MibTableColumn
moduleQueueSize = _ModuleQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 4),
    _ModuleQueueSize_Type()
)
moduleQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleQueueSize.setStatus("current")
_ModuleReloadConfig_Type = Integer32
_ModuleReloadConfig_Object = MibTableColumn
moduleReloadConfig = _ModuleReloadConfig_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 5),
    _ModuleReloadConfig_Type()
)
moduleReloadConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleReloadConfig.setStatus("current")
_ModuleLogLevel_Type = LogLevel
_ModuleLogLevel_Object = MibTableColumn
moduleLogLevel = _ModuleLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 6),
    _ModuleLogLevel_Type()
)
moduleLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleLogLevel.setStatus("current")
_ModuleWorkerThreads_Type = Integer32
_ModuleWorkerThreads_Object = MibTableColumn
moduleWorkerThreads = _ModuleWorkerThreads_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 7),
    _ModuleWorkerThreads_Type()
)
moduleWorkerThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleWorkerThreads.setStatus("current")
_ModuleVersion_Type = DisplayString
_ModuleVersion_Object = MibTableColumn
moduleVersion = _ModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 8),
    _ModuleVersion_Type()
)
moduleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleVersion.setStatus("current")
_ModuleQueueSizeB_Type = Integer32
_ModuleQueueSizeB_Object = MibTableColumn
moduleQueueSizeB = _ModuleQueueSizeB_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 9),
    _ModuleQueueSizeB_Type()
)
moduleQueueSizeB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleQueueSizeB.setStatus("current")
_ModuleTotalMsgCount_Type = Counter64
_ModuleTotalMsgCount_Object = MibTableColumn
moduleTotalMsgCount = _ModuleTotalMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 11),
    _ModuleTotalMsgCount_Type()
)
moduleTotalMsgCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleTotalMsgCount.setStatus("current")
_ModuleSuccessMsgCount_Type = Counter64
_ModuleSuccessMsgCount_Object = MibTableColumn
moduleSuccessMsgCount = _ModuleSuccessMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 12),
    _ModuleSuccessMsgCount_Type()
)
moduleSuccessMsgCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleSuccessMsgCount.setStatus("current")
_ModuleFailedMsgCount_Type = Counter64
_ModuleFailedMsgCount_Object = MibTableColumn
moduleFailedMsgCount = _ModuleFailedMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 13),
    _ModuleFailedMsgCount_Type()
)
moduleFailedMsgCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleFailedMsgCount.setStatus("current")
_ModuleFailedUnknownFlowMsgCount_Type = Counter64
_ModuleFailedUnknownFlowMsgCount_Object = MibTableColumn
moduleFailedUnknownFlowMsgCount = _ModuleFailedUnknownFlowMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 14),
    _ModuleFailedUnknownFlowMsgCount_Type()
)
moduleFailedUnknownFlowMsgCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleFailedUnknownFlowMsgCount.setStatus("current")
_ModuleFailedTimeoutMsgCount_Type = Counter64
_ModuleFailedTimeoutMsgCount_Object = MibTableColumn
moduleFailedTimeoutMsgCount = _ModuleFailedTimeoutMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 15),
    _ModuleFailedTimeoutMsgCount_Type()
)
moduleFailedTimeoutMsgCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleFailedTimeoutMsgCount.setStatus("current")
_ModuleFailedCongestionMsgCount_Type = Counter64
_ModuleFailedCongestionMsgCount_Object = MibTableColumn
moduleFailedCongestionMsgCount = _ModuleFailedCongestionMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 16),
    _ModuleFailedCongestionMsgCount_Type()
)
moduleFailedCongestionMsgCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleFailedCongestionMsgCount.setStatus("current")
_ModuleFailedProcessingMsgCount_Type = Counter64
_ModuleFailedProcessingMsgCount_Object = MibTableColumn
moduleFailedProcessingMsgCount = _ModuleFailedProcessingMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 17),
    _ModuleFailedProcessingMsgCount_Type()
)
moduleFailedProcessingMsgCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleFailedProcessingMsgCount.setStatus("current")
_ModuleFailedDroppedMsgCount_Type = Counter64
_ModuleFailedDroppedMsgCount_Object = MibTableColumn
moduleFailedDroppedMsgCount = _ModuleFailedDroppedMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 18),
    _ModuleFailedDroppedMsgCount_Type()
)
moduleFailedDroppedMsgCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleFailedDroppedMsgCount.setStatus("current")
_ModuleRejectIngressMsgCount_Type = Counter64
_ModuleRejectIngressMsgCount_Object = MibTableColumn
moduleRejectIngressMsgCount = _ModuleRejectIngressMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 19),
    _ModuleRejectIngressMsgCount_Type()
)
moduleRejectIngressMsgCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleRejectIngressMsgCount.setStatus("current")
_ModuleQueuedMsgGauge_Type = Gauge32
_ModuleQueuedMsgGauge_Object = MibTableColumn
moduleQueuedMsgGauge = _ModuleQueuedMsgGauge_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 21),
    _ModuleQueuedMsgGauge_Type()
)
moduleQueuedMsgGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleQueuedMsgGauge.setStatus("current")
_ModuleHighestQueuedMsgGauge_Type = Gauge32
_ModuleHighestQueuedMsgGauge_Object = MibTableColumn
moduleHighestQueuedMsgGauge = _ModuleHighestQueuedMsgGauge_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 22),
    _ModuleHighestQueuedMsgGauge_Type()
)
moduleHighestQueuedMsgGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleHighestQueuedMsgGauge.setStatus("current")
_ModuleQueuedMsgGaugeB_Type = Gauge32
_ModuleQueuedMsgGaugeB_Object = MibTableColumn
moduleQueuedMsgGaugeB = _ModuleQueuedMsgGaugeB_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 23),
    _ModuleQueuedMsgGaugeB_Type()
)
moduleQueuedMsgGaugeB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleQueuedMsgGaugeB.setStatus("current")
_ModuleHighestQueuedMsgGaugeB_Type = Gauge32
_ModuleHighestQueuedMsgGaugeB_Object = MibTableColumn
moduleHighestQueuedMsgGaugeB = _ModuleHighestQueuedMsgGaugeB_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 25, 1, 24),
    _ModuleHighestQueuedMsgGaugeB_Type()
)
moduleHighestQueuedMsgGaugeB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleHighestQueuedMsgGaugeB.setStatus("current")
_RruleTable_Object = MibTable
rruleTable = _RruleTable_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 30)
)
if mibBuilder.loadTexts:
    rruleTable.setStatus("current")
_RruleEntry_Object = MibTableRow
rruleEntry = _RruleEntry_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 30, 1)
)
rruleEntry.setIndexNames(
    (0, "MF-MIB", "rruleIndex"),
)
if mibBuilder.loadTexts:
    rruleEntry.setStatus("current")


class _RruleIndex_Type(Integer32):
    """Custom type rruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RruleIndex_Type.__name__ = "Integer32"
_RruleIndex_Object = MibTableColumn
rruleIndex = _RruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 30, 1, 1),
    _RruleIndex_Type()
)
rruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rruleIndex.setStatus("current")
_RruleAdminStatus_Type = AdminStatus
_RruleAdminStatus_Object = MibTableColumn
rruleAdminStatus = _RruleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 30, 1, 2),
    _RruleAdminStatus_Type()
)
rruleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rruleAdminStatus.setStatus("current")
_RruleName_Type = DisplayString
_RruleName_Object = MibTableColumn
rruleName = _RruleName_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 30, 1, 3),
    _RruleName_Type()
)
rruleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rruleName.setStatus("current")
_RruleDescription_Type = DisplayString
_RruleDescription_Object = MibTableColumn
rruleDescription = _RruleDescription_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 30, 1, 4),
    _RruleDescription_Type()
)
rruleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rruleDescription.setStatus("current")
_RruleLastActivatedOn_Type = Unsigned32
_RruleLastActivatedOn_Object = MibTableColumn
rruleLastActivatedOn = _RruleLastActivatedOn_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 30, 1, 5),
    _RruleLastActivatedOn_Type()
)
rruleLastActivatedOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rruleLastActivatedOn.setStatus("current")
_RruleOperationalStatus_Type = OperationalStatus
_RruleOperationalStatus_Object = MibTableColumn
rruleOperationalStatus = _RruleOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 30, 1, 6),
    _RruleOperationalStatus_Type()
)
rruleOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rruleOperationalStatus.setStatus("current")
_RruleNumberOfUsers_Type = Gauge32
_RruleNumberOfUsers_Object = MibTableColumn
rruleNumberOfUsers = _RruleNumberOfUsers_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 30, 1, 7),
    _RruleNumberOfUsers_Type()
)
rruleNumberOfUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rruleNumberOfUsers.setStatus("current")
_RrulePrimaryDestination_Type = DisplayString
_RrulePrimaryDestination_Object = MibTableColumn
rrulePrimaryDestination = _RrulePrimaryDestination_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 30, 1, 8),
    _RrulePrimaryDestination_Type()
)
rrulePrimaryDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rrulePrimaryDestination.setStatus("current")
_RruleSecondaryDestination_Type = DisplayString
_RruleSecondaryDestination_Object = MibTableColumn
rruleSecondaryDestination = _RruleSecondaryDestination_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 30, 1, 9),
    _RruleSecondaryDestination_Type()
)
rruleSecondaryDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rruleSecondaryDestination.setStatus("current")
_RruleLastResortDestination_Type = DisplayString
_RruleLastResortDestination_Object = MibTableColumn
rruleLastResortDestination = _RruleLastResortDestination_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 30, 1, 10),
    _RruleLastResortDestination_Type()
)
rruleLastResortDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rruleLastResortDestination.setStatus("current")
_EdrTotalRecCount_Type = Counter64
_EdrTotalRecCount_Object = MibScalar
edrTotalRecCount = _EdrTotalRecCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 50),
    _EdrTotalRecCount_Type()
)
edrTotalRecCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edrTotalRecCount.setStatus("current")
_EdrWrittenRecCount_Type = Counter64
_EdrWrittenRecCount_Object = MibScalar
edrWrittenRecCount = _EdrWrittenRecCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 51),
    _EdrWrittenRecCount_Type()
)
edrWrittenRecCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edrWrittenRecCount.setStatus("current")
_EdrDroppedRecCount_Type = Counter64
_EdrDroppedRecCount_Object = MibScalar
edrDroppedRecCount = _EdrDroppedRecCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 52),
    _EdrDroppedRecCount_Type()
)
edrDroppedRecCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edrDroppedRecCount.setStatus("current")
_EdrDroppedQueueFailRecCount_Type = Counter64
_EdrDroppedQueueFailRecCount_Object = MibScalar
edrDroppedQueueFailRecCount = _EdrDroppedQueueFailRecCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 53),
    _EdrDroppedQueueFailRecCount_Type()
)
edrDroppedQueueFailRecCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edrDroppedQueueFailRecCount.setStatus("current")
_EdrDroppedQueueFullRecCount_Type = Counter64
_EdrDroppedQueueFullRecCount_Object = MibScalar
edrDroppedQueueFullRecCount = _EdrDroppedQueueFullRecCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 54),
    _EdrDroppedQueueFullRecCount_Type()
)
edrDroppedQueueFullRecCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edrDroppedQueueFullRecCount.setStatus("current")
_EdrDroppedWriteFailRecCount_Type = Counter64
_EdrDroppedWriteFailRecCount_Object = MibScalar
edrDroppedWriteFailRecCount = _EdrDroppedWriteFailRecCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 2, 55),
    _EdrDroppedWriteFailRecCount_Type()
)
edrDroppedWriteFailRecCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edrDroppedWriteFailRecCount.setStatus("current")
_MfNotifications_ObjectIdentity = ObjectIdentity
mfNotifications = _MfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0)
)
_MfDebug_ObjectIdentity = ObjectIdentity
mfDebug = _MfDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39216, 1, 10)
)
_DebugTable_Object = MibTable
debugTable = _DebugTable_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 10, 1)
)
if mibBuilder.loadTexts:
    debugTable.setStatus("current")
_DebugEntry_Object = MibTableRow
debugEntry = _DebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 10, 1, 1)
)
debugEntry.setIndexNames(
    (0, "MF-MIB", "debugIndex"),
)
if mibBuilder.loadTexts:
    debugEntry.setStatus("current")


class _DebugIndex_Type(Integer32):
    """Custom type debugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DebugIndex_Type.__name__ = "Integer32"
_DebugIndex_Object = MibTableColumn
debugIndex = _DebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 10, 1, 1, 1),
    _DebugIndex_Type()
)
debugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    debugIndex.setStatus("current")
_DebugName_Type = DisplayString
_DebugName_Object = MibTableColumn
debugName = _DebugName_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 10, 1, 1, 2),
    _DebugName_Type()
)
debugName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugName.setStatus("current")
_DebugTraceLevel_Type = TraceLevel
_DebugTraceLevel_Object = MibTableColumn
debugTraceLevel = _DebugTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 10, 1, 1, 3),
    _DebugTraceLevel_Type()
)
debugTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugTraceLevel.setStatus("current")
_DebugTrace_Type = DisplayString
_DebugTrace_Object = MibScalar
debugTrace = _DebugTrace_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 10, 2),
    _DebugTrace_Type()
)
debugTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugTrace.setStatus("current")
_MfDebugCounters_ObjectIdentity = ObjectIdentity
mfDebugCounters = _MfDebugCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39216, 1, 10, 10)
)
_DebugNumberOfMfMessages_Type = Counter64
_DebugNumberOfMfMessages_Object = MibScalar
debugNumberOfMfMessages = _DebugNumberOfMfMessages_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 10, 10, 1),
    _DebugNumberOfMfMessages_Type()
)
debugNumberOfMfMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugNumberOfMfMessages.setStatus("current")
_DebugNumberOfDmtrMessages_Type = Counter64
_DebugNumberOfDmtrMessages_Object = MibScalar
debugNumberOfDmtrMessages = _DebugNumberOfDmtrMessages_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 10, 10, 2),
    _DebugNumberOfDmtrMessages_Type()
)
debugNumberOfDmtrMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugNumberOfDmtrMessages.setStatus("current")
_MfMultiNode_ObjectIdentity = ObjectIdentity
mfMultiNode = _MfMultiNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39216, 1, 20)
)
_ConfigSyncHost_Type = DisplayString
_ConfigSyncHost_Object = MibScalar
configSyncHost = _ConfigSyncHost_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 20, 1),
    _ConfigSyncHost_Type()
)
configSyncHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    configSyncHost.setStatus("current")
_ConfigSyncDir_Type = DisplayString
_ConfigSyncDir_Object = MibScalar
configSyncDir = _ConfigSyncDir_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 20, 2),
    _ConfigSyncDir_Type()
)
configSyncDir.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    configSyncDir.setStatus("current")
_MfLicense_ObjectIdentity = ObjectIdentity
mfLicense = _MfLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39216, 1, 30)
)
_LicenseReload_Type = ReloadAction
_LicenseReload_Object = MibScalar
licenseReload = _LicenseReload_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 30, 1),
    _LicenseReload_Type()
)
licenseReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseReload.setStatus("current")
_MfSessionStore_ObjectIdentity = ObjectIdentity
mfSessionStore = _MfSessionStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39216, 1, 40)
)
_StoreName_Type = DisplayString
_StoreName_Object = MibScalar
storeName = _StoreName_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 40, 1),
    _StoreName_Type()
)
storeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storeName.setStatus("current")
_StoreExpiry_Type = Unsigned32
_StoreExpiry_Object = MibScalar
storeExpiry = _StoreExpiry_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 40, 2),
    _StoreExpiry_Type()
)
storeExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storeExpiry.setStatus("current")
_StoreMaximumMemory_Type = Gauge32
_StoreMaximumMemory_Object = MibScalar
storeMaximumMemory = _StoreMaximumMemory_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 40, 11),
    _StoreMaximumMemory_Type()
)
storeMaximumMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storeMaximumMemory.setStatus("current")
_StoreUsedMemory_Type = Gauge32
_StoreUsedMemory_Object = MibScalar
storeUsedMemory = _StoreUsedMemory_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 40, 12),
    _StoreUsedMemory_Type()
)
storeUsedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storeUsedMemory.setStatus("current")
_StoreUsage_Type = Gauge32
_StoreUsage_Object = MibScalar
storeUsage = _StoreUsage_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 40, 13),
    _StoreUsage_Type()
)
storeUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storeUsage.setStatus("current")
_StoreNumberOfEntries_Type = Gauge32
_StoreNumberOfEntries_Object = MibScalar
storeNumberOfEntries = _StoreNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 40, 14),
    _StoreNumberOfEntries_Type()
)
storeNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storeNumberOfEntries.setStatus("current")
_StoreNumberOfActiveNodes_Type = Gauge32
_StoreNumberOfActiveNodes_Object = MibScalar
storeNumberOfActiveNodes = _StoreNumberOfActiveNodes_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 40, 15),
    _StoreNumberOfActiveNodes_Type()
)
storeNumberOfActiveNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storeNumberOfActiveNodes.setStatus("current")
_StoreUsedDiskSpace_Type = Gauge32
_StoreUsedDiskSpace_Object = MibScalar
storeUsedDiskSpace = _StoreUsedDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 40, 16),
    _StoreUsedDiskSpace_Type()
)
storeUsedDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storeUsedDiskSpace.setStatus("current")
_StoreGetCount_Type = Counter64
_StoreGetCount_Object = MibScalar
storeGetCount = _StoreGetCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 40, 51),
    _StoreGetCount_Type()
)
storeGetCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    storeGetCount.setStatus("current")
_StoreSetCount_Type = Counter64
_StoreSetCount_Object = MibScalar
storeSetCount = _StoreSetCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 40, 52),
    _StoreSetCount_Type()
)
storeSetCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    storeSetCount.setStatus("current")
_StoreDeleteCount_Type = Counter64
_StoreDeleteCount_Object = MibScalar
storeDeleteCount = _StoreDeleteCount_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 40, 53),
    _StoreDeleteCount_Type()
)
storeDeleteCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    storeDeleteCount.setStatus("current")
_MfModules_ObjectIdentity = ObjectIdentity
mfModules = _MfModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50)
)
_MfDict_ObjectIdentity = ObjectIdentity
mfDict = _MfDict_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39216, 1, 60)
)
_DictReload_Type = ReloadAction
_DictReload_Object = MibScalar
dictReload = _DictReload_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 60, 1),
    _DictReload_Type()
)
dictReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dictReload.setStatus("current")
_MfManager_ObjectIdentity = ObjectIdentity
mfManager = _MfManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39216, 1, 70)
)
_LoginUserId_Type = DisplayString
_LoginUserId_Object = MibScalar
loginUserId = _LoginUserId_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 70, 1),
    _LoginUserId_Type()
)
loginUserId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    loginUserId.setStatus("current")
_LoginClientIP_Type = DisplayString
_LoginClientIP_Object = MibScalar
loginClientIP = _LoginClientIP_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 70, 2),
    _LoginClientIP_Type()
)
loginClientIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    loginClientIP.setStatus("current")
_MfQueue_ObjectIdentity = ObjectIdentity
mfQueue = _MfQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39216, 1, 80)
)
_QueueType_Type = DisplayString
_QueueType_Object = MibScalar
queueType = _QueueType_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 80, 1),
    _QueueType_Type()
)
queueType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    queueType.setStatus("current")
_MfFile_ObjectIdentity = ObjectIdentity
mfFile = _MfFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39216, 1, 90)
)
_FileName_Type = DisplayString
_FileName_Object = MibScalar
fileName = _FileName_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 90, 1),
    _FileName_Type()
)
fileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fileName.setStatus("current")

# Managed Objects groups

mfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39216, 1, 4)
)
mfGroup.setObjects(
      *(("MF-MIB", "serverName"),
        ("MF-MIB", "traceLevel"),
        ("MF-MIB", "lastRestart"),
        ("MF-MIB", "logLevel"),
        ("MF-MIB", "severity"),
        ("MF-MIB", "cbNodeIp"),
        ("MF-MIB", "cbNodeName"),
        ("MF-MIB", "cbNodeStatus"),
        ("MF-MIB", "adminStatus"),
        ("MF-MIB", "totalTxCount"),
        ("MF-MIB", "successTxCount"),
        ("MF-MIB", "failedTxCount"),
        ("MF-MIB", "failedProcessTxCount"),
        ("MF-MIB", "failedDroppedTxCount"),
        ("MF-MIB", "failedShutdownTxCount"),
        ("MF-MIB", "failedUnknownFlowTxCount"),
        ("MF-MIB", "failedTimeoutTxCount"),
        ("MF-MIB", "failedCongestionTxCount"),
        ("MF-MIB", "rejectIngressTxCount"),
        ("MF-MIB", "activateFlow"),
        ("MF-MIB", "lastErrorReason"),
        ("MF-MIB", "queuedMsgGauge"),
        ("MF-MIB", "highestQueuedMsgGauge"),
        ("MF-MIB", "queuedMsgGaugeB"),
        ("MF-MIB", "highestQueuedMsgGaugeB"),
        ("MF-MIB", "edrTotalRecCount"),
        ("MF-MIB", "edrWrittenRecCount"),
        ("MF-MIB", "edrDroppedRecCount"),
        ("MF-MIB", "edrDroppedQueueFailRecCount"),
        ("MF-MIB", "edrDroppedQueueFullRecCount"),
        ("MF-MIB", "edrDroppedWriteFailRecCount"),
        ("MF-MIB", "activateRRule"),
        ("MF-MIB", "queueSize"),
        ("MF-MIB", "queueSizeB"),
        ("MF-MIB", "flowName"),
        ("MF-MIB", "flowAdminStatus"),
        ("MF-MIB", "flowOperationalStatus"),
        ("MF-MIB", "flowLogLevel"),
        ("MF-MIB", "flowDescription"),
        ("MF-MIB", "flowLastActivatedOn"),
        ("MF-MIB", "flowTxBeingProcessed"),
        ("MF-MIB", "flowTotalTxCount"),
        ("MF-MIB", "flowSuccessTxCount"),
        ("MF-MIB", "flowFailedTxCount"),
        ("MF-MIB", "flowFailedProcessTxCount"),
        ("MF-MIB", "flowFailedDroppedTxCount"),
        ("MF-MIB", "flowFailedShutdownTxCount"),
        ("MF-MIB", "flowFailedTimeoutTxCount"),
        ("MF-MIB", "flowFailedCongestionTxCount"),
        ("MF-MIB", "flowRejectIngressTxCount"),
        ("MF-MIB", "flowMinimumTotalTxDelay"),
        ("MF-MIB", "flowMaximumTotalTxDelay"),
        ("MF-MIB", "flowAverageTotalTxDelay"),
        ("MF-MIB", "flowPercentageBelow5msec"),
        ("MF-MIB", "flowPercentageBelow10msec"),
        ("MF-MIB", "moduleName"),
        ("MF-MIB", "moduleDescription"),
        ("MF-MIB", "moduleQueueSize"),
        ("MF-MIB", "moduleQueueSizeB"),
        ("MF-MIB", "moduleReloadConfig"),
        ("MF-MIB", "moduleLogLevel"),
        ("MF-MIB", "moduleWorkerThreads"),
        ("MF-MIB", "moduleVersion"),
        ("MF-MIB", "moduleTotalMsgCount"),
        ("MF-MIB", "moduleSuccessMsgCount"),
        ("MF-MIB", "moduleFailedMsgCount"),
        ("MF-MIB", "moduleFailedUnknownFlowMsgCount"),
        ("MF-MIB", "moduleFailedTimeoutMsgCount"),
        ("MF-MIB", "moduleFailedCongestionMsgCount"),
        ("MF-MIB", "moduleFailedProcessingMsgCount"),
        ("MF-MIB", "moduleFailedDroppedMsgCount"),
        ("MF-MIB", "moduleRejectIngressMsgCount"),
        ("MF-MIB", "moduleQueuedMsgGauge"),
        ("MF-MIB", "moduleHighestQueuedMsgGauge"),
        ("MF-MIB", "moduleQueuedMsgGaugeB"),
        ("MF-MIB", "moduleHighestQueuedMsgGaugeB"),
        ("MF-MIB", "debugName"),
        ("MF-MIB", "debugTraceLevel"),
        ("MF-MIB", "debugTrace"),
        ("MF-MIB", "debugNumberOfMfMessages"),
        ("MF-MIB", "debugNumberOfDmtrMessages"),
        ("MF-MIB", "configSyncDir"),
        ("MF-MIB", "configSyncHost"),
        ("MF-MIB", "licenseReload"),
        ("MF-MIB", "storeName"),
        ("MF-MIB", "storeExpiry"),
        ("MF-MIB", "storeMaximumMemory"),
        ("MF-MIB", "storeUsedMemory"),
        ("MF-MIB", "storeUsage"),
        ("MF-MIB", "storeNumberOfEntries"),
        ("MF-MIB", "storeNumberOfActiveNodes"),
        ("MF-MIB", "storeUsedDiskSpace"),
        ("MF-MIB", "storeGetCount"),
        ("MF-MIB", "storeSetCount"),
        ("MF-MIB", "storeDeleteCount"),
        ("MF-MIB", "rruleName"),
        ("MF-MIB", "rruleAdminStatus"),
        ("MF-MIB", "rruleOperationalStatus"),
        ("MF-MIB", "rruleNumberOfUsers"),
        ("MF-MIB", "rruleDescription"),
        ("MF-MIB", "rruleLastActivatedOn"),
        ("MF-MIB", "rrulePrimaryDestination"),
        ("MF-MIB", "rruleSecondaryDestination"),
        ("MF-MIB", "rruleLastResortDestination"),
        ("MF-MIB", "dictReload"),
        ("MF-MIB", "loginUserId"),
        ("MF-MIB", "loginClientIP"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "fileName"))
)
if mibBuilder.loadTexts:
    mfGroup.setStatus("current")


# Notification objects

mfQueueLowWatermarkReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 5)
)
mfQueueLowWatermarkReached.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    mfQueueLowWatermarkReached.setStatus(
        "current"
    )

mfQueueLowWatermarkCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 6)
)
mfQueueLowWatermarkCleared.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    mfQueueLowWatermarkCleared.setStatus(
        "current"
    )

mfQueueHighWatermarkReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 7)
)
mfQueueHighWatermarkReached.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    mfQueueHighWatermarkReached.setStatus(
        "current"
    )

mfQueueHighWatermarkCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 8)
)
mfQueueHighWatermarkCleared.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    mfQueueHighWatermarkCleared.setStatus(
        "current"
    )

mfQueueFullReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 9)
)
mfQueueFullReached.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    mfQueueFullReached.setStatus(
        "current"
    )

mfQueueFullCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 10)
)
mfQueueFullCleared.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    mfQueueFullCleared.setStatus(
        "current"
    )

queueLowWatermarkReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 11)
)
queueLowWatermarkReached.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "moduleName"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    queueLowWatermarkReached.setStatus(
        "current"
    )

queueLowWatermarkCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 12)
)
queueLowWatermarkCleared.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "moduleName"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    queueLowWatermarkCleared.setStatus(
        "current"
    )

queueHighWatermarkReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 13)
)
queueHighWatermarkReached.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "moduleName"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    queueHighWatermarkReached.setStatus(
        "current"
    )

queueHighWatermarkCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 14)
)
queueHighWatermarkCleared.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "moduleName"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    queueHighWatermarkCleared.setStatus(
        "current"
    )

queueFullReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 15)
)
queueFullReached.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "moduleName"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    queueFullReached.setStatus(
        "current"
    )

queueFullCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 16)
)
queueFullCleared.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "moduleName"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    queueFullCleared.setStatus(
        "current"
    )

licenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 21)
)
licenseExpired.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "moduleName"))
)
if mibBuilder.loadTexts:
    licenseExpired.setStatus(
        "current"
    )

licenseAboutToExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 22)
)
licenseAboutToExpire.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "moduleName"))
)
if mibBuilder.loadTexts:
    licenseAboutToExpire.setStatus(
        "current"
    )

saEventQueueLowWatermarkReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 23)
)
saEventQueueLowWatermarkReached.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    saEventQueueLowWatermarkReached.setStatus(
        "current"
    )

saEventQueueLowWatermarkCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 24)
)
saEventQueueLowWatermarkCleared.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    saEventQueueLowWatermarkCleared.setStatus(
        "current"
    )

saEventQueueHighWatermarkReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 25)
)
saEventQueueHighWatermarkReached.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    saEventQueueHighWatermarkReached.setStatus(
        "current"
    )

saEventQueueHighWatermarkCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 26)
)
saEventQueueHighWatermarkCleared.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    saEventQueueHighWatermarkCleared.setStatus(
        "current"
    )

saNotifQueueLowWatermarkReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 27)
)
saNotifQueueLowWatermarkReached.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    saNotifQueueLowWatermarkReached.setStatus(
        "current"
    )

saNotifQueueLowWatermarkCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 28)
)
saNotifQueueLowWatermarkCleared.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    saNotifQueueLowWatermarkCleared.setStatus(
        "current"
    )

saNotifQueueHighWatermarkReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 29)
)
saNotifQueueHighWatermarkReached.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    saNotifQueueHighWatermarkReached.setStatus(
        "current"
    )

saNotifQueueHighWatermarkCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 30)
)
saNotifQueueHighWatermarkCleared.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    saNotifQueueHighWatermarkCleared.setStatus(
        "current"
    )

configSyncFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 31)
)
configSyncFailed.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "serverName"),
        ("MF-MIB", "configSyncDir"))
)
if mibBuilder.loadTexts:
    configSyncFailed.setStatus(
        "current"
    )

configSyncOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 32)
)
configSyncOK.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "serverName"),
        ("MF-MIB", "configSyncDir"))
)
if mibBuilder.loadTexts:
    configSyncOK.setStatus(
        "current"
    )

writingRecordsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 41)
)
writingRecordsFailed.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "lastErrorReason"))
)
if mibBuilder.loadTexts:
    writingRecordsFailed.setStatus(
        "current"
    )

writingRecordsOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 42)
)
writingRecordsOk.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "lastErrorReason"))
)
if mibBuilder.loadTexts:
    writingRecordsOk.setStatus(
        "current"
    )

queuingRecordsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 43)
)
queuingRecordsFailed.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "lastErrorReason"))
)
if mibBuilder.loadTexts:
    queuingRecordsFailed.setStatus(
        "current"
    )

queuingRecordsOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 44)
)
queuingRecordsOk.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "lastErrorReason"))
)
if mibBuilder.loadTexts:
    queuingRecordsOk.setStatus(
        "current"
    )

edrOpenFileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 45)
)
edrOpenFileFailed.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "fileName"))
)
if mibBuilder.loadTexts:
    edrOpenFileFailed.setStatus(
        "current"
    )

edrOpenFileOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 46)
)
edrOpenFileOk.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "fileName"))
)
if mibBuilder.loadTexts:
    edrOpenFileOk.setStatus(
        "current"
    )

edrWriteRecordsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 47)
)
edrWriteRecordsFailed.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "fileName"),
        ("MF-MIB", "edrDroppedWriteFailRecCount"))
)
if mibBuilder.loadTexts:
    edrWriteRecordsFailed.setStatus(
        "current"
    )

edrWriteRecordsOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 48)
)
edrWriteRecordsOk.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "fileName"),
        ("MF-MIB", "edrDroppedWriteFailRecCount"))
)
if mibBuilder.loadTexts:
    edrWriteRecordsOk.setStatus(
        "current"
    )

edrMoveFileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 49)
)
edrMoveFileFailed.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "fileName"))
)
if mibBuilder.loadTexts:
    edrMoveFileFailed.setStatus(
        "current"
    )

storageMemoryLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 50)
)
storageMemoryLimitReached.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "moduleName"))
)
if mibBuilder.loadTexts:
    storageMemoryLimitReached.setStatus(
        "current"
    )

storageMemoryLimitCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 51)
)
storageMemoryLimitCleared.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "moduleName"))
)
if mibBuilder.loadTexts:
    storageMemoryLimitCleared.setStatus(
        "current"
    )

storageMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 52)
)
storageMemoryUsageHigh.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "moduleName"))
)
if mibBuilder.loadTexts:
    storageMemoryUsageHigh.setStatus(
        "current"
    )

cbPeerHealthy = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 60)
)
cbPeerHealthy.setObjects(
    ("MF-MIB", "severity")
)
if mibBuilder.loadTexts:
    cbPeerHealthy.setStatus(
        "current"
    )

cbClusterUnhealthy = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 61)
)
cbClusterUnhealthy.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "cbNodeIp"),
        ("MF-MIB", "cbNodeStatus"))
)
if mibBuilder.loadTexts:
    cbClusterUnhealthy.setStatus(
        "current"
    )

cbClusterNodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 62)
)
cbClusterNodeDown.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "cbNodeIp"))
)
if mibBuilder.loadTexts:
    cbClusterNodeDown.setStatus(
        "current"
    )

cbClusterStatusUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 63)
)
cbClusterStatusUnknown.setObjects(
    ("MF-MIB", "severity")
)
if mibBuilder.loadTexts:
    cbClusterStatusUnknown.setStatus(
        "current"
    )

failedLoginAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 80)
)
failedLoginAttempt.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "loginUserId"),
        ("MF-MIB", "loginClientIP"))
)
if mibBuilder.loadTexts:
    failedLoginAttempt.setStatus(
        "current"
    )

edrQueueLowWatermarkReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 90)
)
edrQueueLowWatermarkReached.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    edrQueueLowWatermarkReached.setStatus(
        "current"
    )

edrQueueLowWatermarkCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 91)
)
edrQueueLowWatermarkCleared.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    edrQueueLowWatermarkCleared.setStatus(
        "current"
    )

edrQueueHighWatermarkReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 92)
)
edrQueueHighWatermarkReached.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    edrQueueHighWatermarkReached.setStatus(
        "current"
    )

edrQueueHighWatermarkCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 93)
)
edrQueueHighWatermarkCleared.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"))
)
if mibBuilder.loadTexts:
    edrQueueHighWatermarkCleared.setStatus(
        "current"
    )

edrQueueFullReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 94)
)
edrQueueFullReached.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"),
        ("MF-MIB", "edrDroppedQueueFullRecCount"))
)
if mibBuilder.loadTexts:
    edrQueueFullReached.setStatus(
        "current"
    )

edrQueueFullCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 95)
)
edrQueueFullCleared.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"),
        ("MF-MIB", "edrDroppedQueueFullRecCount"))
)
if mibBuilder.loadTexts:
    edrQueueFullCleared.setStatus(
        "current"
    )

edrQueueFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 96)
)
edrQueueFailed.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"),
        ("MF-MIB", "edrDroppedQueueFailRecCount"))
)
if mibBuilder.loadTexts:
    edrQueueFailed.setStatus(
        "current"
    )

edrQueueOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 97)
)
edrQueueOk.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "queueType"),
        ("MF-MIB", "queueSize"),
        ("MF-MIB", "edrDroppedQueueFailRecCount"))
)
if mibBuilder.loadTexts:
    edrQueueOk.setStatus(
        "current"
    )

sessionStoreMemoryLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 100)
)
sessionStoreMemoryLimitReached.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "moduleName"))
)
if mibBuilder.loadTexts:
    sessionStoreMemoryLimitReached.setStatus(
        "current"
    )

sessionStoreMemoryLimitCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 101)
)
sessionStoreMemoryLimitCleared.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "moduleName"))
)
if mibBuilder.loadTexts:
    sessionStoreMemoryLimitCleared.setStatus(
        "current"
    )

sessionStoreMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 3, 0, 102)
)
sessionStoreMemoryUsageHigh.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "moduleName"))
)
if mibBuilder.loadTexts:
    sessionStoreMemoryUsageHigh.setStatus(
        "current"
    )


# Notifications groups

mfNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 39216, 1, 5)
)
mfNotificationGroup.setObjects(
      *(("MF-MIB", "mfQueueLowWatermarkReached"),
        ("MF-MIB", "mfQueueLowWatermarkCleared"),
        ("MF-MIB", "mfQueueHighWatermarkReached"),
        ("MF-MIB", "mfQueueHighWatermarkCleared"),
        ("MF-MIB", "mfQueueFullReached"),
        ("MF-MIB", "mfQueueFullCleared"),
        ("MF-MIB", "queueLowWatermarkReached"),
        ("MF-MIB", "queueLowWatermarkCleared"),
        ("MF-MIB", "queueHighWatermarkReached"),
        ("MF-MIB", "queueHighWatermarkCleared"),
        ("MF-MIB", "queueFullReached"),
        ("MF-MIB", "queueFullCleared"),
        ("MF-MIB", "licenseExpired"),
        ("MF-MIB", "licenseAboutToExpire"),
        ("MF-MIB", "saEventQueueLowWatermarkReached"),
        ("MF-MIB", "saEventQueueLowWatermarkCleared"),
        ("MF-MIB", "saEventQueueHighWatermarkReached"),
        ("MF-MIB", "saEventQueueHighWatermarkCleared"),
        ("MF-MIB", "saNotifQueueLowWatermarkReached"),
        ("MF-MIB", "saNotifQueueLowWatermarkCleared"),
        ("MF-MIB", "saNotifQueueHighWatermarkReached"),
        ("MF-MIB", "saNotifQueueHighWatermarkCleared"),
        ("MF-MIB", "configSyncFailed"),
        ("MF-MIB", "configSyncOK"),
        ("MF-MIB", "writingRecordsFailed"),
        ("MF-MIB", "writingRecordsOk"),
        ("MF-MIB", "queuingRecordsFailed"),
        ("MF-MIB", "queuingRecordsOk"),
        ("MF-MIB", "edrOpenFileFailed"),
        ("MF-MIB", "edrOpenFileOk"),
        ("MF-MIB", "edrWriteRecordsFailed"),
        ("MF-MIB", "edrWriteRecordsOk"),
        ("MF-MIB", "edrMoveFileFailed"),
        ("MF-MIB", "storageMemoryLimitReached"),
        ("MF-MIB", "storageMemoryLimitCleared"),
        ("MF-MIB", "storageMemoryUsageHigh"),
        ("MF-MIB", "cbPeerHealthy"),
        ("MF-MIB", "cbClusterUnhealthy"),
        ("MF-MIB", "cbClusterNodeDown"),
        ("MF-MIB", "cbClusterStatusUnknown"),
        ("MF-MIB", "failedLoginAttempt"),
        ("MF-MIB", "edrQueueLowWatermarkReached"),
        ("MF-MIB", "edrQueueLowWatermarkCleared"),
        ("MF-MIB", "edrQueueHighWatermarkReached"),
        ("MF-MIB", "edrQueueHighWatermarkCleared"),
        ("MF-MIB", "edrQueueFullReached"),
        ("MF-MIB", "edrQueueFullCleared"),
        ("MF-MIB", "edrQueueFailed"),
        ("MF-MIB", "edrQueueOk"),
        ("MF-MIB", "sessionStoreMemoryLimitReached"),
        ("MF-MIB", "sessionStoreMemoryLimitCleared"),
        ("MF-MIB", "sessionStoreMemoryUsageHigh"))
)
if mibBuilder.loadTexts:
    mfNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MF-MIB",
    **{"AdminStatus": AdminStatus,
       "OperationalStatus": OperationalStatus,
       "ReloadAction": ReloadAction,
       "TraceLevel": TraceLevel,
       "LogLevel": LogLevel,
       "RateUnit": RateUnit,
       "mfMib": mfMib,
       "mfInfo": mfInfo,
       "serverName": serverName,
       "traceLevel": traceLevel,
       "lastRestart": lastRestart,
       "logLevel": logLevel,
       "severity": severity,
       "cbNodeIp": cbNodeIp,
       "cbNodeName": cbNodeName,
       "cbNodeStatus": cbNodeStatus,
       "adminStatus": adminStatus,
       "mfStatus": mfStatus,
       "totalTxCount": totalTxCount,
       "successTxCount": successTxCount,
       "failedTxCount": failedTxCount,
       "failedProcessTxCount": failedProcessTxCount,
       "failedDroppedTxCount": failedDroppedTxCount,
       "failedShutdownTxCount": failedShutdownTxCount,
       "failedUnknownFlowTxCount": failedUnknownFlowTxCount,
       "failedTimeoutTxCount": failedTimeoutTxCount,
       "failedCongestionTxCount": failedCongestionTxCount,
       "rejectIngressTxCount": rejectIngressTxCount,
       "activateFlow": activateFlow,
       "lastErrorReason": lastErrorReason,
       "activateRRule": activateRRule,
       "queueSize": queueSize,
       "queueSizeB": queueSizeB,
       "flowTable": flowTable,
       "flowEntry": flowEntry,
       "flowIndex": flowIndex,
       "flowAdminStatus": flowAdminStatus,
       "flowName": flowName,
       "flowDescription": flowDescription,
       "flowLastActivatedOn": flowLastActivatedOn,
       "flowTxBeingProcessed": flowTxBeingProcessed,
       "flowOperationalStatus": flowOperationalStatus,
       "flowLogLevel": flowLogLevel,
       "flowTotalTxCount": flowTotalTxCount,
       "flowSuccessTxCount": flowSuccessTxCount,
       "flowFailedTxCount": flowFailedTxCount,
       "flowFailedProcessTxCount": flowFailedProcessTxCount,
       "flowFailedDroppedTxCount": flowFailedDroppedTxCount,
       "flowFailedShutdownTxCount": flowFailedShutdownTxCount,
       "flowFailedTimeoutTxCount": flowFailedTimeoutTxCount,
       "flowFailedCongestionTxCount": flowFailedCongestionTxCount,
       "flowRejectIngressTxCount": flowRejectIngressTxCount,
       "flowMinimumTotalTxDelay": flowMinimumTotalTxDelay,
       "flowMaximumTotalTxDelay": flowMaximumTotalTxDelay,
       "flowAverageTotalTxDelay": flowAverageTotalTxDelay,
       "flowPercentageBelow5msec": flowPercentageBelow5msec,
       "flowPercentageBelow10msec": flowPercentageBelow10msec,
       "queuedMsgGauge": queuedMsgGauge,
       "highestQueuedMsgGauge": highestQueuedMsgGauge,
       "queuedMsgGaugeB": queuedMsgGaugeB,
       "highestQueuedMsgGaugeB": highestQueuedMsgGaugeB,
       "moduleTable": moduleTable,
       "moduleEntry": moduleEntry,
       "moduleIndex": moduleIndex,
       "moduleName": moduleName,
       "moduleDescription": moduleDescription,
       "moduleQueueSize": moduleQueueSize,
       "moduleReloadConfig": moduleReloadConfig,
       "moduleLogLevel": moduleLogLevel,
       "moduleWorkerThreads": moduleWorkerThreads,
       "moduleVersion": moduleVersion,
       "moduleQueueSizeB": moduleQueueSizeB,
       "moduleTotalMsgCount": moduleTotalMsgCount,
       "moduleSuccessMsgCount": moduleSuccessMsgCount,
       "moduleFailedMsgCount": moduleFailedMsgCount,
       "moduleFailedUnknownFlowMsgCount": moduleFailedUnknownFlowMsgCount,
       "moduleFailedTimeoutMsgCount": moduleFailedTimeoutMsgCount,
       "moduleFailedCongestionMsgCount": moduleFailedCongestionMsgCount,
       "moduleFailedProcessingMsgCount": moduleFailedProcessingMsgCount,
       "moduleFailedDroppedMsgCount": moduleFailedDroppedMsgCount,
       "moduleRejectIngressMsgCount": moduleRejectIngressMsgCount,
       "moduleQueuedMsgGauge": moduleQueuedMsgGauge,
       "moduleHighestQueuedMsgGauge": moduleHighestQueuedMsgGauge,
       "moduleQueuedMsgGaugeB": moduleQueuedMsgGaugeB,
       "moduleHighestQueuedMsgGaugeB": moduleHighestQueuedMsgGaugeB,
       "rruleTable": rruleTable,
       "rruleEntry": rruleEntry,
       "rruleIndex": rruleIndex,
       "rruleAdminStatus": rruleAdminStatus,
       "rruleName": rruleName,
       "rruleDescription": rruleDescription,
       "rruleLastActivatedOn": rruleLastActivatedOn,
       "rruleOperationalStatus": rruleOperationalStatus,
       "rruleNumberOfUsers": rruleNumberOfUsers,
       "rrulePrimaryDestination": rrulePrimaryDestination,
       "rruleSecondaryDestination": rruleSecondaryDestination,
       "rruleLastResortDestination": rruleLastResortDestination,
       "edrTotalRecCount": edrTotalRecCount,
       "edrWrittenRecCount": edrWrittenRecCount,
       "edrDroppedRecCount": edrDroppedRecCount,
       "edrDroppedQueueFailRecCount": edrDroppedQueueFailRecCount,
       "edrDroppedQueueFullRecCount": edrDroppedQueueFullRecCount,
       "edrDroppedWriteFailRecCount": edrDroppedWriteFailRecCount,
       "mfNotifications": mfNotifications,
       "mfQueueLowWatermarkReached": mfQueueLowWatermarkReached,
       "mfQueueLowWatermarkCleared": mfQueueLowWatermarkCleared,
       "mfQueueHighWatermarkReached": mfQueueHighWatermarkReached,
       "mfQueueHighWatermarkCleared": mfQueueHighWatermarkCleared,
       "mfQueueFullReached": mfQueueFullReached,
       "mfQueueFullCleared": mfQueueFullCleared,
       "queueLowWatermarkReached": queueLowWatermarkReached,
       "queueLowWatermarkCleared": queueLowWatermarkCleared,
       "queueHighWatermarkReached": queueHighWatermarkReached,
       "queueHighWatermarkCleared": queueHighWatermarkCleared,
       "queueFullReached": queueFullReached,
       "queueFullCleared": queueFullCleared,
       "licenseExpired": licenseExpired,
       "licenseAboutToExpire": licenseAboutToExpire,
       "saEventQueueLowWatermarkReached": saEventQueueLowWatermarkReached,
       "saEventQueueLowWatermarkCleared": saEventQueueLowWatermarkCleared,
       "saEventQueueHighWatermarkReached": saEventQueueHighWatermarkReached,
       "saEventQueueHighWatermarkCleared": saEventQueueHighWatermarkCleared,
       "saNotifQueueLowWatermarkReached": saNotifQueueLowWatermarkReached,
       "saNotifQueueLowWatermarkCleared": saNotifQueueLowWatermarkCleared,
       "saNotifQueueHighWatermarkReached": saNotifQueueHighWatermarkReached,
       "saNotifQueueHighWatermarkCleared": saNotifQueueHighWatermarkCleared,
       "configSyncFailed": configSyncFailed,
       "configSyncOK": configSyncOK,
       "writingRecordsFailed": writingRecordsFailed,
       "writingRecordsOk": writingRecordsOk,
       "queuingRecordsFailed": queuingRecordsFailed,
       "queuingRecordsOk": queuingRecordsOk,
       "edrOpenFileFailed": edrOpenFileFailed,
       "edrOpenFileOk": edrOpenFileOk,
       "edrWriteRecordsFailed": edrWriteRecordsFailed,
       "edrWriteRecordsOk": edrWriteRecordsOk,
       "edrMoveFileFailed": edrMoveFileFailed,
       "storageMemoryLimitReached": storageMemoryLimitReached,
       "storageMemoryLimitCleared": storageMemoryLimitCleared,
       "storageMemoryUsageHigh": storageMemoryUsageHigh,
       "cbPeerHealthy": cbPeerHealthy,
       "cbClusterUnhealthy": cbClusterUnhealthy,
       "cbClusterNodeDown": cbClusterNodeDown,
       "cbClusterStatusUnknown": cbClusterStatusUnknown,
       "failedLoginAttempt": failedLoginAttempt,
       "edrQueueLowWatermarkReached": edrQueueLowWatermarkReached,
       "edrQueueLowWatermarkCleared": edrQueueLowWatermarkCleared,
       "edrQueueHighWatermarkReached": edrQueueHighWatermarkReached,
       "edrQueueHighWatermarkCleared": edrQueueHighWatermarkCleared,
       "edrQueueFullReached": edrQueueFullReached,
       "edrQueueFullCleared": edrQueueFullCleared,
       "edrQueueFailed": edrQueueFailed,
       "edrQueueOk": edrQueueOk,
       "sessionStoreMemoryLimitReached": sessionStoreMemoryLimitReached,
       "sessionStoreMemoryLimitCleared": sessionStoreMemoryLimitCleared,
       "sessionStoreMemoryUsageHigh": sessionStoreMemoryUsageHigh,
       "mfGroup": mfGroup,
       "mfNotificationGroup": mfNotificationGroup,
       "mfDebug": mfDebug,
       "debugTable": debugTable,
       "debugEntry": debugEntry,
       "debugIndex": debugIndex,
       "debugName": debugName,
       "debugTraceLevel": debugTraceLevel,
       "debugTrace": debugTrace,
       "mfDebugCounters": mfDebugCounters,
       "debugNumberOfMfMessages": debugNumberOfMfMessages,
       "debugNumberOfDmtrMessages": debugNumberOfDmtrMessages,
       "mfMultiNode": mfMultiNode,
       "configSyncHost": configSyncHost,
       "configSyncDir": configSyncDir,
       "mfLicense": mfLicense,
       "licenseReload": licenseReload,
       "mfSessionStore": mfSessionStore,
       "storeName": storeName,
       "storeExpiry": storeExpiry,
       "storeMaximumMemory": storeMaximumMemory,
       "storeUsedMemory": storeUsedMemory,
       "storeUsage": storeUsage,
       "storeNumberOfEntries": storeNumberOfEntries,
       "storeNumberOfActiveNodes": storeNumberOfActiveNodes,
       "storeUsedDiskSpace": storeUsedDiskSpace,
       "storeGetCount": storeGetCount,
       "storeSetCount": storeSetCount,
       "storeDeleteCount": storeDeleteCount,
       "mfModules": mfModules,
       "mfDict": mfDict,
       "dictReload": dictReload,
       "mfManager": mfManager,
       "loginUserId": loginUserId,
       "loginClientIP": loginClientIP,
       "mfQueue": mfQueue,
       "queueType": queueType,
       "mfFile": mfFile,
       "fileName": fileName}
)
