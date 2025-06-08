# SNMP MIB module (TROPIC-L1SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-L1SERVICE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:12 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ipCidrRouteEntry,) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "ipCidrRouteEntry")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tnL1ServiceMIB,
 tnServiceModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnL1ServiceMIB",
    "tnServiceModules")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")

(AluWdmEnabledDisabled,
 AluWdmTypeOfNetIfOperation,
 TnApsGroupId,
 TnPerHopBehaviourType,
 TropicChannelIndexType,
 TropicPortIndexType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmEnabledDisabled",
    "AluWdmTypeOfNetIfOperation",
    "TnApsGroupId",
    "TnPerHopBehaviourType",
    "TropicChannelIndexType",
    "TropicPortIndexType")


# MODULE-IDENTITY

tnL1ServiceMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tnL1ServiceMibModule.setRevisions(
        ("2008-03-06 12:00",
         "2008-05-29 12:00",
         "2008-07-25 12:00",
         "2008-08-22 12:00",
         "2008-09-04 12:00",
         "2008-09-09 12:00",
         "2008-10-16 12:00",
         "2009-02-25 12:00",
         "2009-02-26 12:00",
         "2009-02-27 12:00",
         "2009-03-03 12:00",
         "2009-06-04 12:00",
         "2009-07-28 12:00",
         "2009-08-21 12:00",
         "2009-08-24 12:00",
         "2009-08-28 12:00",
         "2010-01-29 12:00",
         "2010-02-09 12:00",
         "2010-06-10 12:00",
         "2010-10-18 12:00",
         "2010-12-14 12:00",
         "2011-02-09 12:00",
         "2011-04-25 12:00",
         "2011-05-23 12:00",
         "2012-11-12 12:00",
         "2013-08-14 12:00",
         "2013-09-04 12:00",
         "2013-12-05 12:00",
         "2014-02-26 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ApsK1K2(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2



class TropicProtectionLevel(TextualConvention, Integer32):
    status = "current"
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
        *(("unprotected", 1),
          ("oneForOne", 2),
          ("onePlusOne", 3),
          ("onePlusOneOpticalSplitter", 4),
          ("onePlusOneESNCP", 5))
    )



class TropicLinkAdminStateType(TextualConvention, Integer32):
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
        *(("enabled", 1),
          ("disabled", 2),
          ("testing", 3),
          ("locked", 4))
    )



class TropicLinkOperationalStateType(TextualConvention, Integer32):
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4))
    )



class TropicOspfAdjacencyStateType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("init", 2),
          ("twoWay", 3),
          ("exchangeStart", 4),
          ("exchange", 5),
          ("loading", 6),
          ("full", 7))
    )



# MIB Managed Objects in the order of their OIDs

_TnL1ServiceConf_ObjectIdentity = ObjectIdentity
tnL1ServiceConf = _TnL1ServiceConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1)
)
_TnL1ServiceGroups_ObjectIdentity = ObjectIdentity
tnL1ServiceGroups = _TnL1ServiceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1)
)
_TnL1ServiceCompliances_ObjectIdentity = ObjectIdentity
tnL1ServiceCompliances = _TnL1ServiceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 2)
)
_TnL1ServiceObjs_ObjectIdentity = ObjectIdentity
tnL1ServiceObjs = _TnL1ServiceObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2)
)
_TnControlNetworkLink_ObjectIdentity = ObjectIdentity
tnControlNetworkLink = _TnControlNetworkLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1)
)
_TnControlNetworkLinkTable_Object = MibTable
tnControlNetworkLinkTable = _TnControlNetworkLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnControlNetworkLinkTable.setStatus("current")
_TnControlNetworkLinkEntry_Object = MibTableRow
tnControlNetworkLinkEntry = _TnControlNetworkLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1)
)
tnControlNetworkLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnControlNetworkLinkEntry.setStatus("current")


class _TnCNLinkDescr_Type(SnmpAdminString):
    """Custom type tnCNLinkDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnCNLinkDescr_Type.__name__ = "SnmpAdminString"
_TnCNLinkDescr_Object = MibTableColumn
tnCNLinkDescr = _TnCNLinkDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 1),
    _TnCNLinkDescr_Type()
)
tnCNLinkDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDescr.setStatus("current")


class _TnCNLinkAdminStatus_Type(TropicLinkAdminStateType):
    """Custom type tnCNLinkAdminStatus based on TropicLinkAdminStateType"""
    defaultValue = 1


_TnCNLinkAdminStatus_Type.__name__ = "TropicLinkAdminStateType"
_TnCNLinkAdminStatus_Object = MibTableColumn
tnCNLinkAdminStatus = _TnCNLinkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 2),
    _TnCNLinkAdminStatus_Type()
)
tnCNLinkAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkAdminStatus.setStatus("current")
_TnCNLinkOperStatus_Type = TropicLinkOperationalStateType
_TnCNLinkOperStatus_Object = MibTableColumn
tnCNLinkOperStatus = _TnCNLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 3),
    _TnCNLinkOperStatus_Type()
)
tnCNLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkOperStatus.setStatus("current")
_TnCNLinkPhysicalIfIndex_Type = InterfaceIndex
_TnCNLinkPhysicalIfIndex_Object = MibTableColumn
tnCNLinkPhysicalIfIndex = _TnCNLinkPhysicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 5),
    _TnCNLinkPhysicalIfIndex_Type()
)
tnCNLinkPhysicalIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkPhysicalIfIndex.setStatus("current")
_TnCNLinkIpAddress_Type = IpAddress
_TnCNLinkIpAddress_Object = MibTableColumn
tnCNLinkIpAddress = _TnCNLinkIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 7),
    _TnCNLinkIpAddress_Type()
)
tnCNLinkIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkIpAddress.setStatus("current")
_TnCNLinkSubnetMask_Type = IpAddress
_TnCNLinkSubnetMask_Object = MibTableColumn
tnCNLinkSubnetMask = _TnCNLinkSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 8),
    _TnCNLinkSubnetMask_Type()
)
tnCNLinkSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkSubnetMask.setStatus("current")


class _TnCNLinkHelloInterval_Type(Unsigned32):
    """Custom type tnCNLinkHelloInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnCNLinkHelloInterval_Type.__name__ = "Unsigned32"
_TnCNLinkHelloInterval_Object = MibTableColumn
tnCNLinkHelloInterval = _TnCNLinkHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 14),
    _TnCNLinkHelloInterval_Type()
)
tnCNLinkHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnCNLinkHelloInterval.setUnits("seconds")


class _TnCNLinkRtrDeadInterval_Type(Unsigned32):
    """Custom type tnCNLinkRtrDeadInterval based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TnCNLinkRtrDeadInterval_Type.__name__ = "Unsigned32"
_TnCNLinkRtrDeadInterval_Object = MibTableColumn
tnCNLinkRtrDeadInterval = _TnCNLinkRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 15),
    _TnCNLinkRtrDeadInterval_Type()
)
tnCNLinkRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnCNLinkRtrDeadInterval.setUnits("seconds")
_TnCNLinkTeMetric_Type = Unsigned32
_TnCNLinkTeMetric_Object = MibTableColumn
tnCNLinkTeMetric = _TnCNLinkTeMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 22),
    _TnCNLinkTeMetric_Type()
)
tnCNLinkTeMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkTeMetric.setStatus("current")


class _TnCNLinkOspfRoutingState_Type(Integer32):
    """Custom type tnCNLinkOspfRoutingState based on Integer32"""
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
        *(("disable", 1),
          ("enable", 2),
          ("redistribute", 3))
    )


_TnCNLinkOspfRoutingState_Type.__name__ = "Integer32"
_TnCNLinkOspfRoutingState_Object = MibTableColumn
tnCNLinkOspfRoutingState = _TnCNLinkOspfRoutingState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 31),
    _TnCNLinkOspfRoutingState_Type()
)
tnCNLinkOspfRoutingState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOspfRoutingState.setStatus("current")


class _TnCNLinkConfigIfType_Type(Integer32):
    """Custom type tnCNLinkConfigIfType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 1),
          ("broadcast", 2),
          ("nonBroadcastMultipleAccess", 3),
          ("pointToPoint", 4),
          ("virtual", 5),
          ("pointToMultipoint", 6))
    )


_TnCNLinkConfigIfType_Type.__name__ = "Integer32"
_TnCNLinkConfigIfType_Object = MibTableColumn
tnCNLinkConfigIfType = _TnCNLinkConfigIfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 32),
    _TnCNLinkConfigIfType_Type()
)
tnCNLinkConfigIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkConfigIfType.setStatus("current")


