# SNMP MIB module (ME1200-DHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-DHCP-SERVER-MIB.mib
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

(ME1200DisplayString,
 ME1200InterfaceIndex,
 ME1200RowEditorState,
 ME1200Unsigned16) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString",
    "ME1200InterfaceIndex",
    "ME1200RowEditorState",
    "ME1200Unsigned16")

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

me1200DhcpServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109)
)
if mibBuilder.loadTexts:
    me1200DhcpServerMIB.setRevisions(
        ("2014-03-11 00:00",
         "2014-02-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200PoolType(TextualConvention, Integer32):
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
        *(("none", 0),
          ("network", 1),
          ("host", 2))
    )



class ME1200NetbiosNodeType(TextualConvention, Integer32):
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
        *(("nodeNone", 0),
          ("nodeB", 1),
          ("nodeP", 2),
          ("nodeM", 3),
          ("nodeH", 4))
    )



class ME1200ClientIdentifierType(TextualConvention, Integer32):
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
        *(("none", 0),
          ("fqdn", 1),
          ("mac", 2))
    )



class ME1200BindingState(TextualConvention, Integer32):
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
          ("allocated", 1),
          ("committed", 2),
          ("expired", 3))
    )



class ME1200BindingType(TextualConvention, Integer32):
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
          ("automatic", 1),
          ("manual", 2),
          ("expired", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200DhcpServerMIBObjects_ObjectIdentity = ObjectIdentity
me1200DhcpServerMIBObjects = _Me1200DhcpServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1)
)
_Me1200DhcpServerConfig_ObjectIdentity = ObjectIdentity
me1200DhcpServerConfig = _Me1200DhcpServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2)
)
_Me1200DhcpServerConfigGlobals_ObjectIdentity = ObjectIdentity
me1200DhcpServerConfigGlobals = _Me1200DhcpServerConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 1)
)
_Me1200DhcpServerConfigGlobalsMode_Type = TruthValue
_Me1200DhcpServerConfigGlobalsMode_Object = MibScalar
me1200DhcpServerConfigGlobalsMode = _Me1200DhcpServerConfigGlobalsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 1, 1),
    _Me1200DhcpServerConfigGlobalsMode_Type()
)
me1200DhcpServerConfigGlobalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigGlobalsMode.setStatus("current")
_Me1200DhcpServerConfigVlanTable_Object = MibTable
me1200DhcpServerConfigVlanTable = _Me1200DhcpServerConfigVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 2)
)
if mibBuilder.loadTexts:
    me1200DhcpServerConfigVlanTable.setStatus("current")
_Me1200DhcpServerConfigVlanEntry_Object = MibTableRow
me1200DhcpServerConfigVlanEntry = _Me1200DhcpServerConfigVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 2, 1)
)
me1200DhcpServerConfigVlanEntry.setIndexNames(
    (0, "ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigVlanIfIndex"),
)
if mibBuilder.loadTexts:
    me1200DhcpServerConfigVlanEntry.setStatus("current")
_Me1200DhcpServerConfigVlanIfIndex_Type = ME1200InterfaceIndex
_Me1200DhcpServerConfigVlanIfIndex_Object = MibTableColumn
me1200DhcpServerConfigVlanIfIndex = _Me1200DhcpServerConfigVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 2, 1, 1),
    _Me1200DhcpServerConfigVlanIfIndex_Type()
)
me1200DhcpServerConfigVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigVlanIfIndex.setStatus("current")
_Me1200DhcpServerConfigVlanMode_Type = TruthValue
_Me1200DhcpServerConfigVlanMode_Object = MibTableColumn
me1200DhcpServerConfigVlanMode = _Me1200DhcpServerConfigVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 2, 1, 2),
    _Me1200DhcpServerConfigVlanMode_Type()
)
me1200DhcpServerConfigVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigVlanMode.setStatus("current")
_Me1200DhcpServerConfigExcludedTable_Object = MibTable
me1200DhcpServerConfigExcludedTable = _Me1200DhcpServerConfigExcludedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 3)
)
if mibBuilder.loadTexts:
    me1200DhcpServerConfigExcludedTable.setStatus("current")
_Me1200DhcpServerConfigExcludedEntry_Object = MibTableRow
me1200DhcpServerConfigExcludedEntry = _Me1200DhcpServerConfigExcludedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 3, 1)
)
me1200DhcpServerConfigExcludedEntry.setIndexNames(
    (0, "ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigExcludedLowIpAddress"),
    (0, "ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigExcludedHighIpAddress"),
)
if mibBuilder.loadTexts:
    me1200DhcpServerConfigExcludedEntry.setStatus("current")
_Me1200DhcpServerConfigExcludedLowIpAddress_Type = IpAddress
_Me1200DhcpServerConfigExcludedLowIpAddress_Object = MibTableColumn
me1200DhcpServerConfigExcludedLowIpAddress = _Me1200DhcpServerConfigExcludedLowIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 3, 1, 1),
    _Me1200DhcpServerConfigExcludedLowIpAddress_Type()
)
me1200DhcpServerConfigExcludedLowIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigExcludedLowIpAddress.setStatus("current")
_Me1200DhcpServerConfigExcludedHighIpAddress_Type = IpAddress
_Me1200DhcpServerConfigExcludedHighIpAddress_Object = MibTableColumn
me1200DhcpServerConfigExcludedHighIpAddress = _Me1200DhcpServerConfigExcludedHighIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 3, 1, 2),
    _Me1200DhcpServerConfigExcludedHighIpAddress_Type()
)
me1200DhcpServerConfigExcludedHighIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigExcludedHighIpAddress.setStatus("current")
_Me1200DhcpServerConfigExcludedAction_Type = ME1200RowEditorState
_Me1200DhcpServerConfigExcludedAction_Object = MibTableColumn
me1200DhcpServerConfigExcludedAction = _Me1200DhcpServerConfigExcludedAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 3, 1, 100),
    _Me1200DhcpServerConfigExcludedAction_Type()
)
me1200DhcpServerConfigExcludedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigExcludedAction.setStatus("current")
_Me1200DhcpServerConfigExcludedIpTableRowEditor_ObjectIdentity = ObjectIdentity
me1200DhcpServerConfigExcludedIpTableRowEditor = _Me1200DhcpServerConfigExcludedIpTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 4)
)
_Me1200DhcpServerConfigExcludedIpTableRowEditorLowIpAddress_Type = IpAddress
_Me1200DhcpServerConfigExcludedIpTableRowEditorLowIpAddress_Object = MibScalar
me1200DhcpServerConfigExcludedIpTableRowEditorLowIpAddress = _Me1200DhcpServerConfigExcludedIpTableRowEditorLowIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 4, 1),
    _Me1200DhcpServerConfigExcludedIpTableRowEditorLowIpAddress_Type()
)
me1200DhcpServerConfigExcludedIpTableRowEditorLowIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigExcludedIpTableRowEditorLowIpAddress.setStatus("current")
_Me1200DhcpServerConfigExcludedIpTableRowEditorHighIpAddress_Type = IpAddress
_Me1200DhcpServerConfigExcludedIpTableRowEditorHighIpAddress_Object = MibScalar
me1200DhcpServerConfigExcludedIpTableRowEditorHighIpAddress = _Me1200DhcpServerConfigExcludedIpTableRowEditorHighIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 4, 2),
    _Me1200DhcpServerConfigExcludedIpTableRowEditorHighIpAddress_Type()
)
me1200DhcpServerConfigExcludedIpTableRowEditorHighIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigExcludedIpTableRowEditorHighIpAddress.setStatus("current")
_Me1200DhcpServerConfigExcludedIpTableRowEditorAction_Type = ME1200RowEditorState
_Me1200DhcpServerConfigExcludedIpTableRowEditorAction_Object = MibScalar
me1200DhcpServerConfigExcludedIpTableRowEditorAction = _Me1200DhcpServerConfigExcludedIpTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 4, 100),
    _Me1200DhcpServerConfigExcludedIpTableRowEditorAction_Type()
)
me1200DhcpServerConfigExcludedIpTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigExcludedIpTableRowEditorAction.setStatus("current")
_Me1200DhcpServerConfigPoolTable_Object = MibTable
me1200DhcpServerConfigPoolTable = _Me1200DhcpServerConfigPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5)
)
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTable.setStatus("current")
_Me1200DhcpServerConfigPoolEntry_Object = MibTableRow
me1200DhcpServerConfigPoolEntry = _Me1200DhcpServerConfigPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1)
)
me1200DhcpServerConfigPoolEntry.setIndexNames(
    (0, "ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolPoolName"),
)
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolEntry.setStatus("current")


class _Me1200DhcpServerConfigPoolPoolName_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolPoolName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200DhcpServerConfigPoolPoolName_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolPoolName_Object = MibTableColumn
me1200DhcpServerConfigPoolPoolName = _Me1200DhcpServerConfigPoolPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 1),
    _Me1200DhcpServerConfigPoolPoolName_Type()
)
me1200DhcpServerConfigPoolPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolPoolName.setStatus("current")
_Me1200DhcpServerConfigPoolPoolType_Type = ME1200PoolType
_Me1200DhcpServerConfigPoolPoolType_Object = MibTableColumn
me1200DhcpServerConfigPoolPoolType = _Me1200DhcpServerConfigPoolPoolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 2),
    _Me1200DhcpServerConfigPoolPoolType_Type()
)
me1200DhcpServerConfigPoolPoolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolPoolType.setStatus("current")
_Me1200DhcpServerConfigPoolIpv4Address_Type = IpAddress
_Me1200DhcpServerConfigPoolIpv4Address_Object = MibTableColumn
me1200DhcpServerConfigPoolIpv4Address = _Me1200DhcpServerConfigPoolIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 3),
    _Me1200DhcpServerConfigPoolIpv4Address_Type()
)
me1200DhcpServerConfigPoolIpv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolIpv4Address.setStatus("current")
_Me1200DhcpServerConfigPoolSubnetMask_Type = IpAddress
_Me1200DhcpServerConfigPoolSubnetMask_Object = MibTableColumn
me1200DhcpServerConfigPoolSubnetMask = _Me1200DhcpServerConfigPoolSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 4),
    _Me1200DhcpServerConfigPoolSubnetMask_Type()
)
me1200DhcpServerConfigPoolSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolSubnetMask.setStatus("current")
_Me1200DhcpServerConfigPoolSubnetBroadcast_Type = IpAddress
_Me1200DhcpServerConfigPoolSubnetBroadcast_Object = MibTableColumn
me1200DhcpServerConfigPoolSubnetBroadcast = _Me1200DhcpServerConfigPoolSubnetBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 5),
    _Me1200DhcpServerConfigPoolSubnetBroadcast_Type()
)
me1200DhcpServerConfigPoolSubnetBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolSubnetBroadcast.setStatus("current")
_Me1200DhcpServerConfigPoolLeaseDay_Type = Unsigned32
_Me1200DhcpServerConfigPoolLeaseDay_Object = MibTableColumn
me1200DhcpServerConfigPoolLeaseDay = _Me1200DhcpServerConfigPoolLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 6),
    _Me1200DhcpServerConfigPoolLeaseDay_Type()
)
me1200DhcpServerConfigPoolLeaseDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolLeaseDay.setStatus("current")
_Me1200DhcpServerConfigPoolLeaseHour_Type = Unsigned32
_Me1200DhcpServerConfigPoolLeaseHour_Object = MibTableColumn
me1200DhcpServerConfigPoolLeaseHour = _Me1200DhcpServerConfigPoolLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 7),
    _Me1200DhcpServerConfigPoolLeaseHour_Type()
)
me1200DhcpServerConfigPoolLeaseHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolLeaseHour.setStatus("current")
_Me1200DhcpServerConfigPoolLeaseMinute_Type = Unsigned32
_Me1200DhcpServerConfigPoolLeaseMinute_Object = MibTableColumn
me1200DhcpServerConfigPoolLeaseMinute = _Me1200DhcpServerConfigPoolLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 8),
    _Me1200DhcpServerConfigPoolLeaseMinute_Type()
)
me1200DhcpServerConfigPoolLeaseMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolLeaseMinute.setStatus("current")


