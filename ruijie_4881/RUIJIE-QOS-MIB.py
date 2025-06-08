# SNMP MIB module (RUIJIE-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-QOS-MIB.mib
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus",
    "IfIndex")

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

ruijieQoSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18)
)
if mibBuilder.loadTexts:
    ruijieQoSMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieQoSPriorityMIBObjects_ObjectIdentity = ObjectIdentity
ruijieQoSPriorityMIBObjects = _RuijieQoSPriorityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1)
)
_RuijieQoSGlobalStatus_Type = EnabledStatus
_RuijieQoSGlobalStatus_Object = MibScalar
ruijieQoSGlobalStatus = _RuijieQoSGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 1),
    _RuijieQoSGlobalStatus_Type()
)
ruijieQoSGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieQoSGlobalStatus.setStatus("current")
_RuijiePriorityTrafficClassNum_Type = Integer32
_RuijiePriorityTrafficClassNum_Object = MibScalar
ruijiePriorityTrafficClassNum = _RuijiePriorityTrafficClassNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 2),
    _RuijiePriorityTrafficClassNum_Type()
)
ruijiePriorityTrafficClassNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePriorityTrafficClassNum.setStatus("current")
_RuijiePriorityClassNum_Type = Integer32
_RuijiePriorityClassNum_Object = MibScalar
ruijiePriorityClassNum = _RuijiePriorityClassNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 3),
    _RuijiePriorityClassNum_Type()
)
ruijiePriorityClassNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePriorityClassNum.setStatus("current")
_RuijiePriorityDscpMaxValue_Type = Integer32
_RuijiePriorityDscpMaxValue_Object = MibScalar
ruijiePriorityDscpMaxValue = _RuijiePriorityDscpMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 4),
    _RuijiePriorityDscpMaxValue_Type()
)
ruijiePriorityDscpMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePriorityDscpMaxValue.setStatus("current")
_RuijieTrafficClassTable_Object = MibTable
ruijieTrafficClassTable = _RuijieTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 5)
)
if mibBuilder.loadTexts:
    ruijieTrafficClassTable.setStatus("current")
_RuijieTrafficClassEntry_Object = MibTableRow
ruijieTrafficClassEntry = _RuijieTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 5, 1)
)
ruijieTrafficClassEntry.setIndexNames(
    (0, "RUIJIE-QOS-MIB", "ruijieTrafficClassPriority"),
)
if mibBuilder.loadTexts:
    ruijieTrafficClassEntry.setStatus("current")
_RuijieTrafficClassPriority_Type = Integer32
_RuijieTrafficClassPriority_Object = MibTableColumn
ruijieTrafficClassPriority = _RuijieTrafficClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 5, 1, 1),
    _RuijieTrafficClassPriority_Type()
)
ruijieTrafficClassPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrafficClassPriority.setStatus("current")
_RuijieTrafficClass_Type = Integer32
_RuijieTrafficClass_Object = MibTableColumn
ruijieTrafficClass = _RuijieTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 5, 1, 2),
    _RuijieTrafficClass_Type()
)
ruijieTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieTrafficClass.setStatus("current")
_RuijiePriorityToDscp_Type = Integer32
_RuijiePriorityToDscp_Object = MibTableColumn
ruijiePriorityToDscp = _RuijiePriorityToDscp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 5, 1, 3),
    _RuijiePriorityToDscp_Type()
)
ruijiePriorityToDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePriorityToDscp.setStatus("current")
_RuijieDscpClassTable_Object = MibTable
ruijieDscpClassTable = _RuijieDscpClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieDscpClassTable.setStatus("current")
_RuijieDscpClassEntry_Object = MibTableRow
ruijieDscpClassEntry = _RuijieDscpClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 6, 1)
)
ruijieDscpClassEntry.setIndexNames(
    (0, "RUIJIE-QOS-MIB", "ruijieDscpClass"),
)
if mibBuilder.loadTexts:
    ruijieDscpClassEntry.setStatus("current")
_RuijieDscpClass_Type = Integer32
_RuijieDscpClass_Object = MibTableColumn
ruijieDscpClass = _RuijieDscpClass_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 6, 1, 1),
    _RuijieDscpClass_Type()
)
ruijieDscpClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDscpClass.setStatus("current")
_RuijieDscpTrafficClassPriority_Type = Integer32
_RuijieDscpTrafficClassPriority_Object = MibTableColumn
ruijieDscpTrafficClassPriority = _RuijieDscpTrafficClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 6, 1, 2),
    _RuijieDscpTrafficClassPriority_Type()
)
ruijieDscpTrafficClassPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDscpTrafficClassPriority.setStatus("current")


class _RuijiePriorityTrafficClassOperMode_Type(Integer32):
    """Custom type ruijiePriorityTrafficClassOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qos-sp", 1),
          ("qos-wrr", 2),
          ("qos-drr", 3))
    )


_RuijiePriorityTrafficClassOperMode_Type.__name__ = "Integer32"
_RuijiePriorityTrafficClassOperMode_Object = MibScalar
ruijiePriorityTrafficClassOperMode = _RuijiePriorityTrafficClassOperMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 7),
    _RuijiePriorityTrafficClassOperMode_Type()
)
ruijiePriorityTrafficClassOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePriorityTrafficClassOperMode.setStatus("current")
_RuijiePriorityBandWidth_Type = OctetString
_RuijiePriorityBandWidth_Object = MibScalar
ruijiePriorityBandWidth = _RuijiePriorityBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 8),
    _RuijiePriorityBandWidth_Type()
)
ruijiePriorityBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePriorityBandWidth.setStatus("current")
_RuijieIfPriorityTable_Object = MibTable
ruijieIfPriorityTable = _RuijieIfPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 9)
)
if mibBuilder.loadTexts:
    ruijieIfPriorityTable.setStatus("current")
_RuijieIfPriorityEntry_Object = MibTableRow
ruijieIfPriorityEntry = _RuijieIfPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 9, 1)
)
ruijieIfPriorityEntry.setIndexNames(
    (0, "RUIJIE-QOS-MIB", "ruijieIfPriorityIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfPriorityEntry.setStatus("current")
_RuijieIfPriorityIfIndex_Type = IfIndex
_RuijieIfPriorityIfIndex_Object = MibTableColumn
ruijieIfPriorityIfIndex = _RuijieIfPriorityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 9, 1, 1),
    _RuijieIfPriorityIfIndex_Type()
)
ruijieIfPriorityIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfPriorityIfIndex.setStatus("current")
_RuijieIfPriority_Type = Integer32
_RuijieIfPriority_Object = MibTableColumn
ruijieIfPriority = _RuijieIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 9, 1, 2),
    _RuijieIfPriority_Type()
)
ruijieIfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfPriority.setStatus("current")


class _RuijieIfPriTrafficClassOperMode_Type(Integer32):
    """Custom type ruijieIfPriTrafficClassOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qos-sp", 1),
          ("qos-wrr", 2),
          ("qos-drr", 3))
    )


_RuijieIfPriTrafficClassOperMode_Type.__name__ = "Integer32"
_RuijieIfPriTrafficClassOperMode_Object = MibTableColumn
ruijieIfPriTrafficClassOperMode = _RuijieIfPriTrafficClassOperMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 9, 1, 3),
    _RuijieIfPriTrafficClassOperMode_Type()
)
ruijieIfPriTrafficClassOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfPriTrafficClassOperMode.setStatus("current")
_RuijieIfPriorityBandwidth_Type = OctetString
_RuijieIfPriorityBandwidth_Object = MibTableColumn
ruijieIfPriorityBandwidth = _RuijieIfPriorityBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 9, 1, 4),
    _RuijieIfPriorityBandwidth_Type()
)
ruijieIfPriorityBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfPriorityBandwidth.setStatus("current")


class _RuijieIfPriorityQosTrustMode_Type(Integer32):
    """Custom type ruijieIfPriorityQosTrustMode based on Integer32"""
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
        *(("not-trust", 1),
          ("trust-cos", 2),
          ("trust-dscp", 3),
          ("trust-ip-precedence", 4))
    )


_RuijieIfPriorityQosTrustMode_Type.__name__ = "Integer32"
_RuijieIfPriorityQosTrustMode_Object = MibTableColumn
ruijieIfPriorityQosTrustMode = _RuijieIfPriorityQosTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 9, 1, 5),
    _RuijieIfPriorityQosTrustMode_Type()
)
ruijieIfPriorityQosTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfPriorityQosTrustMode.setStatus("current")
_RuijieIpPreClassTable_Object = MibTable
ruijieIpPreClassTable = _RuijieIpPreClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 10)
)
if mibBuilder.loadTexts:
    ruijieIpPreClassTable.setStatus("current")
_RuijieIpPreClassEntry_Object = MibTableRow
ruijieIpPreClassEntry = _RuijieIpPreClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 10, 1)
)
ruijieIpPreClassEntry.setIndexNames(
    (0, "RUIJIE-QOS-MIB", "ruijieIpPreClassPriority"),
)
if mibBuilder.loadTexts:
    ruijieIpPreClassEntry.setStatus("current")