class _TnCNLinkConfigRtrPriority_Type(Unsigned32):
    """Custom type tnCNLinkConfigRtrPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnCNLinkConfigRtrPriority_Type.__name__ = "Unsigned32"
_TnCNLinkConfigRtrPriority_Object = MibTableColumn
tnCNLinkConfigRtrPriority = _TnCNLinkConfigRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 33),
    _TnCNLinkConfigRtrPriority_Type()
)
tnCNLinkConfigRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkConfigRtrPriority.setStatus("current")


class _TnCNLinkEquipOperStatus_Type(TropicLinkOperationalStateType):
    """Custom type tnCNLinkEquipOperStatus based on TropicLinkOperationalStateType"""
    defaultValue = 2


_TnCNLinkEquipOperStatus_Type.__name__ = "TropicLinkOperationalStateType"
_TnCNLinkEquipOperStatus_Object = MibTableColumn
tnCNLinkEquipOperStatus = _TnCNLinkEquipOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 34),
    _TnCNLinkEquipOperStatus_Type()
)
tnCNLinkEquipOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkEquipOperStatus.setStatus("current")
_TnCNLinkDhcpEnabled_Type = TruthValue
_TnCNLinkDhcpEnabled_Object = MibTableColumn
tnCNLinkDhcpEnabled = _TnCNLinkDhcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 35),
    _TnCNLinkDhcpEnabled_Type()
)
tnCNLinkDhcpEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDhcpEnabled.setStatus("current")


class _TnCNLinkSpeed_Type(Integer32):
    """Custom type tnCNLinkSpeed based on Integer32"""
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
        *(("auto", 1),
          ("rate10Mbps", 2),
          ("rate100Mbps", 3))
    )


_TnCNLinkSpeed_Type.__name__ = "Integer32"
_TnCNLinkSpeed_Object = MibTableColumn
tnCNLinkSpeed = _TnCNLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 36),
    _TnCNLinkSpeed_Type()
)
tnCNLinkSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkSpeed.setStatus("current")


class _TnCNLinkDuplex_Type(Integer32):
    """Custom type tnCNLinkDuplex based on Integer32"""
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
        *(("auto", 1),
          ("half", 2),
          ("full", 3))
    )


_TnCNLinkDuplex_Type.__name__ = "Integer32"
_TnCNLinkDuplex_Object = MibTableColumn
tnCNLinkDuplex = _TnCNLinkDuplex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 37),
    _TnCNLinkDuplex_Type()
)
tnCNLinkDuplex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDuplex.setStatus("current")


class _TnCNLinkProxyArp_Type(TruthValue):
    """Custom type tnCNLinkProxyArp based on TruthValue"""
    defaultValue = 2


_TnCNLinkProxyArp_Type.__name__ = "TruthValue"
_TnCNLinkProxyArp_Object = MibTableColumn
tnCNLinkProxyArp = _TnCNLinkProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 38),
    _TnCNLinkProxyArp_Type()
)
tnCNLinkProxyArp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkProxyArp.setStatus("current")


class _TnCNLinkDHCPServer_Type(TruthValue):
    """Custom type tnCNLinkDHCPServer based on TruthValue"""
    defaultValue = 1


_TnCNLinkDHCPServer_Type.__name__ = "TruthValue"
_TnCNLinkDHCPServer_Object = MibTableColumn
tnCNLinkDHCPServer = _TnCNLinkDHCPServer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 39),
    _TnCNLinkDHCPServer_Type()
)
tnCNLinkDHCPServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDHCPServer.setStatus("current")


class _TnCNLinkDHCPRange_Type(Unsigned32):
    """Custom type tnCNLinkDHCPRange based on Unsigned32"""
    defaultValue = 1


_TnCNLinkDHCPRange_Type.__name__ = "Unsigned32"
_TnCNLinkDHCPRange_Object = MibTableColumn
tnCNLinkDHCPRange = _TnCNLinkDHCPRange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 40),
    _TnCNLinkDHCPRange_Type()
)
tnCNLinkDHCPRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDHCPRange.setStatus("current")


class _TnCNLinkAdjState_Type(TropicOspfAdjacencyStateType):
    """Custom type tnCNLinkAdjState based on TropicOspfAdjacencyStateType"""
    defaultValue = 1


_TnCNLinkAdjState_Type.__name__ = "TropicOspfAdjacencyStateType"
_TnCNLinkAdjState_Object = MibTableColumn
tnCNLinkAdjState = _TnCNLinkAdjState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 41),
    _TnCNLinkAdjState_Type()
)
tnCNLinkAdjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkAdjState.setStatus("current")


class _TnCNLinkOscMode_Type(Integer32):
    """Custom type tnCNLinkOscMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oc3stm1", 1),
          ("base100FX", 2))
    )


_TnCNLinkOscMode_Type.__name__ = "Integer32"
_TnCNLinkOscMode_Object = MibTableColumn
tnCNLinkOscMode = _TnCNLinkOscMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 42),
    _TnCNLinkOscMode_Type()
)
tnCNLinkOscMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOscMode.setStatus("current")


class _TnCNLinkDHCPDfltGtwy_Type(TruthValue):
    """Custom type tnCNLinkDHCPDfltGtwy based on TruthValue"""
    defaultValue = 1


_TnCNLinkDHCPDfltGtwy_Type.__name__ = "TruthValue"
_TnCNLinkDHCPDfltGtwy_Object = MibTableColumn
tnCNLinkDHCPDfltGtwy = _TnCNLinkDHCPDfltGtwy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 43),
    _TnCNLinkDHCPDfltGtwy_Type()
)
tnCNLinkDHCPDfltGtwy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDHCPDfltGtwy.setStatus("current")


class _TnCNLinkCitAutoStateCtrl_Type(TruthValue):
    """Custom type tnCNLinkCitAutoStateCtrl based on TruthValue"""
    defaultValue = 2


_TnCNLinkCitAutoStateCtrl_Type.__name__ = "TruthValue"
_TnCNLinkCitAutoStateCtrl_Object = MibTableColumn
tnCNLinkCitAutoStateCtrl = _TnCNLinkCitAutoStateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 44),
    _TnCNLinkCitAutoStateCtrl_Type()
)
tnCNLinkCitAutoStateCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkCitAutoStateCtrl.setStatus("current")
_TnCNLinkAutoStateSourceIP_Type = IpAddress
_TnCNLinkAutoStateSourceIP_Object = MibTableColumn
tnCNLinkAutoStateSourceIP = _TnCNLinkAutoStateSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 45),
    _TnCNLinkAutoStateSourceIP_Type()
)
tnCNLinkAutoStateSourceIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkAutoStateSourceIP.setStatus("current")


class _TnCNLinkSourceLossCount_Type(Unsigned32):
    """Custom type tnCNLinkSourceLossCount based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10000),
    )


_TnCNLinkSourceLossCount_Type.__name__ = "Unsigned32"
_TnCNLinkSourceLossCount_Object = MibTableColumn
tnCNLinkSourceLossCount = _TnCNLinkSourceLossCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 46),
    _TnCNLinkSourceLossCount_Type()
)
tnCNLinkSourceLossCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkSourceLossCount.setStatus("current")


class _TnCNLinkSourceIPCheckInterval_Type(Unsigned32):
    """Custom type tnCNLinkSourceIPCheckInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 7200),
    )


_TnCNLinkSourceIPCheckInterval_Type.__name__ = "Unsigned32"
_TnCNLinkSourceIPCheckInterval_Object = MibTableColumn
tnCNLinkSourceIPCheckInterval = _TnCNLinkSourceIPCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 47),
    _TnCNLinkSourceIPCheckInterval_Type()
)
tnCNLinkSourceIPCheckInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkSourceIPCheckInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnCNLinkSourceIPCheckInterval.setUnits("seconds")


class _TnCNLinkOspfAuthentType_Type(Integer32):
    """Custom type tnCNLinkOspfAuthentType based on Integer32"""
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
        *(("none", 1),
          ("simple", 2),
          ("md5", 3))
    )


_TnCNLinkOspfAuthentType_Type.__name__ = "Integer32"
_TnCNLinkOspfAuthentType_Object = MibTableColumn
tnCNLinkOspfAuthentType = _TnCNLinkOspfAuthentType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 48),
    _TnCNLinkOspfAuthentType_Type()
)
tnCNLinkOspfAuthentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOspfAuthentType.setStatus("current")


class _TnCNLinkOspfAuthKey_Type(SnmpAdminString):
    """Custom type tnCNLinkOspfAuthKey based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnCNLinkOspfAuthKey_Type.__name__ = "SnmpAdminString"
_TnCNLinkOspfAuthKey_Object = MibTableColumn
tnCNLinkOspfAuthKey = _TnCNLinkOspfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 49),
    _TnCNLinkOspfAuthKey_Type()
)
tnCNLinkOspfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOspfAuthKey.setStatus("current")


class _TnCNLinkOspfAuthKeyId_Type(Unsigned32):
    """Custom type tnCNLinkOspfAuthKeyId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TnCNLinkOspfAuthKeyId_Type.__name__ = "Unsigned32"
