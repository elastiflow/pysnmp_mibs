# SNMP MIB module (CISCO-LWAPP-MESH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-MESH-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:05 2025
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

(cLApName,
 cLApSysMacAddress) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApName",
    "cLApSysMacAddress")

(CLDot11Channel,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLDot11Channel")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(Unsigned64,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Unsigned64")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappMeshMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616)
)
if mibBuilder.loadTexts:
    ciscoLwappMeshMIB.setRevisions(
        ("2021-04-27 00:00",
         "2019-04-11 00:00",
         "2018-09-12 00:00",
         "2017-06-09 00:00",
         "2010-10-07 00:00",
         "2010-03-03 00:00",
         "2007-03-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappMeshMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappMeshMIBNotifs = _CiscoLwappMeshMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0)
)
_CiscoLwappMeshMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMeshMIBObjects = _CiscoLwappMeshMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1)
)
_CiscoLwappMeshConfig_ObjectIdentity = ObjectIdentity
ciscoLwappMeshConfig = _CiscoLwappMeshConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1)
)
_ClMeshNodeTable_Object = MibTable
clMeshNodeTable = _ClMeshNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1)
)
if mibBuilder.loadTexts:
    clMeshNodeTable.setStatus("current")
_ClMeshNodeEntry_Object = MibTableRow
clMeshNodeEntry = _ClMeshNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1)
)
clMeshNodeEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    clMeshNodeEntry.setStatus("current")


class _ClMeshNodeRole_Type(Integer32):
    """Custom type clMeshNodeRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("map", 1),
          ("rap", 2))
    )


_ClMeshNodeRole_Type.__name__ = "Integer32"
_ClMeshNodeRole_Object = MibTableColumn
clMeshNodeRole = _ClMeshNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 1),
    _ClMeshNodeRole_Type()
)
clMeshNodeRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeRole.setStatus("current")


class _ClMeshNodeGroupName_Type(SnmpAdminString):
    """Custom type clMeshNodeGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ClMeshNodeGroupName_Type.__name__ = "SnmpAdminString"
_ClMeshNodeGroupName_Object = MibTableColumn
clMeshNodeGroupName = _ClMeshNodeGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 2),
    _ClMeshNodeGroupName_Type()
)
clMeshNodeGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeGroupName.setStatus("current")


class _ClMeshNodeBackhaul_Type(Integer32):
    """Custom type clMeshNodeBackhaul based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11b", 2),
          ("dot11g", 3))
    )


_ClMeshNodeBackhaul_Type.__name__ = "Integer32"
_ClMeshNodeBackhaul_Object = MibTableColumn
clMeshNodeBackhaul = _ClMeshNodeBackhaul_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 3),
    _ClMeshNodeBackhaul_Type()
)
clMeshNodeBackhaul.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeBackhaul.setStatus("current")
_ClMeshNodeBackhaulDataRate_Type = Unsigned32
_ClMeshNodeBackhaulDataRate_Object = MibTableColumn
clMeshNodeBackhaulDataRate = _ClMeshNodeBackhaulDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 4),
    _ClMeshNodeBackhaulDataRate_Type()
)
clMeshNodeBackhaulDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeBackhaulDataRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    clMeshNodeBackhaulDataRate.setUnits("Kbps")
_ClMeshNodeEthernetBridge_Type = TruthValue
_ClMeshNodeEthernetBridge_Object = MibTableColumn
clMeshNodeEthernetBridge = _ClMeshNodeEthernetBridge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 5),
    _ClMeshNodeEthernetBridge_Type()
)
clMeshNodeEthernetBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeEthernetBridge.setStatus("current")


class _ClMeshNodeEthernetLinkStatus_Type(Integer32):
    """Custom type clMeshNodeEthernetLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ClMeshNodeEthernetLinkStatus_Type.__name__ = "Integer32"
_ClMeshNodeEthernetLinkStatus_Object = MibTableColumn
clMeshNodeEthernetLinkStatus = _ClMeshNodeEthernetLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 6),
    _ClMeshNodeEthernetLinkStatus_Type()
)
clMeshNodeEthernetLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeEthernetLinkStatus.setStatus("current")
_ClMeshNodePublicSafetyBackhaul_Type = TruthValue
_ClMeshNodePublicSafetyBackhaul_Object = MibTableColumn
clMeshNodePublicSafetyBackhaul = _ClMeshNodePublicSafetyBackhaul_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 7),
    _ClMeshNodePublicSafetyBackhaul_Type()
)
clMeshNodePublicSafetyBackhaul.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodePublicSafetyBackhaul.setStatus("deprecated")
_ClMeshNodeParentMacAddress_Type = MacAddress
_ClMeshNodeParentMacAddress_Object = MibTableColumn
clMeshNodeParentMacAddress = _ClMeshNodeParentMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 8),
    _ClMeshNodeParentMacAddress_Type()
)
clMeshNodeParentMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeParentMacAddress.setStatus("current")


class _ClMeshNodeHeaterStatus_Type(Integer32):
    """Custom type clMeshNodeHeaterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_ClMeshNodeHeaterStatus_Type.__name__ = "Integer32"
_ClMeshNodeHeaterStatus_Object = MibTableColumn
clMeshNodeHeaterStatus = _ClMeshNodeHeaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 9),
    _ClMeshNodeHeaterStatus_Type()
)
clMeshNodeHeaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeHeaterStatus.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeHeaterStatus.setUnits("Percent")
_ClMeshNodeInternalTemp_Type = Integer32
_ClMeshNodeInternalTemp_Object = MibTableColumn
clMeshNodeInternalTemp = _ClMeshNodeInternalTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 10),
    _ClMeshNodeInternalTemp_Type()
)
clMeshNodeInternalTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeInternalTemp.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeInternalTemp.setUnits("degree Celsius")


class _ClMeshNodeType_Type(Integer32):
    """Custom type clMeshNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("indoor", 1),
          ("outdoor", 2))
    )


_ClMeshNodeType_Type.__name__ = "Integer32"
_ClMeshNodeType_Object = MibTableColumn
clMeshNodeType = _ClMeshNodeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 11),
    _ClMeshNodeType_Type()
)
clMeshNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeType.setStatus("current")
_ClMeshNodeHops_Type = Gauge32
_ClMeshNodeHops_Object = MibTableColumn
clMeshNodeHops = _ClMeshNodeHops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 12),
    _ClMeshNodeHops_Type()
)
clMeshNodeHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeHops.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeHops.setUnits("hops")


class _ClMeshNodeChildCount_Type(Gauge32):
    """Custom type clMeshNodeChildCount based on Gauge32"""
    defaultValue = 0


_ClMeshNodeChildCount_Type.__name__ = "Gauge32"
_ClMeshNodeChildCount_Object = MibTableColumn
clMeshNodeChildCount = _ClMeshNodeChildCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 13),
    _ClMeshNodeChildCount_Type()
)
clMeshNodeChildCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeChildCount.setStatus("current")


class _ClMeshNodeBackhaulRadio_Type(Integer32):
    """Custom type clMeshNodeBackhaulRadio based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("dot11bg", 2),
          ("dot11a", 3))
    )


_ClMeshNodeBackhaulRadio_Type.__name__ = "Integer32"
_ClMeshNodeBackhaulRadio_Object = MibTableColumn
clMeshNodeBackhaulRadio = _ClMeshNodeBackhaulRadio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 14),
    _ClMeshNodeBackhaulRadio_Type()
)
clMeshNodeBackhaulRadio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeBackhaulRadio.setStatus("current")


class _ClMeshNodeBHDataRate_Type(Integer32):
    """Custom type clMeshNodeBHDataRate based on Integer32"""
    defaultValue = 4

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
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("mbps1", 1),
          ("mbps2", 2),
          ("mbps5point5", 3),
          ("mbps6", 4),
          ("mbps9", 5),
          ("mbps11", 6),
          ("mbps12", 7),
          ("mbps18", 8),
          ("mbps24", 9),
          ("mbps36", 10),
          ("mbps48", 11),
          ("mbps54", 12),
          ("auto", 13),
          ("htMcs0", 14),
          ("htMcs1", 15),
          ("htMcs2", 16),
          ("htMcs3", 17),
          ("htMcs4", 18),
          ("htMcs5", 19),
          ("htMcs6", 20),
          ("htMcs7", 21),
          ("htMcs8", 22),
          ("htMcs9", 23),
          ("htMcs10", 24),
          ("htMcs11", 25),
          ("htMcs12", 26),
          ("htMcs13", 27),
          ("htMcs14", 28),
          ("htMcs15", 29),
          ("htMcs16", 30),
          ("htMcs17", 31),
          ("htMcs18", 32),
          ("htMcs19", 33),
          ("htMcs20", 34),
          ("htMcs21", 35),
          ("htMcs22", 36),
          ("htMcs23", 37),
          ("vhtMcs0Ss1", 38),
          ("vhtMcs1Ss1", 39),
          ("vhtMcs2Ss1", 40),
          ("vhtMcs3Ss1", 41),
          ("vhtMcs4Ss1", 42),
          ("vhtMcs5Ss1", 43),
          ("vhtMcs6Ss1", 44),
          ("vhtMcs7Ss1", 45),
          ("vhtMcs8Ss1", 46),
          ("vhtMcs9Ss1", 47),
          ("vhtMcs0Ss2", 48),
          ("vhtMcs1Ss2", 49),
          ("vhtMcs2Ss2", 50),
          ("vhtMcs3Ss2", 51),
          ("vhtMcs4Ss2", 52),
          ("vhtMcs5Ss2", 53),
          ("vhtMcs6Ss2", 54),
          ("vhtMcs7Ss2", 55),
          ("vhtMcs8Ss2", 56),
          ("vhtMcs9Ss2", 57),
          ("vhtMcs0Ss3", 58),
          ("vhtMcs1Ss3", 59),
          ("vhtMcs2Ss3", 60),
          ("vhtMcs3Ss3", 61),
          ("vhtMcs4Ss3", 62),
          ("vhtMcs5Ss3", 63),
          ("vhtMcs6Ss3", 64),
          ("vhtMcs7Ss3", 65),
          ("vhtMcs8Ss3", 66),
          ("vhtMcs9Ss3", 67),
          ("default", 65535))
    )


_ClMeshNodeBHDataRate_Type.__name__ = "Integer32"
_ClMeshNodeBHDataRate_Object = MibTableColumn
clMeshNodeBHDataRate = _ClMeshNodeBHDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 15),
    _ClMeshNodeBHDataRate_Type()
)
clMeshNodeBHDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeBHDataRate.setStatus("current")
_ClMeshDaisyChainEnabled_Type = TruthValue
_ClMeshDaisyChainEnabled_Object = MibTableColumn
clMeshDaisyChainEnabled = _ClMeshDaisyChainEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 16),
    _ClMeshDaisyChainEnabled_Type()
)
clMeshDaisyChainEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshDaisyChainEnabled.setStatus("current")
_ClMeshPrefParentMacAddress_Type = MacAddress
_ClMeshPrefParentMacAddress_Object = MibTableColumn
clMeshPrefParentMacAddress = _ClMeshPrefParentMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 17),
    _ClMeshPrefParentMacAddress_Type()
)
clMeshPrefParentMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshPrefParentMacAddress.setStatus("current")
_ClMeshNodeBGNStrictMatch_Type = TruthValue
_ClMeshNodeBGNStrictMatch_Object = MibTableColumn
clMeshNodeBGNStrictMatch = _ClMeshNodeBGNStrictMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 18),
    _ClMeshNodeBGNStrictMatch_Type()
)
clMeshNodeBGNStrictMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeBGNStrictMatch.setStatus("current")
_ClMeshNodeVlanEnabled_Type = TruthValue
_ClMeshNodeVlanEnabled_Object = MibTableColumn
clMeshNodeVlanEnabled = _ClMeshNodeVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 19),
    _ClMeshNodeVlanEnabled_Type()
)
clMeshNodeVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeVlanEnabled.setStatus("current")
_ClMeshNodeNativeVlanId_Type = Unsigned32
_ClMeshNodeNativeVlanId_Object = MibTableColumn
clMeshNodeNativeVlanId = _ClMeshNodeNativeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 20),
    _ClMeshNodeNativeVlanId_Type()
)
clMeshNodeNativeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeNativeVlanId.setStatus("current")


class _ClMeshNodePskKeyClear_Type(TruthValue):
    """Custom type clMeshNodePskKeyClear based on TruthValue"""
    defaultValue = 2


_ClMeshNodePskKeyClear_Type.__name__ = "TruthValue"
_ClMeshNodePskKeyClear_Object = MibTableColumn
clMeshNodePskKeyClear = _ClMeshNodePskKeyClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 21),
    _ClMeshNodePskKeyClear_Type()
)
clMeshNodePskKeyClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodePskKeyClear.setStatus("current")


class _ClMeshNodeRAPDownlinkBackhaul_Type(Integer32):
    """Custom type clMeshNodeRAPDownlinkBackhaul based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("slot0", 1),
          ("slot1", 2))
    )


_ClMeshNodeRAPDownlinkBackhaul_Type.__name__ = "Integer32"
_ClMeshNodeRAPDownlinkBackhaul_Object = MibTableColumn
clMeshNodeRAPDownlinkBackhaul = _ClMeshNodeRAPDownlinkBackhaul_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 22),
    _ClMeshNodeRAPDownlinkBackhaul_Type()
)
clMeshNodeRAPDownlinkBackhaul.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeRAPDownlinkBackhaul.setStatus("current")


class _ClMeshNodeBlockChild_Type(TruthValue):
    """Custom type clMeshNodeBlockChild based on TruthValue"""
    defaultValue = 2


_ClMeshNodeBlockChild_Type.__name__ = "TruthValue"
_ClMeshNodeBlockChild_Object = MibTableColumn
clMeshNodeBlockChild = _ClMeshNodeBlockChild_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 23),
    _ClMeshNodeBlockChild_Type()
)
clMeshNodeBlockChild.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeBlockChild.setStatus("current")


