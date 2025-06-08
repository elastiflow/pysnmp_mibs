# SNMP MIB module (ME1200-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-QOS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:31 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(ME1200EtherType,
 ME1200InterfaceIndex,
 ME1200Percent,
 ME1200PortList,
 ME1200RowEditorState,
 ME1200Unsigned16,
 ME1200Unsigned8) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200EtherType",
    "ME1200InterfaceIndex",
    "ME1200Percent",
    "ME1200PortList",
    "ME1200RowEditorState",
    "ME1200Unsigned16",
    "ME1200Unsigned8")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

me1200QosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14)
)
if mibBuilder.loadTexts:
    me1200QosMIB.setRevisions(
        ("2014-08-14 00:00",
         "2014-03-11 00:00",
         "2014-02-18 00:00",
         "2014-01-29 00:00",
         "2013-10-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200ASRType(TextualConvention, Integer32):
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
        *(("any", 0),
          ("specific", 1),
          ("range", 2))
    )



class ME1200BitType(TextualConvention, Integer32):
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
        *(("any", 0),
          ("zero", 1),
          ("one", 2))
    )



class ME1200DestMacType(TextualConvention, Integer32):
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
        *(("any", 0),
          ("unicast", 1),
          ("multicast", 2),
          ("broadcast", 3))
    )



class ME1200DscpClassify(TextualConvention, Integer32):
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
        *(("none", 0),
          ("zero", 1),
          ("selected", 2),
          ("all", 3))
    )



class ME1200DscpRemark(TextualConvention, Integer32):
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
        *(("disabled", 0),
          ("rewrite", 1),
          ("remap", 2),
          ("remapDp", 3))
    )



class ME1200MaxSelector(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("maximumDropProbability", 0),
          ("maximumFillLevel", 1))
    )



class ME1200QceFrameType(TextualConvention, Integer32):
    status = "current"
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
        *(("any", 0),
          ("etype", 1),
          ("llc", 2),
          ("snap", 3),
          ("ipv4", 4),
          ("ipv6", 5))
    )



class ME1200QceUserType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("admin", 0),
          ("voiceVlan", 1))
    )



class ME1200TagRemarkingMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("classified", 0),
          ("default", 2),
          ("mapped", 3))
    )



class ME1200VcapKeyType(TextualConvention, Integer32):
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
        *(("normal", 0),
          ("doubleTag", 1),
          ("ipAddr", 2),
          ("macIpAddr", 3))
    )



class ME1200VlanTagPriority(TextualConvention, Integer32):
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
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("value0", 1),
          ("value1", 2),
          ("value2", 3),
          ("value3", 4),
          ("value4", 5),
          ("value5", 6),
          ("value6", 7),
          ("value7", 8),
          ("range0to1", 9),
          ("range2to3", 10),
          ("range4to5", 11),
          ("range6to7", 12),
          ("range0to3", 13),
          ("range4to7", 14))
    )



class ME1200VlanTagType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("untagged", 1),
          ("tagged", 2),
          ("cTagged", 3),
          ("sTagged", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200QosMIBObjects_ObjectIdentity = ObjectIdentity
me1200QosMIBObjects = _Me1200QosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1)
)
_Me1200QosConfig_ObjectIdentity = ObjectIdentity
me1200QosConfig = _Me1200QosConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2)
)
_Me1200QosGlobals_ObjectIdentity = ObjectIdentity
me1200QosGlobals = _Me1200QosGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1)
)
_Me1200QosStormPolicers_ObjectIdentity = ObjectIdentity
me1200QosStormPolicers = _Me1200QosStormPolicers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 1)
)
_Me1200QosStormPolicerUnicast_ObjectIdentity = ObjectIdentity
me1200QosStormPolicerUnicast = _Me1200QosStormPolicerUnicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 1, 1)
)
_Me1200QosStormPolicerUnicastEnable_Type = TruthValue
_Me1200QosStormPolicerUnicastEnable_Object = MibScalar
me1200QosStormPolicerUnicastEnable = _Me1200QosStormPolicerUnicastEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 1, 1, 1),
    _Me1200QosStormPolicerUnicastEnable_Type()
)
me1200QosStormPolicerUnicastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosStormPolicerUnicastEnable.setStatus("current")
_Me1200QosStormPolicerUnicastRate_Type = Unsigned32
_Me1200QosStormPolicerUnicastRate_Object = MibScalar
me1200QosStormPolicerUnicastRate = _Me1200QosStormPolicerUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 1, 1, 2),
    _Me1200QosStormPolicerUnicastRate_Type()
)
me1200QosStormPolicerUnicastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosStormPolicerUnicastRate.setStatus("current")
_Me1200QosStormPolicerMulticast_ObjectIdentity = ObjectIdentity
me1200QosStormPolicerMulticast = _Me1200QosStormPolicerMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 1, 2)
)
_Me1200QosStormPolicerMulticastEnable_Type = TruthValue
_Me1200QosStormPolicerMulticastEnable_Object = MibScalar
me1200QosStormPolicerMulticastEnable = _Me1200QosStormPolicerMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 1, 2, 1),
    _Me1200QosStormPolicerMulticastEnable_Type()
)
me1200QosStormPolicerMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosStormPolicerMulticastEnable.setStatus("current")
_Me1200QosStormPolicerMulticastRate_Type = Unsigned32
_Me1200QosStormPolicerMulticastRate_Object = MibScalar
me1200QosStormPolicerMulticastRate = _Me1200QosStormPolicerMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 1, 2, 2),
    _Me1200QosStormPolicerMulticastRate_Type()
)
me1200QosStormPolicerMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosStormPolicerMulticastRate.setStatus("current")
_Me1200QosStormPolicerBroadcast_ObjectIdentity = ObjectIdentity
me1200QosStormPolicerBroadcast = _Me1200QosStormPolicerBroadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 1, 3)
)
_Me1200QosStormPolicerBroadcastEnable_Type = TruthValue
_Me1200QosStormPolicerBroadcastEnable_Object = MibScalar
me1200QosStormPolicerBroadcastEnable = _Me1200QosStormPolicerBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 1, 3, 1),
    _Me1200QosStormPolicerBroadcastEnable_Type()
)
me1200QosStormPolicerBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosStormPolicerBroadcastEnable.setStatus("current")
_Me1200QosStormPolicerBroadcastRate_Type = Unsigned32
_Me1200QosStormPolicerBroadcastRate_Object = MibScalar
me1200QosStormPolicerBroadcastRate = _Me1200QosStormPolicerBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 1, 3, 2),
    _Me1200QosStormPolicerBroadcastRate_Type()
)
me1200QosStormPolicerBroadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosStormPolicerBroadcastRate.setStatus("current")
_Me1200QosWredTable_Object = MibTable
me1200QosWredTable = _Me1200QosWredTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    me1200QosWredTable.setStatus("current")
_Me1200QosWredEntry_Object = MibTableRow
me1200QosWredEntry = _Me1200QosWredEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 2, 1)
)
me1200QosWredEntry.setIndexNames(
    (0, "ME1200-QOS-MIB", "me1200QosWredQueue"),
)
if mibBuilder.loadTexts:
    me1200QosWredEntry.setStatus("current")


class _Me1200QosWredQueue_Type(Integer32):
    """Custom type me1200QosWredQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Me1200QosWredQueue_Type.__name__ = "Integer32"
_Me1200QosWredQueue_Object = MibTableColumn
me1200QosWredQueue = _Me1200QosWredQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 2, 1, 1),
    _Me1200QosWredQueue_Type()
)
me1200QosWredQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosWredQueue.setStatus("current")
_Me1200QosWredEnable_Type = TruthValue
_Me1200QosWredEnable_Object = MibTableColumn
me1200QosWredEnable = _Me1200QosWredEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 2, 1, 2),
    _Me1200QosWredEnable_Type()
)
me1200QosWredEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosWredEnable.setStatus("current")
_Me1200QosWredMinimumFillLevel_Type = ME1200Percent
_Me1200QosWredMinimumFillLevel_Object = MibTableColumn
me1200QosWredMinimumFillLevel = _Me1200QosWredMinimumFillLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 2, 1, 3),
    _Me1200QosWredMinimumFillLevel_Type()
)
me1200QosWredMinimumFillLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosWredMinimumFillLevel.setStatus("current")
_Me1200QosWredMaximum_Type = ME1200Percent
_Me1200QosWredMaximum_Object = MibTableColumn
me1200QosWredMaximum = _Me1200QosWredMaximum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 2, 1, 4),
    _Me1200QosWredMaximum_Type()
)
me1200QosWredMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosWredMaximum.setStatus("current")
_Me1200QosWredMaxSelector_Type = ME1200MaxSelector
_Me1200QosWredMaxSelector_Object = MibTableColumn
me1200QosWredMaxSelector = _Me1200QosWredMaxSelector_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 2, 1, 5),
    _Me1200QosWredMaxSelector_Type()
)
me1200QosWredMaxSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosWredMaxSelector.setStatus("current")
_Me1200QosDscpTable_Object = MibTable
me1200QosDscpTable = _Me1200QosDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    me1200QosDscpTable.setStatus("current")
_Me1200QosDscpEntry_Object = MibTableRow
me1200QosDscpEntry = _Me1200QosDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 3, 1)
)
me1200QosDscpEntry.setIndexNames(
    (0, "ME1200-QOS-MIB", "me1200QosDscpDscp"),
)
if mibBuilder.loadTexts:
    me1200QosDscpEntry.setStatus("current")
_Me1200QosDscpDscp_Type = Dscp
_Me1200QosDscpDscp_Object = MibTableColumn
me1200QosDscpDscp = _Me1200QosDscpDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 3, 1, 1),
    _Me1200QosDscpDscp_Type()
)
me1200QosDscpDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosDscpDscp.setStatus("current")
_Me1200QosDscpTrust_Type = TruthValue
_Me1200QosDscpTrust_Object = MibTableColumn
me1200QosDscpTrust = _Me1200QosDscpTrust_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 3, 1, 2),
    _Me1200QosDscpTrust_Type()
)
me1200QosDscpTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosDscpTrust.setStatus("current")
_Me1200QosDscpCos_Type = Unsigned32
_Me1200QosDscpCos_Object = MibTableColumn
me1200QosDscpCos = _Me1200QosDscpCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 3, 1, 3),
    _Me1200QosDscpCos_Type()
)
me1200QosDscpCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosDscpCos.setStatus("current")
_Me1200QosDscpDpl_Type = ME1200Unsigned8
_Me1200QosDscpDpl_Object = MibTableColumn
me1200QosDscpDpl = _Me1200QosDscpDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 3, 1, 4),
    _Me1200QosDscpDpl_Type()
)
me1200QosDscpDpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosDscpDpl.setStatus("current")
_Me1200QosDscpIngressTranslation_Type = Dscp
_Me1200QosDscpIngressTranslation_Object = MibTableColumn
me1200QosDscpIngressTranslation = _Me1200QosDscpIngressTranslation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 3, 1, 5),
    _Me1200QosDscpIngressTranslation_Type()
)
me1200QosDscpIngressTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosDscpIngressTranslation.setStatus("current")
_Me1200QosDscpClassify_Type = TruthValue
_Me1200QosDscpClassify_Object = MibTableColumn
me1200QosDscpClassify = _Me1200QosDscpClassify_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 3, 1, 6),
    _Me1200QosDscpClassify_Type()
)
me1200QosDscpClassify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosDscpClassify.setStatus("current")
_Me1200QosDscpEgressTranslation_Type = Dscp
_Me1200QosDscpEgressTranslation_Object = MibTableColumn
me1200QosDscpEgressTranslation = _Me1200QosDscpEgressTranslation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 3, 1, 7),
    _Me1200QosDscpEgressTranslation_Type()
)
me1200QosDscpEgressTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosDscpEgressTranslation.setStatus("current")
_Me1200QosDscpEgressTranslationDp1_Type = Dscp
_Me1200QosDscpEgressTranslationDp1_Object = MibTableColumn
me1200QosDscpEgressTranslationDp1 = _Me1200QosDscpEgressTranslationDp1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 3, 1, 8),
    _Me1200QosDscpEgressTranslationDp1_Type()
)
me1200QosDscpEgressTranslationDp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosDscpEgressTranslationDp1.setStatus("current")
_Me1200QosCosToDscpTable_Object = MibTable
me1200QosCosToDscpTable = _Me1200QosCosToDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    me1200QosCosToDscpTable.setStatus("current")
_Me1200QosCosToDscpEntry_Object = MibTableRow
me1200QosCosToDscpEntry = _Me1200QosCosToDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 4, 1)
)
me1200QosCosToDscpEntry.setIndexNames(
    (0, "ME1200-QOS-MIB", "me1200QosCosToDscpCos"),
)
if mibBuilder.loadTexts:
    me1200QosCosToDscpEntry.setStatus("current")


class _Me1200QosCosToDscpCos_Type(Integer32):
    """Custom type me1200QosCosToDscpCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Me1200QosCosToDscpCos_Type.__name__ = "Integer32"
_Me1200QosCosToDscpCos_Object = MibTableColumn
me1200QosCosToDscpCos = _Me1200QosCosToDscpCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 4, 1, 1),
    _Me1200QosCosToDscpCos_Type()
)
me1200QosCosToDscpCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosCosToDscpCos.setStatus("current")
_Me1200QosCosToDscpDscp_Type = Dscp
_Me1200QosCosToDscpDscp_Object = MibTableColumn
me1200QosCosToDscpDscp = _Me1200QosCosToDscpDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 4, 1, 2),
    _Me1200QosCosToDscpDscp_Type()
)
me1200QosCosToDscpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosCosToDscpDscp.setStatus("current")
_Me1200QosCosToDscpDscpDp1_Type = Dscp
_Me1200QosCosToDscpDscpDp1_Object = MibTableColumn
me1200QosCosToDscpDscpDp1 = _Me1200QosCosToDscpDscpDp1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 4, 1, 3),
    _Me1200QosCosToDscpDscpDp1_Type()
)
me1200QosCosToDscpDscpDp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosCosToDscpDscpDp1.setStatus("current")
_Me1200QosQce_ObjectIdentity = ObjectIdentity
me1200QosQce = _Me1200QosQce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10)
)
_Me1200QosQceTable_Object = MibTable
me1200QosQceTable = _Me1200QosQceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    me1200QosQceTable.setStatus("current")
_Me1200QosQceEntry_Object = MibTableRow
me1200QosQceEntry = _Me1200QosQceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1)
)
me1200QosQceEntry.setIndexNames(
    (0, "ME1200-QOS-MIB", "me1200QosQceQceId"),
)
if mibBuilder.loadTexts:
    me1200QosQceEntry.setStatus("current")


