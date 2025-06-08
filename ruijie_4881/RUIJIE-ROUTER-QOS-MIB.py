# SNMP MIB module (RUIJIE-ROUTER-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-ROUTER-QOS-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:02:06 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieRouterQoSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106)
)
if mibBuilder.loadTexts:
    ruijieRouterQoSMIB.setRevisions(
        ("2011-12-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RuijieCosType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cos-be", 1),
          ("cos-af1", 2),
          ("cos-af2", 3),
          ("cos-af3", 4),
          ("cos-af4", 5),
          ("cos-ef", 6),
          ("cos-cs6", 7),
          ("cos-cs7", 8))
    )



class RuijieQType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("q-lpq", 1),
          ("q-wfq", 2),
          ("q-pq", 3))
    )



class RuijieQDirectionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("d-input", 1),
          ("d-output", 2))
    )



class RuijieLayerType(TextualConvention, Integer32):
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
        *(("l3-layer", 0),
          ("link-layer", 1),
          ("all-layer", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RuijieCBQoSMIBObjects_ObjectIdentity = ObjectIdentity
ruijieCBQoSMIBObjects = _RuijieCBQoSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1)
)
_RuijieCBQoSIfStaticsObjects_ObjectIdentity = ObjectIdentity
ruijieCBQoSIfStaticsObjects = _RuijieCBQoSIfStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1)
)
_RuijieCBQoSIfCbwfqRunInfoTable_Object = MibTable
ruijieCBQoSIfCbwfqRunInfoTable = _RuijieCBQoSIfCbwfqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieCBQoSIfCbwfqRunInfoTable.setStatus("current")
_RuijieCBQoSIfCbwfqRunInfoEntry_Object = MibTableRow
ruijieCBQoSIfCbwfqRunInfoEntry = _RuijieCBQoSIfCbwfqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 1, 1)
)
ruijieCBQoSIfCbwfqRunInfoEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieCBQoSIfCbwfqPolicyIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieCBQoSIfCbwfqRunInfoEntry.setStatus("current")
_RuijieCBQoSIfCbwfqPolicyIfIndex_Type = Integer32
_RuijieCBQoSIfCbwfqPolicyIfIndex_Object = MibTableColumn
ruijieCBQoSIfCbwfqPolicyIfIndex = _RuijieCBQoSIfCbwfqPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 1, 1, 1),
    _RuijieCBQoSIfCbwfqPolicyIfIndex_Type()
)
ruijieCBQoSIfCbwfqPolicyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCbwfqPolicyIfIndex.setStatus("current")
_RuijieCBQoSIfCbwfqQueueSize_Type = Integer32
_RuijieCBQoSIfCbwfqQueueSize_Object = MibTableColumn
ruijieCBQoSIfCbwfqQueueSize = _RuijieCBQoSIfCbwfqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 1, 1, 2),
    _RuijieCBQoSIfCbwfqQueueSize_Type()
)
ruijieCBQoSIfCbwfqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCbwfqQueueSize.setStatus("current")
_RuijieCBQoSIfCbwfqDiscard_Type = Counter64
_RuijieCBQoSIfCbwfqDiscard_Object = MibTableColumn
ruijieCBQoSIfCbwfqDiscard = _RuijieCBQoSIfCbwfqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 1, 1, 3),
    _RuijieCBQoSIfCbwfqDiscard_Type()
)
ruijieCBQoSIfCbwfqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCbwfqDiscard.setStatus("current")
_RuijieCBQoSIfCbwfqEfQueueSize_Type = Integer32
_RuijieCBQoSIfCbwfqEfQueueSize_Object = MibTableColumn
ruijieCBQoSIfCbwfqEfQueueSize = _RuijieCBQoSIfCbwfqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 1, 1, 4),
    _RuijieCBQoSIfCbwfqEfQueueSize_Type()
)
ruijieCBQoSIfCbwfqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCbwfqEfQueueSize.setStatus("current")
_RuijieCBQoSIfCbwfqAfQueueSize_Type = Integer32
_RuijieCBQoSIfCbwfqAfQueueSize_Object = MibTableColumn
ruijieCBQoSIfCbwfqAfQueueSize = _RuijieCBQoSIfCbwfqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 1, 1, 5),
    _RuijieCBQoSIfCbwfqAfQueueSize_Type()
)
ruijieCBQoSIfCbwfqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCbwfqAfQueueSize.setStatus("current")
_RuijieCBQoSIfCbwfqBeQueueSize_Type = Integer32
_RuijieCBQoSIfCbwfqBeQueueSize_Object = MibTableColumn
ruijieCBQoSIfCbwfqBeQueueSize = _RuijieCBQoSIfCbwfqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 1, 1, 6),
    _RuijieCBQoSIfCbwfqBeQueueSize_Type()
)
ruijieCBQoSIfCbwfqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCbwfqBeQueueSize.setStatus("current")
_RuijieCBQoSIfCbwfqBeActiveQueueNum_Type = Integer32
_RuijieCBQoSIfCbwfqBeActiveQueueNum_Object = MibTableColumn
ruijieCBQoSIfCbwfqBeActiveQueueNum = _RuijieCBQoSIfCbwfqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 1, 1, 7),
    _RuijieCBQoSIfCbwfqBeActiveQueueNum_Type()
)
ruijieCBQoSIfCbwfqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCbwfqBeActiveQueueNum.setStatus("current")
_RuijieCBQoSIfCbwfqBeMaxActiveQueueNum_Type = Integer32
_RuijieCBQoSIfCbwfqBeMaxActiveQueueNum_Object = MibTableColumn
ruijieCBQoSIfCbwfqBeMaxActiveQueueNum = _RuijieCBQoSIfCbwfqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 1, 1, 8),
    _RuijieCBQoSIfCbwfqBeMaxActiveQueueNum_Type()
)
ruijieCBQoSIfCbwfqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCbwfqBeMaxActiveQueueNum.setStatus("current")
_RuijieCBQoSIfCbwfqBeTotalQueueNum_Type = Integer32
_RuijieCBQoSIfCbwfqBeTotalQueueNum_Object = MibTableColumn
ruijieCBQoSIfCbwfqBeTotalQueueNum = _RuijieCBQoSIfCbwfqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 1, 1, 9),
    _RuijieCBQoSIfCbwfqBeTotalQueueNum_Type()
)
ruijieCBQoSIfCbwfqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCbwfqBeTotalQueueNum.setStatus("current")
_RuijieCBQoSIfCbwfqAfAllocatedQueueNum_Type = Integer32
_RuijieCBQoSIfCbwfqAfAllocatedQueueNum_Object = MibTableColumn
ruijieCBQoSIfCbwfqAfAllocatedQueueNum = _RuijieCBQoSIfCbwfqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 1, 1, 10),
    _RuijieCBQoSIfCbwfqAfAllocatedQueueNum_Type()
)
ruijieCBQoSIfCbwfqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCbwfqAfAllocatedQueueNum.setStatus("current")
_RuijieCBQoSIfCbwfqPass_Type = Counter64
_RuijieCBQoSIfCbwfqPass_Object = MibTableColumn
ruijieCBQoSIfCbwfqPass = _RuijieCBQoSIfCbwfqPass_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 1, 1, 11),
    _RuijieCBQoSIfCbwfqPass_Type()
)
ruijieCBQoSIfCbwfqPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCbwfqPass.setStatus("current")


class _RuijieCBQoSIfCbwfqDroppedRateIn5Min_Type(Integer32):
    """Custom type ruijieCBQoSIfCbwfqDroppedRateIn5Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuijieCBQoSIfCbwfqDroppedRateIn5Min_Type.__name__ = "Integer32"
_RuijieCBQoSIfCbwfqDroppedRateIn5Min_Object = MibTableColumn
ruijieCBQoSIfCbwfqDroppedRateIn5Min = _RuijieCBQoSIfCbwfqDroppedRateIn5Min_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 1, 1, 12),
    _RuijieCBQoSIfCbwfqDroppedRateIn5Min_Type()
)
ruijieCBQoSIfCbwfqDroppedRateIn5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCbwfqDroppedRateIn5Min.setStatus("current")
_RuijieCBQoSIfCbwfqPassBytes_Type = Counter64
_RuijieCBQoSIfCbwfqPassBytes_Object = MibTableColumn
ruijieCBQoSIfCbwfqPassBytes = _RuijieCBQoSIfCbwfqPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 1, 1, 13),
    _RuijieCBQoSIfCbwfqPassBytes_Type()
)
ruijieCBQoSIfCbwfqPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCbwfqPassBytes.setStatus("current")
_RuijieCBQoSIfCbwfqDiscardBytes_Type = Counter64
_RuijieCBQoSIfCbwfqDiscardBytes_Object = MibTableColumn
ruijieCBQoSIfCbwfqDiscardBytes = _RuijieCBQoSIfCbwfqDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 1, 1, 14),
    _RuijieCBQoSIfCbwfqDiscardBytes_Type()
)
ruijieCBQoSIfCbwfqDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCbwfqDiscardBytes.setStatus("current")
_RuijieCBQoSIfClassMatchRunInfoTable_Object = MibTable
ruijieCBQoSIfClassMatchRunInfoTable = _RuijieCBQoSIfClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieCBQoSIfClassMatchRunInfoTable.setStatus("current")
_RuijieCBQoSIfClassMatchRunInfoEntry_Object = MibTableRow
ruijieCBQoSIfClassMatchRunInfoEntry = _RuijieCBQoSIfClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 2, 1)
)
ruijieCBQoSIfClassMatchRunInfoEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieCBQoSIfClassMatchIfIndex"),
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieCBQoSIfClassMatchPolicyDirection"),
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieCBQoSIfClassMatchClassIndex"),
)
if mibBuilder.loadTexts:
    ruijieCBQoSIfClassMatchRunInfoEntry.setStatus("current")
_RuijieCBQoSIfClassMatchIfIndex_Type = Integer32
_RuijieCBQoSIfClassMatchIfIndex_Object = MibTableColumn
ruijieCBQoSIfClassMatchIfIndex = _RuijieCBQoSIfClassMatchIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 2, 1, 1),
    _RuijieCBQoSIfClassMatchIfIndex_Type()
)
ruijieCBQoSIfClassMatchIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfClassMatchIfIndex.setStatus("current")


class _RuijieCBQoSIfClassMatchPolicyDirection_Type(Integer32):
    """Custom type ruijieCBQoSIfClassMatchPolicyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_RuijieCBQoSIfClassMatchPolicyDirection_Type.__name__ = "Integer32"
_RuijieCBQoSIfClassMatchPolicyDirection_Object = MibTableColumn
ruijieCBQoSIfClassMatchPolicyDirection = _RuijieCBQoSIfClassMatchPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 2, 1, 2),
    _RuijieCBQoSIfClassMatchPolicyDirection_Type()
)
ruijieCBQoSIfClassMatchPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfClassMatchPolicyDirection.setStatus("current")
_RuijieCBQoSIfClassMatchClassIndex_Type = Integer32
_RuijieCBQoSIfClassMatchClassIndex_Object = MibTableColumn
ruijieCBQoSIfClassMatchClassIndex = _RuijieCBQoSIfClassMatchClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 2, 1, 3),
    _RuijieCBQoSIfClassMatchClassIndex_Type()
)
ruijieCBQoSIfClassMatchClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfClassMatchClassIndex.setStatus("current")
_RuijieCBQoSIfClassMatchedPackets_Type = Counter64
_RuijieCBQoSIfClassMatchedPackets_Object = MibTableColumn
ruijieCBQoSIfClassMatchedPackets = _RuijieCBQoSIfClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 2, 1, 4),
    _RuijieCBQoSIfClassMatchedPackets_Type()
)
ruijieCBQoSIfClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfClassMatchedPackets.setStatus("current")
_RuijieCBQoSIfClassMatchedBytes_Type = Counter64
_RuijieCBQoSIfClassMatchedBytes_Object = MibTableColumn
ruijieCBQoSIfClassMatchedBytes = _RuijieCBQoSIfClassMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 2, 1, 5),
    _RuijieCBQoSIfClassMatchedBytes_Type()
)
ruijieCBQoSIfClassMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfClassMatchedBytes.setStatus("current")
_RuijieCBQosIfClassPassedPackets_Type = Counter64
_RuijieCBQosIfClassPassedPackets_Object = MibTableColumn
ruijieCBQosIfClassPassedPackets = _RuijieCBQosIfClassPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 2, 1, 6),
    _RuijieCBQosIfClassPassedPackets_Type()
)
ruijieCBQosIfClassPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQosIfClassPassedPackets.setStatus("current")
_RuijieCBQosIfClassDroppedPackets_Type = Counter64
_RuijieCBQosIfClassDroppedPackets_Object = MibTableColumn
ruijieCBQosIfClassDroppedPackets = _RuijieCBQosIfClassDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 2, 1, 7),
    _RuijieCBQosIfClassDroppedPackets_Type()
)
ruijieCBQosIfClassDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQosIfClassDroppedPackets.setStatus("current")


class _RuijieCBQoSIfPolicyName_Type(OctetString):
    """Custom type ruijieCBQoSIfPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieCBQoSIfPolicyName_Type.__name__ = "OctetString"
_RuijieCBQoSIfPolicyName_Object = MibTableColumn
ruijieCBQoSIfPolicyName = _RuijieCBQoSIfPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 2, 1, 8),
    _RuijieCBQoSIfPolicyName_Type()
)
ruijieCBQoSIfPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfPolicyName.setStatus("current")


class _RuijieCBQoSIfClassName_Type(OctetString):
    """Custom type ruijieCBQoSIfClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieCBQoSIfClassName_Type.__name__ = "OctetString"
_RuijieCBQoSIfClassName_Object = MibTableColumn
ruijieCBQoSIfClassName = _RuijieCBQoSIfClassName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 2, 1, 9),
    _RuijieCBQoSIfClassName_Type()
)
ruijieCBQoSIfClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfClassName.setStatus("current")
_RuijieCBQoSIfClassPassBytes_Type = Counter64
_RuijieCBQoSIfClassPassBytes_Object = MibTableColumn
ruijieCBQoSIfClassPassBytes = _RuijieCBQoSIfClassPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 2, 1, 10),
    _RuijieCBQoSIfClassPassBytes_Type()
)
ruijieCBQoSIfClassPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfClassPassBytes.setStatus("current")
_RuijieCBQoSIfClassDiscardBytes_Type = Counter64
_RuijieCBQoSIfClassDiscardBytes_Object = MibTableColumn
ruijieCBQoSIfClassDiscardBytes = _RuijieCBQoSIfClassDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 2, 1, 11),
    _RuijieCBQoSIfClassDiscardBytes_Type()
)
ruijieCBQoSIfClassDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfClassDiscardBytes.setStatus("current")
_RuijieCBQoSIfCarRunInfoTable_Object = MibTable
ruijieCBQoSIfCarRunInfoTable = _RuijieCBQoSIfCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieCBQoSIfCarRunInfoTable.setStatus("current")
_RuijieCBQoSIfCarRunInfoEntry_Object = MibTableRow
ruijieCBQoSIfCarRunInfoEntry = _RuijieCBQoSIfCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 3, 1)
)
ruijieCBQoSIfCarRunInfoEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieCBQoSIfCarIfIndex"),
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieCBQoSIfCarPolicyDirection"),
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieCBQoSIfCarClassIndex"),
)
if mibBuilder.loadTexts:
    ruijieCBQoSIfCarRunInfoEntry.setStatus("current")
_RuijieCBQoSIfCarIfIndex_Type = Integer32
_RuijieCBQoSIfCarIfIndex_Object = MibTableColumn
ruijieCBQoSIfCarIfIndex = _RuijieCBQoSIfCarIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 3, 1, 1),
    _RuijieCBQoSIfCarIfIndex_Type()
)
ruijieCBQoSIfCarIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCarIfIndex.setStatus("current")


class _RuijieCBQoSIfCarPolicyDirection_Type(Integer32):
    """Custom type ruijieCBQoSIfCarPolicyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_RuijieCBQoSIfCarPolicyDirection_Type.__name__ = "Integer32"
_RuijieCBQoSIfCarPolicyDirection_Object = MibTableColumn
ruijieCBQoSIfCarPolicyDirection = _RuijieCBQoSIfCarPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 3, 1, 2),
    _RuijieCBQoSIfCarPolicyDirection_Type()
)
ruijieCBQoSIfCarPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCarPolicyDirection.setStatus("current")
_RuijieCBQoSIfCarClassIndex_Type = Integer32
_RuijieCBQoSIfCarClassIndex_Object = MibTableColumn
ruijieCBQoSIfCarClassIndex = _RuijieCBQoSIfCarClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 3, 1, 3),
    _RuijieCBQoSIfCarClassIndex_Type()
)
ruijieCBQoSIfCarClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCarClassIndex.setStatus("current")
_RuijieCBQoSIfCarConformedPackets_Type = Counter64
_RuijieCBQoSIfCarConformedPackets_Object = MibTableColumn
ruijieCBQoSIfCarConformedPackets = _RuijieCBQoSIfCarConformedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 3, 1, 4),
    _RuijieCBQoSIfCarConformedPackets_Type()
)
ruijieCBQoSIfCarConformedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCarConformedPackets.setStatus("current")
_RuijieCBQoSIfCarConformedBytes_Type = Counter64
_RuijieCBQoSIfCarConformedBytes_Object = MibTableColumn
ruijieCBQoSIfCarConformedBytes = _RuijieCBQoSIfCarConformedBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 3, 1, 5),
    _RuijieCBQoSIfCarConformedBytes_Type()
)
ruijieCBQoSIfCarConformedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCarConformedBytes.setStatus("current")
_RuijieCBQoSIfCarExceededPackets_Type = Counter64
_RuijieCBQoSIfCarExceededPackets_Object = MibTableColumn
ruijieCBQoSIfCarExceededPackets = _RuijieCBQoSIfCarExceededPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 3, 1, 6),
    _RuijieCBQoSIfCarExceededPackets_Type()
)
ruijieCBQoSIfCarExceededPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCarExceededPackets.setStatus("current")
_RuijieCBQoSIfCarExceededBytes_Type = Counter64
_RuijieCBQoSIfCarExceededBytes_Object = MibTableColumn
ruijieCBQoSIfCarExceededBytes = _RuijieCBQoSIfCarExceededBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 3, 1, 7),
    _RuijieCBQoSIfCarExceededBytes_Type()
)
ruijieCBQoSIfCarExceededBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCarExceededBytes.setStatus("current")
_RuijieCBQoSIfCarViolatedPackets_Type = Counter64
_RuijieCBQoSIfCarViolatedPackets_Object = MibTableColumn
ruijieCBQoSIfCarViolatedPackets = _RuijieCBQoSIfCarViolatedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 3, 1, 8),
    _RuijieCBQoSIfCarViolatedPackets_Type()
)
ruijieCBQoSIfCarViolatedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCarViolatedPackets.setStatus("current")
_RuijieCBQoSIfCarViolatedBytes_Type = Counter64
_RuijieCBQoSIfCarViolatedBytes_Object = MibTableColumn
ruijieCBQoSIfCarViolatedBytes = _RuijieCBQoSIfCarViolatedBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 3, 1, 9),
    _RuijieCBQoSIfCarViolatedBytes_Type()
)
ruijieCBQoSIfCarViolatedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfCarViolatedBytes.setStatus("current")
_RuijieCBQoSIfRemarkRunInfoTable_Object = MibTable
ruijieCBQoSIfRemarkRunInfoTable = _RuijieCBQoSIfRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieCBQoSIfRemarkRunInfoTable.setStatus("current")
_RuijieCBQoSIfRemarkRunInfoEntry_Object = MibTableRow
ruijieCBQoSIfRemarkRunInfoEntry = _RuijieCBQoSIfRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 4, 1)
)
ruijieCBQoSIfRemarkRunInfoEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieCBQoSIfRemarkIfIndex"),
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieCBQoSIfRemarkPolicyDirection"),
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieCBQoSIfRemarkClassIndex"),
)
if mibBuilder.loadTexts:
    ruijieCBQoSIfRemarkRunInfoEntry.setStatus("current")
_RuijieCBQoSIfRemarkIfIndex_Type = Integer32
_RuijieCBQoSIfRemarkIfIndex_Object = MibTableColumn
ruijieCBQoSIfRemarkIfIndex = _RuijieCBQoSIfRemarkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 4, 1, 1),
    _RuijieCBQoSIfRemarkIfIndex_Type()
)
ruijieCBQoSIfRemarkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfRemarkIfIndex.setStatus("current")


class _RuijieCBQoSIfRemarkPolicyDirection_Type(Integer32):
    """Custom type ruijieCBQoSIfRemarkPolicyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_RuijieCBQoSIfRemarkPolicyDirection_Type.__name__ = "Integer32"
_RuijieCBQoSIfRemarkPolicyDirection_Object = MibTableColumn
ruijieCBQoSIfRemarkPolicyDirection = _RuijieCBQoSIfRemarkPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 4, 1, 2),
    _RuijieCBQoSIfRemarkPolicyDirection_Type()
)
ruijieCBQoSIfRemarkPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfRemarkPolicyDirection.setStatus("current")
_RuijieCBQoSIfRemarkClassIndex_Type = Integer32
_RuijieCBQoSIfRemarkClassIndex_Object = MibTableColumn
ruijieCBQoSIfRemarkClassIndex = _RuijieCBQoSIfRemarkClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 4, 1, 3),
    _RuijieCBQoSIfRemarkClassIndex_Type()
)
ruijieCBQoSIfRemarkClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfRemarkClassIndex.setStatus("current")
_RuijieCBQoSIfRemarkedPackets_Type = Counter64
_RuijieCBQoSIfRemarkedPackets_Object = MibTableColumn
ruijieCBQoSIfRemarkedPackets = _RuijieCBQoSIfRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 4, 1, 4),
    _RuijieCBQoSIfRemarkedPackets_Type()
)
ruijieCBQoSIfRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfRemarkedPackets.setStatus("current")
_RuijieCBQoSIfRemarkedBytes_Type = Counter64
_RuijieCBQoSIfRemarkedBytes_Object = MibTableColumn
ruijieCBQoSIfRemarkedBytes = _RuijieCBQoSIfRemarkedBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 4, 1, 5),
    _RuijieCBQoSIfRemarkedBytes_Type()
)
ruijieCBQoSIfRemarkedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfRemarkedBytes.setStatus("current")
_RuijieCBQoSIfQueueRunInfoTable_Object = MibTable
ruijieCBQoSIfQueueRunInfoTable = _RuijieCBQoSIfQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ruijieCBQoSIfQueueRunInfoTable.setStatus("current")
_RuijieCBQoSIfQueueRunInfoEntry_Object = MibTableRow
ruijieCBQoSIfQueueRunInfoEntry = _RuijieCBQoSIfQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 5, 1)
)
ruijieCBQoSIfQueueRunInfoEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieCBQoSIfQueueIfIndex"),
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieCBQoSIfQueuePolicyDirection"),
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieCBQoSIfQueueClassIndex"),
)
if mibBuilder.loadTexts:
    ruijieCBQoSIfQueueRunInfoEntry.setStatus("current")
_RuijieCBQoSIfQueueIfIndex_Type = Integer32
_RuijieCBQoSIfQueueIfIndex_Object = MibTableColumn
ruijieCBQoSIfQueueIfIndex = _RuijieCBQoSIfQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 5, 1, 1),
    _RuijieCBQoSIfQueueIfIndex_Type()
)
ruijieCBQoSIfQueueIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfQueueIfIndex.setStatus("current")


class _RuijieCBQoSIfQueuePolicyDirection_Type(Integer32):
    """Custom type ruijieCBQoSIfQueuePolicyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_RuijieCBQoSIfQueuePolicyDirection_Type.__name__ = "Integer32"
_RuijieCBQoSIfQueuePolicyDirection_Object = MibTableColumn
ruijieCBQoSIfQueuePolicyDirection = _RuijieCBQoSIfQueuePolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 5, 1, 2),
    _RuijieCBQoSIfQueuePolicyDirection_Type()
)
ruijieCBQoSIfQueuePolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfQueuePolicyDirection.setStatus("current")
_RuijieCBQoSIfQueueClassIndex_Type = Integer32
_RuijieCBQoSIfQueueClassIndex_Object = MibTableColumn
ruijieCBQoSIfQueueClassIndex = _RuijieCBQoSIfQueueClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 5, 1, 3),
    _RuijieCBQoSIfQueueClassIndex_Type()
)
ruijieCBQoSIfQueueClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfQueueClassIndex.setStatus("current")
_RuijieCBQoSIfQueueMatchedPackets_Type = Counter64
_RuijieCBQoSIfQueueMatchedPackets_Object = MibTableColumn
ruijieCBQoSIfQueueMatchedPackets = _RuijieCBQoSIfQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 5, 1, 4),
    _RuijieCBQoSIfQueueMatchedPackets_Type()
)
ruijieCBQoSIfQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfQueueMatchedPackets.setStatus("current")
_RuijieCBQoSIfQueueMatchedBytes_Type = Counter64
_RuijieCBQoSIfQueueMatchedBytes_Object = MibTableColumn
ruijieCBQoSIfQueueMatchedBytes = _RuijieCBQoSIfQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 5, 1, 5),
    _RuijieCBQoSIfQueueMatchedBytes_Type()
)
ruijieCBQoSIfQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfQueueMatchedBytes.setStatus("current")
_RuijieCBQoSIfQueueEnqueuedPackets_Type = Counter64
_RuijieCBQoSIfQueueEnqueuedPackets_Object = MibTableColumn
ruijieCBQoSIfQueueEnqueuedPackets = _RuijieCBQoSIfQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 5, 1, 6),
    _RuijieCBQoSIfQueueEnqueuedPackets_Type()
)
ruijieCBQoSIfQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfQueueEnqueuedPackets.setStatus("current")
_RuijieCBQoSIfQueueEnqueuedBytes_Type = Counter64
_RuijieCBQoSIfQueueEnqueuedBytes_Object = MibTableColumn
ruijieCBQoSIfQueueEnqueuedBytes = _RuijieCBQoSIfQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 5, 1, 7),
    _RuijieCBQoSIfQueueEnqueuedBytes_Type()
)
ruijieCBQoSIfQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfQueueEnqueuedBytes.setStatus("current")
_RuijieCBQoSIfQueueDiscardedPackets_Type = Counter64
_RuijieCBQoSIfQueueDiscardedPackets_Object = MibTableColumn
ruijieCBQoSIfQueueDiscardedPackets = _RuijieCBQoSIfQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 5, 1, 8),
    _RuijieCBQoSIfQueueDiscardedPackets_Type()
)
ruijieCBQoSIfQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfQueueDiscardedPackets.setStatus("current")
_RuijieCBQoSIfQueueDiscardedBytes_Type = Counter64
_RuijieCBQoSIfQueueDiscardedBytes_Object = MibTableColumn
ruijieCBQoSIfQueueDiscardedBytes = _RuijieCBQoSIfQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 5, 1, 9),
    _RuijieCBQoSIfQueueDiscardedBytes_Type()
)
ruijieCBQoSIfQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfQueueDiscardedBytes.setStatus("current")
_RuijieCBQoSIfWredRunInfoTable_Object = MibTable
ruijieCBQoSIfWredRunInfoTable = _RuijieCBQoSIfWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieCBQoSIfWredRunInfoTable.setStatus("current")
_RuijieCBQoSIfWredRunInfoEntry_Object = MibTableRow
ruijieCBQoSIfWredRunInfoEntry = _RuijieCBQoSIfWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 6, 1)
)
ruijieCBQoSIfWredRunInfoEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieCBQoSIfWredIfIndex"),
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieCBQoSIfWredClassIndex"),
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieCBQoSIfWredClassValue"),
)
if mibBuilder.loadTexts:
    ruijieCBQoSIfWredRunInfoEntry.setStatus("current")
_RuijieCBQoSIfWredIfIndex_Type = Integer32
_RuijieCBQoSIfWredIfIndex_Object = MibTableColumn
ruijieCBQoSIfWredIfIndex = _RuijieCBQoSIfWredIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 6, 1, 1),
    _RuijieCBQoSIfWredIfIndex_Type()
)
ruijieCBQoSIfWredIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfWredIfIndex.setStatus("current")
_RuijieCBQoSIfWredClassIndex_Type = Integer32
_RuijieCBQoSIfWredClassIndex_Object = MibTableColumn
ruijieCBQoSIfWredClassIndex = _RuijieCBQoSIfWredClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 6, 1, 2),
    _RuijieCBQoSIfWredClassIndex_Type()
)
ruijieCBQoSIfWredClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfWredClassIndex.setStatus("current")
_RuijieCBQoSIfWredClassValue_Type = Integer32
_RuijieCBQoSIfWredClassValue_Object = MibTableColumn
ruijieCBQoSIfWredClassValue = _RuijieCBQoSIfWredClassValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 6, 1, 3),
    _RuijieCBQoSIfWredClassValue_Type()
)
ruijieCBQoSIfWredClassValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfWredClassValue.setStatus("current")
_RuijieCBQoSIfWredRandomDiscardedPackets_Type = Counter64
_RuijieCBQoSIfWredRandomDiscardedPackets_Object = MibTableColumn
ruijieCBQoSIfWredRandomDiscardedPackets = _RuijieCBQoSIfWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 6, 1, 4),
    _RuijieCBQoSIfWredRandomDiscardedPackets_Type()
)
ruijieCBQoSIfWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfWredRandomDiscardedPackets.setStatus("current")
_RuijieCBQoSIfWredTailDiscardedPackets_Type = Counter64
_RuijieCBQoSIfWredTailDiscardedPackets_Object = MibTableColumn
ruijieCBQoSIfWredTailDiscardedPackets = _RuijieCBQoSIfWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 1, 1, 6, 1, 5),
    _RuijieCBQoSIfWredTailDiscardedPackets_Type()
)
ruijieCBQoSIfWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCBQoSIfWredTailDiscardedPackets.setStatus("current")
_RuijieIfQoSMIBObjects_ObjectIdentity = ObjectIdentity
ruijieIfQoSMIBObjects = _RuijieIfQoSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2)
)
_RuijieIfQosPQRunInfoTable_Object = MibTable
ruijieIfQosPQRunInfoTable = _RuijieIfQosPQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieIfQosPQRunInfoTable.setStatus("current")
_RuijieIfQosPQRunInfoEntry_Object = MibTableRow
ruijieIfQosPQRunInfoEntry = _RuijieIfQosPQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 1, 1)
)
ruijieIfQosPQRunInfoEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieIfQosPQIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfQosPQRunInfoEntry.setStatus("current")
_RuijieIfQosPQIfIndex_Type = Integer32
_RuijieIfQosPQIfIndex_Object = MibTableColumn
ruijieIfQosPQIfIndex = _RuijieIfQosPQIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 1, 1, 1),
    _RuijieIfQosPQIfIndex_Type()
)
ruijieIfQosPQIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosPQIfIndex.setStatus("current")


class _RuijieIfQosPQListNum_Type(Integer32):
    """Custom type ruijieIfQosPQListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RuijieIfQosPQListNum_Type.__name__ = "Integer32"