class _ClMeshNodeBhaulDataRateType_Type(Integer32):
    """Custom type clMeshNodeBhaulDataRateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("dot11abg", 2),
          ("dot11nMcs", 3),
          ("dot11acMcs", 4),
          ("dot11axMcs", 5))
    )


_ClMeshNodeBhaulDataRateType_Type.__name__ = "Integer32"
_ClMeshNodeBhaulDataRateType_Object = MibTableColumn
clMeshNodeBhaulDataRateType = _ClMeshNodeBhaulDataRateType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 24),
    _ClMeshNodeBhaulDataRateType_Type()
)
clMeshNodeBhaulDataRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeBhaulDataRateType.setStatus("current")


class _ClMeshNodeBhaulDataRate_Type(Integer32):
    """Custom type clMeshNodeBhaulDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1000,
              2000,
              5500,
              6000,
              9000,
              11000,
              12000,
              18000,
              24000,
              36000,
              48000,
              54000)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mbps1", 1000),
          ("mbps2", 2000),
          ("mbps5point5", 5500),
          ("mbps6", 6000),
          ("mbps9", 9000),
          ("mbps11", 11000),
          ("mbps12", 12000),
          ("mbps18", 18000),
          ("mbps24", 24000),
          ("mbps36", 36000),
          ("mbps48", 48000),
          ("mbps54", 54000))
    )


_ClMeshNodeBhaulDataRate_Type.__name__ = "Integer32"
_ClMeshNodeBhaulDataRate_Object = MibTableColumn
clMeshNodeBhaulDataRate = _ClMeshNodeBhaulDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 25),
    _ClMeshNodeBhaulDataRate_Type()
)
clMeshNodeBhaulDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeBhaulDataRate.setStatus("current")
_ClMeshNodeBhaulDataRateMcsIndex_Type = Unsigned32
_ClMeshNodeBhaulDataRateMcsIndex_Object = MibTableColumn
clMeshNodeBhaulDataRateMcsIndex = _ClMeshNodeBhaulDataRateMcsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 26),
    _ClMeshNodeBhaulDataRateMcsIndex_Type()
)
clMeshNodeBhaulDataRateMcsIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeBhaulDataRateMcsIndex.setStatus("current")
_ClMeshNodeBhaulDataRateDot11acSpatialStream_Type = Unsigned32
_ClMeshNodeBhaulDataRateDot11acSpatialStream_Object = MibTableColumn
clMeshNodeBhaulDataRateDot11acSpatialStream = _ClMeshNodeBhaulDataRateDot11acSpatialStream_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 27),
    _ClMeshNodeBhaulDataRateDot11acSpatialStream_Type()
)
clMeshNodeBhaulDataRateDot11acSpatialStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeBhaulDataRateDot11acSpatialStream.setStatus("current")
_ClMeshNodeBhaulDataRateDot11axSpatialStream_Type = Unsigned32
_ClMeshNodeBhaulDataRateDot11axSpatialStream_Object = MibTableColumn
clMeshNodeBhaulDataRateDot11axSpatialStream = _ClMeshNodeBhaulDataRateDot11axSpatialStream_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 28),
    _ClMeshNodeBhaulDataRateDot11axSpatialStream_Type()
)
clMeshNodeBhaulDataRateDot11axSpatialStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeBhaulDataRateDot11axSpatialStream.setStatus("current")
_ClMeshPskTable_Object = MibTable
clMeshPskTable = _ClMeshPskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 2)
)
if mibBuilder.loadTexts:
    clMeshPskTable.setStatus("current")
_ClMeshPskEntry_Object = MibTableRow
clMeshPskEntry = _ClMeshPskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 2, 1)
)
clMeshPskEntry.setIndexNames(
    (0, "CISCO-LWAPP-MESH-MIB", "clMeshPskIndex"),
)
if mibBuilder.loadTexts:
    clMeshPskEntry.setStatus("current")
_ClMeshPskIndex_Type = Unsigned32
_ClMeshPskIndex_Object = MibTableColumn
clMeshPskIndex = _ClMeshPskIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 2, 1, 1),
    _ClMeshPskIndex_Type()
)
clMeshPskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clMeshPskIndex.setStatus("current")


class _ClMeshPskKey_Type(OctetString):
    """Custom type clMeshPskKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 32),
    )


_ClMeshPskKey_Type.__name__ = "OctetString"
_ClMeshPskKey_Object = MibTableColumn
clMeshPskKey = _ClMeshPskKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 2, 1, 2),
    _ClMeshPskKey_Type()
)
clMeshPskKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clMeshPskKey.setStatus("current")
_ClMeshPskTimeStamp_Type = SnmpAdminString
_ClMeshPskTimeStamp_Object = MibTableColumn
clMeshPskTimeStamp = _ClMeshPskTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 2, 1, 3),
    _ClMeshPskTimeStamp_Type()
)
clMeshPskTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshPskTimeStamp.setStatus("current")


class _ClMeshPskKeyDesc_Type(SnmpAdminString):
    """Custom type clMeshPskKeyDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClMeshPskKeyDesc_Type.__name__ = "SnmpAdminString"
_ClMeshPskKeyDesc_Object = MibTableColumn
clMeshPskKeyDesc = _ClMeshPskKeyDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 2, 1, 4),
    _ClMeshPskKeyDesc_Type()
)
clMeshPskKeyDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clMeshPskKeyDesc.setStatus("current")
_ClMeshPskRowStatus_Type = RowStatus
_ClMeshPskRowStatus_Object = MibTableColumn
clMeshPskRowStatus = _ClMeshPskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 2, 1, 5),
    _ClMeshPskRowStatus_Type()
)
clMeshPskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clMeshPskRowStatus.setStatus("current")
_ClMeshProfileTable_Object = MibTable
clMeshProfileTable = _ClMeshProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3)
)
if mibBuilder.loadTexts:
    clMeshProfileTable.setStatus("current")
_ClMeshProfileEntry_Object = MibTableRow
clMeshProfileEntry = _ClMeshProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1)
)
clMeshProfileEntry.setIndexNames(
    (0, "CISCO-LWAPP-MESH-MIB", "cLMeshProfileName"),
)
if mibBuilder.loadTexts:
    clMeshProfileEntry.setStatus("current")


class _CLMeshProfileName_Type(SnmpAdminString):
    """Custom type cLMeshProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLMeshProfileName_Type.__name__ = "SnmpAdminString"
_CLMeshProfileName_Object = MibTableColumn
cLMeshProfileName = _CLMeshProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 1),
    _CLMeshProfileName_Type()
)
cLMeshProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMeshProfileName.setStatus("current")


class _CLMeshProfileDescr_Type(SnmpAdminString):
    """Custom type cLMeshProfileDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLMeshProfileDescr_Type.__name__ = "SnmpAdminString"
_CLMeshProfileDescr_Object = MibTableColumn
cLMeshProfileDescr = _CLMeshProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 2),
    _CLMeshProfileDescr_Type()
)
cLMeshProfileDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileDescr.setStatus("current")


class _CLMeshProfileASTools_Type(TruthValue):
    """Custom type cLMeshProfileASTools based on TruthValue"""
    defaultValue = 2


_CLMeshProfileASTools_Type.__name__ = "TruthValue"
_CLMeshProfileASTools_Object = MibTableColumn
cLMeshProfileASTools = _CLMeshProfileASTools_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 3),
    _CLMeshProfileASTools_Type()
)
cLMeshProfileASTools.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileASTools.setStatus("current")


class _CLMeshProfileAmsdu_Type(TruthValue):
    """Custom type cLMeshProfileAmsdu based on TruthValue"""
    defaultValue = 1


_CLMeshProfileAmsdu_Type.__name__ = "TruthValue"
_CLMeshProfileAmsdu_Object = MibTableColumn
cLMeshProfileAmsdu = _CLMeshProfileAmsdu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 4),
    _CLMeshProfileAmsdu_Type()
)
cLMeshProfileAmsdu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileAmsdu.setStatus("current")


class _CLMeshProfileBackgroundScan_Type(TruthValue):
    """Custom type cLMeshProfileBackgroundScan based on TruthValue"""
    defaultValue = 2


_CLMeshProfileBackgroundScan_Type.__name__ = "TruthValue"
_CLMeshProfileBackgroundScan_Object = MibTableColumn
cLMeshProfileBackgroundScan = _CLMeshProfileBackgroundScan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 5),
    _CLMeshProfileBackgroundScan_Type()
)
cLMeshProfileBackgroundScan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileBackgroundScan.setStatus("current")


class _CLMeshProfileCcnMode_Type(TruthValue):
    """Custom type cLMeshProfileCcnMode based on TruthValue"""
    defaultValue = 2


_CLMeshProfileCcnMode_Type.__name__ = "TruthValue"
_CLMeshProfileCcnMode_Object = MibTableColumn
cLMeshProfileCcnMode = _CLMeshProfileCcnMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 6),
    _CLMeshProfileCcnMode_Type()
)
cLMeshProfileCcnMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileCcnMode.setStatus("current")


class _CLMeshProfileUniversalAccess_Type(TruthValue):
    """Custom type cLMeshProfileUniversalAccess based on TruthValue"""
    defaultValue = 2


_CLMeshProfileUniversalAccess_Type.__name__ = "TruthValue"
_CLMeshProfileUniversalAccess_Object = MibTableColumn
cLMeshProfileUniversalAccess = _CLMeshProfileUniversalAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 7),
    _CLMeshProfileUniversalAccess_Type()
)
cLMeshProfileUniversalAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileUniversalAccess.setStatus("current")


class _CLMeshProfileEtherVlanTransparent_Type(TruthValue):
    """Custom type cLMeshProfileEtherVlanTransparent based on TruthValue"""
    defaultValue = 1


_CLMeshProfileEtherVlanTransparent_Type.__name__ = "TruthValue"
_CLMeshProfileEtherVlanTransparent_Object = MibTableColumn
cLMeshProfileEtherVlanTransparent = _CLMeshProfileEtherVlanTransparent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 8),
    _CLMeshProfileEtherVlanTransparent_Type()
)
cLMeshProfileEtherVlanTransparent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileEtherVlanTransparent.setStatus("current")


class _CLMeshProfileFullSectorDfs_Type(TruthValue):
    """Custom type cLMeshProfileFullSectorDfs based on TruthValue"""
    defaultValue = 1


_CLMeshProfileFullSectorDfs_Type.__name__ = "TruthValue"
_CLMeshProfileFullSectorDfs_Object = MibTableColumn
cLMeshProfileFullSectorDfs = _CLMeshProfileFullSectorDfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 9),
    _CLMeshProfileFullSectorDfs_Type()
)
cLMeshProfileFullSectorDfs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileFullSectorDfs.setStatus("current")


class _CLMeshProfileIdsState_Type(TruthValue):
    """Custom type cLMeshProfileIdsState based on TruthValue"""
    defaultValue = 2


_CLMeshProfileIdsState_Type.__name__ = "TruthValue"
_CLMeshProfileIdsState_Object = MibTableColumn
cLMeshProfileIdsState = _CLMeshProfileIdsState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 10),
    _CLMeshProfileIdsState_Type()
)
cLMeshProfileIdsState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileIdsState.setStatus("current")


class _CLMeshProfileMulticastMode_Type(Integer32):
    """Custom type cLMeshProfileMulticastMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modeRegular", 1),
          ("modeIn", 2),
          ("modeOut", 3))
    )


_CLMeshProfileMulticastMode_Type.__name__ = "Integer32"
_CLMeshProfileMulticastMode_Object = MibTableColumn
cLMeshProfileMulticastMode = _CLMeshProfileMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 11),
    _CLMeshProfileMulticastMode_Type()
)
cLMeshProfileMulticastMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileMulticastMode.setStatus("current")


class _CLMeshProfileRange_Type(Unsigned32):
    """Custom type cLMeshProfileRange based on Unsigned32"""
    defaultValue = 12000


_CLMeshProfileRange_Type.__name__ = "Unsigned32"
_CLMeshProfileRange_Object = MibTableColumn
cLMeshProfileRange = _CLMeshProfileRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 12),
    _CLMeshProfileRange_Type()
)
cLMeshProfileRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileRange.setStatus("current")
if mibBuilder.loadTexts:
    cLMeshProfileRange.setUnits("feet")


class _CLMeshProfileSecurityMode_Type(Integer32):
    """Custom type cLMeshProfileSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eap", 1),
          ("psk", 2))
    )


_CLMeshProfileSecurityMode_Type.__name__ = "Integer32"
_CLMeshProfileSecurityMode_Object = MibTableColumn
cLMeshProfileSecurityMode = _CLMeshProfileSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 13),
    _CLMeshProfileSecurityMode_Type()
)
cLMeshProfileSecurityMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileSecurityMode.setStatus("current")


class _CLMeshProfileConvergenceMethod_Type(Integer32):
    """Custom type cLMeshProfileConvergenceMethod based on Integer32"""
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
        *(("standard", 1),
          ("fast", 2),
          ("veryFast", 3),
          ("noiseTolerentFast", 4))
    )


_CLMeshProfileConvergenceMethod_Type.__name__ = "Integer32"
_CLMeshProfileConvergenceMethod_Object = MibTableColumn
cLMeshProfileConvergenceMethod = _CLMeshProfileConvergenceMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 14),
    _CLMeshProfileConvergenceMethod_Type()
)
cLMeshProfileConvergenceMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileConvergenceMethod.setStatus("current")


class _CLMeshProfileLscOnlyAuthentication_Type(TruthValue):
    """Custom type cLMeshProfileLscOnlyAuthentication based on TruthValue"""
    defaultValue = 2


_CLMeshProfileLscOnlyAuthentication_Type.__name__ = "TruthValue"
_CLMeshProfileLscOnlyAuthentication_Object = MibTableColumn
cLMeshProfileLscOnlyAuthentication = _CLMeshProfileLscOnlyAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 15),
    _CLMeshProfileLscOnlyAuthentication_Type()
)
cLMeshProfileLscOnlyAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileLscOnlyAuthentication.setStatus("current")