class _Me1200QosQceQceId_Type(Integer32):
    """Custom type me1200QosQceQceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200QosQceQceId_Type.__name__ = "Integer32"
_Me1200QosQceQceId_Object = MibTableColumn
me1200QosQceQceId = _Me1200QosQceQceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 1),
    _Me1200QosQceQceId_Type()
)
me1200QosQceQceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosQceQceId.setStatus("current")
_Me1200QosQceNextQceId_Type = Unsigned32
_Me1200QosQceNextQceId_Object = MibTableColumn
me1200QosQceNextQceId = _Me1200QosQceNextQceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 2),
    _Me1200QosQceNextQceId_Type()
)
me1200QosQceNextQceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceNextQceId.setStatus("current")
_Me1200QosQcePortList_Type = ME1200PortList
_Me1200QosQcePortList_Object = MibTableColumn
me1200QosQcePortList = _Me1200QosQcePortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 4),
    _Me1200QosQcePortList_Type()
)
me1200QosQcePortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQcePortList.setStatus("current")
_Me1200QosQceDestMacType_Type = ME1200DestMacType
_Me1200QosQceDestMacType_Object = MibTableColumn
me1200QosQceDestMacType = _Me1200QosQceDestMacType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 5),
    _Me1200QosQceDestMacType_Type()
)
me1200QosQceDestMacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceDestMacType.setStatus("current")
_Me1200QosQceDestMac_Type = MacAddress
_Me1200QosQceDestMac_Object = MibTableColumn
me1200QosQceDestMac = _Me1200QosQceDestMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 6),
    _Me1200QosQceDestMac_Type()
)
me1200QosQceDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceDestMac.setStatus("current")
_Me1200QosQceDestMacMask_Type = MacAddress
_Me1200QosQceDestMacMask_Object = MibTableColumn
me1200QosQceDestMacMask = _Me1200QosQceDestMacMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 7),
    _Me1200QosQceDestMacMask_Type()
)
me1200QosQceDestMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceDestMacMask.setStatus("current")
_Me1200QosQceSrcMac_Type = MacAddress
_Me1200QosQceSrcMac_Object = MibTableColumn
me1200QosQceSrcMac = _Me1200QosQceSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 8),
    _Me1200QosQceSrcMac_Type()
)
me1200QosQceSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceSrcMac.setStatus("current")
_Me1200QosQceSrcMacMask_Type = MacAddress
_Me1200QosQceSrcMacMask_Object = MibTableColumn
me1200QosQceSrcMacMask = _Me1200QosQceSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 9),
    _Me1200QosQceSrcMacMask_Type()
)
me1200QosQceSrcMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceSrcMacMask.setStatus("current")
_Me1200QosQceVlanTagType_Type = ME1200VlanTagType
_Me1200QosQceVlanTagType_Object = MibTableColumn
me1200QosQceVlanTagType = _Me1200QosQceVlanTagType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 10),
    _Me1200QosQceVlanTagType_Type()
)
me1200QosQceVlanTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceVlanTagType.setStatus("current")
_Me1200QosQceVlanIdOp_Type = ME1200ASRType
_Me1200QosQceVlanIdOp_Object = MibTableColumn
me1200QosQceVlanIdOp = _Me1200QosQceVlanIdOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 11),
    _Me1200QosQceVlanIdOp_Type()
)
me1200QosQceVlanIdOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceVlanIdOp.setStatus("current")
_Me1200QosQceVlanId_Type = ME1200Unsigned16
_Me1200QosQceVlanId_Object = MibTableColumn
me1200QosQceVlanId = _Me1200QosQceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 12),
    _Me1200QosQceVlanId_Type()
)
me1200QosQceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceVlanId.setStatus("current")
_Me1200QosQceVlanIdRange_Type = ME1200Unsigned16
_Me1200QosQceVlanIdRange_Object = MibTableColumn
me1200QosQceVlanIdRange = _Me1200QosQceVlanIdRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 13),
    _Me1200QosQceVlanIdRange_Type()
)
me1200QosQceVlanIdRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceVlanIdRange.setStatus("current")
_Me1200QosQcePcp_Type = ME1200VlanTagPriority
_Me1200QosQcePcp_Object = MibTableColumn
me1200QosQcePcp = _Me1200QosQcePcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 14),
    _Me1200QosQcePcp_Type()
)
me1200QosQcePcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQcePcp.setStatus("current")
_Me1200QosQceDei_Type = ME1200BitType
_Me1200QosQceDei_Object = MibTableColumn
me1200QosQceDei = _Me1200QosQceDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 15),
    _Me1200QosQceDei_Type()
)
me1200QosQceDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceDei.setStatus("current")
_Me1200QosQceInnerVlanTagType_Type = ME1200VlanTagType
_Me1200QosQceInnerVlanTagType_Object = MibTableColumn
me1200QosQceInnerVlanTagType = _Me1200QosQceInnerVlanTagType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 16),
    _Me1200QosQceInnerVlanTagType_Type()
)
me1200QosQceInnerVlanTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceInnerVlanTagType.setStatus("current")
_Me1200QosQceInnerVlanIdOp_Type = ME1200ASRType
_Me1200QosQceInnerVlanIdOp_Object = MibTableColumn
me1200QosQceInnerVlanIdOp = _Me1200QosQceInnerVlanIdOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 17),
    _Me1200QosQceInnerVlanIdOp_Type()
)
me1200QosQceInnerVlanIdOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceInnerVlanIdOp.setStatus("current")
_Me1200QosQceInnerVlanId_Type = ME1200Unsigned16
_Me1200QosQceInnerVlanId_Object = MibTableColumn
me1200QosQceInnerVlanId = _Me1200QosQceInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 18),
    _Me1200QosQceInnerVlanId_Type()
)
me1200QosQceInnerVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceInnerVlanId.setStatus("current")
_Me1200QosQceInnerVlanIdRange_Type = ME1200Unsigned16
_Me1200QosQceInnerVlanIdRange_Object = MibTableColumn
me1200QosQceInnerVlanIdRange = _Me1200QosQceInnerVlanIdRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 19),
    _Me1200QosQceInnerVlanIdRange_Type()
)
me1200QosQceInnerVlanIdRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceInnerVlanIdRange.setStatus("current")
_Me1200QosQceInnerPcp_Type = ME1200VlanTagPriority
_Me1200QosQceInnerPcp_Object = MibTableColumn
me1200QosQceInnerPcp = _Me1200QosQceInnerPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 20),
    _Me1200QosQceInnerPcp_Type()
)
me1200QosQceInnerPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceInnerPcp.setStatus("current")
_Me1200QosQceInnerDei_Type = ME1200BitType
_Me1200QosQceInnerDei_Object = MibTableColumn
me1200QosQceInnerDei = _Me1200QosQceInnerDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 21),
    _Me1200QosQceInnerDei_Type()
)
me1200QosQceInnerDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceInnerDei.setStatus("current")
_Me1200QosQceFrameType_Type = ME1200QceFrameType
_Me1200QosQceFrameType_Object = MibTableColumn
me1200QosQceFrameType = _Me1200QosQceFrameType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 100),
    _Me1200QosQceFrameType_Type()
)
me1200QosQceFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceFrameType.setStatus("current")
_Me1200QosQceEtype_Type = ME1200EtherType
_Me1200QosQceEtype_Object = MibTableColumn
me1200QosQceEtype = _Me1200QosQceEtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 101),
    _Me1200QosQceEtype_Type()
)
me1200QosQceEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceEtype.setStatus("current")
_Me1200QosQceLlcDsap_Type = ME1200Unsigned8
_Me1200QosQceLlcDsap_Object = MibTableColumn
me1200QosQceLlcDsap = _Me1200QosQceLlcDsap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 200),
    _Me1200QosQceLlcDsap_Type()
)
me1200QosQceLlcDsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceLlcDsap.setStatus("current")
_Me1200QosQceLlcDsapMask_Type = ME1200Unsigned8
_Me1200QosQceLlcDsapMask_Object = MibTableColumn
me1200QosQceLlcDsapMask = _Me1200QosQceLlcDsapMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 201),
    _Me1200QosQceLlcDsapMask_Type()
)
me1200QosQceLlcDsapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceLlcDsapMask.setStatus("current")
_Me1200QosQceLlcSsap_Type = ME1200Unsigned8
_Me1200QosQceLlcSsap_Object = MibTableColumn
me1200QosQceLlcSsap = _Me1200QosQceLlcSsap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 202),
    _Me1200QosQceLlcSsap_Type()
)
me1200QosQceLlcSsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceLlcSsap.setStatus("current")
_Me1200QosQceLlcSsapMask_Type = ME1200Unsigned8
_Me1200QosQceLlcSsapMask_Object = MibTableColumn
me1200QosQceLlcSsapMask = _Me1200QosQceLlcSsapMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 203),
    _Me1200QosQceLlcSsapMask_Type()
)
me1200QosQceLlcSsapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceLlcSsapMask.setStatus("current")
_Me1200QosQceLlcControl_Type = ME1200Unsigned8
_Me1200QosQceLlcControl_Object = MibTableColumn
me1200QosQceLlcControl = _Me1200QosQceLlcControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 204),
    _Me1200QosQceLlcControl_Type()
)
me1200QosQceLlcControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceLlcControl.setStatus("current")
_Me1200QosQceLlcControlMask_Type = ME1200Unsigned8
_Me1200QosQceLlcControlMask_Object = MibTableColumn
me1200QosQceLlcControlMask = _Me1200QosQceLlcControlMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 205),
    _Me1200QosQceLlcControlMask_Type()
)
me1200QosQceLlcControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceLlcControlMask.setStatus("current")
_Me1200QosQceSnapPid_Type = ME1200Unsigned16
_Me1200QosQceSnapPid_Object = MibTableColumn
me1200QosQceSnapPid = _Me1200QosQceSnapPid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 302),
    _Me1200QosQceSnapPid_Type()
)
me1200QosQceSnapPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceSnapPid.setStatus("current")
_Me1200QosQceSnapPidMask_Type = ME1200Unsigned16
_Me1200QosQceSnapPidMask_Object = MibTableColumn
me1200QosQceSnapPidMask = _Me1200QosQceSnapPidMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 303),
    _Me1200QosQceSnapPidMask_Type()
)
me1200QosQceSnapPidMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceSnapPidMask.setStatus("current")
_Me1200QosQceIpv4Fragment_Type = ME1200BitType
_Me1200QosQceIpv4Fragment_Object = MibTableColumn
me1200QosQceIpv4Fragment = _Me1200QosQceIpv4Fragment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 400),
    _Me1200QosQceIpv4Fragment_Type()
)
me1200QosQceIpv4Fragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv4Fragment.setStatus("current")
_Me1200QosQceIpv4DscpOp_Type = ME1200ASRType
_Me1200QosQceIpv4DscpOp_Object = MibTableColumn
me1200QosQceIpv4DscpOp = _Me1200QosQceIpv4DscpOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 401),
    _Me1200QosQceIpv4DscpOp_Type()
)
me1200QosQceIpv4DscpOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv4DscpOp.setStatus("current")
_Me1200QosQceIpv4Dscp_Type = ME1200Unsigned16
_Me1200QosQceIpv4Dscp_Object = MibTableColumn
me1200QosQceIpv4Dscp = _Me1200QosQceIpv4Dscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 402),
    _Me1200QosQceIpv4Dscp_Type()
)
me1200QosQceIpv4Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv4Dscp.setStatus("current")
_Me1200QosQceIpv4DscpRange_Type = ME1200Unsigned16
_Me1200QosQceIpv4DscpRange_Object = MibTableColumn
me1200QosQceIpv4DscpRange = _Me1200QosQceIpv4DscpRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 403),
    _Me1200QosQceIpv4DscpRange_Type()
)
me1200QosQceIpv4DscpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv4DscpRange.setStatus("current")
_Me1200QosQceIpv4Protocol_Type = ME1200Unsigned8
_Me1200QosQceIpv4Protocol_Object = MibTableColumn
me1200QosQceIpv4Protocol = _Me1200QosQceIpv4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 404),
    _Me1200QosQceIpv4Protocol_Type()
)
me1200QosQceIpv4Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv4Protocol.setStatus("current")
_Me1200QosQceIpv4ProtocolMask_Type = ME1200Unsigned8
_Me1200QosQceIpv4ProtocolMask_Object = MibTableColumn
me1200QosQceIpv4ProtocolMask = _Me1200QosQceIpv4ProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 405),
    _Me1200QosQceIpv4ProtocolMask_Type()
)
me1200QosQceIpv4ProtocolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv4ProtocolMask.setStatus("current")
_Me1200QosQceIpv4SrcIp_Type = IpAddress
_Me1200QosQceIpv4SrcIp_Object = MibTableColumn
me1200QosQceIpv4SrcIp = _Me1200QosQceIpv4SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 406),
    _Me1200QosQceIpv4SrcIp_Type()
)
me1200QosQceIpv4SrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv4SrcIp.setStatus("current")
_Me1200QosQceIpv4SrcIpMask_Type = IpAddress
_Me1200QosQceIpv4SrcIpMask_Object = MibTableColumn
me1200QosQceIpv4SrcIpMask = _Me1200QosQceIpv4SrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 407),
    _Me1200QosQceIpv4SrcIpMask_Type()
)
me1200QosQceIpv4SrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv4SrcIpMask.setStatus("current")
_Me1200QosQceIpv4DestIp_Type = IpAddress
_Me1200QosQceIpv4DestIp_Object = MibTableColumn
me1200QosQceIpv4DestIp = _Me1200QosQceIpv4DestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 408),
    _Me1200QosQceIpv4DestIp_Type()
)
me1200QosQceIpv4DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv4DestIp.setStatus("current")
_Me1200QosQceIpv4DestIpMask_Type = IpAddress
_Me1200QosQceIpv4DestIpMask_Object = MibTableColumn
me1200QosQceIpv4DestIpMask = _Me1200QosQceIpv4DestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 409),
    _Me1200QosQceIpv4DestIpMask_Type()
)
me1200QosQceIpv4DestIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv4DestIpMask.setStatus("current")
_Me1200QosQceIpv4SrcPortOp_Type = ME1200ASRType
_Me1200QosQceIpv4SrcPortOp_Object = MibTableColumn
me1200QosQceIpv4SrcPortOp = _Me1200QosQceIpv4SrcPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 410),
    _Me1200QosQceIpv4SrcPortOp_Type()
)
me1200QosQceIpv4SrcPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv4SrcPortOp.setStatus("current")
_Me1200QosQceIpv4SrcPort_Type = ME1200Unsigned16
_Me1200QosQceIpv4SrcPort_Object = MibTableColumn
me1200QosQceIpv4SrcPort = _Me1200QosQceIpv4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 411),
    _Me1200QosQceIpv4SrcPort_Type()
)
me1200QosQceIpv4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv4SrcPort.setStatus("current")
_Me1200QosQceIpv4SrcPortRange_Type = ME1200Unsigned16
_Me1200QosQceIpv4SrcPortRange_Object = MibTableColumn
me1200QosQceIpv4SrcPortRange = _Me1200QosQceIpv4SrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 412),
    _Me1200QosQceIpv4SrcPortRange_Type()
)
me1200QosQceIpv4SrcPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv4SrcPortRange.setStatus("current")
_Me1200QosQceIpv4DestPortOp_Type = ME1200ASRType
_Me1200QosQceIpv4DestPortOp_Object = MibTableColumn
me1200QosQceIpv4DestPortOp = _Me1200QosQceIpv4DestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 413),
    _Me1200QosQceIpv4DestPortOp_Type()
)
me1200QosQceIpv4DestPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv4DestPortOp.setStatus("current")
_Me1200QosQceIpv4DestPort_Type = ME1200Unsigned16
_Me1200QosQceIpv4DestPort_Object = MibTableColumn
me1200QosQceIpv4DestPort = _Me1200QosQceIpv4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 414),
    _Me1200QosQceIpv4DestPort_Type()
)
me1200QosQceIpv4DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv4DestPort.setStatus("current")
_Me1200QosQceIpv4DestPortRange_Type = ME1200Unsigned16
_Me1200QosQceIpv4DestPortRange_Object = MibTableColumn
me1200QosQceIpv4DestPortRange = _Me1200QosQceIpv4DestPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 415),
    _Me1200QosQceIpv4DestPortRange_Type()
)
me1200QosQceIpv4DestPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv4DestPortRange.setStatus("current")
_Me1200QosQceIpv6DscpOp_Type = ME1200ASRType
_Me1200QosQceIpv6DscpOp_Object = MibTableColumn
me1200QosQceIpv6DscpOp = _Me1200QosQceIpv6DscpOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 500),
    _Me1200QosQceIpv6DscpOp_Type()
)
me1200QosQceIpv6DscpOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv6DscpOp.setStatus("current")
_Me1200QosQceIpv6Dscp_Type = ME1200Unsigned16
_Me1200QosQceIpv6Dscp_Object = MibTableColumn
me1200QosQceIpv6Dscp = _Me1200QosQceIpv6Dscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 501),
    _Me1200QosQceIpv6Dscp_Type()
)
me1200QosQceIpv6Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv6Dscp.setStatus("current")
_Me1200QosQceIpv6DscpRange_Type = ME1200Unsigned16
_Me1200QosQceIpv6DscpRange_Object = MibTableColumn
me1200QosQceIpv6DscpRange = _Me1200QosQceIpv6DscpRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 502),
    _Me1200QosQceIpv6DscpRange_Type()
)
me1200QosQceIpv6DscpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv6DscpRange.setStatus("current")
_Me1200QosQceIpv6Protocol_Type = ME1200Unsigned8
_Me1200QosQceIpv6Protocol_Object = MibTableColumn
me1200QosQceIpv6Protocol = _Me1200QosQceIpv6Protocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 503),
    _Me1200QosQceIpv6Protocol_Type()
)
me1200QosQceIpv6Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv6Protocol.setStatus("current")
_Me1200QosQceIpv6ProtocolMask_Type = ME1200Unsigned8
_Me1200QosQceIpv6ProtocolMask_Object = MibTableColumn
me1200QosQceIpv6ProtocolMask = _Me1200QosQceIpv6ProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 504),
    _Me1200QosQceIpv6ProtocolMask_Type()
)
me1200QosQceIpv6ProtocolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv6ProtocolMask.setStatus("current")
_Me1200QosQceIpv6SrcIp_Type = InetAddressIPv6
_Me1200QosQceIpv6SrcIp_Object = MibTableColumn
me1200QosQceIpv6SrcIp = _Me1200QosQceIpv6SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 506),
    _Me1200QosQceIpv6SrcIp_Type()
)
me1200QosQceIpv6SrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv6SrcIp.setStatus("current")
_Me1200QosQceIpv6SrcIpMask_Type = InetAddressIPv6
_Me1200QosQceIpv6SrcIpMask_Object = MibTableColumn
me1200QosQceIpv6SrcIpMask = _Me1200QosQceIpv6SrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 508),
    _Me1200QosQceIpv6SrcIpMask_Type()
)
me1200QosQceIpv6SrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv6SrcIpMask.setStatus("current")
_Me1200QosQceIpv6DestIp_Type = InetAddressIPv6
_Me1200QosQceIpv6DestIp_Object = MibTableColumn
me1200QosQceIpv6DestIp = _Me1200QosQceIpv6DestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 510),
    _Me1200QosQceIpv6DestIp_Type()
)
me1200QosQceIpv6DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv6DestIp.setStatus("current")
_Me1200QosQceIpv6DestIpMask_Type = InetAddressIPv6
_Me1200QosQceIpv6DestIpMask_Object = MibTableColumn
me1200QosQceIpv6DestIpMask = _Me1200QosQceIpv6DestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 512),
    _Me1200QosQceIpv6DestIpMask_Type()
)
me1200QosQceIpv6DestIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv6DestIpMask.setStatus("current")
_Me1200QosQceIpv6SrcPortOp_Type = ME1200ASRType
_Me1200QosQceIpv6SrcPortOp_Object = MibTableColumn
me1200QosQceIpv6SrcPortOp = _Me1200QosQceIpv6SrcPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 513),
    _Me1200QosQceIpv6SrcPortOp_Type()
)
me1200QosQceIpv6SrcPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv6SrcPortOp.setStatus("current")
_Me1200QosQceIpv6SrcPort_Type = ME1200Unsigned16
_Me1200QosQceIpv6SrcPort_Object = MibTableColumn
me1200QosQceIpv6SrcPort = _Me1200QosQceIpv6SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 514),
    _Me1200QosQceIpv6SrcPort_Type()
)
me1200QosQceIpv6SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv6SrcPort.setStatus("current")
_Me1200QosQceIpv6SrcPortRange_Type = ME1200Unsigned16
_Me1200QosQceIpv6SrcPortRange_Object = MibTableColumn
me1200QosQceIpv6SrcPortRange = _Me1200QosQceIpv6SrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 515),
    _Me1200QosQceIpv6SrcPortRange_Type()
)
me1200QosQceIpv6SrcPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv6SrcPortRange.setStatus("current")
_Me1200QosQceIpv6DestPortOp_Type = ME1200ASRType
_Me1200QosQceIpv6DestPortOp_Object = MibTableColumn
me1200QosQceIpv6DestPortOp = _Me1200QosQceIpv6DestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 516),
    _Me1200QosQceIpv6DestPortOp_Type()
)
me1200QosQceIpv6DestPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv6DestPortOp.setStatus("current")
_Me1200QosQceIpv6DestPort_Type = ME1200Unsigned16
_Me1200QosQceIpv6DestPort_Object = MibTableColumn
me1200QosQceIpv6DestPort = _Me1200QosQceIpv6DestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 517),
    _Me1200QosQceIpv6DestPort_Type()
)
me1200QosQceIpv6DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv6DestPort.setStatus("current")
_Me1200QosQceIpv6DestPortRange_Type = ME1200Unsigned16
_Me1200QosQceIpv6DestPortRange_Object = MibTableColumn
me1200QosQceIpv6DestPortRange = _Me1200QosQceIpv6DestPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 518),
    _Me1200QosQceIpv6DestPortRange_Type()
)
me1200QosQceIpv6DestPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceIpv6DestPortRange.setStatus("current")
_Me1200QosQceActionCosEnable_Type = TruthValue
_Me1200QosQceActionCosEnable_Object = MibTableColumn
me1200QosQceActionCosEnable = _Me1200QosQceActionCosEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 1000),
    _Me1200QosQceActionCosEnable_Type()
)
me1200QosQceActionCosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceActionCosEnable.setStatus("current")
_Me1200QosQceActionCos_Type = Unsigned32
_Me1200QosQceActionCos_Object = MibTableColumn
me1200QosQceActionCos = _Me1200QosQceActionCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 1001),
    _Me1200QosQceActionCos_Type()
)
me1200QosQceActionCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceActionCos.setStatus("current")
_Me1200QosQceActionDplEnable_Type = TruthValue
_Me1200QosQceActionDplEnable_Object = MibTableColumn
me1200QosQceActionDplEnable = _Me1200QosQceActionDplEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 1002),
    _Me1200QosQceActionDplEnable_Type()
)
me1200QosQceActionDplEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceActionDplEnable.setStatus("current")
_Me1200QosQceActionDpl_Type = ME1200Unsigned8
_Me1200QosQceActionDpl_Object = MibTableColumn
me1200QosQceActionDpl = _Me1200QosQceActionDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 1003),
    _Me1200QosQceActionDpl_Type()
)
me1200QosQceActionDpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceActionDpl.setStatus("current")
_Me1200QosQceActionDscpEnable_Type = TruthValue
_Me1200QosQceActionDscpEnable_Object = MibTableColumn
me1200QosQceActionDscpEnable = _Me1200QosQceActionDscpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 1004),
    _Me1200QosQceActionDscpEnable_Type()
)
me1200QosQceActionDscpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceActionDscpEnable.setStatus("current")
_Me1200QosQceActionDscp_Type = ME1200Unsigned8
_Me1200QosQceActionDscp_Object = MibTableColumn
me1200QosQceActionDscp = _Me1200QosQceActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 1005),
    _Me1200QosQceActionDscp_Type()
)
me1200QosQceActionDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceActionDscp.setStatus("current")
_Me1200QosQceActionPcpDeiEnable_Type = TruthValue
_Me1200QosQceActionPcpDeiEnable_Object = MibTableColumn
me1200QosQceActionPcpDeiEnable = _Me1200QosQceActionPcpDeiEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 1006),
    _Me1200QosQceActionPcpDeiEnable_Type()
)
me1200QosQceActionPcpDeiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceActionPcpDeiEnable.setStatus("current")
_Me1200QosQceActionPcp_Type = Unsigned32
_Me1200QosQceActionPcp_Object = MibTableColumn
me1200QosQceActionPcp = _Me1200QosQceActionPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 1007),
    _Me1200QosQceActionPcp_Type()
)
me1200QosQceActionPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceActionPcp.setStatus("current")
_Me1200QosQceActionDei_Type = ME1200Unsigned8
_Me1200QosQceActionDei_Object = MibTableColumn
me1200QosQceActionDei = _Me1200QosQceActionDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 1008),
    _Me1200QosQceActionDei_Type()
)
me1200QosQceActionDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceActionDei.setStatus("current")
_Me1200QosQceActionPolicyEnable_Type = TruthValue
_Me1200QosQceActionPolicyEnable_Object = MibTableColumn
me1200QosQceActionPolicyEnable = _Me1200QosQceActionPolicyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 1009),
    _Me1200QosQceActionPolicyEnable_Type()
)
me1200QosQceActionPolicyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceActionPolicyEnable.setStatus("current")
_Me1200QosQceActionPolicy_Type = Unsigned32
_Me1200QosQceActionPolicy_Object = MibTableColumn
me1200QosQceActionPolicy = _Me1200QosQceActionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 1010),
    _Me1200QosQceActionPolicy_Type()
)
me1200QosQceActionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceActionPolicy.setStatus("current")
_Me1200QosQceAction_Type = ME1200RowEditorState
_Me1200QosQceAction_Object = MibTableColumn
me1200QosQceAction = _Me1200QosQceAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 1, 1, 10000),
    _Me1200QosQceAction_Type()
)
me1200QosQceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceAction.setStatus("current")
_Me1200QosQceTableRowEditor_ObjectIdentity = ObjectIdentity
me1200QosQceTableRowEditor = _Me1200QosQceTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2)
)


class _Me1200QosQceTableRowEditorQceId_Type(Integer32):
    """Custom type me1200QosQceTableRowEditorQceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200QosQceTableRowEditorQceId_Type.__name__ = "Integer32"