_RuijieIfQosPQListNum_Object = MibTableColumn
ruijieIfQosPQListNum = _RuijieIfQosPQListNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 1, 1, 2),
    _RuijieIfQosPQListNum_Type()
)
ruijieIfQosPQListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosPQListNum.setStatus("current")
_RuijieIfQosPQIfName_Type = OctetString
_RuijieIfQosPQIfName_Object = MibTableColumn
ruijieIfQosPQIfName = _RuijieIfQosPQIfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 1, 1, 3),
    _RuijieIfQosPQIfName_Type()
)
ruijieIfQosPQIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosPQIfName.setStatus("current")


class _RuijieIfQosPQHighPkt_Type(Integer32):
    """Custom type ruijieIfQosPQHighPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_RuijieIfQosPQHighPkt_Type.__name__ = "Integer32"
_RuijieIfQosPQHighPkt_Object = MibTableColumn
ruijieIfQosPQHighPkt = _RuijieIfQosPQHighPkt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 1, 1, 4),
    _RuijieIfQosPQHighPkt_Type()
)
ruijieIfQosPQHighPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosPQHighPkt.setStatus("current")
_RuijieIfQosPQHighDiscard_Type = Counter32
_RuijieIfQosPQHighDiscard_Object = MibTableColumn
ruijieIfQosPQHighDiscard = _RuijieIfQosPQHighDiscard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 1, 1, 5),
    _RuijieIfQosPQHighDiscard_Type()
)
ruijieIfQosPQHighDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosPQHighDiscard.setStatus("current")


class _RuijieIfQosPQHighMaxQueLen_Type(Integer32):
    """Custom type ruijieIfQosPQHighMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieIfQosPQHighMaxQueLen_Type.__name__ = "Integer32"
_RuijieIfQosPQHighMaxQueLen_Object = MibTableColumn
ruijieIfQosPQHighMaxQueLen = _RuijieIfQosPQHighMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 1, 1, 6),
    _RuijieIfQosPQHighMaxQueLen_Type()
)
ruijieIfQosPQHighMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosPQHighMaxQueLen.setStatus("current")


class _RuijieIfQosPQMiddlePkt_Type(Integer32):
    """Custom type ruijieIfQosPQMiddlePkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_RuijieIfQosPQMiddlePkt_Type.__name__ = "Integer32"
_RuijieIfQosPQMiddlePkt_Object = MibTableColumn
ruijieIfQosPQMiddlePkt = _RuijieIfQosPQMiddlePkt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 1, 1, 7),
    _RuijieIfQosPQMiddlePkt_Type()
)
ruijieIfQosPQMiddlePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosPQMiddlePkt.setStatus("current")
_RuijieIfQosPQMiddleDiscard_Type = Counter32
_RuijieIfQosPQMiddleDiscard_Object = MibTableColumn
ruijieIfQosPQMiddleDiscard = _RuijieIfQosPQMiddleDiscard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 1, 1, 8),
    _RuijieIfQosPQMiddleDiscard_Type()
)
ruijieIfQosPQMiddleDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosPQMiddleDiscard.setStatus("current")


class _RuijieIfQosPQMiddleMaxQueLen_Type(Integer32):
    """Custom type ruijieIfQosPQMiddleMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieIfQosPQMiddleMaxQueLen_Type.__name__ = "Integer32"
_RuijieIfQosPQMiddleMaxQueLen_Object = MibTableColumn
ruijieIfQosPQMiddleMaxQueLen = _RuijieIfQosPQMiddleMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 1, 1, 9),
    _RuijieIfQosPQMiddleMaxQueLen_Type()
)
ruijieIfQosPQMiddleMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosPQMiddleMaxQueLen.setStatus("current")


class _RuijieIfQosPQNormalPkt_Type(Integer32):
    """Custom type ruijieIfQosPQNormalPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_RuijieIfQosPQNormalPkt_Type.__name__ = "Integer32"
_RuijieIfQosPQNormalPkt_Object = MibTableColumn
ruijieIfQosPQNormalPkt = _RuijieIfQosPQNormalPkt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 1, 1, 10),
    _RuijieIfQosPQNormalPkt_Type()
)
ruijieIfQosPQNormalPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosPQNormalPkt.setStatus("current")
_RuijieIfQosPQNormalDiscard_Type = Counter32
_RuijieIfQosPQNormalDiscard_Object = MibTableColumn
ruijieIfQosPQNormalDiscard = _RuijieIfQosPQNormalDiscard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 1, 1, 11),
    _RuijieIfQosPQNormalDiscard_Type()
)
ruijieIfQosPQNormalDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosPQNormalDiscard.setStatus("current")


class _RuijieIfQosPQNormalMaxQueLen_Type(Integer32):
    """Custom type ruijieIfQosPQNormalMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieIfQosPQNormalMaxQueLen_Type.__name__ = "Integer32"
_RuijieIfQosPQNormalMaxQueLen_Object = MibTableColumn
ruijieIfQosPQNormalMaxQueLen = _RuijieIfQosPQNormalMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 1, 1, 12),
    _RuijieIfQosPQNormalMaxQueLen_Type()
)
ruijieIfQosPQNormalMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosPQNormalMaxQueLen.setStatus("current")


class _RuijieIfQosPQLowPkt_Type(Integer32):
    """Custom type ruijieIfQosPQLowPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_RuijieIfQosPQLowPkt_Type.__name__ = "Integer32"
_RuijieIfQosPQLowPkt_Object = MibTableColumn
ruijieIfQosPQLowPkt = _RuijieIfQosPQLowPkt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 1, 1, 13),
    _RuijieIfQosPQLowPkt_Type()
)
ruijieIfQosPQLowPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosPQLowPkt.setStatus("current")
_RuijieIfQosPQLowDiscard_Type = Counter32
_RuijieIfQosPQLowDiscard_Object = MibTableColumn
ruijieIfQosPQLowDiscard = _RuijieIfQosPQLowDiscard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 1, 1, 14),
    _RuijieIfQosPQLowDiscard_Type()
)
ruijieIfQosPQLowDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosPQLowDiscard.setStatus("current")


class _RuijieIfQosPQLowMaxQueLen_Type(Integer32):
    """Custom type ruijieIfQosPQLowMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieIfQosPQLowMaxQueLen_Type.__name__ = "Integer32"
_RuijieIfQosPQLowMaxQueLen_Object = MibTableColumn
ruijieIfQosPQLowMaxQueLen = _RuijieIfQosPQLowMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 1, 1, 15),
    _RuijieIfQosPQLowMaxQueLen_Type()
)
ruijieIfQosPQLowMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosPQLowMaxQueLen.setStatus("current")
_RuijieIfQosCQRunInfoTable_Object = MibTable
ruijieIfQosCQRunInfoTable = _RuijieIfQosCQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 2)
)
if mibBuilder.loadTexts:
    ruijieIfQosCQRunInfoTable.setStatus("current")
_RuijieIfQosCQRunInfoEntry_Object = MibTableRow
ruijieIfQosCQRunInfoEntry = _RuijieIfQosCQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 2, 1)
)
ruijieIfQosCQRunInfoEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieIfQosCQRunInfoIfIndex"),
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieIfQosCQRunInfoQueNum"),
)
if mibBuilder.loadTexts:
    ruijieIfQosCQRunInfoEntry.setStatus("current")
_RuijieIfQosCQRunInfoIfIndex_Type = Integer32
_RuijieIfQosCQRunInfoIfIndex_Object = MibTableColumn
ruijieIfQosCQRunInfoIfIndex = _RuijieIfQosCQRunInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 2, 1, 1),
    _RuijieIfQosCQRunInfoIfIndex_Type()
)
ruijieIfQosCQRunInfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCQRunInfoIfIndex.setStatus("current")


class _RuijieIfQosCQRunInfoQueNum_Type(Integer32):
    """Custom type ruijieIfQosCQRunInfoQueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RuijieIfQosCQRunInfoQueNum_Type.__name__ = "Integer32"
_RuijieIfQosCQRunInfoQueNum_Object = MibTableColumn
ruijieIfQosCQRunInfoQueNum = _RuijieIfQosCQRunInfoQueNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 2, 1, 2),
    _RuijieIfQosCQRunInfoQueNum_Type()
)
ruijieIfQosCQRunInfoQueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCQRunInfoQueNum.setStatus("current")
_RuijieIfQosCQRunInfoIfName_Type = OctetString
_RuijieIfQosCQRunInfoIfName_Object = MibTableColumn
ruijieIfQosCQRunInfoIfName = _RuijieIfQosCQRunInfoIfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 2, 1, 3),
    _RuijieIfQosCQRunInfoIfName_Type()
)
ruijieIfQosCQRunInfoIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCQRunInfoIfName.setStatus("current")


class _RuijieIfQosCQRunInfoQuePkt_Type(Integer32):
    """Custom type ruijieIfQosCQRunInfoQuePkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_RuijieIfQosCQRunInfoQuePkt_Type.__name__ = "Integer32"
_RuijieIfQosCQRunInfoQuePkt_Object = MibTableColumn
ruijieIfQosCQRunInfoQuePkt = _RuijieIfQosCQRunInfoQuePkt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 2, 1, 4),
    _RuijieIfQosCQRunInfoQuePkt_Type()
)
ruijieIfQosCQRunInfoQuePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCQRunInfoQuePkt.setStatus("current")
_RuijieIfQosCQRunInfoQueDiscard_Type = Counter32
_RuijieIfQosCQRunInfoQueDiscard_Object = MibTableColumn
ruijieIfQosCQRunInfoQueDiscard = _RuijieIfQosCQRunInfoQueDiscard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 2, 1, 5),
    _RuijieIfQosCQRunInfoQueDiscard_Type()
)
ruijieIfQosCQRunInfoQueDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCQRunInfoQueDiscard.setStatus("current")


class _RuijieIfQosCQRunInfoMaxQueLen_Type(Integer32):
    """Custom type ruijieIfQosCQRunInfoMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieIfQosCQRunInfoMaxQueLen_Type.__name__ = "Integer32"
_RuijieIfQosCQRunInfoMaxQueLen_Object = MibTableColumn
ruijieIfQosCQRunInfoMaxQueLen = _RuijieIfQosCQRunInfoMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 2, 1, 6),
    _RuijieIfQosCQRunInfoMaxQueLen_Type()
)
ruijieIfQosCQRunInfoMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCQRunInfoMaxQueLen.setStatus("current")
_RuijieIfQosWFQRunInfoTable_Object = MibTable
ruijieIfQosWFQRunInfoTable = _RuijieIfQosWFQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 3)
)
if mibBuilder.loadTexts:
    ruijieIfQosWFQRunInfoTable.setStatus("current")
_RuijieIfQosWFQRunInfoEntry_Object = MibTableRow
ruijieIfQosWFQRunInfoEntry = _RuijieIfQosWFQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 3, 1)
)
ruijieIfQosWFQRunInfoEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieIfQosWFQIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfQosWFQRunInfoEntry.setStatus("current")
_RuijieIfQosWFQIfIndex_Type = Integer32
_RuijieIfQosWFQIfIndex_Object = MibTableColumn
ruijieIfQosWFQIfIndex = _RuijieIfQosWFQIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 3, 1, 1),
    _RuijieIfQosWFQIfIndex_Type()
)
ruijieIfQosWFQIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosWFQIfIndex.setStatus("current")
_RuijieIfQosWFQIfName_Type = OctetString
_RuijieIfQosWFQIfName_Object = MibTableColumn
ruijieIfQosWFQIfName = _RuijieIfQosWFQIfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 3, 1, 2),
    _RuijieIfQosWFQIfName_Type()
)
ruijieIfQosWFQIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosWFQIfName.setStatus("current")


class _RuijieIfQosWFQMaxQueLen_Type(Integer32):
    """Custom type ruijieIfQosWFQMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieIfQosWFQMaxQueLen_Type.__name__ = "Integer32"
_RuijieIfQosWFQMaxQueLen_Object = MibTableColumn
ruijieIfQosWFQMaxQueLen = _RuijieIfQosWFQMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 3, 1, 3),
    _RuijieIfQosWFQMaxQueLen_Type()
)
ruijieIfQosWFQMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosWFQMaxQueLen.setStatus("current")


class _RuijieIfQosWFQTotalQueNum_Type(Integer32):
    """Custom type ruijieIfQosWFQTotalQueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("a16", 16),
          ("a32", 32),
          ("a64", 64),
          ("a128", 128),
          ("a256", 256),
          ("a512", 512),
          ("a1024", 1024),
          ("a2048", 2048),
          ("a4096", 4096))
    )


_RuijieIfQosWFQTotalQueNum_Type.__name__ = "Integer32"
_RuijieIfQosWFQTotalQueNum_Object = MibTableColumn
ruijieIfQosWFQTotalQueNum = _RuijieIfQosWFQTotalQueNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 3, 1, 4),
    _RuijieIfQosWFQTotalQueNum_Type()
)
ruijieIfQosWFQTotalQueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosWFQTotalQueNum.setStatus("current")
_RuijieIfQosWFQCurQueLen_Type = Integer32
_RuijieIfQosWFQCurQueLen_Object = MibTableColumn
ruijieIfQosWFQCurQueLen = _RuijieIfQosWFQCurQueLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 3, 1, 5),
    _RuijieIfQosWFQCurQueLen_Type()
)
ruijieIfQosWFQCurQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosWFQCurQueLen.setStatus("current")
_RuijieIfQosWFQTotalDiscard_Type = Counter32
_RuijieIfQosWFQTotalDiscard_Object = MibTableColumn
ruijieIfQosWFQTotalDiscard = _RuijieIfQosWFQTotalDiscard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 3, 1, 6),
    _RuijieIfQosWFQTotalDiscard_Type()
)
ruijieIfQosWFQTotalDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosWFQTotalDiscard.setStatus("current")


class _RuijieIfQosWFQActiveQueNum_Type(Integer32):
    """Custom type ruijieIfQosWFQActiveQueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_RuijieIfQosWFQActiveQueNum_Type.__name__ = "Integer32"
_RuijieIfQosWFQActiveQueNum_Object = MibTableColumn
ruijieIfQosWFQActiveQueNum = _RuijieIfQosWFQActiveQueNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 3, 1, 7),
    _RuijieIfQosWFQActiveQueNum_Type()
)
ruijieIfQosWFQActiveQueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosWFQActiveQueNum.setStatus("current")


class _RuijieIfQosWFQMaxActiveQueNum_Type(Integer32):
    """Custom type ruijieIfQosWFQMaxActiveQueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_RuijieIfQosWFQMaxActiveQueNum_Type.__name__ = "Integer32"
_RuijieIfQosWFQMaxActiveQueNum_Object = MibTableColumn
ruijieIfQosWFQMaxActiveQueNum = _RuijieIfQosWFQMaxActiveQueNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 3, 1, 8),
    _RuijieIfQosWFQMaxActiveQueNum_Type()
)
ruijieIfQosWFQMaxActiveQueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosWFQMaxActiveQueNum.setStatus("current")
_RuijieIfQosWredRunInfoTable_Object = MibTable
ruijieIfQosWredRunInfoTable = _RuijieIfQosWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 4)
)
if mibBuilder.loadTexts:
    ruijieIfQosWredRunInfoTable.setStatus("current")
_RuijieIfQosWredRunInfoEntry_Object = MibTableRow
ruijieIfQosWredRunInfoEntry = _RuijieIfQosWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 4, 1)
)
ruijieIfQosWredRunInfoEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieIfQosWredIfIndex"),
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieIfQosWredValue"),
)
if mibBuilder.loadTexts:
    ruijieIfQosWredRunInfoEntry.setStatus("current")
_RuijieIfQosWredIfIndex_Type = Integer32
_RuijieIfQosWredIfIndex_Object = MibTableColumn
ruijieIfQosWredIfIndex = _RuijieIfQosWredIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 4, 1, 1),
    _RuijieIfQosWredIfIndex_Type()
)
ruijieIfQosWredIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosWredIfIndex.setStatus("current")
_RuijieIfQosWredValue_Type = Integer32
_RuijieIfQosWredValue_Object = MibTableColumn
ruijieIfQosWredValue = _RuijieIfQosWredValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 4, 1, 2),
    _RuijieIfQosWredValue_Type()
)
ruijieIfQosWredValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosWredValue.setStatus("current")
_RuijieIfQosWredRandomDiscardedPackets_Type = Counter64
_RuijieIfQosWredRandomDiscardedPackets_Object = MibTableColumn
ruijieIfQosWredRandomDiscardedPackets = _RuijieIfQosWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 4, 1, 3),
    _RuijieIfQosWredRandomDiscardedPackets_Type()
)
ruijieIfQosWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosWredRandomDiscardedPackets.setStatus("current")
_RuijieIfQosWredTailDiscardedPackets_Type = Counter64
_RuijieIfQosWredTailDiscardedPackets_Object = MibTableColumn
ruijieIfQosWredTailDiscardedPackets = _RuijieIfQosWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 4, 1, 4),
    _RuijieIfQosWredTailDiscardedPackets_Type()
)
ruijieIfQosWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosWredTailDiscardedPackets.setStatus("current")
_RuijieIfQosCARTable_Object = MibTable
ruijieIfQosCARTable = _RuijieIfQosCARTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5)
)
if mibBuilder.loadTexts:
    ruijieIfQosCARTable.setStatus("current")
_RuijieIfQosCAREntry_Object = MibTableRow
ruijieIfQosCAREntry = _RuijieIfQosCAREntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5, 1)
)
ruijieIfQosCAREntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieIfQosCARIfIndex"),
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieIfQosCARPktDirection"),
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieIfQosCARindex"),
)
if mibBuilder.loadTexts:
    ruijieIfQosCAREntry.setStatus("current")
_RuijieIfQosCARIfIndex_Type = Integer32
_RuijieIfQosCARIfIndex_Object = MibTableColumn
ruijieIfQosCARIfIndex = _RuijieIfQosCARIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5, 1, 1),
    _RuijieIfQosCARIfIndex_Type()
)
ruijieIfQosCARIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCARIfIndex.setStatus("current")
_RuijieIfQosCARIfName_Type = OctetString
_RuijieIfQosCARIfName_Object = MibTableColumn
ruijieIfQosCARIfName = _RuijieIfQosCARIfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5, 1, 2),
    _RuijieIfQosCARIfName_Type()
)
ruijieIfQosCARIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCARIfName.setStatus("current")


class _RuijieIfQosCARPktDirection_Type(Integer32):
    """Custom type ruijieIfQosCARPktDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("outout", 2))
    )


_RuijieIfQosCARPktDirection_Type.__name__ = "Integer32"
_RuijieIfQosCARPktDirection_Object = MibTableColumn
ruijieIfQosCARPktDirection = _RuijieIfQosCARPktDirection_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5, 1, 3),
    _RuijieIfQosCARPktDirection_Type()
)
ruijieIfQosCARPktDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCARPktDirection.setStatus("current")


class _RuijieIfQosCARType_Type(Integer32):
    """Custom type ruijieIfQosCARType based on Integer32"""
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
        *(("acl", 1),
          ("dscp", 2),
          ("qos-group", 3),
          ("default", 4))
    )


_RuijieIfQosCARType_Type.__name__ = "Integer32"
_RuijieIfQosCARType_Object = MibTableColumn
ruijieIfQosCARType = _RuijieIfQosCARType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5, 1, 4),
    _RuijieIfQosCARType_Type()
)
ruijieIfQosCARType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCARType.setStatus("current")
_RuijieIfQosCARListNum_Type = Integer32
_RuijieIfQosCARListNum_Object = MibTableColumn
ruijieIfQosCARListNum = _RuijieIfQosCARListNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5, 1, 5),
    _RuijieIfQosCARListNum_Type()
)
ruijieIfQosCARListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCARListNum.setStatus("current")
_RuijieIfQosCARindex_Type = Integer32
_RuijieIfQosCARindex_Object = MibTableColumn
ruijieIfQosCARindex = _RuijieIfQosCARindex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5, 1, 6),
    _RuijieIfQosCARindex_Type()
)
ruijieIfQosCARindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCARindex.setStatus("current")


class _RuijieIfQosCARCIR_Type(Integer32):
    """Custom type ruijieIfQosCARCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 155000000),
    )


_RuijieIfQosCARCIR_Type.__name__ = "Integer32"
_RuijieIfQosCARCIR_Object = MibTableColumn
ruijieIfQosCARCIR = _RuijieIfQosCARCIR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5, 1, 7),
    _RuijieIfQosCARCIR_Type()
)
ruijieIfQosCARCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCARCIR.setStatus("current")


class _RuijieIfQosCARBurstSize_Type(Integer32):
    """Custom type ruijieIfQosCARBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15000, 155000000),
    )


_RuijieIfQosCARBurstSize_Type.__name__ = "Integer32"
_RuijieIfQosCARBurstSize_Object = MibTableColumn
ruijieIfQosCARBurstSize = _RuijieIfQosCARBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5, 1, 8),
    _RuijieIfQosCARBurstSize_Type()
)
ruijieIfQosCARBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCARBurstSize.setStatus("current")


class _RuijieIfQosCARExcessBurstSize_Type(Integer32):
    """Custom type ruijieIfQosCARExcessBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_RuijieIfQosCARExcessBurstSize_Type.__name__ = "Integer32"
_RuijieIfQosCARExcessBurstSize_Object = MibTableColumn
ruijieIfQosCARExcessBurstSize = _RuijieIfQosCARExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5, 1, 9),
    _RuijieIfQosCARExcessBurstSize_Type()
)
ruijieIfQosCARExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCARExcessBurstSize.setStatus("current")


class _RuijieIfQosCARConformAction_Type(Integer32):
    """Custom type ruijieIfQosCARConformAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("continue", 1),
          ("drop", 2),
          ("set-dscp-continue", 3),
          ("set-dscp-transmit", 4),
          ("set-prec-continue", 5),
          ("set-prec-transmit", 6),
          ("transmit", 7),
          ("set-mpls-exp-continue", 8),
          ("set-mpls-exp-transmit", 9))
    )


_RuijieIfQosCARConformAction_Type.__name__ = "Integer32"
_RuijieIfQosCARConformAction_Object = MibTableColumn
ruijieIfQosCARConformAction = _RuijieIfQosCARConformAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5, 1, 10),
    _RuijieIfQosCARConformAction_Type()
)
ruijieIfQosCARConformAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCARConformAction.setStatus("current")


class _RuijieIfQosCARExceedAction_Type(Integer32):
    """Custom type ruijieIfQosCARExceedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("continue", 1),
          ("drop", 2),
          ("set-dscp-continue", 3),
          ("set-dscp-transmit", 4),
          ("set-prec-continue", 5),
          ("set-prec-transmit", 6),
          ("transmit", 7),
          ("set-mpls-exp-continue", 8),
          ("set-mpls-exp-transmit", 9))
    )


_RuijieIfQosCARExceedAction_Type.__name__ = "Integer32"
_RuijieIfQosCARExceedAction_Object = MibTableColumn
ruijieIfQosCARExceedAction = _RuijieIfQosCARExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5, 1, 11),
    _RuijieIfQosCARExceedAction_Type()
)
ruijieIfQosCARExceedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCARExceedAction.setStatus("current")


class _RuijieIfQosCARConformNewPrec_Type(Integer32):
    """Custom type ruijieIfQosCARConformNewPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieIfQosCARConformNewPrec_Type.__name__ = "Integer32"
_RuijieIfQosCARConformNewPrec_Object = MibTableColumn
ruijieIfQosCARConformNewPrec = _RuijieIfQosCARConformNewPrec_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5, 1, 12),
    _RuijieIfQosCARConformNewPrec_Type()
)
ruijieIfQosCARConformNewPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCARConformNewPrec.setStatus("current")