class _Me1200DhcpServerConfigPoolDomainName_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolDomainName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200DhcpServerConfigPoolDomainName_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolDomainName_Object = MibTableColumn
me1200DhcpServerConfigPoolDomainName = _Me1200DhcpServerConfigPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 9),
    _Me1200DhcpServerConfigPoolDomainName_Type()
)
me1200DhcpServerConfigPoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolDomainName.setStatus("current")
_Me1200DhcpServerConfigPoolDefaultRouter1_Type = IpAddress
_Me1200DhcpServerConfigPoolDefaultRouter1_Object = MibTableColumn
me1200DhcpServerConfigPoolDefaultRouter1 = _Me1200DhcpServerConfigPoolDefaultRouter1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 10),
    _Me1200DhcpServerConfigPoolDefaultRouter1_Type()
)
me1200DhcpServerConfigPoolDefaultRouter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolDefaultRouter1.setStatus("current")
_Me1200DhcpServerConfigPoolDefaultRouter2_Type = IpAddress
_Me1200DhcpServerConfigPoolDefaultRouter2_Object = MibTableColumn
me1200DhcpServerConfigPoolDefaultRouter2 = _Me1200DhcpServerConfigPoolDefaultRouter2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 11),
    _Me1200DhcpServerConfigPoolDefaultRouter2_Type()
)
me1200DhcpServerConfigPoolDefaultRouter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolDefaultRouter2.setStatus("current")
_Me1200DhcpServerConfigPoolDefaultRouter3_Type = IpAddress
_Me1200DhcpServerConfigPoolDefaultRouter3_Object = MibTableColumn
me1200DhcpServerConfigPoolDefaultRouter3 = _Me1200DhcpServerConfigPoolDefaultRouter3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 12),
    _Me1200DhcpServerConfigPoolDefaultRouter3_Type()
)
me1200DhcpServerConfigPoolDefaultRouter3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolDefaultRouter3.setStatus("current")
_Me1200DhcpServerConfigPoolDefaultRouter4_Type = IpAddress
_Me1200DhcpServerConfigPoolDefaultRouter4_Object = MibTableColumn
me1200DhcpServerConfigPoolDefaultRouter4 = _Me1200DhcpServerConfigPoolDefaultRouter4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 13),
    _Me1200DhcpServerConfigPoolDefaultRouter4_Type()
)
me1200DhcpServerConfigPoolDefaultRouter4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolDefaultRouter4.setStatus("current")
_Me1200DhcpServerConfigPoolDnsServer1_Type = IpAddress
_Me1200DhcpServerConfigPoolDnsServer1_Object = MibTableColumn
me1200DhcpServerConfigPoolDnsServer1 = _Me1200DhcpServerConfigPoolDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 14),
    _Me1200DhcpServerConfigPoolDnsServer1_Type()
)
me1200DhcpServerConfigPoolDnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolDnsServer1.setStatus("current")
_Me1200DhcpServerConfigPoolDnsServer2_Type = IpAddress
_Me1200DhcpServerConfigPoolDnsServer2_Object = MibTableColumn
me1200DhcpServerConfigPoolDnsServer2 = _Me1200DhcpServerConfigPoolDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 15),
    _Me1200DhcpServerConfigPoolDnsServer2_Type()
)
me1200DhcpServerConfigPoolDnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolDnsServer2.setStatus("current")
_Me1200DhcpServerConfigPoolDnsServer3_Type = IpAddress
_Me1200DhcpServerConfigPoolDnsServer3_Object = MibTableColumn
me1200DhcpServerConfigPoolDnsServer3 = _Me1200DhcpServerConfigPoolDnsServer3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 16),
    _Me1200DhcpServerConfigPoolDnsServer3_Type()
)
me1200DhcpServerConfigPoolDnsServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolDnsServer3.setStatus("current")
_Me1200DhcpServerConfigPoolDnsServer4_Type = IpAddress
_Me1200DhcpServerConfigPoolDnsServer4_Object = MibTableColumn
me1200DhcpServerConfigPoolDnsServer4 = _Me1200DhcpServerConfigPoolDnsServer4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 17),
    _Me1200DhcpServerConfigPoolDnsServer4_Type()
)
me1200DhcpServerConfigPoolDnsServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolDnsServer4.setStatus("current")
_Me1200DhcpServerConfigPoolNtpServer1_Type = IpAddress
_Me1200DhcpServerConfigPoolNtpServer1_Object = MibTableColumn
me1200DhcpServerConfigPoolNtpServer1 = _Me1200DhcpServerConfigPoolNtpServer1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 18),
    _Me1200DhcpServerConfigPoolNtpServer1_Type()
)
me1200DhcpServerConfigPoolNtpServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolNtpServer1.setStatus("current")
_Me1200DhcpServerConfigPoolNtpServer2_Type = IpAddress
_Me1200DhcpServerConfigPoolNtpServer2_Object = MibTableColumn
me1200DhcpServerConfigPoolNtpServer2 = _Me1200DhcpServerConfigPoolNtpServer2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 19),
    _Me1200DhcpServerConfigPoolNtpServer2_Type()
)
me1200DhcpServerConfigPoolNtpServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolNtpServer2.setStatus("current")
_Me1200DhcpServerConfigPoolNtpServer3_Type = IpAddress
_Me1200DhcpServerConfigPoolNtpServer3_Object = MibTableColumn
me1200DhcpServerConfigPoolNtpServer3 = _Me1200DhcpServerConfigPoolNtpServer3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 20),
    _Me1200DhcpServerConfigPoolNtpServer3_Type()
)
me1200DhcpServerConfigPoolNtpServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolNtpServer3.setStatus("current")
_Me1200DhcpServerConfigPoolNtpServer4_Type = IpAddress
_Me1200DhcpServerConfigPoolNtpServer4_Object = MibTableColumn
me1200DhcpServerConfigPoolNtpServer4 = _Me1200DhcpServerConfigPoolNtpServer4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 21),
    _Me1200DhcpServerConfigPoolNtpServer4_Type()
)
me1200DhcpServerConfigPoolNtpServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolNtpServer4.setStatus("current")
_Me1200DhcpServerConfigPoolNetbiosNodeType_Type = ME1200NetbiosNodeType
_Me1200DhcpServerConfigPoolNetbiosNodeType_Object = MibTableColumn
me1200DhcpServerConfigPoolNetbiosNodeType = _Me1200DhcpServerConfigPoolNetbiosNodeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 22),
    _Me1200DhcpServerConfigPoolNetbiosNodeType_Type()
)
me1200DhcpServerConfigPoolNetbiosNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolNetbiosNodeType.setStatus("current")


class _Me1200DhcpServerConfigPoolNetbiosScope_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolNetbiosScope based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200DhcpServerConfigPoolNetbiosScope_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolNetbiosScope_Object = MibTableColumn
me1200DhcpServerConfigPoolNetbiosScope = _Me1200DhcpServerConfigPoolNetbiosScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 23),
    _Me1200DhcpServerConfigPoolNetbiosScope_Type()
)
me1200DhcpServerConfigPoolNetbiosScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolNetbiosScope.setStatus("current")
_Me1200DhcpServerConfigPoolNetbiosNameServer1_Type = IpAddress
_Me1200DhcpServerConfigPoolNetbiosNameServer1_Object = MibTableColumn
me1200DhcpServerConfigPoolNetbiosNameServer1 = _Me1200DhcpServerConfigPoolNetbiosNameServer1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 24),
    _Me1200DhcpServerConfigPoolNetbiosNameServer1_Type()
)
me1200DhcpServerConfigPoolNetbiosNameServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolNetbiosNameServer1.setStatus("current")
_Me1200DhcpServerConfigPoolNetbiosNameServer2_Type = IpAddress
_Me1200DhcpServerConfigPoolNetbiosNameServer2_Object = MibTableColumn
me1200DhcpServerConfigPoolNetbiosNameServer2 = _Me1200DhcpServerConfigPoolNetbiosNameServer2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 25),
    _Me1200DhcpServerConfigPoolNetbiosNameServer2_Type()
)
me1200DhcpServerConfigPoolNetbiosNameServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolNetbiosNameServer2.setStatus("current")
_Me1200DhcpServerConfigPoolNetbiosNameServer3_Type = IpAddress
_Me1200DhcpServerConfigPoolNetbiosNameServer3_Object = MibTableColumn
me1200DhcpServerConfigPoolNetbiosNameServer3 = _Me1200DhcpServerConfigPoolNetbiosNameServer3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 26),
    _Me1200DhcpServerConfigPoolNetbiosNameServer3_Type()
)
me1200DhcpServerConfigPoolNetbiosNameServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolNetbiosNameServer3.setStatus("current")
_Me1200DhcpServerConfigPoolNetbiosNameServer4_Type = IpAddress
_Me1200DhcpServerConfigPoolNetbiosNameServer4_Object = MibTableColumn
me1200DhcpServerConfigPoolNetbiosNameServer4 = _Me1200DhcpServerConfigPoolNetbiosNameServer4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 27),
    _Me1200DhcpServerConfigPoolNetbiosNameServer4_Type()
)
me1200DhcpServerConfigPoolNetbiosNameServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolNetbiosNameServer4.setStatus("current")


