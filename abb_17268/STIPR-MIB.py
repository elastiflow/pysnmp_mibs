# SNMP MIB module (STIPR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/abb_17268/STIPR-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:23:57 2025
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

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Abb_ObjectIdentity = ObjectIdentity
abb = _Abb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268)
)
_Stipr_ObjectIdentity = ObjectIdentity
stipr = _Stipr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2)
)
_Stinet1_TxStl_Type = Counter32
_Stinet1_TxStl_Object = MibScalar
stinet1_TxStl = _Stinet1_TxStl_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 1),
    _Stinet1_TxStl_Type()
)
stinet1_TxStl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet1_TxStl.setStatus("mandatory")
_Stinet1_TxSeq_Type = Counter32
_Stinet1_TxSeq_Object = MibScalar
stinet1_TxSeq = _Stinet1_TxSeq_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 2),
    _Stinet1_TxSeq_Type()
)
stinet1_TxSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet1_TxSeq.setStatus("mandatory")
_Stinet1_TxStiSup_Type = Counter32
_Stinet1_TxStiSup_Object = MibScalar
stinet1_TxStiSup = _Stinet1_TxStiSup_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 3),
    _Stinet1_TxStiSup_Type()
)
stinet1_TxStiSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet1_TxStiSup.setStatus("mandatory")
_Stinet1_RxStl_Type = Counter32
_Stinet1_RxStl_Object = MibScalar
stinet1_RxStl = _Stinet1_RxStl_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 4),
    _Stinet1_RxStl_Type()
)
stinet1_RxStl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet1_RxStl.setStatus("mandatory")
_Stinet1_RxSeq_Type = Counter32
_Stinet1_RxSeq_Object = MibScalar
stinet1_RxSeq = _Stinet1_RxSeq_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 5),
    _Stinet1_RxSeq_Type()
)
stinet1_RxSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet1_RxSeq.setStatus("mandatory")
_Stinet1_RxStiSup_Type = Counter32
_Stinet1_RxStiSup_Object = MibScalar
stinet1_RxStiSup = _Stinet1_RxStiSup_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 6),
    _Stinet1_RxStiSup_Type()
)
stinet1_RxStiSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet1_RxStiSup.setStatus("mandatory")
_Stinet1_RxIllType_Type = Counter32
_Stinet1_RxIllType_Object = MibScalar
stinet1_RxIllType = _Stinet1_RxIllType_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 7),
    _Stinet1_RxIllType_Type()
)
stinet1_RxIllType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet1_RxIllType.setStatus("mandatory")
_Stinet1_RxIllStiprId_Type = Counter32
_Stinet1_RxIllStiprId_Object = MibScalar
stinet1_RxIllStiprId = _Stinet1_RxIllStiprId_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 8),
    _Stinet1_RxIllStiprId_Type()
)
stinet1_RxIllStiprId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet1_RxIllStiprId.setStatus("mandatory")
_Stinet1_RxIllLen_Type = Counter32
_Stinet1_RxIllLen_Object = MibScalar
stinet1_RxIllLen = _Stinet1_RxIllLen_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 9),
    _Stinet1_RxIllLen_Type()
)
stinet1_RxIllLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet1_RxIllLen.setStatus("mandatory")
_Stinet1_RxSeqOutOfSeq_Type = Counter32
_Stinet1_RxSeqOutOfSeq_Object = MibScalar
stinet1_RxSeqOutOfSeq = _Stinet1_RxSeqOutOfSeq_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 10),
    _Stinet1_RxSeqOutOfSeq_Type()
)
stinet1_RxSeqOutOfSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet1_RxSeqOutOfSeq.setStatus("mandatory")
_Stinet1_RxSeqDuplicate_Type = Counter32
_Stinet1_RxSeqDuplicate_Object = MibScalar
stinet1_RxSeqDuplicate = _Stinet1_RxSeqDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 11),
    _Stinet1_RxSeqDuplicate_Type()
)
stinet1_RxSeqDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet1_RxSeqDuplicate.setStatus("mandatory")
_Stinet1_RxSeqNotInit_Type = Counter32
_Stinet1_RxSeqNotInit_Object = MibScalar
stinet1_RxSeqNotInit = _Stinet1_RxSeqNotInit_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 12),
    _Stinet1_RxSeqNotInit_Type()
)
stinet1_RxSeqNotInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet1_RxSeqNotInit.setStatus("mandatory")
_Stinet1_SocketActive_Type = Integer32
_Stinet1_SocketActive_Object = MibScalar
stinet1_SocketActive = _Stinet1_SocketActive_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 13),
    _Stinet1_SocketActive_Type()
)
stinet1_SocketActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet1_SocketActive.setStatus("mandatory")
_Stinet1_SockChgState_Type = Counter32
_Stinet1_SockChgState_Object = MibScalar
stinet1_SockChgState = _Stinet1_SockChgState_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 14),
    _Stinet1_SockChgState_Type()
)
stinet1_SockChgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet1_SockChgState.setStatus("mandatory")
_Stinet1_IllStiprId_Type = Integer32
_Stinet1_IllStiprId_Object = MibScalar
stinet1_IllStiprId = _Stinet1_IllStiprId_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 15),
    _Stinet1_IllStiprId_Type()
)
stinet1_IllStiprId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet1_IllStiprId.setStatus("mandatory")
_Stinet1_RxIllStiprIdTime_Type = DisplayString
_Stinet1_RxIllStiprIdTime_Object = MibScalar
stinet1_RxIllStiprIdTime = _Stinet1_RxIllStiprIdTime_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 16),
    _Stinet1_RxIllStiprIdTime_Type()
)
stinet1_RxIllStiprIdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet1_RxIllStiprIdTime.setStatus("mandatory")


