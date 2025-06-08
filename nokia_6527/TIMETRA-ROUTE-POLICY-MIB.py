# SNMP MIB module (TIMETRA-ROUTE-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-ROUTE-POLICY-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:32 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(IpAddressPrefixLength,
 TFCNameOrEmpty,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TPriority,
 TPriorityOrUndefined,
 TmnxBGPFamilyType,
 TmnxBgpAutonomousSystem,
 TmnxBgpLocalPreference,
 TmnxBgpPreference,
 TmnxCreateOrigin,
 TmnxEnabledDisabled,
 TmnxServId) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "IpAddressPrefixLength",
    "TFCNameOrEmpty",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPriority",
    "TPriorityOrUndefined",
    "TmnxBGPFamilyType",
    "TmnxBgpAutonomousSystem",
    "TmnxBgpLocalPreference",
    "TmnxBgpPreference",
    "TmnxCreateOrigin",
    "TmnxEnabledDisabled",
    "TmnxServId")


# MODULE-IDENTITY

timetraRoutePolicyMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 17)
)
if mibBuilder.loadTexts:
    timetraRoutePolicyMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2013-01-01 00:00",
         "2012-02-28 12:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-01-01 00:00",
         "2006-03-23 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2003-01-20 00:00",
         "2001-04-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TASPathName(TNamedItemOrEmpty):
    status = "current"


class TASPathGroupName(TNamedItemOrEmpty):
    status = "current"


class TCommunityName(TNamedItemOrEmpty):
    status = "current"


class TCommunityMember(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 72),
    )



class TCommunityMemberExpression(DisplayString):
    status = "current"


class TCommunityNameExpression(DisplayString):
    status = "current"


class TDampingName(TNamedItemOrEmpty):
    status = "current"


class TPrefixListName(TNamedItemOrEmpty):
    status = "current"


class TPolicyStatementName(TNamedItem):
    status = "current"


class PolicyStatementNameOrEmpty(TNamedItemOrEmpty):
    status = "current"


class TRoutePolicyRegex(DisplayString):
    status = "current"


class TPolicyStatementEntryID(TextualConvention, Unsigned32):
    status = "current"


class TRoutePolicyProtocol(TextualConvention, Integer32):
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("direct", 2),
          ("static", 3),
          ("bgp", 4),
          ("isis", 5),
          ("ospf", 6),
          ("rip", 7),
          ("aggregate", 8),
          ("bgpVpn", 9),
          ("igmp", 10),
          ("pim", 11),
          ("ospf3", 12),
          ("ldp", 13),
          ("subscriber", 14),
          ("mld", 15),
          ("managed", 16),
          ("msdp", 17),
          ("vpnLeak", 18),
          ("mobileHost", 19),
          ("tms", 20),
          ("nat", 21),
          ("periodic", 22),
          ("ipsec", 23),
          ("mpls", 24),
          ("dhcpv6Pd", 25),
          ("dhcpv6Na", 26),
          ("dhcpv6Ta", 27),
          ("dhcpv6PdExcl", 28),
          ("ripng", 29))
    )



class TOspfRouteType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )



class TIsisLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )



class TPolicyEntryAction(TextualConvention, Integer32):
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
        *(("none", 0),
          ("accept", 1),
          ("reject", 2),
          ("continue", 3),
          ("nextPolicy", 4))
    )



class TPolicyEntryEdit(TextualConvention, Integer32):
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
        *(("none", 1),
          ("add", 2),
          ("remove", 3),
          ("replace", 4))
    )



class TPolicyEntryCriteriaOrigin(TextualConvention, Integer32):
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
        *(("none", 1),
          ("igp", 2),
          ("egp", 3),
          ("incomplete", 4),
          ("any", 5),
          ("aaa", 6),
          ("dhcp", 7),
          ("ludb", 8))
    )



class TPolicyActionTag(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class TPolicyEntryCriteriaState(TextualConvention, Integer32):
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("srrpMaster", 2),
          ("srrpNonMaster", 3),
          ("mobileMaster", 4),
          ("mobileSlave", 5),
          ("ipsecMaster", 6),
          ("ipsecMasterNoPeer", 7),
          ("ipsecNonMaster", 8),
          ("mobilePreSlave", 9))
    )



class TPolicyActionMetricSource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igpCost", 1),
          ("metricVal", 2))
    )



class TPolicyEntryAigpMetricEdit(TextualConvention, Integer32):
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
        *(("none", 1),
          ("add", 2),
          ("replace", 3),
          ("useIgp", 4))
    )



class TPolicyEntryCriteriaMvpnType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("intraAsIpmsiAutoDiscovery", 1),
          ("interAsIpmsiAutoDiscovery", 2),
          ("sPmsiAutoDiscovery", 3),
          ("intraAsSegmentLeafAutoDiscovery", 4),
          ("sourceActiveAutoDiscovery", 5),
          ("sharedTreeJoin", 6),
          ("sourceTreeJoin", 7))
    )



class TPolicyVariableName(TNamedItem):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_TmnxRoutePolicyConformance_ObjectIdentity = ObjectIdentity
tmnxRoutePolicyConformance = _TmnxRoutePolicyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17)
)
_TmnxRoutePolicyCompliances_ObjectIdentity = ObjectIdentity
tmnxRoutePolicyCompliances = _TmnxRoutePolicyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1)
)
_TmnxRoutePolicyGroups_ObjectIdentity = ObjectIdentity
tmnxRoutePolicyGroups = _TmnxRoutePolicyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2)
)
_TRoutePolicyObjects_ObjectIdentity = ObjectIdentity
tRoutePolicyObjects = _TRoutePolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17)
)
_TRPOperObjects_ObjectIdentity = ObjectIdentity
tRPOperObjects = _TRPOperObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1)
)
_TRPOperValueObjects_ObjectIdentity = ObjectIdentity
tRPOperValueObjects = _TRPOperValueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1)
)
_TRPOperASPathTableLastChanged_Type = TimeStamp
_TRPOperASPathTableLastChanged_Object = MibScalar
tRPOperASPathTableLastChanged = _TRPOperASPathTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 1),
    _TRPOperASPathTableLastChanged_Type()
)
tRPOperASPathTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperASPathTableLastChanged.setStatus("obsolete")
_TRPOperASPathTable_Object = MibTable
tRPOperASPathTable = _TRPOperASPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tRPOperASPathTable.setStatus("current")
_TRPOperASPathEntry_Object = MibTableRow
tRPOperASPathEntry = _TRPOperASPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 2, 1)
)
tRPOperASPathEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathName"),
)
if mibBuilder.loadTexts:
    tRPOperASPathEntry.setStatus("current")


class _TRPOperASPathName_Type(TASPathName):
    """Custom type tRPOperASPathName based on TASPathName"""
    subtypeSpec = TASPathName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPOperASPathName_Type.__name__ = "TASPathName"
_TRPOperASPathName_Object = MibTableColumn
tRPOperASPathName = _TRPOperASPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 2, 1, 1),
    _TRPOperASPathName_Type()
)
tRPOperASPathName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperASPathName.setStatus("current")
_TRPOperASPathRowStatus_Type = RowStatus
_TRPOperASPathRowStatus_Object = MibTableColumn
tRPOperASPathRowStatus = _TRPOperASPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 2, 1, 2),
    _TRPOperASPathRowStatus_Type()
)
tRPOperASPathRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperASPathRowStatus.setStatus("current")
_TRPOperASPathRegEx_Type = TRoutePolicyRegex
_TRPOperASPathRegEx_Object = MibTableColumn
tRPOperASPathRegEx = _TRPOperASPathRegEx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 2, 1, 3),
    _TRPOperASPathRegEx_Type()
)
tRPOperASPathRegEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperASPathRegEx.setStatus("current")
_TRPOperASPathEntryLastChanged_Type = TimeStamp
_TRPOperASPathEntryLastChanged_Object = MibTableColumn
tRPOperASPathEntryLastChanged = _TRPOperASPathEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 2, 1, 4),
    _TRPOperASPathEntryLastChanged_Type()
)
tRPOperASPathEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperASPathEntryLastChanged.setStatus("obsolete")
_TRPOperCommunityTableLastChanged_Type = TimeStamp
_TRPOperCommunityTableLastChanged_Object = MibScalar
tRPOperCommunityTableLastChanged = _TRPOperCommunityTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 3),
    _TRPOperCommunityTableLastChanged_Type()
)
tRPOperCommunityTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperCommunityTableLastChanged.setStatus("obsolete")
_TRPOperCommunityTable_Object = MibTable
tRPOperCommunityTable = _TRPOperCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tRPOperCommunityTable.setStatus("current")
_TRPOperCommunityEntry_Object = MibTableRow
tRPOperCommunityEntry = _TRPOperCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 4, 1)
)
tRPOperCommunityEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityMember"),
)
if mibBuilder.loadTexts:
    tRPOperCommunityEntry.setStatus("current")


class _TRPOperCommunityName_Type(TCommunityName):
    """Custom type tRPOperCommunityName based on TCommunityName"""
    subtypeSpec = TCommunityName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPOperCommunityName_Type.__name__ = "TCommunityName"
_TRPOperCommunityName_Object = MibTableColumn
tRPOperCommunityName = _TRPOperCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 4, 1, 1),
    _TRPOperCommunityName_Type()
)
tRPOperCommunityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperCommunityName.setStatus("current")
_TRPOperCommunityMember_Type = TCommunityMember
_TRPOperCommunityMember_Object = MibTableColumn
tRPOperCommunityMember = _TRPOperCommunityMember_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 4, 1, 2),
    _TRPOperCommunityMember_Type()
)
tRPOperCommunityMember.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperCommunityMember.setStatus("current")
_TRPOperCommunityRowStatus_Type = RowStatus
_TRPOperCommunityRowStatus_Object = MibTableColumn
tRPOperCommunityRowStatus = _TRPOperCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 4, 1, 3),
    _TRPOperCommunityRowStatus_Type()
)
tRPOperCommunityRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperCommunityRowStatus.setStatus("current")
_TRPOperCommunityEntryLastChanged_Type = TimeStamp
_TRPOperCommunityEntryLastChanged_Object = MibTableColumn
tRPOperCommunityEntryLastChanged = _TRPOperCommunityEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 4, 1, 4),
    _TRPOperCommunityEntryLastChanged_Type()
)
tRPOperCommunityEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperCommunityEntryLastChanged.setStatus("obsolete")
_TRPOperCommunityCreationOrigin_Type = TmnxCreateOrigin
_TRPOperCommunityCreationOrigin_Object = MibTableColumn
tRPOperCommunityCreationOrigin = _TRPOperCommunityCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 4, 1, 5),
    _TRPOperCommunityCreationOrigin_Type()
)
tRPOperCommunityCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperCommunityCreationOrigin.setStatus("current")
_TRPOperDampingTableLastChanged_Type = TimeStamp
_TRPOperDampingTableLastChanged_Object = MibScalar
tRPOperDampingTableLastChanged = _TRPOperDampingTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 5),
    _TRPOperDampingTableLastChanged_Type()
)
tRPOperDampingTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperDampingTableLastChanged.setStatus("obsolete")
_TRPOperDampingTable_Object = MibTable
tRPOperDampingTable = _TRPOperDampingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tRPOperDampingTable.setStatus("current")
_TRPOperDampingEntry_Object = MibTableRow
tRPOperDampingEntry = _TRPOperDampingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 6, 1)
)
tRPOperDampingEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingName"),
)
if mibBuilder.loadTexts:
    tRPOperDampingEntry.setStatus("current")


class _TRPOperDampingName_Type(TDampingName):
    """Custom type tRPOperDampingName based on TDampingName"""
    subtypeSpec = TDampingName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPOperDampingName_Type.__name__ = "TDampingName"
_TRPOperDampingName_Object = MibTableColumn
tRPOperDampingName = _TRPOperDampingName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 6, 1, 1),
    _TRPOperDampingName_Type()
)
tRPOperDampingName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperDampingName.setStatus("current")
_TRPOperDampingRowStatus_Type = RowStatus
_TRPOperDampingRowStatus_Object = MibTableColumn
tRPOperDampingRowStatus = _TRPOperDampingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 6, 1, 2),
    _TRPOperDampingRowStatus_Type()
)
tRPOperDampingRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperDampingRowStatus.setStatus("current")


class _TRPOperDampingHalfLife_Type(Unsigned32):
    """Custom type tRPOperDampingHalfLife based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45),
    )


_TRPOperDampingHalfLife_Type.__name__ = "Unsigned32"
_TRPOperDampingHalfLife_Object = MibTableColumn
tRPOperDampingHalfLife = _TRPOperDampingHalfLife_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 6, 1, 3),
    _TRPOperDampingHalfLife_Type()
)
tRPOperDampingHalfLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperDampingHalfLife.setStatus("current")
if mibBuilder.loadTexts:
    tRPOperDampingHalfLife.setUnits("minutes")


class _TRPOperDampingMaxSuppress_Type(Unsigned32):
    """Custom type tRPOperDampingMaxSuppress based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_TRPOperDampingMaxSuppress_Type.__name__ = "Unsigned32"
_TRPOperDampingMaxSuppress_Object = MibTableColumn
tRPOperDampingMaxSuppress = _TRPOperDampingMaxSuppress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 6, 1, 4),
    _TRPOperDampingMaxSuppress_Type()
)
tRPOperDampingMaxSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperDampingMaxSuppress.setStatus("current")
if mibBuilder.loadTexts:
    tRPOperDampingMaxSuppress.setUnits("minutes")


class _TRPOperDampingReuse_Type(Unsigned32):
    """Custom type tRPOperDampingReuse based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_TRPOperDampingReuse_Type.__name__ = "Unsigned32"
_TRPOperDampingReuse_Object = MibTableColumn
tRPOperDampingReuse = _TRPOperDampingReuse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 6, 1, 5),
    _TRPOperDampingReuse_Type()
)
tRPOperDampingReuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperDampingReuse.setStatus("current")


class _TRPOperDampingSuppress_Type(Unsigned32):
    """Custom type tRPOperDampingSuppress based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_TRPOperDampingSuppress_Type.__name__ = "Unsigned32"
_TRPOperDampingSuppress_Object = MibTableColumn
tRPOperDampingSuppress = _TRPOperDampingSuppress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 6, 1, 6),
    _TRPOperDampingSuppress_Type()
)
tRPOperDampingSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperDampingSuppress.setStatus("current")
_TRPOperDampingEntryLastChanged_Type = TimeStamp
_TRPOperDampingEntryLastChanged_Object = MibTableColumn
tRPOperDampingEntryLastChanged = _TRPOperDampingEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 6, 1, 7),
    _TRPOperDampingEntryLastChanged_Type()
)
tRPOperDampingEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperDampingEntryLastChanged.setStatus("obsolete")
_TRPOperPrefixListTableLastChanged_Type = TimeStamp
_TRPOperPrefixListTableLastChanged_Object = MibScalar
tRPOperPrefixListTableLastChanged = _TRPOperPrefixListTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 7),
    _TRPOperPrefixListTableLastChanged_Type()
)
tRPOperPrefixListTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPrefixListTableLastChanged.setStatus("obsolete")
_TRPOperPrefixListTable_Object = MibTable
tRPOperPrefixListTable = _TRPOperPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8)
)
if mibBuilder.loadTexts:
    tRPOperPrefixListTable.setStatus("current")
_TRPOperPrefixListEntry_Object = MibTableRow
tRPOperPrefixListEntry = _TRPOperPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8, 1)
)
tRPOperPrefixListEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListIpPrefix"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListMask"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListType"),
)
if mibBuilder.loadTexts:
    tRPOperPrefixListEntry.setStatus("current")


class _TRPOperPrefixListName_Type(TPrefixListName):
    """Custom type tRPOperPrefixListName based on TPrefixListName"""
    subtypeSpec = TPrefixListName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPOperPrefixListName_Type.__name__ = "TPrefixListName"
_TRPOperPrefixListName_Object = MibTableColumn
tRPOperPrefixListName = _TRPOperPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8, 1, 1),
    _TRPOperPrefixListName_Type()
)
tRPOperPrefixListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperPrefixListName.setStatus("current")
_TRPOperPrefixListIpPrefix_Type = IpAddress
_TRPOperPrefixListIpPrefix_Object = MibTableColumn
tRPOperPrefixListIpPrefix = _TRPOperPrefixListIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8, 1, 2),
    _TRPOperPrefixListIpPrefix_Type()
)
tRPOperPrefixListIpPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperPrefixListIpPrefix.setStatus("current")
_TRPOperPrefixListMask_Type = IpAddressPrefixLength
_TRPOperPrefixListMask_Object = MibTableColumn
tRPOperPrefixListMask = _TRPOperPrefixListMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8, 1, 3),
    _TRPOperPrefixListMask_Type()
)
tRPOperPrefixListMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperPrefixListMask.setStatus("current")
_TRPOperPrefixListRowStatus_Type = RowStatus
_TRPOperPrefixListRowStatus_Object = MibTableColumn
tRPOperPrefixListRowStatus = _TRPOperPrefixListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8, 1, 4),
    _TRPOperPrefixListRowStatus_Type()
)
tRPOperPrefixListRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPrefixListRowStatus.setStatus("current")


class _TRPOperPrefixListType_Type(Integer32):
    """Custom type tRPOperPrefixListType based on Integer32"""
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
        *(("exact", 1),
          ("longer", 2),
          ("through", 3),
          ("range", 4))
    )


_TRPOperPrefixListType_Type.__name__ = "Integer32"
_TRPOperPrefixListType_Object = MibTableColumn
tRPOperPrefixListType = _TRPOperPrefixListType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8, 1, 5),
    _TRPOperPrefixListType_Type()
)
tRPOperPrefixListType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperPrefixListType.setStatus("current")
_TRPOperPrefixListThroughLength_Type = IpAddressPrefixLength
_TRPOperPrefixListThroughLength_Object = MibTableColumn
tRPOperPrefixListThroughLength = _TRPOperPrefixListThroughLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8, 1, 6),
    _TRPOperPrefixListThroughLength_Type()
)
tRPOperPrefixListThroughLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPrefixListThroughLength.setStatus("current")
_TRPOperPrefixListEntryLastChanged_Type = TimeStamp
_TRPOperPrefixListEntryLastChanged_Object = MibTableColumn
tRPOperPrefixListEntryLastChanged = _TRPOperPrefixListEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8, 1, 7),
    _TRPOperPrefixListEntryLastChanged_Type()
)
tRPOperPrefixListEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPrefixListEntryLastChanged.setStatus("obsolete")
_TRPOperPrefixListBeginLength_Type = IpAddressPrefixLength
_TRPOperPrefixListBeginLength_Object = MibTableColumn
tRPOperPrefixListBeginLength = _TRPOperPrefixListBeginLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8, 1, 8),
    _TRPOperPrefixListBeginLength_Type()
)
tRPOperPrefixListBeginLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPrefixListBeginLength.setStatus("current")
_TRPOperPolicyStatementTableLastChanged_Type = TimeStamp
_TRPOperPolicyStatementTableLastChanged_Object = MibScalar
tRPOperPolicyStatementTableLastChanged = _TRPOperPolicyStatementTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 9),
    _TRPOperPolicyStatementTableLastChanged_Type()
)
tRPOperPolicyStatementTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPolicyStatementTableLastChanged.setStatus("obsolete")
_TRPOperPolicyStatementTable_Object = MibTable
tRPOperPolicyStatementTable = _TRPOperPolicyStatementTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 10)
)
if mibBuilder.loadTexts:
    tRPOperPolicyStatementTable.setStatus("current")
_TRPOperPolicyStatementEntry_Object = MibTableRow
tRPOperPolicyStatementEntry = _TRPOperPolicyStatementEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 10, 1)
)
tRPOperPolicyStatementEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementName"),
)
if mibBuilder.loadTexts:
    tRPOperPolicyStatementEntry.setStatus("current")
_TRPOperPolicyStatementName_Type = TPolicyStatementName
_TRPOperPolicyStatementName_Object = MibTableColumn
tRPOperPolicyStatementName = _TRPOperPolicyStatementName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 10, 1, 1),
    _TRPOperPolicyStatementName_Type()
)
tRPOperPolicyStatementName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperPolicyStatementName.setStatus("current")
_TRPOperPolicyStatementRowStatus_Type = RowStatus
_TRPOperPolicyStatementRowStatus_Object = MibTableColumn
tRPOperPolicyStatementRowStatus = _TRPOperPolicyStatementRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 10, 1, 2),
    _TRPOperPolicyStatementRowStatus_Type()
)
tRPOperPolicyStatementRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPolicyStatementRowStatus.setStatus("current")
_TRPOperPolicyStatementDescription_Type = TItemDescription
_TRPOperPolicyStatementDescription_Object = MibTableColumn
tRPOperPolicyStatementDescription = _TRPOperPolicyStatementDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 10, 1, 3),
    _TRPOperPolicyStatementDescription_Type()
)
tRPOperPolicyStatementDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPolicyStatementDescription.setStatus("current")
_TRPOperPolicyStatementDefaultAction_Type = TPolicyEntryAction
_TRPOperPolicyStatementDefaultAction_Object = MibTableColumn
tRPOperPolicyStatementDefaultAction = _TRPOperPolicyStatementDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 10, 1, 4),
    _TRPOperPolicyStatementDefaultAction_Type()
)
tRPOperPolicyStatementDefaultAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPolicyStatementDefaultAction.setStatus("current")
_TRPOperPolicyStatementEntryLastChanged_Type = TimeStamp
_TRPOperPolicyStatementEntryLastChanged_Object = MibTableColumn
tRPOperPolicyStatementEntryLastChanged = _TRPOperPolicyStatementEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 10, 1, 5),
    _TRPOperPolicyStatementEntryLastChanged_Type()
)
tRPOperPolicyStatementEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPolicyStatementEntryLastChanged.setStatus("obsolete")
_TRPOperPolicyStatementCrOrigin_Type = TmnxCreateOrigin
_TRPOperPolicyStatementCrOrigin_Object = MibTableColumn
tRPOperPolicyStatementCrOrigin = _TRPOperPolicyStatementCrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 10, 1, 6),
    _TRPOperPolicyStatementCrOrigin_Type()
)
tRPOperPolicyStatementCrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPolicyStatementCrOrigin.setStatus("current")
_TRPOperPSDefaultActionParamsTableLastChanged_Type = TimeStamp
_TRPOperPSDefaultActionParamsTableLastChanged_Object = MibScalar
tRPOperPSDefaultActionParamsTableLastChanged = _TRPOperPSDefaultActionParamsTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 11),
    _TRPOperPSDefaultActionParamsTableLastChanged_Type()
)
tRPOperPSDefaultActionParamsTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionParamsTableLastChanged.setStatus("obsolete")
_TRPOperPSDefaultActionParamsTable_Object = MibTable
tRPOperPSDefaultActionParamsTable = _TRPOperPSDefaultActionParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12)
)
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionParamsTable.setStatus("current")
_TRPOperPSDefaultActionParamsEntry_Object = MibTableRow
tRPOperPSDefaultActionParamsEntry = _TRPOperPSDefaultActionParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1)
)
tRPOperPSDefaultActionParamsEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementName"),
)
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionParamsEntry.setStatus("current")
_TRPOperPSDefaultActionASPath_Type = TPolicyEntryEdit
_TRPOperPSDefaultActionASPath_Object = MibTableColumn
tRPOperPSDefaultActionASPath = _TRPOperPSDefaultActionASPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 1),
    _TRPOperPSDefaultActionASPath_Type()
)
tRPOperPSDefaultActionASPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionASPath.setStatus("current")
_TRPOperPSDefaultActionASPathName_Type = TASPathName
_TRPOperPSDefaultActionASPathName_Object = MibTableColumn
tRPOperPSDefaultActionASPathName = _TRPOperPSDefaultActionASPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 2),
    _TRPOperPSDefaultActionASPathName_Type()
)
tRPOperPSDefaultActionASPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionASPathName.setStatus("current")
_TRPOperPSDefaultActionASPathPrependAS_Type = TmnxBgpAutonomousSystem
_TRPOperPSDefaultActionASPathPrependAS_Object = MibTableColumn
tRPOperPSDefaultActionASPathPrependAS = _TRPOperPSDefaultActionASPathPrependAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 3),
    _TRPOperPSDefaultActionASPathPrependAS_Type()
)
tRPOperPSDefaultActionASPathPrependAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionASPathPrependAS.setStatus("obsolete")


class _TRPOperPSDefaultActionASPathPrependCount_Type(Integer32):
    """Custom type tRPOperPSDefaultActionASPathPrependCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_TRPOperPSDefaultActionASPathPrependCount_Type.__name__ = "Integer32"
_TRPOperPSDefaultActionASPathPrependCount_Object = MibTableColumn
tRPOperPSDefaultActionASPathPrependCount = _TRPOperPSDefaultActionASPathPrependCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 4),
    _TRPOperPSDefaultActionASPathPrependCount_Type()
)
tRPOperPSDefaultActionASPathPrependCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionASPathPrependCount.setStatus("current")
_TRPOperPSDefaultActionCommunity1_Type = TPolicyEntryEdit
_TRPOperPSDefaultActionCommunity1_Object = MibTableColumn
tRPOperPSDefaultActionCommunity1 = _TRPOperPSDefaultActionCommunity1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 5),
    _TRPOperPSDefaultActionCommunity1_Type()
)
tRPOperPSDefaultActionCommunity1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionCommunity1.setStatus("obsolete")
_TRPOperPSDefaultActionCommunityName1_Type = TCommunityName
_TRPOperPSDefaultActionCommunityName1_Object = MibTableColumn
tRPOperPSDefaultActionCommunityName1 = _TRPOperPSDefaultActionCommunityName1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 6),
    _TRPOperPSDefaultActionCommunityName1_Type()
)
tRPOperPSDefaultActionCommunityName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionCommunityName1.setStatus("obsolete")
_TRPOperPSDefaultActionCommunity2_Type = TPolicyEntryEdit
_TRPOperPSDefaultActionCommunity2_Object = MibTableColumn
tRPOperPSDefaultActionCommunity2 = _TRPOperPSDefaultActionCommunity2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 7),
    _TRPOperPSDefaultActionCommunity2_Type()
)
tRPOperPSDefaultActionCommunity2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionCommunity2.setStatus("obsolete")
_TRPOperPSDefaultActionCommunityName2_Type = TCommunityName
_TRPOperPSDefaultActionCommunityName2_Object = MibTableColumn
tRPOperPSDefaultActionCommunityName2 = _TRPOperPSDefaultActionCommunityName2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 8),
    _TRPOperPSDefaultActionCommunityName2_Type()
)
tRPOperPSDefaultActionCommunityName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionCommunityName2.setStatus("obsolete")
_TRPOperPSDefaultActionOrigin_Type = TPolicyEntryCriteriaOrigin
_TRPOperPSDefaultActionOrigin_Object = MibTableColumn
tRPOperPSDefaultActionOrigin = _TRPOperPSDefaultActionOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 9),
    _TRPOperPSDefaultActionOrigin_Type()
)
tRPOperPSDefaultActionOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionOrigin.setStatus("current")
_TRPOperPSDefaultActionLocalPreferenceSet_Type = TruthValue
_TRPOperPSDefaultActionLocalPreferenceSet_Object = MibTableColumn
tRPOperPSDefaultActionLocalPreferenceSet = _TRPOperPSDefaultActionLocalPreferenceSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 10),
    _TRPOperPSDefaultActionLocalPreferenceSet_Type()
)
tRPOperPSDefaultActionLocalPreferenceSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionLocalPreferenceSet.setStatus("current")
_TRPOperPSDefaultActionLocalPreference_Type = TmnxBgpLocalPreference
_TRPOperPSDefaultActionLocalPreference_Object = MibTableColumn
tRPOperPSDefaultActionLocalPreference = _TRPOperPSDefaultActionLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 11),
    _TRPOperPSDefaultActionLocalPreference_Type()
)
tRPOperPSDefaultActionLocalPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionLocalPreference.setStatus("current")
_TRPOperPSDefaultActionMetric_Type = TPolicyEntryEdit
_TRPOperPSDefaultActionMetric_Object = MibTableColumn
tRPOperPSDefaultActionMetric = _TRPOperPSDefaultActionMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 12),
    _TRPOperPSDefaultActionMetric_Type()
)
tRPOperPSDefaultActionMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionMetric.setStatus("current")
_TRPOperPSDefaultActionMetricValue_Type = Unsigned32
_TRPOperPSDefaultActionMetricValue_Object = MibTableColumn
tRPOperPSDefaultActionMetricValue = _TRPOperPSDefaultActionMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 13),
    _TRPOperPSDefaultActionMetricValue_Type()
)
tRPOperPSDefaultActionMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionMetricValue.setStatus("current")
_TRPOperPSDefaultActionPreference_Type = TmnxBgpPreference
_TRPOperPSDefaultActionPreference_Object = MibTableColumn
tRPOperPSDefaultActionPreference = _TRPOperPSDefaultActionPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 15),
    _TRPOperPSDefaultActionPreference_Type()
)
tRPOperPSDefaultActionPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionPreference.setStatus("current")
_TRPOperPSDefaultActionDamping_Type = TDampingName
_TRPOperPSDefaultActionDamping_Object = MibTableColumn
tRPOperPSDefaultActionDamping = _TRPOperPSDefaultActionDamping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 16),
    _TRPOperPSDefaultActionDamping_Type()
)
tRPOperPSDefaultActionDamping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionDamping.setStatus("current")
_TRPOperPSDefaultActionNextHopSelf_Type = TruthValue
_TRPOperPSDefaultActionNextHopSelf_Object = MibTableColumn
tRPOperPSDefaultActionNextHopSelf = _TRPOperPSDefaultActionNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 17),
    _TRPOperPSDefaultActionNextHopSelf_Type()
)
tRPOperPSDefaultActionNextHopSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionNextHopSelf.setStatus("current")
_TRPOperPSDefaultActionNextHop_Type = IpAddress
_TRPOperPSDefaultActionNextHop_Object = MibTableColumn
tRPOperPSDefaultActionNextHop = _TRPOperPSDefaultActionNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 18),
    _TRPOperPSDefaultActionNextHop_Type()
)
tRPOperPSDefaultActionNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionNextHop.setStatus("current")
_TRPOperPSDefaultActionTag_Type = TPolicyActionTag
_TRPOperPSDefaultActionTag_Object = MibTableColumn
tRPOperPSDefaultActionTag = _TRPOperPSDefaultActionTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 19),
    _TRPOperPSDefaultActionTag_Type()
)
tRPOperPSDefaultActionTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionTag.setStatus("current")
_TRPOperPSDefaultActionOspfType_Type = TOspfRouteType
_TRPOperPSDefaultActionOspfType_Object = MibTableColumn
tRPOperPSDefaultActionOspfType = _TRPOperPSDefaultActionOspfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 20),
    _TRPOperPSDefaultActionOspfType_Type()
)
tRPOperPSDefaultActionOspfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionOspfType.setStatus("current")
_TRPOperPSDefaultActionParamsEntryLastChanged_Type = TimeStamp
_TRPOperPSDefaultActionParamsEntryLastChanged_Object = MibTableColumn
tRPOperPSDefaultActionParamsEntryLastChanged = _TRPOperPSDefaultActionParamsEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 21),
    _TRPOperPSDefaultActionParamsEntryLastChanged_Type()
)
tRPOperPSDefaultActionParamsEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionParamsEntryLastChanged.setStatus("obsolete")
_TRPOperPSDefActInetNextHopType_Type = InetAddressType
_TRPOperPSDefActInetNextHopType_Object = MibTableColumn
tRPOperPSDefActInetNextHopType = _TRPOperPSDefActInetNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 22),
    _TRPOperPSDefActInetNextHopType_Type()
)
tRPOperPSDefActInetNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActInetNextHopType.setStatus("current")


class _TRPOperPSDefActInetNextHop_Type(InetAddress):
    """Custom type tRPOperPSDefActInetNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TRPOperPSDefActInetNextHop_Type.__name__ = "InetAddress"
_TRPOperPSDefActInetNextHop_Object = MibTableColumn
tRPOperPSDefActInetNextHop = _TRPOperPSDefActInetNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 23),
    _TRPOperPSDefActInetNextHop_Type()
)
tRPOperPSDefActInetNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActInetNextHop.setStatus("current")
_TRPOperPSDefaultActionASPathPend_Type = InetAutonomousSystemNumber
_TRPOperPSDefaultActionASPathPend_Object = MibTableColumn
tRPOperPSDefaultActionASPathPend = _TRPOperPSDefaultActionASPathPend_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 24),
    _TRPOperPSDefaultActionASPathPend_Type()
)
tRPOperPSDefaultActionASPathPend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionASPathPend.setStatus("current")
_TRPOperPSDefActMcRedirSvcId_Type = TmnxServId
_TRPOperPSDefActMcRedirSvcId_Object = MibTableColumn
tRPOperPSDefActMcRedirSvcId = _TRPOperPSDefActMcRedirSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 30),
    _TRPOperPSDefActMcRedirSvcId_Type()
)
tRPOperPSDefActMcRedirSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActMcRedirSvcId.setStatus("current")
_TRPOperPSDefActMcRedirIfIndex_Type = InterfaceIndexOrZero
_TRPOperPSDefActMcRedirIfIndex_Object = MibTableColumn
tRPOperPSDefActMcRedirIfIndex = _TRPOperPSDefActMcRedirIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 31),
    _TRPOperPSDefActMcRedirIfIndex_Type()
)
tRPOperPSDefActMcRedirIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActMcRedirIfIndex.setStatus("current")
_TRPOperPSDefActionMetricSource_Type = TPolicyActionMetricSource
_TRPOperPSDefActionMetricSource_Object = MibTableColumn
tRPOperPSDefActionMetricSource = _TRPOperPSDefActionMetricSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 32),
    _TRPOperPSDefActionMetricSource_Type()
)
tRPOperPSDefActionMetricSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionMetricSource.setStatus("current")
_TRPOperPSDefActionAigpMetric_Type = TPolicyEntryAigpMetricEdit
_TRPOperPSDefActionAigpMetric_Object = MibTableColumn
tRPOperPSDefActionAigpMetric = _TRPOperPSDefActionAigpMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 33),
    _TRPOperPSDefActionAigpMetric_Type()
)
tRPOperPSDefActionAigpMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAigpMetric.setStatus("current")
_TRPOperPSDefActnAigpMetricVal_Type = Unsigned32
_TRPOperPSDefActnAigpMetricVal_Object = MibTableColumn
tRPOperPSDefActnAigpMetricVal = _TRPOperPSDefActnAigpMetricVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 34),
    _TRPOperPSDefActnAigpMetricVal_Type()
)
tRPOperPSDefActnAigpMetricVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActnAigpMetricVal.setStatus("current")


class _TRPOperPSDefActnSrcClassIndex_Type(Unsigned32):
    """Custom type tRPOperPSDefActnSrcClassIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TRPOperPSDefActnSrcClassIndex_Type.__name__ = "Unsigned32"
_TRPOperPSDefActnSrcClassIndex_Object = MibTableColumn
tRPOperPSDefActnSrcClassIndex = _TRPOperPSDefActnSrcClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 35),
    _TRPOperPSDefActnSrcClassIndex_Type()
)
tRPOperPSDefActnSrcClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActnSrcClassIndex.setStatus("current")


class _TRPOperPSDefActnDstClassIndex_Type(Unsigned32):
    """Custom type tRPOperPSDefActnDstClassIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TRPOperPSDefActnDstClassIndex_Type.__name__ = "Unsigned32"
_TRPOperPSDefActnDstClassIndex_Object = MibTableColumn
tRPOperPSDefActnDstClassIndex = _TRPOperPSDefActnDstClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 36),
    _TRPOperPSDefActnDstClassIndex_Type()
)
tRPOperPSDefActnDstClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActnDstClassIndex.setStatus("current")


class _TRPOperPSDefActnOrigValidState_Type(Integer32):
    """Custom type tRPOperPSDefActnOrigValidState based on Integer32"""
    defaultValue = 0

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
        *(("notApplicable", 0),
          ("valid", 1),
          ("notFound", 2),
          ("invalid", 3))
    )


_TRPOperPSDefActnOrigValidState_Type.__name__ = "Integer32"
_TRPOperPSDefActnOrigValidState_Object = MibTableColumn
tRPOperPSDefActnOrigValidState = _TRPOperPSDefActnOrigValidState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 37),
    _TRPOperPSDefActnOrigValidState_Type()
)
tRPOperPSDefActnOrigValidState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActnOrigValidState.setStatus("current")
_TRPOperPSParamsTableLastChanged_Type = TimeStamp
_TRPOperPSParamsTableLastChanged_Object = MibScalar
tRPOperPSParamsTableLastChanged = _TRPOperPSParamsTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 13),
    _TRPOperPSParamsTableLastChanged_Type()
)
tRPOperPSParamsTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSParamsTableLastChanged.setStatus("obsolete")
_TRPOperPSParamsTable_Object = MibTable
tRPOperPSParamsTable = _TRPOperPSParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 14)
)
if mibBuilder.loadTexts:
    tRPOperPSParamsTable.setStatus("current")
_TRPOperPSParamsEntry_Object = MibTableRow
tRPOperPSParamsEntry = _TRPOperPSParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 14, 1)
)
tRPOperPSParamsEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSNameEntryIndex"),
)
if mibBuilder.loadTexts:
    tRPOperPSParamsEntry.setStatus("current")
_TRPOperPSNameEntryIndex_Type = TPolicyStatementEntryID
_TRPOperPSNameEntryIndex_Object = MibTableColumn
tRPOperPSNameEntryIndex = _TRPOperPSNameEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 14, 1, 1),
    _TRPOperPSNameEntryIndex_Type()
)
tRPOperPSNameEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperPSNameEntryIndex.setStatus("current")
_TRPOperPSParamsRowStatus_Type = RowStatus
_TRPOperPSParamsRowStatus_Object = MibTableColumn
tRPOperPSParamsRowStatus = _TRPOperPSParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 14, 1, 2),
    _TRPOperPSParamsRowStatus_Type()
)
tRPOperPSParamsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSParamsRowStatus.setStatus("current")
_TRPOperPSParamsDescription_Type = TItemDescription
_TRPOperPSParamsDescription_Object = MibTableColumn
tRPOperPSParamsDescription = _TRPOperPSParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 14, 1, 3),
    _TRPOperPSParamsDescription_Type()
)
tRPOperPSParamsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSParamsDescription.setStatus("current")
_TRPOperPSParamsAction_Type = TPolicyEntryAction
_TRPOperPSParamsAction_Object = MibTableColumn
tRPOperPSParamsAction = _TRPOperPSParamsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 14, 1, 4),
    _TRPOperPSParamsAction_Type()
)
tRPOperPSParamsAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSParamsAction.setStatus("current")
_TRPOperPSParamsEntryLastChanged_Type = TimeStamp
_TRPOperPSParamsEntryLastChanged_Object = MibTableColumn
tRPOperPSParamsEntryLastChanged = _TRPOperPSParamsEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 14, 1, 5),
    _TRPOperPSParamsEntryLastChanged_Type()
)
tRPOperPSParamsEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSParamsEntryLastChanged.setStatus("obsolete")
_TRPOperPSParamsCreationOrigin_Type = TmnxCreateOrigin
_TRPOperPSParamsCreationOrigin_Object = MibTableColumn
tRPOperPSParamsCreationOrigin = _TRPOperPSParamsCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 14, 1, 6),
    _TRPOperPSParamsCreationOrigin_Type()
)
tRPOperPSParamsCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSParamsCreationOrigin.setStatus("current")
_TRPOperPSAcceptActionParamsTableLastChanged_Type = TimeStamp
_TRPOperPSAcceptActionParamsTableLastChanged_Object = MibScalar
tRPOperPSAcceptActionParamsTableLastChanged = _TRPOperPSAcceptActionParamsTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 15),
    _TRPOperPSAcceptActionParamsTableLastChanged_Type()
)
tRPOperPSAcceptActionParamsTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionParamsTableLastChanged.setStatus("obsolete")
_TRPOperPSAcceptActionParamsTable_Object = MibTable
tRPOperPSAcceptActionParamsTable = _TRPOperPSAcceptActionParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16)
)
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionParamsTable.setStatus("current")
_TRPOperPSAcceptActionParamsEntry_Object = MibTableRow
tRPOperPSAcceptActionParamsEntry = _TRPOperPSAcceptActionParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1)
)
tRPOperPSAcceptActionParamsEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSNameEntryIndex"),
)
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionParamsEntry.setStatus("current")
_TRPOperPSAcceptActionASPath_Type = TPolicyEntryEdit
_TRPOperPSAcceptActionASPath_Object = MibTableColumn
tRPOperPSAcceptActionASPath = _TRPOperPSAcceptActionASPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 1),
    _TRPOperPSAcceptActionASPath_Type()
)
tRPOperPSAcceptActionASPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionASPath.setStatus("current")
_TRPOperPSAcceptActionASPathName_Type = TASPathName
_TRPOperPSAcceptActionASPathName_Object = MibTableColumn
tRPOperPSAcceptActionASPathName = _TRPOperPSAcceptActionASPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 2),
    _TRPOperPSAcceptActionASPathName_Type()
)
tRPOperPSAcceptActionASPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionASPathName.setStatus("current")
_TRPOperPSAcceptActionASPathPrependAS_Type = TmnxBgpAutonomousSystem
_TRPOperPSAcceptActionASPathPrependAS_Object = MibTableColumn
tRPOperPSAcceptActionASPathPrependAS = _TRPOperPSAcceptActionASPathPrependAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 3),
    _TRPOperPSAcceptActionASPathPrependAS_Type()
)
tRPOperPSAcceptActionASPathPrependAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionASPathPrependAS.setStatus("obsolete")


class _TRPOperPSAcceptActionASPathPrependCount_Type(Integer32):
    """Custom type tRPOperPSAcceptActionASPathPrependCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_TRPOperPSAcceptActionASPathPrependCount_Type.__name__ = "Integer32"
_TRPOperPSAcceptActionASPathPrependCount_Object = MibTableColumn
tRPOperPSAcceptActionASPathPrependCount = _TRPOperPSAcceptActionASPathPrependCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 4),
    _TRPOperPSAcceptActionASPathPrependCount_Type()
)
tRPOperPSAcceptActionASPathPrependCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionASPathPrependCount.setStatus("current")
_TRPOperPSAcceptActionCommunity1_Type = TPolicyEntryEdit
_TRPOperPSAcceptActionCommunity1_Object = MibTableColumn
tRPOperPSAcceptActionCommunity1 = _TRPOperPSAcceptActionCommunity1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 5),
    _TRPOperPSAcceptActionCommunity1_Type()
)
tRPOperPSAcceptActionCommunity1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionCommunity1.setStatus("obsolete")
_TRPOperPSAcceptActionCommunityName1_Type = TCommunityName
_TRPOperPSAcceptActionCommunityName1_Object = MibTableColumn
tRPOperPSAcceptActionCommunityName1 = _TRPOperPSAcceptActionCommunityName1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 6),
    _TRPOperPSAcceptActionCommunityName1_Type()
)
tRPOperPSAcceptActionCommunityName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionCommunityName1.setStatus("obsolete")
_TRPOperPSAcceptActionCommunity2_Type = TPolicyEntryEdit
_TRPOperPSAcceptActionCommunity2_Object = MibTableColumn
tRPOperPSAcceptActionCommunity2 = _TRPOperPSAcceptActionCommunity2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 7),
    _TRPOperPSAcceptActionCommunity2_Type()
)
tRPOperPSAcceptActionCommunity2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionCommunity2.setStatus("obsolete")
_TRPOperPSAcceptActionCommunityName2_Type = TCommunityName
_TRPOperPSAcceptActionCommunityName2_Object = MibTableColumn
tRPOperPSAcceptActionCommunityName2 = _TRPOperPSAcceptActionCommunityName2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 8),
    _TRPOperPSAcceptActionCommunityName2_Type()
)
tRPOperPSAcceptActionCommunityName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionCommunityName2.setStatus("obsolete")
_TRPOperPSAcceptActionOrigin_Type = TPolicyEntryCriteriaOrigin
_TRPOperPSAcceptActionOrigin_Object = MibTableColumn
tRPOperPSAcceptActionOrigin = _TRPOperPSAcceptActionOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 9),
    _TRPOperPSAcceptActionOrigin_Type()
)
tRPOperPSAcceptActionOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionOrigin.setStatus("current")
_TRPOperPSAcceptActionLocalPreferenceSet_Type = TruthValue
_TRPOperPSAcceptActionLocalPreferenceSet_Object = MibTableColumn
tRPOperPSAcceptActionLocalPreferenceSet = _TRPOperPSAcceptActionLocalPreferenceSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 10),
    _TRPOperPSAcceptActionLocalPreferenceSet_Type()
)
tRPOperPSAcceptActionLocalPreferenceSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionLocalPreferenceSet.setStatus("current")
_TRPOperPSAcceptActionLocalPreference_Type = TmnxBgpLocalPreference
_TRPOperPSAcceptActionLocalPreference_Object = MibTableColumn
tRPOperPSAcceptActionLocalPreference = _TRPOperPSAcceptActionLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 11),
    _TRPOperPSAcceptActionLocalPreference_Type()
)
tRPOperPSAcceptActionLocalPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionLocalPreference.setStatus("current")
_TRPOperPSAcceptActionMetric_Type = TPolicyEntryEdit
_TRPOperPSAcceptActionMetric_Object = MibTableColumn
tRPOperPSAcceptActionMetric = _TRPOperPSAcceptActionMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 12),
    _TRPOperPSAcceptActionMetric_Type()
)
tRPOperPSAcceptActionMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionMetric.setStatus("current")
_TRPOperPSAcceptActionMetricValue_Type = Unsigned32
_TRPOperPSAcceptActionMetricValue_Object = MibTableColumn
tRPOperPSAcceptActionMetricValue = _TRPOperPSAcceptActionMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 13),
    _TRPOperPSAcceptActionMetricValue_Type()
)
tRPOperPSAcceptActionMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionMetricValue.setStatus("current")
_TRPOperPSAcceptActionPreference_Type = TmnxBgpPreference
_TRPOperPSAcceptActionPreference_Object = MibTableColumn
tRPOperPSAcceptActionPreference = _TRPOperPSAcceptActionPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 15),
    _TRPOperPSAcceptActionPreference_Type()
)
tRPOperPSAcceptActionPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionPreference.setStatus("current")
_TRPOperPSAcceptActionDamping_Type = TDampingName
_TRPOperPSAcceptActionDamping_Object = MibTableColumn
tRPOperPSAcceptActionDamping = _TRPOperPSAcceptActionDamping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 16),
    _TRPOperPSAcceptActionDamping_Type()
)
tRPOperPSAcceptActionDamping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionDamping.setStatus("current")
_TRPOperPSAcceptActionNextHopSelf_Type = TruthValue
_TRPOperPSAcceptActionNextHopSelf_Object = MibTableColumn
tRPOperPSAcceptActionNextHopSelf = _TRPOperPSAcceptActionNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 17),
    _TRPOperPSAcceptActionNextHopSelf_Type()
)
tRPOperPSAcceptActionNextHopSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionNextHopSelf.setStatus("current")
_TRPOperPSAcceptActionNextHop_Type = IpAddress
_TRPOperPSAcceptActionNextHop_Object = MibTableColumn
tRPOperPSAcceptActionNextHop = _TRPOperPSAcceptActionNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 18),
    _TRPOperPSAcceptActionNextHop_Type()
)
tRPOperPSAcceptActionNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionNextHop.setStatus("current")
_TRPOperPSAcceptActionTag_Type = TPolicyActionTag
_TRPOperPSAcceptActionTag_Object = MibTableColumn
tRPOperPSAcceptActionTag = _TRPOperPSAcceptActionTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 19),
    _TRPOperPSAcceptActionTag_Type()
)
tRPOperPSAcceptActionTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionTag.setStatus("current")
_TRPOperPSAcceptActionOspfType_Type = TOspfRouteType
_TRPOperPSAcceptActionOspfType_Object = MibTableColumn
tRPOperPSAcceptActionOspfType = _TRPOperPSAcceptActionOspfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 20),
    _TRPOperPSAcceptActionOspfType_Type()
)
tRPOperPSAcceptActionOspfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionOspfType.setStatus("current")
_TRPOperPSAcceptActionParamsEntryLastChanged_Type = TimeStamp
_TRPOperPSAcceptActionParamsEntryLastChanged_Object = MibTableColumn
tRPOperPSAcceptActionParamsEntryLastChanged = _TRPOperPSAcceptActionParamsEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 21),
    _TRPOperPSAcceptActionParamsEntryLastChanged_Type()
)
tRPOperPSAcceptActionParamsEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionParamsEntryLastChanged.setStatus("obsolete")
_TRPOperPSAcptActInetNextHopType_Type = InetAddressType
_TRPOperPSAcptActInetNextHopType_Object = MibTableColumn
tRPOperPSAcptActInetNextHopType = _TRPOperPSAcptActInetNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 22),
    _TRPOperPSAcptActInetNextHopType_Type()
)
tRPOperPSAcptActInetNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActInetNextHopType.setStatus("current")


class _TRPOperPSAcptActInetNextHop_Type(InetAddress):
    """Custom type tRPOperPSAcptActInetNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TRPOperPSAcptActInetNextHop_Type.__name__ = "InetAddress"
_TRPOperPSAcptActInetNextHop_Object = MibTableColumn
tRPOperPSAcptActInetNextHop = _TRPOperPSAcptActInetNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 23),
    _TRPOperPSAcptActInetNextHop_Type()
)
tRPOperPSAcptActInetNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActInetNextHop.setStatus("current")
_TRPOperPSAcceptActionASPathPend_Type = InetAutonomousSystemNumber
_TRPOperPSAcceptActionASPathPend_Object = MibTableColumn
tRPOperPSAcceptActionASPathPend = _TRPOperPSAcceptActionASPathPend_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 24),
    _TRPOperPSAcceptActionASPathPend_Type()
)
tRPOperPSAcceptActionASPathPend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionASPathPend.setStatus("current")
_TRPOperPSAcceptActionFC_Type = TNamedItemOrEmpty
_TRPOperPSAcceptActionFC_Object = MibTableColumn
tRPOperPSAcceptActionFC = _TRPOperPSAcceptActionFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 25),
    _TRPOperPSAcceptActionFC_Type()
)
tRPOperPSAcceptActionFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionFC.setStatus("current")
_TRPOperPSAcceptActionFCPriority_Type = TPriorityOrUndefined
_TRPOperPSAcceptActionFCPriority_Object = MibTableColumn
tRPOperPSAcceptActionFCPriority = _TRPOperPSAcceptActionFCPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 26),
    _TRPOperPSAcceptActionFCPriority_Type()
)
tRPOperPSAcceptActionFCPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionFCPriority.setStatus("current")


class _TRPOperPSAcptActMcRedirSvcId_Type(TmnxServId):
    """Custom type tRPOperPSAcptActMcRedirSvcId based on TmnxServId"""
    defaultValue = 0


_TRPOperPSAcptActMcRedirSvcId_Type.__name__ = "TmnxServId"
_TRPOperPSAcptActMcRedirSvcId_Object = MibTableColumn
tRPOperPSAcptActMcRedirSvcId = _TRPOperPSAcptActMcRedirSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 30),
    _TRPOperPSAcptActMcRedirSvcId_Type()
)
tRPOperPSAcptActMcRedirSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActMcRedirSvcId.setStatus("current")


class _TRPOperPSAcptActMcRedirIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tRPOperPSAcptActMcRedirIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TRPOperPSAcptActMcRedirIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TRPOperPSAcptActMcRedirIfIndex_Object = MibTableColumn
tRPOperPSAcptActMcRedirIfIndex = _TRPOperPSAcptActMcRedirIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 31),
    _TRPOperPSAcptActMcRedirIfIndex_Type()
)
tRPOperPSAcptActMcRedirIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActMcRedirIfIndex.setStatus("current")


class _TRPOperPSAcptActnMetricSource_Type(TPolicyActionMetricSource):
    """Custom type tRPOperPSAcptActnMetricSource based on TPolicyActionMetricSource"""
    defaultValue = 2


_TRPOperPSAcptActnMetricSource_Type.__name__ = "TPolicyActionMetricSource"
_TRPOperPSAcptActnMetricSource_Object = MibTableColumn
tRPOperPSAcptActnMetricSource = _TRPOperPSAcptActnMetricSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 32),
    _TRPOperPSAcptActnMetricSource_Type()
)
tRPOperPSAcptActnMetricSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActnMetricSource.setStatus("current")
_TRPOperPSAcptActionAigpMetric_Type = TPolicyEntryAigpMetricEdit
_TRPOperPSAcptActionAigpMetric_Object = MibTableColumn
tRPOperPSAcptActionAigpMetric = _TRPOperPSAcptActionAigpMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 33),
    _TRPOperPSAcptActionAigpMetric_Type()
)
tRPOperPSAcptActionAigpMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActionAigpMetric.setStatus("current")
_TRPOperPSAcptActnAigpMetricVal_Type = Unsigned32
_TRPOperPSAcptActnAigpMetricVal_Object = MibTableColumn
tRPOperPSAcptActnAigpMetricVal = _TRPOperPSAcptActnAigpMetricVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 34),
    _TRPOperPSAcptActnAigpMetricVal_Type()
)
tRPOperPSAcptActnAigpMetricVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActnAigpMetricVal.setStatus("current")


class _TRPOperPSAcptActnSrcClassIndex_Type(Unsigned32):
    """Custom type tRPOperPSAcptActnSrcClassIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TRPOperPSAcptActnSrcClassIndex_Type.__name__ = "Unsigned32"
_TRPOperPSAcptActnSrcClassIndex_Object = MibTableColumn
tRPOperPSAcptActnSrcClassIndex = _TRPOperPSAcptActnSrcClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 35),
    _TRPOperPSAcptActnSrcClassIndex_Type()
)
tRPOperPSAcptActnSrcClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActnSrcClassIndex.setStatus("current")


class _TRPOperPSAcptActnDstClassIndex_Type(Unsigned32):
    """Custom type tRPOperPSAcptActnDstClassIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TRPOperPSAcptActnDstClassIndex_Type.__name__ = "Unsigned32"
_TRPOperPSAcptActnDstClassIndex_Object = MibTableColumn
tRPOperPSAcptActnDstClassIndex = _TRPOperPSAcptActnDstClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 36),
    _TRPOperPSAcptActnDstClassIndex_Type()
)
tRPOperPSAcptActnDstClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActnDstClassIndex.setStatus("current")


class _TRPOperPSAcptActnOrigValidState_Type(Integer32):
    """Custom type tRPOperPSAcptActnOrigValidState based on Integer32"""
    defaultValue = 0

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
        *(("notApplicable", 0),
          ("valid", 1),
          ("notFound", 2),
          ("invalid", 3))
    )


_TRPOperPSAcptActnOrigValidState_Type.__name__ = "Integer32"
_TRPOperPSAcptActnOrigValidState_Object = MibTableColumn
tRPOperPSAcptActnOrigValidState = _TRPOperPSAcptActnOrigValidState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 37),
    _TRPOperPSAcptActnOrigValidState_Type()
)
tRPOperPSAcptActnOrigValidState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActnOrigValidState.setStatus("current")
_TRPOperPSToCriteriaTableLastChanged_Type = TimeStamp
_TRPOperPSToCriteriaTableLastChanged_Object = MibScalar
tRPOperPSToCriteriaTableLastChanged = _TRPOperPSToCriteriaTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 17),
    _TRPOperPSToCriteriaTableLastChanged_Type()
)
tRPOperPSToCriteriaTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaTableLastChanged.setStatus("obsolete")
_TRPOperPSToCriteriaTable_Object = MibTable
tRPOperPSToCriteriaTable = _TRPOperPSToCriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18)
)
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaTable.setStatus("current")
_TRPOperPSToCriteriaEntry_Object = MibTableRow
tRPOperPSToCriteriaEntry = _TRPOperPSToCriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1)
)
tRPOperPSToCriteriaEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaIndex"),
)
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaEntry.setStatus("current")
_TRPOperPSToCriteriaIndex_Type = TPolicyStatementEntryID
_TRPOperPSToCriteriaIndex_Object = MibTableColumn
tRPOperPSToCriteriaIndex = _TRPOperPSToCriteriaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 1),
    _TRPOperPSToCriteriaIndex_Type()
)
tRPOperPSToCriteriaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaIndex.setStatus("current")
_TRPOperPSToCriteriaRowStatus_Type = RowStatus
_TRPOperPSToCriteriaRowStatus_Object = MibTableColumn
tRPOperPSToCriteriaRowStatus = _TRPOperPSToCriteriaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 2),
    _TRPOperPSToCriteriaRowStatus_Type()
)
tRPOperPSToCriteriaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaRowStatus.setStatus("current")
_TRPOperPSToCriteriaProtocol_Type = TRoutePolicyProtocol
_TRPOperPSToCriteriaProtocol_Object = MibTableColumn
tRPOperPSToCriteriaProtocol = _TRPOperPSToCriteriaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 3),
    _TRPOperPSToCriteriaProtocol_Type()
)
tRPOperPSToCriteriaProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaProtocol.setStatus("current")
_TRPOperPSToCriteriaNeighborIpAddr_Type = IpAddress
_TRPOperPSToCriteriaNeighborIpAddr_Object = MibTableColumn
tRPOperPSToCriteriaNeighborIpAddr = _TRPOperPSToCriteriaNeighborIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 4),
    _TRPOperPSToCriteriaNeighborIpAddr_Type()
)
tRPOperPSToCriteriaNeighborIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaNeighborIpAddr.setStatus("current")
_TRPOperPSToCriteriaNeighborPrefixList_Type = TPrefixListName
_TRPOperPSToCriteriaNeighborPrefixList_Object = MibTableColumn
tRPOperPSToCriteriaNeighborPrefixList = _TRPOperPSToCriteriaNeighborPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 5),
    _TRPOperPSToCriteriaNeighborPrefixList_Type()
)
tRPOperPSToCriteriaNeighborPrefixList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaNeighborPrefixList.setStatus("current")
_TRPOperPSToCriteriaEntryLastChanged_Type = TimeStamp
_TRPOperPSToCriteriaEntryLastChanged_Object = MibTableColumn
tRPOperPSToCriteriaEntryLastChanged = _TRPOperPSToCriteriaEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 6),
    _TRPOperPSToCriteriaEntryLastChanged_Type()
)
tRPOperPSToCriteriaEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaEntryLastChanged.setStatus("obsolete")
_TRPOperPSToCriteriaIsisLevel_Type = TIsisLevel
_TRPOperPSToCriteriaIsisLevel_Object = MibTableColumn
tRPOperPSToCriteriaIsisLevel = _TRPOperPSToCriteriaIsisLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 7),
    _TRPOperPSToCriteriaIsisLevel_Type()
)
tRPOperPSToCriteriaIsisLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaIsisLevel.setStatus("current")
_TRPOperPSToCriteriaPrefixList1_Type = TPrefixListName
_TRPOperPSToCriteriaPrefixList1_Object = MibTableColumn
tRPOperPSToCriteriaPrefixList1 = _TRPOperPSToCriteriaPrefixList1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 8),
    _TRPOperPSToCriteriaPrefixList1_Type()
)
tRPOperPSToCriteriaPrefixList1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaPrefixList1.setStatus("current")
_TRPOperPSToCriteriaPrefixList2_Type = TPrefixListName
_TRPOperPSToCriteriaPrefixList2_Object = MibTableColumn
tRPOperPSToCriteriaPrefixList2 = _TRPOperPSToCriteriaPrefixList2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 9),
    _TRPOperPSToCriteriaPrefixList2_Type()
)
tRPOperPSToCriteriaPrefixList2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaPrefixList2.setStatus("current")
_TRPOperPSToCriteriaPrefixList3_Type = TPrefixListName
_TRPOperPSToCriteriaPrefixList3_Object = MibTableColumn
tRPOperPSToCriteriaPrefixList3 = _TRPOperPSToCriteriaPrefixList3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 10),
    _TRPOperPSToCriteriaPrefixList3_Type()
)
tRPOperPSToCriteriaPrefixList3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaPrefixList3.setStatus("current")
_TRPOperPSToCriteriaPrefixList4_Type = TPrefixListName
_TRPOperPSToCriteriaPrefixList4_Object = MibTableColumn
tRPOperPSToCriteriaPrefixList4 = _TRPOperPSToCriteriaPrefixList4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 11),
    _TRPOperPSToCriteriaPrefixList4_Type()
)
tRPOperPSToCriteriaPrefixList4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaPrefixList4.setStatus("current")
_TRPOperPSToCriteriaPrefixList5_Type = TPrefixListName
_TRPOperPSToCriteriaPrefixList5_Object = MibTableColumn
tRPOperPSToCriteriaPrefixList5 = _TRPOperPSToCriteriaPrefixList5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 12),
    _TRPOperPSToCriteriaPrefixList5_Type()
)
tRPOperPSToCriteriaPrefixList5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaPrefixList5.setStatus("current")
_TRPOperPSToCritNbrInetAddrType_Type = InetAddressType
_TRPOperPSToCritNbrInetAddrType_Object = MibTableColumn
tRPOperPSToCritNbrInetAddrType = _TRPOperPSToCritNbrInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 13),
    _TRPOperPSToCritNbrInetAddrType_Type()
)
tRPOperPSToCritNbrInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCritNbrInetAddrType.setStatus("current")


class _TRPOperPSToCritNbrInetAddr_Type(InetAddress):
    """Custom type tRPOperPSToCritNbrInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TRPOperPSToCritNbrInetAddr_Type.__name__ = "InetAddress"
_TRPOperPSToCritNbrInetAddr_Object = MibTableColumn
tRPOperPSToCritNbrInetAddr = _TRPOperPSToCritNbrInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 14),
    _TRPOperPSToCritNbrInetAddr_Type()
)
tRPOperPSToCritNbrInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCritNbrInetAddr.setStatus("current")


class _TRPOperPSToCriteriaInstanceId_Type(Unsigned32):
    """Custom type tRPOperPSToCriteriaInstanceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
        ValueRangeConstraint(64, 95),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TRPOperPSToCriteriaInstanceId_Type.__name__ = "Unsigned32"
_TRPOperPSToCriteriaInstanceId_Object = MibTableColumn
tRPOperPSToCriteriaInstanceId = _TRPOperPSToCriteriaInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 15),
    _TRPOperPSToCriteriaInstanceId_Type()
)
tRPOperPSToCriteriaInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaInstanceId.setStatus("current")
_TRPOperPSFromCriteriaTableLastChanged_Type = TimeStamp
_TRPOperPSFromCriteriaTableLastChanged_Object = MibScalar
tRPOperPSFromCriteriaTableLastChanged = _TRPOperPSFromCriteriaTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 19),
    _TRPOperPSFromCriteriaTableLastChanged_Type()
)
tRPOperPSFromCriteriaTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaTableLastChanged.setStatus("obsolete")
_TRPOperPSFromCriteriaTable_Object = MibTable
tRPOperPSFromCriteriaTable = _TRPOperPSFromCriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20)
)
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaTable.setStatus("current")
_TRPOperPSFromCriteriaEntry_Object = MibTableRow
tRPOperPSFromCriteriaEntry = _TRPOperPSFromCriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1)
)
tRPOperPSFromCriteriaEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIndex"),
)
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaEntry.setStatus("current")
_TRPOperPSFromCriteriaIndex_Type = TPolicyStatementEntryID
_TRPOperPSFromCriteriaIndex_Object = MibTableColumn
tRPOperPSFromCriteriaIndex = _TRPOperPSFromCriteriaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 1),
    _TRPOperPSFromCriteriaIndex_Type()
)
tRPOperPSFromCriteriaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaIndex.setStatus("current")
_TRPOperPSFromCriteriaRowStatus_Type = RowStatus
_TRPOperPSFromCriteriaRowStatus_Object = MibTableColumn
tRPOperPSFromCriteriaRowStatus = _TRPOperPSFromCriteriaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 2),
    _TRPOperPSFromCriteriaRowStatus_Type()
)
tRPOperPSFromCriteriaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaRowStatus.setStatus("current")
_TRPOperPSFromCriteriaProtocol_Type = TRoutePolicyProtocol
_TRPOperPSFromCriteriaProtocol_Object = MibTableColumn
tRPOperPSFromCriteriaProtocol = _TRPOperPSFromCriteriaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 3),
    _TRPOperPSFromCriteriaProtocol_Type()
)
tRPOperPSFromCriteriaProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaProtocol.setStatus("current")
_TRPOperPSFromCriteriaNeighborIpAddr_Type = IpAddress
_TRPOperPSFromCriteriaNeighborIpAddr_Object = MibTableColumn
tRPOperPSFromCriteriaNeighborIpAddr = _TRPOperPSFromCriteriaNeighborIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 4),
    _TRPOperPSFromCriteriaNeighborIpAddr_Type()
)
tRPOperPSFromCriteriaNeighborIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaNeighborIpAddr.setStatus("current")
_TRPOperPSFromCriteriaNeighborPrefixList_Type = TPrefixListName
_TRPOperPSFromCriteriaNeighborPrefixList_Object = MibTableColumn
tRPOperPSFromCriteriaNeighborPrefixList = _TRPOperPSFromCriteriaNeighborPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 5),
    _TRPOperPSFromCriteriaNeighborPrefixList_Type()
)
tRPOperPSFromCriteriaNeighborPrefixList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaNeighborPrefixList.setStatus("current")
_TRPOperPSFromCriteriaPrefixList1_Type = TPrefixListName
_TRPOperPSFromCriteriaPrefixList1_Object = MibTableColumn
tRPOperPSFromCriteriaPrefixList1 = _TRPOperPSFromCriteriaPrefixList1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 6),
    _TRPOperPSFromCriteriaPrefixList1_Type()
)
tRPOperPSFromCriteriaPrefixList1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaPrefixList1.setStatus("current")
_TRPOperPSFromCriteriaPrefixList2_Type = TPrefixListName
_TRPOperPSFromCriteriaPrefixList2_Object = MibTableColumn
tRPOperPSFromCriteriaPrefixList2 = _TRPOperPSFromCriteriaPrefixList2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 7),
    _TRPOperPSFromCriteriaPrefixList2_Type()
)
tRPOperPSFromCriteriaPrefixList2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaPrefixList2.setStatus("current")
_TRPOperPSFromCriteriaPrefixList3_Type = TPrefixListName
_TRPOperPSFromCriteriaPrefixList3_Object = MibTableColumn
tRPOperPSFromCriteriaPrefixList3 = _TRPOperPSFromCriteriaPrefixList3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 8),
    _TRPOperPSFromCriteriaPrefixList3_Type()
)
tRPOperPSFromCriteriaPrefixList3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaPrefixList3.setStatus("current")
_TRPOperPSFromCriteriaPrefixList4_Type = TPrefixListName
_TRPOperPSFromCriteriaPrefixList4_Object = MibTableColumn
tRPOperPSFromCriteriaPrefixList4 = _TRPOperPSFromCriteriaPrefixList4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 9),
    _TRPOperPSFromCriteriaPrefixList4_Type()
)
tRPOperPSFromCriteriaPrefixList4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaPrefixList4.setStatus("current")
_TRPOperPSFromCriteriaPrefixList5_Type = TPrefixListName
_TRPOperPSFromCriteriaPrefixList5_Object = MibTableColumn
tRPOperPSFromCriteriaPrefixList5 = _TRPOperPSFromCriteriaPrefixList5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 10),
    _TRPOperPSFromCriteriaPrefixList5_Type()
)
tRPOperPSFromCriteriaPrefixList5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaPrefixList5.setStatus("current")
_TRPOperPSFromCriteriaASPath_Type = TASPathName
_TRPOperPSFromCriteriaASPath_Object = MibTableColumn
tRPOperPSFromCriteriaASPath = _TRPOperPSFromCriteriaASPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 11),
    _TRPOperPSFromCriteriaASPath_Type()
)
tRPOperPSFromCriteriaASPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaASPath.setStatus("current")
_TRPOperPSFromCriteriaCommunity_Type = TCommunityName
_TRPOperPSFromCriteriaCommunity_Object = MibTableColumn
tRPOperPSFromCriteriaCommunity = _TRPOperPSFromCriteriaCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 12),
    _TRPOperPSFromCriteriaCommunity_Type()
)
tRPOperPSFromCriteriaCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaCommunity.setStatus("current")
_TRPOperPSFromCriteriaOrigin_Type = TPolicyEntryCriteriaOrigin
_TRPOperPSFromCriteriaOrigin_Object = MibTableColumn
tRPOperPSFromCriteriaOrigin = _TRPOperPSFromCriteriaOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 13),
    _TRPOperPSFromCriteriaOrigin_Type()
)
tRPOperPSFromCriteriaOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaOrigin.setStatus("current")
_TRPOperPSFromCriteriaOspfRouteType_Type = TOspfRouteType
_TRPOperPSFromCriteriaOspfRouteType_Object = MibTableColumn
tRPOperPSFromCriteriaOspfRouteType = _TRPOperPSFromCriteriaOspfRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 14),
    _TRPOperPSFromCriteriaOspfRouteType_Type()
)
tRPOperPSFromCriteriaOspfRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaOspfRouteType.setStatus("current")
_TRPOperPSFromCriteriaEntryLastChanged_Type = TimeStamp
_TRPOperPSFromCriteriaEntryLastChanged_Object = MibTableColumn
tRPOperPSFromCriteriaEntryLastChanged = _TRPOperPSFromCriteriaEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 15),
    _TRPOperPSFromCriteriaEntryLastChanged_Type()
)
tRPOperPSFromCriteriaEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaEntryLastChanged.setStatus("obsolete")
_TRPOperPSFromCriteriaArea_Type = IpAddress
_TRPOperPSFromCriteriaArea_Object = MibTableColumn
tRPOperPSFromCriteriaArea = _TRPOperPSFromCriteriaArea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 16),
    _TRPOperPSFromCriteriaArea_Type()
)
tRPOperPSFromCriteriaArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaArea.setStatus("current")
_TRPOperPSFromCriteriaAreaConfigured_Type = TruthValue
_TRPOperPSFromCriteriaAreaConfigured_Object = MibTableColumn
tRPOperPSFromCriteriaAreaConfigured = _TRPOperPSFromCriteriaAreaConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 17),
    _TRPOperPSFromCriteriaAreaConfigured_Type()
)
tRPOperPSFromCriteriaAreaConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaAreaConfigured.setStatus("current")
_TRPOperPSFromCriteriaIsisLevel_Type = TIsisLevel
_TRPOperPSFromCriteriaIsisLevel_Object = MibTableColumn
tRPOperPSFromCriteriaIsisLevel = _TRPOperPSFromCriteriaIsisLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 18),
    _TRPOperPSFromCriteriaIsisLevel_Type()
)
tRPOperPSFromCriteriaIsisLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaIsisLevel.setStatus("current")
_TRPOperPSFromCriteriaIsisExternal_Type = TruthValue
_TRPOperPSFromCriteriaIsisExternal_Object = MibTableColumn
tRPOperPSFromCriteriaIsisExternal = _TRPOperPSFromCriteriaIsisExternal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 19),
    _TRPOperPSFromCriteriaIsisExternal_Type()
)
tRPOperPSFromCriteriaIsisExternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaIsisExternal.setStatus("current")
_TRPOperPSFromCriteriaIgmpHostPrefixList_Type = TPrefixListName
_TRPOperPSFromCriteriaIgmpHostPrefixList_Object = MibTableColumn
tRPOperPSFromCriteriaIgmpHostPrefixList = _TRPOperPSFromCriteriaIgmpHostPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 20),
    _TRPOperPSFromCriteriaIgmpHostPrefixList_Type()
)
tRPOperPSFromCriteriaIgmpHostPrefixList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaIgmpHostPrefixList.setStatus("current")
_TRPOperPSFromCriteriaGrpAddrPrefixList_Type = TPrefixListName
_TRPOperPSFromCriteriaGrpAddrPrefixList_Object = MibTableColumn
tRPOperPSFromCriteriaGrpAddrPrefixList = _TRPOperPSFromCriteriaGrpAddrPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 21),
    _TRPOperPSFromCriteriaGrpAddrPrefixList_Type()
)
tRPOperPSFromCriteriaGrpAddrPrefixList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaGrpAddrPrefixList.setStatus("current")
_TRPOperPSFromCriteriaSrcAddr_Type = IpAddress
_TRPOperPSFromCriteriaSrcAddr_Object = MibTableColumn
tRPOperPSFromCriteriaSrcAddr = _TRPOperPSFromCriteriaSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 22),
    _TRPOperPSFromCriteriaSrcAddr_Type()
)
tRPOperPSFromCriteriaSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaSrcAddr.setStatus("current")
_TRPOperPSFromCriteriaInterface_Type = TNamedItemOrEmpty
_TRPOperPSFromCriteriaInterface_Object = MibTableColumn
tRPOperPSFromCriteriaInterface = _TRPOperPSFromCriteriaInterface_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 23),
    _TRPOperPSFromCriteriaInterface_Type()
)
tRPOperPSFromCriteriaInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaInterface.setStatus("current")
_TRPOperPSFromCriteriaTag_Type = TPolicyActionTag
_TRPOperPSFromCriteriaTag_Object = MibTableColumn
tRPOperPSFromCriteriaTag = _TRPOperPSFromCriteriaTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 24),
    _TRPOperPSFromCriteriaTag_Type()
)
tRPOperPSFromCriteriaTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaTag.setStatus("current")
_TRPOperPSFromCritNbrInetAddrType_Type = InetAddressType
_TRPOperPSFromCritNbrInetAddrType_Object = MibTableColumn
tRPOperPSFromCritNbrInetAddrType = _TRPOperPSFromCritNbrInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 25),
    _TRPOperPSFromCritNbrInetAddrType_Type()
)
tRPOperPSFromCritNbrInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCritNbrInetAddrType.setStatus("current")


class _TRPOperPSFromCritNbrInetAddr_Type(InetAddress):
    """Custom type tRPOperPSFromCritNbrInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TRPOperPSFromCritNbrInetAddr_Type.__name__ = "InetAddress"
_TRPOperPSFromCritNbrInetAddr_Object = MibTableColumn
tRPOperPSFromCritNbrInetAddr = _TRPOperPSFromCritNbrInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 26),
    _TRPOperPSFromCritNbrInetAddr_Type()
)
tRPOperPSFromCritNbrInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCritNbrInetAddr.setStatus("current")
_TRPOperPSFromCritSrcInetAddrType_Type = InetAddressType
_TRPOperPSFromCritSrcInetAddrType_Object = MibTableColumn
tRPOperPSFromCritSrcInetAddrType = _TRPOperPSFromCritSrcInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 27),
    _TRPOperPSFromCritSrcInetAddrType_Type()
)
tRPOperPSFromCritSrcInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCritSrcInetAddrType.setStatus("current")


class _TRPOperPSFromCritSrcInetAddr_Type(InetAddress):
    """Custom type tRPOperPSFromCritSrcInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TRPOperPSFromCritSrcInetAddr_Type.__name__ = "InetAddress"
_TRPOperPSFromCritSrcInetAddr_Object = MibTableColumn
tRPOperPSFromCritSrcInetAddr = _TRPOperPSFromCritSrcInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 28),
    _TRPOperPSFromCritSrcInetAddr_Type()
)
tRPOperPSFromCritSrcInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCritSrcInetAddr.setStatus("current")
_TRPOperPSFromCriteriaFamily_Type = TmnxBGPFamilyType
_TRPOperPSFromCriteriaFamily_Object = MibTableColumn
tRPOperPSFromCriteriaFamily = _TRPOperPSFromCriteriaFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 29),
    _TRPOperPSFromCriteriaFamily_Type()
)
tRPOperPSFromCriteriaFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaFamily.setStatus("current")


class _TRPOperPSFromCriteriaInstanceId_Type(Unsigned32):
    """Custom type tRPOperPSFromCriteriaInstanceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
        ValueRangeConstraint(64, 95),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TRPOperPSFromCriteriaInstanceId_Type.__name__ = "Unsigned32"
_TRPOperPSFromCriteriaInstanceId_Object = MibTableColumn
tRPOperPSFromCriteriaInstanceId = _TRPOperPSFromCriteriaInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 30),
    _TRPOperPSFromCriteriaInstanceId_Type()
)
tRPOperPSFromCriteriaInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaInstanceId.setStatus("current")
_TRPOperPSFromCriteriaMatchTag_Type = TmnxEnabledDisabled
_TRPOperPSFromCriteriaMatchTag_Object = MibTableColumn
tRPOperPSFromCriteriaMatchTag = _TRPOperPSFromCriteriaMatchTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 31),
    _TRPOperPSFromCriteriaMatchTag_Type()
)
tRPOperPSFromCriteriaMatchTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaMatchTag.setStatus("current")
_TRPOperPSFromCriteriaState_Type = TPolicyEntryCriteriaState
_TRPOperPSFromCriteriaState_Object = MibTableColumn
tRPOperPSFromCriteriaState = _TRPOperPSFromCriteriaState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 32),
    _TRPOperPSFromCriteriaState_Type()
)
tRPOperPSFromCriteriaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaState.setStatus("current")
_TRPOperPSFromCritASPathGroup_Type = TASPathGroupName
_TRPOperPSFromCritASPathGroup_Object = MibTableColumn
tRPOperPSFromCritASPathGroup = _TRPOperPSFromCritASPathGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 33),
    _TRPOperPSFromCritASPathGroup_Type()
)
tRPOperPSFromCritASPathGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCritASPathGroup.setStatus("current")
_TRPOperPSFromCriteriaPolicy_Type = PolicyStatementNameOrEmpty
_TRPOperPSFromCriteriaPolicy_Object = MibTableColumn
tRPOperPSFromCriteriaPolicy = _TRPOperPSFromCriteriaPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 34),
    _TRPOperPSFromCriteriaPolicy_Type()
)
tRPOperPSFromCriteriaPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaPolicy.setStatus("current")
_TRPOperPSFromCritCreationOrigin_Type = TmnxCreateOrigin
_TRPOperPSFromCritCreationOrigin_Object = MibTableColumn
tRPOperPSFromCritCreationOrigin = _TRPOperPSFromCritCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 35),
    _TRPOperPSFromCritCreationOrigin_Type()
)
tRPOperPSFromCritCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCritCreationOrigin.setStatus("current")
_TRPOperInetPrefixListTblLastChg_Type = TimeStamp
_TRPOperInetPrefixListTblLastChg_Object = MibScalar
tRPOperInetPrefixListTblLastChg = _TRPOperInetPrefixListTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 21),
    _TRPOperInetPrefixListTblLastChg_Type()
)
tRPOperInetPrefixListTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListTblLastChg.setStatus("obsolete")
_TRPOperInetPrefixListTable_Object = MibTable
tRPOperInetPrefixListTable = _TRPOperInetPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22)
)
if mibBuilder.loadTexts:
    tRPOperInetPrefixListTable.setStatus("current")
_TRPOperInetPrefixListEntry_Object = MibTableRow
tRPOperInetPrefixListEntry = _TRPOperInetPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1)
)
tRPOperInetPrefixListEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListPrefixType"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListPrefix"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListPrefixLen"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListType"),
)
if mibBuilder.loadTexts:
    tRPOperInetPrefixListEntry.setStatus("current")


class _TRPOperInetPrefixListName_Type(TPrefixListName):
    """Custom type tRPOperInetPrefixListName based on TPrefixListName"""
    subtypeSpec = TPrefixListName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPOperInetPrefixListName_Type.__name__ = "TPrefixListName"
_TRPOperInetPrefixListName_Object = MibTableColumn
tRPOperInetPrefixListName = _TRPOperInetPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1, 1),
    _TRPOperInetPrefixListName_Type()
)
tRPOperInetPrefixListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListName.setStatus("current")
_TRPOperInetPrefixListPrefixType_Type = InetAddressType
_TRPOperInetPrefixListPrefixType_Object = MibTableColumn
tRPOperInetPrefixListPrefixType = _TRPOperInetPrefixListPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1, 2),
    _TRPOperInetPrefixListPrefixType_Type()
)
tRPOperInetPrefixListPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListPrefixType.setStatus("current")


class _TRPOperInetPrefixListPrefix_Type(InetAddress):
    """Custom type tRPOperInetPrefixListPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TRPOperInetPrefixListPrefix_Type.__name__ = "InetAddress"
_TRPOperInetPrefixListPrefix_Object = MibTableColumn
tRPOperInetPrefixListPrefix = _TRPOperInetPrefixListPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1, 3),
    _TRPOperInetPrefixListPrefix_Type()
)
tRPOperInetPrefixListPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListPrefix.setStatus("current")
_TRPOperInetPrefixListPrefixLen_Type = InetAddressPrefixLength
_TRPOperInetPrefixListPrefixLen_Object = MibTableColumn
tRPOperInetPrefixListPrefixLen = _TRPOperInetPrefixListPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1, 4),
    _TRPOperInetPrefixListPrefixLen_Type()
)
tRPOperInetPrefixListPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListPrefixLen.setStatus("current")


class _TRPOperInetPrefixListType_Type(Integer32):
    """Custom type tRPOperInetPrefixListType based on Integer32"""
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
        *(("exact", 1),
          ("longer", 2),
          ("through", 3),
          ("range", 4))
    )


_TRPOperInetPrefixListType_Type.__name__ = "Integer32"
_TRPOperInetPrefixListType_Object = MibTableColumn
tRPOperInetPrefixListType = _TRPOperInetPrefixListType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1, 5),
    _TRPOperInetPrefixListType_Type()
)
tRPOperInetPrefixListType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListType.setStatus("current")
_TRPOperInetPrefixListRowStatus_Type = RowStatus
_TRPOperInetPrefixListRowStatus_Object = MibTableColumn
tRPOperInetPrefixListRowStatus = _TRPOperInetPrefixListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1, 6),
    _TRPOperInetPrefixListRowStatus_Type()
)
tRPOperInetPrefixListRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListRowStatus.setStatus("current")
_TRPOperInetPrefixListThroughLen_Type = InetAddressPrefixLength
_TRPOperInetPrefixListThroughLen_Object = MibTableColumn
tRPOperInetPrefixListThroughLen = _TRPOperInetPrefixListThroughLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1, 7),
    _TRPOperInetPrefixListThroughLen_Type()
)
tRPOperInetPrefixListThroughLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListThroughLen.setStatus("current")
_TRPOperInetPrefixListLastChg_Type = TimeStamp
_TRPOperInetPrefixListLastChg_Object = MibTableColumn
tRPOperInetPrefixListLastChg = _TRPOperInetPrefixListLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1, 8),
    _TRPOperInetPrefixListLastChg_Type()
)
tRPOperInetPrefixListLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListLastChg.setStatus("obsolete")
_TRPOperInetPrefixListBeginLen_Type = InetAddressPrefixLength
_TRPOperInetPrefixListBeginLen_Object = MibTableColumn
tRPOperInetPrefixListBeginLen = _TRPOperInetPrefixListBeginLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1, 9),
    _TRPOperInetPrefixListBeginLen_Type()
)
tRPOperInetPrefixListBeginLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListBeginLen.setStatus("current")
_TRPOperCommunityExprTable_Object = MibTable
tRPOperCommunityExprTable = _TRPOperCommunityExprTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 25)
)
if mibBuilder.loadTexts:
    tRPOperCommunityExprTable.setStatus("current")
_TRPOperCommunityExprEntry_Object = MibTableRow
tRPOperCommunityExprEntry = _TRPOperCommunityExprEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 25, 1)
)
tRPOperCommunityExprEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityExprName"),
)
if mibBuilder.loadTexts:
    tRPOperCommunityExprEntry.setStatus("current")


class _TRPOperCommunityExprName_Type(TCommunityName):
    """Custom type tRPOperCommunityExprName based on TCommunityName"""
    subtypeSpec = TCommunityName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPOperCommunityExprName_Type.__name__ = "TCommunityName"
_TRPOperCommunityExprName_Object = MibTableColumn
tRPOperCommunityExprName = _TRPOperCommunityExprName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 25, 1, 1),
    _TRPOperCommunityExprName_Type()
)
tRPOperCommunityExprName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperCommunityExprName.setStatus("current")
_TRPOperCommunityExprRowStatus_Type = RowStatus
_TRPOperCommunityExprRowStatus_Object = MibTableColumn
tRPOperCommunityExprRowStatus = _TRPOperCommunityExprRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 25, 1, 2),
    _TRPOperCommunityExprRowStatus_Type()
)
tRPOperCommunityExprRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperCommunityExprRowStatus.setStatus("current")
_TRPOperCommunityExprString1_Type = TCommunityMemberExpression
_TRPOperCommunityExprString1_Object = MibTableColumn
tRPOperCommunityExprString1 = _TRPOperCommunityExprString1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 25, 1, 3),
    _TRPOperCommunityExprString1_Type()
)
tRPOperCommunityExprString1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperCommunityExprString1.setStatus("current")
_TRPOperCommunityExprString2_Type = TCommunityMemberExpression
_TRPOperCommunityExprString2_Object = MibTableColumn
tRPOperCommunityExprString2 = _TRPOperCommunityExprString2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 25, 1, 4),
    _TRPOperCommunityExprString2_Type()
)
tRPOperCommunityExprString2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperCommunityExprString2.setStatus("current")
_TRPOperCommunityExprString3_Type = TCommunityMemberExpression
_TRPOperCommunityExprString3_Object = MibTableColumn
tRPOperCommunityExprString3 = _TRPOperCommunityExprString3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 25, 1, 5),
    _TRPOperCommunityExprString3_Type()
)
tRPOperCommunityExprString3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperCommunityExprString3.setStatus("current")
_TRPOperCommunityExprString4_Type = TCommunityMemberExpression
_TRPOperCommunityExprString4_Object = MibTableColumn
tRPOperCommunityExprString4 = _TRPOperCommunityExprString4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 25, 1, 6),
    _TRPOperCommunityExprString4_Type()
)
tRPOperCommunityExprString4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperCommunityExprString4.setStatus("current")
_TRPOperCommunityExprExactMatch_Type = TruthValue
_TRPOperCommunityExprExactMatch_Object = MibTableColumn
tRPOperCommunityExprExactMatch = _TRPOperCommunityExprExactMatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 25, 1, 7),
    _TRPOperCommunityExprExactMatch_Type()
)
tRPOperCommunityExprExactMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperCommunityExprExactMatch.setStatus("current")
_TRPOperASPathGroupTable_Object = MibTable
tRPOperASPathGroupTable = _TRPOperASPathGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 26)
)
if mibBuilder.loadTexts:
    tRPOperASPathGroupTable.setStatus("current")
_TRPOperASPathGroupEntry_Object = MibTableRow
tRPOperASPathGroupEntry = _TRPOperASPathGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 26, 1)
)
tRPOperASPathGroupEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathGroupName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathGroupEntryIndex"),
)
if mibBuilder.loadTexts:
    tRPOperASPathGroupEntry.setStatus("current")


class _TRPOperASPathGroupName_Type(TASPathGroupName):
    """Custom type tRPOperASPathGroupName based on TASPathGroupName"""
    subtypeSpec = TASPathGroupName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPOperASPathGroupName_Type.__name__ = "TASPathGroupName"
_TRPOperASPathGroupName_Object = MibTableColumn
tRPOperASPathGroupName = _TRPOperASPathGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 26, 1, 1),
    _TRPOperASPathGroupName_Type()
)
tRPOperASPathGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperASPathGroupName.setStatus("current")


class _TRPOperASPathGroupEntryIndex_Type(Unsigned32):
    """Custom type tRPOperASPathGroupEntryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TRPOperASPathGroupEntryIndex_Type.__name__ = "Unsigned32"
_TRPOperASPathGroupEntryIndex_Object = MibTableColumn
tRPOperASPathGroupEntryIndex = _TRPOperASPathGroupEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 26, 1, 2),
    _TRPOperASPathGroupEntryIndex_Type()
)
tRPOperASPathGroupEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperASPathGroupEntryIndex.setStatus("current")
_TRPOperASPathGroupRowStatus_Type = RowStatus
_TRPOperASPathGroupRowStatus_Object = MibTableColumn
tRPOperASPathGroupRowStatus = _TRPOperASPathGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 26, 1, 3),
    _TRPOperASPathGroupRowStatus_Type()
)
tRPOperASPathGroupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperASPathGroupRowStatus.setStatus("current")


class _TRPOperASPathGroupASPathName_Type(TASPathName):
    """Custom type tRPOperASPathGroupASPathName based on TASPathName"""
    subtypeSpec = TASPathName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPOperASPathGroupASPathName_Type.__name__ = "TASPathName"
_TRPOperASPathGroupASPathName_Object = MibTableColumn
tRPOperASPathGroupASPathName = _TRPOperASPathGroupASPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 26, 1, 4),
    _TRPOperASPathGroupASPathName_Type()
)
tRPOperASPathGroupASPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperASPathGroupASPathName.setStatus("current")
_TRPOperASPathGroupASPathRegEx_Type = TRoutePolicyRegex
_TRPOperASPathGroupASPathRegEx_Object = MibTableColumn
tRPOperASPathGroupASPathRegEx = _TRPOperASPathGroupASPathRegEx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 26, 1, 5),
    _TRPOperASPathGroupASPathRegEx_Type()
)
tRPOperASPathGroupASPathRegEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperASPathGroupASPathRegEx.setStatus("current")
_TRPOperPSFromCommExprTable_Object = MibTable
tRPOperPSFromCommExprTable = _TRPOperPSFromCommExprTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 27)
)
if mibBuilder.loadTexts:
    tRPOperPSFromCommExprTable.setStatus("current")
_TRPOperPSFromCommExprEntry_Object = MibTableRow
tRPOperPSFromCommExprEntry = _TRPOperPSFromCommExprEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 27, 1)
)
tRPOperPSFromCommExprEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIndex"),
)
if mibBuilder.loadTexts:
    tRPOperPSFromCommExprEntry.setStatus("current")
_TRPOperPSFromCommExprRowStatus_Type = RowStatus
_TRPOperPSFromCommExprRowStatus_Object = MibTableColumn
tRPOperPSFromCommExprRowStatus = _TRPOperPSFromCommExprRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 27, 1, 1),
    _TRPOperPSFromCommExprRowStatus_Type()
)
tRPOperPSFromCommExprRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCommExprRowStatus.setStatus("current")
_TRPOperPSFromCommExprString1_Type = TCommunityNameExpression
_TRPOperPSFromCommExprString1_Object = MibTableColumn
tRPOperPSFromCommExprString1 = _TRPOperPSFromCommExprString1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 27, 1, 2),
    _TRPOperPSFromCommExprString1_Type()
)
tRPOperPSFromCommExprString1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCommExprString1.setStatus("current")
_TRPOperPSFromCommExprString2_Type = TCommunityNameExpression
_TRPOperPSFromCommExprString2_Object = MibTableColumn
tRPOperPSFromCommExprString2 = _TRPOperPSFromCommExprString2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 27, 1, 3),
    _TRPOperPSFromCommExprString2_Type()
)
tRPOperPSFromCommExprString2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCommExprString2.setStatus("current")
_TRPOperPSFromCommExprString3_Type = TCommunityNameExpression
_TRPOperPSFromCommExprString3_Object = MibTableColumn
tRPOperPSFromCommExprString3 = _TRPOperPSFromCommExprString3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 27, 1, 4),
    _TRPOperPSFromCommExprString3_Type()
)
tRPOperPSFromCommExprString3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCommExprString3.setStatus("current")
_TRPOperPSFromCommExprString4_Type = TCommunityNameExpression
_TRPOperPSFromCommExprString4_Object = MibTableColumn
tRPOperPSFromCommExprString4 = _TRPOperPSFromCommExprString4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 27, 1, 5),
    _TRPOperPSFromCommExprString4_Type()
)
tRPOperPSFromCommExprString4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCommExprString4.setStatus("current")
_TRPOperPSDefActionAddCommTable_Object = MibTable
tRPOperPSDefActionAddCommTable = _TRPOperPSDefActionAddCommTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28)
)
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddCommTable.setStatus("current")
_TRPOperPSDefActionAddCommEntry_Object = MibTableRow
tRPOperPSDefActionAddCommEntry = _TRPOperPSDefActionAddCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1)
)
tRPOperPSDefActionAddCommEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementName"),
)
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddCommEntry.setStatus("current")
_TRPOperPSDefActionAddComm1_Type = TCommunityName
_TRPOperPSDefActionAddComm1_Object = MibTableColumn
tRPOperPSDefActionAddComm1 = _TRPOperPSDefActionAddComm1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 1),
    _TRPOperPSDefActionAddComm1_Type()
)
tRPOperPSDefActionAddComm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm1.setStatus("current")
_TRPOperPSDefActionAddComm2_Type = TCommunityName
_TRPOperPSDefActionAddComm2_Object = MibTableColumn
tRPOperPSDefActionAddComm2 = _TRPOperPSDefActionAddComm2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 2),
    _TRPOperPSDefActionAddComm2_Type()
)
tRPOperPSDefActionAddComm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm2.setStatus("current")
_TRPOperPSDefActionAddComm3_Type = TCommunityName
_TRPOperPSDefActionAddComm3_Object = MibTableColumn
tRPOperPSDefActionAddComm3 = _TRPOperPSDefActionAddComm3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 3),
    _TRPOperPSDefActionAddComm3_Type()
)
tRPOperPSDefActionAddComm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm3.setStatus("current")
_TRPOperPSDefActionAddComm4_Type = TCommunityName
_TRPOperPSDefActionAddComm4_Object = MibTableColumn
tRPOperPSDefActionAddComm4 = _TRPOperPSDefActionAddComm4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 4),
    _TRPOperPSDefActionAddComm4_Type()
)
tRPOperPSDefActionAddComm4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm4.setStatus("current")
_TRPOperPSDefActionAddComm5_Type = TCommunityName
_TRPOperPSDefActionAddComm5_Object = MibTableColumn
tRPOperPSDefActionAddComm5 = _TRPOperPSDefActionAddComm5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 5),
    _TRPOperPSDefActionAddComm5_Type()
)
tRPOperPSDefActionAddComm5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm5.setStatus("current")
_TRPOperPSDefActionAddComm6_Type = TCommunityName
_TRPOperPSDefActionAddComm6_Object = MibTableColumn
tRPOperPSDefActionAddComm6 = _TRPOperPSDefActionAddComm6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 6),
    _TRPOperPSDefActionAddComm6_Type()
)
tRPOperPSDefActionAddComm6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm6.setStatus("current")
_TRPOperPSDefActionAddComm7_Type = TCommunityName
_TRPOperPSDefActionAddComm7_Object = MibTableColumn
tRPOperPSDefActionAddComm7 = _TRPOperPSDefActionAddComm7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 7),
    _TRPOperPSDefActionAddComm7_Type()
)
tRPOperPSDefActionAddComm7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm7.setStatus("current")
_TRPOperPSDefActionAddComm8_Type = TCommunityName
_TRPOperPSDefActionAddComm8_Object = MibTableColumn
tRPOperPSDefActionAddComm8 = _TRPOperPSDefActionAddComm8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 8),
    _TRPOperPSDefActionAddComm8_Type()
)
tRPOperPSDefActionAddComm8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm8.setStatus("current")
_TRPOperPSDefActionAddComm9_Type = TCommunityName
_TRPOperPSDefActionAddComm9_Object = MibTableColumn
tRPOperPSDefActionAddComm9 = _TRPOperPSDefActionAddComm9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 9),
    _TRPOperPSDefActionAddComm9_Type()
)
tRPOperPSDefActionAddComm9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm9.setStatus("current")
_TRPOperPSDefActionAddComm10_Type = TCommunityName
_TRPOperPSDefActionAddComm10_Object = MibTableColumn
tRPOperPSDefActionAddComm10 = _TRPOperPSDefActionAddComm10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 10),
    _TRPOperPSDefActionAddComm10_Type()
)
tRPOperPSDefActionAddComm10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm10.setStatus("current")
_TRPOperPSDefActionAddComm11_Type = TCommunityName
_TRPOperPSDefActionAddComm11_Object = MibTableColumn
tRPOperPSDefActionAddComm11 = _TRPOperPSDefActionAddComm11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 11),
    _TRPOperPSDefActionAddComm11_Type()
)
tRPOperPSDefActionAddComm11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm11.setStatus("current")
_TRPOperPSDefActionAddComm12_Type = TCommunityName
_TRPOperPSDefActionAddComm12_Object = MibTableColumn
tRPOperPSDefActionAddComm12 = _TRPOperPSDefActionAddComm12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 12),
    _TRPOperPSDefActionAddComm12_Type()
)
tRPOperPSDefActionAddComm12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm12.setStatus("current")
_TRPOperPSDefActionAddComm13_Type = TCommunityName
_TRPOperPSDefActionAddComm13_Object = MibTableColumn
tRPOperPSDefActionAddComm13 = _TRPOperPSDefActionAddComm13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 13),
    _TRPOperPSDefActionAddComm13_Type()
)
tRPOperPSDefActionAddComm13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm13.setStatus("current")
_TRPOperPSDefActionAddComm14_Type = TCommunityName
_TRPOperPSDefActionAddComm14_Object = MibTableColumn
tRPOperPSDefActionAddComm14 = _TRPOperPSDefActionAddComm14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 14),
    _TRPOperPSDefActionAddComm14_Type()
)
tRPOperPSDefActionAddComm14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm14.setStatus("current")
_TRPOperPSDefActionAddComm15_Type = TCommunityName
_TRPOperPSDefActionAddComm15_Object = MibTableColumn
tRPOperPSDefActionAddComm15 = _TRPOperPSDefActionAddComm15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 15),
    _TRPOperPSDefActionAddComm15_Type()
)
tRPOperPSDefActionAddComm15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm15.setStatus("current")
_TRPOperPSDefActionAddComm16_Type = TCommunityName
_TRPOperPSDefActionAddComm16_Object = MibTableColumn
tRPOperPSDefActionAddComm16 = _TRPOperPSDefActionAddComm16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 16),
    _TRPOperPSDefActionAddComm16_Type()
)
tRPOperPSDefActionAddComm16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm16.setStatus("current")
_TRPOperPSDefActionAddComm17_Type = TCommunityName
_TRPOperPSDefActionAddComm17_Object = MibTableColumn
tRPOperPSDefActionAddComm17 = _TRPOperPSDefActionAddComm17_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 17),
    _TRPOperPSDefActionAddComm17_Type()
)
tRPOperPSDefActionAddComm17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm17.setStatus("current")
_TRPOperPSDefActionAddComm18_Type = TCommunityName
_TRPOperPSDefActionAddComm18_Object = MibTableColumn
tRPOperPSDefActionAddComm18 = _TRPOperPSDefActionAddComm18_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 18),
    _TRPOperPSDefActionAddComm18_Type()
)
tRPOperPSDefActionAddComm18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm18.setStatus("current")
_TRPOperPSDefActionAddComm19_Type = TCommunityName
_TRPOperPSDefActionAddComm19_Object = MibTableColumn
tRPOperPSDefActionAddComm19 = _TRPOperPSDefActionAddComm19_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 19),
    _TRPOperPSDefActionAddComm19_Type()
)
tRPOperPSDefActionAddComm19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm19.setStatus("current")
_TRPOperPSDefActionAddComm20_Type = TCommunityName
_TRPOperPSDefActionAddComm20_Object = MibTableColumn
tRPOperPSDefActionAddComm20 = _TRPOperPSDefActionAddComm20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 20),
    _TRPOperPSDefActionAddComm20_Type()
)
tRPOperPSDefActionAddComm20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm20.setStatus("current")
_TRPOperPSDefActionAddComm21_Type = TCommunityName
_TRPOperPSDefActionAddComm21_Object = MibTableColumn
tRPOperPSDefActionAddComm21 = _TRPOperPSDefActionAddComm21_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 21),
    _TRPOperPSDefActionAddComm21_Type()
)
tRPOperPSDefActionAddComm21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm21.setStatus("current")
_TRPOperPSDefActionAddComm22_Type = TCommunityName
_TRPOperPSDefActionAddComm22_Object = MibTableColumn
tRPOperPSDefActionAddComm22 = _TRPOperPSDefActionAddComm22_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 22),
    _TRPOperPSDefActionAddComm22_Type()
)
tRPOperPSDefActionAddComm22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm22.setStatus("current")
_TRPOperPSDefActionAddComm23_Type = TCommunityName
_TRPOperPSDefActionAddComm23_Object = MibTableColumn
tRPOperPSDefActionAddComm23 = _TRPOperPSDefActionAddComm23_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 23),
    _TRPOperPSDefActionAddComm23_Type()
)
tRPOperPSDefActionAddComm23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm23.setStatus("current")
_TRPOperPSDefActionAddComm24_Type = TCommunityName
_TRPOperPSDefActionAddComm24_Object = MibTableColumn
tRPOperPSDefActionAddComm24 = _TRPOperPSDefActionAddComm24_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 24),
    _TRPOperPSDefActionAddComm24_Type()
)
tRPOperPSDefActionAddComm24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm24.setStatus("current")
_TRPOperPSDefActionAddComm25_Type = TCommunityName
_TRPOperPSDefActionAddComm25_Object = MibTableColumn
tRPOperPSDefActionAddComm25 = _TRPOperPSDefActionAddComm25_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 25),
    _TRPOperPSDefActionAddComm25_Type()
)
tRPOperPSDefActionAddComm25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm25.setStatus("current")
_TRPOperPSDefActionAddComm26_Type = TCommunityName
_TRPOperPSDefActionAddComm26_Object = MibTableColumn
tRPOperPSDefActionAddComm26 = _TRPOperPSDefActionAddComm26_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 26),
    _TRPOperPSDefActionAddComm26_Type()
)
tRPOperPSDefActionAddComm26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm26.setStatus("current")
_TRPOperPSDefActionAddComm27_Type = TCommunityName
_TRPOperPSDefActionAddComm27_Object = MibTableColumn
tRPOperPSDefActionAddComm27 = _TRPOperPSDefActionAddComm27_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 27),
    _TRPOperPSDefActionAddComm27_Type()
)
tRPOperPSDefActionAddComm27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm27.setStatus("current")
_TRPOperPSDefActionAddComm28_Type = TCommunityName
_TRPOperPSDefActionAddComm28_Object = MibTableColumn
tRPOperPSDefActionAddComm28 = _TRPOperPSDefActionAddComm28_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 28, 1, 28),
    _TRPOperPSDefActionAddComm28_Type()
)
tRPOperPSDefActionAddComm28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAddComm28.setStatus("current")
_TRPOperPSDefActionRemCommTable_Object = MibTable
tRPOperPSDefActionRemCommTable = _TRPOperPSDefActionRemCommTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29)
)
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemCommTable.setStatus("current")
_TRPOperPSDefActionRemCommEntry_Object = MibTableRow
tRPOperPSDefActionRemCommEntry = _TRPOperPSDefActionRemCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1)
)
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemCommEntry.setStatus("current")
_TRPOperPSDefActionRemoveComm1_Type = TCommunityName
_TRPOperPSDefActionRemoveComm1_Object = MibTableColumn
tRPOperPSDefActionRemoveComm1 = _TRPOperPSDefActionRemoveComm1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 1),
    _TRPOperPSDefActionRemoveComm1_Type()
)
tRPOperPSDefActionRemoveComm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm1.setStatus("current")
_TRPOperPSDefActionRemoveComm2_Type = TCommunityName
_TRPOperPSDefActionRemoveComm2_Object = MibTableColumn
tRPOperPSDefActionRemoveComm2 = _TRPOperPSDefActionRemoveComm2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 2),
    _TRPOperPSDefActionRemoveComm2_Type()
)
tRPOperPSDefActionRemoveComm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm2.setStatus("current")
_TRPOperPSDefActionRemoveComm3_Type = TCommunityName
_TRPOperPSDefActionRemoveComm3_Object = MibTableColumn
tRPOperPSDefActionRemoveComm3 = _TRPOperPSDefActionRemoveComm3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 3),
    _TRPOperPSDefActionRemoveComm3_Type()
)
tRPOperPSDefActionRemoveComm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm3.setStatus("current")
_TRPOperPSDefActionRemoveComm4_Type = TCommunityName
_TRPOperPSDefActionRemoveComm4_Object = MibTableColumn
tRPOperPSDefActionRemoveComm4 = _TRPOperPSDefActionRemoveComm4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 4),
    _TRPOperPSDefActionRemoveComm4_Type()
)
tRPOperPSDefActionRemoveComm4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm4.setStatus("current")
_TRPOperPSDefActionRemoveComm5_Type = TCommunityName
_TRPOperPSDefActionRemoveComm5_Object = MibTableColumn
tRPOperPSDefActionRemoveComm5 = _TRPOperPSDefActionRemoveComm5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 5),
    _TRPOperPSDefActionRemoveComm5_Type()
)
tRPOperPSDefActionRemoveComm5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm5.setStatus("current")
_TRPOperPSDefActionRemoveComm6_Type = TCommunityName
_TRPOperPSDefActionRemoveComm6_Object = MibTableColumn
tRPOperPSDefActionRemoveComm6 = _TRPOperPSDefActionRemoveComm6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 6),
    _TRPOperPSDefActionRemoveComm6_Type()
)
tRPOperPSDefActionRemoveComm6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm6.setStatus("current")
_TRPOperPSDefActionRemoveComm7_Type = TCommunityName
_TRPOperPSDefActionRemoveComm7_Object = MibTableColumn
tRPOperPSDefActionRemoveComm7 = _TRPOperPSDefActionRemoveComm7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 7),
    _TRPOperPSDefActionRemoveComm7_Type()
)
tRPOperPSDefActionRemoveComm7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm7.setStatus("current")
_TRPOperPSDefActionRemoveComm8_Type = TCommunityName
_TRPOperPSDefActionRemoveComm8_Object = MibTableColumn
tRPOperPSDefActionRemoveComm8 = _TRPOperPSDefActionRemoveComm8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 8),
    _TRPOperPSDefActionRemoveComm8_Type()
)
tRPOperPSDefActionRemoveComm8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm8.setStatus("current")
_TRPOperPSDefActionRemoveComm9_Type = TCommunityName
_TRPOperPSDefActionRemoveComm9_Object = MibTableColumn
tRPOperPSDefActionRemoveComm9 = _TRPOperPSDefActionRemoveComm9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 9),
    _TRPOperPSDefActionRemoveComm9_Type()
)
tRPOperPSDefActionRemoveComm9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm9.setStatus("current")
_TRPOperPSDefActionRemoveComm10_Type = TCommunityName
_TRPOperPSDefActionRemoveComm10_Object = MibTableColumn
tRPOperPSDefActionRemoveComm10 = _TRPOperPSDefActionRemoveComm10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 10),
    _TRPOperPSDefActionRemoveComm10_Type()
)
tRPOperPSDefActionRemoveComm10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm10.setStatus("current")
_TRPOperPSDefActionRemoveComm11_Type = TCommunityName
_TRPOperPSDefActionRemoveComm11_Object = MibTableColumn
tRPOperPSDefActionRemoveComm11 = _TRPOperPSDefActionRemoveComm11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 11),
    _TRPOperPSDefActionRemoveComm11_Type()
)
tRPOperPSDefActionRemoveComm11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm11.setStatus("current")
_TRPOperPSDefActionRemoveComm12_Type = TCommunityName
_TRPOperPSDefActionRemoveComm12_Object = MibTableColumn
tRPOperPSDefActionRemoveComm12 = _TRPOperPSDefActionRemoveComm12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 12),
    _TRPOperPSDefActionRemoveComm12_Type()
)
tRPOperPSDefActionRemoveComm12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm12.setStatus("current")
_TRPOperPSDefActionRemoveComm13_Type = TCommunityName
_TRPOperPSDefActionRemoveComm13_Object = MibTableColumn
tRPOperPSDefActionRemoveComm13 = _TRPOperPSDefActionRemoveComm13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 13),
    _TRPOperPSDefActionRemoveComm13_Type()
)
tRPOperPSDefActionRemoveComm13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm13.setStatus("current")
_TRPOperPSDefActionRemoveComm14_Type = TCommunityName
_TRPOperPSDefActionRemoveComm14_Object = MibTableColumn
tRPOperPSDefActionRemoveComm14 = _TRPOperPSDefActionRemoveComm14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 14),
    _TRPOperPSDefActionRemoveComm14_Type()
)
tRPOperPSDefActionRemoveComm14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm14.setStatus("current")
_TRPOperPSDefActionRemoveComm15_Type = TCommunityName
_TRPOperPSDefActionRemoveComm15_Object = MibTableColumn
tRPOperPSDefActionRemoveComm15 = _TRPOperPSDefActionRemoveComm15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 15),
    _TRPOperPSDefActionRemoveComm15_Type()
)
tRPOperPSDefActionRemoveComm15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm15.setStatus("current")
_TRPOperPSDefActionRemoveComm16_Type = TCommunityName
_TRPOperPSDefActionRemoveComm16_Object = MibTableColumn
tRPOperPSDefActionRemoveComm16 = _TRPOperPSDefActionRemoveComm16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 16),
    _TRPOperPSDefActionRemoveComm16_Type()
)
tRPOperPSDefActionRemoveComm16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm16.setStatus("current")
_TRPOperPSDefActionRemoveComm17_Type = TCommunityName
_TRPOperPSDefActionRemoveComm17_Object = MibTableColumn
tRPOperPSDefActionRemoveComm17 = _TRPOperPSDefActionRemoveComm17_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 17),
    _TRPOperPSDefActionRemoveComm17_Type()
)
tRPOperPSDefActionRemoveComm17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm17.setStatus("current")
_TRPOperPSDefActionRemoveComm18_Type = TCommunityName
_TRPOperPSDefActionRemoveComm18_Object = MibTableColumn
tRPOperPSDefActionRemoveComm18 = _TRPOperPSDefActionRemoveComm18_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 18),
    _TRPOperPSDefActionRemoveComm18_Type()
)
tRPOperPSDefActionRemoveComm18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm18.setStatus("current")
_TRPOperPSDefActionRemoveComm19_Type = TCommunityName
_TRPOperPSDefActionRemoveComm19_Object = MibTableColumn
tRPOperPSDefActionRemoveComm19 = _TRPOperPSDefActionRemoveComm19_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 19),
    _TRPOperPSDefActionRemoveComm19_Type()
)
tRPOperPSDefActionRemoveComm19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm19.setStatus("current")
_TRPOperPSDefActionRemoveComm20_Type = TCommunityName
_TRPOperPSDefActionRemoveComm20_Object = MibTableColumn
tRPOperPSDefActionRemoveComm20 = _TRPOperPSDefActionRemoveComm20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 20),
    _TRPOperPSDefActionRemoveComm20_Type()
)
tRPOperPSDefActionRemoveComm20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm20.setStatus("current")
_TRPOperPSDefActionRemoveComm21_Type = TCommunityName
_TRPOperPSDefActionRemoveComm21_Object = MibTableColumn
tRPOperPSDefActionRemoveComm21 = _TRPOperPSDefActionRemoveComm21_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 21),
    _TRPOperPSDefActionRemoveComm21_Type()
)
tRPOperPSDefActionRemoveComm21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm21.setStatus("current")
_TRPOperPSDefActionRemoveComm22_Type = TCommunityName
_TRPOperPSDefActionRemoveComm22_Object = MibTableColumn
tRPOperPSDefActionRemoveComm22 = _TRPOperPSDefActionRemoveComm22_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 22),
    _TRPOperPSDefActionRemoveComm22_Type()
)
tRPOperPSDefActionRemoveComm22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm22.setStatus("current")
_TRPOperPSDefActionRemoveComm23_Type = TCommunityName
_TRPOperPSDefActionRemoveComm23_Object = MibTableColumn
tRPOperPSDefActionRemoveComm23 = _TRPOperPSDefActionRemoveComm23_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 23),
    _TRPOperPSDefActionRemoveComm23_Type()
)
tRPOperPSDefActionRemoveComm23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm23.setStatus("current")
_TRPOperPSDefActionRemoveComm24_Type = TCommunityName
_TRPOperPSDefActionRemoveComm24_Object = MibTableColumn
tRPOperPSDefActionRemoveComm24 = _TRPOperPSDefActionRemoveComm24_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 24),
    _TRPOperPSDefActionRemoveComm24_Type()
)
tRPOperPSDefActionRemoveComm24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm24.setStatus("current")
_TRPOperPSDefActionRemoveComm25_Type = TCommunityName
_TRPOperPSDefActionRemoveComm25_Object = MibTableColumn
tRPOperPSDefActionRemoveComm25 = _TRPOperPSDefActionRemoveComm25_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 25),
    _TRPOperPSDefActionRemoveComm25_Type()
)
tRPOperPSDefActionRemoveComm25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm25.setStatus("current")
_TRPOperPSDefActionRemoveComm26_Type = TCommunityName
_TRPOperPSDefActionRemoveComm26_Object = MibTableColumn
tRPOperPSDefActionRemoveComm26 = _TRPOperPSDefActionRemoveComm26_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 26),
    _TRPOperPSDefActionRemoveComm26_Type()
)
tRPOperPSDefActionRemoveComm26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm26.setStatus("current")
_TRPOperPSDefActionRemoveComm27_Type = TCommunityName
_TRPOperPSDefActionRemoveComm27_Object = MibTableColumn
tRPOperPSDefActionRemoveComm27 = _TRPOperPSDefActionRemoveComm27_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 27),
    _TRPOperPSDefActionRemoveComm27_Type()
)
tRPOperPSDefActionRemoveComm27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm27.setStatus("current")
_TRPOperPSDefActionRemoveComm28_Type = TCommunityName
_TRPOperPSDefActionRemoveComm28_Object = MibTableColumn
tRPOperPSDefActionRemoveComm28 = _TRPOperPSDefActionRemoveComm28_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 29, 1, 28),
    _TRPOperPSDefActionRemoveComm28_Type()
)
tRPOperPSDefActionRemoveComm28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionRemoveComm28.setStatus("current")
_TRPOperPSDefActionRepCommTable_Object = MibTable
tRPOperPSDefActionRepCommTable = _TRPOperPSDefActionRepCommTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30)
)
if mibBuilder.loadTexts:
    tRPOperPSDefActionRepCommTable.setStatus("current")
_TRPOperPSDefActionRepCommEntry_Object = MibTableRow
tRPOperPSDefActionRepCommEntry = _TRPOperPSDefActionRepCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1)
)
if mibBuilder.loadTexts:
    tRPOperPSDefActionRepCommEntry.setStatus("current")
_TRPOperPSDefActionReplaceComm1_Type = TCommunityName
_TRPOperPSDefActionReplaceComm1_Object = MibTableColumn
tRPOperPSDefActionReplaceComm1 = _TRPOperPSDefActionReplaceComm1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 1),
    _TRPOperPSDefActionReplaceComm1_Type()
)
tRPOperPSDefActionReplaceComm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm1.setStatus("current")
_TRPOperPSDefActionReplaceComm2_Type = TCommunityName
_TRPOperPSDefActionReplaceComm2_Object = MibTableColumn
tRPOperPSDefActionReplaceComm2 = _TRPOperPSDefActionReplaceComm2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 2),
    _TRPOperPSDefActionReplaceComm2_Type()
)
tRPOperPSDefActionReplaceComm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm2.setStatus("current")
_TRPOperPSDefActionReplaceComm3_Type = TCommunityName
_TRPOperPSDefActionReplaceComm3_Object = MibTableColumn
tRPOperPSDefActionReplaceComm3 = _TRPOperPSDefActionReplaceComm3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 3),
    _TRPOperPSDefActionReplaceComm3_Type()
)
tRPOperPSDefActionReplaceComm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm3.setStatus("current")
_TRPOperPSDefActionReplaceComm4_Type = TCommunityName
_TRPOperPSDefActionReplaceComm4_Object = MibTableColumn
tRPOperPSDefActionReplaceComm4 = _TRPOperPSDefActionReplaceComm4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 4),
    _TRPOperPSDefActionReplaceComm4_Type()
)
tRPOperPSDefActionReplaceComm4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm4.setStatus("current")
_TRPOperPSDefActionReplaceComm5_Type = TCommunityName
_TRPOperPSDefActionReplaceComm5_Object = MibTableColumn
tRPOperPSDefActionReplaceComm5 = _TRPOperPSDefActionReplaceComm5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 5),
    _TRPOperPSDefActionReplaceComm5_Type()
)
tRPOperPSDefActionReplaceComm5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm5.setStatus("current")
_TRPOperPSDefActionReplaceComm6_Type = TCommunityName
_TRPOperPSDefActionReplaceComm6_Object = MibTableColumn
tRPOperPSDefActionReplaceComm6 = _TRPOperPSDefActionReplaceComm6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 6),
    _TRPOperPSDefActionReplaceComm6_Type()
)
tRPOperPSDefActionReplaceComm6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm6.setStatus("current")
_TRPOperPSDefActionReplaceComm7_Type = TCommunityName
_TRPOperPSDefActionReplaceComm7_Object = MibTableColumn
tRPOperPSDefActionReplaceComm7 = _TRPOperPSDefActionReplaceComm7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 7),
    _TRPOperPSDefActionReplaceComm7_Type()
)
tRPOperPSDefActionReplaceComm7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm7.setStatus("current")
_TRPOperPSDefActionReplaceComm8_Type = TCommunityName
_TRPOperPSDefActionReplaceComm8_Object = MibTableColumn
tRPOperPSDefActionReplaceComm8 = _TRPOperPSDefActionReplaceComm8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 8),
    _TRPOperPSDefActionReplaceComm8_Type()
)
tRPOperPSDefActionReplaceComm8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm8.setStatus("current")
_TRPOperPSDefActionReplaceComm9_Type = TCommunityName
_TRPOperPSDefActionReplaceComm9_Object = MibTableColumn
tRPOperPSDefActionReplaceComm9 = _TRPOperPSDefActionReplaceComm9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 9),
    _TRPOperPSDefActionReplaceComm9_Type()
)
tRPOperPSDefActionReplaceComm9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm9.setStatus("current")
_TRPOperPSDefActionReplaceComm10_Type = TCommunityName
_TRPOperPSDefActionReplaceComm10_Object = MibTableColumn
tRPOperPSDefActionReplaceComm10 = _TRPOperPSDefActionReplaceComm10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 10),
    _TRPOperPSDefActionReplaceComm10_Type()
)
tRPOperPSDefActionReplaceComm10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm10.setStatus("current")
_TRPOperPSDefActionReplaceComm11_Type = TCommunityName
_TRPOperPSDefActionReplaceComm11_Object = MibTableColumn
tRPOperPSDefActionReplaceComm11 = _TRPOperPSDefActionReplaceComm11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 11),
    _TRPOperPSDefActionReplaceComm11_Type()
)
tRPOperPSDefActionReplaceComm11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm11.setStatus("current")
_TRPOperPSDefActionReplaceComm12_Type = TCommunityName
_TRPOperPSDefActionReplaceComm12_Object = MibTableColumn
tRPOperPSDefActionReplaceComm12 = _TRPOperPSDefActionReplaceComm12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 12),
    _TRPOperPSDefActionReplaceComm12_Type()
)
tRPOperPSDefActionReplaceComm12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm12.setStatus("current")
_TRPOperPSDefActionReplaceComm13_Type = TCommunityName
_TRPOperPSDefActionReplaceComm13_Object = MibTableColumn
tRPOperPSDefActionReplaceComm13 = _TRPOperPSDefActionReplaceComm13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 13),
    _TRPOperPSDefActionReplaceComm13_Type()
)
tRPOperPSDefActionReplaceComm13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm13.setStatus("current")
_TRPOperPSDefActionReplaceComm14_Type = TCommunityName
_TRPOperPSDefActionReplaceComm14_Object = MibTableColumn
tRPOperPSDefActionReplaceComm14 = _TRPOperPSDefActionReplaceComm14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 14),
    _TRPOperPSDefActionReplaceComm14_Type()
)
tRPOperPSDefActionReplaceComm14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm14.setStatus("current")
_TRPOperPSDefActionReplaceComm15_Type = TCommunityName
_TRPOperPSDefActionReplaceComm15_Object = MibTableColumn
tRPOperPSDefActionReplaceComm15 = _TRPOperPSDefActionReplaceComm15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 15),
    _TRPOperPSDefActionReplaceComm15_Type()
)
tRPOperPSDefActionReplaceComm15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm15.setStatus("current")
_TRPOperPSDefActionReplaceComm16_Type = TCommunityName
_TRPOperPSDefActionReplaceComm16_Object = MibTableColumn
tRPOperPSDefActionReplaceComm16 = _TRPOperPSDefActionReplaceComm16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 16),
    _TRPOperPSDefActionReplaceComm16_Type()
)
tRPOperPSDefActionReplaceComm16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm16.setStatus("current")
_TRPOperPSDefActionReplaceComm17_Type = TCommunityName
_TRPOperPSDefActionReplaceComm17_Object = MibTableColumn
tRPOperPSDefActionReplaceComm17 = _TRPOperPSDefActionReplaceComm17_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 17),
    _TRPOperPSDefActionReplaceComm17_Type()
)
tRPOperPSDefActionReplaceComm17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm17.setStatus("current")
_TRPOperPSDefActionReplaceComm18_Type = TCommunityName
_TRPOperPSDefActionReplaceComm18_Object = MibTableColumn
tRPOperPSDefActionReplaceComm18 = _TRPOperPSDefActionReplaceComm18_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 18),
    _TRPOperPSDefActionReplaceComm18_Type()
)
tRPOperPSDefActionReplaceComm18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm18.setStatus("current")
_TRPOperPSDefActionReplaceComm19_Type = TCommunityName
_TRPOperPSDefActionReplaceComm19_Object = MibTableColumn
tRPOperPSDefActionReplaceComm19 = _TRPOperPSDefActionReplaceComm19_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 19),
    _TRPOperPSDefActionReplaceComm19_Type()
)
tRPOperPSDefActionReplaceComm19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm19.setStatus("current")
_TRPOperPSDefActionReplaceComm20_Type = TCommunityName
_TRPOperPSDefActionReplaceComm20_Object = MibTableColumn
tRPOperPSDefActionReplaceComm20 = _TRPOperPSDefActionReplaceComm20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 20),
    _TRPOperPSDefActionReplaceComm20_Type()
)
tRPOperPSDefActionReplaceComm20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm20.setStatus("current")
_TRPOperPSDefActionReplaceComm21_Type = TCommunityName
_TRPOperPSDefActionReplaceComm21_Object = MibTableColumn
tRPOperPSDefActionReplaceComm21 = _TRPOperPSDefActionReplaceComm21_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 21),
    _TRPOperPSDefActionReplaceComm21_Type()
)
tRPOperPSDefActionReplaceComm21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm21.setStatus("current")
_TRPOperPSDefActionReplaceComm22_Type = TCommunityName
_TRPOperPSDefActionReplaceComm22_Object = MibTableColumn
tRPOperPSDefActionReplaceComm22 = _TRPOperPSDefActionReplaceComm22_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 22),
    _TRPOperPSDefActionReplaceComm22_Type()
)
tRPOperPSDefActionReplaceComm22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm22.setStatus("current")
_TRPOperPSDefActionReplaceComm23_Type = TCommunityName
_TRPOperPSDefActionReplaceComm23_Object = MibTableColumn
tRPOperPSDefActionReplaceComm23 = _TRPOperPSDefActionReplaceComm23_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 23),
    _TRPOperPSDefActionReplaceComm23_Type()
)
tRPOperPSDefActionReplaceComm23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm23.setStatus("current")
_TRPOperPSDefActionReplaceComm24_Type = TCommunityName
_TRPOperPSDefActionReplaceComm24_Object = MibTableColumn
tRPOperPSDefActionReplaceComm24 = _TRPOperPSDefActionReplaceComm24_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 24),
    _TRPOperPSDefActionReplaceComm24_Type()
)
tRPOperPSDefActionReplaceComm24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm24.setStatus("current")
_TRPOperPSDefActionReplaceComm25_Type = TCommunityName
_TRPOperPSDefActionReplaceComm25_Object = MibTableColumn
tRPOperPSDefActionReplaceComm25 = _TRPOperPSDefActionReplaceComm25_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 25),
    _TRPOperPSDefActionReplaceComm25_Type()
)
tRPOperPSDefActionReplaceComm25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm25.setStatus("current")
_TRPOperPSDefActionReplaceComm26_Type = TCommunityName
_TRPOperPSDefActionReplaceComm26_Object = MibTableColumn
tRPOperPSDefActionReplaceComm26 = _TRPOperPSDefActionReplaceComm26_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 26),
    _TRPOperPSDefActionReplaceComm26_Type()
)
tRPOperPSDefActionReplaceComm26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm26.setStatus("current")
_TRPOperPSDefActionReplaceComm27_Type = TCommunityName
_TRPOperPSDefActionReplaceComm27_Object = MibTableColumn
tRPOperPSDefActionReplaceComm27 = _TRPOperPSDefActionReplaceComm27_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 27),
    _TRPOperPSDefActionReplaceComm27_Type()
)
tRPOperPSDefActionReplaceComm27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm27.setStatus("current")
_TRPOperPSDefActionReplaceComm28_Type = TCommunityName
_TRPOperPSDefActionReplaceComm28_Object = MibTableColumn
tRPOperPSDefActionReplaceComm28 = _TRPOperPSDefActionReplaceComm28_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 30, 1, 28),
    _TRPOperPSDefActionReplaceComm28_Type()
)
tRPOperPSDefActionReplaceComm28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionReplaceComm28.setStatus("current")
_TRPOperPSAccActionAddCommTable_Object = MibTable
tRPOperPSAccActionAddCommTable = _TRPOperPSAccActionAddCommTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31)
)
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddCommTable.setStatus("current")
_TRPOperPSAccActionAddCommEntry_Object = MibTableRow
tRPOperPSAccActionAddCommEntry = _TRPOperPSAccActionAddCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1)
)
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddCommEntry.setStatus("current")
_TRPOperPSAccActionAddComm1_Type = TCommunityName
_TRPOperPSAccActionAddComm1_Object = MibTableColumn
tRPOperPSAccActionAddComm1 = _TRPOperPSAccActionAddComm1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 1),
    _TRPOperPSAccActionAddComm1_Type()
)
tRPOperPSAccActionAddComm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm1.setStatus("current")
_TRPOperPSAccActionAddComm2_Type = TCommunityName
_TRPOperPSAccActionAddComm2_Object = MibTableColumn
tRPOperPSAccActionAddComm2 = _TRPOperPSAccActionAddComm2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 2),
    _TRPOperPSAccActionAddComm2_Type()
)
tRPOperPSAccActionAddComm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm2.setStatus("current")
_TRPOperPSAccActionAddComm3_Type = TCommunityName
_TRPOperPSAccActionAddComm3_Object = MibTableColumn
tRPOperPSAccActionAddComm3 = _TRPOperPSAccActionAddComm3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 3),
    _TRPOperPSAccActionAddComm3_Type()
)
tRPOperPSAccActionAddComm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm3.setStatus("current")
_TRPOperPSAccActionAddComm4_Type = TCommunityName
_TRPOperPSAccActionAddComm4_Object = MibTableColumn
tRPOperPSAccActionAddComm4 = _TRPOperPSAccActionAddComm4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 4),
    _TRPOperPSAccActionAddComm4_Type()
)
tRPOperPSAccActionAddComm4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm4.setStatus("current")
_TRPOperPSAccActionAddComm5_Type = TCommunityName
_TRPOperPSAccActionAddComm5_Object = MibTableColumn
tRPOperPSAccActionAddComm5 = _TRPOperPSAccActionAddComm5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 5),
    _TRPOperPSAccActionAddComm5_Type()
)
tRPOperPSAccActionAddComm5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm5.setStatus("current")
_TRPOperPSAccActionAddComm6_Type = TCommunityName
_TRPOperPSAccActionAddComm6_Object = MibTableColumn
tRPOperPSAccActionAddComm6 = _TRPOperPSAccActionAddComm6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 6),
    _TRPOperPSAccActionAddComm6_Type()
)
tRPOperPSAccActionAddComm6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm6.setStatus("current")
_TRPOperPSAccActionAddComm7_Type = TCommunityName
_TRPOperPSAccActionAddComm7_Object = MibTableColumn
tRPOperPSAccActionAddComm7 = _TRPOperPSAccActionAddComm7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 7),
    _TRPOperPSAccActionAddComm7_Type()
)
tRPOperPSAccActionAddComm7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm7.setStatus("current")
_TRPOperPSAccActionAddComm8_Type = TCommunityName
_TRPOperPSAccActionAddComm8_Object = MibTableColumn
tRPOperPSAccActionAddComm8 = _TRPOperPSAccActionAddComm8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 8),
    _TRPOperPSAccActionAddComm8_Type()
)
tRPOperPSAccActionAddComm8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm8.setStatus("current")
_TRPOperPSAccActionAddComm9_Type = TCommunityName
_TRPOperPSAccActionAddComm9_Object = MibTableColumn
tRPOperPSAccActionAddComm9 = _TRPOperPSAccActionAddComm9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 9),
    _TRPOperPSAccActionAddComm9_Type()
)
tRPOperPSAccActionAddComm9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm9.setStatus("current")
_TRPOperPSAccActionAddComm10_Type = TCommunityName
_TRPOperPSAccActionAddComm10_Object = MibTableColumn
tRPOperPSAccActionAddComm10 = _TRPOperPSAccActionAddComm10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 10),
    _TRPOperPSAccActionAddComm10_Type()
)
tRPOperPSAccActionAddComm10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm10.setStatus("current")
_TRPOperPSAccActionAddComm11_Type = TCommunityName
_TRPOperPSAccActionAddComm11_Object = MibTableColumn
tRPOperPSAccActionAddComm11 = _TRPOperPSAccActionAddComm11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 11),
    _TRPOperPSAccActionAddComm11_Type()
)
tRPOperPSAccActionAddComm11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm11.setStatus("current")
_TRPOperPSAccActionAddComm12_Type = TCommunityName
_TRPOperPSAccActionAddComm12_Object = MibTableColumn
tRPOperPSAccActionAddComm12 = _TRPOperPSAccActionAddComm12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 12),
    _TRPOperPSAccActionAddComm12_Type()
)
tRPOperPSAccActionAddComm12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm12.setStatus("current")
_TRPOperPSAccActionAddComm13_Type = TCommunityName
_TRPOperPSAccActionAddComm13_Object = MibTableColumn
tRPOperPSAccActionAddComm13 = _TRPOperPSAccActionAddComm13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 13),
    _TRPOperPSAccActionAddComm13_Type()
)
tRPOperPSAccActionAddComm13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm13.setStatus("current")
_TRPOperPSAccActionAddComm14_Type = TCommunityName
_TRPOperPSAccActionAddComm14_Object = MibTableColumn
tRPOperPSAccActionAddComm14 = _TRPOperPSAccActionAddComm14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 14),
    _TRPOperPSAccActionAddComm14_Type()
)
tRPOperPSAccActionAddComm14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm14.setStatus("current")
_TRPOperPSAccActionAddComm15_Type = TCommunityName
_TRPOperPSAccActionAddComm15_Object = MibTableColumn
tRPOperPSAccActionAddComm15 = _TRPOperPSAccActionAddComm15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 15),
    _TRPOperPSAccActionAddComm15_Type()
)
tRPOperPSAccActionAddComm15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm15.setStatus("current")
_TRPOperPSAccActionAddComm16_Type = TCommunityName
_TRPOperPSAccActionAddComm16_Object = MibTableColumn
tRPOperPSAccActionAddComm16 = _TRPOperPSAccActionAddComm16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 16),
    _TRPOperPSAccActionAddComm16_Type()
)
tRPOperPSAccActionAddComm16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm16.setStatus("current")
_TRPOperPSAccActionAddComm17_Type = TCommunityName
_TRPOperPSAccActionAddComm17_Object = MibTableColumn
tRPOperPSAccActionAddComm17 = _TRPOperPSAccActionAddComm17_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 17),
    _TRPOperPSAccActionAddComm17_Type()
)
tRPOperPSAccActionAddComm17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm17.setStatus("current")
_TRPOperPSAccActionAddComm18_Type = TCommunityName
_TRPOperPSAccActionAddComm18_Object = MibTableColumn
tRPOperPSAccActionAddComm18 = _TRPOperPSAccActionAddComm18_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 18),
    _TRPOperPSAccActionAddComm18_Type()
)
tRPOperPSAccActionAddComm18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm18.setStatus("current")
_TRPOperPSAccActionAddComm19_Type = TCommunityName
_TRPOperPSAccActionAddComm19_Object = MibTableColumn
tRPOperPSAccActionAddComm19 = _TRPOperPSAccActionAddComm19_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 19),
    _TRPOperPSAccActionAddComm19_Type()
)
tRPOperPSAccActionAddComm19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm19.setStatus("current")
_TRPOperPSAccActionAddComm20_Type = TCommunityName
_TRPOperPSAccActionAddComm20_Object = MibTableColumn
tRPOperPSAccActionAddComm20 = _TRPOperPSAccActionAddComm20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 20),
    _TRPOperPSAccActionAddComm20_Type()
)
tRPOperPSAccActionAddComm20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm20.setStatus("current")
_TRPOperPSAccActionAddComm21_Type = TCommunityName
_TRPOperPSAccActionAddComm21_Object = MibTableColumn
tRPOperPSAccActionAddComm21 = _TRPOperPSAccActionAddComm21_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 21),
    _TRPOperPSAccActionAddComm21_Type()
)
tRPOperPSAccActionAddComm21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm21.setStatus("current")
_TRPOperPSAccActionAddComm22_Type = TCommunityName
_TRPOperPSAccActionAddComm22_Object = MibTableColumn
tRPOperPSAccActionAddComm22 = _TRPOperPSAccActionAddComm22_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 22),
    _TRPOperPSAccActionAddComm22_Type()
)
tRPOperPSAccActionAddComm22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm22.setStatus("current")
_TRPOperPSAccActionAddComm23_Type = TCommunityName
_TRPOperPSAccActionAddComm23_Object = MibTableColumn
tRPOperPSAccActionAddComm23 = _TRPOperPSAccActionAddComm23_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 23),
    _TRPOperPSAccActionAddComm23_Type()
)
tRPOperPSAccActionAddComm23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm23.setStatus("current")
_TRPOperPSAccActionAddComm24_Type = TCommunityName
_TRPOperPSAccActionAddComm24_Object = MibTableColumn
tRPOperPSAccActionAddComm24 = _TRPOperPSAccActionAddComm24_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 24),
    _TRPOperPSAccActionAddComm24_Type()
)
tRPOperPSAccActionAddComm24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm24.setStatus("current")
_TRPOperPSAccActionAddComm25_Type = TCommunityName
_TRPOperPSAccActionAddComm25_Object = MibTableColumn
tRPOperPSAccActionAddComm25 = _TRPOperPSAccActionAddComm25_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 25),
    _TRPOperPSAccActionAddComm25_Type()
)
tRPOperPSAccActionAddComm25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm25.setStatus("current")
_TRPOperPSAccActionAddComm26_Type = TCommunityName
_TRPOperPSAccActionAddComm26_Object = MibTableColumn
tRPOperPSAccActionAddComm26 = _TRPOperPSAccActionAddComm26_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 26),
    _TRPOperPSAccActionAddComm26_Type()
)
tRPOperPSAccActionAddComm26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm26.setStatus("current")
_TRPOperPSAccActionAddComm27_Type = TCommunityName
_TRPOperPSAccActionAddComm27_Object = MibTableColumn
tRPOperPSAccActionAddComm27 = _TRPOperPSAccActionAddComm27_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 27),
    _TRPOperPSAccActionAddComm27_Type()
)
tRPOperPSAccActionAddComm27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm27.setStatus("current")
_TRPOperPSAccActionAddComm28_Type = TCommunityName
_TRPOperPSAccActionAddComm28_Object = MibTableColumn
tRPOperPSAccActionAddComm28 = _TRPOperPSAccActionAddComm28_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 28),
    _TRPOperPSAccActionAddComm28_Type()
)
tRPOperPSAccActionAddComm28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddComm28.setStatus("current")
_TRPOperPSAccActionAddCommCrOrig_Type = TmnxCreateOrigin
_TRPOperPSAccActionAddCommCrOrig_Object = MibTableColumn
tRPOperPSAccActionAddCommCrOrig = _TRPOperPSAccActionAddCommCrOrig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 31, 1, 29),
    _TRPOperPSAccActionAddCommCrOrig_Type()
)
tRPOperPSAccActionAddCommCrOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionAddCommCrOrig.setStatus("current")
_TRPOperPSAccActionRemCommTable_Object = MibTable
tRPOperPSAccActionRemCommTable = _TRPOperPSAccActionRemCommTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32)
)
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemCommTable.setStatus("current")
_TRPOperPSAccActionRemCommEntry_Object = MibTableRow
tRPOperPSAccActionRemCommEntry = _TRPOperPSAccActionRemCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1)
)
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemCommEntry.setStatus("current")
_TRPOperPSAccActionRemoveComm1_Type = TCommunityName
_TRPOperPSAccActionRemoveComm1_Object = MibTableColumn
tRPOperPSAccActionRemoveComm1 = _TRPOperPSAccActionRemoveComm1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 1),
    _TRPOperPSAccActionRemoveComm1_Type()
)
tRPOperPSAccActionRemoveComm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm1.setStatus("current")
_TRPOperPSAccActionRemoveComm2_Type = TCommunityName
_TRPOperPSAccActionRemoveComm2_Object = MibTableColumn
tRPOperPSAccActionRemoveComm2 = _TRPOperPSAccActionRemoveComm2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 2),
    _TRPOperPSAccActionRemoveComm2_Type()
)
tRPOperPSAccActionRemoveComm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm2.setStatus("current")
_TRPOperPSAccActionRemoveComm3_Type = TCommunityName
_TRPOperPSAccActionRemoveComm3_Object = MibTableColumn
tRPOperPSAccActionRemoveComm3 = _TRPOperPSAccActionRemoveComm3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 3),
    _TRPOperPSAccActionRemoveComm3_Type()
)
tRPOperPSAccActionRemoveComm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm3.setStatus("current")
_TRPOperPSAccActionRemoveComm4_Type = TCommunityName
_TRPOperPSAccActionRemoveComm4_Object = MibTableColumn
tRPOperPSAccActionRemoveComm4 = _TRPOperPSAccActionRemoveComm4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 4),
    _TRPOperPSAccActionRemoveComm4_Type()
)
tRPOperPSAccActionRemoveComm4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm4.setStatus("current")
_TRPOperPSAccActionRemoveComm5_Type = TCommunityName
_TRPOperPSAccActionRemoveComm5_Object = MibTableColumn
tRPOperPSAccActionRemoveComm5 = _TRPOperPSAccActionRemoveComm5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 5),
    _TRPOperPSAccActionRemoveComm5_Type()
)
tRPOperPSAccActionRemoveComm5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm5.setStatus("current")
_TRPOperPSAccActionRemoveComm6_Type = TCommunityName
_TRPOperPSAccActionRemoveComm6_Object = MibTableColumn
tRPOperPSAccActionRemoveComm6 = _TRPOperPSAccActionRemoveComm6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 6),
    _TRPOperPSAccActionRemoveComm6_Type()
)
tRPOperPSAccActionRemoveComm6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm6.setStatus("current")
_TRPOperPSAccActionRemoveComm7_Type = TCommunityName
_TRPOperPSAccActionRemoveComm7_Object = MibTableColumn
tRPOperPSAccActionRemoveComm7 = _TRPOperPSAccActionRemoveComm7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 7),
    _TRPOperPSAccActionRemoveComm7_Type()
)
tRPOperPSAccActionRemoveComm7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm7.setStatus("current")
_TRPOperPSAccActionRemoveComm8_Type = TCommunityName
_TRPOperPSAccActionRemoveComm8_Object = MibTableColumn
tRPOperPSAccActionRemoveComm8 = _TRPOperPSAccActionRemoveComm8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 8),
    _TRPOperPSAccActionRemoveComm8_Type()
)
tRPOperPSAccActionRemoveComm8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm8.setStatus("current")
_TRPOperPSAccActionRemoveComm9_Type = TCommunityName
_TRPOperPSAccActionRemoveComm9_Object = MibTableColumn
tRPOperPSAccActionRemoveComm9 = _TRPOperPSAccActionRemoveComm9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 9),
    _TRPOperPSAccActionRemoveComm9_Type()
)
tRPOperPSAccActionRemoveComm9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm9.setStatus("current")
_TRPOperPSAccActionRemoveComm10_Type = TCommunityName
_TRPOperPSAccActionRemoveComm10_Object = MibTableColumn
tRPOperPSAccActionRemoveComm10 = _TRPOperPSAccActionRemoveComm10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 10),
    _TRPOperPSAccActionRemoveComm10_Type()
)
tRPOperPSAccActionRemoveComm10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm10.setStatus("current")
_TRPOperPSAccActionRemoveComm11_Type = TCommunityName
_TRPOperPSAccActionRemoveComm11_Object = MibTableColumn
tRPOperPSAccActionRemoveComm11 = _TRPOperPSAccActionRemoveComm11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 11),
    _TRPOperPSAccActionRemoveComm11_Type()
)
tRPOperPSAccActionRemoveComm11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm11.setStatus("current")
_TRPOperPSAccActionRemoveComm12_Type = TCommunityName
_TRPOperPSAccActionRemoveComm12_Object = MibTableColumn
tRPOperPSAccActionRemoveComm12 = _TRPOperPSAccActionRemoveComm12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 12),
    _TRPOperPSAccActionRemoveComm12_Type()
)
tRPOperPSAccActionRemoveComm12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm12.setStatus("current")
_TRPOperPSAccActionRemoveComm13_Type = TCommunityName
_TRPOperPSAccActionRemoveComm13_Object = MibTableColumn
tRPOperPSAccActionRemoveComm13 = _TRPOperPSAccActionRemoveComm13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 13),
    _TRPOperPSAccActionRemoveComm13_Type()
)
tRPOperPSAccActionRemoveComm13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm13.setStatus("current")
_TRPOperPSAccActionRemoveComm14_Type = TCommunityName
_TRPOperPSAccActionRemoveComm14_Object = MibTableColumn
tRPOperPSAccActionRemoveComm14 = _TRPOperPSAccActionRemoveComm14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 14),
    _TRPOperPSAccActionRemoveComm14_Type()
)
tRPOperPSAccActionRemoveComm14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm14.setStatus("current")
_TRPOperPSAccActionRemoveComm15_Type = TCommunityName
_TRPOperPSAccActionRemoveComm15_Object = MibTableColumn
tRPOperPSAccActionRemoveComm15 = _TRPOperPSAccActionRemoveComm15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 15),
    _TRPOperPSAccActionRemoveComm15_Type()
)
tRPOperPSAccActionRemoveComm15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm15.setStatus("current")
_TRPOperPSAccActionRemoveComm16_Type = TCommunityName
_TRPOperPSAccActionRemoveComm16_Object = MibTableColumn
tRPOperPSAccActionRemoveComm16 = _TRPOperPSAccActionRemoveComm16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 16),
    _TRPOperPSAccActionRemoveComm16_Type()
)
tRPOperPSAccActionRemoveComm16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm16.setStatus("current")
_TRPOperPSAccActionRemoveComm17_Type = TCommunityName
_TRPOperPSAccActionRemoveComm17_Object = MibTableColumn
tRPOperPSAccActionRemoveComm17 = _TRPOperPSAccActionRemoveComm17_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 17),
    _TRPOperPSAccActionRemoveComm17_Type()
)
tRPOperPSAccActionRemoveComm17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm17.setStatus("current")
_TRPOperPSAccActionRemoveComm18_Type = TCommunityName
_TRPOperPSAccActionRemoveComm18_Object = MibTableColumn
tRPOperPSAccActionRemoveComm18 = _TRPOperPSAccActionRemoveComm18_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 18),
    _TRPOperPSAccActionRemoveComm18_Type()
)
tRPOperPSAccActionRemoveComm18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm18.setStatus("current")
_TRPOperPSAccActionRemoveComm19_Type = TCommunityName
_TRPOperPSAccActionRemoveComm19_Object = MibTableColumn
tRPOperPSAccActionRemoveComm19 = _TRPOperPSAccActionRemoveComm19_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 19),
    _TRPOperPSAccActionRemoveComm19_Type()
)
tRPOperPSAccActionRemoveComm19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm19.setStatus("current")
_TRPOperPSAccActionRemoveComm20_Type = TCommunityName
_TRPOperPSAccActionRemoveComm20_Object = MibTableColumn
tRPOperPSAccActionRemoveComm20 = _TRPOperPSAccActionRemoveComm20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 20),
    _TRPOperPSAccActionRemoveComm20_Type()
)
tRPOperPSAccActionRemoveComm20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm20.setStatus("current")
_TRPOperPSAccActionRemoveComm21_Type = TCommunityName
_TRPOperPSAccActionRemoveComm21_Object = MibTableColumn
tRPOperPSAccActionRemoveComm21 = _TRPOperPSAccActionRemoveComm21_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 21),
    _TRPOperPSAccActionRemoveComm21_Type()
)
tRPOperPSAccActionRemoveComm21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm21.setStatus("current")
_TRPOperPSAccActionRemoveComm22_Type = TCommunityName
_TRPOperPSAccActionRemoveComm22_Object = MibTableColumn
tRPOperPSAccActionRemoveComm22 = _TRPOperPSAccActionRemoveComm22_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 22),
    _TRPOperPSAccActionRemoveComm22_Type()
)
tRPOperPSAccActionRemoveComm22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm22.setStatus("current")
_TRPOperPSAccActionRemoveComm23_Type = TCommunityName
_TRPOperPSAccActionRemoveComm23_Object = MibTableColumn
tRPOperPSAccActionRemoveComm23 = _TRPOperPSAccActionRemoveComm23_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 23),
    _TRPOperPSAccActionRemoveComm23_Type()
)
tRPOperPSAccActionRemoveComm23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm23.setStatus("current")
_TRPOperPSAccActionRemoveComm24_Type = TCommunityName
_TRPOperPSAccActionRemoveComm24_Object = MibTableColumn
tRPOperPSAccActionRemoveComm24 = _TRPOperPSAccActionRemoveComm24_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 24),
    _TRPOperPSAccActionRemoveComm24_Type()
)
tRPOperPSAccActionRemoveComm24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm24.setStatus("current")
_TRPOperPSAccActionRemoveComm25_Type = TCommunityName
_TRPOperPSAccActionRemoveComm25_Object = MibTableColumn
tRPOperPSAccActionRemoveComm25 = _TRPOperPSAccActionRemoveComm25_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 25),
    _TRPOperPSAccActionRemoveComm25_Type()
)
tRPOperPSAccActionRemoveComm25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm25.setStatus("current")
_TRPOperPSAccActionRemoveComm26_Type = TCommunityName
_TRPOperPSAccActionRemoveComm26_Object = MibTableColumn
tRPOperPSAccActionRemoveComm26 = _TRPOperPSAccActionRemoveComm26_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 26),
    _TRPOperPSAccActionRemoveComm26_Type()
)
tRPOperPSAccActionRemoveComm26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm26.setStatus("current")
_TRPOperPSAccActionRemoveComm27_Type = TCommunityName
_TRPOperPSAccActionRemoveComm27_Object = MibTableColumn
tRPOperPSAccActionRemoveComm27 = _TRPOperPSAccActionRemoveComm27_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 27),
    _TRPOperPSAccActionRemoveComm27_Type()
)
tRPOperPSAccActionRemoveComm27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm27.setStatus("current")
_TRPOperPSAccActionRemoveComm28_Type = TCommunityName
_TRPOperPSAccActionRemoveComm28_Object = MibTableColumn
tRPOperPSAccActionRemoveComm28 = _TRPOperPSAccActionRemoveComm28_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 32, 1, 28),
    _TRPOperPSAccActionRemoveComm28_Type()
)
tRPOperPSAccActionRemoveComm28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionRemoveComm28.setStatus("current")
_TRPOperPSAccActionRepCommTable_Object = MibTable
tRPOperPSAccActionRepCommTable = _TRPOperPSAccActionRepCommTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33)
)
if mibBuilder.loadTexts:
    tRPOperPSAccActionRepCommTable.setStatus("current")
_TRPOperPSAccActionRepCommEntry_Object = MibTableRow
tRPOperPSAccActionRepCommEntry = _TRPOperPSAccActionRepCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1)
)
if mibBuilder.loadTexts:
    tRPOperPSAccActionRepCommEntry.setStatus("current")
_TRPOperPSAccActionReplaceComm1_Type = TCommunityName
_TRPOperPSAccActionReplaceComm1_Object = MibTableColumn
tRPOperPSAccActionReplaceComm1 = _TRPOperPSAccActionReplaceComm1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 1),
    _TRPOperPSAccActionReplaceComm1_Type()
)
tRPOperPSAccActionReplaceComm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm1.setStatus("current")
_TRPOperPSAccActionReplaceComm2_Type = TCommunityName
_TRPOperPSAccActionReplaceComm2_Object = MibTableColumn
tRPOperPSAccActionReplaceComm2 = _TRPOperPSAccActionReplaceComm2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 2),
    _TRPOperPSAccActionReplaceComm2_Type()
)
tRPOperPSAccActionReplaceComm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm2.setStatus("current")
_TRPOperPSAccActionReplaceComm3_Type = TCommunityName
_TRPOperPSAccActionReplaceComm3_Object = MibTableColumn
tRPOperPSAccActionReplaceComm3 = _TRPOperPSAccActionReplaceComm3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 3),
    _TRPOperPSAccActionReplaceComm3_Type()
)
tRPOperPSAccActionReplaceComm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm3.setStatus("current")
_TRPOperPSAccActionReplaceComm4_Type = TCommunityName
_TRPOperPSAccActionReplaceComm4_Object = MibTableColumn
tRPOperPSAccActionReplaceComm4 = _TRPOperPSAccActionReplaceComm4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 4),
    _TRPOperPSAccActionReplaceComm4_Type()
)
tRPOperPSAccActionReplaceComm4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm4.setStatus("current")
_TRPOperPSAccActionReplaceComm5_Type = TCommunityName
_TRPOperPSAccActionReplaceComm5_Object = MibTableColumn
tRPOperPSAccActionReplaceComm5 = _TRPOperPSAccActionReplaceComm5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 5),
    _TRPOperPSAccActionReplaceComm5_Type()
)
tRPOperPSAccActionReplaceComm5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm5.setStatus("current")
_TRPOperPSAccActionReplaceComm6_Type = TCommunityName
_TRPOperPSAccActionReplaceComm6_Object = MibTableColumn
tRPOperPSAccActionReplaceComm6 = _TRPOperPSAccActionReplaceComm6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 6),
    _TRPOperPSAccActionReplaceComm6_Type()
)
tRPOperPSAccActionReplaceComm6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm6.setStatus("current")
_TRPOperPSAccActionReplaceComm7_Type = TCommunityName
_TRPOperPSAccActionReplaceComm7_Object = MibTableColumn
tRPOperPSAccActionReplaceComm7 = _TRPOperPSAccActionReplaceComm7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 7),
    _TRPOperPSAccActionReplaceComm7_Type()
)
tRPOperPSAccActionReplaceComm7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm7.setStatus("current")
_TRPOperPSAccActionReplaceComm8_Type = TCommunityName
_TRPOperPSAccActionReplaceComm8_Object = MibTableColumn
tRPOperPSAccActionReplaceComm8 = _TRPOperPSAccActionReplaceComm8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 8),
    _TRPOperPSAccActionReplaceComm8_Type()
)
tRPOperPSAccActionReplaceComm8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm8.setStatus("current")
_TRPOperPSAccActionReplaceComm9_Type = TCommunityName
_TRPOperPSAccActionReplaceComm9_Object = MibTableColumn
tRPOperPSAccActionReplaceComm9 = _TRPOperPSAccActionReplaceComm9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 9),
    _TRPOperPSAccActionReplaceComm9_Type()
)
tRPOperPSAccActionReplaceComm9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm9.setStatus("current")
_TRPOperPSAccActionReplaceComm10_Type = TCommunityName
_TRPOperPSAccActionReplaceComm10_Object = MibTableColumn
tRPOperPSAccActionReplaceComm10 = _TRPOperPSAccActionReplaceComm10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 10),
    _TRPOperPSAccActionReplaceComm10_Type()
)
tRPOperPSAccActionReplaceComm10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm10.setStatus("current")
_TRPOperPSAccActionReplaceComm11_Type = TCommunityName
_TRPOperPSAccActionReplaceComm11_Object = MibTableColumn
tRPOperPSAccActionReplaceComm11 = _TRPOperPSAccActionReplaceComm11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 11),
    _TRPOperPSAccActionReplaceComm11_Type()
)
tRPOperPSAccActionReplaceComm11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm11.setStatus("current")
_TRPOperPSAccActionReplaceComm12_Type = TCommunityName
_TRPOperPSAccActionReplaceComm12_Object = MibTableColumn
tRPOperPSAccActionReplaceComm12 = _TRPOperPSAccActionReplaceComm12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 12),
    _TRPOperPSAccActionReplaceComm12_Type()
)
tRPOperPSAccActionReplaceComm12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm12.setStatus("current")
_TRPOperPSAccActionReplaceComm13_Type = TCommunityName
_TRPOperPSAccActionReplaceComm13_Object = MibTableColumn
tRPOperPSAccActionReplaceComm13 = _TRPOperPSAccActionReplaceComm13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 13),
    _TRPOperPSAccActionReplaceComm13_Type()
)
tRPOperPSAccActionReplaceComm13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm13.setStatus("current")
_TRPOperPSAccActionReplaceComm14_Type = TCommunityName
_TRPOperPSAccActionReplaceComm14_Object = MibTableColumn
tRPOperPSAccActionReplaceComm14 = _TRPOperPSAccActionReplaceComm14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 14),
    _TRPOperPSAccActionReplaceComm14_Type()
)
tRPOperPSAccActionReplaceComm14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm14.setStatus("current")
_TRPOperPSAccActionReplaceComm15_Type = TCommunityName
_TRPOperPSAccActionReplaceComm15_Object = MibTableColumn
tRPOperPSAccActionReplaceComm15 = _TRPOperPSAccActionReplaceComm15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 15),
    _TRPOperPSAccActionReplaceComm15_Type()
)
tRPOperPSAccActionReplaceComm15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm15.setStatus("current")
_TRPOperPSAccActionReplaceComm16_Type = TCommunityName
_TRPOperPSAccActionReplaceComm16_Object = MibTableColumn
tRPOperPSAccActionReplaceComm16 = _TRPOperPSAccActionReplaceComm16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 16),
    _TRPOperPSAccActionReplaceComm16_Type()
)
tRPOperPSAccActionReplaceComm16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm16.setStatus("current")
_TRPOperPSAccActionReplaceComm17_Type = TCommunityName
_TRPOperPSAccActionReplaceComm17_Object = MibTableColumn
tRPOperPSAccActionReplaceComm17 = _TRPOperPSAccActionReplaceComm17_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 17),
    _TRPOperPSAccActionReplaceComm17_Type()
)
tRPOperPSAccActionReplaceComm17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm17.setStatus("current")
_TRPOperPSAccActionReplaceComm18_Type = TCommunityName
_TRPOperPSAccActionReplaceComm18_Object = MibTableColumn
tRPOperPSAccActionReplaceComm18 = _TRPOperPSAccActionReplaceComm18_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 18),
    _TRPOperPSAccActionReplaceComm18_Type()
)
tRPOperPSAccActionReplaceComm18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm18.setStatus("current")
_TRPOperPSAccActionReplaceComm19_Type = TCommunityName
_TRPOperPSAccActionReplaceComm19_Object = MibTableColumn
tRPOperPSAccActionReplaceComm19 = _TRPOperPSAccActionReplaceComm19_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 19),
    _TRPOperPSAccActionReplaceComm19_Type()
)
tRPOperPSAccActionReplaceComm19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm19.setStatus("current")
_TRPOperPSAccActionReplaceComm20_Type = TCommunityName
_TRPOperPSAccActionReplaceComm20_Object = MibTableColumn
tRPOperPSAccActionReplaceComm20 = _TRPOperPSAccActionReplaceComm20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 20),
    _TRPOperPSAccActionReplaceComm20_Type()
)
tRPOperPSAccActionReplaceComm20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm20.setStatus("current")
_TRPOperPSAccActionReplaceComm21_Type = TCommunityName
_TRPOperPSAccActionReplaceComm21_Object = MibTableColumn
tRPOperPSAccActionReplaceComm21 = _TRPOperPSAccActionReplaceComm21_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 21),
    _TRPOperPSAccActionReplaceComm21_Type()
)
tRPOperPSAccActionReplaceComm21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm21.setStatus("current")
_TRPOperPSAccActionReplaceComm22_Type = TCommunityName
_TRPOperPSAccActionReplaceComm22_Object = MibTableColumn
tRPOperPSAccActionReplaceComm22 = _TRPOperPSAccActionReplaceComm22_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 22),
    _TRPOperPSAccActionReplaceComm22_Type()
)
tRPOperPSAccActionReplaceComm22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm22.setStatus("current")
_TRPOperPSAccActionReplaceComm23_Type = TCommunityName
_TRPOperPSAccActionReplaceComm23_Object = MibTableColumn
tRPOperPSAccActionReplaceComm23 = _TRPOperPSAccActionReplaceComm23_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 23),
    _TRPOperPSAccActionReplaceComm23_Type()
)
tRPOperPSAccActionReplaceComm23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm23.setStatus("current")
_TRPOperPSAccActionReplaceComm24_Type = TCommunityName
_TRPOperPSAccActionReplaceComm24_Object = MibTableColumn
tRPOperPSAccActionReplaceComm24 = _TRPOperPSAccActionReplaceComm24_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 24),
    _TRPOperPSAccActionReplaceComm24_Type()
)
tRPOperPSAccActionReplaceComm24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm24.setStatus("current")
_TRPOperPSAccActionReplaceComm25_Type = TCommunityName
_TRPOperPSAccActionReplaceComm25_Object = MibTableColumn
tRPOperPSAccActionReplaceComm25 = _TRPOperPSAccActionReplaceComm25_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 25),
    _TRPOperPSAccActionReplaceComm25_Type()
)
tRPOperPSAccActionReplaceComm25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm25.setStatus("current")
_TRPOperPSAccActionReplaceComm26_Type = TCommunityName
_TRPOperPSAccActionReplaceComm26_Object = MibTableColumn
tRPOperPSAccActionReplaceComm26 = _TRPOperPSAccActionReplaceComm26_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 26),
    _TRPOperPSAccActionReplaceComm26_Type()
)
tRPOperPSAccActionReplaceComm26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm26.setStatus("current")
_TRPOperPSAccActionReplaceComm27_Type = TCommunityName
_TRPOperPSAccActionReplaceComm27_Object = MibTableColumn
tRPOperPSAccActionReplaceComm27 = _TRPOperPSAccActionReplaceComm27_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 27),
    _TRPOperPSAccActionReplaceComm27_Type()
)
tRPOperPSAccActionReplaceComm27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm27.setStatus("current")
_TRPOperPSAccActionReplaceComm28_Type = TCommunityName
_TRPOperPSAccActionReplaceComm28_Object = MibTableColumn
tRPOperPSAccActionReplaceComm28 = _TRPOperPSAccActionReplaceComm28_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 33, 1, 28),
    _TRPOperPSAccActionReplaceComm28_Type()
)
tRPOperPSAccActionReplaceComm28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAccActionReplaceComm28.setStatus("current")
_TRPOperPSFromCriteriaExtTable_Object = MibTable
tRPOperPSFromCriteriaExtTable = _TRPOperPSFromCriteriaExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 34)
)
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaExtTable.setStatus("current")
_TRPOperPSFromCriteriaExtEntry_Object = MibTableRow
tRPOperPSFromCriteriaExtEntry = _TRPOperPSFromCriteriaExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 34, 1)
)
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaExtEntry.setStatus("current")
_TRPOperPSFromCritExtMvpnType_Type = TPolicyEntryCriteriaMvpnType
_TRPOperPSFromCritExtMvpnType_Object = MibTableColumn
tRPOperPSFromCritExtMvpnType = _TRPOperPSFromCritExtMvpnType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 34, 1, 1),
    _TRPOperPSFromCritExtMvpnType_Type()
)
tRPOperPSFromCritExtMvpnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCritExtMvpnType.setStatus("current")
_TRPOperPSFromCritSrcAddrPfxList_Type = TPrefixListName
_TRPOperPSFromCritSrcAddrPfxList_Object = MibTableColumn
tRPOperPSFromCritSrcAddrPfxList = _TRPOperPSFromCritSrcAddrPfxList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 34, 1, 2),
    _TRPOperPSFromCritSrcAddrPfxList_Type()
)
tRPOperPSFromCritSrcAddrPfxList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCritSrcAddrPfxList.setStatus("current")


class _TRPOperPSFromCritOrigValidState_Type(Integer32):
    """Custom type tRPOperPSFromCritOrigValidState based on Integer32"""
    defaultValue = 0

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
        *(("notApplicable", 0),
          ("valid", 1),
          ("notFound", 2),
          ("invalid", 3))
    )


_TRPOperPSFromCritOrigValidState_Type.__name__ = "Integer32"
_TRPOperPSFromCritOrigValidState_Object = MibTableColumn
tRPOperPSFromCritOrigValidState = _TRPOperPSFromCritOrigValidState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 34, 1, 3),
    _TRPOperPSFromCritOrigValidState_Type()
)
tRPOperPSFromCritOrigValidState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCritOrigValidState.setStatus("current")
_TRPOperPSPolicyVariableTable_Object = MibTable
tRPOperPSPolicyVariableTable = _TRPOperPSPolicyVariableTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 35)
)
if mibBuilder.loadTexts:
    tRPOperPSPolicyVariableTable.setStatus("current")
_TRPOperPSPolicyVariableEntry_Object = MibTableRow
tRPOperPSPolicyVariableEntry = _TRPOperPSPolicyVariableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 35, 1)
)
tRPOperPSPolicyVariableEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIndex"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSPolicyVarName"),
)
if mibBuilder.loadTexts:
    tRPOperPSPolicyVariableEntry.setStatus("current")
_TRPOperPSPolicyVarName_Type = TPolicyVariableName
_TRPOperPSPolicyVarName_Object = MibTableColumn
tRPOperPSPolicyVarName = _TRPOperPSPolicyVarName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 35, 1, 1),
    _TRPOperPSPolicyVarName_Type()
)
tRPOperPSPolicyVarName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperPSPolicyVarName.setStatus("current")
_TRPOperPSPolicyVarRowStatus_Type = RowStatus
_TRPOperPSPolicyVarRowStatus_Object = MibTableColumn
tRPOperPSPolicyVarRowStatus = _TRPOperPSPolicyVarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 35, 1, 2),
    _TRPOperPSPolicyVarRowStatus_Type()
)
tRPOperPSPolicyVarRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSPolicyVarRowStatus.setStatus("current")
_TRPOperPSPolicyVarValue_Type = TNamedItem
_TRPOperPSPolicyVarValue_Object = MibTableColumn
tRPOperPSPolicyVarValue = _TRPOperPSPolicyVarValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 35, 1, 3),
    _TRPOperPSPolicyVarValue_Type()
)
tRPOperPSPolicyVarValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSPolicyVarValue.setStatus("current")
_TRPOperPSAcptActParamsExtTable_Object = MibTable
tRPOperPSAcptActParamsExtTable = _TRPOperPSAcptActParamsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 36)
)
if mibBuilder.loadTexts:
    tRPOperPSAcptActParamsExtTable.setStatus("current")
_TRPOperPSAcptActParamsExtEntry_Object = MibTableRow
tRPOperPSAcptActParamsExtEntry = _TRPOperPSAcptActParamsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 36, 1)
)
if mibBuilder.loadTexts:
    tRPOperPSAcptActParamsExtEntry.setStatus("current")
_TRPOperPSAcptActStickyEcmp_Type = TruthValue
_TRPOperPSAcptActStickyEcmp_Object = MibTableColumn
tRPOperPSAcptActStickyEcmp = _TRPOperPSAcptActStickyEcmp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 36, 1, 1),
    _TRPOperPSAcptActStickyEcmp_Type()
)
tRPOperPSAcptActStickyEcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActStickyEcmp.setStatus("current")
_TRPOperPSAcptActBgpLeaking_Type = TruthValue
_TRPOperPSAcptActBgpLeaking_Object = MibTableColumn
tRPOperPSAcptActBgpLeaking = _TRPOperPSAcptActBgpLeaking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 36, 1, 5),
    _TRPOperPSAcptActBgpLeaking_Type()
)
tRPOperPSAcptActBgpLeaking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActBgpLeaking.setStatus("current")
_TRPOperPSDefActParamsExtTable_Object = MibTable
tRPOperPSDefActParamsExtTable = _TRPOperPSDefActParamsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 37)
)
if mibBuilder.loadTexts:
    tRPOperPSDefActParamsExtTable.setStatus("current")
_TRPOperPSDefActParamsExtEntry_Object = MibTableRow
tRPOperPSDefActParamsExtEntry = _TRPOperPSDefActParamsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 37, 1)
)
if mibBuilder.loadTexts:
    tRPOperPSDefActParamsExtEntry.setStatus("current")
_TRPOperPSDefActStickyEcmp_Type = TruthValue
_TRPOperPSDefActStickyEcmp_Object = MibTableColumn
tRPOperPSDefActStickyEcmp = _TRPOperPSDefActStickyEcmp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 37, 1, 1),
    _TRPOperPSDefActStickyEcmp_Type()
)
tRPOperPSDefActStickyEcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActStickyEcmp.setStatus("current")
_TRPOperPSDefActBgpLeaking_Type = TruthValue
_TRPOperPSDefActBgpLeaking_Object = MibTableColumn
tRPOperPSDefActBgpLeaking = _TRPOperPSDefActBgpLeaking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 37, 1, 5),
    _TRPOperPSDefActBgpLeaking_Type()
)
tRPOperPSDefActBgpLeaking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActBgpLeaking.setStatus("current")
_TRPAdminObjects_ObjectIdentity = ObjectIdentity
tRPAdminObjects = _TRPAdminObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2)
)
_TRPAdminControlObjects_ObjectIdentity = ObjectIdentity
tRPAdminControlObjects = _TRPAdminControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 1)
)
_TRPAdminOwner_Type = TNamedItemOrEmpty
_TRPAdminOwner_Object = MibScalar
tRPAdminOwner = _TRPAdminOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 1, 1),
    _TRPAdminOwner_Type()
)
tRPAdminOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPAdminOwner.setStatus("current")


class _TRPAdminControlApply_Type(Integer32):
    """Custom type tRPAdminControlApply based on Integer32"""
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
        *(("none", 1),
          ("initialize", 2),
          ("commit", 3),
          ("exclusive", 4))
    )


_TRPAdminControlApply_Type.__name__ = "Integer32"
_TRPAdminControlApply_Object = MibScalar
tRPAdminControlApply = _TRPAdminControlApply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 1, 2),
    _TRPAdminControlApply_Type()
)
tRPAdminControlApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRPAdminControlApply.setStatus("current")
_TRPAdminLastSetTimer_Type = TimeInterval
_TRPAdminLastSetTimer_Object = MibScalar
tRPAdminLastSetTimer = _TRPAdminLastSetTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 1, 3),
    _TRPAdminLastSetTimer_Type()
)
tRPAdminLastSetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPAdminLastSetTimer.setStatus("current")
if mibBuilder.loadTexts:
    tRPAdminLastSetTimer.setUnits("centiseconds")


class _TRPAdminLastSetTimeout_Type(Integer32):
    """Custom type tRPAdminLastSetTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TRPAdminLastSetTimeout_Type.__name__ = "Integer32"
_TRPAdminLastSetTimeout_Object = MibScalar
tRPAdminLastSetTimeout = _TRPAdminLastSetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 1, 4),
    _TRPAdminLastSetTimeout_Type()
)
tRPAdminLastSetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRPAdminLastSetTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tRPAdminLastSetTimeout.setUnits("seconds")


class _TRPAdminControlResetExclusive_Type(TruthValue):
    """Custom type tRPAdminControlResetExclusive based on TruthValue"""
    defaultValue = 2


_TRPAdminControlResetExclusive_Type.__name__ = "TruthValue"
_TRPAdminControlResetExclusive_Object = MibScalar
tRPAdminControlResetExclusive = _TRPAdminControlResetExclusive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 1, 5),
    _TRPAdminControlResetExclusive_Type()
)
tRPAdminControlResetExclusive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRPAdminControlResetExclusive.setStatus("current")
_TRPAdminValueObjects_ObjectIdentity = ObjectIdentity
tRPAdminValueObjects = _TRPAdminValueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2)
)
_TRPAdminASPathTable_Object = MibTable
tRPAdminASPathTable = _TRPAdminASPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tRPAdminASPathTable.setStatus("current")
_TRPAdminASPathEntry_Object = MibTableRow
tRPAdminASPathEntry = _TRPAdminASPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 1, 1)
)
tRPAdminASPathEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathName"),
)
if mibBuilder.loadTexts:
    tRPAdminASPathEntry.setStatus("current")


class _TRPAdminASPathName_Type(TASPathName):
    """Custom type tRPAdminASPathName based on TASPathName"""
    subtypeSpec = TASPathName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPAdminASPathName_Type.__name__ = "TASPathName"
_TRPAdminASPathName_Object = MibTableColumn
tRPAdminASPathName = _TRPAdminASPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 1, 1, 1),
    _TRPAdminASPathName_Type()
)
tRPAdminASPathName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminASPathName.setStatus("current")
_TRPAdminASPathRowStatus_Type = RowStatus
_TRPAdminASPathRowStatus_Object = MibTableColumn
tRPAdminASPathRowStatus = _TRPAdminASPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 1, 1, 2),
    _TRPAdminASPathRowStatus_Type()
)
tRPAdminASPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminASPathRowStatus.setStatus("current")
_TRPAdminASPathRegEx_Type = TRoutePolicyRegex
_TRPAdminASPathRegEx_Object = MibTableColumn
tRPAdminASPathRegEx = _TRPAdminASPathRegEx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 1, 1, 3),
    _TRPAdminASPathRegEx_Type()
)
tRPAdminASPathRegEx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminASPathRegEx.setStatus("current")
_TRPAdminCommunityTable_Object = MibTable
tRPAdminCommunityTable = _TRPAdminCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tRPAdminCommunityTable.setStatus("current")
_TRPAdminCommunityEntry_Object = MibTableRow
tRPAdminCommunityEntry = _TRPAdminCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 2, 1)
)
tRPAdminCommunityEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityMember"),
)
if mibBuilder.loadTexts:
    tRPAdminCommunityEntry.setStatus("current")


class _TRPAdminCommunityName_Type(TCommunityName):
    """Custom type tRPAdminCommunityName based on TCommunityName"""
    subtypeSpec = TCommunityName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPAdminCommunityName_Type.__name__ = "TCommunityName"
_TRPAdminCommunityName_Object = MibTableColumn
tRPAdminCommunityName = _TRPAdminCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 2, 1, 1),
    _TRPAdminCommunityName_Type()
)
tRPAdminCommunityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminCommunityName.setStatus("current")
_TRPAdminCommunityMember_Type = TCommunityMember
_TRPAdminCommunityMember_Object = MibTableColumn
tRPAdminCommunityMember = _TRPAdminCommunityMember_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 2, 1, 2),
    _TRPAdminCommunityMember_Type()
)
tRPAdminCommunityMember.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminCommunityMember.setStatus("current")
_TRPAdminCommunityRowStatus_Type = RowStatus
_TRPAdminCommunityRowStatus_Object = MibTableColumn
tRPAdminCommunityRowStatus = _TRPAdminCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 2, 1, 3),
    _TRPAdminCommunityRowStatus_Type()
)
tRPAdminCommunityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminCommunityRowStatus.setStatus("current")
_TRPAdminCommunityCreationOrigin_Type = TmnxCreateOrigin
_TRPAdminCommunityCreationOrigin_Object = MibTableColumn
tRPAdminCommunityCreationOrigin = _TRPAdminCommunityCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 2, 1, 4),
    _TRPAdminCommunityCreationOrigin_Type()
)
tRPAdminCommunityCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPAdminCommunityCreationOrigin.setStatus("current")
_TRPAdminDampingTable_Object = MibTable
tRPAdminDampingTable = _TRPAdminDampingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 3)
)
if mibBuilder.loadTexts:
    tRPAdminDampingTable.setStatus("current")
_TRPAdminDampingEntry_Object = MibTableRow
tRPAdminDampingEntry = _TRPAdminDampingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 3, 1)
)
tRPAdminDampingEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingName"),
)
if mibBuilder.loadTexts:
    tRPAdminDampingEntry.setStatus("current")


class _TRPAdminDampingName_Type(TDampingName):
    """Custom type tRPAdminDampingName based on TDampingName"""
    subtypeSpec = TDampingName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPAdminDampingName_Type.__name__ = "TDampingName"
_TRPAdminDampingName_Object = MibTableColumn
tRPAdminDampingName = _TRPAdminDampingName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 3, 1, 1),
    _TRPAdminDampingName_Type()
)
tRPAdminDampingName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminDampingName.setStatus("current")
_TRPAdminDampingRowStatus_Type = RowStatus
_TRPAdminDampingRowStatus_Object = MibTableColumn
tRPAdminDampingRowStatus = _TRPAdminDampingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 3, 1, 2),
    _TRPAdminDampingRowStatus_Type()
)
tRPAdminDampingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminDampingRowStatus.setStatus("current")


class _TRPAdminDampingHalfLife_Type(Unsigned32):
    """Custom type tRPAdminDampingHalfLife based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45),
    )


_TRPAdminDampingHalfLife_Type.__name__ = "Unsigned32"
_TRPAdminDampingHalfLife_Object = MibTableColumn
tRPAdminDampingHalfLife = _TRPAdminDampingHalfLife_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 3, 1, 3),
    _TRPAdminDampingHalfLife_Type()
)
tRPAdminDampingHalfLife.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminDampingHalfLife.setStatus("current")
if mibBuilder.loadTexts:
    tRPAdminDampingHalfLife.setUnits("minutes")


class _TRPAdminDampingMaxSuppress_Type(Unsigned32):
    """Custom type tRPAdminDampingMaxSuppress based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_TRPAdminDampingMaxSuppress_Type.__name__ = "Unsigned32"
_TRPAdminDampingMaxSuppress_Object = MibTableColumn
tRPAdminDampingMaxSuppress = _TRPAdminDampingMaxSuppress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 3, 1, 4),
    _TRPAdminDampingMaxSuppress_Type()
)
tRPAdminDampingMaxSuppress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminDampingMaxSuppress.setStatus("current")
if mibBuilder.loadTexts:
    tRPAdminDampingMaxSuppress.setUnits("minutes")


class _TRPAdminDampingReuse_Type(Unsigned32):
    """Custom type tRPAdminDampingReuse based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_TRPAdminDampingReuse_Type.__name__ = "Unsigned32"
_TRPAdminDampingReuse_Object = MibTableColumn
tRPAdminDampingReuse = _TRPAdminDampingReuse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 3, 1, 5),
    _TRPAdminDampingReuse_Type()
)
tRPAdminDampingReuse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminDampingReuse.setStatus("current")


class _TRPAdminDampingSuppress_Type(Unsigned32):
    """Custom type tRPAdminDampingSuppress based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_TRPAdminDampingSuppress_Type.__name__ = "Unsigned32"
_TRPAdminDampingSuppress_Object = MibTableColumn
tRPAdminDampingSuppress = _TRPAdminDampingSuppress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 3, 1, 6),
    _TRPAdminDampingSuppress_Type()
)
tRPAdminDampingSuppress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminDampingSuppress.setStatus("current")
_TRPAdminPrefixListTable_Object = MibTable
tRPAdminPrefixListTable = _TRPAdminPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 4)
)
if mibBuilder.loadTexts:
    tRPAdminPrefixListTable.setStatus("current")
_TRPAdminPrefixListEntry_Object = MibTableRow
tRPAdminPrefixListEntry = _TRPAdminPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 4, 1)
)
tRPAdminPrefixListEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListIpPrefix"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListMask"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListType"),
)
if mibBuilder.loadTexts:
    tRPAdminPrefixListEntry.setStatus("current")


class _TRPAdminPrefixListName_Type(TPrefixListName):
    """Custom type tRPAdminPrefixListName based on TPrefixListName"""
    subtypeSpec = TPrefixListName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPAdminPrefixListName_Type.__name__ = "TPrefixListName"
_TRPAdminPrefixListName_Object = MibTableColumn
tRPAdminPrefixListName = _TRPAdminPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 4, 1, 1),
    _TRPAdminPrefixListName_Type()
)
tRPAdminPrefixListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminPrefixListName.setStatus("current")
_TRPAdminPrefixListIpPrefix_Type = IpAddress
_TRPAdminPrefixListIpPrefix_Object = MibTableColumn
tRPAdminPrefixListIpPrefix = _TRPAdminPrefixListIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 4, 1, 2),
    _TRPAdminPrefixListIpPrefix_Type()
)
tRPAdminPrefixListIpPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminPrefixListIpPrefix.setStatus("current")
_TRPAdminPrefixListMask_Type = IpAddressPrefixLength
_TRPAdminPrefixListMask_Object = MibTableColumn
tRPAdminPrefixListMask = _TRPAdminPrefixListMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 4, 1, 3),
    _TRPAdminPrefixListMask_Type()
)
tRPAdminPrefixListMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminPrefixListMask.setStatus("current")
_TRPAdminPrefixListRowStatus_Type = RowStatus
_TRPAdminPrefixListRowStatus_Object = MibTableColumn
tRPAdminPrefixListRowStatus = _TRPAdminPrefixListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 4, 1, 4),
    _TRPAdminPrefixListRowStatus_Type()
)
tRPAdminPrefixListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPrefixListRowStatus.setStatus("current")


class _TRPAdminPrefixListType_Type(Integer32):
    """Custom type tRPAdminPrefixListType based on Integer32"""
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
        *(("exact", 1),
          ("longer", 2),
          ("through", 3),
          ("range", 4))
    )


_TRPAdminPrefixListType_Type.__name__ = "Integer32"
_TRPAdminPrefixListType_Object = MibTableColumn
tRPAdminPrefixListType = _TRPAdminPrefixListType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 4, 1, 5),
    _TRPAdminPrefixListType_Type()
)
tRPAdminPrefixListType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminPrefixListType.setStatus("current")


class _TRPAdminPrefixListThroughLength_Type(IpAddressPrefixLength):
    """Custom type tRPAdminPrefixListThroughLength based on IpAddressPrefixLength"""
    defaultValue = 0


_TRPAdminPrefixListThroughLength_Type.__name__ = "IpAddressPrefixLength"
_TRPAdminPrefixListThroughLength_Object = MibTableColumn
tRPAdminPrefixListThroughLength = _TRPAdminPrefixListThroughLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 4, 1, 6),
    _TRPAdminPrefixListThroughLength_Type()
)
tRPAdminPrefixListThroughLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPrefixListThroughLength.setStatus("current")


class _TRPAdminPrefixListBeginLength_Type(IpAddressPrefixLength):
    """Custom type tRPAdminPrefixListBeginLength based on IpAddressPrefixLength"""
    defaultValue = 0


_TRPAdminPrefixListBeginLength_Type.__name__ = "IpAddressPrefixLength"
_TRPAdminPrefixListBeginLength_Object = MibTableColumn
tRPAdminPrefixListBeginLength = _TRPAdminPrefixListBeginLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 4, 1, 8),
    _TRPAdminPrefixListBeginLength_Type()
)
tRPAdminPrefixListBeginLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPrefixListBeginLength.setStatus("current")
_TRPAdminPolicyStatementTable_Object = MibTable
tRPAdminPolicyStatementTable = _TRPAdminPolicyStatementTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 5)
)
if mibBuilder.loadTexts:
    tRPAdminPolicyStatementTable.setStatus("current")
_TRPAdminPolicyStatementEntry_Object = MibTableRow
tRPAdminPolicyStatementEntry = _TRPAdminPolicyStatementEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 5, 1)
)
tRPAdminPolicyStatementEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementName"),
)
if mibBuilder.loadTexts:
    tRPAdminPolicyStatementEntry.setStatus("current")
_TRPAdminPolicyStatementName_Type = TPolicyStatementName
_TRPAdminPolicyStatementName_Object = MibTableColumn
tRPAdminPolicyStatementName = _TRPAdminPolicyStatementName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 5, 1, 1),
    _TRPAdminPolicyStatementName_Type()
)
tRPAdminPolicyStatementName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminPolicyStatementName.setStatus("current")
_TRPAdminPolicyStatementRowStatus_Type = RowStatus
_TRPAdminPolicyStatementRowStatus_Object = MibTableColumn
tRPAdminPolicyStatementRowStatus = _TRPAdminPolicyStatementRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 5, 1, 2),
    _TRPAdminPolicyStatementRowStatus_Type()
)
tRPAdminPolicyStatementRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPolicyStatementRowStatus.setStatus("current")


class _TRPAdminPolicyStatementDescription_Type(TItemDescription):
    """Custom type tRPAdminPolicyStatementDescription based on TItemDescription"""
    defaultHexValue = ""


_TRPAdminPolicyStatementDescription_Type.__name__ = "TItemDescription"
_TRPAdminPolicyStatementDescription_Object = MibTableColumn
tRPAdminPolicyStatementDescription = _TRPAdminPolicyStatementDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 5, 1, 3),
    _TRPAdminPolicyStatementDescription_Type()
)
tRPAdminPolicyStatementDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPolicyStatementDescription.setStatus("current")


class _TRPAdminPolicyStatementDefaultAction_Type(TPolicyEntryAction):
    """Custom type tRPAdminPolicyStatementDefaultAction based on TPolicyEntryAction"""
    defaultValue = 2


_TRPAdminPolicyStatementDefaultAction_Type.__name__ = "TPolicyEntryAction"
_TRPAdminPolicyStatementDefaultAction_Object = MibTableColumn
tRPAdminPolicyStatementDefaultAction = _TRPAdminPolicyStatementDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 5, 1, 4),
    _TRPAdminPolicyStatementDefaultAction_Type()
)
tRPAdminPolicyStatementDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPolicyStatementDefaultAction.setStatus("current")
_TRPAdminPolicyStatementCrOrigin_Type = TmnxCreateOrigin
_TRPAdminPolicyStatementCrOrigin_Object = MibTableColumn
tRPAdminPolicyStatementCrOrigin = _TRPAdminPolicyStatementCrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 5, 1, 5),
    _TRPAdminPolicyStatementCrOrigin_Type()
)
tRPAdminPolicyStatementCrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPAdminPolicyStatementCrOrigin.setStatus("current")
_TRPAdminPSDefaultActionParamsTable_Object = MibTable
tRPAdminPSDefaultActionParamsTable = _TRPAdminPSDefaultActionParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6)
)
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionParamsTable.setStatus("current")
_TRPAdminPSDefaultActionParamsEntry_Object = MibTableRow
tRPAdminPSDefaultActionParamsEntry = _TRPAdminPSDefaultActionParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1)
)
tRPAdminPSDefaultActionParamsEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementName"),
)
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionParamsEntry.setStatus("current")


class _TRPAdminPSDefaultActionASPath_Type(TPolicyEntryEdit):
    """Custom type tRPAdminPSDefaultActionASPath based on TPolicyEntryEdit"""
    defaultValue = 1


_TRPAdminPSDefaultActionASPath_Type.__name__ = "TPolicyEntryEdit"
_TRPAdminPSDefaultActionASPath_Object = MibTableColumn
tRPAdminPSDefaultActionASPath = _TRPAdminPSDefaultActionASPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 1),
    _TRPAdminPSDefaultActionASPath_Type()
)
tRPAdminPSDefaultActionASPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionASPath.setStatus("current")


class _TRPAdminPSDefaultActionASPathName_Type(TASPathName):
    """Custom type tRPAdminPSDefaultActionASPathName based on TASPathName"""
    defaultHexValue = ""


_TRPAdminPSDefaultActionASPathName_Type.__name__ = "TASPathName"
_TRPAdminPSDefaultActionASPathName_Object = MibTableColumn
tRPAdminPSDefaultActionASPathName = _TRPAdminPSDefaultActionASPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 2),
    _TRPAdminPSDefaultActionASPathName_Type()
)
tRPAdminPSDefaultActionASPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionASPathName.setStatus("current")


class _TRPAdminPSDefaultActionASPathPrependAS_Type(TmnxBgpAutonomousSystem):
    """Custom type tRPAdminPSDefaultActionASPathPrependAS based on TmnxBgpAutonomousSystem"""
    defaultValue = 0


_TRPAdminPSDefaultActionASPathPrependAS_Type.__name__ = "TmnxBgpAutonomousSystem"
_TRPAdminPSDefaultActionASPathPrependAS_Object = MibTableColumn
tRPAdminPSDefaultActionASPathPrependAS = _TRPAdminPSDefaultActionASPathPrependAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 3),
    _TRPAdminPSDefaultActionASPathPrependAS_Type()
)
tRPAdminPSDefaultActionASPathPrependAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionASPathPrependAS.setStatus("obsolete")


class _TRPAdminPSDefaultActionASPathPrependCount_Type(Integer32):
    """Custom type tRPAdminPSDefaultActionASPathPrependCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_TRPAdminPSDefaultActionASPathPrependCount_Type.__name__ = "Integer32"
_TRPAdminPSDefaultActionASPathPrependCount_Object = MibTableColumn
tRPAdminPSDefaultActionASPathPrependCount = _TRPAdminPSDefaultActionASPathPrependCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 4),
    _TRPAdminPSDefaultActionASPathPrependCount_Type()
)
tRPAdminPSDefaultActionASPathPrependCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionASPathPrependCount.setStatus("current")


class _TRPAdminPSDefaultActionCommunity1_Type(TPolicyEntryEdit):
    """Custom type tRPAdminPSDefaultActionCommunity1 based on TPolicyEntryEdit"""
    defaultValue = 1


_TRPAdminPSDefaultActionCommunity1_Type.__name__ = "TPolicyEntryEdit"
_TRPAdminPSDefaultActionCommunity1_Object = MibTableColumn
tRPAdminPSDefaultActionCommunity1 = _TRPAdminPSDefaultActionCommunity1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 5),
    _TRPAdminPSDefaultActionCommunity1_Type()
)
tRPAdminPSDefaultActionCommunity1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionCommunity1.setStatus("obsolete")


class _TRPAdminPSDefaultActionCommunityName1_Type(TCommunityName):
    """Custom type tRPAdminPSDefaultActionCommunityName1 based on TCommunityName"""
    defaultHexValue = ""


_TRPAdminPSDefaultActionCommunityName1_Type.__name__ = "TCommunityName"
_TRPAdminPSDefaultActionCommunityName1_Object = MibTableColumn
tRPAdminPSDefaultActionCommunityName1 = _TRPAdminPSDefaultActionCommunityName1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 6),
    _TRPAdminPSDefaultActionCommunityName1_Type()
)
tRPAdminPSDefaultActionCommunityName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionCommunityName1.setStatus("obsolete")


class _TRPAdminPSDefaultActionCommunity2_Type(TPolicyEntryEdit):
    """Custom type tRPAdminPSDefaultActionCommunity2 based on TPolicyEntryEdit"""
    defaultValue = 1


_TRPAdminPSDefaultActionCommunity2_Type.__name__ = "TPolicyEntryEdit"
_TRPAdminPSDefaultActionCommunity2_Object = MibTableColumn
tRPAdminPSDefaultActionCommunity2 = _TRPAdminPSDefaultActionCommunity2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 7),
    _TRPAdminPSDefaultActionCommunity2_Type()
)
tRPAdminPSDefaultActionCommunity2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionCommunity2.setStatus("obsolete")


class _TRPAdminPSDefaultActionCommunityName2_Type(TCommunityName):
    """Custom type tRPAdminPSDefaultActionCommunityName2 based on TCommunityName"""
    defaultHexValue = ""


_TRPAdminPSDefaultActionCommunityName2_Type.__name__ = "TCommunityName"
_TRPAdminPSDefaultActionCommunityName2_Object = MibTableColumn
tRPAdminPSDefaultActionCommunityName2 = _TRPAdminPSDefaultActionCommunityName2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 8),
    _TRPAdminPSDefaultActionCommunityName2_Type()
)
tRPAdminPSDefaultActionCommunityName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionCommunityName2.setStatus("obsolete")


class _TRPAdminPSDefaultActionOrigin_Type(TPolicyEntryCriteriaOrigin):
    """Custom type tRPAdminPSDefaultActionOrigin based on TPolicyEntryCriteriaOrigin"""
    defaultValue = 1


_TRPAdminPSDefaultActionOrigin_Type.__name__ = "TPolicyEntryCriteriaOrigin"
_TRPAdminPSDefaultActionOrigin_Object = MibTableColumn
tRPAdminPSDefaultActionOrigin = _TRPAdminPSDefaultActionOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 9),
    _TRPAdminPSDefaultActionOrigin_Type()
)
tRPAdminPSDefaultActionOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionOrigin.setStatus("current")


class _TRPAdminPSDefaultActionLocalPreferenceSet_Type(TruthValue):
    """Custom type tRPAdminPSDefaultActionLocalPreferenceSet based on TruthValue"""
    defaultValue = 2


_TRPAdminPSDefaultActionLocalPreferenceSet_Type.__name__ = "TruthValue"
_TRPAdminPSDefaultActionLocalPreferenceSet_Object = MibTableColumn
tRPAdminPSDefaultActionLocalPreferenceSet = _TRPAdminPSDefaultActionLocalPreferenceSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 10),
    _TRPAdminPSDefaultActionLocalPreferenceSet_Type()
)
tRPAdminPSDefaultActionLocalPreferenceSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionLocalPreferenceSet.setStatus("current")


class _TRPAdminPSDefaultActionLocalPreference_Type(TmnxBgpLocalPreference):
    """Custom type tRPAdminPSDefaultActionLocalPreference based on TmnxBgpLocalPreference"""
    defaultValue = 0


_TRPAdminPSDefaultActionLocalPreference_Type.__name__ = "TmnxBgpLocalPreference"
_TRPAdminPSDefaultActionLocalPreference_Object = MibTableColumn
tRPAdminPSDefaultActionLocalPreference = _TRPAdminPSDefaultActionLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 11),
    _TRPAdminPSDefaultActionLocalPreference_Type()
)
tRPAdminPSDefaultActionLocalPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionLocalPreference.setStatus("current")


class _TRPAdminPSDefaultActionMetric_Type(TPolicyEntryEdit):
    """Custom type tRPAdminPSDefaultActionMetric based on TPolicyEntryEdit"""
    defaultValue = 1


_TRPAdminPSDefaultActionMetric_Type.__name__ = "TPolicyEntryEdit"
_TRPAdminPSDefaultActionMetric_Object = MibTableColumn
tRPAdminPSDefaultActionMetric = _TRPAdminPSDefaultActionMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 12),
    _TRPAdminPSDefaultActionMetric_Type()
)
tRPAdminPSDefaultActionMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionMetric.setStatus("current")


class _TRPAdminPSDefaultActionMetricValue_Type(Unsigned32):
    """Custom type tRPAdminPSDefaultActionMetricValue based on Unsigned32"""
    defaultValue = 0


_TRPAdminPSDefaultActionMetricValue_Type.__name__ = "Unsigned32"
_TRPAdminPSDefaultActionMetricValue_Object = MibTableColumn
tRPAdminPSDefaultActionMetricValue = _TRPAdminPSDefaultActionMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 13),
    _TRPAdminPSDefaultActionMetricValue_Type()
)
tRPAdminPSDefaultActionMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionMetricValue.setStatus("current")


class _TRPAdminPSDefaultActionPreference_Type(TmnxBgpPreference):
    """Custom type tRPAdminPSDefaultActionPreference based on TmnxBgpPreference"""
    defaultValue = 0


_TRPAdminPSDefaultActionPreference_Type.__name__ = "TmnxBgpPreference"
_TRPAdminPSDefaultActionPreference_Object = MibTableColumn
tRPAdminPSDefaultActionPreference = _TRPAdminPSDefaultActionPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 15),
    _TRPAdminPSDefaultActionPreference_Type()
)
tRPAdminPSDefaultActionPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionPreference.setStatus("current")


class _TRPAdminPSDefaultActionDamping_Type(TDampingName):
    """Custom type tRPAdminPSDefaultActionDamping based on TDampingName"""
    defaultHexValue = ""


_TRPAdminPSDefaultActionDamping_Type.__name__ = "TDampingName"
_TRPAdminPSDefaultActionDamping_Object = MibTableColumn
tRPAdminPSDefaultActionDamping = _TRPAdminPSDefaultActionDamping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 16),
    _TRPAdminPSDefaultActionDamping_Type()
)
tRPAdminPSDefaultActionDamping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionDamping.setStatus("current")


class _TRPAdminPSDefaultActionNextHopSelf_Type(TruthValue):
    """Custom type tRPAdminPSDefaultActionNextHopSelf based on TruthValue"""
    defaultValue = 2


_TRPAdminPSDefaultActionNextHopSelf_Type.__name__ = "TruthValue"
_TRPAdminPSDefaultActionNextHopSelf_Object = MibTableColumn
tRPAdminPSDefaultActionNextHopSelf = _TRPAdminPSDefaultActionNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 17),
    _TRPAdminPSDefaultActionNextHopSelf_Type()
)
tRPAdminPSDefaultActionNextHopSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionNextHopSelf.setStatus("current")


class _TRPAdminPSDefaultActionNextHop_Type(IpAddress):
    """Custom type tRPAdminPSDefaultActionNextHop based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_TRPAdminPSDefaultActionNextHop_Type.__name__ = "IpAddress"
_TRPAdminPSDefaultActionNextHop_Object = MibTableColumn
tRPAdminPSDefaultActionNextHop = _TRPAdminPSDefaultActionNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 18),
    _TRPAdminPSDefaultActionNextHop_Type()
)
tRPAdminPSDefaultActionNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionNextHop.setStatus("current")


class _TRPAdminPSDefaultActionTag_Type(TPolicyActionTag):
    """Custom type tRPAdminPSDefaultActionTag based on TPolicyActionTag"""
    defaultValue = 0


_TRPAdminPSDefaultActionTag_Type.__name__ = "TPolicyActionTag"
_TRPAdminPSDefaultActionTag_Object = MibTableColumn
tRPAdminPSDefaultActionTag = _TRPAdminPSDefaultActionTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 19),
    _TRPAdminPSDefaultActionTag_Type()
)
tRPAdminPSDefaultActionTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionTag.setStatus("current")


class _TRPAdminPSDefaultActionOspfType_Type(TOspfRouteType):
    """Custom type tRPAdminPSDefaultActionOspfType based on TOspfRouteType"""
    defaultValue = 0


_TRPAdminPSDefaultActionOspfType_Type.__name__ = "TOspfRouteType"
_TRPAdminPSDefaultActionOspfType_Object = MibTableColumn
tRPAdminPSDefaultActionOspfType = _TRPAdminPSDefaultActionOspfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 20),
    _TRPAdminPSDefaultActionOspfType_Type()
)
tRPAdminPSDefaultActionOspfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionOspfType.setStatus("current")
_TRPAdminPSDefActInetNextHopType_Type = InetAddressType
_TRPAdminPSDefActInetNextHopType_Object = MibTableColumn
tRPAdminPSDefActInetNextHopType = _TRPAdminPSDefActInetNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 21),
    _TRPAdminPSDefActInetNextHopType_Type()
)
tRPAdminPSDefActInetNextHopType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActInetNextHopType.setStatus("current")


class _TRPAdminPSDefActInetNextHop_Type(InetAddress):
    """Custom type tRPAdminPSDefActInetNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TRPAdminPSDefActInetNextHop_Type.__name__ = "InetAddress"
_TRPAdminPSDefActInetNextHop_Object = MibTableColumn
tRPAdminPSDefActInetNextHop = _TRPAdminPSDefActInetNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 22),
    _TRPAdminPSDefActInetNextHop_Type()
)
tRPAdminPSDefActInetNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActInetNextHop.setStatus("current")


class _TRPAdminPSDefaultActionASPathPnd_Type(InetAutonomousSystemNumber):
    """Custom type tRPAdminPSDefaultActionASPathPnd based on InetAutonomousSystemNumber"""
    defaultValue = 0


_TRPAdminPSDefaultActionASPathPnd_Type.__name__ = "InetAutonomousSystemNumber"
_TRPAdminPSDefaultActionASPathPnd_Object = MibTableColumn
tRPAdminPSDefaultActionASPathPnd = _TRPAdminPSDefaultActionASPathPnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 23),
    _TRPAdminPSDefaultActionASPathPnd_Type()
)
tRPAdminPSDefaultActionASPathPnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionASPathPnd.setStatus("current")


class _TRPAdminPSDefActMcRedirSvcId_Type(TmnxServId):
    """Custom type tRPAdminPSDefActMcRedirSvcId based on TmnxServId"""
    defaultValue = 0


_TRPAdminPSDefActMcRedirSvcId_Type.__name__ = "TmnxServId"
_TRPAdminPSDefActMcRedirSvcId_Object = MibTableColumn
tRPAdminPSDefActMcRedirSvcId = _TRPAdminPSDefActMcRedirSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 30),
    _TRPAdminPSDefActMcRedirSvcId_Type()
)
tRPAdminPSDefActMcRedirSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActMcRedirSvcId.setStatus("current")


class _TRPAdminPSDefActMcRedirIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tRPAdminPSDefActMcRedirIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TRPAdminPSDefActMcRedirIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TRPAdminPSDefActMcRedirIfIndex_Object = MibTableColumn
tRPAdminPSDefActMcRedirIfIndex = _TRPAdminPSDefActMcRedirIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 31),
    _TRPAdminPSDefActMcRedirIfIndex_Type()
)
tRPAdminPSDefActMcRedirIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActMcRedirIfIndex.setStatus("current")


class _TRPAdminPSDefActionMetricSource_Type(TPolicyActionMetricSource):
    """Custom type tRPAdminPSDefActionMetricSource based on TPolicyActionMetricSource"""
    defaultValue = 2


_TRPAdminPSDefActionMetricSource_Type.__name__ = "TPolicyActionMetricSource"
_TRPAdminPSDefActionMetricSource_Object = MibTableColumn
tRPAdminPSDefActionMetricSource = _TRPAdminPSDefActionMetricSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 32),
    _TRPAdminPSDefActionMetricSource_Type()
)
tRPAdminPSDefActionMetricSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionMetricSource.setStatus("current")


class _TRPAdminPSDefActionAigpMetric_Type(TPolicyEntryAigpMetricEdit):
    """Custom type tRPAdminPSDefActionAigpMetric based on TPolicyEntryAigpMetricEdit"""
    defaultValue = 1


_TRPAdminPSDefActionAigpMetric_Type.__name__ = "TPolicyEntryAigpMetricEdit"
_TRPAdminPSDefActionAigpMetric_Object = MibTableColumn
tRPAdminPSDefActionAigpMetric = _TRPAdminPSDefActionAigpMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 33),
    _TRPAdminPSDefActionAigpMetric_Type()
)
tRPAdminPSDefActionAigpMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAigpMetric.setStatus("current")


class _TRPAdminPSDefActnAigpMetricVal_Type(Unsigned32):
    """Custom type tRPAdminPSDefActnAigpMetricVal based on Unsigned32"""
    defaultValue = 0


_TRPAdminPSDefActnAigpMetricVal_Type.__name__ = "Unsigned32"
_TRPAdminPSDefActnAigpMetricVal_Object = MibTableColumn
tRPAdminPSDefActnAigpMetricVal = _TRPAdminPSDefActnAigpMetricVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 34),
    _TRPAdminPSDefActnAigpMetricVal_Type()
)
tRPAdminPSDefActnAigpMetricVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActnAigpMetricVal.setStatus("current")


class _TRPAdminPSDefActnSrcClassIndex_Type(Unsigned32):
    """Custom type tRPAdminPSDefActnSrcClassIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TRPAdminPSDefActnSrcClassIndex_Type.__name__ = "Unsigned32"
_TRPAdminPSDefActnSrcClassIndex_Object = MibTableColumn
tRPAdminPSDefActnSrcClassIndex = _TRPAdminPSDefActnSrcClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 35),
    _TRPAdminPSDefActnSrcClassIndex_Type()
)
tRPAdminPSDefActnSrcClassIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActnSrcClassIndex.setStatus("current")


class _TRPAdminPSDefActnDstClassIndex_Type(Unsigned32):
    """Custom type tRPAdminPSDefActnDstClassIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TRPAdminPSDefActnDstClassIndex_Type.__name__ = "Unsigned32"
_TRPAdminPSDefActnDstClassIndex_Object = MibTableColumn
tRPAdminPSDefActnDstClassIndex = _TRPAdminPSDefActnDstClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 36),
    _TRPAdminPSDefActnDstClassIndex_Type()
)
tRPAdminPSDefActnDstClassIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActnDstClassIndex.setStatus("current")


class _TRPAdminPSDefActnOrigValidState_Type(Integer32):
    """Custom type tRPAdminPSDefActnOrigValidState based on Integer32"""
    defaultValue = 0

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
        *(("notApplicable", 0),
          ("valid", 1),
          ("notFound", 2),
          ("invalid", 3))
    )


_TRPAdminPSDefActnOrigValidState_Type.__name__ = "Integer32"
_TRPAdminPSDefActnOrigValidState_Object = MibTableColumn
tRPAdminPSDefActnOrigValidState = _TRPAdminPSDefActnOrigValidState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 37),
    _TRPAdminPSDefActnOrigValidState_Type()
)
tRPAdminPSDefActnOrigValidState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActnOrigValidState.setStatus("current")
_TRPAdminPSParamsTable_Object = MibTable
tRPAdminPSParamsTable = _TRPAdminPSParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 7)
)
if mibBuilder.loadTexts:
    tRPAdminPSParamsTable.setStatus("current")
_TRPAdminPSParamsEntry_Object = MibTableRow
tRPAdminPSParamsEntry = _TRPAdminPSParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 7, 1)
)
tRPAdminPSParamsEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSNameEntryIndex"),
)
if mibBuilder.loadTexts:
    tRPAdminPSParamsEntry.setStatus("current")
_TRPAdminPSNameEntryIndex_Type = TPolicyStatementEntryID
_TRPAdminPSNameEntryIndex_Object = MibTableColumn
tRPAdminPSNameEntryIndex = _TRPAdminPSNameEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 7, 1, 1),
    _TRPAdminPSNameEntryIndex_Type()
)
tRPAdminPSNameEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminPSNameEntryIndex.setStatus("current")
_TRPAdminPSParamsRowStatus_Type = RowStatus
_TRPAdminPSParamsRowStatus_Object = MibTableColumn
tRPAdminPSParamsRowStatus = _TRPAdminPSParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 7, 1, 2),
    _TRPAdminPSParamsRowStatus_Type()
)
tRPAdminPSParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSParamsRowStatus.setStatus("current")


class _TRPAdminPSParamsDescription_Type(TItemDescription):
    """Custom type tRPAdminPSParamsDescription based on TItemDescription"""
    defaultHexValue = ""


_TRPAdminPSParamsDescription_Type.__name__ = "TItemDescription"
_TRPAdminPSParamsDescription_Object = MibTableColumn
tRPAdminPSParamsDescription = _TRPAdminPSParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 7, 1, 3),
    _TRPAdminPSParamsDescription_Type()
)
tRPAdminPSParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSParamsDescription.setStatus("current")
_TRPAdminPSParamsAction_Type = TPolicyEntryAction
_TRPAdminPSParamsAction_Object = MibTableColumn
tRPAdminPSParamsAction = _TRPAdminPSParamsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 7, 1, 4),
    _TRPAdminPSParamsAction_Type()
)
tRPAdminPSParamsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSParamsAction.setStatus("current")
_TRPAdminPSParamsCreationOrigin_Type = TmnxCreateOrigin
_TRPAdminPSParamsCreationOrigin_Object = MibTableColumn
tRPAdminPSParamsCreationOrigin = _TRPAdminPSParamsCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 7, 1, 5),
    _TRPAdminPSParamsCreationOrigin_Type()
)
tRPAdminPSParamsCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPAdminPSParamsCreationOrigin.setStatus("current")
_TRPAdminPSAcceptActionParamsTable_Object = MibTable
tRPAdminPSAcceptActionParamsTable = _TRPAdminPSAcceptActionParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8)
)
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionParamsTable.setStatus("current")
_TRPAdminPSAcceptActionParamsEntry_Object = MibTableRow
tRPAdminPSAcceptActionParamsEntry = _TRPAdminPSAcceptActionParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1)
)
tRPAdminPSAcceptActionParamsEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSNameEntryIndex"),
)
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionParamsEntry.setStatus("current")


class _TRPAdminPSAcceptActionASPath_Type(TPolicyEntryEdit):
    """Custom type tRPAdminPSAcceptActionASPath based on TPolicyEntryEdit"""
    defaultValue = 1


_TRPAdminPSAcceptActionASPath_Type.__name__ = "TPolicyEntryEdit"
_TRPAdminPSAcceptActionASPath_Object = MibTableColumn
tRPAdminPSAcceptActionASPath = _TRPAdminPSAcceptActionASPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 1),
    _TRPAdminPSAcceptActionASPath_Type()
)
tRPAdminPSAcceptActionASPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionASPath.setStatus("current")


class _TRPAdminPSAcceptActionASPathName_Type(TASPathName):
    """Custom type tRPAdminPSAcceptActionASPathName based on TASPathName"""
    defaultHexValue = ""


_TRPAdminPSAcceptActionASPathName_Type.__name__ = "TASPathName"
_TRPAdminPSAcceptActionASPathName_Object = MibTableColumn
tRPAdminPSAcceptActionASPathName = _TRPAdminPSAcceptActionASPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 2),
    _TRPAdminPSAcceptActionASPathName_Type()
)
tRPAdminPSAcceptActionASPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionASPathName.setStatus("current")


class _TRPAdminPSAcceptActionASPathPrependAS_Type(TmnxBgpAutonomousSystem):
    """Custom type tRPAdminPSAcceptActionASPathPrependAS based on TmnxBgpAutonomousSystem"""
    defaultValue = 0


_TRPAdminPSAcceptActionASPathPrependAS_Type.__name__ = "TmnxBgpAutonomousSystem"
_TRPAdminPSAcceptActionASPathPrependAS_Object = MibTableColumn
tRPAdminPSAcceptActionASPathPrependAS = _TRPAdminPSAcceptActionASPathPrependAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 3),
    _TRPAdminPSAcceptActionASPathPrependAS_Type()
)
tRPAdminPSAcceptActionASPathPrependAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionASPathPrependAS.setStatus("obsolete")


class _TRPAdminPSAcceptActionASPathPrependCount_Type(Integer32):
    """Custom type tRPAdminPSAcceptActionASPathPrependCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_TRPAdminPSAcceptActionASPathPrependCount_Type.__name__ = "Integer32"
_TRPAdminPSAcceptActionASPathPrependCount_Object = MibTableColumn
tRPAdminPSAcceptActionASPathPrependCount = _TRPAdminPSAcceptActionASPathPrependCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 4),
    _TRPAdminPSAcceptActionASPathPrependCount_Type()
)
tRPAdminPSAcceptActionASPathPrependCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionASPathPrependCount.setStatus("current")


class _TRPAdminPSAcceptActionCommunity1_Type(TPolicyEntryEdit):
    """Custom type tRPAdminPSAcceptActionCommunity1 based on TPolicyEntryEdit"""
    defaultValue = 1


_TRPAdminPSAcceptActionCommunity1_Type.__name__ = "TPolicyEntryEdit"
_TRPAdminPSAcceptActionCommunity1_Object = MibTableColumn
tRPAdminPSAcceptActionCommunity1 = _TRPAdminPSAcceptActionCommunity1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 5),
    _TRPAdminPSAcceptActionCommunity1_Type()
)
tRPAdminPSAcceptActionCommunity1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionCommunity1.setStatus("obsolete")


class _TRPAdminPSAcceptActionCommunityName1_Type(TCommunityName):
    """Custom type tRPAdminPSAcceptActionCommunityName1 based on TCommunityName"""
    defaultHexValue = ""


_TRPAdminPSAcceptActionCommunityName1_Type.__name__ = "TCommunityName"
_TRPAdminPSAcceptActionCommunityName1_Object = MibTableColumn
tRPAdminPSAcceptActionCommunityName1 = _TRPAdminPSAcceptActionCommunityName1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 6),
    _TRPAdminPSAcceptActionCommunityName1_Type()
)
tRPAdminPSAcceptActionCommunityName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionCommunityName1.setStatus("obsolete")


class _TRPAdminPSAcceptActionCommunity2_Type(TPolicyEntryEdit):
    """Custom type tRPAdminPSAcceptActionCommunity2 based on TPolicyEntryEdit"""
    defaultValue = 1


_TRPAdminPSAcceptActionCommunity2_Type.__name__ = "TPolicyEntryEdit"
_TRPAdminPSAcceptActionCommunity2_Object = MibTableColumn
tRPAdminPSAcceptActionCommunity2 = _TRPAdminPSAcceptActionCommunity2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 7),
    _TRPAdminPSAcceptActionCommunity2_Type()
)
tRPAdminPSAcceptActionCommunity2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionCommunity2.setStatus("obsolete")


class _TRPAdminPSAcceptActionCommunityName2_Type(TCommunityName):
    """Custom type tRPAdminPSAcceptActionCommunityName2 based on TCommunityName"""
    defaultHexValue = ""


_TRPAdminPSAcceptActionCommunityName2_Type.__name__ = "TCommunityName"
_TRPAdminPSAcceptActionCommunityName2_Object = MibTableColumn
tRPAdminPSAcceptActionCommunityName2 = _TRPAdminPSAcceptActionCommunityName2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 8),
    _TRPAdminPSAcceptActionCommunityName2_Type()
)
tRPAdminPSAcceptActionCommunityName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionCommunityName2.setStatus("obsolete")


class _TRPAdminPSAcceptActionOrigin_Type(TPolicyEntryCriteriaOrigin):
    """Custom type tRPAdminPSAcceptActionOrigin based on TPolicyEntryCriteriaOrigin"""
    defaultValue = 1


_TRPAdminPSAcceptActionOrigin_Type.__name__ = "TPolicyEntryCriteriaOrigin"
_TRPAdminPSAcceptActionOrigin_Object = MibTableColumn
tRPAdminPSAcceptActionOrigin = _TRPAdminPSAcceptActionOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 9),
    _TRPAdminPSAcceptActionOrigin_Type()
)
tRPAdminPSAcceptActionOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionOrigin.setStatus("current")


class _TRPAdminPSAcceptActionLocalPreferenceSet_Type(TruthValue):
    """Custom type tRPAdminPSAcceptActionLocalPreferenceSet based on TruthValue"""
    defaultValue = 2


_TRPAdminPSAcceptActionLocalPreferenceSet_Type.__name__ = "TruthValue"
_TRPAdminPSAcceptActionLocalPreferenceSet_Object = MibTableColumn
tRPAdminPSAcceptActionLocalPreferenceSet = _TRPAdminPSAcceptActionLocalPreferenceSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 10),
    _TRPAdminPSAcceptActionLocalPreferenceSet_Type()
)
tRPAdminPSAcceptActionLocalPreferenceSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionLocalPreferenceSet.setStatus("current")


class _TRPAdminPSAcceptActionLocalPreference_Type(TmnxBgpLocalPreference):
    """Custom type tRPAdminPSAcceptActionLocalPreference based on TmnxBgpLocalPreference"""
    defaultValue = 0


_TRPAdminPSAcceptActionLocalPreference_Type.__name__ = "TmnxBgpLocalPreference"
_TRPAdminPSAcceptActionLocalPreference_Object = MibTableColumn
tRPAdminPSAcceptActionLocalPreference = _TRPAdminPSAcceptActionLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 11),
    _TRPAdminPSAcceptActionLocalPreference_Type()
)
tRPAdminPSAcceptActionLocalPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionLocalPreference.setStatus("current")


class _TRPAdminPSAcceptActionMetric_Type(TPolicyEntryEdit):
    """Custom type tRPAdminPSAcceptActionMetric based on TPolicyEntryEdit"""
    defaultValue = 1


_TRPAdminPSAcceptActionMetric_Type.__name__ = "TPolicyEntryEdit"
_TRPAdminPSAcceptActionMetric_Object = MibTableColumn
tRPAdminPSAcceptActionMetric = _TRPAdminPSAcceptActionMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 12),
    _TRPAdminPSAcceptActionMetric_Type()
)
tRPAdminPSAcceptActionMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionMetric.setStatus("current")


class _TRPAdminPSAcceptActionMetricValue_Type(Unsigned32):
    """Custom type tRPAdminPSAcceptActionMetricValue based on Unsigned32"""
    defaultValue = 0


_TRPAdminPSAcceptActionMetricValue_Type.__name__ = "Unsigned32"
_TRPAdminPSAcceptActionMetricValue_Object = MibTableColumn
tRPAdminPSAcceptActionMetricValue = _TRPAdminPSAcceptActionMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 13),
    _TRPAdminPSAcceptActionMetricValue_Type()
)
tRPAdminPSAcceptActionMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionMetricValue.setStatus("current")


class _TRPAdminPSAcceptActionPreference_Type(TmnxBgpPreference):
    """Custom type tRPAdminPSAcceptActionPreference based on TmnxBgpPreference"""
    defaultValue = 0


_TRPAdminPSAcceptActionPreference_Type.__name__ = "TmnxBgpPreference"
_TRPAdminPSAcceptActionPreference_Object = MibTableColumn
tRPAdminPSAcceptActionPreference = _TRPAdminPSAcceptActionPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 15),
    _TRPAdminPSAcceptActionPreference_Type()
)
tRPAdminPSAcceptActionPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionPreference.setStatus("current")


class _TRPAdminPSAcceptActionDamping_Type(TDampingName):
    """Custom type tRPAdminPSAcceptActionDamping based on TDampingName"""
    defaultHexValue = ""


_TRPAdminPSAcceptActionDamping_Type.__name__ = "TDampingName"
_TRPAdminPSAcceptActionDamping_Object = MibTableColumn
tRPAdminPSAcceptActionDamping = _TRPAdminPSAcceptActionDamping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 16),
    _TRPAdminPSAcceptActionDamping_Type()
)
tRPAdminPSAcceptActionDamping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionDamping.setStatus("current")


class _TRPAdminPSAcceptActionNextHopSelf_Type(TruthValue):
    """Custom type tRPAdminPSAcceptActionNextHopSelf based on TruthValue"""
    defaultValue = 2


_TRPAdminPSAcceptActionNextHopSelf_Type.__name__ = "TruthValue"
_TRPAdminPSAcceptActionNextHopSelf_Object = MibTableColumn
tRPAdminPSAcceptActionNextHopSelf = _TRPAdminPSAcceptActionNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 17),
    _TRPAdminPSAcceptActionNextHopSelf_Type()
)
tRPAdminPSAcceptActionNextHopSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionNextHopSelf.setStatus("current")


class _TRPAdminPSAcceptActionNextHop_Type(IpAddress):
    """Custom type tRPAdminPSAcceptActionNextHop based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_TRPAdminPSAcceptActionNextHop_Type.__name__ = "IpAddress"
_TRPAdminPSAcceptActionNextHop_Object = MibTableColumn
tRPAdminPSAcceptActionNextHop = _TRPAdminPSAcceptActionNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 18),
    _TRPAdminPSAcceptActionNextHop_Type()
)
tRPAdminPSAcceptActionNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionNextHop.setStatus("current")


class _TRPAdminPSAcceptActionTag_Type(TPolicyActionTag):
    """Custom type tRPAdminPSAcceptActionTag based on TPolicyActionTag"""
    defaultValue = 0


_TRPAdminPSAcceptActionTag_Type.__name__ = "TPolicyActionTag"
_TRPAdminPSAcceptActionTag_Object = MibTableColumn
tRPAdminPSAcceptActionTag = _TRPAdminPSAcceptActionTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 19),
    _TRPAdminPSAcceptActionTag_Type()
)
tRPAdminPSAcceptActionTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionTag.setStatus("current")


class _TRPAdminPSAcceptActionOspfType_Type(TOspfRouteType):
    """Custom type tRPAdminPSAcceptActionOspfType based on TOspfRouteType"""
    defaultValue = 0


_TRPAdminPSAcceptActionOspfType_Type.__name__ = "TOspfRouteType"
_TRPAdminPSAcceptActionOspfType_Object = MibTableColumn
tRPAdminPSAcceptActionOspfType = _TRPAdminPSAcceptActionOspfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 20),
    _TRPAdminPSAcceptActionOspfType_Type()
)
tRPAdminPSAcceptActionOspfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionOspfType.setStatus("current")
_TRPAdminPSAcptActInetNextHopType_Type = InetAddressType
_TRPAdminPSAcptActInetNextHopType_Object = MibTableColumn
tRPAdminPSAcptActInetNextHopType = _TRPAdminPSAcptActInetNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 21),
    _TRPAdminPSAcptActInetNextHopType_Type()
)
tRPAdminPSAcptActInetNextHopType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActInetNextHopType.setStatus("current")


class _TRPAdminPSAcptActInetNextHop_Type(InetAddress):
    """Custom type tRPAdminPSAcptActInetNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TRPAdminPSAcptActInetNextHop_Type.__name__ = "InetAddress"
_TRPAdminPSAcptActInetNextHop_Object = MibTableColumn
tRPAdminPSAcptActInetNextHop = _TRPAdminPSAcptActInetNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 22),
    _TRPAdminPSAcptActInetNextHop_Type()
)
tRPAdminPSAcptActInetNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActInetNextHop.setStatus("current")


class _TRPAdminPSAcceptActionASPathPend_Type(InetAutonomousSystemNumber):
    """Custom type tRPAdminPSAcceptActionASPathPend based on InetAutonomousSystemNumber"""
    defaultValue = 0


_TRPAdminPSAcceptActionASPathPend_Type.__name__ = "InetAutonomousSystemNumber"
_TRPAdminPSAcceptActionASPathPend_Object = MibTableColumn
tRPAdminPSAcceptActionASPathPend = _TRPAdminPSAcceptActionASPathPend_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 23),
    _TRPAdminPSAcceptActionASPathPend_Type()
)
tRPAdminPSAcceptActionASPathPend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionASPathPend.setStatus("current")


class _TRPAdminPSAcceptActionFC_Type(TNamedItemOrEmpty):
    """Custom type tRPAdminPSAcceptActionFC based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TRPAdminPSAcceptActionFC_Type.__name__ = "TNamedItemOrEmpty"
_TRPAdminPSAcceptActionFC_Object = MibTableColumn
tRPAdminPSAcceptActionFC = _TRPAdminPSAcceptActionFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 24),
    _TRPAdminPSAcceptActionFC_Type()
)
tRPAdminPSAcceptActionFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionFC.setStatus("current")


class _TRPAdminPSAcceptActionFCPriority_Type(TPriorityOrUndefined):
    """Custom type tRPAdminPSAcceptActionFCPriority based on TPriorityOrUndefined"""
    defaultValue = 0


_TRPAdminPSAcceptActionFCPriority_Type.__name__ = "TPriorityOrUndefined"
_TRPAdminPSAcceptActionFCPriority_Object = MibTableColumn
tRPAdminPSAcceptActionFCPriority = _TRPAdminPSAcceptActionFCPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 25),
    _TRPAdminPSAcceptActionFCPriority_Type()
)
tRPAdminPSAcceptActionFCPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionFCPriority.setStatus("current")


class _TRPAdminPSAcptActMcRedirSvcId_Type(TmnxServId):
    """Custom type tRPAdminPSAcptActMcRedirSvcId based on TmnxServId"""
    defaultValue = 0


_TRPAdminPSAcptActMcRedirSvcId_Type.__name__ = "TmnxServId"
_TRPAdminPSAcptActMcRedirSvcId_Object = MibTableColumn
tRPAdminPSAcptActMcRedirSvcId = _TRPAdminPSAcptActMcRedirSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 30),
    _TRPAdminPSAcptActMcRedirSvcId_Type()
)
tRPAdminPSAcptActMcRedirSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActMcRedirSvcId.setStatus("current")


class _TRPAdminPSAcptActMcRedirIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tRPAdminPSAcptActMcRedirIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TRPAdminPSAcptActMcRedirIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TRPAdminPSAcptActMcRedirIfIndex_Object = MibTableColumn
tRPAdminPSAcptActMcRedirIfIndex = _TRPAdminPSAcptActMcRedirIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 31),
    _TRPAdminPSAcptActMcRedirIfIndex_Type()
)
tRPAdminPSAcptActMcRedirIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActMcRedirIfIndex.setStatus("current")


class _TRPAdminPSAcptActnMetricSource_Type(TPolicyActionMetricSource):
    """Custom type tRPAdminPSAcptActnMetricSource based on TPolicyActionMetricSource"""
    defaultValue = 2


_TRPAdminPSAcptActnMetricSource_Type.__name__ = "TPolicyActionMetricSource"
_TRPAdminPSAcptActnMetricSource_Object = MibTableColumn
tRPAdminPSAcptActnMetricSource = _TRPAdminPSAcptActnMetricSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 32),
    _TRPAdminPSAcptActnMetricSource_Type()
)
tRPAdminPSAcptActnMetricSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActnMetricSource.setStatus("current")


class _TRPAdminPSAcptActionAigpMetric_Type(TPolicyEntryAigpMetricEdit):
    """Custom type tRPAdminPSAcptActionAigpMetric based on TPolicyEntryAigpMetricEdit"""
    defaultValue = 1


_TRPAdminPSAcptActionAigpMetric_Type.__name__ = "TPolicyEntryAigpMetricEdit"
_TRPAdminPSAcptActionAigpMetric_Object = MibTableColumn
tRPAdminPSAcptActionAigpMetric = _TRPAdminPSAcptActionAigpMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 33),
    _TRPAdminPSAcptActionAigpMetric_Type()
)
tRPAdminPSAcptActionAigpMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActionAigpMetric.setStatus("current")


class _TRPAdminPSAcptActnAigpMetricVal_Type(Unsigned32):
    """Custom type tRPAdminPSAcptActnAigpMetricVal based on Unsigned32"""
    defaultValue = 0


_TRPAdminPSAcptActnAigpMetricVal_Type.__name__ = "Unsigned32"
_TRPAdminPSAcptActnAigpMetricVal_Object = MibTableColumn
tRPAdminPSAcptActnAigpMetricVal = _TRPAdminPSAcptActnAigpMetricVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 34),
    _TRPAdminPSAcptActnAigpMetricVal_Type()
)
tRPAdminPSAcptActnAigpMetricVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActnAigpMetricVal.setStatus("current")


class _TRPAdminPSAcptActnSrcClassIndex_Type(Unsigned32):
    """Custom type tRPAdminPSAcptActnSrcClassIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TRPAdminPSAcptActnSrcClassIndex_Type.__name__ = "Unsigned32"
_TRPAdminPSAcptActnSrcClassIndex_Object = MibTableColumn
tRPAdminPSAcptActnSrcClassIndex = _TRPAdminPSAcptActnSrcClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 35),
    _TRPAdminPSAcptActnSrcClassIndex_Type()
)
tRPAdminPSAcptActnSrcClassIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActnSrcClassIndex.setStatus("current")


class _TRPAdminPSAcptActnDstClassIndex_Type(Unsigned32):
    """Custom type tRPAdminPSAcptActnDstClassIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TRPAdminPSAcptActnDstClassIndex_Type.__name__ = "Unsigned32"
_TRPAdminPSAcptActnDstClassIndex_Object = MibTableColumn
tRPAdminPSAcptActnDstClassIndex = _TRPAdminPSAcptActnDstClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 36),
    _TRPAdminPSAcptActnDstClassIndex_Type()
)
tRPAdminPSAcptActnDstClassIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActnDstClassIndex.setStatus("current")


class _TRPAdminPSAcptActnOrigValidState_Type(Integer32):
    """Custom type tRPAdminPSAcptActnOrigValidState based on Integer32"""
    defaultValue = 0

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
        *(("notApplicable", 0),
          ("valid", 1),
          ("notFound", 2),
          ("invalid", 3))
    )


_TRPAdminPSAcptActnOrigValidState_Type.__name__ = "Integer32"
_TRPAdminPSAcptActnOrigValidState_Object = MibTableColumn
tRPAdminPSAcptActnOrigValidState = _TRPAdminPSAcptActnOrigValidState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 37),
    _TRPAdminPSAcptActnOrigValidState_Type()
)
tRPAdminPSAcptActnOrigValidState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActnOrigValidState.setStatus("current")
_TRPAdminPSToCriteriaTable_Object = MibTable
tRPAdminPSToCriteriaTable = _TRPAdminPSToCriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9)
)
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaTable.setStatus("current")
_TRPAdminPSToCriteriaEntry_Object = MibTableRow
tRPAdminPSToCriteriaEntry = _TRPAdminPSToCriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1)
)
tRPAdminPSToCriteriaEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaIndex"),
)
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaEntry.setStatus("current")
_TRPAdminPSToCriteriaIndex_Type = TPolicyStatementEntryID
_TRPAdminPSToCriteriaIndex_Object = MibTableColumn
tRPAdminPSToCriteriaIndex = _TRPAdminPSToCriteriaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 1),
    _TRPAdminPSToCriteriaIndex_Type()
)
tRPAdminPSToCriteriaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaIndex.setStatus("current")
_TRPAdminPSToCriteriaRowStatus_Type = RowStatus
_TRPAdminPSToCriteriaRowStatus_Object = MibTableColumn
tRPAdminPSToCriteriaRowStatus = _TRPAdminPSToCriteriaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 2),
    _TRPAdminPSToCriteriaRowStatus_Type()
)
tRPAdminPSToCriteriaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaRowStatus.setStatus("current")


class _TRPAdminPSToCriteriaProtocol_Type(TRoutePolicyProtocol):
    """Custom type tRPAdminPSToCriteriaProtocol based on TRoutePolicyProtocol"""
    defaultValue = 1


_TRPAdminPSToCriteriaProtocol_Type.__name__ = "TRoutePolicyProtocol"
_TRPAdminPSToCriteriaProtocol_Object = MibTableColumn
tRPAdminPSToCriteriaProtocol = _TRPAdminPSToCriteriaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 3),
    _TRPAdminPSToCriteriaProtocol_Type()
)
tRPAdminPSToCriteriaProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaProtocol.setStatus("current")


class _TRPAdminPSToCriteriaNeighborIpAddr_Type(IpAddress):
    """Custom type tRPAdminPSToCriteriaNeighborIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TRPAdminPSToCriteriaNeighborIpAddr_Type.__name__ = "IpAddress"
_TRPAdminPSToCriteriaNeighborIpAddr_Object = MibTableColumn
tRPAdminPSToCriteriaNeighborIpAddr = _TRPAdminPSToCriteriaNeighborIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 4),
    _TRPAdminPSToCriteriaNeighborIpAddr_Type()
)
tRPAdminPSToCriteriaNeighborIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaNeighborIpAddr.setStatus("current")


class _TRPAdminPSToCriteriaNeighborPrefixList_Type(TPrefixListName):
    """Custom type tRPAdminPSToCriteriaNeighborPrefixList based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSToCriteriaNeighborPrefixList_Type.__name__ = "TPrefixListName"
_TRPAdminPSToCriteriaNeighborPrefixList_Object = MibTableColumn
tRPAdminPSToCriteriaNeighborPrefixList = _TRPAdminPSToCriteriaNeighborPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 5),
    _TRPAdminPSToCriteriaNeighborPrefixList_Type()
)
tRPAdminPSToCriteriaNeighborPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaNeighborPrefixList.setStatus("current")


class _TRPAdminPSToCriteriaIsisLevel_Type(TIsisLevel):
    """Custom type tRPAdminPSToCriteriaIsisLevel based on TIsisLevel"""
    defaultValue = 0


_TRPAdminPSToCriteriaIsisLevel_Type.__name__ = "TIsisLevel"
_TRPAdminPSToCriteriaIsisLevel_Object = MibTableColumn
tRPAdminPSToCriteriaIsisLevel = _TRPAdminPSToCriteriaIsisLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 7),
    _TRPAdminPSToCriteriaIsisLevel_Type()
)
tRPAdminPSToCriteriaIsisLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaIsisLevel.setStatus("current")


class _TRPAdminPSToCriteriaPrefixList1_Type(TPrefixListName):
    """Custom type tRPAdminPSToCriteriaPrefixList1 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSToCriteriaPrefixList1_Type.__name__ = "TPrefixListName"
_TRPAdminPSToCriteriaPrefixList1_Object = MibTableColumn
tRPAdminPSToCriteriaPrefixList1 = _TRPAdminPSToCriteriaPrefixList1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 8),
    _TRPAdminPSToCriteriaPrefixList1_Type()
)
tRPAdminPSToCriteriaPrefixList1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaPrefixList1.setStatus("current")


class _TRPAdminPSToCriteriaPrefixList2_Type(TPrefixListName):
    """Custom type tRPAdminPSToCriteriaPrefixList2 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSToCriteriaPrefixList2_Type.__name__ = "TPrefixListName"
_TRPAdminPSToCriteriaPrefixList2_Object = MibTableColumn
tRPAdminPSToCriteriaPrefixList2 = _TRPAdminPSToCriteriaPrefixList2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 9),
    _TRPAdminPSToCriteriaPrefixList2_Type()
)
tRPAdminPSToCriteriaPrefixList2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaPrefixList2.setStatus("current")


class _TRPAdminPSToCriteriaPrefixList3_Type(TPrefixListName):
    """Custom type tRPAdminPSToCriteriaPrefixList3 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSToCriteriaPrefixList3_Type.__name__ = "TPrefixListName"
_TRPAdminPSToCriteriaPrefixList3_Object = MibTableColumn
tRPAdminPSToCriteriaPrefixList3 = _TRPAdminPSToCriteriaPrefixList3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 10),
    _TRPAdminPSToCriteriaPrefixList3_Type()
)
tRPAdminPSToCriteriaPrefixList3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaPrefixList3.setStatus("current")


class _TRPAdminPSToCriteriaPrefixList4_Type(TPrefixListName):
    """Custom type tRPAdminPSToCriteriaPrefixList4 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSToCriteriaPrefixList4_Type.__name__ = "TPrefixListName"
_TRPAdminPSToCriteriaPrefixList4_Object = MibTableColumn
tRPAdminPSToCriteriaPrefixList4 = _TRPAdminPSToCriteriaPrefixList4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 11),
    _TRPAdminPSToCriteriaPrefixList4_Type()
)
tRPAdminPSToCriteriaPrefixList4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaPrefixList4.setStatus("current")


class _TRPAdminPSToCriteriaPrefixList5_Type(TPrefixListName):
    """Custom type tRPAdminPSToCriteriaPrefixList5 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSToCriteriaPrefixList5_Type.__name__ = "TPrefixListName"
_TRPAdminPSToCriteriaPrefixList5_Object = MibTableColumn
tRPAdminPSToCriteriaPrefixList5 = _TRPAdminPSToCriteriaPrefixList5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 12),
    _TRPAdminPSToCriteriaPrefixList5_Type()
)
tRPAdminPSToCriteriaPrefixList5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaPrefixList5.setStatus("current")
_TRPAdminPSToCritNbrInetAddrType_Type = InetAddressType
_TRPAdminPSToCritNbrInetAddrType_Object = MibTableColumn
tRPAdminPSToCritNbrInetAddrType = _TRPAdminPSToCritNbrInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 13),
    _TRPAdminPSToCritNbrInetAddrType_Type()
)
tRPAdminPSToCritNbrInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCritNbrInetAddrType.setStatus("current")


class _TRPAdminPSToCritNbrInetAddr_Type(InetAddress):
    """Custom type tRPAdminPSToCritNbrInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TRPAdminPSToCritNbrInetAddr_Type.__name__ = "InetAddress"
_TRPAdminPSToCritNbrInetAddr_Object = MibTableColumn
tRPAdminPSToCritNbrInetAddr = _TRPAdminPSToCritNbrInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 14),
    _TRPAdminPSToCritNbrInetAddr_Type()
)
tRPAdminPSToCritNbrInetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCritNbrInetAddr.setStatus("current")


class _TRPAdminPSToCriteriaInstanceId_Type(Unsigned32):
    """Custom type tRPAdminPSToCriteriaInstanceId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
        ValueRangeConstraint(64, 95),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TRPAdminPSToCriteriaInstanceId_Type.__name__ = "Unsigned32"
_TRPAdminPSToCriteriaInstanceId_Object = MibTableColumn
tRPAdminPSToCriteriaInstanceId = _TRPAdminPSToCriteriaInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 15),
    _TRPAdminPSToCriteriaInstanceId_Type()
)
tRPAdminPSToCriteriaInstanceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaInstanceId.setStatus("current")
_TRPAdminPSFromCriteriaTable_Object = MibTable
tRPAdminPSFromCriteriaTable = _TRPAdminPSFromCriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10)
)
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaTable.setStatus("current")
_TRPAdminPSFromCriteriaEntry_Object = MibTableRow
tRPAdminPSFromCriteriaEntry = _TRPAdminPSFromCriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1)
)
tRPAdminPSFromCriteriaEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIndex"),
)
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaEntry.setStatus("current")
_TRPAdminPSFromCriteriaIndex_Type = TPolicyStatementEntryID
_TRPAdminPSFromCriteriaIndex_Object = MibTableColumn
tRPAdminPSFromCriteriaIndex = _TRPAdminPSFromCriteriaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 1),
    _TRPAdminPSFromCriteriaIndex_Type()
)
tRPAdminPSFromCriteriaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaIndex.setStatus("current")
_TRPAdminPSFromCriteriaRowStatus_Type = RowStatus
_TRPAdminPSFromCriteriaRowStatus_Object = MibTableColumn
tRPAdminPSFromCriteriaRowStatus = _TRPAdminPSFromCriteriaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 2),
    _TRPAdminPSFromCriteriaRowStatus_Type()
)
tRPAdminPSFromCriteriaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaRowStatus.setStatus("current")


class _TRPAdminPSFromCriteriaProtocol_Type(TRoutePolicyProtocol):
    """Custom type tRPAdminPSFromCriteriaProtocol based on TRoutePolicyProtocol"""
    defaultValue = 1


_TRPAdminPSFromCriteriaProtocol_Type.__name__ = "TRoutePolicyProtocol"
_TRPAdminPSFromCriteriaProtocol_Object = MibTableColumn
tRPAdminPSFromCriteriaProtocol = _TRPAdminPSFromCriteriaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 3),
    _TRPAdminPSFromCriteriaProtocol_Type()
)
tRPAdminPSFromCriteriaProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaProtocol.setStatus("current")


class _TRPAdminPSFromCriteriaNeighborIpAddr_Type(IpAddress):
    """Custom type tRPAdminPSFromCriteriaNeighborIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TRPAdminPSFromCriteriaNeighborIpAddr_Type.__name__ = "IpAddress"
_TRPAdminPSFromCriteriaNeighborIpAddr_Object = MibTableColumn
tRPAdminPSFromCriteriaNeighborIpAddr = _TRPAdminPSFromCriteriaNeighborIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 4),
    _TRPAdminPSFromCriteriaNeighborIpAddr_Type()
)
tRPAdminPSFromCriteriaNeighborIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaNeighborIpAddr.setStatus("current")


class _TRPAdminPSFromCriteriaNeighborPrefixList_Type(TPrefixListName):
    """Custom type tRPAdminPSFromCriteriaNeighborPrefixList based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSFromCriteriaNeighborPrefixList_Type.__name__ = "TPrefixListName"
_TRPAdminPSFromCriteriaNeighborPrefixList_Object = MibTableColumn
tRPAdminPSFromCriteriaNeighborPrefixList = _TRPAdminPSFromCriteriaNeighborPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 5),
    _TRPAdminPSFromCriteriaNeighborPrefixList_Type()
)
tRPAdminPSFromCriteriaNeighborPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaNeighborPrefixList.setStatus("current")


class _TRPAdminPSFromCriteriaPrefixList1_Type(TPrefixListName):
    """Custom type tRPAdminPSFromCriteriaPrefixList1 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSFromCriteriaPrefixList1_Type.__name__ = "TPrefixListName"
_TRPAdminPSFromCriteriaPrefixList1_Object = MibTableColumn
tRPAdminPSFromCriteriaPrefixList1 = _TRPAdminPSFromCriteriaPrefixList1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 6),
    _TRPAdminPSFromCriteriaPrefixList1_Type()
)
tRPAdminPSFromCriteriaPrefixList1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaPrefixList1.setStatus("current")


class _TRPAdminPSFromCriteriaPrefixList2_Type(TPrefixListName):
    """Custom type tRPAdminPSFromCriteriaPrefixList2 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSFromCriteriaPrefixList2_Type.__name__ = "TPrefixListName"
_TRPAdminPSFromCriteriaPrefixList2_Object = MibTableColumn
tRPAdminPSFromCriteriaPrefixList2 = _TRPAdminPSFromCriteriaPrefixList2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 7),
    _TRPAdminPSFromCriteriaPrefixList2_Type()
)
tRPAdminPSFromCriteriaPrefixList2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaPrefixList2.setStatus("current")


class _TRPAdminPSFromCriteriaPrefixList3_Type(TPrefixListName):
    """Custom type tRPAdminPSFromCriteriaPrefixList3 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSFromCriteriaPrefixList3_Type.__name__ = "TPrefixListName"
_TRPAdminPSFromCriteriaPrefixList3_Object = MibTableColumn
tRPAdminPSFromCriteriaPrefixList3 = _TRPAdminPSFromCriteriaPrefixList3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 8),
    _TRPAdminPSFromCriteriaPrefixList3_Type()
)
tRPAdminPSFromCriteriaPrefixList3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaPrefixList3.setStatus("current")


class _TRPAdminPSFromCriteriaPrefixList4_Type(TPrefixListName):
    """Custom type tRPAdminPSFromCriteriaPrefixList4 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSFromCriteriaPrefixList4_Type.__name__ = "TPrefixListName"
_TRPAdminPSFromCriteriaPrefixList4_Object = MibTableColumn
tRPAdminPSFromCriteriaPrefixList4 = _TRPAdminPSFromCriteriaPrefixList4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 9),
    _TRPAdminPSFromCriteriaPrefixList4_Type()
)
tRPAdminPSFromCriteriaPrefixList4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaPrefixList4.setStatus("current")


class _TRPAdminPSFromCriteriaPrefixList5_Type(TPrefixListName):
    """Custom type tRPAdminPSFromCriteriaPrefixList5 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSFromCriteriaPrefixList5_Type.__name__ = "TPrefixListName"
_TRPAdminPSFromCriteriaPrefixList5_Object = MibTableColumn
tRPAdminPSFromCriteriaPrefixList5 = _TRPAdminPSFromCriteriaPrefixList5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 10),
    _TRPAdminPSFromCriteriaPrefixList5_Type()
)
tRPAdminPSFromCriteriaPrefixList5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaPrefixList5.setStatus("current")


class _TRPAdminPSFromCriteriaASPath_Type(TASPathName):
    """Custom type tRPAdminPSFromCriteriaASPath based on TASPathName"""
    defaultHexValue = ""


_TRPAdminPSFromCriteriaASPath_Type.__name__ = "TASPathName"
_TRPAdminPSFromCriteriaASPath_Object = MibTableColumn
tRPAdminPSFromCriteriaASPath = _TRPAdminPSFromCriteriaASPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 11),
    _TRPAdminPSFromCriteriaASPath_Type()
)
tRPAdminPSFromCriteriaASPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaASPath.setStatus("current")


class _TRPAdminPSFromCriteriaCommunity_Type(TCommunityName):
    """Custom type tRPAdminPSFromCriteriaCommunity based on TCommunityName"""
    defaultHexValue = ""


_TRPAdminPSFromCriteriaCommunity_Type.__name__ = "TCommunityName"
_TRPAdminPSFromCriteriaCommunity_Object = MibTableColumn
tRPAdminPSFromCriteriaCommunity = _TRPAdminPSFromCriteriaCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 12),
    _TRPAdminPSFromCriteriaCommunity_Type()
)
tRPAdminPSFromCriteriaCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaCommunity.setStatus("current")


class _TRPAdminPSFromCriteriaOrigin_Type(TPolicyEntryCriteriaOrigin):
    """Custom type tRPAdminPSFromCriteriaOrigin based on TPolicyEntryCriteriaOrigin"""
    defaultValue = 1


_TRPAdminPSFromCriteriaOrigin_Type.__name__ = "TPolicyEntryCriteriaOrigin"
_TRPAdminPSFromCriteriaOrigin_Object = MibTableColumn
tRPAdminPSFromCriteriaOrigin = _TRPAdminPSFromCriteriaOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 13),
    _TRPAdminPSFromCriteriaOrigin_Type()
)
tRPAdminPSFromCriteriaOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaOrigin.setStatus("current")


class _TRPAdminPSFromCriteriaOspfRouteType_Type(TOspfRouteType):
    """Custom type tRPAdminPSFromCriteriaOspfRouteType based on TOspfRouteType"""
    defaultValue = 0


_TRPAdminPSFromCriteriaOspfRouteType_Type.__name__ = "TOspfRouteType"
_TRPAdminPSFromCriteriaOspfRouteType_Object = MibTableColumn
tRPAdminPSFromCriteriaOspfRouteType = _TRPAdminPSFromCriteriaOspfRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 14),
    _TRPAdminPSFromCriteriaOspfRouteType_Type()
)
tRPAdminPSFromCriteriaOspfRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaOspfRouteType.setStatus("current")
_TRPAdminPSFromCriteriaArea_Type = IpAddress
_TRPAdminPSFromCriteriaArea_Object = MibTableColumn
tRPAdminPSFromCriteriaArea = _TRPAdminPSFromCriteriaArea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 16),
    _TRPAdminPSFromCriteriaArea_Type()
)
tRPAdminPSFromCriteriaArea.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaArea.setStatus("current")
_TRPAdminPSFromCriteriaAreaConfigured_Type = TruthValue
_TRPAdminPSFromCriteriaAreaConfigured_Object = MibTableColumn
tRPAdminPSFromCriteriaAreaConfigured = _TRPAdminPSFromCriteriaAreaConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 17),
    _TRPAdminPSFromCriteriaAreaConfigured_Type()
)
tRPAdminPSFromCriteriaAreaConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaAreaConfigured.setStatus("current")


class _TRPAdminPSFromCriteriaIsisLevel_Type(TIsisLevel):
    """Custom type tRPAdminPSFromCriteriaIsisLevel based on TIsisLevel"""
    defaultValue = 0


_TRPAdminPSFromCriteriaIsisLevel_Type.__name__ = "TIsisLevel"
_TRPAdminPSFromCriteriaIsisLevel_Object = MibTableColumn
tRPAdminPSFromCriteriaIsisLevel = _TRPAdminPSFromCriteriaIsisLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 18),
    _TRPAdminPSFromCriteriaIsisLevel_Type()
)
tRPAdminPSFromCriteriaIsisLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaIsisLevel.setStatus("current")


class _TRPAdminPSFromCriteriaIsisExternal_Type(TruthValue):
    """Custom type tRPAdminPSFromCriteriaIsisExternal based on TruthValue"""
    defaultValue = 2


_TRPAdminPSFromCriteriaIsisExternal_Type.__name__ = "TruthValue"
_TRPAdminPSFromCriteriaIsisExternal_Object = MibTableColumn
tRPAdminPSFromCriteriaIsisExternal = _TRPAdminPSFromCriteriaIsisExternal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 19),
    _TRPAdminPSFromCriteriaIsisExternal_Type()
)
tRPAdminPSFromCriteriaIsisExternal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaIsisExternal.setStatus("current")
_TRPAdminPSFromCriteriaIgmpHostPrefixList_Type = TPrefixListName
_TRPAdminPSFromCriteriaIgmpHostPrefixList_Object = MibTableColumn
tRPAdminPSFromCriteriaIgmpHostPrefixList = _TRPAdminPSFromCriteriaIgmpHostPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 20),
    _TRPAdminPSFromCriteriaIgmpHostPrefixList_Type()
)
tRPAdminPSFromCriteriaIgmpHostPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaIgmpHostPrefixList.setStatus("current")
_TRPAdminPSFromCriteriaGrpAddrPrefixList_Type = TPrefixListName
_TRPAdminPSFromCriteriaGrpAddrPrefixList_Object = MibTableColumn
tRPAdminPSFromCriteriaGrpAddrPrefixList = _TRPAdminPSFromCriteriaGrpAddrPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 21),
    _TRPAdminPSFromCriteriaGrpAddrPrefixList_Type()
)
tRPAdminPSFromCriteriaGrpAddrPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaGrpAddrPrefixList.setStatus("current")
_TRPAdminPSFromCriteriaSrcAddr_Type = IpAddress
_TRPAdminPSFromCriteriaSrcAddr_Object = MibTableColumn
tRPAdminPSFromCriteriaSrcAddr = _TRPAdminPSFromCriteriaSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 22),
    _TRPAdminPSFromCriteriaSrcAddr_Type()
)
tRPAdminPSFromCriteriaSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaSrcAddr.setStatus("current")
_TRPAdminPSFromCriteriaInterface_Type = TNamedItemOrEmpty
_TRPAdminPSFromCriteriaInterface_Object = MibTableColumn
tRPAdminPSFromCriteriaInterface = _TRPAdminPSFromCriteriaInterface_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 23),
    _TRPAdminPSFromCriteriaInterface_Type()
)
tRPAdminPSFromCriteriaInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaInterface.setStatus("current")


class _TRPAdminPSFromCriteriaTag_Type(TPolicyActionTag):
    """Custom type tRPAdminPSFromCriteriaTag based on TPolicyActionTag"""
    defaultValue = 0


_TRPAdminPSFromCriteriaTag_Type.__name__ = "TPolicyActionTag"
_TRPAdminPSFromCriteriaTag_Object = MibTableColumn
tRPAdminPSFromCriteriaTag = _TRPAdminPSFromCriteriaTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 24),
    _TRPAdminPSFromCriteriaTag_Type()
)
tRPAdminPSFromCriteriaTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaTag.setStatus("current")
_TRPAdminPSFromCritNbrInetAddrType_Type = InetAddressType
_TRPAdminPSFromCritNbrInetAddrType_Object = MibTableColumn
tRPAdminPSFromCritNbrInetAddrType = _TRPAdminPSFromCritNbrInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 25),
    _TRPAdminPSFromCritNbrInetAddrType_Type()
)
tRPAdminPSFromCritNbrInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCritNbrInetAddrType.setStatus("current")


class _TRPAdminPSFromCritNbrInetAddr_Type(InetAddress):
    """Custom type tRPAdminPSFromCritNbrInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TRPAdminPSFromCritNbrInetAddr_Type.__name__ = "InetAddress"
_TRPAdminPSFromCritNbrInetAddr_Object = MibTableColumn
tRPAdminPSFromCritNbrInetAddr = _TRPAdminPSFromCritNbrInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 26),
    _TRPAdminPSFromCritNbrInetAddr_Type()
)
tRPAdminPSFromCritNbrInetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCritNbrInetAddr.setStatus("current")
_TRPAdminPSFromCritSrcInetAddrType_Type = InetAddressType
_TRPAdminPSFromCritSrcInetAddrType_Object = MibTableColumn
tRPAdminPSFromCritSrcInetAddrType = _TRPAdminPSFromCritSrcInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 27),
    _TRPAdminPSFromCritSrcInetAddrType_Type()
)
tRPAdminPSFromCritSrcInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCritSrcInetAddrType.setStatus("current")


class _TRPAdminPSFromCritSrcInetAddr_Type(InetAddress):
    """Custom type tRPAdminPSFromCritSrcInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TRPAdminPSFromCritSrcInetAddr_Type.__name__ = "InetAddress"
_TRPAdminPSFromCritSrcInetAddr_Object = MibTableColumn
tRPAdminPSFromCritSrcInetAddr = _TRPAdminPSFromCritSrcInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 28),
    _TRPAdminPSFromCritSrcInetAddr_Type()
)
tRPAdminPSFromCritSrcInetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCritSrcInetAddr.setStatus("current")


class _TRPAdminPSFromCriteriaFamily_Type(TmnxBGPFamilyType):
    """Custom type tRPAdminPSFromCriteriaFamily based on TmnxBGPFamilyType"""
    defaultBinValue = "0"


_TRPAdminPSFromCriteriaFamily_Type.__name__ = "TmnxBGPFamilyType"
_TRPAdminPSFromCriteriaFamily_Object = MibTableColumn
tRPAdminPSFromCriteriaFamily = _TRPAdminPSFromCriteriaFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 29),
    _TRPAdminPSFromCriteriaFamily_Type()
)
tRPAdminPSFromCriteriaFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaFamily.setStatus("current")


class _TRPAdminPSFromCriteriaInstanceId_Type(Unsigned32):
    """Custom type tRPAdminPSFromCriteriaInstanceId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
        ValueRangeConstraint(64, 95),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TRPAdminPSFromCriteriaInstanceId_Type.__name__ = "Unsigned32"
_TRPAdminPSFromCriteriaInstanceId_Object = MibTableColumn
tRPAdminPSFromCriteriaInstanceId = _TRPAdminPSFromCriteriaInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 30),
    _TRPAdminPSFromCriteriaInstanceId_Type()
)
tRPAdminPSFromCriteriaInstanceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaInstanceId.setStatus("current")


class _TRPAdminPSFromCriteriaMatchTag_Type(TmnxEnabledDisabled):
    """Custom type tRPAdminPSFromCriteriaMatchTag based on TmnxEnabledDisabled"""
    defaultValue = 2


_TRPAdminPSFromCriteriaMatchTag_Type.__name__ = "TmnxEnabledDisabled"
_TRPAdminPSFromCriteriaMatchTag_Object = MibTableColumn
tRPAdminPSFromCriteriaMatchTag = _TRPAdminPSFromCriteriaMatchTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 31),
    _TRPAdminPSFromCriteriaMatchTag_Type()
)
tRPAdminPSFromCriteriaMatchTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaMatchTag.setStatus("current")


class _TRPAdminPSFromCriteriaState_Type(TPolicyEntryCriteriaState):
    """Custom type tRPAdminPSFromCriteriaState based on TPolicyEntryCriteriaState"""
    defaultValue = 1


_TRPAdminPSFromCriteriaState_Type.__name__ = "TPolicyEntryCriteriaState"
_TRPAdminPSFromCriteriaState_Object = MibTableColumn
tRPAdminPSFromCriteriaState = _TRPAdminPSFromCriteriaState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 32),
    _TRPAdminPSFromCriteriaState_Type()
)
tRPAdminPSFromCriteriaState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaState.setStatus("current")


class _TRPAdminPSFromCritASPathGroup_Type(TASPathGroupName):
    """Custom type tRPAdminPSFromCritASPathGroup based on TASPathGroupName"""
    defaultValue = OctetString("")


_TRPAdminPSFromCritASPathGroup_Type.__name__ = "TASPathGroupName"
_TRPAdminPSFromCritASPathGroup_Object = MibTableColumn
tRPAdminPSFromCritASPathGroup = _TRPAdminPSFromCritASPathGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 33),
    _TRPAdminPSFromCritASPathGroup_Type()
)
tRPAdminPSFromCritASPathGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCritASPathGroup.setStatus("current")


class _TRPAdminPSFromCriteriaPolicy_Type(PolicyStatementNameOrEmpty):
    """Custom type tRPAdminPSFromCriteriaPolicy based on PolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_TRPAdminPSFromCriteriaPolicy_Type.__name__ = "PolicyStatementNameOrEmpty"
_TRPAdminPSFromCriteriaPolicy_Object = MibTableColumn
tRPAdminPSFromCriteriaPolicy = _TRPAdminPSFromCriteriaPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 34),
    _TRPAdminPSFromCriteriaPolicy_Type()
)
tRPAdminPSFromCriteriaPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaPolicy.setStatus("current")
_TRPAdminPSFromCritCreationOrigin_Type = TmnxCreateOrigin
_TRPAdminPSFromCritCreationOrigin_Object = MibTableColumn
tRPAdminPSFromCritCreationOrigin = _TRPAdminPSFromCritCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 35),
    _TRPAdminPSFromCritCreationOrigin_Type()
)
tRPAdminPSFromCritCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPAdminPSFromCritCreationOrigin.setStatus("current")
_TRPAdminInetPrefixListTable_Object = MibTable
tRPAdminInetPrefixListTable = _TRPAdminInetPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11)
)
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListTable.setStatus("current")
_TRPAdminInetPrefixListEntry_Object = MibTableRow
tRPAdminInetPrefixListEntry = _TRPAdminInetPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11, 1)
)
tRPAdminInetPrefixListEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListPrefixType"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListPrefix"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListPrefixLen"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListType"),
)
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListEntry.setStatus("current")


class _TRPAdminInetPrefixListName_Type(TPrefixListName):
    """Custom type tRPAdminInetPrefixListName based on TPrefixListName"""
    subtypeSpec = TPrefixListName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPAdminInetPrefixListName_Type.__name__ = "TPrefixListName"
_TRPAdminInetPrefixListName_Object = MibTableColumn
tRPAdminInetPrefixListName = _TRPAdminInetPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11, 1, 1),
    _TRPAdminInetPrefixListName_Type()
)
tRPAdminInetPrefixListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListName.setStatus("current")
_TRPAdminInetPrefixListPrefixType_Type = InetAddressType
_TRPAdminInetPrefixListPrefixType_Object = MibTableColumn
tRPAdminInetPrefixListPrefixType = _TRPAdminInetPrefixListPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11, 1, 2),
    _TRPAdminInetPrefixListPrefixType_Type()
)
tRPAdminInetPrefixListPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListPrefixType.setStatus("current")


class _TRPAdminInetPrefixListPrefix_Type(InetAddress):
    """Custom type tRPAdminInetPrefixListPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TRPAdminInetPrefixListPrefix_Type.__name__ = "InetAddress"
_TRPAdminInetPrefixListPrefix_Object = MibTableColumn
tRPAdminInetPrefixListPrefix = _TRPAdminInetPrefixListPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11, 1, 3),
    _TRPAdminInetPrefixListPrefix_Type()
)
tRPAdminInetPrefixListPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListPrefix.setStatus("current")
_TRPAdminInetPrefixListPrefixLen_Type = InetAddressPrefixLength
_TRPAdminInetPrefixListPrefixLen_Object = MibTableColumn
tRPAdminInetPrefixListPrefixLen = _TRPAdminInetPrefixListPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11, 1, 4),
    _TRPAdminInetPrefixListPrefixLen_Type()
)
tRPAdminInetPrefixListPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListPrefixLen.setStatus("current")


class _TRPAdminInetPrefixListType_Type(Integer32):
    """Custom type tRPAdminInetPrefixListType based on Integer32"""
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
        *(("exact", 1),
          ("longer", 2),
          ("through", 3),
          ("range", 4))
    )


_TRPAdminInetPrefixListType_Type.__name__ = "Integer32"
_TRPAdminInetPrefixListType_Object = MibTableColumn
tRPAdminInetPrefixListType = _TRPAdminInetPrefixListType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11, 1, 5),
    _TRPAdminInetPrefixListType_Type()
)
tRPAdminInetPrefixListType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListType.setStatus("current")
_TRPAdminInetPrefixListRowStatus_Type = RowStatus
_TRPAdminInetPrefixListRowStatus_Object = MibTableColumn
tRPAdminInetPrefixListRowStatus = _TRPAdminInetPrefixListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11, 1, 6),
    _TRPAdminInetPrefixListRowStatus_Type()
)
tRPAdminInetPrefixListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListRowStatus.setStatus("current")


class _TRPAdminInetPrefixListThroughLen_Type(InetAddressPrefixLength):
    """Custom type tRPAdminInetPrefixListThroughLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TRPAdminInetPrefixListThroughLen_Type.__name__ = "InetAddressPrefixLength"
_TRPAdminInetPrefixListThroughLen_Object = MibTableColumn
tRPAdminInetPrefixListThroughLen = _TRPAdminInetPrefixListThroughLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11, 1, 7),
    _TRPAdminInetPrefixListThroughLen_Type()
)
tRPAdminInetPrefixListThroughLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListThroughLen.setStatus("current")


class _TRPAdminInetPrefixListBeginLen_Type(InetAddressPrefixLength):
    """Custom type tRPAdminInetPrefixListBeginLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TRPAdminInetPrefixListBeginLen_Type.__name__ = "InetAddressPrefixLength"
_TRPAdminInetPrefixListBeginLen_Object = MibTableColumn
tRPAdminInetPrefixListBeginLen = _TRPAdminInetPrefixListBeginLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11, 1, 8),
    _TRPAdminInetPrefixListBeginLen_Type()
)
tRPAdminInetPrefixListBeginLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListBeginLen.setStatus("current")
_TRPAdminCommunityExprTable_Object = MibTable
tRPAdminCommunityExprTable = _TRPAdminCommunityExprTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 12)
)
if mibBuilder.loadTexts:
    tRPAdminCommunityExprTable.setStatus("current")
_TRPAdminCommunityExprEntry_Object = MibTableRow
tRPAdminCommunityExprEntry = _TRPAdminCommunityExprEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 12, 1)
)
tRPAdminCommunityExprEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityExprName"),
)
if mibBuilder.loadTexts:
    tRPAdminCommunityExprEntry.setStatus("current")


class _TRPAdminCommunityExprName_Type(TCommunityName):
    """Custom type tRPAdminCommunityExprName based on TCommunityName"""
    subtypeSpec = TCommunityName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPAdminCommunityExprName_Type.__name__ = "TCommunityName"
_TRPAdminCommunityExprName_Object = MibTableColumn
tRPAdminCommunityExprName = _TRPAdminCommunityExprName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 12, 1, 1),
    _TRPAdminCommunityExprName_Type()
)
tRPAdminCommunityExprName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminCommunityExprName.setStatus("current")
_TRPAdminCommunityExprRowStatus_Type = RowStatus
_TRPAdminCommunityExprRowStatus_Object = MibTableColumn
tRPAdminCommunityExprRowStatus = _TRPAdminCommunityExprRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 12, 1, 2),
    _TRPAdminCommunityExprRowStatus_Type()
)
tRPAdminCommunityExprRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminCommunityExprRowStatus.setStatus("current")


class _TRPAdminCommunityExprString1_Type(TCommunityMemberExpression):
    """Custom type tRPAdminCommunityExprString1 based on TCommunityMemberExpression"""
    defaultValue = OctetString("")


_TRPAdminCommunityExprString1_Type.__name__ = "TCommunityMemberExpression"
_TRPAdminCommunityExprString1_Object = MibTableColumn
tRPAdminCommunityExprString1 = _TRPAdminCommunityExprString1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 12, 1, 3),
    _TRPAdminCommunityExprString1_Type()
)
tRPAdminCommunityExprString1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminCommunityExprString1.setStatus("current")


class _TRPAdminCommunityExprString2_Type(TCommunityMemberExpression):
    """Custom type tRPAdminCommunityExprString2 based on TCommunityMemberExpression"""
    defaultValue = OctetString("")


_TRPAdminCommunityExprString2_Type.__name__ = "TCommunityMemberExpression"
_TRPAdminCommunityExprString2_Object = MibTableColumn
tRPAdminCommunityExprString2 = _TRPAdminCommunityExprString2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 12, 1, 4),
    _TRPAdminCommunityExprString2_Type()
)
tRPAdminCommunityExprString2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminCommunityExprString2.setStatus("current")


class _TRPAdminCommunityExprString3_Type(TCommunityMemberExpression):
    """Custom type tRPAdminCommunityExprString3 based on TCommunityMemberExpression"""
    defaultValue = OctetString("")


_TRPAdminCommunityExprString3_Type.__name__ = "TCommunityMemberExpression"
_TRPAdminCommunityExprString3_Object = MibTableColumn
tRPAdminCommunityExprString3 = _TRPAdminCommunityExprString3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 12, 1, 5),
    _TRPAdminCommunityExprString3_Type()
)
tRPAdminCommunityExprString3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminCommunityExprString3.setStatus("current")


class _TRPAdminCommunityExprString4_Type(TCommunityMemberExpression):
    """Custom type tRPAdminCommunityExprString4 based on TCommunityMemberExpression"""
    defaultValue = OctetString("")


_TRPAdminCommunityExprString4_Type.__name__ = "TCommunityMemberExpression"
_TRPAdminCommunityExprString4_Object = MibTableColumn
tRPAdminCommunityExprString4 = _TRPAdminCommunityExprString4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 12, 1, 6),
    _TRPAdminCommunityExprString4_Type()
)
tRPAdminCommunityExprString4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminCommunityExprString4.setStatus("current")


class _TRPAdminCommunityExprExactMatch_Type(TruthValue):
    """Custom type tRPAdminCommunityExprExactMatch based on TruthValue"""
    defaultValue = 2


_TRPAdminCommunityExprExactMatch_Type.__name__ = "TruthValue"
_TRPAdminCommunityExprExactMatch_Object = MibTableColumn
tRPAdminCommunityExprExactMatch = _TRPAdminCommunityExprExactMatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 12, 1, 7),
    _TRPAdminCommunityExprExactMatch_Type()
)
tRPAdminCommunityExprExactMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminCommunityExprExactMatch.setStatus("current")
_TRPAdminASPathGroupTable_Object = MibTable
tRPAdminASPathGroupTable = _TRPAdminASPathGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 13)
)
if mibBuilder.loadTexts:
    tRPAdminASPathGroupTable.setStatus("current")
_TRPAdminASPathGroupEntry_Object = MibTableRow
tRPAdminASPathGroupEntry = _TRPAdminASPathGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 13, 1)
)
tRPAdminASPathGroupEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathGroupName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathGroupEntryIndex"),
)
if mibBuilder.loadTexts:
    tRPAdminASPathGroupEntry.setStatus("current")


class _TRPAdminASPathGroupName_Type(TASPathGroupName):
    """Custom type tRPAdminASPathGroupName based on TASPathGroupName"""
    subtypeSpec = TASPathGroupName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPAdminASPathGroupName_Type.__name__ = "TASPathGroupName"
_TRPAdminASPathGroupName_Object = MibTableColumn
tRPAdminASPathGroupName = _TRPAdminASPathGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 13, 1, 1),
    _TRPAdminASPathGroupName_Type()
)
tRPAdminASPathGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminASPathGroupName.setStatus("current")


class _TRPAdminASPathGroupEntryIndex_Type(Unsigned32):
    """Custom type tRPAdminASPathGroupEntryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TRPAdminASPathGroupEntryIndex_Type.__name__ = "Unsigned32"
_TRPAdminASPathGroupEntryIndex_Object = MibTableColumn
tRPAdminASPathGroupEntryIndex = _TRPAdminASPathGroupEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 13, 1, 2),
    _TRPAdminASPathGroupEntryIndex_Type()
)
tRPAdminASPathGroupEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminASPathGroupEntryIndex.setStatus("current")
_TRPAdminASPathGroupRowStatus_Type = RowStatus
_TRPAdminASPathGroupRowStatus_Object = MibTableColumn
tRPAdminASPathGroupRowStatus = _TRPAdminASPathGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 13, 1, 3),
    _TRPAdminASPathGroupRowStatus_Type()
)
tRPAdminASPathGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminASPathGroupRowStatus.setStatus("current")


class _TRPAdminASPathGroupASPathName_Type(TASPathName):
    """Custom type tRPAdminASPathGroupASPathName based on TASPathName"""
    subtypeSpec = TASPathName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPAdminASPathGroupASPathName_Type.__name__ = "TASPathName"
_TRPAdminASPathGroupASPathName_Object = MibTableColumn
tRPAdminASPathGroupASPathName = _TRPAdminASPathGroupASPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 13, 1, 4),
    _TRPAdminASPathGroupASPathName_Type()
)
tRPAdminASPathGroupASPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminASPathGroupASPathName.setStatus("current")
_TRPAdminASPathGroupASPathRegEx_Type = TRoutePolicyRegex
_TRPAdminASPathGroupASPathRegEx_Object = MibTableColumn
tRPAdminASPathGroupASPathRegEx = _TRPAdminASPathGroupASPathRegEx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 13, 1, 5),
    _TRPAdminASPathGroupASPathRegEx_Type()
)
tRPAdminASPathGroupASPathRegEx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminASPathGroupASPathRegEx.setStatus("current")
_TRPAdminPSFromCommExprTable_Object = MibTable
tRPAdminPSFromCommExprTable = _TRPAdminPSFromCommExprTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 14)
)
if mibBuilder.loadTexts:
    tRPAdminPSFromCommExprTable.setStatus("current")
_TRPAdminPSFromCommExprEntry_Object = MibTableRow
tRPAdminPSFromCommExprEntry = _TRPAdminPSFromCommExprEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 14, 1)
)
tRPAdminPSFromCommExprEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIndex"),
)
if mibBuilder.loadTexts:
    tRPAdminPSFromCommExprEntry.setStatus("current")
_TRPAdminPSFromCommExprRowStatus_Type = RowStatus
_TRPAdminPSFromCommExprRowStatus_Object = MibTableColumn
tRPAdminPSFromCommExprRowStatus = _TRPAdminPSFromCommExprRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 14, 1, 1),
    _TRPAdminPSFromCommExprRowStatus_Type()
)
tRPAdminPSFromCommExprRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCommExprRowStatus.setStatus("current")


class _TRPAdminPSFromCommExprString1_Type(TCommunityNameExpression):
    """Custom type tRPAdminPSFromCommExprString1 based on TCommunityNameExpression"""
    defaultValue = OctetString("")


_TRPAdminPSFromCommExprString1_Type.__name__ = "TCommunityNameExpression"
_TRPAdminPSFromCommExprString1_Object = MibTableColumn
tRPAdminPSFromCommExprString1 = _TRPAdminPSFromCommExprString1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 14, 1, 2),
    _TRPAdminPSFromCommExprString1_Type()
)
tRPAdminPSFromCommExprString1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCommExprString1.setStatus("current")


class _TRPAdminPSFromCommExprString2_Type(TCommunityNameExpression):
    """Custom type tRPAdminPSFromCommExprString2 based on TCommunityNameExpression"""
    defaultValue = OctetString("")


_TRPAdminPSFromCommExprString2_Type.__name__ = "TCommunityNameExpression"
_TRPAdminPSFromCommExprString2_Object = MibTableColumn
tRPAdminPSFromCommExprString2 = _TRPAdminPSFromCommExprString2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 14, 1, 3),
    _TRPAdminPSFromCommExprString2_Type()
)
tRPAdminPSFromCommExprString2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCommExprString2.setStatus("current")


class _TRPAdminPSFromCommExprString3_Type(TCommunityNameExpression):
    """Custom type tRPAdminPSFromCommExprString3 based on TCommunityNameExpression"""
    defaultValue = OctetString("")


_TRPAdminPSFromCommExprString3_Type.__name__ = "TCommunityNameExpression"
_TRPAdminPSFromCommExprString3_Object = MibTableColumn
tRPAdminPSFromCommExprString3 = _TRPAdminPSFromCommExprString3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 14, 1, 4),
    _TRPAdminPSFromCommExprString3_Type()
)
tRPAdminPSFromCommExprString3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCommExprString3.setStatus("current")


class _TRPAdminPSFromCommExprString4_Type(TCommunityNameExpression):
    """Custom type tRPAdminPSFromCommExprString4 based on TCommunityNameExpression"""
    defaultValue = OctetString("")


_TRPAdminPSFromCommExprString4_Type.__name__ = "TCommunityNameExpression"
_TRPAdminPSFromCommExprString4_Object = MibTableColumn
tRPAdminPSFromCommExprString4 = _TRPAdminPSFromCommExprString4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 14, 1, 5),
    _TRPAdminPSFromCommExprString4_Type()
)
tRPAdminPSFromCommExprString4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCommExprString4.setStatus("current")
_TRPAdminPSDefActionAddCommTable_Object = MibTable
tRPAdminPSDefActionAddCommTable = _TRPAdminPSDefActionAddCommTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15)
)
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddCommTable.setStatus("current")
_TRPAdminPSDefActionAddCommEntry_Object = MibTableRow
tRPAdminPSDefActionAddCommEntry = _TRPAdminPSDefActionAddCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1)
)
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddCommEntry.setStatus("current")


class _TRPAdminPSDefActionAddComm1_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm1 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm1_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm1_Object = MibTableColumn
tRPAdminPSDefActionAddComm1 = _TRPAdminPSDefActionAddComm1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 1),
    _TRPAdminPSDefActionAddComm1_Type()
)
tRPAdminPSDefActionAddComm1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm1.setStatus("current")


class _TRPAdminPSDefActionAddComm2_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm2 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm2_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm2_Object = MibTableColumn
tRPAdminPSDefActionAddComm2 = _TRPAdminPSDefActionAddComm2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 2),
    _TRPAdminPSDefActionAddComm2_Type()
)
tRPAdminPSDefActionAddComm2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm2.setStatus("current")


class _TRPAdminPSDefActionAddComm3_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm3 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm3_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm3_Object = MibTableColumn
tRPAdminPSDefActionAddComm3 = _TRPAdminPSDefActionAddComm3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 3),
    _TRPAdminPSDefActionAddComm3_Type()
)
tRPAdminPSDefActionAddComm3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm3.setStatus("current")


class _TRPAdminPSDefActionAddComm4_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm4 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm4_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm4_Object = MibTableColumn
tRPAdminPSDefActionAddComm4 = _TRPAdminPSDefActionAddComm4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 4),
    _TRPAdminPSDefActionAddComm4_Type()
)
tRPAdminPSDefActionAddComm4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm4.setStatus("current")


class _TRPAdminPSDefActionAddComm5_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm5 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm5_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm5_Object = MibTableColumn
tRPAdminPSDefActionAddComm5 = _TRPAdminPSDefActionAddComm5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 5),
    _TRPAdminPSDefActionAddComm5_Type()
)
tRPAdminPSDefActionAddComm5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm5.setStatus("current")


class _TRPAdminPSDefActionAddComm6_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm6 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm6_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm6_Object = MibTableColumn
tRPAdminPSDefActionAddComm6 = _TRPAdminPSDefActionAddComm6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 6),
    _TRPAdminPSDefActionAddComm6_Type()
)
tRPAdminPSDefActionAddComm6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm6.setStatus("current")


class _TRPAdminPSDefActionAddComm7_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm7 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm7_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm7_Object = MibTableColumn
tRPAdminPSDefActionAddComm7 = _TRPAdminPSDefActionAddComm7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 7),
    _TRPAdminPSDefActionAddComm7_Type()
)
tRPAdminPSDefActionAddComm7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm7.setStatus("current")


class _TRPAdminPSDefActionAddComm8_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm8 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm8_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm8_Object = MibTableColumn
tRPAdminPSDefActionAddComm8 = _TRPAdminPSDefActionAddComm8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 8),
    _TRPAdminPSDefActionAddComm8_Type()
)
tRPAdminPSDefActionAddComm8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm8.setStatus("current")


class _TRPAdminPSDefActionAddComm9_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm9 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm9_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm9_Object = MibTableColumn
tRPAdminPSDefActionAddComm9 = _TRPAdminPSDefActionAddComm9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 9),
    _TRPAdminPSDefActionAddComm9_Type()
)
tRPAdminPSDefActionAddComm9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm9.setStatus("current")


class _TRPAdminPSDefActionAddComm10_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm10 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm10_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm10_Object = MibTableColumn
tRPAdminPSDefActionAddComm10 = _TRPAdminPSDefActionAddComm10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 10),
    _TRPAdminPSDefActionAddComm10_Type()
)
tRPAdminPSDefActionAddComm10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm10.setStatus("current")


class _TRPAdminPSDefActionAddComm11_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm11 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm11_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm11_Object = MibTableColumn
tRPAdminPSDefActionAddComm11 = _TRPAdminPSDefActionAddComm11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 11),
    _TRPAdminPSDefActionAddComm11_Type()
)
tRPAdminPSDefActionAddComm11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm11.setStatus("current")


class _TRPAdminPSDefActionAddComm12_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm12 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm12_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm12_Object = MibTableColumn
tRPAdminPSDefActionAddComm12 = _TRPAdminPSDefActionAddComm12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 12),
    _TRPAdminPSDefActionAddComm12_Type()
)
tRPAdminPSDefActionAddComm12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm12.setStatus("current")


class _TRPAdminPSDefActionAddComm13_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm13 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm13_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm13_Object = MibTableColumn
tRPAdminPSDefActionAddComm13 = _TRPAdminPSDefActionAddComm13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 13),
    _TRPAdminPSDefActionAddComm13_Type()
)
tRPAdminPSDefActionAddComm13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm13.setStatus("current")


class _TRPAdminPSDefActionAddComm14_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm14 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm14_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm14_Object = MibTableColumn
tRPAdminPSDefActionAddComm14 = _TRPAdminPSDefActionAddComm14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 14),
    _TRPAdminPSDefActionAddComm14_Type()
)
tRPAdminPSDefActionAddComm14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm14.setStatus("current")


class _TRPAdminPSDefActionAddComm15_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm15 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm15_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm15_Object = MibTableColumn
tRPAdminPSDefActionAddComm15 = _TRPAdminPSDefActionAddComm15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 15),
    _TRPAdminPSDefActionAddComm15_Type()
)
tRPAdminPSDefActionAddComm15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm15.setStatus("current")


class _TRPAdminPSDefActionAddComm16_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm16 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm16_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm16_Object = MibTableColumn
tRPAdminPSDefActionAddComm16 = _TRPAdminPSDefActionAddComm16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 16),
    _TRPAdminPSDefActionAddComm16_Type()
)
tRPAdminPSDefActionAddComm16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm16.setStatus("current")


class _TRPAdminPSDefActionAddComm17_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm17 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm17_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm17_Object = MibTableColumn
tRPAdminPSDefActionAddComm17 = _TRPAdminPSDefActionAddComm17_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 17),
    _TRPAdminPSDefActionAddComm17_Type()
)
tRPAdminPSDefActionAddComm17.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm17.setStatus("current")


class _TRPAdminPSDefActionAddComm18_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm18 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm18_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm18_Object = MibTableColumn
tRPAdminPSDefActionAddComm18 = _TRPAdminPSDefActionAddComm18_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 18),
    _TRPAdminPSDefActionAddComm18_Type()
)
tRPAdminPSDefActionAddComm18.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm18.setStatus("current")


class _TRPAdminPSDefActionAddComm19_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm19 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm19_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm19_Object = MibTableColumn
tRPAdminPSDefActionAddComm19 = _TRPAdminPSDefActionAddComm19_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 19),
    _TRPAdminPSDefActionAddComm19_Type()
)
tRPAdminPSDefActionAddComm19.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm19.setStatus("current")


class _TRPAdminPSDefActionAddComm20_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm20 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm20_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm20_Object = MibTableColumn
tRPAdminPSDefActionAddComm20 = _TRPAdminPSDefActionAddComm20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 20),
    _TRPAdminPSDefActionAddComm20_Type()
)
tRPAdminPSDefActionAddComm20.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm20.setStatus("current")


class _TRPAdminPSDefActionAddComm21_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm21 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm21_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm21_Object = MibTableColumn
tRPAdminPSDefActionAddComm21 = _TRPAdminPSDefActionAddComm21_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 21),
    _TRPAdminPSDefActionAddComm21_Type()
)
tRPAdminPSDefActionAddComm21.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm21.setStatus("current")


class _TRPAdminPSDefActionAddComm22_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm22 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm22_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm22_Object = MibTableColumn
tRPAdminPSDefActionAddComm22 = _TRPAdminPSDefActionAddComm22_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 22),
    _TRPAdminPSDefActionAddComm22_Type()
)
tRPAdminPSDefActionAddComm22.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm22.setStatus("current")


class _TRPAdminPSDefActionAddComm23_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm23 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm23_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm23_Object = MibTableColumn
tRPAdminPSDefActionAddComm23 = _TRPAdminPSDefActionAddComm23_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 23),
    _TRPAdminPSDefActionAddComm23_Type()
)
tRPAdminPSDefActionAddComm23.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm23.setStatus("current")


class _TRPAdminPSDefActionAddComm24_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm24 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm24_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm24_Object = MibTableColumn
tRPAdminPSDefActionAddComm24 = _TRPAdminPSDefActionAddComm24_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 24),
    _TRPAdminPSDefActionAddComm24_Type()
)
tRPAdminPSDefActionAddComm24.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm24.setStatus("current")


class _TRPAdminPSDefActionAddComm25_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm25 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm25_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm25_Object = MibTableColumn
tRPAdminPSDefActionAddComm25 = _TRPAdminPSDefActionAddComm25_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 25),
    _TRPAdminPSDefActionAddComm25_Type()
)
tRPAdminPSDefActionAddComm25.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm25.setStatus("current")


class _TRPAdminPSDefActionAddComm26_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm26 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm26_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm26_Object = MibTableColumn
tRPAdminPSDefActionAddComm26 = _TRPAdminPSDefActionAddComm26_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 26),
    _TRPAdminPSDefActionAddComm26_Type()
)
tRPAdminPSDefActionAddComm26.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm26.setStatus("current")


class _TRPAdminPSDefActionAddComm27_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm27 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm27_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm27_Object = MibTableColumn
tRPAdminPSDefActionAddComm27 = _TRPAdminPSDefActionAddComm27_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 27),
    _TRPAdminPSDefActionAddComm27_Type()
)
tRPAdminPSDefActionAddComm27.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm27.setStatus("current")


class _TRPAdminPSDefActionAddComm28_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionAddComm28 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionAddComm28_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionAddComm28_Object = MibTableColumn
tRPAdminPSDefActionAddComm28 = _TRPAdminPSDefActionAddComm28_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 15, 1, 28),
    _TRPAdminPSDefActionAddComm28_Type()
)
tRPAdminPSDefActionAddComm28.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAddComm28.setStatus("current")
_TRPAdminPSDefActionRemCommTable_Object = MibTable
tRPAdminPSDefActionRemCommTable = _TRPAdminPSDefActionRemCommTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16)
)
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemCommTable.setStatus("current")
_TRPAdminPSDefActionRemCommEntry_Object = MibTableRow
tRPAdminPSDefActionRemCommEntry = _TRPAdminPSDefActionRemCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1)
)
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemCommEntry.setStatus("current")


class _TRPAdminPSDefActionRemoveComm1_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm1 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm1_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm1_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm1 = _TRPAdminPSDefActionRemoveComm1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 1),
    _TRPAdminPSDefActionRemoveComm1_Type()
)
tRPAdminPSDefActionRemoveComm1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm1.setStatus("current")


class _TRPAdminPSDefActionRemoveComm2_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm2 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm2_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm2_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm2 = _TRPAdminPSDefActionRemoveComm2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 2),
    _TRPAdminPSDefActionRemoveComm2_Type()
)
tRPAdminPSDefActionRemoveComm2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm2.setStatus("current")


class _TRPAdminPSDefActionRemoveComm3_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm3 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm3_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm3_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm3 = _TRPAdminPSDefActionRemoveComm3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 3),
    _TRPAdminPSDefActionRemoveComm3_Type()
)
tRPAdminPSDefActionRemoveComm3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm3.setStatus("current")


class _TRPAdminPSDefActionRemoveComm4_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm4 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm4_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm4_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm4 = _TRPAdminPSDefActionRemoveComm4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 4),
    _TRPAdminPSDefActionRemoveComm4_Type()
)
tRPAdminPSDefActionRemoveComm4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm4.setStatus("current")


class _TRPAdminPSDefActionRemoveComm5_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm5 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm5_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm5_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm5 = _TRPAdminPSDefActionRemoveComm5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 5),
    _TRPAdminPSDefActionRemoveComm5_Type()
)
tRPAdminPSDefActionRemoveComm5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm5.setStatus("current")


class _TRPAdminPSDefActionRemoveComm6_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm6 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm6_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm6_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm6 = _TRPAdminPSDefActionRemoveComm6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 6),
    _TRPAdminPSDefActionRemoveComm6_Type()
)
tRPAdminPSDefActionRemoveComm6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm6.setStatus("current")


class _TRPAdminPSDefActionRemoveComm7_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm7 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm7_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm7_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm7 = _TRPAdminPSDefActionRemoveComm7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 7),
    _TRPAdminPSDefActionRemoveComm7_Type()
)
tRPAdminPSDefActionRemoveComm7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm7.setStatus("current")


class _TRPAdminPSDefActionRemoveComm8_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm8 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm8_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm8_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm8 = _TRPAdminPSDefActionRemoveComm8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 8),
    _TRPAdminPSDefActionRemoveComm8_Type()
)
tRPAdminPSDefActionRemoveComm8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm8.setStatus("current")


class _TRPAdminPSDefActionRemoveComm9_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm9 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm9_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm9_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm9 = _TRPAdminPSDefActionRemoveComm9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 9),
    _TRPAdminPSDefActionRemoveComm9_Type()
)
tRPAdminPSDefActionRemoveComm9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm9.setStatus("current")


class _TRPAdminPSDefActionRemoveComm10_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm10 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm10_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm10_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm10 = _TRPAdminPSDefActionRemoveComm10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 10),
    _TRPAdminPSDefActionRemoveComm10_Type()
)
tRPAdminPSDefActionRemoveComm10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm10.setStatus("current")


class _TRPAdminPSDefActionRemoveComm11_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm11 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm11_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm11_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm11 = _TRPAdminPSDefActionRemoveComm11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 11),
    _TRPAdminPSDefActionRemoveComm11_Type()
)
tRPAdminPSDefActionRemoveComm11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm11.setStatus("current")


class _TRPAdminPSDefActionRemoveComm12_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm12 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm12_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm12_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm12 = _TRPAdminPSDefActionRemoveComm12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 12),
    _TRPAdminPSDefActionRemoveComm12_Type()
)
tRPAdminPSDefActionRemoveComm12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm12.setStatus("current")


class _TRPAdminPSDefActionRemoveComm13_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm13 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm13_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm13_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm13 = _TRPAdminPSDefActionRemoveComm13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 13),
    _TRPAdminPSDefActionRemoveComm13_Type()
)
tRPAdminPSDefActionRemoveComm13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm13.setStatus("current")


class _TRPAdminPSDefActionRemoveComm14_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm14 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm14_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm14_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm14 = _TRPAdminPSDefActionRemoveComm14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 14),
    _TRPAdminPSDefActionRemoveComm14_Type()
)
tRPAdminPSDefActionRemoveComm14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm14.setStatus("current")


class _TRPAdminPSDefActionRemoveComm15_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm15 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm15_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm15_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm15 = _TRPAdminPSDefActionRemoveComm15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 15),
    _TRPAdminPSDefActionRemoveComm15_Type()
)
tRPAdminPSDefActionRemoveComm15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm15.setStatus("current")


class _TRPAdminPSDefActionRemoveComm16_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm16 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm16_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm16_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm16 = _TRPAdminPSDefActionRemoveComm16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 16),
    _TRPAdminPSDefActionRemoveComm16_Type()
)
tRPAdminPSDefActionRemoveComm16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm16.setStatus("current")


class _TRPAdminPSDefActionRemoveComm17_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm17 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm17_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm17_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm17 = _TRPAdminPSDefActionRemoveComm17_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 17),
    _TRPAdminPSDefActionRemoveComm17_Type()
)
tRPAdminPSDefActionRemoveComm17.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm17.setStatus("current")


class _TRPAdminPSDefActionRemoveComm18_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm18 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm18_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm18_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm18 = _TRPAdminPSDefActionRemoveComm18_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 18),
    _TRPAdminPSDefActionRemoveComm18_Type()
)
tRPAdminPSDefActionRemoveComm18.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm18.setStatus("current")


class _TRPAdminPSDefActionRemoveComm19_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm19 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm19_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm19_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm19 = _TRPAdminPSDefActionRemoveComm19_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 19),
    _TRPAdminPSDefActionRemoveComm19_Type()
)
tRPAdminPSDefActionRemoveComm19.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm19.setStatus("current")


class _TRPAdminPSDefActionRemoveComm20_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm20 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm20_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm20_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm20 = _TRPAdminPSDefActionRemoveComm20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 20),
    _TRPAdminPSDefActionRemoveComm20_Type()
)
tRPAdminPSDefActionRemoveComm20.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm20.setStatus("current")


class _TRPAdminPSDefActionRemoveComm21_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm21 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm21_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm21_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm21 = _TRPAdminPSDefActionRemoveComm21_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 21),
    _TRPAdminPSDefActionRemoveComm21_Type()
)
tRPAdminPSDefActionRemoveComm21.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm21.setStatus("current")


class _TRPAdminPSDefActionRemoveComm22_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm22 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm22_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm22_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm22 = _TRPAdminPSDefActionRemoveComm22_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 22),
    _TRPAdminPSDefActionRemoveComm22_Type()
)
tRPAdminPSDefActionRemoveComm22.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm22.setStatus("current")


class _TRPAdminPSDefActionRemoveComm23_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm23 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm23_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm23_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm23 = _TRPAdminPSDefActionRemoveComm23_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 23),
    _TRPAdminPSDefActionRemoveComm23_Type()
)
tRPAdminPSDefActionRemoveComm23.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm23.setStatus("current")


class _TRPAdminPSDefActionRemoveComm24_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm24 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm24_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm24_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm24 = _TRPAdminPSDefActionRemoveComm24_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 24),
    _TRPAdminPSDefActionRemoveComm24_Type()
)
tRPAdminPSDefActionRemoveComm24.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm24.setStatus("current")


class _TRPAdminPSDefActionRemoveComm25_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm25 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm25_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm25_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm25 = _TRPAdminPSDefActionRemoveComm25_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 25),
    _TRPAdminPSDefActionRemoveComm25_Type()
)
tRPAdminPSDefActionRemoveComm25.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm25.setStatus("current")


class _TRPAdminPSDefActionRemoveComm26_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm26 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm26_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm26_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm26 = _TRPAdminPSDefActionRemoveComm26_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 26),
    _TRPAdminPSDefActionRemoveComm26_Type()
)
tRPAdminPSDefActionRemoveComm26.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm26.setStatus("current")


class _TRPAdminPSDefActionRemoveComm27_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm27 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm27_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm27_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm27 = _TRPAdminPSDefActionRemoveComm27_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 27),
    _TRPAdminPSDefActionRemoveComm27_Type()
)
tRPAdminPSDefActionRemoveComm27.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm27.setStatus("current")


class _TRPAdminPSDefActionRemoveComm28_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionRemoveComm28 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionRemoveComm28_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionRemoveComm28_Object = MibTableColumn
tRPAdminPSDefActionRemoveComm28 = _TRPAdminPSDefActionRemoveComm28_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 16, 1, 28),
    _TRPAdminPSDefActionRemoveComm28_Type()
)
tRPAdminPSDefActionRemoveComm28.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRemoveComm28.setStatus("current")
_TRPAdminPSDefActionRepCommTable_Object = MibTable
tRPAdminPSDefActionRepCommTable = _TRPAdminPSDefActionRepCommTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17)
)
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRepCommTable.setStatus("current")
_TRPAdminPSDefActionRepCommEntry_Object = MibTableRow
tRPAdminPSDefActionRepCommEntry = _TRPAdminPSDefActionRepCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1)
)
if mibBuilder.loadTexts:
    tRPAdminPSDefActionRepCommEntry.setStatus("current")


class _TRPAdminPSDefActionReplaceComm1_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm1 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm1_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm1_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm1 = _TRPAdminPSDefActionReplaceComm1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 1),
    _TRPAdminPSDefActionReplaceComm1_Type()
)
tRPAdminPSDefActionReplaceComm1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm1.setStatus("current")


class _TRPAdminPSDefActionReplaceComm2_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm2 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm2_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm2_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm2 = _TRPAdminPSDefActionReplaceComm2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 2),
    _TRPAdminPSDefActionReplaceComm2_Type()
)
tRPAdminPSDefActionReplaceComm2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm2.setStatus("current")


class _TRPAdminPSDefActionReplaceComm3_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm3 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm3_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm3_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm3 = _TRPAdminPSDefActionReplaceComm3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 3),
    _TRPAdminPSDefActionReplaceComm3_Type()
)
tRPAdminPSDefActionReplaceComm3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm3.setStatus("current")


class _TRPAdminPSDefActionReplaceComm4_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm4 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm4_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm4_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm4 = _TRPAdminPSDefActionReplaceComm4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 4),
    _TRPAdminPSDefActionReplaceComm4_Type()
)
tRPAdminPSDefActionReplaceComm4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm4.setStatus("current")


class _TRPAdminPSDefActionReplaceComm5_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm5 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm5_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm5_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm5 = _TRPAdminPSDefActionReplaceComm5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 5),
    _TRPAdminPSDefActionReplaceComm5_Type()
)
tRPAdminPSDefActionReplaceComm5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm5.setStatus("current")


class _TRPAdminPSDefActionReplaceComm6_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm6 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm6_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm6_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm6 = _TRPAdminPSDefActionReplaceComm6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 6),
    _TRPAdminPSDefActionReplaceComm6_Type()
)
tRPAdminPSDefActionReplaceComm6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm6.setStatus("current")


class _TRPAdminPSDefActionReplaceComm7_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm7 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm7_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm7_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm7 = _TRPAdminPSDefActionReplaceComm7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 7),
    _TRPAdminPSDefActionReplaceComm7_Type()
)
tRPAdminPSDefActionReplaceComm7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm7.setStatus("current")


class _TRPAdminPSDefActionReplaceComm8_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm8 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm8_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm8_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm8 = _TRPAdminPSDefActionReplaceComm8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 8),
    _TRPAdminPSDefActionReplaceComm8_Type()
)
tRPAdminPSDefActionReplaceComm8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm8.setStatus("current")


class _TRPAdminPSDefActionReplaceComm9_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm9 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm9_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm9_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm9 = _TRPAdminPSDefActionReplaceComm9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 9),
    _TRPAdminPSDefActionReplaceComm9_Type()
)
tRPAdminPSDefActionReplaceComm9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm9.setStatus("current")


class _TRPAdminPSDefActionReplaceComm10_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm10 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm10_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm10_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm10 = _TRPAdminPSDefActionReplaceComm10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 10),
    _TRPAdminPSDefActionReplaceComm10_Type()
)
tRPAdminPSDefActionReplaceComm10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm10.setStatus("current")


class _TRPAdminPSDefActionReplaceComm11_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm11 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm11_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm11_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm11 = _TRPAdminPSDefActionReplaceComm11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 11),
    _TRPAdminPSDefActionReplaceComm11_Type()
)
tRPAdminPSDefActionReplaceComm11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm11.setStatus("current")


class _TRPAdminPSDefActionReplaceComm12_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm12 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm12_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm12_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm12 = _TRPAdminPSDefActionReplaceComm12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 12),
    _TRPAdminPSDefActionReplaceComm12_Type()
)
tRPAdminPSDefActionReplaceComm12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm12.setStatus("current")


class _TRPAdminPSDefActionReplaceComm13_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm13 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm13_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm13_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm13 = _TRPAdminPSDefActionReplaceComm13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 13),
    _TRPAdminPSDefActionReplaceComm13_Type()
)
tRPAdminPSDefActionReplaceComm13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm13.setStatus("current")


class _TRPAdminPSDefActionReplaceComm14_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm14 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm14_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm14_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm14 = _TRPAdminPSDefActionReplaceComm14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 14),
    _TRPAdminPSDefActionReplaceComm14_Type()
)
tRPAdminPSDefActionReplaceComm14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm14.setStatus("current")


class _TRPAdminPSDefActionReplaceComm15_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm15 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm15_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm15_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm15 = _TRPAdminPSDefActionReplaceComm15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 15),
    _TRPAdminPSDefActionReplaceComm15_Type()
)
tRPAdminPSDefActionReplaceComm15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm15.setStatus("current")


class _TRPAdminPSDefActionReplaceComm16_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm16 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm16_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm16_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm16 = _TRPAdminPSDefActionReplaceComm16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 16),
    _TRPAdminPSDefActionReplaceComm16_Type()
)
tRPAdminPSDefActionReplaceComm16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm16.setStatus("current")


class _TRPAdminPSDefActionReplaceComm17_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm17 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm17_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm17_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm17 = _TRPAdminPSDefActionReplaceComm17_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 17),
    _TRPAdminPSDefActionReplaceComm17_Type()
)
tRPAdminPSDefActionReplaceComm17.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm17.setStatus("current")


class _TRPAdminPSDefActionReplaceComm18_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm18 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm18_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm18_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm18 = _TRPAdminPSDefActionReplaceComm18_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 18),
    _TRPAdminPSDefActionReplaceComm18_Type()
)
tRPAdminPSDefActionReplaceComm18.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm18.setStatus("current")


class _TRPAdminPSDefActionReplaceComm19_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm19 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm19_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm19_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm19 = _TRPAdminPSDefActionReplaceComm19_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 19),
    _TRPAdminPSDefActionReplaceComm19_Type()
)
tRPAdminPSDefActionReplaceComm19.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm19.setStatus("current")


class _TRPAdminPSDefActionReplaceComm20_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm20 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm20_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm20_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm20 = _TRPAdminPSDefActionReplaceComm20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 20),
    _TRPAdminPSDefActionReplaceComm20_Type()
)
tRPAdminPSDefActionReplaceComm20.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm20.setStatus("current")


class _TRPAdminPSDefActionReplaceComm21_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm21 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm21_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm21_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm21 = _TRPAdminPSDefActionReplaceComm21_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 21),
    _TRPAdminPSDefActionReplaceComm21_Type()
)
tRPAdminPSDefActionReplaceComm21.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm21.setStatus("current")


class _TRPAdminPSDefActionReplaceComm22_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm22 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm22_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm22_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm22 = _TRPAdminPSDefActionReplaceComm22_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 22),
    _TRPAdminPSDefActionReplaceComm22_Type()
)
tRPAdminPSDefActionReplaceComm22.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm22.setStatus("current")


class _TRPAdminPSDefActionReplaceComm23_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm23 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm23_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm23_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm23 = _TRPAdminPSDefActionReplaceComm23_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 23),
    _TRPAdminPSDefActionReplaceComm23_Type()
)
tRPAdminPSDefActionReplaceComm23.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm23.setStatus("current")


class _TRPAdminPSDefActionReplaceComm24_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm24 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm24_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm24_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm24 = _TRPAdminPSDefActionReplaceComm24_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 24),
    _TRPAdminPSDefActionReplaceComm24_Type()
)
tRPAdminPSDefActionReplaceComm24.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm24.setStatus("current")


class _TRPAdminPSDefActionReplaceComm25_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm25 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm25_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm25_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm25 = _TRPAdminPSDefActionReplaceComm25_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 25),
    _TRPAdminPSDefActionReplaceComm25_Type()
)
tRPAdminPSDefActionReplaceComm25.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm25.setStatus("current")


class _TRPAdminPSDefActionReplaceComm26_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm26 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm26_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm26_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm26 = _TRPAdminPSDefActionReplaceComm26_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 26),
    _TRPAdminPSDefActionReplaceComm26_Type()
)
tRPAdminPSDefActionReplaceComm26.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm26.setStatus("current")


class _TRPAdminPSDefActionReplaceComm27_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm27 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm27_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm27_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm27 = _TRPAdminPSDefActionReplaceComm27_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 27),
    _TRPAdminPSDefActionReplaceComm27_Type()
)
tRPAdminPSDefActionReplaceComm27.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm27.setStatus("current")


class _TRPAdminPSDefActionReplaceComm28_Type(TCommunityName):
    """Custom type tRPAdminPSDefActionReplaceComm28 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSDefActionReplaceComm28_Type.__name__ = "TCommunityName"
_TRPAdminPSDefActionReplaceComm28_Object = MibTableColumn
tRPAdminPSDefActionReplaceComm28 = _TRPAdminPSDefActionReplaceComm28_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 17, 1, 28),
    _TRPAdminPSDefActionReplaceComm28_Type()
)
tRPAdminPSDefActionReplaceComm28.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionReplaceComm28.setStatus("current")
_TRPAdminPSAccActionAddCommTable_Object = MibTable
tRPAdminPSAccActionAddCommTable = _TRPAdminPSAccActionAddCommTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18)
)
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddCommTable.setStatus("current")
_TRPAdminPSAccActionAddCommEntry_Object = MibTableRow
tRPAdminPSAccActionAddCommEntry = _TRPAdminPSAccActionAddCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1)
)
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddCommEntry.setStatus("current")


class _TRPAdminPSAccActionAddComm1_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm1 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm1_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm1_Object = MibTableColumn
tRPAdminPSAccActionAddComm1 = _TRPAdminPSAccActionAddComm1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 1),
    _TRPAdminPSAccActionAddComm1_Type()
)
tRPAdminPSAccActionAddComm1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm1.setStatus("current")


class _TRPAdminPSAccActionAddComm2_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm2 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm2_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm2_Object = MibTableColumn
tRPAdminPSAccActionAddComm2 = _TRPAdminPSAccActionAddComm2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 2),
    _TRPAdminPSAccActionAddComm2_Type()
)
tRPAdminPSAccActionAddComm2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm2.setStatus("current")


class _TRPAdminPSAccActionAddComm3_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm3 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm3_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm3_Object = MibTableColumn
tRPAdminPSAccActionAddComm3 = _TRPAdminPSAccActionAddComm3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 3),
    _TRPAdminPSAccActionAddComm3_Type()
)
tRPAdminPSAccActionAddComm3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm3.setStatus("current")


class _TRPAdminPSAccActionAddComm4_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm4 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm4_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm4_Object = MibTableColumn
tRPAdminPSAccActionAddComm4 = _TRPAdminPSAccActionAddComm4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 4),
    _TRPAdminPSAccActionAddComm4_Type()
)
tRPAdminPSAccActionAddComm4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm4.setStatus("current")


class _TRPAdminPSAccActionAddComm5_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm5 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm5_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm5_Object = MibTableColumn
tRPAdminPSAccActionAddComm5 = _TRPAdminPSAccActionAddComm5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 5),
    _TRPAdminPSAccActionAddComm5_Type()
)
tRPAdminPSAccActionAddComm5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm5.setStatus("current")


class _TRPAdminPSAccActionAddComm6_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm6 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm6_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm6_Object = MibTableColumn
tRPAdminPSAccActionAddComm6 = _TRPAdminPSAccActionAddComm6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 6),
    _TRPAdminPSAccActionAddComm6_Type()
)
tRPAdminPSAccActionAddComm6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm6.setStatus("current")


class _TRPAdminPSAccActionAddComm7_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm7 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm7_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm7_Object = MibTableColumn
tRPAdminPSAccActionAddComm7 = _TRPAdminPSAccActionAddComm7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 7),
    _TRPAdminPSAccActionAddComm7_Type()
)
tRPAdminPSAccActionAddComm7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm7.setStatus("current")


class _TRPAdminPSAccActionAddComm8_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm8 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm8_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm8_Object = MibTableColumn
tRPAdminPSAccActionAddComm8 = _TRPAdminPSAccActionAddComm8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 8),
    _TRPAdminPSAccActionAddComm8_Type()
)
tRPAdminPSAccActionAddComm8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm8.setStatus("current")


class _TRPAdminPSAccActionAddComm9_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm9 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm9_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm9_Object = MibTableColumn
tRPAdminPSAccActionAddComm9 = _TRPAdminPSAccActionAddComm9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 9),
    _TRPAdminPSAccActionAddComm9_Type()
)
tRPAdminPSAccActionAddComm9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm9.setStatus("current")


class _TRPAdminPSAccActionAddComm10_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm10 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm10_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm10_Object = MibTableColumn
tRPAdminPSAccActionAddComm10 = _TRPAdminPSAccActionAddComm10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 10),
    _TRPAdminPSAccActionAddComm10_Type()
)
tRPAdminPSAccActionAddComm10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm10.setStatus("current")


class _TRPAdminPSAccActionAddComm11_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm11 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm11_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm11_Object = MibTableColumn
tRPAdminPSAccActionAddComm11 = _TRPAdminPSAccActionAddComm11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 11),
    _TRPAdminPSAccActionAddComm11_Type()
)
tRPAdminPSAccActionAddComm11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm11.setStatus("current")


class _TRPAdminPSAccActionAddComm12_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm12 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm12_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm12_Object = MibTableColumn
tRPAdminPSAccActionAddComm12 = _TRPAdminPSAccActionAddComm12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 12),
    _TRPAdminPSAccActionAddComm12_Type()
)
tRPAdminPSAccActionAddComm12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm12.setStatus("current")


class _TRPAdminPSAccActionAddComm13_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm13 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm13_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm13_Object = MibTableColumn
tRPAdminPSAccActionAddComm13 = _TRPAdminPSAccActionAddComm13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 13),
    _TRPAdminPSAccActionAddComm13_Type()
)
tRPAdminPSAccActionAddComm13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm13.setStatus("current")


class _TRPAdminPSAccActionAddComm14_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm14 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm14_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm14_Object = MibTableColumn
tRPAdminPSAccActionAddComm14 = _TRPAdminPSAccActionAddComm14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 14),
    _TRPAdminPSAccActionAddComm14_Type()
)
tRPAdminPSAccActionAddComm14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm14.setStatus("current")


class _TRPAdminPSAccActionAddComm15_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm15 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm15_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm15_Object = MibTableColumn
tRPAdminPSAccActionAddComm15 = _TRPAdminPSAccActionAddComm15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 15),
    _TRPAdminPSAccActionAddComm15_Type()
)
tRPAdminPSAccActionAddComm15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm15.setStatus("current")


class _TRPAdminPSAccActionAddComm16_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm16 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm16_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm16_Object = MibTableColumn
tRPAdminPSAccActionAddComm16 = _TRPAdminPSAccActionAddComm16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 16),
    _TRPAdminPSAccActionAddComm16_Type()
)
tRPAdminPSAccActionAddComm16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm16.setStatus("current")


class _TRPAdminPSAccActionAddComm17_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm17 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm17_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm17_Object = MibTableColumn
tRPAdminPSAccActionAddComm17 = _TRPAdminPSAccActionAddComm17_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 17),
    _TRPAdminPSAccActionAddComm17_Type()
)
tRPAdminPSAccActionAddComm17.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm17.setStatus("current")


class _TRPAdminPSAccActionAddComm18_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm18 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm18_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm18_Object = MibTableColumn
tRPAdminPSAccActionAddComm18 = _TRPAdminPSAccActionAddComm18_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 18),
    _TRPAdminPSAccActionAddComm18_Type()
)
tRPAdminPSAccActionAddComm18.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm18.setStatus("current")


class _TRPAdminPSAccActionAddComm19_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm19 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm19_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm19_Object = MibTableColumn
tRPAdminPSAccActionAddComm19 = _TRPAdminPSAccActionAddComm19_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 19),
    _TRPAdminPSAccActionAddComm19_Type()
)
tRPAdminPSAccActionAddComm19.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm19.setStatus("current")


class _TRPAdminPSAccActionAddComm20_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm20 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm20_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm20_Object = MibTableColumn
tRPAdminPSAccActionAddComm20 = _TRPAdminPSAccActionAddComm20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 20),
    _TRPAdminPSAccActionAddComm20_Type()
)
tRPAdminPSAccActionAddComm20.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm20.setStatus("current")


class _TRPAdminPSAccActionAddComm21_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm21 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm21_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm21_Object = MibTableColumn
tRPAdminPSAccActionAddComm21 = _TRPAdminPSAccActionAddComm21_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 21),
    _TRPAdminPSAccActionAddComm21_Type()
)
tRPAdminPSAccActionAddComm21.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm21.setStatus("current")


class _TRPAdminPSAccActionAddComm22_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm22 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm22_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm22_Object = MibTableColumn
tRPAdminPSAccActionAddComm22 = _TRPAdminPSAccActionAddComm22_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 22),
    _TRPAdminPSAccActionAddComm22_Type()
)
tRPAdminPSAccActionAddComm22.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm22.setStatus("current")


class _TRPAdminPSAccActionAddComm23_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm23 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm23_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm23_Object = MibTableColumn
tRPAdminPSAccActionAddComm23 = _TRPAdminPSAccActionAddComm23_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 23),
    _TRPAdminPSAccActionAddComm23_Type()
)
tRPAdminPSAccActionAddComm23.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm23.setStatus("current")


class _TRPAdminPSAccActionAddComm24_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm24 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm24_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm24_Object = MibTableColumn
tRPAdminPSAccActionAddComm24 = _TRPAdminPSAccActionAddComm24_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 24),
    _TRPAdminPSAccActionAddComm24_Type()
)
tRPAdminPSAccActionAddComm24.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm24.setStatus("current")


class _TRPAdminPSAccActionAddComm25_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm25 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm25_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm25_Object = MibTableColumn
tRPAdminPSAccActionAddComm25 = _TRPAdminPSAccActionAddComm25_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 25),
    _TRPAdminPSAccActionAddComm25_Type()
)
tRPAdminPSAccActionAddComm25.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm25.setStatus("current")


class _TRPAdminPSAccActionAddComm26_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm26 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm26_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm26_Object = MibTableColumn
tRPAdminPSAccActionAddComm26 = _TRPAdminPSAccActionAddComm26_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 26),
    _TRPAdminPSAccActionAddComm26_Type()
)
tRPAdminPSAccActionAddComm26.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm26.setStatus("current")


class _TRPAdminPSAccActionAddComm27_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm27 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm27_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm27_Object = MibTableColumn
tRPAdminPSAccActionAddComm27 = _TRPAdminPSAccActionAddComm27_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 27),
    _TRPAdminPSAccActionAddComm27_Type()
)
tRPAdminPSAccActionAddComm27.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm27.setStatus("current")


class _TRPAdminPSAccActionAddComm28_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionAddComm28 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionAddComm28_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionAddComm28_Object = MibTableColumn
tRPAdminPSAccActionAddComm28 = _TRPAdminPSAccActionAddComm28_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 28),
    _TRPAdminPSAccActionAddComm28_Type()
)
tRPAdminPSAccActionAddComm28.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddComm28.setStatus("current")
_TRPAdminPSAccActionAddCommCrOrig_Type = TmnxCreateOrigin
_TRPAdminPSAccActionAddCommCrOrig_Object = MibTableColumn
tRPAdminPSAccActionAddCommCrOrig = _TRPAdminPSAccActionAddCommCrOrig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 18, 1, 29),
    _TRPAdminPSAccActionAddCommCrOrig_Type()
)
tRPAdminPSAccActionAddCommCrOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionAddCommCrOrig.setStatus("current")
_TRPAdminPSAccActionRemCommTable_Object = MibTable
tRPAdminPSAccActionRemCommTable = _TRPAdminPSAccActionRemCommTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19)
)
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemCommTable.setStatus("current")
_TRPAdminPSAccActionRemCommEntry_Object = MibTableRow
tRPAdminPSAccActionRemCommEntry = _TRPAdminPSAccActionRemCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1)
)
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemCommEntry.setStatus("current")


class _TRPAdminPSAccActionRemoveComm1_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm1 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm1_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm1_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm1 = _TRPAdminPSAccActionRemoveComm1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 1),
    _TRPAdminPSAccActionRemoveComm1_Type()
)
tRPAdminPSAccActionRemoveComm1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm1.setStatus("current")


class _TRPAdminPSAccActionRemoveComm2_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm2 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm2_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm2_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm2 = _TRPAdminPSAccActionRemoveComm2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 2),
    _TRPAdminPSAccActionRemoveComm2_Type()
)
tRPAdminPSAccActionRemoveComm2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm2.setStatus("current")


class _TRPAdminPSAccActionRemoveComm3_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm3 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm3_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm3_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm3 = _TRPAdminPSAccActionRemoveComm3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 3),
    _TRPAdminPSAccActionRemoveComm3_Type()
)
tRPAdminPSAccActionRemoveComm3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm3.setStatus("current")


class _TRPAdminPSAccActionRemoveComm4_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm4 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm4_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm4_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm4 = _TRPAdminPSAccActionRemoveComm4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 4),
    _TRPAdminPSAccActionRemoveComm4_Type()
)
tRPAdminPSAccActionRemoveComm4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm4.setStatus("current")


class _TRPAdminPSAccActionRemoveComm5_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm5 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm5_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm5_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm5 = _TRPAdminPSAccActionRemoveComm5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 5),
    _TRPAdminPSAccActionRemoveComm5_Type()
)
tRPAdminPSAccActionRemoveComm5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm5.setStatus("current")


class _TRPAdminPSAccActionRemoveComm6_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm6 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm6_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm6_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm6 = _TRPAdminPSAccActionRemoveComm6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 6),
    _TRPAdminPSAccActionRemoveComm6_Type()
)
tRPAdminPSAccActionRemoveComm6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm6.setStatus("current")


class _TRPAdminPSAccActionRemoveComm7_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm7 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm7_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm7_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm7 = _TRPAdminPSAccActionRemoveComm7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 7),
    _TRPAdminPSAccActionRemoveComm7_Type()
)
tRPAdminPSAccActionRemoveComm7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm7.setStatus("current")


class _TRPAdminPSAccActionRemoveComm8_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm8 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm8_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm8_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm8 = _TRPAdminPSAccActionRemoveComm8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 8),
    _TRPAdminPSAccActionRemoveComm8_Type()
)
tRPAdminPSAccActionRemoveComm8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm8.setStatus("current")


class _TRPAdminPSAccActionRemoveComm9_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm9 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm9_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm9_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm9 = _TRPAdminPSAccActionRemoveComm9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 9),
    _TRPAdminPSAccActionRemoveComm9_Type()
)
tRPAdminPSAccActionRemoveComm9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm9.setStatus("current")


class _TRPAdminPSAccActionRemoveComm10_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm10 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm10_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm10_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm10 = _TRPAdminPSAccActionRemoveComm10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 10),
    _TRPAdminPSAccActionRemoveComm10_Type()
)
tRPAdminPSAccActionRemoveComm10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm10.setStatus("current")


class _TRPAdminPSAccActionRemoveComm11_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm11 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm11_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm11_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm11 = _TRPAdminPSAccActionRemoveComm11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 11),
    _TRPAdminPSAccActionRemoveComm11_Type()
)
tRPAdminPSAccActionRemoveComm11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm11.setStatus("current")


class _TRPAdminPSAccActionRemoveComm12_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm12 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm12_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm12_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm12 = _TRPAdminPSAccActionRemoveComm12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 12),
    _TRPAdminPSAccActionRemoveComm12_Type()
)
tRPAdminPSAccActionRemoveComm12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm12.setStatus("current")


class _TRPAdminPSAccActionRemoveComm13_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm13 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm13_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm13_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm13 = _TRPAdminPSAccActionRemoveComm13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 13),
    _TRPAdminPSAccActionRemoveComm13_Type()
)
tRPAdminPSAccActionRemoveComm13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm13.setStatus("current")


class _TRPAdminPSAccActionRemoveComm14_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm14 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm14_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm14_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm14 = _TRPAdminPSAccActionRemoveComm14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 14),
    _TRPAdminPSAccActionRemoveComm14_Type()
)
tRPAdminPSAccActionRemoveComm14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm14.setStatus("current")


class _TRPAdminPSAccActionRemoveComm15_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm15 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm15_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm15_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm15 = _TRPAdminPSAccActionRemoveComm15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 15),
    _TRPAdminPSAccActionRemoveComm15_Type()
)
tRPAdminPSAccActionRemoveComm15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm15.setStatus("current")


class _TRPAdminPSAccActionRemoveComm16_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm16 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm16_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm16_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm16 = _TRPAdminPSAccActionRemoveComm16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 16),
    _TRPAdminPSAccActionRemoveComm16_Type()
)
tRPAdminPSAccActionRemoveComm16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm16.setStatus("current")


class _TRPAdminPSAccActionRemoveComm17_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm17 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm17_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm17_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm17 = _TRPAdminPSAccActionRemoveComm17_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 17),
    _TRPAdminPSAccActionRemoveComm17_Type()
)
tRPAdminPSAccActionRemoveComm17.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm17.setStatus("current")


class _TRPAdminPSAccActionRemoveComm18_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm18 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm18_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm18_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm18 = _TRPAdminPSAccActionRemoveComm18_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 18),
    _TRPAdminPSAccActionRemoveComm18_Type()
)
tRPAdminPSAccActionRemoveComm18.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm18.setStatus("current")


class _TRPAdminPSAccActionRemoveComm19_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm19 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm19_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm19_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm19 = _TRPAdminPSAccActionRemoveComm19_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 19),
    _TRPAdminPSAccActionRemoveComm19_Type()
)
tRPAdminPSAccActionRemoveComm19.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm19.setStatus("current")


class _TRPAdminPSAccActionRemoveComm20_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm20 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm20_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm20_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm20 = _TRPAdminPSAccActionRemoveComm20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 20),
    _TRPAdminPSAccActionRemoveComm20_Type()
)
tRPAdminPSAccActionRemoveComm20.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm20.setStatus("current")


class _TRPAdminPSAccActionRemoveComm21_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm21 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm21_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm21_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm21 = _TRPAdminPSAccActionRemoveComm21_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 21),
    _TRPAdminPSAccActionRemoveComm21_Type()
)
tRPAdminPSAccActionRemoveComm21.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm21.setStatus("current")


class _TRPAdminPSAccActionRemoveComm22_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm22 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm22_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm22_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm22 = _TRPAdminPSAccActionRemoveComm22_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 22),
    _TRPAdminPSAccActionRemoveComm22_Type()
)
tRPAdminPSAccActionRemoveComm22.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm22.setStatus("current")


class _TRPAdminPSAccActionRemoveComm23_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm23 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm23_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm23_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm23 = _TRPAdminPSAccActionRemoveComm23_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 23),
    _TRPAdminPSAccActionRemoveComm23_Type()
)
tRPAdminPSAccActionRemoveComm23.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm23.setStatus("current")


class _TRPAdminPSAccActionRemoveComm24_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm24 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm24_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm24_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm24 = _TRPAdminPSAccActionRemoveComm24_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 24),
    _TRPAdminPSAccActionRemoveComm24_Type()
)
tRPAdminPSAccActionRemoveComm24.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm24.setStatus("current")


class _TRPAdminPSAccActionRemoveComm25_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm25 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm25_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm25_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm25 = _TRPAdminPSAccActionRemoveComm25_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 25),
    _TRPAdminPSAccActionRemoveComm25_Type()
)
tRPAdminPSAccActionRemoveComm25.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm25.setStatus("current")


class _TRPAdminPSAccActionRemoveComm26_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm26 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm26_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm26_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm26 = _TRPAdminPSAccActionRemoveComm26_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 26),
    _TRPAdminPSAccActionRemoveComm26_Type()
)
tRPAdminPSAccActionRemoveComm26.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm26.setStatus("current")


class _TRPAdminPSAccActionRemoveComm27_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm27 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm27_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm27_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm27 = _TRPAdminPSAccActionRemoveComm27_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 27),
    _TRPAdminPSAccActionRemoveComm27_Type()
)
tRPAdminPSAccActionRemoveComm27.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm27.setStatus("current")


class _TRPAdminPSAccActionRemoveComm28_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionRemoveComm28 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionRemoveComm28_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionRemoveComm28_Object = MibTableColumn
tRPAdminPSAccActionRemoveComm28 = _TRPAdminPSAccActionRemoveComm28_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 19, 1, 28),
    _TRPAdminPSAccActionRemoveComm28_Type()
)
tRPAdminPSAccActionRemoveComm28.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRemoveComm28.setStatus("current")
_TRPAdminPSAccActionRepCommTable_Object = MibTable
tRPAdminPSAccActionRepCommTable = _TRPAdminPSAccActionRepCommTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20)
)
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRepCommTable.setStatus("current")
_TRPAdminPSAccActionRepCommEntry_Object = MibTableRow
tRPAdminPSAccActionRepCommEntry = _TRPAdminPSAccActionRepCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1)
)
if mibBuilder.loadTexts:
    tRPAdminPSAccActionRepCommEntry.setStatus("current")


class _TRPAdminPSAccActionReplaceComm1_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm1 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm1_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm1_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm1 = _TRPAdminPSAccActionReplaceComm1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 1),
    _TRPAdminPSAccActionReplaceComm1_Type()
)
tRPAdminPSAccActionReplaceComm1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm1.setStatus("current")


class _TRPAdminPSAccActionReplaceComm2_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm2 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm2_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm2_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm2 = _TRPAdminPSAccActionReplaceComm2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 2),
    _TRPAdminPSAccActionReplaceComm2_Type()
)
tRPAdminPSAccActionReplaceComm2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm2.setStatus("current")


class _TRPAdminPSAccActionReplaceComm3_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm3 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm3_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm3_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm3 = _TRPAdminPSAccActionReplaceComm3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 3),
    _TRPAdminPSAccActionReplaceComm3_Type()
)
tRPAdminPSAccActionReplaceComm3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm3.setStatus("current")


class _TRPAdminPSAccActionReplaceComm4_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm4 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm4_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm4_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm4 = _TRPAdminPSAccActionReplaceComm4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 4),
    _TRPAdminPSAccActionReplaceComm4_Type()
)
tRPAdminPSAccActionReplaceComm4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm4.setStatus("current")


class _TRPAdminPSAccActionReplaceComm5_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm5 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm5_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm5_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm5 = _TRPAdminPSAccActionReplaceComm5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 5),
    _TRPAdminPSAccActionReplaceComm5_Type()
)
tRPAdminPSAccActionReplaceComm5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm5.setStatus("current")


class _TRPAdminPSAccActionReplaceComm6_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm6 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm6_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm6_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm6 = _TRPAdminPSAccActionReplaceComm6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 6),
    _TRPAdminPSAccActionReplaceComm6_Type()
)
tRPAdminPSAccActionReplaceComm6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm6.setStatus("current")


class _TRPAdminPSAccActionReplaceComm7_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm7 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm7_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm7_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm7 = _TRPAdminPSAccActionReplaceComm7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 7),
    _TRPAdminPSAccActionReplaceComm7_Type()
)
tRPAdminPSAccActionReplaceComm7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm7.setStatus("current")


class _TRPAdminPSAccActionReplaceComm8_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm8 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm8_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm8_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm8 = _TRPAdminPSAccActionReplaceComm8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 8),
    _TRPAdminPSAccActionReplaceComm8_Type()
)
tRPAdminPSAccActionReplaceComm8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm8.setStatus("current")


class _TRPAdminPSAccActionReplaceComm9_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm9 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm9_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm9_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm9 = _TRPAdminPSAccActionReplaceComm9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 9),
    _TRPAdminPSAccActionReplaceComm9_Type()
)
tRPAdminPSAccActionReplaceComm9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm9.setStatus("current")


class _TRPAdminPSAccActionReplaceComm10_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm10 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm10_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm10_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm10 = _TRPAdminPSAccActionReplaceComm10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 10),
    _TRPAdminPSAccActionReplaceComm10_Type()
)
tRPAdminPSAccActionReplaceComm10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm10.setStatus("current")


class _TRPAdminPSAccActionReplaceComm11_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm11 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm11_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm11_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm11 = _TRPAdminPSAccActionReplaceComm11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 11),
    _TRPAdminPSAccActionReplaceComm11_Type()
)
tRPAdminPSAccActionReplaceComm11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm11.setStatus("current")


class _TRPAdminPSAccActionReplaceComm12_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm12 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm12_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm12_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm12 = _TRPAdminPSAccActionReplaceComm12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 12),
    _TRPAdminPSAccActionReplaceComm12_Type()
)
tRPAdminPSAccActionReplaceComm12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm12.setStatus("current")


class _TRPAdminPSAccActionReplaceComm13_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm13 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm13_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm13_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm13 = _TRPAdminPSAccActionReplaceComm13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 13),
    _TRPAdminPSAccActionReplaceComm13_Type()
)
tRPAdminPSAccActionReplaceComm13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm13.setStatus("current")


class _TRPAdminPSAccActionReplaceComm14_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm14 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm14_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm14_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm14 = _TRPAdminPSAccActionReplaceComm14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 14),
    _TRPAdminPSAccActionReplaceComm14_Type()
)
tRPAdminPSAccActionReplaceComm14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm14.setStatus("current")


class _TRPAdminPSAccActionReplaceComm15_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm15 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm15_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm15_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm15 = _TRPAdminPSAccActionReplaceComm15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 15),
    _TRPAdminPSAccActionReplaceComm15_Type()
)
tRPAdminPSAccActionReplaceComm15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm15.setStatus("current")


class _TRPAdminPSAccActionReplaceComm16_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm16 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm16_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm16_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm16 = _TRPAdminPSAccActionReplaceComm16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 16),
    _TRPAdminPSAccActionReplaceComm16_Type()
)
tRPAdminPSAccActionReplaceComm16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm16.setStatus("current")


class _TRPAdminPSAccActionReplaceComm17_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm17 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm17_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm17_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm17 = _TRPAdminPSAccActionReplaceComm17_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 17),
    _TRPAdminPSAccActionReplaceComm17_Type()
)
tRPAdminPSAccActionReplaceComm17.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm17.setStatus("current")


class _TRPAdminPSAccActionReplaceComm18_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm18 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm18_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm18_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm18 = _TRPAdminPSAccActionReplaceComm18_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 18),
    _TRPAdminPSAccActionReplaceComm18_Type()
)
tRPAdminPSAccActionReplaceComm18.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm18.setStatus("current")


class _TRPAdminPSAccActionReplaceComm19_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm19 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm19_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm19_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm19 = _TRPAdminPSAccActionReplaceComm19_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 19),
    _TRPAdminPSAccActionReplaceComm19_Type()
)
tRPAdminPSAccActionReplaceComm19.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm19.setStatus("current")


class _TRPAdminPSAccActionReplaceComm20_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm20 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm20_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm20_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm20 = _TRPAdminPSAccActionReplaceComm20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 20),
    _TRPAdminPSAccActionReplaceComm20_Type()
)
tRPAdminPSAccActionReplaceComm20.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm20.setStatus("current")


class _TRPAdminPSAccActionReplaceComm21_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm21 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm21_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm21_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm21 = _TRPAdminPSAccActionReplaceComm21_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 21),
    _TRPAdminPSAccActionReplaceComm21_Type()
)
tRPAdminPSAccActionReplaceComm21.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm21.setStatus("current")


class _TRPAdminPSAccActionReplaceComm22_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm22 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm22_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm22_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm22 = _TRPAdminPSAccActionReplaceComm22_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 22),
    _TRPAdminPSAccActionReplaceComm22_Type()
)
tRPAdminPSAccActionReplaceComm22.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm22.setStatus("current")


class _TRPAdminPSAccActionReplaceComm23_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm23 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm23_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm23_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm23 = _TRPAdminPSAccActionReplaceComm23_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 23),
    _TRPAdminPSAccActionReplaceComm23_Type()
)
tRPAdminPSAccActionReplaceComm23.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm23.setStatus("current")


class _TRPAdminPSAccActionReplaceComm24_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm24 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm24_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm24_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm24 = _TRPAdminPSAccActionReplaceComm24_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 24),
    _TRPAdminPSAccActionReplaceComm24_Type()
)
tRPAdminPSAccActionReplaceComm24.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm24.setStatus("current")


class _TRPAdminPSAccActionReplaceComm25_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm25 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm25_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm25_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm25 = _TRPAdminPSAccActionReplaceComm25_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 25),
    _TRPAdminPSAccActionReplaceComm25_Type()
)
tRPAdminPSAccActionReplaceComm25.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm25.setStatus("current")


class _TRPAdminPSAccActionReplaceComm26_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm26 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm26_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm26_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm26 = _TRPAdminPSAccActionReplaceComm26_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 26),
    _TRPAdminPSAccActionReplaceComm26_Type()
)
tRPAdminPSAccActionReplaceComm26.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm26.setStatus("current")


class _TRPAdminPSAccActionReplaceComm27_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm27 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm27_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm27_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm27 = _TRPAdminPSAccActionReplaceComm27_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 27),
    _TRPAdminPSAccActionReplaceComm27_Type()
)
tRPAdminPSAccActionReplaceComm27.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm27.setStatus("current")


class _TRPAdminPSAccActionReplaceComm28_Type(TCommunityName):
    """Custom type tRPAdminPSAccActionReplaceComm28 based on TCommunityName"""
    defaultValue = OctetString("")


_TRPAdminPSAccActionReplaceComm28_Type.__name__ = "TCommunityName"
_TRPAdminPSAccActionReplaceComm28_Object = MibTableColumn
tRPAdminPSAccActionReplaceComm28 = _TRPAdminPSAccActionReplaceComm28_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 20, 1, 28),
    _TRPAdminPSAccActionReplaceComm28_Type()
)
tRPAdminPSAccActionReplaceComm28.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAccActionReplaceComm28.setStatus("current")
_TRPAdminPSFromCriteriaExtTable_Object = MibTable
tRPAdminPSFromCriteriaExtTable = _TRPAdminPSFromCriteriaExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 21)
)
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaExtTable.setStatus("current")
_TRPAdminPSFromCriteriaExtEntry_Object = MibTableRow
tRPAdminPSFromCriteriaExtEntry = _TRPAdminPSFromCriteriaExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 21, 1)
)
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaExtEntry.setStatus("current")


class _TRPAdminPSFromCritExtMvpnType_Type(TPolicyEntryCriteriaMvpnType):
    """Custom type tRPAdminPSFromCritExtMvpnType based on TPolicyEntryCriteriaMvpnType"""
    defaultValue = 0


_TRPAdminPSFromCritExtMvpnType_Type.__name__ = "TPolicyEntryCriteriaMvpnType"
_TRPAdminPSFromCritExtMvpnType_Object = MibTableColumn
tRPAdminPSFromCritExtMvpnType = _TRPAdminPSFromCritExtMvpnType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 21, 1, 1),
    _TRPAdminPSFromCritExtMvpnType_Type()
)
tRPAdminPSFromCritExtMvpnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCritExtMvpnType.setStatus("current")


class _TRPAdminPSFromCritSrcAddrPfxList_Type(TPrefixListName):
    """Custom type tRPAdminPSFromCritSrcAddrPfxList based on TPrefixListName"""
    defaultValue = OctetString("")


_TRPAdminPSFromCritSrcAddrPfxList_Type.__name__ = "TPrefixListName"
_TRPAdminPSFromCritSrcAddrPfxList_Object = MibTableColumn
tRPAdminPSFromCritSrcAddrPfxList = _TRPAdminPSFromCritSrcAddrPfxList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 21, 1, 2),
    _TRPAdminPSFromCritSrcAddrPfxList_Type()
)
tRPAdminPSFromCritSrcAddrPfxList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCritSrcAddrPfxList.setStatus("current")


class _TRPAdminPSFromCritOrigValidState_Type(Integer32):
    """Custom type tRPAdminPSFromCritOrigValidState based on Integer32"""
    defaultValue = 0

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
        *(("notApplicable", 0),
          ("valid", 1),
          ("notFound", 2),
          ("invalid", 3))
    )


_TRPAdminPSFromCritOrigValidState_Type.__name__ = "Integer32"
_TRPAdminPSFromCritOrigValidState_Object = MibTableColumn
tRPAdminPSFromCritOrigValidState = _TRPAdminPSFromCritOrigValidState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 21, 1, 3),
    _TRPAdminPSFromCritOrigValidState_Type()
)
tRPAdminPSFromCritOrigValidState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCritOrigValidState.setStatus("current")
_TRPAdminPSPolicyVariableTable_Object = MibTable
tRPAdminPSPolicyVariableTable = _TRPAdminPSPolicyVariableTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 22)
)
if mibBuilder.loadTexts:
    tRPAdminPSPolicyVariableTable.setStatus("current")
_TRPAdminPSPolicyVariableEntry_Object = MibTableRow
tRPAdminPSPolicyVariableEntry = _TRPAdminPSPolicyVariableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 22, 1)
)
tRPAdminPSPolicyVariableEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIndex"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSPolicyVarName"),
)
if mibBuilder.loadTexts:
    tRPAdminPSPolicyVariableEntry.setStatus("current")
_TRPAdminPSPolicyVarName_Type = TPolicyVariableName
_TRPAdminPSPolicyVarName_Object = MibTableColumn
tRPAdminPSPolicyVarName = _TRPAdminPSPolicyVarName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 22, 1, 1),
    _TRPAdminPSPolicyVarName_Type()
)
tRPAdminPSPolicyVarName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminPSPolicyVarName.setStatus("current")
_TRPAdminPSPolicyVarRowStatus_Type = RowStatus
_TRPAdminPSPolicyVarRowStatus_Object = MibTableColumn
tRPAdminPSPolicyVarRowStatus = _TRPAdminPSPolicyVarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 22, 1, 2),
    _TRPAdminPSPolicyVarRowStatus_Type()
)
tRPAdminPSPolicyVarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSPolicyVarRowStatus.setStatus("current")
_TRPAdminPSPolicyVarValue_Type = TNamedItem
_TRPAdminPSPolicyVarValue_Object = MibTableColumn
tRPAdminPSPolicyVarValue = _TRPAdminPSPolicyVarValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 22, 1, 3),
    _TRPAdminPSPolicyVarValue_Type()
)
tRPAdminPSPolicyVarValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSPolicyVarValue.setStatus("current")
_TRPAdminPSAcptActParamsExtTable_Object = MibTable
tRPAdminPSAcptActParamsExtTable = _TRPAdminPSAcptActParamsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 23)
)
if mibBuilder.loadTexts:
    tRPAdminPSAcptActParamsExtTable.setStatus("current")
_TRPAdminPSAcptActParamsExtEntry_Object = MibTableRow
tRPAdminPSAcptActParamsExtEntry = _TRPAdminPSAcptActParamsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 23, 1)
)
if mibBuilder.loadTexts:
    tRPAdminPSAcptActParamsExtEntry.setStatus("current")


class _TRPAdminPSAcptActStickyEcmp_Type(TruthValue):
    """Custom type tRPAdminPSAcptActStickyEcmp based on TruthValue"""
    defaultValue = 2


_TRPAdminPSAcptActStickyEcmp_Type.__name__ = "TruthValue"
_TRPAdminPSAcptActStickyEcmp_Object = MibTableColumn
tRPAdminPSAcptActStickyEcmp = _TRPAdminPSAcptActStickyEcmp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 23, 1, 1),
    _TRPAdminPSAcptActStickyEcmp_Type()
)
tRPAdminPSAcptActStickyEcmp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActStickyEcmp.setStatus("current")


class _TRPAdminPSAcptActBgpLeaking_Type(TruthValue):
    """Custom type tRPAdminPSAcptActBgpLeaking based on TruthValue"""
    defaultValue = 2


_TRPAdminPSAcptActBgpLeaking_Type.__name__ = "TruthValue"
_TRPAdminPSAcptActBgpLeaking_Object = MibTableColumn
tRPAdminPSAcptActBgpLeaking = _TRPAdminPSAcptActBgpLeaking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 23, 1, 5),
    _TRPAdminPSAcptActBgpLeaking_Type()
)
tRPAdminPSAcptActBgpLeaking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActBgpLeaking.setStatus("current")
_TRPAdminPSDefActParamsExtTable_Object = MibTable
tRPAdminPSDefActParamsExtTable = _TRPAdminPSDefActParamsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 24)
)
if mibBuilder.loadTexts:
    tRPAdminPSDefActParamsExtTable.setStatus("current")
_TRPAdminPSDefActParamsExtEntry_Object = MibTableRow
tRPAdminPSDefActParamsExtEntry = _TRPAdminPSDefActParamsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 24, 1)
)
if mibBuilder.loadTexts:
    tRPAdminPSDefActParamsExtEntry.setStatus("current")


class _TRPAdminPSDefActStickyEcmp_Type(TruthValue):
    """Custom type tRPAdminPSDefActStickyEcmp based on TruthValue"""
    defaultValue = 2


_TRPAdminPSDefActStickyEcmp_Type.__name__ = "TruthValue"
_TRPAdminPSDefActStickyEcmp_Object = MibTableColumn
tRPAdminPSDefActStickyEcmp = _TRPAdminPSDefActStickyEcmp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 24, 1, 1),
    _TRPAdminPSDefActStickyEcmp_Type()
)
tRPAdminPSDefActStickyEcmp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActStickyEcmp.setStatus("current")


class _TRPAdminPSDefActBgpLeaking_Type(TruthValue):
    """Custom type tRPAdminPSDefActBgpLeaking based on TruthValue"""
    defaultValue = 2


_TRPAdminPSDefActBgpLeaking_Type.__name__ = "TruthValue"
_TRPAdminPSDefActBgpLeaking_Object = MibTableColumn
tRPAdminPSDefActBgpLeaking = _TRPAdminPSDefActBgpLeaking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 24, 1, 5),
    _TRPAdminPSDefActBgpLeaking_Type()
)
tRPAdminPSDefActBgpLeaking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActBgpLeaking.setStatus("current")
_TRoutePolicyNotifyPrefix_ObjectIdentity = ObjectIdentity
tRoutePolicyNotifyPrefix = _TRoutePolicyNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 17)
)
_TRoutePolicyNotifications_ObjectIdentity = ObjectIdentity
tRoutePolicyNotifications = _TRoutePolicyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 17, 0)
)
tRPOperPSDefaultActionParamsEntry.registerAugmentions(
    ("TIMETRA-ROUTE-POLICY-MIB",
     "tRPOperPSDefActionRemCommEntry")
)
tRPOperPSDefActionRemCommEntry.setIndexNames(*tRPOperPSDefaultActionParamsEntry.getIndexNames())
tRPOperPSDefaultActionParamsEntry.registerAugmentions(
    ("TIMETRA-ROUTE-POLICY-MIB",
     "tRPOperPSDefActionRepCommEntry")
)
tRPOperPSDefActionRepCommEntry.setIndexNames(*tRPOperPSDefaultActionParamsEntry.getIndexNames())
tRPOperPSAcceptActionParamsEntry.registerAugmentions(
    ("TIMETRA-ROUTE-POLICY-MIB",
     "tRPOperPSAccActionAddCommEntry")
)
tRPOperPSAccActionAddCommEntry.setIndexNames(*tRPOperPSAcceptActionParamsEntry.getIndexNames())
tRPOperPSAcceptActionParamsEntry.registerAugmentions(
    ("TIMETRA-ROUTE-POLICY-MIB",
     "tRPOperPSAccActionRemCommEntry")
)
tRPOperPSAccActionRemCommEntry.setIndexNames(*tRPOperPSAcceptActionParamsEntry.getIndexNames())
tRPOperPSAcceptActionParamsEntry.registerAugmentions(
    ("TIMETRA-ROUTE-POLICY-MIB",
     "tRPOperPSAccActionRepCommEntry")
)
tRPOperPSAccActionRepCommEntry.setIndexNames(*tRPOperPSAcceptActionParamsEntry.getIndexNames())
tRPOperPSFromCriteriaEntry.registerAugmentions(
    ("TIMETRA-ROUTE-POLICY-MIB",
     "tRPOperPSFromCriteriaExtEntry")
)
tRPOperPSFromCriteriaExtEntry.setIndexNames(*tRPOperPSFromCriteriaEntry.getIndexNames())
tRPOperPSAcceptActionParamsEntry.registerAugmentions(
    ("TIMETRA-ROUTE-POLICY-MIB",
     "tRPOperPSAcptActParamsExtEntry")
)
tRPOperPSAcptActParamsExtEntry.setIndexNames(*tRPOperPSAcceptActionParamsEntry.getIndexNames())
tRPOperPSDefaultActionParamsEntry.registerAugmentions(
    ("TIMETRA-ROUTE-POLICY-MIB",
     "tRPOperPSDefActParamsExtEntry")
)
tRPOperPSDefActParamsExtEntry.setIndexNames(*tRPOperPSDefaultActionParamsEntry.getIndexNames())
tRPAdminPSDefaultActionParamsEntry.registerAugmentions(
    ("TIMETRA-ROUTE-POLICY-MIB",
     "tRPAdminPSDefActionAddCommEntry")
)
tRPAdminPSDefActionAddCommEntry.setIndexNames(*tRPAdminPSDefaultActionParamsEntry.getIndexNames())
tRPAdminPSDefaultActionParamsEntry.registerAugmentions(
    ("TIMETRA-ROUTE-POLICY-MIB",
     "tRPAdminPSDefActionRemCommEntry")
)
tRPAdminPSDefActionRemCommEntry.setIndexNames(*tRPAdminPSDefaultActionParamsEntry.getIndexNames())
tRPAdminPSDefaultActionParamsEntry.registerAugmentions(
    ("TIMETRA-ROUTE-POLICY-MIB",
     "tRPAdminPSDefActionRepCommEntry")
)
tRPAdminPSDefActionRepCommEntry.setIndexNames(*tRPAdminPSDefaultActionParamsEntry.getIndexNames())
tRPAdminPSAcceptActionParamsEntry.registerAugmentions(
    ("TIMETRA-ROUTE-POLICY-MIB",
     "tRPAdminPSAccActionAddCommEntry")
)
tRPAdminPSAccActionAddCommEntry.setIndexNames(*tRPAdminPSAcceptActionParamsEntry.getIndexNames())
tRPAdminPSAcceptActionParamsEntry.registerAugmentions(
    ("TIMETRA-ROUTE-POLICY-MIB",
     "tRPAdminPSAccActionRemCommEntry")
)
tRPAdminPSAccActionRemCommEntry.setIndexNames(*tRPAdminPSAcceptActionParamsEntry.getIndexNames())
tRPAdminPSAcceptActionParamsEntry.registerAugmentions(
    ("TIMETRA-ROUTE-POLICY-MIB",
     "tRPAdminPSAccActionRepCommEntry")
)
tRPAdminPSAccActionRepCommEntry.setIndexNames(*tRPAdminPSAcceptActionParamsEntry.getIndexNames())
tRPAdminPSFromCriteriaEntry.registerAugmentions(
    ("TIMETRA-ROUTE-POLICY-MIB",
     "tRPAdminPSFromCriteriaExtEntry")
)
tRPAdminPSFromCriteriaExtEntry.setIndexNames(*tRPAdminPSFromCriteriaEntry.getIndexNames())
tRPAdminPSAcceptActionParamsEntry.registerAugmentions(
    ("TIMETRA-ROUTE-POLICY-MIB",
     "tRPAdminPSAcptActParamsExtEntry")
)
tRPAdminPSAcptActParamsExtEntry.setIndexNames(*tRPAdminPSAcceptActionParamsEntry.getIndexNames())
tRPAdminPSDefaultActionParamsEntry.registerAugmentions(
    ("TIMETRA-ROUTE-POLICY-MIB",
     "tRPAdminPSDefActParamsExtEntry")
)
tRPAdminPSDefActParamsExtEntry.setIndexNames(*tRPAdminPSDefaultActionParamsEntry.getIndexNames())

# Managed Objects groups

tmnxRPAdminControlObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 1)
)
tmnxRPAdminControlObjectsGroup.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminOwner"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminControlApply"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminLastSetTimer"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminLastSetTimeout"))
)
if mibBuilder.loadTexts:
    tmnxRPAdminControlObjectsGroup.setStatus("current")

tmnxRPASPathObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 2)
)
tmnxRPASPathObjectsGroup.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathRegEx"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathRegEx"))
)
if mibBuilder.loadTexts:
    tmnxRPASPathObjectsGroup.setStatus("obsolete")

tmnxRPCommunityObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 3)
)
tmnxRPCommunityObjectsGroup.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxRPCommunityObjectsGroup.setStatus("obsolete")

tmnxRPDampingObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 4)
)
tmnxRPDampingObjectsGroup.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingHalfLife"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingMaxSuppress"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingReuse"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingSuppress"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingHalfLife"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingMaxSuppress"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingReuse"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingSuppress"))
)
if mibBuilder.loadTexts:
    tmnxRPDampingObjectsGroup.setStatus("obsolete")

tmnxRPPrefixListObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 5)
)
tmnxRPPrefixListObjectsGroup.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListThroughLength"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListBeginLength"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListThroughLength"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListBeginLength"))
)
if mibBuilder.loadTexts:
    tmnxRPPrefixListObjectsGroup.setStatus("obsolete")

tmnxRPPolicyObjectsV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 9)
)
tmnxRPPolicyObjectsV4v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementDefaultAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionParamsTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionParamsEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementDefaultAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActInetNextHop"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObjectsV4v0Group.setStatus("obsolete")

tmnxRPPolicyEntryObjectsV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 10)
)
tmnxRPPolicyEntryObjectsV4v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionParamsTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionParamsEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaCommunity"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaOspfRouteType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaArea"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaAreaConfigured"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIsisExternal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIgmpHostPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaGrpAddrPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaSrcAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaInterface"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaFamily"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaCommunity"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaOspfRouteType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaArea"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaAreaConfigured"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIsisExternal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIgmpHostPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaGrpAddrPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaSrcAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaInterface"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaFamily"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyEntryObjectsV4v0Group.setStatus("obsolete")

tmnxRPInetPrefixListObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 11)
)
tmnxRPInetPrefixListObjectsGroup.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListTblLastChg"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListThroughLen"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListLastChg"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListBeginLen"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListThroughLen"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListBeginLen"))
)
if mibBuilder.loadTexts:
    tmnxRPInetPrefixListObjectsGroup.setStatus("obsolete")

tmnxRPPolicyEntryObjectsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 12)
)
tmnxRPPolicyEntryObjectsV5v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaCommunity"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaOspfRouteType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaArea"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaAreaConfigured"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIsisExternal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIgmpHostPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaGrpAddrPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaSrcAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaInterface"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaFamily"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaCommunity"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaOspfRouteType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaArea"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaAreaConfigured"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIsisExternal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIgmpHostPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaGrpAddrPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaSrcAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaInterface"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaFamily"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaInstanceId"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyEntryObjectsV5v0Group.setStatus("obsolete")

tmnxRPPolicyObsoleteV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 13)
)
tmnxRPPolicyObsoleteV5v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionParamsTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionParamsEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionParamsTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionParamsEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListTblLastChg"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListLastChg"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObsoleteV5v0Group.setStatus("current")

tmnxRPASPathObjectsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 14)
)
tmnxRPASPathObjectsV5v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathRegEx"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathRegEx"))
)
if mibBuilder.loadTexts:
    tmnxRPASPathObjectsV5v0Group.setStatus("current")

tmnxRPCommunityObjectsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 15)
)
tmnxRPCommunityObjectsV5v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxRPCommunityObjectsV5v0Group.setStatus("current")

tmnxRPDampingObjectsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 16)
)
tmnxRPDampingObjectsV5v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingHalfLife"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingMaxSuppress"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingReuse"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingSuppress"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingHalfLife"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingMaxSuppress"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingReuse"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingSuppress"))
)
if mibBuilder.loadTexts:
    tmnxRPDampingObjectsV5v0Group.setStatus("current")

tmnxRPPrefixListObjectsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 17)
)
tmnxRPPrefixListObjectsV5v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListThroughLength"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListBeginLength"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListThroughLength"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListBeginLength"))
)
if mibBuilder.loadTexts:
    tmnxRPPrefixListObjectsV5v0Group.setStatus("current")

tmnxRPPolicyObjectsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 18)
)
tmnxRPPolicyObjectsV5v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementDefaultAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementDefaultAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActInetNextHop"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObjectsV5v0Group.setStatus("obsolete")

tmnxRPInetPrefixListObjectsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 19)
)
tmnxRPInetPrefixListObjectsV5v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListThroughLen"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListBeginLen"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListThroughLen"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListBeginLen"))
)
if mibBuilder.loadTexts:
    tmnxRPInetPrefixListObjectsV5v0Group.setStatus("current")

tmnxRPPolicyObjectsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 20)
)
tmnxRPPolicyObjectsV7v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementDefaultAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementDefaultAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathPnd"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathPend"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObjectsV7v0Group.setStatus("obsolete")

tmnxRPPolicyEntryObjectsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 21)
)
tmnxRPPolicyEntryObjectsV7v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaCommunity"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaOspfRouteType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaArea"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaAreaConfigured"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIsisExternal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIgmpHostPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaGrpAddrPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaSrcAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaInterface"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaFamily"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaCommunity"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaOspfRouteType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaArea"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaAreaConfigured"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIsisExternal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIgmpHostPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaGrpAddrPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaSrcAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaInterface"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaFamily"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPend"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPend"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaMatchTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaMatchTag"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyEntryObjectsV7v0Group.setStatus("obsolete")

tmnxRPPolicyObsoleteV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 22)
)
tmnxRPPolicyObsoleteV7v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPrependAS"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObsoleteV7v0Group.setStatus("current")

tmnxRPPolicyObjectsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 25)
)
tmnxRPPolicyObjectsV8v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActMcRedirSvcId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActMcRedirIfIndex"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActMcRedirSvcId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActMcRedirIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObjectsV8v0Group.setStatus("current")

tmnxRPQPPBV9v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 26)
)
tmnxRPQPPBV9v0R4Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionFC"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionFCPriority"))
)
if mibBuilder.loadTexts:
    tmnxRPQPPBV9v0R4Group.setStatus("current")

tmnxRPPolicyEntryObjectsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 27)
)
tmnxRPPolicyEntryObjectsV9v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaCommunity"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaOspfRouteType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaArea"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaAreaConfigured"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIsisExternal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIgmpHostPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaGrpAddrPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaSrcAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaInterface"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaFamily"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaCommunity"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaOspfRouteType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaArea"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaAreaConfigured"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIsisExternal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIgmpHostPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaGrpAddrPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaSrcAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaInterface"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaFamily"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPend"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPend"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaMatchTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaMatchTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaState"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaState"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyEntryObjectsV9v0Group.setStatus("obsolete")

tmnxRPPolicyObjectsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 30)
)
tmnxRPPolicyObjectsV9v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActMcRedirSvcId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActMcRedirIfIndex"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActMcRedirSvcId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActMcRedirIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObjectsV9v0Group.setStatus("current")

tmnxRPPolicyObjectsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 31)
)
tmnxRPPolicyObjectsV10v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActnMetricSource"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionMetricSource"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActnMetricSource"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionMetricSource"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActionAigpMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActnAigpMetricVal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActionAigpMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActnAigpMetricVal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityExprString1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityExprString2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityExprString3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityExprString4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityExprRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityExprString1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityExprString2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityExprString3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityExprString4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityExprRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAigpMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActnAigpMetricVal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAigpMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActnAigpMetricVal"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObjectsV10v0Group.setStatus("current")

tmnxRPASPathGroupV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 32)
)
tmnxRPASPathGroupV10v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathGroupRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathGroupASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathGroupASPathRegEx"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathGroupRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathGroupASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathGroupASPathRegEx"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritASPathGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritASPathGroup"))
)
if mibBuilder.loadTexts:
    tmnxRPASPathGroupV10v0Group.setStatus("current")

tmnxRPPolicyEntryObjV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 33)
)
tmnxRPPolicyEntryObjV11v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPolicy"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPolicy"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCommExprRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCommExprString1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCommExprString2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCommExprString3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCommExprString4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCommExprRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCommExprString1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCommExprString2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCommExprString3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCommExprString4"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyEntryObjV11v0Group.setStatus("current")

tmnxRPAdminControlObjV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 34)
)
tmnxRPAdminControlObjV11v0Group.setObjects(
    ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminControlResetExclusive")
)
if mibBuilder.loadTexts:
    tmnxRPAdminControlObjV11v0Group.setStatus("current")

tmnxRPPolicyObjectsV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 35)
)
tmnxRPPolicyObjectsV11v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementDefaultAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementDefaultAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathPnd"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathPend"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPend"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPend"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm6"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm7"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm8"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm9"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm10"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm11"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm12"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm13"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm14"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm15"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm16"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm17"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm18"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm19"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm20"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm21"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm22"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm23"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm24"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm25"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm26"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm27"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAddComm28"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm6"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm7"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm8"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm9"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm10"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm11"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm12"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm13"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm14"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm15"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm16"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm17"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm18"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm19"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm20"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm21"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm22"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm23"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm24"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm25"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm26"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm27"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionRemoveComm28"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm6"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm7"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm8"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm9"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm10"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm11"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm12"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm13"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm14"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm15"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm16"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm17"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm18"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm19"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm20"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm21"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm22"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm23"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm24"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm25"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm26"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm27"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionReplaceComm28"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm6"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm7"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm8"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm9"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm10"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm11"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm12"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm13"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm14"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm15"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm16"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm17"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm18"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm19"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm20"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm21"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm22"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm23"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm24"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm25"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm26"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm27"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAddComm28"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm6"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm7"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm8"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm9"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm10"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm11"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm12"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm13"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm14"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm15"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm16"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm17"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm18"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm19"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm20"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm21"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm22"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm23"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm24"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm25"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm26"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm27"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionRemoveComm28"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm6"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm7"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm8"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm9"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm10"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm11"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm12"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm13"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm14"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm15"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm16"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm17"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm18"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm19"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm20"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm21"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm22"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm23"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm24"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm25"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm26"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm27"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionReplaceComm28"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm6"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm7"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm8"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm9"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm10"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm11"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm12"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm13"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm14"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm15"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm16"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm17"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm18"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm19"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm20"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm21"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm22"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm23"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm24"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm25"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm26"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm27"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddComm28"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm6"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm7"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm8"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm9"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm10"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm11"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm12"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm13"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm14"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm15"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm16"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm17"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm18"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm19"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm20"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm21"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm22"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm23"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm24"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm25"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm26"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm27"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionRemoveComm28"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm6"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm7"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm8"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm9"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm10"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm11"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm12"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm13"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm14"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm15"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm16"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm17"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm18"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm19"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm20"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm21"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm22"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm23"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm24"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm25"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm26"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm27"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionReplaceComm28"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm6"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm7"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm8"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm9"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm10"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm11"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm12"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm13"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm14"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm15"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm16"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm17"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm18"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm19"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm20"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm21"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm22"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm23"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm24"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm25"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm26"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm27"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddComm28"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm6"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm7"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm8"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm9"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm10"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm11"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm12"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm13"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm14"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm15"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm16"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm17"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm18"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm19"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm20"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm21"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm22"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm23"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm24"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm25"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm26"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm27"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionRemoveComm28"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm6"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm7"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm8"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm9"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm10"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm11"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm12"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm13"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm14"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm15"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm16"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm17"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm18"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm19"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm20"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm21"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm22"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm23"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm24"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm25"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm26"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm27"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionReplaceComm28"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObjectsV11v0Group.setStatus("current")

tmnxRPPolicyEntryObjsV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 36)
)
tmnxRPPolicyEntryObjsV11v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaCommunity"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaOspfRouteType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaArea"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaAreaConfigured"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIsisExternal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIgmpHostPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaGrpAddrPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaSrcAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaInterface"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaFamily"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaCommunity"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaOspfRouteType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaArea"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaAreaConfigured"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIsisExternal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIgmpHostPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaGrpAddrPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaSrcAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaInterface"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaFamily"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaMatchTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaMatchTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaState"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaState"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyEntryObjsV11v0Group.setStatus("current")

tmnxRPPolicyObsoleteV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 37)
)
tmnxRPPolicyObsoleteV11v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunityName2"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObsoleteV11v0Group.setStatus("current")

tmnxRPPolicyObjectsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 38)
)
tmnxRPPolicyObjectsV12v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActnSrcClassIndex"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActnDstClassIndex"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActnSrcClassIndex"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActnDstClassIndex"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActnSrcClassIndex"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActnDstClassIndex"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActnSrcClassIndex"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActnDstClassIndex"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityExprExactMatch"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityExprExactMatch"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritExtMvpnType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritExtMvpnType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcAddrPfxList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcAddrPfxList"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObjectsV12v0Group.setStatus("current")

tmnxRPPolicyVarObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 39)
)
tmnxRPPolicyVarObjectsGroup.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSPolicyVarRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSPolicyVarValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSPolicyVarRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSPolicyVarValue"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyVarObjectsGroup.setStatus("current")

tmnxRPOperPSAcceptActionFCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 40)
)
tmnxRPOperPSAcceptActionFCGroup.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionFC"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionFCPriority"))
)
if mibBuilder.loadTexts:
    tmnxRPOperPSAcceptActionFCGroup.setStatus("current")

tRPAdminPSAcceptOrigValidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 41)
)
tRPAdminPSAcceptOrigValidGroup.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActnOrigValidState"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActnOrigValidState"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActnOrigValidState"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActnOrigValidState"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritOrigValidState"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritOrigValidState"))
)
if mibBuilder.loadTexts:
    tRPAdminPSAcceptOrigValidGroup.setStatus("current")

tmnxRPCreationOriginGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 42)
)
tmnxRPCreationOriginGroup.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityCreationOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementCrOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsCreationOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritCreationOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAccActionAddCommCrOrig"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityCreationOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementCrOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsCreationOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritCreationOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAccActionAddCommCrOrig"))
)
if mibBuilder.loadTexts:
    tmnxRPCreationOriginGroup.setStatus("current")

tmnxRPStickyEcmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 43)
)
tmnxRPStickyEcmpGroup.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActStickyEcmp"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActStickyEcmp"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActStickyEcmp"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActStickyEcmp"))
)
if mibBuilder.loadTexts:
    tmnxRPStickyEcmpGroup.setStatus("current")

tmnxRPBgpLeakingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 50)
)
tmnxRPBgpLeakingGroup.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActBgpLeaking"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActBgpLeaking"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActBgpLeaking"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActBgpLeaking"))
)
if mibBuilder.loadTexts:
    tmnxRPBgpLeakingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxRoutePolicy7450V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 3)
)
tmnxRoutePolicy7450V4v0Compliance.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPAdminControlObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV4v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyEntryObjectsV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7450V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxRoutePolicy7750V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 4)
)
tmnxRoutePolicy7750V4v0Compliance.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPAdminControlObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPASPathObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPCommunityObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPDampingObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPrefixListObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV4v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyEntryObjectsV4v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPInetPrefixListObjectsGroup"))
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7750V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxRoutePolicy7450V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 5)
)
tmnxRoutePolicy7450V5v0Compliance.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPAdminControlObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyEntryObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7450V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxRoutePolicy7750V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 6)
)
tmnxRoutePolicy7750V5v0Compliance.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPAdminControlObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPASPathObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPCommunityObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPDampingObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPrefixListObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyEntryObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPInetPrefixListObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7750V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxRoutePolicy7450V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 7)
)
tmnxRoutePolicy7450V7v0Compliance.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPAdminControlObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV7v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyEntryObjectsV7v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV7v0Group"))
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7450V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxRoutePolicy7750V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 8)
)
tmnxRoutePolicy7750V7v0Compliance.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPAdminControlObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPASPathObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPCommunityObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPDampingObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPrefixListObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPInetPrefixListObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV7v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyEntryObjectsV7v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV7v0Group"))
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7750V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxRoutePolicy7450V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 9)
)
tmnxRoutePolicy7450V8v0Compliance.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPAdminControlObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV7v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV8v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyEntryObjectsV7v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV7v0Group"))
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7450V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxRoutePolicy7750V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 10)
)
tmnxRoutePolicy7750V8v0Compliance.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPAdminControlObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPASPathObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPCommunityObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPDampingObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPrefixListObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPInetPrefixListObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV7v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV8v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyEntryObjectsV7v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV7v0Group"))
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7750V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxRoutePolicy7450V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 11)
)
tmnxRoutePolicy7450V9v0Compliance.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPAdminControlObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV7v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV8v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV9v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyEntryObjectsV9v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV7v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPQPPBV9v0R4Group"))
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7450V9v0Compliance.setStatus(
        "obsolete"
    )

tmnxRoutePolicy7750V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 12)
)
tmnxRoutePolicy7750V9v0Compliance.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPAdminControlObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPASPathObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPCommunityObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPDampingObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPrefixListObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPInetPrefixListObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV7v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV8v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV9v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyEntryObjectsV9v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV7v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPQPPBV9v0R4Group"))
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7750V9v0Compliance.setStatus(
        "obsolete"
    )

tmnxRtPolicy7450V10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 13)
)
tmnxRtPolicy7450V10v0Compliance.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPAdminControlObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV7v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV8v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV9v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyEntryObjectsV9v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV7v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPQPPBV9v0R4Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV10v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPASPathGroupV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxRtPolicy7450V10v0Compliance.setStatus(
        "obsolete"
    )

tmnxRtPolicy7750V10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 14)
)
tmnxRtPolicy7750V10v0Compliance.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPAdminControlObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPASPathObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPCommunityObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPDampingObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPrefixListObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPInetPrefixListObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV7v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV8v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV9v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyEntryObjectsV9v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV7v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPQPPBV9v0R4Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV10v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPASPathGroupV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxRtPolicy7750V10v0Compliance.setStatus(
        "obsolete"
    )

tmnxRtPolicyV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 15)
)
tmnxRtPolicyV11v0Compliance.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPAdminControlObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPAdminControlObjV11v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPASPathObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPCommunityObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPDampingObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPrefixListObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPInetPrefixListObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV8v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV9v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV11v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyEntryObjsV11v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV7v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPQPPBV9v0R4Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV10v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPASPathGroupV10v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyEntryObjV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxRtPolicyV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxRtPolicyV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 16)
)
tmnxRtPolicyV12v0Compliance.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPAdminControlObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPAdminControlObjV11v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPASPathObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPCommunityObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPDampingObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPrefixListObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPInetPrefixListObjectsV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV5v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV8v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV9v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV11v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV12v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyVarObjectsGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyEntryObjsV11v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObsoleteV7v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPQPPBV9v0R4Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyObjectsV10v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPASPathGroupV10v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPPolicyEntryObjV11v0Group"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPOperPSAcceptActionFCGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptOrigValidGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPCreationOriginGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPStickyEcmpGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tmnxRPBgpLeakingGroup"))
)
if mibBuilder.loadTexts:
    tmnxRtPolicyV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-ROUTE-POLICY-MIB",
    **{"TASPathName": TASPathName,
       "TASPathGroupName": TASPathGroupName,
       "TCommunityName": TCommunityName,
       "TCommunityMember": TCommunityMember,
       "TCommunityMemberExpression": TCommunityMemberExpression,
       "TCommunityNameExpression": TCommunityNameExpression,
       "TDampingName": TDampingName,
       "TPrefixListName": TPrefixListName,
       "TPolicyStatementName": TPolicyStatementName,
       "PolicyStatementNameOrEmpty": PolicyStatementNameOrEmpty,
       "TRoutePolicyRegex": TRoutePolicyRegex,
       "TPolicyStatementEntryID": TPolicyStatementEntryID,
       "TRoutePolicyProtocol": TRoutePolicyProtocol,
       "TOspfRouteType": TOspfRouteType,
       "TIsisLevel": TIsisLevel,
       "TPolicyEntryAction": TPolicyEntryAction,
       "TPolicyEntryEdit": TPolicyEntryEdit,
       "TPolicyEntryCriteriaOrigin": TPolicyEntryCriteriaOrigin,
       "TPolicyActionTag": TPolicyActionTag,
       "TPolicyEntryCriteriaState": TPolicyEntryCriteriaState,
       "TPolicyActionMetricSource": TPolicyActionMetricSource,
       "TPolicyEntryAigpMetricEdit": TPolicyEntryAigpMetricEdit,
       "TPolicyEntryCriteriaMvpnType": TPolicyEntryCriteriaMvpnType,
       "TPolicyVariableName": TPolicyVariableName,
       "timetraRoutePolicyMIBModule": timetraRoutePolicyMIBModule,
       "tmnxRoutePolicyConformance": tmnxRoutePolicyConformance,
       "tmnxRoutePolicyCompliances": tmnxRoutePolicyCompliances,
       "tmnxRoutePolicy7450V4v0Compliance": tmnxRoutePolicy7450V4v0Compliance,
       "tmnxRoutePolicy7750V4v0Compliance": tmnxRoutePolicy7750V4v0Compliance,
       "tmnxRoutePolicy7450V5v0Compliance": tmnxRoutePolicy7450V5v0Compliance,
       "tmnxRoutePolicy7750V5v0Compliance": tmnxRoutePolicy7750V5v0Compliance,
       "tmnxRoutePolicy7450V7v0Compliance": tmnxRoutePolicy7450V7v0Compliance,
       "tmnxRoutePolicy7750V7v0Compliance": tmnxRoutePolicy7750V7v0Compliance,
       "tmnxRoutePolicy7450V8v0Compliance": tmnxRoutePolicy7450V8v0Compliance,
       "tmnxRoutePolicy7750V8v0Compliance": tmnxRoutePolicy7750V8v0Compliance,
       "tmnxRoutePolicy7450V9v0Compliance": tmnxRoutePolicy7450V9v0Compliance,
       "tmnxRoutePolicy7750V9v0Compliance": tmnxRoutePolicy7750V9v0Compliance,
       "tmnxRtPolicy7450V10v0Compliance": tmnxRtPolicy7450V10v0Compliance,
       "tmnxRtPolicy7750V10v0Compliance": tmnxRtPolicy7750V10v0Compliance,
       "tmnxRtPolicyV11v0Compliance": tmnxRtPolicyV11v0Compliance,
       "tmnxRtPolicyV12v0Compliance": tmnxRtPolicyV12v0Compliance,
       "tmnxRoutePolicyGroups": tmnxRoutePolicyGroups,
       "tmnxRPAdminControlObjectsGroup": tmnxRPAdminControlObjectsGroup,
       "tmnxRPASPathObjectsGroup": tmnxRPASPathObjectsGroup,
       "tmnxRPCommunityObjectsGroup": tmnxRPCommunityObjectsGroup,
       "tmnxRPDampingObjectsGroup": tmnxRPDampingObjectsGroup,
       "tmnxRPPrefixListObjectsGroup": tmnxRPPrefixListObjectsGroup,
       "tmnxRPPolicyObjectsV4v0Group": tmnxRPPolicyObjectsV4v0Group,
       "tmnxRPPolicyEntryObjectsV4v0Group": tmnxRPPolicyEntryObjectsV4v0Group,
       "tmnxRPInetPrefixListObjectsGroup": tmnxRPInetPrefixListObjectsGroup,
       "tmnxRPPolicyEntryObjectsV5v0Group": tmnxRPPolicyEntryObjectsV5v0Group,
       "tmnxRPPolicyObsoleteV5v0Group": tmnxRPPolicyObsoleteV5v0Group,
       "tmnxRPASPathObjectsV5v0Group": tmnxRPASPathObjectsV5v0Group,
       "tmnxRPCommunityObjectsV5v0Group": tmnxRPCommunityObjectsV5v0Group,
       "tmnxRPDampingObjectsV5v0Group": tmnxRPDampingObjectsV5v0Group,
       "tmnxRPPrefixListObjectsV5v0Group": tmnxRPPrefixListObjectsV5v0Group,
       "tmnxRPPolicyObjectsV5v0Group": tmnxRPPolicyObjectsV5v0Group,
       "tmnxRPInetPrefixListObjectsV5v0Group": tmnxRPInetPrefixListObjectsV5v0Group,
       "tmnxRPPolicyObjectsV7v0Group": tmnxRPPolicyObjectsV7v0Group,
       "tmnxRPPolicyEntryObjectsV7v0Group": tmnxRPPolicyEntryObjectsV7v0Group,
       "tmnxRPPolicyObsoleteV7v0Group": tmnxRPPolicyObsoleteV7v0Group,
       "tmnxRPPolicyObjectsV8v0Group": tmnxRPPolicyObjectsV8v0Group,
       "tmnxRPQPPBV9v0R4Group": tmnxRPQPPBV9v0R4Group,
       "tmnxRPPolicyEntryObjectsV9v0Group": tmnxRPPolicyEntryObjectsV9v0Group,
       "tmnxRPPolicyObjectsV9v0Group": tmnxRPPolicyObjectsV9v0Group,
       "tmnxRPPolicyObjectsV10v0Group": tmnxRPPolicyObjectsV10v0Group,
       "tmnxRPASPathGroupV10v0Group": tmnxRPASPathGroupV10v0Group,
       "tmnxRPPolicyEntryObjV11v0Group": tmnxRPPolicyEntryObjV11v0Group,
       "tmnxRPAdminControlObjV11v0Group": tmnxRPAdminControlObjV11v0Group,
       "tmnxRPPolicyObjectsV11v0Group": tmnxRPPolicyObjectsV11v0Group,
       "tmnxRPPolicyEntryObjsV11v0Group": tmnxRPPolicyEntryObjsV11v0Group,
       "tmnxRPPolicyObsoleteV11v0Group": tmnxRPPolicyObsoleteV11v0Group,
       "tmnxRPPolicyObjectsV12v0Group": tmnxRPPolicyObjectsV12v0Group,
       "tmnxRPPolicyVarObjectsGroup": tmnxRPPolicyVarObjectsGroup,
       "tmnxRPOperPSAcceptActionFCGroup": tmnxRPOperPSAcceptActionFCGroup,
       "tRPAdminPSAcceptOrigValidGroup": tRPAdminPSAcceptOrigValidGroup,
       "tmnxRPCreationOriginGroup": tmnxRPCreationOriginGroup,
       "tmnxRPStickyEcmpGroup": tmnxRPStickyEcmpGroup,
       "tmnxRPBgpLeakingGroup": tmnxRPBgpLeakingGroup,
       "tRoutePolicyObjects": tRoutePolicyObjects,
       "tRPOperObjects": tRPOperObjects,
       "tRPOperValueObjects": tRPOperValueObjects,
       "tRPOperASPathTableLastChanged": tRPOperASPathTableLastChanged,
       "tRPOperASPathTable": tRPOperASPathTable,
       "tRPOperASPathEntry": tRPOperASPathEntry,
       "tRPOperASPathName": tRPOperASPathName,
       "tRPOperASPathRowStatus": tRPOperASPathRowStatus,
       "tRPOperASPathRegEx": tRPOperASPathRegEx,
       "tRPOperASPathEntryLastChanged": tRPOperASPathEntryLastChanged,
       "tRPOperCommunityTableLastChanged": tRPOperCommunityTableLastChanged,
       "tRPOperCommunityTable": tRPOperCommunityTable,
       "tRPOperCommunityEntry": tRPOperCommunityEntry,
       "tRPOperCommunityName": tRPOperCommunityName,
       "tRPOperCommunityMember": tRPOperCommunityMember,
       "tRPOperCommunityRowStatus": tRPOperCommunityRowStatus,
       "tRPOperCommunityEntryLastChanged": tRPOperCommunityEntryLastChanged,
       "tRPOperCommunityCreationOrigin": tRPOperCommunityCreationOrigin,
       "tRPOperDampingTableLastChanged": tRPOperDampingTableLastChanged,
       "tRPOperDampingTable": tRPOperDampingTable,
       "tRPOperDampingEntry": tRPOperDampingEntry,
       "tRPOperDampingName": tRPOperDampingName,
       "tRPOperDampingRowStatus": tRPOperDampingRowStatus,
       "tRPOperDampingHalfLife": tRPOperDampingHalfLife,
       "tRPOperDampingMaxSuppress": tRPOperDampingMaxSuppress,
       "tRPOperDampingReuse": tRPOperDampingReuse,
       "tRPOperDampingSuppress": tRPOperDampingSuppress,
       "tRPOperDampingEntryLastChanged": tRPOperDampingEntryLastChanged,
       "tRPOperPrefixListTableLastChanged": tRPOperPrefixListTableLastChanged,
       "tRPOperPrefixListTable": tRPOperPrefixListTable,
       "tRPOperPrefixListEntry": tRPOperPrefixListEntry,
       "tRPOperPrefixListName": tRPOperPrefixListName,
       "tRPOperPrefixListIpPrefix": tRPOperPrefixListIpPrefix,
       "tRPOperPrefixListMask": tRPOperPrefixListMask,
       "tRPOperPrefixListRowStatus": tRPOperPrefixListRowStatus,
       "tRPOperPrefixListType": tRPOperPrefixListType,
       "tRPOperPrefixListThroughLength": tRPOperPrefixListThroughLength,
       "tRPOperPrefixListEntryLastChanged": tRPOperPrefixListEntryLastChanged,
       "tRPOperPrefixListBeginLength": tRPOperPrefixListBeginLength,
       "tRPOperPolicyStatementTableLastChanged": tRPOperPolicyStatementTableLastChanged,
       "tRPOperPolicyStatementTable": tRPOperPolicyStatementTable,
       "tRPOperPolicyStatementEntry": tRPOperPolicyStatementEntry,
       "tRPOperPolicyStatementName": tRPOperPolicyStatementName,
       "tRPOperPolicyStatementRowStatus": tRPOperPolicyStatementRowStatus,
       "tRPOperPolicyStatementDescription": tRPOperPolicyStatementDescription,
       "tRPOperPolicyStatementDefaultAction": tRPOperPolicyStatementDefaultAction,
       "tRPOperPolicyStatementEntryLastChanged": tRPOperPolicyStatementEntryLastChanged,
       "tRPOperPolicyStatementCrOrigin": tRPOperPolicyStatementCrOrigin,
       "tRPOperPSDefaultActionParamsTableLastChanged": tRPOperPSDefaultActionParamsTableLastChanged,
       "tRPOperPSDefaultActionParamsTable": tRPOperPSDefaultActionParamsTable,
       "tRPOperPSDefaultActionParamsEntry": tRPOperPSDefaultActionParamsEntry,
       "tRPOperPSDefaultActionASPath": tRPOperPSDefaultActionASPath,
       "tRPOperPSDefaultActionASPathName": tRPOperPSDefaultActionASPathName,
       "tRPOperPSDefaultActionASPathPrependAS": tRPOperPSDefaultActionASPathPrependAS,
       "tRPOperPSDefaultActionASPathPrependCount": tRPOperPSDefaultActionASPathPrependCount,
       "tRPOperPSDefaultActionCommunity1": tRPOperPSDefaultActionCommunity1,
       "tRPOperPSDefaultActionCommunityName1": tRPOperPSDefaultActionCommunityName1,
       "tRPOperPSDefaultActionCommunity2": tRPOperPSDefaultActionCommunity2,
       "tRPOperPSDefaultActionCommunityName2": tRPOperPSDefaultActionCommunityName2,
       "tRPOperPSDefaultActionOrigin": tRPOperPSDefaultActionOrigin,
       "tRPOperPSDefaultActionLocalPreferenceSet": tRPOperPSDefaultActionLocalPreferenceSet,
       "tRPOperPSDefaultActionLocalPreference": tRPOperPSDefaultActionLocalPreference,
       "tRPOperPSDefaultActionMetric": tRPOperPSDefaultActionMetric,
       "tRPOperPSDefaultActionMetricValue": tRPOperPSDefaultActionMetricValue,
       "tRPOperPSDefaultActionPreference": tRPOperPSDefaultActionPreference,
       "tRPOperPSDefaultActionDamping": tRPOperPSDefaultActionDamping,
       "tRPOperPSDefaultActionNextHopSelf": tRPOperPSDefaultActionNextHopSelf,
       "tRPOperPSDefaultActionNextHop": tRPOperPSDefaultActionNextHop,
       "tRPOperPSDefaultActionTag": tRPOperPSDefaultActionTag,
       "tRPOperPSDefaultActionOspfType": tRPOperPSDefaultActionOspfType,
       "tRPOperPSDefaultActionParamsEntryLastChanged": tRPOperPSDefaultActionParamsEntryLastChanged,
       "tRPOperPSDefActInetNextHopType": tRPOperPSDefActInetNextHopType,
       "tRPOperPSDefActInetNextHop": tRPOperPSDefActInetNextHop,
       "tRPOperPSDefaultActionASPathPend": tRPOperPSDefaultActionASPathPend,
       "tRPOperPSDefActMcRedirSvcId": tRPOperPSDefActMcRedirSvcId,
       "tRPOperPSDefActMcRedirIfIndex": tRPOperPSDefActMcRedirIfIndex,
       "tRPOperPSDefActionMetricSource": tRPOperPSDefActionMetricSource,
       "tRPOperPSDefActionAigpMetric": tRPOperPSDefActionAigpMetric,
       "tRPOperPSDefActnAigpMetricVal": tRPOperPSDefActnAigpMetricVal,
       "tRPOperPSDefActnSrcClassIndex": tRPOperPSDefActnSrcClassIndex,
       "tRPOperPSDefActnDstClassIndex": tRPOperPSDefActnDstClassIndex,
       "tRPOperPSDefActnOrigValidState": tRPOperPSDefActnOrigValidState,
       "tRPOperPSParamsTableLastChanged": tRPOperPSParamsTableLastChanged,
       "tRPOperPSParamsTable": tRPOperPSParamsTable,
       "tRPOperPSParamsEntry": tRPOperPSParamsEntry,
       "tRPOperPSNameEntryIndex": tRPOperPSNameEntryIndex,
       "tRPOperPSParamsRowStatus": tRPOperPSParamsRowStatus,
       "tRPOperPSParamsDescription": tRPOperPSParamsDescription,
       "tRPOperPSParamsAction": tRPOperPSParamsAction,
       "tRPOperPSParamsEntryLastChanged": tRPOperPSParamsEntryLastChanged,
       "tRPOperPSParamsCreationOrigin": tRPOperPSParamsCreationOrigin,
       "tRPOperPSAcceptActionParamsTableLastChanged": tRPOperPSAcceptActionParamsTableLastChanged,
       "tRPOperPSAcceptActionParamsTable": tRPOperPSAcceptActionParamsTable,
       "tRPOperPSAcceptActionParamsEntry": tRPOperPSAcceptActionParamsEntry,
       "tRPOperPSAcceptActionASPath": tRPOperPSAcceptActionASPath,
       "tRPOperPSAcceptActionASPathName": tRPOperPSAcceptActionASPathName,
       "tRPOperPSAcceptActionASPathPrependAS": tRPOperPSAcceptActionASPathPrependAS,
       "tRPOperPSAcceptActionASPathPrependCount": tRPOperPSAcceptActionASPathPrependCount,
       "tRPOperPSAcceptActionCommunity1": tRPOperPSAcceptActionCommunity1,
       "tRPOperPSAcceptActionCommunityName1": tRPOperPSAcceptActionCommunityName1,
       "tRPOperPSAcceptActionCommunity2": tRPOperPSAcceptActionCommunity2,
       "tRPOperPSAcceptActionCommunityName2": tRPOperPSAcceptActionCommunityName2,
       "tRPOperPSAcceptActionOrigin": tRPOperPSAcceptActionOrigin,
       "tRPOperPSAcceptActionLocalPreferenceSet": tRPOperPSAcceptActionLocalPreferenceSet,
       "tRPOperPSAcceptActionLocalPreference": tRPOperPSAcceptActionLocalPreference,
       "tRPOperPSAcceptActionMetric": tRPOperPSAcceptActionMetric,
       "tRPOperPSAcceptActionMetricValue": tRPOperPSAcceptActionMetricValue,
       "tRPOperPSAcceptActionPreference": tRPOperPSAcceptActionPreference,
       "tRPOperPSAcceptActionDamping": tRPOperPSAcceptActionDamping,
       "tRPOperPSAcceptActionNextHopSelf": tRPOperPSAcceptActionNextHopSelf,
       "tRPOperPSAcceptActionNextHop": tRPOperPSAcceptActionNextHop,
       "tRPOperPSAcceptActionTag": tRPOperPSAcceptActionTag,
       "tRPOperPSAcceptActionOspfType": tRPOperPSAcceptActionOspfType,
       "tRPOperPSAcceptActionParamsEntryLastChanged": tRPOperPSAcceptActionParamsEntryLastChanged,
       "tRPOperPSAcptActInetNextHopType": tRPOperPSAcptActInetNextHopType,
       "tRPOperPSAcptActInetNextHop": tRPOperPSAcptActInetNextHop,
       "tRPOperPSAcceptActionASPathPend": tRPOperPSAcceptActionASPathPend,
       "tRPOperPSAcceptActionFC": tRPOperPSAcceptActionFC,
       "tRPOperPSAcceptActionFCPriority": tRPOperPSAcceptActionFCPriority,
       "tRPOperPSAcptActMcRedirSvcId": tRPOperPSAcptActMcRedirSvcId,
       "tRPOperPSAcptActMcRedirIfIndex": tRPOperPSAcptActMcRedirIfIndex,
       "tRPOperPSAcptActnMetricSource": tRPOperPSAcptActnMetricSource,
       "tRPOperPSAcptActionAigpMetric": tRPOperPSAcptActionAigpMetric,
       "tRPOperPSAcptActnAigpMetricVal": tRPOperPSAcptActnAigpMetricVal,
       "tRPOperPSAcptActnSrcClassIndex": tRPOperPSAcptActnSrcClassIndex,
       "tRPOperPSAcptActnDstClassIndex": tRPOperPSAcptActnDstClassIndex,
       "tRPOperPSAcptActnOrigValidState": tRPOperPSAcptActnOrigValidState,
       "tRPOperPSToCriteriaTableLastChanged": tRPOperPSToCriteriaTableLastChanged,
       "tRPOperPSToCriteriaTable": tRPOperPSToCriteriaTable,
       "tRPOperPSToCriteriaEntry": tRPOperPSToCriteriaEntry,
       "tRPOperPSToCriteriaIndex": tRPOperPSToCriteriaIndex,
       "tRPOperPSToCriteriaRowStatus": tRPOperPSToCriteriaRowStatus,
       "tRPOperPSToCriteriaProtocol": tRPOperPSToCriteriaProtocol,
       "tRPOperPSToCriteriaNeighborIpAddr": tRPOperPSToCriteriaNeighborIpAddr,
       "tRPOperPSToCriteriaNeighborPrefixList": tRPOperPSToCriteriaNeighborPrefixList,
       "tRPOperPSToCriteriaEntryLastChanged": tRPOperPSToCriteriaEntryLastChanged,
       "tRPOperPSToCriteriaIsisLevel": tRPOperPSToCriteriaIsisLevel,
       "tRPOperPSToCriteriaPrefixList1": tRPOperPSToCriteriaPrefixList1,
       "tRPOperPSToCriteriaPrefixList2": tRPOperPSToCriteriaPrefixList2,
       "tRPOperPSToCriteriaPrefixList3": tRPOperPSToCriteriaPrefixList3,
       "tRPOperPSToCriteriaPrefixList4": tRPOperPSToCriteriaPrefixList4,
       "tRPOperPSToCriteriaPrefixList5": tRPOperPSToCriteriaPrefixList5,
       "tRPOperPSToCritNbrInetAddrType": tRPOperPSToCritNbrInetAddrType,
       "tRPOperPSToCritNbrInetAddr": tRPOperPSToCritNbrInetAddr,
       "tRPOperPSToCriteriaInstanceId": tRPOperPSToCriteriaInstanceId,
       "tRPOperPSFromCriteriaTableLastChanged": tRPOperPSFromCriteriaTableLastChanged,
       "tRPOperPSFromCriteriaTable": tRPOperPSFromCriteriaTable,
       "tRPOperPSFromCriteriaEntry": tRPOperPSFromCriteriaEntry,
       "tRPOperPSFromCriteriaIndex": tRPOperPSFromCriteriaIndex,
       "tRPOperPSFromCriteriaRowStatus": tRPOperPSFromCriteriaRowStatus,
       "tRPOperPSFromCriteriaProtocol": tRPOperPSFromCriteriaProtocol,
       "tRPOperPSFromCriteriaNeighborIpAddr": tRPOperPSFromCriteriaNeighborIpAddr,
       "tRPOperPSFromCriteriaNeighborPrefixList": tRPOperPSFromCriteriaNeighborPrefixList,
       "tRPOperPSFromCriteriaPrefixList1": tRPOperPSFromCriteriaPrefixList1,
       "tRPOperPSFromCriteriaPrefixList2": tRPOperPSFromCriteriaPrefixList2,
       "tRPOperPSFromCriteriaPrefixList3": tRPOperPSFromCriteriaPrefixList3,
       "tRPOperPSFromCriteriaPrefixList4": tRPOperPSFromCriteriaPrefixList4,
       "tRPOperPSFromCriteriaPrefixList5": tRPOperPSFromCriteriaPrefixList5,
       "tRPOperPSFromCriteriaASPath": tRPOperPSFromCriteriaASPath,
       "tRPOperPSFromCriteriaCommunity": tRPOperPSFromCriteriaCommunity,
       "tRPOperPSFromCriteriaOrigin": tRPOperPSFromCriteriaOrigin,
       "tRPOperPSFromCriteriaOspfRouteType": tRPOperPSFromCriteriaOspfRouteType,
       "tRPOperPSFromCriteriaEntryLastChanged": tRPOperPSFromCriteriaEntryLastChanged,
       "tRPOperPSFromCriteriaArea": tRPOperPSFromCriteriaArea,
       "tRPOperPSFromCriteriaAreaConfigured": tRPOperPSFromCriteriaAreaConfigured,
       "tRPOperPSFromCriteriaIsisLevel": tRPOperPSFromCriteriaIsisLevel,
       "tRPOperPSFromCriteriaIsisExternal": tRPOperPSFromCriteriaIsisExternal,
       "tRPOperPSFromCriteriaIgmpHostPrefixList": tRPOperPSFromCriteriaIgmpHostPrefixList,
       "tRPOperPSFromCriteriaGrpAddrPrefixList": tRPOperPSFromCriteriaGrpAddrPrefixList,
       "tRPOperPSFromCriteriaSrcAddr": tRPOperPSFromCriteriaSrcAddr,
       "tRPOperPSFromCriteriaInterface": tRPOperPSFromCriteriaInterface,
       "tRPOperPSFromCriteriaTag": tRPOperPSFromCriteriaTag,
       "tRPOperPSFromCritNbrInetAddrType": tRPOperPSFromCritNbrInetAddrType,
       "tRPOperPSFromCritNbrInetAddr": tRPOperPSFromCritNbrInetAddr,
       "tRPOperPSFromCritSrcInetAddrType": tRPOperPSFromCritSrcInetAddrType,
       "tRPOperPSFromCritSrcInetAddr": tRPOperPSFromCritSrcInetAddr,
       "tRPOperPSFromCriteriaFamily": tRPOperPSFromCriteriaFamily,
       "tRPOperPSFromCriteriaInstanceId": tRPOperPSFromCriteriaInstanceId,
       "tRPOperPSFromCriteriaMatchTag": tRPOperPSFromCriteriaMatchTag,
       "tRPOperPSFromCriteriaState": tRPOperPSFromCriteriaState,
       "tRPOperPSFromCritASPathGroup": tRPOperPSFromCritASPathGroup,
       "tRPOperPSFromCriteriaPolicy": tRPOperPSFromCriteriaPolicy,
       "tRPOperPSFromCritCreationOrigin": tRPOperPSFromCritCreationOrigin,
       "tRPOperInetPrefixListTblLastChg": tRPOperInetPrefixListTblLastChg,
       "tRPOperInetPrefixListTable": tRPOperInetPrefixListTable,
       "tRPOperInetPrefixListEntry": tRPOperInetPrefixListEntry,
       "tRPOperInetPrefixListName": tRPOperInetPrefixListName,
       "tRPOperInetPrefixListPrefixType": tRPOperInetPrefixListPrefixType,
       "tRPOperInetPrefixListPrefix": tRPOperInetPrefixListPrefix,
       "tRPOperInetPrefixListPrefixLen": tRPOperInetPrefixListPrefixLen,
       "tRPOperInetPrefixListType": tRPOperInetPrefixListType,
       "tRPOperInetPrefixListRowStatus": tRPOperInetPrefixListRowStatus,
       "tRPOperInetPrefixListThroughLen": tRPOperInetPrefixListThroughLen,
       "tRPOperInetPrefixListLastChg": tRPOperInetPrefixListLastChg,
       "tRPOperInetPrefixListBeginLen": tRPOperInetPrefixListBeginLen,
       "tRPOperCommunityExprTable": tRPOperCommunityExprTable,
       "tRPOperCommunityExprEntry": tRPOperCommunityExprEntry,
       "tRPOperCommunityExprName": tRPOperCommunityExprName,
       "tRPOperCommunityExprRowStatus": tRPOperCommunityExprRowStatus,
       "tRPOperCommunityExprString1": tRPOperCommunityExprString1,
       "tRPOperCommunityExprString2": tRPOperCommunityExprString2,
       "tRPOperCommunityExprString3": tRPOperCommunityExprString3,
       "tRPOperCommunityExprString4": tRPOperCommunityExprString4,
       "tRPOperCommunityExprExactMatch": tRPOperCommunityExprExactMatch,
       "tRPOperASPathGroupTable": tRPOperASPathGroupTable,
       "tRPOperASPathGroupEntry": tRPOperASPathGroupEntry,
       "tRPOperASPathGroupName": tRPOperASPathGroupName,
       "tRPOperASPathGroupEntryIndex": tRPOperASPathGroupEntryIndex,
       "tRPOperASPathGroupRowStatus": tRPOperASPathGroupRowStatus,
       "tRPOperASPathGroupASPathName": tRPOperASPathGroupASPathName,
       "tRPOperASPathGroupASPathRegEx": tRPOperASPathGroupASPathRegEx,
       "tRPOperPSFromCommExprTable": tRPOperPSFromCommExprTable,
       "tRPOperPSFromCommExprEntry": tRPOperPSFromCommExprEntry,
       "tRPOperPSFromCommExprRowStatus": tRPOperPSFromCommExprRowStatus,
       "tRPOperPSFromCommExprString1": tRPOperPSFromCommExprString1,
       "tRPOperPSFromCommExprString2": tRPOperPSFromCommExprString2,
       "tRPOperPSFromCommExprString3": tRPOperPSFromCommExprString3,
       "tRPOperPSFromCommExprString4": tRPOperPSFromCommExprString4,
       "tRPOperPSDefActionAddCommTable": tRPOperPSDefActionAddCommTable,
       "tRPOperPSDefActionAddCommEntry": tRPOperPSDefActionAddCommEntry,
       "tRPOperPSDefActionAddComm1": tRPOperPSDefActionAddComm1,
       "tRPOperPSDefActionAddComm2": tRPOperPSDefActionAddComm2,
       "tRPOperPSDefActionAddComm3": tRPOperPSDefActionAddComm3,
       "tRPOperPSDefActionAddComm4": tRPOperPSDefActionAddComm4,
       "tRPOperPSDefActionAddComm5": tRPOperPSDefActionAddComm5,
       "tRPOperPSDefActionAddComm6": tRPOperPSDefActionAddComm6,
       "tRPOperPSDefActionAddComm7": tRPOperPSDefActionAddComm7,
       "tRPOperPSDefActionAddComm8": tRPOperPSDefActionAddComm8,
       "tRPOperPSDefActionAddComm9": tRPOperPSDefActionAddComm9,
       "tRPOperPSDefActionAddComm10": tRPOperPSDefActionAddComm10,
       "tRPOperPSDefActionAddComm11": tRPOperPSDefActionAddComm11,
       "tRPOperPSDefActionAddComm12": tRPOperPSDefActionAddComm12,
       "tRPOperPSDefActionAddComm13": tRPOperPSDefActionAddComm13,
       "tRPOperPSDefActionAddComm14": tRPOperPSDefActionAddComm14,
       "tRPOperPSDefActionAddComm15": tRPOperPSDefActionAddComm15,
       "tRPOperPSDefActionAddComm16": tRPOperPSDefActionAddComm16,
       "tRPOperPSDefActionAddComm17": tRPOperPSDefActionAddComm17,
       "tRPOperPSDefActionAddComm18": tRPOperPSDefActionAddComm18,
       "tRPOperPSDefActionAddComm19": tRPOperPSDefActionAddComm19,
       "tRPOperPSDefActionAddComm20": tRPOperPSDefActionAddComm20,
       "tRPOperPSDefActionAddComm21": tRPOperPSDefActionAddComm21,
       "tRPOperPSDefActionAddComm22": tRPOperPSDefActionAddComm22,
       "tRPOperPSDefActionAddComm23": tRPOperPSDefActionAddComm23,
       "tRPOperPSDefActionAddComm24": tRPOperPSDefActionAddComm24,
       "tRPOperPSDefActionAddComm25": tRPOperPSDefActionAddComm25,
       "tRPOperPSDefActionAddComm26": tRPOperPSDefActionAddComm26,
       "tRPOperPSDefActionAddComm27": tRPOperPSDefActionAddComm27,
       "tRPOperPSDefActionAddComm28": tRPOperPSDefActionAddComm28,
       "tRPOperPSDefActionRemCommTable": tRPOperPSDefActionRemCommTable,
       "tRPOperPSDefActionRemCommEntry": tRPOperPSDefActionRemCommEntry,
       "tRPOperPSDefActionRemoveComm1": tRPOperPSDefActionRemoveComm1,
       "tRPOperPSDefActionRemoveComm2": tRPOperPSDefActionRemoveComm2,
       "tRPOperPSDefActionRemoveComm3": tRPOperPSDefActionRemoveComm3,
       "tRPOperPSDefActionRemoveComm4": tRPOperPSDefActionRemoveComm4,
       "tRPOperPSDefActionRemoveComm5": tRPOperPSDefActionRemoveComm5,
       "tRPOperPSDefActionRemoveComm6": tRPOperPSDefActionRemoveComm6,
       "tRPOperPSDefActionRemoveComm7": tRPOperPSDefActionRemoveComm7,
       "tRPOperPSDefActionRemoveComm8": tRPOperPSDefActionRemoveComm8,
       "tRPOperPSDefActionRemoveComm9": tRPOperPSDefActionRemoveComm9,
       "tRPOperPSDefActionRemoveComm10": tRPOperPSDefActionRemoveComm10,
       "tRPOperPSDefActionRemoveComm11": tRPOperPSDefActionRemoveComm11,
       "tRPOperPSDefActionRemoveComm12": tRPOperPSDefActionRemoveComm12,
       "tRPOperPSDefActionRemoveComm13": tRPOperPSDefActionRemoveComm13,
       "tRPOperPSDefActionRemoveComm14": tRPOperPSDefActionRemoveComm14,
       "tRPOperPSDefActionRemoveComm15": tRPOperPSDefActionRemoveComm15,
       "tRPOperPSDefActionRemoveComm16": tRPOperPSDefActionRemoveComm16,
       "tRPOperPSDefActionRemoveComm17": tRPOperPSDefActionRemoveComm17,
       "tRPOperPSDefActionRemoveComm18": tRPOperPSDefActionRemoveComm18,
       "tRPOperPSDefActionRemoveComm19": tRPOperPSDefActionRemoveComm19,
       "tRPOperPSDefActionRemoveComm20": tRPOperPSDefActionRemoveComm20,
       "tRPOperPSDefActionRemoveComm21": tRPOperPSDefActionRemoveComm21,
       "tRPOperPSDefActionRemoveComm22": tRPOperPSDefActionRemoveComm22,
       "tRPOperPSDefActionRemoveComm23": tRPOperPSDefActionRemoveComm23,
       "tRPOperPSDefActionRemoveComm24": tRPOperPSDefActionRemoveComm24,
       "tRPOperPSDefActionRemoveComm25": tRPOperPSDefActionRemoveComm25,
       "tRPOperPSDefActionRemoveComm26": tRPOperPSDefActionRemoveComm26,
       "tRPOperPSDefActionRemoveComm27": tRPOperPSDefActionRemoveComm27,
       "tRPOperPSDefActionRemoveComm28": tRPOperPSDefActionRemoveComm28,
       "tRPOperPSDefActionRepCommTable": tRPOperPSDefActionRepCommTable,
       "tRPOperPSDefActionRepCommEntry": tRPOperPSDefActionRepCommEntry,
       "tRPOperPSDefActionReplaceComm1": tRPOperPSDefActionReplaceComm1,
       "tRPOperPSDefActionReplaceComm2": tRPOperPSDefActionReplaceComm2,
       "tRPOperPSDefActionReplaceComm3": tRPOperPSDefActionReplaceComm3,
       "tRPOperPSDefActionReplaceComm4": tRPOperPSDefActionReplaceComm4,
       "tRPOperPSDefActionReplaceComm5": tRPOperPSDefActionReplaceComm5,
       "tRPOperPSDefActionReplaceComm6": tRPOperPSDefActionReplaceComm6,
       "tRPOperPSDefActionReplaceComm7": tRPOperPSDefActionReplaceComm7,
       "tRPOperPSDefActionReplaceComm8": tRPOperPSDefActionReplaceComm8,
       "tRPOperPSDefActionReplaceComm9": tRPOperPSDefActionReplaceComm9,
       "tRPOperPSDefActionReplaceComm10": tRPOperPSDefActionReplaceComm10,
       "tRPOperPSDefActionReplaceComm11": tRPOperPSDefActionReplaceComm11,
       "tRPOperPSDefActionReplaceComm12": tRPOperPSDefActionReplaceComm12,
       "tRPOperPSDefActionReplaceComm13": tRPOperPSDefActionReplaceComm13,
       "tRPOperPSDefActionReplaceComm14": tRPOperPSDefActionReplaceComm14,
       "tRPOperPSDefActionReplaceComm15": tRPOperPSDefActionReplaceComm15,
       "tRPOperPSDefActionReplaceComm16": tRPOperPSDefActionReplaceComm16,
       "tRPOperPSDefActionReplaceComm17": tRPOperPSDefActionReplaceComm17,
       "tRPOperPSDefActionReplaceComm18": tRPOperPSDefActionReplaceComm18,
       "tRPOperPSDefActionReplaceComm19": tRPOperPSDefActionReplaceComm19,
       "tRPOperPSDefActionReplaceComm20": tRPOperPSDefActionReplaceComm20,
       "tRPOperPSDefActionReplaceComm21": tRPOperPSDefActionReplaceComm21,
       "tRPOperPSDefActionReplaceComm22": tRPOperPSDefActionReplaceComm22,
       "tRPOperPSDefActionReplaceComm23": tRPOperPSDefActionReplaceComm23,
       "tRPOperPSDefActionReplaceComm24": tRPOperPSDefActionReplaceComm24,
       "tRPOperPSDefActionReplaceComm25": tRPOperPSDefActionReplaceComm25,
       "tRPOperPSDefActionReplaceComm26": tRPOperPSDefActionReplaceComm26,
       "tRPOperPSDefActionReplaceComm27": tRPOperPSDefActionReplaceComm27,
       "tRPOperPSDefActionReplaceComm28": tRPOperPSDefActionReplaceComm28,
       "tRPOperPSAccActionAddCommTable": tRPOperPSAccActionAddCommTable,
       "tRPOperPSAccActionAddCommEntry": tRPOperPSAccActionAddCommEntry,
       "tRPOperPSAccActionAddComm1": tRPOperPSAccActionAddComm1,
       "tRPOperPSAccActionAddComm2": tRPOperPSAccActionAddComm2,
       "tRPOperPSAccActionAddComm3": tRPOperPSAccActionAddComm3,
       "tRPOperPSAccActionAddComm4": tRPOperPSAccActionAddComm4,
       "tRPOperPSAccActionAddComm5": tRPOperPSAccActionAddComm5,
       "tRPOperPSAccActionAddComm6": tRPOperPSAccActionAddComm6,
       "tRPOperPSAccActionAddComm7": tRPOperPSAccActionAddComm7,
       "tRPOperPSAccActionAddComm8": tRPOperPSAccActionAddComm8,
       "tRPOperPSAccActionAddComm9": tRPOperPSAccActionAddComm9,
       "tRPOperPSAccActionAddComm10": tRPOperPSAccActionAddComm10,
       "tRPOperPSAccActionAddComm11": tRPOperPSAccActionAddComm11,
       "tRPOperPSAccActionAddComm12": tRPOperPSAccActionAddComm12,
       "tRPOperPSAccActionAddComm13": tRPOperPSAccActionAddComm13,
       "tRPOperPSAccActionAddComm14": tRPOperPSAccActionAddComm14,
       "tRPOperPSAccActionAddComm15": tRPOperPSAccActionAddComm15,
       "tRPOperPSAccActionAddComm16": tRPOperPSAccActionAddComm16,
       "tRPOperPSAccActionAddComm17": tRPOperPSAccActionAddComm17,
       "tRPOperPSAccActionAddComm18": tRPOperPSAccActionAddComm18,
       "tRPOperPSAccActionAddComm19": tRPOperPSAccActionAddComm19,
       "tRPOperPSAccActionAddComm20": tRPOperPSAccActionAddComm20,
       "tRPOperPSAccActionAddComm21": tRPOperPSAccActionAddComm21,
       "tRPOperPSAccActionAddComm22": tRPOperPSAccActionAddComm22,
       "tRPOperPSAccActionAddComm23": tRPOperPSAccActionAddComm23,
       "tRPOperPSAccActionAddComm24": tRPOperPSAccActionAddComm24,
       "tRPOperPSAccActionAddComm25": tRPOperPSAccActionAddComm25,
       "tRPOperPSAccActionAddComm26": tRPOperPSAccActionAddComm26,
       "tRPOperPSAccActionAddComm27": tRPOperPSAccActionAddComm27,
       "tRPOperPSAccActionAddComm28": tRPOperPSAccActionAddComm28,
       "tRPOperPSAccActionAddCommCrOrig": tRPOperPSAccActionAddCommCrOrig,
       "tRPOperPSAccActionRemCommTable": tRPOperPSAccActionRemCommTable,
       "tRPOperPSAccActionRemCommEntry": tRPOperPSAccActionRemCommEntry,
       "tRPOperPSAccActionRemoveComm1": tRPOperPSAccActionRemoveComm1,
       "tRPOperPSAccActionRemoveComm2": tRPOperPSAccActionRemoveComm2,
       "tRPOperPSAccActionRemoveComm3": tRPOperPSAccActionRemoveComm3,
       "tRPOperPSAccActionRemoveComm4": tRPOperPSAccActionRemoveComm4,
       "tRPOperPSAccActionRemoveComm5": tRPOperPSAccActionRemoveComm5,
       "tRPOperPSAccActionRemoveComm6": tRPOperPSAccActionRemoveComm6,
       "tRPOperPSAccActionRemoveComm7": tRPOperPSAccActionRemoveComm7,
       "tRPOperPSAccActionRemoveComm8": tRPOperPSAccActionRemoveComm8,
       "tRPOperPSAccActionRemoveComm9": tRPOperPSAccActionRemoveComm9,
       "tRPOperPSAccActionRemoveComm10": tRPOperPSAccActionRemoveComm10,
       "tRPOperPSAccActionRemoveComm11": tRPOperPSAccActionRemoveComm11,
       "tRPOperPSAccActionRemoveComm12": tRPOperPSAccActionRemoveComm12,
       "tRPOperPSAccActionRemoveComm13": tRPOperPSAccActionRemoveComm13,
       "tRPOperPSAccActionRemoveComm14": tRPOperPSAccActionRemoveComm14,
       "tRPOperPSAccActionRemoveComm15": tRPOperPSAccActionRemoveComm15,
       "tRPOperPSAccActionRemoveComm16": tRPOperPSAccActionRemoveComm16,
       "tRPOperPSAccActionRemoveComm17": tRPOperPSAccActionRemoveComm17,
       "tRPOperPSAccActionRemoveComm18": tRPOperPSAccActionRemoveComm18,
       "tRPOperPSAccActionRemoveComm19": tRPOperPSAccActionRemoveComm19,
       "tRPOperPSAccActionRemoveComm20": tRPOperPSAccActionRemoveComm20,
       "tRPOperPSAccActionRemoveComm21": tRPOperPSAccActionRemoveComm21,
       "tRPOperPSAccActionRemoveComm22": tRPOperPSAccActionRemoveComm22,
       "tRPOperPSAccActionRemoveComm23": tRPOperPSAccActionRemoveComm23,
       "tRPOperPSAccActionRemoveComm24": tRPOperPSAccActionRemoveComm24,
       "tRPOperPSAccActionRemoveComm25": tRPOperPSAccActionRemoveComm25,
       "tRPOperPSAccActionRemoveComm26": tRPOperPSAccActionRemoveComm26,
       "tRPOperPSAccActionRemoveComm27": tRPOperPSAccActionRemoveComm27,
       "tRPOperPSAccActionRemoveComm28": tRPOperPSAccActionRemoveComm28,
       "tRPOperPSAccActionRepCommTable": tRPOperPSAccActionRepCommTable,
       "tRPOperPSAccActionRepCommEntry": tRPOperPSAccActionRepCommEntry,
       "tRPOperPSAccActionReplaceComm1": tRPOperPSAccActionReplaceComm1,
       "tRPOperPSAccActionReplaceComm2": tRPOperPSAccActionReplaceComm2,
       "tRPOperPSAccActionReplaceComm3": tRPOperPSAccActionReplaceComm3,
       "tRPOperPSAccActionReplaceComm4": tRPOperPSAccActionReplaceComm4,
       "tRPOperPSAccActionReplaceComm5": tRPOperPSAccActionReplaceComm5,
       "tRPOperPSAccActionReplaceComm6": tRPOperPSAccActionReplaceComm6,
       "tRPOperPSAccActionReplaceComm7": tRPOperPSAccActionReplaceComm7,
       "tRPOperPSAccActionReplaceComm8": tRPOperPSAccActionReplaceComm8,
       "tRPOperPSAccActionReplaceComm9": tRPOperPSAccActionReplaceComm9,
       "tRPOperPSAccActionReplaceComm10": tRPOperPSAccActionReplaceComm10,
       "tRPOperPSAccActionReplaceComm11": tRPOperPSAccActionReplaceComm11,
       "tRPOperPSAccActionReplaceComm12": tRPOperPSAccActionReplaceComm12,
       "tRPOperPSAccActionReplaceComm13": tRPOperPSAccActionReplaceComm13,
       "tRPOperPSAccActionReplaceComm14": tRPOperPSAccActionReplaceComm14,
       "tRPOperPSAccActionReplaceComm15": tRPOperPSAccActionReplaceComm15,
       "tRPOperPSAccActionReplaceComm16": tRPOperPSAccActionReplaceComm16,
       "tRPOperPSAccActionReplaceComm17": tRPOperPSAccActionReplaceComm17,
       "tRPOperPSAccActionReplaceComm18": tRPOperPSAccActionReplaceComm18,
       "tRPOperPSAccActionReplaceComm19": tRPOperPSAccActionReplaceComm19,
       "tRPOperPSAccActionReplaceComm20": tRPOperPSAccActionReplaceComm20,
       "tRPOperPSAccActionReplaceComm21": tRPOperPSAccActionReplaceComm21,
       "tRPOperPSAccActionReplaceComm22": tRPOperPSAccActionReplaceComm22,
       "tRPOperPSAccActionReplaceComm23": tRPOperPSAccActionReplaceComm23,
       "tRPOperPSAccActionReplaceComm24": tRPOperPSAccActionReplaceComm24,
       "tRPOperPSAccActionReplaceComm25": tRPOperPSAccActionReplaceComm25,
       "tRPOperPSAccActionReplaceComm26": tRPOperPSAccActionReplaceComm26,
       "tRPOperPSAccActionReplaceComm27": tRPOperPSAccActionReplaceComm27,
       "tRPOperPSAccActionReplaceComm28": tRPOperPSAccActionReplaceComm28,
       "tRPOperPSFromCriteriaExtTable": tRPOperPSFromCriteriaExtTable,
       "tRPOperPSFromCriteriaExtEntry": tRPOperPSFromCriteriaExtEntry,
       "tRPOperPSFromCritExtMvpnType": tRPOperPSFromCritExtMvpnType,
       "tRPOperPSFromCritSrcAddrPfxList": tRPOperPSFromCritSrcAddrPfxList,
       "tRPOperPSFromCritOrigValidState": tRPOperPSFromCritOrigValidState,
       "tRPOperPSPolicyVariableTable": tRPOperPSPolicyVariableTable,
       "tRPOperPSPolicyVariableEntry": tRPOperPSPolicyVariableEntry,
       "tRPOperPSPolicyVarName": tRPOperPSPolicyVarName,
       "tRPOperPSPolicyVarRowStatus": tRPOperPSPolicyVarRowStatus,
       "tRPOperPSPolicyVarValue": tRPOperPSPolicyVarValue,
       "tRPOperPSAcptActParamsExtTable": tRPOperPSAcptActParamsExtTable,
       "tRPOperPSAcptActParamsExtEntry": tRPOperPSAcptActParamsExtEntry,
       "tRPOperPSAcptActStickyEcmp": tRPOperPSAcptActStickyEcmp,
       "tRPOperPSAcptActBgpLeaking": tRPOperPSAcptActBgpLeaking,
       "tRPOperPSDefActParamsExtTable": tRPOperPSDefActParamsExtTable,
       "tRPOperPSDefActParamsExtEntry": tRPOperPSDefActParamsExtEntry,
       "tRPOperPSDefActStickyEcmp": tRPOperPSDefActStickyEcmp,
       "tRPOperPSDefActBgpLeaking": tRPOperPSDefActBgpLeaking,
       "tRPAdminObjects": tRPAdminObjects,
       "tRPAdminControlObjects": tRPAdminControlObjects,
       "tRPAdminOwner": tRPAdminOwner,
       "tRPAdminControlApply": tRPAdminControlApply,
       "tRPAdminLastSetTimer": tRPAdminLastSetTimer,
       "tRPAdminLastSetTimeout": tRPAdminLastSetTimeout,
       "tRPAdminControlResetExclusive": tRPAdminControlResetExclusive,
       "tRPAdminValueObjects": tRPAdminValueObjects,
       "tRPAdminASPathTable": tRPAdminASPathTable,
       "tRPAdminASPathEntry": tRPAdminASPathEntry,
       "tRPAdminASPathName": tRPAdminASPathName,
       "tRPAdminASPathRowStatus": tRPAdminASPathRowStatus,
       "tRPAdminASPathRegEx": tRPAdminASPathRegEx,
       "tRPAdminCommunityTable": tRPAdminCommunityTable,
       "tRPAdminCommunityEntry": tRPAdminCommunityEntry,
       "tRPAdminCommunityName": tRPAdminCommunityName,
       "tRPAdminCommunityMember": tRPAdminCommunityMember,
       "tRPAdminCommunityRowStatus": tRPAdminCommunityRowStatus,
       "tRPAdminCommunityCreationOrigin": tRPAdminCommunityCreationOrigin,
       "tRPAdminDampingTable": tRPAdminDampingTable,
       "tRPAdminDampingEntry": tRPAdminDampingEntry,
       "tRPAdminDampingName": tRPAdminDampingName,
       "tRPAdminDampingRowStatus": tRPAdminDampingRowStatus,
       "tRPAdminDampingHalfLife": tRPAdminDampingHalfLife,
       "tRPAdminDampingMaxSuppress": tRPAdminDampingMaxSuppress,
       "tRPAdminDampingReuse": tRPAdminDampingReuse,
       "tRPAdminDampingSuppress": tRPAdminDampingSuppress,
       "tRPAdminPrefixListTable": tRPAdminPrefixListTable,
       "tRPAdminPrefixListEntry": tRPAdminPrefixListEntry,
       "tRPAdminPrefixListName": tRPAdminPrefixListName,
       "tRPAdminPrefixListIpPrefix": tRPAdminPrefixListIpPrefix,
       "tRPAdminPrefixListMask": tRPAdminPrefixListMask,
       "tRPAdminPrefixListRowStatus": tRPAdminPrefixListRowStatus,
       "tRPAdminPrefixListType": tRPAdminPrefixListType,
       "tRPAdminPrefixListThroughLength": tRPAdminPrefixListThroughLength,
       "tRPAdminPrefixListBeginLength": tRPAdminPrefixListBeginLength,
       "tRPAdminPolicyStatementTable": tRPAdminPolicyStatementTable,
       "tRPAdminPolicyStatementEntry": tRPAdminPolicyStatementEntry,
       "tRPAdminPolicyStatementName": tRPAdminPolicyStatementName,
       "tRPAdminPolicyStatementRowStatus": tRPAdminPolicyStatementRowStatus,
       "tRPAdminPolicyStatementDescription": tRPAdminPolicyStatementDescription,
       "tRPAdminPolicyStatementDefaultAction": tRPAdminPolicyStatementDefaultAction,
       "tRPAdminPolicyStatementCrOrigin": tRPAdminPolicyStatementCrOrigin,
       "tRPAdminPSDefaultActionParamsTable": tRPAdminPSDefaultActionParamsTable,
       "tRPAdminPSDefaultActionParamsEntry": tRPAdminPSDefaultActionParamsEntry,
       "tRPAdminPSDefaultActionASPath": tRPAdminPSDefaultActionASPath,
       "tRPAdminPSDefaultActionASPathName": tRPAdminPSDefaultActionASPathName,
       "tRPAdminPSDefaultActionASPathPrependAS": tRPAdminPSDefaultActionASPathPrependAS,
       "tRPAdminPSDefaultActionASPathPrependCount": tRPAdminPSDefaultActionASPathPrependCount,
       "tRPAdminPSDefaultActionCommunity1": tRPAdminPSDefaultActionCommunity1,
       "tRPAdminPSDefaultActionCommunityName1": tRPAdminPSDefaultActionCommunityName1,
       "tRPAdminPSDefaultActionCommunity2": tRPAdminPSDefaultActionCommunity2,
       "tRPAdminPSDefaultActionCommunityName2": tRPAdminPSDefaultActionCommunityName2,
       "tRPAdminPSDefaultActionOrigin": tRPAdminPSDefaultActionOrigin,
       "tRPAdminPSDefaultActionLocalPreferenceSet": tRPAdminPSDefaultActionLocalPreferenceSet,
       "tRPAdminPSDefaultActionLocalPreference": tRPAdminPSDefaultActionLocalPreference,
       "tRPAdminPSDefaultActionMetric": tRPAdminPSDefaultActionMetric,
       "tRPAdminPSDefaultActionMetricValue": tRPAdminPSDefaultActionMetricValue,
       "tRPAdminPSDefaultActionPreference": tRPAdminPSDefaultActionPreference,
       "tRPAdminPSDefaultActionDamping": tRPAdminPSDefaultActionDamping,
       "tRPAdminPSDefaultActionNextHopSelf": tRPAdminPSDefaultActionNextHopSelf,
       "tRPAdminPSDefaultActionNextHop": tRPAdminPSDefaultActionNextHop,
       "tRPAdminPSDefaultActionTag": tRPAdminPSDefaultActionTag,
       "tRPAdminPSDefaultActionOspfType": tRPAdminPSDefaultActionOspfType,
       "tRPAdminPSDefActInetNextHopType": tRPAdminPSDefActInetNextHopType,
       "tRPAdminPSDefActInetNextHop": tRPAdminPSDefActInetNextHop,
       "tRPAdminPSDefaultActionASPathPnd": tRPAdminPSDefaultActionASPathPnd,
       "tRPAdminPSDefActMcRedirSvcId": tRPAdminPSDefActMcRedirSvcId,
       "tRPAdminPSDefActMcRedirIfIndex": tRPAdminPSDefActMcRedirIfIndex,
       "tRPAdminPSDefActionMetricSource": tRPAdminPSDefActionMetricSource,
       "tRPAdminPSDefActionAigpMetric": tRPAdminPSDefActionAigpMetric,
       "tRPAdminPSDefActnAigpMetricVal": tRPAdminPSDefActnAigpMetricVal,
       "tRPAdminPSDefActnSrcClassIndex": tRPAdminPSDefActnSrcClassIndex,
       "tRPAdminPSDefActnDstClassIndex": tRPAdminPSDefActnDstClassIndex,
       "tRPAdminPSDefActnOrigValidState": tRPAdminPSDefActnOrigValidState,
       "tRPAdminPSParamsTable": tRPAdminPSParamsTable,
       "tRPAdminPSParamsEntry": tRPAdminPSParamsEntry,
       "tRPAdminPSNameEntryIndex": tRPAdminPSNameEntryIndex,
       "tRPAdminPSParamsRowStatus": tRPAdminPSParamsRowStatus,
       "tRPAdminPSParamsDescription": tRPAdminPSParamsDescription,
       "tRPAdminPSParamsAction": tRPAdminPSParamsAction,
       "tRPAdminPSParamsCreationOrigin": tRPAdminPSParamsCreationOrigin,
       "tRPAdminPSAcceptActionParamsTable": tRPAdminPSAcceptActionParamsTable,
       "tRPAdminPSAcceptActionParamsEntry": tRPAdminPSAcceptActionParamsEntry,
       "tRPAdminPSAcceptActionASPath": tRPAdminPSAcceptActionASPath,
       "tRPAdminPSAcceptActionASPathName": tRPAdminPSAcceptActionASPathName,
       "tRPAdminPSAcceptActionASPathPrependAS": tRPAdminPSAcceptActionASPathPrependAS,
       "tRPAdminPSAcceptActionASPathPrependCount": tRPAdminPSAcceptActionASPathPrependCount,
       "tRPAdminPSAcceptActionCommunity1": tRPAdminPSAcceptActionCommunity1,
       "tRPAdminPSAcceptActionCommunityName1": tRPAdminPSAcceptActionCommunityName1,
       "tRPAdminPSAcceptActionCommunity2": tRPAdminPSAcceptActionCommunity2,
       "tRPAdminPSAcceptActionCommunityName2": tRPAdminPSAcceptActionCommunityName2,
       "tRPAdminPSAcceptActionOrigin": tRPAdminPSAcceptActionOrigin,
       "tRPAdminPSAcceptActionLocalPreferenceSet": tRPAdminPSAcceptActionLocalPreferenceSet,
       "tRPAdminPSAcceptActionLocalPreference": tRPAdminPSAcceptActionLocalPreference,
       "tRPAdminPSAcceptActionMetric": tRPAdminPSAcceptActionMetric,
       "tRPAdminPSAcceptActionMetricValue": tRPAdminPSAcceptActionMetricValue,
       "tRPAdminPSAcceptActionPreference": tRPAdminPSAcceptActionPreference,
       "tRPAdminPSAcceptActionDamping": tRPAdminPSAcceptActionDamping,
       "tRPAdminPSAcceptActionNextHopSelf": tRPAdminPSAcceptActionNextHopSelf,
       "tRPAdminPSAcceptActionNextHop": tRPAdminPSAcceptActionNextHop,
       "tRPAdminPSAcceptActionTag": tRPAdminPSAcceptActionTag,
       "tRPAdminPSAcceptActionOspfType": tRPAdminPSAcceptActionOspfType,
       "tRPAdminPSAcptActInetNextHopType": tRPAdminPSAcptActInetNextHopType,
       "tRPAdminPSAcptActInetNextHop": tRPAdminPSAcptActInetNextHop,
       "tRPAdminPSAcceptActionASPathPend": tRPAdminPSAcceptActionASPathPend,
       "tRPAdminPSAcceptActionFC": tRPAdminPSAcceptActionFC,
       "tRPAdminPSAcceptActionFCPriority": tRPAdminPSAcceptActionFCPriority,
       "tRPAdminPSAcptActMcRedirSvcId": tRPAdminPSAcptActMcRedirSvcId,
       "tRPAdminPSAcptActMcRedirIfIndex": tRPAdminPSAcptActMcRedirIfIndex,
       "tRPAdminPSAcptActnMetricSource": tRPAdminPSAcptActnMetricSource,
       "tRPAdminPSAcptActionAigpMetric": tRPAdminPSAcptActionAigpMetric,
       "tRPAdminPSAcptActnAigpMetricVal": tRPAdminPSAcptActnAigpMetricVal,
       "tRPAdminPSAcptActnSrcClassIndex": tRPAdminPSAcptActnSrcClassIndex,
       "tRPAdminPSAcptActnDstClassIndex": tRPAdminPSAcptActnDstClassIndex,
       "tRPAdminPSAcptActnOrigValidState": tRPAdminPSAcptActnOrigValidState,
       "tRPAdminPSToCriteriaTable": tRPAdminPSToCriteriaTable,
       "tRPAdminPSToCriteriaEntry": tRPAdminPSToCriteriaEntry,
       "tRPAdminPSToCriteriaIndex": tRPAdminPSToCriteriaIndex,
       "tRPAdminPSToCriteriaRowStatus": tRPAdminPSToCriteriaRowStatus,
       "tRPAdminPSToCriteriaProtocol": tRPAdminPSToCriteriaProtocol,
       "tRPAdminPSToCriteriaNeighborIpAddr": tRPAdminPSToCriteriaNeighborIpAddr,
       "tRPAdminPSToCriteriaNeighborPrefixList": tRPAdminPSToCriteriaNeighborPrefixList,
       "tRPAdminPSToCriteriaIsisLevel": tRPAdminPSToCriteriaIsisLevel,
       "tRPAdminPSToCriteriaPrefixList1": tRPAdminPSToCriteriaPrefixList1,
       "tRPAdminPSToCriteriaPrefixList2": tRPAdminPSToCriteriaPrefixList2,
       "tRPAdminPSToCriteriaPrefixList3": tRPAdminPSToCriteriaPrefixList3,
       "tRPAdminPSToCriteriaPrefixList4": tRPAdminPSToCriteriaPrefixList4,
       "tRPAdminPSToCriteriaPrefixList5": tRPAdminPSToCriteriaPrefixList5,
       "tRPAdminPSToCritNbrInetAddrType": tRPAdminPSToCritNbrInetAddrType,
       "tRPAdminPSToCritNbrInetAddr": tRPAdminPSToCritNbrInetAddr,
       "tRPAdminPSToCriteriaInstanceId": tRPAdminPSToCriteriaInstanceId,
       "tRPAdminPSFromCriteriaTable": tRPAdminPSFromCriteriaTable,
       "tRPAdminPSFromCriteriaEntry": tRPAdminPSFromCriteriaEntry,
       "tRPAdminPSFromCriteriaIndex": tRPAdminPSFromCriteriaIndex,
       "tRPAdminPSFromCriteriaRowStatus": tRPAdminPSFromCriteriaRowStatus,
       "tRPAdminPSFromCriteriaProtocol": tRPAdminPSFromCriteriaProtocol,
       "tRPAdminPSFromCriteriaNeighborIpAddr": tRPAdminPSFromCriteriaNeighborIpAddr,
       "tRPAdminPSFromCriteriaNeighborPrefixList": tRPAdminPSFromCriteriaNeighborPrefixList,
       "tRPAdminPSFromCriteriaPrefixList1": tRPAdminPSFromCriteriaPrefixList1,
       "tRPAdminPSFromCriteriaPrefixList2": tRPAdminPSFromCriteriaPrefixList2,
       "tRPAdminPSFromCriteriaPrefixList3": tRPAdminPSFromCriteriaPrefixList3,
       "tRPAdminPSFromCriteriaPrefixList4": tRPAdminPSFromCriteriaPrefixList4,
       "tRPAdminPSFromCriteriaPrefixList5": tRPAdminPSFromCriteriaPrefixList5,
       "tRPAdminPSFromCriteriaASPath": tRPAdminPSFromCriteriaASPath,
       "tRPAdminPSFromCriteriaCommunity": tRPAdminPSFromCriteriaCommunity,
       "tRPAdminPSFromCriteriaOrigin": tRPAdminPSFromCriteriaOrigin,
       "tRPAdminPSFromCriteriaOspfRouteType": tRPAdminPSFromCriteriaOspfRouteType,
       "tRPAdminPSFromCriteriaArea": tRPAdminPSFromCriteriaArea,
       "tRPAdminPSFromCriteriaAreaConfigured": tRPAdminPSFromCriteriaAreaConfigured,
       "tRPAdminPSFromCriteriaIsisLevel": tRPAdminPSFromCriteriaIsisLevel,
       "tRPAdminPSFromCriteriaIsisExternal": tRPAdminPSFromCriteriaIsisExternal,
       "tRPAdminPSFromCriteriaIgmpHostPrefixList": tRPAdminPSFromCriteriaIgmpHostPrefixList,
       "tRPAdminPSFromCriteriaGrpAddrPrefixList": tRPAdminPSFromCriteriaGrpAddrPrefixList,
       "tRPAdminPSFromCriteriaSrcAddr": tRPAdminPSFromCriteriaSrcAddr,
       "tRPAdminPSFromCriteriaInterface": tRPAdminPSFromCriteriaInterface,
       "tRPAdminPSFromCriteriaTag": tRPAdminPSFromCriteriaTag,
       "tRPAdminPSFromCritNbrInetAddrType": tRPAdminPSFromCritNbrInetAddrType,
       "tRPAdminPSFromCritNbrInetAddr": tRPAdminPSFromCritNbrInetAddr,
       "tRPAdminPSFromCritSrcInetAddrType": tRPAdminPSFromCritSrcInetAddrType,
       "tRPAdminPSFromCritSrcInetAddr": tRPAdminPSFromCritSrcInetAddr,
       "tRPAdminPSFromCriteriaFamily": tRPAdminPSFromCriteriaFamily,
       "tRPAdminPSFromCriteriaInstanceId": tRPAdminPSFromCriteriaInstanceId,
       "tRPAdminPSFromCriteriaMatchTag": tRPAdminPSFromCriteriaMatchTag,
       "tRPAdminPSFromCriteriaState": tRPAdminPSFromCriteriaState,
       "tRPAdminPSFromCritASPathGroup": tRPAdminPSFromCritASPathGroup,
       "tRPAdminPSFromCriteriaPolicy": tRPAdminPSFromCriteriaPolicy,
       "tRPAdminPSFromCritCreationOrigin": tRPAdminPSFromCritCreationOrigin,
       "tRPAdminInetPrefixListTable": tRPAdminInetPrefixListTable,
       "tRPAdminInetPrefixListEntry": tRPAdminInetPrefixListEntry,
       "tRPAdminInetPrefixListName": tRPAdminInetPrefixListName,
       "tRPAdminInetPrefixListPrefixType": tRPAdminInetPrefixListPrefixType,
       "tRPAdminInetPrefixListPrefix": tRPAdminInetPrefixListPrefix,
       "tRPAdminInetPrefixListPrefixLen": tRPAdminInetPrefixListPrefixLen,
       "tRPAdminInetPrefixListType": tRPAdminInetPrefixListType,
       "tRPAdminInetPrefixListRowStatus": tRPAdminInetPrefixListRowStatus,
       "tRPAdminInetPrefixListThroughLen": tRPAdminInetPrefixListThroughLen,
       "tRPAdminInetPrefixListBeginLen": tRPAdminInetPrefixListBeginLen,
       "tRPAdminCommunityExprTable": tRPAdminCommunityExprTable,
       "tRPAdminCommunityExprEntry": tRPAdminCommunityExprEntry,
       "tRPAdminCommunityExprName": tRPAdminCommunityExprName,
       "tRPAdminCommunityExprRowStatus": tRPAdminCommunityExprRowStatus,
       "tRPAdminCommunityExprString1": tRPAdminCommunityExprString1,
       "tRPAdminCommunityExprString2": tRPAdminCommunityExprString2,
       "tRPAdminCommunityExprString3": tRPAdminCommunityExprString3,
       "tRPAdminCommunityExprString4": tRPAdminCommunityExprString4,
       "tRPAdminCommunityExprExactMatch": tRPAdminCommunityExprExactMatch,
       "tRPAdminASPathGroupTable": tRPAdminASPathGroupTable,
       "tRPAdminASPathGroupEntry": tRPAdminASPathGroupEntry,
       "tRPAdminASPathGroupName": tRPAdminASPathGroupName,
       "tRPAdminASPathGroupEntryIndex": tRPAdminASPathGroupEntryIndex,
       "tRPAdminASPathGroupRowStatus": tRPAdminASPathGroupRowStatus,
       "tRPAdminASPathGroupASPathName": tRPAdminASPathGroupASPathName,
       "tRPAdminASPathGroupASPathRegEx": tRPAdminASPathGroupASPathRegEx,
       "tRPAdminPSFromCommExprTable": tRPAdminPSFromCommExprTable,
       "tRPAdminPSFromCommExprEntry": tRPAdminPSFromCommExprEntry,
       "tRPAdminPSFromCommExprRowStatus": tRPAdminPSFromCommExprRowStatus,
       "tRPAdminPSFromCommExprString1": tRPAdminPSFromCommExprString1,
       "tRPAdminPSFromCommExprString2": tRPAdminPSFromCommExprString2,
       "tRPAdminPSFromCommExprString3": tRPAdminPSFromCommExprString3,
       "tRPAdminPSFromCommExprString4": tRPAdminPSFromCommExprString4,
       "tRPAdminPSDefActionAddCommTable": tRPAdminPSDefActionAddCommTable,
       "tRPAdminPSDefActionAddCommEntry": tRPAdminPSDefActionAddCommEntry,
       "tRPAdminPSDefActionAddComm1": tRPAdminPSDefActionAddComm1,
       "tRPAdminPSDefActionAddComm2": tRPAdminPSDefActionAddComm2,
       "tRPAdminPSDefActionAddComm3": tRPAdminPSDefActionAddComm3,
       "tRPAdminPSDefActionAddComm4": tRPAdminPSDefActionAddComm4,
       "tRPAdminPSDefActionAddComm5": tRPAdminPSDefActionAddComm5,
       "tRPAdminPSDefActionAddComm6": tRPAdminPSDefActionAddComm6,
       "tRPAdminPSDefActionAddComm7": tRPAdminPSDefActionAddComm7,
       "tRPAdminPSDefActionAddComm8": tRPAdminPSDefActionAddComm8,
       "tRPAdminPSDefActionAddComm9": tRPAdminPSDefActionAddComm9,
       "tRPAdminPSDefActionAddComm10": tRPAdminPSDefActionAddComm10,
       "tRPAdminPSDefActionAddComm11": tRPAdminPSDefActionAddComm11,
       "tRPAdminPSDefActionAddComm12": tRPAdminPSDefActionAddComm12,
       "tRPAdminPSDefActionAddComm13": tRPAdminPSDefActionAddComm13,
       "tRPAdminPSDefActionAddComm14": tRPAdminPSDefActionAddComm14,
       "tRPAdminPSDefActionAddComm15": tRPAdminPSDefActionAddComm15,
       "tRPAdminPSDefActionAddComm16": tRPAdminPSDefActionAddComm16,
       "tRPAdminPSDefActionAddComm17": tRPAdminPSDefActionAddComm17,
       "tRPAdminPSDefActionAddComm18": tRPAdminPSDefActionAddComm18,
       "tRPAdminPSDefActionAddComm19": tRPAdminPSDefActionAddComm19,
       "tRPAdminPSDefActionAddComm20": tRPAdminPSDefActionAddComm20,
       "tRPAdminPSDefActionAddComm21": tRPAdminPSDefActionAddComm21,
       "tRPAdminPSDefActionAddComm22": tRPAdminPSDefActionAddComm22,
       "tRPAdminPSDefActionAddComm23": tRPAdminPSDefActionAddComm23,
       "tRPAdminPSDefActionAddComm24": tRPAdminPSDefActionAddComm24,
       "tRPAdminPSDefActionAddComm25": tRPAdminPSDefActionAddComm25,
       "tRPAdminPSDefActionAddComm26": tRPAdminPSDefActionAddComm26,
       "tRPAdminPSDefActionAddComm27": tRPAdminPSDefActionAddComm27,
       "tRPAdminPSDefActionAddComm28": tRPAdminPSDefActionAddComm28,
       "tRPAdminPSDefActionRemCommTable": tRPAdminPSDefActionRemCommTable,
       "tRPAdminPSDefActionRemCommEntry": tRPAdminPSDefActionRemCommEntry,
       "tRPAdminPSDefActionRemoveComm1": tRPAdminPSDefActionRemoveComm1,
       "tRPAdminPSDefActionRemoveComm2": tRPAdminPSDefActionRemoveComm2,
       "tRPAdminPSDefActionRemoveComm3": tRPAdminPSDefActionRemoveComm3,
       "tRPAdminPSDefActionRemoveComm4": tRPAdminPSDefActionRemoveComm4,
       "tRPAdminPSDefActionRemoveComm5": tRPAdminPSDefActionRemoveComm5,
       "tRPAdminPSDefActionRemoveComm6": tRPAdminPSDefActionRemoveComm6,
       "tRPAdminPSDefActionRemoveComm7": tRPAdminPSDefActionRemoveComm7,
       "tRPAdminPSDefActionRemoveComm8": tRPAdminPSDefActionRemoveComm8,
       "tRPAdminPSDefActionRemoveComm9": tRPAdminPSDefActionRemoveComm9,
       "tRPAdminPSDefActionRemoveComm10": tRPAdminPSDefActionRemoveComm10,
       "tRPAdminPSDefActionRemoveComm11": tRPAdminPSDefActionRemoveComm11,
       "tRPAdminPSDefActionRemoveComm12": tRPAdminPSDefActionRemoveComm12,
       "tRPAdminPSDefActionRemoveComm13": tRPAdminPSDefActionRemoveComm13,
       "tRPAdminPSDefActionRemoveComm14": tRPAdminPSDefActionRemoveComm14,
       "tRPAdminPSDefActionRemoveComm15": tRPAdminPSDefActionRemoveComm15,
       "tRPAdminPSDefActionRemoveComm16": tRPAdminPSDefActionRemoveComm16,
       "tRPAdminPSDefActionRemoveComm17": tRPAdminPSDefActionRemoveComm17,
       "tRPAdminPSDefActionRemoveComm18": tRPAdminPSDefActionRemoveComm18,
       "tRPAdminPSDefActionRemoveComm19": tRPAdminPSDefActionRemoveComm19,
       "tRPAdminPSDefActionRemoveComm20": tRPAdminPSDefActionRemoveComm20,
       "tRPAdminPSDefActionRemoveComm21": tRPAdminPSDefActionRemoveComm21,
       "tRPAdminPSDefActionRemoveComm22": tRPAdminPSDefActionRemoveComm22,
       "tRPAdminPSDefActionRemoveComm23": tRPAdminPSDefActionRemoveComm23,
       "tRPAdminPSDefActionRemoveComm24": tRPAdminPSDefActionRemoveComm24,
       "tRPAdminPSDefActionRemoveComm25": tRPAdminPSDefActionRemoveComm25,
       "tRPAdminPSDefActionRemoveComm26": tRPAdminPSDefActionRemoveComm26,
       "tRPAdminPSDefActionRemoveComm27": tRPAdminPSDefActionRemoveComm27,
       "tRPAdminPSDefActionRemoveComm28": tRPAdminPSDefActionRemoveComm28,
       "tRPAdminPSDefActionRepCommTable": tRPAdminPSDefActionRepCommTable,
       "tRPAdminPSDefActionRepCommEntry": tRPAdminPSDefActionRepCommEntry,
       "tRPAdminPSDefActionReplaceComm1": tRPAdminPSDefActionReplaceComm1,
       "tRPAdminPSDefActionReplaceComm2": tRPAdminPSDefActionReplaceComm2,
       "tRPAdminPSDefActionReplaceComm3": tRPAdminPSDefActionReplaceComm3,
       "tRPAdminPSDefActionReplaceComm4": tRPAdminPSDefActionReplaceComm4,
       "tRPAdminPSDefActionReplaceComm5": tRPAdminPSDefActionReplaceComm5,
       "tRPAdminPSDefActionReplaceComm6": tRPAdminPSDefActionReplaceComm6,
       "tRPAdminPSDefActionReplaceComm7": tRPAdminPSDefActionReplaceComm7,
       "tRPAdminPSDefActionReplaceComm8": tRPAdminPSDefActionReplaceComm8,
       "tRPAdminPSDefActionReplaceComm9": tRPAdminPSDefActionReplaceComm9,
       "tRPAdminPSDefActionReplaceComm10": tRPAdminPSDefActionReplaceComm10,
       "tRPAdminPSDefActionReplaceComm11": tRPAdminPSDefActionReplaceComm11,
       "tRPAdminPSDefActionReplaceComm12": tRPAdminPSDefActionReplaceComm12,
       "tRPAdminPSDefActionReplaceComm13": tRPAdminPSDefActionReplaceComm13,
       "tRPAdminPSDefActionReplaceComm14": tRPAdminPSDefActionReplaceComm14,
       "tRPAdminPSDefActionReplaceComm15": tRPAdminPSDefActionReplaceComm15,
       "tRPAdminPSDefActionReplaceComm16": tRPAdminPSDefActionReplaceComm16,
       "tRPAdminPSDefActionReplaceComm17": tRPAdminPSDefActionReplaceComm17,
       "tRPAdminPSDefActionReplaceComm18": tRPAdminPSDefActionReplaceComm18,
       "tRPAdminPSDefActionReplaceComm19": tRPAdminPSDefActionReplaceComm19,
       "tRPAdminPSDefActionReplaceComm20": tRPAdminPSDefActionReplaceComm20,
       "tRPAdminPSDefActionReplaceComm21": tRPAdminPSDefActionReplaceComm21,
       "tRPAdminPSDefActionReplaceComm22": tRPAdminPSDefActionReplaceComm22,
       "tRPAdminPSDefActionReplaceComm23": tRPAdminPSDefActionReplaceComm23,
       "tRPAdminPSDefActionReplaceComm24": tRPAdminPSDefActionReplaceComm24,
       "tRPAdminPSDefActionReplaceComm25": tRPAdminPSDefActionReplaceComm25,
       "tRPAdminPSDefActionReplaceComm26": tRPAdminPSDefActionReplaceComm26,
       "tRPAdminPSDefActionReplaceComm27": tRPAdminPSDefActionReplaceComm27,
       "tRPAdminPSDefActionReplaceComm28": tRPAdminPSDefActionReplaceComm28,
       "tRPAdminPSAccActionAddCommTable": tRPAdminPSAccActionAddCommTable,
       "tRPAdminPSAccActionAddCommEntry": tRPAdminPSAccActionAddCommEntry,
       "tRPAdminPSAccActionAddComm1": tRPAdminPSAccActionAddComm1,
       "tRPAdminPSAccActionAddComm2": tRPAdminPSAccActionAddComm2,
       "tRPAdminPSAccActionAddComm3": tRPAdminPSAccActionAddComm3,
       "tRPAdminPSAccActionAddComm4": tRPAdminPSAccActionAddComm4,
       "tRPAdminPSAccActionAddComm5": tRPAdminPSAccActionAddComm5,
       "tRPAdminPSAccActionAddComm6": tRPAdminPSAccActionAddComm6,
       "tRPAdminPSAccActionAddComm7": tRPAdminPSAccActionAddComm7,
       "tRPAdminPSAccActionAddComm8": tRPAdminPSAccActionAddComm8,
       "tRPAdminPSAccActionAddComm9": tRPAdminPSAccActionAddComm9,
       "tRPAdminPSAccActionAddComm10": tRPAdminPSAccActionAddComm10,
       "tRPAdminPSAccActionAddComm11": tRPAdminPSAccActionAddComm11,
       "tRPAdminPSAccActionAddComm12": tRPAdminPSAccActionAddComm12,
       "tRPAdminPSAccActionAddComm13": tRPAdminPSAccActionAddComm13,
       "tRPAdminPSAccActionAddComm14": tRPAdminPSAccActionAddComm14,
       "tRPAdminPSAccActionAddComm15": tRPAdminPSAccActionAddComm15,
       "tRPAdminPSAccActionAddComm16": tRPAdminPSAccActionAddComm16,
       "tRPAdminPSAccActionAddComm17": tRPAdminPSAccActionAddComm17,
       "tRPAdminPSAccActionAddComm18": tRPAdminPSAccActionAddComm18,
       "tRPAdminPSAccActionAddComm19": tRPAdminPSAccActionAddComm19,
       "tRPAdminPSAccActionAddComm20": tRPAdminPSAccActionAddComm20,
       "tRPAdminPSAccActionAddComm21": tRPAdminPSAccActionAddComm21,
       "tRPAdminPSAccActionAddComm22": tRPAdminPSAccActionAddComm22,
       "tRPAdminPSAccActionAddComm23": tRPAdminPSAccActionAddComm23,
       "tRPAdminPSAccActionAddComm24": tRPAdminPSAccActionAddComm24,
       "tRPAdminPSAccActionAddComm25": tRPAdminPSAccActionAddComm25,
       "tRPAdminPSAccActionAddComm26": tRPAdminPSAccActionAddComm26,
       "tRPAdminPSAccActionAddComm27": tRPAdminPSAccActionAddComm27,
       "tRPAdminPSAccActionAddComm28": tRPAdminPSAccActionAddComm28,
       "tRPAdminPSAccActionAddCommCrOrig": tRPAdminPSAccActionAddCommCrOrig,
       "tRPAdminPSAccActionRemCommTable": tRPAdminPSAccActionRemCommTable,
       "tRPAdminPSAccActionRemCommEntry": tRPAdminPSAccActionRemCommEntry,
       "tRPAdminPSAccActionRemoveComm1": tRPAdminPSAccActionRemoveComm1,
       "tRPAdminPSAccActionRemoveComm2": tRPAdminPSAccActionRemoveComm2,
       "tRPAdminPSAccActionRemoveComm3": tRPAdminPSAccActionRemoveComm3,
       "tRPAdminPSAccActionRemoveComm4": tRPAdminPSAccActionRemoveComm4,
       "tRPAdminPSAccActionRemoveComm5": tRPAdminPSAccActionRemoveComm5,
       "tRPAdminPSAccActionRemoveComm6": tRPAdminPSAccActionRemoveComm6,
       "tRPAdminPSAccActionRemoveComm7": tRPAdminPSAccActionRemoveComm7,
       "tRPAdminPSAccActionRemoveComm8": tRPAdminPSAccActionRemoveComm8,
       "tRPAdminPSAccActionRemoveComm9": tRPAdminPSAccActionRemoveComm9,
       "tRPAdminPSAccActionRemoveComm10": tRPAdminPSAccActionRemoveComm10,
       "tRPAdminPSAccActionRemoveComm11": tRPAdminPSAccActionRemoveComm11,
       "tRPAdminPSAccActionRemoveComm12": tRPAdminPSAccActionRemoveComm12,
       "tRPAdminPSAccActionRemoveComm13": tRPAdminPSAccActionRemoveComm13,
       "tRPAdminPSAccActionRemoveComm14": tRPAdminPSAccActionRemoveComm14,
       "tRPAdminPSAccActionRemoveComm15": tRPAdminPSAccActionRemoveComm15,
       "tRPAdminPSAccActionRemoveComm16": tRPAdminPSAccActionRemoveComm16,
       "tRPAdminPSAccActionRemoveComm17": tRPAdminPSAccActionRemoveComm17,
       "tRPAdminPSAccActionRemoveComm18": tRPAdminPSAccActionRemoveComm18,
       "tRPAdminPSAccActionRemoveComm19": tRPAdminPSAccActionRemoveComm19,
       "tRPAdminPSAccActionRemoveComm20": tRPAdminPSAccActionRemoveComm20,
       "tRPAdminPSAccActionRemoveComm21": tRPAdminPSAccActionRemoveComm21,
       "tRPAdminPSAccActionRemoveComm22": tRPAdminPSAccActionRemoveComm22,
       "tRPAdminPSAccActionRemoveComm23": tRPAdminPSAccActionRemoveComm23,
       "tRPAdminPSAccActionRemoveComm24": tRPAdminPSAccActionRemoveComm24,
       "tRPAdminPSAccActionRemoveComm25": tRPAdminPSAccActionRemoveComm25,
       "tRPAdminPSAccActionRemoveComm26": tRPAdminPSAccActionRemoveComm26,
       "tRPAdminPSAccActionRemoveComm27": tRPAdminPSAccActionRemoveComm27,
       "tRPAdminPSAccActionRemoveComm28": tRPAdminPSAccActionRemoveComm28,
       "tRPAdminPSAccActionRepCommTable": tRPAdminPSAccActionRepCommTable,
       "tRPAdminPSAccActionRepCommEntry": tRPAdminPSAccActionRepCommEntry,
       "tRPAdminPSAccActionReplaceComm1": tRPAdminPSAccActionReplaceComm1,
       "tRPAdminPSAccActionReplaceComm2": tRPAdminPSAccActionReplaceComm2,
       "tRPAdminPSAccActionReplaceComm3": tRPAdminPSAccActionReplaceComm3,
       "tRPAdminPSAccActionReplaceComm4": tRPAdminPSAccActionReplaceComm4,
       "tRPAdminPSAccActionReplaceComm5": tRPAdminPSAccActionReplaceComm5,
       "tRPAdminPSAccActionReplaceComm6": tRPAdminPSAccActionReplaceComm6,
       "tRPAdminPSAccActionReplaceComm7": tRPAdminPSAccActionReplaceComm7,
       "tRPAdminPSAccActionReplaceComm8": tRPAdminPSAccActionReplaceComm8,
       "tRPAdminPSAccActionReplaceComm9": tRPAdminPSAccActionReplaceComm9,
       "tRPAdminPSAccActionReplaceComm10": tRPAdminPSAccActionReplaceComm10,
       "tRPAdminPSAccActionReplaceComm11": tRPAdminPSAccActionReplaceComm11,
       "tRPAdminPSAccActionReplaceComm12": tRPAdminPSAccActionReplaceComm12,
       "tRPAdminPSAccActionReplaceComm13": tRPAdminPSAccActionReplaceComm13,
       "tRPAdminPSAccActionReplaceComm14": tRPAdminPSAccActionReplaceComm14,
       "tRPAdminPSAccActionReplaceComm15": tRPAdminPSAccActionReplaceComm15,
       "tRPAdminPSAccActionReplaceComm16": tRPAdminPSAccActionReplaceComm16,
       "tRPAdminPSAccActionReplaceComm17": tRPAdminPSAccActionReplaceComm17,
       "tRPAdminPSAccActionReplaceComm18": tRPAdminPSAccActionReplaceComm18,
       "tRPAdminPSAccActionReplaceComm19": tRPAdminPSAccActionReplaceComm19,
       "tRPAdminPSAccActionReplaceComm20": tRPAdminPSAccActionReplaceComm20,
       "tRPAdminPSAccActionReplaceComm21": tRPAdminPSAccActionReplaceComm21,
       "tRPAdminPSAccActionReplaceComm22": tRPAdminPSAccActionReplaceComm22,
       "tRPAdminPSAccActionReplaceComm23": tRPAdminPSAccActionReplaceComm23,
       "tRPAdminPSAccActionReplaceComm24": tRPAdminPSAccActionReplaceComm24,
       "tRPAdminPSAccActionReplaceComm25": tRPAdminPSAccActionReplaceComm25,
       "tRPAdminPSAccActionReplaceComm26": tRPAdminPSAccActionReplaceComm26,
       "tRPAdminPSAccActionReplaceComm27": tRPAdminPSAccActionReplaceComm27,
       "tRPAdminPSAccActionReplaceComm28": tRPAdminPSAccActionReplaceComm28,
       "tRPAdminPSFromCriteriaExtTable": tRPAdminPSFromCriteriaExtTable,
       "tRPAdminPSFromCriteriaExtEntry": tRPAdminPSFromCriteriaExtEntry,
       "tRPAdminPSFromCritExtMvpnType": tRPAdminPSFromCritExtMvpnType,
       "tRPAdminPSFromCritSrcAddrPfxList": tRPAdminPSFromCritSrcAddrPfxList,
       "tRPAdminPSFromCritOrigValidState": tRPAdminPSFromCritOrigValidState,
       "tRPAdminPSPolicyVariableTable": tRPAdminPSPolicyVariableTable,
       "tRPAdminPSPolicyVariableEntry": tRPAdminPSPolicyVariableEntry,
       "tRPAdminPSPolicyVarName": tRPAdminPSPolicyVarName,
       "tRPAdminPSPolicyVarRowStatus": tRPAdminPSPolicyVarRowStatus,
       "tRPAdminPSPolicyVarValue": tRPAdminPSPolicyVarValue,
       "tRPAdminPSAcptActParamsExtTable": tRPAdminPSAcptActParamsExtTable,
       "tRPAdminPSAcptActParamsExtEntry": tRPAdminPSAcptActParamsExtEntry,
       "tRPAdminPSAcptActStickyEcmp": tRPAdminPSAcptActStickyEcmp,
       "tRPAdminPSAcptActBgpLeaking": tRPAdminPSAcptActBgpLeaking,
       "tRPAdminPSDefActParamsExtTable": tRPAdminPSDefActParamsExtTable,
       "tRPAdminPSDefActParamsExtEntry": tRPAdminPSDefActParamsExtEntry,
       "tRPAdminPSDefActStickyEcmp": tRPAdminPSDefActStickyEcmp,
       "tRPAdminPSDefActBgpLeaking": tRPAdminPSDefActBgpLeaking,
       "tRoutePolicyNotifyPrefix": tRoutePolicyNotifyPrefix,
       "tRoutePolicyNotifications": tRoutePolicyNotifications}
)
