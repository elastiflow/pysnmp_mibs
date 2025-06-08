# SNMP MIB module (A3COM-HUAWEI-RPR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-RPR-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:03:45 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(rprTopoImageEntry,
 rprTopoImageInetAddress,
 rprTopoImageMacAddress) = mibBuilder.importSymbols(
    "IEEE-802DOT17-RPR-MIB",
    "rprTopoImageEntry",
    "rprTopoImageInetAddress",
    "rprTopoImageMacAddress")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

h3cRpr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60)
)
if mibBuilder.loadTexts:
    h3cRpr.setRevisions(
        ("2005-03-16 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cRprRingletID(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ringlet0", 1),
          ("ringlet1", 2))
    )



class H3cRprServiceClass(TextualConvention, Integer32):
    status = "current"
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
        *(("classC", 1),
          ("classB", 2),
          ("classA1", 3),
          ("classA0", 4))
    )



# MIB Managed Objects in the order of their OIDs

_H3cRprObjects_ObjectIdentity = ObjectIdentity
h3cRprObjects = _H3cRprObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1)
)
_H3cRprMaxmumDefine_ObjectIdentity = ObjectIdentity
h3cRprMaxmumDefine = _H3cRprMaxmumDefine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 1)
)
_H3cRprMaxmumDefineTable_Object = MibTable
h3cRprMaxmumDefineTable = _H3cRprMaxmumDefineTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cRprMaxmumDefineTable.setStatus("current")
_H3cRprMaxmumDefineEntry_Object = MibTableRow
h3cRprMaxmumDefineEntry = _H3cRprMaxmumDefineEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 1, 1, 1)
)
h3cRprMaxmumDefineEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprMaxMumIfIndex"),
)
if mibBuilder.loadTexts:
    h3cRprMaxmumDefineEntry.setStatus("current")
_H3cRprMaxMumIfIndex_Type = InterfaceIndex
_H3cRprMaxMumIfIndex_Object = MibTableColumn
h3cRprMaxMumIfIndex = _H3cRprMaxMumIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 1, 1, 1, 1),
    _H3cRprMaxMumIfIndex_Type()
)
h3cRprMaxMumIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprMaxMumIfIndex.setStatus("current")
_H3cRprMaxStationNumDefine_Type = Integer32
_H3cRprMaxStationNumDefine_Object = MibTableColumn
h3cRprMaxStationNumDefine = _H3cRprMaxStationNumDefine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 1, 1, 1, 2),
    _H3cRprMaxStationNumDefine_Type()
)
h3cRprMaxStationNumDefine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprMaxStationNumDefine.setStatus("current")
_H3cRprMaxReservedRateDefine_Type = Gauge32
_H3cRprMaxReservedRateDefine_Object = MibTableColumn
h3cRprMaxReservedRateDefine = _H3cRprMaxReservedRateDefine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 1, 1, 1, 3),
    _H3cRprMaxReservedRateDefine_Type()
)
h3cRprMaxReservedRateDefine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprMaxReservedRateDefine.setStatus("current")
_H3cRprTopoImage_ObjectIdentity = ObjectIdentity
h3cRprTopoImage = _H3cRprTopoImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 2)
)
_H3cRprTopoImageXTable_Object = MibTable
h3cRprTopoImageXTable = _H3cRprTopoImageXTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cRprTopoImageXTable.setStatus("current")
_H3cRprTopoImageXEntry_Object = MibTableRow
h3cRprTopoImageXEntry = _H3cRprTopoImageXEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h3cRprTopoImageXEntry.setStatus("current")
_H3cRprTopoImageXWestEdgeStatus_Type = TruthValue
_H3cRprTopoImageXWestEdgeStatus_Object = MibTableColumn
h3cRprTopoImageXWestEdgeStatus = _H3cRprTopoImageXWestEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 2, 1, 1, 3),
    _H3cRprTopoImageXWestEdgeStatus_Type()
)
h3cRprTopoImageXWestEdgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprTopoImageXWestEdgeStatus.setStatus("current")
_H3cRprTopoImageXEastEdgeStatus_Type = TruthValue
_H3cRprTopoImageXEastEdgeStatus_Object = MibTableColumn
h3cRprTopoImageXEastEdgeStatus = _H3cRprTopoImageXEastEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 2, 1, 1, 4),
    _H3cRprTopoImageXEastEdgeStatus_Type()
)
h3cRprTopoImageXEastEdgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprTopoImageXEastEdgeStatus.setStatus("current")
_H3cRprTopoImageXStationName_Type = SnmpAdminString
_H3cRprTopoImageXStationName_Object = MibTableColumn
h3cRprTopoImageXStationName = _H3cRprTopoImageXStationName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 2, 1, 1, 5),
    _H3cRprTopoImageXStationName_Type()
)
h3cRprTopoImageXStationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRprTopoImageXStationName.setStatus("current")
_H3cRprSpanCounters_ObjectIdentity = ObjectIdentity
h3cRprSpanCounters = _H3cRprSpanCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3)
)
_H3cRprSrcMacCountTable_Object = MibTable
h3cRprSrcMacCountTable = _H3cRprSrcMacCountTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 1)
)
if mibBuilder.loadTexts:
    h3cRprSrcMacCountTable.setStatus("current")
_H3cRprSrcMacCountEntry_Object = MibTableRow
h3cRprSrcMacCountEntry = _H3cRprSrcMacCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 1, 1)
)
h3cRprSrcMacCountEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprSrcMacCountIfIndex"),
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprSrcMacCountBySrcAddress"),
)
if mibBuilder.loadTexts:
    h3cRprSrcMacCountEntry.setStatus("current")
_H3cRprSrcMacCountIfIndex_Type = InterfaceIndex
_H3cRprSrcMacCountIfIndex_Object = MibTableColumn
h3cRprSrcMacCountIfIndex = _H3cRprSrcMacCountIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 1, 1, 1),
    _H3cRprSrcMacCountIfIndex_Type()
)
h3cRprSrcMacCountIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprSrcMacCountIfIndex.setStatus("current")
_H3cRprSrcMacCountBySrcAddress_Type = MacAddress
_H3cRprSrcMacCountBySrcAddress_Object = MibTableColumn
h3cRprSrcMacCountBySrcAddress = _H3cRprSrcMacCountBySrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 1, 1, 2),
    _H3cRprSrcMacCountBySrcAddress_Type()
)
h3cRprSrcMacCountBySrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprSrcMacCountBySrcAddress.setStatus("current")
_H3cRprSrcMacCountReceivedFrames_Type = Counter64
_H3cRprSrcMacCountReceivedFrames_Object = MibTableColumn
h3cRprSrcMacCountReceivedFrames = _H3cRprSrcMacCountReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 1, 1, 3),
    _H3cRprSrcMacCountReceivedFrames_Type()
)
h3cRprSrcMacCountReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprSrcMacCountReceivedFrames.setStatus("current")
_H3cRprSrcMacCountReceivedOctets_Type = Counter64
_H3cRprSrcMacCountReceivedOctets_Object = MibTableColumn
h3cRprSrcMacCountReceivedOctets = _H3cRprSrcMacCountReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 1, 1, 4),
    _H3cRprSrcMacCountReceivedOctets_Type()
)
h3cRprSrcMacCountReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprSrcMacCountReceivedOctets.setStatus("current")
_H3cRprDestMacCountTable_Object = MibTable
h3cRprDestMacCountTable = _H3cRprDestMacCountTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 2)
)
if mibBuilder.loadTexts:
    h3cRprDestMacCountTable.setStatus("current")