class _Stinet1_ResetStat_Type(Integer32):
    """Custom type stinet1_ResetStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("true", -1),
          ("false", 0))
    )


_Stinet1_ResetStat_Type.__name__ = "Integer32"
_Stinet1_ResetStat_Object = MibScalar
stinet1_ResetStat = _Stinet1_ResetStat_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 17),
    _Stinet1_ResetStat_Type()
)
stinet1_ResetStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stinet1_ResetStat.setStatus("mandatory")
_Stinet2_TxStl_Type = Counter32
_Stinet2_TxStl_Object = MibScalar
stinet2_TxStl = _Stinet2_TxStl_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 18),
    _Stinet2_TxStl_Type()
)
stinet2_TxStl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet2_TxStl.setStatus("mandatory")
_Stinet2_TxSeq_Type = Counter32
_Stinet2_TxSeq_Object = MibScalar
stinet2_TxSeq = _Stinet2_TxSeq_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 19),
    _Stinet2_TxSeq_Type()
)
stinet2_TxSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet2_TxSeq.setStatus("mandatory")
_Stinet2_TxStiSup_Type = Counter32
_Stinet2_TxStiSup_Object = MibScalar
stinet2_TxStiSup = _Stinet2_TxStiSup_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 20),
    _Stinet2_TxStiSup_Type()
)
stinet2_TxStiSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet2_TxStiSup.setStatus("mandatory")
_Stinet2_RxStl_Type = Counter32
_Stinet2_RxStl_Object = MibScalar
stinet2_RxStl = _Stinet2_RxStl_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 21),
    _Stinet2_RxStl_Type()
)
stinet2_RxStl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet2_RxStl.setStatus("mandatory")
_Stinet2_RxSeq_Type = Counter32
_Stinet2_RxSeq_Object = MibScalar
stinet2_RxSeq = _Stinet2_RxSeq_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 22),
    _Stinet2_RxSeq_Type()
)
stinet2_RxSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet2_RxSeq.setStatus("mandatory")
_Stinet2_RxStiSup_Type = Counter32
_Stinet2_RxStiSup_Object = MibScalar
stinet2_RxStiSup = _Stinet2_RxStiSup_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 23),
    _Stinet2_RxStiSup_Type()
)
stinet2_RxStiSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet2_RxStiSup.setStatus("mandatory")
_Stinet2_RxIllType_Type = Counter32
_Stinet2_RxIllType_Object = MibScalar
stinet2_RxIllType = _Stinet2_RxIllType_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 24),
    _Stinet2_RxIllType_Type()
)
stinet2_RxIllType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet2_RxIllType.setStatus("mandatory")
_Stinet2_RxIllStiprId_Type = Counter32
_Stinet2_RxIllStiprId_Object = MibScalar
stinet2_RxIllStiprId = _Stinet2_RxIllStiprId_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 25),
    _Stinet2_RxIllStiprId_Type()
)
stinet2_RxIllStiprId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet2_RxIllStiprId.setStatus("mandatory")
_Stinet2_RxIllLen_Type = Counter32
_Stinet2_RxIllLen_Object = MibScalar
stinet2_RxIllLen = _Stinet2_RxIllLen_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 26),
    _Stinet2_RxIllLen_Type()
)
stinet2_RxIllLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet2_RxIllLen.setStatus("mandatory")
_Stinet2_RxSeqOutOfSeq_Type = Counter32
_Stinet2_RxSeqOutOfSeq_Object = MibScalar
stinet2_RxSeqOutOfSeq = _Stinet2_RxSeqOutOfSeq_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 27),
    _Stinet2_RxSeqOutOfSeq_Type()
)
stinet2_RxSeqOutOfSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet2_RxSeqOutOfSeq.setStatus("mandatory")
_Stinet2_RxSeqDuplicate_Type = Counter32
_Stinet2_RxSeqDuplicate_Object = MibScalar
stinet2_RxSeqDuplicate = _Stinet2_RxSeqDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 28),
    _Stinet2_RxSeqDuplicate_Type()
)
stinet2_RxSeqDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet2_RxSeqDuplicate.setStatus("mandatory")
_Stinet2_RxSeqNotInit_Type = Counter32
_Stinet2_RxSeqNotInit_Object = MibScalar
stinet2_RxSeqNotInit = _Stinet2_RxSeqNotInit_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 29),
    _Stinet2_RxSeqNotInit_Type()
)
stinet2_RxSeqNotInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet2_RxSeqNotInit.setStatus("mandatory")
_Stinet2_SocketActive_Type = Integer32
_Stinet2_SocketActive_Object = MibScalar
stinet2_SocketActive = _Stinet2_SocketActive_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 30),
    _Stinet2_SocketActive_Type()
)
stinet2_SocketActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet2_SocketActive.setStatus("mandatory")
_Stinet2_SockChgState_Type = Counter32
_Stinet2_SockChgState_Object = MibScalar
stinet2_SockChgState = _Stinet2_SockChgState_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 31),
    _Stinet2_SockChgState_Type()
)
stinet2_SockChgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet2_SockChgState.setStatus("mandatory")
_Stinet2_IllStiprId_Type = Integer32
_Stinet2_IllStiprId_Object = MibScalar
stinet2_IllStiprId = _Stinet2_IllStiprId_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 32),
    _Stinet2_IllStiprId_Type()
)
stinet2_IllStiprId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet2_IllStiprId.setStatus("mandatory")
_Stinet2_RxIllStiprIdTime_Type = DisplayString
_Stinet2_RxIllStiprIdTime_Object = MibScalar
stinet2_RxIllStiprIdTime = _Stinet2_RxIllStiprIdTime_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 33),
    _Stinet2_RxIllStiprIdTime_Type()
)
stinet2_RxIllStiprIdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet2_RxIllStiprIdTime.setStatus("mandatory")


class _Stinet2_ResetStat_Type(Integer32):
    """Custom type stinet2_ResetStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("true", -1),
          ("false", 0))
    )


