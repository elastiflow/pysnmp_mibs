# SNMP MIB module (RBN-PORT-COUNTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/RBN-PORT-COUNTERS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:10:42 2025
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

(ApsK1K2,) = mibBuilder.importSymbols(
    "RBN-APS-MIB",
    "ApsK1K2")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnPort,
 RbnSlot) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnPort",
    "RbnSlot")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rpcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25)
)
if mibBuilder.loadTexts:
    rpcMib.setRevisions(
        ("2002-09-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RpcMibNotifications_ObjectIdentity = ObjectIdentity
rpcMibNotifications = _RpcMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 0)
)
_RpcMibObjects_ObjectIdentity = ObjectIdentity
rpcMibObjects = _RpcMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1)
)
_Rpc_ObjectIdentity = ObjectIdentity
rpc = _Rpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1)
)
_RpcGeneralTable_Object = MibTable
rpcGeneralTable = _RpcGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rpcGeneralTable.setStatus("current")
_RpcGeneralEntry_Object = MibTableRow
rpcGeneralEntry = _RpcGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1)
)
rpcGeneralEntry.setIndexNames(
    (0, "RBN-PORT-COUNTERS-MIB", "rpcSlotID"),
    (0, "RBN-PORT-COUNTERS-MIB", "rpcPortID"),
)
if mibBuilder.loadTexts:
    rpcGeneralEntry.setStatus("current")
_RpcSlotID_Type = RbnSlot
_RpcSlotID_Object = MibTableColumn
rpcSlotID = _RpcSlotID_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 1),
    _RpcSlotID_Type()
)
rpcSlotID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rpcSlotID.setStatus("current")
_RpcPortID_Type = RbnPort
_RpcPortID_Object = MibTableColumn
rpcPortID = _RpcPortID_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 2),
    _RpcPortID_Type()
)
rpcPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rpcPortID.setStatus("current")
_RpcGeneralPktsSent_Type = Counter64
_RpcGeneralPktsSent_Object = MibTableColumn
rpcGeneralPktsSent = _RpcGeneralPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 3),
    _RpcGeneralPktsSent_Type()
)
rpcGeneralPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralPktsSent.setStatus("current")
_RpcGeneralPktsRcvd_Type = Counter64
_RpcGeneralPktsRcvd_Object = MibTableColumn
rpcGeneralPktsRcvd = _RpcGeneralPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 4),
    _RpcGeneralPktsRcvd_Type()
)
rpcGeneralPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralPktsRcvd.setStatus("current")
_RpcGeneralBytesSent_Type = Counter64
_RpcGeneralBytesSent_Object = MibTableColumn
rpcGeneralBytesSent = _RpcGeneralBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 5),
    _RpcGeneralBytesSent_Type()
)
rpcGeneralBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralBytesSent.setStatus("current")
_RpcGeneralBytesRcvd_Type = Counter64
_RpcGeneralBytesRcvd_Object = MibTableColumn
rpcGeneralBytesRcvd = _RpcGeneralBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 6),
    _RpcGeneralBytesRcvd_Type()
)
rpcGeneralBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralBytesRcvd.setStatus("current")
_RpcGeneralMcastPktsSent_Type = Counter64
_RpcGeneralMcastPktsSent_Object = MibTableColumn
rpcGeneralMcastPktsSent = _RpcGeneralMcastPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 7),
    _RpcGeneralMcastPktsSent_Type()
)
rpcGeneralMcastPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralMcastPktsSent.setStatus("current")
_RpcGeneralMcastPktsRcvd_Type = Counter64
_RpcGeneralMcastPktsRcvd_Object = MibTableColumn
rpcGeneralMcastPktsRcvd = _RpcGeneralMcastPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 8),
    _RpcGeneralMcastPktsRcvd_Type()
)
rpcGeneralMcastPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralMcastPktsRcvd.setStatus("current")
_RpcGeneralMcastBytesSent_Type = Counter64
_RpcGeneralMcastBytesSent_Object = MibTableColumn
rpcGeneralMcastBytesSent = _RpcGeneralMcastBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 9),
    _RpcGeneralMcastBytesSent_Type()
)
rpcGeneralMcastBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralMcastBytesSent.setStatus("current")
_RpcGeneralMcastBytesRcvd_Type = Counter64
_RpcGeneralMcastBytesRcvd_Object = MibTableColumn
rpcGeneralMcastBytesRcvd = _RpcGeneralMcastBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 10),
    _RpcGeneralMcastBytesRcvd_Type()
)
rpcGeneralMcastBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralMcastBytesRcvd.setStatus("current")
_RpcGeneralXmtPktsDropped_Type = Counter32
_RpcGeneralXmtPktsDropped_Object = MibTableColumn
rpcGeneralXmtPktsDropped = _RpcGeneralXmtPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 11),
    _RpcGeneralXmtPktsDropped_Type()
)
rpcGeneralXmtPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralXmtPktsDropped.setStatus("current")
_RpcGeneralRcvPktsDropped_Type = Counter32
_RpcGeneralRcvPktsDropped_Object = MibTableColumn
rpcGeneralRcvPktsDropped = _RpcGeneralRcvPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 12),
    _RpcGeneralRcvPktsDropped_Type()
)
rpcGeneralRcvPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralRcvPktsDropped.setStatus("current")
_RpcGeneralXmtPktsOutstanding_Type = Counter32
_RpcGeneralXmtPktsOutstanding_Object = MibTableColumn
rpcGeneralXmtPktsOutstanding = _RpcGeneralXmtPktsOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 13),
    _RpcGeneralXmtPktsOutstanding_Type()
)
rpcGeneralXmtPktsOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralXmtPktsOutstanding.setStatus("current")
_RpcGeneralIOBuffers_Type = Counter32
_RpcGeneralIOBuffers_Object = MibTableColumn
rpcGeneralIOBuffers = _RpcGeneralIOBuffers_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 14),
    _RpcGeneralIOBuffers_Type()
)
rpcGeneralIOBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralIOBuffers.setStatus("current")
_RpcGeneralPktXmtRate_Type = Gauge32
_RpcGeneralPktXmtRate_Object = MibTableColumn
rpcGeneralPktXmtRate = _RpcGeneralPktXmtRate_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 15),
    _RpcGeneralPktXmtRate_Type()
)
rpcGeneralPktXmtRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralPktXmtRate.setStatus("current")
if mibBuilder.loadTexts:
    rpcGeneralPktXmtRate.setUnits("Packets Per Second")
_RpcGeneralPktRcvRate_Type = Gauge32
_RpcGeneralPktRcvRate_Object = MibTableColumn
rpcGeneralPktRcvRate = _RpcGeneralPktRcvRate_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 16),
    _RpcGeneralPktRcvRate_Type()
)
rpcGeneralPktRcvRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralPktRcvRate.setStatus("current")
if mibBuilder.loadTexts:
    rpcGeneralPktRcvRate.setUnits("Packets Per Second")
_RpcGeneralPortRateLimitDrops_Type = Counter64
_RpcGeneralPortRateLimitDrops_Object = MibTableColumn
rpcGeneralPortRateLimitDrops = _RpcGeneralPortRateLimitDrops_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 17),
    _RpcGeneralPortRateLimitDrops_Type()
)
rpcGeneralPortRateLimitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralPortRateLimitDrops.setStatus("current")
_RpcGeneralPortPoliceDrops_Type = Counter64
_RpcGeneralPortPoliceDrops_Object = MibTableColumn
rpcGeneralPortPoliceDrops = _RpcGeneralPortPoliceDrops_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 18),
    _RpcGeneralPortPoliceDrops_Type()
)
rpcGeneralPortPoliceDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralPortPoliceDrops.setStatus("current")
_RpcGeneralCctRateLimitDrops_Type = Counter64
_RpcGeneralCctRateLimitDrops_Object = MibTableColumn
rpcGeneralCctRateLimitDrops = _RpcGeneralCctRateLimitDrops_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 19),
    _RpcGeneralCctRateLimitDrops_Type()
)
rpcGeneralCctRateLimitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralCctRateLimitDrops.setStatus("current")
_RpcGeneralCctPoliceDrops_Type = Counter64
_RpcGeneralCctPoliceDrops_Object = MibTableColumn
rpcGeneralCctPoliceDrops = _RpcGeneralCctPoliceDrops_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 20),
    _RpcGeneralCctPoliceDrops_Type()
)
rpcGeneralCctPoliceDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralCctPoliceDrops.setStatus("current")
_RpcGeneralFwdMemUsed_Type = Gauge32
_RpcGeneralFwdMemUsed_Object = MibTableColumn
rpcGeneralFwdMemUsed = _RpcGeneralFwdMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 21),
    _RpcGeneralFwdMemUsed_Type()
)
rpcGeneralFwdMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralFwdMemUsed.setStatus("current")
if mibBuilder.loadTexts:
    rpcGeneralFwdMemUsed.setUnits("Bytes")
_RpcGeneralFloodQFailures_Type = Counter32
_RpcGeneralFloodQFailures_Object = MibTableColumn
rpcGeneralFloodQFailures = _RpcGeneralFloodQFailures_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 1, 1, 22),
    _RpcGeneralFloodQFailures_Type()
)
rpcGeneralFloodQFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcGeneralFloodQFailures.setStatus("current")
_RpcAtmTable_Object = MibTable
rpcAtmTable = _RpcAtmTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rpcAtmTable.setStatus("current")
_RpcAtmEntry_Object = MibTableRow
rpcAtmEntry = _RpcAtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1)
)
rpcAtmEntry.setIndexNames(
    (0, "RBN-PORT-COUNTERS-MIB", "rpcSlotID"),
    (0, "RBN-PORT-COUNTERS-MIB", "rpcPortID"),
)
if mibBuilder.loadTexts:
    rpcAtmEntry.setStatus("current")