class _Me1200DhcpServerConfigPoolNisDomainName_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolNisDomainName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200DhcpServerConfigPoolNisDomainName_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolNisDomainName_Object = MibTableColumn
me1200DhcpServerConfigPoolNisDomainName = _Me1200DhcpServerConfigPoolNisDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 28),
    _Me1200DhcpServerConfigPoolNisDomainName_Type()
)
me1200DhcpServerConfigPoolNisDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolNisDomainName.setStatus("current")
_Me1200DhcpServerConfigPoolNisServer1_Type = IpAddress
_Me1200DhcpServerConfigPoolNisServer1_Object = MibTableColumn
me1200DhcpServerConfigPoolNisServer1 = _Me1200DhcpServerConfigPoolNisServer1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 29),
    _Me1200DhcpServerConfigPoolNisServer1_Type()
)
me1200DhcpServerConfigPoolNisServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolNisServer1.setStatus("current")
_Me1200DhcpServerConfigPoolNisServer2_Type = IpAddress
_Me1200DhcpServerConfigPoolNisServer2_Object = MibTableColumn
me1200DhcpServerConfigPoolNisServer2 = _Me1200DhcpServerConfigPoolNisServer2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 30),
    _Me1200DhcpServerConfigPoolNisServer2_Type()
)
me1200DhcpServerConfigPoolNisServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolNisServer2.setStatus("current")
_Me1200DhcpServerConfigPoolNisServer3_Type = IpAddress
_Me1200DhcpServerConfigPoolNisServer3_Object = MibTableColumn
me1200DhcpServerConfigPoolNisServer3 = _Me1200DhcpServerConfigPoolNisServer3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 31),
    _Me1200DhcpServerConfigPoolNisServer3_Type()
)
me1200DhcpServerConfigPoolNisServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolNisServer3.setStatus("current")
_Me1200DhcpServerConfigPoolNisServer4_Type = IpAddress
_Me1200DhcpServerConfigPoolNisServer4_Object = MibTableColumn
me1200DhcpServerConfigPoolNisServer4 = _Me1200DhcpServerConfigPoolNisServer4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 32),
    _Me1200DhcpServerConfigPoolNisServer4_Type()
)
me1200DhcpServerConfigPoolNisServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolNisServer4.setStatus("current")
_Me1200DhcpServerConfigPoolClientIdentifierType_Type = ME1200ClientIdentifierType
_Me1200DhcpServerConfigPoolClientIdentifierType_Object = MibTableColumn
me1200DhcpServerConfigPoolClientIdentifierType = _Me1200DhcpServerConfigPoolClientIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 33),
    _Me1200DhcpServerConfigPoolClientIdentifierType_Type()
)
me1200DhcpServerConfigPoolClientIdentifierType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolClientIdentifierType.setStatus("current")


class _Me1200DhcpServerConfigPoolClientIdentifierFqdn_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolClientIdentifierFqdn based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Me1200DhcpServerConfigPoolClientIdentifierFqdn_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolClientIdentifierFqdn_Object = MibTableColumn
me1200DhcpServerConfigPoolClientIdentifierFqdn = _Me1200DhcpServerConfigPoolClientIdentifierFqdn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 34),
    _Me1200DhcpServerConfigPoolClientIdentifierFqdn_Type()
)
me1200DhcpServerConfigPoolClientIdentifierFqdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolClientIdentifierFqdn.setStatus("current")
_Me1200DhcpServerConfigPoolClientIdentifierMac_Type = MacAddress
_Me1200DhcpServerConfigPoolClientIdentifierMac_Object = MibTableColumn
me1200DhcpServerConfigPoolClientIdentifierMac = _Me1200DhcpServerConfigPoolClientIdentifierMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 35),
    _Me1200DhcpServerConfigPoolClientIdentifierMac_Type()
)
me1200DhcpServerConfigPoolClientIdentifierMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolClientIdentifierMac.setStatus("current")
_Me1200DhcpServerConfigPoolClientHardwareAddress_Type = MacAddress
_Me1200DhcpServerConfigPoolClientHardwareAddress_Object = MibTableColumn
me1200DhcpServerConfigPoolClientHardwareAddress = _Me1200DhcpServerConfigPoolClientHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 36),
    _Me1200DhcpServerConfigPoolClientHardwareAddress_Type()
)
me1200DhcpServerConfigPoolClientHardwareAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolClientHardwareAddress.setStatus("current")


class _Me1200DhcpServerConfigPoolClientName_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolClientName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200DhcpServerConfigPoolClientName_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolClientName_Object = MibTableColumn
me1200DhcpServerConfigPoolClientName = _Me1200DhcpServerConfigPoolClientName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 37),
    _Me1200DhcpServerConfigPoolClientName_Type()
)
me1200DhcpServerConfigPoolClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolClientName.setStatus("current")


class _Me1200DhcpServerConfigPoolVendorClassId1_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolVendorClassId1 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Me1200DhcpServerConfigPoolVendorClassId1_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolVendorClassId1_Object = MibTableColumn
me1200DhcpServerConfigPoolVendorClassId1 = _Me1200DhcpServerConfigPoolVendorClassId1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 38),
    _Me1200DhcpServerConfigPoolVendorClassId1_Type()
)
me1200DhcpServerConfigPoolVendorClassId1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolVendorClassId1.setStatus("current")


class _Me1200DhcpServerConfigPoolVendorSpecificInfo1_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolVendorSpecificInfo1 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_Me1200DhcpServerConfigPoolVendorSpecificInfo1_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolVendorSpecificInfo1_Object = MibTableColumn
me1200DhcpServerConfigPoolVendorSpecificInfo1 = _Me1200DhcpServerConfigPoolVendorSpecificInfo1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 39),
    _Me1200DhcpServerConfigPoolVendorSpecificInfo1_Type()
)
me1200DhcpServerConfigPoolVendorSpecificInfo1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolVendorSpecificInfo1.setStatus("current")


class _Me1200DhcpServerConfigPoolVendorClassId2_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolVendorClassId2 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Me1200DhcpServerConfigPoolVendorClassId2_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolVendorClassId2_Object = MibTableColumn
me1200DhcpServerConfigPoolVendorClassId2 = _Me1200DhcpServerConfigPoolVendorClassId2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 40),
    _Me1200DhcpServerConfigPoolVendorClassId2_Type()
)
me1200DhcpServerConfigPoolVendorClassId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolVendorClassId2.setStatus("current")


class _Me1200DhcpServerConfigPoolVendorSpecificInfo2_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolVendorSpecificInfo2 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_Me1200DhcpServerConfigPoolVendorSpecificInfo2_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolVendorSpecificInfo2_Object = MibTableColumn
me1200DhcpServerConfigPoolVendorSpecificInfo2 = _Me1200DhcpServerConfigPoolVendorSpecificInfo2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 41),
    _Me1200DhcpServerConfigPoolVendorSpecificInfo2_Type()
)
me1200DhcpServerConfigPoolVendorSpecificInfo2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolVendorSpecificInfo2.setStatus("current")


class _Me1200DhcpServerConfigPoolVendorClassId3_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolVendorClassId3 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Me1200DhcpServerConfigPoolVendorClassId3_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolVendorClassId3_Object = MibTableColumn
me1200DhcpServerConfigPoolVendorClassId3 = _Me1200DhcpServerConfigPoolVendorClassId3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 42),
    _Me1200DhcpServerConfigPoolVendorClassId3_Type()
)
me1200DhcpServerConfigPoolVendorClassId3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolVendorClassId3.setStatus("current")


class _Me1200DhcpServerConfigPoolVendorSpecificInfo3_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolVendorSpecificInfo3 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_Me1200DhcpServerConfigPoolVendorSpecificInfo3_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolVendorSpecificInfo3_Object = MibTableColumn
me1200DhcpServerConfigPoolVendorSpecificInfo3 = _Me1200DhcpServerConfigPoolVendorSpecificInfo3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 43),
    _Me1200DhcpServerConfigPoolVendorSpecificInfo3_Type()
)
me1200DhcpServerConfigPoolVendorSpecificInfo3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolVendorSpecificInfo3.setStatus("current")


class _Me1200DhcpServerConfigPoolVendorClassId4_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolVendorClassId4 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Me1200DhcpServerConfigPoolVendorClassId4_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolVendorClassId4_Object = MibTableColumn
me1200DhcpServerConfigPoolVendorClassId4 = _Me1200DhcpServerConfigPoolVendorClassId4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 44),
    _Me1200DhcpServerConfigPoolVendorClassId4_Type()
)
me1200DhcpServerConfigPoolVendorClassId4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolVendorClassId4.setStatus("current")


class _Me1200DhcpServerConfigPoolVendorSpecificInfo4_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolVendorSpecificInfo4 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_Me1200DhcpServerConfigPoolVendorSpecificInfo4_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolVendorSpecificInfo4_Object = MibTableColumn
me1200DhcpServerConfigPoolVendorSpecificInfo4 = _Me1200DhcpServerConfigPoolVendorSpecificInfo4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 45),
    _Me1200DhcpServerConfigPoolVendorSpecificInfo4_Type()
)
me1200DhcpServerConfigPoolVendorSpecificInfo4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolVendorSpecificInfo4.setStatus("current")
_Me1200DhcpServerConfigPoolAction_Type = ME1200RowEditorState
_Me1200DhcpServerConfigPoolAction_Object = MibTableColumn
me1200DhcpServerConfigPoolAction = _Me1200DhcpServerConfigPoolAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 5, 1, 100),
    _Me1200DhcpServerConfigPoolAction_Type()
)
me1200DhcpServerConfigPoolAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolAction.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditor_ObjectIdentity = ObjectIdentity
me1200DhcpServerConfigPoolTableRowEditor = _Me1200DhcpServerConfigPoolTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6)
)


class _Me1200DhcpServerConfigPoolTableRowEditorPoolName_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolTableRowEditorPoolName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200DhcpServerConfigPoolTableRowEditorPoolName_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolTableRowEditorPoolName_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorPoolName = _Me1200DhcpServerConfigPoolTableRowEditorPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 1),
    _Me1200DhcpServerConfigPoolTableRowEditorPoolName_Type()
)
me1200DhcpServerConfigPoolTableRowEditorPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorPoolName.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorPoolType_Type = ME1200PoolType
_Me1200DhcpServerConfigPoolTableRowEditorPoolType_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorPoolType = _Me1200DhcpServerConfigPoolTableRowEditorPoolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 2),
    _Me1200DhcpServerConfigPoolTableRowEditorPoolType_Type()
)
me1200DhcpServerConfigPoolTableRowEditorPoolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorPoolType.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorIpv4Address_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorIpv4Address_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorIpv4Address = _Me1200DhcpServerConfigPoolTableRowEditorIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 3),
    _Me1200DhcpServerConfigPoolTableRowEditorIpv4Address_Type()
)
me1200DhcpServerConfigPoolTableRowEditorIpv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorIpv4Address.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorSubnetMask_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorSubnetMask_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorSubnetMask = _Me1200DhcpServerConfigPoolTableRowEditorSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 4),
    _Me1200DhcpServerConfigPoolTableRowEditorSubnetMask_Type()
)
me1200DhcpServerConfigPoolTableRowEditorSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorSubnetMask.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorSubnetBroadcast_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorSubnetBroadcast_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorSubnetBroadcast = _Me1200DhcpServerConfigPoolTableRowEditorSubnetBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 5),
    _Me1200DhcpServerConfigPoolTableRowEditorSubnetBroadcast_Type()
)
me1200DhcpServerConfigPoolTableRowEditorSubnetBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorSubnetBroadcast.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorLeaseDay_Type = Unsigned32
_Me1200DhcpServerConfigPoolTableRowEditorLeaseDay_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorLeaseDay = _Me1200DhcpServerConfigPoolTableRowEditorLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 6),
    _Me1200DhcpServerConfigPoolTableRowEditorLeaseDay_Type()
)
me1200DhcpServerConfigPoolTableRowEditorLeaseDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorLeaseDay.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorLeaseHour_Type = Unsigned32
_Me1200DhcpServerConfigPoolTableRowEditorLeaseHour_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorLeaseHour = _Me1200DhcpServerConfigPoolTableRowEditorLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 7),
    _Me1200DhcpServerConfigPoolTableRowEditorLeaseHour_Type()
)
me1200DhcpServerConfigPoolTableRowEditorLeaseHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorLeaseHour.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorLeaseMinute_Type = Unsigned32
_Me1200DhcpServerConfigPoolTableRowEditorLeaseMinute_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorLeaseMinute = _Me1200DhcpServerConfigPoolTableRowEditorLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 8),
    _Me1200DhcpServerConfigPoolTableRowEditorLeaseMinute_Type()
)
me1200DhcpServerConfigPoolTableRowEditorLeaseMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorLeaseMinute.setStatus("current")