class _CLMeshProfileBridgeGroupName_Type(SnmpAdminString):
    """Custom type cLMeshProfileBridgeGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CLMeshProfileBridgeGroupName_Type.__name__ = "SnmpAdminString"
_CLMeshProfileBridgeGroupName_Object = MibTableColumn
cLMeshProfileBridgeGroupName = _CLMeshProfileBridgeGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 16),
    _CLMeshProfileBridgeGroupName_Type()
)
cLMeshProfileBridgeGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileBridgeGroupName.setStatus("current")


class _CLMeshProfileBGNStrictmatch_Type(TruthValue):
    """Custom type cLMeshProfileBGNStrictmatch based on TruthValue"""
    defaultValue = 2


_CLMeshProfileBGNStrictmatch_Type.__name__ = "TruthValue"
_CLMeshProfileBGNStrictmatch_Object = MibTableColumn
cLMeshProfileBGNStrictmatch = _CLMeshProfileBGNStrictmatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 17),
    _CLMeshProfileBGNStrictmatch_Type()
)
cLMeshProfileBGNStrictmatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileBGNStrictmatch.setStatus("current")


class _CLMeshProfileEthernetBridging_Type(TruthValue):
    """Custom type cLMeshProfileEthernetBridging based on TruthValue"""
    defaultValue = 2


_CLMeshProfileEthernetBridging_Type.__name__ = "TruthValue"
_CLMeshProfileEthernetBridging_Object = MibTableColumn
cLMeshProfileEthernetBridging = _CLMeshProfileEthernetBridging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 18),
    _CLMeshProfileEthernetBridging_Type()
)
cLMeshProfileEthernetBridging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileEthernetBridging.setStatus("current")


class _CLMeshProfileBatteryState_Type(TruthValue):
    """Custom type cLMeshProfileBatteryState based on TruthValue"""
    defaultValue = 1


_CLMeshProfileBatteryState_Type.__name__ = "TruthValue"
_CLMeshProfileBatteryState_Object = MibTableColumn
cLMeshProfileBatteryState = _CLMeshProfileBatteryState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 19),
    _CLMeshProfileBatteryState_Type()
)
cLMeshProfileBatteryState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileBatteryState.setStatus("current")


class _CLMeshProfileAuthorizationMethod_Type(SnmpAdminString):
    """Custom type cLMeshProfileAuthorizationMethod based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLMeshProfileAuthorizationMethod_Type.__name__ = "SnmpAdminString"
_CLMeshProfileAuthorizationMethod_Object = MibTableColumn
cLMeshProfileAuthorizationMethod = _CLMeshProfileAuthorizationMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 20),
    _CLMeshProfileAuthorizationMethod_Type()
)
cLMeshProfileAuthorizationMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileAuthorizationMethod.setStatus("current")


class _CLMeshProfileAuthenticationMethod_Type(SnmpAdminString):
    """Custom type cLMeshProfileAuthenticationMethod based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLMeshProfileAuthenticationMethod_Type.__name__ = "SnmpAdminString"
_CLMeshProfileAuthenticationMethod_Object = MibTableColumn
cLMeshProfileAuthenticationMethod = _CLMeshProfileAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 21),
    _CLMeshProfileAuthenticationMethod_Type()
)
cLMeshProfileAuthenticationMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileAuthenticationMethod.setStatus("current")


class _CLMeshProfileDot11bgBhaulRateType_Type(Integer32):
    """Custom type cLMeshProfileDot11bgBhaulRateType based on Integer32"""
    defaultValue = 1

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
        *(("auto", 1),
          ("dot11abg", 2),
          ("dot11nMcs", 3),
          ("dot11axMcs", 4))
    )


_CLMeshProfileDot11bgBhaulRateType_Type.__name__ = "Integer32"
_CLMeshProfileDot11bgBhaulRateType_Object = MibTableColumn
cLMeshProfileDot11bgBhaulRateType = _CLMeshProfileDot11bgBhaulRateType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 22),
    _CLMeshProfileDot11bgBhaulRateType_Type()
)
cLMeshProfileDot11bgBhaulRateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileDot11bgBhaulRateType.setStatus("current")


class _CLMeshProfileDot11bgBhaulRate_Type(Integer32):
    """Custom type cLMeshProfileDot11bgBhaulRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1000,
              2000,
              5500,
              6000,
              9000,
              11000,
              12000,
              18000,
              24000,
              36000,
              48000,
              54000)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mbps1", 1000),
          ("mbps2", 2000),
          ("mbps5point5", 5500),
          ("mbps6", 6000),
          ("mbps9", 9000),
          ("mbps11", 11000),
          ("mbps12", 12000),
          ("mbps18", 18000),
          ("mbps24", 24000),
          ("mbps36", 36000),
          ("mbps48", 48000),
          ("mbps54", 54000))
    )


_CLMeshProfileDot11bgBhaulRate_Type.__name__ = "Integer32"
_CLMeshProfileDot11bgBhaulRate_Object = MibTableColumn
cLMeshProfileDot11bgBhaulRate = _CLMeshProfileDot11bgBhaulRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 23),
    _CLMeshProfileDot11bgBhaulRate_Type()
)
cLMeshProfileDot11bgBhaulRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileDot11bgBhaulRate.setStatus("current")


class _CLMeshProfileDot11bgBhaulRateDot11nMcsIndex_Type(Unsigned32):
    """Custom type cLMeshProfileDot11bgBhaulRateDot11nMcsIndex based on Unsigned32"""
    defaultValue = 0


_CLMeshProfileDot11bgBhaulRateDot11nMcsIndex_Type.__name__ = "Unsigned32"
_CLMeshProfileDot11bgBhaulRateDot11nMcsIndex_Object = MibTableColumn
cLMeshProfileDot11bgBhaulRateDot11nMcsIndex = _CLMeshProfileDot11bgBhaulRateDot11nMcsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 24),
    _CLMeshProfileDot11bgBhaulRateDot11nMcsIndex_Type()
)
cLMeshProfileDot11bgBhaulRateDot11nMcsIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileDot11bgBhaulRateDot11nMcsIndex.setStatus("current")


class _CLMeshProfileDot11aBhaulRateType_Type(Integer32):
    """Custom type cLMeshProfileDot11aBhaulRateType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("dot11abg", 2),
          ("dot11nMcs", 3),
          ("dot11acMcs", 4),
          ("dot11axMcs", 5))
    )


_CLMeshProfileDot11aBhaulRateType_Type.__name__ = "Integer32"
_CLMeshProfileDot11aBhaulRateType_Object = MibTableColumn
cLMeshProfileDot11aBhaulRateType = _CLMeshProfileDot11aBhaulRateType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 25),
    _CLMeshProfileDot11aBhaulRateType_Type()
)
cLMeshProfileDot11aBhaulRateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileDot11aBhaulRateType.setStatus("current")


class _CLMeshProfileDot11aBhaulRate_Type(Integer32):
    """Custom type cLMeshProfileDot11aBhaulRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6000,
              9000,
              12000,
              18000,
              24000,
              36000,
              48000,
              54000)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mbps6", 6000),
          ("mbps9", 9000),
          ("mbps12", 12000),
          ("mbps18", 18000),
          ("mbps24", 24000),
          ("mbps36", 36000),
          ("mbps48", 48000),
          ("mbps54", 54000))
    )


_CLMeshProfileDot11aBhaulRate_Type.__name__ = "Integer32"
_CLMeshProfileDot11aBhaulRate_Object = MibTableColumn
cLMeshProfileDot11aBhaulRate = _CLMeshProfileDot11aBhaulRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 26),
    _CLMeshProfileDot11aBhaulRate_Type()
)
cLMeshProfileDot11aBhaulRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileDot11aBhaulRate.setStatus("current")


class _CLMeshProfileDot11aBhaulRateDot11nMcsIndex_Type(Unsigned32):
    """Custom type cLMeshProfileDot11aBhaulRateDot11nMcsIndex based on Unsigned32"""
    defaultValue = 0


_CLMeshProfileDot11aBhaulRateDot11nMcsIndex_Type.__name__ = "Unsigned32"
_CLMeshProfileDot11aBhaulRateDot11nMcsIndex_Object = MibTableColumn
cLMeshProfileDot11aBhaulRateDot11nMcsIndex = _CLMeshProfileDot11aBhaulRateDot11nMcsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 27),
    _CLMeshProfileDot11aBhaulRateDot11nMcsIndex_Type()
)
cLMeshProfileDot11aBhaulRateDot11nMcsIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileDot11aBhaulRateDot11nMcsIndex.setStatus("current")


class _CLMeshProfileDot11aBhaulRateDot11acMcsIndex_Type(Unsigned32):
    """Custom type cLMeshProfileDot11aBhaulRateDot11acMcsIndex based on Unsigned32"""
    defaultValue = 0


_CLMeshProfileDot11aBhaulRateDot11acMcsIndex_Type.__name__ = "Unsigned32"
_CLMeshProfileDot11aBhaulRateDot11acMcsIndex_Object = MibTableColumn
cLMeshProfileDot11aBhaulRateDot11acMcsIndex = _CLMeshProfileDot11aBhaulRateDot11acMcsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 28),
    _CLMeshProfileDot11aBhaulRateDot11acMcsIndex_Type()
)
cLMeshProfileDot11aBhaulRateDot11acMcsIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileDot11aBhaulRateDot11acMcsIndex.setStatus("current")


class _CLMeshProfileDot11aBhaulRateDot11acSpatialStream_Type(Unsigned32):
    """Custom type cLMeshProfileDot11aBhaulRateDot11acSpatialStream based on Unsigned32"""
    defaultValue = 1


_CLMeshProfileDot11aBhaulRateDot11acSpatialStream_Type.__name__ = "Unsigned32"
_CLMeshProfileDot11aBhaulRateDot11acSpatialStream_Object = MibTableColumn
cLMeshProfileDot11aBhaulRateDot11acSpatialStream = _CLMeshProfileDot11aBhaulRateDot11acSpatialStream_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 29),
    _CLMeshProfileDot11aBhaulRateDot11acSpatialStream_Type()
)
cLMeshProfileDot11aBhaulRateDot11acSpatialStream.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileDot11aBhaulRateDot11acSpatialStream.setStatus("current")
_ClMeshProfileRowStatus_Type = RowStatus
_ClMeshProfileRowStatus_Object = MibTableColumn
clMeshProfileRowStatus = _ClMeshProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 30),
    _ClMeshProfileRowStatus_Type()
)
clMeshProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clMeshProfileRowStatus.setStatus("current")


class _CLMeshProfileDot11bgBhaulRateDot11axMcsIndex_Type(Unsigned32):
    """Custom type cLMeshProfileDot11bgBhaulRateDot11axMcsIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_CLMeshProfileDot11bgBhaulRateDot11axMcsIndex_Type.__name__ = "Unsigned32"
_CLMeshProfileDot11bgBhaulRateDot11axMcsIndex_Object = MibTableColumn
cLMeshProfileDot11bgBhaulRateDot11axMcsIndex = _CLMeshProfileDot11bgBhaulRateDot11axMcsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 31),
    _CLMeshProfileDot11bgBhaulRateDot11axMcsIndex_Type()
)
cLMeshProfileDot11bgBhaulRateDot11axMcsIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileDot11bgBhaulRateDot11axMcsIndex.setStatus("current")


class _CLMeshProfileDot11bgBhaulRateDot11axSpatialStream_Type(Unsigned32):
    """Custom type cLMeshProfileDot11bgBhaulRateDot11axSpatialStream based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CLMeshProfileDot11bgBhaulRateDot11axSpatialStream_Type.__name__ = "Unsigned32"
_CLMeshProfileDot11bgBhaulRateDot11axSpatialStream_Object = MibTableColumn
cLMeshProfileDot11bgBhaulRateDot11axSpatialStream = _CLMeshProfileDot11bgBhaulRateDot11axSpatialStream_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 32),
    _CLMeshProfileDot11bgBhaulRateDot11axSpatialStream_Type()
)
cLMeshProfileDot11bgBhaulRateDot11axSpatialStream.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileDot11bgBhaulRateDot11axSpatialStream.setStatus("current")


class _CLMeshProfileDot11aBhaulRateDot11axMcsIndex_Type(Unsigned32):
    """Custom type cLMeshProfileDot11aBhaulRateDot11axMcsIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_CLMeshProfileDot11aBhaulRateDot11axMcsIndex_Type.__name__ = "Unsigned32"
_CLMeshProfileDot11aBhaulRateDot11axMcsIndex_Object = MibTableColumn
cLMeshProfileDot11aBhaulRateDot11axMcsIndex = _CLMeshProfileDot11aBhaulRateDot11axMcsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 33),
    _CLMeshProfileDot11aBhaulRateDot11axMcsIndex_Type()
)
cLMeshProfileDot11aBhaulRateDot11axMcsIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileDot11aBhaulRateDot11axMcsIndex.setStatus("current")


class _CLMeshProfileDot11aBhaulRateDot11axSpatialStream_Type(Unsigned32):
    """Custom type cLMeshProfileDot11aBhaulRateDot11axSpatialStream based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CLMeshProfileDot11aBhaulRateDot11axSpatialStream_Type.__name__ = "Unsigned32"
_CLMeshProfileDot11aBhaulRateDot11axSpatialStream_Object = MibTableColumn
cLMeshProfileDot11aBhaulRateDot11axSpatialStream = _CLMeshProfileDot11aBhaulRateDot11axSpatialStream_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 3, 1, 34),
    _CLMeshProfileDot11aBhaulRateDot11axSpatialStream_Type()
)
cLMeshProfileDot11aBhaulRateDot11axSpatialStream.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMeshProfileDot11aBhaulRateDot11axSpatialStream.setStatus("current")
_CiscoLwappMeshGlobalConfig_ObjectIdentity = ObjectIdentity
ciscoLwappMeshGlobalConfig = _CiscoLwappMeshGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2)
)


class _ClMeshNodeRange_Type(Unsigned32):
    """Custom type clMeshNodeRange based on Unsigned32"""
    defaultValue = 12000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 132000),
    )


