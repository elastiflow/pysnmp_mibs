# SNMP MIB module (TRILL-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/TRILL-OAM-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 15:41:48 2025
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

(Dot1agCfmEgressActionFieldValue,
 Dot1agCfmIngressActionFieldValue,
 Dot1agCfmRemoteMepState,
 dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepDbEntry,
 dot1agCfmMepEntry,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmEgressActionFieldValue",
    "Dot1agCfmIngressActionFieldValue",
    "Dot1agCfmRemoteMepState",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepDbEntry",
    "dot1agCfmMepEntry",
    "dot1agCfmMepIdentifier")

(LldpChassisId,
 LldpChassisIdSubtype,
 LldpPortId,
 LldpPortIdSubtype) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpChassisId",
    "LldpChassisIdSubtype",
    "LldpPortId",
    "LldpPortIdSubtype")

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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

trillOamMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 238)
)
if mibBuilder.loadTexts:
    trillOamMib.setRevisions(
        ("2016-01-14 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TrillOamNotifications_ObjectIdentity = ObjectIdentity
trillOamNotifications = _TrillOamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 238, 0)
)
_TrillOamMibObjects_ObjectIdentity = ObjectIdentity
trillOamMibObjects = _TrillOamMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 238, 1)
)
_TrillOamMep_ObjectIdentity = ObjectIdentity
trillOamMep = _TrillOamMep_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 238, 1, 1)
)
_TrillOamMepTable_Object = MibTable
trillOamMepTable = _TrillOamMepTable_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1)
)
if mibBuilder.loadTexts:
    trillOamMepTable.setStatus("current")
_TrillOamMepEntry_Object = MibTableRow
trillOamMepEntry = _TrillOamMepEntry_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    trillOamMepEntry.setStatus("current")


class _TrillOamMepRName_Type(Unsigned32):
    """Custom type trillOamMepRName based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65471),
    )


_TrillOamMepRName_Type.__name__ = "Unsigned32"
_TrillOamMepRName_Object = MibTableColumn
trillOamMepRName = _TrillOamMepRName_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 1),
    _TrillOamMepRName_Type()
)
trillOamMepRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepRName.setStatus("current")
_TrillOamMepNextPtmTId_Type = Counter32
_TrillOamMepNextPtmTId_Object = MibTableColumn
trillOamMepNextPtmTId = _TrillOamMepNextPtmTId_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 2),
    _TrillOamMepNextPtmTId_Type()
)
trillOamMepNextPtmTId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepNextPtmTId.setStatus("current")
_TrillOamMepNextMtvmTId_Type = Counter32
_TrillOamMepNextMtvmTId_Object = MibTableColumn
trillOamMepNextMtvmTId = _TrillOamMepNextMtvmTId_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 3),
    _TrillOamMepNextMtvmTId_Type()
)
trillOamMepNextMtvmTId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepNextMtvmTId.setStatus("current")
_TrillOamMepPtrIn_Type = Counter32
_TrillOamMepPtrIn_Object = MibTableColumn
trillOamMepPtrIn = _TrillOamMepPtrIn_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 4),
    _TrillOamMepPtrIn_Type()
)
trillOamMepPtrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrIn.setStatus("current")
_TrillOamMepPtrInOutofOrder_Type = Counter32
_TrillOamMepPtrInOutofOrder_Object = MibTableColumn
trillOamMepPtrInOutofOrder = _TrillOamMepPtrInOutofOrder_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 5),
    _TrillOamMepPtrInOutofOrder_Type()
)
trillOamMepPtrInOutofOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrInOutofOrder.setStatus("current")
_TrillOamMepPtrOut_Type = Counter32
_TrillOamMepPtrOut_Object = MibTableColumn
trillOamMepPtrOut = _TrillOamMepPtrOut_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 6),
    _TrillOamMepPtrOut_Type()
)
trillOamMepPtrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrOut.setStatus("current")
_TrillOamMepMtvrIn_Type = Counter32
_TrillOamMepMtvrIn_Object = MibTableColumn
trillOamMepMtvrIn = _TrillOamMepMtvrIn_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 7),
    _TrillOamMepMtvrIn_Type()
)
trillOamMepMtvrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrIn.setStatus("current")
_TrillOamMepMtvrInOutofOrder_Type = Counter32
_TrillOamMepMtvrInOutofOrder_Object = MibTableColumn
trillOamMepMtvrInOutofOrder = _TrillOamMepMtvrInOutofOrder_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 8),
    _TrillOamMepMtvrInOutofOrder_Type()
)
trillOamMepMtvrInOutofOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrInOutofOrder.setStatus("current")
_TrillOamMepMtvrOut_Type = Counter32
_TrillOamMepMtvrOut_Object = MibTableColumn
trillOamMepMtvrOut = _TrillOamMepMtvrOut_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 9),
    _TrillOamMepMtvrOut_Type()
)
trillOamMepMtvrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrOut.setStatus("current")


class _TrillOamMepTxLbmDestRName_Type(Unsigned32):
    """Custom type trillOamMepTxLbmDestRName based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65471),
    )


_TrillOamMepTxLbmDestRName_Type.__name__ = "Unsigned32"
_TrillOamMepTxLbmDestRName_Object = MibTableColumn
trillOamMepTxLbmDestRName = _TrillOamMepTxLbmDestRName_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 10),
    _TrillOamMepTxLbmDestRName_Type()
)
trillOamMepTxLbmDestRName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxLbmDestRName.setStatus("current")


class _TrillOamMepTxLbmHC_Type(Unsigned32):
    """Custom type trillOamMepTxLbmHC based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_TrillOamMepTxLbmHC_Type.__name__ = "Unsigned32"
_TrillOamMepTxLbmHC_Object = MibTableColumn
trillOamMepTxLbmHC = _TrillOamMepTxLbmHC_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 11),
    _TrillOamMepTxLbmHC_Type()
)
trillOamMepTxLbmHC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxLbmHC.setStatus("current")
_TrillOamMepTxLbmReplyModeOob_Type = TruthValue
_TrillOamMepTxLbmReplyModeOob_Object = MibTableColumn
trillOamMepTxLbmReplyModeOob = _TrillOamMepTxLbmReplyModeOob_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 12),
    _TrillOamMepTxLbmReplyModeOob_Type()
)
trillOamMepTxLbmReplyModeOob.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxLbmReplyModeOob.setStatus("current")


class _TrillOamMepTransmitLbmReplyIp_Type(OctetString):
    """Custom type trillOamMepTransmitLbmReplyIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_TrillOamMepTransmitLbmReplyIp_Type.__name__ = "OctetString"
_TrillOamMepTransmitLbmReplyIp_Object = MibTableColumn
trillOamMepTransmitLbmReplyIp = _TrillOamMepTransmitLbmReplyIp_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 13),
    _TrillOamMepTransmitLbmReplyIp_Type()
)
trillOamMepTransmitLbmReplyIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTransmitLbmReplyIp.setStatus("current")


class _TrillOamMepTxLbmFlowEntropy_Type(OctetString):
    """Custom type trillOamMepTxLbmFlowEntropy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(96, 96),
    )
    fixedLength = 96


_TrillOamMepTxLbmFlowEntropy_Type.__name__ = "OctetString"
_TrillOamMepTxLbmFlowEntropy_Object = MibTableColumn
trillOamMepTxLbmFlowEntropy = _TrillOamMepTxLbmFlowEntropy_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 14),
    _TrillOamMepTxLbmFlowEntropy_Type()
)
trillOamMepTxLbmFlowEntropy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxLbmFlowEntropy.setStatus("current")


class _TrillOamMepTxPtmDestRName_Type(Unsigned32):
    """Custom type trillOamMepTxPtmDestRName based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65471),
    )


