# SNMP MIB module (ARISTA-XGS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-XGS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:46:36 2025
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

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

aristaXgsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26)
)
if mibBuilder.loadTexts:
    aristaXgsMIB.setRevisions(
        ("2020-08-10 00:00",
         "2019-09-27 00:00",
         "2019-01-03 00:00",
         "2018-05-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaXgsMibConformance_ObjectIdentity = ObjectIdentity
aristaXgsMibConformance = _AristaXgsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 1)
)
_AristaXgsMibCompliances_ObjectIdentity = ObjectIdentity
aristaXgsMibCompliances = _AristaXgsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 1, 1)
)
_AristaXgsMibGroups_ObjectIdentity = ObjectIdentity
aristaXgsMibGroups = _AristaXgsMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 1, 2)
)
_AristaXgsQueueWatermarkTable_Object = MibTable
aristaXgsQueueWatermarkTable = _AristaXgsQueueWatermarkTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 2)
)
if mibBuilder.loadTexts:
    aristaXgsQueueWatermarkTable.setStatus("current")
_AristaXgsQueueWatermarkEntry_Object = MibTableRow
aristaXgsQueueWatermarkEntry = _AristaXgsQueueWatermarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 2, 1)
)
aristaXgsQueueWatermarkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARISTA-XGS-MIB", "aristaXgsQueueWatermarkQueueType"),
    (0, "ARISTA-XGS-MIB", "aristaXgsQueueWatermarkQueueId"),
)
if mibBuilder.loadTexts:
    aristaXgsQueueWatermarkEntry.setStatus("current")


class _AristaXgsQueueWatermarkQueueType_Type(Integer32):
    """Custom type aristaXgsQueueWatermarkQueueType based on Integer32"""
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
        *(("ingressHeadroomCells", 1),
          ("ingressSharedCells", 2),
          ("egressUnicastSharedCells", 3),
          ("egressMulticastSharedCells", 4))
    )


_AristaXgsQueueWatermarkQueueType_Type.__name__ = "Integer32"
_AristaXgsQueueWatermarkQueueType_Object = MibTableColumn
aristaXgsQueueWatermarkQueueType = _AristaXgsQueueWatermarkQueueType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 2, 1, 1),
    _AristaXgsQueueWatermarkQueueType_Type()
)
aristaXgsQueueWatermarkQueueType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaXgsQueueWatermarkQueueType.setStatus("current")
_AristaXgsQueueWatermarkQueueId_Type = Unsigned32
_AristaXgsQueueWatermarkQueueId_Object = MibTableColumn
aristaXgsQueueWatermarkQueueId = _AristaXgsQueueWatermarkQueueId_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 2, 1, 2),
    _AristaXgsQueueWatermarkQueueId_Type()
)
aristaXgsQueueWatermarkQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaXgsQueueWatermarkQueueId.setStatus("current")
_AristaXgsQueueWatermarkMaxCellsUsed_Type = Unsigned32
_AristaXgsQueueWatermarkMaxCellsUsed_Object = MibTableColumn
aristaXgsQueueWatermarkMaxCellsUsed = _AristaXgsQueueWatermarkMaxCellsUsed_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 2, 1, 3),
    _AristaXgsQueueWatermarkMaxCellsUsed_Type()
)
aristaXgsQueueWatermarkMaxCellsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsQueueWatermarkMaxCellsUsed.setStatus("current")
_AristaXgsQueueWatermarkCellSize_Type = Unsigned32
_AristaXgsQueueWatermarkCellSize_Object = MibTableColumn
aristaXgsQueueWatermarkCellSize = _AristaXgsQueueWatermarkCellSize_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 2, 1, 4),
    _AristaXgsQueueWatermarkCellSize_Type()
)
aristaXgsQueueWatermarkCellSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsQueueWatermarkCellSize.setStatus("current")
_AristaXgsQueueWatermarkLastResetTime_Type = TimeTicks
_AristaXgsQueueWatermarkLastResetTime_Object = MibTableColumn
aristaXgsQueueWatermarkLastResetTime = _AristaXgsQueueWatermarkLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 2, 1, 5),
    _AristaXgsQueueWatermarkLastResetTime_Type()
)
aristaXgsQueueWatermarkLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsQueueWatermarkLastResetTime.setStatus("current")
_AristaXgsIfTable_Object = MibTable
aristaXgsIfTable = _AristaXgsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3)
)
if mibBuilder.loadTexts:
    aristaXgsIfTable.setStatus("current")