_H3cRprDestMacCountEntry_Object = MibTableRow
h3cRprDestMacCountEntry = _H3cRprDestMacCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 2, 1)
)
h3cRprDestMacCountEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprDestMacCountIfIndex"),
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprDestMacCountByDestAddress"),
)
if mibBuilder.loadTexts:
    h3cRprDestMacCountEntry.setStatus("current")
_H3cRprDestMacCountIfIndex_Type = InterfaceIndex
_H3cRprDestMacCountIfIndex_Object = MibTableColumn
h3cRprDestMacCountIfIndex = _H3cRprDestMacCountIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 2, 1, 1),
    _H3cRprDestMacCountIfIndex_Type()
)
h3cRprDestMacCountIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprDestMacCountIfIndex.setStatus("current")
_H3cRprDestMacCountByDestAddress_Type = MacAddress
_H3cRprDestMacCountByDestAddress_Object = MibTableColumn
h3cRprDestMacCountByDestAddress = _H3cRprDestMacCountByDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 2, 1, 2),
    _H3cRprDestMacCountByDestAddress_Type()
)
h3cRprDestMacCountByDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprDestMacCountByDestAddress.setStatus("current")
_H3cRprDestMacCountReceivedFrames_Type = Counter64
_H3cRprDestMacCountReceivedFrames_Object = MibTableColumn
h3cRprDestMacCountReceivedFrames = _H3cRprDestMacCountReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 2, 1, 3),
    _H3cRprDestMacCountReceivedFrames_Type()
)
h3cRprDestMacCountReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprDestMacCountReceivedFrames.setStatus("current")
_H3cRprDestMacCountReceivedOctets_Type = Counter64
_H3cRprDestMacCountReceivedOctets_Object = MibTableColumn
h3cRprDestMacCountReceivedOctets = _H3cRprDestMacCountReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 2, 1, 4),
    _H3cRprDestMacCountReceivedOctets_Type()
)
h3cRprDestMacCountReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprDestMacCountReceivedOctets.setStatus("current")
_H3cRprPktDropCountTable_Object = MibTable
h3cRprPktDropCountTable = _H3cRprPktDropCountTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 3)
)
if mibBuilder.loadTexts:
    h3cRprPktDropCountTable.setStatus("current")
_H3cRprPktDropCountEntry_Object = MibTableRow
h3cRprPktDropCountEntry = _H3cRprPktDropCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 3, 1)
)
h3cRprPktDropCountEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprPktDropCntIfIndex"),
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprPktDropCntRingletID"),
)
if mibBuilder.loadTexts:
    h3cRprPktDropCountEntry.setStatus("current")
_H3cRprPktDropCntIfIndex_Type = InterfaceIndex
_H3cRprPktDropCntIfIndex_Object = MibTableColumn
h3cRprPktDropCntIfIndex = _H3cRprPktDropCntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 3, 1, 1),
    _H3cRprPktDropCntIfIndex_Type()
)
h3cRprPktDropCntIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprPktDropCntIfIndex.setStatus("current")
_H3cRprPktDropCntRingletID_Type = H3cRprRingletID
_H3cRprPktDropCntRingletID_Object = MibTableColumn
h3cRprPktDropCntRingletID = _H3cRprPktDropCntRingletID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 3, 1, 2),
    _H3cRprPktDropCntRingletID_Type()
)
h3cRprPktDropCntRingletID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprPktDropCntRingletID.setStatus("current")
_H3cRprDownFlowClassAPktDrops_Type = Counter64
_H3cRprDownFlowClassAPktDrops_Object = MibTableColumn
h3cRprDownFlowClassAPktDrops = _H3cRprDownFlowClassAPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 3, 1, 3),
    _H3cRprDownFlowClassAPktDrops_Type()
)
h3cRprDownFlowClassAPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprDownFlowClassAPktDrops.setStatus("current")
_H3cRprUpFlowClassAPktDrops_Type = Counter64
_H3cRprUpFlowClassAPktDrops_Object = MibTableColumn
h3cRprUpFlowClassAPktDrops = _H3cRprUpFlowClassAPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 3, 1, 4),
    _H3cRprUpFlowClassAPktDrops_Type()
)
h3cRprUpFlowClassAPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprUpFlowClassAPktDrops.setStatus("current")
_H3cRprDownFlowClassBPktDrops_Type = Counter64
_H3cRprDownFlowClassBPktDrops_Object = MibTableColumn
h3cRprDownFlowClassBPktDrops = _H3cRprDownFlowClassBPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 3, 1, 5),
    _H3cRprDownFlowClassBPktDrops_Type()
)
h3cRprDownFlowClassBPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprDownFlowClassBPktDrops.setStatus("current")
_H3cRprUpFlowClassBPktDrops_Type = Counter64
_H3cRprUpFlowClassBPktDrops_Object = MibTableColumn
h3cRprUpFlowClassBPktDrops = _H3cRprUpFlowClassBPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 3, 1, 6),
    _H3cRprUpFlowClassBPktDrops_Type()
)
h3cRprUpFlowClassBPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprUpFlowClassBPktDrops.setStatus("current")
_H3cRprDownFlowClassCPktDrops_Type = Counter64
_H3cRprDownFlowClassCPktDrops_Object = MibTableColumn
h3cRprDownFlowClassCPktDrops = _H3cRprDownFlowClassCPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 3, 1, 7),
    _H3cRprDownFlowClassCPktDrops_Type()
)
h3cRprDownFlowClassCPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprDownFlowClassCPktDrops.setStatus("current")
_H3cRprUpFlowClassCPktDrops_Type = Counter64
_H3cRprUpFlowClassCPktDrops_Object = MibTableColumn
h3cRprUpFlowClassCPktDrops = _H3cRprUpFlowClassCPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 3, 3, 1, 8),
    _H3cRprUpFlowClassCPktDrops_Type()
)
h3cRprUpFlowClassCPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprUpFlowClassCPktDrops.setStatus("current")
_H3cRprRS_ObjectIdentity = ObjectIdentity
h3cRprRS = _H3cRprRS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4)
)
_H3cRprStaticRSTable_Object = MibTable
h3cRprStaticRSTable = _H3cRprStaticRSTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 1)
)
if mibBuilder.loadTexts:
    h3cRprStaticRSTable.setStatus("current")
_H3cRprStaticRSEntry_Object = MibTableRow
h3cRprStaticRSEntry = _H3cRprStaticRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 1, 1)
)
h3cRprStaticRSEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprStaticRSIfIndex"),
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprStaticRSMacAddress"),
)
if mibBuilder.loadTexts:
    h3cRprStaticRSEntry.setStatus("current")
