# SNMP MIB module (ME1200-EVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-EVC-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:30 2025
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

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(ME1200DisplayString,
 ME1200InterfaceIndex,
 ME1200PortList,
 ME1200RowEditorState,
 ME1200Unsigned16,
 ME1200Unsigned8) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString",
    "ME1200InterfaceIndex",
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

me1200EvcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62)
)
if mibBuilder.loadTexts:
    me1200EvcMib.setRevisions(
        ("2016-03-03 00:00",
         "2014-10-30 00:00",
         "2014-06-16 00:00",
         "2014-05-09 00:00",
         "2014-03-11 00:00",
         "2014-02-21 00:00",
         "2014-02-18 00:00",
         "2014-01-29 00:00",
         "2014-01-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



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



class ME1200evcDeiMode(TextualConvention, Integer32):
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
        *(("classified", 0),
          ("fixed", 1),
          ("dp", 2))
    )



class ME1200evcDirection(TextualConvention, Integer32):
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
        *(("both", 0),
          ("uniToNni", 1),
          ("nniToUni", 2))
    )



class ME1200evcEceL2cpMode(TextualConvention, Integer32):
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
        *(("forward", 0),
          ("discard", 1),
          ("peer", 2),
          ("tunnel", 3))
    )



class ME1200evcFrameType(TextualConvention, Integer32):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("etype", 1),
          ("llc", 2),
          ("snap", 3),
          ("l2cp", 4),
          ("ipv4", 5),
          ("ipv6", 6))
    )



class ME1200evcInnerTagType(TextualConvention, Integer32):
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
          ("cTagged", 1),
          ("sTagged", 2),
          ("sCustomTagged", 3))
    )



class ME1200evcL2cpDmac(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("custom", 0),
          ("cisco", 1))
    )



class ME1200evcL2cpMode(TextualConvention, Integer32):
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
        *(("forward", 0),
          ("discard", 1),
          ("peer", 2))
    )



class ME1200evcL2cpType(TextualConvention, Integer32):
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("stp", 1),
          ("pause", 2),
          ("lacp", 3),
          ("lamp", 4),
          ("loam", 5),
          ("dot1x", 6),
          ("elmi", 7),
          ("pb", 8),
          ("pbGvrp", 9),
          ("lldp", 10),
          ("gmrp", 11),
          ("gvrp", 12),
          ("uld", 13),
          ("pagp", 14),
          ("pvst", 15),
          ("ciscoVlan", 16),
          ("cdp", 17),
          ("vtp", 18),
          ("dtp", 19),
          ("ciscoStp", 20),
          ("ciscoCfm", 21))
    )



class ME1200evcPcpMode(TextualConvention, Integer32):
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
        *(("classified", 0),
          ("fixed", 1),
          ("mapped", 2))
    )



class ME1200evcPolicerMode(TextualConvention, Integer32):
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
        *(("coupled", 0),
          ("aware", 1),
          ("blind", 2))
    )



class ME1200evcPolicerOp(TextualConvention, Integer32):
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
          ("none", 1),
          ("discard", 2),
          ("evc", 3))
    )



class ME1200evcPolicerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mef", 0),
          ("single", 1))
    )



class ME1200evcPopTag(TextualConvention, Integer32):
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
        *(("zero", 0),
          ("one", 1),
          ("two", 2))
    )



class ME1200evcRuleType(TextualConvention, Integer32):
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
        *(("both", 0),
          ("rx", 1),
          ("tx", 2))
    )



class ME1200evcTxLookup(TextualConvention, Integer32):
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
        *(("vid", 0),
          ("vidPcp", 1),
          ("isdx", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200EvcMibObjects_ObjectIdentity = ObjectIdentity
me1200EvcMibObjects = _Me1200EvcMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1)
)
_Me1200EvcCapabilities_ObjectIdentity = ObjectIdentity
me1200EvcCapabilities = _Me1200EvcCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1)
)
_Me1200EvcCapabilitiesPolicerMax_Type = Unsigned32
_Me1200EvcCapabilitiesPolicerMax_Object = MibScalar
me1200EvcCapabilitiesPolicerMax = _Me1200EvcCapabilitiesPolicerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 1),
    _Me1200EvcCapabilitiesPolicerMax_Type()
)
me1200EvcCapabilitiesPolicerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesPolicerMax.setStatus("current")
_Me1200EvcCapabilitiesEvcMax_Type = Unsigned32
_Me1200EvcCapabilitiesEvcMax_Object = MibScalar
me1200EvcCapabilitiesEvcMax = _Me1200EvcCapabilitiesEvcMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 2),
    _Me1200EvcCapabilitiesEvcMax_Type()
)
me1200EvcCapabilitiesEvcMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesEvcMax.setStatus("current")
_Me1200EvcCapabilitiesEceMax_Type = Unsigned32
_Me1200EvcCapabilitiesEceMax_Object = MibScalar
me1200EvcCapabilitiesEceMax = _Me1200EvcCapabilitiesEceMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 3),
    _Me1200EvcCapabilitiesEceMax_Type()
)
me1200EvcCapabilitiesEceMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesEceMax.setStatus("current")
_Me1200EvcCapabilitiesHasPortDeiColoring_Type = TruthValue
_Me1200EvcCapabilitiesHasPortDeiColoring_Object = MibScalar
me1200EvcCapabilitiesHasPortDeiColoring = _Me1200EvcCapabilitiesHasPortDeiColoring_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 100),
    _Me1200EvcCapabilitiesHasPortDeiColoring_Type()
)
me1200EvcCapabilitiesHasPortDeiColoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasPortDeiColoring.setStatus("current")
_Me1200EvcCapabilitiesHasPortInnerTag_Type = TruthValue
_Me1200EvcCapabilitiesHasPortInnerTag_Object = MibScalar
me1200EvcCapabilitiesHasPortInnerTag = _Me1200EvcCapabilitiesHasPortInnerTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 101),
    _Me1200EvcCapabilitiesHasPortInnerTag_Type()
)
me1200EvcCapabilitiesHasPortInnerTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasPortInnerTag.setStatus("current")
_Me1200EvcCapabilitiesHasPortAddrMode_Type = TruthValue
_Me1200EvcCapabilitiesHasPortAddrMode_Object = MibScalar
me1200EvcCapabilitiesHasPortAddrMode = _Me1200EvcCapabilitiesHasPortAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 102),
    _Me1200EvcCapabilitiesHasPortAddrMode_Type()
)
me1200EvcCapabilitiesHasPortAddrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasPortAddrMode.setStatus("current")
_Me1200EvcCapabilitiesHasPortKey_Type = TruthValue
_Me1200EvcCapabilitiesHasPortKey_Object = MibScalar
me1200EvcCapabilitiesHasPortKey = _Me1200EvcCapabilitiesHasPortKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 103),
    _Me1200EvcCapabilitiesHasPortKey_Type()
)
me1200EvcCapabilitiesHasPortKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasPortKey.setStatus("current")
_Me1200EvcCapabilitiesHasPolicerColorBlind_Type = TruthValue
_Me1200EvcCapabilitiesHasPolicerColorBlind_Object = MibScalar
me1200EvcCapabilitiesHasPolicerColorBlind = _Me1200EvcCapabilitiesHasPolicerColorBlind_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 200),
    _Me1200EvcCapabilitiesHasPolicerColorBlind_Type()
)
me1200EvcCapabilitiesHasPolicerColorBlind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasPolicerColorBlind.setStatus("current")
_Me1200EvcCapabilitiesHasEvcPolicer_Type = TruthValue
_Me1200EvcCapabilitiesHasEvcPolicer_Object = MibScalar
me1200EvcCapabilitiesHasEvcPolicer = _Me1200EvcCapabilitiesHasEvcPolicer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 300),
    _Me1200EvcCapabilitiesHasEvcPolicer_Type()
)
me1200EvcCapabilitiesHasEvcPolicer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEvcPolicer.setStatus("current")
_Me1200EvcCapabilitiesHasEvcUniVid_Type = TruthValue
_Me1200EvcCapabilitiesHasEvcUniVid_Object = MibScalar
me1200EvcCapabilitiesHasEvcUniVid = _Me1200EvcCapabilitiesHasEvcUniVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 301),
    _Me1200EvcCapabilitiesHasEvcUniVid_Type()
)
me1200EvcCapabilitiesHasEvcUniVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEvcUniVid.setStatus("current")
_Me1200EvcCapabilitiesHasEvcItAdd_Type = TruthValue
_Me1200EvcCapabilitiesHasEvcItAdd_Object = MibScalar
me1200EvcCapabilitiesHasEvcItAdd = _Me1200EvcCapabilitiesHasEvcItAdd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 302),
    _Me1200EvcCapabilitiesHasEvcItAdd_Type()
)
me1200EvcCapabilitiesHasEvcItAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEvcItAdd.setStatus("current")
_Me1200EvcCapabilitiesHasEvcETree_Type = TruthValue
_Me1200EvcCapabilitiesHasEvcETree_Object = MibScalar
me1200EvcCapabilitiesHasEvcETree = _Me1200EvcCapabilitiesHasEvcETree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 303),
    _Me1200EvcCapabilitiesHasEvcETree_Type()
)
me1200EvcCapabilitiesHasEvcETree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEvcETree.setStatus("current")
_Me1200EvcCapabilitiesHasEvcName_Type = TruthValue
_Me1200EvcCapabilitiesHasEvcName_Object = MibScalar
me1200EvcCapabilitiesHasEvcName = _Me1200EvcCapabilitiesHasEvcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 304),
    _Me1200EvcCapabilitiesHasEvcName_Type()
)
me1200EvcCapabilitiesHasEvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEvcName.setStatus("current")
_Me1200EvcCapabilitiesHasEceAdvLookup_Type = TruthValue
_Me1200EvcCapabilitiesHasEceAdvLookup_Object = MibScalar
me1200EvcCapabilitiesHasEceAdvLookup = _Me1200EvcCapabilitiesHasEceAdvLookup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 400),
    _Me1200EvcCapabilitiesHasEceAdvLookup_Type()
)
me1200EvcCapabilitiesHasEceAdvLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceAdvLookup.setStatus("current")
_Me1200EvcCapabilitiesHasEceDestMacType_Type = TruthValue
_Me1200EvcCapabilitiesHasEceDestMacType_Object = MibScalar
me1200EvcCapabilitiesHasEceDestMacType = _Me1200EvcCapabilitiesHasEceDestMacType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 401),
    _Me1200EvcCapabilitiesHasEceDestMacType_Type()
)
me1200EvcCapabilitiesHasEceDestMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceDestMacType.setStatus("current")
_Me1200EvcCapabilitiesHasEceDestMac_Type = TruthValue
_Me1200EvcCapabilitiesHasEceDestMac_Object = MibScalar
me1200EvcCapabilitiesHasEceDestMac = _Me1200EvcCapabilitiesHasEceDestMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 402),
    _Me1200EvcCapabilitiesHasEceDestMac_Type()
)
me1200EvcCapabilitiesHasEceDestMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceDestMac.setStatus("current")
_Me1200EvcCapabilitiesHasEceSrcMac_Type = TruthValue
_Me1200EvcCapabilitiesHasEceSrcMac_Object = MibScalar
me1200EvcCapabilitiesHasEceSrcMac = _Me1200EvcCapabilitiesHasEceSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 403),
    _Me1200EvcCapabilitiesHasEceSrcMac_Type()
)
me1200EvcCapabilitiesHasEceSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceSrcMac.setStatus("current")
_Me1200EvcCapabilitiesHasEceInnerTag_Type = TruthValue
_Me1200EvcCapabilitiesHasEceInnerTag_Object = MibScalar
me1200EvcCapabilitiesHasEceInnerTag = _Me1200EvcCapabilitiesHasEceInnerTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 404),
    _Me1200EvcCapabilitiesHasEceInnerTag_Type()
)
me1200EvcCapabilitiesHasEceInnerTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceInnerTag.setStatus("current")
_Me1200EvcCapabilitiesHasEceEtype_Type = TruthValue
_Me1200EvcCapabilitiesHasEceEtype_Object = MibScalar
me1200EvcCapabilitiesHasEceEtype = _Me1200EvcCapabilitiesHasEceEtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 405),
    _Me1200EvcCapabilitiesHasEceEtype_Type()
)
me1200EvcCapabilitiesHasEceEtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceEtype.setStatus("current")
_Me1200EvcCapabilitiesHasEceLlc_Type = TruthValue
_Me1200EvcCapabilitiesHasEceLlc_Object = MibScalar
me1200EvcCapabilitiesHasEceLlc = _Me1200EvcCapabilitiesHasEceLlc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 406),
    _Me1200EvcCapabilitiesHasEceLlc_Type()
)
me1200EvcCapabilitiesHasEceLlc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceLlc.setStatus("current")
_Me1200EvcCapabilitiesHasEceSnap_Type = TruthValue
_Me1200EvcCapabilitiesHasEceSnap_Object = MibScalar
me1200EvcCapabilitiesHasEceSnap = _Me1200EvcCapabilitiesHasEceSnap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 407),
    _Me1200EvcCapabilitiesHasEceSnap_Type()
)
me1200EvcCapabilitiesHasEceSnap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceSnap.setStatus("current")
_Me1200EvcCapabilitiesHasEceL2cp_Type = TruthValue
_Me1200EvcCapabilitiesHasEceL2cp_Object = MibScalar
me1200EvcCapabilitiesHasEceL2cp = _Me1200EvcCapabilitiesHasEceL2cp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 408),
    _Me1200EvcCapabilitiesHasEceL2cp_Type()
)
me1200EvcCapabilitiesHasEceL2cp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceL2cp.setStatus("current")
_Me1200EvcCapabilitiesHasEceIpv4Fragment_Type = TruthValue
_Me1200EvcCapabilitiesHasEceIpv4Fragment_Object = MibScalar
me1200EvcCapabilitiesHasEceIpv4Fragment = _Me1200EvcCapabilitiesHasEceIpv4Fragment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 409),
    _Me1200EvcCapabilitiesHasEceIpv4Fragment_Type()
)
me1200EvcCapabilitiesHasEceIpv4Fragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceIpv4Fragment.setStatus("current")
_Me1200EvcCapabilitiesHasEceIpProto_Type = TruthValue
_Me1200EvcCapabilitiesHasEceIpProto_Object = MibScalar
me1200EvcCapabilitiesHasEceIpProto = _Me1200EvcCapabilitiesHasEceIpProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 410),
    _Me1200EvcCapabilitiesHasEceIpProto_Type()
)
me1200EvcCapabilitiesHasEceIpProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceIpProto.setStatus("current")
_Me1200EvcCapabilitiesHasEceSrcIp_Type = TruthValue
_Me1200EvcCapabilitiesHasEceSrcIp_Object = MibScalar
me1200EvcCapabilitiesHasEceSrcIp = _Me1200EvcCapabilitiesHasEceSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 411),
    _Me1200EvcCapabilitiesHasEceSrcIp_Type()
)
me1200EvcCapabilitiesHasEceSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceSrcIp.setStatus("current")
_Me1200EvcCapabilitiesHasEceDestIp_Type = TruthValue
_Me1200EvcCapabilitiesHasEceDestIp_Object = MibScalar
me1200EvcCapabilitiesHasEceDestIp = _Me1200EvcCapabilitiesHasEceDestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 412),
    _Me1200EvcCapabilitiesHasEceDestIp_Type()
)
me1200EvcCapabilitiesHasEceDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceDestIp.setStatus("current")
_Me1200EvcCapabilitiesHasEceSrcPort_Type = TruthValue
_Me1200EvcCapabilitiesHasEceSrcPort_Object = MibScalar
me1200EvcCapabilitiesHasEceSrcPort = _Me1200EvcCapabilitiesHasEceSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 413),
    _Me1200EvcCapabilitiesHasEceSrcPort_Type()
)
me1200EvcCapabilitiesHasEceSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceSrcPort.setStatus("current")
_Me1200EvcCapabilitiesHasEceDestPort_Type = TruthValue
_Me1200EvcCapabilitiesHasEceDestPort_Object = MibScalar
me1200EvcCapabilitiesHasEceDestPort = _Me1200EvcCapabilitiesHasEceDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 414),
    _Me1200EvcCapabilitiesHasEceDestPort_Type()
)
me1200EvcCapabilitiesHasEceDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceDestPort.setStatus("current")
_Me1200EvcCapabilitiesHasEceRuleType_Type = TruthValue
_Me1200EvcCapabilitiesHasEceRuleType_Object = MibScalar
me1200EvcCapabilitiesHasEceRuleType = _Me1200EvcCapabilitiesHasEceRuleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 415),
    _Me1200EvcCapabilitiesHasEceRuleType_Type()
)
me1200EvcCapabilitiesHasEceRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceRuleType.setStatus("current")
_Me1200EvcCapabilitiesHasEceTxLookup_Type = TruthValue
_Me1200EvcCapabilitiesHasEceTxLookup_Object = MibScalar
me1200EvcCapabilitiesHasEceTxLookup = _Me1200EvcCapabilitiesHasEceTxLookup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 416),
    _Me1200EvcCapabilitiesHasEceTxLookup_Type()
)
me1200EvcCapabilitiesHasEceTxLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceTxLookup.setStatus("current")
_Me1200EvcCapabilitiesHasEceOtAddVid_Type = TruthValue
_Me1200EvcCapabilitiesHasEceOtAddVid_Object = MibScalar
me1200EvcCapabilitiesHasEceOtAddVid = _Me1200EvcCapabilitiesHasEceOtAddVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 417),
    _Me1200EvcCapabilitiesHasEceOtAddVid_Type()
)
me1200EvcCapabilitiesHasEceOtAddVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceOtAddVid.setStatus("current")
_Me1200EvcCapabilitiesHasEcePcpMode_Type = TruthValue
_Me1200EvcCapabilitiesHasEcePcpMode_Object = MibScalar
me1200EvcCapabilitiesHasEcePcpMode = _Me1200EvcCapabilitiesHasEcePcpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 418),
    _Me1200EvcCapabilitiesHasEcePcpMode_Type()
)
me1200EvcCapabilitiesHasEcePcpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEcePcpMode.setStatus("current")
_Me1200EvcCapabilitiesHasEcePcpDeiPreserve_Type = TruthValue
_Me1200EvcCapabilitiesHasEcePcpDeiPreserve_Object = MibScalar
me1200EvcCapabilitiesHasEcePcpDeiPreserve = _Me1200EvcCapabilitiesHasEcePcpDeiPreserve_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 419),
    _Me1200EvcCapabilitiesHasEcePcpDeiPreserve_Type()
)
me1200EvcCapabilitiesHasEcePcpDeiPreserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEcePcpDeiPreserve.setStatus("current")
_Me1200EvcCapabilitiesHasEceDeiMode_Type = TruthValue
_Me1200EvcCapabilitiesHasEceDeiMode_Object = MibScalar
me1200EvcCapabilitiesHasEceDeiMode = _Me1200EvcCapabilitiesHasEceDeiMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 420),
    _Me1200EvcCapabilitiesHasEceDeiMode_Type()
)
me1200EvcCapabilitiesHasEceDeiMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceDeiMode.setStatus("current")
_Me1200EvcCapabilitiesHasEceItAdd_Type = TruthValue
_Me1200EvcCapabilitiesHasEceItAdd_Object = MibScalar
me1200EvcCapabilitiesHasEceItAdd = _Me1200EvcCapabilitiesHasEceItAdd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 421),
    _Me1200EvcCapabilitiesHasEceItAdd_Type()
)
me1200EvcCapabilitiesHasEceItAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceItAdd.setStatus("current")
_Me1200EvcCapabilitiesHasEcePolicer_Type = TruthValue
_Me1200EvcCapabilitiesHasEcePolicer_Object = MibScalar
me1200EvcCapabilitiesHasEcePolicer = _Me1200EvcCapabilitiesHasEcePolicer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 422),
    _Me1200EvcCapabilitiesHasEcePolicer_Type()
)
me1200EvcCapabilitiesHasEcePolicer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEcePolicer.setStatus("current")
_Me1200EvcCapabilitiesHasEceCos_Type = TruthValue
_Me1200EvcCapabilitiesHasEceCos_Object = MibScalar
me1200EvcCapabilitiesHasEceCos = _Me1200EvcCapabilitiesHasEceCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 423),
    _Me1200EvcCapabilitiesHasEceCos_Type()
)
me1200EvcCapabilitiesHasEceCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceCos.setStatus("current")
_Me1200EvcCapabilitiesHasEceDp_Type = TruthValue
_Me1200EvcCapabilitiesHasEceDp_Object = MibScalar
me1200EvcCapabilitiesHasEceDp = _Me1200EvcCapabilitiesHasEceDp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 424),
    _Me1200EvcCapabilitiesHasEceDp_Type()
)
me1200EvcCapabilitiesHasEceDp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEceDp.setStatus("current")
_Me1200EvcCapabilitiesHasEvcPortHqos_Type = TruthValue
_Me1200EvcCapabilitiesHasEvcPortHqos_Object = MibScalar
me1200EvcCapabilitiesHasEvcPortHqos = _Me1200EvcCapabilitiesHasEvcPortHqos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 500),
    _Me1200EvcCapabilitiesHasEvcPortHqos_Type()
)
me1200EvcCapabilitiesHasEvcPortHqos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEvcPortHqos.setStatus("current")
_Me1200EvcCapabilitiesHasEvcPortCounters_Type = TruthValue
_Me1200EvcCapabilitiesHasEvcPortCounters_Object = MibScalar
me1200EvcCapabilitiesHasEvcPortCounters = _Me1200EvcCapabilitiesHasEvcPortCounters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 1, 501),
    _Me1200EvcCapabilitiesHasEvcPortCounters_Type()
)
me1200EvcCapabilitiesHasEvcPortCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesHasEvcPortCounters.setStatus("current")
_Me1200EvcConfig_ObjectIdentity = ObjectIdentity
me1200EvcConfig = _Me1200EvcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2)
)
_Me1200EvcConfigInterface_ObjectIdentity = ObjectIdentity
me1200EvcConfigInterface = _Me1200EvcConfigInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 2)
)
_Me1200EvcConfigInterfaceTable_Object = MibTable
me1200EvcConfigInterfaceTable = _Me1200EvcConfigInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    me1200EvcConfigInterfaceTable.setStatus("current")
_Me1200EvcConfigInterfaceEntry_Object = MibTableRow
me1200EvcConfigInterfaceEntry = _Me1200EvcConfigInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 2, 1, 1)
)
me1200EvcConfigInterfaceEntry.setIndexNames(
    (0, "ME1200-EVC-MIB", "me1200EvcConfigInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    me1200EvcConfigInterfaceEntry.setStatus("current")
_Me1200EvcConfigInterfaceIfIndex_Type = ME1200InterfaceIndex
_Me1200EvcConfigInterfaceIfIndex_Object = MibTableColumn
me1200EvcConfigInterfaceIfIndex = _Me1200EvcConfigInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 2, 1, 1, 1),
    _Me1200EvcConfigInterfaceIfIndex_Type()
)
me1200EvcConfigInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcConfigInterfaceIfIndex.setStatus("current")
_Me1200EvcConfigInterfaceKey_Type = ME1200VcapKeyType
_Me1200EvcConfigInterfaceKey_Object = MibTableColumn
me1200EvcConfigInterfaceKey = _Me1200EvcConfigInterfaceKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 2, 1, 1, 2),
    _Me1200EvcConfigInterfaceKey_Type()
)
me1200EvcConfigInterfaceKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigInterfaceKey.setStatus("current")
_Me1200EvcConfigInterfaceKeyAdv_Type = ME1200VcapKeyType
_Me1200EvcConfigInterfaceKeyAdv_Object = MibTableColumn
me1200EvcConfigInterfaceKeyAdv = _Me1200EvcConfigInterfaceKeyAdv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 2, 1, 1, 3),
    _Me1200EvcConfigInterfaceKeyAdv_Type()
)
me1200EvcConfigInterfaceKeyAdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigInterfaceKeyAdv.setStatus("current")
_Me1200EvcConfigInterfaceAddrMode_Type = TruthValue
_Me1200EvcConfigInterfaceAddrMode_Object = MibTableColumn
me1200EvcConfigInterfaceAddrMode = _Me1200EvcConfigInterfaceAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 2, 1, 1, 4),
    _Me1200EvcConfigInterfaceAddrMode_Type()
)
me1200EvcConfigInterfaceAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigInterfaceAddrMode.setStatus("current")
_Me1200EvcConfigInterfaceAddrModeAdv_Type = TruthValue
_Me1200EvcConfigInterfaceAddrModeAdv_Object = MibTableColumn
me1200EvcConfigInterfaceAddrModeAdv = _Me1200EvcConfigInterfaceAddrModeAdv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 2, 1, 1, 5),
    _Me1200EvcConfigInterfaceAddrModeAdv_Type()
)
me1200EvcConfigInterfaceAddrModeAdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigInterfaceAddrModeAdv.setStatus("current")
_Me1200EvcConfigInterfaceDeiColoring_Type = TruthValue
_Me1200EvcConfigInterfaceDeiColoring_Object = MibTableColumn
me1200EvcConfigInterfaceDeiColoring = _Me1200EvcConfigInterfaceDeiColoring_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 2, 1, 1, 6),
    _Me1200EvcConfigInterfaceDeiColoring_Type()
)
me1200EvcConfigInterfaceDeiColoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigInterfaceDeiColoring.setStatus("current")
_Me1200EvcConfigInterfaceInnerTag_Type = TruthValue
_Me1200EvcConfigInterfaceInnerTag_Object = MibTableColumn
me1200EvcConfigInterfaceInnerTag = _Me1200EvcConfigInterfaceInnerTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 2, 1, 1, 7),
    _Me1200EvcConfigInterfaceInnerTag_Type()
)
me1200EvcConfigInterfaceInnerTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigInterfaceInnerTag.setStatus("current")
_Me1200EvcConfigInterfaceL2cpTable_Object = MibTable
me1200EvcConfigInterfaceL2cpTable = _Me1200EvcConfigInterfaceL2cpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    me1200EvcConfigInterfaceL2cpTable.setStatus("current")
_Me1200EvcConfigInterfaceL2cpEntry_Object = MibTableRow
me1200EvcConfigInterfaceL2cpEntry = _Me1200EvcConfigInterfaceL2cpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 2, 2, 1)
)
me1200EvcConfigInterfaceL2cpEntry.setIndexNames(
    (0, "ME1200-EVC-MIB", "me1200EvcConfigInterfaceL2cpIfIndex"),
    (0, "ME1200-EVC-MIB", "me1200EvcConfigInterfaceL2cpL2cpId"),
)
if mibBuilder.loadTexts:
    me1200EvcConfigInterfaceL2cpEntry.setStatus("current")