_RpcAtmSegOutCells_Type = Counter64
_RpcAtmSegOutCells_Object = MibTableColumn
rpcAtmSegOutCells = _RpcAtmSegOutCells_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 1),
    _RpcAtmSegOutCells_Type()
)
rpcAtmSegOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmSegOutCells.setStatus("current")
_RpcAtmRsmInCells_Type = Counter64
_RpcAtmRsmInCells_Object = MibTableColumn
rpcAtmRsmInCells = _RpcAtmRsmInCells_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 2),
    _RpcAtmRsmInCells_Type()
)
rpcAtmRsmInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmRsmInCells.setStatus("current")
_RpcAtmRsmInDrops_Type = Counter64
_RpcAtmRsmInDrops_Object = MibTableColumn
rpcAtmRsmInDrops = _RpcAtmRsmInDrops_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 3),
    _RpcAtmRsmInDrops_Type()
)
rpcAtmRsmInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmRsmInDrops.setStatus("current")
_RpcAtmRsmLengthErrs_Type = Counter32
_RpcAtmRsmLengthErrs_Object = MibTableColumn
rpcAtmRsmLengthErrs = _RpcAtmRsmLengthErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 4),
    _RpcAtmRsmLengthErrs_Type()
)
rpcAtmRsmLengthErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmRsmLengthErrs.setStatus("current")
_RpcAtmRsmPadErrs_Type = Counter32
_RpcAtmRsmPadErrs_Object = MibTableColumn
rpcAtmRsmPadErrs = _RpcAtmRsmPadErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 5),
    _RpcAtmRsmPadErrs_Type()
)
rpcAtmRsmPadErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmRsmPadErrs.setStatus("current")
_RpcAtmRsmCpiErrs_Type = Counter32
_RpcAtmRsmCpiErrs_Object = MibTableColumn
rpcAtmRsmCpiErrs = _RpcAtmRsmCpiErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 6),
    _RpcAtmRsmCpiErrs_Type()
)
rpcAtmRsmCpiErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmRsmCpiErrs.setStatus("current")
_RpcAtmRsmCrcErrs_Type = Counter32
_RpcAtmRsmCrcErrs_Object = MibTableColumn
rpcAtmRsmCrcErrs = _RpcAtmRsmCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 7),
    _RpcAtmRsmCrcErrs_Type()
)
rpcAtmRsmCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmRsmCrcErrs.setStatus("current")
_RpcAtmRsmTimeoutErrs_Type = Counter32
_RpcAtmRsmTimeoutErrs_Object = MibTableColumn
rpcAtmRsmTimeoutErrs = _RpcAtmRsmTimeoutErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 8),
    _RpcAtmRsmTimeoutErrs_Type()
)
rpcAtmRsmTimeoutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmRsmTimeoutErrs.setStatus("current")
_RpcAtmHostPciBusErrs_Type = Counter32
_RpcAtmHostPciBusErrs_Object = MibTableColumn
rpcAtmHostPciBusErrs = _RpcAtmHostPciBusErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 9),
    _RpcAtmHostPciBusErrs_Type()
)
rpcAtmHostPciBusErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmHostPciBusErrs.setStatus("current")
_RpcAtmHostDmaAfullErrs_Type = Counter32
_RpcAtmHostDmaAfullErrs_Object = MibTableColumn
rpcAtmHostDmaAfullErrs = _RpcAtmHostDmaAfullErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 10),
    _RpcAtmHostDmaAfullErrs_Type()
)
rpcAtmHostDmaAfullErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmHostDmaAfullErrs.setStatus("current")
_RpcAtmHostFrParityErrs_Type = Counter32
_RpcAtmHostFrParityErrs_Object = MibTableColumn
rpcAtmHostFrParityErrs = _RpcAtmHostFrParityErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 11),
    _RpcAtmHostFrParityErrs_Type()
)
rpcAtmHostFrParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmHostFrParityErrs.setStatus("current")
_RpcAtmHostFrSyncErrs_Type = Counter32
_RpcAtmHostFrSyncErrs_Object = MibTableColumn
rpcAtmHostFrSyncErrs = _RpcAtmHostFrSyncErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 12),
    _RpcAtmHostFrSyncErrs_Type()
)
rpcAtmHostFrSyncErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmHostFrSyncErrs.setStatus("current")
_RpcAtmXmtResetCnt_Type = Counter32
_RpcAtmXmtResetCnt_Object = MibTableColumn
rpcAtmXmtResetCnt = _RpcAtmXmtResetCnt_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 13),
    _RpcAtmXmtResetCnt_Type()
)
rpcAtmXmtResetCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmXmtResetCnt.setStatus("current")
_RpcAtmRcvResetCnt_Type = Counter32
_RpcAtmRcvResetCnt_Object = MibTableColumn
rpcAtmRcvResetCnt = _RpcAtmRcvResetCnt_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 14),
    _RpcAtmRcvResetCnt_Type()
)
rpcAtmRcvResetCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmRcvResetCnt.setStatus("current")
_RpcAtmSegStatusqOvflErrs_Type = Counter32
_RpcAtmSegStatusqOvflErrs_Object = MibTableColumn
rpcAtmSegStatusqOvflErrs = _RpcAtmSegStatusqOvflErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 15),
    _RpcAtmSegStatusqOvflErrs_Type()
)
rpcAtmSegStatusqOvflErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmSegStatusqOvflErrs.setStatus("current")
_RpcAtmSegNullSbdInfoErrs_Type = Counter32
_RpcAtmSegNullSbdInfoErrs_Object = MibTableColumn
rpcAtmSegNullSbdInfoErrs = _RpcAtmSegNullSbdInfoErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 16),
    _RpcAtmSegNullSbdInfoErrs_Type()
)
rpcAtmSegNullSbdInfoErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmSegNullSbdInfoErrs.setStatus("current")
_RpcAtmSegGetSbdInfoErrs_Type = Counter32
_RpcAtmSegGetSbdInfoErrs_Object = MibTableColumn
rpcAtmSegGetSbdInfoErrs = _RpcAtmSegGetSbdInfoErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 17),
    _RpcAtmSegGetSbdInfoErrs_Type()
)
rpcAtmSegGetSbdInfoErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmSegGetSbdInfoErrs.setStatus("current")
_RpcAtmSegUndfErrs_Type = Counter32
_RpcAtmSegUndfErrs_Object = MibTableColumn
rpcAtmSegUndfErrs = _RpcAtmSegUndfErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 18),
    _RpcAtmSegUndfErrs_Type()
)
rpcAtmSegUndfErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmSegUndfErrs.setStatus("current")
_RpcAtmSegHostStatusFull_Type = Counter32
_RpcAtmSegHostStatusFull_Object = MibTableColumn
rpcAtmSegHostStatusFull = _RpcAtmSegHostStatusFull_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 19),
    _RpcAtmSegHostStatusFull_Type()
)
rpcAtmSegHostStatusFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmSegHostStatusFull.setStatus("current")
_RpcAtmRsmStatusqOvflErrs_Type = Counter32
_RpcAtmRsmStatusqOvflErrs_Object = MibTableColumn
rpcAtmRsmStatusqOvflErrs = _RpcAtmRsmStatusqOvflErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 20),
    _RpcAtmRsmStatusqOvflErrs_Type()
)
rpcAtmRsmStatusqOvflErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmRsmStatusqOvflErrs.setStatus("current")
_RpcAtmRsmBaErrs_Type = Counter32
_RpcAtmRsmBaErrs_Object = MibTableColumn
rpcAtmRsmBaErrs = _RpcAtmRsmBaErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 21),
    _RpcAtmRsmBaErrs_Type()
)
rpcAtmRsmBaErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmRsmBaErrs.setStatus("current")
_RpcAtmRsmLenErrs_Type = Counter32
_RpcAtmRsmLenErrs_Object = MibTableColumn
rpcAtmRsmLenErrs = _RpcAtmRsmLenErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 22),
    _RpcAtmRsmLenErrs_Type()
)
rpcAtmRsmLenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmRsmLenErrs.setStatus("current")
_RpcAtmRsmFfpdErrs_Type = Counter32
_RpcAtmRsmFfpdErrs_Object = MibTableColumn
rpcAtmRsmFfpdErrs = _RpcAtmRsmFfpdErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 23),
    _RpcAtmRsmFfpdErrs_Type()
)
rpcAtmRsmFfpdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmRsmFfpdErrs.setStatus("current")
_RpcAtmRsmEpdErrs_Type = Counter32
_RpcAtmRsmEpdErrs_Object = MibTableColumn
rpcAtmRsmEpdErrs = _RpcAtmRsmEpdErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 24),
    _RpcAtmRsmEpdErrs_Type()
)
rpcAtmRsmEpdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmRsmEpdErrs.setStatus("current")
_RpcAtmRsmUndfErrs_Type = Counter32
_RpcAtmRsmUndfErrs_Object = MibTableColumn
rpcAtmRsmUndfErrs = _RpcAtmRsmUndfErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 25),
    _RpcAtmRsmUndfErrs_Type()
)
rpcAtmRsmUndfErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmRsmUndfErrs.setStatus("current")
_RpcAtmRsmOvflErrs_Type = Counter32
_RpcAtmRsmOvflErrs_Object = MibTableColumn
rpcAtmRsmOvflErrs = _RpcAtmRsmOvflErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 26),
    _RpcAtmRsmOvflErrs_Type()
)
rpcAtmRsmOvflErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmRsmOvflErrs.setStatus("current")
_RpcAtmRsmSfpdErrs_Type = Counter32
_RpcAtmRsmSfpdErrs_Object = MibTableColumn
rpcAtmRsmSfpdErrs = _RpcAtmRsmSfpdErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 27),
    _RpcAtmRsmSfpdErrs_Type()
)
rpcAtmRsmSfpdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmRsmSfpdErrs.setStatus("current")
_RpcAtmRsmAbortErrs_Type = Counter32
_RpcAtmRsmAbortErrs_Object = MibTableColumn
rpcAtmRsmAbortErrs = _RpcAtmRsmAbortErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 28),
    _RpcAtmRsmAbortErrs_Type()
)
rpcAtmRsmAbortErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmRsmAbortErrs.setStatus("current")
_RpcAtmOnDemandAttempts_Type = Counter32
_RpcAtmOnDemandAttempts_Object = MibTableColumn
rpcAtmOnDemandAttempts = _RpcAtmOnDemandAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 29),
    _RpcAtmOnDemandAttempts_Type()
)
rpcAtmOnDemandAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOnDemandAttempts.setStatus("current")
_RpcAtmOnDemandErrs_Type = Counter32
_RpcAtmOnDemandErrs_Object = MibTableColumn
rpcAtmOnDemandErrs = _RpcAtmOnDemandErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 30),
    _RpcAtmOnDemandErrs_Type()
)
rpcAtmOnDemandErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOnDemandErrs.setStatus("current")
_RpcAtmOamOutCells_Type = Counter64
_RpcAtmOamOutCells_Object = MibTableColumn
rpcAtmOamOutCells = _RpcAtmOamOutCells_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 31),
    _RpcAtmOamOutCells_Type()
)
rpcAtmOamOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOamOutCells.setStatus("current")
_RpcAtmOamInCells_Type = Counter64
_RpcAtmOamInCells_Object = MibTableColumn
rpcAtmOamInCells = _RpcAtmOamInCells_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 32),
    _RpcAtmOamInCells_Type()
)
rpcAtmOamInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOamInCells.setStatus("current")
_RpcAtmOamInF4Segments_Type = Counter64
_RpcAtmOamInF4Segments_Object = MibTableColumn
rpcAtmOamInF4Segments = _RpcAtmOamInF4Segments_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 33),
    _RpcAtmOamInF4Segments_Type()
)
rpcAtmOamInF4Segments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOamInF4Segments.setStatus("current")
_RpcAtmOamInF4EndToEnds_Type = Counter64
_RpcAtmOamInF4EndToEnds_Object = MibTableColumn
rpcAtmOamInF4EndToEnds = _RpcAtmOamInF4EndToEnds_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 34),
    _RpcAtmOamInF4EndToEnds_Type()
)
rpcAtmOamInF4EndToEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOamInF4EndToEnds.setStatus("current")
_RpcAtmOamInF5Segments_Type = Counter64
_RpcAtmOamInF5Segments_Object = MibTableColumn
rpcAtmOamInF5Segments = _RpcAtmOamInF5Segments_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 35),
    _RpcAtmOamInF5Segments_Type()
)
rpcAtmOamInF5Segments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOamInF5Segments.setStatus("current")
_RpcAtmOamInF5EndToEnds_Type = Counter64
_RpcAtmOamInF5EndToEnds_Object = MibTableColumn
rpcAtmOamInF5EndToEnds = _RpcAtmOamInF5EndToEnds_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 36),
    _RpcAtmOamInF5EndToEnds_Type()
)
rpcAtmOamInF5EndToEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOamInF5EndToEnds.setStatus("current")
_RpcAtmOamInPti6s_Type = Counter64
_RpcAtmOamInPti6s_Object = MibTableColumn
rpcAtmOamInPti6s = _RpcAtmOamInPti6s_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 37),
    _RpcAtmOamInPti6s_Type()
)
rpcAtmOamInPti6s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOamInPti6s.setStatus("current")
_RpcAtmOamInPti7s_Type = Counter64
_RpcAtmOamInPti7s_Object = MibTableColumn
rpcAtmOamInPti7s = _RpcAtmOamInPti7s_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 38),
    _RpcAtmOamInPti7s_Type()
)
rpcAtmOamInPti7s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOamInPti7s.setStatus("current")
_RpcAtmOamOutLoopbacks_Type = Counter64
_RpcAtmOamOutLoopbacks_Object = MibTableColumn
rpcAtmOamOutLoopbacks = _RpcAtmOamOutLoopbacks_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 39),
    _RpcAtmOamOutLoopbacks_Type()
)
rpcAtmOamOutLoopbacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOamOutLoopbacks.setStatus("current")
_RpcAtmOamInLoopbacks_Type = Counter64
_RpcAtmOamInLoopbacks_Object = MibTableColumn
rpcAtmOamInLoopbacks = _RpcAtmOamInLoopbacks_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 40),
    _RpcAtmOamInLoopbacks_Type()
)
rpcAtmOamInLoopbacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOamInLoopbacks.setStatus("current")
_RpcAtmOamOutLoopbackResponses_Type = Counter64
_RpcAtmOamOutLoopbackResponses_Object = MibTableColumn
rpcAtmOamOutLoopbackResponses = _RpcAtmOamOutLoopbackResponses_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 41),
    _RpcAtmOamOutLoopbackResponses_Type()
)
rpcAtmOamOutLoopbackResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOamOutLoopbackResponses.setStatus("current")
_RpcAtmOamInLoopbackResponses_Type = Counter64
_RpcAtmOamInLoopbackResponses_Object = MibTableColumn
rpcAtmOamInLoopbackResponses = _RpcAtmOamInLoopbackResponses_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 42),
    _RpcAtmOamInLoopbackResponses_Type()
)
rpcAtmOamInLoopbackResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOamInLoopbackResponses.setStatus("current")
_RpcAtmOamOutAises_Type = Counter64
_RpcAtmOamOutAises_Object = MibTableColumn
rpcAtmOamOutAises = _RpcAtmOamOutAises_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 43),
    _RpcAtmOamOutAises_Type()
)
rpcAtmOamOutAises.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOamOutAises.setStatus("current")
_RpcAtmOamInAises_Type = Counter64
_RpcAtmOamInAises_Object = MibTableColumn
rpcAtmOamInAises = _RpcAtmOamInAises_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 44),
    _RpcAtmOamInAises_Type()
)
rpcAtmOamInAises.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOamInAises.setStatus("current")
_RpcAtmOamOutRdis_Type = Counter64
_RpcAtmOamOutRdis_Object = MibTableColumn
rpcAtmOamOutRdis = _RpcAtmOamOutRdis_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 45),
    _RpcAtmOamOutRdis_Type()
)
rpcAtmOamOutRdis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOamOutRdis.setStatus("current")
_RpcAtmOamInRdis_Type = Counter64
_RpcAtmOamInRdis_Object = MibTableColumn
rpcAtmOamInRdis = _RpcAtmOamInRdis_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 46),
    _RpcAtmOamInRdis_Type()
)
rpcAtmOamInRdis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOamInRdis.setStatus("current")