class _RuijieIfQosCARExceedNewPrec_Type(Integer32):
    """Custom type ruijieIfQosCARExceedNewPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieIfQosCARExceedNewPrec_Type.__name__ = "Integer32"
_RuijieIfQosCARExceedNewPrec_Object = MibTableColumn
ruijieIfQosCARExceedNewPrec = _RuijieIfQosCARExceedNewPrec_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5, 1, 13),
    _RuijieIfQosCARExceedNewPrec_Type()
)
ruijieIfQosCARExceedNewPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCARExceedNewPrec.setStatus("current")
_RuijieIfQosCARConformPkt_Type = Counter32
_RuijieIfQosCARConformPkt_Object = MibTableColumn
ruijieIfQosCARConformPkt = _RuijieIfQosCARConformPkt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5, 1, 14),
    _RuijieIfQosCARConformPkt_Type()
)
ruijieIfQosCARConformPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCARConformPkt.setStatus("current")
_RuijieIfQosCARConformByte_Type = Counter32
_RuijieIfQosCARConformByte_Object = MibTableColumn
ruijieIfQosCARConformByte = _RuijieIfQosCARConformByte_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5, 1, 15),
    _RuijieIfQosCARConformByte_Type()
)
ruijieIfQosCARConformByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCARConformByte.setStatus("current")
_RuijieIfQosCARExceedPkt_Type = Counter32
_RuijieIfQosCARExceedPkt_Object = MibTableColumn
ruijieIfQosCARExceedPkt = _RuijieIfQosCARExceedPkt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5, 1, 16),
    _RuijieIfQosCARExceedPkt_Type()
)
ruijieIfQosCARExceedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCARExceedPkt.setStatus("current")
_RuijieIfQosCARExceedByte_Type = Counter32
_RuijieIfQosCARExceedByte_Object = MibTableColumn
ruijieIfQosCARExceedByte = _RuijieIfQosCARExceedByte_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 5, 1, 17),
    _RuijieIfQosCARExceedByte_Type()
)
ruijieIfQosCARExceedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosCARExceedByte.setStatus("current")
_RuijieIfQosGTSTable_Object = MibTable
ruijieIfQosGTSTable = _RuijieIfQosGTSTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 6)
)
if mibBuilder.loadTexts:
    ruijieIfQosGTSTable.setStatus("current")
_RuijieIfQosGTSEntry_Object = MibTableRow
ruijieIfQosGTSEntry = _RuijieIfQosGTSEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 6, 1)
)
ruijieIfQosGTSEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieIfQosGTSIfIndex"),
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieIfQosGTSType"),
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieIfQosGTSACLNum"),
)
if mibBuilder.loadTexts:
    ruijieIfQosGTSEntry.setStatus("current")
_RuijieIfQosGTSIfIndex_Type = Integer32
_RuijieIfQosGTSIfIndex_Object = MibTableColumn
ruijieIfQosGTSIfIndex = _RuijieIfQosGTSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 6, 1, 1),
    _RuijieIfQosGTSIfIndex_Type()
)
ruijieIfQosGTSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosGTSIfIndex.setStatus("current")
_RuijieIfQosGTSIfName_Type = OctetString
_RuijieIfQosGTSIfName_Object = MibTableColumn
ruijieIfQosGTSIfName = _RuijieIfQosGTSIfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 6, 1, 2),
    _RuijieIfQosGTSIfName_Type()
)
ruijieIfQosGTSIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosGTSIfName.setStatus("current")


class _RuijieIfQosGTSType_Type(Integer32):
    """Custom type ruijieIfQosGTSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acl", 1),
          ("all", 2))
    )


_RuijieIfQosGTSType_Type.__name__ = "Integer32"
_RuijieIfQosGTSType_Object = MibTableColumn
ruijieIfQosGTSType = _RuijieIfQosGTSType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 6, 1, 3),
    _RuijieIfQosGTSType_Type()
)
ruijieIfQosGTSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosGTSType.setStatus("current")


class _RuijieIfQosGTSACLNum_Type(Integer32):
    """Custom type ruijieIfQosGTSACLNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_RuijieIfQosGTSACLNum_Type.__name__ = "Integer32"
_RuijieIfQosGTSACLNum_Object = MibTableColumn
ruijieIfQosGTSACLNum = _RuijieIfQosGTSACLNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 6, 1, 4),
    _RuijieIfQosGTSACLNum_Type()
)
ruijieIfQosGTSACLNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosGTSACLNum.setStatus("current")


class _RuijieIfQosGTSCIR_Type(Integer32):
    """Custom type ruijieIfQosGTSCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 155000000),
    )


_RuijieIfQosGTSCIR_Type.__name__ = "Integer32"
_RuijieIfQosGTSCIR_Object = MibTableColumn
ruijieIfQosGTSCIR = _RuijieIfQosGTSCIR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 6, 1, 5),
    _RuijieIfQosGTSCIR_Type()
)
ruijieIfQosGTSCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosGTSCIR.setStatus("current")


class _RuijieIfQosGTSBurstSize_Type(Integer32):
    """Custom type ruijieIfQosGTSBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15000, 155000000),
    )


_RuijieIfQosGTSBurstSize_Type.__name__ = "Integer32"
_RuijieIfQosGTSBurstSize_Object = MibTableColumn
ruijieIfQosGTSBurstSize = _RuijieIfQosGTSBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 6, 1, 6),
    _RuijieIfQosGTSBurstSize_Type()
)
ruijieIfQosGTSBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosGTSBurstSize.setStatus("current")


class _RuijieIfQosGTSExcessBurstSize_Type(Integer32):
    """Custom type ruijieIfQosGTSExcessBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_RuijieIfQosGTSExcessBurstSize_Type.__name__ = "Integer32"
_RuijieIfQosGTSExcessBurstSize_Object = MibTableColumn
ruijieIfQosGTSExcessBurstSize = _RuijieIfQosGTSExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 6, 1, 7),
    _RuijieIfQosGTSExcessBurstSize_Type()
)
ruijieIfQosGTSExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosGTSExcessBurstSize.setStatus("current")


class _RuijieIfQosGTSMaxQueLen_Type(Integer32):
    """Custom type ruijieIfQosGTSMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieIfQosGTSMaxQueLen_Type.__name__ = "Integer32"
_RuijieIfQosGTSMaxQueLen_Object = MibTableColumn
ruijieIfQosGTSMaxQueLen = _RuijieIfQosGTSMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 6, 1, 8),
    _RuijieIfQosGTSMaxQueLen_Type()
)
ruijieIfQosGTSMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosGTSMaxQueLen.setStatus("current")
_RuijieIfQosGTSCurQueLen_Type = Integer32
_RuijieIfQosGTSCurQueLen_Object = MibTableColumn
ruijieIfQosGTSCurQueLen = _RuijieIfQosGTSCurQueLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 6, 1, 9),
    _RuijieIfQosGTSCurQueLen_Type()
)
ruijieIfQosGTSCurQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosGTSCurQueLen.setStatus("current")
_RuijieIfQosGTSPassPkt_Type = Counter32
_RuijieIfQosGTSPassPkt_Object = MibTableColumn
ruijieIfQosGTSPassPkt = _RuijieIfQosGTSPassPkt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 6, 1, 10),
    _RuijieIfQosGTSPassPkt_Type()
)
ruijieIfQosGTSPassPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosGTSPassPkt.setStatus("current")
_RuijieIfQosGTSPassByte_Type = Counter32
_RuijieIfQosGTSPassByte_Object = MibTableColumn
ruijieIfQosGTSPassByte = _RuijieIfQosGTSPassByte_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 6, 1, 11),
    _RuijieIfQosGTSPassByte_Type()
)
ruijieIfQosGTSPassByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosGTSPassByte.setStatus("current")
_RuijieIfQosGTSDiscardPkt_Type = Counter32
_RuijieIfQosGTSDiscardPkt_Object = MibTableColumn
ruijieIfQosGTSDiscardPkt = _RuijieIfQosGTSDiscardPkt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 6, 1, 12),
    _RuijieIfQosGTSDiscardPkt_Type()
)
ruijieIfQosGTSDiscardPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosGTSDiscardPkt.setStatus("current")
_RuijieIfQosGTSDiscardByte_Type = Counter32
_RuijieIfQosGTSDiscardByte_Object = MibTableColumn
ruijieIfQosGTSDiscardByte = _RuijieIfQosGTSDiscardByte_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 6, 1, 13),
    _RuijieIfQosGTSDiscardByte_Type()
)
ruijieIfQosGTSDiscardByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosGTSDiscardByte.setStatus("current")
_RuijieIfQosRTPIfQueueRunInfoTable_Object = MibTable
ruijieIfQosRTPIfQueueRunInfoTable = _RuijieIfQosRTPIfQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 7)
)
if mibBuilder.loadTexts:
    ruijieIfQosRTPIfQueueRunInfoTable.setStatus("current")
_RuijieIfQosRTPIfQueueRunInfoEntry_Object = MibTableRow
ruijieIfQosRTPIfQueueRunInfoEntry = _RuijieIfQosRTPIfQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 7, 1)
)
ruijieIfQosRTPIfQueueRunInfoEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieIfQosRTPIfApplyIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfQosRTPIfQueueRunInfoEntry.setStatus("current")
_RuijieIfQosRTPIfApplyIfIndex_Type = Integer32
_RuijieIfQosRTPIfApplyIfIndex_Object = MibTableColumn
ruijieIfQosRTPIfApplyIfIndex = _RuijieIfQosRTPIfApplyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 7, 1, 1),
    _RuijieIfQosRTPIfApplyIfIndex_Type()
)
ruijieIfQosRTPIfApplyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosRTPIfApplyIfIndex.setStatus("current")
_RuijieIfQosRTPIfQueueSize_Type = Counter32
_RuijieIfQosRTPIfQueueSize_Object = MibTableColumn
ruijieIfQosRTPIfQueueSize = _RuijieIfQosRTPIfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 7, 1, 2),
    _RuijieIfQosRTPIfQueueSize_Type()
)
ruijieIfQosRTPIfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosRTPIfQueueSize.setStatus("current")
_RuijieIfQosRTPIfQueueMaxSize_Type = Counter32
_RuijieIfQosRTPIfQueueMaxSize_Object = MibTableColumn
ruijieIfQosRTPIfQueueMaxSize = _RuijieIfQosRTPIfQueueMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 7, 1, 3),
    _RuijieIfQosRTPIfQueueMaxSize_Type()
)
ruijieIfQosRTPIfQueueMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosRTPIfQueueMaxSize.setStatus("current")
_RuijieIfQosRTPIfQueueOutputs_Type = Counter32
_RuijieIfQosRTPIfQueueOutputs_Object = MibTableColumn
ruijieIfQosRTPIfQueueOutputs = _RuijieIfQosRTPIfQueueOutputs_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 7, 1, 4),
    _RuijieIfQosRTPIfQueueOutputs_Type()
)
ruijieIfQosRTPIfQueueOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosRTPIfQueueOutputs.setStatus("current")
_RuijieIfQosRTPIfQueueDiscards_Type = Counter32
_RuijieIfQosRTPIfQueueDiscards_Object = MibTableColumn
ruijieIfQosRTPIfQueueDiscards = _RuijieIfQosRTPIfQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 7, 1, 5),
    _RuijieIfQosRTPIfQueueDiscards_Type()
)
ruijieIfQosRTPIfQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosRTPIfQueueDiscards.setStatus("current")
_RuijieIfQosFlowLimitRunInfoTable_Object = MibTable
ruijieIfQosFlowLimitRunInfoTable = _RuijieIfQosFlowLimitRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 8)
)
if mibBuilder.loadTexts:
    ruijieIfQosFlowLimitRunInfoTable.setStatus("current")
_RuijieIfQosFlowLimitRunInfoEntry_Object = MibTableRow
ruijieIfQosFlowLimitRunInfoEntry = _RuijieIfQosFlowLimitRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 8, 1)
)
ruijieIfQosFlowLimitRunInfoEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieIfQosFlowLimitLabelNum"),
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieIfQosFlowLimitPktDirection"),
)
if mibBuilder.loadTexts:
    ruijieIfQosFlowLimitRunInfoEntry.setStatus("current")


class _RuijieIfQosFlowLimitLabelNum_Type(Integer32):
    """Custom type ruijieIfQosFlowLimitLabelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RuijieIfQosFlowLimitLabelNum_Type.__name__ = "Integer32"
_RuijieIfQosFlowLimitLabelNum_Object = MibTableColumn
ruijieIfQosFlowLimitLabelNum = _RuijieIfQosFlowLimitLabelNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 8, 1, 1),
    _RuijieIfQosFlowLimitLabelNum_Type()
)
ruijieIfQosFlowLimitLabelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosFlowLimitLabelNum.setStatus("current")


class _RuijieIfQosFlowLimitPktDirection_Type(Integer32):
    """Custom type ruijieIfQosFlowLimitPktDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_RuijieIfQosFlowLimitPktDirection_Type.__name__ = "Integer32"
_RuijieIfQosFlowLimitPktDirection_Object = MibTableColumn
ruijieIfQosFlowLimitPktDirection = _RuijieIfQosFlowLimitPktDirection_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 8, 1, 2),
    _RuijieIfQosFlowLimitPktDirection_Type()
)
ruijieIfQosFlowLimitPktDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosFlowLimitPktDirection.setStatus("current")


class _RuijieIfQosFlowLimitCIR_Type(Integer32):
    """Custom type ruijieIfQosFlowLimitCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 155000000),
    )


_RuijieIfQosFlowLimitCIR_Type.__name__ = "Integer32"
_RuijieIfQosFlowLimitCIR_Object = MibTableColumn
ruijieIfQosFlowLimitCIR = _RuijieIfQosFlowLimitCIR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 8, 1, 3),
    _RuijieIfQosFlowLimitCIR_Type()
)
ruijieIfQosFlowLimitCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosFlowLimitCIR.setStatus("current")


class _RuijieIfQosFlowLimitBurstSize_Type(Integer32):
    """Custom type ruijieIfQosFlowLimitBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15000, 155000000),
    )


_RuijieIfQosFlowLimitBurstSize_Type.__name__ = "Integer32"
_RuijieIfQosFlowLimitBurstSize_Object = MibTableColumn
ruijieIfQosFlowLimitBurstSize = _RuijieIfQosFlowLimitBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 8, 1, 4),
    _RuijieIfQosFlowLimitBurstSize_Type()
)
ruijieIfQosFlowLimitBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosFlowLimitBurstSize.setStatus("current")


class _RuijieIfQosFlowLimitExcessBurstSize_Type(Integer32):
    """Custom type ruijieIfQosFlowLimitExcessBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_RuijieIfQosFlowLimitExcessBurstSize_Type.__name__ = "Integer32"
_RuijieIfQosFlowLimitExcessBurstSize_Object = MibTableColumn
ruijieIfQosFlowLimitExcessBurstSize = _RuijieIfQosFlowLimitExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 8, 1, 5),
    _RuijieIfQosFlowLimitExcessBurstSize_Type()
)
ruijieIfQosFlowLimitExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosFlowLimitExcessBurstSize.setStatus("current")


class _RuijieIfQosFlowLimitConformAction_Type(Integer32):
    """Custom type ruijieIfQosFlowLimitConformAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("continue", 1),
          ("drop", 2),
          ("set-dscp-continue", 3),
          ("set-dscp-transmit", 4),
          ("set-prec-continue", 5),
          ("set-prec-transmit", 6),
          ("transmit", 7),
          ("set-mpls-exp-continue", 8),
          ("set-mpls-exp-transmit", 9))
    )


_RuijieIfQosFlowLimitConformAction_Type.__name__ = "Integer32"
_RuijieIfQosFlowLimitConformAction_Object = MibTableColumn
ruijieIfQosFlowLimitConformAction = _RuijieIfQosFlowLimitConformAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 8, 1, 6),
    _RuijieIfQosFlowLimitConformAction_Type()
)
ruijieIfQosFlowLimitConformAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosFlowLimitConformAction.setStatus("current")


class _RuijieIfQosFlowLimitExceedAction_Type(Integer32):
    """Custom type ruijieIfQosFlowLimitExceedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("continue", 1),
          ("drop", 2),
          ("set-dscp-continue", 3),
          ("set-dscp-transmit", 4),
          ("set-prec-continue", 5),
          ("set-prec-transmit", 6),
          ("transmit", 7),
          ("set-mpls-exp-continue", 8),
          ("set-mpls-exp-transmit", 9))
    )


_RuijieIfQosFlowLimitExceedAction_Type.__name__ = "Integer32"
_RuijieIfQosFlowLimitExceedAction_Object = MibTableColumn
ruijieIfQosFlowLimitExceedAction = _RuijieIfQosFlowLimitExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 8, 1, 7),
    _RuijieIfQosFlowLimitExceedAction_Type()
)
ruijieIfQosFlowLimitExceedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosFlowLimitExceedAction.setStatus("current")


class _RuijieIfQosFlowLimitConformNewPrec_Type(Integer32):
    """Custom type ruijieIfQosFlowLimitConformNewPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RuijieIfQosFlowLimitConformNewPrec_Type.__name__ = "Integer32"
_RuijieIfQosFlowLimitConformNewPrec_Object = MibTableColumn
ruijieIfQosFlowLimitConformNewPrec = _RuijieIfQosFlowLimitConformNewPrec_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 8, 1, 8),
    _RuijieIfQosFlowLimitConformNewPrec_Type()
)
ruijieIfQosFlowLimitConformNewPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosFlowLimitConformNewPrec.setStatus("current")


class _RuijieIfQosFlowLimitExceedNewPrec_Type(Integer32):
    """Custom type ruijieIfQosFlowLimitExceedNewPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RuijieIfQosFlowLimitExceedNewPrec_Type.__name__ = "Integer32"
_RuijieIfQosFlowLimitExceedNewPrec_Object = MibTableColumn
ruijieIfQosFlowLimitExceedNewPrec = _RuijieIfQosFlowLimitExceedNewPrec_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 8, 1, 9),
    _RuijieIfQosFlowLimitExceedNewPrec_Type()
)
ruijieIfQosFlowLimitExceedNewPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosFlowLimitExceedNewPrec.setStatus("current")
_RuijieIfQosFlowLimitConformPkt_Type = Counter32
_RuijieIfQosFlowLimitConformPkt_Object = MibTableColumn
ruijieIfQosFlowLimitConformPkt = _RuijieIfQosFlowLimitConformPkt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 8, 1, 10),
    _RuijieIfQosFlowLimitConformPkt_Type()
)
ruijieIfQosFlowLimitConformPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosFlowLimitConformPkt.setStatus("current")
_RuijieIfQosFlowLimitConformByte_Type = Counter32
_RuijieIfQosFlowLimitConformByte_Object = MibTableColumn
ruijieIfQosFlowLimitConformByte = _RuijieIfQosFlowLimitConformByte_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 8, 1, 11),
    _RuijieIfQosFlowLimitConformByte_Type()
)
ruijieIfQosFlowLimitConformByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosFlowLimitConformByte.setStatus("current")
_RuijieIfQosFlowLimitExceedPkt_Type = Counter32
_RuijieIfQosFlowLimitExceedPkt_Object = MibTableColumn
ruijieIfQosFlowLimitExceedPkt = _RuijieIfQosFlowLimitExceedPkt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 8, 1, 12),
    _RuijieIfQosFlowLimitExceedPkt_Type()
)
ruijieIfQosFlowLimitExceedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosFlowLimitExceedPkt.setStatus("current")
_RuijieIfQosFlowLimitExceedByte_Type = Counter32
_RuijieIfQosFlowLimitExceedByte_Object = MibTableColumn
ruijieIfQosFlowLimitExceedByte = _RuijieIfQosFlowLimitExceedByte_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 2, 8, 1, 13),
    _RuijieIfQosFlowLimitExceedByte_Type()
)
ruijieIfQosFlowLimitExceedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQosFlowLimitExceedByte.setStatus("current")
_RuijieHQoSMIBObjects_ObjectIdentity = ObjectIdentity
ruijieHQoSMIBObjects = _RuijieHQoSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3)
)
_RuijieHQoSScalarObjects_ObjectIdentity = ObjectIdentity
ruijieHQoSScalarObjects = _RuijieHQoSScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 1)
)


class _RuijieHQoSNameType_Type(Integer32):
    """Custom type ruijieHQoSNameType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknownName", 0),
          ("userQNameIn", 1),
          ("userQNameOut", 2),
          ("userGroupQInName", 3),
          ("userGroupQOutName", 4),
          ("flowQName", 5),
          ("flowMapName", 6),
          ("trafficClassifierName", 7),
          ("trafficBehaviorName", 8),
          ("trafficPolicyName", 9),
          ("portQName", 10))
    )


_RuijieHQoSNameType_Type.__name__ = "Integer32"
_RuijieHQoSNameType_Object = MibScalar
ruijieHQoSNameType = _RuijieHQoSNameType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 1, 1),
    _RuijieHQoSNameType_Type()
)
ruijieHQoSNameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieHQoSNameType.setStatus("current")


class _RuijieHQoSNameFind_Type(OctetString):
    """Custom type ruijieHQoSNameFind based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSNameFind_Type.__name__ = "OctetString"
_RuijieHQoSNameFind_Object = MibScalar
ruijieHQoSNameFind = _RuijieHQoSNameFind_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 1, 2),
    _RuijieHQoSNameFind_Type()
)
ruijieHQoSNameFind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieHQoSNameFind.setStatus("current")


class _RuijieHQoSNameIndex_Type(Integer32):
    """Custom type ruijieHQoSNameIndex based on Integer32"""
    defaultValue = 0


_RuijieHQoSNameIndex_Type.__name__ = "Integer32"
_RuijieHQoSNameIndex_Object = MibScalar
ruijieHQoSNameIndex = _RuijieHQoSNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 1, 3),
    _RuijieHQoSNameIndex_Type()
)
ruijieHQoSNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHQoSNameIndex.setStatus("current")
_RuijieHQoSUserQObjects_ObjectIdentity = ObjectIdentity
ruijieHQoSUserQObjects = _RuijieHQoSUserQObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 2)
)
_RuijieHQoSUserQInIndexNext_Type = Integer32
_RuijieHQoSUserQInIndexNext_Object = MibScalar
ruijieHQoSUserQInIndexNext = _RuijieHQoSUserQInIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 2, 1),
    _RuijieHQoSUserQInIndexNext_Type()
)
ruijieHQoSUserQInIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHQoSUserQInIndexNext.setStatus("current")
_RuijieHQoSUserQOutIndexNext_Type = Integer32
_RuijieHQoSUserQOutIndexNext_Object = MibScalar
ruijieHQoSUserQOutIndexNext = _RuijieHQoSUserQOutIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 2, 2),
    _RuijieHQoSUserQOutIndexNext_Type()
)
ruijieHQoSUserQOutIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHQoSUserQOutIndexNext.setStatus("current")
_RuijieHQoSUserQTable_Object = MibTable
ruijieHQoSUserQTable = _RuijieHQoSUserQTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 2, 3)
)
if mibBuilder.loadTexts:
    ruijieHQoSUserQTable.setStatus("current")
_RuijieHQoSUserQEntry_Object = MibTableRow
ruijieHQoSUserQEntry = _RuijieHQoSUserQEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 2, 3, 1)
)
ruijieHQoSUserQEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieHQoSUserQIndex"),
)
if mibBuilder.loadTexts:
    ruijieHQoSUserQEntry.setStatus("current")
_RuijieHQoSUserQIndex_Type = Unsigned32
_RuijieHQoSUserQIndex_Object = MibTableColumn
ruijieHQoSUserQIndex = _RuijieHQoSUserQIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 2, 3, 1, 1),
    _RuijieHQoSUserQIndex_Type()
)
ruijieHQoSUserQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieHQoSUserQIndex.setStatus("current")


class _RuijieHQoSUserQName_Type(OctetString):
    """Custom type ruijieHQoSUserQName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSUserQName_Type.__name__ = "OctetString"
_RuijieHQoSUserQName_Object = MibTableColumn
ruijieHQoSUserQName = _RuijieHQoSUserQName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 2, 3, 1, 2),
    _RuijieHQoSUserQName_Type()
)
ruijieHQoSUserQName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSUserQName.setStatus("current")
_RuijieHQoSUserQDirection_Type = RuijieQDirectionType
_RuijieHQoSUserQDirection_Object = MibTableColumn
ruijieHQoSUserQDirection = _RuijieHQoSUserQDirection_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 2, 3, 1, 3),
    _RuijieHQoSUserQDirection_Type()
)
ruijieHQoSUserQDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSUserQDirection.setStatus("current")
_RuijieHQoSUserQRowStatus_Type = RowStatus
_RuijieHQoSUserQRowStatus_Object = MibTableColumn
ruijieHQoSUserQRowStatus = _RuijieHQoSUserQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 2, 3, 1, 4),
    _RuijieHQoSUserQRowStatus_Type()
)
ruijieHQoSUserQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSUserQRowStatus.setStatus("current")


class _RuijieHQoSUserQFlowQName_Type(OctetString):
    """Custom type ruijieHQoSUserQFlowQName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSUserQFlowQName_Type.__name__ = "OctetString"
_RuijieHQoSUserQFlowQName_Object = MibTableColumn
ruijieHQoSUserQFlowQName = _RuijieHQoSUserQFlowQName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 2, 3, 1, 5),
    _RuijieHQoSUserQFlowQName_Type()
)
ruijieHQoSUserQFlowQName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSUserQFlowQName.setStatus("current")
_RuijieHQoSUserQFlowQIndex_Type = Unsigned32
_RuijieHQoSUserQFlowQIndex_Object = MibTableColumn
ruijieHQoSUserQFlowQIndex = _RuijieHQoSUserQFlowQIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 2, 3, 1, 6),
    _RuijieHQoSUserQFlowQIndex_Type()
)
ruijieHQoSUserQFlowQIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHQoSUserQFlowQIndex.setStatus("current")


class _RuijieHQoSUserQGroupName_Type(OctetString):
    """Custom type ruijieHQoSUserQGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSUserQGroupName_Type.__name__ = "OctetString"
_RuijieHQoSUserQGroupName_Object = MibTableColumn
ruijieHQoSUserQGroupName = _RuijieHQoSUserQGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 2, 3, 1, 7),
    _RuijieHQoSUserQGroupName_Type()
)
ruijieHQoSUserQGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSUserQGroupName.setStatus("current")
_RuijieHQoSUserQGroupIndex_Type = Unsigned32
_RuijieHQoSUserQGroupIndex_Object = MibTableColumn
ruijieHQoSUserQGroupIndex = _RuijieHQoSUserQGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 2, 3, 1, 8),
    _RuijieHQoSUserQGroupIndex_Type()
)
ruijieHQoSUserQGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHQoSUserQGroupIndex.setStatus("current")


class _RuijieHQoSUserQFlowMapName_Type(OctetString):
    """Custom type ruijieHQoSUserQFlowMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSUserQFlowMapName_Type.__name__ = "OctetString"
_RuijieHQoSUserQFlowMapName_Object = MibTableColumn
ruijieHQoSUserQFlowMapName = _RuijieHQoSUserQFlowMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 2, 3, 1, 9),
    _RuijieHQoSUserQFlowMapName_Type()
)
ruijieHQoSUserQFlowMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSUserQFlowMapName.setStatus("current")
_RuijieHQoSUserQFlowMapIndex_Type = Unsigned32
_RuijieHQoSUserQFlowMapIndex_Object = MibTableColumn
ruijieHQoSUserQFlowMapIndex = _RuijieHQoSUserQFlowMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 2, 3, 1, 10),
    _RuijieHQoSUserQFlowMapIndex_Type()
)
ruijieHQoSUserQFlowMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHQoSUserQFlowMapIndex.setStatus("current")


class _RuijieHQoSUserQCIR_Type(Unsigned32):
    """Custom type ruijieHQoSUserQCIR based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RuijieHQoSUserQCIR_Type.__name__ = "Unsigned32"
_RuijieHQoSUserQCIR_Object = MibTableColumn
ruijieHQoSUserQCIR = _RuijieHQoSUserQCIR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 2, 3, 1, 11),
    _RuijieHQoSUserQCIR_Type()
)
ruijieHQoSUserQCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSUserQCIR.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSUserQCIR.setUnits("kilobits per second")


class _RuijieHQoSUserQPIR_Type(Unsigned32):
    """Custom type ruijieHQoSUserQPIR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
    )