_Me1200EvcConfigInterfaceL2cpIfIndex_Type = ME1200InterfaceIndex
_Me1200EvcConfigInterfaceL2cpIfIndex_Object = MibTableColumn
me1200EvcConfigInterfaceL2cpIfIndex = _Me1200EvcConfigInterfaceL2cpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 2, 2, 1, 1),
    _Me1200EvcConfigInterfaceL2cpIfIndex_Type()
)
me1200EvcConfigInterfaceL2cpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcConfigInterfaceL2cpIfIndex.setStatus("current")


class _Me1200EvcConfigInterfaceL2cpL2cpId_Type(Integer32):
    """Custom type me1200EvcConfigInterfaceL2cpL2cpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Me1200EvcConfigInterfaceL2cpL2cpId_Type.__name__ = "Integer32"
_Me1200EvcConfigInterfaceL2cpL2cpId_Object = MibTableColumn
me1200EvcConfigInterfaceL2cpL2cpId = _Me1200EvcConfigInterfaceL2cpL2cpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 2, 2, 1, 2),
    _Me1200EvcConfigInterfaceL2cpL2cpId_Type()
)
me1200EvcConfigInterfaceL2cpL2cpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcConfigInterfaceL2cpL2cpId.setStatus("current")
_Me1200EvcConfigInterfaceL2cpL2cpMode_Type = ME1200evcL2cpMode
_Me1200EvcConfigInterfaceL2cpL2cpMode_Object = MibTableColumn
me1200EvcConfigInterfaceL2cpL2cpMode = _Me1200EvcConfigInterfaceL2cpL2cpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 2, 2, 1, 3),
    _Me1200EvcConfigInterfaceL2cpL2cpMode_Type()
)
me1200EvcConfigInterfaceL2cpL2cpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigInterfaceL2cpL2cpMode.setStatus("current")
_Me1200EvcConfigPolicerTable_Object = MibTable
me1200EvcConfigPolicerTable = _Me1200EvcConfigPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 3)
)
if mibBuilder.loadTexts:
    me1200EvcConfigPolicerTable.setStatus("current")
_Me1200EvcConfigPolicerEntry_Object = MibTableRow
me1200EvcConfigPolicerEntry = _Me1200EvcConfigPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 3, 1)
)
me1200EvcConfigPolicerEntry.setIndexNames(
    (0, "ME1200-EVC-MIB", "me1200EvcConfigPolicerPolicerId"),
)
if mibBuilder.loadTexts:
    me1200EvcConfigPolicerEntry.setStatus("current")


class _Me1200EvcConfigPolicerPolicerId_Type(Integer32):
    """Custom type me1200EvcConfigPolicerPolicerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Me1200EvcConfigPolicerPolicerId_Type.__name__ = "Integer32"
_Me1200EvcConfigPolicerPolicerId_Object = MibTableColumn
me1200EvcConfigPolicerPolicerId = _Me1200EvcConfigPolicerPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 3, 1, 1),
    _Me1200EvcConfigPolicerPolicerId_Type()
)
me1200EvcConfigPolicerPolicerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcConfigPolicerPolicerId.setStatus("current")
_Me1200EvcConfigPolicerEnable_Type = TruthValue
_Me1200EvcConfigPolicerEnable_Object = MibTableColumn
me1200EvcConfigPolicerEnable = _Me1200EvcConfigPolicerEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 3, 1, 2),
    _Me1200EvcConfigPolicerEnable_Type()
)
me1200EvcConfigPolicerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigPolicerEnable.setStatus("current")
_Me1200EvcConfigPolicerPolicerType_Type = ME1200evcPolicerType
_Me1200EvcConfigPolicerPolicerType_Object = MibTableColumn
me1200EvcConfigPolicerPolicerType = _Me1200EvcConfigPolicerPolicerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 3, 1, 3),
    _Me1200EvcConfigPolicerPolicerType_Type()
)
me1200EvcConfigPolicerPolicerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigPolicerPolicerType.setStatus("current")
_Me1200EvcConfigPolicerPolicerMode_Type = ME1200evcPolicerMode
_Me1200EvcConfigPolicerPolicerMode_Object = MibTableColumn
me1200EvcConfigPolicerPolicerMode = _Me1200EvcConfigPolicerPolicerMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 3, 1, 4),
    _Me1200EvcConfigPolicerPolicerMode_Type()
)
me1200EvcConfigPolicerPolicerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigPolicerPolicerMode.setStatus("current")
_Me1200EvcConfigPolicerLineRate_Type = TruthValue
_Me1200EvcConfigPolicerLineRate_Object = MibTableColumn
me1200EvcConfigPolicerLineRate = _Me1200EvcConfigPolicerLineRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 3, 1, 5),
    _Me1200EvcConfigPolicerLineRate_Type()
)
me1200EvcConfigPolicerLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigPolicerLineRate.setStatus("current")
_Me1200EvcConfigPolicerCir_Type = Unsigned32
_Me1200EvcConfigPolicerCir_Object = MibTableColumn
me1200EvcConfigPolicerCir = _Me1200EvcConfigPolicerCir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 3, 1, 6),
    _Me1200EvcConfigPolicerCir_Type()
)
me1200EvcConfigPolicerCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigPolicerCir.setStatus("current")
_Me1200EvcConfigPolicerCbs_Type = Unsigned32
_Me1200EvcConfigPolicerCbs_Object = MibTableColumn
me1200EvcConfigPolicerCbs = _Me1200EvcConfigPolicerCbs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 3, 1, 7),
    _Me1200EvcConfigPolicerCbs_Type()
)
me1200EvcConfigPolicerCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigPolicerCbs.setStatus("current")
_Me1200EvcConfigPolicerEir_Type = Unsigned32
_Me1200EvcConfigPolicerEir_Object = MibTableColumn
me1200EvcConfigPolicerEir = _Me1200EvcConfigPolicerEir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 3, 1, 8),
    _Me1200EvcConfigPolicerEir_Type()
)
me1200EvcConfigPolicerEir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigPolicerEir.setStatus("current")
_Me1200EvcConfigPolicerEbs_Type = Unsigned32
_Me1200EvcConfigPolicerEbs_Object = MibTableColumn
me1200EvcConfigPolicerEbs = _Me1200EvcConfigPolicerEbs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 3, 1, 9),
    _Me1200EvcConfigPolicerEbs_Type()
)
me1200EvcConfigPolicerEbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigPolicerEbs.setStatus("current")
_Me1200EvcConfigEvc_ObjectIdentity = ObjectIdentity
me1200EvcConfigEvc = _Me1200EvcConfigEvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4)
)
_Me1200EvcConfigEvcTable_Object = MibTable
me1200EvcConfigEvcTable = _Me1200EvcConfigEvcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTable.setStatus("current")
_Me1200EvcConfigEvcEntry_Object = MibTableRow
me1200EvcConfigEvcEntry = _Me1200EvcConfigEvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1)
)
me1200EvcConfigEvcEntry.setIndexNames(
    (0, "ME1200-EVC-MIB", "me1200EvcConfigEvcEvcId"),
)
if mibBuilder.loadTexts:
    me1200EvcConfigEvcEntry.setStatus("current")


class _Me1200EvcConfigEvcEvcId_Type(Integer32):
    """Custom type me1200EvcConfigEvcEvcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Me1200EvcConfigEvcEvcId_Type.__name__ = "Integer32"
_Me1200EvcConfigEvcEvcId_Object = MibTableColumn
me1200EvcConfigEvcEvcId = _Me1200EvcConfigEvcEvcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 1),
    _Me1200EvcConfigEvcEvcId_Type()
)
me1200EvcConfigEvcEvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcEvcId.setStatus("current")
_Me1200EvcConfigEvcVid_Type = ME1200Unsigned16
_Me1200EvcConfigEvcVid_Object = MibTableColumn
me1200EvcConfigEvcVid = _Me1200EvcConfigEvcVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 2),
    _Me1200EvcConfigEvcVid_Type()
)
me1200EvcConfigEvcVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcVid.setStatus("current")
_Me1200EvcConfigEvcIvid_Type = ME1200Unsigned16
_Me1200EvcConfigEvcIvid_Object = MibTableColumn
me1200EvcConfigEvcIvid = _Me1200EvcConfigEvcIvid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 3),
    _Me1200EvcConfigEvcIvid_Type()
)
me1200EvcConfigEvcIvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcIvid.setStatus("current")
_Me1200EvcConfigEvcNniPortList_Type = ME1200PortList
_Me1200EvcConfigEvcNniPortList_Object = MibTableColumn
me1200EvcConfigEvcNniPortList = _Me1200EvcConfigEvcNniPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 4),
    _Me1200EvcConfigEvcNniPortList_Type()
)
me1200EvcConfigEvcNniPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcNniPortList.setStatus("current")
_Me1200EvcConfigEvcLearning_Type = TruthValue
_Me1200EvcConfigEvcLearning_Object = MibTableColumn
me1200EvcConfigEvcLearning = _Me1200EvcConfigEvcLearning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 5),
    _Me1200EvcConfigEvcLearning_Type()
)
me1200EvcConfigEvcLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcLearning.setStatus("current")
_Me1200EvcConfigEvcPolicerOp_Type = ME1200evcPolicerOp
_Me1200EvcConfigEvcPolicerOp_Object = MibTableColumn
me1200EvcConfigEvcPolicerOp = _Me1200EvcConfigEvcPolicerOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 6),
    _Me1200EvcConfigEvcPolicerOp_Type()
)
me1200EvcConfigEvcPolicerOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcPolicerOp.setStatus("current")
_Me1200EvcConfigEvcPolicerId_Type = ME1200Unsigned16
_Me1200EvcConfigEvcPolicerId_Object = MibTableColumn
me1200EvcConfigEvcPolicerId = _Me1200EvcConfigEvcPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 7),
    _Me1200EvcConfigEvcPolicerId_Type()
)
me1200EvcConfigEvcPolicerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcPolicerId.setStatus("current")
_Me1200EvcConfigEvcUniVid_Type = ME1200Unsigned16
_Me1200EvcConfigEvcUniVid_Object = MibTableColumn
me1200EvcConfigEvcUniVid = _Me1200EvcConfigEvcUniVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 8),
    _Me1200EvcConfigEvcUniVid_Type()
)
me1200EvcConfigEvcUniVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcUniVid.setStatus("current")
_Me1200EvcConfigEvcItAddType_Type = ME1200evcInnerTagType
_Me1200EvcConfigEvcItAddType_Object = MibTableColumn
me1200EvcConfigEvcItAddType = _Me1200EvcConfigEvcItAddType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 9),
    _Me1200EvcConfigEvcItAddType_Type()
)
me1200EvcConfigEvcItAddType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcItAddType.setStatus("current")
_Me1200EvcConfigEvcItInnerVid_Type = TruthValue
_Me1200EvcConfigEvcItInnerVid_Object = MibTableColumn
me1200EvcConfigEvcItInnerVid = _Me1200EvcConfigEvcItInnerVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 10),
    _Me1200EvcConfigEvcItInnerVid_Type()
)
me1200EvcConfigEvcItInnerVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcItInnerVid.setStatus("current")
_Me1200EvcConfigEvcItAddVid_Type = ME1200Unsigned16
_Me1200EvcConfigEvcItAddVid_Object = MibTableColumn
me1200EvcConfigEvcItAddVid = _Me1200EvcConfigEvcItAddVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 11),
    _Me1200EvcConfigEvcItAddVid_Type()
)
me1200EvcConfigEvcItAddVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcItAddVid.setStatus("current")
_Me1200EvcConfigEvcItAddPcpDeiPreserve_Type = TruthValue
_Me1200EvcConfigEvcItAddPcpDeiPreserve_Object = MibTableColumn
me1200EvcConfigEvcItAddPcpDeiPreserve = _Me1200EvcConfigEvcItAddPcpDeiPreserve_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 12),
    _Me1200EvcConfigEvcItAddPcpDeiPreserve_Type()
)
me1200EvcConfigEvcItAddPcpDeiPreserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcItAddPcpDeiPreserve.setStatus("current")
_Me1200EvcConfigEvcItAddPcp_Type = Unsigned32
_Me1200EvcConfigEvcItAddPcp_Object = MibTableColumn
me1200EvcConfigEvcItAddPcp = _Me1200EvcConfigEvcItAddPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 13),
    _Me1200EvcConfigEvcItAddPcp_Type()
)
me1200EvcConfigEvcItAddPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcItAddPcp.setStatus("current")
_Me1200EvcConfigEvcItAddDei_Type = ME1200Unsigned8
_Me1200EvcConfigEvcItAddDei_Object = MibTableColumn
me1200EvcConfigEvcItAddDei = _Me1200EvcConfigEvcItAddDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 14),
    _Me1200EvcConfigEvcItAddDei_Type()
)
me1200EvcConfigEvcItAddDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcItAddDei.setStatus("current")
_Me1200EvcConfigEvcLeafVid_Type = ME1200Unsigned16
_Me1200EvcConfigEvcLeafVid_Object = MibTableColumn
me1200EvcConfigEvcLeafVid = _Me1200EvcConfigEvcLeafVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 15),
    _Me1200EvcConfigEvcLeafVid_Type()
)
me1200EvcConfigEvcLeafVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcLeafVid.setStatus("current")
_Me1200EvcConfigEvcLeafIvid_Type = ME1200Unsigned16
_Me1200EvcConfigEvcLeafIvid_Object = MibTableColumn
me1200EvcConfigEvcLeafIvid = _Me1200EvcConfigEvcLeafIvid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 16),
    _Me1200EvcConfigEvcLeafIvid_Type()
)
me1200EvcConfigEvcLeafIvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcLeafIvid.setStatus("current")
_Me1200EvcConfigEvcLeafPortList_Type = ME1200PortList
_Me1200EvcConfigEvcLeafPortList_Object = MibTableColumn
me1200EvcConfigEvcLeafPortList = _Me1200EvcConfigEvcLeafPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 17),
    _Me1200EvcConfigEvcLeafPortList_Type()
)
me1200EvcConfigEvcLeafPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcLeafPortList.setStatus("current")


class _Me1200EvcConfigEvcName_Type(ME1200DisplayString):
    """Custom type me1200EvcConfigEvcName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200EvcConfigEvcName_Type.__name__ = "ME1200DisplayString"
_Me1200EvcConfigEvcName_Object = MibTableColumn
me1200EvcConfigEvcName = _Me1200EvcConfigEvcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 18),
    _Me1200EvcConfigEvcName_Type()
)
me1200EvcConfigEvcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcName.setStatus("current")
_Me1200EvcConfigEvcAction_Type = ME1200RowEditorState
_Me1200EvcConfigEvcAction_Object = MibTableColumn
me1200EvcConfigEvcAction = _Me1200EvcConfigEvcAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 1, 1, 10000),
    _Me1200EvcConfigEvcAction_Type()
)
me1200EvcConfigEvcAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcAction.setStatus("current")
_Me1200EvcConfigEvcTableRowEditor_ObjectIdentity = ObjectIdentity
me1200EvcConfigEvcTableRowEditor = _Me1200EvcConfigEvcTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2)
)


class _Me1200EvcConfigEvcTableRowEditorEvcId_Type(Integer32):
    """Custom type me1200EvcConfigEvcTableRowEditorEvcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Me1200EvcConfigEvcTableRowEditorEvcId_Type.__name__ = "Integer32"
_Me1200EvcConfigEvcTableRowEditorEvcId_Object = MibScalar
me1200EvcConfigEvcTableRowEditorEvcId = _Me1200EvcConfigEvcTableRowEditorEvcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 1),
    _Me1200EvcConfigEvcTableRowEditorEvcId_Type()
)
me1200EvcConfigEvcTableRowEditorEvcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorEvcId.setStatus("current")
_Me1200EvcConfigEvcTableRowEditorVid_Type = ME1200Unsigned16
_Me1200EvcConfigEvcTableRowEditorVid_Object = MibScalar
me1200EvcConfigEvcTableRowEditorVid = _Me1200EvcConfigEvcTableRowEditorVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 2),
    _Me1200EvcConfigEvcTableRowEditorVid_Type()
)
me1200EvcConfigEvcTableRowEditorVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorVid.setStatus("current")
_Me1200EvcConfigEvcTableRowEditorIvid_Type = ME1200Unsigned16
_Me1200EvcConfigEvcTableRowEditorIvid_Object = MibScalar
me1200EvcConfigEvcTableRowEditorIvid = _Me1200EvcConfigEvcTableRowEditorIvid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 3),
    _Me1200EvcConfigEvcTableRowEditorIvid_Type()
)
me1200EvcConfigEvcTableRowEditorIvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorIvid.setStatus("current")
_Me1200EvcConfigEvcTableRowEditorNniPortList_Type = ME1200PortList
_Me1200EvcConfigEvcTableRowEditorNniPortList_Object = MibScalar
me1200EvcConfigEvcTableRowEditorNniPortList = _Me1200EvcConfigEvcTableRowEditorNniPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 4),
    _Me1200EvcConfigEvcTableRowEditorNniPortList_Type()
)
me1200EvcConfigEvcTableRowEditorNniPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorNniPortList.setStatus("current")
_Me1200EvcConfigEvcTableRowEditorLearning_Type = TruthValue
_Me1200EvcConfigEvcTableRowEditorLearning_Object = MibScalar
me1200EvcConfigEvcTableRowEditorLearning = _Me1200EvcConfigEvcTableRowEditorLearning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 5),
    _Me1200EvcConfigEvcTableRowEditorLearning_Type()
)
me1200EvcConfigEvcTableRowEditorLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorLearning.setStatus("current")
_Me1200EvcConfigEvcTableRowEditorPolicerOp_Type = ME1200evcPolicerOp
_Me1200EvcConfigEvcTableRowEditorPolicerOp_Object = MibScalar
me1200EvcConfigEvcTableRowEditorPolicerOp = _Me1200EvcConfigEvcTableRowEditorPolicerOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 6),
    _Me1200EvcConfigEvcTableRowEditorPolicerOp_Type()
)
me1200EvcConfigEvcTableRowEditorPolicerOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorPolicerOp.setStatus("current")
_Me1200EvcConfigEvcTableRowEditorPolicerId_Type = ME1200Unsigned16
_Me1200EvcConfigEvcTableRowEditorPolicerId_Object = MibScalar
me1200EvcConfigEvcTableRowEditorPolicerId = _Me1200EvcConfigEvcTableRowEditorPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 7),
    _Me1200EvcConfigEvcTableRowEditorPolicerId_Type()
)
me1200EvcConfigEvcTableRowEditorPolicerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorPolicerId.setStatus("current")
_Me1200EvcConfigEvcTableRowEditorUniVid_Type = ME1200Unsigned16
_Me1200EvcConfigEvcTableRowEditorUniVid_Object = MibScalar
me1200EvcConfigEvcTableRowEditorUniVid = _Me1200EvcConfigEvcTableRowEditorUniVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 8),
    _Me1200EvcConfigEvcTableRowEditorUniVid_Type()
)
me1200EvcConfigEvcTableRowEditorUniVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorUniVid.setStatus("current")
_Me1200EvcConfigEvcTableRowEditorItAddType_Type = ME1200evcInnerTagType
_Me1200EvcConfigEvcTableRowEditorItAddType_Object = MibScalar
me1200EvcConfigEvcTableRowEditorItAddType = _Me1200EvcConfigEvcTableRowEditorItAddType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 9),
    _Me1200EvcConfigEvcTableRowEditorItAddType_Type()
)
me1200EvcConfigEvcTableRowEditorItAddType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorItAddType.setStatus("current")
_Me1200EvcConfigEvcTableRowEditorItInnerVid_Type = TruthValue
_Me1200EvcConfigEvcTableRowEditorItInnerVid_Object = MibScalar
me1200EvcConfigEvcTableRowEditorItInnerVid = _Me1200EvcConfigEvcTableRowEditorItInnerVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 10),
    _Me1200EvcConfigEvcTableRowEditorItInnerVid_Type()
)
me1200EvcConfigEvcTableRowEditorItInnerVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorItInnerVid.setStatus("current")
_Me1200EvcConfigEvcTableRowEditorItAddVid_Type = ME1200Unsigned16
_Me1200EvcConfigEvcTableRowEditorItAddVid_Object = MibScalar
me1200EvcConfigEvcTableRowEditorItAddVid = _Me1200EvcConfigEvcTableRowEditorItAddVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 11),
    _Me1200EvcConfigEvcTableRowEditorItAddVid_Type()
)
me1200EvcConfigEvcTableRowEditorItAddVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorItAddVid.setStatus("current")
_Me1200EvcConfigEvcTableRowEditorItAddPcpDeiPreserve_Type = TruthValue
_Me1200EvcConfigEvcTableRowEditorItAddPcpDeiPreserve_Object = MibScalar
me1200EvcConfigEvcTableRowEditorItAddPcpDeiPreserve = _Me1200EvcConfigEvcTableRowEditorItAddPcpDeiPreserve_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 12),
    _Me1200EvcConfigEvcTableRowEditorItAddPcpDeiPreserve_Type()
)
me1200EvcConfigEvcTableRowEditorItAddPcpDeiPreserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorItAddPcpDeiPreserve.setStatus("current")
_Me1200EvcConfigEvcTableRowEditorItAddPcp_Type = Unsigned32
_Me1200EvcConfigEvcTableRowEditorItAddPcp_Object = MibScalar
me1200EvcConfigEvcTableRowEditorItAddPcp = _Me1200EvcConfigEvcTableRowEditorItAddPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 13),
    _Me1200EvcConfigEvcTableRowEditorItAddPcp_Type()
)
me1200EvcConfigEvcTableRowEditorItAddPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorItAddPcp.setStatus("current")
_Me1200EvcConfigEvcTableRowEditorItAddDei_Type = ME1200Unsigned8
_Me1200EvcConfigEvcTableRowEditorItAddDei_Object = MibScalar
me1200EvcConfigEvcTableRowEditorItAddDei = _Me1200EvcConfigEvcTableRowEditorItAddDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 14),
    _Me1200EvcConfigEvcTableRowEditorItAddDei_Type()
)
me1200EvcConfigEvcTableRowEditorItAddDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorItAddDei.setStatus("current")
_Me1200EvcConfigEvcTableRowEditorLeafVid_Type = ME1200Unsigned16
_Me1200EvcConfigEvcTableRowEditorLeafVid_Object = MibScalar
me1200EvcConfigEvcTableRowEditorLeafVid = _Me1200EvcConfigEvcTableRowEditorLeafVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 15),
    _Me1200EvcConfigEvcTableRowEditorLeafVid_Type()
)
me1200EvcConfigEvcTableRowEditorLeafVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorLeafVid.setStatus("current")
_Me1200EvcConfigEvcTableRowEditorLeafIvid_Type = ME1200Unsigned16
_Me1200EvcConfigEvcTableRowEditorLeafIvid_Object = MibScalar
me1200EvcConfigEvcTableRowEditorLeafIvid = _Me1200EvcConfigEvcTableRowEditorLeafIvid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 16),
    _Me1200EvcConfigEvcTableRowEditorLeafIvid_Type()
)
me1200EvcConfigEvcTableRowEditorLeafIvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorLeafIvid.setStatus("current")
_Me1200EvcConfigEvcTableRowEditorLeafPortList_Type = ME1200PortList
_Me1200EvcConfigEvcTableRowEditorLeafPortList_Object = MibScalar
me1200EvcConfigEvcTableRowEditorLeafPortList = _Me1200EvcConfigEvcTableRowEditorLeafPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 17),
    _Me1200EvcConfigEvcTableRowEditorLeafPortList_Type()
)
me1200EvcConfigEvcTableRowEditorLeafPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorLeafPortList.setStatus("current")


class _Me1200EvcConfigEvcTableRowEditorName_Type(ME1200DisplayString):
    """Custom type me1200EvcConfigEvcTableRowEditorName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200EvcConfigEvcTableRowEditorName_Type.__name__ = "ME1200DisplayString"
_Me1200EvcConfigEvcTableRowEditorName_Object = MibScalar
me1200EvcConfigEvcTableRowEditorName = _Me1200EvcConfigEvcTableRowEditorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 18),
    _Me1200EvcConfigEvcTableRowEditorName_Type()
)
me1200EvcConfigEvcTableRowEditorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorName.setStatus("current")
_Me1200EvcConfigEvcTableRowEditorAction_Type = ME1200RowEditorState
_Me1200EvcConfigEvcTableRowEditorAction_Object = MibScalar
me1200EvcConfigEvcTableRowEditorAction = _Me1200EvcConfigEvcTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 4, 2, 10000),
    _Me1200EvcConfigEvcTableRowEditorAction_Type()
)
me1200EvcConfigEvcTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorAction.setStatus("current")
_Me1200EvcConfigEce_ObjectIdentity = ObjectIdentity
me1200EvcConfigEce = _Me1200EvcConfigEce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5)
)
_Me1200EvcConfigEceTable_Object = MibTable
me1200EvcConfigEceTable = _Me1200EvcConfigEceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    me1200EvcConfigEceTable.setStatus("current")
_Me1200EvcConfigEceEntry_Object = MibTableRow
me1200EvcConfigEceEntry = _Me1200EvcConfigEceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1)
)
me1200EvcConfigEceEntry.setIndexNames(
    (0, "ME1200-EVC-MIB", "me1200EvcConfigEceEceId"),
)
if mibBuilder.loadTexts:
    me1200EvcConfigEceEntry.setStatus("current")