class _RpcAtmOamLineStatus_Type(Bits):
    """Custom type rpcAtmOamLineStatus based on Bits"""
    namedValues = NamedValues(
        *(("ok", 0),
          ("los", 1),
          ("oof", 2),
          ("lop", 3),
          ("ais", 4),
          ("yellow", 5),
          ("ferf", 6),
          ("febe", 7),
          ("febeLrei", 8),
          ("b2BipErr", 9),
          ("b2Sd", 10),
          ("b2Sf", 11),
          ("rai", 12),
          ("plcpOof", 13),
          ("plcpLof", 14),
          ("plcpYel", 15))
    )

_RpcAtmOamLineStatus_Type.__name__ = "Bits"
_RpcAtmOamLineStatus_Object = MibTableColumn
rpcAtmOamLineStatus = _RpcAtmOamLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 2, 1, 47),
    _RpcAtmOamLineStatus_Type()
)
rpcAtmOamLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOamLineStatus.setStatus("current")
_RpcAtmOc3Table_Object = MibTable
rpcAtmOc3Table = _RpcAtmOc3Table_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rpcAtmOc3Table.setStatus("current")
_RpcAtmOc3Entry_Object = MibTableRow
rpcAtmOc3Entry = _RpcAtmOc3Entry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1)
)
rpcAtmOc3Entry.setIndexNames(
    (0, "RBN-PORT-COUNTERS-MIB", "rpcSlotID"),
    (0, "RBN-PORT-COUNTERS-MIB", "rpcPortID"),
)
if mibBuilder.loadTexts:
    rpcAtmOc3Entry.setStatus("current")
_RpcAtmOc3LineFebeErrs_Type = Counter32
_RpcAtmOc3LineFebeErrs_Object = MibTableColumn
rpcAtmOc3LineFebeErrs = _RpcAtmOc3LineFebeErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 1),
    _RpcAtmOc3LineFebeErrs_Type()
)
rpcAtmOc3LineFebeErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3LineFebeErrs.setStatus("current")
_RpcAtmOc3LineFerfErrs_Type = Counter32
_RpcAtmOc3LineFerfErrs_Object = MibTableColumn
rpcAtmOc3LineFerfErrs = _RpcAtmOc3LineFerfErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 2),
    _RpcAtmOc3LineFerfErrs_Type()
)
rpcAtmOc3LineFerfErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3LineFerfErrs.setStatus("current")
_RpcAtmOc3LineAisErrs_Type = Counter32
_RpcAtmOc3LineAisErrs_Object = MibTableColumn
rpcAtmOc3LineAisErrs = _RpcAtmOc3LineAisErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 3),
    _RpcAtmOc3LineAisErrs_Type()
)
rpcAtmOc3LineAisErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3LineAisErrs.setStatus("current")
_RpcAtmOc3PathFebeErrs_Type = Counter32
_RpcAtmOc3PathFebeErrs_Object = MibTableColumn
rpcAtmOc3PathFebeErrs = _RpcAtmOc3PathFebeErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 4),
    _RpcAtmOc3PathFebeErrs_Type()
)
rpcAtmOc3PathFebeErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3PathFebeErrs.setStatus("current")
_RpcAtmOc3PathFerfErrs_Type = Counter32
_RpcAtmOc3PathFerfErrs_Object = MibTableColumn
rpcAtmOc3PathFerfErrs = _RpcAtmOc3PathFerfErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 5),
    _RpcAtmOc3PathFerfErrs_Type()
)
rpcAtmOc3PathFerfErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3PathFerfErrs.setStatus("current")
_RpcAtmOc3PathAisErrs_Type = Counter32
_RpcAtmOc3PathAisErrs_Object = MibTableColumn
rpcAtmOc3PathAisErrs = _RpcAtmOc3PathAisErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 6),
    _RpcAtmOc3PathAisErrs_Type()
)
rpcAtmOc3PathAisErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3PathAisErrs.setStatus("current")
_RpcAtmOc3PathYellowErrs_Type = Counter32
_RpcAtmOc3PathYellowErrs_Object = MibTableColumn
rpcAtmOc3PathYellowErrs = _RpcAtmOc3PathYellowErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 7),
    _RpcAtmOc3PathYellowErrs_Type()
)
rpcAtmOc3PathYellowErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3PathYellowErrs.setStatus("current")
_RpcAtmOc3StsLof23Errs_Type = Counter32
_RpcAtmOc3StsLof23Errs_Object = MibTableColumn
rpcAtmOc3StsLof23Errs = _RpcAtmOc3StsLof23Errs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 8),
    _RpcAtmOc3StsLof23Errs_Type()
)
rpcAtmOc3StsLof23Errs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3StsLof23Errs.setStatus("current")
_RpcAtmOc3StsLofErrs_Type = Counter32
_RpcAtmOc3StsLofErrs_Object = MibTableColumn
rpcAtmOc3StsLofErrs = _RpcAtmOc3StsLofErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 9),
    _RpcAtmOc3StsLofErrs_Type()
)
rpcAtmOc3StsLofErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3StsLofErrs.setStatus("current")
_RpcAtmOc3StsOofErrs_Type = Counter32
_RpcAtmOc3StsOofErrs_Object = MibTableColumn
rpcAtmOc3StsOofErrs = _RpcAtmOc3StsOofErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 10),
    _RpcAtmOc3StsOofErrs_Type()
)
rpcAtmOc3StsOofErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3StsOofErrs.setStatus("current")
_RpcAtmOc3StsLopErrs_Type = Counter32
_RpcAtmOc3StsLopErrs_Object = MibTableColumn
rpcAtmOc3StsLopErrs = _RpcAtmOc3StsLopErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 11),
    _RpcAtmOc3StsLopErrs_Type()
)
rpcAtmOc3StsLopErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3StsLopErrs.setStatus("current")
_RpcAtmOc3BipErrs_Type = Counter32
_RpcAtmOc3BipErrs_Object = MibTableColumn
rpcAtmOc3BipErrs = _RpcAtmOc3BipErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 12),
    _RpcAtmOc3BipErrs_Type()
)
rpcAtmOc3BipErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3BipErrs.setStatus("current")
_RpcAtmOc3B1Bip8_Type = Counter32
_RpcAtmOc3B1Bip8_Object = MibTableColumn
rpcAtmOc3B1Bip8 = _RpcAtmOc3B1Bip8_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 13),
    _RpcAtmOc3B1Bip8_Type()
)
rpcAtmOc3B1Bip8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3B1Bip8.setStatus("current")
_RpcAtmOc3B2Bip824_Type = Counter32
_RpcAtmOc3B2Bip824_Object = MibTableColumn
rpcAtmOc3B2Bip824 = _RpcAtmOc3B2Bip824_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 14),
    _RpcAtmOc3B2Bip824_Type()
)
rpcAtmOc3B2Bip824.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3B2Bip824.setStatus("current")
_RpcAtmOc3B3Bip8_Type = Counter32
_RpcAtmOc3B3Bip8_Object = MibTableColumn
rpcAtmOc3B3Bip8 = _RpcAtmOc3B3Bip8_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 15),
    _RpcAtmOc3B3Bip8_Type()
)
rpcAtmOc3B3Bip8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3B3Bip8.setStatus("current")
_RpcAtmOc3LocErrs_Type = Counter32
_RpcAtmOc3LocErrs_Object = MibTableColumn
rpcAtmOc3LocErrs = _RpcAtmOc3LocErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 16),
    _RpcAtmOc3LocErrs_Type()
)
rpcAtmOc3LocErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3LocErrs.setStatus("current")
_RpcAtmOc3LosErrs_Type = Counter32
_RpcAtmOc3LosErrs_Object = MibTableColumn
rpcAtmOc3LosErrs = _RpcAtmOc3LosErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 17),
    _RpcAtmOc3LosErrs_Type()
)
rpcAtmOc3LosErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3LosErrs.setStatus("current")
_RpcAtmOc3Plm_Type = Counter32
_RpcAtmOc3Plm_Object = MibTableColumn
rpcAtmOc3Plm = _RpcAtmOc3Plm_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 18),
    _RpcAtmOc3Plm_Type()
)
rpcAtmOc3Plm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3Plm.setStatus("current")


class _RpcAtmOc3SectionStatus_Type(Bits):
    """Custom type rpcAtmOc3SectionStatus based on Bits"""
    namedValues = NamedValues(
        *(("ok", 0),
          ("oof", 1),
          ("los", 2),
          ("lof", 3),
          ("b1BipErr", 4))
    )

_RpcAtmOc3SectionStatus_Type.__name__ = "Bits"
_RpcAtmOc3SectionStatus_Object = MibTableColumn
rpcAtmOc3SectionStatus = _RpcAtmOc3SectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 19),
    _RpcAtmOc3SectionStatus_Type()
)
rpcAtmOc3SectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3SectionStatus.setStatus("current")