_TnCNLinkOspfAuthKeyId_Object = MibTableColumn
tnCNLinkOspfAuthKeyId = _TnCNLinkOspfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 50),
    _TnCNLinkOspfAuthKeyId_Type()
)
tnCNLinkOspfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOspfAuthKeyId.setStatus("current")
_TnCNLinkViaChannelTable_Object = MibTable
tnCNLinkViaChannelTable = _TnCNLinkViaChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnCNLinkViaChannelTable.setStatus("current")
_TnCNLinkViaChannelEntry_Object = MibTableRow
tnCNLinkViaChannelEntry = _TnCNLinkViaChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 2, 1)
)
tnCNLinkViaChannelEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
    (0, "TROPIC-L1SERVICE-MIB", "tnPortIndex"),
    (0, "TROPIC-L1SERVICE-MIB", "tnChannelIndex"),
)
if mibBuilder.loadTexts:
    tnCNLinkViaChannelEntry.setStatus("current")
_TnPortIndex_Type = TropicPortIndexType
_TnPortIndex_Object = MibTableColumn
tnPortIndex = _TnPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 2, 1, 1),
    _TnPortIndex_Type()
)
tnPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPortIndex.setStatus("current")
_TnChannelIndex_Type = TropicChannelIndexType
_TnChannelIndex_Object = MibTableColumn
tnChannelIndex = _TnChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 2, 1, 2),
    _TnChannelIndex_Type()
)
tnChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnChannelIndex.setStatus("current")
_TnCNLinkViaChannelIfIndex_Type = InterfaceIndex
_TnCNLinkViaChannelIfIndex_Object = MibTableColumn
tnCNLinkViaChannelIfIndex = _TnCNLinkViaChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 2, 1, 3),
    _TnCNLinkViaChannelIfIndex_Type()
)
tnCNLinkViaChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkViaChannelIfIndex.setStatus("current")
_TnDataNetworkLink_ObjectIdentity = ObjectIdentity
tnDataNetworkLink = _TnDataNetworkLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 2)
)
_TnL1TrafficParamTable_Object = MibTable
tnL1TrafficParamTable = _TnL1TrafficParamTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    tnL1TrafficParamTable.setStatus("current")
_TnL1TrafficParamEntry_Object = MibTableRow
tnL1TrafficParamEntry = _TnL1TrafficParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 2, 3, 1)
)
tnL1TrafficParamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-L1SERVICE-MIB", "tnL1TrafficParamPerHopBehaviour"),
)
if mibBuilder.loadTexts:
    tnL1TrafficParamEntry.setStatus("current")
_TnL1TrafficParamPerHopBehaviour_Type = TnPerHopBehaviourType
_TnL1TrafficParamPerHopBehaviour_Object = MibTableColumn
tnL1TrafficParamPerHopBehaviour = _TnL1TrafficParamPerHopBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 2, 3, 1, 1),
    _TnL1TrafficParamPerHopBehaviour_Type()
)
tnL1TrafficParamPerHopBehaviour.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnL1TrafficParamPerHopBehaviour.setStatus("current")
_TnL1TrafficParamBookingFactor_Type = Unsigned32
_TnL1TrafficParamBookingFactor_Object = MibTableColumn
tnL1TrafficParamBookingFactor = _TnL1TrafficParamBookingFactor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 2, 3, 1, 2),
    _TnL1TrafficParamBookingFactor_Type()
)
tnL1TrafficParamBookingFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnL1TrafficParamBookingFactor.setStatus("current")
if mibBuilder.loadTexts:
    tnL1TrafficParamBookingFactor.setUnits("percentage")
_TnL1TrafficParamMaximumLoad_Type = Unsigned32
_TnL1TrafficParamMaximumLoad_Object = MibTableColumn
tnL1TrafficParamMaximumLoad = _TnL1TrafficParamMaximumLoad_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 2, 3, 1, 3),
    _TnL1TrafficParamMaximumLoad_Type()
)
tnL1TrafficParamMaximumLoad.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnL1TrafficParamMaximumLoad.setStatus("current")
if mibBuilder.loadTexts:
    tnL1TrafficParamMaximumLoad.setUnits("percentage")
_TnL1TrafficParamPMF_Type = Unsigned32
_TnL1TrafficParamPMF_Object = MibTableColumn
tnL1TrafficParamPMF = _TnL1TrafficParamPMF_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 2, 3, 1, 4),
    _TnL1TrafficParamPMF_Type()
)
tnL1TrafficParamPMF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnL1TrafficParamPMF.setStatus("current")
if mibBuilder.loadTexts:
    tnL1TrafficParamPMF.setUnits("percentage")
_TnL1TrafficParamAvailableBandwidth_Type = Unsigned32
_TnL1TrafficParamAvailableBandwidth_Object = MibTableColumn
tnL1TrafficParamAvailableBandwidth = _TnL1TrafficParamAvailableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 2, 3, 1, 5),
    _TnL1TrafficParamAvailableBandwidth_Type()
)
tnL1TrafficParamAvailableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnL1TrafficParamAvailableBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    tnL1TrafficParamAvailableBandwidth.setUnits("Mb/s")
_TnIpRoute_ObjectIdentity = ObjectIdentity
tnIpRoute = _TnIpRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4)
)
_TnIpStaticRouteTable_Object = MibTable
tnIpStaticRouteTable = _TnIpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tnIpStaticRouteTable.setStatus("current")
_TnIpStaticRouteEntry_Object = MibTableRow
tnIpStaticRouteEntry = _TnIpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 1, 1)
)
tnIpStaticRouteEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnIpStaticRouteDest"),
    (0, "TROPIC-L1SERVICE-MIB", "tnIpStaticRouteMask"),
    (0, "TROPIC-L1SERVICE-MIB", "tnIpStaticRouteTos"),
    (0, "TROPIC-L1SERVICE-MIB", "tnIpStaticRouteNextHop"),
)
if mibBuilder.loadTexts:
    tnIpStaticRouteEntry.setStatus("current")
_TnIpStaticRouteDest_Type = IpAddress
_TnIpStaticRouteDest_Object = MibTableColumn
tnIpStaticRouteDest = _TnIpStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 1, 1, 1),
    _TnIpStaticRouteDest_Type()
)
tnIpStaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIpStaticRouteDest.setStatus("current")
_TnIpStaticRouteMask_Type = IpAddress
_TnIpStaticRouteMask_Object = MibTableColumn
tnIpStaticRouteMask = _TnIpStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 1, 1, 2),
    _TnIpStaticRouteMask_Type()
)
tnIpStaticRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIpStaticRouteMask.setStatus("current")
_TnIpStaticRouteTos_Type = Integer32
_TnIpStaticRouteTos_Object = MibTableColumn
tnIpStaticRouteTos = _TnIpStaticRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 1, 1, 3),
    _TnIpStaticRouteTos_Type()
)
tnIpStaticRouteTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIpStaticRouteTos.setStatus("current")
_TnIpStaticRouteNextHop_Type = IpAddress
_TnIpStaticRouteNextHop_Object = MibTableColumn
tnIpStaticRouteNextHop = _TnIpStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 1, 1, 4),
    _TnIpStaticRouteNextHop_Type()
)
tnIpStaticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIpStaticRouteNextHop.setStatus("current")


class _TnIpStaticRouteMetric_Type(Integer32):
    """Custom type tnIpStaticRouteMetric based on Integer32"""
    defaultValue = -1


_TnIpStaticRouteMetric_Type.__name__ = "Integer32"
_TnIpStaticRouteMetric_Object = MibTableColumn
tnIpStaticRouteMetric = _TnIpStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 1, 1, 6),
    _TnIpStaticRouteMetric_Type()
)
tnIpStaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpStaticRouteMetric.setStatus("current")


class _TnIpStaticRouteWithRedistribution_Type(TruthValue):
    """Custom type tnIpStaticRouteWithRedistribution based on TruthValue"""
    defaultValue = 2


_TnIpStaticRouteWithRedistribution_Type.__name__ = "TruthValue"
_TnIpStaticRouteWithRedistribution_Object = MibTableColumn
tnIpStaticRouteWithRedistribution = _TnIpStaticRouteWithRedistribution_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 1, 1, 7),
    _TnIpStaticRouteWithRedistribution_Type()
)
tnIpStaticRouteWithRedistribution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpStaticRouteWithRedistribution.setStatus("current")
_TnIpStaticRouteRowStatus_Type = RowStatus
_TnIpStaticRouteRowStatus_Object = MibTableColumn
tnIpStaticRouteRowStatus = _TnIpStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 1, 1, 8),
    _TnIpStaticRouteRowStatus_Type()
)
tnIpStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpStaticRouteRowStatus.setStatus("current")
_TnIpCidrRouteTable_Object = MibTable
tnIpCidrRouteTable = _TnIpCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    tnIpCidrRouteTable.setStatus("current")
_TnIpCidrRouteEntry_Object = MibTableRow
tnIpCidrRouteEntry = _TnIpCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    tnIpCidrRouteEntry.setStatus("current")