class _Me1200DhcpServerConfigPoolTableRowEditorDomainName_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolTableRowEditorDomainName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200DhcpServerConfigPoolTableRowEditorDomainName_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolTableRowEditorDomainName_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorDomainName = _Me1200DhcpServerConfigPoolTableRowEditorDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 9),
    _Me1200DhcpServerConfigPoolTableRowEditorDomainName_Type()
)
me1200DhcpServerConfigPoolTableRowEditorDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorDomainName.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorDefaultRouter1_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorDefaultRouter1_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorDefaultRouter1 = _Me1200DhcpServerConfigPoolTableRowEditorDefaultRouter1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 10),
    _Me1200DhcpServerConfigPoolTableRowEditorDefaultRouter1_Type()
)
me1200DhcpServerConfigPoolTableRowEditorDefaultRouter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorDefaultRouter1.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorDefaultRouter2_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorDefaultRouter2_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorDefaultRouter2 = _Me1200DhcpServerConfigPoolTableRowEditorDefaultRouter2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 11),
    _Me1200DhcpServerConfigPoolTableRowEditorDefaultRouter2_Type()
)
me1200DhcpServerConfigPoolTableRowEditorDefaultRouter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorDefaultRouter2.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorDefaultRouter3_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorDefaultRouter3_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorDefaultRouter3 = _Me1200DhcpServerConfigPoolTableRowEditorDefaultRouter3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 12),
    _Me1200DhcpServerConfigPoolTableRowEditorDefaultRouter3_Type()
)
me1200DhcpServerConfigPoolTableRowEditorDefaultRouter3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorDefaultRouter3.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorDefaultRouter4_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorDefaultRouter4_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorDefaultRouter4 = _Me1200DhcpServerConfigPoolTableRowEditorDefaultRouter4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 13),
    _Me1200DhcpServerConfigPoolTableRowEditorDefaultRouter4_Type()
)
me1200DhcpServerConfigPoolTableRowEditorDefaultRouter4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorDefaultRouter4.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorDnsServer1_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorDnsServer1_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorDnsServer1 = _Me1200DhcpServerConfigPoolTableRowEditorDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 14),
    _Me1200DhcpServerConfigPoolTableRowEditorDnsServer1_Type()
)
me1200DhcpServerConfigPoolTableRowEditorDnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorDnsServer1.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorDnsServer2_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorDnsServer2_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorDnsServer2 = _Me1200DhcpServerConfigPoolTableRowEditorDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 15),
    _Me1200DhcpServerConfigPoolTableRowEditorDnsServer2_Type()
)
me1200DhcpServerConfigPoolTableRowEditorDnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorDnsServer2.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorDnsServer3_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorDnsServer3_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorDnsServer3 = _Me1200DhcpServerConfigPoolTableRowEditorDnsServer3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 16),
    _Me1200DhcpServerConfigPoolTableRowEditorDnsServer3_Type()
)
me1200DhcpServerConfigPoolTableRowEditorDnsServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorDnsServer3.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorDnsServer4_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorDnsServer4_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorDnsServer4 = _Me1200DhcpServerConfigPoolTableRowEditorDnsServer4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 17),
    _Me1200DhcpServerConfigPoolTableRowEditorDnsServer4_Type()
)
me1200DhcpServerConfigPoolTableRowEditorDnsServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorDnsServer4.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorNtpServer1_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorNtpServer1_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorNtpServer1 = _Me1200DhcpServerConfigPoolTableRowEditorNtpServer1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 18),
    _Me1200DhcpServerConfigPoolTableRowEditorNtpServer1_Type()
)
me1200DhcpServerConfigPoolTableRowEditorNtpServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorNtpServer1.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorNtpServer2_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorNtpServer2_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorNtpServer2 = _Me1200DhcpServerConfigPoolTableRowEditorNtpServer2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 19),
    _Me1200DhcpServerConfigPoolTableRowEditorNtpServer2_Type()
)
me1200DhcpServerConfigPoolTableRowEditorNtpServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorNtpServer2.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorNtpServer3_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorNtpServer3_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorNtpServer3 = _Me1200DhcpServerConfigPoolTableRowEditorNtpServer3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 20),
    _Me1200DhcpServerConfigPoolTableRowEditorNtpServer3_Type()
)
me1200DhcpServerConfigPoolTableRowEditorNtpServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorNtpServer3.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorNtpServer4_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorNtpServer4_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorNtpServer4 = _Me1200DhcpServerConfigPoolTableRowEditorNtpServer4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 21),
    _Me1200DhcpServerConfigPoolTableRowEditorNtpServer4_Type()
)
me1200DhcpServerConfigPoolTableRowEditorNtpServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorNtpServer4.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorNetbiosNodeType_Type = ME1200NetbiosNodeType
_Me1200DhcpServerConfigPoolTableRowEditorNetbiosNodeType_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorNetbiosNodeType = _Me1200DhcpServerConfigPoolTableRowEditorNetbiosNodeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 22),
    _Me1200DhcpServerConfigPoolTableRowEditorNetbiosNodeType_Type()
)
me1200DhcpServerConfigPoolTableRowEditorNetbiosNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorNetbiosNodeType.setStatus("current")


class _Me1200DhcpServerConfigPoolTableRowEditorNetbiosScope_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolTableRowEditorNetbiosScope based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200DhcpServerConfigPoolTableRowEditorNetbiosScope_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolTableRowEditorNetbiosScope_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorNetbiosScope = _Me1200DhcpServerConfigPoolTableRowEditorNetbiosScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 23),
    _Me1200DhcpServerConfigPoolTableRowEditorNetbiosScope_Type()
)
me1200DhcpServerConfigPoolTableRowEditorNetbiosScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorNetbiosScope.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer1_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer1_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer1 = _Me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 24),
    _Me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer1_Type()
)
me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer1.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer2_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer2_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer2 = _Me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 25),
    _Me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer2_Type()
)
me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer2.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer3_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer3_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer3 = _Me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 26),
    _Me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer3_Type()
)
me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer3.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer4_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer4_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer4 = _Me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 27),
    _Me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer4_Type()
)
me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer4.setStatus("current")


class _Me1200DhcpServerConfigPoolTableRowEditorNisDomainName_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolTableRowEditorNisDomainName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200DhcpServerConfigPoolTableRowEditorNisDomainName_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolTableRowEditorNisDomainName_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorNisDomainName = _Me1200DhcpServerConfigPoolTableRowEditorNisDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 28),
    _Me1200DhcpServerConfigPoolTableRowEditorNisDomainName_Type()
)
me1200DhcpServerConfigPoolTableRowEditorNisDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorNisDomainName.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorNisServer1_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorNisServer1_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorNisServer1 = _Me1200DhcpServerConfigPoolTableRowEditorNisServer1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 29),
    _Me1200DhcpServerConfigPoolTableRowEditorNisServer1_Type()
)
me1200DhcpServerConfigPoolTableRowEditorNisServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorNisServer1.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorNisServer2_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorNisServer2_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorNisServer2 = _Me1200DhcpServerConfigPoolTableRowEditorNisServer2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 30),
    _Me1200DhcpServerConfigPoolTableRowEditorNisServer2_Type()
)
me1200DhcpServerConfigPoolTableRowEditorNisServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorNisServer2.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorNisServer3_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorNisServer3_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorNisServer3 = _Me1200DhcpServerConfigPoolTableRowEditorNisServer3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 31),
    _Me1200DhcpServerConfigPoolTableRowEditorNisServer3_Type()
)
me1200DhcpServerConfigPoolTableRowEditorNisServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorNisServer3.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorNisServer4_Type = IpAddress
_Me1200DhcpServerConfigPoolTableRowEditorNisServer4_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorNisServer4 = _Me1200DhcpServerConfigPoolTableRowEditorNisServer4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 32),
    _Me1200DhcpServerConfigPoolTableRowEditorNisServer4_Type()
)
me1200DhcpServerConfigPoolTableRowEditorNisServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorNisServer4.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorClientIdentifierType_Type = ME1200ClientIdentifierType
_Me1200DhcpServerConfigPoolTableRowEditorClientIdentifierType_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorClientIdentifierType = _Me1200DhcpServerConfigPoolTableRowEditorClientIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 33),
    _Me1200DhcpServerConfigPoolTableRowEditorClientIdentifierType_Type()
)
me1200DhcpServerConfigPoolTableRowEditorClientIdentifierType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorClientIdentifierType.setStatus("current")


class _Me1200DhcpServerConfigPoolTableRowEditorClientIdentifierFqdn_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolTableRowEditorClientIdentifierFqdn based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Me1200DhcpServerConfigPoolTableRowEditorClientIdentifierFqdn_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolTableRowEditorClientIdentifierFqdn_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorClientIdentifierFqdn = _Me1200DhcpServerConfigPoolTableRowEditorClientIdentifierFqdn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 34),
    _Me1200DhcpServerConfigPoolTableRowEditorClientIdentifierFqdn_Type()
)
me1200DhcpServerConfigPoolTableRowEditorClientIdentifierFqdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorClientIdentifierFqdn.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorClientIdentifierMac_Type = MacAddress
_Me1200DhcpServerConfigPoolTableRowEditorClientIdentifierMac_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorClientIdentifierMac = _Me1200DhcpServerConfigPoolTableRowEditorClientIdentifierMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 35),
    _Me1200DhcpServerConfigPoolTableRowEditorClientIdentifierMac_Type()
)
me1200DhcpServerConfigPoolTableRowEditorClientIdentifierMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorClientIdentifierMac.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorClientHardwareAddress_Type = MacAddress
_Me1200DhcpServerConfigPoolTableRowEditorClientHardwareAddress_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorClientHardwareAddress = _Me1200DhcpServerConfigPoolTableRowEditorClientHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 36),
    _Me1200DhcpServerConfigPoolTableRowEditorClientHardwareAddress_Type()
)
me1200DhcpServerConfigPoolTableRowEditorClientHardwareAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorClientHardwareAddress.setStatus("current")


class _Me1200DhcpServerConfigPoolTableRowEditorClientName_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolTableRowEditorClientName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200DhcpServerConfigPoolTableRowEditorClientName_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolTableRowEditorClientName_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorClientName = _Me1200DhcpServerConfigPoolTableRowEditorClientName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 37),
    _Me1200DhcpServerConfigPoolTableRowEditorClientName_Type()
)
me1200DhcpServerConfigPoolTableRowEditorClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorClientName.setStatus("current")


class _Me1200DhcpServerConfigPoolTableRowEditorVendorClassId1_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolTableRowEditorVendorClassId1 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Me1200DhcpServerConfigPoolTableRowEditorVendorClassId1_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolTableRowEditorVendorClassId1_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorVendorClassId1 = _Me1200DhcpServerConfigPoolTableRowEditorVendorClassId1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 38),
    _Me1200DhcpServerConfigPoolTableRowEditorVendorClassId1_Type()
)
me1200DhcpServerConfigPoolTableRowEditorVendorClassId1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorVendorClassId1.setStatus("current")