_Me1200QosQceTableRowEditorQceId_Object = MibScalar
me1200QosQceTableRowEditorQceId = _Me1200QosQceTableRowEditorQceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 1),
    _Me1200QosQceTableRowEditorQceId_Type()
)
me1200QosQceTableRowEditorQceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorQceId.setStatus("current")
_Me1200QosQceTableRowEditorNextQceId_Type = Unsigned32
_Me1200QosQceTableRowEditorNextQceId_Object = MibScalar
me1200QosQceTableRowEditorNextQceId = _Me1200QosQceTableRowEditorNextQceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 2),
    _Me1200QosQceTableRowEditorNextQceId_Type()
)
me1200QosQceTableRowEditorNextQceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorNextQceId.setStatus("current")
_Me1200QosQceTableRowEditorPortList_Type = ME1200PortList
_Me1200QosQceTableRowEditorPortList_Object = MibScalar
me1200QosQceTableRowEditorPortList = _Me1200QosQceTableRowEditorPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 4),
    _Me1200QosQceTableRowEditorPortList_Type()
)
me1200QosQceTableRowEditorPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorPortList.setStatus("current")
_Me1200QosQceTableRowEditorDestMacType_Type = ME1200DestMacType
_Me1200QosQceTableRowEditorDestMacType_Object = MibScalar
me1200QosQceTableRowEditorDestMacType = _Me1200QosQceTableRowEditorDestMacType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 5),
    _Me1200QosQceTableRowEditorDestMacType_Type()
)
me1200QosQceTableRowEditorDestMacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorDestMacType.setStatus("current")
_Me1200QosQceTableRowEditorDestMac_Type = MacAddress
_Me1200QosQceTableRowEditorDestMac_Object = MibScalar
me1200QosQceTableRowEditorDestMac = _Me1200QosQceTableRowEditorDestMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 6),
    _Me1200QosQceTableRowEditorDestMac_Type()
)
me1200QosQceTableRowEditorDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorDestMac.setStatus("current")
_Me1200QosQceTableRowEditorDestMacMask_Type = MacAddress
_Me1200QosQceTableRowEditorDestMacMask_Object = MibScalar
me1200QosQceTableRowEditorDestMacMask = _Me1200QosQceTableRowEditorDestMacMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 7),
    _Me1200QosQceTableRowEditorDestMacMask_Type()
)
me1200QosQceTableRowEditorDestMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorDestMacMask.setStatus("current")
_Me1200QosQceTableRowEditorSrcMac_Type = MacAddress
_Me1200QosQceTableRowEditorSrcMac_Object = MibScalar
me1200QosQceTableRowEditorSrcMac = _Me1200QosQceTableRowEditorSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 8),
    _Me1200QosQceTableRowEditorSrcMac_Type()
)
me1200QosQceTableRowEditorSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorSrcMac.setStatus("current")
_Me1200QosQceTableRowEditorSrcMacMask_Type = MacAddress
_Me1200QosQceTableRowEditorSrcMacMask_Object = MibScalar
me1200QosQceTableRowEditorSrcMacMask = _Me1200QosQceTableRowEditorSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 9),
    _Me1200QosQceTableRowEditorSrcMacMask_Type()
)
me1200QosQceTableRowEditorSrcMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorSrcMacMask.setStatus("current")
_Me1200QosQceTableRowEditorVlanTagType_Type = ME1200VlanTagType
_Me1200QosQceTableRowEditorVlanTagType_Object = MibScalar
me1200QosQceTableRowEditorVlanTagType = _Me1200QosQceTableRowEditorVlanTagType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 10),
    _Me1200QosQceTableRowEditorVlanTagType_Type()
)
me1200QosQceTableRowEditorVlanTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorVlanTagType.setStatus("current")
_Me1200QosQceTableRowEditorVlanIdOp_Type = ME1200ASRType
_Me1200QosQceTableRowEditorVlanIdOp_Object = MibScalar
me1200QosQceTableRowEditorVlanIdOp = _Me1200QosQceTableRowEditorVlanIdOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 11),
    _Me1200QosQceTableRowEditorVlanIdOp_Type()
)
me1200QosQceTableRowEditorVlanIdOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorVlanIdOp.setStatus("current")
_Me1200QosQceTableRowEditorVlanId_Type = ME1200Unsigned16
_Me1200QosQceTableRowEditorVlanId_Object = MibScalar
me1200QosQceTableRowEditorVlanId = _Me1200QosQceTableRowEditorVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 12),
    _Me1200QosQceTableRowEditorVlanId_Type()
)
me1200QosQceTableRowEditorVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorVlanId.setStatus("current")
_Me1200QosQceTableRowEditorVlanIdRange_Type = ME1200Unsigned16
_Me1200QosQceTableRowEditorVlanIdRange_Object = MibScalar
me1200QosQceTableRowEditorVlanIdRange = _Me1200QosQceTableRowEditorVlanIdRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 13),
    _Me1200QosQceTableRowEditorVlanIdRange_Type()
)
me1200QosQceTableRowEditorVlanIdRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorVlanIdRange.setStatus("current")
_Me1200QosQceTableRowEditorPcp_Type = ME1200VlanTagPriority
_Me1200QosQceTableRowEditorPcp_Object = MibScalar
me1200QosQceTableRowEditorPcp = _Me1200QosQceTableRowEditorPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 14),
    _Me1200QosQceTableRowEditorPcp_Type()
)
me1200QosQceTableRowEditorPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorPcp.setStatus("current")
_Me1200QosQceTableRowEditorDei_Type = ME1200BitType
_Me1200QosQceTableRowEditorDei_Object = MibScalar
me1200QosQceTableRowEditorDei = _Me1200QosQceTableRowEditorDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 15),
    _Me1200QosQceTableRowEditorDei_Type()
)
me1200QosQceTableRowEditorDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorDei.setStatus("current")
_Me1200QosQceTableRowEditorInnerVlanTagType_Type = ME1200VlanTagType
_Me1200QosQceTableRowEditorInnerVlanTagType_Object = MibScalar
me1200QosQceTableRowEditorInnerVlanTagType = _Me1200QosQceTableRowEditorInnerVlanTagType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 16),
    _Me1200QosQceTableRowEditorInnerVlanTagType_Type()
)
me1200QosQceTableRowEditorInnerVlanTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorInnerVlanTagType.setStatus("current")
_Me1200QosQceTableRowEditorInnerVlanIdOp_Type = ME1200ASRType
_Me1200QosQceTableRowEditorInnerVlanIdOp_Object = MibScalar
me1200QosQceTableRowEditorInnerVlanIdOp = _Me1200QosQceTableRowEditorInnerVlanIdOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 17),
    _Me1200QosQceTableRowEditorInnerVlanIdOp_Type()
)
me1200QosQceTableRowEditorInnerVlanIdOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorInnerVlanIdOp.setStatus("current")
_Me1200QosQceTableRowEditorInnerVlanId_Type = ME1200Unsigned16
_Me1200QosQceTableRowEditorInnerVlanId_Object = MibScalar
me1200QosQceTableRowEditorInnerVlanId = _Me1200QosQceTableRowEditorInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 18),
    _Me1200QosQceTableRowEditorInnerVlanId_Type()
)
me1200QosQceTableRowEditorInnerVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorInnerVlanId.setStatus("current")
_Me1200QosQceTableRowEditorInnerVlanIdRange_Type = ME1200Unsigned16
_Me1200QosQceTableRowEditorInnerVlanIdRange_Object = MibScalar
me1200QosQceTableRowEditorInnerVlanIdRange = _Me1200QosQceTableRowEditorInnerVlanIdRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 19),
    _Me1200QosQceTableRowEditorInnerVlanIdRange_Type()
)
me1200QosQceTableRowEditorInnerVlanIdRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorInnerVlanIdRange.setStatus("current")
_Me1200QosQceTableRowEditorInnerPcp_Type = ME1200VlanTagPriority
_Me1200QosQceTableRowEditorInnerPcp_Object = MibScalar
me1200QosQceTableRowEditorInnerPcp = _Me1200QosQceTableRowEditorInnerPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 20),
    _Me1200QosQceTableRowEditorInnerPcp_Type()
)
me1200QosQceTableRowEditorInnerPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorInnerPcp.setStatus("current")
_Me1200QosQceTableRowEditorInnerDei_Type = ME1200BitType
_Me1200QosQceTableRowEditorInnerDei_Object = MibScalar
me1200QosQceTableRowEditorInnerDei = _Me1200QosQceTableRowEditorInnerDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 21),
    _Me1200QosQceTableRowEditorInnerDei_Type()
)
me1200QosQceTableRowEditorInnerDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorInnerDei.setStatus("current")
_Me1200QosQceTableRowEditorFrameType_Type = ME1200QceFrameType
_Me1200QosQceTableRowEditorFrameType_Object = MibScalar
me1200QosQceTableRowEditorFrameType = _Me1200QosQceTableRowEditorFrameType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 100),
    _Me1200QosQceTableRowEditorFrameType_Type()
)
me1200QosQceTableRowEditorFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorFrameType.setStatus("current")
_Me1200QosQceTableRowEditorEtype_Type = ME1200EtherType
_Me1200QosQceTableRowEditorEtype_Object = MibScalar
me1200QosQceTableRowEditorEtype = _Me1200QosQceTableRowEditorEtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 101),
    _Me1200QosQceTableRowEditorEtype_Type()
)
me1200QosQceTableRowEditorEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorEtype.setStatus("current")
_Me1200QosQceTableRowEditorLlcDsap_Type = ME1200Unsigned8
_Me1200QosQceTableRowEditorLlcDsap_Object = MibScalar
me1200QosQceTableRowEditorLlcDsap = _Me1200QosQceTableRowEditorLlcDsap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 200),
    _Me1200QosQceTableRowEditorLlcDsap_Type()
)
me1200QosQceTableRowEditorLlcDsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorLlcDsap.setStatus("current")
_Me1200QosQceTableRowEditorLlcDsapMask_Type = ME1200Unsigned8
_Me1200QosQceTableRowEditorLlcDsapMask_Object = MibScalar
me1200QosQceTableRowEditorLlcDsapMask = _Me1200QosQceTableRowEditorLlcDsapMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 201),
    _Me1200QosQceTableRowEditorLlcDsapMask_Type()
)
me1200QosQceTableRowEditorLlcDsapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorLlcDsapMask.setStatus("current")
_Me1200QosQceTableRowEditorLlcSsap_Type = ME1200Unsigned8
_Me1200QosQceTableRowEditorLlcSsap_Object = MibScalar
me1200QosQceTableRowEditorLlcSsap = _Me1200QosQceTableRowEditorLlcSsap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 202),
    _Me1200QosQceTableRowEditorLlcSsap_Type()
)
me1200QosQceTableRowEditorLlcSsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorLlcSsap.setStatus("current")
_Me1200QosQceTableRowEditorLlcSsapMask_Type = ME1200Unsigned8
_Me1200QosQceTableRowEditorLlcSsapMask_Object = MibScalar
me1200QosQceTableRowEditorLlcSsapMask = _Me1200QosQceTableRowEditorLlcSsapMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 203),
    _Me1200QosQceTableRowEditorLlcSsapMask_Type()
)
me1200QosQceTableRowEditorLlcSsapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorLlcSsapMask.setStatus("current")
_Me1200QosQceTableRowEditorLlcControl_Type = ME1200Unsigned8
_Me1200QosQceTableRowEditorLlcControl_Object = MibScalar
me1200QosQceTableRowEditorLlcControl = _Me1200QosQceTableRowEditorLlcControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 204),
    _Me1200QosQceTableRowEditorLlcControl_Type()
)
me1200QosQceTableRowEditorLlcControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorLlcControl.setStatus("current")
_Me1200QosQceTableRowEditorLlcControlMask_Type = ME1200Unsigned8
_Me1200QosQceTableRowEditorLlcControlMask_Object = MibScalar
me1200QosQceTableRowEditorLlcControlMask = _Me1200QosQceTableRowEditorLlcControlMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 205),
    _Me1200QosQceTableRowEditorLlcControlMask_Type()
)
me1200QosQceTableRowEditorLlcControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorLlcControlMask.setStatus("current")
_Me1200QosQceTableRowEditorSnapPid_Type = ME1200Unsigned16
_Me1200QosQceTableRowEditorSnapPid_Object = MibScalar
me1200QosQceTableRowEditorSnapPid = _Me1200QosQceTableRowEditorSnapPid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 302),
    _Me1200QosQceTableRowEditorSnapPid_Type()
)
me1200QosQceTableRowEditorSnapPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorSnapPid.setStatus("current")
_Me1200QosQceTableRowEditorSnapPidMask_Type = ME1200Unsigned16
_Me1200QosQceTableRowEditorSnapPidMask_Object = MibScalar
me1200QosQceTableRowEditorSnapPidMask = _Me1200QosQceTableRowEditorSnapPidMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 303),
    _Me1200QosQceTableRowEditorSnapPidMask_Type()
)
me1200QosQceTableRowEditorSnapPidMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorSnapPidMask.setStatus("current")
_Me1200QosQceTableRowEditorIpv4Fragment_Type = ME1200BitType
_Me1200QosQceTableRowEditorIpv4Fragment_Object = MibScalar
me1200QosQceTableRowEditorIpv4Fragment = _Me1200QosQceTableRowEditorIpv4Fragment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 400),
    _Me1200QosQceTableRowEditorIpv4Fragment_Type()
)
me1200QosQceTableRowEditorIpv4Fragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv4Fragment.setStatus("current")
_Me1200QosQceTableRowEditorIpv4DscpOp_Type = ME1200ASRType
_Me1200QosQceTableRowEditorIpv4DscpOp_Object = MibScalar
me1200QosQceTableRowEditorIpv4DscpOp = _Me1200QosQceTableRowEditorIpv4DscpOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 401),
    _Me1200QosQceTableRowEditorIpv4DscpOp_Type()
)
me1200QosQceTableRowEditorIpv4DscpOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv4DscpOp.setStatus("current")
_Me1200QosQceTableRowEditorIpv4Dscp_Type = ME1200Unsigned16
_Me1200QosQceTableRowEditorIpv4Dscp_Object = MibScalar
me1200QosQceTableRowEditorIpv4Dscp = _Me1200QosQceTableRowEditorIpv4Dscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 402),
    _Me1200QosQceTableRowEditorIpv4Dscp_Type()
)
me1200QosQceTableRowEditorIpv4Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv4Dscp.setStatus("current")
_Me1200QosQceTableRowEditorIpv4DscpRange_Type = ME1200Unsigned16
_Me1200QosQceTableRowEditorIpv4DscpRange_Object = MibScalar
me1200QosQceTableRowEditorIpv4DscpRange = _Me1200QosQceTableRowEditorIpv4DscpRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 403),
    _Me1200QosQceTableRowEditorIpv4DscpRange_Type()
)
me1200QosQceTableRowEditorIpv4DscpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv4DscpRange.setStatus("current")
_Me1200QosQceTableRowEditorIpv4Protocol_Type = ME1200Unsigned8
_Me1200QosQceTableRowEditorIpv4Protocol_Object = MibScalar
me1200QosQceTableRowEditorIpv4Protocol = _Me1200QosQceTableRowEditorIpv4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 404),
    _Me1200QosQceTableRowEditorIpv4Protocol_Type()
)
me1200QosQceTableRowEditorIpv4Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv4Protocol.setStatus("current")
_Me1200QosQceTableRowEditorIpv4ProtocolMask_Type = ME1200Unsigned8
_Me1200QosQceTableRowEditorIpv4ProtocolMask_Object = MibScalar
me1200QosQceTableRowEditorIpv4ProtocolMask = _Me1200QosQceTableRowEditorIpv4ProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 405),
    _Me1200QosQceTableRowEditorIpv4ProtocolMask_Type()
)
me1200QosQceTableRowEditorIpv4ProtocolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv4ProtocolMask.setStatus("current")
_Me1200QosQceTableRowEditorIpv4SrcIp_Type = IpAddress
_Me1200QosQceTableRowEditorIpv4SrcIp_Object = MibScalar
me1200QosQceTableRowEditorIpv4SrcIp = _Me1200QosQceTableRowEditorIpv4SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 406),
    _Me1200QosQceTableRowEditorIpv4SrcIp_Type()
)
me1200QosQceTableRowEditorIpv4SrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv4SrcIp.setStatus("current")
_Me1200QosQceTableRowEditorIpv4SrcIpMask_Type = IpAddress
_Me1200QosQceTableRowEditorIpv4SrcIpMask_Object = MibScalar
me1200QosQceTableRowEditorIpv4SrcIpMask = _Me1200QosQceTableRowEditorIpv4SrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 407),
    _Me1200QosQceTableRowEditorIpv4SrcIpMask_Type()
)
me1200QosQceTableRowEditorIpv4SrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv4SrcIpMask.setStatus("current")
_Me1200QosQceTableRowEditorIpv4DestIp_Type = IpAddress
_Me1200QosQceTableRowEditorIpv4DestIp_Object = MibScalar
me1200QosQceTableRowEditorIpv4DestIp = _Me1200QosQceTableRowEditorIpv4DestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 408),
    _Me1200QosQceTableRowEditorIpv4DestIp_Type()
)
me1200QosQceTableRowEditorIpv4DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv4DestIp.setStatus("current")
_Me1200QosQceTableRowEditorIpv4DestIpMask_Type = IpAddress
_Me1200QosQceTableRowEditorIpv4DestIpMask_Object = MibScalar
me1200QosQceTableRowEditorIpv4DestIpMask = _Me1200QosQceTableRowEditorIpv4DestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 409),
    _Me1200QosQceTableRowEditorIpv4DestIpMask_Type()
)
me1200QosQceTableRowEditorIpv4DestIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv4DestIpMask.setStatus("current")
_Me1200QosQceTableRowEditorIpv4SrcPortOp_Type = ME1200ASRType
_Me1200QosQceTableRowEditorIpv4SrcPortOp_Object = MibScalar
me1200QosQceTableRowEditorIpv4SrcPortOp = _Me1200QosQceTableRowEditorIpv4SrcPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 410),
    _Me1200QosQceTableRowEditorIpv4SrcPortOp_Type()
)
me1200QosQceTableRowEditorIpv4SrcPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv4SrcPortOp.setStatus("current")
_Me1200QosQceTableRowEditorIpv4SrcPort_Type = ME1200Unsigned16
_Me1200QosQceTableRowEditorIpv4SrcPort_Object = MibScalar
me1200QosQceTableRowEditorIpv4SrcPort = _Me1200QosQceTableRowEditorIpv4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 411),
    _Me1200QosQceTableRowEditorIpv4SrcPort_Type()
)
me1200QosQceTableRowEditorIpv4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv4SrcPort.setStatus("current")
_Me1200QosQceTableRowEditorIpv4SrcPortRange_Type = ME1200Unsigned16
_Me1200QosQceTableRowEditorIpv4SrcPortRange_Object = MibScalar
me1200QosQceTableRowEditorIpv4SrcPortRange = _Me1200QosQceTableRowEditorIpv4SrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 412),
    _Me1200QosQceTableRowEditorIpv4SrcPortRange_Type()
)
me1200QosQceTableRowEditorIpv4SrcPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv4SrcPortRange.setStatus("current")
_Me1200QosQceTableRowEditorIpv4DestPortOp_Type = ME1200ASRType
_Me1200QosQceTableRowEditorIpv4DestPortOp_Object = MibScalar
me1200QosQceTableRowEditorIpv4DestPortOp = _Me1200QosQceTableRowEditorIpv4DestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 413),
    _Me1200QosQceTableRowEditorIpv4DestPortOp_Type()
)
me1200QosQceTableRowEditorIpv4DestPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv4DestPortOp.setStatus("current")
_Me1200QosQceTableRowEditorIpv4DestPort_Type = ME1200Unsigned16
_Me1200QosQceTableRowEditorIpv4DestPort_Object = MibScalar
me1200QosQceTableRowEditorIpv4DestPort = _Me1200QosQceTableRowEditorIpv4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 414),
    _Me1200QosQceTableRowEditorIpv4DestPort_Type()
)
me1200QosQceTableRowEditorIpv4DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv4DestPort.setStatus("current")
_Me1200QosQceTableRowEditorIpv4DestPortRange_Type = ME1200Unsigned16
_Me1200QosQceTableRowEditorIpv4DestPortRange_Object = MibScalar
me1200QosQceTableRowEditorIpv4DestPortRange = _Me1200QosQceTableRowEditorIpv4DestPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 415),
    _Me1200QosQceTableRowEditorIpv4DestPortRange_Type()
)
me1200QosQceTableRowEditorIpv4DestPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv4DestPortRange.setStatus("current")
_Me1200QosQceTableRowEditorIpv6DscpOp_Type = ME1200ASRType
_Me1200QosQceTableRowEditorIpv6DscpOp_Object = MibScalar
me1200QosQceTableRowEditorIpv6DscpOp = _Me1200QosQceTableRowEditorIpv6DscpOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 500),
    _Me1200QosQceTableRowEditorIpv6DscpOp_Type()
)
me1200QosQceTableRowEditorIpv6DscpOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv6DscpOp.setStatus("current")
_Me1200QosQceTableRowEditorIpv6Dscp_Type = ME1200Unsigned16
_Me1200QosQceTableRowEditorIpv6Dscp_Object = MibScalar
me1200QosQceTableRowEditorIpv6Dscp = _Me1200QosQceTableRowEditorIpv6Dscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 501),
    _Me1200QosQceTableRowEditorIpv6Dscp_Type()
)
me1200QosQceTableRowEditorIpv6Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv6Dscp.setStatus("current")
_Me1200QosQceTableRowEditorIpv6DscpRange_Type = ME1200Unsigned16
_Me1200QosQceTableRowEditorIpv6DscpRange_Object = MibScalar
me1200QosQceTableRowEditorIpv6DscpRange = _Me1200QosQceTableRowEditorIpv6DscpRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 502),
    _Me1200QosQceTableRowEditorIpv6DscpRange_Type()
)
me1200QosQceTableRowEditorIpv6DscpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv6DscpRange.setStatus("current")
_Me1200QosQceTableRowEditorIpv6Protocol_Type = ME1200Unsigned8
_Me1200QosQceTableRowEditorIpv6Protocol_Object = MibScalar
me1200QosQceTableRowEditorIpv6Protocol = _Me1200QosQceTableRowEditorIpv6Protocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 503),
    _Me1200QosQceTableRowEditorIpv6Protocol_Type()
)
me1200QosQceTableRowEditorIpv6Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv6Protocol.setStatus("current")
_Me1200QosQceTableRowEditorIpv6ProtocolMask_Type = ME1200Unsigned8
_Me1200QosQceTableRowEditorIpv6ProtocolMask_Object = MibScalar
me1200QosQceTableRowEditorIpv6ProtocolMask = _Me1200QosQceTableRowEditorIpv6ProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 504),
    _Me1200QosQceTableRowEditorIpv6ProtocolMask_Type()
)
me1200QosQceTableRowEditorIpv6ProtocolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv6ProtocolMask.setStatus("current")
_Me1200QosQceTableRowEditorIpv6SrcIp_Type = InetAddressIPv6
_Me1200QosQceTableRowEditorIpv6SrcIp_Object = MibScalar
me1200QosQceTableRowEditorIpv6SrcIp = _Me1200QosQceTableRowEditorIpv6SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 506),
    _Me1200QosQceTableRowEditorIpv6SrcIp_Type()
)
me1200QosQceTableRowEditorIpv6SrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv6SrcIp.setStatus("current")
_Me1200QosQceTableRowEditorIpv6SrcIpMask_Type = InetAddressIPv6
_Me1200QosQceTableRowEditorIpv6SrcIpMask_Object = MibScalar
me1200QosQceTableRowEditorIpv6SrcIpMask = _Me1200QosQceTableRowEditorIpv6SrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 508),
    _Me1200QosQceTableRowEditorIpv6SrcIpMask_Type()
)
me1200QosQceTableRowEditorIpv6SrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv6SrcIpMask.setStatus("current")
_Me1200QosQceTableRowEditorIpv6DestIp_Type = InetAddressIPv6
_Me1200QosQceTableRowEditorIpv6DestIp_Object = MibScalar
me1200QosQceTableRowEditorIpv6DestIp = _Me1200QosQceTableRowEditorIpv6DestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 510),
    _Me1200QosQceTableRowEditorIpv6DestIp_Type()
)
me1200QosQceTableRowEditorIpv6DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv6DestIp.setStatus("current")
_Me1200QosQceTableRowEditorIpv6DestIpMask_Type = InetAddressIPv6
_Me1200QosQceTableRowEditorIpv6DestIpMask_Object = MibScalar
me1200QosQceTableRowEditorIpv6DestIpMask = _Me1200QosQceTableRowEditorIpv6DestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 512),
    _Me1200QosQceTableRowEditorIpv6DestIpMask_Type()
)
me1200QosQceTableRowEditorIpv6DestIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv6DestIpMask.setStatus("current")
_Me1200QosQceTableRowEditorIpv6SrcPortOp_Type = ME1200ASRType
_Me1200QosQceTableRowEditorIpv6SrcPortOp_Object = MibScalar
me1200QosQceTableRowEditorIpv6SrcPortOp = _Me1200QosQceTableRowEditorIpv6SrcPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 513),
    _Me1200QosQceTableRowEditorIpv6SrcPortOp_Type()
)
me1200QosQceTableRowEditorIpv6SrcPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv6SrcPortOp.setStatus("current")
_Me1200QosQceTableRowEditorIpv6SrcPort_Type = ME1200Unsigned16
_Me1200QosQceTableRowEditorIpv6SrcPort_Object = MibScalar
me1200QosQceTableRowEditorIpv6SrcPort = _Me1200QosQceTableRowEditorIpv6SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 514),
    _Me1200QosQceTableRowEditorIpv6SrcPort_Type()
)
me1200QosQceTableRowEditorIpv6SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv6SrcPort.setStatus("current")
_Me1200QosQceTableRowEditorIpv6SrcPortRange_Type = ME1200Unsigned16
_Me1200QosQceTableRowEditorIpv6SrcPortRange_Object = MibScalar
me1200QosQceTableRowEditorIpv6SrcPortRange = _Me1200QosQceTableRowEditorIpv6SrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 515),
    _Me1200QosQceTableRowEditorIpv6SrcPortRange_Type()
)
me1200QosQceTableRowEditorIpv6SrcPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv6SrcPortRange.setStatus("current")
_Me1200QosQceTableRowEditorIpv6DestPortOp_Type = ME1200ASRType
_Me1200QosQceTableRowEditorIpv6DestPortOp_Object = MibScalar
me1200QosQceTableRowEditorIpv6DestPortOp = _Me1200QosQceTableRowEditorIpv6DestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 516),
    _Me1200QosQceTableRowEditorIpv6DestPortOp_Type()
)
me1200QosQceTableRowEditorIpv6DestPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv6DestPortOp.setStatus("current")
_Me1200QosQceTableRowEditorIpv6DestPort_Type = ME1200Unsigned16
_Me1200QosQceTableRowEditorIpv6DestPort_Object = MibScalar
me1200QosQceTableRowEditorIpv6DestPort = _Me1200QosQceTableRowEditorIpv6DestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 517),
    _Me1200QosQceTableRowEditorIpv6DestPort_Type()
)
me1200QosQceTableRowEditorIpv6DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv6DestPort.setStatus("current")
_Me1200QosQceTableRowEditorIpv6DestPortRange_Type = ME1200Unsigned16
_Me1200QosQceTableRowEditorIpv6DestPortRange_Object = MibScalar
me1200QosQceTableRowEditorIpv6DestPortRange = _Me1200QosQceTableRowEditorIpv6DestPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 518),
    _Me1200QosQceTableRowEditorIpv6DestPortRange_Type()
)
me1200QosQceTableRowEditorIpv6DestPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorIpv6DestPortRange.setStatus("current")
_Me1200QosQceTableRowEditorActionCosEnable_Type = TruthValue
_Me1200QosQceTableRowEditorActionCosEnable_Object = MibScalar
me1200QosQceTableRowEditorActionCosEnable = _Me1200QosQceTableRowEditorActionCosEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 1000),
    _Me1200QosQceTableRowEditorActionCosEnable_Type()
)
me1200QosQceTableRowEditorActionCosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorActionCosEnable.setStatus("current")
_Me1200QosQceTableRowEditorActionCos_Type = Unsigned32
_Me1200QosQceTableRowEditorActionCos_Object = MibScalar
me1200QosQceTableRowEditorActionCos = _Me1200QosQceTableRowEditorActionCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 1001),
    _Me1200QosQceTableRowEditorActionCos_Type()
)
me1200QosQceTableRowEditorActionCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorActionCos.setStatus("current")
_Me1200QosQceTableRowEditorActionDplEnable_Type = TruthValue
_Me1200QosQceTableRowEditorActionDplEnable_Object = MibScalar
me1200QosQceTableRowEditorActionDplEnable = _Me1200QosQceTableRowEditorActionDplEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 1002),
    _Me1200QosQceTableRowEditorActionDplEnable_Type()
)
me1200QosQceTableRowEditorActionDplEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorActionDplEnable.setStatus("current")
_Me1200QosQceTableRowEditorActionDpl_Type = ME1200Unsigned8
_Me1200QosQceTableRowEditorActionDpl_Object = MibScalar
me1200QosQceTableRowEditorActionDpl = _Me1200QosQceTableRowEditorActionDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 1003),
    _Me1200QosQceTableRowEditorActionDpl_Type()
)
me1200QosQceTableRowEditorActionDpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorActionDpl.setStatus("current")
_Me1200QosQceTableRowEditorActionDscpEnable_Type = TruthValue
_Me1200QosQceTableRowEditorActionDscpEnable_Object = MibScalar
me1200QosQceTableRowEditorActionDscpEnable = _Me1200QosQceTableRowEditorActionDscpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 1004),
    _Me1200QosQceTableRowEditorActionDscpEnable_Type()
)
me1200QosQceTableRowEditorActionDscpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorActionDscpEnable.setStatus("current")
_Me1200QosQceTableRowEditorActionDscp_Type = ME1200Unsigned8
_Me1200QosQceTableRowEditorActionDscp_Object = MibScalar
me1200QosQceTableRowEditorActionDscp = _Me1200QosQceTableRowEditorActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 1005),
    _Me1200QosQceTableRowEditorActionDscp_Type()
)
me1200QosQceTableRowEditorActionDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorActionDscp.setStatus("current")
_Me1200QosQceTableRowEditorActionPcpDeiEnable_Type = TruthValue
_Me1200QosQceTableRowEditorActionPcpDeiEnable_Object = MibScalar
me1200QosQceTableRowEditorActionPcpDeiEnable = _Me1200QosQceTableRowEditorActionPcpDeiEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 1006),
    _Me1200QosQceTableRowEditorActionPcpDeiEnable_Type()
)
me1200QosQceTableRowEditorActionPcpDeiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorActionPcpDeiEnable.setStatus("current")
_Me1200QosQceTableRowEditorActionPcp_Type = Unsigned32
_Me1200QosQceTableRowEditorActionPcp_Object = MibScalar
me1200QosQceTableRowEditorActionPcp = _Me1200QosQceTableRowEditorActionPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 1007),
    _Me1200QosQceTableRowEditorActionPcp_Type()
)
me1200QosQceTableRowEditorActionPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorActionPcp.setStatus("current")
_Me1200QosQceTableRowEditorActionDei_Type = ME1200Unsigned8
_Me1200QosQceTableRowEditorActionDei_Object = MibScalar
me1200QosQceTableRowEditorActionDei = _Me1200QosQceTableRowEditorActionDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 1008),
    _Me1200QosQceTableRowEditorActionDei_Type()
)
me1200QosQceTableRowEditorActionDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorActionDei.setStatus("current")
_Me1200QosQceTableRowEditorActionPolicyEnable_Type = TruthValue
_Me1200QosQceTableRowEditorActionPolicyEnable_Object = MibScalar
me1200QosQceTableRowEditorActionPolicyEnable = _Me1200QosQceTableRowEditorActionPolicyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 1009),
    _Me1200QosQceTableRowEditorActionPolicyEnable_Type()
)
me1200QosQceTableRowEditorActionPolicyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorActionPolicyEnable.setStatus("current")
_Me1200QosQceTableRowEditorActionPolicy_Type = Unsigned32
_Me1200QosQceTableRowEditorActionPolicy_Object = MibScalar
me1200QosQceTableRowEditorActionPolicy = _Me1200QosQceTableRowEditorActionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 1010),
    _Me1200QosQceTableRowEditorActionPolicy_Type()
)
me1200QosQceTableRowEditorActionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorActionPolicy.setStatus("current")
_Me1200QosQceTableRowEditorAction_Type = ME1200RowEditorState
_Me1200QosQceTableRowEditorAction_Object = MibScalar
me1200QosQceTableRowEditorAction = _Me1200QosQceTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 2, 10000),
    _Me1200QosQceTableRowEditorAction_Type()
)
me1200QosQceTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorAction.setStatus("current")
_Me1200QosQcePrecedenceTable_Object = MibTable
me1200QosQcePrecedenceTable = _Me1200QosQcePrecedenceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 3)
)
if mibBuilder.loadTexts:
    me1200QosQcePrecedenceTable.setStatus("current")