class _Me1200EvcConfigEceEceId_Type(Integer32):
    """Custom type me1200EvcConfigEceEceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Me1200EvcConfigEceEceId_Type.__name__ = "Integer32"
_Me1200EvcConfigEceEceId_Object = MibTableColumn
me1200EvcConfigEceEceId = _Me1200EvcConfigEceEceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1),
    _Me1200EvcConfigEceEceId_Type()
)
me1200EvcConfigEceEceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcConfigEceEceId.setStatus("current")
_Me1200EvcConfigEceNextId_Type = Unsigned32
_Me1200EvcConfigEceNextId_Object = MibTableColumn
me1200EvcConfigEceNextId = _Me1200EvcConfigEceNextId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 2),
    _Me1200EvcConfigEceNextId_Type()
)
me1200EvcConfigEceNextId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceNextId.setStatus("current")
_Me1200EvcConfigEceAdvLookup_Type = TruthValue
_Me1200EvcConfigEceAdvLookup_Object = MibTableColumn
me1200EvcConfigEceAdvLookup = _Me1200EvcConfigEceAdvLookup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 3),
    _Me1200EvcConfigEceAdvLookup_Type()
)
me1200EvcConfigEceAdvLookup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceAdvLookup.setStatus("current")
_Me1200EvcConfigEceUniPortList_Type = ME1200PortList
_Me1200EvcConfigEceUniPortList_Object = MibTableColumn
me1200EvcConfigEceUniPortList = _Me1200EvcConfigEceUniPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 4),
    _Me1200EvcConfigEceUniPortList_Type()
)
me1200EvcConfigEceUniPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceUniPortList.setStatus("current")
_Me1200EvcConfigEceSrcMac_Type = MacAddress
_Me1200EvcConfigEceSrcMac_Object = MibTableColumn
me1200EvcConfigEceSrcMac = _Me1200EvcConfigEceSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 10),
    _Me1200EvcConfigEceSrcMac_Type()
)
me1200EvcConfigEceSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceSrcMac.setStatus("current")
_Me1200EvcConfigEceSrcMacMask_Type = MacAddress
_Me1200EvcConfigEceSrcMacMask_Object = MibTableColumn
me1200EvcConfigEceSrcMacMask = _Me1200EvcConfigEceSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 11),
    _Me1200EvcConfigEceSrcMacMask_Type()
)
me1200EvcConfigEceSrcMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceSrcMacMask.setStatus("current")
_Me1200EvcConfigEceDestMacType_Type = ME1200DestMacType
_Me1200EvcConfigEceDestMacType_Object = MibTableColumn
me1200EvcConfigEceDestMacType = _Me1200EvcConfigEceDestMacType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 12),
    _Me1200EvcConfigEceDestMacType_Type()
)
me1200EvcConfigEceDestMacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceDestMacType.setStatus("current")
_Me1200EvcConfigEceDestMac_Type = MacAddress
_Me1200EvcConfigEceDestMac_Object = MibTableColumn
me1200EvcConfigEceDestMac = _Me1200EvcConfigEceDestMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 13),
    _Me1200EvcConfigEceDestMac_Type()
)
me1200EvcConfigEceDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceDestMac.setStatus("current")
_Me1200EvcConfigEceDestMacMask_Type = MacAddress
_Me1200EvcConfigEceDestMacMask_Object = MibTableColumn
me1200EvcConfigEceDestMacMask = _Me1200EvcConfigEceDestMacMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 14),
    _Me1200EvcConfigEceDestMacMask_Type()
)
me1200EvcConfigEceDestMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceDestMacMask.setStatus("current")
_Me1200EvcConfigEceOtMatchType_Type = ME1200VlanTagType
_Me1200EvcConfigEceOtMatchType_Object = MibTableColumn
me1200EvcConfigEceOtMatchType = _Me1200EvcConfigEceOtMatchType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 20),
    _Me1200EvcConfigEceOtMatchType_Type()
)
me1200EvcConfigEceOtMatchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceOtMatchType.setStatus("current")
_Me1200EvcConfigEceOtMatchVid_Type = Unsigned32
_Me1200EvcConfigEceOtMatchVid_Object = MibTableColumn
me1200EvcConfigEceOtMatchVid = _Me1200EvcConfigEceOtMatchVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 21),
    _Me1200EvcConfigEceOtMatchVid_Type()
)
me1200EvcConfigEceOtMatchVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceOtMatchVid.setStatus("current")
_Me1200EvcConfigEceOtMatchPcp_Type = ME1200VlanTagPriority
_Me1200EvcConfigEceOtMatchPcp_Object = MibTableColumn
me1200EvcConfigEceOtMatchPcp = _Me1200EvcConfigEceOtMatchPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 22),
    _Me1200EvcConfigEceOtMatchPcp_Type()
)
me1200EvcConfigEceOtMatchPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceOtMatchPcp.setStatus("current")
_Me1200EvcConfigEceOtMatchDei_Type = ME1200BitType
_Me1200EvcConfigEceOtMatchDei_Object = MibTableColumn
me1200EvcConfigEceOtMatchDei = _Me1200EvcConfigEceOtMatchDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 23),
    _Me1200EvcConfigEceOtMatchDei_Type()
)
me1200EvcConfigEceOtMatchDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceOtMatchDei.setStatus("current")
_Me1200EvcConfigEceItMatchType_Type = ME1200VlanTagType
_Me1200EvcConfigEceItMatchType_Object = MibTableColumn
me1200EvcConfigEceItMatchType = _Me1200EvcConfigEceItMatchType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 30),
    _Me1200EvcConfigEceItMatchType_Type()
)
me1200EvcConfigEceItMatchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceItMatchType.setStatus("current")
_Me1200EvcConfigEceItMatchVid_Type = Unsigned32
_Me1200EvcConfigEceItMatchVid_Object = MibTableColumn
me1200EvcConfigEceItMatchVid = _Me1200EvcConfigEceItMatchVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 31),
    _Me1200EvcConfigEceItMatchVid_Type()
)
me1200EvcConfigEceItMatchVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceItMatchVid.setStatus("current")
_Me1200EvcConfigEceItMatchPcp_Type = ME1200VlanTagPriority
_Me1200EvcConfigEceItMatchPcp_Object = MibTableColumn
me1200EvcConfigEceItMatchPcp = _Me1200EvcConfigEceItMatchPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 32),
    _Me1200EvcConfigEceItMatchPcp_Type()
)
me1200EvcConfigEceItMatchPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceItMatchPcp.setStatus("current")
_Me1200EvcConfigEceItMatchDei_Type = ME1200BitType
_Me1200EvcConfigEceItMatchDei_Object = MibTableColumn
me1200EvcConfigEceItMatchDei = _Me1200EvcConfigEceItMatchDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 33),
    _Me1200EvcConfigEceItMatchDei_Type()
)
me1200EvcConfigEceItMatchDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceItMatchDei.setStatus("current")
_Me1200EvcConfigEceFrameType_Type = ME1200evcFrameType
_Me1200EvcConfigEceFrameType_Object = MibTableColumn
me1200EvcConfigEceFrameType = _Me1200EvcConfigEceFrameType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 50),
    _Me1200EvcConfigEceFrameType_Type()
)
me1200EvcConfigEceFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceFrameType.setStatus("current")
_Me1200EvcConfigEceEtype_Type = ME1200Unsigned16
_Me1200EvcConfigEceEtype_Object = MibTableColumn
me1200EvcConfigEceEtype = _Me1200EvcConfigEceEtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 100),
    _Me1200EvcConfigEceEtype_Type()
)
me1200EvcConfigEceEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceEtype.setStatus("current")
_Me1200EvcConfigEceEtypeMask_Type = ME1200Unsigned16
_Me1200EvcConfigEceEtypeMask_Object = MibTableColumn
me1200EvcConfigEceEtypeMask = _Me1200EvcConfigEceEtypeMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 101),
    _Me1200EvcConfigEceEtypeMask_Type()
)
me1200EvcConfigEceEtypeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceEtypeMask.setStatus("current")
_Me1200EvcConfigEceEtypeData_Type = ME1200Unsigned16
_Me1200EvcConfigEceEtypeData_Object = MibTableColumn
me1200EvcConfigEceEtypeData = _Me1200EvcConfigEceEtypeData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 102),
    _Me1200EvcConfigEceEtypeData_Type()
)
me1200EvcConfigEceEtypeData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceEtypeData.setStatus("current")
_Me1200EvcConfigEceEtypeDataMask_Type = ME1200Unsigned16
_Me1200EvcConfigEceEtypeDataMask_Object = MibTableColumn
me1200EvcConfigEceEtypeDataMask = _Me1200EvcConfigEceEtypeDataMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 103),
    _Me1200EvcConfigEceEtypeDataMask_Type()
)
me1200EvcConfigEceEtypeDataMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceEtypeDataMask.setStatus("current")
_Me1200EvcConfigEceLlcDsap_Type = ME1200Unsigned8
_Me1200EvcConfigEceLlcDsap_Object = MibTableColumn
me1200EvcConfigEceLlcDsap = _Me1200EvcConfigEceLlcDsap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 200),
    _Me1200EvcConfigEceLlcDsap_Type()
)
me1200EvcConfigEceLlcDsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceLlcDsap.setStatus("current")
_Me1200EvcConfigEceLlcDsapMask_Type = ME1200Unsigned8
_Me1200EvcConfigEceLlcDsapMask_Object = MibTableColumn
me1200EvcConfigEceLlcDsapMask = _Me1200EvcConfigEceLlcDsapMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 201),
    _Me1200EvcConfigEceLlcDsapMask_Type()
)
me1200EvcConfigEceLlcDsapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceLlcDsapMask.setStatus("current")
_Me1200EvcConfigEceLlcSsap_Type = ME1200Unsigned8
_Me1200EvcConfigEceLlcSsap_Object = MibTableColumn
me1200EvcConfigEceLlcSsap = _Me1200EvcConfigEceLlcSsap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 202),
    _Me1200EvcConfigEceLlcSsap_Type()
)
me1200EvcConfigEceLlcSsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceLlcSsap.setStatus("current")
_Me1200EvcConfigEceLlcSsapMask_Type = ME1200Unsigned8
_Me1200EvcConfigEceLlcSsapMask_Object = MibTableColumn
me1200EvcConfigEceLlcSsapMask = _Me1200EvcConfigEceLlcSsapMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 203),
    _Me1200EvcConfigEceLlcSsapMask_Type()
)
me1200EvcConfigEceLlcSsapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceLlcSsapMask.setStatus("current")
_Me1200EvcConfigEceLlcControl_Type = ME1200Unsigned8
_Me1200EvcConfigEceLlcControl_Object = MibTableColumn
me1200EvcConfigEceLlcControl = _Me1200EvcConfigEceLlcControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 204),
    _Me1200EvcConfigEceLlcControl_Type()
)
me1200EvcConfigEceLlcControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceLlcControl.setStatus("current")
_Me1200EvcConfigEceLlcControlMask_Type = ME1200Unsigned8
_Me1200EvcConfigEceLlcControlMask_Object = MibTableColumn
me1200EvcConfigEceLlcControlMask = _Me1200EvcConfigEceLlcControlMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 205),
    _Me1200EvcConfigEceLlcControlMask_Type()
)
me1200EvcConfigEceLlcControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceLlcControlMask.setStatus("current")
_Me1200EvcConfigEceLlcPid_Type = ME1200Unsigned16
_Me1200EvcConfigEceLlcPid_Object = MibTableColumn
me1200EvcConfigEceLlcPid = _Me1200EvcConfigEceLlcPid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 206),
    _Me1200EvcConfigEceLlcPid_Type()
)
me1200EvcConfigEceLlcPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceLlcPid.setStatus("current")
_Me1200EvcConfigEceLlcPidMask_Type = ME1200Unsigned16
_Me1200EvcConfigEceLlcPidMask_Object = MibTableColumn
me1200EvcConfigEceLlcPidMask = _Me1200EvcConfigEceLlcPidMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 207),
    _Me1200EvcConfigEceLlcPidMask_Type()
)
me1200EvcConfigEceLlcPidMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceLlcPidMask.setStatus("current")
_Me1200EvcConfigEceSnapOui_Type = Unsigned32
_Me1200EvcConfigEceSnapOui_Object = MibTableColumn
me1200EvcConfigEceSnapOui = _Me1200EvcConfigEceSnapOui_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 300),
    _Me1200EvcConfigEceSnapOui_Type()
)
me1200EvcConfigEceSnapOui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceSnapOui.setStatus("current")
_Me1200EvcConfigEceSnapOuiMask_Type = Unsigned32
_Me1200EvcConfigEceSnapOuiMask_Object = MibTableColumn
me1200EvcConfigEceSnapOuiMask = _Me1200EvcConfigEceSnapOuiMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 301),
    _Me1200EvcConfigEceSnapOuiMask_Type()
)
me1200EvcConfigEceSnapOuiMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceSnapOuiMask.setStatus("current")
_Me1200EvcConfigEceSnapPid_Type = ME1200Unsigned16
_Me1200EvcConfigEceSnapPid_Object = MibTableColumn
me1200EvcConfigEceSnapPid = _Me1200EvcConfigEceSnapPid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 302),
    _Me1200EvcConfigEceSnapPid_Type()
)
me1200EvcConfigEceSnapPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceSnapPid.setStatus("current")
_Me1200EvcConfigEceSnapPidMask_Type = ME1200Unsigned16
_Me1200EvcConfigEceSnapPidMask_Object = MibTableColumn
me1200EvcConfigEceSnapPidMask = _Me1200EvcConfigEceSnapPidMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 303),
    _Me1200EvcConfigEceSnapPidMask_Type()
)
me1200EvcConfigEceSnapPidMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceSnapPidMask.setStatus("current")
_Me1200EvcConfigEceL2cpType_Type = ME1200evcL2cpType
_Me1200EvcConfigEceL2cpType_Object = MibTableColumn
me1200EvcConfigEceL2cpType = _Me1200EvcConfigEceL2cpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 400),
    _Me1200EvcConfigEceL2cpType_Type()
)
me1200EvcConfigEceL2cpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceL2cpType.setStatus("current")
_Me1200EvcConfigEceIpv4Dscp_Type = Unsigned32
_Me1200EvcConfigEceIpv4Dscp_Object = MibTableColumn
me1200EvcConfigEceIpv4Dscp = _Me1200EvcConfigEceIpv4Dscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 500),
    _Me1200EvcConfigEceIpv4Dscp_Type()
)
me1200EvcConfigEceIpv4Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv4Dscp.setStatus("current")
_Me1200EvcConfigEceIpv4Proto_Type = ME1200Unsigned8
_Me1200EvcConfigEceIpv4Proto_Object = MibTableColumn
me1200EvcConfigEceIpv4Proto = _Me1200EvcConfigEceIpv4Proto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 501),
    _Me1200EvcConfigEceIpv4Proto_Type()
)
me1200EvcConfigEceIpv4Proto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv4Proto.setStatus("current")
_Me1200EvcConfigEceIpv4ProtoMask_Type = ME1200Unsigned8
_Me1200EvcConfigEceIpv4ProtoMask_Object = MibTableColumn
me1200EvcConfigEceIpv4ProtoMask = _Me1200EvcConfigEceIpv4ProtoMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 502),
    _Me1200EvcConfigEceIpv4ProtoMask_Type()
)
me1200EvcConfigEceIpv4ProtoMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv4ProtoMask.setStatus("current")
_Me1200EvcConfigEceIpv4Fragment_Type = ME1200BitType
_Me1200EvcConfigEceIpv4Fragment_Object = MibTableColumn
me1200EvcConfigEceIpv4Fragment = _Me1200EvcConfigEceIpv4Fragment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 503),
    _Me1200EvcConfigEceIpv4Fragment_Type()
)
me1200EvcConfigEceIpv4Fragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv4Fragment.setStatus("current")
_Me1200EvcConfigEceIpv4SrcIp_Type = IpAddress
_Me1200EvcConfigEceIpv4SrcIp_Object = MibTableColumn
me1200EvcConfigEceIpv4SrcIp = _Me1200EvcConfigEceIpv4SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 504),
    _Me1200EvcConfigEceIpv4SrcIp_Type()
)
me1200EvcConfigEceIpv4SrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv4SrcIp.setStatus("current")
_Me1200EvcConfigEceIpv4SrcIpMask_Type = IpAddress
_Me1200EvcConfigEceIpv4SrcIpMask_Object = MibTableColumn
me1200EvcConfigEceIpv4SrcIpMask = _Me1200EvcConfigEceIpv4SrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 505),
    _Me1200EvcConfigEceIpv4SrcIpMask_Type()
)
me1200EvcConfigEceIpv4SrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv4SrcIpMask.setStatus("current")
_Me1200EvcConfigEceIpv4DestIp_Type = IpAddress
_Me1200EvcConfigEceIpv4DestIp_Object = MibTableColumn
me1200EvcConfigEceIpv4DestIp = _Me1200EvcConfigEceIpv4DestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 506),
    _Me1200EvcConfigEceIpv4DestIp_Type()
)
me1200EvcConfigEceIpv4DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv4DestIp.setStatus("current")
_Me1200EvcConfigEceIpv4DestIpMask_Type = IpAddress
_Me1200EvcConfigEceIpv4DestIpMask_Object = MibTableColumn
me1200EvcConfigEceIpv4DestIpMask = _Me1200EvcConfigEceIpv4DestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 507),
    _Me1200EvcConfigEceIpv4DestIpMask_Type()
)
me1200EvcConfigEceIpv4DestIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv4DestIpMask.setStatus("current")
_Me1200EvcConfigEceIpv4SrcPort_Type = Unsigned32
_Me1200EvcConfigEceIpv4SrcPort_Object = MibTableColumn
me1200EvcConfigEceIpv4SrcPort = _Me1200EvcConfigEceIpv4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 508),
    _Me1200EvcConfigEceIpv4SrcPort_Type()
)
me1200EvcConfigEceIpv4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv4SrcPort.setStatus("current")
_Me1200EvcConfigEceIpv4DestPort_Type = Unsigned32
_Me1200EvcConfigEceIpv4DestPort_Object = MibTableColumn
me1200EvcConfigEceIpv4DestPort = _Me1200EvcConfigEceIpv4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 509),
    _Me1200EvcConfigEceIpv4DestPort_Type()
)
me1200EvcConfigEceIpv4DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv4DestPort.setStatus("current")
_Me1200EvcConfigEceIpv6Dscp_Type = Unsigned32
_Me1200EvcConfigEceIpv6Dscp_Object = MibTableColumn
me1200EvcConfigEceIpv6Dscp = _Me1200EvcConfigEceIpv6Dscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 600),
    _Me1200EvcConfigEceIpv6Dscp_Type()
)
me1200EvcConfigEceIpv6Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv6Dscp.setStatus("current")
_Me1200EvcConfigEceIpv6Proto_Type = ME1200Unsigned8
_Me1200EvcConfigEceIpv6Proto_Object = MibTableColumn
me1200EvcConfigEceIpv6Proto = _Me1200EvcConfigEceIpv6Proto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 601),
    _Me1200EvcConfigEceIpv6Proto_Type()
)
me1200EvcConfigEceIpv6Proto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv6Proto.setStatus("current")
_Me1200EvcConfigEceIpv6ProtoMask_Type = ME1200Unsigned8
_Me1200EvcConfigEceIpv6ProtoMask_Object = MibTableColumn
me1200EvcConfigEceIpv6ProtoMask = _Me1200EvcConfigEceIpv6ProtoMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 602),
    _Me1200EvcConfigEceIpv6ProtoMask_Type()
)
me1200EvcConfigEceIpv6ProtoMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv6ProtoMask.setStatus("current")
_Me1200EvcConfigEceIpv6SrcIp_Type = InetAddressIPv6
_Me1200EvcConfigEceIpv6SrcIp_Object = MibTableColumn
me1200EvcConfigEceIpv6SrcIp = _Me1200EvcConfigEceIpv6SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 603),
    _Me1200EvcConfigEceIpv6SrcIp_Type()
)
me1200EvcConfigEceIpv6SrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv6SrcIp.setStatus("current")
_Me1200EvcConfigEceIpv6SrcIpMask_Type = InetAddressIPv6
_Me1200EvcConfigEceIpv6SrcIpMask_Object = MibTableColumn
me1200EvcConfigEceIpv6SrcIpMask = _Me1200EvcConfigEceIpv6SrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 604),
    _Me1200EvcConfigEceIpv6SrcIpMask_Type()
)
me1200EvcConfigEceIpv6SrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv6SrcIpMask.setStatus("current")
_Me1200EvcConfigEceIpv6DestIp_Type = InetAddressIPv6
_Me1200EvcConfigEceIpv6DestIp_Object = MibTableColumn
me1200EvcConfigEceIpv6DestIp = _Me1200EvcConfigEceIpv6DestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 605),
    _Me1200EvcConfigEceIpv6DestIp_Type()
)
me1200EvcConfigEceIpv6DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv6DestIp.setStatus("current")
_Me1200EvcConfigEceIpv6DestIpMask_Type = InetAddressIPv6
_Me1200EvcConfigEceIpv6DestIpMask_Object = MibTableColumn
me1200EvcConfigEceIpv6DestIpMask = _Me1200EvcConfigEceIpv6DestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 606),
    _Me1200EvcConfigEceIpv6DestIpMask_Type()
)
me1200EvcConfigEceIpv6DestIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv6DestIpMask.setStatus("current")
_Me1200EvcConfigEceIpv6SrcPort_Type = Unsigned32
_Me1200EvcConfigEceIpv6SrcPort_Object = MibTableColumn
me1200EvcConfigEceIpv6SrcPort = _Me1200EvcConfigEceIpv6SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 607),
    _Me1200EvcConfigEceIpv6SrcPort_Type()
)
me1200EvcConfigEceIpv6SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv6SrcPort.setStatus("current")
_Me1200EvcConfigEceIpv6DestPort_Type = Unsigned32
_Me1200EvcConfigEceIpv6DestPort_Object = MibTableColumn
me1200EvcConfigEceIpv6DestPort = _Me1200EvcConfigEceIpv6DestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 608),
    _Me1200EvcConfigEceIpv6DestPort_Type()
)
me1200EvcConfigEceIpv6DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceIpv6DestPort.setStatus("current")
_Me1200EvcConfigEceDirection_Type = ME1200evcDirection
_Me1200EvcConfigEceDirection_Object = MibTableColumn
me1200EvcConfigEceDirection = _Me1200EvcConfigEceDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1000),
    _Me1200EvcConfigEceDirection_Type()
)
me1200EvcConfigEceDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceDirection.setStatus("current")
_Me1200EvcConfigEceRuleType_Type = ME1200evcRuleType
_Me1200EvcConfigEceRuleType_Object = MibTableColumn
me1200EvcConfigEceRuleType = _Me1200EvcConfigEceRuleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1010),
    _Me1200EvcConfigEceRuleType_Type()
)
me1200EvcConfigEceRuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceRuleType.setStatus("current")
_Me1200EvcConfigEceTxLookup_Type = ME1200evcTxLookup
_Me1200EvcConfigEceTxLookup_Object = MibTableColumn
me1200EvcConfigEceTxLookup = _Me1200EvcConfigEceTxLookup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1011),
    _Me1200EvcConfigEceTxLookup_Type()
)
me1200EvcConfigEceTxLookup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTxLookup.setStatus("current")
_Me1200EvcConfigEcePopTag_Type = ME1200evcPopTag
_Me1200EvcConfigEcePopTag_Object = MibTableColumn
me1200EvcConfigEcePopTag = _Me1200EvcConfigEcePopTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1020),
    _Me1200EvcConfigEcePopTag_Type()
)
me1200EvcConfigEcePopTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEcePopTag.setStatus("current")
_Me1200EvcConfigEceOtAddEnable_Type = TruthValue
_Me1200EvcConfigEceOtAddEnable_Object = MibTableColumn
me1200EvcConfigEceOtAddEnable = _Me1200EvcConfigEceOtAddEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1100),
    _Me1200EvcConfigEceOtAddEnable_Type()
)
me1200EvcConfigEceOtAddEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceOtAddEnable.setStatus("current")
_Me1200EvcConfigEceOtAddVid_Type = ME1200Unsigned16
_Me1200EvcConfigEceOtAddVid_Object = MibTableColumn
me1200EvcConfigEceOtAddVid = _Me1200EvcConfigEceOtAddVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1101),
    _Me1200EvcConfigEceOtAddVid_Type()
)
me1200EvcConfigEceOtAddVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceOtAddVid.setStatus("current")
_Me1200EvcConfigEceOtAddPcpMode_Type = ME1200evcPcpMode
_Me1200EvcConfigEceOtAddPcpMode_Object = MibTableColumn
me1200EvcConfigEceOtAddPcpMode = _Me1200EvcConfigEceOtAddPcpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1102),
    _Me1200EvcConfigEceOtAddPcpMode_Type()
)
me1200EvcConfigEceOtAddPcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceOtAddPcpMode.setStatus("current")
_Me1200EvcConfigEceOtAddPcpDeiPreserve_Type = TruthValue
_Me1200EvcConfigEceOtAddPcpDeiPreserve_Object = MibTableColumn
me1200EvcConfigEceOtAddPcpDeiPreserve = _Me1200EvcConfigEceOtAddPcpDeiPreserve_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1103),
    _Me1200EvcConfigEceOtAddPcpDeiPreserve_Type()
)
me1200EvcConfigEceOtAddPcpDeiPreserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceOtAddPcpDeiPreserve.setStatus("current")
_Me1200EvcConfigEceOtAddPcp_Type = Unsigned32
_Me1200EvcConfigEceOtAddPcp_Object = MibTableColumn
me1200EvcConfigEceOtAddPcp = _Me1200EvcConfigEceOtAddPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1104),
    _Me1200EvcConfigEceOtAddPcp_Type()
)
me1200EvcConfigEceOtAddPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceOtAddPcp.setStatus("current")
_Me1200EvcConfigEceOtAddDeiMode_Type = ME1200evcDeiMode
_Me1200EvcConfigEceOtAddDeiMode_Object = MibTableColumn
me1200EvcConfigEceOtAddDeiMode = _Me1200EvcConfigEceOtAddDeiMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1105),
    _Me1200EvcConfigEceOtAddDeiMode_Type()
)
me1200EvcConfigEceOtAddDeiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceOtAddDeiMode.setStatus("current")
_Me1200EvcConfigEceOtAddDei_Type = ME1200Unsigned8
_Me1200EvcConfigEceOtAddDei_Object = MibTableColumn
me1200EvcConfigEceOtAddDei = _Me1200EvcConfigEceOtAddDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1106),
    _Me1200EvcConfigEceOtAddDei_Type()
)
me1200EvcConfigEceOtAddDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceOtAddDei.setStatus("current")
_Me1200EvcConfigEceItAddType_Type = ME1200evcInnerTagType
_Me1200EvcConfigEceItAddType_Object = MibTableColumn
me1200EvcConfigEceItAddType = _Me1200EvcConfigEceItAddType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1200),
    _Me1200EvcConfigEceItAddType_Type()
)
me1200EvcConfigEceItAddType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceItAddType.setStatus("current")
_Me1200EvcConfigEceItAddVid_Type = ME1200Unsigned16
_Me1200EvcConfigEceItAddVid_Object = MibTableColumn
me1200EvcConfigEceItAddVid = _Me1200EvcConfigEceItAddVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1201),
    _Me1200EvcConfigEceItAddVid_Type()
)
me1200EvcConfigEceItAddVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceItAddVid.setStatus("current")
_Me1200EvcConfigEceItAddPcpMode_Type = ME1200evcPcpMode
_Me1200EvcConfigEceItAddPcpMode_Object = MibTableColumn
me1200EvcConfigEceItAddPcpMode = _Me1200EvcConfigEceItAddPcpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1202),
    _Me1200EvcConfigEceItAddPcpMode_Type()
)
me1200EvcConfigEceItAddPcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceItAddPcpMode.setStatus("current")
_Me1200EvcConfigEceItAddPcpDeiPreserve_Type = TruthValue
_Me1200EvcConfigEceItAddPcpDeiPreserve_Object = MibTableColumn
me1200EvcConfigEceItAddPcpDeiPreserve = _Me1200EvcConfigEceItAddPcpDeiPreserve_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1203),
    _Me1200EvcConfigEceItAddPcpDeiPreserve_Type()
)
me1200EvcConfigEceItAddPcpDeiPreserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceItAddPcpDeiPreserve.setStatus("current")
_Me1200EvcConfigEceItAddPcp_Type = Unsigned32
_Me1200EvcConfigEceItAddPcp_Object = MibTableColumn
me1200EvcConfigEceItAddPcp = _Me1200EvcConfigEceItAddPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1204),
    _Me1200EvcConfigEceItAddPcp_Type()
)
me1200EvcConfigEceItAddPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceItAddPcp.setStatus("current")
_Me1200EvcConfigEceItAddDeiMode_Type = ME1200evcDeiMode
_Me1200EvcConfigEceItAddDeiMode_Object = MibTableColumn
me1200EvcConfigEceItAddDeiMode = _Me1200EvcConfigEceItAddDeiMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1205),
    _Me1200EvcConfigEceItAddDeiMode_Type()
)
me1200EvcConfigEceItAddDeiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceItAddDeiMode.setStatus("current")
_Me1200EvcConfigEceItAddDei_Type = ME1200Unsigned8
_Me1200EvcConfigEceItAddDei_Object = MibTableColumn
me1200EvcConfigEceItAddDei = _Me1200EvcConfigEceItAddDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1206),
    _Me1200EvcConfigEceItAddDei_Type()
)
me1200EvcConfigEceItAddDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceItAddDei.setStatus("current")
_Me1200EvcConfigEceEvcId_Type = ME1200Unsigned16
_Me1200EvcConfigEceEvcId_Object = MibTableColumn
me1200EvcConfigEceEvcId = _Me1200EvcConfigEceEvcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1300),
    _Me1200EvcConfigEceEvcId_Type()
)
me1200EvcConfigEceEvcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceEvcId.setStatus("current")
_Me1200EvcConfigEcePolicerOp_Type = ME1200evcPolicerOp
_Me1200EvcConfigEcePolicerOp_Object = MibTableColumn
me1200EvcConfigEcePolicerOp = _Me1200EvcConfigEcePolicerOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1301),
    _Me1200EvcConfigEcePolicerOp_Type()
)
me1200EvcConfigEcePolicerOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEcePolicerOp.setStatus("current")
_Me1200EvcConfigEcePolicerId_Type = ME1200Unsigned16
_Me1200EvcConfigEcePolicerId_Object = MibTableColumn
me1200EvcConfigEcePolicerId = _Me1200EvcConfigEcePolicerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1302),
    _Me1200EvcConfigEcePolicerId_Type()
)
me1200EvcConfigEcePolicerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEcePolicerId.setStatus("current")
_Me1200EvcConfigEcePolicyNo_Type = Unsigned32
_Me1200EvcConfigEcePolicyNo_Object = MibTableColumn
me1200EvcConfigEcePolicyNo = _Me1200EvcConfigEcePolicyNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1310),
    _Me1200EvcConfigEcePolicyNo_Type()
)
me1200EvcConfigEcePolicyNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEcePolicyNo.setStatus("current")
_Me1200EvcConfigEceCosEnable_Type = TruthValue
_Me1200EvcConfigEceCosEnable_Object = MibTableColumn
me1200EvcConfigEceCosEnable = _Me1200EvcConfigEceCosEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1320),
    _Me1200EvcConfigEceCosEnable_Type()
)
me1200EvcConfigEceCosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceCosEnable.setStatus("current")
_Me1200EvcConfigEceCos_Type = Unsigned32
_Me1200EvcConfigEceCos_Object = MibTableColumn
me1200EvcConfigEceCos = _Me1200EvcConfigEceCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1321),
    _Me1200EvcConfigEceCos_Type()
)
me1200EvcConfigEceCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceCos.setStatus("current")
_Me1200EvcConfigEceDpEnable_Type = TruthValue
_Me1200EvcConfigEceDpEnable_Object = MibTableColumn
me1200EvcConfigEceDpEnable = _Me1200EvcConfigEceDpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1330),
    _Me1200EvcConfigEceDpEnable_Type()
)
me1200EvcConfigEceDpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceDpEnable.setStatus("current")
_Me1200EvcConfigEceDp_Type = ME1200Unsigned8
_Me1200EvcConfigEceDp_Object = MibTableColumn
me1200EvcConfigEceDp = _Me1200EvcConfigEceDp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1331),
    _Me1200EvcConfigEceDp_Type()
)
me1200EvcConfigEceDp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceDp.setStatus("current")
_Me1200EvcConfigEceL2cpMode_Type = ME1200evcEceL2cpMode
_Me1200EvcConfigEceL2cpMode_Object = MibTableColumn
me1200EvcConfigEceL2cpMode = _Me1200EvcConfigEceL2cpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1332),
    _Me1200EvcConfigEceL2cpMode_Type()
)
me1200EvcConfigEceL2cpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceL2cpMode.setStatus("current")
_Me1200EvcConfigEceL2cpDmac_Type = ME1200evcL2cpDmac
_Me1200EvcConfigEceL2cpDmac_Object = MibTableColumn
me1200EvcConfigEceL2cpDmac = _Me1200EvcConfigEceL2cpDmac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 1333),
    _Me1200EvcConfigEceL2cpDmac_Type()
)
me1200EvcConfigEceL2cpDmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceL2cpDmac.setStatus("current")
_Me1200EvcConfigEceAction_Type = ME1200RowEditorState
_Me1200EvcConfigEceAction_Object = MibTableColumn
me1200EvcConfigEceAction = _Me1200EvcConfigEceAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 1, 1, 10000),
    _Me1200EvcConfigEceAction_Type()
)
me1200EvcConfigEceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceAction.setStatus("current")
_Me1200EvcConfigEceTableRowEditor_ObjectIdentity = ObjectIdentity
me1200EvcConfigEceTableRowEditor = _Me1200EvcConfigEceTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2)
)


class _Me1200EvcConfigEceTableRowEditorEceId_Type(Integer32):
    """Custom type me1200EvcConfigEceTableRowEditorEceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Me1200EvcConfigEceTableRowEditorEceId_Type.__name__ = "Integer32"