_RuijieHQoSUserQPIR_Type.__name__ = "Unsigned32"
_RuijieHQoSUserQPIR_Object = MibTableColumn
ruijieHQoSUserQPIR = _RuijieHQoSUserQPIR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 2, 3, 1, 12),
    _RuijieHQoSUserQPIR_Type()
)
ruijieHQoSUserQPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSUserQPIR.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSUserQPIR.setUnits("kilobits per second")
_RuijieHQoSUserGroupQObjects_ObjectIdentity = ObjectIdentity
ruijieHQoSUserGroupQObjects = _RuijieHQoSUserGroupQObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 3)
)
_RuijieHQoSUserGroupQInIndexNext_Type = Integer32
_RuijieHQoSUserGroupQInIndexNext_Object = MibScalar
ruijieHQoSUserGroupQInIndexNext = _RuijieHQoSUserGroupQInIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 3, 1),
    _RuijieHQoSUserGroupQInIndexNext_Type()
)
ruijieHQoSUserGroupQInIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHQoSUserGroupQInIndexNext.setStatus("current")
_RuijieHQoSUserGroupQOutIndexNext_Type = Integer32
_RuijieHQoSUserGroupQOutIndexNext_Object = MibScalar
ruijieHQoSUserGroupQOutIndexNext = _RuijieHQoSUserGroupQOutIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 3, 2),
    _RuijieHQoSUserGroupQOutIndexNext_Type()
)
ruijieHQoSUserGroupQOutIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHQoSUserGroupQOutIndexNext.setStatus("current")
_RuijieHQoSUserGroupQTable_Object = MibTable
ruijieHQoSUserGroupQTable = _RuijieHQoSUserGroupQTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 3, 3)
)
if mibBuilder.loadTexts:
    ruijieHQoSUserGroupQTable.setStatus("current")
_RuijieHQoSUserGroupQEntry_Object = MibTableRow
ruijieHQoSUserGroupQEntry = _RuijieHQoSUserGroupQEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 3, 3, 1)
)
ruijieHQoSUserGroupQEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieHQoSUserGroupQIndex"),
)
if mibBuilder.loadTexts:
    ruijieHQoSUserGroupQEntry.setStatus("current")
_RuijieHQoSUserGroupQIndex_Type = Unsigned32
_RuijieHQoSUserGroupQIndex_Object = MibTableColumn
ruijieHQoSUserGroupQIndex = _RuijieHQoSUserGroupQIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 3, 3, 1, 1),
    _RuijieHQoSUserGroupQIndex_Type()
)
ruijieHQoSUserGroupQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieHQoSUserGroupQIndex.setStatus("current")


class _RuijieHQoSUserGroupQName_Type(OctetString):
    """Custom type ruijieHQoSUserGroupQName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSUserGroupQName_Type.__name__ = "OctetString"
_RuijieHQoSUserGroupQName_Object = MibTableColumn
ruijieHQoSUserGroupQName = _RuijieHQoSUserGroupQName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 3, 3, 1, 2),
    _RuijieHQoSUserGroupQName_Type()
)
ruijieHQoSUserGroupQName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSUserGroupQName.setStatus("current")
_RuijieHQoSUserGroupQDirection_Type = RuijieQDirectionType
_RuijieHQoSUserGroupQDirection_Object = MibTableColumn
ruijieHQoSUserGroupQDirection = _RuijieHQoSUserGroupQDirection_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 3, 3, 1, 3),
    _RuijieHQoSUserGroupQDirection_Type()
)
ruijieHQoSUserGroupQDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSUserGroupQDirection.setStatus("current")
_RuijieHQoSUserGroupQRowStatus_Type = RowStatus
_RuijieHQoSUserGroupQRowStatus_Object = MibTableColumn
ruijieHQoSUserGroupQRowStatus = _RuijieHQoSUserGroupQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 3, 3, 1, 4),
    _RuijieHQoSUserGroupQRowStatus_Type()
)
ruijieHQoSUserGroupQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSUserGroupQRowStatus.setStatus("current")


class _RuijieHQoSUserGroupQShaping_Type(Unsigned32):
    """Custom type ruijieHQoSUserGroupQShaping based on Unsigned32"""
    defaultValue = 10000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RuijieHQoSUserGroupQShaping_Type.__name__ = "Unsigned32"
_RuijieHQoSUserGroupQShaping_Object = MibTableColumn
ruijieHQoSUserGroupQShaping = _RuijieHQoSUserGroupQShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 3, 3, 1, 5),
    _RuijieHQoSUserGroupQShaping_Type()
)
ruijieHQoSUserGroupQShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSUserGroupQShaping.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSUserGroupQShaping.setUnits("kilobits per second")
_RuijieHQoSFlowQObjects_ObjectIdentity = ObjectIdentity
ruijieHQoSFlowQObjects = _RuijieHQoSFlowQObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4)
)
_RuijieHQoSFlowQIndexNext_Type = Integer32
_RuijieHQoSFlowQIndexNext_Object = MibScalar
ruijieHQoSFlowQIndexNext = _RuijieHQoSFlowQIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 1),
    _RuijieHQoSFlowQIndexNext_Type()
)
ruijieHQoSFlowQIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQIndexNext.setStatus("current")
_RuijieHQoSFlowQTable_Object = MibTable
ruijieHQoSFlowQTable = _RuijieHQoSFlowQTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2)
)
if mibBuilder.loadTexts:
    ruijieHQoSFlowQTable.setStatus("current")
_RuijieHQoSFlowQEntry_Object = MibTableRow
ruijieHQoSFlowQEntry = _RuijieHQoSFlowQEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1)
)
ruijieHQoSFlowQEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieHQoSFlowQIndex"),
)
if mibBuilder.loadTexts:
    ruijieHQoSFlowQEntry.setStatus("current")
_RuijieHQoSFlowQIndex_Type = Unsigned32
_RuijieHQoSFlowQIndex_Object = MibTableColumn
ruijieHQoSFlowQIndex = _RuijieHQoSFlowQIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 1),
    _RuijieHQoSFlowQIndex_Type()
)
ruijieHQoSFlowQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQIndex.setStatus("current")


class _RuijieHQoSFlowQName_Type(OctetString):
    """Custom type ruijieHQoSFlowQName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSFlowQName_Type.__name__ = "OctetString"
_RuijieHQoSFlowQName_Object = MibTableColumn
ruijieHQoSFlowQName = _RuijieHQoSFlowQName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 2),
    _RuijieHQoSFlowQName_Type()
)
ruijieHQoSFlowQName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQName.setStatus("current")
_RuijieHQoSFlowQRowStatus_Type = RowStatus
_RuijieHQoSFlowQRowStatus_Object = MibTableColumn
ruijieHQoSFlowQRowStatus = _RuijieHQoSFlowQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 3),
    _RuijieHQoSFlowQRowStatus_Type()
)
ruijieHQoSFlowQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQRowStatus.setStatus("current")


class _RuijieHQoSFlowQBEQType_Type(RuijieQType):
    """Custom type ruijieHQoSFlowQBEQType based on RuijieQType"""
    defaultValue = 2


_RuijieHQoSFlowQBEQType_Type.__name__ = "RuijieQType"
_RuijieHQoSFlowQBEQType_Object = MibTableColumn
ruijieHQoSFlowQBEQType = _RuijieHQoSFlowQBEQType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 4),
    _RuijieHQoSFlowQBEQType_Type()
)
ruijieHQoSFlowQBEQType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQBEQType.setStatus("current")


class _RuijieHQoSFlowQBEQWredWeight_Type(Integer32):
    """Custom type ruijieHQoSFlowQBEQWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieHQoSFlowQBEQWredWeight_Type.__name__ = "Integer32"
_RuijieHQoSFlowQBEQWredWeight_Object = MibTableColumn
ruijieHQoSFlowQBEQWredWeight = _RuijieHQoSFlowQBEQWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 5),
    _RuijieHQoSFlowQBEQWredWeight_Type()
)
ruijieHQoSFlowQBEQWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQBEQWredWeight.setStatus("current")


class _RuijieHQoSFlowQBEQWredName_Type(OctetString):
    """Custom type ruijieHQoSFlowQBEQWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSFlowQBEQWredName_Type.__name__ = "OctetString"
_RuijieHQoSFlowQBEQWredName_Object = MibTableColumn
ruijieHQoSFlowQBEQWredName = _RuijieHQoSFlowQBEQWredName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 6),
    _RuijieHQoSFlowQBEQWredName_Type()
)
ruijieHQoSFlowQBEQWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQBEQWredName.setStatus("current")


class _RuijieHQoSFlowQBEQDepth_Type(Integer32):
    """Custom type ruijieHQoSFlowQBEQDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_RuijieHQoSFlowQBEQDepth_Type.__name__ = "Integer32"
_RuijieHQoSFlowQBEQDepth_Object = MibTableColumn
ruijieHQoSFlowQBEQDepth = _RuijieHQoSFlowQBEQDepth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 7),
    _RuijieHQoSFlowQBEQDepth_Type()
)
ruijieHQoSFlowQBEQDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQBEQDepth.setStatus("current")


class _RuijieHQoSFlowQBEQShaping_Type(Integer32):
    """Custom type ruijieHQoSFlowQBEQShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RuijieHQoSFlowQBEQShaping_Type.__name__ = "Integer32"
_RuijieHQoSFlowQBEQShaping_Object = MibTableColumn
ruijieHQoSFlowQBEQShaping = _RuijieHQoSFlowQBEQShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 8),
    _RuijieHQoSFlowQBEQShaping_Type()
)
ruijieHQoSFlowQBEQShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQBEQShaping.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQBEQShaping.setUnits("kilobits per second")


class _RuijieHQoSFlowQAF1QType_Type(RuijieQType):
    """Custom type ruijieHQoSFlowQAF1QType based on RuijieQType"""
    defaultValue = 2


_RuijieHQoSFlowQAF1QType_Type.__name__ = "RuijieQType"
_RuijieHQoSFlowQAF1QType_Object = MibTableColumn
ruijieHQoSFlowQAF1QType = _RuijieHQoSFlowQAF1QType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 9),
    _RuijieHQoSFlowQAF1QType_Type()
)
ruijieHQoSFlowQAF1QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF1QType.setStatus("current")


class _RuijieHQoSFlowQAF1QWredWeight_Type(Integer32):
    """Custom type ruijieHQoSFlowQAF1QWredWeight based on Integer32"""
    defaultValue = 10


_RuijieHQoSFlowQAF1QWredWeight_Type.__name__ = "Integer32"
_RuijieHQoSFlowQAF1QWredWeight_Object = MibTableColumn
ruijieHQoSFlowQAF1QWredWeight = _RuijieHQoSFlowQAF1QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 10),
    _RuijieHQoSFlowQAF1QWredWeight_Type()
)
ruijieHQoSFlowQAF1QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF1QWredWeight.setStatus("current")


class _RuijieHQoSFlowQAF1QWredName_Type(OctetString):
    """Custom type ruijieHQoSFlowQAF1QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSFlowQAF1QWredName_Type.__name__ = "OctetString"
_RuijieHQoSFlowQAF1QWredName_Object = MibTableColumn
ruijieHQoSFlowQAF1QWredName = _RuijieHQoSFlowQAF1QWredName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 11),
    _RuijieHQoSFlowQAF1QWredName_Type()
)
ruijieHQoSFlowQAF1QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF1QWredName.setStatus("current")


class _RuijieHQoSFlowQAF1QDepth_Type(Integer32):
    """Custom type ruijieHQoSFlowQAF1QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieHQoSFlowQAF1QDepth_Type.__name__ = "Integer32"
_RuijieHQoSFlowQAF1QDepth_Object = MibTableColumn
ruijieHQoSFlowQAF1QDepth = _RuijieHQoSFlowQAF1QDepth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 12),
    _RuijieHQoSFlowQAF1QDepth_Type()
)
ruijieHQoSFlowQAF1QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF1QDepth.setStatus("current")


class _RuijieHQoSFlowQAF1QShaping_Type(Integer32):
    """Custom type ruijieHQoSFlowQAF1QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RuijieHQoSFlowQAF1QShaping_Type.__name__ = "Integer32"
_RuijieHQoSFlowQAF1QShaping_Object = MibTableColumn
ruijieHQoSFlowQAF1QShaping = _RuijieHQoSFlowQAF1QShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 13),
    _RuijieHQoSFlowQAF1QShaping_Type()
)
ruijieHQoSFlowQAF1QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF1QShaping.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF1QShaping.setUnits("kilobits per second")


class _RuijieHQoSFlowQAF2QType_Type(RuijieQType):
    """Custom type ruijieHQoSFlowQAF2QType based on RuijieQType"""
    defaultValue = 2


_RuijieHQoSFlowQAF2QType_Type.__name__ = "RuijieQType"
_RuijieHQoSFlowQAF2QType_Object = MibTableColumn
ruijieHQoSFlowQAF2QType = _RuijieHQoSFlowQAF2QType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 14),
    _RuijieHQoSFlowQAF2QType_Type()
)
ruijieHQoSFlowQAF2QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF2QType.setStatus("current")


class _RuijieHQoSFlowQAF2QWredWeight_Type(Integer32):
    """Custom type ruijieHQoSFlowQAF2QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_RuijieHQoSFlowQAF2QWredWeight_Type.__name__ = "Integer32"
_RuijieHQoSFlowQAF2QWredWeight_Object = MibTableColumn
ruijieHQoSFlowQAF2QWredWeight = _RuijieHQoSFlowQAF2QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 15),
    _RuijieHQoSFlowQAF2QWredWeight_Type()
)
ruijieHQoSFlowQAF2QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF2QWredWeight.setStatus("current")


class _RuijieHQoSFlowQAF2QWredName_Type(OctetString):
    """Custom type ruijieHQoSFlowQAF2QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSFlowQAF2QWredName_Type.__name__ = "OctetString"
_RuijieHQoSFlowQAF2QWredName_Object = MibTableColumn
ruijieHQoSFlowQAF2QWredName = _RuijieHQoSFlowQAF2QWredName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 16),
    _RuijieHQoSFlowQAF2QWredName_Type()
)
ruijieHQoSFlowQAF2QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF2QWredName.setStatus("current")


class _RuijieHQoSFlowQAF2QDepth_Type(Integer32):
    """Custom type ruijieHQoSFlowQAF2QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieHQoSFlowQAF2QDepth_Type.__name__ = "Integer32"
_RuijieHQoSFlowQAF2QDepth_Object = MibTableColumn
ruijieHQoSFlowQAF2QDepth = _RuijieHQoSFlowQAF2QDepth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 17),
    _RuijieHQoSFlowQAF2QDepth_Type()
)
ruijieHQoSFlowQAF2QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF2QDepth.setStatus("current")


class _RuijieHQoSFlowQAF2QShaping_Type(Integer32):
    """Custom type ruijieHQoSFlowQAF2QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RuijieHQoSFlowQAF2QShaping_Type.__name__ = "Integer32"
_RuijieHQoSFlowQAF2QShaping_Object = MibTableColumn
ruijieHQoSFlowQAF2QShaping = _RuijieHQoSFlowQAF2QShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 18),
    _RuijieHQoSFlowQAF2QShaping_Type()
)
ruijieHQoSFlowQAF2QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF2QShaping.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF2QShaping.setUnits("kilobits per second")


class _RuijieHQoSFlowQAF3QType_Type(RuijieQType):
    """Custom type ruijieHQoSFlowQAF3QType based on RuijieQType"""
    defaultValue = 2


_RuijieHQoSFlowQAF3QType_Type.__name__ = "RuijieQType"
_RuijieHQoSFlowQAF3QType_Object = MibTableColumn
ruijieHQoSFlowQAF3QType = _RuijieHQoSFlowQAF3QType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 19),
    _RuijieHQoSFlowQAF3QType_Type()
)
ruijieHQoSFlowQAF3QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF3QType.setStatus("current")


class _RuijieHQoSFlowQAF3QWredWeight_Type(Integer32):
    """Custom type ruijieHQoSFlowQAF3QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_RuijieHQoSFlowQAF3QWredWeight_Type.__name__ = "Integer32"
_RuijieHQoSFlowQAF3QWredWeight_Object = MibTableColumn
ruijieHQoSFlowQAF3QWredWeight = _RuijieHQoSFlowQAF3QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 20),
    _RuijieHQoSFlowQAF3QWredWeight_Type()
)
ruijieHQoSFlowQAF3QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF3QWredWeight.setStatus("current")


class _RuijieHQoSFlowQAF3QWredName_Type(OctetString):
    """Custom type ruijieHQoSFlowQAF3QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSFlowQAF3QWredName_Type.__name__ = "OctetString"
_RuijieHQoSFlowQAF3QWredName_Object = MibTableColumn
ruijieHQoSFlowQAF3QWredName = _RuijieHQoSFlowQAF3QWredName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 21),
    _RuijieHQoSFlowQAF3QWredName_Type()
)
ruijieHQoSFlowQAF3QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF3QWredName.setStatus("current")


class _RuijieHQoSFlowQAF3QDepth_Type(Integer32):
    """Custom type ruijieHQoSFlowQAF3QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieHQoSFlowQAF3QDepth_Type.__name__ = "Integer32"
_RuijieHQoSFlowQAF3QDepth_Object = MibTableColumn
ruijieHQoSFlowQAF3QDepth = _RuijieHQoSFlowQAF3QDepth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 22),
    _RuijieHQoSFlowQAF3QDepth_Type()
)
ruijieHQoSFlowQAF3QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF3QDepth.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF3QDepth.setUnits("kilobits per second")


class _RuijieHQoSFlowQAF3QShaping_Type(Integer32):
    """Custom type ruijieHQoSFlowQAF3QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RuijieHQoSFlowQAF3QShaping_Type.__name__ = "Integer32"
_RuijieHQoSFlowQAF3QShaping_Object = MibTableColumn
ruijieHQoSFlowQAF3QShaping = _RuijieHQoSFlowQAF3QShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 23),
    _RuijieHQoSFlowQAF3QShaping_Type()
)
ruijieHQoSFlowQAF3QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF3QShaping.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF3QShaping.setUnits("kilobits per second")


class _RuijieHQoSFlowQAF4QType_Type(RuijieQType):
    """Custom type ruijieHQoSFlowQAF4QType based on RuijieQType"""
    defaultValue = 2


_RuijieHQoSFlowQAF4QType_Type.__name__ = "RuijieQType"
_RuijieHQoSFlowQAF4QType_Object = MibTableColumn
ruijieHQoSFlowQAF4QType = _RuijieHQoSFlowQAF4QType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 24),
    _RuijieHQoSFlowQAF4QType_Type()
)
ruijieHQoSFlowQAF4QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF4QType.setStatus("current")


class _RuijieHQoSFlowQAF4QWredWeight_Type(Integer32):
    """Custom type ruijieHQoSFlowQAF4QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_RuijieHQoSFlowQAF4QWredWeight_Type.__name__ = "Integer32"
_RuijieHQoSFlowQAF4QWredWeight_Object = MibTableColumn
ruijieHQoSFlowQAF4QWredWeight = _RuijieHQoSFlowQAF4QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 25),
    _RuijieHQoSFlowQAF4QWredWeight_Type()
)
ruijieHQoSFlowQAF4QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF4QWredWeight.setStatus("current")


class _RuijieHQoSFlowQAF4QWredName_Type(OctetString):
    """Custom type ruijieHQoSFlowQAF4QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSFlowQAF4QWredName_Type.__name__ = "OctetString"
_RuijieHQoSFlowQAF4QWredName_Object = MibTableColumn
ruijieHQoSFlowQAF4QWredName = _RuijieHQoSFlowQAF4QWredName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 26),
    _RuijieHQoSFlowQAF4QWredName_Type()
)
ruijieHQoSFlowQAF4QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF4QWredName.setStatus("current")


class _RuijieHQoSFlowQAF4QDepth_Type(Integer32):
    """Custom type ruijieHQoSFlowQAF4QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieHQoSFlowQAF4QDepth_Type.__name__ = "Integer32"
_RuijieHQoSFlowQAF4QDepth_Object = MibTableColumn
ruijieHQoSFlowQAF4QDepth = _RuijieHQoSFlowQAF4QDepth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 27),
    _RuijieHQoSFlowQAF4QDepth_Type()
)
ruijieHQoSFlowQAF4QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF4QDepth.setStatus("current")


class _RuijieHQoSFlowQAF4QShaping_Type(Integer32):
    """Custom type ruijieHQoSFlowQAF4QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_RuijieHQoSFlowQAF4QShaping_Type.__name__ = "Integer32"
_RuijieHQoSFlowQAF4QShaping_Object = MibTableColumn
ruijieHQoSFlowQAF4QShaping = _RuijieHQoSFlowQAF4QShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 28),
    _RuijieHQoSFlowQAF4QShaping_Type()
)
ruijieHQoSFlowQAF4QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF4QShaping.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQAF4QShaping.setUnits("kilobits per second")


class _RuijieHQoSFlowQEFQType_Type(RuijieQType):
    """Custom type ruijieHQoSFlowQEFQType based on RuijieQType"""
    defaultValue = 3


_RuijieHQoSFlowQEFQType_Type.__name__ = "RuijieQType"
_RuijieHQoSFlowQEFQType_Object = MibTableColumn
ruijieHQoSFlowQEFQType = _RuijieHQoSFlowQEFQType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 29),
    _RuijieHQoSFlowQEFQType_Type()
)
ruijieHQoSFlowQEFQType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQEFQType.setStatus("current")


class _RuijieHQoSFlowQEFQWredWeight_Type(Integer32):
    """Custom type ruijieHQoSFlowQEFQWredWeight based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_RuijieHQoSFlowQEFQWredWeight_Type.__name__ = "Integer32"
_RuijieHQoSFlowQEFQWredWeight_Object = MibTableColumn
ruijieHQoSFlowQEFQWredWeight = _RuijieHQoSFlowQEFQWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 30),
    _RuijieHQoSFlowQEFQWredWeight_Type()
)
ruijieHQoSFlowQEFQWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQEFQWredWeight.setStatus("current")


class _RuijieHQoSFlowQEFQWredName_Type(OctetString):
    """Custom type ruijieHQoSFlowQEFQWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSFlowQEFQWredName_Type.__name__ = "OctetString"
_RuijieHQoSFlowQEFQWredName_Object = MibTableColumn
ruijieHQoSFlowQEFQWredName = _RuijieHQoSFlowQEFQWredName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 31),
    _RuijieHQoSFlowQEFQWredName_Type()
)
ruijieHQoSFlowQEFQWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQEFQWredName.setStatus("current")


class _RuijieHQoSFlowQEFQDepth_Type(Integer32):
    """Custom type ruijieHQoSFlowQEFQDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieHQoSFlowQEFQDepth_Type.__name__ = "Integer32"
_RuijieHQoSFlowQEFQDepth_Object = MibTableColumn
ruijieHQoSFlowQEFQDepth = _RuijieHQoSFlowQEFQDepth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 32),
    _RuijieHQoSFlowQEFQDepth_Type()
)
ruijieHQoSFlowQEFQDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQEFQDepth.setStatus("current")


class _RuijieHQoSFlowQEFQShaping_Type(Integer32):
    """Custom type ruijieHQoSFlowQEFQShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RuijieHQoSFlowQEFQShaping_Type.__name__ = "Integer32"
_RuijieHQoSFlowQEFQShaping_Object = MibTableColumn
ruijieHQoSFlowQEFQShaping = _RuijieHQoSFlowQEFQShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 33),
    _RuijieHQoSFlowQEFQShaping_Type()
)
ruijieHQoSFlowQEFQShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQEFQShaping.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQEFQShaping.setUnits("kilobits per second")


class _RuijieHQoSFlowQCS6QType_Type(RuijieQType):
    """Custom type ruijieHQoSFlowQCS6QType based on RuijieQType"""
    defaultValue = 3


_RuijieHQoSFlowQCS6QType_Type.__name__ = "RuijieQType"
_RuijieHQoSFlowQCS6QType_Object = MibTableColumn
ruijieHQoSFlowQCS6QType = _RuijieHQoSFlowQCS6QType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 34),
    _RuijieHQoSFlowQCS6QType_Type()
)
ruijieHQoSFlowQCS6QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQCS6QType.setStatus("current")


class _RuijieHQoSFlowQCS6QWredWeight_Type(Integer32):
    """Custom type ruijieHQoSFlowQCS6QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_RuijieHQoSFlowQCS6QWredWeight_Type.__name__ = "Integer32"
_RuijieHQoSFlowQCS6QWredWeight_Object = MibTableColumn
ruijieHQoSFlowQCS6QWredWeight = _RuijieHQoSFlowQCS6QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 35),
    _RuijieHQoSFlowQCS6QWredWeight_Type()
)
ruijieHQoSFlowQCS6QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQCS6QWredWeight.setStatus("current")


class _RuijieHQoSFlowQCS6QWredName_Type(OctetString):
    """Custom type ruijieHQoSFlowQCS6QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSFlowQCS6QWredName_Type.__name__ = "OctetString"
_RuijieHQoSFlowQCS6QWredName_Object = MibTableColumn
ruijieHQoSFlowQCS6QWredName = _RuijieHQoSFlowQCS6QWredName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 36),
    _RuijieHQoSFlowQCS6QWredName_Type()
)
ruijieHQoSFlowQCS6QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQCS6QWredName.setStatus("current")


class _RuijieHQoSFlowQCS6QDepth_Type(Integer32):
    """Custom type ruijieHQoSFlowQCS6QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieHQoSFlowQCS6QDepth_Type.__name__ = "Integer32"
_RuijieHQoSFlowQCS6QDepth_Object = MibTableColumn
ruijieHQoSFlowQCS6QDepth = _RuijieHQoSFlowQCS6QDepth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 37),
    _RuijieHQoSFlowQCS6QDepth_Type()
)
ruijieHQoSFlowQCS6QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQCS6QDepth.setStatus("current")


class _RuijieHQoSFlowQCS6QShaping_Type(Integer32):
    """Custom type ruijieHQoSFlowQCS6QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RuijieHQoSFlowQCS6QShaping_Type.__name__ = "Integer32"
_RuijieHQoSFlowQCS6QShaping_Object = MibTableColumn
ruijieHQoSFlowQCS6QShaping = _RuijieHQoSFlowQCS6QShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 38),
    _RuijieHQoSFlowQCS6QShaping_Type()
)
ruijieHQoSFlowQCS6QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQCS6QShaping.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQCS6QShaping.setUnits("kilobits per second")


class _RuijieHQoSFlowQCS7QType_Type(RuijieQType):
    """Custom type ruijieHQoSFlowQCS7QType based on RuijieQType"""
    defaultValue = 3


_RuijieHQoSFlowQCS7QType_Type.__name__ = "RuijieQType"
_RuijieHQoSFlowQCS7QType_Object = MibTableColumn
ruijieHQoSFlowQCS7QType = _RuijieHQoSFlowQCS7QType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 39),
    _RuijieHQoSFlowQCS7QType_Type()
)
ruijieHQoSFlowQCS7QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQCS7QType.setStatus("current")


class _RuijieHQoSFlowQCS7QWredWeight_Type(Integer32):
    """Custom type ruijieHQoSFlowQCS7QWredWeight based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_RuijieHQoSFlowQCS7QWredWeight_Type.__name__ = "Integer32"