_Stinet2_ResetStat_Type.__name__ = "Integer32"
_Stinet2_ResetStat_Object = MibScalar
stinet2_ResetStat = _Stinet2_ResetStat_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 34),
    _Stinet2_ResetStat_Type()
)
stinet2_ResetStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stinet2_ResetStat.setStatus("mandatory")
_Stl_SccIntCnt_Type = Counter32
_Stl_SccIntCnt_Object = MibScalar
stl_SccIntCnt = _Stl_SccIntCnt_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 35),
    _Stl_SccIntCnt_Type()
)
stl_SccIntCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_SccIntCnt.setStatus("mandatory")
_Stl_TxGiveupErrors_Type = Counter32
_Stl_TxGiveupErrors_Object = MibScalar
stl_TxGiveupErrors = _Stl_TxGiveupErrors_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 36),
    _Stl_TxGiveupErrors_Type()
)
stl_TxGiveupErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_TxGiveupErrors.setStatus("mandatory")
_Stl_TxCalled_Type = Counter32
_Stl_TxCalled_Object = MibScalar
stl_TxCalled = _Stl_TxCalled_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 37),
    _Stl_TxCalled_Type()
)
stl_TxCalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_TxCalled.setStatus("mandatory")
_Stl_TxOkTotal_Type = Counter32
_Stl_TxOkTotal_Object = MibScalar
stl_TxOkTotal = _Stl_TxOkTotal_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 38),
    _Stl_TxOkTotal_Type()
)
stl_TxOkTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_TxOkTotal.setStatus("mandatory")
_Stl_TxMaxAttempt_Type = Counter32
_Stl_TxMaxAttempt_Object = MibScalar
stl_TxMaxAttempt = _Stl_TxMaxAttempt_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 39),
    _Stl_TxMaxAttempt_Type()
)
stl_TxMaxAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_TxMaxAttempt.setStatus("mandatory")
_Stl_TxDmaAccessStops_Type = Counter32
_Stl_TxDmaAccessStops_Object = MibScalar
stl_TxDmaAccessStops = _Stl_TxDmaAccessStops_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 40),
    _Stl_TxDmaAccessStops_Type()
)
stl_TxDmaAccessStops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_TxDmaAccessStops.setStatus("mandatory")
_Stl_TxCollisions_Type = Counter32
_Stl_TxCollisions_Object = MibScalar
stl_TxCollisions = _Stl_TxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 41),
    _Stl_TxCollisions_Type()
)
stl_TxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_TxCollisions.setStatus("mandatory")
_Stl_TxCts0SetupIntsIgnored_Type = Counter32
_Stl_TxCts0SetupIntsIgnored_Object = MibScalar
stl_TxCts0SetupIntsIgnored = _Stl_TxCts0SetupIntsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 42),
    _Stl_TxCts0SetupIntsIgnored_Type()
)
stl_TxCts0SetupIntsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_TxCts0SetupIntsIgnored.setStatus("mandatory")
_Stl_TxCts1SetupAccInts_Type = Counter32
_Stl_TxCts1SetupAccInts_Object = MibScalar
stl_TxCts1SetupAccInts = _Stl_TxCts1SetupAccInts_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 43),
    _Stl_TxCts1SetupAccInts_Type()
)
stl_TxCts1SetupAccInts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_TxCts1SetupAccInts.setStatus("mandatory")
_Stl_TxCts1AccIntsIgnored_Type = Counter32
_Stl_TxCts1AccIntsIgnored_Object = MibScalar
stl_TxCts1AccIntsIgnored = _Stl_TxCts1AccIntsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 44),
    _Stl_TxCts1AccIntsIgnored_Type()
)
stl_TxCts1AccIntsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_TxCts1AccIntsIgnored.setStatus("mandatory")
_Stl_TxDmaFrameStops_Type = Counter32
_Stl_TxDmaFrameStops_Object = MibScalar
stl_TxDmaFrameStops = _Stl_TxDmaFrameStops_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 45),
    _Stl_TxDmaFrameStops_Type()
)
stl_TxDmaFrameStops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_TxDmaFrameStops.setStatus("mandatory")
_Stl_TxIllCollisionsStart_Type = Counter32
_Stl_TxIllCollisionsStart_Object = MibScalar
stl_TxIllCollisionsStart = _Stl_TxIllCollisionsStart_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 46),
    _Stl_TxIllCollisionsStart_Type()
)
stl_TxIllCollisionsStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_TxIllCollisionsStart.setStatus("mandatory")
_Stl_TxIllCollisions_Type = Counter32
_Stl_TxIllCollisions_Object = MibScalar
stl_TxIllCollisions = _Stl_TxIllCollisions_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 47),
    _Stl_TxIllCollisions_Type()
)
stl_TxIllCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_TxIllCollisions.setStatus("mandatory")
_Stl_TxCrcWaitMaxCnt_Type = Counter32
_Stl_TxCrcWaitMaxCnt_Object = MibScalar
stl_TxCrcWaitMaxCnt = _Stl_TxCrcWaitMaxCnt_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 48),
    _Stl_TxCrcWaitMaxCnt_Type()
)
stl_TxCrcWaitMaxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_TxCrcWaitMaxCnt.setStatus("mandatory")
_Stl_RxCalled_Type = Counter32
_Stl_RxCalled_Object = MibScalar
stl_RxCalled = _Stl_RxCalled_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 49),
    _Stl_RxCalled_Type()
)
stl_RxCalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_RxCalled.setStatus("mandatory")
_Stl_RxOkTotal_Type = Counter32
_Stl_RxOkTotal_Object = MibScalar
stl_RxOkTotal = _Stl_RxOkTotal_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 50),
    _Stl_RxOkTotal_Type()
)
stl_RxOkTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_RxOkTotal.setStatus("mandatory")
_Stl_RxFailure_Type = Counter32
_Stl_RxFailure_Object = MibScalar
stl_RxFailure = _Stl_RxFailure_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 51),
    _Stl_RxFailure_Type()
)
stl_RxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_RxFailure.setStatus("mandatory")
_Stl_RxCrcErrors_Type = Counter32
_Stl_RxCrcErrors_Object = MibScalar
stl_RxCrcErrors = _Stl_RxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 52),
    _Stl_RxCrcErrors_Type()
)
stl_RxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_RxCrcErrors.setStatus("mandatory")
_Stl_RxOverrunErrors_Type = Counter32
_Stl_RxOverrunErrors_Object = MibScalar
stl_RxOverrunErrors = _Stl_RxOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 53),
    _Stl_RxOverrunErrors_Type()
)
stl_RxOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_RxOverrunErrors.setStatus("mandatory")
_Stl_RxMinLenErrors_Type = Counter32
_Stl_RxMinLenErrors_Object = MibScalar
stl_RxMinLenErrors = _Stl_RxMinLenErrors_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 54),
    _Stl_RxMinLenErrors_Type()
)
stl_RxMinLenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_RxMinLenErrors.setStatus("mandatory")
_Stl_RxMaxLenErrors_Type = Counter32
_Stl_RxMaxLenErrors_Object = MibScalar
stl_RxMaxLenErrors = _Stl_RxMaxLenErrors_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 55),
    _Stl_RxMaxLenErrors_Type()
)
stl_RxMaxLenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_RxMaxLenErrors.setStatus("mandatory")
_Stl_RxStiQueueSize_Type = Counter32
_Stl_RxStiQueueSize_Object = MibScalar
stl_RxStiQueueSize = _Stl_RxStiQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 56),
    _Stl_RxStiQueueSize_Type()
)
stl_RxStiQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_RxStiQueueSize.setStatus("mandatory")
_Stl_RxStiQueueTimeouts_Type = Counter32
_Stl_RxStiQueueTimeouts_Object = MibScalar
stl_RxStiQueueTimeouts = _Stl_RxStiQueueTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 57),
    _Stl_RxStiQueueTimeouts_Type()
)
stl_RxStiQueueTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stl_RxStiQueueTimeouts.setStatus("mandatory")