class _TnIpCidrRouteWithRedistribution_Type(TruthValue):
    """Custom type tnIpCidrRouteWithRedistribution based on TruthValue"""
    defaultValue = 2


_TnIpCidrRouteWithRedistribution_Type.__name__ = "TruthValue"
_TnIpCidrRouteWithRedistribution_Object = MibTableColumn
tnIpCidrRouteWithRedistribution = _TnIpCidrRouteWithRedistribution_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 2, 1, 1),
    _TnIpCidrRouteWithRedistribution_Type()
)
tnIpCidrRouteWithRedistribution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpCidrRouteWithRedistribution.setStatus("current")
_TnIpRouteGlobal_ObjectIdentity = ObjectIdentity
tnIpRouteGlobal = _TnIpRouteGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3)
)


class _TnIpStaticRouteRedistributeMetricType_Type(Unsigned32):
    """Custom type tnIpStaticRouteRedistributeMetricType based on Unsigned32"""
    defaultValue = 2


_TnIpStaticRouteRedistributeMetricType_Type.__name__ = "Unsigned32"
_TnIpStaticRouteRedistributeMetricType_Object = MibScalar
tnIpStaticRouteRedistributeMetricType = _TnIpStaticRouteRedistributeMetricType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 1),
    _TnIpStaticRouteRedistributeMetricType_Type()
)
tnIpStaticRouteRedistributeMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpStaticRouteRedistributeMetricType.setStatus("current")


class _TnIpStaticRouteRedistributeMetric_Type(Unsigned32):
    """Custom type tnIpStaticRouteRedistributeMetric based on Unsigned32"""
    defaultValue = 20


_TnIpStaticRouteRedistributeMetric_Type.__name__ = "Unsigned32"
_TnIpStaticRouteRedistributeMetric_Object = MibScalar
tnIpStaticRouteRedistributeMetric = _TnIpStaticRouteRedistributeMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 2),
    _TnIpStaticRouteRedistributeMetric_Type()
)
tnIpStaticRouteRedistributeMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpStaticRouteRedistributeMetric.setStatus("current")


class _TnIpDefaultRouteRedistributeMetricType_Type(Unsigned32):
    """Custom type tnIpDefaultRouteRedistributeMetricType based on Unsigned32"""
    defaultValue = 2


_TnIpDefaultRouteRedistributeMetricType_Type.__name__ = "Unsigned32"
_TnIpDefaultRouteRedistributeMetricType_Object = MibScalar
tnIpDefaultRouteRedistributeMetricType = _TnIpDefaultRouteRedistributeMetricType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 3),
    _TnIpDefaultRouteRedistributeMetricType_Type()
)
tnIpDefaultRouteRedistributeMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpDefaultRouteRedistributeMetricType.setStatus("current")


class _TnIpDefaultRouteRedistributeMetric_Type(Unsigned32):
    """Custom type tnIpDefaultRouteRedistributeMetric based on Unsigned32"""
    defaultValue = 10


_TnIpDefaultRouteRedistributeMetric_Type.__name__ = "Unsigned32"
_TnIpDefaultRouteRedistributeMetric_Object = MibScalar
tnIpDefaultRouteRedistributeMetric = _TnIpDefaultRouteRedistributeMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 4),
    _TnIpDefaultRouteRedistributeMetric_Type()
)
tnIpDefaultRouteRedistributeMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpDefaultRouteRedistributeMetric.setStatus("current")


class _TnIpOspfAreaNumberPPPId_Type(Integer32):
    """Custom type tnIpOspfAreaNumberPPPId based on Integer32"""
    defaultValue = 0


_TnIpOspfAreaNumberPPPId_Type.__name__ = "Integer32"
_TnIpOspfAreaNumberPPPId_Object = MibScalar
tnIpOspfAreaNumberPPPId = _TnIpOspfAreaNumberPPPId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 5),
    _TnIpOspfAreaNumberPPPId_Type()
)
tnIpOspfAreaNumberPPPId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpOspfAreaNumberPPPId.setStatus("current")
_TnSharedRiskGroupObjs_ObjectIdentity = ObjectIdentity
tnSharedRiskGroupObjs = _TnSharedRiskGroupObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 5)
)
_TnL1NetworkLink_ObjectIdentity = ObjectIdentity
tnL1NetworkLink = _TnL1NetworkLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 5, 1)
)
_TnL1Hop_ObjectIdentity = ObjectIdentity
tnL1Hop = _TnL1Hop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 5, 2)
)
_TnL1Fiber_ObjectIdentity = ObjectIdentity
tnL1Fiber = _TnL1Fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 5, 3)
)
_TnL1Conduit_ObjectIdentity = ObjectIdentity
tnL1Conduit = _TnL1Conduit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 5, 4)
)
_TnL1Protection_ObjectIdentity = ObjectIdentity
tnL1Protection = _TnL1Protection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6)
)
_TnApsGroupTable_Object = MibTable
tnApsGroupTable = _TnApsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    tnApsGroupTable.setStatus("current")
_TnApsGroupEntry_Object = MibTableRow
tnApsGroupEntry = _TnApsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1)
)
tnApsGroupEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnApsGroupId"),
)
if mibBuilder.loadTexts:
    tnApsGroupEntry.setStatus("current")
_TnApsGroupId_Type = TnApsGroupId
_TnApsGroupId_Object = MibTableColumn
tnApsGroupId = _TnApsGroupId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 1),
    _TnApsGroupId_Type()
)
tnApsGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnApsGroupId.setStatus("current")
_TnApsGroupRowStatus_Type = RowStatus
_TnApsGroupRowStatus_Object = MibTableColumn
tnApsGroupRowStatus = _TnApsGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 2),
    _TnApsGroupRowStatus_Type()
)
tnApsGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsGroupRowStatus.setStatus("current")


class _TnApsGroupDescr_Type(SnmpAdminString):
    """Custom type tnApsGroupDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnApsGroupDescr_Type.__name__ = "SnmpAdminString"
_TnApsGroupDescr_Object = MibTableColumn
tnApsGroupDescr = _TnApsGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 3),
    _TnApsGroupDescr_Type()
)
tnApsGroupDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsGroupDescr.setStatus("current")


class _TnApsGroupMode_Type(TropicProtectionLevel):
    """Custom type tnApsGroupMode based on TropicProtectionLevel"""
    defaultValue = 4


_TnApsGroupMode_Type.__name__ = "TropicProtectionLevel"
_TnApsGroupMode_Object = MibTableColumn
tnApsGroupMode = _TnApsGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 4),
    _TnApsGroupMode_Type()
)
tnApsGroupMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsGroupMode.setStatus("current")


class _TnApsGroupRevert_Type(Integer32):
    """Custom type tnApsGroupRevert based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 1),
          ("revertive", 2))
    )


_TnApsGroupRevert_Type.__name__ = "Integer32"
_TnApsGroupRevert_Object = MibTableColumn
tnApsGroupRevert = _TnApsGroupRevert_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 5),
    _TnApsGroupRevert_Type()
)
tnApsGroupRevert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsGroupRevert.setStatus("current")


class _TnApsGroupDirection_Type(Integer32):
    """Custom type tnApsGroupDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unidirectional", 1),
          ("bidirectional", 2))
    )


_TnApsGroupDirection_Type.__name__ = "Integer32"
_TnApsGroupDirection_Object = MibTableColumn
tnApsGroupDirection = _TnApsGroupDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 6),
    _TnApsGroupDirection_Type()
)
tnApsGroupDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsGroupDirection.setStatus("current")


class _TnApsGroupExtraTraffic_Type(AluWdmEnabledDisabled):
    """Custom type tnApsGroupExtraTraffic based on AluWdmEnabledDisabled"""
    defaultValue = 2


_TnApsGroupExtraTraffic_Type.__name__ = "AluWdmEnabledDisabled"
_TnApsGroupExtraTraffic_Object = MibTableColumn
tnApsGroupExtraTraffic = _TnApsGroupExtraTraffic_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 7),
    _TnApsGroupExtraTraffic_Type()
)
tnApsGroupExtraTraffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsGroupExtraTraffic.setStatus("current")


class _TnApsGroupWaitToRestore_Type(Unsigned32):
    """Custom type tnApsGroupWaitToRestore based on Unsigned32"""
    defaultValue = 5


_TnApsGroupWaitToRestore_Type.__name__ = "Unsigned32"
_TnApsGroupWaitToRestore_Object = MibTableColumn
tnApsGroupWaitToRestore = _TnApsGroupWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 8),
    _TnApsGroupWaitToRestore_Type()
)
tnApsGroupWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsGroupWaitToRestore.setStatus("current")
if mibBuilder.loadTexts:
    tnApsGroupWaitToRestore.setUnits("minutes")
_TnApsGroupK1K2Rcv_Type = ApsK1K2
_TnApsGroupK1K2Rcv_Object = MibTableColumn
tnApsGroupK1K2Rcv = _TnApsGroupK1K2Rcv_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 9),
    _TnApsGroupK1K2Rcv_Type()
)
tnApsGroupK1K2Rcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnApsGroupK1K2Rcv.setStatus("current")
_TnApsGroupK1K2Trans_Type = ApsK1K2
_TnApsGroupK1K2Trans_Object = MibTableColumn
tnApsGroupK1K2Trans = _TnApsGroupK1K2Trans_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 10),
    _TnApsGroupK1K2Trans_Type()
)
tnApsGroupK1K2Trans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnApsGroupK1K2Trans.setStatus("current")


class _TnApsGroupCurrentStatus_Type(Bits):
    """Custom type tnApsGroupCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("modeMismatch", 0),
          ("channelMismatch", 1),
          ("psbf", 2),
          ("feplf", 3),
          ("extraTraffic", 4))
    )