_Me1200EvcConfigEceTableRowEditorEceId_Object = MibScalar
me1200EvcConfigEceTableRowEditorEceId = _Me1200EvcConfigEceTableRowEditorEceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1),
    _Me1200EvcConfigEceTableRowEditorEceId_Type()
)
me1200EvcConfigEceTableRowEditorEceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorEceId.setStatus("current")
_Me1200EvcConfigEceTableRowEditorNextId_Type = Unsigned32
_Me1200EvcConfigEceTableRowEditorNextId_Object = MibScalar
me1200EvcConfigEceTableRowEditorNextId = _Me1200EvcConfigEceTableRowEditorNextId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 2),
    _Me1200EvcConfigEceTableRowEditorNextId_Type()
)
me1200EvcConfigEceTableRowEditorNextId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorNextId.setStatus("current")
_Me1200EvcConfigEceTableRowEditorAdvLookup_Type = TruthValue
_Me1200EvcConfigEceTableRowEditorAdvLookup_Object = MibScalar
me1200EvcConfigEceTableRowEditorAdvLookup = _Me1200EvcConfigEceTableRowEditorAdvLookup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 3),
    _Me1200EvcConfigEceTableRowEditorAdvLookup_Type()
)
me1200EvcConfigEceTableRowEditorAdvLookup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorAdvLookup.setStatus("current")
_Me1200EvcConfigEceTableRowEditorUniPortList_Type = ME1200PortList
_Me1200EvcConfigEceTableRowEditorUniPortList_Object = MibScalar
me1200EvcConfigEceTableRowEditorUniPortList = _Me1200EvcConfigEceTableRowEditorUniPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 4),
    _Me1200EvcConfigEceTableRowEditorUniPortList_Type()
)
me1200EvcConfigEceTableRowEditorUniPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorUniPortList.setStatus("current")
_Me1200EvcConfigEceTableRowEditorSrcMac_Type = MacAddress
_Me1200EvcConfigEceTableRowEditorSrcMac_Object = MibScalar
me1200EvcConfigEceTableRowEditorSrcMac = _Me1200EvcConfigEceTableRowEditorSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 10),
    _Me1200EvcConfigEceTableRowEditorSrcMac_Type()
)
me1200EvcConfigEceTableRowEditorSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorSrcMac.setStatus("current")
_Me1200EvcConfigEceTableRowEditorSrcMacMask_Type = MacAddress
_Me1200EvcConfigEceTableRowEditorSrcMacMask_Object = MibScalar
me1200EvcConfigEceTableRowEditorSrcMacMask = _Me1200EvcConfigEceTableRowEditorSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 11),
    _Me1200EvcConfigEceTableRowEditorSrcMacMask_Type()
)
me1200EvcConfigEceTableRowEditorSrcMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorSrcMacMask.setStatus("current")
_Me1200EvcConfigEceTableRowEditorDestMacType_Type = ME1200DestMacType
_Me1200EvcConfigEceTableRowEditorDestMacType_Object = MibScalar
me1200EvcConfigEceTableRowEditorDestMacType = _Me1200EvcConfigEceTableRowEditorDestMacType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 12),
    _Me1200EvcConfigEceTableRowEditorDestMacType_Type()
)
me1200EvcConfigEceTableRowEditorDestMacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorDestMacType.setStatus("current")
_Me1200EvcConfigEceTableRowEditorDestMac_Type = MacAddress
_Me1200EvcConfigEceTableRowEditorDestMac_Object = MibScalar
me1200EvcConfigEceTableRowEditorDestMac = _Me1200EvcConfigEceTableRowEditorDestMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 13),
    _Me1200EvcConfigEceTableRowEditorDestMac_Type()
)
me1200EvcConfigEceTableRowEditorDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorDestMac.setStatus("current")
_Me1200EvcConfigEceTableRowEditorDestMacMask_Type = MacAddress
_Me1200EvcConfigEceTableRowEditorDestMacMask_Object = MibScalar
me1200EvcConfigEceTableRowEditorDestMacMask = _Me1200EvcConfigEceTableRowEditorDestMacMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 14),
    _Me1200EvcConfigEceTableRowEditorDestMacMask_Type()
)
me1200EvcConfigEceTableRowEditorDestMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorDestMacMask.setStatus("current")
_Me1200EvcConfigEceTableRowEditorOtMatchType_Type = ME1200VlanTagType
_Me1200EvcConfigEceTableRowEditorOtMatchType_Object = MibScalar
me1200EvcConfigEceTableRowEditorOtMatchType = _Me1200EvcConfigEceTableRowEditorOtMatchType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 20),
    _Me1200EvcConfigEceTableRowEditorOtMatchType_Type()
)
me1200EvcConfigEceTableRowEditorOtMatchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorOtMatchType.setStatus("current")
_Me1200EvcConfigEceTableRowEditorOtMatchVid_Type = Unsigned32
_Me1200EvcConfigEceTableRowEditorOtMatchVid_Object = MibScalar
me1200EvcConfigEceTableRowEditorOtMatchVid = _Me1200EvcConfigEceTableRowEditorOtMatchVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 21),
    _Me1200EvcConfigEceTableRowEditorOtMatchVid_Type()
)
me1200EvcConfigEceTableRowEditorOtMatchVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorOtMatchVid.setStatus("current")
_Me1200EvcConfigEceTableRowEditorOtMatchPcp_Type = ME1200VlanTagPriority
_Me1200EvcConfigEceTableRowEditorOtMatchPcp_Object = MibScalar
me1200EvcConfigEceTableRowEditorOtMatchPcp = _Me1200EvcConfigEceTableRowEditorOtMatchPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 22),
    _Me1200EvcConfigEceTableRowEditorOtMatchPcp_Type()
)
me1200EvcConfigEceTableRowEditorOtMatchPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorOtMatchPcp.setStatus("current")
_Me1200EvcConfigEceTableRowEditorOtMatchDei_Type = ME1200BitType
_Me1200EvcConfigEceTableRowEditorOtMatchDei_Object = MibScalar
me1200EvcConfigEceTableRowEditorOtMatchDei = _Me1200EvcConfigEceTableRowEditorOtMatchDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 23),
    _Me1200EvcConfigEceTableRowEditorOtMatchDei_Type()
)
me1200EvcConfigEceTableRowEditorOtMatchDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorOtMatchDei.setStatus("current")
_Me1200EvcConfigEceTableRowEditorItMatchType_Type = ME1200VlanTagType
_Me1200EvcConfigEceTableRowEditorItMatchType_Object = MibScalar
me1200EvcConfigEceTableRowEditorItMatchType = _Me1200EvcConfigEceTableRowEditorItMatchType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 30),
    _Me1200EvcConfigEceTableRowEditorItMatchType_Type()
)
me1200EvcConfigEceTableRowEditorItMatchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorItMatchType.setStatus("current")
_Me1200EvcConfigEceTableRowEditorItMatchVid_Type = Unsigned32
_Me1200EvcConfigEceTableRowEditorItMatchVid_Object = MibScalar
me1200EvcConfigEceTableRowEditorItMatchVid = _Me1200EvcConfigEceTableRowEditorItMatchVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 31),
    _Me1200EvcConfigEceTableRowEditorItMatchVid_Type()
)
me1200EvcConfigEceTableRowEditorItMatchVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorItMatchVid.setStatus("current")
_Me1200EvcConfigEceTableRowEditorItMatchPcp_Type = ME1200VlanTagPriority
_Me1200EvcConfigEceTableRowEditorItMatchPcp_Object = MibScalar
me1200EvcConfigEceTableRowEditorItMatchPcp = _Me1200EvcConfigEceTableRowEditorItMatchPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 32),
    _Me1200EvcConfigEceTableRowEditorItMatchPcp_Type()
)
me1200EvcConfigEceTableRowEditorItMatchPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorItMatchPcp.setStatus("current")
_Me1200EvcConfigEceTableRowEditorItMatchDei_Type = ME1200BitType
_Me1200EvcConfigEceTableRowEditorItMatchDei_Object = MibScalar
me1200EvcConfigEceTableRowEditorItMatchDei = _Me1200EvcConfigEceTableRowEditorItMatchDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 33),
    _Me1200EvcConfigEceTableRowEditorItMatchDei_Type()
)
me1200EvcConfigEceTableRowEditorItMatchDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorItMatchDei.setStatus("current")
_Me1200EvcConfigEceTableRowEditorFrameType_Type = ME1200evcFrameType
_Me1200EvcConfigEceTableRowEditorFrameType_Object = MibScalar
me1200EvcConfigEceTableRowEditorFrameType = _Me1200EvcConfigEceTableRowEditorFrameType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 50),
    _Me1200EvcConfigEceTableRowEditorFrameType_Type()
)
me1200EvcConfigEceTableRowEditorFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorFrameType.setStatus("current")
_Me1200EvcConfigEceTableRowEditorEtype_Type = ME1200Unsigned16
_Me1200EvcConfigEceTableRowEditorEtype_Object = MibScalar
me1200EvcConfigEceTableRowEditorEtype = _Me1200EvcConfigEceTableRowEditorEtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 100),
    _Me1200EvcConfigEceTableRowEditorEtype_Type()
)
me1200EvcConfigEceTableRowEditorEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorEtype.setStatus("current")
_Me1200EvcConfigEceTableRowEditorEtypeMask_Type = ME1200Unsigned16
_Me1200EvcConfigEceTableRowEditorEtypeMask_Object = MibScalar
me1200EvcConfigEceTableRowEditorEtypeMask = _Me1200EvcConfigEceTableRowEditorEtypeMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 101),
    _Me1200EvcConfigEceTableRowEditorEtypeMask_Type()
)
me1200EvcConfigEceTableRowEditorEtypeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorEtypeMask.setStatus("current")
_Me1200EvcConfigEceTableRowEditorEtypeData_Type = ME1200Unsigned16
_Me1200EvcConfigEceTableRowEditorEtypeData_Object = MibScalar
me1200EvcConfigEceTableRowEditorEtypeData = _Me1200EvcConfigEceTableRowEditorEtypeData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 102),
    _Me1200EvcConfigEceTableRowEditorEtypeData_Type()
)
me1200EvcConfigEceTableRowEditorEtypeData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorEtypeData.setStatus("current")
_Me1200EvcConfigEceTableRowEditorEtypeDataMask_Type = ME1200Unsigned16
_Me1200EvcConfigEceTableRowEditorEtypeDataMask_Object = MibScalar
me1200EvcConfigEceTableRowEditorEtypeDataMask = _Me1200EvcConfigEceTableRowEditorEtypeDataMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 103),
    _Me1200EvcConfigEceTableRowEditorEtypeDataMask_Type()
)
me1200EvcConfigEceTableRowEditorEtypeDataMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorEtypeDataMask.setStatus("current")
_Me1200EvcConfigEceTableRowEditorLlcDsap_Type = ME1200Unsigned8
_Me1200EvcConfigEceTableRowEditorLlcDsap_Object = MibScalar
me1200EvcConfigEceTableRowEditorLlcDsap = _Me1200EvcConfigEceTableRowEditorLlcDsap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 200),
    _Me1200EvcConfigEceTableRowEditorLlcDsap_Type()
)
me1200EvcConfigEceTableRowEditorLlcDsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorLlcDsap.setStatus("current")
_Me1200EvcConfigEceTableRowEditorLlcDsapMask_Type = ME1200Unsigned8
_Me1200EvcConfigEceTableRowEditorLlcDsapMask_Object = MibScalar
me1200EvcConfigEceTableRowEditorLlcDsapMask = _Me1200EvcConfigEceTableRowEditorLlcDsapMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 201),
    _Me1200EvcConfigEceTableRowEditorLlcDsapMask_Type()
)
me1200EvcConfigEceTableRowEditorLlcDsapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorLlcDsapMask.setStatus("current")
_Me1200EvcConfigEceTableRowEditorLlcSsap_Type = ME1200Unsigned8
_Me1200EvcConfigEceTableRowEditorLlcSsap_Object = MibScalar
me1200EvcConfigEceTableRowEditorLlcSsap = _Me1200EvcConfigEceTableRowEditorLlcSsap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 202),
    _Me1200EvcConfigEceTableRowEditorLlcSsap_Type()
)
me1200EvcConfigEceTableRowEditorLlcSsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorLlcSsap.setStatus("current")
_Me1200EvcConfigEceTableRowEditorLlcSsapMask_Type = ME1200Unsigned8
_Me1200EvcConfigEceTableRowEditorLlcSsapMask_Object = MibScalar
me1200EvcConfigEceTableRowEditorLlcSsapMask = _Me1200EvcConfigEceTableRowEditorLlcSsapMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 203),
    _Me1200EvcConfigEceTableRowEditorLlcSsapMask_Type()
)
me1200EvcConfigEceTableRowEditorLlcSsapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorLlcSsapMask.setStatus("current")
_Me1200EvcConfigEceTableRowEditorLlcControl_Type = ME1200Unsigned8
_Me1200EvcConfigEceTableRowEditorLlcControl_Object = MibScalar
me1200EvcConfigEceTableRowEditorLlcControl = _Me1200EvcConfigEceTableRowEditorLlcControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 204),
    _Me1200EvcConfigEceTableRowEditorLlcControl_Type()
)
me1200EvcConfigEceTableRowEditorLlcControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorLlcControl.setStatus("current")
_Me1200EvcConfigEceTableRowEditorLlcControlMask_Type = ME1200Unsigned8
_Me1200EvcConfigEceTableRowEditorLlcControlMask_Object = MibScalar
me1200EvcConfigEceTableRowEditorLlcControlMask = _Me1200EvcConfigEceTableRowEditorLlcControlMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 205),
    _Me1200EvcConfigEceTableRowEditorLlcControlMask_Type()
)
me1200EvcConfigEceTableRowEditorLlcControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorLlcControlMask.setStatus("current")
_Me1200EvcConfigEceTableRowEditorLlcPid_Type = ME1200Unsigned16
_Me1200EvcConfigEceTableRowEditorLlcPid_Object = MibScalar
me1200EvcConfigEceTableRowEditorLlcPid = _Me1200EvcConfigEceTableRowEditorLlcPid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 206),
    _Me1200EvcConfigEceTableRowEditorLlcPid_Type()
)
me1200EvcConfigEceTableRowEditorLlcPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorLlcPid.setStatus("current")
_Me1200EvcConfigEceTableRowEditorLlcPidMask_Type = ME1200Unsigned16
_Me1200EvcConfigEceTableRowEditorLlcPidMask_Object = MibScalar
me1200EvcConfigEceTableRowEditorLlcPidMask = _Me1200EvcConfigEceTableRowEditorLlcPidMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 207),
    _Me1200EvcConfigEceTableRowEditorLlcPidMask_Type()
)
me1200EvcConfigEceTableRowEditorLlcPidMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorLlcPidMask.setStatus("current")
_Me1200EvcConfigEceTableRowEditorSnapOui_Type = Unsigned32
_Me1200EvcConfigEceTableRowEditorSnapOui_Object = MibScalar
me1200EvcConfigEceTableRowEditorSnapOui = _Me1200EvcConfigEceTableRowEditorSnapOui_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 300),
    _Me1200EvcConfigEceTableRowEditorSnapOui_Type()
)
me1200EvcConfigEceTableRowEditorSnapOui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorSnapOui.setStatus("current")
_Me1200EvcConfigEceTableRowEditorSnapOuiMask_Type = Unsigned32
_Me1200EvcConfigEceTableRowEditorSnapOuiMask_Object = MibScalar
me1200EvcConfigEceTableRowEditorSnapOuiMask = _Me1200EvcConfigEceTableRowEditorSnapOuiMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 301),
    _Me1200EvcConfigEceTableRowEditorSnapOuiMask_Type()
)
me1200EvcConfigEceTableRowEditorSnapOuiMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorSnapOuiMask.setStatus("current")
_Me1200EvcConfigEceTableRowEditorSnapPid_Type = ME1200Unsigned16
_Me1200EvcConfigEceTableRowEditorSnapPid_Object = MibScalar
me1200EvcConfigEceTableRowEditorSnapPid = _Me1200EvcConfigEceTableRowEditorSnapPid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 302),
    _Me1200EvcConfigEceTableRowEditorSnapPid_Type()
)
me1200EvcConfigEceTableRowEditorSnapPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorSnapPid.setStatus("current")
_Me1200EvcConfigEceTableRowEditorSnapPidMask_Type = ME1200Unsigned16
_Me1200EvcConfigEceTableRowEditorSnapPidMask_Object = MibScalar
me1200EvcConfigEceTableRowEditorSnapPidMask = _Me1200EvcConfigEceTableRowEditorSnapPidMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 303),
    _Me1200EvcConfigEceTableRowEditorSnapPidMask_Type()
)
me1200EvcConfigEceTableRowEditorSnapPidMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorSnapPidMask.setStatus("current")
_Me1200EvcConfigEceTableRowEditorL2cpType_Type = ME1200evcL2cpType
_Me1200EvcConfigEceTableRowEditorL2cpType_Object = MibScalar
me1200EvcConfigEceTableRowEditorL2cpType = _Me1200EvcConfigEceTableRowEditorL2cpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 400),
    _Me1200EvcConfigEceTableRowEditorL2cpType_Type()
)
me1200EvcConfigEceTableRowEditorL2cpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorL2cpType.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv4Dscp_Type = Unsigned32
_Me1200EvcConfigEceTableRowEditorIpv4Dscp_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv4Dscp = _Me1200EvcConfigEceTableRowEditorIpv4Dscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 500),
    _Me1200EvcConfigEceTableRowEditorIpv4Dscp_Type()
)
me1200EvcConfigEceTableRowEditorIpv4Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv4Dscp.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv4Proto_Type = ME1200Unsigned8
_Me1200EvcConfigEceTableRowEditorIpv4Proto_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv4Proto = _Me1200EvcConfigEceTableRowEditorIpv4Proto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 501),
    _Me1200EvcConfigEceTableRowEditorIpv4Proto_Type()
)
me1200EvcConfigEceTableRowEditorIpv4Proto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv4Proto.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv4ProtoMask_Type = ME1200Unsigned8
_Me1200EvcConfigEceTableRowEditorIpv4ProtoMask_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv4ProtoMask = _Me1200EvcConfigEceTableRowEditorIpv4ProtoMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 502),
    _Me1200EvcConfigEceTableRowEditorIpv4ProtoMask_Type()
)
me1200EvcConfigEceTableRowEditorIpv4ProtoMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv4ProtoMask.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv4Fragment_Type = ME1200BitType
_Me1200EvcConfigEceTableRowEditorIpv4Fragment_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv4Fragment = _Me1200EvcConfigEceTableRowEditorIpv4Fragment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 503),
    _Me1200EvcConfigEceTableRowEditorIpv4Fragment_Type()
)
me1200EvcConfigEceTableRowEditorIpv4Fragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv4Fragment.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv4SrcIp_Type = IpAddress
_Me1200EvcConfigEceTableRowEditorIpv4SrcIp_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv4SrcIp = _Me1200EvcConfigEceTableRowEditorIpv4SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 504),
    _Me1200EvcConfigEceTableRowEditorIpv4SrcIp_Type()
)
me1200EvcConfigEceTableRowEditorIpv4SrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv4SrcIp.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv4SrcIpMask_Type = IpAddress
_Me1200EvcConfigEceTableRowEditorIpv4SrcIpMask_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv4SrcIpMask = _Me1200EvcConfigEceTableRowEditorIpv4SrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 505),
    _Me1200EvcConfigEceTableRowEditorIpv4SrcIpMask_Type()
)
me1200EvcConfigEceTableRowEditorIpv4SrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv4SrcIpMask.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv4DestIp_Type = IpAddress
_Me1200EvcConfigEceTableRowEditorIpv4DestIp_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv4DestIp = _Me1200EvcConfigEceTableRowEditorIpv4DestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 506),
    _Me1200EvcConfigEceTableRowEditorIpv4DestIp_Type()
)
me1200EvcConfigEceTableRowEditorIpv4DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv4DestIp.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv4DestIpMask_Type = IpAddress
_Me1200EvcConfigEceTableRowEditorIpv4DestIpMask_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv4DestIpMask = _Me1200EvcConfigEceTableRowEditorIpv4DestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 507),
    _Me1200EvcConfigEceTableRowEditorIpv4DestIpMask_Type()
)
me1200EvcConfigEceTableRowEditorIpv4DestIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv4DestIpMask.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv4SrcPort_Type = Unsigned32
_Me1200EvcConfigEceTableRowEditorIpv4SrcPort_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv4SrcPort = _Me1200EvcConfigEceTableRowEditorIpv4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 508),
    _Me1200EvcConfigEceTableRowEditorIpv4SrcPort_Type()
)
me1200EvcConfigEceTableRowEditorIpv4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv4SrcPort.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv4DestPort_Type = Unsigned32
_Me1200EvcConfigEceTableRowEditorIpv4DestPort_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv4DestPort = _Me1200EvcConfigEceTableRowEditorIpv4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 509),
    _Me1200EvcConfigEceTableRowEditorIpv4DestPort_Type()
)
me1200EvcConfigEceTableRowEditorIpv4DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv4DestPort.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv6Dscp_Type = Unsigned32
_Me1200EvcConfigEceTableRowEditorIpv6Dscp_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv6Dscp = _Me1200EvcConfigEceTableRowEditorIpv6Dscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 600),
    _Me1200EvcConfigEceTableRowEditorIpv6Dscp_Type()
)
me1200EvcConfigEceTableRowEditorIpv6Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv6Dscp.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv6Proto_Type = ME1200Unsigned8
_Me1200EvcConfigEceTableRowEditorIpv6Proto_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv6Proto = _Me1200EvcConfigEceTableRowEditorIpv6Proto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 601),
    _Me1200EvcConfigEceTableRowEditorIpv6Proto_Type()
)
me1200EvcConfigEceTableRowEditorIpv6Proto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv6Proto.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv6ProtoMask_Type = ME1200Unsigned8
_Me1200EvcConfigEceTableRowEditorIpv6ProtoMask_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv6ProtoMask = _Me1200EvcConfigEceTableRowEditorIpv6ProtoMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 602),
    _Me1200EvcConfigEceTableRowEditorIpv6ProtoMask_Type()
)
me1200EvcConfigEceTableRowEditorIpv6ProtoMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv6ProtoMask.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv6SrcIp_Type = InetAddressIPv6
_Me1200EvcConfigEceTableRowEditorIpv6SrcIp_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv6SrcIp = _Me1200EvcConfigEceTableRowEditorIpv6SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 603),
    _Me1200EvcConfigEceTableRowEditorIpv6SrcIp_Type()
)
me1200EvcConfigEceTableRowEditorIpv6SrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv6SrcIp.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv6SrcIpMask_Type = InetAddressIPv6
_Me1200EvcConfigEceTableRowEditorIpv6SrcIpMask_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv6SrcIpMask = _Me1200EvcConfigEceTableRowEditorIpv6SrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 604),
    _Me1200EvcConfigEceTableRowEditorIpv6SrcIpMask_Type()
)
me1200EvcConfigEceTableRowEditorIpv6SrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv6SrcIpMask.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv6DestIp_Type = InetAddressIPv6
_Me1200EvcConfigEceTableRowEditorIpv6DestIp_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv6DestIp = _Me1200EvcConfigEceTableRowEditorIpv6DestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 605),
    _Me1200EvcConfigEceTableRowEditorIpv6DestIp_Type()
)
me1200EvcConfigEceTableRowEditorIpv6DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv6DestIp.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv6DestIpMask_Type = InetAddressIPv6
_Me1200EvcConfigEceTableRowEditorIpv6DestIpMask_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv6DestIpMask = _Me1200EvcConfigEceTableRowEditorIpv6DestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 606),
    _Me1200EvcConfigEceTableRowEditorIpv6DestIpMask_Type()
)
me1200EvcConfigEceTableRowEditorIpv6DestIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv6DestIpMask.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv6SrcPort_Type = Unsigned32
_Me1200EvcConfigEceTableRowEditorIpv6SrcPort_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv6SrcPort = _Me1200EvcConfigEceTableRowEditorIpv6SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 607),
    _Me1200EvcConfigEceTableRowEditorIpv6SrcPort_Type()
)
me1200EvcConfigEceTableRowEditorIpv6SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv6SrcPort.setStatus("current")
_Me1200EvcConfigEceTableRowEditorIpv6DestPort_Type = Unsigned32
_Me1200EvcConfigEceTableRowEditorIpv6DestPort_Object = MibScalar
me1200EvcConfigEceTableRowEditorIpv6DestPort = _Me1200EvcConfigEceTableRowEditorIpv6DestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 608),
    _Me1200EvcConfigEceTableRowEditorIpv6DestPort_Type()
)
me1200EvcConfigEceTableRowEditorIpv6DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorIpv6DestPort.setStatus("current")
_Me1200EvcConfigEceTableRowEditorDirection_Type = ME1200evcDirection
_Me1200EvcConfigEceTableRowEditorDirection_Object = MibScalar
me1200EvcConfigEceTableRowEditorDirection = _Me1200EvcConfigEceTableRowEditorDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1000),
    _Me1200EvcConfigEceTableRowEditorDirection_Type()
)
me1200EvcConfigEceTableRowEditorDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorDirection.setStatus("current")
_Me1200EvcConfigEceTableRowEditorRuleType_Type = ME1200evcRuleType
_Me1200EvcConfigEceTableRowEditorRuleType_Object = MibScalar
me1200EvcConfigEceTableRowEditorRuleType = _Me1200EvcConfigEceTableRowEditorRuleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1010),
    _Me1200EvcConfigEceTableRowEditorRuleType_Type()
)
me1200EvcConfigEceTableRowEditorRuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorRuleType.setStatus("current")
_Me1200EvcConfigEceTableRowEditorTxLookup_Type = ME1200evcTxLookup
_Me1200EvcConfigEceTableRowEditorTxLookup_Object = MibScalar
me1200EvcConfigEceTableRowEditorTxLookup = _Me1200EvcConfigEceTableRowEditorTxLookup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1011),
    _Me1200EvcConfigEceTableRowEditorTxLookup_Type()
)
me1200EvcConfigEceTableRowEditorTxLookup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorTxLookup.setStatus("current")
_Me1200EvcConfigEceTableRowEditorPopTag_Type = ME1200evcPopTag
_Me1200EvcConfigEceTableRowEditorPopTag_Object = MibScalar
me1200EvcConfigEceTableRowEditorPopTag = _Me1200EvcConfigEceTableRowEditorPopTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1020),
    _Me1200EvcConfigEceTableRowEditorPopTag_Type()
)
me1200EvcConfigEceTableRowEditorPopTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorPopTag.setStatus("current")
_Me1200EvcConfigEceTableRowEditorOtAddEnable_Type = TruthValue
_Me1200EvcConfigEceTableRowEditorOtAddEnable_Object = MibScalar
me1200EvcConfigEceTableRowEditorOtAddEnable = _Me1200EvcConfigEceTableRowEditorOtAddEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1100),
    _Me1200EvcConfigEceTableRowEditorOtAddEnable_Type()
)
me1200EvcConfigEceTableRowEditorOtAddEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorOtAddEnable.setStatus("current")
_Me1200EvcConfigEceTableRowEditorOtAddVid_Type = ME1200Unsigned16
_Me1200EvcConfigEceTableRowEditorOtAddVid_Object = MibScalar
me1200EvcConfigEceTableRowEditorOtAddVid = _Me1200EvcConfigEceTableRowEditorOtAddVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1101),
    _Me1200EvcConfigEceTableRowEditorOtAddVid_Type()
)
me1200EvcConfigEceTableRowEditorOtAddVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorOtAddVid.setStatus("current")
_Me1200EvcConfigEceTableRowEditorOtAddPcpMode_Type = ME1200evcPcpMode
_Me1200EvcConfigEceTableRowEditorOtAddPcpMode_Object = MibScalar
me1200EvcConfigEceTableRowEditorOtAddPcpMode = _Me1200EvcConfigEceTableRowEditorOtAddPcpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1102),
    _Me1200EvcConfigEceTableRowEditorOtAddPcpMode_Type()
)
me1200EvcConfigEceTableRowEditorOtAddPcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorOtAddPcpMode.setStatus("current")
_Me1200EvcConfigEceTableRowEditorOtAddPcpDeiPreserve_Type = TruthValue
_Me1200EvcConfigEceTableRowEditorOtAddPcpDeiPreserve_Object = MibScalar
me1200EvcConfigEceTableRowEditorOtAddPcpDeiPreserve = _Me1200EvcConfigEceTableRowEditorOtAddPcpDeiPreserve_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1103),
    _Me1200EvcConfigEceTableRowEditorOtAddPcpDeiPreserve_Type()
)
me1200EvcConfigEceTableRowEditorOtAddPcpDeiPreserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorOtAddPcpDeiPreserve.setStatus("current")
_Me1200EvcConfigEceTableRowEditorOtAddPcp_Type = Unsigned32
_Me1200EvcConfigEceTableRowEditorOtAddPcp_Object = MibScalar
me1200EvcConfigEceTableRowEditorOtAddPcp = _Me1200EvcConfigEceTableRowEditorOtAddPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1104),
    _Me1200EvcConfigEceTableRowEditorOtAddPcp_Type()
)
me1200EvcConfigEceTableRowEditorOtAddPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorOtAddPcp.setStatus("current")
_Me1200EvcConfigEceTableRowEditorOtAddDeiMode_Type = ME1200evcDeiMode
_Me1200EvcConfigEceTableRowEditorOtAddDeiMode_Object = MibScalar
me1200EvcConfigEceTableRowEditorOtAddDeiMode = _Me1200EvcConfigEceTableRowEditorOtAddDeiMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1105),
    _Me1200EvcConfigEceTableRowEditorOtAddDeiMode_Type()
)
me1200EvcConfigEceTableRowEditorOtAddDeiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorOtAddDeiMode.setStatus("current")
_Me1200EvcConfigEceTableRowEditorOtAddDei_Type = ME1200Unsigned8
_Me1200EvcConfigEceTableRowEditorOtAddDei_Object = MibScalar
me1200EvcConfigEceTableRowEditorOtAddDei = _Me1200EvcConfigEceTableRowEditorOtAddDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1106),
    _Me1200EvcConfigEceTableRowEditorOtAddDei_Type()
)
me1200EvcConfigEceTableRowEditorOtAddDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorOtAddDei.setStatus("current")
_Me1200EvcConfigEceTableRowEditorItAddType_Type = ME1200evcInnerTagType
_Me1200EvcConfigEceTableRowEditorItAddType_Object = MibScalar
me1200EvcConfigEceTableRowEditorItAddType = _Me1200EvcConfigEceTableRowEditorItAddType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1200),
    _Me1200EvcConfigEceTableRowEditorItAddType_Type()
)
me1200EvcConfigEceTableRowEditorItAddType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorItAddType.setStatus("current")
_Me1200EvcConfigEceTableRowEditorItAddVid_Type = ME1200Unsigned16
_Me1200EvcConfigEceTableRowEditorItAddVid_Object = MibScalar
me1200EvcConfigEceTableRowEditorItAddVid = _Me1200EvcConfigEceTableRowEditorItAddVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1201),
    _Me1200EvcConfigEceTableRowEditorItAddVid_Type()
)
me1200EvcConfigEceTableRowEditorItAddVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorItAddVid.setStatus("current")
_Me1200EvcConfigEceTableRowEditorItAddPcpMode_Type = ME1200evcPcpMode
_Me1200EvcConfigEceTableRowEditorItAddPcpMode_Object = MibScalar
me1200EvcConfigEceTableRowEditorItAddPcpMode = _Me1200EvcConfigEceTableRowEditorItAddPcpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1202),
    _Me1200EvcConfigEceTableRowEditorItAddPcpMode_Type()
)
me1200EvcConfigEceTableRowEditorItAddPcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorItAddPcpMode.setStatus("current")
_Me1200EvcConfigEceTableRowEditorItAddPcpDeiPreserve_Type = TruthValue
_Me1200EvcConfigEceTableRowEditorItAddPcpDeiPreserve_Object = MibScalar
me1200EvcConfigEceTableRowEditorItAddPcpDeiPreserve = _Me1200EvcConfigEceTableRowEditorItAddPcpDeiPreserve_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1203),
    _Me1200EvcConfigEceTableRowEditorItAddPcpDeiPreserve_Type()
)
me1200EvcConfigEceTableRowEditorItAddPcpDeiPreserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorItAddPcpDeiPreserve.setStatus("current")
_Me1200EvcConfigEceTableRowEditorItAddPcp_Type = Unsigned32
_Me1200EvcConfigEceTableRowEditorItAddPcp_Object = MibScalar
me1200EvcConfigEceTableRowEditorItAddPcp = _Me1200EvcConfigEceTableRowEditorItAddPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1204),
    _Me1200EvcConfigEceTableRowEditorItAddPcp_Type()
)
me1200EvcConfigEceTableRowEditorItAddPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorItAddPcp.setStatus("current")
_Me1200EvcConfigEceTableRowEditorItAddDeiMode_Type = ME1200evcDeiMode
_Me1200EvcConfigEceTableRowEditorItAddDeiMode_Object = MibScalar
me1200EvcConfigEceTableRowEditorItAddDeiMode = _Me1200EvcConfigEceTableRowEditorItAddDeiMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1205),
    _Me1200EvcConfigEceTableRowEditorItAddDeiMode_Type()
)
me1200EvcConfigEceTableRowEditorItAddDeiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorItAddDeiMode.setStatus("current")
_Me1200EvcConfigEceTableRowEditorItAddDei_Type = ME1200Unsigned8
_Me1200EvcConfigEceTableRowEditorItAddDei_Object = MibScalar
me1200EvcConfigEceTableRowEditorItAddDei = _Me1200EvcConfigEceTableRowEditorItAddDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1206),
    _Me1200EvcConfigEceTableRowEditorItAddDei_Type()
)
me1200EvcConfigEceTableRowEditorItAddDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorItAddDei.setStatus("current")
_Me1200EvcConfigEceTableRowEditorEvcId_Type = ME1200Unsigned16
_Me1200EvcConfigEceTableRowEditorEvcId_Object = MibScalar
me1200EvcConfigEceTableRowEditorEvcId = _Me1200EvcConfigEceTableRowEditorEvcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1300),
    _Me1200EvcConfigEceTableRowEditorEvcId_Type()
)
me1200EvcConfigEceTableRowEditorEvcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorEvcId.setStatus("current")
_Me1200EvcConfigEceTableRowEditorPolicerOp_Type = ME1200evcPolicerOp
_Me1200EvcConfigEceTableRowEditorPolicerOp_Object = MibScalar
me1200EvcConfigEceTableRowEditorPolicerOp = _Me1200EvcConfigEceTableRowEditorPolicerOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1301),
    _Me1200EvcConfigEceTableRowEditorPolicerOp_Type()
)
me1200EvcConfigEceTableRowEditorPolicerOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorPolicerOp.setStatus("current")
_Me1200EvcConfigEceTableRowEditorPolicerId_Type = ME1200Unsigned16
_Me1200EvcConfigEceTableRowEditorPolicerId_Object = MibScalar
me1200EvcConfigEceTableRowEditorPolicerId = _Me1200EvcConfigEceTableRowEditorPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1302),
    _Me1200EvcConfigEceTableRowEditorPolicerId_Type()
)
me1200EvcConfigEceTableRowEditorPolicerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorPolicerId.setStatus("current")
_Me1200EvcConfigEceTableRowEditorPolicyNo_Type = Unsigned32
_Me1200EvcConfigEceTableRowEditorPolicyNo_Object = MibScalar
me1200EvcConfigEceTableRowEditorPolicyNo = _Me1200EvcConfigEceTableRowEditorPolicyNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1310),
    _Me1200EvcConfigEceTableRowEditorPolicyNo_Type()
)
me1200EvcConfigEceTableRowEditorPolicyNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorPolicyNo.setStatus("current")
_Me1200EvcConfigEceTableRowEditorCosEnable_Type = TruthValue
_Me1200EvcConfigEceTableRowEditorCosEnable_Object = MibScalar
me1200EvcConfigEceTableRowEditorCosEnable = _Me1200EvcConfigEceTableRowEditorCosEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1320),
    _Me1200EvcConfigEceTableRowEditorCosEnable_Type()
)
me1200EvcConfigEceTableRowEditorCosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorCosEnable.setStatus("current")
_Me1200EvcConfigEceTableRowEditorCos_Type = Unsigned32
_Me1200EvcConfigEceTableRowEditorCos_Object = MibScalar
me1200EvcConfigEceTableRowEditorCos = _Me1200EvcConfigEceTableRowEditorCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1321),
    _Me1200EvcConfigEceTableRowEditorCos_Type()
)
me1200EvcConfigEceTableRowEditorCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorCos.setStatus("current")
_Me1200EvcConfigEceTableRowEditorDpEnable_Type = TruthValue
_Me1200EvcConfigEceTableRowEditorDpEnable_Object = MibScalar
me1200EvcConfigEceTableRowEditorDpEnable = _Me1200EvcConfigEceTableRowEditorDpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1330),
    _Me1200EvcConfigEceTableRowEditorDpEnable_Type()
)
me1200EvcConfigEceTableRowEditorDpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorDpEnable.setStatus("current")
_Me1200EvcConfigEceTableRowEditorDp_Type = ME1200Unsigned8
_Me1200EvcConfigEceTableRowEditorDp_Object = MibScalar
me1200EvcConfigEceTableRowEditorDp = _Me1200EvcConfigEceTableRowEditorDp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1331),
    _Me1200EvcConfigEceTableRowEditorDp_Type()
)
me1200EvcConfigEceTableRowEditorDp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorDp.setStatus("current")
_Me1200EvcConfigEceTableRowEditorL2cpMode_Type = ME1200evcEceL2cpMode
_Me1200EvcConfigEceTableRowEditorL2cpMode_Object = MibScalar
me1200EvcConfigEceTableRowEditorL2cpMode = _Me1200EvcConfigEceTableRowEditorL2cpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1332),
    _Me1200EvcConfigEceTableRowEditorL2cpMode_Type()
)
me1200EvcConfigEceTableRowEditorL2cpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorL2cpMode.setStatus("current")
_Me1200EvcConfigEceTableRowEditorL2cpDmac_Type = ME1200evcL2cpDmac
_Me1200EvcConfigEceTableRowEditorL2cpDmac_Object = MibScalar
me1200EvcConfigEceTableRowEditorL2cpDmac = _Me1200EvcConfigEceTableRowEditorL2cpDmac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 1333),
    _Me1200EvcConfigEceTableRowEditorL2cpDmac_Type()
)
me1200EvcConfigEceTableRowEditorL2cpDmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorL2cpDmac.setStatus("current")
_Me1200EvcConfigEceTableRowEditorAction_Type = ME1200RowEditorState
_Me1200EvcConfigEceTableRowEditorAction_Object = MibScalar
me1200EvcConfigEceTableRowEditorAction = _Me1200EvcConfigEceTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 2, 10000),
    _Me1200EvcConfigEceTableRowEditorAction_Type()
)
me1200EvcConfigEceTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorAction.setStatus("current")
_Me1200EvcConfigEcePrecedenceTable_Object = MibTable
me1200EvcConfigEcePrecedenceTable = _Me1200EvcConfigEcePrecedenceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    me1200EvcConfigEcePrecedenceTable.setStatus("current")
_Me1200EvcConfigEcePrecedenceEntry_Object = MibTableRow
me1200EvcConfigEcePrecedenceEntry = _Me1200EvcConfigEcePrecedenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 3, 1)
)
me1200EvcConfigEcePrecedenceEntry.setIndexNames(
    (0, "ME1200-EVC-MIB", "me1200EvcConfigEcePrecedenceIndex"),
)
if mibBuilder.loadTexts:
    me1200EvcConfigEcePrecedenceEntry.setStatus("current")


