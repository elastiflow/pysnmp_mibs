# SNMP MIB module (ECONAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/rdp_45555/ECONAT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:50 2025
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

(dot1dBasePort,
 dot1dBasePortEntry,
 dot1dBridge) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort",
    "dot1dBasePortEntry",
    "dot1dBridge")

(DisplayString,) = mibBuilder.importSymbols(
    "RFC-1213",
    "DisplayString")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rdp_ObjectIdentity = ObjectIdentity
rdp = _Rdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45555)
)
_Econat_ObjectIdentity = ObjectIdentity
econat = _Econat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45555, 1)
)
_Counters_ObjectIdentity = ObjectIdentity
counters = _Counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2)
)
_EconatGaddrAlloc_Type = DisplayString
_EconatGaddrAlloc_Object = MibScalar
econatGaddrAlloc = _EconatGaddrAlloc_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 1),
    _EconatGaddrAlloc_Type()
)
econatGaddrAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatGaddrAlloc.setStatus("mandatory")
_EconatGaddrFree_Type = DisplayString
_EconatGaddrFree_Object = MibScalar
econatGaddrFree = _EconatGaddrFree_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 2),
    _EconatGaddrFree_Type()
)
econatGaddrFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatGaddrFree.setStatus("mandatory")
_EconatPortBlockAlloc_Type = DisplayString
_EconatPortBlockAlloc_Object = MibScalar
econatPortBlockAlloc = _EconatPortBlockAlloc_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 3),
    _EconatPortBlockAlloc_Type()
)
econatPortBlockAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatPortBlockAlloc.setStatus("mandatory")
_EconatPortBlockFree_Type = DisplayString
_EconatPortBlockFree_Object = MibScalar
econatPortBlockFree = _EconatPortBlockFree_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 4),
    _EconatPortBlockFree_Type()
)
econatPortBlockFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatPortBlockFree.setStatus("mandatory")
_EconatPortAlloc_Type = DisplayString
_EconatPortAlloc_Object = MibScalar
econatPortAlloc = _EconatPortAlloc_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 5),
    _EconatPortAlloc_Type()
)
econatPortAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatPortAlloc.setStatus("mandatory")
_EconatPortFree_Type = DisplayString
_EconatPortFree_Object = MibScalar
econatPortFree = _EconatPortFree_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 6),
    _EconatPortFree_Type()
)
econatPortFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatPortFree.setStatus("mandatory")
_EconatSessionAlloc_Type = DisplayString
_EconatSessionAlloc_Object = MibScalar
econatSessionAlloc = _EconatSessionAlloc_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 7),
    _EconatSessionAlloc_Type()
)
econatSessionAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAlloc.setStatus("mandatory")
_EconatSessionFree_Type = DisplayString
_EconatSessionFree_Object = MibScalar
econatSessionFree = _EconatSessionFree_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 8),
    _EconatSessionFree_Type()
)
econatSessionFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionFree.setStatus("mandatory")
_EconatSessionAllocErrorEgress_Type = DisplayString
_EconatSessionAllocErrorEgress_Object = MibScalar
econatSessionAllocErrorEgress = _EconatSessionAllocErrorEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 9),
    _EconatSessionAllocErrorEgress_Type()
)
econatSessionAllocErrorEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocErrorEgress.setStatus("mandatory")
_EconatSessionAllocErrorIngress_Type = DisplayString
_EconatSessionAllocErrorIngress_Object = MibScalar
econatSessionAllocErrorIngress = _EconatSessionAllocErrorIngress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 10),
    _EconatSessionAllocErrorIngress_Type()
)
econatSessionAllocErrorIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocErrorIngress.setStatus("mandatory")
_EconatTranslationAllocError_Type = DisplayString
_EconatTranslationAllocError_Object = MibScalar
econatTranslationAllocError = _EconatTranslationAllocError_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 11),
    _EconatTranslationAllocError_Type()
)
econatTranslationAllocError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTranslationAllocError.setStatus("mandatory")
_EconatSessionFreeError_Type = DisplayString
_EconatSessionFreeError_Object = MibScalar
econatSessionFreeError = _EconatSessionFreeError_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 12),
    _EconatSessionFreeError_Type()
)
econatSessionFreeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionFreeError.setStatus("mandatory")
_EconatLoggedMessages_Type = DisplayString
_EconatLoggedMessages_Object = MibScalar
econatLoggedMessages = _EconatLoggedMessages_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 13),
    _EconatLoggedMessages_Type()
)
econatLoggedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatLoggedMessages.setStatus("mandatory")
_EconatDroppedMessages_Type = DisplayString
_EconatDroppedMessages_Object = MibScalar
econatDroppedMessages = _EconatDroppedMessages_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 14),
    _EconatDroppedMessages_Type()
)
econatDroppedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDroppedMessages.setStatus("mandatory")
_EconatAvgEgressRxQueue_Type = DisplayString
_EconatAvgEgressRxQueue_Object = MibScalar
econatAvgEgressRxQueue = _EconatAvgEgressRxQueue_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 15),
    _EconatAvgEgressRxQueue_Type()
)
econatAvgEgressRxQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAvgEgressRxQueue.setStatus("mandatory")
_EconatAvgIngressRxQueue_Type = DisplayString
_EconatAvgIngressRxQueue_Object = MibScalar
econatAvgIngressRxQueue = _EconatAvgIngressRxQueue_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 16),
    _EconatAvgIngressRxQueue_Type()
)
econatAvgIngressRxQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAvgIngressRxQueue.setStatus("mandatory")
_EconatEgressRxQueueVoid_Type = DisplayString
_EconatEgressRxQueueVoid_Object = MibScalar
econatEgressRxQueueVoid = _EconatEgressRxQueueVoid_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 17),
    _EconatEgressRxQueueVoid_Type()
)
econatEgressRxQueueVoid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatEgressRxQueueVoid.setStatus("mandatory")
_EconatEgressRxQueueMedium_Type = DisplayString
_EconatEgressRxQueueMedium_Object = MibScalar
econatEgressRxQueueMedium = _EconatEgressRxQueueMedium_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 18),
    _EconatEgressRxQueueMedium_Type()
)
econatEgressRxQueueMedium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatEgressRxQueueMedium.setStatus("mandatory")
_EconatEgressRxQueueOverflow_Type = DisplayString
_EconatEgressRxQueueOverflow_Object = MibScalar
econatEgressRxQueueOverflow = _EconatEgressRxQueueOverflow_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 19),
    _EconatEgressRxQueueOverflow_Type()
)
econatEgressRxQueueOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatEgressRxQueueOverflow.setStatus("mandatory")
_EconatIngressRxQueueVoid_Type = DisplayString
_EconatIngressRxQueueVoid_Object = MibScalar
econatIngressRxQueueVoid = _EconatIngressRxQueueVoid_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 20),
    _EconatIngressRxQueueVoid_Type()
)
econatIngressRxQueueVoid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatIngressRxQueueVoid.setStatus("mandatory")
_EconatIngressRxQueueMedium_Type = DisplayString
_EconatIngressRxQueueMedium_Object = MibScalar
econatIngressRxQueueMedium = _EconatIngressRxQueueMedium_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 21),
    _EconatIngressRxQueueMedium_Type()
)
econatIngressRxQueueMedium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatIngressRxQueueMedium.setStatus("mandatory")
_EconatIngressRxQueueOverflow_Type = DisplayString
_EconatIngressRxQueueOverflow_Object = MibScalar
econatIngressRxQueueOverflow = _EconatIngressRxQueueOverflow_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 22),
    _EconatIngressRxQueueOverflow_Type()
)
econatIngressRxQueueOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatIngressRxQueueOverflow.setStatus("mandatory")
_EconatDispFreeMbufs0_Type = DisplayString
_EconatDispFreeMbufs0_Object = MibScalar
econatDispFreeMbufs0 = _EconatDispFreeMbufs0_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 23),
    _EconatDispFreeMbufs0_Type()
)
econatDispFreeMbufs0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDispFreeMbufs0.setStatus("mandatory")
_EconatDispFreeMbufs1_Type = DisplayString
_EconatDispFreeMbufs1_Object = MibScalar
econatDispFreeMbufs1 = _EconatDispFreeMbufs1_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 24),
    _EconatDispFreeMbufs1_Type()
)
econatDispFreeMbufs1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDispFreeMbufs1.setStatus("mandatory")
_EconatAvgConnRequestsPerBurst_Type = DisplayString
_EconatAvgConnRequestsPerBurst_Object = MibScalar
econatAvgConnRequestsPerBurst = _EconatAvgConnRequestsPerBurst_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 25),
    _EconatAvgConnRequestsPerBurst_Type()
)
econatAvgConnRequestsPerBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAvgConnRequestsPerBurst.setStatus("mandatory")
_EconatAvgConnRequestsPerNonEmptyBurst_Type = DisplayString
_EconatAvgConnRequestsPerNonEmptyBurst_Object = MibScalar
econatAvgConnRequestsPerNonEmptyBurst = _EconatAvgConnRequestsPerNonEmptyBurst_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 26),
    _EconatAvgConnRequestsPerNonEmptyBurst_Type()
)
econatAvgConnRequestsPerNonEmptyBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAvgConnRequestsPerNonEmptyBurst.setStatus("mandatory")
_EconatConnRingVoid_Type = DisplayString
_EconatConnRingVoid_Object = MibScalar
econatConnRingVoid = _EconatConnRingVoid_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 27),
    _EconatConnRingVoid_Type()
)
econatConnRingVoid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatConnRingVoid.setStatus("mandatory")
_EconatConnRingMedium_Type = DisplayString
_EconatConnRingMedium_Object = MibScalar
econatConnRingMedium = _EconatConnRingMedium_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 28),
    _EconatConnRingMedium_Type()
)
econatConnRingMedium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatConnRingMedium.setStatus("mandatory")
_EconatConnRingPostponed_Type = DisplayString
_EconatConnRingPostponed_Object = MibScalar
econatConnRingPostponed = _EconatConnRingPostponed_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 29),
    _EconatConnRingPostponed_Type()
)
econatConnRingPostponed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatConnRingPostponed.setStatus("mandatory")
_EconatConnRingOverflow_Type = DisplayString
_EconatConnRingOverflow_Object = MibScalar
econatConnRingOverflow = _EconatConnRingOverflow_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 30),
    _EconatConnRingOverflow_Type()
)
econatConnRingOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatConnRingOverflow.setStatus("mandatory")
_EconatRacePrevented1_Type = DisplayString
_EconatRacePrevented1_Object = MibScalar
econatRacePrevented1 = _EconatRacePrevented1_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 32),
    _EconatRacePrevented1_Type()
)
econatRacePrevented1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatRacePrevented1.setStatus("mandatory")
_EconatRacePrevented2_Type = DisplayString
_EconatRacePrevented2_Object = MibScalar
econatRacePrevented2 = _EconatRacePrevented2_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 33),
    _EconatRacePrevented2_Type()
)
econatRacePrevented2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatRacePrevented2.setStatus("mandatory")
_EconatRacePrevented3_Type = DisplayString
_EconatRacePrevented3_Object = MibScalar
econatRacePrevented3 = _EconatRacePrevented3_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 34),
    _EconatRacePrevented3_Type()
)
econatRacePrevented3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatRacePrevented3.setStatus("mandatory")
_EconatIpDropUnknownProto_Type = DisplayString
_EconatIpDropUnknownProto_Object = MibScalar
econatIpDropUnknownProto = _EconatIpDropUnknownProto_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 40),
    _EconatIpDropUnknownProto_Type()
)
econatIpDropUnknownProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatIpDropUnknownProto.setStatus("mandatory")
_EconatIpPassUnknownProto_Type = DisplayString
_EconatIpPassUnknownProto_Object = MibScalar
econatIpPassUnknownProto = _EconatIpPassUnknownProto_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 41),
    _EconatIpPassUnknownProto_Type()
)
econatIpPassUnknownProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatIpPassUnknownProto.setStatus("mandatory")
_EconatIpDropOpaqueProto_Type = DisplayString
_EconatIpDropOpaqueProto_Object = MibScalar
econatIpDropOpaqueProto = _EconatIpDropOpaqueProto_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 42),
    _EconatIpDropOpaqueProto_Type()
)
econatIpDropOpaqueProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatIpDropOpaqueProto.setStatus("mandatory")
_EconatIpPassOpaqueProto_Type = DisplayString
_EconatIpPassOpaqueProto_Object = MibScalar
econatIpPassOpaqueProto = _EconatIpPassOpaqueProto_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 43),
    _EconatIpPassOpaqueProto_Type()
)
econatIpPassOpaqueProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatIpPassOpaqueProto.setStatus("mandatory")
_EconatTranslatedOpaque_Type = DisplayString
_EconatTranslatedOpaque_Object = MibScalar
econatTranslatedOpaque = _EconatTranslatedOpaque_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 44),
    _EconatTranslatedOpaque_Type()
)
econatTranslatedOpaque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTranslatedOpaque.setStatus("mandatory")
_EconatInOpaqueError_Type = DisplayString
_EconatInOpaqueError_Object = MibScalar
econatInOpaqueError = _EconatInOpaqueError_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 45),
    _EconatInOpaqueError_Type()
)
econatInOpaqueError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatInOpaqueError.setStatus("mandatory")
_EconatEgressOpaqueNoPool_Type = DisplayString
_EconatEgressOpaqueNoPool_Object = MibScalar
econatEgressOpaqueNoPool = _EconatEgressOpaqueNoPool_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 46),
    _EconatEgressOpaqueNoPool_Type()
)
econatEgressOpaqueNoPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatEgressOpaqueNoPool.setStatus("mandatory")
_EconatIngressOpaqueNoPool_Type = DisplayString
_EconatIngressOpaqueNoPool_Object = MibScalar
econatIngressOpaqueNoPool = _EconatIngressOpaqueNoPool_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 47),
    _EconatIngressOpaqueNoPool_Type()
)
econatIngressOpaqueNoPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatIngressOpaqueNoPool.setStatus("mandatory")
_EconatSessionAllocNoPoolEgress_Type = DisplayString
_EconatSessionAllocNoPoolEgress_Object = MibScalar
econatSessionAllocNoPoolEgress = _EconatSessionAllocNoPoolEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 50),
    _EconatSessionAllocNoPoolEgress_Type()
)
econatSessionAllocNoPoolEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocNoPoolEgress.setStatus("mandatory")
_EconatSessionAllocNoPoolIngress_Type = DisplayString
_EconatSessionAllocNoPoolIngress_Object = MibScalar
econatSessionAllocNoPoolIngress = _EconatSessionAllocNoPoolIngress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 51),
    _EconatSessionAllocNoPoolIngress_Type()
)
econatSessionAllocNoPoolIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocNoPoolIngress.setStatus("mandatory")
_EconatAvgEgressConnRequests_Type = DisplayString
_EconatAvgEgressConnRequests_Object = MibScalar
econatAvgEgressConnRequests = _EconatAvgEgressConnRequests_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 55),
    _EconatAvgEgressConnRequests_Type()
)
econatAvgEgressConnRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAvgEgressConnRequests.setStatus("mandatory")
_EconatAvgIngressConnRequests_Type = DisplayString
_EconatAvgIngressConnRequests_Object = MibScalar
econatAvgIngressConnRequests = _EconatAvgIngressConnRequests_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 56),
    _EconatAvgIngressConnRequests_Type()
)
econatAvgIngressConnRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAvgIngressConnRequests.setStatus("mandatory")
_EconatAvgEgressConnsCreated_Type = DisplayString
_EconatAvgEgressConnsCreated_Object = MibScalar
econatAvgEgressConnsCreated = _EconatAvgEgressConnsCreated_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 57),
    _EconatAvgEgressConnsCreated_Type()
)
econatAvgEgressConnsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAvgEgressConnsCreated.setStatus("mandatory")
_EconatAvgIngressConnsCreated_Type = DisplayString
_EconatAvgIngressConnsCreated_Object = MibScalar
econatAvgIngressConnsCreated = _EconatAvgIngressConnsCreated_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 58),
    _EconatAvgIngressConnsCreated_Type()
)
econatAvgIngressConnsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAvgIngressConnsCreated.setStatus("mandatory")
_EconatUsedNaptPortBlocks_Type = DisplayString
_EconatUsedNaptPortBlocks_Object = MibScalar
econatUsedNaptPortBlocks = _EconatUsedNaptPortBlocks_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 59),
    _EconatUsedNaptPortBlocks_Type()
)
econatUsedNaptPortBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatUsedNaptPortBlocks.setStatus("mandatory")
_EconatUsedNaptPorts_Type = DisplayString
_EconatUsedNaptPorts_Object = MibScalar
econatUsedNaptPorts = _EconatUsedNaptPorts_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 60),
    _EconatUsedNaptPorts_Type()
)
econatUsedNaptPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatUsedNaptPorts.setStatus("mandatory")
_Poolsinfo_ObjectIdentity = ObjectIdentity
poolsinfo = _Poolsinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61)
)
_Poolid_ObjectIdentity = ObjectIdentity
poolid = _Poolid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0)
)
_EconatNaptTotalAddresses_Type = DisplayString
_EconatNaptTotalAddresses_Object = MibScalar
econatNaptTotalAddresses = _EconatNaptTotalAddresses_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 3),
    _EconatNaptTotalAddresses_Type()
)
econatNaptTotalAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatNaptTotalAddresses.setStatus("mandatory")
_EconatNaptUsedAddress_Type = DisplayString
_EconatNaptUsedAddress_Object = MibScalar
econatNaptUsedAddress = _EconatNaptUsedAddress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 4),
    _EconatNaptUsedAddress_Type()
)
econatNaptUsedAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatNaptUsedAddress.setStatus("mandatory")
_EconatNaptUnusedAddresses_Type = DisplayString
_EconatNaptUnusedAddresses_Object = MibScalar
econatNaptUnusedAddresses = _EconatNaptUnusedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 5),
    _EconatNaptUnusedAddresses_Type()
)
econatNaptUnusedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatNaptUnusedAddresses.setStatus("mandatory")
_EconatNaptTotalPortsTcp_Type = DisplayString
_EconatNaptTotalPortsTcp_Object = MibScalar
econatNaptTotalPortsTcp = _EconatNaptTotalPortsTcp_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 6),
    _EconatNaptTotalPortsTcp_Type()
)
econatNaptTotalPortsTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatNaptTotalPortsTcp.setStatus("mandatory")
_EconatNaptTotalPortsUdp_Type = DisplayString
_EconatNaptTotalPortsUdp_Object = MibScalar
econatNaptTotalPortsUdp = _EconatNaptTotalPortsUdp_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 7),
    _EconatNaptTotalPortsUdp_Type()
)
econatNaptTotalPortsUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatNaptTotalPortsUdp.setStatus("mandatory")
_EconatNaptTotalPortsIcmp_Type = DisplayString
_EconatNaptTotalPortsIcmp_Object = MibScalar
econatNaptTotalPortsIcmp = _EconatNaptTotalPortsIcmp_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 8),
    _EconatNaptTotalPortsIcmp_Type()
)
econatNaptTotalPortsIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatNaptTotalPortsIcmp.setStatus("mandatory")
_EconatNaptUsedPortsTcp_Type = DisplayString
_EconatNaptUsedPortsTcp_Object = MibScalar
econatNaptUsedPortsTcp = _EconatNaptUsedPortsTcp_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 9),
    _EconatNaptUsedPortsTcp_Type()
)
econatNaptUsedPortsTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatNaptUsedPortsTcp.setStatus("mandatory")
_EconatNaptUsedPortsUdp_Type = DisplayString
_EconatNaptUsedPortsUdp_Object = MibScalar
econatNaptUsedPortsUdp = _EconatNaptUsedPortsUdp_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 10),
    _EconatNaptUsedPortsUdp_Type()
)
econatNaptUsedPortsUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatNaptUsedPortsUdp.setStatus("mandatory")
_EconatNaptUsedPortsIcmp_Type = DisplayString
_EconatNaptUsedPortsIcmp_Object = MibScalar
econatNaptUsedPortsIcmp = _EconatNaptUsedPortsIcmp_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 11),
    _EconatNaptUsedPortsIcmp_Type()
)
econatNaptUsedPortsIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatNaptUsedPortsIcmp.setStatus("mandatory")
_EconatBnatTotalAddresses_Type = DisplayString
_EconatBnatTotalAddresses_Object = MibScalar
econatBnatTotalAddresses = _EconatBnatTotalAddresses_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 12),
    _EconatBnatTotalAddresses_Type()
)
econatBnatTotalAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatTotalAddresses.setStatus("mandatory")
_EconatBnatStaticAddresses_Type = DisplayString
_EconatBnatStaticAddresses_Object = MibScalar
econatBnatStaticAddresses = _EconatBnatStaticAddresses_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 13),
    _EconatBnatStaticAddresses_Type()
)
econatBnatStaticAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatStaticAddresses.setStatus("mandatory")
_EconatBnatUsedAddresses_Type = DisplayString
_EconatBnatUsedAddresses_Object = MibScalar
econatBnatUsedAddresses = _EconatBnatUsedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 14),
    _EconatBnatUsedAddresses_Type()
)
econatBnatUsedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatUsedAddresses.setStatus("mandatory")
_EconatBnatUnusedAddresses_Type = DisplayString
_EconatBnatUnusedAddresses_Object = MibScalar
econatBnatUnusedAddresses = _EconatBnatUnusedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 15),
    _EconatBnatUnusedAddresses_Type()
)
econatBnatUnusedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatUnusedAddresses.setStatus("mandatory")
_EconatBnatConnectionsTcpIngress_Type = DisplayString
_EconatBnatConnectionsTcpIngress_Object = MibScalar
econatBnatConnectionsTcpIngress = _EconatBnatConnectionsTcpIngress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 16),
    _EconatBnatConnectionsTcpIngress_Type()
)
econatBnatConnectionsTcpIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatConnectionsTcpIngress.setStatus("mandatory")
_EconatBnatConnectionsUdpIngress_Type = DisplayString
_EconatBnatConnectionsUdpIngress_Object = MibScalar
econatBnatConnectionsUdpIngress = _EconatBnatConnectionsUdpIngress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 17),
    _EconatBnatConnectionsUdpIngress_Type()
)
econatBnatConnectionsUdpIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatConnectionsUdpIngress.setStatus("mandatory")
_EconatBnatConnectionsIcmpIngress_Type = DisplayString
_EconatBnatConnectionsIcmpIngress_Object = MibScalar
econatBnatConnectionsIcmpIngress = _EconatBnatConnectionsIcmpIngress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 18),
    _EconatBnatConnectionsIcmpIngress_Type()
)
econatBnatConnectionsIcmpIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatConnectionsIcmpIngress.setStatus("mandatory")
_EconatBnatConnectionsOtherIngress_Type = DisplayString
_EconatBnatConnectionsOtherIngress_Object = MibScalar
econatBnatConnectionsOtherIngress = _EconatBnatConnectionsOtherIngress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 19),
    _EconatBnatConnectionsOtherIngress_Type()
)
econatBnatConnectionsOtherIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatConnectionsOtherIngress.setStatus("mandatory")
_EconatBnatConnectionsTcpEgress_Type = DisplayString
_EconatBnatConnectionsTcpEgress_Object = MibScalar
econatBnatConnectionsTcpEgress = _EconatBnatConnectionsTcpEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 20),
    _EconatBnatConnectionsTcpEgress_Type()
)
econatBnatConnectionsTcpEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatConnectionsTcpEgress.setStatus("mandatory")
_EconatBnatConnectionsUdpEgress_Type = DisplayString
_EconatBnatConnectionsUdpEgress_Object = MibScalar
econatBnatConnectionsUdpEgress = _EconatBnatConnectionsUdpEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 21),
    _EconatBnatConnectionsUdpEgress_Type()
)
econatBnatConnectionsUdpEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatConnectionsUdpEgress.setStatus("mandatory")
_EconatBnatConnectionsIcmpEgress_Type = DisplayString
_EconatBnatConnectionsIcmpEgress_Object = MibScalar
econatBnatConnectionsIcmpEgress = _EconatBnatConnectionsIcmpEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 22),
    _EconatBnatConnectionsIcmpEgress_Type()
)
econatBnatConnectionsIcmpEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatConnectionsIcmpEgress.setStatus("mandatory")
_EconatBnatConnectionsOtherEgress_Type = DisplayString
_EconatBnatConnectionsOtherEgress_Object = MibScalar
econatBnatConnectionsOtherEgress = _EconatBnatConnectionsOtherEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 23),
    _EconatBnatConnectionsOtherEgress_Type()
)
econatBnatConnectionsOtherEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatConnectionsOtherEgress.setStatus("mandatory")
_EconatBnatConnectionsTcp_Type = DisplayString
_EconatBnatConnectionsTcp_Object = MibScalar
econatBnatConnectionsTcp = _EconatBnatConnectionsTcp_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 24),
    _EconatBnatConnectionsTcp_Type()
)
econatBnatConnectionsTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatConnectionsTcp.setStatus("mandatory")
_EconatBnatConnectionsUdp_Type = DisplayString
_EconatBnatConnectionsUdp_Object = MibScalar
econatBnatConnectionsUdp = _EconatBnatConnectionsUdp_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 25),
    _EconatBnatConnectionsUdp_Type()
)
econatBnatConnectionsUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatConnectionsUdp.setStatus("mandatory")
_EconatBnatConnectionsIcmp_Type = DisplayString
_EconatBnatConnectionsIcmp_Object = MibScalar
econatBnatConnectionsIcmp = _EconatBnatConnectionsIcmp_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 26),
    _EconatBnatConnectionsIcmp_Type()
)
econatBnatConnectionsIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatConnectionsIcmp.setStatus("mandatory")
_EconatBnatConnectionsOther_Type = DisplayString
_EconatBnatConnectionsOther_Object = MibScalar
econatBnatConnectionsOther = _EconatBnatConnectionsOther_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 61, 0, 27),
    _EconatBnatConnectionsOther_Type()
)
econatBnatConnectionsOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatConnectionsOther.setStatus("mandatory")
_EconatTcpSessions_Type = DisplayString
_EconatTcpSessions_Object = MibScalar
econatTcpSessions = _EconatTcpSessions_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 62),
    _EconatTcpSessions_Type()
)
econatTcpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTcpSessions.setStatus("mandatory")
_EconatAproxSessionLimit_Type = DisplayString
_EconatAproxSessionLimit_Object = MibScalar
econatAproxSessionLimit = _EconatAproxSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 63),
    _EconatAproxSessionLimit_Type()
)
econatAproxSessionLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAproxSessionLimit.setStatus("mandatory")
_EconatUdpSessions_Type = DisplayString
_EconatUdpSessions_Object = MibScalar
econatUdpSessions = _EconatUdpSessions_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 64),
    _EconatUdpSessions_Type()
)
econatUdpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatUdpSessions.setStatus("mandatory")
_EconatAproxSessionLimit2_Type = DisplayString
_EconatAproxSessionLimit2_Object = MibScalar
econatAproxSessionLimit2 = _EconatAproxSessionLimit2_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 65),
    _EconatAproxSessionLimit2_Type()
)
econatAproxSessionLimit2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAproxSessionLimit2.setStatus("mandatory")
_EconatIcmpSessions_Type = DisplayString
_EconatIcmpSessions_Object = MibScalar
econatIcmpSessions = _EconatIcmpSessions_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 66),
    _EconatIcmpSessions_Type()
)
econatIcmpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatIcmpSessions.setStatus("mandatory")
_EconatAproxSessionLimit3_Type = DisplayString
_EconatAproxSessionLimit3_Object = MibScalar
econatAproxSessionLimit3 = _EconatAproxSessionLimit3_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 67),
    _EconatAproxSessionLimit3_Type()
)
econatAproxSessionLimit3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAproxSessionLimit3.setStatus("mandatory")
_EconatDpCpuBurst_Type = DisplayString
_EconatDpCpuBurst_Object = MibScalar
econatDpCpuBurst = _EconatDpCpuBurst_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 105),
    _EconatDpCpuBurst_Type()
)
econatDpCpuBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDpCpuBurst.setStatus("mandatory")
_EconatDpTotalMemory_Type = DisplayString
_EconatDpTotalMemory_Object = MibScalar
econatDpTotalMemory = _EconatDpTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 106),
    _EconatDpTotalMemory_Type()
)
econatDpTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDpTotalMemory.setStatus("mandatory")
_EconatDpFreeMemory_Type = DisplayString
_EconatDpFreeMemory_Object = MibScalar
econatDpFreeMemory = _EconatDpFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 107),
    _EconatDpFreeMemory_Type()
)
econatDpFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDpFreeMemory.setStatus("mandatory")
_EconatCpTotalMemory_Type = DisplayString
_EconatCpTotalMemory_Object = MibScalar
econatCpTotalMemory = _EconatCpTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 108),
    _EconatCpTotalMemory_Type()
)
econatCpTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatCpTotalMemory.setStatus("mandatory")
_EconatCpFreeMemory_Type = DisplayString
_EconatCpFreeMemory_Object = MibScalar
econatCpFreeMemory = _EconatCpFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 109),
    _EconatCpFreeMemory_Type()
)
econatCpFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatCpFreeMemory.setStatus("mandatory")
_EconatDpCpuSocket0_Type = DisplayString
_EconatDpCpuSocket0_Object = MibScalar
econatDpCpuSocket0 = _EconatDpCpuSocket0_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 110),
    _EconatDpCpuSocket0_Type()
)
econatDpCpuSocket0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDpCpuSocket0.setStatus("mandatory")
_EconatDpCpuSocket1_Type = DisplayString
_EconatDpCpuSocket1_Object = MibScalar
econatDpCpuSocket1 = _EconatDpCpuSocket1_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 111),
    _EconatDpCpuSocket1_Type()
)
econatDpCpuSocket1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDpCpuSocket1.setStatus("mandatory")
_EconatAvgEgressRxQueueSocket0_Type = DisplayString
_EconatAvgEgressRxQueueSocket0_Object = MibScalar
econatAvgEgressRxQueueSocket0 = _EconatAvgEgressRxQueueSocket0_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 112),
    _EconatAvgEgressRxQueueSocket0_Type()
)
econatAvgEgressRxQueueSocket0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAvgEgressRxQueueSocket0.setStatus("mandatory")
_EconatAvgIngressRxQueueSocket0_Type = DisplayString
_EconatAvgIngressRxQueueSocket0_Object = MibScalar
econatAvgIngressRxQueueSocket0 = _EconatAvgIngressRxQueueSocket0_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 113),
    _EconatAvgIngressRxQueueSocket0_Type()
)
econatAvgIngressRxQueueSocket0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAvgIngressRxQueueSocket0.setStatus("mandatory")
_EconatAvgEgressRxQueueSocket1_Type = DisplayString
_EconatAvgEgressRxQueueSocket1_Object = MibScalar
econatAvgEgressRxQueueSocket1 = _EconatAvgEgressRxQueueSocket1_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 114),
    _EconatAvgEgressRxQueueSocket1_Type()
)
econatAvgEgressRxQueueSocket1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAvgEgressRxQueueSocket1.setStatus("mandatory")
_EconatAvgIngressRxQueueSocket1_Type = DisplayString
_EconatAvgIngressRxQueueSocket1_Object = MibScalar
econatAvgIngressRxQueueSocket1 = _EconatAvgIngressRxQueueSocket1_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 115),
    _EconatAvgIngressRxQueueSocket1_Type()
)
econatAvgIngressRxQueueSocket1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAvgIngressRxQueueSocket1.setStatus("mandatory")
_EconatAvgEgressRxQueueSocketBoth_Type = DisplayString
_EconatAvgEgressRxQueueSocketBoth_Object = MibScalar
econatAvgEgressRxQueueSocketBoth = _EconatAvgEgressRxQueueSocketBoth_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 116),
    _EconatAvgEgressRxQueueSocketBoth_Type()
)
econatAvgEgressRxQueueSocketBoth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAvgEgressRxQueueSocketBoth.setStatus("mandatory")
_EconatAvgIngressRxQueueSocketBoth_Type = DisplayString
_EconatAvgIngressRxQueueSocketBoth_Object = MibScalar
econatAvgIngressRxQueueSocketBoth = _EconatAvgIngressRxQueueSocketBoth_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 117),
    _EconatAvgIngressRxQueueSocketBoth_Type()
)
econatAvgIngressRxQueueSocketBoth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAvgIngressRxQueueSocketBoth.setStatus("mandatory")
_EconatFreeLoggingMbufs_Type = DisplayString
_EconatFreeLoggingMbufs_Object = MibScalar
econatFreeLoggingMbufs = _EconatFreeLoggingMbufs_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 120),
    _EconatFreeLoggingMbufs_Type()
)
econatFreeLoggingMbufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatFreeLoggingMbufs.setStatus("mandatory")
_EconatCntReconfigs_Type = DisplayString
_EconatCntReconfigs_Object = MibScalar
econatCntReconfigs = _EconatCntReconfigs_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 121),
    _EconatCntReconfigs_Type()
)
econatCntReconfigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatCntReconfigs.setStatus("mandatory")
_EconatDroppedClonedMessages_Type = DisplayString
_EconatDroppedClonedMessages_Object = MibScalar
econatDroppedClonedMessages = _EconatDroppedClonedMessages_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 125),
    _EconatDroppedClonedMessages_Type()
)
econatDroppedClonedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDroppedClonedMessages.setStatus("mandatory")
_EconatDroppedLoggerMbufs_Type = DisplayString
_EconatDroppedLoggerMbufs_Object = MibScalar
econatDroppedLoggerMbufs = _EconatDroppedLoggerMbufs_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 126),
    _EconatDroppedLoggerMbufs_Type()
)
econatDroppedLoggerMbufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDroppedLoggerMbufs.setStatus("mandatory")
_EconatRolledQueues_Type = DisplayString
_EconatRolledQueues_Object = MibScalar
econatRolledQueues = _EconatRolledQueues_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 127),
    _EconatRolledQueues_Type()
)
econatRolledQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatRolledQueues.setStatus("mandatory")
_EconatAlgSessionAlloc_Type = DisplayString
_EconatAlgSessionAlloc_Object = MibScalar
econatAlgSessionAlloc = _EconatAlgSessionAlloc_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 130),
    _EconatAlgSessionAlloc_Type()
)
econatAlgSessionAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAlgSessionAlloc.setStatus("mandatory")
_EconatAlgSessionFree_Type = DisplayString
_EconatAlgSessionFree_Object = MibScalar
econatAlgSessionFree = _EconatAlgSessionFree_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 131),
    _EconatAlgSessionFree_Type()
)
econatAlgSessionFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAlgSessionFree.setStatus("mandatory")
_EconatAlgSessionAllocError_Type = DisplayString
_EconatAlgSessionAllocError_Object = MibScalar
econatAlgSessionAllocError = _EconatAlgSessionAllocError_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 132),
    _EconatAlgSessionAllocError_Type()
)
econatAlgSessionAllocError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAlgSessionAllocError.setStatus("mandatory")
_EconatAlgSessionFreeError_Type = DisplayString
_EconatAlgSessionFreeError_Object = MibScalar
econatAlgSessionFreeError = _EconatAlgSessionFreeError_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 133),
    _EconatAlgSessionFreeError_Type()
)
econatAlgSessionFreeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAlgSessionFreeError.setStatus("mandatory")
_EconatAlgTranslationAlloc_Type = DisplayString
_EconatAlgTranslationAlloc_Object = MibScalar
econatAlgTranslationAlloc = _EconatAlgTranslationAlloc_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 134),
    _EconatAlgTranslationAlloc_Type()
)
econatAlgTranslationAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAlgTranslationAlloc.setStatus("mandatory")
_EconatAlgTranslationAllocError_Type = DisplayString
_EconatAlgTranslationAllocError_Object = MibScalar
econatAlgTranslationAllocError = _EconatAlgTranslationAllocError_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 135),
    _EconatAlgTranslationAllocError_Type()
)
econatAlgTranslationAllocError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAlgTranslationAllocError.setStatus("mandatory")
_EconatAlgTranslationFree_Type = DisplayString
_EconatAlgTranslationFree_Object = MibScalar
econatAlgTranslationFree = _EconatAlgTranslationFree_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 136),
    _EconatAlgTranslationFree_Type()
)
econatAlgTranslationFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAlgTranslationFree.setStatus("mandatory")
_EconatAlgTranslationFreeError_Type = DisplayString
_EconatAlgTranslationFreeError_Object = MibScalar
econatAlgTranslationFreeError = _EconatAlgTranslationFreeError_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 137),
    _EconatAlgTranslationFreeError_Type()
)
econatAlgTranslationFreeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAlgTranslationFreeError.setStatus("mandatory")
_EconatTcpStateEstablished_Type = DisplayString
_EconatTcpStateEstablished_Object = MibScalar
econatTcpStateEstablished = _EconatTcpStateEstablished_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 150),
    _EconatTcpStateEstablished_Type()
)
econatTcpStateEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTcpStateEstablished.setStatus("mandatory")
_EconatTcpStateCloseTimeout_Type = DisplayString
_EconatTcpStateCloseTimeout_Object = MibScalar
econatTcpStateCloseTimeout = _EconatTcpStateCloseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 151),
    _EconatTcpStateCloseTimeout_Type()
)
econatTcpStateCloseTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTcpStateCloseTimeout.setStatus("mandatory")
_EconatUdpStateEstablished_Type = DisplayString
_EconatUdpStateEstablished_Object = MibScalar
econatUdpStateEstablished = _EconatUdpStateEstablished_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 152),
    _EconatUdpStateEstablished_Type()
)
econatUdpStateEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatUdpStateEstablished.setStatus("mandatory")
_EconatUdpStateCloseTimeout_Type = DisplayString
_EconatUdpStateCloseTimeout_Object = MibScalar
econatUdpStateCloseTimeout = _EconatUdpStateCloseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 153),
    _EconatUdpStateCloseTimeout_Type()
)
econatUdpStateCloseTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatUdpStateCloseTimeout.setStatus("mandatory")
_EconatIcmpStateEstablished_Type = DisplayString
_EconatIcmpStateEstablished_Object = MibScalar
econatIcmpStateEstablished = _EconatIcmpStateEstablished_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 154),
    _EconatIcmpStateEstablished_Type()
)
econatIcmpStateEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatIcmpStateEstablished.setStatus("mandatory")
_EconatIcmpStateCloseTimeout_Type = DisplayString
_EconatIcmpStateCloseTimeout_Object = MibScalar
econatIcmpStateCloseTimeout = _EconatIcmpStateCloseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 155),
    _EconatIcmpStateCloseTimeout_Type()
)
econatIcmpStateCloseTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatIcmpStateCloseTimeout.setStatus("mandatory")
_EconatGreStateEstablished_Type = DisplayString
_EconatGreStateEstablished_Object = MibScalar
econatGreStateEstablished = _EconatGreStateEstablished_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 156),
    _EconatGreStateEstablished_Type()
)
econatGreStateEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatGreStateEstablished.setStatus("mandatory")
_EconatGreStateCloseTimeout_Type = DisplayString
_EconatGreStateCloseTimeout_Object = MibScalar
econatGreStateCloseTimeout = _EconatGreStateCloseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 157),
    _EconatGreStateCloseTimeout_Type()
)
econatGreStateCloseTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatGreStateCloseTimeout.setStatus("mandatory")
_EconatOpaqueStateEstablished_Type = DisplayString
_EconatOpaqueStateEstablished_Object = MibScalar
econatOpaqueStateEstablished = _EconatOpaqueStateEstablished_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 158),
    _EconatOpaqueStateEstablished_Type()
)
econatOpaqueStateEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatOpaqueStateEstablished.setStatus("mandatory")
_EconatOpaqueStateCloseTimeout_Type = DisplayString
_EconatOpaqueStateCloseTimeout_Object = MibScalar
econatOpaqueStateCloseTimeout = _EconatOpaqueStateCloseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 159),
    _EconatOpaqueStateCloseTimeout_Type()
)
econatOpaqueStateCloseTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatOpaqueStateCloseTimeout.setStatus("mandatory")
_EconatSessTcpAlloc_Type = DisplayString
_EconatSessTcpAlloc_Object = MibScalar
econatSessTcpAlloc = _EconatSessTcpAlloc_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 160),
    _EconatSessTcpAlloc_Type()
)
econatSessTcpAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessTcpAlloc.setStatus("mandatory")
_EconatSessTcpFree_Type = DisplayString
_EconatSessTcpFree_Object = MibScalar
econatSessTcpFree = _EconatSessTcpFree_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 161),
    _EconatSessTcpFree_Type()
)
econatSessTcpFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessTcpFree.setStatus("mandatory")
_EconatSessUdpAlloc_Type = DisplayString
_EconatSessUdpAlloc_Object = MibScalar
econatSessUdpAlloc = _EconatSessUdpAlloc_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 162),
    _EconatSessUdpAlloc_Type()
)
econatSessUdpAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessUdpAlloc.setStatus("mandatory")
_EconatSessUdpFree_Type = DisplayString
_EconatSessUdpFree_Object = MibScalar
econatSessUdpFree = _EconatSessUdpFree_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 163),
    _EconatSessUdpFree_Type()
)
econatSessUdpFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessUdpFree.setStatus("mandatory")
_EconatSessIcmpAlloc_Type = DisplayString
_EconatSessIcmpAlloc_Object = MibScalar
econatSessIcmpAlloc = _EconatSessIcmpAlloc_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 164),
    _EconatSessIcmpAlloc_Type()
)
econatSessIcmpAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessIcmpAlloc.setStatus("mandatory")
_EconatSessIcmpFree_Type = DisplayString
_EconatSessIcmpFree_Object = MibScalar
econatSessIcmpFree = _EconatSessIcmpFree_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 165),
    _EconatSessIcmpFree_Type()
)
econatSessIcmpFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessIcmpFree.setStatus("mandatory")
_EconatSessionAllocPerSec_Type = DisplayString
_EconatSessionAllocPerSec_Object = MibScalar
econatSessionAllocPerSec = _EconatSessionAllocPerSec_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 170),
    _EconatSessionAllocPerSec_Type()
)
econatSessionAllocPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocPerSec.setStatus("mandatory")
_EconatSessionFreePerSec_Type = DisplayString
_EconatSessionFreePerSec_Object = MibScalar
econatSessionFreePerSec = _EconatSessionFreePerSec_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 171),
    _EconatSessionFreePerSec_Type()
)
econatSessionFreePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionFreePerSec.setStatus("mandatory")
_EconatNaptGaddrAllocPerSec_Type = DisplayString
_EconatNaptGaddrAllocPerSec_Object = MibScalar
econatNaptGaddrAllocPerSec = _EconatNaptGaddrAllocPerSec_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 172),
    _EconatNaptGaddrAllocPerSec_Type()
)
econatNaptGaddrAllocPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatNaptGaddrAllocPerSec.setStatus("mandatory")
_EconatNaptGaddrFreePerSec_Type = DisplayString
_EconatNaptGaddrFreePerSec_Object = MibScalar
econatNaptGaddrFreePerSec = _EconatNaptGaddrFreePerSec_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 173),
    _EconatNaptGaddrFreePerSec_Type()
)
econatNaptGaddrFreePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatNaptGaddrFreePerSec.setStatus("mandatory")
_EconatSessionAllocNoPoolEgressPerSec_Type = DisplayString
_EconatSessionAllocNoPoolEgressPerSec_Object = MibScalar
econatSessionAllocNoPoolEgressPerSec = _EconatSessionAllocNoPoolEgressPerSec_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 174),
    _EconatSessionAllocNoPoolEgressPerSec_Type()
)
econatSessionAllocNoPoolEgressPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocNoPoolEgressPerSec.setStatus("mandatory")
_EconatSessionAllocNoPoolIngressPerSec_Type = DisplayString
_EconatSessionAllocNoPoolIngressPerSec_Object = MibScalar
econatSessionAllocNoPoolIngressPerSec = _EconatSessionAllocNoPoolIngressPerSec_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 175),
    _EconatSessionAllocNoPoolIngressPerSec_Type()
)
econatSessionAllocNoPoolIngressPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocNoPoolIngressPerSec.setStatus("mandatory")
_EconatSessTcpAllocPerSec_Type = DisplayString
_EconatSessTcpAllocPerSec_Object = MibScalar
econatSessTcpAllocPerSec = _EconatSessTcpAllocPerSec_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 180),
    _EconatSessTcpAllocPerSec_Type()
)
econatSessTcpAllocPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessTcpAllocPerSec.setStatus("mandatory")
_EconatTcpStateEstablishedPerSec_Type = DisplayString
_EconatTcpStateEstablishedPerSec_Object = MibScalar
econatTcpStateEstablishedPerSec = _EconatTcpStateEstablishedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 181),
    _EconatTcpStateEstablishedPerSec_Type()
)
econatTcpStateEstablishedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTcpStateEstablishedPerSec.setStatus("mandatory")
_EconatSessUdpAllocPerSec_Type = DisplayString
_EconatSessUdpAllocPerSec_Object = MibScalar
econatSessUdpAllocPerSec = _EconatSessUdpAllocPerSec_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 182),
    _EconatSessUdpAllocPerSec_Type()
)
econatSessUdpAllocPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessUdpAllocPerSec.setStatus("mandatory")
_EconatUdpStateEstablishedPerSec_Type = DisplayString
_EconatUdpStateEstablishedPerSec_Object = MibScalar
econatUdpStateEstablishedPerSec = _EconatUdpStateEstablishedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 183),
    _EconatUdpStateEstablishedPerSec_Type()
)
econatUdpStateEstablishedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatUdpStateEstablishedPerSec.setStatus("mandatory")
_EconatTranslatedTcpPerSec_Type = DisplayString
_EconatTranslatedTcpPerSec_Object = MibScalar
econatTranslatedTcpPerSec = _EconatTranslatedTcpPerSec_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 184),
    _EconatTranslatedTcpPerSec_Type()
)
econatTranslatedTcpPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTranslatedTcpPerSec.setStatus("mandatory")
_EconatTranslatedUdpPerSec_Type = DisplayString
_EconatTranslatedUdpPerSec_Object = MibScalar
econatTranslatedUdpPerSec = _EconatTranslatedUdpPerSec_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 185),
    _EconatTranslatedUdpPerSec_Type()
)
econatTranslatedUdpPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTranslatedUdpPerSec.setStatus("mandatory")
_EconatInJumbo_Type = DisplayString
_EconatInJumbo_Object = MibScalar
econatInJumbo = _EconatInJumbo_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 200),
    _EconatInJumbo_Type()
)
econatInJumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatInJumbo.setStatus("mandatory")
_EconatOutJumbo_Type = DisplayString
_EconatOutJumbo_Object = MibScalar
econatOutJumbo = _EconatOutJumbo_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 201),
    _EconatOutJumbo_Type()
)
econatOutJumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatOutJumbo.setStatus("mandatory")
_EconatSessionEarlyFreeIngress_Type = DisplayString
_EconatSessionEarlyFreeIngress_Object = MibScalar
econatSessionEarlyFreeIngress = _EconatSessionEarlyFreeIngress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 300),
    _EconatSessionEarlyFreeIngress_Type()
)
econatSessionEarlyFreeIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionEarlyFreeIngress.setStatus("mandatory")
_EconatSessionEarlyFreeEgress_Type = DisplayString
_EconatSessionEarlyFreeEgress_Object = MibScalar
econatSessionEarlyFreeEgress = _EconatSessionEarlyFreeEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 301),
    _EconatSessionEarlyFreeEgress_Type()
)
econatSessionEarlyFreeEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionEarlyFreeEgress.setStatus("mandatory")
_EconatSessionAllocNaptOtherErrorEgress_Type = DisplayString
_EconatSessionAllocNaptOtherErrorEgress_Object = MibScalar
econatSessionAllocNaptOtherErrorEgress = _EconatSessionAllocNaptOtherErrorEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 320),
    _EconatSessionAllocNaptOtherErrorEgress_Type()
)
econatSessionAllocNaptOtherErrorEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocNaptOtherErrorEgress.setStatus("mandatory")
_EconatSessionAllocNaptTcpErrorEgress_Type = DisplayString
_EconatSessionAllocNaptTcpErrorEgress_Object = MibScalar
econatSessionAllocNaptTcpErrorEgress = _EconatSessionAllocNaptTcpErrorEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 321),
    _EconatSessionAllocNaptTcpErrorEgress_Type()
)
econatSessionAllocNaptTcpErrorEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocNaptTcpErrorEgress.setStatus("mandatory")
_EconatSessionAllocNaptUdpErrorEgress_Type = DisplayString
_EconatSessionAllocNaptUdpErrorEgress_Object = MibScalar
econatSessionAllocNaptUdpErrorEgress = _EconatSessionAllocNaptUdpErrorEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 322),
    _EconatSessionAllocNaptUdpErrorEgress_Type()
)
econatSessionAllocNaptUdpErrorEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocNaptUdpErrorEgress.setStatus("mandatory")
_EconatSessionAllocNaptIcmpErrorEgress_Type = DisplayString
_EconatSessionAllocNaptIcmpErrorEgress_Object = MibScalar
econatSessionAllocNaptIcmpErrorEgress = _EconatSessionAllocNaptIcmpErrorEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 323),
    _EconatSessionAllocNaptIcmpErrorEgress_Type()
)
econatSessionAllocNaptIcmpErrorEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocNaptIcmpErrorEgress.setStatus("mandatory")
_EconatSessionAllocNaptPptpgreErrorEgress_Type = DisplayString
_EconatSessionAllocNaptPptpgreErrorEgress_Object = MibScalar
econatSessionAllocNaptPptpgreErrorEgress = _EconatSessionAllocNaptPptpgreErrorEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 324),
    _EconatSessionAllocNaptPptpgreErrorEgress_Type()
)
econatSessionAllocNaptPptpgreErrorEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocNaptPptpgreErrorEgress.setStatus("mandatory")
_EconatSessionAllocNaptL4otherErrorEgress_Type = DisplayString
_EconatSessionAllocNaptL4otherErrorEgress_Object = MibScalar
econatSessionAllocNaptL4otherErrorEgress = _EconatSessionAllocNaptL4otherErrorEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 325),
    _EconatSessionAllocNaptL4otherErrorEgress_Type()
)
econatSessionAllocNaptL4otherErrorEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocNaptL4otherErrorEgress.setStatus("mandatory")
_EconatDroppedPacketCauseL2mtu_Type = DisplayString
_EconatDroppedPacketCauseL2mtu_Object = MibScalar
econatDroppedPacketCauseL2mtu = _EconatDroppedPacketCauseL2mtu_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 326),
    _EconatDroppedPacketCauseL2mtu_Type()
)
econatDroppedPacketCauseL2mtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDroppedPacketCauseL2mtu.setStatus("mandatory")
_EconatSessionAllocBnatOtherErrorEgress_Type = DisplayString
_EconatSessionAllocBnatOtherErrorEgress_Object = MibScalar
econatSessionAllocBnatOtherErrorEgress = _EconatSessionAllocBnatOtherErrorEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 340),
    _EconatSessionAllocBnatOtherErrorEgress_Type()
)
econatSessionAllocBnatOtherErrorEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocBnatOtherErrorEgress.setStatus("mandatory")
_EconatSessionAllocBnatTcpErrorEgress_Type = DisplayString
_EconatSessionAllocBnatTcpErrorEgress_Object = MibScalar
econatSessionAllocBnatTcpErrorEgress = _EconatSessionAllocBnatTcpErrorEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 341),
    _EconatSessionAllocBnatTcpErrorEgress_Type()
)
econatSessionAllocBnatTcpErrorEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocBnatTcpErrorEgress.setStatus("mandatory")
_EconatSessionAllocBnatUdpErrorEgress_Type = DisplayString
_EconatSessionAllocBnatUdpErrorEgress_Object = MibScalar
econatSessionAllocBnatUdpErrorEgress = _EconatSessionAllocBnatUdpErrorEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 342),
    _EconatSessionAllocBnatUdpErrorEgress_Type()
)
econatSessionAllocBnatUdpErrorEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocBnatUdpErrorEgress.setStatus("mandatory")
_EconatSessionAllocBnatIcmpErrorEgress_Type = DisplayString
_EconatSessionAllocBnatIcmpErrorEgress_Object = MibScalar
econatSessionAllocBnatIcmpErrorEgress = _EconatSessionAllocBnatIcmpErrorEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 343),
    _EconatSessionAllocBnatIcmpErrorEgress_Type()
)
econatSessionAllocBnatIcmpErrorEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocBnatIcmpErrorEgress.setStatus("mandatory")
_EconatSessionAllocBnatPptpgreErrorEgress_Type = DisplayString
_EconatSessionAllocBnatPptpgreErrorEgress_Object = MibScalar
econatSessionAllocBnatPptpgreErrorEgress = _EconatSessionAllocBnatPptpgreErrorEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 344),
    _EconatSessionAllocBnatPptpgreErrorEgress_Type()
)
econatSessionAllocBnatPptpgreErrorEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocBnatPptpgreErrorEgress.setStatus("mandatory")
_EconatSessionAllocBnatL4otherErrorEgress_Type = DisplayString
_EconatSessionAllocBnatL4otherErrorEgress_Object = MibScalar
econatSessionAllocBnatL4otherErrorEgress = _EconatSessionAllocBnatL4otherErrorEgress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 345),
    _EconatSessionAllocBnatL4otherErrorEgress_Type()
)
econatSessionAllocBnatL4otherErrorEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSessionAllocBnatL4otherErrorEgress.setStatus("mandatory")
_EconatNaptGaddrAllocError_Type = DisplayString
_EconatNaptGaddrAllocError_Object = MibScalar
econatNaptGaddrAllocError = _EconatNaptGaddrAllocError_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 360),
    _EconatNaptGaddrAllocError_Type()
)
econatNaptGaddrAllocError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatNaptGaddrAllocError.setStatus("mandatory")
_EconatBnatGaddrAllocError_Type = DisplayString
_EconatBnatGaddrAllocError_Object = MibScalar
econatBnatGaddrAllocError = _EconatBnatGaddrAllocError_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 361),
    _EconatBnatGaddrAllocError_Type()
)
econatBnatGaddrAllocError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatGaddrAllocError.setStatus("mandatory")
_EconatBnatPortAllocErrLimitReached_Type = DisplayString
_EconatBnatPortAllocErrLimitReached_Object = MibScalar
econatBnatPortAllocErrLimitReached = _EconatBnatPortAllocErrLimitReached_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 370),
    _EconatBnatPortAllocErrLimitReached_Type()
)
econatBnatPortAllocErrLimitReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatPortAllocErrLimitReached.setStatus("mandatory")
_EconatBnatPortAllocErrIngressDisabled_Type = DisplayString
_EconatBnatPortAllocErrIngressDisabled_Object = MibScalar
econatBnatPortAllocErrIngressDisabled = _EconatBnatPortAllocErrIngressDisabled_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 371),
    _EconatBnatPortAllocErrIngressDisabled_Type()
)
econatBnatPortAllocErrIngressDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatPortAllocErrIngressDisabled.setStatus("mandatory")
_EconatBnatPortAllocErrIngressInactiveClient_Type = DisplayString
_EconatBnatPortAllocErrIngressInactiveClient_Object = MibScalar
econatBnatPortAllocErrIngressInactiveClient = _EconatBnatPortAllocErrIngressInactiveClient_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 372),
    _EconatBnatPortAllocErrIngressInactiveClient_Type()
)
econatBnatPortAllocErrIngressInactiveClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatPortAllocErrIngressInactiveClient.setStatus("mandatory")
_EconatBnatPortAllocErrIngressNoClient_Type = DisplayString
_EconatBnatPortAllocErrIngressNoClient_Object = MibScalar
econatBnatPortAllocErrIngressNoClient = _EconatBnatPortAllocErrIngressNoClient_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 373),
    _EconatBnatPortAllocErrIngressNoClient_Type()
)
econatBnatPortAllocErrIngressNoClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatPortAllocErrIngressNoClient.setStatus("mandatory")
_EconatBnatPortAllocErrMappingCreation_Type = DisplayString
_EconatBnatPortAllocErrMappingCreation_Object = MibScalar
econatBnatPortAllocErrMappingCreation = _EconatBnatPortAllocErrMappingCreation_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 374),
    _EconatBnatPortAllocErrMappingCreation_Type()
)
econatBnatPortAllocErrMappingCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatPortAllocErrMappingCreation.setStatus("mandatory")
_EconatBnatPortFreeErrNoMapping_Type = DisplayString
_EconatBnatPortFreeErrNoMapping_Object = MibScalar
econatBnatPortFreeErrNoMapping = _EconatBnatPortFreeErrNoMapping_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 375),
    _EconatBnatPortFreeErrNoMapping_Type()
)
econatBnatPortFreeErrNoMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatPortFreeErrNoMapping.setStatus("mandatory")
_EconatBnatPortFreeErrAlreadyZero_Type = DisplayString
_EconatBnatPortFreeErrAlreadyZero_Object = MibScalar
econatBnatPortFreeErrAlreadyZero = _EconatBnatPortFreeErrAlreadyZero_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 376),
    _EconatBnatPortFreeErrAlreadyZero_Type()
)
econatBnatPortFreeErrAlreadyZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatPortFreeErrAlreadyZero.setStatus("mandatory")
_EconatAllocatedLoggerMbufs_Type = DisplayString
_EconatAllocatedLoggerMbufs_Object = MibScalar
econatAllocatedLoggerMbufs = _EconatAllocatedLoggerMbufs_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 380),
    _EconatAllocatedLoggerMbufs_Type()
)
econatAllocatedLoggerMbufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAllocatedLoggerMbufs.setStatus("mandatory")
_EconatAllocatedArpMbufs_Type = DisplayString
_EconatAllocatedArpMbufs_Object = MibScalar
econatAllocatedArpMbufs = _EconatAllocatedArpMbufs_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 381),
    _EconatAllocatedArpMbufs_Type()
)
econatAllocatedArpMbufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAllocatedArpMbufs.setStatus("mandatory")
_EconatAllocatedLldpMbufs_Type = DisplayString
_EconatAllocatedLldpMbufs_Object = MibScalar
econatAllocatedLldpMbufs = _EconatAllocatedLldpMbufs_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 382),
    _EconatAllocatedLldpMbufs_Type()
)
econatAllocatedLldpMbufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAllocatedLldpMbufs.setStatus("mandatory")
_EconatSentLoggerMbufs_Type = DisplayString
_EconatSentLoggerMbufs_Object = MibScalar
econatSentLoggerMbufs = _EconatSentLoggerMbufs_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 385),
    _EconatSentLoggerMbufs_Type()
)
econatSentLoggerMbufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSentLoggerMbufs.setStatus("mandatory")
_EconatSysloggerNoMbufs_Type = DisplayString
_EconatSysloggerNoMbufs_Object = MibScalar
econatSysloggerNoMbufs = _EconatSysloggerNoMbufs_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 387),
    _EconatSysloggerNoMbufs_Type()
)
econatSysloggerNoMbufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatSysloggerNoMbufs.setStatus("mandatory")
_EconatUrllogMsgsEnqueued_Type = DisplayString
_EconatUrllogMsgsEnqueued_Object = MibScalar
econatUrllogMsgsEnqueued = _EconatUrllogMsgsEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 390),
    _EconatUrllogMsgsEnqueued_Type()
)
econatUrllogMsgsEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatUrllogMsgsEnqueued.setStatus("mandatory")
_EconatUrllogMsgsNotEnqueued_Type = DisplayString
_EconatUrllogMsgsNotEnqueued_Object = MibScalar
econatUrllogMsgsNotEnqueued = _EconatUrllogMsgsNotEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 391),
    _EconatUrllogMsgsNotEnqueued_Type()
)
econatUrllogMsgsNotEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatUrllogMsgsNotEnqueued.setStatus("mandatory")
_EconatRaceNoEgressPayload_Type = DisplayString
_EconatRaceNoEgressPayload_Object = MibScalar
econatRaceNoEgressPayload = _EconatRaceNoEgressPayload_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 395),
    _EconatRaceNoEgressPayload_Type()
)
econatRaceNoEgressPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatRaceNoEgressPayload.setStatus("mandatory")
_EconatRaceNoIngressPayload_Type = DisplayString
_EconatRaceNoIngressPayload_Object = MibScalar
econatRaceNoIngressPayload = _EconatRaceNoIngressPayload_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 396),
    _EconatRaceNoIngressPayload_Type()
)
econatRaceNoIngressPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatRaceNoIngressPayload.setStatus("mandatory")
_EconatAlgEnqueued_Type = DisplayString
_EconatAlgEnqueued_Object = MibScalar
econatAlgEnqueued = _EconatAlgEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 397),
    _EconatAlgEnqueued_Type()
)
econatAlgEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAlgEnqueued.setStatus("mandatory")
_EconatAlgRingOverflows_Type = DisplayString
_EconatAlgRingOverflows_Object = MibScalar
econatAlgRingOverflows = _EconatAlgRingOverflows_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 398),
    _EconatAlgRingOverflows_Type()
)
econatAlgRingOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAlgRingOverflows.setStatus("mandatory")
_EconatAlgHashOverflows_Type = DisplayString
_EconatAlgHashOverflows_Object = MibScalar
econatAlgHashOverflows = _EconatAlgHashOverflows_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 399),
    _EconatAlgHashOverflows_Type()
)
econatAlgHashOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAlgHashOverflows.setStatus("mandatory")
_EconatAlgFtpPatchDng_Type = DisplayString
_EconatAlgFtpPatchDng_Object = MibScalar
econatAlgFtpPatchDng = _EconatAlgFtpPatchDng_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 400),
    _EconatAlgFtpPatchDng_Type()
)
econatAlgFtpPatchDng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAlgFtpPatchDng.setStatus("mandatory")
_EconatAlgSipPatchDng_Type = DisplayString
_EconatAlgSipPatchDng_Object = MibScalar
econatAlgSipPatchDng = _EconatAlgSipPatchDng_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 401),
    _EconatAlgSipPatchDng_Type()
)
econatAlgSipPatchDng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAlgSipPatchDng.setStatus("mandatory")
_EconatAlgRtspPatchDng_Type = DisplayString
_EconatAlgRtspPatchDng_Object = MibScalar
econatAlgRtspPatchDng = _EconatAlgRtspPatchDng_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 402),
    _EconatAlgRtspPatchDng_Type()
)
econatAlgRtspPatchDng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatAlgRtspPatchDng.setStatus("mandatory")
_EconatRteHashOverflow_Type = DisplayString
_EconatRteHashOverflow_Object = MibScalar
econatRteHashOverflow = _EconatRteHashOverflow_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 403),
    _EconatRteHashOverflow_Type()
)
econatRteHashOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatRteHashOverflow.setStatus("mandatory")
_EconatPsuStateChanges_Type = DisplayString
_EconatPsuStateChanges_Object = MibScalar
econatPsuStateChanges = _EconatPsuStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 404),
    _EconatPsuStateChanges_Type()
)
econatPsuStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatPsuStateChanges.setStatus("mandatory")
_EconatHairpinProcess_Type = DisplayString
_EconatHairpinProcess_Object = MibScalar
econatHairpinProcess = _EconatHairpinProcess_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 405),
    _EconatHairpinProcess_Type()
)
econatHairpinProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatHairpinProcess.setStatus("mandatory")
_EconatHairpinRefused_Type = DisplayString
_EconatHairpinRefused_Object = MibScalar
econatHairpinRefused = _EconatHairpinRefused_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 406),
    _EconatHairpinRefused_Type()
)
econatHairpinRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatHairpinRefused.setStatus("mandatory")
_EconatPpFailedSanitycheck_Type = DisplayString
_EconatPpFailedSanitycheck_Object = MibScalar
econatPpFailedSanitycheck = _EconatPpFailedSanitycheck_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 407),
    _EconatPpFailedSanitycheck_Type()
)
econatPpFailedSanitycheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatPpFailedSanitycheck.setStatus("mandatory")
_EconatPpCantccHairpin_Type = DisplayString
_EconatPpCantccHairpin_Object = MibScalar
econatPpCantccHairpin = _EconatPpCantccHairpin_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 408),
    _EconatPpCantccHairpin_Type()
)
econatPpCantccHairpin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatPpCantccHairpin.setStatus("mandatory")
_EconatPpCantccReconfig_Type = DisplayString
_EconatPpCantccReconfig_Object = MibScalar
econatPpCantccReconfig = _EconatPpCantccReconfig_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 409),
    _EconatPpCantccReconfig_Type()
)
econatPpCantccReconfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatPpCantccReconfig.setStatus("mandatory")
_EconatPpTranslationBug_Type = DisplayString
_EconatPpTranslationBug_Object = MibScalar
econatPpTranslationBug = _EconatPpTranslationBug_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 410),
    _EconatPpTranslationBug_Type()
)
econatPpTranslationBug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatPpTranslationBug.setStatus("mandatory")
_EconatPpHairpinRefused_Type = DisplayString
_EconatPpHairpinRefused_Object = MibScalar
econatPpHairpinRefused = _EconatPpHairpinRefused_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 411),
    _EconatPpHairpinRefused_Type()
)
econatPpHairpinRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatPpHairpinRefused.setStatus("mandatory")
_EconatPpHairpinRefusedIngress_Type = DisplayString
_EconatPpHairpinRefusedIngress_Object = MibScalar
econatPpHairpinRefusedIngress = _EconatPpHairpinRefusedIngress_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 412),
    _EconatPpHairpinRefusedIngress_Type()
)
econatPpHairpinRefusedIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatPpHairpinRefusedIngress.setStatus("mandatory")
_EconatPpInvalidFlowDrop_Type = DisplayString
_EconatPpInvalidFlowDrop_Object = MibScalar
econatPpInvalidFlowDrop = _EconatPpInvalidFlowDrop_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 413),
    _EconatPpInvalidFlowDrop_Type()
)
econatPpInvalidFlowDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatPpInvalidFlowDrop.setStatus("mandatory")
_EconatNaptPortAlloc_Type = DisplayString
_EconatNaptPortAlloc_Object = MibScalar
econatNaptPortAlloc = _EconatNaptPortAlloc_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 430),
    _EconatNaptPortAlloc_Type()
)
econatNaptPortAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatNaptPortAlloc.setStatus("mandatory")
_EconatNaptPortFree_Type = DisplayString
_EconatNaptPortFree_Object = MibScalar
econatNaptPortFree = _EconatNaptPortFree_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 431),
    _EconatNaptPortFree_Type()
)
econatNaptPortFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatNaptPortFree.setStatus("mandatory")
_EconatBnatGaddrAlloc_Type = DisplayString
_EconatBnatGaddrAlloc_Object = MibScalar
econatBnatGaddrAlloc = _EconatBnatGaddrAlloc_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 432),
    _EconatBnatGaddrAlloc_Type()
)
econatBnatGaddrAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatGaddrAlloc.setStatus("mandatory")
_EconatBnatGaddrFree_Type = DisplayString
_EconatBnatGaddrFree_Object = MibScalar
econatBnatGaddrFree = _EconatBnatGaddrFree_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 433),
    _EconatBnatGaddrFree_Type()
)
econatBnatGaddrFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatGaddrFree.setStatus("mandatory")
_EconatBnatPortAlloc_Type = DisplayString
_EconatBnatPortAlloc_Object = MibScalar
econatBnatPortAlloc = _EconatBnatPortAlloc_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 434),
    _EconatBnatPortAlloc_Type()
)
econatBnatPortAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatPortAlloc.setStatus("mandatory")
_EconatBnatPortFree_Type = DisplayString
_EconatBnatPortFree_Object = MibScalar
econatBnatPortFree = _EconatBnatPortFree_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 435),
    _EconatBnatPortFree_Type()
)
econatBnatPortFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBnatPortFree.setStatus("mandatory")
_EconatBrasDroppedAccess_Type = DisplayString
_EconatBrasDroppedAccess_Object = MibScalar
econatBrasDroppedAccess = _EconatBrasDroppedAccess_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 500),
    _EconatBrasDroppedAccess_Type()
)
econatBrasDroppedAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBrasDroppedAccess.setStatus("mandatory")
_EconatBrasDroppedPolicer_Type = DisplayString
_EconatBrasDroppedPolicer_Object = MibScalar
econatBrasDroppedPolicer = _EconatBrasDroppedPolicer_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 501),
    _EconatBrasDroppedPolicer_Type()
)
econatBrasDroppedPolicer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBrasDroppedPolicer.setStatus("mandatory")
_EconatBrasRedirected_Type = DisplayString
_EconatBrasRedirected_Object = MibScalar
econatBrasRedirected = _EconatBrasRedirected_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 502),
    _EconatBrasRedirected_Type()
)
econatBrasRedirected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatBrasRedirected.setStatus("mandatory")
_EconatDpiBannedEgressTcp_Type = DisplayString
_EconatDpiBannedEgressTcp_Object = MibScalar
econatDpiBannedEgressTcp = _EconatDpiBannedEgressTcp_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 600),
    _EconatDpiBannedEgressTcp_Type()
)
econatDpiBannedEgressTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDpiBannedEgressTcp.setStatus("mandatory")
_EconatDpiBannedIngressTcp_Type = DisplayString
_EconatDpiBannedIngressTcp_Object = MibScalar
econatDpiBannedIngressTcp = _EconatDpiBannedIngressTcp_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 601),
    _EconatDpiBannedIngressTcp_Type()
)
econatDpiBannedIngressTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDpiBannedIngressTcp.setStatus("mandatory")
_EconatDpiBannedEgressUdp_Type = DisplayString
_EconatDpiBannedEgressUdp_Object = MibScalar
econatDpiBannedEgressUdp = _EconatDpiBannedEgressUdp_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 602),
    _EconatDpiBannedEgressUdp_Type()
)
econatDpiBannedEgressUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDpiBannedEgressUdp.setStatus("mandatory")
_EconatDpiBannedIngressUdp_Type = DisplayString
_EconatDpiBannedIngressUdp_Object = MibScalar
econatDpiBannedIngressUdp = _EconatDpiBannedIngressUdp_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 603),
    _EconatDpiBannedIngressUdp_Type()
)
econatDpiBannedIngressUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDpiBannedIngressUdp.setStatus("mandatory")
_EconatDpiRKNLastLoad_Type = DisplayString
_EconatDpiRKNLastLoad_Object = MibScalar
econatDpiRKNLastLoad = _EconatDpiRKNLastLoad_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 605),
    _EconatDpiRKNLastLoad_Type()
)
econatDpiRKNLastLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDpiRKNLastLoad.setStatus("mandatory")
_EconatDpiRKNLastParse_Type = DisplayString
_EconatDpiRKNLastParse_Object = MibScalar
econatDpiRKNLastParse = _EconatDpiRKNLastParse_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 606),
    _EconatDpiRKNLastParse_Type()
)
econatDpiRKNLastParse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDpiRKNLastParse.setStatus("mandatory")
_EconatDpiNoHostBufs_Type = DisplayString
_EconatDpiNoHostBufs_Object = MibScalar
econatDpiNoHostBufs = _EconatDpiNoHostBufs_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 620),
    _EconatDpiNoHostBufs_Type()
)
econatDpiNoHostBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDpiNoHostBufs.setStatus("mandatory")
_EconatDpiNoPathBufs_Type = DisplayString
_EconatDpiNoPathBufs_Object = MibScalar
econatDpiNoPathBufs = _EconatDpiNoPathBufs_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 621),
    _EconatDpiNoPathBufs_Type()
)
econatDpiNoPathBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDpiNoPathBufs.setStatus("mandatory")
_EconatDpiNoStateBufs_Type = DisplayString
_EconatDpiNoStateBufs_Object = MibScalar
econatDpiNoStateBufs = _EconatDpiNoStateBufs_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 622),
    _EconatDpiNoStateBufs_Type()
)
econatDpiNoStateBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatDpiNoStateBufs.setStatus("mandatory")
_EconatTableHash8Ext1_Type = DisplayString
_EconatTableHash8Ext1_Object = MibScalar
econatTableHash8Ext1 = _EconatTableHash8Ext1_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 700),
    _EconatTableHash8Ext1_Type()
)
econatTableHash8Ext1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTableHash8Ext1.setStatus("mandatory")
_EconatTableHash8Ext2_Type = DisplayString
_EconatTableHash8Ext2_Object = MibScalar
econatTableHash8Ext2 = _EconatTableHash8Ext2_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 701),
    _EconatTableHash8Ext2_Type()
)
econatTableHash8Ext2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTableHash8Ext2.setStatus("mandatory")
_EconatTableHash8Ext4_Type = DisplayString
_EconatTableHash8Ext4_Object = MibScalar
econatTableHash8Ext4 = _EconatTableHash8Ext4_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 702),
    _EconatTableHash8Ext4_Type()
)
econatTableHash8Ext4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTableHash8Ext4.setStatus("mandatory")
_EconatTableHash8Ext8_Type = DisplayString
_EconatTableHash8Ext8_Object = MibScalar
econatTableHash8Ext8 = _EconatTableHash8Ext8_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 703),
    _EconatTableHash8Ext8_Type()
)
econatTableHash8Ext8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTableHash8Ext8.setStatus("mandatory")
_EconatTableHash8Ext16_Type = DisplayString
_EconatTableHash8Ext16_Object = MibScalar
econatTableHash8Ext16 = _EconatTableHash8Ext16_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 704),
    _EconatTableHash8Ext16_Type()
)
econatTableHash8Ext16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTableHash8Ext16.setStatus("mandatory")
_EconatTableHash8Overflow_Type = DisplayString
_EconatTableHash8Overflow_Object = MibScalar
econatTableHash8Overflow = _EconatTableHash8Overflow_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 705),
    _EconatTableHash8Overflow_Type()
)
econatTableHash8Overflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTableHash8Overflow.setStatus("mandatory")
_EconatTableHash12Ext1_Type = DisplayString
_EconatTableHash12Ext1_Object = MibScalar
econatTableHash12Ext1 = _EconatTableHash12Ext1_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 706),
    _EconatTableHash12Ext1_Type()
)
econatTableHash12Ext1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTableHash12Ext1.setStatus("mandatory")
_EconatTableHash12Ext2_Type = DisplayString
_EconatTableHash12Ext2_Object = MibScalar
econatTableHash12Ext2 = _EconatTableHash12Ext2_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 707),
    _EconatTableHash12Ext2_Type()
)
econatTableHash12Ext2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTableHash12Ext2.setStatus("mandatory")
_EconatTableHash12Ext4_Type = DisplayString
_EconatTableHash12Ext4_Object = MibScalar
econatTableHash12Ext4 = _EconatTableHash12Ext4_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 708),
    _EconatTableHash12Ext4_Type()
)
econatTableHash12Ext4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTableHash12Ext4.setStatus("mandatory")
_EconatTableHash12Ext8_Type = DisplayString
_EconatTableHash12Ext8_Object = MibScalar
econatTableHash12Ext8 = _EconatTableHash12Ext8_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 709),
    _EconatTableHash12Ext8_Type()
)
econatTableHash12Ext8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTableHash12Ext8.setStatus("mandatory")
_EconatTableHash12Ext16_Type = DisplayString
_EconatTableHash12Ext16_Object = MibScalar
econatTableHash12Ext16 = _EconatTableHash12Ext16_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 710),
    _EconatTableHash12Ext16_Type()
)
econatTableHash12Ext16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTableHash12Ext16.setStatus("mandatory")
_EconatTableHash12Overflow_Type = DisplayString
_EconatTableHash12Overflow_Object = MibScalar
econatTableHash12Overflow = _EconatTableHash12Overflow_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 711),
    _EconatTableHash12Overflow_Type()
)
econatTableHash12Overflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTableHash12Overflow.setStatus("mandatory")
_EconatTransPerUserLimitExceeded_Type = DisplayString
_EconatTransPerUserLimitExceeded_Object = MibScalar
econatTransPerUserLimitExceeded = _EconatTransPerUserLimitExceeded_Object(
    (1, 3, 6, 1, 4, 1, 45555, 1, 2, 712),
    _EconatTransPerUserLimitExceeded_Type()
)
econatTransPerUserLimitExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    econatTransPerUserLimitExceeded.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ECONAT-MIB",
    **{"rdp": rdp,
       "econat": econat,
       "counters": counters,
       "econatGaddrAlloc": econatGaddrAlloc,
       "econatGaddrFree": econatGaddrFree,
       "econatPortBlockAlloc": econatPortBlockAlloc,
       "econatPortBlockFree": econatPortBlockFree,
       "econatPortAlloc": econatPortAlloc,
       "econatPortFree": econatPortFree,
       "econatSessionAlloc": econatSessionAlloc,
       "econatSessionFree": econatSessionFree,
       "econatSessionAllocErrorEgress": econatSessionAllocErrorEgress,
       "econatSessionAllocErrorIngress": econatSessionAllocErrorIngress,
       "econatTranslationAllocError": econatTranslationAllocError,
       "econatSessionFreeError": econatSessionFreeError,
       "econatLoggedMessages": econatLoggedMessages,
       "econatDroppedMessages": econatDroppedMessages,
       "econatAvgEgressRxQueue": econatAvgEgressRxQueue,
       "econatAvgIngressRxQueue": econatAvgIngressRxQueue,
       "econatEgressRxQueueVoid": econatEgressRxQueueVoid,
       "econatEgressRxQueueMedium": econatEgressRxQueueMedium,
       "econatEgressRxQueueOverflow": econatEgressRxQueueOverflow,
       "econatIngressRxQueueVoid": econatIngressRxQueueVoid,
       "econatIngressRxQueueMedium": econatIngressRxQueueMedium,
       "econatIngressRxQueueOverflow": econatIngressRxQueueOverflow,
       "econatDispFreeMbufs0": econatDispFreeMbufs0,
       "econatDispFreeMbufs1": econatDispFreeMbufs1,
       "econatAvgConnRequestsPerBurst": econatAvgConnRequestsPerBurst,
       "econatAvgConnRequestsPerNonEmptyBurst": econatAvgConnRequestsPerNonEmptyBurst,
       "econatConnRingVoid": econatConnRingVoid,
       "econatConnRingMedium": econatConnRingMedium,
       "econatConnRingPostponed": econatConnRingPostponed,
       "econatConnRingOverflow": econatConnRingOverflow,
       "econatRacePrevented1": econatRacePrevented1,
       "econatRacePrevented2": econatRacePrevented2,
       "econatRacePrevented3": econatRacePrevented3,
       "econatIpDropUnknownProto": econatIpDropUnknownProto,
       "econatIpPassUnknownProto": econatIpPassUnknownProto,
       "econatIpDropOpaqueProto": econatIpDropOpaqueProto,
       "econatIpPassOpaqueProto": econatIpPassOpaqueProto,
       "econatTranslatedOpaque": econatTranslatedOpaque,
       "econatInOpaqueError": econatInOpaqueError,
       "econatEgressOpaqueNoPool": econatEgressOpaqueNoPool,
       "econatIngressOpaqueNoPool": econatIngressOpaqueNoPool,
       "econatSessionAllocNoPoolEgress": econatSessionAllocNoPoolEgress,
       "econatSessionAllocNoPoolIngress": econatSessionAllocNoPoolIngress,
       "econatAvgEgressConnRequests": econatAvgEgressConnRequests,
       "econatAvgIngressConnRequests": econatAvgIngressConnRequests,
       "econatAvgEgressConnsCreated": econatAvgEgressConnsCreated,
       "econatAvgIngressConnsCreated": econatAvgIngressConnsCreated,
       "econatUsedNaptPortBlocks": econatUsedNaptPortBlocks,
       "econatUsedNaptPorts": econatUsedNaptPorts,
       "poolsinfo": poolsinfo,
       "poolid": poolid,
       "econatNaptTotalAddresses": econatNaptTotalAddresses,
       "econatNaptUsedAddress": econatNaptUsedAddress,
       "econatNaptUnusedAddresses": econatNaptUnusedAddresses,
       "econatNaptTotalPortsTcp": econatNaptTotalPortsTcp,
       "econatNaptTotalPortsUdp": econatNaptTotalPortsUdp,
       "econatNaptTotalPortsIcmp": econatNaptTotalPortsIcmp,
       "econatNaptUsedPortsTcp": econatNaptUsedPortsTcp,
       "econatNaptUsedPortsUdp": econatNaptUsedPortsUdp,
       "econatNaptUsedPortsIcmp": econatNaptUsedPortsIcmp,
       "econatBnatTotalAddresses": econatBnatTotalAddresses,
       "econatBnatStaticAddresses": econatBnatStaticAddresses,
       "econatBnatUsedAddresses": econatBnatUsedAddresses,
       "econatBnatUnusedAddresses": econatBnatUnusedAddresses,
       "econatBnatConnectionsTcpIngress": econatBnatConnectionsTcpIngress,
       "econatBnatConnectionsUdpIngress": econatBnatConnectionsUdpIngress,
       "econatBnatConnectionsIcmpIngress": econatBnatConnectionsIcmpIngress,
       "econatBnatConnectionsOtherIngress": econatBnatConnectionsOtherIngress,
       "econatBnatConnectionsTcpEgress": econatBnatConnectionsTcpEgress,
       "econatBnatConnectionsUdpEgress": econatBnatConnectionsUdpEgress,
       "econatBnatConnectionsIcmpEgress": econatBnatConnectionsIcmpEgress,
       "econatBnatConnectionsOtherEgress": econatBnatConnectionsOtherEgress,
       "econatBnatConnectionsTcp": econatBnatConnectionsTcp,
       "econatBnatConnectionsUdp": econatBnatConnectionsUdp,
       "econatBnatConnectionsIcmp": econatBnatConnectionsIcmp,
       "econatBnatConnectionsOther": econatBnatConnectionsOther,
       "econatTcpSessions": econatTcpSessions,
       "econatAproxSessionLimit": econatAproxSessionLimit,
       "econatUdpSessions": econatUdpSessions,
       "econatAproxSessionLimit2": econatAproxSessionLimit2,
       "econatIcmpSessions": econatIcmpSessions,
       "econatAproxSessionLimit3": econatAproxSessionLimit3,
       "econatDpCpuBurst": econatDpCpuBurst,
       "econatDpTotalMemory": econatDpTotalMemory,
       "econatDpFreeMemory": econatDpFreeMemory,
       "econatCpTotalMemory": econatCpTotalMemory,
       "econatCpFreeMemory": econatCpFreeMemory,
       "econatDpCpuSocket0": econatDpCpuSocket0,
       "econatDpCpuSocket1": econatDpCpuSocket1,
       "econatAvgEgressRxQueueSocket0": econatAvgEgressRxQueueSocket0,
       "econatAvgIngressRxQueueSocket0": econatAvgIngressRxQueueSocket0,
       "econatAvgEgressRxQueueSocket1": econatAvgEgressRxQueueSocket1,
       "econatAvgIngressRxQueueSocket1": econatAvgIngressRxQueueSocket1,
       "econatAvgEgressRxQueueSocketBoth": econatAvgEgressRxQueueSocketBoth,
       "econatAvgIngressRxQueueSocketBoth": econatAvgIngressRxQueueSocketBoth,
       "econatFreeLoggingMbufs": econatFreeLoggingMbufs,
       "econatCntReconfigs": econatCntReconfigs,
       "econatDroppedClonedMessages": econatDroppedClonedMessages,
       "econatDroppedLoggerMbufs": econatDroppedLoggerMbufs,
       "econatRolledQueues": econatRolledQueues,
       "econatAlgSessionAlloc": econatAlgSessionAlloc,
       "econatAlgSessionFree": econatAlgSessionFree,
       "econatAlgSessionAllocError": econatAlgSessionAllocError,
       "econatAlgSessionFreeError": econatAlgSessionFreeError,
       "econatAlgTranslationAlloc": econatAlgTranslationAlloc,
       "econatAlgTranslationAllocError": econatAlgTranslationAllocError,
       "econatAlgTranslationFree": econatAlgTranslationFree,
       "econatAlgTranslationFreeError": econatAlgTranslationFreeError,
       "econatTcpStateEstablished": econatTcpStateEstablished,
       "econatTcpStateCloseTimeout": econatTcpStateCloseTimeout,
       "econatUdpStateEstablished": econatUdpStateEstablished,
       "econatUdpStateCloseTimeout": econatUdpStateCloseTimeout,
       "econatIcmpStateEstablished": econatIcmpStateEstablished,
       "econatIcmpStateCloseTimeout": econatIcmpStateCloseTimeout,
       "econatGreStateEstablished": econatGreStateEstablished,
       "econatGreStateCloseTimeout": econatGreStateCloseTimeout,
       "econatOpaqueStateEstablished": econatOpaqueStateEstablished,
       "econatOpaqueStateCloseTimeout": econatOpaqueStateCloseTimeout,
       "econatSessTcpAlloc": econatSessTcpAlloc,
       "econatSessTcpFree": econatSessTcpFree,
       "econatSessUdpAlloc": econatSessUdpAlloc,
       "econatSessUdpFree": econatSessUdpFree,
       "econatSessIcmpAlloc": econatSessIcmpAlloc,
       "econatSessIcmpFree": econatSessIcmpFree,
       "econatSessionAllocPerSec": econatSessionAllocPerSec,
       "econatSessionFreePerSec": econatSessionFreePerSec,
       "econatNaptGaddrAllocPerSec": econatNaptGaddrAllocPerSec,
       "econatNaptGaddrFreePerSec": econatNaptGaddrFreePerSec,
       "econatSessionAllocNoPoolEgressPerSec": econatSessionAllocNoPoolEgressPerSec,
       "econatSessionAllocNoPoolIngressPerSec": econatSessionAllocNoPoolIngressPerSec,
       "econatSessTcpAllocPerSec": econatSessTcpAllocPerSec,
       "econatTcpStateEstablishedPerSec": econatTcpStateEstablishedPerSec,
       "econatSessUdpAllocPerSec": econatSessUdpAllocPerSec,
       "econatUdpStateEstablishedPerSec": econatUdpStateEstablishedPerSec,
       "econatTranslatedTcpPerSec": econatTranslatedTcpPerSec,
       "econatTranslatedUdpPerSec": econatTranslatedUdpPerSec,
       "econatInJumbo": econatInJumbo,
       "econatOutJumbo": econatOutJumbo,
       "econatSessionEarlyFreeIngress": econatSessionEarlyFreeIngress,
       "econatSessionEarlyFreeEgress": econatSessionEarlyFreeEgress,
       "econatSessionAllocNaptOtherErrorEgress": econatSessionAllocNaptOtherErrorEgress,
       "econatSessionAllocNaptTcpErrorEgress": econatSessionAllocNaptTcpErrorEgress,
       "econatSessionAllocNaptUdpErrorEgress": econatSessionAllocNaptUdpErrorEgress,
       "econatSessionAllocNaptIcmpErrorEgress": econatSessionAllocNaptIcmpErrorEgress,
       "econatSessionAllocNaptPptpgreErrorEgress": econatSessionAllocNaptPptpgreErrorEgress,
       "econatSessionAllocNaptL4otherErrorEgress": econatSessionAllocNaptL4otherErrorEgress,
       "econatDroppedPacketCauseL2mtu": econatDroppedPacketCauseL2mtu,
       "econatSessionAllocBnatOtherErrorEgress": econatSessionAllocBnatOtherErrorEgress,
       "econatSessionAllocBnatTcpErrorEgress": econatSessionAllocBnatTcpErrorEgress,
       "econatSessionAllocBnatUdpErrorEgress": econatSessionAllocBnatUdpErrorEgress,
       "econatSessionAllocBnatIcmpErrorEgress": econatSessionAllocBnatIcmpErrorEgress,
       "econatSessionAllocBnatPptpgreErrorEgress": econatSessionAllocBnatPptpgreErrorEgress,
       "econatSessionAllocBnatL4otherErrorEgress": econatSessionAllocBnatL4otherErrorEgress,
       "econatNaptGaddrAllocError": econatNaptGaddrAllocError,
       "econatBnatGaddrAllocError": econatBnatGaddrAllocError,
       "econatBnatPortAllocErrLimitReached": econatBnatPortAllocErrLimitReached,
       "econatBnatPortAllocErrIngressDisabled": econatBnatPortAllocErrIngressDisabled,
       "econatBnatPortAllocErrIngressInactiveClient": econatBnatPortAllocErrIngressInactiveClient,
       "econatBnatPortAllocErrIngressNoClient": econatBnatPortAllocErrIngressNoClient,
       "econatBnatPortAllocErrMappingCreation": econatBnatPortAllocErrMappingCreation,
       "econatBnatPortFreeErrNoMapping": econatBnatPortFreeErrNoMapping,
       "econatBnatPortFreeErrAlreadyZero": econatBnatPortFreeErrAlreadyZero,
       "econatAllocatedLoggerMbufs": econatAllocatedLoggerMbufs,
       "econatAllocatedArpMbufs": econatAllocatedArpMbufs,
       "econatAllocatedLldpMbufs": econatAllocatedLldpMbufs,
       "econatSentLoggerMbufs": econatSentLoggerMbufs,
       "econatSysloggerNoMbufs": econatSysloggerNoMbufs,
       "econatUrllogMsgsEnqueued": econatUrllogMsgsEnqueued,
       "econatUrllogMsgsNotEnqueued": econatUrllogMsgsNotEnqueued,
       "econatRaceNoEgressPayload": econatRaceNoEgressPayload,
       "econatRaceNoIngressPayload": econatRaceNoIngressPayload,
       "econatAlgEnqueued": econatAlgEnqueued,
       "econatAlgRingOverflows": econatAlgRingOverflows,
       "econatAlgHashOverflows": econatAlgHashOverflows,
       "econatAlgFtpPatchDng": econatAlgFtpPatchDng,
       "econatAlgSipPatchDng": econatAlgSipPatchDng,
       "econatAlgRtspPatchDng": econatAlgRtspPatchDng,
       "econatRteHashOverflow": econatRteHashOverflow,
       "econatPsuStateChanges": econatPsuStateChanges,
       "econatHairpinProcess": econatHairpinProcess,
       "econatHairpinRefused": econatHairpinRefused,
       "econatPpFailedSanitycheck": econatPpFailedSanitycheck,
       "econatPpCantccHairpin": econatPpCantccHairpin,
       "econatPpCantccReconfig": econatPpCantccReconfig,
       "econatPpTranslationBug": econatPpTranslationBug,
       "econatPpHairpinRefused": econatPpHairpinRefused,
       "econatPpHairpinRefusedIngress": econatPpHairpinRefusedIngress,
       "econatPpInvalidFlowDrop": econatPpInvalidFlowDrop,
       "econatNaptPortAlloc": econatNaptPortAlloc,
       "econatNaptPortFree": econatNaptPortFree,
       "econatBnatGaddrAlloc": econatBnatGaddrAlloc,
       "econatBnatGaddrFree": econatBnatGaddrFree,
       "econatBnatPortAlloc": econatBnatPortAlloc,
       "econatBnatPortFree": econatBnatPortFree,
       "econatBrasDroppedAccess": econatBrasDroppedAccess,
       "econatBrasDroppedPolicer": econatBrasDroppedPolicer,
       "econatBrasRedirected": econatBrasRedirected,
       "econatDpiBannedEgressTcp": econatDpiBannedEgressTcp,
       "econatDpiBannedIngressTcp": econatDpiBannedIngressTcp,
       "econatDpiBannedEgressUdp": econatDpiBannedEgressUdp,
       "econatDpiBannedIngressUdp": econatDpiBannedIngressUdp,
       "econatDpiRKNLastLoad": econatDpiRKNLastLoad,
       "econatDpiRKNLastParse": econatDpiRKNLastParse,
       "econatDpiNoHostBufs": econatDpiNoHostBufs,
       "econatDpiNoPathBufs": econatDpiNoPathBufs,
       "econatDpiNoStateBufs": econatDpiNoStateBufs,
       "econatTableHash8Ext1": econatTableHash8Ext1,
       "econatTableHash8Ext2": econatTableHash8Ext2,
       "econatTableHash8Ext4": econatTableHash8Ext4,
       "econatTableHash8Ext8": econatTableHash8Ext8,
       "econatTableHash8Ext16": econatTableHash8Ext16,
       "econatTableHash8Overflow": econatTableHash8Overflow,
       "econatTableHash12Ext1": econatTableHash12Ext1,
       "econatTableHash12Ext2": econatTableHash12Ext2,
       "econatTableHash12Ext4": econatTableHash12Ext4,
       "econatTableHash12Ext8": econatTableHash12Ext8,
       "econatTableHash12Ext16": econatTableHash12Ext16,
       "econatTableHash12Overflow": econatTableHash12Overflow,
       "econatTransPerUserLimitExceeded": econatTransPerUserLimitExceeded}
)