class _Stl_ResetStat_Type(Integer32):
    """Custom type stl_ResetStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("true", -1),
          ("false", 0))
    )


_Stl_ResetStat_Type.__name__ = "Integer32"
_Stl_ResetStat_Object = MibScalar
stl_ResetStat = _Stl_ResetStat_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 58),
    _Stl_ResetStat_Type()
)
stl_ResetStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stl_ResetStat.setStatus("mandatory")
_Route_RxStlGpe_Type = Counter32
_Route_RxStlGpe_Object = MibScalar
route_RxStlGpe = _Route_RxStlGpe_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 59),
    _Route_RxStlGpe_Type()
)
route_RxStlGpe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    route_RxStlGpe.setStatus("mandatory")
_Route_RxStlLpe_Type = Counter32
_Route_RxStlLpe_Object = MibScalar
route_RxStlLpe = _Route_RxStlLpe_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 60),
    _Route_RxStlLpe_Type()
)
route_RxStlLpe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    route_RxStlLpe.setStatus("mandatory")
_Route_RxStlPeNotCfg_Type = Counter32
_Route_RxStlPeNotCfg_Object = MibScalar
route_RxStlPeNotCfg = _Route_RxStlPeNotCfg_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 61),
    _Route_RxStlPeNotCfg_Type()
)
route_RxStlPeNotCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    route_RxStlPeNotCfg.setStatus("mandatory")
_Route_RxStlPeIdNotCfg_Type = Integer32
_Route_RxStlPeIdNotCfg_Object = MibScalar
route_RxStlPeIdNotCfg = _Route_RxStlPeIdNotCfg_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 62),
    _Route_RxStlPeIdNotCfg_Type()
)
route_RxStlPeIdNotCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    route_RxStlPeIdNotCfg.setStatus("mandatory")
_Route_RxStlPeTimeNotCfg_Type = DisplayString
_Route_RxStlPeTimeNotCfg_Object = MibScalar
route_RxStlPeTimeNotCfg = _Route_RxStlPeTimeNotCfg_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 63),
    _Route_RxStlPeTimeNotCfg_Type()
)
route_RxStlPeTimeNotCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    route_RxStlPeTimeNotCfg.setStatus("mandatory")
_Route_RxStiGpe_Type = Counter32
_Route_RxStiGpe_Object = MibScalar
route_RxStiGpe = _Route_RxStiGpe_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 64),
    _Route_RxStiGpe_Type()
)
route_RxStiGpe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    route_RxStiGpe.setStatus("mandatory")
_Route_RxStiLpe_Type = Counter32
_Route_RxStiLpe_Object = MibScalar
route_RxStiLpe = _Route_RxStiLpe_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 65),
    _Route_RxStiLpe_Type()
)
route_RxStiLpe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    route_RxStiLpe.setStatus("mandatory")
_Route_RxStiPeNotCfg_Type = Counter32
_Route_RxStiPeNotCfg_Object = MibScalar
route_RxStiPeNotCfg = _Route_RxStiPeNotCfg_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 66),
    _Route_RxStiPeNotCfg_Type()
)
route_RxStiPeNotCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    route_RxStiPeNotCfg.setStatus("mandatory")
_Route_RxStiPeIdError_Type = Integer32
_Route_RxStiPeIdError_Object = MibScalar
route_RxStiPeIdError = _Route_RxStiPeIdError_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 67),
    _Route_RxStiPeIdError_Type()
)
route_RxStiPeIdError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    route_RxStiPeIdError.setStatus("mandatory")
_Route_RxStiStiprIdError_Type = Integer32
_Route_RxStiStiprIdError_Object = MibScalar
route_RxStiStiprIdError = _Route_RxStiStiprIdError_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 68),
    _Route_RxStiStiprIdError_Type()
)
route_RxStiStiprIdError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    route_RxStiStiprIdError.setStatus("mandatory")
_Route_RxStiPeTimeError_Type = DisplayString
_Route_RxStiPeTimeError_Object = MibScalar
route_RxStiPeTimeError = _Route_RxStiPeTimeError_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 69),
    _Route_RxStiPeTimeError_Type()
)
route_RxStiPeTimeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    route_RxStiPeTimeError.setStatus("mandatory")


class _Route_ResetStat_Type(Integer32):
    """Custom type route_ResetStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("true", -1),
          ("false", 0))
    )