_Me1200QosQcePrecedenceEntry_Object = MibTableRow
me1200QosQcePrecedenceEntry = _Me1200QosQcePrecedenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 3, 1)
)
me1200QosQcePrecedenceEntry.setIndexNames(
    (0, "ME1200-QOS-MIB", "me1200QosQcePrecedenceIndex"),
)
if mibBuilder.loadTexts:
    me1200QosQcePrecedenceEntry.setStatus("current")


class _Me1200QosQcePrecedenceIndex_Type(Integer32):
    """Custom type me1200QosQcePrecedenceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200QosQcePrecedenceIndex_Type.__name__ = "Integer32"
_Me1200QosQcePrecedenceIndex_Object = MibTableColumn
me1200QosQcePrecedenceIndex = _Me1200QosQcePrecedenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 3, 1, 1),
    _Me1200QosQcePrecedenceIndex_Type()
)
me1200QosQcePrecedenceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosQcePrecedenceIndex.setStatus("current")
_Me1200QosQcePrecedenceQceId_Type = Unsigned32
_Me1200QosQcePrecedenceQceId_Object = MibTableColumn
me1200QosQcePrecedenceQceId = _Me1200QosQcePrecedenceQceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 1, 10, 3, 1, 2),
    _Me1200QosQcePrecedenceQceId_Type()
)
me1200QosQcePrecedenceQceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200QosQcePrecedenceQceId.setStatus("current")
_Me1200QosInterface_ObjectIdentity = ObjectIdentity
me1200QosInterface = _Me1200QosInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2)
)
_Me1200QosIfConfigTable_Object = MibTable
me1200QosIfConfigTable = _Me1200QosIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    me1200QosIfConfigTable.setStatus("current")
_Me1200QosIfConfigEntry_Object = MibTableRow
me1200QosIfConfigEntry = _Me1200QosIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 1, 1)
)
me1200QosIfConfigEntry.setIndexNames(
    (0, "ME1200-QOS-MIB", "me1200QosIfConfigIfIndex"),
)
if mibBuilder.loadTexts:
    me1200QosIfConfigEntry.setStatus("current")
_Me1200QosIfConfigIfIndex_Type = ME1200InterfaceIndex
_Me1200QosIfConfigIfIndex_Object = MibTableColumn
me1200QosIfConfigIfIndex = _Me1200QosIfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 1, 1, 1),
    _Me1200QosIfConfigIfIndex_Type()
)
me1200QosIfConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosIfConfigIfIndex.setStatus("current")
_Me1200QosIfConfigCos_Type = Unsigned32
_Me1200QosIfConfigCos_Object = MibTableColumn
me1200QosIfConfigCos = _Me1200QosIfConfigCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 1, 1, 2),
    _Me1200QosIfConfigCos_Type()
)
me1200QosIfConfigCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfConfigCos.setStatus("current")
_Me1200QosIfConfigDpl_Type = ME1200Unsigned8
_Me1200QosIfConfigDpl_Object = MibTableColumn
me1200QosIfConfigDpl = _Me1200QosIfConfigDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 1, 1, 3),
    _Me1200QosIfConfigDpl_Type()
)
me1200QosIfConfigDpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfConfigDpl.setStatus("current")
_Me1200QosIfConfigPcp_Type = Unsigned32
_Me1200QosIfConfigPcp_Object = MibTableColumn
me1200QosIfConfigPcp = _Me1200QosIfConfigPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 1, 1, 4),
    _Me1200QosIfConfigPcp_Type()
)
me1200QosIfConfigPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfConfigPcp.setStatus("current")
_Me1200QosIfConfigDei_Type = ME1200Unsigned8
_Me1200QosIfConfigDei_Object = MibTableColumn
me1200QosIfConfigDei = _Me1200QosIfConfigDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 1, 1, 5),
    _Me1200QosIfConfigDei_Type()
)
me1200QosIfConfigDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfConfigDei.setStatus("current")
_Me1200QosIfConfigTrustTag_Type = TruthValue
_Me1200QosIfConfigTrustTag_Object = MibTableColumn
me1200QosIfConfigTrustTag = _Me1200QosIfConfigTrustTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 1, 1, 6),
    _Me1200QosIfConfigTrustTag_Type()
)
me1200QosIfConfigTrustTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfConfigTrustTag.setStatus("current")
_Me1200QosIfConfigTrustDscp_Type = TruthValue
_Me1200QosIfConfigTrustDscp_Object = MibTableColumn
me1200QosIfConfigTrustDscp = _Me1200QosIfConfigTrustDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 1, 1, 7),
    _Me1200QosIfConfigTrustDscp_Type()
)
me1200QosIfConfigTrustDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfConfigTrustDscp.setStatus("current")
_Me1200QosIfConfigDwrrCount_Type = ME1200Unsigned8
_Me1200QosIfConfigDwrrCount_Object = MibTableColumn
me1200QosIfConfigDwrrCount = _Me1200QosIfConfigDwrrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 1, 1, 8),
    _Me1200QosIfConfigDwrrCount_Type()
)
me1200QosIfConfigDwrrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfConfigDwrrCount.setStatus("current")
_Me1200QosIfConfigTagRemarkingMode_Type = ME1200TagRemarkingMode
_Me1200QosIfConfigTagRemarkingMode_Object = MibTableColumn
me1200QosIfConfigTagRemarkingMode = _Me1200QosIfConfigTagRemarkingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 1, 1, 9),
    _Me1200QosIfConfigTagRemarkingMode_Type()
)
me1200QosIfConfigTagRemarkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfConfigTagRemarkingMode.setStatus("current")
_Me1200QosIfConfigTagPcp_Type = Unsigned32
_Me1200QosIfConfigTagPcp_Object = MibTableColumn
me1200QosIfConfigTagPcp = _Me1200QosIfConfigTagPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 1, 1, 10),
    _Me1200QosIfConfigTagPcp_Type()
)
me1200QosIfConfigTagPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfConfigTagPcp.setStatus("current")
_Me1200QosIfConfigTagDei_Type = ME1200Unsigned8
_Me1200QosIfConfigTagDei_Object = MibTableColumn
me1200QosIfConfigTagDei = _Me1200QosIfConfigTagDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 1, 1, 11),
    _Me1200QosIfConfigTagDei_Type()
)
me1200QosIfConfigTagDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfConfigTagDei.setStatus("current")
_Me1200QosIfConfigDscpTranslate_Type = TruthValue
_Me1200QosIfConfigDscpTranslate_Object = MibTableColumn
me1200QosIfConfigDscpTranslate = _Me1200QosIfConfigDscpTranslate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 1, 1, 12),
    _Me1200QosIfConfigDscpTranslate_Type()
)
me1200QosIfConfigDscpTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfConfigDscpTranslate.setStatus("current")
_Me1200QosIfConfigDscpClassify_Type = ME1200DscpClassify
_Me1200QosIfConfigDscpClassify_Object = MibTableColumn
me1200QosIfConfigDscpClassify = _Me1200QosIfConfigDscpClassify_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 1, 1, 13),
    _Me1200QosIfConfigDscpClassify_Type()
)
me1200QosIfConfigDscpClassify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfConfigDscpClassify.setStatus("current")
_Me1200QosIfConfigDscpRemark_Type = ME1200DscpRemark
_Me1200QosIfConfigDscpRemark_Object = MibTableColumn
me1200QosIfConfigDscpRemark = _Me1200QosIfConfigDscpRemark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 1, 1, 14),
    _Me1200QosIfConfigDscpRemark_Type()
)
me1200QosIfConfigDscpRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfConfigDscpRemark.setStatus("current")
_Me1200QosIfConfigQceAddressMode_Type = TruthValue
_Me1200QosIfConfigQceAddressMode_Object = MibTableColumn
me1200QosIfConfigQceAddressMode = _Me1200QosIfConfigQceAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 1, 1, 15),
    _Me1200QosIfConfigQceAddressMode_Type()
)
me1200QosIfConfigQceAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfConfigQceAddressMode.setStatus("current")
_Me1200QosIfConfigQceKeyType_Type = ME1200VcapKeyType
_Me1200QosIfConfigQceKeyType_Object = MibTableColumn
me1200QosIfConfigQceKeyType = _Me1200QosIfConfigQceKeyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 1, 1, 16),
    _Me1200QosIfConfigQceKeyType_Type()
)
me1200QosIfConfigQceKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfConfigQceKeyType.setStatus("current")
_Me1200QosIfTagToCosTable_Object = MibTable
me1200QosIfTagToCosTable = _Me1200QosIfTagToCosTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    me1200QosIfTagToCosTable.setStatus("current")
_Me1200QosIfTagToCosEntry_Object = MibTableRow
me1200QosIfTagToCosEntry = _Me1200QosIfTagToCosEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 2, 1)
)
me1200QosIfTagToCosEntry.setIndexNames(
    (0, "ME1200-QOS-MIB", "me1200QosIfTagToCosIfIndex"),
    (0, "ME1200-QOS-MIB", "me1200QosIfTagToCosPcp"),
    (0, "ME1200-QOS-MIB", "me1200QosIfTagToCosDei"),
)
if mibBuilder.loadTexts:
    me1200QosIfTagToCosEntry.setStatus("current")
_Me1200QosIfTagToCosIfIndex_Type = ME1200InterfaceIndex
_Me1200QosIfTagToCosIfIndex_Object = MibTableColumn
me1200QosIfTagToCosIfIndex = _Me1200QosIfTagToCosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 2, 1, 1),
    _Me1200QosIfTagToCosIfIndex_Type()
)
me1200QosIfTagToCosIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosIfTagToCosIfIndex.setStatus("current")


class _Me1200QosIfTagToCosPcp_Type(Integer32):
    """Custom type me1200QosIfTagToCosPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Me1200QosIfTagToCosPcp_Type.__name__ = "Integer32"