class _Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1 = _Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 39),
    _Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1_Type()
)
me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1.setStatus("current")


class _Me1200DhcpServerConfigPoolTableRowEditorVendorClassId2_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolTableRowEditorVendorClassId2 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Me1200DhcpServerConfigPoolTableRowEditorVendorClassId2_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolTableRowEditorVendorClassId2_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorVendorClassId2 = _Me1200DhcpServerConfigPoolTableRowEditorVendorClassId2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 40),
    _Me1200DhcpServerConfigPoolTableRowEditorVendorClassId2_Type()
)
me1200DhcpServerConfigPoolTableRowEditorVendorClassId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorVendorClassId2.setStatus("current")


class _Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2 = _Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 41),
    _Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2_Type()
)
me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2.setStatus("current")


class _Me1200DhcpServerConfigPoolTableRowEditorVendorClassId3_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolTableRowEditorVendorClassId3 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Me1200DhcpServerConfigPoolTableRowEditorVendorClassId3_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolTableRowEditorVendorClassId3_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorVendorClassId3 = _Me1200DhcpServerConfigPoolTableRowEditorVendorClassId3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 42),
    _Me1200DhcpServerConfigPoolTableRowEditorVendorClassId3_Type()
)
me1200DhcpServerConfigPoolTableRowEditorVendorClassId3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorVendorClassId3.setStatus("current")


class _Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3 = _Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 43),
    _Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3_Type()
)
me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3.setStatus("current")


class _Me1200DhcpServerConfigPoolTableRowEditorVendorClassId4_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolTableRowEditorVendorClassId4 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Me1200DhcpServerConfigPoolTableRowEditorVendorClassId4_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolTableRowEditorVendorClassId4_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorVendorClassId4 = _Me1200DhcpServerConfigPoolTableRowEditorVendorClassId4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 44),
    _Me1200DhcpServerConfigPoolTableRowEditorVendorClassId4_Type()
)
me1200DhcpServerConfigPoolTableRowEditorVendorClassId4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorVendorClassId4.setStatus("current")


class _Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4 = _Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 45),
    _Me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4_Type()
)
me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4.setStatus("current")
_Me1200DhcpServerConfigPoolTableRowEditorAction_Type = ME1200RowEditorState
_Me1200DhcpServerConfigPoolTableRowEditorAction_Object = MibScalar
me1200DhcpServerConfigPoolTableRowEditorAction = _Me1200DhcpServerConfigPoolTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 2, 6, 100),
    _Me1200DhcpServerConfigPoolTableRowEditorAction_Type()
)
me1200DhcpServerConfigPoolTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorAction.setStatus("current")
_Me1200DhcpServerStatus_ObjectIdentity = ObjectIdentity
me1200DhcpServerStatus = _Me1200DhcpServerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3)
)
_Me1200DhcpServerStatusDeclinedTable_Object = MibTable
me1200DhcpServerStatusDeclinedTable = _Me1200DhcpServerStatusDeclinedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 1)
)
if mibBuilder.loadTexts:
    me1200DhcpServerStatusDeclinedTable.setStatus("current")
_Me1200DhcpServerStatusDeclinedEntry_Object = MibTableRow
me1200DhcpServerStatusDeclinedEntry = _Me1200DhcpServerStatusDeclinedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 1, 1)
)
me1200DhcpServerStatusDeclinedEntry.setIndexNames(
    (0, "ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusDeclinedEntryNo"),
)
if mibBuilder.loadTexts:
    me1200DhcpServerStatusDeclinedEntry.setStatus("current")


class _Me1200DhcpServerStatusDeclinedEntryNo_Type(Integer32):
    """Custom type me1200DhcpServerStatusDeclinedEntryNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200DhcpServerStatusDeclinedEntryNo_Type.__name__ = "Integer32"
_Me1200DhcpServerStatusDeclinedEntryNo_Object = MibTableColumn
me1200DhcpServerStatusDeclinedEntryNo = _Me1200DhcpServerStatusDeclinedEntryNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 1, 1, 1),
    _Me1200DhcpServerStatusDeclinedEntryNo_Type()
)
me1200DhcpServerStatusDeclinedEntryNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusDeclinedEntryNo.setStatus("current")
_Me1200DhcpServerStatusDeclinedIpv4Address_Type = IpAddress
_Me1200DhcpServerStatusDeclinedIpv4Address_Object = MibTableColumn
me1200DhcpServerStatusDeclinedIpv4Address = _Me1200DhcpServerStatusDeclinedIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 1, 1, 2),
    _Me1200DhcpServerStatusDeclinedIpv4Address_Type()
)
me1200DhcpServerStatusDeclinedIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusDeclinedIpv4Address.setStatus("current")
_Me1200DhcpServerStatusStatistics_ObjectIdentity = ObjectIdentity
me1200DhcpServerStatusStatistics = _Me1200DhcpServerStatusStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 2)
)
_Me1200DhcpServerStatusStatisticsDiscoverCnt_Type = Unsigned32
_Me1200DhcpServerStatusStatisticsDiscoverCnt_Object = MibScalar
me1200DhcpServerStatusStatisticsDiscoverCnt = _Me1200DhcpServerStatusStatisticsDiscoverCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 2, 1),
    _Me1200DhcpServerStatusStatisticsDiscoverCnt_Type()
)
me1200DhcpServerStatusStatisticsDiscoverCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusStatisticsDiscoverCnt.setStatus("current")
_Me1200DhcpServerStatusStatisticsOfferCnt_Type = Unsigned32
_Me1200DhcpServerStatusStatisticsOfferCnt_Object = MibScalar
me1200DhcpServerStatusStatisticsOfferCnt = _Me1200DhcpServerStatusStatisticsOfferCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 2, 2),
    _Me1200DhcpServerStatusStatisticsOfferCnt_Type()
)
me1200DhcpServerStatusStatisticsOfferCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusStatisticsOfferCnt.setStatus("current")
_Me1200DhcpServerStatusStatisticsRequestCnt_Type = Unsigned32
_Me1200DhcpServerStatusStatisticsRequestCnt_Object = MibScalar
me1200DhcpServerStatusStatisticsRequestCnt = _Me1200DhcpServerStatusStatisticsRequestCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 2, 3),
    _Me1200DhcpServerStatusStatisticsRequestCnt_Type()
)
me1200DhcpServerStatusStatisticsRequestCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusStatisticsRequestCnt.setStatus("current")
_Me1200DhcpServerStatusStatisticsAckCnt_Type = Unsigned32
_Me1200DhcpServerStatusStatisticsAckCnt_Object = MibScalar
me1200DhcpServerStatusStatisticsAckCnt = _Me1200DhcpServerStatusStatisticsAckCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 2, 4),
    _Me1200DhcpServerStatusStatisticsAckCnt_Type()
)
me1200DhcpServerStatusStatisticsAckCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusStatisticsAckCnt.setStatus("current")
_Me1200DhcpServerStatusStatisticsNakCnt_Type = Unsigned32
_Me1200DhcpServerStatusStatisticsNakCnt_Object = MibScalar
me1200DhcpServerStatusStatisticsNakCnt = _Me1200DhcpServerStatusStatisticsNakCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 2, 5),
    _Me1200DhcpServerStatusStatisticsNakCnt_Type()
)
me1200DhcpServerStatusStatisticsNakCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusStatisticsNakCnt.setStatus("current")
_Me1200DhcpServerStatusStatisticsDeclineCnt_Type = Unsigned32
_Me1200DhcpServerStatusStatisticsDeclineCnt_Object = MibScalar
me1200DhcpServerStatusStatisticsDeclineCnt = _Me1200DhcpServerStatusStatisticsDeclineCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 2, 6),
    _Me1200DhcpServerStatusStatisticsDeclineCnt_Type()
)
me1200DhcpServerStatusStatisticsDeclineCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusStatisticsDeclineCnt.setStatus("current")
_Me1200DhcpServerStatusStatisticsReleaseCnt_Type = Unsigned32
_Me1200DhcpServerStatusStatisticsReleaseCnt_Object = MibScalar
me1200DhcpServerStatusStatisticsReleaseCnt = _Me1200DhcpServerStatusStatisticsReleaseCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 2, 7),
    _Me1200DhcpServerStatusStatisticsReleaseCnt_Type()
)
me1200DhcpServerStatusStatisticsReleaseCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusStatisticsReleaseCnt.setStatus("current")
_Me1200DhcpServerStatusStatisticsInformCnt_Type = Unsigned32
_Me1200DhcpServerStatusStatisticsInformCnt_Object = MibScalar
me1200DhcpServerStatusStatisticsInformCnt = _Me1200DhcpServerStatusStatisticsInformCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 2, 8),
    _Me1200DhcpServerStatusStatisticsInformCnt_Type()
)
me1200DhcpServerStatusStatisticsInformCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusStatisticsInformCnt.setStatus("current")
_Me1200DhcpServerStatusBindingTable_Object = MibTable
me1200DhcpServerStatusBindingTable = _Me1200DhcpServerStatusBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 3)
)
if mibBuilder.loadTexts:
    me1200DhcpServerStatusBindingTable.setStatus("current")
_Me1200DhcpServerStatusBindingEntry_Object = MibTableRow
me1200DhcpServerStatusBindingEntry = _Me1200DhcpServerStatusBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 3, 1)
)
me1200DhcpServerStatusBindingEntry.setIndexNames(
    (0, "ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusBindingIpAddress"),
)
if mibBuilder.loadTexts:
    me1200DhcpServerStatusBindingEntry.setStatus("current")
_Me1200DhcpServerStatusBindingIpAddress_Type = IpAddress
_Me1200DhcpServerStatusBindingIpAddress_Object = MibTableColumn
me1200DhcpServerStatusBindingIpAddress = _Me1200DhcpServerStatusBindingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 3, 1, 1),
    _Me1200DhcpServerStatusBindingIpAddress_Type()
)
me1200DhcpServerStatusBindingIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusBindingIpAddress.setStatus("current")
_Me1200DhcpServerStatusBindingState_Type = ME1200BindingState
_Me1200DhcpServerStatusBindingState_Object = MibTableColumn
me1200DhcpServerStatusBindingState = _Me1200DhcpServerStatusBindingState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 3, 1, 2),
    _Me1200DhcpServerStatusBindingState_Type()
)
me1200DhcpServerStatusBindingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusBindingState.setStatus("current")
_Me1200DhcpServerStatusBindingType_Type = ME1200BindingType
_Me1200DhcpServerStatusBindingType_Object = MibTableColumn
me1200DhcpServerStatusBindingType = _Me1200DhcpServerStatusBindingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 3, 1, 3),
    _Me1200DhcpServerStatusBindingType_Type()
)
me1200DhcpServerStatusBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusBindingType.setStatus("current")


class _Me1200DhcpServerStatusBindingPoolName_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerStatusBindingPoolName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200DhcpServerStatusBindingPoolName_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerStatusBindingPoolName_Object = MibTableColumn
me1200DhcpServerStatusBindingPoolName = _Me1200DhcpServerStatusBindingPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 3, 1, 4),
    _Me1200DhcpServerStatusBindingPoolName_Type()
)
me1200DhcpServerStatusBindingPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusBindingPoolName.setStatus("current")
_Me1200DhcpServerStatusBindingServerId_Type = IpAddress
_Me1200DhcpServerStatusBindingServerId_Object = MibTableColumn
me1200DhcpServerStatusBindingServerId = _Me1200DhcpServerStatusBindingServerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 3, 1, 5),
    _Me1200DhcpServerStatusBindingServerId_Type()
)
me1200DhcpServerStatusBindingServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusBindingServerId.setStatus("current")
_Me1200DhcpServerStatusBindingVlanId_Type = ME1200Unsigned16
_Me1200DhcpServerStatusBindingVlanId_Object = MibTableColumn
me1200DhcpServerStatusBindingVlanId = _Me1200DhcpServerStatusBindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 3, 1, 6),
    _Me1200DhcpServerStatusBindingVlanId_Type()
)
me1200DhcpServerStatusBindingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusBindingVlanId.setStatus("current")
_Me1200DhcpServerStatusBindingSubnetMask_Type = IpAddress
_Me1200DhcpServerStatusBindingSubnetMask_Object = MibTableColumn
me1200DhcpServerStatusBindingSubnetMask = _Me1200DhcpServerStatusBindingSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 3, 1, 7),
    _Me1200DhcpServerStatusBindingSubnetMask_Type()
)
me1200DhcpServerStatusBindingSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusBindingSubnetMask.setStatus("current")
_Me1200DhcpServerStatusBindingClientIdentifierType_Type = ME1200ClientIdentifierType
_Me1200DhcpServerStatusBindingClientIdentifierType_Object = MibTableColumn
me1200DhcpServerStatusBindingClientIdentifierType = _Me1200DhcpServerStatusBindingClientIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 3, 1, 8),
    _Me1200DhcpServerStatusBindingClientIdentifierType_Type()
)
me1200DhcpServerStatusBindingClientIdentifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusBindingClientIdentifierType.setStatus("current")


class _Me1200DhcpServerStatusBindingClientIdentifierFqdn_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerStatusBindingClientIdentifierFqdn based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Me1200DhcpServerStatusBindingClientIdentifierFqdn_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerStatusBindingClientIdentifierFqdn_Object = MibTableColumn
me1200DhcpServerStatusBindingClientIdentifierFqdn = _Me1200DhcpServerStatusBindingClientIdentifierFqdn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 3, 1, 9),
    _Me1200DhcpServerStatusBindingClientIdentifierFqdn_Type()
)
me1200DhcpServerStatusBindingClientIdentifierFqdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusBindingClientIdentifierFqdn.setStatus("current")
_Me1200DhcpServerStatusBindingClientIdentifierMac_Type = MacAddress
_Me1200DhcpServerStatusBindingClientIdentifierMac_Object = MibTableColumn
me1200DhcpServerStatusBindingClientIdentifierMac = _Me1200DhcpServerStatusBindingClientIdentifierMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 3, 1, 10),
    _Me1200DhcpServerStatusBindingClientIdentifierMac_Type()
)
me1200DhcpServerStatusBindingClientIdentifierMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusBindingClientIdentifierMac.setStatus("current")
_Me1200DhcpServerStatusBindingMacAddress_Type = MacAddress
_Me1200DhcpServerStatusBindingMacAddress_Object = MibTableColumn
me1200DhcpServerStatusBindingMacAddress = _Me1200DhcpServerStatusBindingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 3, 1, 11),
    _Me1200DhcpServerStatusBindingMacAddress_Type()
)
me1200DhcpServerStatusBindingMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusBindingMacAddress.setStatus("current")


class _Me1200DhcpServerStatusBindingLease_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerStatusBindingLease based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Me1200DhcpServerStatusBindingLease_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerStatusBindingLease_Object = MibTableColumn
me1200DhcpServerStatusBindingLease = _Me1200DhcpServerStatusBindingLease_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 3, 1, 12),
    _Me1200DhcpServerStatusBindingLease_Type()
)
me1200DhcpServerStatusBindingLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusBindingLease.setStatus("current")


class _Me1200DhcpServerStatusBindingTimeToExpire_Type(ME1200DisplayString):
    """Custom type me1200DhcpServerStatusBindingTimeToExpire based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Me1200DhcpServerStatusBindingTimeToExpire_Type.__name__ = "ME1200DisplayString"