class _RpcAtmOc3PathStatus_Type(Bits):
    """Custom type rpcAtmOc3PathStatus based on Bits"""
    namedValues = NamedValues(
        *(("ok", 0),
          ("ais", 1),
          ("yellow", 2),
          ("ferf", 3),
          ("sigMismatch", 4),
          ("b3BipErr", 5),
          ("febe", 6),
          ("plm", 7),
          ("uneq", 8))
    )

_RpcAtmOc3PathStatus_Type.__name__ = "Bits"
_RpcAtmOc3PathStatus_Object = MibTableColumn
rpcAtmOc3PathStatus = _RpcAtmOc3PathStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 3, 1, 20),
    _RpcAtmOc3PathStatus_Type()
)
rpcAtmOc3PathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc3PathStatus.setStatus("current")
_RpcAtmDs3Table_Object = MibTable
rpcAtmDs3Table = _RpcAtmDs3Table_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4)
)
if mibBuilder.loadTexts:
    rpcAtmDs3Table.setStatus("current")
_RpcAtmDs3Entry_Object = MibTableRow
rpcAtmDs3Entry = _RpcAtmDs3Entry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4, 1)
)
rpcAtmDs3Entry.setIndexNames(
    (0, "RBN-PORT-COUNTERS-MIB", "rpcSlotID"),
    (0, "RBN-PORT-COUNTERS-MIB", "rpcPortID"),
)
if mibBuilder.loadTexts:
    rpcAtmDs3Entry.setStatus("current")
_RpcAtmDs3PlcpFebeErrs_Type = Counter32
_RpcAtmDs3PlcpFebeErrs_Object = MibTableColumn
rpcAtmDs3PlcpFebeErrs = _RpcAtmDs3PlcpFebeErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4, 1, 1),
    _RpcAtmDs3PlcpFebeErrs_Type()
)
rpcAtmDs3PlcpFebeErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmDs3PlcpFebeErrs.setStatus("current")
_RpcAtmDs3PlcpBipErrs_Type = Counter32
_RpcAtmDs3PlcpBipErrs_Object = MibTableColumn
rpcAtmDs3PlcpBipErrs = _RpcAtmDs3PlcpBipErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4, 1, 2),
    _RpcAtmDs3PlcpBipErrs_Type()
)
rpcAtmDs3PlcpBipErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmDs3PlcpBipErrs.setStatus("current")
_RpcAtmDs3PlcpFrameErrs_Type = Counter32
_RpcAtmDs3PlcpFrameErrs_Object = MibTableColumn
rpcAtmDs3PlcpFrameErrs = _RpcAtmDs3PlcpFrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4, 1, 3),
    _RpcAtmDs3PlcpFrameErrs_Type()
)
rpcAtmDs3PlcpFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmDs3PlcpFrameErrs.setStatus("current")
_RpcAtmDs3PlcpLofErrs_Type = Counter32
_RpcAtmDs3PlcpLofErrs_Object = MibTableColumn
rpcAtmDs3PlcpLofErrs = _RpcAtmDs3PlcpLofErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4, 1, 4),
    _RpcAtmDs3PlcpLofErrs_Type()
)
rpcAtmDs3PlcpLofErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmDs3PlcpLofErrs.setStatus("current")
_RpcAtmDs3PlcpOofErrs_Type = Counter32
_RpcAtmDs3PlcpOofErrs_Object = MibTableColumn
rpcAtmDs3PlcpOofErrs = _RpcAtmDs3PlcpOofErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4, 1, 5),
    _RpcAtmDs3PlcpOofErrs_Type()
)
rpcAtmDs3PlcpOofErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmDs3PlcpOofErrs.setStatus("current")
_RpcAtmDs3PlcpLof23Errs_Type = Counter32
_RpcAtmDs3PlcpLof23Errs_Object = MibTableColumn
rpcAtmDs3PlcpLof23Errs = _RpcAtmDs3PlcpLof23Errs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4, 1, 6),
    _RpcAtmDs3PlcpLof23Errs_Type()
)
rpcAtmDs3PlcpLof23Errs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmDs3PlcpLof23Errs.setStatus("current")
_RpcAtmDs3PlcpYellowErrs_Type = Counter32
_RpcAtmDs3PlcpYellowErrs_Object = MibTableColumn
rpcAtmDs3PlcpYellowErrs = _RpcAtmDs3PlcpYellowErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4, 1, 7),
    _RpcAtmDs3PlcpYellowErrs_Type()
)
rpcAtmDs3PlcpYellowErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmDs3PlcpYellowErrs.setStatus("current")
_RpcAtmDs3OofErrs_Type = Counter32
_RpcAtmDs3OofErrs_Object = MibTableColumn
rpcAtmDs3OofErrs = _RpcAtmDs3OofErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4, 1, 8),
    _RpcAtmDs3OofErrs_Type()
)
rpcAtmDs3OofErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmDs3OofErrs.setStatus("current")
_RpcAtmDs3AisErrs_Type = Counter32
_RpcAtmDs3AisErrs_Object = MibTableColumn
rpcAtmDs3AisErrs = _RpcAtmDs3AisErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4, 1, 9),
    _RpcAtmDs3AisErrs_Type()
)
rpcAtmDs3AisErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmDs3AisErrs.setStatus("current")
_RpcAtmDs3IdleCodes_Type = Counter32
_RpcAtmDs3IdleCodes_Object = MibTableColumn
rpcAtmDs3IdleCodes = _RpcAtmDs3IdleCodes_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4, 1, 10),
    _RpcAtmDs3IdleCodes_Type()
)
rpcAtmDs3IdleCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmDs3IdleCodes.setStatus("current")
_RpcAtmDs3XbitYellowErrs_Type = Counter32
_RpcAtmDs3XbitYellowErrs_Object = MibTableColumn
rpcAtmDs3XbitYellowErrs = _RpcAtmDs3XbitYellowErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4, 1, 11),
    _RpcAtmDs3XbitYellowErrs_Type()
)
rpcAtmDs3XbitYellowErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmDs3XbitYellowErrs.setStatus("current")
_RpcAtmDs3LosErrs_Type = Counter32
_RpcAtmDs3LosErrs_Object = MibTableColumn
rpcAtmDs3LosErrs = _RpcAtmDs3LosErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4, 1, 12),
    _RpcAtmDs3LosErrs_Type()
)
rpcAtmDs3LosErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmDs3LosErrs.setStatus("current")
_RpcAtmDs3LCVs_Type = Counter32
_RpcAtmDs3LCVs_Object = MibTableColumn
rpcAtmDs3LCVs = _RpcAtmDs3LCVs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4, 1, 13),
    _RpcAtmDs3LCVs_Type()
)
rpcAtmDs3LCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmDs3LCVs.setStatus("current")
_RpcAtmDs3FrameErrs_Type = Counter32
_RpcAtmDs3FrameErrs_Object = MibTableColumn
rpcAtmDs3FrameErrs = _RpcAtmDs3FrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4, 1, 14),
    _RpcAtmDs3FrameErrs_Type()
)
rpcAtmDs3FrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmDs3FrameErrs.setStatus("current")
_RpcAtmDs3ParityErrs_Type = Counter32
_RpcAtmDs3ParityErrs_Object = MibTableColumn
rpcAtmDs3ParityErrs = _RpcAtmDs3ParityErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4, 1, 15),
    _RpcAtmDs3ParityErrs_Type()
)
rpcAtmDs3ParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmDs3ParityErrs.setStatus("current")
_RpcAtmDs3PathParityErrs_Type = Counter32
_RpcAtmDs3PathParityErrs_Object = MibTableColumn
rpcAtmDs3PathParityErrs = _RpcAtmDs3PathParityErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4, 1, 16),
    _RpcAtmDs3PathParityErrs_Type()
)
rpcAtmDs3PathParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmDs3PathParityErrs.setStatus("current")
_RpcAtmDs3FebeEvents_Type = Counter32
_RpcAtmDs3FebeEvents_Object = MibTableColumn
rpcAtmDs3FebeEvents = _RpcAtmDs3FebeEvents_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 4, 1, 17),
    _RpcAtmDs3FebeEvents_Type()
)
rpcAtmDs3FebeEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmDs3FebeEvents.setStatus("current")
_RpcAtmE3Table_Object = MibTable
rpcAtmE3Table = _RpcAtmE3Table_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5)
)
if mibBuilder.loadTexts:
    rpcAtmE3Table.setStatus("current")
_RpcAtmE3Entry_Object = MibTableRow
rpcAtmE3Entry = _RpcAtmE3Entry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1)
)
rpcAtmE3Entry.setIndexNames(
    (0, "RBN-PORT-COUNTERS-MIB", "rpcSlotID"),
    (0, "RBN-PORT-COUNTERS-MIB", "rpcPortID"),
)
if mibBuilder.loadTexts:
    rpcAtmE3Entry.setStatus("current")