_TrillOamMepTxPtmDestRName_Type.__name__ = "Unsigned32"
_TrillOamMepTxPtmDestRName_Object = MibTableColumn
trillOamMepTxPtmDestRName = _TrillOamMepTxPtmDestRName_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 15),
    _TrillOamMepTxPtmDestRName_Type()
)
trillOamMepTxPtmDestRName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxPtmDestRName.setStatus("current")


class _TrillOamMepTxPtmHC_Type(Unsigned32):
    """Custom type trillOamMepTxPtmHC based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_TrillOamMepTxPtmHC_Type.__name__ = "Unsigned32"
_TrillOamMepTxPtmHC_Object = MibTableColumn
trillOamMepTxPtmHC = _TrillOamMepTxPtmHC_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 16),
    _TrillOamMepTxPtmHC_Type()
)
trillOamMepTxPtmHC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxPtmHC.setStatus("current")


class _TrillOamMepTxPtmReplyModeOob_Type(TruthValue):
    """Custom type trillOamMepTxPtmReplyModeOob based on TruthValue"""
    defaultValue = 2


_TrillOamMepTxPtmReplyModeOob_Type.__name__ = "TruthValue"
_TrillOamMepTxPtmReplyModeOob_Object = MibTableColumn
trillOamMepTxPtmReplyModeOob = _TrillOamMepTxPtmReplyModeOob_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 17),
    _TrillOamMepTxPtmReplyModeOob_Type()
)
trillOamMepTxPtmReplyModeOob.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxPtmReplyModeOob.setStatus("current")


class _TrillOamMepTransmitPtmReplyIp_Type(OctetString):
    """Custom type trillOamMepTransmitPtmReplyIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_TrillOamMepTransmitPtmReplyIp_Type.__name__ = "OctetString"
_TrillOamMepTransmitPtmReplyIp_Object = MibTableColumn
trillOamMepTransmitPtmReplyIp = _TrillOamMepTransmitPtmReplyIp_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 18),
    _TrillOamMepTransmitPtmReplyIp_Type()
)
trillOamMepTransmitPtmReplyIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTransmitPtmReplyIp.setStatus("current")


class _TrillOamMepTxPtmFlowEntropy_Type(OctetString):
    """Custom type trillOamMepTxPtmFlowEntropy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(96, 96),
    )
    fixedLength = 96


_TrillOamMepTxPtmFlowEntropy_Type.__name__ = "OctetString"
_TrillOamMepTxPtmFlowEntropy_Object = MibTableColumn
trillOamMepTxPtmFlowEntropy = _TrillOamMepTxPtmFlowEntropy_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 19),
    _TrillOamMepTxPtmFlowEntropy_Type()
)
trillOamMepTxPtmFlowEntropy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxPtmFlowEntropy.setStatus("current")


class _TrillOamMepTxPtmStatus_Type(TruthValue):
    """Custom type trillOamMepTxPtmStatus based on TruthValue"""
    defaultValue = 2


_TrillOamMepTxPtmStatus_Type.__name__ = "TruthValue"
_TrillOamMepTxPtmStatus_Object = MibTableColumn
trillOamMepTxPtmStatus = _TrillOamMepTxPtmStatus_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 20),
    _TrillOamMepTxPtmStatus_Type()
)
trillOamMepTxPtmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxPtmStatus.setStatus("current")


class _TrillOamMepTxPtmResultOK_Type(TruthValue):
    """Custom type trillOamMepTxPtmResultOK based on TruthValue"""
    defaultValue = 1


_TrillOamMepTxPtmResultOK_Type.__name__ = "TruthValue"
_TrillOamMepTxPtmResultOK_Object = MibTableColumn
trillOamMepTxPtmResultOK = _TrillOamMepTxPtmResultOK_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 21),
    _TrillOamMepTxPtmResultOK_Type()
)
trillOamMepTxPtmResultOK.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxPtmResultOK.setStatus("current")
_TrillOamMepTxPtmSeqNumber_Type = Unsigned32
_TrillOamMepTxPtmSeqNumber_Object = MibTableColumn
trillOamMepTxPtmSeqNumber = _TrillOamMepTxPtmSeqNumber_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 22),
    _TrillOamMepTxPtmSeqNumber_Type()
)
trillOamMepTxPtmSeqNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxPtmSeqNumber.setStatus("current")


class _TrillOamMepTxPtmMessages_Type(Integer32):
    """Custom type trillOamMepTxPtmMessages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_TrillOamMepTxPtmMessages_Type.__name__ = "Integer32"
_TrillOamMepTxPtmMessages_Object = MibTableColumn
trillOamMepTxPtmMessages = _TrillOamMepTxPtmMessages_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 23),
    _TrillOamMepTxPtmMessages_Type()
)
trillOamMepTxPtmMessages.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxPtmMessages.setStatus("current")
_TrillOamMepTxMtvmTree_Type = Unsigned32
_TrillOamMepTxMtvmTree_Object = MibTableColumn
trillOamMepTxMtvmTree = _TrillOamMepTxMtvmTree_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 24),
    _TrillOamMepTxMtvmTree_Type()
)
trillOamMepTxMtvmTree.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxMtvmTree.setStatus("current")


class _TrillOamMepTxMtvmHC_Type(Unsigned32):
    """Custom type trillOamMepTxMtvmHC based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_TrillOamMepTxMtvmHC_Type.__name__ = "Unsigned32"
_TrillOamMepTxMtvmHC_Object = MibTableColumn
trillOamMepTxMtvmHC = _TrillOamMepTxMtvmHC_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 25),
    _TrillOamMepTxMtvmHC_Type()
)
trillOamMepTxMtvmHC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxMtvmHC.setStatus("current")
_TrillOamMepTxMtvmReplyModeOob_Type = TruthValue
_TrillOamMepTxMtvmReplyModeOob_Object = MibTableColumn
trillOamMepTxMtvmReplyModeOob = _TrillOamMepTxMtvmReplyModeOob_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 26),
    _TrillOamMepTxMtvmReplyModeOob_Type()
)
trillOamMepTxMtvmReplyModeOob.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxMtvmReplyModeOob.setStatus("current")


class _TrillOamMepTransmitMtvmReplyIp_Type(OctetString):
    """Custom type trillOamMepTransmitMtvmReplyIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_TrillOamMepTransmitMtvmReplyIp_Type.__name__ = "OctetString"
_TrillOamMepTransmitMtvmReplyIp_Object = MibTableColumn
trillOamMepTransmitMtvmReplyIp = _TrillOamMepTransmitMtvmReplyIp_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 27),
    _TrillOamMepTransmitMtvmReplyIp_Type()
)
trillOamMepTransmitMtvmReplyIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTransmitMtvmReplyIp.setStatus("current")


