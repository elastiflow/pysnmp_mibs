# SNMP MIB module (CIE1000-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-QOS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:42 2025
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

(CIE1000ASRType,
 CIE1000BitType,
 CIE1000DestMacType,
 CIE1000EtherType,
 CIE1000InterfaceIndex,
 CIE1000Percent,
 CIE1000PortList,
 CIE1000RowEditorState,
 CIE1000Unsigned16,
 CIE1000Unsigned8,
 CIE1000VcapKeyType,
 CIE1000VlanTagPriority,
 CIE1000VlanTagType) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000ASRType",
    "CIE1000BitType",
    "CIE1000DestMacType",
    "CIE1000EtherType",
    "CIE1000InterfaceIndex",
    "CIE1000Percent",
    "CIE1000PortList",
    "CIE1000RowEditorState",
    "CIE1000Unsigned16",
    "CIE1000Unsigned8",
    "CIE1000VcapKeyType",
    "CIE1000VlanTagPriority",
    "CIE1000VlanTagType")

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(IEEE8021STPTPtimeValue,) = mibBuilder.importSymbols(
    "IEEE8021-ST-MIB",
    "IEEE8021STPTPtimeValue")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

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

cie1000QosMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14)
)
if mibBuilder.loadTexts:
    cie1000QosMib.setRevisions(
        ("2016-02-25 00:00",
         "2016-02-11 00:00",
         "2016-01-19 00:00",
         "2015-11-13 00:00",
         "2015-09-30 00:00",
         "2015-08-13 00:00",
         "2015-06-23 00:00",
         "2015-05-27 00:00",
         "2015-04-07 00:00",
         "2014-11-06 00:00",
         "2014-10-08 00:00",
         "2014-09-17 00:00",
         "2014-08-12 00:00",
         "2014-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CIE1000QosDscpClassify(TextualConvention, Integer32):
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



class CIE1000QosDscpRemark(TextualConvention, Integer32):
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



class CIE1000QosEgressMapKey(TextualConvention, Integer32):
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
        *(("cosid", 0),
          ("cosidDpl", 1),
          ("dscp", 2),
          ("dscpDpl", 3))
    )



class CIE1000QosIngressMapKey(TextualConvention, Integer32):
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
        *(("pcp", 0),
          ("pcpDei", 1),
          ("dscp", 2),
          ("dscpPcpDei", 3))
    )



class CIE1000QosQceFrameType(TextualConvention, Integer32):
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



class CIE1000QosQceUserType(TextualConvention, Integer32):
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



class CIE1000QosShaperRateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("line", 0),
          ("data", 1))
    )



class CIE1000QosTagRemarkingMode(TextualConvention, Integer32):
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



class CIE1000QosWredMaxSelector(TextualConvention, Integer32):
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



# MIB Managed Objects in the order of their OIDs

_Cie1000QosMibObjects_ObjectIdentity = ObjectIdentity
cie1000QosMibObjects = _Cie1000QosMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1)
)
_Cie1000QosCapabilities_ObjectIdentity = ObjectIdentity
cie1000QosCapabilities = _Cie1000QosCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1)
)
_Cie1000QosCapabilitiesClassMin_Type = Unsigned32
_Cie1000QosCapabilitiesClassMin_Object = MibScalar
cie1000QosCapabilitiesClassMin = _Cie1000QosCapabilitiesClassMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 1),
    _Cie1000QosCapabilitiesClassMin_Type()
)
cie1000QosCapabilitiesClassMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesClassMin.setStatus("current")
_Cie1000QosCapabilitiesClassMax_Type = Unsigned32
_Cie1000QosCapabilitiesClassMax_Object = MibScalar
cie1000QosCapabilitiesClassMax = _Cie1000QosCapabilitiesClassMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 2),
    _Cie1000QosCapabilitiesClassMax_Type()
)
cie1000QosCapabilitiesClassMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesClassMax.setStatus("current")
_Cie1000QosCapabilitiesDplMin_Type = CIE1000Unsigned8
_Cie1000QosCapabilitiesDplMin_Object = MibScalar
cie1000QosCapabilitiesDplMin = _Cie1000QosCapabilitiesDplMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 3),
    _Cie1000QosCapabilitiesDplMin_Type()
)
cie1000QosCapabilitiesDplMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesDplMin.setStatus("current")
_Cie1000QosCapabilitiesDplMax_Type = CIE1000Unsigned8
_Cie1000QosCapabilitiesDplMax_Object = MibScalar
cie1000QosCapabilitiesDplMax = _Cie1000QosCapabilitiesDplMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 4),
    _Cie1000QosCapabilitiesDplMax_Type()
)
cie1000QosCapabilitiesDplMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesDplMax.setStatus("current")
_Cie1000QosCapabilitiesWredGroupMin_Type = Unsigned32
_Cie1000QosCapabilitiesWredGroupMin_Object = MibScalar
cie1000QosCapabilitiesWredGroupMin = _Cie1000QosCapabilitiesWredGroupMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 5),
    _Cie1000QosCapabilitiesWredGroupMin_Type()
)
cie1000QosCapabilitiesWredGroupMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesWredGroupMin.setStatus("current")
_Cie1000QosCapabilitiesWredGroupMax_Type = Unsigned32
_Cie1000QosCapabilitiesWredGroupMax_Object = MibScalar
cie1000QosCapabilitiesWredGroupMax = _Cie1000QosCapabilitiesWredGroupMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 6),
    _Cie1000QosCapabilitiesWredGroupMax_Type()
)
cie1000QosCapabilitiesWredGroupMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesWredGroupMax.setStatus("current")
_Cie1000QosCapabilitiesWredDplMin_Type = CIE1000Unsigned8
_Cie1000QosCapabilitiesWredDplMin_Object = MibScalar
cie1000QosCapabilitiesWredDplMin = _Cie1000QosCapabilitiesWredDplMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 7),
    _Cie1000QosCapabilitiesWredDplMin_Type()
)
cie1000QosCapabilitiesWredDplMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesWredDplMin.setStatus("current")
_Cie1000QosCapabilitiesWredDplMax_Type = CIE1000Unsigned8
_Cie1000QosCapabilitiesWredDplMax_Object = MibScalar
cie1000QosCapabilitiesWredDplMax = _Cie1000QosCapabilitiesWredDplMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 8),
    _Cie1000QosCapabilitiesWredDplMax_Type()
)
cie1000QosCapabilitiesWredDplMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesWredDplMax.setStatus("current")
_Cie1000QosCapabilitiesQceIdMin_Type = Unsigned32
_Cie1000QosCapabilitiesQceIdMin_Object = MibScalar
cie1000QosCapabilitiesQceIdMin = _Cie1000QosCapabilitiesQceIdMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 9),
    _Cie1000QosCapabilitiesQceIdMin_Type()
)
cie1000QosCapabilitiesQceIdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQceIdMin.setStatus("current")
_Cie1000QosCapabilitiesQceIdMax_Type = Unsigned32
_Cie1000QosCapabilitiesQceIdMax_Object = MibScalar
cie1000QosCapabilitiesQceIdMax = _Cie1000QosCapabilitiesQceIdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 10),
    _Cie1000QosCapabilitiesQceIdMax_Type()
)
cie1000QosCapabilitiesQceIdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQceIdMax.setStatus("current")
_Cie1000QosCapabilitiesPortPolicerBitRateMin_Type = Unsigned32
_Cie1000QosCapabilitiesPortPolicerBitRateMin_Object = MibScalar
cie1000QosCapabilitiesPortPolicerBitRateMin = _Cie1000QosCapabilitiesPortPolicerBitRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 11),
    _Cie1000QosCapabilitiesPortPolicerBitRateMin_Type()
)
cie1000QosCapabilitiesPortPolicerBitRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortPolicerBitRateMin.setStatus("current")
_Cie1000QosCapabilitiesPortPolicerBitRateMax_Type = Unsigned32
_Cie1000QosCapabilitiesPortPolicerBitRateMax_Object = MibScalar
cie1000QosCapabilitiesPortPolicerBitRateMax = _Cie1000QosCapabilitiesPortPolicerBitRateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 12),
    _Cie1000QosCapabilitiesPortPolicerBitRateMax_Type()
)
cie1000QosCapabilitiesPortPolicerBitRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortPolicerBitRateMax.setStatus("current")
_Cie1000QosCapabilitiesPortPolicerBitBurstMin_Type = Unsigned32
_Cie1000QosCapabilitiesPortPolicerBitBurstMin_Object = MibScalar
cie1000QosCapabilitiesPortPolicerBitBurstMin = _Cie1000QosCapabilitiesPortPolicerBitBurstMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 13),
    _Cie1000QosCapabilitiesPortPolicerBitBurstMin_Type()
)
cie1000QosCapabilitiesPortPolicerBitBurstMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortPolicerBitBurstMin.setStatus("current")
_Cie1000QosCapabilitiesPortPolicerBitBurstMax_Type = Unsigned32
_Cie1000QosCapabilitiesPortPolicerBitBurstMax_Object = MibScalar
cie1000QosCapabilitiesPortPolicerBitBurstMax = _Cie1000QosCapabilitiesPortPolicerBitBurstMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 14),
    _Cie1000QosCapabilitiesPortPolicerBitBurstMax_Type()
)
cie1000QosCapabilitiesPortPolicerBitBurstMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortPolicerBitBurstMax.setStatus("current")
_Cie1000QosCapabilitiesPortPolicerFrameRateMin_Type = Unsigned32
_Cie1000QosCapabilitiesPortPolicerFrameRateMin_Object = MibScalar
cie1000QosCapabilitiesPortPolicerFrameRateMin = _Cie1000QosCapabilitiesPortPolicerFrameRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 15),
    _Cie1000QosCapabilitiesPortPolicerFrameRateMin_Type()
)
cie1000QosCapabilitiesPortPolicerFrameRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortPolicerFrameRateMin.setStatus("current")
_Cie1000QosCapabilitiesPortPolicerFrameRateMax_Type = Unsigned32
_Cie1000QosCapabilitiesPortPolicerFrameRateMax_Object = MibScalar
cie1000QosCapabilitiesPortPolicerFrameRateMax = _Cie1000QosCapabilitiesPortPolicerFrameRateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 16),
    _Cie1000QosCapabilitiesPortPolicerFrameRateMax_Type()
)
cie1000QosCapabilitiesPortPolicerFrameRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortPolicerFrameRateMax.setStatus("current")
_Cie1000QosCapabilitiesPortPolicerFrameBurstMin_Type = Unsigned32
_Cie1000QosCapabilitiesPortPolicerFrameBurstMin_Object = MibScalar
cie1000QosCapabilitiesPortPolicerFrameBurstMin = _Cie1000QosCapabilitiesPortPolicerFrameBurstMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 17),
    _Cie1000QosCapabilitiesPortPolicerFrameBurstMin_Type()
)
cie1000QosCapabilitiesPortPolicerFrameBurstMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortPolicerFrameBurstMin.setStatus("current")
_Cie1000QosCapabilitiesPortPolicerFrameBurstMax_Type = Unsigned32
_Cie1000QosCapabilitiesPortPolicerFrameBurstMax_Object = MibScalar
cie1000QosCapabilitiesPortPolicerFrameBurstMax = _Cie1000QosCapabilitiesPortPolicerFrameBurstMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 18),
    _Cie1000QosCapabilitiesPortPolicerFrameBurstMax_Type()
)
cie1000QosCapabilitiesPortPolicerFrameBurstMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortPolicerFrameBurstMax.setStatus("current")
_Cie1000QosCapabilitiesQueuePolicerBitRateMin_Type = Unsigned32
_Cie1000QosCapabilitiesQueuePolicerBitRateMin_Object = MibScalar
cie1000QosCapabilitiesQueuePolicerBitRateMin = _Cie1000QosCapabilitiesQueuePolicerBitRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 19),
    _Cie1000QosCapabilitiesQueuePolicerBitRateMin_Type()
)
cie1000QosCapabilitiesQueuePolicerBitRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQueuePolicerBitRateMin.setStatus("current")
_Cie1000QosCapabilitiesQueuePolicerBitRateMax_Type = Unsigned32
_Cie1000QosCapabilitiesQueuePolicerBitRateMax_Object = MibScalar
cie1000QosCapabilitiesQueuePolicerBitRateMax = _Cie1000QosCapabilitiesQueuePolicerBitRateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 20),
    _Cie1000QosCapabilitiesQueuePolicerBitRateMax_Type()
)
cie1000QosCapabilitiesQueuePolicerBitRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQueuePolicerBitRateMax.setStatus("current")
_Cie1000QosCapabilitiesQueuePolicerBitBurstMin_Type = Unsigned32
_Cie1000QosCapabilitiesQueuePolicerBitBurstMin_Object = MibScalar
cie1000QosCapabilitiesQueuePolicerBitBurstMin = _Cie1000QosCapabilitiesQueuePolicerBitBurstMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 21),
    _Cie1000QosCapabilitiesQueuePolicerBitBurstMin_Type()
)
cie1000QosCapabilitiesQueuePolicerBitBurstMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQueuePolicerBitBurstMin.setStatus("current")
_Cie1000QosCapabilitiesQueuePolicerBitBurstMax_Type = Unsigned32
_Cie1000QosCapabilitiesQueuePolicerBitBurstMax_Object = MibScalar
cie1000QosCapabilitiesQueuePolicerBitBurstMax = _Cie1000QosCapabilitiesQueuePolicerBitBurstMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 22),
    _Cie1000QosCapabilitiesQueuePolicerBitBurstMax_Type()
)
cie1000QosCapabilitiesQueuePolicerBitBurstMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQueuePolicerBitBurstMax.setStatus("current")
_Cie1000QosCapabilitiesQueuePolicerFrameRateMin_Type = Unsigned32
_Cie1000QosCapabilitiesQueuePolicerFrameRateMin_Object = MibScalar
cie1000QosCapabilitiesQueuePolicerFrameRateMin = _Cie1000QosCapabilitiesQueuePolicerFrameRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 23),
    _Cie1000QosCapabilitiesQueuePolicerFrameRateMin_Type()
)
cie1000QosCapabilitiesQueuePolicerFrameRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQueuePolicerFrameRateMin.setStatus("current")
_Cie1000QosCapabilitiesQueuePolicerFrameRateMax_Type = Unsigned32
_Cie1000QosCapabilitiesQueuePolicerFrameRateMax_Object = MibScalar
cie1000QosCapabilitiesQueuePolicerFrameRateMax = _Cie1000QosCapabilitiesQueuePolicerFrameRateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 24),
    _Cie1000QosCapabilitiesQueuePolicerFrameRateMax_Type()
)
cie1000QosCapabilitiesQueuePolicerFrameRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQueuePolicerFrameRateMax.setStatus("current")
_Cie1000QosCapabilitiesQueuePolicerFrameBurstMin_Type = Unsigned32
_Cie1000QosCapabilitiesQueuePolicerFrameBurstMin_Object = MibScalar
cie1000QosCapabilitiesQueuePolicerFrameBurstMin = _Cie1000QosCapabilitiesQueuePolicerFrameBurstMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 25),
    _Cie1000QosCapabilitiesQueuePolicerFrameBurstMin_Type()
)
cie1000QosCapabilitiesQueuePolicerFrameBurstMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQueuePolicerFrameBurstMin.setStatus("current")
_Cie1000QosCapabilitiesQueuePolicerFrameBurstMax_Type = Unsigned32
_Cie1000QosCapabilitiesQueuePolicerFrameBurstMax_Object = MibScalar
cie1000QosCapabilitiesQueuePolicerFrameBurstMax = _Cie1000QosCapabilitiesQueuePolicerFrameBurstMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 26),
    _Cie1000QosCapabilitiesQueuePolicerFrameBurstMax_Type()
)
cie1000QosCapabilitiesQueuePolicerFrameBurstMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQueuePolicerFrameBurstMax.setStatus("current")
_Cie1000QosCapabilitiesPortShaperBitRateMin_Type = Unsigned32
_Cie1000QosCapabilitiesPortShaperBitRateMin_Object = MibScalar
cie1000QosCapabilitiesPortShaperBitRateMin = _Cie1000QosCapabilitiesPortShaperBitRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 27),
    _Cie1000QosCapabilitiesPortShaperBitRateMin_Type()
)
cie1000QosCapabilitiesPortShaperBitRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortShaperBitRateMin.setStatus("current")
_Cie1000QosCapabilitiesPortShaperBitRateMax_Type = Unsigned32
_Cie1000QosCapabilitiesPortShaperBitRateMax_Object = MibScalar
cie1000QosCapabilitiesPortShaperBitRateMax = _Cie1000QosCapabilitiesPortShaperBitRateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 28),
    _Cie1000QosCapabilitiesPortShaperBitRateMax_Type()
)
cie1000QosCapabilitiesPortShaperBitRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortShaperBitRateMax.setStatus("current")
_Cie1000QosCapabilitiesPortShaperBitBurstMin_Type = Unsigned32
_Cie1000QosCapabilitiesPortShaperBitBurstMin_Object = MibScalar
cie1000QosCapabilitiesPortShaperBitBurstMin = _Cie1000QosCapabilitiesPortShaperBitBurstMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 29),
    _Cie1000QosCapabilitiesPortShaperBitBurstMin_Type()
)
cie1000QosCapabilitiesPortShaperBitBurstMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortShaperBitBurstMin.setStatus("current")
_Cie1000QosCapabilitiesPortShaperBitBurstMax_Type = Unsigned32
_Cie1000QosCapabilitiesPortShaperBitBurstMax_Object = MibScalar
cie1000QosCapabilitiesPortShaperBitBurstMax = _Cie1000QosCapabilitiesPortShaperBitBurstMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 30),
    _Cie1000QosCapabilitiesPortShaperBitBurstMax_Type()
)
cie1000QosCapabilitiesPortShaperBitBurstMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortShaperBitBurstMax.setStatus("current")
_Cie1000QosCapabilitiesPortShaperFrameRateMin_Type = Unsigned32
_Cie1000QosCapabilitiesPortShaperFrameRateMin_Object = MibScalar
cie1000QosCapabilitiesPortShaperFrameRateMin = _Cie1000QosCapabilitiesPortShaperFrameRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 31),
    _Cie1000QosCapabilitiesPortShaperFrameRateMin_Type()
)
cie1000QosCapabilitiesPortShaperFrameRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortShaperFrameRateMin.setStatus("current")
_Cie1000QosCapabilitiesPortShaperFrameRateMax_Type = Unsigned32
_Cie1000QosCapabilitiesPortShaperFrameRateMax_Object = MibScalar
cie1000QosCapabilitiesPortShaperFrameRateMax = _Cie1000QosCapabilitiesPortShaperFrameRateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 32),
    _Cie1000QosCapabilitiesPortShaperFrameRateMax_Type()
)
cie1000QosCapabilitiesPortShaperFrameRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortShaperFrameRateMax.setStatus("current")
_Cie1000QosCapabilitiesPortShaperFrameBurstMin_Type = Unsigned32
_Cie1000QosCapabilitiesPortShaperFrameBurstMin_Object = MibScalar
cie1000QosCapabilitiesPortShaperFrameBurstMin = _Cie1000QosCapabilitiesPortShaperFrameBurstMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 33),
    _Cie1000QosCapabilitiesPortShaperFrameBurstMin_Type()
)
cie1000QosCapabilitiesPortShaperFrameBurstMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortShaperFrameBurstMin.setStatus("current")
_Cie1000QosCapabilitiesPortShaperFrameBurstMax_Type = Unsigned32
_Cie1000QosCapabilitiesPortShaperFrameBurstMax_Object = MibScalar
cie1000QosCapabilitiesPortShaperFrameBurstMax = _Cie1000QosCapabilitiesPortShaperFrameBurstMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 34),
    _Cie1000QosCapabilitiesPortShaperFrameBurstMax_Type()
)
cie1000QosCapabilitiesPortShaperFrameBurstMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortShaperFrameBurstMax.setStatus("current")
_Cie1000QosCapabilitiesQueueShaperBitRateMin_Type = Unsigned32
_Cie1000QosCapabilitiesQueueShaperBitRateMin_Object = MibScalar
cie1000QosCapabilitiesQueueShaperBitRateMin = _Cie1000QosCapabilitiesQueueShaperBitRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 35),
    _Cie1000QosCapabilitiesQueueShaperBitRateMin_Type()
)
cie1000QosCapabilitiesQueueShaperBitRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQueueShaperBitRateMin.setStatus("current")
_Cie1000QosCapabilitiesQueueShaperBitRateMax_Type = Unsigned32
_Cie1000QosCapabilitiesQueueShaperBitRateMax_Object = MibScalar
cie1000QosCapabilitiesQueueShaperBitRateMax = _Cie1000QosCapabilitiesQueueShaperBitRateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 36),
    _Cie1000QosCapabilitiesQueueShaperBitRateMax_Type()
)
cie1000QosCapabilitiesQueueShaperBitRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQueueShaperBitRateMax.setStatus("current")
_Cie1000QosCapabilitiesQueueShaperBitBurstMin_Type = Unsigned32
_Cie1000QosCapabilitiesQueueShaperBitBurstMin_Object = MibScalar
cie1000QosCapabilitiesQueueShaperBitBurstMin = _Cie1000QosCapabilitiesQueueShaperBitBurstMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 37),
    _Cie1000QosCapabilitiesQueueShaperBitBurstMin_Type()
)
cie1000QosCapabilitiesQueueShaperBitBurstMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQueueShaperBitBurstMin.setStatus("current")
_Cie1000QosCapabilitiesQueueShaperBitBurstMax_Type = Unsigned32
_Cie1000QosCapabilitiesQueueShaperBitBurstMax_Object = MibScalar
cie1000QosCapabilitiesQueueShaperBitBurstMax = _Cie1000QosCapabilitiesQueueShaperBitBurstMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 38),
    _Cie1000QosCapabilitiesQueueShaperBitBurstMax_Type()
)
cie1000QosCapabilitiesQueueShaperBitBurstMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQueueShaperBitBurstMax.setStatus("current")
_Cie1000QosCapabilitiesQueueShaperFrameRateMin_Type = Unsigned32
_Cie1000QosCapabilitiesQueueShaperFrameRateMin_Object = MibScalar
cie1000QosCapabilitiesQueueShaperFrameRateMin = _Cie1000QosCapabilitiesQueueShaperFrameRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 39),
    _Cie1000QosCapabilitiesQueueShaperFrameRateMin_Type()
)
cie1000QosCapabilitiesQueueShaperFrameRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQueueShaperFrameRateMin.setStatus("current")
_Cie1000QosCapabilitiesQueueShaperFrameRateMax_Type = Unsigned32
_Cie1000QosCapabilitiesQueueShaperFrameRateMax_Object = MibScalar
cie1000QosCapabilitiesQueueShaperFrameRateMax = _Cie1000QosCapabilitiesQueueShaperFrameRateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 40),
    _Cie1000QosCapabilitiesQueueShaperFrameRateMax_Type()
)
cie1000QosCapabilitiesQueueShaperFrameRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQueueShaperFrameRateMax.setStatus("current")
_Cie1000QosCapabilitiesQueueShaperFrameBurstMin_Type = Unsigned32
_Cie1000QosCapabilitiesQueueShaperFrameBurstMin_Object = MibScalar
cie1000QosCapabilitiesQueueShaperFrameBurstMin = _Cie1000QosCapabilitiesQueueShaperFrameBurstMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 41),
    _Cie1000QosCapabilitiesQueueShaperFrameBurstMin_Type()
)
cie1000QosCapabilitiesQueueShaperFrameBurstMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQueueShaperFrameBurstMin.setStatus("current")
_Cie1000QosCapabilitiesQueueShaperFrameBurstMax_Type = Unsigned32
_Cie1000QosCapabilitiesQueueShaperFrameBurstMax_Object = MibScalar
cie1000QosCapabilitiesQueueShaperFrameBurstMax = _Cie1000QosCapabilitiesQueueShaperFrameBurstMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 42),
    _Cie1000QosCapabilitiesQueueShaperFrameBurstMax_Type()
)
cie1000QosCapabilitiesQueueShaperFrameBurstMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQueueShaperFrameBurstMax.setStatus("current")
_Cie1000QosCapabilitiesGlobalStormBitRateMin_Type = Unsigned32
_Cie1000QosCapabilitiesGlobalStormBitRateMin_Object = MibScalar
cie1000QosCapabilitiesGlobalStormBitRateMin = _Cie1000QosCapabilitiesGlobalStormBitRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 43),
    _Cie1000QosCapabilitiesGlobalStormBitRateMin_Type()
)
cie1000QosCapabilitiesGlobalStormBitRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesGlobalStormBitRateMin.setStatus("current")
_Cie1000QosCapabilitiesGlobalStormBitRateMax_Type = Unsigned32
_Cie1000QosCapabilitiesGlobalStormBitRateMax_Object = MibScalar
cie1000QosCapabilitiesGlobalStormBitRateMax = _Cie1000QosCapabilitiesGlobalStormBitRateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 44),
    _Cie1000QosCapabilitiesGlobalStormBitRateMax_Type()
)
cie1000QosCapabilitiesGlobalStormBitRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesGlobalStormBitRateMax.setStatus("current")
_Cie1000QosCapabilitiesGlobalStormBitBurstMin_Type = Unsigned32
_Cie1000QosCapabilitiesGlobalStormBitBurstMin_Object = MibScalar
cie1000QosCapabilitiesGlobalStormBitBurstMin = _Cie1000QosCapabilitiesGlobalStormBitBurstMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 45),
    _Cie1000QosCapabilitiesGlobalStormBitBurstMin_Type()
)
cie1000QosCapabilitiesGlobalStormBitBurstMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesGlobalStormBitBurstMin.setStatus("current")
_Cie1000QosCapabilitiesGlobalStormBitBurstMax_Type = Unsigned32
_Cie1000QosCapabilitiesGlobalStormBitBurstMax_Object = MibScalar
cie1000QosCapabilitiesGlobalStormBitBurstMax = _Cie1000QosCapabilitiesGlobalStormBitBurstMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 46),
    _Cie1000QosCapabilitiesGlobalStormBitBurstMax_Type()
)
cie1000QosCapabilitiesGlobalStormBitBurstMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesGlobalStormBitBurstMax.setStatus("current")
_Cie1000QosCapabilitiesGlobalStormFrameRateMin_Type = Unsigned32
_Cie1000QosCapabilitiesGlobalStormFrameRateMin_Object = MibScalar
cie1000QosCapabilitiesGlobalStormFrameRateMin = _Cie1000QosCapabilitiesGlobalStormFrameRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 47),
    _Cie1000QosCapabilitiesGlobalStormFrameRateMin_Type()
)
cie1000QosCapabilitiesGlobalStormFrameRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesGlobalStormFrameRateMin.setStatus("current")
_Cie1000QosCapabilitiesGlobalStormFrameRateMax_Type = Unsigned32
_Cie1000QosCapabilitiesGlobalStormFrameRateMax_Object = MibScalar
cie1000QosCapabilitiesGlobalStormFrameRateMax = _Cie1000QosCapabilitiesGlobalStormFrameRateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 48),
    _Cie1000QosCapabilitiesGlobalStormFrameRateMax_Type()
)
cie1000QosCapabilitiesGlobalStormFrameRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesGlobalStormFrameRateMax.setStatus("current")
_Cie1000QosCapabilitiesGlobalStormFrameBurstMin_Type = Unsigned32
_Cie1000QosCapabilitiesGlobalStormFrameBurstMin_Object = MibScalar
cie1000QosCapabilitiesGlobalStormFrameBurstMin = _Cie1000QosCapabilitiesGlobalStormFrameBurstMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 49),
    _Cie1000QosCapabilitiesGlobalStormFrameBurstMin_Type()
)
cie1000QosCapabilitiesGlobalStormFrameBurstMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesGlobalStormFrameBurstMin.setStatus("current")
_Cie1000QosCapabilitiesGlobalStormFrameBurstMax_Type = Unsigned32
_Cie1000QosCapabilitiesGlobalStormFrameBurstMax_Object = MibScalar
cie1000QosCapabilitiesGlobalStormFrameBurstMax = _Cie1000QosCapabilitiesGlobalStormFrameBurstMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 50),
    _Cie1000QosCapabilitiesGlobalStormFrameBurstMax_Type()
)
cie1000QosCapabilitiesGlobalStormFrameBurstMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesGlobalStormFrameBurstMax.setStatus("current")
_Cie1000QosCapabilitiesPortStormBitRateMin_Type = Unsigned32
_Cie1000QosCapabilitiesPortStormBitRateMin_Object = MibScalar
cie1000QosCapabilitiesPortStormBitRateMin = _Cie1000QosCapabilitiesPortStormBitRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 51),
    _Cie1000QosCapabilitiesPortStormBitRateMin_Type()
)
cie1000QosCapabilitiesPortStormBitRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortStormBitRateMin.setStatus("current")
_Cie1000QosCapabilitiesPortStormBitRateMax_Type = Unsigned32
_Cie1000QosCapabilitiesPortStormBitRateMax_Object = MibScalar
cie1000QosCapabilitiesPortStormBitRateMax = _Cie1000QosCapabilitiesPortStormBitRateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 52),
    _Cie1000QosCapabilitiesPortStormBitRateMax_Type()
)
cie1000QosCapabilitiesPortStormBitRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortStormBitRateMax.setStatus("current")
_Cie1000QosCapabilitiesPortStormBitBurstMin_Type = Unsigned32
_Cie1000QosCapabilitiesPortStormBitBurstMin_Object = MibScalar
cie1000QosCapabilitiesPortStormBitBurstMin = _Cie1000QosCapabilitiesPortStormBitBurstMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 53),
    _Cie1000QosCapabilitiesPortStormBitBurstMin_Type()
)
cie1000QosCapabilitiesPortStormBitBurstMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortStormBitBurstMin.setStatus("current")
_Cie1000QosCapabilitiesPortStormBitBurstMax_Type = Unsigned32
_Cie1000QosCapabilitiesPortStormBitBurstMax_Object = MibScalar
cie1000QosCapabilitiesPortStormBitBurstMax = _Cie1000QosCapabilitiesPortStormBitBurstMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 54),
    _Cie1000QosCapabilitiesPortStormBitBurstMax_Type()
)
cie1000QosCapabilitiesPortStormBitBurstMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortStormBitBurstMax.setStatus("current")
_Cie1000QosCapabilitiesPortStormFrameRateMin_Type = Unsigned32
_Cie1000QosCapabilitiesPortStormFrameRateMin_Object = MibScalar
cie1000QosCapabilitiesPortStormFrameRateMin = _Cie1000QosCapabilitiesPortStormFrameRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 55),
    _Cie1000QosCapabilitiesPortStormFrameRateMin_Type()
)
cie1000QosCapabilitiesPortStormFrameRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortStormFrameRateMin.setStatus("current")
_Cie1000QosCapabilitiesPortStormFrameRateMax_Type = Unsigned32
_Cie1000QosCapabilitiesPortStormFrameRateMax_Object = MibScalar
cie1000QosCapabilitiesPortStormFrameRateMax = _Cie1000QosCapabilitiesPortStormFrameRateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 56),
    _Cie1000QosCapabilitiesPortStormFrameRateMax_Type()
)
cie1000QosCapabilitiesPortStormFrameRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortStormFrameRateMax.setStatus("current")
_Cie1000QosCapabilitiesPortStormFrameBurstMin_Type = Unsigned32
_Cie1000QosCapabilitiesPortStormFrameBurstMin_Object = MibScalar
cie1000QosCapabilitiesPortStormFrameBurstMin = _Cie1000QosCapabilitiesPortStormFrameBurstMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 57),
    _Cie1000QosCapabilitiesPortStormFrameBurstMin_Type()
)
cie1000QosCapabilitiesPortStormFrameBurstMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortStormFrameBurstMin.setStatus("current")
_Cie1000QosCapabilitiesPortStormFrameBurstMax_Type = Unsigned32
_Cie1000QosCapabilitiesPortStormFrameBurstMax_Object = MibScalar
cie1000QosCapabilitiesPortStormFrameBurstMax = _Cie1000QosCapabilitiesPortStormFrameBurstMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 58),
    _Cie1000QosCapabilitiesPortStormFrameBurstMax_Type()
)
cie1000QosCapabilitiesPortStormFrameBurstMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesPortStormFrameBurstMax.setStatus("current")
_Cie1000QosCapabilitiesIngressMapIdMin_Type = Unsigned32
_Cie1000QosCapabilitiesIngressMapIdMin_Object = MibScalar
cie1000QosCapabilitiesIngressMapIdMin = _Cie1000QosCapabilitiesIngressMapIdMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 59),
    _Cie1000QosCapabilitiesIngressMapIdMin_Type()
)
cie1000QosCapabilitiesIngressMapIdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesIngressMapIdMin.setStatus("current")
_Cie1000QosCapabilitiesIngressMapIdMax_Type = Unsigned32
_Cie1000QosCapabilitiesIngressMapIdMax_Object = MibScalar
cie1000QosCapabilitiesIngressMapIdMax = _Cie1000QosCapabilitiesIngressMapIdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 60),
    _Cie1000QosCapabilitiesIngressMapIdMax_Type()
)
cie1000QosCapabilitiesIngressMapIdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesIngressMapIdMax.setStatus("current")
_Cie1000QosCapabilitiesEgressMapIdMin_Type = Unsigned32
_Cie1000QosCapabilitiesEgressMapIdMin_Object = MibScalar
cie1000QosCapabilitiesEgressMapIdMin = _Cie1000QosCapabilitiesEgressMapIdMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 61),
    _Cie1000QosCapabilitiesEgressMapIdMin_Type()
)
cie1000QosCapabilitiesEgressMapIdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesEgressMapIdMin.setStatus("current")
_Cie1000QosCapabilitiesEgressMapIdMax_Type = Unsigned32
_Cie1000QosCapabilitiesEgressMapIdMax_Object = MibScalar
cie1000QosCapabilitiesEgressMapIdMax = _Cie1000QosCapabilitiesEgressMapIdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 62),
    _Cie1000QosCapabilitiesEgressMapIdMax_Type()
)
cie1000QosCapabilitiesEgressMapIdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesEgressMapIdMax.setStatus("current")
_Cie1000QosCapabilitiesCosIdMin_Type = Unsigned32
_Cie1000QosCapabilitiesCosIdMin_Object = MibScalar
cie1000QosCapabilitiesCosIdMin = _Cie1000QosCapabilitiesCosIdMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 63),
    _Cie1000QosCapabilitiesCosIdMin_Type()
)
cie1000QosCapabilitiesCosIdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesCosIdMin.setStatus("current")
_Cie1000QosCapabilitiesCosIdMax_Type = Unsigned32
_Cie1000QosCapabilitiesCosIdMax_Object = MibScalar
cie1000QosCapabilitiesCosIdMax = _Cie1000QosCapabilitiesCosIdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 64),
    _Cie1000QosCapabilitiesCosIdMax_Type()
)
cie1000QosCapabilitiesCosIdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesCosIdMax.setStatus("current")
_Cie1000QosCapabilitiesQbvGclLenMax_Type = Unsigned32
_Cie1000QosCapabilitiesQbvGclLenMax_Object = MibScalar
cie1000QosCapabilitiesQbvGclLenMax = _Cie1000QosCapabilitiesQbvGclLenMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 65),
    _Cie1000QosCapabilitiesQbvGclLenMax_Type()
)
cie1000QosCapabilitiesQbvGclLenMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesQbvGclLenMax.setStatus("current")
_Cie1000QosCapabilitiesDwrrCountMask_Type = Unsigned32
_Cie1000QosCapabilitiesDwrrCountMask_Object = MibScalar
cie1000QosCapabilitiesDwrrCountMask = _Cie1000QosCapabilitiesDwrrCountMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 101),
    _Cie1000QosCapabilitiesDwrrCountMask_Type()
)
cie1000QosCapabilitiesDwrrCountMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesDwrrCountMask.setStatus("current")
_Cie1000QosCapabilitiesHasGlobalStormPolicers_Type = TruthValue
_Cie1000QosCapabilitiesHasGlobalStormPolicers_Object = MibScalar
cie1000QosCapabilitiesHasGlobalStormPolicers = _Cie1000QosCapabilitiesHasGlobalStormPolicers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 201),
    _Cie1000QosCapabilitiesHasGlobalStormPolicers_Type()
)
cie1000QosCapabilitiesHasGlobalStormPolicers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasGlobalStormPolicers.setStatus("current")
_Cie1000QosCapabilitiesHasPortStormPolicers_Type = TruthValue
_Cie1000QosCapabilitiesHasPortStormPolicers_Object = MibScalar
cie1000QosCapabilitiesHasPortStormPolicers = _Cie1000QosCapabilitiesHasPortStormPolicers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 202),
    _Cie1000QosCapabilitiesHasPortStormPolicers_Type()
)
cie1000QosCapabilitiesHasPortStormPolicers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasPortStormPolicers.setStatus("current")
_Cie1000QosCapabilitiesHasPortQueuePolicers_Type = TruthValue
_Cie1000QosCapabilitiesHasPortQueuePolicers_Object = MibScalar
cie1000QosCapabilitiesHasPortQueuePolicers = _Cie1000QosCapabilitiesHasPortQueuePolicers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 203),
    _Cie1000QosCapabilitiesHasPortQueuePolicers_Type()
)
cie1000QosCapabilitiesHasPortQueuePolicers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasPortQueuePolicers.setStatus("current")
_Cie1000QosCapabilitiesHasWredV1_Type = TruthValue
_Cie1000QosCapabilitiesHasWredV1_Object = MibScalar
cie1000QosCapabilitiesHasWredV1 = _Cie1000QosCapabilitiesHasWredV1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 204),
    _Cie1000QosCapabilitiesHasWredV1_Type()
)
cie1000QosCapabilitiesHasWredV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasWredV1.setStatus("current")
_Cie1000QosCapabilitiesHasWredV2_Type = TruthValue
_Cie1000QosCapabilitiesHasWredV2_Object = MibScalar
cie1000QosCapabilitiesHasWredV2 = _Cie1000QosCapabilitiesHasWredV2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 205),
    _Cie1000QosCapabilitiesHasWredV2_Type()
)
cie1000QosCapabilitiesHasWredV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasWredV2.setStatus("current")
_Cie1000QosCapabilitiesHasFixedTagCosMap_Type = TruthValue
_Cie1000QosCapabilitiesHasFixedTagCosMap_Object = MibScalar
cie1000QosCapabilitiesHasFixedTagCosMap = _Cie1000QosCapabilitiesHasFixedTagCosMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 206),
    _Cie1000QosCapabilitiesHasFixedTagCosMap_Type()
)
cie1000QosCapabilitiesHasFixedTagCosMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasFixedTagCosMap.setStatus("current")
_Cie1000QosCapabilitiesHasTagClassification_Type = TruthValue
_Cie1000QosCapabilitiesHasTagClassification_Object = MibScalar
cie1000QosCapabilitiesHasTagClassification = _Cie1000QosCapabilitiesHasTagClassification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 207),
    _Cie1000QosCapabilitiesHasTagClassification_Type()
)
cie1000QosCapabilitiesHasTagClassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasTagClassification.setStatus("current")
_Cie1000QosCapabilitiesHasTagRemarking_Type = TruthValue
_Cie1000QosCapabilitiesHasTagRemarking_Object = MibScalar
cie1000QosCapabilitiesHasTagRemarking = _Cie1000QosCapabilitiesHasTagRemarking_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 208),
    _Cie1000QosCapabilitiesHasTagRemarking_Type()
)
cie1000QosCapabilitiesHasTagRemarking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasTagRemarking.setStatus("current")
_Cie1000QosCapabilitiesHasDscp_Type = TruthValue
_Cie1000QosCapabilitiesHasDscp_Object = MibScalar
cie1000QosCapabilitiesHasDscp = _Cie1000QosCapabilitiesHasDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 209),
    _Cie1000QosCapabilitiesHasDscp_Type()
)
cie1000QosCapabilitiesHasDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasDscp.setStatus("current")
_Cie1000QosCapabilitiesHasDscpDplClassification_Type = TruthValue
_Cie1000QosCapabilitiesHasDscpDplClassification_Object = MibScalar
cie1000QosCapabilitiesHasDscpDplClassification = _Cie1000QosCapabilitiesHasDscpDplClassification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 210),
    _Cie1000QosCapabilitiesHasDscpDplClassification_Type()
)
cie1000QosCapabilitiesHasDscpDplClassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasDscpDplClassification.setStatus("current")
_Cie1000QosCapabilitiesHasDscpDplRemarking_Type = TruthValue
_Cie1000QosCapabilitiesHasDscpDplRemarking_Object = MibScalar
cie1000QosCapabilitiesHasDscpDplRemarking = _Cie1000QosCapabilitiesHasDscpDplRemarking_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 211),
    _Cie1000QosCapabilitiesHasDscpDplRemarking_Type()
)
cie1000QosCapabilitiesHasDscpDplRemarking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasDscpDplRemarking.setStatus("current")
_Cie1000QosCapabilitiesHasPortPolicersFc_Type = TruthValue
_Cie1000QosCapabilitiesHasPortPolicersFc_Object = MibScalar
cie1000QosCapabilitiesHasPortPolicersFc = _Cie1000QosCapabilitiesHasPortPolicersFc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 212),
    _Cie1000QosCapabilitiesHasPortPolicersFc_Type()
)
cie1000QosCapabilitiesHasPortPolicersFc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasPortPolicersFc.setStatus("current")
_Cie1000QosCapabilitiesHasQueuePolicersFc_Type = TruthValue
_Cie1000QosCapabilitiesHasQueuePolicersFc_Object = MibScalar
cie1000QosCapabilitiesHasQueuePolicersFc = _Cie1000QosCapabilitiesHasQueuePolicersFc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 213),
    _Cie1000QosCapabilitiesHasQueuePolicersFc_Type()
)
cie1000QosCapabilitiesHasQueuePolicersFc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasQueuePolicersFc.setStatus("current")
_Cie1000QosCapabilitiesHasPortShapersDlb_Type = TruthValue
_Cie1000QosCapabilitiesHasPortShapersDlb_Object = MibScalar
cie1000QosCapabilitiesHasPortShapersDlb = _Cie1000QosCapabilitiesHasPortShapersDlb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 214),
    _Cie1000QosCapabilitiesHasPortShapersDlb_Type()
)
cie1000QosCapabilitiesHasPortShapersDlb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasPortShapersDlb.setStatus("current")
_Cie1000QosCapabilitiesHasQueueShapersDlb_Type = TruthValue
_Cie1000QosCapabilitiesHasQueueShapersDlb_Object = MibScalar
cie1000QosCapabilitiesHasQueueShapersDlb = _Cie1000QosCapabilitiesHasQueueShapersDlb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 215),
    _Cie1000QosCapabilitiesHasQueueShapersDlb_Type()
)
cie1000QosCapabilitiesHasQueueShapersDlb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasQueueShapersDlb.setStatus("current")
_Cie1000QosCapabilitiesHasQueueShapersExcess_Type = TruthValue
_Cie1000QosCapabilitiesHasQueueShapersExcess_Object = MibScalar
cie1000QosCapabilitiesHasQueueShapersExcess = _Cie1000QosCapabilitiesHasQueueShapersExcess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 216),
    _Cie1000QosCapabilitiesHasQueueShapersExcess_Type()
)
cie1000QosCapabilitiesHasQueueShapersExcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasQueueShapersExcess.setStatus("current")
_Cie1000QosCapabilitiesHasWredV3_Type = TruthValue
_Cie1000QosCapabilitiesHasWredV3_Object = MibScalar
cie1000QosCapabilitiesHasWredV3 = _Cie1000QosCapabilitiesHasWredV3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 217),
    _Cie1000QosCapabilitiesHasWredV3_Type()
)
cie1000QosCapabilitiesHasWredV3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasWredV3.setStatus("current")
_Cie1000QosCapabilitiesHasQueueShapersCredit_Type = TruthValue
_Cie1000QosCapabilitiesHasQueueShapersCredit_Object = MibScalar
cie1000QosCapabilitiesHasQueueShapersCredit = _Cie1000QosCapabilitiesHasQueueShapersCredit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 218),
    _Cie1000QosCapabilitiesHasQueueShapersCredit_Type()
)
cie1000QosCapabilitiesHasQueueShapersCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasQueueShapersCredit.setStatus("current")
_Cie1000QosCapabilitiesHasQueueCutThrough_Type = TruthValue
_Cie1000QosCapabilitiesHasQueueCutThrough_Object = MibScalar
cie1000QosCapabilitiesHasQueueCutThrough = _Cie1000QosCapabilitiesHasQueueCutThrough_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 219),
    _Cie1000QosCapabilitiesHasQueueCutThrough_Type()
)
cie1000QosCapabilitiesHasQueueCutThrough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasQueueCutThrough.setStatus("current")
_Cie1000QosCapabilitiesHasQce_Type = TruthValue
_Cie1000QosCapabilitiesHasQce_Object = MibScalar
cie1000QosCapabilitiesHasQce = _Cie1000QosCapabilitiesHasQce_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 301),
    _Cie1000QosCapabilitiesHasQce_Type()
)
cie1000QosCapabilitiesHasQce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasQce.setStatus("current")
_Cie1000QosCapabilitiesHasQceAddressMode_Type = TruthValue
_Cie1000QosCapabilitiesHasQceAddressMode_Object = MibScalar
cie1000QosCapabilitiesHasQceAddressMode = _Cie1000QosCapabilitiesHasQceAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 302),
    _Cie1000QosCapabilitiesHasQceAddressMode_Type()
)
cie1000QosCapabilitiesHasQceAddressMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasQceAddressMode.setStatus("current")
_Cie1000QosCapabilitiesHasQceKeyType_Type = TruthValue
_Cie1000QosCapabilitiesHasQceKeyType_Object = MibScalar
cie1000QosCapabilitiesHasQceKeyType = _Cie1000QosCapabilitiesHasQceKeyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 303),
    _Cie1000QosCapabilitiesHasQceKeyType_Type()
)
cie1000QosCapabilitiesHasQceKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasQceKeyType.setStatus("current")
_Cie1000QosCapabilitiesHasQceMacOui_Type = TruthValue
_Cie1000QosCapabilitiesHasQceMacOui_Object = MibScalar
cie1000QosCapabilitiesHasQceMacOui = _Cie1000QosCapabilitiesHasQceMacOui_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 304),
    _Cie1000QosCapabilitiesHasQceMacOui_Type()
)
cie1000QosCapabilitiesHasQceMacOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasQceMacOui.setStatus("current")
_Cie1000QosCapabilitiesHasQceDmac_Type = TruthValue
_Cie1000QosCapabilitiesHasQceDmac_Object = MibScalar
cie1000QosCapabilitiesHasQceDmac = _Cie1000QosCapabilitiesHasQceDmac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 305),
    _Cie1000QosCapabilitiesHasQceDmac_Type()
)
cie1000QosCapabilitiesHasQceDmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasQceDmac.setStatus("current")
_Cie1000QosCapabilitiesHasQceDip_Type = TruthValue
_Cie1000QosCapabilitiesHasQceDip_Object = MibScalar
cie1000QosCapabilitiesHasQceDip = _Cie1000QosCapabilitiesHasQceDip_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 306),
    _Cie1000QosCapabilitiesHasQceDip_Type()
)
cie1000QosCapabilitiesHasQceDip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasQceDip.setStatus("current")
_Cie1000QosCapabilitiesHasQceCTag_Type = TruthValue
_Cie1000QosCapabilitiesHasQceCTag_Object = MibScalar
cie1000QosCapabilitiesHasQceCTag = _Cie1000QosCapabilitiesHasQceCTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 307),
    _Cie1000QosCapabilitiesHasQceCTag_Type()
)
cie1000QosCapabilitiesHasQceCTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasQceCTag.setStatus("current")
_Cie1000QosCapabilitiesHasQceSTag_Type = TruthValue
_Cie1000QosCapabilitiesHasQceSTag_Object = MibScalar
cie1000QosCapabilitiesHasQceSTag = _Cie1000QosCapabilitiesHasQceSTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 308),
    _Cie1000QosCapabilitiesHasQceSTag_Type()
)
cie1000QosCapabilitiesHasQceSTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasQceSTag.setStatus("current")
_Cie1000QosCapabilitiesHasQceInnerTag_Type = TruthValue
_Cie1000QosCapabilitiesHasQceInnerTag_Object = MibScalar
cie1000QosCapabilitiesHasQceInnerTag = _Cie1000QosCapabilitiesHasQceInnerTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 309),
    _Cie1000QosCapabilitiesHasQceInnerTag_Type()
)
cie1000QosCapabilitiesHasQceInnerTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasQceInnerTag.setStatus("current")
_Cie1000QosCapabilitiesHasQceActionPcpDei_Type = TruthValue
_Cie1000QosCapabilitiesHasQceActionPcpDei_Object = MibScalar
cie1000QosCapabilitiesHasQceActionPcpDei = _Cie1000QosCapabilitiesHasQceActionPcpDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 310),
    _Cie1000QosCapabilitiesHasQceActionPcpDei_Type()
)
cie1000QosCapabilitiesHasQceActionPcpDei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasQceActionPcpDei.setStatus("current")
_Cie1000QosCapabilitiesHasQceActionPolicy_Type = TruthValue
_Cie1000QosCapabilitiesHasQceActionPolicy_Object = MibScalar
cie1000QosCapabilitiesHasQceActionPolicy = _Cie1000QosCapabilitiesHasQceActionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 311),
    _Cie1000QosCapabilitiesHasQceActionPolicy_Type()
)
cie1000QosCapabilitiesHasQceActionPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasQceActionPolicy.setStatus("current")
_Cie1000QosCapabilitiesHasShapersRt_Type = TruthValue
_Cie1000QosCapabilitiesHasShapersRt_Object = MibScalar
cie1000QosCapabilitiesHasShapersRt = _Cie1000QosCapabilitiesHasShapersRt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 312),
    _Cie1000QosCapabilitiesHasShapersRt_Type()
)
cie1000QosCapabilitiesHasShapersRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasShapersRt.setStatus("current")
_Cie1000QosCapabilitiesHasQceActionMap_Type = TruthValue
_Cie1000QosCapabilitiesHasQceActionMap_Object = MibScalar
cie1000QosCapabilitiesHasQceActionMap = _Cie1000QosCapabilitiesHasQceActionMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 313),
    _Cie1000QosCapabilitiesHasQceActionMap_Type()
)
cie1000QosCapabilitiesHasQceActionMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasQceActionMap.setStatus("current")
_Cie1000QosCapabilitiesHasIngressMap_Type = TruthValue
_Cie1000QosCapabilitiesHasIngressMap_Object = MibScalar
cie1000QosCapabilitiesHasIngressMap = _Cie1000QosCapabilitiesHasIngressMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 314),
    _Cie1000QosCapabilitiesHasIngressMap_Type()
)
cie1000QosCapabilitiesHasIngressMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasIngressMap.setStatus("current")
_Cie1000QosCapabilitiesHasEgressMap_Type = TruthValue
_Cie1000QosCapabilitiesHasEgressMap_Object = MibScalar
cie1000QosCapabilitiesHasEgressMap = _Cie1000QosCapabilitiesHasEgressMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 315),
    _Cie1000QosCapabilitiesHasEgressMap_Type()
)
cie1000QosCapabilitiesHasEgressMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasEgressMap.setStatus("current")
_Cie1000QosCapabilitiesHasWred2orWredw3_Type = TruthValue
_Cie1000QosCapabilitiesHasWred2orWredw3_Object = MibScalar
cie1000QosCapabilitiesHasWred2orWredw3 = _Cie1000QosCapabilitiesHasWred2orWredw3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 316),
    _Cie1000QosCapabilitiesHasWred2orWredw3_Type()
)
cie1000QosCapabilitiesHasWred2orWredw3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasWred2orWredw3.setStatus("current")
_Cie1000QosCapabilitiesHasDscpDp2_Type = TruthValue
_Cie1000QosCapabilitiesHasDscpDp2_Object = MibScalar
cie1000QosCapabilitiesHasDscpDp2 = _Cie1000QosCapabilitiesHasDscpDp2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 317),
    _Cie1000QosCapabilitiesHasDscpDp2_Type()
)
cie1000QosCapabilitiesHasDscpDp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasDscpDp2.setStatus("current")
_Cie1000QosCapabilitiesHasDscpDp3_Type = TruthValue
_Cie1000QosCapabilitiesHasDscpDp3_Object = MibScalar
cie1000QosCapabilitiesHasDscpDp3 = _Cie1000QosCapabilitiesHasDscpDp3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 318),
    _Cie1000QosCapabilitiesHasDscpDp3_Type()
)
cie1000QosCapabilitiesHasDscpDp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasDscpDp3.setStatus("current")
_Cie1000QosCapabilitiesHasDefaultPcpAndDei_Type = TruthValue
_Cie1000QosCapabilitiesHasDefaultPcpAndDei_Object = MibScalar
cie1000QosCapabilitiesHasDefaultPcpAndDei = _Cie1000QosCapabilitiesHasDefaultPcpAndDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 319),
    _Cie1000QosCapabilitiesHasDefaultPcpAndDei_Type()
)
cie1000QosCapabilitiesHasDefaultPcpAndDei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasDefaultPcpAndDei.setStatus("current")
_Cie1000QosCapabilitiesHasTrustTag_Type = TruthValue
_Cie1000QosCapabilitiesHasTrustTag_Object = MibScalar
cie1000QosCapabilitiesHasTrustTag = _Cie1000QosCapabilitiesHasTrustTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 320),
    _Cie1000QosCapabilitiesHasTrustTag_Type()
)
cie1000QosCapabilitiesHasTrustTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasTrustTag.setStatus("current")
_Cie1000QosCapabilitiesHasCosIdClassification_Type = TruthValue
_Cie1000QosCapabilitiesHasCosIdClassification_Object = MibScalar
cie1000QosCapabilitiesHasCosIdClassification = _Cie1000QosCapabilitiesHasCosIdClassification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 321),
    _Cie1000QosCapabilitiesHasCosIdClassification_Type()
)
cie1000QosCapabilitiesHasCosIdClassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasCosIdClassification.setStatus("current")
_Cie1000QosCapabilitiesHasQbv_Type = TruthValue
_Cie1000QosCapabilitiesHasQbv_Object = MibScalar
cie1000QosCapabilitiesHasQbv = _Cie1000QosCapabilitiesHasQbv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 1, 322),
    _Cie1000QosCapabilitiesHasQbv_Type()
)
cie1000QosCapabilitiesHasQbv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesHasQbv.setStatus("current")
_Cie1000QosConfig_ObjectIdentity = ObjectIdentity
cie1000QosConfig = _Cie1000QosConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2)
)
_Cie1000QosConfigGlobals_ObjectIdentity = ObjectIdentity
cie1000QosConfigGlobals = _Cie1000QosConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1)
)
_Cie1000QosConfigGlobalsStormPolicers_ObjectIdentity = ObjectIdentity
cie1000QosConfigGlobalsStormPolicers = _Cie1000QosConfigGlobalsStormPolicers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 1)
)
_Cie1000QosConfigGlobalsStormPolicersUnicast_ObjectIdentity = ObjectIdentity
cie1000QosConfigGlobalsStormPolicersUnicast = _Cie1000QosConfigGlobalsStormPolicersUnicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 1, 1)
)
_Cie1000QosConfigGlobalsStormPolicersUnicastEnable_Type = TruthValue
_Cie1000QosConfigGlobalsStormPolicersUnicastEnable_Object = MibScalar
cie1000QosConfigGlobalsStormPolicersUnicastEnable = _Cie1000QosConfigGlobalsStormPolicersUnicastEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 1, 1, 1),
    _Cie1000QosConfigGlobalsStormPolicersUnicastEnable_Type()
)
cie1000QosConfigGlobalsStormPolicersUnicastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsStormPolicersUnicastEnable.setStatus("current")
_Cie1000QosConfigGlobalsStormPolicersUnicastRate_Type = Unsigned32
_Cie1000QosConfigGlobalsStormPolicersUnicastRate_Object = MibScalar
cie1000QosConfigGlobalsStormPolicersUnicastRate = _Cie1000QosConfigGlobalsStormPolicersUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 1, 1, 2),
    _Cie1000QosConfigGlobalsStormPolicersUnicastRate_Type()
)
cie1000QosConfigGlobalsStormPolicersUnicastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsStormPolicersUnicastRate.setStatus("current")
_Cie1000QosConfigGlobalsStormPolicersUnicastFrameRate_Type = TruthValue
_Cie1000QosConfigGlobalsStormPolicersUnicastFrameRate_Object = MibScalar
cie1000QosConfigGlobalsStormPolicersUnicastFrameRate = _Cie1000QosConfigGlobalsStormPolicersUnicastFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 1, 1, 3),
    _Cie1000QosConfigGlobalsStormPolicersUnicastFrameRate_Type()
)
cie1000QosConfigGlobalsStormPolicersUnicastFrameRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsStormPolicersUnicastFrameRate.setStatus("current")
_Cie1000QosConfigGlobalsStormPolicersMulticast_ObjectIdentity = ObjectIdentity
cie1000QosConfigGlobalsStormPolicersMulticast = _Cie1000QosConfigGlobalsStormPolicersMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 1, 2)
)
_Cie1000QosConfigGlobalsStormPolicersMulticastEnable_Type = TruthValue
_Cie1000QosConfigGlobalsStormPolicersMulticastEnable_Object = MibScalar
cie1000QosConfigGlobalsStormPolicersMulticastEnable = _Cie1000QosConfigGlobalsStormPolicersMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 1, 2, 1),
    _Cie1000QosConfigGlobalsStormPolicersMulticastEnable_Type()
)
cie1000QosConfigGlobalsStormPolicersMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsStormPolicersMulticastEnable.setStatus("current")
_Cie1000QosConfigGlobalsStormPolicersMulticastRate_Type = Unsigned32
_Cie1000QosConfigGlobalsStormPolicersMulticastRate_Object = MibScalar
cie1000QosConfigGlobalsStormPolicersMulticastRate = _Cie1000QosConfigGlobalsStormPolicersMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 1, 2, 2),
    _Cie1000QosConfigGlobalsStormPolicersMulticastRate_Type()
)
cie1000QosConfigGlobalsStormPolicersMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsStormPolicersMulticastRate.setStatus("current")
_Cie1000QosConfigGlobalsStormPolicersMulticastFrameRate_Type = TruthValue
_Cie1000QosConfigGlobalsStormPolicersMulticastFrameRate_Object = MibScalar
cie1000QosConfigGlobalsStormPolicersMulticastFrameRate = _Cie1000QosConfigGlobalsStormPolicersMulticastFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 1, 2, 3),
    _Cie1000QosConfigGlobalsStormPolicersMulticastFrameRate_Type()
)
cie1000QosConfigGlobalsStormPolicersMulticastFrameRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsStormPolicersMulticastFrameRate.setStatus("current")
_Cie1000QosConfigGlobalsStormPolicersBroadcast_ObjectIdentity = ObjectIdentity
cie1000QosConfigGlobalsStormPolicersBroadcast = _Cie1000QosConfigGlobalsStormPolicersBroadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 1, 3)
)
_Cie1000QosConfigGlobalsStormPolicersBroadcastEnable_Type = TruthValue
_Cie1000QosConfigGlobalsStormPolicersBroadcastEnable_Object = MibScalar
cie1000QosConfigGlobalsStormPolicersBroadcastEnable = _Cie1000QosConfigGlobalsStormPolicersBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 1, 3, 1),
    _Cie1000QosConfigGlobalsStormPolicersBroadcastEnable_Type()
)
cie1000QosConfigGlobalsStormPolicersBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsStormPolicersBroadcastEnable.setStatus("current")
_Cie1000QosConfigGlobalsStormPolicersBroadcastRate_Type = Unsigned32
_Cie1000QosConfigGlobalsStormPolicersBroadcastRate_Object = MibScalar
cie1000QosConfigGlobalsStormPolicersBroadcastRate = _Cie1000QosConfigGlobalsStormPolicersBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 1, 3, 2),
    _Cie1000QosConfigGlobalsStormPolicersBroadcastRate_Type()
)
cie1000QosConfigGlobalsStormPolicersBroadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsStormPolicersBroadcastRate.setStatus("current")
_Cie1000QosConfigGlobalsStormPolicersBroadcastFrameRate_Type = TruthValue
_Cie1000QosConfigGlobalsStormPolicersBroadcastFrameRate_Object = MibScalar
cie1000QosConfigGlobalsStormPolicersBroadcastFrameRate = _Cie1000QosConfigGlobalsStormPolicersBroadcastFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 1, 3, 3),
    _Cie1000QosConfigGlobalsStormPolicersBroadcastFrameRate_Type()
)
cie1000QosConfigGlobalsStormPolicersBroadcastFrameRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsStormPolicersBroadcastFrameRate.setStatus("current")
_Cie1000QosConfigGlobalsWredTable_Object = MibTable
cie1000QosConfigGlobalsWredTable = _Cie1000QosConfigGlobalsWredTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsWredTable.setStatus("current")
_Cie1000QosConfigGlobalsWredEntry_Object = MibTableRow
cie1000QosConfigGlobalsWredEntry = _Cie1000QosConfigGlobalsWredEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 2, 1)
)
cie1000QosConfigGlobalsWredEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigGlobalsWredGroup"),
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigGlobalsWredQueue"),
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigGlobalsWredDpl"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsWredEntry.setStatus("current")


class _Cie1000QosConfigGlobalsWredGroup_Type(Integer32):
    """Custom type cie1000QosConfigGlobalsWredGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Cie1000QosConfigGlobalsWredGroup_Type.__name__ = "Integer32"
_Cie1000QosConfigGlobalsWredGroup_Object = MibTableColumn
cie1000QosConfigGlobalsWredGroup = _Cie1000QosConfigGlobalsWredGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 2, 1, 1),
    _Cie1000QosConfigGlobalsWredGroup_Type()
)
cie1000QosConfigGlobalsWredGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsWredGroup.setStatus("current")


class _Cie1000QosConfigGlobalsWredQueue_Type(Integer32):
    """Custom type cie1000QosConfigGlobalsWredQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cie1000QosConfigGlobalsWredQueue_Type.__name__ = "Integer32"
_Cie1000QosConfigGlobalsWredQueue_Object = MibTableColumn
cie1000QosConfigGlobalsWredQueue = _Cie1000QosConfigGlobalsWredQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 2, 1, 2),
    _Cie1000QosConfigGlobalsWredQueue_Type()
)
cie1000QosConfigGlobalsWredQueue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsWredQueue.setStatus("current")


class _Cie1000QosConfigGlobalsWredDpl_Type(Integer32):
    """Custom type cie1000QosConfigGlobalsWredDpl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Cie1000QosConfigGlobalsWredDpl_Type.__name__ = "Integer32"
_Cie1000QosConfigGlobalsWredDpl_Object = MibTableColumn
cie1000QosConfigGlobalsWredDpl = _Cie1000QosConfigGlobalsWredDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 2, 1, 3),
    _Cie1000QosConfigGlobalsWredDpl_Type()
)
cie1000QosConfigGlobalsWredDpl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsWredDpl.setStatus("current")
_Cie1000QosConfigGlobalsWredEnable_Type = TruthValue
_Cie1000QosConfigGlobalsWredEnable_Object = MibTableColumn
cie1000QosConfigGlobalsWredEnable = _Cie1000QosConfigGlobalsWredEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 2, 1, 4),
    _Cie1000QosConfigGlobalsWredEnable_Type()
)
cie1000QosConfigGlobalsWredEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsWredEnable.setStatus("current")
_Cie1000QosConfigGlobalsWredMinimumFillLevel_Type = CIE1000Percent
_Cie1000QosConfigGlobalsWredMinimumFillLevel_Object = MibTableColumn
cie1000QosConfigGlobalsWredMinimumFillLevel = _Cie1000QosConfigGlobalsWredMinimumFillLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 2, 1, 5),
    _Cie1000QosConfigGlobalsWredMinimumFillLevel_Type()
)
cie1000QosConfigGlobalsWredMinimumFillLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsWredMinimumFillLevel.setStatus("current")
_Cie1000QosConfigGlobalsWredMaximum_Type = CIE1000Percent
_Cie1000QosConfigGlobalsWredMaximum_Object = MibTableColumn
cie1000QosConfigGlobalsWredMaximum = _Cie1000QosConfigGlobalsWredMaximum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 2, 1, 6),
    _Cie1000QosConfigGlobalsWredMaximum_Type()
)
cie1000QosConfigGlobalsWredMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsWredMaximum.setStatus("current")
_Cie1000QosConfigGlobalsWredMaxSelector_Type = CIE1000QosWredMaxSelector
_Cie1000QosConfigGlobalsWredMaxSelector_Object = MibTableColumn
cie1000QosConfigGlobalsWredMaxSelector = _Cie1000QosConfigGlobalsWredMaxSelector_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 2, 1, 7),
    _Cie1000QosConfigGlobalsWredMaxSelector_Type()
)
cie1000QosConfigGlobalsWredMaxSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsWredMaxSelector.setStatus("current")
_Cie1000QosConfigGlobalsWredMaximumDp1_Type = CIE1000Percent
_Cie1000QosConfigGlobalsWredMaximumDp1_Object = MibTableColumn
cie1000QosConfigGlobalsWredMaximumDp1 = _Cie1000QosConfigGlobalsWredMaximumDp1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 2, 1, 8),
    _Cie1000QosConfigGlobalsWredMaximumDp1_Type()
)
cie1000QosConfigGlobalsWredMaximumDp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsWredMaximumDp1.setStatus("current")
_Cie1000QosConfigGlobalsWredMaximumDp2_Type = CIE1000Percent
_Cie1000QosConfigGlobalsWredMaximumDp2_Object = MibTableColumn
cie1000QosConfigGlobalsWredMaximumDp2 = _Cie1000QosConfigGlobalsWredMaximumDp2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 2, 1, 9),
    _Cie1000QosConfigGlobalsWredMaximumDp2_Type()
)
cie1000QosConfigGlobalsWredMaximumDp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsWredMaximumDp2.setStatus("current")
_Cie1000QosConfigGlobalsWredMaximumDp3_Type = CIE1000Percent
_Cie1000QosConfigGlobalsWredMaximumDp3_Object = MibTableColumn
cie1000QosConfigGlobalsWredMaximumDp3 = _Cie1000QosConfigGlobalsWredMaximumDp3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 2, 1, 10),
    _Cie1000QosConfigGlobalsWredMaximumDp3_Type()
)
cie1000QosConfigGlobalsWredMaximumDp3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsWredMaximumDp3.setStatus("current")
_Cie1000QosConfigGlobalsDscpTable_Object = MibTable
cie1000QosConfigGlobalsDscpTable = _Cie1000QosConfigGlobalsDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsDscpTable.setStatus("current")
_Cie1000QosConfigGlobalsDscpEntry_Object = MibTableRow
cie1000QosConfigGlobalsDscpEntry = _Cie1000QosConfigGlobalsDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 3, 1)
)
cie1000QosConfigGlobalsDscpEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigGlobalsDscpDscp"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsDscpEntry.setStatus("current")
_Cie1000QosConfigGlobalsDscpDscp_Type = Dscp
_Cie1000QosConfigGlobalsDscpDscp_Object = MibTableColumn
cie1000QosConfigGlobalsDscpDscp = _Cie1000QosConfigGlobalsDscpDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 3, 1, 1),
    _Cie1000QosConfigGlobalsDscpDscp_Type()
)
cie1000QosConfigGlobalsDscpDscp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsDscpDscp.setStatus("current")
_Cie1000QosConfigGlobalsDscpTrust_Type = TruthValue
_Cie1000QosConfigGlobalsDscpTrust_Object = MibTableColumn
cie1000QosConfigGlobalsDscpTrust = _Cie1000QosConfigGlobalsDscpTrust_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 3, 1, 2),
    _Cie1000QosConfigGlobalsDscpTrust_Type()
)
cie1000QosConfigGlobalsDscpTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsDscpTrust.setStatus("current")
_Cie1000QosConfigGlobalsDscpCos_Type = Unsigned32
_Cie1000QosConfigGlobalsDscpCos_Object = MibTableColumn
cie1000QosConfigGlobalsDscpCos = _Cie1000QosConfigGlobalsDscpCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 3, 1, 3),
    _Cie1000QosConfigGlobalsDscpCos_Type()
)
cie1000QosConfigGlobalsDscpCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsDscpCos.setStatus("current")
_Cie1000QosConfigGlobalsDscpDpl_Type = CIE1000Unsigned8
_Cie1000QosConfigGlobalsDscpDpl_Object = MibTableColumn
cie1000QosConfigGlobalsDscpDpl = _Cie1000QosConfigGlobalsDscpDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 3, 1, 4),
    _Cie1000QosConfigGlobalsDscpDpl_Type()
)
cie1000QosConfigGlobalsDscpDpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsDscpDpl.setStatus("current")
_Cie1000QosConfigGlobalsDscpIngressTranslation_Type = Dscp
_Cie1000QosConfigGlobalsDscpIngressTranslation_Object = MibTableColumn
cie1000QosConfigGlobalsDscpIngressTranslation = _Cie1000QosConfigGlobalsDscpIngressTranslation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 3, 1, 5),
    _Cie1000QosConfigGlobalsDscpIngressTranslation_Type()
)
cie1000QosConfigGlobalsDscpIngressTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsDscpIngressTranslation.setStatus("current")
_Cie1000QosConfigGlobalsDscpClassify_Type = TruthValue
_Cie1000QosConfigGlobalsDscpClassify_Object = MibTableColumn
cie1000QosConfigGlobalsDscpClassify = _Cie1000QosConfigGlobalsDscpClassify_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 3, 1, 6),
    _Cie1000QosConfigGlobalsDscpClassify_Type()
)
cie1000QosConfigGlobalsDscpClassify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsDscpClassify.setStatus("current")
_Cie1000QosConfigGlobalsDscpEgressTranslation_Type = Dscp
_Cie1000QosConfigGlobalsDscpEgressTranslation_Object = MibTableColumn
cie1000QosConfigGlobalsDscpEgressTranslation = _Cie1000QosConfigGlobalsDscpEgressTranslation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 3, 1, 7),
    _Cie1000QosConfigGlobalsDscpEgressTranslation_Type()
)
cie1000QosConfigGlobalsDscpEgressTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsDscpEgressTranslation.setStatus("current")
_Cie1000QosConfigGlobalsDscpEgressTranslationDp1_Type = Dscp
_Cie1000QosConfigGlobalsDscpEgressTranslationDp1_Object = MibTableColumn
cie1000QosConfigGlobalsDscpEgressTranslationDp1 = _Cie1000QosConfigGlobalsDscpEgressTranslationDp1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 3, 1, 8),
    _Cie1000QosConfigGlobalsDscpEgressTranslationDp1_Type()
)
cie1000QosConfigGlobalsDscpEgressTranslationDp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsDscpEgressTranslationDp1.setStatus("current")
_Cie1000QosConfigGlobalsCosToDscpTable_Object = MibTable
cie1000QosConfigGlobalsCosToDscpTable = _Cie1000QosConfigGlobalsCosToDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsCosToDscpTable.setStatus("current")
_Cie1000QosConfigGlobalsCosToDscpEntry_Object = MibTableRow
cie1000QosConfigGlobalsCosToDscpEntry = _Cie1000QosConfigGlobalsCosToDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 4, 1)
)
cie1000QosConfigGlobalsCosToDscpEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigGlobalsCosToDscpCos"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsCosToDscpEntry.setStatus("current")


class _Cie1000QosConfigGlobalsCosToDscpCos_Type(Integer32):
    """Custom type cie1000QosConfigGlobalsCosToDscpCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cie1000QosConfigGlobalsCosToDscpCos_Type.__name__ = "Integer32"
_Cie1000QosConfigGlobalsCosToDscpCos_Object = MibTableColumn
cie1000QosConfigGlobalsCosToDscpCos = _Cie1000QosConfigGlobalsCosToDscpCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 4, 1, 1),
    _Cie1000QosConfigGlobalsCosToDscpCos_Type()
)
cie1000QosConfigGlobalsCosToDscpCos.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsCosToDscpCos.setStatus("current")
_Cie1000QosConfigGlobalsCosToDscpDscp_Type = Dscp
_Cie1000QosConfigGlobalsCosToDscpDscp_Object = MibTableColumn
cie1000QosConfigGlobalsCosToDscpDscp = _Cie1000QosConfigGlobalsCosToDscpDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 4, 1, 2),
    _Cie1000QosConfigGlobalsCosToDscpDscp_Type()
)
cie1000QosConfigGlobalsCosToDscpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsCosToDscpDscp.setStatus("current")
_Cie1000QosConfigGlobalsCosToDscpDscpDp1_Type = Dscp
_Cie1000QosConfigGlobalsCosToDscpDscpDp1_Object = MibTableColumn
cie1000QosConfigGlobalsCosToDscpDscpDp1 = _Cie1000QosConfigGlobalsCosToDscpDscpDp1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 4, 1, 3),
    _Cie1000QosConfigGlobalsCosToDscpDscpDp1_Type()
)
cie1000QosConfigGlobalsCosToDscpDscpDp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsCosToDscpDscpDp1.setStatus("current")
_Cie1000QosConfigGlobalsCosToDscpDscpDp2_Type = Dscp
_Cie1000QosConfigGlobalsCosToDscpDscpDp2_Object = MibTableColumn
cie1000QosConfigGlobalsCosToDscpDscpDp2 = _Cie1000QosConfigGlobalsCosToDscpDscpDp2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 4, 1, 4),
    _Cie1000QosConfigGlobalsCosToDscpDscpDp2_Type()
)
cie1000QosConfigGlobalsCosToDscpDscpDp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsCosToDscpDscpDp2.setStatus("current")
_Cie1000QosConfigGlobalsCosToDscpDscpDp3_Type = Dscp
_Cie1000QosConfigGlobalsCosToDscpDscpDp3_Object = MibTableColumn
cie1000QosConfigGlobalsCosToDscpDscpDp3 = _Cie1000QosConfigGlobalsCosToDscpDscpDp3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 1, 4, 1, 5),
    _Cie1000QosConfigGlobalsCosToDscpDscpDp3_Type()
)
cie1000QosConfigGlobalsCosToDscpDscpDp3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsCosToDscpDscpDp3.setStatus("current")
_Cie1000QosConfigInterface_ObjectIdentity = ObjectIdentity
cie1000QosConfigInterface = _Cie1000QosConfigInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2)
)
_Cie1000QosConfigInterfaceTable_Object = MibTable
cie1000QosConfigInterfaceTable = _Cie1000QosConfigInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceTable.setStatus("current")
_Cie1000QosConfigInterfaceEntry_Object = MibTableRow
cie1000QosConfigInterfaceEntry = _Cie1000QosConfigInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1)
)
cie1000QosConfigInterfaceEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceEntry.setStatus("current")
_Cie1000QosConfigInterfaceIfIndex_Type = CIE1000InterfaceIndex
_Cie1000QosConfigInterfaceIfIndex_Object = MibTableColumn
cie1000QosConfigInterfaceIfIndex = _Cie1000QosConfigInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 1),
    _Cie1000QosConfigInterfaceIfIndex_Type()
)
cie1000QosConfigInterfaceIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceIfIndex.setStatus("current")
_Cie1000QosConfigInterfaceCos_Type = Unsigned32
_Cie1000QosConfigInterfaceCos_Object = MibTableColumn
cie1000QosConfigInterfaceCos = _Cie1000QosConfigInterfaceCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 2),
    _Cie1000QosConfigInterfaceCos_Type()
)
cie1000QosConfigInterfaceCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceCos.setStatus("current")
_Cie1000QosConfigInterfaceDpl_Type = CIE1000Unsigned8
_Cie1000QosConfigInterfaceDpl_Object = MibTableColumn
cie1000QosConfigInterfaceDpl = _Cie1000QosConfigInterfaceDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 3),
    _Cie1000QosConfigInterfaceDpl_Type()
)
cie1000QosConfigInterfaceDpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceDpl.setStatus("current")
_Cie1000QosConfigInterfacePcp_Type = Unsigned32
_Cie1000QosConfigInterfacePcp_Object = MibTableColumn
cie1000QosConfigInterfacePcp = _Cie1000QosConfigInterfacePcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 4),
    _Cie1000QosConfigInterfacePcp_Type()
)
cie1000QosConfigInterfacePcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfacePcp.setStatus("current")
_Cie1000QosConfigInterfaceDei_Type = CIE1000Unsigned8
_Cie1000QosConfigInterfaceDei_Object = MibTableColumn
cie1000QosConfigInterfaceDei = _Cie1000QosConfigInterfaceDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 5),
    _Cie1000QosConfigInterfaceDei_Type()
)
cie1000QosConfigInterfaceDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceDei.setStatus("current")
_Cie1000QosConfigInterfaceTrustTag_Type = TruthValue
_Cie1000QosConfigInterfaceTrustTag_Object = MibTableColumn
cie1000QosConfigInterfaceTrustTag = _Cie1000QosConfigInterfaceTrustTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 6),
    _Cie1000QosConfigInterfaceTrustTag_Type()
)
cie1000QosConfigInterfaceTrustTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceTrustTag.setStatus("current")
_Cie1000QosConfigInterfaceTrustDscp_Type = TruthValue
_Cie1000QosConfigInterfaceTrustDscp_Object = MibTableColumn
cie1000QosConfigInterfaceTrustDscp = _Cie1000QosConfigInterfaceTrustDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 7),
    _Cie1000QosConfigInterfaceTrustDscp_Type()
)
cie1000QosConfigInterfaceTrustDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceTrustDscp.setStatus("current")
_Cie1000QosConfigInterfaceDwrrCount_Type = CIE1000Unsigned8
_Cie1000QosConfigInterfaceDwrrCount_Object = MibTableColumn
cie1000QosConfigInterfaceDwrrCount = _Cie1000QosConfigInterfaceDwrrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 8),
    _Cie1000QosConfigInterfaceDwrrCount_Type()
)
cie1000QosConfigInterfaceDwrrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceDwrrCount.setStatus("current")
_Cie1000QosConfigInterfaceTagRemarkingMode_Type = CIE1000QosTagRemarkingMode
_Cie1000QosConfigInterfaceTagRemarkingMode_Object = MibTableColumn
cie1000QosConfigInterfaceTagRemarkingMode = _Cie1000QosConfigInterfaceTagRemarkingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 9),
    _Cie1000QosConfigInterfaceTagRemarkingMode_Type()
)
cie1000QosConfigInterfaceTagRemarkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceTagRemarkingMode.setStatus("current")
_Cie1000QosConfigInterfaceTagPcp_Type = Unsigned32
_Cie1000QosConfigInterfaceTagPcp_Object = MibTableColumn
cie1000QosConfigInterfaceTagPcp = _Cie1000QosConfigInterfaceTagPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 10),
    _Cie1000QosConfigInterfaceTagPcp_Type()
)
cie1000QosConfigInterfaceTagPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceTagPcp.setStatus("current")
_Cie1000QosConfigInterfaceTagDei_Type = CIE1000Unsigned8
_Cie1000QosConfigInterfaceTagDei_Object = MibTableColumn
cie1000QosConfigInterfaceTagDei = _Cie1000QosConfigInterfaceTagDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 11),
    _Cie1000QosConfigInterfaceTagDei_Type()
)
cie1000QosConfigInterfaceTagDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceTagDei.setStatus("current")
_Cie1000QosConfigInterfaceDscpTranslate_Type = TruthValue
_Cie1000QosConfigInterfaceDscpTranslate_Object = MibTableColumn
cie1000QosConfigInterfaceDscpTranslate = _Cie1000QosConfigInterfaceDscpTranslate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 12),
    _Cie1000QosConfigInterfaceDscpTranslate_Type()
)
cie1000QosConfigInterfaceDscpTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceDscpTranslate.setStatus("current")
_Cie1000QosConfigInterfaceDscpClassify_Type = CIE1000QosDscpClassify
_Cie1000QosConfigInterfaceDscpClassify_Object = MibTableColumn
cie1000QosConfigInterfaceDscpClassify = _Cie1000QosConfigInterfaceDscpClassify_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 13),
    _Cie1000QosConfigInterfaceDscpClassify_Type()
)
cie1000QosConfigInterfaceDscpClassify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceDscpClassify.setStatus("current")
_Cie1000QosConfigInterfaceDscpRemark_Type = CIE1000QosDscpRemark
_Cie1000QosConfigInterfaceDscpRemark_Object = MibTableColumn
cie1000QosConfigInterfaceDscpRemark = _Cie1000QosConfigInterfaceDscpRemark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 14),
    _Cie1000QosConfigInterfaceDscpRemark_Type()
)
cie1000QosConfigInterfaceDscpRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceDscpRemark.setStatus("current")
_Cie1000QosConfigInterfaceQceAddressMode_Type = TruthValue
_Cie1000QosConfigInterfaceQceAddressMode_Object = MibTableColumn
cie1000QosConfigInterfaceQceAddressMode = _Cie1000QosConfigInterfaceQceAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 15),
    _Cie1000QosConfigInterfaceQceAddressMode_Type()
)
cie1000QosConfigInterfaceQceAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQceAddressMode.setStatus("current")
_Cie1000QosConfigInterfaceQceKeyType_Type = CIE1000VcapKeyType
_Cie1000QosConfigInterfaceQceKeyType_Object = MibTableColumn
cie1000QosConfigInterfaceQceKeyType = _Cie1000QosConfigInterfaceQceKeyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 16),
    _Cie1000QosConfigInterfaceQceKeyType_Type()
)
cie1000QosConfigInterfaceQceKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQceKeyType.setStatus("current")
_Cie1000QosConfigInterfaceWredGroup_Type = Unsigned32
_Cie1000QosConfigInterfaceWredGroup_Object = MibTableColumn
cie1000QosConfigInterfaceWredGroup = _Cie1000QosConfigInterfaceWredGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 17),
    _Cie1000QosConfigInterfaceWredGroup_Type()
)
cie1000QosConfigInterfaceWredGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceWredGroup.setStatus("current")
_Cie1000QosConfigInterfaceIngressMap_Type = CIE1000Unsigned16
_Cie1000QosConfigInterfaceIngressMap_Object = MibTableColumn
cie1000QosConfigInterfaceIngressMap = _Cie1000QosConfigInterfaceIngressMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 18),
    _Cie1000QosConfigInterfaceIngressMap_Type()
)
cie1000QosConfigInterfaceIngressMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceIngressMap.setStatus("current")
_Cie1000QosConfigInterfaceEgressMap_Type = CIE1000Unsigned16
_Cie1000QosConfigInterfaceEgressMap_Object = MibTableColumn
cie1000QosConfigInterfaceEgressMap = _Cie1000QosConfigInterfaceEgressMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 19),
    _Cie1000QosConfigInterfaceEgressMap_Type()
)
cie1000QosConfigInterfaceEgressMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceEgressMap.setStatus("current")
_Cie1000QosConfigInterfaceCosId_Type = CIE1000Unsigned8
_Cie1000QosConfigInterfaceCosId_Object = MibTableColumn
cie1000QosConfigInterfaceCosId = _Cie1000QosConfigInterfaceCosId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 1, 1, 20),
    _Cie1000QosConfigInterfaceCosId_Type()
)
cie1000QosConfigInterfaceCosId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceCosId.setStatus("current")
_Cie1000QosConfigInterfaceTagToCosTable_Object = MibTable
cie1000QosConfigInterfaceTagToCosTable = _Cie1000QosConfigInterfaceTagToCosTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceTagToCosTable.setStatus("current")
_Cie1000QosConfigInterfaceTagToCosEntry_Object = MibTableRow
cie1000QosConfigInterfaceTagToCosEntry = _Cie1000QosConfigInterfaceTagToCosEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 2, 1)
)
cie1000QosConfigInterfaceTagToCosEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceTagToCosIfIndex"),
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceTagToCosPcp"),
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceTagToCosDei"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceTagToCosEntry.setStatus("current")
_Cie1000QosConfigInterfaceTagToCosIfIndex_Type = CIE1000InterfaceIndex
_Cie1000QosConfigInterfaceTagToCosIfIndex_Object = MibTableColumn
cie1000QosConfigInterfaceTagToCosIfIndex = _Cie1000QosConfigInterfaceTagToCosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 2, 1, 1),
    _Cie1000QosConfigInterfaceTagToCosIfIndex_Type()
)
cie1000QosConfigInterfaceTagToCosIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceTagToCosIfIndex.setStatus("current")


class _Cie1000QosConfigInterfaceTagToCosPcp_Type(Integer32):
    """Custom type cie1000QosConfigInterfaceTagToCosPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cie1000QosConfigInterfaceTagToCosPcp_Type.__name__ = "Integer32"
_Cie1000QosConfigInterfaceTagToCosPcp_Object = MibTableColumn
cie1000QosConfigInterfaceTagToCosPcp = _Cie1000QosConfigInterfaceTagToCosPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 2, 1, 2),
    _Cie1000QosConfigInterfaceTagToCosPcp_Type()
)
cie1000QosConfigInterfaceTagToCosPcp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceTagToCosPcp.setStatus("current")


class _Cie1000QosConfigInterfaceTagToCosDei_Type(Integer32):
    """Custom type cie1000QosConfigInterfaceTagToCosDei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Cie1000QosConfigInterfaceTagToCosDei_Type.__name__ = "Integer32"
_Cie1000QosConfigInterfaceTagToCosDei_Object = MibTableColumn
cie1000QosConfigInterfaceTagToCosDei = _Cie1000QosConfigInterfaceTagToCosDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 2, 1, 3),
    _Cie1000QosConfigInterfaceTagToCosDei_Type()
)
cie1000QosConfigInterfaceTagToCosDei.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceTagToCosDei.setStatus("current")
_Cie1000QosConfigInterfaceTagToCosCos_Type = Unsigned32
_Cie1000QosConfigInterfaceTagToCosCos_Object = MibTableColumn
cie1000QosConfigInterfaceTagToCosCos = _Cie1000QosConfigInterfaceTagToCosCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 2, 1, 4),
    _Cie1000QosConfigInterfaceTagToCosCos_Type()
)
cie1000QosConfigInterfaceTagToCosCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceTagToCosCos.setStatus("current")
_Cie1000QosConfigInterfaceTagToCosDpl_Type = CIE1000Unsigned8
_Cie1000QosConfigInterfaceTagToCosDpl_Object = MibTableColumn
cie1000QosConfigInterfaceTagToCosDpl = _Cie1000QosConfigInterfaceTagToCosDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 2, 1, 5),
    _Cie1000QosConfigInterfaceTagToCosDpl_Type()
)
cie1000QosConfigInterfaceTagToCosDpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceTagToCosDpl.setStatus("current")
_Cie1000QosConfigInterfaceCosToTagTable_Object = MibTable
cie1000QosConfigInterfaceCosToTagTable = _Cie1000QosConfigInterfaceCosToTagTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceCosToTagTable.setStatus("current")
_Cie1000QosConfigInterfaceCosToTagEntry_Object = MibTableRow
cie1000QosConfigInterfaceCosToTagEntry = _Cie1000QosConfigInterfaceCosToTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 3, 1)
)
cie1000QosConfigInterfaceCosToTagEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceCosToTagIfIndex"),
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceCosToTagCos"),
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceCosToTagDpl"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceCosToTagEntry.setStatus("current")
_Cie1000QosConfigInterfaceCosToTagIfIndex_Type = CIE1000InterfaceIndex
_Cie1000QosConfigInterfaceCosToTagIfIndex_Object = MibTableColumn
cie1000QosConfigInterfaceCosToTagIfIndex = _Cie1000QosConfigInterfaceCosToTagIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 3, 1, 1),
    _Cie1000QosConfigInterfaceCosToTagIfIndex_Type()
)
cie1000QosConfigInterfaceCosToTagIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceCosToTagIfIndex.setStatus("current")


class _Cie1000QosConfigInterfaceCosToTagCos_Type(Integer32):
    """Custom type cie1000QosConfigInterfaceCosToTagCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cie1000QosConfigInterfaceCosToTagCos_Type.__name__ = "Integer32"
_Cie1000QosConfigInterfaceCosToTagCos_Object = MibTableColumn
cie1000QosConfigInterfaceCosToTagCos = _Cie1000QosConfigInterfaceCosToTagCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 3, 1, 2),
    _Cie1000QosConfigInterfaceCosToTagCos_Type()
)
cie1000QosConfigInterfaceCosToTagCos.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceCosToTagCos.setStatus("current")


class _Cie1000QosConfigInterfaceCosToTagDpl_Type(Integer32):
    """Custom type cie1000QosConfigInterfaceCosToTagDpl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Cie1000QosConfigInterfaceCosToTagDpl_Type.__name__ = "Integer32"
_Cie1000QosConfigInterfaceCosToTagDpl_Object = MibTableColumn
cie1000QosConfigInterfaceCosToTagDpl = _Cie1000QosConfigInterfaceCosToTagDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 3, 1, 3),
    _Cie1000QosConfigInterfaceCosToTagDpl_Type()
)
cie1000QosConfigInterfaceCosToTagDpl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceCosToTagDpl.setStatus("current")
_Cie1000QosConfigInterfaceCosToTagPcp_Type = Unsigned32
_Cie1000QosConfigInterfaceCosToTagPcp_Object = MibTableColumn
cie1000QosConfigInterfaceCosToTagPcp = _Cie1000QosConfigInterfaceCosToTagPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 3, 1, 4),
    _Cie1000QosConfigInterfaceCosToTagPcp_Type()
)
cie1000QosConfigInterfaceCosToTagPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceCosToTagPcp.setStatus("current")
_Cie1000QosConfigInterfaceCosToTagDei_Type = CIE1000Unsigned8
_Cie1000QosConfigInterfaceCosToTagDei_Object = MibTableColumn
cie1000QosConfigInterfaceCosToTagDei = _Cie1000QosConfigInterfaceCosToTagDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 3, 1, 5),
    _Cie1000QosConfigInterfaceCosToTagDei_Type()
)
cie1000QosConfigInterfaceCosToTagDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceCosToTagDei.setStatus("current")
_Cie1000QosConfigInterfacePolicerTable_Object = MibTable
cie1000QosConfigInterfacePolicerTable = _Cie1000QosConfigInterfacePolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfacePolicerTable.setStatus("current")
_Cie1000QosConfigInterfacePolicerEntry_Object = MibTableRow
cie1000QosConfigInterfacePolicerEntry = _Cie1000QosConfigInterfacePolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 4, 1)
)
cie1000QosConfigInterfacePolicerEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfacePolicerIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfacePolicerEntry.setStatus("current")
_Cie1000QosConfigInterfacePolicerIfIndex_Type = CIE1000InterfaceIndex
_Cie1000QosConfigInterfacePolicerIfIndex_Object = MibTableColumn
cie1000QosConfigInterfacePolicerIfIndex = _Cie1000QosConfigInterfacePolicerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 4, 1, 1),
    _Cie1000QosConfigInterfacePolicerIfIndex_Type()
)
cie1000QosConfigInterfacePolicerIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfacePolicerIfIndex.setStatus("current")
_Cie1000QosConfigInterfacePolicerEnable_Type = TruthValue
_Cie1000QosConfigInterfacePolicerEnable_Object = MibTableColumn
cie1000QosConfigInterfacePolicerEnable = _Cie1000QosConfigInterfacePolicerEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 4, 1, 2),
    _Cie1000QosConfigInterfacePolicerEnable_Type()
)
cie1000QosConfigInterfacePolicerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfacePolicerEnable.setStatus("current")
_Cie1000QosConfigInterfacePolicerFrameRate_Type = TruthValue
_Cie1000QosConfigInterfacePolicerFrameRate_Object = MibTableColumn
cie1000QosConfigInterfacePolicerFrameRate = _Cie1000QosConfigInterfacePolicerFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 4, 1, 3),
    _Cie1000QosConfigInterfacePolicerFrameRate_Type()
)
cie1000QosConfigInterfacePolicerFrameRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfacePolicerFrameRate.setStatus("current")
_Cie1000QosConfigInterfacePolicerFlowControl_Type = TruthValue
_Cie1000QosConfigInterfacePolicerFlowControl_Object = MibTableColumn
cie1000QosConfigInterfacePolicerFlowControl = _Cie1000QosConfigInterfacePolicerFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 4, 1, 4),
    _Cie1000QosConfigInterfacePolicerFlowControl_Type()
)
cie1000QosConfigInterfacePolicerFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfacePolicerFlowControl.setStatus("current")
_Cie1000QosConfigInterfacePolicerCir_Type = Unsigned32
_Cie1000QosConfigInterfacePolicerCir_Object = MibTableColumn
cie1000QosConfigInterfacePolicerCir = _Cie1000QosConfigInterfacePolicerCir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 4, 1, 5),
    _Cie1000QosConfigInterfacePolicerCir_Type()
)
cie1000QosConfigInterfacePolicerCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfacePolicerCir.setStatus("current")
_Cie1000QosConfigInterfaceQueuePolicerTable_Object = MibTable
cie1000QosConfigInterfaceQueuePolicerTable = _Cie1000QosConfigInterfaceQueuePolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQueuePolicerTable.setStatus("current")
_Cie1000QosConfigInterfaceQueuePolicerEntry_Object = MibTableRow
cie1000QosConfigInterfaceQueuePolicerEntry = _Cie1000QosConfigInterfaceQueuePolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 5, 1)
)
cie1000QosConfigInterfaceQueuePolicerEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQueuePolicerIfIndex"),
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQueuePolicerQueue"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQueuePolicerEntry.setStatus("current")
_Cie1000QosConfigInterfaceQueuePolicerIfIndex_Type = CIE1000InterfaceIndex
_Cie1000QosConfigInterfaceQueuePolicerIfIndex_Object = MibTableColumn
cie1000QosConfigInterfaceQueuePolicerIfIndex = _Cie1000QosConfigInterfaceQueuePolicerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 5, 1, 1),
    _Cie1000QosConfigInterfaceQueuePolicerIfIndex_Type()
)
cie1000QosConfigInterfaceQueuePolicerIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQueuePolicerIfIndex.setStatus("current")


class _Cie1000QosConfigInterfaceQueuePolicerQueue_Type(Integer32):
    """Custom type cie1000QosConfigInterfaceQueuePolicerQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cie1000QosConfigInterfaceQueuePolicerQueue_Type.__name__ = "Integer32"
_Cie1000QosConfigInterfaceQueuePolicerQueue_Object = MibTableColumn
cie1000QosConfigInterfaceQueuePolicerQueue = _Cie1000QosConfigInterfaceQueuePolicerQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 5, 1, 2),
    _Cie1000QosConfigInterfaceQueuePolicerQueue_Type()
)
cie1000QosConfigInterfaceQueuePolicerQueue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQueuePolicerQueue.setStatus("current")
_Cie1000QosConfigInterfaceQueuePolicerEnable_Type = TruthValue
_Cie1000QosConfigInterfaceQueuePolicerEnable_Object = MibTableColumn
cie1000QosConfigInterfaceQueuePolicerEnable = _Cie1000QosConfigInterfaceQueuePolicerEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 5, 1, 3),
    _Cie1000QosConfigInterfaceQueuePolicerEnable_Type()
)
cie1000QosConfigInterfaceQueuePolicerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQueuePolicerEnable.setStatus("current")
_Cie1000QosConfigInterfaceQueuePolicerCir_Type = Unsigned32
_Cie1000QosConfigInterfaceQueuePolicerCir_Object = MibTableColumn
cie1000QosConfigInterfaceQueuePolicerCir = _Cie1000QosConfigInterfaceQueuePolicerCir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 5, 1, 6),
    _Cie1000QosConfigInterfaceQueuePolicerCir_Type()
)
cie1000QosConfigInterfaceQueuePolicerCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQueuePolicerCir.setStatus("current")
_Cie1000QosConfigInterfaceShaperTable_Object = MibTable
cie1000QosConfigInterfaceShaperTable = _Cie1000QosConfigInterfaceShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceShaperTable.setStatus("current")
_Cie1000QosConfigInterfaceShaperEntry_Object = MibTableRow
cie1000QosConfigInterfaceShaperEntry = _Cie1000QosConfigInterfaceShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 6, 1)
)
cie1000QosConfigInterfaceShaperEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceShaperIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceShaperEntry.setStatus("current")
_Cie1000QosConfigInterfaceShaperIfIndex_Type = CIE1000InterfaceIndex
_Cie1000QosConfigInterfaceShaperIfIndex_Object = MibTableColumn
cie1000QosConfigInterfaceShaperIfIndex = _Cie1000QosConfigInterfaceShaperIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 6, 1, 1),
    _Cie1000QosConfigInterfaceShaperIfIndex_Type()
)
cie1000QosConfigInterfaceShaperIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceShaperIfIndex.setStatus("current")
_Cie1000QosConfigInterfaceShaperEnable_Type = TruthValue
_Cie1000QosConfigInterfaceShaperEnable_Object = MibTableColumn
cie1000QosConfigInterfaceShaperEnable = _Cie1000QosConfigInterfaceShaperEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 6, 1, 2),
    _Cie1000QosConfigInterfaceShaperEnable_Type()
)
cie1000QosConfigInterfaceShaperEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceShaperEnable.setStatus("current")
_Cie1000QosConfigInterfaceShaperCir_Type = Unsigned32
_Cie1000QosConfigInterfaceShaperCir_Object = MibTableColumn
cie1000QosConfigInterfaceShaperCir = _Cie1000QosConfigInterfaceShaperCir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 6, 1, 3),
    _Cie1000QosConfigInterfaceShaperCir_Type()
)
cie1000QosConfigInterfaceShaperCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceShaperCir.setStatus("current")
_Cie1000QosConfigInterfaceShaperRateType_Type = CIE1000QosShaperRateType
_Cie1000QosConfigInterfaceShaperRateType_Object = MibTableColumn
cie1000QosConfigInterfaceShaperRateType = _Cie1000QosConfigInterfaceShaperRateType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 6, 1, 4),
    _Cie1000QosConfigInterfaceShaperRateType_Type()
)
cie1000QosConfigInterfaceShaperRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceShaperRateType.setStatus("current")
_Cie1000QosConfigInterfaceQueueShaperTable_Object = MibTable
cie1000QosConfigInterfaceQueueShaperTable = _Cie1000QosConfigInterfaceQueueShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 7)
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQueueShaperTable.setStatus("current")
_Cie1000QosConfigInterfaceQueueShaperEntry_Object = MibTableRow
cie1000QosConfigInterfaceQueueShaperEntry = _Cie1000QosConfigInterfaceQueueShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 7, 1)
)
cie1000QosConfigInterfaceQueueShaperEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQueueShaperIfIndex"),
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQueueShaperQueue"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQueueShaperEntry.setStatus("current")
_Cie1000QosConfigInterfaceQueueShaperIfIndex_Type = CIE1000InterfaceIndex
_Cie1000QosConfigInterfaceQueueShaperIfIndex_Object = MibTableColumn
cie1000QosConfigInterfaceQueueShaperIfIndex = _Cie1000QosConfigInterfaceQueueShaperIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 7, 1, 1),
    _Cie1000QosConfigInterfaceQueueShaperIfIndex_Type()
)
cie1000QosConfigInterfaceQueueShaperIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQueueShaperIfIndex.setStatus("current")


class _Cie1000QosConfigInterfaceQueueShaperQueue_Type(Integer32):
    """Custom type cie1000QosConfigInterfaceQueueShaperQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cie1000QosConfigInterfaceQueueShaperQueue_Type.__name__ = "Integer32"
_Cie1000QosConfigInterfaceQueueShaperQueue_Object = MibTableColumn
cie1000QosConfigInterfaceQueueShaperQueue = _Cie1000QosConfigInterfaceQueueShaperQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 7, 1, 2),
    _Cie1000QosConfigInterfaceQueueShaperQueue_Type()
)
cie1000QosConfigInterfaceQueueShaperQueue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQueueShaperQueue.setStatus("current")
_Cie1000QosConfigInterfaceQueueShaperEnable_Type = TruthValue
_Cie1000QosConfigInterfaceQueueShaperEnable_Object = MibTableColumn
cie1000QosConfigInterfaceQueueShaperEnable = _Cie1000QosConfigInterfaceQueueShaperEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 7, 1, 3),
    _Cie1000QosConfigInterfaceQueueShaperEnable_Type()
)
cie1000QosConfigInterfaceQueueShaperEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQueueShaperEnable.setStatus("current")
_Cie1000QosConfigInterfaceQueueShaperExcess_Type = TruthValue
_Cie1000QosConfigInterfaceQueueShaperExcess_Object = MibTableColumn
cie1000QosConfigInterfaceQueueShaperExcess = _Cie1000QosConfigInterfaceQueueShaperExcess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 7, 1, 4),
    _Cie1000QosConfigInterfaceQueueShaperExcess_Type()
)
cie1000QosConfigInterfaceQueueShaperExcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQueueShaperExcess.setStatus("current")
_Cie1000QosConfigInterfaceQueueShaperCir_Type = Unsigned32
_Cie1000QosConfigInterfaceQueueShaperCir_Object = MibTableColumn
cie1000QosConfigInterfaceQueueShaperCir = _Cie1000QosConfigInterfaceQueueShaperCir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 7, 1, 5),
    _Cie1000QosConfigInterfaceQueueShaperCir_Type()
)
cie1000QosConfigInterfaceQueueShaperCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQueueShaperCir.setStatus("current")
_Cie1000QosConfigInterfaceQueueShaperRateType_Type = CIE1000QosShaperRateType
_Cie1000QosConfigInterfaceQueueShaperRateType_Object = MibTableColumn
cie1000QosConfigInterfaceQueueShaperRateType = _Cie1000QosConfigInterfaceQueueShaperRateType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 7, 1, 6),
    _Cie1000QosConfigInterfaceQueueShaperRateType_Type()
)
cie1000QosConfigInterfaceQueueShaperRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQueueShaperRateType.setStatus("current")
_Cie1000QosConfigInterfaceQueueShaperCredit_Type = TruthValue
_Cie1000QosConfigInterfaceQueueShaperCredit_Object = MibTableColumn
cie1000QosConfigInterfaceQueueShaperCredit = _Cie1000QosConfigInterfaceQueueShaperCredit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 7, 1, 7),
    _Cie1000QosConfigInterfaceQueueShaperCredit_Type()
)
cie1000QosConfigInterfaceQueueShaperCredit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQueueShaperCredit.setStatus("current")
_Cie1000QosConfigInterfaceSchedulerTable_Object = MibTable
cie1000QosConfigInterfaceSchedulerTable = _Cie1000QosConfigInterfaceSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceSchedulerTable.setStatus("current")
_Cie1000QosConfigInterfaceSchedulerEntry_Object = MibTableRow
cie1000QosConfigInterfaceSchedulerEntry = _Cie1000QosConfigInterfaceSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 8, 1)
)
cie1000QosConfigInterfaceSchedulerEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceSchedulerIfIndex"),
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceSchedulerQueue"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceSchedulerEntry.setStatus("current")
_Cie1000QosConfigInterfaceSchedulerIfIndex_Type = CIE1000InterfaceIndex
_Cie1000QosConfigInterfaceSchedulerIfIndex_Object = MibTableColumn
cie1000QosConfigInterfaceSchedulerIfIndex = _Cie1000QosConfigInterfaceSchedulerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 8, 1, 1),
    _Cie1000QosConfigInterfaceSchedulerIfIndex_Type()
)
cie1000QosConfigInterfaceSchedulerIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceSchedulerIfIndex.setStatus("current")


class _Cie1000QosConfigInterfaceSchedulerQueue_Type(Integer32):
    """Custom type cie1000QosConfigInterfaceSchedulerQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cie1000QosConfigInterfaceSchedulerQueue_Type.__name__ = "Integer32"
_Cie1000QosConfigInterfaceSchedulerQueue_Object = MibTableColumn
cie1000QosConfigInterfaceSchedulerQueue = _Cie1000QosConfigInterfaceSchedulerQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 8, 1, 2),
    _Cie1000QosConfigInterfaceSchedulerQueue_Type()
)
cie1000QosConfigInterfaceSchedulerQueue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceSchedulerQueue.setStatus("current")
_Cie1000QosConfigInterfaceSchedulerWeight_Type = CIE1000Percent
_Cie1000QosConfigInterfaceSchedulerWeight_Object = MibTableColumn
cie1000QosConfigInterfaceSchedulerWeight = _Cie1000QosConfigInterfaceSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 8, 1, 3),
    _Cie1000QosConfigInterfaceSchedulerWeight_Type()
)
cie1000QosConfigInterfaceSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceSchedulerWeight.setStatus("current")
_Cie1000QosConfigInterfaceSchedulerCutThrough_Type = TruthValue
_Cie1000QosConfigInterfaceSchedulerCutThrough_Object = MibTableColumn
cie1000QosConfigInterfaceSchedulerCutThrough = _Cie1000QosConfigInterfaceSchedulerCutThrough_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 8, 1, 4),
    _Cie1000QosConfigInterfaceSchedulerCutThrough_Type()
)
cie1000QosConfigInterfaceSchedulerCutThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceSchedulerCutThrough.setStatus("current")
_Cie1000QosConfigInterfaceStormPolicerUnicastTable_Object = MibTable
cie1000QosConfigInterfaceStormPolicerUnicastTable = _Cie1000QosConfigInterfaceStormPolicerUnicastTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 9)
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerUnicastTable.setStatus("current")
_Cie1000QosConfigInterfaceStormPolicerUnicastEntry_Object = MibTableRow
cie1000QosConfigInterfaceStormPolicerUnicastEntry = _Cie1000QosConfigInterfaceStormPolicerUnicastEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 9, 1)
)
cie1000QosConfigInterfaceStormPolicerUnicastEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceStormPolicerUnicastIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerUnicastEntry.setStatus("current")
_Cie1000QosConfigInterfaceStormPolicerUnicastIfIndex_Type = CIE1000InterfaceIndex
_Cie1000QosConfigInterfaceStormPolicerUnicastIfIndex_Object = MibTableColumn
cie1000QosConfigInterfaceStormPolicerUnicastIfIndex = _Cie1000QosConfigInterfaceStormPolicerUnicastIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 9, 1, 1),
    _Cie1000QosConfigInterfaceStormPolicerUnicastIfIndex_Type()
)
cie1000QosConfigInterfaceStormPolicerUnicastIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerUnicastIfIndex.setStatus("current")
_Cie1000QosConfigInterfaceStormPolicerUnicastEnable_Type = TruthValue
_Cie1000QosConfigInterfaceStormPolicerUnicastEnable_Object = MibTableColumn
cie1000QosConfigInterfaceStormPolicerUnicastEnable = _Cie1000QosConfigInterfaceStormPolicerUnicastEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 9, 1, 2),
    _Cie1000QosConfigInterfaceStormPolicerUnicastEnable_Type()
)
cie1000QosConfigInterfaceStormPolicerUnicastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerUnicastEnable.setStatus("current")
_Cie1000QosConfigInterfaceStormPolicerUnicastFrameRate_Type = TruthValue
_Cie1000QosConfigInterfaceStormPolicerUnicastFrameRate_Object = MibTableColumn
cie1000QosConfigInterfaceStormPolicerUnicastFrameRate = _Cie1000QosConfigInterfaceStormPolicerUnicastFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 9, 1, 3),
    _Cie1000QosConfigInterfaceStormPolicerUnicastFrameRate_Type()
)
cie1000QosConfigInterfaceStormPolicerUnicastFrameRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerUnicastFrameRate.setStatus("current")
_Cie1000QosConfigInterfaceStormPolicerUnicastCir_Type = Unsigned32
_Cie1000QosConfigInterfaceStormPolicerUnicastCir_Object = MibTableColumn
cie1000QosConfigInterfaceStormPolicerUnicastCir = _Cie1000QosConfigInterfaceStormPolicerUnicastCir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 9, 1, 4),
    _Cie1000QosConfigInterfaceStormPolicerUnicastCir_Type()
)
cie1000QosConfigInterfaceStormPolicerUnicastCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerUnicastCir.setStatus("current")
_Cie1000QosConfigInterfaceStormPolicerBroadcastTable_Object = MibTable
cie1000QosConfigInterfaceStormPolicerBroadcastTable = _Cie1000QosConfigInterfaceStormPolicerBroadcastTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 10)
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerBroadcastTable.setStatus("current")
_Cie1000QosConfigInterfaceStormPolicerBroadcastEntry_Object = MibTableRow
cie1000QosConfigInterfaceStormPolicerBroadcastEntry = _Cie1000QosConfigInterfaceStormPolicerBroadcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 10, 1)
)
cie1000QosConfigInterfaceStormPolicerBroadcastEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceStormPolicerBroadcastIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerBroadcastEntry.setStatus("current")
_Cie1000QosConfigInterfaceStormPolicerBroadcastIfIndex_Type = CIE1000InterfaceIndex
_Cie1000QosConfigInterfaceStormPolicerBroadcastIfIndex_Object = MibTableColumn
cie1000QosConfigInterfaceStormPolicerBroadcastIfIndex = _Cie1000QosConfigInterfaceStormPolicerBroadcastIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 10, 1, 1),
    _Cie1000QosConfigInterfaceStormPolicerBroadcastIfIndex_Type()
)
cie1000QosConfigInterfaceStormPolicerBroadcastIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerBroadcastIfIndex.setStatus("current")
_Cie1000QosConfigInterfaceStormPolicerBroadcastEnable_Type = TruthValue
_Cie1000QosConfigInterfaceStormPolicerBroadcastEnable_Object = MibTableColumn
cie1000QosConfigInterfaceStormPolicerBroadcastEnable = _Cie1000QosConfigInterfaceStormPolicerBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 10, 1, 2),
    _Cie1000QosConfigInterfaceStormPolicerBroadcastEnable_Type()
)
cie1000QosConfigInterfaceStormPolicerBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerBroadcastEnable.setStatus("current")
_Cie1000QosConfigInterfaceStormPolicerBroadcastFrameRate_Type = TruthValue
_Cie1000QosConfigInterfaceStormPolicerBroadcastFrameRate_Object = MibTableColumn
cie1000QosConfigInterfaceStormPolicerBroadcastFrameRate = _Cie1000QosConfigInterfaceStormPolicerBroadcastFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 10, 1, 3),
    _Cie1000QosConfigInterfaceStormPolicerBroadcastFrameRate_Type()
)
cie1000QosConfigInterfaceStormPolicerBroadcastFrameRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerBroadcastFrameRate.setStatus("current")
_Cie1000QosConfigInterfaceStormPolicerBroadcastCir_Type = Unsigned32
_Cie1000QosConfigInterfaceStormPolicerBroadcastCir_Object = MibTableColumn
cie1000QosConfigInterfaceStormPolicerBroadcastCir = _Cie1000QosConfigInterfaceStormPolicerBroadcastCir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 10, 1, 4),
    _Cie1000QosConfigInterfaceStormPolicerBroadcastCir_Type()
)
cie1000QosConfigInterfaceStormPolicerBroadcastCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerBroadcastCir.setStatus("current")
_Cie1000QosConfigInterfaceStormPolicerUnknownTable_Object = MibTable
cie1000QosConfigInterfaceStormPolicerUnknownTable = _Cie1000QosConfigInterfaceStormPolicerUnknownTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 11)
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerUnknownTable.setStatus("current")
_Cie1000QosConfigInterfaceStormPolicerUnknownEntry_Object = MibTableRow
cie1000QosConfigInterfaceStormPolicerUnknownEntry = _Cie1000QosConfigInterfaceStormPolicerUnknownEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 11, 1)
)
cie1000QosConfigInterfaceStormPolicerUnknownEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceStormPolicerUnknownIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerUnknownEntry.setStatus("current")
_Cie1000QosConfigInterfaceStormPolicerUnknownIfIndex_Type = CIE1000InterfaceIndex
_Cie1000QosConfigInterfaceStormPolicerUnknownIfIndex_Object = MibTableColumn
cie1000QosConfigInterfaceStormPolicerUnknownIfIndex = _Cie1000QosConfigInterfaceStormPolicerUnknownIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 11, 1, 1),
    _Cie1000QosConfigInterfaceStormPolicerUnknownIfIndex_Type()
)
cie1000QosConfigInterfaceStormPolicerUnknownIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerUnknownIfIndex.setStatus("current")
_Cie1000QosConfigInterfaceStormPolicerUnknownEnable_Type = TruthValue
_Cie1000QosConfigInterfaceStormPolicerUnknownEnable_Object = MibTableColumn
cie1000QosConfigInterfaceStormPolicerUnknownEnable = _Cie1000QosConfigInterfaceStormPolicerUnknownEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 11, 1, 2),
    _Cie1000QosConfigInterfaceStormPolicerUnknownEnable_Type()
)
cie1000QosConfigInterfaceStormPolicerUnknownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerUnknownEnable.setStatus("current")
_Cie1000QosConfigInterfaceStormPolicerUnknownFrameRate_Type = TruthValue
_Cie1000QosConfigInterfaceStormPolicerUnknownFrameRate_Object = MibTableColumn
cie1000QosConfigInterfaceStormPolicerUnknownFrameRate = _Cie1000QosConfigInterfaceStormPolicerUnknownFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 11, 1, 3),
    _Cie1000QosConfigInterfaceStormPolicerUnknownFrameRate_Type()
)
cie1000QosConfigInterfaceStormPolicerUnknownFrameRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerUnknownFrameRate.setStatus("current")
_Cie1000QosConfigInterfaceStormPolicerUnknownCir_Type = Unsigned32
_Cie1000QosConfigInterfaceStormPolicerUnknownCir_Object = MibTableColumn
cie1000QosConfigInterfaceStormPolicerUnknownCir = _Cie1000QosConfigInterfaceStormPolicerUnknownCir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 11, 1, 4),
    _Cie1000QosConfigInterfaceStormPolicerUnknownCir_Type()
)
cie1000QosConfigInterfaceStormPolicerUnknownCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerUnknownCir.setStatus("current")
_Cie1000QosConfigInterfaceQbvMaxSduTable_Object = MibTable
cie1000QosConfigInterfaceQbvMaxSduTable = _Cie1000QosConfigInterfaceQbvMaxSduTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 12)
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvMaxSduTable.setStatus("current")
_Cie1000QosConfigInterfaceQbvMaxSduEntry_Object = MibTableRow
cie1000QosConfigInterfaceQbvMaxSduEntry = _Cie1000QosConfigInterfaceQbvMaxSduEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 12, 1)
)
cie1000QosConfigInterfaceQbvMaxSduEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvMaxSduIfIndex"),
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvMaxSduQueue"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvMaxSduEntry.setStatus("current")
_Cie1000QosConfigInterfaceQbvMaxSduIfIndex_Type = CIE1000InterfaceIndex
_Cie1000QosConfigInterfaceQbvMaxSduIfIndex_Object = MibTableColumn
cie1000QosConfigInterfaceQbvMaxSduIfIndex = _Cie1000QosConfigInterfaceQbvMaxSduIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 12, 1, 1),
    _Cie1000QosConfigInterfaceQbvMaxSduIfIndex_Type()
)
cie1000QosConfigInterfaceQbvMaxSduIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvMaxSduIfIndex.setStatus("current")


class _Cie1000QosConfigInterfaceQbvMaxSduQueue_Type(Integer32):
    """Custom type cie1000QosConfigInterfaceQbvMaxSduQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cie1000QosConfigInterfaceQbvMaxSduQueue_Type.__name__ = "Integer32"
_Cie1000QosConfigInterfaceQbvMaxSduQueue_Object = MibTableColumn
cie1000QosConfigInterfaceQbvMaxSduQueue = _Cie1000QosConfigInterfaceQbvMaxSduQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 12, 1, 2),
    _Cie1000QosConfigInterfaceQbvMaxSduQueue_Type()
)
cie1000QosConfigInterfaceQbvMaxSduQueue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvMaxSduQueue.setStatus("current")
_Cie1000QosConfigInterfaceQbvMaxSduMaxSDU_Type = Unsigned32
_Cie1000QosConfigInterfaceQbvMaxSduMaxSDU_Object = MibTableColumn
cie1000QosConfigInterfaceQbvMaxSduMaxSDU = _Cie1000QosConfigInterfaceQbvMaxSduMaxSDU_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 12, 1, 3),
    _Cie1000QosConfigInterfaceQbvMaxSduMaxSDU_Type()
)
cie1000QosConfigInterfaceQbvMaxSduMaxSDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvMaxSduMaxSDU.setStatus("current")
_Cie1000QosConfigInterfaceQbvGclAdminTable_Object = MibTable
cie1000QosConfigInterfaceQbvGclAdminTable = _Cie1000QosConfigInterfaceQbvGclAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 13)
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvGclAdminTable.setStatus("current")
_Cie1000QosConfigInterfaceQbvGclAdminEntry_Object = MibTableRow
cie1000QosConfigInterfaceQbvGclAdminEntry = _Cie1000QosConfigInterfaceQbvGclAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 13, 1)
)
cie1000QosConfigInterfaceQbvGclAdminEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvGclAdminIfIndex"),
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvGclAdminGclIndex"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvGclAdminEntry.setStatus("current")
_Cie1000QosConfigInterfaceQbvGclAdminIfIndex_Type = CIE1000InterfaceIndex
_Cie1000QosConfigInterfaceQbvGclAdminIfIndex_Object = MibTableColumn
cie1000QosConfigInterfaceQbvGclAdminIfIndex = _Cie1000QosConfigInterfaceQbvGclAdminIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 13, 1, 1),
    _Cie1000QosConfigInterfaceQbvGclAdminIfIndex_Type()
)
cie1000QosConfigInterfaceQbvGclAdminIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvGclAdminIfIndex.setStatus("current")


class _Cie1000QosConfigInterfaceQbvGclAdminGclIndex_Type(Integer32):
    """Custom type cie1000QosConfigInterfaceQbvGclAdminGclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Cie1000QosConfigInterfaceQbvGclAdminGclIndex_Type.__name__ = "Integer32"
_Cie1000QosConfigInterfaceQbvGclAdminGclIndex_Object = MibTableColumn
cie1000QosConfigInterfaceQbvGclAdminGclIndex = _Cie1000QosConfigInterfaceQbvGclAdminGclIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 13, 1, 2),
    _Cie1000QosConfigInterfaceQbvGclAdminGclIndex_Type()
)
cie1000QosConfigInterfaceQbvGclAdminGclIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvGclAdminGclIndex.setStatus("current")


class _Cie1000QosConfigInterfaceQbvGclAdminGateState_Type(OctetString):
    """Custom type cie1000QosConfigInterfaceQbvGclAdminGateState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_Cie1000QosConfigInterfaceQbvGclAdminGateState_Type.__name__ = "OctetString"
_Cie1000QosConfigInterfaceQbvGclAdminGateState_Object = MibTableColumn
cie1000QosConfigInterfaceQbvGclAdminGateState = _Cie1000QosConfigInterfaceQbvGclAdminGateState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 13, 1, 3),
    _Cie1000QosConfigInterfaceQbvGclAdminGateState_Type()
)
cie1000QosConfigInterfaceQbvGclAdminGateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvGclAdminGateState.setStatus("current")
_Cie1000QosConfigInterfaceQbvGclAdminTimeInterval_Type = Unsigned32
_Cie1000QosConfigInterfaceQbvGclAdminTimeInterval_Object = MibTableColumn
cie1000QosConfigInterfaceQbvGclAdminTimeInterval = _Cie1000QosConfigInterfaceQbvGclAdminTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 13, 1, 4),
    _Cie1000QosConfigInterfaceQbvGclAdminTimeInterval_Type()
)
cie1000QosConfigInterfaceQbvGclAdminTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvGclAdminTimeInterval.setStatus("current")
_Cie1000QosConfigInterfaceQbvParamsTable_Object = MibTable
cie1000QosConfigInterfaceQbvParamsTable = _Cie1000QosConfigInterfaceQbvParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 14)
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvParamsTable.setStatus("current")
_Cie1000QosConfigInterfaceQbvParamsEntry_Object = MibTableRow
cie1000QosConfigInterfaceQbvParamsEntry = _Cie1000QosConfigInterfaceQbvParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 14, 1)
)
cie1000QosConfigInterfaceQbvParamsEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvParamsIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvParamsEntry.setStatus("current")
_Cie1000QosConfigInterfaceQbvParamsIfIndex_Type = CIE1000InterfaceIndex
_Cie1000QosConfigInterfaceQbvParamsIfIndex_Object = MibTableColumn
cie1000QosConfigInterfaceQbvParamsIfIndex = _Cie1000QosConfigInterfaceQbvParamsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 14, 1, 1),
    _Cie1000QosConfigInterfaceQbvParamsIfIndex_Type()
)
cie1000QosConfigInterfaceQbvParamsIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvParamsIfIndex.setStatus("current")
_Cie1000QosConfigInterfaceQbvParamsGateEnabled_Type = TruthValue
_Cie1000QosConfigInterfaceQbvParamsGateEnabled_Object = MibTableColumn
cie1000QosConfigInterfaceQbvParamsGateEnabled = _Cie1000QosConfigInterfaceQbvParamsGateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 14, 1, 2),
    _Cie1000QosConfigInterfaceQbvParamsGateEnabled_Type()
)
cie1000QosConfigInterfaceQbvParamsGateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvParamsGateEnabled.setStatus("current")


class _Cie1000QosConfigInterfaceQbvParamsAdminGateStates_Type(OctetString):
    """Custom type cie1000QosConfigInterfaceQbvParamsAdminGateStates based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_Cie1000QosConfigInterfaceQbvParamsAdminGateStates_Type.__name__ = "OctetString"
_Cie1000QosConfigInterfaceQbvParamsAdminGateStates_Object = MibTableColumn
cie1000QosConfigInterfaceQbvParamsAdminGateStates = _Cie1000QosConfigInterfaceQbvParamsAdminGateStates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 14, 1, 3),
    _Cie1000QosConfigInterfaceQbvParamsAdminGateStates_Type()
)
cie1000QosConfigInterfaceQbvParamsAdminGateStates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvParamsAdminGateStates.setStatus("current")
_Cie1000QosConfigInterfaceQbvParamsAdminControlListLength_Type = Unsigned32
_Cie1000QosConfigInterfaceQbvParamsAdminControlListLength_Object = MibTableColumn
cie1000QosConfigInterfaceQbvParamsAdminControlListLength = _Cie1000QosConfigInterfaceQbvParamsAdminControlListLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 14, 1, 4),
    _Cie1000QosConfigInterfaceQbvParamsAdminControlListLength_Type()
)
cie1000QosConfigInterfaceQbvParamsAdminControlListLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvParamsAdminControlListLength.setStatus("current")
_Cie1000QosConfigInterfaceQbvParamsAdminCycleTimeNumerator_Type = Unsigned32
_Cie1000QosConfigInterfaceQbvParamsAdminCycleTimeNumerator_Object = MibTableColumn
cie1000QosConfigInterfaceQbvParamsAdminCycleTimeNumerator = _Cie1000QosConfigInterfaceQbvParamsAdminCycleTimeNumerator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 14, 1, 5),
    _Cie1000QosConfigInterfaceQbvParamsAdminCycleTimeNumerator_Type()
)
cie1000QosConfigInterfaceQbvParamsAdminCycleTimeNumerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvParamsAdminCycleTimeNumerator.setStatus("current")
_Cie1000QosConfigInterfaceQbvParamsAdminCycleTimeDenominator_Type = Unsigned32
_Cie1000QosConfigInterfaceQbvParamsAdminCycleTimeDenominator_Object = MibTableColumn
cie1000QosConfigInterfaceQbvParamsAdminCycleTimeDenominator = _Cie1000QosConfigInterfaceQbvParamsAdminCycleTimeDenominator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 14, 1, 6),
    _Cie1000QosConfigInterfaceQbvParamsAdminCycleTimeDenominator_Type()
)
cie1000QosConfigInterfaceQbvParamsAdminCycleTimeDenominator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvParamsAdminCycleTimeDenominator.setStatus("current")
_Cie1000QosConfigInterfaceQbvParamsAdminCycleTimeExtension_Type = Unsigned32
_Cie1000QosConfigInterfaceQbvParamsAdminCycleTimeExtension_Object = MibTableColumn
cie1000QosConfigInterfaceQbvParamsAdminCycleTimeExtension = _Cie1000QosConfigInterfaceQbvParamsAdminCycleTimeExtension_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 14, 1, 7),
    _Cie1000QosConfigInterfaceQbvParamsAdminCycleTimeExtension_Type()
)
cie1000QosConfigInterfaceQbvParamsAdminCycleTimeExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvParamsAdminCycleTimeExtension.setStatus("current")
_Cie1000QosConfigInterfaceQbvParamsAdminBaseTime_Type = IEEE8021STPTPtimeValue
_Cie1000QosConfigInterfaceQbvParamsAdminBaseTime_Object = MibTableColumn
cie1000QosConfigInterfaceQbvParamsAdminBaseTime = _Cie1000QosConfigInterfaceQbvParamsAdminBaseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 14, 1, 8),
    _Cie1000QosConfigInterfaceQbvParamsAdminBaseTime_Type()
)
cie1000QosConfigInterfaceQbvParamsAdminBaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvParamsAdminBaseTime.setStatus("current")
_Cie1000QosConfigInterfaceQbvParamsConfigChange_Type = TruthValue
_Cie1000QosConfigInterfaceQbvParamsConfigChange_Object = MibTableColumn
cie1000QosConfigInterfaceQbvParamsConfigChange = _Cie1000QosConfigInterfaceQbvParamsConfigChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 2, 14, 1, 9),
    _Cie1000QosConfigInterfaceQbvParamsConfigChange_Type()
)
cie1000QosConfigInterfaceQbvParamsConfigChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvParamsConfigChange.setStatus("current")
_Cie1000QosConfigQce_ObjectIdentity = ObjectIdentity
cie1000QosConfigQce = _Cie1000QosConfigQce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3)
)
_Cie1000QosConfigQceTable_Object = MibTable
cie1000QosConfigQceTable = _Cie1000QosConfigQceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cie1000QosConfigQceTable.setStatus("current")
_Cie1000QosConfigQceEntry_Object = MibTableRow
cie1000QosConfigQceEntry = _Cie1000QosConfigQceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1)
)
cie1000QosConfigQceEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigQceQceId"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigQceEntry.setStatus("current")


class _Cie1000QosConfigQceQceId_Type(Integer32):
    """Custom type cie1000QosConfigQceQceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000QosConfigQceQceId_Type.__name__ = "Integer32"
_Cie1000QosConfigQceQceId_Object = MibTableColumn
cie1000QosConfigQceQceId = _Cie1000QosConfigQceQceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 1),
    _Cie1000QosConfigQceQceId_Type()
)
cie1000QosConfigQceQceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigQceQceId.setStatus("current")
_Cie1000QosConfigQceNextQceId_Type = Unsigned32
_Cie1000QosConfigQceNextQceId_Object = MibTableColumn
cie1000QosConfigQceNextQceId = _Cie1000QosConfigQceNextQceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 2),
    _Cie1000QosConfigQceNextQceId_Type()
)
cie1000QosConfigQceNextQceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceNextQceId.setStatus("current")
_Cie1000QosConfigQceSwitchId_Type = Unsigned32
_Cie1000QosConfigQceSwitchId_Object = MibTableColumn
cie1000QosConfigQceSwitchId = _Cie1000QosConfigQceSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 3),
    _Cie1000QosConfigQceSwitchId_Type()
)
cie1000QosConfigQceSwitchId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceSwitchId.setStatus("current")
_Cie1000QosConfigQcePortList_Type = CIE1000PortList
_Cie1000QosConfigQcePortList_Object = MibTableColumn
cie1000QosConfigQcePortList = _Cie1000QosConfigQcePortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 4),
    _Cie1000QosConfigQcePortList_Type()
)
cie1000QosConfigQcePortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQcePortList.setStatus("current")
_Cie1000QosConfigQceDestMacType_Type = CIE1000DestMacType
_Cie1000QosConfigQceDestMacType_Object = MibTableColumn
cie1000QosConfigQceDestMacType = _Cie1000QosConfigQceDestMacType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 5),
    _Cie1000QosConfigQceDestMacType_Type()
)
cie1000QosConfigQceDestMacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceDestMacType.setStatus("current")
_Cie1000QosConfigQceDestMac_Type = MacAddress
_Cie1000QosConfigQceDestMac_Object = MibTableColumn
cie1000QosConfigQceDestMac = _Cie1000QosConfigQceDestMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 6),
    _Cie1000QosConfigQceDestMac_Type()
)
cie1000QosConfigQceDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceDestMac.setStatus("current")
_Cie1000QosConfigQceDestMacMask_Type = MacAddress
_Cie1000QosConfigQceDestMacMask_Object = MibTableColumn
cie1000QosConfigQceDestMacMask = _Cie1000QosConfigQceDestMacMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 7),
    _Cie1000QosConfigQceDestMacMask_Type()
)
cie1000QosConfigQceDestMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceDestMacMask.setStatus("current")
_Cie1000QosConfigQceSrcMac_Type = MacAddress
_Cie1000QosConfigQceSrcMac_Object = MibTableColumn
cie1000QosConfigQceSrcMac = _Cie1000QosConfigQceSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 8),
    _Cie1000QosConfigQceSrcMac_Type()
)
cie1000QosConfigQceSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceSrcMac.setStatus("current")
_Cie1000QosConfigQceSrcMacMask_Type = MacAddress
_Cie1000QosConfigQceSrcMacMask_Object = MibTableColumn
cie1000QosConfigQceSrcMacMask = _Cie1000QosConfigQceSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 9),
    _Cie1000QosConfigQceSrcMacMask_Type()
)
cie1000QosConfigQceSrcMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceSrcMacMask.setStatus("current")
_Cie1000QosConfigQceVlanTagType_Type = CIE1000VlanTagType
_Cie1000QosConfigQceVlanTagType_Object = MibTableColumn
cie1000QosConfigQceVlanTagType = _Cie1000QosConfigQceVlanTagType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 10),
    _Cie1000QosConfigQceVlanTagType_Type()
)
cie1000QosConfigQceVlanTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceVlanTagType.setStatus("current")
_Cie1000QosConfigQceVlanIdOp_Type = CIE1000ASRType
_Cie1000QosConfigQceVlanIdOp_Object = MibTableColumn
cie1000QosConfigQceVlanIdOp = _Cie1000QosConfigQceVlanIdOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 11),
    _Cie1000QosConfigQceVlanIdOp_Type()
)
cie1000QosConfigQceVlanIdOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceVlanIdOp.setStatus("current")
_Cie1000QosConfigQceVlanId_Type = CIE1000Unsigned16
_Cie1000QosConfigQceVlanId_Object = MibTableColumn
cie1000QosConfigQceVlanId = _Cie1000QosConfigQceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 12),
    _Cie1000QosConfigQceVlanId_Type()
)
cie1000QosConfigQceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceVlanId.setStatus("current")
_Cie1000QosConfigQceVlanIdRange_Type = CIE1000Unsigned16
_Cie1000QosConfigQceVlanIdRange_Object = MibTableColumn
cie1000QosConfigQceVlanIdRange = _Cie1000QosConfigQceVlanIdRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 13),
    _Cie1000QosConfigQceVlanIdRange_Type()
)
cie1000QosConfigQceVlanIdRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceVlanIdRange.setStatus("current")
_Cie1000QosConfigQcePcp_Type = CIE1000VlanTagPriority
_Cie1000QosConfigQcePcp_Object = MibTableColumn
cie1000QosConfigQcePcp = _Cie1000QosConfigQcePcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 14),
    _Cie1000QosConfigQcePcp_Type()
)
cie1000QosConfigQcePcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQcePcp.setStatus("current")
_Cie1000QosConfigQceDei_Type = CIE1000BitType
_Cie1000QosConfigQceDei_Object = MibTableColumn
cie1000QosConfigQceDei = _Cie1000QosConfigQceDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 15),
    _Cie1000QosConfigQceDei_Type()
)
cie1000QosConfigQceDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceDei.setStatus("current")
_Cie1000QosConfigQceInnerVlanTagType_Type = CIE1000VlanTagType
_Cie1000QosConfigQceInnerVlanTagType_Object = MibTableColumn
cie1000QosConfigQceInnerVlanTagType = _Cie1000QosConfigQceInnerVlanTagType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 16),
    _Cie1000QosConfigQceInnerVlanTagType_Type()
)
cie1000QosConfigQceInnerVlanTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceInnerVlanTagType.setStatus("current")
_Cie1000QosConfigQceInnerVlanIdOp_Type = CIE1000ASRType
_Cie1000QosConfigQceInnerVlanIdOp_Object = MibTableColumn
cie1000QosConfigQceInnerVlanIdOp = _Cie1000QosConfigQceInnerVlanIdOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 17),
    _Cie1000QosConfigQceInnerVlanIdOp_Type()
)
cie1000QosConfigQceInnerVlanIdOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceInnerVlanIdOp.setStatus("current")
_Cie1000QosConfigQceInnerVlanId_Type = CIE1000Unsigned16
_Cie1000QosConfigQceInnerVlanId_Object = MibTableColumn
cie1000QosConfigQceInnerVlanId = _Cie1000QosConfigQceInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 18),
    _Cie1000QosConfigQceInnerVlanId_Type()
)
cie1000QosConfigQceInnerVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceInnerVlanId.setStatus("current")
_Cie1000QosConfigQceInnerVlanIdRange_Type = CIE1000Unsigned16
_Cie1000QosConfigQceInnerVlanIdRange_Object = MibTableColumn
cie1000QosConfigQceInnerVlanIdRange = _Cie1000QosConfigQceInnerVlanIdRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 19),
    _Cie1000QosConfigQceInnerVlanIdRange_Type()
)
cie1000QosConfigQceInnerVlanIdRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceInnerVlanIdRange.setStatus("current")
_Cie1000QosConfigQceInnerPcp_Type = CIE1000VlanTagPriority
_Cie1000QosConfigQceInnerPcp_Object = MibTableColumn
cie1000QosConfigQceInnerPcp = _Cie1000QosConfigQceInnerPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 20),
    _Cie1000QosConfigQceInnerPcp_Type()
)
cie1000QosConfigQceInnerPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceInnerPcp.setStatus("current")
_Cie1000QosConfigQceInnerDei_Type = CIE1000BitType
_Cie1000QosConfigQceInnerDei_Object = MibTableColumn
cie1000QosConfigQceInnerDei = _Cie1000QosConfigQceInnerDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 21),
    _Cie1000QosConfigQceInnerDei_Type()
)
cie1000QosConfigQceInnerDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceInnerDei.setStatus("current")
_Cie1000QosConfigQceFrameType_Type = CIE1000QosQceFrameType
_Cie1000QosConfigQceFrameType_Object = MibTableColumn
cie1000QosConfigQceFrameType = _Cie1000QosConfigQceFrameType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 100),
    _Cie1000QosConfigQceFrameType_Type()
)
cie1000QosConfigQceFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceFrameType.setStatus("current")
_Cie1000QosConfigQceEtype_Type = CIE1000EtherType
_Cie1000QosConfigQceEtype_Object = MibTableColumn
cie1000QosConfigQceEtype = _Cie1000QosConfigQceEtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 101),
    _Cie1000QosConfigQceEtype_Type()
)
cie1000QosConfigQceEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceEtype.setStatus("current")
_Cie1000QosConfigQceLlcDsap_Type = CIE1000Unsigned8
_Cie1000QosConfigQceLlcDsap_Object = MibTableColumn
cie1000QosConfigQceLlcDsap = _Cie1000QosConfigQceLlcDsap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 200),
    _Cie1000QosConfigQceLlcDsap_Type()
)
cie1000QosConfigQceLlcDsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceLlcDsap.setStatus("current")
_Cie1000QosConfigQceLlcDsapMask_Type = CIE1000Unsigned8
_Cie1000QosConfigQceLlcDsapMask_Object = MibTableColumn
cie1000QosConfigQceLlcDsapMask = _Cie1000QosConfigQceLlcDsapMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 201),
    _Cie1000QosConfigQceLlcDsapMask_Type()
)
cie1000QosConfigQceLlcDsapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceLlcDsapMask.setStatus("current")
_Cie1000QosConfigQceLlcSsap_Type = CIE1000Unsigned8
_Cie1000QosConfigQceLlcSsap_Object = MibTableColumn
cie1000QosConfigQceLlcSsap = _Cie1000QosConfigQceLlcSsap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 202),
    _Cie1000QosConfigQceLlcSsap_Type()
)
cie1000QosConfigQceLlcSsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceLlcSsap.setStatus("current")
_Cie1000QosConfigQceLlcSsapMask_Type = CIE1000Unsigned8
_Cie1000QosConfigQceLlcSsapMask_Object = MibTableColumn
cie1000QosConfigQceLlcSsapMask = _Cie1000QosConfigQceLlcSsapMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 203),
    _Cie1000QosConfigQceLlcSsapMask_Type()
)
cie1000QosConfigQceLlcSsapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceLlcSsapMask.setStatus("current")
_Cie1000QosConfigQceLlcControl_Type = CIE1000Unsigned8
_Cie1000QosConfigQceLlcControl_Object = MibTableColumn
cie1000QosConfigQceLlcControl = _Cie1000QosConfigQceLlcControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 204),
    _Cie1000QosConfigQceLlcControl_Type()
)
cie1000QosConfigQceLlcControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceLlcControl.setStatus("current")
_Cie1000QosConfigQceLlcControlMask_Type = CIE1000Unsigned8
_Cie1000QosConfigQceLlcControlMask_Object = MibTableColumn
cie1000QosConfigQceLlcControlMask = _Cie1000QosConfigQceLlcControlMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 205),
    _Cie1000QosConfigQceLlcControlMask_Type()
)
cie1000QosConfigQceLlcControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceLlcControlMask.setStatus("current")
_Cie1000QosConfigQceSnapPid_Type = CIE1000Unsigned16
_Cie1000QosConfigQceSnapPid_Object = MibTableColumn
cie1000QosConfigQceSnapPid = _Cie1000QosConfigQceSnapPid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 302),
    _Cie1000QosConfigQceSnapPid_Type()
)
cie1000QosConfigQceSnapPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceSnapPid.setStatus("current")
_Cie1000QosConfigQceSnapPidMask_Type = CIE1000Unsigned16
_Cie1000QosConfigQceSnapPidMask_Object = MibTableColumn
cie1000QosConfigQceSnapPidMask = _Cie1000QosConfigQceSnapPidMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 303),
    _Cie1000QosConfigQceSnapPidMask_Type()
)
cie1000QosConfigQceSnapPidMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceSnapPidMask.setStatus("current")
_Cie1000QosConfigQceIpv4Fragment_Type = CIE1000BitType
_Cie1000QosConfigQceIpv4Fragment_Object = MibTableColumn
cie1000QosConfigQceIpv4Fragment = _Cie1000QosConfigQceIpv4Fragment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 400),
    _Cie1000QosConfigQceIpv4Fragment_Type()
)
cie1000QosConfigQceIpv4Fragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv4Fragment.setStatus("current")
_Cie1000QosConfigQceIpv4DscpOp_Type = CIE1000ASRType
_Cie1000QosConfigQceIpv4DscpOp_Object = MibTableColumn
cie1000QosConfigQceIpv4DscpOp = _Cie1000QosConfigQceIpv4DscpOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 401),
    _Cie1000QosConfigQceIpv4DscpOp_Type()
)
cie1000QosConfigQceIpv4DscpOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv4DscpOp.setStatus("current")
_Cie1000QosConfigQceIpv4Dscp_Type = Dscp
_Cie1000QosConfigQceIpv4Dscp_Object = MibTableColumn
cie1000QosConfigQceIpv4Dscp = _Cie1000QosConfigQceIpv4Dscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 402),
    _Cie1000QosConfigQceIpv4Dscp_Type()
)
cie1000QosConfigQceIpv4Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv4Dscp.setStatus("current")
_Cie1000QosConfigQceIpv4DscpRange_Type = Dscp
_Cie1000QosConfigQceIpv4DscpRange_Object = MibTableColumn
cie1000QosConfigQceIpv4DscpRange = _Cie1000QosConfigQceIpv4DscpRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 403),
    _Cie1000QosConfigQceIpv4DscpRange_Type()
)
cie1000QosConfigQceIpv4DscpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv4DscpRange.setStatus("current")
_Cie1000QosConfigQceIpv4Protocol_Type = CIE1000Unsigned8
_Cie1000QosConfigQceIpv4Protocol_Object = MibTableColumn
cie1000QosConfigQceIpv4Protocol = _Cie1000QosConfigQceIpv4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 404),
    _Cie1000QosConfigQceIpv4Protocol_Type()
)
cie1000QosConfigQceIpv4Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv4Protocol.setStatus("current")
_Cie1000QosConfigQceIpv4ProtocolMask_Type = CIE1000Unsigned8
_Cie1000QosConfigQceIpv4ProtocolMask_Object = MibTableColumn
cie1000QosConfigQceIpv4ProtocolMask = _Cie1000QosConfigQceIpv4ProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 405),
    _Cie1000QosConfigQceIpv4ProtocolMask_Type()
)
cie1000QosConfigQceIpv4ProtocolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv4ProtocolMask.setStatus("current")
_Cie1000QosConfigQceIpv4SrcIp_Type = IpAddress
_Cie1000QosConfigQceIpv4SrcIp_Object = MibTableColumn
cie1000QosConfigQceIpv4SrcIp = _Cie1000QosConfigQceIpv4SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 406),
    _Cie1000QosConfigQceIpv4SrcIp_Type()
)
cie1000QosConfigQceIpv4SrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv4SrcIp.setStatus("current")
_Cie1000QosConfigQceIpv4SrcIpMask_Type = IpAddress
_Cie1000QosConfigQceIpv4SrcIpMask_Object = MibTableColumn
cie1000QosConfigQceIpv4SrcIpMask = _Cie1000QosConfigQceIpv4SrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 407),
    _Cie1000QosConfigQceIpv4SrcIpMask_Type()
)
cie1000QosConfigQceIpv4SrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv4SrcIpMask.setStatus("current")
_Cie1000QosConfigQceIpv4DestIp_Type = IpAddress
_Cie1000QosConfigQceIpv4DestIp_Object = MibTableColumn
cie1000QosConfigQceIpv4DestIp = _Cie1000QosConfigQceIpv4DestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 408),
    _Cie1000QosConfigQceIpv4DestIp_Type()
)
cie1000QosConfigQceIpv4DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv4DestIp.setStatus("current")
_Cie1000QosConfigQceIpv4DestIpMask_Type = IpAddress
_Cie1000QosConfigQceIpv4DestIpMask_Object = MibTableColumn
cie1000QosConfigQceIpv4DestIpMask = _Cie1000QosConfigQceIpv4DestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 409),
    _Cie1000QosConfigQceIpv4DestIpMask_Type()
)
cie1000QosConfigQceIpv4DestIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv4DestIpMask.setStatus("current")
_Cie1000QosConfigQceIpv4SrcPortOp_Type = CIE1000ASRType
_Cie1000QosConfigQceIpv4SrcPortOp_Object = MibTableColumn
cie1000QosConfigQceIpv4SrcPortOp = _Cie1000QosConfigQceIpv4SrcPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 410),
    _Cie1000QosConfigQceIpv4SrcPortOp_Type()
)
cie1000QosConfigQceIpv4SrcPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv4SrcPortOp.setStatus("current")
_Cie1000QosConfigQceIpv4SrcPort_Type = CIE1000Unsigned16
_Cie1000QosConfigQceIpv4SrcPort_Object = MibTableColumn
cie1000QosConfigQceIpv4SrcPort = _Cie1000QosConfigQceIpv4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 411),
    _Cie1000QosConfigQceIpv4SrcPort_Type()
)
cie1000QosConfigQceIpv4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv4SrcPort.setStatus("current")
_Cie1000QosConfigQceIpv4SrcPortRange_Type = CIE1000Unsigned16
_Cie1000QosConfigQceIpv4SrcPortRange_Object = MibTableColumn
cie1000QosConfigQceIpv4SrcPortRange = _Cie1000QosConfigQceIpv4SrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 412),
    _Cie1000QosConfigQceIpv4SrcPortRange_Type()
)
cie1000QosConfigQceIpv4SrcPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv4SrcPortRange.setStatus("current")
_Cie1000QosConfigQceIpv4DestPortOp_Type = CIE1000ASRType
_Cie1000QosConfigQceIpv4DestPortOp_Object = MibTableColumn
cie1000QosConfigQceIpv4DestPortOp = _Cie1000QosConfigQceIpv4DestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 413),
    _Cie1000QosConfigQceIpv4DestPortOp_Type()
)
cie1000QosConfigQceIpv4DestPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv4DestPortOp.setStatus("current")
_Cie1000QosConfigQceIpv4DestPort_Type = CIE1000Unsigned16
_Cie1000QosConfigQceIpv4DestPort_Object = MibTableColumn
cie1000QosConfigQceIpv4DestPort = _Cie1000QosConfigQceIpv4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 414),
    _Cie1000QosConfigQceIpv4DestPort_Type()
)
cie1000QosConfigQceIpv4DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv4DestPort.setStatus("current")
_Cie1000QosConfigQceIpv4DestPortRange_Type = CIE1000Unsigned16
_Cie1000QosConfigQceIpv4DestPortRange_Object = MibTableColumn
cie1000QosConfigQceIpv4DestPortRange = _Cie1000QosConfigQceIpv4DestPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 415),
    _Cie1000QosConfigQceIpv4DestPortRange_Type()
)
cie1000QosConfigQceIpv4DestPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv4DestPortRange.setStatus("current")
_Cie1000QosConfigQceIpv6DscpOp_Type = CIE1000ASRType
_Cie1000QosConfigQceIpv6DscpOp_Object = MibTableColumn
cie1000QosConfigQceIpv6DscpOp = _Cie1000QosConfigQceIpv6DscpOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 500),
    _Cie1000QosConfigQceIpv6DscpOp_Type()
)
cie1000QosConfigQceIpv6DscpOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv6DscpOp.setStatus("current")
_Cie1000QosConfigQceIpv6Dscp_Type = Dscp
_Cie1000QosConfigQceIpv6Dscp_Object = MibTableColumn
cie1000QosConfigQceIpv6Dscp = _Cie1000QosConfigQceIpv6Dscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 501),
    _Cie1000QosConfigQceIpv6Dscp_Type()
)
cie1000QosConfigQceIpv6Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv6Dscp.setStatus("current")
_Cie1000QosConfigQceIpv6DscpRange_Type = Dscp
_Cie1000QosConfigQceIpv6DscpRange_Object = MibTableColumn
cie1000QosConfigQceIpv6DscpRange = _Cie1000QosConfigQceIpv6DscpRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 502),
    _Cie1000QosConfigQceIpv6DscpRange_Type()
)
cie1000QosConfigQceIpv6DscpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv6DscpRange.setStatus("current")
_Cie1000QosConfigQceIpv6Protocol_Type = CIE1000Unsigned8
_Cie1000QosConfigQceIpv6Protocol_Object = MibTableColumn
cie1000QosConfigQceIpv6Protocol = _Cie1000QosConfigQceIpv6Protocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 503),
    _Cie1000QosConfigQceIpv6Protocol_Type()
)
cie1000QosConfigQceIpv6Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv6Protocol.setStatus("current")
_Cie1000QosConfigQceIpv6ProtocolMask_Type = CIE1000Unsigned8
_Cie1000QosConfigQceIpv6ProtocolMask_Object = MibTableColumn
cie1000QosConfigQceIpv6ProtocolMask = _Cie1000QosConfigQceIpv6ProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 504),
    _Cie1000QosConfigQceIpv6ProtocolMask_Type()
)
cie1000QosConfigQceIpv6ProtocolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv6ProtocolMask.setStatus("current")
_Cie1000QosConfigQceIpv6SrcIp_Type = InetAddressIPv6
_Cie1000QosConfigQceIpv6SrcIp_Object = MibTableColumn
cie1000QosConfigQceIpv6SrcIp = _Cie1000QosConfigQceIpv6SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 506),
    _Cie1000QosConfigQceIpv6SrcIp_Type()
)
cie1000QosConfigQceIpv6SrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv6SrcIp.setStatus("current")
_Cie1000QosConfigQceIpv6SrcIpMask_Type = InetAddressIPv6
_Cie1000QosConfigQceIpv6SrcIpMask_Object = MibTableColumn
cie1000QosConfigQceIpv6SrcIpMask = _Cie1000QosConfigQceIpv6SrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 508),
    _Cie1000QosConfigQceIpv6SrcIpMask_Type()
)
cie1000QosConfigQceIpv6SrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv6SrcIpMask.setStatus("current")
_Cie1000QosConfigQceIpv6DestIp_Type = InetAddressIPv6
_Cie1000QosConfigQceIpv6DestIp_Object = MibTableColumn
cie1000QosConfigQceIpv6DestIp = _Cie1000QosConfigQceIpv6DestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 510),
    _Cie1000QosConfigQceIpv6DestIp_Type()
)
cie1000QosConfigQceIpv6DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv6DestIp.setStatus("current")
_Cie1000QosConfigQceIpv6DestIpMask_Type = InetAddressIPv6
_Cie1000QosConfigQceIpv6DestIpMask_Object = MibTableColumn
cie1000QosConfigQceIpv6DestIpMask = _Cie1000QosConfigQceIpv6DestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 512),
    _Cie1000QosConfigQceIpv6DestIpMask_Type()
)
cie1000QosConfigQceIpv6DestIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv6DestIpMask.setStatus("current")
_Cie1000QosConfigQceIpv6SrcPortOp_Type = CIE1000ASRType
_Cie1000QosConfigQceIpv6SrcPortOp_Object = MibTableColumn
cie1000QosConfigQceIpv6SrcPortOp = _Cie1000QosConfigQceIpv6SrcPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 513),
    _Cie1000QosConfigQceIpv6SrcPortOp_Type()
)
cie1000QosConfigQceIpv6SrcPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv6SrcPortOp.setStatus("current")
_Cie1000QosConfigQceIpv6SrcPort_Type = CIE1000Unsigned16
_Cie1000QosConfigQceIpv6SrcPort_Object = MibTableColumn
cie1000QosConfigQceIpv6SrcPort = _Cie1000QosConfigQceIpv6SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 514),
    _Cie1000QosConfigQceIpv6SrcPort_Type()
)
cie1000QosConfigQceIpv6SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv6SrcPort.setStatus("current")
_Cie1000QosConfigQceIpv6SrcPortRange_Type = CIE1000Unsigned16
_Cie1000QosConfigQceIpv6SrcPortRange_Object = MibTableColumn
cie1000QosConfigQceIpv6SrcPortRange = _Cie1000QosConfigQceIpv6SrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 515),
    _Cie1000QosConfigQceIpv6SrcPortRange_Type()
)
cie1000QosConfigQceIpv6SrcPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv6SrcPortRange.setStatus("current")
_Cie1000QosConfigQceIpv6DestPortOp_Type = CIE1000ASRType
_Cie1000QosConfigQceIpv6DestPortOp_Object = MibTableColumn
cie1000QosConfigQceIpv6DestPortOp = _Cie1000QosConfigQceIpv6DestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 516),
    _Cie1000QosConfigQceIpv6DestPortOp_Type()
)
cie1000QosConfigQceIpv6DestPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv6DestPortOp.setStatus("current")
_Cie1000QosConfigQceIpv6DestPort_Type = CIE1000Unsigned16
_Cie1000QosConfigQceIpv6DestPort_Object = MibTableColumn
cie1000QosConfigQceIpv6DestPort = _Cie1000QosConfigQceIpv6DestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 517),
    _Cie1000QosConfigQceIpv6DestPort_Type()
)
cie1000QosConfigQceIpv6DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv6DestPort.setStatus("current")
_Cie1000QosConfigQceIpv6DestPortRange_Type = CIE1000Unsigned16
_Cie1000QosConfigQceIpv6DestPortRange_Object = MibTableColumn
cie1000QosConfigQceIpv6DestPortRange = _Cie1000QosConfigQceIpv6DestPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 518),
    _Cie1000QosConfigQceIpv6DestPortRange_Type()
)
cie1000QosConfigQceIpv6DestPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceIpv6DestPortRange.setStatus("current")
_Cie1000QosConfigQceActionCosEnable_Type = TruthValue
_Cie1000QosConfigQceActionCosEnable_Object = MibTableColumn
cie1000QosConfigQceActionCosEnable = _Cie1000QosConfigQceActionCosEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 1000),
    _Cie1000QosConfigQceActionCosEnable_Type()
)
cie1000QosConfigQceActionCosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceActionCosEnable.setStatus("current")
_Cie1000QosConfigQceActionCos_Type = Unsigned32
_Cie1000QosConfigQceActionCos_Object = MibTableColumn
cie1000QosConfigQceActionCos = _Cie1000QosConfigQceActionCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 1001),
    _Cie1000QosConfigQceActionCos_Type()
)
cie1000QosConfigQceActionCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceActionCos.setStatus("current")
_Cie1000QosConfigQceActionDplEnable_Type = TruthValue
_Cie1000QosConfigQceActionDplEnable_Object = MibTableColumn
cie1000QosConfigQceActionDplEnable = _Cie1000QosConfigQceActionDplEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 1002),
    _Cie1000QosConfigQceActionDplEnable_Type()
)
cie1000QosConfigQceActionDplEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceActionDplEnable.setStatus("current")
_Cie1000QosConfigQceActionDpl_Type = CIE1000Unsigned8
_Cie1000QosConfigQceActionDpl_Object = MibTableColumn
cie1000QosConfigQceActionDpl = _Cie1000QosConfigQceActionDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 1003),
    _Cie1000QosConfigQceActionDpl_Type()
)
cie1000QosConfigQceActionDpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceActionDpl.setStatus("current")
_Cie1000QosConfigQceActionDscpEnable_Type = TruthValue
_Cie1000QosConfigQceActionDscpEnable_Object = MibTableColumn
cie1000QosConfigQceActionDscpEnable = _Cie1000QosConfigQceActionDscpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 1004),
    _Cie1000QosConfigQceActionDscpEnable_Type()
)
cie1000QosConfigQceActionDscpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceActionDscpEnable.setStatus("current")
_Cie1000QosConfigQceActionDscp_Type = CIE1000Unsigned8
_Cie1000QosConfigQceActionDscp_Object = MibTableColumn
cie1000QosConfigQceActionDscp = _Cie1000QosConfigQceActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 1005),
    _Cie1000QosConfigQceActionDscp_Type()
)
cie1000QosConfigQceActionDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceActionDscp.setStatus("current")
_Cie1000QosConfigQceActionPcpDeiEnable_Type = TruthValue
_Cie1000QosConfigQceActionPcpDeiEnable_Object = MibTableColumn
cie1000QosConfigQceActionPcpDeiEnable = _Cie1000QosConfigQceActionPcpDeiEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 1006),
    _Cie1000QosConfigQceActionPcpDeiEnable_Type()
)
cie1000QosConfigQceActionPcpDeiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceActionPcpDeiEnable.setStatus("current")
_Cie1000QosConfigQceActionPcp_Type = Unsigned32
_Cie1000QosConfigQceActionPcp_Object = MibTableColumn
cie1000QosConfigQceActionPcp = _Cie1000QosConfigQceActionPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 1007),
    _Cie1000QosConfigQceActionPcp_Type()
)
cie1000QosConfigQceActionPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceActionPcp.setStatus("current")
_Cie1000QosConfigQceActionDei_Type = CIE1000Unsigned8
_Cie1000QosConfigQceActionDei_Object = MibTableColumn
cie1000QosConfigQceActionDei = _Cie1000QosConfigQceActionDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 1008),
    _Cie1000QosConfigQceActionDei_Type()
)
cie1000QosConfigQceActionDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceActionDei.setStatus("current")
_Cie1000QosConfigQceActionPolicyEnable_Type = TruthValue
_Cie1000QosConfigQceActionPolicyEnable_Object = MibTableColumn
cie1000QosConfigQceActionPolicyEnable = _Cie1000QosConfigQceActionPolicyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 1009),
    _Cie1000QosConfigQceActionPolicyEnable_Type()
)
cie1000QosConfigQceActionPolicyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceActionPolicyEnable.setStatus("current")
_Cie1000QosConfigQceActionPolicy_Type = Unsigned32
_Cie1000QosConfigQceActionPolicy_Object = MibTableColumn
cie1000QosConfigQceActionPolicy = _Cie1000QosConfigQceActionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 1010),
    _Cie1000QosConfigQceActionPolicy_Type()
)
cie1000QosConfigQceActionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceActionPolicy.setStatus("current")
_Cie1000QosConfigQceActionMapEnable_Type = TruthValue
_Cie1000QosConfigQceActionMapEnable_Object = MibTableColumn
cie1000QosConfigQceActionMapEnable = _Cie1000QosConfigQceActionMapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 1011),
    _Cie1000QosConfigQceActionMapEnable_Type()
)
cie1000QosConfigQceActionMapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceActionMapEnable.setStatus("current")
_Cie1000QosConfigQceActionMap_Type = CIE1000Unsigned16
_Cie1000QosConfigQceActionMap_Object = MibTableColumn
cie1000QosConfigQceActionMap = _Cie1000QosConfigQceActionMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 1012),
    _Cie1000QosConfigQceActionMap_Type()
)
cie1000QosConfigQceActionMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceActionMap.setStatus("current")
_Cie1000QosConfigQceAction_Type = CIE1000RowEditorState
_Cie1000QosConfigQceAction_Object = MibTableColumn
cie1000QosConfigQceAction = _Cie1000QosConfigQceAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 1, 1, 10000),
    _Cie1000QosConfigQceAction_Type()
)
cie1000QosConfigQceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceAction.setStatus("current")
_Cie1000QosConfigQceTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000QosConfigQceTableRowEditor = _Cie1000QosConfigQceTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2)
)


class _Cie1000QosConfigQceTableRowEditorQceId_Type(Integer32):
    """Custom type cie1000QosConfigQceTableRowEditorQceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000QosConfigQceTableRowEditorQceId_Type.__name__ = "Integer32"
_Cie1000QosConfigQceTableRowEditorQceId_Object = MibScalar
cie1000QosConfigQceTableRowEditorQceId = _Cie1000QosConfigQceTableRowEditorQceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 1),
    _Cie1000QosConfigQceTableRowEditorQceId_Type()
)
cie1000QosConfigQceTableRowEditorQceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorQceId.setStatus("current")
_Cie1000QosConfigQceTableRowEditorNextQceId_Type = Unsigned32
_Cie1000QosConfigQceTableRowEditorNextQceId_Object = MibScalar
cie1000QosConfigQceTableRowEditorNextQceId = _Cie1000QosConfigQceTableRowEditorNextQceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 2),
    _Cie1000QosConfigQceTableRowEditorNextQceId_Type()
)
cie1000QosConfigQceTableRowEditorNextQceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorNextQceId.setStatus("current")
_Cie1000QosConfigQceTableRowEditorSwitchId_Type = Unsigned32
_Cie1000QosConfigQceTableRowEditorSwitchId_Object = MibScalar
cie1000QosConfigQceTableRowEditorSwitchId = _Cie1000QosConfigQceTableRowEditorSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 3),
    _Cie1000QosConfigQceTableRowEditorSwitchId_Type()
)
cie1000QosConfigQceTableRowEditorSwitchId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorSwitchId.setStatus("current")
_Cie1000QosConfigQceTableRowEditorPortList_Type = CIE1000PortList
_Cie1000QosConfigQceTableRowEditorPortList_Object = MibScalar
cie1000QosConfigQceTableRowEditorPortList = _Cie1000QosConfigQceTableRowEditorPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 4),
    _Cie1000QosConfigQceTableRowEditorPortList_Type()
)
cie1000QosConfigQceTableRowEditorPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorPortList.setStatus("current")
_Cie1000QosConfigQceTableRowEditorDestMacType_Type = CIE1000DestMacType
_Cie1000QosConfigQceTableRowEditorDestMacType_Object = MibScalar
cie1000QosConfigQceTableRowEditorDestMacType = _Cie1000QosConfigQceTableRowEditorDestMacType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 5),
    _Cie1000QosConfigQceTableRowEditorDestMacType_Type()
)
cie1000QosConfigQceTableRowEditorDestMacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorDestMacType.setStatus("current")
_Cie1000QosConfigQceTableRowEditorDestMac_Type = MacAddress
_Cie1000QosConfigQceTableRowEditorDestMac_Object = MibScalar
cie1000QosConfigQceTableRowEditorDestMac = _Cie1000QosConfigQceTableRowEditorDestMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 6),
    _Cie1000QosConfigQceTableRowEditorDestMac_Type()
)
cie1000QosConfigQceTableRowEditorDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorDestMac.setStatus("current")
_Cie1000QosConfigQceTableRowEditorDestMacMask_Type = MacAddress
_Cie1000QosConfigQceTableRowEditorDestMacMask_Object = MibScalar
cie1000QosConfigQceTableRowEditorDestMacMask = _Cie1000QosConfigQceTableRowEditorDestMacMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 7),
    _Cie1000QosConfigQceTableRowEditorDestMacMask_Type()
)
cie1000QosConfigQceTableRowEditorDestMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorDestMacMask.setStatus("current")
_Cie1000QosConfigQceTableRowEditorSrcMac_Type = MacAddress
_Cie1000QosConfigQceTableRowEditorSrcMac_Object = MibScalar
cie1000QosConfigQceTableRowEditorSrcMac = _Cie1000QosConfigQceTableRowEditorSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 8),
    _Cie1000QosConfigQceTableRowEditorSrcMac_Type()
)
cie1000QosConfigQceTableRowEditorSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorSrcMac.setStatus("current")
_Cie1000QosConfigQceTableRowEditorSrcMacMask_Type = MacAddress
_Cie1000QosConfigQceTableRowEditorSrcMacMask_Object = MibScalar
cie1000QosConfigQceTableRowEditorSrcMacMask = _Cie1000QosConfigQceTableRowEditorSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 9),
    _Cie1000QosConfigQceTableRowEditorSrcMacMask_Type()
)
cie1000QosConfigQceTableRowEditorSrcMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorSrcMacMask.setStatus("current")
_Cie1000QosConfigQceTableRowEditorVlanTagType_Type = CIE1000VlanTagType
_Cie1000QosConfigQceTableRowEditorVlanTagType_Object = MibScalar
cie1000QosConfigQceTableRowEditorVlanTagType = _Cie1000QosConfigQceTableRowEditorVlanTagType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 10),
    _Cie1000QosConfigQceTableRowEditorVlanTagType_Type()
)
cie1000QosConfigQceTableRowEditorVlanTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorVlanTagType.setStatus("current")
_Cie1000QosConfigQceTableRowEditorVlanIdOp_Type = CIE1000ASRType
_Cie1000QosConfigQceTableRowEditorVlanIdOp_Object = MibScalar
cie1000QosConfigQceTableRowEditorVlanIdOp = _Cie1000QosConfigQceTableRowEditorVlanIdOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 11),
    _Cie1000QosConfigQceTableRowEditorVlanIdOp_Type()
)
cie1000QosConfigQceTableRowEditorVlanIdOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorVlanIdOp.setStatus("current")
_Cie1000QosConfigQceTableRowEditorVlanId_Type = CIE1000Unsigned16
_Cie1000QosConfigQceTableRowEditorVlanId_Object = MibScalar
cie1000QosConfigQceTableRowEditorVlanId = _Cie1000QosConfigQceTableRowEditorVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 12),
    _Cie1000QosConfigQceTableRowEditorVlanId_Type()
)
cie1000QosConfigQceTableRowEditorVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorVlanId.setStatus("current")
_Cie1000QosConfigQceTableRowEditorVlanIdRange_Type = CIE1000Unsigned16
_Cie1000QosConfigQceTableRowEditorVlanIdRange_Object = MibScalar
cie1000QosConfigQceTableRowEditorVlanIdRange = _Cie1000QosConfigQceTableRowEditorVlanIdRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 13),
    _Cie1000QosConfigQceTableRowEditorVlanIdRange_Type()
)
cie1000QosConfigQceTableRowEditorVlanIdRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorVlanIdRange.setStatus("current")
_Cie1000QosConfigQceTableRowEditorPcp_Type = CIE1000VlanTagPriority
_Cie1000QosConfigQceTableRowEditorPcp_Object = MibScalar
cie1000QosConfigQceTableRowEditorPcp = _Cie1000QosConfigQceTableRowEditorPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 14),
    _Cie1000QosConfigQceTableRowEditorPcp_Type()
)
cie1000QosConfigQceTableRowEditorPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorPcp.setStatus("current")
_Cie1000QosConfigQceTableRowEditorDei_Type = CIE1000BitType
_Cie1000QosConfigQceTableRowEditorDei_Object = MibScalar
cie1000QosConfigQceTableRowEditorDei = _Cie1000QosConfigQceTableRowEditorDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 15),
    _Cie1000QosConfigQceTableRowEditorDei_Type()
)
cie1000QosConfigQceTableRowEditorDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorDei.setStatus("current")
_Cie1000QosConfigQceTableRowEditorInnerVlanTagType_Type = CIE1000VlanTagType
_Cie1000QosConfigQceTableRowEditorInnerVlanTagType_Object = MibScalar
cie1000QosConfigQceTableRowEditorInnerVlanTagType = _Cie1000QosConfigQceTableRowEditorInnerVlanTagType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 16),
    _Cie1000QosConfigQceTableRowEditorInnerVlanTagType_Type()
)
cie1000QosConfigQceTableRowEditorInnerVlanTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorInnerVlanTagType.setStatus("current")
_Cie1000QosConfigQceTableRowEditorInnerVlanIdOp_Type = CIE1000ASRType
_Cie1000QosConfigQceTableRowEditorInnerVlanIdOp_Object = MibScalar
cie1000QosConfigQceTableRowEditorInnerVlanIdOp = _Cie1000QosConfigQceTableRowEditorInnerVlanIdOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 17),
    _Cie1000QosConfigQceTableRowEditorInnerVlanIdOp_Type()
)
cie1000QosConfigQceTableRowEditorInnerVlanIdOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorInnerVlanIdOp.setStatus("current")
_Cie1000QosConfigQceTableRowEditorInnerVlanId_Type = CIE1000Unsigned16
_Cie1000QosConfigQceTableRowEditorInnerVlanId_Object = MibScalar
cie1000QosConfigQceTableRowEditorInnerVlanId = _Cie1000QosConfigQceTableRowEditorInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 18),
    _Cie1000QosConfigQceTableRowEditorInnerVlanId_Type()
)
cie1000QosConfigQceTableRowEditorInnerVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorInnerVlanId.setStatus("current")
_Cie1000QosConfigQceTableRowEditorInnerVlanIdRange_Type = CIE1000Unsigned16
_Cie1000QosConfigQceTableRowEditorInnerVlanIdRange_Object = MibScalar
cie1000QosConfigQceTableRowEditorInnerVlanIdRange = _Cie1000QosConfigQceTableRowEditorInnerVlanIdRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 19),
    _Cie1000QosConfigQceTableRowEditorInnerVlanIdRange_Type()
)
cie1000QosConfigQceTableRowEditorInnerVlanIdRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorInnerVlanIdRange.setStatus("current")
_Cie1000QosConfigQceTableRowEditorInnerPcp_Type = CIE1000VlanTagPriority
_Cie1000QosConfigQceTableRowEditorInnerPcp_Object = MibScalar
cie1000QosConfigQceTableRowEditorInnerPcp = _Cie1000QosConfigQceTableRowEditorInnerPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 20),
    _Cie1000QosConfigQceTableRowEditorInnerPcp_Type()
)
cie1000QosConfigQceTableRowEditorInnerPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorInnerPcp.setStatus("current")
_Cie1000QosConfigQceTableRowEditorInnerDei_Type = CIE1000BitType
_Cie1000QosConfigQceTableRowEditorInnerDei_Object = MibScalar
cie1000QosConfigQceTableRowEditorInnerDei = _Cie1000QosConfigQceTableRowEditorInnerDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 21),
    _Cie1000QosConfigQceTableRowEditorInnerDei_Type()
)
cie1000QosConfigQceTableRowEditorInnerDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorInnerDei.setStatus("current")
_Cie1000QosConfigQceTableRowEditorFrameType_Type = CIE1000QosQceFrameType
_Cie1000QosConfigQceTableRowEditorFrameType_Object = MibScalar
cie1000QosConfigQceTableRowEditorFrameType = _Cie1000QosConfigQceTableRowEditorFrameType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 100),
    _Cie1000QosConfigQceTableRowEditorFrameType_Type()
)
cie1000QosConfigQceTableRowEditorFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorFrameType.setStatus("current")
_Cie1000QosConfigQceTableRowEditorEtype_Type = CIE1000EtherType
_Cie1000QosConfigQceTableRowEditorEtype_Object = MibScalar
cie1000QosConfigQceTableRowEditorEtype = _Cie1000QosConfigQceTableRowEditorEtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 101),
    _Cie1000QosConfigQceTableRowEditorEtype_Type()
)
cie1000QosConfigQceTableRowEditorEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorEtype.setStatus("current")
_Cie1000QosConfigQceTableRowEditorLlcDsap_Type = CIE1000Unsigned8
_Cie1000QosConfigQceTableRowEditorLlcDsap_Object = MibScalar
cie1000QosConfigQceTableRowEditorLlcDsap = _Cie1000QosConfigQceTableRowEditorLlcDsap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 200),
    _Cie1000QosConfigQceTableRowEditorLlcDsap_Type()
)
cie1000QosConfigQceTableRowEditorLlcDsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorLlcDsap.setStatus("current")
_Cie1000QosConfigQceTableRowEditorLlcDsapMask_Type = CIE1000Unsigned8
_Cie1000QosConfigQceTableRowEditorLlcDsapMask_Object = MibScalar
cie1000QosConfigQceTableRowEditorLlcDsapMask = _Cie1000QosConfigQceTableRowEditorLlcDsapMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 201),
    _Cie1000QosConfigQceTableRowEditorLlcDsapMask_Type()
)
cie1000QosConfigQceTableRowEditorLlcDsapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorLlcDsapMask.setStatus("current")
_Cie1000QosConfigQceTableRowEditorLlcSsap_Type = CIE1000Unsigned8
_Cie1000QosConfigQceTableRowEditorLlcSsap_Object = MibScalar
cie1000QosConfigQceTableRowEditorLlcSsap = _Cie1000QosConfigQceTableRowEditorLlcSsap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 202),
    _Cie1000QosConfigQceTableRowEditorLlcSsap_Type()
)
cie1000QosConfigQceTableRowEditorLlcSsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorLlcSsap.setStatus("current")
_Cie1000QosConfigQceTableRowEditorLlcSsapMask_Type = CIE1000Unsigned8
_Cie1000QosConfigQceTableRowEditorLlcSsapMask_Object = MibScalar
cie1000QosConfigQceTableRowEditorLlcSsapMask = _Cie1000QosConfigQceTableRowEditorLlcSsapMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 203),
    _Cie1000QosConfigQceTableRowEditorLlcSsapMask_Type()
)
cie1000QosConfigQceTableRowEditorLlcSsapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorLlcSsapMask.setStatus("current")
_Cie1000QosConfigQceTableRowEditorLlcControl_Type = CIE1000Unsigned8
_Cie1000QosConfigQceTableRowEditorLlcControl_Object = MibScalar
cie1000QosConfigQceTableRowEditorLlcControl = _Cie1000QosConfigQceTableRowEditorLlcControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 204),
    _Cie1000QosConfigQceTableRowEditorLlcControl_Type()
)
cie1000QosConfigQceTableRowEditorLlcControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorLlcControl.setStatus("current")
_Cie1000QosConfigQceTableRowEditorLlcControlMask_Type = CIE1000Unsigned8
_Cie1000QosConfigQceTableRowEditorLlcControlMask_Object = MibScalar
cie1000QosConfigQceTableRowEditorLlcControlMask = _Cie1000QosConfigQceTableRowEditorLlcControlMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 205),
    _Cie1000QosConfigQceTableRowEditorLlcControlMask_Type()
)
cie1000QosConfigQceTableRowEditorLlcControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorLlcControlMask.setStatus("current")
_Cie1000QosConfigQceTableRowEditorSnapPid_Type = CIE1000Unsigned16
_Cie1000QosConfigQceTableRowEditorSnapPid_Object = MibScalar
cie1000QosConfigQceTableRowEditorSnapPid = _Cie1000QosConfigQceTableRowEditorSnapPid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 302),
    _Cie1000QosConfigQceTableRowEditorSnapPid_Type()
)
cie1000QosConfigQceTableRowEditorSnapPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorSnapPid.setStatus("current")
_Cie1000QosConfigQceTableRowEditorSnapPidMask_Type = CIE1000Unsigned16
_Cie1000QosConfigQceTableRowEditorSnapPidMask_Object = MibScalar
cie1000QosConfigQceTableRowEditorSnapPidMask = _Cie1000QosConfigQceTableRowEditorSnapPidMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 303),
    _Cie1000QosConfigQceTableRowEditorSnapPidMask_Type()
)
cie1000QosConfigQceTableRowEditorSnapPidMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorSnapPidMask.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv4Fragment_Type = CIE1000BitType
_Cie1000QosConfigQceTableRowEditorIpv4Fragment_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv4Fragment = _Cie1000QosConfigQceTableRowEditorIpv4Fragment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 400),
    _Cie1000QosConfigQceTableRowEditorIpv4Fragment_Type()
)
cie1000QosConfigQceTableRowEditorIpv4Fragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv4Fragment.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv4DscpOp_Type = CIE1000ASRType
_Cie1000QosConfigQceTableRowEditorIpv4DscpOp_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv4DscpOp = _Cie1000QosConfigQceTableRowEditorIpv4DscpOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 401),
    _Cie1000QosConfigQceTableRowEditorIpv4DscpOp_Type()
)
cie1000QosConfigQceTableRowEditorIpv4DscpOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv4DscpOp.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv4Dscp_Type = Dscp
_Cie1000QosConfigQceTableRowEditorIpv4Dscp_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv4Dscp = _Cie1000QosConfigQceTableRowEditorIpv4Dscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 402),
    _Cie1000QosConfigQceTableRowEditorIpv4Dscp_Type()
)
cie1000QosConfigQceTableRowEditorIpv4Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv4Dscp.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv4DscpRange_Type = Dscp
_Cie1000QosConfigQceTableRowEditorIpv4DscpRange_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv4DscpRange = _Cie1000QosConfigQceTableRowEditorIpv4DscpRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 403),
    _Cie1000QosConfigQceTableRowEditorIpv4DscpRange_Type()
)
cie1000QosConfigQceTableRowEditorIpv4DscpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv4DscpRange.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv4Protocol_Type = CIE1000Unsigned8
_Cie1000QosConfigQceTableRowEditorIpv4Protocol_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv4Protocol = _Cie1000QosConfigQceTableRowEditorIpv4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 404),
    _Cie1000QosConfigQceTableRowEditorIpv4Protocol_Type()
)
cie1000QosConfigQceTableRowEditorIpv4Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv4Protocol.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv4ProtocolMask_Type = CIE1000Unsigned8
_Cie1000QosConfigQceTableRowEditorIpv4ProtocolMask_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv4ProtocolMask = _Cie1000QosConfigQceTableRowEditorIpv4ProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 405),
    _Cie1000QosConfigQceTableRowEditorIpv4ProtocolMask_Type()
)
cie1000QosConfigQceTableRowEditorIpv4ProtocolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv4ProtocolMask.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv4SrcIp_Type = IpAddress
_Cie1000QosConfigQceTableRowEditorIpv4SrcIp_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv4SrcIp = _Cie1000QosConfigQceTableRowEditorIpv4SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 406),
    _Cie1000QosConfigQceTableRowEditorIpv4SrcIp_Type()
)
cie1000QosConfigQceTableRowEditorIpv4SrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv4SrcIp.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv4SrcIpMask_Type = IpAddress
_Cie1000QosConfigQceTableRowEditorIpv4SrcIpMask_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv4SrcIpMask = _Cie1000QosConfigQceTableRowEditorIpv4SrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 407),
    _Cie1000QosConfigQceTableRowEditorIpv4SrcIpMask_Type()
)
cie1000QosConfigQceTableRowEditorIpv4SrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv4SrcIpMask.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv4DestIp_Type = IpAddress
_Cie1000QosConfigQceTableRowEditorIpv4DestIp_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv4DestIp = _Cie1000QosConfigQceTableRowEditorIpv4DestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 408),
    _Cie1000QosConfigQceTableRowEditorIpv4DestIp_Type()
)
cie1000QosConfigQceTableRowEditorIpv4DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv4DestIp.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv4DestIpMask_Type = IpAddress
_Cie1000QosConfigQceTableRowEditorIpv4DestIpMask_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv4DestIpMask = _Cie1000QosConfigQceTableRowEditorIpv4DestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 409),
    _Cie1000QosConfigQceTableRowEditorIpv4DestIpMask_Type()
)
cie1000QosConfigQceTableRowEditorIpv4DestIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv4DestIpMask.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv4SrcPortOp_Type = CIE1000ASRType
_Cie1000QosConfigQceTableRowEditorIpv4SrcPortOp_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv4SrcPortOp = _Cie1000QosConfigQceTableRowEditorIpv4SrcPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 410),
    _Cie1000QosConfigQceTableRowEditorIpv4SrcPortOp_Type()
)
cie1000QosConfigQceTableRowEditorIpv4SrcPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv4SrcPortOp.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv4SrcPort_Type = CIE1000Unsigned16
_Cie1000QosConfigQceTableRowEditorIpv4SrcPort_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv4SrcPort = _Cie1000QosConfigQceTableRowEditorIpv4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 411),
    _Cie1000QosConfigQceTableRowEditorIpv4SrcPort_Type()
)
cie1000QosConfigQceTableRowEditorIpv4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv4SrcPort.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv4SrcPortRange_Type = CIE1000Unsigned16
_Cie1000QosConfigQceTableRowEditorIpv4SrcPortRange_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv4SrcPortRange = _Cie1000QosConfigQceTableRowEditorIpv4SrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 412),
    _Cie1000QosConfigQceTableRowEditorIpv4SrcPortRange_Type()
)
cie1000QosConfigQceTableRowEditorIpv4SrcPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv4SrcPortRange.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv4DestPortOp_Type = CIE1000ASRType
_Cie1000QosConfigQceTableRowEditorIpv4DestPortOp_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv4DestPortOp = _Cie1000QosConfigQceTableRowEditorIpv4DestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 413),
    _Cie1000QosConfigQceTableRowEditorIpv4DestPortOp_Type()
)
cie1000QosConfigQceTableRowEditorIpv4DestPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv4DestPortOp.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv4DestPort_Type = CIE1000Unsigned16
_Cie1000QosConfigQceTableRowEditorIpv4DestPort_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv4DestPort = _Cie1000QosConfigQceTableRowEditorIpv4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 414),
    _Cie1000QosConfigQceTableRowEditorIpv4DestPort_Type()
)
cie1000QosConfigQceTableRowEditorIpv4DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv4DestPort.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv4DestPortRange_Type = CIE1000Unsigned16
_Cie1000QosConfigQceTableRowEditorIpv4DestPortRange_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv4DestPortRange = _Cie1000QosConfigQceTableRowEditorIpv4DestPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 415),
    _Cie1000QosConfigQceTableRowEditorIpv4DestPortRange_Type()
)
cie1000QosConfigQceTableRowEditorIpv4DestPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv4DestPortRange.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv6DscpOp_Type = CIE1000ASRType
_Cie1000QosConfigQceTableRowEditorIpv6DscpOp_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv6DscpOp = _Cie1000QosConfigQceTableRowEditorIpv6DscpOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 500),
    _Cie1000QosConfigQceTableRowEditorIpv6DscpOp_Type()
)
cie1000QosConfigQceTableRowEditorIpv6DscpOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv6DscpOp.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv6Dscp_Type = Dscp
_Cie1000QosConfigQceTableRowEditorIpv6Dscp_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv6Dscp = _Cie1000QosConfigQceTableRowEditorIpv6Dscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 501),
    _Cie1000QosConfigQceTableRowEditorIpv6Dscp_Type()
)
cie1000QosConfigQceTableRowEditorIpv6Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv6Dscp.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv6DscpRange_Type = Dscp
_Cie1000QosConfigQceTableRowEditorIpv6DscpRange_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv6DscpRange = _Cie1000QosConfigQceTableRowEditorIpv6DscpRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 502),
    _Cie1000QosConfigQceTableRowEditorIpv6DscpRange_Type()
)
cie1000QosConfigQceTableRowEditorIpv6DscpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv6DscpRange.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv6Protocol_Type = CIE1000Unsigned8
_Cie1000QosConfigQceTableRowEditorIpv6Protocol_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv6Protocol = _Cie1000QosConfigQceTableRowEditorIpv6Protocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 503),
    _Cie1000QosConfigQceTableRowEditorIpv6Protocol_Type()
)
cie1000QosConfigQceTableRowEditorIpv6Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv6Protocol.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv6ProtocolMask_Type = CIE1000Unsigned8
_Cie1000QosConfigQceTableRowEditorIpv6ProtocolMask_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv6ProtocolMask = _Cie1000QosConfigQceTableRowEditorIpv6ProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 504),
    _Cie1000QosConfigQceTableRowEditorIpv6ProtocolMask_Type()
)
cie1000QosConfigQceTableRowEditorIpv6ProtocolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv6ProtocolMask.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv6SrcIp_Type = InetAddressIPv6
_Cie1000QosConfigQceTableRowEditorIpv6SrcIp_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv6SrcIp = _Cie1000QosConfigQceTableRowEditorIpv6SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 506),
    _Cie1000QosConfigQceTableRowEditorIpv6SrcIp_Type()
)
cie1000QosConfigQceTableRowEditorIpv6SrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv6SrcIp.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv6SrcIpMask_Type = InetAddressIPv6
_Cie1000QosConfigQceTableRowEditorIpv6SrcIpMask_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv6SrcIpMask = _Cie1000QosConfigQceTableRowEditorIpv6SrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 508),
    _Cie1000QosConfigQceTableRowEditorIpv6SrcIpMask_Type()
)
cie1000QosConfigQceTableRowEditorIpv6SrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv6SrcIpMask.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv6DestIp_Type = InetAddressIPv6
_Cie1000QosConfigQceTableRowEditorIpv6DestIp_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv6DestIp = _Cie1000QosConfigQceTableRowEditorIpv6DestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 510),
    _Cie1000QosConfigQceTableRowEditorIpv6DestIp_Type()
)
cie1000QosConfigQceTableRowEditorIpv6DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv6DestIp.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv6DestIpMask_Type = InetAddressIPv6
_Cie1000QosConfigQceTableRowEditorIpv6DestIpMask_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv6DestIpMask = _Cie1000QosConfigQceTableRowEditorIpv6DestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 512),
    _Cie1000QosConfigQceTableRowEditorIpv6DestIpMask_Type()
)
cie1000QosConfigQceTableRowEditorIpv6DestIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv6DestIpMask.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv6SrcPortOp_Type = CIE1000ASRType
_Cie1000QosConfigQceTableRowEditorIpv6SrcPortOp_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv6SrcPortOp = _Cie1000QosConfigQceTableRowEditorIpv6SrcPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 513),
    _Cie1000QosConfigQceTableRowEditorIpv6SrcPortOp_Type()
)
cie1000QosConfigQceTableRowEditorIpv6SrcPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv6SrcPortOp.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv6SrcPort_Type = CIE1000Unsigned16
_Cie1000QosConfigQceTableRowEditorIpv6SrcPort_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv6SrcPort = _Cie1000QosConfigQceTableRowEditorIpv6SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 514),
    _Cie1000QosConfigQceTableRowEditorIpv6SrcPort_Type()
)
cie1000QosConfigQceTableRowEditorIpv6SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv6SrcPort.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv6SrcPortRange_Type = CIE1000Unsigned16
_Cie1000QosConfigQceTableRowEditorIpv6SrcPortRange_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv6SrcPortRange = _Cie1000QosConfigQceTableRowEditorIpv6SrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 515),
    _Cie1000QosConfigQceTableRowEditorIpv6SrcPortRange_Type()
)
cie1000QosConfigQceTableRowEditorIpv6SrcPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv6SrcPortRange.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv6DestPortOp_Type = CIE1000ASRType
_Cie1000QosConfigQceTableRowEditorIpv6DestPortOp_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv6DestPortOp = _Cie1000QosConfigQceTableRowEditorIpv6DestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 516),
    _Cie1000QosConfigQceTableRowEditorIpv6DestPortOp_Type()
)
cie1000QosConfigQceTableRowEditorIpv6DestPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv6DestPortOp.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv6DestPort_Type = CIE1000Unsigned16
_Cie1000QosConfigQceTableRowEditorIpv6DestPort_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv6DestPort = _Cie1000QosConfigQceTableRowEditorIpv6DestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 517),
    _Cie1000QosConfigQceTableRowEditorIpv6DestPort_Type()
)
cie1000QosConfigQceTableRowEditorIpv6DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv6DestPort.setStatus("current")
_Cie1000QosConfigQceTableRowEditorIpv6DestPortRange_Type = CIE1000Unsigned16
_Cie1000QosConfigQceTableRowEditorIpv6DestPortRange_Object = MibScalar
cie1000QosConfigQceTableRowEditorIpv6DestPortRange = _Cie1000QosConfigQceTableRowEditorIpv6DestPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 518),
    _Cie1000QosConfigQceTableRowEditorIpv6DestPortRange_Type()
)
cie1000QosConfigQceTableRowEditorIpv6DestPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorIpv6DestPortRange.setStatus("current")
_Cie1000QosConfigQceTableRowEditorActionCosEnable_Type = TruthValue
_Cie1000QosConfigQceTableRowEditorActionCosEnable_Object = MibScalar
cie1000QosConfigQceTableRowEditorActionCosEnable = _Cie1000QosConfigQceTableRowEditorActionCosEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 1000),
    _Cie1000QosConfigQceTableRowEditorActionCosEnable_Type()
)
cie1000QosConfigQceTableRowEditorActionCosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorActionCosEnable.setStatus("current")
_Cie1000QosConfigQceTableRowEditorActionCos_Type = Unsigned32
_Cie1000QosConfigQceTableRowEditorActionCos_Object = MibScalar
cie1000QosConfigQceTableRowEditorActionCos = _Cie1000QosConfigQceTableRowEditorActionCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 1001),
    _Cie1000QosConfigQceTableRowEditorActionCos_Type()
)
cie1000QosConfigQceTableRowEditorActionCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorActionCos.setStatus("current")
_Cie1000QosConfigQceTableRowEditorActionDplEnable_Type = TruthValue
_Cie1000QosConfigQceTableRowEditorActionDplEnable_Object = MibScalar
cie1000QosConfigQceTableRowEditorActionDplEnable = _Cie1000QosConfigQceTableRowEditorActionDplEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 1002),
    _Cie1000QosConfigQceTableRowEditorActionDplEnable_Type()
)
cie1000QosConfigQceTableRowEditorActionDplEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorActionDplEnable.setStatus("current")
_Cie1000QosConfigQceTableRowEditorActionDpl_Type = CIE1000Unsigned8
_Cie1000QosConfigQceTableRowEditorActionDpl_Object = MibScalar
cie1000QosConfigQceTableRowEditorActionDpl = _Cie1000QosConfigQceTableRowEditorActionDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 1003),
    _Cie1000QosConfigQceTableRowEditorActionDpl_Type()
)
cie1000QosConfigQceTableRowEditorActionDpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorActionDpl.setStatus("current")
_Cie1000QosConfigQceTableRowEditorActionDscpEnable_Type = TruthValue
_Cie1000QosConfigQceTableRowEditorActionDscpEnable_Object = MibScalar
cie1000QosConfigQceTableRowEditorActionDscpEnable = _Cie1000QosConfigQceTableRowEditorActionDscpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 1004),
    _Cie1000QosConfigQceTableRowEditorActionDscpEnable_Type()
)
cie1000QosConfigQceTableRowEditorActionDscpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorActionDscpEnable.setStatus("current")
_Cie1000QosConfigQceTableRowEditorActionDscp_Type = CIE1000Unsigned8
_Cie1000QosConfigQceTableRowEditorActionDscp_Object = MibScalar
cie1000QosConfigQceTableRowEditorActionDscp = _Cie1000QosConfigQceTableRowEditorActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 1005),
    _Cie1000QosConfigQceTableRowEditorActionDscp_Type()
)
cie1000QosConfigQceTableRowEditorActionDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorActionDscp.setStatus("current")
_Cie1000QosConfigQceTableRowEditorActionPcpDeiEnable_Type = TruthValue
_Cie1000QosConfigQceTableRowEditorActionPcpDeiEnable_Object = MibScalar
cie1000QosConfigQceTableRowEditorActionPcpDeiEnable = _Cie1000QosConfigQceTableRowEditorActionPcpDeiEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 1006),
    _Cie1000QosConfigQceTableRowEditorActionPcpDeiEnable_Type()
)
cie1000QosConfigQceTableRowEditorActionPcpDeiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorActionPcpDeiEnable.setStatus("current")
_Cie1000QosConfigQceTableRowEditorActionPcp_Type = Unsigned32
_Cie1000QosConfigQceTableRowEditorActionPcp_Object = MibScalar
cie1000QosConfigQceTableRowEditorActionPcp = _Cie1000QosConfigQceTableRowEditorActionPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 1007),
    _Cie1000QosConfigQceTableRowEditorActionPcp_Type()
)
cie1000QosConfigQceTableRowEditorActionPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorActionPcp.setStatus("current")
_Cie1000QosConfigQceTableRowEditorActionDei_Type = CIE1000Unsigned8
_Cie1000QosConfigQceTableRowEditorActionDei_Object = MibScalar
cie1000QosConfigQceTableRowEditorActionDei = _Cie1000QosConfigQceTableRowEditorActionDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 1008),
    _Cie1000QosConfigQceTableRowEditorActionDei_Type()
)
cie1000QosConfigQceTableRowEditorActionDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorActionDei.setStatus("current")
_Cie1000QosConfigQceTableRowEditorActionPolicyEnable_Type = TruthValue
_Cie1000QosConfigQceTableRowEditorActionPolicyEnable_Object = MibScalar
cie1000QosConfigQceTableRowEditorActionPolicyEnable = _Cie1000QosConfigQceTableRowEditorActionPolicyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 1009),
    _Cie1000QosConfigQceTableRowEditorActionPolicyEnable_Type()
)
cie1000QosConfigQceTableRowEditorActionPolicyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorActionPolicyEnable.setStatus("current")
_Cie1000QosConfigQceTableRowEditorActionPolicy_Type = Unsigned32
_Cie1000QosConfigQceTableRowEditorActionPolicy_Object = MibScalar
cie1000QosConfigQceTableRowEditorActionPolicy = _Cie1000QosConfigQceTableRowEditorActionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 1010),
    _Cie1000QosConfigQceTableRowEditorActionPolicy_Type()
)
cie1000QosConfigQceTableRowEditorActionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorActionPolicy.setStatus("current")
_Cie1000QosConfigQceTableRowEditorActionMapEnable_Type = TruthValue
_Cie1000QosConfigQceTableRowEditorActionMapEnable_Object = MibScalar
cie1000QosConfigQceTableRowEditorActionMapEnable = _Cie1000QosConfigQceTableRowEditorActionMapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 1011),
    _Cie1000QosConfigQceTableRowEditorActionMapEnable_Type()
)
cie1000QosConfigQceTableRowEditorActionMapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorActionMapEnable.setStatus("current")
_Cie1000QosConfigQceTableRowEditorActionMap_Type = CIE1000Unsigned16
_Cie1000QosConfigQceTableRowEditorActionMap_Object = MibScalar
cie1000QosConfigQceTableRowEditorActionMap = _Cie1000QosConfigQceTableRowEditorActionMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 1012),
    _Cie1000QosConfigQceTableRowEditorActionMap_Type()
)
cie1000QosConfigQceTableRowEditorActionMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorActionMap.setStatus("current")
_Cie1000QosConfigQceTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000QosConfigQceTableRowEditorAction_Object = MibScalar
cie1000QosConfigQceTableRowEditorAction = _Cie1000QosConfigQceTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 2, 10000),
    _Cie1000QosConfigQceTableRowEditorAction_Type()
)
cie1000QosConfigQceTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorAction.setStatus("current")
_Cie1000QosConfigQcePrecedenceTable_Object = MibTable
cie1000QosConfigQcePrecedenceTable = _Cie1000QosConfigQcePrecedenceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    cie1000QosConfigQcePrecedenceTable.setStatus("current")
_Cie1000QosConfigQcePrecedenceEntry_Object = MibTableRow
cie1000QosConfigQcePrecedenceEntry = _Cie1000QosConfigQcePrecedenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 3, 1)
)
cie1000QosConfigQcePrecedenceEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigQcePrecedenceIndex"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigQcePrecedenceEntry.setStatus("current")


class _Cie1000QosConfigQcePrecedenceIndex_Type(Integer32):
    """Custom type cie1000QosConfigQcePrecedenceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000QosConfigQcePrecedenceIndex_Type.__name__ = "Integer32"
_Cie1000QosConfigQcePrecedenceIndex_Object = MibTableColumn
cie1000QosConfigQcePrecedenceIndex = _Cie1000QosConfigQcePrecedenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 3, 1, 1),
    _Cie1000QosConfigQcePrecedenceIndex_Type()
)
cie1000QosConfigQcePrecedenceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigQcePrecedenceIndex.setStatus("current")
_Cie1000QosConfigQcePrecedenceQceId_Type = Unsigned32
_Cie1000QosConfigQcePrecedenceQceId_Object = MibTableColumn
cie1000QosConfigQcePrecedenceQceId = _Cie1000QosConfigQcePrecedenceQceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 3, 3, 1, 2),
    _Cie1000QosConfigQcePrecedenceQceId_Type()
)
cie1000QosConfigQcePrecedenceQceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosConfigQcePrecedenceQceId.setStatus("current")
_Cie1000QosConfigIngressMap_ObjectIdentity = ObjectIdentity
cie1000QosConfigIngressMap = _Cie1000QosConfigIngressMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4)
)
_Cie1000QosConfigIngressMapTable_Object = MibTable
cie1000QosConfigIngressMapTable = _Cie1000QosConfigIngressMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapTable.setStatus("current")
_Cie1000QosConfigIngressMapEntry_Object = MibTableRow
cie1000QosConfigIngressMapEntry = _Cie1000QosConfigIngressMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 1, 1)
)
cie1000QosConfigIngressMapEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigIngressMapIngressMapId"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapEntry.setStatus("current")


class _Cie1000QosConfigIngressMapIngressMapId_Type(Integer32):
    """Custom type cie1000QosConfigIngressMapIngressMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000QosConfigIngressMapIngressMapId_Type.__name__ = "Integer32"
_Cie1000QosConfigIngressMapIngressMapId_Object = MibTableColumn
cie1000QosConfigIngressMapIngressMapId = _Cie1000QosConfigIngressMapIngressMapId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 1, 1, 1),
    _Cie1000QosConfigIngressMapIngressMapId_Type()
)
cie1000QosConfigIngressMapIngressMapId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapIngressMapId.setStatus("current")
_Cie1000QosConfigIngressMapKey_Type = CIE1000QosIngressMapKey
_Cie1000QosConfigIngressMapKey_Object = MibTableColumn
cie1000QosConfigIngressMapKey = _Cie1000QosConfigIngressMapKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 1, 1, 2),
    _Cie1000QosConfigIngressMapKey_Type()
)
cie1000QosConfigIngressMapKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapKey.setStatus("current")
_Cie1000QosConfigIngressMapActionCos_Type = TruthValue
_Cie1000QosConfigIngressMapActionCos_Object = MibTableColumn
cie1000QosConfigIngressMapActionCos = _Cie1000QosConfigIngressMapActionCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 1, 1, 3),
    _Cie1000QosConfigIngressMapActionCos_Type()
)
cie1000QosConfigIngressMapActionCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapActionCos.setStatus("current")
_Cie1000QosConfigIngressMapActionDpl_Type = TruthValue
_Cie1000QosConfigIngressMapActionDpl_Object = MibTableColumn
cie1000QosConfigIngressMapActionDpl = _Cie1000QosConfigIngressMapActionDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 1, 1, 4),
    _Cie1000QosConfigIngressMapActionDpl_Type()
)
cie1000QosConfigIngressMapActionDpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapActionDpl.setStatus("current")
_Cie1000QosConfigIngressMapActionPcp_Type = TruthValue
_Cie1000QosConfigIngressMapActionPcp_Object = MibTableColumn
cie1000QosConfigIngressMapActionPcp = _Cie1000QosConfigIngressMapActionPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 1, 1, 5),
    _Cie1000QosConfigIngressMapActionPcp_Type()
)
cie1000QosConfigIngressMapActionPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapActionPcp.setStatus("current")
_Cie1000QosConfigIngressMapActionDei_Type = TruthValue
_Cie1000QosConfigIngressMapActionDei_Object = MibTableColumn
cie1000QosConfigIngressMapActionDei = _Cie1000QosConfigIngressMapActionDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 1, 1, 6),
    _Cie1000QosConfigIngressMapActionDei_Type()
)
cie1000QosConfigIngressMapActionDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapActionDei.setStatus("current")
_Cie1000QosConfigIngressMapActionDscp_Type = TruthValue
_Cie1000QosConfigIngressMapActionDscp_Object = MibTableColumn
cie1000QosConfigIngressMapActionDscp = _Cie1000QosConfigIngressMapActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 1, 1, 7),
    _Cie1000QosConfigIngressMapActionDscp_Type()
)
cie1000QosConfigIngressMapActionDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapActionDscp.setStatus("current")
_Cie1000QosConfigIngressMapActionCosid_Type = TruthValue
_Cie1000QosConfigIngressMapActionCosid_Object = MibTableColumn
cie1000QosConfigIngressMapActionCosid = _Cie1000QosConfigIngressMapActionCosid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 1, 1, 8),
    _Cie1000QosConfigIngressMapActionCosid_Type()
)
cie1000QosConfigIngressMapActionCosid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapActionCosid.setStatus("current")
_Cie1000QosConfigIngressMapActionPath_Type = TruthValue
_Cie1000QosConfigIngressMapActionPath_Object = MibTableColumn
cie1000QosConfigIngressMapActionPath = _Cie1000QosConfigIngressMapActionPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 1, 1, 9),
    _Cie1000QosConfigIngressMapActionPath_Type()
)
cie1000QosConfigIngressMapActionPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapActionPath.setStatus("current")
_Cie1000QosConfigIngressMapAction_Type = CIE1000RowEditorState
_Cie1000QosConfigIngressMapAction_Object = MibTableColumn
cie1000QosConfigIngressMapAction = _Cie1000QosConfigIngressMapAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 1, 1, 10000),
    _Cie1000QosConfigIngressMapAction_Type()
)
cie1000QosConfigIngressMapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapAction.setStatus("current")
_Cie1000QosConfigIngressMapTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000QosConfigIngressMapTableRowEditor = _Cie1000QosConfigIngressMapTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 2)
)


class _Cie1000QosConfigIngressMapTableRowEditorIngressMapId_Type(Integer32):
    """Custom type cie1000QosConfigIngressMapTableRowEditorIngressMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000QosConfigIngressMapTableRowEditorIngressMapId_Type.__name__ = "Integer32"
_Cie1000QosConfigIngressMapTableRowEditorIngressMapId_Object = MibScalar
cie1000QosConfigIngressMapTableRowEditorIngressMapId = _Cie1000QosConfigIngressMapTableRowEditorIngressMapId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 2, 1),
    _Cie1000QosConfigIngressMapTableRowEditorIngressMapId_Type()
)
cie1000QosConfigIngressMapTableRowEditorIngressMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapTableRowEditorIngressMapId.setStatus("current")
_Cie1000QosConfigIngressMapTableRowEditorKey_Type = CIE1000QosIngressMapKey
_Cie1000QosConfigIngressMapTableRowEditorKey_Object = MibScalar
cie1000QosConfigIngressMapTableRowEditorKey = _Cie1000QosConfigIngressMapTableRowEditorKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 2, 2),
    _Cie1000QosConfigIngressMapTableRowEditorKey_Type()
)
cie1000QosConfigIngressMapTableRowEditorKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapTableRowEditorKey.setStatus("current")
_Cie1000QosConfigIngressMapTableRowEditorActionCos_Type = TruthValue
_Cie1000QosConfigIngressMapTableRowEditorActionCos_Object = MibScalar
cie1000QosConfigIngressMapTableRowEditorActionCos = _Cie1000QosConfigIngressMapTableRowEditorActionCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 2, 3),
    _Cie1000QosConfigIngressMapTableRowEditorActionCos_Type()
)
cie1000QosConfigIngressMapTableRowEditorActionCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapTableRowEditorActionCos.setStatus("current")
_Cie1000QosConfigIngressMapTableRowEditorActionDpl_Type = TruthValue
_Cie1000QosConfigIngressMapTableRowEditorActionDpl_Object = MibScalar
cie1000QosConfigIngressMapTableRowEditorActionDpl = _Cie1000QosConfigIngressMapTableRowEditorActionDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 2, 4),
    _Cie1000QosConfigIngressMapTableRowEditorActionDpl_Type()
)
cie1000QosConfigIngressMapTableRowEditorActionDpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapTableRowEditorActionDpl.setStatus("current")
_Cie1000QosConfigIngressMapTableRowEditorActionPcp_Type = TruthValue
_Cie1000QosConfigIngressMapTableRowEditorActionPcp_Object = MibScalar
cie1000QosConfigIngressMapTableRowEditorActionPcp = _Cie1000QosConfigIngressMapTableRowEditorActionPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 2, 5),
    _Cie1000QosConfigIngressMapTableRowEditorActionPcp_Type()
)
cie1000QosConfigIngressMapTableRowEditorActionPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapTableRowEditorActionPcp.setStatus("current")
_Cie1000QosConfigIngressMapTableRowEditorActionDei_Type = TruthValue
_Cie1000QosConfigIngressMapTableRowEditorActionDei_Object = MibScalar
cie1000QosConfigIngressMapTableRowEditorActionDei = _Cie1000QosConfigIngressMapTableRowEditorActionDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 2, 6),
    _Cie1000QosConfigIngressMapTableRowEditorActionDei_Type()
)
cie1000QosConfigIngressMapTableRowEditorActionDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapTableRowEditorActionDei.setStatus("current")
_Cie1000QosConfigIngressMapTableRowEditorActionDscp_Type = TruthValue
_Cie1000QosConfigIngressMapTableRowEditorActionDscp_Object = MibScalar
cie1000QosConfigIngressMapTableRowEditorActionDscp = _Cie1000QosConfigIngressMapTableRowEditorActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 2, 7),
    _Cie1000QosConfigIngressMapTableRowEditorActionDscp_Type()
)
cie1000QosConfigIngressMapTableRowEditorActionDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapTableRowEditorActionDscp.setStatus("current")
_Cie1000QosConfigIngressMapTableRowEditorActionCosid_Type = TruthValue
_Cie1000QosConfigIngressMapTableRowEditorActionCosid_Object = MibScalar
cie1000QosConfigIngressMapTableRowEditorActionCosid = _Cie1000QosConfigIngressMapTableRowEditorActionCosid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 2, 8),
    _Cie1000QosConfigIngressMapTableRowEditorActionCosid_Type()
)
cie1000QosConfigIngressMapTableRowEditorActionCosid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapTableRowEditorActionCosid.setStatus("current")
_Cie1000QosConfigIngressMapTableRowEditorActionPath_Type = TruthValue
_Cie1000QosConfigIngressMapTableRowEditorActionPath_Object = MibScalar
cie1000QosConfigIngressMapTableRowEditorActionPath = _Cie1000QosConfigIngressMapTableRowEditorActionPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 2, 9),
    _Cie1000QosConfigIngressMapTableRowEditorActionPath_Type()
)
cie1000QosConfigIngressMapTableRowEditorActionPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapTableRowEditorActionPath.setStatus("current")
_Cie1000QosConfigIngressMapTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000QosConfigIngressMapTableRowEditorAction_Object = MibScalar
cie1000QosConfigIngressMapTableRowEditorAction = _Cie1000QosConfigIngressMapTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 2, 10000),
    _Cie1000QosConfigIngressMapTableRowEditorAction_Type()
)
cie1000QosConfigIngressMapTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapTableRowEditorAction.setStatus("current")
_Cie1000QosConfigIngressMapPcpTable_Object = MibTable
cie1000QosConfigIngressMapPcpTable = _Cie1000QosConfigIngressMapPcpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 3)
)
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapPcpTable.setStatus("current")
_Cie1000QosConfigIngressMapPcpEntry_Object = MibTableRow
cie1000QosConfigIngressMapPcpEntry = _Cie1000QosConfigIngressMapPcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 3, 1)
)
cie1000QosConfigIngressMapPcpEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigIngressMapPcpIngressMapId"),
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigIngressMapPcpPcp"),
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigIngressMapPcpDei"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapPcpEntry.setStatus("current")


class _Cie1000QosConfigIngressMapPcpIngressMapId_Type(Integer32):
    """Custom type cie1000QosConfigIngressMapPcpIngressMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000QosConfigIngressMapPcpIngressMapId_Type.__name__ = "Integer32"
_Cie1000QosConfigIngressMapPcpIngressMapId_Object = MibTableColumn
cie1000QosConfigIngressMapPcpIngressMapId = _Cie1000QosConfigIngressMapPcpIngressMapId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 3, 1, 1),
    _Cie1000QosConfigIngressMapPcpIngressMapId_Type()
)
cie1000QosConfigIngressMapPcpIngressMapId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapPcpIngressMapId.setStatus("current")


class _Cie1000QosConfigIngressMapPcpPcp_Type(Integer32):
    """Custom type cie1000QosConfigIngressMapPcpPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cie1000QosConfigIngressMapPcpPcp_Type.__name__ = "Integer32"
_Cie1000QosConfigIngressMapPcpPcp_Object = MibTableColumn
cie1000QosConfigIngressMapPcpPcp = _Cie1000QosConfigIngressMapPcpPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 3, 1, 2),
    _Cie1000QosConfigIngressMapPcpPcp_Type()
)
cie1000QosConfigIngressMapPcpPcp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapPcpPcp.setStatus("current")


class _Cie1000QosConfigIngressMapPcpDei_Type(Integer32):
    """Custom type cie1000QosConfigIngressMapPcpDei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Cie1000QosConfigIngressMapPcpDei_Type.__name__ = "Integer32"
_Cie1000QosConfigIngressMapPcpDei_Object = MibTableColumn
cie1000QosConfigIngressMapPcpDei = _Cie1000QosConfigIngressMapPcpDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 3, 1, 3),
    _Cie1000QosConfigIngressMapPcpDei_Type()
)
cie1000QosConfigIngressMapPcpDei.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapPcpDei.setStatus("current")
_Cie1000QosConfigIngressMapPcpToCos_Type = CIE1000Unsigned8
_Cie1000QosConfigIngressMapPcpToCos_Object = MibTableColumn
cie1000QosConfigIngressMapPcpToCos = _Cie1000QosConfigIngressMapPcpToCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 3, 1, 4),
    _Cie1000QosConfigIngressMapPcpToCos_Type()
)
cie1000QosConfigIngressMapPcpToCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapPcpToCos.setStatus("current")
_Cie1000QosConfigIngressMapPcpToDpl_Type = CIE1000Unsigned8
_Cie1000QosConfigIngressMapPcpToDpl_Object = MibTableColumn
cie1000QosConfigIngressMapPcpToDpl = _Cie1000QosConfigIngressMapPcpToDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 3, 1, 5),
    _Cie1000QosConfigIngressMapPcpToDpl_Type()
)
cie1000QosConfigIngressMapPcpToDpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapPcpToDpl.setStatus("current")
_Cie1000QosConfigIngressMapPcpToPcp_Type = CIE1000Unsigned8
_Cie1000QosConfigIngressMapPcpToPcp_Object = MibTableColumn
cie1000QosConfigIngressMapPcpToPcp = _Cie1000QosConfigIngressMapPcpToPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 3, 1, 6),
    _Cie1000QosConfigIngressMapPcpToPcp_Type()
)
cie1000QosConfigIngressMapPcpToPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapPcpToPcp.setStatus("current")
_Cie1000QosConfigIngressMapPcpToDei_Type = CIE1000Unsigned8
_Cie1000QosConfigIngressMapPcpToDei_Object = MibTableColumn
cie1000QosConfigIngressMapPcpToDei = _Cie1000QosConfigIngressMapPcpToDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 3, 1, 7),
    _Cie1000QosConfigIngressMapPcpToDei_Type()
)
cie1000QosConfigIngressMapPcpToDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapPcpToDei.setStatus("current")
_Cie1000QosConfigIngressMapPcpToDscp_Type = Dscp
_Cie1000QosConfigIngressMapPcpToDscp_Object = MibTableColumn
cie1000QosConfigIngressMapPcpToDscp = _Cie1000QosConfigIngressMapPcpToDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 3, 1, 8),
    _Cie1000QosConfigIngressMapPcpToDscp_Type()
)
cie1000QosConfigIngressMapPcpToDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapPcpToDscp.setStatus("current")
_Cie1000QosConfigIngressMapPcpToCosid_Type = CIE1000Unsigned8
_Cie1000QosConfigIngressMapPcpToCosid_Object = MibTableColumn
cie1000QosConfigIngressMapPcpToCosid = _Cie1000QosConfigIngressMapPcpToCosid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 3, 1, 9),
    _Cie1000QosConfigIngressMapPcpToCosid_Type()
)
cie1000QosConfigIngressMapPcpToCosid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapPcpToCosid.setStatus("current")
_Cie1000QosConfigIngressMapPcpToPathCosid_Type = CIE1000Unsigned8
_Cie1000QosConfigIngressMapPcpToPathCosid_Object = MibTableColumn
cie1000QosConfigIngressMapPcpToPathCosid = _Cie1000QosConfigIngressMapPcpToPathCosid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 3, 1, 10),
    _Cie1000QosConfigIngressMapPcpToPathCosid_Type()
)
cie1000QosConfigIngressMapPcpToPathCosid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapPcpToPathCosid.setStatus("current")
_Cie1000QosConfigIngressMapDscpTable_Object = MibTable
cie1000QosConfigIngressMapDscpTable = _Cie1000QosConfigIngressMapDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 4)
)
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapDscpTable.setStatus("current")
_Cie1000QosConfigIngressMapDscpEntry_Object = MibTableRow
cie1000QosConfigIngressMapDscpEntry = _Cie1000QosConfigIngressMapDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 4, 1)
)
cie1000QosConfigIngressMapDscpEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigIngressMapDscpIngressMapId"),
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigIngressMapDscpDscp"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapDscpEntry.setStatus("current")


class _Cie1000QosConfigIngressMapDscpIngressMapId_Type(Integer32):
    """Custom type cie1000QosConfigIngressMapDscpIngressMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000QosConfigIngressMapDscpIngressMapId_Type.__name__ = "Integer32"
_Cie1000QosConfigIngressMapDscpIngressMapId_Object = MibTableColumn
cie1000QosConfigIngressMapDscpIngressMapId = _Cie1000QosConfigIngressMapDscpIngressMapId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 4, 1, 1),
    _Cie1000QosConfigIngressMapDscpIngressMapId_Type()
)
cie1000QosConfigIngressMapDscpIngressMapId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapDscpIngressMapId.setStatus("current")
_Cie1000QosConfigIngressMapDscpDscp_Type = Dscp
_Cie1000QosConfigIngressMapDscpDscp_Object = MibTableColumn
cie1000QosConfigIngressMapDscpDscp = _Cie1000QosConfigIngressMapDscpDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 4, 1, 2),
    _Cie1000QosConfigIngressMapDscpDscp_Type()
)
cie1000QosConfigIngressMapDscpDscp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapDscpDscp.setStatus("current")
_Cie1000QosConfigIngressMapDscpToCos_Type = CIE1000Unsigned8
_Cie1000QosConfigIngressMapDscpToCos_Object = MibTableColumn
cie1000QosConfigIngressMapDscpToCos = _Cie1000QosConfigIngressMapDscpToCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 4, 1, 3),
    _Cie1000QosConfigIngressMapDscpToCos_Type()
)
cie1000QosConfigIngressMapDscpToCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapDscpToCos.setStatus("current")
_Cie1000QosConfigIngressMapDscpToDpl_Type = CIE1000Unsigned8
_Cie1000QosConfigIngressMapDscpToDpl_Object = MibTableColumn
cie1000QosConfigIngressMapDscpToDpl = _Cie1000QosConfigIngressMapDscpToDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 4, 1, 4),
    _Cie1000QosConfigIngressMapDscpToDpl_Type()
)
cie1000QosConfigIngressMapDscpToDpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapDscpToDpl.setStatus("current")
_Cie1000QosConfigIngressMapDscpToPcp_Type = CIE1000Unsigned8
_Cie1000QosConfigIngressMapDscpToPcp_Object = MibTableColumn
cie1000QosConfigIngressMapDscpToPcp = _Cie1000QosConfigIngressMapDscpToPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 4, 1, 5),
    _Cie1000QosConfigIngressMapDscpToPcp_Type()
)
cie1000QosConfigIngressMapDscpToPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapDscpToPcp.setStatus("current")
_Cie1000QosConfigIngressMapDscpToDei_Type = CIE1000Unsigned8
_Cie1000QosConfigIngressMapDscpToDei_Object = MibTableColumn
cie1000QosConfigIngressMapDscpToDei = _Cie1000QosConfigIngressMapDscpToDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 4, 1, 6),
    _Cie1000QosConfigIngressMapDscpToDei_Type()
)
cie1000QosConfigIngressMapDscpToDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapDscpToDei.setStatus("current")
_Cie1000QosConfigIngressMapDscpToDscp_Type = Dscp
_Cie1000QosConfigIngressMapDscpToDscp_Object = MibTableColumn
cie1000QosConfigIngressMapDscpToDscp = _Cie1000QosConfigIngressMapDscpToDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 4, 1, 7),
    _Cie1000QosConfigIngressMapDscpToDscp_Type()
)
cie1000QosConfigIngressMapDscpToDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapDscpToDscp.setStatus("current")
_Cie1000QosConfigIngressMapDscpToCosid_Type = CIE1000Unsigned8
_Cie1000QosConfigIngressMapDscpToCosid_Object = MibTableColumn
cie1000QosConfigIngressMapDscpToCosid = _Cie1000QosConfigIngressMapDscpToCosid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 4, 1, 8),
    _Cie1000QosConfigIngressMapDscpToCosid_Type()
)
cie1000QosConfigIngressMapDscpToCosid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapDscpToCosid.setStatus("current")
_Cie1000QosConfigIngressMapDscpToPathCosid_Type = CIE1000Unsigned8
_Cie1000QosConfigIngressMapDscpToPathCosid_Object = MibTableColumn
cie1000QosConfigIngressMapDscpToPathCosid = _Cie1000QosConfigIngressMapDscpToPathCosid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 4, 4, 1, 9),
    _Cie1000QosConfigIngressMapDscpToPathCosid_Type()
)
cie1000QosConfigIngressMapDscpToPathCosid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapDscpToPathCosid.setStatus("current")
_Cie1000QosConfigEgressMap_ObjectIdentity = ObjectIdentity
cie1000QosConfigEgressMap = _Cie1000QosConfigEgressMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5)
)
_Cie1000QosConfigEgressMapTable_Object = MibTable
cie1000QosConfigEgressMapTable = _Cie1000QosConfigEgressMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapTable.setStatus("current")
_Cie1000QosConfigEgressMapEntry_Object = MibTableRow
cie1000QosConfigEgressMapEntry = _Cie1000QosConfigEgressMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 1, 1)
)
cie1000QosConfigEgressMapEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigEgressMapEgressMapId"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapEntry.setStatus("current")


class _Cie1000QosConfigEgressMapEgressMapId_Type(Integer32):
    """Custom type cie1000QosConfigEgressMapEgressMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000QosConfigEgressMapEgressMapId_Type.__name__ = "Integer32"
_Cie1000QosConfigEgressMapEgressMapId_Object = MibTableColumn
cie1000QosConfigEgressMapEgressMapId = _Cie1000QosConfigEgressMapEgressMapId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 1, 1, 1),
    _Cie1000QosConfigEgressMapEgressMapId_Type()
)
cie1000QosConfigEgressMapEgressMapId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapEgressMapId.setStatus("current")
_Cie1000QosConfigEgressMapKey_Type = CIE1000QosEgressMapKey
_Cie1000QosConfigEgressMapKey_Object = MibTableColumn
cie1000QosConfigEgressMapKey = _Cie1000QosConfigEgressMapKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 1, 1, 2),
    _Cie1000QosConfigEgressMapKey_Type()
)
cie1000QosConfigEgressMapKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapKey.setStatus("current")
_Cie1000QosConfigEgressMapActionPcp_Type = TruthValue
_Cie1000QosConfigEgressMapActionPcp_Object = MibTableColumn
cie1000QosConfigEgressMapActionPcp = _Cie1000QosConfigEgressMapActionPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 1, 1, 3),
    _Cie1000QosConfigEgressMapActionPcp_Type()
)
cie1000QosConfigEgressMapActionPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapActionPcp.setStatus("current")
_Cie1000QosConfigEgressMapActionDei_Type = TruthValue
_Cie1000QosConfigEgressMapActionDei_Object = MibTableColumn
cie1000QosConfigEgressMapActionDei = _Cie1000QosConfigEgressMapActionDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 1, 1, 4),
    _Cie1000QosConfigEgressMapActionDei_Type()
)
cie1000QosConfigEgressMapActionDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapActionDei.setStatus("current")
_Cie1000QosConfigEgressMapActionDscp_Type = TruthValue
_Cie1000QosConfigEgressMapActionDscp_Object = MibTableColumn
cie1000QosConfigEgressMapActionDscp = _Cie1000QosConfigEgressMapActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 1, 1, 5),
    _Cie1000QosConfigEgressMapActionDscp_Type()
)
cie1000QosConfigEgressMapActionDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapActionDscp.setStatus("current")
_Cie1000QosConfigEgressMapActionPath_Type = TruthValue
_Cie1000QosConfigEgressMapActionPath_Object = MibTableColumn
cie1000QosConfigEgressMapActionPath = _Cie1000QosConfigEgressMapActionPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 1, 1, 6),
    _Cie1000QosConfigEgressMapActionPath_Type()
)
cie1000QosConfigEgressMapActionPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapActionPath.setStatus("current")
_Cie1000QosConfigEgressMapAction_Type = CIE1000RowEditorState
_Cie1000QosConfigEgressMapAction_Object = MibTableColumn
cie1000QosConfigEgressMapAction = _Cie1000QosConfigEgressMapAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 1, 1, 10000),
    _Cie1000QosConfigEgressMapAction_Type()
)
cie1000QosConfigEgressMapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapAction.setStatus("current")
_Cie1000QosConfigEgressMapTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000QosConfigEgressMapTableRowEditor = _Cie1000QosConfigEgressMapTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 2)
)


class _Cie1000QosConfigEgressMapTableRowEditorEgressMapId_Type(Integer32):
    """Custom type cie1000QosConfigEgressMapTableRowEditorEgressMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000QosConfigEgressMapTableRowEditorEgressMapId_Type.__name__ = "Integer32"
_Cie1000QosConfigEgressMapTableRowEditorEgressMapId_Object = MibScalar
cie1000QosConfigEgressMapTableRowEditorEgressMapId = _Cie1000QosConfigEgressMapTableRowEditorEgressMapId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 2, 1),
    _Cie1000QosConfigEgressMapTableRowEditorEgressMapId_Type()
)
cie1000QosConfigEgressMapTableRowEditorEgressMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapTableRowEditorEgressMapId.setStatus("current")
_Cie1000QosConfigEgressMapTableRowEditorKey_Type = CIE1000QosEgressMapKey
_Cie1000QosConfigEgressMapTableRowEditorKey_Object = MibScalar
cie1000QosConfigEgressMapTableRowEditorKey = _Cie1000QosConfigEgressMapTableRowEditorKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 2, 2),
    _Cie1000QosConfigEgressMapTableRowEditorKey_Type()
)
cie1000QosConfigEgressMapTableRowEditorKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapTableRowEditorKey.setStatus("current")
_Cie1000QosConfigEgressMapTableRowEditorActionPcp_Type = TruthValue
_Cie1000QosConfigEgressMapTableRowEditorActionPcp_Object = MibScalar
cie1000QosConfigEgressMapTableRowEditorActionPcp = _Cie1000QosConfigEgressMapTableRowEditorActionPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 2, 3),
    _Cie1000QosConfigEgressMapTableRowEditorActionPcp_Type()
)
cie1000QosConfigEgressMapTableRowEditorActionPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapTableRowEditorActionPcp.setStatus("current")
_Cie1000QosConfigEgressMapTableRowEditorActionDei_Type = TruthValue
_Cie1000QosConfigEgressMapTableRowEditorActionDei_Object = MibScalar
cie1000QosConfigEgressMapTableRowEditorActionDei = _Cie1000QosConfigEgressMapTableRowEditorActionDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 2, 4),
    _Cie1000QosConfigEgressMapTableRowEditorActionDei_Type()
)
cie1000QosConfigEgressMapTableRowEditorActionDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapTableRowEditorActionDei.setStatus("current")
_Cie1000QosConfigEgressMapTableRowEditorActionDscp_Type = TruthValue
_Cie1000QosConfigEgressMapTableRowEditorActionDscp_Object = MibScalar
cie1000QosConfigEgressMapTableRowEditorActionDscp = _Cie1000QosConfigEgressMapTableRowEditorActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 2, 5),
    _Cie1000QosConfigEgressMapTableRowEditorActionDscp_Type()
)
cie1000QosConfigEgressMapTableRowEditorActionDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapTableRowEditorActionDscp.setStatus("current")
_Cie1000QosConfigEgressMapTableRowEditorActionPath_Type = TruthValue
_Cie1000QosConfigEgressMapTableRowEditorActionPath_Object = MibScalar
cie1000QosConfigEgressMapTableRowEditorActionPath = _Cie1000QosConfigEgressMapTableRowEditorActionPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 2, 6),
    _Cie1000QosConfigEgressMapTableRowEditorActionPath_Type()
)
cie1000QosConfigEgressMapTableRowEditorActionPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapTableRowEditorActionPath.setStatus("current")
_Cie1000QosConfigEgressMapTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000QosConfigEgressMapTableRowEditorAction_Object = MibScalar
cie1000QosConfigEgressMapTableRowEditorAction = _Cie1000QosConfigEgressMapTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 2, 10000),
    _Cie1000QosConfigEgressMapTableRowEditorAction_Type()
)
cie1000QosConfigEgressMapTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapTableRowEditorAction.setStatus("current")
_Cie1000QosConfigEgressMapCosidTable_Object = MibTable
cie1000QosConfigEgressMapCosidTable = _Cie1000QosConfigEgressMapCosidTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapCosidTable.setStatus("current")
_Cie1000QosConfigEgressMapCosidEntry_Object = MibTableRow
cie1000QosConfigEgressMapCosidEntry = _Cie1000QosConfigEgressMapCosidEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 3, 1)
)
cie1000QosConfigEgressMapCosidEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigEgressMapCosidEgressMapId"),
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigEgressMapCosidCosid"),
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigEgressMapCosidDpl"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapCosidEntry.setStatus("current")


class _Cie1000QosConfigEgressMapCosidEgressMapId_Type(Integer32):
    """Custom type cie1000QosConfigEgressMapCosidEgressMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000QosConfigEgressMapCosidEgressMapId_Type.__name__ = "Integer32"
_Cie1000QosConfigEgressMapCosidEgressMapId_Object = MibTableColumn
cie1000QosConfigEgressMapCosidEgressMapId = _Cie1000QosConfigEgressMapCosidEgressMapId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 3, 1, 1),
    _Cie1000QosConfigEgressMapCosidEgressMapId_Type()
)
cie1000QosConfigEgressMapCosidEgressMapId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapCosidEgressMapId.setStatus("current")


class _Cie1000QosConfigEgressMapCosidCosid_Type(Integer32):
    """Custom type cie1000QosConfigEgressMapCosidCosid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cie1000QosConfigEgressMapCosidCosid_Type.__name__ = "Integer32"
_Cie1000QosConfigEgressMapCosidCosid_Object = MibTableColumn
cie1000QosConfigEgressMapCosidCosid = _Cie1000QosConfigEgressMapCosidCosid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 3, 1, 2),
    _Cie1000QosConfigEgressMapCosidCosid_Type()
)
cie1000QosConfigEgressMapCosidCosid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapCosidCosid.setStatus("current")


class _Cie1000QosConfigEgressMapCosidDpl_Type(Integer32):
    """Custom type cie1000QosConfigEgressMapCosidDpl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Cie1000QosConfigEgressMapCosidDpl_Type.__name__ = "Integer32"
_Cie1000QosConfigEgressMapCosidDpl_Object = MibTableColumn
cie1000QosConfigEgressMapCosidDpl = _Cie1000QosConfigEgressMapCosidDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 3, 1, 3),
    _Cie1000QosConfigEgressMapCosidDpl_Type()
)
cie1000QosConfigEgressMapCosidDpl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapCosidDpl.setStatus("current")
_Cie1000QosConfigEgressMapCosidToPcp_Type = CIE1000Unsigned8
_Cie1000QosConfigEgressMapCosidToPcp_Object = MibTableColumn
cie1000QosConfigEgressMapCosidToPcp = _Cie1000QosConfigEgressMapCosidToPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 3, 1, 4),
    _Cie1000QosConfigEgressMapCosidToPcp_Type()
)
cie1000QosConfigEgressMapCosidToPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapCosidToPcp.setStatus("current")
_Cie1000QosConfigEgressMapCosidToDei_Type = CIE1000Unsigned8
_Cie1000QosConfigEgressMapCosidToDei_Object = MibTableColumn
cie1000QosConfigEgressMapCosidToDei = _Cie1000QosConfigEgressMapCosidToDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 3, 1, 5),
    _Cie1000QosConfigEgressMapCosidToDei_Type()
)
cie1000QosConfigEgressMapCosidToDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapCosidToDei.setStatus("current")
_Cie1000QosConfigEgressMapCosidToDscp_Type = Dscp
_Cie1000QosConfigEgressMapCosidToDscp_Object = MibTableColumn
cie1000QosConfigEgressMapCosidToDscp = _Cie1000QosConfigEgressMapCosidToDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 3, 1, 6),
    _Cie1000QosConfigEgressMapCosidToDscp_Type()
)
cie1000QosConfigEgressMapCosidToDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapCosidToDscp.setStatus("current")
_Cie1000QosConfigEgressMapCosidToPathCosid_Type = CIE1000Unsigned8
_Cie1000QosConfigEgressMapCosidToPathCosid_Object = MibTableColumn
cie1000QosConfigEgressMapCosidToPathCosid = _Cie1000QosConfigEgressMapCosidToPathCosid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 3, 1, 7),
    _Cie1000QosConfigEgressMapCosidToPathCosid_Type()
)
cie1000QosConfigEgressMapCosidToPathCosid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapCosidToPathCosid.setStatus("current")
_Cie1000QosConfigEgressMapDscpTable_Object = MibTable
cie1000QosConfigEgressMapDscpTable = _Cie1000QosConfigEgressMapDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 4)
)
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapDscpTable.setStatus("current")
_Cie1000QosConfigEgressMapDscpEntry_Object = MibTableRow
cie1000QosConfigEgressMapDscpEntry = _Cie1000QosConfigEgressMapDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 4, 1)
)
cie1000QosConfigEgressMapDscpEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigEgressMapDscpEgressMapId"),
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigEgressMapDscpDscp"),
    (0, "CIE1000-QOS-MIB", "cie1000QosConfigEgressMapDscpDpl"),
)
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapDscpEntry.setStatus("current")


class _Cie1000QosConfigEgressMapDscpEgressMapId_Type(Integer32):
    """Custom type cie1000QosConfigEgressMapDscpEgressMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000QosConfigEgressMapDscpEgressMapId_Type.__name__ = "Integer32"
_Cie1000QosConfigEgressMapDscpEgressMapId_Object = MibTableColumn
cie1000QosConfigEgressMapDscpEgressMapId = _Cie1000QosConfigEgressMapDscpEgressMapId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 4, 1, 1),
    _Cie1000QosConfigEgressMapDscpEgressMapId_Type()
)
cie1000QosConfigEgressMapDscpEgressMapId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapDscpEgressMapId.setStatus("current")
_Cie1000QosConfigEgressMapDscpDscp_Type = Dscp
_Cie1000QosConfigEgressMapDscpDscp_Object = MibTableColumn
cie1000QosConfigEgressMapDscpDscp = _Cie1000QosConfigEgressMapDscpDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 4, 1, 2),
    _Cie1000QosConfigEgressMapDscpDscp_Type()
)
cie1000QosConfigEgressMapDscpDscp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapDscpDscp.setStatus("current")


class _Cie1000QosConfigEgressMapDscpDpl_Type(Integer32):
    """Custom type cie1000QosConfigEgressMapDscpDpl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Cie1000QosConfigEgressMapDscpDpl_Type.__name__ = "Integer32"
_Cie1000QosConfigEgressMapDscpDpl_Object = MibTableColumn
cie1000QosConfigEgressMapDscpDpl = _Cie1000QosConfigEgressMapDscpDpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 4, 1, 3),
    _Cie1000QosConfigEgressMapDscpDpl_Type()
)
cie1000QosConfigEgressMapDscpDpl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapDscpDpl.setStatus("current")
_Cie1000QosConfigEgressMapDscpToPcp_Type = CIE1000Unsigned8
_Cie1000QosConfigEgressMapDscpToPcp_Object = MibTableColumn
cie1000QosConfigEgressMapDscpToPcp = _Cie1000QosConfigEgressMapDscpToPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 4, 1, 4),
    _Cie1000QosConfigEgressMapDscpToPcp_Type()
)
cie1000QosConfigEgressMapDscpToPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapDscpToPcp.setStatus("current")
_Cie1000QosConfigEgressMapDscpToDei_Type = CIE1000Unsigned8
_Cie1000QosConfigEgressMapDscpToDei_Object = MibTableColumn
cie1000QosConfigEgressMapDscpToDei = _Cie1000QosConfigEgressMapDscpToDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 4, 1, 5),
    _Cie1000QosConfigEgressMapDscpToDei_Type()
)
cie1000QosConfigEgressMapDscpToDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapDscpToDei.setStatus("current")
_Cie1000QosConfigEgressMapDscpToDscp_Type = Dscp
_Cie1000QosConfigEgressMapDscpToDscp_Object = MibTableColumn
cie1000QosConfigEgressMapDscpToDscp = _Cie1000QosConfigEgressMapDscpToDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 4, 1, 6),
    _Cie1000QosConfigEgressMapDscpToDscp_Type()
)
cie1000QosConfigEgressMapDscpToDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapDscpToDscp.setStatus("current")
_Cie1000QosConfigEgressMapDscpToPathCosid_Type = CIE1000Unsigned8
_Cie1000QosConfigEgressMapDscpToPathCosid_Object = MibTableColumn
cie1000QosConfigEgressMapDscpToPathCosid = _Cie1000QosConfigEgressMapDscpToPathCosid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 2, 5, 4, 1, 7),
    _Cie1000QosConfigEgressMapDscpToPathCosid_Type()
)
cie1000QosConfigEgressMapDscpToPathCosid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapDscpToPathCosid.setStatus("current")
_Cie1000QosStatus_ObjectIdentity = ObjectIdentity
cie1000QosStatus = _Cie1000QosStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3)
)
_Cie1000QosStatusInterface_ObjectIdentity = ObjectIdentity
cie1000QosStatusInterface = _Cie1000QosStatusInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2)
)
_Cie1000QosStatusInterfaceTable_Object = MibTable
cie1000QosStatusInterfaceTable = _Cie1000QosStatusInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceTable.setStatus("current")
_Cie1000QosStatusInterfaceEntry_Object = MibTableRow
cie1000QosStatusInterfaceEntry = _Cie1000QosStatusInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 1, 1)
)
cie1000QosStatusInterfaceEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosStatusInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceEntry.setStatus("current")
_Cie1000QosStatusInterfaceIfIndex_Type = CIE1000InterfaceIndex
_Cie1000QosStatusInterfaceIfIndex_Object = MibTableColumn
cie1000QosStatusInterfaceIfIndex = _Cie1000QosStatusInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 1, 1, 1),
    _Cie1000QosStatusInterfaceIfIndex_Type()
)
cie1000QosStatusInterfaceIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceIfIndex.setStatus("current")
_Cie1000QosStatusInterfaceCos_Type = Unsigned32
_Cie1000QosStatusInterfaceCos_Object = MibTableColumn
cie1000QosStatusInterfaceCos = _Cie1000QosStatusInterfaceCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 1, 1, 2),
    _Cie1000QosStatusInterfaceCos_Type()
)
cie1000QosStatusInterfaceCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceCos.setStatus("current")
_Cie1000QosStatusInterfaceSchedulerTable_Object = MibTable
cie1000QosStatusInterfaceSchedulerTable = _Cie1000QosStatusInterfaceSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceSchedulerTable.setStatus("current")
_Cie1000QosStatusInterfaceSchedulerEntry_Object = MibTableRow
cie1000QosStatusInterfaceSchedulerEntry = _Cie1000QosStatusInterfaceSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 2, 1)
)
cie1000QosStatusInterfaceSchedulerEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosStatusInterfaceSchedulerIfIndex"),
    (0, "CIE1000-QOS-MIB", "cie1000QosStatusInterfaceSchedulerQueue"),
)
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceSchedulerEntry.setStatus("current")
_Cie1000QosStatusInterfaceSchedulerIfIndex_Type = CIE1000InterfaceIndex
_Cie1000QosStatusInterfaceSchedulerIfIndex_Object = MibTableColumn
cie1000QosStatusInterfaceSchedulerIfIndex = _Cie1000QosStatusInterfaceSchedulerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 2, 1, 1),
    _Cie1000QosStatusInterfaceSchedulerIfIndex_Type()
)
cie1000QosStatusInterfaceSchedulerIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceSchedulerIfIndex.setStatus("current")


class _Cie1000QosStatusInterfaceSchedulerQueue_Type(Integer32):
    """Custom type cie1000QosStatusInterfaceSchedulerQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cie1000QosStatusInterfaceSchedulerQueue_Type.__name__ = "Integer32"
_Cie1000QosStatusInterfaceSchedulerQueue_Object = MibTableColumn
cie1000QosStatusInterfaceSchedulerQueue = _Cie1000QosStatusInterfaceSchedulerQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 2, 1, 2),
    _Cie1000QosStatusInterfaceSchedulerQueue_Type()
)
cie1000QosStatusInterfaceSchedulerQueue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceSchedulerQueue.setStatus("current")
_Cie1000QosStatusInterfaceSchedulerWeight_Type = CIE1000Percent
_Cie1000QosStatusInterfaceSchedulerWeight_Object = MibTableColumn
cie1000QosStatusInterfaceSchedulerWeight = _Cie1000QosStatusInterfaceSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 2, 1, 3),
    _Cie1000QosStatusInterfaceSchedulerWeight_Type()
)
cie1000QosStatusInterfaceSchedulerWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceSchedulerWeight.setStatus("current")
_Cie1000QosStatusInterfaceSchedulerCutThrough_Type = TruthValue
_Cie1000QosStatusInterfaceSchedulerCutThrough_Object = MibTableColumn
cie1000QosStatusInterfaceSchedulerCutThrough = _Cie1000QosStatusInterfaceSchedulerCutThrough_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 2, 1, 4),
    _Cie1000QosStatusInterfaceSchedulerCutThrough_Type()
)
cie1000QosStatusInterfaceSchedulerCutThrough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceSchedulerCutThrough.setStatus("current")
_Cie1000QosStatusInterfaceQbvGclOprTable_Object = MibTable
cie1000QosStatusInterfaceQbvGclOprTable = _Cie1000QosStatusInterfaceQbvGclOprTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvGclOprTable.setStatus("current")
_Cie1000QosStatusInterfaceQbvGclOprEntry_Object = MibTableRow
cie1000QosStatusInterfaceQbvGclOprEntry = _Cie1000QosStatusInterfaceQbvGclOprEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 3, 1)
)
cie1000QosStatusInterfaceQbvGclOprEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvGclOprIfIndex"),
    (0, "CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvGclOprGclIndex"),
)
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvGclOprEntry.setStatus("current")
_Cie1000QosStatusInterfaceQbvGclOprIfIndex_Type = CIE1000InterfaceIndex
_Cie1000QosStatusInterfaceQbvGclOprIfIndex_Object = MibTableColumn
cie1000QosStatusInterfaceQbvGclOprIfIndex = _Cie1000QosStatusInterfaceQbvGclOprIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 3, 1, 1),
    _Cie1000QosStatusInterfaceQbvGclOprIfIndex_Type()
)
cie1000QosStatusInterfaceQbvGclOprIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvGclOprIfIndex.setStatus("current")


class _Cie1000QosStatusInterfaceQbvGclOprGclIndex_Type(Integer32):
    """Custom type cie1000QosStatusInterfaceQbvGclOprGclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Cie1000QosStatusInterfaceQbvGclOprGclIndex_Type.__name__ = "Integer32"
_Cie1000QosStatusInterfaceQbvGclOprGclIndex_Object = MibTableColumn
cie1000QosStatusInterfaceQbvGclOprGclIndex = _Cie1000QosStatusInterfaceQbvGclOprGclIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 3, 1, 2),
    _Cie1000QosStatusInterfaceQbvGclOprGclIndex_Type()
)
cie1000QosStatusInterfaceQbvGclOprGclIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvGclOprGclIndex.setStatus("current")


class _Cie1000QosStatusInterfaceQbvGclOprGateState_Type(OctetString):
    """Custom type cie1000QosStatusInterfaceQbvGclOprGateState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_Cie1000QosStatusInterfaceQbvGclOprGateState_Type.__name__ = "OctetString"
_Cie1000QosStatusInterfaceQbvGclOprGateState_Object = MibTableColumn
cie1000QosStatusInterfaceQbvGclOprGateState = _Cie1000QosStatusInterfaceQbvGclOprGateState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 3, 1, 3),
    _Cie1000QosStatusInterfaceQbvGclOprGateState_Type()
)
cie1000QosStatusInterfaceQbvGclOprGateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvGclOprGateState.setStatus("current")
_Cie1000QosStatusInterfaceQbvGclOprTimeInterval_Type = Unsigned32
_Cie1000QosStatusInterfaceQbvGclOprTimeInterval_Object = MibTableColumn
cie1000QosStatusInterfaceQbvGclOprTimeInterval = _Cie1000QosStatusInterfaceQbvGclOprTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 3, 1, 4),
    _Cie1000QosStatusInterfaceQbvGclOprTimeInterval_Type()
)
cie1000QosStatusInterfaceQbvGclOprTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvGclOprTimeInterval.setStatus("current")
_Cie1000QosStatusInterfaceQbvOprStatusTable_Object = MibTable
cie1000QosStatusInterfaceQbvOprStatusTable = _Cie1000QosStatusInterfaceQbvOprStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvOprStatusTable.setStatus("current")
_Cie1000QosStatusInterfaceQbvOprStatusEntry_Object = MibTableRow
cie1000QosStatusInterfaceQbvOprStatusEntry = _Cie1000QosStatusInterfaceQbvOprStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 4, 1)
)
cie1000QosStatusInterfaceQbvOprStatusEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvOprStatusIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvOprStatusEntry.setStatus("current")
_Cie1000QosStatusInterfaceQbvOprStatusIfIndex_Type = CIE1000InterfaceIndex
_Cie1000QosStatusInterfaceQbvOprStatusIfIndex_Object = MibTableColumn
cie1000QosStatusInterfaceQbvOprStatusIfIndex = _Cie1000QosStatusInterfaceQbvOprStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 4, 1, 1),
    _Cie1000QosStatusInterfaceQbvOprStatusIfIndex_Type()
)
cie1000QosStatusInterfaceQbvOprStatusIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvOprStatusIfIndex.setStatus("current")


class _Cie1000QosStatusInterfaceQbvOprStatusOperGateStates_Type(OctetString):
    """Custom type cie1000QosStatusInterfaceQbvOprStatusOperGateStates based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_Cie1000QosStatusInterfaceQbvOprStatusOperGateStates_Type.__name__ = "OctetString"
_Cie1000QosStatusInterfaceQbvOprStatusOperGateStates_Object = MibTableColumn
cie1000QosStatusInterfaceQbvOprStatusOperGateStates = _Cie1000QosStatusInterfaceQbvOprStatusOperGateStates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 4, 1, 2),
    _Cie1000QosStatusInterfaceQbvOprStatusOperGateStates_Type()
)
cie1000QosStatusInterfaceQbvOprStatusOperGateStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvOprStatusOperGateStates.setStatus("current")
_Cie1000QosStatusInterfaceQbvOprStatusOperControlListLength_Type = Unsigned32
_Cie1000QosStatusInterfaceQbvOprStatusOperControlListLength_Object = MibTableColumn
cie1000QosStatusInterfaceQbvOprStatusOperControlListLength = _Cie1000QosStatusInterfaceQbvOprStatusOperControlListLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 4, 1, 3),
    _Cie1000QosStatusInterfaceQbvOprStatusOperControlListLength_Type()
)
cie1000QosStatusInterfaceQbvOprStatusOperControlListLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvOprStatusOperControlListLength.setStatus("current")
_Cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeNumerator_Type = Unsigned32
_Cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeNumerator_Object = MibTableColumn
cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeNumerator = _Cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeNumerator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 4, 1, 4),
    _Cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeNumerator_Type()
)
cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeNumerator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeNumerator.setStatus("current")
_Cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeDenominator_Type = Unsigned32
_Cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeDenominator_Object = MibTableColumn
cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeDenominator = _Cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeDenominator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 4, 1, 5),
    _Cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeDenominator_Type()
)
cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeDenominator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeDenominator.setStatus("current")
_Cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeExtension_Type = Unsigned32
_Cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeExtension_Object = MibTableColumn
cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeExtension = _Cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeExtension_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 4, 1, 6),
    _Cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeExtension_Type()
)
cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeExtension.setStatus("current")
_Cie1000QosStatusInterfaceQbvOprStatusOperBaseTime_Type = IEEE8021STPTPtimeValue
_Cie1000QosStatusInterfaceQbvOprStatusOperBaseTime_Object = MibTableColumn
cie1000QosStatusInterfaceQbvOprStatusOperBaseTime = _Cie1000QosStatusInterfaceQbvOprStatusOperBaseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 4, 1, 7),
    _Cie1000QosStatusInterfaceQbvOprStatusOperBaseTime_Type()
)
cie1000QosStatusInterfaceQbvOprStatusOperBaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvOprStatusOperBaseTime.setStatus("current")
_Cie1000QosStatusInterfaceQbvOprStatusConfigChangeTime_Type = IEEE8021STPTPtimeValue
_Cie1000QosStatusInterfaceQbvOprStatusConfigChangeTime_Object = MibTableColumn
cie1000QosStatusInterfaceQbvOprStatusConfigChangeTime = _Cie1000QosStatusInterfaceQbvOprStatusConfigChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 4, 1, 8),
    _Cie1000QosStatusInterfaceQbvOprStatusConfigChangeTime_Type()
)
cie1000QosStatusInterfaceQbvOprStatusConfigChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvOprStatusConfigChangeTime.setStatus("current")
_Cie1000QosStatusInterfaceQbvOprStatusTickGranularity_Type = Unsigned32
_Cie1000QosStatusInterfaceQbvOprStatusTickGranularity_Object = MibTableColumn
cie1000QosStatusInterfaceQbvOprStatusTickGranularity = _Cie1000QosStatusInterfaceQbvOprStatusTickGranularity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 4, 1, 9),
    _Cie1000QosStatusInterfaceQbvOprStatusTickGranularity_Type()
)
cie1000QosStatusInterfaceQbvOprStatusTickGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvOprStatusTickGranularity.setStatus("current")
_Cie1000QosStatusInterfaceQbvOprStatusCurrentTime_Type = IEEE8021STPTPtimeValue
_Cie1000QosStatusInterfaceQbvOprStatusCurrentTime_Object = MibTableColumn
cie1000QosStatusInterfaceQbvOprStatusCurrentTime = _Cie1000QosStatusInterfaceQbvOprStatusCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 4, 1, 10),
    _Cie1000QosStatusInterfaceQbvOprStatusCurrentTime_Type()
)
cie1000QosStatusInterfaceQbvOprStatusCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvOprStatusCurrentTime.setStatus("current")
_Cie1000QosStatusInterfaceQbvOprStatusConfigPending_Type = TruthValue
_Cie1000QosStatusInterfaceQbvOprStatusConfigPending_Object = MibTableColumn
cie1000QosStatusInterfaceQbvOprStatusConfigPending = _Cie1000QosStatusInterfaceQbvOprStatusConfigPending_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 4, 1, 11),
    _Cie1000QosStatusInterfaceQbvOprStatusConfigPending_Type()
)
cie1000QosStatusInterfaceQbvOprStatusConfigPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvOprStatusConfigPending.setStatus("current")
_Cie1000QosStatusInterfaceQbvOprStatusConfigChangeError_Type = Counter64
_Cie1000QosStatusInterfaceQbvOprStatusConfigChangeError_Object = MibTableColumn
cie1000QosStatusInterfaceQbvOprStatusConfigChangeError = _Cie1000QosStatusInterfaceQbvOprStatusConfigChangeError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 4, 1, 12),
    _Cie1000QosStatusInterfaceQbvOprStatusConfigChangeError_Type()
)
cie1000QosStatusInterfaceQbvOprStatusConfigChangeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvOprStatusConfigChangeError.setStatus("current")
_Cie1000QosStatusInterfaceQbvOprStatusSupportedListMax_Type = Unsigned32
_Cie1000QosStatusInterfaceQbvOprStatusSupportedListMax_Object = MibTableColumn
cie1000QosStatusInterfaceQbvOprStatusSupportedListMax = _Cie1000QosStatusInterfaceQbvOprStatusSupportedListMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 2, 4, 1, 13),
    _Cie1000QosStatusInterfaceQbvOprStatusSupportedListMax_Type()
)
cie1000QosStatusInterfaceQbvOprStatusSupportedListMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvOprStatusSupportedListMax.setStatus("current")
_Cie1000QosStatusQce_ObjectIdentity = ObjectIdentity
cie1000QosStatusQce = _Cie1000QosStatusQce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 3)
)
_Cie1000QosStatusQceTable_Object = MibTable
cie1000QosStatusQceTable = _Cie1000QosStatusQceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cie1000QosStatusQceTable.setStatus("current")
_Cie1000QosStatusQceEntry_Object = MibTableRow
cie1000QosStatusQceEntry = _Cie1000QosStatusQceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 3, 1, 1)
)
cie1000QosStatusQceEntry.setIndexNames(
    (0, "CIE1000-QOS-MIB", "cie1000QosStatusQceSwitchId"),
    (0, "CIE1000-QOS-MIB", "cie1000QosStatusQceIndex"),
)
if mibBuilder.loadTexts:
    cie1000QosStatusQceEntry.setStatus("current")
_Cie1000QosStatusQceSwitchId_Type = Unsigned32
_Cie1000QosStatusQceSwitchId_Object = MibTableColumn
cie1000QosStatusQceSwitchId = _Cie1000QosStatusQceSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 3, 1, 1, 1),
    _Cie1000QosStatusQceSwitchId_Type()
)
cie1000QosStatusQceSwitchId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosStatusQceSwitchId.setStatus("current")


class _Cie1000QosStatusQceIndex_Type(Integer32):
    """Custom type cie1000QosStatusQceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000QosStatusQceIndex_Type.__name__ = "Integer32"
_Cie1000QosStatusQceIndex_Object = MibTableColumn
cie1000QosStatusQceIndex = _Cie1000QosStatusQceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 3, 1, 1, 2),
    _Cie1000QosStatusQceIndex_Type()
)
cie1000QosStatusQceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000QosStatusQceIndex.setStatus("current")
_Cie1000QosStatusQceUserId_Type = CIE1000QosQceUserType
_Cie1000QosStatusQceUserId_Object = MibTableColumn
cie1000QosStatusQceUserId = _Cie1000QosStatusQceUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 3, 1, 1, 3),
    _Cie1000QosStatusQceUserId_Type()
)
cie1000QosStatusQceUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusQceUserId.setStatus("current")
_Cie1000QosStatusQceQceId_Type = Unsigned32
_Cie1000QosStatusQceQceId_Object = MibTableColumn
cie1000QosStatusQceQceId = _Cie1000QosStatusQceQceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 3, 1, 1, 4),
    _Cie1000QosStatusQceQceId_Type()
)
cie1000QosStatusQceQceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusQceQceId.setStatus("current")
_Cie1000QosStatusQceConflict_Type = TruthValue
_Cie1000QosStatusQceConflict_Object = MibTableColumn
cie1000QosStatusQceConflict = _Cie1000QosStatusQceConflict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 3, 3, 1, 1, 100),
    _Cie1000QosStatusQceConflict_Type()
)
cie1000QosStatusQceConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000QosStatusQceConflict.setStatus("current")
_Cie1000QosControl_ObjectIdentity = ObjectIdentity
cie1000QosControl = _Cie1000QosControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 4)
)
_Cie1000QosControlQce_ObjectIdentity = ObjectIdentity
cie1000QosControlQce = _Cie1000QosControlQce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 4, 3)
)
_Cie1000QosControlQceConflictResolve_Type = TruthValue
_Cie1000QosControlQceConflictResolve_Object = MibScalar
cie1000QosControlQceConflictResolve = _Cie1000QosControlQceConflictResolve_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 1, 4, 3, 1),
    _Cie1000QosControlQceConflictResolve_Type()
)
cie1000QosControlQceConflictResolve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000QosControlQceConflictResolve.setStatus("current")
_Cie1000QosMibConformance_ObjectIdentity = ObjectIdentity
cie1000QosMibConformance = _Cie1000QosMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2)
)
_Cie1000QosMibCompliances_ObjectIdentity = ObjectIdentity
cie1000QosMibCompliances = _Cie1000QosMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 1)
)
_Cie1000QosMibGroups_ObjectIdentity = ObjectIdentity
cie1000QosMibGroups = _Cie1000QosMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2)
)

# Managed Objects groups

cie1000QosCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 1)
)
cie1000QosCapabilitiesInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosCapabilitiesClassMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesClassMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesDplMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesDplMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesWredGroupMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesWredGroupMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesWredDplMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesWredDplMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQceIdMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQceIdMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortPolicerBitRateMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortPolicerBitRateMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortPolicerBitBurstMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortPolicerBitBurstMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortPolicerFrameRateMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortPolicerFrameRateMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortPolicerFrameBurstMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortPolicerFrameBurstMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQueuePolicerBitRateMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQueuePolicerBitRateMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQueuePolicerBitBurstMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQueuePolicerBitBurstMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQueuePolicerFrameRateMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQueuePolicerFrameRateMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQueuePolicerFrameBurstMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQueuePolicerFrameBurstMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortShaperBitRateMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortShaperBitRateMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortShaperBitBurstMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortShaperBitBurstMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortShaperFrameRateMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortShaperFrameRateMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortShaperFrameBurstMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortShaperFrameBurstMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQueueShaperBitRateMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQueueShaperBitRateMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQueueShaperBitBurstMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQueueShaperBitBurstMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQueueShaperFrameRateMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQueueShaperFrameRateMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQueueShaperFrameBurstMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQueueShaperFrameBurstMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesGlobalStormBitRateMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesGlobalStormBitRateMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesGlobalStormBitBurstMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesGlobalStormBitBurstMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesGlobalStormFrameRateMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesGlobalStormFrameRateMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesGlobalStormFrameBurstMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesGlobalStormFrameBurstMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortStormBitRateMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortStormBitRateMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortStormBitBurstMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortStormBitBurstMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortStormFrameRateMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortStormFrameRateMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortStormFrameBurstMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesPortStormFrameBurstMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesIngressMapIdMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesIngressMapIdMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesEgressMapIdMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesEgressMapIdMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesCosIdMin"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesCosIdMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesQbvGclLenMax"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesDwrrCountMask"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasGlobalStormPolicers"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasPortStormPolicers"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasPortQueuePolicers"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasWredV1"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasWredV2"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasFixedTagCosMap"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasTagClassification"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasTagRemarking"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasDscp"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasDscpDplClassification"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasDscpDplRemarking"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasPortPolicersFc"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasQueuePolicersFc"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasPortShapersDlb"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasQueueShapersDlb"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasQueueShapersExcess"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasWredV3"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasQueueShapersCredit"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasQueueCutThrough"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasQce"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasQceAddressMode"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasQceKeyType"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasQceMacOui"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasQceDmac"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasQceDip"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasQceCTag"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasQceSTag"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasQceInnerTag"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasQceActionPcpDei"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasQceActionPolicy"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasShapersRt"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasQceActionMap"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasIngressMap"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasEgressMap"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasWred2orWredw3"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasDscpDp2"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasDscpDp3"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasDefaultPcpAndDei"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasTrustTag"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasCosIdClassification"),
        ("CIE1000-QOS-MIB", "cie1000QosCapabilitiesHasQbv"))
)
if mibBuilder.loadTexts:
    cie1000QosCapabilitiesInfoGroup.setStatus("current")

cie1000QosConfigGlobalsStormPolicersUnicastInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 2)
)
cie1000QosConfigGlobalsStormPolicersUnicastInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsStormPolicersUnicastEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsStormPolicersUnicastRate"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsStormPolicersUnicastFrameRate"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsStormPolicersUnicastInfoGroup.setStatus("current")

cie1000QosConfigGlobalsStormPolicersMulticastInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 3)
)
cie1000QosConfigGlobalsStormPolicersMulticastInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsStormPolicersMulticastEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsStormPolicersMulticastRate"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsStormPolicersMulticastFrameRate"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsStormPolicersMulticastInfoGroup.setStatus("current")

cie1000QosConfigGlobalsStormPolicersBroadcastInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 4)
)
cie1000QosConfigGlobalsStormPolicersBroadcastInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsStormPolicersBroadcastEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsStormPolicersBroadcastRate"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsStormPolicersBroadcastFrameRate"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsStormPolicersBroadcastInfoGroup.setStatus("current")

cie1000QosConfigGlobalsWredTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 5)
)
cie1000QosConfigGlobalsWredTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsWredGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsWredQueue"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsWredDpl"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsWredEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsWredMinimumFillLevel"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsWredMaximum"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsWredMaxSelector"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsWredMaximumDp1"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsWredMaximumDp2"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsWredMaximumDp3"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsWredTableInfoGroup.setStatus("current")

cie1000QosConfigGlobalsDscpTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 6)
)
cie1000QosConfigGlobalsDscpTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsDscpDscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsDscpTrust"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsDscpCos"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsDscpDpl"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsDscpIngressTranslation"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsDscpClassify"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsDscpEgressTranslation"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsDscpEgressTranslationDp1"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsDscpTableInfoGroup.setStatus("current")

cie1000QosConfigGlobalsCosToDscpTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 7)
)
cie1000QosConfigGlobalsCosToDscpTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsCosToDscpCos"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsCosToDscpDscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsCosToDscpDscpDp1"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsCosToDscpDscpDp2"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsCosToDscpDscpDp3"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigGlobalsCosToDscpTableInfoGroup.setStatus("current")

cie1000QosConfigInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 8)
)
cie1000QosConfigInterfaceTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceIfIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceCos"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceDpl"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfacePcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceDei"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceTrustTag"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceTrustDscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceDwrrCount"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceTagRemarkingMode"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceTagPcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceTagDei"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceDscpTranslate"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceDscpClassify"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceDscpRemark"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQceAddressMode"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQceKeyType"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceWredGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceIngressMap"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceEgressMap"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceCosId"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceTableInfoGroup.setStatus("current")

cie1000QosConfigInterfaceTagToCosTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 9)
)
cie1000QosConfigInterfaceTagToCosTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceTagToCosIfIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceTagToCosPcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceTagToCosDei"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceTagToCosCos"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceTagToCosDpl"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceTagToCosTableInfoGroup.setStatus("current")

cie1000QosConfigInterfaceCosToTagTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 10)
)
cie1000QosConfigInterfaceCosToTagTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceCosToTagIfIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceCosToTagCos"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceCosToTagDpl"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceCosToTagPcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceCosToTagDei"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceCosToTagTableInfoGroup.setStatus("current")

cie1000QosConfigInterfacePolicerTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 11)
)
cie1000QosConfigInterfacePolicerTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigInterfacePolicerIfIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfacePolicerEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfacePolicerFrameRate"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfacePolicerFlowControl"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfacePolicerCir"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfacePolicerTableInfoGroup.setStatus("current")

cie1000QosConfigInterfaceQueuePolicerTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 12)
)
cie1000QosConfigInterfaceQueuePolicerTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQueuePolicerIfIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQueuePolicerQueue"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQueuePolicerEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQueuePolicerCir"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQueuePolicerTableInfoGroup.setStatus("current")

cie1000QosConfigInterfaceShaperTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 13)
)
cie1000QosConfigInterfaceShaperTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceShaperIfIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceShaperEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceShaperCir"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceShaperRateType"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceShaperTableInfoGroup.setStatus("current")

cie1000QosConfigInterfaceQueueShaperTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 14)
)
cie1000QosConfigInterfaceQueueShaperTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQueueShaperIfIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQueueShaperQueue"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQueueShaperEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQueueShaperExcess"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQueueShaperCir"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQueueShaperRateType"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQueueShaperCredit"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQueueShaperTableInfoGroup.setStatus("current")

cie1000QosConfigInterfaceSchedulerTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 15)
)
cie1000QosConfigInterfaceSchedulerTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceSchedulerIfIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceSchedulerQueue"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceSchedulerWeight"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceSchedulerCutThrough"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceSchedulerTableInfoGroup.setStatus("current")

cie1000QosConfigInterfaceStormPolicerUnicastTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 16)
)
cie1000QosConfigInterfaceStormPolicerUnicastTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceStormPolicerUnicastIfIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceStormPolicerUnicastEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceStormPolicerUnicastFrameRate"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceStormPolicerUnicastCir"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerUnicastTableInfoGroup.setStatus("current")

cie1000QosConfigInterfaceStormPolicerBroadcastTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 17)
)
cie1000QosConfigInterfaceStormPolicerBroadcastTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceStormPolicerBroadcastIfIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceStormPolicerBroadcastEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceStormPolicerBroadcastFrameRate"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceStormPolicerBroadcastCir"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerBroadcastTableInfoGroup.setStatus("current")

cie1000QosConfigInterfaceStormPolicerUnknownTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 18)
)
cie1000QosConfigInterfaceStormPolicerUnknownTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceStormPolicerUnknownIfIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceStormPolicerUnknownEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceStormPolicerUnknownFrameRate"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceStormPolicerUnknownCir"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceStormPolicerUnknownTableInfoGroup.setStatus("current")

cie1000QosConfigInterfaceQbvMaxSduTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 19)
)
cie1000QosConfigInterfaceQbvMaxSduTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvMaxSduIfIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvMaxSduQueue"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvMaxSduMaxSDU"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvMaxSduTableInfoGroup.setStatus("current")

cie1000QosConfigInterfaceQbvGclAdminTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 20)
)
cie1000QosConfigInterfaceQbvGclAdminTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvGclAdminIfIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvGclAdminGclIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvGclAdminGateState"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvGclAdminTimeInterval"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvGclAdminTableInfoGroup.setStatus("current")

cie1000QosConfigInterfaceQbvParamsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 21)
)
cie1000QosConfigInterfaceQbvParamsTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvParamsIfIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvParamsGateEnabled"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvParamsAdminGateStates"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvParamsAdminControlListLength"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvParamsAdminCycleTimeNumerator"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvParamsAdminCycleTimeDenominator"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvParamsAdminCycleTimeExtension"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvParamsAdminBaseTime"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvParamsConfigChange"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigInterfaceQbvParamsTableInfoGroup.setStatus("current")

cie1000QosConfigQceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 22)
)
cie1000QosConfigQceTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigQceQceId"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceNextQceId"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceSwitchId"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQcePortList"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceDestMacType"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceDestMac"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceDestMacMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceSrcMac"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceSrcMacMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceVlanTagType"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceVlanIdOp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceVlanId"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceVlanIdRange"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQcePcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceDei"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceInnerVlanTagType"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceInnerVlanIdOp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceInnerVlanId"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceInnerVlanIdRange"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceInnerPcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceInnerDei"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceFrameType"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceEtype"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceLlcDsap"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceLlcDsapMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceLlcSsap"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceLlcSsapMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceLlcControl"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceLlcControlMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceSnapPid"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceSnapPidMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv4Fragment"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv4DscpOp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv4Dscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv4DscpRange"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv4Protocol"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv4ProtocolMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv4SrcIp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv4SrcIpMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv4DestIp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv4DestIpMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv4SrcPortOp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv4SrcPort"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv4SrcPortRange"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv4DestPortOp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv4DestPort"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv4DestPortRange"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv6DscpOp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv6Dscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv6DscpRange"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv6Protocol"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv6ProtocolMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv6SrcIp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv6SrcIpMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv6DestIp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv6DestIpMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv6SrcPortOp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv6SrcPort"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv6SrcPortRange"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv6DestPortOp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv6DestPort"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceIpv6DestPortRange"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceActionCosEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceActionCos"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceActionDplEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceActionDpl"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceActionDscpEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceActionDscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceActionPcpDeiEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceActionPcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceActionDei"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceActionPolicyEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceActionPolicy"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceActionMapEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceActionMap"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceAction"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableInfoGroup.setStatus("current")

cie1000QosConfigQceTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 23)
)
cie1000QosConfigQceTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorQceId"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorNextQceId"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorSwitchId"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorPortList"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorDestMacType"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorDestMac"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorDestMacMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorSrcMac"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorSrcMacMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorVlanTagType"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorVlanIdOp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorVlanId"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorVlanIdRange"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorPcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorDei"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorInnerVlanTagType"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorInnerVlanIdOp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorInnerVlanId"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorInnerVlanIdRange"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorInnerPcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorInnerDei"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorFrameType"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorEtype"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorLlcDsap"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorLlcDsapMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorLlcSsap"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorLlcSsapMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorLlcControl"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorLlcControlMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorSnapPid"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorSnapPidMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv4Fragment"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv4DscpOp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv4Dscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv4DscpRange"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv4Protocol"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv4ProtocolMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv4SrcIp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv4SrcIpMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv4DestIp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv4DestIpMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv4SrcPortOp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv4SrcPort"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv4SrcPortRange"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv4DestPortOp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv4DestPort"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv4DestPortRange"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv6DscpOp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv6Dscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv6DscpRange"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv6Protocol"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv6ProtocolMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv6SrcIp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv6SrcIpMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv6DestIp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv6DestIpMask"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv6SrcPortOp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv6SrcPort"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv6SrcPortRange"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv6DestPortOp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv6DestPort"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorIpv6DestPortRange"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorActionCosEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorActionCos"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorActionDplEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorActionDpl"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorActionDscpEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorActionDscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorActionPcpDeiEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorActionPcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorActionDei"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorActionPolicyEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorActionPolicy"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorActionMapEnable"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorActionMap"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigQceTableRowEditorInfoGroup.setStatus("current")

cie1000QosConfigQcePrecedenceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 24)
)
cie1000QosConfigQcePrecedenceTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigQcePrecedenceIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQcePrecedenceQceId"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigQcePrecedenceTableInfoGroup.setStatus("current")

cie1000QosConfigIngressMapTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 25)
)
cie1000QosConfigIngressMapTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapIngressMapId"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapKey"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapActionCos"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapActionDpl"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapActionPcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapActionDei"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapActionDscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapActionCosid"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapActionPath"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapAction"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapTableInfoGroup.setStatus("current")

cie1000QosConfigIngressMapTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 26)
)
cie1000QosConfigIngressMapTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapTableRowEditorIngressMapId"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapTableRowEditorKey"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapTableRowEditorActionCos"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapTableRowEditorActionDpl"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapTableRowEditorActionPcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapTableRowEditorActionDei"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapTableRowEditorActionDscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapTableRowEditorActionCosid"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapTableRowEditorActionPath"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapTableRowEditorInfoGroup.setStatus("current")

cie1000QosConfigIngressMapPcpTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 27)
)
cie1000QosConfigIngressMapPcpTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapPcpIngressMapId"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapPcpPcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapPcpDei"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapPcpToCos"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapPcpToDpl"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapPcpToPcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapPcpToDei"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapPcpToDscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapPcpToCosid"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapPcpToPathCosid"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapPcpTableInfoGroup.setStatus("current")

cie1000QosConfigIngressMapDscpTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 28)
)
cie1000QosConfigIngressMapDscpTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapDscpIngressMapId"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapDscpDscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapDscpToCos"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapDscpToDpl"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapDscpToPcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapDscpToDei"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapDscpToDscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapDscpToCosid"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapDscpToPathCosid"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigIngressMapDscpTableInfoGroup.setStatus("current")

cie1000QosConfigEgressMapTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 29)
)
cie1000QosConfigEgressMapTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapEgressMapId"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapKey"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapActionPcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapActionDei"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapActionDscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapActionPath"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapAction"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapTableInfoGroup.setStatus("current")

cie1000QosConfigEgressMapTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 30)
)
cie1000QosConfigEgressMapTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapTableRowEditorEgressMapId"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapTableRowEditorKey"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapTableRowEditorActionPcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapTableRowEditorActionDei"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapTableRowEditorActionDscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapTableRowEditorActionPath"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapTableRowEditorInfoGroup.setStatus("current")

cie1000QosConfigEgressMapCosidTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 31)
)
cie1000QosConfigEgressMapCosidTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapCosidEgressMapId"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapCosidCosid"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapCosidDpl"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapCosidToPcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapCosidToDei"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapCosidToDscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapCosidToPathCosid"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapCosidTableInfoGroup.setStatus("current")

cie1000QosConfigEgressMapDscpTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 32)
)
cie1000QosConfigEgressMapDscpTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapDscpEgressMapId"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapDscpDscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapDscpDpl"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapDscpToPcp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapDscpToDei"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapDscpToDscp"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapDscpToPathCosid"))
)
if mibBuilder.loadTexts:
    cie1000QosConfigEgressMapDscpTableInfoGroup.setStatus("current")

cie1000QosStatusInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 33)
)
cie1000QosStatusInterfaceTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceIfIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceCos"))
)
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceTableInfoGroup.setStatus("current")

cie1000QosStatusInterfaceSchedulerTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 34)
)
cie1000QosStatusInterfaceSchedulerTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceSchedulerIfIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceSchedulerQueue"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceSchedulerWeight"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceSchedulerCutThrough"))
)
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceSchedulerTableInfoGroup.setStatus("current")

cie1000QosStatusInterfaceQbvGclOprTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 35)
)
cie1000QosStatusInterfaceQbvGclOprTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvGclOprIfIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvGclOprGclIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvGclOprGateState"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvGclOprTimeInterval"))
)
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvGclOprTableInfoGroup.setStatus("current")

cie1000QosStatusInterfaceQbvOprStatusTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 36)
)
cie1000QosStatusInterfaceQbvOprStatusTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvOprStatusIfIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvOprStatusOperGateStates"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvOprStatusOperControlListLength"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeNumerator"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeDenominator"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeExtension"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvOprStatusOperBaseTime"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvOprStatusConfigChangeTime"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvOprStatusTickGranularity"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvOprStatusCurrentTime"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvOprStatusConfigPending"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvOprStatusConfigChangeError"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvOprStatusSupportedListMax"))
)
if mibBuilder.loadTexts:
    cie1000QosStatusInterfaceQbvOprStatusTableInfoGroup.setStatus("current")

cie1000QosStatusQceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 37)
)
cie1000QosStatusQceTableInfoGroup.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosStatusQceSwitchId"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusQceIndex"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusQceUserId"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusQceQceId"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusQceConflict"))
)
if mibBuilder.loadTexts:
    cie1000QosStatusQceTableInfoGroup.setStatus("current")

cie1000QosControlQceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 2, 38)
)
cie1000QosControlQceInfoGroup.setObjects(
    ("CIE1000-QOS-MIB", "cie1000QosControlQceConflictResolve")
)
if mibBuilder.loadTexts:
    cie1000QosControlQceInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000QosMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 14, 2, 1, 1)
)
cie1000QosMibCompliance.setObjects(
      *(("CIE1000-QOS-MIB", "cie1000QosCapabilitiesInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsStormPolicersUnicastInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsStormPolicersMulticastInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsStormPolicersBroadcastInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsWredTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsDscpTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigGlobalsCosToDscpTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceTagToCosTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceCosToTagTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfacePolicerTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQueuePolicerTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceShaperTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQueueShaperTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceSchedulerTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceStormPolicerUnicastTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceStormPolicerBroadcastTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceStormPolicerUnknownTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvMaxSduTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvGclAdminTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigInterfaceQbvParamsTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQceTableRowEditorInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigQcePrecedenceTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapTableRowEditorInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapPcpTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigIngressMapDscpTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapTableRowEditorInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapCosidTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosConfigEgressMapDscpTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceSchedulerTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvGclOprTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusInterfaceQbvOprStatusTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosStatusQceTableInfoGroup"),
        ("CIE1000-QOS-MIB", "cie1000QosControlQceInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000QosMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-QOS-MIB",
    **{"CIE1000QosDscpClassify": CIE1000QosDscpClassify,
       "CIE1000QosDscpRemark": CIE1000QosDscpRemark,
       "CIE1000QosEgressMapKey": CIE1000QosEgressMapKey,
       "CIE1000QosIngressMapKey": CIE1000QosIngressMapKey,
       "CIE1000QosQceFrameType": CIE1000QosQceFrameType,
       "CIE1000QosQceUserType": CIE1000QosQceUserType,
       "CIE1000QosShaperRateType": CIE1000QosShaperRateType,
       "CIE1000QosTagRemarkingMode": CIE1000QosTagRemarkingMode,
       "CIE1000QosWredMaxSelector": CIE1000QosWredMaxSelector,
       "cie1000QosMib": cie1000QosMib,
       "cie1000QosMibObjects": cie1000QosMibObjects,
       "cie1000QosCapabilities": cie1000QosCapabilities,
       "cie1000QosCapabilitiesClassMin": cie1000QosCapabilitiesClassMin,
       "cie1000QosCapabilitiesClassMax": cie1000QosCapabilitiesClassMax,
       "cie1000QosCapabilitiesDplMin": cie1000QosCapabilitiesDplMin,
       "cie1000QosCapabilitiesDplMax": cie1000QosCapabilitiesDplMax,
       "cie1000QosCapabilitiesWredGroupMin": cie1000QosCapabilitiesWredGroupMin,
       "cie1000QosCapabilitiesWredGroupMax": cie1000QosCapabilitiesWredGroupMax,
       "cie1000QosCapabilitiesWredDplMin": cie1000QosCapabilitiesWredDplMin,
       "cie1000QosCapabilitiesWredDplMax": cie1000QosCapabilitiesWredDplMax,
       "cie1000QosCapabilitiesQceIdMin": cie1000QosCapabilitiesQceIdMin,
       "cie1000QosCapabilitiesQceIdMax": cie1000QosCapabilitiesQceIdMax,
       "cie1000QosCapabilitiesPortPolicerBitRateMin": cie1000QosCapabilitiesPortPolicerBitRateMin,
       "cie1000QosCapabilitiesPortPolicerBitRateMax": cie1000QosCapabilitiesPortPolicerBitRateMax,
       "cie1000QosCapabilitiesPortPolicerBitBurstMin": cie1000QosCapabilitiesPortPolicerBitBurstMin,
       "cie1000QosCapabilitiesPortPolicerBitBurstMax": cie1000QosCapabilitiesPortPolicerBitBurstMax,
       "cie1000QosCapabilitiesPortPolicerFrameRateMin": cie1000QosCapabilitiesPortPolicerFrameRateMin,
       "cie1000QosCapabilitiesPortPolicerFrameRateMax": cie1000QosCapabilitiesPortPolicerFrameRateMax,
       "cie1000QosCapabilitiesPortPolicerFrameBurstMin": cie1000QosCapabilitiesPortPolicerFrameBurstMin,
       "cie1000QosCapabilitiesPortPolicerFrameBurstMax": cie1000QosCapabilitiesPortPolicerFrameBurstMax,
       "cie1000QosCapabilitiesQueuePolicerBitRateMin": cie1000QosCapabilitiesQueuePolicerBitRateMin,
       "cie1000QosCapabilitiesQueuePolicerBitRateMax": cie1000QosCapabilitiesQueuePolicerBitRateMax,
       "cie1000QosCapabilitiesQueuePolicerBitBurstMin": cie1000QosCapabilitiesQueuePolicerBitBurstMin,
       "cie1000QosCapabilitiesQueuePolicerBitBurstMax": cie1000QosCapabilitiesQueuePolicerBitBurstMax,
       "cie1000QosCapabilitiesQueuePolicerFrameRateMin": cie1000QosCapabilitiesQueuePolicerFrameRateMin,
       "cie1000QosCapabilitiesQueuePolicerFrameRateMax": cie1000QosCapabilitiesQueuePolicerFrameRateMax,
       "cie1000QosCapabilitiesQueuePolicerFrameBurstMin": cie1000QosCapabilitiesQueuePolicerFrameBurstMin,
       "cie1000QosCapabilitiesQueuePolicerFrameBurstMax": cie1000QosCapabilitiesQueuePolicerFrameBurstMax,
       "cie1000QosCapabilitiesPortShaperBitRateMin": cie1000QosCapabilitiesPortShaperBitRateMin,
       "cie1000QosCapabilitiesPortShaperBitRateMax": cie1000QosCapabilitiesPortShaperBitRateMax,
       "cie1000QosCapabilitiesPortShaperBitBurstMin": cie1000QosCapabilitiesPortShaperBitBurstMin,
       "cie1000QosCapabilitiesPortShaperBitBurstMax": cie1000QosCapabilitiesPortShaperBitBurstMax,
       "cie1000QosCapabilitiesPortShaperFrameRateMin": cie1000QosCapabilitiesPortShaperFrameRateMin,
       "cie1000QosCapabilitiesPortShaperFrameRateMax": cie1000QosCapabilitiesPortShaperFrameRateMax,
       "cie1000QosCapabilitiesPortShaperFrameBurstMin": cie1000QosCapabilitiesPortShaperFrameBurstMin,
       "cie1000QosCapabilitiesPortShaperFrameBurstMax": cie1000QosCapabilitiesPortShaperFrameBurstMax,
       "cie1000QosCapabilitiesQueueShaperBitRateMin": cie1000QosCapabilitiesQueueShaperBitRateMin,
       "cie1000QosCapabilitiesQueueShaperBitRateMax": cie1000QosCapabilitiesQueueShaperBitRateMax,
       "cie1000QosCapabilitiesQueueShaperBitBurstMin": cie1000QosCapabilitiesQueueShaperBitBurstMin,
       "cie1000QosCapabilitiesQueueShaperBitBurstMax": cie1000QosCapabilitiesQueueShaperBitBurstMax,
       "cie1000QosCapabilitiesQueueShaperFrameRateMin": cie1000QosCapabilitiesQueueShaperFrameRateMin,
       "cie1000QosCapabilitiesQueueShaperFrameRateMax": cie1000QosCapabilitiesQueueShaperFrameRateMax,
       "cie1000QosCapabilitiesQueueShaperFrameBurstMin": cie1000QosCapabilitiesQueueShaperFrameBurstMin,
       "cie1000QosCapabilitiesQueueShaperFrameBurstMax": cie1000QosCapabilitiesQueueShaperFrameBurstMax,
       "cie1000QosCapabilitiesGlobalStormBitRateMin": cie1000QosCapabilitiesGlobalStormBitRateMin,
       "cie1000QosCapabilitiesGlobalStormBitRateMax": cie1000QosCapabilitiesGlobalStormBitRateMax,
       "cie1000QosCapabilitiesGlobalStormBitBurstMin": cie1000QosCapabilitiesGlobalStormBitBurstMin,
       "cie1000QosCapabilitiesGlobalStormBitBurstMax": cie1000QosCapabilitiesGlobalStormBitBurstMax,
       "cie1000QosCapabilitiesGlobalStormFrameRateMin": cie1000QosCapabilitiesGlobalStormFrameRateMin,
       "cie1000QosCapabilitiesGlobalStormFrameRateMax": cie1000QosCapabilitiesGlobalStormFrameRateMax,
       "cie1000QosCapabilitiesGlobalStormFrameBurstMin": cie1000QosCapabilitiesGlobalStormFrameBurstMin,
       "cie1000QosCapabilitiesGlobalStormFrameBurstMax": cie1000QosCapabilitiesGlobalStormFrameBurstMax,
       "cie1000QosCapabilitiesPortStormBitRateMin": cie1000QosCapabilitiesPortStormBitRateMin,
       "cie1000QosCapabilitiesPortStormBitRateMax": cie1000QosCapabilitiesPortStormBitRateMax,
       "cie1000QosCapabilitiesPortStormBitBurstMin": cie1000QosCapabilitiesPortStormBitBurstMin,
       "cie1000QosCapabilitiesPortStormBitBurstMax": cie1000QosCapabilitiesPortStormBitBurstMax,
       "cie1000QosCapabilitiesPortStormFrameRateMin": cie1000QosCapabilitiesPortStormFrameRateMin,
       "cie1000QosCapabilitiesPortStormFrameRateMax": cie1000QosCapabilitiesPortStormFrameRateMax,
       "cie1000QosCapabilitiesPortStormFrameBurstMin": cie1000QosCapabilitiesPortStormFrameBurstMin,
       "cie1000QosCapabilitiesPortStormFrameBurstMax": cie1000QosCapabilitiesPortStormFrameBurstMax,
       "cie1000QosCapabilitiesIngressMapIdMin": cie1000QosCapabilitiesIngressMapIdMin,
       "cie1000QosCapabilitiesIngressMapIdMax": cie1000QosCapabilitiesIngressMapIdMax,
       "cie1000QosCapabilitiesEgressMapIdMin": cie1000QosCapabilitiesEgressMapIdMin,
       "cie1000QosCapabilitiesEgressMapIdMax": cie1000QosCapabilitiesEgressMapIdMax,
       "cie1000QosCapabilitiesCosIdMin": cie1000QosCapabilitiesCosIdMin,
       "cie1000QosCapabilitiesCosIdMax": cie1000QosCapabilitiesCosIdMax,
       "cie1000QosCapabilitiesQbvGclLenMax": cie1000QosCapabilitiesQbvGclLenMax,
       "cie1000QosCapabilitiesDwrrCountMask": cie1000QosCapabilitiesDwrrCountMask,
       "cie1000QosCapabilitiesHasGlobalStormPolicers": cie1000QosCapabilitiesHasGlobalStormPolicers,
       "cie1000QosCapabilitiesHasPortStormPolicers": cie1000QosCapabilitiesHasPortStormPolicers,
       "cie1000QosCapabilitiesHasPortQueuePolicers": cie1000QosCapabilitiesHasPortQueuePolicers,
       "cie1000QosCapabilitiesHasWredV1": cie1000QosCapabilitiesHasWredV1,
       "cie1000QosCapabilitiesHasWredV2": cie1000QosCapabilitiesHasWredV2,
       "cie1000QosCapabilitiesHasFixedTagCosMap": cie1000QosCapabilitiesHasFixedTagCosMap,
       "cie1000QosCapabilitiesHasTagClassification": cie1000QosCapabilitiesHasTagClassification,
       "cie1000QosCapabilitiesHasTagRemarking": cie1000QosCapabilitiesHasTagRemarking,
       "cie1000QosCapabilitiesHasDscp": cie1000QosCapabilitiesHasDscp,
       "cie1000QosCapabilitiesHasDscpDplClassification": cie1000QosCapabilitiesHasDscpDplClassification,
       "cie1000QosCapabilitiesHasDscpDplRemarking": cie1000QosCapabilitiesHasDscpDplRemarking,
       "cie1000QosCapabilitiesHasPortPolicersFc": cie1000QosCapabilitiesHasPortPolicersFc,
       "cie1000QosCapabilitiesHasQueuePolicersFc": cie1000QosCapabilitiesHasQueuePolicersFc,
       "cie1000QosCapabilitiesHasPortShapersDlb": cie1000QosCapabilitiesHasPortShapersDlb,
       "cie1000QosCapabilitiesHasQueueShapersDlb": cie1000QosCapabilitiesHasQueueShapersDlb,
       "cie1000QosCapabilitiesHasQueueShapersExcess": cie1000QosCapabilitiesHasQueueShapersExcess,
       "cie1000QosCapabilitiesHasWredV3": cie1000QosCapabilitiesHasWredV3,
       "cie1000QosCapabilitiesHasQueueShapersCredit": cie1000QosCapabilitiesHasQueueShapersCredit,
       "cie1000QosCapabilitiesHasQueueCutThrough": cie1000QosCapabilitiesHasQueueCutThrough,
       "cie1000QosCapabilitiesHasQce": cie1000QosCapabilitiesHasQce,
       "cie1000QosCapabilitiesHasQceAddressMode": cie1000QosCapabilitiesHasQceAddressMode,
       "cie1000QosCapabilitiesHasQceKeyType": cie1000QosCapabilitiesHasQceKeyType,
       "cie1000QosCapabilitiesHasQceMacOui": cie1000QosCapabilitiesHasQceMacOui,
       "cie1000QosCapabilitiesHasQceDmac": cie1000QosCapabilitiesHasQceDmac,
       "cie1000QosCapabilitiesHasQceDip": cie1000QosCapabilitiesHasQceDip,
       "cie1000QosCapabilitiesHasQceCTag": cie1000QosCapabilitiesHasQceCTag,
       "cie1000QosCapabilitiesHasQceSTag": cie1000QosCapabilitiesHasQceSTag,
       "cie1000QosCapabilitiesHasQceInnerTag": cie1000QosCapabilitiesHasQceInnerTag,
       "cie1000QosCapabilitiesHasQceActionPcpDei": cie1000QosCapabilitiesHasQceActionPcpDei,
       "cie1000QosCapabilitiesHasQceActionPolicy": cie1000QosCapabilitiesHasQceActionPolicy,
       "cie1000QosCapabilitiesHasShapersRt": cie1000QosCapabilitiesHasShapersRt,
       "cie1000QosCapabilitiesHasQceActionMap": cie1000QosCapabilitiesHasQceActionMap,
       "cie1000QosCapabilitiesHasIngressMap": cie1000QosCapabilitiesHasIngressMap,
       "cie1000QosCapabilitiesHasEgressMap": cie1000QosCapabilitiesHasEgressMap,
       "cie1000QosCapabilitiesHasWred2orWredw3": cie1000QosCapabilitiesHasWred2orWredw3,
       "cie1000QosCapabilitiesHasDscpDp2": cie1000QosCapabilitiesHasDscpDp2,
       "cie1000QosCapabilitiesHasDscpDp3": cie1000QosCapabilitiesHasDscpDp3,
       "cie1000QosCapabilitiesHasDefaultPcpAndDei": cie1000QosCapabilitiesHasDefaultPcpAndDei,
       "cie1000QosCapabilitiesHasTrustTag": cie1000QosCapabilitiesHasTrustTag,
       "cie1000QosCapabilitiesHasCosIdClassification": cie1000QosCapabilitiesHasCosIdClassification,
       "cie1000QosCapabilitiesHasQbv": cie1000QosCapabilitiesHasQbv,
       "cie1000QosConfig": cie1000QosConfig,
       "cie1000QosConfigGlobals": cie1000QosConfigGlobals,
       "cie1000QosConfigGlobalsStormPolicers": cie1000QosConfigGlobalsStormPolicers,
       "cie1000QosConfigGlobalsStormPolicersUnicast": cie1000QosConfigGlobalsStormPolicersUnicast,
       "cie1000QosConfigGlobalsStormPolicersUnicastEnable": cie1000QosConfigGlobalsStormPolicersUnicastEnable,
       "cie1000QosConfigGlobalsStormPolicersUnicastRate": cie1000QosConfigGlobalsStormPolicersUnicastRate,
       "cie1000QosConfigGlobalsStormPolicersUnicastFrameRate": cie1000QosConfigGlobalsStormPolicersUnicastFrameRate,
       "cie1000QosConfigGlobalsStormPolicersMulticast": cie1000QosConfigGlobalsStormPolicersMulticast,
       "cie1000QosConfigGlobalsStormPolicersMulticastEnable": cie1000QosConfigGlobalsStormPolicersMulticastEnable,
       "cie1000QosConfigGlobalsStormPolicersMulticastRate": cie1000QosConfigGlobalsStormPolicersMulticastRate,
       "cie1000QosConfigGlobalsStormPolicersMulticastFrameRate": cie1000QosConfigGlobalsStormPolicersMulticastFrameRate,
       "cie1000QosConfigGlobalsStormPolicersBroadcast": cie1000QosConfigGlobalsStormPolicersBroadcast,
       "cie1000QosConfigGlobalsStormPolicersBroadcastEnable": cie1000QosConfigGlobalsStormPolicersBroadcastEnable,
       "cie1000QosConfigGlobalsStormPolicersBroadcastRate": cie1000QosConfigGlobalsStormPolicersBroadcastRate,
       "cie1000QosConfigGlobalsStormPolicersBroadcastFrameRate": cie1000QosConfigGlobalsStormPolicersBroadcastFrameRate,
       "cie1000QosConfigGlobalsWredTable": cie1000QosConfigGlobalsWredTable,
       "cie1000QosConfigGlobalsWredEntry": cie1000QosConfigGlobalsWredEntry,
       "cie1000QosConfigGlobalsWredGroup": cie1000QosConfigGlobalsWredGroup,
       "cie1000QosConfigGlobalsWredQueue": cie1000QosConfigGlobalsWredQueue,
       "cie1000QosConfigGlobalsWredDpl": cie1000QosConfigGlobalsWredDpl,
       "cie1000QosConfigGlobalsWredEnable": cie1000QosConfigGlobalsWredEnable,
       "cie1000QosConfigGlobalsWredMinimumFillLevel": cie1000QosConfigGlobalsWredMinimumFillLevel,
       "cie1000QosConfigGlobalsWredMaximum": cie1000QosConfigGlobalsWredMaximum,
       "cie1000QosConfigGlobalsWredMaxSelector": cie1000QosConfigGlobalsWredMaxSelector,
       "cie1000QosConfigGlobalsWredMaximumDp1": cie1000QosConfigGlobalsWredMaximumDp1,
       "cie1000QosConfigGlobalsWredMaximumDp2": cie1000QosConfigGlobalsWredMaximumDp2,
       "cie1000QosConfigGlobalsWredMaximumDp3": cie1000QosConfigGlobalsWredMaximumDp3,
       "cie1000QosConfigGlobalsDscpTable": cie1000QosConfigGlobalsDscpTable,
       "cie1000QosConfigGlobalsDscpEntry": cie1000QosConfigGlobalsDscpEntry,
       "cie1000QosConfigGlobalsDscpDscp": cie1000QosConfigGlobalsDscpDscp,
       "cie1000QosConfigGlobalsDscpTrust": cie1000QosConfigGlobalsDscpTrust,
       "cie1000QosConfigGlobalsDscpCos": cie1000QosConfigGlobalsDscpCos,
       "cie1000QosConfigGlobalsDscpDpl": cie1000QosConfigGlobalsDscpDpl,
       "cie1000QosConfigGlobalsDscpIngressTranslation": cie1000QosConfigGlobalsDscpIngressTranslation,
       "cie1000QosConfigGlobalsDscpClassify": cie1000QosConfigGlobalsDscpClassify,
       "cie1000QosConfigGlobalsDscpEgressTranslation": cie1000QosConfigGlobalsDscpEgressTranslation,
       "cie1000QosConfigGlobalsDscpEgressTranslationDp1": cie1000QosConfigGlobalsDscpEgressTranslationDp1,
       "cie1000QosConfigGlobalsCosToDscpTable": cie1000QosConfigGlobalsCosToDscpTable,
       "cie1000QosConfigGlobalsCosToDscpEntry": cie1000QosConfigGlobalsCosToDscpEntry,
       "cie1000QosConfigGlobalsCosToDscpCos": cie1000QosConfigGlobalsCosToDscpCos,
       "cie1000QosConfigGlobalsCosToDscpDscp": cie1000QosConfigGlobalsCosToDscpDscp,
       "cie1000QosConfigGlobalsCosToDscpDscpDp1": cie1000QosConfigGlobalsCosToDscpDscpDp1,
       "cie1000QosConfigGlobalsCosToDscpDscpDp2": cie1000QosConfigGlobalsCosToDscpDscpDp2,
       "cie1000QosConfigGlobalsCosToDscpDscpDp3": cie1000QosConfigGlobalsCosToDscpDscpDp3,
       "cie1000QosConfigInterface": cie1000QosConfigInterface,
       "cie1000QosConfigInterfaceTable": cie1000QosConfigInterfaceTable,
       "cie1000QosConfigInterfaceEntry": cie1000QosConfigInterfaceEntry,
       "cie1000QosConfigInterfaceIfIndex": cie1000QosConfigInterfaceIfIndex,
       "cie1000QosConfigInterfaceCos": cie1000QosConfigInterfaceCos,
       "cie1000QosConfigInterfaceDpl": cie1000QosConfigInterfaceDpl,
       "cie1000QosConfigInterfacePcp": cie1000QosConfigInterfacePcp,
       "cie1000QosConfigInterfaceDei": cie1000QosConfigInterfaceDei,
       "cie1000QosConfigInterfaceTrustTag": cie1000QosConfigInterfaceTrustTag,
       "cie1000QosConfigInterfaceTrustDscp": cie1000QosConfigInterfaceTrustDscp,
       "cie1000QosConfigInterfaceDwrrCount": cie1000QosConfigInterfaceDwrrCount,
       "cie1000QosConfigInterfaceTagRemarkingMode": cie1000QosConfigInterfaceTagRemarkingMode,
       "cie1000QosConfigInterfaceTagPcp": cie1000QosConfigInterfaceTagPcp,
       "cie1000QosConfigInterfaceTagDei": cie1000QosConfigInterfaceTagDei,
       "cie1000QosConfigInterfaceDscpTranslate": cie1000QosConfigInterfaceDscpTranslate,
       "cie1000QosConfigInterfaceDscpClassify": cie1000QosConfigInterfaceDscpClassify,
       "cie1000QosConfigInterfaceDscpRemark": cie1000QosConfigInterfaceDscpRemark,
       "cie1000QosConfigInterfaceQceAddressMode": cie1000QosConfigInterfaceQceAddressMode,
       "cie1000QosConfigInterfaceQceKeyType": cie1000QosConfigInterfaceQceKeyType,
       "cie1000QosConfigInterfaceWredGroup": cie1000QosConfigInterfaceWredGroup,
       "cie1000QosConfigInterfaceIngressMap": cie1000QosConfigInterfaceIngressMap,
       "cie1000QosConfigInterfaceEgressMap": cie1000QosConfigInterfaceEgressMap,
       "cie1000QosConfigInterfaceCosId": cie1000QosConfigInterfaceCosId,
       "cie1000QosConfigInterfaceTagToCosTable": cie1000QosConfigInterfaceTagToCosTable,
       "cie1000QosConfigInterfaceTagToCosEntry": cie1000QosConfigInterfaceTagToCosEntry,
       "cie1000QosConfigInterfaceTagToCosIfIndex": cie1000QosConfigInterfaceTagToCosIfIndex,
       "cie1000QosConfigInterfaceTagToCosPcp": cie1000QosConfigInterfaceTagToCosPcp,
       "cie1000QosConfigInterfaceTagToCosDei": cie1000QosConfigInterfaceTagToCosDei,
       "cie1000QosConfigInterfaceTagToCosCos": cie1000QosConfigInterfaceTagToCosCos,
       "cie1000QosConfigInterfaceTagToCosDpl": cie1000QosConfigInterfaceTagToCosDpl,
       "cie1000QosConfigInterfaceCosToTagTable": cie1000QosConfigInterfaceCosToTagTable,
       "cie1000QosConfigInterfaceCosToTagEntry": cie1000QosConfigInterfaceCosToTagEntry,
       "cie1000QosConfigInterfaceCosToTagIfIndex": cie1000QosConfigInterfaceCosToTagIfIndex,
       "cie1000QosConfigInterfaceCosToTagCos": cie1000QosConfigInterfaceCosToTagCos,
       "cie1000QosConfigInterfaceCosToTagDpl": cie1000QosConfigInterfaceCosToTagDpl,
       "cie1000QosConfigInterfaceCosToTagPcp": cie1000QosConfigInterfaceCosToTagPcp,
       "cie1000QosConfigInterfaceCosToTagDei": cie1000QosConfigInterfaceCosToTagDei,
       "cie1000QosConfigInterfacePolicerTable": cie1000QosConfigInterfacePolicerTable,
       "cie1000QosConfigInterfacePolicerEntry": cie1000QosConfigInterfacePolicerEntry,
       "cie1000QosConfigInterfacePolicerIfIndex": cie1000QosConfigInterfacePolicerIfIndex,
       "cie1000QosConfigInterfacePolicerEnable": cie1000QosConfigInterfacePolicerEnable,
       "cie1000QosConfigInterfacePolicerFrameRate": cie1000QosConfigInterfacePolicerFrameRate,
       "cie1000QosConfigInterfacePolicerFlowControl": cie1000QosConfigInterfacePolicerFlowControl,
       "cie1000QosConfigInterfacePolicerCir": cie1000QosConfigInterfacePolicerCir,
       "cie1000QosConfigInterfaceQueuePolicerTable": cie1000QosConfigInterfaceQueuePolicerTable,
       "cie1000QosConfigInterfaceQueuePolicerEntry": cie1000QosConfigInterfaceQueuePolicerEntry,
       "cie1000QosConfigInterfaceQueuePolicerIfIndex": cie1000QosConfigInterfaceQueuePolicerIfIndex,
       "cie1000QosConfigInterfaceQueuePolicerQueue": cie1000QosConfigInterfaceQueuePolicerQueue,
       "cie1000QosConfigInterfaceQueuePolicerEnable": cie1000QosConfigInterfaceQueuePolicerEnable,
       "cie1000QosConfigInterfaceQueuePolicerCir": cie1000QosConfigInterfaceQueuePolicerCir,
       "cie1000QosConfigInterfaceShaperTable": cie1000QosConfigInterfaceShaperTable,
       "cie1000QosConfigInterfaceShaperEntry": cie1000QosConfigInterfaceShaperEntry,
       "cie1000QosConfigInterfaceShaperIfIndex": cie1000QosConfigInterfaceShaperIfIndex,
       "cie1000QosConfigInterfaceShaperEnable": cie1000QosConfigInterfaceShaperEnable,
       "cie1000QosConfigInterfaceShaperCir": cie1000QosConfigInterfaceShaperCir,
       "cie1000QosConfigInterfaceShaperRateType": cie1000QosConfigInterfaceShaperRateType,
       "cie1000QosConfigInterfaceQueueShaperTable": cie1000QosConfigInterfaceQueueShaperTable,
       "cie1000QosConfigInterfaceQueueShaperEntry": cie1000QosConfigInterfaceQueueShaperEntry,
       "cie1000QosConfigInterfaceQueueShaperIfIndex": cie1000QosConfigInterfaceQueueShaperIfIndex,
       "cie1000QosConfigInterfaceQueueShaperQueue": cie1000QosConfigInterfaceQueueShaperQueue,
       "cie1000QosConfigInterfaceQueueShaperEnable": cie1000QosConfigInterfaceQueueShaperEnable,
       "cie1000QosConfigInterfaceQueueShaperExcess": cie1000QosConfigInterfaceQueueShaperExcess,
       "cie1000QosConfigInterfaceQueueShaperCir": cie1000QosConfigInterfaceQueueShaperCir,
       "cie1000QosConfigInterfaceQueueShaperRateType": cie1000QosConfigInterfaceQueueShaperRateType,
       "cie1000QosConfigInterfaceQueueShaperCredit": cie1000QosConfigInterfaceQueueShaperCredit,
       "cie1000QosConfigInterfaceSchedulerTable": cie1000QosConfigInterfaceSchedulerTable,
       "cie1000QosConfigInterfaceSchedulerEntry": cie1000QosConfigInterfaceSchedulerEntry,
       "cie1000QosConfigInterfaceSchedulerIfIndex": cie1000QosConfigInterfaceSchedulerIfIndex,
       "cie1000QosConfigInterfaceSchedulerQueue": cie1000QosConfigInterfaceSchedulerQueue,
       "cie1000QosConfigInterfaceSchedulerWeight": cie1000QosConfigInterfaceSchedulerWeight,
       "cie1000QosConfigInterfaceSchedulerCutThrough": cie1000QosConfigInterfaceSchedulerCutThrough,
       "cie1000QosConfigInterfaceStormPolicerUnicastTable": cie1000QosConfigInterfaceStormPolicerUnicastTable,
       "cie1000QosConfigInterfaceStormPolicerUnicastEntry": cie1000QosConfigInterfaceStormPolicerUnicastEntry,
       "cie1000QosConfigInterfaceStormPolicerUnicastIfIndex": cie1000QosConfigInterfaceStormPolicerUnicastIfIndex,
       "cie1000QosConfigInterfaceStormPolicerUnicastEnable": cie1000QosConfigInterfaceStormPolicerUnicastEnable,
       "cie1000QosConfigInterfaceStormPolicerUnicastFrameRate": cie1000QosConfigInterfaceStormPolicerUnicastFrameRate,
       "cie1000QosConfigInterfaceStormPolicerUnicastCir": cie1000QosConfigInterfaceStormPolicerUnicastCir,
       "cie1000QosConfigInterfaceStormPolicerBroadcastTable": cie1000QosConfigInterfaceStormPolicerBroadcastTable,
       "cie1000QosConfigInterfaceStormPolicerBroadcastEntry": cie1000QosConfigInterfaceStormPolicerBroadcastEntry,
       "cie1000QosConfigInterfaceStormPolicerBroadcastIfIndex": cie1000QosConfigInterfaceStormPolicerBroadcastIfIndex,
       "cie1000QosConfigInterfaceStormPolicerBroadcastEnable": cie1000QosConfigInterfaceStormPolicerBroadcastEnable,
       "cie1000QosConfigInterfaceStormPolicerBroadcastFrameRate": cie1000QosConfigInterfaceStormPolicerBroadcastFrameRate,
       "cie1000QosConfigInterfaceStormPolicerBroadcastCir": cie1000QosConfigInterfaceStormPolicerBroadcastCir,
       "cie1000QosConfigInterfaceStormPolicerUnknownTable": cie1000QosConfigInterfaceStormPolicerUnknownTable,
       "cie1000QosConfigInterfaceStormPolicerUnknownEntry": cie1000QosConfigInterfaceStormPolicerUnknownEntry,
       "cie1000QosConfigInterfaceStormPolicerUnknownIfIndex": cie1000QosConfigInterfaceStormPolicerUnknownIfIndex,
       "cie1000QosConfigInterfaceStormPolicerUnknownEnable": cie1000QosConfigInterfaceStormPolicerUnknownEnable,
       "cie1000QosConfigInterfaceStormPolicerUnknownFrameRate": cie1000QosConfigInterfaceStormPolicerUnknownFrameRate,
       "cie1000QosConfigInterfaceStormPolicerUnknownCir": cie1000QosConfigInterfaceStormPolicerUnknownCir,
       "cie1000QosConfigInterfaceQbvMaxSduTable": cie1000QosConfigInterfaceQbvMaxSduTable,
       "cie1000QosConfigInterfaceQbvMaxSduEntry": cie1000QosConfigInterfaceQbvMaxSduEntry,
       "cie1000QosConfigInterfaceQbvMaxSduIfIndex": cie1000QosConfigInterfaceQbvMaxSduIfIndex,
       "cie1000QosConfigInterfaceQbvMaxSduQueue": cie1000QosConfigInterfaceQbvMaxSduQueue,
       "cie1000QosConfigInterfaceQbvMaxSduMaxSDU": cie1000QosConfigInterfaceQbvMaxSduMaxSDU,
       "cie1000QosConfigInterfaceQbvGclAdminTable": cie1000QosConfigInterfaceQbvGclAdminTable,
       "cie1000QosConfigInterfaceQbvGclAdminEntry": cie1000QosConfigInterfaceQbvGclAdminEntry,
       "cie1000QosConfigInterfaceQbvGclAdminIfIndex": cie1000QosConfigInterfaceQbvGclAdminIfIndex,
       "cie1000QosConfigInterfaceQbvGclAdminGclIndex": cie1000QosConfigInterfaceQbvGclAdminGclIndex,
       "cie1000QosConfigInterfaceQbvGclAdminGateState": cie1000QosConfigInterfaceQbvGclAdminGateState,
       "cie1000QosConfigInterfaceQbvGclAdminTimeInterval": cie1000QosConfigInterfaceQbvGclAdminTimeInterval,
       "cie1000QosConfigInterfaceQbvParamsTable": cie1000QosConfigInterfaceQbvParamsTable,
       "cie1000QosConfigInterfaceQbvParamsEntry": cie1000QosConfigInterfaceQbvParamsEntry,
       "cie1000QosConfigInterfaceQbvParamsIfIndex": cie1000QosConfigInterfaceQbvParamsIfIndex,
       "cie1000QosConfigInterfaceQbvParamsGateEnabled": cie1000QosConfigInterfaceQbvParamsGateEnabled,
       "cie1000QosConfigInterfaceQbvParamsAdminGateStates": cie1000QosConfigInterfaceQbvParamsAdminGateStates,
       "cie1000QosConfigInterfaceQbvParamsAdminControlListLength": cie1000QosConfigInterfaceQbvParamsAdminControlListLength,
       "cie1000QosConfigInterfaceQbvParamsAdminCycleTimeNumerator": cie1000QosConfigInterfaceQbvParamsAdminCycleTimeNumerator,
       "cie1000QosConfigInterfaceQbvParamsAdminCycleTimeDenominator": cie1000QosConfigInterfaceQbvParamsAdminCycleTimeDenominator,
       "cie1000QosConfigInterfaceQbvParamsAdminCycleTimeExtension": cie1000QosConfigInterfaceQbvParamsAdminCycleTimeExtension,
       "cie1000QosConfigInterfaceQbvParamsAdminBaseTime": cie1000QosConfigInterfaceQbvParamsAdminBaseTime,
       "cie1000QosConfigInterfaceQbvParamsConfigChange": cie1000QosConfigInterfaceQbvParamsConfigChange,
       "cie1000QosConfigQce": cie1000QosConfigQce,
       "cie1000QosConfigQceTable": cie1000QosConfigQceTable,
       "cie1000QosConfigQceEntry": cie1000QosConfigQceEntry,
       "cie1000QosConfigQceQceId": cie1000QosConfigQceQceId,
       "cie1000QosConfigQceNextQceId": cie1000QosConfigQceNextQceId,
       "cie1000QosConfigQceSwitchId": cie1000QosConfigQceSwitchId,
       "cie1000QosConfigQcePortList": cie1000QosConfigQcePortList,
       "cie1000QosConfigQceDestMacType": cie1000QosConfigQceDestMacType,
       "cie1000QosConfigQceDestMac": cie1000QosConfigQceDestMac,
       "cie1000QosConfigQceDestMacMask": cie1000QosConfigQceDestMacMask,
       "cie1000QosConfigQceSrcMac": cie1000QosConfigQceSrcMac,
       "cie1000QosConfigQceSrcMacMask": cie1000QosConfigQceSrcMacMask,
       "cie1000QosConfigQceVlanTagType": cie1000QosConfigQceVlanTagType,
       "cie1000QosConfigQceVlanIdOp": cie1000QosConfigQceVlanIdOp,
       "cie1000QosConfigQceVlanId": cie1000QosConfigQceVlanId,
       "cie1000QosConfigQceVlanIdRange": cie1000QosConfigQceVlanIdRange,
       "cie1000QosConfigQcePcp": cie1000QosConfigQcePcp,
       "cie1000QosConfigQceDei": cie1000QosConfigQceDei,
       "cie1000QosConfigQceInnerVlanTagType": cie1000QosConfigQceInnerVlanTagType,
       "cie1000QosConfigQceInnerVlanIdOp": cie1000QosConfigQceInnerVlanIdOp,
       "cie1000QosConfigQceInnerVlanId": cie1000QosConfigQceInnerVlanId,
       "cie1000QosConfigQceInnerVlanIdRange": cie1000QosConfigQceInnerVlanIdRange,
       "cie1000QosConfigQceInnerPcp": cie1000QosConfigQceInnerPcp,
       "cie1000QosConfigQceInnerDei": cie1000QosConfigQceInnerDei,
       "cie1000QosConfigQceFrameType": cie1000QosConfigQceFrameType,
       "cie1000QosConfigQceEtype": cie1000QosConfigQceEtype,
       "cie1000QosConfigQceLlcDsap": cie1000QosConfigQceLlcDsap,
       "cie1000QosConfigQceLlcDsapMask": cie1000QosConfigQceLlcDsapMask,
       "cie1000QosConfigQceLlcSsap": cie1000QosConfigQceLlcSsap,
       "cie1000QosConfigQceLlcSsapMask": cie1000QosConfigQceLlcSsapMask,
       "cie1000QosConfigQceLlcControl": cie1000QosConfigQceLlcControl,
       "cie1000QosConfigQceLlcControlMask": cie1000QosConfigQceLlcControlMask,
       "cie1000QosConfigQceSnapPid": cie1000QosConfigQceSnapPid,
       "cie1000QosConfigQceSnapPidMask": cie1000QosConfigQceSnapPidMask,
       "cie1000QosConfigQceIpv4Fragment": cie1000QosConfigQceIpv4Fragment,
       "cie1000QosConfigQceIpv4DscpOp": cie1000QosConfigQceIpv4DscpOp,
       "cie1000QosConfigQceIpv4Dscp": cie1000QosConfigQceIpv4Dscp,
       "cie1000QosConfigQceIpv4DscpRange": cie1000QosConfigQceIpv4DscpRange,
       "cie1000QosConfigQceIpv4Protocol": cie1000QosConfigQceIpv4Protocol,
       "cie1000QosConfigQceIpv4ProtocolMask": cie1000QosConfigQceIpv4ProtocolMask,
       "cie1000QosConfigQceIpv4SrcIp": cie1000QosConfigQceIpv4SrcIp,
       "cie1000QosConfigQceIpv4SrcIpMask": cie1000QosConfigQceIpv4SrcIpMask,
       "cie1000QosConfigQceIpv4DestIp": cie1000QosConfigQceIpv4DestIp,
       "cie1000QosConfigQceIpv4DestIpMask": cie1000QosConfigQceIpv4DestIpMask,
       "cie1000QosConfigQceIpv4SrcPortOp": cie1000QosConfigQceIpv4SrcPortOp,
       "cie1000QosConfigQceIpv4SrcPort": cie1000QosConfigQceIpv4SrcPort,
       "cie1000QosConfigQceIpv4SrcPortRange": cie1000QosConfigQceIpv4SrcPortRange,
       "cie1000QosConfigQceIpv4DestPortOp": cie1000QosConfigQceIpv4DestPortOp,
       "cie1000QosConfigQceIpv4DestPort": cie1000QosConfigQceIpv4DestPort,
       "cie1000QosConfigQceIpv4DestPortRange": cie1000QosConfigQceIpv4DestPortRange,
       "cie1000QosConfigQceIpv6DscpOp": cie1000QosConfigQceIpv6DscpOp,
       "cie1000QosConfigQceIpv6Dscp": cie1000QosConfigQceIpv6Dscp,
       "cie1000QosConfigQceIpv6DscpRange": cie1000QosConfigQceIpv6DscpRange,
       "cie1000QosConfigQceIpv6Protocol": cie1000QosConfigQceIpv6Protocol,
       "cie1000QosConfigQceIpv6ProtocolMask": cie1000QosConfigQceIpv6ProtocolMask,
       "cie1000QosConfigQceIpv6SrcIp": cie1000QosConfigQceIpv6SrcIp,
       "cie1000QosConfigQceIpv6SrcIpMask": cie1000QosConfigQceIpv6SrcIpMask,
       "cie1000QosConfigQceIpv6DestIp": cie1000QosConfigQceIpv6DestIp,
       "cie1000QosConfigQceIpv6DestIpMask": cie1000QosConfigQceIpv6DestIpMask,
       "cie1000QosConfigQceIpv6SrcPortOp": cie1000QosConfigQceIpv6SrcPortOp,
       "cie1000QosConfigQceIpv6SrcPort": cie1000QosConfigQceIpv6SrcPort,
       "cie1000QosConfigQceIpv6SrcPortRange": cie1000QosConfigQceIpv6SrcPortRange,
       "cie1000QosConfigQceIpv6DestPortOp": cie1000QosConfigQceIpv6DestPortOp,
       "cie1000QosConfigQceIpv6DestPort": cie1000QosConfigQceIpv6DestPort,
       "cie1000QosConfigQceIpv6DestPortRange": cie1000QosConfigQceIpv6DestPortRange,
       "cie1000QosConfigQceActionCosEnable": cie1000QosConfigQceActionCosEnable,
       "cie1000QosConfigQceActionCos": cie1000QosConfigQceActionCos,
       "cie1000QosConfigQceActionDplEnable": cie1000QosConfigQceActionDplEnable,
       "cie1000QosConfigQceActionDpl": cie1000QosConfigQceActionDpl,
       "cie1000QosConfigQceActionDscpEnable": cie1000QosConfigQceActionDscpEnable,
       "cie1000QosConfigQceActionDscp": cie1000QosConfigQceActionDscp,
       "cie1000QosConfigQceActionPcpDeiEnable": cie1000QosConfigQceActionPcpDeiEnable,
       "cie1000QosConfigQceActionPcp": cie1000QosConfigQceActionPcp,
       "cie1000QosConfigQceActionDei": cie1000QosConfigQceActionDei,
       "cie1000QosConfigQceActionPolicyEnable": cie1000QosConfigQceActionPolicyEnable,
       "cie1000QosConfigQceActionPolicy": cie1000QosConfigQceActionPolicy,
       "cie1000QosConfigQceActionMapEnable": cie1000QosConfigQceActionMapEnable,
       "cie1000QosConfigQceActionMap": cie1000QosConfigQceActionMap,
       "cie1000QosConfigQceAction": cie1000QosConfigQceAction,
       "cie1000QosConfigQceTableRowEditor": cie1000QosConfigQceTableRowEditor,
       "cie1000QosConfigQceTableRowEditorQceId": cie1000QosConfigQceTableRowEditorQceId,
       "cie1000QosConfigQceTableRowEditorNextQceId": cie1000QosConfigQceTableRowEditorNextQceId,
       "cie1000QosConfigQceTableRowEditorSwitchId": cie1000QosConfigQceTableRowEditorSwitchId,
       "cie1000QosConfigQceTableRowEditorPortList": cie1000QosConfigQceTableRowEditorPortList,
       "cie1000QosConfigQceTableRowEditorDestMacType": cie1000QosConfigQceTableRowEditorDestMacType,
       "cie1000QosConfigQceTableRowEditorDestMac": cie1000QosConfigQceTableRowEditorDestMac,
       "cie1000QosConfigQceTableRowEditorDestMacMask": cie1000QosConfigQceTableRowEditorDestMacMask,
       "cie1000QosConfigQceTableRowEditorSrcMac": cie1000QosConfigQceTableRowEditorSrcMac,
       "cie1000QosConfigQceTableRowEditorSrcMacMask": cie1000QosConfigQceTableRowEditorSrcMacMask,
       "cie1000QosConfigQceTableRowEditorVlanTagType": cie1000QosConfigQceTableRowEditorVlanTagType,
       "cie1000QosConfigQceTableRowEditorVlanIdOp": cie1000QosConfigQceTableRowEditorVlanIdOp,
       "cie1000QosConfigQceTableRowEditorVlanId": cie1000QosConfigQceTableRowEditorVlanId,
       "cie1000QosConfigQceTableRowEditorVlanIdRange": cie1000QosConfigQceTableRowEditorVlanIdRange,
       "cie1000QosConfigQceTableRowEditorPcp": cie1000QosConfigQceTableRowEditorPcp,
       "cie1000QosConfigQceTableRowEditorDei": cie1000QosConfigQceTableRowEditorDei,
       "cie1000QosConfigQceTableRowEditorInnerVlanTagType": cie1000QosConfigQceTableRowEditorInnerVlanTagType,
       "cie1000QosConfigQceTableRowEditorInnerVlanIdOp": cie1000QosConfigQceTableRowEditorInnerVlanIdOp,
       "cie1000QosConfigQceTableRowEditorInnerVlanId": cie1000QosConfigQceTableRowEditorInnerVlanId,
       "cie1000QosConfigQceTableRowEditorInnerVlanIdRange": cie1000QosConfigQceTableRowEditorInnerVlanIdRange,
       "cie1000QosConfigQceTableRowEditorInnerPcp": cie1000QosConfigQceTableRowEditorInnerPcp,
       "cie1000QosConfigQceTableRowEditorInnerDei": cie1000QosConfigQceTableRowEditorInnerDei,
       "cie1000QosConfigQceTableRowEditorFrameType": cie1000QosConfigQceTableRowEditorFrameType,
       "cie1000QosConfigQceTableRowEditorEtype": cie1000QosConfigQceTableRowEditorEtype,
       "cie1000QosConfigQceTableRowEditorLlcDsap": cie1000QosConfigQceTableRowEditorLlcDsap,
       "cie1000QosConfigQceTableRowEditorLlcDsapMask": cie1000QosConfigQceTableRowEditorLlcDsapMask,
       "cie1000QosConfigQceTableRowEditorLlcSsap": cie1000QosConfigQceTableRowEditorLlcSsap,
       "cie1000QosConfigQceTableRowEditorLlcSsapMask": cie1000QosConfigQceTableRowEditorLlcSsapMask,
       "cie1000QosConfigQceTableRowEditorLlcControl": cie1000QosConfigQceTableRowEditorLlcControl,
       "cie1000QosConfigQceTableRowEditorLlcControlMask": cie1000QosConfigQceTableRowEditorLlcControlMask,
       "cie1000QosConfigQceTableRowEditorSnapPid": cie1000QosConfigQceTableRowEditorSnapPid,
       "cie1000QosConfigQceTableRowEditorSnapPidMask": cie1000QosConfigQceTableRowEditorSnapPidMask,
       "cie1000QosConfigQceTableRowEditorIpv4Fragment": cie1000QosConfigQceTableRowEditorIpv4Fragment,
       "cie1000QosConfigQceTableRowEditorIpv4DscpOp": cie1000QosConfigQceTableRowEditorIpv4DscpOp,
       "cie1000QosConfigQceTableRowEditorIpv4Dscp": cie1000QosConfigQceTableRowEditorIpv4Dscp,
       "cie1000QosConfigQceTableRowEditorIpv4DscpRange": cie1000QosConfigQceTableRowEditorIpv4DscpRange,
       "cie1000QosConfigQceTableRowEditorIpv4Protocol": cie1000QosConfigQceTableRowEditorIpv4Protocol,
       "cie1000QosConfigQceTableRowEditorIpv4ProtocolMask": cie1000QosConfigQceTableRowEditorIpv4ProtocolMask,
       "cie1000QosConfigQceTableRowEditorIpv4SrcIp": cie1000QosConfigQceTableRowEditorIpv4SrcIp,
       "cie1000QosConfigQceTableRowEditorIpv4SrcIpMask": cie1000QosConfigQceTableRowEditorIpv4SrcIpMask,
       "cie1000QosConfigQceTableRowEditorIpv4DestIp": cie1000QosConfigQceTableRowEditorIpv4DestIp,
       "cie1000QosConfigQceTableRowEditorIpv4DestIpMask": cie1000QosConfigQceTableRowEditorIpv4DestIpMask,
       "cie1000QosConfigQceTableRowEditorIpv4SrcPortOp": cie1000QosConfigQceTableRowEditorIpv4SrcPortOp,
       "cie1000QosConfigQceTableRowEditorIpv4SrcPort": cie1000QosConfigQceTableRowEditorIpv4SrcPort,
       "cie1000QosConfigQceTableRowEditorIpv4SrcPortRange": cie1000QosConfigQceTableRowEditorIpv4SrcPortRange,
       "cie1000QosConfigQceTableRowEditorIpv4DestPortOp": cie1000QosConfigQceTableRowEditorIpv4DestPortOp,
       "cie1000QosConfigQceTableRowEditorIpv4DestPort": cie1000QosConfigQceTableRowEditorIpv4DestPort,
       "cie1000QosConfigQceTableRowEditorIpv4DestPortRange": cie1000QosConfigQceTableRowEditorIpv4DestPortRange,
       "cie1000QosConfigQceTableRowEditorIpv6DscpOp": cie1000QosConfigQceTableRowEditorIpv6DscpOp,
       "cie1000QosConfigQceTableRowEditorIpv6Dscp": cie1000QosConfigQceTableRowEditorIpv6Dscp,
       "cie1000QosConfigQceTableRowEditorIpv6DscpRange": cie1000QosConfigQceTableRowEditorIpv6DscpRange,
       "cie1000QosConfigQceTableRowEditorIpv6Protocol": cie1000QosConfigQceTableRowEditorIpv6Protocol,
       "cie1000QosConfigQceTableRowEditorIpv6ProtocolMask": cie1000QosConfigQceTableRowEditorIpv6ProtocolMask,
       "cie1000QosConfigQceTableRowEditorIpv6SrcIp": cie1000QosConfigQceTableRowEditorIpv6SrcIp,
       "cie1000QosConfigQceTableRowEditorIpv6SrcIpMask": cie1000QosConfigQceTableRowEditorIpv6SrcIpMask,
       "cie1000QosConfigQceTableRowEditorIpv6DestIp": cie1000QosConfigQceTableRowEditorIpv6DestIp,
       "cie1000QosConfigQceTableRowEditorIpv6DestIpMask": cie1000QosConfigQceTableRowEditorIpv6DestIpMask,
       "cie1000QosConfigQceTableRowEditorIpv6SrcPortOp": cie1000QosConfigQceTableRowEditorIpv6SrcPortOp,
       "cie1000QosConfigQceTableRowEditorIpv6SrcPort": cie1000QosConfigQceTableRowEditorIpv6SrcPort,
       "cie1000QosConfigQceTableRowEditorIpv6SrcPortRange": cie1000QosConfigQceTableRowEditorIpv6SrcPortRange,
       "cie1000QosConfigQceTableRowEditorIpv6DestPortOp": cie1000QosConfigQceTableRowEditorIpv6DestPortOp,
       "cie1000QosConfigQceTableRowEditorIpv6DestPort": cie1000QosConfigQceTableRowEditorIpv6DestPort,
       "cie1000QosConfigQceTableRowEditorIpv6DestPortRange": cie1000QosConfigQceTableRowEditorIpv6DestPortRange,
       "cie1000QosConfigQceTableRowEditorActionCosEnable": cie1000QosConfigQceTableRowEditorActionCosEnable,
       "cie1000QosConfigQceTableRowEditorActionCos": cie1000QosConfigQceTableRowEditorActionCos,
       "cie1000QosConfigQceTableRowEditorActionDplEnable": cie1000QosConfigQceTableRowEditorActionDplEnable,
       "cie1000QosConfigQceTableRowEditorActionDpl": cie1000QosConfigQceTableRowEditorActionDpl,
       "cie1000QosConfigQceTableRowEditorActionDscpEnable": cie1000QosConfigQceTableRowEditorActionDscpEnable,
       "cie1000QosConfigQceTableRowEditorActionDscp": cie1000QosConfigQceTableRowEditorActionDscp,
       "cie1000QosConfigQceTableRowEditorActionPcpDeiEnable": cie1000QosConfigQceTableRowEditorActionPcpDeiEnable,
       "cie1000QosConfigQceTableRowEditorActionPcp": cie1000QosConfigQceTableRowEditorActionPcp,
       "cie1000QosConfigQceTableRowEditorActionDei": cie1000QosConfigQceTableRowEditorActionDei,
       "cie1000QosConfigQceTableRowEditorActionPolicyEnable": cie1000QosConfigQceTableRowEditorActionPolicyEnable,
       "cie1000QosConfigQceTableRowEditorActionPolicy": cie1000QosConfigQceTableRowEditorActionPolicy,
       "cie1000QosConfigQceTableRowEditorActionMapEnable": cie1000QosConfigQceTableRowEditorActionMapEnable,
       "cie1000QosConfigQceTableRowEditorActionMap": cie1000QosConfigQceTableRowEditorActionMap,
       "cie1000QosConfigQceTableRowEditorAction": cie1000QosConfigQceTableRowEditorAction,
       "cie1000QosConfigQcePrecedenceTable": cie1000QosConfigQcePrecedenceTable,
       "cie1000QosConfigQcePrecedenceEntry": cie1000QosConfigQcePrecedenceEntry,
       "cie1000QosConfigQcePrecedenceIndex": cie1000QosConfigQcePrecedenceIndex,
       "cie1000QosConfigQcePrecedenceQceId": cie1000QosConfigQcePrecedenceQceId,
       "cie1000QosConfigIngressMap": cie1000QosConfigIngressMap,
       "cie1000QosConfigIngressMapTable": cie1000QosConfigIngressMapTable,
       "cie1000QosConfigIngressMapEntry": cie1000QosConfigIngressMapEntry,
       "cie1000QosConfigIngressMapIngressMapId": cie1000QosConfigIngressMapIngressMapId,
       "cie1000QosConfigIngressMapKey": cie1000QosConfigIngressMapKey,
       "cie1000QosConfigIngressMapActionCos": cie1000QosConfigIngressMapActionCos,
       "cie1000QosConfigIngressMapActionDpl": cie1000QosConfigIngressMapActionDpl,
       "cie1000QosConfigIngressMapActionPcp": cie1000QosConfigIngressMapActionPcp,
       "cie1000QosConfigIngressMapActionDei": cie1000QosConfigIngressMapActionDei,
       "cie1000QosConfigIngressMapActionDscp": cie1000QosConfigIngressMapActionDscp,
       "cie1000QosConfigIngressMapActionCosid": cie1000QosConfigIngressMapActionCosid,
       "cie1000QosConfigIngressMapActionPath": cie1000QosConfigIngressMapActionPath,
       "cie1000QosConfigIngressMapAction": cie1000QosConfigIngressMapAction,
       "cie1000QosConfigIngressMapTableRowEditor": cie1000QosConfigIngressMapTableRowEditor,
       "cie1000QosConfigIngressMapTableRowEditorIngressMapId": cie1000QosConfigIngressMapTableRowEditorIngressMapId,
       "cie1000QosConfigIngressMapTableRowEditorKey": cie1000QosConfigIngressMapTableRowEditorKey,
       "cie1000QosConfigIngressMapTableRowEditorActionCos": cie1000QosConfigIngressMapTableRowEditorActionCos,
       "cie1000QosConfigIngressMapTableRowEditorActionDpl": cie1000QosConfigIngressMapTableRowEditorActionDpl,
       "cie1000QosConfigIngressMapTableRowEditorActionPcp": cie1000QosConfigIngressMapTableRowEditorActionPcp,
       "cie1000QosConfigIngressMapTableRowEditorActionDei": cie1000QosConfigIngressMapTableRowEditorActionDei,
       "cie1000QosConfigIngressMapTableRowEditorActionDscp": cie1000QosConfigIngressMapTableRowEditorActionDscp,
       "cie1000QosConfigIngressMapTableRowEditorActionCosid": cie1000QosConfigIngressMapTableRowEditorActionCosid,
       "cie1000QosConfigIngressMapTableRowEditorActionPath": cie1000QosConfigIngressMapTableRowEditorActionPath,
       "cie1000QosConfigIngressMapTableRowEditorAction": cie1000QosConfigIngressMapTableRowEditorAction,
       "cie1000QosConfigIngressMapPcpTable": cie1000QosConfigIngressMapPcpTable,
       "cie1000QosConfigIngressMapPcpEntry": cie1000QosConfigIngressMapPcpEntry,
       "cie1000QosConfigIngressMapPcpIngressMapId": cie1000QosConfigIngressMapPcpIngressMapId,
       "cie1000QosConfigIngressMapPcpPcp": cie1000QosConfigIngressMapPcpPcp,
       "cie1000QosConfigIngressMapPcpDei": cie1000QosConfigIngressMapPcpDei,
       "cie1000QosConfigIngressMapPcpToCos": cie1000QosConfigIngressMapPcpToCos,
       "cie1000QosConfigIngressMapPcpToDpl": cie1000QosConfigIngressMapPcpToDpl,
       "cie1000QosConfigIngressMapPcpToPcp": cie1000QosConfigIngressMapPcpToPcp,
       "cie1000QosConfigIngressMapPcpToDei": cie1000QosConfigIngressMapPcpToDei,
       "cie1000QosConfigIngressMapPcpToDscp": cie1000QosConfigIngressMapPcpToDscp,
       "cie1000QosConfigIngressMapPcpToCosid": cie1000QosConfigIngressMapPcpToCosid,
       "cie1000QosConfigIngressMapPcpToPathCosid": cie1000QosConfigIngressMapPcpToPathCosid,
       "cie1000QosConfigIngressMapDscpTable": cie1000QosConfigIngressMapDscpTable,
       "cie1000QosConfigIngressMapDscpEntry": cie1000QosConfigIngressMapDscpEntry,
       "cie1000QosConfigIngressMapDscpIngressMapId": cie1000QosConfigIngressMapDscpIngressMapId,
       "cie1000QosConfigIngressMapDscpDscp": cie1000QosConfigIngressMapDscpDscp,
       "cie1000QosConfigIngressMapDscpToCos": cie1000QosConfigIngressMapDscpToCos,
       "cie1000QosConfigIngressMapDscpToDpl": cie1000QosConfigIngressMapDscpToDpl,
       "cie1000QosConfigIngressMapDscpToPcp": cie1000QosConfigIngressMapDscpToPcp,
       "cie1000QosConfigIngressMapDscpToDei": cie1000QosConfigIngressMapDscpToDei,
       "cie1000QosConfigIngressMapDscpToDscp": cie1000QosConfigIngressMapDscpToDscp,
       "cie1000QosConfigIngressMapDscpToCosid": cie1000QosConfigIngressMapDscpToCosid,
       "cie1000QosConfigIngressMapDscpToPathCosid": cie1000QosConfigIngressMapDscpToPathCosid,
       "cie1000QosConfigEgressMap": cie1000QosConfigEgressMap,
       "cie1000QosConfigEgressMapTable": cie1000QosConfigEgressMapTable,
       "cie1000QosConfigEgressMapEntry": cie1000QosConfigEgressMapEntry,
       "cie1000QosConfigEgressMapEgressMapId": cie1000QosConfigEgressMapEgressMapId,
       "cie1000QosConfigEgressMapKey": cie1000QosConfigEgressMapKey,
       "cie1000QosConfigEgressMapActionPcp": cie1000QosConfigEgressMapActionPcp,
       "cie1000QosConfigEgressMapActionDei": cie1000QosConfigEgressMapActionDei,
       "cie1000QosConfigEgressMapActionDscp": cie1000QosConfigEgressMapActionDscp,
       "cie1000QosConfigEgressMapActionPath": cie1000QosConfigEgressMapActionPath,
       "cie1000QosConfigEgressMapAction": cie1000QosConfigEgressMapAction,
       "cie1000QosConfigEgressMapTableRowEditor": cie1000QosConfigEgressMapTableRowEditor,
       "cie1000QosConfigEgressMapTableRowEditorEgressMapId": cie1000QosConfigEgressMapTableRowEditorEgressMapId,
       "cie1000QosConfigEgressMapTableRowEditorKey": cie1000QosConfigEgressMapTableRowEditorKey,
       "cie1000QosConfigEgressMapTableRowEditorActionPcp": cie1000QosConfigEgressMapTableRowEditorActionPcp,
       "cie1000QosConfigEgressMapTableRowEditorActionDei": cie1000QosConfigEgressMapTableRowEditorActionDei,
       "cie1000QosConfigEgressMapTableRowEditorActionDscp": cie1000QosConfigEgressMapTableRowEditorActionDscp,
       "cie1000QosConfigEgressMapTableRowEditorActionPath": cie1000QosConfigEgressMapTableRowEditorActionPath,
       "cie1000QosConfigEgressMapTableRowEditorAction": cie1000QosConfigEgressMapTableRowEditorAction,
       "cie1000QosConfigEgressMapCosidTable": cie1000QosConfigEgressMapCosidTable,
       "cie1000QosConfigEgressMapCosidEntry": cie1000QosConfigEgressMapCosidEntry,
       "cie1000QosConfigEgressMapCosidEgressMapId": cie1000QosConfigEgressMapCosidEgressMapId,
       "cie1000QosConfigEgressMapCosidCosid": cie1000QosConfigEgressMapCosidCosid,
       "cie1000QosConfigEgressMapCosidDpl": cie1000QosConfigEgressMapCosidDpl,
       "cie1000QosConfigEgressMapCosidToPcp": cie1000QosConfigEgressMapCosidToPcp,
       "cie1000QosConfigEgressMapCosidToDei": cie1000QosConfigEgressMapCosidToDei,
       "cie1000QosConfigEgressMapCosidToDscp": cie1000QosConfigEgressMapCosidToDscp,
       "cie1000QosConfigEgressMapCosidToPathCosid": cie1000QosConfigEgressMapCosidToPathCosid,
       "cie1000QosConfigEgressMapDscpTable": cie1000QosConfigEgressMapDscpTable,
       "cie1000QosConfigEgressMapDscpEntry": cie1000QosConfigEgressMapDscpEntry,
       "cie1000QosConfigEgressMapDscpEgressMapId": cie1000QosConfigEgressMapDscpEgressMapId,
       "cie1000QosConfigEgressMapDscpDscp": cie1000QosConfigEgressMapDscpDscp,
       "cie1000QosConfigEgressMapDscpDpl": cie1000QosConfigEgressMapDscpDpl,
       "cie1000QosConfigEgressMapDscpToPcp": cie1000QosConfigEgressMapDscpToPcp,
       "cie1000QosConfigEgressMapDscpToDei": cie1000QosConfigEgressMapDscpToDei,
       "cie1000QosConfigEgressMapDscpToDscp": cie1000QosConfigEgressMapDscpToDscp,
       "cie1000QosConfigEgressMapDscpToPathCosid": cie1000QosConfigEgressMapDscpToPathCosid,
       "cie1000QosStatus": cie1000QosStatus,
       "cie1000QosStatusInterface": cie1000QosStatusInterface,
       "cie1000QosStatusInterfaceTable": cie1000QosStatusInterfaceTable,
       "cie1000QosStatusInterfaceEntry": cie1000QosStatusInterfaceEntry,
       "cie1000QosStatusInterfaceIfIndex": cie1000QosStatusInterfaceIfIndex,
       "cie1000QosStatusInterfaceCos": cie1000QosStatusInterfaceCos,
       "cie1000QosStatusInterfaceSchedulerTable": cie1000QosStatusInterfaceSchedulerTable,
       "cie1000QosStatusInterfaceSchedulerEntry": cie1000QosStatusInterfaceSchedulerEntry,
       "cie1000QosStatusInterfaceSchedulerIfIndex": cie1000QosStatusInterfaceSchedulerIfIndex,
       "cie1000QosStatusInterfaceSchedulerQueue": cie1000QosStatusInterfaceSchedulerQueue,
       "cie1000QosStatusInterfaceSchedulerWeight": cie1000QosStatusInterfaceSchedulerWeight,
       "cie1000QosStatusInterfaceSchedulerCutThrough": cie1000QosStatusInterfaceSchedulerCutThrough,
       "cie1000QosStatusInterfaceQbvGclOprTable": cie1000QosStatusInterfaceQbvGclOprTable,
       "cie1000QosStatusInterfaceQbvGclOprEntry": cie1000QosStatusInterfaceQbvGclOprEntry,
       "cie1000QosStatusInterfaceQbvGclOprIfIndex": cie1000QosStatusInterfaceQbvGclOprIfIndex,
       "cie1000QosStatusInterfaceQbvGclOprGclIndex": cie1000QosStatusInterfaceQbvGclOprGclIndex,
       "cie1000QosStatusInterfaceQbvGclOprGateState": cie1000QosStatusInterfaceQbvGclOprGateState,
       "cie1000QosStatusInterfaceQbvGclOprTimeInterval": cie1000QosStatusInterfaceQbvGclOprTimeInterval,
       "cie1000QosStatusInterfaceQbvOprStatusTable": cie1000QosStatusInterfaceQbvOprStatusTable,
       "cie1000QosStatusInterfaceQbvOprStatusEntry": cie1000QosStatusInterfaceQbvOprStatusEntry,
       "cie1000QosStatusInterfaceQbvOprStatusIfIndex": cie1000QosStatusInterfaceQbvOprStatusIfIndex,
       "cie1000QosStatusInterfaceQbvOprStatusOperGateStates": cie1000QosStatusInterfaceQbvOprStatusOperGateStates,
       "cie1000QosStatusInterfaceQbvOprStatusOperControlListLength": cie1000QosStatusInterfaceQbvOprStatusOperControlListLength,
       "cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeNumerator": cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeNumerator,
       "cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeDenominator": cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeDenominator,
       "cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeExtension": cie1000QosStatusInterfaceQbvOprStatusOperCycleTimeExtension,
       "cie1000QosStatusInterfaceQbvOprStatusOperBaseTime": cie1000QosStatusInterfaceQbvOprStatusOperBaseTime,
       "cie1000QosStatusInterfaceQbvOprStatusConfigChangeTime": cie1000QosStatusInterfaceQbvOprStatusConfigChangeTime,
       "cie1000QosStatusInterfaceQbvOprStatusTickGranularity": cie1000QosStatusInterfaceQbvOprStatusTickGranularity,
       "cie1000QosStatusInterfaceQbvOprStatusCurrentTime": cie1000QosStatusInterfaceQbvOprStatusCurrentTime,
       "cie1000QosStatusInterfaceQbvOprStatusConfigPending": cie1000QosStatusInterfaceQbvOprStatusConfigPending,
       "cie1000QosStatusInterfaceQbvOprStatusConfigChangeError": cie1000QosStatusInterfaceQbvOprStatusConfigChangeError,
       "cie1000QosStatusInterfaceQbvOprStatusSupportedListMax": cie1000QosStatusInterfaceQbvOprStatusSupportedListMax,
       "cie1000QosStatusQce": cie1000QosStatusQce,
       "cie1000QosStatusQceTable": cie1000QosStatusQceTable,
       "cie1000QosStatusQceEntry": cie1000QosStatusQceEntry,
       "cie1000QosStatusQceSwitchId": cie1000QosStatusQceSwitchId,
       "cie1000QosStatusQceIndex": cie1000QosStatusQceIndex,
       "cie1000QosStatusQceUserId": cie1000QosStatusQceUserId,
       "cie1000QosStatusQceQceId": cie1000QosStatusQceQceId,
       "cie1000QosStatusQceConflict": cie1000QosStatusQceConflict,
       "cie1000QosControl": cie1000QosControl,
       "cie1000QosControlQce": cie1000QosControlQce,
       "cie1000QosControlQceConflictResolve": cie1000QosControlQceConflictResolve,
       "cie1000QosMibConformance": cie1000QosMibConformance,
       "cie1000QosMibCompliances": cie1000QosMibCompliances,
       "cie1000QosMibCompliance": cie1000QosMibCompliance,
       "cie1000QosMibGroups": cie1000QosMibGroups,
       "cie1000QosCapabilitiesInfoGroup": cie1000QosCapabilitiesInfoGroup,
       "cie1000QosConfigGlobalsStormPolicersUnicastInfoGroup": cie1000QosConfigGlobalsStormPolicersUnicastInfoGroup,
       "cie1000QosConfigGlobalsStormPolicersMulticastInfoGroup": cie1000QosConfigGlobalsStormPolicersMulticastInfoGroup,
       "cie1000QosConfigGlobalsStormPolicersBroadcastInfoGroup": cie1000QosConfigGlobalsStormPolicersBroadcastInfoGroup,
       "cie1000QosConfigGlobalsWredTableInfoGroup": cie1000QosConfigGlobalsWredTableInfoGroup,
       "cie1000QosConfigGlobalsDscpTableInfoGroup": cie1000QosConfigGlobalsDscpTableInfoGroup,
       "cie1000QosConfigGlobalsCosToDscpTableInfoGroup": cie1000QosConfigGlobalsCosToDscpTableInfoGroup,
       "cie1000QosConfigInterfaceTableInfoGroup": cie1000QosConfigInterfaceTableInfoGroup,
       "cie1000QosConfigInterfaceTagToCosTableInfoGroup": cie1000QosConfigInterfaceTagToCosTableInfoGroup,
       "cie1000QosConfigInterfaceCosToTagTableInfoGroup": cie1000QosConfigInterfaceCosToTagTableInfoGroup,
       "cie1000QosConfigInterfacePolicerTableInfoGroup": cie1000QosConfigInterfacePolicerTableInfoGroup,
       "cie1000QosConfigInterfaceQueuePolicerTableInfoGroup": cie1000QosConfigInterfaceQueuePolicerTableInfoGroup,
       "cie1000QosConfigInterfaceShaperTableInfoGroup": cie1000QosConfigInterfaceShaperTableInfoGroup,
       "cie1000QosConfigInterfaceQueueShaperTableInfoGroup": cie1000QosConfigInterfaceQueueShaperTableInfoGroup,
       "cie1000QosConfigInterfaceSchedulerTableInfoGroup": cie1000QosConfigInterfaceSchedulerTableInfoGroup,
       "cie1000QosConfigInterfaceStormPolicerUnicastTableInfoGroup": cie1000QosConfigInterfaceStormPolicerUnicastTableInfoGroup,
       "cie1000QosConfigInterfaceStormPolicerBroadcastTableInfoGroup": cie1000QosConfigInterfaceStormPolicerBroadcastTableInfoGroup,
       "cie1000QosConfigInterfaceStormPolicerUnknownTableInfoGroup": cie1000QosConfigInterfaceStormPolicerUnknownTableInfoGroup,
       "cie1000QosConfigInterfaceQbvMaxSduTableInfoGroup": cie1000QosConfigInterfaceQbvMaxSduTableInfoGroup,
       "cie1000QosConfigInterfaceQbvGclAdminTableInfoGroup": cie1000QosConfigInterfaceQbvGclAdminTableInfoGroup,
       "cie1000QosConfigInterfaceQbvParamsTableInfoGroup": cie1000QosConfigInterfaceQbvParamsTableInfoGroup,
       "cie1000QosConfigQceTableInfoGroup": cie1000QosConfigQceTableInfoGroup,
       "cie1000QosConfigQceTableRowEditorInfoGroup": cie1000QosConfigQceTableRowEditorInfoGroup,
       "cie1000QosConfigQcePrecedenceTableInfoGroup": cie1000QosConfigQcePrecedenceTableInfoGroup,
       "cie1000QosConfigIngressMapTableInfoGroup": cie1000QosConfigIngressMapTableInfoGroup,
       "cie1000QosConfigIngressMapTableRowEditorInfoGroup": cie1000QosConfigIngressMapTableRowEditorInfoGroup,
       "cie1000QosConfigIngressMapPcpTableInfoGroup": cie1000QosConfigIngressMapPcpTableInfoGroup,
       "cie1000QosConfigIngressMapDscpTableInfoGroup": cie1000QosConfigIngressMapDscpTableInfoGroup,
       "cie1000QosConfigEgressMapTableInfoGroup": cie1000QosConfigEgressMapTableInfoGroup,
       "cie1000QosConfigEgressMapTableRowEditorInfoGroup": cie1000QosConfigEgressMapTableRowEditorInfoGroup,
       "cie1000QosConfigEgressMapCosidTableInfoGroup": cie1000QosConfigEgressMapCosidTableInfoGroup,
       "cie1000QosConfigEgressMapDscpTableInfoGroup": cie1000QosConfigEgressMapDscpTableInfoGroup,
       "cie1000QosStatusInterfaceTableInfoGroup": cie1000QosStatusInterfaceTableInfoGroup,
       "cie1000QosStatusInterfaceSchedulerTableInfoGroup": cie1000QosStatusInterfaceSchedulerTableInfoGroup,
       "cie1000QosStatusInterfaceQbvGclOprTableInfoGroup": cie1000QosStatusInterfaceQbvGclOprTableInfoGroup,
       "cie1000QosStatusInterfaceQbvOprStatusTableInfoGroup": cie1000QosStatusInterfaceQbvOprStatusTableInfoGroup,
       "cie1000QosStatusQceTableInfoGroup": cie1000QosStatusQceTableInfoGroup,
       "cie1000QosControlQceInfoGroup": cie1000QosControlQceInfoGroup}
)