_RpcAtmE3MaFebe_Type = Counter32
_RpcAtmE3MaFebe_Object = MibTableColumn
rpcAtmE3MaFebe = _RpcAtmE3MaFebe_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 1),
    _RpcAtmE3MaFebe_Type()
)
rpcAtmE3MaFebe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3MaFebe.setStatus("current")
_RpcAtmE3EmBip_Type = Counter32
_RpcAtmE3EmBip_Object = MibTableColumn
rpcAtmE3EmBip = _RpcAtmE3EmBip_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 2),
    _RpcAtmE3EmBip_Type()
)
rpcAtmE3EmBip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3EmBip.setStatus("current")
_RpcAtmE3MaFerf_Type = Counter32
_RpcAtmE3MaFerf_Object = MibTableColumn
rpcAtmE3MaFerf = _RpcAtmE3MaFerf_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 3),
    _RpcAtmE3MaFerf_Type()
)
rpcAtmE3MaFerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3MaFerf.setStatus("current")
_RpcAtmE3E3E4Lof_Type = Counter32
_RpcAtmE3E3E4Lof_Object = MibTableColumn
rpcAtmE3E3E4Lof = _RpcAtmE3E3E4Lof_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 4),
    _RpcAtmE3E3E4Lof_Type()
)
rpcAtmE3E3E4Lof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3E3E4Lof.setStatus("current")
_RpcAtmE3E3E4Oof_Type = Counter32
_RpcAtmE3E3E4Oof_Object = MibTableColumn
rpcAtmE3E3E4Oof = _RpcAtmE3E3E4Oof_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 5),
    _RpcAtmE3E3E4Oof_Type()
)
rpcAtmE3E3E4Oof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3E3E4Oof.setStatus("current")
_RpcAtmE3E3E4Lof23_Type = Counter32
_RpcAtmE3E3E4Lof23_Object = MibTableColumn
rpcAtmE3E3E4Lof23 = _RpcAtmE3E3E4Lof23_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 6),
    _RpcAtmE3E3E4Lof23_Type()
)
rpcAtmE3E3E4Lof23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3E3E4Lof23.setStatus("current")
_RpcAtmE3E3E4Ais_Type = Counter32
_RpcAtmE3E3E4Ais_Object = MibTableColumn
rpcAtmE3E3E4Ais = _RpcAtmE3E3E4Ais_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 7),
    _RpcAtmE3E3E4Ais_Type()
)
rpcAtmE3E3E4Ais.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3E3E4Ais.setStatus("current")
_RpcAtmE3Loc_Type = Counter32
_RpcAtmE3Loc_Object = MibTableColumn
rpcAtmE3Loc = _RpcAtmE3Loc_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 8),
    _RpcAtmE3Loc_Type()
)
rpcAtmE3Loc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3Loc.setStatus("current")
_RpcAtmE3PayloadMismatch_Type = Counter32
_RpcAtmE3PayloadMismatch_Object = MibTableColumn
rpcAtmE3PayloadMismatch = _RpcAtmE3PayloadMismatch_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 9),
    _RpcAtmE3PayloadMismatch_Type()
)
rpcAtmE3PayloadMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3PayloadMismatch.setStatus("current")
_RpcAtmE3PlcpFebe_Type = Counter32
_RpcAtmE3PlcpFebe_Object = MibTableColumn
rpcAtmE3PlcpFebe = _RpcAtmE3PlcpFebe_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 10),
    _RpcAtmE3PlcpFebe_Type()
)
rpcAtmE3PlcpFebe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3PlcpFebe.setStatus("current")
_RpcAtmE3PlcpBip_Type = Counter32
_RpcAtmE3PlcpBip_Object = MibTableColumn
rpcAtmE3PlcpBip = _RpcAtmE3PlcpBip_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 11),
    _RpcAtmE3PlcpBip_Type()
)
rpcAtmE3PlcpBip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3PlcpBip.setStatus("current")
_RpcAtmE3PlcpFrmErrs_Type = Counter32
_RpcAtmE3PlcpFrmErrs_Object = MibTableColumn
rpcAtmE3PlcpFrmErrs = _RpcAtmE3PlcpFrmErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 12),
    _RpcAtmE3PlcpFrmErrs_Type()
)
rpcAtmE3PlcpFrmErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3PlcpFrmErrs.setStatus("current")
_RpcAtmE3PlcpLof_Type = Counter32
_RpcAtmE3PlcpLof_Object = MibTableColumn
rpcAtmE3PlcpLof = _RpcAtmE3PlcpLof_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 13),
    _RpcAtmE3PlcpLof_Type()
)
rpcAtmE3PlcpLof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3PlcpLof.setStatus("current")
_RpcAtmE3PlcpOof_Type = Counter32
_RpcAtmE3PlcpOof_Object = MibTableColumn
rpcAtmE3PlcpOof = _RpcAtmE3PlcpOof_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 14),
    _RpcAtmE3PlcpOof_Type()
)
rpcAtmE3PlcpOof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3PlcpOof.setStatus("current")
_RpcAtmE3PlcpLof23_Type = Counter32
_RpcAtmE3PlcpLof23_Object = MibTableColumn
rpcAtmE3PlcpLof23 = _RpcAtmE3PlcpLof23_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 15),
    _RpcAtmE3PlcpLof23_Type()
)
rpcAtmE3PlcpLof23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3PlcpLof23.setStatus("current")
_RpcAtmE3PlcpYellow_Type = Counter32
_RpcAtmE3PlcpYellow_Object = MibTableColumn
rpcAtmE3PlcpYellow = _RpcAtmE3PlcpYellow_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 16),
    _RpcAtmE3PlcpYellow_Type()
)
rpcAtmE3PlcpYellow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3PlcpYellow.setStatus("current")
_RpcAtmE3Ais_Type = Counter32
_RpcAtmE3Ais_Object = MibTableColumn
rpcAtmE3Ais = _RpcAtmE3Ais_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 17),
    _RpcAtmE3Ais_Type()
)
rpcAtmE3Ais.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3Ais.setStatus("current")
_RpcAtmE3Oof_Type = Counter32
_RpcAtmE3Oof_Object = MibTableColumn
rpcAtmE3Oof = _RpcAtmE3Oof_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 18),
    _RpcAtmE3Oof_Type()
)
rpcAtmE3Oof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3Oof.setStatus("current")
_RpcAtmE3AbitYel_Type = Counter32
_RpcAtmE3AbitYel_Object = MibTableColumn
rpcAtmE3AbitYel = _RpcAtmE3AbitYel_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 19),
    _RpcAtmE3AbitYel_Type()
)
rpcAtmE3AbitYel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3AbitYel.setStatus("current")
_RpcAtmE3FebeAllOnes_Type = Counter32
_RpcAtmE3FebeAllOnes_Object = MibTableColumn
rpcAtmE3FebeAllOnes = _RpcAtmE3FebeAllOnes_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 20),
    _RpcAtmE3FebeAllOnes_Type()
)
rpcAtmE3FebeAllOnes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3FebeAllOnes.setStatus("current")
_RpcAtmE3FAS_Type = Counter32
_RpcAtmE3FAS_Object = MibTableColumn
rpcAtmE3FAS = _RpcAtmE3FAS_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 21),
    _RpcAtmE3FAS_Type()
)
rpcAtmE3FAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3FAS.setStatus("current")
_RpcAtmE3Los_Type = Counter32
_RpcAtmE3Los_Object = MibTableColumn
rpcAtmE3Los = _RpcAtmE3Los_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 22),
    _RpcAtmE3Los_Type()
)
rpcAtmE3Los.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3Los.setStatus("current")
_RpcAtmE3LCV_Type = Counter32
_RpcAtmE3LCV_Object = MibTableColumn
rpcAtmE3LCV = _RpcAtmE3LCV_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 23),
    _RpcAtmE3LCV_Type()
)
rpcAtmE3LCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3LCV.setStatus("current")
_RpcAtmE3LocalAlarmOn_Type = TruthValue
_RpcAtmE3LocalAlarmOn_Object = MibTableColumn
rpcAtmE3LocalAlarmOn = _RpcAtmE3LocalAlarmOn_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 24),
    _RpcAtmE3LocalAlarmOn_Type()
)
rpcAtmE3LocalAlarmOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3LocalAlarmOn.setStatus("current")
_RpcAtmE3RemoteAlarmOn_Type = TruthValue
_RpcAtmE3RemoteAlarmOn_Object = MibTableColumn
rpcAtmE3RemoteAlarmOn = _RpcAtmE3RemoteAlarmOn_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 25),
    _RpcAtmE3RemoteAlarmOn_Type()
)
rpcAtmE3RemoteAlarmOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3RemoteAlarmOn.setStatus("current")
_RpcAtmE3LinkUp_Type = TruthValue
_RpcAtmE3LinkUp_Object = MibTableColumn
rpcAtmE3LinkUp = _RpcAtmE3LinkUp_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 5, 1, 26),
    _RpcAtmE3LinkUp_Type()
)
rpcAtmE3LinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmE3LinkUp.setStatus("current")
_RpcAtmOc12Table_Object = MibTable
rpcAtmOc12Table = _RpcAtmOc12Table_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6)
)
if mibBuilder.loadTexts:
    rpcAtmOc12Table.setStatus("current")
_RpcAtmOc12Entry_Object = MibTableRow
rpcAtmOc12Entry = _RpcAtmOc12Entry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1)
)
rpcAtmOc12Entry.setIndexNames(
    (0, "RBN-PORT-COUNTERS-MIB", "rpcSlotID"),
    (0, "RBN-PORT-COUNTERS-MIB", "rpcPortID"),
)
if mibBuilder.loadTexts:
    rpcAtmOc12Entry.setStatus("current")
_RpcAtmOc12ParityErrs_Type = Counter32
_RpcAtmOc12ParityErrs_Object = MibTableColumn
rpcAtmOc12ParityErrs = _RpcAtmOc12ParityErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 1),
    _RpcAtmOc12ParityErrs_Type()
)
rpcAtmOc12ParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12ParityErrs.setStatus("current")
_RpcAtmOc12FifoUndrErrs_Type = Counter32
_RpcAtmOc12FifoUndrErrs_Object = MibTableColumn
rpcAtmOc12FifoUndrErrs = _RpcAtmOc12FifoUndrErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 2),
    _RpcAtmOc12FifoUndrErrs_Type()
)
rpcAtmOc12FifoUndrErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12FifoUndrErrs.setStatus("current")
_RpcAtmOc12B1Errs_Type = Counter32
_RpcAtmOc12B1Errs_Object = MibTableColumn
rpcAtmOc12B1Errs = _RpcAtmOc12B1Errs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 3),
    _RpcAtmOc12B1Errs_Type()
)
rpcAtmOc12B1Errs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12B1Errs.setStatus("current")
_RpcAtmOc12B2Errs_Type = Counter32
_RpcAtmOc12B2Errs_Object = MibTableColumn
rpcAtmOc12B2Errs = _RpcAtmOc12B2Errs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 4),
    _RpcAtmOc12B2Errs_Type()
)
rpcAtmOc12B2Errs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12B2Errs.setStatus("current")
_RpcAtmOc12M1Errs_Type = Counter32
_RpcAtmOc12M1Errs_Object = MibTableColumn
rpcAtmOc12M1Errs = _RpcAtmOc12M1Errs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 5),
    _RpcAtmOc12M1Errs_Type()
)
rpcAtmOc12M1Errs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12M1Errs.setStatus("current")
_RpcAtmOc12S1Errs_Type = Counter32
_RpcAtmOc12S1Errs_Object = MibTableColumn
rpcAtmOc12S1Errs = _RpcAtmOc12S1Errs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 6),
    _RpcAtmOc12S1Errs_Type()
)
rpcAtmOc12S1Errs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12S1Errs.setStatus("current")
_RpcAtmOc12J1OofErrs_Type = Counter32
_RpcAtmOc12J1OofErrs_Object = MibTableColumn
rpcAtmOc12J1OofErrs = _RpcAtmOc12J1OofErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 7),
    _RpcAtmOc12J1OofErrs_Type()
)
rpcAtmOc12J1OofErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12J1OofErrs.setStatus("current")
_RpcAtmOc12G1Errs_Type = Counter32
_RpcAtmOc12G1Errs_Object = MibTableColumn
rpcAtmOc12G1Errs = _RpcAtmOc12G1Errs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 8),
    _RpcAtmOc12G1Errs_Type()
)
rpcAtmOc12G1Errs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12G1Errs.setStatus("current")
_RpcAtmOc12B3Errs_Type = Counter32
_RpcAtmOc12B3Errs_Object = MibTableColumn
rpcAtmOc12B3Errs = _RpcAtmOc12B3Errs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 9),
    _RpcAtmOc12B3Errs_Type()
)
rpcAtmOc12B3Errs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12B3Errs.setStatus("current")
_RpcAtmOc12FifoOvflErrs_Type = Counter32
_RpcAtmOc12FifoOvflErrs_Object = MibTableColumn
rpcAtmOc12FifoOvflErrs = _RpcAtmOc12FifoOvflErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 10),
    _RpcAtmOc12FifoOvflErrs_Type()
)
rpcAtmOc12FifoOvflErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12FifoOvflErrs.setStatus("current")
_RpcAtmOc12K1Byte_Type = ApsK1K2
_RpcAtmOc12K1Byte_Object = MibTableColumn
rpcAtmOc12K1Byte = _RpcAtmOc12K1Byte_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 11),
    _RpcAtmOc12K1Byte_Type()
)
rpcAtmOc12K1Byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12K1Byte.setStatus("current")
_RpcAtmOc12K2Byte_Type = ApsK1K2
_RpcAtmOc12K2Byte_Object = MibTableColumn
rpcAtmOc12K2Byte = _RpcAtmOc12K2Byte_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 12),
    _RpcAtmOc12K2Byte_Type()
)
rpcAtmOc12K2Byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12K2Byte.setStatus("current")
_RpcAtmOc12S1Byte_Type = Counter32
_RpcAtmOc12S1Byte_Object = MibTableColumn
rpcAtmOc12S1Byte = _RpcAtmOc12S1Byte_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 13),
    _RpcAtmOc12S1Byte_Type()
)
rpcAtmOc12S1Byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12S1Byte.setStatus("current")
_RpcAtmOc12C2Byte_Type = Counter32
_RpcAtmOc12C2Byte_Object = MibTableColumn
rpcAtmOc12C2Byte = _RpcAtmOc12C2Byte_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 14),
    _RpcAtmOc12C2Byte_Type()
)
rpcAtmOc12C2Byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12C2Byte.setStatus("current")
_RpcAtmOc12G1Byte_Type = Counter32
_RpcAtmOc12G1Byte_Object = MibTableColumn
rpcAtmOc12G1Byte = _RpcAtmOc12G1Byte_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 15),
    _RpcAtmOc12G1Byte_Type()
)
rpcAtmOc12G1Byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12G1Byte.setStatus("current")