class _TrillOamMepTxMtvmFlowEntropy_Type(OctetString):
    """Custom type trillOamMepTxMtvmFlowEntropy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(96, 96),
    )
    fixedLength = 96


_TrillOamMepTxMtvmFlowEntropy_Type.__name__ = "OctetString"
_TrillOamMepTxMtvmFlowEntropy_Object = MibTableColumn
trillOamMepTxMtvmFlowEntropy = _TrillOamMepTxMtvmFlowEntropy_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 28),
    _TrillOamMepTxMtvmFlowEntropy_Type()
)
trillOamMepTxMtvmFlowEntropy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxMtvmFlowEntropy.setStatus("current")


class _TrillOamMepTxMtvmStatus_Type(TruthValue):
    """Custom type trillOamMepTxMtvmStatus based on TruthValue"""
    defaultValue = 2


_TrillOamMepTxMtvmStatus_Type.__name__ = "TruthValue"
_TrillOamMepTxMtvmStatus_Object = MibTableColumn
trillOamMepTxMtvmStatus = _TrillOamMepTxMtvmStatus_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 29),
    _TrillOamMepTxMtvmStatus_Type()
)
trillOamMepTxMtvmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxMtvmStatus.setStatus("current")


class _TrillOamMepTxMtvmResultOK_Type(TruthValue):
    """Custom type trillOamMepTxMtvmResultOK based on TruthValue"""
    defaultValue = 1


_TrillOamMepTxMtvmResultOK_Type.__name__ = "TruthValue"
_TrillOamMepTxMtvmResultOK_Object = MibTableColumn
trillOamMepTxMtvmResultOK = _TrillOamMepTxMtvmResultOK_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 30),
    _TrillOamMepTxMtvmResultOK_Type()
)
trillOamMepTxMtvmResultOK.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxMtvmResultOK.setStatus("current")


class _TrillOamMepTxMtvmMessages_Type(Integer32):
    """Custom type trillOamMepTxMtvmMessages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_TrillOamMepTxMtvmMessages_Type.__name__ = "Integer32"
_TrillOamMepTxMtvmMessages_Object = MibTableColumn
trillOamMepTxMtvmMessages = _TrillOamMepTxMtvmMessages_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 31),
    _TrillOamMepTxMtvmMessages_Type()
)
trillOamMepTxMtvmMessages.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxMtvmMessages.setStatus("current")
_TrillOamMepTxMtvmSeqNumber_Type = Unsigned32
_TrillOamMepTxMtvmSeqNumber_Object = MibTableColumn
trillOamMepTxMtvmSeqNumber = _TrillOamMepTxMtvmSeqNumber_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 32),
    _TrillOamMepTxMtvmSeqNumber_Type()
)
trillOamMepTxMtvmSeqNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxMtvmSeqNumber.setStatus("current")
_TrillOamMepTxMtvmScopeList_Type = OctetString
_TrillOamMepTxMtvmScopeList_Object = MibTableColumn
trillOamMepTxMtvmScopeList = _TrillOamMepTxMtvmScopeList_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 33),
    _TrillOamMepTxMtvmScopeList_Type()
)
trillOamMepTxMtvmScopeList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepTxMtvmScopeList.setStatus("current")
_TrillOamMepDiscontinuityTime_Type = TimeStamp
_TrillOamMepDiscontinuityTime_Object = MibTableColumn
trillOamMepDiscontinuityTime = _TrillOamMepDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 1, 1, 34),
    _TrillOamMepDiscontinuityTime_Type()
)
trillOamMepDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepDiscontinuityTime.setStatus("current")
_TrillOamMepFlowCfgTable_Object = MibTable
trillOamMepFlowCfgTable = _TrillOamMepFlowCfgTable_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 2)
)
if mibBuilder.loadTexts:
    trillOamMepFlowCfgTable.setStatus("current")
_TrillOamMepFlowCfgEntry_Object = MibTableRow
trillOamMepFlowCfgEntry = _TrillOamMepFlowCfgEntry_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 2, 1)
)
trillOamMepFlowCfgEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "TRILL-OAM-MIB", "trillOamMepFlowCfgIndex"),
)
if mibBuilder.loadTexts:
    trillOamMepFlowCfgEntry.setStatus("current")


class _TrillOamMepFlowCfgIndex_Type(Unsigned32):
    """Custom type trillOamMepFlowCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrillOamMepFlowCfgIndex_Type.__name__ = "Unsigned32"
_TrillOamMepFlowCfgIndex_Object = MibTableColumn
trillOamMepFlowCfgIndex = _TrillOamMepFlowCfgIndex_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 2, 1, 1),
    _TrillOamMepFlowCfgIndex_Type()
)
trillOamMepFlowCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trillOamMepFlowCfgIndex.setStatus("current")


class _TrillOamMepFlowCfgFlowEntropy_Type(OctetString):
    """Custom type trillOamMepFlowCfgFlowEntropy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(96, 96),
    )
    fixedLength = 96


_TrillOamMepFlowCfgFlowEntropy_Type.__name__ = "OctetString"
_TrillOamMepFlowCfgFlowEntropy_Object = MibTableColumn
trillOamMepFlowCfgFlowEntropy = _TrillOamMepFlowCfgFlowEntropy_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 2, 1, 2),
    _TrillOamMepFlowCfgFlowEntropy_Type()
)
trillOamMepFlowCfgFlowEntropy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepFlowCfgFlowEntropy.setStatus("current")


class _TrillOamMepFlowCfgDestRName_Type(Unsigned32):
    """Custom type trillOamMepFlowCfgDestRName based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65471),
    )


_TrillOamMepFlowCfgDestRName_Type.__name__ = "Unsigned32"
_TrillOamMepFlowCfgDestRName_Object = MibTableColumn
trillOamMepFlowCfgDestRName = _TrillOamMepFlowCfgDestRName_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 2, 1, 3),
    _TrillOamMepFlowCfgDestRName_Type()
)
trillOamMepFlowCfgDestRName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepFlowCfgDestRName.setStatus("current")


class _TrillOamMepFlowCfgFlowHC_Type(Unsigned32):
    """Custom type trillOamMepFlowCfgFlowHC based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_TrillOamMepFlowCfgFlowHC_Type.__name__ = "Unsigned32"
_TrillOamMepFlowCfgFlowHC_Object = MibTableColumn
trillOamMepFlowCfgFlowHC = _TrillOamMepFlowCfgFlowHC_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 2, 1, 4),
    _TrillOamMepFlowCfgFlowHC_Type()
)
trillOamMepFlowCfgFlowHC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepFlowCfgFlowHC.setStatus("current")
_TrillOamMepFlowCfgRowStatus_Type = RowStatus
_TrillOamMepFlowCfgRowStatus_Object = MibTableColumn
trillOamMepFlowCfgRowStatus = _TrillOamMepFlowCfgRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 2, 1, 5),
    _TrillOamMepFlowCfgRowStatus_Type()
)
trillOamMepFlowCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trillOamMepFlowCfgRowStatus.setStatus("current")
_TrillOamPtrTable_Object = MibTable
trillOamPtrTable = _TrillOamPtrTable_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3)
)
if mibBuilder.loadTexts:
    trillOamPtrTable.setStatus("current")
_TrillOamPtrEntry_Object = MibTableRow
trillOamPtrEntry = _TrillOamPtrEntry_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1)
)
trillOamPtrEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "TRILL-OAM-MIB", "trillOamMepPtrTransactionId"),
)
if mibBuilder.loadTexts:
    trillOamPtrEntry.setStatus("current")


class _TrillOamMepPtrTransactionId_Type(Unsigned32):
    """Custom type trillOamMepPtrTransactionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrillOamMepPtrTransactionId_Type.__name__ = "Unsigned32"
_TrillOamMepPtrTransactionId_Object = MibTableColumn
trillOamMepPtrTransactionId = _TrillOamMepPtrTransactionId_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1, 1),
    _TrillOamMepPtrTransactionId_Type()
)
trillOamMepPtrTransactionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trillOamMepPtrTransactionId.setStatus("current")


class _TrillOamMepPtrHC_Type(Unsigned32):
    """Custom type trillOamMepPtrHC based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_TrillOamMepPtrHC_Type.__name__ = "Unsigned32"
_TrillOamMepPtrHC_Object = MibTableColumn
trillOamMepPtrHC = _TrillOamMepPtrHC_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1, 2),
    _TrillOamMepPtrHC_Type()
)
trillOamMepPtrHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrHC.setStatus("current")