_RuijieHQoSFlowQCS7QWredWeight_Object = MibTableColumn
ruijieHQoSFlowQCS7QWredWeight = _RuijieHQoSFlowQCS7QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 40),
    _RuijieHQoSFlowQCS7QWredWeight_Type()
)
ruijieHQoSFlowQCS7QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQCS7QWredWeight.setStatus("current")


class _RuijieHQoSFlowQCS7QWredName_Type(OctetString):
    """Custom type ruijieHQoSFlowQCS7QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSFlowQCS7QWredName_Type.__name__ = "OctetString"
_RuijieHQoSFlowQCS7QWredName_Object = MibTableColumn
ruijieHQoSFlowQCS7QWredName = _RuijieHQoSFlowQCS7QWredName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 41),
    _RuijieHQoSFlowQCS7QWredName_Type()
)
ruijieHQoSFlowQCS7QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQCS7QWredName.setStatus("current")


class _RuijieHQoSFlowQCS7QDepth_Type(Integer32):
    """Custom type ruijieHQoSFlowQCS7QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieHQoSFlowQCS7QDepth_Type.__name__ = "Integer32"
_RuijieHQoSFlowQCS7QDepth_Object = MibTableColumn
ruijieHQoSFlowQCS7QDepth = _RuijieHQoSFlowQCS7QDepth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 42),
    _RuijieHQoSFlowQCS7QDepth_Type()
)
ruijieHQoSFlowQCS7QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQCS7QDepth.setStatus("current")


class _RuijieHQoSFlowQCS7QShaping_Type(Integer32):
    """Custom type ruijieHQoSFlowQCS7QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RuijieHQoSFlowQCS7QShaping_Type.__name__ = "Integer32"
_RuijieHQoSFlowQCS7QShaping_Object = MibTableColumn
ruijieHQoSFlowQCS7QShaping = _RuijieHQoSFlowQCS7QShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 4, 2, 1, 43),
    _RuijieHQoSFlowQCS7QShaping_Type()
)
ruijieHQoSFlowQCS7QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQCS7QShaping.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSFlowQCS7QShaping.setUnits("kilobits per second")
_RuijieHQoSFlowMapObjects_ObjectIdentity = ObjectIdentity
ruijieHQoSFlowMapObjects = _RuijieHQoSFlowMapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 5)
)
_RuijieHQoSFlowMapIndexNext_Type = Integer32
_RuijieHQoSFlowMapIndexNext_Object = MibScalar
ruijieHQoSFlowMapIndexNext = _RuijieHQoSFlowMapIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 5, 1),
    _RuijieHQoSFlowMapIndexNext_Type()
)
ruijieHQoSFlowMapIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHQoSFlowMapIndexNext.setStatus("current")
_RuijieHQoSFlowMapTable_Object = MibTable
ruijieHQoSFlowMapTable = _RuijieHQoSFlowMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 5, 2)
)
if mibBuilder.loadTexts:
    ruijieHQoSFlowMapTable.setStatus("current")
_RuijieHQoSFlowMapEntry_Object = MibTableRow
ruijieHQoSFlowMapEntry = _RuijieHQoSFlowMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 5, 2, 1)
)
ruijieHQoSFlowMapEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieHQoSFlowMapIndex"),
)
if mibBuilder.loadTexts:
    ruijieHQoSFlowMapEntry.setStatus("current")
_RuijieHQoSFlowMapIndex_Type = Unsigned32
_RuijieHQoSFlowMapIndex_Object = MibTableColumn
ruijieHQoSFlowMapIndex = _RuijieHQoSFlowMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 5, 2, 1, 1),
    _RuijieHQoSFlowMapIndex_Type()
)
ruijieHQoSFlowMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieHQoSFlowMapIndex.setStatus("current")


class _RuijieHQoSFlowMapName_Type(OctetString):
    """Custom type ruijieHQoSFlowMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSFlowMapName_Type.__name__ = "OctetString"
_RuijieHQoSFlowMapName_Object = MibTableColumn
ruijieHQoSFlowMapName = _RuijieHQoSFlowMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 5, 2, 1, 2),
    _RuijieHQoSFlowMapName_Type()
)
ruijieHQoSFlowMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowMapName.setStatus("current")
_RuijieHQoSFlowMapRowStatus_Type = RowStatus
_RuijieHQoSFlowMapRowStatus_Object = MibTableColumn
ruijieHQoSFlowMapRowStatus = _RuijieHQoSFlowMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 5, 2, 1, 3),
    _RuijieHQoSFlowMapRowStatus_Type()
)
ruijieHQoSFlowMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowMapRowStatus.setStatus("current")


class _RuijieHQoSFlowMapBEQ2PortQ_Type(RuijieCosType):
    """Custom type ruijieHQoSFlowMapBEQ2PortQ based on RuijieCosType"""
    defaultValue = 1


_RuijieHQoSFlowMapBEQ2PortQ_Type.__name__ = "RuijieCosType"
_RuijieHQoSFlowMapBEQ2PortQ_Object = MibTableColumn
ruijieHQoSFlowMapBEQ2PortQ = _RuijieHQoSFlowMapBEQ2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 5, 2, 1, 4),
    _RuijieHQoSFlowMapBEQ2PortQ_Type()
)
ruijieHQoSFlowMapBEQ2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowMapBEQ2PortQ.setStatus("current")


class _RuijieHQoSFlowMapAF1Q2PortQ_Type(RuijieCosType):
    """Custom type ruijieHQoSFlowMapAF1Q2PortQ based on RuijieCosType"""
    defaultValue = 2


_RuijieHQoSFlowMapAF1Q2PortQ_Type.__name__ = "RuijieCosType"
_RuijieHQoSFlowMapAF1Q2PortQ_Object = MibTableColumn
ruijieHQoSFlowMapAF1Q2PortQ = _RuijieHQoSFlowMapAF1Q2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 5, 2, 1, 5),
    _RuijieHQoSFlowMapAF1Q2PortQ_Type()
)
ruijieHQoSFlowMapAF1Q2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowMapAF1Q2PortQ.setStatus("current")


class _RuijieHQoSFlowMapAF2Q2PortQ_Type(RuijieCosType):
    """Custom type ruijieHQoSFlowMapAF2Q2PortQ based on RuijieCosType"""
    defaultValue = 3


_RuijieHQoSFlowMapAF2Q2PortQ_Type.__name__ = "RuijieCosType"
_RuijieHQoSFlowMapAF2Q2PortQ_Object = MibTableColumn
ruijieHQoSFlowMapAF2Q2PortQ = _RuijieHQoSFlowMapAF2Q2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 5, 2, 1, 6),
    _RuijieHQoSFlowMapAF2Q2PortQ_Type()
)
ruijieHQoSFlowMapAF2Q2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowMapAF2Q2PortQ.setStatus("current")


class _RuijieHQoSFlowMapAF3Q2PortQ_Type(RuijieCosType):
    """Custom type ruijieHQoSFlowMapAF3Q2PortQ based on RuijieCosType"""
    defaultValue = 4


_RuijieHQoSFlowMapAF3Q2PortQ_Type.__name__ = "RuijieCosType"
_RuijieHQoSFlowMapAF3Q2PortQ_Object = MibTableColumn
ruijieHQoSFlowMapAF3Q2PortQ = _RuijieHQoSFlowMapAF3Q2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 5, 2, 1, 7),
    _RuijieHQoSFlowMapAF3Q2PortQ_Type()
)
ruijieHQoSFlowMapAF3Q2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowMapAF3Q2PortQ.setStatus("current")


class _RuijieHQoSFlowMapAF4Q2PortQ_Type(RuijieCosType):
    """Custom type ruijieHQoSFlowMapAF4Q2PortQ based on RuijieCosType"""
    defaultValue = 5


_RuijieHQoSFlowMapAF4Q2PortQ_Type.__name__ = "RuijieCosType"
_RuijieHQoSFlowMapAF4Q2PortQ_Object = MibTableColumn
ruijieHQoSFlowMapAF4Q2PortQ = _RuijieHQoSFlowMapAF4Q2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 5, 2, 1, 8),
    _RuijieHQoSFlowMapAF4Q2PortQ_Type()
)
ruijieHQoSFlowMapAF4Q2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowMapAF4Q2PortQ.setStatus("current")


class _RuijieHQoSFlowMapEFQ2PortQ_Type(RuijieCosType):
    """Custom type ruijieHQoSFlowMapEFQ2PortQ based on RuijieCosType"""
    defaultValue = 6


_RuijieHQoSFlowMapEFQ2PortQ_Type.__name__ = "RuijieCosType"
_RuijieHQoSFlowMapEFQ2PortQ_Object = MibTableColumn
ruijieHQoSFlowMapEFQ2PortQ = _RuijieHQoSFlowMapEFQ2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 5, 2, 1, 9),
    _RuijieHQoSFlowMapEFQ2PortQ_Type()
)
ruijieHQoSFlowMapEFQ2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowMapEFQ2PortQ.setStatus("current")


class _RuijieHQoSFlowMapCS6Q2PortQ_Type(RuijieCosType):
    """Custom type ruijieHQoSFlowMapCS6Q2PortQ based on RuijieCosType"""
    defaultValue = 7


_RuijieHQoSFlowMapCS6Q2PortQ_Type.__name__ = "RuijieCosType"
_RuijieHQoSFlowMapCS6Q2PortQ_Object = MibTableColumn
ruijieHQoSFlowMapCS6Q2PortQ = _RuijieHQoSFlowMapCS6Q2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 5, 2, 1, 10),
    _RuijieHQoSFlowMapCS6Q2PortQ_Type()
)
ruijieHQoSFlowMapCS6Q2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowMapCS6Q2PortQ.setStatus("current")


class _RuijieHQoSFlowMapCS7Q2PortQ_Type(RuijieCosType):
    """Custom type ruijieHQoSFlowMapCS7Q2PortQ based on RuijieCosType"""
    defaultValue = 8


_RuijieHQoSFlowMapCS7Q2PortQ_Type.__name__ = "RuijieCosType"
_RuijieHQoSFlowMapCS7Q2PortQ_Object = MibTableColumn
ruijieHQoSFlowMapCS7Q2PortQ = _RuijieHQoSFlowMapCS7Q2PortQ_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 5, 2, 1, 11),
    _RuijieHQoSFlowMapCS7Q2PortQ_Type()
)
ruijieHQoSFlowMapCS7Q2PortQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSFlowMapCS7Q2PortQ.setStatus("current")
_RuijieHQoSTClassifierObjects_ObjectIdentity = ObjectIdentity
ruijieHQoSTClassifierObjects = _RuijieHQoSTClassifierObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6)
)
_RuijieHQoSTClassifierIndexNext_Type = Integer32
_RuijieHQoSTClassifierIndexNext_Object = MibScalar
ruijieHQoSTClassifierIndexNext = _RuijieHQoSTClassifierIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 1),
    _RuijieHQoSTClassifierIndexNext_Type()
)
ruijieHQoSTClassifierIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierIndexNext.setStatus("current")
_RuijieHQoSTClassifierTable_Object = MibTable
ruijieHQoSTClassifierTable = _RuijieHQoSTClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2)
)
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierTable.setStatus("current")
_RuijieHQoSTClassifierEntry_Object = MibTableRow
ruijieHQoSTClassifierEntry = _RuijieHQoSTClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1)
)
ruijieHQoSTClassifierEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieHQoSTClassifierIndex"),
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieHQoSTClassifierInstance"),
)
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierEntry.setStatus("current")
_RuijieHQoSTClassifierIndex_Type = Unsigned32
_RuijieHQoSTClassifierIndex_Object = MibTableColumn
ruijieHQoSTClassifierIndex = _RuijieHQoSTClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 1),
    _RuijieHQoSTClassifierIndex_Type()
)
ruijieHQoSTClassifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierIndex.setStatus("current")
_RuijieHQoSTClassifierInstance_Type = Unsigned32
_RuijieHQoSTClassifierInstance_Object = MibTableColumn
ruijieHQoSTClassifierInstance = _RuijieHQoSTClassifierInstance_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 2),
    _RuijieHQoSTClassifierInstance_Type()
)
ruijieHQoSTClassifierInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierInstance.setStatus("current")


class _RuijieHQoSTClassifierName_Type(OctetString):
    """Custom type ruijieHQoSTClassifierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSTClassifierName_Type.__name__ = "OctetString"
_RuijieHQoSTClassifierName_Object = MibTableColumn
ruijieHQoSTClassifierName = _RuijieHQoSTClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 3),
    _RuijieHQoSTClassifierName_Type()
)
ruijieHQoSTClassifierName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierName.setStatus("current")


class _RuijieHQoSTClassifierType_Type(Integer32):
    """Custom type ruijieHQoSTClassifierType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tc-or", 1),
          ("tc-and", 2))
    )


_RuijieHQoSTClassifierType_Type.__name__ = "Integer32"
_RuijieHQoSTClassifierType_Object = MibTableColumn
ruijieHQoSTClassifierType = _RuijieHQoSTClassifierType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 4),
    _RuijieHQoSTClassifierType_Type()
)
ruijieHQoSTClassifierType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierType.setStatus("current")
_RuijieHQoSTClassifierRowStatus_Type = RowStatus
_RuijieHQoSTClassifierRowStatus_Object = MibTableColumn
ruijieHQoSTClassifierRowStatus = _RuijieHQoSTClassifierRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 5),
    _RuijieHQoSTClassifierRowStatus_Type()
)
ruijieHQoSTClassifierRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierRowStatus.setStatus("current")


class _RuijieHQoSTClassifierMatchMask_Type(Bits):
    """Custom type ruijieHQoSTClassifierMatchMask based on Bits"""
    namedValues = NamedValues(
        *(("tc-v4-any", 0),
          ("tc-v4-aclID", 1),
          ("tc-v4-aclName", 2),
          ("tc-v4-dscp", 3),
          ("tc-v4-tos", 4),
          ("tc-v6-any", 5),
          ("tc-v6-aclID", 6),
          ("tc-v6-aclName", 7),
          ("tc-v6-dscp", 8),
          ("tc-vlan-cos", 9),
          ("tc-exp", 10),
          ("tc-srcmac", 11),
          ("tc-dstmac", 12))
    )

_RuijieHQoSTClassifierMatchMask_Type.__name__ = "Bits"
_RuijieHQoSTClassifierMatchMask_Object = MibTableColumn
ruijieHQoSTClassifierMatchMask = _RuijieHQoSTClassifierMatchMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 6),
    _RuijieHQoSTClassifierMatchMask_Type()
)
ruijieHQoSTClassifierMatchMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierMatchMask.setStatus("current")


class _RuijieHQoSTClassifierMatchV4Any_Type(TruthValue):
    """Custom type ruijieHQoSTClassifierMatchV4Any based on TruthValue"""
    defaultValue = 2


_RuijieHQoSTClassifierMatchV4Any_Type.__name__ = "TruthValue"
_RuijieHQoSTClassifierMatchV4Any_Object = MibTableColumn
ruijieHQoSTClassifierMatchV4Any = _RuijieHQoSTClassifierMatchV4Any_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 7),
    _RuijieHQoSTClassifierMatchV4Any_Type()
)
ruijieHQoSTClassifierMatchV4Any.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierMatchV4Any.setStatus("current")


class _RuijieHQoSTClassifierMatchV4AclID_Type(Integer32):
    """Custom type ruijieHQoSTClassifierMatchV4AclID based on Integer32"""
    defaultValue = 0


_RuijieHQoSTClassifierMatchV4AclID_Type.__name__ = "Integer32"
_RuijieHQoSTClassifierMatchV4AclID_Object = MibTableColumn
ruijieHQoSTClassifierMatchV4AclID = _RuijieHQoSTClassifierMatchV4AclID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 8),
    _RuijieHQoSTClassifierMatchV4AclID_Type()
)
ruijieHQoSTClassifierMatchV4AclID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierMatchV4AclID.setStatus("current")


class _RuijieHQoSTClassifierV4AclName_Type(OctetString):
    """Custom type ruijieHQoSTClassifierV4AclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSTClassifierV4AclName_Type.__name__ = "OctetString"
_RuijieHQoSTClassifierV4AclName_Object = MibTableColumn
ruijieHQoSTClassifierV4AclName = _RuijieHQoSTClassifierV4AclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 9),
    _RuijieHQoSTClassifierV4AclName_Type()
)
ruijieHQoSTClassifierV4AclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierV4AclName.setStatus("current")


class _RuijieHQoSTClassifierMatchV4Dscp_Type(Integer32):
    """Custom type ruijieHQoSTClassifierMatchV4Dscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RuijieHQoSTClassifierMatchV4Dscp_Type.__name__ = "Integer32"
_RuijieHQoSTClassifierMatchV4Dscp_Object = MibTableColumn
ruijieHQoSTClassifierMatchV4Dscp = _RuijieHQoSTClassifierMatchV4Dscp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 10),
    _RuijieHQoSTClassifierMatchV4Dscp_Type()
)
ruijieHQoSTClassifierMatchV4Dscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierMatchV4Dscp.setStatus("current")


class _RuijieHQoSTClassifierMatchV4Tos_Type(Integer32):
    """Custom type ruijieHQoSTClassifierMatchV4Tos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieHQoSTClassifierMatchV4Tos_Type.__name__ = "Integer32"
_RuijieHQoSTClassifierMatchV4Tos_Object = MibTableColumn
ruijieHQoSTClassifierMatchV4Tos = _RuijieHQoSTClassifierMatchV4Tos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 11),
    _RuijieHQoSTClassifierMatchV4Tos_Type()
)
ruijieHQoSTClassifierMatchV4Tos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierMatchV4Tos.setStatus("current")


class _RuijieHQoSTClassifierMatchV6Any_Type(TruthValue):
    """Custom type ruijieHQoSTClassifierMatchV6Any based on TruthValue"""
    defaultValue = 2


_RuijieHQoSTClassifierMatchV6Any_Type.__name__ = "TruthValue"
_RuijieHQoSTClassifierMatchV6Any_Object = MibTableColumn
ruijieHQoSTClassifierMatchV6Any = _RuijieHQoSTClassifierMatchV6Any_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 12),
    _RuijieHQoSTClassifierMatchV6Any_Type()
)
ruijieHQoSTClassifierMatchV6Any.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierMatchV6Any.setStatus("current")
_RuijieHQoSTClassifierMatchV6AclID_Type = Integer32
_RuijieHQoSTClassifierMatchV6AclID_Object = MibTableColumn
ruijieHQoSTClassifierMatchV6AclID = _RuijieHQoSTClassifierMatchV6AclID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 13),
    _RuijieHQoSTClassifierMatchV6AclID_Type()
)
ruijieHQoSTClassifierMatchV6AclID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierMatchV6AclID.setStatus("current")


class _RuijieHQoSTClassifierV6AclName_Type(OctetString):
    """Custom type ruijieHQoSTClassifierV6AclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSTClassifierV6AclName_Type.__name__ = "OctetString"
_RuijieHQoSTClassifierV6AclName_Object = MibTableColumn
ruijieHQoSTClassifierV6AclName = _RuijieHQoSTClassifierV6AclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 14),
    _RuijieHQoSTClassifierV6AclName_Type()
)
ruijieHQoSTClassifierV6AclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierV6AclName.setStatus("current")


class _RuijieHQoSTClassifierMatchV6Dscp_Type(Integer32):
    """Custom type ruijieHQoSTClassifierMatchV6Dscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieHQoSTClassifierMatchV6Dscp_Type.__name__ = "Integer32"
_RuijieHQoSTClassifierMatchV6Dscp_Object = MibTableColumn
ruijieHQoSTClassifierMatchV6Dscp = _RuijieHQoSTClassifierMatchV6Dscp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 15),
    _RuijieHQoSTClassifierMatchV6Dscp_Type()
)
ruijieHQoSTClassifierMatchV6Dscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierMatchV6Dscp.setStatus("current")


class _RuijieHQoSTClassifierMatchCos_Type(Integer32):
    """Custom type ruijieHQoSTClassifierMatchCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieHQoSTClassifierMatchCos_Type.__name__ = "Integer32"
_RuijieHQoSTClassifierMatchCos_Object = MibTableColumn
ruijieHQoSTClassifierMatchCos = _RuijieHQoSTClassifierMatchCos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 16),
    _RuijieHQoSTClassifierMatchCos_Type()
)
ruijieHQoSTClassifierMatchCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierMatchCos.setStatus("current")


class _RuijieHQoSTClassifierMatchExp_Type(Integer32):
    """Custom type ruijieHQoSTClassifierMatchExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieHQoSTClassifierMatchExp_Type.__name__ = "Integer32"
_RuijieHQoSTClassifierMatchExp_Object = MibTableColumn
ruijieHQoSTClassifierMatchExp = _RuijieHQoSTClassifierMatchExp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 17),
    _RuijieHQoSTClassifierMatchExp_Type()
)
ruijieHQoSTClassifierMatchExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierMatchExp.setStatus("current")
_RuijieHQoSTClassifierMatchSrcMac_Type = MacAddress
_RuijieHQoSTClassifierMatchSrcMac_Object = MibTableColumn
ruijieHQoSTClassifierMatchSrcMac = _RuijieHQoSTClassifierMatchSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 18),
    _RuijieHQoSTClassifierMatchSrcMac_Type()
)
ruijieHQoSTClassifierMatchSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierMatchSrcMac.setStatus("current")
_RuijieHQoSTClassifierMatchDstMac_Type = MacAddress
_RuijieHQoSTClassifierMatchDstMac_Object = MibTableColumn
ruijieHQoSTClassifierMatchDstMac = _RuijieHQoSTClassifierMatchDstMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 6, 2, 1, 19),
    _RuijieHQoSTClassifierMatchDstMac_Type()
)
ruijieHQoSTClassifierMatchDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTClassifierMatchDstMac.setStatus("current")
_RuijieHQoSTBehaviorObjects_ObjectIdentity = ObjectIdentity
ruijieHQoSTBehaviorObjects = _RuijieHQoSTBehaviorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 7)
)
_RuijieHQoSTBehaviorIndexNext_Type = Integer32
_RuijieHQoSTBehaviorIndexNext_Object = MibScalar
ruijieHQoSTBehaviorIndexNext = _RuijieHQoSTBehaviorIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 7, 1),
    _RuijieHQoSTBehaviorIndexNext_Type()
)
ruijieHQoSTBehaviorIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHQoSTBehaviorIndexNext.setStatus("current")
_RuijieHQoSTBehaviorTable_Object = MibTable
ruijieHQoSTBehaviorTable = _RuijieHQoSTBehaviorTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 7, 2)
)
if mibBuilder.loadTexts:
    ruijieHQoSTBehaviorTable.setStatus("current")
_RuijieHQoSTBehaviorEntry_Object = MibTableRow
ruijieHQoSTBehaviorEntry = _RuijieHQoSTBehaviorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 7, 2, 1)
)
ruijieHQoSTBehaviorEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieHQoSTBehaviorIndex"),
)
if mibBuilder.loadTexts:
    ruijieHQoSTBehaviorEntry.setStatus("current")
_RuijieHQoSTBehaviorIndex_Type = Unsigned32
_RuijieHQoSTBehaviorIndex_Object = MibTableColumn
ruijieHQoSTBehaviorIndex = _RuijieHQoSTBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 7, 2, 1, 1),
    _RuijieHQoSTBehaviorIndex_Type()
)
ruijieHQoSTBehaviorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieHQoSTBehaviorIndex.setStatus("current")


class _RuijieHQoSTBehaviorName_Type(OctetString):
    """Custom type ruijieHQoSTBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSTBehaviorName_Type.__name__ = "OctetString"
_RuijieHQoSTBehaviorName_Object = MibTableColumn
ruijieHQoSTBehaviorName = _RuijieHQoSTBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 7, 2, 1, 2),
    _RuijieHQoSTBehaviorName_Type()
)
ruijieHQoSTBehaviorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTBehaviorName.setStatus("current")
_RuijieHQoSTBehaviorRowStatus_Type = RowStatus
_RuijieHQoSTBehaviorRowStatus_Object = MibTableColumn
ruijieHQoSTBehaviorRowStatus = _RuijieHQoSTBehaviorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 7, 2, 1, 3),
    _RuijieHQoSTBehaviorRowStatus_Type()
)
ruijieHQoSTBehaviorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTBehaviorRowStatus.setStatus("current")


class _RuijieHQoSTBehaviorMask_Type(Bits):
    """Custom type ruijieHQoSTBehaviorMask based on Bits"""
    namedValues = NamedValues(
        *(("user-queue", 0),
          ("set-cos", 1),
          ("set-color", 2),
          ("remark-v4-dscp", 3),
          ("remark-v4-tos", 4),
          ("remark-v6-dscp", 5),
          ("remark-vlan-cos", 6),
          ("remark-exp", 7),
          ("sub-policy", 8))
    )

_RuijieHQoSTBehaviorMask_Type.__name__ = "Bits"
_RuijieHQoSTBehaviorMask_Object = MibTableColumn
ruijieHQoSTBehaviorMask = _RuijieHQoSTBehaviorMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 7, 2, 1, 4),
    _RuijieHQoSTBehaviorMask_Type()
)
ruijieHQoSTBehaviorMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTBehaviorMask.setStatus("current")


class _RuijieHQoSTBehaviorUserQName_Type(OctetString):
    """Custom type ruijieHQoSTBehaviorUserQName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSTBehaviorUserQName_Type.__name__ = "OctetString"
_RuijieHQoSTBehaviorUserQName_Object = MibTableColumn
ruijieHQoSTBehaviorUserQName = _RuijieHQoSTBehaviorUserQName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 7, 2, 1, 5),
    _RuijieHQoSTBehaviorUserQName_Type()
)
ruijieHQoSTBehaviorUserQName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTBehaviorUserQName.setStatus("current")
_RuijieHQoSTBehaviorUserQDir_Type = RuijieQDirectionType
_RuijieHQoSTBehaviorUserQDir_Object = MibTableColumn
ruijieHQoSTBehaviorUserQDir = _RuijieHQoSTBehaviorUserQDir_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 7, 2, 1, 6),
    _RuijieHQoSTBehaviorUserQDir_Type()
)
ruijieHQoSTBehaviorUserQDir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTBehaviorUserQDir.setStatus("current")


class _RuijieHQoSTBehaviorTCos_Type(RuijieCosType):
    """Custom type ruijieHQoSTBehaviorTCos based on RuijieCosType"""
    defaultValue = 1


_RuijieHQoSTBehaviorTCos_Type.__name__ = "RuijieCosType"
_RuijieHQoSTBehaviorTCos_Object = MibTableColumn
ruijieHQoSTBehaviorTCos = _RuijieHQoSTBehaviorTCos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 7, 2, 1, 7),
    _RuijieHQoSTBehaviorTCos_Type()
)
ruijieHQoSTBehaviorTCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTBehaviorTCos.setStatus("current")


class _RuijieHQoSTBehaviorTColor_Type(Integer32):
    """Custom type ruijieHQoSTBehaviorTColor based on Integer32"""
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
        *(("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_RuijieHQoSTBehaviorTColor_Type.__name__ = "Integer32"
_RuijieHQoSTBehaviorTColor_Object = MibTableColumn
ruijieHQoSTBehaviorTColor = _RuijieHQoSTBehaviorTColor_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 7, 2, 1, 8),
    _RuijieHQoSTBehaviorTColor_Type()
)
ruijieHQoSTBehaviorTColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTBehaviorTColor.setStatus("current")


class _RuijieHQoSTBehaviorRV4Dscp_Type(Integer32):
    """Custom type ruijieHQoSTBehaviorRV4Dscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RuijieHQoSTBehaviorRV4Dscp_Type.__name__ = "Integer32"