_ClMeshNodeRange_Type.__name__ = "Unsigned32"
_ClMeshNodeRange_Object = MibScalar
clMeshNodeRange = _ClMeshNodeRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 1),
    _ClMeshNodeRange_Type()
)
clMeshNodeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeRange.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeRange.setUnits("feet")


class _ClMeshBackhaulClientAccess_Type(TruthValue):
    """Custom type clMeshBackhaulClientAccess based on TruthValue"""
    defaultValue = 2


_ClMeshBackhaulClientAccess_Type.__name__ = "TruthValue"
_ClMeshBackhaulClientAccess_Object = MibScalar
clMeshBackhaulClientAccess = _ClMeshBackhaulClientAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 2),
    _ClMeshBackhaulClientAccess_Type()
)
clMeshBackhaulClientAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshBackhaulClientAccess.setStatus("current")


class _ClMeshMacFilterList_Type(TruthValue):
    """Custom type clMeshMacFilterList based on TruthValue"""
    defaultValue = 1


_ClMeshMacFilterList_Type.__name__ = "TruthValue"
_ClMeshMacFilterList_Object = MibScalar
clMeshMacFilterList = _ClMeshMacFilterList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 3),
    _ClMeshMacFilterList_Type()
)
clMeshMacFilterList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshMacFilterList.setStatus("current")


class _ClMeshMeshNodeAuthFailureThreshold_Type(Unsigned32):
    """Custom type clMeshMeshNodeAuthFailureThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ClMeshMeshNodeAuthFailureThreshold_Type.__name__ = "Unsigned32"
_ClMeshMeshNodeAuthFailureThreshold_Object = MibScalar
clMeshMeshNodeAuthFailureThreshold = _ClMeshMeshNodeAuthFailureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 4),
    _ClMeshMeshNodeAuthFailureThreshold_Type()
)
clMeshMeshNodeAuthFailureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshMeshNodeAuthFailureThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clMeshMeshNodeAuthFailureThreshold.setUnits("failures")


class _ClMeshMeshChildAssociationFailuresThreshold_Type(Unsigned32):
    """Custom type clMeshMeshChildAssociationFailuresThreshold based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_ClMeshMeshChildAssociationFailuresThreshold_Type.__name__ = "Unsigned32"
_ClMeshMeshChildAssociationFailuresThreshold_Object = MibScalar
clMeshMeshChildAssociationFailuresThreshold = _ClMeshMeshChildAssociationFailuresThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 5),
    _ClMeshMeshChildAssociationFailuresThreshold_Type()
)
clMeshMeshChildAssociationFailuresThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshMeshChildAssociationFailuresThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clMeshMeshChildAssociationFailuresThreshold.setUnits("failures")


class _ClMeshMeshChildExcludedParentInterval_Type(TimeInterval):
    """Custom type clMeshMeshChildExcludedParentInterval based on TimeInterval"""
    defaultValue = 48000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18000, 96000),
    )


_ClMeshMeshChildExcludedParentInterval_Type.__name__ = "TimeInterval"
_ClMeshMeshChildExcludedParentInterval_Object = MibScalar
clMeshMeshChildExcludedParentInterval = _ClMeshMeshChildExcludedParentInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 6),
    _ClMeshMeshChildExcludedParentInterval_Type()
)
clMeshMeshChildExcludedParentInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshMeshChildExcludedParentInterval.setStatus("current")
if mibBuilder.loadTexts:
    clMeshMeshChildExcludedParentInterval.setUnits("hundredths-seconds")


class _ClMeshSNRThresholdAbate_Type(Unsigned32):
    """Custom type clMeshSNRThresholdAbate based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 50),
    )


_ClMeshSNRThresholdAbate_Type.__name__ = "Unsigned32"
_ClMeshSNRThresholdAbate_Object = MibScalar
clMeshSNRThresholdAbate = _ClMeshSNRThresholdAbate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 7),
    _ClMeshSNRThresholdAbate_Type()
)
clMeshSNRThresholdAbate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshSNRThresholdAbate.setStatus("current")
if mibBuilder.loadTexts:
    clMeshSNRThresholdAbate.setUnits("db")


class _ClMeshSNRThresholdOnset_Type(Unsigned32):
    """Custom type clMeshSNRThresholdOnset based on Unsigned32"""
    defaultValue = 12

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 50),
    )


_ClMeshSNRThresholdOnset_Type.__name__ = "Unsigned32"
_ClMeshSNRThresholdOnset_Object = MibScalar
clMeshSNRThresholdOnset = _ClMeshSNRThresholdOnset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 8),
    _ClMeshSNRThresholdOnset_Type()
)
clMeshSNRThresholdOnset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshSNRThresholdOnset.setStatus("current")
if mibBuilder.loadTexts:
    clMeshSNRThresholdOnset.setUnits("db")


class _ClMeshSNRCheckTimeInterval_Type(TimeInterval):
    """Custom type clMeshSNRCheckTimeInterval based on TimeInterval"""
    defaultValue = 18000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18000, 96000),
    )


_ClMeshSNRCheckTimeInterval_Type.__name__ = "TimeInterval"
_ClMeshSNRCheckTimeInterval_Object = MibScalar
clMeshSNRCheckTimeInterval = _ClMeshSNRCheckTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 9),
    _ClMeshSNRCheckTimeInterval_Type()
)
clMeshSNRCheckTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshSNRCheckTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    clMeshSNRCheckTimeInterval.setUnits("hundredths-seconds")


class _ClMeshExcessiveParentChangeThreshold_Type(Unsigned32):
    """Custom type clMeshExcessiveParentChangeThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ClMeshExcessiveParentChangeThreshold_Type.__name__ = "Unsigned32"
_ClMeshExcessiveParentChangeThreshold_Object = MibScalar
clMeshExcessiveParentChangeThreshold = _ClMeshExcessiveParentChangeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 10),
    _ClMeshExcessiveParentChangeThreshold_Type()
)
clMeshExcessiveParentChangeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshExcessiveParentChangeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clMeshExcessiveParentChangeThreshold.setUnits("occcurences")


class _ClMeshExcessiveParentChangeInterval_Type(TimeInterval):
    """Custom type clMeshExcessiveParentChangeInterval based on TimeInterval"""
    defaultValue = 360000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180000, 360000),
    )


_ClMeshExcessiveParentChangeInterval_Type.__name__ = "TimeInterval"
_ClMeshExcessiveParentChangeInterval_Object = MibScalar
clMeshExcessiveParentChangeInterval = _ClMeshExcessiveParentChangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 11),
    _ClMeshExcessiveParentChangeInterval_Type()
)
clMeshExcessiveParentChangeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshExcessiveParentChangeInterval.setStatus("current")
if mibBuilder.loadTexts:
    clMeshExcessiveParentChangeInterval.setUnits("hundredths-seconds")


class _ClMeshBackgroundScan_Type(TruthValue):
    """Custom type clMeshBackgroundScan based on TruthValue"""
    defaultValue = 1


_ClMeshBackgroundScan_Type.__name__ = "TruthValue"
_ClMeshBackgroundScan_Object = MibScalar
clMeshBackgroundScan = _ClMeshBackgroundScan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 12),
    _ClMeshBackgroundScan_Type()
)
clMeshBackgroundScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshBackgroundScan.setStatus("current")


class _ClMeshAuthenticationMode_Type(Integer32):
    """Custom type clMeshAuthenticationMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("eap", 2),
          ("psk", 3))
    )


_ClMeshAuthenticationMode_Type.__name__ = "Integer32"
_ClMeshAuthenticationMode_Object = MibScalar
clMeshAuthenticationMode = _ClMeshAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 13),
    _ClMeshAuthenticationMode_Type()
)
clMeshAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshAuthenticationMode.setStatus("current")


class _ClMeshExcessiveHopCountThreshold_Type(Unsigned32):
    """Custom type clMeshExcessiveHopCountThreshold based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ClMeshExcessiveHopCountThreshold_Type.__name__ = "Unsigned32"
_ClMeshExcessiveHopCountThreshold_Object = MibScalar
clMeshExcessiveHopCountThreshold = _ClMeshExcessiveHopCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 14),
    _ClMeshExcessiveHopCountThreshold_Type()
)
clMeshExcessiveHopCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshExcessiveHopCountThreshold.setStatus("current")


class _ClMeshExcessiveRapChildThreshold_Type(Unsigned32):
    """Custom type clMeshExcessiveRapChildThreshold based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ClMeshExcessiveRapChildThreshold_Type.__name__ = "Unsigned32"
_ClMeshExcessiveRapChildThreshold_Object = MibScalar
clMeshExcessiveRapChildThreshold = _ClMeshExcessiveRapChildThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 15),
    _ClMeshExcessiveRapChildThreshold_Type()
)
clMeshExcessiveRapChildThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshExcessiveRapChildThreshold.setStatus("current")


class _ClMeshExcessiveMapChildThreshold_Type(Unsigned32):
    """Custom type clMeshExcessiveMapChildThreshold based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ClMeshExcessiveMapChildThreshold_Type.__name__ = "Unsigned32"
_ClMeshExcessiveMapChildThreshold_Object = MibScalar
clMeshExcessiveMapChildThreshold = _ClMeshExcessiveMapChildThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 16),
    _ClMeshExcessiveMapChildThreshold_Type()
)
clMeshExcessiveMapChildThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshExcessiveMapChildThreshold.setStatus("current")


class _ClMeshHighSNRThresholdAbate_Type(Unsigned32):
    """Custom type clMeshHighSNRThresholdAbate based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 80),
    )


_ClMeshHighSNRThresholdAbate_Type.__name__ = "Unsigned32"
_ClMeshHighSNRThresholdAbate_Object = MibScalar
clMeshHighSNRThresholdAbate = _ClMeshHighSNRThresholdAbate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 17),
    _ClMeshHighSNRThresholdAbate_Type()
)
clMeshHighSNRThresholdAbate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshHighSNRThresholdAbate.setStatus("current")
if mibBuilder.loadTexts:
    clMeshHighSNRThresholdAbate.setUnits("db")


class _ClMeshHighSNRThresholdOnset_Type(Unsigned32):
    """Custom type clMeshHighSNRThresholdOnset based on Unsigned32"""
    defaultValue = 56

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 80),
    )


_ClMeshHighSNRThresholdOnset_Type.__name__ = "Unsigned32"
_ClMeshHighSNRThresholdOnset_Object = MibScalar
clMeshHighSNRThresholdOnset = _ClMeshHighSNRThresholdOnset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 18),
    _ClMeshHighSNRThresholdOnset_Type()
)
clMeshHighSNRThresholdOnset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshHighSNRThresholdOnset.setStatus("current")
if mibBuilder.loadTexts:
    clMeshHighSNRThresholdOnset.setUnits("db")


class _ClMeshPublicSafetyBackhaulGlobal_Type(TruthValue):
    """Custom type clMeshPublicSafetyBackhaulGlobal based on TruthValue"""
    defaultValue = 2


_ClMeshPublicSafetyBackhaulGlobal_Type.__name__ = "TruthValue"
_ClMeshPublicSafetyBackhaulGlobal_Object = MibScalar
clMeshPublicSafetyBackhaulGlobal = _ClMeshPublicSafetyBackhaulGlobal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 19),
    _ClMeshPublicSafetyBackhaulGlobal_Type()
)
clMeshPublicSafetyBackhaulGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshPublicSafetyBackhaulGlobal.setStatus("current")


class _ClMeshisAMSDUEnable_Type(TruthValue):
    """Custom type clMeshisAMSDUEnable based on TruthValue"""
    defaultValue = 2


_ClMeshisAMSDUEnable_Type.__name__ = "TruthValue"
_ClMeshisAMSDUEnable_Object = MibScalar
clMeshisAMSDUEnable = _ClMeshisAMSDUEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 20),
    _ClMeshisAMSDUEnable_Type()
)
clMeshisAMSDUEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshisAMSDUEnable.setStatus("current")


class _ClMeshIsIdsEnable_Type(TruthValue):
    """Custom type clMeshIsIdsEnable based on TruthValue"""
    defaultValue = 1


_ClMeshIsIdsEnable_Type.__name__ = "TruthValue"
_ClMeshIsIdsEnable_Object = MibScalar
clMeshIsIdsEnable = _ClMeshIsIdsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 21),
    _ClMeshIsIdsEnable_Type()
)
clMeshIsIdsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshIsIdsEnable.setStatus("current")


class _ClMeshIsDCAChannelsEnable_Type(TruthValue):
    """Custom type clMeshIsDCAChannelsEnable based on TruthValue"""
    defaultValue = 2


_ClMeshIsDCAChannelsEnable_Type.__name__ = "TruthValue"
_ClMeshIsDCAChannelsEnable_Object = MibScalar
clMeshIsDCAChannelsEnable = _ClMeshIsDCAChannelsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 22),
    _ClMeshIsDCAChannelsEnable_Type()
)
clMeshIsDCAChannelsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshIsDCAChannelsEnable.setStatus("current")


class _ClMeshIsExtendedUAEnable_Type(TruthValue):
    """Custom type clMeshIsExtendedUAEnable based on TruthValue"""
    defaultValue = 2


_ClMeshIsExtendedUAEnable_Type.__name__ = "TruthValue"
_ClMeshIsExtendedUAEnable_Object = MibScalar
clMeshIsExtendedUAEnable = _ClMeshIsExtendedUAEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 23),
    _ClMeshIsExtendedUAEnable_Type()
)
clMeshIsExtendedUAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshIsExtendedUAEnable.setStatus("current")


class _ClMeshIsBDomainChannelsEnable_Type(TruthValue):
    """Custom type clMeshIsBDomainChannelsEnable based on TruthValue"""
    defaultValue = 2


_ClMeshIsBDomainChannelsEnable_Type.__name__ = "TruthValue"
_ClMeshIsBDomainChannelsEnable_Object = MibScalar
clMeshIsBDomainChannelsEnable = _ClMeshIsBDomainChannelsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 24),
    _ClMeshIsBDomainChannelsEnable_Type()
)
clMeshIsBDomainChannelsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshIsBDomainChannelsEnable.setStatus("current")


class _ClMeshPskKeyProvisionEnable_Type(TruthValue):
    """Custom type clMeshPskKeyProvisionEnable based on TruthValue"""
    defaultValue = 2


_ClMeshPskKeyProvisionEnable_Type.__name__ = "TruthValue"
_ClMeshPskKeyProvisionEnable_Object = MibScalar
clMeshPskKeyProvisionEnable = _ClMeshPskKeyProvisionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 25),
    _ClMeshPskKeyProvisionEnable_Type()
)
clMeshPskKeyProvisionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshPskKeyProvisionEnable.setStatus("current")


class _ClMeshPskKeyWindowEnable_Type(TruthValue):
    """Custom type clMeshPskKeyWindowEnable based on TruthValue"""
    defaultValue = 2


_ClMeshPskKeyWindowEnable_Type.__name__ = "TruthValue"
_ClMeshPskKeyWindowEnable_Object = MibScalar
clMeshPskKeyWindowEnable = _ClMeshPskKeyWindowEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 26),
    _ClMeshPskKeyWindowEnable_Type()
)
clMeshPskKeyWindowEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshPskKeyWindowEnable.setStatus("current")


class _ClMeshEthenetBridgingVlanTransparent_Type(TruthValue):
    """Custom type clMeshEthenetBridgingVlanTransparent based on TruthValue"""
    defaultValue = 2


_ClMeshEthenetBridgingVlanTransparent_Type.__name__ = "TruthValue"
_ClMeshEthenetBridgingVlanTransparent_Object = MibScalar
clMeshEthenetBridgingVlanTransparent = _ClMeshEthenetBridgingVlanTransparent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 27),
    _ClMeshEthenetBridgingVlanTransparent_Type()
)
clMeshEthenetBridgingVlanTransparent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshEthenetBridgingVlanTransparent.setStatus("current")


class _ClMeshRAPDownlinkBackhaul_Type(Integer32):
    """Custom type clMeshRAPDownlinkBackhaul based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("slot0", 1),
          ("slot1", 2))
    )