class _TrillOamMepPtrFlag_Type(Unsigned32):
    """Custom type trillOamMepPtrFlag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TrillOamMepPtrFlag_Type.__name__ = "Unsigned32"
_TrillOamMepPtrFlag_Object = MibTableColumn
trillOamMepPtrFlag = _TrillOamMepPtrFlag_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1, 3),
    _TrillOamMepPtrFlag_Type()
)
trillOamMepPtrFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrFlag.setStatus("current")


class _TrillOamMepPtrErrorCode_Type(Unsigned32):
    """Custom type trillOamMepPtrErrorCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrillOamMepPtrErrorCode_Type.__name__ = "Unsigned32"
_TrillOamMepPtrErrorCode_Object = MibTableColumn
trillOamMepPtrErrorCode = _TrillOamMepPtrErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1, 4),
    _TrillOamMepPtrErrorCode_Type()
)
trillOamMepPtrErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrErrorCode.setStatus("current")
_TrillOamMepPtrTerminalMep_Type = TruthValue
_TrillOamMepPtrTerminalMep_Object = MibTableColumn
trillOamMepPtrTerminalMep = _TrillOamMepPtrTerminalMep_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1, 5),
    _TrillOamMepPtrTerminalMep_Type()
)
trillOamMepPtrTerminalMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrTerminalMep.setStatus("current")


class _TrillOamMepPtrLastEgressId_Type(Unsigned32):
    """Custom type trillOamMepPtrLastEgressId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrillOamMepPtrLastEgressId_Type.__name__ = "Unsigned32"
_TrillOamMepPtrLastEgressId_Object = MibTableColumn
trillOamMepPtrLastEgressId = _TrillOamMepPtrLastEgressId_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1, 6),
    _TrillOamMepPtrLastEgressId_Type()
)
trillOamMepPtrLastEgressId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrLastEgressId.setStatus("current")
_TrillOamMepPtrIngress_Type = Dot1agCfmIngressActionFieldValue
_TrillOamMepPtrIngress_Object = MibTableColumn
trillOamMepPtrIngress = _TrillOamMepPtrIngress_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1, 7),
    _TrillOamMepPtrIngress_Type()
)
trillOamMepPtrIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrIngress.setStatus("current")
_TrillOamMepPtrIngressMac_Type = MacAddress
_TrillOamMepPtrIngressMac_Object = MibTableColumn
trillOamMepPtrIngressMac = _TrillOamMepPtrIngressMac_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1, 8),
    _TrillOamMepPtrIngressMac_Type()
)
trillOamMepPtrIngressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrIngressMac.setStatus("current")
_TrillOamMepPtrIngressPortIdSubtype_Type = LldpPortIdSubtype
_TrillOamMepPtrIngressPortIdSubtype_Object = MibTableColumn
trillOamMepPtrIngressPortIdSubtype = _TrillOamMepPtrIngressPortIdSubtype_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1, 9),
    _TrillOamMepPtrIngressPortIdSubtype_Type()
)
trillOamMepPtrIngressPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrIngressPortIdSubtype.setStatus("current")
_TrillOamMepPtrIngressPortId_Type = LldpPortId
_TrillOamMepPtrIngressPortId_Object = MibTableColumn
trillOamMepPtrIngressPortId = _TrillOamMepPtrIngressPortId_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1, 10),
    _TrillOamMepPtrIngressPortId_Type()
)
trillOamMepPtrIngressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrIngressPortId.setStatus("current")
_TrillOamMepPtrEgress_Type = Dot1agCfmEgressActionFieldValue
_TrillOamMepPtrEgress_Object = MibTableColumn
trillOamMepPtrEgress = _TrillOamMepPtrEgress_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1, 11),
    _TrillOamMepPtrEgress_Type()
)
trillOamMepPtrEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrEgress.setStatus("current")
_TrillOamMepPtrEgressMac_Type = MacAddress
_TrillOamMepPtrEgressMac_Object = MibTableColumn
trillOamMepPtrEgressMac = _TrillOamMepPtrEgressMac_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1, 12),
    _TrillOamMepPtrEgressMac_Type()
)
trillOamMepPtrEgressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrEgressMac.setStatus("current")
_TrillOamMepPtrEgressPortIdSubtype_Type = LldpPortIdSubtype
_TrillOamMepPtrEgressPortIdSubtype_Object = MibTableColumn
trillOamMepPtrEgressPortIdSubtype = _TrillOamMepPtrEgressPortIdSubtype_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1, 13),
    _TrillOamMepPtrEgressPortIdSubtype_Type()
)
trillOamMepPtrEgressPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrEgressPortIdSubtype.setStatus("current")
_TrillOamMepPtrEgressPortId_Type = LldpPortId
_TrillOamMepPtrEgressPortId_Object = MibTableColumn
trillOamMepPtrEgressPortId = _TrillOamMepPtrEgressPortId_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1, 14),
    _TrillOamMepPtrEgressPortId_Type()
)
trillOamMepPtrEgressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrEgressPortId.setStatus("current")
_TrillOamMepPtrChassisIdSubtype_Type = LldpChassisIdSubtype
_TrillOamMepPtrChassisIdSubtype_Object = MibTableColumn
trillOamMepPtrChassisIdSubtype = _TrillOamMepPtrChassisIdSubtype_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1, 15),
    _TrillOamMepPtrChassisIdSubtype_Type()
)
trillOamMepPtrChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrChassisIdSubtype.setStatus("current")
_TrillOamMepPtrChassisId_Type = LldpChassisId
_TrillOamMepPtrChassisId_Object = MibTableColumn
trillOamMepPtrChassisId = _TrillOamMepPtrChassisId_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1, 16),
    _TrillOamMepPtrChassisId_Type()
)
trillOamMepPtrChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrChassisId.setStatus("current")


class _TrillOamMepPtrOrganizationSpecificTlv_Type(OctetString):
    """Custom type trillOamMepPtrOrganizationSpecificTlv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 1500),
    )


_TrillOamMepPtrOrganizationSpecificTlv_Type.__name__ = "OctetString"
_TrillOamMepPtrOrganizationSpecificTlv_Object = MibTableColumn
trillOamMepPtrOrganizationSpecificTlv = _TrillOamMepPtrOrganizationSpecificTlv_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1, 17),
    _TrillOamMepPtrOrganizationSpecificTlv_Type()
)
trillOamMepPtrOrganizationSpecificTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrOrganizationSpecificTlv.setStatus("current")


class _TrillOamMepPtrNextHopNicknames_Type(OctetString):
    """Custom type trillOamMepPtrNextHopNicknames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 1500),
    )


_TrillOamMepPtrNextHopNicknames_Type.__name__ = "OctetString"
_TrillOamMepPtrNextHopNicknames_Object = MibTableColumn
trillOamMepPtrNextHopNicknames = _TrillOamMepPtrNextHopNicknames_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 3, 1, 18),
    _TrillOamMepPtrNextHopNicknames_Type()
)
trillOamMepPtrNextHopNicknames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepPtrNextHopNicknames.setStatus("current")
_TrillOamMtvrTable_Object = MibTable
trillOamMtvrTable = _TrillOamMtvrTable_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4)
)
if mibBuilder.loadTexts:
    trillOamMtvrTable.setStatus("current")
_TrillOamMtvrEntry_Object = MibTableRow
trillOamMtvrEntry = _TrillOamMtvrEntry_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1)
)
trillOamMtvrEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "TRILL-OAM-MIB", "trillOamMepPtrTransactionId"),
    (0, "TRILL-OAM-MIB", "trillOamMepMtvrReceiveOrder"),
)
if mibBuilder.loadTexts:
    trillOamMtvrEntry.setStatus("current")


class _TrillOamMepMtvrTransactionId_Type(Unsigned32):
    """Custom type trillOamMepMtvrTransactionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrillOamMepMtvrTransactionId_Type.__name__ = "Unsigned32"