class _Me1200EvcConfigEcePrecedenceIndex_Type(Integer32):
    """Custom type me1200EvcConfigEcePrecedenceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Me1200EvcConfigEcePrecedenceIndex_Type.__name__ = "Integer32"
_Me1200EvcConfigEcePrecedenceIndex_Object = MibTableColumn
me1200EvcConfigEcePrecedenceIndex = _Me1200EvcConfigEcePrecedenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 3, 1, 1),
    _Me1200EvcConfigEcePrecedenceIndex_Type()
)
me1200EvcConfigEcePrecedenceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcConfigEcePrecedenceIndex.setStatus("current")
_Me1200EvcConfigEcePrecedenceEceId_Type = Unsigned32
_Me1200EvcConfigEcePrecedenceEceId_Object = MibTableColumn
me1200EvcConfigEcePrecedenceEceId = _Me1200EvcConfigEcePrecedenceEceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 5, 3, 1, 2),
    _Me1200EvcConfigEcePrecedenceEceId_Type()
)
me1200EvcConfigEcePrecedenceEceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcConfigEcePrecedenceEceId.setStatus("current")
_Me1200EvcConfigEvcInterfaceTable_Object = MibTable
me1200EvcConfigEvcInterfaceTable = _Me1200EvcConfigEvcInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 6)
)
if mibBuilder.loadTexts:
    me1200EvcConfigEvcInterfaceTable.setStatus("current")
_Me1200EvcConfigEvcInterfaceEntry_Object = MibTableRow
me1200EvcConfigEvcInterfaceEntry = _Me1200EvcConfigEvcInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 6, 1)
)
me1200EvcConfigEvcInterfaceEntry.setIndexNames(
    (0, "ME1200-EVC-MIB", "me1200EvcConfigEvcInterfaceEvcId"),
    (0, "ME1200-EVC-MIB", "me1200EvcConfigEvcInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    me1200EvcConfigEvcInterfaceEntry.setStatus("current")


class _Me1200EvcConfigEvcInterfaceEvcId_Type(Integer32):
    """Custom type me1200EvcConfigEvcInterfaceEvcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Me1200EvcConfigEvcInterfaceEvcId_Type.__name__ = "Integer32"
_Me1200EvcConfigEvcInterfaceEvcId_Object = MibTableColumn
me1200EvcConfigEvcInterfaceEvcId = _Me1200EvcConfigEvcInterfaceEvcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 6, 1, 1),
    _Me1200EvcConfigEvcInterfaceEvcId_Type()
)
me1200EvcConfigEvcInterfaceEvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcInterfaceEvcId.setStatus("current")
_Me1200EvcConfigEvcInterfaceIfIndex_Type = ME1200InterfaceIndex
_Me1200EvcConfigEvcInterfaceIfIndex_Object = MibTableColumn
me1200EvcConfigEvcInterfaceIfIndex = _Me1200EvcConfigEvcInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 6, 1, 2),
    _Me1200EvcConfigEvcInterfaceIfIndex_Type()
)
me1200EvcConfigEvcInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcInterfaceIfIndex.setStatus("current")
_Me1200EvcConfigEvcInterfaceHqosId_Type = ME1200Unsigned16
_Me1200EvcConfigEvcInterfaceHqosId_Object = MibTableColumn
me1200EvcConfigEvcInterfaceHqosId = _Me1200EvcConfigEvcInterfaceHqosId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 2, 6, 1, 3),
    _Me1200EvcConfigEvcInterfaceHqosId_Type()
)
me1200EvcConfigEvcInterfaceHqosId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcConfigEvcInterfaceHqosId.setStatus("current")
_Me1200EvcStatus_ObjectIdentity = ObjectIdentity
me1200EvcStatus = _Me1200EvcStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3)
)
_Me1200EvcStatusEvcTable_Object = MibTable
me1200EvcStatusEvcTable = _Me1200EvcStatusEvcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 3)
)
if mibBuilder.loadTexts:
    me1200EvcStatusEvcTable.setStatus("current")
_Me1200EvcStatusEvcEntry_Object = MibTableRow
me1200EvcStatusEvcEntry = _Me1200EvcStatusEvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 3, 1)
)
me1200EvcStatusEvcEntry.setIndexNames(
    (0, "ME1200-EVC-MIB", "me1200EvcStatusEvcEvcId"),
)
if mibBuilder.loadTexts:
    me1200EvcStatusEvcEntry.setStatus("current")


class _Me1200EvcStatusEvcEvcId_Type(Integer32):
    """Custom type me1200EvcStatusEvcEvcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Me1200EvcStatusEvcEvcId_Type.__name__ = "Integer32"
_Me1200EvcStatusEvcEvcId_Object = MibTableColumn
me1200EvcStatusEvcEvcId = _Me1200EvcStatusEvcEvcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 3, 1, 1),
    _Me1200EvcStatusEvcEvcId_Type()
)
me1200EvcStatusEvcEvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcStatusEvcEvcId.setStatus("current")
_Me1200EvcStatusEvcConflict_Type = TruthValue
_Me1200EvcStatusEvcConflict_Object = MibTableColumn
me1200EvcStatusEvcConflict = _Me1200EvcStatusEvcConflict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 3, 1, 2),
    _Me1200EvcStatusEvcConflict_Type()
)
me1200EvcStatusEvcConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEvcConflict.setStatus("current")
_Me1200EvcStatusEceTable_Object = MibTable
me1200EvcStatusEceTable = _Me1200EvcStatusEceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 4)
)
if mibBuilder.loadTexts:
    me1200EvcStatusEceTable.setStatus("current")
_Me1200EvcStatusEceEntry_Object = MibTableRow
me1200EvcStatusEceEntry = _Me1200EvcStatusEceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 4, 1)
)
me1200EvcStatusEceEntry.setIndexNames(
    (0, "ME1200-EVC-MIB", "me1200EvcStatusEceIndex"),
)
if mibBuilder.loadTexts:
    me1200EvcStatusEceEntry.setStatus("current")


class _Me1200EvcStatusEceIndex_Type(Integer32):
    """Custom type me1200EvcStatusEceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Me1200EvcStatusEceIndex_Type.__name__ = "Integer32"