_ClMeshRAPDownlinkBackhaul_Type.__name__ = "Integer32"
_ClMeshRAPDownlinkBackhaul_Object = MibScalar
clMeshRAPDownlinkBackhaul = _ClMeshRAPDownlinkBackhaul_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 28),
    _ClMeshRAPDownlinkBackhaul_Type()
)
clMeshRAPDownlinkBackhaul.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshRAPDownlinkBackhaul.setStatus("current")


class _ClMeshPskInUseKeyIndex_Type(Unsigned32):
    """Custom type clMeshPskInUseKeyIndex based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ClMeshPskInUseKeyIndex_Type.__name__ = "Unsigned32"
_ClMeshPskInUseKeyIndex_Object = MibScalar
clMeshPskInUseKeyIndex = _ClMeshPskInUseKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 29),
    _ClMeshPskInUseKeyIndex_Type()
)
clMeshPskInUseKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshPskInUseKeyIndex.setStatus("current")


class _ClMeshEthBridgingAllowBpdu_Type(TruthValue):
    """Custom type clMeshEthBridgingAllowBpdu based on TruthValue"""
    defaultValue = 2


_ClMeshEthBridgingAllowBpdu_Type.__name__ = "TruthValue"
_ClMeshEthBridgingAllowBpdu_Object = MibScalar
clMeshEthBridgingAllowBpdu = _ClMeshEthBridgingAllowBpdu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 30),
    _ClMeshEthBridgingAllowBpdu_Type()
)
clMeshEthBridgingAllowBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshEthBridgingAllowBpdu.setStatus("current")


class _ClMeshIsRapChannelSyncEnabled_Type(TruthValue):
    """Custom type clMeshIsRapChannelSyncEnabled based on TruthValue"""
    defaultValue = 2


_ClMeshIsRapChannelSyncEnabled_Type.__name__ = "TruthValue"
_ClMeshIsRapChannelSyncEnabled_Object = MibScalar
clMeshIsRapChannelSyncEnabled = _ClMeshIsRapChannelSyncEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 31),
    _ClMeshIsRapChannelSyncEnabled_Type()
)
clMeshIsRapChannelSyncEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshIsRapChannelSyncEnabled.setStatus("current")


class _ClMeshIsBackhaulRrmEnabled_Type(TruthValue):
    """Custom type clMeshIsBackhaulRrmEnabled based on TruthValue"""
    defaultValue = 2


_ClMeshIsBackhaulRrmEnabled_Type.__name__ = "TruthValue"
_ClMeshIsBackhaulRrmEnabled_Object = MibScalar
clMeshIsBackhaulRrmEnabled = _ClMeshIsBackhaulRrmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 32),
    _ClMeshIsBackhaulRrmEnabled_Type()
)
clMeshIsBackhaulRrmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshIsBackhaulRrmEnabled.setStatus("current")


class _ClMeshIsCacEnabled_Type(TruthValue):
    """Custom type clMeshIsCacEnabled based on TruthValue"""
    defaultValue = 2


_ClMeshIsCacEnabled_Type.__name__ = "TruthValue"
_ClMeshIsCacEnabled_Object = MibScalar
clMeshIsCacEnabled = _ClMeshIsCacEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 33),
    _ClMeshIsCacEnabled_Type()
)
clMeshIsCacEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshIsCacEnabled.setStatus("current")
_CiscoLwappMeshNeighborsStatus_ObjectIdentity = ObjectIdentity
ciscoLwappMeshNeighborsStatus = _CiscoLwappMeshNeighborsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3)
)
_ClMeshNeighborTable_Object = MibTable
clMeshNeighborTable = _ClMeshNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1)
)
if mibBuilder.loadTexts:
    clMeshNeighborTable.setStatus("current")
_ClMeshNeighborEntry_Object = MibTableRow
clMeshNeighborEntry = _ClMeshNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1, 1)
)
clMeshNeighborEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-MESH-MIB", "clMeshNeighborMacAddress"),
)
if mibBuilder.loadTexts:
    clMeshNeighborEntry.setStatus("current")
_ClMeshNeighborMacAddress_Type = MacAddress
_ClMeshNeighborMacAddress_Object = MibTableColumn
clMeshNeighborMacAddress = _ClMeshNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1, 1, 1),
    _ClMeshNeighborMacAddress_Type()
)
clMeshNeighborMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clMeshNeighborMacAddress.setStatus("current")


class _ClMeshNeighborType_Type(Bits):
    """Custom type clMeshNeighborType based on Bits"""
    namedValues = NamedValues(
        *(("parent", 0),
          ("neighbor", 1),
          ("excluded", 2),
          ("child", 3),
          ("beacon", 4),
          ("default", 5))
    )

_ClMeshNeighborType_Type.__name__ = "Bits"
_ClMeshNeighborType_Object = MibTableColumn
clMeshNeighborType = _ClMeshNeighborType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1, 1, 2),
    _ClMeshNeighborType_Type()
)
clMeshNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNeighborType.setStatus("current")
_ClMeshNeighborLinkSnr_Type = Integer32
_ClMeshNeighborLinkSnr_Object = MibTableColumn
clMeshNeighborLinkSnr = _ClMeshNeighborLinkSnr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1, 1, 3),
    _ClMeshNeighborLinkSnr_Type()
)
clMeshNeighborLinkSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNeighborLinkSnr.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNeighborLinkSnr.setUnits("dB")
_ClMeshNeighborChannel_Type = CLDot11Channel
_ClMeshNeighborChannel_Object = MibTableColumn
clMeshNeighborChannel = _ClMeshNeighborChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1, 1, 4),
    _ClMeshNeighborChannel_Type()
)
clMeshNeighborChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNeighborChannel.setStatus("current")
_ClMeshNeighborUpdate_Type = TimeStamp
_ClMeshNeighborUpdate_Object = MibTableColumn
clMeshNeighborUpdate = _ClMeshNeighborUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1, 1, 5),
    _ClMeshNeighborUpdate_Type()
)
clMeshNeighborUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNeighborUpdate.setStatus("current")
_ClMeshAtfStatsTable_Object = MibTable
clMeshAtfStatsTable = _ClMeshAtfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 2)
)
if mibBuilder.loadTexts:
    clMeshAtfStatsTable.setStatus("current")
_ClMeshAtfStatsEntry_Object = MibTableRow
clMeshAtfStatsEntry = _ClMeshAtfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 2, 1)
)
clMeshAtfStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-MESH-MIB", "clMeshNeighborMacAddress"),
)
if mibBuilder.loadTexts:
    clMeshAtfStatsEntry.setStatus("current")


class _ClMeshAtfAirtimeUsedInstantaneous_Type(Unsigned32):
    """Custom type clMeshAtfAirtimeUsedInstantaneous based on Unsigned32"""
    defaultValue = 0


_ClMeshAtfAirtimeUsedInstantaneous_Type.__name__ = "Unsigned32"
_ClMeshAtfAirtimeUsedInstantaneous_Object = MibTableColumn
clMeshAtfAirtimeUsedInstantaneous = _ClMeshAtfAirtimeUsedInstantaneous_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 2, 1, 1),
    _ClMeshAtfAirtimeUsedInstantaneous_Type()
)
clMeshAtfAirtimeUsedInstantaneous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshAtfAirtimeUsedInstantaneous.setStatus("current")
if mibBuilder.loadTexts:
    clMeshAtfAirtimeUsedInstantaneous.setUnits("Microseconds")


class _ClMeshAtfAirtimeUsedCumulative_Type(Unsigned64):
    """Custom type clMeshAtfAirtimeUsedCumulative based on Unsigned64"""
    defaultValue = 0


_ClMeshAtfAirtimeUsedCumulative_Type.__name__ = "Unsigned64"
_ClMeshAtfAirtimeUsedCumulative_Object = MibTableColumn
clMeshAtfAirtimeUsedCumulative = _ClMeshAtfAirtimeUsedCumulative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 2, 1, 2),
    _ClMeshAtfAirtimeUsedCumulative_Type()
)
clMeshAtfAirtimeUsedCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshAtfAirtimeUsedCumulative.setStatus("current")
if mibBuilder.loadTexts:
    clMeshAtfAirtimeUsedCumulative.setUnits("Microseconds")


class _ClMeshAtfFramesSentInstantaneous_Type(Unsigned32):
    """Custom type clMeshAtfFramesSentInstantaneous based on Unsigned32"""
    defaultValue = 0


_ClMeshAtfFramesSentInstantaneous_Type.__name__ = "Unsigned32"
_ClMeshAtfFramesSentInstantaneous_Object = MibTableColumn
clMeshAtfFramesSentInstantaneous = _ClMeshAtfFramesSentInstantaneous_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 2, 1, 3),
    _ClMeshAtfFramesSentInstantaneous_Type()
)
clMeshAtfFramesSentInstantaneous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshAtfFramesSentInstantaneous.setStatus("current")
if mibBuilder.loadTexts:
    clMeshAtfFramesSentInstantaneous.setUnits("bytes")


class _ClMeshAtfFramesSentCumulative_Type(Unsigned64):
    """Custom type clMeshAtfFramesSentCumulative based on Unsigned64"""
    defaultValue = 0


_ClMeshAtfFramesSentCumulative_Type.__name__ = "Unsigned64"
_ClMeshAtfFramesSentCumulative_Object = MibTableColumn
clMeshAtfFramesSentCumulative = _ClMeshAtfFramesSentCumulative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 2, 1, 4),
    _ClMeshAtfFramesSentCumulative_Type()
)
clMeshAtfFramesSentCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshAtfFramesSentCumulative.setStatus("current")
if mibBuilder.loadTexts:
    clMeshAtfFramesSentCumulative.setUnits("bytes")


class _ClMeshAtfFramesDroppedInstantaneous_Type(Unsigned32):
    """Custom type clMeshAtfFramesDroppedInstantaneous based on Unsigned32"""
    defaultValue = 0


_ClMeshAtfFramesDroppedInstantaneous_Type.__name__ = "Unsigned32"
_ClMeshAtfFramesDroppedInstantaneous_Object = MibTableColumn
clMeshAtfFramesDroppedInstantaneous = _ClMeshAtfFramesDroppedInstantaneous_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 2, 1, 5),
    _ClMeshAtfFramesDroppedInstantaneous_Type()
)
clMeshAtfFramesDroppedInstantaneous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshAtfFramesDroppedInstantaneous.setStatus("current")
if mibBuilder.loadTexts:
    clMeshAtfFramesDroppedInstantaneous.setUnits("bytes")


class _ClMeshAtfFramesDroppedCumulative_Type(Unsigned64):
    """Custom type clMeshAtfFramesDroppedCumulative based on Unsigned64"""
    defaultValue = 0


_ClMeshAtfFramesDroppedCumulative_Type.__name__ = "Unsigned64"
_ClMeshAtfFramesDroppedCumulative_Object = MibTableColumn
clMeshAtfFramesDroppedCumulative = _ClMeshAtfFramesDroppedCumulative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 2, 1, 6),
    _ClMeshAtfFramesDroppedCumulative_Type()
)
clMeshAtfFramesDroppedCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshAtfFramesDroppedCumulative.setStatus("current")
if mibBuilder.loadTexts:
    clMeshAtfFramesDroppedCumulative.setUnits("bytes")
_CiscoLwappMeshNotifControlConfig_ObjectIdentity = ObjectIdentity
ciscoLwappMeshNotifControlConfig = _CiscoLwappMeshNotifControlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4)
)


class _ClMeshAuthFailureNotifEnabled_Type(TruthValue):
    """Custom type clMeshAuthFailureNotifEnabled based on TruthValue"""
    defaultValue = 1


_ClMeshAuthFailureNotifEnabled_Type.__name__ = "TruthValue"
_ClMeshAuthFailureNotifEnabled_Object = MibScalar
clMeshAuthFailureNotifEnabled = _ClMeshAuthFailureNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 1),
    _ClMeshAuthFailureNotifEnabled_Type()
)
clMeshAuthFailureNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshAuthFailureNotifEnabled.setStatus("current")


class _ClMeshChildExcludedParentNotifEnabled_Type(TruthValue):
    """Custom type clMeshChildExcludedParentNotifEnabled based on TruthValue"""
    defaultValue = 1


_ClMeshChildExcludedParentNotifEnabled_Type.__name__ = "TruthValue"
_ClMeshChildExcludedParentNotifEnabled_Object = MibScalar
clMeshChildExcludedParentNotifEnabled = _ClMeshChildExcludedParentNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 2),
    _ClMeshChildExcludedParentNotifEnabled_Type()
)
clMeshChildExcludedParentNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshChildExcludedParentNotifEnabled.setStatus("current")


class _ClMeshParentChangeNotifEnabled_Type(TruthValue):
    """Custom type clMeshParentChangeNotifEnabled based on TruthValue"""
    defaultValue = 1


_ClMeshParentChangeNotifEnabled_Type.__name__ = "TruthValue"
_ClMeshParentChangeNotifEnabled_Object = MibScalar
clMeshParentChangeNotifEnabled = _ClMeshParentChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 3),
    _ClMeshParentChangeNotifEnabled_Type()
)
clMeshParentChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshParentChangeNotifEnabled.setStatus("current")


class _ClMeshChildMovedNotifEnabled_Type(TruthValue):
    """Custom type clMeshChildMovedNotifEnabled based on TruthValue"""
    defaultValue = 1


_ClMeshChildMovedNotifEnabled_Type.__name__ = "TruthValue"
_ClMeshChildMovedNotifEnabled_Object = MibScalar
clMeshChildMovedNotifEnabled = _ClMeshChildMovedNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 4),
    _ClMeshChildMovedNotifEnabled_Type()
)
clMeshChildMovedNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshChildMovedNotifEnabled.setStatus("current")


class _ClMeshExcessiveParentChangeNotifEnabled_Type(TruthValue):
    """Custom type clMeshExcessiveParentChangeNotifEnabled based on TruthValue"""
    defaultValue = 1


_ClMeshExcessiveParentChangeNotifEnabled_Type.__name__ = "TruthValue"
_ClMeshExcessiveParentChangeNotifEnabled_Object = MibScalar
clMeshExcessiveParentChangeNotifEnabled = _ClMeshExcessiveParentChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 5),
    _ClMeshExcessiveParentChangeNotifEnabled_Type()
)
clMeshExcessiveParentChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshExcessiveParentChangeNotifEnabled.setStatus("current")


class _ClMeshPoorSNRNotifEnabled_Type(TruthValue):
    """Custom type clMeshPoorSNRNotifEnabled based on TruthValue"""
    defaultValue = 1


_ClMeshPoorSNRNotifEnabled_Type.__name__ = "TruthValue"
_ClMeshPoorSNRNotifEnabled_Object = MibScalar
clMeshPoorSNRNotifEnabled = _ClMeshPoorSNRNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 6),
    _ClMeshPoorSNRNotifEnabled_Type()
)
clMeshPoorSNRNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshPoorSNRNotifEnabled.setStatus("current")


class _ClMeshConsoleLoginNotifEnabled_Type(TruthValue):
    """Custom type clMeshConsoleLoginNotifEnabled based on TruthValue"""
    defaultValue = 1


_ClMeshConsoleLoginNotifEnabled_Type.__name__ = "TruthValue"
_ClMeshConsoleLoginNotifEnabled_Object = MibScalar
clMeshConsoleLoginNotifEnabled = _ClMeshConsoleLoginNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 7),
    _ClMeshConsoleLoginNotifEnabled_Type()
)
clMeshConsoleLoginNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshConsoleLoginNotifEnabled.setStatus("current")


class _ClMeshDefaultBridgeGroupNameNotifEnabled_Type(TruthValue):
    """Custom type clMeshDefaultBridgeGroupNameNotifEnabled based on TruthValue"""
    defaultValue = 1


_ClMeshDefaultBridgeGroupNameNotifEnabled_Type.__name__ = "TruthValue"
_ClMeshDefaultBridgeGroupNameNotifEnabled_Object = MibScalar
clMeshDefaultBridgeGroupNameNotifEnabled = _ClMeshDefaultBridgeGroupNameNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 8),
    _ClMeshDefaultBridgeGroupNameNotifEnabled_Type()
)
clMeshDefaultBridgeGroupNameNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshDefaultBridgeGroupNameNotifEnabled.setStatus("current")


class _ClMeshExcessiveHopCountNotifEnabled_Type(TruthValue):
    """Custom type clMeshExcessiveHopCountNotifEnabled based on TruthValue"""
    defaultValue = 1


_ClMeshExcessiveHopCountNotifEnabled_Type.__name__ = "TruthValue"
_ClMeshExcessiveHopCountNotifEnabled_Object = MibScalar
clMeshExcessiveHopCountNotifEnabled = _ClMeshExcessiveHopCountNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 9),
    _ClMeshExcessiveHopCountNotifEnabled_Type()
)
clMeshExcessiveHopCountNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshExcessiveHopCountNotifEnabled.setStatus("current")


class _ClMeshExcessiveChildrenNotifEnabled_Type(TruthValue):
    """Custom type clMeshExcessiveChildrenNotifEnabled based on TruthValue"""
    defaultValue = 1


_ClMeshExcessiveChildrenNotifEnabled_Type.__name__ = "TruthValue"
_ClMeshExcessiveChildrenNotifEnabled_Object = MibScalar
clMeshExcessiveChildrenNotifEnabled = _ClMeshExcessiveChildrenNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 10),
    _ClMeshExcessiveChildrenNotifEnabled_Type()
)
clMeshExcessiveChildrenNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshExcessiveChildrenNotifEnabled.setStatus("current")


class _ClMeshHighSNRNotifEnabled_Type(TruthValue):
    """Custom type clMeshHighSNRNotifEnabled based on TruthValue"""
    defaultValue = 1


_ClMeshHighSNRNotifEnabled_Type.__name__ = "TruthValue"
_ClMeshHighSNRNotifEnabled_Object = MibScalar
clMeshHighSNRNotifEnabled = _ClMeshHighSNRNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 11),
    _ClMeshHighSNRNotifEnabled_Type()
)
clMeshHighSNRNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshHighSNRNotifEnabled.setStatus("current")
_CiscoLwappMeshMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMeshMIBNotifObjects = _CiscoLwappMeshMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 5)
)
_ClMeshNodeMacAddress_Type = MacAddress
_ClMeshNodeMacAddress_Object = MibScalar
clMeshNodeMacAddress = _ClMeshNodeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 5, 1),
    _ClMeshNodeMacAddress_Type()
)
clMeshNodeMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clMeshNodeMacAddress.setStatus("current")


class _ClMeshAuthFailureReason_Type(Integer32):
    """Custom type clMeshAuthFailureReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInMacFilterList", 1),
          ("securityFailure", 2))
    )