_H3cRprStaticRSIfIndex_Type = InterfaceIndex
_H3cRprStaticRSIfIndex_Object = MibTableColumn
h3cRprStaticRSIfIndex = _H3cRprStaticRSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 1, 1, 1),
    _H3cRprStaticRSIfIndex_Type()
)
h3cRprStaticRSIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprStaticRSIfIndex.setStatus("current")
_H3cRprStaticRSMacAddress_Type = MacAddress
_H3cRprStaticRSMacAddress_Object = MibTableColumn
h3cRprStaticRSMacAddress = _H3cRprStaticRSMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 1, 1, 2),
    _H3cRprStaticRSMacAddress_Type()
)
h3cRprStaticRSMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprStaticRSMacAddress.setStatus("current")
_H3cRprStaticRSRingletID_Type = H3cRprRingletID
_H3cRprStaticRSRingletID_Object = MibTableColumn
h3cRprStaticRSRingletID = _H3cRprStaticRSRingletID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 1, 1, 3),
    _H3cRprStaticRSRingletID_Type()
)
h3cRprStaticRSRingletID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRprStaticRSRingletID.setStatus("current")
_H3cRprStaticRSTtl_Type = Integer32
_H3cRprStaticRSTtl_Object = MibTableColumn
h3cRprStaticRSTtl = _H3cRprStaticRSTtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 1, 1, 4),
    _H3cRprStaticRSTtl_Type()
)
h3cRprStaticRSTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprStaticRSTtl.setStatus("current")
_H3cRprStaticRSValid_Type = TruthValue
_H3cRprStaticRSValid_Object = MibTableColumn
h3cRprStaticRSValid = _H3cRprStaticRSValid_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 1, 1, 5),
    _H3cRprStaticRSValid_Type()
)
h3cRprStaticRSValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprStaticRSValid.setStatus("current")
_H3cRprStaticRSRowStatus_Type = RowStatus
_H3cRprStaticRSRowStatus_Object = MibTableColumn
h3cRprStaticRSRowStatus = _H3cRprStaticRSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 1, 1, 6),
    _H3cRprStaticRSRowStatus_Type()
)
h3cRprStaticRSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRprStaticRSRowStatus.setStatus("current")
_H3cRprIpv4DynamicRSTable_Object = MibTable
h3cRprIpv4DynamicRSTable = _H3cRprIpv4DynamicRSTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 2)
)
if mibBuilder.loadTexts:
    h3cRprIpv4DynamicRSTable.setStatus("current")
_H3cRprIpv4DynamicRSEntry_Object = MibTableRow
h3cRprIpv4DynamicRSEntry = _H3cRprIpv4DynamicRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 2, 1)
)
h3cRprIpv4DynamicRSEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprIpv4DynamicRSIfIndex"),
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprIpv4DynamicRSMacAddress"),
)
if mibBuilder.loadTexts:
    h3cRprIpv4DynamicRSEntry.setStatus("current")
_H3cRprIpv4DynamicRSIfIndex_Type = InterfaceIndex
_H3cRprIpv4DynamicRSIfIndex_Object = MibTableColumn
h3cRprIpv4DynamicRSIfIndex = _H3cRprIpv4DynamicRSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 2, 1, 1),
    _H3cRprIpv4DynamicRSIfIndex_Type()
)
h3cRprIpv4DynamicRSIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprIpv4DynamicRSIfIndex.setStatus("current")
_H3cRprIpv4DynamicRSMacAddress_Type = MacAddress
_H3cRprIpv4DynamicRSMacAddress_Object = MibTableColumn
h3cRprIpv4DynamicRSMacAddress = _H3cRprIpv4DynamicRSMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 2, 1, 2),
    _H3cRprIpv4DynamicRSMacAddress_Type()
)
h3cRprIpv4DynamicRSMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprIpv4DynamicRSMacAddress.setStatus("current")
_H3cRprIpv4DynamicRSRingletID_Type = H3cRprRingletID
_H3cRprIpv4DynamicRSRingletID_Object = MibTableColumn
h3cRprIpv4DynamicRSRingletID = _H3cRprIpv4DynamicRSRingletID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 2, 1, 3),
    _H3cRprIpv4DynamicRSRingletID_Type()
)
h3cRprIpv4DynamicRSRingletID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprIpv4DynamicRSRingletID.setStatus("current")
_H3cRprIpv4DynamicRSTtl_Type = Integer32
_H3cRprIpv4DynamicRSTtl_Object = MibTableColumn
h3cRprIpv4DynamicRSTtl = _H3cRprIpv4DynamicRSTtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 2, 1, 4),
    _H3cRprIpv4DynamicRSTtl_Type()
)
h3cRprIpv4DynamicRSTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprIpv4DynamicRSTtl.setStatus("current")
_H3cRprIpv6DynamicRSTable_Object = MibTable
h3cRprIpv6DynamicRSTable = _H3cRprIpv6DynamicRSTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 3)
)
if mibBuilder.loadTexts:
    h3cRprIpv6DynamicRSTable.setStatus("current")
_H3cRprIpv6DynamicRSEntry_Object = MibTableRow
h3cRprIpv6DynamicRSEntry = _H3cRprIpv6DynamicRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 3, 1)
)
h3cRprIpv6DynamicRSEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprIpv6DynamicRSIfIndex"),
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprIpv6DynamicRSMacAddress"),
)
if mibBuilder.loadTexts:
    h3cRprIpv6DynamicRSEntry.setStatus("current")
_H3cRprIpv6DynamicRSIfIndex_Type = InterfaceIndex
_H3cRprIpv6DynamicRSIfIndex_Object = MibTableColumn
h3cRprIpv6DynamicRSIfIndex = _H3cRprIpv6DynamicRSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 3, 1, 1),
    _H3cRprIpv6DynamicRSIfIndex_Type()
)
h3cRprIpv6DynamicRSIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprIpv6DynamicRSIfIndex.setStatus("current")
_H3cRprIpv6DynamicRSMacAddress_Type = MacAddress
_H3cRprIpv6DynamicRSMacAddress_Object = MibTableColumn
h3cRprIpv6DynamicRSMacAddress = _H3cRprIpv6DynamicRSMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 3, 1, 2),
    _H3cRprIpv6DynamicRSMacAddress_Type()
)
h3cRprIpv6DynamicRSMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprIpv6DynamicRSMacAddress.setStatus("current")
_H3cRprIpv6DynamicRSRingletID_Type = H3cRprRingletID
_H3cRprIpv6DynamicRSRingletID_Object = MibTableColumn
h3cRprIpv6DynamicRSRingletID = _H3cRprIpv6DynamicRSRingletID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 3, 1, 3),
    _H3cRprIpv6DynamicRSRingletID_Type()
)
h3cRprIpv6DynamicRSRingletID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprIpv6DynamicRSRingletID.setStatus("current")
_H3cRprIpv6DynamicRSTtl_Type = Integer32
_H3cRprIpv6DynamicRSTtl_Object = MibTableColumn
h3cRprIpv6DynamicRSTtl = _H3cRprIpv6DynamicRSTtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 3, 1, 4),
    _H3cRprIpv6DynamicRSTtl_Type()
)
h3cRprIpv6DynamicRSTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprIpv6DynamicRSTtl.setStatus("current")
_H3cRprIpv4OverallRSTable_Object = MibTable
h3cRprIpv4OverallRSTable = _H3cRprIpv4OverallRSTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 4)
)
if mibBuilder.loadTexts:
    h3cRprIpv4OverallRSTable.setStatus("current")
_H3cRprIpv4OverallRSEntry_Object = MibTableRow
h3cRprIpv4OverallRSEntry = _H3cRprIpv4OverallRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 4, 1)
)
h3cRprIpv4OverallRSEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprIpv4OverallRSIfIndex"),
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprIpv4OverallRSMacAddress"),
)
if mibBuilder.loadTexts:
    h3cRprIpv4OverallRSEntry.setStatus("current")