_RuijieIpPreClassPriority_Type = Integer32
_RuijieIpPreClassPriority_Object = MibTableColumn
ruijieIpPreClassPriority = _RuijieIpPreClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 10, 1, 1),
    _RuijieIpPreClassPriority_Type()
)
ruijieIpPreClassPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpPreClassPriority.setStatus("current")
_RuijieIpPreToDscp_Type = Integer32
_RuijieIpPreToDscp_Object = MibTableColumn
ruijieIpPreToDscp = _RuijieIpPreToDscp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 10, 1, 2),
    _RuijieIpPreToDscp_Type()
)
ruijieIpPreToDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIpPreToDscp.setStatus("current")
_RuijieIfRateLimitTable_Object = MibTable
ruijieIfRateLimitTable = _RuijieIfRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 11)
)
if mibBuilder.loadTexts:
    ruijieIfRateLimitTable.setStatus("current")
_RuijieIfRateLimitEntry_Object = MibTableRow
ruijieIfRateLimitEntry = _RuijieIfRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 11, 1)
)
ruijieIfRateLimitEntry.setIndexNames(
    (0, "RUIJIE-QOS-MIB", "ruijieIfRateLimitIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfRateLimitEntry.setStatus("current")
_RuijieIfRateLimitIndex_Type = IfIndex
_RuijieIfRateLimitIndex_Object = MibTableColumn
ruijieIfRateLimitIndex = _RuijieIfRateLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 11, 1, 1),
    _RuijieIfRateLimitIndex_Type()
)
ruijieIfRateLimitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfRateLimitIndex.setStatus("current")
_RuijieIfRateLimitInMaxBandWidth_Type = Unsigned32
_RuijieIfRateLimitInMaxBandWidth_Object = MibTableColumn
ruijieIfRateLimitInMaxBandWidth = _RuijieIfRateLimitInMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 11, 1, 2),
    _RuijieIfRateLimitInMaxBandWidth_Type()
)
ruijieIfRateLimitInMaxBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfRateLimitInMaxBandWidth.setStatus("current")
_RuijieIfRateLimitInBurstFlowLimit_Type = Integer32
_RuijieIfRateLimitInBurstFlowLimit_Object = MibTableColumn
ruijieIfRateLimitInBurstFlowLimit = _RuijieIfRateLimitInBurstFlowLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 11, 1, 3),
    _RuijieIfRateLimitInBurstFlowLimit_Type()
)
ruijieIfRateLimitInBurstFlowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfRateLimitInBurstFlowLimit.setStatus("current")
_RuijieIfRateLimitOutMaxBandWidth_Type = Unsigned32
_RuijieIfRateLimitOutMaxBandWidth_Object = MibTableColumn
ruijieIfRateLimitOutMaxBandWidth = _RuijieIfRateLimitOutMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 11, 1, 4),
    _RuijieIfRateLimitOutMaxBandWidth_Type()
)
ruijieIfRateLimitOutMaxBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfRateLimitOutMaxBandWidth.setStatus("current")
_RuijieIfRateLimitOutBurstFlowLimit_Type = Integer32
_RuijieIfRateLimitOutBurstFlowLimit_Object = MibTableColumn
ruijieIfRateLimitOutBurstFlowLimit = _RuijieIfRateLimitOutBurstFlowLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 11, 1, 5),
    _RuijieIfRateLimitOutBurstFlowLimit_Type()
)
ruijieIfRateLimitOutBurstFlowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfRateLimitOutBurstFlowLimit.setStatus("current")
_RuijieIfQueueSupportTable_Object = MibTable
ruijieIfQueueSupportTable = _RuijieIfQueueSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12)
)
if mibBuilder.loadTexts:
    ruijieIfQueueSupportTable.setStatus("current")
_RuijieIfQueueSupportEntry_Object = MibTableRow
ruijieIfQueueSupportEntry = _RuijieIfQueueSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1)
)
ruijieIfQueueSupportEntry.setIndexNames(
    (0, "RUIJIE-QOS-MIB", "ruijieIfIndex"),
    (0, "RUIJIE-QOS-MIB", "ruijieIfQueueIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfQueueSupportEntry.setStatus("current")
_RuijieIfIndex_Type = IfIndex
_RuijieIfIndex_Object = MibTableColumn
ruijieIfIndex = _RuijieIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 1),
    _RuijieIfIndex_Type()
)
ruijieIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIndex.setStatus("current")
_RuijieIfQueueIndex_Type = Integer32
_RuijieIfQueueIndex_Object = MibTableColumn
ruijieIfQueueIndex = _RuijieIfQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 2),
    _RuijieIfQueueIndex_Type()
)
ruijieIfQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQueueIndex.setStatus("current")
_RuijieIfQueueSupportTransmitPacket_Type = Counter64
_RuijieIfQueueSupportTransmitPacket_Object = MibTableColumn
ruijieIfQueueSupportTransmitPacket = _RuijieIfQueueSupportTransmitPacket_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 3),
    _RuijieIfQueueSupportTransmitPacket_Type()
)
ruijieIfQueueSupportTransmitPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQueueSupportTransmitPacket.setStatus("current")
_RuijieIfQueueSupportTransmitBytes_Type = Counter64
_RuijieIfQueueSupportTransmitBytes_Object = MibTableColumn
ruijieIfQueueSupportTransmitBytes = _RuijieIfQueueSupportTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 4),
    _RuijieIfQueueSupportTransmitBytes_Type()
)
ruijieIfQueueSupportTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQueueSupportTransmitBytes.setStatus("current")
_RuijieIfQueueSupportDropPacket_Type = Counter64
_RuijieIfQueueSupportDropPacket_Object = MibTableColumn
ruijieIfQueueSupportDropPacket = _RuijieIfQueueSupportDropPacket_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 5),
    _RuijieIfQueueSupportDropPacket_Type()
)
ruijieIfQueueSupportDropPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQueueSupportDropPacket.setStatus("current")
_RuijieIfQueueSupportDropBytes_Type = Counter64
_RuijieIfQueueSupportDropBytes_Object = MibTableColumn
ruijieIfQueueSupportDropBytes = _RuijieIfQueueSupportDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 6),
    _RuijieIfQueueSupportDropBytes_Type()
)
ruijieIfQueueSupportDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQueueSupportDropBytes.setStatus("current")
_RuijieIfQueueSupportTransmitPacketsRate_Type = Counter64
_RuijieIfQueueSupportTransmitPacketsRate_Object = MibTableColumn
ruijieIfQueueSupportTransmitPacketsRate = _RuijieIfQueueSupportTransmitPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 7),
    _RuijieIfQueueSupportTransmitPacketsRate_Type()
)
ruijieIfQueueSupportTransmitPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQueueSupportTransmitPacketsRate.setStatus("current")
_RuijieIfQueueSupportTransmitBitsRate_Type = Counter64
_RuijieIfQueueSupportTransmitBitsRate_Object = MibTableColumn
ruijieIfQueueSupportTransmitBitsRate = _RuijieIfQueueSupportTransmitBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 8),
    _RuijieIfQueueSupportTransmitBitsRate_Type()
)
ruijieIfQueueSupportTransmitBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQueueSupportTransmitBitsRate.setStatus("current")
_RuijieIfQueueSupportPacketsLossRate_Type = Integer32
_RuijieIfQueueSupportPacketsLossRate_Object = MibTableColumn
ruijieIfQueueSupportPacketsLossRate = _RuijieIfQueueSupportPacketsLossRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 9),
    _RuijieIfQueueSupportPacketsLossRate_Type()
)
ruijieIfQueueSupportPacketsLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQueueSupportPacketsLossRate.setStatus("current")
_RuijieIfQueueSupportBytesLossRate_Type = Integer32
_RuijieIfQueueSupportBytesLossRate_Object = MibTableColumn
ruijieIfQueueSupportBytesLossRate = _RuijieIfQueueSupportBytesLossRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 10),
    _RuijieIfQueueSupportBytesLossRate_Type()
)
ruijieIfQueueSupportBytesLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQueueSupportBytesLossRate.setStatus("current")
_RuijieIfQueueSupportDropPacketsRate_Type = Counter64
_RuijieIfQueueSupportDropPacketsRate_Object = MibTableColumn
ruijieIfQueueSupportDropPacketsRate = _RuijieIfQueueSupportDropPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 11),
    _RuijieIfQueueSupportDropPacketsRate_Type()
)
ruijieIfQueueSupportDropPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQueueSupportDropPacketsRate.setStatus("current")
_RuijieIfQueueSupportDropBitsRate_Type = Counter64
_RuijieIfQueueSupportDropBitsRate_Object = MibTableColumn
ruijieIfQueueSupportDropBitsRate = _RuijieIfQueueSupportDropBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 12),
    _RuijieIfQueueSupportDropBitsRate_Type()
)
ruijieIfQueueSupportDropBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQueueSupportDropBitsRate.setStatus("current")