_Me1200QosIfTagToCosPcp_Object = MibTableColumn
me1200QosIfTagToCosPcp = _Me1200QosIfTagToCosPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 2, 1, 2),
    _Me1200QosIfTagToCosPcp_Type()
)
me1200QosIfTagToCosPcp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosIfTagToCosPcp.setStatus("current")


class _Me1200QosIfTagToCosDei_Type(Integer32):
    """Custom type me1200QosIfTagToCosDei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Me1200QosIfTagToCosDei_Type.__name__ = "Integer32"
_Me1200QosIfTagToCosDei_Object = MibTableColumn
me1200QosIfTagToCosDei = _Me1200QosIfTagToCosDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 2, 1, 3),
    _Me1200QosIfTagToCosDei_Type()
)
me1200QosIfTagToCosDei.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosIfTagToCosDei.setStatus("current")
_Me1200QosIfTagToCosCos_Type = Unsigned32
_Me1200QosIfTagToCosCos_Object = MibTableColumn
me1200QosIfTagToCosCos = _Me1200QosIfTagToCosCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 2, 1, 4),
    _Me1200QosIfTagToCosCos_Type()
)
me1200QosIfTagToCosCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfTagToCosCos.setStatus("current")
_Me1200QosIfTagToCosDpl_Type = ME1200Unsigned8
_Me1200QosIfTagToCosDpl_Object = MibTableColumn
me1200QosIfTagToCosDpl = _Me1200QosIfTagToCosDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 2, 1, 5),
    _Me1200QosIfTagToCosDpl_Type()
)
me1200QosIfTagToCosDpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfTagToCosDpl.setStatus("current")
_Me1200QosIfCosToTagTable_Object = MibTable
me1200QosIfCosToTagTable = _Me1200QosIfCosToTagTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    me1200QosIfCosToTagTable.setStatus("current")
_Me1200QosIfCosToTagEntry_Object = MibTableRow
me1200QosIfCosToTagEntry = _Me1200QosIfCosToTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 3, 1)
)
me1200QosIfCosToTagEntry.setIndexNames(
    (0, "ME1200-QOS-MIB", "me1200QosIfCosToTagIfIndex"),
    (0, "ME1200-QOS-MIB", "me1200QosIfCosToTagCos"),
    (0, "ME1200-QOS-MIB", "me1200QosIfCosToTagDpl"),
)
if mibBuilder.loadTexts:
    me1200QosIfCosToTagEntry.setStatus("current")
_Me1200QosIfCosToTagIfIndex_Type = ME1200InterfaceIndex
_Me1200QosIfCosToTagIfIndex_Object = MibTableColumn
me1200QosIfCosToTagIfIndex = _Me1200QosIfCosToTagIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 3, 1, 1),
    _Me1200QosIfCosToTagIfIndex_Type()
)
me1200QosIfCosToTagIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosIfCosToTagIfIndex.setStatus("current")


class _Me1200QosIfCosToTagCos_Type(Integer32):
    """Custom type me1200QosIfCosToTagCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Me1200QosIfCosToTagCos_Type.__name__ = "Integer32"
_Me1200QosIfCosToTagCos_Object = MibTableColumn
me1200QosIfCosToTagCos = _Me1200QosIfCosToTagCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 3, 1, 2),
    _Me1200QosIfCosToTagCos_Type()
)
me1200QosIfCosToTagCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosIfCosToTagCos.setStatus("current")


class _Me1200QosIfCosToTagDpl_Type(Integer32):
    """Custom type me1200QosIfCosToTagDpl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Me1200QosIfCosToTagDpl_Type.__name__ = "Integer32"
_Me1200QosIfCosToTagDpl_Object = MibTableColumn
me1200QosIfCosToTagDpl = _Me1200QosIfCosToTagDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 3, 1, 3),
    _Me1200QosIfCosToTagDpl_Type()
)
me1200QosIfCosToTagDpl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosIfCosToTagDpl.setStatus("current")
_Me1200QosIfCosToTagPcp_Type = Unsigned32
_Me1200QosIfCosToTagPcp_Object = MibTableColumn
me1200QosIfCosToTagPcp = _Me1200QosIfCosToTagPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 3, 1, 4),
    _Me1200QosIfCosToTagPcp_Type()
)
me1200QosIfCosToTagPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfCosToTagPcp.setStatus("current")
_Me1200QosIfCosToTagDei_Type = ME1200Unsigned8
_Me1200QosIfCosToTagDei_Object = MibTableColumn
me1200QosIfCosToTagDei = _Me1200QosIfCosToTagDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 3, 1, 5),
    _Me1200QosIfCosToTagDei_Type()
)
me1200QosIfCosToTagDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfCosToTagDei.setStatus("current")
_Me1200QosIfPolicerTable_Object = MibTable
me1200QosIfPolicerTable = _Me1200QosIfPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    me1200QosIfPolicerTable.setStatus("current")
_Me1200QosIfPolicerEntry_Object = MibTableRow
me1200QosIfPolicerEntry = _Me1200QosIfPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 4, 1)
)
me1200QosIfPolicerEntry.setIndexNames(
    (0, "ME1200-QOS-MIB", "me1200QosIfPolicerIfIndex"),
)
if mibBuilder.loadTexts:
    me1200QosIfPolicerEntry.setStatus("current")
_Me1200QosIfPolicerIfIndex_Type = ME1200InterfaceIndex
_Me1200QosIfPolicerIfIndex_Object = MibTableColumn
me1200QosIfPolicerIfIndex = _Me1200QosIfPolicerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 4, 1, 1),
    _Me1200QosIfPolicerIfIndex_Type()
)
me1200QosIfPolicerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosIfPolicerIfIndex.setStatus("current")
_Me1200QosIfPolicerEnable_Type = TruthValue
_Me1200QosIfPolicerEnable_Object = MibTableColumn
me1200QosIfPolicerEnable = _Me1200QosIfPolicerEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 4, 1, 2),
    _Me1200QosIfPolicerEnable_Type()
)
me1200QosIfPolicerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfPolicerEnable.setStatus("current")
_Me1200QosIfPolicerFrameRate_Type = TruthValue
_Me1200QosIfPolicerFrameRate_Object = MibTableColumn
me1200QosIfPolicerFrameRate = _Me1200QosIfPolicerFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 4, 1, 3),
    _Me1200QosIfPolicerFrameRate_Type()
)
me1200QosIfPolicerFrameRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfPolicerFrameRate.setStatus("current")
_Me1200QosIfPolicerFlowControl_Type = TruthValue
_Me1200QosIfPolicerFlowControl_Object = MibTableColumn
me1200QosIfPolicerFlowControl = _Me1200QosIfPolicerFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 4, 1, 4),
    _Me1200QosIfPolicerFlowControl_Type()
)
me1200QosIfPolicerFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfPolicerFlowControl.setStatus("current")
_Me1200QosIfPolicerCir_Type = Unsigned32
_Me1200QosIfPolicerCir_Object = MibTableColumn
me1200QosIfPolicerCir = _Me1200QosIfPolicerCir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 4, 1, 5),
    _Me1200QosIfPolicerCir_Type()
)
me1200QosIfPolicerCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfPolicerCir.setStatus("current")
_Me1200QosIfQueuePolicerTable_Object = MibTable
me1200QosIfQueuePolicerTable = _Me1200QosIfQueuePolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    me1200QosIfQueuePolicerTable.setStatus("current")
_Me1200QosIfQueuePolicerEntry_Object = MibTableRow
me1200QosIfQueuePolicerEntry = _Me1200QosIfQueuePolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 5, 1)
)
me1200QosIfQueuePolicerEntry.setIndexNames(
    (0, "ME1200-QOS-MIB", "me1200QosIfQueuePolicerIfIndex"),
    (0, "ME1200-QOS-MIB", "me1200QosIfQueuePolicerQueue"),
)
if mibBuilder.loadTexts:
    me1200QosIfQueuePolicerEntry.setStatus("current")
_Me1200QosIfQueuePolicerIfIndex_Type = ME1200InterfaceIndex
_Me1200QosIfQueuePolicerIfIndex_Object = MibTableColumn
me1200QosIfQueuePolicerIfIndex = _Me1200QosIfQueuePolicerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 5, 1, 1),
    _Me1200QosIfQueuePolicerIfIndex_Type()
)
me1200QosIfQueuePolicerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosIfQueuePolicerIfIndex.setStatus("current")


class _Me1200QosIfQueuePolicerQueue_Type(Integer32):
    """Custom type me1200QosIfQueuePolicerQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Me1200QosIfQueuePolicerQueue_Type.__name__ = "Integer32"
_Me1200QosIfQueuePolicerQueue_Object = MibTableColumn
me1200QosIfQueuePolicerQueue = _Me1200QosIfQueuePolicerQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 5, 1, 2),
    _Me1200QosIfQueuePolicerQueue_Type()
)
me1200QosIfQueuePolicerQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosIfQueuePolicerQueue.setStatus("current")
_Me1200QosIfQueuePolicerEnable_Type = TruthValue
_Me1200QosIfQueuePolicerEnable_Object = MibTableColumn
me1200QosIfQueuePolicerEnable = _Me1200QosIfQueuePolicerEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 5, 1, 3),
    _Me1200QosIfQueuePolicerEnable_Type()
)
me1200QosIfQueuePolicerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfQueuePolicerEnable.setStatus("current")
_Me1200QosIfQueuePolicerCir_Type = Unsigned32
_Me1200QosIfQueuePolicerCir_Object = MibTableColumn
me1200QosIfQueuePolicerCir = _Me1200QosIfQueuePolicerCir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 5, 1, 6),
    _Me1200QosIfQueuePolicerCir_Type()
)
me1200QosIfQueuePolicerCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfQueuePolicerCir.setStatus("current")
_Me1200QosIfShaperTable_Object = MibTable
me1200QosIfShaperTable = _Me1200QosIfShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    me1200QosIfShaperTable.setStatus("current")
_Me1200QosIfShaperEntry_Object = MibTableRow
me1200QosIfShaperEntry = _Me1200QosIfShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 6, 1)
)
me1200QosIfShaperEntry.setIndexNames(
    (0, "ME1200-QOS-MIB", "me1200QosIfShaperIfIndex"),
)
if mibBuilder.loadTexts:
    me1200QosIfShaperEntry.setStatus("current")