class _RpcAtmOc12J0Bytes_Type(OctetString):
    """Custom type rpcAtmOc12J0Bytes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_RpcAtmOc12J0Bytes_Type.__name__ = "OctetString"
_RpcAtmOc12J0Bytes_Object = MibTableColumn
rpcAtmOc12J0Bytes = _RpcAtmOc12J0Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 16),
    _RpcAtmOc12J0Bytes_Type()
)
rpcAtmOc12J0Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12J0Bytes.setStatus("current")


class _RpcAtmOc12J1Bytes_Type(OctetString):
    """Custom type rpcAtmOc12J1Bytes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_RpcAtmOc12J1Bytes_Type.__name__ = "OctetString"
_RpcAtmOc12J1Bytes_Object = MibTableColumn
rpcAtmOc12J1Bytes = _RpcAtmOc12J1Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 17),
    _RpcAtmOc12J1Bytes_Type()
)
rpcAtmOc12J1Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12J1Bytes.setStatus("current")
_RpcAtmOc12TxHecErrs_Type = Counter32
_RpcAtmOc12TxHecErrs_Object = MibTableColumn
rpcAtmOc12TxHecErrs = _RpcAtmOc12TxHecErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 18),
    _RpcAtmOc12TxHecErrs_Type()
)
rpcAtmOc12TxHecErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12TxHecErrs.setStatus("current")
_RpcAtmOc12RxDiscardErrs_Type = Counter32
_RpcAtmOc12RxDiscardErrs_Object = MibTableColumn
rpcAtmOc12RxDiscardErrs = _RpcAtmOc12RxDiscardErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 19),
    _RpcAtmOc12RxDiscardErrs_Type()
)
rpcAtmOc12RxDiscardErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12RxDiscardErrs.setStatus("current")


class _RpcAtmOc12SectionStatus_Type(Bits):
    """Custom type rpcAtmOc12SectionStatus based on Bits"""
    namedValues = NamedValues(
        *(("ok", 0),
          ("oof", 1),
          ("los", 2),
          ("lof", 3),
          ("b1BipErr", 4))
    )

_RpcAtmOc12SectionStatus_Type.__name__ = "Bits"
_RpcAtmOc12SectionStatus_Object = MibTableColumn
rpcAtmOc12SectionStatus = _RpcAtmOc12SectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 20),
    _RpcAtmOc12SectionStatus_Type()
)
rpcAtmOc12SectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12SectionStatus.setStatus("current")


class _RpcAtmOc12PortStatus_Type(Bits):
    """Custom type rpcAtmOc12PortStatus based on Bits"""
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1),
          ("lalarm", 2),
          ("ralarm", 3))
    )

_RpcAtmOc12PortStatus_Type.__name__ = "Bits"
_RpcAtmOc12PortStatus_Object = MibTableColumn
rpcAtmOc12PortStatus = _RpcAtmOc12PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 6, 1, 21),
    _RpcAtmOc12PortStatus_Type()
)
rpcAtmOc12PortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcAtmOc12PortStatus.setStatus("current")
_RpcEthernetTable_Object = MibTable
rpcEthernetTable = _RpcEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7)
)
if mibBuilder.loadTexts:
    rpcEthernetTable.setStatus("current")
_RpcEthernetEntry_Object = MibTableRow
rpcEthernetEntry = _RpcEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1)
)
rpcEthernetEntry.setIndexNames(
    (0, "RBN-PORT-COUNTERS-MIB", "rpcSlotID"),
    (0, "RBN-PORT-COUNTERS-MIB", "rpcPortID"),
)
if mibBuilder.loadTexts:
    rpcEthernetEntry.setStatus("current")
_RpcEthernetJabber_Type = Counter64
_RpcEthernetJabber_Object = MibTableColumn
rpcEthernetJabber = _RpcEthernetJabber_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 1),
    _RpcEthernetJabber_Type()
)
rpcEthernetJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetJabber.setStatus("current")
_RpcEthernetUnderflow_Type = Counter64
_RpcEthernetUnderflow_Object = MibTableColumn
rpcEthernetUnderflow = _RpcEthernetUnderflow_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 2),
    _RpcEthernetUnderflow_Type()
)
rpcEthernetUnderflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetUnderflow.setStatus("current")
_RpcEthernetLostCarrier_Type = Counter64
_RpcEthernetLostCarrier_Object = MibTableColumn
rpcEthernetLostCarrier = _RpcEthernetLostCarrier_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 3),
    _RpcEthernetLostCarrier_Type()
)
rpcEthernetLostCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetLostCarrier.setStatus("current")
_RpcEthernetNoCarrier_Type = Counter64
_RpcEthernetNoCarrier_Object = MibTableColumn
rpcEthernetNoCarrier = _RpcEthernetNoCarrier_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 4),
    _RpcEthernetNoCarrier_Type()
)
rpcEthernetNoCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetNoCarrier.setStatus("current")
_RpcEthernetLateCollision_Type = Counter64
_RpcEthernetLateCollision_Object = MibTableColumn
rpcEthernetLateCollision = _RpcEthernetLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 5),
    _RpcEthernetLateCollision_Type()
)
rpcEthernetLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetLateCollision.setStatus("current")
_RpcEthernetExcessiveCollision_Type = Counter64
_RpcEthernetExcessiveCollision_Object = MibTableColumn
rpcEthernetExcessiveCollision = _RpcEthernetExcessiveCollision_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 6),
    _RpcEthernetExcessiveCollision_Type()
)
rpcEthernetExcessiveCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetExcessiveCollision.setStatus("current")
_RpcEthernetLinkFailure_Type = Counter64
_RpcEthernetLinkFailure_Object = MibTableColumn
rpcEthernetLinkFailure = _RpcEthernetLinkFailure_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 7),
    _RpcEthernetLinkFailure_Type()
)
rpcEthernetLinkFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetLinkFailure.setStatus("current")
_RpcEthernetDeferred_Type = Counter64
_RpcEthernetDeferred_Object = MibTableColumn
rpcEthernetDeferred = _RpcEthernetDeferred_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 8),
    _RpcEthernetDeferred_Type()
)
rpcEthernetDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetDeferred.setStatus("current")
_RpcEthernetOkWithCollision_Type = Counter64
_RpcEthernetOkWithCollision_Object = MibTableColumn
rpcEthernetOkWithCollision = _RpcEthernetOkWithCollision_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 9),
    _RpcEthernetOkWithCollision_Type()
)
rpcEthernetOkWithCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetOkWithCollision.setStatus("current")
_RpcEthernetReclaimed_Type = Counter64
_RpcEthernetReclaimed_Object = MibTableColumn
rpcEthernetReclaimed = _RpcEthernetReclaimed_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 10),
    _RpcEthernetReclaimed_Type()
)
rpcEthernetReclaimed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetReclaimed.setStatus("current")
_RpcEthernetDescripErrs_Type = Counter64
_RpcEthernetDescripErrs_Object = MibTableColumn
rpcEthernetDescripErrs = _RpcEthernetDescripErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 11),
    _RpcEthernetDescripErrs_Type()
)
rpcEthernetDescripErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetDescripErrs.setStatus("current")
_RpcEthernetOversizedFrames_Type = Counter64
_RpcEthernetOversizedFrames_Object = MibTableColumn
rpcEthernetOversizedFrames = _RpcEthernetOversizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 12),
    _RpcEthernetOversizedFrames_Type()
)
rpcEthernetOversizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetOversizedFrames.setStatus("current")
_RpcEthernetCollisions_Type = Counter64
_RpcEthernetCollisions_Object = MibTableColumn
rpcEthernetCollisions = _RpcEthernetCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 13),
    _RpcEthernetCollisions_Type()
)
rpcEthernetCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetCollisions.setStatus("current")
_RpcEthernetWatchdog_Type = Counter64
_RpcEthernetWatchdog_Object = MibTableColumn
rpcEthernetWatchdog = _RpcEthernetWatchdog_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 14),
    _RpcEthernetWatchdog_Type()
)
rpcEthernetWatchdog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetWatchdog.setStatus("current")
_RpcEthernetMiiErrs_Type = Counter64
_RpcEthernetMiiErrs_Object = MibTableColumn
rpcEthernetMiiErrs = _RpcEthernetMiiErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 15),
    _RpcEthernetMiiErrs_Type()
)
rpcEthernetMiiErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetMiiErrs.setStatus("current")
_RpcEthernetCrcErrs_Type = Counter64
_RpcEthernetCrcErrs_Object = MibTableColumn
rpcEthernetCrcErrs = _RpcEthernetCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 16),
    _RpcEthernetCrcErrs_Type()
)
rpcEthernetCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetCrcErrs.setStatus("current")
_RpcEthernetDribble_Type = Counter64
_RpcEthernetDribble_Object = MibTableColumn
rpcEthernetDribble = _RpcEthernetDribble_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 17),
    _RpcEthernetDribble_Type()
)
rpcEthernetDribble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetDribble.setStatus("current")
_RpcEthernetOverflow_Type = Counter64
_RpcEthernetOverflow_Object = MibTableColumn
rpcEthernetOverflow = _RpcEthernetOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 18),
    _RpcEthernetOverflow_Type()
)
rpcEthernetOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetOverflow.setStatus("current")
_RpcEthernetRuntFrames_Type = Counter64
_RpcEthernetRuntFrames_Object = MibTableColumn
rpcEthernetRuntFrames = _RpcEthernetRuntFrames_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 19),
    _RpcEthernetRuntFrames_Type()
)
rpcEthernetRuntFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetRuntFrames.setStatus("current")
_RpcEthernetBusParityErrs_Type = Counter64
_RpcEthernetBusParityErrs_Object = MibTableColumn
rpcEthernetBusParityErrs = _RpcEthernetBusParityErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 20),
    _RpcEthernetBusParityErrs_Type()
)
rpcEthernetBusParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetBusParityErrs.setStatus("current")
_RpcEthernetBusMasterAborts_Type = Counter64
_RpcEthernetBusMasterAborts_Object = MibTableColumn
rpcEthernetBusMasterAborts = _RpcEthernetBusMasterAborts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 21),
    _RpcEthernetBusMasterAborts_Type()
)
rpcEthernetBusMasterAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetBusMasterAborts.setStatus("current")
_RpcEthernetBusTargetAborts_Type = Counter64
_RpcEthernetBusTargetAborts_Object = MibTableColumn
rpcEthernetBusTargetAborts = _RpcEthernetBusTargetAborts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 22),
    _RpcEthernetBusTargetAborts_Type()
)
rpcEthernetBusTargetAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetBusTargetAborts.setStatus("current")
_RpcEthernetBusUnknownErrs_Type = Counter64
_RpcEthernetBusUnknownErrs_Object = MibTableColumn
rpcEthernetBusUnknownErrs = _RpcEthernetBusUnknownErrs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 1, 1, 7, 1, 23),
    _RpcEthernetBusUnknownErrs_Type()
)
rpcEthernetBusUnknownErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcEthernetBusUnknownErrs.setStatus("current")
_RpcMibConformance_ObjectIdentity = ObjectIdentity
rpcMibConformance = _RpcMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 2)
)
_RpcMibCompliances_ObjectIdentity = ObjectIdentity
rpcMibCompliances = _RpcMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 2, 1)
)
_RpcMibGroups_ObjectIdentity = ObjectIdentity
rpcMibGroups = _RpcMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 2, 2)
)

# Managed Objects groups

rpcGenCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 2, 2, 1)
)
rpcGenCountersGroup.setObjects(
      *(("RBN-PORT-COUNTERS-MIB", "rpcSlotID"),
        ("RBN-PORT-COUNTERS-MIB", "rpcPortID"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralPktsSent"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralPktsRcvd"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralBytesSent"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralBytesRcvd"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralMcastPktsSent"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralMcastPktsRcvd"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralMcastBytesSent"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralMcastBytesRcvd"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralXmtPktsDropped"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralRcvPktsDropped"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralXmtPktsOutstanding"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralIOBuffers"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralPktXmtRate"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralPktRcvRate"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralPortRateLimitDrops"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralPortPoliceDrops"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralCctRateLimitDrops"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralCctPoliceDrops"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralFwdMemUsed"),
        ("RBN-PORT-COUNTERS-MIB", "rpcGeneralFloodQFailures"))
)
if mibBuilder.loadTexts:
    rpcGenCountersGroup.setStatus("current")

rpcAtmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 2, 2, 2)
)
rpcAtmGroup.setObjects(
      *(("RBN-PORT-COUNTERS-MIB", "rpcAtmSegOutCells"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmRsmInCells"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmRsmInDrops"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmRsmLengthErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmRsmPadErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmRsmCpiErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmRsmCrcErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmRsmTimeoutErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmHostPciBusErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmHostDmaAfullErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmHostFrParityErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmHostFrSyncErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmXmtResetCnt"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmRcvResetCnt"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmSegStatusqOvflErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmSegNullSbdInfoErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmSegGetSbdInfoErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmSegUndfErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmSegHostStatusFull"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmRsmStatusqOvflErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmRsmBaErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmRsmLenErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmRsmFfpdErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmRsmEpdErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmRsmUndfErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmRsmOvflErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmRsmSfpdErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmRsmAbortErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOnDemandAttempts"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOnDemandErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOamOutCells"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOamInCells"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOamInF4Segments"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOamInF4EndToEnds"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOamInF5Segments"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOamInF5EndToEnds"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOamInPti6s"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOamInPti7s"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOamOutLoopbacks"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOamInLoopbacks"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOamOutLoopbackResponses"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOamInLoopbackResponses"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOamOutAises"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOamInAises"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOamOutRdis"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOamInRdis"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOamLineStatus"))
)
if mibBuilder.loadTexts:
    rpcAtmGroup.setStatus("current")

rpcAtmOc3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 2, 2, 3)
)
rpcAtmOc3Group.setObjects(
      *(("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3LineFebeErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3LineFerfErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3LineAisErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3PathFebeErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3PathFerfErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3PathAisErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3PathYellowErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3StsLof23Errs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3StsLofErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3StsOofErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3StsLopErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3BipErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3B1Bip8"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3B2Bip824"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3B3Bip8"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3LocErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3LosErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3Plm"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3SectionStatus"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc3PathStatus"))
)
if mibBuilder.loadTexts:
    rpcAtmOc3Group.setStatus("current")

rpcAtmDs3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 2, 2, 4)
)
rpcAtmDs3Group.setObjects(
      *(("RBN-PORT-COUNTERS-MIB", "rpcAtmDs3PlcpFebeErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmDs3PlcpBipErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmDs3PlcpFrameErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmDs3PlcpLofErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmDs3PlcpOofErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmDs3PlcpLof23Errs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmDs3PlcpYellowErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmDs3OofErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmDs3AisErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmDs3IdleCodes"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmDs3XbitYellowErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmDs3LosErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmDs3LCVs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmDs3FrameErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmDs3ParityErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmDs3PathParityErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmDs3FebeEvents"))
)
if mibBuilder.loadTexts:
    rpcAtmDs3Group.setStatus("current")

rpcAtmE3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 2, 2, 5)
)
rpcAtmE3Group.setObjects(
      *(("RBN-PORT-COUNTERS-MIB", "rpcAtmE3Los"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3LCV"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3LocalAlarmOn"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3RemoteAlarmOn"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3LinkUp"))
)
if mibBuilder.loadTexts:
    rpcAtmE3Group.setStatus("current")

rpcAtmE3G751Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 2, 2, 6)
)
rpcAtmE3G751Group.setObjects(
      *(("RBN-PORT-COUNTERS-MIB", "rpcAtmE3PlcpFebe"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3PlcpBip"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3PlcpFrmErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3PlcpLof"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3PlcpOof"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3PlcpLof23"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3PlcpYellow"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3Ais"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3Oof"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3AbitYel"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3FebeAllOnes"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3FAS"))
)
if mibBuilder.loadTexts:
    rpcAtmE3G751Group.setStatus("current")

rpcAtmE3G832Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 2, 2, 7)
)
rpcAtmE3G832Group.setObjects(
      *(("RBN-PORT-COUNTERS-MIB", "rpcAtmE3MaFebe"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3EmBip"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3MaFerf"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3E3E4Lof"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3E3E4Oof"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3E3E4Lof23"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3E3E4Ais"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3Loc"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmE3PayloadMismatch"))
)
if mibBuilder.loadTexts:
    rpcAtmE3G832Group.setStatus("current")