class _RuijieIfQueueSupportQueueName_Type(DisplayString):
    """Custom type ruijieIfQueueSupportQueueName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieIfQueueSupportQueueName_Type.__name__ = "DisplayString"
_RuijieIfQueueSupportQueueName_Object = MibTableColumn
ruijieIfQueueSupportQueueName = _RuijieIfQueueSupportQueueName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 13),
    _RuijieIfQueueSupportQueueName_Type()
)
ruijieIfQueueSupportQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQueueSupportQueueName.setStatus("current")
_RuijieIfQueueSupportInQueuePackets_Type = Counter64
_RuijieIfQueueSupportInQueuePackets_Object = MibTableColumn
ruijieIfQueueSupportInQueuePackets = _RuijieIfQueueSupportInQueuePackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 14),
    _RuijieIfQueueSupportInQueuePackets_Type()
)
ruijieIfQueueSupportInQueuePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQueueSupportInQueuePackets.setStatus("current")
_RuijieIfQueueSupportInQueueBytes_Type = Counter64
_RuijieIfQueueSupportInQueueBytes_Object = MibTableColumn
ruijieIfQueueSupportInQueueBytes = _RuijieIfQueueSupportInQueueBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 15),
    _RuijieIfQueueSupportInQueueBytes_Type()
)
ruijieIfQueueSupportInQueueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQueueSupportInQueueBytes.setStatus("current")
_RuijieIfQueueSupportTailDropPackets_Type = Counter64
_RuijieIfQueueSupportTailDropPackets_Object = MibTableColumn
ruijieIfQueueSupportTailDropPackets = _RuijieIfQueueSupportTailDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 16),
    _RuijieIfQueueSupportTailDropPackets_Type()
)
ruijieIfQueueSupportTailDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQueueSupportTailDropPackets.setStatus("current")
_RuijieIfQueueSupportTailDropBytes_Type = Counter64
_RuijieIfQueueSupportTailDropBytes_Object = MibTableColumn
ruijieIfQueueSupportTailDropBytes = _RuijieIfQueueSupportTailDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 17),
    _RuijieIfQueueSupportTailDropBytes_Type()
)
ruijieIfQueueSupportTailDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQueueSupportTailDropBytes.setStatus("current")
_RuijieIfQueueSupportWredDropPackets_Type = Counter64
_RuijieIfQueueSupportWredDropPackets_Object = MibTableColumn
ruijieIfQueueSupportWredDropPackets = _RuijieIfQueueSupportWredDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 18),
    _RuijieIfQueueSupportWredDropPackets_Type()
)
ruijieIfQueueSupportWredDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQueueSupportWredDropPackets.setStatus("current")
_RuijieIfQueueSupportWredDropBytes_Type = Counter64
_RuijieIfQueueSupportWredDropBytes_Object = MibTableColumn
ruijieIfQueueSupportWredDropBytes = _RuijieIfQueueSupportWredDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 12, 1, 19),
    _RuijieIfQueueSupportWredDropBytes_Type()
)
ruijieIfQueueSupportWredDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfQueueSupportWredDropBytes.setStatus("current")
_RuijieIfMulticastQueueSupportTable_Object = MibTable
ruijieIfMulticastQueueSupportTable = _RuijieIfMulticastQueueSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 13)
)
if mibBuilder.loadTexts:
    ruijieIfMulticastQueueSupportTable.setStatus("current")
_RuijieIfMulticastQueueSupportEntry_Object = MibTableRow
ruijieIfMulticastQueueSupportEntry = _RuijieIfMulticastQueueSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 13, 1)
)
ruijieIfMulticastQueueSupportEntry.setIndexNames(
    (0, "RUIJIE-QOS-MIB", "ruijieIfIndexMulticast"),
    (0, "RUIJIE-QOS-MIB", "ruijieIfMulticastQueueIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfMulticastQueueSupportEntry.setStatus("current")
_RuijieIfIndexMulticast_Type = IfIndex
_RuijieIfIndexMulticast_Object = MibTableColumn
ruijieIfIndexMulticast = _RuijieIfIndexMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 13, 1, 1),
    _RuijieIfIndexMulticast_Type()
)
ruijieIfIndexMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIndexMulticast.setStatus("current")
_RuijieIfMulticastQueueIndex_Type = Integer32
_RuijieIfMulticastQueueIndex_Object = MibTableColumn
ruijieIfMulticastQueueIndex = _RuijieIfMulticastQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 13, 1, 2),
    _RuijieIfMulticastQueueIndex_Type()
)
ruijieIfMulticastQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfMulticastQueueIndex.setStatus("current")
_RuijieIfMulticastQueueSupportTransmitPacket_Type = Counter64
_RuijieIfMulticastQueueSupportTransmitPacket_Object = MibTableColumn
ruijieIfMulticastQueueSupportTransmitPacket = _RuijieIfMulticastQueueSupportTransmitPacket_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 13, 1, 3),
    _RuijieIfMulticastQueueSupportTransmitPacket_Type()
)
ruijieIfMulticastQueueSupportTransmitPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfMulticastQueueSupportTransmitPacket.setStatus("current")
_RuijieIfMulticastQueueSupportTransmitBytes_Type = Counter64
_RuijieIfMulticastQueueSupportTransmitBytes_Object = MibTableColumn
ruijieIfMulticastQueueSupportTransmitBytes = _RuijieIfMulticastQueueSupportTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 13, 1, 4),
    _RuijieIfMulticastQueueSupportTransmitBytes_Type()
)
ruijieIfMulticastQueueSupportTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfMulticastQueueSupportTransmitBytes.setStatus("current")
_RuijieIfMulticastQueueSupportDropPacket_Type = Counter64
_RuijieIfMulticastQueueSupportDropPacket_Object = MibTableColumn
ruijieIfMulticastQueueSupportDropPacket = _RuijieIfMulticastQueueSupportDropPacket_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 13, 1, 5),
    _RuijieIfMulticastQueueSupportDropPacket_Type()
)
ruijieIfMulticastQueueSupportDropPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfMulticastQueueSupportDropPacket.setStatus("current")
_RuijieIfMulticastQueueSupportDropBytes_Type = Counter64
_RuijieIfMulticastQueueSupportDropBytes_Object = MibTableColumn
ruijieIfMulticastQueueSupportDropBytes = _RuijieIfMulticastQueueSupportDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 13, 1, 6),
    _RuijieIfMulticastQueueSupportDropBytes_Type()
)
ruijieIfMulticastQueueSupportDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfMulticastQueueSupportDropBytes.setStatus("current")
_RuijieWredEcnStatsTable_Object = MibTable
ruijieWredEcnStatsTable = _RuijieWredEcnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 14)
)
if mibBuilder.loadTexts:
    ruijieWredEcnStatsTable.setStatus("current")
_RuijieWredEcnStatsEntry_Object = MibTableRow
ruijieWredEcnStatsEntry = _RuijieWredEcnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 14, 1)
)
ruijieWredEcnStatsEntry.setIndexNames(
    (0, "RUIJIE-QOS-MIB", "ruijieWredEcnStatsIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieWredEcnStatsEntry.setStatus("current")
_RuijieWredEcnStatsIfIndex_Type = Unsigned32
_RuijieWredEcnStatsIfIndex_Object = MibTableColumn
ruijieWredEcnStatsIfIndex = _RuijieWredEcnStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 14, 1, 1),
    _RuijieWredEcnStatsIfIndex_Type()
)
ruijieWredEcnStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWredEcnStatsIfIndex.setStatus("current")


class _RuijieWredDropped_Type(Counter64):
    """Custom type ruijieWredDropped based on Counter64"""
    defaultValue = 0


_RuijieWredDropped_Type.__name__ = "Counter64"
_RuijieWredDropped_Object = MibTableColumn
ruijieWredDropped = _RuijieWredDropped_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 14, 1, 2),
    _RuijieWredDropped_Type()
)
ruijieWredDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWredDropped.setStatus("current")


class _RuijieEcnSended_Type(Counter64):
    """Custom type ruijieEcnSended based on Counter64"""
    defaultValue = 0


_RuijieEcnSended_Type.__name__ = "Counter64"
_RuijieEcnSended_Object = MibTableColumn
ruijieEcnSended = _RuijieEcnSended_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 14, 1, 3),
    _RuijieEcnSended_Type()
)
ruijieEcnSended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEcnSended.setStatus("current")
_RuijieQoSDsProTable_Object = MibTable
ruijieQoSDsProTable = _RuijieQoSDsProTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 15)
)
if mibBuilder.loadTexts:
    ruijieQoSDsProTable.setStatus("current")
_RuijieQoSDsProEntry_Object = MibTableRow
ruijieQoSDsProEntry = _RuijieQoSDsProEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 15, 1)
)
ruijieQoSDsProEntry.setIndexNames(
    (0, "RUIJIE-QOS-MIB", "ruijieQoSDsProIndex"),
)
if mibBuilder.loadTexts:
    ruijieQoSDsProEntry.setStatus("current")
_RuijieQoSDsProIndex_Type = Unsigned32
_RuijieQoSDsProIndex_Object = MibTableColumn
ruijieQoSDsProIndex = _RuijieQoSDsProIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 15, 1, 1),
    _RuijieQoSDsProIndex_Type()
)
ruijieQoSDsProIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSDsProIndex.setStatus("current")


class _RuijieQoSDsProName_Type(DisplayString):
    """Custom type ruijieQoSDsProName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RuijieQoSDsProName_Type.__name__ = "DisplayString"
_RuijieQoSDsProName_Object = MibTableColumn
ruijieQoSDsProName = _RuijieQoSDsProName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 15, 1, 2),
    _RuijieQoSDsProName_Type()
)
ruijieQoSDsProName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieQoSDsProName.setStatus("current")
_RuijieQoSDsProInMapTable_Object = MibTable
ruijieQoSDsProInMapTable = _RuijieQoSDsProInMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 16)
)
if mibBuilder.loadTexts:
    ruijieQoSDsProInMapTable.setStatus("current")