_Me1200QosIfShaperIfIndex_Type = ME1200InterfaceIndex
_Me1200QosIfShaperIfIndex_Object = MibTableColumn
me1200QosIfShaperIfIndex = _Me1200QosIfShaperIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 6, 1, 1),
    _Me1200QosIfShaperIfIndex_Type()
)
me1200QosIfShaperIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosIfShaperIfIndex.setStatus("current")
_Me1200QosIfShaperEnable_Type = TruthValue
_Me1200QosIfShaperEnable_Object = MibTableColumn
me1200QosIfShaperEnable = _Me1200QosIfShaperEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 6, 1, 2),
    _Me1200QosIfShaperEnable_Type()
)
me1200QosIfShaperEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfShaperEnable.setStatus("current")
_Me1200QosIfShaperCir_Type = Unsigned32
_Me1200QosIfShaperCir_Object = MibTableColumn
me1200QosIfShaperCir = _Me1200QosIfShaperCir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 6, 1, 3),
    _Me1200QosIfShaperCir_Type()
)
me1200QosIfShaperCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfShaperCir.setStatus("current")
_Me1200QosIfQueueShaperTable_Object = MibTable
me1200QosIfQueueShaperTable = _Me1200QosIfQueueShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 7)
)
if mibBuilder.loadTexts:
    me1200QosIfQueueShaperTable.setStatus("current")
_Me1200QosIfQueueShaperEntry_Object = MibTableRow
me1200QosIfQueueShaperEntry = _Me1200QosIfQueueShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 7, 1)
)
me1200QosIfQueueShaperEntry.setIndexNames(
    (0, "ME1200-QOS-MIB", "me1200QosIfQueueShaperIfIndex"),
    (0, "ME1200-QOS-MIB", "me1200QosIfQueueShaperQueue"),
)
if mibBuilder.loadTexts:
    me1200QosIfQueueShaperEntry.setStatus("current")
_Me1200QosIfQueueShaperIfIndex_Type = ME1200InterfaceIndex
_Me1200QosIfQueueShaperIfIndex_Object = MibTableColumn
me1200QosIfQueueShaperIfIndex = _Me1200QosIfQueueShaperIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 7, 1, 1),
    _Me1200QosIfQueueShaperIfIndex_Type()
)
me1200QosIfQueueShaperIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosIfQueueShaperIfIndex.setStatus("current")


class _Me1200QosIfQueueShaperQueue_Type(Integer32):
    """Custom type me1200QosIfQueueShaperQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Me1200QosIfQueueShaperQueue_Type.__name__ = "Integer32"
_Me1200QosIfQueueShaperQueue_Object = MibTableColumn
me1200QosIfQueueShaperQueue = _Me1200QosIfQueueShaperQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 7, 1, 2),
    _Me1200QosIfQueueShaperQueue_Type()
)
me1200QosIfQueueShaperQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosIfQueueShaperQueue.setStatus("current")
_Me1200QosIfQueueShaperEnable_Type = TruthValue
_Me1200QosIfQueueShaperEnable_Object = MibTableColumn
me1200QosIfQueueShaperEnable = _Me1200QosIfQueueShaperEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 7, 1, 3),
    _Me1200QosIfQueueShaperEnable_Type()
)
me1200QosIfQueueShaperEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfQueueShaperEnable.setStatus("current")
_Me1200QosIfQueueShaperExcess_Type = TruthValue
_Me1200QosIfQueueShaperExcess_Object = MibTableColumn
me1200QosIfQueueShaperExcess = _Me1200QosIfQueueShaperExcess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 7, 1, 4),
    _Me1200QosIfQueueShaperExcess_Type()
)
me1200QosIfQueueShaperExcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfQueueShaperExcess.setStatus("current")
_Me1200QosIfQueueShaperCir_Type = Unsigned32
_Me1200QosIfQueueShaperCir_Object = MibTableColumn
me1200QosIfQueueShaperCir = _Me1200QosIfQueueShaperCir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 7, 1, 5),
    _Me1200QosIfQueueShaperCir_Type()
)
me1200QosIfQueueShaperCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfQueueShaperCir.setStatus("current")
_Me1200QosIfSchedulerTable_Object = MibTable
me1200QosIfSchedulerTable = _Me1200QosIfSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    me1200QosIfSchedulerTable.setStatus("current")
_Me1200QosIfSchedulerEntry_Object = MibTableRow
me1200QosIfSchedulerEntry = _Me1200QosIfSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 8, 1)
)
me1200QosIfSchedulerEntry.setIndexNames(
    (0, "ME1200-QOS-MIB", "me1200QosIfSchedulerIfIndex"),
    (0, "ME1200-QOS-MIB", "me1200QosIfSchedulerQueue"),
)
if mibBuilder.loadTexts:
    me1200QosIfSchedulerEntry.setStatus("current")
_Me1200QosIfSchedulerIfIndex_Type = ME1200InterfaceIndex
_Me1200QosIfSchedulerIfIndex_Object = MibTableColumn
me1200QosIfSchedulerIfIndex = _Me1200QosIfSchedulerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 8, 1, 1),
    _Me1200QosIfSchedulerIfIndex_Type()
)
me1200QosIfSchedulerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosIfSchedulerIfIndex.setStatus("current")


class _Me1200QosIfSchedulerQueue_Type(Integer32):
    """Custom type me1200QosIfSchedulerQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Me1200QosIfSchedulerQueue_Type.__name__ = "Integer32"
_Me1200QosIfSchedulerQueue_Object = MibTableColumn
me1200QosIfSchedulerQueue = _Me1200QosIfSchedulerQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 8, 1, 2),
    _Me1200QosIfSchedulerQueue_Type()
)
me1200QosIfSchedulerQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosIfSchedulerQueue.setStatus("current")
_Me1200QosIfSchedulerWeight_Type = ME1200Percent
_Me1200QosIfSchedulerWeight_Object = MibTableColumn
me1200QosIfSchedulerWeight = _Me1200QosIfSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 2, 2, 8, 1, 3),
    _Me1200QosIfSchedulerWeight_Type()
)
me1200QosIfSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosIfSchedulerWeight.setStatus("current")
_Me1200QosStatus_ObjectIdentity = ObjectIdentity
me1200QosStatus = _Me1200QosStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 3)
)
_Me1200QosStatusGlobals_ObjectIdentity = ObjectIdentity
me1200QosStatusGlobals = _Me1200QosStatusGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 3, 1)
)
_Me1200QosStatusQceTable_Object = MibTable
me1200QosStatusQceTable = _Me1200QosStatusQceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    me1200QosStatusQceTable.setStatus("current")
_Me1200QosStatusQceEntry_Object = MibTableRow
me1200QosStatusQceEntry = _Me1200QosStatusQceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 3, 1, 1, 1)
)
me1200QosStatusQceEntry.setIndexNames(
    (0, "ME1200-QOS-MIB", "me1200QosStatusQceIndex"),
)
if mibBuilder.loadTexts:
    me1200QosStatusQceEntry.setStatus("current")


class _Me1200QosStatusQceIndex_Type(Integer32):
    """Custom type me1200QosStatusQceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200QosStatusQceIndex_Type.__name__ = "Integer32"
_Me1200QosStatusQceIndex_Object = MibTableColumn
me1200QosStatusQceIndex = _Me1200QosStatusQceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 3, 1, 1, 1, 2),
    _Me1200QosStatusQceIndex_Type()
)
me1200QosStatusQceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosStatusQceIndex.setStatus("current")
_Me1200QosStatusQceUserId_Type = ME1200QceUserType
_Me1200QosStatusQceUserId_Object = MibTableColumn
me1200QosStatusQceUserId = _Me1200QosStatusQceUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 3, 1, 1, 1, 3),
    _Me1200QosStatusQceUserId_Type()
)
me1200QosStatusQceUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200QosStatusQceUserId.setStatus("current")
_Me1200QosStatusQceQceId_Type = Unsigned32
_Me1200QosStatusQceQceId_Object = MibTableColumn
me1200QosStatusQceQceId = _Me1200QosStatusQceQceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 3, 1, 1, 1, 4),
    _Me1200QosStatusQceQceId_Type()
)
me1200QosStatusQceQceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200QosStatusQceQceId.setStatus("current")
_Me1200QosStatusQceConflict_Type = TruthValue
_Me1200QosStatusQceConflict_Object = MibTableColumn
me1200QosStatusQceConflict = _Me1200QosStatusQceConflict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 3, 1, 1, 1, 100),
    _Me1200QosStatusQceConflict_Type()
)
me1200QosStatusQceConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200QosStatusQceConflict.setStatus("current")
_Me1200QosStatusInterface_ObjectIdentity = ObjectIdentity
me1200QosStatusInterface = _Me1200QosStatusInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 3, 2)
)
_Me1200QosStatusIfTable_Object = MibTable
me1200QosStatusIfTable = _Me1200QosStatusIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    me1200QosStatusIfTable.setStatus("current")
_Me1200QosStatusIfEntry_Object = MibTableRow
me1200QosStatusIfEntry = _Me1200QosStatusIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 3, 2, 1, 1)
)
me1200QosStatusIfEntry.setIndexNames(
    (0, "ME1200-QOS-MIB", "me1200QosStatusIfIfIndex"),
)
if mibBuilder.loadTexts:
    me1200QosStatusIfEntry.setStatus("current")
_Me1200QosStatusIfIfIndex_Type = ME1200InterfaceIndex
_Me1200QosStatusIfIfIndex_Object = MibTableColumn
me1200QosStatusIfIfIndex = _Me1200QosStatusIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 3, 2, 1, 1, 1),
    _Me1200QosStatusIfIfIndex_Type()
)
me1200QosStatusIfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosStatusIfIfIndex.setStatus("current")
_Me1200QosStatusIfCos_Type = Unsigned32
_Me1200QosStatusIfCos_Object = MibTableColumn
me1200QosStatusIfCos = _Me1200QosStatusIfCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 3, 2, 1, 1, 2),
    _Me1200QosStatusIfCos_Type()
)
me1200QosStatusIfCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200QosStatusIfCos.setStatus("current")
_Me1200QosStatusIfSchedulerTable_Object = MibTable
me1200QosStatusIfSchedulerTable = _Me1200QosStatusIfSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    me1200QosStatusIfSchedulerTable.setStatus("current")
_Me1200QosStatusIfSchedulerEntry_Object = MibTableRow
me1200QosStatusIfSchedulerEntry = _Me1200QosStatusIfSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 3, 2, 2, 1)
)
me1200QosStatusIfSchedulerEntry.setIndexNames(
    (0, "ME1200-QOS-MIB", "me1200QosStatusIfSchedulerIfIndex"),
    (0, "ME1200-QOS-MIB", "me1200QosStatusIfSchedulerQueue"),
)
if mibBuilder.loadTexts:
    me1200QosStatusIfSchedulerEntry.setStatus("current")
_Me1200QosStatusIfSchedulerIfIndex_Type = ME1200InterfaceIndex
_Me1200QosStatusIfSchedulerIfIndex_Object = MibTableColumn
me1200QosStatusIfSchedulerIfIndex = _Me1200QosStatusIfSchedulerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 3, 2, 2, 1, 1),
    _Me1200QosStatusIfSchedulerIfIndex_Type()
)
me1200QosStatusIfSchedulerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosStatusIfSchedulerIfIndex.setStatus("current")


class _Me1200QosStatusIfSchedulerQueue_Type(Integer32):
    """Custom type me1200QosStatusIfSchedulerQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Me1200QosStatusIfSchedulerQueue_Type.__name__ = "Integer32"
_Me1200QosStatusIfSchedulerQueue_Object = MibTableColumn
me1200QosStatusIfSchedulerQueue = _Me1200QosStatusIfSchedulerQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 3, 2, 2, 1, 2),
    _Me1200QosStatusIfSchedulerQueue_Type()
)
me1200QosStatusIfSchedulerQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200QosStatusIfSchedulerQueue.setStatus("current")
_Me1200QosStatusIfSchedulerWeight_Type = ME1200Percent
_Me1200QosStatusIfSchedulerWeight_Object = MibTableColumn
me1200QosStatusIfSchedulerWeight = _Me1200QosStatusIfSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 3, 2, 2, 1, 3),
    _Me1200QosStatusIfSchedulerWeight_Type()
)
me1200QosStatusIfSchedulerWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200QosStatusIfSchedulerWeight.setStatus("current")
_Me1200QosControl_ObjectIdentity = ObjectIdentity
me1200QosControl = _Me1200QosControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 4)
)
_Me1200QosControlGlobals_ObjectIdentity = ObjectIdentity
me1200QosControlGlobals = _Me1200QosControlGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 4, 1)
)
_Me1200QosControlGlobalsConflictResolve_Type = TruthValue
_Me1200QosControlGlobalsConflictResolve_Object = MibScalar
me1200QosControlGlobalsConflictResolve = _Me1200QosControlGlobalsConflictResolve_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 1, 4, 1, 1),
    _Me1200QosControlGlobalsConflictResolve_Type()
)
me1200QosControlGlobalsConflictResolve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200QosControlGlobalsConflictResolve.setStatus("current")
_Me1200QosMIBConformance_ObjectIdentity = ObjectIdentity
me1200QosMIBConformance = _Me1200QosMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3)
)
_Me1200QosMIBCompliances_ObjectIdentity = ObjectIdentity
me1200QosMIBCompliances = _Me1200QosMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 1)
)
_Me1200QosMIBGroups_ObjectIdentity = ObjectIdentity
me1200QosMIBGroups = _Me1200QosMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2)
)

# Managed Objects groups

me1200QosStormPolicerUnicastInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 1)
)
me1200QosStormPolicerUnicastInfoGroup.setObjects(
      *(("ME1200-QOS-MIB", "me1200QosStormPolicerUnicastEnable"),
        ("ME1200-QOS-MIB", "me1200QosStormPolicerUnicastRate"))
)
if mibBuilder.loadTexts:
    me1200QosStormPolicerUnicastInfoGroup.setStatus("current")

me1200QosStormPolicerMulticastInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 2)
)
me1200QosStormPolicerMulticastInfoGroup.setObjects(
      *(("ME1200-QOS-MIB", "me1200QosStormPolicerMulticastEnable"),
        ("ME1200-QOS-MIB", "me1200QosStormPolicerMulticastRate"))
)
if mibBuilder.loadTexts:
    me1200QosStormPolicerMulticastInfoGroup.setStatus("current")

me1200QosStormPolicerBroadcastInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 3)
)
me1200QosStormPolicerBroadcastInfoGroup.setObjects(
      *(("ME1200-QOS-MIB", "me1200QosStormPolicerBroadcastEnable"),
        ("ME1200-QOS-MIB", "me1200QosStormPolicerBroadcastRate"))
)
if mibBuilder.loadTexts:
    me1200QosStormPolicerBroadcastInfoGroup.setStatus("current")

me1200QosWredTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 4)
)
me1200QosWredTableInfoGroup.setObjects(
      *(("ME1200-QOS-MIB", "me1200QosWredEnable"),
        ("ME1200-QOS-MIB", "me1200QosWredMinimumFillLevel"),
        ("ME1200-QOS-MIB", "me1200QosWredMaximum"),
        ("ME1200-QOS-MIB", "me1200QosWredMaxSelector"))
)
if mibBuilder.loadTexts:
    me1200QosWredTableInfoGroup.setStatus("current")

me1200QosDscpTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 5)
)
me1200QosDscpTableInfoGroup.setObjects(
      *(("ME1200-QOS-MIB", "me1200QosDscpTrust"),
        ("ME1200-QOS-MIB", "me1200QosDscpCos"),
        ("ME1200-QOS-MIB", "me1200QosDscpDpl"),
        ("ME1200-QOS-MIB", "me1200QosDscpIngressTranslation"),
        ("ME1200-QOS-MIB", "me1200QosDscpClassify"),
        ("ME1200-QOS-MIB", "me1200QosDscpEgressTranslation"),
        ("ME1200-QOS-MIB", "me1200QosDscpEgressTranslationDp1"))
)
if mibBuilder.loadTexts:
    me1200QosDscpTableInfoGroup.setStatus("current")

me1200QosCosToDscpTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 6)
)
me1200QosCosToDscpTableInfoGroup.setObjects(
      *(("ME1200-QOS-MIB", "me1200QosCosToDscpDscp"),
        ("ME1200-QOS-MIB", "me1200QosCosToDscpDscpDp1"))
)
if mibBuilder.loadTexts:
    me1200QosCosToDscpTableInfoGroup.setStatus("current")

me1200QosQceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 7)
)
me1200QosQceTableInfoGroup.setObjects(
      *(("ME1200-QOS-MIB", "me1200QosQceNextQceId"),
        ("ME1200-QOS-MIB", "me1200QosQcePortList"),
        ("ME1200-QOS-MIB", "me1200QosQceDestMacType"),
        ("ME1200-QOS-MIB", "me1200QosQceDestMac"),
        ("ME1200-QOS-MIB", "me1200QosQceDestMacMask"),
        ("ME1200-QOS-MIB", "me1200QosQceSrcMac"),
        ("ME1200-QOS-MIB", "me1200QosQceSrcMacMask"),
        ("ME1200-QOS-MIB", "me1200QosQceVlanTagType"),
        ("ME1200-QOS-MIB", "me1200QosQceVlanIdOp"),
        ("ME1200-QOS-MIB", "me1200QosQceVlanId"),
        ("ME1200-QOS-MIB", "me1200QosQceVlanIdRange"),
        ("ME1200-QOS-MIB", "me1200QosQcePcp"),
        ("ME1200-QOS-MIB", "me1200QosQceDei"),
        ("ME1200-QOS-MIB", "me1200QosQceInnerVlanTagType"),
        ("ME1200-QOS-MIB", "me1200QosQceInnerVlanIdOp"),
        ("ME1200-QOS-MIB", "me1200QosQceInnerVlanId"),
        ("ME1200-QOS-MIB", "me1200QosQceInnerVlanIdRange"),
        ("ME1200-QOS-MIB", "me1200QosQceInnerPcp"),
        ("ME1200-QOS-MIB", "me1200QosQceInnerDei"),
        ("ME1200-QOS-MIB", "me1200QosQceFrameType"),
        ("ME1200-QOS-MIB", "me1200QosQceEtype"),
        ("ME1200-QOS-MIB", "me1200QosQceLlcDsap"),
        ("ME1200-QOS-MIB", "me1200QosQceLlcDsapMask"),
        ("ME1200-QOS-MIB", "me1200QosQceLlcSsap"),
        ("ME1200-QOS-MIB", "me1200QosQceLlcSsapMask"),
        ("ME1200-QOS-MIB", "me1200QosQceLlcControl"),
        ("ME1200-QOS-MIB", "me1200QosQceLlcControlMask"),
        ("ME1200-QOS-MIB", "me1200QosQceSnapPid"),
        ("ME1200-QOS-MIB", "me1200QosQceSnapPidMask"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv4Fragment"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv4DscpOp"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv4Dscp"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv4DscpRange"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv4Protocol"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv4ProtocolMask"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv4SrcIp"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv4SrcIpMask"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv4DestIp"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv4DestIpMask"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv4SrcPortOp"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv4SrcPort"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv4SrcPortRange"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv4DestPortOp"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv4DestPort"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv4DestPortRange"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv6DscpOp"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv6Dscp"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv6DscpRange"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv6Protocol"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv6ProtocolMask"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv6SrcIp"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv6SrcIpMask"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv6DestIp"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv6DestIpMask"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv6SrcPortOp"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv6SrcPort"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv6SrcPortRange"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv6DestPortOp"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv6DestPort"),
        ("ME1200-QOS-MIB", "me1200QosQceIpv6DestPortRange"),
        ("ME1200-QOS-MIB", "me1200QosQceActionCosEnable"),
        ("ME1200-QOS-MIB", "me1200QosQceActionCos"),
        ("ME1200-QOS-MIB", "me1200QosQceActionDplEnable"),
        ("ME1200-QOS-MIB", "me1200QosQceActionDpl"),
        ("ME1200-QOS-MIB", "me1200QosQceActionDscpEnable"),
        ("ME1200-QOS-MIB", "me1200QosQceActionDscp"),
        ("ME1200-QOS-MIB", "me1200QosQceActionPcpDeiEnable"),
        ("ME1200-QOS-MIB", "me1200QosQceActionPcp"),
        ("ME1200-QOS-MIB", "me1200QosQceActionDei"),
        ("ME1200-QOS-MIB", "me1200QosQceActionPolicyEnable"),
        ("ME1200-QOS-MIB", "me1200QosQceActionPolicy"),
        ("ME1200-QOS-MIB", "me1200QosQceAction"))
)
if mibBuilder.loadTexts:
    me1200QosQceTableInfoGroup.setStatus("current")