_AristaXgsIfEntry_Object = MibTableRow
aristaXgsIfEntry = _AristaXgsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1)
)
aristaXgsIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aristaXgsIfEntry.setStatus("current")
_AristaXgsIfTxIpV4L3UcOk_Type = Counter64
_AristaXgsIfTxIpV4L3UcOk_Object = MibTableColumn
aristaXgsIfTxIpV4L3UcOk = _AristaXgsIfTxIpV4L3UcOk_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 1),
    _AristaXgsIfTxIpV4L3UcOk_Type()
)
aristaXgsIfTxIpV4L3UcOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfTxIpV4L3UcOk.setStatus("current")
_AristaXgsIfTxIpV6L3UcOk_Type = Counter64
_AristaXgsIfTxIpV6L3UcOk_Object = MibTableColumn
aristaXgsIfTxIpV6L3UcOk = _AristaXgsIfTxIpV6L3UcOk_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 2),
    _AristaXgsIfTxIpV6L3UcOk_Type()
)
aristaXgsIfTxIpV6L3UcOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfTxIpV6L3UcOk.setStatus("current")
_AristaXgsIfTxIpV4L3McOk_Type = Counter64
_AristaXgsIfTxIpV4L3McOk_Object = MibTableColumn
aristaXgsIfTxIpV4L3McOk = _AristaXgsIfTxIpV4L3McOk_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 3),
    _AristaXgsIfTxIpV4L3McOk_Type()
)
aristaXgsIfTxIpV4L3McOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfTxIpV4L3McOk.setStatus("current")
_AristaXgsIfTxIpV6L3McOk_Type = Counter64
_AristaXgsIfTxIpV6L3McOk_Object = MibTableColumn
aristaXgsIfTxIpV6L3McOk = _AristaXgsIfTxIpV6L3McOk_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 4),
    _AristaXgsIfTxIpV6L3McOk_Type()
)
aristaXgsIfTxIpV6L3McOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfTxIpV6L3McOk.setStatus("current")
_AristaXgsIfTxL2MtuError_Type = Counter64
_AristaXgsIfTxL2MtuError_Object = MibTableColumn
aristaXgsIfTxL2MtuError = _AristaXgsIfTxL2MtuError_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 5),
    _AristaXgsIfTxL2MtuError_Type()
)
aristaXgsIfTxL2MtuError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfTxL2MtuError.setStatus("current")
_AristaXgsIfTxL3UcAgedDrop_Type = Counter64
_AristaXgsIfTxL3UcAgedDrop_Object = MibTableColumn
aristaXgsIfTxL3UcAgedDrop = _AristaXgsIfTxL3UcAgedDrop_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 6),
    _AristaXgsIfTxL3UcAgedDrop_Type()
)
aristaXgsIfTxL3UcAgedDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfTxL3UcAgedDrop.setStatus("current")
_AristaXgsIfTxTtlDrop_Type = Counter64
_AristaXgsIfTxTtlDrop_Object = MibTableColumn
aristaXgsIfTxTtlDrop = _AristaXgsIfTxTtlDrop_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 7),
    _AristaXgsIfTxTtlDrop_Type()
)
aristaXgsIfTxTtlDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfTxTtlDrop.setStatus("current")
_AristaXgsIfTxInvalidVlan_Type = Counter64
_AristaXgsIfTxInvalidVlan_Object = MibTableColumn
aristaXgsIfTxInvalidVlan = _AristaXgsIfTxInvalidVlan_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 8),
    _AristaXgsIfTxInvalidVlan_Type()
)
aristaXgsIfTxInvalidVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfTxInvalidVlan.setStatus("current")
_AristaXgsIfTxVxltMiss_Type = Counter64
_AristaXgsIfTxVxltMiss_Object = MibTableColumn
aristaXgsIfTxVxltMiss = _AristaXgsIfTxVxltMiss_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 9),
    _AristaXgsIfTxVxltMiss_Type()
)
aristaXgsIfTxVxltMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfTxVxltMiss.setStatus("current")
_AristaXgsIfTxL2McDrop_Type = Counter64
_AristaXgsIfTxL2McDrop_Object = MibTableColumn
aristaXgsIfTxL2McDrop = _AristaXgsIfTxL2McDrop_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 10),
    _AristaXgsIfTxL2McDrop_Type()
)
aristaXgsIfTxL2McDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfTxL2McDrop.setStatus("current")
_AristaXgsIfTxUnknownDrop_Type = Counter64
_AristaXgsIfTxUnknownDrop_Object = MibTableColumn
aristaXgsIfTxUnknownDrop = _AristaXgsIfTxUnknownDrop_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 11),
    _AristaXgsIfTxUnknownDrop_Type()
)
aristaXgsIfTxUnknownDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfTxUnknownDrop.setStatus("current")
_AristaXgsIfNonCongestionDiscard_Type = Counter64
_AristaXgsIfNonCongestionDiscard_Object = MibTableColumn
aristaXgsIfNonCongestionDiscard = _AristaXgsIfNonCongestionDiscard_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 12),
    _AristaXgsIfNonCongestionDiscard_Type()
)
aristaXgsIfNonCongestionDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfNonCongestionDiscard.setStatus("current")
_AristaXgsIfRxMcDrop_Type = Counter64
_AristaXgsIfRxMcDrop_Object = MibTableColumn
aristaXgsIfRxMcDrop = _AristaXgsIfRxMcDrop_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 13),
    _AristaXgsIfRxMcDrop_Type()
)
aristaXgsIfRxMcDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfRxMcDrop.setStatus("current")
_AristaXgsIfRxTunnelError_Type = Counter64
_AristaXgsIfRxTunnelError_Object = MibTableColumn
aristaXgsIfRxTunnelError = _AristaXgsIfRxTunnelError_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 14),
    _AristaXgsIfRxTunnelError_Type()
)
aristaXgsIfRxTunnelError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfRxTunnelError.setStatus("current")
_AristaXgsIfRxBufferPoolDiscard_Type = Counter64
_AristaXgsIfRxBufferPoolDiscard_Object = MibTableColumn
aristaXgsIfRxBufferPoolDiscard = _AristaXgsIfRxBufferPoolDiscard_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 15),
    _AristaXgsIfRxBufferPoolDiscard_Type()
)
aristaXgsIfRxBufferPoolDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfRxBufferPoolDiscard.setStatus("current")
_AristaXgsIfRxPolicyDiscard_Type = Counter64
_AristaXgsIfRxPolicyDiscard_Object = MibTableColumn
aristaXgsIfRxPolicyDiscard = _AristaXgsIfRxPolicyDiscard_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 16),
    _AristaXgsIfRxPolicyDiscard_Type()
)
aristaXgsIfRxPolicyDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfRxPolicyDiscard.setStatus("current")
_AristaXgsIfRxUrpfDrop_Type = Counter64
_AristaXgsIfRxUrpfDrop_Object = MibTableColumn
aristaXgsIfRxUrpfDrop = _AristaXgsIfRxUrpfDrop_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 17),
    _AristaXgsIfRxUrpfDrop_Type()
)
aristaXgsIfRxUrpfDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfRxUrpfDrop.setStatus("current")
_AristaXgsIfRxVlanDrop_Type = Counter64
_AristaXgsIfRxVlanDrop_Object = MibTableColumn
aristaXgsIfRxVlanDrop = _AristaXgsIfRxVlanDrop_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 18),
    _AristaXgsIfRxVlanDrop_Type()
)
aristaXgsIfRxVlanDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfRxVlanDrop.setStatus("current")
_AristaXgsIfRxFpDrop_Type = Counter64
_AristaXgsIfRxFpDrop_Object = MibTableColumn
aristaXgsIfRxFpDrop = _AristaXgsIfRxFpDrop_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 19),
    _AristaXgsIfRxFpDrop_Type()
)
aristaXgsIfRxFpDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfRxFpDrop.setStatus("current")
_AristaXgsIfRxL2MtuError_Type = Counter64
_AristaXgsIfRxL2MtuError_Object = MibTableColumn
aristaXgsIfRxL2MtuError = _AristaXgsIfRxL2MtuError_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 20),
    _AristaXgsIfRxL2MtuError_Type()
)
aristaXgsIfRxL2MtuError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfRxL2MtuError.setStatus("current")
_AristaXgsIfTxMacError_Type = Counter64
_AristaXgsIfTxMacError_Object = MibTableColumn
aristaXgsIfTxMacError = _AristaXgsIfTxMacError_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 21),
    _AristaXgsIfTxMacError_Type()
)
aristaXgsIfTxMacError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfTxMacError.setStatus("current")
_AristaXgsIfTxPCError_Type = Counter64
_AristaXgsIfTxPCError_Object = MibTableColumn
aristaXgsIfTxPCError = _AristaXgsIfTxPCError_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 22),
    _AristaXgsIfTxPCError_Type()
)
aristaXgsIfTxPCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfTxPCError.setStatus("current")
_AristaXgsIfIpV4L3Discard_Type = Counter64
_AristaXgsIfIpV4L3Discard_Object = MibTableColumn
aristaXgsIfIpV4L3Discard = _AristaXgsIfIpV4L3Discard_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 23),
    _AristaXgsIfIpV4L3Discard_Type()
)
aristaXgsIfIpV4L3Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfIpV4L3Discard.setStatus("current")
_AristaXgsIfIpV4L3Ok_Type = Counter64
_AristaXgsIfIpV4L3Ok_Object = MibTableColumn
aristaXgsIfIpV4L3Ok = _AristaXgsIfIpV4L3Ok_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 24),
    _AristaXgsIfIpV4L3Ok_Type()
)
aristaXgsIfIpV4L3Ok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfIpV4L3Ok.setStatus("current")
_AristaXgsIfIpV4L3HeaderError_Type = Counter64
_AristaXgsIfIpV4L3HeaderError_Object = MibTableColumn
aristaXgsIfIpV4L3HeaderError = _AristaXgsIfIpV4L3HeaderError_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 25),
    _AristaXgsIfIpV4L3HeaderError_Type()
)
aristaXgsIfIpV4L3HeaderError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfIpV4L3HeaderError.setStatus("current")
_AristaXgsIfIpV4L3Mcast_Type = Counter64
_AristaXgsIfIpV4L3Mcast_Object = MibTableColumn
aristaXgsIfIpV4L3Mcast = _AristaXgsIfIpV4L3Mcast_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 26),
    _AristaXgsIfIpV4L3Mcast_Type()
)
aristaXgsIfIpV4L3Mcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfIpV4L3Mcast.setStatus("current")
_AristaXgsIfIpV6L3Discard_Type = Counter64
_AristaXgsIfIpV6L3Discard_Object = MibTableColumn
aristaXgsIfIpV6L3Discard = _AristaXgsIfIpV6L3Discard_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 27),
    _AristaXgsIfIpV6L3Discard_Type()
)
aristaXgsIfIpV6L3Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfIpV6L3Discard.setStatus("current")
_AristaXgsIfIpV6L3Ok_Type = Counter64
_AristaXgsIfIpV6L3Ok_Object = MibTableColumn
aristaXgsIfIpV6L3Ok = _AristaXgsIfIpV6L3Ok_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 28),
    _AristaXgsIfIpV6L3Ok_Type()
)
aristaXgsIfIpV6L3Ok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfIpV6L3Ok.setStatus("current")
_AristaXgsIfIpV6L3HeaderError_Type = Counter64
_AristaXgsIfIpV6L3HeaderError_Object = MibTableColumn
aristaXgsIfIpV6L3HeaderError = _AristaXgsIfIpV6L3HeaderError_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 29),
    _AristaXgsIfIpV6L3HeaderError_Type()
)
aristaXgsIfIpV6L3HeaderError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfIpV6L3HeaderError.setStatus("current")
_AristaXgsIfIpV6L3Mcast_Type = Counter64
_AristaXgsIfIpV6L3Mcast_Object = MibTableColumn
aristaXgsIfIpV6L3Mcast = _AristaXgsIfIpV6L3Mcast_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 30),
    _AristaXgsIfIpV6L3Mcast_Type()
)
aristaXgsIfIpV6L3Mcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfIpV6L3Mcast.setStatus("current")
_AristaXgsIfRxUc_Type = Counter64
_AristaXgsIfRxUc_Object = MibTableColumn
aristaXgsIfRxUc = _AristaXgsIfRxUc_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 31),
    _AristaXgsIfRxUc_Type()
)
aristaXgsIfRxUc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfRxUc.setStatus("current")
_AristaXgsIfRxIngressNfDrop_Type = Counter64
_AristaXgsIfRxIngressNfDrop_Object = MibTableColumn
aristaXgsIfRxIngressNfDrop = _AristaXgsIfRxIngressNfDrop_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 32),
    _AristaXgsIfRxIngressNfDrop_Type()
)
aristaXgsIfRxIngressNfDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfRxIngressNfDrop.setStatus("current")
_AristaXgsIfTxFcsError_Type = Counter64
_AristaXgsIfTxFcsError_Object = MibTableColumn
aristaXgsIfTxFcsError = _AristaXgsIfTxFcsError_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 33),
    _AristaXgsIfTxFcsError_Type()
)
aristaXgsIfTxFcsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfTxFcsError.setStatus("current")
_AristaXgsIfRxAccessPortTrillDiscard_Type = Counter64
_AristaXgsIfRxAccessPortTrillDiscard_Object = MibTableColumn
aristaXgsIfRxAccessPortTrillDiscard = _AristaXgsIfRxAccessPortTrillDiscard_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 34),
    _AristaXgsIfRxAccessPortTrillDiscard_Type()
)
aristaXgsIfRxAccessPortTrillDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfRxAccessPortTrillDiscard.setStatus("current")
_AristaXgsIfRxNetworkPortNonTrillDiscard_Type = Counter64
_AristaXgsIfRxNetworkPortNonTrillDiscard_Object = MibTableColumn
aristaXgsIfRxNetworkPortNonTrillDiscard = _AristaXgsIfRxNetworkPortNonTrillDiscard_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 35),
    _AristaXgsIfRxNetworkPortNonTrillDiscard_Type()
)
aristaXgsIfRxNetworkPortNonTrillDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfRxNetworkPortNonTrillDiscard.setStatus("current")
_AristaXgsIfTxAccessPortTrillDiscard_Type = Counter64
_AristaXgsIfTxAccessPortTrillDiscard_Object = MibTableColumn
aristaXgsIfTxAccessPortTrillDiscard = _AristaXgsIfTxAccessPortTrillDiscard_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 36),
    _AristaXgsIfTxAccessPortTrillDiscard_Type()
)
aristaXgsIfTxAccessPortTrillDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfTxAccessPortTrillDiscard.setStatus("current")
_AristaXgsIfTxNetworkPortNonTrillDiscard_Type = Counter64
_AristaXgsIfTxNetworkPortNonTrillDiscard_Object = MibTableColumn
aristaXgsIfTxNetworkPortNonTrillDiscard = _AristaXgsIfTxNetworkPortNonTrillDiscard_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 37),
    _AristaXgsIfTxNetworkPortNonTrillDiscard_Type()
)
aristaXgsIfTxNetworkPortNonTrillDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfTxNetworkPortNonTrillDiscard.setStatus("current")
_AristaXgsIfEcnMarkedPackets_Type = Counter64
_AristaXgsIfEcnMarkedPackets_Object = MibTableColumn
aristaXgsIfEcnMarkedPackets = _AristaXgsIfEcnMarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 38),
    _AristaXgsIfEcnMarkedPackets_Type()
)
aristaXgsIfEcnMarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfEcnMarkedPackets.setStatus("current")
_AristaXgsIfWredEctDropPktCounter_Type = Counter64
_AristaXgsIfWredEctDropPktCounter_Object = MibTableColumn
aristaXgsIfWredEctDropPktCounter = _AristaXgsIfWredEctDropPktCounter_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 39),
    _AristaXgsIfWredEctDropPktCounter_Type()
)
aristaXgsIfWredEctDropPktCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfWredEctDropPktCounter.setStatus("current")
_AristaXgsIfWredNonEctDropPktCounter_Type = Counter64
_AristaXgsIfWredNonEctDropPktCounter_Object = MibTableColumn
aristaXgsIfWredNonEctDropPktCounter = _AristaXgsIfWredNonEctDropPktCounter_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 40),
    _AristaXgsIfWredNonEctDropPktCounter_Type()
)
aristaXgsIfWredNonEctDropPktCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfWredNonEctDropPktCounter.setStatus("current")
_AristaXgsIfTxSplitHorizonDrop_Type = Counter64
_AristaXgsIfTxSplitHorizonDrop_Object = MibTableColumn
aristaXgsIfTxSplitHorizonDrop = _AristaXgsIfTxSplitHorizonDrop_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 41),
    _AristaXgsIfTxSplitHorizonDrop_Type()
)
aristaXgsIfTxSplitHorizonDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfTxSplitHorizonDrop.setStatus("current")
_AristaXgsIfWredDropPktCounter_Type = Counter64
_AristaXgsIfWredDropPktCounter_Object = MibTableColumn
aristaXgsIfWredDropPktCounter = _AristaXgsIfWredDropPktCounter_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 3, 1, 42),
    _AristaXgsIfWredDropPktCounter_Type()
)
aristaXgsIfWredDropPktCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsIfWredDropPktCounter.setStatus("current")
_AristaXgsNexthopEcmpUnderlayMaxEntries_Type = Unsigned32
_AristaXgsNexthopEcmpUnderlayMaxEntries_Object = MibScalar
aristaXgsNexthopEcmpUnderlayMaxEntries = _AristaXgsNexthopEcmpUnderlayMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 4),
    _AristaXgsNexthopEcmpUnderlayMaxEntries_Type()
)
aristaXgsNexthopEcmpUnderlayMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsNexthopEcmpUnderlayMaxEntries.setStatus("current")
_AristaXgsNexthopEcmpOverlayMaxEntries_Type = Unsigned32
_AristaXgsNexthopEcmpOverlayMaxEntries_Object = MibScalar
aristaXgsNexthopEcmpOverlayMaxEntries = _AristaXgsNexthopEcmpOverlayMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 5),
    _AristaXgsNexthopEcmpOverlayMaxEntries_Type()
)
aristaXgsNexthopEcmpOverlayMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsNexthopEcmpOverlayMaxEntries.setStatus("current")
_AristaXgsNexthopEcmpUnderlayInUseEntries_Type = Unsigned32
_AristaXgsNexthopEcmpUnderlayInUseEntries_Object = MibScalar
aristaXgsNexthopEcmpUnderlayInUseEntries = _AristaXgsNexthopEcmpUnderlayInUseEntries_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 6),
    _AristaXgsNexthopEcmpUnderlayInUseEntries_Type()
)
aristaXgsNexthopEcmpUnderlayInUseEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsNexthopEcmpUnderlayInUseEntries.setStatus("current")
_AristaXgsNexthopEcmpOverlayInUseEntries_Type = Unsigned32
_AristaXgsNexthopEcmpOverlayInUseEntries_Object = MibScalar
aristaXgsNexthopEcmpOverlayInUseEntries = _AristaXgsNexthopEcmpOverlayInUseEntries_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 7),
    _AristaXgsNexthopEcmpOverlayInUseEntries_Type()
)
aristaXgsNexthopEcmpOverlayInUseEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsNexthopEcmpOverlayInUseEntries.setStatus("current")
_AristaXgsNexthopEcmpUnderlayMaxSets_Type = Unsigned32
_AristaXgsNexthopEcmpUnderlayMaxSets_Object = MibScalar
aristaXgsNexthopEcmpUnderlayMaxSets = _AristaXgsNexthopEcmpUnderlayMaxSets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 8),
    _AristaXgsNexthopEcmpUnderlayMaxSets_Type()
)
aristaXgsNexthopEcmpUnderlayMaxSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsNexthopEcmpUnderlayMaxSets.setStatus("current")
_AristaXgsNexthopEcmpOverlayMaxSets_Type = Unsigned32
_AristaXgsNexthopEcmpOverlayMaxSets_Object = MibScalar
aristaXgsNexthopEcmpOverlayMaxSets = _AristaXgsNexthopEcmpOverlayMaxSets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 9),
    _AristaXgsNexthopEcmpOverlayMaxSets_Type()
)
aristaXgsNexthopEcmpOverlayMaxSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsNexthopEcmpOverlayMaxSets.setStatus("current")
_AristaXgsNexthopEcmpUnderlayInUseSets_Type = Unsigned32
_AristaXgsNexthopEcmpUnderlayInUseSets_Object = MibScalar
aristaXgsNexthopEcmpUnderlayInUseSets = _AristaXgsNexthopEcmpUnderlayInUseSets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 10),
    _AristaXgsNexthopEcmpUnderlayInUseSets_Type()
)
aristaXgsNexthopEcmpUnderlayInUseSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsNexthopEcmpUnderlayInUseSets.setStatus("current")
_AristaXgsNexthopEcmpOverlayInUseSets_Type = Unsigned32
_AristaXgsNexthopEcmpOverlayInUseSets_Object = MibScalar
aristaXgsNexthopEcmpOverlayInUseSets = _AristaXgsNexthopEcmpOverlayInUseSets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 11),
    _AristaXgsNexthopEcmpOverlayInUseSets_Type()
)
aristaXgsNexthopEcmpOverlayInUseSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsNexthopEcmpOverlayInUseSets.setStatus("current")
_AristaXgsNexthopEcmpMaxEntries_Type = Unsigned32
_AristaXgsNexthopEcmpMaxEntries_Object = MibScalar
aristaXgsNexthopEcmpMaxEntries = _AristaXgsNexthopEcmpMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 12),
    _AristaXgsNexthopEcmpMaxEntries_Type()
)
aristaXgsNexthopEcmpMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsNexthopEcmpMaxEntries.setStatus("current")
_AristaXgsNexthopEcmpMaxSets_Type = Unsigned32
_AristaXgsNexthopEcmpMaxSets_Object = MibScalar
aristaXgsNexthopEcmpMaxSets = _AristaXgsNexthopEcmpMaxSets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 13),
    _AristaXgsNexthopEcmpMaxSets_Type()
)
aristaXgsNexthopEcmpMaxSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsNexthopEcmpMaxSets.setStatus("current")
_AristaXgsNexthopEcmpInUseEntries_Type = Unsigned32
_AristaXgsNexthopEcmpInUseEntries_Object = MibScalar
aristaXgsNexthopEcmpInUseEntries = _AristaXgsNexthopEcmpInUseEntries_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 14),
    _AristaXgsNexthopEcmpInUseEntries_Type()
)
aristaXgsNexthopEcmpInUseEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsNexthopEcmpInUseEntries.setStatus("current")
_AristaXgsNexthopEcmpInUseSets_Type = Unsigned32
_AristaXgsNexthopEcmpInUseSets_Object = MibScalar
aristaXgsNexthopEcmpInUseSets = _AristaXgsNexthopEcmpInUseSets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 15),
    _AristaXgsNexthopEcmpInUseSets_Type()
)
aristaXgsNexthopEcmpInUseSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsNexthopEcmpInUseSets.setStatus("current")
_AristaXgsCpuQueueStatsTable_Object = MibTable
aristaXgsCpuQueueStatsTable = _AristaXgsCpuQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 16)
)
if mibBuilder.loadTexts:
    aristaXgsCpuQueueStatsTable.setStatus("current")