_H3cRprIpv4OverallRSIfIndex_Type = InterfaceIndex
_H3cRprIpv4OverallRSIfIndex_Object = MibTableColumn
h3cRprIpv4OverallRSIfIndex = _H3cRprIpv4OverallRSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 4, 1, 1),
    _H3cRprIpv4OverallRSIfIndex_Type()
)
h3cRprIpv4OverallRSIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprIpv4OverallRSIfIndex.setStatus("current")
_H3cRprIpv4OverallRSMacAddress_Type = MacAddress
_H3cRprIpv4OverallRSMacAddress_Object = MibTableColumn
h3cRprIpv4OverallRSMacAddress = _H3cRprIpv4OverallRSMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 4, 1, 2),
    _H3cRprIpv4OverallRSMacAddress_Type()
)
h3cRprIpv4OverallRSMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprIpv4OverallRSMacAddress.setStatus("current")


class _H3cRprIpv4OverallRSType_Type(Integer32):
    """Custom type h3cRprIpv4OverallRSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_H3cRprIpv4OverallRSType_Type.__name__ = "Integer32"
_H3cRprIpv4OverallRSType_Object = MibTableColumn
h3cRprIpv4OverallRSType = _H3cRprIpv4OverallRSType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 4, 1, 3),
    _H3cRprIpv4OverallRSType_Type()
)
h3cRprIpv4OverallRSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprIpv4OverallRSType.setStatus("current")
_H3cRprIpv4OverallRSRingletID_Type = H3cRprRingletID
_H3cRprIpv4OverallRSRingletID_Object = MibTableColumn
h3cRprIpv4OverallRSRingletID = _H3cRprIpv4OverallRSRingletID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 4, 1, 4),
    _H3cRprIpv4OverallRSRingletID_Type()
)
h3cRprIpv4OverallRSRingletID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprIpv4OverallRSRingletID.setStatus("current")
_H3cRprIpv4OverallRSTtl_Type = Integer32
_H3cRprIpv4OverallRSTtl_Object = MibTableColumn
h3cRprIpv4OverallRSTtl = _H3cRprIpv4OverallRSTtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 4, 1, 5),
    _H3cRprIpv4OverallRSTtl_Type()
)
h3cRprIpv4OverallRSTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprIpv4OverallRSTtl.setStatus("current")
_H3cRprVrrpRSTable_Object = MibTable
h3cRprVrrpRSTable = _H3cRprVrrpRSTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 5)
)
if mibBuilder.loadTexts:
    h3cRprVrrpRSTable.setStatus("current")
_H3cRprVrrpRSEntry_Object = MibTableRow
h3cRprVrrpRSEntry = _H3cRprVrrpRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 5, 1)
)
h3cRprVrrpRSEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprVrrpRSIfIndex"),
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprVrrpRSVirtualMacAddress"),
)
if mibBuilder.loadTexts:
    h3cRprVrrpRSEntry.setStatus("current")
_H3cRprVrrpRSIfIndex_Type = InterfaceIndex
_H3cRprVrrpRSIfIndex_Object = MibTableColumn
h3cRprVrrpRSIfIndex = _H3cRprVrrpRSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 5, 1, 1),
    _H3cRprVrrpRSIfIndex_Type()
)
h3cRprVrrpRSIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprVrrpRSIfIndex.setStatus("current")
_H3cRprVrrpRSVirtualMacAddress_Type = MacAddress
_H3cRprVrrpRSVirtualMacAddress_Object = MibTableColumn
h3cRprVrrpRSVirtualMacAddress = _H3cRprVrrpRSVirtualMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 5, 1, 2),
    _H3cRprVrrpRSVirtualMacAddress_Type()
)
h3cRprVrrpRSVirtualMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprVrrpRSVirtualMacAddress.setStatus("current")
_H3cRprVrrpRSMacAddress_Type = MacAddress
_H3cRprVrrpRSMacAddress_Object = MibTableColumn
h3cRprVrrpRSMacAddress = _H3cRprVrrpRSMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 5, 1, 3),
    _H3cRprVrrpRSMacAddress_Type()
)
h3cRprVrrpRSMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprVrrpRSMacAddress.setStatus("current")
_H3cRprVrrpRSRingletID_Type = H3cRprRingletID
_H3cRprVrrpRSRingletID_Object = MibTableColumn
h3cRprVrrpRSRingletID = _H3cRprVrrpRSRingletID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 5, 1, 4),
    _H3cRprVrrpRSRingletID_Type()
)
h3cRprVrrpRSRingletID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprVrrpRSRingletID.setStatus("current")
_H3cRprVrrpRSTtl_Type = Integer32
_H3cRprVrrpRSTtl_Object = MibTableColumn
h3cRprVrrpRSTtl = _H3cRprVrrpRSTtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 5, 1, 5),
    _H3cRprVrrpRSTtl_Type()
)
h3cRprVrrpRSTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprVrrpRSTtl.setStatus("current")
_H3cRprDefaultRingIDTable_Object = MibTable
h3cRprDefaultRingIDTable = _H3cRprDefaultRingIDTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 6)
)
if mibBuilder.loadTexts:
    h3cRprDefaultRingIDTable.setStatus("current")
_H3cRprDefaultRingIDEntry_Object = MibTableRow
h3cRprDefaultRingIDEntry = _H3cRprDefaultRingIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 6, 1)
)
h3cRprDefaultRingIDEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprDefaultRingIDIfIndex"),
)
if mibBuilder.loadTexts:
    h3cRprDefaultRingIDEntry.setStatus("current")
_H3cRprDefaultRingIDIfIndex_Type = InterfaceIndex
_H3cRprDefaultRingIDIfIndex_Object = MibTableColumn
h3cRprDefaultRingIDIfIndex = _H3cRprDefaultRingIDIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 6, 1, 1),
    _H3cRprDefaultRingIDIfIndex_Type()
)
h3cRprDefaultRingIDIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprDefaultRingIDIfIndex.setStatus("current")
_H3cRprDefaultConfigRingletID_Type = H3cRprRingletID
_H3cRprDefaultConfigRingletID_Object = MibTableColumn
h3cRprDefaultConfigRingletID = _H3cRprDefaultConfigRingletID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 6, 1, 2),
    _H3cRprDefaultConfigRingletID_Type()
)
h3cRprDefaultConfigRingletID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRprDefaultConfigRingletID.setStatus("current")
_H3cRprDefaultActiveRingID_Type = H3cRprRingletID
_H3cRprDefaultActiveRingID_Object = MibTableColumn
h3cRprDefaultActiveRingID = _H3cRprDefaultActiveRingID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 4, 6, 1, 3),
    _H3cRprDefaultActiveRingID_Type()
)
h3cRprDefaultActiveRingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprDefaultActiveRingID.setStatus("current")
_H3cRprDefect_ObjectIdentity = ObjectIdentity
h3cRprDefect = _H3cRprDefect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 5)
)
_H3cRprDefectReportTable_Object = MibTable
h3cRprDefectReportTable = _H3cRprDefectReportTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 5, 1)
)
if mibBuilder.loadTexts:
    h3cRprDefectReportTable.setStatus("current")
_H3cRprDefectReportEntry_Object = MibTableRow
h3cRprDefectReportEntry = _H3cRprDefectReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 5, 1, 1)
)
h3cRprDefectReportEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprDefectIfIndex"),
)
if mibBuilder.loadTexts:
    h3cRprDefectReportEntry.setStatus("current")
_H3cRprDefectIfIndex_Type = InterfaceIndex
_H3cRprDefectIfIndex_Object = MibTableColumn
h3cRprDefectIfIndex = _H3cRprDefectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 5, 1, 1, 1),
    _H3cRprDefectIfIndex_Type()
)
h3cRprDefectIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprDefectIfIndex.setStatus("current")


class _H3cRprDefectCurrentStatus_Type(Bits):
    """Custom type h3cRprDefectCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("topologyOpenRing", 0),
          ("topoInstability", 1),
          ("topoInconsistent", 2),
          ("dulpMacAddress", 3),
          ("dulpIPAddress", 4),
          ("lrttDefect", 5),
          ("protCfgDefect", 6),
          ("jumboCfgDefect", 7),
          ("excessReservedRateDefect", 8),
          ("excessMaxStationNum", 9),
          ("miscabling", 10),
          ("backPressure", 11))
    )