_RuijieHQoSTBehaviorRV4Dscp_Object = MibTableColumn
ruijieHQoSTBehaviorRV4Dscp = _RuijieHQoSTBehaviorRV4Dscp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 7, 2, 1, 9),
    _RuijieHQoSTBehaviorRV4Dscp_Type()
)
ruijieHQoSTBehaviorRV4Dscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTBehaviorRV4Dscp.setStatus("current")


class _RuijieHQoSTBehaviorRV4Tos_Type(Integer32):
    """Custom type ruijieHQoSTBehaviorRV4Tos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieHQoSTBehaviorRV4Tos_Type.__name__ = "Integer32"
_RuijieHQoSTBehaviorRV4Tos_Object = MibTableColumn
ruijieHQoSTBehaviorRV4Tos = _RuijieHQoSTBehaviorRV4Tos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 7, 2, 1, 10),
    _RuijieHQoSTBehaviorRV4Tos_Type()
)
ruijieHQoSTBehaviorRV4Tos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTBehaviorRV4Tos.setStatus("current")


class _RuijieHQoSTBehaviorRV6Dscp_Type(Integer32):
    """Custom type ruijieHQoSTBehaviorRV6Dscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieHQoSTBehaviorRV6Dscp_Type.__name__ = "Integer32"
_RuijieHQoSTBehaviorRV6Dscp_Object = MibTableColumn
ruijieHQoSTBehaviorRV6Dscp = _RuijieHQoSTBehaviorRV6Dscp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 7, 2, 1, 11),
    _RuijieHQoSTBehaviorRV6Dscp_Type()
)
ruijieHQoSTBehaviorRV6Dscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTBehaviorRV6Dscp.setStatus("current")


class _RuijieHQoSTBehaviorRVlanCos_Type(Integer32):
    """Custom type ruijieHQoSTBehaviorRVlanCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieHQoSTBehaviorRVlanCos_Type.__name__ = "Integer32"
_RuijieHQoSTBehaviorRVlanCos_Object = MibTableColumn
ruijieHQoSTBehaviorRVlanCos = _RuijieHQoSTBehaviorRVlanCos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 7, 2, 1, 12),
    _RuijieHQoSTBehaviorRVlanCos_Type()
)
ruijieHQoSTBehaviorRVlanCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTBehaviorRVlanCos.setStatus("current")


class _RuijieHQoSTBehaviorRExp_Type(Integer32):
    """Custom type ruijieHQoSTBehaviorRExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieHQoSTBehaviorRExp_Type.__name__ = "Integer32"
_RuijieHQoSTBehaviorRExp_Object = MibTableColumn
ruijieHQoSTBehaviorRExp = _RuijieHQoSTBehaviorRExp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 7, 2, 1, 13),
    _RuijieHQoSTBehaviorRExp_Type()
)
ruijieHQoSTBehaviorRExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTBehaviorRExp.setStatus("current")


class _RuijieHQoSTBehaviorSubPolicyName_Type(OctetString):
    """Custom type ruijieHQoSTBehaviorSubPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSTBehaviorSubPolicyName_Type.__name__ = "OctetString"
_RuijieHQoSTBehaviorSubPolicyName_Object = MibTableColumn
ruijieHQoSTBehaviorSubPolicyName = _RuijieHQoSTBehaviorSubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 7, 2, 1, 14),
    _RuijieHQoSTBehaviorSubPolicyName_Type()
)
ruijieHQoSTBehaviorSubPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTBehaviorSubPolicyName.setStatus("current")
_RuijieHQoSTPolicyObjects_ObjectIdentity = ObjectIdentity
ruijieHQoSTPolicyObjects = _RuijieHQoSTPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8)
)
_RuijieHQoSTPolicyIndexNext_Type = Integer32
_RuijieHQoSTPolicyIndexNext_Object = MibScalar
ruijieHQoSTPolicyIndexNext = _RuijieHQoSTPolicyIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8, 1),
    _RuijieHQoSTPolicyIndexNext_Type()
)
ruijieHQoSTPolicyIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHQoSTPolicyIndexNext.setStatus("current")
_RuijieHQoSTPolicyTable_Object = MibTable
ruijieHQoSTPolicyTable = _RuijieHQoSTPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8, 2)
)
if mibBuilder.loadTexts:
    ruijieHQoSTPolicyTable.setStatus("current")
_RuijieHQoSTPolicyEntry_Object = MibTableRow
ruijieHQoSTPolicyEntry = _RuijieHQoSTPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8, 2, 1)
)
ruijieHQoSTPolicyEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieHQoSTPolicyIndex"),
)
if mibBuilder.loadTexts:
    ruijieHQoSTPolicyEntry.setStatus("current")
_RuijieHQoSTPolicyIndex_Type = Unsigned32
_RuijieHQoSTPolicyIndex_Object = MibTableColumn
ruijieHQoSTPolicyIndex = _RuijieHQoSTPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8, 2, 1, 1),
    _RuijieHQoSTPolicyIndex_Type()
)
ruijieHQoSTPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieHQoSTPolicyIndex.setStatus("current")


class _RuijieHQoSTPolicyName_Type(OctetString):
    """Custom type ruijieHQoSTPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSTPolicyName_Type.__name__ = "OctetString"
_RuijieHQoSTPolicyName_Object = MibTableColumn
ruijieHQoSTPolicyName = _RuijieHQoSTPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8, 2, 1, 2),
    _RuijieHQoSTPolicyName_Type()
)
ruijieHQoSTPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTPolicyName.setStatus("current")
_RuijieHQoSTPolicyRowStatus_Type = RowStatus
_RuijieHQoSTPolicyRowStatus_Object = MibTableColumn
ruijieHQoSTPolicyRowStatus = _RuijieHQoSTPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8, 2, 1, 3),
    _RuijieHQoSTPolicyRowStatus_Type()
)
ruijieHQoSTPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTPolicyRowStatus.setStatus("current")
_RuijieHQoSTPolicyMapIndexNext_Type = Integer32
_RuijieHQoSTPolicyMapIndexNext_Object = MibScalar
ruijieHQoSTPolicyMapIndexNext = _RuijieHQoSTPolicyMapIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8, 3),
    _RuijieHQoSTPolicyMapIndexNext_Type()
)
ruijieHQoSTPolicyMapIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHQoSTPolicyMapIndexNext.setStatus("current")
_RuijieHQoSTPolicyMapTable_Object = MibTable
ruijieHQoSTPolicyMapTable = _RuijieHQoSTPolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8, 4)
)
if mibBuilder.loadTexts:
    ruijieHQoSTPolicyMapTable.setStatus("current")
_RuijieHQoSTPolicyMapEntry_Object = MibTableRow
ruijieHQoSTPolicyMapEntry = _RuijieHQoSTPolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8, 4, 1)
)
ruijieHQoSTPolicyMapEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieHQoSTPolicyMapIndex"),
)
if mibBuilder.loadTexts:
    ruijieHQoSTPolicyMapEntry.setStatus("current")
_RuijieHQoSTPolicyMapIndex_Type = Unsigned32
_RuijieHQoSTPolicyMapIndex_Object = MibTableColumn
ruijieHQoSTPolicyMapIndex = _RuijieHQoSTPolicyMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8, 4, 1, 1),
    _RuijieHQoSTPolicyMapIndex_Type()
)
ruijieHQoSTPolicyMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieHQoSTPolicyMapIndex.setStatus("current")


class _RuijieHQoSTPolicyMapPolicyName_Type(OctetString):
    """Custom type ruijieHQoSTPolicyMapPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSTPolicyMapPolicyName_Type.__name__ = "OctetString"
_RuijieHQoSTPolicyMapPolicyName_Object = MibTableColumn
ruijieHQoSTPolicyMapPolicyName = _RuijieHQoSTPolicyMapPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8, 4, 1, 2),
    _RuijieHQoSTPolicyMapPolicyName_Type()
)
ruijieHQoSTPolicyMapPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTPolicyMapPolicyName.setStatus("current")
_RuijieHQoSTPolicyMapPolicyIndex_Type = Unsigned32
_RuijieHQoSTPolicyMapPolicyIndex_Object = MibTableColumn
ruijieHQoSTPolicyMapPolicyIndex = _RuijieHQoSTPolicyMapPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8, 4, 1, 3),
    _RuijieHQoSTPolicyMapPolicyIndex_Type()
)
ruijieHQoSTPolicyMapPolicyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTPolicyMapPolicyIndex.setStatus("current")


class _RuijieHQoSTPolicyMapTClassfierName_Type(OctetString):
    """Custom type ruijieHQoSTPolicyMapTClassfierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSTPolicyMapTClassfierName_Type.__name__ = "OctetString"
_RuijieHQoSTPolicyMapTClassfierName_Object = MibTableColumn
ruijieHQoSTPolicyMapTClassfierName = _RuijieHQoSTPolicyMapTClassfierName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8, 4, 1, 4),
    _RuijieHQoSTPolicyMapTClassfierName_Type()
)
ruijieHQoSTPolicyMapTClassfierName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTPolicyMapTClassfierName.setStatus("current")
_RuijieHQoSTPolicyMapTClassfierIndex_Type = Unsigned32
_RuijieHQoSTPolicyMapTClassfierIndex_Object = MibTableColumn
ruijieHQoSTPolicyMapTClassfierIndex = _RuijieHQoSTPolicyMapTClassfierIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8, 4, 1, 5),
    _RuijieHQoSTPolicyMapTClassfierIndex_Type()
)
ruijieHQoSTPolicyMapTClassfierIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTPolicyMapTClassfierIndex.setStatus("current")


class _RuijieHQoSTPolicyMapTBehaviorName_Type(OctetString):
    """Custom type ruijieHQoSTPolicyMapTBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSTPolicyMapTBehaviorName_Type.__name__ = "OctetString"
_RuijieHQoSTPolicyMapTBehaviorName_Object = MibTableColumn
ruijieHQoSTPolicyMapTBehaviorName = _RuijieHQoSTPolicyMapTBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8, 4, 1, 6),
    _RuijieHQoSTPolicyMapTBehaviorName_Type()
)
ruijieHQoSTPolicyMapTBehaviorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTPolicyMapTBehaviorName.setStatus("current")
_RuijieHQoSTPolicyMapTBehaviorIndex_Type = Unsigned32
_RuijieHQoSTPolicyMapTBehaviorIndex_Object = MibTableColumn
ruijieHQoSTPolicyMapTBehaviorIndex = _RuijieHQoSTPolicyMapTBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8, 4, 1, 7),
    _RuijieHQoSTPolicyMapTBehaviorIndex_Type()
)
ruijieHQoSTPolicyMapTBehaviorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTPolicyMapTBehaviorIndex.setStatus("current")


class _RuijieHQoSTPolicyMapPrecedence_Type(Unsigned32):
    """Custom type ruijieHQoSTPolicyMapPrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_RuijieHQoSTPolicyMapPrecedence_Type.__name__ = "Unsigned32"
_RuijieHQoSTPolicyMapPrecedence_Object = MibTableColumn
ruijieHQoSTPolicyMapPrecedence = _RuijieHQoSTPolicyMapPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8, 4, 1, 8),
    _RuijieHQoSTPolicyMapPrecedence_Type()
)
ruijieHQoSTPolicyMapPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTPolicyMapPrecedence.setStatus("current")
_RuijieHQoSTPolicyMapRowStatus_Type = RowStatus
_RuijieHQoSTPolicyMapRowStatus_Object = MibTableColumn
ruijieHQoSTPolicyMapRowStatus = _RuijieHQoSTPolicyMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 8, 4, 1, 9),
    _RuijieHQoSTPolicyMapRowStatus_Type()
)
ruijieHQoSTPolicyMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSTPolicyMapRowStatus.setStatus("current")
_RuijieHQoSVoQObjects_ObjectIdentity = ObjectIdentity
ruijieHQoSVoQObjects = _RuijieHQoSVoQObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 9)
)


class _RuijieHQoSVoQEnable_Type(TruthValue):
    """Custom type ruijieHQoSVoQEnable based on TruthValue"""
    defaultValue = 2


_RuijieHQoSVoQEnable_Type.__name__ = "TruthValue"
_RuijieHQoSVoQEnable_Object = MibScalar
ruijieHQoSVoQEnable = _RuijieHQoSVoQEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 9, 1),
    _RuijieHQoSVoQEnable_Type()
)
ruijieHQoSVoQEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieHQoSVoQEnable.setStatus("current")
_RuijieHQoSVoQDeviceTable_Object = MibTable
ruijieHQoSVoQDeviceTable = _RuijieHQoSVoQDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 9, 2)
)
if mibBuilder.loadTexts:
    ruijieHQoSVoQDeviceTable.setStatus("current")
_RuijieHQoSVoQDeviceEntry_Object = MibTableRow
ruijieHQoSVoQDeviceEntry = _RuijieHQoSVoQDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 9, 2, 1)
)
ruijieHQoSVoQDeviceEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieHQoSVoQDeviceId"),
)
if mibBuilder.loadTexts:
    ruijieHQoSVoQDeviceEntry.setStatus("current")
_RuijieHQoSVoQDeviceId_Type = Unsigned32
_RuijieHQoSVoQDeviceId_Object = MibTableColumn
ruijieHQoSVoQDeviceId = _RuijieHQoSVoQDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 9, 2, 1, 1),
    _RuijieHQoSVoQDeviceId_Type()
)
ruijieHQoSVoQDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieHQoSVoQDeviceId.setStatus("current")
_RuijieHQoSVoQDeviceCredit_Type = Unsigned32
_RuijieHQoSVoQDeviceCredit_Object = MibTableColumn
ruijieHQoSVoQDeviceCredit = _RuijieHQoSVoQDeviceCredit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 9, 2, 1, 2),
    _RuijieHQoSVoQDeviceCredit_Type()
)
ruijieHQoSVoQDeviceCredit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieHQoSVoQDeviceCredit.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSVoQDeviceCredit.setUnits("Mbit/s")
_RuijieHQoSPortQObjects_ObjectIdentity = ObjectIdentity
ruijieHQoSPortQObjects = _RuijieHQoSPortQObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10)
)
_RuijieHQoSPortQIndexNext_Type = Integer32
_RuijieHQoSPortQIndexNext_Object = MibScalar
ruijieHQoSPortQIndexNext = _RuijieHQoSPortQIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 1),
    _RuijieHQoSPortQIndexNext_Type()
)
ruijieHQoSPortQIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHQoSPortQIndexNext.setStatus("current")
_RuijieHQoSPortQTable_Object = MibTable
ruijieHQoSPortQTable = _RuijieHQoSPortQTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2)
)
if mibBuilder.loadTexts:
    ruijieHQoSPortQTable.setStatus("current")
_RuijieHQoSPortQEntry_Object = MibTableRow
ruijieHQoSPortQEntry = _RuijieHQoSPortQEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1)
)
ruijieHQoSPortQEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieHQoSPortQIndex"),
)
if mibBuilder.loadTexts:
    ruijieHQoSPortQEntry.setStatus("current")
_RuijieHQoSPortQIndex_Type = Unsigned32
_RuijieHQoSPortQIndex_Object = MibTableColumn
ruijieHQoSPortQIndex = _RuijieHQoSPortQIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 1),
    _RuijieHQoSPortQIndex_Type()
)
ruijieHQoSPortQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieHQoSPortQIndex.setStatus("current")


class _RuijieHQoSPortQName_Type(OctetString):
    """Custom type ruijieHQoSPortQName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSPortQName_Type.__name__ = "OctetString"
_RuijieHQoSPortQName_Object = MibTableColumn
ruijieHQoSPortQName = _RuijieHQoSPortQName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 2),
    _RuijieHQoSPortQName_Type()
)
ruijieHQoSPortQName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQName.setStatus("current")
_RuijieHQoSPortQRowStatus_Type = RowStatus
_RuijieHQoSPortQRowStatus_Object = MibTableColumn
ruijieHQoSPortQRowStatus = _RuijieHQoSPortQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 3),
    _RuijieHQoSPortQRowStatus_Type()
)
ruijieHQoSPortQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQRowStatus.setStatus("current")


class _RuijieHQoSPortQBEQType_Type(RuijieQType):
    """Custom type ruijieHQoSPortQBEQType based on RuijieQType"""
    defaultValue = 2


_RuijieHQoSPortQBEQType_Type.__name__ = "RuijieQType"
_RuijieHQoSPortQBEQType_Object = MibTableColumn
ruijieHQoSPortQBEQType = _RuijieHQoSPortQBEQType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 4),
    _RuijieHQoSPortQBEQType_Type()
)
ruijieHQoSPortQBEQType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQBEQType.setStatus("current")


class _RuijieHQoSPortQBEQWredWeight_Type(Integer32):
    """Custom type ruijieHQoSPortQBEQWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_RuijieHQoSPortQBEQWredWeight_Type.__name__ = "Integer32"
_RuijieHQoSPortQBEQWredWeight_Object = MibTableColumn
ruijieHQoSPortQBEQWredWeight = _RuijieHQoSPortQBEQWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 5),
    _RuijieHQoSPortQBEQWredWeight_Type()
)
ruijieHQoSPortQBEQWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQBEQWredWeight.setStatus("current")


class _RuijieHQoSPortQBEQWredName_Type(OctetString):
    """Custom type ruijieHQoSPortQBEQWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSPortQBEQWredName_Type.__name__ = "OctetString"
_RuijieHQoSPortQBEQWredName_Object = MibTableColumn
ruijieHQoSPortQBEQWredName = _RuijieHQoSPortQBEQWredName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 6),
    _RuijieHQoSPortQBEQWredName_Type()
)
ruijieHQoSPortQBEQWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQBEQWredName.setStatus("current")


class _RuijieHQoSPortQBEQDepth_Type(Integer32):
    """Custom type ruijieHQoSPortQBEQDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieHQoSPortQBEQDepth_Type.__name__ = "Integer32"
_RuijieHQoSPortQBEQDepth_Object = MibTableColumn
ruijieHQoSPortQBEQDepth = _RuijieHQoSPortQBEQDepth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 7),
    _RuijieHQoSPortQBEQDepth_Type()
)
ruijieHQoSPortQBEQDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQBEQDepth.setStatus("current")


class _RuijieHQoSPortQBEQShaping_Type(Integer32):
    """Custom type ruijieHQoSPortQBEQShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RuijieHQoSPortQBEQShaping_Type.__name__ = "Integer32"
_RuijieHQoSPortQBEQShaping_Object = MibTableColumn
ruijieHQoSPortQBEQShaping = _RuijieHQoSPortQBEQShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 8),
    _RuijieHQoSPortQBEQShaping_Type()
)
ruijieHQoSPortQBEQShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQBEQShaping.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSPortQBEQShaping.setUnits("kilobits per second")


class _RuijieHQoSPortQAF1QType_Type(RuijieQType):
    """Custom type ruijieHQoSPortQAF1QType based on RuijieQType"""
    defaultValue = 2


_RuijieHQoSPortQAF1QType_Type.__name__ = "RuijieQType"
_RuijieHQoSPortQAF1QType_Object = MibTableColumn
ruijieHQoSPortQAF1QType = _RuijieHQoSPortQAF1QType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 9),
    _RuijieHQoSPortQAF1QType_Type()
)
ruijieHQoSPortQAF1QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF1QType.setStatus("current")


class _RuijieHQoSPortQAF1QWredWeight_Type(Integer32):
    """Custom type ruijieHQoSPortQAF1QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_RuijieHQoSPortQAF1QWredWeight_Type.__name__ = "Integer32"
_RuijieHQoSPortQAF1QWredWeight_Object = MibTableColumn
ruijieHQoSPortQAF1QWredWeight = _RuijieHQoSPortQAF1QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 10),
    _RuijieHQoSPortQAF1QWredWeight_Type()
)
ruijieHQoSPortQAF1QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF1QWredWeight.setStatus("current")


class _RuijieHQoSPortQAF1QWredName_Type(OctetString):
    """Custom type ruijieHQoSPortQAF1QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSPortQAF1QWredName_Type.__name__ = "OctetString"
_RuijieHQoSPortQAF1QWredName_Object = MibTableColumn
ruijieHQoSPortQAF1QWredName = _RuijieHQoSPortQAF1QWredName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 11),
    _RuijieHQoSPortQAF1QWredName_Type()
)
ruijieHQoSPortQAF1QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF1QWredName.setStatus("current")


class _RuijieHQoSPortQAF1QDepth_Type(Integer32):
    """Custom type ruijieHQoSPortQAF1QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieHQoSPortQAF1QDepth_Type.__name__ = "Integer32"
_RuijieHQoSPortQAF1QDepth_Object = MibTableColumn
ruijieHQoSPortQAF1QDepth = _RuijieHQoSPortQAF1QDepth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 12),
    _RuijieHQoSPortQAF1QDepth_Type()
)
ruijieHQoSPortQAF1QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF1QDepth.setStatus("current")


class _RuijieHQoSPortQAF1QShaping_Type(Integer32):
    """Custom type ruijieHQoSPortQAF1QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RuijieHQoSPortQAF1QShaping_Type.__name__ = "Integer32"
_RuijieHQoSPortQAF1QShaping_Object = MibTableColumn
ruijieHQoSPortQAF1QShaping = _RuijieHQoSPortQAF1QShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 13),
    _RuijieHQoSPortQAF1QShaping_Type()
)
ruijieHQoSPortQAF1QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF1QShaping.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF1QShaping.setUnits("kilobits per second")


class _RuijieHQoSPortQAF2QType_Type(RuijieQType):
    """Custom type ruijieHQoSPortQAF2QType based on RuijieQType"""
    defaultValue = 2


_RuijieHQoSPortQAF2QType_Type.__name__ = "RuijieQType"
_RuijieHQoSPortQAF2QType_Object = MibTableColumn
ruijieHQoSPortQAF2QType = _RuijieHQoSPortQAF2QType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 14),
    _RuijieHQoSPortQAF2QType_Type()
)
ruijieHQoSPortQAF2QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF2QType.setStatus("current")


class _RuijieHQoSPortQAF2QWredWeight_Type(Integer32):
    """Custom type ruijieHQoSPortQAF2QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_RuijieHQoSPortQAF2QWredWeight_Type.__name__ = "Integer32"
_RuijieHQoSPortQAF2QWredWeight_Object = MibTableColumn
ruijieHQoSPortQAF2QWredWeight = _RuijieHQoSPortQAF2QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 15),
    _RuijieHQoSPortQAF2QWredWeight_Type()
)
ruijieHQoSPortQAF2QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF2QWredWeight.setStatus("current")


class _RuijieHQoSPortQAF2QWredName_Type(OctetString):
    """Custom type ruijieHQoSPortQAF2QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSPortQAF2QWredName_Type.__name__ = "OctetString"
_RuijieHQoSPortQAF2QWredName_Object = MibTableColumn
ruijieHQoSPortQAF2QWredName = _RuijieHQoSPortQAF2QWredName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 16),
    _RuijieHQoSPortQAF2QWredName_Type()
)
ruijieHQoSPortQAF2QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF2QWredName.setStatus("current")


class _RuijieHQoSPortQAF2QDepth_Type(Integer32):
    """Custom type ruijieHQoSPortQAF2QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieHQoSPortQAF2QDepth_Type.__name__ = "Integer32"
_RuijieHQoSPortQAF2QDepth_Object = MibTableColumn
ruijieHQoSPortQAF2QDepth = _RuijieHQoSPortQAF2QDepth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 17),
    _RuijieHQoSPortQAF2QDepth_Type()
)
ruijieHQoSPortQAF2QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF2QDepth.setStatus("current")


class _RuijieHQoSPortQAF2QShaping_Type(Integer32):
    """Custom type ruijieHQoSPortQAF2QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RuijieHQoSPortQAF2QShaping_Type.__name__ = "Integer32"
_RuijieHQoSPortQAF2QShaping_Object = MibTableColumn
ruijieHQoSPortQAF2QShaping = _RuijieHQoSPortQAF2QShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 18),
    _RuijieHQoSPortQAF2QShaping_Type()
)
ruijieHQoSPortQAF2QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF2QShaping.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF2QShaping.setUnits("kilobits per second")


class _RuijieHQoSPortQAF3QType_Type(RuijieQType):
    """Custom type ruijieHQoSPortQAF3QType based on RuijieQType"""
    defaultValue = 2


_RuijieHQoSPortQAF3QType_Type.__name__ = "RuijieQType"
_RuijieHQoSPortQAF3QType_Object = MibTableColumn
ruijieHQoSPortQAF3QType = _RuijieHQoSPortQAF3QType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 19),
    _RuijieHQoSPortQAF3QType_Type()
)
ruijieHQoSPortQAF3QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF3QType.setStatus("current")


class _RuijieHQoSPortQAF3QWredWeight_Type(Integer32):
    """Custom type ruijieHQoSPortQAF3QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_RuijieHQoSPortQAF3QWredWeight_Type.__name__ = "Integer32"
_RuijieHQoSPortQAF3QWredWeight_Object = MibTableColumn
ruijieHQoSPortQAF3QWredWeight = _RuijieHQoSPortQAF3QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 20),
    _RuijieHQoSPortQAF3QWredWeight_Type()
)
ruijieHQoSPortQAF3QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF3QWredWeight.setStatus("current")


class _RuijieHQoSPortQAF3QWredName_Type(OctetString):
    """Custom type ruijieHQoSPortQAF3QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSPortQAF3QWredName_Type.__name__ = "OctetString"
_RuijieHQoSPortQAF3QWredName_Object = MibTableColumn
ruijieHQoSPortQAF3QWredName = _RuijieHQoSPortQAF3QWredName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 21),
    _RuijieHQoSPortQAF3QWredName_Type()
)
ruijieHQoSPortQAF3QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF3QWredName.setStatus("current")


class _RuijieHQoSPortQAF3QDepth_Type(Integer32):
    """Custom type ruijieHQoSPortQAF3QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieHQoSPortQAF3QDepth_Type.__name__ = "Integer32"
_RuijieHQoSPortQAF3QDepth_Object = MibTableColumn
ruijieHQoSPortQAF3QDepth = _RuijieHQoSPortQAF3QDepth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 22),
    _RuijieHQoSPortQAF3QDepth_Type()
)
ruijieHQoSPortQAF3QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF3QDepth.setStatus("current")


class _RuijieHQoSPortQAF3QShaping_Type(Integer32):
    """Custom type ruijieHQoSPortQAF3QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RuijieHQoSPortQAF3QShaping_Type.__name__ = "Integer32"
_RuijieHQoSPortQAF3QShaping_Object = MibTableColumn
ruijieHQoSPortQAF3QShaping = _RuijieHQoSPortQAF3QShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 23),
    _RuijieHQoSPortQAF3QShaping_Type()
)
ruijieHQoSPortQAF3QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF3QShaping.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF3QShaping.setUnits("kilobits per second")


class _RuijieHQoSPortQAF4QType_Type(RuijieQType):
    """Custom type ruijieHQoSPortQAF4QType based on RuijieQType"""
    defaultValue = 2


_RuijieHQoSPortQAF4QType_Type.__name__ = "RuijieQType"
_RuijieHQoSPortQAF4QType_Object = MibTableColumn
ruijieHQoSPortQAF4QType = _RuijieHQoSPortQAF4QType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 24),
    _RuijieHQoSPortQAF4QType_Type()
)
ruijieHQoSPortQAF4QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF4QType.setStatus("current")


class _RuijieHQoSPortQAF4QWredWeight_Type(Integer32):
    """Custom type ruijieHQoSPortQAF4QWredWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_RuijieHQoSPortQAF4QWredWeight_Type.__name__ = "Integer32"
_RuijieHQoSPortQAF4QWredWeight_Object = MibTableColumn
ruijieHQoSPortQAF4QWredWeight = _RuijieHQoSPortQAF4QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 25),
    _RuijieHQoSPortQAF4QWredWeight_Type()
)
ruijieHQoSPortQAF4QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF4QWredWeight.setStatus("current")