_TnApsGroupCurrentStatus_Type.__name__ = "Bits"
_TnApsGroupCurrentStatus_Object = MibTableColumn
tnApsGroupCurrentStatus = _TnApsGroupCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 11),
    _TnApsGroupCurrentStatus_Type()
)
tnApsGroupCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnApsGroupCurrentStatus.setStatus("current")


class _TnApsGroupModeMismatches_Type(Counter32):
    """Custom type tnApsGroupModeMismatches based on Counter32"""
    defaultValue = 0


_TnApsGroupModeMismatches_Type.__name__ = "Counter32"
_TnApsGroupModeMismatches_Object = MibTableColumn
tnApsGroupModeMismatches = _TnApsGroupModeMismatches_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 12),
    _TnApsGroupModeMismatches_Type()
)
tnApsGroupModeMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnApsGroupModeMismatches.setStatus("current")


class _TnApsGroupChannelMismatches_Type(Counter32):
    """Custom type tnApsGroupChannelMismatches based on Counter32"""
    defaultValue = 0


_TnApsGroupChannelMismatches_Type.__name__ = "Counter32"
_TnApsGroupChannelMismatches_Object = MibTableColumn
tnApsGroupChannelMismatches = _TnApsGroupChannelMismatches_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 13),
    _TnApsGroupChannelMismatches_Type()
)
tnApsGroupChannelMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnApsGroupChannelMismatches.setStatus("current")


class _TnApsGroupPSBFs_Type(Counter32):
    """Custom type tnApsGroupPSBFs based on Counter32"""
    defaultValue = 0


_TnApsGroupPSBFs_Type.__name__ = "Counter32"
_TnApsGroupPSBFs_Object = MibTableColumn
tnApsGroupPSBFs = _TnApsGroupPSBFs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 14),
    _TnApsGroupPSBFs_Type()
)
tnApsGroupPSBFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnApsGroupPSBFs.setStatus("current")


class _TnApsGroupFEPLFs_Type(Counter32):
    """Custom type tnApsGroupFEPLFs based on Counter32"""
    defaultValue = 0


_TnApsGroupFEPLFs_Type.__name__ = "Counter32"
_TnApsGroupFEPLFs_Object = MibTableColumn
tnApsGroupFEPLFs = _TnApsGroupFEPLFs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 15),
    _TnApsGroupFEPLFs_Type()
)
tnApsGroupFEPLFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnApsGroupFEPLFs.setStatus("current")
_TnApsGroupSwitchedIfIndex_Type = InterfaceIndex
_TnApsGroupSwitchedIfIndex_Object = MibTableColumn
tnApsGroupSwitchedIfIndex = _TnApsGroupSwitchedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 16),
    _TnApsGroupSwitchedIfIndex_Type()
)
tnApsGroupSwitchedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnApsGroupSwitchedIfIndex.setStatus("current")
_TnApsGroupMembers_Type = SnmpAdminString
_TnApsGroupMembers_Object = MibTableColumn
tnApsGroupMembers = _TnApsGroupMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 17),
    _TnApsGroupMembers_Type()
)
tnApsGroupMembers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsGroupMembers.setStatus("current")
_TnApsMemberTable_Object = MibTable
tnApsMemberTable = _TnApsMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    tnApsMemberTable.setStatus("current")
_TnApsMemberEntry_Object = MibTableRow
tnApsMemberEntry = _TnApsMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 2, 1)
)
tnApsMemberEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnApsGroupId"),
    (0, "TROPIC-L1SERVICE-MIB", "tnApsMemberIfIndex"),
)
if mibBuilder.loadTexts:
    tnApsMemberEntry.setStatus("current")
_TnApsMemberIfIndex_Type = InterfaceIndex
_TnApsMemberIfIndex_Object = MibTableColumn
tnApsMemberIfIndex = _TnApsMemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 2, 1, 1),
    _TnApsMemberIfIndex_Type()
)
tnApsMemberIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnApsMemberIfIndex.setStatus("current")
_TnApsMemberRowStatus_Type = RowStatus
_TnApsMemberRowStatus_Object = MibTableColumn
tnApsMemberRowStatus = _TnApsMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 2, 1, 2),
    _TnApsMemberRowStatus_Type()
)
tnApsMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsMemberRowStatus.setStatus("current")


class _TnApsMemberConfigNumber_Type(Integer32):
    """Custom type tnApsMemberConfigNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_TnApsMemberConfigNumber_Type.__name__ = "Integer32"
_TnApsMemberConfigNumber_Object = MibTableColumn
tnApsMemberConfigNumber = _TnApsMemberConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 2, 1, 3),
    _TnApsMemberConfigNumber_Type()
)
tnApsMemberConfigNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsMemberConfigNumber.setStatus("current")


class _TnApsMemberSwitch_Type(Integer32):
    """Custom type tnApsMemberSwitch based on Integer32"""
    defaultValue = 1

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
        *(("noCmd", 1),
          ("clear", 2),
          ("lockoutOfProtection", 3),
          ("forcedSwitchWorkToProtect", 4),
          ("forcedSwitchProtectToWork", 5),
          ("manualSwitchWorkToProtect", 6),
          ("manualSwitchProtectToWork", 7),
          ("exercise", 8))
    )


_TnApsMemberSwitch_Type.__name__ = "Integer32"
_TnApsMemberSwitch_Object = MibTableColumn
tnApsMemberSwitch = _TnApsMemberSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 2, 1, 5),
    _TnApsMemberSwitch_Type()
)
tnApsMemberSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsMemberSwitch.setStatus("current")


class _TnApsMemberCurrentStatus_Type(Bits):
    """Custom type tnApsMemberCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("lockedOut", 0),
          ("sd", 1),
          ("sf", 2),
          ("switched", 3),
          ("txActive", 4),
          ("txStandby", 5),
          ("rxActive", 6),
          ("rxStandby", 7))
    )

_TnApsMemberCurrentStatus_Type.__name__ = "Bits"
_TnApsMemberCurrentStatus_Object = MibTableColumn
tnApsMemberCurrentStatus = _TnApsMemberCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 2, 1, 7),
    _TnApsMemberCurrentStatus_Type()
)
tnApsMemberCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnApsMemberCurrentStatus.setStatus("current")
_TnIpTunnel_ObjectIdentity = ObjectIdentity
tnIpTunnel = _TnIpTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 7)
)
_TnControlNetworkMap_ObjectIdentity = ObjectIdentity
tnControlNetworkMap = _TnControlNetworkMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 8)
)
_TnControlNetworkMapTable_Object = MibTable
tnControlNetworkMapTable = _TnControlNetworkMapTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    tnControlNetworkMapTable.setStatus("current")
_TnControlNetworkMapEntry_Object = MibTableRow
tnControlNetworkMapEntry = _TnControlNetworkMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 8, 1, 1)
)
tnControlNetworkMapEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnCNMapTableIndex"),
)
if mibBuilder.loadTexts:
    tnControlNetworkMapEntry.setStatus("current")
_TnCNMapTableIndex_Type = Unsigned32
_TnCNMapTableIndex_Object = MibTableColumn
tnCNMapTableIndex = _TnCNMapTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 8, 1, 1, 1),
    _TnCNMapTableIndex_Type()
)
tnCNMapTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCNMapTableIndex.setStatus("current")
_TnCNMapIpAddress_Type = IpAddress
_TnCNMapIpAddress_Object = MibTableColumn
tnCNMapIpAddress = _TnCNMapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 8, 1, 1, 2),
    _TnCNMapIpAddress_Type()
)
tnCNMapIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNMapIpAddress.setStatus("current")