_H3cRprDefectCurrentStatus_Type.__name__ = "Bits"
_H3cRprDefectCurrentStatus_Object = MibTableColumn
h3cRprDefectCurrentStatus = _H3cRprDefectCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 5, 1, 1, 2),
    _H3cRprDefectCurrentStatus_Type()
)
h3cRprDefectCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprDefectCurrentStatus.setStatus("current")
_H3cRprPriorityMap_ObjectIdentity = ObjectIdentity
h3cRprPriorityMap = _H3cRprPriorityMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 6)
)
_H3cRprPriority2ClassMapTable_Object = MibTable
h3cRprPriority2ClassMapTable = _H3cRprPriority2ClassMapTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 6, 1)
)
if mibBuilder.loadTexts:
    h3cRprPriority2ClassMapTable.setStatus("current")
_H3cRprPriority2ClassMapEntry_Object = MibTableRow
h3cRprPriority2ClassMapEntry = _H3cRprPriority2ClassMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 6, 1, 1)
)
h3cRprPriority2ClassMapEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprPriority2ClassMapIfIndex"),
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprPriority2ClassMapType"),
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprPriorityValue"),
)
if mibBuilder.loadTexts:
    h3cRprPriority2ClassMapEntry.setStatus("current")
_H3cRprPriority2ClassMapIfIndex_Type = InterfaceIndex
_H3cRprPriority2ClassMapIfIndex_Object = MibTableColumn
h3cRprPriority2ClassMapIfIndex = _H3cRprPriority2ClassMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 6, 1, 1, 1),
    _H3cRprPriority2ClassMapIfIndex_Type()
)
h3cRprPriority2ClassMapIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprPriority2ClassMapIfIndex.setStatus("current")


class _H3cRprPriority2ClassMapType_Type(Integer32):
    """Custom type h3cRprPriority2ClassMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tag", 1),
          ("mpls", 2),
          ("ip", 3))
    )


_H3cRprPriority2ClassMapType_Type.__name__ = "Integer32"
_H3cRprPriority2ClassMapType_Object = MibTableColumn
h3cRprPriority2ClassMapType = _H3cRprPriority2ClassMapType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 6, 1, 1, 2),
    _H3cRprPriority2ClassMapType_Type()
)
h3cRprPriority2ClassMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprPriority2ClassMapType.setStatus("current")


class _H3cRprPriorityValue_Type(Integer32):
    """Custom type h3cRprPriorityValue based on Integer32"""
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
        *(("pri0", 1),
          ("pri1", 2),
          ("pri2", 3),
          ("pri3", 4),
          ("pri4", 5),
          ("pri5", 6),
          ("pri6", 7),
          ("pri7", 8))
    )


_H3cRprPriorityValue_Type.__name__ = "Integer32"
_H3cRprPriorityValue_Object = MibTableColumn
h3cRprPriorityValue = _H3cRprPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 6, 1, 1, 3),
    _H3cRprPriorityValue_Type()
)
h3cRprPriorityValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprPriorityValue.setStatus("current")
_H3cRprPriority2ClassMap_Type = H3cRprServiceClass
_H3cRprPriority2ClassMap_Object = MibTableColumn
h3cRprPriority2ClassMap = _H3cRprPriority2ClassMap_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 6, 1, 1, 4),
    _H3cRprPriority2ClassMap_Type()
)
h3cRprPriority2ClassMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRprPriority2ClassMap.setStatus("current")
_H3cRprRateLimitConfig_ObjectIdentity = ObjectIdentity
h3cRprRateLimitConfig = _H3cRprRateLimitConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 7)
)
_H3cRprRateLimitConfigTable_Object = MibTable
h3cRprRateLimitConfigTable = _H3cRprRateLimitConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 7, 1)
)
if mibBuilder.loadTexts:
    h3cRprRateLimitConfigTable.setStatus("current")
_H3cRprRateLimitConfigEntry_Object = MibTableRow
h3cRprRateLimitConfigEntry = _H3cRprRateLimitConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 7, 1, 1)
)
h3cRprRateLimitConfigEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprRateLimitConfigIfIndex"),
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprRateLimitConfigRingletId"),
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprRateLimitConfigServiceClass"),
)
if mibBuilder.loadTexts:
    h3cRprRateLimitConfigEntry.setStatus("current")
_H3cRprRateLimitConfigIfIndex_Type = InterfaceIndex
_H3cRprRateLimitConfigIfIndex_Object = MibTableColumn
h3cRprRateLimitConfigIfIndex = _H3cRprRateLimitConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 7, 1, 1, 1),
    _H3cRprRateLimitConfigIfIndex_Type()
)
h3cRprRateLimitConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprRateLimitConfigIfIndex.setStatus("current")
_H3cRprRateLimitConfigRingletId_Type = H3cRprRingletID
_H3cRprRateLimitConfigRingletId_Object = MibTableColumn
h3cRprRateLimitConfigRingletId = _H3cRprRateLimitConfigRingletId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 7, 1, 1, 2),
    _H3cRprRateLimitConfigRingletId_Type()
)
h3cRprRateLimitConfigRingletId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprRateLimitConfigRingletId.setStatus("current")
_H3cRprRateLimitConfigServiceClass_Type = H3cRprServiceClass
_H3cRprRateLimitConfigServiceClass_Object = MibTableColumn
h3cRprRateLimitConfigServiceClass = _H3cRprRateLimitConfigServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 7, 1, 1, 3),
    _H3cRprRateLimitConfigServiceClass_Type()
)
h3cRprRateLimitConfigServiceClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprRateLimitConfigServiceClass.setStatus("current")
_H3cRprRateLimitConfigValue_Type = Integer32
_H3cRprRateLimitConfigValue_Object = MibTableColumn
h3cRprRateLimitConfigValue = _H3cRprRateLimitConfigValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 7, 1, 1, 4),
    _H3cRprRateLimitConfigValue_Type()
)
h3cRprRateLimitConfigValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRprRateLimitConfigValue.setStatus("current")
_H3cRprMacAddrLearn_ObjectIdentity = ObjectIdentity
h3cRprMacAddrLearn = _H3cRprMacAddrLearn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 8)
)
_H3cRprMacLearnCfgTable_Object = MibTable
h3cRprMacLearnCfgTable = _H3cRprMacLearnCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 8, 1)
)
if mibBuilder.loadTexts:
    h3cRprMacLearnCfgTable.setStatus("current")
_H3cRprMacLearnCfgEntry_Object = MibTableRow
h3cRprMacLearnCfgEntry = _H3cRprMacLearnCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 8, 1, 1)
)
h3cRprMacLearnCfgEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprMacLearnIfIndex"),
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprMacLearnRprMac"),
)
if mibBuilder.loadTexts:
    h3cRprMacLearnCfgEntry.setStatus("current")
_H3cRprMacLearnIfIndex_Type = InterfaceIndex
_H3cRprMacLearnIfIndex_Object = MibTableColumn
h3cRprMacLearnIfIndex = _H3cRprMacLearnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 8, 1, 1, 1),
    _H3cRprMacLearnIfIndex_Type()
)
h3cRprMacLearnIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprMacLearnIfIndex.setStatus("current")
_H3cRprMacLearnRprMac_Type = MacAddress
_H3cRprMacLearnRprMac_Object = MibTableColumn
h3cRprMacLearnRprMac = _H3cRprMacLearnRprMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 8, 1, 1, 2),
    _H3cRprMacLearnRprMac_Type()
)
h3cRprMacLearnRprMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRprMacLearnRprMac.setStatus("current")
_H3cRprMacLearnType_Type = Integer32
_H3cRprMacLearnType_Object = MibTableColumn
h3cRprMacLearnType = _H3cRprMacLearnType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 8, 1, 1, 3),
    _H3cRprMacLearnType_Type()
)
h3cRprMacLearnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRprMacLearnType.setStatus("current")
_H3cRprMacLearnDestMac_Type = MacAddress
_H3cRprMacLearnDestMac_Object = MibTableColumn
h3cRprMacLearnDestMac = _H3cRprMacLearnDestMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 8, 1, 1, 4),
    _H3cRprMacLearnDestMac_Type()
)
h3cRprMacLearnDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRprMacLearnDestMac.setStatus("current")


class _H3cRprMacLearnVlanId_Type(Integer32):
    """Custom type h3cRprMacLearnVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cRprMacLearnVlanId_Type.__name__ = "Integer32"