rpcAtmOc12Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 2, 2, 8)
)
rpcAtmOc12Group.setObjects(
      *(("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12ParityErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12FifoUndrErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12B1Errs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12B2Errs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12M1Errs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12S1Errs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12J1OofErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12G1Errs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12B3Errs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12FifoOvflErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12K1Byte"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12K2Byte"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12S1Byte"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12C2Byte"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12G1Byte"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12J0Bytes"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12J1Bytes"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12TxHecErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12RxDiscardErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12SectionStatus"),
        ("RBN-PORT-COUNTERS-MIB", "rpcAtmOc12PortStatus"))
)
if mibBuilder.loadTexts:
    rpcAtmOc12Group.setStatus("current")

rpcEthernetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 2, 2, 9)
)
rpcEthernetGroup.setObjects(
      *(("RBN-PORT-COUNTERS-MIB", "rpcEthernetJabber"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetUnderflow"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetLostCarrier"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetNoCarrier"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetLateCollision"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetExcessiveCollision"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetLinkFailure"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetDeferred"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetOkWithCollision"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetReclaimed"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetDescripErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetOversizedFrames"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetCollisions"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetWatchdog"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetMiiErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetCrcErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetDribble"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetOverflow"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetRuntFrames"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetBusParityErrs"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetBusMasterAborts"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetBusTargetAborts"),
        ("RBN-PORT-COUNTERS-MIB", "rpcEthernetBusUnknownErrs"))
)
if mibBuilder.loadTexts:
    rpcEthernetGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rpcMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 25, 2, 1, 1)
)
rpcMibCompliance.setObjects(
    ("RBN-PORT-COUNTERS-MIB", "rpcGenCountersGroup")
)
if mibBuilder.loadTexts:
    rpcMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-PORT-COUNTERS-MIB",
    **{"rpcMib": rpcMib,
       "rpcMibNotifications": rpcMibNotifications,
       "rpcMibObjects": rpcMibObjects,
       "rpc": rpc,
       "rpcGeneralTable": rpcGeneralTable,
       "rpcGeneralEntry": rpcGeneralEntry,
       "rpcSlotID": rpcSlotID,
       "rpcPortID": rpcPortID,
       "rpcGeneralPktsSent": rpcGeneralPktsSent,
       "rpcGeneralPktsRcvd": rpcGeneralPktsRcvd,
       "rpcGeneralBytesSent": rpcGeneralBytesSent,
       "rpcGeneralBytesRcvd": rpcGeneralBytesRcvd,
       "rpcGeneralMcastPktsSent": rpcGeneralMcastPktsSent,
       "rpcGeneralMcastPktsRcvd": rpcGeneralMcastPktsRcvd,
       "rpcGeneralMcastBytesSent": rpcGeneralMcastBytesSent,
       "rpcGeneralMcastBytesRcvd": rpcGeneralMcastBytesRcvd,
       "rpcGeneralXmtPktsDropped": rpcGeneralXmtPktsDropped,
       "rpcGeneralRcvPktsDropped": rpcGeneralRcvPktsDropped,
       "rpcGeneralXmtPktsOutstanding": rpcGeneralXmtPktsOutstanding,
       "rpcGeneralIOBuffers": rpcGeneralIOBuffers,
       "rpcGeneralPktXmtRate": rpcGeneralPktXmtRate,
       "rpcGeneralPktRcvRate": rpcGeneralPktRcvRate,
       "rpcGeneralPortRateLimitDrops": rpcGeneralPortRateLimitDrops,
       "rpcGeneralPortPoliceDrops": rpcGeneralPortPoliceDrops,
       "rpcGeneralCctRateLimitDrops": rpcGeneralCctRateLimitDrops,
       "rpcGeneralCctPoliceDrops": rpcGeneralCctPoliceDrops,
       "rpcGeneralFwdMemUsed": rpcGeneralFwdMemUsed,
       "rpcGeneralFloodQFailures": rpcGeneralFloodQFailures,
       "rpcAtmTable": rpcAtmTable,
       "rpcAtmEntry": rpcAtmEntry,
       "rpcAtmSegOutCells": rpcAtmSegOutCells,
       "rpcAtmRsmInCells": rpcAtmRsmInCells,
       "rpcAtmRsmInDrops": rpcAtmRsmInDrops,
       "rpcAtmRsmLengthErrs": rpcAtmRsmLengthErrs,
       "rpcAtmRsmPadErrs": rpcAtmRsmPadErrs,
       "rpcAtmRsmCpiErrs": rpcAtmRsmCpiErrs,
       "rpcAtmRsmCrcErrs": rpcAtmRsmCrcErrs,
       "rpcAtmRsmTimeoutErrs": rpcAtmRsmTimeoutErrs,
       "rpcAtmHostPciBusErrs": rpcAtmHostPciBusErrs,
       "rpcAtmHostDmaAfullErrs": rpcAtmHostDmaAfullErrs,
       "rpcAtmHostFrParityErrs": rpcAtmHostFrParityErrs,
       "rpcAtmHostFrSyncErrs": rpcAtmHostFrSyncErrs,
       "rpcAtmXmtResetCnt": rpcAtmXmtResetCnt,
       "rpcAtmRcvResetCnt": rpcAtmRcvResetCnt,
       "rpcAtmSegStatusqOvflErrs": rpcAtmSegStatusqOvflErrs,
       "rpcAtmSegNullSbdInfoErrs": rpcAtmSegNullSbdInfoErrs,
       "rpcAtmSegGetSbdInfoErrs": rpcAtmSegGetSbdInfoErrs,
       "rpcAtmSegUndfErrs": rpcAtmSegUndfErrs,
       "rpcAtmSegHostStatusFull": rpcAtmSegHostStatusFull,
       "rpcAtmRsmStatusqOvflErrs": rpcAtmRsmStatusqOvflErrs,
       "rpcAtmRsmBaErrs": rpcAtmRsmBaErrs,
       "rpcAtmRsmLenErrs": rpcAtmRsmLenErrs,
       "rpcAtmRsmFfpdErrs": rpcAtmRsmFfpdErrs,
       "rpcAtmRsmEpdErrs": rpcAtmRsmEpdErrs,
       "rpcAtmRsmUndfErrs": rpcAtmRsmUndfErrs,
       "rpcAtmRsmOvflErrs": rpcAtmRsmOvflErrs,
       "rpcAtmRsmSfpdErrs": rpcAtmRsmSfpdErrs,
       "rpcAtmRsmAbortErrs": rpcAtmRsmAbortErrs,
       "rpcAtmOnDemandAttempts": rpcAtmOnDemandAttempts,
       "rpcAtmOnDemandErrs": rpcAtmOnDemandErrs,
       "rpcAtmOamOutCells": rpcAtmOamOutCells,
       "rpcAtmOamInCells": rpcAtmOamInCells,
       "rpcAtmOamInF4Segments": rpcAtmOamInF4Segments,
       "rpcAtmOamInF4EndToEnds": rpcAtmOamInF4EndToEnds,
       "rpcAtmOamInF5Segments": rpcAtmOamInF5Segments,
       "rpcAtmOamInF5EndToEnds": rpcAtmOamInF5EndToEnds,
       "rpcAtmOamInPti6s": rpcAtmOamInPti6s,
       "rpcAtmOamInPti7s": rpcAtmOamInPti7s,
       "rpcAtmOamOutLoopbacks": rpcAtmOamOutLoopbacks,
       "rpcAtmOamInLoopbacks": rpcAtmOamInLoopbacks,
       "rpcAtmOamOutLoopbackResponses": rpcAtmOamOutLoopbackResponses,
       "rpcAtmOamInLoopbackResponses": rpcAtmOamInLoopbackResponses,
       "rpcAtmOamOutAises": rpcAtmOamOutAises,
       "rpcAtmOamInAises": rpcAtmOamInAises,
       "rpcAtmOamOutRdis": rpcAtmOamOutRdis,
       "rpcAtmOamInRdis": rpcAtmOamInRdis,
       "rpcAtmOamLineStatus": rpcAtmOamLineStatus,
       "rpcAtmOc3Table": rpcAtmOc3Table,
       "rpcAtmOc3Entry": rpcAtmOc3Entry,
       "rpcAtmOc3LineFebeErrs": rpcAtmOc3LineFebeErrs,
       "rpcAtmOc3LineFerfErrs": rpcAtmOc3LineFerfErrs,
       "rpcAtmOc3LineAisErrs": rpcAtmOc3LineAisErrs,
       "rpcAtmOc3PathFebeErrs": rpcAtmOc3PathFebeErrs,
       "rpcAtmOc3PathFerfErrs": rpcAtmOc3PathFerfErrs,
       "rpcAtmOc3PathAisErrs": rpcAtmOc3PathAisErrs,
       "rpcAtmOc3PathYellowErrs": rpcAtmOc3PathYellowErrs,
       "rpcAtmOc3StsLof23Errs": rpcAtmOc3StsLof23Errs,
       "rpcAtmOc3StsLofErrs": rpcAtmOc3StsLofErrs,
       "rpcAtmOc3StsOofErrs": rpcAtmOc3StsOofErrs,
       "rpcAtmOc3StsLopErrs": rpcAtmOc3StsLopErrs,
       "rpcAtmOc3BipErrs": rpcAtmOc3BipErrs,
       "rpcAtmOc3B1Bip8": rpcAtmOc3B1Bip8,
       "rpcAtmOc3B2Bip824": rpcAtmOc3B2Bip824,
       "rpcAtmOc3B3Bip8": rpcAtmOc3B3Bip8,
       "rpcAtmOc3LocErrs": rpcAtmOc3LocErrs,
       "rpcAtmOc3LosErrs": rpcAtmOc3LosErrs,
       "rpcAtmOc3Plm": rpcAtmOc3Plm,
       "rpcAtmOc3SectionStatus": rpcAtmOc3SectionStatus,
       "rpcAtmOc3PathStatus": rpcAtmOc3PathStatus,
       "rpcAtmDs3Table": rpcAtmDs3Table,
       "rpcAtmDs3Entry": rpcAtmDs3Entry,
       "rpcAtmDs3PlcpFebeErrs": rpcAtmDs3PlcpFebeErrs,
       "rpcAtmDs3PlcpBipErrs": rpcAtmDs3PlcpBipErrs,
       "rpcAtmDs3PlcpFrameErrs": rpcAtmDs3PlcpFrameErrs,
       "rpcAtmDs3PlcpLofErrs": rpcAtmDs3PlcpLofErrs,
       "rpcAtmDs3PlcpOofErrs": rpcAtmDs3PlcpOofErrs,
       "rpcAtmDs3PlcpLof23Errs": rpcAtmDs3PlcpLof23Errs,
       "rpcAtmDs3PlcpYellowErrs": rpcAtmDs3PlcpYellowErrs,
       "rpcAtmDs3OofErrs": rpcAtmDs3OofErrs,
       "rpcAtmDs3AisErrs": rpcAtmDs3AisErrs,
       "rpcAtmDs3IdleCodes": rpcAtmDs3IdleCodes,
       "rpcAtmDs3XbitYellowErrs": rpcAtmDs3XbitYellowErrs,
       "rpcAtmDs3LosErrs": rpcAtmDs3LosErrs,
       "rpcAtmDs3LCVs": rpcAtmDs3LCVs,
       "rpcAtmDs3FrameErrs": rpcAtmDs3FrameErrs,
       "rpcAtmDs3ParityErrs": rpcAtmDs3ParityErrs,
       "rpcAtmDs3PathParityErrs": rpcAtmDs3PathParityErrs,
       "rpcAtmDs3FebeEvents": rpcAtmDs3FebeEvents,
       "rpcAtmE3Table": rpcAtmE3Table,
       "rpcAtmE3Entry": rpcAtmE3Entry,
       "rpcAtmE3MaFebe": rpcAtmE3MaFebe,
       "rpcAtmE3EmBip": rpcAtmE3EmBip,
       "rpcAtmE3MaFerf": rpcAtmE3MaFerf,
       "rpcAtmE3E3E4Lof": rpcAtmE3E3E4Lof,
       "rpcAtmE3E3E4Oof": rpcAtmE3E3E4Oof,
       "rpcAtmE3E3E4Lof23": rpcAtmE3E3E4Lof23,
       "rpcAtmE3E3E4Ais": rpcAtmE3E3E4Ais,
       "rpcAtmE3Loc": rpcAtmE3Loc,
       "rpcAtmE3PayloadMismatch": rpcAtmE3PayloadMismatch,
       "rpcAtmE3PlcpFebe": rpcAtmE3PlcpFebe,
       "rpcAtmE3PlcpBip": rpcAtmE3PlcpBip,
       "rpcAtmE3PlcpFrmErrs": rpcAtmE3PlcpFrmErrs,
       "rpcAtmE3PlcpLof": rpcAtmE3PlcpLof,
       "rpcAtmE3PlcpOof": rpcAtmE3PlcpOof,
       "rpcAtmE3PlcpLof23": rpcAtmE3PlcpLof23,
       "rpcAtmE3PlcpYellow": rpcAtmE3PlcpYellow,
       "rpcAtmE3Ais": rpcAtmE3Ais,
       "rpcAtmE3Oof": rpcAtmE3Oof,
       "rpcAtmE3AbitYel": rpcAtmE3AbitYel,
       "rpcAtmE3FebeAllOnes": rpcAtmE3FebeAllOnes,
       "rpcAtmE3FAS": rpcAtmE3FAS,
       "rpcAtmE3Los": rpcAtmE3Los,
       "rpcAtmE3LCV": rpcAtmE3LCV,
       "rpcAtmE3LocalAlarmOn": rpcAtmE3LocalAlarmOn,
       "rpcAtmE3RemoteAlarmOn": rpcAtmE3RemoteAlarmOn,
       "rpcAtmE3LinkUp": rpcAtmE3LinkUp,
       "rpcAtmOc12Table": rpcAtmOc12Table,
       "rpcAtmOc12Entry": rpcAtmOc12Entry,
       "rpcAtmOc12ParityErrs": rpcAtmOc12ParityErrs,
       "rpcAtmOc12FifoUndrErrs": rpcAtmOc12FifoUndrErrs,
       "rpcAtmOc12B1Errs": rpcAtmOc12B1Errs,
       "rpcAtmOc12B2Errs": rpcAtmOc12B2Errs,
       "rpcAtmOc12M1Errs": rpcAtmOc12M1Errs,
       "rpcAtmOc12S1Errs": rpcAtmOc12S1Errs,
       "rpcAtmOc12J1OofErrs": rpcAtmOc12J1OofErrs,
       "rpcAtmOc12G1Errs": rpcAtmOc12G1Errs,
       "rpcAtmOc12B3Errs": rpcAtmOc12B3Errs,
       "rpcAtmOc12FifoOvflErrs": rpcAtmOc12FifoOvflErrs,
       "rpcAtmOc12K1Byte": rpcAtmOc12K1Byte,
       "rpcAtmOc12K2Byte": rpcAtmOc12K2Byte,
       "rpcAtmOc12S1Byte": rpcAtmOc12S1Byte,
       "rpcAtmOc12C2Byte": rpcAtmOc12C2Byte,
       "rpcAtmOc12G1Byte": rpcAtmOc12G1Byte,
       "rpcAtmOc12J0Bytes": rpcAtmOc12J0Bytes,
       "rpcAtmOc12J1Bytes": rpcAtmOc12J1Bytes,
       "rpcAtmOc12TxHecErrs": rpcAtmOc12TxHecErrs,
       "rpcAtmOc12RxDiscardErrs": rpcAtmOc12RxDiscardErrs,
       "rpcAtmOc12SectionStatus": rpcAtmOc12SectionStatus,
       "rpcAtmOc12PortStatus": rpcAtmOc12PortStatus,
       "rpcEthernetTable": rpcEthernetTable,
       "rpcEthernetEntry": rpcEthernetEntry,
       "rpcEthernetJabber": rpcEthernetJabber,
       "rpcEthernetUnderflow": rpcEthernetUnderflow,
       "rpcEthernetLostCarrier": rpcEthernetLostCarrier,
       "rpcEthernetNoCarrier": rpcEthernetNoCarrier,
       "rpcEthernetLateCollision": rpcEthernetLateCollision,
       "rpcEthernetExcessiveCollision": rpcEthernetExcessiveCollision,
       "rpcEthernetLinkFailure": rpcEthernetLinkFailure,
       "rpcEthernetDeferred": rpcEthernetDeferred,
       "rpcEthernetOkWithCollision": rpcEthernetOkWithCollision,
       "rpcEthernetReclaimed": rpcEthernetReclaimed,
       "rpcEthernetDescripErrs": rpcEthernetDescripErrs,
       "rpcEthernetOversizedFrames": rpcEthernetOversizedFrames,
       "rpcEthernetCollisions": rpcEthernetCollisions,
       "rpcEthernetWatchdog": rpcEthernetWatchdog,
       "rpcEthernetMiiErrs": rpcEthernetMiiErrs,
       "rpcEthernetCrcErrs": rpcEthernetCrcErrs,
       "rpcEthernetDribble": rpcEthernetDribble,
       "rpcEthernetOverflow": rpcEthernetOverflow,
       "rpcEthernetRuntFrames": rpcEthernetRuntFrames,
       "rpcEthernetBusParityErrs": rpcEthernetBusParityErrs,
       "rpcEthernetBusMasterAborts": rpcEthernetBusMasterAborts,
       "rpcEthernetBusTargetAborts": rpcEthernetBusTargetAborts,
       "rpcEthernetBusUnknownErrs": rpcEthernetBusUnknownErrs,
       "rpcMibConformance": rpcMibConformance,
       "rpcMibCompliances": rpcMibCompliances,
       "rpcMibCompliance": rpcMibCompliance,
       "rpcMibGroups": rpcMibGroups,
       "rpcGenCountersGroup": rpcGenCountersGroup,
       "rpcAtmGroup": rpcAtmGroup,
       "rpcAtmOc3Group": rpcAtmOc3Group,
       "rpcAtmDs3Group": rpcAtmDs3Group,
       "rpcAtmE3Group": rpcAtmE3Group,
       "rpcAtmE3G751Group": rpcAtmE3G751Group,
       "rpcAtmE3G832Group": rpcAtmE3G832Group,
       "rpcAtmOc12Group": rpcAtmOc12Group,
       "rpcEthernetGroup": rpcEthernetGroup}
)