_AristaXgsCpuQueueStatsEntry_Object = MibTableRow
aristaXgsCpuQueueStatsEntry = _AristaXgsCpuQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 16, 1)
)
aristaXgsCpuQueueStatsEntry.setIndexNames(
    (0, "ARISTA-XGS-MIB", "aristaXgsCpuQueueStatsForwardingElementIdentifier"),
    (0, "ARISTA-XGS-MIB", "aristaXgsCpuQueueStatsQueueIdentifier"),
)
if mibBuilder.loadTexts:
    aristaXgsCpuQueueStatsEntry.setStatus("current")


class _AristaXgsCpuQueueStatsForwardingElementIdentifier_Type(DisplayString):
    """Custom type aristaXgsCpuQueueStatsForwardingElementIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AristaXgsCpuQueueStatsForwardingElementIdentifier_Type.__name__ = "DisplayString"
_AristaXgsCpuQueueStatsForwardingElementIdentifier_Object = MibTableColumn
aristaXgsCpuQueueStatsForwardingElementIdentifier = _AristaXgsCpuQueueStatsForwardingElementIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 16, 1, 1),
    _AristaXgsCpuQueueStatsForwardingElementIdentifier_Type()
)
aristaXgsCpuQueueStatsForwardingElementIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaXgsCpuQueueStatsForwardingElementIdentifier.setStatus("current")


class _AristaXgsCpuQueueStatsQueueIdentifier_Type(DisplayString):
    """Custom type aristaXgsCpuQueueStatsQueueIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AristaXgsCpuQueueStatsQueueIdentifier_Type.__name__ = "DisplayString"