_Me1200DhcpServerStatusBindingTimeToExpire_Object = MibTableColumn
me1200DhcpServerStatusBindingTimeToExpire = _Me1200DhcpServerStatusBindingTimeToExpire_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 3, 3, 1, 13),
    _Me1200DhcpServerStatusBindingTimeToExpire_Type()
)
me1200DhcpServerStatusBindingTimeToExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpServerStatusBindingTimeToExpire.setStatus("current")
_Me1200DhcpServerControl_ObjectIdentity = ObjectIdentity
me1200DhcpServerControl = _Me1200DhcpServerControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 4)
)
_Me1200DhcpServerControlStatistics_ObjectIdentity = ObjectIdentity
me1200DhcpServerControlStatistics = _Me1200DhcpServerControlStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 4, 1)
)
_Me1200DhcpServerControlStatisticsClear_Type = TruthValue
_Me1200DhcpServerControlStatisticsClear_Object = MibScalar
me1200DhcpServerControlStatisticsClear = _Me1200DhcpServerControlStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 4, 1, 1),
    _Me1200DhcpServerControlStatisticsClear_Type()
)
me1200DhcpServerControlStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerControlStatisticsClear.setStatus("current")
_Me1200DhcpServerControlBinding_ObjectIdentity = ObjectIdentity
me1200DhcpServerControlBinding = _Me1200DhcpServerControlBinding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 4, 2)
)
_Me1200DhcpServerControlBindingClearByIp_Type = IpAddress
_Me1200DhcpServerControlBindingClearByIp_Object = MibScalar
me1200DhcpServerControlBindingClearByIp = _Me1200DhcpServerControlBindingClearByIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 4, 2, 1),
    _Me1200DhcpServerControlBindingClearByIp_Type()
)
me1200DhcpServerControlBindingClearByIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerControlBindingClearByIp.setStatus("current")
_Me1200DhcpServerControlBindingClearByType_Type = ME1200BindingType
_Me1200DhcpServerControlBindingClearByType_Object = MibScalar
me1200DhcpServerControlBindingClearByType = _Me1200DhcpServerControlBindingClearByType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 1, 4, 2, 2),
    _Me1200DhcpServerControlBindingClearByType_Type()
)
me1200DhcpServerControlBindingClearByType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpServerControlBindingClearByType.setStatus("current")
_Me1200DhcpServerMIBConformance_ObjectIdentity = ObjectIdentity
me1200DhcpServerMIBConformance = _Me1200DhcpServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 2)
)
_Me1200DhcpServerMIBCompliances_ObjectIdentity = ObjectIdentity
me1200DhcpServerMIBCompliances = _Me1200DhcpServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 2, 1)
)
_Me1200DhcpServerMIBGroups_ObjectIdentity = ObjectIdentity
me1200DhcpServerMIBGroups = _Me1200DhcpServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 2, 2)
)

# Managed Objects groups

me1200DhcpServerConfigGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 2, 2, 1)
)
me1200DhcpServerConfigGlobalsInfoGroup.setObjects(
    ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigGlobalsMode")
)
if mibBuilder.loadTexts:
    me1200DhcpServerConfigGlobalsInfoGroup.setStatus("current")

me1200DhcpServerConfigVlanTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 2, 2, 2)
)
me1200DhcpServerConfigVlanTableInfoGroup.setObjects(
    ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigVlanMode")
)
if mibBuilder.loadTexts:
    me1200DhcpServerConfigVlanTableInfoGroup.setStatus("current")

me1200DhcpServerConfigExcludedTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 2, 2, 3)
)
me1200DhcpServerConfigExcludedTableInfoGroup.setObjects(
    ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigExcludedAction")
)
if mibBuilder.loadTexts:
    me1200DhcpServerConfigExcludedTableInfoGroup.setStatus("current")

me1200DhcpServerConfigExcludedIpTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 2, 2, 4)
)
me1200DhcpServerConfigExcludedIpTableRowEditorInfoGroup.setObjects(
      *(("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigExcludedIpTableRowEditorLowIpAddress"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigExcludedIpTableRowEditorHighIpAddress"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigExcludedIpTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200DhcpServerConfigExcludedIpTableRowEditorInfoGroup.setStatus("current")

me1200DhcpServerConfigPoolTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 2, 2, 5)
)
me1200DhcpServerConfigPoolTableInfoGroup.setObjects(
      *(("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolPoolType"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolIpv4Address"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolSubnetMask"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolSubnetBroadcast"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolLeaseDay"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolLeaseHour"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolLeaseMinute"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolDomainName"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolDefaultRouter1"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolDefaultRouter2"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolDefaultRouter3"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolDefaultRouter4"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolDnsServer1"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolDnsServer2"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolDnsServer3"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolDnsServer4"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolNtpServer1"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolNtpServer2"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolNtpServer3"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolNtpServer4"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolNetbiosNodeType"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolNetbiosScope"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolNetbiosNameServer1"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolNetbiosNameServer2"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolNetbiosNameServer3"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolNetbiosNameServer4"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolNisDomainName"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolNisServer1"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolNisServer2"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolNisServer3"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolNisServer4"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolClientIdentifierType"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolClientIdentifierFqdn"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolClientIdentifierMac"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolClientHardwareAddress"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolClientName"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolVendorClassId1"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolVendorSpecificInfo1"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolVendorClassId2"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolVendorSpecificInfo2"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolVendorClassId3"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolVendorSpecificInfo3"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolVendorClassId4"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolVendorSpecificInfo4"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolAction"))
)
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableInfoGroup.setStatus("current")

me1200DhcpServerConfigPoolTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 2, 2, 6)
)
me1200DhcpServerConfigPoolTableRowEditorInfoGroup.setObjects(
      *(("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorPoolName"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorPoolType"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorIpv4Address"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorSubnetMask"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorSubnetBroadcast"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorLeaseDay"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorLeaseHour"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorLeaseMinute"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorDomainName"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorDefaultRouter1"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorDefaultRouter2"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorDefaultRouter3"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorDefaultRouter4"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorDnsServer1"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorDnsServer2"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorDnsServer3"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorDnsServer4"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorNtpServer1"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorNtpServer2"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorNtpServer3"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorNtpServer4"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorNetbiosNodeType"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorNetbiosScope"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer1"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer2"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer3"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer4"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorNisDomainName"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorNisServer1"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorNisServer2"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorNisServer3"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorNisServer4"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorClientIdentifierType"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorClientIdentifierFqdn"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorClientIdentifierMac"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorClientHardwareAddress"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorClientName"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorVendorClassId1"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorVendorClassId2"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorVendorClassId3"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorVendorClassId4"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200DhcpServerConfigPoolTableRowEditorInfoGroup.setStatus("current")

me1200DhcpServerStatusDeclinedTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 2, 2, 7)
)
me1200DhcpServerStatusDeclinedTableInfoGroup.setObjects(
    ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusDeclinedIpv4Address")
)
if mibBuilder.loadTexts:
    me1200DhcpServerStatusDeclinedTableInfoGroup.setStatus("current")

me1200DhcpServerStatusStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 2, 2, 8)
)
me1200DhcpServerStatusStatisticsInfoGroup.setObjects(
      *(("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusStatisticsDiscoverCnt"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusStatisticsOfferCnt"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusStatisticsRequestCnt"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusStatisticsAckCnt"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusStatisticsNakCnt"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusStatisticsDeclineCnt"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusStatisticsReleaseCnt"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusStatisticsInformCnt"))
)
if mibBuilder.loadTexts:
    me1200DhcpServerStatusStatisticsInfoGroup.setStatus("current")

me1200DhcpServerStatusBindingTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 2, 2, 9)
)
me1200DhcpServerStatusBindingTableInfoGroup.setObjects(
      *(("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusBindingState"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusBindingType"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusBindingPoolName"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusBindingServerId"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusBindingVlanId"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusBindingSubnetMask"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusBindingClientIdentifierType"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusBindingClientIdentifierFqdn"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusBindingClientIdentifierMac"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusBindingMacAddress"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusBindingLease"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusBindingTimeToExpire"))
)
if mibBuilder.loadTexts:
    me1200DhcpServerStatusBindingTableInfoGroup.setStatus("current")

me1200DhcpServerControlStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 2, 2, 10)
)
me1200DhcpServerControlStatisticsInfoGroup.setObjects(
    ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerControlStatisticsClear")
)
if mibBuilder.loadTexts:
    me1200DhcpServerControlStatisticsInfoGroup.setStatus("current")