class _RuijieHQoSPortQAF4QWredName_Type(OctetString):
    """Custom type ruijieHQoSPortQAF4QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSPortQAF4QWredName_Type.__name__ = "OctetString"
_RuijieHQoSPortQAF4QWredName_Object = MibTableColumn
ruijieHQoSPortQAF4QWredName = _RuijieHQoSPortQAF4QWredName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 26),
    _RuijieHQoSPortQAF4QWredName_Type()
)
ruijieHQoSPortQAF4QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF4QWredName.setStatus("current")


class _RuijieHQoSPortQAF4QDepth_Type(Integer32):
    """Custom type ruijieHQoSPortQAF4QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieHQoSPortQAF4QDepth_Type.__name__ = "Integer32"
_RuijieHQoSPortQAF4QDepth_Object = MibTableColumn
ruijieHQoSPortQAF4QDepth = _RuijieHQoSPortQAF4QDepth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 27),
    _RuijieHQoSPortQAF4QDepth_Type()
)
ruijieHQoSPortQAF4QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF4QDepth.setStatus("current")


class _RuijieHQoSPortQAF4QShaping_Type(Integer32):
    """Custom type ruijieHQoSPortQAF4QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RuijieHQoSPortQAF4QShaping_Type.__name__ = "Integer32"
_RuijieHQoSPortQAF4QShaping_Object = MibTableColumn
ruijieHQoSPortQAF4QShaping = _RuijieHQoSPortQAF4QShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 28),
    _RuijieHQoSPortQAF4QShaping_Type()
)
ruijieHQoSPortQAF4QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF4QShaping.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSPortQAF4QShaping.setUnits("kilobits per second")


class _RuijieHQoSPortQEFQType_Type(RuijieQType):
    """Custom type ruijieHQoSPortQEFQType based on RuijieQType"""
    defaultValue = 3


_RuijieHQoSPortQEFQType_Type.__name__ = "RuijieQType"
_RuijieHQoSPortQEFQType_Object = MibTableColumn
ruijieHQoSPortQEFQType = _RuijieHQoSPortQEFQType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 29),
    _RuijieHQoSPortQEFQType_Type()
)
ruijieHQoSPortQEFQType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQEFQType.setStatus("current")


class _RuijieHQoSPortQEFQWredWeight_Type(Integer32):
    """Custom type ruijieHQoSPortQEFQWredWeight based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_RuijieHQoSPortQEFQWredWeight_Type.__name__ = "Integer32"
_RuijieHQoSPortQEFQWredWeight_Object = MibTableColumn
ruijieHQoSPortQEFQWredWeight = _RuijieHQoSPortQEFQWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 30),
    _RuijieHQoSPortQEFQWredWeight_Type()
)
ruijieHQoSPortQEFQWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQEFQWredWeight.setStatus("current")


class _RuijieHQoSPortQEFQWredName_Type(OctetString):
    """Custom type ruijieHQoSPortQEFQWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSPortQEFQWredName_Type.__name__ = "OctetString"
_RuijieHQoSPortQEFQWredName_Object = MibTableColumn
ruijieHQoSPortQEFQWredName = _RuijieHQoSPortQEFQWredName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 31),
    _RuijieHQoSPortQEFQWredName_Type()
)
ruijieHQoSPortQEFQWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQEFQWredName.setStatus("current")


class _RuijieHQoSPortQEFQDepth_Type(Integer32):
    """Custom type ruijieHQoSPortQEFQDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieHQoSPortQEFQDepth_Type.__name__ = "Integer32"
_RuijieHQoSPortQEFQDepth_Object = MibTableColumn
ruijieHQoSPortQEFQDepth = _RuijieHQoSPortQEFQDepth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 32),
    _RuijieHQoSPortQEFQDepth_Type()
)
ruijieHQoSPortQEFQDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQEFQDepth.setStatus("current")


class _RuijieHQoSPortQEFQShaping_Type(Integer32):
    """Custom type ruijieHQoSPortQEFQShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RuijieHQoSPortQEFQShaping_Type.__name__ = "Integer32"
_RuijieHQoSPortQEFQShaping_Object = MibTableColumn
ruijieHQoSPortQEFQShaping = _RuijieHQoSPortQEFQShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 33),
    _RuijieHQoSPortQEFQShaping_Type()
)
ruijieHQoSPortQEFQShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQEFQShaping.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSPortQEFQShaping.setUnits("kilobits per second")


class _RuijieHQoSPortQCS6QType_Type(RuijieQType):
    """Custom type ruijieHQoSPortQCS6QType based on RuijieQType"""
    defaultValue = 3


_RuijieHQoSPortQCS6QType_Type.__name__ = "RuijieQType"
_RuijieHQoSPortQCS6QType_Object = MibTableColumn
ruijieHQoSPortQCS6QType = _RuijieHQoSPortQCS6QType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 34),
    _RuijieHQoSPortQCS6QType_Type()
)
ruijieHQoSPortQCS6QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQCS6QType.setStatus("current")


class _RuijieHQoSPortQCS6QWredWeight_Type(Integer32):
    """Custom type ruijieHQoSPortQCS6QWredWeight based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_RuijieHQoSPortQCS6QWredWeight_Type.__name__ = "Integer32"
_RuijieHQoSPortQCS6QWredWeight_Object = MibTableColumn
ruijieHQoSPortQCS6QWredWeight = _RuijieHQoSPortQCS6QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 35),
    _RuijieHQoSPortQCS6QWredWeight_Type()
)
ruijieHQoSPortQCS6QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQCS6QWredWeight.setStatus("current")


class _RuijieHQoSPortQCS6QWredName_Type(OctetString):
    """Custom type ruijieHQoSPortQCS6QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSPortQCS6QWredName_Type.__name__ = "OctetString"
_RuijieHQoSPortQCS6QWredName_Object = MibTableColumn
ruijieHQoSPortQCS6QWredName = _RuijieHQoSPortQCS6QWredName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 36),
    _RuijieHQoSPortQCS6QWredName_Type()
)
ruijieHQoSPortQCS6QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQCS6QWredName.setStatus("current")


class _RuijieHQoSPortQCS6QDepth_Type(Integer32):
    """Custom type ruijieHQoSPortQCS6QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieHQoSPortQCS6QDepth_Type.__name__ = "Integer32"
_RuijieHQoSPortQCS6QDepth_Object = MibTableColumn
ruijieHQoSPortQCS6QDepth = _RuijieHQoSPortQCS6QDepth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 37),
    _RuijieHQoSPortQCS6QDepth_Type()
)
ruijieHQoSPortQCS6QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQCS6QDepth.setStatus("current")


class _RuijieHQoSPortQCS6QShaping_Type(Integer32):
    """Custom type ruijieHQoSPortQCS6QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RuijieHQoSPortQCS6QShaping_Type.__name__ = "Integer32"
_RuijieHQoSPortQCS6QShaping_Object = MibTableColumn
ruijieHQoSPortQCS6QShaping = _RuijieHQoSPortQCS6QShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 38),
    _RuijieHQoSPortQCS6QShaping_Type()
)
ruijieHQoSPortQCS6QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQCS6QShaping.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSPortQCS6QShaping.setUnits("kilobits per second")


class _RuijieHQoSPortQCS7QType_Type(RuijieQType):
    """Custom type ruijieHQoSPortQCS7QType based on RuijieQType"""
    defaultValue = 3


_RuijieHQoSPortQCS7QType_Type.__name__ = "RuijieQType"
_RuijieHQoSPortQCS7QType_Object = MibTableColumn
ruijieHQoSPortQCS7QType = _RuijieHQoSPortQCS7QType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 39),
    _RuijieHQoSPortQCS7QType_Type()
)
ruijieHQoSPortQCS7QType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQCS7QType.setStatus("current")


class _RuijieHQoSPortQCS7QWredWeight_Type(Integer32):
    """Custom type ruijieHQoSPortQCS7QWredWeight based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_RuijieHQoSPortQCS7QWredWeight_Type.__name__ = "Integer32"
_RuijieHQoSPortQCS7QWredWeight_Object = MibTableColumn
ruijieHQoSPortQCS7QWredWeight = _RuijieHQoSPortQCS7QWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 40),
    _RuijieHQoSPortQCS7QWredWeight_Type()
)
ruijieHQoSPortQCS7QWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQCS7QWredWeight.setStatus("current")


class _RuijieHQoSPortQCS7QWredName_Type(OctetString):
    """Custom type ruijieHQoSPortQCS7QWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSPortQCS7QWredName_Type.__name__ = "OctetString"
_RuijieHQoSPortQCS7QWredName_Object = MibTableColumn
ruijieHQoSPortQCS7QWredName = _RuijieHQoSPortQCS7QWredName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 41),
    _RuijieHQoSPortQCS7QWredName_Type()
)
ruijieHQoSPortQCS7QWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQCS7QWredName.setStatus("current")


class _RuijieHQoSPortQCS7QDepth_Type(Integer32):
    """Custom type ruijieHQoSPortQCS7QDepth based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuijieHQoSPortQCS7QDepth_Type.__name__ = "Integer32"
_RuijieHQoSPortQCS7QDepth_Object = MibTableColumn
ruijieHQoSPortQCS7QDepth = _RuijieHQoSPortQCS7QDepth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 42),
    _RuijieHQoSPortQCS7QDepth_Type()
)
ruijieHQoSPortQCS7QDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQCS7QDepth.setStatus("current")


class _RuijieHQoSPortQCS7QShaping_Type(Integer32):
    """Custom type ruijieHQoSPortQCS7QShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RuijieHQoSPortQCS7QShaping_Type.__name__ = "Integer32"
_RuijieHQoSPortQCS7QShaping_Object = MibTableColumn
ruijieHQoSPortQCS7QShaping = _RuijieHQoSPortQCS7QShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 10, 2, 1, 43),
    _RuijieHQoSPortQCS7QShaping_Type()
)
ruijieHQoSPortQCS7QShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieHQoSPortQCS7QShaping.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSPortQCS7QShaping.setUnits("kilobits per second")
_RuijieHQoSIfAppObjects_ObjectIdentity = ObjectIdentity
ruijieHQoSIfAppObjects = _RuijieHQoSIfAppObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 11)
)
_RuijieHQoSIfAppTable_Object = MibTable
ruijieHQoSIfAppTable = _RuijieHQoSIfAppTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 11, 1)
)
if mibBuilder.loadTexts:
    ruijieHQoSIfAppTable.setStatus("current")
_RuijieHQoSIfAppEntry_Object = MibTableRow
ruijieHQoSIfAppEntry = _RuijieHQoSIfAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 11, 1, 1)
)
ruijieHQoSIfAppEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-QOS-MIB", "ruijieHQoSIfAppIndex"),
)
if mibBuilder.loadTexts:
    ruijieHQoSIfAppEntry.setStatus("current")
_RuijieHQoSIfAppIndex_Type = InterfaceIndex
_RuijieHQoSIfAppIndex_Object = MibTableColumn
ruijieHQoSIfAppIndex = _RuijieHQoSIfAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 11, 1, 1, 1),
    _RuijieHQoSIfAppIndex_Type()
)
ruijieHQoSIfAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieHQoSIfAppIndex.setStatus("current")


class _RuijieHQoSIfAppInPolicyName_Type(OctetString):
    """Custom type ruijieHQoSIfAppInPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSIfAppInPolicyName_Type.__name__ = "OctetString"
_RuijieHQoSIfAppInPolicyName_Object = MibTableColumn
ruijieHQoSIfAppInPolicyName = _RuijieHQoSIfAppInPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 11, 1, 1, 2),
    _RuijieHQoSIfAppInPolicyName_Type()
)
ruijieHQoSIfAppInPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieHQoSIfAppInPolicyName.setStatus("current")
_RuijieHQoSIfAppInPolicyIndex_Type = Unsigned32
_RuijieHQoSIfAppInPolicyIndex_Object = MibTableColumn
ruijieHQoSIfAppInPolicyIndex = _RuijieHQoSIfAppInPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 11, 1, 1, 3),
    _RuijieHQoSIfAppInPolicyIndex_Type()
)
ruijieHQoSIfAppInPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHQoSIfAppInPolicyIndex.setStatus("current")


class _RuijieHQoSIfAppInPolicyLayer_Type(RuijieLayerType):
    """Custom type ruijieHQoSIfAppInPolicyLayer based on RuijieLayerType"""
    defaultValue = 0


_RuijieHQoSIfAppInPolicyLayer_Type.__name__ = "RuijieLayerType"
_RuijieHQoSIfAppInPolicyLayer_Object = MibTableColumn
ruijieHQoSIfAppInPolicyLayer = _RuijieHQoSIfAppInPolicyLayer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 11, 1, 1, 4),
    _RuijieHQoSIfAppInPolicyLayer_Type()
)
ruijieHQoSIfAppInPolicyLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieHQoSIfAppInPolicyLayer.setStatus("current")


class _RuijieHQoSIfAppOutPolicyName_Type(OctetString):
    """Custom type ruijieHQoSIfAppOutPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSIfAppOutPolicyName_Type.__name__ = "OctetString"
_RuijieHQoSIfAppOutPolicyName_Object = MibTableColumn
ruijieHQoSIfAppOutPolicyName = _RuijieHQoSIfAppOutPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 11, 1, 1, 5),
    _RuijieHQoSIfAppOutPolicyName_Type()
)
ruijieHQoSIfAppOutPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieHQoSIfAppOutPolicyName.setStatus("current")
_RuijieHQoSIfAppOutPolicyIndex_Type = Unsigned32
_RuijieHQoSIfAppOutPolicyIndex_Object = MibTableColumn
ruijieHQoSIfAppOutPolicyIndex = _RuijieHQoSIfAppOutPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 11, 1, 1, 6),
    _RuijieHQoSIfAppOutPolicyIndex_Type()
)
ruijieHQoSIfAppOutPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHQoSIfAppOutPolicyIndex.setStatus("current")


class _RuijieHQoSIfAppOutPolicyLayer_Type(RuijieLayerType):
    """Custom type ruijieHQoSIfAppOutPolicyLayer based on RuijieLayerType"""
    defaultValue = 0


_RuijieHQoSIfAppOutPolicyLayer_Type.__name__ = "RuijieLayerType"
_RuijieHQoSIfAppOutPolicyLayer_Object = MibTableColumn
ruijieHQoSIfAppOutPolicyLayer = _RuijieHQoSIfAppOutPolicyLayer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 11, 1, 1, 7),
    _RuijieHQoSIfAppOutPolicyLayer_Type()
)
ruijieHQoSIfAppOutPolicyLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieHQoSIfAppOutPolicyLayer.setStatus("current")


class _RuijieHQoSIfAppPortQueueName_Type(OctetString):
    """Custom type ruijieHQoSIfAppPortQueueName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHQoSIfAppPortQueueName_Type.__name__ = "OctetString"
_RuijieHQoSIfAppPortQueueName_Object = MibTableColumn
ruijieHQoSIfAppPortQueueName = _RuijieHQoSIfAppPortQueueName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 11, 1, 1, 8),
    _RuijieHQoSIfAppPortQueueName_Type()
)
ruijieHQoSIfAppPortQueueName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieHQoSIfAppPortQueueName.setStatus("current")
_RuijieHQoSIfAppPortQueueIndex_Type = Unsigned32
_RuijieHQoSIfAppPortQueueIndex_Object = MibTableColumn
ruijieHQoSIfAppPortQueueIndex = _RuijieHQoSIfAppPortQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 11, 1, 1, 9),
    _RuijieHQoSIfAppPortQueueIndex_Type()
)
ruijieHQoSIfAppPortQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHQoSIfAppPortQueueIndex.setStatus("current")