_Me1200EvcStatusEceIndex_Object = MibTableColumn
me1200EvcStatusEceIndex = _Me1200EvcStatusEceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 4, 1, 1),
    _Me1200EvcStatusEceIndex_Type()
)
me1200EvcStatusEceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcStatusEceIndex.setStatus("current")
_Me1200EvcStatusEceConflict_Type = TruthValue
_Me1200EvcStatusEceConflict_Object = MibTableColumn
me1200EvcStatusEceConflict = _Me1200EvcStatusEceConflict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 4, 1, 2),
    _Me1200EvcStatusEceConflict_Type()
)
me1200EvcStatusEceConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEceConflict.setStatus("current")
_Me1200EvcStatusEvcInterfaceTable_Object = MibTable
me1200EvcStatusEvcInterfaceTable = _Me1200EvcStatusEvcInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 5)
)
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceTable.setStatus("current")
_Me1200EvcStatusEvcInterfaceEntry_Object = MibTableRow
me1200EvcStatusEvcInterfaceEntry = _Me1200EvcStatusEvcInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 5, 1)
)
me1200EvcStatusEvcInterfaceEntry.setIndexNames(
    (0, "ME1200-EVC-MIB", "me1200EvcStatusEvcInterfaceEvcId"),
    (0, "ME1200-EVC-MIB", "me1200EvcStatusEvcInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceEntry.setStatus("current")


class _Me1200EvcStatusEvcInterfaceEvcId_Type(Integer32):
    """Custom type me1200EvcStatusEvcInterfaceEvcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Me1200EvcStatusEvcInterfaceEvcId_Type.__name__ = "Integer32"
_Me1200EvcStatusEvcInterfaceEvcId_Object = MibTableColumn
me1200EvcStatusEvcInterfaceEvcId = _Me1200EvcStatusEvcInterfaceEvcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 5, 1, 1),
    _Me1200EvcStatusEvcInterfaceEvcId_Type()
)
me1200EvcStatusEvcInterfaceEvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceEvcId.setStatus("current")
_Me1200EvcStatusEvcInterfaceIfIndex_Type = ME1200InterfaceIndex
_Me1200EvcStatusEvcInterfaceIfIndex_Object = MibTableColumn
me1200EvcStatusEvcInterfaceIfIndex = _Me1200EvcStatusEvcInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 5, 1, 2),
    _Me1200EvcStatusEvcInterfaceIfIndex_Type()
)
me1200EvcStatusEvcInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceIfIndex.setStatus("current")
_Me1200EvcStatusEvcInterfaceRxGreenFrames_Type = Counter64
_Me1200EvcStatusEvcInterfaceRxGreenFrames_Object = MibTableColumn
me1200EvcStatusEvcInterfaceRxGreenFrames = _Me1200EvcStatusEvcInterfaceRxGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 5, 1, 3),
    _Me1200EvcStatusEvcInterfaceRxGreenFrames_Type()
)
me1200EvcStatusEvcInterfaceRxGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceRxGreenFrames.setStatus("current")
_Me1200EvcStatusEvcInterfaceRxGreenBytes_Type = Counter64
_Me1200EvcStatusEvcInterfaceRxGreenBytes_Object = MibTableColumn
me1200EvcStatusEvcInterfaceRxGreenBytes = _Me1200EvcStatusEvcInterfaceRxGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 5, 1, 4),
    _Me1200EvcStatusEvcInterfaceRxGreenBytes_Type()
)
me1200EvcStatusEvcInterfaceRxGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceRxGreenBytes.setStatus("current")
_Me1200EvcStatusEvcInterfaceRxYellowFrames_Type = Counter64
_Me1200EvcStatusEvcInterfaceRxYellowFrames_Object = MibTableColumn
me1200EvcStatusEvcInterfaceRxYellowFrames = _Me1200EvcStatusEvcInterfaceRxYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 5, 1, 5),
    _Me1200EvcStatusEvcInterfaceRxYellowFrames_Type()
)
me1200EvcStatusEvcInterfaceRxYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceRxYellowFrames.setStatus("current")
_Me1200EvcStatusEvcInterfaceRxYellowBytes_Type = Counter64
_Me1200EvcStatusEvcInterfaceRxYellowBytes_Object = MibTableColumn
me1200EvcStatusEvcInterfaceRxYellowBytes = _Me1200EvcStatusEvcInterfaceRxYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 5, 1, 6),
    _Me1200EvcStatusEvcInterfaceRxYellowBytes_Type()
)
me1200EvcStatusEvcInterfaceRxYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceRxYellowBytes.setStatus("current")
_Me1200EvcStatusEvcInterfaceRxRedFrames_Type = Counter64
_Me1200EvcStatusEvcInterfaceRxRedFrames_Object = MibTableColumn
me1200EvcStatusEvcInterfaceRxRedFrames = _Me1200EvcStatusEvcInterfaceRxRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 5, 1, 7),
    _Me1200EvcStatusEvcInterfaceRxRedFrames_Type()
)
me1200EvcStatusEvcInterfaceRxRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceRxRedFrames.setStatus("current")
_Me1200EvcStatusEvcInterfaceRxRedBytes_Type = Counter64
_Me1200EvcStatusEvcInterfaceRxRedBytes_Object = MibTableColumn
me1200EvcStatusEvcInterfaceRxRedBytes = _Me1200EvcStatusEvcInterfaceRxRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 5, 1, 8),
    _Me1200EvcStatusEvcInterfaceRxRedBytes_Type()
)
me1200EvcStatusEvcInterfaceRxRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceRxRedBytes.setStatus("current")
_Me1200EvcStatusEvcInterfaceRxDiscardFrames_Type = Counter64
_Me1200EvcStatusEvcInterfaceRxDiscardFrames_Object = MibTableColumn
me1200EvcStatusEvcInterfaceRxDiscardFrames = _Me1200EvcStatusEvcInterfaceRxDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 5, 1, 9),
    _Me1200EvcStatusEvcInterfaceRxDiscardFrames_Type()
)
me1200EvcStatusEvcInterfaceRxDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceRxDiscardFrames.setStatus("current")
_Me1200EvcStatusEvcInterfaceRxDiscardBytes_Type = Counter64
_Me1200EvcStatusEvcInterfaceRxDiscardBytes_Object = MibTableColumn
me1200EvcStatusEvcInterfaceRxDiscardBytes = _Me1200EvcStatusEvcInterfaceRxDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 5, 1, 10),
    _Me1200EvcStatusEvcInterfaceRxDiscardBytes_Type()
)
me1200EvcStatusEvcInterfaceRxDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceRxDiscardBytes.setStatus("current")
_Me1200EvcStatusEvcInterfaceTxGreenFrames_Type = Counter64
_Me1200EvcStatusEvcInterfaceTxGreenFrames_Object = MibTableColumn
me1200EvcStatusEvcInterfaceTxGreenFrames = _Me1200EvcStatusEvcInterfaceTxGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 5, 1, 100),
    _Me1200EvcStatusEvcInterfaceTxGreenFrames_Type()
)
me1200EvcStatusEvcInterfaceTxGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceTxGreenFrames.setStatus("current")
_Me1200EvcStatusEvcInterfaceTxGreenBytes_Type = Counter64
_Me1200EvcStatusEvcInterfaceTxGreenBytes_Object = MibTableColumn
me1200EvcStatusEvcInterfaceTxGreenBytes = _Me1200EvcStatusEvcInterfaceTxGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 5, 1, 101),
    _Me1200EvcStatusEvcInterfaceTxGreenBytes_Type()
)
me1200EvcStatusEvcInterfaceTxGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceTxGreenBytes.setStatus("current")
_Me1200EvcStatusEvcInterfaceTxYellowFrames_Type = Counter64
_Me1200EvcStatusEvcInterfaceTxYellowFrames_Object = MibTableColumn
me1200EvcStatusEvcInterfaceTxYellowFrames = _Me1200EvcStatusEvcInterfaceTxYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 5, 1, 102),
    _Me1200EvcStatusEvcInterfaceTxYellowFrames_Type()
)
me1200EvcStatusEvcInterfaceTxYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceTxYellowFrames.setStatus("current")
_Me1200EvcStatusEvcInterfaceTxYellowBytes_Type = Counter64
_Me1200EvcStatusEvcInterfaceTxYellowBytes_Object = MibTableColumn
me1200EvcStatusEvcInterfaceTxYellowBytes = _Me1200EvcStatusEvcInterfaceTxYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 5, 1, 103),
    _Me1200EvcStatusEvcInterfaceTxYellowBytes_Type()
)
me1200EvcStatusEvcInterfaceTxYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceTxYellowBytes.setStatus("current")
_Me1200EvcStatusEvcInterfaceTxDiscardFrames_Type = Counter64
_Me1200EvcStatusEvcInterfaceTxDiscardFrames_Object = MibTableColumn
me1200EvcStatusEvcInterfaceTxDiscardFrames = _Me1200EvcStatusEvcInterfaceTxDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 5, 1, 104),
    _Me1200EvcStatusEvcInterfaceTxDiscardFrames_Type()
)
me1200EvcStatusEvcInterfaceTxDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceTxDiscardFrames.setStatus("current")
_Me1200EvcStatusEvcInterfaceTxDiscardBytes_Type = Counter64
_Me1200EvcStatusEvcInterfaceTxDiscardBytes_Object = MibTableColumn
me1200EvcStatusEvcInterfaceTxDiscardBytes = _Me1200EvcStatusEvcInterfaceTxDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 5, 1, 105),
    _Me1200EvcStatusEvcInterfaceTxDiscardBytes_Type()
)
me1200EvcStatusEvcInterfaceTxDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceTxDiscardBytes.setStatus("current")
_Me1200EvcStatusEceInterfaceTable_Object = MibTable
me1200EvcStatusEceInterfaceTable = _Me1200EvcStatusEceInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 6)
)
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceTable.setStatus("current")
_Me1200EvcStatusEceInterfaceEntry_Object = MibTableRow
me1200EvcStatusEceInterfaceEntry = _Me1200EvcStatusEceInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 6, 1)
)
me1200EvcStatusEceInterfaceEntry.setIndexNames(
    (0, "ME1200-EVC-MIB", "me1200EvcStatusEceInterfaceIndex"),
    (0, "ME1200-EVC-MIB", "me1200EvcStatusEceInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceEntry.setStatus("current")


class _Me1200EvcStatusEceInterfaceIndex_Type(Integer32):
    """Custom type me1200EvcStatusEceInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Me1200EvcStatusEceInterfaceIndex_Type.__name__ = "Integer32"
_Me1200EvcStatusEceInterfaceIndex_Object = MibTableColumn
me1200EvcStatusEceInterfaceIndex = _Me1200EvcStatusEceInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 6, 1, 1),
    _Me1200EvcStatusEceInterfaceIndex_Type()
)
me1200EvcStatusEceInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceIndex.setStatus("current")
_Me1200EvcStatusEceInterfaceIfIndex_Type = ME1200InterfaceIndex
_Me1200EvcStatusEceInterfaceIfIndex_Object = MibTableColumn
me1200EvcStatusEceInterfaceIfIndex = _Me1200EvcStatusEceInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 6, 1, 2),
    _Me1200EvcStatusEceInterfaceIfIndex_Type()
)
me1200EvcStatusEceInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceIfIndex.setStatus("current")
_Me1200EvcStatusEceInterfaceRxGreenFrames_Type = Counter64
_Me1200EvcStatusEceInterfaceRxGreenFrames_Object = MibTableColumn
me1200EvcStatusEceInterfaceRxGreenFrames = _Me1200EvcStatusEceInterfaceRxGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 6, 1, 3),
    _Me1200EvcStatusEceInterfaceRxGreenFrames_Type()
)
me1200EvcStatusEceInterfaceRxGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceRxGreenFrames.setStatus("current")
_Me1200EvcStatusEceInterfaceRxGreenBytes_Type = Counter64
_Me1200EvcStatusEceInterfaceRxGreenBytes_Object = MibTableColumn
me1200EvcStatusEceInterfaceRxGreenBytes = _Me1200EvcStatusEceInterfaceRxGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 6, 1, 4),
    _Me1200EvcStatusEceInterfaceRxGreenBytes_Type()
)
me1200EvcStatusEceInterfaceRxGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceRxGreenBytes.setStatus("current")
_Me1200EvcStatusEceInterfaceRxYellowFrames_Type = Counter64
_Me1200EvcStatusEceInterfaceRxYellowFrames_Object = MibTableColumn
me1200EvcStatusEceInterfaceRxYellowFrames = _Me1200EvcStatusEceInterfaceRxYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 6, 1, 5),
    _Me1200EvcStatusEceInterfaceRxYellowFrames_Type()
)
me1200EvcStatusEceInterfaceRxYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceRxYellowFrames.setStatus("current")
_Me1200EvcStatusEceInterfaceRxYellowBytes_Type = Counter64
_Me1200EvcStatusEceInterfaceRxYellowBytes_Object = MibTableColumn
me1200EvcStatusEceInterfaceRxYellowBytes = _Me1200EvcStatusEceInterfaceRxYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 6, 1, 6),
    _Me1200EvcStatusEceInterfaceRxYellowBytes_Type()
)
me1200EvcStatusEceInterfaceRxYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceRxYellowBytes.setStatus("current")
_Me1200EvcStatusEceInterfaceRxRedFrames_Type = Counter64
_Me1200EvcStatusEceInterfaceRxRedFrames_Object = MibTableColumn
me1200EvcStatusEceInterfaceRxRedFrames = _Me1200EvcStatusEceInterfaceRxRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 6, 1, 7),
    _Me1200EvcStatusEceInterfaceRxRedFrames_Type()
)
me1200EvcStatusEceInterfaceRxRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceRxRedFrames.setStatus("current")
_Me1200EvcStatusEceInterfaceRxRedBytes_Type = Counter64
_Me1200EvcStatusEceInterfaceRxRedBytes_Object = MibTableColumn
me1200EvcStatusEceInterfaceRxRedBytes = _Me1200EvcStatusEceInterfaceRxRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 6, 1, 8),
    _Me1200EvcStatusEceInterfaceRxRedBytes_Type()
)
me1200EvcStatusEceInterfaceRxRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceRxRedBytes.setStatus("current")
_Me1200EvcStatusEceInterfaceRxDiscardFrames_Type = Counter64
_Me1200EvcStatusEceInterfaceRxDiscardFrames_Object = MibTableColumn
me1200EvcStatusEceInterfaceRxDiscardFrames = _Me1200EvcStatusEceInterfaceRxDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 6, 1, 9),
    _Me1200EvcStatusEceInterfaceRxDiscardFrames_Type()
)
me1200EvcStatusEceInterfaceRxDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceRxDiscardFrames.setStatus("current")
_Me1200EvcStatusEceInterfaceRxDiscardBytes_Type = Counter64
_Me1200EvcStatusEceInterfaceRxDiscardBytes_Object = MibTableColumn
me1200EvcStatusEceInterfaceRxDiscardBytes = _Me1200EvcStatusEceInterfaceRxDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 6, 1, 10),
    _Me1200EvcStatusEceInterfaceRxDiscardBytes_Type()
)
me1200EvcStatusEceInterfaceRxDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceRxDiscardBytes.setStatus("current")
_Me1200EvcStatusEceInterfaceTxGreenFrames_Type = Counter64
_Me1200EvcStatusEceInterfaceTxGreenFrames_Object = MibTableColumn
me1200EvcStatusEceInterfaceTxGreenFrames = _Me1200EvcStatusEceInterfaceTxGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 6, 1, 100),
    _Me1200EvcStatusEceInterfaceTxGreenFrames_Type()
)
me1200EvcStatusEceInterfaceTxGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceTxGreenFrames.setStatus("current")
_Me1200EvcStatusEceInterfaceTxGreenBytes_Type = Counter64
_Me1200EvcStatusEceInterfaceTxGreenBytes_Object = MibTableColumn
me1200EvcStatusEceInterfaceTxGreenBytes = _Me1200EvcStatusEceInterfaceTxGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 6, 1, 101),
    _Me1200EvcStatusEceInterfaceTxGreenBytes_Type()
)
me1200EvcStatusEceInterfaceTxGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceTxGreenBytes.setStatus("current")
_Me1200EvcStatusEceInterfaceTxYellowFrames_Type = Counter64
_Me1200EvcStatusEceInterfaceTxYellowFrames_Object = MibTableColumn
me1200EvcStatusEceInterfaceTxYellowFrames = _Me1200EvcStatusEceInterfaceTxYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 6, 1, 102),
    _Me1200EvcStatusEceInterfaceTxYellowFrames_Type()
)
me1200EvcStatusEceInterfaceTxYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceTxYellowFrames.setStatus("current")
_Me1200EvcStatusEceInterfaceTxYellowBytes_Type = Counter64
_Me1200EvcStatusEceInterfaceTxYellowBytes_Object = MibTableColumn
me1200EvcStatusEceInterfaceTxYellowBytes = _Me1200EvcStatusEceInterfaceTxYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 6, 1, 103),
    _Me1200EvcStatusEceInterfaceTxYellowBytes_Type()
)
me1200EvcStatusEceInterfaceTxYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceTxYellowBytes.setStatus("current")
_Me1200EvcStatusEceInterfaceTxDiscardFrames_Type = Counter64
_Me1200EvcStatusEceInterfaceTxDiscardFrames_Object = MibTableColumn
me1200EvcStatusEceInterfaceTxDiscardFrames = _Me1200EvcStatusEceInterfaceTxDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 6, 1, 104),
    _Me1200EvcStatusEceInterfaceTxDiscardFrames_Type()
)
me1200EvcStatusEceInterfaceTxDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceTxDiscardFrames.setStatus("current")
_Me1200EvcStatusEceInterfaceTxDiscardBytes_Type = Counter64
_Me1200EvcStatusEceInterfaceTxDiscardBytes_Object = MibTableColumn
me1200EvcStatusEceInterfaceTxDiscardBytes = _Me1200EvcStatusEceInterfaceTxDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 3, 6, 1, 105),
    _Me1200EvcStatusEceInterfaceTxDiscardBytes_Type()
)
me1200EvcStatusEceInterfaceTxDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceTxDiscardBytes.setStatus("current")
_Me1200EvcControl_ObjectIdentity = ObjectIdentity
me1200EvcControl = _Me1200EvcControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 4)
)
_Me1200EvcControlEvcInterfaceTable_Object = MibTable
me1200EvcControlEvcInterfaceTable = _Me1200EvcControlEvcInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 4, 5)
)
if mibBuilder.loadTexts:
    me1200EvcControlEvcInterfaceTable.setStatus("current")
_Me1200EvcControlEvcInterfaceEntry_Object = MibTableRow
me1200EvcControlEvcInterfaceEntry = _Me1200EvcControlEvcInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 4, 5, 1)
)
me1200EvcControlEvcInterfaceEntry.setIndexNames(
    (0, "ME1200-EVC-MIB", "me1200EvcControlEvcInterfaceEvcId"),
    (0, "ME1200-EVC-MIB", "me1200EvcControlEvcInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    me1200EvcControlEvcInterfaceEntry.setStatus("current")


class _Me1200EvcControlEvcInterfaceEvcId_Type(Integer32):
    """Custom type me1200EvcControlEvcInterfaceEvcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Me1200EvcControlEvcInterfaceEvcId_Type.__name__ = "Integer32"
_Me1200EvcControlEvcInterfaceEvcId_Object = MibTableColumn
me1200EvcControlEvcInterfaceEvcId = _Me1200EvcControlEvcInterfaceEvcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 4, 5, 1, 1),
    _Me1200EvcControlEvcInterfaceEvcId_Type()
)
me1200EvcControlEvcInterfaceEvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcControlEvcInterfaceEvcId.setStatus("current")
_Me1200EvcControlEvcInterfaceIfIndex_Type = ME1200InterfaceIndex
_Me1200EvcControlEvcInterfaceIfIndex_Object = MibTableColumn
me1200EvcControlEvcInterfaceIfIndex = _Me1200EvcControlEvcInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 4, 5, 1, 2),
    _Me1200EvcControlEvcInterfaceIfIndex_Type()
)
me1200EvcControlEvcInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcControlEvcInterfaceIfIndex.setStatus("current")
_Me1200EvcControlEvcInterfaceClearStatistics_Type = TruthValue
_Me1200EvcControlEvcInterfaceClearStatistics_Object = MibTableColumn
me1200EvcControlEvcInterfaceClearStatistics = _Me1200EvcControlEvcInterfaceClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 4, 5, 1, 3),
    _Me1200EvcControlEvcInterfaceClearStatistics_Type()
)
me1200EvcControlEvcInterfaceClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcControlEvcInterfaceClearStatistics.setStatus("current")
_Me1200EvcControlEceInterfaceTable_Object = MibTable
me1200EvcControlEceInterfaceTable = _Me1200EvcControlEceInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 4, 6)
)
if mibBuilder.loadTexts:
    me1200EvcControlEceInterfaceTable.setStatus("current")
_Me1200EvcControlEceInterfaceEntry_Object = MibTableRow
me1200EvcControlEceInterfaceEntry = _Me1200EvcControlEceInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 4, 6, 1)
)
me1200EvcControlEceInterfaceEntry.setIndexNames(
    (0, "ME1200-EVC-MIB", "me1200EvcControlEceInterfaceIndex"),
    (0, "ME1200-EVC-MIB", "me1200EvcControlEceInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    me1200EvcControlEceInterfaceEntry.setStatus("current")


class _Me1200EvcControlEceInterfaceIndex_Type(Integer32):
    """Custom type me1200EvcControlEceInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Me1200EvcControlEceInterfaceIndex_Type.__name__ = "Integer32"
_Me1200EvcControlEceInterfaceIndex_Object = MibTableColumn
me1200EvcControlEceInterfaceIndex = _Me1200EvcControlEceInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 4, 6, 1, 1),
    _Me1200EvcControlEceInterfaceIndex_Type()
)
me1200EvcControlEceInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcControlEceInterfaceIndex.setStatus("current")
_Me1200EvcControlEceInterfaceIfIndex_Type = ME1200InterfaceIndex
_Me1200EvcControlEceInterfaceIfIndex_Object = MibTableColumn
me1200EvcControlEceInterfaceIfIndex = _Me1200EvcControlEceInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 4, 6, 1, 2),
    _Me1200EvcControlEceInterfaceIfIndex_Type()
)
me1200EvcControlEceInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200EvcControlEceInterfaceIfIndex.setStatus("current")
_Me1200EvcControlEceInterfaceClearStatistics_Type = TruthValue
_Me1200EvcControlEceInterfaceClearStatistics_Object = MibTableColumn
me1200EvcControlEceInterfaceClearStatistics = _Me1200EvcControlEceInterfaceClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 1, 4, 6, 1, 3),
    _Me1200EvcControlEceInterfaceClearStatistics_Type()
)
me1200EvcControlEceInterfaceClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200EvcControlEceInterfaceClearStatistics.setStatus("current")
_Me1200EvcMibConformance_ObjectIdentity = ObjectIdentity
me1200EvcMibConformance = _Me1200EvcMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2)
)
_Me1200EvcMibCompliances_ObjectIdentity = ObjectIdentity
me1200EvcMibCompliances = _Me1200EvcMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 1)
)
_Me1200EvcMibGroups_ObjectIdentity = ObjectIdentity
me1200EvcMibGroups = _Me1200EvcMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 2)
)

# Managed Objects groups

me1200EvcCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 2, 1)
)
me1200EvcCapabilitiesInfoGroup.setObjects(
      *(("ME1200-EVC-MIB", "me1200EvcCapabilitiesPolicerMax"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesEvcMax"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesEceMax"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasPortDeiColoring"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasPortInnerTag"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasPortAddrMode"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasPortKey"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasPolicerColorBlind"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEvcPolicer"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEvcUniVid"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEvcItAdd"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEvcETree"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEvcName"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceAdvLookup"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceDestMacType"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceDestMac"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceSrcMac"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceInnerTag"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceEtype"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceLlc"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceSnap"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceL2cp"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceIpv4Fragment"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceIpProto"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceSrcIp"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceDestIp"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceSrcPort"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceDestPort"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceRuleType"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceTxLookup"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceOtAddVid"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEcePcpMode"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEcePcpDeiPreserve"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceDeiMode"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceItAdd"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEcePolicer"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceCos"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEceDp"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEvcPortHqos"),
        ("ME1200-EVC-MIB", "me1200EvcCapabilitiesHasEvcPortCounters"))
)
if mibBuilder.loadTexts:
    me1200EvcCapabilitiesInfoGroup.setStatus("current")

me1200EvcConfigInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 2, 2)
)
me1200EvcConfigInterfaceTableInfoGroup.setObjects(
      *(("ME1200-EVC-MIB", "me1200EvcConfigInterfaceKey"),
        ("ME1200-EVC-MIB", "me1200EvcConfigInterfaceKeyAdv"),
        ("ME1200-EVC-MIB", "me1200EvcConfigInterfaceAddrMode"),
        ("ME1200-EVC-MIB", "me1200EvcConfigInterfaceAddrModeAdv"),
        ("ME1200-EVC-MIB", "me1200EvcConfigInterfaceDeiColoring"),
        ("ME1200-EVC-MIB", "me1200EvcConfigInterfaceInnerTag"))
)
if mibBuilder.loadTexts:
    me1200EvcConfigInterfaceTableInfoGroup.setStatus("current")

me1200EvcConfigInterfaceL2cpTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 2, 3)
)
me1200EvcConfigInterfaceL2cpTableInfoGroup.setObjects(
    ("ME1200-EVC-MIB", "me1200EvcConfigInterfaceL2cpL2cpMode")
)
if mibBuilder.loadTexts:
    me1200EvcConfigInterfaceL2cpTableInfoGroup.setStatus("current")

me1200EvcConfigPolicerTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 2, 4)
)
me1200EvcConfigPolicerTableInfoGroup.setObjects(
      *(("ME1200-EVC-MIB", "me1200EvcConfigPolicerEnable"),
        ("ME1200-EVC-MIB", "me1200EvcConfigPolicerPolicerType"),
        ("ME1200-EVC-MIB", "me1200EvcConfigPolicerPolicerMode"),
        ("ME1200-EVC-MIB", "me1200EvcConfigPolicerLineRate"),
        ("ME1200-EVC-MIB", "me1200EvcConfigPolicerCir"),
        ("ME1200-EVC-MIB", "me1200EvcConfigPolicerCbs"),
        ("ME1200-EVC-MIB", "me1200EvcConfigPolicerEir"),
        ("ME1200-EVC-MIB", "me1200EvcConfigPolicerEbs"))
)
if mibBuilder.loadTexts:
    me1200EvcConfigPolicerTableInfoGroup.setStatus("current")