_AristaXgsCpuQueueStatsQueueIdentifier_Object = MibTableColumn
aristaXgsCpuQueueStatsQueueIdentifier = _AristaXgsCpuQueueStatsQueueIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 16, 1, 2),
    _AristaXgsCpuQueueStatsQueueIdentifier_Type()
)
aristaXgsCpuQueueStatsQueueIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaXgsCpuQueueStatsQueueIdentifier.setStatus("current")
_AristaXgsCpuQueueStatsRxBytes_Type = Counter64
_AristaXgsCpuQueueStatsRxBytes_Object = MibTableColumn
aristaXgsCpuQueueStatsRxBytes = _AristaXgsCpuQueueStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 16, 1, 3),
    _AristaXgsCpuQueueStatsRxBytes_Type()
)
aristaXgsCpuQueueStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsCpuQueueStatsRxBytes.setStatus("current")
_AristaXgsCpuQueueStatsRxPackets_Type = Counter64
_AristaXgsCpuQueueStatsRxPackets_Object = MibTableColumn
aristaXgsCpuQueueStatsRxPackets = _AristaXgsCpuQueueStatsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 16, 1, 4),
    _AristaXgsCpuQueueStatsRxPackets_Type()
)
aristaXgsCpuQueueStatsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsCpuQueueStatsRxPackets.setStatus("current")
_AristaXgsCpuQueueStatsRxBytesDropped_Type = Counter64
_AristaXgsCpuQueueStatsRxBytesDropped_Object = MibTableColumn
aristaXgsCpuQueueStatsRxBytesDropped = _AristaXgsCpuQueueStatsRxBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 16, 1, 5),
    _AristaXgsCpuQueueStatsRxBytesDropped_Type()
)
aristaXgsCpuQueueStatsRxBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsCpuQueueStatsRxBytesDropped.setStatus("current")
_AristaXgsCpuQueueStatsRxPacketsDropped_Type = Counter64
_AristaXgsCpuQueueStatsRxPacketsDropped_Object = MibTableColumn
aristaXgsCpuQueueStatsRxPacketsDropped = _AristaXgsCpuQueueStatsRxPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 16, 1, 6),
    _AristaXgsCpuQueueStatsRxPacketsDropped_Type()
)
aristaXgsCpuQueueStatsRxPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXgsCpuQueueStatsRxPacketsDropped.setStatus("current")