_Route_ResetStat_Type.__name__ = "Integer32"
_Route_ResetStat_Object = MibScalar
route_ResetStat = _Route_ResetStat_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 70),
    _Route_ResetStat_Type()
)
route_ResetStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    route_ResetStat.setStatus("mandatory")
_Stinet_UdpErrors_Type = Counter32
_Stinet_UdpErrors_Object = MibScalar
stinet_UdpErrors = _Stinet_UdpErrors_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 71),
    _Stinet_UdpErrors_Type()
)
stinet_UdpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet_UdpErrors.setStatus("mandatory")
_Stinet_RxStlQueueSize_Type = Counter32
_Stinet_RxStlQueueSize_Object = MibScalar
stinet_RxStlQueueSize = _Stinet_RxStlQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 74),
    _Stinet_RxStlQueueSize_Type()
)
stinet_RxStlQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet_RxStlQueueSize.setStatus("mandatory")
_Stinet_RxStlQueueTimeouts_Type = DisplayString
_Stinet_RxStlQueueTimeouts_Object = MibScalar
stinet_RxStlQueueTimeouts = _Stinet_RxStlQueueTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 75),
    _Stinet_RxStlQueueTimeouts_Type()
)
stinet_RxStlQueueTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stinet_RxStlQueueTimeouts.setStatus("mandatory")