me1200QosQceTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 8)
)
me1200QosQceTableRowEditorInfoGroup.setObjects(
      *(("ME1200-QOS-MIB", "me1200QosQceTableRowEditorQceId"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorNextQceId"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorPortList"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorDestMacType"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorDestMac"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorDestMacMask"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorSrcMac"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorSrcMacMask"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorVlanTagType"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorVlanIdOp"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorVlanId"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorVlanIdRange"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorPcp"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorDei"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorInnerVlanTagType"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorInnerVlanIdOp"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorInnerVlanId"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorInnerVlanIdRange"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorInnerPcp"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorInnerDei"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorFrameType"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorEtype"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorLlcDsap"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorLlcDsapMask"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorLlcSsap"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorLlcSsapMask"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorLlcControl"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorLlcControlMask"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorSnapPid"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorSnapPidMask"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv4Fragment"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv4DscpOp"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv4Dscp"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv4DscpRange"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv4Protocol"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv4ProtocolMask"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv4SrcIp"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv4SrcIpMask"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv4DestIp"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv4DestIpMask"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv4SrcPortOp"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv4SrcPort"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv4SrcPortRange"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv4DestPortOp"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv4DestPort"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv4DestPortRange"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv6DscpOp"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv6Dscp"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv6DscpRange"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv6Protocol"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv6ProtocolMask"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv6SrcIp"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv6SrcIpMask"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv6DestIp"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv6DestIpMask"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv6SrcPortOp"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv6SrcPort"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv6SrcPortRange"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv6DestPortOp"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv6DestPort"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorIpv6DestPortRange"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorActionCosEnable"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorActionCos"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorActionDplEnable"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorActionDpl"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorActionDscpEnable"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorActionDscp"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorActionPcpDeiEnable"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorActionPcp"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorActionDei"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorActionPolicyEnable"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorActionPolicy"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200QosQceTableRowEditorInfoGroup.setStatus("current")

me1200QosQcePrecedenceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 9)
)
me1200QosQcePrecedenceTableInfoGroup.setObjects(
    ("ME1200-QOS-MIB", "me1200QosQcePrecedenceQceId")
)
if mibBuilder.loadTexts:
    me1200QosQcePrecedenceTableInfoGroup.setStatus("current")

me1200QosIfConfigTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 10)
)
me1200QosIfConfigTableInfoGroup.setObjects(
      *(("ME1200-QOS-MIB", "me1200QosIfConfigCos"),
        ("ME1200-QOS-MIB", "me1200QosIfConfigDpl"),
        ("ME1200-QOS-MIB", "me1200QosIfConfigPcp"),
        ("ME1200-QOS-MIB", "me1200QosIfConfigDei"),
        ("ME1200-QOS-MIB", "me1200QosIfConfigTrustTag"),
        ("ME1200-QOS-MIB", "me1200QosIfConfigTrustDscp"),
        ("ME1200-QOS-MIB", "me1200QosIfConfigDwrrCount"),
        ("ME1200-QOS-MIB", "me1200QosIfConfigTagRemarkingMode"),
        ("ME1200-QOS-MIB", "me1200QosIfConfigTagPcp"),
        ("ME1200-QOS-MIB", "me1200QosIfConfigTagDei"),
        ("ME1200-QOS-MIB", "me1200QosIfConfigDscpTranslate"),
        ("ME1200-QOS-MIB", "me1200QosIfConfigDscpClassify"),
        ("ME1200-QOS-MIB", "me1200QosIfConfigDscpRemark"),
        ("ME1200-QOS-MIB", "me1200QosIfConfigQceAddressMode"),
        ("ME1200-QOS-MIB", "me1200QosIfConfigQceKeyType"))
)
if mibBuilder.loadTexts:
    me1200QosIfConfigTableInfoGroup.setStatus("current")

me1200QosIfTagToCosTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 11)
)
me1200QosIfTagToCosTableInfoGroup.setObjects(
      *(("ME1200-QOS-MIB", "me1200QosIfTagToCosCos"),
        ("ME1200-QOS-MIB", "me1200QosIfTagToCosDpl"))
)
if mibBuilder.loadTexts:
    me1200QosIfTagToCosTableInfoGroup.setStatus("current")

me1200QosIfCosToTagTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 12)
)
me1200QosIfCosToTagTableInfoGroup.setObjects(
      *(("ME1200-QOS-MIB", "me1200QosIfCosToTagPcp"),
        ("ME1200-QOS-MIB", "me1200QosIfCosToTagDei"))
)
if mibBuilder.loadTexts:
    me1200QosIfCosToTagTableInfoGroup.setStatus("current")

me1200QosIfPolicerTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 13)
)
me1200QosIfPolicerTableInfoGroup.setObjects(
      *(("ME1200-QOS-MIB", "me1200QosIfPolicerEnable"),
        ("ME1200-QOS-MIB", "me1200QosIfPolicerFrameRate"),
        ("ME1200-QOS-MIB", "me1200QosIfPolicerFlowControl"),
        ("ME1200-QOS-MIB", "me1200QosIfPolicerCir"))
)
if mibBuilder.loadTexts:
    me1200QosIfPolicerTableInfoGroup.setStatus("current")

me1200QosIfQueuePolicerTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 14)
)
me1200QosIfQueuePolicerTableInfoGroup.setObjects(
      *(("ME1200-QOS-MIB", "me1200QosIfQueuePolicerEnable"),
        ("ME1200-QOS-MIB", "me1200QosIfQueuePolicerCir"))
)
if mibBuilder.loadTexts:
    me1200QosIfQueuePolicerTableInfoGroup.setStatus("current")

me1200QosIfShaperTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 15)
)
me1200QosIfShaperTableInfoGroup.setObjects(
      *(("ME1200-QOS-MIB", "me1200QosIfShaperEnable"),
        ("ME1200-QOS-MIB", "me1200QosIfShaperCir"))
)
if mibBuilder.loadTexts:
    me1200QosIfShaperTableInfoGroup.setStatus("current")

me1200QosIfQueueShaperTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 16)
)
me1200QosIfQueueShaperTableInfoGroup.setObjects(
      *(("ME1200-QOS-MIB", "me1200QosIfQueueShaperEnable"),
        ("ME1200-QOS-MIB", "me1200QosIfQueueShaperExcess"),
        ("ME1200-QOS-MIB", "me1200QosIfQueueShaperCir"))
)
if mibBuilder.loadTexts:
    me1200QosIfQueueShaperTableInfoGroup.setStatus("current")

me1200QosIfSchedulerTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 17)
)
me1200QosIfSchedulerTableInfoGroup.setObjects(
    ("ME1200-QOS-MIB", "me1200QosIfSchedulerWeight")
)
if mibBuilder.loadTexts:
    me1200QosIfSchedulerTableInfoGroup.setStatus("current")

me1200QosStatusQceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 18)
)
me1200QosStatusQceTableInfoGroup.setObjects(
      *(("ME1200-QOS-MIB", "me1200QosStatusQceUserId"),
        ("ME1200-QOS-MIB", "me1200QosStatusQceQceId"),
        ("ME1200-QOS-MIB", "me1200QosStatusQceConflict"))
)
if mibBuilder.loadTexts:
    me1200QosStatusQceTableInfoGroup.setStatus("current")

me1200QosStatusIfTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 19)
)
me1200QosStatusIfTableInfoGroup.setObjects(
    ("ME1200-QOS-MIB", "me1200QosStatusIfCos")
)
if mibBuilder.loadTexts:
    me1200QosStatusIfTableInfoGroup.setStatus("current")

me1200QosStatusIfSchedulerTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 20)
)
me1200QosStatusIfSchedulerTableInfoGroup.setObjects(
    ("ME1200-QOS-MIB", "me1200QosStatusIfSchedulerWeight")
)
if mibBuilder.loadTexts:
    me1200QosStatusIfSchedulerTableInfoGroup.setStatus("current")