me1200EvcConfigEvcTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 2, 5)
)
me1200EvcConfigEvcTableInfoGroup.setObjects(
      *(("ME1200-EVC-MIB", "me1200EvcConfigEvcVid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcIvid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcNniPortList"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcLearning"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcPolicerOp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcPolicerId"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcUniVid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcItAddType"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcItInnerVid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcItAddVid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcItAddPcpDeiPreserve"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcItAddPcp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcItAddDei"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcLeafVid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcLeafIvid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcLeafPortList"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcName"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcAction"))
)
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableInfoGroup.setStatus("current")

me1200EvcConfigEvcTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 2, 6)
)
me1200EvcConfigEvcTableRowEditorInfoGroup.setObjects(
      *(("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorEvcId"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorVid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorIvid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorNniPortList"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorLearning"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorPolicerOp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorPolicerId"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorUniVid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorItAddType"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorItInnerVid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorItAddVid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorItAddPcpDeiPreserve"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorItAddPcp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorItAddDei"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorLeafVid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorLeafIvid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorLeafPortList"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorName"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200EvcConfigEvcTableRowEditorInfoGroup.setStatus("current")

me1200EvcConfigEceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 2, 7)
)
me1200EvcConfigEceTableInfoGroup.setObjects(
      *(("ME1200-EVC-MIB", "me1200EvcConfigEceNextId"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceAdvLookup"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceUniPortList"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceSrcMac"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceSrcMacMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceDestMacType"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceDestMac"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceDestMacMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceOtMatchType"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceOtMatchVid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceOtMatchPcp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceOtMatchDei"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceItMatchType"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceItMatchVid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceItMatchPcp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceItMatchDei"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceFrameType"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceEtype"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceEtypeMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceEtypeData"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceEtypeDataMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceLlcDsap"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceLlcDsapMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceLlcSsap"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceLlcSsapMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceLlcControl"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceLlcControlMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceLlcPid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceLlcPidMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceSnapOui"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceSnapOuiMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceSnapPid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceSnapPidMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceL2cpType"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv4Dscp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv4Proto"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv4ProtoMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv4Fragment"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv4SrcIp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv4SrcIpMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv4DestIp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv4DestIpMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv4SrcPort"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv4DestPort"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv6Dscp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv6Proto"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv6ProtoMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv6SrcIp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv6SrcIpMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv6DestIp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv6DestIpMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv6SrcPort"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceIpv6DestPort"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceDirection"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceRuleType"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTxLookup"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEcePopTag"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceOtAddEnable"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceOtAddVid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceOtAddPcpMode"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceOtAddPcpDeiPreserve"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceOtAddPcp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceOtAddDeiMode"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceOtAddDei"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceItAddType"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceItAddVid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceItAddPcpMode"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceItAddPcpDeiPreserve"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceItAddPcp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceItAddDeiMode"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceItAddDei"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceEvcId"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEcePolicerOp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEcePolicerId"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEcePolicyNo"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceCosEnable"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceCos"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceDpEnable"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceDp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceL2cpMode"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceL2cpDmac"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceAction"))
)
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableInfoGroup.setStatus("current")

me1200EvcConfigEceTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 2, 8)
)
me1200EvcConfigEceTableRowEditorInfoGroup.setObjects(
      *(("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorEceId"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorNextId"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorAdvLookup"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorUniPortList"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorSrcMac"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorSrcMacMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorDestMacType"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorDestMac"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorDestMacMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorOtMatchType"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorOtMatchVid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorOtMatchPcp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorOtMatchDei"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorItMatchType"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorItMatchVid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorItMatchPcp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorItMatchDei"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorFrameType"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorEtype"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorEtypeMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorEtypeData"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorEtypeDataMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorLlcDsap"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorLlcDsapMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorLlcSsap"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorLlcSsapMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorLlcControl"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorLlcControlMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorLlcPid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorLlcPidMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorSnapOui"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorSnapOuiMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorSnapPid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorSnapPidMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorL2cpType"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv4Dscp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv4Proto"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv4ProtoMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv4Fragment"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv4SrcIp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv4SrcIpMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv4DestIp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv4DestIpMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv4SrcPort"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv4DestPort"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv6Dscp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv6Proto"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv6ProtoMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv6SrcIp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv6SrcIpMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv6DestIp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv6DestIpMask"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv6SrcPort"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorIpv6DestPort"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorDirection"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorRuleType"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorTxLookup"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorPopTag"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorOtAddEnable"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorOtAddVid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorOtAddPcpMode"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorOtAddPcpDeiPreserve"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorOtAddPcp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorOtAddDeiMode"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorOtAddDei"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorItAddType"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorItAddVid"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorItAddPcpMode"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorItAddPcpDeiPreserve"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorItAddPcp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorItAddDeiMode"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorItAddDei"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorEvcId"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorPolicerOp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorPolicerId"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorPolicyNo"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorCosEnable"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorCos"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorDpEnable"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorDp"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorL2cpMode"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorL2cpDmac"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200EvcConfigEceTableRowEditorInfoGroup.setStatus("current")

me1200EvcConfigEcePrecedenceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 2, 9)
)
me1200EvcConfigEcePrecedenceTableInfoGroup.setObjects(
    ("ME1200-EVC-MIB", "me1200EvcConfigEcePrecedenceEceId")
)
if mibBuilder.loadTexts:
    me1200EvcConfigEcePrecedenceTableInfoGroup.setStatus("current")

me1200EvcConfigEvcInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 2, 10)
)
me1200EvcConfigEvcInterfaceTableInfoGroup.setObjects(
    ("ME1200-EVC-MIB", "me1200EvcConfigEvcInterfaceHqosId")
)
if mibBuilder.loadTexts:
    me1200EvcConfigEvcInterfaceTableInfoGroup.setStatus("current")

me1200EvcStatusEvcTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 2, 11)
)
me1200EvcStatusEvcTableInfoGroup.setObjects(
    ("ME1200-EVC-MIB", "me1200EvcStatusEvcConflict")
)
if mibBuilder.loadTexts:
    me1200EvcStatusEvcTableInfoGroup.setStatus("current")

me1200EvcStatusEceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 2, 12)
)
me1200EvcStatusEceTableInfoGroup.setObjects(
    ("ME1200-EVC-MIB", "me1200EvcStatusEceConflict")
)
if mibBuilder.loadTexts:
    me1200EvcStatusEceTableInfoGroup.setStatus("current")

me1200EvcStatusEvcInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 2, 13)
)
me1200EvcStatusEvcInterfaceTableInfoGroup.setObjects(
      *(("ME1200-EVC-MIB", "me1200EvcStatusEvcInterfaceRxGreenFrames"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEvcInterfaceRxGreenBytes"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEvcInterfaceRxYellowFrames"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEvcInterfaceRxYellowBytes"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEvcInterfaceRxRedFrames"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEvcInterfaceRxRedBytes"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEvcInterfaceRxDiscardFrames"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEvcInterfaceRxDiscardBytes"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEvcInterfaceTxGreenFrames"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEvcInterfaceTxGreenBytes"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEvcInterfaceTxYellowFrames"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEvcInterfaceTxYellowBytes"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEvcInterfaceTxDiscardFrames"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEvcInterfaceTxDiscardBytes"))
)
if mibBuilder.loadTexts:
    me1200EvcStatusEvcInterfaceTableInfoGroup.setStatus("current")

me1200EvcStatusEceInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 2, 14)
)
me1200EvcStatusEceInterfaceTableInfoGroup.setObjects(
      *(("ME1200-EVC-MIB", "me1200EvcStatusEceInterfaceRxGreenFrames"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEceInterfaceRxGreenBytes"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEceInterfaceRxYellowFrames"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEceInterfaceRxYellowBytes"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEceInterfaceRxRedFrames"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEceInterfaceRxRedBytes"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEceInterfaceRxDiscardFrames"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEceInterfaceRxDiscardBytes"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEceInterfaceTxGreenFrames"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEceInterfaceTxGreenBytes"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEceInterfaceTxYellowFrames"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEceInterfaceTxYellowBytes"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEceInterfaceTxDiscardFrames"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEceInterfaceTxDiscardBytes"))
)
if mibBuilder.loadTexts:
    me1200EvcStatusEceInterfaceTableInfoGroup.setStatus("current")

me1200EvcControlEvcInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 2, 15)
)
me1200EvcControlEvcInterfaceTableInfoGroup.setObjects(
    ("ME1200-EVC-MIB", "me1200EvcControlEvcInterfaceClearStatistics")
)
if mibBuilder.loadTexts:
    me1200EvcControlEvcInterfaceTableInfoGroup.setStatus("current")