class _Stinet_ResetStat_Type(Integer32):
    """Custom type stinet_ResetStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("true", -1),
          ("false", 0))
    )


_Stinet_ResetStat_Type.__name__ = "Integer32"
_Stinet_ResetStat_Object = MibScalar
stinet_ResetStat = _Stinet_ResetStat_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 76),
    _Stinet_ResetStat_Type()
)
stinet_ResetStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stinet_ResetStat.setStatus("mandatory")
_Rts1_Connects_Type = Counter32
_Rts1_Connects_Object = MibScalar
rts1_Connects = _Rts1_Connects_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 77),
    _Rts1_Connects_Type()
)
rts1_Connects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rts1_Connects.setStatus("mandatory")
_Rts1_NoAnswer_Type = Counter32
_Rts1_NoAnswer_Object = MibScalar
rts1_NoAnswer = _Rts1_NoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 78),
    _Rts1_NoAnswer_Type()
)
rts1_NoAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rts1_NoAnswer.setStatus("mandatory")
_Rts1_NewTable_Type = Counter32
_Rts1_NewTable_Object = MibScalar
rts1_NewTable = _Rts1_NewTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 79),
    _Rts1_NewTable_Type()
)
rts1_NewTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rts1_NewTable.setStatus("mandatory")
_Rts1_LastConnectTime_Type = DisplayString
_Rts1_LastConnectTime_Object = MibScalar
rts1_LastConnectTime = _Rts1_LastConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 80),
    _Rts1_LastConnectTime_Type()
)
rts1_LastConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rts1_LastConnectTime.setStatus("mandatory")
_Rts1_TableTimestamp_Type = DisplayString
_Rts1_TableTimestamp_Object = MibScalar
rts1_TableTimestamp = _Rts1_TableTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 81),
    _Rts1_TableTimestamp_Type()
)
rts1_TableTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rts1_TableTimestamp.setStatus("mandatory")


class _Rts1_ResetStat_Type(Integer32):
    """Custom type rts1_ResetStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("true", -1),
          ("false", 0))
    )