_RuijieQoSDsProInMapEntry_Object = MibTableRow
ruijieQoSDsProInMapEntry = _RuijieQoSDsProInMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 16, 1)
)
ruijieQoSDsProInMapEntry.setIndexNames(
    (0, "RUIJIE-QOS-MIB", "ruijieQoSDsProInMapName"),
    (0, "RUIJIE-QOS-MIB", "ruijieQoSDsProInMapType"),
    (0, "RUIJIE-QOS-MIB", "ruijieQoSDsProInMapPri"),
)
if mibBuilder.loadTexts:
    ruijieQoSDsProInMapEntry.setStatus("current")


class _RuijieQoSDsProInMapName_Type(DisplayString):
    """Custom type ruijieQoSDsProInMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RuijieQoSDsProInMapName_Type.__name__ = "DisplayString"
_RuijieQoSDsProInMapName_Object = MibTableColumn
ruijieQoSDsProInMapName = _RuijieQoSDsProInMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 16, 1, 1),
    _RuijieQoSDsProInMapName_Type()
)
ruijieQoSDsProInMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSDsProInMapName.setStatus("current")


class _RuijieQoSDsProInMapType_Type(Integer32):
    """Custom type ruijieQoSDsProInMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ip-dscp-input", 1),
          ("dot1p-input", 3),
          ("mpls-exp-input", 5))
    )


_RuijieQoSDsProInMapType_Type.__name__ = "Integer32"
_RuijieQoSDsProInMapType_Object = MibTableColumn
ruijieQoSDsProInMapType = _RuijieQoSDsProInMapType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 16, 1, 2),
    _RuijieQoSDsProInMapType_Type()
)
ruijieQoSDsProInMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSDsProInMapType.setStatus("current")
_RuijieQoSDsProInMapPri_Type = Unsigned32
_RuijieQoSDsProInMapPri_Object = MibTableColumn
ruijieQoSDsProInMapPri = _RuijieQoSDsProInMapPri_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 16, 1, 3),
    _RuijieQoSDsProInMapPri_Type()
)
ruijieQoSDsProInMapPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSDsProInMapPri.setStatus("current")
_RuijieQoSDsProInMapCos_Type = Unsigned32
_RuijieQoSDsProInMapCos_Object = MibTableColumn
ruijieQoSDsProInMapCos = _RuijieQoSDsProInMapCos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 16, 1, 4),
    _RuijieQoSDsProInMapCos_Type()
)
ruijieQoSDsProInMapCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieQoSDsProInMapCos.setStatus("current")


class _RuijieQoSDsProInMapColor_Type(Integer32):
    """Custom type ruijieQoSDsProInMapColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 0),
          ("yellow", 1),
          ("red", 2))
    )


_RuijieQoSDsProInMapColor_Type.__name__ = "Integer32"
_RuijieQoSDsProInMapColor_Object = MibTableColumn
ruijieQoSDsProInMapColor = _RuijieQoSDsProInMapColor_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 16, 1, 5),
    _RuijieQoSDsProInMapColor_Type()
)
ruijieQoSDsProInMapColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieQoSDsProInMapColor.setStatus("current")
_RuijieQoSDsProOutMapTable_Object = MibTable
ruijieQoSDsProOutMapTable = _RuijieQoSDsProOutMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 17)
)
if mibBuilder.loadTexts:
    ruijieQoSDsProOutMapTable.setStatus("current")
_RuijieQoSDsProOutMapEntry_Object = MibTableRow
ruijieQoSDsProOutMapEntry = _RuijieQoSDsProOutMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 17, 1)
)
ruijieQoSDsProOutMapEntry.setIndexNames(
    (0, "RUIJIE-QOS-MIB", "ruijieQoSDsProOutMapName"),
    (0, "RUIJIE-QOS-MIB", "ruijieQoSDsProOutMapType"),
    (0, "RUIJIE-QOS-MIB", "ruijieQoSDsProOutMapCos"),
    (0, "RUIJIE-QOS-MIB", "ruijieQoSDsProOutMapColor"),
)
if mibBuilder.loadTexts:
    ruijieQoSDsProOutMapEntry.setStatus("current")


class _RuijieQoSDsProOutMapName_Type(DisplayString):
    """Custom type ruijieQoSDsProOutMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RuijieQoSDsProOutMapName_Type.__name__ = "DisplayString"
_RuijieQoSDsProOutMapName_Object = MibTableColumn
ruijieQoSDsProOutMapName = _RuijieQoSDsProOutMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 17, 1, 1),
    _RuijieQoSDsProOutMapName_Type()
)
ruijieQoSDsProOutMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSDsProOutMapName.setStatus("current")


class _RuijieQoSDsProOutMapType_Type(Integer32):
    """Custom type ruijieQoSDsProOutMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ip-dscp-output", 2),
          ("dot1p-output", 4),
          ("mpls-exp-output", 6))
    )


_RuijieQoSDsProOutMapType_Type.__name__ = "Integer32"
_RuijieQoSDsProOutMapType_Object = MibTableColumn
ruijieQoSDsProOutMapType = _RuijieQoSDsProOutMapType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 17, 1, 2),
    _RuijieQoSDsProOutMapType_Type()
)
ruijieQoSDsProOutMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSDsProOutMapType.setStatus("current")
_RuijieQoSDsProOutMapCos_Type = Unsigned32
_RuijieQoSDsProOutMapCos_Object = MibTableColumn
ruijieQoSDsProOutMapCos = _RuijieQoSDsProOutMapCos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 17, 1, 3),
    _RuijieQoSDsProOutMapCos_Type()
)
ruijieQoSDsProOutMapCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSDsProOutMapCos.setStatus("current")


class _RuijieQoSDsProOutMapColor_Type(Integer32):
    """Custom type ruijieQoSDsProOutMapColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 0),
          ("yellow", 1),
          ("red", 2))
    )


_RuijieQoSDsProOutMapColor_Type.__name__ = "Integer32"
_RuijieQoSDsProOutMapColor_Object = MibTableColumn
ruijieQoSDsProOutMapColor = _RuijieQoSDsProOutMapColor_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 17, 1, 4),
    _RuijieQoSDsProOutMapColor_Type()
)
ruijieQoSDsProOutMapColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSDsProOutMapColor.setStatus("current")
_RuijieQoSDsProOutMapPri_Type = Unsigned32
_RuijieQoSDsProOutMapPri_Object = MibTableColumn
ruijieQoSDsProOutMapPri = _RuijieQoSDsProOutMapPri_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 17, 1, 5),
    _RuijieQoSDsProOutMapPri_Type()
)
ruijieQoSDsProOutMapPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieQoSDsProOutMapPri.setStatus("current")
_RuijieQoSIfDirTable_Object = MibTable
ruijieQoSIfDirTable = _RuijieQoSIfDirTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 18)
)
if mibBuilder.loadTexts:
    ruijieQoSIfDirTable.setStatus("current")
_RuijieQoSIfDirEntry_Object = MibTableRow
ruijieQoSIfDirEntry = _RuijieQoSIfDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 18, 1)
)
ruijieQoSIfDirEntry.setIndexNames(
    (0, "RUIJIE-QOS-MIB", "ruijieQoSIfIndex"),
    (0, "RUIJIE-QOS-MIB", "ruijieQoSIfDirIndex"),
)
if mibBuilder.loadTexts:
    ruijieQoSIfDirEntry.setStatus("current")
_RuijieQoSIfIndex_Type = IfIndex
_RuijieQoSIfIndex_Object = MibTableColumn
ruijieQoSIfIndex = _RuijieQoSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 18, 1, 1),
    _RuijieQoSIfIndex_Type()
)
ruijieQoSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSIfIndex.setStatus("current")


class _RuijieQoSIfDirIndex_Type(Integer32):
    """Custom type ruijieQoSIfDirIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("input", 0),
          ("output", 1))
    )


_RuijieQoSIfDirIndex_Type.__name__ = "Integer32"
_RuijieQoSIfDirIndex_Object = MibTableColumn
ruijieQoSIfDirIndex = _RuijieQoSIfDirIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 18, 1, 2),
    _RuijieQoSIfDirIndex_Type()
)
ruijieQoSIfDirIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSIfDirIndex.setStatus("current")


class _RuijieQoSIfDirDsProName_Type(DisplayString):
    """Custom type ruijieQoSIfDirDsProName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RuijieQoSIfDirDsProName_Type.__name__ = "DisplayString"
_RuijieQoSIfDirDsProName_Object = MibTableColumn
ruijieQoSIfDirDsProName = _RuijieQoSIfDirDsProName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 18, 1, 3),
    _RuijieQoSIfDirDsProName_Type()
)
ruijieQoSIfDirDsProName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieQoSIfDirDsProName.setStatus("current")
_RuijieQoSIfStatisTable_Object = MibTable
ruijieQoSIfStatisTable = _RuijieQoSIfStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 19)
)
if mibBuilder.loadTexts:
    ruijieQoSIfStatisTable.setStatus("current")
_RuijieQoSIfStatisEntry_Object = MibTableRow
ruijieQoSIfStatisEntry = _RuijieQoSIfStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 19, 1)
)
ruijieQoSIfStatisEntry.setIndexNames(
    (0, "RUIJIE-QOS-MIB", "ruijieQoSIfStatisIndex"),
)
if mibBuilder.loadTexts:
    ruijieQoSIfStatisEntry.setStatus("current")