_TrillOamMepMtvrTransactionId_Object = MibTableColumn
trillOamMepMtvrTransactionId = _TrillOamMepMtvrTransactionId_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 1),
    _TrillOamMepMtvrTransactionId_Type()
)
trillOamMepMtvrTransactionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trillOamMepMtvrTransactionId.setStatus("current")


class _TrillOamMepMtvrReceiveOrder_Type(Unsigned32):
    """Custom type trillOamMepMtvrReceiveOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TrillOamMepMtvrReceiveOrder_Type.__name__ = "Unsigned32"
_TrillOamMepMtvrReceiveOrder_Object = MibTableColumn
trillOamMepMtvrReceiveOrder = _TrillOamMepMtvrReceiveOrder_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 2),
    _TrillOamMepMtvrReceiveOrder_Type()
)
trillOamMepMtvrReceiveOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trillOamMepMtvrReceiveOrder.setStatus("current")


class _TrillOamMepMtvrFlag_Type(Unsigned32):
    """Custom type trillOamMepMtvrFlag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TrillOamMepMtvrFlag_Type.__name__ = "Unsigned32"
_TrillOamMepMtvrFlag_Object = MibTableColumn
trillOamMepMtvrFlag = _TrillOamMepMtvrFlag_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 3),
    _TrillOamMepMtvrFlag_Type()
)
trillOamMepMtvrFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrFlag.setStatus("current")


class _TrillOamMepMtvrErrorCode_Type(Unsigned32):
    """Custom type trillOamMepMtvrErrorCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrillOamMepMtvrErrorCode_Type.__name__ = "Unsigned32"
_TrillOamMepMtvrErrorCode_Object = MibTableColumn
trillOamMepMtvrErrorCode = _TrillOamMepMtvrErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 4),
    _TrillOamMepMtvrErrorCode_Type()
)
trillOamMepMtvrErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrErrorCode.setStatus("current")


class _TrillOamMepMtvrLastEgressId_Type(Unsigned32):
    """Custom type trillOamMepMtvrLastEgressId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrillOamMepMtvrLastEgressId_Type.__name__ = "Unsigned32"
_TrillOamMepMtvrLastEgressId_Object = MibTableColumn
trillOamMepMtvrLastEgressId = _TrillOamMepMtvrLastEgressId_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 5),
    _TrillOamMepMtvrLastEgressId_Type()
)
trillOamMepMtvrLastEgressId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrLastEgressId.setStatus("current")
_TrillOamMepMtvrIngress_Type = Dot1agCfmIngressActionFieldValue
_TrillOamMepMtvrIngress_Object = MibTableColumn
trillOamMepMtvrIngress = _TrillOamMepMtvrIngress_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 6),
    _TrillOamMepMtvrIngress_Type()
)
trillOamMepMtvrIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrIngress.setStatus("current")
_TrillOamMepMtvrIngressMac_Type = MacAddress
_TrillOamMepMtvrIngressMac_Object = MibTableColumn
trillOamMepMtvrIngressMac = _TrillOamMepMtvrIngressMac_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 7),
    _TrillOamMepMtvrIngressMac_Type()
)
trillOamMepMtvrIngressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrIngressMac.setStatus("current")
_TrillOamMepMtvrIngressPortIdSubtype_Type = LldpPortIdSubtype
_TrillOamMepMtvrIngressPortIdSubtype_Object = MibTableColumn
trillOamMepMtvrIngressPortIdSubtype = _TrillOamMepMtvrIngressPortIdSubtype_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 8),
    _TrillOamMepMtvrIngressPortIdSubtype_Type()
)
trillOamMepMtvrIngressPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrIngressPortIdSubtype.setStatus("current")
_TrillOamMepMtvrIngressPortId_Type = LldpPortId
_TrillOamMepMtvrIngressPortId_Object = MibTableColumn
trillOamMepMtvrIngressPortId = _TrillOamMepMtvrIngressPortId_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 9),
    _TrillOamMepMtvrIngressPortId_Type()
)
trillOamMepMtvrIngressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrIngressPortId.setStatus("current")
_TrillOamMepMtvrEgress_Type = Dot1agCfmEgressActionFieldValue
_TrillOamMepMtvrEgress_Object = MibTableColumn
trillOamMepMtvrEgress = _TrillOamMepMtvrEgress_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 10),
    _TrillOamMepMtvrEgress_Type()
)
trillOamMepMtvrEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrEgress.setStatus("current")
_TrillOamMepMtvrEgressMac_Type = MacAddress
_TrillOamMepMtvrEgressMac_Object = MibTableColumn
trillOamMepMtvrEgressMac = _TrillOamMepMtvrEgressMac_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 11),
    _TrillOamMepMtvrEgressMac_Type()
)
trillOamMepMtvrEgressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrEgressMac.setStatus("current")
_TrillOamMepMtvrEgressPortIdSubtype_Type = LldpPortIdSubtype
_TrillOamMepMtvrEgressPortIdSubtype_Object = MibTableColumn
trillOamMepMtvrEgressPortIdSubtype = _TrillOamMepMtvrEgressPortIdSubtype_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 12),
    _TrillOamMepMtvrEgressPortIdSubtype_Type()
)
trillOamMepMtvrEgressPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrEgressPortIdSubtype.setStatus("current")
_TrillOamMepMtvrEgressPortId_Type = LldpPortId
_TrillOamMepMtvrEgressPortId_Object = MibTableColumn
trillOamMepMtvrEgressPortId = _TrillOamMepMtvrEgressPortId_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 13),
    _TrillOamMepMtvrEgressPortId_Type()
)
trillOamMepMtvrEgressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrEgressPortId.setStatus("current")
_TrillOamMepMtvrChassisIdSubtype_Type = LldpChassisIdSubtype
_TrillOamMepMtvrChassisIdSubtype_Object = MibTableColumn
trillOamMepMtvrChassisIdSubtype = _TrillOamMepMtvrChassisIdSubtype_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 14),
    _TrillOamMepMtvrChassisIdSubtype_Type()
)
trillOamMepMtvrChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrChassisIdSubtype.setStatus("current")
_TrillOamMepMtvrChassisId_Type = LldpChassisId
_TrillOamMepMtvrChassisId_Object = MibTableColumn
trillOamMepMtvrChassisId = _TrillOamMepMtvrChassisId_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 15),
    _TrillOamMepMtvrChassisId_Type()
)
trillOamMepMtvrChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrChassisId.setStatus("current")


class _TrillOamMepMtvrOrganizationSpecificTlv_Type(OctetString):
    """Custom type trillOamMepMtvrOrganizationSpecificTlv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 1500),
    )


_TrillOamMepMtvrOrganizationSpecificTlv_Type.__name__ = "OctetString"
_TrillOamMepMtvrOrganizationSpecificTlv_Object = MibTableColumn
trillOamMepMtvrOrganizationSpecificTlv = _TrillOamMepMtvrOrganizationSpecificTlv_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 16),
    _TrillOamMepMtvrOrganizationSpecificTlv_Type()
)
trillOamMepMtvrOrganizationSpecificTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrOrganizationSpecificTlv.setStatus("current")


class _TrillOamMepMtvrNextHopNicknames_Type(OctetString):
    """Custom type trillOamMepMtvrNextHopNicknames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 1500),
    )