_ClMeshAuthFailureReason_Type.__name__ = "Integer32"
_ClMeshAuthFailureReason_Object = MibScalar
clMeshAuthFailureReason = _ClMeshAuthFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 5, 2),
    _ClMeshAuthFailureReason_Type()
)
clMeshAuthFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clMeshAuthFailureReason.setStatus("current")
_ClMeshPreviousParentMacAddress_Type = MacAddress
_ClMeshPreviousParentMacAddress_Object = MibScalar
clMeshPreviousParentMacAddress = _ClMeshPreviousParentMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 5, 3),
    _ClMeshPreviousParentMacAddress_Type()
)
clMeshPreviousParentMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clMeshPreviousParentMacAddress.setStatus("current")


class _ClMeshConsoleLoginStatus_Type(Integer32):
    """Custom type clMeshConsoleLoginStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failure", 2))
    )


_ClMeshConsoleLoginStatus_Type.__name__ = "Integer32"
_ClMeshConsoleLoginStatus_Object = MibScalar
clMeshConsoleLoginStatus = _ClMeshConsoleLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 5, 4),
    _ClMeshConsoleLoginStatus_Type()
)
clMeshConsoleLoginStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clMeshConsoleLoginStatus.setStatus("current")
_ClMeshNodePrevTemperatureState_Type = SnmpAdminString
_ClMeshNodePrevTemperatureState_Object = MibScalar
clMeshNodePrevTemperatureState = _ClMeshNodePrevTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 5, 5),
    _ClMeshNodePrevTemperatureState_Type()
)
clMeshNodePrevTemperatureState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clMeshNodePrevTemperatureState.setStatus("current")
_ClMeshNodeNewTemperatureState_Type = SnmpAdminString
_ClMeshNodeNewTemperatureState_Object = MibScalar
clMeshNodeNewTemperatureState = _ClMeshNodeNewTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 5, 6),
    _ClMeshNodeNewTemperatureState_Type()
)
clMeshNodeNewTemperatureState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clMeshNodeNewTemperatureState.setStatus("current")
_CiscoLwappMeshGpsObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMeshGpsObjects = _CiscoLwappMeshGpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 6)
)
_ClMeshGpsInfoTable_Object = MibTable
clMeshGpsInfoTable = _ClMeshGpsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 6, 1)
)
if mibBuilder.loadTexts:
    clMeshGpsInfoTable.setStatus("current")
_ClMeshGpsInfoEntry_Object = MibTableRow
clMeshGpsInfoEntry = _ClMeshGpsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 6, 1, 1)
)
clMeshGpsInfoEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    clMeshGpsInfoEntry.setStatus("current")
_ClMeshGpsLocationPresent_Type = TruthValue
_ClMeshGpsLocationPresent_Object = MibTableColumn
clMeshGpsLocationPresent = _ClMeshGpsLocationPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 6, 1, 1, 1),
    _ClMeshGpsLocationPresent_Type()
)
clMeshGpsLocationPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshGpsLocationPresent.setStatus("deprecated")
_ClMeshGpsLocationValid_Type = TruthValue
_ClMeshGpsLocationValid_Object = MibTableColumn
clMeshGpsLocationValid = _ClMeshGpsLocationValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 6, 1, 1, 2),
    _ClMeshGpsLocationValid_Type()
)
clMeshGpsLocationValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshGpsLocationValid.setStatus("deprecated")
_ClMeshGpsLatitude_Type = SnmpAdminString
_ClMeshGpsLatitude_Object = MibTableColumn
clMeshGpsLatitude = _ClMeshGpsLatitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 6, 1, 1, 3),
    _ClMeshGpsLatitude_Type()
)
clMeshGpsLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshGpsLatitude.setStatus("deprecated")
_ClMeshGpsLongitude_Type = SnmpAdminString
_ClMeshGpsLongitude_Object = MibTableColumn
clMeshGpsLongitude = _ClMeshGpsLongitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 6, 1, 1, 4),
    _ClMeshGpsLongitude_Type()
)
clMeshGpsLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshGpsLongitude.setStatus("deprecated")
_ClMeshGpsAltitude_Type = SnmpAdminString
_ClMeshGpsAltitude_Object = MibTableColumn
clMeshGpsAltitude = _ClMeshGpsAltitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 6, 1, 1, 5),
    _ClMeshGpsAltitude_Type()
)
clMeshGpsAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshGpsAltitude.setStatus("deprecated")
_ClMeshGpsCollectionTime_Type = TimeStamp
_ClMeshGpsCollectionTime_Object = MibTableColumn
clMeshGpsCollectionTime = _ClMeshGpsCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 6, 1, 1, 6),
    _ClMeshGpsCollectionTime_Type()
)
clMeshGpsCollectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshGpsCollectionTime.setStatus("deprecated")
_CiscoLwappMeshMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappMeshMIBConform = _CiscoLwappMeshMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2)
)
_CiscoLwappMeshMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappMeshMIBCompliances = _CiscoLwappMeshMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 1)
)
_CiscoLwappMeshMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappMeshMIBGroups = _CiscoLwappMeshMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2)
)

# Managed Objects groups

ciscoLwappMeshConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 1)
)
ciscoLwappMeshConfigGroup.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNodeRole"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeGroupName"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaul"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaulDataRate"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeEthernetBridge"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeEthernetLinkStatus"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodePublicSafetyBackhaul"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHeaterStatus"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeInternalTemp"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeType"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHops"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeRange"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshBackhaulClientAccess"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMacFilterList"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMeshNodeAuthFailureThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMeshChildAssociationFailuresThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMeshChildExcludedParentInterval"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshSNRThresholdAbate"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshSNRThresholdOnset"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshSNRCheckTimeInterval"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeInterval"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshBackgroundScan"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshAuthenticationMode"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshConfigGroup.setStatus("deprecated")

ciscoLwappMeshNeighborStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 2)
)
ciscoLwappMeshNeighborStatusGroup.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborType"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNeighborLinkSnr"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNeighborChannel"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNeighborUpdate"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshNeighborStatusGroup.setStatus("current")

ciscoLwappMeshNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 3)
)
ciscoLwappMeshNotifControlGroup.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshAuthFailureNotifEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshChildExcludedParentNotifEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshParentChangeNotifEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshChildMovedNotifEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeNotifEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPoorSNRNotifEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshConsoleLoginNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshNotifControlGroup.setStatus("current")

ciscoLwappMeshNotifObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 4)
)
ciscoLwappMeshNotifObjsGroup.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNodeMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshAuthFailureReason"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPreviousParentMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshConsoleLoginStatus"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodePrevTemperatureState"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeNewTemperatureState"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshNotifObjsGroup.setStatus("current")

ciscoLwappMeshConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 6)
)
ciscoLwappMeshConfigGroupSup1.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNodeRole"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeGroupName"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaul"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaulDataRate"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeEthernetBridge"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeEthernetLinkStatus"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHeaterStatus"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeInternalTemp"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeType"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHops"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeChildCount"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaulRadio"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeRange"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshBackhaulClientAccess"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMacFilterList"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMeshNodeAuthFailureThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMeshChildAssociationFailuresThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMeshChildExcludedParentInterval"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshSNRThresholdAbate"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshSNRThresholdOnset"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshHighSNRThresholdAbate"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshHighSNRThresholdOnset"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshSNRCheckTimeInterval"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeInterval"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshBackgroundScan"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshAuthenticationMode"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveHopCountThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveRapChildThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveMapChildThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPublicSafetyBackhaulGlobal"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshisAMSDUEnable"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshIsIdsEnable"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshIsDCAChannelsEnable"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshIsExtendedUAEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshConfigGroupSup1.setStatus("deprecated")

ciscoLwappMeshNotifControlGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 7)
)
ciscoLwappMeshNotifControlGroupSup1.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshHighSNRNotifEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshDefaultBridgeGroupNameNotifEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveHopCountNotifEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveChildrenNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshNotifControlGroupSup1.setStatus("current")

ciscoLwappMeshConfigGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 9)
)
ciscoLwappMeshConfigGroupSup2.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNodeRole"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeGroupName"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaul"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBHDataRate"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeEthernetBridge"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeEthernetLinkStatus"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHeaterStatus"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeInternalTemp"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeType"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHops"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeChildCount"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaulRadio"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeRange"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshBackhaulClientAccess"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMacFilterList"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMeshNodeAuthFailureThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMeshChildAssociationFailuresThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMeshChildExcludedParentInterval"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshSNRThresholdAbate"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshSNRThresholdOnset"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshHighSNRThresholdAbate"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshHighSNRThresholdOnset"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshSNRCheckTimeInterval"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeInterval"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshBackgroundScan"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshAuthenticationMode"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveHopCountThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveRapChildThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveMapChildThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPublicSafetyBackhaulGlobal"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshisAMSDUEnable"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshIsIdsEnable"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshIsDCAChannelsEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshConfigGroupSup2.setStatus("current")

ciscoLwappMeshAtfStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 10)
)
ciscoLwappMeshAtfStatusGroup.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshAtfAirtimeUsedInstantaneous"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshAtfAirtimeUsedCumulative"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshAtfFramesSentInstantaneous"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshAtfFramesSentCumulative"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshAtfFramesDroppedInstantaneous"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshAtfFramesDroppedCumulative"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshAtfStatusGroup.setStatus("current")

ciscoLwappMeshConfigGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 11)
)
ciscoLwappMeshConfigGroupRev3.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshIsExtendedUAEnable"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshIsBDomainChannelsEnable"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPskKeyProvisionEnable"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPskKeyWindowEnable"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshEthenetBridgingVlanTransparent"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshRAPDownlinkBackhaul"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshEthBridgingAllowBpdu"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshIsRapChannelSyncEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshIsBackhaulRrmEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshIsCacEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshConfigGroupRev3.setStatus("current")

ciscoLwappMeshPskConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 12)
)
ciscoLwappMeshPskConfigGroup.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshPskIndex"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPskKey"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPskTimeStamp"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPskKeyDesc"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPskRowStatus"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPskInUseKeyIndex"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshPskConfigGroup.setStatus("current")

ciscoLwappMeshProfileConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 13)
)
ciscoLwappMeshProfileConfigGroup.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "cLMeshProfileName"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDescr"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileASTools"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileAmsdu"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileBackgroundScan"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileCcnMode"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileUniversalAccess"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileEtherVlanTransparent"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileFullSectorDfs"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileIdsState"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileMulticastMode"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileRange"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileSecurityMode"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileConvergenceMethod"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileLscOnlyAuthentication"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileBridgeGroupName"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileBGNStrictmatch"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileEthernetBridging"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileBatteryState"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileAuthorizationMethod"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileAuthenticationMethod"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11bgBhaulRateType"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11bgBhaulRate"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11bgBhaulRateDot11nMcsIndex"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11aBhaulRateType"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11aBhaulRate"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11aBhaulRateDot11nMcsIndex"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11aBhaulRateDot11acMcsIndex"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11aBhaulRateDot11acSpatialStream"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshProfileRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshProfileConfigGroup.setStatus("deprecated")

ciscoLwappMeshProfileConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 14)
)
ciscoLwappMeshProfileConfigGroupRev1.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "cLMeshProfileName"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDescr"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileASTools"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileAmsdu"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileBackgroundScan"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileCcnMode"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileUniversalAccess"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileEtherVlanTransparent"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileFullSectorDfs"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileIdsState"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileMulticastMode"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileRange"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileSecurityMode"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileConvergenceMethod"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileLscOnlyAuthentication"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileBridgeGroupName"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileBGNStrictmatch"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileEthernetBridging"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileBatteryState"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileAuthorizationMethod"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileAuthenticationMethod"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11bgBhaulRateType"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11bgBhaulRate"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11bgBhaulRateDot11nMcsIndex"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11aBhaulRateType"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11aBhaulRate"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11aBhaulRateDot11nMcsIndex"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11aBhaulRateDot11acMcsIndex"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11aBhaulRateDot11acSpatialStream"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshProfileRowStatus"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11bgBhaulRateDot11axMcsIndex"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11bgBhaulRateDot11axSpatialStream"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11aBhaulRateDot11axMcsIndex"),
        ("CISCO-LWAPP-MESH-MIB", "cLMeshProfileDot11aBhaulRateDot11axSpatialStream"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBhaulDataRateDot11axSpatialStream"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshProfileConfigGroupRev1.setStatus("current")


# Notification objects

ciscoLwappMeshAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 1)
)
ciscoLwappMeshAuthFailure.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNodeMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshAuthFailureReason"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshAuthFailure.setStatus(
        "current"
    )

ciscoLwappMeshChildExcludedParent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 2)
)
ciscoLwappMeshChildExcludedParent.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPreviousParentMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshChildExcludedParent.setStatus(
        "current"
    )

ciscoLwappMeshParentChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 3)
)
ciscoLwappMeshParentChange.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPreviousParentMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshParentChange.setStatus(
        "current"
    )

ciscoLwappMeshChildMoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 4)
)
ciscoLwappMeshChildMoved.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborType"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshChildMoved.setStatus(
        "current"
    )

ciscoLwappMeshExcessiveParentChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 5)
)
ciscoLwappMeshExcessiveParentChange.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborType"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshExcessiveParentChange.setStatus(
        "current"
    )

ciscoLwappMeshOnsetSNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 6)
)
ciscoLwappMeshOnsetSNR.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborLinkSnr"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshOnsetSNR.setStatus(
        "current"
    )

ciscoLwappMeshAbateSNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 7)
)
ciscoLwappMeshAbateSNR.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborLinkSnr"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshAbateSNR.setStatus(
        "current"
    )

ciscoLwappMeshConsoleLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 8)
)
ciscoLwappMeshConsoleLogin.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNodeMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshConsoleLoginStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshConsoleLogin.setStatus(
        "current"
    )

ciscoLwappMeshDefaultBridgeGroupName = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 9)
)
ciscoLwappMeshDefaultBridgeGroupName.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshDefaultBridgeGroupName.setStatus(
        "current"
    )

ciscoLwappMeshExcessiveHopCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 10)
)
ciscoLwappMeshExcessiveHopCount.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHops"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshExcessiveHopCount.setStatus(
        "current"
    )

ciscoLwappMeshExcessiveChildren = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 11)
)
ciscoLwappMeshExcessiveChildren.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeRole"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeChildCount"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshExcessiveChildren.setStatus(
        "current"
    )

ciscoLwappMeshOnsetHighSNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 12)
)
ciscoLwappMeshOnsetHighSNR.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborLinkSnr"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshOnsetHighSNR.setStatus(
        "current"
    )

ciscoLwappMeshAbateHighSNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 13)
)
ciscoLwappMeshAbateHighSNR.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborLinkSnr"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshAbateHighSNR.setStatus(
        "current"
    )

ciscoLwappMeshTemperatureStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 14)
)
ciscoLwappMeshTemperatureStateChange.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNodeMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodePrevTemperatureState"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeNewTemperatureState"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshTemperatureStateChange.setStatus(
        "current"
    )

ciscoLwappMeshPskKeyAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 15)
)
ciscoLwappMeshPskKeyAuthFailure.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeMacAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshPskKeyAuthFailure.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappMeshNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 5)
)
ciscoLwappMeshNotifsGroup.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshAuthFailure"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshChildExcludedParent"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshParentChange"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshChildMoved"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshExcessiveParentChange"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshOnsetSNR"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshAbateSNR"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshConsoleLogin"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshNotifsGroup.setStatus(
        "current"
    )

ciscoLwappMeshNotifsGroupSup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 8)
)
ciscoLwappMeshNotifsGroupSup1.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshDefaultBridgeGroupName"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshExcessiveHopCount"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshExcessiveChildren"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshAbateHighSNR"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshOnsetHighSNR"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshNotifsGroupSup1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappMeshMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 1, 1)
)
ciscoLwappMeshMIBCompliance.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshConfigGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNeighborStatusGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifControlGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifObjsGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifsGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappMeshMIBComplianceR01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 1, 2)
)
ciscoLwappMeshMIBComplianceR01.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNeighborStatusGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifControlGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifObjsGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifsGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshConfigGroupSup1"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifControlGroupSup1"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifsGroupSup1"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshMIBComplianceR01.setStatus(
        "deprecated"
    )

ciscoLwappMeshMIBComplianceR02 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 1, 3)
)
ciscoLwappMeshMIBComplianceR02.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNeighborStatusGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifControlGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifObjsGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifsGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshConfigGroupSup2"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifControlGroupSup1"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifsGroupSup1"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshConfigGroupRev3"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshAtfStatusGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshPskConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshMIBComplianceR02.setStatus(
        "deprecated"
    )

ciscoLwappMeshMIBComplianceR03 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 1, 4)
)
ciscoLwappMeshMIBComplianceR03.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNeighborStatusGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifControlGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifObjsGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifsGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshConfigGroupSup2"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifControlGroupSup1"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifsGroupSup1"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshConfigGroupRev3"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshAtfStatusGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshPskConfigGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshProfileConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshMIBComplianceR03.setStatus(
        "deprecated"
    )

ciscoLwappMeshMIBComplianceR04 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 1, 5)
)
ciscoLwappMeshMIBComplianceR04.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNeighborStatusGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifControlGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifObjsGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifsGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshConfigGroupSup2"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifControlGroupSup1"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifsGroupSup1"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshConfigGroupRev3"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshAtfStatusGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshPskConfigGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshProfileConfigGroup"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshProfileConfigGroupRev1"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshMIBComplianceR04.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-MESH-MIB",
    **{"ciscoLwappMeshMIB": ciscoLwappMeshMIB,
       "ciscoLwappMeshMIBNotifs": ciscoLwappMeshMIBNotifs,
       "ciscoLwappMeshAuthFailure": ciscoLwappMeshAuthFailure,
       "ciscoLwappMeshChildExcludedParent": ciscoLwappMeshChildExcludedParent,
       "ciscoLwappMeshParentChange": ciscoLwappMeshParentChange,
       "ciscoLwappMeshChildMoved": ciscoLwappMeshChildMoved,
       "ciscoLwappMeshExcessiveParentChange": ciscoLwappMeshExcessiveParentChange,
       "ciscoLwappMeshOnsetSNR": ciscoLwappMeshOnsetSNR,
       "ciscoLwappMeshAbateSNR": ciscoLwappMeshAbateSNR,
       "ciscoLwappMeshConsoleLogin": ciscoLwappMeshConsoleLogin,
       "ciscoLwappMeshDefaultBridgeGroupName": ciscoLwappMeshDefaultBridgeGroupName,
       "ciscoLwappMeshExcessiveHopCount": ciscoLwappMeshExcessiveHopCount,
       "ciscoLwappMeshExcessiveChildren": ciscoLwappMeshExcessiveChildren,
       "ciscoLwappMeshOnsetHighSNR": ciscoLwappMeshOnsetHighSNR,
       "ciscoLwappMeshAbateHighSNR": ciscoLwappMeshAbateHighSNR,
       "ciscoLwappMeshTemperatureStateChange": ciscoLwappMeshTemperatureStateChange,
       "ciscoLwappMeshPskKeyAuthFailure": ciscoLwappMeshPskKeyAuthFailure,
       "ciscoLwappMeshMIBObjects": ciscoLwappMeshMIBObjects,
       "ciscoLwappMeshConfig": ciscoLwappMeshConfig,
       "clMeshNodeTable": clMeshNodeTable,
       "clMeshNodeEntry": clMeshNodeEntry,
       "clMeshNodeRole": clMeshNodeRole,
       "clMeshNodeGroupName": clMeshNodeGroupName,
       "clMeshNodeBackhaul": clMeshNodeBackhaul,
       "clMeshNodeBackhaulDataRate": clMeshNodeBackhaulDataRate,
       "clMeshNodeEthernetBridge": clMeshNodeEthernetBridge,
       "clMeshNodeEthernetLinkStatus": clMeshNodeEthernetLinkStatus,
       "clMeshNodePublicSafetyBackhaul": clMeshNodePublicSafetyBackhaul,
       "clMeshNodeParentMacAddress": clMeshNodeParentMacAddress,
       "clMeshNodeHeaterStatus": clMeshNodeHeaterStatus,
       "clMeshNodeInternalTemp": clMeshNodeInternalTemp,
       "clMeshNodeType": clMeshNodeType,
       "clMeshNodeHops": clMeshNodeHops,
       "clMeshNodeChildCount": clMeshNodeChildCount,
       "clMeshNodeBackhaulRadio": clMeshNodeBackhaulRadio,
       "clMeshNodeBHDataRate": clMeshNodeBHDataRate,
       "clMeshDaisyChainEnabled": clMeshDaisyChainEnabled,
       "clMeshPrefParentMacAddress": clMeshPrefParentMacAddress,
       "clMeshNodeBGNStrictMatch": clMeshNodeBGNStrictMatch,
       "clMeshNodeVlanEnabled": clMeshNodeVlanEnabled,
       "clMeshNodeNativeVlanId": clMeshNodeNativeVlanId,
       "clMeshNodePskKeyClear": clMeshNodePskKeyClear,
       "clMeshNodeRAPDownlinkBackhaul": clMeshNodeRAPDownlinkBackhaul,
       "clMeshNodeBlockChild": clMeshNodeBlockChild,
       "clMeshNodeBhaulDataRateType": clMeshNodeBhaulDataRateType,
       "clMeshNodeBhaulDataRate": clMeshNodeBhaulDataRate,
       "clMeshNodeBhaulDataRateMcsIndex": clMeshNodeBhaulDataRateMcsIndex,
       "clMeshNodeBhaulDataRateDot11acSpatialStream": clMeshNodeBhaulDataRateDot11acSpatialStream,
       "clMeshNodeBhaulDataRateDot11axSpatialStream": clMeshNodeBhaulDataRateDot11axSpatialStream,
       "clMeshPskTable": clMeshPskTable,
       "clMeshPskEntry": clMeshPskEntry,
       "clMeshPskIndex": clMeshPskIndex,
       "clMeshPskKey": clMeshPskKey,
       "clMeshPskTimeStamp": clMeshPskTimeStamp,
       "clMeshPskKeyDesc": clMeshPskKeyDesc,
       "clMeshPskRowStatus": clMeshPskRowStatus,
       "clMeshProfileTable": clMeshProfileTable,
       "clMeshProfileEntry": clMeshProfileEntry,
       "cLMeshProfileName": cLMeshProfileName,
       "cLMeshProfileDescr": cLMeshProfileDescr,
       "cLMeshProfileASTools": cLMeshProfileASTools,
       "cLMeshProfileAmsdu": cLMeshProfileAmsdu,
       "cLMeshProfileBackgroundScan": cLMeshProfileBackgroundScan,
       "cLMeshProfileCcnMode": cLMeshProfileCcnMode,
       "cLMeshProfileUniversalAccess": cLMeshProfileUniversalAccess,
       "cLMeshProfileEtherVlanTransparent": cLMeshProfileEtherVlanTransparent,
       "cLMeshProfileFullSectorDfs": cLMeshProfileFullSectorDfs,
       "cLMeshProfileIdsState": cLMeshProfileIdsState,
       "cLMeshProfileMulticastMode": cLMeshProfileMulticastMode,
       "cLMeshProfileRange": cLMeshProfileRange,
       "cLMeshProfileSecurityMode": cLMeshProfileSecurityMode,
       "cLMeshProfileConvergenceMethod": cLMeshProfileConvergenceMethod,
       "cLMeshProfileLscOnlyAuthentication": cLMeshProfileLscOnlyAuthentication,
       "cLMeshProfileBridgeGroupName": cLMeshProfileBridgeGroupName,
       "cLMeshProfileBGNStrictmatch": cLMeshProfileBGNStrictmatch,
       "cLMeshProfileEthernetBridging": cLMeshProfileEthernetBridging,
       "cLMeshProfileBatteryState": cLMeshProfileBatteryState,
       "cLMeshProfileAuthorizationMethod": cLMeshProfileAuthorizationMethod,
       "cLMeshProfileAuthenticationMethod": cLMeshProfileAuthenticationMethod,
       "cLMeshProfileDot11bgBhaulRateType": cLMeshProfileDot11bgBhaulRateType,
       "cLMeshProfileDot11bgBhaulRate": cLMeshProfileDot11bgBhaulRate,
       "cLMeshProfileDot11bgBhaulRateDot11nMcsIndex": cLMeshProfileDot11bgBhaulRateDot11nMcsIndex,
       "cLMeshProfileDot11aBhaulRateType": cLMeshProfileDot11aBhaulRateType,
       "cLMeshProfileDot11aBhaulRate": cLMeshProfileDot11aBhaulRate,
       "cLMeshProfileDot11aBhaulRateDot11nMcsIndex": cLMeshProfileDot11aBhaulRateDot11nMcsIndex,
       "cLMeshProfileDot11aBhaulRateDot11acMcsIndex": cLMeshProfileDot11aBhaulRateDot11acMcsIndex,
       "cLMeshProfileDot11aBhaulRateDot11acSpatialStream": cLMeshProfileDot11aBhaulRateDot11acSpatialStream,
       "clMeshProfileRowStatus": clMeshProfileRowStatus,
       "cLMeshProfileDot11bgBhaulRateDot11axMcsIndex": cLMeshProfileDot11bgBhaulRateDot11axMcsIndex,
       "cLMeshProfileDot11bgBhaulRateDot11axSpatialStream": cLMeshProfileDot11bgBhaulRateDot11axSpatialStream,
       "cLMeshProfileDot11aBhaulRateDot11axMcsIndex": cLMeshProfileDot11aBhaulRateDot11axMcsIndex,
       "cLMeshProfileDot11aBhaulRateDot11axSpatialStream": cLMeshProfileDot11aBhaulRateDot11axSpatialStream,
       "ciscoLwappMeshGlobalConfig": ciscoLwappMeshGlobalConfig,
       "clMeshNodeRange": clMeshNodeRange,
       "clMeshBackhaulClientAccess": clMeshBackhaulClientAccess,
       "clMeshMacFilterList": clMeshMacFilterList,
       "clMeshMeshNodeAuthFailureThreshold": clMeshMeshNodeAuthFailureThreshold,
       "clMeshMeshChildAssociationFailuresThreshold": clMeshMeshChildAssociationFailuresThreshold,
       "clMeshMeshChildExcludedParentInterval": clMeshMeshChildExcludedParentInterval,
       "clMeshSNRThresholdAbate": clMeshSNRThresholdAbate,
       "clMeshSNRThresholdOnset": clMeshSNRThresholdOnset,
       "clMeshSNRCheckTimeInterval": clMeshSNRCheckTimeInterval,
       "clMeshExcessiveParentChangeThreshold": clMeshExcessiveParentChangeThreshold,
       "clMeshExcessiveParentChangeInterval": clMeshExcessiveParentChangeInterval,
       "clMeshBackgroundScan": clMeshBackgroundScan,
       "clMeshAuthenticationMode": clMeshAuthenticationMode,
       "clMeshExcessiveHopCountThreshold": clMeshExcessiveHopCountThreshold,
       "clMeshExcessiveRapChildThreshold": clMeshExcessiveRapChildThreshold,
       "clMeshExcessiveMapChildThreshold": clMeshExcessiveMapChildThreshold,
       "clMeshHighSNRThresholdAbate": clMeshHighSNRThresholdAbate,
       "clMeshHighSNRThresholdOnset": clMeshHighSNRThresholdOnset,
       "clMeshPublicSafetyBackhaulGlobal": clMeshPublicSafetyBackhaulGlobal,
       "clMeshisAMSDUEnable": clMeshisAMSDUEnable,
       "clMeshIsIdsEnable": clMeshIsIdsEnable,
       "clMeshIsDCAChannelsEnable": clMeshIsDCAChannelsEnable,
       "clMeshIsExtendedUAEnable": clMeshIsExtendedUAEnable,
       "clMeshIsBDomainChannelsEnable": clMeshIsBDomainChannelsEnable,
       "clMeshPskKeyProvisionEnable": clMeshPskKeyProvisionEnable,
       "clMeshPskKeyWindowEnable": clMeshPskKeyWindowEnable,
       "clMeshEthenetBridgingVlanTransparent": clMeshEthenetBridgingVlanTransparent,
       "clMeshRAPDownlinkBackhaul": clMeshRAPDownlinkBackhaul,
       "clMeshPskInUseKeyIndex": clMeshPskInUseKeyIndex,
       "clMeshEthBridgingAllowBpdu": clMeshEthBridgingAllowBpdu,
       "clMeshIsRapChannelSyncEnabled": clMeshIsRapChannelSyncEnabled,
       "clMeshIsBackhaulRrmEnabled": clMeshIsBackhaulRrmEnabled,
       "clMeshIsCacEnabled": clMeshIsCacEnabled,
       "ciscoLwappMeshNeighborsStatus": ciscoLwappMeshNeighborsStatus,
       "clMeshNeighborTable": clMeshNeighborTable,
       "clMeshNeighborEntry": clMeshNeighborEntry,
       "clMeshNeighborMacAddress": clMeshNeighborMacAddress,
       "clMeshNeighborType": clMeshNeighborType,
       "clMeshNeighborLinkSnr": clMeshNeighborLinkSnr,
       "clMeshNeighborChannel": clMeshNeighborChannel,
       "clMeshNeighborUpdate": clMeshNeighborUpdate,
       "clMeshAtfStatsTable": clMeshAtfStatsTable,
       "clMeshAtfStatsEntry": clMeshAtfStatsEntry,
       "clMeshAtfAirtimeUsedInstantaneous": clMeshAtfAirtimeUsedInstantaneous,
       "clMeshAtfAirtimeUsedCumulative": clMeshAtfAirtimeUsedCumulative,
       "clMeshAtfFramesSentInstantaneous": clMeshAtfFramesSentInstantaneous,
       "clMeshAtfFramesSentCumulative": clMeshAtfFramesSentCumulative,
       "clMeshAtfFramesDroppedInstantaneous": clMeshAtfFramesDroppedInstantaneous,
       "clMeshAtfFramesDroppedCumulative": clMeshAtfFramesDroppedCumulative,
       "ciscoLwappMeshNotifControlConfig": ciscoLwappMeshNotifControlConfig,
       "clMeshAuthFailureNotifEnabled": clMeshAuthFailureNotifEnabled,
       "clMeshChildExcludedParentNotifEnabled": clMeshChildExcludedParentNotifEnabled,
       "clMeshParentChangeNotifEnabled": clMeshParentChangeNotifEnabled,
       "clMeshChildMovedNotifEnabled": clMeshChildMovedNotifEnabled,
       "clMeshExcessiveParentChangeNotifEnabled": clMeshExcessiveParentChangeNotifEnabled,
       "clMeshPoorSNRNotifEnabled": clMeshPoorSNRNotifEnabled,
       "clMeshConsoleLoginNotifEnabled": clMeshConsoleLoginNotifEnabled,
       "clMeshDefaultBridgeGroupNameNotifEnabled": clMeshDefaultBridgeGroupNameNotifEnabled,
       "clMeshExcessiveHopCountNotifEnabled": clMeshExcessiveHopCountNotifEnabled,
       "clMeshExcessiveChildrenNotifEnabled": clMeshExcessiveChildrenNotifEnabled,
       "clMeshHighSNRNotifEnabled": clMeshHighSNRNotifEnabled,
       "ciscoLwappMeshMIBNotifObjects": ciscoLwappMeshMIBNotifObjects,
       "clMeshNodeMacAddress": clMeshNodeMacAddress,
       "clMeshAuthFailureReason": clMeshAuthFailureReason,
       "clMeshPreviousParentMacAddress": clMeshPreviousParentMacAddress,
       "clMeshConsoleLoginStatus": clMeshConsoleLoginStatus,
       "clMeshNodePrevTemperatureState": clMeshNodePrevTemperatureState,
       "clMeshNodeNewTemperatureState": clMeshNodeNewTemperatureState,
       "ciscoLwappMeshGpsObjects": ciscoLwappMeshGpsObjects,
       "clMeshGpsInfoTable": clMeshGpsInfoTable,
       "clMeshGpsInfoEntry": clMeshGpsInfoEntry,
       "clMeshGpsLocationPresent": clMeshGpsLocationPresent,
       "clMeshGpsLocationValid": clMeshGpsLocationValid,
       "clMeshGpsLatitude": clMeshGpsLatitude,
       "clMeshGpsLongitude": clMeshGpsLongitude,
       "clMeshGpsAltitude": clMeshGpsAltitude,
       "clMeshGpsCollectionTime": clMeshGpsCollectionTime,
       "ciscoLwappMeshMIBConform": ciscoLwappMeshMIBConform,
       "ciscoLwappMeshMIBCompliances": ciscoLwappMeshMIBCompliances,
       "ciscoLwappMeshMIBCompliance": ciscoLwappMeshMIBCompliance,
       "ciscoLwappMeshMIBComplianceR01": ciscoLwappMeshMIBComplianceR01,
       "ciscoLwappMeshMIBComplianceR02": ciscoLwappMeshMIBComplianceR02,
       "ciscoLwappMeshMIBComplianceR03": ciscoLwappMeshMIBComplianceR03,
       "ciscoLwappMeshMIBComplianceR04": ciscoLwappMeshMIBComplianceR04,
       "ciscoLwappMeshMIBGroups": ciscoLwappMeshMIBGroups,
       "ciscoLwappMeshConfigGroup": ciscoLwappMeshConfigGroup,
       "ciscoLwappMeshNeighborStatusGroup": ciscoLwappMeshNeighborStatusGroup,
       "ciscoLwappMeshNotifControlGroup": ciscoLwappMeshNotifControlGroup,
       "ciscoLwappMeshNotifObjsGroup": ciscoLwappMeshNotifObjsGroup,
       "ciscoLwappMeshNotifsGroup": ciscoLwappMeshNotifsGroup,
       "ciscoLwappMeshConfigGroupSup1": ciscoLwappMeshConfigGroupSup1,
       "ciscoLwappMeshNotifControlGroupSup1": ciscoLwappMeshNotifControlGroupSup1,
       "ciscoLwappMeshNotifsGroupSup1": ciscoLwappMeshNotifsGroupSup1,
       "ciscoLwappMeshConfigGroupSup2": ciscoLwappMeshConfigGroupSup2,
       "ciscoLwappMeshAtfStatusGroup": ciscoLwappMeshAtfStatusGroup,
       "ciscoLwappMeshConfigGroupRev3": ciscoLwappMeshConfigGroupRev3,
       "ciscoLwappMeshPskConfigGroup": ciscoLwappMeshPskConfigGroup,
       "ciscoLwappMeshProfileConfigGroup": ciscoLwappMeshProfileConfigGroup,
       "ciscoLwappMeshProfileConfigGroupRev1": ciscoLwappMeshProfileConfigGroupRev1}
)