_RuijieQoSIfStatisIndex_Type = IfIndex
_RuijieQoSIfStatisIndex_Object = MibTableColumn
ruijieQoSIfStatisIndex = _RuijieQoSIfStatisIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 19, 1, 1),
    _RuijieQoSIfStatisIndex_Type()
)
ruijieQoSIfStatisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSIfStatisIndex.setStatus("current")
_RuijieQoSIfInBytes_Type = Counter64
_RuijieQoSIfInBytes_Object = MibTableColumn
ruijieQoSIfInBytes = _RuijieQoSIfInBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 19, 1, 2),
    _RuijieQoSIfInBytes_Type()
)
ruijieQoSIfInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSIfInBytes.setStatus("current")
_RuijieQoSIfInPkts_Type = Counter64
_RuijieQoSIfInPkts_Object = MibTableColumn
ruijieQoSIfInPkts = _RuijieQoSIfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 19, 1, 3),
    _RuijieQoSIfInPkts_Type()
)
ruijieQoSIfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSIfInPkts.setStatus("current")
_RuijieQoSTrafficClassMIBObjects_ObjectIdentity = ObjectIdentity
ruijieQoSTrafficClassMIBObjects = _RuijieQoSTrafficClassMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2)
)
_RuijieQoSTrafficClassTable_Object = MibTable
ruijieQoSTrafficClassTable = _RuijieQoSTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieQoSTrafficClassTable.setStatus("current")
_RuijieQoSTrafficClassEntry_Object = MibTableRow
ruijieQoSTrafficClassEntry = _RuijieQoSTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 1, 1)
)
ruijieQoSTrafficClassEntry.setIndexNames(
    (0, "RUIJIE-QOS-MIB", "ruijieQosClassMapName"),
)
if mibBuilder.loadTexts:
    ruijieQoSTrafficClassEntry.setStatus("current")


class _RuijieQosClassMapName_Type(DisplayString):
    """Custom type ruijieQosClassMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieQosClassMapName_Type.__name__ = "DisplayString"
_RuijieQosClassMapName_Object = MibTableColumn
ruijieQosClassMapName = _RuijieQosClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 1, 1, 1),
    _RuijieQosClassMapName_Type()
)
ruijieQosClassMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQosClassMapName.setStatus("current")


class _RuijieQosClassAclName_Type(DisplayString):
    """Custom type ruijieQosClassAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieQosClassAclName_Type.__name__ = "DisplayString"
_RuijieQosClassAclName_Object = MibTableColumn
ruijieQosClassAclName = _RuijieQosClassAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 1, 1, 2),
    _RuijieQosClassAclName_Type()
)
ruijieQosClassAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieQosClassAclName.setStatus("current")
_RuijieQosClassMapEntryStatus_Type = ConfigStatus
_RuijieQosClassMapEntryStatus_Object = MibTableColumn
ruijieQosClassMapEntryStatus = _RuijieQosClassMapEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 1, 1, 3),
    _RuijieQosClassMapEntryStatus_Type()
)
ruijieQosClassMapEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieQosClassMapEntryStatus.setStatus("current")
_RuijieQoSPoliceMapTable_Object = MibTable
ruijieQoSPoliceMapTable = _RuijieQoSPoliceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 2)
)
if mibBuilder.loadTexts:
    ruijieQoSPoliceMapTable.setStatus("current")
_RuijieQoSPoliceMapEntry_Object = MibTableRow
ruijieQoSPoliceMapEntry = _RuijieQoSPoliceMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 2, 1)
)
ruijieQoSPoliceMapEntry.setIndexNames(
    (0, "RUIJIE-QOS-MIB", "ruijieQosPoliceMapName"),
)
if mibBuilder.loadTexts:
    ruijieQoSPoliceMapEntry.setStatus("current")


class _RuijieQosPoliceMapName_Type(DisplayString):
    """Custom type ruijieQosPoliceMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieQosPoliceMapName_Type.__name__ = "DisplayString"
_RuijieQosPoliceMapName_Object = MibTableColumn
ruijieQosPoliceMapName = _RuijieQosPoliceMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 2, 1, 1),
    _RuijieQosPoliceMapName_Type()
)
ruijieQosPoliceMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQosPoliceMapName.setStatus("current")
_RuijieQosPoliceMapEntryStatus_Type = ConfigStatus
_RuijieQosPoliceMapEntryStatus_Object = MibTableColumn
ruijieQosPoliceMapEntryStatus = _RuijieQosPoliceMapEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 2, 1, 2),
    _RuijieQosPoliceMapEntryStatus_Type()
)
ruijieQosPoliceMapEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieQosPoliceMapEntryStatus.setStatus("current")
_RuijieQoSPoliceMapConfTable_Object = MibTable
ruijieQoSPoliceMapConfTable = _RuijieQoSPoliceMapConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3)
)
if mibBuilder.loadTexts:
    ruijieQoSPoliceMapConfTable.setStatus("current")
_RuijieQoSPoliceMapConfEntry_Object = MibTableRow
ruijieQoSPoliceMapConfEntry = _RuijieQoSPoliceMapConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1)
)
ruijieQoSPoliceMapConfEntry.setIndexNames(
    (0, "RUIJIE-QOS-MIB", "ruijieQoSPoliceCfgPoliceMapName"),
    (0, "RUIJIE-QOS-MIB", "ruijieQoSPoliceCfgClassMapName"),
)
if mibBuilder.loadTexts:
    ruijieQoSPoliceMapConfEntry.setStatus("current")


class _RuijieQoSPoliceCfgPoliceMapName_Type(DisplayString):
    """Custom type ruijieQoSPoliceCfgPoliceMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieQoSPoliceCfgPoliceMapName_Type.__name__ = "DisplayString"
_RuijieQoSPoliceCfgPoliceMapName_Object = MibTableColumn
ruijieQoSPoliceCfgPoliceMapName = _RuijieQoSPoliceCfgPoliceMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1, 1),
    _RuijieQoSPoliceCfgPoliceMapName_Type()
)
ruijieQoSPoliceCfgPoliceMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSPoliceCfgPoliceMapName.setStatus("current")


class _RuijieQoSPoliceCfgClassMapName_Type(DisplayString):
    """Custom type ruijieQoSPoliceCfgClassMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieQoSPoliceCfgClassMapName_Type.__name__ = "DisplayString"
_RuijieQoSPoliceCfgClassMapName_Object = MibTableColumn
ruijieQoSPoliceCfgClassMapName = _RuijieQoSPoliceCfgClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1, 2),
    _RuijieQoSPoliceCfgClassMapName_Type()
)
ruijieQoSPoliceCfgClassMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieQoSPoliceCfgClassMapName.setStatus("current")
_RuijieQoSPoliceMapConfMaxBandWidth_Type = Unsigned32
_RuijieQoSPoliceMapConfMaxBandWidth_Object = MibTableColumn
ruijieQoSPoliceMapConfMaxBandWidth = _RuijieQoSPoliceMapConfMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1, 3),
    _RuijieQoSPoliceMapConfMaxBandWidth_Type()
)
ruijieQoSPoliceMapConfMaxBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieQoSPoliceMapConfMaxBandWidth.setStatus("current")
_RuijieQoSPoliceMapConfBurstFlowLimit_Type = Integer32
_RuijieQoSPoliceMapConfBurstFlowLimit_Object = MibTableColumn
ruijieQoSPoliceMapConfBurstFlowLimit = _RuijieQoSPoliceMapConfBurstFlowLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1, 4),
    _RuijieQoSPoliceMapConfBurstFlowLimit_Type()
)
ruijieQoSPoliceMapConfBurstFlowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieQoSPoliceMapConfBurstFlowLimit.setStatus("current")


class _RuijieQoSPoliceMapConfExceedAction_Type(Integer32):
    """Custom type ruijieQoSPoliceMapConfExceedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("modify-dscp", 2))
    )


_RuijieQoSPoliceMapConfExceedAction_Type.__name__ = "Integer32"
_RuijieQoSPoliceMapConfExceedAction_Object = MibTableColumn
ruijieQoSPoliceMapConfExceedAction = _RuijieQoSPoliceMapConfExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1, 5),
    _RuijieQoSPoliceMapConfExceedAction_Type()
)
ruijieQoSPoliceMapConfExceedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieQoSPoliceMapConfExceedAction.setStatus("current")
_RuijieQoSPoliceMapConfExceedDscp_Type = Integer32
_RuijieQoSPoliceMapConfExceedDscp_Object = MibTableColumn
ruijieQoSPoliceMapConfExceedDscp = _RuijieQoSPoliceMapConfExceedDscp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1, 6),
    _RuijieQoSPoliceMapConfExceedDscp_Type()
)
ruijieQoSPoliceMapConfExceedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieQoSPoliceMapConfExceedDscp.setStatus("current")
_RuijieQoSPoliceMapConfNewDscp_Type = Integer32
_RuijieQoSPoliceMapConfNewDscp_Object = MibTableColumn
ruijieQoSPoliceMapConfNewDscp = _RuijieQoSPoliceMapConfNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1, 7),
    _RuijieQoSPoliceMapConfNewDscp_Type()
)
ruijieQoSPoliceMapConfNewDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieQoSPoliceMapConfNewDscp.setStatus("current")
_RuijieQoSPoliceMapCfgEntryStatus_Type = ConfigStatus
_RuijieQoSPoliceMapCfgEntryStatus_Object = MibTableColumn
ruijieQoSPoliceMapCfgEntryStatus = _RuijieQoSPoliceMapCfgEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1, 8),
    _RuijieQoSPoliceMapCfgEntryStatus_Type()
)
ruijieQoSPoliceMapCfgEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieQoSPoliceMapCfgEntryStatus.setStatus("current")
_RuijieQoSPoliceMapConfMaxHighBandWidth_Type = Unsigned32
_RuijieQoSPoliceMapConfMaxHighBandWidth_Object = MibTableColumn
ruijieQoSPoliceMapConfMaxHighBandWidth = _RuijieQoSPoliceMapConfMaxHighBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1, 9),
    _RuijieQoSPoliceMapConfMaxHighBandWidth_Type()
)
ruijieQoSPoliceMapConfMaxHighBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieQoSPoliceMapConfMaxHighBandWidth.setStatus("current")
_RuijieQosPoliceIfExtTable_Object = MibTable
ruijieQosPoliceIfExtTable = _RuijieQosPoliceIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 5)
)
if mibBuilder.loadTexts:
    ruijieQosPoliceIfExtTable.setStatus("current")