me1200QosControlGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 2, 21)
)
me1200QosControlGlobalsInfoGroup.setObjects(
    ("ME1200-QOS-MIB", "me1200QosControlGlobalsConflictResolve")
)
if mibBuilder.loadTexts:
    me1200QosControlGlobalsInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200QosMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 14, 3, 1, 1)
)
me1200QosMIBCompliance.setObjects(
      *(("ME1200-QOS-MIB", "me1200QosStormPolicerUnicastInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosStormPolicerMulticastInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosStormPolicerBroadcastInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosWredTableInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosDscpTableInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosCosToDscpTableInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosQceTableInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosQceTableRowEditorInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosQcePrecedenceTableInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosIfConfigTableInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosIfTagToCosTableInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosIfCosToTagTableInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosIfPolicerTableInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosIfQueuePolicerTableInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosIfShaperTableInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosIfQueueShaperTableInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosIfSchedulerTableInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosStatusQceTableInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosStatusIfTableInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosStatusIfSchedulerTableInfoGroup"),
        ("ME1200-QOS-MIB", "me1200QosControlGlobalsInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200QosMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-QOS-MIB",
    **{"ME1200ASRType": ME1200ASRType,
       "ME1200BitType": ME1200BitType,
       "ME1200DestMacType": ME1200DestMacType,
       "ME1200DscpClassify": ME1200DscpClassify,
       "ME1200DscpRemark": ME1200DscpRemark,
       "ME1200MaxSelector": ME1200MaxSelector,
       "ME1200QceFrameType": ME1200QceFrameType,
       "ME1200QceUserType": ME1200QceUserType,
       "ME1200TagRemarkingMode": ME1200TagRemarkingMode,
       "ME1200VcapKeyType": ME1200VcapKeyType,
       "ME1200VlanTagPriority": ME1200VlanTagPriority,
       "ME1200VlanTagType": ME1200VlanTagType,
       "me1200QosMIB": me1200QosMIB,
       "me1200QosMIBObjects": me1200QosMIBObjects,
       "me1200QosConfig": me1200QosConfig,
       "me1200QosGlobals": me1200QosGlobals,
       "me1200QosStormPolicers": me1200QosStormPolicers,
       "me1200QosStormPolicerUnicast": me1200QosStormPolicerUnicast,
       "me1200QosStormPolicerUnicastEnable": me1200QosStormPolicerUnicastEnable,
       "me1200QosStormPolicerUnicastRate": me1200QosStormPolicerUnicastRate,
       "me1200QosStormPolicerMulticast": me1200QosStormPolicerMulticast,
       "me1200QosStormPolicerMulticastEnable": me1200QosStormPolicerMulticastEnable,
       "me1200QosStormPolicerMulticastRate": me1200QosStormPolicerMulticastRate,
       "me1200QosStormPolicerBroadcast": me1200QosStormPolicerBroadcast,
       "me1200QosStormPolicerBroadcastEnable": me1200QosStormPolicerBroadcastEnable,
       "me1200QosStormPolicerBroadcastRate": me1200QosStormPolicerBroadcastRate,
       "me1200QosWredTable": me1200QosWredTable,
       "me1200QosWredEntry": me1200QosWredEntry,
       "me1200QosWredQueue": me1200QosWredQueue,
       "me1200QosWredEnable": me1200QosWredEnable,
       "me1200QosWredMinimumFillLevel": me1200QosWredMinimumFillLevel,
       "me1200QosWredMaximum": me1200QosWredMaximum,
       "me1200QosWredMaxSelector": me1200QosWredMaxSelector,
       "me1200QosDscpTable": me1200QosDscpTable,
       "me1200QosDscpEntry": me1200QosDscpEntry,
       "me1200QosDscpDscp": me1200QosDscpDscp,
       "me1200QosDscpTrust": me1200QosDscpTrust,
       "me1200QosDscpCos": me1200QosDscpCos,
       "me1200QosDscpDpl": me1200QosDscpDpl,
       "me1200QosDscpIngressTranslation": me1200QosDscpIngressTranslation,
       "me1200QosDscpClassify": me1200QosDscpClassify,
       "me1200QosDscpEgressTranslation": me1200QosDscpEgressTranslation,
       "me1200QosDscpEgressTranslationDp1": me1200QosDscpEgressTranslationDp1,
       "me1200QosCosToDscpTable": me1200QosCosToDscpTable,
       "me1200QosCosToDscpEntry": me1200QosCosToDscpEntry,
       "me1200QosCosToDscpCos": me1200QosCosToDscpCos,
       "me1200QosCosToDscpDscp": me1200QosCosToDscpDscp,
       "me1200QosCosToDscpDscpDp1": me1200QosCosToDscpDscpDp1,
       "me1200QosQce": me1200QosQce,
       "me1200QosQceTable": me1200QosQceTable,
       "me1200QosQceEntry": me1200QosQceEntry,
       "me1200QosQceQceId": me1200QosQceQceId,
       "me1200QosQceNextQceId": me1200QosQceNextQceId,
       "me1200QosQcePortList": me1200QosQcePortList,
       "me1200QosQceDestMacType": me1200QosQceDestMacType,
       "me1200QosQceDestMac": me1200QosQceDestMac,
       "me1200QosQceDestMacMask": me1200QosQceDestMacMask,
       "me1200QosQceSrcMac": me1200QosQceSrcMac,
       "me1200QosQceSrcMacMask": me1200QosQceSrcMacMask,
       "me1200QosQceVlanTagType": me1200QosQceVlanTagType,
       "me1200QosQceVlanIdOp": me1200QosQceVlanIdOp,
       "me1200QosQceVlanId": me1200QosQceVlanId,
       "me1200QosQceVlanIdRange": me1200QosQceVlanIdRange,
       "me1200QosQcePcp": me1200QosQcePcp,
       "me1200QosQceDei": me1200QosQceDei,
       "me1200QosQceInnerVlanTagType": me1200QosQceInnerVlanTagType,
       "me1200QosQceInnerVlanIdOp": me1200QosQceInnerVlanIdOp,
       "me1200QosQceInnerVlanId": me1200QosQceInnerVlanId,
       "me1200QosQceInnerVlanIdRange": me1200QosQceInnerVlanIdRange,
       "me1200QosQceInnerPcp": me1200QosQceInnerPcp,
       "me1200QosQceInnerDei": me1200QosQceInnerDei,
       "me1200QosQceFrameType": me1200QosQceFrameType,
       "me1200QosQceEtype": me1200QosQceEtype,
       "me1200QosQceLlcDsap": me1200QosQceLlcDsap,
       "me1200QosQceLlcDsapMask": me1200QosQceLlcDsapMask,
       "me1200QosQceLlcSsap": me1200QosQceLlcSsap,
       "me1200QosQceLlcSsapMask": me1200QosQceLlcSsapMask,
       "me1200QosQceLlcControl": me1200QosQceLlcControl,
       "me1200QosQceLlcControlMask": me1200QosQceLlcControlMask,
       "me1200QosQceSnapPid": me1200QosQceSnapPid,
       "me1200QosQceSnapPidMask": me1200QosQceSnapPidMask,
       "me1200QosQceIpv4Fragment": me1200QosQceIpv4Fragment,
       "me1200QosQceIpv4DscpOp": me1200QosQceIpv4DscpOp,
       "me1200QosQceIpv4Dscp": me1200QosQceIpv4Dscp,
       "me1200QosQceIpv4DscpRange": me1200QosQceIpv4DscpRange,
       "me1200QosQceIpv4Protocol": me1200QosQceIpv4Protocol,
       "me1200QosQceIpv4ProtocolMask": me1200QosQceIpv4ProtocolMask,
       "me1200QosQceIpv4SrcIp": me1200QosQceIpv4SrcIp,
       "me1200QosQceIpv4SrcIpMask": me1200QosQceIpv4SrcIpMask,
       "me1200QosQceIpv4DestIp": me1200QosQceIpv4DestIp,
       "me1200QosQceIpv4DestIpMask": me1200QosQceIpv4DestIpMask,
       "me1200QosQceIpv4SrcPortOp": me1200QosQceIpv4SrcPortOp,
       "me1200QosQceIpv4SrcPort": me1200QosQceIpv4SrcPort,
       "me1200QosQceIpv4SrcPortRange": me1200QosQceIpv4SrcPortRange,
       "me1200QosQceIpv4DestPortOp": me1200QosQceIpv4DestPortOp,
       "me1200QosQceIpv4DestPort": me1200QosQceIpv4DestPort,
       "me1200QosQceIpv4DestPortRange": me1200QosQceIpv4DestPortRange,
       "me1200QosQceIpv6DscpOp": me1200QosQceIpv6DscpOp,
       "me1200QosQceIpv6Dscp": me1200QosQceIpv6Dscp,
       "me1200QosQceIpv6DscpRange": me1200QosQceIpv6DscpRange,
       "me1200QosQceIpv6Protocol": me1200QosQceIpv6Protocol,
       "me1200QosQceIpv6ProtocolMask": me1200QosQceIpv6ProtocolMask,
       "me1200QosQceIpv6SrcIp": me1200QosQceIpv6SrcIp,
       "me1200QosQceIpv6SrcIpMask": me1200QosQceIpv6SrcIpMask,
       "me1200QosQceIpv6DestIp": me1200QosQceIpv6DestIp,
       "me1200QosQceIpv6DestIpMask": me1200QosQceIpv6DestIpMask,
       "me1200QosQceIpv6SrcPortOp": me1200QosQceIpv6SrcPortOp,
       "me1200QosQceIpv6SrcPort": me1200QosQceIpv6SrcPort,
       "me1200QosQceIpv6SrcPortRange": me1200QosQceIpv6SrcPortRange,
       "me1200QosQceIpv6DestPortOp": me1200QosQceIpv6DestPortOp,
       "me1200QosQceIpv6DestPort": me1200QosQceIpv6DestPort,
       "me1200QosQceIpv6DestPortRange": me1200QosQceIpv6DestPortRange,
       "me1200QosQceActionCosEnable": me1200QosQceActionCosEnable,
       "me1200QosQceActionCos": me1200QosQceActionCos,
       "me1200QosQceActionDplEnable": me1200QosQceActionDplEnable,
       "me1200QosQceActionDpl": me1200QosQceActionDpl,
       "me1200QosQceActionDscpEnable": me1200QosQceActionDscpEnable,
       "me1200QosQceActionDscp": me1200QosQceActionDscp,
       "me1200QosQceActionPcpDeiEnable": me1200QosQceActionPcpDeiEnable,
       "me1200QosQceActionPcp": me1200QosQceActionPcp,
       "me1200QosQceActionDei": me1200QosQceActionDei,
       "me1200QosQceActionPolicyEnable": me1200QosQceActionPolicyEnable,
       "me1200QosQceActionPolicy": me1200QosQceActionPolicy,
       "me1200QosQceAction": me1200QosQceAction,
       "me1200QosQceTableRowEditor": me1200QosQceTableRowEditor,
       "me1200QosQceTableRowEditorQceId": me1200QosQceTableRowEditorQceId,
       "me1200QosQceTableRowEditorNextQceId": me1200QosQceTableRowEditorNextQceId,
       "me1200QosQceTableRowEditorPortList": me1200QosQceTableRowEditorPortList,
       "me1200QosQceTableRowEditorDestMacType": me1200QosQceTableRowEditorDestMacType,
       "me1200QosQceTableRowEditorDestMac": me1200QosQceTableRowEditorDestMac,
       "me1200QosQceTableRowEditorDestMacMask": me1200QosQceTableRowEditorDestMacMask,
       "me1200QosQceTableRowEditorSrcMac": me1200QosQceTableRowEditorSrcMac,
       "me1200QosQceTableRowEditorSrcMacMask": me1200QosQceTableRowEditorSrcMacMask,
       "me1200QosQceTableRowEditorVlanTagType": me1200QosQceTableRowEditorVlanTagType,
       "me1200QosQceTableRowEditorVlanIdOp": me1200QosQceTableRowEditorVlanIdOp,
       "me1200QosQceTableRowEditorVlanId": me1200QosQceTableRowEditorVlanId,
       "me1200QosQceTableRowEditorVlanIdRange": me1200QosQceTableRowEditorVlanIdRange,
       "me1200QosQceTableRowEditorPcp": me1200QosQceTableRowEditorPcp,
       "me1200QosQceTableRowEditorDei": me1200QosQceTableRowEditorDei,
       "me1200QosQceTableRowEditorInnerVlanTagType": me1200QosQceTableRowEditorInnerVlanTagType,
       "me1200QosQceTableRowEditorInnerVlanIdOp": me1200QosQceTableRowEditorInnerVlanIdOp,
       "me1200QosQceTableRowEditorInnerVlanId": me1200QosQceTableRowEditorInnerVlanId,
       "me1200QosQceTableRowEditorInnerVlanIdRange": me1200QosQceTableRowEditorInnerVlanIdRange,
       "me1200QosQceTableRowEditorInnerPcp": me1200QosQceTableRowEditorInnerPcp,
       "me1200QosQceTableRowEditorInnerDei": me1200QosQceTableRowEditorInnerDei,
       "me1200QosQceTableRowEditorFrameType": me1200QosQceTableRowEditorFrameType,
       "me1200QosQceTableRowEditorEtype": me1200QosQceTableRowEditorEtype,
       "me1200QosQceTableRowEditorLlcDsap": me1200QosQceTableRowEditorLlcDsap,
       "me1200QosQceTableRowEditorLlcDsapMask": me1200QosQceTableRowEditorLlcDsapMask,
       "me1200QosQceTableRowEditorLlcSsap": me1200QosQceTableRowEditorLlcSsap,
       "me1200QosQceTableRowEditorLlcSsapMask": me1200QosQceTableRowEditorLlcSsapMask,
       "me1200QosQceTableRowEditorLlcControl": me1200QosQceTableRowEditorLlcControl,
       "me1200QosQceTableRowEditorLlcControlMask": me1200QosQceTableRowEditorLlcControlMask,
       "me1200QosQceTableRowEditorSnapPid": me1200QosQceTableRowEditorSnapPid,
       "me1200QosQceTableRowEditorSnapPidMask": me1200QosQceTableRowEditorSnapPidMask,
       "me1200QosQceTableRowEditorIpv4Fragment": me1200QosQceTableRowEditorIpv4Fragment,
       "me1200QosQceTableRowEditorIpv4DscpOp": me1200QosQceTableRowEditorIpv4DscpOp,
       "me1200QosQceTableRowEditorIpv4Dscp": me1200QosQceTableRowEditorIpv4Dscp,
       "me1200QosQceTableRowEditorIpv4DscpRange": me1200QosQceTableRowEditorIpv4DscpRange,
       "me1200QosQceTableRowEditorIpv4Protocol": me1200QosQceTableRowEditorIpv4Protocol,
       "me1200QosQceTableRowEditorIpv4ProtocolMask": me1200QosQceTableRowEditorIpv4ProtocolMask,
       "me1200QosQceTableRowEditorIpv4SrcIp": me1200QosQceTableRowEditorIpv4SrcIp,
       "me1200QosQceTableRowEditorIpv4SrcIpMask": me1200QosQceTableRowEditorIpv4SrcIpMask,
       "me1200QosQceTableRowEditorIpv4DestIp": me1200QosQceTableRowEditorIpv4DestIp,
       "me1200QosQceTableRowEditorIpv4DestIpMask": me1200QosQceTableRowEditorIpv4DestIpMask,
       "me1200QosQceTableRowEditorIpv4SrcPortOp": me1200QosQceTableRowEditorIpv4SrcPortOp,
       "me1200QosQceTableRowEditorIpv4SrcPort": me1200QosQceTableRowEditorIpv4SrcPort,
       "me1200QosQceTableRowEditorIpv4SrcPortRange": me1200QosQceTableRowEditorIpv4SrcPortRange,
       "me1200QosQceTableRowEditorIpv4DestPortOp": me1200QosQceTableRowEditorIpv4DestPortOp,
       "me1200QosQceTableRowEditorIpv4DestPort": me1200QosQceTableRowEditorIpv4DestPort,
       "me1200QosQceTableRowEditorIpv4DestPortRange": me1200QosQceTableRowEditorIpv4DestPortRange,
       "me1200QosQceTableRowEditorIpv6DscpOp": me1200QosQceTableRowEditorIpv6DscpOp,
       "me1200QosQceTableRowEditorIpv6Dscp": me1200QosQceTableRowEditorIpv6Dscp,
       "me1200QosQceTableRowEditorIpv6DscpRange": me1200QosQceTableRowEditorIpv6DscpRange,
       "me1200QosQceTableRowEditorIpv6Protocol": me1200QosQceTableRowEditorIpv6Protocol,
       "me1200QosQceTableRowEditorIpv6ProtocolMask": me1200QosQceTableRowEditorIpv6ProtocolMask,
       "me1200QosQceTableRowEditorIpv6SrcIp": me1200QosQceTableRowEditorIpv6SrcIp,
       "me1200QosQceTableRowEditorIpv6SrcIpMask": me1200QosQceTableRowEditorIpv6SrcIpMask,
       "me1200QosQceTableRowEditorIpv6DestIp": me1200QosQceTableRowEditorIpv6DestIp,
       "me1200QosQceTableRowEditorIpv6DestIpMask": me1200QosQceTableRowEditorIpv6DestIpMask,
       "me1200QosQceTableRowEditorIpv6SrcPortOp": me1200QosQceTableRowEditorIpv6SrcPortOp,
       "me1200QosQceTableRowEditorIpv6SrcPort": me1200QosQceTableRowEditorIpv6SrcPort,
       "me1200QosQceTableRowEditorIpv6SrcPortRange": me1200QosQceTableRowEditorIpv6SrcPortRange,
       "me1200QosQceTableRowEditorIpv6DestPortOp": me1200QosQceTableRowEditorIpv6DestPortOp,
       "me1200QosQceTableRowEditorIpv6DestPort": me1200QosQceTableRowEditorIpv6DestPort,
       "me1200QosQceTableRowEditorIpv6DestPortRange": me1200QosQceTableRowEditorIpv6DestPortRange,
       "me1200QosQceTableRowEditorActionCosEnable": me1200QosQceTableRowEditorActionCosEnable,
       "me1200QosQceTableRowEditorActionCos": me1200QosQceTableRowEditorActionCos,
       "me1200QosQceTableRowEditorActionDplEnable": me1200QosQceTableRowEditorActionDplEnable,
       "me1200QosQceTableRowEditorActionDpl": me1200QosQceTableRowEditorActionDpl,
       "me1200QosQceTableRowEditorActionDscpEnable": me1200QosQceTableRowEditorActionDscpEnable,
       "me1200QosQceTableRowEditorActionDscp": me1200QosQceTableRowEditorActionDscp,
       "me1200QosQceTableRowEditorActionPcpDeiEnable": me1200QosQceTableRowEditorActionPcpDeiEnable,
       "me1200QosQceTableRowEditorActionPcp": me1200QosQceTableRowEditorActionPcp,
       "me1200QosQceTableRowEditorActionDei": me1200QosQceTableRowEditorActionDei,
       "me1200QosQceTableRowEditorActionPolicyEnable": me1200QosQceTableRowEditorActionPolicyEnable,
       "me1200QosQceTableRowEditorActionPolicy": me1200QosQceTableRowEditorActionPolicy,
       "me1200QosQceTableRowEditorAction": me1200QosQceTableRowEditorAction,
       "me1200QosQcePrecedenceTable": me1200QosQcePrecedenceTable,
       "me1200QosQcePrecedenceEntry": me1200QosQcePrecedenceEntry,
       "me1200QosQcePrecedenceIndex": me1200QosQcePrecedenceIndex,
       "me1200QosQcePrecedenceQceId": me1200QosQcePrecedenceQceId,
       "me1200QosInterface": me1200QosInterface,
       "me1200QosIfConfigTable": me1200QosIfConfigTable,
       "me1200QosIfConfigEntry": me1200QosIfConfigEntry,
       "me1200QosIfConfigIfIndex": me1200QosIfConfigIfIndex,
       "me1200QosIfConfigCos": me1200QosIfConfigCos,
       "me1200QosIfConfigDpl": me1200QosIfConfigDpl,
       "me1200QosIfConfigPcp": me1200QosIfConfigPcp,
       "me1200QosIfConfigDei": me1200QosIfConfigDei,
       "me1200QosIfConfigTrustTag": me1200QosIfConfigTrustTag,
       "me1200QosIfConfigTrustDscp": me1200QosIfConfigTrustDscp,
       "me1200QosIfConfigDwrrCount": me1200QosIfConfigDwrrCount,
       "me1200QosIfConfigTagRemarkingMode": me1200QosIfConfigTagRemarkingMode,
       "me1200QosIfConfigTagPcp": me1200QosIfConfigTagPcp,
       "me1200QosIfConfigTagDei": me1200QosIfConfigTagDei,
       "me1200QosIfConfigDscpTranslate": me1200QosIfConfigDscpTranslate,
       "me1200QosIfConfigDscpClassify": me1200QosIfConfigDscpClassify,
       "me1200QosIfConfigDscpRemark": me1200QosIfConfigDscpRemark,
       "me1200QosIfConfigQceAddressMode": me1200QosIfConfigQceAddressMode,
       "me1200QosIfConfigQceKeyType": me1200QosIfConfigQceKeyType,
       "me1200QosIfTagToCosTable": me1200QosIfTagToCosTable,
       "me1200QosIfTagToCosEntry": me1200QosIfTagToCosEntry,
       "me1200QosIfTagToCosIfIndex": me1200QosIfTagToCosIfIndex,
       "me1200QosIfTagToCosPcp": me1200QosIfTagToCosPcp,
       "me1200QosIfTagToCosDei": me1200QosIfTagToCosDei,
       "me1200QosIfTagToCosCos": me1200QosIfTagToCosCos,
       "me1200QosIfTagToCosDpl": me1200QosIfTagToCosDpl,
       "me1200QosIfCosToTagTable": me1200QosIfCosToTagTable,
       "me1200QosIfCosToTagEntry": me1200QosIfCosToTagEntry,
       "me1200QosIfCosToTagIfIndex": me1200QosIfCosToTagIfIndex,
       "me1200QosIfCosToTagCos": me1200QosIfCosToTagCos,
       "me1200QosIfCosToTagDpl": me1200QosIfCosToTagDpl,
       "me1200QosIfCosToTagPcp": me1200QosIfCosToTagPcp,
       "me1200QosIfCosToTagDei": me1200QosIfCosToTagDei,
       "me1200QosIfPolicerTable": me1200QosIfPolicerTable,
       "me1200QosIfPolicerEntry": me1200QosIfPolicerEntry,
       "me1200QosIfPolicerIfIndex": me1200QosIfPolicerIfIndex,
       "me1200QosIfPolicerEnable": me1200QosIfPolicerEnable,
       "me1200QosIfPolicerFrameRate": me1200QosIfPolicerFrameRate,
       "me1200QosIfPolicerFlowControl": me1200QosIfPolicerFlowControl,
       "me1200QosIfPolicerCir": me1200QosIfPolicerCir,
       "me1200QosIfQueuePolicerTable": me1200QosIfQueuePolicerTable,
       "me1200QosIfQueuePolicerEntry": me1200QosIfQueuePolicerEntry,
       "me1200QosIfQueuePolicerIfIndex": me1200QosIfQueuePolicerIfIndex,
       "me1200QosIfQueuePolicerQueue": me1200QosIfQueuePolicerQueue,
       "me1200QosIfQueuePolicerEnable": me1200QosIfQueuePolicerEnable,
       "me1200QosIfQueuePolicerCir": me1200QosIfQueuePolicerCir,
       "me1200QosIfShaperTable": me1200QosIfShaperTable,
       "me1200QosIfShaperEntry": me1200QosIfShaperEntry,
       "me1200QosIfShaperIfIndex": me1200QosIfShaperIfIndex,
       "me1200QosIfShaperEnable": me1200QosIfShaperEnable,
       "me1200QosIfShaperCir": me1200QosIfShaperCir,
       "me1200QosIfQueueShaperTable": me1200QosIfQueueShaperTable,
       "me1200QosIfQueueShaperEntry": me1200QosIfQueueShaperEntry,
       "me1200QosIfQueueShaperIfIndex": me1200QosIfQueueShaperIfIndex,
       "me1200QosIfQueueShaperQueue": me1200QosIfQueueShaperQueue,
       "me1200QosIfQueueShaperEnable": me1200QosIfQueueShaperEnable,
       "me1200QosIfQueueShaperExcess": me1200QosIfQueueShaperExcess,
       "me1200QosIfQueueShaperCir": me1200QosIfQueueShaperCir,
       "me1200QosIfSchedulerTable": me1200QosIfSchedulerTable,
       "me1200QosIfSchedulerEntry": me1200QosIfSchedulerEntry,
       "me1200QosIfSchedulerIfIndex": me1200QosIfSchedulerIfIndex,
       "me1200QosIfSchedulerQueue": me1200QosIfSchedulerQueue,
       "me1200QosIfSchedulerWeight": me1200QosIfSchedulerWeight,
       "me1200QosStatus": me1200QosStatus,
       "me1200QosStatusGlobals": me1200QosStatusGlobals,
       "me1200QosStatusQceTable": me1200QosStatusQceTable,
       "me1200QosStatusQceEntry": me1200QosStatusQceEntry,
       "me1200QosStatusQceIndex": me1200QosStatusQceIndex,
       "me1200QosStatusQceUserId": me1200QosStatusQceUserId,
       "me1200QosStatusQceQceId": me1200QosStatusQceQceId,
       "me1200QosStatusQceConflict": me1200QosStatusQceConflict,
       "me1200QosStatusInterface": me1200QosStatusInterface,
       "me1200QosStatusIfTable": me1200QosStatusIfTable,
       "me1200QosStatusIfEntry": me1200QosStatusIfEntry,
       "me1200QosStatusIfIfIndex": me1200QosStatusIfIfIndex,
       "me1200QosStatusIfCos": me1200QosStatusIfCos,
       "me1200QosStatusIfSchedulerTable": me1200QosStatusIfSchedulerTable,
       "me1200QosStatusIfSchedulerEntry": me1200QosStatusIfSchedulerEntry,
       "me1200QosStatusIfSchedulerIfIndex": me1200QosStatusIfSchedulerIfIndex,
       "me1200QosStatusIfSchedulerQueue": me1200QosStatusIfSchedulerQueue,
       "me1200QosStatusIfSchedulerWeight": me1200QosStatusIfSchedulerWeight,
       "me1200QosControl": me1200QosControl,
       "me1200QosControlGlobals": me1200QosControlGlobals,
       "me1200QosControlGlobalsConflictResolve": me1200QosControlGlobalsConflictResolve,
       "me1200QosMIBConformance": me1200QosMIBConformance,
       "me1200QosMIBCompliances": me1200QosMIBCompliances,
       "me1200QosMIBCompliance": me1200QosMIBCompliance,
       "me1200QosMIBGroups": me1200QosMIBGroups,
       "me1200QosStormPolicerUnicastInfoGroup": me1200QosStormPolicerUnicastInfoGroup,
       "me1200QosStormPolicerMulticastInfoGroup": me1200QosStormPolicerMulticastInfoGroup,
       "me1200QosStormPolicerBroadcastInfoGroup": me1200QosStormPolicerBroadcastInfoGroup,
       "me1200QosWredTableInfoGroup": me1200QosWredTableInfoGroup,
       "me1200QosDscpTableInfoGroup": me1200QosDscpTableInfoGroup,
       "me1200QosCosToDscpTableInfoGroup": me1200QosCosToDscpTableInfoGroup,
       "me1200QosQceTableInfoGroup": me1200QosQceTableInfoGroup,
       "me1200QosQceTableRowEditorInfoGroup": me1200QosQceTableRowEditorInfoGroup,
       "me1200QosQcePrecedenceTableInfoGroup": me1200QosQcePrecedenceTableInfoGroup,
       "me1200QosIfConfigTableInfoGroup": me1200QosIfConfigTableInfoGroup,
       "me1200QosIfTagToCosTableInfoGroup": me1200QosIfTagToCosTableInfoGroup,
       "me1200QosIfCosToTagTableInfoGroup": me1200QosIfCosToTagTableInfoGroup,
       "me1200QosIfPolicerTableInfoGroup": me1200QosIfPolicerTableInfoGroup,
       "me1200QosIfQueuePolicerTableInfoGroup": me1200QosIfQueuePolicerTableInfoGroup,
       "me1200QosIfShaperTableInfoGroup": me1200QosIfShaperTableInfoGroup,
       "me1200QosIfQueueShaperTableInfoGroup": me1200QosIfQueueShaperTableInfoGroup,
       "me1200QosIfSchedulerTableInfoGroup": me1200QosIfSchedulerTableInfoGroup,
       "me1200QosStatusQceTableInfoGroup": me1200QosStatusQceTableInfoGroup,
       "me1200QosStatusIfTableInfoGroup": me1200QosStatusIfTableInfoGroup,
       "me1200QosStatusIfSchedulerTableInfoGroup": me1200QosStatusIfSchedulerTableInfoGroup,
       "me1200QosControlGlobalsInfoGroup": me1200QosControlGlobalsInfoGroup}
)