me1200DhcpServerControlBindingInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 2, 2, 11)
)
me1200DhcpServerControlBindingInfoGroup.setObjects(
      *(("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerControlBindingClearByIp"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerControlBindingClearByType"))
)
if mibBuilder.loadTexts:
    me1200DhcpServerControlBindingInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200DhcpServerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 109, 2, 1, 1)
)
me1200DhcpServerMIBCompliance.setObjects(
      *(("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigGlobalsInfoGroup"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigVlanTableInfoGroup"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigExcludedTableInfoGroup"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigExcludedIpTableRowEditorInfoGroup"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableInfoGroup"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerConfigPoolTableRowEditorInfoGroup"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusDeclinedTableInfoGroup"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusStatisticsInfoGroup"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerStatusBindingTableInfoGroup"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerControlStatisticsInfoGroup"),
        ("ME1200-DHCP-SERVER-MIB", "me1200DhcpServerControlBindingInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200DhcpServerMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-DHCP-SERVER-MIB",
    **{"ME1200PoolType": ME1200PoolType,
       "ME1200NetbiosNodeType": ME1200NetbiosNodeType,
       "ME1200ClientIdentifierType": ME1200ClientIdentifierType,
       "ME1200BindingState": ME1200BindingState,
       "ME1200BindingType": ME1200BindingType,
       "me1200DhcpServerMIB": me1200DhcpServerMIB,
       "me1200DhcpServerMIBObjects": me1200DhcpServerMIBObjects,
       "me1200DhcpServerConfig": me1200DhcpServerConfig,
       "me1200DhcpServerConfigGlobals": me1200DhcpServerConfigGlobals,
       "me1200DhcpServerConfigGlobalsMode": me1200DhcpServerConfigGlobalsMode,
       "me1200DhcpServerConfigVlanTable": me1200DhcpServerConfigVlanTable,
       "me1200DhcpServerConfigVlanEntry": me1200DhcpServerConfigVlanEntry,
       "me1200DhcpServerConfigVlanIfIndex": me1200DhcpServerConfigVlanIfIndex,
       "me1200DhcpServerConfigVlanMode": me1200DhcpServerConfigVlanMode,
       "me1200DhcpServerConfigExcludedTable": me1200DhcpServerConfigExcludedTable,
       "me1200DhcpServerConfigExcludedEntry": me1200DhcpServerConfigExcludedEntry,
       "me1200DhcpServerConfigExcludedLowIpAddress": me1200DhcpServerConfigExcludedLowIpAddress,
       "me1200DhcpServerConfigExcludedHighIpAddress": me1200DhcpServerConfigExcludedHighIpAddress,
       "me1200DhcpServerConfigExcludedAction": me1200DhcpServerConfigExcludedAction,
       "me1200DhcpServerConfigExcludedIpTableRowEditor": me1200DhcpServerConfigExcludedIpTableRowEditor,
       "me1200DhcpServerConfigExcludedIpTableRowEditorLowIpAddress": me1200DhcpServerConfigExcludedIpTableRowEditorLowIpAddress,
       "me1200DhcpServerConfigExcludedIpTableRowEditorHighIpAddress": me1200DhcpServerConfigExcludedIpTableRowEditorHighIpAddress,
       "me1200DhcpServerConfigExcludedIpTableRowEditorAction": me1200DhcpServerConfigExcludedIpTableRowEditorAction,
       "me1200DhcpServerConfigPoolTable": me1200DhcpServerConfigPoolTable,
       "me1200DhcpServerConfigPoolEntry": me1200DhcpServerConfigPoolEntry,
       "me1200DhcpServerConfigPoolPoolName": me1200DhcpServerConfigPoolPoolName,
       "me1200DhcpServerConfigPoolPoolType": me1200DhcpServerConfigPoolPoolType,
       "me1200DhcpServerConfigPoolIpv4Address": me1200DhcpServerConfigPoolIpv4Address,
       "me1200DhcpServerConfigPoolSubnetMask": me1200DhcpServerConfigPoolSubnetMask,
       "me1200DhcpServerConfigPoolSubnetBroadcast": me1200DhcpServerConfigPoolSubnetBroadcast,
       "me1200DhcpServerConfigPoolLeaseDay": me1200DhcpServerConfigPoolLeaseDay,
       "me1200DhcpServerConfigPoolLeaseHour": me1200DhcpServerConfigPoolLeaseHour,
       "me1200DhcpServerConfigPoolLeaseMinute": me1200DhcpServerConfigPoolLeaseMinute,
       "me1200DhcpServerConfigPoolDomainName": me1200DhcpServerConfigPoolDomainName,
       "me1200DhcpServerConfigPoolDefaultRouter1": me1200DhcpServerConfigPoolDefaultRouter1,
       "me1200DhcpServerConfigPoolDefaultRouter2": me1200DhcpServerConfigPoolDefaultRouter2,
       "me1200DhcpServerConfigPoolDefaultRouter3": me1200DhcpServerConfigPoolDefaultRouter3,
       "me1200DhcpServerConfigPoolDefaultRouter4": me1200DhcpServerConfigPoolDefaultRouter4,
       "me1200DhcpServerConfigPoolDnsServer1": me1200DhcpServerConfigPoolDnsServer1,
       "me1200DhcpServerConfigPoolDnsServer2": me1200DhcpServerConfigPoolDnsServer2,
       "me1200DhcpServerConfigPoolDnsServer3": me1200DhcpServerConfigPoolDnsServer3,
       "me1200DhcpServerConfigPoolDnsServer4": me1200DhcpServerConfigPoolDnsServer4,
       "me1200DhcpServerConfigPoolNtpServer1": me1200DhcpServerConfigPoolNtpServer1,
       "me1200DhcpServerConfigPoolNtpServer2": me1200DhcpServerConfigPoolNtpServer2,
       "me1200DhcpServerConfigPoolNtpServer3": me1200DhcpServerConfigPoolNtpServer3,
       "me1200DhcpServerConfigPoolNtpServer4": me1200DhcpServerConfigPoolNtpServer4,
       "me1200DhcpServerConfigPoolNetbiosNodeType": me1200DhcpServerConfigPoolNetbiosNodeType,
       "me1200DhcpServerConfigPoolNetbiosScope": me1200DhcpServerConfigPoolNetbiosScope,
       "me1200DhcpServerConfigPoolNetbiosNameServer1": me1200DhcpServerConfigPoolNetbiosNameServer1,
       "me1200DhcpServerConfigPoolNetbiosNameServer2": me1200DhcpServerConfigPoolNetbiosNameServer2,
       "me1200DhcpServerConfigPoolNetbiosNameServer3": me1200DhcpServerConfigPoolNetbiosNameServer3,
       "me1200DhcpServerConfigPoolNetbiosNameServer4": me1200DhcpServerConfigPoolNetbiosNameServer4,
       "me1200DhcpServerConfigPoolNisDomainName": me1200DhcpServerConfigPoolNisDomainName,
       "me1200DhcpServerConfigPoolNisServer1": me1200DhcpServerConfigPoolNisServer1,
       "me1200DhcpServerConfigPoolNisServer2": me1200DhcpServerConfigPoolNisServer2,
       "me1200DhcpServerConfigPoolNisServer3": me1200DhcpServerConfigPoolNisServer3,
       "me1200DhcpServerConfigPoolNisServer4": me1200DhcpServerConfigPoolNisServer4,
       "me1200DhcpServerConfigPoolClientIdentifierType": me1200DhcpServerConfigPoolClientIdentifierType,
       "me1200DhcpServerConfigPoolClientIdentifierFqdn": me1200DhcpServerConfigPoolClientIdentifierFqdn,
       "me1200DhcpServerConfigPoolClientIdentifierMac": me1200DhcpServerConfigPoolClientIdentifierMac,
       "me1200DhcpServerConfigPoolClientHardwareAddress": me1200DhcpServerConfigPoolClientHardwareAddress,
       "me1200DhcpServerConfigPoolClientName": me1200DhcpServerConfigPoolClientName,
       "me1200DhcpServerConfigPoolVendorClassId1": me1200DhcpServerConfigPoolVendorClassId1,
       "me1200DhcpServerConfigPoolVendorSpecificInfo1": me1200DhcpServerConfigPoolVendorSpecificInfo1,
       "me1200DhcpServerConfigPoolVendorClassId2": me1200DhcpServerConfigPoolVendorClassId2,
       "me1200DhcpServerConfigPoolVendorSpecificInfo2": me1200DhcpServerConfigPoolVendorSpecificInfo2,
       "me1200DhcpServerConfigPoolVendorClassId3": me1200DhcpServerConfigPoolVendorClassId3,
       "me1200DhcpServerConfigPoolVendorSpecificInfo3": me1200DhcpServerConfigPoolVendorSpecificInfo3,
       "me1200DhcpServerConfigPoolVendorClassId4": me1200DhcpServerConfigPoolVendorClassId4,
       "me1200DhcpServerConfigPoolVendorSpecificInfo4": me1200DhcpServerConfigPoolVendorSpecificInfo4,
       "me1200DhcpServerConfigPoolAction": me1200DhcpServerConfigPoolAction,
       "me1200DhcpServerConfigPoolTableRowEditor": me1200DhcpServerConfigPoolTableRowEditor,
       "me1200DhcpServerConfigPoolTableRowEditorPoolName": me1200DhcpServerConfigPoolTableRowEditorPoolName,
       "me1200DhcpServerConfigPoolTableRowEditorPoolType": me1200DhcpServerConfigPoolTableRowEditorPoolType,
       "me1200DhcpServerConfigPoolTableRowEditorIpv4Address": me1200DhcpServerConfigPoolTableRowEditorIpv4Address,
       "me1200DhcpServerConfigPoolTableRowEditorSubnetMask": me1200DhcpServerConfigPoolTableRowEditorSubnetMask,
       "me1200DhcpServerConfigPoolTableRowEditorSubnetBroadcast": me1200DhcpServerConfigPoolTableRowEditorSubnetBroadcast,
       "me1200DhcpServerConfigPoolTableRowEditorLeaseDay": me1200DhcpServerConfigPoolTableRowEditorLeaseDay,
       "me1200DhcpServerConfigPoolTableRowEditorLeaseHour": me1200DhcpServerConfigPoolTableRowEditorLeaseHour,
       "me1200DhcpServerConfigPoolTableRowEditorLeaseMinute": me1200DhcpServerConfigPoolTableRowEditorLeaseMinute,
       "me1200DhcpServerConfigPoolTableRowEditorDomainName": me1200DhcpServerConfigPoolTableRowEditorDomainName,
       "me1200DhcpServerConfigPoolTableRowEditorDefaultRouter1": me1200DhcpServerConfigPoolTableRowEditorDefaultRouter1,
       "me1200DhcpServerConfigPoolTableRowEditorDefaultRouter2": me1200DhcpServerConfigPoolTableRowEditorDefaultRouter2,
       "me1200DhcpServerConfigPoolTableRowEditorDefaultRouter3": me1200DhcpServerConfigPoolTableRowEditorDefaultRouter3,
       "me1200DhcpServerConfigPoolTableRowEditorDefaultRouter4": me1200DhcpServerConfigPoolTableRowEditorDefaultRouter4,
       "me1200DhcpServerConfigPoolTableRowEditorDnsServer1": me1200DhcpServerConfigPoolTableRowEditorDnsServer1,
       "me1200DhcpServerConfigPoolTableRowEditorDnsServer2": me1200DhcpServerConfigPoolTableRowEditorDnsServer2,
       "me1200DhcpServerConfigPoolTableRowEditorDnsServer3": me1200DhcpServerConfigPoolTableRowEditorDnsServer3,
       "me1200DhcpServerConfigPoolTableRowEditorDnsServer4": me1200DhcpServerConfigPoolTableRowEditorDnsServer4,
       "me1200DhcpServerConfigPoolTableRowEditorNtpServer1": me1200DhcpServerConfigPoolTableRowEditorNtpServer1,
       "me1200DhcpServerConfigPoolTableRowEditorNtpServer2": me1200DhcpServerConfigPoolTableRowEditorNtpServer2,
       "me1200DhcpServerConfigPoolTableRowEditorNtpServer3": me1200DhcpServerConfigPoolTableRowEditorNtpServer3,
       "me1200DhcpServerConfigPoolTableRowEditorNtpServer4": me1200DhcpServerConfigPoolTableRowEditorNtpServer4,
       "me1200DhcpServerConfigPoolTableRowEditorNetbiosNodeType": me1200DhcpServerConfigPoolTableRowEditorNetbiosNodeType,
       "me1200DhcpServerConfigPoolTableRowEditorNetbiosScope": me1200DhcpServerConfigPoolTableRowEditorNetbiosScope,
       "me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer1": me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer1,
       "me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer2": me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer2,
       "me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer3": me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer3,
       "me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer4": me1200DhcpServerConfigPoolTableRowEditorNetbiosNameServer4,
       "me1200DhcpServerConfigPoolTableRowEditorNisDomainName": me1200DhcpServerConfigPoolTableRowEditorNisDomainName,
       "me1200DhcpServerConfigPoolTableRowEditorNisServer1": me1200DhcpServerConfigPoolTableRowEditorNisServer1,
       "me1200DhcpServerConfigPoolTableRowEditorNisServer2": me1200DhcpServerConfigPoolTableRowEditorNisServer2,
       "me1200DhcpServerConfigPoolTableRowEditorNisServer3": me1200DhcpServerConfigPoolTableRowEditorNisServer3,
       "me1200DhcpServerConfigPoolTableRowEditorNisServer4": me1200DhcpServerConfigPoolTableRowEditorNisServer4,
       "me1200DhcpServerConfigPoolTableRowEditorClientIdentifierType": me1200DhcpServerConfigPoolTableRowEditorClientIdentifierType,
       "me1200DhcpServerConfigPoolTableRowEditorClientIdentifierFqdn": me1200DhcpServerConfigPoolTableRowEditorClientIdentifierFqdn,
       "me1200DhcpServerConfigPoolTableRowEditorClientIdentifierMac": me1200DhcpServerConfigPoolTableRowEditorClientIdentifierMac,
       "me1200DhcpServerConfigPoolTableRowEditorClientHardwareAddress": me1200DhcpServerConfigPoolTableRowEditorClientHardwareAddress,
       "me1200DhcpServerConfigPoolTableRowEditorClientName": me1200DhcpServerConfigPoolTableRowEditorClientName,
       "me1200DhcpServerConfigPoolTableRowEditorVendorClassId1": me1200DhcpServerConfigPoolTableRowEditorVendorClassId1,
       "me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1": me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1,
       "me1200DhcpServerConfigPoolTableRowEditorVendorClassId2": me1200DhcpServerConfigPoolTableRowEditorVendorClassId2,
       "me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2": me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2,
       "me1200DhcpServerConfigPoolTableRowEditorVendorClassId3": me1200DhcpServerConfigPoolTableRowEditorVendorClassId3,
       "me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3": me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3,
       "me1200DhcpServerConfigPoolTableRowEditorVendorClassId4": me1200DhcpServerConfigPoolTableRowEditorVendorClassId4,
       "me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4": me1200DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4,
       "me1200DhcpServerConfigPoolTableRowEditorAction": me1200DhcpServerConfigPoolTableRowEditorAction,
       "me1200DhcpServerStatus": me1200DhcpServerStatus,
       "me1200DhcpServerStatusDeclinedTable": me1200DhcpServerStatusDeclinedTable,
       "me1200DhcpServerStatusDeclinedEntry": me1200DhcpServerStatusDeclinedEntry,
       "me1200DhcpServerStatusDeclinedEntryNo": me1200DhcpServerStatusDeclinedEntryNo,
       "me1200DhcpServerStatusDeclinedIpv4Address": me1200DhcpServerStatusDeclinedIpv4Address,
       "me1200DhcpServerStatusStatistics": me1200DhcpServerStatusStatistics,
       "me1200DhcpServerStatusStatisticsDiscoverCnt": me1200DhcpServerStatusStatisticsDiscoverCnt,
       "me1200DhcpServerStatusStatisticsOfferCnt": me1200DhcpServerStatusStatisticsOfferCnt,
       "me1200DhcpServerStatusStatisticsRequestCnt": me1200DhcpServerStatusStatisticsRequestCnt,
       "me1200DhcpServerStatusStatisticsAckCnt": me1200DhcpServerStatusStatisticsAckCnt,
       "me1200DhcpServerStatusStatisticsNakCnt": me1200DhcpServerStatusStatisticsNakCnt,
       "me1200DhcpServerStatusStatisticsDeclineCnt": me1200DhcpServerStatusStatisticsDeclineCnt,
       "me1200DhcpServerStatusStatisticsReleaseCnt": me1200DhcpServerStatusStatisticsReleaseCnt,
       "me1200DhcpServerStatusStatisticsInformCnt": me1200DhcpServerStatusStatisticsInformCnt,
       "me1200DhcpServerStatusBindingTable": me1200DhcpServerStatusBindingTable,
       "me1200DhcpServerStatusBindingEntry": me1200DhcpServerStatusBindingEntry,
       "me1200DhcpServerStatusBindingIpAddress": me1200DhcpServerStatusBindingIpAddress,
       "me1200DhcpServerStatusBindingState": me1200DhcpServerStatusBindingState,
       "me1200DhcpServerStatusBindingType": me1200DhcpServerStatusBindingType,
       "me1200DhcpServerStatusBindingPoolName": me1200DhcpServerStatusBindingPoolName,
       "me1200DhcpServerStatusBindingServerId": me1200DhcpServerStatusBindingServerId,
       "me1200DhcpServerStatusBindingVlanId": me1200DhcpServerStatusBindingVlanId,
       "me1200DhcpServerStatusBindingSubnetMask": me1200DhcpServerStatusBindingSubnetMask,
       "me1200DhcpServerStatusBindingClientIdentifierType": me1200DhcpServerStatusBindingClientIdentifierType,
       "me1200DhcpServerStatusBindingClientIdentifierFqdn": me1200DhcpServerStatusBindingClientIdentifierFqdn,
       "me1200DhcpServerStatusBindingClientIdentifierMac": me1200DhcpServerStatusBindingClientIdentifierMac,
       "me1200DhcpServerStatusBindingMacAddress": me1200DhcpServerStatusBindingMacAddress,
       "me1200DhcpServerStatusBindingLease": me1200DhcpServerStatusBindingLease,
       "me1200DhcpServerStatusBindingTimeToExpire": me1200DhcpServerStatusBindingTimeToExpire,
       "me1200DhcpServerControl": me1200DhcpServerControl,
       "me1200DhcpServerControlStatistics": me1200DhcpServerControlStatistics,
       "me1200DhcpServerControlStatisticsClear": me1200DhcpServerControlStatisticsClear,
       "me1200DhcpServerControlBinding": me1200DhcpServerControlBinding,
       "me1200DhcpServerControlBindingClearByIp": me1200DhcpServerControlBindingClearByIp,
       "me1200DhcpServerControlBindingClearByType": me1200DhcpServerControlBindingClearByType,
       "me1200DhcpServerMIBConformance": me1200DhcpServerMIBConformance,
       "me1200DhcpServerMIBCompliances": me1200DhcpServerMIBCompliances,
       "me1200DhcpServerMIBCompliance": me1200DhcpServerMIBCompliance,
       "me1200DhcpServerMIBGroups": me1200DhcpServerMIBGroups,
       "me1200DhcpServerConfigGlobalsInfoGroup": me1200DhcpServerConfigGlobalsInfoGroup,
       "me1200DhcpServerConfigVlanTableInfoGroup": me1200DhcpServerConfigVlanTableInfoGroup,
       "me1200DhcpServerConfigExcludedTableInfoGroup": me1200DhcpServerConfigExcludedTableInfoGroup,
       "me1200DhcpServerConfigExcludedIpTableRowEditorInfoGroup": me1200DhcpServerConfigExcludedIpTableRowEditorInfoGroup,
       "me1200DhcpServerConfigPoolTableInfoGroup": me1200DhcpServerConfigPoolTableInfoGroup,
       "me1200DhcpServerConfigPoolTableRowEditorInfoGroup": me1200DhcpServerConfigPoolTableRowEditorInfoGroup,
       "me1200DhcpServerStatusDeclinedTableInfoGroup": me1200DhcpServerStatusDeclinedTableInfoGroup,
       "me1200DhcpServerStatusStatisticsInfoGroup": me1200DhcpServerStatusStatisticsInfoGroup,
       "me1200DhcpServerStatusBindingTableInfoGroup": me1200DhcpServerStatusBindingTableInfoGroup,
       "me1200DhcpServerControlStatisticsInfoGroup": me1200DhcpServerControlStatisticsInfoGroup,
       "me1200DhcpServerControlBindingInfoGroup": me1200DhcpServerControlBindingInfoGroup}
)