# Managed Objects groups

aristaXgsMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 1, 2, 1)
)
aristaXgsMibGroup.setObjects(
      *(("ARISTA-XGS-MIB", "aristaXgsQueueWatermarkMaxCellsUsed"),
        ("ARISTA-XGS-MIB", "aristaXgsQueueWatermarkCellSize"),
        ("ARISTA-XGS-MIB", "aristaXgsQueueWatermarkLastResetTime"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxIpV4L3UcOk"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxIpV6L3UcOk"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxIpV4L3McOk"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxIpV6L3McOk"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxL2MtuError"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxL3UcAgedDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxTtlDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxInvalidVlan"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxVxltMiss"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxL2McDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxUnknownDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfNonCongestionDiscard"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxMcDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxTunnelError"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxBufferPoolDiscard"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxPolicyDiscard"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxUrpfDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxVlanDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxFpDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxL2MtuError"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxMacError"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxPCError"),
        ("ARISTA-XGS-MIB", "aristaXgsIfIpV4L3Discard"),
        ("ARISTA-XGS-MIB", "aristaXgsIfIpV4L3Ok"),
        ("ARISTA-XGS-MIB", "aristaXgsIfIpV4L3HeaderError"),
        ("ARISTA-XGS-MIB", "aristaXgsIfIpV4L3Mcast"),
        ("ARISTA-XGS-MIB", "aristaXgsIfIpV6L3Discard"),
        ("ARISTA-XGS-MIB", "aristaXgsIfIpV6L3Ok"),
        ("ARISTA-XGS-MIB", "aristaXgsIfIpV6L3HeaderError"),
        ("ARISTA-XGS-MIB", "aristaXgsIfIpV6L3Mcast"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxUc"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxIngressNfDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxFcsError"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxAccessPortTrillDiscard"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxNetworkPortNonTrillDiscard"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxAccessPortTrillDiscard"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxNetworkPortNonTrillDiscard"),
        ("ARISTA-XGS-MIB", "aristaXgsIfEcnMarkedPackets"),
        ("ARISTA-XGS-MIB", "aristaXgsIfWredEctDropPktCounter"),
        ("ARISTA-XGS-MIB", "aristaXgsIfWredNonEctDropPktCounter"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxSplitHorizonDrop"))
)
if mibBuilder.loadTexts:
    aristaXgsMibGroup.setStatus("deprecated")

aristaXgsWatermarkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 1, 2, 2)
)
aristaXgsWatermarkGroup.setObjects(
      *(("ARISTA-XGS-MIB", "aristaXgsQueueWatermarkMaxCellsUsed"),
        ("ARISTA-XGS-MIB", "aristaXgsQueueWatermarkCellSize"),
        ("ARISTA-XGS-MIB", "aristaXgsQueueWatermarkLastResetTime"))
)
if mibBuilder.loadTexts:
    aristaXgsWatermarkGroup.setStatus("current")

aristaXgsIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 1, 2, 3)
)
aristaXgsIfGroup.setObjects(
      *(("ARISTA-XGS-MIB", "aristaXgsIfTxIpV4L3UcOk"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxIpV6L3UcOk"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxIpV4L3McOk"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxIpV6L3McOk"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxL2MtuError"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxL3UcAgedDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxTtlDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxInvalidVlan"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxVxltMiss"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxL2McDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxUnknownDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfNonCongestionDiscard"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxMcDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxTunnelError"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxBufferPoolDiscard"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxPolicyDiscard"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxUrpfDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxVlanDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxFpDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxL2MtuError"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxMacError"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxPCError"),
        ("ARISTA-XGS-MIB", "aristaXgsIfIpV4L3Discard"),
        ("ARISTA-XGS-MIB", "aristaXgsIfIpV4L3Ok"),
        ("ARISTA-XGS-MIB", "aristaXgsIfIpV4L3HeaderError"),
        ("ARISTA-XGS-MIB", "aristaXgsIfIpV4L3Mcast"),
        ("ARISTA-XGS-MIB", "aristaXgsIfIpV6L3Discard"),
        ("ARISTA-XGS-MIB", "aristaXgsIfIpV6L3Ok"),
        ("ARISTA-XGS-MIB", "aristaXgsIfIpV6L3HeaderError"),
        ("ARISTA-XGS-MIB", "aristaXgsIfIpV6L3Mcast"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxUc"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxIngressNfDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxFcsError"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxAccessPortTrillDiscard"),
        ("ARISTA-XGS-MIB", "aristaXgsIfRxNetworkPortNonTrillDiscard"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxAccessPortTrillDiscard"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxNetworkPortNonTrillDiscard"),
        ("ARISTA-XGS-MIB", "aristaXgsIfEcnMarkedPackets"),
        ("ARISTA-XGS-MIB", "aristaXgsIfWredEctDropPktCounter"),
        ("ARISTA-XGS-MIB", "aristaXgsIfWredNonEctDropPktCounter"),
        ("ARISTA-XGS-MIB", "aristaXgsIfTxSplitHorizonDrop"),
        ("ARISTA-XGS-MIB", "aristaXgsIfWredDropPktCounter"))
)
if mibBuilder.loadTexts:
    aristaXgsIfGroup.setStatus("current")

aristaXgsNexthopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 1, 2, 4)
)
aristaXgsNexthopGroup.setObjects(
      *(("ARISTA-XGS-MIB", "aristaXgsNexthopEcmpUnderlayMaxEntries"),
        ("ARISTA-XGS-MIB", "aristaXgsNexthopEcmpOverlayMaxEntries"),
        ("ARISTA-XGS-MIB", "aristaXgsNexthopEcmpUnderlayInUseEntries"),
        ("ARISTA-XGS-MIB", "aristaXgsNexthopEcmpOverlayInUseEntries"),
        ("ARISTA-XGS-MIB", "aristaXgsNexthopEcmpUnderlayMaxSets"),
        ("ARISTA-XGS-MIB", "aristaXgsNexthopEcmpOverlayMaxSets"),
        ("ARISTA-XGS-MIB", "aristaXgsNexthopEcmpUnderlayInUseSets"),
        ("ARISTA-XGS-MIB", "aristaXgsNexthopEcmpOverlayInUseSets"),
        ("ARISTA-XGS-MIB", "aristaXgsNexthopEcmpMaxEntries"),
        ("ARISTA-XGS-MIB", "aristaXgsNexthopEcmpMaxSets"),
        ("ARISTA-XGS-MIB", "aristaXgsNexthopEcmpInUseEntries"),
        ("ARISTA-XGS-MIB", "aristaXgsNexthopEcmpInUseSets"))
)
if mibBuilder.loadTexts:
    aristaXgsNexthopGroup.setStatus("current")

aristaXgsCpuQueueStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 1, 2, 5)
)
aristaXgsCpuQueueStatsGroup.setObjects(
      *(("ARISTA-XGS-MIB", "aristaXgsCpuQueueStatsRxBytes"),
        ("ARISTA-XGS-MIB", "aristaXgsCpuQueueStatsRxPackets"),
        ("ARISTA-XGS-MIB", "aristaXgsCpuQueueStatsRxBytesDropped"),
        ("ARISTA-XGS-MIB", "aristaXgsCpuQueueStatsRxPacketsDropped"))
)
if mibBuilder.loadTexts:
    aristaXgsCpuQueueStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaXgsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 1, 1, 1)
)
aristaXgsMibCompliance.setObjects(
    ("ARISTA-XGS-MIB", "aristaXgsMibGroup")
)
if mibBuilder.loadTexts:
    aristaXgsMibCompliance.setStatus(
        "deprecated"
    )

aristaXgsMibCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 26, 1, 1, 2)
)
aristaXgsMibCompliance2.setObjects(
      *(("ARISTA-XGS-MIB", "aristaXgsNexthopGroup"),
        ("ARISTA-XGS-MIB", "aristaXgsWatermarkGroup"),
        ("ARISTA-XGS-MIB", "aristaXgsIfGroup"),
        ("ARISTA-XGS-MIB", "aristaXgsCpuQueueStatsGroup"))
)
if mibBuilder.loadTexts:
    aristaXgsMibCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-XGS-MIB",
    **{"aristaXgsMIB": aristaXgsMIB,
       "aristaXgsMibConformance": aristaXgsMibConformance,
       "aristaXgsMibCompliances": aristaXgsMibCompliances,
       "aristaXgsMibCompliance": aristaXgsMibCompliance,
       "aristaXgsMibCompliance2": aristaXgsMibCompliance2,
       "aristaXgsMibGroups": aristaXgsMibGroups,
       "aristaXgsMibGroup": aristaXgsMibGroup,
       "aristaXgsWatermarkGroup": aristaXgsWatermarkGroup,
       "aristaXgsIfGroup": aristaXgsIfGroup,
       "aristaXgsNexthopGroup": aristaXgsNexthopGroup,
       "aristaXgsCpuQueueStatsGroup": aristaXgsCpuQueueStatsGroup,
       "aristaXgsQueueWatermarkTable": aristaXgsQueueWatermarkTable,
       "aristaXgsQueueWatermarkEntry": aristaXgsQueueWatermarkEntry,
       "aristaXgsQueueWatermarkQueueType": aristaXgsQueueWatermarkQueueType,
       "aristaXgsQueueWatermarkQueueId": aristaXgsQueueWatermarkQueueId,
       "aristaXgsQueueWatermarkMaxCellsUsed": aristaXgsQueueWatermarkMaxCellsUsed,
       "aristaXgsQueueWatermarkCellSize": aristaXgsQueueWatermarkCellSize,
       "aristaXgsQueueWatermarkLastResetTime": aristaXgsQueueWatermarkLastResetTime,
       "aristaXgsIfTable": aristaXgsIfTable,
       "aristaXgsIfEntry": aristaXgsIfEntry,
       "aristaXgsIfTxIpV4L3UcOk": aristaXgsIfTxIpV4L3UcOk,
       "aristaXgsIfTxIpV6L3UcOk": aristaXgsIfTxIpV6L3UcOk,
       "aristaXgsIfTxIpV4L3McOk": aristaXgsIfTxIpV4L3McOk,
       "aristaXgsIfTxIpV6L3McOk": aristaXgsIfTxIpV6L3McOk,
       "aristaXgsIfTxL2MtuError": aristaXgsIfTxL2MtuError,
       "aristaXgsIfTxL3UcAgedDrop": aristaXgsIfTxL3UcAgedDrop,
       "aristaXgsIfTxTtlDrop": aristaXgsIfTxTtlDrop,
       "aristaXgsIfTxInvalidVlan": aristaXgsIfTxInvalidVlan,
       "aristaXgsIfTxVxltMiss": aristaXgsIfTxVxltMiss,
       "aristaXgsIfTxL2McDrop": aristaXgsIfTxL2McDrop,
       "aristaXgsIfTxUnknownDrop": aristaXgsIfTxUnknownDrop,
       "aristaXgsIfNonCongestionDiscard": aristaXgsIfNonCongestionDiscard,
       "aristaXgsIfRxMcDrop": aristaXgsIfRxMcDrop,
       "aristaXgsIfRxTunnelError": aristaXgsIfRxTunnelError,
       "aristaXgsIfRxBufferPoolDiscard": aristaXgsIfRxBufferPoolDiscard,
       "aristaXgsIfRxPolicyDiscard": aristaXgsIfRxPolicyDiscard,
       "aristaXgsIfRxUrpfDrop": aristaXgsIfRxUrpfDrop,
       "aristaXgsIfRxVlanDrop": aristaXgsIfRxVlanDrop,
       "aristaXgsIfRxFpDrop": aristaXgsIfRxFpDrop,
       "aristaXgsIfRxL2MtuError": aristaXgsIfRxL2MtuError,
       "aristaXgsIfTxMacError": aristaXgsIfTxMacError,
       "aristaXgsIfTxPCError": aristaXgsIfTxPCError,
       "aristaXgsIfIpV4L3Discard": aristaXgsIfIpV4L3Discard,
       "aristaXgsIfIpV4L3Ok": aristaXgsIfIpV4L3Ok,
       "aristaXgsIfIpV4L3HeaderError": aristaXgsIfIpV4L3HeaderError,
       "aristaXgsIfIpV4L3Mcast": aristaXgsIfIpV4L3Mcast,
       "aristaXgsIfIpV6L3Discard": aristaXgsIfIpV6L3Discard,
       "aristaXgsIfIpV6L3Ok": aristaXgsIfIpV6L3Ok,
       "aristaXgsIfIpV6L3HeaderError": aristaXgsIfIpV6L3HeaderError,
       "aristaXgsIfIpV6L3Mcast": aristaXgsIfIpV6L3Mcast,
       "aristaXgsIfRxUc": aristaXgsIfRxUc,
       "aristaXgsIfRxIngressNfDrop": aristaXgsIfRxIngressNfDrop,
       "aristaXgsIfTxFcsError": aristaXgsIfTxFcsError,
       "aristaXgsIfRxAccessPortTrillDiscard": aristaXgsIfRxAccessPortTrillDiscard,
       "aristaXgsIfRxNetworkPortNonTrillDiscard": aristaXgsIfRxNetworkPortNonTrillDiscard,
       "aristaXgsIfTxAccessPortTrillDiscard": aristaXgsIfTxAccessPortTrillDiscard,
       "aristaXgsIfTxNetworkPortNonTrillDiscard": aristaXgsIfTxNetworkPortNonTrillDiscard,
       "aristaXgsIfEcnMarkedPackets": aristaXgsIfEcnMarkedPackets,
       "aristaXgsIfWredEctDropPktCounter": aristaXgsIfWredEctDropPktCounter,
       "aristaXgsIfWredNonEctDropPktCounter": aristaXgsIfWredNonEctDropPktCounter,
       "aristaXgsIfTxSplitHorizonDrop": aristaXgsIfTxSplitHorizonDrop,
       "aristaXgsIfWredDropPktCounter": aristaXgsIfWredDropPktCounter,
       "aristaXgsNexthopEcmpUnderlayMaxEntries": aristaXgsNexthopEcmpUnderlayMaxEntries,
       "aristaXgsNexthopEcmpOverlayMaxEntries": aristaXgsNexthopEcmpOverlayMaxEntries,
       "aristaXgsNexthopEcmpUnderlayInUseEntries": aristaXgsNexthopEcmpUnderlayInUseEntries,
       "aristaXgsNexthopEcmpOverlayInUseEntries": aristaXgsNexthopEcmpOverlayInUseEntries,
       "aristaXgsNexthopEcmpUnderlayMaxSets": aristaXgsNexthopEcmpUnderlayMaxSets,
       "aristaXgsNexthopEcmpOverlayMaxSets": aristaXgsNexthopEcmpOverlayMaxSets,
       "aristaXgsNexthopEcmpUnderlayInUseSets": aristaXgsNexthopEcmpUnderlayInUseSets,
       "aristaXgsNexthopEcmpOverlayInUseSets": aristaXgsNexthopEcmpOverlayInUseSets,
       "aristaXgsNexthopEcmpMaxEntries": aristaXgsNexthopEcmpMaxEntries,
       "aristaXgsNexthopEcmpMaxSets": aristaXgsNexthopEcmpMaxSets,
       "aristaXgsNexthopEcmpInUseEntries": aristaXgsNexthopEcmpInUseEntries,
       "aristaXgsNexthopEcmpInUseSets": aristaXgsNexthopEcmpInUseSets,
       "aristaXgsCpuQueueStatsTable": aristaXgsCpuQueueStatsTable,
       "aristaXgsCpuQueueStatsEntry": aristaXgsCpuQueueStatsEntry,
       "aristaXgsCpuQueueStatsForwardingElementIdentifier": aristaXgsCpuQueueStatsForwardingElementIdentifier,
       "aristaXgsCpuQueueStatsQueueIdentifier": aristaXgsCpuQueueStatsQueueIdentifier,
       "aristaXgsCpuQueueStatsRxBytes": aristaXgsCpuQueueStatsRxBytes,
       "aristaXgsCpuQueueStatsRxPackets": aristaXgsCpuQueueStatsRxPackets,
       "aristaXgsCpuQueueStatsRxBytesDropped": aristaXgsCpuQueueStatsRxBytesDropped,
       "aristaXgsCpuQueueStatsRxPacketsDropped": aristaXgsCpuQueueStatsRxPacketsDropped}
)