_RuijieQosPoliceIfExtEntry_Object = MibTableRow
ruijieQosPoliceIfExtEntry = _RuijieQosPoliceIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 5, 1)
)
ruijieQosPoliceIfExtEntry.setIndexNames(
    (0, "RUIJIE-QOS-MIB", "ruijieQosPoliceIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieQosPoliceIfExtEntry.setStatus("current")
_RuijieQosPoliceIfIndex_Type = IfIndex
_RuijieQosPoliceIfIndex_Object = MibTableColumn
ruijieQosPoliceIfIndex = _RuijieQosPoliceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 5, 1, 1),
    _RuijieQosPoliceIfIndex_Type()
)
ruijieQosPoliceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQosPoliceIfIndex.setStatus("current")


class _RuijieIfInPoliceMapName_Type(DisplayString):
    """Custom type ruijieIfInPoliceMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieIfInPoliceMapName_Type.__name__ = "DisplayString"
_RuijieIfInPoliceMapName_Object = MibTableColumn
ruijieIfInPoliceMapName = _RuijieIfInPoliceMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 5, 1, 2),
    _RuijieIfInPoliceMapName_Type()
)
ruijieIfInPoliceMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfInPoliceMapName.setStatus("current")


class _RuijieIfOutPoliceMapName_Type(DisplayString):
    """Custom type ruijieIfOutPoliceMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieIfOutPoliceMapName_Type.__name__ = "DisplayString"
_RuijieIfOutPoliceMapName_Object = MibTableColumn
ruijieIfOutPoliceMapName = _RuijieIfOutPoliceMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 5, 1, 3),
    _RuijieIfOutPoliceMapName_Type()
)
ruijieIfOutPoliceMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfOutPoliceMapName.setStatus("current")
_RuijieQosPoliceStatisTable_Object = MibTable
ruijieQosPoliceStatisTable = _RuijieQosPoliceStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 6)
)
if mibBuilder.loadTexts:
    ruijieQosPoliceStatisTable.setStatus("current")
_RuijieQosPoliceStatisEntry_Object = MibTableRow
ruijieQosPoliceStatisEntry = _RuijieQosPoliceStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 6, 1)
)
ruijieQosPoliceStatisEntry.setIndexNames(
    (0, "RUIJIE-QOS-MIB", "ruijieQosPoliceStatisIfIndex"),
    (0, "RUIJIE-QOS-MIB", "ruijieQosPoliceStatisDir"),
    (0, "RUIJIE-QOS-MIB", "ruijieQosPoliceStatisPmap"),
    (0, "RUIJIE-QOS-MIB", "ruijieQosPoliceStatisCmap"),
)
if mibBuilder.loadTexts:
    ruijieQosPoliceStatisEntry.setStatus("current")
_RuijieQosPoliceStatisIfIndex_Type = Unsigned32
_RuijieQosPoliceStatisIfIndex_Object = MibTableColumn
ruijieQosPoliceStatisIfIndex = _RuijieQosPoliceStatisIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 6, 1, 1),
    _RuijieQosPoliceStatisIfIndex_Type()
)
ruijieQosPoliceStatisIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQosPoliceStatisIfIndex.setStatus("current")


class _RuijieQosPoliceStatisDir_Type(Integer32):
    """Custom type ruijieQosPoliceStatisDir based on Integer32"""
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


_RuijieQosPoliceStatisDir_Type.__name__ = "Integer32"
_RuijieQosPoliceStatisDir_Object = MibTableColumn
ruijieQosPoliceStatisDir = _RuijieQosPoliceStatisDir_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 6, 1, 2),
    _RuijieQosPoliceStatisDir_Type()
)
ruijieQosPoliceStatisDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQosPoliceStatisDir.setStatus("current")


class _RuijieQosPoliceStatisPmap_Type(DisplayString):
    """Custom type ruijieQosPoliceStatisPmap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieQosPoliceStatisPmap_Type.__name__ = "DisplayString"
_RuijieQosPoliceStatisPmap_Object = MibTableColumn
ruijieQosPoliceStatisPmap = _RuijieQosPoliceStatisPmap_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 6, 1, 3),
    _RuijieQosPoliceStatisPmap_Type()
)
ruijieQosPoliceStatisPmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQosPoliceStatisPmap.setStatus("current")


class _RuijieQosPoliceStatisCmap_Type(DisplayString):
    """Custom type ruijieQosPoliceStatisCmap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieQosPoliceStatisCmap_Type.__name__ = "DisplayString"
_RuijieQosPoliceStatisCmap_Object = MibTableColumn
ruijieQosPoliceStatisCmap = _RuijieQosPoliceStatisCmap_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 6, 1, 4),
    _RuijieQosPoliceStatisCmap_Type()
)
ruijieQosPoliceStatisCmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQosPoliceStatisCmap.setStatus("current")


class _RuijieQosPoliceStatisMatchPackets_Type(Counter64):
    """Custom type ruijieQosPoliceStatisMatchPackets based on Counter64"""
    defaultValue = 0


_RuijieQosPoliceStatisMatchPackets_Type.__name__ = "Counter64"
_RuijieQosPoliceStatisMatchPackets_Object = MibTableColumn
ruijieQosPoliceStatisMatchPackets = _RuijieQosPoliceStatisMatchPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 6, 1, 5),
    _RuijieQosPoliceStatisMatchPackets_Type()
)
ruijieQosPoliceStatisMatchPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQosPoliceStatisMatchPackets.setStatus("current")


class _RuijieQosPoliceStatisMatchBytes_Type(Counter64):
    """Custom type ruijieQosPoliceStatisMatchBytes based on Counter64"""
    defaultValue = 0


_RuijieQosPoliceStatisMatchBytes_Type.__name__ = "Counter64"
_RuijieQosPoliceStatisMatchBytes_Object = MibTableColumn
ruijieQosPoliceStatisMatchBytes = _RuijieQosPoliceStatisMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 6, 1, 6),
    _RuijieQosPoliceStatisMatchBytes_Type()
)
ruijieQosPoliceStatisMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQosPoliceStatisMatchBytes.setStatus("current")


class _RuijieQosPoliceStatisMissPackets_Type(Counter64):
    """Custom type ruijieQosPoliceStatisMissPackets based on Counter64"""
    defaultValue = 0


_RuijieQosPoliceStatisMissPackets_Type.__name__ = "Counter64"
_RuijieQosPoliceStatisMissPackets_Object = MibTableColumn
ruijieQosPoliceStatisMissPackets = _RuijieQosPoliceStatisMissPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 6, 1, 7),
    _RuijieQosPoliceStatisMissPackets_Type()
)
ruijieQosPoliceStatisMissPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQosPoliceStatisMissPackets.setStatus("current")


class _RuijieQosPoliceStatisMissBytes_Type(Counter64):
    """Custom type ruijieQosPoliceStatisMissBytes based on Counter64"""
    defaultValue = 0


_RuijieQosPoliceStatisMissBytes_Type.__name__ = "Counter64"
_RuijieQosPoliceStatisMissBytes_Object = MibTableColumn
ruijieQosPoliceStatisMissBytes = _RuijieQosPoliceStatisMissBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 6, 1, 8),
    _RuijieQosPoliceStatisMissBytes_Type()
)
ruijieQosPoliceStatisMissBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQosPoliceStatisMissBytes.setStatus("current")


class _RuijieQosPoliceStatisPassPackets_Type(Counter64):
    """Custom type ruijieQosPoliceStatisPassPackets based on Counter64"""
    defaultValue = 0


_RuijieQosPoliceStatisPassPackets_Type.__name__ = "Counter64"
_RuijieQosPoliceStatisPassPackets_Object = MibTableColumn
ruijieQosPoliceStatisPassPackets = _RuijieQosPoliceStatisPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 6, 1, 9),
    _RuijieQosPoliceStatisPassPackets_Type()
)
ruijieQosPoliceStatisPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQosPoliceStatisPassPackets.setStatus("current")


class _RuijieQosPoliceStatisPassBytes_Type(Counter64):
    """Custom type ruijieQosPoliceStatisPassBytes based on Counter64"""
    defaultValue = 0


_RuijieQosPoliceStatisPassBytes_Type.__name__ = "Counter64"
_RuijieQosPoliceStatisPassBytes_Object = MibTableColumn
ruijieQosPoliceStatisPassBytes = _RuijieQosPoliceStatisPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 6, 1, 10),
    _RuijieQosPoliceStatisPassBytes_Type()
)
ruijieQosPoliceStatisPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQosPoliceStatisPassBytes.setStatus("current")