_Rts1_ResetStat_Type.__name__ = "Integer32"
_Rts1_ResetStat_Object = MibScalar
rts1_ResetStat = _Rts1_ResetStat_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 82),
    _Rts1_ResetStat_Type()
)
rts1_ResetStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rts1_ResetStat.setStatus("mandatory")
_Rts2_Connects_Type = Counter32
_Rts2_Connects_Object = MibScalar
rts2_Connects = _Rts2_Connects_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 83),
    _Rts2_Connects_Type()
)
rts2_Connects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rts2_Connects.setStatus("mandatory")
_Rts2_NoAnswer_Type = Counter32
_Rts2_NoAnswer_Object = MibScalar
rts2_NoAnswer = _Rts2_NoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 84),
    _Rts2_NoAnswer_Type()
)
rts2_NoAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rts2_NoAnswer.setStatus("mandatory")
_Rts2_NewTable_Type = Counter32
_Rts2_NewTable_Object = MibScalar
rts2_NewTable = _Rts2_NewTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 85),
    _Rts2_NewTable_Type()
)
rts2_NewTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rts2_NewTable.setStatus("mandatory")
_Rts2_LastConnectTime_Type = DisplayString
_Rts2_LastConnectTime_Object = MibScalar
rts2_LastConnectTime = _Rts2_LastConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 86),
    _Rts2_LastConnectTime_Type()
)
rts2_LastConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rts2_LastConnectTime.setStatus("mandatory")
_Rts2_TableTimestamp_Type = DisplayString
_Rts2_TableTimestamp_Object = MibScalar
rts2_TableTimestamp = _Rts2_TableTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 87),
    _Rts2_TableTimestamp_Type()
)
rts2_TableTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rts2_TableTimestamp.setStatus("mandatory")


class _Rts2_ResetStat_Type(Integer32):
    """Custom type rts2_ResetStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("true", -1),
          ("false", 0))
    )


_Rts2_ResetStat_Type.__name__ = "Integer32"
_Rts2_ResetStat_Object = MibScalar
rts2_ResetStat = _Rts2_ResetStat_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 88),
    _Rts2_ResetStat_Type()
)
rts2_ResetStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rts2_ResetStat.setStatus("mandatory")


class _Gw_NktNetConnected_Type(Integer32):
    """Custom type gw_NktNetConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("true", -1),
          ("false", 0))
    )