me1200EvcControlEceInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 2, 16)
)
me1200EvcControlEceInterfaceTableInfoGroup.setObjects(
    ("ME1200-EVC-MIB", "me1200EvcControlEceInterfaceClearStatistics")
)
if mibBuilder.loadTexts:
    me1200EvcControlEceInterfaceTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200EvcMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 62, 2, 1, 1)
)
me1200EvcMibCompliance.setObjects(
      *(("ME1200-EVC-MIB", "me1200EvcCapabilitiesInfoGroup"),
        ("ME1200-EVC-MIB", "me1200EvcConfigInterfaceTableInfoGroup"),
        ("ME1200-EVC-MIB", "me1200EvcConfigInterfaceL2cpTableInfoGroup"),
        ("ME1200-EVC-MIB", "me1200EvcConfigPolicerTableInfoGroup"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableInfoGroup"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcTableRowEditorInfoGroup"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableInfoGroup"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEceTableRowEditorInfoGroup"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEcePrecedenceTableInfoGroup"),
        ("ME1200-EVC-MIB", "me1200EvcConfigEvcInterfaceTableInfoGroup"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEvcTableInfoGroup"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEceTableInfoGroup"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEvcInterfaceTableInfoGroup"),
        ("ME1200-EVC-MIB", "me1200EvcStatusEceInterfaceTableInfoGroup"),
        ("ME1200-EVC-MIB", "me1200EvcControlEvcInterfaceTableInfoGroup"),
        ("ME1200-EVC-MIB", "me1200EvcControlEceInterfaceTableInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200EvcMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-EVC-MIB",
    **{"ME1200BitType": ME1200BitType,
       "ME1200DestMacType": ME1200DestMacType,
       "ME1200VcapKeyType": ME1200VcapKeyType,
       "ME1200VlanTagPriority": ME1200VlanTagPriority,
       "ME1200VlanTagType": ME1200VlanTagType,
       "ME1200evcDeiMode": ME1200evcDeiMode,
       "ME1200evcDirection": ME1200evcDirection,
       "ME1200evcEceL2cpMode": ME1200evcEceL2cpMode,
       "ME1200evcFrameType": ME1200evcFrameType,
       "ME1200evcInnerTagType": ME1200evcInnerTagType,
       "ME1200evcL2cpDmac": ME1200evcL2cpDmac,
       "ME1200evcL2cpMode": ME1200evcL2cpMode,
       "ME1200evcL2cpType": ME1200evcL2cpType,
       "ME1200evcPcpMode": ME1200evcPcpMode,
       "ME1200evcPolicerMode": ME1200evcPolicerMode,
       "ME1200evcPolicerOp": ME1200evcPolicerOp,
       "ME1200evcPolicerType": ME1200evcPolicerType,
       "ME1200evcPopTag": ME1200evcPopTag,
       "ME1200evcRuleType": ME1200evcRuleType,
       "ME1200evcTxLookup": ME1200evcTxLookup,
       "me1200EvcMib": me1200EvcMib,
       "me1200EvcMibObjects": me1200EvcMibObjects,
       "me1200EvcCapabilities": me1200EvcCapabilities,
       "me1200EvcCapabilitiesPolicerMax": me1200EvcCapabilitiesPolicerMax,
       "me1200EvcCapabilitiesEvcMax": me1200EvcCapabilitiesEvcMax,
       "me1200EvcCapabilitiesEceMax": me1200EvcCapabilitiesEceMax,
       "me1200EvcCapabilitiesHasPortDeiColoring": me1200EvcCapabilitiesHasPortDeiColoring,
       "me1200EvcCapabilitiesHasPortInnerTag": me1200EvcCapabilitiesHasPortInnerTag,
       "me1200EvcCapabilitiesHasPortAddrMode": me1200EvcCapabilitiesHasPortAddrMode,
       "me1200EvcCapabilitiesHasPortKey": me1200EvcCapabilitiesHasPortKey,
       "me1200EvcCapabilitiesHasPolicerColorBlind": me1200EvcCapabilitiesHasPolicerColorBlind,
       "me1200EvcCapabilitiesHasEvcPolicer": me1200EvcCapabilitiesHasEvcPolicer,
       "me1200EvcCapabilitiesHasEvcUniVid": me1200EvcCapabilitiesHasEvcUniVid,
       "me1200EvcCapabilitiesHasEvcItAdd": me1200EvcCapabilitiesHasEvcItAdd,
       "me1200EvcCapabilitiesHasEvcETree": me1200EvcCapabilitiesHasEvcETree,
       "me1200EvcCapabilitiesHasEvcName": me1200EvcCapabilitiesHasEvcName,
       "me1200EvcCapabilitiesHasEceAdvLookup": me1200EvcCapabilitiesHasEceAdvLookup,
       "me1200EvcCapabilitiesHasEceDestMacType": me1200EvcCapabilitiesHasEceDestMacType,
       "me1200EvcCapabilitiesHasEceDestMac": me1200EvcCapabilitiesHasEceDestMac,
       "me1200EvcCapabilitiesHasEceSrcMac": me1200EvcCapabilitiesHasEceSrcMac,
       "me1200EvcCapabilitiesHasEceInnerTag": me1200EvcCapabilitiesHasEceInnerTag,
       "me1200EvcCapabilitiesHasEceEtype": me1200EvcCapabilitiesHasEceEtype,
       "me1200EvcCapabilitiesHasEceLlc": me1200EvcCapabilitiesHasEceLlc,
       "me1200EvcCapabilitiesHasEceSnap": me1200EvcCapabilitiesHasEceSnap,
       "me1200EvcCapabilitiesHasEceL2cp": me1200EvcCapabilitiesHasEceL2cp,
       "me1200EvcCapabilitiesHasEceIpv4Fragment": me1200EvcCapabilitiesHasEceIpv4Fragment,
       "me1200EvcCapabilitiesHasEceIpProto": me1200EvcCapabilitiesHasEceIpProto,
       "me1200EvcCapabilitiesHasEceSrcIp": me1200EvcCapabilitiesHasEceSrcIp,
       "me1200EvcCapabilitiesHasEceDestIp": me1200EvcCapabilitiesHasEceDestIp,
       "me1200EvcCapabilitiesHasEceSrcPort": me1200EvcCapabilitiesHasEceSrcPort,
       "me1200EvcCapabilitiesHasEceDestPort": me1200EvcCapabilitiesHasEceDestPort,
       "me1200EvcCapabilitiesHasEceRuleType": me1200EvcCapabilitiesHasEceRuleType,
       "me1200EvcCapabilitiesHasEceTxLookup": me1200EvcCapabilitiesHasEceTxLookup,
       "me1200EvcCapabilitiesHasEceOtAddVid": me1200EvcCapabilitiesHasEceOtAddVid,
       "me1200EvcCapabilitiesHasEcePcpMode": me1200EvcCapabilitiesHasEcePcpMode,
       "me1200EvcCapabilitiesHasEcePcpDeiPreserve": me1200EvcCapabilitiesHasEcePcpDeiPreserve,
       "me1200EvcCapabilitiesHasEceDeiMode": me1200EvcCapabilitiesHasEceDeiMode,
       "me1200EvcCapabilitiesHasEceItAdd": me1200EvcCapabilitiesHasEceItAdd,
       "me1200EvcCapabilitiesHasEcePolicer": me1200EvcCapabilitiesHasEcePolicer,
       "me1200EvcCapabilitiesHasEceCos": me1200EvcCapabilitiesHasEceCos,
       "me1200EvcCapabilitiesHasEceDp": me1200EvcCapabilitiesHasEceDp,
       "me1200EvcCapabilitiesHasEvcPortHqos": me1200EvcCapabilitiesHasEvcPortHqos,
       "me1200EvcCapabilitiesHasEvcPortCounters": me1200EvcCapabilitiesHasEvcPortCounters,
       "me1200EvcConfig": me1200EvcConfig,
       "me1200EvcConfigInterface": me1200EvcConfigInterface,
       "me1200EvcConfigInterfaceTable": me1200EvcConfigInterfaceTable,
       "me1200EvcConfigInterfaceEntry": me1200EvcConfigInterfaceEntry,
       "me1200EvcConfigInterfaceIfIndex": me1200EvcConfigInterfaceIfIndex,
       "me1200EvcConfigInterfaceKey": me1200EvcConfigInterfaceKey,
       "me1200EvcConfigInterfaceKeyAdv": me1200EvcConfigInterfaceKeyAdv,
       "me1200EvcConfigInterfaceAddrMode": me1200EvcConfigInterfaceAddrMode,
       "me1200EvcConfigInterfaceAddrModeAdv": me1200EvcConfigInterfaceAddrModeAdv,
       "me1200EvcConfigInterfaceDeiColoring": me1200EvcConfigInterfaceDeiColoring,
       "me1200EvcConfigInterfaceInnerTag": me1200EvcConfigInterfaceInnerTag,
       "me1200EvcConfigInterfaceL2cpTable": me1200EvcConfigInterfaceL2cpTable,
       "me1200EvcConfigInterfaceL2cpEntry": me1200EvcConfigInterfaceL2cpEntry,
       "me1200EvcConfigInterfaceL2cpIfIndex": me1200EvcConfigInterfaceL2cpIfIndex,
       "me1200EvcConfigInterfaceL2cpL2cpId": me1200EvcConfigInterfaceL2cpL2cpId,
       "me1200EvcConfigInterfaceL2cpL2cpMode": me1200EvcConfigInterfaceL2cpL2cpMode,
       "me1200EvcConfigPolicerTable": me1200EvcConfigPolicerTable,
       "me1200EvcConfigPolicerEntry": me1200EvcConfigPolicerEntry,
       "me1200EvcConfigPolicerPolicerId": me1200EvcConfigPolicerPolicerId,
       "me1200EvcConfigPolicerEnable": me1200EvcConfigPolicerEnable,
       "me1200EvcConfigPolicerPolicerType": me1200EvcConfigPolicerPolicerType,
       "me1200EvcConfigPolicerPolicerMode": me1200EvcConfigPolicerPolicerMode,
       "me1200EvcConfigPolicerLineRate": me1200EvcConfigPolicerLineRate,
       "me1200EvcConfigPolicerCir": me1200EvcConfigPolicerCir,
       "me1200EvcConfigPolicerCbs": me1200EvcConfigPolicerCbs,
       "me1200EvcConfigPolicerEir": me1200EvcConfigPolicerEir,
       "me1200EvcConfigPolicerEbs": me1200EvcConfigPolicerEbs,
       "me1200EvcConfigEvc": me1200EvcConfigEvc,
       "me1200EvcConfigEvcTable": me1200EvcConfigEvcTable,
       "me1200EvcConfigEvcEntry": me1200EvcConfigEvcEntry,
       "me1200EvcConfigEvcEvcId": me1200EvcConfigEvcEvcId,
       "me1200EvcConfigEvcVid": me1200EvcConfigEvcVid,
       "me1200EvcConfigEvcIvid": me1200EvcConfigEvcIvid,
       "me1200EvcConfigEvcNniPortList": me1200EvcConfigEvcNniPortList,
       "me1200EvcConfigEvcLearning": me1200EvcConfigEvcLearning,
       "me1200EvcConfigEvcPolicerOp": me1200EvcConfigEvcPolicerOp,
       "me1200EvcConfigEvcPolicerId": me1200EvcConfigEvcPolicerId,
       "me1200EvcConfigEvcUniVid": me1200EvcConfigEvcUniVid,
       "me1200EvcConfigEvcItAddType": me1200EvcConfigEvcItAddType,
       "me1200EvcConfigEvcItInnerVid": me1200EvcConfigEvcItInnerVid,
       "me1200EvcConfigEvcItAddVid": me1200EvcConfigEvcItAddVid,
       "me1200EvcConfigEvcItAddPcpDeiPreserve": me1200EvcConfigEvcItAddPcpDeiPreserve,
       "me1200EvcConfigEvcItAddPcp": me1200EvcConfigEvcItAddPcp,
       "me1200EvcConfigEvcItAddDei": me1200EvcConfigEvcItAddDei,
       "me1200EvcConfigEvcLeafVid": me1200EvcConfigEvcLeafVid,
       "me1200EvcConfigEvcLeafIvid": me1200EvcConfigEvcLeafIvid,
       "me1200EvcConfigEvcLeafPortList": me1200EvcConfigEvcLeafPortList,
       "me1200EvcConfigEvcName": me1200EvcConfigEvcName,
       "me1200EvcConfigEvcAction": me1200EvcConfigEvcAction,
       "me1200EvcConfigEvcTableRowEditor": me1200EvcConfigEvcTableRowEditor,
       "me1200EvcConfigEvcTableRowEditorEvcId": me1200EvcConfigEvcTableRowEditorEvcId,
       "me1200EvcConfigEvcTableRowEditorVid": me1200EvcConfigEvcTableRowEditorVid,
       "me1200EvcConfigEvcTableRowEditorIvid": me1200EvcConfigEvcTableRowEditorIvid,
       "me1200EvcConfigEvcTableRowEditorNniPortList": me1200EvcConfigEvcTableRowEditorNniPortList,
       "me1200EvcConfigEvcTableRowEditorLearning": me1200EvcConfigEvcTableRowEditorLearning,
       "me1200EvcConfigEvcTableRowEditorPolicerOp": me1200EvcConfigEvcTableRowEditorPolicerOp,
       "me1200EvcConfigEvcTableRowEditorPolicerId": me1200EvcConfigEvcTableRowEditorPolicerId,
       "me1200EvcConfigEvcTableRowEditorUniVid": me1200EvcConfigEvcTableRowEditorUniVid,
       "me1200EvcConfigEvcTableRowEditorItAddType": me1200EvcConfigEvcTableRowEditorItAddType,
       "me1200EvcConfigEvcTableRowEditorItInnerVid": me1200EvcConfigEvcTableRowEditorItInnerVid,
       "me1200EvcConfigEvcTableRowEditorItAddVid": me1200EvcConfigEvcTableRowEditorItAddVid,
       "me1200EvcConfigEvcTableRowEditorItAddPcpDeiPreserve": me1200EvcConfigEvcTableRowEditorItAddPcpDeiPreserve,
       "me1200EvcConfigEvcTableRowEditorItAddPcp": me1200EvcConfigEvcTableRowEditorItAddPcp,
       "me1200EvcConfigEvcTableRowEditorItAddDei": me1200EvcConfigEvcTableRowEditorItAddDei,
       "me1200EvcConfigEvcTableRowEditorLeafVid": me1200EvcConfigEvcTableRowEditorLeafVid,
       "me1200EvcConfigEvcTableRowEditorLeafIvid": me1200EvcConfigEvcTableRowEditorLeafIvid,
       "me1200EvcConfigEvcTableRowEditorLeafPortList": me1200EvcConfigEvcTableRowEditorLeafPortList,
       "me1200EvcConfigEvcTableRowEditorName": me1200EvcConfigEvcTableRowEditorName,
       "me1200EvcConfigEvcTableRowEditorAction": me1200EvcConfigEvcTableRowEditorAction,
       "me1200EvcConfigEce": me1200EvcConfigEce,
       "me1200EvcConfigEceTable": me1200EvcConfigEceTable,
       "me1200EvcConfigEceEntry": me1200EvcConfigEceEntry,
       "me1200EvcConfigEceEceId": me1200EvcConfigEceEceId,
       "me1200EvcConfigEceNextId": me1200EvcConfigEceNextId,
       "me1200EvcConfigEceAdvLookup": me1200EvcConfigEceAdvLookup,
       "me1200EvcConfigEceUniPortList": me1200EvcConfigEceUniPortList,
       "me1200EvcConfigEceSrcMac": me1200EvcConfigEceSrcMac,
       "me1200EvcConfigEceSrcMacMask": me1200EvcConfigEceSrcMacMask,
       "me1200EvcConfigEceDestMacType": me1200EvcConfigEceDestMacType,
       "me1200EvcConfigEceDestMac": me1200EvcConfigEceDestMac,
       "me1200EvcConfigEceDestMacMask": me1200EvcConfigEceDestMacMask,
       "me1200EvcConfigEceOtMatchType": me1200EvcConfigEceOtMatchType,
       "me1200EvcConfigEceOtMatchVid": me1200EvcConfigEceOtMatchVid,
       "me1200EvcConfigEceOtMatchPcp": me1200EvcConfigEceOtMatchPcp,
       "me1200EvcConfigEceOtMatchDei": me1200EvcConfigEceOtMatchDei,
       "me1200EvcConfigEceItMatchType": me1200EvcConfigEceItMatchType,
       "me1200EvcConfigEceItMatchVid": me1200EvcConfigEceItMatchVid,
       "me1200EvcConfigEceItMatchPcp": me1200EvcConfigEceItMatchPcp,
       "me1200EvcConfigEceItMatchDei": me1200EvcConfigEceItMatchDei,
       "me1200EvcConfigEceFrameType": me1200EvcConfigEceFrameType,
       "me1200EvcConfigEceEtype": me1200EvcConfigEceEtype,
       "me1200EvcConfigEceEtypeMask": me1200EvcConfigEceEtypeMask,
       "me1200EvcConfigEceEtypeData": me1200EvcConfigEceEtypeData,
       "me1200EvcConfigEceEtypeDataMask": me1200EvcConfigEceEtypeDataMask,
       "me1200EvcConfigEceLlcDsap": me1200EvcConfigEceLlcDsap,
       "me1200EvcConfigEceLlcDsapMask": me1200EvcConfigEceLlcDsapMask,
       "me1200EvcConfigEceLlcSsap": me1200EvcConfigEceLlcSsap,
       "me1200EvcConfigEceLlcSsapMask": me1200EvcConfigEceLlcSsapMask,
       "me1200EvcConfigEceLlcControl": me1200EvcConfigEceLlcControl,
       "me1200EvcConfigEceLlcControlMask": me1200EvcConfigEceLlcControlMask,
       "me1200EvcConfigEceLlcPid": me1200EvcConfigEceLlcPid,
       "me1200EvcConfigEceLlcPidMask": me1200EvcConfigEceLlcPidMask,
       "me1200EvcConfigEceSnapOui": me1200EvcConfigEceSnapOui,
       "me1200EvcConfigEceSnapOuiMask": me1200EvcConfigEceSnapOuiMask,
       "me1200EvcConfigEceSnapPid": me1200EvcConfigEceSnapPid,
       "me1200EvcConfigEceSnapPidMask": me1200EvcConfigEceSnapPidMask,
       "me1200EvcConfigEceL2cpType": me1200EvcConfigEceL2cpType,
       "me1200EvcConfigEceIpv4Dscp": me1200EvcConfigEceIpv4Dscp,
       "me1200EvcConfigEceIpv4Proto": me1200EvcConfigEceIpv4Proto,
       "me1200EvcConfigEceIpv4ProtoMask": me1200EvcConfigEceIpv4ProtoMask,
       "me1200EvcConfigEceIpv4Fragment": me1200EvcConfigEceIpv4Fragment,
       "me1200EvcConfigEceIpv4SrcIp": me1200EvcConfigEceIpv4SrcIp,
       "me1200EvcConfigEceIpv4SrcIpMask": me1200EvcConfigEceIpv4SrcIpMask,
       "me1200EvcConfigEceIpv4DestIp": me1200EvcConfigEceIpv4DestIp,
       "me1200EvcConfigEceIpv4DestIpMask": me1200EvcConfigEceIpv4DestIpMask,
       "me1200EvcConfigEceIpv4SrcPort": me1200EvcConfigEceIpv4SrcPort,
       "me1200EvcConfigEceIpv4DestPort": me1200EvcConfigEceIpv4DestPort,
       "me1200EvcConfigEceIpv6Dscp": me1200EvcConfigEceIpv6Dscp,
       "me1200EvcConfigEceIpv6Proto": me1200EvcConfigEceIpv6Proto,
       "me1200EvcConfigEceIpv6ProtoMask": me1200EvcConfigEceIpv6ProtoMask,
       "me1200EvcConfigEceIpv6SrcIp": me1200EvcConfigEceIpv6SrcIp,
       "me1200EvcConfigEceIpv6SrcIpMask": me1200EvcConfigEceIpv6SrcIpMask,
       "me1200EvcConfigEceIpv6DestIp": me1200EvcConfigEceIpv6DestIp,
       "me1200EvcConfigEceIpv6DestIpMask": me1200EvcConfigEceIpv6DestIpMask,
       "me1200EvcConfigEceIpv6SrcPort": me1200EvcConfigEceIpv6SrcPort,
       "me1200EvcConfigEceIpv6DestPort": me1200EvcConfigEceIpv6DestPort,
       "me1200EvcConfigEceDirection": me1200EvcConfigEceDirection,
       "me1200EvcConfigEceRuleType": me1200EvcConfigEceRuleType,
       "me1200EvcConfigEceTxLookup": me1200EvcConfigEceTxLookup,
       "me1200EvcConfigEcePopTag": me1200EvcConfigEcePopTag,
       "me1200EvcConfigEceOtAddEnable": me1200EvcConfigEceOtAddEnable,
       "me1200EvcConfigEceOtAddVid": me1200EvcConfigEceOtAddVid,
       "me1200EvcConfigEceOtAddPcpMode": me1200EvcConfigEceOtAddPcpMode,
       "me1200EvcConfigEceOtAddPcpDeiPreserve": me1200EvcConfigEceOtAddPcpDeiPreserve,
       "me1200EvcConfigEceOtAddPcp": me1200EvcConfigEceOtAddPcp,
       "me1200EvcConfigEceOtAddDeiMode": me1200EvcConfigEceOtAddDeiMode,
       "me1200EvcConfigEceOtAddDei": me1200EvcConfigEceOtAddDei,
       "me1200EvcConfigEceItAddType": me1200EvcConfigEceItAddType,
       "me1200EvcConfigEceItAddVid": me1200EvcConfigEceItAddVid,
       "me1200EvcConfigEceItAddPcpMode": me1200EvcConfigEceItAddPcpMode,
       "me1200EvcConfigEceItAddPcpDeiPreserve": me1200EvcConfigEceItAddPcpDeiPreserve,
       "me1200EvcConfigEceItAddPcp": me1200EvcConfigEceItAddPcp,
       "me1200EvcConfigEceItAddDeiMode": me1200EvcConfigEceItAddDeiMode,
       "me1200EvcConfigEceItAddDei": me1200EvcConfigEceItAddDei,
       "me1200EvcConfigEceEvcId": me1200EvcConfigEceEvcId,
       "me1200EvcConfigEcePolicerOp": me1200EvcConfigEcePolicerOp,
       "me1200EvcConfigEcePolicerId": me1200EvcConfigEcePolicerId,
       "me1200EvcConfigEcePolicyNo": me1200EvcConfigEcePolicyNo,
       "me1200EvcConfigEceCosEnable": me1200EvcConfigEceCosEnable,
       "me1200EvcConfigEceCos": me1200EvcConfigEceCos,
       "me1200EvcConfigEceDpEnable": me1200EvcConfigEceDpEnable,
       "me1200EvcConfigEceDp": me1200EvcConfigEceDp,
       "me1200EvcConfigEceL2cpMode": me1200EvcConfigEceL2cpMode,
       "me1200EvcConfigEceL2cpDmac": me1200EvcConfigEceL2cpDmac,
       "me1200EvcConfigEceAction": me1200EvcConfigEceAction,
       "me1200EvcConfigEceTableRowEditor": me1200EvcConfigEceTableRowEditor,
       "me1200EvcConfigEceTableRowEditorEceId": me1200EvcConfigEceTableRowEditorEceId,
       "me1200EvcConfigEceTableRowEditorNextId": me1200EvcConfigEceTableRowEditorNextId,
       "me1200EvcConfigEceTableRowEditorAdvLookup": me1200EvcConfigEceTableRowEditorAdvLookup,
       "me1200EvcConfigEceTableRowEditorUniPortList": me1200EvcConfigEceTableRowEditorUniPortList,
       "me1200EvcConfigEceTableRowEditorSrcMac": me1200EvcConfigEceTableRowEditorSrcMac,
       "me1200EvcConfigEceTableRowEditorSrcMacMask": me1200EvcConfigEceTableRowEditorSrcMacMask,
       "me1200EvcConfigEceTableRowEditorDestMacType": me1200EvcConfigEceTableRowEditorDestMacType,
       "me1200EvcConfigEceTableRowEditorDestMac": me1200EvcConfigEceTableRowEditorDestMac,
       "me1200EvcConfigEceTableRowEditorDestMacMask": me1200EvcConfigEceTableRowEditorDestMacMask,
       "me1200EvcConfigEceTableRowEditorOtMatchType": me1200EvcConfigEceTableRowEditorOtMatchType,
       "me1200EvcConfigEceTableRowEditorOtMatchVid": me1200EvcConfigEceTableRowEditorOtMatchVid,
       "me1200EvcConfigEceTableRowEditorOtMatchPcp": me1200EvcConfigEceTableRowEditorOtMatchPcp,
       "me1200EvcConfigEceTableRowEditorOtMatchDei": me1200EvcConfigEceTableRowEditorOtMatchDei,
       "me1200EvcConfigEceTableRowEditorItMatchType": me1200EvcConfigEceTableRowEditorItMatchType,
       "me1200EvcConfigEceTableRowEditorItMatchVid": me1200EvcConfigEceTableRowEditorItMatchVid,
       "me1200EvcConfigEceTableRowEditorItMatchPcp": me1200EvcConfigEceTableRowEditorItMatchPcp,
       "me1200EvcConfigEceTableRowEditorItMatchDei": me1200EvcConfigEceTableRowEditorItMatchDei,
       "me1200EvcConfigEceTableRowEditorFrameType": me1200EvcConfigEceTableRowEditorFrameType,
       "me1200EvcConfigEceTableRowEditorEtype": me1200EvcConfigEceTableRowEditorEtype,
       "me1200EvcConfigEceTableRowEditorEtypeMask": me1200EvcConfigEceTableRowEditorEtypeMask,
       "me1200EvcConfigEceTableRowEditorEtypeData": me1200EvcConfigEceTableRowEditorEtypeData,
       "me1200EvcConfigEceTableRowEditorEtypeDataMask": me1200EvcConfigEceTableRowEditorEtypeDataMask,
       "me1200EvcConfigEceTableRowEditorLlcDsap": me1200EvcConfigEceTableRowEditorLlcDsap,
       "me1200EvcConfigEceTableRowEditorLlcDsapMask": me1200EvcConfigEceTableRowEditorLlcDsapMask,
       "me1200EvcConfigEceTableRowEditorLlcSsap": me1200EvcConfigEceTableRowEditorLlcSsap,
       "me1200EvcConfigEceTableRowEditorLlcSsapMask": me1200EvcConfigEceTableRowEditorLlcSsapMask,
       "me1200EvcConfigEceTableRowEditorLlcControl": me1200EvcConfigEceTableRowEditorLlcControl,
       "me1200EvcConfigEceTableRowEditorLlcControlMask": me1200EvcConfigEceTableRowEditorLlcControlMask,
       "me1200EvcConfigEceTableRowEditorLlcPid": me1200EvcConfigEceTableRowEditorLlcPid,
       "me1200EvcConfigEceTableRowEditorLlcPidMask": me1200EvcConfigEceTableRowEditorLlcPidMask,
       "me1200EvcConfigEceTableRowEditorSnapOui": me1200EvcConfigEceTableRowEditorSnapOui,
       "me1200EvcConfigEceTableRowEditorSnapOuiMask": me1200EvcConfigEceTableRowEditorSnapOuiMask,
       "me1200EvcConfigEceTableRowEditorSnapPid": me1200EvcConfigEceTableRowEditorSnapPid,
       "me1200EvcConfigEceTableRowEditorSnapPidMask": me1200EvcConfigEceTableRowEditorSnapPidMask,
       "me1200EvcConfigEceTableRowEditorL2cpType": me1200EvcConfigEceTableRowEditorL2cpType,
       "me1200EvcConfigEceTableRowEditorIpv4Dscp": me1200EvcConfigEceTableRowEditorIpv4Dscp,
       "me1200EvcConfigEceTableRowEditorIpv4Proto": me1200EvcConfigEceTableRowEditorIpv4Proto,
       "me1200EvcConfigEceTableRowEditorIpv4ProtoMask": me1200EvcConfigEceTableRowEditorIpv4ProtoMask,
       "me1200EvcConfigEceTableRowEditorIpv4Fragment": me1200EvcConfigEceTableRowEditorIpv4Fragment,
       "me1200EvcConfigEceTableRowEditorIpv4SrcIp": me1200EvcConfigEceTableRowEditorIpv4SrcIp,
       "me1200EvcConfigEceTableRowEditorIpv4SrcIpMask": me1200EvcConfigEceTableRowEditorIpv4SrcIpMask,
       "me1200EvcConfigEceTableRowEditorIpv4DestIp": me1200EvcConfigEceTableRowEditorIpv4DestIp,
       "me1200EvcConfigEceTableRowEditorIpv4DestIpMask": me1200EvcConfigEceTableRowEditorIpv4DestIpMask,
       "me1200EvcConfigEceTableRowEditorIpv4SrcPort": me1200EvcConfigEceTableRowEditorIpv4SrcPort,
       "me1200EvcConfigEceTableRowEditorIpv4DestPort": me1200EvcConfigEceTableRowEditorIpv4DestPort,
       "me1200EvcConfigEceTableRowEditorIpv6Dscp": me1200EvcConfigEceTableRowEditorIpv6Dscp,
       "me1200EvcConfigEceTableRowEditorIpv6Proto": me1200EvcConfigEceTableRowEditorIpv6Proto,
       "me1200EvcConfigEceTableRowEditorIpv6ProtoMask": me1200EvcConfigEceTableRowEditorIpv6ProtoMask,
       "me1200EvcConfigEceTableRowEditorIpv6SrcIp": me1200EvcConfigEceTableRowEditorIpv6SrcIp,
       "me1200EvcConfigEceTableRowEditorIpv6SrcIpMask": me1200EvcConfigEceTableRowEditorIpv6SrcIpMask,
       "me1200EvcConfigEceTableRowEditorIpv6DestIp": me1200EvcConfigEceTableRowEditorIpv6DestIp,
       "me1200EvcConfigEceTableRowEditorIpv6DestIpMask": me1200EvcConfigEceTableRowEditorIpv6DestIpMask,
       "me1200EvcConfigEceTableRowEditorIpv6SrcPort": me1200EvcConfigEceTableRowEditorIpv6SrcPort,
       "me1200EvcConfigEceTableRowEditorIpv6DestPort": me1200EvcConfigEceTableRowEditorIpv6DestPort,
       "me1200EvcConfigEceTableRowEditorDirection": me1200EvcConfigEceTableRowEditorDirection,
       "me1200EvcConfigEceTableRowEditorRuleType": me1200EvcConfigEceTableRowEditorRuleType,
       "me1200EvcConfigEceTableRowEditorTxLookup": me1200EvcConfigEceTableRowEditorTxLookup,
       "me1200EvcConfigEceTableRowEditorPopTag": me1200EvcConfigEceTableRowEditorPopTag,
       "me1200EvcConfigEceTableRowEditorOtAddEnable": me1200EvcConfigEceTableRowEditorOtAddEnable,
       "me1200EvcConfigEceTableRowEditorOtAddVid": me1200EvcConfigEceTableRowEditorOtAddVid,
       "me1200EvcConfigEceTableRowEditorOtAddPcpMode": me1200EvcConfigEceTableRowEditorOtAddPcpMode,
       "me1200EvcConfigEceTableRowEditorOtAddPcpDeiPreserve": me1200EvcConfigEceTableRowEditorOtAddPcpDeiPreserve,
       "me1200EvcConfigEceTableRowEditorOtAddPcp": me1200EvcConfigEceTableRowEditorOtAddPcp,
       "me1200EvcConfigEceTableRowEditorOtAddDeiMode": me1200EvcConfigEceTableRowEditorOtAddDeiMode,
       "me1200EvcConfigEceTableRowEditorOtAddDei": me1200EvcConfigEceTableRowEditorOtAddDei,
       "me1200EvcConfigEceTableRowEditorItAddType": me1200EvcConfigEceTableRowEditorItAddType,
       "me1200EvcConfigEceTableRowEditorItAddVid": me1200EvcConfigEceTableRowEditorItAddVid,
       "me1200EvcConfigEceTableRowEditorItAddPcpMode": me1200EvcConfigEceTableRowEditorItAddPcpMode,
       "me1200EvcConfigEceTableRowEditorItAddPcpDeiPreserve": me1200EvcConfigEceTableRowEditorItAddPcpDeiPreserve,
       "me1200EvcConfigEceTableRowEditorItAddPcp": me1200EvcConfigEceTableRowEditorItAddPcp,
       "me1200EvcConfigEceTableRowEditorItAddDeiMode": me1200EvcConfigEceTableRowEditorItAddDeiMode,
       "me1200EvcConfigEceTableRowEditorItAddDei": me1200EvcConfigEceTableRowEditorItAddDei,
       "me1200EvcConfigEceTableRowEditorEvcId": me1200EvcConfigEceTableRowEditorEvcId,
       "me1200EvcConfigEceTableRowEditorPolicerOp": me1200EvcConfigEceTableRowEditorPolicerOp,
       "me1200EvcConfigEceTableRowEditorPolicerId": me1200EvcConfigEceTableRowEditorPolicerId,
       "me1200EvcConfigEceTableRowEditorPolicyNo": me1200EvcConfigEceTableRowEditorPolicyNo,
       "me1200EvcConfigEceTableRowEditorCosEnable": me1200EvcConfigEceTableRowEditorCosEnable,
       "me1200EvcConfigEceTableRowEditorCos": me1200EvcConfigEceTableRowEditorCos,
       "me1200EvcConfigEceTableRowEditorDpEnable": me1200EvcConfigEceTableRowEditorDpEnable,
       "me1200EvcConfigEceTableRowEditorDp": me1200EvcConfigEceTableRowEditorDp,
       "me1200EvcConfigEceTableRowEditorL2cpMode": me1200EvcConfigEceTableRowEditorL2cpMode,
       "me1200EvcConfigEceTableRowEditorL2cpDmac": me1200EvcConfigEceTableRowEditorL2cpDmac,
       "me1200EvcConfigEceTableRowEditorAction": me1200EvcConfigEceTableRowEditorAction,
       "me1200EvcConfigEcePrecedenceTable": me1200EvcConfigEcePrecedenceTable,
       "me1200EvcConfigEcePrecedenceEntry": me1200EvcConfigEcePrecedenceEntry,
       "me1200EvcConfigEcePrecedenceIndex": me1200EvcConfigEcePrecedenceIndex,
       "me1200EvcConfigEcePrecedenceEceId": me1200EvcConfigEcePrecedenceEceId,
       "me1200EvcConfigEvcInterfaceTable": me1200EvcConfigEvcInterfaceTable,
       "me1200EvcConfigEvcInterfaceEntry": me1200EvcConfigEvcInterfaceEntry,
       "me1200EvcConfigEvcInterfaceEvcId": me1200EvcConfigEvcInterfaceEvcId,
       "me1200EvcConfigEvcInterfaceIfIndex": me1200EvcConfigEvcInterfaceIfIndex,
       "me1200EvcConfigEvcInterfaceHqosId": me1200EvcConfigEvcInterfaceHqosId,
       "me1200EvcStatus": me1200EvcStatus,
       "me1200EvcStatusEvcTable": me1200EvcStatusEvcTable,
       "me1200EvcStatusEvcEntry": me1200EvcStatusEvcEntry,
       "me1200EvcStatusEvcEvcId": me1200EvcStatusEvcEvcId,
       "me1200EvcStatusEvcConflict": me1200EvcStatusEvcConflict,
       "me1200EvcStatusEceTable": me1200EvcStatusEceTable,
       "me1200EvcStatusEceEntry": me1200EvcStatusEceEntry,
       "me1200EvcStatusEceIndex": me1200EvcStatusEceIndex,
       "me1200EvcStatusEceConflict": me1200EvcStatusEceConflict,
       "me1200EvcStatusEvcInterfaceTable": me1200EvcStatusEvcInterfaceTable,
       "me1200EvcStatusEvcInterfaceEntry": me1200EvcStatusEvcInterfaceEntry,
       "me1200EvcStatusEvcInterfaceEvcId": me1200EvcStatusEvcInterfaceEvcId,
       "me1200EvcStatusEvcInterfaceIfIndex": me1200EvcStatusEvcInterfaceIfIndex,
       "me1200EvcStatusEvcInterfaceRxGreenFrames": me1200EvcStatusEvcInterfaceRxGreenFrames,
       "me1200EvcStatusEvcInterfaceRxGreenBytes": me1200EvcStatusEvcInterfaceRxGreenBytes,
       "me1200EvcStatusEvcInterfaceRxYellowFrames": me1200EvcStatusEvcInterfaceRxYellowFrames,
       "me1200EvcStatusEvcInterfaceRxYellowBytes": me1200EvcStatusEvcInterfaceRxYellowBytes,
       "me1200EvcStatusEvcInterfaceRxRedFrames": me1200EvcStatusEvcInterfaceRxRedFrames,
       "me1200EvcStatusEvcInterfaceRxRedBytes": me1200EvcStatusEvcInterfaceRxRedBytes,
       "me1200EvcStatusEvcInterfaceRxDiscardFrames": me1200EvcStatusEvcInterfaceRxDiscardFrames,
       "me1200EvcStatusEvcInterfaceRxDiscardBytes": me1200EvcStatusEvcInterfaceRxDiscardBytes,
       "me1200EvcStatusEvcInterfaceTxGreenFrames": me1200EvcStatusEvcInterfaceTxGreenFrames,
       "me1200EvcStatusEvcInterfaceTxGreenBytes": me1200EvcStatusEvcInterfaceTxGreenBytes,
       "me1200EvcStatusEvcInterfaceTxYellowFrames": me1200EvcStatusEvcInterfaceTxYellowFrames,
       "me1200EvcStatusEvcInterfaceTxYellowBytes": me1200EvcStatusEvcInterfaceTxYellowBytes,
       "me1200EvcStatusEvcInterfaceTxDiscardFrames": me1200EvcStatusEvcInterfaceTxDiscardFrames,
       "me1200EvcStatusEvcInterfaceTxDiscardBytes": me1200EvcStatusEvcInterfaceTxDiscardBytes,
       "me1200EvcStatusEceInterfaceTable": me1200EvcStatusEceInterfaceTable,
       "me1200EvcStatusEceInterfaceEntry": me1200EvcStatusEceInterfaceEntry,
       "me1200EvcStatusEceInterfaceIndex": me1200EvcStatusEceInterfaceIndex,
       "me1200EvcStatusEceInterfaceIfIndex": me1200EvcStatusEceInterfaceIfIndex,
       "me1200EvcStatusEceInterfaceRxGreenFrames": me1200EvcStatusEceInterfaceRxGreenFrames,
       "me1200EvcStatusEceInterfaceRxGreenBytes": me1200EvcStatusEceInterfaceRxGreenBytes,
       "me1200EvcStatusEceInterfaceRxYellowFrames": me1200EvcStatusEceInterfaceRxYellowFrames,
       "me1200EvcStatusEceInterfaceRxYellowBytes": me1200EvcStatusEceInterfaceRxYellowBytes,
       "me1200EvcStatusEceInterfaceRxRedFrames": me1200EvcStatusEceInterfaceRxRedFrames,
       "me1200EvcStatusEceInterfaceRxRedBytes": me1200EvcStatusEceInterfaceRxRedBytes,
       "me1200EvcStatusEceInterfaceRxDiscardFrames": me1200EvcStatusEceInterfaceRxDiscardFrames,
       "me1200EvcStatusEceInterfaceRxDiscardBytes": me1200EvcStatusEceInterfaceRxDiscardBytes,
       "me1200EvcStatusEceInterfaceTxGreenFrames": me1200EvcStatusEceInterfaceTxGreenFrames,
       "me1200EvcStatusEceInterfaceTxGreenBytes": me1200EvcStatusEceInterfaceTxGreenBytes,
       "me1200EvcStatusEceInterfaceTxYellowFrames": me1200EvcStatusEceInterfaceTxYellowFrames,
       "me1200EvcStatusEceInterfaceTxYellowBytes": me1200EvcStatusEceInterfaceTxYellowBytes,
       "me1200EvcStatusEceInterfaceTxDiscardFrames": me1200EvcStatusEceInterfaceTxDiscardFrames,
       "me1200EvcStatusEceInterfaceTxDiscardBytes": me1200EvcStatusEceInterfaceTxDiscardBytes,
       "me1200EvcControl": me1200EvcControl,
       "me1200EvcControlEvcInterfaceTable": me1200EvcControlEvcInterfaceTable,
       "me1200EvcControlEvcInterfaceEntry": me1200EvcControlEvcInterfaceEntry,
       "me1200EvcControlEvcInterfaceEvcId": me1200EvcControlEvcInterfaceEvcId,
       "me1200EvcControlEvcInterfaceIfIndex": me1200EvcControlEvcInterfaceIfIndex,
       "me1200EvcControlEvcInterfaceClearStatistics": me1200EvcControlEvcInterfaceClearStatistics,
       "me1200EvcControlEceInterfaceTable": me1200EvcControlEceInterfaceTable,
       "me1200EvcControlEceInterfaceEntry": me1200EvcControlEceInterfaceEntry,
       "me1200EvcControlEceInterfaceIndex": me1200EvcControlEceInterfaceIndex,
       "me1200EvcControlEceInterfaceIfIndex": me1200EvcControlEceInterfaceIfIndex,
       "me1200EvcControlEceInterfaceClearStatistics": me1200EvcControlEceInterfaceClearStatistics,
       "me1200EvcMibConformance": me1200EvcMibConformance,
       "me1200EvcMibCompliances": me1200EvcMibCompliances,
       "me1200EvcMibCompliance": me1200EvcMibCompliance,
       "me1200EvcMibGroups": me1200EvcMibGroups,
       "me1200EvcCapabilitiesInfoGroup": me1200EvcCapabilitiesInfoGroup,
       "me1200EvcConfigInterfaceTableInfoGroup": me1200EvcConfigInterfaceTableInfoGroup,
       "me1200EvcConfigInterfaceL2cpTableInfoGroup": me1200EvcConfigInterfaceL2cpTableInfoGroup,
       "me1200EvcConfigPolicerTableInfoGroup": me1200EvcConfigPolicerTableInfoGroup,
       "me1200EvcConfigEvcTableInfoGroup": me1200EvcConfigEvcTableInfoGroup,
       "me1200EvcConfigEvcTableRowEditorInfoGroup": me1200EvcConfigEvcTableRowEditorInfoGroup,
       "me1200EvcConfigEceTableInfoGroup": me1200EvcConfigEceTableInfoGroup,
       "me1200EvcConfigEceTableRowEditorInfoGroup": me1200EvcConfigEceTableRowEditorInfoGroup,
       "me1200EvcConfigEcePrecedenceTableInfoGroup": me1200EvcConfigEcePrecedenceTableInfoGroup,
       "me1200EvcConfigEvcInterfaceTableInfoGroup": me1200EvcConfigEvcInterfaceTableInfoGroup,
       "me1200EvcStatusEvcTableInfoGroup": me1200EvcStatusEvcTableInfoGroup,
       "me1200EvcStatusEceTableInfoGroup": me1200EvcStatusEceTableInfoGroup,
       "me1200EvcStatusEvcInterfaceTableInfoGroup": me1200EvcStatusEvcInterfaceTableInfoGroup,
       "me1200EvcStatusEceInterfaceTableInfoGroup": me1200EvcStatusEceInterfaceTableInfoGroup,
       "me1200EvcControlEvcInterfaceTableInfoGroup": me1200EvcControlEvcInterfaceTableInfoGroup,
       "me1200EvcControlEceInterfaceTableInfoGroup": me1200EvcControlEceInterfaceTableInfoGroup}
)