_H3cRprMacLearnVlanId_Object = MibTableColumn
h3cRprMacLearnVlanId = _H3cRprMacLearnVlanId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 8, 1, 1, 5),
    _H3cRprMacLearnVlanId_Type()
)
h3cRprMacLearnVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRprMacLearnVlanId.setStatus("current")
_H3cRprMacLearnRinglet_Type = H3cRprRingletID
_H3cRprMacLearnRinglet_Object = MibTableColumn
h3cRprMacLearnRinglet = _H3cRprMacLearnRinglet_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 8, 1, 1, 6),
    _H3cRprMacLearnRinglet_Type()
)
h3cRprMacLearnRinglet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRprMacLearnRinglet.setStatus("current")
_H3cRprMacLearnTtl_Type = Integer32
_H3cRprMacLearnTtl_Object = MibTableColumn
h3cRprMacLearnTtl = _H3cRprMacLearnTtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 8, 1, 1, 7),
    _H3cRprMacLearnTtl_Type()
)
h3cRprMacLearnTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprMacLearnTtl.setStatus("current")
_H3cRprMacLearnIsValid_Type = TruthValue
_H3cRprMacLearnIsValid_Object = MibTableColumn
h3cRprMacLearnIsValid = _H3cRprMacLearnIsValid_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 8, 1, 1, 8),
    _H3cRprMacLearnIsValid_Type()
)
h3cRprMacLearnIsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRprMacLearnIsValid.setStatus("current")
_H3cRprMacLearnRowStatus_Type = RowStatus
_H3cRprMacLearnRowStatus_Object = MibTableColumn
h3cRprMacLearnRowStatus = _H3cRprMacLearnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 8, 1, 1, 9),
    _H3cRprMacLearnRowStatus_Type()
)
h3cRprMacLearnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRprMacLearnRowStatus.setStatus("current")
_H3cRprTrapVar_ObjectIdentity = ObjectIdentity
h3cRprTrapVar = _H3cRprTrapVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 9)
)
_H3cRprTrapVarTable_Object = MibTable
h3cRprTrapVarTable = _H3cRprTrapVarTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 9, 1)
)
if mibBuilder.loadTexts:
    h3cRprTrapVarTable.setStatus("current")
_H3cRprTrapVarEntry_Object = MibTableRow
h3cRprTrapVarEntry = _H3cRprTrapVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 9, 1, 1)
)
h3cRprTrapVarEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RPR-MIB", "h3cRprTrapIfIndex"),
)
if mibBuilder.loadTexts:
    h3cRprTrapVarEntry.setStatus("current")
_H3cRprTrapIfIndex_Type = InterfaceIndex
_H3cRprTrapIfIndex_Object = MibTableColumn
h3cRprTrapIfIndex = _H3cRprTrapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 9, 1, 1, 1),
    _H3cRprTrapIfIndex_Type()
)
h3cRprTrapIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cRprTrapIfIndex.setStatus("current")
_H3cRprTrapRinglet_Type = H3cRprRingletID
_H3cRprTrapRinglet_Object = MibTableColumn
h3cRprTrapRinglet = _H3cRprTrapRinglet_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 9, 1, 1, 2),
    _H3cRprTrapRinglet_Type()
)
h3cRprTrapRinglet.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cRprTrapRinglet.setStatus("current")
_H3cRprTrapTopoMacAddress_Type = MacAddress
_H3cRprTrapTopoMacAddress_Object = MibTableColumn
h3cRprTrapTopoMacAddress = _H3cRprTrapTopoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 9, 1, 1, 3),
    _H3cRprTrapTopoMacAddress_Type()
)
h3cRprTrapTopoMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cRprTrapTopoMacAddress.setStatus("current")
_H3cRprTrapIpAddress_Type = InetAddress
_H3cRprTrapIpAddress_Object = MibTableColumn
h3cRprTrapIpAddress = _H3cRprTrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 9, 1, 1, 4),
    _H3cRprTrapIpAddress_Type()
)
h3cRprTrapIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cRprTrapIpAddress.setStatus("current")
_H3cRprTrap_ObjectIdentity = ObjectIdentity
h3cRprTrap = _H3cRprTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 10)
)
rprTopoImageEntry.registerAugmentions(
    ("A3COM-HUAWEI-RPR-MIB",
     "h3cRprTopoImageXEntry")
)
h3cRprTopoImageXEntry.setIndexNames(*rprTopoImageEntry.getIndexNames())

# Managed Objects groups


# Notification objects

h3cRprTopologyOpenRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 10, 1)
)
h3cRprTopologyOpenRing.setObjects(
      *(("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapIfIndex"),
        ("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapRinglet"))
)
if mibBuilder.loadTexts:
    h3cRprTopologyOpenRing.setStatus(
        "current"
    )

h3cRprTopologyCloseRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 10, 2)
)
h3cRprTopologyCloseRing.setObjects(
      *(("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapIfIndex"),
        ("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapRinglet"))
)
if mibBuilder.loadTexts:
    h3cRprTopologyCloseRing.setStatus(
        "current"
    )

h3cRprTopologyInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 10, 3)
)
h3cRprTopologyInconsistent.setObjects(
    ("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapIfIndex")
)
if mibBuilder.loadTexts:
    h3cRprTopologyInconsistent.setStatus(
        "current"
    )