_Gw_NktNetConnected_Type.__name__ = "Integer32"
_Gw_NktNetConnected_Object = MibScalar
gw_NktNetConnected = _Gw_NktNetConnected_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2, 89),
    _Gw_NktNetConnected_Type()
)
gw_NktNetConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw_NktNetConnected.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STIPR-MIB",
    **{"abb": abb,
       "stipr": stipr,
       "stinet1_TxStl": stinet1_TxStl,
       "stinet1_TxSeq": stinet1_TxSeq,
       "stinet1_TxStiSup": stinet1_TxStiSup,
       "stinet1_RxStl": stinet1_RxStl,
       "stinet1_RxSeq": stinet1_RxSeq,
       "stinet1_RxStiSup": stinet1_RxStiSup,
       "stinet1_RxIllType": stinet1_RxIllType,
       "stinet1_RxIllStiprId": stinet1_RxIllStiprId,
       "stinet1_RxIllLen": stinet1_RxIllLen,
       "stinet1_RxSeqOutOfSeq": stinet1_RxSeqOutOfSeq,
       "stinet1_RxSeqDuplicate": stinet1_RxSeqDuplicate,
       "stinet1_RxSeqNotInit": stinet1_RxSeqNotInit,
       "stinet1_SocketActive": stinet1_SocketActive,
       "stinet1_SockChgState": stinet1_SockChgState,
       "stinet1_IllStiprId": stinet1_IllStiprId,
       "stinet1_RxIllStiprIdTime": stinet1_RxIllStiprIdTime,
       "stinet1_ResetStat": stinet1_ResetStat,
       "stinet2_TxStl": stinet2_TxStl,
       "stinet2_TxSeq": stinet2_TxSeq,
       "stinet2_TxStiSup": stinet2_TxStiSup,
       "stinet2_RxStl": stinet2_RxStl,
       "stinet2_RxSeq": stinet2_RxSeq,
       "stinet2_RxStiSup": stinet2_RxStiSup,
       "stinet2_RxIllType": stinet2_RxIllType,
       "stinet2_RxIllStiprId": stinet2_RxIllStiprId,
       "stinet2_RxIllLen": stinet2_RxIllLen,
       "stinet2_RxSeqOutOfSeq": stinet2_RxSeqOutOfSeq,
       "stinet2_RxSeqDuplicate": stinet2_RxSeqDuplicate,
       "stinet2_RxSeqNotInit": stinet2_RxSeqNotInit,
       "stinet2_SocketActive": stinet2_SocketActive,
       "stinet2_SockChgState": stinet2_SockChgState,
       "stinet2_IllStiprId": stinet2_IllStiprId,
       "stinet2_RxIllStiprIdTime": stinet2_RxIllStiprIdTime,
       "stinet2_ResetStat": stinet2_ResetStat,
       "stl_SccIntCnt": stl_SccIntCnt,
       "stl_TxGiveupErrors": stl_TxGiveupErrors,
       "stl_TxCalled": stl_TxCalled,
       "stl_TxOkTotal": stl_TxOkTotal,
       "stl_TxMaxAttempt": stl_TxMaxAttempt,
       "stl_TxDmaAccessStops": stl_TxDmaAccessStops,
       "stl_TxCollisions": stl_TxCollisions,
       "stl_TxCts0SetupIntsIgnored": stl_TxCts0SetupIntsIgnored,
       "stl_TxCts1SetupAccInts": stl_TxCts1SetupAccInts,
       "stl_TxCts1AccIntsIgnored": stl_TxCts1AccIntsIgnored,
       "stl_TxDmaFrameStops": stl_TxDmaFrameStops,
       "stl_TxIllCollisionsStart": stl_TxIllCollisionsStart,
       "stl_TxIllCollisions": stl_TxIllCollisions,
       "stl_TxCrcWaitMaxCnt": stl_TxCrcWaitMaxCnt,
       "stl_RxCalled": stl_RxCalled,
       "stl_RxOkTotal": stl_RxOkTotal,
       "stl_RxFailure": stl_RxFailure,
       "stl_RxCrcErrors": stl_RxCrcErrors,
       "stl_RxOverrunErrors": stl_RxOverrunErrors,
       "stl_RxMinLenErrors": stl_RxMinLenErrors,
       "stl_RxMaxLenErrors": stl_RxMaxLenErrors,
       "stl_RxStiQueueSize": stl_RxStiQueueSize,
       "stl_RxStiQueueTimeouts": stl_RxStiQueueTimeouts,
       "stl_ResetStat": stl_ResetStat,
       "route_RxStlGpe": route_RxStlGpe,
       "route_RxStlLpe": route_RxStlLpe,
       "route_RxStlPeNotCfg": route_RxStlPeNotCfg,
       "route_RxStlPeIdNotCfg": route_RxStlPeIdNotCfg,
       "route_RxStlPeTimeNotCfg": route_RxStlPeTimeNotCfg,
       "route_RxStiGpe": route_RxStiGpe,
       "route_RxStiLpe": route_RxStiLpe,
       "route_RxStiPeNotCfg": route_RxStiPeNotCfg,
       "route_RxStiPeIdError": route_RxStiPeIdError,
       "route_RxStiStiprIdError": route_RxStiStiprIdError,
       "route_RxStiPeTimeError": route_RxStiPeTimeError,
       "route_ResetStat": route_ResetStat,
       "stinet_UdpErrors": stinet_UdpErrors,
       "stinet_RxStlQueueSize": stinet_RxStlQueueSize,
       "stinet_RxStlQueueTimeouts": stinet_RxStlQueueTimeouts,
       "stinet_ResetStat": stinet_ResetStat,
       "rts1_Connects": rts1_Connects,
       "rts1_NoAnswer": rts1_NoAnswer,
       "rts1_NewTable": rts1_NewTable,
       "rts1_LastConnectTime": rts1_LastConnectTime,
       "rts1_TableTimestamp": rts1_TableTimestamp,
       "rts1_ResetStat": rts1_ResetStat,
       "rts2_Connects": rts2_Connects,
       "rts2_NoAnswer": rts2_NoAnswer,
       "rts2_NewTable": rts2_NewTable,
       "rts2_LastConnectTime": rts2_LastConnectTime,
       "rts2_TableTimestamp": rts2_TableTimestamp,
       "rts2_ResetStat": rts2_ResetStat,
       "gw_NktNetConnected": gw_NktNetConnected}
)