_TrillOamMepMtvrNextHopNicknames_Type.__name__ = "OctetString"
_TrillOamMepMtvrNextHopNicknames_Object = MibTableColumn
trillOamMepMtvrNextHopNicknames = _TrillOamMepMtvrNextHopNicknames_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 17),
    _TrillOamMepMtvrNextHopNicknames_Type()
)
trillOamMepMtvrNextHopNicknames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrNextHopNicknames.setStatus("current")
_TrillOamMepMtvrReceiverAvailability_Type = TruthValue
_TrillOamMepMtvrReceiverAvailability_Object = MibTableColumn
trillOamMepMtvrReceiverAvailability = _TrillOamMepMtvrReceiverAvailability_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 18),
    _TrillOamMepMtvrReceiverAvailability_Type()
)
trillOamMepMtvrReceiverAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrReceiverAvailability.setStatus("current")
_TrillOamMepMtvrReceiverCount_Type = TruthValue
_TrillOamMepMtvrReceiverCount_Object = MibTableColumn
trillOamMepMtvrReceiverCount = _TrillOamMepMtvrReceiverCount_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 4, 1, 19),
    _TrillOamMepMtvrReceiverCount_Type()
)
trillOamMepMtvrReceiverCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepMtvrReceiverCount.setStatus("current")
_TrillOamMepDbTable_Object = MibTable
trillOamMepDbTable = _TrillOamMepDbTable_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 5)
)
if mibBuilder.loadTexts:
    trillOamMepDbTable.setStatus("current")
_TrillOamMepDbEntry_Object = MibTableRow
trillOamMepDbEntry = _TrillOamMepDbEntry_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    trillOamMepDbEntry.setStatus("current")


class _TrillOamMepDbFlowIndex_Type(Unsigned32):
    """Custom type trillOamMepDbFlowIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrillOamMepDbFlowIndex_Type.__name__ = "Unsigned32"
_TrillOamMepDbFlowIndex_Object = MibTableColumn
trillOamMepDbFlowIndex = _TrillOamMepDbFlowIndex_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 5, 1, 1),
    _TrillOamMepDbFlowIndex_Type()
)
trillOamMepDbFlowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepDbFlowIndex.setStatus("current")


class _TrillOamMepDbFlowEntropy_Type(OctetString):
    """Custom type trillOamMepDbFlowEntropy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(96, 96),
    )
    fixedLength = 96


_TrillOamMepDbFlowEntropy_Type.__name__ = "OctetString"
_TrillOamMepDbFlowEntropy_Object = MibTableColumn
trillOamMepDbFlowEntropy = _TrillOamMepDbFlowEntropy_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 5, 1, 2),
    _TrillOamMepDbFlowEntropy_Type()
)
trillOamMepDbFlowEntropy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepDbFlowEntropy.setStatus("current")
_TrillOamMepDbFlowState_Type = Dot1agCfmRemoteMepState
_TrillOamMepDbFlowState_Object = MibTableColumn
trillOamMepDbFlowState = _TrillOamMepDbFlowState_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 5, 1, 3),
    _TrillOamMepDbFlowState_Type()
)
trillOamMepDbFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepDbFlowState.setStatus("current")
_TrillOamMepDbFlowFailedOkTime_Type = TimeStamp
_TrillOamMepDbFlowFailedOkTime_Object = MibTableColumn
trillOamMepDbFlowFailedOkTime = _TrillOamMepDbFlowFailedOkTime_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 5, 1, 4),
    _TrillOamMepDbFlowFailedOkTime_Type()
)
trillOamMepDbFlowFailedOkTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepDbFlowFailedOkTime.setStatus("current")