class _RuijieQosPoliceStatisDropPackets_Type(Counter64):
    """Custom type ruijieQosPoliceStatisDropPackets based on Counter64"""
    defaultValue = 0


_RuijieQosPoliceStatisDropPackets_Type.__name__ = "Counter64"
_RuijieQosPoliceStatisDropPackets_Object = MibTableColumn
ruijieQosPoliceStatisDropPackets = _RuijieQosPoliceStatisDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 6, 1, 11),
    _RuijieQosPoliceStatisDropPackets_Type()
)
ruijieQosPoliceStatisDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQosPoliceStatisDropPackets.setStatus("current")


class _RuijieQosPoliceStatisDropBytes_Type(Counter64):
    """Custom type ruijieQosPoliceStatisDropBytes based on Counter64"""
    defaultValue = 0


_RuijieQosPoliceStatisDropBytes_Type.__name__ = "Counter64"
_RuijieQosPoliceStatisDropBytes_Object = MibTableColumn
ruijieQosPoliceStatisDropBytes = _RuijieQosPoliceStatisDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 6, 1, 12),
    _RuijieQosPoliceStatisDropBytes_Type()
)
ruijieQosPoliceStatisDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQosPoliceStatisDropBytes.setStatus("current")
_RuijieQoSMIBConformance_ObjectIdentity = ObjectIdentity
ruijieQoSMIBConformance = _RuijieQoSMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 3)
)
_RuijieQoSMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieQoSMIBCompliances = _RuijieQoSMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 3, 1)
)
_RuijieQoSMIBGroups_ObjectIdentity = ObjectIdentity
ruijieQoSMIBGroups = _RuijieQoSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 3, 2)
)

# Managed Objects groups

ruijieQoSPriorityMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 3, 2, 1)
)
ruijieQoSPriorityMIBGroup.setObjects(
      *(("RUIJIE-QOS-MIB", "ruijieQoSGlobalStatus"),
        ("RUIJIE-QOS-MIB", "ruijiePriorityTrafficClassNum"),
        ("RUIJIE-QOS-MIB", "ruijiePriorityClassNum"),
        ("RUIJIE-QOS-MIB", "ruijiePriorityDscpMaxValue"),
        ("RUIJIE-QOS-MIB", "ruijieTrafficClassPriority"),
        ("RUIJIE-QOS-MIB", "ruijieTrafficClass"),
        ("RUIJIE-QOS-MIB", "ruijiePriorityToDscp"),
        ("RUIJIE-QOS-MIB", "ruijieDscpClass"),
        ("RUIJIE-QOS-MIB", "ruijieDscpTrafficClassPriority"),
        ("RUIJIE-QOS-MIB", "ruijiePriorityTrafficClassOperMode"),
        ("RUIJIE-QOS-MIB", "ruijiePriorityBandWidth"),
        ("RUIJIE-QOS-MIB", "ruijieIfPriorityIfIndex"),
        ("RUIJIE-QOS-MIB", "ruijieIfPriority"),
        ("RUIJIE-QOS-MIB", "ruijieIfPriTrafficClassOperMode"),
        ("RUIJIE-QOS-MIB", "ruijieIfPriorityBandwidth"),
        ("RUIJIE-QOS-MIB", "ruijieIfPriorityQosTrustMode"),
        ("RUIJIE-QOS-MIB", "ruijieIpPreClassPriority"),
        ("RUIJIE-QOS-MIB", "ruijieIpPreToDscp"))
)
if mibBuilder.loadTexts:
    ruijieQoSPriorityMIBGroup.setStatus("current")

ruijieQoSTrafficClassMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 3, 2, 2)
)
ruijieQoSTrafficClassMIBGroup.setObjects(
      *(("RUIJIE-QOS-MIB", "ruijieQosClassMapName"),
        ("RUIJIE-QOS-MIB", "ruijieQosClassAclName"),
        ("RUIJIE-QOS-MIB", "ruijieQosClassMapEntryStatus"),
        ("RUIJIE-QOS-MIB", "ruijieQosPoliceMapName"),
        ("RUIJIE-QOS-MIB", "ruijieQosPoliceMapEntryStatus"),
        ("RUIJIE-QOS-MIB", "ruijieQoSPoliceCfgPoliceMapName"),
        ("RUIJIE-QOS-MIB", "ruijieQoSPoliceCfgClassMapName"),
        ("RUIJIE-QOS-MIB", "ruijieQoSPoliceMapConfMaxBandWidth"),
        ("RUIJIE-QOS-MIB", "ruijieQoSPoliceMapConfExceedAction"),
        ("RUIJIE-QOS-MIB", "ruijieQoSPoliceMapConfExceedDscp"),
        ("RUIJIE-QOS-MIB", "ruijieQoSPoliceMapConfNewDscp"),
        ("RUIJIE-QOS-MIB", "ruijieQoSPoliceMapCfgEntryStatus"),
        ("RUIJIE-QOS-MIB", "ruijieQoSPoliceMapConfMaxHighBandWidth"),
        ("RUIJIE-QOS-MIB", "ruijieQosPoliceIfIndex"),
        ("RUIJIE-QOS-MIB", "ruijieIfInPoliceMapName"),
        ("RUIJIE-QOS-MIB", "ruijieIfOutPoliceMapName"))
)
if mibBuilder.loadTexts:
    ruijieQoSTrafficClassMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieQoSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 3, 1, 1)
)
ruijieQoSMIBCompliance.setObjects(
      *(("RUIJIE-QOS-MIB", "ruijieQoSPriorityMIBGroup"),
        ("RUIJIE-QOS-MIB", "ruijieQoSTrafficClassMIBGroup"))
)
if mibBuilder.loadTexts:
    ruijieQoSMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-QOS-MIB",
    **{"ruijieQoSMIB": ruijieQoSMIB,
       "ruijieQoSPriorityMIBObjects": ruijieQoSPriorityMIBObjects,
       "ruijieQoSGlobalStatus": ruijieQoSGlobalStatus,
       "ruijiePriorityTrafficClassNum": ruijiePriorityTrafficClassNum,
       "ruijiePriorityClassNum": ruijiePriorityClassNum,
       "ruijiePriorityDscpMaxValue": ruijiePriorityDscpMaxValue,
       "ruijieTrafficClassTable": ruijieTrafficClassTable,
       "ruijieTrafficClassEntry": ruijieTrafficClassEntry,
       "ruijieTrafficClassPriority": ruijieTrafficClassPriority,
       "ruijieTrafficClass": ruijieTrafficClass,
       "ruijiePriorityToDscp": ruijiePriorityToDscp,
       "ruijieDscpClassTable": ruijieDscpClassTable,
       "ruijieDscpClassEntry": ruijieDscpClassEntry,
       "ruijieDscpClass": ruijieDscpClass,
       "ruijieDscpTrafficClassPriority": ruijieDscpTrafficClassPriority,
       "ruijiePriorityTrafficClassOperMode": ruijiePriorityTrafficClassOperMode,
       "ruijiePriorityBandWidth": ruijiePriorityBandWidth,
       "ruijieIfPriorityTable": ruijieIfPriorityTable,
       "ruijieIfPriorityEntry": ruijieIfPriorityEntry,
       "ruijieIfPriorityIfIndex": ruijieIfPriorityIfIndex,
       "ruijieIfPriority": ruijieIfPriority,
       "ruijieIfPriTrafficClassOperMode": ruijieIfPriTrafficClassOperMode,
       "ruijieIfPriorityBandwidth": ruijieIfPriorityBandwidth,
       "ruijieIfPriorityQosTrustMode": ruijieIfPriorityQosTrustMode,
       "ruijieIpPreClassTable": ruijieIpPreClassTable,
       "ruijieIpPreClassEntry": ruijieIpPreClassEntry,
       "ruijieIpPreClassPriority": ruijieIpPreClassPriority,
       "ruijieIpPreToDscp": ruijieIpPreToDscp,
       "ruijieIfRateLimitTable": ruijieIfRateLimitTable,
       "ruijieIfRateLimitEntry": ruijieIfRateLimitEntry,
       "ruijieIfRateLimitIndex": ruijieIfRateLimitIndex,
       "ruijieIfRateLimitInMaxBandWidth": ruijieIfRateLimitInMaxBandWidth,
       "ruijieIfRateLimitInBurstFlowLimit": ruijieIfRateLimitInBurstFlowLimit,
       "ruijieIfRateLimitOutMaxBandWidth": ruijieIfRateLimitOutMaxBandWidth,
       "ruijieIfRateLimitOutBurstFlowLimit": ruijieIfRateLimitOutBurstFlowLimit,
       "ruijieIfQueueSupportTable": ruijieIfQueueSupportTable,
       "ruijieIfQueueSupportEntry": ruijieIfQueueSupportEntry,
       "ruijieIfIndex": ruijieIfIndex,
       "ruijieIfQueueIndex": ruijieIfQueueIndex,
       "ruijieIfQueueSupportTransmitPacket": ruijieIfQueueSupportTransmitPacket,
       "ruijieIfQueueSupportTransmitBytes": ruijieIfQueueSupportTransmitBytes,
       "ruijieIfQueueSupportDropPacket": ruijieIfQueueSupportDropPacket,
       "ruijieIfQueueSupportDropBytes": ruijieIfQueueSupportDropBytes,
       "ruijieIfQueueSupportTransmitPacketsRate": ruijieIfQueueSupportTransmitPacketsRate,
       "ruijieIfQueueSupportTransmitBitsRate": ruijieIfQueueSupportTransmitBitsRate,
       "ruijieIfQueueSupportPacketsLossRate": ruijieIfQueueSupportPacketsLossRate,
       "ruijieIfQueueSupportBytesLossRate": ruijieIfQueueSupportBytesLossRate,
       "ruijieIfQueueSupportDropPacketsRate": ruijieIfQueueSupportDropPacketsRate,
       "ruijieIfQueueSupportDropBitsRate": ruijieIfQueueSupportDropBitsRate,
       "ruijieIfQueueSupportQueueName": ruijieIfQueueSupportQueueName,
       "ruijieIfQueueSupportInQueuePackets": ruijieIfQueueSupportInQueuePackets,
       "ruijieIfQueueSupportInQueueBytes": ruijieIfQueueSupportInQueueBytes,
       "ruijieIfQueueSupportTailDropPackets": ruijieIfQueueSupportTailDropPackets,
       "ruijieIfQueueSupportTailDropBytes": ruijieIfQueueSupportTailDropBytes,
       "ruijieIfQueueSupportWredDropPackets": ruijieIfQueueSupportWredDropPackets,
       "ruijieIfQueueSupportWredDropBytes": ruijieIfQueueSupportWredDropBytes,
       "ruijieIfMulticastQueueSupportTable": ruijieIfMulticastQueueSupportTable,
       "ruijieIfMulticastQueueSupportEntry": ruijieIfMulticastQueueSupportEntry,
       "ruijieIfIndexMulticast": ruijieIfIndexMulticast,
       "ruijieIfMulticastQueueIndex": ruijieIfMulticastQueueIndex,
       "ruijieIfMulticastQueueSupportTransmitPacket": ruijieIfMulticastQueueSupportTransmitPacket,
       "ruijieIfMulticastQueueSupportTransmitBytes": ruijieIfMulticastQueueSupportTransmitBytes,
       "ruijieIfMulticastQueueSupportDropPacket": ruijieIfMulticastQueueSupportDropPacket,
       "ruijieIfMulticastQueueSupportDropBytes": ruijieIfMulticastQueueSupportDropBytes,
       "ruijieWredEcnStatsTable": ruijieWredEcnStatsTable,
       "ruijieWredEcnStatsEntry": ruijieWredEcnStatsEntry,
       "ruijieWredEcnStatsIfIndex": ruijieWredEcnStatsIfIndex,
       "ruijieWredDropped": ruijieWredDropped,
       "ruijieEcnSended": ruijieEcnSended,
       "ruijieQoSDsProTable": ruijieQoSDsProTable,
       "ruijieQoSDsProEntry": ruijieQoSDsProEntry,
       "ruijieQoSDsProIndex": ruijieQoSDsProIndex,
       "ruijieQoSDsProName": ruijieQoSDsProName,
       "ruijieQoSDsProInMapTable": ruijieQoSDsProInMapTable,
       "ruijieQoSDsProInMapEntry": ruijieQoSDsProInMapEntry,
       "ruijieQoSDsProInMapName": ruijieQoSDsProInMapName,
       "ruijieQoSDsProInMapType": ruijieQoSDsProInMapType,
       "ruijieQoSDsProInMapPri": ruijieQoSDsProInMapPri,
       "ruijieQoSDsProInMapCos": ruijieQoSDsProInMapCos,
       "ruijieQoSDsProInMapColor": ruijieQoSDsProInMapColor,
       "ruijieQoSDsProOutMapTable": ruijieQoSDsProOutMapTable,
       "ruijieQoSDsProOutMapEntry": ruijieQoSDsProOutMapEntry,
       "ruijieQoSDsProOutMapName": ruijieQoSDsProOutMapName,
       "ruijieQoSDsProOutMapType": ruijieQoSDsProOutMapType,
       "ruijieQoSDsProOutMapCos": ruijieQoSDsProOutMapCos,
       "ruijieQoSDsProOutMapColor": ruijieQoSDsProOutMapColor,
       "ruijieQoSDsProOutMapPri": ruijieQoSDsProOutMapPri,
       "ruijieQoSIfDirTable": ruijieQoSIfDirTable,
       "ruijieQoSIfDirEntry": ruijieQoSIfDirEntry,
       "ruijieQoSIfIndex": ruijieQoSIfIndex,
       "ruijieQoSIfDirIndex": ruijieQoSIfDirIndex,
       "ruijieQoSIfDirDsProName": ruijieQoSIfDirDsProName,
       "ruijieQoSIfStatisTable": ruijieQoSIfStatisTable,
       "ruijieQoSIfStatisEntry": ruijieQoSIfStatisEntry,
       "ruijieQoSIfStatisIndex": ruijieQoSIfStatisIndex,
       "ruijieQoSIfInBytes": ruijieQoSIfInBytes,
       "ruijieQoSIfInPkts": ruijieQoSIfInPkts,
       "ruijieQoSTrafficClassMIBObjects": ruijieQoSTrafficClassMIBObjects,
       "ruijieQoSTrafficClassTable": ruijieQoSTrafficClassTable,
       "ruijieQoSTrafficClassEntry": ruijieQoSTrafficClassEntry,
       "ruijieQosClassMapName": ruijieQosClassMapName,
       "ruijieQosClassAclName": ruijieQosClassAclName,
       "ruijieQosClassMapEntryStatus": ruijieQosClassMapEntryStatus,
       "ruijieQoSPoliceMapTable": ruijieQoSPoliceMapTable,
       "ruijieQoSPoliceMapEntry": ruijieQoSPoliceMapEntry,
       "ruijieQosPoliceMapName": ruijieQosPoliceMapName,
       "ruijieQosPoliceMapEntryStatus": ruijieQosPoliceMapEntryStatus,
       "ruijieQoSPoliceMapConfTable": ruijieQoSPoliceMapConfTable,
       "ruijieQoSPoliceMapConfEntry": ruijieQoSPoliceMapConfEntry,
       "ruijieQoSPoliceCfgPoliceMapName": ruijieQoSPoliceCfgPoliceMapName,
       "ruijieQoSPoliceCfgClassMapName": ruijieQoSPoliceCfgClassMapName,
       "ruijieQoSPoliceMapConfMaxBandWidth": ruijieQoSPoliceMapConfMaxBandWidth,
       "ruijieQoSPoliceMapConfBurstFlowLimit": ruijieQoSPoliceMapConfBurstFlowLimit,
       "ruijieQoSPoliceMapConfExceedAction": ruijieQoSPoliceMapConfExceedAction,
       "ruijieQoSPoliceMapConfExceedDscp": ruijieQoSPoliceMapConfExceedDscp,
       "ruijieQoSPoliceMapConfNewDscp": ruijieQoSPoliceMapConfNewDscp,
       "ruijieQoSPoliceMapCfgEntryStatus": ruijieQoSPoliceMapCfgEntryStatus,
       "ruijieQoSPoliceMapConfMaxHighBandWidth": ruijieQoSPoliceMapConfMaxHighBandWidth,
       "ruijieQosPoliceIfExtTable": ruijieQosPoliceIfExtTable,
       "ruijieQosPoliceIfExtEntry": ruijieQosPoliceIfExtEntry,
       "ruijieQosPoliceIfIndex": ruijieQosPoliceIfIndex,
       "ruijieIfInPoliceMapName": ruijieIfInPoliceMapName,
       "ruijieIfOutPoliceMapName": ruijieIfOutPoliceMapName,
       "ruijieQosPoliceStatisTable": ruijieQosPoliceStatisTable,
       "ruijieQosPoliceStatisEntry": ruijieQosPoliceStatisEntry,
       "ruijieQosPoliceStatisIfIndex": ruijieQosPoliceStatisIfIndex,
       "ruijieQosPoliceStatisDir": ruijieQosPoliceStatisDir,
       "ruijieQosPoliceStatisPmap": ruijieQosPoliceStatisPmap,
       "ruijieQosPoliceStatisCmap": ruijieQosPoliceStatisCmap,
       "ruijieQosPoliceStatisMatchPackets": ruijieQosPoliceStatisMatchPackets,
       "ruijieQosPoliceStatisMatchBytes": ruijieQosPoliceStatisMatchBytes,
       "ruijieQosPoliceStatisMissPackets": ruijieQosPoliceStatisMissPackets,
       "ruijieQosPoliceStatisMissBytes": ruijieQosPoliceStatisMissBytes,
       "ruijieQosPoliceStatisPassPackets": ruijieQosPoliceStatisPassPackets,
       "ruijieQosPoliceStatisPassBytes": ruijieQosPoliceStatisPassBytes,
       "ruijieQosPoliceStatisDropPackets": ruijieQosPoliceStatisDropPackets,
       "ruijieQosPoliceStatisDropBytes": ruijieQosPoliceStatisDropBytes,
       "ruijieQoSMIBConformance": ruijieQoSMIBConformance,
       "ruijieQoSMIBCompliances": ruijieQoSMIBCompliances,
       "ruijieQoSMIBCompliance": ruijieQoSMIBCompliance,
       "ruijieQoSMIBGroups": ruijieQoSMIBGroups,
       "ruijieQoSPriorityMIBGroup": ruijieQoSPriorityMIBGroup,
       "ruijieQoSTrafficClassMIBGroup": ruijieQoSTrafficClassMIBGroup}
)