class _RuijieHQoSIfAppPortQueueShaping_Type(Integer32):
    """Custom type ruijieHQoSIfAppPortQueueShaping based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RuijieHQoSIfAppPortQueueShaping_Type.__name__ = "Integer32"
_RuijieHQoSIfAppPortQueueShaping_Object = MibTableColumn
ruijieHQoSIfAppPortQueueShaping = _RuijieHQoSIfAppPortQueueShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 3, 11, 1, 1, 10),
    _RuijieHQoSIfAppPortQueueShaping_Type()
)
ruijieHQoSIfAppPortQueueShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieHQoSIfAppPortQueueShaping.setStatus("current")
if mibBuilder.loadTexts:
    ruijieHQoSIfAppPortQueueShaping.setUnits("kilobits per second")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-ROUTER-QOS-MIB",
    **{"RuijieCosType": RuijieCosType,
       "RuijieQType": RuijieQType,
       "RuijieQDirectionType": RuijieQDirectionType,
       "RuijieLayerType": RuijieLayerType,
       "ruijieRouterQoSMIB": ruijieRouterQoSMIB,
       "ruijieCBQoSMIBObjects": ruijieCBQoSMIBObjects,
       "ruijieCBQoSIfStaticsObjects": ruijieCBQoSIfStaticsObjects,
       "ruijieCBQoSIfCbwfqRunInfoTable": ruijieCBQoSIfCbwfqRunInfoTable,
       "ruijieCBQoSIfCbwfqRunInfoEntry": ruijieCBQoSIfCbwfqRunInfoEntry,
       "ruijieCBQoSIfCbwfqPolicyIfIndex": ruijieCBQoSIfCbwfqPolicyIfIndex,
       "ruijieCBQoSIfCbwfqQueueSize": ruijieCBQoSIfCbwfqQueueSize,
       "ruijieCBQoSIfCbwfqDiscard": ruijieCBQoSIfCbwfqDiscard,
       "ruijieCBQoSIfCbwfqEfQueueSize": ruijieCBQoSIfCbwfqEfQueueSize,
       "ruijieCBQoSIfCbwfqAfQueueSize": ruijieCBQoSIfCbwfqAfQueueSize,
       "ruijieCBQoSIfCbwfqBeQueueSize": ruijieCBQoSIfCbwfqBeQueueSize,
       "ruijieCBQoSIfCbwfqBeActiveQueueNum": ruijieCBQoSIfCbwfqBeActiveQueueNum,
       "ruijieCBQoSIfCbwfqBeMaxActiveQueueNum": ruijieCBQoSIfCbwfqBeMaxActiveQueueNum,
       "ruijieCBQoSIfCbwfqBeTotalQueueNum": ruijieCBQoSIfCbwfqBeTotalQueueNum,
       "ruijieCBQoSIfCbwfqAfAllocatedQueueNum": ruijieCBQoSIfCbwfqAfAllocatedQueueNum,
       "ruijieCBQoSIfCbwfqPass": ruijieCBQoSIfCbwfqPass,
       "ruijieCBQoSIfCbwfqDroppedRateIn5Min": ruijieCBQoSIfCbwfqDroppedRateIn5Min,
       "ruijieCBQoSIfCbwfqPassBytes": ruijieCBQoSIfCbwfqPassBytes,
       "ruijieCBQoSIfCbwfqDiscardBytes": ruijieCBQoSIfCbwfqDiscardBytes,
       "ruijieCBQoSIfClassMatchRunInfoTable": ruijieCBQoSIfClassMatchRunInfoTable,
       "ruijieCBQoSIfClassMatchRunInfoEntry": ruijieCBQoSIfClassMatchRunInfoEntry,
       "ruijieCBQoSIfClassMatchIfIndex": ruijieCBQoSIfClassMatchIfIndex,
       "ruijieCBQoSIfClassMatchPolicyDirection": ruijieCBQoSIfClassMatchPolicyDirection,
       "ruijieCBQoSIfClassMatchClassIndex": ruijieCBQoSIfClassMatchClassIndex,
       "ruijieCBQoSIfClassMatchedPackets": ruijieCBQoSIfClassMatchedPackets,
       "ruijieCBQoSIfClassMatchedBytes": ruijieCBQoSIfClassMatchedBytes,
       "ruijieCBQosIfClassPassedPackets": ruijieCBQosIfClassPassedPackets,
       "ruijieCBQosIfClassDroppedPackets": ruijieCBQosIfClassDroppedPackets,
       "ruijieCBQoSIfPolicyName": ruijieCBQoSIfPolicyName,
       "ruijieCBQoSIfClassName": ruijieCBQoSIfClassName,
       "ruijieCBQoSIfClassPassBytes": ruijieCBQoSIfClassPassBytes,
       "ruijieCBQoSIfClassDiscardBytes": ruijieCBQoSIfClassDiscardBytes,
       "ruijieCBQoSIfCarRunInfoTable": ruijieCBQoSIfCarRunInfoTable,
       "ruijieCBQoSIfCarRunInfoEntry": ruijieCBQoSIfCarRunInfoEntry,
       "ruijieCBQoSIfCarIfIndex": ruijieCBQoSIfCarIfIndex,
       "ruijieCBQoSIfCarPolicyDirection": ruijieCBQoSIfCarPolicyDirection,
       "ruijieCBQoSIfCarClassIndex": ruijieCBQoSIfCarClassIndex,
       "ruijieCBQoSIfCarConformedPackets": ruijieCBQoSIfCarConformedPackets,
       "ruijieCBQoSIfCarConformedBytes": ruijieCBQoSIfCarConformedBytes,
       "ruijieCBQoSIfCarExceededPackets": ruijieCBQoSIfCarExceededPackets,
       "ruijieCBQoSIfCarExceededBytes": ruijieCBQoSIfCarExceededBytes,
       "ruijieCBQoSIfCarViolatedPackets": ruijieCBQoSIfCarViolatedPackets,
       "ruijieCBQoSIfCarViolatedBytes": ruijieCBQoSIfCarViolatedBytes,
       "ruijieCBQoSIfRemarkRunInfoTable": ruijieCBQoSIfRemarkRunInfoTable,
       "ruijieCBQoSIfRemarkRunInfoEntry": ruijieCBQoSIfRemarkRunInfoEntry,
       "ruijieCBQoSIfRemarkIfIndex": ruijieCBQoSIfRemarkIfIndex,
       "ruijieCBQoSIfRemarkPolicyDirection": ruijieCBQoSIfRemarkPolicyDirection,
       "ruijieCBQoSIfRemarkClassIndex": ruijieCBQoSIfRemarkClassIndex,
       "ruijieCBQoSIfRemarkedPackets": ruijieCBQoSIfRemarkedPackets,
       "ruijieCBQoSIfRemarkedBytes": ruijieCBQoSIfRemarkedBytes,
       "ruijieCBQoSIfQueueRunInfoTable": ruijieCBQoSIfQueueRunInfoTable,
       "ruijieCBQoSIfQueueRunInfoEntry": ruijieCBQoSIfQueueRunInfoEntry,
       "ruijieCBQoSIfQueueIfIndex": ruijieCBQoSIfQueueIfIndex,
       "ruijieCBQoSIfQueuePolicyDirection": ruijieCBQoSIfQueuePolicyDirection,
       "ruijieCBQoSIfQueueClassIndex": ruijieCBQoSIfQueueClassIndex,
       "ruijieCBQoSIfQueueMatchedPackets": ruijieCBQoSIfQueueMatchedPackets,
       "ruijieCBQoSIfQueueMatchedBytes": ruijieCBQoSIfQueueMatchedBytes,
       "ruijieCBQoSIfQueueEnqueuedPackets": ruijieCBQoSIfQueueEnqueuedPackets,
       "ruijieCBQoSIfQueueEnqueuedBytes": ruijieCBQoSIfQueueEnqueuedBytes,
       "ruijieCBQoSIfQueueDiscardedPackets": ruijieCBQoSIfQueueDiscardedPackets,
       "ruijieCBQoSIfQueueDiscardedBytes": ruijieCBQoSIfQueueDiscardedBytes,
       "ruijieCBQoSIfWredRunInfoTable": ruijieCBQoSIfWredRunInfoTable,
       "ruijieCBQoSIfWredRunInfoEntry": ruijieCBQoSIfWredRunInfoEntry,
       "ruijieCBQoSIfWredIfIndex": ruijieCBQoSIfWredIfIndex,
       "ruijieCBQoSIfWredClassIndex": ruijieCBQoSIfWredClassIndex,
       "ruijieCBQoSIfWredClassValue": ruijieCBQoSIfWredClassValue,
       "ruijieCBQoSIfWredRandomDiscardedPackets": ruijieCBQoSIfWredRandomDiscardedPackets,
       "ruijieCBQoSIfWredTailDiscardedPackets": ruijieCBQoSIfWredTailDiscardedPackets,
       "ruijieIfQoSMIBObjects": ruijieIfQoSMIBObjects,
       "ruijieIfQosPQRunInfoTable": ruijieIfQosPQRunInfoTable,
       "ruijieIfQosPQRunInfoEntry": ruijieIfQosPQRunInfoEntry,
       "ruijieIfQosPQIfIndex": ruijieIfQosPQIfIndex,
       "ruijieIfQosPQListNum": ruijieIfQosPQListNum,
       "ruijieIfQosPQIfName": ruijieIfQosPQIfName,
       "ruijieIfQosPQHighPkt": ruijieIfQosPQHighPkt,
       "ruijieIfQosPQHighDiscard": ruijieIfQosPQHighDiscard,
       "ruijieIfQosPQHighMaxQueLen": ruijieIfQosPQHighMaxQueLen,
       "ruijieIfQosPQMiddlePkt": ruijieIfQosPQMiddlePkt,
       "ruijieIfQosPQMiddleDiscard": ruijieIfQosPQMiddleDiscard,
       "ruijieIfQosPQMiddleMaxQueLen": ruijieIfQosPQMiddleMaxQueLen,
       "ruijieIfQosPQNormalPkt": ruijieIfQosPQNormalPkt,
       "ruijieIfQosPQNormalDiscard": ruijieIfQosPQNormalDiscard,
       "ruijieIfQosPQNormalMaxQueLen": ruijieIfQosPQNormalMaxQueLen,
       "ruijieIfQosPQLowPkt": ruijieIfQosPQLowPkt,
       "ruijieIfQosPQLowDiscard": ruijieIfQosPQLowDiscard,
       "ruijieIfQosPQLowMaxQueLen": ruijieIfQosPQLowMaxQueLen,
       "ruijieIfQosCQRunInfoTable": ruijieIfQosCQRunInfoTable,
       "ruijieIfQosCQRunInfoEntry": ruijieIfQosCQRunInfoEntry,
       "ruijieIfQosCQRunInfoIfIndex": ruijieIfQosCQRunInfoIfIndex,
       "ruijieIfQosCQRunInfoQueNum": ruijieIfQosCQRunInfoQueNum,
       "ruijieIfQosCQRunInfoIfName": ruijieIfQosCQRunInfoIfName,
       "ruijieIfQosCQRunInfoQuePkt": ruijieIfQosCQRunInfoQuePkt,
       "ruijieIfQosCQRunInfoQueDiscard": ruijieIfQosCQRunInfoQueDiscard,
       "ruijieIfQosCQRunInfoMaxQueLen": ruijieIfQosCQRunInfoMaxQueLen,
       "ruijieIfQosWFQRunInfoTable": ruijieIfQosWFQRunInfoTable,
       "ruijieIfQosWFQRunInfoEntry": ruijieIfQosWFQRunInfoEntry,
       "ruijieIfQosWFQIfIndex": ruijieIfQosWFQIfIndex,
       "ruijieIfQosWFQIfName": ruijieIfQosWFQIfName,
       "ruijieIfQosWFQMaxQueLen": ruijieIfQosWFQMaxQueLen,
       "ruijieIfQosWFQTotalQueNum": ruijieIfQosWFQTotalQueNum,
       "ruijieIfQosWFQCurQueLen": ruijieIfQosWFQCurQueLen,
       "ruijieIfQosWFQTotalDiscard": ruijieIfQosWFQTotalDiscard,
       "ruijieIfQosWFQActiveQueNum": ruijieIfQosWFQActiveQueNum,
       "ruijieIfQosWFQMaxActiveQueNum": ruijieIfQosWFQMaxActiveQueNum,
       "ruijieIfQosWredRunInfoTable": ruijieIfQosWredRunInfoTable,
       "ruijieIfQosWredRunInfoEntry": ruijieIfQosWredRunInfoEntry,
       "ruijieIfQosWredIfIndex": ruijieIfQosWredIfIndex,
       "ruijieIfQosWredValue": ruijieIfQosWredValue,
       "ruijieIfQosWredRandomDiscardedPackets": ruijieIfQosWredRandomDiscardedPackets,
       "ruijieIfQosWredTailDiscardedPackets": ruijieIfQosWredTailDiscardedPackets,
       "ruijieIfQosCARTable": ruijieIfQosCARTable,
       "ruijieIfQosCAREntry": ruijieIfQosCAREntry,
       "ruijieIfQosCARIfIndex": ruijieIfQosCARIfIndex,
       "ruijieIfQosCARIfName": ruijieIfQosCARIfName,
       "ruijieIfQosCARPktDirection": ruijieIfQosCARPktDirection,
       "ruijieIfQosCARType": ruijieIfQosCARType,
       "ruijieIfQosCARListNum": ruijieIfQosCARListNum,
       "ruijieIfQosCARindex": ruijieIfQosCARindex,
       "ruijieIfQosCARCIR": ruijieIfQosCARCIR,
       "ruijieIfQosCARBurstSize": ruijieIfQosCARBurstSize,
       "ruijieIfQosCARExcessBurstSize": ruijieIfQosCARExcessBurstSize,
       "ruijieIfQosCARConformAction": ruijieIfQosCARConformAction,
       "ruijieIfQosCARExceedAction": ruijieIfQosCARExceedAction,
       "ruijieIfQosCARConformNewPrec": ruijieIfQosCARConformNewPrec,
       "ruijieIfQosCARExceedNewPrec": ruijieIfQosCARExceedNewPrec,
       "ruijieIfQosCARConformPkt": ruijieIfQosCARConformPkt,
       "ruijieIfQosCARConformByte": ruijieIfQosCARConformByte,
       "ruijieIfQosCARExceedPkt": ruijieIfQosCARExceedPkt,
       "ruijieIfQosCARExceedByte": ruijieIfQosCARExceedByte,
       "ruijieIfQosGTSTable": ruijieIfQosGTSTable,
       "ruijieIfQosGTSEntry": ruijieIfQosGTSEntry,
       "ruijieIfQosGTSIfIndex": ruijieIfQosGTSIfIndex,
       "ruijieIfQosGTSIfName": ruijieIfQosGTSIfName,
       "ruijieIfQosGTSType": ruijieIfQosGTSType,
       "ruijieIfQosGTSACLNum": ruijieIfQosGTSACLNum,
       "ruijieIfQosGTSCIR": ruijieIfQosGTSCIR,
       "ruijieIfQosGTSBurstSize": ruijieIfQosGTSBurstSize,
       "ruijieIfQosGTSExcessBurstSize": ruijieIfQosGTSExcessBurstSize,
       "ruijieIfQosGTSMaxQueLen": ruijieIfQosGTSMaxQueLen,
       "ruijieIfQosGTSCurQueLen": ruijieIfQosGTSCurQueLen,
       "ruijieIfQosGTSPassPkt": ruijieIfQosGTSPassPkt,
       "ruijieIfQosGTSPassByte": ruijieIfQosGTSPassByte,
       "ruijieIfQosGTSDiscardPkt": ruijieIfQosGTSDiscardPkt,
       "ruijieIfQosGTSDiscardByte": ruijieIfQosGTSDiscardByte,
       "ruijieIfQosRTPIfQueueRunInfoTable": ruijieIfQosRTPIfQueueRunInfoTable,
       "ruijieIfQosRTPIfQueueRunInfoEntry": ruijieIfQosRTPIfQueueRunInfoEntry,
       "ruijieIfQosRTPIfApplyIfIndex": ruijieIfQosRTPIfApplyIfIndex,
       "ruijieIfQosRTPIfQueueSize": ruijieIfQosRTPIfQueueSize,
       "ruijieIfQosRTPIfQueueMaxSize": ruijieIfQosRTPIfQueueMaxSize,
       "ruijieIfQosRTPIfQueueOutputs": ruijieIfQosRTPIfQueueOutputs,
       "ruijieIfQosRTPIfQueueDiscards": ruijieIfQosRTPIfQueueDiscards,
       "ruijieIfQosFlowLimitRunInfoTable": ruijieIfQosFlowLimitRunInfoTable,
       "ruijieIfQosFlowLimitRunInfoEntry": ruijieIfQosFlowLimitRunInfoEntry,
       "ruijieIfQosFlowLimitLabelNum": ruijieIfQosFlowLimitLabelNum,
       "ruijieIfQosFlowLimitPktDirection": ruijieIfQosFlowLimitPktDirection,
       "ruijieIfQosFlowLimitCIR": ruijieIfQosFlowLimitCIR,
       "ruijieIfQosFlowLimitBurstSize": ruijieIfQosFlowLimitBurstSize,
       "ruijieIfQosFlowLimitExcessBurstSize": ruijieIfQosFlowLimitExcessBurstSize,
       "ruijieIfQosFlowLimitConformAction": ruijieIfQosFlowLimitConformAction,
       "ruijieIfQosFlowLimitExceedAction": ruijieIfQosFlowLimitExceedAction,
       "ruijieIfQosFlowLimitConformNewPrec": ruijieIfQosFlowLimitConformNewPrec,
       "ruijieIfQosFlowLimitExceedNewPrec": ruijieIfQosFlowLimitExceedNewPrec,
       "ruijieIfQosFlowLimitConformPkt": ruijieIfQosFlowLimitConformPkt,
       "ruijieIfQosFlowLimitConformByte": ruijieIfQosFlowLimitConformByte,
       "ruijieIfQosFlowLimitExceedPkt": ruijieIfQosFlowLimitExceedPkt,
       "ruijieIfQosFlowLimitExceedByte": ruijieIfQosFlowLimitExceedByte,
       "ruijieHQoSMIBObjects": ruijieHQoSMIBObjects,
       "ruijieHQoSScalarObjects": ruijieHQoSScalarObjects,
       "ruijieHQoSNameType": ruijieHQoSNameType,
       "ruijieHQoSNameFind": ruijieHQoSNameFind,
       "ruijieHQoSNameIndex": ruijieHQoSNameIndex,
       "ruijieHQoSUserQObjects": ruijieHQoSUserQObjects,
       "ruijieHQoSUserQInIndexNext": ruijieHQoSUserQInIndexNext,
       "ruijieHQoSUserQOutIndexNext": ruijieHQoSUserQOutIndexNext,
       "ruijieHQoSUserQTable": ruijieHQoSUserQTable,
       "ruijieHQoSUserQEntry": ruijieHQoSUserQEntry,
       "ruijieHQoSUserQIndex": ruijieHQoSUserQIndex,
       "ruijieHQoSUserQName": ruijieHQoSUserQName,
       "ruijieHQoSUserQDirection": ruijieHQoSUserQDirection,
       "ruijieHQoSUserQRowStatus": ruijieHQoSUserQRowStatus,
       "ruijieHQoSUserQFlowQName": ruijieHQoSUserQFlowQName,
       "ruijieHQoSUserQFlowQIndex": ruijieHQoSUserQFlowQIndex,
       "ruijieHQoSUserQGroupName": ruijieHQoSUserQGroupName,
       "ruijieHQoSUserQGroupIndex": ruijieHQoSUserQGroupIndex,
       "ruijieHQoSUserQFlowMapName": ruijieHQoSUserQFlowMapName,
       "ruijieHQoSUserQFlowMapIndex": ruijieHQoSUserQFlowMapIndex,
       "ruijieHQoSUserQCIR": ruijieHQoSUserQCIR,
       "ruijieHQoSUserQPIR": ruijieHQoSUserQPIR,
       "ruijieHQoSUserGroupQObjects": ruijieHQoSUserGroupQObjects,
       "ruijieHQoSUserGroupQInIndexNext": ruijieHQoSUserGroupQInIndexNext,
       "ruijieHQoSUserGroupQOutIndexNext": ruijieHQoSUserGroupQOutIndexNext,
       "ruijieHQoSUserGroupQTable": ruijieHQoSUserGroupQTable,
       "ruijieHQoSUserGroupQEntry": ruijieHQoSUserGroupQEntry,
       "ruijieHQoSUserGroupQIndex": ruijieHQoSUserGroupQIndex,
       "ruijieHQoSUserGroupQName": ruijieHQoSUserGroupQName,
       "ruijieHQoSUserGroupQDirection": ruijieHQoSUserGroupQDirection,
       "ruijieHQoSUserGroupQRowStatus": ruijieHQoSUserGroupQRowStatus,
       "ruijieHQoSUserGroupQShaping": ruijieHQoSUserGroupQShaping,
       "ruijieHQoSFlowQObjects": ruijieHQoSFlowQObjects,
       "ruijieHQoSFlowQIndexNext": ruijieHQoSFlowQIndexNext,
       "ruijieHQoSFlowQTable": ruijieHQoSFlowQTable,
       "ruijieHQoSFlowQEntry": ruijieHQoSFlowQEntry,
       "ruijieHQoSFlowQIndex": ruijieHQoSFlowQIndex,
       "ruijieHQoSFlowQName": ruijieHQoSFlowQName,
       "ruijieHQoSFlowQRowStatus": ruijieHQoSFlowQRowStatus,
       "ruijieHQoSFlowQBEQType": ruijieHQoSFlowQBEQType,
       "ruijieHQoSFlowQBEQWredWeight": ruijieHQoSFlowQBEQWredWeight,
       "ruijieHQoSFlowQBEQWredName": ruijieHQoSFlowQBEQWredName,
       "ruijieHQoSFlowQBEQDepth": ruijieHQoSFlowQBEQDepth,
       "ruijieHQoSFlowQBEQShaping": ruijieHQoSFlowQBEQShaping,
       "ruijieHQoSFlowQAF1QType": ruijieHQoSFlowQAF1QType,
       "ruijieHQoSFlowQAF1QWredWeight": ruijieHQoSFlowQAF1QWredWeight,
       "ruijieHQoSFlowQAF1QWredName": ruijieHQoSFlowQAF1QWredName,
       "ruijieHQoSFlowQAF1QDepth": ruijieHQoSFlowQAF1QDepth,
       "ruijieHQoSFlowQAF1QShaping": ruijieHQoSFlowQAF1QShaping,
       "ruijieHQoSFlowQAF2QType": ruijieHQoSFlowQAF2QType,
       "ruijieHQoSFlowQAF2QWredWeight": ruijieHQoSFlowQAF2QWredWeight,
       "ruijieHQoSFlowQAF2QWredName": ruijieHQoSFlowQAF2QWredName,
       "ruijieHQoSFlowQAF2QDepth": ruijieHQoSFlowQAF2QDepth,
       "ruijieHQoSFlowQAF2QShaping": ruijieHQoSFlowQAF2QShaping,
       "ruijieHQoSFlowQAF3QType": ruijieHQoSFlowQAF3QType,
       "ruijieHQoSFlowQAF3QWredWeight": ruijieHQoSFlowQAF3QWredWeight,
       "ruijieHQoSFlowQAF3QWredName": ruijieHQoSFlowQAF3QWredName,
       "ruijieHQoSFlowQAF3QDepth": ruijieHQoSFlowQAF3QDepth,
       "ruijieHQoSFlowQAF3QShaping": ruijieHQoSFlowQAF3QShaping,
       "ruijieHQoSFlowQAF4QType": ruijieHQoSFlowQAF4QType,
       "ruijieHQoSFlowQAF4QWredWeight": ruijieHQoSFlowQAF4QWredWeight,
       "ruijieHQoSFlowQAF4QWredName": ruijieHQoSFlowQAF4QWredName,
       "ruijieHQoSFlowQAF4QDepth": ruijieHQoSFlowQAF4QDepth,
       "ruijieHQoSFlowQAF4QShaping": ruijieHQoSFlowQAF4QShaping,
       "ruijieHQoSFlowQEFQType": ruijieHQoSFlowQEFQType,
       "ruijieHQoSFlowQEFQWredWeight": ruijieHQoSFlowQEFQWredWeight,
       "ruijieHQoSFlowQEFQWredName": ruijieHQoSFlowQEFQWredName,
       "ruijieHQoSFlowQEFQDepth": ruijieHQoSFlowQEFQDepth,
       "ruijieHQoSFlowQEFQShaping": ruijieHQoSFlowQEFQShaping,
       "ruijieHQoSFlowQCS6QType": ruijieHQoSFlowQCS6QType,
       "ruijieHQoSFlowQCS6QWredWeight": ruijieHQoSFlowQCS6QWredWeight,
       "ruijieHQoSFlowQCS6QWredName": ruijieHQoSFlowQCS6QWredName,
       "ruijieHQoSFlowQCS6QDepth": ruijieHQoSFlowQCS6QDepth,
       "ruijieHQoSFlowQCS6QShaping": ruijieHQoSFlowQCS6QShaping,
       "ruijieHQoSFlowQCS7QType": ruijieHQoSFlowQCS7QType,
       "ruijieHQoSFlowQCS7QWredWeight": ruijieHQoSFlowQCS7QWredWeight,
       "ruijieHQoSFlowQCS7QWredName": ruijieHQoSFlowQCS7QWredName,
       "ruijieHQoSFlowQCS7QDepth": ruijieHQoSFlowQCS7QDepth,
       "ruijieHQoSFlowQCS7QShaping": ruijieHQoSFlowQCS7QShaping,
       "ruijieHQoSFlowMapObjects": ruijieHQoSFlowMapObjects,
       "ruijieHQoSFlowMapIndexNext": ruijieHQoSFlowMapIndexNext,
       "ruijieHQoSFlowMapTable": ruijieHQoSFlowMapTable,
       "ruijieHQoSFlowMapEntry": ruijieHQoSFlowMapEntry,
       "ruijieHQoSFlowMapIndex": ruijieHQoSFlowMapIndex,
       "ruijieHQoSFlowMapName": ruijieHQoSFlowMapName,
       "ruijieHQoSFlowMapRowStatus": ruijieHQoSFlowMapRowStatus,
       "ruijieHQoSFlowMapBEQ2PortQ": ruijieHQoSFlowMapBEQ2PortQ,
       "ruijieHQoSFlowMapAF1Q2PortQ": ruijieHQoSFlowMapAF1Q2PortQ,
       "ruijieHQoSFlowMapAF2Q2PortQ": ruijieHQoSFlowMapAF2Q2PortQ,
       "ruijieHQoSFlowMapAF3Q2PortQ": ruijieHQoSFlowMapAF3Q2PortQ,
       "ruijieHQoSFlowMapAF4Q2PortQ": ruijieHQoSFlowMapAF4Q2PortQ,
       "ruijieHQoSFlowMapEFQ2PortQ": ruijieHQoSFlowMapEFQ2PortQ,
       "ruijieHQoSFlowMapCS6Q2PortQ": ruijieHQoSFlowMapCS6Q2PortQ,
       "ruijieHQoSFlowMapCS7Q2PortQ": ruijieHQoSFlowMapCS7Q2PortQ,
       "ruijieHQoSTClassifierObjects": ruijieHQoSTClassifierObjects,
       "ruijieHQoSTClassifierIndexNext": ruijieHQoSTClassifierIndexNext,
       "ruijieHQoSTClassifierTable": ruijieHQoSTClassifierTable,
       "ruijieHQoSTClassifierEntry": ruijieHQoSTClassifierEntry,
       "ruijieHQoSTClassifierIndex": ruijieHQoSTClassifierIndex,
       "ruijieHQoSTClassifierInstance": ruijieHQoSTClassifierInstance,
       "ruijieHQoSTClassifierName": ruijieHQoSTClassifierName,
       "ruijieHQoSTClassifierType": ruijieHQoSTClassifierType,
       "ruijieHQoSTClassifierRowStatus": ruijieHQoSTClassifierRowStatus,
       "ruijieHQoSTClassifierMatchMask": ruijieHQoSTClassifierMatchMask,
       "ruijieHQoSTClassifierMatchV4Any": ruijieHQoSTClassifierMatchV4Any,
       "ruijieHQoSTClassifierMatchV4AclID": ruijieHQoSTClassifierMatchV4AclID,
       "ruijieHQoSTClassifierV4AclName": ruijieHQoSTClassifierV4AclName,
       "ruijieHQoSTClassifierMatchV4Dscp": ruijieHQoSTClassifierMatchV4Dscp,
       "ruijieHQoSTClassifierMatchV4Tos": ruijieHQoSTClassifierMatchV4Tos,
       "ruijieHQoSTClassifierMatchV6Any": ruijieHQoSTClassifierMatchV6Any,
       "ruijieHQoSTClassifierMatchV6AclID": ruijieHQoSTClassifierMatchV6AclID,
       "ruijieHQoSTClassifierV6AclName": ruijieHQoSTClassifierV6AclName,
       "ruijieHQoSTClassifierMatchV6Dscp": ruijieHQoSTClassifierMatchV6Dscp,
       "ruijieHQoSTClassifierMatchCos": ruijieHQoSTClassifierMatchCos,
       "ruijieHQoSTClassifierMatchExp": ruijieHQoSTClassifierMatchExp,
       "ruijieHQoSTClassifierMatchSrcMac": ruijieHQoSTClassifierMatchSrcMac,
       "ruijieHQoSTClassifierMatchDstMac": ruijieHQoSTClassifierMatchDstMac,
       "ruijieHQoSTBehaviorObjects": ruijieHQoSTBehaviorObjects,
       "ruijieHQoSTBehaviorIndexNext": ruijieHQoSTBehaviorIndexNext,
       "ruijieHQoSTBehaviorTable": ruijieHQoSTBehaviorTable,
       "ruijieHQoSTBehaviorEntry": ruijieHQoSTBehaviorEntry,
       "ruijieHQoSTBehaviorIndex": ruijieHQoSTBehaviorIndex,
       "ruijieHQoSTBehaviorName": ruijieHQoSTBehaviorName,
       "ruijieHQoSTBehaviorRowStatus": ruijieHQoSTBehaviorRowStatus,
       "ruijieHQoSTBehaviorMask": ruijieHQoSTBehaviorMask,
       "ruijieHQoSTBehaviorUserQName": ruijieHQoSTBehaviorUserQName,
       "ruijieHQoSTBehaviorUserQDir": ruijieHQoSTBehaviorUserQDir,
       "ruijieHQoSTBehaviorTCos": ruijieHQoSTBehaviorTCos,
       "ruijieHQoSTBehaviorTColor": ruijieHQoSTBehaviorTColor,
       "ruijieHQoSTBehaviorRV4Dscp": ruijieHQoSTBehaviorRV4Dscp,
       "ruijieHQoSTBehaviorRV4Tos": ruijieHQoSTBehaviorRV4Tos,
       "ruijieHQoSTBehaviorRV6Dscp": ruijieHQoSTBehaviorRV6Dscp,
       "ruijieHQoSTBehaviorRVlanCos": ruijieHQoSTBehaviorRVlanCos,
       "ruijieHQoSTBehaviorRExp": ruijieHQoSTBehaviorRExp,
       "ruijieHQoSTBehaviorSubPolicyName": ruijieHQoSTBehaviorSubPolicyName,
       "ruijieHQoSTPolicyObjects": ruijieHQoSTPolicyObjects,
       "ruijieHQoSTPolicyIndexNext": ruijieHQoSTPolicyIndexNext,
       "ruijieHQoSTPolicyTable": ruijieHQoSTPolicyTable,
       "ruijieHQoSTPolicyEntry": ruijieHQoSTPolicyEntry,
       "ruijieHQoSTPolicyIndex": ruijieHQoSTPolicyIndex,
       "ruijieHQoSTPolicyName": ruijieHQoSTPolicyName,
       "ruijieHQoSTPolicyRowStatus": ruijieHQoSTPolicyRowStatus,
       "ruijieHQoSTPolicyMapIndexNext": ruijieHQoSTPolicyMapIndexNext,
       "ruijieHQoSTPolicyMapTable": ruijieHQoSTPolicyMapTable,
       "ruijieHQoSTPolicyMapEntry": ruijieHQoSTPolicyMapEntry,
       "ruijieHQoSTPolicyMapIndex": ruijieHQoSTPolicyMapIndex,
       "ruijieHQoSTPolicyMapPolicyName": ruijieHQoSTPolicyMapPolicyName,
       "ruijieHQoSTPolicyMapPolicyIndex": ruijieHQoSTPolicyMapPolicyIndex,
       "ruijieHQoSTPolicyMapTClassfierName": ruijieHQoSTPolicyMapTClassfierName,
       "ruijieHQoSTPolicyMapTClassfierIndex": ruijieHQoSTPolicyMapTClassfierIndex,
       "ruijieHQoSTPolicyMapTBehaviorName": ruijieHQoSTPolicyMapTBehaviorName,
       "ruijieHQoSTPolicyMapTBehaviorIndex": ruijieHQoSTPolicyMapTBehaviorIndex,
       "ruijieHQoSTPolicyMapPrecedence": ruijieHQoSTPolicyMapPrecedence,
       "ruijieHQoSTPolicyMapRowStatus": ruijieHQoSTPolicyMapRowStatus,
       "ruijieHQoSVoQObjects": ruijieHQoSVoQObjects,
       "ruijieHQoSVoQEnable": ruijieHQoSVoQEnable,
       "ruijieHQoSVoQDeviceTable": ruijieHQoSVoQDeviceTable,
       "ruijieHQoSVoQDeviceEntry": ruijieHQoSVoQDeviceEntry,
       "ruijieHQoSVoQDeviceId": ruijieHQoSVoQDeviceId,
       "ruijieHQoSVoQDeviceCredit": ruijieHQoSVoQDeviceCredit,
       "ruijieHQoSPortQObjects": ruijieHQoSPortQObjects,
       "ruijieHQoSPortQIndexNext": ruijieHQoSPortQIndexNext,
       "ruijieHQoSPortQTable": ruijieHQoSPortQTable,
       "ruijieHQoSPortQEntry": ruijieHQoSPortQEntry,
       "ruijieHQoSPortQIndex": ruijieHQoSPortQIndex,
       "ruijieHQoSPortQName": ruijieHQoSPortQName,
       "ruijieHQoSPortQRowStatus": ruijieHQoSPortQRowStatus,
       "ruijieHQoSPortQBEQType": ruijieHQoSPortQBEQType,
       "ruijieHQoSPortQBEQWredWeight": ruijieHQoSPortQBEQWredWeight,
       "ruijieHQoSPortQBEQWredName": ruijieHQoSPortQBEQWredName,
       "ruijieHQoSPortQBEQDepth": ruijieHQoSPortQBEQDepth,
       "ruijieHQoSPortQBEQShaping": ruijieHQoSPortQBEQShaping,
       "ruijieHQoSPortQAF1QType": ruijieHQoSPortQAF1QType,
       "ruijieHQoSPortQAF1QWredWeight": ruijieHQoSPortQAF1QWredWeight,
       "ruijieHQoSPortQAF1QWredName": ruijieHQoSPortQAF1QWredName,
       "ruijieHQoSPortQAF1QDepth": ruijieHQoSPortQAF1QDepth,
       "ruijieHQoSPortQAF1QShaping": ruijieHQoSPortQAF1QShaping,
       "ruijieHQoSPortQAF2QType": ruijieHQoSPortQAF2QType,
       "ruijieHQoSPortQAF2QWredWeight": ruijieHQoSPortQAF2QWredWeight,
       "ruijieHQoSPortQAF2QWredName": ruijieHQoSPortQAF2QWredName,
       "ruijieHQoSPortQAF2QDepth": ruijieHQoSPortQAF2QDepth,
       "ruijieHQoSPortQAF2QShaping": ruijieHQoSPortQAF2QShaping,
       "ruijieHQoSPortQAF3QType": ruijieHQoSPortQAF3QType,
       "ruijieHQoSPortQAF3QWredWeight": ruijieHQoSPortQAF3QWredWeight,
       "ruijieHQoSPortQAF3QWredName": ruijieHQoSPortQAF3QWredName,
       "ruijieHQoSPortQAF3QDepth": ruijieHQoSPortQAF3QDepth,
       "ruijieHQoSPortQAF3QShaping": ruijieHQoSPortQAF3QShaping,
       "ruijieHQoSPortQAF4QType": ruijieHQoSPortQAF4QType,
       "ruijieHQoSPortQAF4QWredWeight": ruijieHQoSPortQAF4QWredWeight,
       "ruijieHQoSPortQAF4QWredName": ruijieHQoSPortQAF4QWredName,
       "ruijieHQoSPortQAF4QDepth": ruijieHQoSPortQAF4QDepth,
       "ruijieHQoSPortQAF4QShaping": ruijieHQoSPortQAF4QShaping,
       "ruijieHQoSPortQEFQType": ruijieHQoSPortQEFQType,
       "ruijieHQoSPortQEFQWredWeight": ruijieHQoSPortQEFQWredWeight,
       "ruijieHQoSPortQEFQWredName": ruijieHQoSPortQEFQWredName,
       "ruijieHQoSPortQEFQDepth": ruijieHQoSPortQEFQDepth,
       "ruijieHQoSPortQEFQShaping": ruijieHQoSPortQEFQShaping,
       "ruijieHQoSPortQCS6QType": ruijieHQoSPortQCS6QType,
       "ruijieHQoSPortQCS6QWredWeight": ruijieHQoSPortQCS6QWredWeight,
       "ruijieHQoSPortQCS6QWredName": ruijieHQoSPortQCS6QWredName,
       "ruijieHQoSPortQCS6QDepth": ruijieHQoSPortQCS6QDepth,
       "ruijieHQoSPortQCS6QShaping": ruijieHQoSPortQCS6QShaping,
       "ruijieHQoSPortQCS7QType": ruijieHQoSPortQCS7QType,
       "ruijieHQoSPortQCS7QWredWeight": ruijieHQoSPortQCS7QWredWeight,
       "ruijieHQoSPortQCS7QWredName": ruijieHQoSPortQCS7QWredName,
       "ruijieHQoSPortQCS7QDepth": ruijieHQoSPortQCS7QDepth,
       "ruijieHQoSPortQCS7QShaping": ruijieHQoSPortQCS7QShaping,
       "ruijieHQoSIfAppObjects": ruijieHQoSIfAppObjects,
       "ruijieHQoSIfAppTable": ruijieHQoSIfAppTable,
       "ruijieHQoSIfAppEntry": ruijieHQoSIfAppEntry,
       "ruijieHQoSIfAppIndex": ruijieHQoSIfAppIndex,
       "ruijieHQoSIfAppInPolicyName": ruijieHQoSIfAppInPolicyName,
       "ruijieHQoSIfAppInPolicyIndex": ruijieHQoSIfAppInPolicyIndex,
       "ruijieHQoSIfAppInPolicyLayer": ruijieHQoSIfAppInPolicyLayer,
       "ruijieHQoSIfAppOutPolicyName": ruijieHQoSIfAppOutPolicyName,
       "ruijieHQoSIfAppOutPolicyIndex": ruijieHQoSIfAppOutPolicyIndex,
       "ruijieHQoSIfAppOutPolicyLayer": ruijieHQoSIfAppOutPolicyLayer,
       "ruijieHQoSIfAppPortQueueName": ruijieHQoSIfAppPortQueueName,
       "ruijieHQoSIfAppPortQueueIndex": ruijieHQoSIfAppPortQueueIndex,
       "ruijieHQoSIfAppPortQueueShaping": ruijieHQoSIfAppPortQueueShaping}
)