class _TrillOamMepDbRBridgeName_Type(Unsigned32):
    """Custom type trillOamMepDbRBridgeName based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65471),
    )


_TrillOamMepDbRBridgeName_Type.__name__ = "Unsigned32"
_TrillOamMepDbRBridgeName_Object = MibTableColumn
trillOamMepDbRBridgeName = _TrillOamMepDbRBridgeName_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 5, 1, 5),
    _TrillOamMepDbRBridgeName_Type()
)
trillOamMepDbRBridgeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepDbRBridgeName.setStatus("current")
_TrillOamMepDbLastGoodSeqNum_Type = Counter32
_TrillOamMepDbLastGoodSeqNum_Object = MibTableColumn
trillOamMepDbLastGoodSeqNum = _TrillOamMepDbLastGoodSeqNum_Object(
    (1, 3, 6, 1, 2, 1, 238, 1, 1, 5, 1, 6),
    _TrillOamMepDbLastGoodSeqNum_Type()
)
trillOamMepDbLastGoodSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trillOamMepDbLastGoodSeqNum.setStatus("current")
_TrillOamMibConformance_ObjectIdentity = ObjectIdentity
trillOamMibConformance = _TrillOamMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 238, 2)
)
_TrillOamMibCompliances_ObjectIdentity = ObjectIdentity
trillOamMibCompliances = _TrillOamMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 238, 2, 1)
)
_TrillOamMibGroups_ObjectIdentity = ObjectIdentity
trillOamMibGroups = _TrillOamMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 238, 2, 2)
)
dot1agCfmMepEntry.registerAugmentions(
    ("TRILL-OAM-MIB",
     "trillOamMepEntry")
)
trillOamMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepDbEntry.registerAugmentions(
    ("TRILL-OAM-MIB",
     "trillOamMepDbEntry")
)
trillOamMepDbEntry.setIndexNames(*dot1agCfmMepDbEntry.getIndexNames())

# Managed Objects groups

trillOamMepMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 238, 2, 2, 1)
)
trillOamMepMandatoryGroup.setObjects(
      *(("TRILL-OAM-MIB", "trillOamMepRName"),
        ("TRILL-OAM-MIB", "trillOamMepNextPtmTId"),
        ("TRILL-OAM-MIB", "trillOamMepNextMtvmTId"),
        ("TRILL-OAM-MIB", "trillOamMepPtrIn"),
        ("TRILL-OAM-MIB", "trillOamMepPtrInOutofOrder"),
        ("TRILL-OAM-MIB", "trillOamMepPtrOut"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrIn"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrInOutofOrder"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrOut"),
        ("TRILL-OAM-MIB", "trillOamMepTxLbmDestRName"),
        ("TRILL-OAM-MIB", "trillOamMepTxLbmHC"),
        ("TRILL-OAM-MIB", "trillOamMepTxLbmReplyModeOob"),
        ("TRILL-OAM-MIB", "trillOamMepTransmitLbmReplyIp"),
        ("TRILL-OAM-MIB", "trillOamMepTxLbmFlowEntropy"),
        ("TRILL-OAM-MIB", "trillOamMepTxPtmDestRName"),
        ("TRILL-OAM-MIB", "trillOamMepTxPtmHC"),
        ("TRILL-OAM-MIB", "trillOamMepTxPtmReplyModeOob"),
        ("TRILL-OAM-MIB", "trillOamMepTransmitPtmReplyIp"),
        ("TRILL-OAM-MIB", "trillOamMepTxPtmFlowEntropy"),
        ("TRILL-OAM-MIB", "trillOamMepTxPtmStatus"),
        ("TRILL-OAM-MIB", "trillOamMepTxPtmResultOK"),
        ("TRILL-OAM-MIB", "trillOamMepTxPtmMessages"),
        ("TRILL-OAM-MIB", "trillOamMepTxPtmSeqNumber"),
        ("TRILL-OAM-MIB", "trillOamMepTxMtvmTree"),
        ("TRILL-OAM-MIB", "trillOamMepTxMtvmHC"),
        ("TRILL-OAM-MIB", "trillOamMepTxMtvmReplyModeOob"),
        ("TRILL-OAM-MIB", "trillOamMepTransmitMtvmReplyIp"),
        ("TRILL-OAM-MIB", "trillOamMepTxMtvmFlowEntropy"),
        ("TRILL-OAM-MIB", "trillOamMepTxMtvmStatus"),
        ("TRILL-OAM-MIB", "trillOamMepTxMtvmResultOK"),
        ("TRILL-OAM-MIB", "trillOamMepTxMtvmMessages"),
        ("TRILL-OAM-MIB", "trillOamMepTxMtvmSeqNumber"),
        ("TRILL-OAM-MIB", "trillOamMepTxMtvmScopeList"),
        ("TRILL-OAM-MIB", "trillOamMepDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    trillOamMepMandatoryGroup.setStatus("current")

trillOamMepFlowCfgTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 238, 2, 2, 2)
)
trillOamMepFlowCfgTableGroup.setObjects(
      *(("TRILL-OAM-MIB", "trillOamMepFlowCfgFlowEntropy"),
        ("TRILL-OAM-MIB", "trillOamMepFlowCfgDestRName"),
        ("TRILL-OAM-MIB", "trillOamMepFlowCfgFlowHC"),
        ("TRILL-OAM-MIB", "trillOamMepFlowCfgRowStatus"))
)
if mibBuilder.loadTexts:
    trillOamMepFlowCfgTableGroup.setStatus("current")

trillOamPtrTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 238, 2, 2, 3)
)
trillOamPtrTableGroup.setObjects(
      *(("TRILL-OAM-MIB", "trillOamMepPtrHC"),
        ("TRILL-OAM-MIB", "trillOamMepPtrFlag"),
        ("TRILL-OAM-MIB", "trillOamMepPtrErrorCode"),
        ("TRILL-OAM-MIB", "trillOamMepPtrTerminalMep"),
        ("TRILL-OAM-MIB", "trillOamMepPtrLastEgressId"),
        ("TRILL-OAM-MIB", "trillOamMepPtrIngress"),
        ("TRILL-OAM-MIB", "trillOamMepPtrIngressMac"),
        ("TRILL-OAM-MIB", "trillOamMepPtrIngressPortIdSubtype"),
        ("TRILL-OAM-MIB", "trillOamMepPtrIngressPortId"),
        ("TRILL-OAM-MIB", "trillOamMepPtrEgress"),
        ("TRILL-OAM-MIB", "trillOamMepPtrEgressMac"),
        ("TRILL-OAM-MIB", "trillOamMepPtrEgressPortIdSubtype"),
        ("TRILL-OAM-MIB", "trillOamMepPtrEgressPortId"),
        ("TRILL-OAM-MIB", "trillOamMepPtrChassisIdSubtype"),
        ("TRILL-OAM-MIB", "trillOamMepPtrChassisId"),
        ("TRILL-OAM-MIB", "trillOamMepPtrOrganizationSpecificTlv"),
        ("TRILL-OAM-MIB", "trillOamMepPtrNextHopNicknames"))
)
if mibBuilder.loadTexts:
    trillOamPtrTableGroup.setStatus("current")

trillOamMtvrTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 238, 2, 2, 4)
)
trillOamMtvrTableGroup.setObjects(
      *(("TRILL-OAM-MIB", "trillOamMepMtvrFlag"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrErrorCode"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrLastEgressId"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrIngress"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrIngressMac"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrIngressPortIdSubtype"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrIngressPortId"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrEgress"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrEgressMac"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrEgressPortIdSubtype"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrEgressPortId"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrChassisIdSubtype"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrChassisId"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrOrganizationSpecificTlv"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrNextHopNicknames"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrReceiverAvailability"),
        ("TRILL-OAM-MIB", "trillOamMepMtvrReceiverCount"))
)
if mibBuilder.loadTexts:
    trillOamMtvrTableGroup.setStatus("current")

trillOamMepDbGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 238, 2, 2, 5)
)
trillOamMepDbGroup.setObjects(
      *(("TRILL-OAM-MIB", "trillOamMepDbFlowIndex"),
        ("TRILL-OAM-MIB", "trillOamMepDbFlowEntropy"),
        ("TRILL-OAM-MIB", "trillOamMepDbFlowState"),
        ("TRILL-OAM-MIB", "trillOamMepDbFlowFailedOkTime"),
        ("TRILL-OAM-MIB", "trillOamMepDbRBridgeName"),
        ("TRILL-OAM-MIB", "trillOamMepDbLastGoodSeqNum"))
)
if mibBuilder.loadTexts:
    trillOamMepDbGroup.setStatus("current")


# Notification objects

trillOamFaultAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 238, 0, 1)
)
trillOamFaultAlarm.setObjects(
    ("TRILL-OAM-MIB", "trillOamMepDbFlowState")
)
if mibBuilder.loadTexts:
    trillOamFaultAlarm.setStatus(
        "current"
    )


# Notifications groups

trillOamNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 238, 2, 2, 6)
)
trillOamNotificationGroup.setObjects(
    ("TRILL-OAM-MIB", "trillOamFaultAlarm")
)
if mibBuilder.loadTexts:
    trillOamNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

trillOamMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 238, 2, 1, 1)
)
trillOamMibCompliance.setObjects(
      *(("TRILL-OAM-MIB", "trillOamMepMandatoryGroup"),
        ("TRILL-OAM-MIB", "trillOamMepFlowCfgTableGroup"),
        ("TRILL-OAM-MIB", "trillOamPtrTableGroup"),
        ("TRILL-OAM-MIB", "trillOamMtvrTableGroup"),
        ("TRILL-OAM-MIB", "trillOamMepDbGroup"),
        ("TRILL-OAM-MIB", "trillOamNotificationGroup"))
)
if mibBuilder.loadTexts:
    trillOamMibCompliance.setStatus(
        "current"
    )

trillOamMibReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 238, 2, 1, 2)
)
trillOamMibReadOnlyCompliance.setObjects(
      *(("TRILL-OAM-MIB", "trillOamMepMandatoryGroup"),
        ("TRILL-OAM-MIB", "trillOamMepFlowCfgTableGroup"),
        ("TRILL-OAM-MIB", "trillOamPtrTableGroup"),
        ("TRILL-OAM-MIB", "trillOamMtvrTableGroup"),
        ("TRILL-OAM-MIB", "trillOamMepDbGroup"),
        ("TRILL-OAM-MIB", "trillOamNotificationGroup"))
)
if mibBuilder.loadTexts:
    trillOamMibReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRILL-OAM-MIB",
    **{"trillOamMib": trillOamMib,
       "trillOamNotifications": trillOamNotifications,
       "trillOamFaultAlarm": trillOamFaultAlarm,
       "trillOamMibObjects": trillOamMibObjects,
       "trillOamMep": trillOamMep,
       "trillOamMepTable": trillOamMepTable,
       "trillOamMepEntry": trillOamMepEntry,
       "trillOamMepRName": trillOamMepRName,
       "trillOamMepNextPtmTId": trillOamMepNextPtmTId,
       "trillOamMepNextMtvmTId": trillOamMepNextMtvmTId,
       "trillOamMepPtrIn": trillOamMepPtrIn,
       "trillOamMepPtrInOutofOrder": trillOamMepPtrInOutofOrder,
       "trillOamMepPtrOut": trillOamMepPtrOut,
       "trillOamMepMtvrIn": trillOamMepMtvrIn,
       "trillOamMepMtvrInOutofOrder": trillOamMepMtvrInOutofOrder,
       "trillOamMepMtvrOut": trillOamMepMtvrOut,
       "trillOamMepTxLbmDestRName": trillOamMepTxLbmDestRName,
       "trillOamMepTxLbmHC": trillOamMepTxLbmHC,
       "trillOamMepTxLbmReplyModeOob": trillOamMepTxLbmReplyModeOob,
       "trillOamMepTransmitLbmReplyIp": trillOamMepTransmitLbmReplyIp,
       "trillOamMepTxLbmFlowEntropy": trillOamMepTxLbmFlowEntropy,
       "trillOamMepTxPtmDestRName": trillOamMepTxPtmDestRName,
       "trillOamMepTxPtmHC": trillOamMepTxPtmHC,
       "trillOamMepTxPtmReplyModeOob": trillOamMepTxPtmReplyModeOob,
       "trillOamMepTransmitPtmReplyIp": trillOamMepTransmitPtmReplyIp,
       "trillOamMepTxPtmFlowEntropy": trillOamMepTxPtmFlowEntropy,
       "trillOamMepTxPtmStatus": trillOamMepTxPtmStatus,
       "trillOamMepTxPtmResultOK": trillOamMepTxPtmResultOK,
       "trillOamMepTxPtmSeqNumber": trillOamMepTxPtmSeqNumber,
       "trillOamMepTxPtmMessages": trillOamMepTxPtmMessages,
       "trillOamMepTxMtvmTree": trillOamMepTxMtvmTree,
       "trillOamMepTxMtvmHC": trillOamMepTxMtvmHC,
       "trillOamMepTxMtvmReplyModeOob": trillOamMepTxMtvmReplyModeOob,
       "trillOamMepTransmitMtvmReplyIp": trillOamMepTransmitMtvmReplyIp,
       "trillOamMepTxMtvmFlowEntropy": trillOamMepTxMtvmFlowEntropy,
       "trillOamMepTxMtvmStatus": trillOamMepTxMtvmStatus,
       "trillOamMepTxMtvmResultOK": trillOamMepTxMtvmResultOK,
       "trillOamMepTxMtvmMessages": trillOamMepTxMtvmMessages,
       "trillOamMepTxMtvmSeqNumber": trillOamMepTxMtvmSeqNumber,
       "trillOamMepTxMtvmScopeList": trillOamMepTxMtvmScopeList,
       "trillOamMepDiscontinuityTime": trillOamMepDiscontinuityTime,
       "trillOamMepFlowCfgTable": trillOamMepFlowCfgTable,
       "trillOamMepFlowCfgEntry": trillOamMepFlowCfgEntry,
       "trillOamMepFlowCfgIndex": trillOamMepFlowCfgIndex,
       "trillOamMepFlowCfgFlowEntropy": trillOamMepFlowCfgFlowEntropy,
       "trillOamMepFlowCfgDestRName": trillOamMepFlowCfgDestRName,
       "trillOamMepFlowCfgFlowHC": trillOamMepFlowCfgFlowHC,
       "trillOamMepFlowCfgRowStatus": trillOamMepFlowCfgRowStatus,
       "trillOamPtrTable": trillOamPtrTable,
       "trillOamPtrEntry": trillOamPtrEntry,
       "trillOamMepPtrTransactionId": trillOamMepPtrTransactionId,
       "trillOamMepPtrHC": trillOamMepPtrHC,
       "trillOamMepPtrFlag": trillOamMepPtrFlag,
       "trillOamMepPtrErrorCode": trillOamMepPtrErrorCode,
       "trillOamMepPtrTerminalMep": trillOamMepPtrTerminalMep,
       "trillOamMepPtrLastEgressId": trillOamMepPtrLastEgressId,
       "trillOamMepPtrIngress": trillOamMepPtrIngress,
       "trillOamMepPtrIngressMac": trillOamMepPtrIngressMac,
       "trillOamMepPtrIngressPortIdSubtype": trillOamMepPtrIngressPortIdSubtype,
       "trillOamMepPtrIngressPortId": trillOamMepPtrIngressPortId,
       "trillOamMepPtrEgress": trillOamMepPtrEgress,
       "trillOamMepPtrEgressMac": trillOamMepPtrEgressMac,
       "trillOamMepPtrEgressPortIdSubtype": trillOamMepPtrEgressPortIdSubtype,
       "trillOamMepPtrEgressPortId": trillOamMepPtrEgressPortId,
       "trillOamMepPtrChassisIdSubtype": trillOamMepPtrChassisIdSubtype,
       "trillOamMepPtrChassisId": trillOamMepPtrChassisId,
       "trillOamMepPtrOrganizationSpecificTlv": trillOamMepPtrOrganizationSpecificTlv,
       "trillOamMepPtrNextHopNicknames": trillOamMepPtrNextHopNicknames,
       "trillOamMtvrTable": trillOamMtvrTable,
       "trillOamMtvrEntry": trillOamMtvrEntry,
       "trillOamMepMtvrTransactionId": trillOamMepMtvrTransactionId,
       "trillOamMepMtvrReceiveOrder": trillOamMepMtvrReceiveOrder,
       "trillOamMepMtvrFlag": trillOamMepMtvrFlag,
       "trillOamMepMtvrErrorCode": trillOamMepMtvrErrorCode,
       "trillOamMepMtvrLastEgressId": trillOamMepMtvrLastEgressId,
       "trillOamMepMtvrIngress": trillOamMepMtvrIngress,
       "trillOamMepMtvrIngressMac": trillOamMepMtvrIngressMac,
       "trillOamMepMtvrIngressPortIdSubtype": trillOamMepMtvrIngressPortIdSubtype,
       "trillOamMepMtvrIngressPortId": trillOamMepMtvrIngressPortId,
       "trillOamMepMtvrEgress": trillOamMepMtvrEgress,
       "trillOamMepMtvrEgressMac": trillOamMepMtvrEgressMac,
       "trillOamMepMtvrEgressPortIdSubtype": trillOamMepMtvrEgressPortIdSubtype,
       "trillOamMepMtvrEgressPortId": trillOamMepMtvrEgressPortId,
       "trillOamMepMtvrChassisIdSubtype": trillOamMepMtvrChassisIdSubtype,
       "trillOamMepMtvrChassisId": trillOamMepMtvrChassisId,
       "trillOamMepMtvrOrganizationSpecificTlv": trillOamMepMtvrOrganizationSpecificTlv,
       "trillOamMepMtvrNextHopNicknames": trillOamMepMtvrNextHopNicknames,
       "trillOamMepMtvrReceiverAvailability": trillOamMepMtvrReceiverAvailability,
       "trillOamMepMtvrReceiverCount": trillOamMepMtvrReceiverCount,
       "trillOamMepDbTable": trillOamMepDbTable,
       "trillOamMepDbEntry": trillOamMepDbEntry,
       "trillOamMepDbFlowIndex": trillOamMepDbFlowIndex,
       "trillOamMepDbFlowEntropy": trillOamMepDbFlowEntropy,
       "trillOamMepDbFlowState": trillOamMepDbFlowState,
       "trillOamMepDbFlowFailedOkTime": trillOamMepDbFlowFailedOkTime,
       "trillOamMepDbRBridgeName": trillOamMepDbRBridgeName,
       "trillOamMepDbLastGoodSeqNum": trillOamMepDbLastGoodSeqNum,
       "trillOamMibConformance": trillOamMibConformance,
       "trillOamMibCompliances": trillOamMibCompliances,
       "trillOamMibCompliance": trillOamMibCompliance,
       "trillOamMibReadOnlyCompliance": trillOamMibReadOnlyCompliance,
       "trillOamMibGroups": trillOamMibGroups,
       "trillOamMepMandatoryGroup": trillOamMepMandatoryGroup,
       "trillOamMepFlowCfgTableGroup": trillOamMepFlowCfgTableGroup,
       "trillOamPtrTableGroup": trillOamPtrTableGroup,
       "trillOamMtvrTableGroup": trillOamMtvrTableGroup,
       "trillOamMepDbGroup": trillOamMepDbGroup,
       "trillOamNotificationGroup": trillOamNotificationGroup}
)