h3cRprTopologyInstability = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 10, 4)
)
h3cRprTopologyInstability.setObjects(
    ("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapIfIndex")
)
if mibBuilder.loadTexts:
    h3cRprTopologyInstability.setStatus(
        "current"
    )

h3cRprDuplicateMacAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 10, 5)
)
h3cRprDuplicateMacAddress.setObjects(
      *(("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapIfIndex"),
        ("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapTopoMacAddress"))
)
if mibBuilder.loadTexts:
    h3cRprDuplicateMacAddress.setStatus(
        "current"
    )

h3cRprDulplicateIPAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 10, 6)
)
h3cRprDulplicateIPAddress.setObjects(
      *(("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapIfIndex"),
        ("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapIpAddress"))
)
if mibBuilder.loadTexts:
    h3cRprDulplicateIPAddress.setStatus(
        "current"
    )

h3cRprIncompleteLRTT = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 10, 7)
)
h3cRprIncompleteLRTT.setObjects(
    ("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapIfIndex")
)
if mibBuilder.loadTexts:
    h3cRprIncompleteLRTT.setStatus(
        "current"
    )

h3cRprProtecConfigInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 10, 8)
)
h3cRprProtecConfigInconsistent.setObjects(
    ("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapIfIndex")
)
if mibBuilder.loadTexts:
    h3cRprProtecConfigInconsistent.setStatus(
        "current"
    )

h3cRprJumboConfigInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 10, 9)
)
h3cRprJumboConfigInconsistent.setObjects(
    ("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapIfIndex")
)
if mibBuilder.loadTexts:
    h3cRprJumboConfigInconsistent.setStatus(
        "current"
    )

h3cRprExceedMaxReservRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 10, 10)
)
h3cRprExceedMaxReservRate.setObjects(
      *(("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapIfIndex"),
        ("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapRinglet"))
)
if mibBuilder.loadTexts:
    h3cRprExceedMaxReservRate.setStatus(
        "current"
    )

h3cRprExceedMaxStationNum = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 10, 11)
)
h3cRprExceedMaxStationNum.setObjects(
    ("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapIfIndex")
)
if mibBuilder.loadTexts:
    h3cRprExceedMaxStationNum.setStatus(
        "current"
    )

h3cRprMiscabling = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 10, 12)
)
h3cRprMiscabling.setObjects(
      *(("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapIfIndex"),
        ("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapRinglet"))
)
if mibBuilder.loadTexts:
    h3cRprMiscabling.setStatus(
        "current"
    )

h3cRprBackPressure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 10, 13)
)
h3cRprBackPressure.setObjects(
      *(("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapIfIndex"),
        ("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapRinglet"),
        ("A3COM-HUAWEI-RPR-MIB", "h3cRprPriority2ClassMap"))
)
if mibBuilder.loadTexts:
    h3cRprBackPressure.setStatus(
        "current"
    )