class _TnCNMapNeName_Type(OctetString):
    """Custom type tnCNMapNeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 81),
    )


_TnCNMapNeName_Type.__name__ = "OctetString"
_TnCNMapNeName_Object = MibTableColumn
tnCNMapNeName = _TnCNMapNeName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 8, 1, 1, 3),
    _TnCNMapNeName_Type()
)
tnCNMapNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNMapNeName.setStatus("current")


class _TnCNMapSoftwareRelease_Type(OctetString):
    """Custom type tnCNMapSoftwareRelease based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 81),
    )


_TnCNMapSoftwareRelease_Type.__name__ = "OctetString"
_TnCNMapSoftwareRelease_Object = MibTableColumn
tnCNMapSoftwareRelease = _TnCNMapSoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 8, 1, 1, 4),
    _TnCNMapSoftwareRelease_Type()
)
tnCNMapSoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNMapSoftwareRelease.setStatus("current")
_TnNetworkInterface_ObjectIdentity = ObjectIdentity
tnNetworkInterface = _TnNetworkInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9)
)
_TnNetIfTable_Object = MibTable
tnNetIfTable = _TnNetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    tnNetIfTable.setStatus("current")
_TnNetIfEntry_Object = MibTableRow
tnNetIfEntry = _TnNetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1)
)
tnNetIfEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnNetIfIndex"),
)
if mibBuilder.loadTexts:
    tnNetIfEntry.setStatus("current")


class _TnNetIfIndex_Type(Unsigned32):
    """Custom type tnNetIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_TnNetIfIndex_Type.__name__ = "Unsigned32"
_TnNetIfIndex_Object = MibTableColumn
tnNetIfIndex = _TnNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 1),
    _TnNetIfIndex_Type()
)
tnNetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNetIfIndex.setStatus("current")
_TnNetIfTypeOfOperation_Type = AluWdmTypeOfNetIfOperation
_TnNetIfTypeOfOperation_Object = MibTableColumn
tnNetIfTypeOfOperation = _TnNetIfTypeOfOperation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 2),
    _TnNetIfTypeOfOperation_Type()
)
tnNetIfTypeOfOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfTypeOfOperation.setStatus("current")


class _TnNetIfStatus_Type(Integer32):
    """Custom type tnNetIfStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnNetIfStatus_Type.__name__ = "Integer32"
_TnNetIfStatus_Object = MibTableColumn
tnNetIfStatus = _TnNetIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 3),
    _TnNetIfStatus_Type()
)
tnNetIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfStatus.setStatus("current")


class _TnNetIfPacketType_Type(Integer32):
    """Custom type tnNetIfPacketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("std", 1),
          ("non-std", 2))
    )


_TnNetIfPacketType_Type.__name__ = "Integer32"
_TnNetIfPacketType_Object = MibTableColumn
tnNetIfPacketType = _TnNetIfPacketType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 4),
    _TnNetIfPacketType_Type()
)
tnNetIfPacketType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfPacketType.setStatus("current")


class _TnNetIfMtu_Type(Integer32):
    """Custom type tnNetIfMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 1500),
    )


_TnNetIfMtu_Type.__name__ = "Integer32"
_TnNetIfMtu_Object = MibTableColumn
tnNetIfMtu = _TnNetIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 5),
    _TnNetIfMtu_Type()
)
tnNetIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfMtu.setStatus("current")


class _TnNetIfHelloInterval_Type(Unsigned32):
    """Custom type tnNetIfHelloInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnNetIfHelloInterval_Type.__name__ = "Unsigned32"
_TnNetIfHelloInterval_Object = MibTableColumn
tnNetIfHelloInterval = _TnNetIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 6),
    _TnNetIfHelloInterval_Type()
)
tnNetIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnNetIfHelloInterval.setUnits("seconds")


class _TnNetIfRtrDeadInterval_Type(Unsigned32):
    """Custom type tnNetIfRtrDeadInterval based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnNetIfRtrDeadInterval_Type.__name__ = "Unsigned32"
_TnNetIfRtrDeadInterval_Object = MibTableColumn
tnNetIfRtrDeadInterval = _TnNetIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 7),
    _TnNetIfRtrDeadInterval_Type()
)
tnNetIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnNetIfRtrDeadInterval.setUnits("seconds")


class _TnNetIfMetric_Type(Unsigned32):
    """Custom type tnNetIfMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnNetIfMetric_Type.__name__ = "Unsigned32"
_TnNetIfMetric_Object = MibTableColumn
tnNetIfMetric = _TnNetIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 8),
    _TnNetIfMetric_Type()
)
tnNetIfMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfMetric.setStatus("current")


class _TnNetIfOspfAuthentType_Type(Integer32):
    """Custom type tnNetIfOspfAuthentType based on Integer32"""
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
        *(("none", 1),
          ("simple", 2),
          ("md5", 3))
    )


_TnNetIfOspfAuthentType_Type.__name__ = "Integer32"
_TnNetIfOspfAuthentType_Object = MibTableColumn
tnNetIfOspfAuthentType = _TnNetIfOspfAuthentType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 9),
    _TnNetIfOspfAuthentType_Type()
)
tnNetIfOspfAuthentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfOspfAuthentType.setStatus("current")


class _TnNetIfOspfAuthKey_Type(OctetString):
    """Custom type tnNetIfOspfAuthKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnNetIfOspfAuthKey_Type.__name__ = "OctetString"
_TnNetIfOspfAuthKey_Object = MibTableColumn
tnNetIfOspfAuthKey = _TnNetIfOspfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 10),
    _TnNetIfOspfAuthKey_Type()
)
tnNetIfOspfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfOspfAuthKey.setStatus("current")


class _TnNetIfOspfAuthKeyId_Type(Unsigned32):
    """Custom type tnNetIfOspfAuthKeyId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TnNetIfOspfAuthKeyId_Type.__name__ = "Unsigned32"
_TnNetIfOspfAuthKeyId_Object = MibTableColumn
tnNetIfOspfAuthKeyId = _TnNetIfOspfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 11),
    _TnNetIfOspfAuthKeyId_Type()
)
tnNetIfOspfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfOspfAuthKeyId.setStatus("current")


class _TnNetIfCnLinkAdjState_Type(TropicOspfAdjacencyStateType):
    """Custom type tnNetIfCnLinkAdjState based on TropicOspfAdjacencyStateType"""
    defaultValue = 1


_TnNetIfCnLinkAdjState_Type.__name__ = "TropicOspfAdjacencyStateType"
_TnNetIfCnLinkAdjState_Object = MibTableColumn
tnNetIfCnLinkAdjState = _TnNetIfCnLinkAdjState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 12),
    _TnNetIfCnLinkAdjState_Type()
)
tnNetIfCnLinkAdjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetIfCnLinkAdjState.setStatus("current")


class _TnNetIfMtuNeg_Type(Integer32):
    """Custom type tnNetIfMtuNeg based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1500),
    )


_TnNetIfMtuNeg_Type.__name__ = "Integer32"
_TnNetIfMtuNeg_Object = MibTableColumn
tnNetIfMtuNeg = _TnNetIfMtuNeg_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 13),
    _TnNetIfMtuNeg_Type()
)
tnNetIfMtuNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetIfMtuNeg.setStatus("current")
_TnNetIfFacilityTable_Object = MibTable
tnNetIfFacilityTable = _TnNetIfFacilityTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    tnNetIfFacilityTable.setStatus("current")
_TnNetIfFacilityEntry_Object = MibTableRow
tnNetIfFacilityEntry = _TnNetIfFacilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 2, 1)
)
tnNetIfFacilityEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnNetIfIndex"),
    (0, "TROPIC-L1SERVICE-MIB", "tnNetIfFacilityIfIndex"),
    (0, "TROPIC-L1SERVICE-MIB", "tnNetIfFacilityIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnNetIfFacilityEntry.setStatus("current")
_TnNetIfFacilityIfIndex_Type = Unsigned32
_TnNetIfFacilityIfIndex_Object = MibTableColumn
tnNetIfFacilityIfIndex = _TnNetIfFacilityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 2, 1, 1),
    _TnNetIfFacilityIfIndex_Type()
)
tnNetIfFacilityIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNetIfFacilityIfIndex.setStatus("current")
_TnNetIfFacilityIfIndexLo_Type = Unsigned32
_TnNetIfFacilityIfIndexLo_Object = MibTableColumn
tnNetIfFacilityIfIndexLo = _TnNetIfFacilityIfIndexLo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 2, 1, 2),
    _TnNetIfFacilityIfIndexLo_Type()
)
tnNetIfFacilityIfIndexLo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNetIfFacilityIfIndexLo.setStatus("current")
_TnNetIfFacilityTypeOfOperation_Type = AluWdmTypeOfNetIfOperation
_TnNetIfFacilityTypeOfOperation_Object = MibTableColumn
tnNetIfFacilityTypeOfOperation = _TnNetIfFacilityTypeOfOperation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 2, 1, 3),
    _TnNetIfFacilityTypeOfOperation_Type()
)
tnNetIfFacilityTypeOfOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfFacilityTypeOfOperation.setStatus("current")