h3cRprBackPressureOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 60, 1, 10, 14)
)
h3cRprBackPressureOver.setObjects(
      *(("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapIfIndex"),
        ("A3COM-HUAWEI-RPR-MIB", "h3cRprTrapRinglet"),
        ("A3COM-HUAWEI-RPR-MIB", "h3cRprPriority2ClassMap"))
)
if mibBuilder.loadTexts:
    h3cRprBackPressureOver.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-RPR-MIB",
    **{"H3cRprRingletID": H3cRprRingletID,
       "H3cRprServiceClass": H3cRprServiceClass,
       "h3cRpr": h3cRpr,
       "h3cRprObjects": h3cRprObjects,
       "h3cRprMaxmumDefine": h3cRprMaxmumDefine,
       "h3cRprMaxmumDefineTable": h3cRprMaxmumDefineTable,
       "h3cRprMaxmumDefineEntry": h3cRprMaxmumDefineEntry,
       "h3cRprMaxMumIfIndex": h3cRprMaxMumIfIndex,
       "h3cRprMaxStationNumDefine": h3cRprMaxStationNumDefine,
       "h3cRprMaxReservedRateDefine": h3cRprMaxReservedRateDefine,
       "h3cRprTopoImage": h3cRprTopoImage,
       "h3cRprTopoImageXTable": h3cRprTopoImageXTable,
       "h3cRprTopoImageXEntry": h3cRprTopoImageXEntry,
       "h3cRprTopoImageXWestEdgeStatus": h3cRprTopoImageXWestEdgeStatus,
       "h3cRprTopoImageXEastEdgeStatus": h3cRprTopoImageXEastEdgeStatus,
       "h3cRprTopoImageXStationName": h3cRprTopoImageXStationName,
       "h3cRprSpanCounters": h3cRprSpanCounters,
       "h3cRprSrcMacCountTable": h3cRprSrcMacCountTable,
       "h3cRprSrcMacCountEntry": h3cRprSrcMacCountEntry,
       "h3cRprSrcMacCountIfIndex": h3cRprSrcMacCountIfIndex,
       "h3cRprSrcMacCountBySrcAddress": h3cRprSrcMacCountBySrcAddress,
       "h3cRprSrcMacCountReceivedFrames": h3cRprSrcMacCountReceivedFrames,
       "h3cRprSrcMacCountReceivedOctets": h3cRprSrcMacCountReceivedOctets,
       "h3cRprDestMacCountTable": h3cRprDestMacCountTable,
       "h3cRprDestMacCountEntry": h3cRprDestMacCountEntry,
       "h3cRprDestMacCountIfIndex": h3cRprDestMacCountIfIndex,
       "h3cRprDestMacCountByDestAddress": h3cRprDestMacCountByDestAddress,
       "h3cRprDestMacCountReceivedFrames": h3cRprDestMacCountReceivedFrames,
       "h3cRprDestMacCountReceivedOctets": h3cRprDestMacCountReceivedOctets,
       "h3cRprPktDropCountTable": h3cRprPktDropCountTable,
       "h3cRprPktDropCountEntry": h3cRprPktDropCountEntry,
       "h3cRprPktDropCntIfIndex": h3cRprPktDropCntIfIndex,
       "h3cRprPktDropCntRingletID": h3cRprPktDropCntRingletID,
       "h3cRprDownFlowClassAPktDrops": h3cRprDownFlowClassAPktDrops,
       "h3cRprUpFlowClassAPktDrops": h3cRprUpFlowClassAPktDrops,
       "h3cRprDownFlowClassBPktDrops": h3cRprDownFlowClassBPktDrops,
       "h3cRprUpFlowClassBPktDrops": h3cRprUpFlowClassBPktDrops,
       "h3cRprDownFlowClassCPktDrops": h3cRprDownFlowClassCPktDrops,
       "h3cRprUpFlowClassCPktDrops": h3cRprUpFlowClassCPktDrops,
       "h3cRprRS": h3cRprRS,
       "h3cRprStaticRSTable": h3cRprStaticRSTable,
       "h3cRprStaticRSEntry": h3cRprStaticRSEntry,
       "h3cRprStaticRSIfIndex": h3cRprStaticRSIfIndex,
       "h3cRprStaticRSMacAddress": h3cRprStaticRSMacAddress,
       "h3cRprStaticRSRingletID": h3cRprStaticRSRingletID,
       "h3cRprStaticRSTtl": h3cRprStaticRSTtl,
       "h3cRprStaticRSValid": h3cRprStaticRSValid,
       "h3cRprStaticRSRowStatus": h3cRprStaticRSRowStatus,
       "h3cRprIpv4DynamicRSTable": h3cRprIpv4DynamicRSTable,
       "h3cRprIpv4DynamicRSEntry": h3cRprIpv4DynamicRSEntry,
       "h3cRprIpv4DynamicRSIfIndex": h3cRprIpv4DynamicRSIfIndex,
       "h3cRprIpv4DynamicRSMacAddress": h3cRprIpv4DynamicRSMacAddress,
       "h3cRprIpv4DynamicRSRingletID": h3cRprIpv4DynamicRSRingletID,
       "h3cRprIpv4DynamicRSTtl": h3cRprIpv4DynamicRSTtl,
       "h3cRprIpv6DynamicRSTable": h3cRprIpv6DynamicRSTable,
       "h3cRprIpv6DynamicRSEntry": h3cRprIpv6DynamicRSEntry,
       "h3cRprIpv6DynamicRSIfIndex": h3cRprIpv6DynamicRSIfIndex,
       "h3cRprIpv6DynamicRSMacAddress": h3cRprIpv6DynamicRSMacAddress,
       "h3cRprIpv6DynamicRSRingletID": h3cRprIpv6DynamicRSRingletID,
       "h3cRprIpv6DynamicRSTtl": h3cRprIpv6DynamicRSTtl,
       "h3cRprIpv4OverallRSTable": h3cRprIpv4OverallRSTable,
       "h3cRprIpv4OverallRSEntry": h3cRprIpv4OverallRSEntry,
       "h3cRprIpv4OverallRSIfIndex": h3cRprIpv4OverallRSIfIndex,
       "h3cRprIpv4OverallRSMacAddress": h3cRprIpv4OverallRSMacAddress,
       "h3cRprIpv4OverallRSType": h3cRprIpv4OverallRSType,
       "h3cRprIpv4OverallRSRingletID": h3cRprIpv4OverallRSRingletID,
       "h3cRprIpv4OverallRSTtl": h3cRprIpv4OverallRSTtl,
       "h3cRprVrrpRSTable": h3cRprVrrpRSTable,
       "h3cRprVrrpRSEntry": h3cRprVrrpRSEntry,
       "h3cRprVrrpRSIfIndex": h3cRprVrrpRSIfIndex,
       "h3cRprVrrpRSVirtualMacAddress": h3cRprVrrpRSVirtualMacAddress,
       "h3cRprVrrpRSMacAddress": h3cRprVrrpRSMacAddress,
       "h3cRprVrrpRSRingletID": h3cRprVrrpRSRingletID,
       "h3cRprVrrpRSTtl": h3cRprVrrpRSTtl,
       "h3cRprDefaultRingIDTable": h3cRprDefaultRingIDTable,
       "h3cRprDefaultRingIDEntry": h3cRprDefaultRingIDEntry,
       "h3cRprDefaultRingIDIfIndex": h3cRprDefaultRingIDIfIndex,
       "h3cRprDefaultConfigRingletID": h3cRprDefaultConfigRingletID,
       "h3cRprDefaultActiveRingID": h3cRprDefaultActiveRingID,
       "h3cRprDefect": h3cRprDefect,
       "h3cRprDefectReportTable": h3cRprDefectReportTable,
       "h3cRprDefectReportEntry": h3cRprDefectReportEntry,
       "h3cRprDefectIfIndex": h3cRprDefectIfIndex,
       "h3cRprDefectCurrentStatus": h3cRprDefectCurrentStatus,
       "h3cRprPriorityMap": h3cRprPriorityMap,
       "h3cRprPriority2ClassMapTable": h3cRprPriority2ClassMapTable,
       "h3cRprPriority2ClassMapEntry": h3cRprPriority2ClassMapEntry,
       "h3cRprPriority2ClassMapIfIndex": h3cRprPriority2ClassMapIfIndex,
       "h3cRprPriority2ClassMapType": h3cRprPriority2ClassMapType,
       "h3cRprPriorityValue": h3cRprPriorityValue,
       "h3cRprPriority2ClassMap": h3cRprPriority2ClassMap,
       "h3cRprRateLimitConfig": h3cRprRateLimitConfig,
       "h3cRprRateLimitConfigTable": h3cRprRateLimitConfigTable,
       "h3cRprRateLimitConfigEntry": h3cRprRateLimitConfigEntry,
       "h3cRprRateLimitConfigIfIndex": h3cRprRateLimitConfigIfIndex,
       "h3cRprRateLimitConfigRingletId": h3cRprRateLimitConfigRingletId,
       "h3cRprRateLimitConfigServiceClass": h3cRprRateLimitConfigServiceClass,
       "h3cRprRateLimitConfigValue": h3cRprRateLimitConfigValue,
       "h3cRprMacAddrLearn": h3cRprMacAddrLearn,
       "h3cRprMacLearnCfgTable": h3cRprMacLearnCfgTable,
       "h3cRprMacLearnCfgEntry": h3cRprMacLearnCfgEntry,
       "h3cRprMacLearnIfIndex": h3cRprMacLearnIfIndex,
       "h3cRprMacLearnRprMac": h3cRprMacLearnRprMac,
       "h3cRprMacLearnType": h3cRprMacLearnType,
       "h3cRprMacLearnDestMac": h3cRprMacLearnDestMac,
       "h3cRprMacLearnVlanId": h3cRprMacLearnVlanId,
       "h3cRprMacLearnRinglet": h3cRprMacLearnRinglet,
       "h3cRprMacLearnTtl": h3cRprMacLearnTtl,
       "h3cRprMacLearnIsValid": h3cRprMacLearnIsValid,
       "h3cRprMacLearnRowStatus": h3cRprMacLearnRowStatus,
       "h3cRprTrapVar": h3cRprTrapVar,
       "h3cRprTrapVarTable": h3cRprTrapVarTable,
       "h3cRprTrapVarEntry": h3cRprTrapVarEntry,
       "h3cRprTrapIfIndex": h3cRprTrapIfIndex,
       "h3cRprTrapRinglet": h3cRprTrapRinglet,
       "h3cRprTrapTopoMacAddress": h3cRprTrapTopoMacAddress,
       "h3cRprTrapIpAddress": h3cRprTrapIpAddress,
       "h3cRprTrap": h3cRprTrap,
       "h3cRprTopologyOpenRing": h3cRprTopologyOpenRing,
       "h3cRprTopologyCloseRing": h3cRprTopologyCloseRing,
       "h3cRprTopologyInconsistent": h3cRprTopologyInconsistent,
       "h3cRprTopologyInstability": h3cRprTopologyInstability,
       "h3cRprDuplicateMacAddress": h3cRprDuplicateMacAddress,
       "h3cRprDulplicateIPAddress": h3cRprDulplicateIPAddress,
       "h3cRprIncompleteLRTT": h3cRprIncompleteLRTT,
       "h3cRprProtecConfigInconsistent": h3cRprProtecConfigInconsistent,
       "h3cRprJumboConfigInconsistent": h3cRprJumboConfigInconsistent,
       "h3cRprExceedMaxReservRate": h3cRprExceedMaxReservRate,
       "h3cRprExceedMaxStationNum": h3cRprExceedMaxStationNum,
       "h3cRprMiscabling": h3cRprMiscabling,
       "h3cRprBackPressure": h3cRprBackPressure,
       "h3cRprBackPressureOver": h3cRprBackPressureOver}
)