class _TnNetIfFacilityEccChanType_Type(Integer32):
    """Custom type tnNetIfFacilityEccChanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gcc0", 1),
          ("gcc1", 2),
          ("gcc2", 3))
    )


_TnNetIfFacilityEccChanType_Type.__name__ = "Integer32"
_TnNetIfFacilityEccChanType_Object = MibTableColumn
tnNetIfFacilityEccChanType = _TnNetIfFacilityEccChanType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 2, 1, 4),
    _TnNetIfFacilityEccChanType_Type()
)
tnNetIfFacilityEccChanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfFacilityEccChanType.setStatus("current")
ipCidrRouteEntry.registerAugmentions(
    ("TROPIC-L1SERVICE-MIB",
     "tnIpCidrRouteEntry")
)
tnIpCidrRouteEntry.setIndexNames(*ipCidrRouteEntry.getIndexNames())

# Managed Objects groups

tnControlNetworkLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 1)
)
tnControlNetworkLinkGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnCNLinkDescr"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkAdminStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOperStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkPhysicalIfIndex"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkIpAddress"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkSubnetMask"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkHelloInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkRtrDeadInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkTeMetric"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfRoutingState"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkConfigIfType"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkConfigRtrPriority"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkEquipOperStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkDhcpEnabled"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkSpeed"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkDuplex"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkProxyArp"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkDHCPServer"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkDHCPRange"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkAdjState"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOscMode"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkDHCPDfltGtwy"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkCitAutoStateCtrl"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkAutoStateSourceIP"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkSourceLossCount"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkSourceIPCheckInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfAuthentType"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfAuthKey"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfAuthKeyId"))
)
if mibBuilder.loadTexts:
    tnControlNetworkLinkGroup.setStatus("current")

tnCNLinkViaChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 2)
)
tnCNLinkViaChannelGroup.setObjects(
    ("TROPIC-L1SERVICE-MIB", "tnCNLinkViaChannelIfIndex")
)
if mibBuilder.loadTexts:
    tnCNLinkViaChannelGroup.setStatus("current")

tnIpStaticRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 3)
)
tnIpStaticRouteGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnIpStaticRouteDest"),
        ("TROPIC-L1SERVICE-MIB", "tnIpStaticRouteMask"),
        ("TROPIC-L1SERVICE-MIB", "tnIpStaticRouteTos"),
        ("TROPIC-L1SERVICE-MIB", "tnIpStaticRouteNextHop"),
        ("TROPIC-L1SERVICE-MIB", "tnIpStaticRouteMetric"),
        ("TROPIC-L1SERVICE-MIB", "tnIpStaticRouteWithRedistribution"))
)
if mibBuilder.loadTexts:
    tnIpStaticRouteGroup.setStatus("current")

tnIpCidrRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 4)
)
tnIpCidrRouteGroup.setObjects(
    ("TROPIC-L1SERVICE-MIB", "tnIpCidrRouteWithRedistribution")
)
if mibBuilder.loadTexts:
    tnIpCidrRouteGroup.setStatus("current")

tnL1TrafficParmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 5)
)
tnL1TrafficParmGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnL1TrafficParamBookingFactor"),
        ("TROPIC-L1SERVICE-MIB", "tnL1TrafficParamMaximumLoad"),
        ("TROPIC-L1SERVICE-MIB", "tnL1TrafficParamPMF"),
        ("TROPIC-L1SERVICE-MIB", "tnL1TrafficParamAvailableBandwidth"))
)
if mibBuilder.loadTexts:
    tnL1TrafficParmGroup.setStatus("current")

tnIpRouteGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 6)
)
tnIpRouteGlobalGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnIpStaticRouteRedistributeMetricType"),
        ("TROPIC-L1SERVICE-MIB", "tnIpStaticRouteRedistributeMetric"),
        ("TROPIC-L1SERVICE-MIB", "tnIpDefaultRouteRedistributeMetricType"),
        ("TROPIC-L1SERVICE-MIB", "tnIpDefaultRouteRedistributeMetric"),
        ("TROPIC-L1SERVICE-MIB", "tnIpOspfAreaNumberPPPId"))
)
if mibBuilder.loadTexts:
    tnIpRouteGlobalGroup.setStatus("current")

tnApsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 10)
)
tnApsGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnApsGroupRowStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupDescr"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupMode"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupRevert"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupDirection"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupExtraTraffic"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupWaitToRestore"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupK1K2Rcv"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupK1K2Trans"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupCurrentStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupModeMismatches"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupChannelMismatches"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupPSBFs"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupFEPLFs"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupSwitchedIfIndex"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupMembers"))
)
if mibBuilder.loadTexts:
    tnApsGroup.setStatus("current")

tnApsMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 11)
)
tnApsMemberGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnApsMemberRowStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnApsMemberConfigNumber"),
        ("TROPIC-L1SERVICE-MIB", "tnApsMemberSwitch"),
        ("TROPIC-L1SERVICE-MIB", "tnApsMemberCurrentStatus"))
)
if mibBuilder.loadTexts:
    tnApsMemberGroup.setStatus("current")

tnControlNetworkMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 13)
)
tnControlNetworkMapGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnCNMapIpAddress"),
        ("TROPIC-L1SERVICE-MIB", "tnCNMapNeName"),
        ("TROPIC-L1SERVICE-MIB", "tnCNMapSoftwareRelease"))
)
if mibBuilder.loadTexts:
    tnControlNetworkMapGroup.setStatus("current")

tnNetIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 14)
)
tnNetIfGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnNetIfTypeOfOperation"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfPacketType"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfMtu"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfHelloInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfRtrDeadInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfMetric"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfAuthentType"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfAuthKey"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfAuthKeyId"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfCnLinkAdjState"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfMtuNeg"))
)
if mibBuilder.loadTexts:
    tnNetIfGroup.setStatus("current")

tnNetIfFacilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 15)
)
tnNetIfFacilityGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnNetIfFacilityTypeOfOperation"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfFacilityEccChanType"))
)
if mibBuilder.loadTexts:
    tnNetIfFacilityGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnL1ServiceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 2, 1)
)
tnL1ServiceCompliance.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnControlNetworkLinkGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkViaChannelGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnIpStaticRouteGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnIpCidrRouteGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnL1TrafficParmGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnIpRouteGlobalGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnApsMemberGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnControlNetworkMapGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfFacilityGroup"))
)
if mibBuilder.loadTexts:
    tnL1ServiceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-L1SERVICE-MIB",
    **{"ApsK1K2": ApsK1K2,
       "TropicProtectionLevel": TropicProtectionLevel,
       "TropicLinkAdminStateType": TropicLinkAdminStateType,
       "TropicLinkOperationalStateType": TropicLinkOperationalStateType,
       "TropicOspfAdjacencyStateType": TropicOspfAdjacencyStateType,
       "tnL1ServiceMibModule": tnL1ServiceMibModule,
       "tnL1ServiceConf": tnL1ServiceConf,
       "tnL1ServiceGroups": tnL1ServiceGroups,
       "tnControlNetworkLinkGroup": tnControlNetworkLinkGroup,
       "tnCNLinkViaChannelGroup": tnCNLinkViaChannelGroup,
       "tnIpStaticRouteGroup": tnIpStaticRouteGroup,
       "tnIpCidrRouteGroup": tnIpCidrRouteGroup,
       "tnL1TrafficParmGroup": tnL1TrafficParmGroup,
       "tnIpRouteGlobalGroup": tnIpRouteGlobalGroup,
       "tnApsGroup": tnApsGroup,
       "tnApsMemberGroup": tnApsMemberGroup,
       "tnControlNetworkMapGroup": tnControlNetworkMapGroup,
       "tnNetIfGroup": tnNetIfGroup,
       "tnNetIfFacilityGroup": tnNetIfFacilityGroup,
       "tnL1ServiceCompliances": tnL1ServiceCompliances,
       "tnL1ServiceCompliance": tnL1ServiceCompliance,
       "tnL1ServiceObjs": tnL1ServiceObjs,
       "tnControlNetworkLink": tnControlNetworkLink,
       "tnControlNetworkLinkTable": tnControlNetworkLinkTable,
       "tnControlNetworkLinkEntry": tnControlNetworkLinkEntry,
       "tnCNLinkDescr": tnCNLinkDescr,
       "tnCNLinkAdminStatus": tnCNLinkAdminStatus,
       "tnCNLinkOperStatus": tnCNLinkOperStatus,
       "tnCNLinkPhysicalIfIndex": tnCNLinkPhysicalIfIndex,
       "tnCNLinkIpAddress": tnCNLinkIpAddress,
       "tnCNLinkSubnetMask": tnCNLinkSubnetMask,
       "tnCNLinkHelloInterval": tnCNLinkHelloInterval,
       "tnCNLinkRtrDeadInterval": tnCNLinkRtrDeadInterval,
       "tnCNLinkTeMetric": tnCNLinkTeMetric,
       "tnCNLinkOspfRoutingState": tnCNLinkOspfRoutingState,
       "tnCNLinkConfigIfType": tnCNLinkConfigIfType,
       "tnCNLinkConfigRtrPriority": tnCNLinkConfigRtrPriority,
       "tnCNLinkEquipOperStatus": tnCNLinkEquipOperStatus,
       "tnCNLinkDhcpEnabled": tnCNLinkDhcpEnabled,
       "tnCNLinkSpeed": tnCNLinkSpeed,
       "tnCNLinkDuplex": tnCNLinkDuplex,
       "tnCNLinkProxyArp": tnCNLinkProxyArp,
       "tnCNLinkDHCPServer": tnCNLinkDHCPServer,
       "tnCNLinkDHCPRange": tnCNLinkDHCPRange,
       "tnCNLinkAdjState": tnCNLinkAdjState,
       "tnCNLinkOscMode": tnCNLinkOscMode,
       "tnCNLinkDHCPDfltGtwy": tnCNLinkDHCPDfltGtwy,
       "tnCNLinkCitAutoStateCtrl": tnCNLinkCitAutoStateCtrl,
       "tnCNLinkAutoStateSourceIP": tnCNLinkAutoStateSourceIP,
       "tnCNLinkSourceLossCount": tnCNLinkSourceLossCount,
       "tnCNLinkSourceIPCheckInterval": tnCNLinkSourceIPCheckInterval,
       "tnCNLinkOspfAuthentType": tnCNLinkOspfAuthentType,
       "tnCNLinkOspfAuthKey": tnCNLinkOspfAuthKey,
       "tnCNLinkOspfAuthKeyId": tnCNLinkOspfAuthKeyId,
       "tnCNLinkViaChannelTable": tnCNLinkViaChannelTable,
       "tnCNLinkViaChannelEntry": tnCNLinkViaChannelEntry,
       "tnPortIndex": tnPortIndex,
       "tnChannelIndex": tnChannelIndex,
       "tnCNLinkViaChannelIfIndex": tnCNLinkViaChannelIfIndex,
       "tnDataNetworkLink": tnDataNetworkLink,
       "tnL1TrafficParamTable": tnL1TrafficParamTable,
       "tnL1TrafficParamEntry": tnL1TrafficParamEntry,
       "tnL1TrafficParamPerHopBehaviour": tnL1TrafficParamPerHopBehaviour,
       "tnL1TrafficParamBookingFactor": tnL1TrafficParamBookingFactor,
       "tnL1TrafficParamMaximumLoad": tnL1TrafficParamMaximumLoad,
       "tnL1TrafficParamPMF": tnL1TrafficParamPMF,
       "tnL1TrafficParamAvailableBandwidth": tnL1TrafficParamAvailableBandwidth,
       "tnIpRoute": tnIpRoute,
       "tnIpStaticRouteTable": tnIpStaticRouteTable,
       "tnIpStaticRouteEntry": tnIpStaticRouteEntry,
       "tnIpStaticRouteDest": tnIpStaticRouteDest,
       "tnIpStaticRouteMask": tnIpStaticRouteMask,
       "tnIpStaticRouteTos": tnIpStaticRouteTos,
       "tnIpStaticRouteNextHop": tnIpStaticRouteNextHop,
       "tnIpStaticRouteMetric": tnIpStaticRouteMetric,
       "tnIpStaticRouteWithRedistribution": tnIpStaticRouteWithRedistribution,
       "tnIpStaticRouteRowStatus": tnIpStaticRouteRowStatus,
       "tnIpCidrRouteTable": tnIpCidrRouteTable,
       "tnIpCidrRouteEntry": tnIpCidrRouteEntry,
       "tnIpCidrRouteWithRedistribution": tnIpCidrRouteWithRedistribution,
       "tnIpRouteGlobal": tnIpRouteGlobal,
       "tnIpStaticRouteRedistributeMetricType": tnIpStaticRouteRedistributeMetricType,
       "tnIpStaticRouteRedistributeMetric": tnIpStaticRouteRedistributeMetric,
       "tnIpDefaultRouteRedistributeMetricType": tnIpDefaultRouteRedistributeMetricType,
       "tnIpDefaultRouteRedistributeMetric": tnIpDefaultRouteRedistributeMetric,
       "tnIpOspfAreaNumberPPPId": tnIpOspfAreaNumberPPPId,
       "tnSharedRiskGroupObjs": tnSharedRiskGroupObjs,
       "tnL1NetworkLink": tnL1NetworkLink,
       "tnL1Hop": tnL1Hop,
       "tnL1Fiber": tnL1Fiber,
       "tnL1Conduit": tnL1Conduit,
       "tnL1Protection": tnL1Protection,
       "tnApsGroupTable": tnApsGroupTable,
       "tnApsGroupEntry": tnApsGroupEntry,
       "tnApsGroupId": tnApsGroupId,
       "tnApsGroupRowStatus": tnApsGroupRowStatus,
       "tnApsGroupDescr": tnApsGroupDescr,
       "tnApsGroupMode": tnApsGroupMode,
       "tnApsGroupRevert": tnApsGroupRevert,
       "tnApsGroupDirection": tnApsGroupDirection,
       "tnApsGroupExtraTraffic": tnApsGroupExtraTraffic,
       "tnApsGroupWaitToRestore": tnApsGroupWaitToRestore,
       "tnApsGroupK1K2Rcv": tnApsGroupK1K2Rcv,
       "tnApsGroupK1K2Trans": tnApsGroupK1K2Trans,
       "tnApsGroupCurrentStatus": tnApsGroupCurrentStatus,
       "tnApsGroupModeMismatches": tnApsGroupModeMismatches,
       "tnApsGroupChannelMismatches": tnApsGroupChannelMismatches,
       "tnApsGroupPSBFs": tnApsGroupPSBFs,
       "tnApsGroupFEPLFs": tnApsGroupFEPLFs,
       "tnApsGroupSwitchedIfIndex": tnApsGroupSwitchedIfIndex,
       "tnApsGroupMembers": tnApsGroupMembers,
       "tnApsMemberTable": tnApsMemberTable,
       "tnApsMemberEntry": tnApsMemberEntry,
       "tnApsMemberIfIndex": tnApsMemberIfIndex,
       "tnApsMemberRowStatus": tnApsMemberRowStatus,
       "tnApsMemberConfigNumber": tnApsMemberConfigNumber,
       "tnApsMemberSwitch": tnApsMemberSwitch,
       "tnApsMemberCurrentStatus": tnApsMemberCurrentStatus,
       "tnIpTunnel": tnIpTunnel,
       "tnControlNetworkMap": tnControlNetworkMap,
       "tnControlNetworkMapTable": tnControlNetworkMapTable,
       "tnControlNetworkMapEntry": tnControlNetworkMapEntry,
       "tnCNMapTableIndex": tnCNMapTableIndex,
       "tnCNMapIpAddress": tnCNMapIpAddress,
       "tnCNMapNeName": tnCNMapNeName,
       "tnCNMapSoftwareRelease": tnCNMapSoftwareRelease,
       "tnNetworkInterface": tnNetworkInterface,
       "tnNetIfTable": tnNetIfTable,
       "tnNetIfEntry": tnNetIfEntry,
       "tnNetIfIndex": tnNetIfIndex,
       "tnNetIfTypeOfOperation": tnNetIfTypeOfOperation,
       "tnNetIfStatus": tnNetIfStatus,
       "tnNetIfPacketType": tnNetIfPacketType,
       "tnNetIfMtu": tnNetIfMtu,
       "tnNetIfHelloInterval": tnNetIfHelloInterval,
       "tnNetIfRtrDeadInterval": tnNetIfRtrDeadInterval,
       "tnNetIfMetric": tnNetIfMetric,
       "tnNetIfOspfAuthentType": tnNetIfOspfAuthentType,
       "tnNetIfOspfAuthKey": tnNetIfOspfAuthKey,
       "tnNetIfOspfAuthKeyId": tnNetIfOspfAuthKeyId,
       "tnNetIfCnLinkAdjState": tnNetIfCnLinkAdjState,
       "tnNetIfMtuNeg": tnNetIfMtuNeg,
       "tnNetIfFacilityTable": tnNetIfFacilityTable,
       "tnNetIfFacilityEntry": tnNetIfFacilityEntry,
       "tnNetIfFacilityIfIndex": tnNetIfFacilityIfIndex,
       "tnNetIfFacilityIfIndexLo": tnNetIfFacilityIfIndexLo,
       "tnNetIfFacilityTypeOfOperation": tnNetIfFacilityTypeOfOperation,
       "tnNetIfFacilityEccChanType": tnNetIfFacilityEccChanType}
)
